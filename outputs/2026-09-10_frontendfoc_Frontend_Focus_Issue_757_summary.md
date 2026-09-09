### [获取失败](https://blog.master.dev/new-things-you-should-know-about-html-here-in-mid-2026/)

**原文标题**: [Failed to retrieve](https://blog.master.dev/new-things-you-should-know-about-html-here-in-mid-2026/)

无法总结：获取内容失败，状态码 429。

---

### [](https://lea.verou.me/blog/2026/dark-mode-toggles-2/)

**原文标题**: [
		The best dark mode toggle is probably none • Lea Verou](https://lea.verou.me/blog/2026/dark-mode-toggles-2/)

作者从「两状态暗色模式切换」的推荐出发，经过大量讨论后，转为更激进的结论：大多数网站根本不该放一个常驻的暗色模式切换控件；默认跟随系统，并把偏好设置放进设置面板即可。

- 💡 核心立场演变：作者原主张「两状态切换」优于「三状态」，后来进一步认为绝大多数网站根本不需要常驻切换按钮。
- 🎯 两状态切换的逻辑：如果必须有控件，只要能在「跟随系统」与「当前系统的相反模式」间切换，就能覆盖用户「换一下主题」的真实意图，三态反而多余。
- 🗣️ Bramus 的主要反对：他担心 OS 自动切换暗色时段时，两状态控件会让用户之前显式选择的模式被覆盖，因而认为三状态更清晰。
- 📅 对反对意见的回应：所谓「夜间自动切换」其实不是问题——用户只需一次点击即可永久固定模式；无需每个会话重复操作。
- 📊 批评对方方法论：Bramus 用「开发者构建哪种控件」来推断「用户易用性」，混淆了惯例与实现便利，不能替代用户研究。
- 🧠 认知负担不能被美化：「本地反馈」只是按钮变化而页面不变，恰恰是失败；三状态还会强迫用户做「系统其实是什么」的无谓心智转换。
- ⚠️ 失败场景罕见且易恢复：要触发 Bramus 担心的情形需多个条件叠加；即便发生，一键即可修正，不值得为它牺牲常规体验。
- 🧩 替代设计各有亮点但多属伪需求：Vale 的 3-in-2、Toni 的可撤销切换等富有创意，但大多在解决一个用户很少真正在意的问题。
- 👀 决定性启发：作者意识到常驻暗色切换几乎只出现在开发者网站上；主流消费级网站都将深色模式放在设置面板，因此它不值得占用宝贵的首屏位置。
- 🧪 正确验证方式应该靠数据：与其靠定性测试，不如收集真实用户的大规模交互数据，观察点击频率、实际行为与操作耗时。
- 🔍 最终方法论提醒：动手解决问题前，先问「这是否真的值得解决的问题」，避免掉进伪问题优化陷阱。

---

### [](https://lea.verou.me/blog/2026/dark-mode-toggles/)

**原文标题**: [
		Dark mode toggles: two states are enough • Lea Verou](https://lea.verou.me/blog/2026/dark-mode-toggles/)

本文论述了三态深色模式切换（亮色/暗色/系统）为何是常见的 UX 反模式，并解释了更优的双态切换做法：双态控件其实能完整表达三种数据状态，关键在于正确管理用户覆盖值，并只在用户主动操作时评估是否移除覆盖。文章也指出三态控件仅在特定场景下才合理，核心原则是：不要为用户当前不存在的问题提供选项。

- 🌗 三态切换器常见于许多网站，但它属于“实现驱动 UI”：把底层三种数据状态直接暴露给了用户，而不是围绕用户真实目标设计。
- 🎯 用户浏览网站时的主题需求只有两种：页面看起来没问题（继续做正事），或页面太亮/太暗需要临时调整；不存在“主动维护系统策略”这种天然目标。
- 🔁 一个好的双态切换可以表达全部三种状态：默认显示当前解析结果（如太阳/月亮）；首次点击写入相反值的覆盖；再次点击则移除覆盖、回到跟随系统。
- ⚠️ 常见的双态实现错误是：当系统偏好后来改变时，过度主动地清除用户存储的覆盖值；这种清理只应在用户交互时评估，不能因系统事件而偷偷发生。
- 🧠 三态切换会带来认知负担和界面成本，常见形式包括三个图标并排、循环切换或下拉菜单；这些都会增加感知摩擦，且选择与当前显示相同的选项时没有可见反馈。
- 🛠️ 双态切换被批评，往往是因为拿糟糕的双态实现去对比良好的三态实现；正确实现的双态控件能避免“不可逆”问题，并支持用户控制与自由度。
- 📱 三态控件真正合理的场景包括：位于独立设置面板中的颜色方案选项，以及当同一颜色模式在不同系统设置下被刻意实现得不同（需要让用户明确区分）时。
- 📌 核心通用原则是：用户不会为解决当前不存在的问题而寻找选项；不要提前呈现未来才可能相关的状态，应在其真正变得重要时再浮现出来。
- 🚫 作者最后补充认为，最好的深色模式切换器可能根本没有；如果决定直接跟随系统偏好而不提供切换，也是完全合理的选项。

---

### [](https://www.bram.us/2026/08/18/the-case-for-tri-state-dark-mode-toggles/)

**原文标题**: [The Case for Tri-State Dark Mode Toggles – Bram.us](https://www.bram.us/2026/08/18/the-case-for-tri-state-dark-mode-toggles/)

作者在文中主张，网站深色模式切换不应只做两态（浅色/深色），而应采用三态（系统/浅色/深色）设计；他从用户预期、可预测性和清晰性出发，回应了Lea Verou的反驳，并分享了调查数据、可行的两态实现方案以及一个保留三态的优雅UI设计。

- 🌓 核心论点：深色模式切换应优先采用三态控制（System/Light/Dark），而非简单的两态开关。
- 🤨 起因：作者看到Modern Web Guidance指南建议两态控制，但早在2020年他就认为这类控件应提供“跟随系统”的选项。
- 📝 作者并不认同Lea说“两态即可”的理由：手动切换不一定是临时调整；即便页面整体没变，被选中的选项也有局部视觉反馈。
- 📊 作者在社交媒体上的调查显示：43人支持三态、7人支持两态，另有4人表示不提供切换控件、只跟随系统偏好。
- ⏰ 两态方案的硬伤：当OS按时间段自动切换浅色/深色时，用户先前明确选择的“浅色”，会在夜间被悄悄映射成“深色”，造成困惑。
- 🔧 若坚持两态，较好的做法：一是在“跟随系统”状态上明确标注Auto；二是把显式的light/dark值写入存储，但这样仍需“重置”入口，不如直接用三态。
- 🎛️ 作者欣赏Vale的UI方案：只显示Light/Dark两个按钮，两者都未选中即代表System；点击已选中的值会取消选择，回到跟随系统。
- 🧭 核心原则：清晰性优先于简洁性；用户操作后期待状态被持久记住，不应因时间变化而意外改变。
- 💬 评论区仍有争议：部分人认为这是极端场景，多一次点击即可解决；作者反驳并非所有网站都有设置页，而且用户不应被要求额外点击。

---

### [使用OpenAI Codex构建雄心勃勃的界面 | Master.dev](https://master.dev/courses/codex/?utm_source=email&utm_medium=frontendfocus&utm_content=codexcooper)

**原文标题**: [Build Ambitious Interfaces with OpenAI Codex | Master.dev](https://master.dev/courses/codex/?utm_source=email&utm_medium=frontendfocus&utm_content=codexcooper)

本課程為免費的 OpenAI Codex 前端開發實戰課程，由 OpenAI 開發者體驗工程師 Katia Gil Guzman 授課，教你運用 Agentic Coding 工作流程，從設定 Codex、視覺化建構與驗證 UI，到部署至 ChatGPT Sites，全面提升前端開發效率與品質。

- 🎓 課程共 22 堂、約 3.4 小時，評分 4.7，完成後可獲得結業證書，並能分享至 LinkedIn。
- 👩‍💻 講師 Katia Gil Guzman 具備微軟 Azure AI、Stripe 平台架構等豐富經驗，目前專注於 OpenAI 代理式開發工具。
- 📋 先備條件只需具備基本提示詞知識與軟體開發經驗，適合想導入 AI 輔助前端開發的工程師。
- ⚙️ 教學重點涵蓋：為 Codex 選擇適合的模型與推理強度，並透過 Agents.md 建立專案上下文、外掛與瀏覽器工具。
- 🎯 透過目標設定、明確的 UI 測試與迭代回饋迴路，掌握「建構、檢視、引導、驗證」的前端開發流程。
- 🔁 學習將團隊前端工作流程轉換為可重複使用的 Skills、Plugins 與自動化，穩定產出元件與功能。
- 🌍 可直接從 Codex 將專案部署到 ChatGPT Sites，快速分享成品。
- 🖼️ 課程內容包含 App Shots 與註解等視覺回饋技巧，可減少反覆溝通、加快迭代。
- ✨ 探索「Living Frontends」創新應用，將靜態畫面提升為動態視覺化，適合呈現複雜主題與文件。
- 🗂️ 課程模組涵蓋簡介、Codex 概觀、Sites 建置、3D 動畫互動、既有程式碼整合及 Living Frontends，總長約 3 小時 24 分。
- 🎮 學習平台具備進度追蹤、筆記、測驗與單字卡功能，可彈性安排學習節奏。
- 🆓 免費註冊即可取得永久課程存取權，無需信用卡，另有多門免費進階課程可選。

---

### [](https://vale.rocks/posts/html-relics)

**原文标题**: [Antiquated HTML Snippets and Artefacts | Vale.Rocks](https://vale.rocks/posts/html-relics)

这篇博文回顾了许多因为浏览器竞争、第三方插件、移动设备演变等“环境性变化”而过时或被遗忘的 HTML 片段，并逐一解释它们的来源、用途和消亡原因。这类代码并非规范本身废弃，而是被时代与生态淘汰的“数字遗物”。

- ⚔️ 浏览器战争遗留产物：`X-UA-Compatible` 用于指定 IE 的渲染模式，Google Chrome Frame、`requiresActiveX` 也属于此类；IE 与 Netscape 的条件注释则用于精准区分不同浏览器和版本。
- 🗺️ 地理位置与内容标签：ICBM 坐标 meta 标记曾经标注网站地理位置；PICS 用于内容分级却因虚假标注而失败；`MSSmartTagsPreventParsing` 则是为阻止 IE 6 的 Smart Tags 自动插入超链接而出现。
- 🎬 IE 专属显示控制：`Page-Enter`/`Page-Exit` 可加页面切换动画；`Window-target=_top` 用于防止被 iframe 嵌入；`imagetoolbar=no` 禁用图片工具栏；`cleartype=on` 改善低分辨率屏幕字形渲染。
- 🚫 抵御第三方干扰：开发者用 meta 标签关闭 Skype Toolbar 自动识别电话、阻止百度移动“转码”重排页面，也用来禁用 IE 图片工具栏等入侵式功能。
- 🔎 SEO 与搜索引擎旧事：AJAX 时代用 `fragment` meta 让 Google 抓取动态页面；`robots noydir/noodp` 避免搜索引擎采用目录描述；`revisit-after` 只是一个从未被主流搜索引擎采用的 SEO 迷思。
- 📌 固定网站与 PWA 前身：IE 的 `msapplication-*`、Chrome 的 `application-url`、Safari 的 `mask-icon`、iOS 的 `apple-*` 等标签，都曾用来定制固定到系统界面或主屏幕的应用外观，最终被现代 PWA 取代。
- 📱 移动端与特殊浏览器适配：UC/QQ 浏览器有 `screen-orientation`、`x5-orientation`、`full-screen` 等标签；早年的 `HandheldFriendly`/`MobileOptimized` 针对 PDA 和 Windows Mobile；`msapplication-tap-highlight` 则关闭 IE 11 的点击高亮。
- ⚡ 预取与加速方案：Chrome 曾支持 `rel=prerender` 预渲染页面，后被 Speculation Rules API 取代；`rel=amphtml` 关联 AMP 版本，随着 AMP 失势也不再必要。
- 🧩 旧日建站与博客生态：FrontPage 注入的 WebBot 注释、用于博客客户端发现的 `rel=EditURI` RSD、以及 `rel=pingback` 引用通知，都因平台更迭或滥用漏洞而退出主流。
- 📣 社交分享元数据：Facebook Share Partners 时代使用 `rel=image_src` 等标签，后来是 Twitter 卡片 meta；如今 Twitter 文档下线且平台日落，作者建议删除这些标签并全面改用 Open Graph。
- 🧠 怀旧反思：这些过时的 HTML 片段承载着浏览器战争和 Web 平台演进的记忆；文章并不详尽，更多古怪案例仍可在 WhatWG Wiki 中找到。

---

### [获取失败](https://www.w3.org/news/2026/w3c-opens-2026-community-wide-survey/)

**原文标题**: [Failed to retrieve](https://www.w3.org/news/2026/w3c-opens-2026-community-wide-survey/)

无法总结：获取内容失败，状态码 403。

---

### [Tailwind Labs 加入 Shopify - Tailwind CSS](https://tailwindcss.com/blog/tailwind-is-joining-shopify)

**原文标题**: [Tailwind Labs is joining Shopify - Tailwind CSS](https://tailwindcss.com/blog/tailwind-is-joining-shopify)

Tailwind CSS 创始人宣布该项目正式加入 Shopify，以保障其长期稳定维护与发展。框架仍将保持开源并沿用 MIT 许可，但围绕 Tailwind 的商业业务将不再扩张。

- 🎨 Tailwind CSS 已走过九年，目前每周安装量超过 1.1 亿次，并被 ChatGPT、X、Cloudflare、Reddit 等大型公司采用。
- 🛍️ 加入 Shopify 后，开发团队可在真实的复杂业务场景（如店铺、管理后台、结账与 Shop App）中持续改进框架。
- 🤝 Shopify 是最早大规模采用 Tailwind CSS 的公司之一，并将其视为核心基础设施。
- 🚀 创始人认同 Shopify 帮助更多人创业的使命，也看好其探索 agentic commerce 等前沿方向。
- 🔓 Tailwind CSS 及其他开源项目保持 MIT 许可，原团队继续领导维护，Shopify 提供支持。
- 🚧 商业层面将不再扩展新客户，现有 Tailwind Plus 与 ui.sh 用户仍可继续使用。
- ❤️ 感谢社区九年来的支持，相信 Shopify 是让项目继续发展的最佳归宿。

---

### [获取失败](https://blogs.windows.com/msedgedev/2026/09/03/calling-for-interop-2027-proposals/)

**原文标题**: [Failed to retrieve](https://blogs.windows.com/msedgedev/2026/09/03/calling-for-interop-2027-proposals/)

无法总结：获取内容失败，状态码 403。

---

### [](https://techcrunch.com/2026/09/08/chrome-is-now-shipping-updates-every-2-weeks-as-ai-changes-the-security-landscape/)

**原文标题**: [Chrome is now shipping updates every 2 weeks as AI changes the security landscape | TechCrunch](https://techcrunch.com/2026/09/08/chrome-is-now-shipping-updates-every-2-weeks-as-ai-changes-the-security-landscape/)

Chrome 宣布将发布周期从四周缩短至两周，以应对 AI 时代的安全威胁与功能迭代需求，并带动行业跟进。

- 🌐 Chrome 于本周二推出 153 版，正式从四周发布周期切换到两周，覆盖桌面、iOS 和 Android。
- 🤖 更快的发布周期与安全策略调整相关，AI 工具和社区报告推高补丁量，缩短周期更便于管理修复。
- 🛡️ 缩短漏洞公开到修复推送的“N-day”空窗期，有助于更快遏制 AI 带来的新型威胁。
- 🚀 两周更新还能加速功能发布，帮助 Chrome 应对 AI 时代层出不穷的新浏览器竞争者。
- ✨ Google 正在试验更多 Chrome AI 功能，并需要快速迭代，这也依赖更短的更新周期。
- 🌍 作为全球最常用的浏览器，Chrome 的调整促使 Mozilla、Microsoft、Brave 等也开始采用两周发布节奏。
- 📜 这不是 Chrome 首次缩短周期，2021 年已从六周改为四周，延续了“早发布、勤发布”的原则。

---

### [](https://groups.google.com/a/mozilla.org/g/dev-platform/c/3YMV4MS34KA/m/8CblVBJCAAAJ)

**原文标题**: [Intent to ship: JPEG XL](https://groups.google.com/a/mozilla.org/g/dev-platform/c/3YMV4MS34KA/m/8CblVBJCAAAJ)

概述：Mozilla 计划在 Firefox 中默认启用 JPEG XL 解码（基于 Rust 的 jxl-rs），原定于 Firefox 157，后推迟到 158。该讨论涉及性能、功能完整性、兼容性及测试覆盖；其中社区对无损 JPEG XL 解码速度远慢于 WebP 表示担忧。

- 🚀 宣布默认启用：Firefox 计划在所有平台默认开启 JPEG XL 解码，采用标准 ISO/IEC 18181，由 Rust 编写；原定 157，后调整为 158。
- ⚙️ 当前状态：image.jxl.enabled 已在 Nightly 默认开启，Firefox 152+ 通过 Firefox Labs 开关测试。
- 🌐 浏览器动态：Safari 17.0（2023）已支持；Chrome 有同样的 Rust 库实现，但尚无发布意向。
- ⚡ 性能进展：jxl-rs 0.6.0 新增多线程解码；基准测试略优于 Safari 的 C++ libjxl，但与自家其他图像解码器相比，大图接近、小图差距较大。
- ✨ 功能对齐：支持动画和渐进显示，与 Blink 实现相当；HDR 图像以 SDR 显示，但 JXL 色调映射优于其他格式；Safari 缺少渐进渲染和动画。
- 🧪 测试完备：wpt 覆盖各种颜色模式、编码工具等；另有约 30 个 gtest、相关 mochitests/reftests 及性能基准；fuzzing 团队也将在切换前重新测试。
- 🖼️ 动画确认：开发人员确认 Animated JXL 已受支持。
- ⚠️ 性能质疑：有成员测量显示无损 JPEG XL 解码比无损 WebP 慢约 15–30 倍，文件大小仅缩小约 10%；建议只发布有损 JPEG XL，避免 CDN 追逐压缩率而损害终端用户体验和电池续航。
- 📅 时间调整：剩余工作超过预期，默认启用从 Firefox 157 推迟到 158；Nightly 和 Labs 开关及偏好设置保持不变。
- 💬 兼容性观点：有人支持保留无损 JPEG XL，以兼容 Safari，并预期其用途很小众；但也指出开发者可能误以为有损 JPEG XL 在网页质量上优于 AVIF，需要宣传和引导。

---

### [](https://lapcatsoftware.com/articles/2026/9/1.html)

**原文标题**: [Chrome again exempts Google from user site data settings](https://lapcatsoftware.com/articles/2026/9/1.html)

overview summary：Jeff Johnson發現Chrome再次出現類似六年前的漏洞，即Google自家網站被豁免於用戶的「關閉視窗時刪除網站資料」設定，導致google.com的Cookies與儲存資料在關閉Chrome後依然留存。作者重現於Chrome 152版，質疑這是Google的品質控管疏失，並呼籲政府拆分其搜尋壟斷。

- 🔁 六年前曾通報的Chrome漏洞再度出現：Google網站被排除在用戶的網站資料刪除設定之外。
- 🖥️ 於兩台Mac、Chrome 152.0.7977.83版重現；測試時改用DuckDuckGo搜尋引擎，確認非搜尋設定所致。
- 🚫 使用者未登入Chrome，且全域設定為「關閉所有視窗時刪除網站資料」，但關閉唯一視窗後，google.com資料仍保存在裝置上。
- 🍪 殘留資料包含Cookies、Local Storage與Session Storage；只有www.google.com受到此豁免影響。
- ⚖️ 作者傾向以Hanlon剃刀解釋為「無能而非惡意」，但仍批評Google的品管與測試不足，不該讓此類問題再次發生。
- 💰 諷刺Google賺取巨額利潤，卻連基本QA都沒做好；建議加入單元測試並減慢開發速度。
- 🏛️ 作者認為政府應加速行動，拆分Google搜尋壟斷，並抱怨未登入時搜尋結果會導向opaque的`google.com/goto`連結，而非真實網址。

---

### [jQuery二十年：一个小库如何重塑Web开发 - InfoQ](https://www.infoq.com/news/2026/09/jquery-20-years/)

**原文标题**: [Twenty Years of jQuery: How a Little Library Rewired Web Development - InfoQ](https://www.infoq.com/news/2026/09/jquery-20-years/)

jQuery 迎来二十周年，从 2006 年首次发布至今深刻改变了 Web 开发。它让 JavaScript 变得简单易用、跨浏览器一致，并催生了庞大的社区生态，但后来也面临现代框架和原生 API 的冲击。尽管如此，至今仍有大量网站依赖它，其影响延续至今。

- 🎉 2006年8月26日，jQuery 1.0 正式发布，由 John Resig 创建，最初在 BarCampNYC 亮相。
- ✨ “写 JavaScript 应该有趣”的理念，将 document.getElementById 等繁琐操作简化为 `$()`，极大降低了前端开发门槛。
- 🌍 jQuery 普及了 CSS 选择器、链式操作、动画和 Ajax，在 IE6 等浏览器不一致时代做到跨浏览器统一。
- 👥 强大的社区与插件生态统一了 JS 开发者，影响后续众多框架，成为“write less, do more”的先驱。
- 🔄 随着 React、Angular 等声明式框架兴起，以及 querySelectorAll、fetch、classList 等原生 API 成熟，jQuery 逐渐被视为遗留风格。
- 🛡️ 旧版 jQuery 的安全漏洞仍是现实问题，因为它在 WordPress、Drupal、Bootstrap 等中深度嵌入，W3Techs 显示约 66% 网站仍在使用。
- ❤️ 仍有如 Docker 工程师等发声维护 jQuery，认为它“帮助塑造了当今的 Web”，并由 OpenJS 基金会继续维护。

---

### [2026年自定义滚动条组件 – Master.dev 博客](https://blog.master.dev/custom-scrollbar-component-in-2026/)

**原文标题**: [Custom Scrollbar Component In 2026 – Master.dev Blog](https://blog.master.dev/custom-scrollbar-component-in-2026/)

overview summary  
本文介绍在2026年如何利用 CSS scroll-driven animations 与 Anchor Positioning 实现自定义滚动条组件，仅在拖拽交互时使用少量 JavaScript，大幅降低效能开销与复杂度。  

- 🎯 传统自定义滚动条需用 ResizeObserver、scroll 事件与手动 DOM 更新，易造成 Reflow 与效能问题。  
- 📌 使用 CSS Anchor Positioning（anchor-name / anchor()）将条固定在滚动容器内，且不随内容滚走。  
- 🧩 以 scroll-timeline 与 timeline-scope 建立滚动进度，并通过 @property 与 keyframes 驱动 --start、--end、--opacity 等 CSS 变量。  
- 📏 搭配 Container Queries 与 animation-range，让滚动条高度准确反映内容比例，并避免过度缩窄（min-block-size + min()）。  
- 🚀 当内容可滚动时，利用同名关键帧自动让滚动条显示，并恢复 pointer-events；未溢出时则隐藏。  
- 🖱️ 拖拽部分才需 JavaScript：pointerdown / pointermove 呼叫 scrollTo，并处理 RTL 方向及移除事件监听。  
- ♿ 由于未改变原生滚动机制，无障碍方面基本安全，但两端跳转与键盘操作仍依赖原生行为。  
- 🛠️ 实际价值：跨浏览器统一外观、避免 Windows 上无 overlay 滚动条盖住内容、减少多可滚动区域视觉噪音、支援高客制化视觉设计。  
- ⚠️ 兼容性提醒：应使用 @supports 包裹；非 Nightly Firefox 可能出现滚动异常，建议留意浏览器支援状况。  
- ✨ 应用範例包含 Facebook、Discord、Spotify 与 VS Code for the Web / CodePen 等大型专案。

---

### [](https://kciter.so/posts/the-expensive-main-thread/en/)

**原文标题**: [The Browser's Main Thread Is Expensive | kciter.so](https://kciter.so/posts/the-expensive-main-thread/en/)

浏览器主线程是性能瓶颈的核心：它同时负责 JavaScript 执行与画面渲染，一旦被长时间占用，输入、动画和滚动都会卡顿；优化重点是合理分配主线程时间，或将工作移出主线程。

- 🧵 主线程同时运行 JavaScript 和渲染管线（样式计算、布局、绘制），单任务执行期间无法响应输入或绘制帧，超过 50ms 即被视为长任务。
- ⏱️ 60Hz 屏幕每帧预算约 16.6ms，扣除浏览器开销后实际约 10ms；性能指标 INP 和 TBT 本质上都在衡量主线程被阻塞的时间。
- ✂️ 拆分（Splitting）：把大任务切成小块，用 setTimeout、requestAnimationFrame 或 scheduler.yield() 主动让出主线程，在间隙处理输入与渲染；注意不要切得过细，且无法拆分同步原子操作（如 JSON.parse）。
- 📦 批处理（Batching）：通过防抖、节流或 requestAnimationFrame 合帧，把高频事件合并为一次执行；也适用于 DOM 写入、状态更新与网络上报，减少渲染管线的重复固定开销。
- 🚦 优先级（Prioritizing）：用队列配合 MessageChannel 实现任务调度，紧急任务插队到前面；React 的 startTransition/useDeferredValue 以及“闲时处理、急时优先”模式都属此类。
- ⏳ 延迟（Deferring）：不立刻做不必要的工作，如代码分割、离线屏内容用 IntersectionObserver 或 content-visibility 延迟渲染、滚动出视口后暂停持续动画。
- 🎨 交给合成器：用 transform/opacity 做动画可绕过主线程，由合成器线程处理；列表动画可用 FLIP 技术，只触发一次布局，其余交给合成器。
- ⚠️ 避免布局抖动：读取与写入布局属性要分组进行，否则会在循环中反复强制重排，拖慢主线程。
- 👷 交给 Worker：纯计算（图像处理、大数据解析）可放入 Web Worker；用 Transferable 对象转移 ArrayBuffer 所有权以避免拷贝开销；Worker 无法访问 DOM，只适合重计算场景。
- 🗑️ 消除不必要的工作：面对数据洪流可丢弃旧日志、合并排名类更新为最终值、用 memoization 跳过重复计算；不做工作才是最大的性能优化。

---

### [](https://www.tigerdata.com/go/trial?utm_source=content-syndication&utm_medium=referral&utm_campaign=frontend-focus-newsletter)

**原文标题**: [Postgres for time-series workloads at any scale. | Tiger Data](https://www.tigerdata.com/go/trial?utm_source=content-syndication&utm_medium=referral&utm_campaign=frontend-focus-newsletter)

Tiger Data 是面向时序工作负载的 PostgreSQL 云服务，能在真实业务中支撑超大规模数据，提供高度弹性、企业级安全与可观测性，并附带免费试用信用额度，帮助 IoT 等企业快速上云与管理数据。

- 📈 单服务实测可处理每天 3 万亿指标、3 PB 数据，总计容纳 1 千万亿数据点。
- 💵 新账户可获 $1000 信用额度，30 天有效，无需信用卡、仅限新用户。
- 🏭 受到数千家 IoT 企业的信任与采用。
- ⚖️ 读写分离，通过最多 10 节点的副本集与 SSD/S3 分层存储实现轻松扩展。
- 💸 计算与存储分离，可独立扩缩容，避免为闲置容量付费，兼顾成本与性能。
- 🛡️ 提供多可用区集群、自动故障转移、时间点恢复和跨区域备份，实现高可用。
- 🔒 企业级合规：支持 SOC 2、HIPAA、GDPR，并具备全程加密、SSO、RBAC 和审计日志。
- 📊 深度可观测：支持查询下钻与仪表盘，可向 CloudWatch、Datadog、Prometheus 发送指标。
- ⚡ 快速启动：分钟级完成数据库部署，并可通过 SQL、CLI、Terraform、Cursor 或 Claude Code 管理。
- 🔌 可融入现有技术栈，支持主流云厂商及完整 Postgres 生态。
- 🏅 企业默认保障：具备合同化 SLA、区域数据隔离，以及 24/7 全球 Postgres 专家支持。

---

### [](https://utilitybend.com/blog/container-style-queries-and-advanced-attr-rethinking-how-to-wire-up-my-components-in-css)

**原文标题**: [Container style queries and advanced attr(): rethinking how to wire up my components in CSS | utilitybend](https://utilitybend.com/blog/container-style-queries-and-advanced-attr-rethinking-how-to-wire-up-my-components-in-css)

overview summary
本文介绍如何结合 CSS 容器样式查询与新一代 attr()，让组件仅通过 HTML 属性自动调整样式与布局，减少修饰类和 JS 参与。

- 🔍 高级 attr() 现在可用于任意 CSS 属性，并支持类型/单位解析，例如数值、长度、自定义标识符及 fallback 值。
- 📏 容器样式查询可查询祖先容器上的自定义属性，无需 container-type，即可让子组件按环境自适应。
- 🧱 网格示例：通过 data-repeat 与 data-gap 属性直接控制列数和间距；data-minSize 则自动决定换行宽度。
- 💧 间距使用 cqi 单位随容器缩放，使 HTML 无需携带单位，同时组件保留自己的单位系统。
- 🎚️ 密度控制采用单一 --density-scale 乘数，统一缩放 padding、圆角、头像、字号等，避免重复编写尺寸变体。
- 🖱️ 拖动示例：容器声明 data-density，attr(custom-ident) 将其转换为标识符，卡片移入新容器后由样式查询自动重设外观。
- 🎨 综合示例：一个容器用 data-featured、data-accent 等属性驱动“推荐卡片”和强调色，纯 CSS 完成状态分发。
- 🌐 支持情况：容器样式查询已成为 Baseline；高级 attr() 在 Chrome/Edge 133、Firefox 155 中可用，Safari 仍处预览。
- 🔄 若需兼容旧浏览器，可通过 @supports 提供降级写法，但作者更倾向未来直接使用这些新特性。
- 💭 作者认为这套思路会重塑 CSS 架构，让 HTML 声明需求、CSS 自动完成适配，值得在实践中转换思维方式。

---

### [](https://portswigger.net/research/css-the-bomb-inside-your-inbox)

**原文标题**: [CSS:the bomb inside your inbox | PortSwigger Research](https://portswigger.net/research/css-the-bomb-inside-your-inbox)

这篇文章介绍了安全研究员 Gareth Heyes 对多个主流 Webmail 客户端（Outlook、Gmail、Fastmail、ProtonMail、Yahoo/AOL Mail 等）的研究，展示了如何利用 CSS 绕过 HTML/CSS 清洗器，突破信任边界，实现 UI 欺骗、令牌窃取、账户接管、密码窃取，以及通过间接提示注入控制 AI 浏览器。

- 📧 滥用 HTML `<label>` 的 `for` 属性可触发网页中的隐藏 UI 操作；作者在 Outlook 中发现可借此打开工具栏并固定消息的未修复漏洞。
- 🤖 利用 CSS `:before/:after`、透明度和隐藏文本，可对 AI 浏览器（如 OpenAI Atlas）实施间接提示注入，让 AI 在用户要求翻译时自动打开大量标签页并外泄数据。
- 📋 在支持 `contenteditable` 的邮箱中粘贴恶意 CSS 可触发竞态条件；Firefox 允许内联样式及背景请求，借此可通过嵌套属性选择器暴力破解 Medium 的 12 字符登录令牌，实现账户接管。
- 🚫 即使 CSP 禁止外部资源，也能通过生成数字组合链接、`@font-face` 修改字形高度和 CSS 动画构建“字体高度预言机”，进而窃取邮件中的数字令牌。
- 🧹 CSS 语法非常宽松，存在大量可用于绕过净化器的怪癖，如注释解析差异、属性名中的特殊字符、十六进制转义及多种可发起外部请求的 CSS 属性。
- 🖼️ 通过转义字符或 `image-set(var(--x,'//...'))` 等方式可绕过 Fastmail、ProtonMail、Gmail 等邮箱的图片代理，实现打开追踪、IP 获取甚至结合 AI 注入窃取 Slack 令牌。
- 🔀 浏览器 CSSOM 在读取 CSS 规则时可能发生变异，例如转义序列 `\7d\2a` 被解码为 `}*`，从而使 Fastmail 的净化器把看似安全的内容变为可控制页面的恶意 CSS。
- 🧩 Outlook 会对自定义 data 属性进行白名单处理，但其 JS 库会向 DOM 追加带白名单外 CSS 值的节点——形成 CSS gadget，可借此 deface 页面并配合其他漏洞实现高危害攻击。
- ⚡ CSS hotwiring 利用 `:before/:after` 继承点击事件，可让受害者在页面上任意位置点击时触发指定 UI 操作，并可通过 z-index 串联多步骤操作。
- ⌨️ 现有“CSS 键盘记录器”因缺少属性值与 DOM 属性的绑定而实际无效；作者利用 `<select>`、`:checked`、CSS gadget 及 Outlook 净化器绕过，构造出 Firefox 上可用的实时密码窃取登录界面。
- 🛡️ 防御建议包括：使用沙箱 iframe 严格隔离邮件内容、限制自定义属性和 CSSOM 变异字符、阻止邮件中的图片请求、屏蔽 `<select>` 及 `:has/:checked/:focus/:not` 等危险选择器、始终使用图片代理并检查 HTML/CSS gadget。
- 🔮 未来攻击方向包括基于 Chrome 新元素 `selectedcontent` 的纯 HTML 键盘记录器，以及利用 interest invokers、popover 和 `interestfor` 实现 Chrome 上的实时键盘记录攻击。

---

### [](https://dropbox.tech/security/how-our-inhouse-auditor-tests-cookie-behavior-across-hundreds-of-web-surfaces)

**原文标题**: [Testing cookie behavior across hundreds of web surfaces with our in-house auditor - Dropbox](https://dropbox.tech/security/how-our-inhouse-auditor-tests-cookie-behavior-across-hundreds-of-web-surfaces)

Dropbox 工程团队为应对 200 多个网站页面在 Cookie 横幅合规上的挑战，构建了内部“Cookie 审计器”。它借助 Playwright 模拟各类访客（美国、欧盟、GPC 信号），自动验证 Cookie 加载是否符合用户隐私偏好；同时配套 URL 检测器来发现需要测试的网页，把隐私合规转化为可持续验证的工程实践，并输出每周报告供团队跟进问题。

- 🔐 **合规复杂性**：随着网页上线、改版、重定向及实验等动态变化，Cookie 横幅的保存与应用可能被意外破坏；手动检查数百个网页极耗人力。
- 🌍 **规模化挑战**：Dropbox 有 200 多个网页表面，Cookie 因用途而异；还需支持 Global Privacy Control（GPC）等自动传递的隐私偏好信号。
- ⚙️ **规则转化**：隐私与工程团队将法律概念（如 opt-in、严格必要）转化为机器可执行的具体测试标准，并让批准 Cookie 列表和例外项由隐私团队直接更新，无需改代码。
- 🖥️ **内部集成**：因自研 Cookie 横幅，审计器可直接对接现有同意基础设施，便于随产品与法规要求调整审计规则。
- 🧪 **类似用户的测试**：审计器使用 Playwright，在全新隔离浏览器会话中启动；每次对每页运行三种测试：美国默认、欧盟默认、带 GPC 信号。
- 🔄 **验证用户选择**：测试先记录页面加载时的 Cookie，再点击“拒绝非必要 Cookie”（识别底层控件而非文字），随后重载页面确认偏好仍然生效，若有异常则记录待审。
- 🔍 **发现覆盖盲区**：审计器只能测试已知 URL，因此团队借助流量数据（数十亿条记录）过滤出唯一路径，再经多轮筛选排除无需测试页面、合并同类逻辑，并选取代表性 URL 进行审计。
- 🛡️ **持续验证隐私**：隐私与可靠性、安全性一样需要持续关注；每周报告会区分潜在违规与已知误报，帮助团队快速定位问题，并追踪趋势变化。
- 📊 **实践启示**：自动化只是其中一环；真正的关键工作是定义正确行为、维护可靠待测清单、区分真实问题与噪音，并建立恰当的团队协作审查流程。

---

### [](https://neil.fraser.name/news/2026/09/03/)

**原文标题**: [Neil Fraser: News: .name Termination](https://neil.fraser.name/news/2026/09/03/)

Neil Fraser 在 2026 年因 Verisign 与 ICANN 终止整个 .name 第三级域名而面临个人域名、邮箱及网络身份被彻底剥夺的风险，他正在准备法律应对。

- 📅 作者约 25 年前注册了 neil.fraser.name 和 bev.fraser.name，长期作为网站、邮箱及 API 服务的稳定载体。
- 🏢 2026 年 4 月 15 日，Verisign 以简化管理为由提议销毁整个 .name 第三级域名，7 月 28 日获 ICANN 批准。
- 🔍 与声誉不佳的普通三级域名不同，.name 是专门设立的三级体系，类似 *.ny.us 和 *.co.uk，并非可疑操作。
- 😠 作者最初选择 .name 是因为其运营方为 Global Name Registry 而非 Verisign，但后来 Verisign 收购了该公司；作者指责提案中包含谎言。
- 💥 后果包括：网站将在 2 月消失（即便已付费至 2040 年）、邮箱失效、依赖该域名的 IoT 设备变砖，作者等于从互联网上消失。
- 🕳️ 更严重的是，第三级域名消失后，他人可能抢注 fraser.name，进而控制 neil.fraser.name，劫持数十年间关联的账户、身份认证与设备。
- ⚖️ 此次受影响的还有约 22,000 人，作者表明准备诉诸法律手段。

---

### [使用Three.js、WebGPU和TSL构建无限液态玻璃网格 | Codrops](https://tympanus.net/codrops/2026/09/08/building-an-infinite-liquid-glass-grid-with-three-js-webgpu-and-tsl/)

**原文标题**: [Building an Infinite Liquid Glass Grid with Three.js, WebGPU, and TSL | Codrops](https://tympanus.net/codrops/2026/09/08/building-an-infinite-liquid-glass-grid-with-three-js-webgpu-and-tsl/)

这篇文章展示了如何利用 Three.js、WebGPU 和 TSL 构建一个无光源、无后处理的无限液体玻璃网格。作者详细拆解了用 SDF 伪造玻璃、球面伪装无限平面、以及用 GPU 布料模拟实现流动效果的技术细节。

- 🌊 核心实验：一个由数百张玻璃视频卡片组成的“无限液体玻璃旋转木马”，在浏览器 WebGPU 中实时运行，场景中没有任何光源。
- 🧱 技术栈：基于 Next.js、React Three Fiber v10、WebGPU 与 TSL；使用 MeshBasicNodeMaterial 自定义 colorNode，单 pass 完成，无需后处理或渲染目标。
- 🔮 玻璃伪造术：每张卡片只是扁平细分平面；用圆角矩形 SDF 计算边缘距离，进而建立高度图模拟玻璃厚度与斜角（可调 bevelPower）。
- 📐 法线来源：对高度图做上下左右的小步采样，用差值求斜率并生成表面法线，从而支撑后续折射与反射计算。
- 🌈 色散折射：对每个颜色通道使用不同折射率，多次 refract 并采样自身视频纹理，叠加后产生彩色边缘；TSL 的 JS for 循环会在编译时展开，tap 数量可灵活调节画质。
- 💡 反射与菲涅尔：用反射方向采样环境贴图，通过菲涅尔公式控制从垂直视角到掠射角的反射强度，营造真实玻璃感。
- ✨ 边缘高光：基于 SDF 距离执行 smoothstep，形成贴合卡片边缘的细长光带，并叠加垂直方向渐变，模拟来自上方的光。
- 🌍 无限网格的骗局：卡片实际被放置在巨大球面上，x/y 坐标被理解为沿球面行走的距离；拖动时，从一侧消失的卡片会从另一侧悄悄绕回，让视角产生“无限延伸”的错觉。
- 🖱️ 流畅拖拽：拖动用 Motion 的 pan 手势处理，位置和速度存于 motionValue；R3F 帧循环直接读取，不从 React 重渲染。
- 🧾 文本方案演进：最初用 CSS3DRenderer 手写 div + matrix3d 让真实 HTML 精确跟随 WebGPU 网格；后来改用 pmndrs/glyph 的 MSDF 字体在场景内渲染，使文字能随布料变形并参与折射。
- 🌊 “液体”升级：加入 GPU XPBD 布料模拟（TSL compute pass），卡片锚定在球面上，同时带有距离/弯曲约束和粘度，让网格拖动时呈现迟滞、涟漪与果冻般的摆动。

---

### [](https://www.freecodecamp.org/news/how-the-chrome-dino-game-works/)

**原文标题**: [How the Chrome Dino Game Works Under the Hood: A Tour of Chromium's Source Code](https://www.freecodecamp.org/news/how-the-chrome-dino-game-works/)

overview summary  
这篇文章深入解析了 Chrome 恐龙游戏背后的 Chromium 源码，揭示了它如何通过时间缩放、物理常量、公平生成规则、精确碰撞检测和隐藏细节，成为一款设计精巧的游戏，并总结了可迁移到其他项目的工程经验。

- 🕐 游戏用 deltaTime 按实际时间缩放速度，而非按帧移动，确保在不同刷新率设备上运行速度一致且公平。
- 🦖 恐龙物理由少量常量定义：重力 0.6、跳跃初速 -10、速度上限 13，单位基于 60 FPS 的像素/帧。
- ✏️ 源码中“INIITAL_JUMP_VELOCITY”拼错为三个 I，随 Chrome 分发近十年，且因改动风险而不修。
- 🎮 跳跃高度可控制：轻点空间键小跳，按住则全弧跳跃，空中按↓会加速下坠，提升操作上限。
- ⚖️ 游戏内置“公平引擎”：开局 3 秒无障碍、障碍间距随速度变大、集群障碍需先达到足够速度才出现、同类型障碍不会连续出现三次。
- 🦤 翼龙只在速度达到 8.5 后出现，且有独立速度偏移，以打破玩家节奏感，但绝不会形成无解局面。
- 📦 碰撞检测用多个小矩形而非单个大框：恐龙站立时是 6 个盒子，下蹲时换成 1 个长低盒；先粗略外框判断，再精细逐盒检测，视觉上更“诚实”。
- 🌙 到达 700 分触发夜晚模式，持续 12 秒；月亮有 7 个不同相位循环变化，星星以更慢速度移动形成视差。
- 👀 细节藏得很深：待机时恐龙会随机眨眼、得分基于像素乘 0.025、计分板满五位后刻意“归零”、移动端有独立速度系数、死亡后 750ms 内防误触重启。
- 🧠 可借鉴之处：用时间而非帧驱动运动、按玩家当前能力生成障碍、用空场代替新手教学、用历史记录保证多样、让碰撞贴合视觉、为看不见的细节投入设计感。

---

### [](https://www.bram.us/2026/09/07/animating-css-grid-layouts-with-css-anchor-positioning/)

**原文标题**: [Animating CSS Grid Layouts with CSS Anchor Positioning – Bram.us](https://www.bram.us/2026/09/07/animating-css-grid-layouts-with-css-anchor-positioning/)

本文介绍了一种利用 CSS Anchor Positioning 配合 CSS Transitions 实现网格重排动画的技术，该方案无需 JavaScript，也无需 View Transitions，动画可中断且性能自然。

- 📐 核心思路：将每个网格单元的内容锚定到自身，通过过渡动画实现尺寸变化时的平滑移动。
- 🧱 结构要点：网格单元是虚拟概念，需要额外包裹一个 `<div class="content">` 作为锚点，并将该内容绝对定位到对应单元上。
- 🎨 布局代码：使用 `display: grid; grid-template-columns: repeat(auto-fill, 6rem); gap: 1em;` 建立自适应网格。
- 🔗 锚点设置：为每个 `.cell` 设置 `anchor-name: --a;` 和 `anchor-scope: --a;`，使锚点在各自单元内作用，避免命名冲突。
- 📏 精确控制：`.cell` 设置 `aspect-ratio: 1;` 保持正方形；`.content` 使用 `inset: anchor(inside);` 并显式设置 `width` 与 `height`，防止插值过程中拉伸。
- ✨ 动画实现：`.content` 上添加 `transition: inset 0.2s ease;`，即可在网格重排时平滑过渡到新位置。
- 🚀 主要优势：不需要 JavaScript 动画控制，完全由 CSS 驱动；调整视口时动画不排队，可立即响应并打断。
- ⚠️ 浏览器注意：Firefox 目前不支持 Anchor Positioning 的 style/layout 交错处理，因此网格会直接跳变而不会动画。
- 🖥️ 演示案例：文章提供了两个 CodePen 示例，分别展示基础动画与高保真版（接近 Brave 新标签页效果）。
- 📚 相关延伸：Chris Coyier 曾将其与 Masonry.js 的动画效果对比，并强调该方案在原生 CSS 中实现了类似行为。

---

### [drawably — 手绘UI控件](https://www.drawably.dev/)

**原文标题**: [drawably — hand-drawn UI controls](https://www.drawably.dev/)

overview summary：Drawably 是一个轻量级手绘风格 UI 组件库，提供多种可交互控件，并能在加载或悬停时自动重绘笔画，支持 React 与原生 JavaScript 使用。

- ✏️ 手绘风格 UI 组件，每个控件在加载时都会重新生成笔画效果
- 🖱️ 悬停控件即可触发重新绘制，交互体验生动
- 🧩 提供按钮、复选框、输入框、卡片、单选框、开关、分割线、箭头等多种组件
- 📦 零依赖，主要通过 CSS 实现手绘效果，无需额外库
- ⚛️ 支持 React 组件导入及原生 JS API 调用，接入方式灵活
- 🎨 笔触类型包含 Pen、Pencil、Marker，满足不同手绘质感需求
- 📥 通过 npm 安装（`npm i drawably`），当前版本 v0.3.10，MIT 许可

---

### [](https://github.com/Danilaa1/drawably)

**原文标题**: [GitHub - Danilaa1/drawably: Hand-drawn UI controls. Every mount generates a fresh pen sketch from seeded randomness, and the stroke boils like an animated doodle. Zero dependencies, 4 KB of JS and one stylesheet. · GitHub](https://github.com/Danilaa1/drawably)

drawably 是一个零依赖、轻量的手绘风格 UI 控件库，约 7 KB JS（gzipped）+ 3 KB CSS；每次挂载都会用随机种子生成独特的手绘草图，笔画带有微动的“沸腾”动画效果。内置真实 DOM 交互与无障碍支持，提供 React 封装、文本装饰、可选手绘字体，以及可导出的底层绘图工具，整体基于 MIT 协议开源。

- 📦 安装与快速开始：通过 `npm i drawably` 安装，调用 `drawablyButton(el, opts)`；React 项目使用 `<DrawablyButton>`，每次挂载返回句柄，可调用 `resketch()` / `destroy()`。
- 🖊️ 按钮变体与异步状态：支持 `outline`（默认）、`solid`、`scribble`；内置 `idle`、`loading`、`error`、`success` 状态，可用 CSS 变量调整状态颜色，并通过 `tone` 设置中性/危险风格。
- 🧩 控件类型丰富：提供按钮、复选框、单选、开关、输入框、文本域、选择框、分割线、卡片、徽章、列表等；列表可自定义 `dash`/`check` 标记，所有控件都有对应 React 组件。
- ♿ 真实的无障碍支持：原生 input/select/textarea 保留在 DOM 中，键盘、表单、标签和读屏器正常工作；手绘 SVG 位于底层且标记为 `aria-hidden`。
- ✍️ 文本装饰与标注：提供下划线、高亮、圆圈、箭头，可插入任意单词或短语；跨行自动逐行绘制，箭头使用文档坐标并且随滚动/缩放重绘。
- ⚙️ 统一配置选项：所有控件接受 `seed`（可复现草图）、`roughness`（抖动）、`boil`（帧间动画像素）、`stroke`/`fill`/`paper` 颜色与 `width` 宽度；颜色基于 CSS 自定义属性便于主题化。
- 🎭 动效与减少动态偏好：笔画以 1200ms 循环三帧微抖动画，hover/press 会重新手绘交互控件；完全支持 `prefers-reduced-motion`，在用户要求减少动态时冻结为静态草图。
- 🔠 可选手绘字体：提供 Drawably Pen 字体（31 KB，包含字母、数字和标点），通过 `import "drawably/font.css"` 引入；默认不加载，无需字体也能正常使用。
- 🛠️ 导出底层构建工具：可用 `roughRoundedRect`、`roughLine`、`roughCircle`、`roughArrow`、`roughCheckmark`、`scribbleFill` 等函数生成 SVG 路径，`variants()` 生成动画帧；还导出 PRNG `mulberry32` 和 `randomSeed`。
- 📜 开源与体积：仓库为 MIT 许可；核心无依赖，React 封装增加不到 1 KB，适合对体积敏感的嵌入场景。

---

### [](https://vgpu.sh/)

**原文标题**: [vgpu](https://vgpu.sh/)

在浏览器和 Node.js 等环境中，用同一 Shader 做到“一处编写、处处渲染”。vgpu 是一个基于 WebGPU 的渲染库，能支持交互式画布、高分辨率图片、视频输出和 CI 渲染测试；它还为 WGSL 提供模块化导入、构建期优化和命令行工具，并内置多个高级渲染示例。

- 🔁 一次性编写着色器，即可在浏览器和 headless Node.js 中运行，支持交互式画布、任意分辨率（如 8192×4608 PNG）、60fps MP4 视频和 CI 无头渲染测试。
- 📦 用 `effect()` 从 WGSL 源创建渲染效果，调用 `.draw()` 即可输出到指定目标（target）。
- ♻️ 支持像 TypeScript 一样导入/导出 WGSL 模块；构建时自动解析模块图、反射绑定、移除未使用声明并压缩源码。
- ✂️ 示例中一个包含结构体、公式的着色器经优化后仅生成 397 字节的紧凑 WGSL 代码。
- 🧰 提供 `npx vgpu` 命令行工具，可查阅文档、拉取示例、校验 WGSL 语法（check）以及诊断运行时问题（doctor）。
- 🖼️ 内置丰富示例：屏幕空间折射的玻璃立方体（Transmission）、光线追踪黑洞（Black Hole）、基于 FFT 的海洋表面、Radiance Cascades 的二维全局光照等。
- 📚 文档涵盖快速开始、核心概念、API 参考和示例源码；同时面向 agent 工具提供 Examples API 参考和 OpenAPI 3.1 描述。

---

### [EAS观察](https://expo.dev/services/eas-observe?utm_source=frontendfocus&utm_medium=email&utm_campaign=observe-ga)

**原文标题**: [EAS Observe](https://expo.dev/services/eas-observe?utm_source=frontendfocus&utm_medium=email&utm_campaign=observe-ga)

EAS Observe 是 Expo 为 Expo / React Native 应用推出的生产环境性能监控服务。通过安装 expo-observe，它能自动采集真实用户会话中的启动性能、屏幕级耗时、错误与自定义事件，并把所有指标与对应的 EAS 构建或 OTA 更新关联，让开发者快速定位“是哪个版本拖慢了体验”，从而更快发现并修复问题。

- 📦 一键接入：安装 expo-observe 后，自动上报冷启动/温启动、Bundle 加载、首次渲染、可交互时间等 5 类启动指标，并附带帧率、电池、热状态和网络信息。
- 🔗 发布即关联：每个 EAS Build 和 OTA Update 都会作为标记出现在性能时间线上，悬停可看差异，点击可查看该版本的所有会话，方便对比发布前后变化。
- 🧭 路由级分析：通过 Expo Router 集成，将“可交互时间”按屏幕/路由拆分，支持多选路由对比，快速定位是哪个页面让用户等待最久。
- 🛑 精确错误定位：JavaScript 错误带有指向源码文件与行号的堆栈，不再面对压缩混淆代码，并按错误原因聚合，可判断修复应走 EAS Update 还是发新版。
- ⏱️ 完整性能分布：支持 P50 / P90 / P99 分位数，覆盖从旗舰机到低端设备的真实表现；可下钻到单个会话查看设备、OS、更新渠道和完整事件时间线。
- 📈 自定义会话时间线：通过 Observe.logEvent 记录登录、结算、同步失败等业务关键事件，结合导航与性能事件，还原用户转化或流失前的完整现场。
- 🤖 适合人看也适合 Agent：可在 Dashboard 阅读，也能通过 CLI / Expo Skills 让 AI Agent 直接拉取指标、路由、事件和会话；Observe 会自动生成发送给 Agent 的完整上下文 prompt，省去手动复制粘贴。
- 🔐 数据隐私与采样：只收集性能计时、设备型号、OS 版本、App 版本和匿名安装 ID，不含个人身份信息；可设置 sampleRate（按安装确定性采样），也可运行时用 dispatchingEnabled 控制上报。
- 💰 免费额度：单次安装即可在几分钟内获得真实会话数据，Free 计划每月包含 100,000 个事件。
- ⚙️ 适用与定位：面向 Expo SDK 55+ 并使用 EAS 的应用；纯 React Native CLI 支持仍在路线图中。Observe 与 Sentry/Datadog 互补——Observe 专注 EAS 发布管线关联，而错误追踪与通用 APM 由其他工具负责。

---

### [](https://wcagtoolkit.com/wcag-radar)

**原文标题**: [WCAG Radar: 28 free checks in your browser | WCAG Toolkit](https://wcagtoolkit.com/wcag-radar)

WCAG Radar 是由无障碍审计公司 Proper Access 推出的浏览器端无障碍检查工具，提供 46 项 WCAG 2.2 检查，其中 28 项可免费使用。它支持通过书签或浏览器扩展在本地运行，可在登录后页面与 localhost 使用，且不会向服务器发送任何页面数据。工具面向内容编辑、设计与开发者设有不同检查面板，还提供专家问答、报告导出等付费增强功能。

- 🧰 核心定位：在浏览器中直接对当前页面执行无障碍检查，帮助用户快速定位和修复常见 WCAG 问题。
- 🆓 免费与付费：28 项检查永久免费，无需账户；付费许可证可解锁全部 46 项检查、完整书签工具及报告导出功能。
- 🖥️ 安装方式：提供书签和 Chrome、Firefox、Safari 扩展；书签适用于无法安装软件的工作电脑，扩展对严格 CSP 站点更可靠。
- 🔒 隐私设计：所有检查在浏览器本地完成，不收集 IP、不使用 Cookie，适合内网、登录环境和本地开发。
- 📑 内容作者面板：检查替代文本、标题结构、链接文字、表格、页面语言、样式关闭后的阅读顺序，以及隐藏内容和强调标记等。
- 🎨 设计师面板：覆盖文本与边框对比度、灰度模拟、200% 文字缩放、页面缩放、文本间距、320px 重排、目标尺寸和动效检查。
- 👨‍💻 开发者面板：包含 ARIA 角色与属性、可访问名称、Tab 顺序、iframe 标题、自动填充、必填字段和错误消息关联等。
- 💡 专家问答支持：每项检查均可跳转至审计门户，使用“点数”向高级审计师提问，答复通常需 3 至 5 个工作日。
- 📄 报告导出：付费版可将测试会话生成为 HTML 报告，按元素列出检查结果、状态及对应文本，便于团队跟进。
- 💰 定价模式：个人许可证每年 €119 或每月 €11.95；团队订阅按席位计费，起价为每年 €350，席位越多单价越低。
- 🔁 持续更新：开发活跃，每月新增检查项；书签版会自动获取最新版本，扩展版经商店审核后更新。
- 🧑‍🤝‍🧑 定位边界：自动化工具仅能发现约 30%–40% 的问题，适合审计前自行排查，不能替代专业人工审计。

---

### [](https://github.com/thoughtbot/roux)

**原文标题**: [GitHub - thoughtbot/roux: A boilerplate of pre-defined native CSS styling · GitHub](https://github.com/thoughtbot/roux)

Roux 是 thoughtbot 发布的一个开源样板，提供预定义的原生 CSS 架构与 HTML 组件。它不是一个重型框架，而是一套可挑选、可扩展的起点，帮助开发者在启动新项目时快速建立有组织、可维护的样式系统。

- 🎨 核心定位：Roux 提供组织良好的 CSS 文件、变量、基础样式和简单 HTML 组件，可整体采用或按需挑选，类似“样式表模板仓库”。
- 🧩 解决痛点：避免从空白 CSS 文件开始，默认处理样式组织、颜色与间距变量、浏览器重置、表单/按钮/排版一致性以及可访问性等问题。
- ✅ 适用场景：适合想手写原生 CSS、需要结构化起点、想用 CSS 变量统一设计令牌、启动新项目或重构混乱样式的开发者。
- ❌ 不适用场景：偏好 Tailwind 等 utility-first 框架、需要复杂 JS 交互组件、或已有成熟 CSS 体系的团队不建议使用。
- 📦 包含内容：按表单、排版、按钮、表格等拆分的文件结构，集中在 `_variables.css` 的设计令牌，基础元素样式，以及语义化可访问的 HTML 组件。
- ⚙️ 安装方式：运行 `npx github:thoughtbot/roux init` 可将 `src/css` 复制到项目根目录的 `css` 文件夹，也可手动复制源码或直接 clone 仓库。
- 🚀 快速开始：安装后修改 `_variables.css` 中的颜色，在页面中导入 `app.css`，并把自定义组件样式放入 `css/components/`；可选使用 Lightning CSS 编译成一个文件。
- 💎 Rails 集成：Rails 8 的 Propshaft 不支持 CSS `@import`，建议通过 cssbundling-rails 和 PostCSS 进行打包，避免浏览器多次请求。
- 🗂️ 文件结构：包含 `reset/`、`base/`、`components/`、`utilities/` 和入口 `app.css`；导入顺序上，重置最先，`_variables.css` 和 `_fonts.css` 作为依赖较早导入。
- 🎯 定制设计令牌：颜色系统先定义原始色阶（如 `--color--blue-100`），再映射为语义变量（如 `--color--primary-base`），并遵循 `--property--variant` 命名；还可扩展暗色模式。
- 🔡 字体定制：在 `_fonts.css` 中使用 `@font-face` 添加字体，并配合 `font-display: swap`，然后在 `_variables.css` 中定义字体栈供排版使用。
- 🔘 按钮与表单：按钮使用 `.button` 加 `.button--primary`/`--secondary` 类，可作用于 `<button>` 或 `<a>`；表单推荐将 `<input>` 嵌套在 `<label>` 内，利用 CSS `:has()` 实现纵向排列。
- 🧱 其他基础样式：涵盖动画（尊重 reduced motion）、details/summary 折叠面板、响应式媒体、dialog 模态框、圆角条纹表格、以及标题粗体等排版默认值。
- 🛠️ 组件与工具：`components/` 可放置自定义组件 CSS；utilities 提供 `.hide-visually` 等辅助类，支持屏幕阅读器可访问的视觉隐藏，并预留 `.u-[name]` 扩展模式。
- 🤝 开源与贡献：项目使用 MIT License，接受 bug 报告和 PR，参与需遵守 code of conduct；由 thoughtbot 维护和资助，面向自定义 CSS 开发者开放使用。

---

### [](https://roux.thoughtbot.dev/)

**原文标题**: [Roux CSS & Components](https://roux.thoughtbot.dev/)

Roux 是一套原生 CSS 架构与 HTML 组件样板，旨在为项目提供组织化的样式表、变量、基础样式和可访问的语义化组件。它不是 Tailwind 或 Material UI 那类框架，而更像一个可灵活选用或整体采用的启动基础，适合用来快速搭建自己的 CSS 与 HTML 结构。

- 📁 提供原生 CSS 文件架构、变量、基础样式与简单 HTML 组件，助你免去从零搭建
- 🧩 可挑选所需部分、当作灵感来源，或整体采用整套系统，灵活且可扩展
- ♿ 所有 HTML 组件默认追求可访问性与语义化，确保用户友好
- 🔁 可看作 Bitters 与 Refills 的替代方案，走向全原生配置
- 📦 包含 Alert、Badge、Button、Dialog/Modal、Disclosures、Form、Loading Indicator 等常用组件
- 📋 另有 Page Footer/Header、Pagination、Quote、Search、Table 与 Typography 等页面级样式
- 🤝 欢迎通过 GitHub 提交 bug 与 pull request，也鼓励在讨论区分享新功能想法
- 📜 项目遵循 code of conduct，并使用 thoughtbot 的开源许可
- 🏢 由 thoughtbot 维护与赞助，提供开源项目及商业合作服务

---

### [The Fixi项目](https://fixiproject.org/)

**原文标题**: [The Fixi Project](https://fixiproject.org/)

Fixi 项目是一组轻量级 Web 库集合，每个库都以极简方式重新实现现有工具（如 htmx、hyperscript、idiomorph、fetch 等），支持单独或打包使用，并采用 BSD-0 许可。

- 🚲 fixi（3.4/1.2kb）：受 htmx 启发，提供超级增强 HTML 的功能。
- 🥊 moxi（4.6/1.8kb）：受 hyperscript 启发，提供内联脚本与响应式能力。
- 📡 ssexi（4.1/1.4kb）：受 hx-sse.js 启发，支持流式 HTML 与事件处理。
- ♻️ paxi（1.5/0.6kb）：受 idiomorph 启发，用于 DOM 补丁与 morphing。
- 🐕 rexi（4.3/1.4kb）：受 fetch 启发，提供更符合人体工学的 fetch() 封装。
- 📦 每个库都是独立脚本，可通过 script 标签、npm、vendor 或 CDN 引入；建议先加载 moxi.js 再加载 fixi.js。
- 🧰 提供 All-in-One 合包（约 4.5kb br），包含全部五个库的压缩版本，也可通过 npm 安装 the-fixi-project。
- 📄 所有 fixi 项目均采用 BSD-0 许可，并托管在 Github 上。

---

### [](https://github.com/bigskysoftware/the-fixi-project)

**原文标题**: [GitHub - bigskysoftware/the-fixi-project: The Fixi Project · GitHub](https://github.com/bigskysoftware/the-fixi-project)

该仓库介绍的是 “The Fixi Project”——一组由五个小型 Web 库组成的集合，每个库的源码（未压缩、未混淆）都小于 Preact 的 min.gz 大小（约 4.7KB），并强调可组合性与轻量。

- 🚲 **fixi.js**：基于 htmx，通过元素属性（如 `fx-action`、`fx-method`）直接从 DOM 发起 HTTP 请求，并用服务器返回的 HTML 替换自身或目标元素。
- 🥊 **moxi.js**：提供 `on-*` 内联脚本与响应式 `live` 属性，行为可直接写在元素上，无需单独 `<script>`，支持 `q()`、`trigger()`、`wait()` 等辅助函数。
- 📡 **ssexi.js**：为 fixi 增加 Server-Sent Events 支持，可在响应为 `text/event-stream` 时流式追加消息到目标，也可触发自定义 DOM 事件。
- ♻️ **paxi.js**：基于 idiomorph 的 DOM 形变（morph）策略，按 id 就地更新子树，保留焦点、选区、输入状态和事件监听，并支持 CSS 过渡。
- 🐕 **rexi.js**：流畅的 `fetch()` 封装，自动处理表单/对象序列化、非 2xx 抛错、解码响应以及按需中止，可直接接收对象、`FormData` 或表单元素。
- 🧰 **the-fixi-project.js**：提供预合并、压缩并 brotli 压缩的统一包，整个项目压缩后约 4.4KB，可通过 CDN 引入。
- ⚙️ **开发命令**：`npm install`、`npm run clone`、`npm test`（可限定子项目）、`npm run build`、`npm run llms`、`npm run demo`、`npm run serve`。
- 📜 **许可证**：全部库采用 BSD-0（Zero-Clause BSD），项目拥有 52 stars、3 forks，并托管于 GitHub。

---

### [](https://strich.io/?ref=frontend-focus)

**原文标题**: [STRICH | Barcode Scanning for Web Apps](https://strich.io/?ref=frontend-focus)

STRICH 是一个基于 JavaScript 的实时条码扫描 SDK，可在 Web 浏览器中直接识别 1D/2D 条码，无需后端。它主打纯前端处理、现代 Web 技术兼容性、轻松集成与高识别率，同时提供企业级支持和透明定价，并附带 14 天免费试用。

- 🌐 纯前端实时扫描：无需后端，摄像头画面在浏览器内即可完成 1D/2D 条码解码与识别。
- ⚡ 基于现代 Web 技术（WebAssembly/WebGL），兼容 iOS/Android 各主流浏览器与框架，且零第三方依赖。
- 🔍 支持 Code128、EAN/UPC、QR Code、Data Matrix、PDF417 等常用码制，也能应对褪色、破损、反光及反色条码。
- 🖼️ 内置完整扫描 UI（瞄准框、闪光灯、点按聚焦），并提供一行代码即可调用的 Popup Scanner。
- 🛠️ 为开发者优化：可从 NPM/CDN 安装，提供 TypeScript 类型、各框架示例及完善文档，集成通常不到一天。
- 📱 Web 应用优势：无应用商店审核与分发限制，链接即更新，一套代码省成本，也支持 PWA 安装体验和离线能力。
- 💼 企业级方案：可选自定义品牌白标、离线许可检查，获得 GS1 Solution Partner 认证，并由团队持续维护与支持。
- 💶 透明定价：提供 Basic、Professional、Business、Enterprise 多个档位，不限设备数量，支持随时取消和免费试用。
- 🗣️ 客户口碑突出：在户外、光照不佳等严苛场景下仍能快速可靠识别，明显优于 ZXing/Quagga 等免费库。

---

### [](https://confectioneryapp.com/)

**原文标题**: [Confectionery: Clean website screenshots for macOS](https://confectioneryapp.com/)

这段内容介绍 Confectionery，一款为 macOS 打造的极简浏览器，目标是移除标签页、工具栏等界面噪音，让设计截图干净且完整地呈现。

- 🍬 Confectionery 专注于“干净网页截图”，没有标签页、地址栏、工具栏或扩展的干扰。
- 🎨 浏览器窗口颜色会自动适配当前网站，让内容看起来更沉浸、不分心。
- 🖥️ 对比 Chrome、Firefox、Safari：它们截图时总会留下标签栏、工具栏或浏览器控件，影响设计展示。
- ✂️ Confectionery 为设计作品留出完整屏幕，特别适合设计师展示或保存网页截图。
- 💻 免费提供给 Mac 用户，开发者是 Vadim Demedes。

---

