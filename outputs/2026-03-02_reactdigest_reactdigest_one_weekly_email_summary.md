### [React 文摘：电子邮件通讯](https://reactdigest.net/)

**原文标题**: [React Digest: Email Newsletter](https://reactdigest.net/)

《React Digest》是一份为 React 开发者精心策划的每周通讯，汇集了超过 20,226 名前端软件工程师，通过精选文章和简短摘要帮助读者高效学习新知、节省时间。

- 📰 每周精选文章，附有简短摘要，帮助开发者快速获取有价值的内容
- ⏱️ 节省寻找优质内容的时间，提升学习效率
- 🧠 每周学习新知识，紧跟 React 技术发展动态
- 👥 拥有超过 20,226 名前端工程师订阅，形成专业社区
- 👍 读者反馈积极，认可其内容实用性和时效性

---

### [我们如何在一周内用 AI 重建 Next.js](https://blog.cloudflare.com/vinext/)

**原文标题**: [How we rebuilt Next.js with AI in one week](https://blog.cloudflare.com/vinext/)

上周，一位工程师与 AI 模型在一周内重建了最流行的前端框架 Next.js，推出了基于 Vite 的替代品 vinext。它可作为 Next.js 的即插即用替代方案，部署到 Cloudflare Workers 只需一条命令，初步测试显示生产构建速度提升高达 4 倍，客户端包体积减少 57%。项目总成本约 1100 美元。

- 🚀 **vinext 诞生**：基于 Vite 重建 Next.js API，支持现有 Next.js 项目无缝迁移，提供更快的构建速度和更小的包体积。
- ⚡ **性能优势**：生产构建速度比 Next.js 快 1.6 至 4.4 倍，客户端包体积减少 56%-57%。
- ☁️ **云部署优化**：专为 Cloudflare Workers 设计，支持一键部署，内置 KV 缓存实现增量静态再生（ISR）。
- 🔄 **框架兼容性**：95% 代码为纯 Vite 实现，支持多平台适配，已与 Vercel 等平台验证兼容。
- 🧪 **实验性阶段**：项目虽新，但已通过 1700+ 单元测试和 380+ 端到端测试，覆盖 Next.js 94% 的 API。
- 🤖 **AI 驱动开发**：借助 Claude 等 AI 模型，在不到一周内完成核心开发，凸显 AI 在复杂项目中的高效协作能力。
- 📊 **流量感知预渲染**：引入实验性功能，仅预渲染高流量页面，优化大型站点构建效率。
- 🌐 **开源生态**：项目完全开源，鼓励社区贡献，支持多平台扩展和定制化部署。

---

### [文员技能 - AI | 文员文档](https://clerk.com/docs/guides/ai/skills?utm_source=react-digest&utm_medium=newsletter&utm_campaign=skills&utm_content=03-02-26&dub_id=kno3zgSIx8P766P8)

**原文标题**: [Clerk Skills - AI | Clerk Docs](https://clerk.com/docs/guides/ai/skills?utm_source=react-digest&utm_medium=newsletter&utm_campaign=skills&utm_content=03-02-26&dub_id=kno3zgSIx8P766P8)

Clerk Skills 是可安装的扩展包，为 AI 编程助手提供 Clerk 相关的专业知识，帮助开发者集成身份验证、管理组织、同步用户等功能。

- 🧩 Clerk Skills 是 AI 助手的扩展包，提供 Clerk 专业知识
- 📦 可通过 `npx skills add clerk/skills` 安装全部或指定技能
- 🤖 支持 Claude Code、Cursor、Windsurf 等多种 AI 编程助手
- 📚 包含七种技能：基础路由、框架集成、自定义 UI、Next.js 模式、组织管理、Webhooks 和测试
- 💡 示例提示指导如何使用各技能，如添加身份验证、构建自定义表单等

---

### [React 医生](https://www.react.doctor/)

**原文标题**: [React Doctor](https://www.react.doctor/)

本文介绍了人工智能在医疗领域的应用现状与未来趋势，重点探讨了其在疾病诊断、药物研发、个性化治疗和医疗管理等方面的突破性进展，同时分析了面临的伦理挑战与技术瓶颈。

- 🩺 AI 辅助诊断系统通过影像识别技术提升疾病检测准确率，尤其在早期癌症筛查中表现突出
- 🔬 深度学习加速新药研发流程，大幅缩短化合物筛选与临床试验周期
- 📊 医疗大数据分析实现个性化治疗方案，根据患者基因特征动态调整用药策略
- 🤖 手术机器人完成精密微创操作，减少人为误差并提升复杂手术成功率
- 🛡️ 区块链技术保障医疗数据安全，解决患者隐私保护与数据共享的平衡难题
- ⚖️ 面临算法透明度不足与伦理审查机制缺失等挑战，需建立行业标准与监管框架

---

### [创建查询抽象](https://tkdodo.eu/blog/creating-query-abstractions)

**原文标题**: [Creating Query Abstractions](https://tkdodo.eu/blog/creating-query-abstractions)

本文探讨了在 React Query 中创建查询抽象的最佳实践，指出传统自定义钩子方法在类型安全和灵活性上的局限，并推荐使用`queryOptions`作为更优的抽象方案，以实现更好的类型推断和跨环境兼容性。

- 🛠️ 自定义钩子作为查询抽象存在局限，如类型推断复杂、无法在非组件环境使用，且难以适配不同 React Query 钩子。
- 🔧 使用`UseQueryOptions`类型进行抽象时，容易导致数据类型变为`unknown`，丧失类型安全性。
- 🧩 `queryOptions`函数是 React Query v5 推荐的抽象方式，它仅封装配置，可在任何环境使用，并保持完整的类型推断。
- 🧠 通过`queryOptions`创建的抽象不可配置，使用时可通过扩展选项灵活覆盖，简化代码并提升可维护性。
- 🚀 该方法支持与`useQuery`、`useSuspenseQuery`等多种钩子兼容，解决了自定义钩子与环境绑定的问题。

---

### [如何在 React Router 中通过 sergiodxa 创建多目录路由组织](https://sergiodxa.com/tutorials/create-a-multi-directory-route-organization-in-react-router)

**原文标题**: [How to Create a Multi-Directory Route Organization in React Router by sergiodxa](https://sergiodxa.com/tutorials/create-a-multi-directory-route-organization-in-react-router)

随着应用规模扩大，单一的路由文件夹会变得难以管理。通过将路由按逻辑拆分为多个目录，可以在保持每个目录内扁平化路由约定的同时，实现团队独立开发和代码库的清晰组织。

- 📁 **多目录结构组织**：将路由按功能或团队拆分为 `public/`、`app/`、`api/` 和 `actions/` 等子目录，每个目录内部仍遵循扁平化路由约定。
- ⚙️ **并行配置路由源**：使用 `flatRoutes()` 分别扫描各目录，结合 `Promise.all()` 并行加载，并通过 `prefix()` 为路由组添加路径前缀，保持构建效率。
- 🧩 **按区块共享布局**：在目录内使用 `_.tsx` 文件创建布局路由，使嵌套路由自动继承该布局，便于共享导航、样式或中间件。
- 🔗 **跨区块布局共享**：通过 `layout()` 包装多个路由组，实现在不同区块（如公开页面和应用路由）之间共享公共布局。
- 🔄 **跨目录依赖处理**：不同目录的路由可通过绝对路径相互引用，例如在应用路由中调用独立 `actions/` 目录的表单处理逻辑。
- 👥 **扩展至团队协作**：可按团队或功能模块划分目录（如 `marketing/`、`dashboard/`），每个团队独立管理自己的路由，通过中心 `routes.ts` 统一注册，便于扩展和维护。

---

### [响应式深度：使用 React Three Fiber 构建滚动驱动的 3D 图像管道 | Codrops](https://tympanus.net/codrops/2026/02/17/reactive-depth-building-a-scroll-driven-3d-image-tube-with-react-three-fiber/)

**原文标题**: [Reactive Depth: Building a Scroll-Driven 3D Image Tube with React Three Fiber | Codrops](https://tympanus.net/codrops/2026/02/17/reactive-depth-building-a-scroll-driven-3d-image-tube-with-react-three-fiber/)

本教程介绍如何使用 React Three Fiber 构建一个由滚动驱动、无限循环的 3D 图像管。通过结合着色器变形、惯性运动、确定性循环和同步 DOM 叠加，创建一个具有物理连贯性的 WebGL 体验。

- 🎯 **统一运动系统**：所有交互（滚动、鼠标移动、悬停）都影响同一套运动参数，确保场景元素协调一致
- 🏗️ **着色器驱动网格**：通过顶点着色器实现网格平面变形，根据鼠标位置和边缘距离平滑调整顶点高度
- 📐 **数学生成网格**：在片段着色器中用数学函数实时绘制抗锯齿网格线，避免纹理使用
- 🔄 **无缝垂直循环**：通过智能重定位实现图像管的无限滚动效果，消除视觉跳跃
- ⚡ **惯性阻尼系统**：滚动输入转化为旋转速度，每帧进行平滑阻尼处理，实现自然物理运动
- ⏱️ **时间缩放悬停**：悬停时通过缩放时间增量（dt）统一降低整个系统速度，保持物理连贯性
- 🚫 **事件传播控制**：合理阻止事件冒泡，防止交互冲突
- 🚀 **性能优化**：避免每帧重新渲染、无光线投射、无内存分配，保持帧率稳定

---

### [编码时实时无障碍测试 | 借助 AI 实现 WCAG 合规 | BrowserStack](https://www.browserstack.com/accessibility-testing/accessibility-devtools?utm_source=newsletter&utm_medium=PR&utm_platform=&utm_content=product-updates&utm_campaign=PR-A11y-Devtools&utm_campaigncode=701OW00000gNPyPYAW&utm_term=react-digest)

**原文标题**: [Real-time accessibility testing while coding | WCAG conformance with AI | BrowserStack](https://www.browserstack.com/accessibility-testing/accessibility-devtools?utm_source=newsletter&utm_medium=PR&utm_platform=&utm_content=product-updates&utm_campaign=PR-A11y-Devtools&utm_campaigncode=701OW00000gNPyPYAW&utm_term=react-digest)

BrowserStack Accessibility DevTools 是一款帮助开发者在编码时实时检测和修复网页可访问性问题的工具，通过集成到 IDE 或终端，利用 Spectra™ 规则引擎和 AI 辅助建议，确保代码在提交前符合 WCAG 标准，并支持多种开发环境和 CI/CD 集成。

- 🛠️ **实时检测**：在 IDE 或终端中即时发现可访问性问题，支持“左移”工作流，在开发阶段解决问题
- 🤖 **AI 辅助修复**：提供上下文感知的修复建议，直接在工作流中指导如何满足 WCAG 标准
- 🔌 **广泛集成**：支持 VS Code、IntelliJ、WebStorm 等多种主流 IDE 和 CLI 环境
- 🚫 **提交前拦截**：可扫描文件或目录，防止不符合可访问性标准的代码被提交到仓库或 CI/CD 流水线
- 🌐 **渲染代码测试**：通过 MCP 对渲染后的代码进行自动化扫描，并与 AI 工具连接获取修复建议
- 📊 **平台化测试**：提供完整的可访问性测试解决方案，包括报告、辅助分析和自动化审计，无需自建框架

---

### [获取失败](https://hacks.mozilla.org/2026/02/goodbye-innerhtml-hello-sethtml-stronger-xss-protection-in-firefox-148/)

**原文标题**: [Failed to retrieve](https://hacks.mozilla.org/2026/02/goodbye-innerhtml-hello-sethtml-stronger-xss-protection-in-firefox-148/)

无法总结：获取内容失败，状态码 403。

---

### [利用浏览器<canvas>进行数据压缩](https://jstrieb.github.io/posts/canvas-compress/)

**原文标题**: [Using the Browser’s <canvas> for Data Compression](https://jstrieb.github.io/posts/canvas-compress/)

本文介绍了一种利用浏览器 Canvas API 实现数据压缩的巧妙方法，尤其适用于需要在 JavaScript 前端进行数据压缩的场景，例如在单页应用（SPA）中将状态存储在 URL 哈希中时。

- 🖼️ 通过将数据编码为 PNG 图像并利用浏览器内置的图像压缩功能，间接实现数据压缩，即使考虑到 PNG 格式的开销，通常也能获得比原始数据更小的体积。
- 🔧 提供了具体的 JavaScript 代码示例，包括`compress`函数将 Uint8Array 压缩为 base64 字符串，以及异步的`decompress`函数进行解压。
- 🌐 该方法主要针对不支持现代 Compression Streams API 的旧版浏览器，提供了一种兼容性解决方案。
- 📄 文章最初发表于 2026 年 2 月 19 日，是为 Paged Out! 杂志第八期撰写的单页文章，并附有演示和测试文件。
- 🧪 包含一个演示页面和测试文件，用于验证压缩和解压代码的正确性，其中测试工具部分使用了大型语言模型辅助开发。

---

### [Oxfmt Beta | JavaScript 氧化编译器](https://oxc.rs/blog/2026-02-24-oxfmt-beta)

**原文标题**: [Oxfmt Beta | The JavaScript Oxidation Compiler](https://oxc.rs/blog/2026-02-24-oxfmt-beta)

Oxfmt 已进入 Beta 阶段，这是一款基于 Rust 构建、兼容 Prettier 的代码格式化工具，专为 JavaScript 生态系统设计，旨在提供与现代工具链完全兼容的同时显著提升性能。

- 🚀 Oxfmt 在无缓存首次运行时比 Prettier 快 30 倍以上，比 Biome 快 3 倍
- 📄 支持 JavaScript、TypeScript、JSON、YAML、HTML、CSS、Markdown 等多种文件格式
- 🔧 新增内置导入排序、Tailwind CSS 集成和 package.json 字段自动排序功能
- ✅ 现已通过 Prettier 的 JavaScript 和 TypeScript 一致性测试，实现 100% 兼容
- 📦 已被 Vue.js、Turborepo、HuggingFace.js 等多个知名项目采用
- ⚙️ 提供从 Prettier 一键迁移命令和 AI 辅助迁移提示
- 🖥️ 支持所有主流编辑器，包括 VS Code、IntelliJ 和 Neovim
- 🛠️ 新增 Node.js API 和增强的 CLI 选项，如配置初始化和迁移工具
- 🗺️ 未来路线图包括支持 Prettier 插件、优化嵌入式代码格式化及性能提升

---

### [使用 CSS 为链接添加下划线 | 始终扭曲](https://www.alwaystwisted.com/articles/underlining-links-with-css)

**原文标题**: [Underlining Links With CSS | Always Twisted](https://www.alwaystwisted.com/articles/underlining-links-with-css)

本文介绍了如何使用现代 CSS 属性精细控制链接下划线的样式，包括颜色、粗细、偏移和位置等，以提升设计效果和可读性。

- 🎨 使用 `text-decoration` 简写属性可一次性设置下划线的类型、样式、颜色和粗细
- 📏 `text-decoration-thickness` 允许用像素或相对单位精确控制下划线粗细
- 🌈 `text-decoration-color` 可让下划线颜色与文本颜色不同，实现更佳视觉效果
- 🎭 `text-decoration-style` 提供实线、双线、点线、虚线和波浪线等多种样式选择
- 📐 `text-underline-offset` 控制文本与下划线之间的间距，增加呼吸感
- 🔽 `text-underline-position` 特别适用于处理带下伸部分的文字，确保下划线位置一致
- ✍️ `text-decoration-skip-ink` 控制下划线是否避开字母下伸部分，影响可读性
- ⚠️ 注意：某些属性如偏移和位置需单独设置，简写属性可能重置其他样式
- 🌐 建议采用渐进增强策略，确保所有浏览器都能获得基本可用的下划线样式

---

### [CSS 自定义列表深度指南 - Piccalilli](https://piccalil.li/blog/an-in-depth-guide-to-customising-lists-with-css/)

**原文标题**: [
  An in-depth guide to customising lists with CSS - Piccalilli
](https://piccalil.li/blog/an-in-depth-guide-to-customising-lists-with-css/)

本文深入探讨了如何使用 CSS 自定义列表样式，涵盖了从基础样式调整到高级自定义技术的全面指南，包括无序列表和有序列表的样式修改、标记符号的个性化、颜色与字体调整，以及通过伪元素和计数器实现复杂自定义效果的方法。

- 📝 列表样式基础：使用`list-style-type`属性更改无序列表的标记符号（如圆点、圆圈、方块），或通过`list-style-image`使用图像作为标记。
- 🔢 有序列表定制：通过`list-style-type`支持多种编号系统（如拉丁字母、罗马数字等），并可自定义后缀符号。
- 🎨 标记样式调整：使用`::marker`伪元素可调整标记的颜色和字体属性，但样式选项有限。
- 🛠️ 高级自定义技术：通过`@counter-style`规则定义自定义编号序列或符号循环，支持跨浏览器兼容。
- 📏 完全控制标记：结合`list-style: none`和`::before`伪元素，可完全自定义标记的位置、样式和内容，实现灵活布局。
- 🔗 实用资源与总结：文章提供了多种 CSS 属性的适用场景总结，并推荐了进一步学习的资源和规范文档。

---

### [网页精灵 • 乔希·W·科莫](https://www.joshwcomeau.com/animation/sprites/)

**原文标题**: [Sprites on the Web • Josh W. Comeau](https://www.joshwcomeau.com/animation/sprites/)

本文介绍了 CSS 精灵动画技术，包括其基本原理、实现步骤、应用场景及注意事项，特别强调了在网页动画中如何利用现代 CSS 属性实现高效且可控的精灵动画效果。

- 🐦 **起源背景**：Twitter 在 2015 年将“收藏”功能改为“点赞”时，为兼容低端设备，采用游戏中的精灵动画技术替代 DOM 动画
- 🖼️ **核心原理**：将动画所有帧合并为一张精灵图，通过 CSS 控制显示区域，逐帧切换形成动画
- 🔧 **实现步骤**：使用`<img>`标签配合`object-fit: cover`和`object-position`属性，结合`steps()`时间函数实现离散帧切换
- ⚡ **性能优势**：相比 GIF 动画，精灵动画更轻量（约 30kb）、支持动态控制（速度、暂停）且兼容高分辨率显示
- ⚠️ **技术细节**：`steps()`函数的`jump-none`参数确保循环动画包含首尾帧，而默认`jump-end`适用于非循环动画
- 🎮 **适用场景**：适合重复性强的装饰动画（如闪烁图标、角色动画），不适合需要随机性或复杂交互的动态效果
- 🚫 **局限性**：精灵动画缺乏程序化动画的灵活性和随机性，中断时可能出现显示异常
- 🐱 **创意应用**：可用于网页互动元素（如会睡觉的猫咪动画），结合 CSS 控制实现动态行为变化

---

### [虚拟滚动处理数十亿行数据——来自 HighTable 的技术](https://rednegra.net/blog/20260212-virtual-scroll/)

**原文标题**: [Virtual Scrolling for Billions of Rows — Techniques from HighTable](https://rednegra.net/blog/20260212-virtual-scroll/)

本文介绍了 React 组件 HighTable 中用于处理数十亿行数据垂直滚动的五种关键技术，旨在保持高性能和可访问性。

- 🚀 **惰性加载**：仅加载当前可见的单元格数据，避免一次性加载全部数据，显著减少内存占用。
- ✂️ **表格切片**：只渲染可见行对应的 HTML 元素，大幅减少 DOM 节点数量，提升渲染性能。
- 🌌 **无限像素**：通过设置画布最大高度并降低滚动条分辨率，突破浏览器对元素高度的限制，支持海量行数。
- 🎯 **像素级精确滚动**：结合全局与局部两种滚动模式，允许用户通过滚动条快速跳转，同时支持鼠标滚轮进行精细浏览。
- 🎮 **两步随机访问**：将垂直与水平滚动逻辑分离，确保键盘导航或程序跳转时能准确定位到任意单元格。

---

### [编程文摘：电子邮件通讯](https://programmingdigest.net/?utm_source=web-archive&utm_campaign=react)

**原文标题**: [Programming Digest: Email Newsletter](https://programmingdigest.net/?utm_source=web-archive&utm_campaign=react)

《编程文摘》是一份为软件工程师精心筛选的每周通讯，汇集优质文章摘要，帮助读者高效学习新知、节省信息筛选时间，目前已有超过 19,698 名工程师订阅。

- 📬 每周精选推送：为软件工程师定制，提供含摘要的优质文章合集
- ⏱️ 高效省时：帮助读者快速获取有价值内容，免去自行搜寻的负担
- 🧠 持续学习：每周更新，确保订阅者能定期获得新知识
- 👥 社群认可：订阅者反馈积极，认为内容切合需求且启发思考
- 🌍 广泛受众：被全球多家知名科技企业的软件工程师阅读

---

### [科技领导力：电子邮件通讯](https://leadershipintech.com/?utm_source=web-archive&utm_campaign=react)

**原文标题**: [Leadership in Tech: Email Newsletter](https://leadershipintech.com/?utm_source=web-archive&utm_campaign=react)

一份为 CTO、工程经理和高级工程师精心策划的新闻通讯，旨在帮助他们成为更优秀的领导者。每周一和周四发送一封邮件，提供精选文章与简短摘要，助您高效获取有价值内容，每周学习新知识。

- 📬 超过 22,271 名工程领导者订阅，每周两封精选邮件
- 🕒 节省寻找优质内容的时间，直接阅读带摘要的精选文章
- 📚 每周学习新知识，聚焦领导力建设与软件领域深度内容
- 💬 读者好评：内容精准涵盖架构讨论、会议、计划及沟通技巧
- 🎯 重点文章如授权技能探讨，凸显其关键性
- 🌍 受到全球科技领导者阅读，来自 Bonobo Press 2013-2026 年持续发布

---

### [C#文摘：电子邮件通讯](https://csharpdigest.net/?utm_source=web-archive&utm_campaign=react)

**原文标题**: [C# Digest: Email Newsletter](https://csharpdigest.net/?utm_source=web-archive&utm_campaign=react)

《C#文摘》是一份专为.NET开发者精心策划的每周通讯，汇集精选文章与简短摘要，帮助超过17,000名工程师高效学习新知、节省时间。

- 📧 每周为.NET开发者推送精选内容，涵盖C#与.NET技术动态  
- ⏱️ 提供文章摘要，帮助读者快速筛选有价值信息，节省时间  
- 🧠 持续更新知识库，让订阅者每周都能学到新技能  
- 💬 读者反馈积极，内容可直接应用于工作场景，如功能标志、LINQ 技巧等  
- 🌍 服务全球.NET 工程师社群，包括微软、谷歌等企业开发者

---

### [让开发者保持最新动态——Bonobo Press](https://bonobopress.com/)

**原文标题**: [Keeping developers up to date â Bonobo Press](https://bonobopress.com/)

Bonobo Press 是一家自 2013 年起为超过 80,000 名软件开发者、IT 专业人士和技术人员提供最新资讯的媒体公司，通过发布简洁高效的软件通讯，帮助技术从业者节省时间并保持行业更新。

- 📧 提供多种软件通讯订阅，面向开发者、工程经理、技术主管和 CTO 等群体，以清晰简洁的内容节省读者时间
- 🎯 提供广告服务，帮助广告主精准触达软件工程师、团队领导、工程经理、CTO 及 IT 决策者等专业受众
- 📞 设有联系渠道，支持咨询、建议和广告合作等沟通需求

---

### [过往通讯：第一页](https://reactdigest.net/newsletters)

**原文标题**: [Past Newsletters: Page 1](https://reactdigest.net/newsletters)

React Digest 是一份专注于 React 生态的时事通讯，涵盖前沿技术、性能优化、最佳实践及漏洞分析等内容，旨在帮助开发者提升 React 开发技能。

- 🛠️ 探索 Next.js 重建、虚拟滚动数十亿行数据及 React Router 集成等创新技术
- 🐛 分享调试趣闻，如心形表情符号导致应用变慢，并介绍 React Native 改进和动画优化
- 🤖 分析 AI 在调试 React 中的应用，讨论 ViewTransition 元素和单元测试最佳实践
- ⚡ 深入 React 的 useOptimistic 钩子复杂性，探讨 Turbopack 编译和开源 React 桥接方案
- 📚 总结 React 最佳实践，包括性能优化、Client Components 使用及 TanStack 表单避坑指南
- 🔍 揭秘如何逆向工程 React 组件，分享 useEffectEvent 状态管理和 React Conf 2025 最新演讲
- 🧠 评估 AI 编写 React 代码的实际效果，回顾前端开发 30 年演进及类型安全组件技巧
- 🏆 精选 2025 年热门 React 文章，涵盖设计模式、状态管理和函数式编程等主题
- 🛡️ 分析 React 漏洞教训，探讨服务器组件和性能优化，提供假日安全提醒
- 🚀 介绍 React 19.2 的 INP 优化进展，对比 TanStack Router 与 Next.js，分享 useEffectEvent 使用技巧
- ⚠️ 警示 React 和 Next.js 关键漏洞，探讨设计系统构建和钩子改进方法
- ♿ 聚焦自动化无障碍测试，简化派生状态组件，并解析 React Router 对服务器组件的支持
- 🔄 分享从 Enzyme 迁移到 React Testing Library 的经验，讨论异步测试和可访问工具提示设计
- 🌟 展示 React 19.2 新特性，如自动优化和错误处理改进，以及定时器同步和测试最佳实践
- 🔗 探讨 URL 作为状态管理的优势，多语言应用质量提升及原子状态性能优化
- 🧩 解析 JavaScript 指令复杂性，比较 React 与 Remix 发展路径，介绍 React.createPortal 构建浮动 UI
- ⚡ 评估 React 服务器组件性能提升，探讨 Rari SSR 突破和 GraphQL 误解澄清
- 🔄 分享序列化状态管理技巧，避免属性钻取，并分析 TanStack Router 上下文继承
- ⚡ 优化 Suspense 与 useSyncExternalStore，提升结账体验，并讨论 useEffect 数据获取的替代方案

---

### [隐私](https://reactdigest.net/privacy)

**原文标题**: [Privacy](https://reactdigest.net/privacy)

React Digest 的隐私政策概述了其如何收集、使用和保护用户的个人信息，强调透明度、合法性和用户控制权，并遵守相关数据保护法规。

- 🔍 在收集个人信息前会明确说明用途，仅用于指定目的或经用户同意
- 📧 仅收集电子邮件地址用于发送新闻简报，不作其他用途
- 🛡️ 采取合理安全措施保护个人信息，防止丢失、盗窃或未经授权访问
- 📋 向用户公开个人信息管理政策与实践，确保透明度
- 🚫 不收集或存储 13 岁以下儿童的信息，网站也不针对该年龄段设计
- 📬 用户可随时通过邮件联系，查询或请求删除存储的个人信息
- 📭 每封新闻简报都包含退订链接，用户可随时取消订阅
- 📜 承诺遵守数据保护法（如英国《数据保护法》），保障用户权利

---

### [媒体资料包 – Bonobo Press](https://bonobopress.com/media-kit/)

**原文标题**: [Media Kit â Bonobo Press](https://bonobopress.com/media-kit/)

Bonobo Press 为技术专业人士提供高参与度的新闻简报广告服务，专注于连接广告商与精准目标受众，涵盖软件工具、招聘、会议等多种广告类型。

- 📧 **领导力科技**：面向技术领导者的双周简报，订阅者 22,325 人，开信率 57.95%，点击率 11.38%，赞助费每期 2,235 美元，受众多为欧美企业的决策者。
- 💻 **编程文摘**：面向软件工程师的每周简报，订阅者 20,032 人，开信率 50.41%，点击率 14.83%，赞助费每期 985 美元，覆盖从初级到管理层的开发者。
- ⚙️ **C#文摘**：针对.NET 开发者的每周简报，订阅者 17,098 人，开信率 54.92%，点击率 21.63%，赞助费每期 1,220 美元，受众多来自企业和大型组织。
- ⚛️ **React 文摘**：面向 React 前端开发者的每周简报，订阅者 20,075 人，开信率 54.06%，点击率 12.17%，赞助费每期 1,375 美元，提供次级广告位选项。
- 📊 **高互动率**：所有简报的互动率均超过行业基准两倍以上，通过严格列表清理确保读者参与度。
- 🎯 **精准受众**：订阅者主要来自欧美，涵盖谷歌、亚马逊等知名公司及各种规模企业，职位包括 CTO、工程师等。
- 📝 **纯文本广告**：广告格式为纯文本，需包含链接、标题和描述，最佳提交截止时间为发布前 4 天。
- 🔄 **合作流程**：从需求沟通、排期规划、发票支付到广告上线和效果报告，提供完整服务流程。
- 🤝 **长期合作**：许多合作伙伴会重复预订广告，涵盖身份管理、开发工具、安全等多个技术领域。

---

