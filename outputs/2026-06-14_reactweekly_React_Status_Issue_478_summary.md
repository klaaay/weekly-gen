### [2026 年 React 库指南 - Robin Wieruch](https://www.robinwieruch.de/react-libraries/)

**原文标题**: [React Libraries for 2026 - Robin Wieruch](https://www.robinwieruch.de/react-libraries/)

### 概述摘要
React 生态系统在 2026 年已高度成熟，开发者可根据项目需求灵活选择库和工具，从轻量级客户端应用到全栈服务端渲染方案均有成熟推荐。

- 📦 **项目启动**：Vite 是客户端渲染首选，Next.js/TanStack Start 用于全栈应用，Astro 适合静态站点；React Compiler v1.0 已自动优化性能
- 🧰 **包管理**：npm 最普及，pnpm 高效，Bun 作为一体化工具链增长迅速；Turborepo/Nx 用于 Monorepo 管理
- 🗂️ **状态管理**：useState/useReducer 处理局部状态，Zustand 成全局状态新标准；TanStack Query 负责远程数据缓存
- 🌐 **数据获取**：TanStack Query（REST/GraphQL）、tRPC（端到端类型安全）、RSC/RSF（服务端数据获取）
- 🧭 **路由**：React Router v7 支持库/框架双模式，TanStack Router 以类型安全著称
- 🎨 **样式方案**：Tailwind CSS v4 成行业标准，CSS Modules 用于封装，PandaCSS/vanilla-extract 替代运行时 CSS-in-JS
- 🧩 **UI 库**：shadcn/ui（无头组件+Tailwind）成主流，Mantine v8/Material UI 仍广泛使用
- ⚡ **动画与图表**：Motion（动画）、Recharts（图表）、D3（底层可视化）
- 📝 **表单与验证**：React Hook Form + Zod 最流行，TanStack Form/Conform针对不同场景
- 🔒 **认证**：Better Auth 开源首选，Clerk/Kinde 付费方案，Supabase Auth 集成便捷
- 🖥️ **后端与数据库**：Hono/Express 用于后端，Drizzle ORM 成数据库层新宠，Supabase/Neon/Turso 为流行数据库
- 🚀 **部署**：Vercel（Next.js 最优）、Netlify、Coolify（自托管）、Cloudflare（边缘计算）
- 🧪 **测试**：Vitest + React Testing Library（单元/集成），Playwright（端到端）
- 🌍 **国际化**：react-i18next 通用，next-intl 专为 Next.js，Paraglide JS 编译时优化
- 📧 **邮件与支付**：react-email（邮件模板），Stripe/Paddle（支付），Polar.sh（开源 MoR）
- 📱 **跨平台**：Expo（React Native 框架），Tauri（桌面应用），Tamagui（Web/移动统一组件）
- 🎯 **其他**：Temporal API（日期处理）、Tiptap（富文本编辑器）、Storybook（组件文档）、v0（AI 原型生成）

---

### [Meticulous AI - 无需编写测试的自动化前端测试](https://www.meticulous.ai/?utm_source=reactstatus&utm_medium=newsletter&utm_campaign=26q2&utm_content=primary)

**原文标题**: [Meticulous AI - Automated Frontend Testing Without Writing Tests](https://www.meticulous.ai/?utm_source=reactstatus&utm_medium=newsletter&utm_campaign=26q2&utm_content=primary)

Meticulous 是一款零开发工作量的自动化测试工具，能全面、确定性地验证代码，帮助团队以 AI 编写代码的速度安全交付，深受 Dropbox、Notion 等企业信赖。

- 🚀 **零开发工作量**：无需编写、修复或维护测试，测试套件随应用自动演进。
- 🎯 **全面且确定性**：从 Chromium 底层构建确定性调度引擎，彻底消除测试不稳定（flakes），实现闪电般快速测试。
- 🤖 **AI 驱动测试生成**：通过记录开发中的交互，AI 引擎自动生成覆盖所有代码分支和边缘用例的测试套件。
- 🔍 **PR 影响预览**：提交 PR 时即可查看对用户工作流的影响，通过模拟后端响应避免假阳性，无需特殊测试账号。
- ⚡ **极速规模化测试**：测试在计算集群上高度并行化，可测试数千个屏幕并在 120 秒内获得结果。
- 🔗 **灵活集成**：支持 NextJS、React、Vue、Angular、Nuxt、SvelteKit 等主流框架，可补充或替代现有测试套件。
- 🏢 **企业级信任**：被超过 100 家组织（包括 Dropbox、Notion 等）采用，工程师反馈“无法想象没有它的工作”。

---

### [React 基础](https://react.foundation/)

**原文标题**: [React Foundation](https://react.foundation/)

概述总结
React 基金会是一个社区驱动的透明组织，致力于通过代码贡献、教育支持和资金资助来维护和发展 React 生态系统。

- 🌐 社区驱动：React 基金会以社区为核心，鼓励开发者通过代码、教学、组织活动等方式参与，共同构建 React 的未来。
- 🔍 100% 透明：基金会承诺完全透明，所有决策和资金使用公开，确保社区信任。
- 💰 资助维护者：通过多渠道（如代码贡献、赞助）直接为维护 React 生态库的开发者提供财务支持。
- 📚 教育与资源：提供教程、文档和研讨会，帮助开发者掌握 React 及相关工具，降低学习门槛。
- 🌍 全球可访问性：确保 React 对全球开发者开放包容，无论其背景或资源如何，促进公平参与。
- 🤝 贡献途径：支持多种参与方式，包括提交代码、组织社区、创建教育内容或财务捐赠，共同强化生态系统。
- 🛒 商店支持：通过购买商品或直接捐赠，为维护者、教育和可访问性倡议提供资金。
- 🏆 成为会员：正式会员可参与资金决策投票，获取独家更新和社区认可，助力 React 可持续发展。

---

### [React 基金会：由 Linux 基金会托管的 React 新家 – React](https://react.dev/blog/2026/02/24/the-react-foundation)

**原文标题**: [The React Foundation: A New Home for React Hosted by the Linux Foundation – React](https://react.dev/blog/2026/02/24/the-react-foundation)

### 概述摘要
React 基金会正式成立，由 Linux 基金会托管，React、React Native 及相关项目所有权从 Meta 转移至该基金会。

- 🏢 **独立托管**：React 基金会由 Linux 基金会托管，React、React Native 和 JSX 等项目不再归 Meta 所有。
- 🤝 **创始成员**：八家白金创始成员包括 Amazon、Callstack、Expo、华为、Meta、Microsoft、Software Mansion 和 Vercel，华为为新加入成员。
- 🧑‍💼 **治理结构**：董事会由各成员代表组成，Seth Webster 担任执行董事；技术治理独立于董事会，由贡献者和维护者决定方向。
- ⏳ **临时领导委员会**：已成立临时领导委员会，负责制定技术治理结构，后续将公布更多细节。
- 📋 **下一步计划**：包括完成技术治理结构、转移仓库和网站、支持 React 生态项目、筹备下一届 React Conf。
- 🙏 **感谢社区**：感谢数千名贡献者、创始成员及数百万开发者，基金会因社区而存在，共同构建未来。

---

### [GitHub - react/react：用于Web和原生用户界面的库 · GitHub](https://github.com/react/react)

**原文标题**: [GitHub - react/react: The library for web and native user interfaces. · GitHub](https://github.com/react/react)

React 是一个用于构建用户界面的 JavaScript 库，支持声明式、组件化和跨平台开发，拥有 246k 星标和 51.1k 分支，采用 MIT 许可证。

- 📚 React 是一个用于构建用户界面的 JavaScript 库，强调声明式编程，使代码更可预测、易调试
- 🧩 基于组件的架构：封装独立组件管理自身状态，通过组合构建复杂界面，逻辑用 JavaScript 而非模板编写
- 🌍 学习一次，随处编写：不依赖特定技术栈，可与现有代码共存，支持服务器端渲染（Node）和移动端（React Native）
- ⚡ 渐进式采用：可从快速入门、添加到现有项目或创建新应用开始，灵活使用
- 📖 文档丰富：包括快速入门、教程、思考 React、安装、描述 UI、添加交互、管理状态等章节
- 💻 示例代码展示：使用 JSX 语法（非必需但推荐），如`<HelloMessage name="Taylor"/>`渲染“Hello Taylor”
- 🤝 开源贡献：主要目的是持续优化 React 核心，欢迎社区提交 bug 修复和改进
- 📜 行为准则：采用 Facebook 行为准则，要求参与者遵守
- 🛠️ 贡献指南：提供开发流程、如何提出修复和改进、构建测试方法
- 🌟 新手友好：有“good first issues”列表，适合初学者参与
- 📄 许可证：MIT 许可证，开源免费使用
- 📊 仓库活跃：246k 星标、51.1k 分支、129 个发布版本（最新 19.2.7 于 2026 年 6 月 1 日）
- 🔧 技术栈：JavaScript（49.4%）、Rust（25.9%）、TypeScript（22.6%）等

---

### [TanStack AI Beta：AI 工具界的瑞士军刀成长记 | TanStack 博客](https://tanstack.com/blog/tanstack-ai-beta)

**原文标题**: [TanStack AI Beta: The Switzerland of AI Tooling Grows Up | TanStack Blog](https://tanstack.com/blog/tanstack-ai-beta)

TanStack AI 已进入 Beta 阶段，这是一个框架无关、供应商无关的 AI 工具包，提供稳定、多模态、类型安全的开发体验。

- 🚀 **Beta 意味着稳定**：核心 API 已稳定，协议已文档化，测试基础设施完善，可以用于构建真实产品。
- 🎨 **统一 API 覆盖所有模态**：文本、图像、视频、音频、语音聊天等模态都通过相同的 `chat()`、`generateAudio()` 等函数调用，切换供应商只需更改导入的适配器。
- 🛡️ **按模型类型安全**：每个模型和供应商的选项都在类型层面进行约束，IDE 能准确提示，不兼容的工具会在编译时报错。
- 🧩 **构建真实系统**：提供中间件、延迟工具发现、代码执行沙箱、MCP 支持以及实验性的编排功能，帮助管理生产级 AI 应用的复杂性。
- 🌐 **TypeScript 优先，开放协议**：基于 AG-UI 协议，支持多种传输方式（HTTP、WebSocket），可与任何语言的后端（如 Kotlin、Python）互操作，前端支持 React、Vue、Svelte 等。
- 🔍 **可调试性**：提供可插拔的调试日志和基于 TanStack Devtools 的同构开发者工具，可清晰查看 LLM 的每一步操作。
- ✅ **经过严格测试**：每个 PR 都会在 10 个 LLM 供应商上运行 265 个端到端测试，确保可靠性。
- 💡 **保持开源与诚实**：无供应商锁定，无平台迁移要求，提供与 Vercel AI SDK 的客观对比。

---

### [TanStack Table V9：表单化 | TanStack 博客](https://tanstack.com/blog/tanstack-table-v9-taking-form)

**原文标题**: [TanStack Table V9: Taking Form | TanStack Blog](https://tanstack.com/blog/tanstack-table-v9-taking-form)

TanStack Table V9 Beta 正式发布，带来了多项重大改进，解决了 V8 中的核心问题，并提升了性能、可扩展性和开发者体验。

- 🎉 TanStack Table V9 Beta 发布，经过多年开发，终于接近完成
- 🔧 状态管理改用 TanStack Store，兼容 React Compiler，支持原子状态和选择器订阅，减少不必要的重新渲染
- ⚡ 内存和性能优化：大型虚拟化表格内存使用更少，通过共享原型和缓存计算提升效率
- 🌳 功能可摇树优化：按需注册功能（如排序、分页），减少打包体积，TypeScript 类型安全
- 🧩 自定义功能扩展：提供与内置功能相同的扩展模型，便于创建可复用的表格组件
- 🔄 可复用表格代码：新增 `createTableHook`，支持一次定义通用配置和组件，跨文件复用
- 🛠️ 开发者工具：集成 TanStack Devtools，支持实时检查表格状态和衍生数据
- 📚 提供完整迁移指南和大量示例（React、Angular、Vue 等框架的 Kitchen Sink 示例）

---

### [RFC: 支持使用 disposable 作为 useEffect 清理函数，作者：remcohaszing · 拉取请求 #278 · reactjs/rfcs · GitHub](https://github.com/reactjs/rfcs/pull/278)

**原文标题**: [RFC: support using disposable as useEffect cleanup by remcohaszing · Pull Request #278 · reactjs/rfcs · GitHub](https://github.com/reactjs/rfcs/pull/278)

React 的 RFC #278 提出允许在 useEffect 和 useLayoutEffect 中返回 disposable 对象，替代传统的回调函数进行清理操作。

- 📝 核心提案：允许 useEffect 和 useLayoutEffect 返回 disposable 对象（具有 Symbol.dispose 方法的对象）作为清理函数
- 💡 基本示例：通过返回 `{ [Symbol.dispose]() { console.log('Disposed!') } }` 实现清理逻辑
- 🔄 替代方案：提供比传统回调函数更简洁、更符合资源管理模式的清理方式
- 👍 社区反响：获得 18 个赞、4 个爱心和 4 个关注表情，显示一定关注度
- 🔧 当前状态：Pull Request #278 处于开放状态，尚未合并到主分支
- 👥 参与者：由 remcohaszing 提交，暂无指定审核人或分配者

---

### [发布 0.86.0 · react/react-native · GitHub](https://github.com/react/react-native/releases/tag/v0.86.0)

**原文标题**: [Release 0.86.0 · react/react-native · GitHub](https://github.com/react/react-native/releases/tag/v0.86.0)

React Native v0.86.0 正式发布，包含多项新功能、改进和错误修复。

- 🎯 **无障碍功能增强**：新增对 `AccessibilityInfo` 中基于 Promise 方法的测试支持，并修复了多个未解决的 Promise 问题。
- 🎨 **动画系统优化**：为动画后端添加了 Suspense 测试，并修复了 C++ 原生动画节点管理器中的 1 帧延迟问题。
- 🛠️ **开发者工具升级**：React Native DevTools 新增自定义渲染器操作跟踪，支持明/暗模式模拟，并改进了 WebSocket 连接稳定性。
- 📱 **运行时改进**：新增视图转换 API、视口大小支持，并修复了事件时间戳、性能 API 排序崩溃等问题。
- 🧩 **平台特定更新**：Android 端新增 `PlatformColor` 支持、硬件事件处理；iOS 端新增隐私清单、网络请求拦截器，并修复了 IPv6 连接问题。
- 🔒 **安全修复**：升级 `fast-xml-parser` 和 `minimatch` 依赖，修复多个 CVE 漏洞。
- ⚡ **性能与构建优化**：更新 Metro 至 ^0.84.2，缓存预构建 iOS 二进制文件，并修复了 CocoaPods 和 Hermes 的编译问题。
- 🐛 **关键错误修复**：修复了 Modal 样式、TextInput 自动大写、ScrollView 性能事件、Image 尺寸获取等大量问题。

---

### [🚀React Native Windows v0.83 正式发布！！React Native](https://devblogs.microsoft.com/react-native/%F0%9F%9A%80react-native-windows-v0-83-is-here/)

**原文标题**: [🚀React Native Windows v0.83 is here!! React Native](https://devblogs.microsoft.com/react-native/%F0%9F%9A%80react-native-windows-v0-83-is-here/)

React Native Windows v0.83 正式发布，与 React Native 0.83.4 对齐，进一步推进 Fabric 架构，带来更丰富的输入、自动化、辅助功能支持，以及新的性能测试工具和多项稳定性修复。

- 🚀 新增组件性能测试框架，可在 CI 中测量 Fabric 组件性能，及早发现回归问题
- 🖱️ 增强指针事件支持，包含 button 属性识别鼠标按键，补齐 W3C 标准事件处理器
- ♿ ChildSite 新增 AutomationOption 设置器，支持跨边界 UI 自动化与辅助功能合规
- 🔍 修复 Narrator 焦点在 XAML 岛屿边界无法跳转的问题，提升第三方模块辅助功能体验
- 🧩 Fabric 组件实现 overflow 样式，支持 italic、underline、strikethrough 等 TextInput 富文本样式
- 🔧 修复多项稳定性问题：Fabric 应用循环依赖、TextInput 选择崩溃、SHIFT+F10 上下文菜单、圆角阴影渲染、ScrollView 内文本指针事件、MSBuild 链接器 bug
- 📊 缩小与 Paper 及其他平台的特性差距，鼓励用户提交缺失属性 issue
- 🏁 更新 Gallery 应用至 0.83 版本，可在 Microsoft Store 或直接链接下载体验新功能

---

### [React Native、Hermes 字节码与 Kindle 主页 | Rincon](https://sighery.com/posts/patching-kindle-homepage/)

**原文标题**: [React Native, Hermes bytecode, and the Kindle homepage | Rincon](https://sighery.com/posts/patching-kindle-homepage/)

Kindle 主页使用 React Native 和 Hermes 字节码，可通过逆向工程修改广告内容。

- 📱 Kindle 自 5.14.2 版本起，主页应用改用 React Native 和 Hermes 字节码，取代了旧的 Java 实现
- 🔧 Hermes 字节码版本不兼容，Kindle 使用版本 84，需构建特定版本（v0.11.0）才能进行逆向
- 🛠️ 使用 hbctool 工具可反汇编和重新汇编 Hermes 字节码，支持字符串和操作码补丁
- 📝 字符串补丁简单但有限制（不能改变长度），操作码补丁更强大，可修改函数逻辑
- 🎯 通过 screenControl 工具定位 Kindle 主页广告组件，找到对应模板函数（如 Template49、Template18）
- ✅ 成功移除广告需要针对特定渲染函数打补丁，部分模板可直接修改，部分需找到对应的 render 函数
- 🤖 开发了 KPP_Patch 工具，可自动查找并修补 Kindle 主页广告，支持通过函数名或 ID 定位
- 🔍 未来可进一步探索 Hermes 字节码，为 Kindle 开发更多实用补丁

---

### [在 Next.js 中构建活动导航链接组件 | Aurora Scharff](https://aurorascharff.no/posts/building-an-active-navlink-component-in-nextjs/)

**原文标题**: [Building an Active NavLink Component in Next.js | Aurora Scharff](https://aurorascharff.no/posts/building-an-active-navlink-component-in-nextjs/)

本篇文章详细介绍了如何在 Next.js 中构建一个功能完备的 NavLink 组件，涵盖从基础实现到高级特性，包括样式切换、渲染属性、pending 状态、前缀匹配、无障碍支持、TypeScript 类型、首屏闪烁预防以及 cacheComponents 兼容性。

- 🔗 核心思路：基于 `usePathname()` 或 `useSelectedLayoutSegments()` 读取当前路由，实现链接的激活状态判断。
- 🎨 渲染属性模式：`className` 和 `children` 支持函数形式，接收 `{ isActive, isPending }`，让消费者灵活控制样式和内容。
- ⚡ 添加 pending 状态：利用 `useLinkStatus()` 在链接内部跟踪导航加载状态，并通过渲染属性暴露 `isPending`。
- 🧩 前缀匹配与精确匹配：默认支持嵌套路由前缀匹配（如 `/search` 匹配 `/search?q=react`），通过 `exact` 属性可切换到精确匹配。
- ♿ 无障碍支持：自动为激活链接添加 `aria-current="page"`，便于辅助技术识别，同时可配合 CSS 或 Tailwind 进行样式控制。
- 🛠️ TypeScript 类型：为组件添加完整类型定义，支持 `next/link` 所有属性、静态类型链接验证，并区分 `className` 与 `children` 的渲染属性签名。
- 🚫 首屏闪烁预防：通过内联脚本在 HTML 解析阶段根据 `location.pathname` 设置 `aria-current`，确保激活样式在 React 水合前就已生效。
- 📦 cacheComponents 兼容：将 `Suspense` 边界内置于组件中，使每个链接独立处理动态数据，避免整个导航被阻塞或出现布局偏移。
- 🧠 两种路由读取方式对比：`usePathname()` 直接比较 URL 字符串，简单但可能因重写导致水合不匹配；`useSelectedLayoutSegments()` 基于路由段比较，更稳定但依赖路由结构。
- ⚠️ 注意事项：函数形式的 `className` 或 `children` 不可序列化，无法在服务端组件中直接使用；若使用重写功能，建议采用 `useSelectedLayoutSegments()` 或延迟读取路径名。

---

### [最佳加载状态是无加载状态 :: jjenzz](https://jjenzz.com/best-loading-states-are-no-loading-states/)

**原文标题**: [The Best Loading States Are No Loading States :: jjenzz](https://jjenzz.com/best-loading-states-are-no-loading-states/)

### 概述总结
本文探讨如何通过路由过渡和预加载策略，从根本上减少甚至消除组件级别的加载状态，将等待逻辑提升至应用层级，从而简化开发并提升用户体验。

- 🚫 **核心问题**：现代应用过度依赖骨架屏、旋转器等加载状态，但这些 UI 只是将等待从导航前转移到了导航后，并未真正解决等待问题。
- 🌐 **历史启示**：传统网页由浏览器统一处理加载，不存在半渲染页面；SPA 虽实现即时导航，却引入了组件级加载状态的碎片化问题。
- 🛣️ **路由过渡方案**：路由器可在后台预加载数据，待数据就绪后再提交导航，从而避免导航后出现空白或加载状态，兼顾即时反馈与完整渲染。
- ⚡ **预加载策略**：利用链接悬停或进入视口等时机提前加载数据，使导航几乎瞬间完成；若仍有延迟，则使用全局加载指示器（如 GitHub 进度条）作为兜底。
- 🔍 **诊断反馈**：若导航后出现空白区域，说明预加载遗漏；延迟内容则提示数据依赖结构需优化——将空白视为调试信号而非直接添加加载状态。
- 🔄 **页面刷新处理**：刷新时使用全屏覆盖层等待所有查询完成，避免组件级加载；同时利用本地持久化（如 TanStack DB）减少首次加载后的等待。
- 🎯 **终极目标**：通过预加载和本地缓存，使加载状态成为罕见兜底而非常态，最终让加载状态变得多余，而非设计更好的加载状态。

---

### [当 React 父组件需要了解其子组件时](https://www.jayfreestone.com/writing/updating-react-parents-in-response-to-changes-in-children/)

**原文标题**: [When React parent components need to know their children](https://www.jayfreestone.com/writing/updating-react-parents-in-response-to-changes-in-children/)

概述总结  
- 🔄 React 中父组件需要了解子组件时，通常应保持线性数据流，但某些场景下可打破规则  
- 🧩 复合组件（Compound Components）中，父组件可通过遍历子组件 props 获取数据，但无法处理任意嵌套子组件  
- 🌲 React ARIA/Spectrum使用“伪DOM”Portal技术，在虚拟文档中首次渲染组件树，以获取嵌套子组件信息  
- 📄 管理`<head/>`标签时，需通过外部状态、上下文和钩子（如 Unhead 库）实现 SSR 和客户端同步  
- 🧭 已知路由树结构时，可使用 React Router 的`useMatches`钩子读取子路由元数据（如面包屑导航）  
- ⚠️ 这些方法属于例外情况，通常建议直接通过 props 传递数据

---

### [未找到标题](https://visx.airbnb.tech/)

**原文标题**: [No title found](https://visx.airbnb.tech/)

本文介绍了通过合理使用表情符号和简洁的列表格式，高效总结文章核心内容的方法。

- 📝 使用“-”符号创建简洁的要点列表，确保每一点都包含关键信息。
- 🎯 为每个要点选择合适表情符号，增强视觉吸引力和内容表达。
- 📋 在列表顶部添加无标题的概述总结，快速传达文章主旨。
- 🧠 聚焦核心内容，避免冗余，确保总结准确捕捉文章精髓。

---

### [未找到标题](https://visx.airbnb.tech/gallery)

**原文标题**: [No title found](https://visx.airbnb.tech/gallery)

概述：本文探讨了人工智能在医疗诊断中的应用，强调了其提高准确性和效率的潜力，同时指出数据隐私和算法偏见等挑战。

- 🩺 人工智能通过分析医学影像，能辅助医生更快速地识别疾病，如癌症和视网膜病变。
- 📊 机器学习模型可处理大量患者数据，帮助预测疾病风险，实现个性化治疗方案。
- 🔒 数据隐私是主要担忧，医疗数据的收集和使用需严格遵循法规，以保护患者信息。
- ⚖️ 算法偏见可能导致诊断不公，需确保训练数据多样性和模型公平性。
- 🤖 人工智能并非替代医生，而是作为工具提升诊断效率，最终决策仍由人类负责。

---

### [无](https://expo.dev/blog/best-way-to-build-a-mobile-app-that-makes-money-in-2026?utm_source=react-status&utm_medium=email&utm_campaign=33087804-React%2520to%2520Native)

**原文标题**: [None](https://expo.dev/blog/best-way-to-build-a-mobile-app-that-makes-money-in-2026?utm_source=react-status&utm_medium=email&utm_campaign=33087804-React%2520to%2520Native)

概述摘要：本文探讨了人工智能在医疗领域的应用，重点介绍了诊断辅助、药物研发和个性化治疗等方面的进展，同时指出了数据隐私和算法偏见等挑战。

- 🩺 人工智能通过分析医学影像和病历数据，显著提升了疾病诊断的准确性和效率。
- 💊 在药物研发中，AI 加速了候选药物的筛选过程，缩短了新药上市周期。
- 🧬 个性化治疗借助 AI 分析患者基因组数据，制定更精准的治疗方案。
- 🔒 数据隐私问题成为 AI 医疗应用的主要障碍，需加强法规和技术保护措施。
- ⚖️ 算法偏见可能加剧医疗不平等，需确保训练数据的多样性和公平性。

---

### [PDFSlick](https://pdfslick.dev/)

**原文标题**: [PDFSlick](https://pdfslick.dev/)

概述
PDFSlick Sync 是一项新功能，可为 PDF 文档添加实时协作能力，支持在 React、SolidJS、Svelte 和 JavaScript 应用中查看和交互 PDF。

- 🎉 宣布推出 PDFSlick Sync，为 PDF 文档带来实时协作功能
- 📄 支持在 React、SolidJS、Svelte 和 JavaScript 应用中查看和交互 PDF
- 🚀 提供多种示例应用，包括完整查看器、评论、多文档支持
- 🖼️ 包含缩略图布局、水平缩略图等视图选项
- 🔍 提供简单 PDF 查看器，支持导航和缩放功能
- ⚠️ 支持错误处理，提升应用稳定性
- © 2026 由 Vancho Stojkov 开发，Vane Kosturanov 设计 Logo

---

### [React 入门指南 - 文档](https://pdfslick.dev/docs/react)

**原文标题**: [Getting started with React - Docs](https://pdfslick.dev/docs/react)

本指南介绍了如何在 React 中快速集成 PDFSlick 库，用于显示 PDF 文档。

- 📦 **安装与导入**：通过 npm/yarn/pnpm 安装`@pdfslick/react`包，并导入`usePDFSlick()`钩子和 CSS 样式文件（如`@pdfslick/react/dist/pdf_viewer.css`）。
- 🖥️ **核心组件与钩子**：使用`usePDFSlick()`钩子，传入 PDF 文件路径和选项对象（如`singlePageViewer: true`和`scaleValue: "page-fit"`），返回`PDFSlickViewer`、`viewerRef`和`usePDFSlickStore`。
- 🔧 **视图渲染**：通过`<PDFSlickViewer>`组件和`viewerRef`渲染 PDF，结合`usePDFSlickStore`实现导航功能（如自定义`PDFNavigation`组件）。
- ⚠️ **重要提示**：CSS 样式文件需在应用入口（如`index.tsx`或`App.tsx`）中全局导入一次，确保 PDFSlick 正常显示。

---

### [GitHub - gre/bezier-easing-editor: 使用 React 和 SVG 制作的立方贝塞尔曲线编辑器 · GitHub](https://github.com/gre/bezier-easing-editor)

**原文标题**: [GitHub - gre/bezier-easing-editor: Cubic Bezier Curve editor made with React & SVG · GitHub](https://github.com/gre/bezier-easing-editor)

这是一个基于 React 和 SVG 构建的三次贝塞尔曲线编辑器开源项目。

- 📦 可通过 npm 安装 `bezier-easing-editor`，支持 React 17+ 和 TypeScript
- 🎮 提供受控（value + onChange）和非受控（defaultValue）两种使用模式
- ⚙️ 丰富的可配置属性：尺寸、颜色、进度可视化、只读模式等
- 🧪 开发环境支持 vitest 测试、tsup 构建、vite 示例应用
- 🚀 自动发布流程：使用 changesets 管理版本，合并后自动发布到 npm 和 GitHub Releases
- 🌐 示例应用通过 GitHub Pages 自动部署
- 📄 采用 MIT 许可证，拥有 356 颗星和 40 个复刻

---

### [GitHub - ibrahimcesar/react-lite-youtube-embed：📺 默认私密、更快更简洁的 React 应用 YouTube 嵌入组件 · GitHub](https://github.com/ibrahimcesar/react-lite-youtube-embed)

**原文标题**: [GitHub - ibrahimcesar/react-lite-youtube-embed: 📺 ‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎< A private by default, faster and cleaner YouTube embed component for React applications /> · GitHub](https://github.com/ibrahimcesar/react-lite-youtube-embed)

React Lite YouTube Embed 是一个为 React 应用设计的轻量级、注重隐私的 YouTube 嵌入组件，大小不到 5KB。

- 📦 **超轻量** – 压缩后仅 5KB（JS + CSS），远小于 YouTube 默认的 500KB iframe。
- 🔒 **默认隐私** – 用户点击前不加载 YouTube 资源，无 Cookie 或追踪。
- 🖼️ **按需加载** – 仅显示缩略图，点击后才加载播放器，提升性能。
- 🧠 **SEO 友好** – 支持 JSON-LD 结构化数据，帮助搜索引擎理解视频内容。
- ♿ **无障碍** – 支持键盘导航和屏幕阅读器，提升可访问性。
- 🛠️ **TypeScript 支持** – 提供完整的类型定义，方便开发。
- 🎬 **播放事件** – 支持 onPlay、onPause、onEnd 等事件，便于集成分析。
- 🖥️ **高质量缩略图** – 可指定 maxresdefault 等分辨率，适合英雄区展示。
- 🔒 **安全可靠** – 包含 SLSA 构建验证、CodeQL 扫描和依赖审计。

---

### [GitHub - alexbrazier/react-native-network-logger: 一个用于 React Native 的 HTTP 网络请求监控器，提供 iOS 和 Android 应用内界面，无需原生代码](https://github.com/alexbrazier/react-native-network-logger)

**原文标题**: [GitHub - alexbrazier/react-native-network-logger: An HTTP network request monitor for React Native with in-app interface for iOS and Android with no native code · GitHub](https://github.com/alexbrazier/react-native-network-logger)

react-native-network-logger 是一个用于 React Native 的 HTTP 网络流量监控工具，提供应用内界面，支持 iOS 和 Android，无需原生依赖。

- 🌟 支持 iOS 和 Android 平台，零原生依赖，可替代 Wormholy
- 📱 提供应用内查看器，可单独查看请求/响应头和正文
- 🔄 支持复制或分享头部、正文、完整请求，以及 cURL 格式分享
- 🎨 内置深色/浅色主题，并允许完全自定义主题对象
- ⚙️ 可配置最大请求数（默认 500）、忽略特定主机、URL 或模式
- 📊 支持按升序或降序排序，设置最大显示行数，以及紧凑行模式
- 🚀 可强制启用，即使与其他网络拦截器（如 Reactotron）冲突
- 🔗 支持集成现有导航，使用自定义返回按钮
- 📦 内置 TypeScript 定义，提取 GraphQL 操作名，支持 HAR 格式导出
- 🛠️ 适合调试构建和发布版本，可安全捆绑并通过标志控制

---

### [GitHub - numandev1/react-native-compressor: 🗜️压缩图片、视频和音频，效果如同 WhatsApp 🚀✨](https://github.com/numandev1/react-native-compressor)

**原文标题**: [GitHub - numandev1/react-native-compressor: 🗜️Compress Image, Video, and Audio same like Whatsapp 🚀✨ · GitHub](https://github.com/numandev1/react-native-compressor)

这是一个 React Native 压缩库，能像 WhatsApp 一样自动压缩图片、视频和音频，且体积小巧。

- 🗜️ 支持图片、视频和音频的自动或手动压缩，效果类似 WhatsApp
- 📦 体积仅增加 50KB，远小于 FFmpeg 的 9MB
- 🖼️ 图片压缩支持自动模式（类似 WhatsApp）和手动设置最大宽高、质量
- 🎬 视频压缩支持自动模式、手动设置码率，并可取消进行中的压缩
- 🎵 音频压缩支持通过质量等级或手动设置比特率、采样率、声道数
- ☁️ 支持后台上传、取消上传（单个或全部），以及文件下载
- 🎞️ 可生成视频缩略图并清理缓存
- 📊 提供获取图片/视频元数据、转换真实路径、生成临时文件路径等工具函数
- ⚙️ 支持 React Native 新架构（Turbo Module）和 Expo 托管工作流

---

### [发布 v14.0.0 · callstack/react-native-testing-library · GitHub](https://github.com/callstack/react-native-testing-library/releases/tag/v14.0.0)

**原文标题**: [Release v14.0.0 · callstack/react-native-testing-library · GitHub](https://github.com/callstack/react-native-testing-library/releases/tag/v14.0.0)

react-native-testing-library v14.0.0 版本发布，包含重大变更、新功能和迁移指南。

- 🚀 最低要求升级：需要 React 19+、React Native 0.78+ 和 Node.js ^22.13.0 || >=24，并弃用 React 18 支持。
- 🔄 核心 API 异步化：`render()`、`renderHook()`、`fireEvent()` 和 `act()` 现在默认返回 Promise，需使用 `await` 调用。
- 🧹 移除旧 API：删除了 `renderAsync`、`renderHookAsync`、`fireEventAsync`、`update` 别名、`UNSAFE_root` 和遗留 `UNSAFE_*` 查询。
- 🆕 新功能引入：重新引入 `container` API，仅暴露宿主元素，并支持类似 React Native 的隐藏属性（如 `display: 'none'`）。
- 🛠️ 行为改进：`fireEvent.press()` 和 `fireEvent.scroll()` 现在传递默认合成事件对象，并改进可访问名称计算。
- 📦 依赖变更：用 Test Renderer 替换 React Test Renderer，需安装匹配 React 19 版本的 Test Renderer（如 1.0、1.1 或 1.2）。
- ⚠️ 警告与验证：`configure`、`render` 等函数在传递未知选项时发出警告，并强制文本字符串在 `<Text>` 组件内渲染。
- 🧩 提供 Codemods：包含 `rntl-v14-update-deps` 和 `rntl-v14-async-functions` 两个自动化迁移工具，简化升级过程。

---

### [GitHub - prescottprue/react-redux-firebase: Firebase 的 Redux 绑定。包含 React Hooks 和高阶组件。](https://github.com/prescottprue/react-redux-firebase)

**原文标题**: [GitHub - prescottprue/react-redux-firebase: Redux bindings for Firebase. Includes React Hooks and Higher Order Components. · GitHub](https://github.com/prescottprue/react-redux-firebase)

react-redux-firebase 是一个为 Firebase 提供 Redux 绑定的库，包含 React Hooks 和高阶组件，支持实时数据库、Firestore 和存储等功能。

- 🔥 支持认证功能，自动加载用户配置文件
- 📡 全面支持 Firebase 平台，包括实时数据库、Firestore 和存储
- 🔗 通过 React Hooks（`useFirebaseConnect`、`useFirestoreConnect`）或高阶组件自动绑定/解绑监听器
- 🧩 提供数据填充功能，类似 Mongoose 的 `populate` 或 SQL 的 `JOIN`
- 📊 支持多种查询类型，如 `orderByChild`、`limitToLast`、`startAt` 等
- 🛠 集成示例丰富，包括 `redux-thunk`、`redux-observable` 等
- 🌐 支持服务器端渲染和 React Native
- 📦 安装简单，通过 `npm install --save react-redux-firebase` 即可
- 📚 提供详细文档和示例，位于 `react-redux-firebase.com`

---

### [发布 v9.1.0 · mui/material-ui · GitHub](https://github.com/mui/material-ui/releases/tag/v9.1.0)

**原文标题**: [Release v9.1.0 · mui/material-ui · GitHub](https://github.com/mui/material-ui/releases/tag/v9.1.0)

Material-UI v9.1.0 发布，包含多项无障碍改进和组件修复。

- ⚙️ 支持 `prefers-reduced-motion` 设置，尊重用户动画偏好
- ♿️ 通过 `enhanceHighContrast` 主题包装器改进 Windows 高对比度模式支持
- 🔧 自动补全组件修复：清除高亮、受控值、VoiceOver 焦点、空引用等问题
- 🏷️ 徽章组件添加 `aria-hidden` 属性并使用内联 CSS 变量定位
- 🔘 按钮组件修复自定义 flex 间隙样式
- 🗔 对话框组件修复不需要的焦点环
- 🔍 焦点陷阱组件修复 `tabIndex >= 1` 时的错误标签顺序
- ⏳ 进度组件仅显示一次运行时错误
- 📋 选择组件支持空格键选择和关闭时输入查找
- 👣 步骤按钮和步骤器组件改进暗色模式对比度和垂直布局
- 📑 标签页组件修复 React 18 的 roving tabindex 和重复警告
- 🎨 主题组件新增高对比度主题增强器
- ⏰ 时间线项目修复额外间距问题
- 💡 工具提示组件修复子元素禁用时卡住的问题
- 🔄 过渡组件支持自定义和 `prefers-reduced-motion`
- 🛡️ 工具函数修复 `fastDeepAssign` 的原型污染
- 📚 文档改进：添加 `slotProps` 文档、修复链接、优化加载性能
- 🧪 测试改进：添加 axe-core 可访问性测试和 Tailwind CSS 配置
- 🛠️ 代码基础设施：转换多个包到 TypeScript、优化 CI 工作流

---

### [适用于 iOS 和 Android 的预构建组织组件](https://clerk.com/changelog/2026-06-05-ios-android-organization-management?utm_source=cooper_press&utm_medium=newsletter&utm_campaign=org-components&utm_content=06-12-26&dub_id=L2maH6F3rNx6uR0N)

**原文标题**: [Prebuilt Organization components for iOS and Android](https://clerk.com/changelog/2026-06-05-ios-android-organization-management?utm_source=cooper_press&utm_medium=newsletter&utm_campaign=org-components&utm_content=06-12-26&dub_id=L2maH6F3rNx6uR0N)

### 概述摘要
Clerk 的原生移动 SDK 现已为 iOS 和 Android 提供预构建的组织管理 UI，涵盖账户切换和组织设置功能。

- 🔄 **OrganizationSwitcher**：显示当前组织或个人账户，支持切换账户、接受邀请/建议、创建组织及管理当前组织。
- 📋 **OrganizationListView**：独立的账户选择器，用于选择个人账户或组织，包含成员身份、邀请、建议及组织创建功能。
- ⚙️ **OrganizationProfileView**：权限控制下的组织管理界面，可编辑资料详情、管理成员、邀请、请求、验证域名、退出或删除组织。
- 👥 **贡献者**：Sam Wolfand 和 Sean Perez。

---

### [performative-ui | AI 原生 React 组件](https://vorpus.github.io/performativeUI/)

**原文标题**: [performative-ui | AI-native React Components](https://vorpus.github.io/performativeUI/)

本报告概述了全球气候变化对农业生产的深远影响，并提出了适应性策略。

- 🌍 全球气温上升导致极端天气频发，如干旱和洪水，严重影响农作物产量。
- 🌾 主要粮食作物（如小麦、水稻）的种植区域正被迫向更高纬度迁移，以应对温度变化。
- 💧 水资源短缺加剧，灌溉系统面临压力，需推广节水技术和雨水收集方法。
- 🌱 农业生物多样性下降，传统品种的遗传资源丧失，威胁长期粮食安全。
- 🛠️ 建议采用气候智能型农业，包括改良作物品种、精准农业和土壤保护措施。
- 📊 政策支持至关重要，需加强国际合作，提供资金和技术援助，帮助小农户适应变化。

---

### [performative-ui | AI 原生 React 组件](https://vorpus.github.io/performativeUI/#/components/node-graph)

**原文标题**: [performative-ui | AI-native React Components](https://vorpus.github.io/performativeUI/#/components/node-graph)

概述摘要：本文探讨了人工智能在医疗领域的应用，重点介绍了其如何通过数据分析、诊断辅助和个性化治疗提升医疗效率与准确性，同时强调了数据隐私和伦理挑战的重要性。

- 🩺 人工智能通过分析大量医疗数据（如影像、病历）辅助医生更快速、精准地诊断疾病。
- 💊 个性化治疗：AI 可根据患者基因、生活习惯等数据定制治疗方案，提高疗效。
- 📊 效率提升：自动化处理行政任务（如预约、病历整理），减轻医护人员负担。
- 🔒 数据隐私：医疗数据敏感，需严格保护患者隐私，防止泄露或滥用。
- ⚖️ 伦理挑战：AI 决策的透明性、责任归属及算法偏见问题需谨慎解决。

---

### [一夜之间，构建 HTML 优先网站让我们的用户翻倍](https://mohkohn.co.uk/writing/html-first/)

**原文标题**: [How building an HTML-first site doubled our users overnight](https://mohkohn.co.uk/writing/html-first/)

概述总结  
- 📈 采用 HTML 优先策略后，用户数量一夜之间翻倍。  
- 🏢 客户是一家公用事业公司，面临客户满意度低于 96% 可能被罚款数百万英镑的压力。  
- ❌ 之前两次昂贵的尝试（包括 React 应用）均告失败，React 应用因加载缓慢、可访问性差等问题上线 3 天即被撤回。  
- 🛠️ 使用 Astro 构建 HTML 优先网站，JavaScript 仅用于渐进增强，确保在老旧设备和弱网络下正常工作。  
- 🎯 核心要求：每个表单会话有唯一 ID、数据实时存储在后台、无需 JavaScript 即可完成表单、支持老旧浏览器、满足 WCAG AA 可访问性标准。  
- 📝 表单采用传统页面提交模式，每步提交后验证并重定向，避免客户端 JavaScript 的复杂性和性能问题。  
- 💡 开发了轻量级 HTML Web 组件（validation-enhancer），利用浏览器原生验证，提供现代错误提示，代码不到 1KB，且支持回退机制。  
- 🚀 上线后表单完成人数翻倍，分析工具甚至无法追踪到新用户来源（因 JavaScript 失败被忽略的用户）。  
- ⏳ 后端会话保持数据不丢失，有用户在一个月后完成表单。  
- 😞 继任者认为 HTML 优先方法“工作量更大”，但作者强调：不应抛弃使用老旧设备、弱网络或辅助技术的用户，尤其是公共服务。

---

### [WWDC26 新闻：Safari 27 测试版中的 WebKit | WebKit](https://webkit.org/blog/17967/news-from-wwdc26-webkit-in-safari-27-beta/)

**原文标题**: [  News from WWDC26: WebKit in Safari 27 beta | WebKit](https://webkit.org/blog/17967/news-from-wwdc26-webkit-in-safari-27-beta/)

以下是 WWDC26 上 Safari 27 Beta 版本的更新摘要：

Safari 27 Beta 带来了 58 项新功能、525 项修复和 4 项弃用，重点提升了 WebKit 的质量、标准合规性和开发者体验。

- 🎨 **自定义 Select 元素**：新增 `appearance: base-select` 和 `::picker-icon`、`::checkmark` 等伪元素，让你无需 JavaScript 即可完全自定义 `<select>` 样式，同时保留原生表单控件的无障碍性和功能。
- 🖱️ **滚动锚定 (Scroll Anchoring)**：自动调整滚动位置，防止因上方内容加载（如图片、广告）导致的页面跳动，多数网站无需额外配置即可受益。
- ⚡ **WebAssembly JSPI 支持**：实现 JavaScript Promise 集成，让 Wasm 代码能以同步方式等待异步操作，简化 C/C++/Rust 等代码向 Web 的移植。
- 🧭 **变换感知锚点定位**：当锚点元素应用 CSS 变换（如缩放、旋转）时，定位元素能正确跟随其变换后的位置，完善了锚点定位功能。
- 🎯 **CSS 新特性**：新增 `:heading` 伪类（匹配所有标题）、`revert-rule` 关键字（精确回退样式规则）、`stretch` 关键字（填充可用空间，考虑外边距）等。
- 📜 **子像素内联布局**：文本和内联元素可实现设备像素级精确定位，显著提升块级方向上的布局准确性。
- 🔧 **JavaScript 模块加载器重写**：完全符合标准的 ES 模块加载器，修复了顶层 await 的模块执行顺序和初始化问题，解决了长期存在的跨浏览器兼容性痛点。
- 🖼️ **HTML 改进**：支持 `<img sizes="auto">`（自动计算响应式图片尺寸）、声明式 Shadow DOM 的 `shadowrootslotassignment` 属性。
- 🌐 **Web API 增强**：新增 Service Worker 静态路由 API、SharedWorker 内创建 Dedicated Worker、`ReadableStream` 异步迭代及跨上下文传输能力。
- 🎥 **媒体与 WebRTC**：支持 `TextTrackCue.endTime = Infinity`（无限时长的字幕）、WebRTC 的 `targetLatency` 属性及视频源宽高统计。
- 🧩 **WebAssembly 与 MathML**：Wasm 支持 JSPI；MathML 支持多字符运算符、`tabindex`、`focus()` 等，提升键盘导航和无障碍性。
- 🌍 **空间 Web**：visionOS 支持沉浸式网站环境；`<model>` 元素扩展至 iOS、iPadOS 和 macOS；支持 `dynamic-range-limit` 控制 HDR 渲染。
- 🎨 **渲染与 WebGPU**：新增 `srgb-linear` 和 `display-p3-linear` 颜色空间；WebGPU 支持 WGSL 着色器的 `clip_distances` 内置值。
- 🛠️ **Web Inspector 升级**：颜色选择器内联显示对比度信息；网络标签显示完整重定向链；元素标签新增子网格和网格线徽章。
- 🔒 **网络与存储**：支持 loopback 主机的 Secure Cookie；Cookie Store API 支持 `maxAge` 设置。
- ♿ **无障碍性修复**：大量修复，包括 SVG `<use>` 元素、`aria-owns`、`aria-labelledby`、VoiceOver 与 MathML 的交互等。
- 🐛 **大量 Bug 修复**：涵盖 CSS、JavaScript、HTML、媒体、渲染、表单、打印等多个领域，共计 525 项修复，显著提升稳定性和标准一致性。

---

### [发布 electron v43.0.0-beta.1 · electron/electron · GitHub](https://github.com/electron/electron/releases/tag/v43.0.0-beta.1)

**原文标题**: [Release electron v43.0.0-beta.1 · electron/electron · GitHub](https://github.com/electron/electron/releases/tag/v43.0.0-beta.1)

概述摘要  
Electron v43.0.0-beta.1 版本发布，包含多项修复和性能改进，并更新了 Chromium 内核。  

- 🐛 修复：分离的 DevTools 窗口中的上下文菜单现在正确聚焦 DevTools 窗口，而非被检查页面  
- ⚡ 性能提升：macOS 构建启用 ThinLTO 优化，提升应用启动速度和运行时性能  
- 🛠️ 修复：解决 Buffer/TextEncoder API 的数据截断问题，以及 Apple Silicon 上 fs.writeFileSync 的崩溃  
- 🚀 启动优化：主进程从嵌入式 Node.js 快照启动，框架和预加载脚本缓存为 V8 字节码，沙盒渲染器启动数据提前推送  
- 🐧 跨平台改进：Linux 和 Windows 构建启用 ThinLTO 链接时优化，提升性能  
- 🗑️ 移除：Linux 上 dialog API 的 showHiddenFiles 支持  
- 🔄 更新：Chromium 内核升级至 150.0.7863.0

---

