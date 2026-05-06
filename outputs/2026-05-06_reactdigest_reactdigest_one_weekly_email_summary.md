### [React 文摘：电子邮件通讯](https://reactdigest.net/)

**原文标题**: [React Digest: Email Newsletter](https://reactdigest.net/)

这是一份为React开发者精心策划的每周通讯，帮助您节省时间、学习新知。

- 📬 每周一封邮件，服务超过22,601名前端软件工程师
- 📝 精选文章并附简短摘要，节省寻找优质内容的时间
- 🧠 每周都能学到新东西
- 💬 读者反馈积极，称赞文章实用且紧跟React发展（如并发模式）
- 🏢 读者来自各大前端工程团队
- 📅 涵盖2013-2026年间的持续内容更新

---

### [在她生命的早期。而且他们都不是六岁。我已经。](https://www.readwriterachel.com/things-i-learned/2026/04/23/back-to-basics-react-variables.html)

**原文标题**: [Early in her life. And all of them isnât six years old. Iâve.](https://www.readwriterachel.com/things-i-learned/2026/04/23/back-to-basics-react-variables.html)

概述总结
- 🌍 她早年生活，但并非六岁，她站在那里注视着“美丽新世界”。
- 🎭 应当能够有意识地欺骗，同时保持坚定的目标，沿着通道前行。
- ⏳ 伯纳德匆忙赶到，立体金发女郎和“更多针脚”出现，男子说“别和约翰一起”，让他受苦。
- 🤔 男子提到“有趣你提到他们”，同样的事情出现，他确实如此。
- 📚 参见：所有情况中偶然发生的分裂。

---

### [AI可观测性](https://www.telerik.com/webinars/progress-telerik/ai-observability?utm_medium=cpm&utm_source=reactdigest&utm_campaign=dt_ai_observability_webinar)

**原文标题**: [
	AI Observability
](https://www.telerik.com/webinars/progress-telerik/ai-observability?utm_medium=cpm&utm_source=reactdigest&utm_campaign=dt_ai_observability_webinar)

本网络研讨会探讨了AI系统在生产环境中面临的独特可观测性挑战，并提供了工程化的解决方案。

- 🤖 **AI系统需要新的可观测性模型**：传统APM工具无法解释AI行为，即使系统运行正常，AI也可能产生错误答案、调用错误工具或推高成本。
- ⚠️ **传统监控的盲区**：团队面临更长的调试周期、对提示词和检索过程缺乏可见性、生产事故难以定位根因，以及代理工作流日益复杂带来的成本风险。
- 🔍 **关键议题涵盖**：系统输出与AI行为测量的区别、多步骤代理工作流中的常见故障场景、从提示词到令牌使用量的重要生产信号，以及现代AI可观测性如何帮助快速追踪和修复问题。
- 🎤 **主讲嘉宾**：Ed Charbeneau（Principal Developer Advocate，微软MVP）和Lyubomir Atanasov（产品经理，专注于代理可观测性），将分享工程优先的AI可观测性方法。

---

### [获取失败](https://www.rubrik.com/blog/architecture/26/2/async-react-building-non-blocking-uis-with-usetransition-and-useactionstate)

**原文标题**: [Failed to retrieve](https://www.rubrik.com/blog/architecture/26/2/async-react-building-non-blocking-uis-with-usetransition-and-useactionstate)

无法总结：获取内容失败，状态码 403。

---

### [React Flow 在生产中真正重要的技巧 | 作者：Roman Fedytskyi | 2026年4月 | Medium](https://medium.com/@roman_fedyskyi/react-flow-tips-that-actually-matter-in-production-db7c093932f6)

**原文标题**: [React Flow Tips That Actually Matter in Production | by Roman Fedytskyi | Apr, 2026 | Medium](https://medium.com/@roman_fedyskyi/react-flow-tips-that-actually-matter-in-production-db7c093932f6)

### 概述摘要  
本文分享了在实际生产环境中使用React Flow构建图表工具的关键技巧，强调从系统层面而非UI层面思考，以应对性能、状态管理和扩展性挑战。

- 🧠 **将图表视为状态而非UI**：使用受控状态管理节点和边，并引入存储层以简化日志、验证和持久化。
- 🧩 **保持节点简单**：节点仅渲染数据，不管理行为或业务逻辑，避免系统碎片化。
- 📋 **将编辑功能移出节点**：使用侧边栏编辑模式，集中管理更新逻辑，保持图表清晰。
- 🔗 **提前验证连接**：通过`isValidConnection`函数限制连接规则，防止无效状态。
- ⚡ **性能依赖结构**：使用`React.memo`优化，但核心是控制更新传播范围，避免全局重绘。
- 📸 **导出需要管道处理**：通过`html-to-image`和视口计算生成干净输出，避免UI伪影。
- 💾 **尽早实现持久化**：即使使用localStorage，也能强制状态整洁，改善架构。
- 📊 **记录交互日志**：通过`track`函数记录用户操作，便于调试和系统增长。
- 🗂️ **早期组织应用结构**：按功能划分目录（如nodes、store、export），保持可维护性。
- 🏗️ **总结**：将React Flow视为基础设施而非简单UI组件，早期做出正确决策，确保系统可预测、可扩展。

---

### [构建你自己的永不失同步的闪烁骨架 — Neciu Dan](https://neciudan.dev/lets-build-dynamic-shimmer-skeletons)

**原文标题**: [Build your own shimmer skeleton that never goes out of sync — Neciu Dan](https://neciudan.dev/lets-build-dynamic-shimmer-skeletons)

以下是您提供内容的摘要：

本文章介绍了一种构建永不与UI不同步的骨架屏（shimmer skeleton）的方法，通过直接测量真实组件的DOM结构来自动生成占位符，从而避免手动维护骨架组件。

- 📦 **核心问题**：传统骨架屏需要为每个UI组件单独创建并手动同步骨架组件，一旦布局变更，骨架屏极易过时，形成维护陷阱。
- 🛠️ **现有库的局限**：`react-loading-skeleton` 和 `react-content-loader` 简化了动画，但仍需硬编码尺寸和形状，无法自动与真实组件同步。
- 💡 **创新思路**：直接渲染真实组件（使用假数据），隐藏文字（`color: transparent`），然后测量其DOM元素位置，并在其上覆盖动态闪烁块。组件本身就是骨架屏。
- 📏 **DOM测量方法**：使用 `getBoundingClientRect()` 获取图片、标题、段落等“叶子元素”的精确位置和尺寸，并利用 `getComputedStyle()` 获取其 `border-radius`，使闪烁块形状（如圆形头像）与真实元素匹配。
- ✨ **闪烁动画实现**：通过CSS `linear-gradient` 和 `@keyframes` 动画，在测量出的矩形块上实现从左到右的扫光效果，模拟加载状态。
- 🔗 **React集成**：通过 `useLayoutEffect` 在浏览器绘制前完成测量，避免闪烁。使用 `React.Children.only` 和 `React.cloneElement` 注入假数据（`templateProps`），实现加载与就绪状态的无缝切换。
- ⚠️ **边缘情况处理**：需处理块级元素全宽拉伸、隐藏元素（`display: none`）、无尺寸图片、SVG元素及窗口缩放等问题，以确保测量准确。
- 📝 **假数据设计**：假数据无需完全真实，但应模拟真实数据的长度和数量（如列表项数），以生成大小合适的占位符。
- ⚖️ **权衡与性能**：运行时测量有轻微性能开销，但通常极低（12个组件<2ms）。组件需能使用假数据渲染，且避免在测量阶段执行副作用（如API调用）。

---

### [React 如何无序流式输出 UI 却依然保持顺序 | React 内部探秘](https://inside-react.vercel.app/blog/how-react-streams-ui-out-of-order)

**原文标题**: [How React streams UI out of order and still manages to keep order | Inside React](https://inside-react.vercel.app/blog/how-react-streams-ui-out-of-order)

### 概述总结
React通过Suspense边界实现无序流式传输，先发送就绪内容并预留占位符，待数据就绪后通过JavaScript将组件替换到正确位置，从而避免传统流式传输的顺序阻塞问题。

- 🚀 **核心机制**：React利用`<template>`标签作为占位符，将未就绪的组件包裹在Suspense边界内，先发送已就绪的UI（如导航栏和页脚），待数据加载完成后通过`$RC`函数进行DOM替换。
- 🔄 **生命周期**：Suspense边界经历三个状态：`$?`（待定，显示fallback）、`$~`（排队，内容就绪等待替换）、`$`（完成，内容已插入DOM）。
- 🛠️ **实现细节**：服务器将就绪组件渲染为隐藏的`<div>`（如`id="S:0"`），随后发送`<script>`标签调用`$RC("B:0", "S:0")`，该函数通过`$RB`队列和`$RV`函数在下一帧执行DOM替换，清除fallback并插入真实内容。
- ⚠️ **潜在风险**：由于React仅通过`document.getElementById`查找模板占位符，若开发者手动插入相同ID的`<template>`，可能导致错误的DOM替换，破坏Suspense的正常工作。
- 💡 **与传统流式传输的区别**：常规HTML流式传输需按顺序发送块，而React通过将DOM作为暂存区，利用JavaScript实现无序组件插入，提升页面首屏加载体验。

---

### [提示 API | Chrome 上的 AI | Chrome 开发者](https://developer.chrome.com/docs/ai/prompt-api)

**原文标题**: [The Prompt API  |  AI on Chrome  |  Chrome for Developers](https://developer.chrome.com/docs/ai/prompt-api)

Prompt API 允许在浏览器中使用 Gemini Nano 模型处理自然语言请求，支持文本、图像和音频输入，并可用于构建搜索、新闻摘要、内容过滤等功能。

- 💡 **核心功能**：通过自然语言与 Gemini Nano 模型交互，支持文本、图像、音频多模态输入，可构建 AI 搜索、个性化新闻、内容过滤、日历事件创建等应用。
- 🖥️ **硬件要求**：需 Windows 10/11、macOS 13+、Linux 或 Chromebook Plus 设备，至少 22GB 存储空间，GPU 需 4GB+ VRAM，CPU 需 16GB+ RAM 和 4 核+，网络需无限流量。
- 🚀 **使用步骤**：先调用 `LanguageModel.availability()` 检查模型可用性，再用 `create()` 创建会话，最后通过 `prompt()` 或 `promptStreaming()` 发送请求。
- ⚙️ **参数定制**：支持设置 `topK` 和 `temperature` 控制输出多样性，可通过 `initialPrompts` 添加上下文，用 `responseConstraint` 约束输出格式（如 JSON Schema）。
- 🔄 **会话管理**：每个会话有上下文窗口，可监控 `contextUsage`，支持克隆、终止会话，以及通过 `append()` 添加后续提示。
- 🌐 **多模态支持**：输入支持音频（AudioBuffer、Blob 等）和视觉元素（图片、Canvas、视频帧），输出仅限文本，需在创建会话时声明 `expectedInputs` 和 `expectedOutputs`。
- 🔒 **权限与安全**：默认仅顶层窗口和同源 iframe 可用，跨域 iframe 需设置 `allow="language-model"`，不支持 Web Workers。
- 📊 **性能优化**：建议复用会话避免重复创建，使用流式输出处理长响应，监听 `contextoverflow` 事件管理上下文溢出。
- 🧪 **实验与反馈**：Chrome 138+ 支持，需启用相关 flag，可通过 GitHub 提交 bug、功能请求或参与早期预览计划。

---

### [响应式图片的终结 - Piccalilli](https://piccalil.li/blog/the-end-of-responsive-images/)

**原文标题**: [
  The end of responsive images - Piccalilli
](https://piccalil.li/blog/the-end-of-responsive-images/)

概述总结  
- 🎯 作者Mat Marquis在14年后终于可以揭示：他作为RICG主席主导了响应式图片标记（srcset/sizes）的标准化，尽管他自己也讨厌sizes的复杂性。  
- 🔍 响应式图片解决了带宽浪费问题：过去固定大图会强制所有用户下载大文件，而srcset和sizes让浏览器根据上下文选择最佳尺寸。  
- 🚫 作者承认sizes是“最糟糕的部分”：它需要手动描述图片在不同断点下的尺寸，难以自动化，例如“(min-width: 1340px) 257px”这类复杂语法。  
- 💡 新解决方案是`sizes="auto"`：结合`loading="lazy"`，浏览器能在布局渲染后自动计算图片尺寸，无需手动指定sizes值。  
- ✅ 向后兼容：不支持auto的浏览器会忽略该值，继续使用后续sizes内容，因此可立即使用。  
- 📉 仅对首屏关键图片（如LCP元素）仍需手动sizes，其余图片均可使用`loading="lazy" sizes="auto"`简化工作。  
- 🏆 作者坚持：尽管sizes令人痛苦，但当时浏览器无法自动处理，这种“放弃控制”的设计是正确且必要的。

---

### [滚动驱动动画 • 乔什·W·科莫](https://www.joshwcomeau.com/animation/scroll-driven-animations/)

**原文标题**: [Scroll-Driven Animations • Josh W. Comeau](https://www.joshwcomeau.com/animation/scroll-driven-animations/)

以下是根据您提供的文本内容生成的摘要：

概述摘要  
- 📜 **核心概念**：将CSS关键帧动画映射到滚动距离，而非时间，通过`animation-timeline: view()`实现。  
- 🎯 **时序函数**：可应用自定义缓动曲线（如`cubic-bezier`或弹簧效果`linear()`）到滚动驱动动画。  
- 📏 **动画范围**：使用`animation-range`属性自定义动画开始/结束点，支持`cover`、`contain`、`entry`、`exit`等值。  
- 🎬 **进入与退出**：通过`entry`和`exit`范围实现元素进入/离开视口时的动画效果，可组合多个关键帧。  
- 🔢 **范围百分比**：通过`animation-range-start`和`animation-range-end`精确控制动画起止位置（如`cover 0%`到`cover 50%`）。  
- 📊 **滚动进度时间线**：使用`scroll()`跟踪整体滚动进度，适用于阅读进度条等场景。  
- 🔗 **链接时间线**：通过`view-timeline`和`timeline-scope`分离测量元素与动画元素，实现跨元素滚动驱动动画。  
- 🚀 **浏览器支持**：约85%的浏览器支持（除Firefox需启用标志），有polyfill但功能有限。  
- 💡 **扩展应用**：除滚动驱动外，还可结合`animation-trigger`实现滚动触发动画（目前仅Chrome/Edge支持）。

---

### [暗色模式的六个层级 - CSSence.com](https://cssence.com/2024/six-levels-of-dark-mode/)

**原文标题**: [Six levels of dark mode - CSSence.com](https://cssence.com/2024/six-levels-of-dark-mode/)

本文探讨了实现网站深色模式的六个层级，从基础到高级，涵盖HTML、CSS和JavaScript方法，并强调用户偏好与可访问性的重要性。

- 🌙 **第一层：基础** - 通过`<meta name="color-scheme" content="light dark">`标签让浏览器自动适配用户偏好，无需额外CSS。
- 🎨 **第二层：基本** - 使用CSS `color-scheme: light dark;`声明，结合系统颜色实现简单样式，但推荐优先用meta标签。
- ⚡ **第三层：温和** - 利用`light-dark()`函数直接定义颜色，如`background-color: light-dark(black, white);`，但浏览器支持有限。
- 🛠️ **第四层：大胆** - 通过`@media (prefers-color-scheme: dark)`媒体查询实现全面自定义，可调整颜色、滤镜或阴影。
- 📂 **第五层：二分** - 在HTML中用`<link media="...">`分别加载浅色/深色样式表，优化加载性能。
- 💻 **第六层：激进** - 结合JavaScript的`matchMedia`函数动态响应模式切换，实现交互式控制。
- 🚀 **第七层：超越** - 构建颜色方案切换器，提供“自动/浅色/深色”三种模式，而非仅依赖系统偏好。
- 🔍 **第八层：迷人** - 使用CSS `:has()`选择器直接查询`<meta>`标签内容，无需额外类名或属性，实现更优雅的切换。

---

### [错误](https://evilmartians.com/chronicles/how-to-make-your-website-visible-to-llms)

**原文标题**: [Error](https://evilmartians.com/chronicles/how-to-make-your-website-visible-to-llms)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='evilmartians.com', port=443): Max retries exceeded with url: /chronicles/how-to-make-your-website-visible-to-llms (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [错误](https://saschb2b.com/blog/react-compiler-year-in-review)

**原文标题**: [Error](https://saschb2b.com/blog/react-compiler-year-in-review)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='saschb2b.com', port=443): Max retries exceeded with url: /blog/react-compiler-year-in-review (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [错误](https://programmingdigest.net/?utm_source=web-archive&utm_campaign=react)

**原文标题**: [Error](https://programmingdigest.net/?utm_source=web-archive&utm_campaign=react)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='programmingdigest.net', port=443): Max retries exceeded with url: /?utm_source=web-archive&utm_campaign=react (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [错误](https://leadershipintech.com/?utm_source=web-archive&utm_campaign=react)

**原文标题**: [Error](https://leadershipintech.com/?utm_source=web-archive&utm_campaign=react)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='leadershipintech.com', port=443): Max retries exceeded with url: /?utm_source=web-archive&utm_campaign=react (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [错误](https://csharpdigest.net/?utm_source=web-archive&utm_campaign=react)

**原文标题**: [Error](https://csharpdigest.net/?utm_source=web-archive&utm_campaign=react)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='csharpdigest.net', port=443): Max retries exceeded with url: /?utm_source=web-archive&utm_campaign=react (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [错误](https://bonobopress.com)

**原文标题**: [Error](https://bonobopress.com)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='bonobopress.com', port=443): Max retries exceeded with url: / (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [错误](https://reactdigest.net/newsletters)

**原文标题**: [Error](https://reactdigest.net/newsletters)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='reactdigest.net', port=443): Max retries exceeded with url: /newsletters (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [错误](https://reactdigest.net/privacy)

**原文标题**: [Error](https://reactdigest.net/privacy)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='reactdigest.net', port=443): Max retries exceeded with url: /privacy (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [错误](https://bonobopress.com/media-kit)

**原文标题**: [Error](https://bonobopress.com/media-kit)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='bonobopress.com', port=443): Max retries exceeded with url: /media-kit (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

