### [WOFF 1.0: a milestone on W3C’s journey of fonts on the web | 2026 | Blog | W3C](https://www.w3.org/blog/2026/woff-1-0-a-milestone-on-w3cs-journey-of-fonts-on-the-web/)

**原文标题**: [WOFF 1.0: a milestone on W3C’s journey of fonts on the web | 2026 | Blog | W3C](https://www.w3.org/blog/2026/woff-1-0-a-milestone-on-w3cs-journey-of-fonts-on-the-web/)

WOFF 1.0 的发布是 W3C 在网页字体领域的关键里程碑，它通过无 DRM 的压缩格式解决了许可与技术争议，推动了网页字体的广泛采用，并为后续 WOFF 2.0 和增量字体传输（IFT）的发展奠定了基础。

- 🖥️ 1990 年代 W3C 已开始探索网页字体，并定义了 `@font-face`，但因许可和加密争议未能普及。
- 🤝 2009 年 Mozilla 的 ZOT 格式与 typographer 的 .webfont 格式合并，催生了 WOFF 雏形，放弃 DRM 和根字符串。
- 📜 2010 年 7 月 27 日 WOFF 1.0 首份公开工作草案发布，成为无 DRM、可广泛实施的字体格式。
- 📈 从 2011 年接近零使用率到 2020 年全球 80% 网站使用网页字体，WOFF 1.0 推动了爆发式增长。
- ⚡ WOFF 2.0（2014 年草案）通过更优压缩（Brotli）实现高达 40% 更小文件，2025 年占字体请求约 65%。
- 🏆 2022 年 WOFF 相关工作获艾美奖，表彰其在网页和电视设备字体标准化中的贡献。
- 🔮 当前 Web Fonts 工作组聚焦增量字体传输（IFT），可部分下载字体字节，解决中文、日韩文等大字符集及慢网络的延迟问题。

---

### [Web 字体：基本原理，1996](https://www.w3.org/TR/font-rationale/)

**原文标题**: [Fonts for the Web: Rationale, 1996](https://www.w3.org/TR/font-rationale/)

该文档是 W3C 于 1996 年制定的 Web 字体需求文档，2022 年作为历史记录发布。它记录了早期 Web 字体工作组的目标、场景与术语，并回顾了影响深远的技术决策与时代局限。

- 📜 **历史背景**：1996 年 W3C 研讨会催生 Web 字体工作组，1997 年提出`@font-face`，1998 年并入 CSS2，但可依赖的 Web 字体（WOFF）直至 2010 年才普及。
- 🎯 **核心目标**：要求开放框架、支持 HTML 与非 HTML、快速发布、动态生成、文档本地字体、IPR 保护、最小网络流量、渐进布局、按名称选字体、字体数据访问、字体合成/替换、跨平台、减少图片替代文本、不强制购买新字体、支持连字与上下文形式。
- 🔒 **许可与 IPR**：当时认为 Web 使用字体近乎盗版，许可条款模糊；后来 WOFF 携带许可链接，催生清晰印刷/Web 许可区分，自由字体（如 OFL）兴起。
- 🔗 **链接机制**：CSS-based 链接最终成为主流，但早期也有 HTML `<link>` 方案；数十年后 HTML 预加载机制再次浮现。
- ✂️ **字符与字形**：文档明确区分字符与字形，连字等应由字体引擎处理而非 HTML 内容；此区分对后续 OpenType 特性在 CSS 中应用至关重要。
- 🛠️ **字体合成与替换**：因早期网速慢，字体合成/替换受重视，但实际困难超出预期；后随网速提升，重点转向直接下载正确字体。
- 🏷️ **按名称选择字体**：目标是建立字体族、字重等继承模型（CSS1/2 方式），而非在每个元素上指定完整字体面。
- 💾 **缓存与隐私**：积极缓存以减少延迟，但现代安全（跨站脚本）与隐私保护实践削弱了缓存的效益。
- 🅰️ **可变字体先兆**：文档提及 TrueType GX，预示后来可变字体在响应式设计中的重要性。

---

### [适用于任何规模的时间序列工作负载的 Postgres。| Tiger Data](https://www.tigerdata.com/go/trial?utm_source=content-syndication&utm_medium=referral&utm_campaign=frontend-focus-newsletter)

**原文标题**: [Postgres for time-series workloads at any scale. | Tiger Data](https://www.tigerdata.com/go/trial?utm_source=content-syndication&utm_medium=referral&utm_campaign=frontend-focus-newsletter)

Tiger Cloud 提供可处理任何规模时间序列负载的 Postgres 服务，具备超大规模处理能力（每天 3 万亿指标、3PB 数据、1 千万亿数据点），并提供免费试用额度及企业级功能。

- 🚀 超大规模处理：每天处理 3 万亿指标、存储 3PB 数据、支持 1 千万亿数据点
- 💰 免费试用：新用户注册即获$1000 信用额度，30 天有效，无需信用卡
- 🔄 弹性扩展：支持读写分离，最多 10 个节点副本集，配合分层 SSD/S3 实现无限且经济的存储
- 💸 按需付费：计算与存储分离，独立扩展，不浪费闲置容量
- 🔒 高可用：多可用区集群，自动故障切换、时间点恢复及跨区域备份
- 🏢 企业级安全：SOC 2、HIPAA、GDPR 合规，始终开启加密、SSO、RBAC 及审计日志
- 📊 深度可观测性：查询下钻与仪表盘，可发送指标到 CloudWatch、Datadog、Prometheus
- ⚡ 快速部署：几分钟内创建数据库，支持 SQL、CLI、Terraform、Cursor 或 Claude Code 管理
- 🔌 广泛集成：支持主流云提供商及 Postgres 生态
- 🛡️ 企业支持：合同 SLA、区域数据隔离、24/7 全球专家支持及企业级响应保证

---

### [CSS Infinity Use Cases · July 25, 2026](https://nerdy.dev/css-infinity-use-cases)

**原文标题**: [CSS Infinity Use Cases · July 25, 2026](https://nerdy.dev/css-infinity-use-cases)

本文介绍了 CSS 中`infinity`（和`-infinity`）的多种妙用，从解决特定问题的优雅方法到有趣的创意玩法，覆盖了边框半径、动画、z-index、clamp、视图过渡、响应式设计、布尔逻辑等多个场景，并附带了基础语法说明。

- 🔵 圆与药丸：`border-radius: calc(infinity * 1px)` 一键实现完美圆角，无需再写超大数值。
- ❄️ 永久状态：`animation-duration: calc(infinity * 1s)` 让动画/过渡看似冻结，保持最终状态。
- 📈 最高 z-index：`z-index: calc(infinity)` 可达浏览器允许的最大整数 `2147483647`。
- 🚀 无限范围：`calc(infinity * 1px)` 用于移除 `clamp()` 的上下限，实现无天花板/地板效果。
- 🖼️ 冻结视图过渡：将 `::view-transition-*` 的 `animation-duration` 设为无限，暂停过渡以方便调试。
- 📱 响应式半径：结合 `clamp()` 和 `infinity`，根据视口或容器尺寸动态切换圆角（0px 或 20px）。
- 🔢 布尔逻辑：用 `clamp(0, (条件)*infinity, 1)` 将变量压成 0 或 1，驱动其他属性（如 flex-grow、字号）。
- 🎭 背景遮罩：借助 `box-shadow: 0 0 0 calc(infinity * 1px) #0005` 创建覆盖全屏的非交互背景。
- 🔄 滚动触发：设置 `timeline-trigger-activation-range-end: calc(infinity * 1px)` 使滚动过渡只进不退。

---

### [calc() keywords | Can I use... Support tables for HTML5, CSS3, etc](https://caniuse.com/wf-calc-constants)

**原文标题**: [calc() keywords | Can I use... Support tables for HTML5, CSS3, etc](https://caniuse.com/wf-calc-constants)

calc() 函数在全球浏览器中支持率为 91.38%，主流现代浏览器已全面支持，但部分旧版本浏览器仍不支持。

- 🌐 全球支持率高达 91.38%，但仍有少量浏览器不兼容。
- ✅ Chrome 110+、Firefox 114+、Safari 16.0+ 等现代版本均已支持。
- ❌ Edge 12-109、Firefox 2-113、Chrome 4-109、Safari 3.1-15.6 等旧版本不支持。
- ❌ UC Browser 15.5、QQ Browser 14.9、KaiOS 2.5-3 等浏览器完全不支持。
- ❓ Opera 10-12.1 及旧版 Android Browser 支持情况未知。
- ✅ 移动端 Chrome for Android 150、Firefox for Android 152、Samsung Internet 21+ 均支持。

---

### [CodePen 2.0 发布 – CodePen](https://blog.codepen.io/2026/07/23/two-point-oh/)

**原文标题**: [The Launch of CodePen 2.0 – CodePen](https://blog.codepen.io/2026/07/23/two-point-oh/)

概述：CodePen 2.0 正式发布，这是团队最具雄心的项目，重建在线编辑器以支持部署、文件系统、版本控制、实时协作等现代功能，并保持可扩展性以持续进化。

- 🎉 宣布 CodePen 2.0 正式发布，为开发者重建编辑器，支持所有经典功能并新增扩展能力。
- 🌐 每个 Pen 可一键部署为独立网站（*.codepen.app），支持自定义域名和自动更新。
- 📁 每个 Pen 拥有改良的真文件系统，支持多文件和多页面，可随时使用。
- ⏪ 提供版本系统，可随时回滚到任意历史状态。
- 👥 支持邀请任何人（用户名或邮箱）作为编辑者或查看者，实时协作编辑。
- 🧩 通过 Blocks 可任意组合技术（如 Tailwind、Vue、Nunjucks 等），无需手动配置。
- ♿ 屏幕阅读器可访问性大幅提升。
- 🎧 推出多个播客详细解读 2.0 特性（如模板、实时系统、版本集成等）。
- 🕰️ 项目开发数年，展示了从 2021 年起的早期原型、设计系统及界面演变。
- 🔮 未来计划：探索 AI 集成；经典编辑器仍可访问；将增加更多处理器（如 Tailwind、Lightning CSS 等）。
- 🔧 经典用户可用 Classic Block 和最小 UI 模式（快捷键 ⌘-U/Control-U）快速适应 2.0，并提升性能。

---

### [CodePen：用于构建与部署网站的在线代码编辑器](https://codepen.io/)

**原文标题**: [CodePen – Online Code Editor For Building & Deploying Websites](https://codepen.io/)

CodePen 是面向设计师和开发者的在线开发环境，集成常用前端工具并提供从编写、预览到部署的一体化工作流。

- 🧰 支持 Sass、Vue、TypeScript、Prettier 等工具，无需本地安装即可开始编写代码。
- ⚡ 内置编译器会处理代码和资源，提供接近实时的预览反馈。
- 📁 可用文件、文件夹和模板组织完整网站，而不仅限于单个 HTML、CSS、JS 片段。
- 🤝 提供版本记录、协作、诊断、隐私控制和资源托管，便于展示、调试与分享作品。
- 🚀 任意 Pen 可一键发布为网站，减少部署和域名配置的门槛。

---

### [消灭 Cookie 横幅！](https://killthecookiebanner.eu/)

**原文标题**: [Kill the Cookie Banner!](https://killthecookiebanner.eu/)

欧盟委员会提议通过浏览器自动信号消除误导性 Cookie 横幅，但跟踪行业游说反对，导致提案受阻。现呼吁公众联系代表支持改革。

- 🔔 Cookie 横幅被设计成误导和烦人的形式，让高达 90% 的人被迫同意跟踪，而只有 3% 的人自愿被跟踪，系统本质上有缺陷。
- 🏛️ 欧盟委员会在 2025 年秋季提出改革方案：通过浏览器自动发送隐私偏好信号（接受、拒绝或限制跟踪），从而永久告别 Cookie 横幅。
- 🕵️ 跟踪行业（以谷歌为首）拼命游说，多个成员国和欧洲议会正在阻挠这一简单有效的解决方案，担心降低跟踪同意率。
- 💌 欢迎你采取行动：联系欧洲议会或成员国的代表，表达对 Cookie 横幅的不满，支持自动信号提案。
- ⚠️ 该提案是“Digital Omnibus”改革的一部分，其他内容可能削弱用户权利，但消灭 Cookie 横幅的部分值得支持。
- 🤝 该倡议由欧洲多家民间组织发起，欢迎更多组织加入。

---

### [NOYB 每天维护你的隐私权](https://noyb.eu/en)

**原文标题**: [NOYB enforces your right to privacy everyday](https://noyb.eu/en)

以下是对您提供的新闻摘要的概述和要点总结：

概述总结：近期一系列关于 GDPR 和数据隐私的新闻，涉及 Cookie 横幅滥用、欧美数据传输危机、企业“付费或同意”模式、信用评分诉讼等，部分投诉已获成功。

- 🍪 dict.cc 要求用户“同意”1741 家合作伙伴追踪，引发 GDPR 投诉。
- 🇺🇸 美国最高法院裁定 FTC 独立性受损，欧美数据传输面临重大挑战。
- 🛑 欧盟委员会提议取消 Cookie 横幅，却遭部分成员国及 Google 反对。
- 📉 奥地利信用机构 CRIF 被指秘密评分，noyb 发起集体诉讼。
- 🔄 北欧媒体巨头 Schibsted 推行“付费或同意”模式，遭投诉。
- ✅ noyb 成功促使 ORF.at 更正其误导性 Cookie 横幅。

---

### [为未来设计 Firefox](https://blog.mozilla.org/en/firefox/new-firefox-design/)

**原文标题**: [Designing Firefox for the future](https://blog.mozilla.org/en/firefox/new-firefox-design/)

Mozilla 正在以 Project Nova 为内部代号更新 Firefox 的设计系统，目标是在保留熟悉感的同时，让浏览器更统一、私密、快速且易于个性化。

- 🎨 新设计将统一标签页、面板、设置和图标的视觉语言，采用更柔和的形状、暖色调与更清晰的间距。
- 🔒 隐私功能会更易发现和配置，包括内置 VPN、隐私浏览、AI 功能开关与增强型跟踪保护。
- ⚡ Firefox 优先呈现关键页面内容，并表示近一年关键内容加载时间已有改善。
- 🧩 标签组、分屏、垂直标签和紧凑模式等效率功能会更便于使用。
- 🖼️ 新主题、壁纸和无障碍设计将加强跨设备的一致性与可定制性。

---

### [在 Firefox Nightly 中试用新设计](https://blog.nightly.mozilla.org/2026/07/27/new-firefox-design/)

**原文标题**: [Try the New Firefox Design in Nightly – Firefox Nightly News](https://blog.nightly.mozilla.org/2026/07/27/new-firefox-design/)

Firefox Nightly 已开放试用下一代界面设计，让用户在正式版更广泛发布前体验变化并反馈问题。

- 🧭 新界面整合了更柔和的标签页、暖色调、更新的图标、紧凑模式和主题选项。
- 🧪 Mozilla 希望测试者重点检查图标与间距、个性化、窗口缩放、键盘导航、读屏器及不同语言布局。
- 🐞 如发现视觉或功能异常，可在 Bugzilla 提交复现步骤、截图或录屏以及系统和 Nightly 版本信息。
- 📅 设计仍会在未来数周持续打磨，之后再向更广泛的 Firefox 用户推出。

---

### [Download and test future releases of Firefox for desktop, Android and iOS.
 — Firefox.com](https://www.firefox.com/en-GB/channel/desktop/#nightly)

**原文标题**: [
  Download and test future releases of Firefox for desktop, Android and iOS.
 — Firefox.com](https://www.firefox.com/en-GB/channel/desktop/#nightly)

Firefox 提供多个预发布版本供用户尝鲜，包括 Nightly、Beta 和 Developer Edition，每个版本适用于不同平台，部分旧系统需改用 ESR 版本，所有预发布版本默认会向 Mozilla 发送数据以协助改进。

- 🌙 **Nightly 频道**：每日更新一至两次，让用户率先体验下一代 Web 浏览器，并帮助改进其性能。
- 🧪 **Beta 频道**：在更稳定的预发布构建中测试即将推出的功能，适合希望提前体验但又追求相对稳定的用户。
- 🛠️ **Developer Edition 频道**：专为开发者打造，集成构建、测试、扩展等工具，仅限开发者使用。
- 🖥️ **多平台支持**：提供 Windows（32/64 位、ARM64）、macOS、Linux（64 位、ARM64）等版本，以及 MSI 安装包。
- ⚠️ **旧系统限制**：Windows 8.1 及以下、macOS 10.14 及以下不再支持 Beta、Developer Edition 和 Nightly，需改用 Firefox ESR。
- 📊 **数据共享**：所有预发布版本默认发送使用数据至 Mozilla 及其合作伙伴，用于发现问题与优化功能。
- 🔗 **其他资源**：提供隐私声明、发行说明、所有语言及平台版本下载，Debian/Ubuntu 用户可通过 APT 仓库安装。
- 📬 **订阅更新**：可在页面底部输入邮箱及国家/地区，订阅 Firefox 相关资讯，需同意使用条款和隐私政策。

---

### [Safari 26.6 的 WebKit 功能 | WebKit](https://webkit.org/blog/18178/webkit-features-for-safari-26-6/)

**原文标题**: [  WebKit Features for Safari 26.6 | WebKit](https://webkit.org/blog/18178/webkit-features-for-safari-26-6/)

Safari 26.6 发布，改进了 WebAssembly 流式编译并修复了八项 Bug，涵盖 CSS、Service Workers、网络、扩展和 WebRTC 等领域。

- 🧩 WebAssembly 的 `compileStreaming()` 与 `instantiateStreaming()` 新增 `compileOptions` 参数，支持在流式编译中启用 JS String Builtins。
- 🎨 修复了三项 CSS 问题：`ic` 长度单位在页面缩放时错误、固定定位元素使用 `position-area` 时后备失败、CSS `zoom` 与字体属性在 iPad 桌面网站模式下的交互异常。
- 🌐 修复了分区 Cookie 无法通过 `WKHTTPCookieStore` 删除的网络问题。
- 👷 两项 Service Worker 修复：主脚本缺失时注册未自动注销导致无法重新注册、导入脚本缺失时同样未自动注销。
- 🧩 修复了 Web 扩展每次启动时服务 Worker 注册数据库文件累积导致的性能下降。
- 📞 修复了 `RTCPeerConnection` 配置 `iceTransportPolicy: "relay"` 后在 macOS Sequoia 上无法收集 ICE 候选的问题。

---

### [立即下载适用于 Arm64 Linux 的 Google Chrome](https://www.omgubuntu.co.uk/2026/07/chrome-arm64-linux-available)

**原文标题**: [Download Google Chrome for Arm64 Linux now](https://www.omgubuntu.co.uk/2026/07/chrome-arm64-linux-available)

Google 为 Arm64 Linux 设备（包括树莓派）提供了官方 Chrome 构建版，目前可通过修改下载链接获取，并已支持账户同步与部分媒体播放功能，但仍有 DRM 限制。

- 🐧 谷歌为 Arm64 Linux 设备（如树莓派、骁龙 X 笔记本等）推出了官方 Chrome Arm64 构建版，当前可通过将下载链接中的 "amd64" 改为 "arm64" 获取。
- 🖥️ 在树莓派 5 的 Ubuntu 上成功安装 Chrome v150 稳定版，支持 Google 账户同步，可同步扩展、书签、密码和设置。
- 🎞️ 包含原生 Widevine DRM 模块，但 Linux 下为“软件安全”模式，流媒体最高支持 1080p，无法实现 4K 或 HDR。
- 🚀 YouTube 2K 播放流畅（无硬件解码），BBC iPlayer 最高画质播放流畅，优于 Firefox Snap 在 Arm64 上的表现。
- ⚠️ 目前该构建版本尚未正式公告，可能不够稳定，Chrome 下载页面仍默认提供 AMD64 版本，需用户手动调整链接。

---

### [网站的未来 · Joost.blog](https://joost.blog/future-of-the-website/)

**原文标题**: [The future of the website · Joost.blog](https://joost.blog/future-of-the-website/)

网站的未来：从单纯的人类浏览界面，进化为同时服务人类和 AI 代理、可验证、多接口的业务中枢。技术完美成为选择，真实性成为唯一护城河，转化行为逐渐离开网站。

- 🤖 网站需为 AI 代理优化：网站内容不仅要适合人类，还要提供易于机器解析的表面，避免重蹈 m-dot 或 AMP 的覆辙，应维持单一数据源与多渲染输出。
- 🛠️ 技术完美是可选项：过去需要罕见专业知识的网站技术完善，现在可通过工具自动完成，技术优势正变为基准线，真正价值转向机器无法回答的问题。
- 📊 网站重要性因业务而异：对本地服务商（如水管工）网站非必需；对品牌而言，网站比实体店铺更重要，能触达全球客户。
- 🔗 网站成为接口组合：除 HTML 外，还应提供 MCP 服务器、命令行客户端等接口，让 AI 代理能直接交互、下单、预约，标准会变但趋势不变。
- 🛒 转化离开网站：更多购买决策发生在 AI 问答、聊天界面等场景，网站角色转为权威事实源（系统记录），为各决策表面提供可靠数据。
- 🔒 真实性是唯一护城河：AI 生成内容充斥，唯有真实（真实工作、真实人、真实评价）才有价值。代理可交叉验证，真实需可查证，网站需与其他网络存在联动体现身份、来源和信任。
- 🏠 网站是业务的可验证大本营：它服务多种表面、接受代理指令、证明业务真实，同时仍接待人类访客。成功的网站需技术优秀、易于代理访问、并保持无可替代的真实性。

---

### [当你需要制作三角形时，想想圆锥渐变 – Master.dev 博客](https://master.dev/blog/when-you-need-to-make-a-triangle-think-conic-gradients/)

**原文标题**: [When You Need To Make a Triangle, Think Conic Gradients – Master.dev Blog](https://master.dev/blog/when-you-need-to-make-a-triangle-think-conic-gradients/)

conic-gradient() 在 CSS 中其实很有用，尤其通过设置硬色标、移动中心点、调整起始角度，可以轻松创建三角形，并带来更多控制力。

- 🎨 conic-gradient() 的硬色标能做出饼图或扇形，但更推荐用 SVG 实现交互
- 🔄 移动渐变中心点（如移到左下角）可产生向外辐射的射线效果
- 📐 通过设置起始角度（如 from 0.25turn at 0 0）和色标角度，可精准绘制三角形
- 🔺 相比线性渐变，圆锥渐变在控制角度和三角形时更直观，尤其用于导航三角形等场景
- 🛠️ 创建三角形还有众多其他方法：边框法、clip-path、border-shape、SVG、Canvas、skew 变换等
- 📚 文中推广了 CSS 学习路径，涵盖基础到高级布局，并提供 20% 折扣

---

### [Measuring Component Performance with the Container Timing API – CSS Wizardry](https://csswizardry.com/2026/07/meaasuring-component-performance-with-the-container-timing-api/)

**原文标题**: [Measuring Component Performance with the Container Timing API – CSS Wizardry](https://csswizardry.com/2026/07/meaasuring-component-performance-with-the-container-timing-api/)

Container Timing API 是一种实验性的性能指标，让开发者能够测量整个 DOM 子树（如产品卡片、搜索结果区域）的内容渲染过程，而不是单个元素。它通过 `containertiming` 属性标记组件，并利用 `PerformanceObserver` 获取多次内容绘制的更新，从而揭示组件逐步呈现的“形状”，解决了传统指标无法反映自定义组件是否对用户可见的问题。

- 📦 **解决的问题**：LCP、Element Timing 等通用指标无法准确反映如“购买框”或“搜索结果网格”等自定义组件的渲染完成情况，Container Timing 允许定义组件边界并跟踪其内容绘制的进程。
- ⚙️ **工作原理**：在组件根元素上添加 `containertiming="your-identifier"` 属性，然后通过 `PerformanceObserver` 监听 `container` 类型的条目，获取 `firstRenderTime`、`startTime`、`size`、`lastPaintedElement` 等属性，反映新内容绘制的时间与区域增长。
- 🧩 **与 Element Timing 的区别**：Element Timing 关注单个元素（如图片或文本）的渲染时间；Container Timing 关注整个子树的内容累积，提供逐步的绘制序列而非单一时间点，更适合衡量用户认知中的“组件就绪”。
- 🔬 **实际应用场景**：适合电商产品详情页、搜索结果列表、仪表板小部件、出版商首页等，这些组件由多个独立部分构成，且当前难以用标准指标衡量；也可用于团队级性能契约。
- ⏳ **组件“完成”的陷阱**：浏览器无法知道组件是否还会有更多内容（如懒加载、动态更新），因此 API 不会提供“完成”事件，而是输出一系列更新，需要开发者根据业务定义（如首次渲染、最终面积增长）来解读。
- ⚠️ **不是新 Core Web Vital**：Container Timing 不是替代 LCP 的官方指标，也不是“组件可用”指标（它只测量绘制，不测量交互性、数据加载或 JavaScript 就绪），需谨慎命名最终指标。
- 🌐 **浏览器支持与试用**：目前是 Chrome 148-153 的 Origin Trial，可在 flags 或 token 启用；Firefox 已有正面立场，WebKit 待定；建议在重要组件上采样使用，并注意分析偏差（仅 Chromium 数据）。

---

### [Container Timing origin trial  |  Blog  |  Chrome for Developers](https://developer.chrome.com/blog/container-timing-origin-trial)

**原文标题**: [Container Timing origin trial  |  Blog  |  Chrome for Developers](https://developer.chrome.com/blog/container-timing-origin-trial)

Chrome 正在推出 Container Timing API 的起源试验，它扩展了 Element Timing，用于测量整个内容容器（如组件、部件）的加载时间，帮助开发者更精确地了解页面各部分的渲染性能。

- 📦 **Container Timing 是什么**：一种性能 API，通过添加 `containertiming` 属性标记 HTML 容器，使用 `PerformanceObserver` 监听容器内元素首次渲染和最新绘制的时间，提供比 LCP 更细粒度的组件级加载指标。
- 🧩 **工作原理**：为容器内的每个元素记录首次内容绘制（类似 LCP），后续用户交互导致的非内容更新不会触发新条目；可通过 `containertiming-ignore` 属性忽略子容器。
- 🚀 **启用方式**：从 Chrome 148 起可通过注册起源试验 token 启用，此前可在 Chrome 147 中使用 `chrome://flags` 标志或命令行启用。
- 🎯 **最佳实践**：尽早添加 `containertiming` 属性（最好在 HTML 中），使用有意义的标识符，仅测量关键容器（如英雄区、产品网格），忽略广告等不影响核心指标的元素。
- 🛠️ **特性检测**：使用 `typeof PerformanceContainerTiming !== "undefined"` 检测支持，避免在 origin trial 期间因 `supportedEntryTypes` 冻结而误判。
- 💬 **反馈与开源**：API 由 Bloomberg 开发、Igalia 实现，已在 GitHub 上开放 issue 反馈，并有相关规范和技术实现文档。

---

### [GitHub - WICG/container-timing: 容器定时 · GitHub](https://github.com/WICG/container-timing)

**原文标题**: [GitHub - WICG/container-timing: Container Timing · GitHub](https://github.com/WICG/container-timing)

概览：Container Timing API 使开发者能够监控含有 `containertiming` 属性的 DOM 部分的首次显示和初始绘制完成时间，弥补了 Element Timing 的不足，为组件性能测量提供精确数据。

- 🚀 通过 `containertiming` 属性标记容器根元素，接收首次绘制和累计绘制区域的性能条目。
- 🖼️ `PerformanceContainerTiming` 包含 `startTime`、`intersectionRect`、`size`、`firstRenderTime`、`lastPaintedElement` 等信息。
- 🔧 使用 `containertimingignore` 属性可忽略 DOM 中的特定子树，避免影响测量。
- ⚠️ 必须在元素添加到文档前设置属性，否则只能获取后续事件。
- 🌐 目前仅在 Chrome Canary 中通过 flag 启用，支持 Origin Trial。
- 🔒 API 不跨 iframe 暴露信息，安全性良好。
- 📊 对比替代方案更高效：无需手动为每个元素添加 elementtiming，不阻塞渲染，避免 race condition。
- ❓ 有额外问题待解决：动态注册、深度限制、忽略块、用户输入停止跟踪等。

---

### [应该何时记录以及记录什么？ | Sentry 博客](https://blog.sentry.io/logging-best-practices/?utm_source=frontendfocus&utm_medium=paid-community&utm_campaign=logs-fy27q2-evergreen&utm_content=newsletter-sponsored-link-logging-blog-learnmore)

**原文标题**: [When and what should I be logging? | Sentry Blog](https://blog.sentry.io/logging-best-practices/?utm_source=frontendfocus&utm_medium=paid-community&utm_campaign=logs-fy27q2-evergreen&utm_content=newsletter-sponsored-link-logging-blog-learnmore)

本文介绍了日志记录的最佳实践，包括合适的日志内容、结构化写法、日志级别选择及需避免记录的数据，以帮助开发者更高效地调试和运营应用。

- 📝 记录重要运行时决策（如特征开关、用户分组），便于复现不同用户的行为差异。
- 🧩 记录功能或算法的中间步骤与最终结果，快速定位流程中的失败环节。
- 🔐 记录审计与访问事件（创建、更新、删除、权限等），用于排查支持案例和合规要求。
- 🐛 记录错误和失败的上文（如重试次数、状态码、运行时状态），配合 Sentry 的 Capture Error 使用。
- 🏗️ 使用结构化日志（键值对），包含用户、事件和时间的上下文，便于搜索和可视化。
- 🔗 随着请求演进累积上下文，如 Trace ID，关联分布式追踪。
- 📊 选择合适的日志级别：debug 用于诊断，info 用于正常事件，warn 用于可恢复问题，error 用于已处理的异常。
- ❌ 避免记录每个函数调用（应使用 profiling/tracing）。
- 🔒 避免记录 PII 及其他敏感信息，优先使用不透明用户 ID，遵守 GDPR、HIPAA 等法规。
- 💾 避免记录无特定目的的大数据块，权衡成本与风险，按需提取关键字段。
- 💡 日志可作为临时调试工具，添加后验证完毕可移除，不必永久保留。

---

### [Swapping a lightweight image for an animated SVG - Stuff & Nonsense](https://stuffandnonsense.co.uk/blog/swapping-a-lightweight-image-for-an-animated-svg/)

**原文标题**: [Swapping a lightweight image for an animated SVG - Stuff & Nonsense](https://stuffandnonsense.co.uk/blog/swapping-a-lightweight-image-for-an-animated-svg/)

该文章介绍了一种通过先加载轻量级静态 AVIF 图片，再在合适条件下替换为动画 SVG 以提升网页性能的方法，避免了初始加载时消耗过多带宽和解析资源。

- 🖼️ 动画 SVG 内联导致 HTML 臃肿，加载慢且占用带宽（可达半兆字节），影响首屏渲染。
- 🚀 解决方案：使用`<picture>`元素先加载静态 AVIF 图片作为占位，无 JavaScript 参与，消除布局偏移。
- ⚙️ 通过`data-`属性声明动画资源 URL 和触发条件（媒体查询），使 HTML 保持声明式，JavaScript 作为逐步增强。
- ⏳ 利用双重`requestAnimationFrame`确保首屏渲染后再异步获取动画，避免阻塞页面展示。
- 📡 仅当视口匹配媒体查询时，才通过`fetch`请求动画 HTML 片段，移动端不下载，节省流量。
- 🔄 使用`DOMParser`解析片段并用`DocumentFragment`一次性替换 DOM，支持响应式恢复：窗口变窄时自动切回静态图片。
- ✅ 该模式兼顾性能与体验：首屏快速显示、动画按需加载、可逆增强，是性能与个性的平衡。

---

### [Medium](https://tech.olx.com/handling-concurrency-on-the-web-with-web-locks-api-163b7e07eddd?gi=0328e7c36fc4)

**原文标题**: [Medium](https://tech.olx.com/handling-concurrency-on-the-web-with-web-locks-api-163b7e07eddd?gi=0328e7c36fc4)

概述总结：本文介绍了使用 Web Locks API 解决浏览器多标签页并发上传大文件时的重复上传问题，提供了从问题分析、同步原理解释到 React 实现方案的完整实践。

- 🚩 问题背景：用户同时打开多个标签页时，每个标签页都会尝试恢复同一个大文件上传，导致重复上传、浪费带宽和成本。
- 🔒 锁的机制：通过互斥锁确保共享资源一次只被一个调用者访问，防止竞态条件，借鉴银行账户同步场景。
- ❌ 传统方案缺陷：localStorage+ 轮询存在竞态和锁持久化问题；Broadcast Channel API 则需要手动实现状态机，容易出错。
- ✨ Web Locks API 优势：浏览器原生互斥锁，原子获取、自动释放、非阻塞、API 简单，兼容主流浏览器。
- 🛠️ 实现策略：用户发起的上传使用非阻塞锁（不阻塞用户）；恢复上传使用条件锁（仅获取锁的标签页执行恢复）。
- 🔧 关键实现：通过`holdLockUntilComplete`函数管理锁的生命周期，监听上传完成、错误、取消等事件自动释放锁，并提供降级方案。
- 📈 实际效果：零重复上传、用户体验提升、降低成本、代码更简洁。
- 💡 适用场景与注意事项：适用于文件上传、后台同步等单例操作；性能开销极小；需测试跨浏览器和异常情况。

---

### [Web 锁 API - Web API | MDN](https://developer.mozilla.org/en-US/docs/Web/API/Web_Locks_API)

**原文标题**: [Web Locks API - Web APIs | MDN](https://developer.mozilla.org/en-US/docs/Web/API/Web_Locks_API)

Web Locks API 允许不同标签页或 Web Worker 中的脚本通过异步锁机制协调对共享资源的访问，支持独占和共享模式，并提供监控与高级控制功能，已在多数浏览器中广泛可用。

- 🔒 锁由应用命名（如 `"my_net_db_sync"`），同一源下同一时刻只有一个独占锁持有者，或多个共享锁持有者共存
- 🌐 锁作用域限定于源（origin），不同源（如 `https://example.com` 与 `https://example.org:8080`）的锁互不干扰
- ⚙️ 使用 `navigator.locks.request()` 请求锁，回调中执行异步任务，任务完成后锁自动释放；该方法返回 Promise
- 📋 选项包括：`mode`（独占/共享）、`ifAvailable`（无法立即获得时回调 `null`）、`steal`（抢夺现有锁）、`signal`（通过 AbortSignal 中止请求）
- 🔍 通过 `navigator.locks.query()` 可获取当前源的锁状态快照（持有/排队请求及模式），便于调试
- ⏳ 高级用法：回调返回 Promise 可长时间持有锁，通过 `resolve`/`reject` 显式释放
- ⚠️ 死锁风险：多个锁嵌套或乱序请求可能导致死锁，可通过避免嵌套、固定顺序或超时策略防范
- 📚 接口：`Lock`（提供名称和模式）与 `LockManager`（提供 `request()` 和 `query()` 方法），通过 `navigator.locks` 访问

---

### [新研究：你所信赖的核心网页指标阈值可能是错误的](https://embrace.io/blog/research-core-web-vitals/)

**原文标题**: [New research: The Core Web Vitals thresholds you trust might be wrong](https://embrace.io/blog/research-core-web-vitals/)

Black Friday 是对每个零售应用的极限挑战。本文介绍了领先团队如何利用 Embrace 和 OpenTelemetry 将技术性能与真实用户体验关联，从而在关键时刻保持高转化率。

- 🛒 Black Friday 是零售应用的压力测试
- 🔗 领先团队用 Embrace 和 OpenTelemetry 连接技术性能与用户体验
- 📈 通过关联数据，在关键时刻提升转化率

---

### [In-N-Out Animation using sibling-index() – Master.dev Blog](https://master.dev/blog/in-n-out-animation-using-sibling-index/)

**原文标题**: [In-N-Out Animation using sibling-index() – Master.dev Blog](https://master.dev/blog/in-n-out-animation-using-sibling-index/)

该文章介绍了如何利用 CSS 的 `sibling-index()` 函数，结合网格布局和 `translate` 属性，在不使用 JavaScript（除增删元素外）的情况下实现元素的进出动画效果。

- 🧩 **核心技巧**：使用 `sibling-index()` 获取元素在同级中的索引，配合 `grid-area: 1/1` 将所有元素重叠，再通过 `translate` 按索引偏移；元素增减时索引自动更新，`transition` 驱动平滑动画。
- 🎬 **入场效果**：通过 `@starting-style` 定义新元素出现时的初始样式（如透明 + 左移），实现优雅的入场动画。
- 📝 **简易代码**：核心 CSS 仅需约 6 行，即可实现类似 Chris 原始 demo 的列表增删动画效果，JavaScript 只需处理 DOM 操作。
- ⚠️ **主要缺点**：元素脱离文档流后容器高度可能不足（需固定高度或等高）；所有元素必须等高/等宽；无法实现元素的淡出动画（期待未来 `@ending-style`）。
- 🛠️ **变通应用**：通过 `cqw`（容器查询单位）和 `sibling-count()` 实现自适应重叠头像列表；结合 `offset` 与 `circle()` 制作圆形展开列表；甚至可模拟网格布局（需额外 hack 修正容器高度）。
- 📚 **更多示例**：包括响应式头像列表、圆形展开头像、可自适应屏幕的网格布局，展示该技巧在不同场景下的灵活性和扩展性。
- 🧪 **总结**：`sibling-index()` 的真正超能力在于结合 `transition` 实现元素动态变化的自动动画，尽管存在局限，但代码极简且效果惊艳，值得与 view transition 方法对比学习。

---

### [SVG 滤镜文字效果：凸版印刷、墨迹增益、木活字](https://www.carmenansio.com/articles/svg-filters-on-type/)

**原文标题**: [SVG Filter Text Effects: Letterpress, Ink Gain, Woodtype](https://www.carmenansio.com/articles/svg-filters-on-type/)

本文介绍了如何使用 SVG 滤镜在网页文字上复现传统印刷术的视觉效果（如油墨扩散、木刻阴影、金属凸起等），并详细演示了多种滤镜原语的组合应用。

- ✒️ **真实外描边**：使用 `feMorphology operator="dilate"` 让字形轮廓向外扩展，配合 `feFlood` 染色，得到完全在字体外部的描边（CSS `text-stroke` 无法实现）。
- 💡 **金属凸起特效**：通过 `feSpecularLighting` 将模糊的 `SourceAlpha` 视为高度图，模拟点光源下的金属字表面高光，支持鼠标交互移动光源。
- 🪵 **阴影木活字**：堆叠多个 `feOffset` 生成阶梯状阴影，再用 `feComposite operator="out"` 切掉原字形，可自由控制阴影方向和颜色。
- 🖨️ **磨损印刷效果**：`feTurbulence` 产生噪声，经 `feDisplacementMap` 扭曲字形，模拟老旧铅字边缘破损或油墨晕开，效果强弱可调。
- 🫧 **粘稠融合**：高模糊（`feGaussianBlur`）后通过 `feColorMatrix` 设置陡峭的 alpha 阈值，使相邻字形融合成流动形状，适合表现液态感。
- 🌈 **色差分裂**：用三个 `feColorMatrix` 分别提取 R、G、B 通道，将红蓝通道进行 `feOffset` 偏移后叠加，模拟印刷套版不准的彩色边缘。
- 💡 **霓虹发光**：先对 `SourceAlpha` 染色，再用两个不同半径的模糊产生内亮外晕的效果，合并后叠加原文字，可制作管状发光文字。
- 🎨 **镀金首字母**：组合 `feMorphology` 外描边、金色渐变填充与 `feSpecularLighting` 高光，配合 `shape-outside` 实现文字环绕，模拟中世纪手稿金箔装饰。
- ⚙️ **应用方式**：SVG `<filter>` 既可直接用在 SVG `<text>` 上，也可通过 CSS `filter: url(#id)` 应用于任意 HTML 元素；滤镜定义需放在可见但隐藏的内联 SVG 中（避免 `display:none`）。
- ⚡ **性能与兼容**：`feTurbulence`、`feDisplacementMap` 和 `feSpecularLighting` 较耗性能，建议用 `requestAnimationFrame` 驱动动画，并使用 `IntersectionObserver` 和 `prefers-reduced-motion` 优化；需扩展滤镜边界（`x、y、width、height`）以防像素裁剪。

---

### [在 JS 中以每秒 60 亿次操作转换颜色——Dima Kryaklin](https://dkryaklin.com/blog/colordx-gpu)

**原文标题**: [Converting colors in JS at 6 billion operations per second â Dima Kryaklin](https://dkryaklin.com/blog/colordx-gpu)

请提供您希望我总结的文本内容，以便我按照指定模板生成概述和要点列表。

---

### [被盗的纽扣 | 阿纳托利·曾科夫](https://anatolyzenkov.com/stolen-buttons)

**原文标题**: [Stolen Buttons | Anatoly Zenkov](https://anatolyzenkov.com/stolen-buttons)

概述总结  
用户从每个访问的网站“偷”一个按钮，并展示其收藏。页面包含大量不同网站上的按钮文本、操作选项和多语言标签，涵盖了登录、注册、购买、设置等常见功能。

- 🕵️“偷按钮”概念：用户从访问的每个网站窃取一个按钮，并展示自己的收藏。
- 🗂️ 收藏展示：页面展示了大量来自不同网站的按钮文本，包括英语和德语等多种语言。
- 🔘 常见操作按钮：如“登录”、“注册”、“商店访问”、“添加到购物车”、“接受”、“拒绝”等。
- 🛒 购买与订阅：涉及“选择订阅”、“立即购买”、“免费试用”、“升级到 Plus”等选项。
- 🎨 设计相关：包括“设计”、“展示”、“组件浏览”、“继续阅读”等按钮。
- 🌐 多语言支持：文本混合了德语和英语，如“Anmelden”、“Registrieren”、“Shop besuchen”等。
- 🔄 交互选项：如“接受邀请”、“同意”、“关闭”、“重置”、“查看更多”等。
- 📱 其他功能：包括“联系信息”、“热力图了解”、“用户与角色”、“创建帖子”、“搜索”等。

---

### [按钮窃贼 | 阿纳托利·曾科夫](https://anatolyzenkov.com/stolen-buttons/button-stealer)

**原文标题**: [Button Stealer | Anatoly Zenkov](https://anatolyzenkov.com/stolen-buttons/button-stealer)

Button Stealer 是一款自动从每个网站“偷取”一个按钮的浏览器扩展，功能有趣且无用，完全免费，评分高且注重隐私。  
- 🤖 自动运行：浏览网页时自动偷取按钮，无需手动操作  
- 🎯 实用零：纯粹为了好玩，毫无实际用途  
- 🆓 完全免费：下载安装不花一分钱  
- ⭐ 高评分：获得 4.9/5 的评分，Chrome 网上商店排名第三  
- 🚀 产品认可：Product Hunt 当日的产品，获 492 个赞  
- 🧑‍💻 作者信息：由 Theo 开发（3t.gg）  
- 🔒 隐私保护：所有操作在本地完成，不发送任何数据，保障隐私安全

---

### [Canvas UI：创意画布与 WebGL 组件库](https://canvasui.dev/)

**原文标题**: [Canvas UI: Creative Canvas and WebGL Component Library](https://canvasui.dev/)

Canvas UI 是一个开源的 HTML-in-Canvas 和 WebGL 组件库，提供可复制粘贴的框架无关组件，所有效果在画布上实时渲染，支持多种前端框架，且永久免费使用。

- 🎨 提供 25+ 种创意 WebGL 与 Canvas 组件，如 Blaze、Liquid、Glass、Shatter、Particle Reveal 等，每个组件都可在官网实时预览
- 🚀 通过单行命令`npx shadcn@latest add @canvas-ui/particle-reveal-react`即可安装完整源码到项目，无需绑定版本
- 📋 三步使用：挑选组件→运行 CLI 命令→自由修改代码，组件源码完全归你所有
- 🔄 框架无关：每个效果提供 React、Solid、Preact、Vue、Svelte 及纯 TypeScript 共六种版本，参数一致
- 🤖 AI 就绪：支持 shadcn MCP 协议，智能助手可通过单个提示词浏览、安装组件
- 💸 永久免费：MIT+Commons Clause 许可，可自由用于个人或商业项目，仅禁止转售组件本身
- 🌐 浏览器兼容：实验性 Canvas 效果在 Chrome 上需启标记，其他浏览器优雅降级为 WebGL 叠加层，WebGL 组件支持所有现代浏览器
- ⚡ 性能优化：效果通过 GPU 渲染，独立于 React 渲染周期，仅在挂载时初始化，离屏暂停，卸载时清理，支持减少动画偏好
- 📦 更新灵活：代码直接放入你的仓库，可随时重新安装最新版或自行修改

---

### [AI 工作流构建器图表库 — JointJS](https://www.jointjs.com/ai-workflow-builders?utm_source=frontend-focus&utm_medium=sponzored-ad)

**原文标题**: [AI workflow builder diagramming library — JointJS](https://www.jointjs.com/ai-workflow-builders?utm_source=frontend-focus&utm_medium=sponzored-ad)

overview summary
JointJS for React 是一个生产级图表库，专为构建复杂可视化界面（如 AI 工作流编辑器、BPMN 建模工具等）而设计。它提供高度自定义的节点 UI、任意图拓扑支持、虚拟渲染、框架无关性（React、Angular、Vue、Svelte）以及商业支持，帮助团队从原型快速过渡到生产环境。

- 🧩 **原生 React 集成**：专为 React 应用优化的图表库，提供生产级性能和详细文档。
- 🎨 **完全自定义节点 UI**：支持在节点内嵌入交互式组件（如模型选择器、提示编辑器、滑块），渲染和行为完全可控。
- 🔄 **任意图拓扑**：允许循环、条件分支、动态子图，不局限于 DAG 结构。
- 🔗 **端口级连接控制**：精确定义哪些端口可连接，在交互时强制执行规则，确保用户构建有效管道。
- ⚡ **虚拟渲染**：仅渲染视口内的元素，即使数百个节点也能保持稳定性能。
- ↩️ **复合撤销/重做**：将级联删除等操作作为原子级撤销，用户体验流畅。
- 🌐 **框架无关**：支持 React、Angular、Vue、Svelte 和 TypeScript，无缝集成现有架构。
- 🛠️ **商业支持与 SLA**：提供专用帮助台、保证响应时间和经过验证的定制问题解答。
- 📈 **AI 工作流构建器**：提供现成模板，包含自定义节点、属性编辑器、拖放、边路由和撤销/重做，快速启动开发。
- 💬 **客户证言**：全球创新企业（如 Silo team、Itemis、NICE Systems）称赞其节省开发时间、提升产品体验。

---

### [简介 - MapLibre GL JS](https://maplibre.org/maplibre-gl-js/docs/)

**原文标题**: [Introduction - MapLibre GL JS](https://maplibre.org/maplibre-gl-js/docs/)

MapLibre GL JS 是一个基于 TypeScript 的库，利用 WebGL 在浏览器中渲染交互式地图，其外观由 MapLibre Style Spec 定义的样式文档控制。它属于 MapLibre 生态系统，同系列还有面向移动端的 MapLibre Native。

- 🌍 核心功能：使用 WebGL 渲染矢量瓦片地图，支持交互式地图操作。
- 📖 文档结构：分为主类（如 Map 对象）、全局函数、标记与控件、地理几何工具、用户交互处理器、数据源、事件系统等章节。
- 🚀 快速开始：通过 CDN 引入 CSS 和 ESM 模块即可创建地图，示例使用 `<script type="module">` 加载。
- 📦 npm 安装：通过 `npm install maplibre-gl` 安装，然后导入 `Map` 和 CSS 文件。
- 🔧 ESM 支持：v6 仅提供 ESM 模块，需根据打包器（Vite、webpack 5+、esbuild、Rollup 等）配置 worker URL。
- 🛠️ 打包器配置：示例展示了不同工具（Vite、webpack、esbuild、Rollup）的 worker 设置方法。
- 🔒 CSP 指令：若使用内容安全策略，需允许 `worker-src 'self'` 和 `img-src data: blob: 'self'`。
- 🎨 CSS 引用：必须引入 `maplibre-gl.css`，否则 Popup、Marker 等 DOM 元素无法正确显示。

---

### [发布 v6.0.0 · maplibre/maplibre-gl-js · GitHub](https://github.com/maplibre/maplibre-gl-js/releases/tag/v6.0.0)

**原文标题**: [Release v6.0.0 · maplibre/maplibre-gl-js · GitHub](https://github.com/maplibre/maplibre-gl-js/releases/tag/v6.0.0)

MapLibre GL JS v6.0.0 版本是一次重大更新，全面转向现代 JavaScript 生态，移除 WebGL1 和 UMD 支持，重构事件系统与类型定义，同时带来大量性能优化和错误修复。

- 🚀 切换到 ESM-only 分发，移除 UMD 和 CSP 专用包，改用 `<script type="module">` 导入
- ⛔ 移除 WebGL1 支持，现在仅兼容 WebGL2，提升性能与新功能
- 📦 重构事件系统，所有事件均为独立类，`Map` 不再继承 `Camera` 而是组合，类型更严格
- 🆕 新增 `line-layer-opacity`、`fill-layer-opacity` 图层整体透明度属性
- 💡 改进类型定义，`{get,set}LayoutProperty` 等方法现在反射实际类型
- ⚡ 性能优化：特征状态改用数组索引、顶点着色器不透明度剪裁、纹理使用 `texStorage2D` 等
- 🎨 新增 `Map.setMissingStyleImageResolver` 异步图像解析器，替代旧的 `styleimagemissing` 回调
- 🔄 光照位置插值改为球坐标，保持径向距离平滑过渡
- 🐛 修复透明重叠线条生成伪影的问题（通过 `line-layer-opacity` 解决）
- 🐛 修复 `flyTo` 在设置 `minZoom` 时的相机跳跃
- 🐛 修复取消 worker 请求导致内存泄漏（`Actor.sendAsync` 现返回 `AbortError`）
- 🐛 修复跨域模块 worker 加载问题，保留 ESM 语义
- 🐛 修复 `queryRenderedFeatures` 在瓦片冲突重载时的错误
- 🔗 使用 Rolldown 替代 Rollup 进行打包，类型导出速度提升 78 倍
- 📐 地形渲染优化：复用纹理、跳过不必要的数据查找、减少内存分配
- 🌐 更新 maplibre-gl-style-spec 至 v25，对过时表达式抛出警告而非静默失败
- 🧹 清除所有 Mapbox 残余引用，`#pragma mapbox` 改为 `#pragma maplibre`
- 🏷️ 支持 GeoJSON 内部嵌套对象，编码方式变为 `__$json__` 结构
- 🔧 `Hash` 位置控制改用 `URLSearchParams`，提高可扩展性
- 📝 运行时错误警告现在指向具体的样式位置（如 `layers[3].paint.line-color`）

---

### [maplibre-gl-js/docs/guides/v5-to-v6-migration-guide.md at main · maplibre/maplibre-gl-js · GitHub](https://github.com/maplibre/maplibre-gl-js/blob/main/docs/guides/v5-to-v6-migration-guide.md)

**原文标题**: [maplibre-gl-js/docs/guides/v5-to-v6-migration-guide.md at main · maplibre/maplibre-gl-js · GitHub](https://github.com/maplibre/maplibre-gl-js/blob/main/docs/guides/v5-to-v6-migration-guide.md)

本次更新将 MapLibre GL JS 从 v5 迁移至 v6，主要涉及模块化、导入方式、脚本加载、Worker 配置、CSP、事件等关键变化。

- 🔄 v6 仅发布 ES 模块，不再提供 UMD 和独立的 CSP 构建文件，主文件改为 `maplibre-gl.mjs`
- 📥 若使用默认导入（`import maplibregl from 'maplibre-gl'`），需改为命名导入或命名空间导入；命名导入保持不变
- 🖥️ 若通过 `<script src>` 加载，需改用 `<script type="module">` 并从 CDN 导入 `.mjs` 文件
- 🔧 `setWorkerUrl()` 在直接浏览器 ESM 中自动处理，无需调用；在打包器中仍需手动调用一次
- 🛡️ CSP 指令需调整：从 CDN 跨域加载时需添加 `worker-src 'self' blob:`；自托管 Worker 文件则不需要 `blob:`，但需确保 `img-src` 包含 `data: blob:`
- 📐 `zoomLevelsToOverscale` 参数默认行为改变（切片矢量瓦片而非过缩放），设为 `undefined` 可恢复 v5 旧行为
- 🏷️ 所有 `#pragma mapbox` 应替换为 `#pragma maplibre`
- 🎯 事件对象现在为类实例，建议通过 `type` 字段判断事件类型，而非使用 `instanceof`
- 🖼️ `styleimagemissing` 监听器中不再允许通过 `map.addImage()` 解析当前缺失图像，应改用 `map.setMissingStyleImageResolver()` 提供图像生成函数

---

### [Markdy — 开源动画 DSL 引擎](https://markdy.com/)

**原文标题**: [Markdy â Open-Source Animation DSL Engine](https://markdy.com/)

Markdy 是一个轻量级、零依赖的动画场景脚本语言和渲染引擎，基于纯 TypeScript 和 Web Animations API，适合 AI 生成、框架无关，并提供丰富的生态系统与交互式学习工具。

- 📦 核心特性：零依赖、纯 TypeScript 解析器；基于 Web Animations API 和 CSS 变换的原生渲染；AI 友好的结构化 DSL；框架无关，支持 Astro 组件。
- 🧩 轻量包体系：`@markdy/core`（解析器+AST，~12KB）和 `@markdy/renderer-dom`（浏览器渲染器，~22KB）为必需，Astro、MDX、CLI 为可选扩展。
- 🛠 工具与插件：语言服务器（LSP）提供诊断、自动补全；可选 actor 包（stdlib-systems）用于系统架构图；CLI 支持终端渲染与预览。
- 🎮 交互式示例与编辑器：提供多个真实示例（如爱情故事、战斗场面），内置编辑器支持自动补全和实时预览，可一键运行。
- 📚 学习指南：从场景设置（画布、帧率）、角色定位与修饰符、时间线和动作（进入、移动、淡入淡出）、说话与效果（气泡、抖动）、表情与肢体控制（关节旋转、拳打脚踢），到资产加载、变量模板和序列封装，逐步进阶。
- 🤖 AI 友好设计：通过 `AGENT.md` 完整文档让 AI 理解语法，用户用自然语言描述场景即可生成合法脚本，支持 Claude、ChatGPT 等 AI 工具。
- 🌐 社区与案例：已有真实项目在生产中使用，如 Astro 场景、安全漏洞演示等。

---

### [Mermaid | 图表绘制工具](https://mermaid.ai/open-source/)

**原文标题**: [Mermaid | Diagramming and charting tool](https://mermaid.ai/open-source/)

该团队由 Knut Sveidqvist 创建，并有多位开发者和贡献者组成，欢迎社区参与。

- 🧑‍💻 创始人：Knut Sveidqvist
- 🏆 赞助者：Knut Sveidqvist 和 Nacho Orlandoni
- 🛠️ 开发者：Nacho Orlandoni、Sidharth Vinod、Ashish Jain、Neil Cuzon、Alois Klink、Tyler Liu、Reda Al Sulais、Nikolay Rozhkov、Justin Greywolf、Steph Huynh、Matthieu Morel、Per Brolin、Marc Faber、Yash Singh、Mindaugas Laganeckas
- 🤝 社区贡献者：欢迎加入并参与

---

### [KaTeX – 最快的网络数学排版库](https://katex.org/)

**原文标题**: [KaTeX – The fastest math typesetting library for the web](https://katex.org/)

概述：KaTeX 是一个用于 Web 的极速数学排版库，具有同步渲染、无依赖、打印质量高、支持服务端渲染等特点，并提供多种配置选项。

- ⚡ 同步渲染：无需页面重排，速度极快  
- 🖨️ 打印质量：基于 Donald Knuth 的 TeX，排版效果达到业界标准  
- 📦 自包含：无外部依赖，易于集成到网站资源中  
- 🌐 服务端渲染：通过 Node.js 预渲染，跨环境输出一致  
- 🚀 轻量高效：即使页面包含数百个表达式也能快速加载  
- ⚙️ 丰富选项：支持 displayMode、leqno、fleqn 等配置及宏定义  
- 🔗 开源许可：MIT 许可，由众多贡献者共同维护

---

### [KaTeX – 最快的网页数学排版库](https://katex.org/#demo)

**原文标题**: [KaTeX – The fastest math typesetting library for the web](https://katex.org/#demo)

KaTeX 是一个专为网页设计的超快速数学排版库，拥有简洁 API、无依赖、同步渲染、基于 TeX 标准、支持服务器端预渲染，并提供丰富的可配置选项。

- 📐 数学排版库：KaTeX 号称“最快”的网页数学排版工具，基于 TeX 标准，渲染质量高  
- ⚡ 同步快速渲染：无需重排页面，即使页面包含数百个表达式也能闪电般响应  
- 🧩 无依赖自包含：易于集成到网站资源中，不依赖任何外部库  
- 🖥️ 服务端渲染：通过 Node.js 预渲染，输出一致，可发送纯 HTML  
- 🏆 对比优势：比 MathJax 更快，适合高性能需求  
- 🔧 丰富选项：支持 displayMode、leqno、fleqn、错误处理（throwOnError）、输出格式（html、mathml）、宏定义等  
- 📋 编辑器功能：最大化编辑器、复制 KaTeX 代码、复制永久链接  
- 👥 开源社区：由 Emily Eisenberg 和 Sophie Alpert 创建，MIT 许可，众多贡献者；网站由 Netlify 提供支持

---

### [抖动它！](https://ditherit.com/)

**原文标题**: [Dither it!](https://ditherit.com/)

请提供需要总结的文本内容，我将按照模板为您生成中文概述和要点。

---

### [@joshwcomeau.com 在 Bluesky 上](https://bsky.app/profile/joshwcomeau.com/post/3mralqfq3m22n)

**原文标题**: [@joshwcomeau.com on Bluesky](https://bsky.app/profile/joshwcomeau.com/post/3mralqfq3m22n)

此帖介绍了一个名为 ditherit.com 的酷炫网站，用户可上传图片并尝试不同的抖动算法，以减小文件大小或实现艺术效果。网站需要 JavaScript 支持。

- 🚨 网站公告：ditherit.com 上线，可上传图片实验抖动算法
- 🎨 功能：支持多种抖动算法，用于文件压缩或艺术创作
- 🔧 要求：该交互式网页需启用 JavaScript
- 🧵 作者附上了示例线程（线程中展示效果）

---
