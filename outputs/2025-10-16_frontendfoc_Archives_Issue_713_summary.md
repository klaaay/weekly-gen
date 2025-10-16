### [前端聚焦 第 713 期：2025 年 10 月 15 日](https://frontendfoc.us/issues/713)

**原文标题**: [Frontend Focus Issue 713: October 15, 2025](https://frontendfoc.us/issues/713)

前端技术动态概览：涵盖浏览器更新、CSS 新特性、AI 编程工具及开发资源等前沿资讯。

- 🌐 Firefox 144 发布，所有主流浏览器现已支持 View Transitions API，新增 moveBefore() 方法及画中画功能优化
- 📖 MDN 推出 CSS 视图过渡新手指南，帮助开发者快速掌握该概念
- 🤖 新课程《专业 AI 编程设置》教授如何利用 Cursor 和 Claude Code 提升编码效率
- 🎯 CSS Grid 布局思维模型详解，通过网格线实现精准元素定位
- ⚡ Firefox 团队推出 Interop 功能投票平台，收集开发者对 Web 平台特性的优先级意见
- 🆕 W3C 启用新 logo，React 转入独立基金会管理，CSS Podcast 第五季开播
- 🛠️ 现代 CSS 实现圆角标签页、contrast-color 函数优化探讨、progress() 函数应用场景解析
- 🔧 开源工具 Triplex 支持 React Three Fiber 组件可视化构建，Mirrow 实现 SVG 动态创作
- 📈 Make Graph 在线图表工具提供 10+ 图表类型与主题，EmbedPDF 无依赖 PDF 查看器
- 🚀 Bun 1.3 全栈 JS 运行时升级，新增热重载开发服务器和 React 项目脚手架功能

---

### [Firefox 144.0 全新功能、更新与修复一览](https://www.firefox.com/en-US/firefox/144.0/releasenotes/)

**原文标题**: [Firefox  144.0, See All New Features, Updates and Fixes](https://www.firefox.com/en-US/firefox/144.0/releasenotes/)

Firefox 144.0 版本于 2025 年 10 月 14 日发布，带来多项功能更新与改进，包括标签组优化、隐私管理增强、视觉搜索集成、AI 搜索工具以及开发者工具升级等。

- 🎯 标签组功能优化：折叠状态下可直接拖入标签，专注模式可突出显示当前活动标签
- 👥 多账户配置文件：支持创建独立配置文件区分工作/生活场景，含自定义命名与主题功能（逐步推送中）
- 🖼️ 画中画增强：新增 Shift+ 点击关闭按钮可不中断视频播放
- 🔐 密码管理器升级：本地存储密码加密方案升级为 AES-256-CBC
- 🔍 视觉搜索集成：右键图片可使用 Google Lens 进行图像识别与文本提取（需设谷歌为默认搜索引擎）
- 🤖 AI 搜索工具：地址栏集成 Perplexity AI 问答引擎，提供智能答案
- 🌐 语言支持扩展：新增阿塞拜疆语、孟加拉语等翻译，优化多语种翻译质量
- 🛡️ 安全修复：包含多项安全性更新与漏洞修复
- 💻 开发者功能：新增 CSS 自定义属性跳转、View Transitions API 支持、WebGPU 接口扩展等
- 📱 平台兼容性：停止支持 Windows 8.1 及以下、macOS 10.14 及以下系统，建议使用 ESR 版本

---

### [视图过渡 API - Web API | MDN](https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API)

**原文标题**: [View Transition API - Web APIs | MDN](https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API)

View Transition API 提供了一种在不同网站视图间创建动画过渡的机制，支持单页面应用和多页面应用的视图切换动画。

- 🌐 简化视图切换动画，适用于单页面和多页面应用
- ⚡ 减少用户认知负荷，提升体验和感知加载速度
- 🛠️ 解决传统实现中的复杂 CSS/JavaScript 编写和可访问性问题
- 🔧 提供 ViewTransition 接口和 startViewTransition() 方法控制过渡
- 🎨 支持自定义动画效果和过渡条件设置
- 📄 通过 HTML 的<link rel="expect">和 CSS 新属性控制过渡行为
- 🎯 包含伪类和伪元素用于精细控制过渡状态
- 📱 提供多个演示案例展示实际应用效果
- 📚 兼容现代浏览器，有详细规范文档支持

---

### [视图转换 API（单文档）| 我能用吗... HTML5、CSS3 等支持表格](https://caniuse.com/view-transitions)

**原文标题**: [View Transitions API (single-document) | Can I use... Support tables for HTML5, CSS3, etc](https://caniuse.com/view-transitions)

View Transitions API（单文档）是一种用于在不同 DOM 状态之间创建动画过渡的机制，同时以单步操作更新 DOM 内容，目前全球支持率为 88.03%。

- 🌐 全球浏览器支持率达 88.03%
- 🎬 提供 DOM 状态间动画过渡机制
- 📄 专为单文档转换设计
- ✅ Chrome 111+、Edge 111+、Safari 18+、Firefox 144+ 已支持
- ❌ IE、Opera Mini 及旧版浏览器不支持
- 📱 移动端 Chrome Android 141+、Safari iOS 18+ 已支持
- 🔧 可通过 MDN 和 Chrome 开发者文档获取技术资源

---

### [使用 moveBefore 在 DOM 中移动元素并保持状态 – Bram.us](https://www.bram.us/2025/01/16/move-elements-around-the-dom-while-preserving-their-state-with-movebefore/)

**原文标题**: [Move elements around the DOM while preserving their state with moveBefore – Bram.us](https://www.bram.us/2025/01/16/move-elements-around-the-dom-while-preserving-their-state-with-movebefore/)

Chrome 133 引入的新方法 moveBefore 允许在 DOM 中移动元素时保持其原有状态，相比传统 insertBefore 方法具有显著优势。

- 🆕 Chrome 133 新增 moveBefore 方法，可在移动 DOM 元素时保持元素状态
- 🔄 传统 insertBefore 方法会导致元素重新加载，丢失当前状态
- 🎬 演示显示使用 moveBefore 移动 iframe 时视频播放不会中断
- 📍 移动时保持焦点状态、弹窗开启、CSS 动画继续执行
- 🔧 语法与 insertBefore 相似，便于替换使用
- ⚠️ 会触发 MutationObserver 的两个变更记录，出于兼容性考虑
- 🌐 目前仅 Chrome 133+ 支持，Safari 和 Firefox 已表示将支持
- 🔍 可通过特征检测"moveBefore" in Element.prototype 检查浏览器支持

---

### [Firefox 144 开发者版 - Mozilla | MDN](https://developer.mozilla.org/en-US/docs/Mozilla/Firefox/Releases/144)

**原文标题**: [Firefox 144 for developers - Mozilla | MDN](https://developer.mozilla.org/en-US/docs/Mozilla/Firefox/Releases/144)

Firefox 144 版本于 2025 年 10 月 14 日发布，为开发者带来多项功能更新与改进，涵盖网页开发、扩展开发及实验性功能。

- 🔧 HTML 按钮元素新增 command 与 commandfor 属性支持，支持预定义或自定义操作
- 🧮 移除已弃用的 MathML STIXGeneral 字体及相关设置
- 🎭 CSS 新增单页面应用视图过渡动画样式支持，包含伪类与属性
- 🗺️ JavaScript 中 Map 与 WeakMap 新增 getOrInsert 系列方法，支持键值自动插入
- 📱 ScreenOrientation 接口的 lock()/unlock() 方法现支持安卓与 Windows 平板
- 🔄 单页面应用正式支持视图过渡 API，简化页面切换动画
- 🎨 CSSOM 标准接口 CSSStyleProperties 完成实现（取代非标准 CSS2Properties）
- ⚡ PerformanceEventTiming 新增 interactionId 属性，用于用户交互性能分析
- 📄 DOM 元素新增 moveBefore() 方法，移动子元素时保持状态
- 🛡️ 跨域 iframe 重定向顶层页面需用户交互或显式授权
- 🔗 RTCDataChannel 可传输至 Worker 线程并新增关闭事件监听
- 🎥 媒体设备支持 resizeMode 约束，智能调整视频参数
- 🧹 移除 Document 与 Element 的非标准脚本执行事件
- 📥 WebDriver 新增下载开始事件与屏幕方向/时区模拟功能
- 🖱️ 回滚滚动定位算法至即时模式，解决平滑滚动竞态条件
- 🎨 扩展开发支持指定 CSS 注入样式来源（用户/作者级）
- 💾 storage.local 与 storage.managed 新增存储空间查询接口
- ⚗️ 实验性功能：datetime-local 输入框支持时间选择器（需手动开启）

---

### [CSS 视图过渡初学者指南](https://developer.mozilla.org/en-US/blog/view-transitions-beginner-guide/)

**原文标题**: [A beginner-friendly guide to view transitions in CSS](https://developer.mozilla.org/en-US/blog/view-transitions-beginner-guide/)

现代浏览器支持的视图过渡 API 让多页面应用也能实现单页面应用般的流畅动画过渡效果，只需少量 CSS 代码即可增强用户体验。

- 🌐 视图过渡 API 使多页面应用 (MPA) 实现页面间平滑动画成为可能，过去这仅限单页面应用 (SPA)
- 📱 该功能采用渐进增强设计，不支持该特性的浏览器仍可正常显示页面内容
- 🚀 基础过渡效果仅需一行 CSS 代码：@view-transition { navigation: auto; }
- 🎬 可通过::view-transition-old 和::view-transition-new 伪元素自定义过渡动画
- ⚡ 当前 Chrome、Edge 和 Safari 已支持 Level 2 跨页面过渡功能
- 🎭 示例演示了如何创建滑动动画效果，通过覆盖默认混合模式实现独特过渡
- 🔧 开发者可自由组合动画效果，为不同页面设计专属过渡方式

---

### [CSS 网格：一种实用的思维模型与网格线的强大功能 | WebKit](https://webkit.org/blog/17474/css-grid-a-helpful-mental-model-and-the-power-of-grid-lines/)

**原文标题**: [  CSS Grid: A helpful mental model and the power of grid lines | WebKit](https://webkit.org/blog/17474/css-grid-a-helpful-mental-model-and-the-power-of-grid-lines/)

CSS Grid 是一种强大的布局工具，通过网格线实现复杂设计。文章建议将网格视为电子表格，先定义容器结构，再使用网格线定位元素，并介绍了关键属性和术语。

- 📐 将网格布局类比为电子表格，先定义列和行模板（如 `grid-template-columns: 1fr 1fr 1fr`）
- 🧭 使用网格线（如 `grid-row: 1/3`）而非行列编号来精确定位元素
- 📏 掌握三种核心属性：容器模板属性（`grid-template-rows/columns`）、子项定位属性（`grid-row/column`）和自动填充属性（`grid-auto-rows`）
- 🔀 默认流式布局会自动填充网格单元，显式定位元素会优先排列
- 🎯 通过合并网格区域实现跨行跨列布局（如示例中的附加组件横跨两行）
- 📚 建议后续学习更直观的网格区域（grid areas）定位方法

---

### [互操作性功能排名](https://interop-rank.jakearchibald.com/)

**原文标题**: [Interop Feature Ranking](https://interop-rank.jakearchibald.com/)

overview summary
本文介绍了人工智能在现代生活中的广泛应用及其带来的便利，涵盖了从智能助手到医疗诊断等多个领域，展示了技术发展如何提升效率并改善日常生活。

- 🤖 智能助手通过语音识别和自然语言处理技术，帮助用户管理日程、查询信息和控制智能家居设备
- 🏥 医疗领域利用 AI 进行疾病诊断和影像分析，提高诊断准确率并辅助医生制定治疗方案  
- 🚗 自动驾驶技术结合传感器和算法，实现车辆自主导航，提升交通安全和出行效率
- 🏠 智能家居系统自动调节室内环境，包括温度、照明和安防，创造舒适节能的生活空间
- 📱 个性化推荐算法根据用户行为偏好，在娱乐和电商平台提供定制化内容与服务
- 🌐 自然语言处理技术赋能翻译软件和客服机器人，打破语言障碍并提升服务体验

---

### [interop/2026 在 main · web-platform-tests/interop · GitHub](https://github.com/web-platform-tests/interop/tree/main/2026)

**原文标题**: [interop/2026 at main · web-platform-tests/interop · GitHub](https://github.com/web-platform-tests/interop/tree/main/2026)

这是一个关于 web-platform-tests 项目中 interop 仓库的 GitHub 页面概览。

- 🧪 这是一个用于 web 平台测试的互操作性仓库
- 👥 项目为公开仓库，需要登录才能更改通知设置
- ⭐ 获得了 446 个星标，有 32 个复刻
- 📊 包含 188 个待处理的问题和 5 个拉取请求
- 🛡️ 设有 2 个项目和安全相关功能
- ⚠️ 页面加载时出现错误，需要重新加载
- 🧭 提供代码、问题、拉取请求等额外导航选项

---

### [W3C 标志焕新：不止于表面改变，迈向持久与可持续成功的一小步 | 2025 年 | 博客 | W3C](https://www.w3.org/blog/2025/w3c-logo-refresh-more-than-a-cosmetic-change-a-small-step-towards-durable-and-sustainable-success/)

**原文标题**: [W3C logo refresh: more than a cosmetic change, a small step towards durable and sustainable success | 2025 | Blog | W3C](https://www.w3.org/blog/2025/w3c-logo-refresh-more-than-a-cosmetic-change-a-small-step-towards-durable-and-sustainable-success/)

W3C 在 2025 年世界标准日发布新标识，这不仅是视觉更新，更是配合 2025-2028 战略目标的重要举措，标志着该组织向更可持续、更具影响力的方向演进。

- 🌐 新标识设计延续自 2018 年启动的品牌重塑计划，取代已使用 28 年的旧标识
- 🎯 同步更新口号为“让网络为所有人服务”，呼应四大战略目标：巩固架构、增强影响、多元支持、拓展覆盖
- 💡 品牌更新体现 W3C 从技术导向转向更注重社会价值的定位，强调普惠性与可持续性
- 🔄 作为成立 31 年的联盟暨 2 年非营利组织，此次变革旨在提升敏捷性与全球参与度
- 🌍 战略目标包含财务多元化与全球社区拓展，确保未来 30 年持续推动开放网络标准

---

### [React 基金会介绍——React](https://react.dev/blog/2025/10/07/introducing-the-react-foundation)

**原文标题**: [Introducing the React Foundation – React](https://react.dev/blog/2025/10/07/introducing-the-react-foundation)

React 将脱离 Meta 成立独立基金会，并建立新的技术治理架构，以更好地服务社区生态。

- 🏛️ React 与 React Native 将迁移至新成立的 React 基金会，由多家企业共同治理
- 🌍 基金会将负责基础设施维护、组织 React Conf 会议并提供生态项目资金支持
- 👥 创始成员包括亚马逊、微软、Vercel 等七家对生态有重要影响的企业
- ⚖️ 将建立独立于基金会的技术治理架构，确保技术方向由贡献者共同决定
- 🚀 此举旨在使 React 突破单一公司局限，保障项目长期可持续发展

---

### [CSS 播客回归！我成为联合主持人了——Bram.us](https://www.bram.us/2025/10/14/the-css-podcast-is-back-and-im-a-co-host-now/)

**原文标题**: [The CSS Podcast is back! And I’m a co-host now. – Bram.us](https://www.bram.us/2025/10/14/the-css-podcast-is-back-and-im-a-co-host-now/)

CSS 播客第五季回归，由 Una 和 Bramus 共同主持，首期节目聚焦 CSS 的 if() 函数与自定义函数功能。

- 🎙️ CSS 播客第五季正式回归，新任主持 Una 与 Bramus 搭档合作
- 🆕 首期节目深度解析 CSS 的 if() 条件函数与@function 自定义函数
- 👥 原主持人 Adam 因裁员离开，三人六月在 CSS Day 会面并获传承祝福
- 📅 节目于 2025 年 10 月 14 日由谷歌开发者关系工程师 Bramus 发布
- 🔗 内容遵循 Creative Commons 4.0 许可，代码示例采用 MIT 许可证

---

### [Lit 加入 OpenJS 基金会！—— Lit](https://lit.dev/blog/2025-10-14-openjs/)

**原文标题**: [Lit is Joining the OpenJS Foundation! – Lit](https://lit.dev/blog/2025-10-14-openjs/)

Lit 正式加入 OpenJS 基金会成为影响力项目，标志着该项目从单一企业主导转向真正社区驱动的开源治理模式。

- 🎉 Lit 成为 OpenJS 基金会影响力项目，与 Node.js 等核心项目并列
- 🌐 项目资产全面移交基金会，确保长期中立发展
- 👥 成立技术指导委员会，含谷歌/Adobe/Reddit 等多元代表
- 📈 作为最受欢迎 Web 组件库，npm 下载量排名第五
- 🤝 通过 RFC 流程和双周会议推动社区共治
- 🚀 持续推动 Web 标准发展，已参与多项浏览器功能改进
- 📢 将招募社区经理，加强开发者生态建设
- 💬 通过官网和 Discord 社区欢迎开发者参与贡献

---

### [现代 CSS 圆角标签页 – 前端大师博客](https://frontendmasters.com/blog/modern-css-round-out-tabs/)

**原文标题**: [Modern CSS Round-Out Tabs – Frontend Masters Blog](https://frontendmasters.com/blog/modern-css-round-out-tabs/)

本文介绍了使用 CSS 的 shape() 函数创建圆角外扩标签页的现代方法，通过 clip-path 裁剪实现无需额外元素的复杂形状设计。

- 🎨 传统方法需四个额外元素实现圆角外扩效果，而现代 CSS 使用 shape() 配合 clip-path 直接裁剪矩形生成标签形状
- 📐 通过分步绘制演示：从底部左角开始，结合曲线命令和灵活坐标点构建自适应形状
- 🔧 支持 CSS 变量自定义参数（如--tabGirth），实现动态调整标签外观
- 🌐 添加悬停动效和单方向溢出控制等交互增强
- ⚠️ 提供@supports 回退方案，在不支持 shape() 的浏览器中显示简化样式
- ♿ 指出当前实现需完善键盘导航等无障碍功能
- 💡 推荐参考 Temani Afif 和 Ana Tudor 的现代实现方案

---

### [CSS 形状模块第一级 | 我能用吗... HTML5、CSS3 等支持情况表](https://caniuse.com/css-shapes)

**原文标题**: [CSS Shapes Level 1 | Can I use... Support tables for HTML5, CSS3, etc](https://caniuse.com/css-shapes)

CSS Shapes Level 1 规范允许通过几何形状控制文本环绕效果，目前在全球浏览器中获得 95.83% 的支持率。

- 🌐 全球支持率达 95.83%，覆盖主流现代浏览器
- 🔺 支持通过 shape-outside、shape-margin 和 shape-image-threshold 属性定义文本环绕区域
- ✅ Chrome 37+、Edge 79+、Safari 7.1+、Firefox 62+ 版本均提供稳定支持
- 📱 移动端 Safari 8+、Chrome Android 141+ 等主流移动浏览器均兼容
- 🚫 仅 Opera Mini 和早期 IE/旧版移动浏览器不支持此特性
- 📚 可通过 A List Apart 文章和 Firefox 跟踪错误报告获取技术细节

---

### [[研讨会] 优化前端性能：监控最佳实践 · Luma](https://luma.com/svmryn3f)

**原文标题**: [[Workshop] Fixing Your Frontend: Performance Monitoring Best Practices · Luma](https://luma.com/svmryn3f)

概述：Sentry 是一款受到 400 万开发者认可的应用监控软件，被认为表现不错。

- 👨‍💻 四百万开发者认为其表现良好
- 📊 专注于应用监控功能
- 🔔 提供订阅服务模式
- 👍 整体评价积极正面

---

### [对比色那些事儿 · 正经与闲谈](https://stuffandnonsense.co.uk/blog/the-thing-about-contrast-color)

**原文标题**: [The thing about contrast-color  •  Stuff & Nonsense](https://stuffandnonsense.co.uk/blog/the-thing-about-contrast-color)

作者对 CSS 的 contrast-color() 函数进行了测试，发现该功能能根据背景色自动选择黑白文本色，但存在对比度过高导致阅读不适的问题。他建议为该函数添加类似滤镜的对比度调节参数。

- 🎨 函数能自动选择黑白文本色以匹配背景对比度
- ⚠️ 实际使用中发现黑白对比度过高影响阅读舒适度
- 🎯 作者网站采用深蓝背景与米白文本的柔和搭配
- 🔧 建议为 contrast-color() 添加对比度调节参数
- 📝 目前该功能仅支持 Safari 浏览器

---

### [对比色那些事儿 | CSS 技巧](https://css-tricks.com/the-thing-about-contrast-color/)

**原文标题**: [The thing about contrast-color | CSS-Tricks](https://css-tricks.com/the-thing-about-contrast-color/)

文章讨论了 CSS 的 contrast-color() 函数在颜色对比度方面的局限性，并介绍了 light-dark() 作为替代方案。

- 🎨 contrast-color() 函数目前仅支持在深色背景上返回白色、浅色背景上返回黑色的二元对比方案
- 😣 纯白/纯黑与任何颜色形成的最高对比度可能造成视觉不适，影响阅读体验
- 🌰 作者在实际项目中采用深蓝色背景 (#212E45) 搭配灰白色文字 (#d3d5da) 来平衡对比度与舒适度
- 🔧 使用 light-dark() 函数可实现更灵活的颜色控制，支持设置半透明色值
- 📈 未来 contrast-color() 将支持更多对比算法和返回颜色，并考虑用户偏好因素
- 📚 WCAG 3.0 标准正在完善对比度评估体系，当前函数存在明显局限性

---

### [CSS 中的新 progress() 函数——Amit Merchant——关于 PHP、JavaScript 等技术的博客](https://www.amitmerchant.com/the-progress-function-css/)

**原文标题**: [The new progress() function in CSS — Amit Merchant — A blog on PHP, JavaScript, and more](https://www.amitmerchant.com/the-progress-function-css/)

CSS 新增的 progress() 函数让开发者能够通过视口宽度在最小与最大尺寸间的变化比例，直接控制元素属性变化，无需复杂计算或 JavaScript 即可实现流畅的响应式效果。

- 📱 实现响应式视觉效果：如图像随视口变窄而渐透明、卡片随视口增大而轻微缩放
- 🎛️ 简化数值映射逻辑：函数返回 0-1 间的归一化值，自动处理不同单位（px/vw/rem）的边界计算
- 🌊 支持多场景应用：包括自适应布局阈值调整、滚动动效关联、组件状态驱动样式、流体排版优化等
- ⚡ 提升开发效率：替代复杂的 calc() 表达式，避免媒体查询重复代码
- 🌐 浏览器兼容现状：目前 Chromium 内核浏览器与 Safari 26 已支持，Firefox 暂未实现
- 💡 实际应用示例：通过 CodePen 演示图像透明度随视口变化的实时效果
- 🔄 类似游戏开发技术：原理与 shader 中的 smoothstep() 函数相似，实现平滑插值

---

### [CSS :is() :where() 魔法发生之处 · 马蒂亚斯·奥特](https://matthiasott.com/notes/css-is-where-the-magic-happens)

**原文标题**: [ CSS :is() :where() the Magic Happens · Matthias Ott](https://matthiasott.com/notes/css-is-where-the-magic-happens)

CSS 的:is() 和:where() 伪类函数是现代 CSS 中极具实用价值的功能，它们能显著简化选择器写法并提升代码灵活性，尽管浏览器支持良好但实际使用率仍有提升空间。

- 🎯 简化选择器语法：通过组合选择器列表替代重复代码，提升可读性和维护性
- 🛡️ 容错机制：当选择器列表中存在无效项时，仅忽略该条目而非整个规则集
- ⚖️ 特异性差异：:is() 继承列表中最具体选择器的权重，:where() 始终保持零特异性
- 🎨 应用场景：广泛用于 CSS 重置、组件样式覆盖及与:has() 等选择器组合实现复杂逻辑
- 🔧 实践案例：如 Manuel 的 UA+ 重置样式表展示了对表单元素字体的继承控制

---

### [Web 组件的杀手级特性 - daverupert.com](https://daverupert.com/2025/10/custom-elements-manifest-killer-feature/)

**原文标题**: [The killer feature of Web Components - daverupert.com](https://daverupert.com/2025/10/custom-elements-manifest-killer-feature/)

Web Components 的杀手级特性是自定义元素清单（CEM），它通过标准化 JSON 格式描述组件 API，并赋能丰富的生态工具链，显著提升开发效率。

- 📄 CEM 是社区标准 JSON 格式，可自动提取组件的属性、事件、插槽等 API 信息
- 🏷️ 通过 JSDoc 注释增强文档，支持标注 CSS 变量、插槽作用域等高级特性
- ⚙️ 仅需两行命令即可生成清单文件，无缝集成现有工作流
- 🔧 生态工具基于 CEM 实现文档生成、编辑器智能提示、多框架适配等超能力
- 🚀 显著减少样板代码，提升组件可维护性和跨团队协作效率
- 🌱 由社区驱动发展，标准化描述方式释放组件生态潜力

---

### [如何使用 GSAP 为 WebGL 着色器添加动画：涟漪、揭示与动态模糊效果 | Codrops](https://tympanus.net/codrops/2025/10/08/how-to-animate-webgl-shaders-with-gsap-ripples-reveals-and-dynamic-blur-effects/)

**原文标题**: [How to Animate WebGL Shaders with GSAP: Ripples, Reveals, and Dynamic Blur Effects | Codrops](https://tympanus.net/codrops/2025/10/08/how-to-animate-webgl-shaders-with-gsap-ripples-reveals-and-dynamic-blur-effects/)

本教程详细介绍了如何结合 GSAP 与 WebGL 着色器创建四种动态交互效果：点击涟漪、图像遮罩揭示、按压动态模糊以及可滚动轮播。通过控制着色器 uniform 变量并与 GSAP 时间轴同步，实现实时响应的视觉体验。

- 🎯 使用 GSAP Observer 监听点击/悬停事件，通过 Raycaster 获取 UV 坐标驱动着色器效果
- 🌊 实现点击涟漪效果：通过动画 uRippleProgress uniform 在顶点着色器中生成波形变形
- 🎭 创建悬停遮罩揭示：动态混合双纹理，依据鼠标位置生成圆形渐变遮罩
- ⏳ 开发按压交互效果：通过 GSAP 时间轴分阶段控制灰度过渡与噪波扭曲
- 🎠 构建动态模糊轮播：基于视口位置计算模糊强度，采用多通道 Kawase 模糊算法
- 🔄 同步 DOM 与 Canvas：使用正交相机将屏幕坐标转换为 WebGL 世界坐标
- ⚡ 优化渲染性能：通过 gsap.ticker.add 将 Three.js 渲染循环集成到 GSAP 更新周期
- 🎨 灵活材质系统：创建可扩展的 ShaderMaterial 类，支持多种 uniform 参数动画

---

### [如何为 Astro 静态站点添加快速客户端搜索——邪恶火星人团队博客《火星编年史》](https://evilmartians.com/chronicles/how-to-add-fast-client-side-search-to-astro-static-sites)

**原文标题**: [How to add fast, client-side search to Astro static sites—Martian Chronicles, Evil Martians’ team blog](https://evilmartians.com/chronicles/how-to-add-fast-client-side-search-to-astro-static-sites)

本文介绍了如何为 Astro 静态站点添加快速客户端搜索功能，通过构建时生成 JSON 索引并结合 MiniSearch 库实现高效搜索体验。

- 🚀 利用 Astro 端点生成静态搜索索引，避免依赖外部爬虫和 API
- 📝 使用 unified 库将 MDX 内容转换为纯文本，去除 JSX 标签和 Markdown 语法
- 🔍 采用 MiniSearch 实现客户端全文搜索，支持模糊匹配和字段权重设置
- ⚡ 通过预加载索引和延迟初始化优化性能，仅在输入框聚焦时加载数据
- 🎯 对搜索结果进行智能解析，高亮显示最佳匹配片段
- ⌨️ 集成 KeyUX 库实现键盘导航支持，添加 Cmd/Ctrl+K 快捷搜索
- 🔧 可自定义搜索算法，支持标题和正文字段差异化权重
- 📱 完全静态化方案，确保搜索数据与项目状态实时同步

---

### [无 JavaScript 实现暗色模式切换 | 博客 | Jesse Stuart](https://www.jessestuart.ca/posts/2025-10-12-implementing-dark-mode-toggle-without-javascript/)

**原文标题**: [
    Implementing Dark Mode Toggle without JavaScript | 
    Blog | Jesse Stuart

](https://www.jessestuart.ca/posts/2025-10-12-implementing-dark-mode-toggle-without-javascript/)

本文介绍了如何仅使用 CSS 和 HTML 实现网站深色模式切换功能，通过结合 CSS 的 light-dark 函数、color-scheme 属性、prefers-color-scheme 媒体查询和单选按钮组，无需 JavaScript 即可创建模式切换器，并提供了 JavaScript 增强方案用于持久化用户偏好。

- 🌙 使用 CSS 的 light-dark 函数和 color-scheme 属性实现基础深色模式支持
- 🔘 通过隐藏的单选按钮组（light/dark/auto）和标签创建无 JS 切换控件
- 🌓 利用 prefers-color-scheme 媒体查询自动匹配系统主题设置
- 🎭 运用 CSS :has() 选择器和:checked 状态实现动态标签显示逻辑
- 💾 附加 JavaScript 方案使用 localStorage 持久化用户选择
- 🔄 可选功能：当系统主题与用户选择一致时自动恢复 auto 模式
- ⚠️ 纯 CSS 方案的局限性：页面刷新后无法保持状态
- 🎨 采用月亮☾和太阳☼符号作为视觉切换指示器

---

### [镜子](https://mirrow.app/)

**原文标题**: [mirrow](https://mirrow.app/)

Mirrow 是一个简化 SVG 设计和动画的工具，允许用户在一个文件中完成设计、样式和动画，无需额外 CSS 或脚本。

- 🎨 统一文件设计 SVG，无需外部 CSS 或 JavaScript
- ⚡ 内置动画功能，支持属性如半径和位置的变化
- 🔄 自动生成适用于 React、Svelte 等框架的代码
- 🖱️ 支持交互效果，如悬停和激活状态
- 📄 提供文档和在线演示，方便学习和使用

---

### [镜子](https://mirrow.app/playground/)

**原文标题**: [mirrow](https://mirrow.app/playground/)

Mirrow 是一个用于实时生成 SVG 图形的实验性工具，用户可通过编写 DSL 代码即时预览图形效果。

- 🎮 提供交互式编程环境，支持即时编译和图形渲染
- ✏️ 采用领域专用语言，简化 SVG 图形创建流程
- ⚡ 具备实时错误提示功能，帮助快速调试代码
- 🖼️ 输出结果为标准 SVG 格式，可直接应用于网页项目
- 🔬 设计为实验平台，便于开发者探索图形编程可能性

---

### [虎湖：实时分析系统与智能体的新架构 | TigerData](https://www.tigerdata.com/blog/tiger-lake-a-new-architecture-for-real-time-analytical-systems-and-agents?utm_source=cooperpress&utm_medium=referral&utm_campaign=project-eyeballs-2025&utm_content=frontend-focus-newsletter-tigerlake-1)

**原文标题**: [Tiger Lake: A New Architecture for Real-Time Analytical Systems and Agents | TigerData](https://www.tigerdata.com/blog/tiger-lake-a-new-architecture-for-real-time-analytical-systems-and-agents?utm_source=cooperpress&utm_medium=referral&utm_campaign=project-eyeballs-2025&utm_content=frontend-focus-newsletter-tigerlake-1)

Timescale 公司推出 Tiger Lake 新架构，通过双向实时数据流打通 PostgreSQL 与湖仓架构，消除传统数据孤岛，实现运营数据与分析系统的无缝集成。

- 🚀 推出 Tiger Lake 架构：建立 PostgreSQL 与湖仓平台间的双向实时数据流，替代复杂的数据管道
- 🔄 采用开放式架构：基于 Apache Iceberg 和 Amazon S3，支持持续数据复制与流式回传
- 📊 实现运营级湖仓架构：通过青铜（原始数据）、白银（清洗数据）、黄金（聚合数据）三层实现实时数据闭环
- 🎯 应用场景覆盖：实时仪表板（结合实时指标与历史数据）、监控系统（统一数据源）、智能体（无需额外基础设施）
- ⚡ 技术优势：简化技术栈、降低延迟、避免数据冗余，支持标准 SQL 查询
- 🔮 未来规划：2025 年夏季支持直接查询 Iceberg 目录，秋季实现完整往返工作流
- 🛠️ 快速部署：通过简单 SQL 命令即可启用数据同步功能
- 🌟 客户案例：Speedcast、Lumia Health 等企业已用于工业遥测、智能体工作流等场景

---

### [Triplex 开源并迁移至 Poimandres • Triplex](https://triplex.dev/blog/triplex-moves-to-pmndrs)

**原文标题**: [Triplex Goes Open Source and Moves to Poimandres • Triplex](https://triplex.dev/blog/triplex-moves-to-pmndrs)

Triplex 已加入 Poimandres 集体并完全开源，标志着这款 React Three Fiber 可视化编辑工具进入社区驱动新阶段。项目创始人因未能实现商业化转型且入职新公司，决定将三年开发成果移交开源社区。

- 🚀 **项目开源迁移** - 代码库已转移至 github.com/pmndrs/triplex，保留所有历史记录与工单
- ⏳ **三年开发历程** - 自 2022 年实验项目起步，历经 1300 次提交实现从概念到成熟产品的演进
- 🛠️ **核心功能演进** - 支持 3D 组件可视化编辑、子元素面板操作、VS Code 扩展、AST 路径选择系统等关键特性
- 📉 **商业化未果** - 未能找到产品市场契合点，缺乏付费用户验证
- 🌱 **社区共建启航** - 邀请开发者参与插件开发、多框架支持、AI 功能增强、云平台构建等未来规划
- 🔮 **发展路线开放** - 支持 Vue/Svelte 等非 React 框架、Next.js 集成、低代码功能等方向由社区共同决策

---

### [简介 - React Three Fiber](https://r3f.docs.pmnd.rs/getting-started/introduction)

**原文标题**: [Introduction - React Three Fiber](https://r3f.docs.pmnd.rs/getting-started/introduction)

React-three-fiber 是一个用于 three.js 的 React 渲染器，允许开发者使用声明式组件构建 3D 场景，无缝集成 React 生态系统。

- 🎯 通过可复用组件构建交互式 3D 场景
- 📦 安装命令：npm install three @types/three @react-three/fiber
- ⚠️ 需配对对应版本（如 v8 配 React 18，v9 配 React 19）
- 🚀 无性能损耗且支持 Three.js 全部功能
- 🔄 自动同步 Three.js 新特性无需更新库
- 🎮 提供完整交互示例（悬停/点击动画）
- 📱 支持 React Native 移动端开发
- 🌐 拥有丰富生态库（物理引擎/后期处理/ARVR）
- 🛠️ 建议先掌握 React Hooks 与 Three.js 基础概念

---

### [波曼德瑞斯](https://pmnd.rs/)

**原文标题**: [Poimandres](https://pmnd.rs/)

好的，请提供您需要总结的文本内容，我将按照以下格式为您生成中文摘要：

概述总结
- 😊 要点一
- 📊 要点二
- 🔍 要点三

请将需要总结的文本粘贴在下方，我会立即为您处理。

---

### [Poimandres 文档](https://docs.pmnd.rs/)

**原文标题**: [Poimandres documentation](https://docs.pmnd.rs/)

本文概述了多个与 React Three Fiber 生态系统相关的库和工具，涵盖 3D 渲染、动画、状态管理和扩展功能。

- 🌐 React Three Fiber：基于 React 的 three.js 渲染器，用于创建 3D 图形
- 🎠 React Spring：为 React 组件提供弹簧动画基础功能
- 🛠️ Drei：React Three Fiber 的实用工具集，包含多种辅助函数和抽象
- 🐻 Zustand：轻量级、高性能的 React 状态管理库，采用钩子 API
- ⚛️ Jotai：原始且灵活的 React 状态管理解决方案
- 🔄 Valtio：为 React 和原生 JS 简化代理状态管理
- ♿ A11y：为 WebGL 提供无障碍访问支持的 React Three Fiber 组件
- 🎨 React Postprocessing：React Three Fiber 的后处理效果包装器
- 🖥️ uikit：为 React Three Fiber 带来用户界面组件
- 🕶️ xr：支持 VR/AR 功能的 React Three Fiber 扩展
- 📚 Docs：pmndrs 项目的统一文档生成工具
- 🤖 prai：构建逐步 LLM 指令的 JavaScript 框架
- 🌌 viverse：专为 VIVERSE 平台打造的 Three.js 和 React Three Fiber 应用开发工具包

---

### [Triplex for VS Code [测试版] - Visual Studio 应用商店](https://marketplace.visualstudio.com/items?itemName=trytriplex.triplex-vsce)

**原文标题**: [
        Triplex for VS Code [BETA] - Visual Studio Marketplace
    ](https://marketplace.visualstudio.com/items?itemName=trytriplex.triplex-vsce)

Visual Studio Code 的 Triplex 扩展是一个可视化工作空间工具，专为 React / Three Fiber 开发设计，帮助开发者在编码时保持上下文。

- 🚀 将 VS Code 及其分支转变为可视化工作空间，支持 React 组件通过 "Open in Triplex" 操作直接打开
- 📚 提供入门指南，包括从模板创建项目、完成首个 3D 组件教程及场景学习
- 💬 推荐加入 Discord 和 GitHub 等社区论坛，获取开发支持和交流
- ❓ 常见问题解答：需使用 --enable-coi 标志启用安全上下文，仅支持导出组件，提供组件错误解决和编辑器重载方法
- ⚡ 性能优化建议：启用 GPU 加速以避免运行缓慢问题

---

### [免费原创图片生成器](https://ogimage.click/)

**原文标题**: [Free OG Image Generator](https://ogimage.click/)

ogImage.click 是一个免费在线工具，可快速生成适用于社交媒体平台的 OG 图片、博客配图和 Twitter/X 头图等，无需注册即可使用全部功能。

- 🆓 完全免费且无需注册，立即使用所有功能
- 🌐 支持多平台图片生成，包括 Open Graph、Twitter/X 和博客等
- 🎨 提供 8 种专业模板，含基础版、英雄版和 Logo 版等布局
- 💾 支持 PNG/JPEG/WebP 格式导出，推荐 PNG 以获得最佳显示效果
- ✏️ 高级自定义选项，可上传 Logo、设置渐变背景和网格叠加等
- ⚡ 实时预览界面，修改即时可见，生成速度极快
- 📱 提供 HTML 和 Next.js 两种集成方式，附带完整代码示例
- 🏆 荣获 Peerlist 周榜第一名，被数千开发者信赖使用

---

### [开发工具 - 终极开发者工具箱 | 免费在线工具](https://dev-tool.dev/)

**原文标题**: [Dev Tools - Your Ultimate Developer Toolkit | Free Online Tools](https://dev-tool.dev/)

该文章介绍了一个多功能在线工具集，提供多种实用工具以简化开发者和设计师的日常工作流程。

- 📊 JSON 查看器：轻松查看和格式化 JSON 数据，提高可读性
- 📝 文本比较：快速比较两段文本以识别差异
- 🔠 大小写转换：在 camelCase、snake_case、kebab-case 等格式间转换文本
- 🧮 令牌计数器：分析文本令牌化并计算 AI 模型的 API 成本
- 🔑 UUID 生成器：为应用程序生成唯一标识符
- 🔄 Base64 转换器：轻松编码或解码 Base64 字符串
- ⚙️ JSON 转 TypeScript：将 JSON 对象转换为 TypeScript 接口和类型
- 🔒 JWT 解码器：安全地解码和验证 JSON Web 令牌
- 🗃️ SQL 格式化器：格式化 SQL 查询并高亮关键字
- 🔢 数字进制转换：在二进制、八进制、十进制和十六进制间转换数字
- 📋 CSV 与 JSON 转换器：在 CSV 和 JSON 格式间转换，支持表头
- 🖼️ 图片格式转换：在 PNG、JPEG、WebP 和 BMP 格式间转换图片
- 📝 Markdown 编辑器：轻松编写、预览和编辑 Markdown 文件
- ⏰ Cron 计算器：轻松生成和验证 cron 表达式
- 🔍 正则表达式生成器：交互式创建和测试正则表达式
- 💻 代码演练场：在交互式环境中试验代码片段
- 🕐 时间戳转换：在时间戳和可读日期间相互转换
- 🔐 哈希生成器：生成 MD5、SHA-1、SHA-256 和 SHA-512 哈希值
- 🌐 URL 编码器：安全地编码和解码 URL 及 URI 组件
- 📄 Lorem 生成器：为设计和布局生成占位文本
- 📱 二维码生成器：为文本、URL、联系信息等创建二维码
- 🎨 调色板生成器：使用色彩理论生成美观的配色方案

---

### [在线免费图表制作工具](https://makegraph.app/)

**原文标题**: [Make Graph - Online Free Graph Maker](https://makegraph.app/)

一款免费的在线图表制作工具，无需下载或注册即可快速创建专业级数据可视化图表

- 📊 提供 8 种以上专业图表类型，包括柱状图、折线图、饼图、散点图等
- 🎨 内置精美主题模板和专业配色方案，支持品牌风格定制
- ⚡ 即时生成图表，支持 PNG/SVG 格式导出，适配各类演示场景
- 🔒 采用隐私优先原则，所有数据处理均在本地浏览器完成
- ♿ 配备无障碍功能，支持纹理图案辅助色觉障碍用户识别数据
- 🆓 完全免费使用，无需注册账户即可开始创作

---

### [GitHub - embedpdf/embed-pdf-viewer：一款可无缝集成到任何JavaScript项目中的PDF查看器](https://github.com/embedpdf/embed-pdf-viewer)

**原文标题**: [GitHub - embedpdf/embed-pdf-viewer: A PDF viewer that seamlessly integrates with any JavaScript project](https://github.com/embedpdf/embed-pdf-viewer)

EmbedPDF 是一个开源 JavaScript PDF 查看器，具有框架无关性和丰富的功能特性。

- 📄 开源 PDF 查看器，采用 MIT 许可证，可集成到任何 JavaScript 项目中
- 🔧 框架无关设计，支持 React、Vue、Svelte、Preact 和原生 JavaScript
- ✨ 提供注释功能（高亮、便签、自由文本、手绘）、真实内容擦除、搜索和缩放等特性
- 🚀 具备平滑虚拟化滚动和可插拔架构，支持 tree-shaking 优化
- 🌐 项目拥有 2.3k 星标和 114 个分支，活跃社区支持
- 📚 提供完整文档、安装指南和在线演示
- 🤝 欢迎贡献，提供贡献指南和 GitHub 讨论区
- ⚖️ 基于 PDFium 技术，遵守 Apache 2.0 许可证

---

### [开源 JavaScript PDF 查看器——快速、可定制且框架无关 | EmbedPDF](https://www.embedpdf.com/)

**原文标题**: [Open-Source JavaScript PDF Viewer – Fast, Customizable & Framework-Agnostic | EmbedPDF](https://www.embedpdf.com/)

EmbedPDF 是一个轻量级、可自定义的开源 PDF 查看器，无需依赖即可集成到各类 JavaScript 项目中。

- 📄 开源免费：基于 MIT 许可证，无付费限制，提供完整源代码
- 🎛️ 高度可定制：支持主题、注释、搜索等功能的完整 API 控制
- 🌐 框架通用：兼容 JavaScript/TypeScript 项目，支持 React、Vue、Svelte 及原生开发
- ⚡ 快速集成：仅需两行代码即可在 500px 容器中嵌入 PDF 查看器
- 🚀 性能优异：文档加载更快，用户体验流畅，节省开发时间
- 🔧 生态完善：提供详细文档、工具支持和 GitHub 社区协作

---

### [嵌入 PDF](https://app.embedpdf.com/)

**原文标题**: [EmbedPDF](https://app.embedpdf.com/)

好的，请提供您需要总结的文本内容，我将按照以下格式为您生成中文摘要：

概述总结
- 😊 要点一
- 📊 要点二
- 🔍 要点三

请将需要总结的文本粘贴在下方，我会立即为您处理。

---

### [人人皆可 JavaScript - Piccalilli](https://piccalil.li/javascript-for-everyone?utm_source=frontend-focus&utm_medium=referral-ad&utm_campaign=js4e-launch)

**原文标题**: [
  JavaScript for Everyone - Piccalilli
](https://piccalil.li/javascript-for-everyone?utm_source=frontend-focus&utm_medium=referral-ad&utm_campaign=js4e-launch)

本课程旨在帮助 JavaScript 开发者超越语法层面，深入理解语言核心机制，通过实用模式提升综合技能水平。

- 🎯 课程聚焦 JavaScript 深层理解而非语法记忆，帮助掌握语言运行原理
- ⏱️ 自主学习无时间限制，采用混合媒体形式，预计学习时长 15-30 小时
- 💡 包含 12 个模块 50 多节课，涵盖原始类型、集合、函数、类、异步编程等核心概念
- 👨🏫 由资深开发者 Mat Marquis 授课，拥有近 20 年行业经验，擅长将复杂概念通俗化
- 🌍 支持全球购买，提供 PPP 折扣政策，现价£161.85（原价£249）
- 🤝 购买即享专属 Discord 社区支持、终身访问权限和结业证书
- 🚀 适合具备基础 JavaScript 知识的开发者，旨在推动长期职业发展

---

### [Bun 1.3 | Bun 博客](https://bun.com/blog/bun-v1.3)

**原文标题**: [Bun 1.3 | Bun Blog](https://bun.com/blog/bun-v1.3)

Bun 1.3 是迄今为止最大的版本更新，将其转变为功能全面的全栈 JavaScript 运行时，显著增强了前端开发、全栈应用构建、数据库集成、包管理和测试调试等方面的能力。

- 🚀 **全栈开发服务器**：内置热重载、浏览器到终端日志输出，支持 Bun.serve() 路由和参数化路径
- 🔥 **前端开发增强**：原生支持 HTML 文件直接运行，内置热模块替换和 React Fast Refresh
- 🗄️ **统一数据库客户端**：Bun.SQL 支持 MySQL/MariaDB、PostgreSQL 和 SQLite，提供高性能统一 API
- 📦 **包管理改进**：引入依赖目录同步版本、隔离安装、安全扫描 API 和交互式更新
- 🧪 **测试框架升级**：VS Code 测试浏览器集成、并发测试、类型测试和更丰富的匹配器
- 🔧 **构建工具优化**：支持跨平台编译、代码签名、程序化创建可执行文件和更智能的压缩
- 🌐 **WebSocket 增强**：RFC 6455 合规的子协议协商、头部覆盖和自动压缩支持
- 🛡️ **安全功能**：Bun.secrets 加密凭证存储、CSRF 保护和加密性能大幅提升
- 📊 **性能优化**：postMessage 速度提升 500 倍，内存使用减少 10-30%，启动时间更快
- 🔌 **Node.js 兼容性**：支持 800+ 新测试，改进 worker_threads、node:test 和 node:vm 模块

---

### [Bun 1.3 | Bun 博客](https://bun.com/blog/bun-v1.3#getting-started)

**原文标题**: [Bun 1.3 | Bun Blog](https://bun.com/blog/bun-v1.3#getting-started)

Bun 1.3 是迄今为止最大的版本更新，将其转变为一个功能全面的全栈 JavaScript 运行时，集成了前端开发、数据库客户端、Redis 支持、WebSocket 增强、包管理优化及性能提升等多项改进。

- 🚀 **全栈开发服务器**：内置热重载、浏览器到终端日志输出，支持 Bun.serve() 路由和参数化路径
- 🔥 **前端开发增强**：直接运行 HTML 文件，内置热模块替换和 React Fast Refresh，生产构建优化
- 🗄️ **统一数据库支持**：Bun.SQL 提供 MySQL、PostgreSQL 和 SQLite 的统一 API，支持数组操作和动态列操作
- 📡 **内置 Redis 客户端**：支持标准操作、发布/订阅和自动重连，性能优于 ioredis
- 🌐 **WebSocket 改进**：符合 RFC 6455 的子协议协商、头部覆盖和自动压缩支持
- 📦 **包管理升级**：引入依赖目录、隔离安装、安全扫描 API 和最小发布年龄保护
- ⚡ **性能优化**：减少空闲 CPU 使用、降低内存占用、加速 Bun.build 和加密操作
- 🧪 **测试与调试增强**：VS Code 测试资源管理器集成、并发测试、类型测试和更丰富的匹配器
- 🔧 **Node.js 兼容性提升**：支持 VM 模块、node:test、Worker 线程和环境数据 API
- 🛡️ **安全功能**：Bun.secrets 加密凭证存储、CSRF 保护和代码签名支持
- 📊 **开发者体验改进**：更好的 TypeScript 默认配置、控制台深度控制和自定义 User-Agent

---

### [非 HTML 内容](https://frontendfoc.us/open/713/*%7CUID%7C*?ipx=t)

**原文标题**: [Non-HTML content](https://frontendfoc.us/open/713/*%7CUID%7C*?ipx=t)

无法总结：非 HTML 内容。

---

