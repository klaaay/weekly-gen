### [前端聚焦第 732 期：2026 年 3 月 11 日](https://frontendfoc.us/issues/732)

**原文标题**: [Frontend Focus Issue 732: March 11, 2026](https://frontendfoc.us/issues/732)

本期《前端聚焦》简报涵盖了 CSS 动画状态机、HTML 新属性提案、Eleventy 更名、Flash 现代化尝试、Firefox Nova 设计、PWA 支持现状、Chrome 146 更新、前端性能优化及多项开发工具资源。

- 🎨 **CSS 动画状态机**：微软 Edge 团队提出仅用 CSS 实现元素聚焦状态样式的新思路
- ⌨️ **HTML 新属性提案**：Chrome 团队建议新增`focusgroup`属性，用声明式方法简化键盘导航开发
- 🔄 **Eleventy 更名**：静态站点生成器 Eleventy 更名为 Build Awesome，同步启动 Pro 版众筹（已暂停）
- ⚡️ **Flash 现代化尝试**：Newgrounds 开发者计划用现代技术重建 Flash 的创作体验
- 🌐 **浏览器动态**：Firefox Nova 设计预览、PWA 跨设备支持报告、Chrome 146 新增滚动动画与调试工具
- 📊 **前端性能实践**：探讨 z-index 规范化、CSS 锚点定位陷阱、异步页面过渡及地理定位元素特性
- 🛠️ **开发资源更新**：Reveal.js 6.0 发布、React Native 开发体验升级、25 万+SVG 图标库及 JS 压缩基准测试套件

---

### [Patrick - 仅用 CSS 通过 CSS 动画作为状态机记忆焦点和悬停状态](https://patrickbrosset.com/articles/2026-03-09-using-css-animations-as-state-machines-to-remember-focus-and-hover-states-with-css-only/)

**原文标题**: [Patrick  - Using CSS animations as state machines to remember focus and hover states with CSS only](https://patrickbrosset.com/articles/2026-03-09-using-css-animations-as-state-machines-to-remember-focus-and-hover-states-with-css-only/)

本文介绍了一种仅使用 CSS 动画来记录元素是否曾被聚焦或悬停状态的技术，通过将 CSS 动画作为状态机，利用`animation-play-state`和`animation-fill-mode`属性实现状态的持久化。

- 🎯 利用 CSS 动画作为状态机，通过极短动画时长（如 0.00001 秒）和`animation-fill-mode: forwards`使元素在触发后保持最终状态
- 🔄 结合`:focus`或`:hover`伪类触发动画播放，实现无 JavaScript 的焦点或悬停状态记忆
- 🎨 可动画化任意 CSS 属性（包括自定义属性），甚至非动画属性如`content`，用于动态显示图标等效果
- 🏗️ 通过自定义属性（如`--was-focused`）和容器样式查询（`@container style()`）实现条件样式应用，提升代码复用性
- 📦 支持多个元素独立记录状态，适用于表单标签等交互场景，增强用户体验

---

### [获取失败](https://frontendfoc.us/link/181951/web)

**原文标题**: [Failed to retrieve](https://frontendfoc.us/link/181951/web)

无法总结：获取内容失败，状态码 403。

---

### [开发者反馈征集：焦点小组  | 博客  | Chrome 开发者](https://developer.chrome.com/blog/focusgroup-rfc)

**原文标题**: [Request for developer feedback: focusgroup  |  Blog  |  Chrome for Developers](https://developer.chrome.com/blog/focusgroup-rfc)

Chrome for Developers 博客介绍了 `focusgroup` HTML 属性，这是一个新的声明式 API，旨在简化复合小部件（如工具栏、标签页列表、菜单等）的键盘箭头键导航，无需编写繁琐的 JavaScript 代码。该提案由微软通过 OpenUI 社区组提出，并得到谷歌支持，目前处于开发者反馈阶段，可在 Chrome 和 Edge 等 Chromium 浏览器中通过实验性标志或源试用进行测试。

- 🚀 **简化导航**：`focusgroup` 属性通过声明式方式实现箭头键导航，无需手动管理 `tabindex` 或编写 JavaScript 代码。
- 🧩 **支持多种模式**：提供 `toolbar`、`tablist`、`menu`、`menubar`、`listbox` 和 `radiogroup` 等行为令牌，对应 ARIA 创作实践指南中的常见模式。
- 🔧 **灵活配置**：支持 `inline`、`block`、`wrap`、`nomemory` 等修饰符，以控制导航轴、循环行为及焦点记忆。
- 🎯 **焦点控制**：通过 `focusgroupstart` 属性指定初始焦点元素，结合 `nomemory` 修饰符可精确控制焦点行为。
- 🔄 **嵌套与排除**：支持嵌套 `focusgroup`，每个组独立运作；使用 `focusgroup="none"` 可将元素排除在祖先组的箭头导航之外。
- 🌐 **跨边界支持**：默认支持 Shadow DOM 边界，并可结合 CSS `reading-flow` 属性，确保导航顺序与视觉布局一致。
- ♿ **无障碍优化**：浏览器会根据行为令牌自动推断适当的 ARIA 角色，提升无障碍体验，同时允许开发者手动设置角色。
- 🛠️ **渐进增强**：提供 JavaScript 特性检测，可在不支持 `focusgroup` 时回退到手动实现。
- 📢 **征集反馈**：开发者可通过 Chrome 实验性标志或源试用测试该功能，并向 OpenUI GitHub 提交问题，以帮助完善 API 设计。

---

### [WorkOS FGA：AI 代理的授权层 — WorkOS](https://workos.com/blog/agents-need-authorization-not-just-authentication?utm_source=cpff&utm_medium=referral&utm_campaign=q12026)

**原文标题**: [WorkOS FGA: The authorization layer for AI agents — WorkOS](https://workos.com/blog/agents-need-authorization-not-just-authentication?utm_source=cpff&utm_medium=referral&utm_campaign=q12026)

本文介绍了 WorkOS 推出的细粒度授权（FGA）系统，旨在解决 AI 智能体在访问控制方面带来的新挑战。随着 AI 智能体在企业环境中执行任务，传统的基于角色的访问控制（RBAC）模型因其扁平化结构而难以适应智能体动态、细粒度的权限需求。FGA 通过将 RBAC 与资源层次结构相结合，为智能体提供精确的权限范围，防止权限过度授予或泄露，同时支持自动化的生命周期管理。

- 🔐 **智能体打破传统授权模式**：AI 智能体（如文档总结、故障排查代理）使用人类相同的身份验证方式（如 OAuth 令牌），导致权限继承问题，可能引发“混淆代理”风险，泄露敏感数据。
- 🏗️ **细粒度授权（FGA）的核心原理**：FGA 将 RBAC 应用于资源层次结构，允许将角色（如编辑者、查看者）绑定到特定资源节点（如代码分支），实现权限的垂直继承和横向隔离，避免权限泛滥。
- 🤖 **解决两类智能体的授权问题**：对于“代理用户”的智能体，FGA 通过计算用户与智能体权限的交集来实施范围衰减；对于自主智能体，FGA 作为约束层，防止其获得“上帝模式”的根访问权限。
- 🧠 **应对智能体记忆与上下文安全**：FGA 可扩展至智能体的长期记忆管理，通过元数据标记和过滤检索，防止敏感信息在不同用户间泄露，确保上下文安全。
- 🔄 **企业级治理与自动化生命周期**：WorkOS FGA 与身份提供商集成，支持通过 SCIM 等标准自动配置和撤销智能体权限，确保访问权限不会超过其所需时间，满足企业审计和合规要求。
- 🚀 **未来研究方向**：包括多跳委托与来源追溯、即时权限（零常驻权限）以及基于意图的访问控制，旨在使授权系统能够理解智能体的语义意图，并提供动态防护。

---

### [Eleventy 现已更名为 Build Awesome — Eleventy](https://www.11ty.dev/blog/build-awesome/)

**原文标题**: [Eleventy is now Build Awesome — Eleventy](https://www.11ty.dev/blog/build-awesome/)

Eleventy 宣布更名为 Build Awesome，作为加入 Font Awesome 后的品牌统一行动，旨在通过 Kickstarter 众筹获得可持续资金支持，以推动项目长期发展。更名后，现有 Eleventy 项目将保持完全兼容，包括插件、构建命令等，且核心维护团队不变。Build Awesome Pro 版本将为付费用户提供更多功能和服务，同时免费版将继续维护并受益于资金注入。项目原有的 Open Collective 账户仍用于报销社区支出，但未来主要支持渠道将转向 Kickstarter。

- 📢 Eleventy 更名为 Build Awesome，作为 Font Awesome 旗下项目，以统一品牌并寻求可持续发展
- 🔄 更名不影响现有项目兼容性，Eleventy v4 将对应 Build Awesome v4，插件和构建命令均可继续使用
- 💡 Build Awesome Pro 将为付费用户提供增强功能，免费版仍保持开放，资金用于提升整体项目质量
- 🎯 通过 Kickstarter 众筹获取资金，支持项目开发、维护和新功能添加，确保长期稳定
- 🤝 社区贡献者仍可通过 Open Collective 报销费用，但未来主要支持方式转向 Kickstarter
- 📚 相关资源包括升级助手插件、社区博客和会议记录，帮助用户平滑过渡和深入了解变更

---

### [Eleventy 是一款更简洁的静态网站生成器](https://www.11ty.dev/)

**原文标题**: [Eleventy is a simpler static site generator](https://www.11ty.dev/)

Eleventy 是一个简单易用的静态网站生成器，以其快速构建、零配置起步和灵活扩展性著称，支持多种模板语言，无需客户端 JavaScript，适合长期稳定的项目开发。

- 🚀 **快速构建**：Eleventy 在构建速度上表现卓越，处理大量 Markdown 文件时远超其他流行静态站点生成器。
- 🛠️ **零配置起步**：开箱即用，无需复杂设置即可开始项目，同时提供灵活的配置选项进行扩展。
- 🌐 **多模板语言支持**：支持 HTML、Markdown、WebC、JavaScript 等多种模板语言，可在同一项目中混合使用。
- ⚡ **无客户端 JavaScript**：默认不依赖任何 JavaScript 框架，生成纯静态页面，确保网站性能与可访问性。
- 🏗️ **渐进式采用**：允许逐步迁移现有项目，无需一次性重写，仅转换指定文件即可。
- 🔒 **稳定可靠**：自 2017 年发布以来，仅三次更新需开发者调整代码，被 NASA、Google 等大型机构信任使用。
- 📈 **社区活跃**：拥有热情友好的开发者社区，提供丰富的插件、教程和持续改进的支持。
- 🌍 **生产就绪**：已被数千个 GitHub 仓库使用，下载量超过 1600 万次，适合各种规模的生产项目。

---

### [Font Awesome](https://fontawesome.com)

**原文标题**: [Font Awesome](https://fontawesome.com)

本文介绍了人工智能在医疗领域的应用现状与前景，重点探讨了其在疾病诊断、治疗方案优化及医疗管理效率提升方面的作用，并简要提及了相关的技术挑战和伦理考量。

- 🤖 AI 辅助诊断系统能通过分析医学影像快速识别病灶，提高早期疾病检出率
- 💊 基于机器学习的个性化治疗方案可结合患者数据优化用药与治疗路径
- 📊 智能医疗管理平台整合临床数据，助力医院资源调度与远程医疗服务
- ⚠️ 数据隐私保护与算法透明度仍是亟待解决的技术伦理挑战
- 🔮 未来 AI 或将成为医疗人员的协同工具，推动精准医疗发展

---

### [非 HTML 内容](https://webawesome.com)

**原文标题**: [Non-HTML content](https://webawesome.com)

无法总结：非 HTML 内容。

---

### [我们暂停 Kickstarter 众筹——博客精彩继续](https://blog.fontawesome.com/pausing-kickstarter/)

**原文标题**: [We’re Pressing Pause on our Kickstarter—Blog Awesome](https://blog.fontawesome.com/pausing-kickstarter/)

Font Awesome 在 Kickstarter 上发起的 Build Awesome 项目因邮件送达问题导致宣传受阻，已决定暂停众筹活动。项目本身将保持免费开源，而 Build Awesome Pro 是基于该开源框架的付费网站构建工具。团队正在修复邮件系统，并计划在未来重新启动众筹。

- 📧 邮件送达问题导致众筹宣传受阻，仅 5-10% 的目标受众收到启动邮件
- ⏸️ 团队决定暂停 Kickstarter 活动，已支持者不会被扣款
- 🔓 Build Awesome 将始终保持免费开源，众筹旨在支持其长期维护
- 🛠️ Build Awesome Pro 是基于开源框架的付费网站构建工具
- 🔄 团队正在修复邮件系统，并计划未来重新启动众筹
- 📢 呼吁用户通过口碑分享项目，并检查垃圾邮件箱避免错过通知

---

### [Eleventy 更名及其他变动，我对此并不感冒。——大卫·罗登](https://davidrhoden.com/notes/eleventy-is-changing-its-name-among-other-things-and-i-dont-love-it/)

**原文标题**: [Eleventy is changing its name, among other things, and I don't love it. - David Rhoden](https://davidrhoden.com/notes/eleventy-is-changing-its-name-among-other-things-and-i-dont-love-it/)

作者对 Eleventy 被 Font Awesome 收购并更名为“Build Awesome”一事表达了不满，认为新名称尴尬且背离了原有开发者社区的精神，同时担忧产品未来将过度迎合非技术用户而忽视核心开发者需求。

- 😠 作者强烈反对 Eleventy 更名为“Build Awesome”，认为新名称尴尬且不愿使用
- 🏢 Eleventy 被 Font Awesome 收购，将推出付费 Pro 版并提供可视化协作编辑工具
- 👥 引用开发者 Brennan Kenneth Brown 的观点，指出增加非程序员工具可能破坏开发体验
- 💸 作者认为此次变更主要是为了商业化盈利，而非服务现有开发者社区
- 🔧 批评静态站点生成器添加 CMS 功能是徒劳的，因为目标用户更偏好本地开发环境
- 🚪 担心产品未来将过度迎合终端客户而忽视核心开发者，这原本应是开发者的职责

---

### [Eleventy 的终结 · brennan.day](https://brennan.day/the-end-of-eleventy/)

**原文标题**: [The End of Eleventy · brennan.day](https://brennan.day/the-end-of-eleventy/)

文章探讨了静态网站生成器 Eleventy（11ty）被 Font Awesome 公司通过 Kickstarter 项目“Build Awesome”商业化重品牌的事件，作者作为 11ty 的长期用户和贡献者，对此举表示担忧。文章回顾了静态网站生成器的发展历史、11ty 的起源与特点，以及过去类似商业化尝试（如 Gatsby、Stackbit）的失败案例。作者认为，试图向不关心技术细节的非技术用户推销此类工具，而忽视现有开发者社区的需求，是本末倒置且难以成功的。文章最后提及了 11ty 的社区反应和已故开发者 James Williamson 的贡献，强调开源项目可持续性与商业化之间的内在矛盾。

- 🚨 Font Awesome 通过 Kickstarter 将开源静态网站生成器 Eleventy 重品牌为“Build Awesome”，旨在商业化，但忽视了核心开发者社区的需求。
- 📜 静态网站生成器（SSG）如 Jekyll、Hugo、Gatsby 和 Eleventy，通过模板和 Markdown 生成高效、安全的静态网站，避免了动态 CMS 的复杂性。
- ⚙️ Eleventy 由 Zach Leatherman 创建，以灵活、支持多模板引擎、不强制使用客户端 JavaScript 框架而受欢迎，被 NASA、Google 等机构使用。
- 💸 过去类似商业化尝试（如 Gatsby Cloud、Stackbit）因无法实现快速增长而失败，或被 Netlify 等公司收购后关闭，显示 SSG 商业化困难。
- 🧑‍💻 作者指出，真正使用静态网站生成器的开发者更喜欢免费本地工具（如 IDE 和终端），而非商业化产品，因此 Build Awesome 可能无法解决根本问题。
- 🌐 文章批评商业化公司忽视 IndieWeb 等独立社区，导致产品脱离实际用户，变得企业化、资本主义化，损害了开源精神。
- 💡 作者以自己的项目 Berry House 为例，说明通过低价或免费服务帮助非营利组织和边缘群体建立静态网站，是更可持续的模式。
- 😔 社区反应复杂，许多开发者对重品牌表示担忧，认为这可能使 Eleventy 失去原有的简洁性和社区驱动特性，甚至导致项目消亡。
- 🦝 文章缅怀已故开发者 James Williamson 及其对 Eleventy 社区的无私贡献，强调开源项目中的精神遗产比商业化更重要。

---

### [再见，Eleventy：Juha-Matti Santala](https://hamatti.org/posts/au-revoir-eleventy/)

**原文标题**: [
      Au revoir, Eleventy : Juha-Matti Santala
    ](https://hamatti.org/posts/au-revoir-eleventy/)

作者自 2018 年起使用静态网站生成器 Eleventy，对其简洁性和可控性极为满意，并基于它构建了数十个网站。然而，随着 Eleventy 被 Font Awesome 收购并更名为 Build Awesome，作者认为其发展方向变得商业化且偏离了自己的兴趣，因此决定停止使用。作者计划将当前版本固定保存，以便未来继续使用，并感谢开发者和社区的支持，同时邀请读者就此事进行深入交流。

- 🛠️ 作者自 2018 年开始使用 Eleventy，欣赏其简洁性和完全可控的设计，并基于它构建了许多网站。
- 🔄 Eleventy 被 Font Awesome 收购并更名为 Build Awesome，作者认为新方向过于商业化且不符合个人需求。
- 🏁 作者决定停止使用 Eleventy，但会保存当前版本以便未来继续使用。
- 🙏 作者感谢 Eleventy 的开发者和社区，理解项目寻求可持续资金的需求。
- 💌 作者邀请读者通过电子邮件分享对此事的看法，希望进行更深入的讨论。

---

### [构建新版 Flash——比尔著](https://bill.newgrounds.com/news/post/1607118)

**原文标题**: [Building a new Flash - by Bill](https://bill.newgrounds.com/news/post/1607118)

一位名为 Bill 的开发者正在构建一个名为 FlashSuccessor 的全新 2D 动画创作工具，旨在成为现代版的 Flash。该工具兼容 Linux、Mac 和 PC，并支持导入旧的.fla 文件进行编辑。项目目前处于积极开发阶段，具备完整的动画制作功能，并寻求通过 Patreon 获得支持以组建团队。

- 🛠️ **核心功能**：完整的 2D 动画创作环境，包括时间轴、绘图工具、符号库、补间动画和脚本支持，使用 C#、Avalonia 和 SkiaSharp 构建。
- 🔄 **兼容性**：支持导入和编辑 Adobe Flash的.fla/XFL文件，并计划通过转译器将ActionScript转换为C#以保持脚本功能。
- 🎨 **绘图与动画**：提供矢量绘图引擎（支持五种绘画模式）、形状补间、符号系统（图形、影片剪辑、按钮）以及多层时间轴动画。
- 💾 **导入导出**：支持导入.fla 文件，并可导出为 SWF 格式或 HTML5/Canvas，便于内容发布和播放。
- 📜 **脚本与自动化**：内置基于Roslyn的C#脚本引擎，支持创作时脚本和运行时帧脚本，提供丰富的API用于控制和扩展。
- 🔊 **音频编辑**：集成音频编辑器，支持波形显示、剪辑和与时间轴同步的音频播放预览。
- 🖥️ **用户界面**：采用可停靠面板、浮动窗口和多标签文档设计，提供类似专业软件的用户体验。
- 🌍 **跨平台**：工具兼容 Windows、Mac 和 Linux 系统，注重多平台支持。
- 🤝 **社区与支持**：开发者通过 Patreon 寻求资助，以组建团队加速开发，并在 Newgrounds 上更新项目进展。

---

### [关于 Flash 的思考 - 苹果](https://web.archive.org/web/20170615060422/https://www.apple.com/hotnews/thoughts-on-flash/)

**原文标题**: [Thoughts on Flash - Apple](https://web.archive.org/web/20170615060422/https://www.apple.com/hotnews/thoughts-on-flash/)

苹果与 Adobe 曾有过紧密合作，共同开创了桌面出版时代，但如今两家公司已渐行渐远。苹果决定不在 iPhone、iPod 和 iPad 上支持 Flash，主要基于技术层面的考量，而非商业竞争。Flash 是封闭的专有系统，而苹果倡导开放的 Web 标准如 HTML5。Flash 在移动设备上存在安全、性能、电池续航及触控兼容性等问题，且其跨平台开发工具会限制开发者利用苹果平台的创新功能。苹果认为，移动时代的低功耗设备、触控界面和开放网络标准更适合 HTML5 等新技术，而 Flash 已逐渐不再必要。

- 💼 苹果与 Adobe 曾有长期合作，但如今合作领域有限  
- 🔒 Flash 是封闭的专有系统，而苹果支持 HTML5 等开放标准  
- 🌐 苹果移动设备可通过 H.264 格式访问大部分网络视频，无需 Flash  
- ⚠️ Flash 存在安全隐患、性能不稳定且导致 Mac 崩溃  
- 🔋 Flash 视频解码耗电高，而 H.264 硬件解码可延长电池续航  
- 👆 Flash 基于鼠标设计，不兼容触控设备的交互方式  
- 🛠️ 第三方跨平台工具如 Flash 会限制开发者利用苹果平台的创新功能  
- 📱 苹果 App Store 已有大量应用和游戏，无需依赖 Flash  
- 🚀 苹果倡导开放标准，推动 HTML5 在移动设备上的发展

---

### [Mozilla 正进行 Firefox 重大重新设计，这是它的新面貌 - Neowin](https://www.neowin.net/news/mozilla-is-working-on-a-big-firefox-redesign-here-is-what-it-looks-like/)

**原文标题**: [Mozilla is working on a big Firefox redesign, here is what it looks like - Neowin](https://www.neowin.net/news/mozilla-is-working-on-a-big-firefox-redesign-here-is-what-it-looks-like/)

D-Link Nuclias Connect AX3000 Wi-Fi 6 接入点目前在亚马逊上以半价优惠促销。

- 📡 支持 Wi-Fi 6 技术，提供更快的无线网络速度和更高的连接效率  
- 💰 当前享受 50% 折扣，促销活动正在进行中  
- 🛒 在亚马逊平台独家销售，限时优惠  
- ⏱️ 促销信息发布于 57 分钟前，建议尽快购买

---

### [PWA 支持 — pwa.support](https://pwa.support/pwa-support.html)

**原文标题**: [PWA Support â pwa.support](https://pwa.support/pwa-support.html)

PWA（渐进式网络应用）的支持情况因操作系统和浏览器而异，其中 Chromium 内核浏览器在 Windows 上支持最全面，macOS 的 Safari 在 Sonoma 系统中已支持安装，而 Firefox 在所有桌面平台均不支持 PWA 安装。Linux 的支持则取决于桌面环境。本文通过六个维度（安装便捷性、启动体验、应用切换、链接捕获、推送通知、外部链接处理）评估了不同平台组合下的 PWA 体验，数据截至 2026 年 3 月 9 日。

- 🌐 **平台支持差异**：Chromium 浏览器在 Windows 上支持最全面；macOS Safari 已支持安装；Firefox 桌面版全平台不支持安装；Linux 支持依赖桌面环境
- 📱 **iOS 体验**：所有浏览器安装流程均随系统更新变化且不易发现；外部链接会在应用内浏览器打开而非系统浏览器
- 🤖 **Android 数据**：文中未提供具体评估结果（作者标注部分项目尚未测试）
- 🍎 **macOS 表现**：Chrome/Safari/Edge 安装便捷；推送通知支持不全（Chrome/Edge 通知点击后仅打开浏览器而非 PWA）
- 🪟 **Windows 特性**：Chrome/Edge 安装体验良好；推送通知存在缺陷（Chrome 无法接收，Edge 点击后不打开 PWA）
- 🐧 **Linux 特殊性**：Gnome/Wayland 组合可能导致图标显示异常；链接捕获需通过浏览器二次跳转
- 🔬 **评估方法论**：从安装引导、启动方式、应用切换、链接跳转、通知响应、外部链接处理六个维度对比原生应用体验
- ⚠️ **普遍局限**：多数平台在链接捕获和推送通知方面支持不完整；外部链接常在本窗口打开而非系统浏览器

---

### [Chrome 146 新功能  |  博客  |  Chrome 开发者](https://developer.chrome.com/blog/new-in-chrome-146?hl=en)

**原文标题**: [New in Chrome 146  |  Blog  |  Chrome for Developers](https://developer.chrome.com/blog/new-in-chrome-146?hl=en)

Chrome 146 版本现已推出，本次更新引入了多项关键功能，旨在提升网页开发的交互性、安全性与组件管理效率。

- 🎬 **滚动触发动画**：新增通过滚动位置控制 CSS 动画的功能，如播放、暂停和重置，使交互效果更易实现。
- 🧩 **作用域自定义元素注册表**：允许在页面内为同一标签名定义多个自定义元素，有效避免来自不同库的组件名称冲突。
- 🛡️ **Sanitizer API**：提供清理用户输入 HTML 内容的方法，移除可能执行脚本的部分，帮助开发者更轻松地构建防 XSS 攻击的网页应用。
- 📚 **更多资源**：开发者可查阅完整的发布说明、DevTools 更新及 Chrome 状态页面，以获取全部变更详情。

---

### [DevTools（Chrome 146）新功能  | 博客  | Chrome 开发者](https://developer.chrome.com/blog/new-in-devtools-146?hl=en)

**原文标题**: [What's new in DevTools (Chrome 146)  |  Blog  |  Chrome for Developers](https://developer.chrome.com/blog/new-in-devtools-146?hl=en)

Chrome 146 开发者工具更新，主要增强了样式表调试、控制台体验和隐私调试流程，并包含多项功能改进与无障碍优化。

- 🛠️ **DevTools MCP 服务器更新至 0.19.0**：新增集成 Lighthouse 审计、Slim 模式、针对可访问性和 LCP 的调试技能，并扩展了浏览器上下文隔离和屏幕录制等工具能力。
- 💾 **控制台历史编辑内容保留**：解决了长期存在的痛点，现在在命令历史中导航时，已编辑的内容不会丢失。
- 🧩 **增强对 Adopted Style Sheets 的支持**：在 Elements 面板中，Adopted Style Sheets 现在被分组在专用节点下，可直接检查和编辑，便于调试 Web Components 和现代 CSS 架构。
- 📐 **网格编辑器支持密集布局算法**：在 Styles 面板的 Grid Editor 中，现在可以方便地切换 `grid-auto-flow` 的 `dense` 打包模式。
- 🔒 **简化的隐私调试流程**：原“隐私与安全”面板更名为“安全”，隐私相关问题（如第三方 Cookie）现直接在控制台中报告，无需切换面板。
- 🐛 **其他亮点与无障碍改进**：包括 Sources 面板的堆栈跟踪架构大修、Network 面板的发起者弹出框改进，以及 Recorder、Application 面板等多处屏幕阅读器支持和焦点可见性优化。

---

### [Video.js | 开源视频播放器](https://videojs.org/)

**原文标题**: [Video.js | Open Source Video Player](https://videojs.org/)

本文介绍了 Video.js 10，这是一个完全重写的现代网页视频播放器，它通过模块化架构和独立的 UI 组件提供了高度可定制性，同时显著提升了性能。

- 🎬 **模块化架构**：Video.js 10 采用全新架构，UI 与媒体渲染器分离，每个组件独立并通过开放 API 协作，支持树摇和代码分割。
- ⚙️ **高度可定制**：开发者可以完全控制播放器的各个组件，包括自定义错误对话框、控制按钮和皮肤样式，实现个性化设计。
- 📦 **轻量高效**：相比旧版本，Video.js 10 的初始加载时间大幅缩短（从 3.96 秒降至 0.75 秒），文件大小从 200kB 减少到 38kB，显著提升用户体验。
- 🔧 **现代化开发**：专为现代 JavaScript 打包工具设计，提供 React 组件库和完整的 CSS 样式系统，支持响应式设计和无障碍访问。
- 🚀 **开发路线图**：包含技术预览（2025 年 10 月）、测试版（2026 年 3 月）、正式版（2026 年中）和功能完善（2026 年底）四个阶段。
- 🤝 **企业支持**：由 Mux 作为企业赞助商领导开发，提供 CDN、设备测试和静态托管等基础设施支持。

---

### [Video.js v10 Beta：你好，世界（再次）| 博客 | Video.js | 开源视频播放器](https://videojs.org/blog/videojs-v10-beta-hello-world-again)

**原文标题**: [Video.js v10 Beta: Hello, World (again) | Blog | Video.js | Open Source Video Player](https://videojs.org/blog/videojs-v10-beta-hello-world-again)

Video.js v10 Beta 是一次从零开始的重写，由多个开源项目团队合作完成，旨在通过大幅减小文件体积、提供现代化开发体验、支持深度定制以及优化 AI 开发体验，为开发者提供更高效、灵活的网页视频播放解决方案。

- 🎉 Video.js v10 Beta 发布，由多个开源视频项目团队合作重写，支持数十亿月播放量
- 📦 默认包体积减少 88%，通过模块化架构和按需加载显著优化文件大小
- ⚙️ 提供一流的 React、TypeScript 和 Tailwind 支持，允许基于现代开发模式深度定制
- 🎨 包含精心设计的默认皮肤，提供美观且高性能的播放体验
- 🤖 优化代码库和文档结构，提升 AI 代理开发视频播放器的效率
- 🚀 引入 SPF（流处理框架），为简单自适应流媒体用例大幅减小引擎体积
- 🧩 采用可组合架构，允许开发者按需选择功能，移除未使用的代码
- 🎛️ 提供预设配置，针对视频、音频和背景视频等常见用例优化开箱即用体验
- 🔮 关注 AI 开发体验，提供更少抽象的组件和优化文档，支持 AI 代理高效构建
- 🧪 目前处于测试阶段，API 尚未完全稳定，欢迎开发者反馈和测试

---

### [z-index 的用途 | CSS-Tricks](https://css-tricks.com/the-value-of-z-index/)

**原文标题**: [The Value of z-index | CSS-Tricks](https://css-tricks.com/the-value-of-z-index/)

本文探讨了在大型项目中管理 `z-index` 属性的挑战，并提出了通过 CSS 变量（tokens）系统化管理的解决方案，以避免随意使用“魔法数字”导致的维护困难和冲突。

- 🧩 `z-index` 是控制网页元素堆叠顺序的关键属性，常用于模态框、提示框等组件
- 🚨 大型项目中常出现随意使用高数值（如 `10001`）的“魔法数字”，导致代码难以维护和调试
- 🔍 堆叠上下文（Stacking Context）决定了 `z-index` 的有效范围，不同上下文中的数值无法直接比较
- 💡 最大 `z-index` 值为 2147483647（32 位有符号整数上限），超出将被浏览器限制
- 🏗️ 解决方案：使用 CSS 变量定义全局层级 token（如 `--z-toast: 100`），实现集中管理
- 🔄 新增元素时只需插入新 token 并调整数值，无需修改现有组件
- 📐 使用 `calc()` 建立元素间的相对层级关系（如背景始终在覆盖层下一级）
- 🧠 引入局部 token（`--z-top`/`--z-bottom`）管理组件内部堆叠，避免与全局层级混淆
- 🛠️ 通用组件（如工具提示）使用局部 token 即可适应不同上下文
- ⚡ 合理使用负值实现内部装饰效果（如背景图案）
- 📜 黄金规则：禁用魔法数字、强制使用 token、优先检查堆叠上下文而非数值
- 🤖 推荐使用 `z-index-token-enforcer` 等工具自动化检查，确保系统规范执行

---

### [锚点定位的大陷阱——前端大师博客](https://frontendmasters.com/blog/the-big-gotcha-of-anchor-positioning/)

**原文标题**: [The Big Gotcha of Anchor Positioning – Frontend Masters Blog](https://frontendmasters.com/blog/the-big-gotcha-of-anchor-positioning/)

CSS 锚点定位功能允许元素相对于其他元素定位，但存在一个关键限制：锚点元素必须在布局上先于被定位元素完成，否则定位会失效。

- 🚨 锚点元素必须在其关联定位元素之前完全布局完成，否则定位将失败
- 🔧 建议将锚点与定位元素设为兄弟节点，并将锚点置于 DOM 首位以确保兼容性
- 🧩 若锚点使用非默认定位（如 absolute），需特别注意 DOM 顺序和包含块关系
- 📚 可使用 anchor-tool 辅助理解定位范围，并参考 IMCB（插入修改包含块）概念调整对齐
- ⚠️ 当前规范可能导致意外错误，开发者需额外排查此类 CSS 新问题

---

### [TimescaleDB — 顶尖时序数据库 | 泰格数据](https://www.tigerdata.com/timescaledb?utm_source=cooperpress&utm_medium=referral&utm_campaign=frontend-focus-newsletter)

**原文标题**: [TimescaleDB — The #1 Time-Series Database | Tiger Data](https://www.tigerdata.com/timescaledb?utm_source=cooperpress&utm_medium=referral&utm_campaign=frontend-focus-newsletter)

TimescaleDB 是一个基于 PostgreSQL 构建的开源时序数据库，专为处理传感器、链上和客户数据而设计，提供实时分析、高效压缩和自动管理功能，适用于初创公司和企业。

- 🚀 核心功能：自动分区（Hypertables）、行列混合存储、高达 95% 的数据压缩、增量物化视图和自动化管理
- ⏱️ 时序分析：提供约 200 个原生 SQL 函数（Hyperfunctions），支持时间加权平均、插值和部分聚合等高级分析
- ☁️ 云平台兼容：100% PostgreSQL 兼容，支持弹性扩展，适用于 Crypto 和能源科技等行业
- 🛠️ 开源社区：拥有 22,000+ GitHub Stars 和 12,000+ Slack 成员，支持 Helm 快速部署
- 📈 客户案例：被 Cloudflare、Replicated 和 orca.so 等企业采用，平衡了性能与 PostgreSQL 的简易性
- 🆓 入门选项：提供免费试用和开源下载，帮助企业快速实现毫秒级数十亿行数据查询

---

### [SpeedCurve | 多快才算够快？以实用魔法视角重新思考网页性能](https://www.speedcurve.com/blog/fast/)

**原文标题**: [SpeedCurve | How fast is fast enough? Rethinking web performance in pragmagical terms](https://www.speedcurve.com/blog/fast/)

在数字世界中，流畅的用户体验如同礼物般珍贵。"足够快"不仅是提升转化率，更是创造无缝、无摩擦且近乎隐形的体验。本文探讨了如何超越传统性能指标，结合业务实用性与用户愉悦感，实现"实用魔法"般的性能目标。

- 🎯 "足够快"没有统一标准，需根据具体网站和受众定制性能阈值
- 🚀 极速体验（如 100 毫秒内响应）能消除认知摩擦，创造"魔法般"的流畅感
- 📊 业务指标存在"性能高原"，仅满足基本要求可能错失增长机会
- 🔍 谷歌核心网页指标是起点而非终点，需结合自身用户数据分析
- 📈 速度不仅影响即时转化，还塑造用户记忆、信任和回访行为
- 🧠 指标不等于感受，需结合可用性研究理解真实用户体验
- ⏱️ 参与型任务和生产型任务对延迟的容忍度截然不同
- 🔗 旅程级性能至关重要，单个缓慢环节可能破坏整个流程的动量
- ✨ 应超越"可接受"标准，追求流畅、轻松、直观的体验
- 🤝 实用魔法性能兼顾业务目标与用户体验，在现实中追求卓越

---

### [使用原生 JavaScript 构建异步页面过渡效果 | Codrops](https://tympanus.net/codrops/2026/02/26/building-async-page-transitions-in-vanilla-javascript/)

**原文标题**: [Building Async Page Transitions in Vanilla JavaScript | Codrops](https://tympanus.net/codrops/2026/02/26/building-async-page-transitions-in-vanilla-javascript/)

本文介绍了如何使用原生 JavaScript、GSAP 和 Vite 构建一个轻量级的单页应用（SPA）路由系统，实现异步页面过渡效果，无需依赖任何前端框架。通过克隆页面容器并同时动画化当前页面和下一页面的方式，实现真正的交叉淡入淡出过渡效果。

- 🛠️ **项目设置**：使用 Vite 创建项目，选择 Vanilla 模板，清理初始文件，建立基本的项目结构。
- 📄 **HTML 结构**：通过`data-transition`属性定义页面容器和包装器，实现页面过渡时的 DOM 管理。
- 📂 **页面模块化**：将每个页面作为独立模块，包含 HTML 和 JavaScript 文件，支持动态导入和初始化函数。
- 🧭 **路由系统**：创建自定义路由器，拦截链接点击，使用 History API 管理导航，并支持动态加载页面模块。
- 🎬 **过渡引擎**：利用 GSAP 实现动画时间线，通过克隆容器和同时动画化两个页面，实现平滑的交叉淡入淡出效果。
- 🔄 **动画细节**：添加进入动画，如标题的滑动效果，增强用户体验和视觉深度。
- 🚀 **扩展功能**：讨论了进一步优化方向，如页面生命周期钩子、中断过渡、预加载和元标签更新等。

---

### [地理位置元素的强制可访问性——前端大师博客](https://frontendmasters.com/blog/the-enforced-accessibility-of-the-geolocation-element/)

**原文标题**: [The Enforced Accessibility of the Geolocation Element – Frontend Masters Blog](https://frontendmasters.com/blog/the-enforced-accessibility-of-the-geolocation-element/)

HTML 新增了`<geolocation>`元素，这是一个具有强制可访问性设计的按钮，用于获取用户地理位置。它由 Chrome 率先实现，目前在其他浏览器中的支持时间尚不确定。该元素在安全性和防欺骗方面有严格限制，包括固定的图标和文本、部分 CSS 样式被禁用或受限，以及违反某些样式规则时会自动禁用功能。

- 🗺️ `<geolocation>`是 HTML 新增元素，外观为带地图图标和“使用位置”文本的按钮，设计固定不可更改。
- 🔒 点击按钮会根据权限状态触发地理位置请求、提示授权或提醒已拒绝，并允许从拒绝状态恢复授权。
- 🌐 支持渐进增强，可通过内部放置`<button>`或使用 polyfill 实现，且文本会根据 DOM 的`lang`属性自动本地化。
- 🚫 部分 CSS 样式被完全禁用（如`transform`、`opacity`），部分样式数值受限（如`letter-spacing`、`font-size`有最小/最大值）。
- ⚠️ 某些 CSS 允许应用但会导致按钮功能失效（如颜色对比度不足），且不会在控制台报错，仅在 DevTools 的“问题”区域提示。
- 🛡️ 严格的可访问性规则主要出于安全考虑，旨在防止用户被诱导意外共享地理位置。

---

### [一个让数字瞬间更美观的 CSS 属性 — Amit Merchant — 关于 PHP、JavaScript 等技术的博客](https://www.amitmerchant.com/one-css-property-that-makes-numbers-look-instantly-better/)

**原文标题**: [One CSS Property That Makes Numbers Look Instantly Better — Amit Merchant — A blog on PHP, JavaScript, and more](https://www.amitmerchant.com/one-css-property-that-makes-numbers-look-instantly-better/)

在网页设计中，使用`font-variant-numeric: tabular-nums`这一 CSS 属性可以解决比例字体中数字宽度不一导致的视觉错位问题，使数字在表格、计时器或仪表盘等场景中显示更整齐、稳定，提升用户体验。

- 🕰️ 比例字体中数字宽度不同，在表格或动态变化时易造成视觉错位和布局偏移
- 🔧 使用`font-variant-numeric: tabular-nums`可强制数字等宽显示，即使是在比例字体中
- 📊 适用于时钟、财务表格、分析仪表盘、计分板等需要数字对齐的场景
- 🌐 该属性兼容所有现代浏览器，可放心使用
- 🎨 作者提供了 CodePen 演示，并推荐参考 MDN 文档了解更多细节

---

### [CSS 中的原生随机值](https://alvaromontoro.com/blog/68092/native-random-values-in-css)

**原文标题**: [Native Random Values in CSS](https://alvaromontoro.com/blog/68092/native-random-values-in-css)

CSS 工作组发布了 Values and Units Module Level 5，引入了原生机制，仅使用 CSS 即可生成随机内容。这标志着 CSS 从确定性语言向支持随机性的转变，目前仅 Safari 部分支持。

- 🎲 CSS 新增 `random()` 函数，可在指定范围内生成随机值，支持最小值和最大值参数，并可选择增量步长以控制精度。
- 🔗 通过共享选项（如虚线标识符、`element-shared` 关键字或 `fixed` 参数），可在属性、元素或全局范围内共享随机值，确保一致性。
- 📝 `random-item()` 函数从给定列表中随机选择一个值，适用于离散属性，且共享变量为必需参数，以保持结果关联性。
- 🌐 当前浏览器支持有限，仅 Safari 26.2 版本部分支持 `random()`，而 `random-item()` 尚未得到广泛实现，需注意生产环境中的兼容性。
- 💡 这些函数将随机性处理移至 CSS 布局层，减少对 JavaScript 的依赖，适用于颜色、旋转或间距等视觉增强场景，但需考虑缓存和性能影响。

---

### [NoJS 3 - Flappy Bird 的黎明。使用纯 HTML 和 CSS 制作 Flappy Bird 克隆版，无需 JavaScript](https://blog.scottlogic.com/2026/03/09/noJS-3-flappy-bird.html)

**原文标题**: [NoJS 3 - The dawn of Flappy Bird. Making a Flappy Bird clone using pure HTML and CSS, no JavaScript](https://blog.scottlogic.com/2026/03/09/noJS-3-flappy-bird.html)

本文介绍了仅使用 HTML 和 CSS（无需 JavaScript）制作《Flappy Bird》游戏克隆版的方法，展示了现代 CSS 技术的强大功能。

- 🐦 通过纯 HTML 和 CSS 实现《Flappy Bird》游戏核心玩法，无需 JavaScript
- 🎮 利用 CSS 动画和关键帧控制小鸟飞行与管道移动
- 🚀 采用 CSS 变量和 calc() 函数实现游戏动态计算
- 🎯 使用:checked 伪类和相邻兄弟选择器处理游戏交互逻辑
- 📱 完全响应式设计，适配各种屏幕尺寸
- ⚡ 展示现代 CSS 已能实现传统需 JavaScript 完成的复杂交互
- 🔧 提供完整代码示例和实现原理详解

---

### [使用 requestAnimationFrame 提升动画性能 | DebugBear](https://www.debugbear.com/blog/requestanimationframe)

**原文标题**: [Improve Animation Performance With requestAnimationFrame | DebugBear](https://www.debugbear.com/blog/requestanimationframe)

本文介绍了如何使用`requestAnimationFrame`优化动画性能，对比了其与`setTimeout`的差异，并探讨了在 React 和 Vue 中的具体应用，以及如何通过合理调度提升交互响应速度。

- 🎯 `requestAnimationFrame`是专为视觉更新设计的浏览器 API，确保回调在浏览器下一次重绘前执行，实现更流畅的动画效果
- ⏱️ 与`setTimeout`相比，`requestAnimationFrame`能同步显示刷新率，自动暂停于后台标签页，避免帧率不稳定和掉帧问题
- ⚛️ 在 React 中，可通过`useEffect`或自定义 Hook 使用`requestAnimationFrame`，注意在组件卸载时取消动画帧请求
- 🖼️ 在 Vue 中，可利用 VueUse 库的`useRafFn`组合式函数，自动处理清理、暂停/恢复和响应式集成
- 🚀 采用`rAF → setTimeout`模式可确保在交互后立即更新 UI，再将繁重任务推迟到下一帧执行，有效改善 INP 指标
- 🔄 其他调度 API 如`requestIdleCallback`适用于后台任务，`scheduler.yield`适合拆分繁重任务，而`Promise.then`则不适合用于渲染让步
- 📊 理解并合理运用`requestAnimationFrame`对优化 Core Web Vitals 至关重要，可借助 DebugBear 等工具监控性能指标变化

---

### [前端 OAuth 2.0 的攻防解析 • Philippe De Ryck • YOW! 2025 - YouTube](https://www.youtube.com/watch?v=oGktdQ45bTg)

**原文标题**: [Breaking & Securing OAuth 2.0 in Frontends • Philippe De Ryck • YOW! 2025 - YouTube](https://www.youtube.com/watch?v=oGktdQ45bTg)

该文本为 YouTube 网站底部的通用法律与信息链接列表，概述了其核心功能板块与用户政策。

- 📄 关于平台的基本信息与介绍
- 📢 新闻与媒体相关资源
- ©️ 版权声明与保护政策
- 📞 用户联系与反馈渠道
- 🧑‍🎨 内容创作者相关资源
- 💼 广告合作与商业推广
- 👨‍💻 开发者工具与 API 信息
- ⚖️ 服务条款与使用协议
- 🔒 隐私保护与数据政策
- 🛡️ 平台安全与内容规范
- ⚙️ 产品功能运作说明
- 🧪 新功能测试与更新
- 🏢 公司所有权与年份标识

---

### [我是如何将 Bluesky 点赞功能添加到我的 Astro 博客的](https://loige.co/how-i-added-bluesky-likes-to-my-astro-blog/)

**原文标题**: [How I added Bluesky likes to my Astro blog](https://loige.co/how-i-added-bluesky-likes-to-my-astro-blog/)

本文介绍了作者如何在 Astro 博客中集成 Bluesky 点赞功能，通过使用 Lea Verou 开发的 bluesky-likes Web 组件包，无需 API 密钥或服务器端代码即可展示点赞数和用户头像。

- 🛠️ 使用 bluesky-likes Web 组件包，无需服务器端代码或 API 密钥即可集成 Bluesky 点赞功能
- 📝 在 Astro 博客的内容配置中添加 bluesky_url 字段，用于关联每篇文章的 Bluesky 帖子链接
- 🧩 创建 BlueskyReactions.astro 组件，通过 CSS 自定义属性实现主题适配，并利用 esm.sh 加载脚本
- 🔗 在文章页面模板中条件渲染组件，仅当文章 frontmatter 包含 bluesky_url 时显示
- 🔍 使用 bsky CLI 工具匹配博客文章与 Bluesky 帖子，并通过 AI 辅助快速更新多篇文章的 frontmatter
- 🎨 组件支持深色/浅色主题自动适配，通过 CSS 自定义属性与博客设计无缝集成
- ⚡ 整个集成过程仅需修改少量代码：1 行配置、46 行组件代码和 3 行页面集成代码

---

### [HTML 演示框架 | reveal.js](https://revealjs.com/)

**原文标题**: [The HTML presentation framework | reveal.js](https://revealjs.com/)

reveal.js 是一个开源 HTML 演示框架，允许用户通过网页浏览器免费创建功能全面且美观的演示文稿。它基于开放网络技术，支持 CSS 样式调整、iframe 嵌入外部页面及 JavaScript API 自定义功能，并提供嵌套幻灯片、Markdown 支持、自动动画、PDF 导出、演讲者备注、LaTeX 公式和高亮代码等丰富特性。

- 🌐 开源 HTML 框架，免费创建网页演示文稿
- 🛠️ 基于开放网络技术，支持 CSS、iframe 和 JavaScript API 自定义
- ✨ 内置嵌套幻灯片、Markdown、自动动画、PDF 导出等多项功能
- ⚡ 快速入门，可通过安装指南或在线编辑器 Slides.com 轻松上手
- 👥 由@hakimel 主导开发，社区贡献支持，可通过 Slides.com 会员计划赞助项目

---

### [发布 6.0.0 版本 · hakimel/reveal.js · GitHub](https://github.com/hakimel/reveal.js/releases/tag/6.0.0)

**原文标题**: [Release 6.0.0 · hakimel/reveal.js · GitHub](https://github.com/hakimel/reveal.js/releases/tag/6.0.0)

reveal.js 发布了 6.0.0 版本，主要引入了官方的 React 封装包，并进行了多项重大变更、功能增强和问题修复。

- 🎉 **新增官方 React 封装**：推出了 `@revealjs/react` 包，允许使用 React 组件（如 `<Deck>`、`<Slide>`）构建演示文稿。
- ⚠️ **重大变更**：插件路径、ES 模块和 CSS 文件路径已更新，TypeScript 类型现内置，需参考升级指南进行迁移。
- 🛠️ **构建工具切换**：从 gulp 改为使用 Vite 进行构建和开发。
- 🎨 **功能增强**：新增仅演讲者视图显示控件的选项、改进视频自动播放处理、支持 MathJax 4、提升可访问性等。
- 🐛 **问题修复**：解决了 Android 和 iOS 上的视频播放问题、修复了主题字体缺失和 SCSS 语法警告等。
- 👥 **社区贡献**：此版本由 hakimel、tobi-or-not-tobi 和 Khlick 等多位贡献者共同完成。

---

### [Expo SDK 55 - 更新日志](https://expo.dev/changelog/sdk-55?utm_source=frontendfocus&utm_medium=referral&utm_campaign=35663643-SDK%2055&utm_content=SDK_55_changelog)

**原文标题**: [Expo SDK 55 - Expo Changelog](https://expo.dev/changelog/sdk-55?utm_source=frontendfocus&utm_medium=referral&utm_campaign=35663643-SDK%2055&utm_content=SDK_55_changelog)

Expo SDK 55 正式发布，包含 React Native 0.83 和 React 19.2，引入了多项重要更新与改进。

- 🚀 **SDK 55 发布**：包含 React Native 0.83 和 React 19.2，SDK 56 预计在第二季度发布。
- ⏳ **过渡期安排**：Expo Go 和应用商店项目暂时保持 SDK 54，建议迁移至开发构建。
- 🎨 **项目模板更新**：采用原生标签页 API，优化设计，引入 `/src` 文件夹结构。
- 🏗️ **弃用旧架构**：SDK 55 起不再支持旧架构，相关配置已移除。
- ⚡ **Hermes v1 可选**：带来性能提升和现代 JavaScript 功能支持，但会显著增加构建时间。
- 📦 **Hermes 字节码差分**：通过 EAS Update 和 `expo-updates` 优化更新下载大小，减少约 75% 的下载时间。
- 🤖 **AI 工具扩展**：Expo MCP 支持 CLI 操作和 EAS 查询，提供官方 AI 技能库。
- 🔗 **Brownfield 应用改进**：新增 `expo-brownfield` 包，支持集成和隔离两种开发模式。
- 🧭 **Expo Router 增强**：新增 Colors API、Apple Zoom 过渡、Stack.Toolbar API 等原生功能。
- 🎭 **Expo UI 进展**：Jetpack Compose 升级至 Beta，SwiftUI 组件 API 更贴近原生，新增多项组件和修饰符。
- 📦 **包版本统一**：所有 Expo SDK 包版本与 SDK 主版本号对齐，便于识别兼容性。
- 🛠️ **Expo Modules Core 更新**：支持 Swift 6 语言模式、ArrayBuffer 和静态函数。
- 🔧 **Expo CLI 改进**：优化开发服务器启动界面，支持环境文件和动态应用配置加载。
- 📱 **实验性功能**：新增 `expo-widgets`（iOS 小组件）、`expo-blur` Android 稳定版、`expo-sharing` 接收共享数据支持。
- 🌐 **其他亮点**：Expo Go 界面重构，Expo Web 支持 SSR 和数据加载器，多个模块（如 `expo-audio`、`expo-sqlite`）功能增强。
- ⚠️ **废弃与破坏性变更**：移除旧配置字段，调整工具链，更新最低 Node.js 和 Xcode 版本要求。
- 🔄 **升级指南**：提供升级步骤，建议使用升级技能辅助，注意处理破坏性变更和依赖更新。

---

### [未找到标题](https://inspira-ui.com/)

**原文标题**: [No title found](https://inspira-ui.com/)

本文介绍了人工智能在医疗领域的应用现状与前景，重点探讨了其在疾病诊断、治疗方案优化及医疗管理效率提升方面的作用，同时简要提及了相关的技术挑战和伦理考量。

- 🤖 AI 辅助诊断系统能通过分析医学影像快速识别病灶，提高早期疾病检出率
- 💊 基于机器学习的个性化治疗方案可结合患者数据优化用药与治疗路径
- ⚡ 智能医疗管理平台自动化处理行政流程，显著减轻医护人员行政负担
- 🧬 基因组学与 AI 结合助力精准医疗发展，加速靶向药物研发进程
- ⚖️ 数据隐私保护与算法透明度是目前医疗 AI 推广面临的主要伦理挑战

---

### [所有组件 - Inspira UI](https://inspira-ui.com/docs/en/components)

**原文标题**: [All Components - Inspira UI](https://inspira-ui.com/docs/en/components)

Inspira UI 组件库发布了两个新组件，并更新了多个现有组件，目前共提供 128 个组件，涵盖背景、按钮、卡片、特效等多种类别。

- 🆕 **图像徽章**：一个可悬停以显示更多图像的徽章组件。
- 🆕 **刻度背景**：一种重复的对角线、水平或垂直线图案背景效果。
- ✨ **更新组件**：包括“坠落星星背景”、“Github 地球仪”、“图案背景”等多个组件获得了功能或样式更新。
- 📦 **组件总数**：当前库中总计有 128 个组件，覆盖了从基础 UI 元素到复杂动画特效的广泛需求。
- 🏷️ **分类清晰**：所有组件按类别（如背景、按钮、卡片等）和状态（全新、已更新）进行了组织，便于查找。

---

### [照片调色板](https://photopalettes.com/)

**原文标题**: [Photo Palettes](https://photopalettes.com/)

本文介绍了人工智能在医疗领域的应用现状与前景，重点探讨了其在疾病诊断、治疗方案优化及医疗管理效率提升方面的作用，同时简要提及了相关的技术挑战和伦理考量。

- 🤖 AI 辅助诊断系统能通过分析医学影像快速识别病灶，提高早期疾病检出率
- 💊 基于机器学习的个性化治疗方案可结合患者数据优化用药与治疗路径
- 📊 智能医疗管理系统自动化处理病历、排班等流程，减轻医护行政负担
- ⚠️ 数据隐私保护与算法透明度仍是医疗 AI 推广需要解决的关键问题
- 🔮 未来 AI 或与远程医疗、可穿戴设备结合，构建预防性健康管理生态

---

### [所有 SVG 图标 - 免费开源 SVG 矢量图标 | 所有 SVG 图标](https://allsvgicons.com/)

**原文标题**: [All SVG Icons - Free and Open Source SVG Vector Icons | All SVG Icons](https://allsvgicons.com/)

该网站提供超过 25 万个免费 SVG 图标，涵盖 220 多个图标库，支持多种格式下载和自定义，适用于各类设计开发项目。

- 🆓 提供超过 25 万个免费 SVG 图标，来自 220 多个精选图标库
- 🛠️ 支持自定义并下载为 PNG、SVG、JSX 和 Base64 等多种格式
- 📚 包含 Material Symbols、Font Awesome、Bootstrap Icons 等流行图标集
- 🧩 提供图标使用指南、库比较和博客文章等学习资源
- 🔗 网站还提供其他工具如 SVG 优化器、免费 Logo 制作和网站图标生成器

---

### [GitHub - privatenumber/minification-benchmarks: 🏃‍♂️🏃‍♀️🏃 JS 压缩性能基准测试：babel-minify、esbuild、terser、uglify-js、swc、google closure compiler、tdewolff/minify、oxc-minify · GitHub](https://github.com/privatenumber/minification-benchmarks)

**原文标题**: [GitHub - privatenumber/minification-benchmarks: 🏃‍♂️🏃‍♀️🏃 JS minification benchmarks: babel-minify, esbuild, terser, uglify-js, swc, google closure compiler, tdewolff/minify, oxc-minify · GitHub](https://github.com/privatenumber/minification-benchmarks)

该项目对多个 JavaScript 代码压缩工具进行了性能基准测试，旨在帮助开发者根据压缩效果和速度选择适合的工具。

- 📊 **项目目的**：通过基准测试比较不同 JavaScript 压缩工具的性能，帮助开发者选择最合适的工具，并促进工具间的竞争与改进。
- ⚙️ **测试方法**：每个压缩工具在独立进程中运行，设置 10 秒超时；验证压缩前后的代码完整性；采用最小化配置（禁用源映射和注释）进行对比。
- 📈 **评估指标**：综合考虑压缩后大小（Gzip 压缩）和压缩时间，通过加权评分进行排名，其中大小权重通常更高（85%），但极端慢速时会调整权重。
- 🏆 **测试结果**：在多个流行 JavaScript 库（如 React、jQuery、Vue 等）的测试中，不同工具表现各异；例如，@swc/core 在大型文件上表现平衡，oxc-minify 在速度上领先，而 uglify-js 在压缩率上优势明显。
- 🚀 **工具对比**：@swc/core 被评为综合最佳，因其在压缩率和速度间取得良好平衡；oxc-minify 在速度上突出；uglify-js 在压缩率上领先但速度较慢；部分工具如 babel-minify 和 tedivm/jshrink 因错误或超时被淘汰。
- 💡 **使用建议**：选择工具时应根据实际需求权衡压缩率、速度和兼容性；例如，注重网络传输性能可选@swc/core，追求极致压缩率可考虑 uglify-js，而需要快速迭代则推荐 oxc-minify 或@cminify/cminify-linux-x64。

---

### [GitHub - heyform/heyform: 开源表单构建器 · GitHub](https://github.com/heyform/heyform#readme)

**原文标题**: [GitHub - heyform/heyform: Open-Source Form Builder · GitHub](https://github.com/heyform/heyform#readme)

HeyForm 是一个开源的表单构建工具，允许用户无需编程技能即可创建互动式对话表单，用于调查、问卷、测验和投票。

- 📝 **功能丰富**：支持多种输入类型，包括文本、图片选择、日期选择和文件上传，并具备智能逻辑和强大的第三方集成能力。
- 🎨 **品牌定制**：提供可自定义的视觉主题和高级样式选项，允许用户通过自定义 CSS 深度匹配品牌形象。
- 📊 **数据分析**：内置详细的分析工具，可追踪完成率和流失率，并支持将结果导出为 CSV 格式。
- 🚀 **快速入门**：推荐使用官方托管服务，享受高可靠性、自动备份和安全维护，同时支持项目开发。
- 🏗️ **自托管选项**：提供自托管安装指南，允许用户在自有服务器上部署 HeyForm。
- 💻 **本地开发**：包含完整的本地开发设置说明，方便贡献者参与项目。
- 🤝 **社区支持**：通过 Discord 服务器和问题追踪系统提供帮助，并欢迎开源贡献。
- 📜 **开源许可**：项目采用 AGPL-3.0 许可证，确保开源合规性和透明度。

---

### [EXIF 元数据查看器 - 发现图像中的隐藏信息 | 免费浏览器扩展 | ternera](https://www.ternera.org/exif)

**原文标题**: [EXIF Metadata Viewer - Find Hidden Information in Images | Free Browser Extension | ternera](https://www.ternera.org/exif)

该文章介绍了一款名为 EXIF Metadata Viewer 的浏览器扩展，可直接在浏览器中查看图像内嵌的 EXIF 元数据，包括拍摄参数、位置和时间等信息，适用于摄影学习、隐私检查等多种用途。

- 📸 快速查看图像 EXIF 元数据，包括相机型号、光圈、快门速度等拍摄设置
- 🌍 可显示图像拍摄的地理位置（若包含 GPS 数据）
- ⏰ 提供图像拍摄的具体日期和时间信息
- 🔧 通过右键菜单直接使用，支持 Chrome 及 Chromium 内核浏览器
- 🛡️ 完全免费且不收集用户个人数据，尊重隐私保护
- 📱 适用于摄影师学习、隐私检查、数字取证和摄影爱好者等多种场景

---

### [非 HTML 内容](https://frontendfoc.us/open/732/*%7CUID%7C*?ipx=t)

**原文标题**: [Non-HTML content](https://frontendfoc.us/open/732/*%7CUID%7C*?ipx=t)

无法总结：非 HTML 内容。

---

