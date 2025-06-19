### [前端聚焦第 697 期：2025 年 6 月 18 日](https://frontendfoc.us/issues/697)

**原文标题**: [Frontend Focus Issue 697: June 18, 2025](https://frontendfoc.us/issues/697)

订阅随时可取消，邮箱安全有保障（隐私政策在此）。

- 🚀 CSS 新特性：微软 Edge 团队推出间隙装饰（gap decorations），减少伪元素 hack 需求，提供交互式演示页面（需 Chromium 浏览器启用标志）。  
- ✅ 前端开发者趣味清单：Nic Chan 分享前端开发的幽默自嘲清单，值得探索。  
- 📊 SurveyJS 赞助：支持 React/Angular/Vue 3 的表单构建工具，可完全自定义 UI 与数据控制。  
- 🎨 Payload 加入 Figma：开源 CMS Payload 被收购，未来将与设计系统深度集成（James Mikrut 在 Syntax 播客讨论）。  
- 🔒 HTML 规范更新：Chrome 团队修改属性中转义尖括号的规则，防止 XSS 漏洞。  
- 🐱 CSS 动画技巧：Jake Archibald 详解变换顺序对动画自然度的影响（附猫咪示例）。  
- ♿ ARIA 指南：Eric Bailey 分享 ARIA 实用建议与常见误区。  
- 🍎 Safari 争议：Alex Russell 批评苹果 WWDC'25 对 Web 生态的消极态度。  
- 🧩 CSS 创意实验：Sladjana 用 (S)CSS 构建七巧板交互界面。  
- 🍔 汉堡菜单研究：Kate Kaplan 分析其识别度与固有缺陷。  
- 🧰 工具推荐：  
  - Anime.js 4.0：强大的 Web 动画库，支持 SVG/DOM。  
  - Tonkotsu AI 赞助：自然语言 IDE，免费早期体验。  
  - 关键 CSS 生成器：按需提取并压缩 CSS。  
  - DarkModeJS 2.0：基于用户偏好管理深色模式。  
  - RampenSau：色板生成库，支持色调循环与缓动函数调整。

---

### [CSS 间隙样式新方法  |  Chrome 开发者博客](https://developer.chrome.com/blog/gap-decorations)

**原文标题**: [A new way to style gaps in CSS  |  Blog  |  Chrome for Developers](https://developer.chrome.com/blog/gap-decorations)

Chrome 和 Edge 139 推出了 CSS 间隙装饰功能，为 Flex、Grid 和多列布局中的间隙提供了新的样式解决方案，无需依赖边框或伪元素等传统技巧。

- 🎨 **CSS 间隙装饰功能**：支持通过`column-rule`和新增的`row-rule`属性直接样式化间隙，提升视觉一致性和可维护性。  
- 🚀 **优势**：不影响布局、支持`repeat()`语法、无需额外 DOM 元素，并提供更多自定义属性（如`*rule-break`和`gap-rule-paint-order`）。  
- ⚙️ **试用方式**：在 Chrome 或 Edge 139 中启用实验性功能标志（`edge://flags`或`chrome://flags`），并通过开发者互动演示体验。  
- 📱 **示例演示**：包括汉堡菜单、笔记本布局和每日 CSS 新闻等案例，展示不同场景下的间隙装饰应用。  
- 📢 **反馈征集**：开发者可通过提交 Chromium bug 报告分享使用体验，帮助完善功能（目前暂不支持动画和超多网格轨道场景）。  
- 📜 **许可信息**：内容遵循 Creative Commons 4.0 许可，代码示例采用 Apache 2.0 许可。

---

### [获取失败](https://frontendfoc.us/link/170526/web)

**原文标题**: [Failed to retrieve](https://frontendfoc.us/link/170526/web)

无法总结：获取内容失败，状态码 403。

---

### [CSS 间隙装饰效果实验场](https://microsoftedge.github.io/Demos/css-gap-decorations/playground.html)

**原文标题**: [CSS Gap Decorations playground](https://microsoftedge.github.io/Demos/css-gap-decorations/playground.html)

这是一个展示 CSS Gaps Decorations Module Level 1 特性的交互式演示，允许实时调整间距和规则属性，适用于多列、弹性盒和网格布局。

- 🎮 交互式演示：通过控件实时调整间距（gap）、规则（rule）和绘制顺序（paint-order）属性。
- 🏗️ 布局支持：演示适用于多列（multicolumn）、弹性盒（flex）和网格（grid）布局。
- ⚠️ 浏览器兼容性：目前仅 Chromium 内核浏览器支持，需启用`--enable-features=CSSGapDecoration`标志。
- 🛠️ 网格布局设置：可调整行/列规则宽度、样式、颜色、间距及跨越项行为。
- 📏 弹性盒布局设置：支持自定义行/列规则参数与特殊宽度的弹性项。
- 📚 多列布局设置：提供列间距、规则样式及动态视口适应功能。
- ✨ 核心优势：通过纯 CSS 实现视觉分隔，无需额外标签，保持语义结构清晰。
- 📝 操作提示：建议结合`column-rule`系列属性控制分隔线样式与交互逻辑。  

（注：演示包含虚拟文本"Lorem ipsum"作为内容占位符，实际功能以官方规范为准）

---

### [你还不算前端开发者，除非你…… - Nic Chan](https://www.nicchan.me/blog/youre-not-a-front-end-developer-until-youve/)

**原文标题**: [You're not a front-end developer until you've... - Nic Chan](https://www.nicchan.me/blog/youre-not-a-front-end-developer-until-youve/)

一位拥有 10 年前端开发经验的开发者以幽默自嘲的方式，分享了一系列行业内的趣事和常见经历，并附上了一个互动式评分小测试。

- 🎉 开发者庆祝职业生涯 10 周年，分享一系列幽默自嘲的行业趣事  
- 🕵️‍♂️ 花数小时排查页面出现横向滚动条的原因  
- 🎨 被要求放大 Logo 并改成霓虹绿色  
- 📏 被要求将元素向右移动两个像素  
- ⚡ Meta 产品 API 突然崩溃的无奈经历  
- 🐛 在生产环境搞崩网站  
- 🔄 写出一个在 Firefox、Chrome 或 Safari 中轮流出错的循环 bug  
- 💡 向他人解释问题时自己突然找到解决方案  
- 🔍 搜索问题发现结果指向自己写的博客文章  
- 💾 坚称不是缓存问题结果就是缓存问题  
- 🔄 刷新生产环境后疑惑本地修改未生效  
- 😤 因 DNS 设置崩溃或大发雷霆  
- 🌓 对深色/浅色模式有强烈偏好  
- 🏷️ 购买域名做副业一年后任其过期  
- 🚧 完成副业 90% 后因失去兴趣放弃  
- 🛠️ 开发仅对自己有用的细分项目  
- 👨‍👩‍👧‍👦 为家人自制简陋但能用的应用替代付费方案  
- 🏗️ 产生创业点子并给名称去掉元音字母  
- 🎨 不断产生重做个人网站的冲动  
- 🔄 用新框架重写去年刚用其他框架写完的项目  
- 📻 为娱乐收听开发类播客  
- 🧙‍♂️ 用开发者技能在非技术朋友面前炫技  
- 🌾 幻想辞职归隐从事木工或农耕  

（注：以上已从原文 30 条经历中精选最具代表性的 23 条进行呈现，保留核心幽默元素和行业洞察，省略部分重复或相似条目）

---

### [Payload 即将加入 Figma！](https://payloadcms.com/posts/blog/payload-is-joining-figma)

**原文标题**: [Payload is joining Figma!](https://payloadcms.com/posts/blog/payload-is-joining-figma)

Payload 宣布加入 Figma，未来将共同解决设计与代码之间的鸿沟问题，同时保持其开源承诺和核心功能不变。

- 🎉 **重大消息**：Payload 正式加入 Figma，双方将共同推动设计与开发的无缝协作。  
- 🎨 **愿景一致**：Figma 认可 Payload 的开源理念，双方在简化工作流程和提升开发者体验上目标一致。  
- 🔄 **解决痛点**：通过整合设计系统与 CMS，减少设计师与开发者之间的重复劳动，提升内容管理效率。  
- 🔒 **不变承诺**：Payload 保持开源、自托管，团队和现有功能（如开发者体验、社区支持）均不受影响。  
- 🚀 **未来计划**：借助 Figma 资源，拓展更多功能（如设计系统集成），扩大用户群体和测试范围。  
- ❓ **答疑渠道**：用户可通过 Discord 和 GitHub 提问，团队将及时回应。  
- 📢 **用户保障**：短期内 Payload 的使用方式不变，长期将逐步推出创新解决方案。

---

### [Figma 为何收购内容管理系统？ - YouTube](https://www.youtube.com/watch?v=6wvoauy80gc)

**原文标题**: [Why did Figma buy a CMS? - YouTube](https://www.youtube.com/watch?v=6wvoauy80gc)

该内容为 YouTube 网站底部的导航链接列表，涵盖版权、联系、创作者、广告合作等相关信息。

- 📢 关于我们  
- 🗞️ 新闻动态  
- ©️ 版权信息  
- 📞 联系我们  
- 🎨 创作者相关  
- 💼 广告合作  
- 👩💻 开发者资源  
- 📜 使用条款  
- 🔒 隐私政策  
- ⚖️ 政策与安全  
- 🔧 YouTube 运作机制  
- 🧪 测试新功能  
- ®️ 谷歌公司版权所有（2025）

---

### [HTML 规范变更：属性中转义<和> | 博客 | Chrome 开发者](https://developer.chrome.com/blog/escape-attributes)

**原文标题**: [HTML spec change: escaping < and > in attributes  |  Blog  |  Chrome for Developers](https://developer.chrome.com/blog/escape-attributes)

HTML 规范更新：在属性中转义<和>字符，以增强安全性并防止 mXSS 漏洞。

- 🛠️ 2025 年 5 月 20 日，HTML 规范更新，要求在属性中转义<和>字符，防止 mXSS 漏洞。
- 🚀 该变更已在 Chrome 138 Beta 版（2025 年 5 月 28 日）中实现，并将于 2025 年 6 月 24 日发布稳定版。
- 🔍 变更影响：使用 innerHTML、outerHTML 或 getHTML() 时，属性中的<和>会被转义为&lt;和&gt;。
- ⚠️ 可能受影响的情况：通过正则表达式解析 HTML 属性值或依赖静态 HTML 比较的测试可能会失败。
- 🔄 未受影响的情况：DOM API（如 getAttribute、dataset 等）仍返回解码后的值，与之前一致。
- 📅 其他浏览器支持：Firefox 140 和 Safari 26 Beta 也将跟进此变更。
- 🐛 如遇问题，可通过 https://issues.chromium.org/提交反馈。
- 📚 更多信息：包括原始错误报告、规范变更 PR、ChromeStatus 条目及安全博客文章链接。

---

### [使用 CSS 实现缩放动画：变换顺序有时很重要… - JakeArchibald.com](https://jakearchibald.com/2025/animating-zooming/)

**原文标题**: [Animating zooming using CSS: transform order is important… sometimes - JakeArchibald.com](https://jakearchibald.com/2025/animating-zooming/)

概述  
本文探讨了 CSS 中 transform 属性顺序对动画效果的影响，特别是缩放（scale）和平移（translate）组合时的“怪异”动画现象，并提供了解决方案和深入的技术分析。

- 🌀 **问题现象**  
  - 缩放动画出现“俯冲”效果，而非直线放大，原因是 scale 和 translate 的顺序不当导致 translate 受 scale 倍数影响。

- 🔍 **原因分析**  
  - CSS 动画通过线性插值计算 transform 属性，scale 在后会动态放大 translate 的位移值，导致非线性动画。

- 🛠️ **解决方案**  
  - 调整顺序为`translate`在前，并手动乘以 scale 值（如`translate(-99.3%, 60.6%) scale(3)`），或使用 CSS 变量和`calc()`简化计算。

- ⚠️ **伪修复陷阱**  
  - 初始设置`rotate(0)`会强制 CSS 用矩阵动画，偶然解决但依赖边缘情况，不推荐。

- 📐 **替代方案：3D 透视**  
  - 使用`perspective`和 3D 位移（如`translateZ`）模拟更自然的“靠近”效果，但动画曲线与 scale 不同。

- 🔧 **开发技巧**  
  - 拆分`translate`和`scale`为独立属性，或利用 CSS 变量提升代码可维护性。

---

### [OAuth 提供商改进](https://clerk.com/changelog/2025-06-13-oauth-improvements?utm_source=cooper-press&utm_medium=newsletter&utm_campaign=oauth&utm_content=06-18-25&dub_id=DaeBAQHfiQSzmcAf)

**原文标题**: [OAuth Provider Improvements](https://clerk.com/changelog/2025-06-13-oauth-improvements?utm_source=cooper-press&utm_medium=newsletter&utm_campaign=oauth&utm_content=06-18-25&dub_id=DaeBAQHfiQSzmcAf)

Clerk 宣布对其 OAuth 功能进行了重大扩展，新增多项特性以支持更广泛的应用场景，包括 MCP 服务的实现。

- 🔒 OAuth 令牌现在可以通过 Clerk 的 SDK 进行验证并即时撤销。
- 📜 支持授权服务器元数据，开箱即用。
- 🖥️ OAuth 授权流程新增了同意屏幕，确保用户明确授予权限。
- 🌐 改进了 CORS 处理，支持在浏览器中完成令牌交换的公共客户端。
- 🔄 支持 OAuth 客户端的动态客户端注册。
- 🤖 Clerk 的 OAuth 实现满足使用 Clerk 作为授权服务的 MCP 服务的所有要求。

- 📚 Clerk 发布了详细的 OAuth 指南，解释了 OAuth 的三种不同用途：OAuth 范围访问、OAuth 单点登录（SSO）和 OAuth 用户管理。
- 🛠️ 提供了如何在 Clerk 应用中实现 OAuth 范围访问的指南。
- 🔍 Clerk 的 Next.js SDK 示例展示了如何验证 OAuth 访问令牌。
- 📱 目前大多数 SDK 生态系统都支持 OAuth 令牌验证，包括 Next.js、JavaScript 后端 SDK、Express SDK 等。
- 🚧 即将推出的 SDK 包括 Astro、Nuxt、PHP、Go、Ruby、Expo 和 iOS。

- ✅ 新的 OAuth 同意屏幕显示请求应用的名称、徽标和请求的范围，提供清晰的接受/拒绝选项。
- ⚙️ 新 OAuth 应用默认启用同意屏幕，现有应用默认禁用但强烈建议启用。
- 🔄 支持动态客户端注册，允许通过 API 编程创建 OAuth 客户端。
- 🤖 Clerk 的 OAuth 功能现在支持构建 MCP 服务，允许 AI 应用安全访问用户数据。
- 🔜 自定义范围功能即将推出，目前正在收集用户反馈以优先开发。

---

### [OAuth 提供商改进](https://clerk.com/changelog/2025-06-13-oauth-improvements?utm_source=cooper-press&utm_medium=newsletter&utm_campaign=oauth&utm_content=06-18-25&dub_id=DaeBAQHfiQSzmcAf)

**原文标题**: [OAuth Provider Improvements](https://clerk.com/changelog/2025-06-13-oauth-improvements?utm_source=cooper-press&utm_medium=newsletter&utm_campaign=oauth&utm_content=06-18-25&dub_id=DaeBAQHfiQSzmcAf)

Clerk 宣布对其 OAuth 功能进行了重大扩展，新增多项特性以支持更广泛的应用场景，包括 MCP 服务的实现。

- 🔒 OAuth 令牌现在可以通过 Clerk 的 SDK 进行验证和即时撤销。
- 📜 支持授权服务器元数据，开箱即用。
- 🖥️ OAuth 授权流程新增了同意屏幕，确保用户明确授权范围。
- 🌐 改进了 CORS 处理，支持在浏览器中完成令牌交换的公共客户端。
- 🔄 支持 OAuth 客户端的动态客户端注册。
- 🤖 Clerk 的 OAuth 实现满足 MCP 服务作为授权服务的所有要求。
- 📚 提供了详细的 OAuth 指南和实现示例，帮助开发者快速上手。
- 🛠️ OAuth 令牌验证已在多数 SDK 中可用，包括 Next.js、JavaScript 后端 SDK 等，其他 SDK 支持即将推出。
- ✅ 新增的 OAuth 同意屏幕显示请求应用的名称、徽标和请求的权限范围，增强安全性。
- 🔧 动态客户端注册允许通过 API 编程方式创建 OAuth 客户端。
- 🚀 Clerk 的 OAuth 改进为构建 MCP 服务提供了坚实基础，支持 AI 应用安全访问用户数据。
- 🔜 自定义 OAuth 范围的支持即将推出，开发者可通过路线图提供反馈。

---

### [我初学 ARIA 时希望有人告诉我的事——Smashing Magazine](https://www.smashingmagazine.com/2025/06/what-i-wish-someone-told-me-aria/)

**原文标题**: [What I Wish Someone Told Me When I Was Getting Into ARIA — Smashing Magazine](https://www.smashingmagazine.com/2025/06/what-i-wish-someone-told-me-aria/)

以下是按照您提供的模板对文章内容的总结：

overview summary  
本文由设计师 Eric Bailey 撰写，旨在为初学者提供关于 ARIA（Accessible Rich Internet Applications）的实用指南。文章涵盖了 ARIA 的基本概念、历史背景、使用规则、常见误区以及实际应用中的注意事项，帮助读者更好地理解和应用 ARIA 以提升网页可访问性。

- 🧠 **ARIA 的核心概念**  
  ARIA 是一种通过 HTML 标记为屏幕阅读器和语音控制软件提供额外信息的技术，用于增强交互性、目的和状态的传达。

- 🕰️ **ARIA 的历史背景**  
  ARIA 最初发布于 2006 年，旨在弥补 HTML 在交互体验可访问性方面的不足，其设计反映了当时的操作系统交互范式。

- 📜 **ARIA 的使用规则**  
  1. 优先使用原生 HTML 元素；  
  2. 不要修改原生元素的语义；  
  3. 确保所有交互元素可通过键盘操作；  
  4. 不要在可聚焦元素上使用`role="presentation"`或`aria-hidden="true"`；  
  5. 为交互元素提供明确的名称。

- ⚠️ **常见误区与注意事项**  
  - ARIA 角色有特定含义，不能随意使用（如误用`role="menu"`）；  
  - ARIA 不会自动解锁功能，仅提供提示；  
  - 某些 ARIA 状态需要特定角色支持；  
  - 并非所有 ARIA 声明都能被辅助技术支持。

- 🛠️ **实际应用建议**  
  - 动态更新 ARIA 状态（如`aria-expanded`）；  
  - 避免冗余 ARIA 声明（如`<button role="button">`）；  
  - 谨慎使用`aria-label`和`aria-live`；  
  - 测试时需考虑操作系统、浏览器和辅助技术的组合支持。

- 🔍 **测试与验证**  
  - 手动测试辅助技术（如 NVDA、JAWS）是确保 ARIA 有效的关键；  
  - macOS VoiceOver 可能存在支持问题，建议以 Windows 屏幕阅读器为基准。

- 💡 **ARIA 的扩展用途**  
  - 可通过 CSS 为 ARIA 状态添加样式；  
  - 在 UI 测试中使用 ARIA 属性（如`getByRole`）提高测试的可靠性。

- ❤️ **ARIA 的终极目标**  
  ARIA 的核心是关心用户，确保残障人士能够平等地使用网络体验。

---

### [WWDC '25 上的 Safari：圣诞幽灵往事 - 鲜为人知的笔记](https://infrequently.org/2025/06/the-ghost-of-christmas-past/)

**原文标题**: [Safari at WWDC '25: The Ghost of Christmas Past - Infrequently Noted](https://infrequently.org/2025/06/the-ghost-of-christmas-past/)

苹果在 2025 年 WWDC 上宣布了 Safari 的一系列新功能，其中大部分功能在其他主流浏览器中早已实现。以下是关键点总结：

- 🚀 **功能追赶**：Safari 新增的功能大多已在 Chromium 等浏览器中推出多年，如 WebGPU（2023）、SVG Favicons（2020）、HDR Images（2023）等。  
- 🏗️ **少量创新**：苹果在部分功能上领先，如 Digital Credentials API、CSS 的`contrast-color()`和 ALAC 格式支持，但这些功能可能在其他浏览器中更快推出。  
- 📉 **长期落后**：过去十年中，Safari 在功能完整性上一直落后于其他浏览器引擎。  
- ⚖️ **欧盟法规应对**：苹果在遵守欧盟《数字市场法案》时表现消极，设置技术障碍和苛刻合同条款，阻碍其他浏览器引擎在 iOS 上的竞争。  
- 💰 **高额利润**：苹果通过与谷歌的交易每年获利约 190 亿美元，但对 WebKit 和 Safari 的投入极少。  
- 🔥 **批评与呼吁**：文章指责苹果故意压制 Web 生态，呼吁开发者不要被其营销话术误导，并强调苹果有能力但不愿加大投入改进浏览器技术。  

整体来看，Safari 的更新更多是弥补与其他浏览器的差距，而非真正的创新，同时苹果在开放浏览器竞争和投资 Web 生态方面表现消极。

---

### [液态玻璃：苹果，你该明白——纳特·塔诺夫](https://tarnoff.info/2025/06/11/liquid-glass-apple-you-know-better/)

**原文标题**: [Liquid Glass: Apple, you know better – Nat Tarnoff](https://tarnoff.info/2025/06/11/liquid-glass-apple-you-know-better/)

苹果发布了名为“Liquid Glass”的新设计系统，引发了对可访问性的担忧，作者呼吁苹果作为无障碍领域的领导者应重新考虑这一设计。

- 👁️ Apple 推出“Liquid Glass”设计系统，UI 呈现玻璃效果，包括透明背景、光谱畸变和高光阴影。  
- 🎨 字体颜色随背景自动调整，但未说明混合背景下的处理方式。  
- ⚠️ 默认设计存在对比度问题，可能影响普通及低视力用户的可访问性。  
- 🏛️ 作者批评该设计与苹果近期“全球无障碍意识日”承诺相矛盾，认为苹果内部专家应提出反对。  
- 📱 苹果的设计风格常被业界模仿，此次可能引发更广泛的无障碍隐患。  
- ♿ 在当前联邦政府政策对残障人士不利的背景下，作者呼吁苹果坚守无障碍领导地位。  
- 🔍 建议通过 LinkedIn 或 Bluesky 平台进一步讨论此问题。

---

### [如何跟上 CSS 新特性 | CSS-Tricks](https://css-tricks.com/how-to-keep-up-with-new-css-features/)

**原文标题**: [How to Keep Up With New CSS Features | CSS-Tricks](https://css-tricks.com/how-to-keep-up-with-new-css-features/)

文章概述了如何跟踪 CSS 新特性的多种方法和资源，帮助开发者及时了解最新动态。

- 🌐 **Google 的 web.dev 博客**：Rachel Andrew 每月发布的 Web 平台更新，涵盖 CSS、JavaScript 和 HTML 的新特性。  
- 📚 **CSS-Tricks 等出版物**：包括 CSS 特性大全和其他优质资源，如 Smashing Magazine、Frontend Masters Blog 等。  
- 🔍 **Web Platform Features Explorer**：基于 Baseline 状态查找新特性的结构化工具。  
- 📊 **Web Platform Status 仪表盘**：提供更精细的过滤功能，如按 Baseline 年份或 Top CSS Interop 筛选特性。  
- 📈 **Chrome Platform Status 仪表盘**：提供特性采用率的详细数据，包括顶级网站的使用情况。  
- 🛠️ **Polypane 浏览器**：提供实验性 Chromium 特性探索工具，按版本分类。  
- 🎥 **Kevin Powell 的 YouTube 频道**：定期发布 CSS 新特性的视频总结，并提供每周 HTML 和 CSS 技巧。  
- 📢 **CSS 工作组**：直接关注 CSS 工作组的邮件列表或 RSS 源，获取最新动态。  
- 📱 **浏览器发布说明**：关注 Chrome、Safari 和 Firefox 的发布说明，了解新 CSS 特性的支持情况。  
- 🤖 **ChatGPT**：通过提问获取过去一年或即将支持的 CSS 新特性。  
- 📅 **其他资源**：如 Igalia 的 BCD Watch、HTTP Archive Web Almanac、caniuse 新闻版块等。  
- 🐦 **社交媒体**：关注 Bluesky、Mastodon 等平台上的 CSS 专家，获取最新讨论和实验。  
- 📝 **State of CSS 调查**：参与年度调查，了解并标记新特性，生成个人阅读列表。

---

### [突破界限：用 (S)CSS 构建七巧板拼图 | CSS-Tricks](https://css-tricks.com/breaking-boundaries-building-a-tangram-puzzle-with-scss/)

**原文标题**: [Breaking Boundaries: Building a Tangram Puzzle With (S)CSS | CSS-Tricks](https://css-tricks.com/breaking-boundaries-building-a-tangram-puzzle-with-scss/)

概述总结  
作者通过纯 CSS 和 Sass 构建了一个完全交互式的七巧板拼图游戏，挑战了传统认为此类游戏必须依赖 JavaScript 的观点。文章详细介绍了从 HTML 结构设计、Sass 映射数据管理到动态样式生成的完整实现过程，展示了 CSS 在交互式 UI 中的潜力。

- 🧩 **挑战传统认知**：作者最初认为拖拽旋转类游戏必须使用 JavaScript，但通过 Sass 的映射、混合和函数成功实现了纯 CSS 解决方案。  
- 🎯 **项目动机**：探索 CSS 的交互极限、提升 CSS 技能，并享受纯 CSS 实现的乐趣。  
- 🛠️ **核心工具**：利用 Sass 的映射存储拼图形状数据（颜色、路径、位置等），通过混合动态生成 CSS 规则，避免重复代码。  
- 📐 **HTML 结构**：使用大量单选按钮模拟交互状态（如旋转角度、拼图形状选择），通过 Pug 模板简化 HTML 编写。  
- 🔄 **旋转逻辑**：用 8 个单选按钮模拟 45°递增旋转，通过标签切换实现无限旋转效果。  
- 🏆 **胜利条件**：预定义正确拼图组合，通过混合验证玩家放置是否正确，触发反馈动画或锁定拼块。  
- 🌟 **纯 CSS 魔法**：最终实现包括开始/重置、拼块拖拽、旋转、位置验证及胜利庆祝等完整功能，无 JavaScript 依赖。

---

### [1fr 1fr vs auto auto vs 50% 50% —— Frontend Masters 博客](https://frontendmasters.com/blog/1fr-1fr-vs-auto-auto-vs-50-50/)

**原文标题**: [1fr 1fr vs auto auto vs 50% 50% – Frontend Masters Blog](https://frontendmasters.com/blog/1fr-1fr-vs-auto-auto-vs-50-50/)

概述总结  
文章探讨了 CSS Grid 中三种列定义方式（`1fr 1fr`、`auto auto`、`50% 50%`）的异同，通过实例展示了它们在默认、添加间隙和内容溢出时的表现差异，并提供了解决方案和实用建议。

- 🎯 **基本行为对比**  
  三种方式（`1fr 1fr`、`auto auto`、`50% 50%`）默认均生成等宽两列，但底层逻辑不同。

- ⚠️ **百分比单位的风险**  
  `50% 50%`在添加间隙（`gap`）时会超出容器宽度（因总宽度变为`100% + 间隙值`），需手动调整计算避免溢出。

- 🤹 **auto 的动态性**  
  `auto`列宽由内容决定，不同文本量会导致列宽不均，适合内容尺寸明确但需注意不可预测性。

- 📏 **fr 单位的灵活性**  
  `1fr`按剩余空间比例分配，通常最直观，但可能因内容（如长 URL）被迫扩展，需配合`minmax(0, 1fr)`限制最小宽度。

- 🛠️ **混合使用与进阶关键词**  
  可组合不同单位（如`20% 1fr`）或使用`min-content`/`max-content`等关键词应对复杂布局需求。

- 🔍 **推荐学习资源**  
  提及 Jen Kramer 的 CSS 布局课程，涵盖 Grid、Flexbox 等现代布局技术。

---

### [汉堡菜单图标今日辨识度探究 - NN/g](https://www.nngroup.com/articles/hamburger-menu-icon-recognizability/)

**原文标题**: [The Hamburger-Menu Icon Today: Is it Recognizable? - NN/g](https://www.nngroup.com/articles/hamburger-menu-icon-recognizability/)

概述总结  
汉堡菜单图标如今已被广泛认知，但仍需遵循隐藏导航的最佳实践。尽管用户对其熟悉度提高，但设计时仍需注意位置、样式和标签，以避免混淆和提升可用性。  

- 🍔 汉堡菜单如今比十年前更被用户熟悉，但隐藏导航的最佳实践依然适用。  
- 📉 早期研究发现，汉堡菜单降低了用户参与度、任务完成率和满意度。  
- 📱 随着移动优先设计的普及，汉堡菜单成为空间节省的经典解决方案。  
- 🔍 近期研究表明，用户能正确识别标准样式的汉堡菜单图标，尤其是在左上角位置。  
- ⚠️ 类似样式的图标（如列表或筛选图标）可能被误认为汉堡菜单，需谨慎设计。  
- 🛠️ 设计汉堡菜单时，应使用标准三线图标、置于左上角、添加“菜单”标签并避免多余装饰。  
- 🔄 隐藏导航始终会增加交互成本，因此仅在必要时使用汉堡菜单。  
- 📚 进一步阅读资源包括关于图标可用性和导航模式的研究与指南。

---

### [错误](https://frontendfoc.us/link/170630/web)

**原文标题**: [Error](https://frontendfoc.us/link/170630/web)

无法总结：获取内容时出错 - ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))

---

### [想成为更优秀的前端工程师？试试一周待命值班——丹·奥德尔](https://denodell.com/blog/try-a-week-on-call)

**原文标题**: [Want to Be a Better Frontend Engineer? Try a Week On-Call — Den Odell](https://denodell.com/blog/try-a-week-on-call)

值班一周能显著提升前端工程师的技能和责任感，通过实战压力暴露系统弱点并改进开发习惯。

- 🚨 **直面真实问题**：凌晨 2:43 处理用户无法结账的故障，发现后端数据问题导致前端按钮失效，凸显前端需对全链路体验负责。  
- 🧠 **改变质量思维**：值班迫使你不仅关注代码是否工作，更关注失败时的表现、可调试性及容错能力。  
- 🌐 **前端是故障集散地**：用户所有问题都通过前端暴露，如服务中断、令牌过期、第三方脚本阻塞等，需主动掌控体验。  
- 🛠️ **为失败而设计**：习惯性添加清晰加载状态、空数据/错误处理、详细日志，并假设一切可能出错。  
- ❓ **提问更全面**：开始思考 API 无返回、功能开关失效等极端场景，避免用户陷入不可用界面。  
- ⏰ **开发即责任**：值班带来问责制，减少偷懒的 TODO 和“本地能用就行”的侥幸心理，代码更健壮。  
- 💡 **高效学习**：一周值班胜过数月 Bug 跟踪，真实压力暴露系统弱点，倒逼开发方式升级。

---

### [构建无障碍 UI 的自私理由 | 阅读茶叶迹象](https://nolanlawson.com/2025/06/16/selfish-reasons-for-building-accessible-uis/)

**原文标题**: [Selfish reasons for building accessible UIs | Read the Tea Leaves](https://nolanlawson.com/2025/06/16/selfish-reasons-for-building-accessible-uis/)

文章讨论了构建无障碍 UI 的自私理由，强调无障碍设计不仅对残障人士有益，也能提升开发者自身的开发体验和效率。

- 🐛 **调试便利性**：使用语义化 HTML（如`<table>`）比`<div>`更易于在开发者工具中定位和调试元素。  
- 🏷️ **命名规范**：遵循 ARIA 规范（如`combobox`、`listbox`）能减少命名困扰，统一代码语义。  
- � **测试友好性**：无障碍属性（如`role`和`aria-*`）使 UI 测试更健壮，减少对易变类名的依赖。  
- ⌨️ **提升键盘操作**：支持键盘快捷键（如`Esc`关闭弹窗）能优化开发者自身的使用体验。  
- 🌱 **行业现状反思**：当前网页无障碍达标率低，但通过“利己”角度说服开发者可能比道德说教更有效。

---

### [恶意浏览器扩展的风险日益加剧 - Socket](https://socket.dev/blog/the-growing-risk-of-malicious-browser-extensions)

**原文标题**: [The Growing Risk of Malicious Browser Extensions - Socket](https://socket.dev/blog/the-growing-risk-of-malicious-browser-extensions)

乌克兰国歌被嵌入 JavaScript UI 工具包以针对俄语网站  

- 🔍 Socket 发现 npm 包中隐藏的抗议软件，针对俄语访客  
- 🛑 该软件会阻止用户交互并播放乌克兰国歌  
- 🌐 主要影响使用特定 JavaScript UI 工具包的俄语网站  
- 📅 事件曝光于 2025 年 6 月 17 日  
- 📢 由研究员 Olivia Brown 披露

---

### [Anime.js | JavaScript 动画引擎](https://animejs.com/)

**原文标题**: [Anime.js | JavaScript Animation Engine](https://animejs.com/)

overview summary  
Anime.js 是一个快速且多功能的 JavaScript 动画库，提供丰富的工具集和直观的 API，支持从基础动画到复杂交互的所有需求。  

- 🚀 **高性能动画引擎** - 快速、轻量且功能强大，适用于任何网页动画需求。  
- 📦 **模块化设计** - 按需导入功能，保持代码体积小巧（核心仅 24.5KB）。  
- 🛠️ **全面工具集** - 支持 CSS 变换、SVG 路径动画、时间轴同步、滚动触发等。  
- 🎨 **直观 API** - 简单易用的语法，支持属性级参数、关键帧和内置缓动效果。  
- 🔄 **高级功能** - 包含拖拽交互、弹簧物理效果、响应式媒体查询适配等。  
- 📜 **时间轴控制** - 精确编排动画序列与回调同步。  
- 🖱️ **交互支持** - 内置拖拽 API 和滚动观察器，增强用户互动体验。  
- 📱 **响应式设计** - 通过 Scope API 轻松适配不同屏幕尺寸。  
- 💡 **免费开源** - 由社区赞助支持，提供详细文档和示例代码。  
- 🌟 **跨浏览器兼容** - 突破浏览器限制，统一动画实现方式。  

示例代码片段展示了常见用途，如元素旋转、路径跟随、形状变形等。

---

### [SVG | Anime.js | JavaScript 动画引擎](https://animejs.com/documentation/svg/)

**原文标题**: [SVG | Anime.js | JavaScript Animation Engine](https://animejs.com/documentation/svg/)

overview summary  
本文详细介绍了动画库 Anime.js 的核心功能和使用方法，包括安装、基本用法、动画参数设置、回调函数、方法调用、属性配置以及实用工具等。内容涵盖了从基础到高级的各个方面，适合开发者快速上手并深入使用。

- 🚀 **入门指南**  
  - 安装与导入  
  - 支持原生 JS 和 React  

- ⏱️ **动画控制**  
  - 定时器与播放设置（延迟、持续时间、循环等）  
  - 回调函数（开始、完成、更新等）  

- 🎛️ **方法与属性**  
  - 播放控制方法（播放、暂停、重启等）  
  - 动画目标类型（CSS 选择器、DOM 元素、JS 对象等）  

- 🎨 **动画属性**  
  - 支持 CSS 属性、变换、变量  
  - 支持 SVG 属性和 HTML 属性  

- 🔢 **补间动画参数**  
  - 数值、颜色、函数等补间类型  
  - 关键帧与补间参数设置  

- 📊 **时间轴功能**  
  - 添加动画与同步时间轴  
  - 播放设置与回调函数  

- 🕹️ **可拖动功能**  
  - 坐标轴参数与设置  
  - 回调函数与方法调用  

- 🔍 **滚动观察器**  
  - 容器与目标设置  
  - 阈值与同步模式  

- 🛠️ **实用工具**  
  - 动画引擎参数与方法  
  - SVG 工具（变形、路径动画等）  

- 🔄 **其他功能**  
  - 范围与随机工具  
  - 链式工具与硬件加速优化

---

### [入门指南 | Anime.js | JavaScript 动画引擎](https://animejs.com/documentation/getting-started/)

**原文标题**: [Getting started | Anime.js | JavaScript Animation Engine](https://animejs.com/documentation/getting-started/)

overview summary  
Anime.js 是一个功能强大的 JavaScript 动画库，支持多种动画配置和方法，涵盖从基础安装到高级功能的全面指南。  

- 📥 **安装与导入**  
  - 提供下载、安装和导入 Anime.js 的详细步骤  
  - 包含迁移指南（适用于从 v3 升级的用户）  

- 🛠️ **核心功能**  
  - 支持原生 JS 和 React 使用  
  - 提供计时器（Timer）和播放设置（Playback settings）  

- ⚙️ **动画参数**  
  - 延迟（delay）、持续时间（duration）、循环（loop）等基础参数  
  - 高级选项如反向播放（reversed）、自动播放（autoplay）  

- 🔄 **回调函数**  
  - 动画生命周期钩子：开始（onBegin）、完成（onComplete）、更新（onUpdate）等  

- ▶️ **控制方法**  
  - 播放（play）、暂停（pause）、重启（restart）等操作  
  - 高级控制如跳转（seek）、拉伸（stretch）  

- 🎯 **目标类型**  
  - 支持 CSS 选择器、DOM 元素、JS 对象等多种目标  
  - 可动画属性包括 CSS 变换、变量、SVG 属性等  

- 🌈 **动画值类型**  
  - 数值、颜色、函数等多样化插值方式  

- 📊 **时间轴（Timeline）**  
  - 支持添加动画、同步时间轴、函数调用等功能  

- 🖱️ **拖拽功能（Draggable）**  
  - 配置轴参数、回调函数及物理模拟设置  

- 🔍 **滚动观察（ScrollObserver）**  
  - 容器与目标配置、阈值设定及滚动同步模式  

- 🔧 **工具与实用功能**  
  - 提供随机数、插值、单位转换等链式工具  
  - 支持硬件加速和 WAAPI 优化  

- ⚡ **引擎配置**  
  - 时间单位、帧率、精度等全局参数设置

---

### [豚骨拉面](https://www.tonkotsu.ai)

**原文标题**: [Tonkotsu](https://www.tonkotsu.ai)

好的，请提供需要总结的文本内容，我会按照您要求的格式生成概述和带表情符号的要点列表。  

示例格式：  

这里是文章的概述总结。  

- 📌 第一个关键点  
- 🔍 第二个关键点  
- 💡 第三个关键点  

请提供具体内容，我会为您生成相应的总结！

---

### [GitHub - toolwind/anchors: Tailwind CSS 锚点定位工具，提供简洁 API 实现相对于自定义锚点的灵活声明式定位](https://github.com/toolwind/anchors)

**原文标题**: [GitHub - toolwind/anchors: Anchors for Tailwind CSS provides a simple API for working with CSS anchor positioning, enabling flexible, declarative positioning relative to custom anchors.](https://github.com/toolwind/anchors)

这是一个关于 Tailwind CSS 插件 "Anchors for Tailwind CSS" 的介绍，该插件提供了对 CSS 锚点定位 API 的支持，使开发者能够通过 Tailwind 的实用类来灵活地定位元素。

- ⚓ **插件功能**：提供声明式支持 CSS 锚点定位 API，包括定义锚点（`anchor-name`）和相对于锚点定位元素（`position-anchor`、`position-area` 等）。
- 📦 **安装方式**：通过 npm 安装 `@toolwind/anchors` 并在 Tailwind 配置文件中引入。
- 🛠️ **使用方法**：  
  - 使用 `anchor/{name}` 定义锚点。  
  - 使用 `anchored/{name}` 将元素附加到锚点。  
  - 使用 `anchored-{position}` 指定元素相对于锚点的位置区域。  
  - 结合 `anchored-{side}/{name}` 在单个实用类中完成锚定和定位。
- 📏 **支持的工具类**：包括 `anchor/{name}`、`anchored/{name}`、`anchored-{position}` 等，以及高级功能如条件可见性（`position-visibility`）和备用定位（`position-try-order`、`position-try-fallbacks`）。
- 🔄 **视图过渡 API 集成**：每个 `anchored/{name}` 类包含 `view-transition-name`，支持使用浏览器原生视图过渡 API 进行平滑动画。
- 📚 **额外资源**：提供 MDN、CSS Tricks 和规范文档链接，帮助开发者深入了解 CSS 锚点定位 API。
- 🎯 **优势**：声明式锚点定位、完整支持原生 CSS 属性、内置视图过渡支持、完全 JIT 兼容无需运行时。

---

### [CSS 锚点定位 | 我能用... HTML5、CSS3 等支持情况表](https://caniuse.com/css-anchor-positioning)

**原文标题**: [CSS Anchor Positioning | Can I use... Support tables for HTML5, CSS3, etc](https://caniuse.com/css-anchor-positioning)

CSS 锚点定位功能允许元素相对于“锚元素”在页面上任意放置，不受其他元素布局影响，目前全球使用率为 71.45%。

- 🌍 **全球使用率**：71.45%  
- 📌 **功能描述**：元素可相对于锚元素自由定位，不受其他布局限制  
- ⚙️ **浏览器支持情况**：  
  - **Chrome**：✅ 125+ 版本支持  
  - **Edge**：✅ 125+ 版本支持  
  - **Safari**：✅ 26.0+ 版本支持  
  - **Firefox**：❌ 暂不支持  
  - **Opera**：✅ 111+ 版本支持  
  - **IE**：❌ 全版本不支持  
- 📱 **移动端支持**：  
  - **Chrome Android**：✅ 137+ 版本支持  
  - **Safari iOS**：✅ 26.0+ 版本支持  
  - **其他主流安卓浏览器**：多数不支持（如 UC、QQ、Baidu）  
- 🔧 **资源链接**：  
  - 官方博客、Firefox 需求追踪、Polyfill 方案、WebKit 立场说明

---

### [关键 CSS 生成器 | Kigo](https://critical-css-extractor.kigo.studio/)

**原文标题**: [Critical CSS Generator | Kigo](https://critical-css-extractor.kigo.studio/)

好的，请提供需要总结的文本内容，我会按照您要求的模板生成概述和带表情符号的要点列表。  

示例模板：  

概述总结  
- 🌟 要点 1  
- 📌 要点 2  
- 🔍 要点 3  

请提供具体内容，我会为您生成相应的总结！

---

### [GitHub - Assortment/darkmodejs：网页暗色模式管理工具包](https://github.com/Assortment/darkmodejs)

**原文标题**: [GitHub - Assortment/darkmodejs: Utility package for managing Dark Mode on the web](https://github.com/Assortment/darkmodejs)

darkmodejs 是一个用于管理网页暗色模式的实用工具包，利用 matchMedia API 和 prefers-color-scheme 媒体查询来监听和响应系统主题变化。

- 🌐 **功能概述**：支持根据操作系统暗色模式自动切换网页主题，提供主题变化监听和回调功能。  
- 📌 **依赖条件**：需运行在支持暗色模式的操作系统（如 macOS 10.14+、Windows 10 等）和兼容 prefers-color-scheme 的浏览器。  
- ⚠️ **版本注意**：v2+ 版本弃用旧版 MediaQueryList 方法，改用 addEventListener/removeEventListener。  
- 📦 **安装方式**：通过 npm 安装 `@assortment/darkmodejs`，支持 ES6 import 或 ES5 require。  
- 🛠️ **API 配置**：  
  - 接受 `onChange(activeTheme, themes)` 回调函数，返回当前主题（dark/light/no-preference/no-support）。  
  - 提供 `removeListeners()` 方法用于清理监听器。  
- 🎨 **应用示例**：结合 Emotion Theming 实现动态主题切换，提供 [演示项目](https://darkmodejs-demo.netlify.com/)。  
- 📜 **开源协议**：MIT 许可证，由 Luke Whitehouse 维护。  
- 🔗 **资源链接**：  
  - 代码仓库：[GitHub](https://github.com/Assortment/darkmodejs)  
  - 支持浏览器列表：[caniuse](https://caniuse.com)

---

### [GitHub - meodai/rampensau：使用色相循环和简单缓动函数的调色板生成工具](https://github.com/meodai/rampensau)

**原文标题**: [GitHub - meodai/rampensau: Color palette generation function using hue cycling and simple easing functions.](https://github.com/meodai/rampensau)

RampenSau 是一个使用色相循环和缓动函数生成颜色渐变的库，适用于数据可视化、设计、生成艺术等领域。

- 🎨 **功能概述**：RampenSau 通过色相循环和缓动函数生成颜色渐变，支持多种色彩模式和自定义配置。
- 🌈 **主要特性**：
  - 生成基于 HSL/HSV/LCH/OKLCH 的颜色渐变。
  - 支持自定义色相、饱和度和亮度的范围和缓动函数。
  - 提供预定义的曲线方法（如 'lamé'、'sine'）简化配置。
- 📦 **安装方式**：
  - 通过 npm 安装：`npm install rampensau`。
  - 支持 ES 和 CJS 模块导入，也可直接通过 CDN 引入。
- 🛠 **使用方法**：
  - 核心函数 `generateColorRamp` 生成颜色数组（HSL 格式）。
  - 支持色相序列生成或自定义色相列表。
  - 提供 `transformFn` 选项用于颜色后处理或格式转换。
- 🎭 **辅助功能**：
  - 提供 `uniqueRandomHues` 生成唯一随机色相。
  - 支持色彩调和理论（如互补色、三分色等）。
  - 包含实用工具函数（如数组洗牌、插值计算等）。
- 📜 **许可证**：MIT 开源协议，允许自由使用和修改。
- 🌍 **项目背景**：名称 "RampenSau" 结合了德语中的“渐变”和“舞台焦点”，寓意库的视觉表现力。

---

### [RampenSau — 基于 HSL 色彩模型中曲线的色带生成器](https://meodai.github.io/rampensau/)

**原文标题**: [RampenSau — Color ramp generator using curves within the HSL color model](https://meodai.github.io/rampensau/)

RampenSau 是一个轻量级、无依赖且极速的色彩生成库，利用色相循环和缓动函数生成悦目的渐变色阶。

- 🌈 RampenSau 是一个快速、轻量且无依赖的色阶生成库  
- 🎨 通过色相循环（hue cycling）和缓动函数生成平滑渐变色  
- 🚀 提供高度可定制化参数，如起始色相（hStart）、色相中心位置（hStartCenter）和色相循环次数（hCycles）  
- 🔄 hStart 支持多种预设色相值（如 0°红、45°黄、90°绿等）  
- ⚖️ hStartCenter 可调整起始色相在色阶中的位置（0 为起点，1 为终点，默认 0.5 居中）  
- 🔄 hCycles 控制色相变化幅度（1 为完整色相环循环，负值反向循环）  
- 🎲 支持随机生成色阶样本，保持明度/饱和度范围一致  
- 📋 提供 HSL 色彩模型输出（[0-360°, 0-1, 0-1]），兼顾性能与轻量化  
- 📥 可复制色板到剪贴板，但建议直接集成库以实现动态色彩系统  
- 💡 作者倡导将色板视为响应数据/主题的"活系统"，而非静态颜色集合  
- 🔗 开源项目，GitHub 可获取完整代码

---

### [非 HTML 内容](https://frontendfoc.us/open/697/*%7CUID%7C*?ipx=t)

**原文标题**: [Non-HTML content](https://frontendfoc.us/open/697/*%7CUID%7C*?ipx=t)

无法总结：非 HTML 内容。

---

