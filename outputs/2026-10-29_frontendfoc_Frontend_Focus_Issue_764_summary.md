### [Chrome 157 中的 HTML-in-Canvas：在 2D、WebGL 和 WebGPU 中实现交互式 DOM | 博客 | Chrome for Developers](https://developer.chrome.com/blog/html-in-canvas)

**原文标题**: [HTML-in-Canvas in Chrome 157: Interactive DOM inside 2D, WebGL, and WebGPU  |  Blog  |  Chrome for Developers](https://developer.chrome.com/blog/html-in-canvas)

Chrome 157 正式稳定发布 HTML-in-Canvas API，经过 origin trial 后上线。该 API 将可交互、可访问的 DOM 与高性能、像素级控制的 `<canvas>` 结合，支持在 2D、WebGL 和 WebGPU 中渲染 HTML 内容，兼顾浏览器能力与 GPU 加速图形。

- 🌉 **核心价值**：连接 DOM 的交互性与 canvas 的高性能渲染，避免在两者之间二选一。
- ⚖️ **解决痛点**：传统 canvas 缺少文本选择、复制粘贴、右键菜单、页面查找、翻译、自动填充和屏幕阅读器等能力；纯 HTML 又难以高效控制复杂 UI 性能。
- 🧩 **旧方案局限**：用 `fillText()` 绘制文本会导致可访问性和浏览器功能缺失；浮动 HTML 覆盖层则可能出现同步延迟、视觉撕裂、裁剪与层叠限制，以及逐帧更新性能开销。
- ✅ **关键优势**：canvas 内的 HTML 支持文本布局与样式、表单控件、选择复制右键、无障碍树、翻译、自动填充、页面查找、浏览器扩展和 DevTools 调试。
- 🔍 **额外能力**：渲染进 2D/3D 场景的 DOM 内容可被搜索引擎和 AI 代理索引，也可将包含实时 DOM 的 canvas 合成结果导出为图片或视频流。
- 🎯 **主要场景**：大型 canvas 应用、3D 场景与游戏/WebXR、媒体编辑与导出、着色器驱动的表现型 UI。
- 🚀 **快速上手**：为 canvas 设置 `content="drawable"`，将子元素标记为 `drawable`；2D 中使用 `drawElementImage()` 绘制，3D 中可通过 `updateElementGeometry()` 同步几何变换。
- 🛠️ **生态支持**：Three.js 提供实验性 `HTMLTexture`，PlayCanvas 支持 `setSource()`，Babylon.js 提供 `HtmlTexture`，PixiJS v8.19.0 支持 `HTMLSource`，另有 CanvasUI 组件库。
- 🧪 **兼容与回退**：上线前应检测 API 支持情况；不支持时可回退到浮动 HTML 覆盖层或 `three-html-render`、`html2canvas`、`dom-to-image` 等社区方案。
- 📚 **后续行动**：查阅完整文档、使用 Modern Web Guidance 升级编码助手、在 WICG GitHub 仓库反馈问题，并体验社区示例。

---

### [HTML-in-canvas：交互式内容与高性能图形交汇之处 - YouTube](https://www.youtube.com/watch?v=mB0eWkWubuk)

**原文标题**: [HTML-in-canvas: Where interactive content and high performance graphics meet - YouTube](https://www.youtube.com/watch?v=mB0eWkWubuk)

该内容主要是 YouTube 网站页脚中的导航链接与版权声明，未包含实质性文章正文。

- 📄 包含“关于、新闻、版权、联系我们”等基础信息入口。
- 👥 提供创作者、广告合作、开发者相关链接。
- 📜 列出服务条款、隐私、政策与安全等法律与政策入口。
- ⚙️ 包含 YouTube 运作方式与测试新功能入口。
- ©️ 版权声明显示为 © 2026 Google LLC。

---

### [为用户内容创建动态社交媒体卡片](https://blog.master.dev/what-should-you-put-on-a-dynamic-custom-social-media-card-image/)

**原文标题**: [Creating Dynamic Social Media Cards for User Content](https://blog.master.dev/what-should-you-put-on-a-dynamic-custom-social-media-card-image/)

本文讨论了如何为大量用户生成内容或电商页面设计“动态社交媒体卡片”：与其逐页手工设计，不如建立系统，用动态数据自动生成分享图。文章介绍了 Open Graph、Twitter Card 等 HTML 元标签以及链接展开（unfurl）机制，并比较了 Discord、Slack、iMessage、X 等平台展示差异。核心建议是：优先展示页面中最有趣、最具上下文价值的视觉内容，避免重复标题、描述和 URL，并控制文字量。

- 🧩 动态卡片适合 UGC、电商等页面数量过多、无法逐页手工设计的场景，应通过系统结合动态数据生成图片。
- 🎨 如果能为特定 URL 定制卡片，通常应定制：突出品牌、吸引力，并快速传达页面核心信息。
- 🏷️ 常见实现是在 HTML 中加入 `og:image`、`twitter:image`、`twitter:card` 等元标签，并配合标题、描述、favicon 等 SEO/分享信息。
- 🖼️ 可为社交分享图添加 `og:image:alt` 替代文本，以便更准确地描述图片内容。
- 🔗 链接在聊天或社交平台中会“展开”为卡片，但各平台展示规则不同，且可能随时变化，无法完全控制。
- 📱 文章对比了 Discord、Mastodon、Slack、Bluesky、iMessage、LinkedIn、Threads、WhatsApp、X 等平台在 URL、站点名、标题、描述、图片大小等方面的差异。
- 🧠 大图不必重复展示标题，因为多数 unfurl 已包含标题；重复标题很常见，但往往显得冗余。
- 🏢 站点名称、URL 和 favicon 通常已由平台展示，因此卡片图中不一定要重复；可考虑放 logo 强化品牌。
- 🚫 通常不建议在图中重复商品 URL 或完整描述，尤其是描述较长、层级较低时，容易造成文字过多。
- 📊 更有价值的是展示页面独特动态数据，如作者/头像、点赞、浏览量、评分、折扣、图表、波形、标签等。
- 🎮 也可让内容本身说话，例如 Steam 游戏图或 CodePen 截图；CodePen 每次保存都会截图并用作社交图。
- 🔍 动态数据可条件性展示：只有数据有趣时才显示，例如“精选 Pen”或较高互动数据，避免低值或零值尴尬。
- 📐 社交图通常按 1200×630 设计，但在 Slack 等平台可能显示为小方块，文字可读性有限，因此应少放文字。
- ⚙️ 平台规则差异明显：X 可能用 unfurl 替代链接，Bluesky 支持 `standard.site` 特殊按钮，Slack 管理员可永久关闭某域名展开。
- 🛠️ 可用 Next.js 内置方案、11ty/WordPress 插件、Cloudinary URL 参数等生成动态社交图片。
- ✅ 最终建议：展示页面最有趣的实际图片和上下文数据，避免过多文字，尤其避免重复元标签已有信息。

---

### [Meticulous AI - 无需编写测试的自动化前端测试](https://www.meticulous.ai/?utm_source=frontend_focus&utm_medium=newsletter&utm_campaign=26q3_3&utm_term=primary+content)

**原文标题**: [Meticulous AI - Automated Frontend Testing Without Writing Tests](https://www.meticulous.ai/?utm_source=frontend_focus&utm_medium=newsletter&utm_campaign=26q3_3&utm_term=primary+content)

Meticulous 是一款面向复杂代码库的自动化端到端测试工具，以零开发者维护、自动生成持续演进的测试套件为核心，通过录制真实用户交互并在合并前验证影响，帮助团队高速交付无回归代码。

- 🚀 自动、穷尽且确定性的验证，开发者几乎无需投入即可使用。
- 🎥 通过脚本标签记录本地、预发布和预览环境的真实交互，也可选记录生产环境以扩大覆盖。
- 🤖 AI 根据交互覆盖的代码分支自动生成并持续演进视觉端到端测试，覆盖用户流程和边缘场景。
- 🔍 提交拉取请求即可在合并前查看改动对用户工作流的影响。
- 🧪 默认回放已录制的后端响应，测试无副作用、减少误报，无需特殊测试账号或模拟数据。
- ♻️ 测试随应用自动增删更新，无需编写、修复或维护测试。
- ⚡ 基于 Chromium 层级的确定性调度引擎，从底层消除不稳定测试并实现极快执行。
- 📈 测试在计算集群中高度并行化，可在约 120 秒内测试数千个界面。
- 🔌 支持 NextJS、React、Vue、Angular、Nuxt、SvelteKit，并可与现有测试套件互补或替代。
- 🏢 已被 100 多家组织采用，包括 Dropbox、Notion、Engine 等，用于提升回归防护与开发速度。

---

### [DeadTag：被遗忘的网站标签如何成为 iPhone 间谍软件的投放网络](https://blog.report-uri.com/deadtag-how-forgotten-website-tags-became-a-delivery-network-for-iphone-spyware/)

**原文标题**: [DeadTag: How Forgotten Website Tags Became a Delivery Network for iPhone Spyware](https://blog.report-uri.com/deadtag-how-forgotten-website-tags-became-a-delivery-network-for-iphone-spyware/)

Report URI 与 iVerify 联合研究发现，名为 DeadTag 的大规模恶意流量生态通过收购已过期的第三方网站标签域名，向数千个网站注入恶意脚本，并将访客流量出售给诈骗、赌博及 iPhone 漏洞利用团伙。其中最危险的买家利用 Coruna 与 DarkSword 两套 iOS 漏洞工具包，对特定 iPhone 用户实施“零点击”浏览器攻击并植入间谍软件。

- 🏷️ DeadTag 不直接入侵网站，而是接管网站早已遗忘、仍在加载的过期分析/广告标签域名，域名一被重新注册，相关网站就会自动加载攻击者代码。
- 🌐 研究已确认 660+ 个过期并被重新注册的域名，仍嵌入数千个网站，估计每月影响约 1.35 亿次访问。
- 🕵️ 恶意脚本仅约 2 KB，会过滤搜索引擎、安全扫描器和机器人；对普通访客也常返回空内容，隐蔽性极强。
- 💰 DeadTag 将访客流量按竞价出售，流向 fake VPN 弹窗、假调查/中奖页面、赌博与加密赌场诈骗、搜索广告页面等。
- 📱 最危险买家是 iPhone 漏洞利用团伙：伪造 Polymarket 页面，按 iOS 版本投递 Coruna（iOS 13–17.2.1）或 P7 DarkSword（iOS 18.4–18.7）。
- ☠️ 两套工具均攻击浏览器本身，用户只需打开页面就可能中招，无需点击或安装；成功后窃取钥匙串密码、加密钱包、设备与账户信息。
- 🔗 Coruna 与 DarkSword 虽为不同漏洞工具包，但在此行动中把窃取数据回传至同一服务器，显示由同一操作者按受害者设备选择攻击工具。
- 🛒 该团伙不只依赖 DeadTag，还入侵数百家 PrestaShop 电商商店，将 DarkSword 加载器伪装成分析代码；另发现数百个托管 Coruna 加载器的站点。
- 🇨🇳 归因方面：DeadTag 背后身份不明，看似商业流量操作；iPhone 漏洞团伙疑似中文操作者，代码含简体中文注释，基础设施多为中文加密交易所、赌博及品牌仿冒站点。
- 🛡️ 网站运营者应审计并移除废弃第三方标签、监控脚本变化、部署内容安全策略（CSP）；iPhone 用户应更新 iOS，高风险人群开启 Lockdown Mode。
- 🚨 若怀疑中招：重启手机、更改钥匙串中保存的密码，并将加密资产转移到使用全新助记词的新钱包。

---

### [请稍等……](https://css-tricks.com/)

**原文标题**: [One moment, please...](https://css-tricks.com/)

当前内容仅为加载提示，表示系统正在验证请求，请用户耐心等待。

- ⏳ 页面处于加载状态，尚未显示正文内容。
- 🔐 系统正在验证用户请求。
- 🕒 需等待验证完成后才能继续访问。
- 📄 所提供文本信息有限，无法提炼更多实质内容。

---

### [请稍等……](https://css-tricks.com/css-tricks-has-a-new-owner/)

**原文标题**: [One moment, please...](https://css-tricks.com/css-tricks-has-a-new-owner/)

该文本仅为一个加载提示，说明系统正在验证请求，请用户耐心等待，未包含实质性文章内容。

- ⏳ 页面当前处于加载或等待状态。
- 🔐 系统正在验证用户的请求。
- 🙏 提示用户稍候并耐心等待。
- 📄 文本中没有更多正文或关键信息。

---

### [@geoffgraham.me 在 Bluesky 上](https://bsky.app/profile/geoffgraham.me)

**原文标题**: [@geoffgraham.me on Bluesky](https://bsky.app/profile/geoffgraham.me)

这是 Geoff Graham 的 Bluesky 个人资料页，页面包含其个人网站、去中心化标识、简介、与 CSS-Tricks 的关联，以及使用 Bluesky 需启用 JavaScript 的提示和了解更多信息的链接。

- 👤 姓名为 Geoff Graham
- 🌐 个人网站是 geoffgraham.me
- 🆔 去中心化标识为 did:plc:frp2eva5fxq3irxjneevgrpo
- 💬 简介为“Shower thoughts and sweet nothings”，并关联 @css-tricks.com
- ⚠️ 页面提示需启用 JavaScript 才能使用 Bluesky
- 🔗 可通过 bsky.social 和 atproto.com 了解更多信息

---

### [Firefox 159 面向开发者的发行说明（稳定版）- Mozilla | MDN](https://developer.mozilla.org/en-US/docs/Mozilla/Firefox/Releases/159)

**原文标题**: [Firefox 159 release notes for developers (Stable) - Mozilla | MDN](https://developer.mozilla.org/en-US/docs/Mozilla/Firefox/Releases/159)

Firefox 159 稳定版于 2026 年 10 月 27 日发布，为开发者带来 CSS 滚动驱动动画默认启用、旧版 masonry 语法移除、HTML Sanitizer 与 WebGL 扩展更新、作用域自定义元素注册表支持，以及 WebDriver 兼容性和实验性功能改进；HTML 与 JavaScript 无重大变化。

- 🗓️ Firefox 159 于 2026 年 10 月 27 日发布；HTML 和 JavaScript 无显著变化。
- 🎞️ CSS 滚动驱动动画默认启用，可沿滚动容器的时间线而非文档时间线动画属性值（Firefox bug 1324602）。
- 🧱 移除旧版 masonry 布局语法：`grid-template-columns`/`grid-template-rows` 的 `masonry` 值和 `masonry-auto-flow` 属性，改由 `grid-lanes`/`inline-grid-lanes` 的网格车道布局取代（Firefox bug 2077170）。
- 🧼 HTML Sanitizer API 的 `Element.setHTML()` 等方法改为在解析时移除不需要的元素和属性；结果相同，但相邻文本会合并为单个文本节点（Firefox bug 2070498）。
- 🎮 WebGL 新增 `EXT_clip_control` 扩展（驱动支持时可用），可改变裁剪空间到窗口坐标的映射，并支持 0 到 1 深度范围与 reversed-Z（Firefox bug 1885031）。
- 🪞 WebGL 新增 `EXT_texture_mirror_clamp_to_edge` 扩展（驱动支持时可用），提供 `MIRROR_CLAMP_TO_EDGE_EXT` 纹理环绕模式（Firefox bug 1908749）。
- 🧊 WebGL 2 的 `EXT_texture_norm16` 扩展在支持 16 位归一化格式的设备上默认启用（Firefox bug 1735401）。
- 🧩 DOM 支持作用域自定义元素注册表，`Document`、`Element` 和 `ShadowRoot` 可使用 `customElementRegistry`，并可通过 `CustomElementRegistry()` 创建作用域注册表以避免组件命名冲突（Firefox bug 2070506）。
- 🧪 WebDriver：推荐首选项改为默认值；移除 `--remote-allow-system-access`，改用 `MOZ_REMOTE_ALLOW_SYSTEM_ACCESS=1`；修复超时后内部轮询持续到关闭导致的内存泄漏。
- 🛰️ WebDriver BiDi：实现 `emulation.setMediaFeaturesOverride`（目前仅支持 `prefers-color-scheme`），并新增 Firefox 专有扩展的机器可读 CDDL 文件。
- ⚙️ 实验性功能：CSS 数值工厂函数（如 `CSS.px()`）在 workers 和 worklets 中暴露；`MathMLAnchorElement` 新增 `download`、`ping`、`rel`、`relList` 和 `referrerPolicy` 属性，均需相应首选项开启。

---

### [数字凭证 API 签发功能随 Chrome 155 发布 | 博客 | Chrome 开发者](https://developer.chrome.com/blog/digital-credentials-api-issuance?hl=en)

**原文标题**: [Digital Credentials API issuance ships in Chrome 155  |  Blog  |  Chrome for Developers](https://developer.chrome.com/blog/digital-credentials-api-issuance?hl=en)

Chrome for Developers 博客宣布：Chrome 155 起默认启用 Digital Credentials API 发行功能，网站可将数字身份证等凭证直接写入用户钱包；文章介绍了同设备与跨设备流程、代码实现、与 origin trial 的差异、测试方法和行业采用案例。

- 🚀 Chrome 155 及以后默认启用 Digital Credentials API issuance，无需 origin trial token 或 flag。
- 🧩 API 作为传输层连接网站与移动设备钱包应用，发行方可把新凭证直接添加到用户钱包。
- 🏛 数字身份生态包含发行方、验证方/依赖方和持有方（钱包应用），常见方式是从发行方网站或应用发起 push provisioning。
- ⚙️ 发行通过 `navigator.credentials.create()` 并在 `digital` 成员中传入请求，由 Chrome 交给操作系统处理；Android 使用 Credential Manager，并支持 OpenID4VCI 等标准协议。
- 📱 同设备流程：Android 上 Credential Manager 显示兼容钱包列表，用户选择并同意后，钱包按发行协议从发行方获取凭证。
- 💻 跨设备流程：桌面 Chrome 显示 QR 码，用户用 Android 设备扫描完成；设备间用蓝牙确认距离，必要时提示开启蓝牙。
- 🖱️ 实现时需在点击等用户手势处理器中调用 `create()`，因为需要 transient user activation；示例包含预授权码流程和错误处理。
- ⚠️ 错误处理：用户取消、无可用钱包或无用户激活通常返回 `NotAllowedError`；浏览器不支持返回 `NotSupportedError` 并应回退；请求格式错误返回 `TypeError`。
- 🔄 相比 origin trial 的变化：Chrome 146 起 `create()` 消耗用户激活；Chrome 148 起取消流程由 `NetworkError` 改为 `NotAllowedError`；Chrome 151 起阻止 opaque origins 并对未识别协议标识发出弃用警告，推荐使用 `openid4vci-v1`。
- 🧪 Chrome 152 起可通过 CDP 的 `DigitalCredentials.setVirtualWalletBehavior` 使用虚拟钱包做自动化测试；跨域 iframe 需允许 `digital-credentials-create` 权限策略。
- 🏦 行业采用示例：德国 Sparkasse 使用该 API 让账户持有人将已验证年龄凭证保存到 Google Wallet，用于线上和线下年龄验证。
- 📚 文章提供 W3C 规范、OpenID4VCI 1.0、开发者指南、demo issuer 和 demo CMWallet 等资源，并建议在 Chrome 155+、安装支持的钱包、跨设备流程开启蓝牙后进行测试。

---

### [获取失败](https://www.w3.org/blog/2026/w3c-launches-second-pilot-of-program-to-support-open-source-projects/)

**原文标题**: [Failed to retrieve](https://www.w3.org/blog/2026/w3c-launches-second-pilot-of-program-to-support-open-source-projects/)

无法总结：获取内容失败，状态码 403。

---

### [告别 Arc](https://arc.net/)

**原文标题**: [A farewell to Arc](https://arc.net/)

Arc 浏览器将于 2026 年 12 月 22 日正式停止服务，团队将把工程与安全重点转向新浏览器 Dia；Arc 用户需在截止前完成迁移或导出数据。

- 🗓️ Arc 于 2026 年 12 月 22 日停止服务，macOS/Windows 版届时无法访问或使用，账户停用且个人数据将在 30 天内删除。
- 🚫 2026 年 10 月 22 日起停止创建新 Arc 账户；现有用户暂不受影响，但可开始导出数据并导入 Dia。
- 📱 2026 年 11 月 23 日起，iOS/Android 版关闭 Browse for Me 等 AI 功能，停止登录与标签页同步；Arc Search 仍可作为简化浏览器使用。
- 🤖 Android 版 Arc Search 将于 2026 年 12 月 22 日从 Google Play 下架，并从已安装设备中移除。
- 🧭 Dia 是 Arc 团队打造的新浏览器，重点应对 AI 时代的安全需求，稳定性、速度和安全性超过 Arc 基准。
- 🔁 迁移便捷：密码、书签、扩展、历史记录、Spaces（变为 Profiles）、文件夹（变为 Tab Groups）、固定标签和收藏可导入 Dia。
- 🆓 Arc 中常用的浏览器功能在 Dia 中免费，AI 功能为可选。
- 💾 用户可在 2026 年 12 月 22 日前从 Arc 导出标签页/数据；若使用 Dia 可直接导入，无需先导出。
- 🛟 截止日前可通过 Arc Help Center 聊天获取迁移、导出和删除数据帮助；使用 Dia 可从应用内联系支持。

---

### [Dia | 让工作日更美好的浏览器。](https://www.diabrowser.com/)

**原文标题**: [Dia | The browser for better days at work.](https://www.diabrowser.com/)

Dia 是一款超越传统浏览器的智能工作浏览器，可免费下载并支持 macOS 与 Windows；它通过整合日历、收件箱、Slack、Notion、Teams 等信息，帮助用户更高效地开启工作、查找答案、生成报告并管理多场景工作流，同时强调隐私与团队安全控制。

- 🌅 **Morning Brief**：每天开始前汇总日历、收件箱和关键链接，让用户提前掌握当天安排。
- 🧠 **智能整合**：直接向 Dia 提问，即可把分散在 Slack、Notion、Teams 等工具中的信息整理成可分享的报告。
- 🔍 **上下文搜索**：一次提问即可跨 GSuite、Teams、标签页等查找答案，减少手动搜索。
- 👤 **多场景 Profiles**：区分工作、自由职业和个人生活，拥有独立标签页、登录状态和 AI 上下文，滑动即可切换。
- 🧩 **工作流增强**：Live Work 快速进入 GitHub、Notion 等工作页面；Better Meetings 自动准备会议页、议程和文档；Splits 支持分屏并记住布局。
- 📊 **Deck 与标签管理**：可让 Dia 将零散上下文生成演示文稿，并按“设计评审”“Q2 规划”等命名整理标签页。
- 🔒 **隐私优先**：用户可控制记忆、连接工具、广告与追踪器拦截等设置；数据不出售、不用于广告画像，Sync 端到端加密。
- 🛡️ **Dia for Work**：为企业提供 SSO、管理员工具等安全护栏，方便团队安全使用。

---

### [禅浏览器](https://zen-browser.app/)

**原文标题**: [Zen Browser](https://zen-browser.app/)

Zen 是一款注重隐私、设计精美且功能丰富的浏览器，目前 Beta 版已开放，目标是带来更平静、更专注的上网体验，并强调不会以用户数据为代价。

- 🌐 Zen 以“更平静的互联网”为愿景，兼顾美观设计与隐私保护。
- 🔒 强调重视用户体验而非数据，主打隐私优先。
- 🚀 Beta 版现已可用，并鼓励用户支持项目。
- 🗂️ 工作区功能可分类整理标签页，便于分隔和管理不同项目。
- 🖥️ 紧凑模式可在不需要时隐藏标签栏，释放更多屏幕空间。
- 👀 Glance 可快速切换常用标签页，无需翻找历史记录。
- 🪟 分屏视图支持两个标签页并排显示，方便比较和切换。
- ❤️ 项目感谢赞助商支持，也欢迎用户直接捐赠参与。
- 🧭 核心价值观包括免费开源、简单而强大、隐私保护且始终更新。

---

### [是时候回到 Firefox 了。你热爱的互联网依然在这里。 - YouTube](https://www.youtube.com/watch?v=E2AoYIKwJqM)

**原文标题**: [It’s time to come back to Firefox. The Internet you loved is still here. - YouTube](https://www.youtube.com/watch?v=E2AoYIKwJqM)

该内容为 YouTube 网站底部的导航与版权信息，集中列出关于、新闻、版权、联系、创作者、广告、开发者、条款、隐私、政策与安全、YouTube 工作原理及新功能测试等链接，并标注 © 2026 Google LLC。

- 🔗 包含“关于、新闻、版权、联系我们”等基础信息入口。
- 👥 提供“创作者、广告、开发者”等合作与开发相关链接。
- 📜 列出“条款、隐私、政策与安全”等法律与政策入口。
- ⚙️ 包含“YouTube 工作原理”和“测试新功能”的说明与功能入口。
- ©️ 底部标注版权归属为 © 2026 Google LLC。

---

### [Safari 27.1 的 WebKit 功能 | WebKit](https://webkit.org/blog/18486/webkit-features-for-safari-27-1/)

**原文标题**: [  WebKit Features for Safari 27.1 | WebKit](https://webkit.org/blog/18486/webkit-features-for-safari-27-1/)

Safari 27.1 随 iPhone Duo 发布，核心信息是“没有大新闻”：它与其他 iPhone 使用相同的 WebKit 引擎和 Web 技术，网站与 Web 应用可正常兼容。面向用户新增折叠状态下的 PDF 双页并排显示；面向开发者提供 Device Posture API 与 Viewport Segments API 的预览版，并建议采用响应式设计与特性检测来适配折叠屏。

- 📱 Safari 27.1 随 iPhone Duo 推出，但并未引入独立 WebKit 或特殊 Web 技术，现有网站和 Web 应用应像在其他 iPhone 上一样工作。
- 📄 用户将 iPhone Duo 像书一样半折叠查看网页 PDF 时，Safari 27.1 会自动双页并排显示；展开或完全闭合后恢复单页。
- 🧪 开发者可在功能标志后预览 Device Posture API 和 Viewport Segments API，路径为“设置 > App > Safari > 高级 > 功能标志”。
- 📐 Safari 27.1 的视口 CSS 宽度范围约为 382–951 px，高度约为 368–902 px，覆盖外屏、内屏、横竖屏及双窗口等姿态。
- 🧭 建议使用现代响应式 Web 设计、CSS Grid、Flexbox、媒体查询与特性检测，避免 UA 嗅探，以适配各种屏幕尺寸。
- 🛠️ 无需实体 iPhone Duo 也可测试，可下载 Xcode 27.1 或更高版本，通过 Device Hub 创建并使用 iPhone Duo 模拟器。
- 🔄 Device Posture API 可通过 `device-posture` 媒体查询和 `navigator.devicePosture` 报告 `folded`（半折叠）与 `continuous`（平整）两种姿态，并监听变化事件。
- 🪟 Viewport Segments API 通过 `horizontal-viewport-segments`、`vertical-viewport-segments` 媒体查询、六个环境变量及 `window.viewport.segments` 描述折叠两侧的显示区域。
- 🎨 目前网页内容不会延伸到 iPhone Duo 外屏侧边控件后方，Safari 会用页面背景色填充；WebKit 正在探索更稳妥、易用的扩展方案。
- 💬 官方欢迎开发者反馈 API 使用体验、问题与对网页内容延伸至控件后方区域的建议。

---

### [设备姿态 API - Web API | MDN](https://developer.mozilla.org/en-US/docs/Web/API/Device_Posture_API)

**原文标题**: [Device Posture API - Web APIs | MDN](https://developer.mozilla.org/en-US/docs/Web/API/Device_Posture_API)

设备姿态 API 是一项实验性功能，可帮助开发者构建能感知折叠设备物理姿态并随姿态变化而调整的用户界面；它定义了 continuous 与 folded 两种姿态，并提供 CSS 媒体特性、JavaScript 接口和姿态变化事件，但当前浏览器支持有限，不建议未经兼容性检查直接用于生产环境。

- ⚠️ 该功能可用性有限，不属于 Baseline，在部分主流浏览器中无法使用，使用前需查看兼容性表。
- 🧪 它属于实验性技术，生产环境使用前应谨慎评估。
- 📱 核心用途是让界面适配折叠设备，并响应设备姿态变化。
- 📖 折叠设备可用于平整屏幕或书本式形态，设计时需避免内容被物理铰链遮挡或受中央折痕影响。
- ➡️ 当前姿态包括 `continuous`（平整状态，含完全展开、完全闭合及非折叠设备）和 `folded`（书本或笔记本式折叠状态）。
- 🎨 提供 CSS `@media` 特性 `device-posture`，用于检测设备当前姿态。
- 🧩 提供 `DevicePosture` 接口，可访问当前姿态 `type`，并监听 `change` 事件。
- 🔌 通过 `Navigator.devicePosture` 获取浏览器对应的 `DevicePosture` 对象。
- 💻 官方示例展示全部功能；开发者工具可模拟折叠设备，但通常只能模拟完全展开或闭合，因此会返回 `continuous`。
- 🔗 相关内容还包括 Viewport Segments API 以及 Chrome 开发者网站上的 Foldable APIs 源试用信息。

---

### [视口分段 API - Web API | MDN](https://developer.mozilla.org/en-US/docs/Web/API/Viewport_segments_API)

**原文标题**: [Viewport Segments API - Web APIs | MDN](https://developer.mozilla.org/en-US/docs/Web/API/Viewport_segments_API)

Viewport Segments API 是一项实验性且非 Baseline 的 Web 能力，允许开发者通过 CSS 和 JavaScript 获取由折叠、铰链或多屏等硬件特性分割出的逻辑视口段的位置与尺寸，从而为可折叠/双屏设备构建更稳健的响应式布局。

- 🧪 **实验性与兼容性限制**：该功能尚未成为 Baseline，部分主流浏览器不支持；生产使用前应仔细查看浏览器兼容性表。
- 📐 **核心能力**：开发者可访问每个视口段的位置和尺寸，并针对不同段大小与排列方式优化响应式设计。
- 🧩 **视口段来源**：当视口被折叠、铰链或独立显示屏之间的硬件特征分割时，会形成逻辑上独立的视口段。
- 🎯 **设计目标**：帮助设计元素贴合不同屏幕段，避免内容被切成两半或被物理折叠/连接处遮挡。
- 🔍 **需要掌握的信息**：设备是否有折叠或连接处、各段尺寸、各段是否等大，以及段是并排还是上下排列。
- 🖥️ **JavaScript 接口**：`Viewport` 表示设备视口，`Viewport.segments` 返回一组 `DOMRect`，描述各视口段的位置和尺寸；`Window.viewport` 返回当前 `Viewport` 实例。
- 🧭 **CSS 媒体特性**：`horizontal-viewport-segments` 和 `vertical-viewport-segments` 可检测水平或垂直排列的视口段数量。
- 📏 **CSS 环境变量**：提供各视口段边缘坐标和尺寸的访问能力。
- 📱 **示例与模拟限制**：官方提供演示，建议在可折叠设备上查看；浏览器开发者工具可模拟折叠设备，但不包含不同物理段的模拟。
- 📚 **规范与相关资源**：规范为 CSS Viewport Module Level 1；另可参考 Using the Viewport Segments API、CSSOM View API、Device Posture API、CSS 环境变量及折叠设备 API 的 Origin trial。

---

### [探究一例奇特的字体格式回退案例 | Paul Calvano](https://paulcalvano.com/2026-10-18-investigating-a-curious-case-of-font-format-fallbacks/)

**原文标题**: [Investigating a Curious Case of Font Format Fallbacks | Paul Calvano](https://paulcalvano.com/2026-10-18-investigating-a-curious-case-of-font-format-fallbacks/)

本文讲述了作者在 NY WebPerf Meetup 的 Meet4Speed 活动中分析一个电商网站性能时，发现并深入排查 FontAwesome 字体因文件内部大小不匹配而依次回退加载 WOFF2、WOFF、TTF 的罕见问题，并给出修复与优化建议。

- 🍕 Meet4Speed 是 NY WebPerf Meetup 的互动式性能分析活动，没有讲者，大家围坐会议桌吃披萨，并用 Chrome DevTools、WebPageTest 分析参会者网站。
- 🛒 在一次热门电商网站分析中，团队发现第三方性能功能单点故障、字体仅用于极少量文本、仅 5 个字形却未子集化、预加载脚本未使用、CDN 图片优化静默失败、图片懒加载未生效等问题。
- 🔍 最意外的问题是 FontAwesome 在 Chrome、Safari、Edge 中依次加载 WOFF2、WOFF、TTF 三种格式；同一字体重复加载通常因预加载，但此处没有预加载，且请求呈顺序回退模式。
- ⚠️ DevTools 控制台出现“Failed to decode downloaded font”“Failed to convert WOFF 2.0 font to SFNT”“OTS parsing error: incorrect file size in WOFF header”等错误，说明浏览器无法解码或解析字体。
- 🧩 浏览器内部会把 WOFF2/WOFF 转换为 TTF，并使用 SFNT 容器保存字体数据；OTS 是 OpenType 字体清洗器，解析失败会触发回退。
- 📏 排查发现 HTTP Content-Length 与实际下载文件大小一致，CDN 也正确报告大小；真正问题是字体文件自身头部声明的文件大小与实际文件大小不匹配。
- 🧾 WOFF2 文件实际 77,159 字节，但内部头记录 77,160 字节；WOFF 也存在头部大小与实际文件大小不一致，导致解码失败并回退到下一格式。
- 🛠️ 该字体是较旧的 Font Awesome 4 版本，可能因版本编码错误或下载损坏导致；修复方式是替换为新版字体文件，并考虑按实际使用字形做子集化。
- 📈 修复后预计对 FCP 有可测量影响；该问题并不常见（HTTP Archive 中不普遍），但排查过程很有学习价值，也展示了 Meet4Speed 活动可能带来的深入分析。

---

### [没有噪音，只有你想要的会话回放 | Sentry](https://sentry.io/resources/201-session-replays/?utm_source=frontendfocus&utm_medium=paid-community&utm_campaign=tracing-fy27q3-sessionreplayworkshop&utm_content=newsletter-sponsored-link-register)

**原文标题**: [The session replays you want without the noise | Sentry](https://sentry.io/resources/201-session-replays/?utm_source=frontendfocus&utm_medium=paid-community&utm_campaign=tracing-fy27q3-sessionreplayworkshop&utm_content=newsletter-sponsored-link-register)

本次内容介绍了一场关于 Session Replay 的实操工作坊，重点讲解如何减少无关噪音、精准找到所需会话回放，并涵盖采样、自定义 React Hooks、用户反馈、筛选标签与隐私设置等关键能力；同时提到赞助的 Syntax 开发者播客。

- 🎯 工作坊主题：无需噪音，获得想要的 Session Replay，而不只是错误附带的视频。
- ⚙️ 实操内容：创建自定义 React Hooks、带 Replay 的用户反馈、以及用筛选器和标签定位会话。
- 📊 采样设置：介绍两种采样率、buffer mode 的作用以及推荐默认值。
- 🪝 自定义 Hooks：用于捕获特定用户群体、已知问题 URL 或刚上线流程等精确会话。
- 💬 用户反馈：配置反馈组件，让 bug 报告自动附带对应 Replay。
- 🔍 查找回放：使用筛选器、dead clicks、rage clicks 和自定义标签，按产品实际结构切分回放。
- 🔒 隐私：说明默认设置以及如何自定义隐私选项。
- 🎙️ 播客推荐：提到赞助 Syntax 开发者播客，并可在常用平台收听。

---

### [](https://csswizardry.com/2026/10/web-perf-wednesday-014-performance-budgets-need-a-representative-worst/)

**原文标题**: [Web-Perf Wednesday 014 – Performance Budgets Need a Representative Worst – CSS Wizardry](https://csswizardry.com/2026/10/web-perf-wednesday-014-performance-budgets-need-a-representative-worst/)

本文来自 Harry Roberts 于 2026 年 10 月 21 日发布的 Web-Perf Wednesday 014，核心是修正性能预算的设置方法，并汇总 Safari、Chrome 与 DevTools 的三项新变化。

- 📅 文章主题为“性能预算需要一个有代表性的最差值”，强调单次异常值会误导预算设置。
- 🎯 过去取“近期最差结果”作为初始预算过于简单；若 LCP 通常 2.2 秒但偶发 7.1 秒，7.1 秒预算会掩盖严重退化。
- 📊 改进方法是使用代表性最差值，如 P90 或 P95；若每日记录 P75 LCP，可计算这些日值的 P90，并提供 Google Sheet 模板辅助计算。
- 🧩 预算仍需人工判断：数据要覆盖正常波动，区分合成测试、RUM、第三方请求等不同人群，并让阈值来源与执行环境一致。
- 🍎 Safari 27 在 iOS、iPadOS、macOS 和 visionOS 上按域名阻止身份解析基础设施，可能影响归因、受众匹配和网络瀑布。
- 🌐 Chrome 156 于 10 月 20 日进入稳定版，不再缓存失败的模块加载，使 `import()` 可真正重试；但重试需有次数限制并记录失败与恢复情况。
- 🧠 Chrome DevTools 可检测共享 V8 上下文中未使用的闭包变量，帮助定位内存保留问题；SPA 中可重复路由或交互后对比快照。
- 🤝 作者还提供咨询帮助，协助选择代表性周期、拆分不兼容数据群体，并将预算与 trace、RUM 或发布证据关联。

---

### [互联网历史上最脆弱的一周…… - YouTube](https://www.youtube.com/watch?v=SMGg7iisHmc)

**原文标题**: [The most vulnerable week in internet history... - YouTube](https://www.youtube.com/watch?v=SMGg7iisHmc)

该内容为 YouTube 页面底部的导航与版权信息，集中列出平台介绍、联系渠道、创作者/广告/开发者资源、法律政策、安全说明、功能测试入口，以及 Google LLC 的 2026 年版权声明。

- 🏢 包含 About、Press、Contact us 等平台介绍与联系入口。
- 👥 提供 Creators、Advertise、Developers 等创作者、广告和开发者资源。
- ⚖️ 列出 Terms、Privacy、Policy & Safety、Copyright 等法律、隐私、安全与版权链接。
- ⚙️ 包含 How YouTube works 与 Test new features 等产品说明和功能测试入口。
- ©️ 底部标注 © 2026 Google LLC 版权信息。

---

### [为 AI 生成的 HTML 构建隔离预览 – Master.dev 博客](https://blog.master.dev/building-an-isolated-preview-for-ai-generated-html/)

**原文标题**: [Building an Isolated Preview for AI-Generated HTML – Master.dev Blog](https://blog.master.dev/building-an-isolated-preview-for-ai-generated-html/)

本文围绕“如何安全预览 AI 生成的 HTML”展开：直接用 `iframe.srcdoc` 渲染看似安全，实则会让不可信代码继承宿主页面权限。作者通过三个攻击测试说明沙箱、CSP 与消息通信必须分别配置，并给出可落地的四层防护方案。

- 🧨 **初始做法有隐患**：把模型返回的 HTML 直接写入 `iframe.srcdoc`，虽然没有用 `innerHTML`，但仍会在宿主环境附近执行未审查代码。
- 🕵️ **同源读取风险**：未加 `sandbox` 的 `srcdoc` iframe 与宿主同源，可读取 `parent.document`、`localStorage`、Cookie 等敏感信息。
- 🚪 **跳出框架风险**：恶意页面可尝试导航顶层窗口、打开弹窗或提交表单；仅 `allow-scripts` 能阻止这些行为，但不应随意追加 `allow-top-navigation` 等权限。
- 📡 **网络外传仍可能发生**：即使沙箱阻止读取宿主和导航，`fetch()` 或远程图片请求仍可能携带数据外传，需要 CSP 限制资源加载。
- 🧱 **沙箱从空白开始**：使用 `sandbox=""` 作为基线，只按需添加 `allow-scripts`，每增加一个 token 都应有明确理由。
- ⚠️ **禁止危险组合**：不要同时使用 `allow-scripts` 与 `allow-same-origin`，否则不可信内容可能接触宿主并移除自身沙箱限制。
- 🆔 **不要信任 `"null"` 来源**：沙箱 iframe 的不透明源在消息事件中序列化为 `"null"`，不能用于来源白名单；应使用 `event.source` 校验真实窗口引用。
- 🌐 **独立源更稳妥**：高价值场景应把预览部署到一次性或独立域名，使沙箱逃逸后也难以接触主站会话与数据。
- 🛡️ **CSP 是独立防线**：在预览文档中加入 `default-src 'none'` 等策略，限制脚本、样式、图片和网络请求；`srcdoc` 还会继承宿主 CSP。
- 🔐 **消息通道需严格校验**：预览与父页面通信时，应校验 `event.source`、消息结构和数值范围；必要时使用 `MessageChannel` 建立私有通道。
- ✅ **安全预览仍要可用**：加固后的预览应阻止读取宿主、顶层导航和网络外传，同时仍能接受合法的高度调整消息，并拒绝伪造或畸形消息。
- 🚢 **实践原则**：先空沙箱再加最小权限、尽量使用独立源、沙箱与 CSP 同时启用、所有放宽策略都要能说明原因并承担风险。

---

### [网站应该可以打印](https://brennenputh.me/blog/printable-websites/)

**原文标题**: [Websites Should Be Printable](https://brennenputh.me/blog/printable-websites/)

文章从作者个人偏好打印阅读和纸笔标注出发，指出许多网页默认打印效果很差，并分享如何用 CSS 优化打印样式；核心观点是：即使是纯文字网站，也应让用户能在自己喜欢的媒介中舒适阅读内容，这是对用户的一种体贴。

- 🖨️ 作者喜欢打印文档并做标注，认为打印阅读比屏幕阅读更能投入，因此希望自己的网页内容也能方便打印。
- 🧪 作者测试自己网页的打印效果后发现：字号过大、页眉难看、链接在黑白打印中呈灰色，整体不可接受。
- 🎨 解决方案是使用 CSS 的 `@media print` 和自定义类，为打印版单独设置样式。
- 👁️ `onlyPrint` 用于只在打印版显示元素，例如在副标题后添加作者署名。
- 🙈 `noPrint` 用于在打印时隐藏元素，例如作者把页眉隐藏，因为打印出来很难看。
- 🔠 打印时应重新设置字号：正文和列表约 `12pt`，标题从 `13pt` 到 `16pt` 逐级增大。
- 💻 代码块通过 `giallo` 相关样式调整，但仍有问题：代码块容易整块输出、难以跨页断开，作者希望获得解决方案。
- 🔗 链接在屏幕上用蓝色没问题，但灰度打印效果差，因此打印时改为黑色。
- ✍️ 作者更新说明：文章收到 Lobsters 和 Hacker News 反馈后，他正在进一步简化样式表。
- ❤️ 作者承认专门优化打印样式费时，且打印网页的人可能很少，但纯文字网站让用户以喜欢的方式阅读内容始终是好事。
- 📣 这篇文章后来登上 Hacker News 和 Lobsters 首页，作者希望它能促使更多人重视网页打印体验。

---

### [为什么我仍在制作 CSS 教程 - YouTube](https://www.youtube.com/watch?v=wAwaEgr9MTo)

**原文标题**: [Why I'm still making CSS tutorials - YouTube](https://www.youtube.com/watch?v=wAwaEgr9MTo)

本内容为 YouTube 网站页脚信息，集中列出平台介绍、联系入口、创作者与开发者资源、广告服务、法律与安全政策、功能说明及版权声明。

- 📄 包含 About、Press、Copyright、Contact us 等平台介绍、新闻与联系入口。
- 👥 提供 Creators、Advertise、Developers 等面向创作者、广告主和开发者的资源。
- ⚖️ 列出 Terms、Privacy、Policy & Safety 等法律、隐私与安全相关政策。
- ⚙️ 包含 How YouTube works 与 Test new features，用于说明平台运作方式及测试新功能。
- ©️ 标注 © 2026 Google LLC 的版权信息。

---

### [TitleArt — 让文字看起来像 1997 年](https://titleart.dvy.io/)

**原文标题**: [TitleArt — Make text like it’s 1997](https://titleart.dvy.io/)

该文本仅为一个加载状态提示，未包含可总结的文章正文。
- ⏳ 内容显示“Loading TitleArt…”，表示标题艺术图正在加载。
- 📄 由于缺少正文信息，无法提取更多关键要点。

---

### [适用于任意规模时间序列工作负载的 Postgres。| Tiger Data](https://www.tigerdata.com/go/trial?utm_source=content-syndication&utm_medium=referral&utm_campaign=frontend-focus-newsletter)

**原文标题**: [Postgres for time-series workloads at any scale. | Tiger Data](https://www.tigerdata.com/go/trial?utm_source=content-syndication&utm_medium=referral&utm_campaign=frontend-focus-newsletter)

Tiger Cloud 是面向任意规模时间序列工作负载的 Postgres 平台，强调单服务可达 3 万亿指标/天、3 PB 数据与 1 千万亿数据点，并提供企业级高可用、安全合规、可观测性和快速部署能力。

- 📈 单 Tiger Cloud 服务可实现每天 3 万亿指标、3 PB 数据、1 千万亿数据点的真实规模。
- 🎁 新账户注册可获 1000 美元额度，有效期 30 天，无需信用卡，仅限新账户。
- 🏭 受到数千家 IoT 等领域企业信任。
- ⚡ 通过最多 10 个节点的副本集分离读写，并支持 SSD/S3 分层存储，实现低成本、近乎无限的存储扩展。
- 💰 计算与存储分离，可独立扩展，避免为闲置容量付费并优化性能。
- 🛡️ 提供多可用区集群、自动故障转移、时间点恢复和跨区域备份，保障高可用性。
- 🔐 企业级能力包括 SOC 2、HIPAA、GDPR 合规、始终加密、SSO、RBAC 和审计日志。
- 🔍 深度可观测性支持查询下钻和仪表盘，并可将指标发送至 CloudWatch、Datadog、Prometheus。
- 🚀 可在数分钟内开通数据库，并通过 SQL、CLI、Terraform、Cursor 或 Claude Code 管理。
- 🔌 可与首选云提供商及更广泛的 Postgres 生态集成。
- 🏢 企业版默认就绪：合同化正常运行时间 SLA、区域数据隔离、合规认证。
- ☎️ 提供 7×24 小时全球 Postgres 专家支持和有保障的企业响应时间。

- 📄 页面底部包含隐私偏好、法律、隐私、站点地图及 2026 年版权信息（Timescale, Inc., d/b/a Tiger Data）。

---

### [网站规范](https://specification.website/)

**原文标题**: [The Website Specification](https://specification.website/)

这份指南系统梳理了一个好网站应具备的技术细节，覆盖从页面 `<title>` 到 HTTP 响应头的完整链路，面向人类用户与 AI 代理，且不限定技术栈。内容按 10 大领域、178 个主题组织，并强调每项细节都有标准依据和明确理由。

- 📘 覆盖网站建设全流程：从文档基础、用户体验到安全、隐私、SEO 与 AI 代理可读性。
- 🧱 10 大领域包括：基础、SEO、无障碍、安全、Well-Known URIs、代理就绪、性能、隐私、韧性、国际化。
- ♿ 体验相关领域关注可用性、无障碍、性能与国际化，确保不同能力和地区的用户都能使用。
- 🔐 信任相关领域关注安全、隐私与韧性，保护访客并保证网站在异常情况下仍可运作。
- 🔎 发现相关领域关注 SEO、Well-Known URIs 与 Agent Readiness，让网站被搜索者和 AI 代理理解。
- ✅ 每个主题都说明“是什么、为什么重要、如何实现”，检查清单项目均为是/否判断。
- 📊 检查项分为：必需 36 项、推荐 87 项、可选 49 项、应避免 6 项。
- 🛠️ 可用于审计网站、发现缺失项、修复后重新检查。
- 🤖 提供开放只读 MCP 服务器，代理可查询完整规范，参考工具无需认证。
- 🌐 强调标准而非观点、每个主题引用一手来源、平台无关、开放协作并欢迎 PR。

---

### [browser-whisper — 基于 WebGPU 的浏览器原生音频转录](https://whisper.tanpreet.xyz/)

**原文标题**: [browser-whisper — Browser-Native Audio Transcription via WebGPU](https://whisper.tanpreet.xyz/)

该内容介绍 `browser-whisper` 在浏览器端进行语音转写的安装方式、基础用法与在线演示功能。

- 📦 支持使用 `bun`、`npm`、`pnpm`、`yarn` 安装，示例命令为 `bun add browser-whisper`。
- 🧩 通过 `import { BrowserWhisper } from 'browser-whisper'` 引入并创建实例。
- ⚙️ 可指定模型，例如 `new BrowserWhisper({ model: 'whisper-base' })`。
- 🎙️ 调用 `whisper.transcribe(file)` 可异步逐段获取转写结果中的 `text`、`start`、`end`。
- 🖥️ 提供浏览器实时演示，可上传音频或视频并一步完成转写。
- 🧪 全部演示还涵盖 OPFS 缓存、手动下载模型，以及实时麦克风与 VAD 功能。

---

### [UI 音效设计：936 个界面音效 | UI SFX](https://uisfx.com/)

**原文标题**: [UI Sound Design: 936 Interface Sound Effects | UI SFX](https://uisfx.com/)

UI SFX 是一个开源 UI 音效设计库，面向 Web、移动、SaaS、教育、媒体和游戏产品，提供可直接上线的界面音效系统。共 936 个声音，覆盖 78 个语义化 UI 提示、12 种声音风格、72 个短音效和 6 个无缝循环；代码为 MIT，音频为 CC0。

- 📦 通过 `npm install uisfx` 安装，零依赖；支持 Web 实时合成，也可复制全部 936 个 MP3/Ogg 到原生、游戏或媒体项目。
- 🎛️ 提供 12 种声音个性：Minimal、Soft、Glass、Arcade、Mechanical、Organic、Dreamy、Sci-fi、Rubber、Cinematic、Studio、Zen，适配不同产品气质。
- 🧩 78 个语义化提示覆盖输入、选择、导航、编辑、移动、通信、反馈、进度、循环、媒体、系统、奖励、商业 13 类，每类 6 个。
- 🔁 包含 72 个 one-shots 和 6 个 seamless loops；one-shots 自动结束，loops 返回可停止控制。
- 🤖 提供 coding agent prompt，让代理为产品选择合适 feel，并完成整体音效布置。
- 🎚️ 可逐项试听并比较同一 cue 在不同 feel 下的表现，还提供 workflow、shop、game quest、player、team chat 交互 demo 展示情境状态变化。
- 📖 附带完整 UI sound design field guide，涵盖界面时刻选择、语义化声音语言、one-shots/loops 设计、无障碍与跨平台实现。
- 💰 项目通过赞助维持开源维护、新 feel 和更干净 loops；代码保持 MIT，所有声音保持 CC0。
- 🔗 提供 GitHub、npm、agent guide 和赞助入口，便于集成与持续使用。

---

### [GitHub - romainsimon/uisfx：为你的界面提供 UI 音效 · GitHub](https://github.com/romainsimon/uisfx)

**原文标题**: [GitHub - romainsimon/uisfx: UI Sound Effects for your interfaces · GitHub](https://github.com/romainsimon/uisfx)

overview summary  
UI SFX 是面向 Web、移动端、SaaS、教育、媒体和游戏的开源语义化界面音效系统，可通过统一语义提示在不同音色包间切换，代码 MIT、音频 CC0，并提供 npm 包、轻量 Web Audio 运行时和可直接使用的音频文件。

- 🎯 **核心能力**：用 `success`、`drop`、`level-up` 等语义提示调用音效，切换 12 种音色包无需修改交互代码。
- 📦 **内容规模**：包含 78 个语义提示、13 类交互、12 个完整音色包、936 个原创音效，均提供 MP3 与 Ogg。
- 🎚️ **音效类型**：72 个短 one-shots 与 6 个无缝循环，循环覆盖 loading、processing、recording、connecting、scanning、streaming。
- 🧩 **12 种音色人格**：minimal、soft、glass、arcade、mechanical、organic、dreamy、scifi、rubber、cinematic、studio、zen，适配效率、移动、游戏、AI、创意等场景。
- ⚡ **运行时轻量**：压缩后 Web Audio 运行时仅 12.0 kB，零依赖；懒创建 `AudioContext`，首次可信交互调用 `unlock()`。
- 🛠️ **易集成**：通过 `npm install uisfx` 安装；`createUISFX` 配置音色包与偏好，`play` 播放，`setPack` 切包；支持 HTML 数据属性绑定。
- 🔁 **播放器策略**：默认 8 voices，循环去重，重复结果重启，高频提示限流，切换音色包时迁移活动循环句柄。
- 📁 **跨平台音频**：提供 `sounds/{pack}/{cue}.mp3/ogg` 与 manifest，可用于 React Native、Swift、Kotlin、Unity、Godot、视频等环境。
- ♿ **无障碍原则**：声音只强化可见反馈；提供持久静音与音量设置；不以声音作为成功、警告、错误的唯一区分；首次交互后播放。
- 💾 **偏好与预加载**：`preferences` 将音色包、音量、启用状态存入 localStorage；`preload()` 支持 `AbortSignal`，避免阻塞主任务。
- 🧪 **可复现构建**：音效由确定性合成配方生成；需 Node 22.20+、Chrome/Chromium、ffmpeg；质量门禁验证大小、峰值、尾静音、循环接缝、相似度等。
- 🧠 **设计理念**：将“产品事件 → 语义提示 → 音色包 → 配方/资源”分离，避免 `soft-pop-03.mp3` 式命名造成含义碎片化。
- 📜 **许可与社区**：TypeScript 代码 MIT，音频与音色包插画 CC0；仓库约 898 stars、49 forks，欢迎贡献并赞助。
- 🌐 **在线体验**：可在 uisfx.com 预览全部音效、提示与音色人格。

---

### [MicroKit UI - 复制粘贴即可使用的 React 与 CSS 微交互](https://microkit.co/)

**原文标题**: [MicroKit UI - Copy-paste React & CSS microinteractions](https://microkit.co/)

MicroKit UI 是一个面向重视交互体验的开发者打造的微交互组件库，提供 54 个可复用的按钮、导航、输入等组件，支持 React 与 CSS，并通过官方 shadcn registry 分发。它强调“细节决定体验”，不提供 npm 包，而是让开发者按需复制、修改并直接用于项目。

- 🧩 组件库定位：MicroKit UI 专注于“每次交互背后的体验”，适合追求细节与动效的开发者。
- 🛠️ 安装方式：通过官方 shadcn registry 使用，例如 `npx shadcn@latest add @microkit/cursor-edge-glow-button`。
- 🎛️ 组件数量：共 54 个微交互，涵盖点击反馈、导航、输入等类型。
- ⚛️ 技术栈：支持 React 和 CSS，并提供 TypeScript 或 JavaScript、CSS 或 Tailwind 的版本选择。
- 📋 使用方式：不发布 npm 包，开发者复制组件代码后即可自由编辑；除图标场景外，不会向 `package.json` 添加依赖。
- 📦 依赖情况：26 个交互无需额外依赖；28 个组件使用 `lucide-react` 图标。
- 🎨 Tailwind 支持：每个交互都提供 Tailwind 版本，兼容 Tailwind v3 和 v4，站点本身基于 Tailwind v4。
- ⚙️ Next.js 兼容：多数组件为无客户端状态的标记与 CSS，可直接用于 Server Component；涉及状态、ref 或事件处理时需添加 `"use client"`。
- 🧾 授权与提交：代码采用 MIT 许可证；支持提交自己的交互，通过表单生成 GitHub issue。
- ⭐ 社区支持：项目鼓励在 GitHub 上点星，帮助更多开发者发现 MicroKit。

---

### [面向静态网站的托管表单，无需后端 — CraftForms Cloud](https://craftforms.app/developers/?utm_source=frontendfocus&utm_medium=newsletter&utm_campaign=ff-2026-10-28-classified)

**原文标题**: [Hosted Forms for Static Sites, No Backend â CraftForms Cloud](https://craftforms.app/developers/?utm_source=frontendfocus&utm_medium=newsletter&utm_campaign=ff-2026-10-28-classified)

overview summary  
CraftForms 让静态网站无需后端即可嵌入表单：通过可视化编辑器搭建表单，粘贴两行 HTML 即可收集不限量提交，并支持实时价格、预订、定金、自定义代码提交和无验证码反垃圾。

- 🛠️ 无需后端：在可视化编辑器中建表单，粘贴两行 HTML 到任意静态站点即可运行。
- ♾️ 免费计划也可无限收集提交，并支持预订、实时价格和定金。
- 🔐 每个表单绑定网站密钥，防止他人复制表单到自己的网站。
- ⚡ 字段和价格运行时加载，编辑器修改后静态站点立即生效，无需重建。
- 🧪 支持 localhost/127.0.0.1 测试，任意端口可用，且不占用套餐网站名额。
- 🧩 兼容 Astro、Hugo、Eleventy、Next.js 静态导出、Cloudflare、Netlify、Vercel 等输出 HTML 的环境。
- 💻 也可自建表单并通过 fetch() 以 JSON 提交，显示自定义感谢信息。
- 🛡️ 无验证码反垃圾：嵌入表单检测真实填写行为，并按地址和表单限流。
- 🆓 Free：€0，1 个表单、1 个网站，每月 100 封通知邮件，无支付和文件上传。
- 💳 Solo：€6/月，首 30 天免费，25 个表单、1 个网站，支持自有 Stripe/PayPal 支付和文件上传。
- 🏢 Studio：€22/月，200 个表单、25 个网站，适合代理机构，含 PDF 构建器。
- ⚠️ 当前限制：无可分享表单链接；仅内置 Mailchimp 和 Brevo 集成；不支持普通 HTML form action 提交。
- 🚀 免费开始，无需信用卡；注册并确认邮箱后即可建表单并在开发服务器测试。

---

### [](https://developer-api.foxit.com/developer-blogs/api-guides-tutorials/pdf-editor-api-programmatic-editing/?utm_source=draftdev&utm_medium=newsletter&utm_campaign=frontendfocus_20261028)

**原文标题**: [Foxit PDF Editor API: Programmatic Editing at Scale](https://developer-api.foxit.com/developer-blogs/api-guides-tutorials/pdf-editor-api-programmatic-editing/?utm_source=draftdev&utm_medium=newsletter&utm_campaign=frontendfocus_20261028)

文章介绍 2026 年面向 AI 代理的 10 款 PDF MCP 服务器，比较免费本地阅读器与可转换、编辑和保护文件的云 API，帮助按任务选择合适方案，并重点关注文档去向、完整工作流成本及连接前的安全缺口。

- 📄 并非所有 PDF MCP 服务器都能满足 AI 代理需求，需根据具体任务匹配。
- 🧰 指南比较 10 种方案，覆盖从免费本地阅读器到云端 API。
- 🔄 云 API 可完成文件转换、编辑和保护等操作。
- 📍 评估重点包括文档发送位置、完整工作流成本，以及连接前需弥补的安全缺口。

---

### [](https://charliegerard.dev/blog/overgrown-extension/)

**原文标题**: [Overgrown, when plants invade your abandoned tabs | Charlie Gerard | Senior research engineer & Creative Technologist Charlie Gerard | Senior research engineer & Creative Technologist](https://charliegerard.dev/blog/overgrown-extension/)

Charlie Gerard 将“植物过度生长”的创意应用到浏览器标签页，开发了一个有趣的 Chrome 扩展：长期未查看的标签会被藤蔓覆盖，用户需用鼠标划掉植物才能重新操作页面。

- 🌿 创作灵感来自“Overgrowth”一词，联想到末日场景中植物侵占废弃建筑，并进一步延伸到被遗忘的浏览器标签页。
- ⏱️ 每个标签都有“忽视计时器”：标签不在视野中时计时，正在查看时暂停。
- 🌱 标签被忽视越久，植物会从边缘向中心生长得越多。
- 🚫 当标签被覆盖超过 5% 时，页面会被藤蔓“封锁”，仍可滚动，但不能点击、选择或拖拽内容。
- 🖱️ 用户需用鼠标拖拽划断藤蔓；降到 5% 时残余植物会脱落，若再次忽视标签则重新生长。
- 🔪 可选择生锈砍刀、电锯或火焰喷射器作为“武器”，也能调整标签被完全覆盖所需时间。
- 😅 作者曾考虑禁止关闭过度生长的标签，直到清除植物为止，但因太烦人而放弃。
- 🧩 扩展代码分为三部分：background.js 管理标签生命周期；popup 处理时间设置、武器选择、标签列表与状态；content 负责植物/武器 SVG、生长定位、忽视计时和音效。
- 🪚 作者希望借此重新开始做小项目；目前新电脑上只开了 22 个标签，其中 14 个已完全被植物覆盖。虽然不一定让人更常阅读标签，但清理藤蔓让回归标签更有趣。

---

### [](https://github.com/charliegerard/Overgrown)

**原文标题**: [GitHub - charliegerard/Overgrown: A Chrome extension that lets plants invade your abandoned tabs the longer you leave them unread. To get the page back, you have to slash through the plants with your mouse, as if trying to open an overgrown door. · GitHub](https://github.com/charliegerard/Overgrown)

Overgrown 是 charliegerard 的 Chrome 扩展开源仓库，用植物蔓延未读标签页的方式来提醒你处理闲置页面；要恢复页面，需要用鼠标划开植物。

- 🌿 核心机制：标签页越久未读，植物越会侵占页面，需用鼠标划除植物，像打开杂草丛生的门。
- 🚫 当标签页被植物覆盖超过 5% 时，后面的页面无法使用。
- 🧩 安装方式：下载仓库中的 `dist` 文件夹，在 `chrome://extensions` 开启开发者模式，点击“加载已解压的扩展程序”并选择 `dist/`。
- 📊 仓库公开，约有 81 stars、2 forks、1 watcher、2 commits。
- 📁 主要包含 `dist`、`public`、`src`、`popup.html`、`package.json` 及 Vite 配置文件。
- 📝 README 提供扩展演示、安装说明和作者博客文章链接，便于进一步了解。

---

