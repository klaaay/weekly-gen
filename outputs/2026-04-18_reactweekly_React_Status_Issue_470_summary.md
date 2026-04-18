### [React Server Components 随心所欲 | TanStack 博客](https://tanstack.com/blog/react-server-components)

**原文标题**: [React Server Components Your Way | TanStack Blog](https://tanstack.com/blog/react-server-components)

TanStack 提出了一种全新的 React Server Components（RSC）实现模型，将其视为可获取、可缓存的数据流而非服务器主导的组件树，从而提供更灵活的架构选择。该模型通过 TanStack Start 框架实现，允许开发者按需使用 RSC，并引入了创新的 Composite Components 概念，使客户端能够自主填充服务器组件的插槽，实现更自由的 UI 组合。

- 🚀 **RSC 作为数据流**：TanStack 将 RSC 视为可获取、可缓存的 React Flight 数据流，而非强制性的应用架构核心，提供了更细粒度的控制。
- 🛠️ **灵活的集成方式**：开发者可以在服务器任意位置创建 RSC 流，并在客户端或 SSR 中解码，无需依赖特定的框架约定。
- 💾 **简化的缓存策略**：RSC 流可像普通数据一样被缓存，兼容 TanStack Query、Router 及 CDN 等现有缓存层，无需重新设计缓存逻辑。
- 🛡️ **增强的安全性**：采用明确的 RPC（通过 `createServerFn`）而非隐式的 `'use server'` 操作，减少攻击面，强调输入验证与身份验证。
- 🌈 **覆盖全场景频谱**：支持从完全交互式 SPA 到完全静态页面的所有前端用例，允许按路由、组件或用例灵活选择模式。
- 📊 **实际的性能收益**：在 TanStack.com 的内容密集型页面（如博客、文档）中应用 RSC 后，有效减少了客户端 JavaScript 体积，提升了 Lighthouse 分数并降低了阻塞时间。
- 🔀 **创新的 Composite Components**：引入新概念，允许服务器组件定义“插槽”，由客户端决定填充何种交互式 UI，实现了服务器与客户端在组件树组合上的责任分离。
- ⚠️ **当前为实验性功能**：RSC 支持在 TanStack Start RC 中处于实验阶段，API 可能调整，且暂未集成框架的序列化功能。
- ❓ **明确的定位对比**：与 Next.js App Router 的服务器优先模型不同，TanStack Start 采用同构优先，RSC 是可选的优化工具而非强制架构。

---

### [安装 Vega SDK 与开发者工具 | Vega 入门指南](https://developer.amazon.com/docs/vega/0.22/setup-overview.html?sc_category=PAI&sc_channel=3P&sc_publisher=RS&sc_campaign=ACQ_VG&sc_country=US&sc_detail=RSTATUS-5_VG_101)

**原文标题**: [Install the Vega SDK and Developer Tools | Vega Get Started ](https://developer.amazon.com/docs/vega/0.22/setup-overview.html?sc_category=PAI&sc_channel=3P&sc_publisher=RS&sc_campaign=ACQ_VG&sc_country=US&sc_detail=RSTATUS-5_VG_101)

本文档介绍了 Vega SDK 0.22 版本的安装与开发工具配置指南，涵盖从基础安装到高级功能设置的完整流程。

- 🛠️ **安装 Vega SDK**：提供完整的安装指南，包括 CLI 工具和平台工具（如 VVD 虚拟设备）的安装与环境配置。
- ⚙️ **设置开发工具**：指导在 VS Code 中配置 Vega Studio，安装必要扩展并设置开发环境与工作区。
- 🔧 **启用开发者模式**：开启设备开发功能，支持应用测试、安全访问、包管理、调试及文件系统操作。
- 🔄 **配置快速刷新**：设置实时开发更新功能，适用于 VVD 和 Fire TV 设备，并包含常见问题排查。
- 📦 **管理包管理器**：Vega CLI 仅构建原生部分和应用包，允许自由选择 npm、Yarn 或 pnpm 等工具。
- 🧩 **设置 Yarn 工作区**：学习使用 Yarn 工作区管理 Vega TV 项目中的多个包。
- 📊 **管理遥测数据**：自动收集使用统计和错误日志，帮助 Amazon 改进工具功能与用户体验。

---

### [Reddit - 请等待验证](https://www.reddit.com/r/reactjs/comments/1shuyg4/whats_a_react_pattern_you_massused_then_realized/)

**原文标题**: [Reddit - Please wait for verification](https://www.reddit.com/r/reactjs/comments/1shuyg4/whats_a_react_pattern_you_massused_then_realized/)

本文介绍了人工智能在医疗领域的应用现状与前景，重点探讨了其在疾病诊断、治疗方案优化及医疗管理效率提升方面的作用，同时简要提及了相关的技术挑战和伦理考量。

- 🤖 AI 辅助诊断系统能通过分析医学影像快速识别病灶，提高早期疾病检出率
- 💊 基于机器学习的个性化治疗方案可结合患者数据优化用药与治疗路径
- ⚡ 智能医疗管理平台自动化处理行政流程，显著减轻医护人员行政负担
- 🧬 基因组学与 AI 结合助力精准医疗发展，加速靶向药物研发进程
- ⚖️ 数据隐私保护与算法透明度仍是医疗 AI 推广需要解决的关键伦理问题

---

### [Material UI v9.0 - MUI](https://mui.com/blog/introducing-material-ui-v9/)

**原文标题**: [Material UI v9.0 - MUI](https://mui.com/blog/introducing-material-ui-v9/)

Material UI v9.0 发布，重点提升默认无障碍支持、键盘导航可靠性和主题与 CSS 集成，并引入基于 Base UI 的新组件。

- 🎯 引入基于 Base UI 的新组件：NumberField（数字输入控件）和 Menubar（支持子菜单的水平菜单栏）
- 🎨 主题系统增强：扩展 CSS 变量以支持 color-mix()，提升派生颜色控制与设计系统集成
- 📖 文档与修复：明确 Tooltip 交互说明，修复 nativeColor 文档及多项组件无障碍问题
- ♿ 无障碍与交互改进：优化 Autocomplete、Backdrop、ButtonBase 等组件行为，提升键盘导航（如 Roving TabIndex）
- 🧹 平台清理：删除重复 CSS 规则、优化 sx 属性性能（提升达 30%）、移除 Joy UI 代码
- ⚠️ 破坏性变更：移除已弃用属性（如 component），带来约 3% 包体积缩减和整体性能提升
- 🚀 未来规划：移除 Emotion 依赖、持续性能与无障碍改进、集成更多 Base UI 组件

---

### [Material UI 与 MUI X v9 正式发布 - MUI](https://mui.com/blog/introducing-mui-v9/#one-mui-ecosystem-a-synced-major-version)

**原文标题**: [Introducing Material UI and MUI X v9 - MUI](https://mui.com/blog/introducing-mui-v9/#one-mui-ecosystem-a-synced-major-version)

Material UI 和 MUI X 同时发布 v9 版本，旨在统一生态系统，提供更一致、可预测的开发体验。此次更新聚焦于更好的集成、产品组合扩展以及 AI 工作流支持，并引入了新的组件和管理控制台。

- 🎉 **版本统一**：Material UI 和 MUI X 的主要版本号重新对齐至 v9，简化了升级和兼容性管理。
- 🧩 **组件增强**：Material UI 新增 NumberField 和 Menubar；MUI X 的 Data Grid、Charts 等组件在稳定性、可访问性和功能上得到提升。
- 🤖 **AI 工作流**：Data Grid AI Assistant 正式可用，配合新的 MUI Console 应用，便于管理许可证和 API 密钥，支持生产环境部署。
- 🆕 **新产品亮相**：MUI X 新增 Scheduler（资源日历和日程表）和 Chat（对话式 UI）组件的 alpha 版本。
- 🔄 **更名与调整**：生成式 UI 工具“MUI Chat”更名为“MUI Recipes”，以避免与新的聊天组件混淆。
- 💰 **许可更新**：MUI X 的 Pro 和 Premium 计划改为基于应用的许可模式，并更新了定价结构。
- 📊 **遥测数据**：商业组件在开发模式下默认启用遥测功能，以帮助改进产品，用户可按需选择退出。
- 🚀 **未来规划**：后续将专注于组件组合扩展、深化 AI 原生工作流，并探索移除 Emotion 依赖以改进主题分层和样式系统。

---

### [[编译器] 将 React 编译器移植到 Rust by josephsavona · Pull Request #36173 · facebook/react · GitHub](https://github.com/facebook/react/pull/36173)

**原文标题**: [[compiler] Port React Compiler to Rust by josephsavona · Pull Request #36173 · facebook/react · GitHub](https://github.com/facebook/react/pull/36173)

React Compiler 正在被移植到 Rust 语言，这是一个实验性的进行中项目，旨在提升性能并支持更多工具链集成。

- 🚀 **实验性 Rust 移植**：这是一个早期的工作版本，旨在将 React Compiler 从 TypeScript 移植到 Rust，以获取并行开发中的反馈。
- ⚙️ **架构与开发**：架构由人工设计，但大部分代码由 AI 编写，内部采用与 TS 版本相同的中间表示（HIR）和优化流程。
- 📈 **性能提升**：初步性能数据显示，Rust 版本作为 Babel 插件运行时速度提升约 3 倍，核心转换逻辑快约 10 倍。
- 🔗 **工具链集成**：目前提供了 Babel、OXC 和 SWC 的集成示例，未来计划支持更多原生集成，并优化 API 设计。
- ✅ **测试与验证**：所有 1725 个测试用例均已通过，确保与 TS 版本在输出和中间状态上的一致性。
- 🤝 **合作邀请**：项目邀请社区伙伴参与，共同将 Rust 版本集成到 OXC、SWC 等工具中，并欢迎对 AST 和范围表示提供反馈。

---

### [垂直代码库](https://tkdodo.eu/blog/the-vertical-codebase)

**原文标题**: [The Vertical Codebase](https://tkdodo.eu/blog/the-vertical-codebase)

本文讨论了代码库结构从水平划分（按类型分组）转向垂直划分（按功能或领域分组）的重要性，认为垂直结构能提高代码的内聚性、降低耦合度，更利于团队协作和长期维护。

- 🏗️ 作者反对按组件、钩子、类型、工具等类型水平划分代码库，认为这会导致代码分散且难以维护。
- 📈 水平结构在项目初期可能方便，但随着代码量增长，会变得混乱且难以重构，如 Sentry 代码库所示。
- 🤖 即使有 AI 辅助开发，良好的代码结构、边界约束和快速反馈循环对提升开发效率仍至关重要。
- 🧠 代码应遵循“共同变化的代码放在一起”的原则，减少认知负荷，垂直结构能更好地实现这一点。
- 🔗 理想代码结构应追求低耦合和高内聚，垂直分组能明确代码依赖关系，增强模块专注度。
- 🎯 垂直结构按功能或领域（如“仪表盘”、“分析”）组织代码，与产品团队架构自然契合，便于代码所有权管理。
- 🔄 确定垂直分组虽具挑战性，但通常可基于路由、页面或功能模块来划分，需团队深入思考。
- 📦 共享代码（如设计系统组件）可作为独立垂直模块处理，并通过包管理或规则明确其公共接口和依赖边界。
- 🚧 垂直结构的实施难点在于正确分类代码和避免重复实现，这需要加强团队间的沟通与协作。

---

### [获取失败](https://developer.salesforce.com/blogs/2026/04/build-with-react-run-on-salesforce-introducing-salesforce-multi-framework)

**原文标题**: [Failed to retrieve](https://developer.salesforce.com/blogs/2026/04/build-with-react-run-on-salesforce-introducing-salesforce-multi-framework)

无法总结：获取内容失败，状态码 403。

---

### [获取失败](https://spin.atomicobject.com/recreate-omnichord-for-ipad/)

**原文标题**: [Failed to retrieve](https://spin.atomicobject.com/recreate-omnichord-for-ipad/)

无法总结：获取内容失败，状态码 403。

---

### [React Native 构建优化完全指南 | 神话工程师](https://themythicalengineer.com/the-complete-guide-to-react-native-build-optimization.html)

**原文标题**: [The Complete Guide to React Native Build Optimization | The Mythical Engineer](https://themythicalengineer.com/the-complete-guide-to-react-native-build-optimization.html)

本文介绍了如何通过优化 Gradle 并行执行、加速 Metro 打包、使用 ccache 缓存 C++ 编译以及仅构建活动架构，将 React Native Android 发布构建时间从 20 多分钟大幅缩短至几分钟。

- 🐢 默认构建缓慢：React Native Android 发布构建通常耗时过长，主要因为 Gradle、Metro 和 C++ 编译器默认配置保守，未能充分利用多核 CPU。
- ⚙️ 优化 Gradle 并行执行：通过修改`gradle.properties`，启用并行任务执行、设置最大工作线程数（如 75% CPU 核心）并增加 JVM 内存分配，可使构建时间减半。
- 🚀 加速 Metro 打包：在`metro.config.js`中动态配置`maxWorkers`（如 50% CPU 核心），让 Metro 使用多个工作线程，显著提升 JavaScript 打包速度。
- 💾 使用 ccache 缓存 C++ 编译：安装并配置 ccache，缓存 TurboModules 和 Fabric 的 C++ 编译结果，后续构建命中缓存可跳过重复编译，大幅缩短时间。
- 🎯 仅构建活动架构：在开发脚本中添加`--active-arch-only`标志，让 React Native 仅针对当前设备架构构建，使调试构建提速 2-3 倍。
- 📊 验证与基准测试：提供自动化脚本（如`benchmark-build.sh`）来清理缓存、执行构建并生成性能报告，帮助量化优化效果。
- ⏱️ 综合效果：结合所有优化后，发布构建时间可从 20 多分钟降至 2-5 分钟，后续构建甚至更快，尤其在现代多核系统或 Apple Silicon 上。

---

### [React 相册 - 响应式 React 照片画廊组件](https://react-photo-album.com/)

**原文标题**: [React Photo Album - Responsive photo gallery component for React](https://react-photo-album.com/)

React Photo Album 是一个专为 React 设计的响应式照片画廊组件，支持行、列和瀑布流布局，并具备服务器端渲染、响应式图像和 TypeScript 支持等特性。

- 🖼️ 专为 React 18+ 构建，支持服务器端渲染，确保客户端水合前像素完美显示
- 📱 内置响应式图像支持，自动分辨率切换，优化不同视口下的加载体验
- 🧩 提供三种布局选项：行布局、列布局和瀑布流布局，满足多样化展示需求
- ⚙️ 高度可配置和可定制，支持自定义数据属性，并内置 TypeScript 类型定义
- 🚀 注重性能优化，能够高效处理大型相册，确保流畅的用户体验
- 📄 包含详细文档、示例和更新日志，方便开发者快速上手和集成

---

### [砌体布局 | React 相册](https://react-photo-album.com/examples/masonry)

**原文标题**: [Masonry Layout | React Photo Album](https://react-photo-album.com/examples/masonry)

该文章介绍了如何使用 MasonryPhotoAlbum 组件实现砌体式布局，并提供了代码示例、在线演示和相关资源链接。

- 🧱 使用 MasonryPhotoAlbum 组件实现砌体布局
- 📦 引入 react-photo-album 库及样式文件
- 🖼️ 通过 photos 数据源传递图片参数
- 🌐 提供在线演示和代码编辑沙盒环境
- 🔗 包含源代码仓库和布局文档导航链接

---

### [免费开源动画 ReactJS 组件 | animata](https://animata.design/)

**原文标题**: [Free & Open Source Animated ReactJS Components | animata](https://animata.design/)

这是一个名为 Animata 的开源 React 动画组件库，提供超过 194 个可直接复制使用的预制动画组件，旨在帮助开发者快速构建美观且交互生动的用户界面。

- 🚀 **加速开发**：提供超过 194 个预制动画 React 组件，可直接复制到任何项目中，无需安装或构建步骤，显著提升开发效率。
- 🎨 **设计精美**：所有组件均带有动画效果，旨在让界面“看起来更棒”，提升用户体验和视觉吸引力。
- 🆓 **免费开源**：基于 MIT 许可证，永久免费使用，并由不断壮大的开发者社区共同驱动和维护。
- ⭐ **备受信赖**：在 GitHub 上获得超过 2,300 颗星，被全球各地的开发团队信任和使用。
- 🧩 **种类丰富**：组件库涵盖背景、按钮、卡片、图表、加载器、进度条、骨架屏等 19 个类别，满足多种 UI 需求。
- 🌍 **广泛兼容**：支持 Next.js、Remix、Vite、Astro、Gatsby 等多种现代前端框架和构建工具。
- ♿ **开箱即用**：每个组件都预先内置了可访问性支持，包括键盘焦点、屏幕阅读器标签和减少动画的备用方案。
- 🔧 **源于实践**：所有组件都先在实际应用产品中得到验证，确保其可用性和实用性，然后才被纳入库中。

---

### [卡片布局 | 免费开源动画 ReactJS 组件](https://animata.design/docs/card/card-spread)

**原文标题**: [Card Spread | Free & Open Source Animated ReactJS Components](https://animata.design/docs/card/card-spread)

该文档介绍了一个名为 Animata 的 UI 组件库，包含多种交互式组件，并详细说明了“卡片展开”组件的安装和使用方法。

- 📚 **组件库概览** - 文档展示了一个丰富的 UI 组件库，涵盖背景、按钮、卡片、图表、文本、小部件等多种交互式组件。
- 🛠️ **快速开始指南** - 提供了从介绍、设置到本地运行、添加组件和项目结构的完整入门指引。
- 📁 **结构化分类** - 组件按功能清晰分类，如容器、特征卡片、浮动按钮、图表、图像、列表等，便于查找。
- 🃏 **卡片组件示例** - 重点演示了“卡片展开”组件，它能在悬停时旋转，点击后展开并平铺显示多个卡片内容。
- 💻 **代码集成步骤** - 详细说明了通过命令行创建文件、复制粘贴 React 代码来安装和使用“卡片展开”组件的具体流程。
- 🔄 **交互状态管理** - 组件使用 React 的`useState`钩子管理展开/收起状态，并通过 CSS 类实现平滑的旋转和平移动画。
- 📝 **示例内容展示** - 组件内置了便签、购物清单、提醒事项等示例卡片，展示了其在实际场景中的应用。

---

### [Slack 介绍界面 | 免费开源动画 ReactJS 组件](https://animata.design/docs/hero/slack-intro)

**原文标题**: [Slack's intro screen | Free & Open Source Animated ReactJS Components](https://animata.design/docs/hero/slack-intro)

该文档介绍了一个名为“Animata”的 UI 组件库，提供了丰富的动画组件和详细的集成指南，特别展示了受 Slack 启发的英雄区域组件实现。

- 📚 **组件库概览**：包含背景、按钮、卡片、图表、文本等 10 大类超过 100 个可复用动画组件
- ⚙️ **快速集成**：提供完整的本地运行、组件添加和文件夹结构配置指南
- 🎨 **Slack 风格示例**：详细演示了如何实现具有波浪文字效果的动态英雄区域组件
- 📦 **技术实现**：基于 React+TypeScript，支持自定义动画参数和响应式设计
- 🔧 **开发友好**：包含最佳实践、变更日志和贡献指南，支持社区协作完善

---

### [故障文本 | 免费开源动画 ReactJS 组件](https://animata.design/docs/text/glitch-text)

**原文标题**: [Glitch Text | Free & Open Source Animated ReactJS Components](https://animata.design/docs/text/glitch-text)

该内容是一个 UI 组件库的文档结构，包含入门指南、组件分类及具体实现示例，重点展示了 Glitch Text 组件的代码实现。

- 🚀 **入门指南** - 包含介绍、设置、更新日志、贡献指南和本地运行说明
- 📁 **项目结构** - 详细说明文件夹组织方式、组件添加流程和开发规范
- 🎨 **组件分类** - 涵盖背景、按钮、卡片、图表、文本等 8 大类共 134 个交互组件
- ⚙️ **组件示例** - 以 Glitch Text 为例展示完整实现代码，包含动画定义和 React 组件
- 🔧 **技术细节** - 提供 CSS 动画关键帧、TypeScript 组件代码和文件创建命令
- 👥 **社区协作** - 包含贡献指南、开发者致谢和 GitHub 编辑链接

---

### [面向 React 网页开发者的博览会](https://expo.dev/solutions/expo-for-react-web-devs?utm_source=react-status&utm_medium=email&utm_campaign=33087804-React%2520to%2520Native)

**原文标题**: [Expo for React web devs](https://expo.dev/solutions/expo-for-react-web-devs?utm_source=react-status&utm_medium=email&utm_campaign=33087804-React%2520to%2520Native)

Expo 是一个基于 React Native 的框架，让熟悉 React 的 Web 开发者能够使用现有技能构建 iOS 和 Android 原生应用，无需学习新工具或重写代码。

- 🚀 **React 开发者快速上手**：利用已有的 React 知识，通过 Expo 构建完全原生的移动应用，无需从头开始
- 📱 **真正的原生体验**：React Native 渲染为实际平台原生组件，而非 Web 视图，提供用户期望的性能和精致度
- 🔄 **跨平台开发**：单一代码库可同时面向 iOS、Android 和 Web 平台，共享导航和后端逻辑
- 🛠️ **简化移动开发**：包含 100 多个维护良好的库、顶级开发工具和服务，自动化移动开发中最困难的部分
- 📁 **文件路由系统**：采用类似 Next.js 的文件路由方式，对 Web 开发者友好
- ⚡ **无需 Xcode/Android Studio**：通过 EAS Build 和 Submit 处理复杂的原生构建和提交流程
- 🌐 **开源模式**：采用开源模型和快速迭代周期，延续 Web 开发的最佳实践
- 💬 **开发者社区认可**：受到 React 开发者社区的广泛好评和推荐

---

### [VisionCamera V5 有哪些新特性？](https://blog.margelo.com/whats-new-in-visioncamera-v5)

**原文标题**: [What's New in VisionCamera V5?](https://blog.margelo.com/whats-new-in-visioncamera-v5)

VisionCamera V5 是一次重大更新，基于全新的 Nitro 模块系统重构，引入了约束 API 以简化相机配置，支持内存照片、深度流、RAW 捕获和多相机会话等高级功能，并采用模块化设计提升灵活性和性能。

- 🚀 **全面重构至 Nitro 模块**：替换了手写的 JSI/C++ 层，实现完全类型安全、性能提升和更灵活的开发者工作流。
- 🎯 **全新的约束 API**：通过声明式约束让相机自动协商最佳配置，解决了跨平台（iOS/Android）特性兼容性问题。
- 📸 **内存照片对象**：`capturePhoto` 直接返回内存中的照片对象，无需读写临时文件，提升响应速度。
- 🔧 **模块化输出设计**：相机输出（如照片、视频）作为独立的 `HybridObject`，支持按需附加和更优雅的 API 调用。
- 📚 **全新文档与包结构**：提供详细的 API 文档，并将功能拆分为多个插件包（如条码扫描、GPU 加速重采样），避免单体依赖。
- ⚡ **性能优化**：Nitro 模块使原生调用速度提升约 15-60 倍，并支持懒加载属性，减少启动延迟和相机延迟。
- 🌐 **跨平台一致性**：条码扫描等功能现统一使用 MLKit，确保 iOS 和 Android 行为一致。
- 🛠️ **高级相机控制**：支持手动曝光/对焦/白平衡、完整的视频动态范围配置（如 HDR、Log）以及对焦自定义选项。
- 📐 **坐标系统转换**：提供预览、帧和相机坐标之间的转换支持，便于实现视觉反馈（如条码轮廓绘制）。
- 🔌 **可扩展原生集成**：允许通过 Nitro 模块开发自定义相机输出、设备等，无需修改核心库代码。
- 📦 **多相机会话支持**：通过命令式 API 实现同时使用多个相机设备进行流式传输或捕获。
- 🖼️ **GPU 加速重采样器**：新的 `react-native-vision-camera-resizer` 包提供 GPU 加速的帧重采样，性能提升约 5 倍。

---

### [VisionCamera - 最强大的 React Native 相机库 | VisionCamera](https://visioncamera.margelo.com/)

**原文标题**: [VisionCamera - The most powerful React Native Camera library | VisionCamera](https://visioncamera.margelo.com/)

VisionCamera 是 React Native 中最强大、高性能的相机库，支持照片和视频拍摄、二维码/条形码扫描、帧处理器等多种功能。

- 📸 支持照片和视频拍摄
- 🔍 支持二维码和条形码扫描
- ⚙️ 提供帧处理器功能
- 📚 包含 API 参考文档
- 🚀 提供快速入门指南

---

### [在公开发布前通过命令行在本地主机测试 OpenGraph | Simon Hartcher](https://simonhartcher.com/posts/2026-04-15-testing-opengraph-on-localhost-from-the-cli/)

**原文标题**: [Testing OpenGraph on localhost from the CLI before you go public | Simon Hartcher](https://simonhartcher.com/posts/2026-04-15-testing-opengraph-on-localhost-from-the-cli/)

作者开发了名为 og-check 的 CLI 工具，用于在本地测试 OpenGraph 标签，避免依赖公共 URL 和在线调试器的缓存问题，从而提升开发效率。

- 🛠️ 开发背景：作者在网站开发中常遇到 OpenGraph 标签调试的麻烦，传统工具需公共 URL，且存在缓存问题，导致迭代效率低下。
- 🖥️ 工具功能：og-check 可直接从本地 URL 获取并渲染 OpenGraph 预览，支持在终端内显示图片，大幅缩短反馈周期。
- 🖼️ 终端兼容：工具利用 Kitty 图形协议，兼容多种终端（如 Kitty、Ghostty、WezTerm 等），不支持的终端仍可显示文本信息。
- ⚙️ 工作原理：通过 Zig 的 HTTP 客户端获取页面，解析 meta 标签，并使用 zigdown 渲染 Markdown 或输出 JSON 格式。
- 📊 输出格式：提供四种输出选项，包括默认的 OpenGraph 预览、Twitter 卡片预览、标签表格和 JSON 格式，便于集成到 CI 流程。
- 📦 安装方式：可通过预构建二进制文件、从源码编译或使用 mise 工具安装，支持多平台和架构。

---

### [获取失败](https://developers.facebook.com/tools/debug/)

**原文标题**: [Failed to retrieve](https://developers.facebook.com/tools/debug/)

无法总结：获取内容失败，状态码 400。

---

### [GitHub - ankeetmaini/react-infinite-scroll-component: 一个超棒的 React 无限滚动组件。· GitHub](https://github.com/ankeetmaini/react-infinite-scroll-component)

**原文标题**: [GitHub - ankeetmaini/react-infinite-scroll-component: An awesome Infinite Scroll component in react. · GitHub](https://github.com/ankeetmaini/react-infinite-scroll-component)

这是一个用于 React 的无限滚动组件，体积小巧（4.15 kB），功能强大，支持下拉刷新和多种滚动模式，简化了无限滚动的实现。

- 🚀 **轻量高效** - 组件仅 4.15 kB，采用 IntersectionObserver 实现触发，性能更优，无运行时依赖。
- 🔄 **核心功能** - 支持无限滚动与下拉刷新，通过`next`函数加载数据，`hasMore`控制是否继续加载。
- 🎯 **灵活配置** - 可通过`height`、`scrollableTarget`或默认 body 滚动三种方式使用，支持自定义加载提示和结束信息。
- 📦 **易于集成** - 通过 npm 或 yarn 安装，提供 ES6 和 CommonJS 导入方式，基本使用只需几行代码。
- 🔧 **丰富属性** - 包括`dataLength`、`loader`、`endMessage`、`pullDownToRefresh`、`inverse`（顶部滚动）等可配置选项。
- 🌟 **社区活跃** - 拥有 3.1k 星标，由多位贡献者维护，遵循 MIT 许可证，文档详细并附带实时示例。

---

### [GitHub - rcaferati/react-native-awesome-button: React Native 按钮组件。Awesome Button 是一款以 60 帧每秒呈现 3D 效果、支持进度显示、适配社交分享、可扩展且适用于生产环境的组件，提供一系列精美的动画 UI 按钮。📱 · GitHub](https://github.com/rcaferati/react-native-awesome-button)

**原文标题**: [GitHub - rcaferati/react-native-awesome-button: React Native button component. Awesome Button is a 3D at 60fps, progress enabled, social ready, extendable, production ready component that renders an awesome animated set of UI buttons. 📱 · GitHub](https://github.com/rcaferati/react-native-awesome-button)

这是一个用于 React Native 的 3D 动画按钮组件库，支持进度显示、多种主题和社交风格，具有高度可定制性和生产就绪性。

- 📦 **安装与使用**：通过 npm 安装 `@rcaferati/react-native-awesome-button`，支持 React >= 18.2.0 和 React Native >= 0.76.0，提供 `AwesomeButton` 和 `ThemedButton` 两种组件。
- 🎨 **主题与样式**：内置多种主题（如 basic, rick, bruce）和变体（primary, secondary, social 等），支持自定义大小（icon, small, medium, large）和透明模式。
- 🔄 **进度按钮**：启用 `progress` 属性后，`onPress` 回调会接收一个 `next` 函数，用于在异步操作完成后触发进度动画完成。
- 🧩 **内容定制**：支持通过 `before`、`after` 和 `extra` 属性添加图标、文本或渐变背景等自定义内容，并支持任意 React Native 子元素。
- ⚙️ **丰富属性**：提供大量可配置属性，如尺寸、边框、动画效果、按压反馈、防抖等，并包含完整的 TypeScript 类型定义。
- 🛠️ **开发与演示**：项目包含完整的开发脚本和质量检查，附带一个 Expo 演示应用，展示了所有主题、变体及高级功能的使用示例。

---

### [GitHub - VictorHAS/mqtt-react-hooks：使用Hooks与MQTT代理进行发布/订阅通信的ReactJS库 · GitHub](https://github.com/VictorHAS/mqtt-react-hooks)

**原文标题**: [GitHub - VictorHAS/mqtt-react-hooks: ReactJS library for Pub/Sub communication with an MQTT broker using Hooks · GitHub](https://github.com/VictorHAS/mqtt-react-hooks)

这是一个用于在 React 应用中通过 Hooks 连接、发布和订阅 MQTT 消息的库，最新版本 3.0.0 进行了重大架构重写，提升了性能和稳定性。

- 🚀 **版本 3.0.0 重大更新**：引入全局可扩展的订阅管理器，消除重复事件监听，支持智能引用计数和预缓存消息。
- 📦 **安装简单**：通过`npm add mqtt-react-hooks mqtt`即可快速安装。
- 🔌 **连接配置**：使用`<Connector>`组件包裹应用，并指定`brokerUrl`来初始化 MQTT 客户端。
- 📡 **状态管理**：`useMqttState`钩子提供连接状态、客户端实例和消息等全局信息。
- 📨 **订阅消息**：`useSubscription`支持订阅单个或多个主题，并自动处理消息缓存和网络订阅。
- ✉️ **发布消息**：通过`useMqttState`或`useSubscription`获取客户端实例，直接调用`publish`方法发送消息。
- 🛠️ **开发提示**：针对 Vite/Webpack 等打包工具可能遇到的模块解析问题，建议参考 MQTT.js 的官方打包文档。
- 📄 **开源许可**：项目采用 MIT 许可证，欢迎贡献代码和改进建议。

---

### [又一个 React 灯箱 - 适用于 React 的现代灯箱组件](https://yet-another-react-lightbox.com/)

**原文标题**: [Yet Another React Lightbox - Modern lightbox component for React](https://yet-another-react-lightbox.com/)

Yet Another React Lightbox 是一个现代、高性能且易于定制的 React 灯箱组件，支持插件扩展和响应式图像。

- 🚀 **专为 React 构建**：兼容 React 19、18、17 及 16.8.0+ 版本。
- 🖱️ **多设备导航**：支持键盘、鼠标、触摸板和触摸屏操作。
- 📦 **智能预加载**：避免显示未完全下载的图像，并限制预加载数量以保持性能。
- 📱 **响应式支持**：开箱即用支持响应式图像与自动分辨率切换。
- 🎬 **视频与缩放**：可通过插件支持视频幻灯片和图像缩放功能。
- 🎨 **高度可定制**：可自定义任何 UI 元素或添加自定义幻灯片。
- 🧩 **模块化设计**：核心功能轻量，通过插件按需添加额外特性。
- 📘 **TypeScript 支持**：内置类型定义，提供完整的开发体验。
- 🌍 **国际化与布局**：兼容 RTL（从右到左）布局。
- 📚 **丰富资源**：提供详细文档、示例和更新日志，便于集成与学习。

---

### [发布 styled-components@6.4.0 · styled-components/styled-components · GitHub](https://github.com/styled-components/styled-components/releases/tag/styled-components%406.4.0)

**原文标题**: [Release styled-components@6.4.0 · styled-components/styled-components · GitHub](https://github.com/styled-components/styled-components/releases/tag/styled-components%406.4.0)

styled-components 发布了 6.4.0 版本，带来了多项重要更新，包括性能优化、React Server Components 支持、CSS 变量主题创建、IE11 支持移除、CSP nonce 支持增强，以及针对 React Native 的改进和内存泄漏修复。

- 🚀 **性能显著提升**：通过三层记忆化和热路径微优化，父组件重渲染速度提升 3.3 倍，首次挂载快 1.7-2.5 倍，大幅改善渲染效率。
- 🌐 **React Server Components 支持**：新增内联样式注入、去重功能及 `stylisPluginRSC` 插件，修复子索引选择器问题，优化服务器端渲染体验。
- 🎨 **CSS 变量主题创建**：引入 `createTheme()` 函数，支持跨 RSC 和客户端组件的 CSS 变量主题，提供稳定的类名哈希，避免水合不匹配。
- 🗑️ **移除 IE11 支持**：将构建目标改为 ES2015，删除相关依赖和遗留代码，简化代码库并提升现代浏览器兼容性。
- 🔒 **增强 CSP nonce 支持**：新增多种配置方式，包括通过 `StyleSheetManager` 的 `nonce` 属性、`ServerStyleSheet` 构造函数或 HTML meta 标签，提升安全性。
- 🛠️ **`createGlobalStyle` 重构**：改为共享样式表组，修复卸载实例时样式丢失、重挂载后样式分散及 SSR 组 ID 泄漏等问题，确保样式注入顺序稳定。
- 📱 **React Native 改进**：替换 postcss 为轻量级 CSS 声明解析器，修复 Expo/Metro 中的崩溃问题，解析速度提升 4-6 倍，并更新原生组件别名列表。
- 🐛 **修复内存泄漏**：解决长期运行应用中因自由格式字符串插值导致的内存泄漏问题，提升应用稳定性。
- 📦 **减小安装体积**：通过清理未使用的依赖，优化安装包大小，提升开发体验。

---

### [GitHub - pmndrs/react-three-fiber: 🇨🇭 Three.js 的 React 渲染器 · GitHub](https://github.com/pmndrs/react-three-fiber)

**原文标题**: [GitHub - pmndrs/react-three-fiber: 🇨🇭 A React renderer for Three.js · GitHub](https://github.com/pmndrs/react-three-fiber)

react-three-fiber 是一个用于 Three.js 的 React 渲染器，允许开发者以声明式、可复用的组件方式构建 3D 场景，并能够与 React 生态系统无缝集成。

- 🎨 **声明式 3D 渲染**：通过 JSX 组件构建 Three.js 场景，使代码更模块化和可维护。
- ⚡ **无性能开销**：组件在 React 外渲染，性能与原生 Three.js 相当，且在大规模场景中借助 React 调度能力更优。
- 🔄 **实时同步 Three.js 更新**：直接映射 Three.js API，新版本特性无需等待库更新即可使用。
- 📦 **丰富生态系统**：拥有众多周边库，如 @react-three/drei（工具集）、@react-three/xr（VR/AR 支持）等，覆盖物理、UI、后期处理等需求。
- 🌍 **跨平台支持**：支持 Web、React Native 等环境，示例中提供了 React Native 的配置指南。
- 🛠️ **易于上手**：提供完整文档、示例和 TypeScript 支持，适合熟悉 React 和 Three.js 基础的开发者。

---

### [发布 react-email@6.0.0 · resend/react-email · GitHub](https://github.com/resend/react-email/releases/tag/react-email%406.0.0)

**原文标题**: [Release react-email@6.0.0 · resend/react-email · GitHub](https://github.com/resend/react-email/releases/tag/react-email%406.0.0)

React-Email 发布了 6.0.0 版本，这是一个主要更新，将所有组件和渲染工具统一整合到单个 `react-email` 包中，简化了安装和导入体验，并计划弃用原有的多个独立包。

- 🚀 **主要变更**：所有组件和工具现直接从 `react-email` 包导出，取代了之前的 `@react-email/components` 等独立包。
- ⚠️ **破坏性变化**：不再推荐从旧包导入，仅 `@react-email/render` 和 `@react-email/editor` 暂时保留，但 `render` 仍可从 `react-email` 使用。
- 🔧 **迁移指南**：移除旧包、更新 `react-email` 至最新版，并将导入路径改为 `"react-email"`。
- 🛠️ **补丁更新**：在预览开发服务器中用 WHATWG URL API 替换了已弃用的 `url.parse()`。

---

### [摇滚与反应节 2026——奥斯陆洛克菲勒的科技、数据摇滚、美食与派对](https://reactnorway.com/?utm_medium=social&utm_source=ReactStatus)

**原文标题**: [Rock & React Festival 2026 – Tech, Datarock, Food & Party at Rockefeller, Oslo](https://reactnorway.com/?utm_medium=social&utm_source=ReactStatus)

React Norway 2026 是一场将编程与摇滚音乐结合的独特 React 前端技术大会，将于 2026 年 6 月 5 日在奥斯陆传奇音乐场馆 Rockefeller 举行。大会汇集了行业领袖与专家，通过一系列前沿技术演讲、实践研讨会以及晚间音乐会，为开发者提供学习、交流和娱乐的一站式体验。

- 🎸 **独特形式**：在奥斯陆著名摇滚音乐场地 Rockefeller 举办，融合技术演讲与现场音乐，打造“编程遇见和弦”的节日氛围。
- 📅 **核心日程**：2026 年 6 月 5 日举行，包含从上午注册到晚间摇滚音乐会的全天活动。
- 🎤 **明星讲师阵容**：邀请多位来自 Netlify、Auth0、Vercel、Hugging Face、Amazon 等公司的专家，涵盖 React 安全、AI 集成、性能优化、可观测性等前沿话题。
- 🕒 **重点演讲议题**：包括 React 应用安全实战、TanStack Start 与 AI 结合、低延迟配对编程、自动化 UX 研究、代码清理、前端可观测性、异步 React 状态管理、浏览器内多模态 AI 代理、编译器驱动框架 Isograph 以及 AI 流式渲染 React 组件等。
- 🎟️ **多元化票务**：提供包含全天会议和晚间音乐会的“摇滚与 React”套票、仅音乐会门票以及免费的线上会议观看选项。
- 🏆 **趣味竞赛**：举办音乐独奏比赛，优胜者可赢得包含酒店住宿的会议门票。
- 🏨 **合作伙伴福利**：与会者可享受附近 Comfort Hotel Xpress Youngstorget 的住宿折扣。
- 📍 **场地与历史**：Rockefeller 场馆可容纳约 1300 人，拥有专业级设施。会议前身为始于 2019 年的 React Day Norway，历年规模与形式不断演进。

---

### [STRICH | 网页应用条码扫描](https://strich.io/?ref=react-status)

**原文标题**: [STRICH | Barcode Scanning for Web Apps](https://strich.io/?ref=react-status)

STRICH 是一款用于网页应用的 JavaScript 库，支持在浏览器中实时扫描一维和二维条码，无需原生应用或后端支持。它提供简单透明的定价、开发者友好的集成方式，并包含企业级功能。

- 📦 **JavaScript/WASM 库**：通过 npm 安装，可直接在网页应用中实现条码扫描，无需依赖原生应用或后端。
- 💰 **透明定价**：提供按月订阅，无设备数量限制，含免费 30 天试用，可随时取消。
- 🛠️ **开发者友好**：零依赖，支持所有主流前端框架，提供详细文档和 TypeScript 绑定。
- 🌐 **网页应用优势**：避免应用商店审核，易于分发和更新，降低开发成本，支持 PWA 离线操作。
- 📷 **高性能扫描**：支持多种一维和二维条码，内置扫描 UI 和弹窗扫描器，可读取模糊、损坏或反色条码。
- 🏢 **企业级功能**：提供白标定制、完全离线部署、固定年费定价及优先支持选项。
- ⭐ **客户好评**：多家企业（如图书馆、零售、医疗科技）反馈其稳定性、易集成性和出色支持。
- ❓ **常见问题**：涵盖扫描限制、框架兼容性、条码支持及与免费方案的对比，提供详细解答和演示应用。

---

### [依赖冷却期让你成为搭便车者](https://calpaterson.com/deps.html)

**原文标题**: [Dependency cooldowns turn you into a free-rider](https://calpaterson.com/deps.html)

依赖冷却期看似能防范供应链攻击，实则让用户成为搭便车者，将风险转嫁给未设置冷却期的用户，且无法根本解决问题。相比之下，上传队列通过在中央服务器统一延迟新包分发，能更公平、有效地提升安全性，尤其适用于 AI 领域。

- 🕒 依赖冷却期要求项目在采用新版本前等待数天，希望他人先发现恶意代码，但这本质上是搭便车行为。
- 🔄 该做法将风险转移给未设置冷却期的用户，让他们充当无偿测试者，且难以在整个生态系统中持续推行。
- ⚙️ 实施依赖冷却期需多个包管理器和项目单独配置，过程复杂且容易因意外操作而失效。
- 🚀 上传队列作为中央解决方案，在包发布后、分发前引入等待期，统一运行安全扫描并允许自愿测试。
- 🛡️ 上传队列消除了搭便车问题，无需各项目单独配置，即使开发者意外安装单个包也能获得保护。
- 📅 延迟分发能减少发布凭证的滥用风险，并为用户和维护者提供新版本发布的预先通知。
- 🤖 在 AI 领域，上传队列尤为重要，可防止恶意 Markdown 文件攻击，并通过双重审核机制增强安全性。
- 💰 上传队列的实施资金可通过企业赞助或付费加急审核服务解决，已有成功案例如 Debian 项目。
- ⚖️ 依赖冷却期虽对个体有益，但作为社区实践会加剧集体风险，而上传队列能更系统化地提升整个生态系统的安全。

---

### [针对“返回按钮劫持”的新垃圾政策发布  |  Google 搜索中心博客  |  Google for Developers](https://developers.google.com/search/blog/2026/04/back-button-hijacking)

**原文标题**: [Introducing a new spam policy for "back button hijacking"  |  Google Search Central Blog  |  Google for Developers](https://developers.google.com/search/blog/2026/04/back-button-hijacking)

谷歌搜索中心宣布将“返回按钮劫持”明确列为恶意行为，并纳入垃圾信息政策，自 2026 年 6 月 15 日起执行。此举旨在打击干扰用户浏览器导航、破坏返回按钮正常功能的欺骗性做法，以提升用户体验和信任度。

- 🚫 **政策更新**：明确将“返回按钮劫持”列为违反垃圾信息政策中“恶意行为”的条目，可能导致手动处罚或搜索排名降级。
- 🔍 **问题定义**：指网站通过脚本或技术手段阻止用户点击返回按钮时立即回到上一页面，转而跳转至无关页面、广告或推荐内容。
- 😠 **影响与原因**：此行为破坏浏览器功能，违背用户预期，导致体验受挫和信任下降；谷歌基于用户至上原则，强调其一直反对在浏览历史中插入欺骗性页面。
- ⏳ **执行时间**：政策提前两个月公布（2026 年 4 月 13 日），将于 2026 年 6 月 15 日正式生效，以便网站所有者进行调整。
- 🛠️ **整改建议**：网站所有者需审查并移除任何导致返回按钮劫持的代码、库或广告配置，确保导航体验真实、顺畅。
- 📝 **后续处理**：若网站因手动操作受影响，修复后可通过搜索控制台提交重新审核请求；也可通过社交媒体或帮助社区反馈问题。

---

### [Node.js — Node.js 24.15.0（长期支持版）](https://nodejs.org/en/blog/release/v24.15.0)

**原文标题**: [Node.js — Node.js 24.15.0 (LTS)](https://nodejs.org/en/blog/release/v24.15.0)

Node.js 24.15.0（LTS）版本“Krypton”发布，包含多项新功能、性能优化、错误修复及依赖项更新，标志着 SQLite 模块进入发布候选阶段，并提升了多个核心模块的稳定性与功能。

- 🚀 **CLI 新增选项**：添加了`--max-heap-size`和`--require-module/--no-require-module`命令行选项，增强运行时配置灵活性。
- 🔐 **加密功能增强**：`crypto`模块支持原始密钥格式，并更新了根证书，提升了安全性与兼容性。
- 📁 **文件系统改进**：`fs.stat`及其 Promise 版本新增`throwIfNoEntry`选项，优化文件状态检查的错误处理。
- 🌐 **网络模块升级**：`http2`模块添加`http1Options`以配置 HTTP/1 回退，`net`模块为`Socket`新增`setTOS`和`getTOS`方法。
- 🗃️ **SQLite 模块进展**：SQLite 模块标记为发布候选（RC），并新增`limits`属性到`DatabaseSync`，提升数据库操作能力。
- 🔧 **模块系统稳定化**：`require(esm)`和模块编译缓存标记为稳定功能，增强了 ES 模块与 CommonJS 的互操作性。
- 🛠️ **诊断与测试工具**：新增 C++ 层面对诊断通道的支持，`test_runner`暴露工作线程 ID 并优化中断处理，提升开发调试体验。
- ⚡ **性能与内存优化**：多项底层改进，包括 Buffer 操作、事件监听器处理及启动性能优化，提升整体运行时效率。
- 🔄 **依赖项更新**：升级了 npm、V8、OpenSSL 等关键依赖，并更新了 ada、simdjson 等库，确保安全性与现代标准兼容。
- 🐛 **错误修复与安全补丁**：修复了 HTTP、流处理、压缩模块中的多个问题，包括内存泄漏和竞争条件，增强了稳定性。

---

### [TanStack Router、Start 和 Query 中 Solid 2.0 Beta 支持 | TanStack 博客](https://tanstack.com/blog/tanstack-start-solid-v2)

**原文标题**: [Solid 2.0 Beta Support in TanStack Router, Start, and Query | TanStack Blog](https://tanstack.com/blog/tanstack-start-solid-v2)

TanStack 宣布其 Router、Start 和 Query 库现已支持 Solid 2.0 测试版，使开发者能够在实际应用中立即体验 Solid 2.0 的新特性，包括异步渲染、派生状态和 SSR 的重大改进。

- 🚀 **立即开始体验**：可通过官方 Solid 示例创建新项目，或升级现有 TanStack Router 或 Start 应用至指定测试版依赖。
- 📦 **依赖更新指南**：提供了 npm、pnpm、yarn 和 bun 的详细命令，用于更新 Solid 2.0 相关核心库及配套工具。
- ⚙️ **主要变化来源**：API 基本保持稳定，主要突破性变化源于 Solid 2.0 本身，建议开发者参考官方迁移指南。
- 💡 **版本意义**：Solid 2.0 引入了细粒度非空异步、可变派生、派生信号等新特性，尤其有利于大型应用的路由和服务器渲染。
- 🔍 **早期反馈征集**：支持仍处于早期阶段，鼓励开发者在 Discord 社区提供使用反馈，以帮助完善集成。
- 📚 **资源链接**：文中提供了 Solid 2.0 测试版讨论和路线图讨论的链接，供深入探索。

---

