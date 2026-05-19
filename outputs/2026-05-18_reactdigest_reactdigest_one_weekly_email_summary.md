### [React 文摘：邮件通讯](https://reactdigest.net/)

**原文标题**: [React Digest: Email Newsletter](https://reactdigest.net/)

这是一份面向 React 开发者的精选周刊，每周一封邮件，帮助开发者高效获取优质内容。

- 📧 每周一封邮件，为超过 22,507 名前端工程师精心挑选内容
- 📝 附带简短摘要的手选文章，节省寻找有价值内容的时间
- 🧠 每周学习新知识，持续跟进 React 生态演进
- ⭐ 读者反馈积极，称赞文章实用、内容优质，尤其对 React 并发模式等主题评价高
- 🏢 读者来自各大前端公司，涵盖广泛行业背景
- 🔗 提供新闻通讯、隐私政策及广告投放选项

---

### [React 项目实战 — 坦纳·林斯利](https://tannerlinsley.com/posts/projecting-react)

**原文标题**: [Projecting React â Tanner Linsley](https://tannerlinsley.com/posts/projecting-react)

### 概述总结
Tanner Linsley 通过 AI 辅助构建了 React 的轻量化投影版本`@tanstack/redact`，将 React 运行时从 60KB 压缩至 7-9KB，同时保持核心 API 兼容性，并已在两个生产站点验证其性能优势。

- 🚀 **核心动机**：React 19 的 60KB gzip 体积对 TanStack Start 而言过于臃肿，而 Preact 兼容层已无法完美适配 React 19 的 API。
- 💡 **理念转变**：受 Kyle Mathews 启发，将代码视为“物化视图”——思想是基础表，代码只是投影之一，AI 使生成特定投影的成本大幅降低。
- 🛠️ **技术实现**：通过 Vite 插件实现功能级开关（8 个可切换特性），`full`预设 9.39KB，`nano`预设 7.08KB，用户代码无需修改。
- 📊 **性能数据**：相比 React 19，客户端导航速度提升 2.24 倍，SSR 提升 3 倍，稳定列表渲染快 18%，总 JS 体积减少 33% 至 4.7%。
- 🌐 **生产验证**：tannerlinsley.com 和 tanstack.com 已完全运行在该投影上，FCP 降低 18%，LCP 降低 12%，RSC 页面 LCP 有 8-43% 回归但仍在绿色阈值内。
- ⚠️ **局限性**：不支持并发模式、时间切片、React DevTools，`useTransition`和`useDeferredValue`同步执行，需明确权衡通用性。
- 🤖 **AI 协作模式**：核心代码一天内通过 AI 提示完成，后续仅需描述生产环境 bug 即可获得修复，无需深入调试。
- 🧩 **社区定位**：明确声明这不是“替代 React”，而是针对特定应用形状的窄实验，不打算营销或纳入 TanStack Start 主项目。
- 🔮 **未来趋势**：类比 Linux 发行版和音乐混音，认为 Web 开发将进入“投影化”时代——开发者能为自己的需求定制库的轻量版本。

---

### [从 React 到使用 nanotags 的原生 Web：一次节省了 100KB 的迁移——火星编年史，邪恶火星人团队博客](https://evilmartians.com/chronicles/from-react-to-native-web-with-nanotags-a-migration-that-saved-100kb)

**原文标题**: [From React to native web with nanotags: a migration that saved 100 KB—Martian Chronicles, Evil Martians’ team blog](https://evilmartians.com/chronicles/from-react-to-native-web-with-nanotags-a-migration-that-saved-100kb)

概述总结  
- 📉 通过从 React 迁移到原生 Web Components，营销网站减少了 100 KB 的 JavaScript，且功能未受影响。  
- 🧩 使用 Astro 和 nanostores 结合自定义元素，实现了轻量级交互，避免了全量框架的负担。  
- 🛠️ 开发了 nanotags 库，简化了 Web Components 的编写，提供类型安全、自动清理和响应式属性。  
- ♿ 通过 W3C ARIA 指南和附件模式，确保了无障碍性，甚至在某些方面优于 React。  
- 📦 核心库仅 2.5 KB，整体组件系统约 3 KB，远小于 React 或 Lit 的体积。  
- 🌐 强调平台原生能力（如自定义元素、DOM API）已足够应对静态网站需求，无需额外框架。

---

### [React2Shell 的故事 | Lachlan Davidson | 博客](https://lachlan.nz/blog/the-react2shell-story/)

**原文标题**: [The React2Shell Story | Lachlan Davidson | Blog](https://lachlan.nz/blog/the-react2shell-story/)

React2Shell 漏洞事件概述  
- 📅 2025 年 11 月 30 日，安全研究员 Lachlan Davidson 向 Meta 报告了 React 中的严重远程代码执行漏洞（CVE-2025-55182），Meta 于 12 月 3 日发布修复。  
- 🔍 漏洞源于 React Server Components 的"Flight"协议，该协议允许传递复杂 JavaScript 对象，但缺乏对原型属性访问的安全检查。  
- ⚠️ 攻击者可利用 Flight 协议发送恶意对象，通过原型链访问（如`Number.prototype.toString`）或 thenable 对象，触发 React 内部函数调用链。  
- 🧩 漏洞利用链复杂：通过伪造 Chunk 对象、操控服务器清单、调用`Module._load`实现任意代码执行，最终 PoC 仅需在 Next.js 应用中运行脚本即可触发 RCE。  
- 🛡️ Meta 团队在 17 小时内确认漏洞，与 React/Vercel 团队协作开发补丁，并协调行业伙伴部署防御措施。  
- 🌐 该漏洞影响数百万网站，包括大型 AI 公司和加密货币交易平台，凸显了 React Server Components 协议的安全风险。

---

### [五种模型，一个 React 技术栈：为何每个大语言模型都构建相同的应用 | Sascha Becker](https://saschb2b.com/blog/llm-default-react-stack)

**原文标题**: [Five Models, One React Stack: Why Every LLM Builds the Same App | Sascha Becker](https://saschb2b.com/blog/llm-default-react-stack)

当前主流 AI 模型（Claude、GPT、Gemini、DeepSeek、Qwen、v0、Lovable、Bolt）在构建 React 应用时，几乎都默认使用同一套技术栈：Next.js 或 Vite、TypeScript、Tailwind CSS、shadcn/ui、TanStack Query 和 Zustand。这种趋同并非巧合，而是由训练数据主导、Token 经济学和 AI 编码工具特性共同驱动的结果，并可能引发前端生态的“单一文化”问题。

- 📊 **趋同现状一览**：多个模型和 AI 构建工具的输出高度一致，前端框架、样式方案、组件库、状态管理几乎雷同，形成“八行数据，一套 UI 层”的局面。
- 🧠 **Token 经济学偏爱 Tailwind**：Tailwind 的原子化类名（如`flex`、`p-4`）是高频、可预测的 Token，减少了跨文件依赖和命名风险，对 LLM 而言是“阻力最小的路径”。
- 📦 **shadcn/ui的“开放代码”优势**：组件以纯 JSX 和 Tailwind 类名形式复制到项目中，无需记忆复杂 API，且提供 MCP 服务器和官方 Claude Skill，专为 LLM 消费优化。
- 🔄 **训练数据主导的飞轮效应**：最流行的栈成为训练数据主力，LLM 输出又将其推回 GitHub，形成“流行→训练→输出→更流行”的自我强化循环，其他框架（Vue、Svelte、Solid 等）的可见性被系统性削弱。
- ⏳ **版本滞后永久化**：LLM 基于训练数据统计输出，旧模式（如`useEffect + fetch`）因数据量大而占优，新特性（如 React Compiler）难以普及，且 AI 生成的旧代码会进一步污染未来训练数据。
- 🚫 **新人看不到“菜单”**：初学者通过 LLM 构建应用时，模型默认选择 React + Tailwind + shadcn，且不告知有其他选项，导致他们根本不知道技术栈是“可选择的类别”。
- 🎨 **“AI slop”美学问题**：无设计约束时，模型输出趋同的 UI 风格（圆角、Inter 字体、灰色调、蓝色按钮），品牌差异化需要主动对抗模型默认值。
- 🧩 **长尾框架受损**：小型、小众、有创意的框架因缺乏训练数据而边缘化，只有强企业支持或积极拥抱 LLM 的框架（如 shadcn、Chakra、Tailwind）能存活。
- 🛠️ **如何引导模型偏离默认栈**：提供五级干预方案，从最脆弱的提示指令（Level 1）到最强力的工具护栏（Level 5），包括项目规则文件（CLAUDE.md）、代码库示例、Skills/MCP 服务器、ESLint 限制和 CI 过滤。
- ⚖️ **诚实结论**：默认栈的存在有其合理原因（Tailwind 适合 LLM、shadcn 适合编辑、React 赢得市场），但问题在于选择被系统冻结。保持工具多样性需要主动付出努力，否则将导致千篇一律的 Web。

---

### [事后分析：TanStack npm 供应链安全事件 | TanStack 博客](https://tanstack.com/blog/npm-supply-chain-compromise-postmortem)

**原文标题**: [Postmortem: TanStack npm supply-chain compromise | TanStack Blog](https://tanstack.com/blog/npm-supply-chain-compromise-postmortem)

以下是 TanStack 官方发布的关于 npm 供应链攻击事件的总结：

2026 年 5 月 11 日，TanStack 的 Router/Start 仓库遭受了 npm 供应链攻击，攻击者利用 GitHub Actions 的缓存投毒和 OIDC 令牌提取漏洞，发布了 84 个恶意包版本。目前所有包已恢复安全，事件已解除警报。

- 📦 **影响范围**：仅 Router/Start 仓库受影响，42 个 monorepo 包各有 2 个恶意版本，共 84 个版本，其他 TanStack 库（如 Query、Table、Form 等）未受影响。
- 🔗 **攻击链**：攻击者结合了 `pull_request_target` 的“Pwn Request”模式、GitHub Actions 缓存投毒（跨 fork↔base 信任边界）以及从 GitHub Actions 运行进程内存中提取 OIDC 令牌，从而绕过正常发布流程。
- ⏱️ **时间线**：恶意包于 19:20–19:26 UTC 发布，外部研究人员在 19:46 UTC 发现并报告，维护团队在约 1 小时 43 分钟内完成全部 84 个版本的弃用，npm 在约 4 小时 35 分钟内移除所有恶意 tarball。
- 🛡️ **恶意行为**：恶意包在 `npm install` 时执行 `router_init.js` 脚本，窃取 AWS、GCP、Kubernetes、Vault、npm、GitHub 和 SSH 凭据，并通过 Session/Oxen 信使网络外传，还能自我传播至受害者维护的其他包。
- ✅ **当前状态**：所有已发布的 TanStack 包（包括 Router 和 Start）当前版本均安全可安装。建议在 2026-05-11 安装过受影响版本的用户轮换所有可访问的凭据。
- 📚 **教训与改进**：缺乏内部警报机制、`pull_request_target` 工作流未审计、第三方操作使用了浮动引用、npm 的“有依赖则不可取消发布”策略导致延迟，以及 OIDC 信任发布缺乏逐次审核。未来将加强监控和审计。

---

### [浏览器对大网站区别对待 — 丹·奥德尔](https://denodell.com/blog/browsers-treat-big-sites-differently)

**原文标题**: [
      Browsers Treat Big Sites Differently — Den Odell
    ](https://denodell.com/blog/browsers-treat-big-sites-differently)

### 概述总结
浏览器对不同网站给予特殊渲染处理，Safari 和 Firefox 通过域名检测注入修复代码，而 Chrome 因市场主导地位无需此类操作，这反映了现代网络开发中 Chrome 的垄断地位。

- 🔍 Safari 和 Firefox 的代码中内置了针对特定域名的修复逻辑，例如 TikTok、Netflix、Instagram 甚至 SeatGuru 都会获得特殊渲染处理。
- 🛠️ Firefox 的`about:compat`页面列出了可开关的网站特定干预措施，包括注入 CSS/JavaScript 和修改用户代理字符串。
- 🎥 Safari 的`Quirks.cpp`文件包含针对 Facebook、X（Twitter）、Reddit 等网站的 PiP 视频修复，以及 Amazon 产品图片的触摸事件处理。
- ⚠️ Chrome 不需要类似修复，因为超过 80% 的用户使用 Chromium 浏览器，开发者默认以 Chrome 为标准构建网站。
- 🔄 这形成了反馈循环：开发者针对 Chrome 开发，用户遇到其他浏览器问题后转向 Chrome，进一步巩固其主导地位。
- 📋 修复范围广泛，包括滚动行为、触摸事件、视口计算、图片 MIME 类型处理等数千行代码。
- 💡 浏览器厂商选择直接修复而非等待网站更新，因为后者可能耗时数月且未必成功。
- 🧪 建议开发者定期在 Firefox 和 Safari 中测试网站，避免依赖 Chrome 的隐性兼容性。

---

### [获取失败](https://css-tricks.com/why-keyboard-users-cant-scroll-your-overflow-containers/)

**原文标题**: [Failed to retrieve](https://css-tricks.com/why-keyboard-users-cant-scroll-your-overflow-containers/)

无法总结：获取内容失败，状态码 415。

---

### [控制无限动画的速度](https://css-tip.com/speed-control/)

**原文标题**: [Control the Speed of Infinite Animations](https://css-tip.com/speed-control/)

### 概述总结
通过`animation-composition: add`和双动画叠加，实现悬停时控制无限动画速度、方向或暂停的 CSS 技巧。

- 🎛️ **核心原理**：利用`animation-composition: add`叠加两个相同动画，通过暂停/运行第二个动画来调节整体速度。
- ⚡ **速度因子控制**：通过 CSS 变量`--s`调整速度（>1 加速，0-1 减速，0 停止，<0 反向）。
- 🛠️ **基础代码结构**：定义主动画与辅助动画，辅助动画通过`abs()`计算时长并默认暂停，悬停时恢复运行。
- 🔄 **兼容性处理**：针对`if()`条件支持不足，提供备用方案：分别定义`init`和`control`两个关键帧动画，`control`动画使用`sign()`函数控制方向。
- 🖱️ **交互示例**：支持旋转、滚动字幕（`offset-distance`）、发光边框（CSS 变量）等场景，悬停触发速度变化。
- 🎯 **灵活扩展**：只需替换`rotate`为其他动画属性（如`translate`、`opacity`），即可应用于不同效果。

---

### [一个香草路由实验 · 丹妮拉·巴伦](https://danielabaron.me/blog/a-vanilla-routing-experiment/)

**原文标题**: [A Vanilla Routing Experiment · Daniela Baron](https://danielabaron.me/blog/a-vanilla-routing-experiment/)

本文探讨了使用原生 JavaScript 构建客户端路由的实践，分析了其优缺点，并提供了完整的实现方案。

- 🧭 概述：作者尝试用纯 JavaScript 实现 SPA 路由，发现看似简单但实际面临多个挑战，包括视图逻辑分离、浏览器导航、深度链接、无效路由、部署路径和回归测试等问题。
- 🔄 视图逻辑分离：初始实现将视图逻辑混入路由类，违反了关注点分离原则。通过重构为视图目录结构（每个视图包含独立模板和脚本），并使用 ES6 动态导入加载视图模块，实现了路由与视图逻辑的解耦。
- ⬅️ 浏览器导航修复：初始实现导致浏览器后退/前进按钮产生重复历史记录。通过区分用户点击（pushState=true）和浏览器导航（pushState=false），以及初始加载不推送状态，解决了该问题。
- 🔗 深度链接支持：直接访问 URL（如/about）会因服务器返回 404 而失败。通过创建 404.html 页面捕获目标 URL 并重定向到 index.html，再由路由恢复路径，实现了深度链接支持。
- ❌ 无效路由处理：当用户访问未注册路由时，路由器会显示自定义 404 页面，避免空白页或静默重定向。
- 🌐 部署路径适配：GitHub Pages 等平台使用子路径部署，导致 URL 构建错误。通过 ES 模块的 import.meta.url 动态获取基础路径，并构建完整 URL，解决了部署路径问题。
- 🧪 回归测试必要性：自定义路由需要手动测试浏览器后退/前进、刷新、直接 URL 访问等行为。作者引入 Playwright 端到端测试，通过自动化测试确保路由功能稳定。
- ⚖️ 权衡与适用场景：原生路由适合小型项目或教育目的，但缺乏 URL 参数、嵌套路由、查询字符串解析等高级功能。对于复杂项目，使用成熟框架可能更高效。

---

### [9 次 Web 平台受库影响 | Jad Joubran](https://jadjoubran.io/blog/web-platform-influenced-by-libraries)

**原文标题**: [9 Times the Web Platform Was Influenced by Libraries | Jad Joubran](https://jadjoubran.io/blog/web-platform-influenced-by-libraries)

以下是您提供的文章摘要，包含概述和要点列表：

概述摘要  
网络平台并没有发明大多数最佳 API，而是通过库的实践和反馈逐步标准化了这些功能。

- 📜 **querySelector 和 querySelectorAll**：从 Dojo 和 jQuery 的 `$()` 演变而来，简化了 DOM 元素选择，替代了手动遍历。
- 🔘 **popovertarget 和 command**：受 Bootstrap 的 `data-*` 属性启发，用 HTML 属性替代 JavaScript 实现按钮与弹窗的声明式绑定。
- 🎨 **classList**：源自 jQuery 的 `.addClass()` 等方法，提供了更简洁的类名操作，无需手动处理字符串。
- 🧰 **字符串和数组的实用方法**：如 `startsWith`、`includes`、`flat` 等，来自 Underscore、Lodash 等库，标准化后成为原生功能。
- 📦 **structuredClone**：从 Lodash 的 `_.cloneDeep` 和 `JSON.parse/stringify` 技巧进化而来，支持深度克隆复杂对象（如 Date、Map）。
- ⏳ **Promises**：基于 Promises/A+ 规范，从 Dojo、jQuery、Bluebird 等库演变，成为异步编程的标准模式。
- 📂 **ES Modules**：从 CommonJS 和 AMD 模块系统演化而来，提供原生的 `import/export` 语法，统一了代码分割。
- 🕰️ **Temporal**：由 Moment.js 维护者推动，替代了有缺陷的 Date 对象，提供不可变、时区感知的日期处理。
- 🔍 **Element.closest()**：源自 jQuery 的 `.closest()`，简化了 DOM 祖先元素的查找，常用于事件委托。

---

### [学习 JavaScript - 33 个 JavaScript 概念](https://33jsconcepts.com/)

**原文标题**: [Learn JavaScript - 33 JavaScript Concepts](https://33jsconcepts.com/)

### 概述
该资源是一个全面的 JavaScript 学习指南，涵盖 33 个核心概念，旨在帮助不同水平的开发者深入理解 JavaScript 的工作原理，从基础到高级主题均有涉及。

- 📚 **核心概念覆盖**：包含从原始类型、作用域、闭包等基础，到事件循环、异步编程、函数式编程及设计模式等高级主题。
- 👥 **面向多元受众**：适合初学者建立扎实基础、自学者填补知识空白、求职者准备面试以及经验开发者巩固模型。
- 🧩 **结构化学习路径**：概念按逻辑顺序组织，每个页面提供清晰解释、可运行代码示例、图解和深度资源。
- 🌍 **社区驱动项目**：由 Leonardo Maldonado 创建，获 GitHub 2018 年顶级开源项目认可，有数百贡献者和 40+ 种语言翻译。
- 🚀 **实用学习体验**：强调“理解而非复制”，包含知识检查，帮助开发者从复制代码进阶到自信交付。

---

### [React 中的无障碍性：常见错误及修复方法 - Certificates.dev](https://certificates.dev/blog/accessibility-in-react-common-mistakes-and-how-to-fix-them)

**原文标题**: [Accessibility in React: Common Mistakes and How to Fix Them - Certificates.dev](https://certificates.dev/blog/accessibility-in-react-common-mistakes-and-how-to-fix-them)

本文探讨了 React 应用中常见的无障碍性问题，并提供了具体的修复方法，涵盖语义化标签、焦点管理、标签与错误关联、动态更新通知等方面。

- 🏗️ **使用正确的 HTML 元素**：用 `<button>` 替代 `<div onClick>`，用 `<a>` 替代 `<div>` 模拟链接，避免重复实现浏览器原生功能。
- 📑 **维护标题层级**：确保 `<h1>` 到 `<h6>` 按逻辑顺序排列，不因样式跳过层级；使用 `<header>`、`<nav>`、`<main>` 等地标元素辅助导航。
- 🏷️ **为交互元素添加标签**：所有表单输入需关联 `<label>`，图标按钮使用 `aria-label` 或隐藏文本，图片需添加 `alt` 属性（装饰性图片用 `alt=""`）。
- 🔗 **使用 `useId` 连接标签和错误**：通过 `aria-describedby` 将错误信息与输入框关联，并用 `aria-invalid` 标记无效状态；保持错误容器常驻 DOM 以便屏幕阅读器检测内容变化。
- 🎯 **管理焦点**：页面切换时聚焦到新内容标题（如 `<h1 tabIndex={-1}>`），模态框使用原生 `<dialog>` 自动处理焦点陷阱和 Escape 关闭；删除元素后需将焦点移至合理位置。
- 📢 **通知动态更新**：使用 `role="alert"`（紧急）或 `role="status"`（非紧急）包裹动态内容，并保持容器常驻 DOM 以触发屏幕阅读器朗读。
- 🎨 **基于 ARIA 属性设置样式**：利用 `aria-selected`、`aria-expanded` 等属性通过 CSS 或 Tailwind 进行样式控制，避免额外状态管理。
- 🔍 **快速审计清单**：检查非语义化点击元素、标题层级、表单标签、图标按钮/链接的标签、图片 alt 属性、错误关联、模态框焦点、条件渲染后的焦点、动态更新通知，并通过 Tab 键和自动化工具（如 axe-core）进行测试。

---

### [编程文摘：邮件通讯](https://programmingdigest.net/?utm_source=web-archive&utm_campaign=react)

**原文标题**: [Programming Digest: Email Newsletter](https://programmingdigest.net/?utm_source=web-archive&utm_campaign=react)

概述摘要  
- 📧 每周一封精心策划的邮件，面向软件工程师  
- 👥 已有超过 23,202 名软件工程师订阅  
- 📖 精选文章并附简短摘要，节省阅读时间  
- 🧠 每周学习新知识  
- 💬 读者反馈：内容实用，如 API 设计和高效方法  
- 🏢 读者来自各大软件公司  
- 📅 2013-2026 年持续运营，提供隐私和广告选项

---

### [科技领导力：邮件通讯](https://leadershipintech.com/?utm_source=web-archive&utm_campaign=react)

**原文标题**: [Leadership in Tech: Email Newsletter](https://leadershipintech.com/?utm_source=web-archive&utm_campaign=react)

本内容介绍了一份面向技术领导者的精选邮件通讯，旨在帮助 CTO、工程经理及资深工程师提升领导力。

- 📬 每周一、四发送一封邮件，覆盖超过 28,851 名工程领导者
- ⏱️ 精选文章并附简短摘要，节省寻找优质内容的时间
- 📚 每周学习新知识，聚焦领导力、架构、沟通等关键主题
- 💬 读者好评如潮，称赞其对领导力文章的精挑细选及对沟通、授权等技能的强调
- 🌐 读者来自全球顶尖科技公司，如 Google、Meta、Microsoft、Apple 等
- 📅 通讯由 Bonobo Press 运营，提供隐私保护和广告选项

---

### [C# 文摘：电子邮件通讯](https://csharpdigest.net/?utm_source=web-archive&utm_campaign=react)

**原文标题**: [C# Digest: Email Newsletter](https://csharpdigest.net/?utm_source=web-archive&utm_campaign=react)

本内容介绍了 C# Digest——一份为.NET 开发者精心策划的每周邮件通讯。

- 📧 每周一封邮件，精选C#文章并附简短摘要，帮助开发者节省时间。
- 👥 已有超过20,449名C#工程师订阅，读者反馈实用性强。
- 💡 内容涵盖 LINQ、DiagnosticListener、Operation Result Pattern 等实用技术。
- 🏢 读者来自全球各大公司，深受.NET 工程师信赖。
- 🔒 提供隐私保护及广告服务，由 Bonobo Press 运营。

---

### [让开发者保持最新动态 – Bonobo Press](https://bonobopress.com/)

**原文标题**: [Keeping developers up to date â Bonobo Press](https://bonobopress.com/)

Bonobo Press 自 2013 年起，通过简洁的软件资讯通讯，服务超过 80,000 名开发者与 IT 专业人士。

- 📰 提供面向开发者、技术主管和 CTO 的精选资讯通讯，内容简洁高效
- 🎯 提供广告服务，精准触达软件工程师、团队领导及 IT 决策者
- 📞 欢迎联系咨询、建议或广告合作，联系方式公开
- 📅 版权覆盖 2013 至 2026 年，并设有使用条款

---

### [过往新闻简报：第 1 页](https://reactdigest.net/newsletters)

**原文标题**: [Past Newsletters: Page 1](https://reactdigest.net/newsletters)

以下是对所提供内容的总结：

React Digest 新闻简报涵盖了 2026 年 1 月至 5 月期间的重要 React 动态，包括安全漏洞、性能优化、新特性、最佳实践和开发者经验分享。

- 🔒 发现 React Flight 协议存在严重 RCE 漏洞，默认 Next.js 应用易受攻击；TanStack npm 包遭 GitHub Actions 攻击，30 分钟内泄露云密钥
- ♿ 常见 React 无障碍错误包括缺失语义、焦点断裂和静默动态更新；React Router 7 处理模态框、加载器和反馈无需 useEffect
- 🪝 React 19 新钩子 useTransition 和 useActionState 简化异步代码，自动跟踪待处理状态并修复竞态条件
- ⚡ Railway 从 Next.js 迁移到 Vite，构建时间从 10 分钟降至 2 分钟；研究发现只有 lodash 和 moment.js 导致真正包体积膨胀
- 🏗️ MDN 用服务端 HTML 和 Lit Web 组件替换 React SPA，开发构建从 2 分钟降至 2 秒；GitHub 通过减少 DOM 膨胀和虚拟化加速大 PR 差异
- 🔄 React Fiber 将渲染拆分为~5ms 块，允许紧急更新中断慢任务；React Native 0.85 增加原生 Flexbox 动画支持
- 📚 指南揭示初级开发者所需隐性知识；文章指出信号无法解决 React 怪癖，并展示 Next.js App Router 错误处理技巧
- 🪝 use() 钩子打破常规，在渲染时读取 Promise 并与 Suspense 配合，消除 useEffect 数据获取反模式
- 🗑️ 86% 前端项目存在内存泄漏，500 个 React、Vue 和 Angular 仓库发现 55,864 个泄漏模式，来自定时器和事件清理缺失
- 🧠 AI 调试能力、React 新 ViewTransition 元素、单元测试见解和 Copilot CLI 工程细节；避免过度使用 useCallback
- 🎨 探索 React 最佳实践、2025 年生态系统演变、Client Components 和 React transitions 性能提升；避免 TanStack 表单陷阱
- 🤖 AI 在 React 编码中表现参差不齐；30 年 Web 发展历程；前端测试技巧；React transitions 和类型安全组件
- 🎉 2025 年最佳 React 文章包括设计模式、状态管理、重渲染和函数式编程

---

### [隐私](https://reactdigest.net/privacy)

**原文标题**: [Privacy](https://reactdigest.net/privacy)

本隐私政策概述了 React Digest 如何收集、使用和保护您的个人信息，强调透明度和数据安全。

- 🔒 我们仅在收集前明确目的，并仅用于指定目的或法律要求，除非获得同意。
- ⏳ 个人信息仅保留至实现目的所需的时间。
- ⚖️ 通过合法公平的方式收集信息，并确保数据准确、完整且最新。
- 🛡️ 采取合理安全措施保护信息，防止丢失、盗窃或未经授权的访问。
- 📧 收集您的电子邮件地址仅用于发送新闻通讯，不用于其他目的。
- 🚫 我们坚决反对垃圾邮件，您可随时通过邮件中的取消订阅链接退订。
- 👶 不收集 13 岁以下儿童的信息，网站也不面向儿童设计。
- 📋 根据英国《数据保护法》，您可请求访问我们存储的您的信息（发送邮件至[email protected]）。
- 🗑️ 如需删除数据，请发送邮件至[email protected]申请。
- 📅 政策有效期至 2026 年，由 Bonobo Press 管理。

---

### [媒体资料包 – 倭黑猩猩出版社](https://bonobopress.com/media-kit/)

**原文标题**: [Media Kit â Bonobo Press](https://bonobopress.com/media-kit/)

Bonobo Press 提供面向软件开发者和技术领导者的高参与度新闻通讯广告服务，覆盖多个细分领域，并提供详细的定价和流程说明。

- 📊 **高参与度受众**：新闻通讯的参与度是行业基准的两倍以上，通过严格的列表清洗确保读者活跃度。
- 🎯 **Leadership in Tech**：面向技术领导者（CTO、工程经理等），22,325 订阅者，开放率 57.95%，每次赞助$2,235，预计点击 365-585 次。
- 💻 **Programming Digest**：面向软件工程师，20,032 订阅者，开放率 50.41%，每次赞助$985，预计点击 273-493 次，CPC 较低。
- 🔧 **C# Digest**：面向.NET/C#开发者，17,098 订阅者，开放率 54.92%，每次赞助$1,220，预计点击 411-631 次，CTR 最高。
- ⚛️ **React Digest**：面向前端开发者，20,075 订阅者，开放率 54.06%，每次赞助$1,375，预计点击 303-523 次。
- 📝 **纯文本广告格式**：广告以文本形式嵌入新闻通讯主内容，包括链接、标题和描述，截止日期为发布前 4 天。
- 🗓️ **预订流程**：需提前几周联系，流程包括产品介绍、排期、发票付款锁定、素材交付、广告上线和效果报告。
- 🤝 **成功案例**：合作伙伴包括 Okta、GitLab、Datadog、MongoDB 等，常重复赞助。

---

