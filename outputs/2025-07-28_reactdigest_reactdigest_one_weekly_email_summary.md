### [React 文摘：电子邮件通讯](https://reactdigest.net/)

**原文标题**: [React Digest: Email Newsletter](https://reactdigest.net/)

《React Digest》是一份专为 React 开发者精心策划的每周通讯，汇集了精选文章和简短摘要，帮助开发者节省时间并每周学习新知识。  

- 📰 每周一封邮件，为 22,306 多名前端软件工程师提供精选内容  
- 🔍 阅读经过筛选的文章，附带简短摘要  
- ⏱️ 节省寻找有价值内容的时间  
- 🌱 每周学习新知识  
- 💬 读者反馈：内容实用、信息更新及时，特别提到关于 React 并发模式的文章很有帮助  
- 🌍 来自全球前端工程师的阅读与认可  
- ©️ 由 Bonobo Press 发布，涵盖 2013-2025 年

---

### [介绍 Zustand（状态管理）—— Frontend Masters 博客](https://frontendmasters.com/blog/introducing-zustand/)

**原文标题**: [Introducing Zustand (State Management) – Frontend Masters Blog](https://frontendmasters.com/blog/introducing-zustand/)

概述总结  
Zustand 是一个简洁但功能强大的状态管理库，适用于 React 应用。它通过减少样板代码和优化渲染性能，提供了比 React Context 更高效的解决方案。  

- 🚀 **Zustand 简介**：Zustand 是一个已有 5 年历史的状态管理库，以其简洁和高效著称。  
- 🛠️ **快速上手**：通过一个任务管理应用示例，展示了 Zustand 的基本用法和性能优势。  
- 🔄 **状态更新**：使用`set`函数轻松更新状态，支持部分更新和完全覆盖。  
- 📖 **正确读取状态**：推荐使用选择器函数或`useShallow`钩子来优化组件渲染，避免不必要的重绘。  
- 🌐 **异步支持**：Zustand 天然支持异步操作，可以在异步函数中调用`set`更新状态。  
- 🔍 **状态读取**：支持在组件内外读取状态，包括通过`getState`方法在非 React 环境中使用。  
- 📚 **扩展功能**：支持手动订阅、与 Immer 等不可变库集成，适合复杂应用场景。  
- 💡 **性能优势**：相比 React Context，Zustand 能显著减少不必要的组件重渲染，提升应用性能。  
- 🤔 **社区反馈**：文章评论区讨论了 Zustand 与 Redux、Context 的对比，以及其在 SSR 中的应用问题。  

Zustand 以其简洁性和高性能，成为 React 状态管理的优选方案之一。

---

### [一丝不苟](https://www.meticulous.ai/?utm_source=react_digest)

**原文标题**: [Meticulous](https://www.meticulous.ai/?utm_source=react_digest)

Meticulous AI 是一个创新的测试工具，通过 AI 自动生成和维护测试套件，无需手动编写或维护测试用例，帮助开发者高效覆盖应用的所有边缘情况，提升代码质量和开发速度。

- 🚀 **无需编写测试** - Meticulous AI 自动生成并维护测试套件，覆盖所有用户流程和边缘情况。  
- 🛠️ **无缝集成** - 通过添加脚本标签，轻松在开发、预发布和生产环境中记录会话。  
- ⚡ **高效测试** - 测试高度并行化，可在 120 秒内完成数千次测试。  
- 🔄 **自动更新** - 测试套件随应用演进自动更新，无需人工干预。  
- 🛡️ **零误报** - 通过模拟后端响应，避免因数据变化导致的误报，无需额外设置测试账户。  
- 📈 **提升开发速度** - 帮助团队快速迭代，确保代码无回归问题。  
- 🌟 **客户认可** - 被 Dropbox、Notion 等 100 多家组织信任，显著提升开发效率和代码质量。  
- 🔧 **多框架支持** - 支持 NextJS、React、Vue、Angular、Nuxt 和 SvelteKit 等多种前端框架。  
- 🔗 **灵活使用** - 可作为现有测试套件的补充或完全替代。

---

### [使用 React 构建可拖放的看板 - DEV 社区](https://dev.to/surajondev/building-a-kanban-board-with-drag-and-drop-in-react-2pop)

**原文标题**: [Building a Kanban Board with Drag and Drop in React - DEV Community](https://dev.to/surajondev/building-a-kanban-board-with-drag-and-drop-in-react-2pop)

概述：本文介绍了如何使用 React 和 Dnd-Kit 库构建一个具有拖放功能的看板（Kanban Board），并详细讲解了项目设置、核心代码实现以及功能演示。

- 🚀 文章介绍了如何使用 React 和 Dnd-Kit 库构建一个具有拖放功能的看板（Kanban Board）。
- 🔧 项目需要基本的 JavaScript、React 和 TailwindCSS 知识，并使用 NextJS 框架进行搭建。
- 📦 使用了@dnd-kit/core 库实现拖放功能，sonner 库用于显示提示消息。
- 🏗️ Dnd-Kit 库分为四个主要部分：DndContext、Sensors、Droppable 和 Draggable。
- 💻 提供了 Draggable 和 Droppable 组件的代码示例，并详细讲解了其实现原理。
- 🖱️ 通过 PointerSensor 和 KeyboardSensor 支持鼠标和键盘的拖放操作。
- 🔄 实现了 handleDragStart 和 handleDragEnd 函数，用于处理拖放开始和结束时的逻辑。
- 📊 使用虚拟数据模拟后端数据，并展示了如何动态更新任务状态。
- 🎨 通过 TailwindCSS 实现了看板的 UI 设计，包括任务卡片和列样式。
- 🌐 提供了 CodeSandbox 链接，展示了完整的代码和功能演示。
- 📝 文章最后总结了如何将拖放功能应用到实际项目中，并提供了作者的社交媒体链接。

---

### [React 中单页应用的现状与未来 | Felipe Gustavo 的博客](https://www.felgus.dev/blog/future-spa)

**原文标题**: [The present and the future of SPAs in React | Felipe Gustavo's Blog](https://www.felgus.dev/blog/future-spa)

React 生态中关于 SPA（单页应用）的现状与未来探讨，涉及服务器渲染、并发模式及新特性的应用。

- 🚀 **当前模式**：传统 SPA 采用“渲染时获取”模式，存在瀑布流问题，而“渲染即获取”模式能提前调用路由加载器，优化用户体验。
- 🔄 **服务器组件**：即使无服务器，也可在构建阶段生成 React 服务器组件（RSC），为经典 SPA 提供静态组件支持。
- ⚡ **并发特性**：React 18 的`useTransition`和`useDeferred`允许设置 UI 更新优先级，提升界面流畅度，适用于各种规模应用。
- 🔗 **预加载策略**：利用路由器的`Link`组件动态预加载路由数据，减少延迟，加快页面渲染。
- 🛠️ **React 实验室创新**：引入`ViewTransition`实现流畅页面过渡动画，`Activity`组件支持预渲染，节省关键毫秒，提升交互体验。

---

### [React 图形可视化指南：库选择、最佳实践与实现](https://cambridge-intelligence.com/react-graph-visualization-library/)

**原文标题**: [
		React Graph Visualization Guide: Libraries, Best Practices & Implementation	](https://cambridge-intelligence.com/react-graph-visualization-library/)

React 图形可视化工具包因其与现有技术栈的无缝集成和强大的数据可视化能力，成为开发者的首选。以下是关键点总结：

- 🚀 **React 图形可视化概述**：利用 React 构建动态、交互式的节点 - 链接图，适用于复杂网络的可视化，如网络安全资产图、客户 360 档案等。  
- 🔧 **技术优势**：React 的声明式编程和虚拟 DOM 实现高效更新，支持实时数据流和复杂条件样式，提升用户体验和可维护性。  
- 🏢 **行业应用**：  
  - 🔒 **网络安全**：集成 React 仪表盘，实时分析设备关系和警报模式，支持自定义过滤和钻取工作流。  
  - 🕵️ **情报与执法**：动态更新证据数据，创建可复用的调查模板，并嵌入交互式报告仪表盘。  
  - 💰 **金融服务与反欺诈**：同步实时交易数据，高亮异常行为，构建可复用的风险指标组件。  
- 🌐 **其他场景**：AI 决策解释、IoT 设备管理及网络拓扑可视化。  
- 📊 **构建要点**：  
  - 选择合适工具（开源库、商业 SDK 如 ReGraph）。  
  - 设计节点/边数据结构，结合布局与交互模型，利用 React 的状态管理实现动态更新。  
- 📂 **数据结构建议**：使用 JSON 格式定义节点 ID、标签、样式及元数据，边需包含源/目标和关系类型。  
- 📚 **推荐工具**：  
  - **商业 SDK**：ReGraph（高性能、企业级支持）。  
  - **开源选项**：Cytoscape.js（需 React 封装）、React Flow（适合低代码工作流）。  
- 🔄 **替代方案**：  
  - **JavaScript 库**：KeyLines（传统编码风格）、D3.js（高灵活性但复杂）。  
  - **专用平台**：Neo4j Bloom（限于 Neo4j 生态）、Gephi（静态分析工具）。  
- 🎯 **行动建议**：通过 ReGraph 试用体验高性能 React 图形可视化，适用于威胁映射、欺诈调查等场景。

---

### [如何在 React Router 中使用 Action Routes - sergiodxa](https://sergiodxa.com/tutorials/use-action-routes-in-react-router)

**原文标题**: [How to Use Action Routes in React Router by sergiodxa](https://sergiodxa.com/tutorials/use-action-routes-in-react-router)

React Router 中的 Action Routes 模式用于集中处理资源操作（如创建、更新、删除），通过单一文件定义服务端和客户端逻辑，提升代码复用性和可维护性。

- 🛠 **Action Routes 简介**  
  通过 Resource Routes 处理特定操作，集中逻辑于单个文件，支持服务端和客户端操作。

- 📂 **配置 Action Routes**  
  创建 `routes/actions` 文件夹，按 `名词-动词.ts` 命名（如 `post-create.ts`），并通过 `prefix` 将路由前缀设为 `/actions`。

- 🔄 **服务端操作与验证**  
  使用 Zod 验证输入数据，结合身份检查（如 `authenticate`）和状态码工具（如 `created`、`badRequest`）返回类型化响应。

- 🎯 **客户端副作用处理**  
  通过 `clientAction` 处理成功/失败后的 UI 反馈（如显示 Toast 或重定向），复用服务端操作结果。

- 🌍 **国际化支持**  
  在操作中直接集成 i18n，返回本地化的错误或成功消息。

- 🔐 **权限控制**  
  依赖中间件处理身份验证，在操作内实现细粒度授权（如订阅检查），返回 `forbidden` 等状态码。

- 🏗 **设计优势**  
  减少重复逻辑，提升可测试性，长期维护更灵活。适用于多路由触发同一操作的场景。

- 📌 **命名建议**  
  推荐扁平化路由结构（如 `post-create.ts`），便于管理和理解。

---

### [:has() CSS 伪类 | 动手实践](https://gomakethings.com/the-has-css-pseudo-class/)

**原文标题**: [The :has() CSS pseudo-class | Go Make Things](https://gomakethings.com/the-has-css-pseudo-class/)

2025 年 7 月 22 日关于 CSS 伪类`:has()`的介绍，作者在 Kelp UI 库中实践了这一新特性，探讨了其功能和应用场景。

- 🎨 **父元素条件样式**：`:has()`允许根据子元素或相邻兄弟元素的存在来样式化父元素，例如`.wizard:has(> .merlin)`会选中包含`.merlin`子元素的`.wizard`。
- 🔗 **兄弟元素检测**：传统 CSS 只能通过`+`选择相邻兄弟，而`:has()`可逆向检测元素是否拥有兄弟，如`.wizard:has(+ .wizard)`为含后续兄弟的巫师添加底部边框。
- 🛠️ **实际应用案例**：在 Kelp 中，作者用`:has()`为折叠组添加细节元素间的分隔线，或触发带`[trigger]`属性的输入框对应标签的样式。
- 💡 **语法直观性**：CSS 的`:has()`写法贴近自然语言表达，如“如果某元素有某子元素，则应用样式”。
- 🌟 **现代 CSS 优势**：文章强调类似`:has()`的特性让 CSS 更强大，简化了以往需复杂 hack 才能实现的布局需求。

---

### [设计滚动行为：何时保存用户位置 - NN/g](https://www.nngroup.com/articles/saving-scroll-position/)

**原文标题**: [Designing Scroll Behavior: When to Save a User’s Place - NN/g](https://www.nngroup.com/articles/saving-scroll-position/)

文章概述：  
探讨了在设计滚动行为时保存用户位置的重要性，以及在不同情境下是否应保留滚动位置的权衡。通过实际案例和用户研究，分析了保存滚动位置的优缺点，并提出了具体的设计建议。

- 📜 保存滚动位置能减少用户交互成本，尤其在长列表浏览（如电商、新闻聚合）中，避免用户返回时重新定位。  
- 🔄 例外情况：内容频繁更新（如实时新闻、体育赛事）时，重置滚动位置可确保用户看到最新信息。  
- ⏳ 长时间未操作后（如超过 30-60 分钟），重置滚动位置更合理，避免用户因遗忘上下文而困惑。  
- 🤔 当用户意图不明确时，默认保存滚动位置并提供快捷重置选项（如“跳至最新消息”按钮）是低干扰方案。  
- 🎯 滚动行为设计需结合具体场景，细微差别可能显著影响用户体验效率。  
- 📱 案例：Spotify 未保存播客列表滚动位置导致用户重复操作；ChatGPT 未保留聊天记录位置增加了操作摩擦。

---

### [SVG 友好入门指南 • 乔希·W·科莫](https://www.joshwcomeau.com/svg/friendly-introduction-to-svg/)

**原文标题**: [A Friendly Introduction to SVG • Josh W. Comeau](https://www.joshwcomeau.com/svg/friendly-introduction-to-svg/)

SVG（可缩放矢量图形）是一种基于 XML 的图像格式，适用于网页开发，支持动态修改和动画效果。

- 🎨 SVG 是一种基于 XML 的矢量图像格式，可以直接嵌入 HTML 中，并通过 CSS 和 JavaScript 进行动态修改。
- 🖌️ SVG 提供多种基本图形元素，如线条（`<line>`）、矩形（`<rect>`）、圆形（`<circle>`）、椭圆（`<ellipse>`）和多边形（`<polygon>`）。
- 📏 SVG 的`viewBox`属性允许定义内部坐标系，使图形在不同尺寸下保持比例和清晰度。
- ✏️ 描边（`stroke`）属性可以设置颜色、宽度、虚线样式（`stroke-dasharray`）和线帽样式（`stroke-linecap`），并支持 CSS 动画。
- 🌀 通过`stroke-dashoffset`属性，可以实现描边动画效果，如绘制效果或旋转加载动画。
- 📐 `<path>`元素支持复杂路径绘制，如贝塞尔曲线和椭圆弧，适合创建更复杂的图形。
- 🚀 SVG 的矢量特性使其在任何缩放比例下都能保持清晰，适合响应式设计和动态图形需求。

---

### [处理带参数的 JavaScript 事件监听器——Smashing Magazine](https://www.smashingmagazine.com/2025/07/handling-javascript-event-listeners-parameters/)

**原文标题**: [Handling JavaScript Event Listeners With Parameters — Smashing Magazine](https://www.smashingmagazine.com/2025/07/handling-javascript-event-listeners-parameters/)

JavaScript 事件监听器带参数处理的实用指南

- 🚀 事件监听器在 JavaScript 中至关重要，但管理不当可能导致内存泄漏和性能问题。
- ⚠️ 常见错误：直接在 addEventListener() 中调用带参数的函数（如 myFunction(param1, param2)），这会立即执行函数而非响应事件。
- 🛠️ 解决方案 1：使用箭头/匿名函数包裹处理函数，但需注意这类监听器需通过 AbortController 移除（适合批量移除场景）。
- 🔄 方案 1 示例：
  ```javascript
  button.addEventListener("click", (event) => {
    handleClick(event, "hello", "world");
  }, { signal: controller.signal });
  ```
- 🧩 解决方案 2：利用闭包特性，外层函数接收参数，返回实际的事件处理函数，便于通过 removeEventListener() 单独移除。
- 🔄 方案 2 示例：
  ```javascript
  const handler = createHandler("Hello", 1); // 闭包保存参数
  button.addEventListener("click", handler);
  button.removeEventListener("click", handler); // 传统移除方式
  ```
- ♻️ 最佳实践：始终移除无用的事件监听器，推荐根据场景选择 AbortController（批量）或闭包+removeEventListener（单个）。
- 🌟 核心优势：这些方法完美兼容现代浏览器，兼顾参数传递与内存管理需求。

---

### [获取失败](https://spin.atomicobject.com/better-promise-all/)

**原文标题**: [Failed to retrieve](https://spin.atomicobject.com/better-promise-all/)

无法总结：获取内容失败，状态码 403。

---

### [《架构师微前端指南：React 与 Angular 的模块联邦实践》](https://developersvoice.com/blog/frontend/micro-frontends-with-react-and-angular/)

**原文标题**: [The Architectâs Guide to Micro-Frontends: Module Federation with React & Angular](https://developersvoice.com/blog/frontend/micro-frontends-with-react-and-angular/)

现代企业应用常面临单体架构扩展的痛点，微前端通过模块联邦等技术实现前端解耦与团队自治。以下是核心要点：

- 🏗️ **单体架构痛点**：技术债务累积、团队协作瓶颈、紧耦合导致的脆弱性。
- 🔗 **微前端原则**：独立部署、自治团队、技术无关性，业务与架构对齐。
- 🛠️ **集成策略对比**：构建时（NPM 包）易形成“分布式单体”，运行时（模块联邦）实现真正解耦。
- 🔄 **模块联邦核心**：宿主（Host）与远程（Remote）动态加载，共享依赖避免重复。
- ⚙️ **架构设计**：  
  - **Shell 应用**：负责路由、鉴权、全局状态与布局（薄壳/厚壳权衡）。  
  - **远程微前端**：按业务域划分，暴露最小接口，管理版本兼容性。  
  - **共享依赖**：通过单例模式管理框架库（如 React/Angular），避免冲突。
- ⚛️ **React 实践**：动态加载远程组件（Suspense + lazy），事件总线跨应用通信，路由由 Shell 主导。
- 🅰️ **Angular 实践**：CLI 集成模块联邦，动态加载远程模块，RxJS 实现跨应用通信。
- 🌐 **多框架混合**：通过 Web Components 或手动挂载实现 React 与 Angular 互操作，自定义事件通信。
- 🔒 **生产级考量**：  
  - **认证**：推荐 Shell 集中管理，传递用户上下文。  
  - **CI/CD**：独立流水线，环境隔离，渐进式发布。  
  - **性能**：缓存 RemoteEntry，监控分布式错误与性能。  
  - **设计系统**：版本化共享组件库，避免 UI 碎片化。
- 🚀 **未来趋势**：浏览器原生模块支持（如 Import Maps）、SSR/SSG 集成、工具链演进（Vite/Rspack）。
- 🤔 **适用性评估**：适合多团队协作的复杂应用，需权衡复杂度与团队自治需求。

---

### [编程文摘：电子邮件通讯](https://programmingdigest.net/?utm_source=web-archive&utm_campaign=react)

**原文标题**: [Programming Digest: Email Newsletter](https://programmingdigest.net/?utm_source=web-archive&utm_campaign=react)

每周精选编程文摘，为软件工程师提供高质量内容，涵盖技术文章、学习资源与行业动态，助力持续成长与效率提升。

- 📧 每周一封电子邮件，覆盖 19,201+ 软件工程师  
- 🔍 精选文章附简短摘要，节省筛选时间  
- 🌱 每周学习新知识，持续提升技能  
- 💬 读者好评：内容精准匹配兴趣，如 API 设计专题  
- 🚀 推荐优质资源（如《Moving Faster》获特别推荐）  
- 🌍 全球软件工程师共同订阅，来自 Bonobo Press 出品  
- 🔒 包含隐私政策与广告合作信息（2013-2025 年运营）

---

### [科技领导力：电子邮件通讯](https://leadershipintech.com/?utm_source=web-archive&utm_campaign=react)

**原文标题**: [Leadership in Tech: Email Newsletter](https://leadershipintech.com/?utm_source=web-archive&utm_campaign=react)

每周为技术领导者精心筛选的优质内容，助力 CTO、工程经理和高级工程师提升领导力。  

- 📩 超过 26,841 名工程领导者订阅的每周电子邮件  
- 📖 精选文章附简短摘要，节省寻找有价值内容的时间  
- 🌱 每周学习新知识，持续成长  
- ❤️ 读者好评：内容精准，涵盖架构讨论、会议规划及沟通技巧  
- 🏆 特别提及关于“授权”的文章，强调其关键性  
- 🌍 来自全球科技领导者的信赖阅读  

© 2013-2025 Bonobo Press | 订阅服务 · 隐私 · 广告合作

---

### [C#文摘：电子邮件通讯](https://csharpdigest.net/?utm_source=web-archive&utm_campaign=react)

**原文标题**: [C# Digest: Email Newsletter](https://csharpdigest.net/?utm_source=web-archive&utm_campaign=react)

C# Digest 是一份专为 .NET 开发者精心策划的每周通讯，提供精选文章和简短摘要，帮助开发者节省时间并每周学习新知识。

- 📧 超过 19,900 名 C# 工程师订阅这份每周电子邮件  
- 📖 阅读精选文章并附有简短摘要  
- ⏳ 节省寻找有价值内容的时间  
- 🌱 每周学习新知识  
- 💬 读者反馈：  
  - 🏢 部分内容已在实际工作中应用  
  - 🔍 发现了如标准功能标志、LINQ 和 DiagnosticListener 等新知识  
  - ❤️ 推荐了关于“操作结果模式”的文章，并促使迁移 Azure Function  
- 🌍 读者来自全球各地的 .NET 工程师  
- © 2013-2025 Bonobo Press 所有

---

### [让开发者与时俱进——Bonobo 出版社](https://bonobopress.com/)

**原文标题**: [Keeping developers up to date â Bonobo Press](https://bonobopress.com/)

Bonobo Press 是一家自 2013 年起为软件开发者和技术专业人士提供新闻资讯的出版商，拥有超过 88,000 名订阅者，涵盖开发者、IT 专业人士和技术专家。

- 📧 提供每周精选的软件开发者、工程经理、技术主管和 CTO 的新闻简报，简洁高效，深受技术人士喜爱。  
- 📢 提供广告服务，帮助广告主精准触达软件工程师、团队领导、工程经理、CTO 及 IT 决策者等目标受众。  
- 📄 可查看媒体资料包并开始合作广告投放。  
- 📩 如有任何问题、建议或广告需求，欢迎随时联系。  
- © 2013-2025 Bonobo Press 版权所有，附有条款链接。

---

### [往期通讯：第 1 页](https://reactdigest.net/newsletters)

**原文标题**: [Past Newsletters: Page 1](https://reactdigest.net/newsletters)

以下是 React Digest 的精选内容概述：

- 🚀 2025 年 7 月 27 日：深入探讨 Zustand 状态管理、React 拖放看板及 React Router 的 Action Routes  
- 🧩 2025 年 7 月 20 日：模块联邦、Astro 高效架构及 React 并发 API 解析  
- 📜 2025 年 7 月 13 日：React 历史演进、PDF.js 集成及服务器组件测试方法  
- 🧠 2025 年 7 月 6 日：组件模块化哲学、AI 代理构建与数据获取技术  
- ⚡ 2025 年 6 月 29 日：React 重渲染优化、Zero-UI 提速及 Server Components 应用  
- ✋ 2025 年 6 月 22 日：实时手势识别、自定义 useState 钩子及本地优先数据策略  
- 🔄 2025 年 6 月 15 日：细粒度响应式 Store、Next.js 状态管理及 URL 状态化  
- 🛠️ 2025 年 6 月 8 日：现代 React 框架复杂性分析、Progressive JSON 及 Remix 未来展望  
- 🚦 2025 年 6 月 1 日：高效数据获取、TanStack 路由及 React 错误边界实践  
- 🎯 2025 年 5 月 25 日：flushSync 焦点管理、并发渲染及 AI 辅助开发  
- 🔐 2025 年 5 月 18 日：React Router OpenAuth、依赖倒置原则及 RSC 静态生成  
- 📊 2025 年 5 月 11 日：复杂应用数据架构、色彩方案切换及 Dan Abramov 的 HTML 新视角  
- 🌈 2025 年 5 月 4 日：View Transitions 动画、useEffect 顺序及 Promise 序列化  
- 🧩 2025 年 4 月 27 日："不可能组件"探讨、React Query 状态简化及 AI 聊天 SDK  
- 📡 2025 年 4 月 20 日：服务端渲染进阶、全栈 AI 应用构建及 React 架构演进  
- 🏗️ 2025 年 4 月 13 日：高级 React 技巧、动态表单挑战及服务器组件深入  
- ⚖️ 2025 年 4 月 6 日：架构权衡、无库表单构建及 Dash.js 自适应流  
- 🔑 2025 年 3 月 30 日：Next.js 授权、View Transition API 及国际化实践  
- 🌐 2025 年 3 月 23 日：SSR 深度解析、TanStack 实时数据及 URL 状态管理  
- ⚡ 2025 年 3 月 16 日：Next.js 性能优化、Toast 通知实现及测试库迁移案例  

（注：因原文为多期简报合集，摘要保留了时间线与核心主题，emoji 按技术类型匹配）

---

### [隐私](https://reactdigest.net/privacy)

**原文标题**: [Privacy](https://reactdigest.net/privacy)

隐私政策概述：本文详细说明了 React Digest 如何收集、使用和保护用户的个人信息，强调了数据保护的合法性和透明度，并提供了用户访问和删除个人数据的途径。

- 🔒 隐私至关重要，因此制定了明确的政策来说明个人信息的收集、使用和披露方式。  
- 🎯 在收集个人信息前会明确目的，并仅用于指定或相关用途，需用户同意或法律要求。  
- ⏳ 个人信息仅保留至达成目的所需的时间。  
- 📝 通过合法公正的方式收集信息，并在适当时获得用户知情或同意。  
- ✔️ 确保个人数据准确、完整且最新，以满足使用目的。  
- 🛡️ 采取合理安全措施保护个人信息，防止丢失、盗窃或未经授权的访问。  
- 📢 向用户公开关于个人信息管理的政策和实践。  
- ✉️ 仅收集用户邮箱地址用于发送每周通讯，不用于其他目的。  
- 🚸 遵守 COPPA，不收集或存储 13 岁以下儿童的信息，网站也不面向该年龄段设计。  
- 📬 用户可根据《数据保护法》（英国）要求获取或删除存储的个人信息，联系邮箱：[email protected]。  
- 🚫 强烈反对垃圾邮件，提供随时退订链接，不参与任何形式的垃圾邮件活动。  
- ©️ 版权归 Bonobo Press 所有（2013-2025），涵盖新闻通讯、隐私和广告相关事项。

---

### [媒体资料包——Bonobo 出版社](https://bonobopress.com/media-kit/)

**原文标题**: [Media Kit â Bonobo Press](https://bonobopress.com/media-kit/)

Bonobo Press 为程序员和技术人员提供每周精选新闻简报，涵盖软件开发、工程管理等领域，帮助广告商精准触达目标受众并提升转化率。

- 📧 **Newsletters**：提供四种技术简报，包括《Leadership in Tech》《Programming Digest》《C# Digest》《React Digest》，订阅者覆盖欧美，高打开率和点击率。  
- 📊 **数据统计**：各简报订阅量 18K-26K，打开率 47%-58%，点击率 11%-22%，赞助价格$875-$1,940/期。  
- 🎯 **受众画像**：细分读者职位（CTO、开发工程师等）、经验水平及行业（科技、金融、医疗等），支持精准投放。  
- 💰 **广告形式**：纯文本内嵌，格式为“链接 + 标题（<100 字符）+ 描述（<400 字符）”，需提前 4 天提交。  
- 📅 **预订流程**：沟通需求→确认排期→付款锁定→内容优化→广告上线→效果反馈。  
- 🤝 **合作案例**：Okta、GitLab、MongoDB 等知名企业曾多次赞助。  
- 📩 **联系方式**：需提前数周预约档期，支持邮件咨询合作细节。

---

