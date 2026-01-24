### [React 状态周报 第 459 期：2026 年 1 月 23 日](https://react.statuscode.com/issues/459)

**原文标题**: [React Status Issue 459: January 23, 2026](https://react.statuscode.com/issues/459)

本期简报聚焦 React 生态的新动态与工具更新，涵盖视频创作、UI 组件、性能优化及社区活动等多元内容。

- 🎬 Remotion 推出 AI 代理技能，支持通过提示词直接生成高质量 React 视频，引发广泛关注与尝试。
- 📝 SurveyJS 提供 React 拖放表单构建器，支持无代码设计并与任意后端集成，数据收集不受 SaaS 限制。
- ⚙️ 文章探讨 Shadcn 单选按钮的过度复杂性，引发对 UI 框架在可访问性与跨浏览器行为中权衡的讨论。
- 🌍 React Paris 将于 3 月 26-27 日举行，提供线上线下混合参与方式。
- 📱 Tiny Harvest 展示 React Native 与 Expo 开发的“休闲农场”手游，体现跨平台开发潜力。
- 🚀 Turbopack 通过减少构建量提升大型代码库的热重载速度与缓存效率。
- 📚 多篇技术文章分享 React Compiler 适配、useMemo/useCallback 性能优化及 Next.js PWA 离线支持实践。
- 🛠️ 新工具包括自动生成骨架屏的 Shimmer 库、React Native Windows v0.81 更新及 Vercel 的 AI 生成 UI 实验项目 json-render。
- 🔄 生态动态涵盖 Mastra AI 框架 1.0 发布、Electron 40 版本升级及 HTTP Archive 2025 年度网络报告发布。

---

### [Remotion | 以编程方式制作视频](https://www.remotion.dev/)

**原文标题**: [Remotion | Make videos programmatically](https://www.remotion.dev/)

Remotion 是一个基于 React 的编程式视频创作框架，允许开发者通过代码创建、编辑和渲染动态视频，并提供云端渲染、多种许可证选项和丰富的社区资源。

- 🎬 使用 React 技术通过代码创建复杂的视频内容，支持参数化动态编辑
- ⚙️ 提供 Remotion Studio、Player 和 Editor Starter 等工具，便于视频制作与集成
- ☁️ 支持本地、服务器或通过 Remotion Lambda 进行可扩展的云端渲染，输出 MP4 等格式
- 💼 提供免费许可证（适用于 3 人以下团队）和公司许可证（4 人以上团队，含优先支持）
- 🏢 提供企业许可证，包含定制条款、月度咨询和专属支持等高级服务
- 🛠️ 包含丰富的用例展示，如音乐可视化、字幕生成和年度回顾视频等
- 🌐 拥有活跃的开发者社区，提供大量文档、模板和专家支持资源

---

### [未找到标题](https://x.com/Remotion/status/2013626968386765291)

**原文标题**: [No title found](https://x.com/Remotion/status/2013626968386765291)

该页面提示用户浏览器中 JavaScript 功能未启用或存在兼容性问题，导致无法正常使用 X 平台（原 Twitter），并提供了相应的解决建议与支持资源。

- 🔧 检测到 JavaScript 被禁用，请启用或更换受支持的浏览器
- 🌐 可访问帮助中心查看支持的浏览器列表
- 🛡️ 部分隐私扩展可能导致异常，建议暂时禁用后重试
- 🔄 遇到错误时可尝试刷新页面重新加载
- 📜 页脚包含服务条款、隐私政策等法律文件链接

---

### [skills/skills/remotion/SKILL.md 位于主分支 · remotion-dev/skills · GitHub](https://github.com/remotion-dev/skills/blob/main/skills/remotion/SKILL.md)

**原文标题**: [skills/skills/remotion/SKILL.md at main · remotion-dev/skills · GitHub](https://github.com/remotion-dev/skills/blob/main/skills/remotion/SKILL.md)

这是一个名为 Remotion Skills 的 GitHub 仓库，由 remotion-dev 组织维护，用于展示与 Remotion 框架相关的技能和项目。

- 🏷️ **仓库名称**：skills
- 👥 **维护者**：remotion-dev 组织
- ⭐ **受欢迎度**：获得 601 个星标
- 🍴 **复刻数**：被复刻 61 次
- 📂 **公开状态**：仓库为公开可见
- 🔒 **安全状态**：安全扫描显示 0 个问题
- 📝 **协作状态**：当前无开放的议题或拉取请求

---

### [Claude 代码会话 · GitHub](https://gist.github.com/JonnyBurger/5b801182176f1b76447901fbeb5a84ac)

**原文标题**: [Claude Code Session · GitHub](https://gist.github.com/JonnyBurger/5b801182176f1b76447901fbeb5a84ac)

本文档记录了在 Claude Code 环境中使用 Remotion 框架创建动画视频的完整开发过程，展示了从初始设置到最终渲染的交互式编程会话。

- 🎬 **创建终端动画**：开发了一个 macOS 风格的终端窗口组件，包含标题栏、交通灯按钮和命令行界面。
- ⌨️ **实现打字机效果**：为终端添加了动态打字动画，逐步显示"npx skills add remotion-dev/skills"命令。
- 📊 **模拟安装输出**：在命令执行后显示 SKILLS ASCII 艺术标志和分阶段出现的安装进度信息。
- 🎞️ **构建主合成**：创建了包含 3D 旋转、弹簧动画和翻转效果的主合成序列，终端从底部滑入并随时间旋转。
- 🖼️ **添加品牌标识**：整合了 Remotion、Claude Code 和 OpenCode 的 logo，并设计了"Agent Skills now available"文字动画。
- 🔄 **实现复杂转场**：终端在完成输出后向前翻转 90 度，同时背景显示品牌标识组合。
- ⚙️ **参数微调过程**：通过多次迭代调整字体大小、尺寸比例、旋转角度和动画时长等视觉效果。
- 🎥 **最终渲染输出**：将 8 秒时长的动画渲染为视频文件，展示了完整的开发工作流程。

---

### [Claude Code 现已能制作视频（Remotion 指南）- YouTube](https://www.youtube.com/watch?v=Vu_XOKKgJtA)

**原文标题**: [Claude Code Can Make Videos Now (Remotion Guide) - YouTube](https://www.youtube.com/watch?v=Vu_XOKKgJtA)

该文本是 YouTube 网站页脚的导航链接列表，展示了其各项政策、资源与功能入口。

- 🏠 **平台信息** - 包含版权声明、联系方式和运营公司信息
- 👥 **用户服务** - 提供创作者支持、广告投放和开发者资源
- 📜 **政策条款** - 涵盖使用规范、隐私政策及安全说明
- 🔧 **功能体系** - 说明平台运作机制并邀请用户体验新功能

---

### [仅通过提示创建视频 - Claude Code 与 Remotion - YouTube](https://www.youtube.com/watch?v=Xtd4DjU9AU8)

**原文标题**: [Creating videos just from prompting - Claude Code and Remotion - YouTube](https://www.youtube.com/watch?v=Xtd4DjU9AU8)

YouTube 平台功能与服务概览  
- 🏠 主页与导航结构  
- 📄 法律与政策文档  
- 📞 用户支持与联系渠道  
- 🎨 创作者资源与工具  
- 💼 广告合作与商业化服务  
- ⚙️ 开发者接口与技术支持  
- 📜 平台使用条款与协议  
- 🔒 隐私保护与安全措施  
- 🔄 平台运行机制说明  
- 🧪 新功能测试与体验  
- ©️ 谷歌公司版权声明（截至 2026 年）

---

### [人们如何利用 Claude 代码（Remotion 技能）生成视频 - YouTube](https://www.youtube.com/watch?v=7OR-L0AySn8)

**原文标题**: [How people are generating videos with Claude Code (Remotion Skill) - YouTube](https://www.youtube.com/watch?v=7OR-L0AySn8)

YouTube 平台是一个提供视频分享和观看服务的在线平台，由 Google LLC 运营。

- 📄 提供平台规则与政策信息，包括使用条款和隐私政策
- 🔒 强调用户隐私与平台安全措施
- 🛠️ 为内容创作者、广告商和开发者提供专门资源与工具
- 📢 设有新闻发布室，用于公布官方动态
- 🆕 鼓励用户体验新推出的功能
- ©️ 明确版权归属和联系渠道

---

### [未找到标题](https://x.com/search?q=remotion&src=typed_query)

**原文标题**: [No title found](https://x.com/search?q=remotion&src=typed_query)

该页面提示用户浏览器中 JavaScript 功能未启用或受限，导致无法正常使用 X 平台（原 Twitter），并提供了相应的解决建议与支持资源。

- 🚫 JavaScript 未启用导致功能受限
- 🌐 建议启用 JavaScript 或更换受支持浏览器
- 📖 可访问帮助中心查看浏览器兼容列表
- 🔧 隐私扩展插件可能引发访问问题
- 🔄 提供“重试”功能应对临时故障
- ⚖️ 页面底部包含服务条款与隐私政策链接

---

### [调查与表单管理软件 - SurveyJS](https://surveyjs.io/?utm_source=react_status&utm_medium=referral&utm_campaign=q1_2026)

**原文标题**: [Survey and Form Management Software - SurveyJS](https://surveyjs.io/?utm_source=react_status&utm_medium=referral&utm_campaign=q1_2026)

SurveyJS 是一个开源 JavaScript 库套件，用于在 Web 应用中自主构建和管理调查表单，支持完全的数据所有权和自托管，无需依赖第三方 SaaS 平台。

- 📚 **表单库** – 免费 MIT 许可的 UI 组件，可解析 JSON 文件并即时渲染动态交互式表单，用于收集用户响应并发送至自有数据库。
- 🛠️ **调查创建器** – 白标拖放式表单构建器，自动生成描述表单结构、布局和样式的 JSON 模式，支持完全自定义以匹配应用设计。
- 📊 **仪表板** – UI 组件，通过解析 JSON 模式识别数据类型，并用响应数据填充自定义仪表板，以交互式图表和表格可视化调查结果。
- 🖨️ **PDF 生成器** – UI 组件，使用表单 JSON 模式将表单渲染为 PDF，可填充收集的响应数据，并支持导出为可编辑或预填 PDF。
- ♿ **无障碍支持** – 表单库和调查创建器完全符合 WCAG、Section 508 和 ARIA 标准，支持键盘导航和屏幕阅读器。
- ∞ **无使用限制** – 无管理员、受访者、表单数量、提交次数或功能限制，所有数据存储在自有数据库中。
- 🔧 **自定义输入字段** – 可定义自定义独立或复合问题类型，或集成 Angular、React、Vue 3 组件创建高级可重用输入控件。
- 📴 **离线数据收集** – 支持完全离线工作，表单、主题和响应本地存储，恢复在线后自动同步数据。
- 💳 **一次性购买许可** – 开发者一次性购买即可永久使用调查创建器、PDF 生成器和仪表板，包含 12 个月免费维护。
- ✅ **自定义数据验证** – 支持超越基础验证器的自定义客户端规则和服务器端检查，使用 JavaScript 函数和事件处理器实现。
- 🔓 **开源与白标** – 所有库开源（GitHub 提供），支持 React、Angular、Vue 3 和原生 JS，可完全控制表单外观和样式自定义。
- 🤖 **AI 辅助** – 通过 API 集成 AI，支持自然语言表单生成、翻译和智能内容建议，提升表单构建效率。
- 🏢 **多行业适用** – 服务于保险、医疗、市场研究、教育、人力资源、电商、客户体验、非营利组织和银行等行业，满足敏感数据收集与合规需求。
- 🔒 **安全数据收集** – 支持自托管，确保数据流完全在自有基础设施内控制，保障隐私并满足 HIPAA、FERPA、GDPR 等法规要求。
- 🔄 **前后端分离** – 仅提供前端 UI 库，需自行构建后端处理数据存储、用户管理和业务逻辑，保持对数据和后端的完全控制。

---

### [Shadcn 单选按钮令人难以置信的过度复杂性](https://paulmakeswebsites.com/writing/shadcn-radio-button/)

**原文标题**: [The Incredible Overcomplexity of the Shadcn Radio Button](https://paulmakeswebsites.com/writing/shadcn-radio-button/)

作者在尝试更新网页应用中的单选按钮样式时，发现项目使用了 Shadcn 组件库中的复杂 React 组件，这引发了对现代前端开发过度复杂化的反思。通过分析 Shadcn 依赖 Radix UI 库的实现方式，揭示了用 ARIA 角色模拟原生 HTML 元素的反模式，并对比了仅用 CSS 轻松定制样式的简洁方案。文章批判了当前为简单交互引入多层抽象导致的性能负担和认知负荷，倡导回归浏览器原生元素的简洁与高效。

- 🎨 **样式定制本可简单**：仅需 CSS 的`appearance: none`和伪元素即可完全自定义单选按钮样式，无需 JavaScript 或额外依赖
- 🏗️ **层层抽象增加复杂度**：Shadcn 基于 Radix UI 构建，两个库叠加导致理解单个组件需阅读数百行代码
- ⚠️ **违反无障碍最佳实践**：用 ARIA 角色将按钮模拟成单选按钮，违背“优先使用原生语义元素”的 WAI-ARIA 第一准则
- 📦 **隐性性能成本**：为渲染简单控件需加载第三方图标库和大量 JavaScript，增加页面体积与解析时间
- 🔄 **历史遗留问题已解决**：跨浏览器样式不一致问题多年前已通过标准 CSS 方案解决，复杂重构不再必要
- ⚖️ **开发便利的代价**：组件库虽降低 CSS 学习成本，但引入了依赖管理、版本升级和抽象泄漏等新问题
- 🌐 **原生元素的优雅**：`<input type="radio">`作为 30 年历史的浏览器原生元素，兼具语义完整、零依赖与即时渲染优势

---

### [Shadcn 单选按钮的过度复杂性 | Hacker News](https://news.ycombinator.com/item?id=46688971)

**原文标题**: [The Overcomplexity of the Shadcn Radio Button | Hacker News](https://news.ycombinator.com/item?id=46688971)

本文讨论了 Shadcn UI 库中单选按钮组件的过度复杂性问题，指出其实现方式远超出原生 HTML 单选按钮的简洁性，并引发了关于现代前端开发中过度依赖框架和抽象导致代码臃肿的广泛讨论。

- 🎯 **核心问题**：Shadcn 的单选按钮组件使用了大量不必要的 JavaScript 和依赖，而现代 CSS 已能轻松实现相同样式。
- 🔄 **框架争议**：许多评论者认为 React 等框架虽提供了便利，但也导致开发者忽视了原生 Web 技术（HTML/CSS）的能力。
- 🛠️ **替代方案**：建议优先使用原生 HTML 元素配合现代 CSS 进行样式定制，或选择更轻量的库如 Basecoat UI。
- 📉 **性能影响**：过度复杂的组件会增加加载时间、维护成本，并可能影响用户体验和可访问性。
- 🤔 **行业反思**：讨论揭示了前端开发中普遍存在的“过度工程化”现象，呼吁在项目需求与解决方案复杂度间取得平衡。

---

### [React 巴黎：React，魔法般的魅力！](https://react.paris/)

**原文标题**: [React Paris: React C'est Magique!](https://react.paris/)

React Paris 2026 是一场为期两天的单轨道 React 技术大会，将于 2026 年 3 月 26 日至 27 日在巴黎举行。大会汇聚了来自全球的开发者、团队负责人和顾问，旨在提供启发、学习和交流的机会。内容涵盖 React 服务器组件、AI、设计系统、性能、状态管理、Remix、TypeScript 等前沿话题，并包含实践研讨会、顶尖演讲者分享以及丰富的社交活动。

- 🗓️ **活动时间**：2026 年 3 月 26 日至 27 日，为期两天。
- 🎤 **演讲阵容**：已公布超过 22 位顶尖演讲者，包括来自 IBM、Google、Tesla 等公司的专家。
- 🚀 **核心议题**：涵盖 React 服务器组件、AI、设计系统、性能优化、状态管理、Remix、TypeScript 等热门技术。
- 🤝 **活动形式**：单轨道会议，包含主题演讲、闪电演讲、交流会、会前聚会及派对等环节。
- 🎫 **门票类型**：提供线下实体票（含独家现场内容）和在线票两种选择。
- 📍 **会议地点**：巴黎蒙帕纳斯铂尔曼酒店，拥有宽敞明亮的会议空间。
- 🎥 **往届回顾**：提供了 2024 年和 2025 年大会的精彩回顾视频，展示社区活力与成长。
- 🤲 **社区与赞助**：由 BeJS 组织，拥有包括 Figma、Resend 在内的多家赞助商，并设有多元化奖学金计划。

---

### [微收成：温馨农场应用 - App Store](https://apps.apple.com/us/app/tiny-harvest-cozy-farm/id6755226300)

**原文标题**: [âTiny Harvest: Cozy Farm App - App Store](https://apps.apple.com/us/app/tiny-harvest-cozy-farm/id6755226300)

《Tiny Harvest》是一款专为 iPhone 设计的休闲放置类农场模拟游戏，玩家可以轻松打造梦想农场，通过种植、制作、探索和社交等多元玩法享受宁静的田园体验。

- 🌱 种植多样作物并收获资源，体验农场经营的核心乐趣
- 🛠️ 将原材料加工成各类商品，并通过升级建筑解锁新配方
- 📦 完成每日订单赚取金币与经验，逐步成为区域最佳农场主
- 🗺️ 派遣探险者前往不同地区，收集黏土、浆果等稀有材料
- 🏗️ 扩建并升级农场建筑，实现离线收益与资源产出
- 👥 添加好友互助合作，通过每日协助获得额外奖励
- 🧚 解锁伴随农场成长的魔法精灵，获取增益效果
- ⏳ 无压力节奏与碎片化设计，适合短时放松或长时间沉浸
- 📱 仅限 iOS 平台，含内购项目，开发者持续更新优化体验
- ⭐ 玩家评价积极，赞赏其简约界面与持续的内容改进

---

### [微小的收获 - Google Play 上的应用](https://play.google.com/store/apps/details?id=com.supersimon.harvestgame)

**原文标题**: [Tiny Harvest - Apps on Google Play](https://play.google.com/store/apps/details?id=com.supersimon.harvestgame)

《Tiny Harvest》是一款休闲农场模拟游戏，玩家通过种植作物、制作物品、完成订单和探索冒险，逐步发展自己的小农场，享受轻松无压力的游戏体验。

- 🌱 种植多样作物：种植数十种独特作物，按时收获以维持农场运转
- 🛠️ 制作实用物品：将原材料加工成面粉、绳索等商品，升级建筑解锁新配方
- 📦 完成订单赚取奖励：通过每日订单获得金币、经验值和资源
- 🗺️ 探索不同区域：派遣探险队前往森林、河畔等地收集稀有材料
- 🏗️ 扩建升级农场：添加并升级建筑，实现离线收益
- 👥 好友互助系统：通过好友代码互相帮助，获得额外奖励
- 🧚 农场精灵伙伴：解锁魔法伴侣，随农场成长提供增益效果
- ☁️ 轻松休闲体验：无压力游戏设计，支持短时或长时游玩，适合喜爱农场模拟和放置类游戏的玩家

---

### [场景测试](https://scenetest.github.io/scenetest-js/)

**原文标题**: [Scenetest](https://scenetest.github.io/scenetest-js/)

Scenetest 是一个面向 Vite 应用的本地优先测试框架，旨在通过将断言直接嵌入应用代码来测试应用的实际状态与数据层，而非仅依赖 DOM 操作。它利用 React 生命周期和 Server Actions 模式，实现类型安全的多上下文断言，从而更自然地验证应用逻辑。

- 🎯 **测试理念革新**：传统测试依赖浏览器模拟操作，而 Scenetest 直接测试组件状态、本地数据库等数据层，确保应用核心逻辑被验证。
- 🔧 **内联断言**：通过 `should`、`failed` 和 `assert` 函数在组件、钩子中嵌入测试代码，类型安全且在生产环境中自动移除，无运行时开销。
- 🌐 **多上下文比较**：利用 Server Actions 模式，在 React 生命周期中触发断言，对比客户端状态与服务器数据，避免传统测试中繁琐的 `window` 对象暴露。
- 🧩 **场景测试**：通过 `scene` 定义用户流程（如更新个人资料），自动化交互步骤，同时内联断言自动执行，无需手动编写额外验证。
- ⚡ **开发体验优化**：测试代码与应用逻辑共存，减少重复断言和抽象层，使测试更贴近实际使用场景，提升维护性和可靠性。
- 🚀 **早期项目**：Scenetest 目前处于开发初期，鼓励开发者通过 GitHub 或社交媒体反馈意见。

---

### [GitHub - sailscastshq/boring-stack：使用久经考验的技术，数日内而非数周内交付JavaScript产品。](https://github.com/sailscastshq/boring-stack)

**原文标题**: [GitHub - sailscastshq/boring-stack: Ship JavaScript products with battle-tested technologies in days not weeks.](https://github.com/sailscastshq/boring-stack)

Boring JavaScript Stack 是一个基于成熟技术的全栈 JavaScript 项目启动器，旨在帮助开发者快速构建和交付可靠的 JavaScript 应用，避免追逐技术潮流带来的复杂性。

- 🚀 使用 `npx create-sails <项目名>` 快速启动，支持 Vue、React 或 Svelte 前端框架
- 🛠️ 技术栈包括 Sails、Inertia 和 Tailwind CSS，无需客户端状态管理或额外 API
- ⚡ 通过 Inertia 实现后端直接向前端页面传递数据，无需双重路由
- 🌐 提供在线 StackBlitz 模板，可直接在浏览器中试用 Vue、React 和 Svelte 版本
- 📚 详细文档和社区支持，包括 GitHub 讨论、问题反馈和功能建议渠道
- 🤝 由 Kelvin Omereshone 主导开发，遵循“专注于向真实用户交付产品”的理念

---

### [深入 Turbopack：通过减少构建实现更快的构建速度 | Next.js](https://nextjs.org/blog/turbopack-incremental-computation)

**原文标题**: [Inside Turbopack: Building Faster by Building Less | Next.js](https://nextjs.org/blog/turbopack-incremental-computation)

Turbopack 是 Next.js 的新默认打包工具，采用增量计算和细粒度缓存架构，旨在实现大规模 Web 应用的即时构建和快速开发体验。其核心通过自动追踪函数依赖关系，仅重新计算受变更影响的部分，从而显著提升性能。

- 🚀 **增量架构优化**：Turbopack 基于增量计算设计，通过缓存和细粒度依赖跟踪，仅针对变更部分重新计算，避免全量编译，提升大型应用构建速度。
- 🔧 **自动化依赖追踪**：引入“值单元格”（Vc<…>）概念，自动记录函数执行与数据依赖关系，实现比传统手动声明依赖更精准的缓存，减少人为错误。
- 📊 **聚合图高效查询**：在依赖图之上构建聚合图，分层汇总子图信息，优化对错误收集、脏节点检测等操作的查询效率，支持海量中间结果的快速遍历。
- 💾 **文件系统缓存持久化**：从 Next.js 16.1 开始，默认启用稳定的文件系统缓存，将依赖图、聚合图及中间结果持久化到磁盘，实现开发服务器快速热启动。
- ⚡ **按需驱动执行**：采用需求驱动机制，仅当脏函数涉及活跃查询（如打开的网页或生产构建请求）时才触发重新计算，减少不必要的计算开销。
- 🌍 **灵感源于多领域研究**：架构借鉴了 Rust-Analyzer 的 Salsa、Parcel、Rust 编译器查询系统等前沿成果，结合 webpack 实践经验，专注于解决大规模应用构建性能瓶颈。

---

### [适应 React 编译器的库逻辑调整 | 趣味编程](https://playfulprogramming.com/posts/react-compiler-library-support/)

**原文标题**: [
	Adapting Library Logic for React Compiler | Playful Programming
](https://playfulprogramming.com/posts/react-compiler-library-support/)

本文探讨了在启用 React Compiler 时，TanStack Form 库遇到的边缘情况问题，包括如何检测和修复由编译器优化导致的 bug，以及如何调整库逻辑以兼容编译器。

- 🐛 在启用 React Compiler 后，当包含可变对象的 hook 返回值传递给子组件时，会导致状态更新失效，而 ESLint 未能完全捕获此类问题。
- 🔍 通过分析编译器生成的代码，发现问题的根源在于编译器对对象引用稳定性的优化策略与直接修改状态对象的行为不兼容。
- ⚙️ 使用`panicThreshold: 'all_errors'`配置可以强制 React Compiler 报告所有优化问题，帮助开发者更全面地检测潜在错误。
- 🛠️ 修复方案是避免直接修改状态对象，转而使用`useMemo`创建新的对象引用，确保编译器能正确跟踪依赖并触发更新。
- 📚 文章还讨论了 TanStack Form 采用类结构实现跨框架支持的设计思路，以及如何通过调整构建配置来模拟依赖库的编译排除场景。

---

### [使用 useMemo 和 useCallback 提升 React 性能 | DebugBear](https://www.debugbear.com/blog/react-usememo-usecallback)

**原文标题**: [Improve React Performance With useMemo And useCallback | DebugBear](https://www.debugbear.com/blog/react-usememo-usecallback)

本文探讨了如何利用 `useMemo` 和 `useCallback` 这两个 React 钩子来优化应用性能，解释了它们的工作原理、适用场景以及最佳实践，旨在帮助开发者避免不必要的重新渲染和计算开销。

- 🚀 `useMemo` 用于缓存**计算结果**，避免在每次渲染时重复执行昂贵的计算，仅当依赖项变化时才重新计算。
- 🔗 `useCallback` 用于缓存**函数引用**，确保函数在依赖项未变时保持稳定，防止因引用变化导致子组件不必要的重新渲染。
- ⚠️ 两者都应谨慎使用，仅在存在可测量的性能问题时才考虑，避免过度优化。
- 📊 优化前应先使用 React DevTools 等工具进行性能测量，确保优化针对实际瓶颈。
- 🛠️ 结合 `React.memo` 使用 `useCallback` 可有效避免子组件因函数引用变化而重新渲染。
- 📈 推荐使用函数式状态更新来配合 `useCallback`，以减少依赖项并避免闭包陷阱。
- 📚 可参考 Vercel 的 React 性能规则等资源，深入学习性能优化最佳实践。

---

### [构建具有真正离线支持的 Next.js 16 PWA - LogRocket 博客](https://blog.logrocket.com/nextjs-16-pwa-offline-support/)

**原文标题**: [Build a Next.js 16 PWA with true offline support - LogRocket Blog](https://blog.logrocket.com/nextjs-16-pwa-offline-support/)

本文介绍了如何使用 Next.js 16 构建一个具备真正离线支持的渐进式 Web 应用（PWA），通过服务工作者、IndexedDB 和同步机制实现离线数据操作与网络恢复后的自动同步。

- 🛠️ **超越基础应用外壳**：真正的离线支持不仅缓存静态资源，还能在无网络时处理用户操作，使用 IndexedDB 本地存储数据，并在网络恢复后自动同步。
- 📦 **技术栈配置**：使用 Serwist 替代 next-pwa，结合 Next.js 16 配置服务工作者，通过 IndexedDB 存储结构化数据，并利用 idb 库简化操作。
- 🔄 **同步机制实现**：通过在线事件监听和同步函数，检测网络恢复后自动同步未上传的数据，确保离线操作的数据一致性。
- 🧩 **组件化开发**：构建 TodoList 组件管理本地任务，添加在线状态指示器，提升用户在离线环境下的操作反馈与体验。
- ⚠️ **常见问题与优化**：注意服务工作者更新策略、HTTPS 部署要求及 iOS Safari 的限制，未来可通过后台同步 API、推送通知和冲突解决机制进一步优化。

---

### [错误](https://react.statuscode.com/link/179748/web)

**原文标题**: [Error](https://react.statuscode.com/link/179748/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='github.com', port=443): Max retries exceeded with url: /darula-hpp/shimmer-from-structure (Caused by ProxyError('Unable to connect to proxy', RemoteDisconnected('Remote end closed connection without response')))

---

### [TimescaleDB：排名第一的 PostgreSQL 时序数据库 | 开源与云端 | Tiger Data](https://www.tigerdata.com/timescaledb?utm_source=cooperpress&utm_medium=referral&utm_campaign=react-status-newsletter)

**原文标题**: [TimescaleDB: #1 PostgreSQL Time-Series Database | Open Source & Cloud | Tiger Data](https://www.tigerdata.com/timescaledb?utm_source=cooperpress&utm_medium=referral&utm_campaign=react-status-newsletter)

TimescaleDB 是一款基于 PostgreSQL 构建的时序数据库，专为处理传感器、链上及客户数据而设计，提供实时分析、大规模压缩存储及完全兼容 PostgreSQL 的功能。它支持自动分区、行列混合存储、高达 95% 的压缩率、增量物化视图等核心能力，适用于物联网、金融科技和实时分析等场景，并提供云端托管和自托管两种部署方式。

- 🚀 **高性能时序处理**：通过自动分区（Hypertables）和行列混合存储，实现快速数据摄入与高效查询，支持大规模时序数据分析。
- 💾 **智能存储与压缩**：提供高达 95% 的数据压缩率，并支持自动分层存储，显著降低历史数据存储成本，同时提升查询速度。
- 🔄 **实时分析能力**：借助增量物化视图（Continuous Aggregates）和时序专用函数，支持实时仪表盘和复杂时序分析，无需全量数据重处理。
- ☁️ **云端托管优势**：Tiger Cloud 提供一键部署、自动扩展、高可用架构、安全合规支持及按需计费，简化运维并降低资源闲置成本。
- 🛠️ **灵活部署选项**：支持自托管（社区/企业版）和全托管云服务，保留 PostgreSQL 完整生态，兼容 SQL 查询、地理空间及向量数据类型。
- 📊 **多行业应用场景**：广泛应用于物联网设备监控、金融科技高频数据分析和实时客户洞察等领域，受 Cloudflare、Replicated 等企业信赖。
- 🔧 **全面管理与支持**：提供自动化数据管理、作业调度、性能监控工具及 24/7 专家技术支持，助力用户从原型开发到大规模生产部署。

---

### [🚀React Native Windows v0.81 现已发布！！React Native](https://devblogs.microsoft.com/react-native/%f0%9f%9a%80react-native-windows-v0-81-is-here/)

**原文标题**: [🚀React Native Windows v0.81 is here!! React Native](https://devblogs.microsoft.com/react-native/%f0%9f%9a%80react-native-windows-v0-81-is-here/)

总结失败：Connection error.

---

### [获取失败](https://react.statuscode.com/link/179751/web)

**原文标题**: [Failed to retrieve](https://react.statuscode.com/link/179751/web)

无法总结：获取内容失败，状态码 429。

---

### [json-render | 带防护机制的 AI 生成 UI](https://json-render.dev/)

**原文标题**: [json-render | AI-generated UI with guardrails](https://json-render.dev/)

该工具通过 AI 将用户自然语言描述转换为受组件目录约束的 JSON 结构，并实时渲染为 UI 界面，同时支持导出为独立 React 代码。

- 🧱 **定义组件目录**：开发者预先定义可用的组件、操作与数据绑定规则，为 AI 生成设定边界。
- 🤖 **AI 生成 JSON**：用户输入需求描述后，AI 输出符合目录规范的 JSON 结构，确保生成内容可控。
- 🎨 **实时渲染 UI**：支持流式响应，JSON 数据可逐步渲染为可视化界面。
- 💻 **导出独立代码**：可将生成的 UI 导出为完整的 React 项目（如 Next.js），包含所有组件与依赖，无需运行时库。
- 🔒 **功能特性**：包括目录约束、流式渲染、双向数据绑定、条件显示与自定义操作处理。

---

### [GitHub - zoontek/react-native-bootsplash: 🚀 应用启动时显示启动画面，准备就绪后隐藏。](https://github.com/zoontek/react-native-bootsplash)

**原文标题**: [GitHub - zoontek/react-native-bootsplash: 🚀 Show a splash screen during app startup. Hide it when you are ready.](https://github.com/zoontek/react-native-bootsplash)

这是一个用于 React Native 的启动屏（Splash Screen）库，可在应用启动时显示自定义启动画面，并在应用准备就绪后隐藏。它支持 Android、iOS 和 Web 平台，提供 CLI 工具快速生成资源文件，并包含丰富的配置选项，如深色模式、品牌标识集成等。

- 🚀 **功能概述**：在 React Native 应用启动时显示启动屏，支持自定义隐藏时机与动画效果。
- 📦 **安装与支持**：通过 npm 或 yarn 安装，遵循 React Native 版本支持策略，兼容最新及前两个次要版本。
- 🛠️ **快速设置**：提供 CLI 工具自动生成多平台资源文件（如图片、配置文件），支持自定义背景色、Logo 尺寸等。
- 🔑 **高级功能**：通过许可证密钥解锁品牌标识集成、深色模式资源生成等高级选项，可批量生成超 50 个文件。
- 📱 **平台集成**：详细说明 Android 与 iOS 的本地代码配置步骤，包括与 `react-native-screens` 的兼容处理。
- ⚙️ **API 使用**：提供 `hide()`、`isVisible()` 和 `useHideAnimation()` 等方法，支持自定义隐藏动画与状态管理。
- ❓ **常见问题**：涵盖系统栏颜色设置、React Navigation 集成、测试模拟等实用解决方案。
- 🌐 **社区与支持**：开源项目，接受赞助与企业级支持，拥有活跃的社区贡献与更新记录。

---

### [罗克帕克](https://alexsergey.github.io/rockpack/)

**原文标题**: [Rockpack](https://alexsergey.github.io/rockpack/)

Rockpack 是一个轻量级、零配置的解决方案，能快速搭建支持服务器端渲染（SSR）、打包、代码检查和测试的 React 应用，让开发者在 5 分钟内启动一个现代化、性能优化的 React 项目。

- 🚀 **零配置启动**：无需复杂设置，立即开始构建应用。
- 🌐 **内置 SSR 支持**：无缝集成服务器端渲染，提升 SEO 和首屏加载速度。
- 📦 **智能打包**：开箱即用的打包功能，优化性能。
- ✅ **自动代码检查**：通过内置的代码检查和风格检查保持代码质量。
- 🧪 **预置测试环境**：集成 Jest 等流行工具，配置完善的测试环境。
- 🔧 **高度可扩展**：轻松自定义以满足更高级的开发需求。
- ⚙️ **快速入门**：通过 `@rockpack/starter` 模块一键生成项目骨架，支持单页应用、SSR、纯 React 项目等多种类型。

---

### [GitHub - marmelab/react-admin：基于REST/GraphQL API 的单页应用前端框架，采用 TypeScript、React 和 Material Design](https://github.com/marmelab/react-admin)

**原文标题**: [GitHub - marmelab/react-admin: A frontend Framework for single-page applications on top of REST/GraphQL APIs, using TypeScript, React and Material Design](https://github.com/marmelab/react-admin)

React-admin 是一个基于 TypeScript、React 和 Material Design 的前端框架，用于在 REST/GraphQL API 之上构建单页面应用。它提供丰富的组件和钩子，支持高度定制，并拥有活跃的社区和商业支持。

- 🔌 **后端无关**：可连接任何 REST 或 GraphQL API，提供超过 45 种适配器
- 🧩 **功能全面**：内置认证、路由、表单、数据表格、搜索过滤、国际化等完整功能模块
- 🪡 **高质量标准**：注重可访问性、响应式设计、安全性和性能
- 💻 **优秀开发体验**：完整文档、TypeScript 支持、Storybook 演示和模块化架构
- 👑 **卓越用户体验**：支持乐观渲染、实时过滤、撤销操作和偏好设置
- 🛠 **高度可定制**：允许替换任何组件以满足特定需求
- 📦 **易于安装**：通过 npm 或 yarn 即可安装，快速开始项目开发
- 📚 **丰富示例**：提供电商、CRM、博客等多个演示项目供参考
- 🤝 **活跃社区**：拥有 Discord、StackOverflow 等社区支持渠道
- 🔄 **持续维护**：采用 master/next 分支策略，定期发布更新版本

---

### [发布 v3.7.0 · recharts/recharts · GitHub](https://github.com/recharts/recharts/releases/tag/v3.7.0)

**原文标题**: [Release v3.7.0 · recharts/recharts · GitHub](https://github.com/recharts/recharts/releases/tag/v3.7.0)

Recharts 发布了 v3.7.0 版本，主要包含新功能、改进、修复和文档更新，同时引入了两个新钩子并弃用了 Cell 组件。

- 📢 Cell 组件已弃用，将在下一个主要版本中移除，建议迁移至相应图表元素的 shape 属性。
- 🆕 新增 useIsTooltipActive 和 useActiveTooltipCoordinate 钩子，分别用于检测工具提示活动状态和获取当前坐标。
- 🔧 Tooltip 组件的 offset 属性现在支持 Coordinate 对象，增强了灵活性。
- 📊 X/YAxis 新增 "auto" 轴类型，能自动根据数据选择 "category" 或 "number" 类型。
- 🛠️ 修复了 BarChart 在多个正值系列中的堆叠偏移问题，并解决了 BarStack 的循环依赖和裁剪路径错误。
- 📚 文档现已自动生成，提高了准确性，并新增了深色模式支持。
- 👏 感谢新贡献者 @jkr2255、@cloud-walker、@bigsaigon333 和 @huangkevin-apr 的首次贡献。

---

### [Recharts](https://recharts.github.io/en-US/examples/)

**原文标题**: [Recharts](https://recharts.github.io/en-US/examples/)

本文介绍了多种图表类型及其交互功能示例，用户可通过点击类别查看实际效果。

- 📊 探索不同图表类型和功能的交互示例
- 📈 包含折线图、面积图、条形图等九种图表类型
- 🖱️ 支持通过点击分类查看实际演示效果
- 💡 提供提示：悬停图例可查看详细信息
- 📱 强调响应式容器适配不同设备显示

---

### [错误](https://react.statuscode.com/link/179758/web)

**原文标题**: [Error](https://react.statuscode.com/link/179758/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='github.com', port=443): Max retries exceeded with url: /vercel/next.js/releases/tag/v16.2.0-canary.5 (Caused by ProxyError('Unable to connect to proxy', RemoteDisconnected('Remote end closed connection without response')))

---

### [发布 v16.1.4 · vercel/next.js · GitHub](https://github.com/vercel/next.js/releases/tag/v16.1.4)

**原文标题**: [Release v16.1.4 · vercel/next.js · GitHub](https://github.com/vercel/next.js/releases/tag/v16.1.4)

Next.js 发布了 v16.1.4 版本，这是一个主要针对 bug 修复的向后移植版本，不包含 canary 分支中所有待定的新功能或变更。

- 🔧 **核心变更**：仅当实验性标志启用时才过滤 Next 配置（#88733）
- 🙏 **致谢**：特别感谢 @mischnic 的贡献
- 👥 **贡献者**：mischnic
- 📅 **发布时间**：2024 年 1 月 19 日 23:43
- 🏷️ **版本状态**：基于 canary 分支的 348 次提交，属于稳定修复版本

---

### [宣布 Rolldown 1.0 RC 版本发布 | VoidZero](https://voidzero.dev/posts/announcing-rolldown-rc)

**原文标题**: [Announcing Rolldown 1.0 RC | VoidZero](https://voidzero.dev/posts/announcing-rolldown-rc)

Rolldown 1.0 发布候选版本正式推出，这是一个基于 Rust 开发的高性能 JavaScript 打包工具，旨在成为 Vite 的未来默认打包器。它兼容 Rollup 插件生态，性能比 Rollup 快 10-30 倍，并引入了如精细化代码分割等新特性。当前版本标志着 API 已进入稳定阶段，鼓励开发者试用并提供反馈。

- 🚀 **性能飞跃**：基于 Rust 构建，比 Rollup 快 10-30 倍，支持并行处理与 WASM 跨平台构建
- 🔌 **生态兼容**：完全兼容 Rollup 插件 API，现有插件无需修改即可使用
- ⚙️ **内置功能**：集成 TypeScript、JSX 转换、Node.js 模块解析，无需额外插件
- 🧩 **高级代码分割**：提供类似 webpack 的精细化代码分割控制，支持动态导入优化
- 🧪 **实验特性**：部分功能如模块类型、监听模式仍处于实验阶段，需谨慎用于生产
- 📦 **Vite 集成**：Vite 8 测试版已默认采用 Rolldown，统一开发与生产构建流程
- 📈 **持续优化**：自测试版以来已修复大量问题，性能与兼容性持续提升
- 🌍 **社区驱动**：由 150 多位贡献者共同开发，欢迎通过 GitHub 和 Discord 参与反馈

---

### [shadcn/ui 主题兼容性](https://clerk.com/changelog/2025-07-23-shadcn-theme?utm_source=cooper_press&utm_medium=newsletter&utm_campaign=shadcn-theme&utm_content=01-23-26&dub_id=98wn4zzZUkWV1H6h)

**原文标题**: [shadcn/ui theme compatibility](https://clerk.com/changelog/2025-07-23-shadcn-theme?utm_source=cooper_press&utm_medium=newsletter&utm_campaign=shadcn-theme&utm_content=01-23-26&dub_id=98wn4zzZUkWV1H6h)

Clerk 推出了基于 shadcn/ui 的新主题，使 Clerk 的认证组件能够自动匹配用户现有的 shadcn/ui 主题配置，从而确保认证界面与应用整体风格一致。

- 🎨 Clerk 推出基于 shadcn/ui 的新主题，使认证组件能自动匹配应用现有主题
- 🛠️ 该主题基于 CSS 变量支持构建，确保认证界面与应用风格原生融合
- 📦 通过安装 @clerk/themes 包并配置 ClerkProvider 即可使用此主题

---

### [注册 - Auth0](https://auth0.com/signup?onboard_app=auth_for_aa&ocid=701KZ000000cXXxYAM_aPA4z0000008OZeGAM?utm_source=cooperpress&utm_campaign=amer_namer_usa_all_ciam_dev_dg_plg_auth0_native_cooperpress_native_aud_jan_2026_placements_utm2&utm_medium=cpc&utm_id=aNKWR000002m8zp4AA)

**原文标题**: [Sign Up - Auth0](https://auth0.com/signup?onboard_app=auth_for_aa&ocid=701KZ000000cXXxYAM_aPA4z0000008OZeGAM?utm_source=cooperpress&utm_campaign=amer_namer_usa_all_ciam_dev_dg_plg_auth0_native_cooperpress_native_aud_jan_2026_placements_utm2&utm_medium=cpc&utm_id=aNKWR000002m8zp4AA)

Auth0 注册页面概述，提供免费账户注册服务，包含多种登录方式及开发者友好的安全功能。

- 📧 通过邮箱注册并同意营销通讯与隐私政策
- ✅ 注册需同意服务条款和隐私政策
- 🔐 支持 GitHub/Google/Microsoft 第三方快捷登录
- 🛡️ 提供 AI 代理安全连接与敏感操作人工审批功能
- 🆓 免费套餐含 2.5 万月活用户与可定制登录流程
- 🛠️ 配备暴力破解防护和渐进式用户画像功能
- 👨‍💻 专为各阶段开发者设计的身份验证平台

---

### [TypeScript AI 框架 - Mastra](https://mastra.ai/)

**原文标题**: [The Typescript AI framework - Mastra](https://mastra.ai/)

Mastra 是一个基于现代 TypeScript 技术栈构建 AI 应用和智能体的全栈框架，提供从开发、测试到部署的全流程工具。

- 🚀 **快速开始**：通过`npm create mastra@latest`命令即可创建项目，支持本地开发服务器和 JavaScript 编写智能体逻辑
- 🛠️ **核心功能**：提供智能体、工作流、RAG、记忆系统、工具集成和 MCP 支持，实现从创意到落地的完整开发流程
- 🔍 **开发体验**：内置可视化开发工作室，支持智能体和工作流的迭代与可视化调试
- 📊 **生产就绪**：提供可观测性平台，支持上下文调优、召回率改进，通过自定义评估实现人类级准确率
- 🧪 **评估体系**：支持模型评分、规则基和统计方法评估智能体输出，具备输入输出处理能力防止提示注入
- 🔒 **安全部署**：集成身份系统保护智能体端点，支持与 Next.js、Express、Hono 等框架无缝集成
- ☁️ **灵活架构**：Apache 2.0 开源协议，可部署为独立服务或与现有应用集成，支持 API 暴露和规模化部署
- 📚 **学习资源**：提供模板库、教程、工作坊和《智能体构建原则》电子书，涵盖浏览器自动化、代码生成、深度研究等实用场景
- 🎯 **社区生态**：拥有丰富的预构建模板和社区解决方案，包括 PDF 转音频、文本转 SQL、谷歌表格分析等实际应用案例

---

### [宣布 Mastra 1.0 版本发布！ - Mastra 博客](https://mastra.ai/blog/announcing-mastra-1)

**原文标题**: [Announcing Mastra 1.0! - Mastra Blog](https://mastra.ai/blog/announcing-mastra-1)

Mastra 1.0 稳定版正式发布，标志着这个开源 AI 代理框架经过 15 个月的快速发展与数月生产环境测试后，API 已趋于稳定。本次更新聚焦于提升生产环境运行体验，核心改进包括引入服务器适配器以简化部署、支持复合存储实现按域配置、全面兼容 AI SDK v6，并优化了处理器系统与工作流。该版本已应用于 Replit、PayPal 等企业的生产场景，下载量突破 30 万次/周，社区贡献者超 300 名。

- 🚀 **稳定版发布**：Mastra 1.0 结束 Beta 阶段正式发布，包含 94 项修复及多项新功能
- 🛠️ **生产优化**：重点改进部署流程、系统可观测性，并解决实际生产问题
- 🔌 **服务器适配器**：新增 Express/Hono/Fastify/Koa 适配器，可将 Mastra 无缝集成至现有 Node.js 服务
- 🗃️ **复合存储架构**：支持为不同数据域（如工作流、记忆）独立配置存储后端（如 Postgres、LibSQL）
- 🤖 **AI SDK v6 支持**：完全兼容 LanguageModelV3 模型与 ToolLoopAgent，保持向后兼容
- 🔄 **工作流增强**：优化线程克隆、处理器系统，并统一可观测性数据格式
- ⚠️ **破坏性变更**：调整工具执行签名、重构导入路径、重命名运行时上下文等，提供自动化迁移工具
- 📈 **生态增长**：周下载量超 30 万，GitHub 星标 19.8k，被 PayPal、Replit 等企业用于生产环境 AI 代理
- 🧭 **升级指南**：新项目可通过 CLI 快速创建，现有项目可使用 codemod 自动迁移至 1.0

---

### [Electron 40.0.0 | Electron](https://www.electronjs.org/blog/electron-40-0)

**原文标题**: [Electron 40.0.0 | Electron](https://www.electronjs.org/blog/electron-40-0)

Electron 40.0.0 正式发布，主要升级了 Chromium、Node.js 和 V8 的版本，并引入了多项新功能与改进，同时包含一些破坏性变更。

- 🚀 **核心组件升级**：Chromium 升级至 144.0.7559.60，Node.js 升级至 v24.11.1，V8 引擎升级至 14.4。
- ✨ **新增功能与改进**：包括支持 HDR 色彩空间、新增硬件加速检测 API、增强无障碍功能管理、支持动态 ESM 导入等。
- ⚠️ **破坏性变更**：渲染进程中直接使用剪贴板 API 已被弃用，macOS 调试符号文件改用 xz 压缩格式。
- 📅 **支持周期更新**：Electron 37.x.y 版本已结束支持，建议用户升级至新版。
- 🔮 **未来规划**：团队将继续跟进 Chromium、Node 和 V8 等核心组件的更新，维护项目发展路线。

---

### [2025 年网络年鉴](https://almanac.httparchive.org/en/2025/)

**原文标题**: [The 2025 Web Almanac](https://almanac.httparchive.org/en/2025/)

《2025 年网络年鉴》是 HTTP Archive 发布的年度网络状态综合报告，结合海量数据与行业专家洞察，涵盖页面内容、用户体验、发布与分发等 16 个主题领域。

- 📊 报告基于 HTTP Archive 对 1620 万个网站的月度测试数据，处理数据量达 244TB
- 📈 性能章节显示：桌面端 97% 网站达到良好交互响应（INP≤200 毫秒），但新功能普及呈现头部站点领先、长尾依赖 CMS 默认配置的不均衡态势
- 🎯 核心发现包括：87% 移动页面使用至少一种网络字体，顶级桌面页面卸载处理器使用率较 2024 年下降 7 个百分点至 28%
- 👥 由 72 名志愿者共同完成，涵盖规划、研究、撰写及制作全流程
- 🔍 采用 WebPageTest 和 Lighthouse 技术栈，所有数据均开放于 BigQuery 公共数据库供深度分析

---

### [错误](https://react.statuscode.com/link/179767/web)

**原文标题**: [Error](https://react.statuscode.com/link/179767/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='react.statuscode.com', port=443): Max retries exceeded with url: /link/179767/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [性能 | 2025 | HTTP Archive 网络年鉴](https://almanac.httparchive.org/en/2025/performance)

**原文标题**: [Performance | 2025 | The Web Almanac by HTTP Archive](https://almanac.httparchive.org/en/2025/performance)

本文分析了 2025 年网页性能现状，重点关注核心网页指标（Core Web Vitals）的进展与挑战。数据显示，网页加载速度、交互性和视觉稳定性整体呈改善趋势，但移动与桌面性能差距依然存在，且不同流行度的网站在优化重点和采用新技术方面呈现分化。

- 📈 **核心网页指标持续改善**：2025 年，48% 的移动网站和 56% 的桌面网站达到良好标准，移动端进步显著，但桌面端增长放缓。
- 📱 **移动与桌面性能差距**：在加载速度（LCP）和交互性（INP）方面，移动端仍落后于桌面端，但 INP 的差距正在缩小。
- 🏆 **热门网站引领交互优化**：前 1,000 名网站在 INP 上提升最快（从 53% 升至 63%），显示其对用户体验的重视。
- 🏠 **首页与次级页面表现差异**：次级页面因缓存优势，在加载速度（LCP）上通常优于首页；但首页在交互性（INP）上反超，可能因优化更集中。
- 🖼️ **图像仍是性能关键**：绝大多数 LCP 元素为图像，但现代格式（如 WebP）采用缓慢，且约 17% 的页面错误地延迟加载 LCP 图像。
- ⚡ **交互性显著提升**：移动端 INP 达到 77%（较 2024 年上升 3%），但实验室指标 TBT 却恶化，反映 JavaScript 执行负担加重。
- 🧱 **视觉稳定性进步显著**：81% 的移动页面达到良好 CLS，但仍有大量页面存在未设置尺寸的图像（62%）和非合成动画（40%）。
- 🛠️ **新技术采用分化**：Early Hints 和 Speculation Rules 等新特性整体采用率低，但 Speculation Rules 在长尾网站（如 WordPress 站点）中更普及。
- 🔄 **性能优化基础仍存挑战**：许多网站仍未落实图像尺寸定义、字体预加载等基本最佳实践，显示优化深度不足。

---

### [错误](https://react.statuscode.com/link/179769/web)

**原文标题**: [Error](https://react.statuscode.com/link/179769/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='react.statuscode.com', port=443): Max retries exceeded with url: /link/179769/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [错误](https://react.statuscode.com/link/179770/web)

**原文标题**: [Error](https://react.statuscode.com/link/179770/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='react.statuscode.com', port=443): Max retries exceeded with url: /link/179770/web (Caused by ProxyError('Unable to connect to proxy', RemoteDisconnected('Remote end closed connection without response')))

---

### [ReactOS 30 年历程 | ReactOS 项目](https://reactos.org/blogs/30yrs-of-ros/)

**原文标题**: [30 years of ReactOS | ReactOS Project](https://reactos.org/blogs/30yrs-of-ros/)

ReactOS 项目庆祝其成立 30 周年，回顾了从 1996 年至今的发展历程，包括技术里程碑、社区贡献和未来发展方向。

- 🎂 ReactOS 于 1996 年启动，最初源自 FreeWin95 项目，旨在创建开源 Windows NT 克隆系统，首版 0.1.0 于 2003 年发布。
- 🛠️ 早期开发面临挑战，需从零构建 NT 内核和驱动，社区通过邮件列表协作，氛围友好开放。
- 🚀 2003-2006 年（0.2.x 版本）快速发展，添加桌面界面和稳定性提升，但曾因代码审计暂停贡献。
- 📉 2006-2016 年（0.3.x 版本）受审计影响进展放缓，但仍引入网络支持、包管理器和 x86_64 端口。
- 💻 2016 年至今（0.4.x 版本）推出新图形界面和内核调试支持，x86_64 版本功能接近 x86 但兼容性有限。
- 🔮 未来计划包括新构建环境、NTFS/ATA 驱动、多处理器支持、UEFI 和 GPU 驱动改进，鼓励社区通过捐赠、开发或测试参与。
- 📊 项目累计 8.8 万次提交、301 位贡献者、3.1 万文件及近 1500 万行代码，持续推动开源 Windows 兼容系统发展。

---

