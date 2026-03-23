### [React 文摘：电子邮件通讯](https://reactdigest.net/)

**原文标题**: [React Digest: Email Newsletter](https://reactdigest.net/)

《React Digest》是一份为 React 开发者精心策划的每周通讯，汇集了前端工程师社区精选内容，旨在帮助开发者高效学习并节省时间。

- 📰 每周为超过 23,936 名前端工程师推送精选文章与摘要
- ⏱️ 帮助开发者节省筛选优质内容的时间
- 📚 每周通过手选文章持续学习新知识
- 🌟 读者反馈称赞其内容实用、更新及时（含并发模式等深度解析）
- 🌍 被全球前端工程师广泛阅读，由 Bonobo Press 运营

---

### [18 个月的代码，付诸东流。我们的教训在此。 | 汤姆·皮亚吉奥](https://tompiagg.io/posts/we-threw-away-1-5-years-of-code)

**原文标题**: [18 Months of Code, Gone. Here's What We Learned. | Tom Piaggio](https://tompiagg.io/posts/we-threw-away-1-5-years-of-code)

经过 18 个月的产品开发与客户签约后，团队决定全面重写代码库，放弃原有技术栈，转向更高效、可维护的架构。

- 🐛 **早期忽视测试导致质量危机**：初期为追求快速上线，采用无测试、非严格 TypeScript 的策略，团队扩张后代码混乱、Bug 频发，甚至导致客户流失。
- 🔄 **技术债务过重选择重写而非重构**：早期为弥补 AI 模型不足构建了复杂封装，如今模型进步使这些代码过时，且旧代码库技术债务沉重，重写更经济。
- 🚫 **弃用 Next.js 和 Server Actions**：Server Actions 存在异步处理困难、难以测试、全局顺序执行、可观测性差、安全风险及错误流控制等问题，开发体验和性能不佳。
- ⚡ **改用 React + tRPC + Hono 提升性能**：新栈将前端编译为静态文件 CDN 分发，后端内存占用低于 100MB，相比 Next.js 实例 8GB 内存大幅优化成本和速度。
- 🔧 **选用 Argo 解决复杂工作流编排**：鉴于需要管理有状态 Kubernetes 任务（如移动设备测试），放弃了 useworkflow 等方案，采用 Kubernetes 原生的 Argo 保证可靠执行与扩展性。

---

### [组件主题编辑器](https://clerk.com/components/theme-editor?utm_source=react-digest&utm_medium=newsletter&utm_campaign=theme-editor&utm_content=03-23-26&dub_id=mF1jv6HPjBbs04yy)

**原文标题**: [Components Theme editor](https://clerk.com/components/theme-editor?utm_source=react-digest&utm_medium=newsletter&utm_campaign=theme-editor&utm_content=03-23-26&dub_id=mF1jv6HPjBbs04yy)

本文介绍了人工智能在医疗领域的应用现状与前景，重点探讨了其在疾病诊断、治疗方案优化及医疗管理效率提升方面的作用，并简要提及了相关的伦理挑战。

- 🏥 AI 辅助诊断系统能通过分析医学影像快速识别病灶，提高早期疾病检出率
- 💊 基于机器学习的个性化治疗方案可结合患者数据优化用药与治疗路径
- ⚙️ 智能医疗管理平台自动化处理行政流程，减轻医护人员行政负担
- 🔬 基因组学与 AI 结合助力精准医疗发展，推动靶向治疗研究
- ⚖️ 数据隐私与算法透明度成为 AI 医疗应用亟待解决的伦理议题

---

### [比皮](https://www.bippy.dev/)

**原文标题**: [bippy](https://www.bippy.dev/)

本文介绍了人工智能在医疗领域的应用现状与前景，重点探讨了其在疾病诊断、治疗方案优化及医疗管理效率提升方面的作用，并简要提及了相关的技术挑战和伦理考量。

- 🤖 AI 辅助诊断系统能通过分析医学影像快速识别病灶，提高早期疾病检出率
- 💊 基于机器学习的个性化治疗方案可结合患者数据优化用药与治疗路径
- 📊 智能医疗管理平台整合临床数据，提升医院运营效率与资源分配合理性
- ⚠️ 数据隐私保护与算法透明度是目前医疗 AI 推广面临的主要伦理挑战
- 🔮 未来 AI 将与医生协同工作，形成“增强智能”的医疗新模式

---

### [React：单例模式并非如你所想的那般邪恶 - DEV 社区](https://dev.to/link2twenty/react-singletons-arent-as-evil-as-you-think-44m8)

**原文标题**: [React: Singletons aren't as evil as you think - DEV Community](https://dev.to/link2twenty/react-singletons-arent-as-evil-as-you-think-44m8)

本文探讨了在 React 中单例模式的实际应用，反驳了其作为“全局状态混乱来源”的常见批评，并通过构建一个 Toast 通知系统的实例，展示了如何利用原生 JavaScript 类与 React 的 useSyncExternalStore 结合，实现简洁、高效且框架无关的状态管理方案。

- 🧩 单例模式在 React 中常被误解为难以测试和追踪的全局状态捷径，但实际上它可以变得轻量、强大且易于实现
- 🔄 传统实现中，组件需通过轮询或手动同步来获取单例数据更新，代码繁琐且易出错
- 🎯 通过扩展 EventTarget 类并利用自定义事件，可以实现单例状态变化时自动通知组件，使代码更清晰可靠
- 🧱 使用 TypeScript 增强类型安全，结合原生类继承（如 TypedEventTarget）减少依赖并提升代码可维护性
- ⚡ 引入 React 的 useSyncExternalStore 钩子，将外部单例状态无缝同步到组件，实现类似原生状态管理的体验
- 🚀 示例中的 Toast 管理器展示了单例如何独立处理定时任务和状态更新，同时保持与 UI 框架的解耦
- 🌉 该架构的突出优势在于单例逻辑纯用 JavaScript 类编写，不依赖 React，便于在微前端或多框架间共享逻辑
- 💡 作者指出，类似模式已被现代库如 TanStack Hotkeys 采用，证明了其在实际生产中的可行性

---

### [理解 React 中的'key'属性 | React 内部解析](https://inside-react.vercel.app/blog/making-sense-of-key-prop-in-react)

**原文标题**: [Making sense of 'key' prop in react | Inside React](https://inside-react.vercel.app/blog/making-sense-of-key-prop-in-react)

React 的 `key` 属性用于在列表渲染中为每个元素提供稳定且唯一的标识，帮助 React 在组件更新时准确识别哪些元素被移动、添加或删除，从而避免不必要的 DOM 操作和状态错乱问题。

- 🔑 **`key` 的作用**：为列表中的每个元素提供唯一标识，使 React 能正确追踪元素的变化，而不是仅依赖位置进行对比。
- 🧩 **无 `key` 的问题**：在列表顺序变化时，React 可能错误地复用组件实例，导致状态错乱（如排序后按钮状态跟随错误元素）。
- 📍 **索引作为 `key` 的局限**：使用数组索引作为 `key` 在列表静态且无内部状态时可行，但若列表顺序变化或元素有状态（如输入框），会导致状态错乱。
- 🎲 **随机值作为 `key` 的危害**：使用 `Math.random()` 等不稳定值会导致每次渲染时 `key` 变化，迫使 React 重新创建所有元素，破坏性能与状态保持。
- ⚙️ **`key` 对组件的影响**：对于非列表的独立组件，通常无需 `key`；但若为组件添加 `key`，React 会将其视为新身份，可能触发重新挂载和状态重置。
- ✅ **正确使用 `key`**：应选择稳定且唯一的标识（如数据 ID），确保 `key` 在渲染间不变，以优化 React 的协调过程并提升性能。

---

### [尖叫架构与共位：让项目结构讲述故事](https://thetshaped.dev/p/screaming-architecture-and-colocation-nodejs-typescript-react)

**原文标题**: [Screaming Architecture & Colocation: Let Your Project Structure Tell the Story](https://thetshaped.dev/p/screaming-architecture-and-colocation-nodejs-typescript-react)

本文介绍了在前后端项目中应用“尖叫架构”与“就近存放”原则的重要性，强调应按照业务功能而非技术角色来组织代码结构，以提升项目的可理解性、可维护性和团队协作效率。

- 🗣️ **尖叫架构**：项目结构应清晰“尖叫”出应用的核心业务（如医疗系统包含`patients/`、`appointments/`等），而非框架细节，从而提升代码可发现性、功能隔离性和团队所有权。
- 📍 **就近存放**：在 React 等前端项目中，将代码（组件、逻辑、类型）尽可能放在使用它的位置附近，避免过早抽象到`utils/`等通用目录，保持高内聚。
- 🧩 **功能优先结构**：结合上述原则，后端按功能模块（如`patients/`）组织，内部包含该功能所需的控制器、服务、路由等文件；前端则在`features/`下按功能组织组件和逻辑，真正共享的代码才放入`shared/`。
- ⚖️ **灵活应用**：分层结构在小型应用、库开发或单人团队中仍可能适用，可采用“顶层功能分组，功能内部分层”的混合模式。
- 🛡️ **边界强制**：通过 ESLint（如`eslint-plugin-boundaries`）或 TypeScript 项目引用等工具，强制模块间的依赖规则，防止架构随时间退化。
- 🚀 **渐进迁移**：建议以功能为单位逐步重构，避免大规模重写，并通过工具固化约定，使架构“隐形”地引导开发者直观找到所需代码。

---

### [精密 AI - 无需编写测试的自动化前端测试](https://www.meticulous.ai/?utm_source=react-digest&utm_medium=newsletter&utm_campaign=26q1&utm_content=secondary)

**原文标题**: [Meticulous AI - Automated Frontend Testing Without Writing Tests](https://www.meticulous.ai/?utm_source=react-digest&utm_medium=newsletter&utm_campaign=26q1&utm_content=secondary)

Meticulous AI 是一款自动化、全面且确定性的测试工具，通过记录用户与应用交互生成持续演进的测试套件，覆盖所有代码分支和用户流程，无需手动编写或维护测试，帮助团队快速、可靠地发布代码。

- 🎯 **自动化测试生成**：通过记录开发、预演和生产环境中的用户交互，自动生成并持续更新端到端测试套件。
- 🌳 **全面覆盖**：追踪每个交互执行的代码分支，确保测试覆盖所有代码行、用户流程和边缘情况。
- 🚀 **无副作用测试**：默认模拟后端响应，避免因数据变化导致的误报，无需设置测试账户或模拟数据。
- ⚡ **快速并行执行**：测试在计算集群上高度并行化，可在 120 秒内完成数千个页面的测试。
- 🔧 **易于集成**：支持主流前端框架（如 React、Vue、Angular），通过添加脚本标签即可快速接入现有开发流程。
- 🛡️ **消除测试波动**：基于 Chromium 构建的确定性调度引擎，从根本上消除测试的不稳定性，提升测试速度。
- 💼 **受企业信赖**：已被 Dropbox、Notion 等超过 100 家组织采用，帮助工程团队提升开发效率与代码质量。

---

### [una.im | 超越黑白对比的 contrast-color() 函数](https://una.im/advanced-contrast-color/)

**原文标题**: [una.im | contrast-color() beyond black & white](https://una.im/advanced-contrast-color/)

本文介绍了 CSS 新特性`contrast-color()`的两种进阶应用方法，该功能能根据背景色自动返回对比度最高的黑色或白色文本颜色，但开发者可通过技术手段实现更丰富的色彩选择。

- 🎨 **方法一：使用`color-mix()`混合色彩**  
  将`contrast-color()`返回的黑/白色与品牌色按比例混合（浅色背景建议 10–25%，深色背景建议 30–40%），在保持可访问性的同时增添色彩个性，需搭配 WCAG 或 APCA 对比度检查工具验证。

- 🧩 **方法二：结合样式查询定制调色板**  
  通过注册自定义属性`--contrast-color`捕获对比色结果，利用`if()`函数或`@container style()`块根据明暗状态切换完整色彩方案，实现对文本颜色的精细控制，但需自行确保色彩组合的对比度达标。

- ⚠️ **注意事项**  
  两种方法均需开发者自行验证色彩对比度，当前浏览器支持存在差异（方法一依赖样式查询，方法二需 Chrome 137+），但核心思路都是将`contrast-color()`作为明暗检测器，为动态主题设计提供基础。

---

### [使用锚定容器查询构建动态切换提示 - Piccalilli](https://piccalil.li/blog/building-dynamic-toggletips-using-anchored-container-queries/)

**原文标题**: [
  Building dynamic toggletips using anchored container queries - Piccalilli
](https://piccalil.li/blog/building-dynamic-toggletips-using-anchored-container-queries/)

本文介绍了如何使用锚定容器查询构建动态切换提示，结合弹出层、锚定定位等现代 CSS 特性实现响应式布局，并逐步增强用户体验。

- 🚀 Chrome 143 引入锚定容器查询，可基于锚定元素的回退位置动态调整样式
- 🎯 使用弹出层（popover）和锚定属性（anchor）语义化标记切换提示，实现渐进增强
- 🛠️ 通过现代 attr() 函数或手动 CSS 设置锚定关联，支持不同浏览器兼容性
- 📐 利用 position-area 和 position-try 属性控制提示框定位，实现自动翻转适应空间
- 🔄 使用 container-type: anchored 查询回退状态，动态调整提示框箭头的方向
- 🎨 结合 corner-shape 属性创建圆滑或三角形箭头，提升视觉体验
- 🌐 通过@supports 检测功能支持，确保在不兼容浏览器中基本功能可用
- 📦 所有代码可渐进增强，新特性成为基线后可简化实现

---

### [NES.css - NES 风格 CSS 框架](https://nostalgic-css.github.io/NES.css/)

**原文标题**: [NES.css - NES-style CSS Framework](https://nostalgic-css.github.io/NES.css/)

NES.css 是一个 8 位像素风格的 CSS 框架，提供组件并支持通过 npm、Yarn 或 CDN 安装，需用户自定义布局，由核心团队及贡献者维护。

- 🎮 框架风格：采用复古 8 位像素（NES 风格）设计
- 📦 安装方式：支持 npm、Yarn 及 CDN 多种安装渠道
- 🧩 功能特性：仅提供 UI 组件，需自行定义页面布局
- 👥 开发团队：由核心团队、荣誉成员及社区贡献者共同维护
- 📰 项目背景：创始文章发表于 2018 年 12 月 GitHub 博客

---

### [49MB 的网页 | thatshubham](https://thatshubham.com/blog/news-audit)

**原文标题**: [The 49MB Web Page | thatshubham](https://thatshubham.com/blog/news-audit)

本文批判了现代新闻网站过度臃肿、追踪用户数据、采用敌对性用户体验设计以追求短期广告收益的现象，并呼吁回归简洁、尊重读者的网页设计。

- 📰 **新闻网站臃肿不堪**：访问《纽约时报》仅查看四个标题就触发了 422 个网络请求，加载了 49MB 数据，页面两分钟后才稳定，相当于下载了整张专辑的音乐文件。
- 🔍 **过度追踪与隐私侵犯**：网站加载时，浏览器被迫处理数十个广告竞价请求，下载大量追踪 JavaScript，并在后台进行用户行为监控，导致 CPU 过载和电池消耗。
- 💰 **敌对性设计的经济驱动**：出版商为了短期广告收益（CPM），牺牲长期读者留存，采用延长页面停留时间的设计策略，将用户挫败感转化为产品。
- 🚫 **用户体验的层层阻碍**：用户常遭遇“Z 轴战争”——GDPR 横幅、订阅弹窗、通知请求等同时出现，必须执行多个关闭操作才能访问实际内容。
- 📱 **移动端的视觉窒息**：粘性头部、广告栏和视频播放器占据大部分屏幕，实际内容仅占视口的极小比例，用户被迫频繁滚动，交互成本高昂。
- 🔄 **布局偏移与阅读干扰**：广告异步加载导致页面布局突然移动（CLS 灾难），破坏用户的空间记忆和阅读流程，增加认知负担。
- 🌱 **简洁替代方案的存在**：如 text.npr.org 等轻量级文本版本和 RSS 订阅证明，用户渴望无干扰、内容优先的浏览体验，市场存在需求。
- 🛠️ **改进建议与呼吁**：建议延迟弹窗触发、预留广告空间避免布局偏移、合并非侵入式提示，并呼吁停止让第三方营销脚本主导网站架构。

---

### [源映射：通过标准发布功能 | 彭博 JS 博客](https://bloomberg.github.io/js-blog/post/standardizing-source-maps/)

**原文标题**: [Source Maps: Shipping Features Through Standards | Bloomberg JS Blog](https://bloomberg.github.io/js-blog/post/standardizing-source-maps/)

Source Maps 是现代 Web 开发的关键工具，用于将编译、压缩后的代码映射回原始源代码，以方便调试。经过多年非标准化发展，其格式在 2024 年正式成为 ECMA-426 标准。文章回顾了 Source Maps 的起源、工作原理、演进历程，并介绍了新标准下的未来特性规划。

- 🗺️ **起源与作用**：Source Maps 源于 Google Closure Tools，用于解决代码优化后调试困难的问题，将生成代码映射回源代码。
- 📜 **格式演进**：最初无官方标准，依赖共享文档；2011 年发布的 Revision 3 成为现代基础，通过 Base64 VLQ 编码大幅减小文件体积。
- 🔧 **核心结构**：Source Map 是 JSON 文件，包含版本、源文件列表、映射数据等字段，其中 `mappings` 字段存储编码后的位置映射信息。
- 🤝 **标准化进程**：2023 年成立 TC39-TG4 任务组，汇集多方代表，于 2024 年正式发布 ECMA-426 标准，为功能演进奠定基础。
- 🚀 **未来特性**：新标准下正开发“作用域映射”和“范围映射”等高级功能，旨在提升调试精度，支持复杂编译场景。
- 🌍 **社区协作**：强调开源生态合作的重要性，鼓励工具开发者参与标准制定，共同改善 JavaScript 开发体验。

---

### [TypeScript 6.0 RC 版本发布公告](https://devblogs.microsoft.com/typescript/announcing-typescript-6-0-rc/)

**原文标题**: [Announcing TypeScript 6.0 RC - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-6-0-rc/)

TypeScript 6.0 RC 已发布，这是基于当前 JavaScript 代码库的最后一个主要版本，旨在为使用 Go 重写的原生 TypeScript 7.0 铺平道路。此版本包含多项新特性、改进以及为迎接 7.0 所做的重大变更和弃用，标志着向现代开发实践的过渡。

- 🚀 **发布候选版本**：TypeScript 6.0 RC 现已可用，可通过 `npm install -D typescript@rc` 安装，它是通往原生 TypeScript 7.0 的桥梁版本。
- 🧠 **改进类型推断**：对于未使用 `this` 的函数，减少了其上下文敏感性，从而在泛型调用中实现了更佳的类型推断，特别是在方法语法中。
- 🗂️ **支持 `#/` 子路径导入**：现在支持以 `#/` 开头的子路径导入，与 Node.js 20+ 保持一致，简化了项目内部的模块映射。
- ⚙️ **模块解析组合**：现在允许将 `--moduleResolution bundler` 与 `--module commonjs` 组合使用，为许多项目提供了合适的升级路径。
- 🔢 **稳定类型排序标志**：引入了 `--stableTypeOrdering` 标志，使 TypeScript 6.0 的类型排序行为与 7.0 保持一致，有助于减少版本间差异的噪音，但可能会带来性能开销。
- 📅 **新增 `es2025` 编译目标**：增加了 `es2025` 作为 `target` 和 `lib` 的新选项，包含了新的内置 API 类型。
- ⏳ **内置 Temporal API 类型**：为已达到 Stage 3 的 Temporal 日期/时间 API 提供了内置类型支持，可通过 `esnext` 或 `esnext.temporal` 使用。
- 🗺️ **新增 Map 的 "upsert" 方法类型**：为 `Map` 和 `WeakMap` 新增的 `getOrInsert` 和 `getOrInsertComputed` 方法提供了类型支持，简化了常见的"检查 - 插入"模式。
- 🛡️ **新增 `RegExp.escape` 类型**：为新的 `RegExp.escape` 函数提供了类型支持，用于安全地转义正则表达式中的特殊字符。
- 🌐 **DOM 库包含可迭代类型**：`dom` 库现在默认包含了 `dom.iterable` 和 `dom.asynciterable` 的内容，简化了配置。
- ⚠️ **重大变更与弃用**：作为过渡版本，6.0 引入了多项重大变更和弃用以迎接 7.0，包括默认启用 `strict` 模式、`module` 默认为 `esnext`、`target` 默认为最新 ES 版本、`types` 默认为空数组、弃用 `target: es5`、`--moduleResolution node`、`--baseUrl`、`--outFile` 等。建议使用 `"ignoreDeprecations": "6.0"` 暂时忽略警告，但这些选项将在 7.0 中完全移除。
- 🛠️ **为 7.0 做准备**：TypeScript 6.0 的核心目标是帮助开发者平稳过渡到即将发布的、性能大幅提升的原生 TypeScript 7.0。团队鼓励用户尝试 RC 版本并提供反馈。

---

### [Vite 8.0 正式发布！ | Vite](https://vite.dev/blog/announcing-vite8)

**原文标题**: [Vite 8.0 is out! | Vite](https://vite.dev/blog/announcing-vite8)

Vite 8.0 正式发布，采用 Rust 编写的 Rolldown 作为统一打包工具，带来高达 10-30 倍的构建速度提升，同时保持完整的插件兼容性。此次更新还包括插件目录 registry.vite.dev 的推出、多项新功能增强，以及对社区贡献的感谢。

- 🚀 **性能飞跃**：Vite 8 集成 Rolldown 作为单一 Rust 打包工具，构建速度提升 10-30 倍，同时完全兼容现有 Vite 和 Rollup 插件。
- 🌐 **插件生态**：推出 registry.vite.dev 插件目录，方便开发者搜索和管理 Vite、Rolldown 及 Rollup 插件。
- ⚙️ **功能增强**：新增内置开发工具、TypeScript 路径别名支持、装饰器元数据支持、Wasm SSR 支持及浏览器控制台转发等功能。
- 📈 **实际成效**：多家公司实测构建时间大幅减少，如 Linear 从 46 秒降至 6 秒，Beehiiv 减少 64%。
- 🔄 **平滑迁移**：提供兼容层自动转换配置，建议复杂项目先通过 rolldown-vite 包逐步迁移至 Vite 8。
- 📦 **安装体积**：由于集成 lightningcss 和 Rolldown，安装包增加约 15 MB，团队将持续优化。
- 🙏 **社区致谢**：感谢 Rollup 和 esbuild 的历史贡献，以及社区在测试和反馈中的关键作用。

---

### [基于特性的 React 架构 - Robin Wieruch](https://www.robinwieruch.de/react-components-database-relations/)

**原文标题**: [Feature-Based React Architecture - Robin Wieruch](https://www.robinwieruch.de/react-components-database-relations/)

本文探讨了在 React 全栈应用中，如何通过功能导向的架构设计，使数据库关系与 React 组件结构相协调，避免因数据嵌套关系导致代码复杂化。

- 🏗️ 在 React 服务器组件和服务器动作的驱动下，UI 与数据库的交互更直接，但大型应用中仍需通过领域层和数据访问层等中间层进行连接。
- 🔗 数据库中的表关系（如博客应用中的用户、文章和评论表）直接影响 React 组件的设计，组件组合成为连接数据库与 UI 的理想桥梁。
- 🧩 通过将文章组件拆分为专注于文章内容与评论的两个独立组件，遵循功能单一原则，有助于实现清晰的功能文件夹结构。
- 📊 在数据获取函数中，将获取文章与获取评论的功能分离，避免随着代码库增长出现嵌套关系的无限组合（如`getPostWithComments`），保持代码的专注性与可维护性。

---

### [编程文摘：电子邮件通讯](https://programmingdigest.net/?utm_source=web-archive&utm_campaign=react)

**原文标题**: [Programming Digest: Email Newsletter](https://programmingdigest.net/?utm_source=web-archive&utm_campaign=react)

《编程文摘》是一份为软件工程师精心筛选的每周通讯，汇集高质量文章，帮助读者节省时间并持续学习新知识。

- 📬 超过 25,011 名软件工程师订阅这份每周电子邮件
- 🎯 每期推送附简短摘要的精选文章，节省寻找优质内容的时间
- 🧠 每周帮助读者学习新知识，获得订阅者积极反馈
- 🌍 读者群体涵盖全球知名科技企业与机构
- 📅 由 Bonobo Press 自 2013 年持续运营至今

---

### [科技领导力：电子邮件通讯](https://leadershipintech.com/?utm_source=web-archive&utm_campaign=react)

**原文标题**: [Leadership in Tech: Email Newsletter](https://leadershipintech.com/?utm_source=web-archive&utm_campaign=react)

《Leadership in Tech》是一份专为技术领导者设计的精选通讯，旨在通过每周精选文章，帮助 CTO、工程经理和高级工程师提升领导力技能，节省信息筛选时间，并持续学习行业新知。

- 📧 每周两期邮件，覆盖超过 29,412 名工程领导者  
- 🎯 内容专为 CTO、工程经理和高级工程师精选，聚焦领导力提升  
- 📚 提供文章摘要，节省读者筛选内容的时间  
- 🌱 每周更新，确保读者持续学习新知识  
- 💬 读者好评：认可其在软件领域领导力内容的独特汇编价值  
- 🏢 发行方为 Bonobo Press，服务自 2013 年持续运营

---

### [C#文摘：电子邮件通讯](https://csharpdigest.net/?utm_source=web-archive&utm_campaign=react)

**原文标题**: [C# Digest: Email Newsletter](https://csharpdigest.net/?utm_source=web-archive&utm_campaign=react)

《C# Digest》是一份专为.NET 开发者精心策划的每周通讯，汇集精选文章与简短摘要，帮助超过 20,567 名工程师高效获取有价值内容，每周学习新知识。

- 📰 每周为.NET 开发者推送精选文章与摘要
- 👥 已吸引超过20,567名C#工程师订阅
- ⏱️ 帮助开发者节省筛选内容的时间
- 🌱 每周持续学习新技术与工具
- 💬 读者反馈积极，内容可直接应用于工作场景
- 🌍 受到全球.NET 工程师群体的广泛阅读

---

### [让开发者保持最新动态——Bonobo Press](https://bonobopress.com/)

**原文标题**: [Keeping developers up to date â Bonobo Press](https://bonobopress.com/)

Bonobo Press 是一家自 2013 年起为超过 80,000 名软件开发者、IT 专业人士和技术人员提供最新资讯的媒体公司，通过简洁高效的新闻通讯服务，帮助技术从业者节省时间并保持行业前沿信息的更新。

- 📰 提供面向软件开发者、工程经理、技术主管和 CTO 的精选新闻通讯，以清晰简洁的内容节省读者时间
- 🎯 为广告商提供触及技术细分受众的机会，包括软件工程师、团队领导、工程经理、CTO 及 IT 决策者
- 📞 设有联系渠道，支持业务咨询、建议反馈及广告合作需求
- 📅 自 2013 年持续运营，服务延续至 2026 年，并附有相关服务条款说明

---

### [过往通讯：第一页](https://reactdigest.net/newsletters)

**原文标题**: [Past Newsletters: Page 1](https://reactdigest.net/newsletters)

《React Digest》是一份专注于 React 生态的技术简报，涵盖性能优化、最佳实践、新特性及漏洞分析等内容。

- 🛠️ 重建 18 个月代码的经验揭示了未经测试代码库对用户的危害，同时介绍了无需修改代码即可访问 React Fiber 树的工具 Bippy
- 🔄 探讨了基于特性的 React 架构，解释了 React 状态更新的异步特性及 AsyncLocalStorage 在上下文传递中的应用
- 🧠 前端内存泄漏影响 86% 项目，研究显示常见泄漏模式来自定时器和事件监听器未清理
- ⚡ 虚拟滚动技术支持数十亿行数据渲染，同时探讨了微前端架构和 Next.js 的 AI 增强功能
- 🐛 包含非常规调试案例（如表情符号导致性能下降）及 AI 辅助 React 调试的实践分析
- ⚠️ 多次讨论 React 与 Next.js 的安全漏洞，强调及时更新和遵循最佳实践的重要性
- 📚 持续分享 React 最佳实践，包括状态管理、性能优化、测试迁移（Enzyme 转 Testing Library）等主题
- 🆕 跟踪 React 新版本特性（如 19.2 版的 INP 优化）和生态演进（服务器组件、Turbopack 编译器等）
- 🔗 探讨 URL 作为状态管理的实践，以及多语言应用、原子状态等高级开发模式
- 🎯 包含年度精选文章汇总、开发者学习指南及会议（React Conf）最新动态

---

### [隐私](https://reactdigest.net/privacy)

**原文标题**: [Privacy](https://reactdigest.net/privacy)

本隐私政策概述了 React Digest 如何收集、使用和保护用户的个人信息，特别强调仅收集电子邮件地址用于发送新闻简报，并严格遵守数据保护法规，确保用户隐私安全。

- 🔍 在收集个人信息前会明确告知收集目的
- 🎯 仅为实现指定目的或经用户同意/法律要求使用个人信息
- ⏳ 仅在必要时保留个人信息
- ⚖️ 通过合法公平方式并在适当时征得同意收集信息
- 📊 确保个人数据相关、准确、完整且及时更新
- 🛡️ 采取合理安全措施防止信息丢失、被盗或未经授权访问
- 📋 向用户公开个人信息管理政策与实践
- 📧 仅收集电子邮件地址用于发送新闻简报
- 🚫 不收集或存储 13 岁以下儿童信息
- 📬 用户可联系特定邮箱获取或删除存储的个人信息
- 📭 提供新闻简报退订链接，反对垃圾邮件

---

### [媒体资料包 – Bonobo Press](https://bonobopress.com/media-kit/)

**原文标题**: [Media Kit â Bonobo Press](https://bonobopress.com/media-kit/)

Bonobo Press 为技术专业人士提供精心策划的新闻简报，旨在帮助广告商精准触达软件开发者、技术领导等目标受众，通过高参与度的内容推动互动、潜在客户和转化。

- 📧 **新闻简报与统计数据**：提供四份专注于不同技术领域的新闻简报，包括《Leadership in Tech》、《Programming Digest》、《C# Digest》和《React Digest》，每份简报均拥有高订阅数、打开率和点击率，并详细列出赞助成本和受众特征。
- 🎯 **目标受众与覆盖范围**：受众主要为欧洲和美国的软件工程师、技术领导及决策者，涵盖从初创公司到大型企业（如 Google、Amazon）的多种行业，确保广告能精准触达潜在客户。
- 💰 **费率卡与广告格式**：提供清晰的赞助价格、预计广告点击量和每次点击成本，广告格式为纯文本，需包含链接、标题和描述，强调文本内容能带来最高参与度。
- 📋 **订购流程与合作伙伴**：从咨询到广告上线的步骤包括产品介绍、时间安排、发票支付、内容优化和效果报告，并展示了过去合作伙伴（如 Okta、GitLab、MongoDB）的成功案例，许多广告商重复预订。
- 🤝 **联系与合作**：鼓励广告商提前联系以确保广告位，提供定制化建议，旨在通过高参与度的新闻简报帮助提升品牌曝光、获取潜在客户并实现业务增长。

---

