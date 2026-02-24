### [React 医生](https://www.react.doctor/)

**原文标题**: [React Doctor](https://www.react.doctor/)

本文介绍了人工智能在医疗领域的应用现状与未来展望，重点探讨了其在疾病诊断、药物研发、个性化治疗及医疗管理中的具体作用，同时分析了当前面临的挑战与发展趋势。

- 🏥 AI 辅助诊断系统能通过医学影像分析提升疾病检测准确率，尤其在早期癌症识别方面表现突出
- 🔬 深度学习加速了新药研发流程，大幅缩短化合物筛选与临床试验周期
- 📊 基于患者基因数据的个性化治疗方案正成为精准医疗的核心发展方向
- 🤖 手术机器人与康复机器人的应用显著提高了复杂手术的精确度和患者康复效果
- 🛡️ 医疗数据安全与算法透明度仍是当前 AI 医疗应用需要突破的关键伦理难题
- 🌐 5G 与物联网技术正在推动远程医疗与实时健康监测系统的快速发展

---

### [管道 – WorkOS 文档](https://workos.com/docs/pipes?utm_source=cpreact&utm_medium=newsletter&utm_campaign=q12026&utm_content=no_rebuild)

**原文标题**: [Pipes – WorkOS Docs](https://workos.com/docs/pipes?utm_source=cpreact&utm_medium=newsletter&utm_campaign=q12026&utm_content=no_rebuild)

WorkOS Pipes 是一个允许用户安全连接第三方账户到应用程序的服务，简化了与 GitHub、Slack、Google 等流行服务的集成流程，无需处理 OAuth 流程、令牌刷新逻辑或凭证存储。

- 🔧 **配置提供者**：在 WorkOS 仪表板的 Pipes 部分配置提供者，选择所需服务或联系团队添加未列出的提供者。
- 🛠️ **共享凭证**：在沙盒环境中使用 WorkOS 管理的共享凭证，用户可立即连接，无需为每个提供者创建 OAuth 应用，需指定应用所需的作用域和可选描述。
- 🔑 **自定义凭证**：生产环境中使用自有 OAuth 凭证，包括在提供者仪表板创建应用、设置重定向 URI、提供客户端 ID 和密钥，并指定作用域和描述。
- 🖥️ **提供者管理**：通过 Pipes Widget 提供预建 UI，让用户连接和管理账户，显示可用提供者并处理授权流程，描述信息在 WorkOS 仪表板中设置。
- 🔄 **获取访问令牌**：用户连接提供者后，可从后端获取访问令牌以代表用户调用 API，Pipes 自动处理令牌刷新，并在问题出现时返回错误信息指导用户重新授权。

---

### [styled-components](https://styled-components.com/)

**原文标题**: [styled-components](https://styled-components.com/)

styled-components 是一个用于 React 的 CSS-in-JS 库，允许开发者在 JavaScript 中编写 CSS 样式，实现组件化样式管理，具有强类型和灵活性的特点。

- 📚 **文档与资源**：提供完整的文档、示例展示、生态系统和版本发布信息，方便开发者学习和使用。
- 🎨 **样式编写方式**：使用模板字符串语法在 JavaScript 中直接编写 CSS，支持嵌套、伪类、媒体查询等所有 CSS 特性。
- ⚙️ **组件化样式**：通过创建 `styled.button` 等样式化组件，将样式与 React 组件紧密结合，实现可复用的样式组件。
- 🔧 **动态样式**：支持通过 props 动态调整样式，例如根据 `$primary` 属性切换按钮的主要样式。
- 🚀 **快速上手**：安装简单，只需运行 `npm install styled-components`，无需构建步骤即可开始使用。
- 🛠️ **工具推荐**：建议使用 Babel 插件以获得更清晰的类名、服务端渲染兼容性和更小的打包体积。
- 🌍 **广泛应用**：被 Target、Giphy、Coinbase 等知名公司使用，用于构建美观的网站和应用程序。
- 📖 **学习路径**：提供从基础到进阶的文档，帮助开发者逐步掌握 styled-components 的所有功能。

---

### [感谢 - 开放集体](https://opencollective.com/styled-components/updates/thank-you)

**原文标题**: [Thank you - Open Collective](https://opencollective.com/styled-components/updates/thank-you)

styled-components 项目宣布进入维护模式，主要原因是 React 生态变化、CSS-in-JS 热度下降以及核心维护者不再活跃使用。项目将保持现有 API 并停止接受捐赠，仅进行必要的维护。社区反应不一，部分用户表达不舍并探讨替代方案，也有讨论涉及 React 上下文 API 在 RSC 中的兼容性问题。

- 🛠️ styled-components 进入维护模式，停止接受新捐赠，仅提供必要维护
- 🔄 项目保持现有 API 不变，避免给现有用户带来迁移负担
- 📉 CSS-in-JS 生态热度下降，Tailwind 等工具流行度上升
- 💬 社区反应复杂，部分用户推荐替代方案如 next-yak、Restyle 等
- ⚛️ 讨论涉及 React 上下文 API 在 RSC 中的兼容性争议

---

### [发布 styled-components@6.3.0 · styled-components/styled-components · GitHub](https://github.com/styled-components/styled-components/releases/tag/styled-components%406.3.0)

**原文标题**: [Release styled-components@6.3.0 · styled-components/styled-components · GitHub](https://github.com/styled-components/styled-components/releases/tag/styled-components%406.3.0)

styled-components 6.3.0 版本发布，主要增加了对 React Server Components (RSC) 的原生支持，无需额外配置即可在 RSC 环境中自动处理 CSS 注入。同时扩展了内置 HTML 和 SVG 元素别名，并修复了 TypeScript 中对 CSS 自定义属性的类型支持。

- 🚀 新增 React Server Components (RSC) 支持：自动检测 RSC 环境，无需 `'use client'` 指令，CSS 以内联样式标签注入并由 React 19 自动优化。
- 🧩 扩展元素别名：新增对现代 HTML（如 `search`、`slot`）和 SVG 元素（如 `feBlend`、`linearGradient`）的样式支持。
- 🔧 修复 TypeScript 类型：现在完全支持在 `style` 属性和 `.attrs` 中使用 CSS 自定义属性（CSS 变量）。
- ⚙️ 更新构建工具：共享 CSS 属性处理工具已更新至最新版本。

---

### [styled-components](https://styled-components.com/docs/advanced#react-server-components)

**原文标题**: [styled-components](https://styled-components.com/docs/advanced#react-server-components)

styled-components 是一个用于 React 的 CSS-in-JS 库，允许开发者通过 JavaScript 编写组件级样式，支持主题化、服务器端渲染和动态样式等功能。

- 🎨 **主题支持**：通过 `ThemeProvider` 组件提供主题，支持嵌套主题和函数式主题，可在组件中通过 `props.theme` 访问。
- 🔗 **引用其他组件**：支持通过组件选择器模式，在样式中引用其他样式组件，实现上下文样式覆盖。
- 🛡️ **安全性**：需注意用户输入作为样式插值可能引发 CSS 注入攻击，建议使用 `CSS.escape` 进行防护。
- 🔄 **服务器端渲染**：支持 SSR，通过 `ServerStyleSheet` 收集样式并注入到 HTML 中，同时兼容 React Server Components。
- 📝 **样式对象**：支持以 JavaScript 对象形式编写 CSS，便于迁移现有样式代码。
- 🛠️ **工具链**：提供 Babel、SWC、TypeScript 等插件，优化构建和开发体验。
- ⚠️ **与现有 CSS 共存**：需注意样式优先级和冲突问题，可通过提高特异性或使用命名空间解决。
- 🔧 **高级 API**：包括 `withTheme`、`useTheme` 等工具，方便在非样式组件中访问主题。

---

### [响应式深度：使用 React Three Fiber 构建滚动驱动的 3D 图像管道 | Codrops](https://tympanus.net/codrops/2026/02/17/reactive-depth-building-a-scroll-driven-3d-image-tube-with-react-three-fiber/)

**原文标题**: [Reactive Depth: Building a Scroll-Driven 3D Image Tube with React Three Fiber | Codrops](https://tympanus.net/codrops/2026/02/17/reactive-depth-building-a-scroll-driven-3d-image-tube-with-react-three-fiber/)

本教程教你使用 React Three Fiber 构建一个由滚动驱动、无限循环的 3D 图像管。通过结合着色器变形、惯性运动、确定性循环和同步 DOM 叠加，创建一个具有物理连贯性的 WebGL 体验。

- 🎯 **统一运动系统**：所有交互（滚动、鼠标移动、悬停）都影响同一套运动参数，确保场景的连贯性
- 🖥️ **着色器驱动网格**：在顶点着色器中根据鼠标位置和边缘距离平滑变形背景网格，无需纹理即可生成抗锯齿网格线
- 🔄 **无缝垂直循环**：通过动态调整当前位置和目标值，实现图像管的无限滚动效果，避免视觉跳跃
- ⚙️ **惯性阻尼控制**：滚动输入转化为速度而非直接旋转，通过每帧阻尼计算实现平滑自然的运动效果
- ⏳ **悬停时间缩放**：悬停图像时通过缩放时间增量（dt）统一减速整个系统，保持物理合理性
- 🚫 **事件传播控制**：阻止网格事件冒泡，避免与容器级指针跟踪产生干扰
- ⚡ **性能优化**：避免光线投射、React 状态动画循环和每帧内存分配，保持帧率稳定

---

### [JS 密集型方法与长期性能目标不兼容。](https://sgom.es/posts/2026-02-13-js-heavy-approaches-are-not-compatible-with-long-term-performance-goals/)

**原文标题**: [JS-heavy approaches are not compatible with long-term performance goals](https://sgom.es/posts/2026-02-13-js-heavy-approaches-are-not-compatible-with-long-term-performance-goals/)

本文基于作者在 Web 性能优化领域的实践经验，指出过度依赖 JavaScript（尤其是 React 等框架）的前端开发模式难以满足长期性能目标，并倡导更多采用服务端中心化架构。

- 🚫 **JS 密集型方案与长期性能目标不兼容**：大量 JS 代码会增加浏览器解析、编译和执行负担，导致应用启动慢、运行时卡顿，且随着时间推移性能易恶化。
- 📦 **依赖包成本高昂且难以控制**：npm 包常引入冗余代码，体积随时间增长，而工具链缺乏对包大小的透明提示，升级时可能意外增加体积。
- ⚠️ **框架易导致性能陷阱**：React 等框架常鼓励简化开发却牺牲性能的模式（如全局状态滥用、同步导入、缺乏代码分割），使优化需额外精力且易被后续更改破坏。
- 🐛 **性能调试工具不完善**：框架自带的开发工具（如 React DevTools）与浏览器原生性能分析脱节，增加调试复杂度，且缺乏关键信息（如耗时聚合视图）。
- 🛡️ **缓解措施需持续投入**：可通过性能预算、代码分割、包大小追踪、静态检测和真实用户监控等手段改善，但整体维护成本高，且难以根本解决性能脆弱性问题。
- ⚖️ **JS 密集型方案的实际收益存疑**：尽管生态丰富，但框架生态不稳定（如 API 变更导致重写），性能优化常与开发效率冲突，且可能排除低端设备用户。
- 🌐 **服务端中心化是更优替代方案**：将逻辑移至服务器可利用更强算力，减少客户端负担，提供更稳定的性能体验，并适合多数内容型应用（如配合 HTML 导航、部分 hydration 或 htmx 等轻量方案）。
- 🔄 **行业需改变开发习惯**：应避免盲目选用 JS 框架，而是根据实际需求评估架构，优先考虑服务端渲染或多页面应用，以用户设备体验为核心进行技术选型。

---

### [为智能代理未来构建 Next.js | Next.js](https://nextjs.org/blog/agentic-future)

**原文标题**: [Building Next.js for an agentic future | Next.js](https://nextjs.org/blog/agentic-future)

Next.js 团队过去一年致力于提升框架的 AI 智能体（agent）体验，通过实验和集成，认识到关键在于从智能体的视角出发，使其能“看见”和理解框架内部状态，从而提供有效的开发支持。

- 🧠 **核心理念转变**：将智能体视为 Next.js 的一等用户，从它们的视角思考所需信息、时机和消费方式。
- 👁️ **解决可见性问题**：最初发现智能体无法感知浏览器中的运行时错误、客户端警告和渲染组件，通过增强日志转发和结构化错误数据来改善。
- 🛠️ **实验性内置智能体**：开发了名为 Vector 的浏览器内聊天智能体，集成 Next.js 最佳实践以减少幻觉，但因与通用编码工具功能重叠而停止。
- 🔌 **MCP 集成突破**：通过模型上下文协议（MCP）暴露 Next.js 内部状态（如错误、路由、渲染片段），使智能体能访问开发服务器并与之通信。
- 📚 **提供框架知识**：为智能体嵌入压缩文档索引（agents.md）和结构化工作流（Next.js 技能），弥补其训练数据中缺乏的框架概念。
- 🔄 **形成调试闭环**：通过增强日志记录、知识提供和服务发现，在代码、运行时和 AI 之间建立紧密的调试反馈循环。
- 🚀 **未来计划**：简化采用流程，如通过`npx @next/codemod`生成最新文档索引，并计划将智能体支持内置到`next dev`中，实现自动上下文提供。

---

### [TanStack Router - 如何在 React 中成为路由大师 - YouTube](https://www.youtube.com/watch?v=Ab01W6h4Giw)

**原文标题**: [TanStack Router - How to Become a Routing God in React - YouTube](https://www.youtube.com/watch?v=Ab01W6h4Giw)

该文本是 YouTube 网站页脚的标准链接列表，概述了其核心服务条款、公司信息及用户资源。

- 📄 关于平台与公司信息
- 📰 新闻与媒体相关
- ©️ 版权说明与政策
- 📞 联系与合作方式
- 🎬 内容创作者资源
- 📢 广告与商业合作
- 💻 开发者工具与 API
- ⚖️ 服务条款与协议
- 🔒 隐私与数据保护
- 🛡️ 平台安全与政策
- 🔧 产品功能与测试
- ™️ 商标与所有权声明

---

### [TanStack 路由器](https://tanstack.com/router/latest)

**原文标题**: [TanStack Router](https://tanstack.com/router/latest)

TanStack Router 是一款专为 React 和 Solid 应用设计的类型安全路由库，提供客户端和全栈应用支持，具备强大的搜索参数管理和无缝的生态系统集成。

- 🚀 **类型安全与强大功能**：基于现代路由模式重新构建，提供 100% 类型安全且不牺牲开发者体验。
- 🔄 **内置数据获取与缓存**：通过加载器 API 提升数据获取效率，避免瀑布流问题，支持即时导航、内置缓存和自动预加载。
- 🔗 **搜索参数 API**：提供类似状态管理器的搜索参数处理能力，支持模式验证、类型安全及前后端操作，便于 URL 状态管理。
- 📈 **开发者高度评价**：被广泛认为使用后难以回归其他路由方案，特别适合 TypeScript 项目，提供出色的开发体验。
- 🛠️ **丰富功能与轻量级**：支持并行路由加载器、嵌套/布局路由、自动代码拆分等功能，体积轻巧（约 12kb）。
- 🌐 **广泛集成与示例**：提供文件路由和代码路由两种方式，支持与 TanStack Query、SSR、tRPC 等工具集成，并包含多种示例项目。

---

### [开源 React 甘特图 | SVAR 甘特图](https://svar.dev/react/gantt/)

**原文标题**: [Open-Source React Gantt Chart | SVAR Gantt](https://svar.dev/react/gantt/)

SVAR Gantt 是一款免费且可自定义的 React 甘特图组件，能快速集成到网页应用中，支持 TypeScript 和 React 19，并提供 MCP 服务器以辅助 AI 开发。

- 🚀 **快速集成**：几分钟内即可将功能强大的甘特图嵌入网页应用
- 🔧 **高度可定制**：提供免费和 Pro 版本，满足不同开发需求
- 📊 **技术兼容**：完美支持 TypeScript 和最新的 React 19 框架
- 🤖 **AI 开发辅助**：内置 MCP 服务器，提升开发效率
- 🌐 **演示丰富**：提供在线演示和示例，方便预览和测试

---

### [Next.js 甘特图教程 – SVAR React 甘特图 | SVAR 博客](https://svar.dev/blog/nextjs-gantt-chart-tutorial/)

**原文标题**: [Next.js Gantt Chart Tutorial â SVAR React Gantt | SVAR Blog](https://svar.dev/blog/nextjs-gantt-chart-tutorial/)

本文介绍了如何在 Next.js 应用中集成 SVAR React Gantt 图表组件，从创建项目到解决常见集成问题，最终实现一个功能完整的交互式甘特图。

- 🚀 **Next.js 作为首选框架**：适用于构建复杂、可扩展的 React 应用，提供路由、服务端渲染（SSR）和 SEO 友好页面等功能，在 2025 年 State of JS 调查中保持高使用率。
- 📊 **SVAR React Gantt 的优势**：提供免费和 PRO 版本，原生 React 支持，高性能处理大量任务，具备 TypeScript 支持和灵活 API，可快速集成到 Next.js 项目中。
- ⏱️ **快速集成教程**：在 20 分钟内完成甘特图的基本搭建，包括任务管理、拖拽调整、依赖关系编辑和内置工具栏使用。
- 🛠️ **具体实现步骤**：创建 Next.js 项目并安装 SVAR Gantt 包，通过客户端组件引入图表，添加 CSS 样式和主题（如 Willow 主题）以确保正确渲染。
- ⚠️ **解决布局与警告问题**：调整容器高度以实现全屏显示，并通过客户端渲染或忽略警告来处理 SSR 导致的水合警告。
- ✏️ **启用任务编辑功能**：通过集成 SVAR React Editor 组件，实现任务属性的可视化编辑，提升用户交互体验。
- 📚 **后续进阶内容**：预告下一部分将涉及后端集成，包括 API 路由创建、数据库持久化及服务器同步，以构建生产级调度模块。

---

### [TanStack 热键](https://tanstack.com/hotkeys/latest)

**原文标题**: [TanStack Hotkeys](https://tanstack.com/hotkeys/latest)

TanStack Hotkeys 是一个功能丰富的键盘快捷键库，提供类型安全、跨平台支持，并包含序列检测、按键状态跟踪和快捷键录制等高级功能。

- 🎯 **类型安全与跨平台** – 通过类型安全的 Hotkey 字符串验证快捷键组合，并使用跨平台的 `Mod` 修饰符自动适配 macOS（Cmd）和其他系统（Ctrl）。
- ⚙️ **智能默认设置** – 内置合理的默认行为，如自动阻止默认事件和事件冒泡，智能忽略输入框焦点状态，并支持快捷键作用域限定。
- ⌨️ **序列与录制功能** – 支持多步骤键盘序列（如 Vim 风格命令），并提供内置的快捷键录制器，允许用户自定义快捷键。
- 📦 **功能全面且轻量** – 提供按键保持检测、冲突警告、显示格式化工具等丰富功能，核心库轻量且支持 Tree-Shaking。
- 🔧 **开发工具与维护** – 包含开发工具，支持自动清理，由活跃的维护者团队更新，并欢迎合作伙伴共同推进项目发展。

---

### [TanStack | 面向 Web 开发者的高质量开源软件](https://tanstack.com/)

**原文标题**: [TanStack | High Quality Open-Source Software for Web Developers](https://tanstack.com/)

TanStack 是一个为 Web 开发者提供高质量开源软件的工具集合，专注于构建无头、类型安全且功能强大的 Web 应用工具，涵盖路由、状态管理、数据可视化、表格等多个领域。

- 🚀 **全栈框架**：TanStack Start 是一个基于 TanStack Router 和 Vite 的全栈框架，支持完整的 SSR、流式渲染和服务器函数。
- 🧭 **类型安全路由**：TanStack Router 为 React 和 Solid 应用提供完全类型安全的客户端及全栈路由解决方案。
- 🔄 **异步状态管理**：TanStack Query 提供强大的异步状态管理、服务器状态工具和数据获取功能，支持多框架。
- 💾 **客户端数据存储**：TanStack DB 是一个响应式的客户端优先存储库，支持集合、实时查询和乐观更新。
- 🧩 **框架无关数据存储**：TanStack Store 是一个不可变响应式数据存储，为 TanStack 库及其框架适配器提供核心支持。
- 🤖 **统一 AI SDK**：TanStack AI 是一个开源 AI SDK，提供跨多个提供商的统一接口，无供应商锁定。
- 📊 **无头表格 UI**：TanStack Table 提供无头 UI，用于构建强大的表格和数据网格，支持多种框架。
- 📝 **高性能表单**：TanStack Form 提供无头、高性能且类型安全的表单状态管理，适用于多种框架。
- ⌨️ **类型安全快捷键**：TanStack Hotkeys 提供类型安全的键盘快捷键、序列检测和按键状态跟踪。
- ⚡ **虚拟化列表**：TanStack Virtual 为大型可滚动元素列表提供无头虚拟化 UI，确保高性能。
- ⏱️ **性能优化工具**：TanStack Pacer 提供防抖、节流、速率限制、队列和批处理等核心性能优化功能。
- 🔧 **开发工具**：TanStack Devtools 提供一个集中的开发工具面板，支持自定义集成。
- 📦 **包管理工具**：TanStack Config 提供用于发布和维护高质量 JavaScript 包的工具和配置。
- 🛠️ **CLI 与 AI 工具包**：TanStack CLI 提供命令行工具、MCP 服务器和 AI 工具包，用于创建应用和集成 AI 代理。

---

### [概述 | TanStack 热键文档](https://tanstack.com/hotkeys/latest/docs/overview)

**原文标题**: [Overview | TanStack Hotkeys Docs](https://tanstack.com/hotkeys/latest/docs/overview)

TanStack Hotkeys 是一个类型安全、框架无关的键盘快捷键处理库，提供全面的工具集，支持热键注册、按键状态跟踪、自定义快捷键录制和多键序列处理，具备一流的 TypeScript 支持和跨平台兼容性。

- 🚀 **类型安全的热键字符串** – 提供完整的自动补全功能，支持如 `Control+A`、`Mod+Shift+G` 等有效修饰符组合，也可使用原始对象注册热键。
- 🌍 **跨平台兼容性** – `Mod` 在 macOS 上解析为 `Meta`（Cmd），在 Windows/Linux 上解析为 `Control`，并基于 `event.key` API 确保按键识别的可靠性。
- 🎯 **热键注册与管理** – 通过集中的 `HotkeyManager` 实现按目标监听、冲突检测和自动输入过滤，简化热键管理。
- 🔢 **多键序列支持** – 支持 Vim 风格的多键序列（如 `['G', 'G']`），可配置超时时间，增强操作灵活性。
- ⏺️ **热键录制功能** – 提供交互式捕获功能，适用于设置界面，支持便携的 `Mod` 格式转换，方便用户自定义快捷键。
- 📊 **按键状态跟踪** – 提供实时按键状态钩子（如 `useHeldKeys`、`useKeyHold`），帮助监控按键按下状态。
- 🖥️ **显示格式化工具** – 支持平台感知的格式化显示（如 macOS 显示 `⌘⇧S`，Windows 显示 `Ctrl+Shift+S`），便于创建快捷键提示界面。
- ⚛️ **框架适配与开发工具** – 提供 React 钩子（如 `useHotkey`、`useHotkeySequence`）和强大的开发工具，实时查看已注册热键和按键状态。

---

### [TimescaleDB：PostgreSQL 时序数据库 | 虎数 | 虎数](https://www.tigerdata.com/timescaledb?utm_source=cooperpress&utm_medium=referral&utm_campaign=react-status-newsletter)

**原文标题**: [TimescaleDB: PostgreSQL Time-Series DB | Tiger Data | Tiger Data](https://www.tigerdata.com/timescaledb?utm_source=cooperpress&utm_medium=referral&utm_campaign=react-status-newsletter)

TimescaleDB 是一个基于 Postgres 构建的时序数据库，提供高性能时序数据处理、实时分析和事件管理，兼具开源灵活性与企业级云服务支持。

- 🚀 **核心能力**：具备自动分区、行列混合存储、高达 95% 的压缩率、增量物化视图等专业时序功能，支持海量数据高速写入与查询
- ☁️ **云服务优势**：Tiger Cloud 提供一键部署、自动化数据分层至低成本存储、弹性计算资源、高可用架构及企业级安全合规支持
- 🔧 **开源自托管**：社区版和企业版可在自有基础设施部署，完整支持 PostgreSQL 生态，包含时序函数、数据压缩和调度管理
- 📊 **应用场景**：广泛适用于物联网设备监控、金融科技实时数据分析、客户实时仪表板等需要处理高频时序数据的领域
- ⭐ **客户认可**：获 Cloudflare、Replicated 等企业采用，平衡了操作简便性、专业 OLAP 性能与 PostgreSQL 原生兼容性
- 🛠️ **全面支持**：提供 24/7 专家技术支持、技术指导及从原型到生产环境的全周期服务保障

---

### [Broad Infinite List by suhaotian - 适用于 React、Vue 3 和 React Native 的双向无限列表](https://suhaotian.github.io/broad-infinite-list/)

**原文标题**: [Broad Infinite List by suhaotian  - The bidirectional infinite list for React, Vue 3 and React Native](https://suhaotian.github.io/broad-infinite-list/)

在一个项目频道中，团队成员反复询问最新部署状态并检查服务器状态，显示出对系统稳定性的高度关注。

- 🔄 频道成员多次请求检查最新部署情况
- 🖥️ 服务器状态被持续监控和确认
- ⏰ 所有消息均在同一时间（12:15）发送
- 📊 频道历史记录达到 10,000 条消息
- 👥 当前有用户在线参与讨论

---

### [GitHub - react-scad/react-scad：将JSX转换为SCAD。](https://github.com/react-scad/react-scad)

**原文标题**: [GitHub - react-scad/react-scad: Transpile JSX to SCAD.](https://github.com/react-scad/react-scad)

react-scad 是一个将 JSX 转换为 OpenSCAD 代码的工具，允许开发者使用 React/JSX 的组件化思维来创建参数化 3D 模型，并生成标准的 .scad 文件供 OpenSCAD 或切片软件使用。

- 🚀 **核心功能**：将 JSX 语法转换为 OpenSCAD 代码，实现基于组件的 3D 建模。
- 🧩 **设计理念**：采用 React 的组件、属性和组合模式，避免传统 SCAD 脚本的嵌套和参数传递复杂性。
- 📁 **输出格式**：生成纯 .scad 文件，兼容 OpenSCAD 及各类 3D 打印切片软件。
- ⚙️ **快速开始**：支持通过 CLI 创建新项目或集成到现有项目，提供实时预览和监听模式。
- 🔗 **互操作性**：支持导入外部 SCAD 库或内联原始 SCAD 代码，便于复用现有资源。
- 📐 **全面覆盖**：实现了所有主要 SCAD 图元（立方体、球体、圆柱体等）和操作（联合、差集、变换等）。
- 🛠️ **自定义与扩展**：提供底层 API 支持自定义输出路径或内存中处理，并欢迎社区贡献缺失功能。
- 📜 **开源协议**：基于 MIT 许可证开源，项目依赖 React 和 OpenSCAD 生态。

---

### [GitHub - tomkp/react-split-pane: React 分割面板组件](https://github.com/tomkp/react-split-pane)

**原文标题**: [GitHub - tomkp/react-split-pane: React split-pane component](https://github.com/tomkp/react-split-pane)

这是一个用于 React 的现代化、可访问、TypeScript 优先的拆分面板组件，支持水平和垂直布局，提供丰富的自定义选项和良好的用户体验。

- 🪝 基于现代 React 模式构建，采用钩子（Hooks）实现
- 📘 完全使用 TypeScript 编写，提供开箱即用的类型安全
- ♿ 具备键盘导航、ARIA 属性和屏幕阅读器支持，可访问性良好
- 📱 全面支持移动端和触摸设备
- 🎯 功能灵活，支持受控/非受控模式、嵌套布局及两个以上面板
- 🪶 轻量级，压缩后体积小于 5KB
- ⚡ 性能优化，使用 RAF 节流处理和优化的渲染
- 🎨 高度可定制，支持自定义样式和分隔条
- 💾 提供持久化钩子，可将面板尺寸保存到本地存储
- 🧩 支持对齐点（Snap Points）和自定义键盘导航步骤

---

### [GitHub - nickjvandyke/eslint-plugin-react-you-might-not-need-an-effect：捕获不必要的React副作用，让代码更简洁、更快速、更安全。](https://github.com/nickjvandyke/eslint-plugin-react-you-might-not-need-an-effect)

**原文标题**: [GitHub - nickjvandyke/eslint-plugin-react-you-might-not-need-an-effect: Catch unnecessary React effects to make your code simpler, faster, and safer.](https://github.com/nickjvandyke/eslint-plugin-react-you-might-not-need-an-effect)

这是一个 ESLint 插件，旨在帮助 React 开发者识别和避免不必要的 `useEffect` 使用，从而让代码更简洁、运行更快且更可靠。它通过分析状态、属性、引用及其依赖关系，提供具体的反模式警告和改进建议。

- 🎯 **核心目标**：捕获不必要的 React 副作用，使代码更简单、快速和安全。
- 📦 **安装方式**：可通过 npm 或 yarn 安装为开发依赖。
- ⚙️ **配置选项**：提供推荐（warning）和严格（error）两种配置，支持传统和扁平配置格式。
- 🔍 **规则示例**：包括禁止在副作用中存储派生状态、链式更新状态、将副作用用作事件处理器等。
- 💡 **建议配合**：推荐同时启用 `react-hooks/exhaustive-deps` 等规则以提高分析准确性。
- 📚 **学习资源**：插件文档链接到 React 官方关于 `useEffect` 和“你可能不需要副作用”的指南。
- 🤝 **反馈与改进**：鼓励用户提交问题以帮助完善插件，因为实际使用中的副作用误用场景繁多。

---

### [GitHub - dominikbulaj/react-scroll-into-view：声明式滚动至视图（任意）页面元素。微型React实用组件。](https://github.com/dominikbulaj/react-scroll-into-view)

**原文标题**: [GitHub - dominikbulaj/react-scroll-into-view: Declarative way for scrolling into view (any) page element. Tiny React utility component.](https://github.com/dominikbulaj/react-scroll-into-view)

这是一个用于 React 的轻量级工具组件，提供声明式滚动到页面任意元素的功能。

- 🎯 **核心功能**：通过封装 `Element.scrollIntoView()` 实现声明式滚动到目标元素
- 📦 **安装方式**：支持 npm、yarn、pnpm、bun 多种包管理器安装
- ⚙️ **配置灵活**：支持平滑滚动、对齐选项及完整的 `scrollIntoView` 原生参数
- 🎨 **使用简单**：只需包裹可点击子元素并指定目标选择器即可工作
- 📄 **开源许可**：采用 MIT 许可证，项目托管在 GitHub 上公开维护
- 🔧 **技术栈**：基于 TypeScript 开发，适用于 React 应用场景

---

### [GitHub - ibrahimcesar/react-lite-youtube-embed: 📺 一款默认私密、更快更简洁的 React 应用 YouTube 嵌入组件](https://github.com/ibrahimcesar/react-lite-youtube-embed)

**原文标题**: [GitHub - ibrahimcesar/react-lite-youtube-embed: 📺 ‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎< A private by default, faster and cleaner YouTube embed component for React applications />](https://github.com/ibrahimcesar/react-lite-youtube-embed)

这是一个用于 React 应用的轻量级、注重隐私的 YouTube 嵌入组件，它通过延迟加载和优化来提升性能与用户体验。

- 📦 **轻量高效** – 组件压缩后小于 5KB，相比官方 iframe 大幅减少资源加载
- 🛡️ **隐私优先** – 默认不加载 YouTube 跟踪器与 Cookie，保护用户隐私
- ⚡ **性能优化** – 仅预加载缩略图，点击后才加载播放器，减少网络请求
- 🔧 **功能丰富** – 支持懒加载、SEO 结构化数据、播放器事件监听与高质量封面
- 📚 **完善生态** – 提供完整文档、示例、TypeScript 支持及贡献指南
- 🧪 **安全可靠** – 包含 SLSA 构建验证、CodeQL 安全扫描与依赖审计

---

### [Vega 开发者文档 | Vega](https://developer.amazon.com/docs/vega/vega.html?sc_category=PAI&sc_channel=3P&sc_publisher=RS&sc_campaign=ACQ_VG&sc_country=US&sc_detail=RSTATUS-3_VG_GEN)

**原文标题**: [Vega Developer Documentation | Vega ](https://developer.amazon.com/docs/vega/vega.html?sc_category=PAI&sc_channel=3P&sc_publisher=RS&sc_campaign=ACQ_VG&sc_country=US&sc_detail=RSTATUS-3_VG_GEN)

Vega 开发者文档提供了构建适用于 Vega 平台应用的全面资源与工具，涵盖开发入门、设计、测试、发布及性能优化等环节，并包含社区支持与 API 参考。

- 🚀 **快速入门** – 提供入门指南、工具包安装及示例代码，帮助开发者快速上手 Vega 应用开发。
- 🛠️ **开发与测试** – 包含 Vega Studio（VS Code 扩展）、虚拟设备测试环境及性能优化指南，支持全流程开发调试。
- 📚 **资源文档** – 提供完整的 API 参考、React Native 支持说明及端到端开发文档，覆盖设计与发布全阶段。
- 🤝 **社区支持** – 设有 Vega 社区论坛、常见问题解答及精选文章，便于开发者交流与获取帮助。
- 🔗 **扩展服务** – 关联 Amazon 开发者生态资源，如 Appstore、AWS、Alexa 等，并提供多平台设备支持。

---

### [React 峰会——全球最大的 React 技术大会](https://reactsummit.com/?utm_source=partner&utm_medium=reactstatus)

**原文标题**: [React Summit – The Biggest React Conference Worldwide](https://reactsummit.com/?utm_source=partner&utm_medium=reactstatus)

React Summit 是全球最大的 React 年度会议，聚焦 React 生态系统和现代 Web 开发，将于 2026 年 6 月 12 日和 16 日在阿姆斯特丹举行，提供线下和远程混合参与方式。会议包含 Base Camp 和 Summit 双轨道，汇聚 60 多位演讲者分享前沿见解，预计吸引来自全球的 10,000 多名开发者，其中 1,500 人将亲临阿姆斯特丹现场。活动涵盖深度专题研讨（如全栈开发、AI 辅助编程）、会前会后 workshops、社区交流、城市游览及盛大的 React 派对。会议提供多种票务选择，包括线下混合票、远程票及包含 JSNation 会议的联票，并设有奖学金支持和开源奖项评选。

- 🗓️ **会议时间与地点**：2026 年 6 月 12 日 & 16 日在荷兰阿姆斯特丹举行，提供线下与远程混合参与模式。
- 🎤 **演讲阵容与规模**：60 多位 React 专家及行业领袖分享最新见解，预计吸引全球超过 10,000 名开发者，其中 1,500 人现场参与。
- 🏔️ **会议轨道与内容**：设立 Base Camp 和 Summit 双轨道，涵盖全栈开发、AI 工程、晋升高级工程师等深度专题，以及会前会后的 workshops。
- 🎟️ **票务与参与方式**：提供多种票务选择，包括线下混合票（€600 起）、远程票（€180 起）及与 JSNation 的联票，支持分期付款和团队折扣。
- 🌍 **社区与活动**：设有 React 开源奖项、城市游览（游船与步行）、大型派对、美食节及针对 underrepresented groups 的 100 个奖学金名额。
- 🛠️ **讲者与议题亮点**：已公布部分讲者及议题，如 React Server Components 实践、React Query 进阶、AI 辅助编程等，CFP 仍在开放中。
- 📺 **远程参与体验**：远程参会者可享受高清直播、演讲者问答、讨论室、线上 workshops 及会后录像回放。
- 🤝 **赞助与合作伙伴**：会议由 GitNation 组织，得到多家科技公司赞助，并提供企业合作与志愿者参与机会。

---

### [面向人类与 AI 的最快前端工具 | Christoph Nakazawa](https://cpojer.net/posts/fastest-frontend-tooling)

**原文标题**: [Fastest Frontend Tooling for Humans & AI | Christoph Nakazawa](https://cpojer.net/posts/fastest-frontend-tooling)

2026 年 JavaScript 工具链将迎来速度飞跃，通过采用 TypeScript Go、Oxfmt、Oxlint 等现代工具，结合严格配置与优化实践，可显著提升开发效率，为人类与 AI 提供更快的反馈循环和更可靠的代码质量。

- 🚀 **TypeScript Go**：采用 Go 重写的 TypeScript 编译器，类型检查速度提升约 10 倍，且能捕获更多类型错误，支持编辑器集成
- 🎨 **Oxfmt 替代 Prettier**：内置导入排序、Tailwind 类排序等插件，对非 JS/TS 语言回退至 Prettier，迁移过程可通过提示自动化
- 🔍 **Oxlint 替代 ESLint**：支持直接运行 ESLint 插件，提供类型感知检查，可与 TypeScript Go 集成进行类型验证
- 📦 **严格 lint 配置**：@nkzw/oxlint-config 提供零警告、强一致性、防 bug 的规则集，专为提升 AI 代码生成质量设计
- ⚡ **开发体验优化**：使用 npm-run-all2 并行执行脚本，结合 ts-node 与 swc 实现 Node.js 服务的瞬时热重载
- 🛠️ **经典工具持续使用**：pnpm 保持高效包管理，Vite 作为首选构建工具，React 凭借编译器与异步特性保持竞争力
- 🎯 **核心目标**：构建无需妥协的快速、稳定、功能完整的工具链，减少项目根目录配置文件数量

---

### [非 HTML 内容](https://cpojer.net/posts/fastest-frontend-tooling.md)

**原文标题**: [Non-HTML content](https://cpojer.net/posts/fastest-frontend-tooling.md)

无法总结：非 HTML 内容。

---

### [npm 批量可信发布配置与脚本安全性现已全面推出 - GitHub 更新日志](https://github.blog/changelog/2026-02-18-npm-bulk-trusted-publishing-config-and-script-security-now-generally-available/)

**原文标题**: [npm bulk trusted publishing config and script security now generally available - GitHub Changelog](https://github.blog/changelog/2026-02-18-npm-bulk-trusted-publishing-config-and-script-security-now-generally-available/)

npm CLI v11.10.0+ 发布两项新功能，旨在提升软件供应链安全性和配置效率。

- 🔄 **批量配置 OIDC 可信发布**：维护者现可通过 `npm trust` 命令一次性为多个包添加或更新可信发布配置，无需逐个包单独设置。
- 🛡️ **新增 `--allow-git` 安装标志**：Git 依赖（直接或传递）可能包含覆盖 git 执行路径的 `.npmrc` 文件，即使在 `--ignore-scripts` 下也可能导致任意代码执行。此标志允许用户明确控制该行为，默认值为 `all` 以保持向后兼容，但强烈建议立即使用 `--allow-git=none` 并在确实需要 Git 依赖时重新启用。预计 npm CLI v12 将默认设为 `none`。

---

### [Electrobun 文档 - 构建超快速、轻量级、跨平台的桌面应用](https://blackboard.sh/electrobun/docs/)

**原文标题**: [Electrobun Documentation - Build ultra fast, tiny, cross-platform desktop apps](https://blackboard.sh/electrobun/docs/)

Electrobun 是一个基于 TypeScript 的超快、超小、跨平台桌面应用开发框架，利用原生绑定和 Bun 运行时实现高性能。

- 🚀 极速轻量：启动时间低于 50ms，应用包体仅 14MB，更新包仅 14KB
- 🌐 跨平台支持：支持 macOS、Windows 和 Linux 系统开发
- ⚙️ 原生体验：采用系统原生 Webview 渲染（可选 CEF），实现 100% 原生操作感
- 🔧 技术架构：结合 C++/ObjC/Zig 原生绑定，以 Bun 作为后端运行时和打包工具
- 📦 内置功能：包含原生窗口管理、应用菜单、系统托盘、上下文菜单和基于 bsdiff 的更新机制
- 📚 开发资源：提供完整的 API 文档、快速入门指南和高级教程，涵盖界面构建、打包分发和代码签名等主题

---

### [构建：默认启用 Temporal by richardlau · Pull Request #61806 · nodejs/node · GitHub](https://github.com/nodejs/node/pull/61806)

**原文标题**: [build: enable Temporal by default by richardlau · Pull Request #61806 · nodejs/node · GitHub](https://github.com/nodejs/node/pull/61806)

该 PR 提议在 Node.js 构建中默认启用 Temporal 支持，这需要新增 Rust 工具链（cargo 和 rustc）作为构建依赖，并引入了相应的配置选项与自动检测逻辑。

- 🛠️ 默认启用 Temporal 支持需依赖 Rust 工具链（cargo 和 rustc）
- ⚙️ 新增`--v8-disable-temporal-support`选项可显式禁用 Temporal 支持
- 🔍 未指定选项时自动检测 Rust 工具链：若未检测到则警告并禁用，检测到则启用
- ❌ 使用`--v8-enable-temporal-support`时若缺少 Rust 工具链则构建报错
- 🚫 同时使用启用与禁用选项会导致配置脚本报错
- 🚧 该变更计划在 Node.js 26 版本中推出，目前等待 V8 更新
- 🤔 社区讨论了自动检测可能因系统更新意外影响 Temporal 状态的问题
- ✅ 多位核心成员已批准该 PR，并标记为重大变更

---

