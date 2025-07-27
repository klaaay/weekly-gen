### [React 状态周报第 437 期：2025 年 7 月 23 日](https://react.statuscode.com/issues/437)

**原文标题**: [React Status Issue 437: July 23, 2025](https://react.statuscode.com/issues/437)

概述  
本期内容涵盖了 React 生态的最新动态，包括新工具、库、教程和最佳实践，适合开发者了解前沿技术和提升开发效率。  

- ⚛️ **Untitled UI React**：一个基于 Tailwind CSS 和 React Aria 的开源 UI 组件库，提供免费和 PRO 版本，支持 Figma 集成。  
- 📚 **React Compiler 文档更新**：React 团队优化了官方文档，帮助开发者更好地使用这一 AOT 优化工具。  
- 🚫 **React 和 Next.js 常见错误避免**：David Khourshid 分享实用模式，避免冗余状态和嵌套数据等问题。  
- � **Figma MCP vs Claude**：对比两种将 Figma 设计转换为 React 代码的方法，探讨其效果差异。  
- 🏗️ **Zustand 状态管理**：介绍成熟且简洁的状态管理库 Zustand，适合 React 开发者使用。  
- 🔮 **React Router 与 Server Components**：探讨 React Router 未来对 Server Components 的支持及其影响。  
- � **React 图形可视化**：推荐 React 图形可视化工具，适合构建动态交互式 UI。  
- 🛠️ **新工具与库**：包括 Reagraph（网络图可视化）、React Unity WebGL（Unity 集成）、React CodeMirror（代码编辑器）等。  
- 📢 **JavaScript 生态动态**：涵盖 Bun 更新、Laravel 在 Node.js 运行、eslint-config-prettier 安全事件等。

---

### [无标题 UI React —— React UI 组件库](https://www.untitledui.com/react)

**原文标题**: [Untitled UI React â React UI Component Library](https://www.untitledui.com/react)

Untitled UI React 是一个开源 React UI 组件库，基于 Tailwind CSS 和 React Aria 构建，提供丰富的组件和模板，帮助开发者快速构建现代、美观的界面。

- 🚀 **开源组件库**：Untitled UI React 是最大的开源 React UI 组件库之一，支持直接复制、粘贴和构建。  
- 🛠️ **技术栈**：基于 React v19.1、Tailwind CSS v4.1、TypeScript v5.8 和 React Aria，确保高性能和可访问性。  
- 📦 **丰富组件**：包含数千个组件和变体，如按钮、表格、模态框、图表等，满足各种开发需求。  
- 🎨 **设计同步**：与 Untitled UI Figma 完美同步，确保设计和代码一致性。  
- ⚡ **快速启动**：提供 CLI 工具和预配置的 Starter Kits（如 Next.js、Vite），加速项目开发。  
- 🌙 **暗黑模式**：内置 CSS 变量支持，一键切换暗黑模式。  
- 💰 **灵活定价**：提供免费版和付费 PRO 版（Solo/Team），支持无限项目使用和终身更新。  
- 📚 **详细文档**：完善的文档和示例，降低学习成本。  
- 🌍 **社区认可**：被全球 28 万 + 设计师和开发者使用，多家知名公司推荐。

---

### [介绍 | 无标题用户界面](https://untitledui.com/react/docs/introduction)

**原文标题**: [Introduction | Untitled UI](https://untitledui.com/react/docs/introduction)

Untitled UI React 是一个基于全球最大 Figma UI 套件的开源 React 组件库，提供现成的高质量组件，帮助快速构建现代界面。

- 🚀 **组件库介绍**：Untitled UI React 是全球最大的开源 React 组件集合，基于 Tailwind CSS 和 React Aria，可直接复制粘贴使用。  
- ⚡ **技术栈**：采用 React v19.1、Tailwind CSS v4.1、TypeScript v5.8 和 React Aria v1.9，确保高性能和现代化。  
- ♿ **无障碍支持**：基于 React Aria 构建，所有组件均符合无障碍标准。  
- 🔓 **开源自由**：免费提供基础组件，MIT 许可，可自由修改和扩展，无供应商锁定。  
- 🛠️ **灵活控制**：直接获取源代码，无需管理依赖，完全自主定制。  
- 🌟 **专业版优势**：PRO 版本包含更多高级组件、仪表板和页面模板。  
- 🔄 **持续更新**：所有产品终身免费更新，紧跟技术潮流。  
- 🎨 **设计同步**：与 Untitled UI Figma 设计系统完美对齐，保持设计与代码一致。  
- 💡 **贡献支持**：欢迎通过 GitHub 提交问题或拉取请求参与改进。  
- 📥 **快速开始**：提供安装指南，助你立即上手。

---

### [React 编译器 - React](https://react.dev/learn/react-compiler)

**原文标题**: [React Compiler – React](https://react.dev/learn/react-compiler)

React Compiler 是一个自动优化 React 应用的编译器，通过处理记忆化减少手动使用 `useMemo`、`useCallback` 和 `React.memo` 的需求。

- 🚀 **功能简介**：自动优化 React 应用，处理记忆化，无需手动使用 `useMemo`、`useCallback` 或 `React.memo`。  
- ⚙️ **安装指南**：提供安装步骤，并介绍如何与构建工具配置。  
- 🔄 **渐进式采用**：支持在现有代码库中逐步启用 React Compiler，无需一次性全面切换。  
- 🐞 **调试与问题排查**：提供调试指南，帮助区分编译器错误与运行时问题，识别常见错误模式，并遵循系统化调试流程。  
- 📋 **配置与参考**：包含详细配置选项和 API 参考，如 React 版本兼容性、函数级编译控制及预编译库的支持。  
- 🌐 **额外资源**：推荐加入 React Compiler 工作组，获取更多讨论与信息。  
- 🔗 **相关链接**：提供 React 开发者工具、快速入门、社区资源等进一步学习内容。

---

### [Figma MCP 大战 Claude：UI 设计对决！- YouTube](https://www.youtube.com/watch?v=uGp5kTPWaqY)

**原文标题**: [Figma MCP vs Claude: UI Building Battle! - YouTube](https://www.youtube.com/watch?v=uGp5kTPWaqY)

关于 YouTube 平台的相关信息与资源链接  
- 📢 关于：平台的基本介绍与背景信息  
- 🗞️ 新闻：获取最新动态与公告  
- ©️ 版权：版权政策与相关内容  
- 📩 联系我们：用户沟通与支持渠道  
- 🎨 创作者：创作者资源与支持计划  
- 💼 广告：广告合作与商业机会  
- 💻 开发者：开发者工具与 API 信息  
- 📜 条款：平台使用条款与协议  
- 🔒 隐私：用户隐私政策与数据保护  
- ⚖️ 政策与安全：社区准则与安全措施  
- 🔧 YouTube 运作机制：平台功能与工作原理说明  
- � 测试新功能：体验最新推出的实验性功能  
- ®️ 版权声明：2025 年 Google LLC 版权所有

---

### [介绍我们的开发者模式 MCP 服务器：将 Figma 融入您的工作流程 | Figma 博客](https://www.figma.com/blog/introducing-figmas-dev-mode-mcp-server/)

**原文标题**: [Introducing our Dev Mode MCP server: Bringing Figma into your workflow | Figma Blog](https://www.figma.com/blog/introducing-figmas-dev-mode-mcp-server/)

Figma 宣布推出 Dev Mode MCP 服务器测试版，将设计上下文直接集成到开发者工作流中，帮助 LLM 生成更符合设计意图的代码。

- 🚀 **测试版发布**：Figma 推出 Dev Mode MCP 服务器测试版，支持 LLM 在设计上下文中生成代码。  
- 🔗 **MCP 标准**：通过 Model Context Protocol（MCP）标准，将 Figma 设计上下文集成到 Copilot、Cursor 等开发工具中。  
- 🛠 **功能亮点**：支持原子组件创建、多层级应用流程构建，提升设计到代码的效率和准确性。  
- 📅 **未来计划**：将推出远程服务器功能、更深度的代码库集成等更新，持续迭代产品。  
- 🤖 **上下文重要性**：LLM 需要更多上下文（如代码库结构、设计意图）以生成符合团队独特模式的代码。  
- 🎨 **设计意图转换**：Figma Dev Mode MCP 服务器通过模式元数据、截图、交互性和内容等方式，为 LLM 提供全面的设计上下文。  
- 🔧 **工具配置**：开发者可以配置服务器设置，控制提供给 LLM 的上下文类型，优化代码生成。  
- 📸 **截图功能**：提供高层次的视觉信息，帮助 LLM 理解设计流程和节点关系。  
- 💡 **交互性示例**：通过伪代码和示例代码，帮助 LLM 更好地理解设计行为和状态。  
- 📝 **内容提取**：从 Figma 中提取文本、SVG、图层名称等内容，帮助 LLM 填充数据模型。  
- 🔄 **持续改进**：未来将支持注释、Grid 等功能，并优化 Code Connect 体验。  
- 📢 **反馈征集**：Figma 鼓励用户提供反馈，以指导未来功能的开发。  
- 🔗 **获取方式**：所有 Dev 或 Full 席位用户均可访问 Dev Mode MCP 服务器。

---

### [介绍 Zustand（状态管理）—— Frontend Masters 博客](https://frontendmasters.com/blog/introducing-zustand/)

**原文标题**: [Introducing Zustand (State Management) – Frontend Masters Blog](https://frontendmasters.com/blog/introducing-zustand/)

概述：  
Zustand 是一个简洁但功能强大的 React 状态管理库，旨在简化状态管理并提升渲染性能。本文通过一个任务管理应用示例，对比了使用 React Context 和 Zustand 的不同实现方式，展示了 Zustand 的优势和最佳实践。

- 🚀 **Zustand 简介**  
  Zustand 是一个轻量级且高效的状态管理库，适合 React 应用，尤其适合需要避免“prop drilling”的场景。

- 📂 **示例应用**  
  通过一个任务管理应用，展示了三种实现方式：React Context、非最佳实践的 Zustand 和优化后的 Zustand。

- 🔄 **React Context 的问题**  
  使用 React Context 会导致所有消费者组件在状态变化时重新渲染，即使它们不依赖变化的状态部分。

- 🛠️ **Zustand 的基本用法**  
  使用 `create` 方法创建状态存储，并通过 `set` 函数更新状态，简化了状态管理代码。

- ⚡ **优化状态读取**  
  通过传递选择器函数给 `useTasksStore`，可以避免不必要的重新渲染，提升性能。

- 🔄 **异步支持**  
  Zustand 支持异步操作，可以在异步函数中调用 `set` 来更新状态。

- 📖 **读取状态的其他方式**  
  提供了 `get` 函数和 `getState` 方法，方便在存储内部或 React 组件外部读取状态。

- 🔍 **高级功能**  
  Zustand 支持手动订阅、与 Immer 集成等高级功能，适合复杂应用场景。

- 🎯 **结论**  
  Zustand 是一个简单、有趣且高效的状态管理解决方案，能够显著提升 React 应用的性能和开发体验。

---

### [GitHub - pmndrs/zustand: 🐻 React 状态管理的极简方案](https://github.com/pmndrs/zustand)

**原文标题**: [GitHub - pmndrs/zustand: 🐻 Bear necessities for state management in React](https://github.com/pmndrs/zustand)

zustand 是一个轻量、快速且可扩展的 React 状态管理库，采用简化的 Flux 原则，基于 hooks 的舒适 API，无样板代码且不固执己见。

- 🐻 轻量且快速的状态管理解决方案  
- 🎣 基于 hooks 的 API，使用简单  
- 🚀 无需上下文包装，减少样板代码  
- 🔍 支持选择性状态更新，避免不必要的渲染  
- 🧩 中间件支持（如持久化、Immer、Redux 工具等）  
- ⚡ 支持异步操作和外部状态访问  
- 📦 提供 Vanilla 版本，可在非 React 环境中使用  
- 🔄 支持 Redux 风格的重置和中间件  
- 🛠️ 内置解决常见问题（如僵尸子问题、并发问题等）  
- 🌐 支持 TypeScript，类型安全  
- 📚 丰富的文档和示例

---

### [React Router 与 React Server Components：前行之路 | Remix](https://remix.run/blog/react-router-and-react-server-components)

**原文标题**: [React Router and React Server Components: The Path Forward | Remix](https://remix.run/blog/react-router-and-react-server-components)

React Router 正在整合 React Server Components (RSC) 支持，这一变革不仅简化了架构，还增强了数据加载、流式 UI 和代码分割的能力，同时降低了对特定打包工具的依赖。

- 🚀 **RSC 支持**：React Router 将支持 RSC，提供更强大的数据模式，同时保持向后兼容性。  
- 🔄 **架构简化**：新的 RSC 架构减少了打包器的耦合，使 React Router 更轻量且易于使用。  
- 📊 **数据加载优化**：开发者可以选择使用 Framework Mode 的 loader 函数或 RSC 的 props 传递方式，灵活应对不同场景。  
- ⏳ **流式 UI 支持**：通过 `<Await>` 组件（Framework Mode）或 `use(promise)`（RSC），实现部分内容的渐进加载。  
- 🧩 **代码分割改进**：RSC 的动态导入和 "use client" 指令减少了初始加载的代码量，提升性能。  
- 🔧 **现有项目兼容**：当前使用 Framework Mode 或 Data Mode 的项目无需迁移，未来可无缝过渡到 RSC 版本。  
- ⚠️ **不稳定阶段**：React Router RSC 目前仍处于实验阶段，建议新项目暂用现有 API，但欢迎开发者试用并提供反馈。  
- 🔮 **未来计划**：Vite 将支持 RSC 的 Framework Mode，进一步简化配置和构建流程，减少生成文件的复杂性。  
- 🌟 **更广泛的应用**：RSC 的加入使 React Router 能更好地支持从 SPA 到复杂 SSR 应用的全栈开发场景。

---

### [React 图形可视化指南：库选择、最佳实践与实现](https://cambridge-intelligence.com/react-graph-visualization-library/?utm_campaign=16812718-React%20Status%20newsletter%20ad&utm_source=NewsletterAd&utm_medium=SponsoredLink)

**原文标题**: [
		React Graph Visualization Guide: Libraries, Best Practices & Implementation	](https://cambridge-intelligence.com/react-graph-visualization-library/?utm_campaign=16812718-React%20Status%20newsletter%20ad&utm_source=NewsletterAd&utm_medium=SponsoredLink)

React 图形可视化工具包是现代开发者在数据可视化中的首选，尤其适合需要无缝集成到现有技术栈的场景。其组件化设计和动态交互能力使其成为复杂网络可视化的理想选择。

- 🔍 **React 图形可视化定义**：利用 React 构建交互式节点链接图，适用于复杂网络分析，如网络安全、金融欺诈检测等。  
- 🛠️ **核心优势**：声明式编程模型、虚拟 DOM 高效更新、实时数据响应和可扩展架构。  
- 🏢 **行业应用**：  
  - 🔒 **网络安全**：实时分析设备关系与警报模式，集成 React 仪表盘。  
  - 🕵️ **情报与执法**：动态处理变化数据，支持证据分类和交互式报告。  
  - 💰 **金融服务**：实时交易监控与欺诈模式可视化，复用组件提升效率。  
- 📊 **构建要点**：选择合适库（如 ReGraph 或开源方案）、设计节点/边数据结构、优化布局与交互模型。  
- 📂 **数据结构建议**：JSON 格式，包含 ID、标签、样式及元数据，支持分层（如组合节点）和流式更新。  
- 📚 **推荐工具**：  
  - 🏆 **ReGraph**：高性能商业 SDK，专为复杂图形设计。  
  - 🆓 **开源选项**：Cytoscape.js（需 React 封装）、React Flow（低代码场景）。  
- 🔄 **替代方案**：  
  - KeyLines（传统 JS 库）、D3.js（高灵活性）、Neo4j Bloom（限于 Neo4j 生态）。  
- 🚀 **行动建议**：通过 ReGraph 试用体验高性能 React 图形可视化，适用于威胁映射、知识图谱等场景。

---

### [如何使用 Matter.js 和 React Native Skia 构建 2D 游戏风格物理效果](https://expo.dev/blog/build-2d-game-style-physics-with-matter-js-and-react-native-skia)

**原文标题**: [How to Build 2D Game-Style Physics with Matter.js and React Native Skia](https://expo.dev/blog/build-2d-game-style-physics-with-matter-js-and-react-native-skia)

Expo 是一个提供应用开发服务的平台，包含文档、博客、产品信息、定价等资源，并支持社区交流和合规服务。

- 📝 Blog - 提供博客文章  
- 📚 Docs - 开发文档资源  
- 🛠 Product - 产品相关信息和工具  
- 💰 Pricing - 价格方案  
- 🚀 EAS - Expo 应用服务  
- 📊 Dashboard - 控制面板  
- 🌟 Star us on GitHub - GitHub 上点赞支持  
- 📱 Expo Go - 移动端应用  
- 🛰 Expo Orbit - 社区或工具  
- 🍴 Snack - 代码分享平台  
- 📰 Newsletter - 订阅通讯  
- 💬 Join Discord - 加入社区交流  
- � Legal - 法律条款和隐私政策  
- ©️ Copyright - 版权信息

---

### [我们将网站迁移至 Eleventy，性能提升 24% | Etch 软件工作室](https://etch.co/blog/we-migrated-our-site-to-eleventy-and-increased-performance-by-24-percent)

**原文标题**: [We migrated our site to Eleventy and increased performance by 24% | Etch Software Studio](https://etch.co/blog/we-migrated-our-site-to-eleventy-and-increased-performance-by-24-percent)

将网站从 Next.js 迁移到 Eleventy 后，性能提升了 24%，减少了依赖并优化了用户体验。

- 🚀 性能提升：Lighthouse 性能评分从 76 提升至 97，主页 JavaScript 大小从 2161KB 降至 11.3KB。  
- 🛠️ 工具选择：Eleventy 提供轻量级工具集，专注于 HTML 模板、CSS 打包和少量 JavaScript。  
- 📉 依赖减少：NPM 依赖从 1115 个降至 13 个，代码行数从 6877 减少到 4307。  
- 🌐 浏览器优化：Eleventy 仅在构建时运行，不向浏览器发送额外代码。  
- 🔧 稳定性：自 2018 年以来，Eleventy 仅进行了 3 次主要版本更新，减少了维护负担。  
- 📜 模板语言：选择 WebC 作为模板语言，支持 HTML 和 Web 组件，但学习曲线较陡。  
- 🎨 样式打包：使用 WebC 内置打包工具和 Lightning CSS 进行 CSS 压缩和浏览器兼容性处理。  
- ⚡ JavaScript 交互：通过 Web 组件实现客户端交互，减少不必要的 JavaScript 加载。  
- 🔄 服务工人：自定义 Workbox 服务工人，预缓存静态资源并优化缓存策略。  
- 💡 最终结论：Eleventy 更适合静态内容网站，简化了工具链并提升了整体性能。

---

### [Eleventy 是一个更简单的静态网站生成器](https://www.11ty.dev/)

**原文标题**: [Eleventy is a simpler static site generator](https://www.11ty.dev/)

Eleventy 是一个简单易用的静态网站生成器，支持多种模板语言，具有快速构建和高度灵活的特点。

- 🚀 **快速构建** - Eleventy 构建速度极快，处理 4000 个 Markdown 文件仅需 1.93 秒，远超其他工具如 Astro、Gatsby 和 Next.js。  
- 🛠️ **多模板支持** - 支持 HTML、Markdown、WebC、JavaScript 等多种模板语言，可混合使用。  
- 🌍 **生产就绪** - 被 NASA、Google、Microsoft 等知名机构使用，GitHub 上有 82,000+ 仓库使用。  
- 🔒 **无追踪** - 不收集用户数据，无需担心隐私问题。  
- ⚙️ **零配置启动** - 开箱即用，也支持灵活配置和插件扩展。  
- 📂 **兼容现有结构** - 无需特定目录结构，支持渐进式迁移。  
- 🧩 **社区强大** - 拥有活跃且友好的开发者社区。  
- 🏆 **用户口碑** - 获得 Google 开源奖，开发者评价极高。  
- 🔄 **无客户端 JS** - 默认不生成客户端 JavaScript，适合长期项目。  
- 📚 **丰富文档** - 提供详细指南和教程，入门简单。

---

### [使用 React 创建支持社交登录认证的 PWA 应用 | Okta 开发者](https://developer.okta.com/blog/2025/07/22/react-pwa)

**原文标题**: [Create a React PWA with Social Login Authentication | Okta Developer](https://developer.okta.com/blog/2025/07/22/react-pwa)

概述：本文详细介绍了如何使用 React 构建一个支持离线功能的渐进式 Web 应用（PWA），并通过 Okta 集成 Google 社交登录认证，实现安全、快速的用户身份验证。

- 🚀 渐进式 Web 应用（PWA）结合了原生应用的速度、可靠性和离线功能，并通过 Web 交付。
- 🔒 使用 Okta 作为身份提供商，实现安全、可扩展且对开发者友好的身份验证。
- 🔄 联合身份允许用户使用现有的社交账户（如 Google）登录。
- 🛠️ 需要准备 Node.js、NPM、命令行终端、基本的 JavaScript 和 TypeScript 知识，以及 Google Cloud Console 账户。
- 📝 创建 Okta 集成，包括设置应用程序类型、授权类型和重定向 URI。
- ⚛️ 使用 Vite 模板创建 React 应用，并安装 React Router 和 Okta SDK。
- 🛡️ 在 React 应用中通过 React Router 和 Okta SDK 保护路由，实现 OAuth 2.0 和 OpenID Connect（OIDC）认证。
- 🔗 配置 Google 作为 Okta 中的身份提供商，并测试 Google 社交登录功能。
- 📱 使用 vite-plugin-pwa 插件将 React 应用设置为 PWA，支持离线功能。
- 📋 构建一个安全的待办事项列表 React PWA，通过本地存储实现数据持久化。
- 📚 提供更多学习资源，包括渐进式 Web 应用、Redux 管理认证状态和 Android 登录等内容。

---

### [Reagraph - 基于 WebGL 的高性能网络图可视化 React 组件](https://reagraph.dev/)

**原文标题**: [Reagraph - a high-performance network graph visualization built in WebGL for React](https://reagraph.dev/)

Reagraph 是一个基于 WebGL 的开源网络图可视化工具，专为 React 设计，支持 2D 和 3D 视图，提供高度可定制化的图表构建方案。

- 🌐 **WebGL 驱动**：利用 WebGL 技术实现高性能的 2D 和 3D 图形渲染。
- 🛠️ **高度可定制**：基于 D3 构建，支持完全自定义视觉效果、交互和行为。
- 📊 **大数据处理**：能够高效处理大规模数据集，渲染速度快且设置简单。
- 🧠 **智能默认配置**：无需复杂配置即可生成美观的图表。
- 🔗 **复杂聚类支持**：适用于高级用例，支持复杂的数据模式。
- 🚀 **React 集成**：专为 React 设计，轻松构建交互式数据可视化。
- 🎨 **主题定制**：支持浅色和深色主题，并可自定义主题样式。
- 📦 **简单上手**：通过 npm 安装即可快速开始使用，提供详细的文档和示例。
- ❤️ **开源免费**：由 Good Code 开发，免费使用且易于扩展。

---

### [简介 - Reagraph](https://reagraph.dev/docs)

**原文标题**: [Introduction - Reagraph](https://reagraph.dev/docs)

Reagraph 是一个基于 WebGL 构建的高性能网络图可视化工具，专为 React 设计。

- 🚀 **WebGL 基础**：提供高性能的图形渲染能力  
- 📊 **节点大小**：支持根据属性、页面排名、中心性等自定义调整  
- 🌓 **主题模式**：内置浅色和深色模式，支持自定义主题  
- 🛤️ **路径查找**：支持节点之间的路径查找功能  
- 🎯 **径向上下文菜单**：提供便捷的交互操作  
- 🔍 **高亮与选择钩子**：支持节点的高亮和选择功能  
- 🖱️ **节点拖拽**：允许用户通过拖拽调整节点位置  
- 🪃 **套索选择**：支持通过套索工具批量选择节点  
- ➕ **节点展开/折叠**：可动态展开或折叠节点  
- 🎨 **自定义节点**：支持高度自定义的节点样式  
- 📝 **高级标签布局**：优化标签显示位置  
- 🔗 **边插值**：支持边的平滑插值显示  
- 🧩 **聚类功能**：提供节点聚类功能以简化复杂网络

---

### [@storybook/core - Storybook](https://storybook.reagraph.dev/)

**原文标题**: [@storybook/core - Storybook](https://storybook.reagraph.dev/)

好的，请提供需要总结的文本内容，我会按照您要求的模板生成概述和带表情符号的要点列表。  

示例模板：  

概述总结  

- 🌟 要点一  
- 📌 要点二  
- 🔍 要点三  

请提供具体文本，我会为您生成相应的总结！

---

### [GitHub - reaviz/reagraph: 🕸 基于 React 的 WebGL 图形可视化库。由@goodcodeus 维护。](https://github.com/reaviz/reagraph)

**原文标题**: [GitHub - reaviz/reagraph: 🕸 WebGL Graph Visualizations for React. Maintained by @goodcodeus.](https://github.com/reaviz/reagraph)

Reagraph 是一个基于 WebGL 的高性能 React 网络图可视化库，由 @goodcodeus 维护，支持多种布局和自定义功能。

- 🚀 **快速链接**  
  - 查看[文档和示例](reagraph.dev)  
  - 在[CodeSandbox](https://codesandbox.io)上体验基础示例  
  - 通过[更新日志](CHANGELOG.md)了解最新动态  

- 💎 **其他项目**  
  - Reaflow：工作流和图表开源库  
  - Reablocks：基于 Tailwind 的 React 组件库  
  - Reaviz：React 数据可视化库  
  - Reachat：构建 LLM/Chat UI 的开源库  

- ✨ **核心功能**  
  - 基于 WebGL 的高性能渲染  
  - 支持节点大小、主题自定义、路径查找  
  - 多种布局（2D/3D 力导向图、树状图、径向图等）  
  - 高级标签布局、边绑定、聚类等  

- 📦 **安装与使用**  
  - 通过 `npm i reagraph` 或 `yarn add reagraph` 安装  
  - 提供简单的 API 示例（如 `GraphCanvas` 组件）  

- 🔭 **开发与贡献**  
  - 克隆仓库后运行 `npm start` 即可启动 Storybook  
  - 欢迎通过 GitHub 提交改进  

- ❤️ **社区支持**  
  - 由 33+ 贡献者共同维护  
  - 采用 Apache-2.0 开源协议  

- 🌐 **技术栈**  
  - 主要语言：TypeScript（97.8%）  
  - 主题标签：React/WebGL/网络图可视化

---

### [React Unity WebGL](https://react-unity-webgl.dev/)

**原文标题**: [React Unity WebGL](https://react-unity-webgl.dev/)

React Unity WebGL 是一个用于在 React 应用中嵌入 Unity WebGL 构建的现代解决方案，支持双向通信和交互。

- 🎮 **React Unity WebGL 简介**  
  自 2017 年起，帮助开发者将 Unity 游戏带到网页端，实现与网页组件的交互和使用 Web API。

- 📦 **安装方法**  
  通过 npm 安装：`npm install react-unity-webgl`。

- 🌍 **基础示例**  
  展示如何在 React 应用中嵌入 Unity WebGL 构建，使用 `useUnityContext` 配置加载路径。

- ⏳ **加载状态**  
  使用 `loadingProgression` 和 `isLoaded` 显示加载进度，并在加载完成后显示 Unity 内容。

- 📡 **通信示例**  
  通过 `sendMessage` 和事件监听实现 Unity 与 React 之间的双向通信，例如游戏结束事件和分数传递。

- 📊 **性能分析**  
  使用 `useUnityMetricsInfo` 监控 Unity 应用的帧率（FPS）等性能指标。

- 🔄 **交互功能**  
  提供按钮触发 Unity 中的方法（如生成敌人），并实时更新 React 界面。

---

### [Unity 实时开发平台 | 3D、2D、VR 及 AR 引擎](https://unity.com/)

**原文标题**: [Unity Real-Time Development Platform | 3D, 2D, VR & AR Engine](https://unity.com/)

Unity 平台概览  
- 🎮 支持 20+ 终端平台运行 Unity 创作内容²  
- 📥 每月 Made with Unity 应用下载量达 36 亿次³  
- 🏆 全球 Top100 游戏中 82% 使用 Unity 开发⁴  

核心功能与服务  
- 🕹️ **游戏开发**：覆盖 20+ 平台的一站式工具链，助力游戏从创作到发行⁵  
- 🏭 **工业应用**：将 CAD/3D 数据转化为跨设备沉浸式体验  
- 📈 **增长支持**：提供变现工具与专业服务，助力应用商业化  

成功案例与资源  
- 🌟 **成功故事**：展示全球开发者使用 Unity 的卓越成果  
- 📚 **资源中心**：包含知识库、问题追踪器等实用工具  
- 🎓 **学习平台**：在线课程、认证与教育机构合作资源  
- 🌍 **创作者社区**：连接全球从业者与爱好者的交流网络  

订阅方案  
- 🆓 **个人版**：免费使用全球流行游戏引擎  
- 💼 **专业版**：为团队提供多平台专业开发工具  
- � **企业版**：支持大型 3D 项目的定制化企业服务  

注：数据截至 2023 年 12 月（部分来源为 Unity 内部统计）  
创作者荣誉案例包括《蝙蝠侠》《原神》等知名作品团队

---

### [GitHub - jeffreylanters/react-unity-webgl: React Unity WebGL 提供了一个现代解决方案，用于在 React 应用中嵌入 Unity WebGL 构建，同时提供高级 API 以实现 Unity 与 React 之间的双向通信和交互。](https://github.com/jeffreylanters/react-unity-webgl)

**原文标题**: [GitHub - jeffreylanters/react-unity-webgl: React Unity WebGL provides a modern solution for embedding Unity WebGL builds in your React Application while providing advanced APIs for two way communication and interaction between Unity and React.](https://github.com/jeffreylanters/react-unity-webgl)

React Unity WebGL 是一个用于在 React 应用中嵌入 Unity WebGL 构建的现代解决方案，提供高级 API 实现双向通信和交互。

- 🎮 **项目功能**：提供 React 与 Unity WebGL 之间的双向通信和交互能力。  
- 🌐 **官网**：[react-unity-webgl.dev](https://react-unity-webgl.dev)  
- 📜 **许可证**：Apache-2.0 开源协议  
- ⭐ **受欢迎度**：1.8k Stars，170 Forks  
- 🔄 **兼容性**：仅支持 Unity 2020 及以上版本，旧版本需使用遗留模块  
- 💻 **安装**：通过 npm 或 yarn 安装，需确保 Unity 版本兼容  
- 📚 **文档**：官网提供详细文档、API 参考和示例代码  
- 💡 **快速开始**：基本实现只需配置 Unity 文件路径并渲染组件  
- 🤝 **社区支持**：提供 Discord 社区和讨论区，欢迎贡献和问题反馈  
- 💖 **维护声明**：项目为个人维护，免费但接受捐赠或赞助支持  
- 🛠 **开发与测试**：贡献需先通过讨论区提案，遵循开发流程

---

### [React CodeMirror - React 的 CodeMirror 组件](https://uiwjs.github.io/react-codemirror/)

**原文标题**: [React CodeMirror - CodeMirror component for React.](https://uiwjs.github.io/react-codemirror/)

好的，请提供需要总结的文本内容，我会按照您要求的格式生成概述和带表情符号的要点列表。  

示例格式：  

这里是文章的概述总结  

- 🌟 要点一  
- 📌 要点二  
- 🔍 要点三  

请提供具体文本，我会为您生成相应的总结。

---

### [CodeMirror](https://codemirror.net/)

**原文标题**: [CodeMirror](https://codemirror.net/)

CodeMirror 是一个用于网页的代码编辑器组件，支持多种编辑功能，并提供丰富的编程接口以进一步扩展。

- 🌐 **网页代码编辑器**：适用于网站，支持多种编辑功能和扩展接口。  
- ♿ **无障碍支持**：兼容屏幕阅读器和键盘操作。  
- 📱 **移动端适配**：利用原生选择与编辑功能。  
- ↔️ **双向文本**：支持左右向文字混合输入。  
- 🎨 **语法高亮**：通过颜色区分代码结构。  
- 🔢 **行号显示**：在代码旁显示行号或其他信息。  
- 💡 **自动补全**：提供语言相关的补全提示。  
- 📂 **代码折叠**：可临时隐藏部分代码。  
- 🔍 **搜索替换**：支持正则表达式和替换功能。  
- 🌳 **完整解析**：生成详细语法树以支持语言集成。  
- 🔌 **扩展接口**：支持复杂编辑器扩展。  
- 🧩 **模块化设计**：基于通用公共 API 实现功能。  
- ⚡ **高效性能**：大文档和长行仍保持流畅。  
- 🏷️ **括号自动闭合**：输入时自动匹配括号。  
- ❗ **代码检查**：显示错误和警告信息。  
- 🎭 **灵活样式**：支持混合字体样式和内嵌组件。  
- 🖌️ **主题定制**：可导入或创建自定义主题。  
- 👥 **协作编辑**：多用户同时编辑同一文档。  
- ⏪ **撤销历史**：支持协作编辑的撤销与重做。  
- ✏️ **多选区编辑**：同时编辑多个代码区域。  
- 🌍 **国际化**：支持自定义显示文本。  
- 📜 **开源许可**：采用 MIT 许可证，开发于 GitHub。  
- 💰 **商业支持**：鼓励商业用户资助维护。  
- 🏅 **赞助商**：包括 Holmusk 等公司的支持。  
- 📚 **语言支持**：涵盖 JavaScript、Python 等主流语言，并提供社区维护的扩展包。  
- 🛠️ **社区与支持**：通过论坛交流，问题提交至 issue 跟踪器，遵守行为准则。

---

### [GitHub - uiwjs/react-codemirror: 适用于 React 的 CodeMirror 6 组件。@codemirror https://uiwjs.github.io/react-codemirror/](https://github.com/uiwjs/react-codemirror)

**原文标题**: [GitHub - uiwjs/react-codemirror: CodeMirror 6 component for React. @codemirror https://uiwjs.github.io/react-codemirror/](https://github.com/uiwjs/react-codemirror)

react-codemirror 是一个基于 CodeMirror 6 的 React 组件库，提供了丰富的代码编辑功能和主题定制选项。

- 🚀 快速配置 API，支持 React Hook（需要 React 16.8+）。
- 🌱 使用 CodeMirror 6，支持 TypeScript 编写，提供更好的代码提示。
- 🌐 支持直接在浏览器中使用，提供丰富的示例预览。
- 🎨 支持主题定制，提供主题编辑器。
- 📦 安装简单：`npm install @uiw/react-codemirror --save`。
- 🌍 支持多种语言扩展，如 JavaScript、HTML、CSS、Markdown 等。
- 🔄 提供 Codemirror Merge 组件，用于高亮显示两个版本文件的差异。
- 🎭 支持自定义主题，可以通过 `createTheme` 创建个性化主题。
- 📊 支持通过 `initialState` 从 JSON 序列化中恢复编辑器状态。
- 🔧 开发友好，提供详细的开发指南和相关资源。

---

### [GitHub - marsbos/fluent-state：面向 React 的流畅、响应式且不可变的本地状态管理工具](https://github.com/marsbos/fluent-state)

**原文标题**: [GitHub - marsbos/fluent-state: Fluent, reactive & immutable local state management for React.](https://github.com/marsbos/fluent-state)

一个用于 React 的流畅、响应式和不可变的本地状态管理库。

- 🚀 **安装方式**  
  通过 npm 或 yarn 安装：`npm install fluent-state` 或 `yarn add fluent-state`  

- ⚡ **快速开始**  
  提供简洁的 API 示例，如计数器功能，结合状态和效果。  

- 💡 **设计初衷**  
  旨在替代`useState`、`useReducer`和`useEffect`，提供单一、流畅且响应式的 API，减少样板代码。  

- ✨ **核心特性**  
  - 流畅的 getter/setter API（如`state.user.name("Alice")`）  
  - 不可变更新，兼容 React  
  - 自动追踪的 effects，零样板  
  - 支持嵌套对象和数组  
  - 响应式计算状态（通过`compute`）  
  - 轻量（约 2.4kb）  

- ⚙️ **技术实现**  
  使用 Proxy 代理路径访问函数而非状态对象本身，确保轻量且高效。  

- 🔍 **复杂示例**  
  如待办事项应用，展示嵌套状态和自动依赖追踪的效果。  

- ❓ **常见问题**  
  解答了状态访问函数、不可变更新和 effects 运行机制等疑问。  

- 🛣 **未来计划**  
  包括持久化插件、DevTools 集成、性能优化等。  

- 🤝 **贡献与许可**  
  欢迎贡献，采用 MIT 许可，由 Marcel Bos 开发。

---

### [GitHub - uiwjs/react-md-editor: 一款简单的 Markdown 编辑器，支持预览，基于 React.js 和 TypeScript 实现。](https://github.com/uiwjs/react-md-editor)

**原文标题**: [GitHub - uiwjs/react-md-editor: A simple markdown editor with preview, implemented with React.js and TypeScript.](https://github.com/uiwjs/react-md-editor)

一个基于 React.js 和 TypeScript 实现的简单 Markdown 编辑器，支持预览功能。

- 📝 **功能概述**：提供实时预览、语法高亮、自定义工具栏等功能的 Markdown 编辑器。
- 🔧 **核心特性**：
  - 📑 支持 Tab 键缩进，可自定义缩进大小。
  - ♻️ 基于`textarea`封装，不依赖其他现代编辑器（如 Ace、CodeMirror 等）。
  - 🚧 独立于`uiw`组件库。
  - 🚘 自动列表换行。
  - 😻 支持 GitHub 风格的 Markdown。
  - 🌒 支持暗黑模式（v3.11.0+）。
  - 💡 兼容 Next.js（提供示例）。
  - 📋 支持行复制（Ctrl+D）和移动（Alt+ 上下箭头）（v3.24.0+）。
- 🚀 **快速开始**：
  - 通过`npm i @uiw/react-md-editor`或`yarn add @uiw/react-md-editor`安装。
  - 基本用法示例：
    ```jsx
    import MDEditor from '@uiw/react-md-editor';
    const [value, setValue] = useState("**Hello world!!!**");
    <MDEditor value={value} onChange={setValue} />
    ```
- 🔒 **安全提示**：需对 Markdown 内容进行消毒处理以防止 XSS 攻击（推荐使用`rehype-sanitize`插件）。
- 🛠 **高级功能**：
  - 自定义工具栏（通过`commands`和`extraCommands`属性）。
  - 支持 KaTeX 数学公式渲染（需安装`katex`）。
  - 支持 Mermaid 图表（需安装`mermaid`）。
  - 禁用代码高亮（使用`@uiw/react-md-editor/nohighlight`组件）。
  - 编辑器高度自适应（通过`minHeight`和`visibleDragbar`控制）。
- 🌐 **国际化**：提供中文命令集（`@uiw/react-md-editor/commands-cn`）。
- 📦 **相关项目**：`@uiw/react-markdown-preview`（Markdown 预览组件）、`@uiw/react-codemirror`（代码编辑器）等。
- 📜 **许可证**：MIT License。

---

### [React 的 Markdown 编辑器](https://uiwjs.github.io/react-md-editor/)

**原文标题**: [Markdown Editor for React.](https://uiwjs.github.io/react-md-editor/)

好的，请提供您需要总结的文本内容，我会按照您要求的模板进行整理，包括概述总结和带表情符号的要点列表。  

示例模板：  

概述总结  
- 📌 要点 1  
- 🔍 要点 2  
- 📊 要点 3  

请提供具体文本，我会为您生成符合要求的总结。

---

### [GitHub - igordanchenko/yet-another-react-lightbox: 又一个现代化的 React 灯箱组件](https://github.com/igordanchenko/yet-another-react-lightbox)

**原文标题**: [GitHub - igordanchenko/yet-another-react-lightbox: Modern React lightbox component](https://github.com/igordanchenko/yet-another-react-lightbox)

一个现代的 React 轻量级灯箱组件，支持多种功能和插件，适用于各种图片展示需求。

- 🚀 **项目信息**: 开源项目"yet-another-react-lightbox"，拥有 1.1k 星和 45 个 fork，采用 MIT 许可证。
- ⚛️ **React 支持**: 兼容 React 18、17 和 16.8.0+ 版本。
- 🎨 **用户体验**: 支持键盘、鼠标、触摸板和触摸屏导航。
- 🖼️ **图片预加载**: 确保图片完全下载后才显示，避免部分加载问题。
- ⚡ **性能优化**: 预加载有限数量的图片，平衡性能和用户体验。
- 📱 **响应式设计**: 支持自动分辨率切换的响应式图片。
- 🎥 **视频支持**: 通过插件支持视频幻灯片。
- 🔍 **缩放功能**: 通过插件支持图片缩放。
- 🛠️ **高度可定制**: 可自定义任何 UI 元素或添加自定义幻灯片。
- 📦 **轻量设计**: 仅包含核心功能，通过插件扩展额外功能。
- 📜 **TypeScript 支持**: 内置类型定义。
- 🌍 **RTL 支持**: 兼容从右到左的布局。
- 📚 **文档与示例**: 提供详细文档和示例，帮助快速上手。
- 🔌 **插件系统**: 支持多种插件，如标题、计数器、下载、全屏、内联、分享、幻灯片放映、缩略图、视频和缩放等。
- 📝 **安装与使用**: 通过 npm 安装，提供最小设置示例和推荐设置示例，支持第三方图片组件集成。

---

### [GitHub - software-mansion/react-native-audio-api: 高性能音频引擎](https://github.com/software-mansion/react-native-audio-api)

**原文标题**: [GitHub - software-mansion/react-native-audio-api: High-performance audio engine](https://github.com/software-mansion/react-native-audio-api)

React Native Audio API 是一个基于 Web Audio API 规范的高性能音频引擎，专为 React Native 环境设计，允许开发者以与浏览器相同的方式生成和修改音频。

- 🎵 **高性能音频引擎**：基于 Web Audio API 规范，适用于 React Native 环境。  
- 📚 **文档与安装**：提供详细的[入门指南](docs.swmansion.com/react-native-audio-api/)，帮助开发者快速上手。  
- 🚀 **功能路线图**：包括声音合成、音频文件支持、分析节点、音高校正、麦克风支持等。  
- 🔧 **系统配置**：支持后台模式配置、远程控制和锁屏集成。  
- 📜 **许可证**：采用 MIT 许可证，部分代码源自 Webkit，版权归相关组织所有。  
- 💬 **社区支持**：开发者可通过 Discord 社区反馈意见或提出新想法。  
- 🌟 **项目状态**：拥有 392 个星标、22 个分支，由 Software Mansion 维护。  
- 📂 **代码结构**：主要使用 C++（60.7%）和 TypeScript（17.4%）编写。  
- 📦 **示例应用**：提供示例项目代码，位于 `/apps/common-app` 目录。  
- 🤝 **贡献与支持**：欢迎开发者提交问题或直接联系维护者进行合作。

---

### [发布 5.10.0 版本 · marmelab/react-admin · GitHub](https://github.com/marmelab/react-admin/releases/tag/v5.10.0)

**原文标题**: [Release 5.10.0 · marmelab/react-admin · GitHub](https://github.com/marmelab/react-admin/releases/tag/v5.10.0)

react-admin 项目发布了 v5.10.0 版本，包含多项功能更新、修复和文档改进。

- 🚀 新增 `<ColumnsButton>` 的搜索输入功能，适用于列数较多的情况 (#10848)  
- ⌨️ 为 `<MenuItemLink>` 添加菜单键盘快捷键支持 (#10790)  
- 🛠️ 为页面和引用 MUI 组件添加 `render` 属性 (#10837, #10832)  
- 🔄 新增 `<ReferenceArrayInputBase>` 和 `<ReferenceManyCountBase>` 组件 (#10833, #10808)  
- ✅ 为 `<RadioButtonGroupInput>` 和 `<CheckboxGroupInput>` 添加禁用选项支持 (#10821)  
- 📦 引用字段支持 `empty` 属性 (#10817)  
- ⬆️ 更新 `react-query` 依赖至最低 v5.83 (#10838)  
- 🐛 修复 `useEditController` 未传递所有变量至 `useUpdate` 的问题 (#10839)  
- 📚 文档修复和回溯（RBAC、DatagridAg、Tree 等）(#10840, #10846, #10845, #10847)  
- ⚠️ 注意：升级时可能因 `@tanstack/react-query` 版本冲突导致 TypeScript 或运行时错误，需手动去重锁文件中的依赖

---

### [GitHub - stripe/react-stripe-js: Stripe.js 和 Stripe Elements 的 React 组件](https://github.com/stripe/react-stripe-js)

**原文标题**: [GitHub - stripe/react-stripe-js: React components for Stripe.js and Stripe Elements](https://github.com/stripe/react-stripe-js)

这是一个关于 React Stripe.js 库的 GitHub 仓库页面，提供了 React 组件用于集成 Stripe.js 和 Stripe Elements 支付功能。

- 🚀 **项目概述**: React Stripe.js 是一个用于集成 Stripe.js 和 Stripe Elements 的 React 组件库。
- ⭐ **项目数据**: 1.9k 星标，291 次 fork，MIT 许可证。
- 📚 **文档**: 提供 React Stripe.js 的参考文档和从 react-stripe-elements 迁移的指南。
- 💻 **使用示例**: 提供最小化示例代码，包括使用 hooks 和类组件的实现方式。
- 🔧 **安装**: 通过 npm 安装@stripe/react-stripe-js 和@stripe/stripe-js。
- 🛠 **技术细节**: 支持 TypeScript，类型声明与@stripe/stripe-js 版本同步。
- 🤝 **贡献**: 提供贡献指南，欢迎社区贡献。
- 🔗 **资源**: 包含 README、MIT 许可证、行为准则和安全政策。

---

### [GitHub - wxik/react-native-rich-editor: 轻量级 React Native（JavaScript, H5）富文本编辑器](https://github.com/wxik/react-native-rich-editor)

**原文标题**: [GitHub - wxik/react-native-rich-editor: Lightweight React Native (JavaScript, H5) rich text editor](https://github.com/wxik/react-native-rich-editor)

一个轻量级的 React Native 富文本编辑器，支持 Android 和 iOS 平台，提供丰富的编辑功能和自定义选项。

- 📱 **跨平台支持**：适用于 Android 和 iOS 的 React Native 富文本编辑器。
- 🌐 **在线预览**：提供部分功能的在线演示。
- 📦 **安装简单**：通过 yarn 或 npm 安装，依赖 react-native-webview。
- 🛠 **丰富功能**：支持插入图片、链接、视频，自定义字体，以及多种文本样式（加粗、斜体、下划线等）。
- 🔧 **高度可定制**：提供多种回调函数和样式配置选项，满足不同需求。
- 📜 **MIT 许可证**：开源且免费使用。
- 🌟 **社区活跃**：拥有 886 个星标和 331 个 fork，持续更新和维护。
- 📖 **详细文档**：包含完整的 API 文档和使用示例，便于开发者快速上手。

---

### [Laravel 与 Node.js：Watt 运行环境中的 PHP](https://blog.platformatic.dev/laravel-nodejs-php-in-watt-runtime)

**原文标题**: [Laravel and Node.js: PHP in Watt Runtime](https://blog.platformatic.dev/laravel-nodejs-php-in-watt-runtime)

Laravel 应用现可通过 Platformatic PHP stackable 在 Node.js 的 Watt 运行时中运行，实现 PHP 与 JavaScript 生态的无缝集成。

- 🚀 **核心优势**：允许 Laravel 在 Node.js 进程中运行，减少基础设施分离，共享资源。  
- 🔧 **技术原理**：基于 Rust 的 `@platformatic/php-node` 模块，在 Node.js 内嵌多线程 PHP 运行时，降低延迟。  
- 📦 **快速入门**：  
  - 创建项目目录并初始化 `package.json`。  
  - 配置工作区，添加 Laravel 应用到 `web/laravel`。  
  - 通过 `platformatic.json` 设置文档根目录和 URL 重写规则。  
  - 安装依赖后运行 `npm run dev` 启动。  
- ⚙️ **配置详解**：  
  - `docroot` 指向 Laravel 的 `public` 目录。  
  - `rewriter` 确保请求路由至 `index.php`。  
  - 支持热重载和自定义 PHP 扩展。  
- 🌟 **未来潜力**：统一部署 PHP 与 Node.js 服务、渐进式迁移、多语言微服务架构。  
- 🔍 **进阶功能**：环境变量管理、性能调优、与其他 Platformatic 服务集成。  
- 📚 **资源推荐**：参考 GitHub 示例和官方文档，欢迎社区贡献。

---

### [Bun v1.2.19 | Bun 博客](https://bun.sh/blog/bun-v1.2.19)

**原文标题**: [Bun v1.2.19 | Bun Blog](https://bun.sh/blog/bun-v1.2.19)

Bun 是一个用于构建和测试全栈 JavaScript 和 TypeScript 应用程序的完整工具包。  

- 🚀 **安装 Bun**  
  - 支持多种安装方式：curl、npm、PowerShell、scoop、brew 和 Docker。  

- 🔄 **升级 Bun**  
  - 使用 `bun upgrade` 命令轻松升级。  

- 📦 **改进的 `bun install`**  
  - 新增 `--linker=isolated` 选项，支持类似 pnpm 的隔离和符号链接 `node_modules`，特别适用于 monorepo。  

- 🔍 **交互式依赖更新**  
  - 新增 `bun update --interactive` 命令，帮助选择需要更新的依赖项。  

- 📝 **`package.json` 管理工具**  
  - 新增 `bun pm pkg` 命令，支持 `get`、`set`、`delete` 和 `fix` 子命令，方便自动化管理项目配置。  

- ⚡ **性能优化**  
  - 修复了工作区包多次重新评估的问题，提升了安装速度和可靠性。  

- 🔄 **依赖解析优先级调整**  
  - 调整依赖解析逻辑，优先级为 `devDependencies` > `optionalDependencies` > `dependencies` > `peerDependencies`。  

- 🔕 **`bun pm pack` 新增 `--quiet` 标志**  
  - 抑制冗长输出，仅打印生成的 tarball 文件名，便于脚本处理。  

- 📂 **`.npmrc` 支持**  
  - `bun install` 和 `bun add` 现在支持读取 `.npmrc` 中的 `link-workspace-packages` 和 `save-exact` 设置。  

- ❓ **`bun why` 命令**  
  - 新增 `bun why <package>` 命令，用于追踪依赖链，帮助调试 `node_modules`。  

- 🏗 **顶层 `catalog` 和 `catalogs` 支持**  
  - 现在可以在 `package.json` 的顶层定义 `catalog` 和 `catalogs`，简化配置。  

- 🧪 **VS Code 测试资源管理器集成**  
  - Bun 的 VS Code 扩展现在支持原生 Test Explorer UI，方便测试管理和查看结果。  

- 🤖 **AI 代理优化**  
  - `bun test` 输出在 AI 代理（如 Claude Code）中更加紧凑，节省上下文窗口。  

- 🔧 **`test.each` 变量替换**  
  - 支持在 `test.each` 标题中使用变量替换，提升测试可读性。  

- 🚫 **测试覆盖率忽略文件**  
  - 新增 `test.coveragePathIgnorePatterns` 选项，支持通过 glob 模式忽略文件。  

- 📸 **快照文件链接更新**  
  - 快照文件头部的链接更新为 Bun 官方文档地址。  

- ⚡ **`Bun.sql` 性能提升**  
  - 自动管道化查询，性能提升高达 5 倍。  

- ⏱ **减少首次查询延迟**  
  - 新增 `--sql-preconnect` CLI 标志，提前建立数据库连接以减少首次查询延迟。  

- 🔏 **Windows 代码签名支持**  
  - `bun build --compile` 生成的独立可执行文件现在支持 Authenticode 代码签名。  

- 🚀 **启动优化**  
  - 启动时间减少 1ms，内存使用减少 3MB。  

- 🔍 **`console.log` 深度配置**  
  - 新增 `--console-depth` CLI 标志和 `bunfig.toml` 配置，支持调整对象日志的深度。  

- ⚡ **SIMD 加速多行注释解析**  
  - 使用 SIMD 指令加速大型多行注释的解析。  

- 🌳 **改进的树摇优化**  
  - 支持消除死代码路径中的 `try...catch...finally` 块，减少打包体积。  

- 🔄 **Node.js 兼容性改进**  
  - 支持更多 V8 C++ API，改进 `vm.constants.DONT_CONTEXTIFY` 和 `os.networkInterfaces()` 等功能的兼容性。  

- 🛠 **其他改进和修复**  
  - 修复了 `Bun.which()`、`fetch()`、`Bun.inspect` 等多个运行时和打包工具的 bug。  

- 🙏 **感谢贡献者**  
  - 特别感谢 18 位贡献者的贡献！

---

### [eslint-config-prettier 遭篡改：下载量达 3000 万的 npm 包如何传播恶意软件 —— 安全可信的开源之道](https://safedep.io/eslint-config-prettier-major-npm-supply-chain-hack/)

**原文标题**: [eslint-config-prettier Compromised: How npm Package with 30 Million Downloads Spread Malware — Safe and Trusted Open Source](https://safedep.io/eslint-config-prettier-major-npm-supply-chain-hack/)

eslint-config-prettier 等热门 npm 包遭供应链攻击，通过恶意代码传播窃取软件，影响数百万开发者。

- 🚨 **攻击概述**：eslint-config-prettier 等 npm 包因维护者 JounQin 账号被钓鱼攻击而植入恶意代码，每周下载量达 7800 万次。  
- 📅 **时间线**：7 月 18 日用户发现异常版本，19 日维护者确认账号被盗，20 日 SafeDep 团队介入分析。  
- 💻 **技术细节**：恶意版本通过`install.js`加载 PE32+ 文件`node-gyp.dll`，在 Windows 系统上传播 Scavenger 恶意软件。  
- 🛡️ **防护措施**：SafeDep 工具（如`vet`和`pmg`）可自动检测并阻止恶意包在开发环境、CI/CD 等环节的安装。  
- 🔍 **影响范围**：主要影响 Windows 用户，Linux 和 macOS 不受影响，恶意软件可能窃取文件、凭证等敏感信息。  
- 📢 **后续行动**：已分配 CVE-2025-54313 漏洞编号，建议开发者检查依赖并更新工具防护。

---

### [行为](https://bhvr.dev/)

**原文标题**: [bhvr](https://bhvr.dev/)

现代轻量级开放网络技术栈  

- 🚀 **Bun + Hono + Vite + React**：结合高性能工具链，打造现代轻量级网络应用  
- 🛠️ **快速创建**：通过命令 `bun create bhvr@latest` 一键生成项目  
- 🌐 **开放网络**：专为现代 Web 设计，支持高效开发与部署  
- ⚡ **高性能**：利用 Bun 和 Vite 的快速构建与热更新能力  
- 🔥 **简洁开发**：Hono 提供轻量级后端，React 负责灵活的前端交互

---

### [Hono - 基于 Web 标准的 Web 框架](https://hono.dev/)

**原文标题**: [Hono - Web framework built on Web Standards](https://hono.dev/)

超快速且轻量级的路由器 RegExpRouter，性能卓越，hono/tiny 预设大小不足 14kB，仅使用 Web 标准 API。

- ⚡ 超快速：RegExpRouter 路由器性能极佳  
- 🪶 轻量级：hono/tiny 预设体积小于 14kB  
- 🌐 标准兼容：仅依赖 Web 标准 API 实现

---

### [Vite | 下一代前端工具](https://vite.dev/)

**原文标题**: [Vite | Next Generation Frontend Tooling](https://vite.dev/)

Vite 是一个现代化的前端构建工具，提供快速、高效的开发体验。  

- 🚀 **快速构建** - Vite 利用原生 ES 模块和按需编译，显著提升开发服务器的启动速度。  
- 📚 **多版本文档** - 提供 Vite 2 至 Vite 6 的详细文档，支持开发者查阅不同版本的配置和使用方法。  
- 🌍 **多语言支持** - 文档支持多种语言，包括简体中文、英文、日语、西班牙语等，方便全球开发者使用。  
- 🔌 **插件生态** - 提供丰富的插件系统，开发者可以扩展功能或集成其他工具。  
- 📢 **社区活跃** - 通过 Discord、Mastodon、X（Twitter）等平台保持社区交流，并举办 ViteConf 等活动。  
- 🔄 **持续更新** - 定期发布更新日志（Changelog），鼓励开发者参与贡献（Contributing）。  
- 🎨 **主题定制** - 支持外观（Appearance）调整，适应不同用户的偏好。

---

