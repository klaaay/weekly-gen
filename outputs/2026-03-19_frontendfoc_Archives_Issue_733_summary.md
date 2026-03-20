### [前端聚焦第 733 期：2026 年 3 月 18 日](https://frontendfoc.us/issues/733)

**原文标题**: [Frontend Focus Issue 733: March 18, 2026](https://frontendfoc.us/issues/733)

本期《前端聚焦》简报涵盖 JPEG 压缩技术原理、网页性能优化、CSS 新功能、前端开发工具更新及多个实用资源与教程。

- 🖼️ JPEG 压缩技术深度解析：探讨其基于人类视觉偏见的文件压缩机制
- 📊 网页性能警示：新闻网站单页加载可达 49MB 数据，揭示资源优化迫切性
- 🪵 结构化日志实践：推荐使用 LogTape 和 Sentry 替代 console.log 进行生产环境调试
- 🌐 网络效率监控：Edge 146 实验功能可识别需优化的首方/第三方资源
- 🎨 CSS 色彩突破：contrast-color() 函数现可返回黑白外的丰富色彩
- 📰 行业动态速览：包括 BaseWatch 基线功能追踪、CSS 时间提案、Chrome 登陆 ARM64 Linux 等
- 🎯 前端技术实践：涵盖可定制 select 元素应用、CSS 方法论探讨、内存泄漏实证研究
- 🛠️ 工具生态更新：Vite 8.0 支持 Wasm SSR，Astro 6.0 新增字体 API，Clerk 发布可视化主题编辑器
- 🧩 开发资源集锦：包含 ArtPlayer 视频组件、Starwind UI 组件库、Color API 色彩工具等
- 👁️ 视觉敏感度测试：互动网站可检测用户色彩辨别能力的"最小可觉差"

---

### [王苏菲](https://www.sophielwang.com/blog/jpeg)

**原文标题**: [Sophie Wang](https://www.sophielwang.com/blog/jpeg)

本文介绍了人工智能在医疗领域的应用现状与前景，重点探讨了其在疾病诊断、治疗方案优化及医疗管理效率提升方面的作用，并指出面临的挑战与未来发展方向。

- 🏥 AI 辅助诊断系统能通过分析医学影像快速识别病灶，提高早期疾病检出率
- 💊 基于机器学习的个性化治疗方案可结合患者数据优化用药与治疗路径
- 📊 智能医疗管理平台能整合临床数据，减少医护人员行政负担
- 🔬 基因组学与 AI 结合助力精准医疗发展，实现靶向治疗突破
- ⚠️ 数据隐私保护与算法透明度仍是亟待解决的核心伦理问题
- 🌐 跨机构医疗数据共享机制的建立将推动 AI 医疗规模化落地

---

### [49MB 的网页 | thatshubham](https://thatshubham.com/blog/news-audit)

**原文标题**: [The 49MB Web Page | thatshubham](https://thatshubham.com/blog/news-audit)

现代新闻网站为了短期广告收益，牺牲用户体验，导致页面臃肿、加载缓慢，并充满干扰性设计，将读者置于敌对境地。

- 📰 **页面臃肿不堪**：访问《纽约时报》查看四个标题，竟触发 422 个网络请求，下载 49MB 数据，页面两分钟才稳定，相当于下载了整张专辑。
- 🏗️ **技术倒退对比**：49MB 的网页数据量远超 Windows 95 系统（28 张软盘），也相当于 10-12 首高质量 MP3 歌曲，与过去有限的宽带速度形成讽刺对比。
- 🕵️ **过度追踪与性能损耗**：新闻网站嵌入大量跟踪 JavaScript，在后台进行程序化广告竞价，消耗 CPU 与电量，侵犯用户隐私。
- 🚫 **敌对用户体验设计**：为提升“可见性”和“页面停留时间”指标，网站采用弹窗、自动播放视频、布局偏移等设计，增加用户交互成本。
- 📱 **移动端体验窒息**：宝贵的屏幕空间被固定栏、广告和模态窗口占据，实际内容区域仅占约 11%，迫使读者频繁滚动。
- 💡 **解决方案与希望**：可通过延迟弹窗、预留广告空间、使用轻量版网站（如 text.npr.org）或 RSS 订阅来改善体验，平衡商业与用户需求。
- 🔄 **系统性问题根源**：这种架构源于无数局部合理的商业决策，将用户注意力视为可提取资源，而非尊重读者。

---

### [使用 LogTape 和 Sentry 将 console.log 替换为结构化日志记录](https://sentry.io/cookbook/structured-logging-logtape/?utm_source=frontendfocus&utm_medium=paid-community&utm_campaign=logs-fy27q1-cookbook&utm_content=newsletter-logtape-primary-trysentry)

**原文标题**: [Replace console.log with structured logging using LogTape | Sentry](https://sentry.io/cookbook/structured-logging-logtape/?utm_source=frontendfocus&utm_medium=paid-community&utm_campaign=logs-fy27q1-cookbook&utm_content=newsletter-logtape-primary-trysentry)

本文介绍了如何使用 LogTape 和 Sentry 将 console.log 替换为结构化、可追踪的日志记录，以提升生产环境调试效率。

- 🛠️ **安装与配置**：安装 LogTape 及其 Sentry 接收器，配置客户端和服务端日志记录，支持隐式和显式上下文管理。
- 🔍 **结构化日志记录**：用结构化对象替代字符串日志，包含用户 ID、订单详情等关键数据，使日志可查询、易调试。
- 🌐 **前端集成**：通过 React 上下文提供器自动附加会话数据到前端日志，组件可便捷获取上下文丰富的记录器。
- 🧩 **日志过滤与分类**：使用过滤器控制日志级别，避免生产环境噪音；通过嵌套分类（如`['my-app', 'checkout']`）组织日志，便于在 Sentry 中按域查询。
- 🔗 **追踪关联**：Sentry 自动将日志与追踪 ID 关联，在错误发生时可在同一追踪视图中查看相关日志、错误和会话回放。
- 📊 **查询与告警**：在 Sentry 日志浏览器中基于结构化属性（如用户 ID、订单 ID）查询日志，并可创建告警和仪表板监控关键模式。
- 💡 **最佳实践**：建议在关键节点记录丰富上下文而非频繁记录，避免敏感数据，并合理设置日志级别以控制成本与噪音。

---

### [获取失败](https://frontendfoc.us/link/182350/web)

**原文标题**: [Failed to retrieve](https://frontendfoc.us/link/182350/web)

无法总结：获取内容失败，状态码 403。

---

### [una.im | 超越黑白对比的 contrast-color()](https://una.im/advanced-contrast-color/)

**原文标题**: [una.im | contrast-color() beyond black & white](https://una.im/advanced-contrast-color/)

本文介绍了 CSS 新特性`contrast-color()`的两种进阶用法，该功能可基于背景色自动返回对比度最高的黑色或白色文本颜色，但原计划的多色选项未纳入 v1 标准。文章提供了两种方法扩展其应用：一是使用`color-mix()`混合品牌色生成柔和色调，二是通过样式查询和自定义属性构建完整调色板系统。

- 🎨 **方法一：使用 color-mix() 混合色调**  
  通过将`contrast-color()`返回的黑/白色与品牌色按比例混合（浅色建议 10–25%，深色建议 30–40%），可在保持可访问性的同时增添色彩个性。需搭配 WCAG 或 APCA 对比度检查工具验证效果。

- 🧩 **方法二：样式查询构建自定义调色板**  
  结合`@property`注册自定义属性、样式查询及`if()`函数，可基于背景色明暗动态切换完整配色方案。此方法需手动测试颜色组合，但能实现高度定制化的动态主题。

- ⚠️ **注意事项与浏览器支持**  
  两种方法均需开发者自行验证颜色对比度。方法一依赖样式查询，目前仅 Chrome 147+ 和 Safari 26+ 完全支持；方法二需 Chrome 137+，但可通过`@container style()`语法获得更广兼容性。

- 🌟 **核心价值**  
  `contrast-color()`本质是明暗检测器，为动态主题设计提供基础判断。开发者可借此实现从简单色调混合到完整调色板系统的灵活控制，但最终色彩可访问性责任仍在于人工测试。

---

### [contrast-color() - CSS | MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/contrast-color)

**原文标题**: [contrast-color() - CSS | MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/contrast-color)

CSS 的`contrast-color()`函数用于根据输入颜色自动生成对比色（黑色或白色），以提升文本可读性，但需注意其浏览器兼容性有限且在某些颜色背景下可能无法满足所有可读性需求。

- 🎨 **功能作用**：接收一个颜色值，返回对比度最高的白色或黑色，常用于确保符合 WCAG AA 最低对比度标准
- ⚠️ **使用限制**：中色调背景可能无法与黑白文本形成足够对比，建议搭配浅色或深色背景使用
- 🌐 **兼容性**：非基线功能，部分主流浏览器尚未支持，需使用`@supports`进行特性检测
- 💡 **应用场景**：自动设置按钮文本颜色、适配深浅色模式，减少手动维护颜色配对的工作量
- 🔧 **语法示例**：`color: contrast-color(var(--button-color))`可直接在 CSS 中调用
- 📚 **相关标准**：属于 CSS Color Module Level 5 规范，与`prefers-color-scheme`等媒体查询配合使用效果更佳

---

### [BaseWatch — 追踪 CSS 与浏览器功能支持，获取基线提醒](https://basewatch.dev)

**原文标题**: [BaseWatch â Track CSS & Browser Feature Support, Get Baseline Alerts](https://basewatch.dev)

本文介绍了人工智能在医疗领域的应用现状与前景，重点探讨了其在疾病诊断、治疗方案优化及医疗管理效率提升方面的作用，并指出相关技术发展面临的挑战与伦理考量。

- 🏥 AI 辅助诊断系统能通过分析医学影像快速识别病灶，提高早期疾病检出率
- 💊 基于机器学习的个性化治疗方案可结合患者数据优化用药与治疗路径
- 📊 智能医疗管理平台整合临床数据，助力医院资源调度与远程医疗服务
- ⚠️ 数据隐私保护与算法透明度仍是当前技术落地需要解决的关键问题
- 🔮 未来 AI 将与人类医生协同工作，推动精准医疗和预防性医疗体系发展

---

### [[css-values][css-conditional][css-animations] 基于时间的 CSS 提案 · 第 13655 号议题 · w3c/csswg-drafts · GitHub](https://github.com/w3c/csswg-drafts/issues/13655)

**原文标题**: [[css-values][css-conditional][css-animations] Proposal for time-based CSS · Issue #13655 · w3c/csswg-drafts · GitHub](https://github.com/w3c/csswg-drafts/issues/13655)

该提案旨在讨论在 CSS 中引入基于用户本地时间的条件、动画和值支持，以增强样式与时间的动态关联。

- 🕐 **时间驱动样式**：提议在 CSS 中直接集成用户本地时间，避免依赖脚本设置自定义属性或动画，提升代码内聚性和健壮性。
- 🎨 **动态主题应用**：例如，迷你游戏可根据一年中的日期生成颜色主题，每日自动更新背景颜色组合。
- 📅 **时间表高亮**：在活动时间表中，根据当前时间高亮显示进行中的行，并控制滚动对齐方式。
- 🕒 **条件显示控制**：例如，在特定时间自动显示或隐藏活动横幅，无需额外脚本干预。
- ⏱️ **时间轴动画**：支持基于一天中的时间或特定时间点触发动画，如模拟时钟动画或新年倒计时效果。

---

### [浏览器状态日网络盛会](https://remysharp.com/2026/03/18/web-of-state-of-the-browser-day-out)

**原文标题**: [Web of State of the Browser Day Out](https://remysharp.com/2026/03/18/web-of-state-of-the-browser-day-out)

作者参加了“State of the Browser”和“Web Day Out”两场活动，强烈推荐参与此类会议。活动不仅提供了实用的技术见解，还营造了包容、进步的社区氛围，让作者深受启发并重新思考了个人与社区的价值。

- 🌐 **State of the Browser**：以可访问性和开放网络为核心，涵盖 CSS 新特性、性能优化等话题，强调社区包容性。
- 🎤 **演讲亮点**：包括 CSS 锚点定位、内向性格工作法、时间 API Temporal 的演进，以及性能与可访问性的实践经验。
- 🛠️ **Web Day Out**：注重实践应用，分享 CSS 新功能、Baseline 项目预测、字体排版进展等可直接落地的技术内容。
- 👥 **社区价值**：活动间的交流让作者感受到进步社区的温暖，强调平等、分享与代表性，与其个人价值观高度契合。
- 💡 **个人收获**：激发编码灵感，深化对网络社区作为进步微社会的认同，并思考如何将社区精神扩展到更广泛领域。

---

### [SotB14 | 浏览器现状第 14 期](https://2026.stateofthebrowser.com/)

**原文标题**: [SotB14 | State of the Browser 14](https://2026.stateofthebrowser.com/)

State of the Browser 14 会议已结束，期待明年再见。

- 🗣️ 最新公布的演讲嘉宾包括 Zach Leatherman、Jason Williams 等
- 🌐 伦敦 Web 标准组织致力于团结专业人士，共同推动网络发展
- 📅 每月举办聚会，涵盖 HTML、JavaScript、CSS、可访问性等主题

---

### [2026 年 3 月 12 日布莱顿网络日游](https://webdayout.com/)

**原文标题**: [Web Day Out in Brighton, March 12th 2026](https://webdayout.com/)

本次网络日活动聚焦于当前浏览器技术的最新应用，于 2026 年 3 月 12 日举行，旨在深入探讨可直接投入使用的网页平台功能。

- 🌐 活动主题围绕现代浏览器技术的即时应用展开
- 📅 于 2026 年 3 月 12 日举行，包含八位专家演讲
- 🔧 内容涵盖 HTML、CSS 及 JavaScript 最新平台特性
- 📸 活动当日通过照片集锦记录精彩瞬间
- 🎤 汇聚九位行业专家包括 Jemima Abu、Rachel Andrew 等
- 🗓️ 官网提供完整日程安排供参与者查阅
- 📬 设有邮件订阅服务持续更新活动资讯

---

### [Chromium 博客：将 Chrome 引入 ARM64 Linux 设备](https://blog.chromium.org/2026/03/bringing-chrome-to-arm64-linux-devices.html)

**原文标题**: [
Chromium Blog: Bringing Chrome to ARM64 Linux Devices
](https://blog.chromium.org/2026/03/bringing-chrome-to-arm64-linux-devices.html)

谷歌将于 2026 年第二季度为 ARM64 Linux 设备推出 Chrome 浏览器，延续其在 Arm 架构设备上的扩展，旨在为更多用户提供安全、稳定且功能丰富的浏览体验，并深化与开源社区及硬件伙伴的合作。

- 🚀 **发布计划**：Chrome 将于 2026 年第二季度登陆 ARM64 Linux 设备，延续其在 Arm 架构的 macOS（2020 年）和 Windows（2024 年）上的扩展。
- 🌐 **生态整合**：通过登录谷歌账户，用户可跨设备同步书签、历史记录和标签页，并直接访问 Chrome 网上应用店中的扩展程序，无需额外工具或开发者设置。
- 🔒 **安全防护**：提供增强型安全浏览功能，利用 AI 和已知威胁列表实时防御网络钓鱼和恶意软件；集成谷歌支付和密码管理器，支持安全支付和跨设备密码管理。
- 🤝 **行业合作**：与英伟达合作，简化其 DGX Spark AI 超算设备的 Chrome 安装流程；其他 Linux 发行版用户也可通过 chrome.com/download 获取 ARM64 版本。
- 🎯 **用户体验**：致力于为 ARM64 Linux 用户提供与其他平台一致的优质浏览体验，满足对开源 Chromium 项目与谷歌服务生态结合的需求。

---

### [滥用自定义选择器 | CSS 技巧](https://css-tricks.com/abusing-customizable-selects/)

**原文标题**: [Abusing Customizable Selects | CSS-Tricks](https://css-tricks.com/abusing-customizable-selects/)

本文介绍了如何利用新的可自定义 `<select>` 功能，通过 CSS 和 HTML 创建有趣且视觉丰富的交互式选择器演示，包括曲线文件夹堆栈、扇形卡片组和圆形表情符号选择器，并强调了渐进增强和浏览器兼容性。

- 🎨 通过 `appearance: base-select` 和 `::picker()` 伪元素启用可自定义选择器样式，解锁完整样式能力
- 📁 在第一个演示中，使用 `sibling-index()` 函数和 CSS 变换创建曲线文件夹堆栈，并利用 `@starting-style` 实现平滑动画
- 🃏 第二个演示通过自定义 `<button>` 覆盖默认选中内容，结合 `sibling-index()` 和 `sibling-count()` 实现扇形卡片展开效果
- ⭕ 第三个演示利用 `anchor()` 函数和 CSS 三角函数（`cos()`、`sin()`）将选项排列为圆形布局
- 🔧 所有演示均保持 `<select>` 元素的原始可访问性和功能，在不支持的浏览器中会优雅降级为普通选择器
- 🚀 强调可自定义选择器作为渐进增强功能，即使在新特性支持有限的情况下也能正常使用

---

### [CSS 中没有“错误”](https://www.sitepoint.com/there-is-no-wrong-in-css/)

**原文标题**: [There Is No “Wrong” in CSS](https://www.sitepoint.com/there-is-no-wrong-in-css/)

本文探讨了 CSS 中是否存在“错误”写法，认为只要代码有效且无实际弊端，就不应被视作错误。CSS 的灵活性和平台责任意味着开发者有调整自由，而用户访问障碍应由平台机制解决，非开发者全责。

- 🛠️ 只要 CSS 代码有效且未造成明显用户体验或开发体验问题，就没有必要改变它，因为 Web 平台强调向后兼容性。
- 🧑‍💻 如果 CSS 存在特定问题（如不支持 RTL 布局），责任在于开发者自身根据需求调整，而非遵循外部绝对规则。
- 🔄 CSS 易于修改，即使使用旧技术（如浮动布局），也可随时替换为更好方案，因此难以构成无法纠正的严重错误。
- 🌐 用户访问障碍主要应由 Web 平台负责解决，平台应确保开发者意图易于实现且不易造成使用壁垒，而非单纯归咎于 CSS 写法。
- 🧠 面对他人对 CSS 的批评，需结合具体情境判断建议是否适用，避免教条主义，最终 CSS 的多样性允许以不同方式解决设计问题。

---

### [面向 React 网页开发者的博览会](https://expo.dev/solutions/expo-for-react-web-devs?utm_source=frontendfocus&utm_medium=email&utm_campaign=33087804-React%2520to%2520Native&utm_content=react-to-native-lp)

**原文标题**: [Expo for React web devs](https://expo.dev/solutions/expo-for-react-web-devs?utm_source=frontendfocus&utm_medium=email&utm_campaign=33087804-React%2520to%2520Native&utm_content=react-to-native-lp)

Expo 是一个基于 React Native 的框架，让熟悉 React 的 Web 开发者能够使用现有技能构建 iOS 和 Android 原生应用，无需重新学习或使用 Xcode 等原生开发工具。

- 🚀 **React 技能复用**：开发者可直接运用 React 的组件化开发模式，使用 JavaScript/TypeScript 编写跨平台应用代码
- 📱 **原生性能体验**：React Native 渲染的是真正的平台原生 UI 元素，而非 Webview，确保应用性能与用户体验
- 🔄 **统一代码库**：通过 Expo Router 和 API Routes 实现 iOS、Android 和 Web 平台共享代码，包括导航和后端逻辑
- 🛠️ **开发工具完善**：提供文件路由系统（类似 Next.js）、原生 API 封装（相机/推送等）、自动化构建服务（EAS Build），无需配置原生开发环境
- 🌟 **社区高度认可**：被 Meta 推荐使用，拥有 100 多个维护良好的开源库，开发者社区反馈积极
- 📚 **学习资源丰富**：提供详细文档、教程和 12 分钟快速入门指南，帮助 React 开发者快速过渡到移动开发

---

### [前端内存泄漏：基于 500 个仓库的静态分析与五种场景基准研究](https://stackinsight.dev/blog/memory-leak-empirical-study/)

**原文标题**: [Frontend Memory Leaks: A 500-Repository Static Analysis and Five-Scenario Benchmark Study](https://stackinsight.dev/blog/memory-leak-empirical-study/)

本文通过对 500 个开源仓库进行静态分析，并结合五种场景的基准测试，系统研究了前端内存泄漏的普遍性和实际影响。研究发现，86% 的仓库存在至少一种未清理资源的代码模式，总计发现 55,864 个潜在泄漏点。基准测试表明，每种未清理的模式在每个组件挂载/卸载周期中平均导致约 8 KB 的堆内存无法回收，且这种增长是线性累积的。

- 🕵️ **静态分析发现**：扫描了 714,217 个文件，在 430 个仓库中发现了 55,864 个未清理资源的模式，其中定时器清理缺失（43.9%）和事件监听器移除缺失（19.0%）是最常见的问题。
- ⚙️ **框架分布**：React 仓库的问题数量最多（占 62.3%），Vue 占 28.2%，Angular 占 9.5%。这与样本中 React 仓库数量较多有关，但也反映了各框架特定的易漏模式。
- ⏱️ **定时器是主要问题**：`setTimeout`和`setInterval`没有对应清理的情况占总发现的 40.1%，成为最常见的泄漏来源。
- 📊 **基准测试结果**：在五种典型场景（如 React 的`useEffect`事件监听、Vue 的`onMounted`定时器、Angular 的订阅等）中，未清理的“坏”版本在每个周期平均导致约 8 KB 内存无法回收，而正确清理的“好”版本内存增长近乎为零。
- 📈 **线性累积效应**：泄漏是确定性的，每个周期泄漏量稳定。例如，一个具有 3 个泄漏模式的组件，在用户进行 100 次导航后，可能累积约 2.4 MB 的无法回收内存。
- 📱 **实际影响**：在移动设备上，这种累积内存可能触发浏览器标签被系统终止；在长期运行的桌面应用（如 Electron 应用）中，可能导致应用逐渐变慢。
- 🛠️ **修复简单**：大多数情况下，修复只需添加一行清理代码（如在`useEffect`中返回清理函数，或在 Vue 的`onUnmounted`、Angular 的`ngOnDestroy`中执行清理操作）。
- 🔍 **检测建议**：工程团队应优先审计定时器、事件监听器和订阅的清理情况，并考虑在生产环境中监控堆内存增长趋势。
- ⚠️ **注意事项**：研究存在一些局限性，例如测试使用合成组件、静态分析可能存在误报/漏报、测试环境为 Node.js 而非真实浏览器等。

---

### [使用锚定容器查询构建动态切换提示 - Piccalilli](https://piccalil.li/blog/building-dynamic-toggletips-using-anchored-container-queries/)

**原文标题**: [
  Building dynamic toggletips using anchored container queries - Piccalilli
](https://piccalil.li/blog/building-dynamic-toggletips-using-anchored-container-queries/)

本文介绍了如何使用锚定容器查询构建动态切换提示，结合弹出层、锚点定位等现代 CSS 特性，实现根据空间自动调整位置的交互效果。

- 🚀 Chrome 143 引入锚定容器查询，可基于锚点位置动态调整元素样式
- 🎯 使用弹出层（popover）和锚点属性实现语义化标记与定位关联
- 🔧 通过现代 attr() 函数或传统 CSS 渐进增强建立锚点关联
- 📐 利用 position-area 和 position-try 实现智能定位与翻转
- 🎨 使用 corner-shape 创建圆滑边角，支持优雅降级
- 🔍 通过 @container anchored() 查询检测定位状态并调整提示符位置
- 🧩 采用渐进增强策略，确保功能在不支持新特性的浏览器中仍可工作

---

### [使用 Three.js、Velocity 和情绪背景构建滚动响应的 3D 画廊 | Codrops](https://tympanus.net/codrops/2026/03/09/building-a-scroll-reactive-3d-gallery-with-three-js-velocity-and-mood-based-backgrounds/)

**原文标题**: [Building a Scroll-Reactive 3D Gallery with Three.js, Velocity, and Mood-Based Backgrounds | Codrops](https://tympanus.net/codrops/2026/03/09/building-a-scroll-reactive-3d-gallery-with-three-js-velocity-and-mood-based-backgrounds/)

本文介绍了一个使用 Three.js 构建的滚动响应式 3D 画廊教程，结合深度分层图像、调色板驱动的背景和基于滚动速度的动态效果，旨在创造一种沉浸式的浏览体验。

- 🎨 教程核心：构建一个基于滚动驱动的 WebGL 画廊，通过 Three.js 实现深度分层图像、调色板背景和动态响应效果
- 🏗️ 系统架构：基于三个核心概念——深度（Z 轴分层）、氛围（图像调色板驱动背景）和动态（滚动速度作为交互信号）
- 📐 技术实现：使用 Vite、Three.js 和原生 JavaScript，采用模块化类结构管理场景、画廊、滚动和背景
- 🖼️ 图像处理：每个图像携带自定义调色板，背景根据滚动位置在调色板之间平滑过渡
- 🎮 交互设计：滚动速度驱动微动效果，包括视差、漂移和呼吸动画，增强空间感和响应性
- 🌪️ 视觉增强：添加了动态轨迹效果，使用 Catmull-Rom 样条曲线创建流畅的引导路径
- 📝 编辑层：支持添加文本标签和颜色信息，使画廊适合产品展示或故事叙述
- 🔮 扩展可能：可替换图像内容、深化速度信号应用，或添加音频交互提升沉浸感

---

### [大气深度画廊 | Codrops](https://tympanus.net/Tutorials/DepthGallery/)

**原文标题**: [Atmospheric Depth Gallery | Codrops](https://tympanus.net/Tutorials/DepthGallery/)

大气深度画廊是一个基于 WebGL 和 Three.js 的交互式视觉项目，通过动态色彩布局和滚动交互，模拟大气层的深度与色彩变化。

- 🌌 项目使用 Three.js 和 WebGL 技术构建，实现高性能的视觉渲染
- 🎨 色彩布局灵感来源于@thisislandscape，呈现大气层的渐变色调
- 🖱️ 支持滚动交互，用户可通过滚动探索不同深度层次
- 🔧 按 D 键可开启调试工具，便于开发者查看技术细节
- 📁 提供所有演示案例和 GitHub 代码仓库，方便参考与学习

---

### [错误](https://frontendfoc.us/link/182363/web)

**原文标题**: [Error](https://frontendfoc.us/link/182363/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='meiert.com', port=443): Max retries exceeded with url: /blog/astro-html-minification/ (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1000)')))

---

### [4 个让 Tailwind 成为布局构建利器的理由 | CSS 技巧](https://css-tricks.com/4-reasons-that-make-tailwind-great-for-building-layouts/)

**原文标题**: [4 Reasons That Make Tailwind Great for Building Layouts | CSS-Tricks](https://css-tricks.com/4-reasons-that-make-tailwind-great-for-building-layouts/)

Tailwind CSS 因其与 HTML 结构紧密关联、无需命名布局、适应上下文变化及灵活响应式设计等优势，在构建页面布局时表现出色，尤其适合通过实用类快速实现清晰、可维护的布局结构。

- 🏗️ 布局样式与 HTML 结构高度依赖，Tailwind 的实用类（如 `grid-cols-3`、`col-span-2`）或 CSS 变量（如 `[--cols:3]`）使布局在代码中直观可见，无需在 CSS 中重新构建心智模型。
- 🏷️ 避免为布局命名困难，传统类名（如 `.two-columns`）无法准确描述布局细节，而 Tailwind 直接用数值表达（如 `[--span:4]`），让结构一目了然。
- 🔄 布局需求随上下文变化，Tailwind 允许直接调整间距（如 `gap-8` 与 `gap-4`）或最大宽度（如 `max-w-[12em]`），无需创建多余修饰类，适应不同场景。
- 📱 响应式变体可即时创建，通过 Tailwind 的响应式前缀（如 `md:[--cols:5]`），能灵活调整布局在不同断点的列数，避免 CSS 膨胀，保持代码简洁。

---

### [原生 JSON 模块终于成为现实 - 马特·史密斯](https://allthingssmitty.com/2026/03/16/native-json-modules-are-finally-real/)

**原文标题**: [
    Native JSON modules are finally real - Matt Smith
  ](https://allthingssmitty.com/2026/03/16/native-json-modules-are-finally-real/)

原生 JSON 模块现已正式成为 JavaScript 标准，通过 import 属性实现直接导入，无需构建工具转换。

- 🎉 原生 JSON 模块支持：使用`import config from "./config.json" with { type: "json" }`语法，浏览器和运行时可直接解析 JSON 文件
- 🔑 显式类型声明：必须添加`with { type: "json" }`属性，明确告知运行时按 JSON 解析而非执行代码
- ⚡ 运行时解析：JSON 在首次导入时获取并解析，遵循标准 ESM 缓存机制，相同模块共享实例
- 🛠️ 平台责任转移：从构建工具模拟转向平台原生支持，但仍需服务器正确设置`Content-Type: application/json`
- 📦 与构建工具对比：原生方案无需构建步骤，支持原始 ESM，但缺少内联、资源哈希等构建时优化
- 🌐 更广泛的应用前景：导入属性模式为 CSS 模块等其他结构化类型铺平道路，使模块系统更显式和可扩展

---

### [Vite 8.0 正式发布！ | Vite](https://vite.dev/blog/announcing-vite8)

**原文标题**: [Vite 8.0 is out! | Vite](https://vite.dev/blog/announcing-vite8)

Vite 8.0 正式发布，采用 Rust 编写的 Rolldown 作为统一打包工具，带来高达 10-30 倍的构建速度提升，同时保持完整的插件兼容性。此次更新还包括插件目录 registry.vite.dev 的推出、多项新功能增强，以及对 Node.js 版本的要求更新。

- 🚀 **性能飞跃**：Vite 8 集成 Rolldown 作为单一 Rust 打包工具，构建速度提升 10-30 倍，并完全兼容现有 Vite 和 Rollup 插件。
- 🌐 **插件生态**：推出官方插件目录 registry.vite.dev，方便开发者查找适用于 Vite、Rolldown 和 Rollup 的插件。
- ⚡ **开发体验**：新增内置开发工具、TypeScript 路径别名支持、装饰器元数据支持、Wasm SSR 支持及浏览器控制台转发功能。
- 🔧 **配套更新**：同步发布 @vitejs/plugin-react v6，改用 Oxc 处理 React Refresh，减少依赖并缩小安装体积。
- 📈 **实测效果**：多家企业实测显示生产构建时间大幅减少，如 Linear 从 46 秒降至 6 秒，部分项目提升达 64%。
- 🛠️ **未来规划**：正在开发完整打包模式、原始 AST 传输、原生 MagicString 转换等功能，以进一步提升性能与开发效率。
- 📦 **安装体积**：因集成 lightningcss 和 Rolldown，安装体积增加约 15 MB，团队将持续优化以减少大小。
- 🔄 **迁移指南**：提供平滑迁移路径，多数项目无需配置更改，复杂项目建议先试用 rolldown-vite 包再升级至 Vite 8。
- 🙏 **致谢社区**：特别感谢 Rollup 和 esbuild 团队的历史贡献，以及社区在测试和反馈中的关键作用。

---

### [关于 Vite 8、Vite+ 与 Void 的一切须知](https://www.builder.io/blog/vite-8-vite-plus-void)

**原文标题**: [Everything You Need to Know about Vite 8, Vite+, and Void](https://www.builder.io/blog/vite-8-vite-plus-void)

Vite 8 带来了基于 Rust 的核心工具链，显著提升了构建速度和开发体验，同时 Vite+ 和 Void 共同构建了一个更完整的平台生态系统，旨在提供一体化的开发与部署工作流。

- 🚀 **Vite 8 核心更新**：采用 Rust 工具链（Rolldown 和 Oxc），构建速度提升 10-30 倍，实现开发与生产环境一致性，并内置开发者工具等改进。
- 🛠️ **架构优化**：统一工具链减少插件支持复杂度，为未来优化奠定基础，提升长期稳定性。
- 📦 **Vite+ 平台化工具链**：整合 Vite、Vitest、Oxlint 等工具，提供统一 CLI，专注于工作流和 monorepo 支持，目前以 MIT 许可证开源。
- ☁️ **Void 部署平台**：基于 Cloudflare Workers，支持一键部署全栈应用，提供后端 SDK 和自动资源调配，但需注意平台锁定风险。
- 🔄 **升级建议**：建议大多数项目升级 Vite 8，但需测试兼容性；Vite+ 适合工具链复杂的团队；Void 适用于快速开发的全栈项目，但需评估长期灵活性。
- 🌍 **生态影响**：Vite 作为多个现代前端框架的基础，其更新影响广泛，标志着前端工具链的重要演进。

---

### [核心 3](https://clerk.com/changelog/2026-03-03-core-3?utm_source=cooper_press&utm_medium=newsletter&utm_campaign=core-3&utm_content=03-18-26&dub_id=0ZhEAQup5kJGkZbh)

**原文标题**: [Core 3](https://clerk.com/changelog/2026-03-03-core-3?utm_source=cooper_press&utm_medium=newsletter&utm_campaign=core-3&utm_content=03-18-26&dub_id=0ZhEAQup5kJGkZbh)

Clerk 发布了 Core 3 SDK 重大更新，重点改进了自定义 API、主题编辑器、无密钥模式支持、现代 React 兼容性和性能优化。

- 🛠️ **改进的自定义 API**：重新设计了`useSignIn`、`useSignUp`、`useCheckout`钩子，新增`useWaitlist`钩子，简化自定义认证界面开发。
- 🎨 **主题编辑器与交互式文档**：提供可视化组件定制工具，支持实时预览和代码复制。
- 🔑 **扩展无密钥模式**：新增支持 TanStack Start、Astro 和 React Router 框架，无需配置 API 密钥即可快速体验。
- ⚛️ **现代 React 支持**：优化以兼容 React 并发渲染特性（如过渡、Suspense 和流式 SSR），避免状态同步冲突。
- 🚀 **性能提升**：减小包体积约 50KB，优化卫星域名重定向策略，改进离线处理和令牌获取效率。
- 📦 **其他更新**：简化包名、统一`<Show>`组件、自动主题切换、Vite 环境变量自动检测等。
- ⚠️ **废弃项**：Clerk Elements 和`@clerk/types`包已被废弃，推荐使用新钩子和内置类型导出。

---

### [Astro 6.0 | Astro](https://astro.build/blog/astro-6/)

**原文标题**: [Astro 6.0 | Astro](https://astro.build/blog/astro-6/)

Astro 6.0 正式发布，带来了一系列新功能和改进，包括内置字体 API、内容安全策略 API、实时内容集合支持，并重构了开发服务器和构建管道，以提升开发与生产环境的一致性。此外，还引入了实验性的 Rust 编译器、队列渲染和路由缓存等功能，并升级了核心依赖包。

- 🚀 **重构开发服务器**：利用 Vite 新环境 API，开发时可直接运行生产环境，减少开发与生产环境差异，特别优化了 Cloudflare 等非 Node.js 运行时的支持。
- 🌐 **内置字体 API**：简化自定义字体配置，自动处理下载、缓存、优化回退字体和预加载链接，提升网站性能与隐私保护。
- 🔄 **实时内容集合**：支持请求时获取外部托管内容，无需重新构建即可实时更新，与现有内容集合 API 无缝集成。
- 🛡️ **内容安全策略**：提供内置 CSP 配置，自动哈希脚本和样式，支持静态和动态页面，增强网站安全性。
- 📦 **升级核心依赖**：包括 Vite 7、Shiki 4 和 Zod 4，并需 Node 22 或更高版本，以提升性能和安全性。
- ⚙️ **实验性 Rust 编译器**：作为 Go 编译器的后继者，提供更快的速度和更可靠的诊断，可通过标志启用。
- ⚡ **实验性队列渲染**：采用两遍渲染策略，提升渲染速度和内存效率，计划在 Astro v7 中默认启用。
- 💾 **实验性路由缓存**：提供平台无关的缓存 API，支持服务器渲染响应的缓存控制，集成实时内容集合自动失效功能。
- 👥 **社区贡献**：感谢核心团队及众多贡献者的代码、文档和测试支持，推动 Astro 6 的发布。

---

### [GitHub - zhw2590582/ArtPlayer: :art: ArtPlayer.js 是一款现代化且功能齐全的 HTML5 视频播放器 · GitHub](https://github.com/zhw2590582/ArtPlayer)

**原文标题**: [GitHub - zhw2590582/ArtPlayer: :art: ArtPlayer.js is a modern and full featured HTML5 video player · GitHub](https://github.com/zhw2590582/ArtPlayer)

ArtPlayer.js 是一款功能丰富且易于使用的现代 HTML5 视频播放器，支持高度自定义和多种插件集成。

- 🎥 **功能全面**：支持 HTML5 视频播放，可自定义控件，并轻松集成 flv.js、hls.js 等流媒体库。
- 📦 **易于安装**：可通过 npm、yarn 或 CDN 快速安装，支持模块化和全局变量使用。
- 🔌 **插件丰富**：提供弹幕、字幕、画中画、广告等多种官方插件，扩展播放器功能。
- 🌐 **格式支持**：直接兼容 .vtt、.ass、.srt 字幕格式，并支持 HLS、DASH 等流媒体协议。
- 📄 **开源项目**：采用 MIT 许可证，拥有活跃的社区，接受捐赠，并提供详细的文档和示例。

---

### [ArtPlayer.js - 现代 HTML5 视频播放器](https://artplayer.org/)

**原文标题**: [ArtPlayer.js - Modern HTML5 Video Player](https://artplayer.org/)

概述：本文介绍了文件上传功能的基本概念、常见用途及实现方式，强调其在数据交换和存储中的重要性。

- 📁 文件上传允许用户将本地文件传输到服务器或云端存储
- 🔒 安全性是关键考虑因素，需防范恶意文件与数据泄露
- 🌐 广泛应用于网站表单、云存储和内容管理系统
- ⚙️ 实现方式包括 HTML 表单、JavaScript 接口及后端处理逻辑
- 📏 通常涉及文件大小限制、类型验证和上传进度显示

---

### [星风界面](https://starwind.dev/)

**原文标题**: [Starwind UI](https://starwind.dev/)

Starwind UI 是一个专为 Astro 框架设计的动画组件库，提供超过 45 个可定制且易于访问的组件，帮助开发者快速构建美观的网站。

- 🚀 通过 CLI 快速安装，使用 `npx starwind@latest init` 即可开始
- 🎨 基于 Tailwind CSS 样式，组件完全可自定义
- ♿ 注重可访问性，支持键盘导航
- 📦 开源且采用 MIT 许可证，代码完全开放
- ⚡ 专为 Astro 优化，使用原生 JavaScript 实现

---

### [GitHub - starwind-ui/starwind-ui：适用于Astro的shadcn/ui。45+个动画且可访问的组件。通过CLI安装。拥有代码所有权。· GitHub](https://github.com/starwind-ui/starwind-ui)

**原文标题**: [GitHub - starwind-ui/starwind-ui: shadcn/ui for Astro. 45+ animated and accessible components. Install via CLI. Own the code. · GitHub](https://github.com/starwind-ui/starwind-ui)

Starwind UI 是一个基于 Astro 和原生 JavaScript 构建的动画组件库，包含 45 个以上设计精美、开箱即带动画且具备可访问性的组件。它采用类似 shadcn/ui 的理念，允许开发者将组件直接添加到自己的代码库中，从而获得完全的所有权和控制权。

- 🎯 **代码所有权** - 组件直接存在于项目中，而非 `node_modules` 目录内，支持完全自定义。
- ✨ **默认带动画** - 基于 Tailwind CSS v4 提供流畅、精美的开箱即用动画效果。
- ♿ **可访问性** - 支持键盘导航和屏幕阅读器，在设计时充分考虑了无障碍需求。
- 🚀 **零运行时依赖** - 纯 Astro 和原生 JavaScript 实现，无重型框架拖慢速度。
- 🛠️ **CLI 工具驱动** - 可通过简单的 `npx starwind add` 命令按需添加组件。
- 📦 **快速开始** - 使用 `npx starwind@latest init` 初始化项目，并通过 CLI 添加组件。
- 🤖 **AI 集成支持** - 提供 `llms.txt`、`llms-full.txt` 等资源及 MCP 服务器，便于 AI 工具集成。
- 📄 **开源与贡献** - 项目采用 MIT 许可证，并提供了详细的贡献指南，欢迎社区参与。

---

### [主题设计师 | Starwind Pro](https://pro.starwind.dev/tools/theme-designer/)

**原文标题**: [Theme Designer | Starwind Pro](https://pro.starwind.dev/tools/theme-designer/)

这是一个主题设计工具的界面，主要用于自定义网站或应用的主题样式，包含颜色、字体、圆角等视觉变量的设置，并支持亮色与深色两种模式。

- 🖥️ **设备要求**：主题设计器需要桌面端或平板设备的大屏幕才能正常使用。
- 🎨 **颜色定制**：提供亮色与深色两套模式，可分别设置主色、背景色、卡片色、边框色及成功/警告/错误等状态色。
- 🔤 **字体设置**：可分别选择标题字体、正文字体和等宽字体，支持从字体库安装。
- 📐 **样式变量**：可调整边框圆角半径和间距比例，支持强制直角选项。
- 👁️ **实时预览**：设计器提供组件、定价、登录等页面的实时预览，方便查看效果。
- 💾 **主题管理**：支持保存自定义主题到本地存储、导出生成的 CSS 代码，并内置多种预设主题。
- 🧩 **组件展示**：预览区域展示了按钮、徽章、表单、提示框、表格等多种 UI 组件的样式。

---

### [颜色 API](https://www.thecolorapi.com/)

**原文标题**: [The Color API](https://www.thecolorapi.com/)

Color API 是一款快速、现代的在线工具，用于颜色转换、命名、配色方案生成及占位图获取。用户只需通过两个端点 `/id` 和 `/scheme` 即可完成所有操作，支持 JSON、HTML 和 SVG 格式输出。

- 🎨 通过 `/id` 端点可转换和识别颜色，支持 HEX、RGB、CMYK、HSL 和 HSV 格式输入，返回颜色名称、转换值及对比色建议
- 🌈 使用 `/scheme` 端点可生成多种配色方案，包括单色、类比、互补、三元等模式，并可自定义方案长度
- 📄 所有端点均提供 JSON、HTML 和 SVG 格式输出，SVG 格式便于嵌入和分享
- 🔧 该工具为开源项目，开发者鼓励用户在使用过程中提供支持与反馈

---

### [中风 - 动画 SVG](https://stroke.abhii.space/)

**原文标题**: [Stroke - Animate SVGs](https://stroke.abhii.space/)

Stroke 是一个用于为 SVG 图形（如标志、签名和插图）创建精美手绘动画的库，特别适用于 React 和 Next.js 项目。

- 🎨 在画布中绘制 SVG 图形
- 📋 复制生成的代码
- ⚛️ 粘贴到 React 或 Next.js 组件中
- 📦 安装 motion 库
- 🔧 使用 className 属性调整大小
- 🎨 使用 color 属性更改颜色
- 💛 示例：<Stroke className="w-100 h-auto" color="yellow"/>

---

### [我的ΔE(OK) JND 是多少？](https://www.keithcirkel.co.uk/whats-my-jnd/)

**原文标题**: [What's My ΔE(OK) JND?](https://www.keithcirkel.co.uk/whats-my-jnd/)

这是一个测试用户色彩辨别能力的在线游戏，通过逐步缩小两种颜色的差异来测量用户的“最小可觉差”。

- 👁️ 用户通过点击两种颜色之间的分界线来辨别差异
- 🎮 游戏难度逐渐增加，颜色差异越来越小
- 📊 大约需要 40 轮测试来确定个人的最小可觉差
- 🏆 大多数人的得分在 0.02 左右
- 🔗 提供“困难模式”选项和结果分享功能
- 📱 包含屏幕清洁剂推广链接和博客文章指引

---

### [色彩过载 - 基思·瑟克尔](https://www.keithcirkel.co.uk/too-much-color/)

**原文标题**: [Too Much Color - Keith Cirkel](https://www.keithcirkel.co.uk/too-much-color/)

本文探讨了在 CSS 颜色表示中，多少小数位数是足够的。作者通过分析不同颜色空间（如 oklch、oklab、lab、lch 等）的感知差异（dE）和“刚好可察觉差异”（JND），得出结论：对于 0-1 范围的颜色通道（如 oklch 的 L 和 C），3 位小数是安全且足够的；对于较大范围（如 lab 的 L 为 0-100），1 位小数即可。这适用于静态颜色和颜色计算（如混合、链式操作），以确保误差不会累积到可察觉的程度。同时，作者指出浏览器内部通常使用 32 位浮点数存储颜色，但多余的精度并无实际意义，而压缩工具可以采用这些规则来优化 CSS 文件大小。

- 🎨 对于 oklch 和 oklab 颜色空间，L（亮度）和 C（色度）通道只需 3 位小数（如.oklch(.659 .304 234.752)），即可保证人眼无法察觉差异，并为颜色计算提供安全余量。
- 🔢 对于 lab 和 lch 颜色空间，由于通道范围较大（如 L 为 0-100），1 位小数就足够，整数位已是感知极限，但多加 1 位可避免链式计算中的误差累积。
- 🌈 色相（hue）通道在 oklch 中范围为 0-360，即使整数位也低于可察觉差异，但建议使用 1 位小数以防止多次计算时的误差积累。
- 🖥️ sRGB 表示法（如 rgb、hsl）中，通道通常为整数或百分比，多余的小数位会被浏览器量化为 8 位值，因此 1 位小数或整数即可满足需求。
- 🔄 在颜色空间转换或链式操作（如 color-mix）中，3 位小数规则能有效抑制误差放大，确保多次转换后颜色仍保持视觉一致。
- 📉 测试显示，2 位小数虽在静态颜色中接近感知极限，但在颜色计算中可能导致误差累积超过可察觉差异，因此不推荐。
- 🧪 作者通过交互式工具和大量测试验证了这些规则，并计划将其应用于 CSS 压缩工具 csskit 中，以优化颜色值的精简处理。

---

### [非 HTML 内容](https://frontendfoc.us/open/733/*%7CUID%7C*?ipx=t)

**原文标题**: [Non-HTML content](https://frontendfoc.us/open/733/*%7CUID%7C*?ipx=t)

无法总结：非 HTML 内容。

---

