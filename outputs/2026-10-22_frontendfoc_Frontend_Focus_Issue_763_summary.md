### [2027 年 Web 平台功能排名](https://interop-rank.fxdx.dev/)

**原文标题**: [2027 Web Platform Feature Ranking](https://interop-rank.fxdx.dev/)

您尚未提供需要总结的文章内容，因此暂时无法生成摘要与要点。

- 📄 请粘贴文章正文或相关内容
- ✅ 收到内容后，我会按“概述 + 要点”格式整理
- 🔍 要点将包含关键信息与核心结论
- 🧾 每个要点会使用“-”符号并搭配合适的表情符号

---

### [CSS 的未来 ✨ • Josh W. Comeau](https://www.joshwcomeau.com/css/interop-2027/)

**原文标题**: [The Future of CSS ✨ • Josh W. Comeau](https://www.joshwcomeau.com/css/interop-2027/)

Interop 2027 正在规划中，Mozilla 通过排名系统收集开发者最期待的 Web 特性；文章列出作者投票的 10 个 CSS 提案，多数已在 Chromium 实现，可作为渐进增强提前试用，若入选 Interop 有望加速跨浏览器普及。

- 🌐 Interop 项目由主流浏览器厂商协作推进，能显著提升 Web 特性的跨浏览器支持率，Subgrid 就是成功案例。
- 🧩 CSS 函数提案允许用 `@function` 定义可复用函数，并可结合 `calc()`、三角函数实现极坐标转换等复杂效果。
- 🔲 `corner-shape` 支持 squircle、bevel、notch、scoop 等角形，且会改变实际 border-box，使边框、轮廓和阴影正确跟随。
- ✏️ `border-shape` 可自定义直线、弧线和贝塞尔曲线组成的边框形状，并支持形状间动画。
- ⚓ 锚点容器查询为 Anchor Positioning Level 2 增加回退位置检测，解决 tooltip 翻转后无法判断位置的问题。
- ♻️ `inherit()` 函数提案允许读取继承值并用 `calc()` 修改，例如修正嵌套圆角，但目前尚无浏览器实现。
- 🎬 滚动触发动画与滚动驱动动画互补，可在滚动到特定位置时触发关键帧动画，减少对 IntersectionObserver 的依赖。
- ♿ `reading-flow` 和 `reading-order` 可让 Tab 顺序跟随视觉布局，改善响应式网格和 Flexbox 的可访问性。
- 📏 `interpolate-size` 与 `calc-size()` 支持在 `height: 0` 和 `height: auto` 等关键字尺寸间动画，适合折叠面板。
- 🧱 Gap decorations 通过 `rule`、`row-rule`、`column-rule` 为网格间隙绘制边框式线条，避免空单元格和背景色 hack。
- 📌 滚动状态容器查询可检测 sticky 元素是否“粘住”，以及滚动容器是否还能向上/向下滚动，用于粘性头部和滚动渐变提示。
- 🚀 截至 2026 年 10 月，这些特性多仅在 Chrome/Edge 支持，Firefox/Safari 尚未支持；作者建议用 `@supports` 渐进增强，并鼓励开发者参与 Interop 2027 排名投票。

---

### [我对 Interop 2027 的首选推荐](https://www.sarasoueidan.com/blog/interop-2027-rankings/)

**原文标题**: [My top picks for Interop 2027](https://www.sarasoueidan.com/blog/interop-2027-rankings/)

文章发布于 2026 年 10 月 11 日，作者分享了自己对 Interop 2027 功能的优先选择。Interop 是提升 Web 平台关键特性跨浏览器互操作性的年度项目；Firefox 连续第二年提供排序页面，让 Web 社区影响浏览器厂商的工作重点。作者主要根据功能用例和预期效果选择，偏爱能同时改善用户体验、可访问性与开发者体验的特性。

- 🗳️ Firefox 连续第二年开放 Interop 2027 功能排序，帮助团队确定优先提案，社区可借此影响浏览器实现重点。
- 🥇 排名第一：HTML `focusgroup` 属性，有助于创建更可访问的常见 UI 模式。
- 🥈 排名第二：`ariaNotify()` API，与 `focusgroup` 正确、负责地使用时，可提升可访问性并减少手动工作。
- 🥉 排名第三：HTML `headingoffset`、`headingreset` 属性与 CSS `:heading()` 伪类组合包，用于完善标题层级控制。
- ✨ 其他获投票但未排名：Interest Invokers、可定制/可样式化 `<select>`、响应式 iframe 等长期需求功能。
- 🎨 CSS 增强包括 `border-shape`、`corner-shape`、gap decorations、`flex-wrap: balance`、`@counter-style`。
- 🎞️ 期待 `interpolate-size` 与 `calc-size()`，以及允许 `display` 和 `content-visibility` 过渡/动画。
- 🧭 还支持 `reading-flow`/`reading-order`、`object-view-box` 等布局与图像控制能力。
- ⚖️ 规则是不能给功能降票；不熟悉、无感或负面的功能可留空不排名。
- 👥 作者也分享了 Ana Rodrigues、Declan Chidlow、Cyd Stumpel 等人的 Interop 2027 选择，强调偏好主观且源于经验与职业需求。

---

### [我的 Interop 2027 排名 - 2026 年 10 月 11 日 07:00 UTC | Vale.Rocks](https://vale.rocks/micros/20261011-0700)

**原文标题**: [My Interop 2027 Rankings - 11 Oct 2026 07:00 UTC | Vale.Rocks](https://vale.rocks/micros/20261011-0700)

作者提交了 Firefox 2027 Web 平台功能排名，只挑选自己最关注的 Interop 提案，并逐项说明理由；重点集中在 SVG、CSS 可访问性与布局、表单控件、图片渐进渲染、JavaScript 日期 API、滚动动画、响应式 iframe 和折叠设备 API。

- 🗳️ 作者按个人兴趣提交 Interop 2027 排名，只列出最关注的项目，避免“全部高亮等于没有重点”。
- 🖼️ 优先支持 SVG 改进，尤其是修复 SVG 滤镜相关缺陷并增强多种能力。
- ♿ 关注 CSS `reading-flow` 和 `reading-order` 属性，认为它们有望修复大量可访问性问题。
- 🧪 支持 CSS `@supports at-rule()`，便于检测新特性支持情况，尤其适合文章演示和渐进增强。
- 📐 关注 `flex-wrap: balance`、`line-clamp`、`corner-shape`、`gap decorations` 等布局与样式能力。
- 🎛️ 希望原生支持可定制、可样式化的 `<select>`，替代大量可访问性较差的 hack 实现。
- 🖼️ 支持 JPEG XL 和 AVIF 图片渐进渲染，让用户在下载完整图片前先看到预览。
- ⏱️ 支持 JavaScript `Temporal`，作者直言“不需要 Temporal 活下去，只需要 Date 死掉”。
- 🎞️ 关注 CSS 滚动触发动画，认为可与滚动驱动动画互补。
- 🪟 希望支持响应式 iframe，解决此前已讨论过的实现痛点。
- 📱 关注 Device Posture API，为折叠设备上的 Web 体验带来与原生应用更接近的能力。
- 🔗 文末还推荐了其他作者的排名和更广泛的 Web 平台愿望清单。

---

### [……这就是我的排名！2027 年版 | Always Twisted](https://www.alwaystwisted.com/articles/and-thats-my-rank-2027-edition)

**原文标题**: [... And That's My Rank! 2027 Edition | Always Twisted](https://www.alwaystwisted.com/articles/and-thats-my-rank-2027-edition)

2026 年 9 月 11 日发布的《And That's My Rank! 2027 Edition》介绍了 Interop 2027 的开发者投票，作者列出了希望获得跨浏览器支持的 Web 平台特性，核心主题是 CSS 正变得更强，能够接管过去依赖 Sass 或 JavaScript 的工作。

- 🗳️ Interop 投票进入第二年，Rick 接棒 Jake；参与成本几乎为零，可表达开发者真正想要的跨浏览器能力。
- 🧩 清单包括 CSS `@function`、`@mixin`/`@apply`、`if()`、`calc-size()`、扩展 `attr()` 等，让 CSS 更接近 Sass 的能力。
- 📐 布局与视觉效果涉及 `margin-trim`、`corner-shape`、CSS anchor positioning 和 `text-box`。
- 🎛️ 可定制的原生 `<select>` 允许用 CSS 调整下拉框、按钮和选项外观。
- 🔁 `margin-trim` 和 anchor positioning 是去年已关注、今年仍在名单中的“熟面孔”。
- 🎯 作者认为原生函数、混入、条件、内在尺寸和表单控件定制会显著增强 Web 平台，减少 workaround。
- ⏳ 文章发布时仍可前往 Developer Signals 查看其他开发者的选择并投票。
- 🛠️ 文末还提供了现代化重构与最佳实践咨询入口。

---

### [我的 Interop 2027 排名 – Eric 的归档思考](https://meyerweb.com/eric/thoughts/2026/10/14/my-interop-2027-rankings/)

**原文标题**: [My Interop 2027 Rankings  –  Eric’s Archived Thoughts](https://meyerweb.com/eric/thoughts/2026/10/14/my-interop-2027-rankings/)

文章介绍作者对 Interop 2027 提案的个人排名：Interop 提案期已结束，团队正结合开发者信号筛选提案；Jake Archibald 的排名工具允许 GitHub 用户对约 150 个提案排序，结果匿名共享。作者共排了 20 项，强调 Temporal、修复互操作缺口、去掉厂商前缀和推动新特性早期协同实现，并声明这不代表其作为 Igalia 代表的正式投票。

- 🗳️ Interop 2027 提案期于 9 月底结束，团队正在评估提案；开发者信号包括调查、博客、视频和排名工具等。
- 🛠️ Jake Archibald 的排名工具允许 GitHub 用户对约 150 个提案排序，结果匿名提供给 Interop 团队。
- ⚠️ 作者强调这是个人排名，不代表也不会预测其作为 Igalia 代表的正式投票。
- 🥇 第 1 名：JavaScript Temporal，认为其远优于 Date，能处理时区、夏令时和历史时区变更。
- 🥈 第 2 名：CSS sibling-count() 和 sibling-index() 的互操作修复，属于“已发布但仍有 WPT 失败”的典型 Interop 提案。
- 🥉 第 3 名：去掉 CSS box-decoration-break 的厂商前缀；第 4 名：HTML headingoffset 和 headingreset 属性；第 5/6 名：CSS line-clamp 与 margin-trim。
- 📋 作者共排 20 项，还涵盖 Trusted Types、DOM moveBefore()、Viewport Segments API、WebCodecs 互操作等。
- 🎨 CSS 相关还包括 anchor positioning 动画/变换、色域映射、corner-shape、polygon() 顶点圆角、border-shape、gap 装饰、grid lanes（masonry）、linked parameters、display/content-visibility 过渡、尺寸容器查询中的 var()。
- 🚫 未列入的提案原因包括已有较强支持、缺乏标准或浏览器兴趣，或作者认为想法不佳。
- 💬 评论者 Richard Rutter 表示更希望修复一个 29 年前的 break-after:avoid 旧 bug。

---

### [哦，你好，安娜——我的互操作功能排名](https://ohhelloana.blog/my-interop-2027/)

**原文标题**: [Oh Hello Ana - My Interop feature ranking](https://ohhelloana.blog/my-interop-2027/)

Ana Rodrigues 于 2026 年 10 月 8 日发文，介绍 Firefox 团队推出的 Interop 2027 提案排名网站，并分享自己的排序思路：在“对个人博客有利”和“让日常工作更轻松、能删代码”之间各选五项，形成平衡榜单；10 月 19 日更新称其他开发者也开始发布类似榜单，Firefox 排名网站新增分享功能。

- 🗳️ Firefox 推出 Interop 2027 提案排名网站，让用户按关心程度对提案排序。
- ⚖️ 作者从个人博客受益与工作提效/删代码两个角度各选五项，保持平衡。
- 🧩 最终十项包括 CSS `random()`、`corner-shape`、gap decorations、`border-shape`、`object-view-box`、`flex-wrap: balance`、`reading-flow`/`reading-order`、可定制 `<select>`、103 Early Hints preloading、CSS grid lanes（masonry）。
- 🎉 纯娱乐榜单还包括 `sibling-count()`/`sibling-index()`、`filter(image, ...filters)`、`random-item()`、尺寸容器查询中的 `var()`、无厂商前缀的 `box-decoration-break` 等。
- 💼 工作与客户高频需求包括 `flex-wrap: balance`、可定制 `<select>`、103 Early Hints、masonry、`reading-flow`/`reading-order`、尺寸容器查询中的 `var()`、CSS linked parameters、`@supports at-rule()`、响应式 iframe、`AccentColor` 反映 `accent-color`。
- 👥 更新称其他开发者（如 Sara Soueidan、Eric A. Meyer 等）也发布排名，Firefox 排名网站新增分享功能，便于生成博客文章。
- 📝 文末提供留言表单和更多文章链接。

---

### [我的 Interop 2027 排名——Tyler Sticka](https://tylersticka.com/journal/interop-2027-rank/)

**原文标题**: [My Interop 2027 Ranking â Tyler Sticka](https://tylersticka.com/journal/interop-2027-rank/)

文章概述：作者分享了自己对 Interop 2027 提案的排名，重点选出八项最期待的 CSS 新特性并说明理由，同时提到 Firefox 团队正在征集排名意见，并表达了对 Ana Rodrigues 榜单的认可。

- 📅 文章发布于 2026 年 10 月 9 日，主题是作者的 Interop 2027 排名。
- 🦊 Firefox 团队希望社区帮助对 Interop 2027 提案进行排名。
- 🎨 支持 CSS `border-shape`，以便设计更自由、更独特的新容器。
- 🧩 期待 CSS gap decorations，用来简化网格中的分隔线设计。
- 🔽 看好可自定义的 `<select>`，因为已有演示效果非常吸引人。
- 📏 希望 CSS `interpolate-size` 和 `calc-size()` 能基于真实内容改进尺寸与动画。
- 🎲 期待 CSS `random()`，让样式具有真正的随机性。
- ↔️ 支持 `flex-wrap: balance`，以改善布局平衡并减少孤行问题。
- 🌈 关注 CSS 色域映射，因为 sRGB 之外的世界仍让人感到陌生。
- 📖 期待 `reading-flow` 和 `reading-order`，以便更深入使用网格并减少副作用。
- 👍 作者也很喜欢 Ana Rodrigues 的排名。
- 💻 其他日志条目提到“改造一台 15 年前的 MacBook Air”，日期为 2026 年 10 月 1 日。

---

### [Bluesky 上的 @sturobson.com](https://bsky.app/profile/sturobson.com/post/3mxlhrdlock22)

**原文标题**: [@sturobson.com on Bluesky](https://bsky.app/profile/sturobson.com/post/3mxlhrdlock22)

该帖子汇总了多位开发者分享的 Interop 2027 排名与选择文章链接，并表达感谢。

- 📝 作者 Stuart Robson 在 Bluesky 发帖，个人网站为 sturobson.com。
- 🔗 提到 @ohhelloana.blog 的 Interop 2027 文章：https://ohhelloana.blog/my-interop-2027/
- 🔗 提到 @tylersticka.com 的 Interop 2027 排名：https://tylersticka.com/journal/interop-2027-rank/
- 🔗 提到 @pawelgrzybek.com 的 Interop 2027 选择：https://pawelgrzybek.com/my-interop-2027-picks/
- 🔗 提到 @vale.rocks 的相关短文：https://vale.rocks/micros/20261011-0700
- 🕒 帖子发布时间为 2026-10-11T07:21:39.057Z，并附有 🙏🖤 表情。

---

### [Meticulous AI - 无需编写测试的自动化前端测试](https://www.meticulous.ai/?utm_source=frontend_focus&utm_medium=newsletter&utm_campaign=26q4_2&utm_term=primary+content)

**原文标题**: [Meticulous AI - Automated Frontend Testing Without Writing Tests](https://www.meticulous.ai/?utm_source=frontend_focus&utm_medium=newsletter&utm_campaign=26q4_2&utm_term=primary+content)

overview summary
Meticulous 是面向复杂代码库的自动化端到端视觉测试平台：通过录制开发、预发布和生产环境的用户交互，AI 持续生成并维护覆盖全应用流程的测试，在合并前暴露回归问题，并强调零维护、无 flake、高速并行与低开发者投入。

- 🎯 核心价值：自动化、穷尽式、确定性的测试验证，让团队以代理编写代码的速度交付可靠代码。
- 🧠 工作方式：添加 recorder 脚本记录交互，AI 根据代码分支覆盖生成持续演进的视觉端到端测试。
- 🔀 PR 影响分析：提交拉取请求后，可在合并前查看变更对用户工作流的影响。
- 🧪 无副作用测试：默认保存并回放后端响应，避免数据变化导致误报，无需特殊测试账号或逐次 mock 数据。
- 🔄 自动维护：测试随应用演进自动新增和淘汰，无需开发者编写、修复或维护测试。
- ⚡ 高速与稳定：基于 Chromium 的确定性调度引擎消除 flake，并通过计算集群并行运行数千屏幕，约 120 秒内出结果。
- 🧩 灵活使用：可补充或替代现有测试套件，支持 NextJS、React、Vue、Angular、Nuxt、SvelteKit 等集成。
- 🏢 市场验证：声称获 100+ 组织信任，并有 Dropbox、Notion、Engine 等工程负责人正面评价。
- 🔐 配套能力：提供集成、安全、文档、演示预约与快速上手入口。

---

### [2026 年 HTML 现状](https://survey.devographics.com/en-US/survey/state-of-html/2026)

**原文标题**: [State of HTML 2026](https://survey.devographics.com/en-US/survey/state-of-html/2026)

提供的内容仅为“Loading...”加载提示，暂无实质文章信息可供总结。
- ⏳ 原文仅显示“Loading...”，表示内容正在加载。
- 📄 未包含正文、关键信息或可提取要点。
- 🔍 建议提供完整文本后再进行有效摘要。

---

### [](https://webkit.org/blog/18438/blocking-identity-resolution-infrastructure/)

**原文标题**: [  Blocking Identity Resolution Infrastructure | WebKit](https://webkit.org/blog/18438/blocking-identity-resolution-infrastructure/)

Apple 与 WebKit 长期通过 Cookie 隐私保护、存储与缓存分区、反指纹识别等措施防止网络追踪；在全面阻止跨站 Cookie 六年后，又针对“后 Cookie 时代”的身份解析追踪，在最新系统中默认阻止身份解析基础设施的网络访问，同时保留网站的第一方个性化能力。

- 🍪 Apple 从首版 Safari 起就保护 Cookie 隐私，并较早推出存储与缓存分区，持续对抗设备指纹识别。
- 🚫 WebKit 六年前已全面阻止跨站 Cookie，但追踪行业转向“身份解析”等后 Cookie 追踪方式。
- 📧 身份解析中，第三方会在用户登录或订阅时暗中收集邮箱，生成与邮箱永久绑定的不透明追踪 ID，并存储在网站上用于跨站画像和广告定向。
- 🔗 退出登录或退订邮件并不会删除第三方保存的追踪 ID 和邮箱；随着更多登录和表单数据被收集，第三方会构建“身份图谱”。
- 📱 邮箱和电话号码属于个人可识别信息，可用于跨网站甚至跨设备追踪；用户提供信息时通常不会预期被第三方用于其他目的。
- 🏢 第一方个性化不属于追踪，但中心化身份解析器作为第三方，掌握跨网站、跨设备、跨参与方的数据，并具备清算所式的匹配与定向能力。
- 🛡️ 在 iOS、iPadOS、macOS 和 visionOS 27 中，Safari 与 WebKit 在域名层面阻止对身份解析基础设施的网络访问，防止其获取邮箱及后续追踪。
- ✉️ iCloud+ 的“隐藏我的电子邮件”可生成随机唯一邮箱地址，帮助抵御基于邮箱的追踪。
- 🔒 Apple 承诺默认阻止隐蔽和跨站追踪，同时继续支持网站提供第一方个性化服务。

---

### [PHP：新闻存档 - 2026](https://www.php.net/archive/2026.php#2026-10-21-5)

**原文标题**: [PHP: News Archive - 2026](https://www.php.net/archive/2026.php#2026-10-21-5)

2026 年 10 月 21 日，PHP 发布安全公告，修复两个可导致未认证远程代码执行的关键漏洞，所有 PHP 用户应立即升级至 PHP 8.5.12、8.4.27、8.3.36 或 8.2.35；无法立即更新时，可采取临时缓解措施，但它们不能替代更新。

- 🚨 **风险范围**：所有处理 Web 请求的 PHP 安装均受影响，包括 PHP-FPM、Apache mod_php、php-cgi、FrankenPHP 和 LiteSpeed；其中 mod_php 风险最高，已演示未认证请求可在应用代码运行前触发攻击。
- 🧨 **漏洞一**：CVE-2026-109618（GHSA-w8hw-w9fx-j79w）为 OOM 内存破坏导致 RCE，内存耗尽处理可能中断 PHP，使请求清理把仅部分初始化的内部请求数据当作有效数据。
- 🧬 **漏洞二**：CVE-2026-109619（GHSA-6wmf-4rv5-p3rp）为陈旧全局状态导致 RCE，请求拥有的内部状态可在底层内存释放后残留，后续同一 worker 请求可能在正常初始化重置前使用该状态。
- ⬆️ **更新方式**：升级至 PHP 8.5.12、8.4.27、8.3.36 或 8.2.35；源码及 Windows 源码/二进制可从官方下载页获取，Linux 发行版和 LTS 厂商已提前获得补丁，应检查厂商更新包。
- ⏳ **旧版本说明**：PHP 8.1 及更早版本不再由 PHP 项目更新；部分发行版/LTS 厂商提供回溯修复，可联系厂商或升级到受支持版本；依赖 rpms.remirepo.net 的用户应改用发行版包或从源码构建，该仓库当日不会提供更新。
- 🛠️ **源码回溯**：PHP 安全团队为 PHP 7.4、8.0、8.1 提供了最小源码回溯补丁，方便从源码构建或无法获得 LTS 厂商支持的用户。
- 🧱 **缓解 OOM 漏洞**：设置 `memory_limit=-1`，最好通过 FPM pool 或 Apache 的 `php_admin_value` 等应用无法覆盖的方式，并确认没有池、目录或应用重新设回有限值；同时降低 `post_max_size`（无上传 8M，有上传 32M），并保持 `upload_max_filesize` 小于它。
- 🌐 **缓解请求路径**：在 Web 服务器或代理层限制解码请求大小、输入字段数、multipart 分片数、请求头数量和嵌套深度，并覆盖没有可用 `Content-Length` 的请求；可用容器或 cgroup 限制作为可用性边界，优先只杀死受影响 worker，不要使用 `RLIMIT_AS` 或 `RLIMIT_DATA`。
- 🔐 **缓解陈旧状态漏洞**：设置 `session.upload_progress.enabled=0` 并重启所有 worker，应通过 `php.ini`、FPM pool 或服务器配置在请求解析前生效，不要依赖 `ini_set()` 或 FPM `.user.ini`；PHP 8.5 还应设置 `fatal_error_backtraces=0` 并重启所有 worker。
- 🧹 **其他加固**：移除按请求应用、会在初始化前产生诊断信息的无效或弃用设置；隐藏诊断信息无助于修复；修复攻击者可触发的致命错误和执行超时，包括回调、上传/导入处理及清理阶段失败。

---

### [Chrome 157 发布说明 - Chrome 平台状态](https://chromestatus.com/release-notes/157)

**原文标题**: [Chrome 157 Release Notes - Chrome Platform Status](https://chromestatus.com/release-notes/157)

本文汇总 Chrome 平台近期功能与更新，涵盖 Sanitizer API、Service Worker、Android 语言检测、Web Bluetooth、安全策略、CSS、DOM、图形与 WebGPU、性能优化及新源试用等方向。

- 🛡️ SanitizerConfig 和 Sanitizer 新增 `javascriptURLs` 选项，开发者可选择是否清理用于导航的 `javascript:` URL；未使用该选项时行为保持不变。
- 👷 Service Worker 中暴露 `ProgressEvent`，支持构造包含 `lengthComputable`、`loaded` 和 `total` 的进度事件，与其他 Worker 上下文及 XHR 标准保持一致。
- 🌐 Chrome for Android 提供 Language Detector API，可利用设备端机器学习离线检测文本语言，兼顾隐私与速度。
- 🔵 Web Bluetooth 的 `BluetoothRemoteGATTServer` 继承 `EventTarget`，支持标准事件方法，可在 GATT 服务器上派发连接级事件。
- 🔒 Chrome 157 起 Background Fetch 强制实施 CORS，与常规 Fetch 的安全策略保持一致，防止站点借此绕过 CORS 等检查。
- 🎨 CSS 新增 `corner` 简写及按角、按边的子简写，可一次设置 `border-radius` 和 `corner-shape`；`corners` 保留为兼容别名。
- 📐 CSS `position-visibility` 的 `anchors-valid` 更名为 `anchor-valid` 并明确仅默认锚点生效；同时发布 `anchor-visible`、`anchor-valid`，弃用复数版本但暂不移除。
- ✂️ CSS `text-decoration-inset` 可控制下划线、上划线和删除线相对文本边缘的内缩或延伸，支持 `auto`、长度、百分比及单值/双值语法。
- 🔤 CSS `text-overflow` 新增 `<string>` 值，可自定义截断提示文本，例如“(more)”。
- 🧩 Capability Elements 新增 `displaymode` 属性，使 `<camera>`、`<microphone>`、`<geolocation>` 能以纯图标紧凑模式渲染，同时保留原生安全保证和无障碍支持。
- 📄 新增 HTML 插入与流式方法：`before/after/append/prepend/replaceWith` 可接收 HTML，`stream{Append}HTML{Unsafe}` 返回 `WritableStream`，并支持 `runScripts` 及 Trusted Types 解析选项。
- 🖼️ HTML-in-canvas 允许用 canvas 自定义 HTML 渲染，提供布局管理、绘制能力、DOM 与 canvas 同步的渲染事件及几何更新能力。
- ⚙️ WebGPU/WGSL 支持对 `atomic<vec2u>` 使用 64 位原子最小/最大操作，无需完整 64 位整数支持即可实现相关算法。
- ⏱️ Long Animation Frames API 新增 `styleDuration` 和 `forcedStyleDuration`，帮助开发者区分样式与布局耗时。
- 🧪 新源试用包括 Connection Allowlists 嵌入执行，允许父文档限制 iframe、嵌套文档或 Worker 的外部连接；以及 Overscroll Areas，允许元素锚定到其他元素的过滚动区域并通过滑动手势显示。

---

### [Chrome 中已弃用 unload 事件 | 博客 | Chrome for Developers](https://developer.chrome.com/blog/unload-deprecated-in-chrome)

**原文标题**: [Unload event deprecated in Chrome  |  Blog  |  Chrome for Developers](https://developer.chrome.com/blog/unload-deprecated-in-chrome)

Chrome 已在 Chrome 155 中完成对 `unload` 事件的弃用，默认不再为 Chrome 及其他 Chromium 浏览器触发该事件。该事件因页面生命周期变化、移动端后台页面被静默关闭以及与 bfcache 冲突而日益不可靠，Chrome 经过多年准备和分阶段推出来消除这一不确定性，并提升返回/前进导航的即时恢复体验。

- ⚠️ `unload` 事件设计于早期网页打开、使用、关闭的简单场景，但现代页面生命周期不可预测，移动端尤其常无法执行处理器。
- 🧩 与 bfcache 存在冲突：使用 `unload` 可能导致页面无法进入 bfcache，且不同浏览器处理不一致，造成行为混乱。
- 🗓️ Chrome 从 2025 年 3 月到 2026 年 9 月分阶段弃用，持续监控破坏并收集开发者反馈，最终在 Chrome 155 完成。
- 📱 由于 iOS 上的 Chrome 使用 Safari 的 WebKit 引擎，`unload` 在 iOS 设备上仍可能触发。
- 🔓 Chrome 通过 Permission Policy API 和企业设置提供退出机制；少数网站仍可选择继续接收 `unload` 事件，但官方不建议依赖。
- 📉 影响数据显示，`unload` 使用率从 18% 的导航降至不足 4%；其作为 bfcache 唯一阻塞原因的比例从 6% 降至约 1%，约多出 5% 的导航可使用即时前进/后退。
- 🌐 Chromium 代码库将很快默认启用该变更，其他 Chromium 浏览器也会受影响；Chrome 希望其他浏览器跟进，并在 HTML 规范讨论中推动该遗留 API 退役。

---

### [面向 Web 使用场景的 JPEG XL 与 AVIF 对比 - JakeArchibald.com](https://jakearchibald.com/2026/jpeg-xl-vs-avif/)

**原文标题**: [JPEG XL vs AVIF for web use-cases - JakeArchibald.com](https://jakearchibald.com/2026/jpeg-xl-vs-avif/)

overview summary
本文基于最新编码器与浏览器实测，比较 JPEG XL 与 AVIF 在网页场景中的表现。总体结论是：网页有损照片和多数常见场景应优先选择 AVIF 4:4:4，并视情况使用较高 effort；JPEG XL 在无损、JPEG 无损转码和个别图像上更有优势，jixel 缩小了差距但仍有明显权衡。

- 📸 有损照片：AVIF 通常文件更小；默认 effort 下最佳 JPEG XL 仍大 15–25%，最高 effort 下差距缩小到 6–20%，但个别图像 JPEG XL 可反超。
- 🧩 编码器差异：jixel 多数情况下比 libjxl 更小，但存在为指标“取巧”而观感变差的案例；透明细节场景例外。
- 🖼️ 截图与插画：AVIF 明显更优；JPEG XL 默认 effort 大 30–90%，最高 effort 大 20–70%；有损 AVIF 已足够，除非需要位精确结果。
- 🪟 透明度：AVIF 大幅领先；libjxl 默认/最高 effort 分别大约 31–44%/61–70%，jixel 因无损 alpha 可达 AVIF 的 2–3 倍。
- ⚡ 性能：AVIF 综合编码更快、更省内存、解码更快；JPEG XL 中质量解码约慢 2–3 倍，高质量时差距缩小。
- ⚙️ effort 建议：AVIF 和 jixel 提高 effort 通常值得；libjxl 提高 effort 收益很小，却显著更慢、更耗内存。
- 🎨 4:2:0：AVIF 4:2:0 不应作为默认，通常不减小文件且更难达到高质量；4:4:4 更稳妥，截图高质量场景是例外。
- ✅ 质量稳定性：单一质量设置下各编码器波动方向相似，未发现明显风险。
- 🌈 渐进加载：JPEG XL 渐进在高 effort 下几乎免费；AVIF 渐进目前仅 Chrome 支持、Firefox 进行中，更复杂但预览更可控、文件常更小、解码更快。
- 🌟 HDR：JPEG XL 缺少浏览器可用的 gain maps，相比 AVIF 是重大限制；非 gain map HDR 下指标分歧较大。
- 🔁 JPEG 转码：JPEG XL 可无损将现有 JPEG 缩小 9–20%，大图解码有时更快。
- 🏆 无损：JPEG XL 明显胜出；无损 WebP 约大 9–17%，无损 AVIF 约大 30–120%，但网页很少需要无损。
- 🎞️ 动画：不建议使用动画图像格式，视频格式更合适；动画 AVIF 实测远小于动画 JPEG XL，但播放实现仍不理想。
- 🧭 当前建议：默认 AVIF 4:4:4 并使用可接受的最高 effort；若 AVIF 文件异常大，再尝试 jixel 的 JPEG XL，并用自有图片实测，避免依赖二手信息或 AI 生成的误导结论。

---

### [JXL 艺术画廊 – JPEG XL](https://jpegxl.info/art/big_gallery.html)

**原文标题**: [JXL Art gallery – JPEG XL](https://jpegxl.info/art/big_gallery.html)

该画廊是 JXL Art Gallery 的极简 JXL 艺术作品索引，按 2021—2025 年组织，收录大量以极小文件体积呈现的图像，突出 JPEG XL 在超低码率与实验性视觉表达上的可能性。

- 🖼️ HDR 作品被放在单独页面，避免浏览时因高动态范围效果“闪瞎眼”。
- 📊 画廊共包含 194 张嵌入式图像，总计 391.0 百万像素，合并体积仅 8,168 字节（7.98 KiB）。
- ⚡ 整体码率低至 0.0001671 bits per pixel，体现极高的压缩效率与实验性质。
- 📅 作品按 2021、2022、2023、2024、2025 年份分区展示，时间线清晰。
- 🎨 题材涵盖抽象图案、几何结构、自然模拟、渐变纹理、旗帜、像素风、幽默梗图与生成艺术。
- 👤 多数作品由 Jon Sneyers 创作，同时包含 jjido、CrushedAsian255、Lonnie、MSLP、Tirr 等多位贡献者。
- 🧪 许多作品体积极小，常见为 20—50 字节左右，部分标题本身也带有实验与幽默色彩。
- 🔬 整体内容强调“极小字节数 + 高像素数”的对比，展示 JXL 艺术在压缩、规则生成与视觉错觉方面的探索。

---

### [用 CSS random() 函数拥抱俏皮的不完美 — Smashing Magazine](https://www.smashingmagazine.com/2026/10/embracing-playful-imperfection-css-random-function/)

**原文标题**: [Embracing Playful Imperfection With The CSS random() Function — Smashing Magazine](https://www.smashingmagazine.com/2026/10/embracing-playful-imperfection-css-random-function/)

文章介绍原生 CSS `random()` 函数如何为网页带来可控的随机性与俏皮的不完美。作者 Brecht De Ruyte 通过多个 CodePen 演示，展示无需 JavaScript 或 Sass 循环即可实现有机排版、弹跳字母、倾斜卡片、滚动展开卡组、随机速度滚动和散景效果，并讨论适用场景、浏览器支持与无障碍注意事项。

- 🎯 核心价值：`random()` 来自 CSS Values and Units Level 5，可在浏览器中生成伪随机值，减少对 JavaScript 动画库或大量预处理器生成 CSS 的依赖。
- 🧩 基本语法：`random(min, max, step?)`；最小值和最大值必须使用相同单位，`step` 可让随机值落在离散步进上。
- 🔑 缓存键：通过 `random(--key element-scoped, ...)` 让多个属性共享同一个随机值，例如让卡片的宽高保持一致。
- 🌐 浏览器支持：Safari 已支持，Chrome 156 正在推出，Firefox 有积极信号；建议用 `@supports` 做渐进增强。
- 🚀 未来功能：`random-item()` 可从颜色或关键字列表中随机选择，目前尚无浏览器支持。
- ✍️ 演示一：给字母添加轻微旋转、位移和透明度变化，悬停时恢复整齐；需用 `aria-hidden` 与 `aria-label` 避免屏幕阅读器逐字朗读。
- 🏀 演示二：字母弹跳使用随机跳跃高度、时长、延迟和压扁参数；负延迟可让动画在页面加载时立即运行。
- 🃏 演示三：卡片随机倾斜并动态调整阴影，悬停或键盘聚焦时回正。
- 🎞️ 演示四：用 `sibling-index()` / `sibling-count()` 计算扇形排列，再用 `random()` 添加手作抖动，并结合滚动时间线展开卡组。
- 🌊 演示五：用 `random()` 和 `pow(-1, sibling-index())` 实现不同速度与方向的滚动文字漂移。
- 📷 演示六：`random()` 配合 `blur()`、`opacity` 和 `scale` 模拟浅景深散景，悬停时对焦清晰。
- ✅ 适用场景：装饰性微不完美、环境动画去同步、生成式背景、编辑设计，以及在数学结构上叠加随机细节。
- ⚠️ 避免场景：核心布局与网格、正文排版、交互目标；始终尊重 `prefers-reduced-motion`，并确保悬停/聚焦时恢复可用性。
- 💡 结论：随机并非要破坏设计系统，而是在一致性基础上加入俏皮的不完美；内置能力带来零 JavaScript 开销的乐趣。

---

### [Chrome 156 发布说明 - Chrome 平台状态](https://chromestatus.com/release-notes/156)

**原文标题**: [Chrome 156 Release Notes - Chrome Platform Status](https://chromestatus.com/release-notes/156)

Chrome 157 带来多项网络、CSS、存储、图形、实时通信与弃用更新，重点提升模块加载可靠性、CSS 表现力、IndexedDB 稳定性及 WebRTC 调试能力。

- 🌐 模块加载失败不再被缓存，开发者可通过再次调用 `import()` 手动重试，改善不稳定网络下的模块使用体验。
- 📦 压缩字典传输更新：获取 `rel=compression-dictionary` 链接时使用正确请求目标，并正确设置 mode、credentials、referrer、referrerpolicy，同时考虑 `crossorigin` 与 `referrer` 属性。
- 🔐 WebTransport 支持通过 `WebTransportOptions` 传递自定义 HTTP 请求头，并可检查服务器响应头，便于在 CONNECT 握手中携带元数据、认证令牌和自定义参数。
- 🧭 新增 CSS 导航来源伪类，可选择发起导航的链接、按钮或表单元素，并在整个导航过程中保持选中。
- 🎲 新增 CSS `random()` 函数，可在指定范围内生成随机数值，用于随机布局等场景，并支持通过 `<random-key>` 控制随机值缓存与共享。
- 📜 单轴滚动容器扩展 `overflow`，支持 `scroll` 与 `clip` 组合值，使 `position: sticky` 可按轴受不同祖先滚动容器约束。
- 🧲 `scroll-snap-type: pair` 可让容器在一个轴吸附到某元素时，另一轴也吸附到同一元素。
- 🗄️ IndexedDB 后端改用 SQLite，Web API 不变，预期提升可靠性和一定性能；当前适用于新数据存储，现有 LevelDB 数据不受影响，后续将迁移旧数据。
- 🎮 WebGPU WGSL 片段深度支持 `less`/`greater` 修饰符，可显式设置缓冲模式并启用 early-Z 优化。
- 📞 WebRTC 诊断日志 API 允许授权应用触发诊断数据收集用于本地调试，并可在用户授权下与浏览器厂商共享；管理员可通过企业策略启用。
- 🚫 移除 FencedFrame 元素和 `window.fence` API：M156 保留占位并让相关 API 变为 no-op，M157 开始受控移除，稳定后视回归情况全面移除。

---

### [记录光线而非模拟光线 | Miris](https://www.miris.com/blog/recording-light-instead-of-simulating-it?utm_source=web_referral&mrls=web_referral&utm_medium=public_relations&mrlc=public_relations&utm_campaign=raz-pr&utm_content=plugin&prg=fidelity&utm_term=frontend&dp=dp)

**原文标题**: [Recording light instead of simulating it | Miris](https://www.miris.com/blog/recording-light-instead-of-simulating-it?utm_source=web_referral&mrls=web_referral&utm_medium=public_relations&mrlc=public_relations&utm_campaign=raz-pr&utm_content=plugin&prg=fidelity&utm_term=frontend&dp=dp)

本文介绍了一种以辐射场（Radiance Field）和高斯泼溅（Gaussian Splatting）为核心的实时 3D 渲染与流式传输方案。核心观点是：与其在运行时模拟光线，不如离线记录光线行为，再通过分层流式传输把高保真 3D 内容快速送达浏览器和移动设备。文章对比了路径追踪、光栅化 PBR 与辐射场方案，强调辐射场在保真度和 GPU 友好性上的优势，并用 Miris 的流式方案说明 40GB OpenUSD 资产如何在慢速 4G 下约 10 秒内可交互、30 秒变清晰、2 分钟达到照片级效果。

- ⚡ 核心主张：辐射场可在消费级硬件上实时渲染，并达到传统光栅化 PBR 在结构上难以达到的保真度。
- 💡 关键区别：PBR 模拟“光应该怎样”，辐射场记录“光实际怎样”，因此全局光照、半影、遮蔽、反射、次表面散射等效果天然包含在数据中。
- 🧠 性能原因：高斯泼溅每像素执行相同、独立、顺序读取的小计算，符合 GPU 擅长的并行模式；无需几何、材质和灯光也能以 120fps 在手机上渲染。
- 📱 示例数据：同一场景在 iPhone 上单帧约 8 毫秒，而源资产曾是 40GB OpenUSD 文件。
- 🔍 传统 PBR 瓶颈：依赖直接光照、屏幕空间近似、阴影贴图和多次渲染 pass；场景光学复杂度越高，帧成本越高，且结果仍受“模拟模型”上限约束。
- 🎞️ 辐射场优势：保真度由训练视图和编码容量决定，而不是 BRDF；无需 UV、材质和灯光绑定，静态场景下仅相机移动即可回放已记录的光照。
- 📦 核心问题：完整辐射场单资产原始数据可达 GB 级，传统 glTF/USD 下载模式无法满足 Web 实时交付。
- 🚚 空间流式传输：分层细化、按屏幕误差优先加载、视锥剔除、自适应码率；首帧约 150KB 即可交互，无需加载条或弹出式加载。
- 📊 对比数据：40GB OpenUSD 在 1.4Mbps 慢速 4G 下约需 2.5 天；优化 glTF 约 4GB、约 6 小时且永远达不到照片级；辐射场流约 10 秒交互、30 秒清晰、2 分钟照片级。
- 🧩 集成方式：只需两行 three.js 代码，`MirisStream` 继承 `Object3D`，可直接放入场景图并兼容相机、控制器和渲染循环。
- 🔮 未来趋势：Three.js r186 将原生支持 `GaussianSplatMesh`，但流式传输与 LOD 仍是关键缺失层；编码会变化，但流式接入方式可保持不变。

---

### [使用 calc-size() 让高度适应背景图案尺寸](https://ishadeed.com/article/fit-height-background-pattern-calc-size/)

**原文标题**: [Fit height to background pattern size with calc-size()](https://ishadeed.com/article/fit-height-background-pattern-calc-size/)

内容将围绕简洁表达、案例或数据支撑、知识学习与提醒，以及高质量内容推荐展开。
- ✍️ 用简洁语言清楚解释观点，避免过多文字。
- 📊 至少包含一个数据或清晰示例。
- 💡 帮助学习新知识，或提醒已有知识。
- ✅ 承诺提供顶级质量的内容推荐。

---

### [CrUX 中现已提供实验性软导航指标 | 博客 | web.dev](https://web.dev/blog/crux-experimental-soft-navs)

**原文标题**: [Experimental soft navigation metrics now available in CrUX  |  Blog  |  web.dev](https://web.dev/blog/crux-experimental-soft-navs)

Chrome 于 2026 年 10 月 13 日在 CrUX 中推出实验性软导航指标，将 SPA 内部页面切换纳入 Core Web Vitals 测量，以更完整反映真实用户体验；大多数网站指标不变，只有高软导航占比的 SPA 会明显改善。

- 🧪 背景：SPA 通过 JavaScript 动态更新内容和 URL，形成“软导航”，此前 CrUX 只记录首次硬加载，难以跨站比较。
- 📊 三项实验指标：LCP、INP、CLS 均新增“含软导航”版本，分别覆盖硬导航与软导航、按单次软导航分段、按页面视图和 URL 分段统计。
- 🔍 INP 变化：交互响应按每次软导航或硬导航单独衡量，不再把整个 SPA 会话的交互都归因到首次页面加载。
- 📈 影响范围：约 70% 的源站几乎没有软导航流量，仅 7%–11% 的源站超过一半页面浏览为软导航；但在前 1000 网站中，Android 和桌面端分别有 35% 和 42% 高度依赖软导航。
- ⚡ 高软导航 SPA：LCP 通常改善，Android 上 75%–100% 软导航占比站点的“良好”LCP 从 26% 升至 87%；INP 通过率约翻倍，但仍可能受主线程 JavaScript 影响；CLS 因按页面视图分段而改善。
- 🛠 获取方式：2026 年 10 月发布起，可通过 CrUX BigQuery、CrUX API、CrUX History API 和 CrUX Vis 查看这些实验指标。
- 🧭 后续计划：指标暂标记为实验性并开放社区反馈，目标 2027 年 5 月转正；转正后 Search Console 将切换使用新数据，11 月还计划加入导航类型和 FCP 的实验性软导航指标。

---

### [用数学平衡你的标题样式——克雷格·阿博特](https://www.craigabbott.co.uk/blog/2026/using-maths-to-balance-your-heading-styles/)

**原文标题**: [Using maths to balance your heading styles - Craig Abbott](https://www.craigabbott.co.uk/blog/2026/using-maths-to-balance-your-heading-styles/)

文章介绍了一套用模块化比例（modular scale）系统化设计六个标题层级的方法：从正文基础字号出发，用统一比例计算字号与间距，在不依赖颜色、斜体或全大写的情况下保持标题可识别、可访问且视觉平衡。

- 🎯 核心目标是让 H1–H6 既视觉可区分又兼顾可访问性，尤其避免仅靠颜色传达层级。
- ♿ 强调不能依赖颜色，因为色觉缺陷用户和 Windows 高对比度/forced-colors 模式会失去颜色差异；也应避免斜体和全大写，以照顾阅读困难与阅读障碍用户。
- 📐 使用模块化比例：设置 `--ratio: 1.5`、`--s0: 1.2rem`，再按比例生成 `--s1` 到 `--s3` 及 `--s-1` 到 `--s-3`，所有字号与间距都来自同一系统。
- 🔠 视觉线索按强弱排序：字号最强，其次间距，最后字重；先用最强线索，不够时逐层叠加。
- 📏 字号分配为 `h1: --s3`、`h2: --s2`、`h3: --s1`，`h5/h6` 回落到正文大小 `--s0`，并坚持标题不应小于其引导的正文。
- 🧮 H4 使用“半步”解决 H3 到 H4 之间约 19px 到 28px 的视觉跳跃：取几何平均数，即 `calc(var(--s0) * sqrt(var(--ratio)))`，约 23.5px。
- 🧱 间距采用 prose flow 与 lobotomized owl 选择器：清零外边距，通过 `--flow-space` 控制元素上方间距；标题上方间距更大，标题下方间距更小以拉近相关内容。
- ⚖️ 字重只用于 H6，将其降到 `500`，既与 H5 区分，也避免与 `<strong>` 混淆；前提是字体需包含所需字重，最好使用可变字体。
- 🎨 颜色只作为可选增强：H5、H6 可略微降低透明度，但即使进入 forced-colors 模式，层级仍能靠字号、间距、字重维持。
- 🧩 另一写法是用 `pow()` 直接从基数计算每一步，如 `pow(var(--ratio), 3)`；H4 可写成 `pow(var(--ratio), 0.5)`，结果相同但更统一。
- 🛠️ 最终方案形成可维护的设计系统：减少“凭感觉调像素”，让字号、间距和层级始终基于同一比例保持平衡。

---

### [我们真的需要 alpha() 吗？ - YouTube](https://www.youtube.com/watch?v=Pfj9OmvqU0Q)

**原文标题**: [Do we really need alpha()? - YouTube](https://www.youtube.com/watch?v=Pfj9OmvqU0Q)

该文本是一组 YouTube 网站页脚/导航链接及版权声明，主要涵盖平台介绍、联系渠道、创作者与广告服务、开发者资源、法律与隐私政策、功能说明以及 Google 的版权信息。

- 🏢 平台介绍与媒体信息：About、Press
- ⚖️ 版权与联系渠道：Copyright、Contact us
- 🎬 创作者、广告与开发者入口：Creators、Advertise、Developers
- 🔐 法律、隐私与安全政策：Terms、Privacy、Policy & Safety
- ⚙️ YouTube 运作说明与功能测试：How YouTube works、Test new features
- ©️ 版权归属：© 2026 Google LLC

---

### [错误](https://tetralogical.com/blog/2026/10/15/wcag3/)

**原文标题**: [Error](https://tetralogical.com/blog/2026/10/15/wcag3/)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='tetralogical.com', port=443): Max retries exceeded with url: /blog/2026/10/15/wcag3/ (Caused by ProxyError('Unable to connect to proxy', RemoteDisconnected('Remote end closed connection without response')))

---

### [](https://theconsensus.dev/p/2026/10/04/compression-and-concatenation-on-the-web.html?focus=1)

**原文标题**: [
    Compression and concatenation on the web - The Consensus
  ](https://theconsensus.dev/p/2026/10/04/compression-and-concatenation-on-the-web.html?focus=1)

本文探讨 Web 压缩与压缩流拼接：gzip、Brotli、Zstandard 在服务端预压缩、动态压缩及多段文件合并中的实际表现。重点结论是：压缩能减少传输字节，但拼接压缩文件不仅取决于格式规范，还取决于浏览器、curl 等客户端是否真正支持；gzip 虽可简单拼接但客户端兼容性差，Brotli 需额外工具或扩展，zstd 原生支持拼接且浏览器可直接解码。

- 📉 **压缩目标**：减少服务端到客户端的传输字节；需在压缩率与压缩速度之间权衡，静态资源可承担更高压缩成本。
- 🧭 **协商机制**：客户端通过 `Accept-Encoding` 声明支持的格式，服务端用 `Content-Encoding` 返回对应压缩内容。
- ⚡ **静态预压缩**：对静态 HTML/CSS/JS 等可在构建时生成 `.gz`、`.br`、`.zst` 文件，避免请求时动态压缩的开销。
- 🌐 **使用现状**：gzip、Brotli、zstd 是主要 Web 压缩格式；Brotli 在 CDN 流量中占比领先，gzip 在非 CDN 流量中仍占多数。
- 🧩 **gzip 拼接**：命令行 `cat` 多个 gzip 文件后 `gunzip` 可还原，但 curl 可能报错，Chrome 只显示第一段并静默丢弃后续内容。
- 🛠️ **gzip 安全拼接**：zlib 示例程序 `gzjoin.c` 可生成客户端可读的拼接文件，且无需重新压缩，但仅作为示例存在，主流语言缺少内建 API。
- 🚫 **Brotli 默认限制**：Google Brotli 参考实现不支持 gzip 式直接拼接，简单 `cat` 后会产生损坏输入。
- 🔧 **Brotli 变通方案**：rust-brotli 提供可拼接/可追加标志，并可在末尾追加特定字节，使 Google Brotli、curl 和浏览器都能解码；Google Brotli 的流偏移方案支持不完整。
- ✅ **zstd 原生优势**：zstd 从设计上支持拼接，直接 `cat` 多个 `.zst` 文件即可被 zstd、curl 和 Chrome 正确解码。
- 🔄 **规范演进**：文章关注的不仅是规范缺口，而是实现者如何在不产生“其他实现无法解码”的文件前提下扩展兼容性。

---

### [](https://nolanlawson.com/2026/10/19/do-web-components-have-a-future-if-nobody-is-writing-them/)

**原文标题**: [Do web components have a future if nobody is writing them? | Read the Tea Leaves](https://nolanlawson.com/2026/10/19/do-web-components-have-a-future-if-nobody-is-writing-them/)

本文讨论 AI 代理编码兴起后 Web Components 的复用价值与未来前景。作者回顾“use the platform”与 Polymer 的渊源，分析 Google Modern Web Guidance 对 Web Components 的冷淡态度，并指出代理生成代码、框架可替换和 DIY 组件趋势正在削弱其核心卖点；但微前端沙箱、独立组件复用等场景仍有机会，且 Web Components 已通过影响平台标准取得不可逆成果。

- 🧭 “use the platform”常被误读为“用 Web Components”，这源于 Polymer 的口号；作者原本强调的是更高效的 HTML/CSS 平台特性。
- 🤖 Google 的 Modern Web Guidance 面向 AI agent 推荐现代浏览器能力，但 Web Components 更像事后补充，指南甚至劝先判断是否真的需要自定义元素。
- 🧩 仅有少数场景获推荐：Chrome 扩展复杂 UI 的 shadow DOM、设计系统、可嵌入组件和自包含 UI，范围较窄。
- ⚠️ AI 编码削弱 Web Components 的原始前提：手写 HTML、代码稀缺、复用是经济必需；如今 UI 可从零 vibe-code。
- 🏗️ 框架层也被视为可丢弃，组件库从“开箱即用”转向 shadcn 式 DIY；LLM 让样板代码成为优势，不利于 shadow DOM 等特性。
- 🛡️ 可挽救方向之一是微前端与 agent 沙箱：Web Components 可隔离 CSS、事件和全局变量，但 iframe 提供更强隔离。
- ♻️ 复用仍重要：如 `<emoji-picker>` 这类独立客户端组件适合打包为 Web Component；AI 时代共享代码未必减少。
- ⚛️ React 虽可能成为 agent 的复用层，但作者认为它未必是终点，虚拟 DOM 仍有性能开销；最终框架可能只是 agent 的脚注。
- 🧪 作者仍喜欢 Web Components，本站主题选择器就是 light DOM 组件，但需明确要求 agent 才会使用。
- 🚧 SSR、样式共享、可访问性等长期问题仍未解决，倡导者需加倍证明其相关性。
- 🏆 即使未来式微，Web Components 已赢得“解释平台”的胜利，并影响 Open UI、可定制 select、popover、invoker commands 等标准。

---

### [](https://chartist.dev/)

**原文标题**: [Chartist](https://chartist.dev/)

overview summary
Chartist 是一个自 2014 年起开源的轻量级 SVG 图表库，主张“简单图表，交给 CSS 打扮”：它只输出带可预测类名的纯 SVG，样式完全由使用者的 CSS 控制，不用 Canvas、没有依赖、没有主题引擎。它提供折线、柱状、饼/环/仪表和组合图，支持响应式、服务端渲染和 CDN 直接引入，并以开放的插件管线支持扩展；相比 Chart.js 等库体积更小、许可更宽松，但内置图表类型和交互功能较少。

- 🎨 **核心理念**：Chartist 负责绘制干净、响应式的 SVG 图表，着色、线条和文字等外观都交给 CSS 类与自定义属性来定义。
- 📦 **体积小巧**：核心仅 5.8 kB，核心加折线图约 14.5 kB；按需导入，未用到的图表不会打包。
- 📊 **图表类型**：折线、面积、散点、柱状（并排或堆叠）、饼图、环形图、仪表盘，以及柱线组合图。
- 🧩 **组合图表**：可在同一图表中叠加柱状与折线，并各自绑定左、右独立的 Y 轴。
- 📱 **响应式双方案**：既可按窗口宽度，也可按图表容器宽度（实验性），断点条件直接用 CSS 写法表达。
- 🖥️ **服务端渲染**：输出真实 SVG 文本标签，可用 `renderToString` 生成 PDF、邮件和图片所需内容。
- ⚙️ **无需构建步骤**：原生 ES Module，可直接从 CDN 引入，也支持 npm 安装。
- 🔌 **开放的插件管线**：resolve、prepare、layout、compose、scene、render、mount 七个阶段各有事件，任何元素都可在 `compose` 阶段修改、替换或装饰。
- 🧰 **官方扩展包**：`@chartist-js/tooltips`（鼠标、触摸、键盘提示）、`@chartist-js/essentials`（轴标题、趋势线、对数轴）、`@chartist-js/terminal`（终端与文本艺术图）。
- 📈 **使用规模**：每月 49.4 万次 npm 下载、GitHub 13.4k 星、72.8k 个公开仓库依赖，自 2014 年起已投产 12 年。
- 🆚 **横向对比**：一处折线图 14.5 kB，明显小于 Chart.js 49.4 kB、ApexCharts 172.3 kB、Highcharts 104.7 kB。
- 🏆 **优势场景**：包体小、纯 SVG、用现有 CSS 定制、CDN 即用、MIT 或 WTFPL 宽松许可、无商业授权费用。
- ⚠️ **相对短板**：开箱图表类型较少，工具提示、缩放、平移等交互需借助插件或自行实现。
- 🧑‍🤝‍🧑 **生态封装**：React、Angular、Vue、Svelte、Node、Ember、Blazor、Rails、R、WordPress 等均有社区封装。
- ✍️ **文档体验**：文档示例全部实时可编辑，改数据或 CSS 即刻重绘，无需沙箱站点或打包器。
- 🚀 **快速上手**：`npm install chartist`，一次导入、一次函数调用即可得到一张图。

---

### [](https://chartist.dev/docs/coming-from-1x/)

**原文标题**: [Coming from 1.x · Chartist](https://chartist.dev/docs/coming-from-1x/)

Chartist v2 在保留 1.x 类 API、样式和导出兼容性的同时，新增函数式 API、组合图、SSR 等能力；迁移核心是启用 compat 处理 1.x 事件与旧插件，并逐步把类用法迁移到函数式 API。2.x 仅弃用类相关 API，3.0 才移除。

- ✅ 1.x 代码可直接运行：`LineChart`、`BarChart`、`PieChart` 等类、构造参数、导出、CSS 类名和默认样式均保留，v2 通过截图测试对齐 1.5.0。
- 🧩 v2 在同一引擎上新增 `lineChart()`、`barChart()`、`pieChart()` 和 `chart()` 函数式 API，类与函数可在同一页面并存，支持逐图迁移。
- ⚠️ 1.x 事件（`data`、`optionsChanged`、`draw`、`created`、`animationBegin/End`）默认不再自动触发；需在 `plugins` 中加入从 `chartist/compat` 导入的 `compat`。
- 🔌 1.x 插件在类用法中需配合 `compat`；在函数式 API 中需用 `fromLegacyPlugin()` 包装，普通函数插件会被函数 API 拒绝。
- 🧱 函数返回句柄：立即渲染（类为下一 tick）、容器尺寸变化重绘、`update({ data })`、`setOptions()`、`detach()`/`destroy()`，v2 事件改为 `compose` 等管线事件。
- ✍️ 1.x `draw` 处理器应改写为 v2 插件，通过 `compose` 在渲染前修改场景节点；这样还可兼容服务端渲染。
- 🚫 2.x 弃用类及仅类相关 API，3.0 移除：图表类改为函数；选项类型改为 `*PresetOptions`；轴类改用 `autoScaleAxis()` 等；`EventEmitter`/1.x 事件类型从 `compat` 导入。
- 🏷️ `labelInterpolationFnc` 更名为 `labelTransform`，旧名仍可用，同时设置时 `labelTransform` 优先。
- 🧩 社区旧插件多依赖全局 `Chartist` 和 `Chartist.plugins`；导入 `chartist/compat` 会补齐全局，再按模块/UMD/打包器方式加载脚本并用 `fromLegacyPlugin` 包装。
- 📦 仅加载一份 Chartist；`compat` 模块与已有 UMD 全局冲突时会警告，双副本会破坏插件的 `instanceof` 类型检查。
- 🆕 函数式 API 独享：组合图、容器查询响应式、`toScene()`/`renderToString()` SSR、v2 插件管线、`setOptions()` 与 `on` 首屏监听、更严格类型。
- 🎨 所有图表可用 CSS 自定义属性（如 `--ct-series-a`、`--ct-line-width`）和可选无障碍调色板；UMD 仍发布但仅作兼容，旧 0.x 文件名为副本，0.x API 不回归。
- 🛠️ v2 修复多项 1.x 行为：轴 `low`/`high` 优先于柱状图零线、`fixedScaleAxis` divisor 末刻度、甜甜圈宽度/标签位置、`stackMode`、舍入、动画事件、`off()` 只移除自身监听、整圆扇区、降序 x、空值缺口、标签重叠、折线 `referenceValue`、series 16–26 配色、iframe/JSDOM、打印缩放、`reverseData` 的 meta 等。
- 📚 迁移建议：先升级并加入 `compat` 检查事件，再逐图把构造函数换成函数，最后把 `draw` 处理器和旧插件迁移为 v2 插件或 `fromLegacyPlugin`。

---

### [滚动触发动画调试器（开发者工具扩展）– Bram.us](https://www.bram.us/2026/10/14/scroll-triggered-animations-debugger-devtools-extension/)

**原文标题**: [Scroll-Triggered Animations Debugger (DevTools Extension) – Bram.us](https://www.bram.us/2026/10/14/scroll-triggered-animations-debugger-devtools-extension/)

Bramus 发布了 Scroll-Triggered Animations Debugger 浏览器 DevTools 扩展，用于可视化和调试 CSS Scroll-Triggered Animations，并提供 Chrome 商店下载与 GitHub 反馈渠道。

- 🧩 扩展会在 Chrome DevTools 的 Elements 面板中新增“Scroll-Triggered Animations”面板。
- 🗺️ 提供交互式 minimap，用于可视化滚动容器、元素和 subject。
- 🎞️ 同时支持 ScrollTimeline（`scroll()`）与 ViewTimeline（`view()`）。
- 🚦 状态灯会在触发激活时由红色（Inactive）变为绿色（Active），并兼容 `position: sticky`。
- 🎨 可显示并实时编辑 `timeline-trigger-activation-range`（蓝色）与 `timeline-trigger-active-range`（绿色）。
- 📦 扩展已上架 Chrome Web Store，GitHub 仓库可用于报告问题和提交功能请求。
- 🧪 背景：作者结合 2023 年 Scroll-Driven Animations Debugger 的架构与 CodePen 可视化原型，通过 Antigravity/Gemini 快速构建了该扩展。
- ⚠️ 已知限制：使用 `90vh` 等相对或视口单位时，范围编辑器会显示为计算后的 px，因为浏览器 API 无法读取作者书写的原始单位。
- 🐞 iframe 内元素无法工作，受 Chrome DevTools bug（crbug/1480418）影响；在 CodePen 中需使用独立 Debug View 打开。
- 🔮 未来计划：修复问题并增加增强功能；长期希望 Chrome DevTools 内建支持后扩展自然淘汰。
- 📣 作者鼓励通过 Bluesky、Mastodon、LinkedIn 等社交平台分享传播。

---

### [滚动触发动画调试器 - Chrome 网上应用店](https://chromewebstore.google.com/detail/scroll-triggered-animatio/ganooodmdnigcfdddlijnhkipjklbgag)

**原文标题**: [Scroll-Triggered Animations Debugger - Chrome Web Store](https://chromewebstore.google.com/detail/scroll-triggered-animatio/ganooodmdnigcfdddlijnhkipjklbgag)

该 Chrome DevTools 扩展用于可视化和调试 CSS 滚动触发动画（`timeline-trigger`、`animation-trigger`、`trigger-scope`）。安装后会在 Elements 面板新增“Scroll-Triggered Animations”窗格，实时展示滚动容器、动画元素与受跟踪主体，并支持实时编辑触发范围。

- 🛠️ **用途**：帮助开发者调试和可视化 CSS Scroll-Triggered Animations。
- 🎯 **核心能力**：可视化滚动容器、动画元素，以及 ViewTimeline 下的受跟踪主体。
- 🔄 **兼容类型**：支持 ScrollTimeline（`scroll()`）和 ViewTimeline（`view()`）。
- 🚦 **状态指示**：触发器激活时，状态灯由红色（Inactive）变为绿色（Active）。
- 📌 **布局兼容**：可与 `position: sticky` 正常配合使用。
- 📐 **范围可视化**：用蓝色显示 `timeline-trigger-activation-range`，用绿色显示 `timeline-trigger-active-range`；ScrollTimeline 下为虚线，ViewTimeline 下为阴影框。
- ✏️ **实时编辑**：可通过下拉框和输入框实时修改激活范围与活动范围；空间不足时可用“Edit Values”折叠编辑区。
- 🧭 **使用方式**：像平常一样在 DevTools 中检查元素，再选择“Scroll-Triggered Animations”窗格查看实时可视化。
- 📊 **工具栏信息**：可在多个动画间切换，并查看状态灯、触发器名称与操作、滚动容器名称、时间线类型，以及总滚动进度、效果进度和实际滚动偏移（像素）。
- ⚙️ **缩放控制**：右上角可设置缩放因子，通常无需手动设置，可视化会自动适配空间。
- 📦 **版本信息**：版本 1.0.0，2026 年 10 月 14 日更新，大小 137KiB，语言英语，作者 Bramus Van Damme，20 名用户，暂无评分。
- 🔒 **隐私说明**：开发者声明不收集或使用数据，不出售给第三方，也不用于无关用途或信贷/贷款评估。

---

### [GitHub - bramus/scroll-triggered-animations-debugger-extension：用于调试滚动触发动画的浏览器扩展 · GitHub](https://github.com/bramus/scroll-triggered-animations-debugger-extension/)

**原文标题**: [GitHub - bramus/scroll-triggered-animations-debugger-extension: Browser extension to debug Scroll-Triggered Animations · GitHub](https://github.com/bramus/scroll-triggered-animations-debugger-extension/)

该仓库介绍一个用于调试 CSS Scroll-Triggered Animations 的 Chrome DevTools 浏览器扩展，可可视化滚动容器、动画元素与触发状态，并支持实时编辑触发范围；扩展可从 Chrome Web Store 安装，目前为闭源。

- 🧩 扩展用途：在 Chrome DevTools 中可视化并调试 CSS Scroll-Triggered Animations（timeline-trigger、animation-trigger、trigger-scope）。
- 🎯 可视化内容：滚动容器、动画元素，以及 ViewTimeline 跟踪的 subject。
- 📜 时间线支持：支持 ScrollTimeline（scroll()）和 ViewTimeline（view()）。
- 🚦 状态指示：触发器激活时，状态灯由红色（Inactive）变为绿色（Active）。
- 📌 兼容性：可与 position: sticky 正常配合使用。
- 🟦🟩 范围调试：显示 timeline-trigger-activation-range（蓝色）和 timeline-trigger-active-range（绿色）调试线/框，并支持实时编辑。
- 🛠️ 使用方式：安装后 Elements 面板新增“Scroll-Triggered Animations”窗格；检查元素即可查看，并随页面滚动实时更新。
- 📊 工具栏信息：可切换多个动画，显示状态灯、触发器名称与动作、滚动容器名称、时间线类型、总滚动进度、效果进度及实际滚动偏移（px）。
- ⚙️ 视图控制：右上角可设置缩放因子，通常自动适配可用空间；底部范围编辑器可通过“Edit Values”折叠/展开并实时修改。
- 💬 FAQ 与反馈：FAQ 可在 Issue 列表中通过标签查找（GitHub 默认隐藏已关闭 Issue，需使用直链）；报告问题需提供可复现 URL。
- 🔒 许可与仓库：扩展目前闭源；仓库公开，含 1 次提交，0 stars、0 watchers、0 forks。
- 🛒 安装渠道：可从 Chrome Web Store 获取扩展。

---

### [Expo — 使用 React 构建原生应用](https://expo.dev/?utm_campaign=mobile-ai-infra&utm_source=email&utm_medium=frontendfocus&utm_term=home&utm_content=Cooperpress)

**原文标题**: [Expo — Build native apps with React](https://expo.dev/?utm_campaign=mobile-ai-infra&utm_source=email&utm_medium=frontendfocus&utm_term=home&utm_content=Cooperpress)

Expo 是面向“代理式移动开发”的基础设施平台，提供 CLI、开发工具、云模拟器、CI/CD、分发、OTA 更新与生产监控，帮助团队和 AI 代理从开发、测试到部署和观测全流程构建移动应用；平台强调单代码库覆盖 Android、iOS 和 Web，并获得大量开发者与社区采用。

- 🚀 定位为 Agentic mobile infrastructure，支持用 CLI 和开发工具构建、测试、发布并持续学习每次发布。
- 📊 规模数据亮眼：3M+ 开发者、50K+ GitHub stars，并已在生产环境被信任使用。
- 🧱 提供代理式工作流四大模块：Develop 开发、Test 测试、Deploy 部署、Monitor 监控。
- 📱 开发侧支持 Expo CLI、Skills、MCP、Expo Go 和 Simulators，可在设备或云端验证应用。
- ☁️ 测试侧提供云模拟器和设备基础设施，代理可按需运行应用、验证工作并附截图、录屏和日志，无需 Mac。
- 🚢 部署侧支持 TestFlight 与应用商店原生发布，Update 负责后续 OTA 更新、渠道和灰度发布。
- 👀 Monitor/Observe 提供崩溃信息、性能指标和 Update 采用率，并可在出问题时通过 Update 快速修复。
- 🧩 Expo SDK 已有 10+ 年积累，提供 100+ 生产级 API，一次安装即可使用，并欢迎原生代码。
- 🔄 支持 Expo、React Native、Swift、Jetpack Compose、Kotlin 等基础设施，单代码库分发到 Android、iOS 和 Web。
- ⚙️ Workflows 可自动化构建、测试和发布；Launch 简化上架 App Store；Hosting 支持 Web 分发。
- 📈 社区与使用数据：7M+ 周下载、100K+ 活跃开发者、500K+ 项目、100K+ 日构建，80% React Native 开发者选择 Expo，Discord 70K+ 成员。
- 💬 开发者评价集中在易用、跨平台、低配置设备也能开发、库丰富、性能好、升级方便和 OTA 更新高效。
- 🔐 合规与背书包括 Recommended by Meta、React Foundation Member、SOC 2 Type II、GDPR、CCPA 和 SSO。

---

### [Pele · Mermaid 图表作为可主题化 SVG](https://pele.run/)

**原文标题**: [Pele Â· Mermaid diagrams as themeable SVG](https://pele.run/)

Pele 是一个轻量级开源库，可将 Mermaid 图表渲染为 SVG，并通过 CSS 变量进行主题化；它零依赖，性能显著优于 Mermaid.js，适用于在应用或 Obsidian 中快速渲染图表。

- 🪶 Pele 是开源、轻量的库，可将 Mermaid 语法渲染为 SVG
- 🎨 使用 CSS 变量设置颜色和字体，颜色变更无需重新渲染
- 🚀 零依赖，体积约 230 kB gzip，渲染仅约 0.05–0.3 ms
- 📊 相比 Mermaid.js：体积更小、速度快至 500 倍、依赖为 0
- 🧩 支持 Mermaid 12.1.0 内置的全部图表类型
- 📱 小屏幕下会自适应布局，而不是简单缩放图表
- 💻 可通过 npm/pnpm/yarn/bun 安装，调用 `render()` 并插入返回的 SVG
- 🏔️ 为 Obsidian 开发，名称源自火山与火焰女神 Pele，采用 MIT 许可证
- 🔗 提供示例、API、主题、兼容性、安全性及 Playground 等资源

---

### [Mermaid | 绘图与图表工具](https://mermaid.js.org/)

**原文标题**: [Mermaid | Diagramming and charting tool](https://mermaid.js.org/)

该页面介绍了项目团队的核心成员与贡献者，并邀请社区成员参与共建。

- 👤 Knut Sveidqvist 是项目创建者，同时也是赞助者。
- 💻 Sidharth Vinod 是开发者，同时也是赞助者。
- 🧑‍💻 团队还包括 Ashish Jain、Alois Klink、Neil Cuzon、Tyler Liu、Reda Al Sulais、Per Brolin、Nikolay Rozhkov、Justin Greywolf、Steph Huynh、Matthieu Morel、Marc Faber、Yash Singh、Nacho Orlandoni、Mindaugas Laganeckas 等开发者。
- 🤝 页面设有 Contributors 区域，鼓励加入社区并参与贡献。

---

### [游乐场 · 贝利](https://pele.run/playground)

**原文标题**: [Playground Â· Pele](https://pele.run/playground)

该内容主要展示了 Mermaid Playground 在线编辑器的界面、操作入口及大量图表语法示例，并包含从 Mermaid 文本解析、布局、渲染到 SVG 输出的流程说明与对比预览。

- 🧩 内容核心是 Mermaid Playground/在线编辑器的功能与示例集合。
- 🛠️ 界面提供打开文件、打开示例、设置、重置、清空、自动换行、搜索等操作。
- 📊 列举了大量 Mermaid 支持的图表类型，如流程图、类图、ER 图、甘特图、序列图、状态图、时间线、思维导图、饼图、象限图、需求图、架构图等。
- 🔄 源码示例使用 `flowchart TD` 展示从 Mermaid 文本到解析、布局、渲染、SVG 输出及 CSS 主题化的过程，不支持时会回退。
- 👥 示例中包含 `Pele` 子图，并在输出区提供 Pele 与 Mermaid 的 SVG 对比。
- ⚠️ 页面提示需要启用 JavaScript 才能在 Playground 中渲染图表。

---

### [pour · 免费无障碍检查器与 WCAG 2.2 审计工具](https://pour.dev/)

**原文标题**: [pour · Free Accessibility Checker & WCAG 2.2 Audit Tool](https://pour.dev/)

pour 是一套免费开源的网页无障碍检测工具，旨在让网络对所有人可用。它通过浏览器扩展、命令行、编辑器插件和 VR 应用等多种形式，帮助发现并修复网站的可访问性问题，支持 55+ 种模拟和 WCAG 标准检查。

- 🔍 **全方位检测**：pour 检查网页可访问性，定位问题元素、解释原因并提供修复指导，支持 55+ 种视觉、感官和运动模拟（如隧道视野、白内障、色盲等），并提醒每六人中就有一人体验网络的方式不同。
- 🧩 **多平台工具**：提供浏览器扩展（Chrome/Edge/Firefox）、书签小工具、命令行（pour-cli）、VS Code 扩展、对比度检查器和可集成的 pour-engine。
- 📊 **覆盖与数据**：遵循 WCAG 2.2，覆盖 86 条标准中的 51 条，提供 99 条自动化规则和 35 条人工检查清单；94.6% 的顶级网站存在可证明的无障碍故障（2026 年 10 月）。
- ⚡ **速度与准确**：比 axe-core 快 3 倍（典型页面）至 24 倍（最大页面）；在 Beta Block 测试中检测出全部 38 个预设故障，标记 8 个人工判断项，无误报。
- 🎮 **Meta Quest 应用**：将模拟效果实时叠加到真实房间，支持 Quest 3/3S，数据不离开头显，免费。
- 🛠️ **使用流程**：安装扩展 → 打开并审计 → 阅读发现 → 修复后重新检查；CLI 支持 CI/CD 集成和网站全站报告。
- 🆓 **非营利免费**：所有工具永久免费，无需账户，无订阅，接受捐赠。
- ⚖️ **法规合规**：帮助满足欧洲无障碍法案（2025 年 6 月生效）、美国 ADA Title II（2027/2028 年截止）等要求，符合 WCAG 2.2 AA 标准。
- 👁️ **WCAG 四大原则**：可感知、可操作、可理解、稳健，pour 以此命名并指导检测。

---

### [Claude Code 的 Lighthouse · 将 PageSpeed 审计转化为 CLAUDE.md 修复计划（免费）](https://lighthouse-md.com/)

**原文标题**: [Lighthouse for Claude Code · Turn PageSpeed audits into a CLAUDE.md fix plan (free)](https://lighthouse-md.com/)

该工具将 PageSpeed Insights/Lighthouse 审计结果转化为仓库可直接使用的 CLAUDE.md 修复简报，并一键交给 Claude Code 执行；同时提供 Chrome 扩展和 Shopify 应用，覆盖性能、无障碍、最佳实践与 SEO。

- 🧭 核心流程：粘贴 URL 并选择移动或桌面策略，调用 PageSpeed Insights v5；云端运行约 10–30 秒，低于 0.9 的审计会给出修复建议和问题清单。
- 🧩 输出内容：为每个失败审计提供具体、可执行的修复动作，并按 URL、选择器、HTML 片段和可节省的 ms/KB 排名“主要问题”。
- 🤖 一键交接：可直接打开预载完整计划的 Claude Code，或复制/下载 CLAUDE.md 放入仓库。
- 🧠 CLAUDE.md：Claude Code 读取的纯 Markdown 项目上下文文件，包含限速配置、第三方影响、主线程拆分和当前通过项“不要回退”清单。
- 🧱 Chrome 扩展：无需复制 URL，一键分析当前标签页，也支持已登录的私有 staging 站点。
- 🛍️ Shopify 应用：基于 269 家商店的测量中位移动分为 48；在 Shopify 后台提供每周 Core Web Vitals 跟踪、主题修复计划和 Sidekick 问答，3 次免费审计。
- ⚡ 性能重点：LCP < 2.5s、TBT < 200ms、CLS < 0.1、FCP < 1.8s、Speed Index < 3.4s；常见修复包括预加载 LCP 图、代码分割、延迟第三方脚本、压缩文本、内联关键 CSS。
- 🖼️ 资源优化：减少未使用 JS/CSS、消除渲染阻塞资源、使用 WebP/AVIF 等下一代图片格式、设置高效缓存策略与 HTTPS。
- ♿ 无障碍审计：主地标、链接/按钮可访问名称、aria-hidden 焦点问题、颜色对比度、标题层级、图片 alt 等均有修复建议。
- 🔎 SEO 审计：涵盖 meta description、canonical、title、hreflang、描述性链接文本、可抓取链接、控制台错误、旧版 JavaScript、DevTools 问题等。
- 📊 评分标准：90–100 为 Good，50–89 为 Needs Improvement，0–49 为 Poor；建议 Performance 达到 90+ 且三项 Core Web Vitals 均处于 Good。
- 🧪 Core Web Vitals：LCP 衡量最大可见元素渲染速度，INP 衡量交互响应（<200ms），CLS 衡量意外布局偏移（<0.1）。
- 🛠️ 修复性能问题：从最差审计开始；优先处理高影响项，如延迟非关键 JS、预加载 LCP 图、设置图片宽高、启用文本压缩、移除未使用第三方脚本。
- 🌐 staging/localhost：Web 应用要求公开可访问的 HTTPS URL；私有 staging 可用 Chrome 扩展，localhost 支持可能在未来版本提供。
- 🔐 隐私与速度：URL 会发送给 Google PageSpeed Insights 运行审计，不存储在工具服务器；无需账号，分析在 Google 云端完成，通常 10–30 秒。
- ✅ 准确性与可操作性：“Top offenders”直接来自 Lighthouse 结果，仅展示每项前几项，便于 Claude Code 用模式在代码库中查找类似问题。

---

### [3dsvg — 将 SVG 转换为 3D 的最简单方法](https://3dsvg.design/)

**原文标题**: [3dsvg — The easiest way to turn SVGs into 3D](https://3dsvg.design/)

该内容展示了一个字体选择与 3D 文字/图形定制工具界面，支持字体预览、SVG 上传、对象参数调整、材质与动画设置，并提供反馈选项。

- 🔤 提供多种字体：DM Sans、Bebas Neue、Playfair Display、Righteous、Black Ops One、Permanent Marker、Rubik Mono One、Pacifico、Oswald、Archivo Black
- ⏳ 界面显示“Loading font...”字体加载状态，并支持加载星形示例
- 📤 支持上传 SVG 文件并选择文件
- 🎛️ 设置面板包含对象、颜色 #4f46e5、深度 1.0、平滑度 60%、缩放 8.0 和重置位置
- 🧱 可调整背景、材质、纹理、动画、交互和灯光等效果
- 💬 反馈区域提供“What's your feedback?”提示及 Image、Video、Auto 选项

---

### [Furifont：字体内置振假名](https://furifont.antfu.me/)

**原文标题**: [Furifont: furigana built into the font](https://furifont.antfu.me/)

未提供可总结的文章内容，因此暂时无法生成要点摘要。
- 📄 请在“Use the following content:”后补充文章正文。
- ✍️ 收到内容后，我会用中文输出“概述 + Emoji 要点”格式的摘要。
- ✅ 要点将使用“-”符号，并提炼关键信息与核心结论。

---

### [](https://github.com/antfu/furifont)

**原文标题**: [GitHub - antfu/furifont: A Japanese font that shows furigana by itself. · GitHub](https://github.com/antfu/furifont)

Furifont 是一款自带振假名（furigana）的日文字体，通过字体内部的 OpenType 连字技术直接显示读音，无需 `<ruby>` 标记、JavaScript 或插件，只要支持自定义字体即可使用。

- 📝 **项目简介**：一款自带振假名的日文字体，文本保持纯文本格式，无需额外标记或脚本。
- ⚙️ **工作原理**：基于思源黑体/宋体编译，内置词典和连字规则，将单词（如“今日”）映射为一个带振假名的字形；长词优先，无明确读音的汉字保持原样。
- ⚠️ **注意事项**：由于字体只能看到连续的一段汉字而非整句，振假名可能不准确。
- ⬇️ **下载选项**：每个版本提供 Sans/Serif、平假名/罗马字、常规体（OpenType 和 WOFF2）以及可变字体（ExtraLight 到 Heavy，TrueType 和 WOFF2），需设置 `line-height` ≥1.6 避免裁切。
- 🌐 **网页使用**：官网提供书签小工具和用户脚本，可将任意页面设为 Furifont 字体，并可选送假名读音。
- 🛠️ **自定义构建**：支持更换基础字体、词表、振假名字母或大小，需 Node 22.18+，通过 `npx furifont dev` 实时预览，`npx furifont build` 构建。
- 📦 **包结构**：`furifont`（CLI/服务端）、`@furifont/core`（字形与 OpenType 规则）、`@furifont/compiler`（绘制字形）、`@furifont/dictionary`（编译词典）、`@furifont/helper-web`（网页引擎）、`packages/app`（网站与 Customize）。
- 📜 **致谢与许可**：灵感来自 Mengshen-pinyin-font 和 Fira Code；代码 MIT，字体 SIL OFL 1.1，词典数据 CC BY-SA 4.0。

---

