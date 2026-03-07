### [获取失败](https://www.patreon.com/posts/seven-years-to-typescript-152144830)

**原文标题**: [Failed to retrieve](https://www.patreon.com/posts/seven-years-to-typescript-152144830)

无法总结：获取内容失败，状态码 403。

---

### [CLI 安装程序 – AuthKit – WorkOS 文档](https://workos.com/docs/authkit/cli-installer?utm_source=cpreact&utm_medium=newsletter&utm_campaign=q12026)

**原文标题**: [CLI Installer – AuthKit – WorkOS Docs](https://workos.com/docs/authkit/cli-installer?utm_source=cpreact&utm_medium=newsletter&utm_campaign=q12026)

WorkOS CLI 安装器能通过单一命令快速为项目集成 AuthKit，自动完成框架检测、SDK 安装、路由配置和环境设置，使应用在约两分钟内实现完整的身份验证功能。

- 🛠️ **自动框架检测** – CLI 通过 AI 识别项目依赖和文件结构，确定框架及版本（如 Next.js、React、SvelteKit 等），并安装对应的 SDK。
- 🔐 **账户认证与配置** – 自动打开浏览器进行 WorkOS 安全登录，并配置仪表板的重定向 URI、CORS 来源和主页 URL。
- 📁 **项目分析与文件生成** – 分析项目结构，创建 OAuth 回调路由、身份验证中间件/代理和提供者包装器，并写入环境变量到 `.env.local`。
- ✅ **集成验证** – 运行构建以验证编译无误，确保集成成功；支持 `--debug` 标志进行详细故障排查。
- ⚙️ **灵活选项与故障处理** – 提供 CLI 选项如 `--integration` 手动指定框架，`--no-validate` 跳过验证；安装后可使用 `git diff` 查看更改，或运行 `workos doctor` 诊断问题。

---

### [React 正通过 Activity 组件改变流媒体应用的格局 | Mux](https://www.mux.com/blog/react-is-changing-the-game-for-streaming-apps-with-the-activity-component)

**原文标题**: [React is changing the game for streaming apps with the Activity component | Mux](https://www.mux.com/blog/react-is-changing-the-game-for-streaming-apps-with-the-activity-component)

视频流应用常包含复杂多视图界面，传统导航方式易导致状态丢失。React 19.2 推出的`<Activity>`组件通过保持组件挂载而非卸载，结合`useLayoutEffect`控制播放行为，实现了无缝状态保留体验。

- 🎬 传统条件渲染方案在切换标签页时会卸载播放器组件，导致播放进度丢失
- 🔄 `<Activity>`组件通过`mode`属性控制显隐，隐藏时组件保持挂载但不可见
- ⚠️ 单纯使用`<Activity>`可能造成视频在后台继续播放，影响用户体验
- ⏸️ 最佳方案需结合`useLayoutEffect`钩子，在组件隐藏时自动暂停播放
- 🔗 必须通过`forwardRef`将播放器引用传递给父组件才能实现精确控制
- 📊 该模式同样适用于表单、数据表格、绘图应用等需要保持状态的场景
- 🚀 实施需升级至 React 19.2，并遵循组件包装、引用传递和效果钩子的完整流程

---

### [<活动> – React](https://react.dev/reference/react/Activity)

**原文标题**: [<Activity> – React](https://react.dev/reference/react/Activity)

Activity 是 React 的一个组件，用于隐藏和恢复其子组件的 UI 和内部状态，通过 `display: none` 隐藏内容并清理副作用，同时保留状态以便后续恢复，适用于优化交互和预渲染场景。

- 🎭 **隐藏与恢复状态**：使用 `mode` 属性（`'visible'` 或 `'hidden'`）控制子组件的可见性，隐藏时保留状态，恢复时无需重新初始化。
- 🔄 **替代条件渲染**：相比条件渲染（如 `&&`），Activity 避免卸载组件，从而保持其内部状态（如表单输入、展开状态）。
- 🌐 **DOM 状态保留**：隐藏时子组件的 DOM 元素不被销毁，适合需要保留临时状态（如文本输入）的 UI 部分。
- ⚡ **预渲染优化**：即使初始隐藏，子组件也会在低优先级下渲染，可提前加载代码或数据，加快后续显示速度。
- 🚀 **提升水合性能**：Activity 边界将组件树分割为独立单元，支持 React 的选择性水合，使页面部分更早可交互。
- ⚠️ **处理副作用**：隐藏时组件的 Effects 被清理，但某些 DOM 元素（如 `<video>`）可能需手动清理副作用，建议使用 `useLayoutEffect` 进行管理。
- 🔍 **调试建议**：使用 `<StrictMode>` 检测未正确清理的 Effects，确保组件在隐藏时行为稳健。

---

### [ViteLand 二月 2026 回顾：新动态一览 | VoidZero](https://voidzero.dev/posts/whats-new-feb-2026)

**原文标题**: [What’s New in ViteLand: February 2026 Recap | VoidZero](https://voidzero.dev/posts/whats-new-feb-2026)

ViteLand 2026 年 2 月更新回顾了 Vite+ 生态系统的多项进展，包括 Oxfmt 进入 Beta 阶段、各核心工具的性能提升与新功能，以及社区动态和即将举行的活动。

- 🚀 Oxfmt 进入 Beta 阶段，实现与 Prettier 的完全兼容，运行速度提升高达 36 倍，并已获多家知名团队采用。
- 🔧 Vite 8 Beta 推出了实验性开发者工具，新增插件注册表，便于开发者发现和使用 npm 上的 Vite 插件。
- ⚡ Vitest 4.1 Beta 引入了 `aroundEach` 和 `aroundAll` 钩子，并计划在 UI 中添加慢速测试过滤器以优化测试套件。
- 📦 Rolldown 通过优化内部文件路径处理，性能提升高达 9.6%，并新增了深度文档解释死代码消除机制。
- 🛠️ Oxc 的语义分析因标识符哈希预计算而提速约 4-6%，Oxlint 增加了类型感知 linting 配置选项和支持更多规则。
- 📅 即将举办的活动包括 Evan You 在 Vue.js Amsterdam 的演讲，以及 Alexander Lichter 在 Laravel Live Japan 2026 和 enterJS 2026 的分享。
- 🌐 社区动态丰富，包括 Cloudflare 发布基于 Vite 8 的 `vinext`、Astro 开发基于 Oxc 的 Rust 编译器，以及多个项目迁移至 Vitest 和 Oxlint。

---

### [模态可访问性 · adobe/react-spectrum · 讨论 #9696 · GitHub](https://github.com/adobe/react-spectrum/discussions/9696#discussioncomment-15942257)

**原文标题**: [Modal a11y · adobe/react-spectrum · Discussion #9696 · GitHub](https://github.com/adobe/react-spectrum/discussions/9696#discussioncomment-15942257)

本文讨论了 React Aria 库中 Modal 组件为何使用`<section role="dialog">`而非原生`<dialog>`元素，以及为何未添加`aria-modal="true"`属性的原因，主要基于浏览器兼容性、第三方库集成、动画控制和焦点管理等实际开发需求。

- 🎭 **顶层渲染问题**：原生`<dialog>`的顶层特性可能导致与第三方组件（如聊天插件、引导教程）的叠加顺序冲突，而 JS 库可更灵活控制层级。
- 🚫 **无障碍属性选择**：未使用`aria-modal="true"`是为了通过`inert`属性更精确地控制外部元素的隐藏，避免影响如 Toast 等需同时可见的组件。
- 🎬 **动画支持限制**：原生`<dialog>`的动画过渡（如背景遮罩）支持有限，复杂动画需依赖 JS 库实现。
- 📜 **页面滚动控制**：原生`<dialog>`无法自动阻止背景页面滚动，需额外 JS 处理，而库通常内置此功能。
- 🎯 **焦点管理差异**：原生`<dialog>`允许焦点跳出到浏览器界面，可能不符合无障碍实践，JS 库可严格限制焦点在对话框内。
- ⚖️ **适用场景建议**：简单应用可使用原生`<dialog>`，但复杂场景（需兼容第三方组件、定制动画等）仍推荐 JS 库方案。

---

### [发布 0.85.0-rc.0 · facebook/react-native · GitHub](https://github.com/facebook/react-native/releases/tag/v0.85.0-rc.0)

**原文标题**: [Release 0.85.0-rc.0 · facebook/react-native · GitHub](https://github.com/facebook/react-native/releases/tag/v0.85.0-rc.0)

React Native 发布了版本 0.85.0-rc.0，这是一个预发布版本，包含了一系列重要的更新、修复和改动，主要聚焦于移除废弃的 API、增强动画后端、改进开发工具、优化性能与稳定性，并修复了多个平台上的已知问题。

- 🚀 **移除废弃 API**：移除了已弃用的类型别名、`StyleSheet.absoluteFill` API，并停止支持旧版本的 Node.js。
- 🛠️ **动画后端增强**：引入了新的动画后端功能，包括文档、示例、时间戳更新和线程安全改进。
- 🔧 **开发工具改进**：支持多个 CDP 连接、修复网络事件发送、优化 DevTools 界面，并改进了与 Metro 的集成。
- 📱 **平台特定更新**：Android 上增加了自定义字体查询、滚动视图自动聚焦控制；iOS 上改进了文本输入选择数据处理、边框半径裁剪和性能优化。
- 🐛 **问题修复**：修复了内存泄漏、崩溃问题、图像显示异常、网络连接错误及可访问性相关的问题。
- 🔄 **代码库现代化**：将部分 Java 类迁移到 Kotlin，更新了 Flow 类型，并重构了部分核心逻辑以提升可维护性。
- ⚠️ **废弃通知**：标记了`AccessibilityInfo.setAccessibilityFocus`等 API 为废弃，建议开发者迁移到新 API。
- 📦 **构建与依赖更新**：升级了 Gradle 版本，调整了 Hermes 构建标志，并优化了预构建框架的生成。

---

### [将灯塔引入应用：为 React Native 构建性能指标 - Indeed 工程博客](https://engineering.indeedblog.com/blog/2026/03/bringing-lighthouse-to-the-app-building-performance-metrics-for-react-native/)

**原文标题**: [Bringing Lighthouse to the App: Building Performance Metrics for React Native - Indeed Engineering Blog](https://engineering.indeedblog.com/blog/2026/03/bringing-lighthouse-to-the-app-building-performance-metrics-for-react-native/)

Indeed 开源了一个 React Native 性能测量库，将 Lighthouse 的核心网页指标理念引入移动应用，帮助团队在向“应用优先”转型时监控和提升应用性能。

- 🎯 **挑战**：从网页优先转向应用优先时，缺乏标准化方法来衡量 React Native 页面的性能表现。
- 📊 **解决方案**：借鉴核心网页指标，定义了三个关键性能指标：首帧时间、可交互时间和首次输入延迟。
- ⚡ **指标阈值**：针对原生应用特性设定了比网页更严格的标准，例如可交互时间低于 500ms 为良好。
- 🛠️ **集成简易**：通过一个 React Hook 实现，仅需三步即可集成到组件中，几乎无性能开销。
- 🏗️ **技术实现**：利用 InteractionManager 测量首帧时间，组件自报告可交互状态，通过 PanResponder 捕获输入延迟。
- 📈 **实际效果**：在 ViewJob 页面应用后，获得了平均 81 分的性能评分，并能输出完整的性能分析数据。
- 🔮 **未来计划**：将系统扩展到更多页面，并基于数据实现自动化警报、性能预算和 A/B 测试等。
- 🌐 **开源贡献**：项目已开源，鼓励类似转型中的公司使用和参与贡献。

---

### [打造你自己的视频分享应用——使用 Next.js 和 Mux 的 Loom 克隆版 JavaScript 教程 - YouTube](https://www.youtube.com/watch?v=IBTx5aGj-6U)

**原文标题**: [Build Your Own Video Sharing App – Loom Clone with Next.js and Mux JavaScript Tutorial - YouTube](https://www.youtube.com/watch?v=IBTx5aGj-6U)

该内容为 YouTube 网站底部的通用导航链接列表，并非一篇文章或具有实质内容的文本。

- 🏠 **核心功能与服务** - 包括版权声明、联系方式、创作者与广告商入口
- ⚖️ **政策与安全** - 涵盖使用条款、隐私政策及平台运作规则说明
- 🔄 **平台动态** - 提供新功能测试入口和开发者资源
- ©️ **版权标识** - 明确标注谷歌公司的版权归属与年份信息

---

### [我如何利用 Cursor 迁移框架](https://kentcdodds.com/blog/how-i-used-cursor-to-migrate-frameworks)

**原文标题**: [How I used Cursor to Migrate Frameworks](https://kentcdodds.com/blog/how-i-used-cursor-to-migrate-frameworks)

作者使用 Cursor AI 工具成功升级了个人网站 kentcdodds.com 的依赖包，整个过程分为易、中、难三个级别逐步进行，并特别处理了 Remix 到 React Router v7 的复杂迁移，最终所有升级均顺利完成。

- 🛠️ 作者利用 Cursor AI 将项目过时依赖包按升级难度分为易、中、难三组，并制定了升级策略。
- 📦 首先顺利完成了 19 个“简单”级别的依赖包更新，未遇到问题。
- 🔄 随后处理 42 个“中等”级别更新，虽有小问题但整体平稳，得益于项目良好的测试和文档。
- ⚙️ 针对 14 个“困难”级别更新，作者逐个处理，先后完成了 Vite/Vitest、Zod 和 XState 的重大版本升级。
- 🚀 最复杂的 Remix v2 到 React Router v7 迁移通过 Cursor 的长时运行代理功能完成，涉及路由系统重构和补丁文件处理。
- 🤖 升级过程中，Cursor 的 BugBot 和 CodeRabbit 自动检测并修复问题，作者通过多次迭代最终合并成功。
- ⚡ 作者表示目前日常需同时管理多个项目和 AI 代理，工作强度高且充满挑战，但乐在其中。
- ⚖️ 文末提到在高效工作的同时，也面临着难以平衡工作与休息的普遍困境。

---

### [Cloudflare 刚刚草率分叉了 Next.js… - YouTube](https://www.youtube.com/watch?v=abbeIUOCzmw)

**原文标题**: [Cloudflare just slop forked Next.js… - YouTube](https://www.youtube.com/watch?v=abbeIUOCzmw)

该文本为 YouTube 网站底部的导航链接列表，展示了其各项服务与政策入口。

- 🏠 概要
- 📰 プレスルーム
- ©️ 著作権
- 📞 お問い合わせ
- 🎨 クリエイター向け
- 📢 広告掲載
- 💻 開発者向け - 📜 利用規約
- 🔒 プライバシー・ポリシーとセキュリティ
- ⚙️ YouTube の仕組み
- 🧪 新機能を試してみる
- ™️ © 2026 Google LLC

---

### [我们如何在一周内用 AI 重建 Next.js](https://blog.cloudflare.com/vinext/)

**原文标题**: [How we rebuilt Next.js with AI in one week](https://blog.cloudflare.com/vinext/)

本文介绍了 Cloudflare 团队如何在一周内利用 AI 重建了 Next.js 框架，创建了名为 vinext 的替代方案。vinext 基于 Vite 构建，可部署到 Cloudflare Workers，在早期测试中构建速度提升至 4 倍，客户端包体积减少 57%，开发成本约 1100 美元。

- 🚀 **vinext 诞生**：一名工程师借助 AI 在一周内基于 Vite 重建 Next.js，实现无缝替换，构建速度提升 4 倍，包体积减少 57%
- 🔧 **解决部署痛点**：Next.js 在无服务器生态部署困难，vinext 直接实现 Next.js API，支持 Vite 环境 API，跨平台运行
- ⚡ **性能优势**：生产构建时间最快达 1.67 秒（4.4 倍加速），客户端包体积最小 72.9KB（减少 57%）
- ☁️ **云部署集成**：专为 Cloudflare Workers 优化，单命令完成构建部署，支持 KV 缓存和 ISR 功能
- 🧪 **实验性项目**：覆盖 Next.js 16 的 94% API，含 1700+ 测试，已有生产案例但需谨慎使用
- 🤖 **AI 开发突破**：利用 Claude 等 AI 工具编写大部分代码，通过严格测试流程保障质量，成本约 1100 美元
- 📊 **流量感知预渲染**：实验性功能，根据实际访问量预渲染页面，避免无用构建，优化大型站点
- 🔮 **行业影响**：AI 可能改变软件抽象层设计，减少人为复杂性，直接基于规范实现功能
- 🌐 **生态开放**：95% 代码与 Cloudflare 无关，欢迎其他平台贡献，已验证可在 Vercel 等平台运行
- 🛠️ **迁移支持**：提供 AI 迁移技能和手动迁移指南，支持现有 Next.js 项目平滑过渡

---

### [主屏幕小部件与 Expo 实时活动](https://expo.dev/blog/home-screen-widgets-and-live-activities-in-expo)

**原文标题**: [Home screen widgets and Live Activities in Expo](https://expo.dev/blog/home-screen-widgets-and-live-activities-in-expo)

Expo 推出全新的 expo-widgets 库，允许开发者使用 Expo UI 组件构建 iOS 主屏幕小组件和实时活动，无需原生设置即可实现。

- 🚀 **零配置开发**：expo-widgets 库通过 Continuous Native Generation 自动处理原生配置，省去 Xcode 目标创建、App Groups 设置等繁琐步骤
- 📱 **React 组件化**：小组件可直接定义为 React 组件，利用@expo/ui 库将 React 组件映射为 SwiftUI 原生视图，系统按需渲染
- ⏱️ **实时活动支持**：支持锁屏横幅和灵动岛多形态显示，可通过 APNs 推送更新或远程启动活动
- ☕ **交互功能示例**：提供咖啡计数器示例代码，展示如何创建带按钮交互的小组件，支持状态更新无需启动应用
- 🎯 **场景区分**：小组件适合日历、天气等“随时查看”场景，实时活动适用于外卖配送、赛事比分等“进行中”事件
- 🔮 **未来规划**：将添加时间线回读、刷新策略和图片支持等功能，目前处于 alpha 测试阶段

---

### [微基](https://tinybase.org/)

**原文标题**: [TinyBase](https://tinybase.org/)

TinyBase 是一个轻量级、响应式的本地优先数据存储与同步引擎，最新版本 v8.0 支持对象、数组和中间件，适用于构建快速、离线的 Web 应用。

- 🚀 **响应式数据监听**：监听数据变化，仅更新变动的部分，提升应用性能，支持 React 绑定和预构建组件，内置撤销栈和开发者工具。
- 🗄️ **类数据库功能**：支持键值对和表格数据，可定义类型化模式，提供索引、指标聚合、表关联和强大的查询引擎（无需 SQL）。
- 🔄 **数据同步与持久化**：原生 CRDT 支持，实现跨设备数据同步与合并，可持久化到文件、浏览器存储、IndexedDB、SQLite/PostgreSQL 等。
- 📱 **本地优先设计**：专为离线应用优化，数据存储在用户设备，体积小巧（6.2kB–13.2kB），无依赖，100% 测试覆盖，开源且文档齐全。
- 🔧 **丰富的工具集成**：与 React、IndexedDB、PostgreSQL、SQLite、YJS、Automerge 等工具兼容，提供架构指南帮助选择合适方案。
- ⚛️ **React 集成与组件**：提供 React Hooks 和预构建组件（如表格展示、数据检查器），简化 UI 开发，支持实时数据绑定。
- 🛡️ **数据模式与验证**：支持值表和表模式，确保数据类型和默认值，可集成 Zod、TypeBox 等库进行运行时验证。
- 📊 **高级查询与聚合**：通过 TinyQL 进行跨表查询、过滤和聚合，支持参数化查询和结果排序分页，结果保持响应式。
- 🔍 **索引与关系管理**：提供索引快速查找和数据关联功能，支持监听，便于构建复杂数据模型（如链表）。
- ⏪ **检查点与撤销栈**：内置检查点功能，支持前进/后退操作，实现撤销和重做能力。
- 📦 **轻量与高效**：核心模块仅 6.2kB，完整包 13.2kB，UI 模块额外 5.5kB–4.0kB，无依赖，运行速度快。
- ✅ **全面测试与文档**：100% 测试覆盖率，包含详细指南、演示和 API 示例，易于上手和集成。

---

### [架构选项 | TinyBase](https://tinybase.org/guides/the-basics/architectural-options/)

**原文标题**: [Architectural Options | TinyBase](https://tinybase.org/guides/the-basics/architectural-options/)

TinyBase 提供了多种架构选项，用于在应用中集成数据存储、持久化和同步功能，从简单的独立内存存储到复杂的客户端 - 服务器同步方案。

- 🚀 **独立内存存储**：数据仅在应用运行时存在，适合原型开发，但关闭后数据丢失。
- ☁️ **只读云端数据**：启动时从服务器加载数据到内存，适用于静态参考应用，但数据不可交互保存。
- 💾 **浏览器存储**：利用本地存储（如 LocalStorage、OPFS）持久化数据，支持会话间保留，但受限于单设备且可能被清除。
- 🗄️ **客户端数据库存储**：通过 WASM 将数据持久化到 SQLite 等客户端数据库，提供结构化存储，但会增加资源负载。
- 🔄 **仅客户端同步**：使用 MergeableStore 和 Synchronizer 在客户端间同步数据，支持多设备共享，但缺乏中央数据源。
- 🌐 **客户端 - 服务器同步**：服务器作为数据源协调客户端同步，结合持久化存储（如 SQLite），增强数据可靠性和认证控制。
- 🔌 **第三方同步**：集成外部同步平台（如 ElectricSQL、Yjs），便于与现有服务对接，但增加复杂性和潜在成本。
- 🧩 **混合架构**：可根据需求组合多种策略，例如同时使用内存存储、本地持久化和云端同步，灵活适应复杂应用场景。

---

### [调查与表单管理软件 - SurveyJS](https://surveyjs.io/?utm_source=react_status&utm_medium=email&utm_campaign=q1)

**原文标题**: [Survey and Form Management Software - SurveyJS](https://surveyjs.io/?utm_source=react_status&utm_medium=email&utm_campaign=q1)

SurveyJS 是一个开源的前端表单和问卷管理库，提供完整的表单构建、数据收集、分析和 PDF 导出功能，支持自托管，确保数据完全自主控制。

- 📚 **表单库** – 免费 MIT 许可的 UI 组件，可解析 JSON 文件并动态渲染交互式表单，用于收集用户响应并发送至自有数据库。
- 🛠️ **表单设计器** – 支持拖拽操作的白色标签表单构建工具，自动生成 JSON 结构，可自定义样式，用于可视化创建和编辑表单。
- 📊 **仪表盘** – 通过 JSON 模式解析数据，生成交互式图表和表格，用于实时可视化问卷结果。
- 📄 **PDF 生成器** – 将表单 JSON 转换为 PDF，支持预填响应数据，可导出为可编辑或预填的 PDF 文件。
- ♿ **无障碍支持** – 完全符合 WCAG、Section 508 和 ARIA 标准，支持键盘导航和屏幕阅读器。
- ∞ **无使用限制** – 无管理员、受访者、表单数量或提交次数限制，所有数据存储于自有数据库。
- 🧩 **自定义输入字段** – 支持创建自定义问题类型，可集成 Angular、React 或 Vue 3 组件。
- 📶 **离线数据收集** – 支持完全离线工作，数据本地存储，恢复网络后自动同步。
- 💳 **一次性购买许可** – 一次性购买开发者许可，永久使用，包含 12 个月免费维护。
- ✅ **自定义数据验证** – 支持客户端和服务器端自定义验证规则，通过 JavaScript 函数实现。
- 🔓 **开源透明** – 所有库开源，支持 React、Angular、Vue 3 和原生 JavaScript，可自行修改和扩展。
- 🎨 **白色标签化** – 完全控制表单和设计器外观，支持 CSS 变量自定义主题和样式。
- 🤖 **AI 辅助** – 通过 API 集成 AI，支持自然语言生成表单、翻译和智能内容建议。
- 🏥 **多行业适用** – 适用于保险、医疗、市场研究、教育、人力资源、电商、客户体验、非营利组织和银行等领域，支持敏感数据的安全收集。
- 🔒 **数据安全与合规** – 支持自托管，确保数据流完全在自有基础设施内，符合 HIPAA、FERPA、GDPR 等法规要求。
- ⚙️ **前后端分离** – 仅提供前端 UI 库，需自行构建后端处理数据存储、用户管理和业务逻辑。
- 📋 **灵活授权管理** – 许可可分配给多个开发者，提供直接的技术支持和帮助台访问。

---

### [GitHub - callstackincubator/react-native-grab：React Native UI 变更的触控抓取上下文工具 · GitHub](https://github.com/callstackincubator/react-native-grab)

**原文标题**: [GitHub - callstackincubator/react-native-grab: Touch-to-grab context tool for React Native UI changes · GitHub](https://github.com/callstackincubator/react-native-grab)

React Native Grab 是一个用于 React Native 的触摸抓取上下文工具，旨在通过直接选择屏幕上的 UI 元素来捕获精确的源代码上下文，从而帮助开发者更高效地进行 UI 修改。

- 🎯 **精准选择元素**：通过触摸直接选择屏幕上的确切原生 UI 元素，无需在提示中描述布局。
- 🏗️ **仅支持新架构**：该库仅适用于启用了 Fabric 渲染器的新架构，不兼容旧架构或 Paper 渲染器。
- ⚡ **提升编辑效率**：捕获真实的 React Native 视图上下文，减少对低熵 UI 更改（如间距、对齐和文本更新）的搜索时间。
- 🔧 **集成与配置**：通过 Metro 中间件集成，安装后需在应用根节点包裹 `ReactNativeGrabRoot`，并在使用原生导航器时为每个屏幕包裹 `ReactNativeGrabScreen`。
- 📚 **详细文档与支持**：提供完整的安装、快速开始、API 和故障排除指南，由 Callstack 团队维护，开源且免费使用。

---

### [GitHub - rcaferati/react-awesome-slider: 一款高性能、轻量级的 React 滑块/轮播组件，专为媒体与内容过渡设计，具备 60 帧动画、模块化样式、可选高阶组件及全页导航工具。🖥️📱 · GitHub](https://github.com/rcaferati/react-awesome-slider)

**原文标题**: [GitHub - rcaferati/react-awesome-slider: A performant, lightweight React slider/carousel for media and content transitions, featuring 60fps animations, modular styling, optional HOCs, and fullpage navigation utilities. 🖥️📱 · GitHub](https://github.com/rcaferati/react-awesome-slider)

这是一个高性能、轻量级的 React 轮播组件，提供流畅的动画、模块化样式、可选的高阶组件和全页面导航工具。

- 🚀 **高性能轮播组件** – 提供流畅的 60fps 动画，支持媒体和内容过渡。
- 🎨 **多种动画效果** – 默认侧滑动画，额外提供立方体、折叠、缩放等动画样式。
- 📱 **响应式与触摸支持** – 支持移动端触摸滑动导航。
- 🔧 **灵活的配置选项** – 可通过 `media` 属性或子元素定义幻灯片，支持无限循环、自动播放等。
- 🎛️ **高阶组件（HOC）支持** – 包含自动播放、带标题图像、动画文字等包装器。
- 🌐 **全页面导航工具** – 提供 `Provider`、`Link` 等组件，支持幻灯片作为路由的 SPA 应用。
- 💅 **模块化样式定制** – 支持 CSS 变量覆盖和 CSS Modules，便于主题和样式调整。
- 📦 **易于集成** – 通过 npm 安装，兼容 React 18+，提供详细的快速入门指南。

---

### [故事书 - Storybook](https://react-awesome-slider.caferati.dev/)

**原文标题**: [storybook - Storybook](https://react-awesome-slider.caferati.dev/)

本文介绍了人工智能在医疗领域的应用现状与前景，重点探讨了其在疾病诊断、治疗方案优化及医疗管理效率提升方面的作用，并简要提及了相关的技术挑战和伦理考量。

- 🤖 AI 辅助诊断系统能通过分析医学影像快速识别病灶，提高早期疾病检出率
- 💊 基于机器学习的个性化治疗方案可结合患者数据优化用药剂量和治疗路径
- 📊 智能医疗管理平台能整合临床数据，减少行政负荷，提升医院运营效率
- ⚠️ 数据隐私保护与算法透明度仍是医疗 AI 推广过程中需要解决的关键问题
- 🔮 未来 AI 或将在远程医疗、药物研发等领域产生更深入的变革性影响

---

### [打造你的复古游戏库 - 8bitcn/ui](https://www.8bitcn.com/)

**原文标题**: [Build your retro library - 8bitcn/ui](https://www.8bitcn.com/)

8bitcn/ui 是一个复古 8 位风格的开源 UI 组件库，提供多种组件和主题，支持主流框架，并包含代码分发平台。

- 🎮 提供复古 8 位风格组件，如按钮、下拉菜单、游戏菜单等
- 🧩 支持多种前端框架，可快速构建游戏化界面
- 📦 包含代码分发平台，方便开发者使用和分享
- 🎨 提供多种主题和组件块，如游戏状态、进度条、弹窗等
- 🤝 开源项目，由社区贡献者共同维护，代码托管在 GitHub
- 💖 接受赞助，有不同等级的赞助商支持项目发展
- 🌐 鼓励用户提交使用项目构建的应用，有机会在网站上展示

---

### [入门指南 - 8bitcn/ui](https://www.8bitcn.com/docs)

**原文标题**: [Getting Started - 8bitcn/ui](https://www.8bitcn.com/docs)

8bitcn/ui 是一个提供复古风格 UI 组件的库，基于 shadcn/ui 构建，支持快速集成到项目中，并提供 AI 辅助开发功能。

- 🎮 提供多种复古风格 UI 组件，如健康条、经验条、复古模式切换器等
- ⚙️ 支持通过 components.json 快速添加组件库注册表
- 🤖 可选初始化 MCP 配置，实现 AI 辅助开发，提供完整的组件库上下文
- 📚 包含详细文档、组件示例和区块模板
- 🛠️ 由 OrcDev 和贡献者开发，源代码托管在 GitHub
- 💝 得到 Shadcn Blocks、Shadcn Studio 等项目的赞助支持

---

### [React Cosmos](https://reactcosmos.org/)

**原文标题**: [React Cosmos](https://reactcosmos.org/)

React Cosmos 是一个用于独立开发和测试 React UI 组件的沙盒环境，支持快速原型设计、轻松调试和规模化质量维护，并兼容多种主流框架和工具。

- 🧪 通过基于文件系统的模块约定轻松定义组件状态
- 🎮 提供浏览组件状态和操作组件的交互式界面
- 🌐 支持将交互式组件库部署到任何静态托管服务
- 🔌 兼容 Vite、Webpack、React Native、Next.js 及自定义设置
- 🧩 提供全栈插件系统以扩展 React Cosmos 的各个方面
- 🏗️ 采用 100% TypeScript 编写，依赖少，设计测试严谨

---

### [引言 – React Cosmos](https://reactcosmos.org/docs#what-is-react-cosmos)

**原文标题**: [Introduction – React Cosmos](https://reactcosmos.org/docs#what-is-react-cosmos)

React Cosmos 是一个用于独立开发和测试 UI 组件的强大工具，通过沙盒环境和组件库功能优化工作流程，支持快速迭代和高质量组件开发，并具备轻量级架构和全面的插件系统。

- 🧩 组件隔离开发：允许在独立环境中专注于单个组件，提升迭代速度与组件质量
- 📚 组件库构建：帮助组织项目并促进组件复用，节省时间并确保设计一致性
- 🛠️ 核心功能丰富：包括基于文件系统的 Fixtures 定义、用户友好的浏览界面、数据操控面板和静态导出部署
- 🔌 广泛集成支持：与 Vite、Webpack、React Native、Next.js 等主流工具无缝集成，并支持自定义设置
- 🧱 轻量架构设计：采用库而非框架模式，确保兼容性与代码简洁性，专注于 React 生态
- 🔧 全面插件系统：通过低层级插件 API 实现高度可扩展性，核心功能也基于同一系统构建
- ⚛️ 专注 React 生态：充分利用 React 组件模型潜力，为开发者提供卓越体验

---

### [BlockNote - 基于块的 JavaScript React 富文本编辑器](https://www.blocknotejs.org/)

**原文标题**: [BlockNote - Javascript Block-Based React rich text editor](https://www.blocknotejs.org/)

BlockNote 是一款面向 React 的开源、AI 原生、现代化块编辑器，提供即用型编辑体验和高度可定制性，支持实时协作与 AI 集成，适用于个人和商业项目。

- ✨ 即用型编辑器：提供完整的块编辑体验，包括斜杠菜单、格式化工具栏和拖拽功能，开箱即用。
- 🛠️ 开发者友好：提供类型安全、直观的 API，支持自定义块、内联内容和设计系统集成。
- 🤝 实时协作：基于 Yjs 实现本地优先的实时同步、评论和版本控制，支持离线编辑。
- 🧠 AI 集成：支持在编辑器中直接进行 AI 辅助写作和编辑，可连接多种 AI 模型。
- 🌍 开源承诺：核心编辑器免费开源，高级功能如 AI 集成和导出工具对开源项目免费，商业项目需订阅。
- 🏛️ 生态贡献：基于 ProseMirror 和 Yjs 构建，积极为开源生态系统做出贡献。
- 💰 透明定价：提供清晰的许可模式，核心功能免费，高级功能按需订阅。

---

### [BlockNote - 示例](https://www.blocknotejs.org/examples)

**原文标题**: [BlockNote - Examples](https://www.blocknotejs.org/examples)

BlockNote 是一个功能丰富的块编辑器框架，提供多种示例和功能演示，涵盖基础设置、后端集成、UI 组件定制、主题调整、互操作性、自定义模式、协作编辑和 AI 集成等方面。

- 🧱 **基础功能**：包括基本设置、文档 JSON 展示、多列块、默认模式展示及块操作等示例。
- 🔧 **UI 组件定制**：支持移除 UI 元素、添加快捷工具栏按钮、块类型选择项及侧边菜单按钮等。
- 🎨 **主题与样式**：提供添加 CSS 类、更改字体、覆盖 CSS 样式和主题变量，以及代码块语法高亮等功能。
- 🔄 **互操作性**：支持将块转换为 HTML、Markdown、PDF、DOCX 等格式，并支持从 HTML 或 Markdown 解析为块。
- 🛠️ **自定义模式**：包括提醒块、提及菜单、字体样式、PDF 块等自定义块类型的实现示例。
- 👥 **协作编辑**：集成 PartyKit、Liveblocks、Y-Sweet 和 ElectricSQL 等工具，支持实时协作和评论功能。
- 🤖 **AI 集成**：提供富文本编辑器 AI 集成、AI Playground 演示及添加 AI 菜单项等示例。
- 📚 **示例资源**：提供交互式演示环境和多个代码示例，方便开发者快速上手和定制。

---

### [GitHub - Shopify/react-native-skia: 基于 Skia 的高性能 React Native 图形库 · GitHub](https://github.com/Shopify/react-native-skia)

**原文标题**: [GitHub - Shopify/react-native-skia: High-performance React Native Graphics using Skia · GitHub](https://github.com/Shopify/react-native-skia)

React Native Skia 是一个为 React Native 提供高性能 2D 图形渲染能力的库，它基于 Google 的 Skia 图形引擎，广泛应用于 Chrome、Android 和 Flutter 等产品中。

- 🎨 **高性能图形渲染**：利用 Skia 引擎为 React Native 应用提供强大的 2D 绘图功能。
- 🔧 **双后端支持**：默认使用 Ganesh 后端，也可通过配置启用实验性的 Graphite 后端（需 Android API 26+）。
- 📚 **完善文档与社区**：提供详细文档、贡献指南，并在 GitHub 上拥有活跃的开发者社区（8.2k 星标）。
- 🛠️ **开发友好**：支持库的本地构建、测试，并采用 TypeScript 和 C++ 为主要开发语言。
- 📄 **开源许可**：基于 MIT 许可证发布，遵循明确的行为准则和安全政策。

---

### [GitHub - rommguy/react-custom-scroll：轻松自定义浏览器滚动条，保留原生操作系统滚动行为 · GitHub](https://github.com/rommguy/react-custom-scroll)

**原文标题**: [GitHub - rommguy/react-custom-scroll: Easily customize the browser scroll bar with native OS scroll behavior · GitHub](https://github.com/rommguy/react-custom-scroll)

这是一个用于 React 的跨浏览器自定义滚动条组件，它保持了原生滚动行为但允许自定义视觉样式。

- 🎨 **可自定义设计** - 通过 CSS 类`rcs-custom-scrollbar`和`rcs-inner-handle`修改滚动条外观
- 🌐 **跨浏览器兼容** - 在所有浏览器中实现相同的滚动条设计和布局
- ⚡ **保持原生行为** - 使用原生滚动机制，保持原有的滚动动画和速率
- 📦 **安装简单** - 通过`npm i react-custom-scroll --save`安装，需要 React 18+
- ⚙️ **丰富配置选项** - 支持`heightRelativeToParent`、`flex`、`onScroll`、`rtl`、`scrollTo`等多种属性
- 🔧 **Flexbox 支持** - 提供两种方案在 flex 布局中使用自定义滚动条
- 📝 **TypeScript 支持** - 可通过`@types/react-custom-scroll`安装类型定义
- 🐛 **问题排查指南** - 包含常见问题解决方案，如移除 overflow 属性、注意 JSX 大小写等
- 🛠️ **开发与构建** - 使用 Vite 构建，支持开发模式和测试
- 📄 **开源项目** - MIT 许可证，拥有 571 星标，66 个分支，被 1.8k+ 项目使用

---

### [GitHub - sojinantony01/react-cron-generator：用于生成cron表达式的简单React组件 · GitHub](https://github.com/sojinantony01/react-cron-generator)

**原文标题**: [GitHub - sojinantony01/react-cron-generator: Simple react component to generate cron expressions · GitHub](https://github.com/sojinantony01/react-cron-generator)

这是一个用于生成 Cron 表达式的 React 组件，支持 Unix 和 Quartz 两种格式，提供可视化构建、验证、国际化等功能，适用于任务调度场景。

- 🕐 **支持双格式**：兼容 Unix（5 字段）和 Quartz（6 或 7 字段）两种 Cron 表达式格式
- 🔄 **自动转换**：内置 Unix 与 Quartz 格式间的相互转换功能
- ✅ **内置验证**：提供完整的 Cron 表达式验证机制
- 🌍 **国际化**：支持自定义翻译函数，适配多语言场景
- ♿ **无障碍访问**：符合 WCAG 标准，支持键盘导航和屏幕阅读器
- 📱 **响应式设计**：适配移动端与桌面端各种设备
- 🎨 **高度可定制**：允许样式配置和标签自定义
- 🔒 **类型安全**：完全使用 TypeScript 开发，提供完整类型定义
- ⚡ **性能优化**：采用记忆化计算和高效重渲染策略
- 📦 **易于集成**：通过 npm 或 yarn 安装，提供详细使用示例

---

### [GitHub - aralroca/next-translate: Next.js 插件 + i18n API，适用于 Next.js 🌍 - 轻松加载页面翻译并便捷使用！· GitHub](https://github.com/aralroca/next-translate)

**原文标题**: [GitHub - aralroca/next-translate: Next.js plugin + i18n API for Next.js 🌍  -  Load page translations and use them in an easy way! · GitHub](https://github.com/aralroca/next-translate)

Next-translate 是一个为 Next.js 项目提供国际化支持的库，它包含一个 Next.js 插件和一个 i18n API，旨在简化页面翻译的加载和使用过程。

- 🌍 **核心目标**：在 Next.js 环境中保持翻译的简洁性。
- 🚀 **自动优化**：根据页面配置自动加载所需语言和命名空间的翻译文件，提升性能。
- 📦 **轻量高效**：体积小巧（约 1KB），支持 Tree Shaking，且无额外依赖。
- 🛠️ **易于配置**：通过 `i18n.json` 配置文件定义支持的语言、默认语言及各页面所需的翻译命名空间。
- 🔌 **插件集成**：通过 `next-translate-plugin` 在构建时处理翻译，与代码中的 `useTranslation` 等 API 配合使用。
- 📄 **多种使用方式**：提供 `useTranslation` Hook、`Trans` 组件、`getT` 异步函数等多种 API 来在组件和页面中使用翻译。
- 🔢 **功能丰富**：支持插值、复数形式、嵌套翻译、回退机制、HTML 内嵌翻译和自定义格式化器等高级功能。
- ⚙️ **灵活适配**：支持 Next.js 13+ 的 App Router 目录结构，并提供了配置 Turbopack 的选项。
- 🧩 **扩展性强**：可通过 `I18nProvider` 实现页面内多语言混合使用等复杂场景。
- 📚 **示例齐全**：提供基础、复杂、App 目录及禁用 Webpack 加载器等多种演示项目供参考。

---

### [GitHub - react-icons/react-icons: 流行图标包的 SVG React 图标 · GitHub](https://github.com/react-icons/react-icons)

**原文标题**: [GitHub - react-icons/react-icons: svg react icons of popular icon packs · GitHub](https://github.com/react-icons/react-icons)

React Icons 是一个用于在 React 项目中轻松集成流行图标库的工具，它通过 ES6 导入方式支持按需使用图标，优化项目体积。

- 📦 **安装简便**：通过 yarn 或 npm 即可安装，支持现代项目及特定框架如 Meteor、Gatsby。
- 🎯 **按需导入**：仅导入所需图标，避免整个字体文件，示例展示了从 Font Awesome 导入啤酒图标。
- 📚 **多图标库支持**：包含 Font Awesome、Material Design、Ant Design 等 30 多个图标集，总计数万个图标。
- ⚙️ **可配置性**：使用 IconContext 全局设置颜色、大小、类名等属性，支持 React 16.3 以上版本。
- 🔄 **版本迁移**：从 v2 升级到 v3 需调整导入方式，并手动处理垂直对齐样式。
- 🛠️ **开发与贡献**：提供构建脚本，支持添加新图标集，包含预览网站和演示项目。
- 📄 **许可信息**：项目基于 MIT 许可证，图标来源多样，需遵循各自授权协议。
- 🌐 **项目活跃**：GitHub 上拥有 12.5k 星标，由社区维护，支持 TypeScript 并免去额外类型依赖。

---

### [GitHub - kcsujeet/ilamy-calendar：一款现代化的开源FullCalendar替代方案，专为React设计。支持月、周、日、年视图，具备拖放功能，水平和垂直资源视图，以及符合RFC 5545 标准的重复事件——全部采用 MIT 许可证。· GitHub](https://github.com/kcsujeet/ilamy-calendar)

**原文标题**: [GitHub - kcsujeet/ilamy-calendar: A modern, open-source FullCalendar alternative for React. Month, week, day, and year views with drag-and-drop, horizontal and vertical resource views, and RFC 5545 recurring events — all MIT licensed. · GitHub](https://github.com/kcsujeet/ilamy-calendar)

这是一个名为 ilamy-calendar 的开源 React 日历组件库，提供强大的日程管理功能，采用现代技术栈构建。

- 🗓️ **多视图支持**：包含月、周、日和年视图，并支持平滑过渡
- 📊 **资源日历**：通过时间线布局可视化和管理多资源事件
- 🎯 **拖放功能**：支持在日期和时间槽之间移动事件，具备碰撞检测
- 🔄 **RFC 5545 重复事件**：完整 RRULE 支持，提供 Google 日历风格的操作
- 📤 **iCalendar 导出**：符合 RFC 5545 标准的.ics 文件导出，支持重复事件处理
- 🌍 **国际化**：支持 100 多种语言环境，可配置周起始日
- 🎨 **可定制样式**：使用 Tailwind CSS 和 CSS 变量进行灵活主题定制
- ⚡ **性能优化**：按需生成重复事件，高效日期范围计算，最小化重新渲染
- 📱 **响应式设计**：适配桌面、平板和移动设备的自适应布局
- 🔧 **开发者体验**：完整 TypeScript 支持，全面的类型定义和文档
- 🎛️ **高级事件管理**：全天事件、多日事件、事件验证和批量操作

---

### [文员技能 - AI | 文员文档](https://clerk.com/docs/guides/ai/skills?utm_source=cooper_press&utm_medium=newsletter&utm_campaign=skills&utm_content=03-06-26&dub_id=MzwPigDjvT8ay9Mn)

**原文标题**: [Clerk Skills - AI | Clerk Docs](https://clerk.com/docs/guides/ai/skills?utm_source=cooper_press&utm_medium=newsletter&utm_campaign=skills&utm_content=03-06-26&dub_id=MzwPigDjvT8ay9Mn)

Clerk Skills 是为 AI 编程助手设计的可安装技能包，使其掌握 Clerk 平台的专业知识，从而帮助开发者集成身份验证、管理组织、同步用户等功能。

- 🧩 Clerk Skills 是可安装的技能包，能让 AI 助手掌握 Clerk 的专业知识，协助处理身份验证、组织管理、用户同步等任务
- ⚙️ 支持通过 `npx skills add clerk/skills` 安装全部技能，或使用 `--skill` 参数安装特定技能
- 🤖 兼容 Claude Code、Cursor、Windsurf、GitHub Copilot 等多种主流 AI 编程助手
- 📚 提供七种核心技能：基础路由、框架集成、自定义 UI、Next.js 高级模式、组织管理、Webhook 同步和测试支持
- 💬 安装后可直接通过自然语言指令调用对应技能，例如“为我的 Next.js 应用添加 Clerk 身份验证”或“通过 Webhook 将用户同步到 Prisma”
- 🔄 内容最后更新于 2026 年 3 月 4 日，并设有反馈渠道供用户评价

---

### [学习 Visual Studio Code](https://lazarpress.gumroad.com/l/learnvscode)

**原文标题**: [Learn Visual Studio Code](https://lazarpress.gumroad.com/l/learnvscode)

本文介绍了人工智能在医疗领域的应用现状与前景，重点探讨了其在疾病诊断、治疗方案优化及医疗管理效率提升方面的作用，同时简要提及了相关的伦理挑战。

- 🩺 AI 辅助诊断系统能通过分析医学影像快速识别病灶，提高早期疾病检出率
- 💊 基于机器学习的个性化治疗方案可结合患者数据优化用药剂量和治疗路径
- 📊 智能医疗管理系统能自动化处理病历整理、预约调度等行政工作
- ⚖️ 数据隐私保护和算法透明度是目前医疗 AI 面临的主要伦理考量
- 🔮 未来 AI 将与人类医生协同工作，形成“增强智能”医疗新模式

---

### [Inertia.js v3 现已进入测试阶段 | Laravel - 为工匠与代理打造的精简技术栈](https://laravel.com/blog/inertiajs-v3-is-now-in-beta)

**原文标题**: [Inertia.js v3 Is Now in Beta | Laravel - The clean stack for Artisans and agents](https://laravel.com/blog/inertiajs-v3-is-now-in-beta)

Inertia.js v3 首个测试版发布，引入 Vite 插件、内置 XHR 客户端、乐观更新等新特性，简化配置并提升开发体验，现开放社区测试。

- 🚀 **内置 XHR 客户端**：移除 Axios 依赖，内置轻量 HTTP 客户端，减少包体积与依赖项。
- ⚡ **Vite 插件集成**：自动处理页面解析、懒加载与 SSR 配置，大幅减少初始化代码。
- 🔄 **乐观更新支持**：用户操作可立即更新界面，服务器响应后自动同步或回滚状态。
- 🌐 **独立 HTTP 请求钩子**：新增 `useHttp` 支持非页面跳转的 API 调用，保留响应式状态管理。
- ⚙️ **布局属性管理**：通过 `useLayoutProps` 统一管理布局参数，支持页面动态覆盖。
- 🛠️ **异常处理增强**：新增 `handleExceptionsUsing` 方法，支持自定义错误页并共享全局数据。
- 📦 **开发环境 SSR 优化**：Vite 插件支持开发时自动 SSR，无需单独启动 Node 服务。
- 🔗 **即时页面跳转**：通过 `component` 属性预加载目标组件，实现无等待导航体验。
- 📄 **嵌套属性类型支持**：`Inertia::optional()` 等方法现支持嵌套数组与点符号路径。
- ⚠️ **升级要求**：需 PHP 8.2+、Laravel 11+ 及对应前端框架新版本，部分 API 变更需迁移。

---

### [发布 npmx：一款面向 npm 注册表的快速现代浏览器](https://npmx.dev/blog/alpha-release)

**原文标题**: [Announcing npmx: a fast, modern browser for the npm registry](https://npmx.dev/blog/alpha-release)

npmx 是一个面向 npm 注册表的快速现代浏览器，旨在通过提供包大小、模块格式和过时依赖等关键数据，帮助开发者更高效地搜索、评估和管理 npm 包。该项目自 2026 年 1 月启动后，迅速吸引了全球开发者社区的积极参与，强调开放性、可访问性和国际化，目前已在 alpha 阶段提供多语言支持、社交功能及与多种开发工具的直接集成。

- 🚀 **快速启动**：npmx 旨在提升 npm 包的搜索、评估和管理速度，提供安装大小、模块格式等实用数据。
- 🌍 **社区驱动**：项目启动后迅速获得全球开发者响应，16 天内吸引超过 105 位贡献者，体现了开放协作的力量。
- 🔧 **功能丰富**：支持包详情查看、下载统计、过时依赖警告、ESM/CJS 模块格式识别，并集成 StackBlitz 等演示环境。
- 🌐 **多语言与无障碍**：提供 19 种语言界面、深浅色模式及键盘友好设计，注重可访问性。
- 🤝 **社交与协作**：内置包点赞和社交功能，鼓励开发者与包维护者建立联系，强化开源社区互动。
- 📈 **持续发展**：目前处于 alpha 阶段，积极收集用户反馈以迭代至 beta 版本，欢迎新手参与贡献。
- 💡 **开源引导**：提供详细的首次贡献指南，降低参与门槛，营造包容的开源环境。

---

### [我们如何遭遇沙虫袭击：一份完整的复盘报告 | Trigger.dev](https://trigger.dev/blog/shai-hulud-postmortem)

**原文标题**: [How we got hit by Shai-Hulud: A complete post-mortem | Trigger.dev](https://trigger.dev/blog/shai-hulud-postmortem)

2025 年 11 月 25 日，Trigger.dev 公司遭遇了名为“Shai-Hulud 2.0”的 npm 供应链蠕虫攻击。攻击通过一名工程师在开发机器上安装受感染的依赖包开始，窃取了其 GitHub 凭证，导致攻击者获得了对公司 GitHub 组织的未授权访问。攻击者进行了长达 17 小时的侦察，克隆了 669 个仓库，并最终在 10 分钟内对 16 个仓库的 199 个分支进行了破坏性操作（如强制推送和关闭拉取请求）。幸运的是，公司的 npm 官方包从未被感染，生产数据库和 AWS 资源也未受影响。团队在几分钟内检测并响应，撤销了访问权限，并在 7 小时内恢复了所有分支。事后，公司采取了多项安全强化措施，包括全局禁用 npm 脚本、升级到 pnpm 10、启用分支保护以及采用 OIDC 进行 npm 发布。

- 🐛 **攻击源头**：工程师在运行 `pnpm install` 时，依赖树中的恶意包通过 `preinstall` 脚本执行，下载并运行了用于凭证窃取的 TruffleHog 工具。
- 🔍 **长时间侦察**：攻击者窃取凭证后，潜伏约 17 小时，从美国和印度基础设施大规模克隆公司仓库，并实时监控工程师的正常工作活动。
- 💥 **破坏性攻击**：攻击在短时间内集中进行，强制推送分支、关闭拉取请求，并留下署名为“Linus Torvalds”的虚假提交。
- 🚨 **快速检测与响应**：团队通过 Slack 通知迅速发现异常，在 4 分钟内识别并移除了受损账户，阻止了攻击的持续。
- 🛡️ **有限的实际损害**：公司的 npm 包未被篡改，生产系统未遭入侵，这得益于已实施的 2FA 发布保护和部分分支保护规则。
- 🔑 **凭证暴露风险**：在受损笔记本电脑的回收站中发现了 GitHub App 的私钥，虽无证据表明被利用，但公司立即进行了密钥轮换并通知了可能受影响的客户。
- 🛠️ **安全措施升级**：事后全局禁用 npm 脚本、升级至 pnpm 10 以默认忽略脚本并设置包安装延迟、为所有仓库启用分支保护、采用 OIDC 进行 npm 发布以消除长期令牌风险。
- 📚 **经验教训**：强调了在 npm 生态中包可执行任意代码的风险，建议所有团队在 `.npmrc` 中设置 `ignore-scripts=true`，并为关键分支启用保护。

---

