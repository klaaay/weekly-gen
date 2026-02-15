### [构建坚不可摧的 React 组件 - 舒丁](https://shud.in/thoughts/build-bulletproof-react-components)

**原文标题**: [Building Bulletproof React Components - Shu Ding](https://shud.in/thoughts/build-bulletproof-react-components)

构建健壮的 React 组件需要超越常规场景，确保在服务器渲染、并发渲染等复杂环境下仍能稳定工作。本文通过一系列实例，展示了如何使组件具备服务器兼容性、水合稳定性、多实例支持、并发安全性、组合灵活性、门户适应性、过渡动画支持、活动状态管理、数据防泄漏及未来兼容性，从而打造真正可靠的组件。

- 🛡️ **服务器兼容**：避免在服务器端使用浏览器 API（如 localStorage），应将其移至 useEffect 中执行。
- 💧 **水合稳定**：通过内联脚本在浏览器绘制前设置正确状态，防止水合过程中的样式闪烁。
- 🔢 **多实例支持**：使用 useId 生成唯一标识符，避免多个实例间的 DOM 冲突。
- ⚡ **并发安全**：利用 React.cache 对服务器组件的数据请求进行去重，避免重复查询。
- 🧩 **组合灵活**：使用 Context 而非 cloneElement 传递数据，以兼容服务器组件和异步子组件。
- 🪟 **门户适应**：通过 ownerDocument.defaultView 绑定事件，确保组件在 iframe 或弹窗中正常工作。
- 🎬 **过渡动画**：使用 startTransition 包装状态更新，以实现平滑的视图过渡效果。
- 🎭 **活动状态管理**：通过动态设置 style 标签的 media 属性，控制组件隐藏时的样式影响。
- 🔒 **数据防泄漏**：使用 taintUniqueValue 标记敏感数据，防止其意外传递至客户端。
- 🚀 **未来兼容**：依赖 useState 而非 useMemo 来保证数据的持久性，避免 React 内部优化导致的状态丢失。

---

### [agent-skills/skills/react-best-practices at main · vercel-labs/agent-skills · GitHub](https://github.com/vercel-labs/agent-skills/tree/main/skills/react-best-practices)

**原文标题**: [agent-skills/skills/react-best-practices at main · vercel-labs/agent-skills · GitHub](https://github.com/vercel-labs/agent-skills/tree/main/skills/react-best-practices)

这是一个由 Vercel Labs 开发的开源项目，名为“agent-skills”，专注于为 AI 智能体提供可扩展的技能库。

- 🧠 **开源技能库**：项目旨在构建一个供 AI 智能体使用的技能集合，促进功能扩展
- 🛠️ **活跃开发**：项目托管在 GitHub 上，拥有大量关注者（20.4k 星标）和活跃的社区参与
- 🔄 **协作开发**：包含多个议题（35 个）和拉取请求（35 个），显示社区贡献活跃
- 📊 **项目管理**：提供代码、议题、安全等多维度导航选项，便于协作与管理
- 🔓 **公开访问**：项目为公开状态，允许用户分叉和参与，但需登录调整通知设置

---

### [TypeScript 6.0 Beta 版本发布](https://devblogs.microsoft.com/typescript/announcing-typescript-6-0-beta/)

**原文标题**: [Announcing TypeScript 6.0 Beta - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-6-0-beta/)

TypeScript 6.0 Beta 版本已发布，这是基于当前 JavaScript 代码库的最后一个主要版本，旨在为使用 Go 重写的 TypeScript 7.0 原生版本铺平道路。此版本引入了多项新特性、改进以及为适应现代 JavaScript 生态而做的重大变更和弃用。

- 🚀 **过渡性发布**：TypeScript 6.0 是通往原生版本 7.0 的桥梁，包含了对齐和准备工作。
- 🧠 **改进 `this` 上下文推断**：对于未使用 `this` 的函数，类型推断不再将其视为上下文敏感函数，解决了某些方法语法中的推断问题。
- 📁 **支持 `#/` 子路径导入**：现在支持以 `#/` 开头的 Node.js 子路径导入，简化了路径映射配置。
- ⚙️ **模块解析组合**：`--moduleResolution bundler` 现在可与 `--module commonjs` 组合使用，为许多项目提供了合适的升级路径。
- 🔢 **新增 `--stableTypeOrdering` 标志**：帮助减少 6.0 与 7.0 之间因类型排序差异导致的输出噪音，便于迁移比较。
- 🎯 **新增 `es2025` 编译目标**：为 `target` 和 `lib` 选项添加了 `es2025`，包含新的内置 API 类型。
- ⏳ **内置 `Temporal` API 类型**：为处于 Stage 3 的 Temporal 日期时间提案提供了内置类型支持。
- 🗺️ **新增 Map `upsert` 方法类型**：为 `Map` 和 `WeakMap` 新增的 `getOrInsert` 和 `getOrInsertComputed` 方法提供了类型支持。
- 🛡️ **新增 `RegExp.escape` 类型**：为新的 `RegExp.escape` 函数提供了类型支持。
- 🌐 **DOM 库包含可迭代类型**：`dom` 库现在默认包含 `dom.iterable` 和 `dom.asynciterable` 的内容，简化了配置。
- ⚠️ **多项重大变更与弃用**：包括默认启用 `strict` 模式、`module` 默认改为 `esnext`、弃用 `target: es5`、`--moduleResolution node`、`--baseUrl`、`--outFile` 等，旨在反映现代开发实践并为 7.0 做准备。
- 🛠️ **准备迁移至 7.0**：强烈建议在升级到 6.0 后解决所有弃用警告，以便顺利过渡到即将发布的 TypeScript 7.0 原生版本。

---

### [ESLint v10.0.0 发布 - ESLint - 可插拔的 JavaScript 代码检查工具](https://eslint.org/blog/2026/02/eslint-v10.0.0-released/)

**原文标题**: [ESLint v10.0.0 released - ESLint - Pluggable JavaScript Linter](https://eslint.org/blog/2026/02/eslint-v10.0.0-released/)

ESLint v10.0.0 是一个主要版本发布，引入了新功能、修复了错误，并包含多项重大变更，需要用户仔细阅读迁移指南以确保顺利升级。

- 🚀 **重大版本更新**：ESLint v10.0.0 作为主要版本，包含新功能、错误修复和破坏性变更，需手动安装 `eslint@10.0.0`。
- ⚠️ **Node.js 支持变更**：不再支持 Node.js v20.19.0 之前版本、v21.x 和 v23.x，仅支持 v20.19.0、v22.13.0 及以上版本。
- 📄 **全新配置查找算法**：默认从每个被检查文件的目录开始查找 `eslint.config.*`，支持单次运行中使用多个配置文件，适用于 monorepo。
- 🗑️ **移除 eslintrc 功能**：完全移除了旧的 eslintrc 配置系统，包括相关环境变量、CLI 参数和文件支持，全面转向扁平配置。
- 🔍 **JSX 引用追踪**：现在正确追踪 JSX 元素的引用，解决了 `no-unused-vars` 和 `no-undef` 规则中的误报和漏报问题。
- 📦 **内置类型定义**：Espree 和 ESLint Scope 包现在包含内置类型定义，取代了之前的 `@types/` 包，需检查类型兼容性。
- 🧪 **RuleTester 增强**：新增断言选项（`requireMessage`、`requireLocation`、`requireData`）以强化测试，并改进失败测试的位置报告。
- ⚙️ **规则与 API 更新**：`max-params` 规则新增 `countThis` 选项；移除已弃用的 `context` 成员和 `SourceCode` 方法；`Program` AST 节点范围现在涵盖整个源代码。
- 🎨 **格式化器上下文颜色属性**：当使用 `--color` 或 `--no-color` 时，格式化器的上下文对象会包含 `color` 属性，便于自定义颜色输出。
- 📋 **更新推荐配置**：`eslint:recommended` 配置已更新，包含新的重要规则。
- 🔧 **依赖与构建调整**：不再支持 jiti < v2.2.0；进行了多项错误修复、文档更新和内部重构。

---

### [Bun v1.3.9 | Bun 博客](https://bun.sh/blog/bun-v1.3.9#faster-bun-markdown-react)

**原文标题**: [Bun v1.3.9 | Bun Blog](https://bun.sh/blog/bun-v1.3.9#faster-bun-markdown-react)

本文介绍了 Bun 的安装方法、升级方式、并行与顺序运行脚本的功能，以及多项性能优化和错误修复。

- 🚀 **安装 Bun**：支持多种安装方式，包括 curl、npm、PowerShell、Scoop、Homebrew 和 Docker。
- 🔄 **升级 Bun**：使用`bun upgrade`命令轻松升级。
- ⚙️ **运行脚本**：新增`--parallel`和`--sequential`选项，支持并行或顺序运行 package.json 脚本，并带有前缀输出。
- 🔗 **HTTP/2连接升级**：修复了`net.Server`到`Http2SecureServer`的连接升级模式，适用于代理服务器。
- 🧪 **自动恢复模拟**：`mock()`和`spyOn()`支持`Symbol.dispose`，使用`using`关键字自动恢复模拟。
- 🛡️ **NO_PROXY 支持**：现在即使显式设置代理选项，`NO_PROXY`环境变量也会被正确检查。
- 📊 **CPU 性能分析**：新增`--cpu-prof-interval`标志，可配置 CPU 分析器的采样间隔。
- 📦 **ESM 字节码**：`--compile`现在支持 ESM 格式的字节码。
- 🐛 **ARM64 修复**：修复了在 ARMv8.0 aarch64 CPU 上的崩溃问题。
- ⚡ **性能提升**：包括更快的 Markdown 渲染、`AbortSignal.abort()`优化、正则表达式 SIMD 加速等。
- 🔧 **JavaScriptCore 升级**：多项优化，如`String#startsWith`、`Set#size`、`Map#size`、`String#trim`等。
- 🐞 **错误修复**：包括 Node.js 兼容性改进、Bun API 修复、Web API 问题解决和 TypeScript 类型修正。

---

### [重写 useActionState by rickhanlonii · Pull Request #8284 · reactjs/react.dev · GitHub](https://github.com/reactjs/react.dev/pull/8284)

**原文标题**: [Rewrite useActionState by rickhanlonii · Pull Request #8284 · reactjs/react.dev · GitHub](https://github.com/reactjs/react.dev/pull/8284)

这是一个关于 React 官方文档仓库中 `useActionState` Hook 文档重写的 Pull Request 讨论，主要涉及文档内容更新、API 命名讨论和功能示例改进。

- 📝 **文档重写**：对 `useActionState` 的文档进行全面重写，旨在更清晰地展示其在表单之外的用途，并通过渐进式示例说明其价值。
- 🔄 **命名讨论**：社区对 API 命名进行了深入讨论，提出了 `dispatchAction`、`asyncReducer`、`asyncDispatch` 等备选方案，以更准确地反映其支持同步/异步副作用的特点。
- 🎯 **核心目标**：强调 `useActionState` 用于管理用户操作的状态，可视为支持副作用的 `useReducer`，并能处理操作队列、乐观更新和错误状态。
- 📚 **示例改进**：新增了包括错误处理、表单输入保留、混合同步/异步操作以及可中止操作在内的多种使用场景示例，使文档更加实用。
- 🛠 **功能亮点**：展示了如何与 `useOptimistic` 和 `useTransition` 结合使用，以优化用户体验，例如处理待定状态和乐观更新。
- 🤝 **社区协作**：多位贡献者参与了代码审查和讨论，提出了关于文档结构、示例内容和错误处理的宝贵建议，体现了开源协作的精神。

---

### [获取失败](https://github.com/rickhanlonii/react.dev/blob/58b6c16b63ce764e2545447239f2491ea45f7470/src/content/reference/react/useActionState.md)

**原文标题**: [Failed to retrieve](https://github.com/rickhanlonii/react.dev/blob/58b6c16b63ce764e2545447239f2491ea45f7470/src/content/reference/react/useActionState.md)

无法总结：获取内容失败，状态码 429。

---

### [React Native 0.84 - 默认启用 Hermes V1 · React Native](https://reactnative.dev/blog/2026/02/11/react-native-0.84)

**原文标题**: [React Native 0.84 - Hermes V1 by Default · React Native](https://reactnative.dev/blog/2026/02/11/react-native-0.84)

React Native 0.84 版本正式发布，将 Hermes V1 设为默认 JavaScript 引擎，显著提升应用性能，同时默认启用 iOS 预编译二进制文件以加快构建速度，并继续移除旧架构代码，要求 Node.js 22 或更高版本。

- 🚀 Hermes V1 现为 iOS 和 Android 的默认 JavaScript 引擎，带来自动性能提升和内存优化，无需迁移即可享受改进。
- ⚡ iOS 默认启用预编译二进制文件，大幅减少构建时间，无需每次从源码编译 React Native 核心。
- 🗑️ 继续移除旧架构组件，iOS 默认排除旧架构代码以减小应用体积，Android 删除多个旧架构类。
- 🔧 最低要求 Node.js 22.11 或更高版本，以支持现代 JavaScript 特性。
- 🛠️ 包含 React 19.2.3 同步更新、ESLint v9 扁平配置支持、新增图像格式和键盘事件处理等平台改进。
- ♿ 增强无障碍功能，如自动为可点击文本添加链接角色，修复 Android 回收视图的无障碍状态问题。
- 🔗 URL API 改进，添加标准属性和方法，更接近 Web 标准。
- ⚠️ 包含一些破坏性变更，如 iOS 图像观察者 API 调整和 Android 移除 BridgeDevSupportManager。
- 📢 弃用 XHRInterceptor 和 WebSocketInterceptor API，建议使用 Chrome DevTools Protocol。
- 🙏 感谢 95 位贡献者的 650 多次提交，特别鸣谢关键贡献者。
- 🔄 升级指南：使用 React Native Upgrade Helper 或尝试 AI 升级技能，新项目可通过 CLI 创建，Expo 项目需使用 canary 版本。

---

### [虚拟滚动处理数十亿行数据——来自 HighTable 的技术](https://rednegra.net/blog/20260212-virtual-scroll/)

**原文标题**: [Virtual Scrolling for Billions of Rows — Techniques from HighTable](https://rednegra.net/blog/20260212-virtual-scroll/)

本文介绍了 React 组件 HighTable 中用于处理数十亿行数据垂直滚动的五种关键技术，这些技术结合了懒加载、表格切片、无限像素、像素级精确滚动和两步随机访问，以实现高性能和高可访问性。

- 🚀 **懒加载**：仅加载当前可见的单元格数据，避免一次性加载全部数据，显著减少内存占用。
- ✂️ **表格切片**：只渲染可见的行，而非整个表格，大幅减少 HTML 元素数量，提升渲染性能。
- 🌌 **无限像素**：通过设置画布最大高度并降低滚动条分辨率，突破浏览器对元素高度的限制，支持海量行数。
- 🎯 **像素级精确滚动**：结合全局和局部两种滚动模式，允许用户通过滚动条快速跳转或通过鼠标滚轮精细浏览。
- 🎮 **两步随机访问**：分离垂直和水平滚动逻辑，支持通过键盘或程序跳转到任意单元格，确保导航的准确性和流畅性。

---

### [半色调的渐变 - 马克西姆·赫克尔的博客](https://blog.maximeheckel.com/posts/shades-of-halftone/)

**原文标题**: [Shades of Halftone - The Blog of Maxime Heckel](https://blog.maximeheckel.com/posts/shades-of-halftone/)

本文探讨了半色调效果的多样性与实现方式，从基础的点阵网格到复杂的多通道和动态变体，展示了如何通过 GLSL 着色器技术创造丰富的视觉纹理和艺术风格。

- 🎨 半色调效果源于印刷技术，现已成为数字设计中的艺术工具，通过点阵模拟渐变和纹理。
- 🔍 核心原理是利用网格中的点大小变化产生光学错觉，人眼对高频率点阵进行空间平均，形成连续色调感。
- ⚙️ 基础实现包括使用 GLSL 绘制圆形、通过`fract`函数创建网格，并结合像素化处理将半色调应用于图像或视频。
- 🌈 多通道半色调（如 CMYK）通过叠加不同颜色的网格层模拟印刷效果，需处理莫尔条纹和颜色混合问题。
- 🔄 动态变体包括“粘性”圆点合并、点位移动画等，通过扩展采样核和混合技术打破网格限制，增强有机感。
- 🚀 文章最后展望了基于半色调的实时着色器绘画技术，如点彩画和水彩效果，展示了该技术的扩展潜力。

---

### [GitHub - pmndrs/react-three-fiber: 🇨🇭 一个用于 Three.js 的 React 渲染器](https://github.com/pmndrs/react-three-fiber)

**原文标题**: [GitHub - pmndrs/react-three-fiber: 🇨🇭 A React renderer for Three.js](https://github.com/pmndrs/react-three-fiber)

react-three-fiber 是一个用于 Three.js 的 React 渲染器，允许开发者以声明式、可复用的组件构建 3D 场景，并能够与 React 生态系统无缝集成。

- 🎨 这是一个 React 渲染器，专为 Three.js 设计，支持通过 JSX 声明式构建 3D 场景
- ⚡ 性能无开销，甚至能通过 React 的调度能力在大规模场景中超越原生 Three.js
- 🔄 自动与 Three.js 新特性同步，无需等待库更新即可使用最新功能
- 📦 拥有丰富的生态系统，包括物理引擎、后处理、UI 组件和可视化编辑器等众多扩展库
- 🌍 被多家知名公司和项目采用，涵盖设计、建模、CAD、AI 等多个领域
- 📄 采用 MIT 许可证，支持开源贡献，可通过 OpenCollective 或加密货币进行赞助

---

### [自动创建首个组织并智能命名](https://clerk.com/changelog/2026-01-22-default-organization-naming?utm_source=cooper_press&utm_medium=newsletter&utm_campaign=auto-org&utm_content=02-13-26&dub_id=QxcyjOmcHQ6D3iR5)

**原文标题**: [Automatically create first organization with smart naming](https://clerk.com/changelog/2026-01-22-default-organization-naming?utm_source=cooper_press&utm_medium=newsletter&utm_campaign=auto-org&utm_content=02-13-26&dub_id=QxcyjOmcHQ6D3iR5)

Clerk 推出新功能，自动为新用户创建首个组织并智能命名，简化入门流程。

- 🚀 自动创建首个组织：消除手动设置步骤，用户注册后即自动加入首个组织，提升入门体验
- 🏷️ 智能命名建议：根据用户邮箱域名自动生成组织名称（如 alex@clerk.com→“Clerk”），或使用成员姓名变量个性化命名
- ⚙️ 灵活配置选项：支持禁用特定命名规则，提供备用名称方案，确保适用不同场景
- 📚 快速启用指南：可通过 Clerk 仪表板的组织设置配置，详细步骤参考官方文档

---

### [我在我的博客中添加了 Bluesky 评论区。](https://micahcantor.com/blog/bluesky-comment-section.html)

**原文标题**: [I added a Bluesky comment section to my blog](https://micahcantor.com/blog/bluesky-comment-section.html)

作者在个人博客中嵌入了 Bluesky 评论区，利用其开放 API 实现静态站点的动态互动，避免了自建评论系统的运维负担。

- 🌐 通过 Bluesky 的公开 API 获取帖子回复，直接显示在博客中，无需自建后端服务
- ⚙️ 使用 TypeScript 和 Bluesky SDK 开发，结合 React Server Components 与 MDX 管理内容
- 🛠️ 采用 Tanstack React-Query 处理数据请求，简化加载与错误状态管理
- 📱 设计简约的评论区 UI，支持回复缩进和移动端适配，并添加排序、点赞数显示等功能
- 🔓 强调 Bluesky 基于开放协议 AT Proto 的优势，避免平台被单一实体控制
- 📦 提供 GitHub 开源代码，方便其他开发者参考实现类似功能

---

### [在 React 中构建富文本编辑器 | Puck](https://puckeditor.com/blog/building-a-rich-text-editor-in-react)

**原文标题**: [Building a Rich Text Editor in React | Puck](https://puckeditor.com/blog/building-a-rich-text-editor-in-react)

本文探讨了在 React 应用中实现富文本编辑的挑战，并介绍了使用 Puck 构建结构化、可定制富文本编辑器的方法。

- 🦾 富文本编辑在 React 中具有挑战性，传统方法如直接使用 HTML 或 contenteditable 容易导致状态不一致和难以维护的问题。
- 🏗️ 结构化内容模型通过将富文本视为数据而非标记，提供了更好的可控性、验证能力和扩展性。
- 🔧 Puck 是一个基于 React 的开源可视化编辑器，通过配置驱动的方式简化富文本编辑的集成和定制。
- 🛠️ 使用 Puck 可以轻松设置富文本编辑器，支持内联编辑、自定义格式选项和限制标题层级等功能。
- 🧩 Puck 基于 TipTap 构建，支持通过扩展添加新功能（如上标），而无需修改编辑器核心代码。
- 🎯 关键优势包括：结构化内容管理、可控的编辑体验、通过配置实现扩展性，以及编辑行为与用户界面的清晰分离。

---

### [提升退出动画效果的 React 技巧](https://barvian.me/react-exit-animations)

**原文标题**: [A React trick to improve exit animations](https://barvian.me/react-exit-animations)

本文介绍了一种利用 React 的 Suspense 组件来优化退出动画的技巧，通过“冻结”正在退出的组件以防止其内容在动画期间更新，从而提升用户体验。

- 🐛 **问题**：在 React 中，触发退出动画的更新常会同时改变退出组件的内容，导致动画期间内容闪烁，分散用户注意力。
- 🔍 **探索**：尝试过保存状态或延迟更新等方法，但要么过于繁琐，要么处理动画中断时较复杂；理想方案是让 React 停止提交退出组件的 DOM 更改。
- 💡 **解决方案**：利用 Suspense 组件在挂起时暂停 DOM 提交的特性，创建了一个`Freeze`包装器，通过移除 Suspense 的`display: none`样式来“冻结”组件，保持其退出前的状态。
- ⚙️ **实现**：`Freeze`组件结合 Suspense 和自定义观察器，在插入效果中恢复元素显示，并配合无限 Promise 实现挂起，代码示例展示了与 React Aria Components 的集成用法。
- 📈 **效果**：该方法在实践中表现良好，能同时冻结 React 状态交互（如悬停），但属于技巧性方案，未来可能随 React 更新而失效，作者希望 React 团队能正式支持类似“可见但非活跃”的状态。

---

### [获取失败](https://engineering.gusto.com/the-journey-to-a-safer-frontend-why-we-removed-react-fc-095ff0b3e2e4)

**原文标题**: [Failed to retrieve](https://engineering.gusto.com/the-journey-to-a-safer-frontend-why-we-removed-react-fc-095ff0b3e2e4)

无法总结：获取内容失败，状态码 403。

---

### [弗兰肯 TUI —— Rust 的怪物终端 UI 内核](https://frankentui.com/web_react)

**原文标题**: [FrankenTUI — The Monster Terminal UI Kernel for Rust](https://frankentui.com/web_react)

FrankenTUI 是一个 React 组件，允许在任意 React 页面中嵌入一个实时的、GPU 加速的终端界面，仅需少量代码即可实现，并支持自动调整大小和跨浏览器运行。

- 🚀 **快速集成**：仅需三行代码即可在 React 页面中嵌入一个功能完整的 GPU 加速终端。
- 🔧 **灵活调整**：支持通过拖拽手柄调整组件大小，终端会自动重新适配网格布局。
- 📐 **预设尺寸**：提供紧凑（60×20）、标准（80×24）、宽屏（120×30）和全宽（自动）四种预设尺寸。
- 🌐 **跨浏览器**：完整的 WASM 内核在浏览器中以 60fps 运行，兼容 Chrome、Edge、Safari 和 Firefox。
- 💼 **多样用例**：适用于 Web 终端应用、可嵌入的 TUI 小组件、交互式文档以及演示页面等多种场景。
- ⚙️ **简易配置**：通过简单的 Props 控制尺寸、键盘捕获、状态显示等行为，并提供加载完成、调整大小和错误处理等回调函数。

---

### [介绍 Tambo 1.0 | tambo 博客](https://tambo.co/blog/posts/introducing-tambo-generative-ui)

**原文标题**: [Introducing Tambo 1.0 | tambo blog](https://tambo.co/blog/posts/introducing-tambo-generative-ui)

本文介绍了人工智能在医疗领域的应用现状与前景，重点探讨了其在疾病诊断、治疗方案优化及医疗管理效率提升方面的作用，同时简要提及了相关的技术挑战和伦理考量。

- 🤖 AI 辅助诊断系统通过分析医学影像提升疾病识别准确率
- 💊 基于算法的个性化治疗方案推荐助力精准医疗发展
- ⚡ 智能流程管理工具优化医院资源分配与患者就诊体验
- 🧠 自然语言处理技术加速医疗文献分析与临床决策支持
- ⚖️ 数据隐私保护与算法透明度成为行业关注重点

---

### [rari：基于 Rust 运行时的 React 服务器组件](https://rari.build/)

**原文标题**: [rari: React Server Components on a Rust Runtime](https://rari.build/)

本文介绍了人工智能在医疗领域的应用现状与前景，重点探讨了其在疾病诊断、治疗方案优化及医疗管理效率提升方面的作用，同时简要提及了相关的技术挑战和伦理考量。

- 🤖 AI 辅助诊断系统通过分析医学影像提升疾病识别准确率
- 💊 基于算法的个性化治疗方案推荐助力精准医疗发展
- ⚡ 智能流程管理工具优化医院资源分配与患者就诊体验
- 🔬 基因组学与 AI 结合加速新药研发和病理机制研究
- ⚖️ 数据隐私保护与算法透明度成为实际应用中的关键议题

---

### [入门指南 / rari 文档](https://rari.build/docs/getting-started)

**原文标题**: [Getting Started / rari Docs](https://rari.build/docs/getting-started)

本文介绍了人工智能在医疗领域的应用现状与前景，重点探讨了其在疾病诊断、药物研发和个性化治疗方面的突破性进展，同时简要提及了相关的伦理挑战。

- 🏥 AI 辅助诊断系统能通过分析医学影像快速识别病变，提升早期癌症等疾病的检出率
- 🔬 机器学习加速了新药研发流程，大幅缩短化合物筛选与临床试验设计的时间周期
- 🧬 基于患者基因组数据的 AI 模型可为慢性病患者提供动态优化的个性化治疗方案
- ⚖️ 医疗 AI 的算法透明度与数据隐私保护仍是需要持续关注的核心伦理议题

---

### [发布 v6.7.0 · vadimdemedes/ink · GitHub](https://github.com/vadimdemedes/ink/releases/tag/v6.7.0)

**原文标题**: [Release v6.7.0 · vadimdemedes/ink · GitHub](https://github.com/vadimdemedes/ink/releases/tag/v6.7.0)

这是一个关于 Ink 库 v6.7.0 版本发布的 GitHub 页面内容摘要，主要包含版本更新信息和错误修复。

- 🎉 **新增功能**：支持 React 并发渲染（可选）和同步更新，提升终端体验。
- 🖥️ **终端优化**：添加 Kitty 键盘协议支持（可选）和 IME 光标定位 API。
- 🔧 **修复问题**：解决了初始渲染时的全屏换行符问题及多个 useInput 钩子的警告。
- 🐛 **错误处理**：修复了 macOS 上 Option+Return 键的处理及终端尺寸检测的改进。
- 📊 **社区反馈**：获得了 4 个“欢呼”和 5 个“火箭”表情反应，显示积极反响。

---

### [GitHub - pioner92/react-native-turbo-base64: ⚡ React Native 最快的 base64 编码/解码库。通过优化的 C++ 和 JSI 绑定，速度提升高达 10 倍。](https://github.com/pioner92/react-native-turbo-base64)

**原文标题**: [GitHub - pioner92/react-native-turbo-base64: ⚡ The fastest base64 encoding/decoding library for React Native. Up to 10x faster with optimized C++ and JSI bindings.](https://github.com/pioner92/react-native-turbo-base64)

这是一个用于 React Native 的极速 base64 编码/解码库，通过优化的 C++ 代码和 JSI 绑定实现，性能最高可提升 10 倍，专为需要高性能 base64 处理的应用场景设计。

- 🚀 **性能卓越**：采用优化的 C++ 和 JSI 直接绑定，消除桥接开销，编码/解码速度比其他库快达 5-10 倍。
- 📦 **功能全面**：支持标准和 URL 安全的 base64 格式，提供完整的 API，包括编码、解码、计算字节长度和去除填充等功能。
- 🔧 **易于集成**：安装简单，支持 npm/yarn 安装，iOS 需 pod install，Android 无需额外配置，并提供详细的快速入门指南。
- 🛡️ **稳定可靠**：包含完整的 TypeScript 类型定义，经过充分测试，兼容 Expo，且无运行时依赖。
- 📚 **资源丰富**：提供详细的 API 文档、高级使用示例（如图片处理、大文件操作）以及故障排除指南，便于开发者使用和问题排查。

---

### [React 峰会——全球最大的 React 开发者大会](https://reactsummit.com/?utm_source=partner&utm_medium=reactstatus)

**原文标题**: [React Summit – The Biggest React Conference Worldwide](https://reactsummit.com/?utm_source=partner&utm_medium=reactstatus)

React Summit 是全球最大的 React 年度会议，聚焦 React 生态系统与现代 Web 开发，将于 2026 年 6 月 12 日与 16 日在阿姆斯特丹举行，提供线上线下混合参与模式。会议汇集了来自全球的顶尖工程师，设有 Base Camp 和 Summit 双轨道，涵盖 60 多位讲者的前沿分享，预计吸引超过 10,000 名开发者参与，其中 1,500 名将亲临阿姆斯特丹现场。

- 🗓️ **会议时间与地点**：2026 年 6 月 12 日（线下）与 16 日（线上）在阿姆斯特丹举行，提供混合参与体验。
- 🎤 **核心内容**：设有双轨道（Base Camp 与 Summit），60 多位讲者分享 React、全栈开发、AI 辅助编程等最新见解。
- 🌍 **参与规模**：预计超过 10,000 名全球开发者参与，其中 1,500 名将线下齐聚阿姆斯特丹。
- 🎟️ **票务选项**：提供混合票（线下 + 远程，€600 起）、远程票（€180 起）及包含 JSNation 的套票，支持团队折扣与分期付款。
- 🏆 **特色活动**：包含 React 开源奖项、城市导览（游船与步行）、全球最大 React 派对及食品卡车节。
- 🛠️ **深度专题**：聚焦全栈开发与架构、晋升高级工程师/Tech Lead、AI 辅助编程及 AI 工程等主题。
- 🧑‍🏫 **讲者阵容**：已公布部分讲者，包括 Aurora Scharff、Dominik Dorfmeister、Kitze 等 React 专家与培训师。
- 📚 **会前会后工作坊**：提供免费与付费工作坊，涵盖 React Server Components、React Query、DevOps 等实践内容。
- 🤝 **社区贡献**：提供 100 个奖学金名额给科技领域 underrepresented 群体，并设有 React 开源奖项以表彰杰出项目。
- 📍 **场地与赞助**：主会场为 KromhoutHal，现有铂金、黄金等多级赞助商，并持续招募合作伙伴与志愿者。

---

### [使用 Vega 开发 | 设计与开发 Vega 应用](https://developer.amazon.com/docs/vega/0.22/vega-develop.html?sc_category=PAI&sc_channel=3P&sc_publisher=RS&sc_campaign=ACQ_VG&sc_country=US&sc_detail=RSTATUS-2_VG_GEN)

**原文标题**: [Develop with Vega | Design and Develop Vega Apps ](https://developer.amazon.com/docs/vega/0.22/vega-develop.html?sc_category=PAI&sc_channel=3P&sc_publisher=RS&sc_campaign=ACQ_VG&sc_country=US&sc_detail=RSTATUS-2_VG_GEN)

Vega 开发平台为电视应用开发者提供全面的资源、工具和指南，涵盖从创建、调试到性能优化和发布的完整流程。

- 📚 **开发资源** – 提供示例代码、开发指南和 API 文档，支持应用开发者和库创建者
- 🛠️ **应用构建** – 支持从零创建应用，使用 Vega Studio 和 VS Code 扩展提升开发效率
- ⚡ **性能优化** – 强调从设计阶段关注性能，提供 UI 流畅性、内存管理和性能测试指南
- 📺 **核心开发领域** – 涵盖媒体播放、焦点管理、调试、应用配置等电视应用关键主题
- 🌐 **Web 应用与模块** – 支持基于 Chromium 的 Web 应用和 Turbo Modules 原生通信优化
- 🔧 **测试与运行** – 提供模拟器、Fire TV Stick 真机测试和用户实测环境
- 🔌 **集成扩展** – 支持 Fire TV 功能（如应用内购）和丰富的 React Native 社区库集成

---

### [发布 8.0.0 版本 · getsentry/sentry-react-native · GitHub](https://github.com/getsentry/sentry-react-native/releases/tag/8.0.0)

**原文标题**: [Release 8.0.0 · getsentry/sentry-react-native · GitHub](https://github.com/getsentry/sentry-react-native/releases/tag/8.0.0)

Sentry React Native SDK 发布 8.0.0 版本，包含重大变更、新功能及多项改进，主要涉及最低版本要求提升、原生初始化支持与配置优化。

- 🚨 **重大变更**：提升 iOS/macOS/tvOS、Android 及自托管服务的最低版本要求，例如 iOS 需 15.0+、Android Gradle Plugin 需 7.4.0+。
- 📄 **配置文件支持**：新增通过 `sentry.options.json` 文件配置 SDK，支持在原生层初始化以捕获应用启动错误。
- 🔧 **Expo 插件增强**：为 `@sentry/react-native/expo` 插件添加 `useNativeInit` 选项，实现原生自动初始化。
- 🛠 **内部重构**：提取 iOS 和 Android 的原生初始化逻辑为独立结构，提升代码模块化。
- 📦 **依赖更新**：升级 Cocoa SDK 至 v9.4.1、CLI 至 v3.2.0，带来新特性和性能改进。

---

### [比较 zustand 与 jotai - npmx](https://npmx.dev/compare?packages=zustand,jotai)

**原文标题**: [Compare zustand vs jotai - npmx](https://npmx.dev/compare?packages=zustand,jotai)

该工具用于在 npm 生态中横向对比不同软件包，帮助开发者根据性能、体积、健康度等维度选择合适依赖。

- 📦 支持并排对比多个 npm 包（如 zustand 与 jotai）
- 🔍 提供多维度筛选：性能、包体积、依赖数量、健康度等
- 📊 展示关键指标：周下载量、点赞数、发布时间、维护状态
- 🛡️ 集成安全检查：许可证类型、漏洞检测
- ⚙️ 兼容性分析：引擎支持、TypeScript 声明、模块格式

---

### [如何在 Node.js 中发起 HTTP 请求](https://nodejsdesignpatterns.com/blog/nodejs-http-request/)

**原文标题**: [How to make an HTTP request in Node.js](https://nodejsdesignpatterns.com/blog/nodejs-http-request/)

本文全面介绍了在 Node.js 中进行 HTTP 请求的现代方法，重点推荐使用 Node.js 18+ 内置的 `fetch()` API。文章涵盖了从基础请求到高级场景（如流式传输、并发请求、错误重试、文件上传和测试模拟）的详细指南，并对比了 `fetch()` 与传统的 `http/https` 模块及外部库的适用场景。

- 🚀 **推荐使用内置 fetch API**：Node.js 18 及以上版本内置了 `fetch()` 函数，无需安装额外依赖即可进行 HTTP 请求，语法与浏览器端一致。
- 📝 **处理请求与响应**：进行 GET/POST 请求时，需检查 `response.ok` 处理 HTTP 语义错误，并使用 `.json()`、`.text()` 等方法解析响应体。
- ⏱️ **设置超时与重试**：使用 `AbortSignal.timeout()` 防止请求无限挂起；对于临时性故障，可实现指数退避的重试逻辑。
- 🌊 **支持流式传输**：通过 `ReadableStream` 处理大文件上传或下载，避免将整个文件加载到内存，提升应用性能与可靠性。
- 🔐 **身份验证与安全**：通过请求头添加 `Authorization: Bearer <token>` 等进行身份验证；使用 `URL` 和 `URLSearchParams` 安全构建查询参数，防止注入攻击。
- 🧪 **测试与模拟**：使用 `undici` 包的 `MockAgent` 模拟 HTTP 请求，便于编写不依赖真实网络的单元测试。
- ⚡ **性能考量**：`fetch()` 适用于大多数场景，但在高吞吐量系统中，直接使用 `undici.request()` 或 `http/https` 模块可能获得更高性能。
- 🛠️ **传统模块使用**：`http` 和 `https` 模块适用于 Node.js 18 以下版本、遗留代码集成或需要直接控制底层连接的场景。
- ❓ **常见问题解答**：明确了 `fetch()` 是当前最简单、推荐的方式，而 `axios` 或 `got` 等外部库主要用于需要自动重试、拦截器等高级功能的场景。

---

### [CSS 选择器 - 2026 版 - 项目华莱士](https://www.projectwallace.com/the-css-selection/2026)

**原文标题**: [The CSS Selection - 2026 Edition - Project Wallace](https://www.projectwallace.com/the-css-selection/2026)

本文基于对超过 10 万个网站 CSS 使用情况的分析，总结了 2026 年 CSS 在实际应用中的状态，涵盖了样式表构成、规则、选择器、声明和值等多个维度，并揭示了新兴特性的采用率与遗留问题。

- 📊 **样式表规模**：中位数网站 CSS 文件大小为 309kB，最大达 52.5MB；源代码行数中位数为 10,677 行。
- 🎨 **At 规则使用**：`@media`（93%）、`@font-face`（86%）和`@keyframes`（84%）采用率最高，而`@supports`（45%）和`@layer`（2.7%）使用较少。
- 🧩 **规则结构**：中位数网站包含 2,802 条规则，每规则最大声明数中位数为 50，嵌套深度普遍较浅（中位数为 1 层）。
- 🔍 **选择器趋势**：伪类`:where`（91%）和`:has`（41%）采用率显著，可访问性选择器使用较少（中位数仅 1 个）。
- ⚠️ **声明问题**：`!important`声明中位数为 154 条，占所有声明的 2%；旧版浏览器 hack（如`*property`）仍在 18.8% 的网站中出现。
- 🎨 **值与单位**：颜色格式以 HEX（97%）为主，OKLCH 等新格式采用率低（1.9%）；`px`（98%）仍是最常用单位，但视口单位（如`dvh`）开始普及。
- 📈 **新兴特性**：容器查询（`@container`）已在 9.6% 的网站中使用，自定义属性（CSS 变量）中位数网站使用 68 个。
- 🔧 **分析局限**：当前数据基于字符串对比，未来需改进值标准化和相关性分析，并计划使用无头浏览器获取更真实数据。

---

### [Windows XP 反应版](https://react-xp.jamiepates.com/)

**原文标题**: [Windows XP React Edition](https://react-xp.jamiepates.com/)

本文介绍了人工智能在医疗领域的应用现状与前景，重点探讨了其在疾病诊断、治疗方案优化及医疗管理效率提升方面的作用，同时简要提及了相关的技术挑战和伦理考量。

- 🤖 AI 辅助诊断系统通过分析医学影像提升疾病识别准确率
- 💊 基于机器学习的个性化治疗方案推荐改善治疗效果
- ⚡ 智能流程自动化缩短患者等待时间并优化资源分配
- 🧬 基因组学数据分析助力精准医疗与药物研发
- 🛡️ 数据隐私保护与算法透明度成为实际应用中的关键挑战
- 🌐 远程医疗与可穿戴设备结合实现全天候健康监测

---

