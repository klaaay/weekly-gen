### [2026 年 HTML 现状](https://2026.stateofhtml.com/en-US)

**原文标题**: [State of HTML 2026](https://2026.stateofhtml.com/en-US)

本次页面介绍“State of HTML 2026”调查：调查期为 2026 年 10 月 1 日至 11 月 1 日，共有 2,091 名受访者，并提供问卷回顾、数据获取与下载入口。开篇强调浏览器原生能力与厂商协作正在加速发展，而 JavaScript 框架趋于稳定；在 AI 辅助编码普及的背景下，重新学习现代 Web API 正合时宜。

- 📅 调查时间：2026 年 10 月 1 日至 11 月 1 日，受访者 2,091 人。
- 🗂️ 页面提供调查归档、问卷回顾、获取数据和下载入口，并可见 State of HTML 2025 入口。
- 🌐 过去 Web API 能力有限，复杂布局依赖技巧，促使 JavaScript 框架、库和工具大量涌现。
- 🧩 如今 JS 框架围绕少数成熟方案整合，变化速度放缓；浏览器厂商合作更紧密，更快发布跨浏览器新功能。
- 🤖 AI 辅助代码生成逐渐普及，常直接调用浏览器 API、跳过 JS 框架，因此开发者需要重新打好 Web 基础。
- 🎯 本次调查旨在帮助开发者了解现代浏览器实际能力与前端趋势。
- 🤝 合作伙伴包括 Google Chrome 团队，以及招聘、无代码、认证与用户管理、前端课程、趋势学习、浏览器等支持方。
- 🙏 特别感谢 Lea Verou 负责问卷设计、Christopher Kirk-Nielsen 负责 Logo 设计；页面还提供邮箱订阅下次调查通知及多语言翻译贡献名单。

---

### [2026 年 HTML 现状：使用情况](https://2026.stateofhtml.com/en-US/usage/#ai_generated_code_balance)

**原文标题**: [State of HTML 2026: Usage](https://2026.stateofhtml.com/en-US/usage/#ai_generated_code_balance)

这份调查汇总了开发者在使用 HTML 和 Web 平台功能时遇到的主要障碍，重点涉及浏览器兼容性、表单控件样式、原生组件缺失、渐进增强、HTML/CSS 与 JavaScript 的投入比例，以及 AI 代码生成和浏览器 AI API 等方面。核心问题集中在浏览器支持差异、表单元素难以定制，以及缺少开发者期待的原生 UI 组件。

- 🌐 浏览器互操作：Customizable Select 已接近完成，但仅 Firefox 仍缺支持；Popover API 已在所有主流浏览器中支持，浏览器支持对采用它的阻碍应会下降。
- 🧩 功能受限：开发者因兼容性或缺少支持而无法使用 Customizable Select、popover 属性、Anchor Positioning、Temporal、File System Access API、dialog、Web Bluetooth、WebUSB、PWA、datalist 等功能。
- 📅 受限最严重：`<select>` 的受限评分较去年下降 10%，日期输入成为“功能限制影响最大”的功能。
- 🏗️ 缺失元素：开发者最希望新增原生 datatable、tabs、combobox/autocomplete、switch/toggle、富文本编辑器、可排序拖拽列表、下拉菜单、HTML include、骨架屏和右键菜单。
- 🎨 样式痛点：`<select>` 最难样式化，其次是日期输入、`<select multiple>`、checkbox、time 输入、验证错误、radio、range、`<details>/<summary>` 和颜色输入；表单元素仍是主要样式难题。
- ♿ 渐进增强：43% 的受访者不关心网站或应用在没有 JavaScript 时是否可用，只有 4% 将其视为必需；将渐进增强列为高优先级与采用更多无障碍技术相关。
- ⚖️ HTML/CSS 与 JS/TS 比例：开发者投入 HTML/CSS 的时间中位数为 63%；代码库仍包含大量 JavaScript/TypeScript，但浏览器原生能力可能接管部分 JS 工作。
- 🤖 AI 代码生成：受访者代码中 AI 生成比例的中位数为 50%；State of Devs 受访者为 63%，而 CSS 代码中 AI 生成比例仅为 13%。
- 🧠 浏览器 AI API：最希望原生支持翻译、语音识别、字幕生成、语言检测、摘要、计算机视觉等；也有不少人选择“不需要”浏览器 AI API。
- 📦 其他痛点：原生 HTML include 或模板缺失被再次提及；内容、浏览器厂商问题和生态问题也是相关痛点。

---

### [Popover API - Web API | MDN](https://developer.mozilla.org/en-US/docs/Web/API/Popover_API)

**原文标题**: [Popover API - Web APIs | MDN](https://developer.mozilla.org/en-US/docs/Web/API/Popover_API)

Popover API 提供了一种标准、一致且灵活的方式，用于在其他页面内容之上显示弹出内容；自 2025 年 1 月起，它进入 Baseline 2025 新可用状态，可通过 HTML 属性或 JavaScript 控制，适用于非模态浮层场景。

- 📅 自 2025 年 1 月起，该功能可在最新设备和浏览器版本中工作；旧设备或浏览器可能不支持，且部分功能支持程度可能不同。
- 🧩 Popover API 为开发者提供标准化、一致且灵活的机制，用于在其他页面内容之上显示弹出内容。
- 🪟 使用 Popover API 创建的弹出框始终是非模态的；如需模态弹出框，应使用 `<dialog>`，也可使用 `<dialog popover>` 组合弹出框控制与对话框语义。
- 💡 典型用例包括操作菜单、自定义“toast”通知、表单元素建议、内容选择器和教学 UI。
- 🖱️ 可通过 HTML 属性创建，例如用 `popovertarget` 按钮控制带 `popover` 的元素；也可通过 JavaScript 的 `togglePopover()` 切换显示与隐藏。
- 🔗 相关功能 interest invokers 可在悬停/聚焦时显示弹出框，无需 JavaScript。
- 🏷️ HTML 属性包括：`interestfor` 定义 interest invoker 的目标；`popover` 将元素变为弹出框并接受 `auto`、`hint`、`manual`；`popovertarget` 将按钮/输入框变为控制按钮；`popovertargetaction` 指定 `hide`、`show` 或 `toggle`。
- 🎨 CSS 特性包括：`::backdrop` 在弹出框后方添加全屏背景效果；`interest-delay` 系列控制兴趣延迟；`:interest-source` 和 `:interest-target` 在表示兴趣时设置样式；`:popover-open` 匹配正在显示的弹出框。
- 🧱 接口包括 `InterestEvent`（用于 `interest` 和 `loseinterest` 事件，含 `source` 属性）与 `ToggleEvent`（用于 `beforetoggle` 和 `toggle` 事件）。
- ⚙️ 方法包括：`hidePopover()` 从顶层移除并设置 `display: none`；`showPopover()` 添加到顶层；`togglePopover()` 在显示与隐藏间切换。
- 🔍 属性包括：`interestForElement`、`HTMLElement.popover`、`popoverTargetElement`、`popoverTargetAction`，可用于获取/设置状态、目标与控制动作，并支持特性检测。
- 🔔 事件包括：`beforetoggle` 在状态变化前触发，可阻止打开或更新其他元素；`toggle` 在状态变化后触发；`interest` 和 `loseinterest` 在目标元素上表示兴趣显示或失去时触发。
- 📚 文档还包含示例、规范、浏览器兼容性及参见项，如 `popover`、`popovertarget`、`popovertargetaction`、`::backdrop`、`:popover-open`。

---

### [2026 年 HTML 现状：使用情况](https://2026.stateofhtml.com/en-US/usage/)

**原文标题**: [State of HTML 2026: Usage](https://2026.stateofhtml.com/en-US/usage/)

这份调查围绕开发者如何使用 HTML 及 Web 平台功能，梳理了浏览器互操作性、功能限制、缺失元素、样式定制、渐进增强、HTML/CSS 与 JS/TS 时间分配、AI 代码生成和浏览器 AI API 等痛点。整体看，表单控件与浏览器支持差异仍是主要困扰，原生数据表格/标签页等元素呼声高，AI 生成代码已占一定比例，但 CSS 与浏览器原生 AI 能力的使用仍有限。

- 🌐 浏览器互操作性：Customizable Select 接近完成，但 Firefox 仍不支持；Popover API 已在所有主流浏览器支持，因浏览器支持不足而受阻的开发者减少。
- 🧩 互操作性痛点排名：Customizable Select（59 票，+0.39）居首，其后是 `popover` 属性（39，+0.18）、Anchor Positioning（21）、Temporal（18）、File System Access API（14）等。
- ⚠️ 功能受限：`<input type="date">` 以 21 票成为限制影响最大的功能；`<select>` 为 15 票，且因样式定制进展得分较去年下降 10%。
- 🧱 缺失元素：开发者最希望新增原生 Datatable（538 票）、Tabs（476）、Combobox/autocomplete（462）、Switch/toggle（397）、富文本编辑器（380）等。
- 🎨 样式问题：`<select>`（573 票）最难样式化，其次是 `<input type="date">`（456）、`<select multiple>`（299）、checkbox（277）；表单元素仍是主要痛点。
- ♿ 渐进增强：43% 受访者不关心站点在无 JavaScript 下运行，仅 4% 将其列为必需；重视渐进增强与更多无障碍技术使用相关。
- ⏱️ HTML/CSS 与 JS/TS 平衡：HTML/CSS 与 JavaScript/TypeScript 投入时间中位数约 63%，代码库仍含大量 JS/TS，但浏览器原生能力可能改变分工。
- 🤖 AI 代码生成：受访者代码中 AI 生成比例中位数为 50%；State of Devs 受访者为 63%，但 CSS 代码中 AI 生成比例仅 13%。
- 🗣️ 浏览器 AI API：最希望原生支持翻译（697 票），其次语音识别（398）；也有 325 人选择“无”。
- 🧷 其他痛点：原生 HTML include 或模板能力缺失被多次提及；内容、浏览器厂商问题和生态问题也是其他痛点来源。

---

### [HTML 2026 现状：表单](https://2026.stateofhtml.com/en-US/features/forms/)

**原文标题**: [State of HTML 2026: Forms](https://2026.stateofhtml.com/en-US/features/forms/)

overview summary
本文汇总了表单相关元素与属性的使用情况、开发者情绪与痛点：`<datalist>` 使用率上升但正面情绪下降，表单样式与自定义仍是最大痛点，输入元素、浏览器兼容、表单验证与无障碍问题也较突出。

- 📈 `<datalist>` 使用率同比增长，从 30% 升至 44%，但正面情绪从 44% 降至 34%，整体排名从第 1 降到第 18。
- 🧩 受访者提到 `<datalist>` 的样式定制、无障碍和浏览器 bug 等问题，说明功能发布后的后续支持未完全达到开发者预期；使用越多，批评也可能越多。
- 🎨 表单元素使用情况：`<input type="color">` 已用 48.9%、听过 39.5%、未听过 10.7%；`<datalist>` 分别为 44.1%、32.8%、21.7%；`input.showPicker()` 为 19.1%、30.3%、50.1%；Customizable Select 为 19%、47.8%、32.5%。
- 📊 体验与情绪基准：平均“用过”为 33%，平均“正面”为 32%，平均“负面”为 4%。
- 🛠️ 表单痛点中，样式与自定义仍是首要问题（158 条回答），其次是输入元素问题（127 条）、浏览器厂商问题（86 条）、表单验证（83 条）和无障碍（20 条）。
- ♿ 其他痛点包括终端用户体验、开发者体验、认知负担、编辑 API、对 JavaScript/框架的依赖、表单处理、Web Components、标签问题等。
- 📚 推荐资源：Kevin Powell 的“CSS-only Form Validation Hints”，介绍用 CSS 为用户提供上下文提示，并根据字段有效/无效状态手工创建和动画化 SVG（合作伙伴赞助内容）。

---

### [HTML 2026 现状：结论](https://2026.stateofhtml.com/en-US/conclusion/)

**原文标题**: [State of HTML 2026: Conclusion](https://2026.stateofhtml.com/en-US/conclusion/)

overview summary：本文回顾 Web 基础层（HTML 与浏览器能力）的年度变化，指出声明式 HTML 和元素相关 API 正快速改善开发体验，但仍存在表单控件、浏览器差异及移动 OS 影响等痛点；无障碍备受关注，未来重点包括可定制表单控件、HTML includes 与 OpenUI 标准化。

- 🌐 浏览器正在试验无需 JavaScript 的权限授予元素，可定制 select 接近全浏览器支持，并出现 color、switch、showPicker()、rangegroup 等新表单能力。
- ✨ `<dialog>`、`<details>` 和 `popover` 已让开发更轻松；声明式 API 因代码更少、处理更多而受欢迎，HTML/元素相关 API 获得最多喜爱。
- 🧩 Web 基础层也包括非用户面向功能，如 speculation rules、声明式 WebMCP、`loading` 和 `fetchpriority`，可帮助浏览器优化数据加载与交互。
- ⚠️ 部分功能采用有限：`datalist` 不可靠，WebUSB、SpeechRecognition 用例受限，`<model>` 仅用于展示静态 3D 模型。
- 📱 浏览器差异仍是长期痛点，但问题已从“行为不同”转向“尚未跟上”；移动 OS 及其 UI 选择对 Web 的影响是今年主要痛点。
- ♿ 无障碍是调查受访者的首要关注之一；好 HTML 与无障碍相互交织，浏览器应帮助开发者判断是否对所有用户都正确。
- 🔮 未来愿望包括在可定制 select 落地后定制所有表单控件（先从 `datalist` 开始）、HTML includes，以及 OpenUI 推进 tabs、focusgroup 等标准化。
- 🧱 平台虽无巨大飞跃，但方向正确；`dialog` 和 `popover` 的广泛支持消除了主要痛点，HTML 作为基础层缓慢而审慎地演进并非坏事。

---

### [调查与表单管理软件 - SurveyJS](https://surveyjs.io/?utm_source=frontend&utm_medium=email)

**原文标题**: [Survey and Form Management Software - SurveyJS](https://surveyjs.io/?utm_source=frontend&utm_medium=email)

SurveyJS 是一套用于在 Web 应用中构建、管理和分析调查与表单的开源 JavaScript UI 组件库，强调前端灵活集成、数据自主、自托管和避免 SaaS 锁定，帮助团队减少数月定制开发。

- 🧩 **Form Library**：MIT 许可的动态表单渲染组件，可解析 SurveyJS JSON 并立即生成交互式表单，收集响应后发送到自有数据库。
- 🛠️ **Survey Creator**：白标拖拽式表单构建器，自动生成描述结构、布局、样式和行为的 JSON Schema，非技术用户也能可视化创建和编辑表单。
- 📊 **Dashboard**：读取 SurveyJS JSON Schema，识别数据类型并用交互式图表、表格展示调查结果，支持实时数据分析。
- 📄 **PDF Generator**：根据表单 JSON Schema 将 Web 表单渲染为可编辑 PDF，也可用已收集响应生成预填 PDF。
- 🔓 **开源与数据自主**：所有库开源，支持 React、Angular、Vue 3 和 Vanilla JS，可集成、扩展和修改，调查数据可完全自托管。
- ♾️ **无使用限制**：不限制管理员、受访者、表单数量、提交量、文件上传或功能使用，数据存储在自有数据库。
- ♿ **无障碍支持**：Form Library 和 Survey Creator 符合 WCAG、Section 508 和 ARIA 标准，支持键盘导航和屏幕阅读器。
- 📴 **离线收集**：调查、主题和响应可本地存储，离线创建和收集数据，恢复联网后自动同步。
- 🎨 **白标与主题适配**：共享设计令牌和可复用主题，支持 Bootstrap、Material UI、shadcn/ui 等主题适配，便于匹配现有设计系统。
- 🤖 **AI 辅助**：可通过 API 集成 AI，实现自然语言生成表单、翻译和智能内容建议。
- 💳 **许可模式**：Survey Creator、PDF Generator 和 Dashboard 采用一次性开发者许可，含 12 个月免费维护和该期间版本永久使用权；后续维护通过续订扩展。
- 🏢 **行业应用**：适用于保险、医疗、市场研究、教育、人力资源、电商、客户体验、非营利和银行等场景，支持敏感数据安全采集与合规管理。
- 🔐 **企业安全与合规**：自托管可让组织完全控制数据流、存储、隐私和合规，避免第三方 SaaS 依赖，应对 HIPAA、FERPA、GDPR 等要求。
- ⚙️ **仅负责前端**：SurveyJS 不存储、访问或跟踪数据，也不提供后端；用户可连接任意服务器、数据库和用户管理系统，自行实现审批流和认证等后端逻辑。

---

### [AI 在 Web 开发中常犯的 10 大错误 | 博客 | Chrome for Developers](https://developer.chrome.com/blog/top-10-things-ai-gets-wrong-in-web-dev?hl=en)

**原文标题**: [Top 10 things AI gets wrong in web development  |  Blog  |  Chrome for Developers](https://developer.chrome.com/blog/top-10-things-ai-gets-wrong-in-web-dev?hl=en)

Modern Web Guidance 1.0 已稳定发布，旨在把 Web 平台专业知识、最佳实践和浏览器兼容性数据直接嵌入 AI 编码代理。官方评测显示，未使用该工具的编码代理平均仅通过约 50% 的检查，而使用后可达约 90%；文章据此总结了 AI 在 Web 开发中最常出错的 10 个领域。

- 🚀 **发布目标**：帮助使用 AI 编码代理的开发者充分利用现代 Web 平台能力，提升用户体验。
- 📊 **评测结果**：引导代理通过率约 90%，未引导代理约 50%，说明即使最新前沿模型也不能可靠遵循现代 Web 最佳实践。
- ♿ **无障碍：焦点与 inert 管理**：常见错误包括未把焦点移入新视图或返回时未恢复、用 JS 手写焦点陷阱而非使用 `<dialog>`/`inert`、工具栏每个项都成为 Tab 停靠点、`:focus-visible` 轮廓对比度不足。
- 🌀 **无障碍：减少动态效果**：常忽略 `prefers-reduced-motion`，如全局无条件平滑滚动、滚动驱动动画无检查、错误移除过渡属性、用 `0.01ms` 重置所有过渡、未对视图过渡做条件控制。
- 📝 **无障碍：表单校验与自动填充**：常见问题包括用 JS 重新实现 `:user-invalid`、`aria-invalid` 与可见错误不同步、依赖占位符提示格式、提示放在输入框下方易被键盘遮挡、自动填充仅用边框颜色提示。
- 👆 **用户体验：滑动与触摸手势**：AI 常手写触摸逻辑而非使用 CSS Scroll Snap、遗漏 `overscroll-behavior-x:none`、在主线程驱动滑动进度、未支持键盘焦点。
- 🪟 **用户体验：对话框、弹出层与顶层过渡**：应优先使用原生 `popover`、`<dialog>`、`@starting-style`、`transition-behavior`，避免手写点击外部关闭、滚动锁定和返回键监听。
- 🌓 **用户体验：深色模式与主题自适应控件**：常漏掉 `<meta name="color-scheme">`、未设置 `color-scheme`、未使用 `light-dark()`、只提供二元切换且无法恢复系统默认、未监听 `storage` 事件同步多标签页。
- ⚡ **性能：运行时响应与流畅度**：应使用 `scheduler.postTask()`/`scheduler.yield()`、`content-visibility`、`contain-intrinsic-size`、`contentvisibilityautostatechange` 和 CSS 滚动状态查询，避免自定义 `setTimeout()` 队列、`display:none` 隐藏 SPA 视图等。
- 📐 **性能：布局偏移与视觉闪烁**：需为 `<video>` 设置宽高或 `aspect-ratio`，用 `font-size-adjust` 减少字体切换回流，使用 `dvh`/`svh`，用 `blocking="render"`、`rel="expect"` 控制渲染，避免旧式反闪烁片段。
- 🔒 **安全：DOM XSS 与 HTML 净化**：应优先使用原生 `setHTML()`，不可用时懒加载 DOMPurify；避免手写白名单净化器、宽松 Trusted Types 策略、静态页面 CSP 配置不当，并正确使用哈希、nonce、`strict-dynamic`、`report-sample`。
- 🔑 **安全：Passkey 登录与凭证生命周期**：应使用 `parseCreationOptionsFromJSON()`、`parseRequestOptionsFromJSON()`、`credential.toJSON()`，处理 `signalUnknownCredential()`、`getClientCapabilities()`、`AbortController`，并用 `uiMode:"immediate"` 替代过时的 `mediation:"immediate"`。
- 🛠️ **开始使用**：运行 `npx modern-web-guidance@latest install`，或通过代理插件市场安装；也可在 GitHub 仓库提交 issue 或参与贡献以补齐更多缺口。

---

### [现代 Web 指南 1.0：你的编码代理所缺失的 Web 平台专业知识 | 博客 | Chrome for Developers](https://developer.chrome.com/blog/modern-web-guidance-v1)

**原文标题**: [Modern Web Guidance 1.0: The web platform expertise your coding agent is missing  |  Blog  |  Chrome for Developers](https://developer.chrome.com/blog/modern-web-guidance-v1)

Modern Web Guidance 1.0 已正式稳定发布，旨在将经专家审核的 Web 开发最佳实践、浏览器兼容性数据和现代化工作流直接嵌入编码智能体，帮助其写出更快、更可访问、更安全的 Web 代码；该版本还获得 Firefox 与 Edge 支持，成为跨浏览器协作项目。

- 🚀 稳定版发布：Chrome for Developers 于 2026 年 11 月 10 日宣布 Modern Web Guidance 1.0 正式发布。
- 🧩 核心定位：把 Web 平台专业知识、最佳实践和 Baseline/浏览器兼容数据嵌入编码智能体。
- 🛠️ 现代化工作流：可扫描现有 HTML、CSS、JavaScript 和 `package.json`，发现可安全升级的机会并指导智能体修改。
- 📚 指南库扩展：覆盖数百个经验证的 AI 知识缺口，提供专家审核的跨浏览器解决方案。
- ♿ 专家审核加强：每条指南由领域技术负责人签核，用户侧指南还包含专门的无障碍审查与真实辅助技术测试。
- 📊 评估透明：所有指南均有完整评估覆盖，并提供公开评估仪表板展示可衡量改进。
- 🌐 跨浏览器协作：Firefox 和 Edge 加入 Chrome，共同支持项目、改善兼容性并贡献代码。
- 🎯 弥补模型短板：重点改善可访问性、用户体验、性能和安全，例如焦点管理、减少动态效果、表单验证、触摸手势、弹窗过渡、主题切换、主线程调度、布局偏移、HTML 净化、CSP 和通行密钥。
- ⚡ 推荐更优 Web 特性：优先推荐原生 HTML/CSS 能力而非自定义 JavaScript，并根据项目浏览器支持目标给出建议。
- 🔍 与 DevTools 配合：Modern Web Guidance 提供编码前知识，Chrome DevTools for agents 提供运行时验证、调试和优化能力。
- 🏆 落地成效：Pensionbazaar/Policybazaar 将交付周期缩短 90%+、UI Bug 降低 90%+，审计工作量减少 92%；WeTV 自动解决 90% 性能检查失败，调试时间减少 87%；note 通过率从 61% 提升至 94%，LCP 图片优先级正确率提升 28%；MetaMask 机器人 5 周内审查约 480 个 PR，推动修复 43 个问题，中位修复时间 15 分钟。
- 📦 安装方式：在项目目录运行 `npx modern-web-guidance@latest install`，已有版本可运行 `npx modern-web-guidance@latest update`，也可通过 Claude Code、Codex、Cursor、Copilot 等插件市场安装。
- 🤝 社区共建：由 Chrome 发起，联合浏览器伙伴、Web 标准与无障碍专家及开源贡献者共同完成。

---

### [推出跨源存储 API | 博客 | Chrome 开发者](https://developer.chrome.com/blog/introducing-cross-origin-storage)

**原文标题**: [Introducing the Cross-Origin Storage API  |  Blog  |  Chrome for Developers](https://developer.chrome.com/blog/introducing-cross-origin-storage)

本文介绍 Modern Web Guidance 已稳定，并重点说明 Chrome for Developers 提出的 Cross-Origin Storage API（COS）：它通过内容哈希让不同站点共享完全相同的资源，从而减少大型文件的重复下载与存储，同时涵盖典型用例、试验方式、生态支持、标准化进展以及安全隐私挑战。

- 🚀 Modern Web Guidance 已稳定，可用专家审核的 Web 开发最佳实践升级编码代理。
- 🧩 COS 是早期 WICG 提案，客户端按加密哈希定位内容，并从任意 URL 获取，在指定站点或所有站点间共享。
- 📦 针对相同资源被各站重复下载存储的问题，适用于 AI 模型、Wasm 模块、热门 JavaScript 库/框架、游戏引擎和大型 Web 字体等场景。
- 🔧 API 提供 `navigator.crossOriginStorage.getFileHandle()`；还计划集成到 HTML、CSS、JavaScript 和 `fetch()` 中。
- 🧪 可通过 Chrome Web Store、Firefox Add-ons、Safari App Store 的扩展 polyfill API，并在同一浏览器中测试流程。
- 🌱 生态已有实验性支持：Emscripten、Flutter、Transformers.js、WebLLM、wllama、Nuxt.js/Vite COS 插件、Prompt API Polyfill、Prebid.js 等。
- 🏛️ 标准化方面包括 W3C TAG 设计评审、HTML/CSS/Fetch 标准集成提案、Web Platform Tests 进行中，并已向 Mozilla 和 WebKit 征求标准立场。
- 🔐 共享精确已知资源带来安全收益，也存在安全挑战；文章提供安全与隐私问卷、explainer、规范草案、bug、演示和播客等反馈资源。

---

### [jQuery 4.1.0 和 3.8.0 发布：薪火相传 | jQuery 官方博客](https://blog.jquery.com/2026/11/17/jquery-4-1-0-and-3-8-0-released-passing-the-torch/)

**原文标题**: [jQuery 4.1.0 and 3.8.0 Released: Passing the Torch | Official jQuery Blog](https://blog.jquery.com/2026/11/17/jquery-4-1-0-and-3-8-0-released-passing-the-torch/)

jQuery 于 2026 年 11 月 17 日发布 jQuery 4.1.0 与 3.8.0。3.8.0 是 3.x 分支最后一个计划功能版本，未来 3.x 仅接收关键安全与缺陷修复；官方建议用户尽快升级到 4.x，并提供升级指南和 jQuery Migrate 插件辅助迁移。

- 🚀 两个版本均包含 AJAX transport `completeCallback` 新调用方式：可传入单个对象，便于未来扩展并选择性提供参数。
- 🛡️ 修复选择器标识符匹配中的 ReDoS 漏洞，并将选择器中的严格文档比较改为松散比较，避免旧版 IE/Edge 偶发崩溃。
- 🔗 4.1.0 为 `jqXHR` 新增 `responseURL`，可获取浏览器跟随重定向后的最终请求 URL。
- 🧩 4.1.0 支持序列化与表单关联的自定义元素，并让 CSS 方法可在非 XHTML XML 文档中正常工作。
- ⚡ 4.1.0 全面改用 `querySelectorAll`，替代 `getElementsByTagName` / `getElementsByClassName`，修复部分旧缺陷并优化选择性能。
- 🏎️ 4.1.0 优化 `jQuery.uniqueSort` 去重算法，从 O(N²) 降至 O(N)，行为与排序不变。
- 🧭 3.8.0 支持 `hidden="until-found"`，并正式弃用 jQuery 原型上的 `push/sort/splice` 及 `jQuery.expr[":"]` / `jQuery.expr.filters`。
- 🩹 3.8.0 回移多项 4.0.0 修复，包括自移除脚本的 `.html()`、`jQuery.cleanData`、表格 `<col>` 尺寸、`leverageNative` 原生事件处理及 CSS zoom/隐藏 iframe 支持测试。
- 📦 发布文件可通过 jQuery CDN 和 npm 获取，包含普通版与 slim 版；3.x 后续只做关键修复，4.x 是活跃开发主线。

---

### [GitHub - camsong/You-Dont-Need-jQuery: Examples of how to do query, style, dom, ajax, event etc like jQuery with plain javascript. · GitHub](https://github.com/camsong/You-Dont-Need-jQuery)

**原文标题**: [GitHub - camsong/You-Dont-Need-jQuery: Examples of how to do query, style, dom, ajax, event etc like jQuery with plain javascript. · GitHub](https://github.com/camsong/You-Dont-Need-jQuery)

该项目是 camsong 维护的 You-Dont-Need-jQuery，用原生 JavaScript 示例展示如何替代 jQuery 的查询、样式、DOM、Ajax、事件、工具函数、Promise 和动画等常见操作；仓库约 20.1k Star、1.7k Fork，采用 MIT 许可证，并提供多语言 README。

- 🔍 **查询选择器**：可用 `document.querySelector` / `querySelectorAll` 替代 jQuery 选择器；注意 `querySelector` 返回首个匹配元素或 `null`，`querySelectorAll` 返回静态 NodeList。
- 🎨 **CSS 与样式**：使用 `getComputedStyle`、`el.style`、`classList` 等实现样式读写与类名增删切换。
- 📐 **尺寸与位置**：用 `clientHeight`、`offsetHeight`、`getBoundingClientRect`、`offsetLeft`、`scrollY` 等替代 jQuery 的宽高、位置和滚动操作。
- 🧱 **DOM 操作**：原生支持 `remove`、`textContent`、`innerHTML`、`append`、`prepend`、`before`、`after`、`matches`、`cloneNode`、`replaceChildren` 等。
- 🌐 **Ajax**：推荐使用 `fetch` 替代 `$.ajax` / `$.getJSON`；需自行检查 `response.ok`，并可用 `AbortController` / `AbortSignal.timeout` 实现取消和超时。
- 🖱️ **事件处理**：使用 `addEventListener`、`removeEventListener`、`{ once: true }`、事件委托和 `CustomEvent` / `dispatchEvent` 替代 `on`、`one`、`off`、`trigger`。
- 🛠️ **工具函数**：`Array.isArray`、`Object.assign`、`structuredClone`、`Array.from`、`String.prototype.trim`、`Array.prototype.map/filter/includes` 等可替代多数 jQuery 工具方法。
- ⏳ **Promise**：原生 `Promise`、`then/catch/finally`、`Promise.all`、`async/await` 和 `Promise.withResolvers` 可替代 `done/fail/always`、`$.when`、`$.Deferred`。
- 🎞️ **动画**：Web Animations API（`el.animate()`）最接近 jQuery 动画效果，可实现显示隐藏、淡入淡出、滑动和自定义动画。
- ⚠️ **注意事项**：项目面向现代常青浏览器，已移除 IE 专用兼容方案；原生替代并非所有场景完全等价，迁移前应测试。
- ✅ **适用建议**：jQuery 仍是优秀库且有合理使用场景；不必强行迁移，只有在适合时再采用原生方案。

---

### [Chrome 158 发布说明 - Chrome 平台状态](https://chromestatus.com/release-notes/158)

**原文标题**: [Chrome 158 Release Notes - Chrome Platform Status](https://chromestatus.com/release-notes/158)

本次 Chrome 更新涵盖 CSS 高亮与对齐、SVG 嵌入与文本路径、Web 应用安装、媒体状态与音频渲染、权限策略、WebHID Android 支持及 WebTransport 网络能力增强，并提供相应企业管控策略。
- 🎨 CSS 新增 `::highlight(*)` 通用选择器，可匹配所有自定义高亮伪元素；`*` 不贡献特异性，适合作为基础样式并被具名高亮规则覆盖。
- ↔️ 新增 `flow-start`/`flow-end` 对齐关键字，作为 `flex-start`/`flex-end` 的别名，用于放置方向反转场景；序列化时返回 `flow-start`/`flow-end`。
- 🖼️ `object-fit` 和 `object-position` 现可作用于 `<object>`/`<embed>` 中加载的 SVG 文档，行为类似 `<img>`，不再总是拉伸整个内容框。
- 📲 新增 HTML `<install>` 元素，无需 JavaScript 即可请求安装跨源 Web 应用，并可由企业策略与权限策略控制。
- ⚙️ Web Install API 自 Chrome 158 起提供 `navigator.install()`，以命令式方式提示安装 Web 应用，并与 `<install>` 元素并行推出。
- 🎬 新增媒体元素伪类 `:playing`、`:paused`、`:seeking`、`:buffering`、`:stalled`、`:muted`、`:volume-locked`，根据音频/视频状态匹配元素。
- 🎧 `OfflineAudioContext` 支持增量渲染，通过分块处理音频图数据，降低处理大量数据时的内存需求。
- 🔒 新增 `focus-without-user-activation` 权限策略，控制嵌入内容在无用户激活时的程序化聚焦；不影响用户点击或 Tab 聚焦。
- ✍️ SVG `textPath` 新增 `side` 属性，可选择文本沿路径哪一侧排列；`side="right"` 可反转路径方向，便于在圆形路径内外放置文字。
- 📡 Direct Sockets API 为 Isolated Web Apps 增加源特定多播（SSM），允许加入多播组时指定源地址，仅接收该源 UDP 数据，提升过滤与抗欺骗/DoS 能力。
- 🖱️ WebHID 扩展至 Android（Chrome 158，依赖 Android 17/API 37+），Web API 表面不变；不支持 WebView，并提供多项企业策略控制。
- 🌐 WebTransport 新增预期并发入站流提示，可通过构造参数配置初始 QUIC 流额度，降低高并发服务器被初始流限制阻塞的风险。
- ⏳ WebTransport 新增 `draining` Promise，服务器指示会话将优雅退役时可提前建立替代会话，同时保持现有流可用。
- 📶 WebTransport 新增 `reliability` 与 `supportsReliableOnly` 属性，用于指示是否支持可靠连接及不可靠数据报；Chromium 初始返回 `pending`，HTTP/3 连接后为 `supports-unreliable`，`supportsReliableOnly` 返回 `false`。

---

### [DevTools 新功能 - 2026 年 12](https://developer.chrome.com/blog/new-in-devtools-december-2026)

**原文标题**: [New in DevTools - December 2026  |  Blog  |  Chrome for Developers](https://developer.chrome.com/blog/new-in-devtools-december-2026)

本期汇总 Chrome 157 和 Chrome 158 中 DevTools 的重要更新，涵盖面向编码代理的 MCP 工具、AI 辅助 Lighthouse 审计、Elements/Sources/Application/Performance/Memory 面板增强，以及网络、控制台、设备模式和无障碍改进；同时 Modern Web Guidance 已稳定。

- 🚀 Modern Web Guidance 已稳定，可为编码代理提供专家审核的 Web 开发最佳实践。
- 🤖 Chrome DevTools MCP 服务器 v1.11.0–v1.13.0 新增日志点、虚拟 WebAuthn 认证器、配置热重载、离线堆快照分析、并行工具执行等能力。
- 🧪 AI 辅助功能可运行多类别 Lighthouse 报告和代理浏览审计，并内联显示失败审计、评分仪表和 DOM 节点。
- 🎛️ Elements 面板支持强制 `:buffering` 和 `:stalled` 媒体状态，新增 `position-try-fallbacks` 交互式色板、`position-area` 对齐编辑和 IMCB 覆盖高亮。
- 🧭 Sources 面板支持 ECMA-426 source map scopes，可在 Scope 视图、堆栈跟踪、表达式求值和自动补全中使用原始变量与函数名。
- 📱 Application 面板新增 Sub apps 检查、Isolated Web App 身份信息、自定义拼写检查词典查看和存储数据清理改进。
- ⚡ Performance 和 Memory 面板优化大型 trace 解析速度与内存占用，改进 Lantern HTTP/2、HTTP/3 和 ES module 模拟，并增强生成器/异步函数/ES module 的堆快照上下文分析。
- 🌐 Network、Console 和 Device Mode 有多项改进，包括 WebSocket 非 ASCII 文本帧字节长度、仅复制可见控制台文本、设备截图直接复制到剪贴板等。
- ♿ 无障碍改进包括实时公告跳转到 JavaScript 调用点、键盘焦点指示器对比度提升，以及 Settings、Application、Recorder 中的屏幕阅读器语义增强。

---

### [汉堡王、麦当劳与特朗普推文中的旧 Bitly 链接遭劫持 | Ransomnews](https://ransomnews.com/burger-king-tweet-bitly-link-hijack-2026/)

**原文标题**: [Old Bitly links hijacked in Burger King, McDonald’s and Trump tweets | Ransomnews](https://ransomnews.com/burger-king-tweet-bitly-link-hijack-2026/)

概述总结  
2026 年 11 月 15 日，攻击者通过重新注册旧 Bitly 短链接的后半段，使多年前的推文跳转到无关或恶意页面。Burger King、McDonald’s、Donald Trump 等旧帖受影响，Bitly 确认问题并停用相关链接；没有证据表明相关账号被黑。

- 🍔 Burger King 2011 年推文中的 Bitly 链接被他人于 2026 年 11 月 15 日重新注册，跳转到维基百科“纳粹集中营列表”；品牌账号并未被入侵。
- 🍟 McDonald’s 2011 年推文中的 Bitly 链接于同日 05:14 被重新注册，跳转到维基百科“9·11 袭击”条目；同样不是账号被黑。
- 🔗 攻击方式是“短链接劫持/失效链接劫持”：旧 Bitly 链接的后半段可被重新注册，原推文、邮件、PDF 或二维码会跳转到新主人指定的页面。
- 📊 对 Trump 2009 至 2013 年 97 条 Bitly 链接的检查显示：40 条仍为原始链接，49 条被重建但大致指向原内容，7 条指向无关内容，1 条被 Bitly 拦截。
- ⚠️ 7 条异常链接中，4 条于 2026 年 11 月 15 日注册，分别指向 Roblox 资料页、YouTube 视频和关于 Trump 与 Jeffrey Epstein 的维基页面。
- 🧨 一条 2011 年 Trump 推文包含三个子女视频链接，三个均被替换；其中两个指向仿冒 World Liberty Financial 和 DappRadar 的加密相关域名。
- 🕵️ 最早发现的变更在 11 月 14 日晚；Burger King 与 McDonald’s 链接变更相隔 18 分钟，观察者怀疑同一行为者所为，但无确证。
- ✅ Bitly 于 19:13 UTC 在 X 确认问题，称恶意行为者滥用了某些旧的非活跃链接，已暂停涉事账号并停用受影响链接，Trust and Safety 团队正在加强防护。
- 🛑 至 19:22 UTC，Burger King、McDonald’s 及 7 条异常 Trump 链接均显示“Link Deactivated”；49 条被重建但仍指向原意的链接仍可访问。
- 📰 CNN 当晚报道 Bill Gates、Justin Trudeau、Mike Pence、FBI、美国国防部等旧帖也受影响；Ransomnews 未独立核实这些链接。
- 🚫 Burger King 和 McDonald’s 均未被黑客入侵；推文内容未变，变化发生在 Bitly 侧，旧链接被重新分配。
- 🛡️ 建议品牌导出旧帖中的 bit.ly 链接，在链接后加“+”查看创建日期和目的地；若创建日期晚于发帖时间，说明链接已不属于原发布者，应删除或报告 Bitly。
- 💡 普通用户不要因账号认证或帖子陈旧就信任链接；点击前用“+”预览目的地，尤其警惕要求登录或连接加密钱包的页面。
- 🔍 风险不限于 X：旧邮件、PDF、幻灯片、印刷二维码和帮助页中的短链接同样可能被劫持，并可能被用于诈骗。

---

### [获取失败](https://arc.net)

**原文标题**: [Failed to retrieve](https://arc.net)

无法总结：获取内容失败，状态码 403。

---

### [2026 年 Arc 关闭后最佳 Arc 浏览器替代品](https://blog.master.dev/browsers-to-try-if-youre-being-forced-off-arc/)

**原文标题**: [Best Arc Browser Alternatives After Arc Shuts Down in 2026](https://blog.master.dev/browsers-to-try-if-youre-being-forced-off-arc/)

作者因 Arc 将于 2026 年 12 月 22 日停止支持，转而寻找 Arc 风格替代浏览器；文章基于个人实际使用体验，比较各浏览器的优点与痛点，并指出 Cra 目前最接近 Arc、作者尚未弃用。

- ⏳ Arc 官方宣布 2026-12-22 日落；应用不会立刻消失，但同步可能停止，且缺少 Chromium 更新会带来安全风险。
- 🧭 作者重点看 Arc 的 Spaces、分屏、Little Arc、固定标签等体验；正文因缺少 Spaces/分屏排除 Aside、Phi、Nav8，评论中有人认为 Phi 已有改进。
- 🏢 Dia：Arc 团队下一代产品，需 Atlassian 账号；有打磨，但标签同步不完整、无 Little Arc、固定标签不跨空间、空间指示点太小、AI 聊天不实用。
- 🧩 Crest：高度还原 Arc，大 emoji 固定标签/空间指示、Peek/Quick Windows 不错；但 Kagi 默认搜索、URL 栏布局、1Password 扩展和 Chromium+WebKit 双引擎造成问题。
- 🦊 Zen：最精致、最忠实的 Arc 移植之一，团队和支持成熟；但基于 Firefox，DevTools、部分网站/扩展不便，无 Little Arc，空间图标变灰。
- 🗂️ Ardia：Arc+Dia 风格，Little Ardia、iCloud 同步是亮点；但空间即配置文件、非固定标签随窗口丢失，光标消失 bug 劝退。
- 🧪 yab：WebKit 版 Arc 克隆，支持 Chrome DevTools/扩展，可自带 AI；但 UI 有重叠、全局安装 skills/MCP 造成意外，无 Little Arc。
- 🧱 Arcium：基于 Helium 的实验，隐私方向有趣；但空间总开新窗口、不能装扩展，暂不成候选。
- 🎯 Cra：最直接的 Arc 克隆，导入器好用、iCloud/Dropbox 同步、Little Arc 完整、支持常驻工具栏；仅发现扩展无法移除的小 bug，作者尚未弃用。
- 🏹 Flecha：Chromium Arc 克隆，开发者向搜索、固定标签跨空间、拖拽分屏、MCP 控制；但本地服务栏不可关、设置内文件夹管理、无真正 Little Arc、固定标签不能拖拽排序。
- 📌 其他提及：Safari/Chrome/Firefox 已有侧边标签等基础能力；Search Browser 设计好但无同步；Vivaldi 功能过载；Orion 扩展支持好但放弃 Windows/Linux。
- 💬 评论补充：Flecha 名称是西班牙语“箭”，与 Arc/弓呼应；Aside 因无 Spaces/分屏被作者排除。

---

### [HTML 和 CSS 中的图表](https://www.keithcirkel.co.uk/html-graphs/)

**原文标题**: [Charts in HTML and CSS](https://www.keithcirkel.co.uk/html-graphs/)

本文介绍了一种仅使用语义化 HTML 和 CSS 来构建图表的方法：不依赖 JavaScript、图表库或 SVG，同时保证内容在移除样式后仍可读，并兼顾屏幕阅读器与交互体验。文章按图表类型给出实现思路，并总结了 CSS 原生能力的边界与上线前检查要点。

- 🧱 以语义化元素为基础：表格用于一组或多组数据，`<meter>` 表示相对上限的值，列表表示有序数据或占比，`<data>` 表示机器可读的数值。
- 🎨 用 CSS 自定义属性传递数值：文本供人阅读，`--v` 等属性供布局计算，并通过 `calc()` 将数值缩放到 0 到 1 的比例。
- 🖌️ 用 CSS 现有能力绘图：背景尺寸绘制条形，`color-mix()` 绘制热力，`conic-gradient()` 绘制饼图，伪元素结合 `atan2()` 绘制线段。
- 🧮 借助 `sibling-index()` 和 `sibling-count()` 自动处理颜色与位置，减少手工编号。
- 🖱️ 交互完全由选择器完成：`:hover` 显示提示，`:has()` 联动其他区域，图例中的复选框控制系列显隐，全程无需 JavaScript。
- 📊 按场景选择图表：上限对比用 `meter`，单系列用柱状图，多系列用条形图，二维数值用热力图，占比用环形图，头条数字与趋势用统计卡片和迷你折线图，时间序列用折线图或面积图。
- 📏 所有比例、最小值和最大值通常需要写入标记中，因为 CSS 无法跨兄弟节点读取值或计算最大值、总和。
- 🔗 连接两个数据点的图形需要重复相邻值，例如折线段的 `--a` 和环形图扇区的 `--from`。
- 🧩 表头与同列单元格的关联需要为每列编写 `:nth-child()` 选择器；图例显隐和悬停隔离也依赖固定选择器块。
- 🔢 计数器可将计算数值转为文本，但只输出整数，且没有千位分隔符或默认“+”号；可用 `@counter-style` 处理正负号。
- 🎯 透明像素仍会捕获指针，因此装饰层应设置 `pointer-events: none`，并用 `clip-path` 精确限定点击区域。
- 🪟 注意层叠上下文：`transform`、`opacity`、`z-index` 等会创建独立上下文，共享图层应放在统一的 `isolation: isolate` 父级中。
- 🧷 悬停不能改变布局：为悬停文本预留空间，使用固定标签列、`min-width: 0` 和溢出处理，避免元素移位。
- 🧵 目标之间不要留空隙，否则悬停会闪烁；让悬停区域相邻，并把视觉间隙绘制在区域内部。
- 📐 细线应对齐整像素，避免 1px 线落在小数像素位置时被浏览器丢弃。
- ✅ 上线前需逐项检查：悬停不引发布局变化、不闪烁、不遮挡标签；验证明暗主题；移除样式后内容仍可作为表格或列表阅读。
- 🌐 已在 Chromium 155 和 Firefox 158 中检查，Safari 尚未测试；依赖的新特性包括 `sibling-index()`、`@property`、`:has()`、三角函数、容器查询、`color-mix()`、`oklch()`、`light-dark()` 等。
- 🤖 该页面也可作为编码代理的技能参考：保存为 `html-graphs/reference.html`，并配合 `SKILL.md` 让代理按相同模式生成图表。

---

### [Highcharts 轨道 | Highcharts](https://www.highcharts.com/products/orbit/?utm_source=frontendfocus&utm_medium=newsletter_sponsoredlink)

**原文标题**: [Highcharts Orbit | Highcharts](https://www.highcharts.com/products/orbit/?utm_source=frontendfocus&utm_medium=newsletter_sponsoredlink)

Orbit 是 Highcharts 的增强分析工具，可通过一个脚本将现有图表升级为可探索、预测、注释和分享的交互式分析工具，无需定制开发，并提供 60 天免费试用。

- 🚀 **单脚本集成**：无需从零构建或编写自定义代码，即可为所有现有 Highcharts 图表添加强大分析能力。
- ⏱️ **快速交付**：几分钟内即可提供专业分析体验，而不是耗时数月开发。
- 🔍 **深度分析**：用户可在图表中筛选、预测、注释并分享洞察，还能连接多个可视化以发现数据关系。
- 🔗 **交互式分享**：分享链接会保留筛选、预测和注释，同事可交互探索，无需上传图表数据到外部服务。
- 🧭 **页面模式**：将整个仪表盘变为分析工作区，可跨图表、地图和数据网格比较与调查数据。
- 🧰 **丰富工具栏**：支持异常检测、预测、相关性、摘要统计、数据网格、筛选聚焦、派生系列、技术指标、全屏和纯图表模式。
- 🤖 **可选 AI 功能**：AI 助手、叙述器、洞察和替代可视化处于 Beta，可独立配置并可完全禁用。
- 🛡️ **安全可靠**：由 Highcharts 团队开发和维护，提供文档、专业支持和持续维护。
- ⚙️ **集中管理**：通过管理后台控制功能开关、使用量与信用、团队权限及全局品牌样式。
- 🔐 **数据隐私**：多数工具在浏览器本地运行；仅发送匿名使用统计，启用 AI 时图表配置和数据会发送至 Orbit 后端处理。
- 📦 **使用要求**：需 Highcharts 12 或更高版本；数据网格和技术指标等功能可能需要 Highcharts Grid Pro 或 Highcharts Stock 额外许可。
- 💻 **本地开发**：可将 localhost 或 127.0.0.1 加入部署，便于本地开发测试，且不计入站点数量。
- 📞 **获取支持**：如需定价、方案选择或设置帮助，可联系销售团队。

---

### [CSS caret-* 属性与自定义插入符可访问性](https://www.sarasoueidan.com/blog/caret-styling-accessibility/)

**原文标题**: [The CSS caret-* properties and custom caret accessibility](https://www.sarasoueidan.com/blog/caret-styling-accessibility/)

本文围绕 CSS 的 `caret-*` 属性与自定义光标可访问性展开，说明光标不仅是输入框中的插入光标，也可在“光标浏览”模式下作为键盘导航光标；作者强调自定义光标样式虽有潜力，但必须优先尊重用户系统偏好，并满足 WCAG 与 EN 301 549 等可访问性要求，否则可能损害键盘用户和指针用户的体验。

- 🧭 **光标有两种重要形态**：可编辑区域中的“插入光标”是焦点指示器；启用光标浏览后，页面中的“导航光标”帮助键盘用户精确定位和选择文本。
- ⌨️ **光标浏览是重要的键盘导航功能**：按 `F7` 可在 Edge、Chrome、Firefox 等浏览器中启用，用方向键移动光标、选择文本和跟随链接；Safari 虽支持但光标不可见。
- 🎨 **浏览器默认光标颜色继承文本颜色**：默认使用 `currentColor`，因此光标在链接上可能随链接颜色变化；默认样式由 CSS Basic User Interface 模块定义。
- ⚙️ **操作系统提供光标可访问性设置**：macOS 有“优先非闪烁光标”，且被主流浏览器应用于插入光标和导航光标；Windows 提供文本光标指示器、粗细和闪烁速率设置。
- 🚫 **浏览器对系统偏好支持并不完整**：Windows 的光标粗细和闪烁速率设置目前不被浏览器应用于插入光标，导航光标也不支持多数 Windows 光标设置。
- 🧩 **CSS 提供三类光标样式属性**：`caret-color` 设置颜色，`caret-shape` 设置形状，`caret-animation` 控制动画，另有 `caret` 简写；规范主要面向插入光标，浏览器可自行决定是否应用于导航光标。
- 📏 **`caret-shape` 支持有限**：可选 `bar`、`block`、`underscore`；目前主要在 Chromium 浏览器中需启用实验性功能，且块状光标可能因透明度降低而影响对比度。
- 🎞️ **自定义动画需谨慎**：`caret-animation: manual` 可接管闪烁动画，但快速闪烁可能触发 WCAG 2.3.1 风险；应避免快速闪烁，并用 `prefers-reduced-motion` 限制动画。
- ✅ **插入光标需满足焦点可见与对比度要求**：作为焦点指示器，应满足 WCAG 2.4.7；修改 `caret-color` 后需确保与相邻颜色至少 3:1 对比度，或提供其他合格焦点指示器。
- 🔍 **导航光标也需非文本对比度**：它不属于焦点指示器，但受 WCAG 1.4.11 约束；自定义颜色需在文本框、可编辑区域及其他页面背景上都保持至少 3:1 对比度。
- ⚖️ **用户需求优先于作者样式**：Web 设计原则和 EN 301 549 v4.1.1 都要求尊重用户偏好，网页不应阻止或显式覆盖用户代理按用户设置呈现内容。
- 🛑 **实践建议是保守定制光标**：不要只依赖光标作为唯一焦点指示器；如必须自定义，应提供关闭自定义光标样式的选项，并等待浏览器提供更可靠的用户偏好检测与覆盖机制。

---

### [Apple HomeView 上的 Safari | WebKit](https://webkit.org/blog/18608/safari-on-apple-homeview/)

**原文标题**: [  Safari on Apple HomeView | WebKit](https://webkit.org/blog/18608/safari-on-apple-homeview/)

Safari 正式登陆 Apple HomeView，成为继 macOS、iOS、iPadOS 和 visionOS 之后的新平台。文章说明：大多数网站无需专门改动即可运行，但开发者可通过结构化菜谱数据、字幕轨道、语义化 HTML、功能检测和响应式布局，让站点在语音、触控、方形小屏等场景下表现更好。

- 🍎 Safari 于 2026 年 11 月 13 日登陆 Apple HomeView，基于 WebKit。
- 🗣️ 用户可隔空语音操作，也可轻触 7 英寸方形显示屏，快速查资料、打开链接、看菜谱等。
- 🧑‍💻 开发者通常无需额外适配，因为 Web 本身面向不同屏幕和输入方式设计。
- 🍳 烹饪体验会识别页面中的菜谱，并基于 schema.org Recipe 的 JSON-LD 数据提供分步精简视图；建议站点补充相应标记。
- 🎬 HomeView 支持丰富的音视频体验；视频字幕建议使用 WebVTT，并通过 `<track>` 元素提供。
- ♿ 避免假设用户只会点击或触控；语音是重要输入方式，应使用真实按钮、链接、表单控件、清晰标签、大触控目标和灵活布局。
- 🧭 避免 User-Agent 嗅探；HomeView 也会报告 iOS UA，应改用功能检测，并用 Smart App Banners 替代自定义下载应用横幅。
- 📐 注意方形和较矮视口：固定页眉页脚可能挤压内容，过高的弹窗可能无法关闭；可用 `max-height: 90vh; overflow-y: auto;` 等布局修复。
- 🧪 若无 HomeView 设备，可在手机横屏下测试，或在 Safari 响应式设计模式中设置视口为 448×364。
- 🌐 采用现代最佳实践构建健壮、灵活的网站，更有可能适应未来新设备和新交互方式。

---

### [PropFLIP · 2026 年 11 月 10 日](https://nerdy.dev/prop-flip)

**原文标题**: [PropFLIP Â· November 10, 2026](https://nerdy.dev/prop-flip)

文章介绍 PropFLIP：一种把 FLIP 动画与 `@property` 类型化自定义属性、CSS transition 结合起来的现代做法。它用 4 个可过渡属性控制位移与缩放，实现可中断的布局动画，同时修复缩放造成的圆角和内容挤压，并讨论性能边界。

- 🧩 核心思路：布局先到 Last，再用 `transform` 把元素视觉上拉回 First，然后过渡回 `0/1`，避免直接动画 `left/top/width/height` 导致逐帧布局。
- ⚙️ 四个类型化属性：`--tx`、`--ty` 默认 `0`，`--sx`、`--sy` 默认 `1`；用 `translate()` 和 `scale()` 组合出 FLIP 变换，`transform-origin: top left` 便于配合 `getBoundingClientRect()`。
- 🎞️ CSS 负责播放：每个属性可单独设置 duration、easing、delay，因此能做弧线、摆动、不同节奏，并支持中途打断。
- 🟠 修复缩放变形：圆角用 `calc(var(--r)/var(--sx)) / calc(var(--r)/var(--sy))` 保持形状；直接子元素用反向 `translate/scale` 抵消父级缩放，所以 `--sx/--sy` 特意设为继承。
- 🧪 JS 流程：measure First → 关闭 transition → 改 DOM → measure Last → 写入反向 `--tx/--ty/--sx/--sy` → 读 `offsetHeight` 强制提交 → 恢复 transition → 重置为 `0/1`。
- ⚡ 性能限制：布局只计算一次，但每帧仍有样式重算；继承的 `--sx/--sy` 会令后代失效，且注册属性动画目前不在合成器线程，适合少量元素，不适合数百元素或主线程繁忙页面。
- 🚀 作者期望：未来浏览器能让类型化自定义属性动画离开主线程；现阶段 PropFLIP 是“少 JS”与“性能不一定最佳”的权衡。
- 💬 评论反馈：圆角修复很实用；可中断是亮点；也有人关注 SVG 图标、子元素缩放和中途打断时是否稳定。

---

### [为 AI 智能体提供更好的 CSS 调试方法 — Amit Merchant — 关于 PHP、JavaScript 等的博客](https://www.amitmerchant.com/giving-ai-agents-a-better-way-to-debug-css/)

**原文标题**: [Giving AI Agents a Better Way to Debug CSS — Amit Merchant — A blog on PHP, JavaScript, and more](https://www.amitmerchant.com/giving-ai-agents-a-better-way-to-debug-css/)

文章介绍了如何通过 Chrome DevTools MCP 的新工具 `get_css_styles`，让 AI 编程助手直接在浏览器中检查元素实际应用的 CSS 规则，从而更准确地诊断样式覆盖、优先级和级联问题，而不是仅靠阅读源码猜测。

- 🔍 **核心问题**：CSS 声明看似有效却未生效，通常与级联、优先级、级联层、媒体查询或继承有关。
- 🛠️ **解决方案**：Chrome DevTools MCP 提供 `get_css_styles`，可让 AI 代理查看浏览器中真实应用的样式信息。
- ⚙️ **配置方式**：在 Codex 中添加自定义 MCP 服务器，名称设为 `chrome-devtools`，类型为 `STDIO`，命令为 `npx -y chrome-devtools-mcp@latest`。
- 🧭 **工作流程**：AI 先用 `take_snapshot` 识别页面元素，再把元素 UID 传给 `get_css_styles` 获取匹配规则、继承样式、内联样式、自定义属性和被覆盖声明。
- 🎯 **示例诊断**：当 `#main .card h2` 的绿色规则胜过 `.card h2` 的红色规则时，AI 可识别这是由更高特异性导致。
- 🧹 **扩展用途**：可用于 CSS 审计，发现冗余声明、重复规则、不必要的高特异性、冲突的级联层和重复的 `!important`。
- 📱 **更多场景**：还可调查暗色模式、响应式布局、冲突媒体查询等样式问题。
- 🤖 **价值与限制**：AI 不再只依赖源码猜测，而能基于浏览器运行时信息给出更有依据的诊断；但仍需人工复核其结论和修改建议。

---

### [构建一个 atproto 链接聚合器 | jola.dev](https://jola.dev/posts/building-atproto-link-aggregator)

**原文标题**: [
      Building an atproto link aggregator | jola.dev
    ](https://jola.dev/posts/building-atproto-link-aggregator)

overview summary  
shelf.cafe 是作者用 Elixir 构建的 atproto 链接聚合器实验，结合自动抓取博客与用户提交，支持评论、投票、热榜与回链展示，并强调性能、数据自主和避免供应商锁定；上线后已有 7K+ 链接。

- 🧪 **项目定位**：shelf.cafe 是 atproto 链接聚合器实验，目标是结合 Bubbles 的自动内容流与 Reddit/HN 式提交、评论和投票。
- 🔗 **内容来源**：像 Bubbles 一样关注一组博客 feed 并自动发布新内容，同时支持用户单独提交链接。
- ⚙️ **核心功能**：支持评论、投票和按热度衰减排序的首页；首页会保持内容新鲜。
- 🚀 **性能设计**：首页加载约 250ms，未缓存首屏约 170kB；采用服务端渲染，优化移动端弱网体验。
- 💬 **回链索引**：实时处理 Bluesky 帖子，记录提及 Shelf 已提交 URL 的帖子，把相关讨论自动展示在评论区，缓解冷启动问题。
- 🛡️ **审核机制**：使用 atproto 标签器（Bluesky、Blacksky、Northsky、Skywatch Blue）自动隐藏垃圾/诈骗内容，并可本地封禁；曾用于隐藏大量 HN 机器人。
- 📈 **排名算法**：使用 `Score = Votes ^ 0.8 / (Age + 2) ^ 1.8`，让新内容每天有机会刷新，同时高票内容可停留更久。
- 📚 **博客列表**：最初沿用 Bubbles 的公开 OPML，但正转向更精选、偏长文和深度写作的列表，未来计划提供 `/blogs.opml`。
- 🧩 **投票组件**：提供 CORS 开放的 XRPC `getItems` 接口和可嵌入的“Vote on Shelf”小组件，可显示票数或引导提交链接。
- 🌐 **atproto 特性**：词表已发布，渲染首页所需数据都在协议上；用户可自建 AppView、另写排序算法，甚至从协议重建 Shelf 数据库。
- ⌨️ **提交方式**：除网站外，也可用 `goat` 命令行工具直接创建 `cafe.shelf.item` 记录，体现协议层互操作与自动化潜力。
- ✍️ **开发理念**：作者坚持手写代码、重视工程质量与数据所有权，认为 atproto 的核心价值是用户拥有数据、无供应商锁定。

---

### [Allo，你友好的邻里字体](https://allo.joshpuckett.me/)

**原文标题**: [Allo, your friendly neighborhood font](https://allo.joshpuckett.me/)

Allo 是一款免费开源的友好型可变字体，面向屏幕与界面设计，在清晰、温暖与可调性之间取得平衡，并提供丰富字符、OpenType 功能和多语言支持。

- 🎨 可变字体：支持字重、圆润度和光学尺寸调节，可灵活塑造字体个性。
- ⚖️ 三个可变轴：字重 100–900、圆润度 0–100、光学尺寸 14–32，并会自动适配文本与展示场景。
- 🖥️ 屏幕与界面优化：适合 UI 使用，兼顾可读性与亲和力。
- 🔤 细节丰富：包含表格数字、分数、随大写字母抬升的标点、输入即出现的箭头，以及各字重下的真斜体。
- 🌍 多语言支持：覆盖 50+ 种语言。
- ✨ 字符与功能：606 个字形、467 个字符，支持风格集、替代字形、上下文替代等功能。
- ⌨️ 界面符号齐全：提供命令键、箭头、勾选、警告等常用 UI 符号。
- 🆓 免费开源：采用 SIL Open Font License，价格 $0.00。
- 📦 获取方便：可下载全部字重与样式，也支持 `npm i allo-font` 使用 Web 字体。
- 🙏 设计背景：基于 Inter 4.1 重绘，作者 Josh Puckett，并向 Honk Sans 致敬。

---

### [GitHub - joshpuckett/allo：Allo 是你身边友好的字体，免费且开源 · GitHub](https://github.com/joshpuckett/allo)

**原文标题**: [GitHub - joshpuckett/allo: Allo is your friendly neighborhood typeface, free and open source · GitHub](https://github.com/joshpuckett/allo)

Allo 是一款免费开源的友好型可变字体，专为屏幕和界面设计，支持字重、圆润度与光学尺寸调节，并提供静态字体、可变字体、Web 字体及 npm 安装方式。

- 🔤 开源字体：Allo 免费开源，采用 SIL Open Font License 1.1，可商用、修改和再分发，但不能单独售卖字体。
- 🎛️ 三个可变轴：光学尺寸 opsz 9–32（默认 14）、字重 wght 100–900（默认 400）、圆润度 ROND 0–100（默认 50）。
- 📦 字体文件：提供 18 个静态字体（Thin 到 Black，各带 Oblique）、AlloVariable.ttf，以及 WOFF2 网页字体。
- 🌐 Web 使用：可通过 npm 安装 `allo-font`，也可自托管 `fonts/webfonts` 中的 WOFF2 文件。
- ⚡ 精简版本：`AlloVariableFriendly.woff2` 将圆润度固定为 50，文件约小一半。
- 🔠 OpenType 功能：支持单层 a、消歧字形、开放数字、表格数字、分数、上下标、大写旁标点、连字和上下文替代等。
- 🖥️ 屏幕优化：光学尺寸随字号自动调整，Display 更紧凑，小字号主要调整间距。
- 🛠️ 构建方式：需 Python 3.9+，运行 `build.py` 可生成字体文件、校验和与发布压缩包，构建可复现。
- 📐 源文件结构：`Allo.designspace` 含 48 个主 master 和 8 个稀疏图层；静态字体从可变字体母版切出后单独编辑，斜体为独立绘制。
- 🤝 贡献规则：发现问题或缺字可开 issue；目前暂不接受直接修改母版或字体文件的 Pull Request。
- 🌱 来源与致谢：Allo 基于 Inter 4.2 起步，但所有字形均已重绘，并参考 Honk Sans 的温暖趣味风格。

---

### [谁先发货？](https://patrickbrosset.com:443/lab/who-shipped-first/)

**原文标题**: [Who shipped first?](https://patrickbrosset.com:443/lab/who-shipped-first/)

概述：该内容比较各浏览器引擎在桌面端“谁最先支持某个 Web 功能”，依据 web-features 数据集中首个支持版本的发布日期，并排除早期已支持及 discouraged 功能。

- 🌐 比较对象：Chromium（Chrome 和 Edge）、Gecko（Firefox）、WebKit（Safari）三大浏览器引擎。
- 🖥️ 统计口径：仅统计桌面版本，排除 discouraged 功能，以 web-features 数据集中首个支持该功能的版本发布日期为准。
- ⏳ 排除早期功能：任一引擎在 2008-12-11 前已支持的 178 个功能不计入，因为 Safari 和 Firefox 早于 Chrome 多年，计入无法说明谁更早创新。
- 🤝 同月首发不计：若最早支持的引擎在同一月发布该功能，则视为协同发布，不把“首创”归给任何引擎。
- 📅 数据说明：数据生成于 2026-11-18；另有 32 个功能因首个支持版本仅为近似值（如“≤79”）而被排除。
- 📊 分析范围：可分为全部功能、至少 2 个引擎支持的功能、3 个引擎均支持的功能。
- 🏷️ 展示维度：按引擎统计“首创”数量，并展示随时间累计的首创情况；分类包括 Chromium、Gecko、WebKit 以及“无人（同月）”。

---

### [适用于任意规模时间序列工作负载的 Postgres。 | Tiger Data](https://www.tigerdata.com/go/trial?utm_source=content-syndication&utm_medium=referral&utm_campaign=frontend-focus-newsletter&utm_content=sponsored-chartquery-1118)

**原文标题**: [Postgres for time-series workloads at any scale. | Tiger Data](https://www.tigerdata.com/go/trial?utm_source=content-syndication&utm_medium=referral&utm_campaign=frontend-focus-newsletter&utm_content=sponsored-chartquery-1118)

Tiger Data 的 Tiger Cloud 是面向任意规模时间序列工作负载的 Postgres 平台，展示单个 Tiger Cloud 服务可承载每日 3 万亿指标、3PB 数据和 1 千万亿数据点，并提供新账户 1000 美元信用额度等优惠。

- 🚀 面向任意规模的时间序列工作负载，基于 Postgres 提供 Tiger Cloud 服务。
- 📊 单个 Tiger Cloud 服务的真实规模可达每日 3 万亿指标、3PB 数据、1 千万亿数据点。
- 💳 新账户注册可获得 1000 美元信用额度，有效期 30 天，无需信用卡，仅限新账户。
- 🏭 受到数千家 IoT 公司信赖。
- 📈 核心能力包括：通过最多 10 个节点的副本集分离读写，并使用分层 SSD/S3 实现低成本、近乎无限存储。
- 💰 计算与存储分离，可独立扩展，避免为空闲容量付费并优化性能。
- 🛡️ 高可用：多可用区集群、自动故障转移、时间点恢复和跨区域备份。
- 🔐 企业级能力：SOC 2、HIPAA、GDPR 合规，始终加密、SSO、RBAC 和审计日志。
- 🔍 深度可观测性：查询下钻和仪表盘，并将指标发送至 CloudWatch、Datadog、Prometheus。
- ⚡ 快速启动：数分钟内完成数据库配置，并可通过 SQL、CLI、Terraform、Cursor 或 Claude Code 管理。
- 🔌 可与首选云厂商及更广泛的 Postgres 生态集成。
- 🏢 企业版提供合同化正常运行时间 SLA、区域数据隔离、合规认证和 24/7 全球 Postgres 专家支持。

---

### [BugShot — 一键搞定缺陷报告](https://bug-shot.com/)

**原文标题**: [BugShot — Bug Reporting in One Shot](https://bug-shot.com/)

BugShot 是一款面向 Google Chrome 的免费、免注册 Bug 报告扩展，将发现、修复、捕获和报告 Bug 整合到同一浏览器工作流中，并通过可视化检查、录制回放、AI 草稿、自动上下文与一键提交，减少团队沟通成本和调试时间。

- 🐞 一站式处理：发现、修复、捕获、报告 Bug 均可在浏览器内完成。
- 🧩 免费免注册：从 Chrome 应用商店安装后即可使用，无需注册。
- 🔍 检查与编辑：点击页面元素查看样式和属性，并可在可视化编辑器中实时调整。
- ✨ AI 样式修改：用自然语言描述需求，AI 自动重写 CSS，并支持页面内前后对比。
- 🎥 录制与回放：支持实时录制，或保存最近 30 秒的常开回放，错过问题也能补抓。
- 📝 AI 生成报告：将捕获数据整理为结构化报告，包含步骤、预期行为和实际行为。
- 📋 自动收集上下文：每次报告自动附带浏览器、分辨率和 DOM 信息，减少追问环境配置。
- 🚀 一键提交问题：可将完整附件提交至 Jira、GitHub、Linear、Notion 等工具。
- 🧠 日志查看器：视频可与控制台、网络和操作日志同步回放，便于定位原因。
- 📊 跟踪问题状态：可在 BugShot 内实时查看并更新已提交问题的状态。
- 🔗 使用流程：连接跟踪器、选择捕获模式、编辑样式、AI 生成草稿、提交报告、检查状态。
- 💬 用户反馈积极：QA、设计、后端和前端用户均认为可视化差异、录制、自动日志和 AI 草稿显著提升了协作与调试效率。
- ❓ FAQ 要点：产品免费且无需注册；面向 Chrome；支持 Jira、GitHub、Linear、Notion 等跟踪器；AI 功能的具体要求与数据处理细节原文未展开。

---

### [GitHub - ocavue/astrobook：极简 Storybook 替代方案 · GitHub](https://github.com/ocavue/astrobook)

**原文标题**: [GitHub - ocavue/astrobook: Minimal Storybook alternative · GitHub](https://github.com/ocavue/astrobook)

Astrobook 是一个极简的 UI 组件游乐场，定位为 Storybook 的轻量替代品，支持 React、Vue、Preact、Svelte、Solid、Lit 和 Astro 等多框架，提供统一环境来开发、测试和展示组件；项目采用 MIT 许可证，并提供在线演示和多种集成示例。

- 🧩 支持 React、Vue、Preact、Svelte、Solid、Lit、Astro，多框架组件可在同一环境中开发与展示。
- ⚙️ 快速开始需安装 `astro`、对应框架集成和 `astrobook`，并在 `astro.config.mjs` 中加入 `astrobook()` 集成。
- 🗂️ Astrobook 会扫描所有 `.stories.{ts,tsx,js,jsx,mts,mjs}` 文件，故事文件需包含默认导出和一个或多个命名导出。
- 🧱 兼容 Storybook Component Story Format v3 的有限子集，支持 `args` 和 `decorators` 属性。
- 🎨 装饰器可包裹组件并添加样式，例如 React 绿色边框和 Astro 红色边框；目前仅支持样式调整，不能改变组件上下文或客户端行为。
- 📌 单故事提升：若模块只有一个故事导出且名称与模块名相同，会自动提升，避免侧边栏出现 `Button/Button` 这类冗余嵌套。
- 🔍 `directory` 选项可指定扫描故事的目录，默认是当前工作目录。
- 🌐 `subpath` 选项可将 Astrobook 挂载到现有 Astro 项目的子路径，如 `/playground`，并相对于 Astro 的 `base` 路径。
- 💅 `css` 选项可导入自定义 CSS；`head` 选项可提供自定义 `<head>` 组件；`title` 可设置站点标题。
- 🏠 `home` 可替换默认首页；`homeContent` 可自定义内置首页的标题、副标题、版本徽章和仓库徽章。
- 🚀 可通过 `process.env.NODE_ENV` 仅在开发环境启用 Astrobook，避免生产构建包含它。
- 💬 在 iframe 中运行时，可通过 `postMessage({ type: 'astrobook:set-theme', theme })` 切换明暗主题。
- ⭐ 仓库约 289 stars、18 forks，提供在线演示 `astrobook.pages.dev` 及 TailwindCSS、UnoCSS、PandaCSS、自定义首页等示例。

---

### [Astrobook](https://astrobook.pages.dev/)

**原文标题**: [Astrobook](https://astrobook.pages.dev/)

Astrobook 是一个极简的 UI 组件演练场，当前版本为 v0.13.3，页面提供在 GitHub 上 Star 项目的入口。

- 🧩 Astrobook 定位为极简的 UI 组件 playground（演练场）。
- 🏷️ 当前版本号为 v0.13.3。
- ⭐ 页面包含“Star on GitHub”引导，鼓励用户在 GitHub 上收藏项目。

---

### [Aura — 渐变生成器与制作工具](https://auragradients.vercel.app/)

**原文标题**: [Aura — Gradient Generator & Maker](https://auragradients.vercel.app/)

Aura 是一个持续扩充的氛围渐变集合，利用分层渐变与 CSS 混合模式打造柔和、通透、如光一般的背景，可轻松用于各类界面。

- 🌈 核心技术：通过分层渐变与 CSS blend modes 生成环境光感背景。
- 🎨 产品定位：柔和、有氛围、易嵌入任何 UI。
- 🧭 分类浏览：All、Aura、Mesh、Nebula、Prism、Lattice、Grain、Glass、Flux 等。
- 🖱️ 操作入口：支持 Preview、Customize、Copy Prompt，并提供 Try it out、Browse gradients、Star on GitHub（显示 206）入口。
- 🌅 示例渐变：Sunrise Drift 蓝橙高调、Golden Hour 琥珀到焦赭、Midnight Sapphire 钴蓝到紫墨。
- 🌌 极光与光束：Aurora Nova、Aurora Borealis、Aurora Beams、Midnight Horizon 呈现宇宙、极光与斜向光束效果。
- ✨ 材质与色调：Champagne Fizz、Silver Mist、Arctic Frost、Ember Glow、Dusty Rose 覆盖金色、雾灰、冰蓝、珊瑚与复古玫瑰等风格。

---

### [GitHub - CristianOlivera1/Aura：](https://github.com/CristianOlivera1/Aura)

**原文标题**: [GitHub - CristianOlivera1/Aura: Ambient UI gradients built with layered CSS blend modes. Backgrounds that feel like light. · GitHub](https://github.com/CristianOlivera1/Aura)

Aura 是一个开源的环境 UI 渐变项目，使用分层 CSS 混合模式生成“像光一样的背景”。它提供 200+ 种氛围渐变，并支持在浏览器中实时预览、调整和导出，适合直接用于各类界面设计。项目采用 MIT 许可证，当前获得 529 个 Star 和 36 个 Fork。

- 🌈 **项目定位**：用分层 CSS 混合模式构建氛围感 UI 渐变，让背景呈现柔和的光感效果。
- 🎨 **丰富预设**：内置 200+ 种分层、氛围化渐变，可直接预览并用于界面背景。
- 👀 **实时预览**：悬停卡片即可预览渐变，支持全屏查看、前后切换和键盘快捷键。
- 🌗 **全局光效**：页面会随当前渐变产生光晕效果，并适配浅色与深色主题。
- 🛠️ **浏览器定制**：支持添加、删除、重排图层，调整混合模式、模糊、透明度和基础色。
- 🎞️ **颗粒叠加**：可切换颗粒覆盖层，模拟胶片质感，并支持撤销/重做。
- 📦 **多格式导出**：可复制 CSS、Tailwind、CSS Variables、CSS-in-JS 代码，也可一键复制全部格式。
- 🖼️ **图片下载**：支持将渐变下载为 PNG 或 SVG。
- 🤖 **AI 提示词**：一键复制可直接粘贴到 ChatGPT、Claude 或 Copilot 的提示词，用于在其他项目中重建渐变。
- 🚀 **快速开始**：使用 `pnpm install` 安装依赖，`pnpm dev` 启动开发服务器，访问 `http://localhost:3000`。
- ⚙️ **常用命令**：`pnpm dev` 启动开发、`pnpm build` 生产构建、`pnpm lint` 运行 ESLint。
- 📄 **开源许可**：项目采用 MIT 许可证，欢迎通过 Issue 或 Pull Request 参与贡献。

---

### [面向 Web 应用的 JavaScript 条形码与二维码扫描 SDK](https://strich.io/?ref=frontend-focus)

**原文标题**: [JavaScript Barcode & QR Code Scanner SDK for Web Apps](https://strich.io/?ref=frontend-focus)

STRICH 是一款面向 Web 应用的 JavaScript 条码扫描 SDK，可直接在浏览器中利用设备摄像头实时识别多种 1D/2D 条码，强调客户端本地处理、无需后端、零依赖、易集成，并提供透明订阅定价与企业方案。

- 📷 支持实时扫描 Code 128、EAN/UPC、QR Code、Data Matrix、PDF417、Aztec 等常见一维/二维条码。
- ⚡ 基于 GPU 加速解码管线，完全在设备端运行，单 JS 文件内嵌 WASM，包体小于 1 MB。
- 🧩 零依赖，兼容原生 JS、React、Angular、Vue、Svelte，可通过 NPM 或 CDN 安装。
- 🖥️ 提供开箱即用的 Popup Scanner 弹窗扫描界面，也可嵌入自有布局，并内置取景框、摄像头切换、闪光灯和点击对焦。
- 🛡️ 解码完全本地进行，条码数据不离开设备；可选离线运行附加组件，避免网络流量和供应链风险。
- 🔍 针对真实场景优化，可读取褪色/破损、反光/低光、曲面包装以及反色条码。
- 📱 在真实设备上测试，包括旧款 iPhone、iPad、低端 Android 手机和平板，并持续跟进浏览器和系统更新。
- 💰 Basic 计划 €99/月，最多 10k 次扫描/月；Professional €249/月，最多 100k 次扫描/月；超出为软限制，不阻断扫描。
- 🏢 Business 计划起价 €4,000/年，含 1 个应用，额外应用 €1,500/年/个，支持无限扫描与设备、固定年费。
- 🧾 Enterprise 起价 €7,500/年，支持采购订单、供应商注册、经销商、OEM 授权和定制许可条款。
- 🆓 提供 14 天免费试用，集成通常少于一天；官方称相比免费开源库更适合需要维护和商业支持的场景。
- 🇨🇭 由瑞士 Pixelverse GmbH 开发，是 GS1 Solution Partner，并获得 swiss made software 标签。

---

### [推出 Expo Simulators：专为智能体打造的云端模拟器](https://expo.dev/blog/introducing-expo-simulators-cloud-simulators-built-for-agents?utm_campaign=agentic-development&utm_source=FrontEndFocus&utm_medium=awareness&utm_term=newsletter&utm_content=simulators)

**原文标题**: [Introducing Expo Simulators: cloud simulators built for agents](https://expo.dev/blog/introducing-expo-simulators-cloud-simulators-built-for-agents?utm_campaign=agentic-development&utm_source=FrontEndFocus&utm_medium=awareness&utm_term=newsletter&utm_content=simulators)

概述总结  
- 📄 您尚未提供需要总结的文本内容，因此暂时无法生成要点摘要。请发送文章或内容后，我会按模板整理关键信息并配上合适表情符号。

---

### [2026 年面向开发者的十大最佳 PDF 生成器 API](https://developer-api.foxit.com/developer-blogs/api-guides-tutorials/best-pdf-generator-apis/?utm_source=draftdev&utm_medium=newsletter&utm_campaign=frontendfocus_20261118)

**原文标题**: [10 Best PDF Generator APIs for Developers in 2026](https://developer-api.foxit.com/developer-blogs/api-guides-tutorials/best-pdf-generator-apis/?utm_source=draftdev&utm_medium=newsletter&utm_campaign=frontendfocus_20261118)

本文介绍 2026 年 8 款可替代 Unstructured.io 的文档解析工具，面向从原型迈向生产环境的团队，帮助判断是否需要替换解析器、分块器、连接器，或同时替换三者。

- 📄 文章聚焦 Unstructured.io 的 8 个文档解析替代方案。
- 🔁 从原型迁移到生产环境时，常需替换解析器、分块器、连接器，或三者全部替换。
- 🧰 对比工具包括 Foxit PDF Services API、LlamaParse、Reducto、Docling 等。
- 💰 评估维度涵盖成本、表格处理、分块能力和文件覆盖范围。
- 🗺️ 还提供元素映射、计费计算和切换前测试计划，辅助迁移决策。

---

### [推出空间 CSS：开发者预览 | WebKit](https://webkit.org/blog/18621/introducing-spatial-css-a-developer-preview/)

**原文标题**: [  Introducing spatial CSS: A developer preview | WebKit](https://webkit.org/blog/18621/introducing-spatial-css-a-developer-preview/)

WebKit 在 visionOS 27.3 的 Safari 中推出 spatial CSS API 的有限开发者预览，重点通过 `<model>` 元素在网页中组合、定位和控制 3D 内容，并以声明式 CSS 延续现有 Web 开发模式。

- 🧭 **预览范围**：该功能主要面向 visionOS 27.3 的 Safari，开发者可在“设置 > App > Safari > 高级 > 功能标志 > CSS Portals”中开启。
- 🧱 **核心元素**：`<model>` 元素已在 Safari 27 全平台可用，可独立呈现原生 3D 对象；spatial CSS 进一步支持多个 3D 内容的组合与配置。
- 🌀 **`spatial: portal`**：让 `<div>`、`<figure>` 等容器成为共享 3D 空间，使内部多个模型处于同一 portal 场景中。
- 📐 **空间 transform**：在 portal 内使用标准 `transform` 对模型进行真正的 3D 移动、旋转和缩放，并支持动画与过渡。
- ⚓ **`position-anchor`**：借鉴 CSS 锚点定位，通过 `position-context: anchor` 将模型对齐到另一个模型上的指定锚点，便于拼装家具等 3D 对象。
- 💡 **`@environment-map`**：新增类似 `@keyframes` 的语法，用于定义、复用和管理环境光照，预览支持 360º HDR 图像。
- 🖱️ **`portal-action: orbit`**：允许用户通过旋转场景来环绕查看 3D 内容，未来可能扩展 `pan-x`、`pan-y` 等模式。
- 🪟 **`requestVolumetricScene()`**：可由用户操作触发，将 portal 中的空间内容移出浏览器窗口，在 visionOS 的用户空间中呈现为 Connected Volumetric Scene。
- 🌐 **设计理念**：spatial CSS 通过媒体查询、动画和声明式 CSS 适配不同设备与上下文，减少 JavaScript 状态管理，并支持在手机、平板、电脑和头显等浏览器中设计空间内容。
- 🧪 **反馈与体验**：文章提供演示页面，鼓励开发者在 visionOS 模拟器中体验该预览，并通过 Mastodon、X 或 WebKit Bugzilla 提交反馈。

---

