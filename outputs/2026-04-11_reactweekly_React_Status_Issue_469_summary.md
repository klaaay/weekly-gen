### [提升差异行性能的艰难攀登 - GitHub 博客](https://github.blog/engineering/architecture-optimization/the-uphill-climb-of-making-diff-lines-performant/)

**原文标题**: [The uphill climb of making diff lines performant - The GitHub Blog](https://github.blog/engineering/architecture-optimization/the-uphill-climb-of-making-diff-lines-performant/)

GitHub团队通过重构“文件更改”标签页的diff行组件，显著提升了大型拉取请求的性能。优化措施包括简化React组件树、减少DOM节点、采用虚拟化技术及优化数据访问模式，从而降低了内存占用、提升了交互响应速度。

- 🚀 **性能大幅提升**：通过简化组件和减少DOM节点，使大型拉取请求的交互响应时间（INP）降低约78%，内存使用减少约50%。
- 🏗️ **架构重构**：从v1的复杂嵌套组件（每行8-13个组件）改为v2的扁平化设计（每行仅2个组件），减少了代码复杂性和事件处理开销。
- 🖥️ **虚拟化技术应用**：针对超大型拉取请求（超过1万行），采用窗口虚拟化技术，仅渲染可见内容，使DOM节点和内存占用减少90%以上。
- 📊 **数据访问优化**：将O(n)状态查找改为基于Map的O(1)常量访问，提升评论管理和行选择等操作的效率。
- 🛠️ **工程实践改进**：限制useEffect使用、优化CSS选择器、实现渐进式加载等，全面提升渲染性能和用户体验。

---

### [Anthropic Lydia Hallie深度解析Claude代码 | AddEvent](https://www.addevent.com/event/8n58y7bjwqmr)

**原文标题**: [Claude Code Deep Dive with Lydia Hallie from Anthropic | AddEvent](https://www.addevent.com/event/8n58y7bjwqmr)

Anthropic公司的Lydia Hallie将举办一场关于Claude Code的深度技术研讨会，由Frontend Masters提供独家免费工作坊，旨在帮助开发者深入理解并掌握Claude Code的高级配置与定制开发。

- 🧠 **深入探索Claude Code**：超越默认设置，学习从提示到响应的内部机制，逐层配置演示项目。
- ⚙️ **实践配置与开发**：涵盖CLAUDE.md文件、权限管理、技能集成，以及从零构建自定义MCP服务器。
- 🗓️ **时间安排**：2026年4月21日，美国芝加哥时间上午9:30至下午4:30（日本时间4月21日23:30至4月22日06:30）。
- 🆓 **免费参与**：通过Frontend Masters官网链接即可免费注册参加。
- 👩‍💻 **专家主讲**：由Anthropic公司的Lydia Hallie主持，内容面向希望深度定制AI编码助手的开发者。

---

### [发布 v7.0.0 · vadimdemedes/ink · GitHub](https://github.com/vadimdemedes/ink/releases/tag/v7.0.0)

**原文标题**: [Release v7.0.0 · vadimdemedes/ink · GitHub](https://github.com/vadimdemedes/ink/releases/tag/v7.0.0)

Ink 7.0.0 版本发布，这是一个重大更新，引入了多项新功能、改进和破坏性变更，主要围绕提升React命令行界面开发体验。

- 🚨 **破坏性变更**：要求 Node.js 22 和 React 19.2+，并修正了 Backspace 键和 Escape 键的按键事件处理逻辑。
- 🆕 **新增功能**：引入了多个新 Hook，如 `usePaste`（处理粘贴）、`useWindowSize`（窗口尺寸）、`useBoxMetrics`（测量尺寸）和 `useAnimation`（动画支持）。
- 🖥️ **渲染增强**：为 `render()` 函数新增了 `alternateScreen`（备用屏幕缓冲区）和 `interactive`（交互模式）选项。
- 🧩 **组件功能扩展**：为 `<Box>` 组件新增了边框背景色、最大尺寸、宽高比等布局属性；为 `<Text>` 组件新增了 `wrap="hard"` 属性。
- 🔧 **修复与改进**：修复了增量渲染、未映射键码崩溃、CJK文本截断和宽字符分割等问题，并改进了 Kitty 键盘协议的检测方式。

---

### [版本 v9.0.0 | Mantine](https://mantine.dev/changelog/9-0-0/#marquee-component)

**原文标题**: [Version v9.0.0 | Mantine](https://mantine.dev/changelog/9-0-0/#marquee-component)

Mantine 9.0.0 是一个重大版本更新，引入了全新的日程安排组件包、多个新组件和钩子，以及对现有组件的多项改进和增强，包括对 React 19 的更好支持、异步表单验证和性能优化。

- 📅 **全新日程安排包**：新增 `@mantine/schedule` 包，提供完整的日历日程组件，支持日、周、月、年视图及拖拽事件管理。
- 🔄 **折叠组件增强**：`Collapse` 组件新增水平方向支持，并引入了对应的 `use-collapse` 和 `use-horizontal-collapse` 钩子。
- 🪟 **浮动窗口功能**：新增 `use-floating-window` 钩子和 `FloatingWindow` 组件，用于创建可拖拽的浮动元素。
- 📜 **新布局与滚动组件**：引入了 `OverflowList`、`Marquee`、`Scroller` 组件及对应的 `use-scroller` 钩子，用于处理内容溢出、连续滚动和可导航的滚动区域。
- 📊 **图表与数据展示**：`@mantine/charts` 新增 `BarsList` 组件，用于展示水平条形图列表。
- 🃏 **卡片与输入组件改进**：`Card` 支持水平方向；`Checkbox.Group` 和 `Switch.Group` 新增 `maxSelectedValues` 属性以限制选择数量；所有输入组件支持 `loading` 状态。
- 🎛️ **表单功能升级**：`use-form` 支持异步验证、`TransformedValues` 类型参数、新的验证器（`isUrl`, `isOneOf`）以及 `Standard Schema` 集成。
- 🔧 **组件通用性与功能增强**：多个组件（如 `SegmentedControl`, `Select`）支持泛型值类型；`Combobox` 支持虚拟化；`Highlight` 支持按词着色和全词匹配。
- 📏 **布局与交互优化**：`Grid` 改用 `gap` 属性并移除负边距；`Slider` 支持垂直方向；`SimpleGrid` 新增 `minColWidth` 和 `autoRows` 属性；`AppShell` 新增静态模式。
- ⚙️ **依赖与底层更新**：要求 React 19.2+；多个钩子迁移使用 React 19 的 `useEffectEvent`；`Transition` 等组件使用 React 19 `Activity` 以保持隐藏状态。
- 🎨 **主题与样式调整**：新增 `fontWeights` 主题属性控制字体粗细；默认主题圆角从 `sm` 改为 `md`；所有组件支持逻辑边距/内边距样式属性。
- 📚 **文档与工具**：新增自定义组件、受控与非受控组件等指南；发布 `@mantine/mcp-server` 包，通过 Model Context Protocol 提供文档数据。

---

### [React巴黎26 - YouTube](https://www.youtube.com/playlist?list=PL53Z0yyYnpWhsizNWtlnyM7XWFUSw437J)

**原文标题**: [React Paris 26 - YouTube](https://www.youtube.com/playlist?list=PL53Z0yyYnpWhsizNWtlnyM7XWFUSw437J)

该页面为YouTube平台的官方信息与政策说明区域，涵盖服务条款、隐私政策及功能说明等内容。

- 📄 关于平台的基本信息与介绍
- 📰 新闻与公告发布
- ©️ 版权政策与保护措施
- 📞 用户联系与反馈渠道
- 🛠️ 创作者工具与资源
- 📢 广告合作与商业化选项
- 💻 开发者接口与技术文档
- ⚖️ 服务条款与使用协议
- 🔒 隐私政策与数据安全
- ⚙️ 平台运作机制说明
- 🧪 新功能测试与更新
- ™️ 商标与所有权声明（谷歌公司2026）

---

### [React Native 0.85 - 全新动画后端与Jest预设包发布 · React Native](https://reactnative.dev/blog/2026/04/07/react-native-0.85)

**原文标题**: [React Native 0.85 - New Animation Backend, New Jest Preset Package · React Native](https://reactnative.dev/blog/2026/04/07/react-native-0.85)

React Native 0.85 版本发布，引入了新的共享动画后端，将 Jest 预设移至独立包，并包含多项开发工具改进、Metro 服务器 TLS 支持及多项破坏性变更。

- 🎬 **新动画后端**：与 Software Mansion 合作构建的共享动画后端，支持 Animated 和 Reanimated，现可原生驱动布局属性动画。
- 🔧 **开发工具增强**：支持多 CDP 连接、macOS 原生标签页及恢复 Android 网络面板请求预览。
- 🔒 **Metro TLS 支持**：开发服务器现可配置 TLS，启用 HTTPS 和 WSS 连接，便于本地安全测试。
- 📦 **Jest 预设独立包**：Jest 预设从核心包移至 `@react-native/jest-preset`，减小包体积并提升灵活性。
- 🚫 **Node.js 版本更新**：停止支持 EOL 的 Node.js 版本，最低要求为 v20.19.4 或 v22+。
- 🗑️ **API 清理**：移除已弃用的 `StyleSheet.absoluteFillObject`，推荐使用 `StyleSheet.absoluteFill`。
- ⚙️ **其他破坏性变更**：包括 Android 和 iOS 的架构清理、类型别名移除及多项内部 API 调整。
- 📈 **依赖更新**：Metro 升级至 ^0.84.0，React 使用 Hermes 250829098.0.10，并包含多项 TypeScript 和构建改进。

---

### [TanStack Start：一个以客户端为先的Web框架 - Tanner Linsley - YouTube](https://www.youtube.com/watch?v=8XGcc-FRPuo)

**原文标题**: [TanStack Start: A Client First Web Framework - Tanner Linsley - YouTube](https://www.youtube.com/watch?v=8XGcc-FRPuo)

该页面为YouTube网站的页脚导航部分，列出了平台的关键政策、功能说明及法律信息。

- 📄 关于平台的基本信息与介绍
- 📰 新闻与媒体相关资源
- ©️ 版权声明与知识产权说明
- 📞 联系与用户支持渠道
- 🧑‍🎨 内容创作者相关资源
- 📢 广告与商业合作信息
- 👨‍💻 开发者工具与API资源
- ⚖️ 服务条款与使用协议
- 🔒 隐私政策与数据保护
- 🛡️ 平台安全与政策说明
- ⚙️ YouTube功能运作原理
- 🧪 新功能测试与更新
- 🏢 2026年谷歌公司版权所有

---

### [MDN新前端技术内幕](https://developer.mozilla.org/en-US/blog/mdn-front-end-deep-dive/)

**原文标题**: [Under the hood of MDN's new frontend](https://developer.mozilla.org/en-US/blog/mdn-front-end-deep-dive/)

去年，MDN推出了新的前端架构，最显著的变化是简化并统一了页面设计风格，但最大的改进在于底层代码的重构。这次重构解决了旧前端的技术债务问题，包括复杂的Webpack配置、混乱的CSS以及React应用与静态内容难以交互的困境。通过采用Web Components和Lit框架，团队成功将交互功能模块化，并利用服务器端组件优化了性能。新架构支持按需加载资源，显著提升了开发体验和页面加载速度，同时基于Baseline项目确保了对现代Web技术的广泛兼容性。

- 🚀 **前端重构**：MDN去年推出了全新的前端架构，表面是设计风格的统一，核心是底层代码的彻底重写。
- 🛠️ **技术债务清理**：旧前端基于React，存在复杂的Webpack配置、CSS混乱及与静态内容交互困难等问题，维护成本高。
- 🔗 **Web Components应用**：采用Lit框架开发Web Components，解决了在静态内容中嵌入交互功能（如Scrimba学习模块）的难题。
- ⚡ **性能优化**：通过服务器端组件和按需加载机制，仅加载页面所需的CSS和JavaScript，提升加载速度并减少资源浪费。
- 🌐 **开发体验提升**：使用Rspack构建工具，将开发环境启动时间从2分钟缩短至2秒，简化了命令流程并提高了开发效率。
- 📊 **兼容性保障**：依据Baseline项目标准选择Web技术，确保新功能在广泛浏览器中的可用性，减少对Polyfill的依赖。
- 🔧 **架构简化**：摒弃了复杂的SPA架构，采用扁平化的组件结构，使组件管理更直观，降低了维护复杂度。
- 🤝 **社区参与**：鼓励开发者在GitHub提交问题或贡献代码，并通过Discord频道进行技术交流。

---

### [使用Sentry追踪优化React Native结账性能 | Sentry](https://sentry.io/cookbook/track-checkout-performance-react-native/?utm_source=reactstatus&utm_medium=paid-community&utm_campaign=mobile-fy27q1-cookbook&utm_content=newsletter-link-rn-tracing-trysentry)

**原文标题**: [Fix Checkout Performance in React Native with Sentry Tracing | Sentry](https://sentry.io/cookbook/track-checkout-performance-react-native/?utm_source=reactstatus&utm_medium=paid-community&utm_campaign=mobile-fy27q1-cookbook&utm_content=newsletter-link-rn-tracing-trysentry)

本文介绍了如何利用Sentry追踪工具监控和优化React Native应用的结账流程性能，涵盖从启用分布式追踪到设置警报和仪表板的完整步骤。

- 🛠️ **启用追踪与设置传播目标**：在React Native应用中初始化Sentry SDK，设置`tracesSampleRate`并配置`tracePropagationTargets`以连接前端与Python后端，实现分布式追踪。
- 📱 **添加结账屏幕完全显示时间**：通过`Sentry.TimeToFullDisplay`组件手动标记屏幕内容加载完成，补充自动记录的初始显示时间（TTID）。
- ⏱️ **创建结账操作自定义跨度**：使用`Sentry.startSpan`包装关键操作（如加载目录和处理结账），添加可过滤属性以便后续分析。
- 📊 **在移动洞察中查看性能数据**：通过Sentry的移动洞察功能查看平均显示时间、冷启动时间及事务持续时间，定位结账屏幕性能。
- 🔍 **深入分析慢速事务**：从事务列表中筛选慢速结账事务，通过事务摘要中的瀑布图识别耗时操作（如慢速HTTP请求）。
- 🌐 **在追踪浏览器中探索跨度**：使用追踪浏览器查看完整追踪链路，包括后端耗时，支持按属性分组和分位数对比分析。
- ⚡ **优化后端端点并验证**：针对识别的慢速请求进行优化（如缓存、查询优化），重新部署后通过追踪浏览器对比性能改进。
- 🚨 **设置慢速结账警报**：基于结账跨度筛选条件创建警报，设定阈值（如平均持续时间超过1秒）并配置通知方式（如邮件或Slack）。
- 📈 **添加结账处理时间仪表板组件**：在仪表板中创建组件，配置数据集为跨度、Y轴为平均持续时间，并过滤结账操作跨度以持续监控性能。

---

### [信号，基于推拉算法的原理 — 威利·布劳纳](https://willybrauner.com/journal/signal-the-push-pull-based-algorithm)

**原文标题**: [Signals, the push-pull based algorithm — Willy Brauner](https://willybrauner.com/journal/signal-the-push-pull-based-algorithm)

Signals是响应式编程的核心机制，通过push-pull算法实现细粒度响应式更新。push机制在信号变更时立即通知依赖项，而pull机制在计算值被读取时才惰性重新计算。系统通过全局STACK自动追踪依赖关系，并利用dirty标志实现缓存失效，确保高效更新。

- 🚀 **Push机制**：信号变更时立即向订阅者推送通知，实现快速依赖传播
- 🐌 **Pull机制**：计算值仅在读取时重新计算，通过dirty标志控制缓存失效
- 🧲 **自动依赖追踪**：利用全局STACK在运行时动态建立信号与计算值间的关联
- 🔄 **双向传播**：push向下传播失效通知，pull向上触发重新计算
- 🏗️ **响应式范式**：继承自1970年代的反应式编程思想，类似电子表格的自动更新
- ⚡ **框架应用**：已被Solid、Vue、Preact等现代前端框架广泛采用
- 🔮 **未来标准**：TC39提案正在推动Signals成为JavaScript原生特性
- 🛠️ **实现核心**：通过signal/computed函数构建响应式图，支持复杂依赖关系

---

### [移动铁路前端脱离Next.js](https://blog.railway.com/p/moving-railways-frontend-off-nextjs)

**原文标题**: [Moving Railway's Frontend Off Next.js](https://blog.railway.com/p/moving-railways-frontend-off-nextjs)

Railway 已将其前端从 Next.js 迁移至 Vite + TanStack Router，以提升开发效率和构建速度，同时保持零停机。

- 🚀 **构建速度大幅提升**：前端构建时间从超过 10 分钟缩短至不到 2 分钟，显著加快了迭代速度。
- 🛠️ **选择更适合的技术栈**：由于产品以客户端为主，Next.js 的服务器优先模式不再适用，TanStack Start + Vite 提供了更匹配的客户端优先、显式开发模型。
- 🔄 **无缝迁移过程**：通过两个 PR 完成迁移，第一个移除 Next.js 特定依赖，第二个直接替换框架，实现了零停机部署。
- 📦 **优化资产与缓存策略**：利用 Vite 的模块化打包和 Fastly 边缘缓存，实现资源的高效分发与缓存，提升用户体验。
- ⚖️ **权衡与取舍**：放弃了 Next.js 的内置图像优化和部分生态系统工具，转而使用自有方案，并接受了新框架的成熟度风险。
- 🌐 **基础设施无需改动**：迁移过程中，Railway 自身的基础设施支持了平滑过渡，预览部署和健康检查等功能保持不变。
- ⏱️ **加速迭代周期**：通过减少构建和部署时间，缩短了从代码编写到用户可见的周期，提升了整体开发效率。

---

### [React 颜色选择器组件](https://uiwjs.github.io/react-color/)

**原文标题**: [Color picker component for React.](https://uiwjs.github.io/react-color/)

该应用需要启用JavaScript才能正常运行。

- 🛠️ 技术依赖：必须开启JavaScript功能以支持应用交互
- 🌐 运行环境：确保浏览器设置允许执行脚本
- ⚙️ 核心提示：页面功能完全依赖JavaScript技术实现

---

### [骨场 - 为你的用户界面准备的骨架屏](https://boneyard.vercel.app/overview)

**原文标题**: [boneyard - skeleton screens for your UI](https://boneyard.vercel.app/overview)

Boneyard-js 是一个用于生成骨架屏的 JavaScript 库，通过自动捕捉真实 UI 的布局来创建像素级匹配的骨架屏，无需手动测量或调整。

- 🛠️ **自动生成骨架**：通过 CLI 工具自动检测开发服务器和 Tailwind 断点，生成与真实布局完全同步的骨架屏 JSON 数据。
- 📦 **简单集成**：使用 `<Skeleton>` 组件包裹目标组件，只需运行一次构建命令并导入注册表即可自动解析骨架数据。
- ⚡ **高效性能**：运行时仅约 7.5KB，骨架数据以紧凑的数组格式存储，支持增量构建以提升效率。
- 🎯 **零布局偏移**：骨架屏基于实际渲染内容提取，确保加载过程中页面布局稳定无跳动。

---

### [Docusaurus 3.10 | Docusaurus](https://docusaurus.io/blog/releases/3.10)

**原文标题**: [Docusaurus 3.10 | Docusaurus](https://docusaurus.io/blog/releases/3.10)

Docusaurus 3.10 是 v3.x 系列的最后一个版本，旨在帮助用户为即将到来的 Docusaurus v4 做准备。此版本引入了多项新功能和改进，包括安全增强、性能优化、更严格的 MDX 语法支持，以及实验性的版本控制系统（VCS）API。同时，它提供了 v4 未来标志，允许用户逐步启用 v4 中的破坏性变更，确保平稳升级。

- 🚀 **v4 未来标志**：新增多个未来标志（如 `future.v4.siteStorageNamespacing`、`future.v4.fasterByDefault`），帮助用户提前适配 v4 的破坏性变更，如存储键自动命名空间和默认启用更快构建。
- 🔒 **安全增强**：采用 npm 可信发布机制，新增安全工作流以检测依赖漏洞，并推荐使用包管理器（如 pnpm）的发布冷却期等功能来保护站点供应链。
- ⚡ **Docusaurus Faster 稳定版**：更快构建基础设施（包括 Rspack、SWC）现已稳定，并将在 v4 中默认启用，同时支持 Yarn PnP 和新的 `gitEagerVcs` 标志以提升性能。
- 💾 **站点存储 API 稳定**：`config.storage` API 标记为稳定，v4 将默认自动为存储键添加命名空间，避免 `localStorage` 键冲突。
- 📝 **严格 MDX 语法**：鼓励使用原生 MDX 语法（如 `:::type[标题]` 警告、JSX 注释 `{/* */}`、MDX 注释标题 ID），以提高文档可移植性和生态系统兼容性，并为 v4 默认禁用 MDX v1 兼容选项做准备。
- 🔧 **实验性 VCS API**：新增版本控制系统 API，支持集成 Git 以外的 VCS，并内置 Git Eager 策略以显著提升大型站点的构建性能。
- 🌍 **翻译更新**：新增乌尔都语（ur）主题翻译，并补全巴西葡萄牙语（pt-BR）翻译。
- 🛠️ **其他改进**：包括 TypeScript 6.0 支持、`siteConfig.headTags` API 增强、实时代码块主题重置按钮、`<DocCard>` 和 `<Tabs>` 组件优化，以及多项错误修复和依赖项精简。

---

### [GitHub - uiwjs/react-md-editor: 一款基于React.js和TypeScript实现的简易Markdown编辑器，支持预览功能。· GitHub](https://github.com/uiwjs/react-md-editor)

**原文标题**: [GitHub - uiwjs/react-md-editor: A simple markdown editor with preview, implemented with React.js and TypeScript. · GitHub](https://github.com/uiwjs/react-md-editor)

这是一个基于 React 和 TypeScript 实现的简单 Markdown 编辑器，支持实时预览、语法高亮、自定义工具栏等功能，不依赖其他现代编辑器。

- 📦 **轻量封装**：基于 `textarea` 封装，不依赖 Ace、CodeMirror 等大型编辑器。
- 🚀 **功能丰富**：支持 GitHub 风格 Markdown、自动列表、Tab 缩进、行复制/移动、暗黑模式等。
- 🔧 **高度可定制**：提供无头模式、自定义工具栏、国际化、KaTeX 数学公式和 Mermaid 图表支持。
- 🛡️ **安全可控**：支持通过 `rehype-sanitize` 防止 XSS 攻击，可禁用特定 HTML 元素。
- 📱 **灵活集成**：兼容 Next.js，支持响应式高度、占位符、最大长度限制及多种预览模式。
- 📄 **多场景适用**：提供纯预览组件、代码高亮优化版本及详细的开发文档和示例。

---

### [React Markdown 编辑器](https://raw.githack.com/uiwjs/react-md-editor/2f25d39/index.html)

**原文标题**: [Markdown Editor for React.](https://raw.githack.com/uiwjs/react-md-editor/2f25d39/index.html)

本文介绍了人工智能在医疗领域的应用现状与前景，重点探讨了其在疾病诊断、药物研发和个性化治疗方面的突破性进展，同时简要提及了相关的伦理挑战。

- 🏥 AI辅助诊断系统能通过分析医学影像快速识别病变，提升早期癌症等疾病的检出率
- 🔬 机器学习加速了新药研发过程，大幅缩短化合物筛选与临床试验周期
- 📊 基于患者数据的个性化治疗方案正成为现实，AI能预测药物反应并优化治疗路径
- ⚖️ 数据隐私与算法透明度等伦理问题仍需在技术发展中同步解决

---

### [GitHub - ankeetmaini/react-infinite-scroll-component: 一个超棒的React无限滚动组件。· GitHub](https://github.com/ankeetmaini/react-infinite-scroll-component)

**原文标题**: [GitHub - ankeetmaini/react-infinite-scroll-component: An awesome Infinite Scroll component in react. · GitHub](https://github.com/ankeetmaini/react-infinite-scroll-component)

这是一个用于React的无限滚动组件，体积小巧（4.15 kB），支持下拉刷新功能，易于集成。

- 📦 **安装与引入**：可通过npm或yarn安装，支持ES6和CommonJS模块导入。
- 🔄 **核心功能**：组件通过监听滚动位置自动触发数据加载，支持自定义加载提示和结束信息。
- ⬇️ **下拉刷新**：提供可选的“下拉刷新”功能，包含阈值设置和自定义提示内容。
- 🎯 **滚动容器**：支持在指定高度的元素、父级滚动容器或全局窗口（body）中进行滚动。
- ⚙️ **丰富配置**：提供如`next`、`hasMore`、`dataLength`、`loader`、`scrollThreshold`等多项属性以控制滚动行为。
- 🔄 **反向滚动**：通过设置`inverse`属性，可实现从顶部开始加载内容的无限滚动（如聊天记录）。
- 📚 **文档与示例**：提供详细的版本化文档和多个在线示例，展示不同使用场景。
- 👥 **社区贡献**：项目遵循all-contributors规范，由多位贡献者共同维护，采用MIT开源协议。

---

### [发布 v7.0.0 · ankeetmaini/react-infinite-scroll-component · GitHub](https://github.com/ankeetmaini/react-infinite-scroll-component/releases/tag/v7.0.0)

**原文标题**: [Release v7.0.0 · ankeetmaini/react-infinite-scroll-component · GitHub](https://github.com/ankeetmaini/react-infinite-scroll-component/releases/tag/v7.0.0)

该开源库发布了7.0.0版本，主要更新包括提升React和Node.js的最低版本要求、升级开发工具链，并引入了新的JSX转换方式。

- 🚀 **版本升级**：发布v7.0.0版本，要求React版本至少为17.0.0，Node.js版本至少为18.18.0
- ⚙️ **工具链更新**：升级了Jest、Husky和Storybook等开发工具，采用新的JSX转换方式，无需再引入React
- ⚠️ **重大变更**：不再支持React 16及以下版本和Node 16及以下版本，但API接口保持不变
- 📦 **安装方式**：可通过npm或yarn安装，具体命令为`npm install react-infinite-scroll-component`或`yarn add react-infinite-scroll-component`
- 🔄 **迁移指南**：若项目仍在使用React 16，需先升级至React 17，但无需修改现有代码接口

---

### [GitHub - mkuczera/react-native-haptic-feedback：恰到好处的触觉反馈：Core Haptics、AHAP文件、模式符号及适用于iOS与Android的跨平台工具集。](https://github.com/mkuczera/react-native-haptic-feedback)

**原文标题**: [GitHub - mkuczera/react-native-haptic-feedback: Haptics that feel right: Core Haptics, AHAP files, pattern notation, and cross-platform utilities for iOS and Android. · GitHub](https://github.com/mkuczera/react-native-haptic-feedback)

这是一个用于 React Native 的全面触觉反馈库，支持 iOS 的 Core Haptics 和 Android 的丰富 API，提供自定义模式、开发者友好的钩子以及跨平台实用工具。

- 📱 **跨平台支持**：为 iOS（Core Haptics）和 Android（Vibrator API）提供丰富的触觉反馈功能。
- 🛠️ **核心 API**：提供 `trigger`、`impact`、`stop`、`isSupported` 等方法来触发和控制触觉效果。
- 🎛️ **自定义模式**：支持通过 `triggerPattern` 和简洁的符号（如 `oO.O`）创建自定义触觉序列。
- 🍎 **AHAP 文件支持**：在 iOS 上可直接播放 Apple Haptic and Audio Pattern 文件，并提供了跨平台包装器 `playHaptic`。
- ⚙️ **系统状态与开关**：可获取设备触觉状态（如振动是否启用）并设置全局启用/禁用开关。
- 🎨 **预设与组件**：内置多种预设模式（如成功、错误），并提供 `useHaptics` 钩子和 `TouchableHaptic` 组件方便集成。
- 📋 **平台内部机制**：详细说明了 iOS 的三层回退链和 Android 的 API 层级支持，帮助诊断设备兼容性问题。
- 🧪 **测试与迁移**：提供 Jest 模拟，并包含从 v2 迁移到 v3 的指南。
- 🌐 **附加资源**：拥有配套测试应用、完整文档网站，并感谢相关开源贡献者。

---

### [GitHub - gilbarbara/react-inlinesvg: ReactJS的SVG加载器组件 · GitHub](https://github.com/gilbarbara/react-inlinesvg)

**原文标题**: [GitHub - gilbarbara/react-inlinesvg: An SVG loader component for ReactJS · GitHub](https://github.com/gilbarbara/react-inlinesvg)

这是一个用于在React应用中内联加载SVG的组件库，支持本地、远程或数据URI形式的SVG资源，并提供了丰富的自定义选项。

- 🏖 **易于使用**：只需设置`src`属性即可加载SVG
- 🛠 **高度灵活**：提供多种配置选项，如缓存、唯一ID生成和预处理函数
- ⚡️ **智能缓存**：支持内存缓存和浏览器持久化缓存（通过CacheProvider）
- 🚀 **服务端渲染友好**：完全支持SSR环境
- 🌐 **浏览器兼容**：支持所有支持SVG和fetch的浏览器，可通过polyfill兼容旧版
- 🔧 **丰富功能**：包含加载状态、错误处理、自定义标题/描述等特性
- 📦 **多种加载方式**：支持URL、路径、数据URI和原始SVG字符串
- 🛡 **CORS支持**：正确处理跨域SVG加载
- 🎨 **样式控制**：支持通过CSS样式化内联SVG，解决传统SVG使用中的样式限制问题

---

### [GitHub - remarkablemark/html-react-parser: 📝 HTML 转 React 解析器。· GitHub](https://github.com/remarkablemark/html-react-parser)

**原文标题**: [GitHub - remarkablemark/html-react-parser: 📝 HTML to React parser. · GitHub](https://github.com/remarkablemark/html-react-parser)

这是一个名为 html-react-parser 的 JavaScript 库，用于将 HTML 字符串解析为 React 元素，支持在服务器端（Node.js）和客户端（浏览器）使用。

- 📦 **功能概述**：该库的核心功能是将 HTML 字符串转换为一个或多个 React 元素，便于在 React 应用中动态渲染 HTML 内容。
- ⚙️ **主要特性**：提供 `replace` 和 `transform` 等选项，允许开发者在解析过程中替换元素、转换属性或自定义处理逻辑。
- 🛠️ **安装方式**：支持通过 NPM、Yarn 或 CDN 安装，并兼容 ES 模块和 CommonJS 模块导入。
- 🧩 **使用示例**：支持解析单个元素、多个相邻元素、嵌套元素及带属性的元素，并可通过选项灵活控制解析行为。
- ⚠️ **注意事项**：库本身不提供 XSS 安全防护或 HTML 消毒功能，且部分配置（如 `htmlparser2` 选项）仅在服务器端生效。
- 🔄 **迁移指南**：文档提供了从旧版本升级的详细说明，包括 TypeScript 类型调整和 API 变更。
- ❓ **常见问题**：涵盖了脚本标签处理、属性调用、SSR 支持、标签大小写控制等常见问题的解答。
- 📊 **性能信息**：包含基准测试结果和包大小检查，帮助开发者评估解析性能。
- 👥 **贡献与支持**：项目欢迎代码贡献和资金支持，并提供了多种赞助方式。

---

### [React-日历](https://projects.wojtekmaj.pl/react-calendar/)

**原文标题**: [React-Calendar](https://projects.wojtekmaj.pl/react-calendar/)

本文介绍了人工智能在医疗领域的应用现状与前景，重点探讨了其在疾病诊断、药物研发和个性化治疗方面的突破性进展，同时简要提及了相关的伦理挑战。

- 🏥 AI辅助诊断系统能通过分析医学影像快速识别病灶，提升早期癌症等疾病的检出率
- 🔬 机器学习加速了新药研发过程，大幅缩短化合物筛选与临床试验周期
- 📊 基于患者基因数据的人工智能模型可为慢性病患者提供个性化治疗方案
- ⚖️ 医疗AI面临数据隐私、算法透明度及责任认定等伦理监管问题

---

### [GitHub - Shopify/react-native-skia: 使用Skia实现高性能React Native图形渲染 · GitHub](https://github.com/Shopify/react-native-skia)

**原文标题**: [GitHub - Shopify/react-native-skia: High-performance React Native Graphics using Skia · GitHub](https://github.com/Shopify/react-native-skia)

React Native Skia 是一个由 Shopify 维护的开源项目，它将高性能的 Skia 2D 图形引擎引入 React Native，用于实现复杂的图形渲染。

- 🎨 **高性能图形库**：基于 Skia 引擎，为 React Native 提供强大的 2D 图形绘制能力。
- 🌐 **广泛应用**：Skia 是 Chrome、Android、Flutter 等众多知名产品的图形引擎。
- 📦 **安装与使用**：提供完整的安装指南和详细文档，支持通过 npm/yarn 快速集成。
- 🔬 **实验性功能**：提供 Graphite 后端预览版（@next 渠道），适用于高级用例，但暂不建议生产环境使用。
- 🤝 **开源贡献**：项目遵循 MIT 许可证，欢迎开发者参与贡献，有明确的开发与测试指南。
- 📊 **项目活跃**：拥有 8.3k 星标、586 复刻和活跃的社区维护，定期发布更新版本。
- ⚙️ **多语言实现**：核心代码主要使用 TypeScript 和 C++ 编写，确保跨平台性能与一致性。

---

### [SerpApi 游乐场 - SerpApi](https://serpapi.com/playground/?utm_source=cooperpress&utm_campaign=react_classified)

**原文标题**: [SerpApi Playground - SerpApi](https://serpapi.com/playground/?utm_source=cooperpress&utm_campaign=react_classified)

SerpApi Playground 是一个用于测试和探索搜索引擎结果页（SERP）数据的工具，支持多种搜索引擎和功能模块，便于开发者集成和调试。

- 🔍 支持多种搜索引擎，包括 Google、Bing、Baidu、Yandex 等，覆盖全球主流搜索平台
- 🛠️ 提供丰富功能模块，如 AI 概述、本地服务、购物、视频、地图等，满足多样化数据需求
- 📊 可获取结构化数据，包括 JSON 格式结果，便于自动化处理和数据分析
- 🔄 包含历史记录和代码导出功能，方便回溯测试结果并集成到开发项目中
- 🌐 涵盖额外平台如电商（Amazon、eBay）、社交媒体（Facebook、YouTube）和本地服务（Yelp、Tripadvisor），扩展数据采集范围

---

### [GitHub - audiojs/web-audio-api: Web音频API的便携式实现 · GitHub](https://github.com/audiojs/web-audio-api)

**原文标题**: [GitHub - audiojs/web-audio-api: Portable implementation of Web audio API · GitHub](https://github.com/audiojs/web-audio-api)

这是一个用于Node.js环境的Web Audio API实现，无需浏览器即可在服务器端或命令行中处理音频。

- 🎵 **便携式Web Audio API** – 提供完整的Web Audio API polyfill，100%通过WPT一致性测试，无原生依赖。
- 🖥️ **服务器端音频处理** – 支持在Node.js中离线渲染音频、CLI脚本音频生成以及API和流水线中的音频合成。
- 🔌 **兼容主流库** – 可与Tone.js等Web音频库无缝协作，在Node环境中直接使用。
- 📦 **易于安装使用** – 通过npm安装，内置扬声器输出支持，无需额外设置。
- 🧪 **丰富的示例** – 包含测试信号、听觉错觉、合成器、生成式音乐等多种音频示例，支持参数化调用。
- ⚙️ **Node.js扩展功能** – 提供超出标准的Node专属功能，如通过回调注册处理器、将音频输出到任意可写流等。
- ❓ **常见问题解答** – 涵盖上下文关闭、Tone.js集成、音频文件解码、单元测试和性能基准等实用信息。
- 🏗️ **拉取式架构设计** – 采用基于音频图的拉取式渲染，128样本量子化处理，DSP内核与图逻辑分离，便于未来WASM替换。
- 📄 **MIT许可证** – 开源项目，拥有活跃的社区贡献和版本发布。

---

### [阅读代码前我运行的Git命令](https://piechowski.io/post/git-commands-before-reading-code/)

**原文标题**: [The Git Commands I Run Before Reading Any Code](https://piechowski.io/post/git-commands-before-reading-code/)

在接手新代码库时，作者会先运行五个Git命令来分析提交历史，从而快速了解项目的健康状况、风险区域和团队动态，而不是直接阅读代码文件。

- 🔄 **高频变更文件**：列出过去一年中修改最频繁的20个文件，高变更率且无人愿意负责的文件通常是代码库的“痛点”和主要风险源。
- 👥 **贡献者分析**：通过提交数量排名识别核心贡献者，若单人贡献超过60%则存在“巴士因子”风险，同时关注近期活跃度以评估知识传承情况。
- 🐛 **缺陷聚集区**：筛选涉及修复、缺陷等关键词的提交，找出常出问题的文件，若与高频变更文件重叠则代表最高风险代码。
- 📈 **项目活跃度趋势**：按月统计提交数量，通过变化曲线判断团队是保持稳定节奏、失去动力还是采用批量发布模式。
- 🚨 **紧急修复频率**：统计一年内的回滚、热修复等紧急提交，高频出现意味着部署流程或测试可靠性存在问题，低频则可能反映稳定性或提交信息不规范。

---

### [介绍JetStream 3基准测试套件 | WebKit](https://webkit.org/blog/17899/introducing-the-jetstream-3-benchmark-suite/)

**原文标题**: [  Introducing the JetStream 3 Benchmark Suite | WebKit](https://webkit.org/blog/17899/introducing-the-jetstream-3-benchmark-suite/)

JetStream 3.0 是 WebKit、Google 和 Mozilla 联合推出的跨浏览器基准测试套件重大更新，旨在更全面地衡量现代 Web 应用性能，特别是 WebAssembly 和 JavaScript 的执行效率。它摒弃了过时的微基准测试，采用更大规模、更真实的工作负载，并统一了 JavaScript 和 WebAssembly 的评分方法，以反映从启动到持续运行的完整生命周期性能。

- 🚀 **WebAssembly 评分方法革新**：JetStream 3 取消了独立的启动/运行时评分，改为与 JavaScript 相同的多迭代评分，涵盖首次迭代（启动成本）、最差情况迭代（卡顿）和平均情况迭代（持续吞吐量），确保引擎优化 WebAssembly 实例的完整生命周期。
- 📈 **摆脱微基准测试陷阱**：通过采用更大、更复杂的工作负载，减少对单一“热点”函数的过度优化，促使引擎在 JIT 编译器和标准库功能上实现更广泛的效率提升。
- 🛠️ **WebAssembly GC 性能优化**：通过内联 GC 分配、改进内存布局和消除对象析构函数，将 WasmGC 子测试性能提升约 40%，显著减少了垃圾回收开销。
- 🔍 **类型检查与间接调用优化**：采用 Cohen 类型显示算法内联类型检查，并通过分析间接调用站点实现多态内联，提升了 Dart、Kotlin 等语言编译代码的执行效率。
- ⚙️ **编译器与寄存器分配器改进**：引入贪婪寄存器分配器替代原有算法，提升编译速度和代码质量；同时改进内联启发式方法，基于调用反馈优化代码大小和性能。
- 🔢 **BigInt 与异步函数增强**：优化 BigInt 的乘除算法和内存布局，提升大整数运算性能；重写微任务队列并将 Promise 实现移至 C++，显著提高异步代码执行效率。
- 🌐 **SIMD 与解释器支持**：在 JavaScriptCore 的解释器层 IPInt 中全面支持 SIMD 指令，使 SIMD 代码能够近乎即时启动，即使在 JIT 禁用的情况下也能运行。
- 📊 **性能提升成果**：这些架构改进使 Safari 26.4 相比 26.0 版本在 JetStream 3 上性能提升约 10%，为用户带来更快的页面加载和更流畅的交互体验。

---

### [2026年人工智能发展状况](https://survey.devographics.com/en-US/survey/state-of-ai/2026)

**原文标题**: [State of AI 2026](https://survey.devographics.com/en-US/survey/state-of-ai/2026)

本文介绍了2026年“Web开发AI现状”调查的启动，探讨了AI对程序员职业的潜在影响，并提供了调查的详细信息。

- 🕐 调查预计耗时约15分钟，面向所有经验水平的Web开发者
- 🎯 旨在了解现代AI工具如何影响Web开发领域
- 📊 收集的数据将用于发布免费在线报告，并按要求提供完整数据集
- 👥 由Devographics团队与志愿者及社区共同运作
- 📅 调查时间为2026年4月10日至5月10日，结果随后发布
- 🌍 提供多语言翻译支持，由社区志愿者协助完成

---

### [JSHeroes 2026 | 社区组织的JS大会](https://jsheroes.io/)

**原文标题**: [JSHeroes 2026 | Community Organized JS Conference](https://jsheroes.io/)

JSHeroes 2026 是一场在罗马尼亚克卢日-纳波卡举办的为期两天的社区非营利性 JavaScript 与前端技术会议，旨在汇聚全球开发者，探讨未来技术趋势、分享实践经验，并关注开发者成长与行业人文关怀。

- 🧭 **主题前瞻**：会议聚焦 2026 年工程架构趋势、工具框架演进、AI 对开发的影响，以及适应变化所需的技能与职业发展。
- 🧑‍💻 **讲者阵容**：汇聚了来自 Deno、Vercel、Cloudflare 等公司的多位技术专家，涵盖 JavaScript、性能优化、可访问性、Web Components、Node.js 等广泛领域。
- 🗣️ **专题演讲**：包括《JavaScript 时间旅行指南》、《用逆向工程消除信任问题》、《前端代码法医分析》、《Web 组件样式实践》、《认知负荷危机》等实战与深度议题。
- ⏰ **日程安排**：为期两天，包含主题演讲、分组讨论、交流环节，重点关注开发体验、代码质量、性能、创意编码等方向。
- ♿ **包容体验**：会议在五星级酒店举办，场地充分考虑无障碍设施，并提供多样化的饮食选择。
- ❤️ **社区驱动**：由志愿者团队组织，秉承开源透明理念，旨在促进知识分享与社区共建，并公开所有会议数据。
- 👥 **团队协作**：活动由多位组织者、志愿者及品牌大使共同筹备，确保内容质量与活动流畅体验。
- 🤝 **赞助合作**：得到多家金牌、铜牌赞助商及媒体伙伴的支持，共同推动会议成功举办。

---

