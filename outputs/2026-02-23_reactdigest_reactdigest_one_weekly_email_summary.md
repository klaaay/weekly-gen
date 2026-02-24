### [React 文摘：电子邮件通讯](https://reactdigest.net/)

**原文标题**: [React Digest: Email Newsletter](https://reactdigest.net/)

《React Digest》是一份面向 React 开发者精心策划的每周通讯，汇集了前端工程师社区精选内容，帮助读者高效学习新知。

- 📬 每周为超过 25,942 名前端工程师推送精选文章与摘要
- ⏱️ 通过人工筛选内容，帮助开发者节省信息检索时间
- 📚 每期包含短摘要推荐文章，助力读者持续掌握行业新知识
- 🌍 订阅者覆盖全球知名科技企业开发团队
- 👍 读者反馈积极，认可其内容实用性与时效性

---

### [虚拟滚动处理数十亿行数据——来自 HighTable 的技术](https://rednegra.net/blog/20260212-virtual-scroll/)

**原文标题**: [Virtual Scrolling for Billions of Rows — Techniques from HighTable](https://rednegra.net/blog/20260212-virtual-scroll/)

本文介绍了 React 组件 HighTable 中用于处理数十亿行数据垂直滚动的五种关键技术，这些技术结合了懒加载、表格切片、无限像素、像素级精确滚动和两步随机访问，以实现高性能和良好的可访问性。

- 🚀 **懒加载技术**：仅加载当前可见的单元格数据，通过异步获取和缓存机制，显著减少内存占用，例如处理 10 亿行数据时仅需加载约 3KB 的可见部分。
- ✂️ **表格切片技术**：只渲染当前可见的行，通过动态调整 HTML 结构和绝对定位，将渲染的 HTML 元素数量从数十亿减少到常数级别（如 30 个），提升性能。
- 🌌 **无限像素技术**：通过设置画布最大高度并降低滚动条分辨率，突破浏览器对元素高度的限制，支持任意数量的行数（如数十亿行），但会牺牲部分滚动精度。
- 🎯 **像素级精确滚动技术**：结合全局和本地两种滚动模式，用户可以通过鼠标滚轮进行精细的本地滚动，或通过拖动滚动条进行全局跳转，确保每个像素都可访问。
- 🎮 **两步随机访问技术**：将垂直和水平滚动逻辑分离，支持通过键盘或程序化方式跳转到任意单元格，并自动滚动到目标位置，同时保持焦点管理，提升用户体验。

---

### [AI 赋能开发者：如何利用 AI 代理构建 RAG 电商网站实现 50% 生产力跃升 - DevCraft](https://www.telerik.com/webinars/devcraft/ai-for-developers-how-to-achieve-a-50-percent-productivity-boost?utm_medium=cpm&utm_source=reactdigest&utm_campaign=dt_ai_productivity_webinar_bitovi)

**原文标题**: [
	AI for Developers: How to Achieve a 50% Productivity Boost Building a RAG-Based E-Commerce Site with AI Agents - DevCraft
](https://www.telerik.com/webinars/devcraft/ai-for-developers-how-to-achieve-a-50-percent-productivity-boost?utm_medium=cpm&utm_source=reactdigest&utm_campaign=dt_ai_productivity_webinar_bitovi)

Telerik 2025 年第四季度发布网络研讨会，聚焦于报告工具和 Fiddler 调试套件的更新，由 Ed Charbeneau 和 Rick Hellwege 主讲，旨在展示新功能和改进。

- 📅 **研讨会时间**：2025 年 12 月 5 日下午 4 点举行
- 🎤 **主讲嘉宾**：Ed Charbeneau 和 Rick Hellwege
- 📊 **报告工具更新**：涵盖 Telerik Reporting 和 Telerik Report Server 的新特性
- 🔧 **调试工具增强**：包括 Fiddler Classic、Fiddler Everywhere 等调试产品的改进
- 🛠️ **开发工具套件**：涉及 DevCraft、Telerik JustMock 等其他相关工具
- 📺 **观看方式**：提供网络研讨会回放，方便按需学习

---

### [React Router 加载器与操作作为集成点 - sergiodxa](https://sergiodxa.com/articles/react-router-loaders-and-actions-as-integration-points)

**原文标题**: [React Router Loaders and Actions as Integration Points by sergiodxa](https://sergiodxa.com/articles/react-router-loaders-and-actions-as-integration-points)

React Router 的加载器和操作应被视为应用集成点，而非独立测试单元。通过测试业务逻辑层（如数据验证、授权、数据库查询等）和编写端到端测试，可以更有效地确保功能正确性，同时避免模拟 HTTP 层的复杂性。

- 🧩 React Router 的加载器和操作设计为集成点，连接 HTTP 层与应用业务逻辑，不建议单独测试
- 🧪 示例展示了如何通过模拟请求、上下文和参数来测试加载器和操作，但复杂依赖（如身份验证、数据库）会使模拟变得困难
- 🔧 更好的方法是测试业务逻辑层，例如独立测试数据模型（如 `User.find` 和 `user.update`）和辅助函数（如验证和授权）
- 📊 通过隔离测试业务逻辑，可以确保加载器和操作的正确性，无需模拟 HTTP 层，使测试更专注且易于维护
- 🌐 对于 HTTP 层集成测试，推荐使用端到端测试工具（如 Playwright）来验证整个应用流程，从请求到响应

---

### [获取失败](https://lukasniessen.medium.com/micro-frontends-when-they-make-sense-and-when-they-dont-a1a06b726065)

**原文标题**: [Failed to retrieve](https://lukasniessen.medium.com/micro-frontends-when-they-make-sense-and-when-they-dont-a1a06b726065)

无法总结：获取内容失败，状态码 403。

---

### [为智能代理未来构建 Next.js | Next.js](https://nextjs.org/blog/agentic-future)

**原文标题**: [Building Next.js for an agentic future | Next.js](https://nextjs.org/blog/agentic-future)

Next.js 团队在过去一年中致力于提升框架的 AI 智能体（agent）体验，通过实验和集成，认识到关键在于从智能体的视角出发，使其能“看见”框架内部状态，从而提供有效的开发支持。

- 🧠 **核心理念转变**：将智能体视为 Next.js 的一等用户，从它们的视角思考信息需求和使用场景，驱动功能改进。
- 🐛 **解决可见性问题**：最初发现智能体无法感知浏览器中的运行时错误和组件状态，通过增强日志转发和错误数据结构化来提升可见性。
- 🧪 **实验性浏览器内智能体**：开发了集成于 Next.js 的 Vector 智能体，支持页面元素选择和代码修改，但因与通用编码工具重叠而停止，但其结构化可见性和框架知识被保留。
- 🔗 **MCP 集成突破**：通过 Model Context Protocol（MCP）暴露 Next.js 内部状态（如路由、渲染段），使智能体能访问开发服务器并获取实时数据，还提供了升级和缓存迁移的工具与提示。
- 📚 **知识嵌入支持**：创建压缩文档索引（agents.md）和结构化工作流（Next.js skills），帮助智能体理解未在训练数据中的框架概念。
- 🔄 **实践改进**：基于智能体需求，增强了服务器操作日志记录和浏览器错误转发，形成了代码、运行时和 AI 之间的紧密调试循环。
- 🚀 **未来方向**：计划通过`npx @next/codemod`简化文档索引生成，扩展评估套件以覆盖更多 API，并最终将智能体上下文支持内置到`next dev`中，实现零配置自动适配。

---

### [构建坚不可摧的 React 组件 - 舒丁](https://shud.in/thoughts/build-bulletproof-react-components)

**原文标题**: [Building Bulletproof React Components - Shu Ding](https://shud.in/thoughts/build-bulletproof-react-components)

构建健壮的 React 组件需要超越常规场景，确保在服务器渲染、并发渲染、异步子组件等复杂环境下依然可靠。关键在于使组件具备服务器兼容性、水合稳定性、多实例支持、并发安全、组合灵活性、门户兼容性、过渡动画支持、活动状态管理、数据防泄漏以及未来兼容性。

- 🛡️ **服务器兼容**：避免在服务器端使用浏览器 API（如 localStorage），应将其移至 useEffect 中执行
- 💧 **水合稳定**：通过内联脚本在浏览器绘制前同步设置初始状态，防止页面闪烁
- 🔢 **多实例支持**：使用 useId 生成唯一标识符，避免多个实例间的 DOM 冲突
- ⚡ **并发安全**：利用 React.cache 对服务器组件的数据请求进行去重，避免重复查询
- 🧩 **组合灵活**：使用 Context 替代 cloneElement 传递数据，兼容服务器组件和异步子组件
- 🪟 **门户兼容**：通过 ownerDocument.defaultView 获取正确的窗口上下文，确保事件监听在 iframe 等环境中正常工作
- 🎬 **过渡动画**：使用 startTransition 包装状态更新，支持视图过渡动画
- 🎭 **活动状态**：通过 useLayoutEffect 动态设置 style 标签的 media 属性，控制隐藏组件的样式影响
- 🔒 **数据防泄漏**：使用 taintUniqueValue 标记敏感数据，防止意外传递给客户端组件
- 🚀 **未来兼容**：优先使用 useState 而非 useMemo 来保证数据持久性，适应 React 未来的优化策略

---

### [精密 AI - 无需编写测试的自动化前端测试](https://www.meticulous.ai/?utm_source=react-digest&utm_medium=newsletter&utm_campaign=26q1&utm_content=secondary)

**原文标题**: [Meticulous AI - Automated Frontend Testing Without Writing Tests](https://www.meticulous.ai/?utm_source=react-digest&utm_medium=newsletter&utm_campaign=26q1&utm_content=secondary)

Meticulous AI 是一款创新的自动化测试工具，通过记录用户与应用的交互并利用 AI 生成持续演进的测试套件，帮助开发者无需编写或维护测试代码即可全面覆盖应用的所有边缘情况和用户流程，从而显著提升开发效率和软件可靠性。

- 🚀 无需编写或维护测试代码，AI 自动生成并更新测试套件，覆盖所有用户流程和边缘情况
- 📹 通过添加脚本标签记录开发、预演和生产环境中的用户交互，生成可视化端到端测试
- 🔄 测试套件随应用演进自动更新，新增功能时自动添加测试，过时测试自动移除
- ⚡ 从 Chromium 底层构建确定性调度引擎，彻底消除测试波动，实现闪电般快速测试
- 🛡️ 通过模拟后端响应实现无副作用测试，无需设置测试账户或模拟数据，避免误报
- 🔗 支持与现有测试套件结合使用或完全替代，轻松集成到 CI/CD 流程中
- 🌐 兼容主流前端框架（如 React、Vue、Angular、Next.js 等），设置简单快捷
- 💼 已被 Dropbox、Notion 等 100 多家组织信任使用，显著提升开发速度和代码可靠性

---

### [CSS 自定义列表深度指南 - Piccalilli](https://piccalil.li/blog/an-in-depth-guide-to-customising-lists-with-css/)

**原文标题**: [
  An in-depth guide to customising lists with CSS - Piccalilli
](https://piccalil.li/blog/an-in-depth-guide-to-customising-lists-with-css/)

本文深入探讨了如何使用 CSS 自定义列表样式，涵盖了从基础样式调整到高级自定义技术的全面指南，包括无序列表和有序列表的样式修改、标记符号的个性化、颜色与字体调整，以及通过伪元素和计数器实现复杂自定义效果的方法。

- 📝 列表应被视为文本的延续部分，使用内边距来缩进列表项，使标记符号整齐排列。
- 🔘 无序列表默认使用实心圆点，可通过`list-style-type`属性更改为圆圈或方块，甚至使用自定义符号、文字或表情符号。
- 🖼️ 使用`list-style-image`属性可以将图像作为列表标记符号，并通过`list-style-position`控制标记符号的位置。
- 🔢 有序列表默认使用十进制数字，可通过`list-style-type`更改为字母或罗马数字等系统，支持多种非拉丁编号系统。
- 🎨 通过`::marker`伪元素可以调整标记符号的颜色和字体属性，但样式应用有限，仅支持颜色和字体相关属性。
- 🛠️ 使用`@counter-style`规则可以定义自定义的编号序列或符号序列，支持跨浏览器使用，提供更灵活的样式控制。
- 📏 通过`li::before`伪元素和计数器函数（如`counter()`和`counters()`）可以实现对标记符号的完全控制，包括位置、大小和样式。
- 🔄 使用 HTML 的`start`、`value`和`reversed`属性可以调整列表的起始值、特定项的值或倒序计数。
- 🌟 结合多种技术（如绝对定位、自定义计数器样式和文本修剪）可以创建复杂的列表样式，如使用 Unicode 符号作为标记符号并调整其对齐和颜色。

---

### [文本换行对齐：美观调整](https://matklad.github.io/2026/02/14/justifying-text-wrap-pretty.html)

**原文标题**: [Justifying text-wrap: pretty](https://matklad.github.io/2026/02/14/justifying-text-wrap-pretty.html)

2025 年 Safari 浏览器率先实现了 text-wrap: pretty 属性，旨在优化网页排版，但该功能与 text-align: justify 结合使用时会导致词间距异常增大，影响美观性。

- 📜 2025 年 Safari 率先实现 text-wrap: pretty 排版优化功能，推动网页排版向传统印刷美学靠拢
- ⚙️ 传统贪婪换行算法长期导致网页排版不美观，而 Knuth-Plass 动态规划算法虽能优化却受限于浏览器动态环境
- 🌐 浏览器需处理动态窗口宽度等复杂因素，使智能换行算法实现难度高于传统印刷排版
- 🔍 text-wrap: pretty 与 text-align: justify 组合使用时，系统性的宽度超调会导致词间距异常增大
- 🐛 当前实现中动态规划算法预设行宽略小于段落宽度，经两端对齐后暴露出间距过大的视觉缺陷
- ✨ 开发者肯定 WebKit 团队的创新贡献，同时呼吁修复这个影响排版美观性的技术细节问题

---

### [宣布互操作性 2026 | WebKit](https://webkit.org/blog/17818/announcing-interop-2026/)

**原文标题**: [  Announcing Interop 2026 | WebKit](https://webkit.org/blog/17818/announcing-interop-2026/)

Interop 2026 是第五年度的跨浏览器互操作性项目，由苹果、谷歌、Igalia、微软和 Mozilla 合作推动，旨在通过统一测试和标准对齐，提升 20 项关键 Web 技术的浏览器间一致性，为开发者提供更可靠的开发基础。

- 🎯 **锚点定位**：延续 2025 年工作，优化元素相对定位的规范与测试可靠性。
- 🎨 **高级 attr()**：扩展 CSS `attr()` 函数至所有属性，支持类型转换，实现 HTML 属性到样式的动态绑定。
- 📦 **容器样式查询**：允许 CSS 根据容器内自定义属性值条件应用样式，增强主题与状态响应能力。
- 🌗 **contrast-color()**：自动选择与指定颜色对比度更高的黑色或白色，简化设计系统配色。
- 🔍 **自定义高亮 API**：通过 JavaScript 和伪元素高亮任意文本范围，无需操作 DOM，适用于搜索高亮和代码编辑器。
- 🪟 **对话框与弹出层增强**：新增 `closedby` 属性、`popover="hint"` 和 `:open` 伪类，提升可访问性与用户体验。
- 📤 **Fetch 上传与范围请求**：支持可读流请求体、增强 FormData 和 Range 头，实现流式上传和部分内容获取。
- 🗃️ **IndexedDB 的 getAllRecords()**：新增批量检索和反向查询方法，提升数据读取性能。
- 🔗 **Wasm 的 JSPI**：让 WebAssembly 同步代码无缝集成 JavaScript 的 Promise API，简化现有应用移植。
- 📽️ **媒体伪类**：提供七种 CSS 伪类（如 `:playing`、`:buffering`），基于媒体播放状态应用样式，减少 JavaScript 依赖。
- 🧭 **导航 API**：改进单页应用导航控制，新增 `precommitHandler` 选项，确保资源加载后再提交导航。
- 🧩 **作用域自定义元素注册**：允许不同部分使用独立的元素注册，解决 Web 组件命名冲突。
- 🎞️ **滚动驱动动画**：通过 CSS 将动画进度与滚动位置绑定，无需 JavaScript 即可创建视差和滚动触发效果。
- 🖱️ **滚动吸附**：优化 CSS Scroll Snap 的跨浏览器一致性，提升轮播等交互体验。
- 🌀 **shape() 函数**：使用路径命令创建复杂响应式裁剪形状，替代多边形和 SVG 路径。
- ✨ **视图过渡**：扩展至跨文档视图过渡，支持页面间平滑动画，提升导航体验。
- 🌐 **Web 兼容性**：针对 ESM 模块加载、滚动事件时序和 `user-select` 等实际问题，提升网站跨浏览器兼容性。
- 📞 **WebRTC**：继续解决实时音视频通信的互操作问题，提高标准一致性。
- 🚀 **WebTransport**：基于 HTTP/3 提供低延迟双向通信，支持数据报和可靠流，适用于游戏和实时协作。
- 🔍 **CSS Zoom**：标准化 `zoom` 属性，确保元素缩放时布局行为一致，区别于纯视觉缩放的 `transform: scale()`。

---

### [获取失败](https://modern-css.com/)

**原文标题**: [Failed to retrieve](https://modern-css.com/)

无法总结：获取内容失败，状态码 403。

---

### [GitHub - knadh/oat：超轻量级、零依赖、语义化HTML、CSS、JS UI 库。压缩后约 8KB。](https://github.com/knadh/oat)

**原文标题**: [GitHub - knadh/oat: Ultra-lightweight, zero dependency, semantic HTML, CSS, JS UI library. ~8KB min+gz.](https://github.com/knadh/oat)

Oat UI 是一个超轻量级、无依赖的语义化 HTML、CSS 和 JavaScript UI 库，旨在通过简洁的代码和语义化标签提供美观的网页组件，避免复杂构建和依赖问题。

- 🏗️ 采用语义化 HTML 标签和属性，无需类名即可实现样式，减少标记污染
- 📦 超轻量设计，压缩后仅约 8KB，包含 CSS 和 JavaScript 文件
- 🔗 零依赖，无需框架或复杂构建流程，引入文件即可使用
- ⚙️ 部分动态组件基于 WebComponents，使用极简 JavaScript 实现
- 🚀 专为厌倦臃肿、依赖繁多和突发变更的 UI 库的开发者设计
- 📄 提供在线演示和文档，当前版本低于 v1，可能存在重大变更
- ⭐ 在 GitHub 上获得 3.6k 星标和 166 个分支，采用 MIT 许可证

---

### [一颗破碎的心 - 艾伦·派克](https://allenpike.com/2026/a-broken-heart/)

**原文标题**: [
    A Broken Heart - Allen Pike
  ](https://allenpike.com/2026/a-broken-heart/)

作者在优化网页仪表板时，发现加载时间从 1 秒激增至 10 秒，最终通过排查发现是 Safari 浏览器在渲染 Noto Color Emoji 字体中的特定表情符号（如❤️）时存在严重性能问题，导致布局计算耗时增加 100 倍。通过调整字体优先级（优先使用 Apple Color Emoji）暂时解决了问题。

- 🐛 网页仪表板加载时间异常增加，从 1 秒延长到 10 秒
- 🔍 初步怀疑 React 性能问题，但优化后未见改善
- 🌐 问题仅在 Safari 浏览器中出现，性能分析显示 94%CPU 时间耗在布局计算上
- ❤️ 最终发现罪魁祸首是“发送反馈”按钮中的心形表情符号
- 🖥️ 根本原因是 Noto Color Emoji 字体在 Safari 中回退使用 SVG 渲染，导致特定表情符号布局耗时激增
- 🛠️ 通过将字体顺序调整为优先使用 Apple Color Emoji 临时解决问题
- 🤖 作者借助 AI 编程助手 Claude 快速定位问题并生成最小复现案例
- ⚠️ 警示：AI 编程工具虽强大高效，但也可能引入意想不到的复杂问题

---

### [编程文摘：电子邮件通讯](https://programmingdigest.net/?utm_source=web-archive&utm_campaign=react)

**原文标题**: [Programming Digest: Email Newsletter](https://programmingdigest.net/?utm_source=web-archive&utm_campaign=react)

《编程文摘》是一份为软件工程师精心筛选的每周通讯，汇集超过 25,318 名专业人士，通过精选文章与摘要帮助读者高效获取有价值内容，每周学习新知。

- 📬 每周为软件工程师推送精选文章与摘要
- 👥 已吸引超过 25,318 名专业人士订阅
- ⏱️ 帮助读者节省筛选优质内容的时间
- 🌱 每期确保读者能学到新知识
- 💬 获得订阅者积极反馈，认可内容实用性
- 🌍 读者群体涵盖全球知名科技企业

---

### [科技领导力：电子邮件通讯](https://leadershipintech.com/?utm_source=web-archive&utm_campaign=react)

**原文标题**: [Leadership in Tech: Email Newsletter](https://leadershipintech.com/?utm_source=web-archive&utm_campaign=react)

《Leadership in Tech》是一份面向技术领域管理者和资深工程师的精选通讯，旨在通过每周推送精选文章，帮助读者提升领导力、节省信息筛选时间并持续学习新知识。

- 📬 面向 CTO、工程经理和资深工程师，助力提升领导力
- 📧 每周一和周四发送，已吸引超过 29,426 名工程领导者订阅
- 🎯 精选文章并附简短摘要，节省读者筛选内容的时间
- 🌱 每周持续提供新知识，涵盖架构讨论、会议规划、沟通技巧等主题
- 👍 读者好评如潮，特别认可其在软件领域领导力内容整合的独到性
- 🏢 由 Bonobo Press 发行，受到众多科技公司领导者关注

---

### [C#文摘：电子邮件通讯](https://csharpdigest.net/?utm_source=web-archive&utm_campaign=react)

**原文标题**: [C# Digest: Email Newsletter](https://csharpdigest.net/?utm_source=web-archive&utm_campaign=react)

C# Digest 是一份面向.NET 开发者的精选周报，旨在通过精选文章和简短摘要，帮助开发者高效获取有价值的技术内容，每周学习新知识。

- 📧 超过20,827名C#工程师订阅的每周电子邮件
- 📖 提供精选文章与简短摘要，节省寻找优质内容的时间
- 🆕 每周学习新知识，涵盖如标准功能标志、LINQ、DiagnosticListener 等实用主题
- 👍 读者反馈积极，包括在工作中应用推荐内容、向同行分享操作结果模式等文章
- 🌍 受到全球.NET 工程师的阅读与认可

---

### [让开发者保持最新动态——Bonobo Press](https://bonobopress.com/)

**原文标题**: [Keeping developers up to date â Bonobo Press](https://bonobopress.com/)

Bonobo Press 是一家自 2013 年起为软件开发者、IT 专业人士和技术人员提供新闻资讯服务的出版商，拥有超过 93,000 名订阅用户，通过简洁高效的新闻简报帮助读者节省时间并获取最新行业动态。

- 📧 提供面向软件开发者、工程经理、技术主管和 CTO 的精选新闻简报，以清晰简洁的内容节省读者时间
- 🎯 提供广告服务，帮助广告主精准触达软件工程师、团队领导、工程经理、CTO 及 IT 决策者等专业受众
- 📞 设有联系渠道，支持用户咨询、建议或广告合作需求

---

### [往期通讯：第一页](https://reactdigest.net/newsletters)

**原文标题**: [Past Newsletters: Page 1](https://reactdigest.net/newsletters)

本期 React Digest 汇总了多期技术通讯，涵盖虚拟滚动、React Router、微前端、AI 集成、性能优化、调试技巧、安全漏洞及测试迁移等前沿主题，旨在为开发者提供全面的 React 生态动态与最佳实践。

- 🚀 探索 React 中处理数十亿行数据的虚拟滚动技术
- 🐛 分享一个因心形表情符号导致应用卡顿的趣味调试案例
- 🤖 分析 AI 在 React 调试中的应用与局限性
- ⚡ 讨论 useOptimistic 钩子的复杂性与适用场景
- 📚 总结 2025 年 React 最佳实践与生态系统趋势
- 🛡️ 回顾 React 安全漏洞教训及服务器组件性能优化
- 🔧 介绍从 Enzyme 迁移至 React Testing Library 的经验
- 🌐 探讨 URL 作为状态管理的优势与多语言应用优化
- 🔄 深入 React 服务器组件的性能影响与序列化技巧
- ⚙️ 解析 React 渲染行为细节与并发 hydration 方案

---

### [隐私](https://reactdigest.net/privacy)

**原文标题**: [Privacy](https://reactdigest.net/privacy)

React Digest 的隐私政策概述了其如何收集、使用和保护用户的个人信息，强调透明度、合法性和用户控制权，并遵守相关数据保护法规。

- 🔍 在收集个人信息前会明确说明用途，仅用于指定或兼容目的，并在必要时征得同意
- 📧 仅收集电子邮件地址用于发送新闻简报，不用于其他目的或垃圾邮件
- 🛡️ 采取合理安全措施保护个人信息，防止丢失、盗窃或未经授权的访问
- 📋 用户有权访问、更正或删除其存储的个人信息，可通过指定邮箱联系操作
- 🚫 严格遵守 COPPA，不收集或存储 13 岁以下儿童的信息
- 📬 提供明确的退订方式，用户可随时取消订阅新闻简报
- ⚖️ 业务运营遵循隐私保护原则，确保个人信息机密性得到维护

---

### [媒体资料包 – 博诺博出版社](https://bonobopress.com/media-kit/)

**原文标题**: [Media Kit â Bonobo Press](https://bonobopress.com/media-kit/)

Bonobo Press 为技术专业人士提供高参与度的新闻简报广告服务，旨在通过精准的受众定位，帮助广告商推广软件工具、产品、职位、会议等，以产生互动、潜在客户和转化。

- 📧 **新闻简报概览**：提供四份面向不同技术角色的新闻简报，包括《Leadership in Tech》、《Programming Digest》、《C# Digest》和《React Digest》，均拥有高打开率和点击率，受众主要来自欧洲和美国。
- 📊 **广告效果数据**：每份简报均提供订阅人数、打开率、点击率、赞助成本、预计广告点击量和每次点击成本等详细指标，例如《Leadership in Tech》的打开率达 57.95%，点击率为 11.38%。
- 🎯 **目标受众**：受众涵盖工程经理、CTO、软件工程师、.NET 开发者、React 前端开发者等，多为决策者或技术专家，就职于 Google、Amazon 等各类公司。
- 💰 **赞助选项**：提供主要和次要广告位，价格因简报而异，如《Leadership in Tech》主要位置每期$2,235，次要位置$1,565。
- 📝 **广告格式**：广告为纯文本形式，包含链接、标题（少于 100 字符）和描述（少于 400 字符），需在发布前 4 天提交。
- 🔄 **订购流程**：包括咨询、排期、发票支付、素材交付、广告上线和效果报告，建议提前数周联系以确保档期。
- 🤝 **合作伙伴案例**：曾与 Okta、GitLab、Datadog 等多个知名品牌合作，许多广告商重复预订赞助。
- 📞 **联系方式**：鼓励广告商通过网站联系，以讨论定制化广告方案，提升潜在客户和转化率。

---

