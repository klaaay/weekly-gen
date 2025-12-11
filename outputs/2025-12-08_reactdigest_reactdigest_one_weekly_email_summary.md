### [React 文摘：电子邮件通讯](https://reactdigest.net/)

**原文标题**: [React Digest: Email Newsletter](https://reactdigest.net/)

《React Digest》是一份专为 React 开发者精心策划的每周通讯，汇集前端工程师社群，提供精选文章与摘要，帮助读者高效学习新知。

- 📰 每周为 React 开发者推送精选文章与简短摘要
- 👥 拥有超过 24,733 名前端软件工程师订阅者
- ⏱️ 帮助读者节省寻找优质内容的时间
- 🌱 每周持续学习 React 领域新知识
- 💬 读者反馈称赞其内容实用、能及时跟进技术演进
- 🌍 被全球前端工程师广泛阅读

---

### [React2Shell (CVE-2025-55182)：关键 React 漏洞 | Wiz 博客](https://www.wiz.io/blog/critical-vulnerability-in-react-cve-2025-55182)

**原文标题**: [React2Shell (CVE-2025-55182): Critical React Vulnerability | Wiz Blog](https://www.wiz.io/blog/critical-vulnerability-in-react-cve-2025-55182)

React 和 Next.js 中存在两个关键远程代码执行漏洞（CVE-2025-55182 和 CVE-2025-66478），它们源于 React 服务器组件（RSC）“Flight”协议的不安全反序列化。默认配置下的应用极易受到攻击，仅需一个特制的 HTTP 请求即可实现利用。漏洞已被野外利用，攻击者借此进行云凭证窃取和加密货币挖矿。Wiz 数据显示，39% 的云环境中存在易受攻击的实例。安全团队应立即升级至已修复的版本。

- 🚨 **漏洞概述**：CVE-2025-55182（React）和 CVE-2025-66478（Next.js）是关键的未认证 RCE 漏洞，源于 RSC“Flight”协议的不安全反序列化。
- ⚠️ **影响范围**：默认配置下的 React 19 生态和 Next.js 等框架均受影响，标准部署无需代码修改即可被利用。
- 🌐 **利用情况**：漏洞已被野外利用，攻击者通过特制 HTTP 请求实现 RCE，并观察到云凭证窃取和加密货币挖矿活动。
- 📊 **风险数据**：Wiz 研究显示，39% 的云环境中存在易受攻击实例，44% 的云环境有公开暴露的 Next.js 应用。
- 🛠️ **受影响产品**：包括 React 19.0.x 至 19.2.x、Next.js 14.3.0-canary.77 及更高版本，以及 Vite、Parcel 等集成 RSC 的框架。
- 🔧 **缓解措施**：立即升级 React 至 19.0.1/19.1.2/19.2.1，Next.js 至相应安全版本；检查其他 RSC 框架更新。
- 🛡️ **安全建议**：使用 Wiz 等工具进行漏洞检测、镜像扫描和运行时监控，防范攻击活动。

---

### [精密 AI——无需编写测试的自动化前端测试](https://www.meticulous.ai/?utm_source=react_digest)

**原文标题**: [Meticulous AI - Automated Frontend Testing Without Writing Tests](https://www.meticulous.ai/?utm_source=react_digest)

Meticulous AI 是一款创新的自动化测试工具，通过记录用户与应用的交互来生成并维护测试套件，无需手动编写或维护测试代码，帮助开发团队高效、无差错地发布代码。

- 🚀 **无需编写测试** – 通过记录用户交互自动生成测试，覆盖所有用户流程和边缘情况，无需手动编写或维护测试代码。
- 🔄 **测试自动演进** – 随着应用更新，测试套件自动添加新测试并移除过时测试，保持测试套件始终最新且完整。
- ⚡ **闪电般快速执行** – 测试在计算集群上高度并行化，可在 120 秒内测试数千个页面，大幅提升测试效率。
- 🛡️ **彻底消除测试波动** – 从 Chromium 底层构建，采用确定性调度引擎，确保测试结果稳定可靠，无随机失败。
- 🔗 **无缝集成与安全** – 支持与现有测试套件结合使用或完全替代，提供多种前端框架集成选项，并确保数据安全。
- 📈 **提升开发效率** – 被 Dropbox、Notion 等超过 100 家组织信任，帮助团队预防回归错误，增强代码库质量信心。

---

### [获取失败](https://engineering.udacity.com/building-a-design-system-in-2026-5cfd8d85043c)

**原文标题**: [Failed to retrieve](https://engineering.udacity.com/building-a-design-system-in-2026-5cfd8d85043c)

无法总结：获取内容失败，状态码 403。

---

### [React 已变，你的 Hooks 也该更新了 - Matt Smith](https://allthingssmitty.com/2025/12/01/react-has-changed-your-hooks-should-too/)

**原文标题**: [
    React has changed, your Hooks should too - Matt Smith
  ](https://allthingssmitty.com/2025/12/01/react-has-changed-your-hooks-should-too/)

React Hooks 已推出多年，但许多代码库仍沿用旧有模式，如过度依赖 `useState` 和 `useEffect`。随着 React 18/19 并发特性的引入，React 处理数据（尤其是异步数据）的方式已发生变化。本文探讨了现代 Hook 的最佳实践，包括如何避免滥用 `useEffect`、利用自定义 Hook 封装逻辑、使用 `useSyncExternalStore` 管理订阅状态、通过并发工具优化 UI 响应性，以及构建可测试的 Hook 架构。最后，文章指出 React 正朝着数据优先的渲染流程发展，开发者应调整 Hook 使用方式以适应服务器/客户端边界，提升应用的可维护性和未来兼容性。

- 🚨 **避免滥用 useEffect**：仅将其用于真正的副作用（如网络请求、DOM 操作），而非派生状态或数据转换。优先使用 `useMemo`、`useCallback` 或框架提供的工具在渲染期间计算数据。
- 🧩 **自定义 Hook 实现封装**：将领域逻辑提取到自定义 Hook 中，使组件专注于 UI 渲染，提升代码可测试性和可维护性。
- 🔗 **使用 useSyncExternalStore 管理订阅状态**：适用于浏览器 API（如 `matchMedia`）或外部存储（如 Redux），确保同步更新并避免渲染不一致问题。
- ⚡ **利用并发工具优化性能**：通过 `useDeferredValue` 延迟派生值计算，或使用 `startTransition` 推迟状态更新，保持 UI 响应流畅。
- 🧪 **构建可测试的 Hook 架构**：将逻辑与 UI 分离，直接测试 Hook 函数，并利用 React DevTools 简化调试过程。
- 🌐 **适应数据优先的 React 趋势**：关注 Server Components、`use()`、服务端操作等新特性，减少对 `useEffect` 的依赖，转向更清晰的渲染驱动数据流。

---

### [没有蓝色条](https://wtbb.vercel.app/)

**原文标题**: [Without the blue bar](https://wtbb.vercel.app/)

我构建了一个完全流式传输、即时加载的 GitHub 仓库视图版本，它保留了原生浏览器搜索功能，移除了蓝色加载条，并且感觉比原版快得多。

- 🚀 作者受到社区讨论启发，针对 GitHub 速度慢的问题，构建了一个优化版本，核心目标是保持快速体验和原生浏览器搜索功能。
- 📱 文章解释了列表虚拟化技术（如 UITableView）的原理，通过复用可见区域外的元素来提升渲染性能，这在移动设备和浏览器中广泛应用。
- 🔍 GitHub 已在大文件浏览中采用虚拟化技术，通过透明文本框保留原生搜索，但拉取请求中的差异组件因行数较少，虚拟化反而可能降低性能。
- ⏳ 蓝色加载条是界面阻塞的表现，理想目标是消除其出现的必要性，而非仅仅加快加载速度。
- ⚙️ 作者采用混合方案：基于 2024 年的 CSS/JS 基准，优先避免 JavaScript，流式传输所有内容，使用最快框架（Next.js），并保护浏览器主线程。
- 🖥️ 选择 Next.js 和 React 服务器组件（RSC），将大部分渲染和逻辑移至服务器，减少客户端负担，同时保持流式传输和服务器驱动 UI 的优势。
- 🎨 利用 CSS 的`content-visibility`和`contain-intrinsic-size`属性模拟虚拟化效果，在不破坏原生搜索的前提下提升大型文件渲染性能。
- 🏗️ 分析了 GitHub 前端架构：从 jQuery 转向 React，采用 Primer 设计系统，但部分组件依赖客户端逻辑，可能导致响应式体验不佳。
- 🔧 技术实现上使用 GraphQL（Relay）获取数据，Tailwind CSS 进行样式设计，并逐步移植 GitHub 的设计令牌，追求像素级还原。
- 💡 通过纯 CSS 实现部分交互功能（如文件数量切换、提交详情展开），减少 JavaScript 依赖，提升性能。
- ⚡ 利用 Next.js 的缓存组件和流式渲染，实现近乎即时的路由切换，并通过预取链接进一步优化感知速度。
- 📈 最终成果是一个感觉上更接近原生应用、无需蓝色加载条的 GitHub 仓库视图，为探索 RSC 和性能优化提供了实践参考。

---

### [为 MDX 文档站点创建 LLMs 的 Markdown 复制按钮 | amanhimself.dev](https://amanhimself.dev/blog/create-a-copy-as-markdown-for-mdx-documentation/)

**原文标题**: [Create a copy as markdown button for LLMs in an MDX documentation site | amanhimself.dev](https://amanhimself.dev/blog/create-a-copy-as-markdown-for-mdx-documentation/)

在基于 MDX 的文档站点中实现“复制为 Markdown”按钮，需要将动态组件（如场景、JSON 驱动的表格、API 文档）转换为纯 Markdown。核心方案包括定位当前页面的 MDX 源文件、获取原始内容并通过转换管道处理、扩展所有动态组件为 Markdown，最后将结果复制到剪贴板或供 AI 工具使用。

- 🧩 **识别关键任务**：定位 MDX 源文件、获取原始内容、扩展动态组件、输出 Markdown。
- 🔄 **转换流程**：客户端处理，使用正则表达式移除 React 导入，并将组件转换为 Markdown 等价物。
- ⚙️ **实现步骤**：创建 React 组件触发操作，通过路由获取 MDX 文件路径，使用`prepareMarkdownForCopyAsync`函数处理转换。
- 📄 **内容处理**：分阶段处理 Frontmatter、移除导入语句、转换链接和代码块等简单组件，再异步扩展场景和 API 文档等复杂组件。
- 🧱 **组件扩展**：对于场景组件，加载外部 MDX 文件并递归转换；对于 API 文档，获取 TypeDoc JSON 并将其结构转换为格式化的 Markdown。
- 🔧 **模式通用性**：该方案可扩展，新组件类型可通过相同模式（匹配、获取数据、转换、替换）集成到转换管道中。

---

### [豚骨拉面](https://www.tonkotsu.ai/morethanvibes?utm_source=bonobo&utm_campaign=dec8)

**原文标题**: [Tonkotsu](https://www.tonkotsu.ai/morethanvibes?utm_source=bonobo&utm_campaign=dec8)

本文介绍了人工智能在医疗领域的应用现状与前景，重点探讨了其在疾病诊断、治疗方案优化及医疗管理效率提升方面的作用，并简要提及了相关的技术挑战和伦理考量。

- 🤖 AI 辅助诊断系统能通过分析医学影像快速识别病灶，提高早期疾病检出率
- 💊 基于机器学习的个性化治疗方案可结合患者数据优化用药与治疗路径
- 📊 智能医疗管理平台整合临床数据，提升医院运营效率与资源分配合理性
- ⚠️ 数据隐私保护与算法透明度仍是当前技术落地需要解决的关键问题
- 🔮 未来 AI 或将在预防医学和远程医疗领域发挥更重要的辅助作用

---

### [前端十大戒律 | Felipe Gustavo 的博客](https://www.felgus.dev/blog/ten-frontend-commandments)

**原文标题**: [Ten Frontend Commandments | Felipe Gustavo's Blog](https://www.felgus.dev/blog/ten-frontend-commandments)

本文总结了前端开发的十条实用准则，旨在帮助开发者高效管理项目、协调团队并确保交付质量。

- 🛑 若当前版本已获认可，无需额外改动
- 🤝 面对复杂设计需求，拉上业务方共同决策
- 👥 促进设计师与业务方直接沟通以简化方案或调整排期
- ⏳ 提前与后端协调需求并明确责任
- 🌙 选择低峰时段部署以减少用户对问题的感知
- 📝 在工单中详细记录修改内容和决策依据
- 📱 全面测试不同分辨率及弱网/低性能设备表现
- ⏰ 工期紧张时优先保障核心功能与用户流程
- 🔍 紧密配合测试团队，快速修复问题
- ⚖️ 合理评估工期，避免过度承诺

---

### [CSS 2025 年历](https://cssadventcalendar.dev/)

**原文标题**: [CSS Advent Calendar 2025](https://cssadventcalendar.dev/)

该应用需要启用 JavaScript 才能正常运行。

- 🔧 必须启用 JavaScript 以支持应用功能
- 🌐 确保浏览器设置允许 JavaScript 执行
- ⚡ 启用后可正常加载和交互应用内容

---

### [顶层困扰：弹出层与对话框之争 - HTMHell](https://htmhell.dev/adventcalendar/2025/1/)

**原文标题**: [Top layer troubles: popover vs. dialog - HTMHell](https://htmhell.dev/adventcalendar/2025/1/)

本文讨论了在网页开发中同时使用原生对话框（dialog）和弹出层（popover）时可能出现的交互冲突问题，特别是当弹出层需要显示在已打开的模态对话框之上时，由于对话框会使页面其他部分变为“惰性”（inert），导致弹出层无法通过键盘或屏幕阅读器访问。文章通过一个通知 toast 的实际案例，解释了问题的根源，并提供了解决方案。

- 🧱 堆叠上下文（stacking context）决定了元素在 Z 轴上的层叠顺序，而 `z-index` 仅在同一个堆叠上下文中有效。
- 🏆 顶层（top layer）是浏览器中最顶层的渲染层，可以超越任何堆叠上下文，目前只有通过 `showModal()` 打开的对话框和弹出层（popover）能进入此层。
- 🐛 当模态对话框打开时，页面其他部分会变为“惰性”（inert），这会导致虽然弹出层在视觉上显示在对话框之上，但无法通过键盘或屏幕阅读器访问。
- 🔧 解决方案是将弹出层移动到对话框的 DOM 结构内部，并设置 `popover="manual"` 来防止误触关闭。
- ⚠️ 如果网页或应用可能同时显示对话框和弹出层，需要考虑设计机制来协调两者的显示，或者暂时抑制背景弹出层的显示。
- 📚 作者建议在完全替换自定义弹出层架构前，注意这种潜在冲突，并关注相关 HTML 标准的讨论进展。

---

### [Bun 加入 Anthropic | Bun 博客](https://bun.com/blog/bun-joins-anthropic)

**原文标题**: [Bun is joining Anthropic | Bun Blog](https://bun.com/blog/bun-joins-anthropic)

Bun 已被 Anthropic 收购，将作为 Claude Code 等 AI 编程工具的核心基础设施，同时保持开源、公开开发且团队不变，未来将更专注于高性能 JavaScript 工具链和 AI 编程生态的优化。

- 🚀 **Bun 被 Anthropic 收购**：将作为 Claude Code、Claude Agent SDK 等 AI 编程产品的底层基础设施  
- 🔓 **开源承诺不变**：保持 MIT 许可证，代码公开开发，团队持续维护  
- 🎯 **发展重心延续**：继续优化 JavaScript 工具链性能、Node.js 兼容性及替代 Node.js 的运行时目标  
- 🤖 **深度整合 AI 生态**：基于 Claude Code 等工具的前沿需求，加速 Bun 对 AI 编程场景的适配  
- ⚡ **技术优势强化**：利用单文件可执行文件特性，为 AI 工具提供轻量、跨平台的部署方案  
- 📈 **长期稳定性提升**：依托 Anthropic 资源，避免商业化压力，专注技术迭代与生态建设  
- 🌍 **历史发展回顾**：从个人项目到月下载量超 720 万的开源运行时，持续聚焦开发效率提升  
- 🔮 **未来定位**：成为 AI 驱动软件构建、运行和测试的最佳平台，同时保持通用 JavaScript 工具的竞争力

---

### [错误](https://calendar.perfplanet.com/2025/improve-ttfb-and-ux-with-http-streaming/)

**原文标题**: [Error](https://calendar.perfplanet.com/2025/improve-ttfb-and-ux-with-http-streaming/)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='calendar.perfplanet.com', port=443): Max retries exceeded with url: /2025/improve-ttfb-and-ux-with-http-streaming/ (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1000)')))

---

### [GitHub - trekhleb/javascript-algorithms: 📝 使用 JavaScript 实现的算法和数据结构，附带解释和进一步阅读链接](https://github.com/trekhleb/javascript-algorithms)

**原文标题**: [GitHub - trekhleb/javascript-algorithms: 📝 Algorithms and data structures implemented in JavaScript with explanations and links to further readings](https://github.com/trekhleb/javascript-algorithms)

这是一个包含大量 JavaScript 算法和数据结构实现的 GitHub 仓库，提供详细的解释和进一步阅读链接，适合学习和面试准备。

- 📚 仓库包含多种数据结构和算法的 JavaScript 实现，如链表、树、图、排序和搜索算法等
- 🌍 支持多语言文档，包括中文、英文、日文等，方便全球开发者学习
- 🧪 提供完整的测试环境，可通过 npm 运行测试和代码检查，便于验证和实践
- 📊 附有算法复杂度（大 O 表示法）和数据结构操作复杂度的详细参考图表
- 🆓 开源项目，采用 MIT 许可证，鼓励贡献和协作，拥有活跃的社区支持

---

### [如何利用派生状态简化 React 组件](https://www.freecodecamp.org/news/simplify-react-components-with-derived-state/)

**原文标题**: [How to Simplify Your React Components with Derived State](https://www.freecodecamp.org/news/simplify-react-components-with-derived-state/)

本文介绍了在 React 中如何通过派生状态简化组件，避免过度使用 useState 导致的数据重复、不必要的重新渲染和同步问题。通过具体示例展示了如何从 props、现有状态、URL 参数和外部数据中派生状态，并提供了使用 useMemo 优化性能的方法，同时指出了仍需使用 useState 的场景。

- 🚀 避免过度使用 useState：存储可计算的值会导致数据重复、调试困难和额外渲染
- 🔄 从 props 或现有状态派生：如全名可由姓氏和名字拼接，无需单独存储状态
- 🌐 从 URL 参数派生：使用路由库（如 React Router）的钩子直接获取参数，避免状态同步问题
- 📡 从外部数据派生：利用数据获取库（如 React Query）的状态作为单一数据源，减少冗余状态
- ⚡ 使用 useMemo 优化性能：对昂贵计算进行缓存，避免不必要的重新计算
- 🎯 仍需使用 useState 的场景：受控输入和独立状态变化（如模态框开关）需要直接管理状态
- 🧠 核心原则：只存储无法派生的状态，保持状态最小化以提升可维护性

---

### [编程文摘：电子邮件通讯](https://programmingdigest.net/?utm_source=web-archive&utm_campaign=react)

**原文标题**: [Programming Digest: Email Newsletter](https://programmingdigest.net/?utm_source=web-archive&utm_campaign=react)

《编程文摘》是一份面向软件工程师的每周精选简报，旨在通过筛选优质内容帮助读者高效学习新知、节省时间，并已获得超过 2.3 万名工程师的订阅与积极反馈。

- 📬 每周为软件工程师精选推送优质文章与摘要
- ⏱️ 帮助读者节省寻找有价值内容的时间
- 🌱 每期内容均包含可学习的新知识
- 👥 已吸引超过 23,386 名软件工程师订阅
- 💬 读者反馈称赞其内容精准实用、启发性强

---

### [科技领导力：电子邮件通讯](https://leadershipintech.com/?utm_source=web-archive&utm_campaign=react)

**原文标题**: [Leadership in Tech: Email Newsletter](https://leadershipintech.com/?utm_source=web-archive&utm_campaign=react)

这是一份为技术领导者精心打造的每周通讯，旨在通过精选文章帮助他们提升领导力、节省时间并持续学习。

- 📬 **订阅规模**：超过 27,934 名工程领导者订阅这份每周电子邮件
- 🎯 **目标读者**：面向 CTO、工程经理和高级工程师，助力成为更好的领导者
- 📚 **内容特色**：提供人工精选文章并附有简短摘要，节省寻找有价值内容的时间
- 🌱 **核心价值**：确保读者每周都能学到新知识，持续成长
- 💬 **读者好评**：用户称赞其领导力建设文章精准实用，尤其关注架构讨论、会议、计划及沟通等主题
- 🏢 **发布方**：由 Bonobo Press 自 2013 年持续运营至今

---

### [C#文摘：电子邮件通讯](https://csharpdigest.net/?utm_source=web-archive&utm_campaign=react)

**原文标题**: [C# Digest: Email Newsletter](https://csharpdigest.net/?utm_source=web-archive&utm_campaign=react)

C# Digest 是一份面向.NET 开发者的精选周刊，提供高质量内容以节省读者时间并促进每周学习。

- 📧 超过19,592名C#工程师订阅的每周电子邮件
- 📖 精选文章配简短摘要，节省寻找有价值内容的时间
- 🆕 每周学习新知识，涵盖标准功能标志、LINQ 等实用主题
- 💬 读者反馈积极，文章如操作结果模式已被应用于实际工作
- 🌍 受到全球.NET 工程师欢迎，内容实用性强

---

### [让开发者保持最新动态——Bonobo Press](https://bonobopress.com/)

**原文标题**: [Keeping developers up to date â Bonobo Press](https://bonobopress.com/)

Bonobo Press 是一家自 2013 年起为软件开发者、IT 专业人士和技术人员提供最新资讯的媒体公司，拥有超过 93,000 名订阅用户。

- 📰 提供精选的每周新闻简报，内容简洁清晰，帮助技术人员节省时间
- 🎯 提供广告服务，可精准触达软件工程师、技术主管和 IT 决策者等专业受众
- 📞 支持通过联系渠道进行咨询、建议或广告合作

---

### [过往通讯：第一页](https://reactdigest.net/newsletters)

**原文标题**: [Past Newsletters: Page 1](https://reactdigest.net/newsletters)

《React Digest》是一份专注于 React 生态的新闻简报，涵盖框架更新、性能优化、状态管理及最佳实践等主题。

- 🚨 探讨 React 与 Next.js 的关键安全漏洞及应对措施
- ♿ 介绍 React 中自动化无障碍测试的实现方法
- 🧪 分享从 Enzyme 迁移到 React Testing Library 的实践经验
- ⚡ 解析 React 19.2 的自动优化与错误处理新特性
- 🔗 探讨 URL 作为状态管理的应用场景
- 🧭 分析 JavaScript 指令与 React/Remix 的技术演进
- ⚙️ 评估 React 服务端组件的实际性能影响
- 🔄 研究 React 状态序列化与反序列化的高效方案
- ⏱️ 探索 useSyncExternalStore 在并发渲染中的应用
- 🎨 剖析 React 渲染行为的细节与 useEffectEvent 新特性
- 📊 展示 2025 年 React 状态管理的前沿方案
- 🏆 讨论 React 生态主导地位对技术创新的影响
- 💾 介绍 TanStack DB 响应式客户端存储工具
- 🛠️ 探索无框架支持 React 服务端组件的解决方案
- ⚡ 综述 React 并发特性的核心机制
- ⏳ 分析 hydration 过程对应用性能的深层影响
- 💡 强调缓存一致性在 React 应用中的关键作用
- 👷 探索 Web Workers 在 React 性能优化中的应用
- ⚙️ 深入剖析 useCallback 的实际使用场景与误区
- 🐻 介绍轻量级状态管理库 Zustand 的核心特性

---

### [隐私](https://reactdigest.net/privacy)

**原文标题**: [Privacy](https://reactdigest.net/privacy)

React Digest 的隐私政策概述了其如何收集、使用和保护用户的个人信息，特别强调仅收集邮箱地址用于发送周刊，并遵循透明、合法和安全的数据处理原则。

- 🔍 在收集个人信息前会明确说明用途，并仅用于指定或经同意的目的
- 📧 仅收集用户邮箱地址以发送周刊，不用于其他目的或垃圾邮件
- 🛡️ 采取合理安全措施保护个人信息，防止丢失、盗用或未经授权的访问
- 📜 遵循数据最小化原则，仅保留必要时间，并确保信息准确、完整
- 👶 严格遵守儿童隐私保护，不收集 13 岁以下儿童信息
- 📬 用户可随时通过邮件联系查询、修改或删除个人数据
- 🚫 提供明确的退订方式，坚决反对垃圾邮件行为
- 🌐 业务运营遵循声明的隐私原则，确保个人信息机密性

---

### [媒体资料包 – Bonobo Press](https://bonobopress.com/media-kit/)

**原文标题**: [Media Kit â Bonobo Press](https://bonobopress.com/media-kit/)

Bonobo Press 是一家专注于为程序员和技术人员提供最新趋势、工具和技术资讯的媒体平台，通过精心策划的周报吸引高度参与的专业读者，并为合作伙伴提供精准的广告投放服务，以覆盖目标受众并提升参与度、潜在客户和转化率。

- 📧 **领导力技术周报**：面向工程经理、技术领导、CTO 等决策者，订阅者 27,818 人，打开率 57.95%，点击率 11.38%，赞助费用每期 2,235 美元，主要受众来自欧洲和美国，涵盖谷歌、亚马逊等大型企业。
- 💻 **编程摘要周报**：针对软件工程师和开发者，订阅者 21,632 人，打开率 50.41%，点击率 14.83%，赞助费用每期 985 美元，受众经验层次多样，以欧洲和美国为主。
- ⚙️ **C# 摘要周报**：专注于.NET和C#开发者，订阅者19,856人，打开率54.92%，点击率21.63%，赞助费用每期1,220美元，受众多就职于医疗、金融等大型企业。
- ⚛️ **React 摘要周报**：服务于 React 前端开发者，订阅者 23,831 人，打开率 54.06%，点击率 12.17%，赞助费用每期 1,375 美元，覆盖多种公司和行业。
- 📊 **广告格式与流程**：广告为纯文本形式，需包含链接、标题和简短描述，提交截止日期为发布前 4 天；预订流程包括咨询、排期、付款、素材交付和效果报告。
- 🤝 **合作伙伴与案例**：曾与 Okta、GitLab、MongoDB 等多家知名公司合作，提供重复赞助机会，确保广告触达精准技术受众。

---

