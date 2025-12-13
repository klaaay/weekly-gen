### [Next.js 安全更新：2025 年 12 月 11 日 | Next.js](https://nextjs.org/blog/security-update-2025-12-11)

**原文标题**: [Next.js Security Update: December 11, 2025 | Next.js](https://nextjs.org/blog/security-update-2025-12-11)

Next.js 于 2025 年 12 月 11 日发布安全更新，针对 React 服务器组件协议中新发现的两个漏洞（CVE-2025-55183 和 CVE-2025-55184）提供了修复方案。这些漏洞源于上游 React 实现，会影响使用 App Router 的 Next.js 应用，可能导致拒绝服务或源代码暴露。用户需根据自身版本升级至指定的修复版本。

- 🚨 **漏洞概述**：新发现两个 React 服务器组件协议漏洞，均不允许远程代码执行，但需及时修复。
- ⚠️ **影响与严重性**：CVE-2025-55184（高危）可导致服务器拒绝服务；CVE-2025-55183（中危）可能暴露源代码和业务逻辑。
- 🔄 **修复更新**：CVE-2025-55184 的初始修复不完整，已发布完整修复 CVE-2025-67779，此前已升级的用户需再次更新。
- 📊 **受影响版本**：涉及 Next.js 13.3 及以上、14.x、15.x 及 16.x 的多个版本，具体修复版本已在文中列出。
- ⬆️ **升级操作**：所有用户必须升级至其发布线的最新修复版本，无替代方案，可使用工具`npx fix-react2shell-next`辅助升级。
- ℹ️ **补充说明**：Pages Router 应用不受影响，但仍建议升级；漏洞由安全研究人员发现并已负责任地披露。

---

### [React 新时代已来临：你需要了解的关键信息 - LogRocket 博客](https://blog.logrocket.com/the-next-era-of-react/)

**原文标题**: [The next era of React has arrived: Here's what you need to know - LogRocket Blog](https://blog.logrocket.com/the-next-era-of-react/)

React 已进入异步协调的新时代，通过声明式原语简化了异步 UI 构建，将开发者从手动管理加载状态、错误处理和竞态条件的繁琐工作中解放出来。

- 🚀 **React 19 引入 Actions**：使用`startTransition`自动追踪异步操作状态，简化表单提交等场景的代码。
- ⚡ **乐观更新提供即时反馈**：`useOptimistic`在等待服务器响应时立即更新 UI，提升用户体验。
- 🌀 **Suspense 声明式处理加载状态**：通过边界定义加载回退界面，实现并行数据加载。
- 🔄 **Transitions 与 Suspense 结合**：导航时保持现有内容可见，避免界面闪烁，实现平滑过渡。
- 📥 **use() 直接读取异步数据**：替代`useEffect`进行数据获取，与 Suspense 配合简化代码结构。
- 🛡️ **useDeferredValue 稳定快速更新**：延迟处理频繁输入（如搜索），保持 UI 响应性。
- 🧩 **框架集成实现完整协调**：路由、数据层和设计系统共同运用这些原语，构建流畅的异步应用。
- 🛠️ **可逐步采用**：新原语与现有代码兼容，适合在复杂交互功能中逐步替换传统模式。

---

### [错误](https://launch.arcjet.com/AVRyNTP)

**原文标题**: [Error](https://launch.arcjet.com/AVRyNTP)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='arcjet.com', port=443): Max retries exceeded with url: /?ref=nextjs-weekly&utm_campaign=nextjs-weekly (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [未找到标题](https://x.com/rauchg/status/1997362942929440937)

**原文标题**: [No title found](https://x.com/rauchg/status/1997362942929440937)

该页面提示用户浏览器中 JavaScript 功能未启用或受限，导致无法正常使用 X 平台（原 Twitter），并提供了相应的解决方案和支持信息。

- 🔒 检测到浏览器已禁用 JavaScript，导致 X 平台功能受限
- 🌐 建议启用 JavaScript 或切换至受支持的浏览器版本
- 📚 可通过帮助中心查询具体支持的浏览器列表
- 🛠️ 提供故障排除建议：尝试刷新页面或禁用隐私扩展插件
- ⚖️ 页面底部包含服务条款、隐私政策等法律声明链接

---

### [用自定义 Cloudflare 缓存层替代 Next.js ISR](https://www.mintlify.com/blog/page-speed-improvements)

**原文标题**: [Replacing Next.js ISR with a custom Cloudflare cache layer](https://www.mintlify.com/blog/page-speed-improvements)

Mintlify 为成千上万的开发者网站提供文档服务，每月处理 7200 万页面浏览量。随着团队扩张和部署频率增加，原有的 Next.js ISR 缓存方案无法应对缓存失效问题，导致近四分之一的用户访问时遭遇冷启动延迟。为此，团队设计了一个基于 Cloudflare 的自定义边缘缓存层，将部署与缓存失效解耦，使缓存命中率从 76% 提升至接近 100%，有效消除了冷启动。

- 🛠️ **代理层**：在流量前端部署 Cloudflare Worker，根据路径、部署 ID 和请求类型构建唯一缓存键，利用边缘缓存（15 天 TTL）代理所有请求。
- 🔄 **自动版本检测与重新验证**：通过 Vercel 的 webhook 获取新部署 ID 并存储至 Cloudflare KV；当用户请求时，Worker 对比响应头中的版本与 KV 中的期望版本，若不一致则异步触发重新验证，用户立即获得旧缓存，新版本在后台预热。
- 🔒 **重新验证协调器**：使用 Durable Objects 作为全局锁，防止并行更新导致版本冲突；协调重新验证流程，包括锁定、消息队列处理和超时解锁（30 分钟容错）。
- ⚙️ **重新验证 Worker**：通过 Cloudflare Queues 处理重新验证和预热的队列消息，以批处理方式（每次 6 个连接）获取并预热所有页面的 HTML 和 RSC 变体，确保完整站点地图缓存后再更新 KV 版本。
- 🚀 **主动预热**：当客户更新文档内容时，后端通过 Worker 的管理 API 触发主动预热，将指定路径加入队列处理，防止旧版本覆盖新缓存，结合反应式重新验证实现双保险。
- 📈 **成果与自愈能力**：缓存命中率接近 100%，系统能处理代码部署和内容更新两种场景；具备自愈机制——失败重新验证会自动重试，锁定时自动清理，且边缘缓存在源站故障时仍能提供快速响应。

---

### [- YouTube](https://www.youtube.com/watch?v=d_oywGfuTnc)

**原文标题**: [ - YouTube](https://www.youtube.com/watch?v=d_oywGfuTnc)

该内容为 YouTube 平台页脚导航链接，主要涵盖平台信息、用户指南及法律条款。

- ℹ️ 关于平台的基本信息与介绍
- 📰 新闻发布与媒体相关资源
- ©️ 版权政策与知识产权说明
- 📞 用户联系与客服渠道
- 🎬 内容创作者专属资源
- 📢 广告合作与商业推广
- 💻 开发者工具与 API 接口
- ⚖️ 服务条款与使用规范
- 🔒 隐私保护与数据政策
- 🛡️ 平台安全与内容审核机制
- ⚙️ YouTube 功能运作原理说明
- 🧪 新功能测试与体验计划
- ⏳ 2025 年谷歌公司版权所有声明

---

### [React 中 useEffectEvent 的注意事项](https://slicker.me/react/useEffectEvent.html)

**原文标题**: [Do's and Don'ts of useEffectEvent in React](https://slicker.me/react/useEffectEvent.html)

useEffectEvent 是一个 React Hook，用于从 Effect 中提取非响应式逻辑，允许读取最新的 props 或 state 值，而不会因这些值的变化触发 Effect 重新执行。

- 🎯 **解决核心问题**：在 Effect 中读取最新值（如主题、用户偏好）时，避免将其加入依赖数组导致不必要的重新运行。
- 🔧 **关键机制**：创建一个稳定的函数引用，始终读取最新值，但不会在值变化时触发 Effect 重新执行。
- ✅ **正确用法**：在 Effect 内部直接调用、用于读取最新 props/state、分离响应式与非响应式逻辑、与清理逻辑结合使用。
- ❌ **避免用法**：在常规事件处理器、渲染过程中、异步调用或延迟后调用，或将其作为 prop 传递给其他组件。
- 📊 **常见用例**：日志记录与分析、携带最新状态的第三方库回调、基于最新值的防抖处理。
- ⚠️ **注意事项**：仅用于明确的非响应式逻辑需求，保持函数目的单一，避免在生产环境中使用直到稳定版发布。

---

### [React 巴黎：React，魔法般的魅力！](https://react.paris/?utm_source=nextjsweekly&utm_medium=Referral&utm_campaign=newsletter)

**原文标题**: [React Paris: React C'est Magique!](https://react.paris/?utm_source=nextjsweekly&utm_medium=Referral&utm_campaign=newsletter)

React Paris 2026 是一场为期两天的单轨道 React 技术大会，将于 2026 年 3 月 26 日至 27 日在巴黎举行，聚焦 React 生态系统的最新趋势与实践，提供丰富的演讲、实践环节和社交机会。

- 🗓️ **活动时间**：2026 年 3 月 26 日至 27 日，为期两天
- 🎤 **演讲阵容**：超过 22 位演讲者，涵盖 React Server Components、AI、设计系统、性能、Remix、TypeScript 等前沿话题
- 🎟️ **门票类型**：提供线下实体票（含独家内容与餐饮）和线上票（含录播访问）
- 🏛️ **活动地点**：巴黎蒙帕纳斯铂尔曼酒店，拥有宽敞的会议空间与自然采光
- 🤝 **核心活动**：包括主题演讲、闪电演讲、交流会、派对及实践环节，强调学习与社交并重
- 📈 **往届回顾**：2024 与 2025 年大会均获得积极反响，社区持续成长并注重多样性
- 🎯 **参会者**：面向开发者、团队负责人、顾问等，旨在激发灵感、促进学习与建立联系
- 🌐 **合作伙伴**：得到多家企业与社区的支持，包括铂金、青铜及多样性赞助商

---

### [ElevenLabs 用户界面 | ElevenLabs 用户界面](https://ui.elevenlabs.io/)

**原文标题**: [ElevenLabs UI | ElevenLabs UI](https://ui.elevenlabs.io/)

本文介绍了 Scribe v2 Realtime 的交互界面，展示了一系列可定制和扩展的开源智能体与音频组件，旨在提供实时的语音交互和音频可视化体验。

- 🎵 **音频组件**：包含实时音频可视化波形图和平滑滚动动画，支持音乐播放与控制
- 🤖 **智能体交互**：通过“Agent Orbs”可视化智能体状态（空闲、聆听、对话），提供模拟对话功能
- 🎤 **语音功能**：集成 ElevenLabs 语音合成技术，支持语音聊天、语音填充表单和实时语音通话
- 🎯 **用户目标**：设有每日活动目标设置功能，支持卡路里消耗目标调整
- 🖥️ **界面控制**：包含完整的音乐播放器控件、对话启动界面和客户支持语音聊天入口
- 🔧 **开源特性**：所有组件均为开源设计，允许用户自定义和扩展功能模块

---

### [GitHub - SameerJS6/lina：即插即用的 shadcn/ui ScrollArea 替代方案（基于 Radix/Base UI），具备原生触控、自适应遮罩和精致交互效果。](https://github.com/SameerJS6/lina)

**原文标题**: [GitHub - SameerJS6/lina: Drop-in shadcn/ui ScrollArea replacement (Radix/Base UI) with native touch, adaptive masks, and polished interactions.](https://github.com/SameerJS6/lina)

Lina 是一个专为现代 UI 设计的自适应滚动区域组件，可作为 shadcn/ui ScrollArea 的直接替代品，提供更优的默认设置和更接近原生的交互体验。

- 🎯 **无缝替代**：完全兼容 shadcn/ui ScrollArea 的 API、属性和样式，可零成本替换。
- 📱 **原生触控优化**：针对 iOS/Android 设备优化，支持动量滚动和被动监听，触感流畅自然。
- 🎨 **自适应遮罩**：仅在内容可滚动时显示边缘渐变效果，并根据滚动位置、轴向和容器形状实时调整。
- 🖱️ **微交互设计**：在非触控设备上提供悬停/按压效果的滚动条，滑块响应灵敏。
- 🔄 **双框架支持**：提供基于 Radix UI 和 Base UI 的两种版本，保持一致的 API 和视觉设计。
- 📦 **简易安装**：通过一行命令即可快速集成到项目中。
- 📄 **完整文档**：提供详细的使用指南和示例代码。
- ⚖️ **MIT 许可**：开源免费，可自由使用和修改。

---

### [GitHub - openstatusHQ/openstatus-template](https://github.com/openstatusHQ/openstatus-template)

**原文标题**: [GitHub - openstatusHQ/openstatus-template](https://github.com/openstatusHQ/openstatus-template)

OpenStatus 模板是一个基于 Next.js 和 shadcn/ui 构建的静态单页应用模板，旨在帮助开发者快速搭建项目界面。它提供了一系列高级布局组件，如 ActionCard、SectionCard、FormCard、MetricCard 和 EmptyState，这些组件遵循统一的结构模式，便于构建和管理界面布局。

- 📦 **模板用途**：基于 Next.js 和 shadcn/ui，用于快速启动项目并支持静态导出。
- 🏗️ **核心组件**：提供 ActionCard、SectionCard、FormCard、MetricCard 和 EmptyState 等高级布局组件。
- 📐 **结构模式**：组件通常遵循 Group-Card-Header/Content/Footer 的层级结构，确保界面一致性。
- 🔧 **组件示例**：例如 FormCard 包含 Header、Title、Description、Content 和 Footer 等部分，支持禁用和交互控制。
- 📊 **详细文档**：列出了每个组件（如 MetricCard、ActionCard、Section、EmptyState）的 HTML 标签和描述，方便集成。
- 🛠️ **安装方式**：通过 pnpm 命令直接添加组件，例如 `pnpm dlx shadcn@latest add [URL]`。
- 🌐 **项目状态**：模板托管在 GitHub，拥有 162 个星标和 17 个分支，主要使用 TypeScript 开发。

---

### [TypeScript 7 进展 - 2025 年 12 月 - TypeScript](https://devblogs.microsoft.com/typescript/progress-on-typescript-7-december-2025/)

**原文标题**: [Progress on TypeScript 7 - December 2025 - TypeScript](https://devblogs.microsoft.com/typescript/progress-on-typescript-7-december-2025/)

TypeScript 7.0（代号“Corsa”）的开发进展顺利，该版本将编译器与语言服务迁移至原生代码，以提升性能、内存使用和并行处理能力。目前原生预览版已稳定可用，编辑器支持与语言服务功能基本完备，编译器类型检查接近完成，并显著提升了构建速度。TypeScript 6.0 将是最后一个基于 JavaScript 的版本，之后团队将全力投入 7.0 的开发与优化。

- 🚀 TypeScript 7.0 将编译器与语言服务迁移至原生代码，显著提升性能与内存效率
- 🔧 编辑器语言服务功能已基本就绪，包括自动导入、重命名等核心特性，可通过 VS Code 扩展体验
- ⚡ 编译器类型检查接近完成，构建速度大幅提升，部分项目可达 10 倍加速
- 🛠️ 支持增量编译、项目引用等高级功能，兼容现有工作流
- ⚠️ 部分特性尚不完善，如低版本 ES 目标编译、监视模式效率、旧 API 支持等
- 📜 TypeScript 6.0 将是最后一个 JavaScript 版本，主要作为向 7.0 过渡的桥梁
- 🔄 团队将重点转向 7.0 开发，减少对 6.0 的功能更新，以加速原生版本成熟
- 📢 鼓励开发者试用预览版并提供反馈，帮助完善最终版本

---

### [使用 V0 和 Claude Code 加速构建](https://strapi.io/blog/building-faster-with-v0-and-claude-code-lessons-learned-from-vibe-coding?utm_campaign=19282052-Newsletter%20Sponsorships&utm_source=Nextjs&utm_medium=2nd-sponsor)

**原文标题**: [Building Faster with V0 and Claude Code](https://strapi.io/blog/building-faster-with-v0-and-claude-code-lessons-learned-from-vibe-coding?utm_campaign=19282052-Newsletter%20Sponsorships&utm_source=Nextjs&utm_medium=2nd-sponsor)

本文分享了作者使用 V0 和 Claude Code 进行“氛围编程”的经验与教训，强调 AI 工具虽能加速开发，但并非万能，仍需开发者具备扎实的技术基础、清晰的项目理解和有效的提示工程技巧。

- 🧠 **AI 工具非万能**：V0 和 Claude Code 等 AI 工具能快速生成代码，但并非“魔法子弹”，开发者仍需明确项目目标、理解数据结构和所用技术栈。
- 🛠️ **工具特性与选择**：V0 专注于基于 Next.js 的 UI 快速原型生成，Claude Code 则是终端端的全栈编码助手，两者结合可实现高效并行开发。
- 📋 **提示工程至关重要**：清晰的提示词（包括角色设定、任务描述、数据结构、约束条件等）能显著提升 AI 输出质量，避免“幻觉”和错误。
- 🚫 **常见陷阱与应对**：模糊提示导致 AI 臆测、单次提示结果不完整、未受控的副作用（如 API 过载）是常见问题，需通过分步提示、代码审查和速率限制来规避。
- 🔄 **开发流程实践**：根据现有项目情况（已有 Strapi 后端、已有 Next.js 前端或从零开始）采用不同策略，例如利用真实 API 响应数据引导 AI 生成类型安全的前端代码。
- 📚 **项目文档化**：为 Claude Code 创建详细的`CLAUDE.md`文件，包含项目结构、命令、配置和官方文档链接，能极大提升 AI 协作效率。
- ⚙️ **安全与最佳实践**：切勿将 AI 工具直接指向生产环境，始终在开发环境中测试；建立清晰的 AI 代理工作流程（探索→规划→编码→提交），并保持人类开发者的最终审核权。
- 🔮 **持续学习与实验**：AI 辅助开发领域快速演进，开发者应积极尝试、建立文档并分享经验，目标是利用工具提升思维效率和构建速度，而非替代思考。

---

### [Vercel for Platforms 平台介绍 - Vercel](https://vercel.com/changelog/introducing-vercel-for-platforms)

**原文标题**: [Introducing Vercel for Platforms - Vercel](https://vercel.com/changelog/introducing-vercel-for-platforms)

Vercel 推出了 Vercel for Platforms 产品，使开发者能够轻松为用户创建和管理客户项目，提供多租户和多项目两种平台模式，并引入了 Platform Elements 库以简化平台构建流程。

- 🏗️ 提供多租户和多项目两种平台构建模式
- 🌐 多租户模式支持通配符域名和自定义域名，实现单次部署全局更新
- 🔒 自动处理 SSL 证书和 DNS 验证，简化域名管理流程
- 🛡️ 多项目模式为每个客户创建独立项目，实现环境隔离
- ⚡ 支持通过 SDK 快速部署客户代码并自动检测框架
- 📦 新增 Platform Elements 库降低平台开发复杂度
- 🚀 提供多租户和多项目模式的快速入门指南

---

### [CSS 2025 年度回顾](https://chrome.dev/css-wrapped-2025/)

**原文标题**: [CSS Wrapped 2025](https://chrome.dev/css-wrapped-2025/)

本文介绍了 2024 年 CSS 和 HTML 的一系列新特性与改进，涵盖交互组件、滚动体验、动画优化及样式增强等方面，旨在提升开发者构建现代 Web 应用的能力与效率。

- 🎛️ **调用器命令**：通过`commandfor`和`command`属性，无需 JavaScript 即可声明式控制对话框和弹出层的显示与隐藏，支持自定义命令。
- 🖱️ **对话框轻量关闭**：新增`closedby`属性，使`<dialog>`元素支持点击外部或按 ESC 键关闭，类似弹出层的行为。
- 💡 **提示弹出层**：`popover="hint"`允许创建临时性 UI（如工具提示），不会关闭其他弹出层，并可结合`interestfor`属性实现悬停触发。
- 🎨 **可自定义选择框**：通过`appearance: base-select`完全用 CSS 样式化`<select>`元素，支持 HTML 内容嵌入和下拉列表顶层渲染。
- 🏎️ **滚动按钮与标记**：新增`::scroll-button()`和`::scroll-marker()`伪元素，用于创建原生可访问的轮播导航，无需 JavaScript。
- 🔗 **滚动目标组**：`scroll-target-group`属性将锚点链接列表转换为滚动标记，结合`:target-current`实现滚动高亮导航。
- 🎯 **锚定容器查询**：通过`container-type: anchored`和`anchored()`函数，根据定位回退状态动态调整样式（如工具提示箭头方向）。
- 👁️ **兴趣调用器**：`interestfor`属性提供声明式方式，在悬停或聚焦时触发 UI 显示，特别适合工具提示和预览卡片，支持延迟设置。
- 📜 **滚动状态查询**：`container-type: scroll-state`允许查询元素是否处于滚动、吸附或固定状态，并据此应用样式。
- 🔢 **树计数函数**：`sibling-index()`和`sibling-count()`函数简化基于元素位置的动画和布局，实现自动适应的交错效果。
- 🧭 **滚动至视图容器**：`scrollIntoView()`新增`container`选项，限制滚动到最近祖先容器，避免嵌套滚动问题。
- 🌀 **嵌套视图过渡组**：扩展视图过渡 API，支持嵌套`::view-transition-group`以保留 3D 和裁剪效果。
- 🏗️ **DOM 状态保留移动**：`moveBefore()`方法在移动元素（如视频或 iframe）时保持其状态，避免重新加载。
- 🛠️ **高级 attr() 函数**：增强`attr()`支持解析属性值为颜色、长度等类型，并可用于任何 CSS 属性。
- 🍪 **ToggleEvent.source**：在切换事件中识别触发元素，便于根据不同按钮执行操作（如接受或拒绝 Cookie）。
- 📏 **文本框特性**：`text-box-trim`和`text-box-edge`属性优化文本垂直对齐，实现视觉居中。
- ✂️ **shape() 函数**：用于创建复杂响应式裁剪形状，支持动画和自定义属性控制。
- ⚖️ **if() 语句**：在 CSS 中引入条件逻辑，基于媒体查询、特性支持或样式查询动态设置属性值。
- 🔧 **自定义函数**：通过`@function`定义可重用 CSS 函数，提升代码复用性和清晰度。
- 📊 **扩展范围语法**：在样式查询和`if()`中支持范围比较（如`>`、`<`），增强动态样式能力。
- 📐 **拉伸尺寸关键字**：`stretch`关键字使元素填充包含块空间，同时保留外边距。
- 🔶 **角形形状**：`corner-shape`属性提供多种角形样式（如斜角、凹口、圆形），并支持动画和超级椭圆曲线定制。

---

### [- YouTube](https://www.youtube.com/watch?v=S1YKKpLR7XI)

**原文标题**: [ - YouTube](https://www.youtube.com/watch?v=S1YKKpLR7XI)

该文本为 YouTube 平台页脚导航链接列表，概述了网站的主要政策、功能与公司信息。

- 📄 关于平台与公司信息
- 📰 新闻与媒体相关
- ©️ 版权说明
- 📞 联系渠道
- 🧑‍🎨 创作者服务
- 📢 广告合作
- 👨‍💻 开发者资源
- ⚖️ 使用条款
- 🔒 隐私政策
- 🛡️ 安全与政策
- ⚙️ 平台运作机制
- 🧪 新功能测试
- 🏢 企业版权声明（2025 年谷歌公司）

---

### [设计系统设计 | TkDodo 的博客](https://tkdodo.eu/blog/designing-design-systems)

**原文标题**: [Designing Design Systems | TkDodo's blog](https://tkdodo.eu/blog/designing-design-systems)

作者虽非设计师，但作为后端工程师转型前端，现于 Sentry 设计工程团队负责构建 Scraps 设计系统，强调设计系统不仅是美观组件，更是提升团队协作与开发效率的关键工具。

- 🛠️ 设计系统需兼顾 API 设计、性能、开发者体验等工程要素，确保系统稳健易用
- 🚀 团队核心目标是帮助产品快速交付，设计系统是重要工具之一，但开发者教育、高效 CI 流程同样关键
- 📝 优秀设计系统应注重类型安全、文档完善、可访问性内置，并避免过度设计（如减少布尔属性）
- 🔧 提倡组合优于继承，提供可控组件与合理的默认设置，同时支持必要的“逃生舱口”
- 🌐 设计系统成功依赖团队文化采纳，而非单纯技术实现，需鼓励外部贡献并保持一致性

---

