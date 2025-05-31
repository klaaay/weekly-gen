### [React 状态周报第 429 期：2025 年 5 月 14 日](https://react.statuscode.com/issues/429)

**原文标题**: [React Status Issue 429: May 14, 2025](https://react.statuscode.com/issues/429)

概述  
React Status 将于 5 月 28 日恢复发布，编辑 Peter Cooper 将参加 Google I/O。本期内容包括 React 相关工具更新、技术文章推荐、赞助商信息及其他 JavaScript 生态动态。  

- 📅 **暂停通知**：React Status 暂停发布，5 月 28 日恢复，编辑将参加 Google I/O。  
- ⚡ **React 电子项目**：介绍使用 React 设计电路板的工具 tscircuit。  
- 🎓 **React 课程**：Frontend Masters 提供 React 19+ 新特性课程。  
- 🤔 **Server 组件解析**：Dan Abramov 解释如何将 Server 组件预渲染为静态资源。  
- 🔄 **TanStack Query 更新**：RFC 提议合并方法为`query()`和`infiniteQuery()`。  
- 🏗️ **React 未来讨论**：Reddit 社区探讨 React 在 2025 年的前景。  
- 🛠️ **工具推荐**：包括 React Chrono 时间轴组件、Bippy React 内部工具等。  
- 📰 **技术文章**：涵盖 React Context、React Query、依赖反转等主题。  
- 📢 **赞助商信息**：Meticulous 自动化测试、Hope AI 设计系统等。  
- 🌐 **JavaScript 动态**：V8 资源管理、Parcel 更新、npm 包最佳实践等。  
- 📧 **订阅提醒**：可随时退订，隐私政策保障邮箱安全。

---

### [React，可视化 —— react.gg](https://react.gg/visualized)

**原文标题**: [React, visualized âÂ react.gg](https://react.gg/visualized)

网页的发展历史为 React 的诞生提供了重要背景，每一阶段的技术演进都为 React 的灵感来源奠定了基础。

- 🌐 jQuery 时代：简化了 DOM 操作和跨浏览器兼容性，为前端开发铺平道路  
- � Backbone 时代：引入了 MVC 架构，推动前端应用的结构化发展  
- ⚡ AngularJS 时代：双向数据绑定和指令系统革新了前端开发方式  
- 🧩 React 诞生：综合前人经验，引入虚拟 DOM 和组件化思想解决性能问题  
- 🔄 技术演进：每个阶段的技术突破都为 React 的设计理念提供了关键启发

---

### [TanStack Router 之美 | TkDodo 的博客](https://tkdodo.eu/blog/the-beauty-of-tan-stack-router)

**原文标题**: [The Beauty of TanStack Router | TkDodo's blog](https://tkdodo.eu/blog/the-beauty-of-tan-stack-router)

TanStack Router 是一款专为 TypeScript 设计的现代化路由解决方案，提供出色的开发者体验和类型安全支持。以下是其主要特点：

- 🚀 **类型安全路由**：完全基于 TypeScript 设计，提供高度类型推断，避免手动类型断言，确保路由参数和链接的类型安全。  
- 🔍 **严格或宽松参数获取**：通过 `useParams` 的 `strict` 和 `from` 参数，灵活控制路由参数的获取方式，兼顾类型安全和复用性。  
- 🔗 **类型安全的链接**：`<Link>` 组件自动验证目标路由和参数，避免无效导航。  
- 📊 **搜索参数状态管理**：支持搜索参数的验证和类型化，通过 `validateSearch` 和标准 schema 库（如 `arktype`）实现。  
- ⚡ **细粒度订阅**：通过选择器（selectors）优化性能，避免不必要的重新渲染，类似状态管理库的订阅机制。  
- 📂 **文件式路由支持**：支持代码式和文件式路由配置，便于快速定位和维护路由逻辑。  
- ⏳ **内置 Suspense 支持**：自动包裹路由组件，简化异步数据加载和错误边界处理。  
- 🔄 **React Transitions 限制**：目前因 `useSyncExternalStore` 的限制，对并发特性的支持有限。  
- 🛠 **更多功能**：包括路由上下文、嵌套路由、查询集成等，全面提升开发效率。  

TanStack Router 结合了类型安全和开发者友好性，是 React 生态中路由方案的佼佼者。

---

### [发布 v9.0.0 · storybookjs/storybook · GitHub](https://github.com/storybookjs/storybook/releases/tag/v9.0.0)

**原文标题**: [Release v9.0.0 · storybookjs/storybook · GitHub](https://github.com/storybookjs/storybook/releases/tag/v9.0.0)

Storybook 9.0 是一个重大版本更新，专注于测试和包体积优化，引入了多项新功能和改进，同时对现有功能进行了大量修复和优化。

- 🚀 **组件测试**：新增交互测试、无障碍测试、视觉变化测试和覆盖率测试功能  
- 🪶 **包体积优化**：减少了 48% 的包体积  
- 🏷️ **标签管理**：支持基于标签的组织方式  
- 🌐 **全局变量**：新增 Story 全局变量支持  
- 🛠️ **框架升级**：对 Svelte、Next.js、React Native 和 Angular 进行了重大升级  
- 📚 **迁移指南**：提供了详细的迁移指南以帮助用户从旧版本升级  
- 🔧 **大量修复和改进**：涵盖了 A11y、Controls、Docs、Vitest 等多个模块的优化和问题修复  
- 🧩 **核心功能整合**：将多个插件（如 Controls、Viewport 等）整合到核心中  
- ⚡ **性能提升**：优化了测试模块、高亮功能等核心体验  
- 📦 **依赖项清理**：移除了多个过时或不必要的依赖项  

该版本由 29 位贡献者共同完成，总计提交了 240 项变更。

---

### [React Router RSC 预览 | Remix](https://remix.run/blog/rsc-preview)

**原文标题**: [React Router RSC Preview | Remix](https://remix.run/blog/rsc-preview)

React Router 发布了 RSC（React Server Components）的预览支持，允许开发者在现有路由中通过 loaders/actions 返回 RSC 内容，并支持混合使用客户端组件和服务端组件。

- 🚀 **RSC 预览支持**：React Router 现已支持 RSC，可通过克隆仓库体验。
- 🔄 **混合路由**：支持现有路由返回 RSC 内容，同时新增“服务端组件路由”（Server Component Routes）。
- 💻 **客户端组件**：通过 `"use client"` 标记客户端组件。
- ⚡ **服务端函数**：通过 `"use server"` 定义服务端函数，调用后自动重新验证路由。
- 🎯 **增量采用**：可在现有应用中逐步采用 RSC，无需全面迁移。
- 📊 **数据优化**：通过中间件实现查询批处理和缓存，避免 N+1 查询问题。
- 🛠️ **工具支持**：当前预览基于 Parcel，未来将支持 Vite 等更多打包工具。
- 🙏 **致谢**：特别感谢 Jacob Ebey 在 RSC 支持上的多年贡献。
- 🎬 **示例演示**：提供了电影示例演示和源代码，展示 RSC 的实际应用。
- 🔮 **未来计划**：等待 Vite 官方支持 RSC，并优化页面重新验证机制。

---

### [Astro 5.8 | Astro](https://astro.build/blog/astro-580/)

**原文标题**: [Astro 5.8 | Astro](https://astro.build/blog/astro-580/)

Astro 5.8 是一个重要的更新，主要提升了 Node.js 的最低版本要求，并提供了升级工具和指南。此外，还包含了一些错误修复和社区贡献者的感谢。

- 🔄 **Node.js 版本更新**：最低要求提升至 18.20.8，并建议升级至 Node.js 22，因为 Node.js 18 已停止支持。  
- ⚙️ **升级工具**：推荐使用 `@astrojs/upgrade` CLI 工具或手动运行包管理器的升级命令。  
- 📜 **版本支持政策**：Astro 暂时仍支持 Node.js 18.20.8，但未来会完全放弃支持。  
- 🌐 **部署环境更新**：需确保本地和 CI/CD 环境使用支持的 Node.js 版本，可通过 `.nvmrc` 或环境变量设置。  
- ☁️ **Cloudflare Pages 用户**：需手动将 Node.js 版本覆盖为 22，因为默认版本 18.17.1 不再受支持。  
- 🐛 **错误修复**：包含自 5.7 版本以来的多项问题修复，详情参见更新日志。  
- 👏 **社区贡献**：感谢核心团队及众多社区贡献者的代码和文档改进。  
- 💬 **交流与反馈**：欢迎在 Astro Discord 中提问或交流。

---

### [删除边缘函数示例 by leerob · Pull Request #1135 · vercel/examples · GitHub](https://github.com/vercel/examples/pull/1135)

**原文标题**: [Delete edge functions examples by leerob · Pull Request #1135 · vercel/examples · GitHub](https://github.com/vercel/examples/pull/1135)

Vercel 宣布将逐步弃用 Edge Functions，并推荐用户迁移至 Fluid compute 和完整的 Node.js 运行时。  

- 🚨 **Edge Functions 弃用**：Vercel 宣布 Edge Functions 将被弃用，建议用户转向 Fluid compute。  
- 🔄 **替代方案**：Fluid compute 保留了 Edge Functions 的优势，同时避免了 Edge 运行时的限制。  
- 🌍 **区域一致性**：建议将 Vercel Function 区域与数据库区域保持一致，以提高性能。  
- 📅 **时间安排**：官方将在未来几个月内发布更多信息，现有用户无需立即采取行动。  
- 🛠 **清理工作**：Vercel 正在更新模板和示例，以引导新用户直接使用 Fluid。  
- 📊 **项目状态**：多个示例项目的状态更新显示部分成功和失败的情况。

---

### [流体计算](https://vercel.com/fluid)

**原文标题**: [Fluid compute](https://vercel.com/fluid)

无服务器形态的服务器性能  
Fluid Compute 结合了服务器的高效性和无服务器的灵活性，支持实时动态工作负载，如 API、流媒体和 AI。  

- 💡 **高效与灵活结合**：Fluid Compute 实现类似服务器的并发性，优化资源使用，提升效率。  
- ⏳ **解决闲置问题**：传统无服务器在闲置时资源利用率低，Fluid 则最大化计算时间，减少浪费。  
- 💬 **用户案例**：通过并发调用共享资源，某企业 API 端点成本降低 50% 且无需代码改动。  
- 🤖 **AI 工作负载**：低延迟、高并发处理，适应不同规模任务。  
- 🚀 **关键业务 API**：高流量下保持快速、稳定的响应。  
- 🖥️ **动态渲染**：极低延迟生成动态页面，提升加载速度。  
- 🔗 **中间件功能**：支持动态路由、身份验证和个性化设置。  
- 🌐 **全球扩展**：结合服务器和无服务器优势，高效扩展关键业务。  

**功能对比**  
- ❄️ **冷启动处理**：Fluid 预防冷启动，传统无服务器存在冷启动问题。  
- 📈 **扩展性**：Fluid 自动高效扩展，传统需手动或低效自动扩展。  
- 🔄 **并发模型**：Fluid 支持水平与垂直并发，传统仅单一方向。  
- 🛠️ **运维开销**：Fluid 自动优化，传统无服务器效率低下。  
- 💰 **定价模式**：均按需付费，但 Fluid 资源利用率更高。  

**动态 Web 应用特性**  
- 🔄 **函数内并发**：单实例处理多调用，降低成本。  
- ⚡ **冷启动优化**：预预热与字节码缓存加速响应。  
- 🌊 **流式传输**：实时数据推送，提升 AI/媒体应用性能。  
- 🌍 **跨区域容灾**：故障时自动切换备份区域。  
- 📊 **动态扩缩容**：根据需求实时调整资源。  
- 📝 **后响应任务**：响应后继续执行日志记录等操作。  

**行动号召**  
- 🚀 **立即部署**：开始构建卓越应用。  
- 📞 **联系销售**：获取更多支持。

---

### [GitHub 新手教程：使用 GitHub Copilot 构建 React 应用 - GitHub 博客](https://github.blog/ai-and-ml/github-copilot/github-for-beginners-building-a-react-app-with-github-copilot/)

**原文标题**: [GitHub for Beginners: Building a React App with GitHub Copilot - The GitHub Blog](https://github.blog/ai-and-ml/github-copilot/github-for-beginners-building-a-react-app-with-github-copilot/)

本文介绍了如何使用 GitHub Copilot 构建一个 React 前端应用，连接之前创建的 Planventure 后端 API。以下是关键步骤和要点：

- 🚀 **概述**：通过 GitHub Copilot 辅助，使用 React 和 Material UI 构建一个具有用户认证、行程管理等功能的前端应用。

- 💻 **准备工作**：需要 VS Code、Node.js、npm 和 GitHub Copilot 访问权限，或使用 GitHub Codespace 云端开发环境。

- 🔧 **初始设置**：克隆 Planventure 仓库，切换到 client-start 分支，安装依赖并启动开发服务器。

- 🔐 **用户认证**：创建 AuthLayout 组件，构建登录和注册表单，设置认证上下文和令牌管理。

- 🔄 **API 连接**：更新登录和注册表单以使用 API 服务，调试可能出现的错误。

- 📊 **仪表盘和导航**：创建带有侧边栏导航的仪表盘布局，展示用户的行程列表。

- ✏️ **行程管理**：添加新建行程表单，允许用户编辑行程详情，并管理每日活动行程。

- 🏨 **额外功能**：用户可添加住宿和交通信息到行程概览页面。

- 📌 **下一步**：完成 MVP 应用后，鼓励继续探索 GitHub Copilot 的免费使用，并参与社区讨论。

- 🎉 **总结**：借助 GitHub Copilot 高效构建功能齐全的 React 前端应用，提升开发效率。

---

### [RedwoodSDK 是一个面向 Cloudflare 的 React 框架](https://rwsdk.com/blog/your-react-meta-framework-feels-broken)

**原文标题**: [RedwoodSDK is a React framework for Cloudflare](https://rwsdk.com/blog/your-react-meta-framework-feels-broken)

现代 React 元框架让开发体验变得复杂，开发者常陷入抽象陷阱，而 RedwoodSDK 试图回归 JavaScript 本质，减少魔法代码。

- 🤯 开发者常因框架的复杂抽象感到困惑，代码与实际执行脱节，调试困难。  
- 🧩 框架隐藏底层逻辑，要求开发者适应新规则，而非利用已有 JavaScript 知识。  
- 🚫 当前框架问题：自定义语法、隐式转换、框架特定魔法词增加学习成本。  
- ✨ RedwoodSDK 解决方案：零魔法、基于 Web API、简单部署，保持透明和可组合性。  
- 🔄 对比示例：Next.js 和 Remix 的间接路由与数据加载 vs RedwoodSDK 的直接函数式路由。  
- 🌐 RedwoodSDK 原则：不假装新语言，不增加构建层，与 Web 和谐共处。  
- 🛠️ RedwoodSDK 技术栈：TypeScript、React、Vite 和 Cloudflare，简单透明。  
- 📚 更多阅读：RedwoodSDK 提供每路由文档控制、全栈共置和流式获取等功能。

---

### [使用 AI 构建基于物理的角色控制器 | Codrops](https://tympanus.net/codrops/2025/05/28/building-a-physics-based-character-controller-with-the-help-of-ai/)

**原文标题**: [Building a Physics-Based Character Controller with the Help of AI | Codrops](https://tympanus.net/codrops/2025/05/28/building-a-physics-based-character-controller-with-the-help-of-ai/)

概述：本文介绍了如何利用 AI 工具 Bolt.new 结合 React Three Fiber、Three.js 和 Rapier 构建一个基于物理的角色控制器，涵盖物理设置、动画集成、跨平台输入支持等关键步骤，展示了 AI 辅助开发在快速原型设计中的优势。

- 🚀 **AI 辅助开发**：使用 Bolt.new 工具，通过自然语言提示生成代码，简化物理设置、动画集成等复杂任务。
- 🎮 **物理基础**：采用 Rapier 物理引擎，使用胶囊碰撞体和地面平面实现角色移动和交互。
- ⚙️ **实时调试**：通过 Leva.js GUI 面板实时调整移动速度、跳跃力等参数，加速迭代。
- 📡 **地面检测**：利用射线检测技术判断角色是否着地，确保跳跃和动画过渡自然。
- 🕺 **动画集成**：通过 Mixamo 导入 GLB 模型，动态切换待机、奔跑和下落动画，实现流畅的动画混合。
- 🌍 **环境构建**：在 Blender 中设计场景并导出为 GLB 文件，优化纹理分辨率以提升性能。
- 📱 **跨平台输入**：支持桌面（键盘/鼠标）、移动设备（虚拟摇杆）和游戏手柄，通过 AI 生成统一逻辑。
- 💡 **AI 工作流**：开发者通过描述功能需求，AI 自动生成代码，减少样板代码编写，提高开发效率。
- 🎯 **成果展示**：最终项目包含物理碰撞、动画混合和跨平台支持，适合游戏和交互体验开发。

---

### [人工游乐场](https://artificial-playground-demo.netlify.app/)

**原文标题**: [Artificial Playground](https://artificial-playground-demo.netlify.app/)

好的，请提供需要总结的文本内容，我会按照您要求的格式生成概述和带表情符号的要点列表。  

示例格式：  

这里是文章的概述总结，简明扼要地概括全文核心内容。  

- 🌟 第一个关键点，用简短的语言描述。  
- 🔍 第二个关键点，突出重要信息。  
- 📌 第三个关键点，补充细节或结论。  

请提供具体文本，我会立即为您处理！

---

### [React 并发渲染的故事 - YouTube](https://www.youtube.com/watch?v=edN42P_vfCI)

**原文标题**: [The Story of Concurrent Rendering in React - YouTube](https://www.youtube.com/watch?v=edN42P_vfCI)

这是一个关于 YouTube 平台相关信息和政策的页面概览。

- 📢 **关于** - 提供 YouTube 的基本信息和背景。  
- 📰 **新闻** - 与 YouTube 相关的新闻和公告。  
- ©️ **版权** - 版权信息及政策。  
- 📩 **联系我们** - 提供与 YouTube 团队联系的途径。  
- 🎨 **创作者** - 与内容创作者相关的资源和支持。  
- 💼 **广告** - 广告合作和推广信息。  
- 💻 **开发者** - 开发者工具和资源。  
- 📜 **条款** - 使用条款和条件。  
- 🔒 **隐私** - 隐私政策和数据保护措施。  
- ⚖️ **政策与安全** - 平台政策及安全指南。  
- ▶️ **YouTube 工作原理** - 解释平台的功能和机制。  
- 🧪 **测试新功能** - 新功能的测试和更新信息。  
- 🏢 **© 2025 Google LLC** - 版权归属和公司信息。

---

### [使用 Expo 和原生代码实现实时音频处理](https://expo.dev/blog/real-time-audio-processing-with-expo-and-native-code)

**原文标题**: [Real-time audio processing with Expo and native code](https://expo.dev/blog/real-time-audio-processing-with-expo-and-native-code)

这是一个关于 Expo 网站导航和资源页面的内容，列出了主要的功能链接和公司信息。

- 🌐 **导航菜单**：包含博客、搜索、文档、工具等主要入口  
- ⚙️ **开发工具**：EAS（Expo 应用服务）、Expo CLI、EAS CLI、Expo Go 等开发者资源  
- 📚 **资源支持**：文档、博客、更新日志、通讯订阅和技术支持链接  
- 💼 **公司信息**：主页、定价、客户案例、关于我们和招聘信息  
- ⚖️ **法律条款**：服务协议、公平使用政策、隐私政策及社区准则  
- ©️ **版权声明**：归 650 Industries 公司所有，标注系统运行状态

---

### [React 全新 Activity 组件：性能大幅提升！ - YouTube](https://www.youtube.com/watch?v=gRKVL5w-2Lc)

**原文标题**: [React's New Activity Component: Huge Performance Win! - YouTube](https://www.youtube.com/watch?v=gRKVL5w-2Lc)

YouTube 平台相关信息概览  

- 📢 关于我们 - 提供 YouTube 的背景和基本信息  
- 🗞️ 新闻动态 - 获取 YouTube 相关的最新新闻和公告  
- ©️ 版权信息 - 了解 YouTube 的版权政策和内容  
- 📩 联系我们 - 提供与 YouTube 团队联系的途径  
- 🎨 创作者信息 - 面向内容创作者的相关资源和支持  
- 💼 广告合作 - 广告主和商业合作的详细信息  
- 👩💻 开发者资源 - 面向开发者的工具和 API 信息  
- 📜 服务条款 - 使用 YouTube 平台的法律条款  
- 🔒 隐私政策 - 用户数据保护和隐私政策说明  
- ⚖️ 政策与安全 - 平台规则、安全措施和社区准则  
- 🔧 工作原理 - YouTube 平台的运作机制和功能介绍  
- � 测试新功能 - 参与新功能的测试和反馈  
- © 2025 Google LLC - 版权归属和公司信息

---

### [为你的 Next.js 应用添加 Google 登录的最简单方法 ✍️ - Tom Dekan](https://tomdekan.com/articles/google-sign-in-nextjs)

**原文标题**: [The simplest way to add Google sign-in to your Next.js app ✍️ - Tom Dekan](https://tomdekan.com/articles/google-sign-in-nextjs)

本文介绍了如何在 Next.js 应用中集成 Google 登录功能，使用 Prisma ORM 和 BetterAuth 工具，从项目搭建到部署的完整流程。

- 🚀 使用 Next.js (App Router) 和 Prisma ORM 搭建项目，集成 Google 登录功能  
- 🔐 自托管认证 vs 托管认证服务，选择自托管以完全控制数据  
- 🛠️ 项目初始化：使用 create-next-app 创建项目，安装必要的依赖  
- 📦 安装 BetterAuth 和 Prisma 相关依赖，配置环境变量  
- 🗄️ 设置 PostgreSQL 数据库，创建用户和数据库  
- 🔑 获取 Google OAuth 客户端 ID 和密钥，配置到环境变量  
- 🔄 初始化 Prisma，生成客户端并连接 BetterAuth  
- 📝 创建认证处理程序和客户端包装器  
- 🖥️ 创建登录页面、登出按钮和受保护的仪表盘页面  
- 🔒 使用中间件全局保护路由，确保用户登录  
- 🎨 美化登录页面和主页，添加动画和视觉效果  
- 🚦 本地测试登录功能，确保流程正常  
- 🌐 部署到 Vercel，更新 Google OAuth 回调 URL  
- 📂 完整代码可在 GitHub 仓库 tomdekan/tom-auth-starter 获取

---

### [Docusaurus 3.8 | Docusaurus](https://docusaurus.io/blog/releases/3.8)

**原文标题**: [Docusaurus 3.8 | Docusaurus](https://docusaurus.io/blog/releases/3.8)

Docusaurus 3.8 发布，带来构建性能提升、新功能和未来标志以准备 Docusaurus 4。

- 🚀 **性能优化**：通过多项优化提升构建基础设施性能，包括两个新的 Docusaurus Faster 选项。
- 🔥 **Docusaurus Faster**：通过实验性标志大幅提升构建速度，推荐一次性开启所有选项。
- 💾 **持久缓存**：启用 Rspack 持久缓存，后续构建速度提升 2-5 倍。
- � **工作线程**：引入 Node.js 工作线程池，静态站点生成时间平均缩短 2 倍。
- 🛠 **其他优化**：包括优化开发服务器启动时间、Git 命令队列、SVG 精灵等。
- 🚩 **未来标志**：引入 Docusaurus v4 的未来标志，帮助逐步适应即将到来的重大变更。
- 🎨 **CSS 层叠层**：计划在 v4 中使用 CSS 层叠层，提供更好的 CSS 控制。
- 🔄 **postBuild() 变更**：移除遗留的 `head` 属性，为静态站点生成工作线程做准备。
- 🌐 **翻译更新**：新增土耳其语、波兰语、中文和日语的主题翻译。
- 🛠 **维护更新**：支持 Node.js 24 和 TypeScript 5.8，移除无用 npm 包。
- 📦 **其他变更**：包括 Markdown 代码块行号初始化、自定义页面标题格式化等。

---

### [Docusaurus 3.8 | Docusaurus](https://docusaurus.io/blog/releases/3.8#future-flags)

**原文标题**: [Docusaurus 3.8 | Docusaurus](https://docusaurus.io/blog/releases/3.8#future-flags)

Docusaurus 3.8 发布，带来构建性能提升、新功能和未来标志以准备 Docusaurus 4。

- 🚀 **性能优化**：通过多种优化提升构建基础设施性能，包括两个新的 Docusaurus Faster 选项。
- 🔥 **Docusaurus Faster**：通过实验性标志大幅提升构建速度，推荐一次性开启所有标志。
- 💾 **持久缓存**：启用 Rspack 持久缓存，后续构建速度提升 2-5 倍。
- � **工作线程**：引入 Node.js 工作线程池，静态站点生成时间平均缩短 2 倍。
- 🛠 **其他优化**：包括优化 macOS 开发服务器启动时间、Git 命令队列、SVG 精灵等。
- 📊 **效果**：React Native 和 Docusaurus 官网构建时间显著缩短，冷构建和热重建均有大幅提升。
- 🚩 **未来标志**：引入 Docusaurus v4 未来标志，帮助逐步适应即将到来的重大变更。
- 🎨 **CSS 层叠**：计划在 v4 中使用 CSS 层叠，提供更好的 CSS 控制。
- 🔄 **postBuild 变更**：移除遗留的 `head` 属性，对现有插件影响极小。
- 🌐 **系统颜色模式**：经典主题支持恢复为系统/OS 颜色模式。
- 📜 **代码块重构**：主题代码块组件重构，更易于扩展和定制。
- 🌍 **翻译更新**：新增土耳其语、波兰语、中文和日语的主题翻译。
- 🛠 **维护更新**：支持 Node.js 24 和 TypeScript 5.8，移除无用 npm 包，内部化未维护的包。
- 📝 **其他变更**：包括文档版本下拉菜单支持 `versions` 属性、支持 Bun 标签转换等。

---

### [ReactJust](https://reactjust.dev/)

**原文标题**: [ReactJust](https://reactjust.dev/)

专注于 React 本身，不引入额外抽象、内置功能或强制路由，自由选择工具和模式。

- ⚛️ 仅使用 React 核心功能，避免不必要的抽象  
- 🛠️ 不强制内置功能，保持灵活性  
- 🚫 无预设路由限制，自由选择路由方案  
- 🔧 支持开发者按偏好选用工具与设计模式

---

### [SaaS 应用全教程 2025 | 7 天内用 Next JS、Supabase 和支付功能发布你的 SaaS 应用 - YouTube](https://www.youtube.com/watch?v=XUkNR-JfHwo&utm_source=cooper-press&utm_medium=newsletter&utm_campaign=jsm-saas&utm_content=05-28-25&dub_id=4Q23jUrNPo31FHXC)

**原文标题**: [SaaS App Full Course 2025 | Launch Your SaaS in Under 7 Days with Next JS, Supabase & Payments - YouTube](https://www.youtube.com/watch?v=XUkNR-JfHwo&utm_source=cooper-press&utm_medium=newsletter&utm_campaign=jsm-saas&utm_content=05-28-25&dub_id=4Q23jUrNPo31FHXC)

这是一个关于 YouTube 平台相关信息和政策的页面，涵盖了多个方面的内容。

- 📢 关于 YouTube 的基本信息和背景  
- 📰 新闻和媒体相关资讯  
- ©️ 版权信息和政策  
- 📞 联系方式和用户支持  
- 🎨 内容创作者的相关资源  
- 💼 广告和商业合作机会  
- 💻 开发者工具和资源  
- 📜 使用条款和条件  
- 🔒 隐私政策和数据保护  
- ⚖️ 平台政策与安全指南  
- 🔧 YouTube 功能运作机制  
- 🧪 新功能的测试与更新  
- © 2025 Google LLC 版权归属声明

---

### [摇滚包](https://alexsergey.github.io/rockpack/)

**原文标题**: [Rockpack](https://alexsergey.github.io/rockpack/)

Rockpack 是一个轻量级、零配置的解决方案，能快速搭建支持服务端渲染（SSR）、打包、代码检查和测试的 React 应用。5 分钟内即可启动一个现代化、性能优化的 React 项目，适合希望跳过配置直接开发的开发者。

- 🚀 **快速 SSR**：无缝集成服务端渲染，提升 SEO 和首屏加载速度。  
- 📦 **智能打包**：开箱即用的高性能打包支持。  
- ✨ **自动代码检查**：内置代码质量和风格检查。  
- � **测试就绪**：预置 Jest 等流行测试工具。  
- ⚡ **零配置**：极简设置，立即开始开发。  
- 🔗 **集成 React/SSR/Webpack**：一站式高效开发方案。  
- � **生产优化**：遵循最佳实践进行打包、检查和渲染。  
- 🔧 **可扩展**：轻松定制高级需求。  
- 🛠️ **快速入门**：通过 `@rockpack/starter` 模块创建应用骨架，支持多种类型（如 SPA、SSR、纯 React 项目等）。  
  - 安装：`npm i @rockpack/starter -g`  
  - 创建：`rockpack <项目名>`  
  - 选择应用类型和模块（MIT 许可证）。

---

### [GitHub - AlexSergey/rockpack: Rockpack 是一个轻量级、零配置的解决方案，用于快速搭建支持服务器端渲染（SSR）、打包、代码检查和测试的 React 应用。](https://github.com/AlexSergey/rockpack)

**原文标题**: [GitHub - AlexSergey/rockpack: Rockpack is a lightweight, zero-configuration solution for quickly setting up a React application with full support for Server-Side Rendering (SSR), bundling, linting, and testing.](https://github.com/AlexSergey/rockpack)

Rockpack 是一个轻量级、零配置的解决方案，用于快速搭建支持服务端渲染（SSR）、打包、代码检查和测试的 React 应用。它提供了模块化的功能，适合从新手到大型项目的各种需求。

- 🚀 **快速启动**：5 分钟内即可搭建一个现代化的 React 应用，支持 SSR、打包、代码检查和测试。
- ⚡ **零配置**：开箱即用，无需复杂设置，适合快速验证想法或开发项目。
- 🔧 **模块化设计**：支持按需使用，适用于遗留项目或特定功能需求。
- 📦 **功能丰富**：支持多种文件格式导入、图像优化、CSS/SCSS/Less 模块、TypeScript 和 Babel 等。
- 🛠 **工具集成**：内置 Webpack、Jest 和 ESLint，提供最佳实践配置。
- 🔄 **SSR 支持**：通过 `iSSR` 模块轻松实现服务端渲染，优化 SEO 和加载性能。
- 📚 **多种应用类型**：支持 SPA、SSR、React 组件和 UMD 库的快速搭建。
- 🔍 **灵活扩展**：可自定义配置，适合不同规模和复杂度的项目。
- 📜 **MIT 许可**：完全免费，欢迎贡献和协作。

---

### [GitHub - xxsnakerxx/react-native-alert-queue: 基于 Promise、队列化且完全可定制的 React Native 提示框](https://github.com/xxsnakerxx/react-native-alert-queue)

**原文标题**: [GitHub - xxsnakerxx/react-native-alert-queue: Promise-based, queued and fully customizable Alert for React Native.](https://github.com/xxsnakerxx/react-native-alert-queue)

这是一个名为 `react-native-alert-queue` 的 React Native 库，提供了基于 Promise 的、可队列化和完全可定制的 Alert 功能。

- 🚀 **核心功能**：支持异步/等待（`async/await`）使用，提供顺序 Alert 队列管理。
- 🎨 **UI 定制**：允许动态更新 Alert 的标题、消息、按钮等，支持 SVG 图标和自定义渲染器。
- 🎉 **特效支持**：内置庆祝效果的彩色纸屑（Confetti）动画。
- 🌐 **跨平台**：支持 React Native Web。
- ⚙️ **配置灵活**：提供全局样式和行为配置，支持自定义辅助函数和实时更新。
- 📦 **安装简单**：通过 npm 或 yarn 安装，需要 `react-native-reanimated 3.x` 作为依赖。
- 📚 **丰富文档**：包含详细的 API 参考、示例应用和贡献指南。
- 🔄 **高级特性**：支持自定义按钮属性、插槽（Slots）内容注入和异步操作管理。
- 📜 **开源协议**：采用 MIT 许可证发布。

---

### [React 日期选择组件 | React DayPicker](https://daypicker.dev/)

**原文标题**: [Date Picker Component for React | React DayPicker](https://daypicker.dev/)

React DayPicker 是一个用于创建日期选择器、日历和日期输入功能的 React 组件，适用于各种 Web 应用场景。

- 🛠 提供丰富的属性选项，支持高度自定义日历功能  
- 🎨 设计简洁，易于通过 CSS 或 CSS 框架进行样式定制  
- 📅 支持多种日期选择模式：单日、多日、日期范围及自定义选择  
- 🌍 支持多语言本地化和时区设置  
- 🌐 兼容 ISO 8601、波斯和广播日历格式  
- 🦮 符合 WCAG 2.1 AA 无障碍标准  
- ⚙️ 可自定义组件以扩展渲染元素  
- 🔤 轻松与输入字段集成  
- 📦 基于 TypeScript 开发，依赖 date-fns 进行日期处理和格式化  
- ⚛️ 兼容 React 16.8 及以上版本  
- 📜 采用 MIT 许可证开源  
- 💬 提供社区支持：讨论论坛和问题反馈渠道  
- 🪳 支持用户报告问题和提出功能请求  
- 🎗️ 可通过 GitHub 赞助项目维护者

---

### [GitHub - pmndrs/react-spring: ✌️ 基于弹簧物理的 React 动画库](https://github.com/pmndrs/react-spring)

**原文标题**: [GitHub - pmndrs/react-spring: ✌️ A spring physics based React animation library](https://github.com/pmndrs/react-spring)

react-spring 是一个基于弹簧物理原理的 React 动画库，支持跨平台使用，提供灵活的工具来实现各种动画效果。

- ✌️ **核心特点**：基于弹簧物理原理的动画库，提供流畅的交互体验。  
- 🌍 **跨平台支持**：兼容 react-dom、react-native、react-three-fiber、react-konva 和 react-zdog。  
- 🛠️ **灵活使用**：支持声明式或命令式动画编写方式。  
- 🚀 **快速上手**：通过简单的 `useSpring` 钩子即可实现动画效果。  
- 📚 **丰富文档**：提供详细文档和示例，方便学习和使用。  
- ⭐ **受欢迎程度**：拥有 28.7k 星标，被 183k+ 项目使用。  
- 🤝 **社区支持**：由 181+ 贡献者共同维护，支持 OpenCollective 赞助。  
- 📜 **开源许可**：采用 MIT 许可证，可自由使用和修改。

---

### [GitHub - gregberge/react-teleporter: 在同一 React 树中传送组件 📡](https://github.com/gregberge/react-teleporter)

**原文标题**: [GitHub - gregberge/react-teleporter: Teleport React components in the same React tree 📡](https://github.com/gregberge/react-teleporter)

react-teleporter 是一个用于在同一 React 树中传送组件的库，允许在复杂应用中灵活配置组件位置。

- 📡 主要功能：通过 `createTeleporter` 创建传送器，实现组件从 `Source` 到 `Target` 的动态传送。
- 🛠️ 示例用法：在 `Header` 中定义 `Target`，在 `Page` 中通过 `Source` 传送内容（如“Loading...”）。
- 🔄 多源支持：通过 `{ multiSources: true }` 选项允许多个 `Source` 注入到同一 `Target`。
- 🎯 自定义目标：使用 `useTargetRef` 创建自定义目标引用，支持更灵活的 DOM 元素控制。
- 📝 动态属性：`Target` 支持 `as` 属性修改标签类型，并支持所有属性透传。
- ⚙️ 高级用法：支持子组件为函数，可访问 `Target` 元素并触发事件（如 `dispatchEvent`）。
- 📦 开源信息：MIT 许可证，1.1k Stars，19 Forks，支持 TypeScript 和 JavaScript。

---

### [发布 4.0.0-beta.4 版 · software-mansion/react-native-reanimated · GitHub](https://github.com/software-mansion/react-native-reanimated/releases/tag/4.0.0-beta.4)

**原文标题**: [Release 4.0.0-beta.4 · software-mansion/react-native-reanimated · GitHub](https://github.com/software-mansion/react-native-reanimated/releases/tag/4.0.0-beta.4)

react-native-reanimated 4.0.0-beta.4 版本发布，包含多项功能改进、错误修复和依赖更新。

- 🛠️ 修复了 Web 平台上的 `cancelAnimation` 和 `boxShadow` 问题  
- 📱 支持 React Native 0.79 和 0.80 版本  
- 🧪 新增 Jest 动画属性测试支持  
- 🎨 改进布局动画和颜色处理逻辑  
- 🔧 优化工作流和静态检查工具  
- 📚 更新文档和兼容性表格  
- 🚀 发布 react-native-worklets 0.3.0 版本  
- 🐛 修复了传感器、CSS 动画和样式更新的多个问题  
- 🌟 新增 2 位贡献者，共 18 位开发者参与此版本

---

### [2025 年 5 月 19 日发布——React Spectrum 版本更新](https://react-spectrum.adobe.com/releases/2025-05-19.html)

**原文标题**: [May 19, 2025 Release â React Spectrum Releases](https://react-spectrum.adobe.com/releases/2025-05-19.html)

2025 年 5 月 19 日发布的版本包含多项功能增强、性能优化和问题修复，涵盖键盘可访问性、React 19 兼容性、TypeScript 支持等，并感谢社区贡献。

- 🚀 新增 `moveBefore` 和 `moveAfter` 方法至 `useTreeData`  
- 🎯 为集合组件添加 `shouldSelectOnPressUp` 属性  
- 🖥️ 在 `DialogTrigger` 中为 `Popover` 增加 `--trigger-width` 支持  
- 🔘 优化 `TagGroup` 键盘可访问性，支持 Tab 切换至删除按钮  
- ⚛️ 支持 React 19 的 ref 清理回调行为  
- 📊 提升动态表格列更新的稳定性  
- ⚡ 优化 React 过渡中的集合更新性能  
- 🚫 修复禁用集合项点击时获取焦点的问题  
- 📅 为 `Calendar` 添加 `aria-details` 支持  
- 🔄 修复 `@internationalized/date` 循环依赖  
- 📜 改进 TypeScript 类型兼容性（支持旧版 `@types/react`）  
- 👆 提升可按压元素的 `touch-action` 样式性能  
- 🛠️ 修复 SSR 中的 `document is not defined` 错误  
- 📚 文档修正（默认占位符、拼写错误等）  
- 📦 发布多版本包（如 `@adobe/react-spectrum@3.42.0` 等）

---

### [ESLint v9.27.0 发布 - ESLint - 可插拔的 JavaScript 代码检查工具](https://eslint.org/blog/2025/05/eslint-v9.27.0-released/)

**原文标题**: [ESLint v9.27.0 released - ESLint - Pluggable JavaScript Linter](https://eslint.org/blog/2025/05/eslint-v9.27.0-released/)

ESLint v9.27.0 是一个小版本升级，引入了新功能并修复了之前版本中的多个错误。主要更新包括将 MCP 服务器分离为独立包、新增环境变量设置功能标志、规则改进及 TypeScript 语法支持增强等。

- 🚀 **MCP 服务器独立包**：ESLint MCP 服务器从核心中分离为 `@eslint/mcp` 包，减少依赖数量和大小，原有 CLI 标志 `--mcp` 仍兼容。  
- 🌍 **环境变量功能标志**：新增 `ESLINT_FLAGS` 环境变量，便于在 CI/CD 或跨命令中统一启用功能标志。  
- 🔍 **新增规则 `no-unassigned-vars`**：检测未赋值但被读取的 `let`/`var` 变量，避免潜在错误。  
- 🔧 **规则优化**：  
  - `no-useless-escape` 新增 `allowRegexCharacters` 选项，允许正则中特定字符的冗余转义。  
  - `no-array-constructor` 支持自动修复（`--fix`）。  
- 💻 **TypeScript 支持增强**：核心规则 `max-params` 和 `no-unassigned-vars` 新增对 TypeScript 语法的完整支持。  
- 🐞 **Bug 修复**：包括类型定义修正、配置文件键排序（减少 Git 差异）等。  
- 📚 **文档更新**：补充 TypeScript 相关说明、编辑器集成（如 Neovim）及配置示例优化。  
- 🔄 **依赖升级与重构**：更新多项目依赖，优化内部工具链（如测试环境适配 Node.js 24）。

---

### [JavaScript 简史 | Deno](https://deno.com/blog/history-of-javascript)

**原文标题**: [A brief history of JavaScript | Deno](https://deno.com/blog/history-of-javascript)

JavaScript 诞生 30 周年，从诞生之初的简陋脚本语言发展为全球最流行的编程语言，深刻影响了现代 Web 开发。以下是其发展历程中的关键节点：

- 🚀 **1994 年 12 月**：Netscape 发布 Netscape Navigator 1.0 浏览器，为 JavaScript 的诞生奠定基础  
- 💡 **1995 年 5 月**：Brendan Eich 用 10 天设计出 JavaScript，初衷是为网页添加交互性  
- ⚔️ **1996 年 3 月**：微软推出 JScript 与 Netscape 竞争，引发浏览器脚本语言分裂  
- 🌐 **1997 年 6 月**：JavaScript 提交 ECMA 国际标准化，形成 ECMAScript 规范  
- 🔓 **1998 年 1 月**：Netscape 开源浏览器代码，催生 Mozilla 项目和未来 Firefox  
- 📜 **1999 年 12 月**：ECMAScript 3 发布，新增正则表达式、异常处理等核心功能  
- 🔄 **2004 年 4 月**：Gmail 采用 AJAX 技术，开启 Web 2.0 时代  
- 🛠️ **2006 年 3 月**：jQuery 诞生，解决跨浏览器兼容性问题  
- 🚀 **2008 年 9 月**：Google 发布 Chrome 浏览器及 V8 引擎，大幅提升 JS 执行速度  
- 💻 **2009 年 3 月**：Ryan Dahl 创建 Node.js，使 JS 突破浏览器限制  
- 📦 **2010 年 1 月**：npm 1.0 发布，彻底改变 JS 代码共享方式  
- ⚛️ **2013 年 5 月**：Facebook 开源 React，推动声明式 UI 范式革新  
- 🦕 **2018 年 6 月**：Ryan Dahl 预告 Deno 项目，反思 Node.js 设计缺陷  
- 🧩 **2019 年 4 月**：Node.js 实验性支持 ES 模块，逐步统一模块系统  
- 🚀 **2020 年 5 月**：Deno 1.0 发布，内置 TypeScript 和安全权限模型  
- 🐢 **2024 年 2 月**：Node.js 选定火箭龟 (Rocket Turtle) 作为官方吉祥物  
- ⚖️ **2024 年 9 月**：Deno 发起#FreeJavaScript 运动，挑战 Oracle 对 JS 商标的所有权  
- 🤖 **2025 年 3 月**：TypeScript 宣布将用 Go 语言重写以提升性能  

JavaScript 已从简单的网页脚本发展为全栈开发的核心语言，涵盖前端、后端、移动应用甚至太空任务。其成功源于开源社区的持续创新和对技术标准的不断突破。

---

### [JavaScript 框架入门 - YouTube](https://www.youtube.com/watch?v=DAci3O2j31o)

**原文标题**: [Introduction to JavaScript Frameworks - YouTube](https://www.youtube.com/watch?v=DAci3O2j31o)

YouTube 平台相关信息概览  

- 📢 关于我们 - 介绍 YouTube 的背景与宗旨  
- 📰 新闻动态 - 提供最新媒体资讯与公告  
- ©️ 版权信息 - 明确平台内容版权归属  
- 📩 联系我们 - 用户与平台沟通渠道  
- 🎨 创作者资源 - 支持内容创作者的相关服务  
- 💼 广告合作 - 广告投放与商业合作信息  
- 💻 开发者工具 - 开放 API 与技术资源  
- 📜 使用条款 - 平台服务协议与规范  
- 🔒 隐私政策 - 用户数据保护条款  
- ⚖️ 政策与安全 - 内容审核与社区准则  
- 🔧 功能测试 - 新特性实验与用户体验优化  
- ®️ 商标声明 - 谷歌公司 2025 版权标识

---

### [GitHub - googleapis/js-genai：适用于Gemini和Vertex AI 的 TypeScript/JavaScript SDK](https://github.com/googleapis/js-genai)

**原文标题**: [GitHub - googleapis/js-genai: TypeScript/JavaScript SDK for Gemini and Vertex AI.](https://github.com/googleapis/js-genai)

Google Gen AI SDK 是一个为 TypeScript 和 JavaScript 开发者设计的工具包，用于构建基于 Gemini 的应用程序，支持 Gemini Developer API 和 Vertex AI。该 SDK 提供了多种功能，包括模型调用、缓存管理、聊天会话、文件上传和实时交互等。

- 🚀 **项目信息**  
  - 公开仓库，621 stars，70 forks，Apache-2.0 许可证  
  - 支持 TypeScript/JavaScript，适用于 Gemini 和 Vertex AI  

- 🔑 **安全提示**  
  - 避免在客户端代码中暴露 API 密钥，生产环境建议使用服务端实现  

- 📦 **安装与初始化**  
  - 通过 `npm install @google/genai` 安装  
  - 支持通过 API 密钥（Google AI Studio）或 Vertex AI 配置初始化  

- ⚡ **核心功能**  
  - 支持模型调用（如 `generateContent`）、流式响应（`generateContentStream`）  
  - 提供缓存、聊天会话、文件上传和实时交互模块  
  - 支持函数调用（Function Calling）以实现外部系统交互  

- 🌐 **API 版本控制**  
  - 默认使用 beta API 端点，可手动切换至稳定版本（如 `v1` 或 `v1alpha`）  

- 📂 **示例与文档**  
  - 提供快速入门代码和 GitHub 示例目录  
  - 详细文档见 [googleapis.github.io/js-genai/](https://googleapis.github.io/js-genai/)  

- 🔄 **与其他 SDK 的区别**  
  - 这是 Google Deepmind 的官方 SDK，优先支持 Gemini 2.0+ 新特性  
  - 旧版 SDK（如 `@google/generative_language`）不再接收新功能更新  

- 📊 **项目活跃度**  
  - 22 位贡献者，9.4k+ 项目使用，最新版本发布于 2025 年 5 月

---

### [10 倍速 TypeScript - TypeScript](https://devblogs.microsoft.com/typescript/typescript-native-port/)

**原文标题**: [A 10x Faster TypeScript - TypeScript](https://devblogs.microsoft.com/typescript/typescript-native-port/)

TypeScript 团队宣布将推出原生版本的 TypeScript 编译器，预计性能提升 10 倍，大幅减少编辑器启动和构建时间，并降低内存使用。  

- 🚀 TypeScript 将推出原生编译器，性能提升高达 10 倍，大幅优化大型代码库的加载和检查速度。  
- ⏱️ 实测多个流行项目（如 VS Code、Playwright）的构建时间显著缩短，部分项目提速超过 10 倍。  
- 💻 编辑器体验大幅改善，项目加载时间减少 8 倍，语言服务操作（如代码补全、跳转定义）响应更快。  
- 📉 内存占用降低约 50%，未来可能进一步优化。  
- 🔧 原生版本计划 2025 年中发布预览版，年底前实现完整功能支持。  
- 📜 采用 Go 语言重写，代码库开源，开发者可提前测试。  
- 🔄 未来版本规划：TypeScript 6.x 仍基于 JS，TypeScript 7.0 将作为原生版本发布，两者将并行维护。  
- 🤖 性能提升为 AI 工具提供更高效的代码分析能力，支持更复杂的重构和错误检测。  
- ❓ 团队将在 GitHub 和 Discord 社区解答疑问，并持续更新进展。

---

### [宣布 TypeScript 原生预览版 - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-native-previews/)

**原文标题**: [Announcing TypeScript Native Previews - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-native-previews/)

TypeScript 宣布推出原生预览版，通过 Go 语言重写编译器，实现了 10 倍以上的性能提升，并支持共享内存并行和并发处理。开发者可通过 npm 安装预览版编译器，VS Code 用户也可通过扩展市场获取编辑器功能预览。尽管仍有一些功能缺失，团队将持续更新并计划将其作为 TypeScript 7 发布。

- 🚀 TypeScript 原生预览版发布，性能提升 10 倍以上  
- 🔧 通过 npm 安装预览版编译器：`npm install -D @typescript/native-preview`  
- 📝 VS Code 扩展支持预览，需手动启用实验性功能  
- ⏳ 目前缺失部分功能，如 `--build` 模式和自动导入等  
- 🔍 已支持 JSX 和 JavaScript+JSDoc 类型检查  
- 📅 计划作为 TypeScript 7 发布，未来将支持更多功能

---

