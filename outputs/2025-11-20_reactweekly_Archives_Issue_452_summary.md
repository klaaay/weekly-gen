### [React 状态周报 第 452 期：2025 年 11 月 19 日](https://react.statuscode.com/issues/452)

**原文标题**: [React Status Issue 452: November 19, 2025](https://react.statuscode.com/issues/452)

React 生态系统最新动态：包含 imgui-react-runtime 混合开发框架发布、2025 年度开发者调查启动、工具库版本更新及行业观点探讨

- 🎯 imgui-react-runtime 正式发布：实现 React 与轻量级 GUI 库 Dear ImGui 的融合开发
- 📊 2025 年 React 生态调查启动：Devographics 年度调查截止 11 月 25 日，可查阅 2024 年结果
- 🐛 Sentry AI 代码审查升级：拦截超 3 万次生产环境错误，修复速度提升 50%
- 💡 工具组件设计反思：Dominik 提出工具提示组件应与使用场景深度耦合
- 🔄 重大迁移案例：HubSpot 团队分享 76000+ 测试用例从 Enzyme 转向 React Testing Library
- 🌐 开发范式讨论：Richard MacManus 探讨 AI 工具默认倾向 React 而非原生 Web 方案的现状
- 📦 多工具更新：NativeWind 样式优化、TanStack DB 0.5 查询驱动同步、Fumadocs 文档框架发布
- 🛠️ 开发工具动态：ESLint 基线检测插件获奖、React Player 3.4 发布、Git 2.52 新增文件修改追踪命令
- ⚡ 云服务进展：Cloud 66 支持 S3 兼容存储部署、PlanetScale 推出 5 美元 PostgreSQL 服务
- 🤖 技术前沿：Gemini Pro 3 预览版发布并集成 GitHub Copilot，TypeScript 不可变实验进行中

---

### [GitHub - tmikov/imgui-react-runtime: React + Dear ImGui + 静态 Hermes 运行时](https://github.com/tmikov/imgui-react-runtime)

**原文标题**: [GitHub - tmikov/imgui-react-runtime: React + Dear ImGui + Static Hermes](https://github.com/tmikov/imgui-react-runtime)

imgui-react-runtime 是一个实验性项目，将 React 与 Dear ImGui 和 Static Hermes 结合，通过声明式组件模型构建原生图形界面，支持完整的 React 功能，包括钩子和状态管理。

- 🚀 **React + Dear ImGui 集成**：使用 React 的 JSX 和组件模型编写 Dear ImGui 界面，支持钩子和事件处理
- ⚡ **Static Hermes 运行时**：零成本 FFI 调用 Dear ImGui C API，支持原生编译、字节码和源码三种模式
- 🖥️ **跨平台支持**：已测试 macOS 和 Linux，Windows 支持即将推出
- 🛠️ **示例应用**：包含 Hello World、功能展示和动态窗口管理三个示例，演示多种功能
- 📦 **组件库**：提供窗口、文本、按钮、表格、绘图等原生 Dear ImGui 组件
- 🔧 **自定义组件**：支持通过 ImGui DrawList API 创建完全自定义的控件和可视化元素
- 🏗️ **三单元架构**：jslib（事件循环）、React（协调器）和 ImGui（渲染器）通过 globalThis 通信
- 📋 **构建系统**：基于 CMake，自动下载和构建 Hermes，支持三种编译模式和可选 React 编译器优化

---

### [未找到标题](https://x.com/tmikov/status/1979771014340047088)

**原文标题**: [No title found](https://x.com/tmikov/status/1979771014340047088)

检测到浏览器中 JavaScript 功能未启用，建议通过启用 JavaScript 或更换受支持浏览器继续使用 X 平台。受支持浏览器列表可查阅帮助中心，隐私类扩展可能引发访问异常，建议暂时禁用后重试。

- 🚫 JavaScript 未启用导致功能受限
- 🌐 需启用 JavaScript 或更换受支持浏览器  
- 📖 支持浏览器列表详见帮助中心  
- 🔒 隐私扩展可能造成访问问题  
- 🔄 建议禁用扩展后重新尝试操作

---

### [GitHub - ocornut/imgui: Dear ImGui：轻量级 C++ 图形用户界面库，依赖极少](https://github.com/ocornut/imgui)

**原文标题**: [GitHub - ocornut/imgui: Dear ImGui: Bloat-free Graphical User interface for C++ with minimal dependencies](https://github.com/ocornut/imgui)

Dear ImGui 是一个轻量级 C++ 图形用户界面库，专为工具开发和实时应用设计，具有无冗余依赖、跨平台和高性能的特点。

- 🎯 专为工具开发设计：专注于内容创作工具、调试工具和可视化工具的开发
- ⚡ 即时模式 GUI：采用 IMGUI 范式，减少状态同步和代码冗余
- 🖥️ 渲染器无关：支持多种图形 API（DX、OpenGL、Vulkan、Metal 等）
- 📦 轻量级：核心文件少，易于集成到现有项目中
- 🌍 跨平台支持：提供 Windows、macOS、Linux、Android 等多平台后端
- 🔧 快速迭代：支持动态 UI 创建和实时数据可视化
- 🆓 开源许可：基于 MIT 许可证，可免费商用
- 🛠️ 丰富生态：拥有大量第三方扩展和语言绑定
- 📊 演示完善：提供功能完整的演示窗口展示各种特性
- 💼 行业应用：被众多游戏公司和开发者广泛使用

---

### [React 2025 现状报告](https://survey.devographics.com/en-US/survey/state-of-react/2025)

**原文标题**: [State of React 2025](https://survey.devographics.com/en-US/survey/state-of-react/2025)

React 2025 现状调查邀请开发者参与，旨在收集社区对 React 生态系统的使用反馈，所有数据将公开并用于指导技术发展方向。

- 🐢 React 从"快速迭代"转变为"稳步演进"，逐步推出服务端组件等创新功能
- 🚀 2025 年将正式推出备受期待的 React 编译器，并成立 React 基金会
- ⏱️ 调查耗时约 15-20 分钟，所有问题均为选填
- 🌍 面向所有 React 使用者开放，包括职业开发者、学生和爱好者
- 📊 旨在评估 React API 及生态库的认知度与使用情况
- 📈 调查结果将公开，供开发者和企业参考制定技术路线图
- 📅 调查时间为 10 月 25 日至 11 月 25 日，结果随后发布
- 👥 由 Devographics 联合社区贡献者共同运营，支持多语言翻译

---

### [React 2024 现状报告](https://2024.stateofreact.com/en-US)

**原文标题**: [State of React 2024](https://2024.stateofreact.com/en-US)

2024 年是 React 的巩固之年，在社区仍在适应服务端组件变革的背景下，React 19 通过消除开发痛点实现了稳定发展，而生态系统则持续迸发创新活力。

- 🛠️ React 19 聚焦体验优化：弃用 forwardRef、改进水合错误提示、引入提升性能的新编译器
- 🌊 生态系统创新不断：TanStack 基于 Query 成功经验推出挑战 Next.js 的全新元框架
- 🏆 保持行业领先地位：全球最受欢迎的 JavaScript 库进入相对稳定发展阶段
- 📢 特别说明：本调查与 Meta、Vercel 及 React 官方无关联
- 🌐 国际化协作：涵盖西班牙语、日语、中文等十余种语言版本的社区翻译

---

### [AI 代码审查：减少 3 万缺陷，提速 50% | Sentry 产品博客](https://blog.sentry.io/ai-code-review-30k-bugs-lighter-50-faster/?utm_source=reactstatus&utm_medium=paid-community&utm_campaign=aicodereview-fy26q4-aicodereviewlaunch&utm_content=newsletter-30k-blog-learnmore)

**原文标题**: [AI Code Review: 30K Bugs Lighter, 50% faster | Product Blog • Sentry](https://blog.sentry.io/ai-code-review-30k-bugs-lighter-50-faster/?utm_source=reactstatus&utm_medium=paid-community&utm_campaign=aicodereview-fy26q4-aicodereviewlaunch&utm_content=newsletter-30k-blog-learnmore)

AI 代码审查工具发布 30 天成效显著，在提升代码质量与开发效率方面取得突破性进展。

- 🐛 成功检测超过 3 万个代码缺陷，包括训练计划应用中的日程逻辑冲突和用户操作阻断等关键问题
- ⚡ 审查性能提升 50%，通过优化模型选择、设定思考预算限制及迭代控制实现降延迟
- 📝 评论结构升级为三重模块：详细问题分析 + 修复方案 + 可复制 AI 提示模板
- 🤖 推出 Claude 智能插件实现自动验证代码问题并生成修复补丁
- 🎥 提供线上工作坊回放，演示工具配置与实战应用方法
- 🌐 开放社区反馈渠道，鼓励开发者体验后提交使用心得

---

### [AI 代码审查：减少 3 万缺陷，提速 50% | 产品博客 • Sentry](https://blog.sentry.io/ai-code-review-30k-bugs-lighter-50-faster/?utm_source=reactstatus&utm_medium=paid-community&utm_campaign=aicodereview-fy26q4-aicodereviewlaunch&utm_content=newsletter-30k-blog-learnmore%20)

**原文标题**: [AI Code Review: 30K Bugs Lighter, 50% faster | Product Blog • Sentry](https://blog.sentry.io/ai-code-review-30k-bugs-lighter-50-faster/?utm_source=reactstatus&utm_medium=paid-community&utm_campaign=aicodereview-fy26q4-aicodereviewlaunch&utm_content=newsletter-30k-blog-learnmore%20)

AI 代码审查工具推出 30 天内发现超过 3 万个错误，性能提升 50%，并新增多项实用功能。

- 🐛 发现 30,000 多个代码错误，包括训练计划应用中的日程逻辑冲突和用户界面阻塞问题
- ⚡ 审查延迟降低 50%，通过优化模型选择、设置思考预算和迭代限制实现性能提升
- 📝 改进 PR 评论结构，包含详细分析、修复建议和可直接复制的 AI 提示模板
- 🤖 推出 Claude 技能，可自动验证问题并生成经过验证的代码补丁
- 🎥 提供在线研讨会回放，演示工具配置和使用方法
- 📢 邀请用户体验并反馈，提供多个社交平台分享渠道

---

### [工具提示组件不应存在 | TkDodo 的博客](https://tkdodo.eu/blog/tooltip-components-should-not-exist)

**原文标题**: [Tooltip Components Should Not Exist | TkDodo's blog](https://tkdodo.eu/blog/tooltip-components-should-not-exist)

作者认为工具提示组件不应作为独立组件存在，而应通过更高级别的模式组件来实现，以确保一致性和可访问性。

- 🚫 独立工具提示组件易被误用，导致可访问性问题
- ⌨️ 非交互元素上的工具提示无法通过键盘触发
- 🤯 随意添加工具提示会造成用户体验不一致
- 🎯 建议通过模式组件（如带 title 属性的按钮、必填标题的图标按钮）封装工具提示功能
- 🚧 限制底层工具提示组件能促进更创新的设计思考

---

### [支持 TanStack Start - Vercel](https://vercel.com/changelog/support-for-tanstack-start)

**原文标题**: [Support for TanStack Start - Vercel](https://vercel.com/changelog/support-for-tanstack-start)

Vercel 现已自动识别并支持 TanStack Start 全栈应用框架，该框架基于 TanStack Router 构建，适用于 React 和 Solid 项目。

- 🚀 通过创建新应用或在 vite.config.ts 中添加 nitro() 配置即可快速部署
- ⚙️ 部署配置需引入 tanstackStart 插件与 nitro 模块
- 💰 默认采用流体计算与动态 CPU 计费模式
- 📈 根据流量自动弹性伸缩资源
- 🧾 按实际使用量计费，闲置时段不产生费用
- 📚 详细指南可查阅官方集成文档

---

### [禅绘](https://zenpaint.org/)

**原文标题**: [ZenPaint](https://zenpaint.org/)

文章概述了人工智能在现代社会中的广泛应用及其带来的机遇与挑战。

- 🤖 人工智能技术正迅速渗透各行各业，提升生产效率
- 💡 机器学习算法通过数据分析为决策提供有力支持
- 🌐 自然语言处理技术改善了人机交互体验
- ⚠️ 需关注数据隐私保护与算法偏见问题
- 🔧 企业需建立完善的 AI 伦理规范与监管机制
- 📚 加强公众数字素养教育以应对技术变革

---

### [CSS Grid 由 intergalacticspacehighway 提交的拉取请求 #1865 · facebook/yoga · GitHub](https://github.com/facebook/yoga/pull/1865)

**原文标题**: [CSS Grid by intergalacticspacehighway · Pull Request #1865 · facebook/yoga · GitHub](https://github.com/facebook/yoga/pull/1865)

一位开发者向 Facebook 的 Yoga 项目提交了 CSS Grid 布局功能的实现，该功能作为 Flexbox 的补充系统，提供二维布局控制。目前已完成核心属性支持并正在进行多项优化改进。

- 🎯 扩展 Yoga 以支持 CSS Grid 规范，提供二维布局控制系统
- ✅ 已完成 grid-template-columns/rows、grid-column/row-start/end 等核心属性实现
- 📏 支持 minmax()、auto、百分比、固定单位和 fr 单位等尺寸函数
- 🚧 正在进行绝对定位项目布局、基线对齐和测试用例开发等优化工作
- 📋 未来计划实现 grid-template-areas、masonry 布局和 subgrid 等高级功能
- ❤️ 获得社区热烈反响，收获 106 个爱心和 72 个火箭表情反应

---

### [移山之举：我们从 Enzyme 迁移至 React 测试库的历程](https://product.hubspot.com/blog/migrated-from-enzyme-to-react-testing-library)

**原文标题**: [Moving Mountains: How We Migrated from Enzyme to React Testing Library](https://product.hubspot.com/blog/migrated-from-enzyme-to-react-testing-library)

本文详细介绍了团队如何用两年半时间将 76000 多个测试从 Enzyme 迁移到 React Testing Library 的完整过程，包括规划策略、教育推广、执行方法和规模化迁移经验。

- 🚀 **测试框架变革**：由于 Enzyme 停止支持 React 18，团队在 2022 年决定采用更贴近用户交互测试理念的 React Testing Library 作为新标准
- 📊 **精准评估规模**：通过运行时监控而非静态分析，将 500 多个需要迁移的代码库按测试量分为六个优先级等级
- 🎯 **渐进式迁移策略**：从测试量少的包开始迁移，集中处理技术债务，同时设置 2024 年底完成的明确目标
- 📚 **理念教育先行**：通过内部会议、技术分享和文档，帮助团队理解从工程师视角到用户视角的测试范式转变
- 🛠️ **智能执行机制**：通过 PR 自动评论阻止新增 Enzyme 测试，在测试报告中实时展示迁移进度，但不阻断正常开发流程
- 🤝 **规模化协作**：使用 Monarch 系统协调跨团队迁移，通过专项嵌入小组为关键团队提供一对一迁移支持
- ⚡ **人工优先原则**：尽管 AI 工具已成熟，但团队选择通过人工迁移确保测试质量，为后续复杂场景保留 AI 应用空间
- ✅ **显著成果**：2025 年 2 月完成全部迁移，为使用 Suspense 和 React Compiler 等新特性铺平道路

---

### [引言 · 酶](https://enzymejs.github.io/enzyme/)

**原文标题**: [Introduction · Enzyme](https://enzymejs.github.io/enzyme/)

Enzyme 是一个用于 React 的 JavaScript 测试工具，提供直观的 API 来测试和操作 React 组件输出，支持浅渲染、完整 DOM 渲染和静态渲染等多种测试方式。

- 🧪 支持多种 React 版本适配器，包括 React 16.x/15.x/0.14.x/0.13.x
- 🔌 提供官方适配器和第三方适配器（Preact/Inferno）
- 🧩 兼容主流测试框架（Mocha/Jest/Karma 等）和断言库
- 📖 API 设计模仿 jQuery，提供 find()/simulate() 等链式操作方法
- 🎯 支持三种渲染模式：浅渲染（Shallow）、完整 DOM 渲染（Mount）、静态渲染（Render）
- ⚠️ 对 React Hooks 支持存在部分限制（useEffect/useLayoutEffect 在浅渲染中不触发）
- 🔄 提供迁移指南帮助从 Enzyme 2.x 升级到 3.x
- 🌐 包含完整的 API 参考文档和代码示例
- 📦 通过 npm 安装并需配置对应 React 版本的适配器

---

### [当人人都是开发者时，我们如何推广 Web 平台而非 React？](https://webtechnology.news/when-everyones-a-developer-how-do-we-promote-the-web-platform-over-react/)

**原文标题**: [When Everyone’s a Developer, How Do We Promote the Web Platform Over React?](https://webtechnology.news/when-everyones-a-developer-how-do-we-promote-the-web-platform-over-react/)

随着 AI 开发趋势导致 React 框架被过度推荐，当前 Web 平台原生功能未能得到充分利用。本文探讨了如何推广 Web 平台特性以替代 React 框架。

- 🧞 AI 工具默认生成 React 代码，导致 Web 平台原生功能被忽视
- 📈 Vercel 和 Netlify 用户激增，但"氛围编程"者仅获得 React 解决方案
- ⚠️ 专家指出这会导致用户体验下降，类比 AI 内容淹没人类创作
- 💡 建议明确提示 AI 使用原生 Web 技术（如 Vanilla JS/HTML/CSS API）
- 📚 呼吁构建无框架代码数据集供 AI 学习
- 🌟 需要展示无重型框架的现代 Web 项目成功案例
- 🔗 业界专家批评框架阻碍 Web 平台创新速度
- 🍎 苹果应用商店网页版采用 Svelte 框架引发关注
- 🤖 微软推出 Magentic Marketplace 模拟 AI 代理协作环境
- 🦣 去中心化社交平台 Mastodon/Bluesky 持续更新功能
- ✨ HyperCard 历史证明低代码开发始终存在需求

---

### [将静态站点部署至任意云端](https://www.cloud66.com/products/static-sites/)

**原文标题**: [Deploy Static Sites to Any Cloud](https://www.cloud66.com/products/static-sites/)

Cloud 66 静态站点服务支持将静态网站部署到任何兼容 S3 存储的云平台，通过自带存储和 CDN 实现成本优化与完整控制。

- 🚀 支持任意云平台部署，兼容所有 S3 存储服务
- 💰 结合自有 S3 存储可节省高达 40% 成本
- 🔌 支持主流静态站点生成器（Jekyll/Hugo/Gatsby 等）
- ⚙️ 提供托管构建服务器，支持自定义构建流程
- 🌐 可配置任意 CDN 加速内容分发
- 🔒 自动管理 SSL 证书和流量重定向
- 📊 实时流量监控与精细化流量规则控制
- 🔄 支持预览部署和阶段环境管理
- 🌍 已支持 AWS/GCP/Azure/DigitalOcean 等主流云服务商
- 🛡️ 通过密钥管理和变量配置保障部署安全

---

### [Nativewind：加速 React Native 样式开发 | Hashrocket](https://hashrocket.com/blog/posts/nativewind-speeding-up-styling-in-react-native)

**原文标题**: [Nativewind: Speeding up Styling in React Native | Hashrocket](https://hashrocket.com/blog/posts/nativewind-speeding-up-styling-in-react-native)

Nativewind 是一个将 Tailwind CSS 类名引入 React Native 开发的库，通过熟悉的 Tailwind 语法加速移动应用开发流程。

- 🎯 使用 Tailwind CSS 类名直接为 React Native 组件添加样式，无需编写 StyleSheet 代码
- ⚡ 支持运行时或编译时转换，通过 Babel 插件实现更高效的样式处理
- 🛠️ 配置简单，支持 Expo 项目，只需安装相关依赖并配置 tailwind.config.js 文件
- 📱 生成的样式与标准 React Native 样式兼容，可与其他动画和导航库无缝集成
- 🎨 支持自定义颜色和类名扩展，保持设计系统一致性
- 🔄 减少在组件代码和样式表之间的切换，提升开发效率和代码可读性
- 🌐 便于实现响应式设计，支持 Tailwind 断点适配不同屏幕尺寸
- ✨ 实验性支持 Tailwind 动画类，在 iOS 和 Android 上运行良好

---

### [Nativewind](https://www.nativewind.dev/)

**原文标题**: [Nativewind](https://www.nativewind.dev/)

Nativewind 是一个让开发者能够在 React Native 应用中使用 Tailwind CSS 样式框架的工具，现已发布 v5 预发布版本，提供跨平台一致的设计体验。

- 🎨 支持 Tailwind CSS 工具类在 React Native 中的使用，实现跨平台样式统一
- 🌙 内置深色/浅色模式切换功能
- 🎯 提供 P3 广色域色彩系统支持
- 🛠️ 支持 CSS 变量和动画配置
- 📱 已被众多知名应用采用，包括 Ramble、Focusminny、Brainnotes 等
- 🧩 提供丰富的 UI 组件库：NativewindUI、React Native Reusables、gluestack
- 🚀 帮助开发者快速构建具有原生外观的高质量应用

---

### [尽可能将状态封装在组件中](https://blacksheepcode.com/posts/encapsulate_as_much_state_as_possible)

**原文标题**: [Encapsulate as much state as possible in your component](https://blacksheepcode.com/posts/encapsulate_as_much_state_as_possible)

本文讨论了在 React 组件设计中应尽可能封装状态的重要性，通过对比两种组件接口设计方式，展示了将状态转换逻辑封装在组件内部能提升代码可维护性和测试便利性。

- 🚫 错误模式：通过 props 完全控制组件状态会使父组件承担状态转换逻辑，增加使用复杂度
- ✅ 正确方案：组件应内部管理状态，仅暴露异步操作函数（如返回 Promise 的 onClick）
- 🧪 测试优势：封装状态的组件更易测试，能直接模拟用户操作流程
- 🔄 状态转换：组件应自主处理 pending→loading→success/error 的状态流转
- 📦 复杂组件示例：自动补全组件应内部封装防抖、请求取消、分页等复杂逻辑
- 🛠️ 开发效率：良好封装的组件接口能减少重复代码，降低使用错误率
- ⚡ 实际应用：这种模式特别适合处理异步操作的用户交互组件

---

### [富马文档](https://fumadocs.dev/)

**原文标题**: [Fumadocs](https://fumadocs.dev/)

Fumadocs 是一个基于 React.js 的现代化文档框架，提供高度可定制化的文档构建解决方案，支持多种开发框架和内容源，让开发者能够快速构建美观且功能丰富的文档网站。

- 🚀 **快速启动** - 通过命令行工具快速创建项目，支持 Next.js 等多种 React 框架
- 🎨 **高度可定制** - 提供精美主题和无头模式，允许完全自定义 UI 设计
- 📝 **多格式支持** - 原生支持 Markdown 和 MDX，提供丰富的语法扩展和代码高亮
- 🔧 **框架无关** - 兼容任何 React.js 框架，包括 Next.js、Tanstack Start、React Router 等
- 🧩 **模块化设计** - 采用内容 - 核心-UI 分离架构，可作为库灵活集成到现有项目
- 🔍 **强大搜索** - 轻松集成 Orama 和 Algolia 搜索功能
- 🌐 **多源内容** - 支持 MDX、内容集合和各种 CMS 系统
- 💫 **实时内容** - 结合 MDX 和 React 服务器组件，支持动态数据展示
- 👥 **社区驱动** - 完全开源，由活跃社区维护和贡献
- ⚡ **开发体验** - 受到众多知名开发者和团队的高度评价

---

### [快速构建优化网站，专注内容创作 | Docusaurus](https://docusaurus.io/)

**原文标题**: [Build optimized websites quickly, focus on your content | Docusaurus](https://docusaurus.io/)

Docusaurus 3.9 正式发布，这是一个专注于内容创作的静态网站生成工具，通过 MDX 支持快速构建优化网站。

- 🚀 支持 MDX 格式，可在 Markdown 中嵌入 React 组件，专注文档创作
- ⚛️ 基于 React 架构，可通过组件灵活定制网站布局和功能
- 🌍 内置国际化支持，轻松实现多语言文档翻译
- 📚 提供文档版本管理，保持文档与项目版本同步
- 🔍 集成 Algolia 搜索功能，方便用户快速查找内容
- 💝 获得众多开发者好评，包括 Redux、Supabase 等团队认可
- 🛠️ 简化网站搭建流程，开源项目可快速部署文档站点
- ✨ 支持深色模式等现代化功能，提升用户体验

---

### [TanStack DB 0.5 — 查询驱动同步 | TanStack 博客](https://tanstack.com/blog/tanstack-db-0.5-query-driven-sync)

**原文标题**: [TanStack DB 0.5 — Query-Driven Sync | TanStack Blog](https://tanstack.com/blog/tanstack-db-0.5-query-driven-sync)

TanStack DB 0.5 引入了查询驱动同步功能，通过组件查询自动生成精确的 API 调用，无需自定义端点或后端修改。该版本提供三种同步模式（即时、按需、渐进式），支持智能请求合并与增量加载，结合差异数据流技术实现毫秒级客户端查询更新。

- 🚀 查询即 API：组件查询自动转换为精准 API 请求，无需额外接口开发
- ⚡ 三种同步模式：即时加载（适用于静态数据）、按需加载（大数据集优化）、渐进加载（兼顾首屏速度与全量数据）
- 🔄 智能请求优化：自动合并重复查询、增量加载差异数据、关联查询批量请求
- 🛠️ 多后端支持：兼容 REST/GraphQL/tRPC，提供谓词映射工具
- 📊 性能优势：差异数据流技术实现 10 万 + 数据即时更新，集成 TanStack Query 缓存策略
- 🔮 演进路径：支持从 REST 平滑升级到实时同步引擎（Electric/Trailbase/PowerSync）
- 🎯 开发体验：声明式查询语法，类型安全，单次映射持续复用

---

### [基线 JS 文档](https://baselinejs.vercel.app/)

**原文标题**: [Baseline JS Docs](https://baselinejs.vercel.app/)

该 ESLint 插件通过检测代码中不符合 Web 平台基线标准的 API 使用，帮助开发者确保 JavaScript 代码的跨浏览器兼容性。

- 🎯 核心功能：检测 JavaScript 代码中不符合 Web 平台基线标准的 API 使用
- 🌐 兼容标准：基于跨浏览器兼容性标准 Web Platform Baseline
- ⚠️ 问题示例：检测到 getYear() 方法并非广泛支持的基线功能
- 🚀 开发目标：确保代码在所有浏览器中都能正常运行
- 📚 资源支持：提供完整文档和 GitHub 开源项目
- 🔧 使用场景：帮助开发者默认采用符合基线标准的编码实践

---

### [基准工具黑客马拉松获奖名单揭晓……  |  Blog  |  web.dev](https://web.dev/blog/baseline-hackathon-2025-winners)

**原文标题**: [The winners of the Baseline Tooling Hackathon are...  |  Blog  |  web.dev](https://web.dev/blog/baseline-hackathon-2025-winners)

Baseline 工具黑客松获奖项目揭晓，三项创新工具从近 3000 名开发者提交的数百个项目中脱颖而出，分别获得万美元奖池的冠亚季军。

- 🥇 **ESLint 基线检测插件** - 冠军项目由 Ryuya Hasegawa 开发的 eslint-plugin-baseline-js，可检测 JavaScript/TypeScript 代码中超出基线标准的特性，集成 web-features 数据集与 TypeScript 解析器，提供开箱即用的配置文档
- 🤖 **AI 开发辅助工具** - 亚军项目 Technickel Dev 开发的 baseline-mcp 服务器，为 AI 编程助手提供准确的 Web 特性兼容性数据，支持特性查询与现代替代方案推荐
- 🎬 **视频基线组件** - 季军项目 Zoran Jambor 打造的 Baseline Status for Video 应用，通过 Web 组件生成可嵌入视频的兼容性指示器，支持绿幕抠像与动画录制
- 🌟 **生态影响** - 所有获奖项目均基于 web-features 权威数据，有效推动 Baseline 标准在代码检查、AI 编程、视频教程等多元场景的普及应用
- 🙏 **社区致谢** - 主办方特别感谢所有参赛者与反馈调查参与者，其中 10 位"最有价值反馈"获奖者已收到通知

---

### [基准线  |  web.dev](https://web.dev/baseline)

**原文标题**: [Baseline  |  web.dev](https://web.dev/baseline)

Web Platform Baseline 提供了关于浏览器对 Web 平台功能支持的清晰信息，帮助开发者判断哪些功能可在项目中使用。它由 WebDX 社区组织定义，包含新可用和广泛可用两个阶段，并整合到多种开发工具中。

- 🌐 Baseline 由 WebDX 社区组织定义，提供浏览器功能支持标准
- 📊 功能分为新可用（核心浏览器支持）和广泛可用（30 个月后）两个阶段
- 🔧 已集成到 Chrome DevTools、VS Code、ESLint 等开发工具
- 📦 可通过 Browserslist 和 web-features 包在项目中应用
- 🎯 按年度分组为 Baseline 目标（如 2023-2025）
- 📰 每月发布摘要更新社区动态
- 📚 在 MDN 和 Can I Use 等平台可查询功能状态
- 💡 帮助开发者决策 polyfill 使用和功能采用时机

---

### [GitHub - cookpete/react-player：用于播放多种URL的React组件，支持文件路径、YouTube、Facebook、Twitch、SoundCloud、Streamable、Vimeo、Wistia和DailyMotion](https://github.com/cookpete/react-player)

**原文标题**: [GitHub - cookpete/react-player: A React component for playing a variety of URLs, including file paths, YouTube, Facebook, Twitch, SoundCloud, Streamable, Vimeo, Wistia and DailyMotion](https://github.com/cookpete/react-player)

一个用于播放多种媒体源的 React 组件，支持文件路径、YouTube、Facebook 等平台，提供灵活的播放控制和自定义配置。

- 🎬 支持多种媒体源，包括本地文件、HLS/DASH 流媒体及主流视频平台
- ⚙️ 提供丰富的播放控制属性，如自动播放、音量调节、播放速率控制等  
- 🖼️ 支持轻量模式预览图、画中画模式和自定义控件
- 📱 具备响应式设计，可适配不同屏幕尺寸
- 🔧 允许通过配置项深度定制各平台播放器参数
- 🎯 提供完整的回调函数系统，覆盖播放全生命周期事件
- 🔌 支持自定义播放器扩展和第三方 SDK 覆盖
- 📦 支持懒加载和代码分割优化性能
- 🌐 采用 MIT 开源协议，由 Mux 团队维护更新

---

### [ReactPlayer 演示](https://cookpete.github.io/react-player/)

**原文标题**: [ReactPlayer Demo](https://cookpete.github.io/react-player/)

文章概述了人工智能在现代社会中的广泛应用及其带来的机遇与挑战。

- 🤖 人工智能技术正迅速渗透各行各业，提升生产效率
- 💡 机器学习算法通过数据分析为决策提供有力支持
- 🌐 自然语言处理技术改善了人机交互体验
- ⚠️ 需关注数据隐私保护和算法偏见问题
- 🔧 企业需建立完善的 AI 伦理规范和使用准则
- 📚 加强公众数字素养教育以应对技术变革

---

### [GitHub - mrousavy/react-native-mmkv：⚡️ React Native 最快的键值存储方案，比 AsyncStorage 快约 30 倍！](https://github.com/mrousavy/react-native-mmkv)

**原文标题**: [GitHub - mrousavy/react-native-mmkv: ⚡️ The fastest key/value storage for React Native. ~30x faster than AsyncStorage!](https://github.com/mrousavy/react-native-mmkv)

这是一个高性能的 React Native 键值存储库，基于微信开源的 MMKV 框架，提供比 AsyncStorage 快约 30 倍的存储性能。

- ⚡️ 极速性能：采用 JSI 和 C++ NitroModules 技术，完全同步操作，比 AsyncStorage 快约 30 倍
- 🔐 安全加密：支持数据加密存储，可配置加密密钥保护敏感信息
- 📱 多平台支持：完整支持 iOS、Android 和 Web 平台
- 🎯 多种数据类型：支持字符串、布尔值、数字和 ArrayBuffer 等多种数据类型
- 🔄 多实例管理：可创建多个存储实例，分离用户数据和全局数据
- 📊 状态管理集成：提供 React Hooks API，轻松集成 Redux、Recoil、Zustand 等状态管理库
- 🛠️ 灵活配置：可自定义存储路径、加密密钥、只读模式等参数
- 🧪 测试友好：内置 Jest 和 Vitest 模拟实例，便于单元测试

---

### [react-native-mmkv/docs/V4_UPGRADE_GUIDE.md 位于 main · mrousavy/react-native-mmkv · GitHub](https://github.com/mrousavy/react-native-mmkv/blob/main/docs/V4_UPGRADE_GUIDE.md)

**原文标题**: [react-native-mmkv/docs/V4_UPGRADE_GUIDE.md at main · mrousavy/react-native-mmkv · GitHub](https://github.com/mrousavy/react-native-mmkv/blob/main/docs/V4_UPGRADE_GUIDE.md)

这是一个 GitHub 仓库页面，显示加载错误信息

🚫 页面加载出错提示
- 需要重新加载页面才能正常显示

🔔 通知设置限制
- 必须登录账户才能修改通知设置

📊 仓库基本数据
- 7.8k 星标 | 318 复刻 | 15 个问题 | 33 个拉取请求

🔧 功能模块异常
- 代码、问题、拉取请求等核心模块均显示加载错误

🔄 操作建议
- 建议重新加载页面以解决显示问题

---

### [GitHub - stripe/react-stripe-js：用于 Stripe.js 和 Stripe Elements 的 React 组件](https://github.com/stripe/react-stripe-js)

**原文标题**: [GitHub - stripe/react-stripe-js: React components for Stripe.js and Stripe Elements](https://github.com/stripe/react-stripe-js)

这是一个用于在 React 应用中集成 Stripe 支付功能的官方库，提供 React 组件封装 Stripe.js 和支付元素，支持现代 React 特性。

- ⚛️ 提供 React 组件封装 Stripe.js 和支付元素集成
- 📚 支持 TypeScript，具有完整的类型声明
- 🔄 兼容 React 16.8 及以上版本，支持 Hooks 和类组件
- 🛠️ 包含 Elements、PaymentElement 等核心组件
- 📖 提供详细文档、代码示例和迁移指南
- 🔧 支持自定义支付界面外观
- 📦 采用 MIT 开源许可证，社区活跃
- 🌐 可通过 CodeSandbox 快速体验和测试

---

### [GitHub - AlexSergey/rockpack: Rockpack 是一个轻量级、零配置的解决方案，用于快速搭建支持服务端渲染（SSR）、打包、代码检查和测试的 React 应用。](https://github.com/AlexSergey/rockpack)

**原文标题**: [GitHub - AlexSergey/rockpack: Rockpack is a lightweight, zero-configuration solution for quickly setting up a React application with full support for Server-Side Rendering (SSR), bundling, linting, and testing.](https://github.com/AlexSergey/rockpack)

Rockpack 是一个轻量级、零配置的 React 应用快速搭建解决方案，提供完整的服务端渲染、打包、代码检查和测试支持，帮助开发者在 5 分钟内启动现代化 React 项目。

- 🚀 **快速启动**：零配置即可创建支持 SSR、打包、代码检查和测试的 React 应用
- 🛠️ **模块化架构**：包含@rockpack/starter、@rockpack/compiler、@rockpack/tester 和@rockpack/codestyle 四个核心模块
- ⚡ **多种应用类型**：支持 SPA、SSR 应用、React 组件和 UMD 库的快速搭建
- 🔧 **开箱即用**：内置 Webpack 最佳实践配置、ESLint 规则、Jest 测试环境和 TypeScript 支持
- 📦 **生产优化**：自动处理图片/SVG 优化、CSS 模块、PostCSS 和打包分析
- 🔄 **灵活集成**：可模块化集成到现有项目，支持自定义配置无需 eject
- 🎯 **适用场景**：适合初学者、大型项目、创业想法验证和组件库开发
- 📄 **开源许可**：采用 MIT 许可证，完全免费且开放协作

---

### [STRICH：适用于网页应用的条码扫描工具](https://strich.io/?ref=react-status)

**原文标题**: [STRICH: Barcode Scanning for Web Apps](https://strich.io/?ref=react-status)

STRICH 是一个用于网页应用的 JavaScript 条码扫描库，支持实时 1D/2D 条码识别，无需原生应用或后端支持。

- 📱 支持主流浏览器和移动设备，兼容所有常见网页框架
- ⚡ 基于 WebAssembly 和 WebGL 技术，提供高性能扫描体验
- 🎯 内置扫描 UI 界面，支持相机选择、闪光灯、点击对焦等功能
- 🔄 支持多种 1D/2D 条码格式，包括 QR 码、Data Matrix、PDF417 等
- 💰 提供透明定价方案，包含免费试用和三种付费套餐
- 🏢 具备企业级功能：白标定制、离线运行、GS1 标准支持
- 📚 提供完善的文档、示例代码和技术支持
- 🌟 获得多个行业客户好评，包括图书馆、医疗、零售等领域

---

### [全栈 Next.js 16 课程 - 通往 Next 之路](https://www.road-to-next.com/?utm_source=frontend_weekly&utm_medium=referral&utm_campaign=next_course)

**原文标题**: [Full-Stack Next.js 16 Course - The Road to Next](https://www.road-to-next.com/?utm_source=frontend_weekly&utm_medium=referral&utm_campaign=next_course)

这是一门由 Robin Wieruch 推出的全栈 Web 开发视频课程，专注于 Next.js 16 和 React 19，旨在帮助开发者从初级进阶到高级水平，掌握构建真实 SaaS 产品所需的技能。

- 🎯 **课程目标**：培养全栈开发能力，涵盖从 UI 到数据库的完整开发流程
- 🚀 **技术栈**：Next.js 16、React 19、Prisma、Supabase、TypeScript 等现代工具
- 📚 **课程结构**：包含开发者旅程和软件工程师旅程两个阶段，逐步深入
- 💻 **实践项目**：通过构建可部署的 SaaS 入门套件巩固学习成果
- 👥 **适合人群**：前端转全栈、不同语言背景开发者、自由职业者及技术创业者
- 🏆 **教学特色**：注重代码架构、软件工程思维和实际业务场景应用
- 🌟 **附加价值**：提供 Discord 社区、完成证书和 14 天退款保证
- 💰 **价格选项**：开发者旅程$249，软件工程师旅程$349（含折扣）

---

### [实验：使 TypeScript 默认不可变](https://evanhahn.com/typescript-immutability-experiment/)

**原文标题**: [Experiment: making TypeScript immutable-by-default](https://evanhahn.com/typescript-immutability-experiment/)

作者尝试在 TypeScript 中实现默认不可变变量，通过禁用内置库并自定义类型定义，成功使数组和 Record 类型默认不可变，但未能实现普通对象的默认不可变性。

- 🚫 禁用 TypeScript 内置库，通过设置 noLib 标志移除默认可变类型定义
- 🧩 创建基础类型定义文件 lib.d.ts，包含空接口作为类型占位符
- 🔒 通过 readonly 修饰符成功实现数组的默认不可变性，禁止直接赋值和 push 等操作
- 🔄 定义 MutableArray 接口实现可控的可变数组，需显式声明
- 📝 扩展方案到 Record 类型，分别定义不可变 Record 和可变 MutableRecord
- ❌ 普通对象{foo:"bar"}的默认不可变性实现失败，无法通过修改 Object 接口达成
- 💡 建议未来可通过 lint 规则强制实现完全不可变，或等待语言原生支持

---

### [Gemini 3：新闻与公告](https://blog.google/products/gemini/gemini-3-collection/)

**原文标题**: [Gemini 3: News and announcements](https://blog.google/products/gemini/gemini-3-collection/)

Gemini 3 作为谷歌最新一代人工智能模型，整合了多模态理解、长上下文处理、思维推理与原生工具使用等能力，旨在帮助用户实现各类创意构想。

- 🧠 推出 Gemini 3 智能模型，融合多模态与推理能力
- 📱 Gemini 应用迎来重大升级，搭载新一代模型
- 🔍 搜索引擎集成 Gemini 3，提升智能搜索体验
- 💻 开发者可通过 Antigravity 平台使用智能编码功能
- 🏢 企业版与 Vertex AI 平台同步上线新模型
- 🎨 生成式 UI 技术在 Gemini 应用中实现动态交互界面
- ⚙️ 命令行工具与 Android Studio 集成开发支持
- 🔥 Flutter 平台推出 GenUI SDK 测试版本

---

### [Gemini 3 开发者指南  |  Gemini API  |  Google AI for Developers](https://ai.google.dev/gemini-api/docs/gemini-3?thinking=high)

**原文标题**: [Gemini 3 Developer Guide  |  Gemini API  |  Google AI for Developers](https://ai.google.dev/gemini-api/docs/gemini-3?thinking=high)

Gemini 3 是最新一代智能模型系列，具备先进的推理能力，支持自主编码、多模态任务和智能工作流处理。开发者可通过控制思考层级、媒体分辨率等参数优化性能，并需注意思维签名机制以保持连续对话的推理质量。

- 🧠 **动态思考控制**：支持高/低思考层级，高层级增强复杂推理，低层级降低延迟
- 🖼️ **媒体分辨率调节**：可针对图像/PDF/视频设置不同解析度，平衡识别精度与 token 消耗
- 🔐 **思维签名机制**：通过加密签名维持跨 API 调用的推理连贯性，需严格遵循返回规则
- ⚡ **默认温度设置**：推荐保持 temperature=1.0，调整可能导致数学推理性能下降
- 🛠️ **工具集成扩展**：支持结构化输出结合谷歌搜索、代码执行、URL 上下文等工具
- 📊 **技术规格升级**：128K 上下文窗口，2025 年 1 月知识截止，输入/输出定价分层
- 🔄 **迁移注意事项**：从 Gemini 2.5 迁移需调整提示词策略，注意 PDF 解析默认分辨率变化
- 🎯 **提示词优化**：推荐使用简洁指令，将关键问题置于长文本末尾以提升推理准确性

---

### [Gemini 3 Pro 现已在 GitHub Copilot 中公开预览 - GitHub 更新日志](https://github.blog/changelog/2025-11-18-gemini-3-pro-is-in-public-preview-for-github-copilot/)

**原文标题**: [Gemini 3 Pro is in public preview for GitHub Copilot - GitHub Changelog](https://github.blog/changelog/2025-11-18-gemini-3-pro-is-in-public-preview-for-github-copilot/)

Gemini 3 Pro 模型现已在 GitHub Copilot 中开放公共预览，该模型将逐步向 Copilot Pro、Pro+、Business 和 Enterprise 订阅用户开放。用户可在 VS Code、GitHub 网页端、移动端及 CLI 中选择使用此模型，企业用户需在设置中启用策略，个人用户可直接在模型选择器中切换。

- 🚀 Gemini 3 Pro 作为谷歌最新前沿模型，现进入 GitHub Copilot 公共预览阶段
- 📅 自 2025 年 11 月 18 日起逐步向 Pro/Pro+/Business/Enterprise 用户开放
- 💻 支持在 VS Code、github.com、GitHub Mobile 及 CLI 的对话模型选择器中调用
- ⚙️ 企业管理员需在 Copilot 设置中启用策略，个人用户可通过模型选择器直接切换
- 🔑 支持自带 API 密钥模式，需在模型管理界面手动配置
- 📚 用户可通过官方文档了解详情，在 GitHub 社区提交使用反馈

---

### [2025 年 10 月（版本 1.106）](https://code.visualstudio.com/updates/v1_106)

**原文标题**: [October 2025 (version 1.106)](https://code.visualstudio.com/updates/v1_106)

VS Code 2025 年 10 月版本 (1.106) 带来三大核心更新：集中管理 AI 代理会话的 Agent HQ、增强安全控制机制，以及优化日常编码体验的编辑器改进。

- 🎯 **Agent HQ 统一视图** - 新增代理会话中心，支持本地与云端 AI 代理的集中监控和管理
- 🛡️ **安全与信任增强** - 引入工具后审批机制，支持按来源批量信任 MCP 服务器
- ✨ **编辑器体验优化** - 差异编辑器支持删除文本选择，Go to Line 命令新增字符定位功能
- 🤖 **计划代理功能** - 新增分步任务规划代理，支持自定义规划流程
- 🌐 **云端代理集成** - Copilot 编码代理集成至 Chat 扩展，提供更原生体验
- 🔄 **自定义代理升级** - 聊天模式重命名为自定义代理，支持跨环境运行配置
- 📝 **代码编辑改进** - 内联建议开源合并，支持通过装订区图标暂停建议
- 🎨 **界面视觉刷新** - 更新 codicon 图标集，采用更现代的曲线设计
- ⚙️ **高级设置支持** - 新增高级设置分类，专为需要精细控制的用户设计
- 💬 **聊天功能增强** - 改进工具选择算法，支持保存对话为可重用提示
- 🔧 **终端智能感知** - 终端 IntelliSense 结束预览阶段，正式向所有用户推出
- 📊 **测试覆盖导航** - 新增未覆盖代码行导航命令，便于快速定位测试缺口
- 🔐 **认证管理优化** - 扩展账户偏好设置更易发现，微软认证淘汰经典模式

---

### [2025 年 10 月（版本 1.106）](https://code.visualstudio.com/updates/v1_106#_terminal-intellisense)

**原文标题**: [October 2025 (version 1.106)](https://code.visualstudio.com/updates/v1_106#_terminal-intellisense)

Visual Studio Code 2025 年 10 月版本（1.106）带来多项重要更新，涵盖 AI 助手增强、代码编辑优化、终端功能改进及扩展开发支持等方面。

- 🎯 **AI 助手管理中心**：新增 Agent Sessions 视图，集中管理本地与云端 AI 会话，支持搜索和统一视图模式
- 📋 **智能任务规划**：内置 Plan Agent 可分解复杂任务并生成实施计划，支持自定义规划流程
- ☁️ **云端代理集成**：Copilot 编码代理深度集成，支持 CLI 代理会话和编辑跟踪
- 🛠️ **自定义代理升级**：聊天模式更名为自定义代理，支持跨环境运行和元数据配置
- 📝 **代码编辑增强**：差异编辑器支持删除文本选择，行跳转功能新增字符定位和边界处理
- 🎨 **界面体验优化**：更新图标设计，支持 Linux 策略管理，多文件差异编辑器支持跨文件导航
- 🤖 **聊天工具改进**：基于嵌入的工具选择优化，新增工具后审批和批量信任功能
- 💻 **终端智能感知**：正式发布终端 IntelliSense，支持多 Shell 类型和丰富配置选项
- 🔧 **扩展开发支持**：新增 Secondary SideBar 视图容器，Quick Pick API 增强，支持 Markdown 树项标签
- 🔒 **安全认证更新**：MCP 支持组织级服务器管理，Microsoft 认证淘汰经典模式
- 🧪 **实验性功能**：终端文件写入检测、隐藏终端管理、推理样式显示等预览特性

---

### [Git 2.52 版本亮点 - GitHub 官方博客](https://github.blog/open-source/git/highlights-from-git-2-52/)

**原文标题**: [Highlights from Git 2.52 - The GitHub Blog](https://github.blog/open-source/git/highlights-from-git-2-52/)

Git 2.52 版本引入了多项重要功能与优化，包括树级追溯、仓库维护策略增强、新子命令支持及性能提升等。

- 🌳 **树级追溯功能**：新增`git last-modified`命令，高效追溯目录内各文件的最新修改提交，速度提升约 5.5 倍
- 🛠️ **仓库维护优化**：新增`geometric`维护任务，结合几何重组与垃圾清理，提升大型仓库运行效率
- 📚 **引用管理增强**：`git refs`新增`list`与`exists`子命令，统一引用查询操作
- 🧪 **实验性仓库命令**：新增`git repo`命令，提供仓库结构统计与配置信息查询功能
- 🌿 **默认分支变更**：Git 3.0 将默认分支名从"master"改为"main"，支持提前体验
- 🔄 **哈希算法过渡**：持续推进 SHA-1 向 SHA-256 迁移，为跨算法交互奠定基础
- 🦀 **Rust 语言支持**：首次引入可选 Rust 组件，用于变长整数编码，为未来功能重构铺路
- 🔍 **布隆过滤器增强**：扩展对通配符路径规范的支持，提升路径范围查询性能
- ⚡ **多领域性能优化**：包括`git describe`提速 30%、`git log -L`加速、索引处理优化等
- 🧹 **稀疏检出清理**：新增`git sparse-checkout clean`命令，简化工作目录清理操作

---

### [PlanetScale 5 美元套餐现已上线 —— PlanetScale](https://planetscale.com/blog/5-dollar-planetscale-is-here)

**原文标题**: [$5 PlanetScale is live â PlanetScale](https://planetscale.com/blog/5-dollar-planetscale-is-here)

PlanetScale 推出每月 5 美元起的单节点 Postgres 数据库服务，现已完成全球部署，为非高可用场景提供经济高效的生产就绪方案。

- 💰 **起价优惠** - 单节点数据库月费仅 5 美元起，开发分支同步降至 5 美元/月
- 🚀 **生产就绪** - 支持初创项目、概念验证及开发环境，具备完整生产级功能
- 🔧 **功能齐全** - 包含查询洞察、分支管理、模式推荐等开发者友好功能
- 📈 **灵活扩容** - 支持垂直扩展集群规格，可随时升级至高可用模式（主实例 + 多副本）
- 🧩 **未来扩展** - 即将推出 Neki 分片方案支持水平扩展，满足业务增长需求
- 🌐 **全球部署** - 基于 PlanetScale 云平台运行，承载过大型网络负载验证

---

### [LibreOffice 中的 Wordle 游戏 — bojidar-bg.dev](https://bojidar-bg.dev/blog/2025-11-11-wordle-libreoffice/)

**原文标题**: [Wordle in LibreOffice — bojidar-bg.dev](https://bojidar-bg.dev/blog/2025-11-11-wordle-libreoffice/)

在 LibreOffice 中使用 JavaScript 宏实现 Wordle 游戏，探索了当前 JavaScript 宏的开发流程与挑战。

- 🎮 通过 LibreOffice Writer 的脚本 API 成功创建了 Wordle 克隆游戏，利用文本高亮特性实现字母评分功能
- 📚 发现 LibreOffice 文档严重缺乏 JavaScript 宏编写指导，需自行研究 ODT 文件结构和 manifest 配置
- 🔧 手动解压/压缩 ODT 文件来嵌入 JavaScript 宏，需创建特定目录结构和 XML 描述文件
- ⚡ 使用 Rhino JavaScript 引擎和 UNO API，通过 XModifyListener 监听文档修改事件
- 🎨 实现文本高亮通过 XPropertySet 设置 CharBackColor 属性，使用 XParagraphCursor 导航文本段落
- 🐛 遇到 Java 字符串类型混淆、事件递归、撤销管理等问题，通过类型转换和 XUndoManager 解决
- 🔍 集成 LibreOffice 拼写检查器验证单词，使用 Timer 实现动画消息显示
- 💡 尽管开发流程复杂，但 UNO API 功能强大稳定，支持深度定制 Office 功能

---

