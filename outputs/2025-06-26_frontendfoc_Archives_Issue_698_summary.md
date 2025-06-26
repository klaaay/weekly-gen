### [前端聚焦第 698 期：2025 年 6 月 25 日](https://frontendfoc.us/issues/698)

**原文标题**: [Frontend Focus Issue 698: June 25, 2025](https://frontendfoc.us/issues/698)

- 🚀 纯 CSS 实现滚动驱动动画指南：介绍使用 CSS 的 scroll() 和 view() 函数创建滚动动画，无需 JavaScript，包含进度条和视口元素动画的代码示例，并提及可访问性和运动注意事项。  
- 🤖 网络机器人与检测技术简史：概述机器人与检测技术的演变，涵盖 IP 信誉、指纹识别、无头浏览器漏洞、代理检测、验证码、行为分析等内容。  
- ♿ 成为无障碍专家：通过更新的深度视频课程学习网页无障碍知识，包括语义 HTML、ARIA 标签、焦点样式、颜色对比等。  
- ⚡ Astro 5.10 发布：主要亮点是响应式图片功能正式发布，新增实验性动态内容获取功能，并改进了 CSP 支持。  
- 🦊 Firefox 140.0 新特性：新增垂直标签功能，支持 Custom Highlight API 和 SVG fetchpriority 属性等。  
- 📊 简讯：JSON 模块脚本现已广泛可用；Firefox 扩展政策 8 月更新；State of CSS 调查还剩一周。  
- 🍏 CSS 实现液态玻璃效果：展示用 CSS 模拟苹果液态玻璃设计语言，兼容性有限但实验性强。  
- 🔍 浅析 Chrome 137 的 CSS if() 函数：介绍语法、工作原理及与其他属性的搭配使用。  
- 🔐 OAuth 工作原理：实用指南，包含代码示例、安全提示和第三方集成解析。  
- 🎨 CSS 颜色全解析：深入讲解 CSS 颜色函数（如 lab() 和 oklch()）的技术细节与应用。  
- ⚖ CSS 层、BEM 与工具类对比：探讨如何避免特异性问题，减少!important 的使用。  
- 📸 JPEG 成为网络图像标准的历史：回顾 JPEG 如何成为主流格式及其技术背景。  
- 👀 改进 Intersection 与 Mutation Observers 的 API：简化使用方式的代码重构方案。  
- 🛠 工具与资源：包括 SVG 背景生成器、语法高亮自定义元素、AI 代理前端安全方案、浏览器自动化工具、WCAG 颜色对比检查器等。

---

### [仅用 CSS 实现滚动驱动动画指南 | WebKit](https://webkit.org/blog/17101/a-guide-to-scroll-driven-animations-with-just-css/)

**原文标题**: [  A guide to Scroll-driven Animations with just CSS | WebKit](https://webkit.org/blog/17101/a-guide-to-scroll-driven-animations-with-just-css/)

CSS 滚动驱动动画指南：仅用 CSS 实现滚动触发动画效果  

- 🚀 **CSS 动画的演进**：从 2007 年简单的颜色渐变到如今复杂的滚动驱动动画，无需依赖第三方库或 JavaScript。  
- 🛠️ **三大核心组件**：  
  - **目标元素**：页面中需要动画的对象（如进度条、图片）。  
  - **关键帧**：定义动画效果（如宽度变化、滑动淡入）。  
  - **时间轴**：通过`scroll()`或`view()`关联滚动行为与动画进度。  
- 📜 **滚动时间轴（`scroll()`）**：动画进度与用户滚动直接绑定（如底部进度条随滚动延伸）。  
- 👀 **视图时间轴（`view()`）**：动画在元素进入视口时触发（如图片滑动进入后固定）。  
- ⚙️ **动画范围控制**：通过`animation-range`调整动画起止位置（如设为`0% 50%`让动画中途停止）。  
- ♿ **无障碍考虑**：使用`@media not (prefers-reduced-motion)`避免对敏感用户造成不适。  
- 🔧 **进阶自定义**：支持调整滚动轴（`block`/`inline`）和滚动容器（`root`/`self`）。  
- 🌟 **浏览器支持**：Safari 26 beta 已支持，可即时体验效果。  
- 📢 **反馈与交流**：作者鼓励通过社交媒体分享实践成果或提交问题至 WebKit 团队。  

（代码示例和完整实现细节可参考原文。）

---

### [网络机器人简史与检测技术 · OlegWock](https://sinja.io/blog/bot-or-not)

**原文标题**: [A short history of web bots and bot detection techniques · OlegWock](https://sinja.io/blog/bot-or-not)

本文概述了网络机器人和机器人检测技术的发展历程，从简单的机器人脚本到复杂的检测技术，以及两者之间的持续对抗。

- 🤖 最简单的机器人可以通过 HTTP 请求访问网站，但容易被检测，例如通过 User-Agent 等 HTTP 头信息。
- 🌐 IP 信誉和代理：使用云服务 IP 容易被检测，因此机器人需要使用住宅或移动代理来隐藏真实来源。
- 🔍 TCP 指纹识别：不同操作系统在 TCP 协议处理上的差异可用于检测机器人。
- 🔒 TLS 指纹识别：TLS 握手过程中的加密套件和扩展信息也可用于识别客户端操作系统。
- 📜 JavaScript 检测：通过执行 JavaScript 收集浏览器环境信息，检测机器人。
- 🖥️ 无头浏览器：如 Selenium、Puppeteer 等工具可以模拟真实浏览器，但仍可能被检测。
- 🆕 新型无头模式：Chrome 的新无头模式更接近真实浏览器，减少了被检测的风险。
- 🎭 行为分析：通过分析鼠标移动、键盘输入等行为模式，检测机器人。
- 🧩 高级行为分析：利用 AI 模型分析大量行为数据，识别机器人模式。
- ✅ 验证码：如 reCAPTCHA 等挑战用于区分人类和机器人，但可能被外包人工解决。
- ⏱️ 工作量证明：通过要求客户端完成一定计算量来增加机器人成本。
- 🕵️ 代理检测：通过延迟、WebRTC 泄漏、DNS 泄漏等技术检测代理使用。
- 🕰️ 时区检测：比较 IP 地理位置和浏览器时区，检测代理使用。
- 📚 进一步阅读：推荐 incolumitas.com 等资源深入了解该主题。

---

### [Astro 5.10 | Astro](https://astro.build/blog/astro-5100/)

**原文标题**: [Astro 5.10 | Astro](https://astro.build/blog/astro-5100/)

Astro 5.10 引入了多项新功能和改进，包括实验性的实时内容集合、稳定的响应式图片、CSP 改进以及可定制的 Cloudflare Workers 入口点。

- 🚀 **实验性实时内容集合**：支持在运行时获取内容，适用于频繁变化或需要个性化的数据。
- 🖼️ **响应式图片稳定版**：自动生成优化的 `srcset` 和 `sizes` 属性，提升页面加载性能。
- 🔒 **CSP 改进**：支持生成 CSP 头部，提升安全性和性能。
- ☁️ **可定制的 Cloudflare Workers 入口点**：支持自定义入口文件，便于使用 Cloudflare Workers 的高级功能。
- 🔄 **升级指南**：提供了自动和手动升级的方法，推荐使用 `@astrojs/upgrade` CLI 工具。
- 🛠️ **错误处理和类型安全**：实时内容集合提供明确的错误处理和类型安全 API。
- 📚 **社区贡献**：感谢众多贡献者的代码和文档改进。

---

### [内容安全策略（CSP）- HTTP | MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CSP)

**原文标题**: [Content Security Policy (CSP) - HTTP | MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CSP)

内容安全策略（CSP）是一种安全功能，通过向浏览器发送指令来限制网站代码的行为，主要用于防御跨站脚本（XSS）等攻击。

- 🛡️ **CSP 的核心作用**：控制资源加载（如 JavaScript），防御 XSS 攻击，同时可防止点击劫持和强制 HTTPS 加载。
- 📜 **策略传递方式**：通过 HTTP 响应头`Content-Security-Policy`或 HTML 的`<meta>`标签设置，但后者功能有限。
- 🔧 **指令结构**：由多个分号分隔的指令组成，例如`default-src 'self'; img-src example.com`，分别限制默认资源和图片的加载来源。
- ⚠️ **XSS 防护机制**：禁用内联脚本、`eval()`等危险 API，推荐使用随机数（nonce）或哈希（hash）验证脚本合法性。
- 🔒 **严格 CSP（Strict CSP）**：基于 nonce 或 hash 的指令更安全，避免传统白名单策略的漏洞，例如`script-src 'nonce-{随机值}'`。
- 🌐 **第三方脚本处理**：通过`strict-dynamic`关键字允许受信任脚本动态加载其他资源，但需谨慎使用以降低风险。
- 🖼️ **点击劫持防护**：使用`frame-ancestors 'none'`阻止页面被嵌入到 iframe 中。
- 🔄 **不安全请求升级**：`upgrade-insecure-requests`自动将 HTTP 资源请求升级为 HTTPS，解决混合内容问题。
- 📊 **测试与报告**：通过`Content-Security-Policy-Report-Only`头测试策略，利用 Reporting API 或`report-uri`收集违规报告。
- 🔧 **代码改造建议**：替换内联事件处理器为`addEventListener()`，移除`javascript:` URL 等不安全模式。

---

### [Firefox 140.0 版本全新功能、更新与修复一览](https://www.mozilla.org/en-US/firefox/140.0/releasenotes/)

**原文标题**: [Firefox  140.0, See All New Features, Updates and Fixes](https://www.mozilla.org/en-US/firefox/140.0/releasenotes/)

Firefox 140.0 版本于 2025 年 6 月 24 日发布，新增多项功能并修复问题，同时提供多平台下载支持。

- 🆕 **新功能**  
  - 垂直标签页：可调整固定标签页区域大小，优化访问效率。  
  - 自定义搜索引擎：支持手动添加更多搜索引擎。  
  - 扩展工具栏自定义：可隐藏扩展快捷方式。  
  - 标签页卸载功能：右键卸载标签页以减少内存占用。  
  - 智能全页翻译：优先翻译当前可视区域内容，提升速度。  
  - 阿拉伯语版本内置拼写检查词典。  
  - 意大利、波兰和奥地利启用地址自动填充。  

- 🛠️ **修复与变更**  
  - 多项安全性修复。  
  - 移除 Pocket 工具栏图标及新标签页集成（服务已关闭）。  
  - 企业版政策更新详见《Firefox for Enterprise 140 发布说明》。  

- 💻 **开发者更新**  
  - 检查器面板搜索功能增强，支持 DOM 元素排序和伪选择器状态。  
  - 新增`aria-keyshortcuts`、`CookieStore API`、`Custom Highlight API`支持。  
  - 私有浏览模式现支持 Service Workers。  
  - 统一`<h1>`元素的用户代理样式。  
  - 转义 HTML 属性中的`<`和`>`符号以防范 mXSS 攻击。  

- ⚠️ **已知问题**  
  - 部分深色主题可能导致侧边栏文本对比度问题（可通过内置深色主题临时解决）。  

- 👏 **社区贡献**  
  - 18 名新志愿者开发者参与代码提交，列举了主要贡献者及对应 Bug 编号。  

- ⬇️ **下载支持**  
  - 提供 Windows（含 ARM64/MSI）、macOS、Linux（32/64 位）、Android/iOS 版本下载。  
  - 不再支持 Windows 8.1 及以下、macOS 10.14 及以下系统，建议使用 ESR 版本。  

- 📌 **其他资源**  
  - 包含完整版本变更日志、新闻稿及 Firefox 支持页面链接。

---

### [Firefox 140 开发者版 - Mozilla | MDN](https://developer.mozilla.org/en-US/docs/Mozilla/Firefox/Releases/140)

**原文标题**: [Firefox 140 for developers - Mozilla | MDN](https://developer.mozilla.org/en-US/docs/Mozilla/Firefox/Releases/140)

Firefox 140 于 2025 年 6 月 24 日发布，为开发者带来多项功能更新与改进。

- 🎨 **CSS 支持**：新增 CSS Custom Highlight API，允许通过 JavaScript 定义文本范围并应用高亮样式（`::highlight`伪元素）。  
- 🗑️ **移除功能**：取消嵌套在分节元素中`<h1>`的 UA 样式，统一字体大小。  
- 🖼️ **SVG 增强**：支持`fetchpriority`属性，优化外部资源加载优先级（适用于`<feimage>`、`<image>`和`<script>`）。  
- 🍪 **API 更新**：引入 Cookie Store API，提供基于 Promise 的异步 cookie 管理（主线程和服务 Worker 均支持）。  
- 🔒 **安全改进**：HTML 序列化时自动转义属性中的`<`和`>`为`&lt;`/`&gt;`，防止注入攻击。  
- 🖱️ **DOM 事件**：新增`pointerrawupdate`事件，支持高精度指针输入处理。  
- 🚫 **废弃内容**：移除`MutationEvent`及相关事件（如`DOMSubtreeModified`）。  
- 🤖 **WebDriver 优化**：修复 Actions 命令超时问题，新增容器安全设置参数`acceptInsecureCerts`及导航事件`browsingContext.navigationCommitted`。  
- 🔧 **扩展开发**：`cookies.set()`默认`sameSite`值改为`unspecified`。  
- 🧪 **实验性功能**：包括`Notification.maxActions`、`<dialog>`的`closedBy`属性、`Atomics.waitAsync()`等（需手动启用）。  

（注：文末版本历史与贡献信息未纳入摘要）

---

### [JSON 模块脚本现已成为基线新功能  |  Blog  |  web.dev](https://web.dev/blog/json-imports-baseline-newly-available?hl=en)

**原文标题**: [JSON module scripts are now Baseline Newly available  |  Blog  |  web.dev](https://web.dev/blog/json-imports-baseline-newly-available?hl=en)

现代浏览器现已全面支持 JSON 模块脚本和导入属性，简化了 JSON 文件的导入流程。

- 🚀 现代浏览器已支持 JSON 模块脚本和导入属性，无需再通过复杂方法导入 JSON 文件。  
- 📜 示例代码展示了如何通过`import`语句直接导入 JSON 文件，并立即使用解析后的数据。  
- 🔍 使用`with { type: "json" }`声明可确保浏览器正确处理 JSON 文件，避免 MIME 类型错误。  
- ⚠️ 若省略类型声明，浏览器会默认导入 JavaScript 模块，可能导致请求失败。  
- 📚 更多细节可参考 HTML 规范中的 JSON 模块脚本处理部分。  
- ©️ 内容遵循 Creative Commons 4.0 许可，代码示例遵循 Apache 2.0 许可。

---

### [获取失败](https://frontendfoc.us/link/170843/web)

**原文标题**: [Failed to retrieve](https://frontendfoc.us/link/170843/web)

无法总结：获取内容失败，状态码 403。

---

### [CSS 2025 现状](https://survey.devographics.com/en-US/survey/state-of-css/2025?source=frontendfocus)

**原文标题**: [State of CSS 2025](https://survey.devographics.com/en-US/survey/state-of-css/2025?source=frontendfocus)

overview summary  
该内容主要介绍了 2025 年 CSS 调查的背景、目的、参与方式以及常见问题解答，同时呼吁开发者参与并支持翻译工作。  

- 🐌 2025 年 CSS 调查的核心愿望：减缓创新节奏，让开发者有时间巩固和掌握近年新增的 CSS 功能（如子网格、`:has()`、滚动驱动动画等）。  
- 📊 调查目标：追踪新特性的采用情况，帮助开发者和技术公司决策技术方向，并为浏览器厂商提供优先级参考。  
- ⏱️ 预计耗时：15-20 分钟，所有问题均可跳过，适合任何使用 CSS 的人群（职业、学生或爱好者）。  
- 🌍 开放数据：所有收集的数据将公开，供开发者或企业使用，浏览器厂商也会参考以调整开发重点。  
- 📅 时间安排：2025 年 6 月 1 日至 7 月 1 日开放调查，结果将在结束后不久发布。  
- 👥 组织方：由 Devographics 联合贡献者、翻译志愿者共同运营，设计过程开放透明，社区和浏览器厂商参与。  
- ❓ 更多信息：可通过公告帖了解详情，并提供多语言翻译支持（列举了包括简体中文在内的多种语言翻译者）。  
- 🤝 翻译协助：呼吁更多人帮助翻译调查内容，并列出了已支持的语言和贡献者。

---

### [液态玻璃，但用 CSS 实现 | Atlas Pup 实验室博客](https://atlaspuplabs.com/blog/liquid-glass-but-in-css)

**原文标题**: [Liquid Glass, but in CSS | Atlas Pup Labs Blog](https://atlaspuplabs.com/blog/liquid-glass-but-in-css)

Apple 在 WWDC25 发布了名为"Liquid Glass"的新设计语言，作者尝试用 CSS 实现类似效果。

- 🍎 Apple 在 WWDC25 开发者大会上发布了名为 Liquid Glass 的新设计语言  
- 💻 作者探索用 CSS 实现类似效果，但仅兼容 Chrome 浏览器  
- ✨ 效果分解：镜面高光、模糊处理、色彩滤镜和折射模拟  
- 📐 使用 CSS 的 box-shadow 创建边缘高光效果  
- 🔍 通过 backdrop-filter 实现模糊和色彩调整  
- 🌀 利用 SVG 滤镜模拟玻璃折射效果  
- 🎨 创建失真映射图来扭曲背景内容  
- 🌈 添加色差效果模拟光线折射  
- ⚠️ 目前无法在 Safari/Firefox 实现完整效果  
- 🚫 多个玻璃元素会导致性能问题

---

### [轻轻探讨 Chrome 137 中的 CSS if() 函数 | CSS-Tricks](https://css-tricks.com/lightly-poking-at-the-css-if-function-in-chrome-137/)

**原文标题**: [Lightly Poking at the CSS if() Function in Chrome 137 | CSS-Tricks](https://css-tricks.com/lightly-poking-at-the-css-if-function-in-chrome-137/)

CSS if() 函数在 Chrome 137 中正式发布，这是 CSS 中一种新的条件语句实现方式，允许在单行中根据多个条件返回结果。

- 🚀 **快速开发**：CSS if() 函数从提案到 Chrome 实现仅用了不到一年时间，速度远超预期。  
- 🔍 **语法解析**：if() 支持 style()、media() 和 supports() 等条件判断，并可嵌套多个条件语句。  
- 💡 **基本用法**：通过条件判断返回不同的样式值，例如 `color: if(style(--theme: dark): oklch(52% 0.18 140); else: oklch(65% 0.05 220))`。  
- 📜 **语法演变**：最初的提案语法较简单，最终实现支持更复杂的多条件分支和默认值（else）。  
- 🧩 **可读性优化**：多条件嵌套可能导致代码混乱，建议通过换行和缩进提升可读性。  
- 🌐 **功能扩展**：支持类似 @supports 和 @media 的功能，例如 `supports(backdrop-filter: blur(10px))` 或 `media(width >= 768px)`。  
- ⚠️ **兼容性限制**：目前仅 Chrome 137+ 支持，其他浏览器尚未跟进。  
- 🔮 **未来展望**：社区已开始探索实际用例，反馈将推动功能进一步完善。

---

### [类型：`if()` | Can I use... HTML5、CSS3 等支持表格](https://caniuse.com/mdn-css_types_if)

**原文标题**: [types: `if()` | Can I use... Support tables for HTML5, CSS3, etc](https://caniuse.com/mdn-css_types_if)

全球 47.71% 的浏览器支持`if()`类型，但不同浏览器和版本的支持情况差异显著。

- 🌍 **全球支持率**：47.71% 的浏览器支持`if()`类型。  
- 🚫 **IE**：所有版本均不支持。  
- ✅ **Edge**：仅 137 版本开始支持。  
- 🚫 **Firefox**：所有版本均不支持。  
- ✅ **Chrome**：137 版本及以上支持。  
- 🚫 **Safari**：所有版本均不支持，TP 版本支持情况未知。  
- 🚫 **Opera**：所有版本均不支持。  
- 🚫 **Safari iOS**：所有版本均不支持。  
- ❓ **Opera Mini/Android UC/QQ/Baidu/KaiOS**：支持情况未知。  
- ✅ **Android Browser/Chrome Android**：137 版本开始支持。  
- 🚫 **Firefox Android/Samsung Internet**：不支持。

---

### [OAuth 工作原理](https://clerk.com/blog/how-oauth-works?utm_source=cooper-press&utm_medium=newsletter&utm_campaign=oauth&utm_content=06-25-25-fef&dub_id=2VvBk0kAZcQfw84W)

**原文标题**: [How OAuth Works](https://clerk.com/blog/how-oauth-works?utm_source=cooper-press&utm_medium=newsletter&utm_campaign=oauth&utm_content=06-25-25-fef&dub_id=2VvBk0kAZcQfw84W)

OAuth 是一种开放授权标准，允许第三方应用在无需用户提供密码的情况下访问其部分数据。本文通过实际代码示例和安全最佳实践，详细解释了 OAuth 的作用机制，特别是授权码流程（Authorization Code Flow）。

- 🔐 OAuth 允许第三方应用访问用户数据而无需共享密码，遵循最小权限原则。
- 🔄 授权码流程（Authorization Code Flow）是 OAuth 的核心机制，涉及多个步骤以确保安全性。
- 💻 文章提供了实际代码示例，展示如何实现 OAuth 流程，而不仅仅是理论讲解。
- 🛡️ 安全措施包括 PKCE、state 参数等，以防止 CSRF 攻击和其他安全威胁。
- 📱 公共客户端（如移动应用和单页应用）使用 PKCE 替代 client_secret 以增强安全性。
- 🔄 动态客户端注册（Dynamic Client Registration）允许通过 API 注册 OAuth 客户端，但存在安全风险。
- 🔗 OAuth 与 OIDC（OpenID Connect）结合使用，提供用户身份信息（如姓名、电子邮件等）。
- 🛠️ Clerk 提供了内置的 OAuth 授权服务器，支持自动处理安全措施如 PKCE 和 state 参数。
- 📚 文章还涵盖了常见问题，如令牌刷新、令牌类型（JWT 或不透明令牌）和权限撤销。

---

### [用 CSS 为万物上色 | CSS-Tricks](https://css-tricks.com/color-everything-in-css/)

**原文标题**: [Color Everything in CSS | CSS-Tricks](https://css-tricks.com/color-everything-in-css/)

CSS 中的颜色功能全面解析  

- 🌈 CSS 颜色功能包括 color()、hsl()、lab()、lch()、oklab()、oklch() 和 rgb() 等  
- 📚 颜色空间（如 sRGB、CIELAB、Oklab）是颜色的坐标系统映射，决定可用颜色范围  
- 🎨 颜色模型（如 RGB、HSL）通过数学描述颜色，需结合颜色空间才能确定具体颜色  
- 🔍 色域（Color Gamut）指颜色空间或设备能显示的颜色范围，超出范围称为“超出色域”  
- 🖥️ 现代 CSS 支持通过 color() 函数访问更多颜色空间（如 display-p3、prophoto-rgb）  
- 📊 CIEXYZ 颜色空间是定义其他颜色空间的基础，用于描述和转换不同颜色空间  
- 🔧 CSS 中新增的 color-mix() 和 contrast-color() 等函数提供了更强大的颜色处理能力  
- 📱 不同颜色空间（如 Oklab）在感知均匀性上表现更好，适合现代广色域显示设备

---

### [CSS 层叠层与 BEM 与实用类：特异性控制 —— Smashing Magazine](https://www.smashingmagazine.com/2025/06/css-cascade-layers-bem-utility-classes-specificity-control/)

**原文标题**: [CSS Cascade Layers Vs. BEM Vs. Utility Classes: Specificity Control — Smashing Magazine](https://www.smashingmagazine.com/2025/06/css-cascade-layers-bem-utility-classes-specificity-control/)

CSS 特异性控制方法比较：BEM、工具类和层叠层

- 🎯 文章探讨了 CSS 特异性控制的三种方法：BEM、工具类和 CSS 层叠层（@layer），并比较了它们的优缺点。
- 🔍 CSS 特异性问题常见于样式覆盖失败的情况，通常开发者会使用!important，但这并非最佳实践。
- 📚 特异性基础：浏览器通过 CSS 层叠算法决定哪个样式声明应用于元素，随着项目扩大，特异性问题会加剧。
- ⚔️ 开发者常用方法：
  - BEM：通过命名约定简化特异性。
  - 工具类：通过原子类避免特异性。
  - 层叠层：通过分层管理特异性。
- 🧩 BEM：
  - 优点：结构清晰，特异性低且一致。
  - 缺点：类名冗长，复用性受限，命名困难。
- 🧱 工具类：
  - 优点：开发速度快，特异性一致。
  - 缺点：HTML 冗长，全局样式修改困难。
- 🏗️ 层叠层：
  - 优点：完全控制样式优先级，可与其他方法结合。
  - 缺点：可能被滥用，需要深入理解 CSS。
- 🔄 三者比较：
  - BEM 适合设计系统和团队协作。
  - 工具类适合快速开发和原型。
  - 层叠层适合遗留代码和复杂项目。
- 🤝 结合使用：层叠层可与 BEM 或工具类结合，优化特异性控制。
- 🏆 结论：没有绝对最佳方法，应根据项目需求选择或组合使用，保持特异性低并利用层叠层管理优先级。

---

### [JPEG 如何成为互联网的图像标准 - IEEE Spectrum](https://spectrum.ieee.org/jpeg-image-format-history)

**原文标题**: [How JPEG Became the Internet’s Image Standard - IEEE Spectrum](https://spectrum.ieee.org/jpeg-image-format-history)

JPEG 格式在三十年前成为互联网上分享数字照片的主导方式，至今仍在网络中占据重要地位。

- 📅 **历史背景**：JPEG 格式在三十年前成为互联网上分享数字照片的标准。  
- 🌐 **网络主导**：至今仍是网络上最常用的图像格式之一。  
- 📸 **数字照片**：专为数字照片的压缩和分享设计，平衡了文件大小和图像质量。  
- 🔍 **技术优势**：高效的压缩算法使其在互联网传输中表现出色。  
- 🏆 **长期影响**：尽管有新技术出现，JPEG 因其兼容性和普及度仍占据主导地位。  
- ✍️ **作者观点**：Ernie Smith 通过其长期运行的通讯 Tedium 探讨了这一技术的持久影响。

---

### [更好的交集与变异观察者 API | CSS-Tricks](https://css-tricks.com/a-better-api-for-the-intersection-and-mutation-observers/)

**原文标题**: [A Better API for the Intersection and Mutation Observers | CSS-Tricks](https://css-tricks.com/a-better-api-for-the-intersection-and-mutation-observers/)

概述：本文介绍了如何简化 JavaScript 中的 `MutationObserver` 和 `IntersectionObserver` API 的使用方法，通过重构代码使其更易用，并提供了相关示例和实用工具库推荐。

- 🛠️ 文章展示了如何将复杂的 `MutationObserver` 和 `IntersectionObserver` API 重构为更简洁的形式，类似于之前对 `ResizeObserver` 的改造。  
- 📝 `MutationObserver` 的 API 与 `ResizeObserver` 类似，可以通过回调或事件监听模式使用，并支持多种观察选项。  
- 🔄 `IntersectionObserver` 的 API 也类似，但需要在创建时传入选项，而不是在观察时传入。  
- ⏹️ 提供了断开观察者的方法，如 `disconnect` 和 `unobserve`，并确保在断开前处理未处理的记录。  
- 📦 推荐使用 Splendid Labz 的实用工具库，其中包含简化后的观察者方法，支持同时观察多个元素。  
- 🎓 文章还提到作者提供的 JavaScript 课程，强调重构技能的重要性，并鼓励读者学习如何构建和优化实际组件。  
- 🔗 最后，文章以推广 Splendid Labz 的工具库和作者的课程结束，邀请读者进一步探索。

---

### [为什么可视化网站构建工具没有流行起来 - YouTube](https://www.youtube.com/watch?v=BK_71QjkZmA)

**原文标题**: [Why visual website builders didn't take off - YouTube](https://www.youtube.com/watch?v=BK_71QjkZmA)

关于 YouTube 的相关信息与链接  
- 📢 关于：了解 YouTube 的基本信息  
- 🗞️ 新闻：查看最新动态与公告  
- ©️ 版权：版权相关声明与政策  
- 📩 联系我们：提供联系方式  
- 🎨 创作者：创作者资源与支持  
- 💼 广告：广告合作与推广  
- 👩💻 开发者：开发者工具与 API  
- 📜 条款：使用条款与条件  
- 🔒 隐私：隐私政策与数据保护  
- ⚖️ 政策与安全：平台规范与安全措施  
- 🔧 YouTube 工作原理：平台运作机制  
- 🧪 测试新功能：体验最新功能测试  
- © 2025 谷歌 LLC：版权归属与年份声明

---

### [获取失败](https://frontendfoc.us/link/170854/web)

**原文标题**: [Failed to retrieve](https://frontendfoc.us/link/170854/web)

无法总结：获取内容失败，状态码 403。

---

### [使用 Three.js、GSAP 和 Web Audio API 编写 3D 音频可视化器 | Codrops](https://tympanus.net/codrops/2025/06/18/coding-a-3d-audio-visualizer-with-three-js-gsap-web-audio-api/)

**原文标题**: [Coding a 3D Audio Visualizer with Three.js, GSAP & Web Audio API | Codrops](https://tympanus.net/codrops/2025/06/18/coding-a-3d-audio-visualizer-with-three-js-gsap-web-audio-api/)

使用 Three.js、GSAP 和 Web Audio API 创建一个 3D 音频可视化工具，其中包含一个发光的 3D 球体，根据音乐节奏脉动和尖刺，同时 GSAP 可拖动的面板围绕它漂移，具有平滑的惯性动力运动。

- 🎵 通过 Web Audio API 分析音频，实时驱动 3D 球体的脉动和变形。
- 🌐 使用 Three.js 创建 3D 场景，包含动态球体和其他视觉元素。
- 🖥️ 通过自定义 GLSL 着色器实现顶点变形和边缘发光效果。
- 🎨 使用 GSAP 处理平滑动画和用户交互，包括可拖动的 UI 面板和惯性效果。
- 🔧 提供 UI 控制面板，允许用户调整旋转速度、分辨率、失真量等参数。
- 📊 在 UI 中显示音频频谱分析器和终端输出，增强科技感。
- 🚀 通过 GSAP 实现相机动画和面板拖动，增加交互性和沉浸感。
- 🎶 包含多个音轨选择，可视化工具会根据音频的强度和频率实时调整视觉效果。

---

### [JavaScript 破坏了网络（还称之为进步）—— Jono Alderson](https://www.jonoalderson.com/conjecture/javascript-broke-the-web-and-called-it-progress/)

**原文标题**: [JavaScript broke the web (and called it progress) - Jono Alderson](https://www.jonoalderson.com/conjecture/javascript-broke-the-web-and-called-it-progress/)

现代网页因过度依赖 JavaScript 而变得臃肿、低效且难以维护，开发者文化推崇复杂性而非用户体验，导致本应简单的网页变成需要复杂工具链的“应用”。  

- 🐌 **网页性能低下**：现代网站加载缓慢、渲染不稳定，依赖大量 JavaScript，牺牲了用户体验。  
- 🔧 **不必要的复杂性**：简单任务（如修改标题）需要多个工程师、框架和构建流程，过度工程化成为常态。  
- 📱 **历史转折点**：2010 年后，为追求“类应用体验”，开发者滥用 JavaScript 框架，但实际效果更差。  
- 👨💻 **开发者优先文化**：工具链优化“开发者体验”（DX），却忽视用户体验（UX），抽象层导致与用户需求脱节。  
- 🏗️ **重复造轮子**：JavaScript 生态正重新实现本由 HTML/CSS 原生支持的功能（如路由、服务端渲染），但更臃肿脆弱。  
- 🔄 **无休止的技术迭代**：技术栈持续变动，团队疲于应对框架更新而非解决用户问题。  
- 🚫 **非技术人员的困境**：营销、SEO 人员因复杂流程无法自主更新内容，开发团队垄断控制权。  
- ✅ **解决方案**：回归基础——服务端渲染、语义化 HTML、按需使用 JavaScript，优先考虑性能与可维护性。  
- 💡 **反思与行动**：开发者应质疑架构选择，拒绝“为技术而技术”，推动以用户结果为导向的简单方案。  

（注：总结保留原文批判框架滥用、呼吁简化的核心观点，省略评论区具体讨论以保持简洁。）

---

### [时尚 SVG 背景，为您的网站与设计添彩 | Mossaik](https://mossaik.app/)

**原文标题**: [stylish SVG Backgrounds for your websites and designs | Mossaik](https://mossaik.app/)

Mossaik 是一款免费工具，帮助用户创建抽象 SVG 图像，适用于网站、移动设备等多种场景，提升视觉吸引力和用户体验。

- 🎨 **创建美丽 SVG 图像**：提供抽象波浪设计，适用于网站、设备背景等，支持 SVG 或 PNG 导出。  
- 🌊 **高度可定制**：可调整波浪数量、角度、颜色及渐变模式，满足个性化需求。  
- 📱 **移动设备优化**：为手机和平板提供轻量高清背景，增添活力与个性化。  
- 💻 **电脑设备适用**：为笔记本和台式机设计，增强视觉体验，营造数字风水氛围。  
- 🌐 **网站设计利器**：通过动态波浪图案提升网站吸引力，高分辨率 SVG 确保画质清晰。  
- 🚀 **免费使用**：无需付费，直接启动编辑器即可开始创作。  
- ✨ **提升用户留存**：独特设计元素降低网站跳出率，增加访客互动。  
- ©️ **版权信息**：由 Gabriel Perales 开发，2024 年起所有权利保留。

---

### [<syntax-highlight>元素 - Web 组件](https://andreruffert.github.io/syntax-highlight-element/)

**原文标题**: [<syntax-highlight> element - Web Component](https://andreruffert.github.io/syntax-highlight-element/)

概述总结  
一个使用 CSS Custom Highlight API 实现语法高亮的自定义元素，支持通过 npm 或 CDN 安装，提供基础主题和语言配置选项。  

- 📦 **安装方式**  
  - 通过 npm 安装：`npm install syntax-highlight-element`  
  - 或通过 CDN 引入 ES 模块  

- 🛠️ **使用方法**  
  - JavaScript 中导入模块或直接使用 CDN 链接  
  - HTML 中通过`<syntax-highlight language="js">`标签指定语言  
  - 需加载主题 CSS（如`prettylights.css`）  

- 🎨 **主题支持**  
  - 当前主题有限，支持自定义或贡献新主题  

- 🌐 **语言配置**  
  - 默认支持`html|css|js`，可通过`language`属性指定  
  - 支持通过`window.she.config`扩展语言和令牌类型  

- 📚 **依赖与鸣谢**  
  - 基于 Prism 的语法分析器  
  - 灵感来自 Bramus Van Damme 的博客文章

---

### [CSS 自定义高亮 API - Web API | MDN](https://developer.mozilla.org/en-US/docs/Web/API/CSS_Custom_Highlight_API)

**原文标题**: [CSS Custom Highlight API - Web APIs | MDN](https://developer.mozilla.org/en-US/docs/Web/API/CSS_Custom_Highlight_API)

CSS Custom Highlight API 允许通过 JavaScript 创建文本范围并用 CSS 样式化，无需影响 DOM 结构。

- 🌟 **功能概述**：CSS Custom Highlight API 提供了一种用 JavaScript 创建文本范围并用 CSS 样式化的方法，适用于文本编辑器和代码编辑器等场景。  
- 🔍 **核心概念**：扩展了浏览器内置的高亮伪元素（如`::selection`），支持自定义`Range`对象，实现更灵活的文本高亮。  
- 🛠 **使用步骤**：  
  1. 创建`Range`对象定义文本范围。  
  2. 为范围创建`Highlight`对象（支持多范围关联）。  
  3. 通过`HighlightRegistry`注册高亮。  
  4. 用`::highlight()`伪元素样式化。  
- 📜 **接口说明**：  
  - `Highlight`：表示一组需样式化的文本范围。  
  - `HighlightRegistry`：通过`CSS.highlights`注册和管理高亮。  
- 🔧 **示例：搜索高亮**：  
  - HTML：输入框和文本内容。  
  - JavaScript：监听输入事件，匹配文本并创建高亮。  
  - CSS：通过`::highlight(search-results)`设置样式。  
- 🌐 **浏览器兼容性**：需检查`api.Highlight`和`api.HighlightRegistry`的支持情况。  
- 📚 **扩展阅读**：相关资源包括 MDN 文档和 CSS 伪元素指南。

---

### [Highlight API：has | Can I use... 支持 HTML5、CSS3 等的兼容性表格](https://caniuse.com/mdn-api_highlight_has)

**原文标题**: [Highlight API: has | Can I use... Support tables for HTML5, CSS3, etc](https://caniuse.com/mdn-api_highlight_has)

Highlight API 的全球使用率为 88.74%，主要浏览器支持情况如下：

- 🌍 全球使用率：88.74%  
- 🚫 IE 6-11：不支持  
- ✅ Edge 105-137：支持  
- 🚫 Firefox 2-139：不支持，✅ 140+：支持  
- � Chrome 4-104：不支持，✅ 105-141：支持  
- 🍏 Safari 3.1-17.1：不支持，✅ 17.2-18.5 及 26.0+：支持  
- 🎭 Opera 10-90：不支持，✅ 91-117：支持  
- 📱 Safari iOS 3.2-17.1：不支持，✅ 17.2-18.5 及 26.0：支持  
- ❓ Opera Mini/UC/QQ/Baidu/KaiOS：支持情况未知  
- 🤖 Android Browser 2.1-4.4.4：不支持，✅ 137：支持  
- 📲 Chrome Android/Firefox Android：✅ 137 支持/🚫 139 不支持  
- 🌟 Samsung Internet 4-19：不支持，✅ 20-28：支持

---

### [GitHub - andreruffert/syntax-highlight-element: 👓 使用 CSS 自定义高亮 API 实现的语法高亮](https://github.com/andreruffert/syntax-highlight-element)

**原文标题**: [GitHub - andreruffert/syntax-highlight-element: 👓 Syntax Highlighting using the CSS Custom Highlight API](https://github.com/andreruffert/syntax-highlight-element)

一个基于 CSS Custom Highlight API 实现的语法高亮 Web 组件，使用 Prism 的标记器，无需为每个标记包裹<span>元素。

- 👓 项目名称：syntax-highlight-element  
- 🌐 功能：利用 CSS Custom Highlight API 实现无 span 包裹的语法高亮  
- 📦 安装方式：支持 npm 安装或 CDN 引入  
- 🛠️ 使用示例：通过<syntax-highlight language="js">标签高亮代码  
- 🎨 主题支持：需加载预设主题（如 prettylights.css），支持自定义主题  
- ⚙️ 配置项：可自定义语言支持（默认 html/css/js）和标记类型  
- 🌍 浏览器依赖：需兼容 CSS Custom Highlight API  
- 📜 许可证：MIT 开源协议  
- ✨ 特色：基于 Prism 标记器，灵感来自 Bramus Van Damme 的博客  
- 📊 项目数据：344 星标，4 分支，2 位贡献者

---

### [保障 AI 代理安全：认证、授权与防御指南 —— WorkOS](https://workos.com/blog/securing-ai-agents?utm_source=cpff&utm_medium=referral&utm_campaign=q22025)

**原文标题**: [Securing AI agents: A guide to authentication, authorization, and defense â WorkOS](https://workos.com/blog/securing-ai-agents?utm_source=cpff&utm_medium=referral&utm_campaign=q22025)

AI 代理的快速发展带来了强大的功能，同时也引入了新的安全风险。本文详细介绍了如何通过认证、授权和防御措施来确保 AI 代理的安全性。

- 🔐 **AI 代理的安全挑战**：与传统软件不同，AI 代理具有自主决策能力，可能带来不可预测的风险，如系统级风险、上下文中毒和缺乏常识性判断。  
- 🛡️ **认证机制**：采用机器对机器（M2M）认证，如 OAuth 2.0 客户端凭证流，确保每个代理都有唯一的身份验证凭据。  
- 🔑 **授权策略**：实施最小权限原则和上下文感知授权，动态调整代理的权限，限制其访问范围。  
- 🚨 **防御措施**：包括输入验证、速率限制、异常检测和网络分段，以防止恶意攻击和代理的异常行为。  
- ⚠️ **防范善意代理的风险**：通过定义安全操作限制、人工审批流程和沙盒测试，避免代理因过度自主而引发问题。  
- 🏢 **WorkOS 的解决方案**：提供企业级基础设施，支持 M2M 认证、细粒度授权、审计日志和异常检测，帮助安全部署 AI 代理。  
- 🔮 **未来展望**：随着 AI 代理的复杂性和自主性提升，安全挑战将持续演变，需构建灵活的安全架构以应对新兴威胁。

---

### [浏览器 MCP - 用 AI 自动化您的浏览器操作](https://browsermcp.io/)

**原文标题**: [Browser MCP - Automate your browser with AI](https://browsermcp.io/)

Browser MCP 是一款浏览器扩展工具，可将 AI 应用与浏览器连接，实现自动化测试和任务执行，提升工作效率并保障隐私安全。

- 🌐 **功能概述**  
  通过 Browser MCP，AI 应用（如 Cursor、Claude）可直接操控浏览器，完成表单填写、数据收集等重复性任务。

- 🧪 **应用场景**  
  - 自动化测试：端到端代码测试、用户流程验证及 UI 元素检查。  
  - ⚙️ 任务自动化：数据采集、表单填充等日常操作。  

- 🔥 **核心优势**  
  - ⚡ 本地运行：无网络延迟，性能更优。  
  - 🔒 隐私保护：浏览器活动仅保留在本地设备。  
  - 👤 保持登录：使用现有浏览器配置，无需重复认证。  
  - 🥷 隐蔽性：模拟真实浏览器指纹，规避基础机器人检测。  

- 🛠️ **使用步骤**  
  1. 安装浏览器扩展  
  2. 配置 MCP 服务器至 AI 应用  
  3. 开始自动化流程  

- 🧰 **支持操作**  
  - 页面导航（🌐）、点击（👆）、拖拽（✋）  
  - 文本输入（🔤）、截图（🖼️）、控制台日志获取（🖥️）等  

- 🤖 **兼容 AI 工具**  
  支持 Cursor、Claude、Windsurf、VSCode 等。  

- ⚡ **开发信息**  
  由 ExtensionStack 构建，提供便捷安装（Chrome 扩展）。

---

### [GitHub - BrowserMCP/mcp：Browser MCP 是一款模型上下文提供器（MCP）服务器，能让 AI 应用控制您的浏览器](https://github.com/browsermcp/mcp)

**原文标题**: [GitHub - BrowserMCP/mcp: Browser MCP is a Model Context Provider (MCP) server that allows AI applications to control your browser](https://github.com/browsermcp/mcp)

Browser MCP 是一个模型上下文提供者（MCP）服务器，允许 AI 应用程序控制用户的浏览器，实现本地自动化操作，保持隐私和登录状态。

- 🌐 **项目简介**：Browser MCP 是一个 MCP 服务器加 Chrome 扩展，用于通过 AI 应用程序自动化控制浏览器。  
- 🚀 **主要特点**：  
  - ⚡ **快速**：本地自动化操作，无网络延迟。  
  - 🔒 **隐私**：所有浏览器活动仅在本地设备上进行，不发送到远程服务器。  
  - 👤 **保持登录**：使用现有浏览器配置文件，保持登录状态。  
  - 🥷 **隐蔽性**：避免基本的机器人检测和 CAPTCHA。  
- 📜 **许可证**：Apache-2.0 许可证。  
- 📊 **项目数据**：2.6k 星标，171 次分叉。  
- 🔧 **开发状态**：核心 MCP 代码已开源，但尚无法独立构建。  
- 🔗 **资源**：官网[browsermcp.io](https://browsermcp.io)，文档和更多信息可参考 README。  
- 💡 **背景**：基于 Playwright MCP 服务器改进，专注于用户现有浏览器配置文件的自动化操作。

---

### [对比报告 - WCAG 颜色对比检查工具](https://contrast.report/)

**原文标题**: [Contrast Report - WCAG Colour Contrast Checker](https://contrast.report/)

好的，请提供需要总结的文本内容，我会按照您要求的格式生成概述和带表情符号的要点列表。  

示例格式：  

这里是文章的概述总结  

- 📌 要点一：关键信息  
- 🔍 要点二：核心内容  
- 💡 要点三：重要细节  

请提供具体文本，我会为您生成相应的总结。

---

### [将文本转换为 SVG 路径 | Text-To-SVG.com](https://text-to-svg.com/)

**原文标题**: [Convert Text to SVG Path | Text-To-SVG.com](https://text-to-svg.com/)

这是一个简单的工具，可将任何文本转换为 SVG 路径。

- ✏️ 输入文本即可转换为 SVG 路径  
- 👀 可查看 SVG 源代码或直接下载 SVG/PNG 文件  
- 🅰️ 提供字体选择功能  
- 📏 可调整字体大小  
- 🎨 支持颜色选择  
- ↔️ 可设置行高百分比  
- ↩️ 支持按字符数自动换行  
- ⚡ 生成 SVG 按钮一键转换  
- 📄 显示生成的 SVG 源代码  
- ⬇️ 提供 PNG/SVG 下载选项

---

### [SlimImg - 图片压缩工具 | 无需上传](https://slimimg.tools/)

**原文标题**: [SlimImg - Image Compression Tool | No Upload Needed](https://slimimg.tools/)

SlimImg.tools 是一款本地图像处理工具，专注于图像压缩和 EXIF 管理，无需上传，保障隐私安全。

- 🖼️ **本地处理**：所有操作在浏览器内完成，无需上传至服务器，确保数据隐私。
- 🔒 **隐私保护**：可一键修改或删除 EXIF、GPS 等敏感元数据，防止信息泄露。
- ⚡ **高效压缩**：自由调整压缩比例，平衡画质与文件大小，显著减小体积。
- 🌐 **提升网站性能**：优化后的图片加速网页加载，改善 SEO 和用户体验。
- 💾 **节省资源**：减小图片体积，节省存储空间和网络流量。
- ✨ **安全分享**：去除敏感信息后分享图片，更安心便捷。
- 📂 **多格式支持**：兼容 JPG、PNG、WebP 等常见格式，支持拖拽或批量上传。

---

### [非 HTML 内容](https://frontendfoc.us/open/698/*%7CUID%7C*?ipx=t)

**原文标题**: [Non-HTML content](https://frontendfoc.us/open/698/*%7CUID%7C*?ipx=t)

无法总结：非 HTML 内容。

---

