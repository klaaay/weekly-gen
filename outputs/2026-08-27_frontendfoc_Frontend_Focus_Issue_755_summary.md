### [](https://ishadeed.com/article/flex-wrap-balance/)

**原文标题**: [Balancing flex items with flex-wrap: balance](https://ishadeed.com/article/flex-wrap-balance/)

本内容阐述了高质量内容分享的核心标准：简洁清晰、包含实例、带来新知，并承诺优质推荐。

- 📌 要点明确，用最少的语言解释清楚，避免冗长
- 🖼️ 每点至少配一个图表或具体例子，帮助理解
- 💡 内容需让人学到新知识，或至少唤醒已有记忆
- 🏆 确保推荐内容质量上乘，用户可放心接收

---

### [](https://nolanlawson.com/2026/08/23/the-asteroid-currently-hitting-frontend-web-development/)

**原文标题**: [The asteroid currently hitting frontend web development | Read the Tea Leaves](https://nolanlawson.com/2026/08/23/the-asteroid-currently-hitting-frontend-web-development/)

overview summary
本文是前端开发者 Nolan Lawson 对 AI 冲击前端开发与前端教育现状的反思。他观察到众多知名前端教育者纷纷退出或转向 AI 话题，甚至自己用 Claude 测试复杂 CSS 性能问题也得到了高质量回答。他认为前端领域正被 AI 快速接管，原因是前端交给 agent 风险低、开发者体验逐渐让位于“agent 体验”、对开发者友好的新标准不再受重视。他提出几个可能的出路：让 agent 理解架构趋势、打造对 agent 友好的网站、以及为 AI 生成的低质量前端提供咨询。全文以“小行星撞地球”作比，表达对行业未来的悲观，但也呼吁同行正视变化并寻找生存之道。

- 🤖 许多顶尖前端教育者（如 Axel Rauschmayer、Josh W. Comeau 等）相继淡出或转向 AI 主题，前端教育生态正被 AI 浪潮重塑。
- 🧠 作者用高难度 CSS 性能优化问题测试 Claude，AI 给出了专业且完整的诊断思路，说明 AI 已能胜任部分前端专家的分析工作。
- ⚠️ 前端相对于后端风险更低、更易替换，因此开发者更放心把前端交给 AI 代理无监督处理。
- 📉 开发者体验（DevExp）正变得不如“Agent 体验”重要，例如 Cursor 和 Viget 从 Solid/Lit 迁回 React，只因为 AI 最熟悉 React。
- 🌍 浏览器标准领域对改善开发者体验的 API（如 shadow DOM、自定义元素）关注度将下降，而真正提升能力的标准会继续受到重视。
- 🧭 作者提出方向之一：AI 代理需要被“教育”理解架构，例如不要滥用 SPA，而应选择 Astro/Eleventy 等 MPA 框架，以减少 token 浪费和复杂 bug。
- 🤝 方向之二：让网站对 AI 代理更友好（如 Vercel 的 is-agentic），本质仍是做好服务端渲染、无障碍和性能，但作者担心这会加速网页被代理取代。
- 🔧 方向之三：为大量 AI 生成的“vibe-coded”低质量前端提供咨询和修复服务，这在短期内可能带来机会，但长期不确定。
- 🦕 作者用“小行星撞地球”和“新冠”作比喻，认为行业必须正视 AI 带来的破坏性变化，盲目回避只会陷入否认。
- 💬 评论区也出现不同声音：有人主张 AI 可当作教学工具来学习，也有人认为后端其实更容易被 AI 接管，而设计、审美等领域较难被 AI 取代。

---

### [](https://www.tigerdata.com/go/trial?utm_source=content-syndication&utm_medium=referral&utm_campaign=frontend-focus-newsletter)

**原文标题**: [Postgres for time-series workloads at any scale. | Tiger Data](https://www.tigerdata.com/go/trial?utm_source=content-syndication&utm_medium=referral&utm_campaign=frontend-focus-newsletter)

Tiger Data 提供基于 Postgres 的时序数据云服务，主打超大规模、弹性伸缩、企业级合规与快速部署，并针对新用户提供免费试用额度。以下是其核心要点：

- 📊 单服务可支撑每日 3 万亿指标、3PB 数据及 1 千万亿数据点的实时时序负载
- 💰 新账户立享 $1000 额度，30 天有效，无需信用卡
- ⚙️ 读写分离支持最多 10 个副本节点，搭配 SSD/S3 分层存储，实现无限扩展与成本优化
- 💡 计算与存储完全解耦，可独立扩缩容，避免为空闲资源付费
- 🔄 多可用区集群具备自动故障转移、时间点恢复和跨区域备份，确保高可用
- 🔐 符合 SOC 2、HIPAA、GDPR 标准，内置加密、SSO、RBAC 及审计日志
- 📉 提供查询钻取与仪表盘，可监控性能与错误，并集成 CloudWatch、Datadog、Prometheus
- ⏱️ 分钟级完成数据库部署，支持 SQL、CLI、Terraform、Cursor 或 Claude Code 管理
- 🔌 无缝接入主流云提供商与 Postgres 生态扩展
- 🛡️ 企业用户享有合同化 SLA、区域数据隔离，以及 24/7 全球专家支持与保障响应时间

---

### [](https://www.matuzo.at/blog/2026/html-boilerplate)

**原文标题**: [My HTML boilerplate in 2026 - Manuel Matuzović](https://www.matuzo.at/blog/2026/html-boilerplate)

这篇文章介绍了作者在 2026 年使用的 HTML 基本模板，逐行解释了每个标签和属性的用途、必要性及最佳实践，并明确区分了必需项与可选项，帮助开发者搭建健壮、响应式、对 SEO 和社交网络友好的页面基础。

- 📄 基础必备：`DOCTYPE`、`lang`、`charset`、`title` 仍是 HTML 文档最核心的必需元素，分别负责兼容模式、自然语言、字符编码和唯一标题。
- 📱 响应式适配：`viewport` 设置宽度为设备宽度；新增的 `text-scale` 元标签可让移动端尊重系统字体缩放，但需充分测试以免布局错乱。
- 🚫 JavaScript 状态：在 `<html>` 上使用 `no-js` 类，再通过内联脚本切换为 `js`，方便为无 JS 环境提供样式或优化组件渲染。
- 🎨 样式引入：使用渲染阻塞 CSS 加载全局样式，并单独提供 `media="print"` 的打印样式表以节省纸张和墨水。
- ⚡ 脚本加载策略：渲染阻塞脚本放在 head 中同步加载；非阻塞脚本使用 `type="module"` 实现延迟执行，兼顾性能。
- 🖼️ 图标三件套：`favicon.ico` 兼顾旧浏览器，SVG favicon 支持矢量缩放和深色模式，`apple-touch-icon` 用于 iOS 主屏。
- 📱 Android 清单：通过 `site.webmanifest` 提供 PWA 或主屏图标信息，其中 maskable 图标需预留约 80% 的安全区。
- 🔍 SEO 优化：`canonical` 防止重复内容，`meta description` 提供搜索摘要；`og:url` 和 `og:image` 则保证社交分享链接预览正确。
- 🐘 联邦宇宙集成：`rel="me"` 验证 Mastodon 个人主页身份，`fediverse:creator` 可在分享时自动标注作者。
- 🤖 LLM 与新技术：通过 `alternate` 提供 Markdown 版本以降低 AI 解析成本；`site.standard.publication` 用于发布到 Atmosphere。
- 🎛️ 可选增强标签：`theme-color`、`preload`、`RSS`、`author`、`viewport-fit`、`interactive-widget` 和 `color-scheme` 可按实际需求灵活添加。

---

### [HTML 可以做到 · Chris Burnell](https://chrisburnell.com/html-can-do-that/)

**原文标题**: [HTML Can Do That · Chris Burnell](https://chrisburnell.com/html-can-do-that/)

overview summary  
- 🧩 HTML 正逐步取代部分 JavaScript 功能，本文展示了纯 HTML 即可实现的动态交互。  
- 💬 `popover` 属性配合 `popovertarget` 可轻松实现弹出层，支持轻触关闭和 Esc 键，无需管理 z-index。  
- 📦 `<dialog>` 元素支持模态框，结合 `popover` 或 JavaScript 的 `.showModal()` / `.close()` 使用。  
- 🎹 通过共享 `name` 属性，多个 `<details>` 可组成手风琴效果，互斥展开。  
- 🎛️ `command` 与 `commandfor` 属性让按钮直接控制 popover 或 dialog，未来还能扩展更多命令。  
- 🖼️ `loading="lazy"` 实现图片懒加载，无需 IntersectionObserver。  
- 🔍 `hidden="until-found"` 允许通过片段链接自动显示隐藏内容，但浏览器支持仍有限。  
- 🎨 原生表单元素（颜色、日期、范围、进度条、仪表）开箱即用，但实现和可访问性欠佳，需谨慎使用。  
- 📝 `<datalist>` 提供原生自动完成建议，但跨输入类型支持不一，可能有坑。  
- ⚠️ 作者提醒：部分新特性尚不成熟，不宜作为决策依据，且需关注无障碍体验。

---

### [](https://developer.mozilla.org/en-US/docs/Mozilla/Firefox/Releases/154)

**原文标题**: [Firefox 154 release notes for developers (Stable) - Mozilla | MDN](https://developer.mozilla.org/en-US/docs/Mozilla/Firefox/Releases/154)

Firefox 154 开发者版本更新摘要，涵盖 CSS、JavaScript、Web API、WebDriver 及扩展开发等多项改进，并新增若干实验性功能。

- 🛠️ 开发者工具：JSON 查看器新增底部面包屑，显示所选条目在 JSON 结构中的位置。
- 🎨 CSS：新增 `sibling-count()` 和 `sibling-index()` 函数，支持 `text-box`、`text-box-edge`、`text-box-trim` 属性以控制文本块方向间距。
- 💻 JavaScript：新增 `Iterator.prototype.includes()`、`join()`、`chunks()` 与 `windows()` 方法，增强迭代器处理能力。
- 🌐 WebRTC：支持 `RTCIceTransport.getSelectedCandidatePair()` 及 `selectedcandidatepairchange` 事件；`RTCDtlsTransport` 新增 `error` 事件；`getParameters()`/`setParameters()` 支持 `rtcp` 属性；补充更多证书与传输统计字段。
- 🚗 WebDriver：改进异步滚轮事件处理，修复子框架导航提前完成问题；`browsingContext` 下载事件新增下载 ID，支持 `unhandledPromptBehavior` 的 `ignore` 状态，新增用户上下文字段及屏幕录制命令，增强工作区语言覆盖设定。
- 🧩 扩展开发：支持 `sandbox` 清单键，允许扩展页面使用不透明源并运行 `eval()` 等被 CSP 阻止的操作。
- 🧪 实验功能：默认禁用，可在 `about:config` 开启；包括无前缀 `line-clamp`、`text-decoration-inset` 百分比值、`progress()` 函数及 CSS Typed Object Model API（仅 Nightly）。

---

### [sibling-index() CSS 函数 - CSS | MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/sibling-index)

**原文标题**: [sibling-index() CSS function - CSS | MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/sibling-index)

该文章介绍了 CSS 的 `sibling-index()` 函数，它返回当前元素在父元素所有兄弟节点中的位置索引（从 1 开始），可结合 `calc()` 用于动态样式、动画等场景，并说明了语法、示例及浏览器兼容性。

- 🔢 返回当前元素在所有兄弟节点中的整数索引，第一个为 `1`，最后一个等于兄弟元素总数。
- ⚖️ 与 `:nth-child()` 类似从 `1` 计数；但不同于 `counter()`，它返回可计算的 `<integer>` 而非字符串。
- ✍️ 语法为 `sibling-index()`，不需要任何参数，直接使用即可。
- 📏 动态宽度示例：`width: calc(sibling-index() * 50px)` 可让每个列表项宽度按顺序递增。
- 🎬 顺序动画示例：通过 `animation-delay: calc(1s * sibling-index())` 实现元素按 DOM 顺序逐个淡入。
- 🌐 兼容性：属于 Baseline 2026 新特性，自 2026 年 8 月起在最新浏览器可用，旧设备可能不支持。
- 🔗 可配合 `sibling-count()` 和 `counter()` 使用，实现更复杂的兄弟元素样式逻辑。

---

### [获取失败](https://hacks.mozilla.org/2026/08/intent-to-ship-jpeg-xl/)

**原文标题**: [Failed to retrieve](https://hacks.mozilla.org/2026/08/intent-to-ship-jpeg-xl/)

无法总结：获取内容失败，状态码 403。

---

### [介绍 WordPress 浏览器扩展 – WordPress 新闻](https://wordpress.org/news/2026/08/browser-extension/)

**原文标题**: [Introducing the WordPress Browser Extension – WordPress News](https://wordpress.org/news/2026/08/browser-extension/)

WordPress 官方浏览器扩展正式发布，支持 Chrome、Chromium 和 Safari，旨在隐藏管理员工具条、提供快捷访问入口，并附带开发者工具，同时保护用户隐私。

- 🧩 扩展已上架 Chrome Web Store 和 Mac App Store，代码开源，适用于 Chrome/Chromium 及 macOS Safari 浏览器。
- 🚫 可自动或按站点隐藏 WordPress 管理工具条，避免遮挡视口、消除页面显示差异，且无需关闭个人资料中的相关设置。
- 🔗 保留常用快捷方式于浏览器工具栏，一键访问仪表盘、编辑器、文章/页面/分类/模板等，两键即可恢复完整工具条。
- 🌐 浏览时工具栏图标会显示当前站点是否为 WordPress 及登录状态，并支持从任意位置快速跳转到自己管理的站点。
- 🛠️ 内置开发者实用工具：绘制区块边界、手机尺寸预览窗口、缓存清除刷新、清除 Cookie 与本地存储，无需安装插件。
- 🔒 所有处理均在本地完成，仅读取当前页面或必要时向站点请求信息，偏好设置与登录站点列表存于浏览器，无追踪或分析。
- 🤝 项目由独立项目转为官方项目，获 Matt Mullenweg 支持，核心贡献者包括 Fabian Kägy 和 Khokan Sardar，另有团队参与测试与完善。
- 📂 开发进度在 GitHub 仓库公开，欢迎提交 bug 报告和拉取请求。

---

### [Chrome 153 测试](https://developer.chrome.com/blog/chrome-153-beta?hl=en)

**原文标题**: [Chrome 153 beta  |  Blog  |  Chrome for Developers](https://developer.chrome.com/blog/chrome-153-beta?hl=en)

Chrome 153 是首个采用两周发布周期的版本，带来多项 CSS、JavaScript、Web API 更新，以及新源试用和若干移除。

- 🎨 新增单轴滚动容器支持，允许 `overflow: scroll clip` 实现按轴约束 sticky 定位
- 🔒 引入 `scroll-axis-lock` 属性，开发者可控制是否禁止对角滚动锁定
- 🔤 JavaScript 新增 Iterator `join()` 方法，可拼接迭代器内容为字符串
- 🤝 新增 Joint Iteration（zip）提案，用于同步推进多个迭代器
- 📷 新增 `<camera>` 和 `<microphone>` 能力元素，以声明式控件请求单摄像头或麦克风权限
- 🔊 支持 IAMF 空间音频格式解码，可通过 HTML 媒体元素和 MSE 播放沉浸式 3D 音频
- ⏱️ 对齐 `transitionrun` 和媒体查询事件的分派时序，与 Gecko/WebKit 互操作
- 🎚️ WebAudio 新增可配置渲染量子大小，支持 `renderSizeHint` 参数
- 🧩 WebGPU 新增 `buffer_view` WGSL 功能，可 reinterpret 变量数据
- 🦀 XML 解析在非 XSLT 场景改用 Rust 内存安全实现，提升安全性
- 📊 新源试用：JavaScript Self-Profiling Markers，可在采样中添加浏览器活动类型标记
- 🗑️ 移除非标准 `_current` 导航目标
- 🗑️ 移除 `document.requestStorageAccessFor` 及相关网站集（RWS）

---

### [请稍等……](https://css-tricks.com/css-navigation-matching-early-days/)

**原文标题**: [One moment, please...](https://css-tricks.com/css-navigation-matching-early-days/)

正在加载中，系统提示用户请求正在验证，请耐心等待。

- ⏳ 页面显示“Loader”加载组件，表明当前处于等待状态。
- 🔐 请求正在被系统验证，用户无需进行额外操作。

---

### [获取失败](https://arstechnica.com/security/2026/08/aliexpress-caught-fingerprinting-visitors-after-sending-inaudible-sounds-to-browsers/)

**原文标题**: [Failed to retrieve](https://arstechnica.com/security/2026/08/aliexpress-caught-fingerprinting-visitors-after-sending-inaudible-sounds-to-browsers/)

无法总结：获取内容失败，状态码 202。

---

### [](https://expo.dev/blog/how-to-build-mobile-apps-with-ai-the-three-tools-that-actually-matter?utm_source=frontendfocus&utm_medium=email&utm_campaign=Expo-Agent)

**原文标题**: [How to build mobile apps with AI: the three tools that actually matter â Expo blog](https://expo.dev/blog/how-to-build-mobile-apps-with-ai-the-three-tools-that-actually-matter?utm_source=frontendfocus&utm_medium=email&utm_campaign=Expo-Agent)

本文介绍了用 AI 构建移动应用时真正重要的三个工具：Skills（技能）、MCP 服务器和 AI 工作流。作者以 habit tracker 应用为例，展示了如何用这些工具让 AI 高效地写出美观、高性能的移动应用。

- 🛠️ 三个关键工具：Skills、MCP servers、AI 工作流，缺一不可。
- 📄 Skills 是 SKILL.md 指令文件，AI 按需读取，上下文成本低；支持显式 `/` 命令或让 AI 自主调用。
- 🧩 Expo 官方提供技能集，可一次安装多个；`find-skills` 技能还可搜索约 90 万个社区技能。
- 🔌 MCP 服务器让 AI 连接外部服务（如 Expo dashboard），读取构建日志、驱动模拟器、验证修复是否真正生效。
- 🖥️ Expo MCP 分服务器工具和本地工具；本地工具需额外安装，可截图、点击、查看原生和 JS 日志。
- ⚠️ MCP 比 Skills 更消耗上下文，所有工具定义会预加载；只在项目实际使用对应服务时才安装。
- 🧠 AI 工作流的核心：给足上下文、明确需求、控制上下文臃肿。
- 💡 若不清楚需求，可让 AI 扮演 ideation 伙伴，用 `/co-ceo` 或 `grill-me` 类技能帮助梳理产品方向。
- 📏 上下文使用建议保持在 50% 以下；超过后模型易 hallucination，且每次响应更贵。
- 🔀 一个对话只聚焦一个目标；需要切换话题时用“分支”而非继续堆叠，保持每条线程简洁。
- 🚀 上手顺序：先添加 Expo skills，再连接一个 MCP，最后安装状态行监控上下文。
- ✅ 构建失败时先运行 `expo doctor` 检查依赖问题，再通过 MCP 读取日志并让 AI 自动修复。

---

### [3D CSS 指南：perspective、preserve-3d 与 translateZ](https://www.carmenansio.com/articles/3d-css-guide/)

**原文标题**: [3D CSS Guide: perspective, preserve-3d and translateZ](https://www.carmenansio.com/articles/3d-css-guide/)

overview summary  
- 🎮 文章以《超级马里奥兄弟 3》的伪 3D 与《超级马里奥 64》的真 3D 对比为引，讲解 CSS 3D 变换的核心概念与实践技巧。  
- 🧱 从视差滚动的平面景深，到`perspective`、`perspective-origin`、`preserve-3d`等属性，逐步构建出可交互的 3D 场景。  
- 🕹️ 强调相机控制、性能优化、无障碍支持及浏览器兼容性，最终汇总成一份实用的“说明书”。  

- 🖼️ 伪深度靠“近大远小”的视差实现：远处物体移动慢、近处移动快，仅需不同`translateX`速度即可模拟。  
- 📷 `perspective`定义相机到屏幕的距离，值越小透视越夸张（鱼眼），通常界面用 800–1200px。  
- 👀 `perspective-origin`控制相机站位，移动它可从不同角度观察场景，相当于马里奥 64 中的黄色视角按钮。  
- 🔗 `transform-style: preserve-3d`保持子元素处于同一 3D 空间，否则会被压平为父级平面上的贴图；需检查整条父链都设置此属性。  
- 📦 一切 3D 物体皆由“长方体”构成：六个面各自旋转并沿法线平移，用`--w`、`--h`、`--d`三个变量控制尺寸即可复用。  
- 🌀 `rotateX`、`rotateY`、`rotateZ`对应俯仰、偏航、翻滚；变换顺序从左到右依次作用于新坐标系，写反会得到错误位置。  
- 🏗️ 构建场景只需把若干方块放在同一`preserve-3d`平面上，再对父级施加统一旋转，就能实现“环绕相机”效果。  
- ⚡ 性能三原则：只动画`transform`和`opacity`、对移动元素加`will-change: transform`、尊重`prefers-reduced-motion`。  
- 🧰 工具补充：`translate3d`、`rotate3d`、`scale3d`、`matrix3d`，以及独立的`translate`/`rotate`/`scale`属性，便于分别控制。  
- ♿ 3D 只是视觉增强：键盘操作、ARIA 标签、焦点样式、真实状态驱动，确保无鼠标或辅助技术用户也能完全使用。  
- ⚠️ 常见陷阱：`overflow`会强制压平`preserve-3d`；深度排序不精确，`z-index`无效；模糊/发光会被裁剪到图层矩形内。  
- 🖥️ Safari 中若元素同时带`overflow`、`filter`、`clip-path`、`mask`或`opacity<1`，可能意外压平 3D 场景。  
- 📖 快速查错：场景不立体→检查父链`preserve-3d`与裁剪属性；面排序错→按`translateZ`排序；卡顿→只动画合成属性；眩晕→降级为静态帧。  
- 🎯 从平面平台到可操控相机的立体世界，核心仅需六项属性即可实现——浏览器早已支持十年以上，放心大胆去构建。

---

### [从 Sass 迁移到原生 CSS 的过程 | Chris Smith](https://chrissmith.xyz/blog/2026/the-process-of-migrating-from-sass-to-native-css/)

**原文标题**: [The process of migrating from Sass to native CSS | Chris Smith](https://chrissmith.xyz/blog/2026/the-process-of-migrating-from-sass-to-native-css/)

overview summary  
本文介绍了将项目从 Sass 迁移到原生 CSS 的完整过程，包括迁移动机、具体步骤以及导入方式的改变，帮助开发者顺利去除 Sass 依赖。

- 🏁 动机：原生 CSS 已支持变量、嵌套等特性，Sass 不再是必需品；迁移可减少重复代码、加快构建、去除编译器依赖。
- 🔍 找出所有 .scss 文件，并搜索 Sass 特有功能（如 mixin、lighten() 等），替换为 CSS 函数或复制编译后的值。
- 💬 将 // 注释改为 /* */，否则后续规则可能无法被解析。
- 🗑️ 删除由 Sass 生成的 CSS 文件、压缩文件和 map 文件，注意保留手写 CSS。
- 📝 将 .scss 文件重命名为 .css，并更新所有引用（如 <link> 或 styleUrl）。
- ⚙️ .NET 项目需检查 <Content> 配置，确保部署时包含正确的 CSS 文件。
- 🧪 重新构建并运行测试，手动检查页面，防止 CSS 规则缺失导致的隐性错误。
- 🧹 迁移完成后移除 Sass 编译器和相关配置，清理 .scss 残留引用。
- 📦 导入策略改变：原生 CSS 的 @import 会触发运行时请求，建议改为多个小文件并行加载，利用 HTTP/2 提升性能。
- 🚀 若改变打包方式，需测试性能，可考虑服务端打包、压缩或延迟非关键 CSS。

---

### [](https://0.mk/blog/link-rot)

**原文标题**: [Where did the old web go? We followed 657,607 links to find out. | 0.mk](https://0.mk/blog/link-rot)

overview summary  
- 🕸️ 一篇关于 0.mk 链接缩短器历史数据的分析：恢复了 2009–2014 年间的 657,607 条链接，并逐一访问验证，发现旧网页大规模消逝。  
- 📉 在可访问的 492,620 个唯一 URL 中，仅 21.3% 仍能正常加载；76.7% 的历史链接已无法打开。  
- 🔌 链接失效的主因是网络连接失败（51.24%）和 HTTP 错误（25.44%），其中 404 错误最常见。  
- 🏛️ 大型平台如 YouTube、Wikipedia 和 Google 存活率较高，而个人博客、论坛、本地新闻及照片托管网站大量消失。  
- 🇲🇰 数据记录了马其顿早期互联网生态，许多本地新闻网站已永久关闭，短链接比新闻机构“活得更久”。  
- 💎 数据库中有趣发现：第一个短链接指向一个 CSS 文件；最短链接指向“最长域名”；还有 4,478 个链接指向其他缩短服务，形成“双重脆弱”。  
- 🤖 0.mk 在 2026 年借助 AI 技术重新上线，AI 承担了垃圾信息过滤、滥用审查和监控等原本无法负担的工作。  
- 🔍 检测方法：每个链接最多跟随 5 次重定向，并对连接失败从第二网络重试；HTTP 2xx/3xx视为加载成功。

---

### [](https://www.bram.us/2026/08/20/the-future-of-css-target-multiple-classes-with-the-class-prefix-selector/)

**原文标题**: [The Future of CSS: Target Multiple Classes with the Class Prefix Selector – Bram.us](https://www.bram.us/2026/08/20/the-future-of-css-target-multiple-classes-with-the-class-prefix-selector/)

overview summary
- 🎯 文章介紹了 CSS 即将推出的「类前缀选择器」（`.prefix-*`），用于高效匹配共享前缀的多个类，解决现有做法（额外基类、逐一列举、属性选择器）的痛点。
- ⚡️ 属性选择器性能极差：基准测试中普通类选择器跑出 6000+ runs/s，而 `[class*=" btn-"]` 仅约 328 runs/s，慢了近 20 倍。
- ✨ 新语法非常简洁：例如 `.btn-*` 即可匹配 `btn-primary`、`btn-secondary` 等类；该方案由 Lea Verou 提出，并在 2026 年 8 月 CSSWG 柏林 F2F 会议上决议加入 CSS Selectors Level 5。
- 🔍 细节行为：`.foo-*` 不会匹配 `class="foo-"`（空后缀），也不会匹配 `class="foo--"`；目前规范要求前缀后至少有一个字符，且该字符不能是连字符。
- 🚫 限制明确：目前仅支持连字符作为分隔符，`_` 等分隔符未来可能纳入；任意通配前缀（如 `.foo*`）和中间通配符（如 `.card-*-primary`）都不允许，以避免误匹配（如 `.footer`）并保护浏览器选择器性能优化。
- ❓ 为何不重用 `|=` 选择器：`[class|="foo"]` 会意外匹配独立基类（如 `.bi`）、对多类元素不生效（因为只检查属性值开头）、性能不佳；更重要的是，统一 `-*` 语法是 CSSWG 未来扩展通配符（如属性名 `[data-*]`、自定义元素名）的大方向。
- 📅 浏览器支持目前为零：该特性处于规范草案早期，Chromium 已建 bug #550093337，Firefox 和 Safari 尚未跟踪；可能还需数年才能投入生产环境。
- 🧪 可用 `@supports selector(.foo-*)` 进行特性检测，判断当前浏览器是否支持此选择器。

---

### [](https://agustinbarrientos.com/writing/senior-eye/searchable-accordions/)

**原文标题**: [Building an Accordion the Browser Can Search - Agustin Barrientos](https://agustinbarrientos.com/writing/senior-eye/searchable-accordions/)

这篇文章探讨了如何构建一个浏览器可搜索的折叠面板（手风琴），核心是解决 `display:none` 导致浏览器查找、深链和滚动到文本失效的问题。文章对比了多种隐藏方式对可发现性的影响，推荐优先使用原生 `<details name>`，并在自定义折叠组件中利用 `hidden="until-found"` 与 `beforematch` 事件来保持内容可被浏览器找到。同时强调渐进增强、状态同步和用真实浏览器工具验证。

- 🔍 核心问题：用 `display:none` 折叠答案时，浏览器“在页面中查找”、`#id` 深链和 `#:~:text=` 滚动到文本都找不到已隐藏的内容。
- 🧩 “隐藏”并非单一状态：`display:none`、布尔 `hidden`、`content-visibility`、`hidden="until-found"`、视觉隐藏等对渲染、查找和无障碍树的影响各不相同。
- 📋 关键区别：`hidden="until-found"` 是唯一能让内容在视觉上隐藏、但浏览器查找时能自动揭示的方式；`content-visibility:auto` 可被查找但内容靠近视口时仍会渲染。
- 🏛️ 原生优先：FAQ 这类摘要/内容结构应优先使用 `<details name="faq">`，无需 JavaScript 即可获得单开分组、查找揭示和深链支持。
- ⚙️ 自定义场景：当必须自己实现触发器时，用 `hidden="until-found"` 代替 `display:none`，并把可折叠内容放在 light DOM 的 slot 中。
- ⚡ 状态同步：`beforematch` 事件在浏览器揭示内容前触发，会冒泡且不可取消；应在处理函数中同步 `aria-expanded` 和 `open`，但不要移除 `hidden` 属性以免破坏揭示链。
- 🧱 避免 shadow DOM 陷阱：shadow root 内的 `id` 无法被文档深链定位，且 `beforematch` 的 `composed:false` 不会跨边界，因此内容需保持在 light DOM。
- 🌐 兼容性：`until-found` 支持 Chrome 102+、Firefox 148+、Safari 26.2+；Safari 能揭示但不滚动到精确匹配，`beforematch` 已跨引擎可用。
- ⚠️ 常见错误：能用 `<details>` 却自定义折叠、移除原生 marker、忘记 `until-found` 元素仍生成边框和背景、或使用 `display:none`/`inline` 导致无法揭示。
- 🧠 资深与初级的差别：根据“谁仍需要访问内容”来选择隐藏方式；让平台负责发现机制；保持组件状态诚实；精确区分“支持”的具体行为。
- 🛠️ 动手验证：用真实浏览器的 Cmd/Ctrl F、深链和屏幕阅读器测试，而不是只依赖组件测试通过。

---

### [欧盟人工智能标注新指南 — Smashing Magazine](https://www.smashingmagazine.com/2026/08/eu-guidelines-ai-labelling/)

**原文标题**: [New EU Guidelines For AI Labelling — Smashing Magazine](https://www.smashingmagazine.com/2026/08/eu-guidelines-ai-labelling/)

欧盟新 AI 标签法规自 2026 年 8 月 2 日生效，要求面向欧盟用户的企业对深度伪造、聊天机器人、未经人工审核的公共利益 AI 文本等明确披露；文章同时解析了合规边界、图标使用误区及全球类似立法趋势。

- 🇪🇺 新规自 2026 年 8 月 2 日起生效，适用于所有向欧盟公民提供 AI 服务的全球企业，不限于欧盟本地公司。
- 🏷️ 必须标注的内容包括：深度伪造、聊天机器人/AI 代理、完全由 AI 撰写且未经人工审查的公共利益文本，以及情绪识别和生物识别工具。
- ⚖️ 法律义务同时落在 AI 系统的提供者和部署者身上，即使使用第三方 AI 工具，也不能免除标注责任。
- ✅ 并非所有 AI 内容都需要标注：经人类实质性审查并有人署名负责的内容，以及拼写检查、翻译等辅助性编辑，不触发披露要求。
- 🔍 “公共利益”涉及健康、安全、环境、经济、政治、科学等；广告或营销中逼真的 AI 图像可能被要求披露。
- ✨ 仅仅使用✨图标不够，欧盟发布了官方 AI 图标集，要求清晰可见、搭配纯文本标签、可被辅助技术访问，并在内容被分享时保持显示。
- 🌍 全球多地正同步立法：中国（2025 年 9 月）、加州（2026 年 8 月）、韩国（2026 年 1 月）、印度（2026 年 2 月）均已有类似 AI 标注要求。
- 💡 核心原则很明确：当 AI 内容可能被误认为人类内容时，创作者必须以清楚、明显、无歧义的方式披露。

---

### [](https://a-dev.github.io/probes/corner-shape/)

**原文标题**: [CSS corner-shape generator: squircles with a fallback](https://a-dev.github.io/probes/corner-shape/)

该工具用于生成 CSS `corner-shape` 属性，可调整圆角形状并复制代码，同时提供两种回退方案。

- 🔧 `corner-shape` 可修改 `border-radius` 定义的角部曲线形状，支持超椭圆等多种预设。
- 📈 指数 `k` 决定形状：0 为斜切、1 为圆形、2 为苹果 squircle、负值内凹，超出范围则变为凹口或方形。
- 🧩 默认回退到 `border-radius`，兼容边框阴影但仅支持外凸；精确回退用 `clip-path` 完全复刻形状但会裁剪边框区域。
- ⚖️ 外凸角会自动换算等效 `border-radius` 保持视觉一致，内凹角则保留原半径并提醒。
- 🎯 精确模式使用 Bézier 分段拟合，误差控制在半径的 0.25% 以内，支持至 `superellipse(-3)`。
- 🖥️ 提供实时预览、尺寸/比例/内边距/字体调整、各角独立设置及多种预设，方便设计调试。
- 📋 一键复制 CSS，并附带浏览器支持状态说明（当前数据未加载）。

---

### [](https://dev.to/a-dev/css-corner-shape-add-a-squircle-to-your-design-today-with-the-right-fallback-3ne6)

**原文标题**: [CSS corner-shape: add a squircle to your design today with the right fallback - DEV Community](https://dev.to/a-dev/css-corner-shape-add-a-squircle-to-your-design-today-with-the-right-fallback-3ne6)

文章介绍了 CSS 新属性 `corner-shape`，尤其是 `squircle`（超椭圆）形状如何让界面曲线更自然，并重点说明了在浏览器支持有限的情况下如何优雅回退，包括用 `@supports` 调整 `border-radius`、用 `clip-path` 处理凹形，以及利用 `calc()` 自动匹配半径。

- 🎨 `corner-shape` 可创建比普通圆角更灵动的曲线，`squircle` 是苹果和诺基亚早已使用的经典形状。
- 🌐 该属性目前仅 Chromium 内核浏览器（Chrome/Edge 139+）支持，需为其他浏览器准备回退。
- 📏 视觉上 `corner-shape` 与 `border-radius` 的半径并不相等，直接套用会效果不符，必须调整数值。
- 🧮 本质是 `superellipse(n)` 超椭圆函数，参数 `n` 控制曲率加速方式；`n=1` 为圆，`n=2` 为 squircle，`n=0` 为平切，负值对应凹形。
- 🗂️ 预设值包括 `notch`、`scoop`、`bevel`、`round`、`squircle`、`square`，覆盖从凹到凸的各阶段。
- 🛠️ 文章提供在线生成器，可生成回退代码：在 `@supports` 内使用 `corner-shape`，外部用调整后的 `border-radius` 兜底。
- 🔪 当 `superellipse` 参数小于 1（凹形）时，需要用 `clip-path` 做精确回退，但会裁掉阴影和轮廓等效果。
- 💡 进阶技巧：用 CSS `calc()` 和 `pow()` 自动计算回退半径，让 `s > 1` 的凸形无需生成器也能匹配视觉。
- 📐 作者还展示了如何将这类形状封装成 CSS 方法论中的“原子”类，方便在大型项目中复用。

---

### [介绍 Microlighter - daverupert.com](https://daverupert.com/2026/08/microlighter/)

**原文标题**: [Introducing Microlighter - daverupert.com](https://daverupert.com/2026/08/microlighter/)

作者介绍了他开发的一款名为 MicroLighter 的小型客户端语法高亮器，它利用 CSS Custom Highlights API 实现零 DOM 突变的高亮效果，并采用 Textmate 语法按需加载语言，同时将额外功能拆分为 Web Component，兼顾轻量、灵活与易用性。

- ✨ MicroLighter 是一个零依赖、约 2KB（gzip）的客户端语法高亮器，基于 CSS Custom Highlights API 构建。
- 🎨 使用 CSS 的 `::highlight(token-name)` 伪元素标记高亮范围，而非注入 `<span>`，避免 DOM 修改。
- 🧩 利用 Textmate 语言语法，支持几乎所有编程语言，并借鉴 PrismJS 简化了 token 分类，更易上手。
- 📦 所有语言语法按需动态加载，减少初始 bundle 体积，只为实际使用的语言付费。
- 🌗 内置主题采用 `light-dark()` 函数，将亮色和暗色主题合并为单一可读主题。
- 🔧 核心库只负责“推断语言并高亮”这一件事，行号、复制按钮等额外功能全部移入 `<micro-lighter>` 自定义元素。
- 🕸️ Web Component 使用 ShadowDOM 封装 UI，职责分离清晰，且可通过继承扩展自定义功能。
- 💡 作者提到 `::highlight()` 目前不支持斜体、粗体或字体切换，但换来了更简洁的 API 和零 DOM 操作。
- 📚 创建动机是 Jekyll 博客的高亮器频繁出问题，尝试过 Highlight.js、PrismJS、Rouge、Shiki 后，想探索 Bramus 的 Highlight API 方案。
- ⚡ 使用时可自动初始化，也可按需动态 `import()`，仅当页面存在代码块时加载脚本。
- 🛠️ 提供 ESM 版本方便自定义调用，例如通过 `highlightAll({ selector })` 限定高亮范围。
- 🎛️ Web Component 支持 `data-syntax-theme`、`line-numbers`、`controls="copy"` 等属性，开箱即用。
- 🎯 主题定制基于语义化 CSS 变量（如 `--syntax-comment`、`--syntax-function`），配合 `::highlight()` 伪元素可轻松打造自己的样式。

---

### [](https://developer.mozilla.org/en-US/docs/Web/API/CSS_Custom_Highlight_API)

**原文标题**: [CSS Custom Highlight API - Web APIs | MDN](https://developer.mozilla.org/en-US/docs/Web/API/CSS_Custom_Highlight_API)

overview summary  
- 🎨 CSS 自定义高亮 API 可让开发者用 JavaScript 创建任意文本范围，并通过 CSS 进行样式化，不影响 DOM 结构。  
- 📌 它扩展了 ::selection、::spelling-error 等内置高亮伪元素，支持自定义 Range 对象。  
- 🔍 使用四步流程：创建 Range 对象、创建 Highlight 对象、注册到 HighlightRegistry、用 ::highlight() 伪元素设置样式。  
- 🔧 多个 Range 可归入一个 Highlight，也可创建多个 Highlight 分别设置不同样式（如协作文本编辑器按用户着色）。  
- 📋 通过 CSS.highlights（类似 Map）注册或删除高亮，支持 set、delete、clear 操作。  
- ♿ 自定义高亮本身不提供语义信息，可通过 type 属性暴露语义，但兼容性不一；必要时建议使用 <mark> 或补充无障碍提示。  
- 🧩 相关接口：Highlight（表示范围集合）和 HighlightRegistry（通过 CSS.highlights 访问）。  
- 🔎 示例展示搜索高亮：监听输入事件、遍历文本节点、创建匹配范围、注册高亮，并用 CSS 设置背景色与文字色。  
- 🌐 该功能自 2025 年 6 月起在最新设备与浏览器中可用，但旧浏览器可能不支持。

---

### [电子签名 API 指南：为您的应用添加签名功能](https://developer-api.foxit.com/developer-blogs/api-guides-tutorials/esignature-api-guide-add-signing-app/?utm_source=draftdev&utm_medium=newsletter&utm_campaign=frontendfocus_20260826)

**原文标题**: [eSignature API Guide: Add Signing to Your App](https://developer-api.foxit.com/developer-blogs/api-guides-tutorials/esignature-api-guide-add-signing-app/?utm_source=draftdev&utm_medium=newsletter&utm_campaign=frontendfocus_20260826)

本文介绍了 2026 年面向开发者的 6 个 DocuSign API 替代方案，并围绕集成速度、长期维护等六个关键维度进行对比，旨在帮助开发者快速做出选择。

- ⏱️ 节省调研时间：直接对比六款 eSign API，避免开发者花费数小时进行人工研究。
- 📜 替代品清单：涵盖 Dropbox Sign、Adobe Acrobat Sign、PandaDoc、SignNow、BoldSign 和 Foxit eSign。
- 🔍 多维评估标准：重点考察集成速度与长期维护等六个最关键的评判维度。
- 🛠️ 开发者导向：内容专为开发者设计，关注 API 接入效率与后续维护体验。
- 📅 前瞻性参考：提供 2026 年值得关注的 DocuSign API 替代方案趋势。

---

### [](https://mobileview.app/)

**原文标题**: [Mobile View — see your site on desktop & mobile at once](https://mobileview.app/)

该评论来自俄罗斯用户 Vladimir Solyankin，他近期开始使用此应用，但已确信它优于同类产品。他称赞应用设计美观、功能强大，并向作者表达了感谢。

- 🇷🇺 用户来自俄罗斯，名为 Vladimir Solyankin  
- ⏳ 虽然使用时间不长，但已决定长期选用  
- 🏆 在同类应用中脱颖而出，获得高度认可  
- 🎨 设计精美，视觉效果出色  
- ⚙️ 功能完善，体验优秀  
- 🙏 对作者表示衷心感谢

---

### [](https://github.com/aarongustafson/form-saver)

**原文标题**: [GitHub - aarongustafson/form-saver: A web component that stores (and restores) values within the form it wraps · GitHub](https://github.com/aarongustafson/form-saver)

overview summary  
- 📦 form-saver 是一个 Web Component，用于自动保存并恢复其包裹表单中的字段值，主要面向崩溃恢复和会话中断场景。  
- 💾 用户在输入时自动将表单数据保存到 localStorage，页面重新加载后自动恢复已保存的值。  
- 🧹 成功提交后清除已保存的数据，也可通过 `retain` 属性保留指定字段。  
- 🎛 支持 `retain-choice` 注入可选的保留复选框，并可自定义标签和放置容器。  
- ⚙️ 提供 `saveFormState()`、`restoreFormState()`、`clearSavedData()` 等核心方法。  
- 🧩 支持的字段包括 input（排除 file/submit/button/reset/image）、textarea、select（单选和多选）。  
- 🌐 基于现代 Web 标准（Custom Elements v1、Light DOM、ES Modules），旧浏览器可能需要 polyfill。  
- 🛠 安装方式：`npm install @aarongustafson/form-saver`，支持自动定义或手动定义自定义元素。  
- 📝 可用 `storage-key` 覆盖默认存储键，默认键格式为 `form-saver:{method}:{resolvedActionUrl}`。  
- 🧪 项目包含测试、覆盖率、lint、格式化等开发脚本，并提供了多个在线演示。

---

### [<form-saver> Web 组件演示](https://aarongustafson.github.io/form-saver/demo/)

**原文标题**: [<form-saver> Web Component Demo](https://aarongustafson.github.io/form-saver/demo/)

这段文字介绍了一个名为 `<form-saver>` 的 Web 组件，它可在表单提交后保存并恢复字段值，并提供了 `retain`、`retain-choice` 等属性来灵活控制字段保留与用户体验。
- 📝 `<form-saver>` 会自动保存并恢复其内部第一个表单的字段值，刷新后仍可看到输入内容。
- 💾 基本用法：在表单中输入后刷新页面，字段值会被自动恢复。
- 🔧 `retain` 属性接受空格分隔的字段名列表，成功提交后仅保留这些字段，其他字段被清空。
- ✅ 例如：使用 `retain="name email"` 时，提交后刷新，Name 和 Email 恢复，Message 为空白。
- ☑️ `retain-choice` 属性会向表单注入一个可访问的复选框，默认不选中时提交后仍会清除保留字段。
- 🏷️ 用 `retain-choice-label` 可自定义复选框的标签文本，例如“Remember my details next time”。
- 📦 用 `retain-choice-container` 指定 CSS 选择器，可将复选框追加到表单内指定容器中。
- 📚 完整属性、事件及浏览器支持信息请参阅 README。

---

### [抖动 — 矢量抖动工具](https://dither.neato.fun/)

**原文标题**: [Dither — Vector Dither Tool](https://dither.neato.fun/)

您提供的消息中没有实际文本内容，只有图片上传占位符或加载按钮的提示。由于我无法直接读取图片，请将需要总结的文字内容粘贴到对话中，我会根据您的要求生成中文要点总结。

- 📭 文本缺失：当前没有提供任何文章或段落，无法进行总结。
- 🖼️ 图片无法识别：我无法从“Drop an image”或“Load Image”按钮中提取信息，请上传图片并手动输入其中的文字。
- 📝 格式已准备：一旦您提供文本，我将严格按照“概述摘要 + 表情符号要点”的模板输出中文摘要。

---

### [](https://sveltebits.xyz/)

**原文标题**: [Svelte Bits - Animated UI Components For Svelte](https://sveltebits.xyz/)

overview summary
Svelte Bits 是一个面向创意开发者的 Svelte 5 组件库，提供 130+ 可定制动画组件与背景，支持 TypeScript 和 Tailwind，可通过 jsrepo 或 shadcn 快速集成，并兼容 AI 编程工具，开源免费。

- ✨ 提供 130+ 组件：涵盖背景、文本效果、动画和 UI 模式，可直接嵌入项目
- 🧩 组件高度可定制：如 ColorBends 支持颜色、速度、频率、噪声、旋转等属性实时调整
- 🗂️ 清晰分类：分为 Backgrounds、Animations、Text Animations、Components 等四类，方便查找
- ⚡ 技术栈统一：所有组件基于 Svelte 5 + TypeScript + Tailwind，类型安全且风格一致
- 🤖 AI 友好：与 Cursor、Copilot、v0 等工具配合良好，可描述需求后直接生成并引入
- 📦 安装便捷：支持 npx jsrepo add 或 shadcn 方式，组件直接落入代码库即用
- 🌟 开源免费：项目在 GitHub 上开源，持续增长，欢迎 Star 关注
- 🔗 生态关联：是 React Bits 的 Svelte 移植版，由 davidhdev 开发，并提供 Vue Bits 等版本

---

### [React Bits - 用于 React 的动画 UI 组件](https://reactbits.dev/)

**原文标题**: [React Bits - Animated UI Components For React](https://reactbits.dev/)

overview summary  
- 📄 您尚未提供需要总结的文章内容，因此无法生成要点列表。  
- ✏️ 请发送具体文本，我将按照模板为您提炼关键信息和要点。

---

### [公有领域图像档案库](https://pdimagearchive.org/)

**原文标题**: [
			Public Domain Image Archive
		](https://pdimagearchive.org/)

概述：这是一个公共领域图像档案库，收录超过 1.1 万件版权过期作品，可自由浏览、下载和复用，并持续更新，支持多种分类浏览方式。

- 🖼️ 收录 11,206 件已进入公共领域的作品，供所有人免费浏览、下载和复用
- 🔄 这是一个动态数据库，每周都会新增图像
- 🗂️ 提供按艺术家、世纪、风格、主题、标签等分类浏览功能
- ♾️ 设有“无限视图”模式，可沉浸式浏览全部作品
- 🔍 支持在艺术家、世纪、风格、主题、标签或全部作品中快速选择切换

---

### [](https://type.lol/)

**原文标题**: [Type.lol - Independent Type Foundry Index](https://type.lol/)

您好，您没有提供需要总结的文本内容。请把文章或文本粘贴在消息中，我将按照模板用中文为您生成概述和带表情符号的要点列表。

---

### [](https://www.youtube.com/watch?v=3YtygAx_C6A)

**原文标题**: [A Walkable ASCII Cyberpunk City in One HTML File - YouTube](https://www.youtube.com/watch?v=3YtygAx_C6A)

概述：此內容為 YouTube 頁面的標準導覽與法律資訊連結清單，涵蓋平台介紹、支援、政策及版權等項目。
- 📰 提供新聞中心與媒體相關資訊連結
- ©️ 標示版權與聯絡方式
- 🎨 列出創作者與廣告刊登選項
- 👨‍💻 包含開發人員資源與平台運作說明
- 🔒 涵蓋條款、私隱及安全政策
- 🧪 提供測試新功能入口
- 📅 顯示 © 2026 Google LLC 版權聲明

---

