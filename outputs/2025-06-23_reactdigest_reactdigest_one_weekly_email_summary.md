### [React 文摘：电子邮件通讯](https://reactdigest.net/)

**原文标题**: [React Digest: Email Newsletter](https://reactdigest.net/)

《React Digest》是一份专为 React 开发者精心策划的周更简报，汇聚前端工程师的精选内容与实用资源。  

- 📰 **精选周更邮件**：为 22,604+ 名前端工程师提供每周精选文章与简短摘要。  
- ⏱️ **高效省时**：帮助开发者节省筛选优质内容的时间，直接获取有价值的信息。  
- 🌱 **持续学习**：每周推送新知识，涵盖 React 生态最新动态（如并发模式等实战技巧）。  
- 🗣️ **用户好评**：读者称赞内容实用、更新及时，文章质量高且易于理解。  
- 🌍 **广泛受众**：被全球多家知名科技公司的前端团队订阅并信赖。  
- ©️ **版权信息**：由 Bonobo Press 运营，涵盖隐私政策与广告合作说明（2013-2025）。

---

### [视频会议中的实时手势识别 | Software Mansion](https://blog.swmansion.com/real-time-gesture-recognition-in-videoconferencing-4711855a1a53?gi=6afc1d3ff011)

**原文标题**: [Real-Time Gesture Recognition in Videoconferencing | Software Mansion](https://blog.swmansion.com/real-time-gesture-recognition-in-videoconferencing-4711855a1a53?gi=6afc1d3ff011)

实时视频会议中的手势识别技术概述

- 🚀 手势识别技术通过 AI 增强视频会议体验，如 Apple 的 Reactions 和 Snapchat 滤镜  
- 🤖 核心技术包括计算机视觉、低延迟通信和实时视频合成，依赖 WebRTC、WebGPU 等浏览器 API  
- 🛠️ 实现方案：结合 MediaPipe 手部关键点检测、Smelter 视频合成和 Fishjam 的 WebRTC 服务  
- ⚙️ 关键挑战：浏览器端实时运行 AI 模型需使用 Web Worker 避免主线程阻塞  
- ✋ 超时手势识别逻辑：检测双手垂直/手指伸直/中指触碰掌心等特征  
- 🎥 动态效果触发：通过 React 状态管理实现手势驱动的动画叠加（如文字滑入效果）  
- 🌐 开源资源：提供完整演示 Demo 和 GitHub 源码，支持 Chrome/Safari 浏览器  
- 🔮 未来展望：Insertable Streams API 等新技术将进一步提升浏览器视频处理能力  

（注：根据用户要求，省略了"overview summary"标题，直接以内容开头）

---

### [OAuth 工作原理](https://clerk.com/blog/how-oauth-works?utm_source=react-digest&utm_medium=newsletter&utm_campaign=oauth&utm_content=06-23-25&dub_id=56bUU5JpiDUnb9pn)

**原文标题**: [How OAuth Works](https://clerk.com/blog/how-oauth-works?utm_source=react-digest&utm_medium=newsletter&utm_campaign=oauth&utm_content=06-23-25&dub_id=56bUU5JpiDUnb9pn)

OAuth 是一种开放授权标准，允许第三方应用在无需用户共享密码的情况下访问其部分数据。本指南通过实际代码示例和安全最佳实践，详细解释了 OAuth 的作用机制，特别是授权码流程（Authorization Code Flow），并介绍了相关术语、常见用例及安全注意事项。

- 🔐 OAuth 允许第三方应用访问用户数据而无需密码，遵循最小权限原则
- 🔄 授权码流程（Authorization Code Flow）是 OAuth 的核心机制，分两步交换令牌确保安全性
- 💻 实际代码示例展示了如何实现 OAuth 集成，包括请求授权和处理回调
- 🛡️ 安全措施包括 PKCE（Proof Key for Code Exchange）、state 参数和动态客户端注册
- 🔑 访问令牌（Access Token）和刷新令牌（Refresh Token）的机制及过期处理
- 🌐 公开客户端（如 SPA 和移动应用）与保密客户端的区别及安全考量
- 📝 动态客户端注册的潜在风险与适用场景
- 🔗 OAuth 与 OIDC（OpenID Connect）的关系及如何结合使用
- 🛠️ 使用 Clerk 简化 OAuth 实现，自动处理安全性和端点配置

---

### [将 React 的<ViewTransition>引入原生 JS](https://plainvanillaweb.com/blog/articles/2025-06-12-view-transitions/)

**原文标题**: [Bringing React's <ViewTransition> to vanilla JS](https://plainvanillaweb.com/blog/articles/2025-06-12-view-transitions/)

overview summary  
本文作者表达了对 React 的喜爱，但也指出其过度设计的倾向，提倡探索更简单、更原生的解决方案。文章以视图过渡（View Transitions）为例，详细介绍了其基本原理、浏览器兼容性问题及实际应用中的挑战，并对比了 React 的解决方案与原生实现的优劣。最后，作者分享了一个基于原生 JavaScript 的视图过渡实现，并提到了一些高级话题如 Shadow DOM 的局限性。

- 🚀 React 是现代 Web 开发的默认选择，但有时过度设计，简单方案可能更优。  
- 🎨 视图过渡（View Transitions）允许浏览器在页面状态变化时实现平滑动画，但兼容性有限（仅 Chrome/Edge/Safari）。  
- ⚠️ 实际应用中存在诸多问题：Firefox 不支持、命名冲突、过渡中断、用户输入阻塞等。  
- 🧙 React 通过魔法般的智能批处理和队列机制解决这些问题，但增加了复杂性。  
- 🔄 作者尝试用原生 JavaScript 实现类似功能，通过队列管理过渡任务，避免中断。  
- 📦 示例代码展示了客户端路由和视图过渡的结合，代码量接近 React 但更轻量。  
- 👻 Shadow DOM 中元素需特殊处理才能参与过渡，增加了复杂度。  
- 🔗 完整代码和自定义元素实现可在 GitHub 示例库中查看。

---

### [使用 useEffect 获取数据——为什么即使是简单应用，你也应该直接选择 react-query](https://reactpractice.dev/articles/data-fetching-with-useeffect-why-you-should-go-straight-to-react-query-even-for-simple-apps/)

**原文标题**: [Data fetching with useEffect - why you should go straight to react-query, even for simple apps](https://reactpractice.dev/articles/data-fetching-with-useeffect-why-you-should-go-straight-to-react-query-even-for-simple-apps/)

文章讨论了在 React 中使用`useEffect`进行数据获取的局限性，并推荐直接使用`react-query`库，即使是简单的应用场景。

- 🏁 使用`useEffect`进行数据获取虽然简单，但需要大量样板代码，且容易引发竞态条件问题。  
- 🐛 基本示例中未处理清理逻辑，可能导致应用显示过时的请求结果。  
- 🛠️ 改进后的示例通过`ignore`标志避免竞态条件，但代码复杂度增加。  
- ⏳ 处理加载和错误状态需要更多代码，进一步增加复杂性。  
- 🔄 自定义钩子`useFetch`可复用逻辑，但仍缺乏缓存等高级功能。  
- 🚀 `react-query`提供了内置的加载/错误处理、缓存等功能，大幅简化代码。  
- 📦 最终示例展示`react-query`的简洁性，推荐作为默认数据获取方案。  
- 🔗 文章附带代码沙盒链接，供读者实践所有示例。

---

### [如何创建自己的简易 useState 钩子](https://www.deepintodev.com/blog/how-to-create-your-own-simple-use-state-hook)

**原文标题**: [How to Create Your Own Simple useState Hook](https://www.deepintodev.com/blog/how-to-create-your-own-simple-use-state-hook)

本文介绍了如何从零开始实现一个简化版的 React `useState`钩子，并解释了 React 钩子规则背后的原理。

- 🏗️ 通过逐步构建简化版`useState`函数，展示了其核心机制：返回状态值和更新函数
- 🔄 使用闭包实现状态持久化，避免每次渲染时重置状态值
- 📊 采用数组存储多个状态值，通过索引跟踪不同`useState`调用的状态
- ⚙️ 实现重新渲染机制，确保状态更新后 UI 同步刷新
- 🔄 每次渲染前重置调用索引，保证状态顺序一致性
- 🔒 利用闭包保存状态索引，解决异步更新时的索引错位问题
- ⚠️ 解释了 React 钩子必须在顶层调用的原因：依赖稳定的调用顺序
- 🧩 说明为什么钩子只能在 React 函数组件中使用（状态与组件实例关联）
- 💡 最终实现支持多个独立状态管理的简化版`useState`

---

### [零并非本地优先。它更胜一筹。 :: jjenzz](https://jjenzz.com/zero-is-not-local-first-its-better/)

**原文标题**: [Zero is Not Local-First. It's Better. :: jjenzz](https://jjenzz.com/zero-is-not-local-first-its-better/)

Zero 并非完全的本地优先（local-first）方案，而是采用「部分同步优先」模式，在保持服务器为数据源的同时优化客户端性能与响应速度。其核心设计通过选择性同步、预加载和同构化更新机制，平衡了数据控制与用户体验。

- 🌐 **部分同步优先**：Zero 仅同步当前查询的特定数据（如单条待办事项），而非全量数据，避免本地存储过载和性能下降。  
- 🚀 **预加载优化**：通过 `preload()` API 提前缓存数据到本地（如 IndexedDB），减少页面切换时的加载延迟，支持按需清理。  
- 🔄 **同构化数据更新**：客户端与服务器共享同一套 mutator 逻辑，支持乐观更新（Optimistic UI），自动处理临时状态不一致。  
- ⚖️ **服务器为数据源**：采用游戏行业的「服务器调和」技术，确保最终一致性，便于调试且无需客户端加密数据。  
- 🛠️ **灵活后端集成**：支持 Postgres、MongoDB 等现有数据库，无供应商锁定，适配既有技术栈。  
- ⏳ **离线处理限制**：冲突解决机制不适用于长期离线场景，失败操作会回滚至服务器状态。  
- 🔮 **开发阶段**：目前为 Alpha 版本，API 快速迭代中，可关注其路线图获取更新。

---

### [一丝不苟](https://www.meticulous.ai/?utm_source=react_digest)

**原文标题**: [Meticulous](https://www.meticulous.ai/?utm_source=react_digest)

Meticulous AI 提供了一种无需编写或维护测试的自动化测试解决方案，通过记录用户交互并生成覆盖所有边缘情况的测试套件，帮助开发团队快速、可靠地发布代码。

- 🚀 **无需编写测试** - Meticulous AI 自动生成并维护测试套件，覆盖所有用户流程和边缘情况。  
- 🔍 **记录用户交互** - 通过在开发、预发布和生产环境中添加脚本，记录用户会话以生成测试。  
- 🤖 **智能测试生成** - AI 引擎分析代码分支，生成视觉端到端测试，确保全面覆盖。  
- ⚡ **快速集成** - 轻松与现有 CI 集成，无需额外配置测试账户或模拟数据。  
- 🛠️ **零维护** - 测试套件随应用演进自动更新，无需手动修复过时测试。  
- 🚫 **无抖动测试** - 基于 Chromium 的确定性调度引擎，消除测试中的随机失败。  
- 📊 **高效并行测试** - 支持大规模并行测试，数千个测试可在 120 秒内完成。  
- 💬 **客户认可** - 被 Dropbox、WithPower 和 Lattice 等 100 多家组织信任，显著提升开发效率和代码质量。  
- 🔗 **多框架支持** - 兼容 NextJS、React、Vue、Angular、Nuxt 和 SvelteKit 等主流前端框架。  
- 🎯 **快速上手** - 几分钟内完成设置，立即为整个应用生成测试覆盖。

---

### [你应该了解的即将推出的 JavaScript 新特性 - DEV 社区](https://dev.to/maxprilutskiy/upcoming-javascript-features-you-should-know-about-178h)

**原文标题**: [Upcoming JavaScript Features You Should Know About - DEV Community](https://dev.to/maxprilutskiy/upcoming-javascript-features-you-should-know-about-178h)

概述  
文章介绍了即将推出的 JavaScript 新特性，这些特性将显著改变开发者的编码方式，包括管道操作符、模式匹配、Temporal API、资源管理和装饰器等。这些特性旨在解决长期困扰开发者的问题，如代码可读性、复杂条件处理、日期处理和资源管理等。

- 🚀 **管道操作符提升代码可读性**：通过 `|>` 操作符简化嵌套函数调用，使数据流更清晰。  
- 🧩 **模式匹配简化复杂条件逻辑**：替代繁琐的 `if/else` 和 `switch`，支持结构化数据匹配和析构。  
- 📅 **Temporal API 解决日期处理问题**：提供不可变日期对象和时区支持，替代易错的 `Date` 对象。  
- 🧹 **资源管理消除内存泄漏**：通过 `using` 和 `await using` 自动管理资源释放，避免手动清理。  
- ✨ **装饰器增强功能而不改变核心逻辑**：为类和方法添加日志、验证等横切关注点，保持代码整洁。  
- 🔧 **如何立即使用这些特性**：通过 Babel、Vite 等工具配置插件或 polyfill，提前体验新特性。  

这些特性不仅优化了代码结构，还提升了开发效率和可维护性，部分已进入 TC39 流程的后期阶段，开发者可以提前尝试。

---

### [JavaScript 的早期编写历程](https://www.trevorlasn.com/blog/revisiting-legacy-javascript)

**原文标题**: [How JavaScript Was Written Back In the Day](https://www.trevorlasn.com/blog/revisiting-legacy-javascript)

文章回顾了 2006-2015 年间 JavaScript 的开发模式和技术解决方案，探讨了早期框架如 jQuery 如何应对浏览器兼容性问题，并展示了在没有现代 JavaScript 功能的情况下开发者如何创造性地解决问题。

- 🔍 作者研究了 2006-2015 年的 JavaScript 代码，发现早期框架的解决方案令人印象深刻。  
- 🌐 2006 年 Web 开发面临浏览器兼容性问题，特别是 IE6 的市场主导地位。  
- 🛠️ jQuery 1.0 通过抽象浏览器差异，提供一致的 API，简化了 DOM 操作和 AJAX 请求。  
- 🔄 jQuery 的 API 重载设计使其使用起来非常直观，例如`$('#element').addClass('active').fadeIn()`。  
- 📜 早期 JavaScript 缺乏现代功能如`Array.from()`和展开运算符，开发者使用`[].push.apply(this, arguments)`等变通方法。  
- 🏗️ 2010 年后 JavaScript 应用变得更复杂，事件系统使用手动回调管理，变量声明集中在函数顶部以避免作用域问题。  
- 🔄 使用`_.rest(arguments)`处理剩余参数，因为当时没有`...args`语法。  
- 📡 在`fetch()` API 出现前，AJAX 请求依赖`XMLHttpRequest`或`ActiveXObject`。  
- 🔧 开发者使用`|| function()`模式提供 polyfill，手动复制对象属性，使用`for...in`循环迭代属性。  
- 🏛️ ES6 之前，构造函数和原型方法是标准的 OOP 实现方式，`Object.create(null)`创建无原型的对象。  
- 🔄 全局变量如`Dep.target`用于状态跟踪，`while (i--)`循环用于性能优化的反向迭代。  
- 💡 这些早期模式展示了开发者在 ES3 和 ES5 限制下的创造性解决方案，尽管许多技术现已过时。

---

### [多异步本地存储 | Nico 的博客](https://www.nico.fyi/blog/multiple-async-local-storage)

**原文标题**: [Multiple Async Local Storage | Nico's Blog](https://www.nico.fyi/blog/multiple-async-local-storage)

文章概述了如何在 Next.js 中使用多个异步本地存储（Async Local Storage）来避免属性钻取（prop drilling），类似于 React 中的多上下文（context）用法，以保持代码模块化。

- 🚀 异步本地存储可以像 React Context 一样嵌套使用，避免属性钻取问题。  
- 🔧 通过`request-context.ts`创建请求上下文，存储搜索参数、路径参数和请求体。  
- 🛠️ 使用`runWithMultipleContexts`函数实现多上下文嵌套，支持模块化代码结构。  
- 📂 在路由处理器（如`route.ts`）中，结合用户上下文和请求上下文调用主函数（如`getData`）。  
- 📊 在`getData`函数中，通过`getRequestContext`和`getUserContext`轻松获取上下文数据。  
- 🔄 这种方法保持了代码的清晰性和可维护性，适用于需要多层数据传递的场景。  
- 🔖 相关技术栈：Next.js、TypeScript、异步本地存储。

---

### [CSS 层叠层与 BEM 与实用类：特异性控制 —— Smashing Magazine](https://www.smashingmagazine.com/2025/06/css-cascade-layers-bem-utility-classes-specificity-control/)

**原文标题**: [CSS Cascade Layers Vs. BEM Vs. Utility Classes: Specificity Control — Smashing Magazine](https://www.smashingmagazine.com/2025/06/css-cascade-layers-bem-utility-classes-specificity-control/)

概述总结  
Victor Ayomipo 探讨了 CSS 中特异性控制的三种方法：BEM、实用类（Utility Classes）和 CSS 级联层（Cascade Layers）。文章分析了每种方法的优缺点、适用场景以及如何结合使用它们来有效管理 CSS 特异性问题。

- 🎯 **CSS 特异性问题**  
  CSS 特异性常导致样式覆盖问题，开发者通常通过`!important`解决，但这种方法风险高且不推荐。

- 📚 **特异性基础**  
  浏览器通过 CSS 级联算法决定哪个样式声明生效，特异性分数高的规则优先。随着项目扩大，特异性冲突加剧。

- 🏗️ **BEM 方法**  
  BEM 通过命名约定（Block-Element-Modifier）保持低特异性，使代码可预测且易于维护。但类名可能冗长，且复用性受限。

- ⚡ **实用类方法**  
  实用类通过原子化样式（如`p-2`、`text-red`）避免特异性问题，每个类特异性相同。适合快速开发，但 HTML 可能显得臃肿。

- 🏗 **CSS 级联层**  
  `@layer`允许开发者通过分层控制样式优先级，无视特异性分数。适合管理遗留代码或第三方样式，但需谨慎分层以避免滥用。

- 🔄 **方法比较与结合**  
  - BEM 适合设计系统和团队协作。  
  - 实用类适合快速原型开发。  
  - 级联层适合复杂项目或样式覆盖。  
  结合级联层与 BEM 或实用类可优化特异性控制。

- 🛠️ **实践建议**  
  保持特异性最低，优先使用级联层管理样式优先级，避免`!important`。根据项目需求选择或组合方法。

---

### [CSS 样式间隙新方案  |  博客  |  Chrome 开发者](https://developer.chrome.com/blog/gap-decorations)

**原文标题**: [A new way to style gaps in CSS  |  Blog  |  Chrome for Developers](https://developer.chrome.com/blog/gap-decorations)

Chrome 和 Edge 139 推出了 CSS 间隙装饰功能，为 Flex、Grid 和多列布局中的间隙提供了新的样式解决方案，无需依赖边框或伪元素等传统方法。

- 🎨 **CSS 间隙装饰功能**：支持通过`column-rule`和新增的`row-rule`属性直接样式化间隙，提升视觉一致性和可维护性。  
- 🚀 **优势**：不影响布局、支持`repeat()`语法、减少冗余标记，并提供更多自定义选项（如`*rule-break`和`*rule-outset`）。  
- ⚙️ **开发者试用**：需在 Chrome 或 Edge 139 中启用实验性功能标志（`edge://flags`或`chrome://flags`）。  
- 📱 **示例演示**：包含汉堡菜单、笔记本布局和数独游戏等交互式案例，展示不同属性的实际应用。  
- 🐞 **反馈征集**：功能仍在开发中，开发者可提交 bug 或建议以帮助完善。  
- 📜 **许可证信息**：内容遵循 Creative Commons 4.0 许可，代码示例采用 Apache 2.0 许可。

---

### [JPEG 如何成为互联网的图像标准 - IEEE Spectrum](https://spectrum.ieee.org/jpeg-image-format-history)

**原文标题**: [How JPEG Became the Internet’s Image Standard - IEEE Spectrum](https://spectrum.ieee.org/jpeg-image-format-history)

JPEG 格式在三十年前成为互联网上分享数字照片的主导方式，至今仍在网络中占据重要地位。

- 📅 **历史背景**：JPEG 格式在三十年前成为互联网上分享数字照片的标准。  
- 🌐 **网络主导**：至今仍是网络上最常用的图像格式之一。  
- 📸 **技术优势**：因其高效的压缩算法，能在保持较好画质的同时减小文件大小。  
- 🔄 **持久性**：尽管有新技术出现，JPEG 因其兼容性和普及度仍难以被取代。  
- 📰 **作者观点**：Ernie Smith 通过其新闻通讯 Tedium 探讨了这一技术的长期影响。

---

### [使用 CSS 实现缩放动画：变换顺序有时很重要… - JakeArchibald.com](https://jakearchibald.com/2025/animating-zooming/)

**原文标题**: [Animating zooming using CSS: transform order is important… sometimes - JakeArchibald.com](https://jakearchibald.com/2025/animating-zooming/)

概述  
本文探讨了 CSS 中变换顺序对动画效果的影响，特别是缩放（scale）和平移（translate）的组合使用，以及如何通过调整顺序或使用其他方法实现更自然的动画效果。

- 🌀 **变换顺序的影响**：CSS 中`scale`和`translate`的顺序不同会导致动画效果差异，`scale`在前会放大平移效果，产生“俯冲”感。  
- 🔄 **默认动画机制**：CSS 规范通过填充和线性插值处理变换动画，但`scale`会非线性放大`translate`的效果。  
- 🛠️ **修复方法**：将`translate`置于`scale`之前，并手动调整平移值（乘以缩放系数）以实现平滑动画。  
- 📐 **开发工具优化**：使用 CSS 变量和`calc()`简化调整过程，例如`translate(calc(var(--x) * var(--scale)), calc(var(--y) * var(--scale)))`。  
- ⚠️ **伪解决方案的陷阱**：初始设置`rotate(0)`会触发 CSS 的矩阵转换，偶然实现预期效果，但依赖边缘情况不推荐。  
- 🎥 **3D 变换替代方案**：使用`perspective`和 3D 平移（如`translate-z`）模拟透视移动效果，与纯缩放动画的线性变化形成对比。  
- 🔍 **效果对比**：3D 变换在视觉上更接近真实透视变化，但缩放动画可能更适合“放大”意图的场景。  
- 🙏 **致谢**：感谢 Ana Rodrigues 的反馈帮助完善内容。  

（注：文末关于 Disqus 的吐槽未纳入摘要，因其与主题无关。）

---

### [我初学 ARIA 时希望有人告诉我的事 —— Smashing Magazine](https://www.smashingmagazine.com/2025/06/what-i-wish-someone-told-me-aria/)

**原文标题**: [What I Wish Someone Told Me When I Was Getting Into ARIA — Smashing Magazine](https://www.smashingmagazine.com/2025/06/what-i-wish-someone-told-me-aria/)

以下是按照您提供的模板总结的内容：

overview summary  
本文由设计师 Eric Bailey 撰写，旨在为初学者提供关于 ARIA（Accessible Rich Internet Applications）的实用指南。文章涵盖了 ARIA 的基本概念、历史背景、使用规则、常见误区以及实际应用中的注意事项，帮助读者更好地理解和运用 ARIA 来提升网页的可访问性。

- 🧠 **ARIA 的核心概念**  
  ARIA 是一种通过 HTML 标记为屏幕阅读器和语音控制软件提供额外信息的技术，用于增强交互性、目的和状态的传达。

- ⏳ **ARIA 的历史背景**  
  ARIA 最初发布于 2006 年，旨在弥补 HTML 在交互体验可访问性方面的不足，其设计反映了当时的操作系统交互范式。

- 📜 **ARIA 的使用规则**  
  ARIA 有五条基本规则，包括优先使用原生 HTML 元素、确保交互元素可通过键盘操作、避免在可聚焦元素上使用`role="presentation"`等。

- ❌ **常见误区**  
  ARIA 并非万能，滥用可能导致可访问性问题。例如，不应在已具有隐式角色的元素上重复声明 ARIA 角色。

- 🔍 **ARIA 的语法与声明**  
  ARIA 通过角色（roles）、状态（states）和属性（properties）来增强 HTML，其声明方式与 HTML 属性类似，但需注意其特定的语法规则。

- 🛠 **ARIA 的实际应用**  
  ARIA 常用于动态更新内容（如展开/折叠面板），需结合 JavaScript 实现交互逻辑，且仅通过 ARIA 无法自动赋予元素交互能力。

- 🌐 **ARIA 的跨平台支持**  
  ARIA 的支持情况因操作系统、辅助技术和浏览器版本而异，需通过实际测试确保其有效性。

- ⚠️ **注意事项**  
  `aria-label`和`aria-live`等属性使用需谨慎，避免因误用导致可访问性问题。此外，ARIA Authoring Practices Guide（APG）中的示例并非全部可直接使用。

- 🖥 **测试与验证**  
  建议使用 NVDA 或 JAWS 等主流屏幕阅读器进行测试，避免过度依赖 macOS VoiceOver，因其支持可能存在不足。

- 💡 **ARIA 的扩展用途**  
  ARIA 不仅可用于增强可访问性，还可用于 CSS 样式和 UI 测试，帮助构建更健壮的用户界面。

- ❤️ **ARIA 的终极目标**  
  ARIA 的核心是关注用户，确保残障人士能够与其他人一样无障碍地使用网络体验。

---

### [响应式编程很简单](https://romgrk.com/posts/reactivity-is-easy/)

**原文标题**: [Reactivity is easy](https://romgrk.com/posts/reactivity-is-easy/)

概述  
本文探讨了在 React 生态系统中实现细粒度响应式更新的方法，通过 MUI X Data Grid 的案例展示了一种简洁的解决方案，并提供了代码示例和优化建议。

- 🚀 **响应式更新的挑战**：React 中全局状态变更导致所有组件重新渲染，性能开销大。  
- 🛠️ **解决方案**：提出基于`Store`类和`useSelector`钩子的细粒度更新方案，仅更新相关组件（代码少于 35 行）。  
- 🔍 **核心机制**：通过订阅模式和选择器（selector）精准控制组件渲染，避免不必要的更新。  
- ⚡ **性能优化**：结合`useSyncExternalStore`解决异步渲染问题，并推荐使用`reselect`实现记忆化派生状态。  
- 📦 **工具化**：提供`store-x-selector`封装包，集成性能优化和类型支持，简化开发。  
- 💡 **最佳实践**：建议合理使用记忆化（memoization），避免过度或不足优化。  
- 🌟 **扩展性**：未来可探索事件驱动的响应式模型（类似 SolidJS 信号机制）。

---

### [编程文摘：电子邮件通讯](https://programmingdigest.net/?utm_source=web-archive&utm_campaign=react)

**原文标题**: [Programming Digest: Email Newsletter](https://programmingdigest.net/?utm_source=web-archive&utm_campaign=react)

《Programming Digest》是一份专为软件工程师精心挑选的每周通讯，提供精选文章和简短摘要，帮助读者节省时间并每周学习新知识。  

- 📧 每周一封电子邮件，已吸引超过 18,196 名软件工程师订阅  
- 📖 精选文章搭配简短摘要，节省寻找有价值内容的时间  
- 🎯 每周学习新知识，满足持续学习的需求  
- 💬 读者反馈积极，认为内容实用且贴合兴趣（如 API 设计、效率提升等）  
- 🌍 订阅者遍布全球，深受软件工程师信赖  
- ©️ 由 Bonobo Press 发行，注重隐私与内容质量

---

### [科技领导力：电子邮件通讯](https://leadershipintech.com/?utm_source=web-archive&utm_campaign=react)

**原文标题**: [Leadership in Tech: Email Newsletter](https://leadershipintech.com/?utm_source=web-archive&utm_campaign=react)

《Leadership in Tech》是一份为技术领导者精心打造的每周通讯，旨在帮助 CTO、工程经理和高级工程师提升领导力。  

- 📰 **精选内容**：每周推送精选文章与简短摘要，节省读者寻找优质内容的时间。  
- 🎯 **目标读者**：面向 26,787+ 技术领导者，提供高效的知识获取渠道。  
- 🌟 **读者反馈**：用户称赞其领导力建设文章（如授权技巧、架构讨论、沟通方法）独具价值且切中需求。  
- 🏢 **品牌背书**：受到科技行业领袖广泛阅读，由 Bonobo Press 发行（2013-2025）。  
- 🔒 **附加信息**：涵盖隐私政策、广告合作等模块，保持透明度。

---

### [C#文摘：电子邮件通讯](https://csharpdigest.net/?utm_source=web-archive&utm_campaign=react)

**原文标题**: [C# Digest: Email Newsletter](https://csharpdigest.net/?utm_source=web-archive&utm_campaign=react)

C# Digest 是一份为.NET 开发者精心策划的每周通讯，旨在为开发者提供有价值的内容，节省时间并每周学习新知识。

- 📰 每周精选文章，附简短摘要，为.NET 开发者提供有价值的内容  
- ✉️ 超过19,857名C#工程师订阅，每周一封邮件  
- ⏱️ 节省时间，避免自行筛选低质量内容  
- 🎓 每周学习新知识，持续提升技能  
- 💬 读者反馈积极，部分内容已应用于实际工作  
- 🔍 涵盖多种主题，如标准功能标志、LINQ、DiagnosticListener 等  
- 👍 特别推荐《The Operation Result Pattern》一文，受到读者及同事好评  
- 🌍 读者遍布全球，来自各大知名公司  
- ©️ 由 Bonobo Press 发布，2013-2025

---

### [让开发者与时俱进——Bonobo Press](https://bonobopress.com/)

**原文标题**: [Keeping developers up to date â Bonobo Press](https://bonobopress.com/)

Bonobo Press 是一家自 2013 年起为软件开发者和技术专业人士提供新闻资讯的出版商，拥有超过 88,000 名订阅者，提供简洁高效的每周通讯，并为企业提供广告服务以触达目标技术受众。

- 📰 自 2013 年起为 88,000+ 软件开发者和技术专业人士提供最新资讯  
- ✉️ 每周发布精选通讯，涵盖开发者、工程经理、技术主管等多类读者  
- ⏱️ 以简洁高效的内容帮助技术人员节省时间  
- 📢 提供广告服务，精准触达工程师、团队领导及技术决策者  
- 📄 可查看媒体资料包并开始合作  
- 📧 欢迎通过联系页面进行咨询、建议或广告合作

---

### [往期通讯：第 1 页](https://reactdigest.net/newsletters)

**原文标题**: [Past Newsletters: Page 1](https://reactdigest.net/newsletters)

overview summary  
本期汇总了 React Digest 自 2025 年 2 月至 6 月的多期内容，涵盖实时手势识别、数据获取优化、自定义 Hook、状态管理、性能优化等 React 生态前沿话题，并包含 Dan Abramov 等专家的深度分享。

- 🎥 **实时手势识别**：探讨视频会议中的实时手势识别技术，并对比 React 中的数据获取方法（2025 年 6 月 22 日）。  
- ⚡ **细粒度响应式**：通过最小化 Store 类实现响应式，避免 Next.js 中的 Props 透传问题（2025 年 6 月 15 日）。  
- 🧩 **框架复杂性**：分析现代 React 框架的痛点，提供 API 消费指南及 Progressive JSON 等创新技术（2025 年 6 月 8 日）。  
- 🚀 **高效数据获取**：Dan Abramov 分享单次导航数据加载策略，及 TanStack Router 的路由解决方案（2025 年 6 月 1 日）。  
- 🎯 **焦点管理**：利用`flushSync`掌握 React 焦点控制，探讨并发渲染与 AI 辅助开发（2025 年 5 月 25 日）。  
- 🔐 **认证与路由**：结合 React Router 实现 OpenAuth，揭秘 Context 效率真相（2025 年 5 月 18 日）。  
- 🏗️ **数据架构**：复杂应用中的数据获取架构设计，含 Dan Abramov 对 HTML 的新思考（2025 年 5 月 11 日）。  
- ✨ **视图过渡**：React 新特性 View Transitions 与 Activity 组件提升 UI 动画流畅度（2025 年 5 月 4 日）。  
- 🤯 **不可能组件**：Dan Abramov 探讨非常规组件，React Query 状态简化实践（2025 年 4 月 27 日）。  
- 📡 **服务端渲染**：JSX 传输优化、全栈 AI 聊天应用构建及 React 架构演进（2025 年 4 月 20 日）。  
- 🛠️ **高级技巧**：React Query 机制、协调算法解析及动态表单挑战（2025 年 4 月 13 日）。  
- ⚖️ **架构权衡**：Zustand/Immer 实践、无库表单方案与自适应流媒体（2025 年 4 月 6 日）。  
- 🔑 **Next.js 授权**：Robin 的授权方案与 React View Transition API 解析（2025 年 3 月 30 日）。  
- 📊 **SSR 深度**：React 服务端渲染、TanStack 实时数据更新及 URL 状态管理（2025 年 3 月 23 日）。  
- ⚡ **性能优化**：Next.js 性能调优、Toast 通知实现及替代`React.memo`方案（2025 年 3 月 16 日）。  
- 📶 **信号挑战**：React 中信号技术的应用难点与状态转换分析（2025 年 3 月 9 日）。  
- λ **函数式编程**：React 19 缓存 API 优化数据获取，CRA 迁移至 Vite 指南（2025 年 3 月 2 日）。  
- 🌅 **CRA 退役**：Create React App 弃用，转向现代框架集成与自定义 Hook（2025 年 2 月 23 日）。  
- ✍️ **渲染器重构**：ProseMirror 渲染器 React 重制经验与 React Router 原理（2025 年 2 月 16 日）。  
- 🧩 **设计模式**：动态样式加载、Context 库构建及表单数据持久化（2025 年 2 月 9 日）。

---

### [隐私](https://reactdigest.net/privacy)

**原文标题**: [Privacy](https://reactdigest.net/privacy)

隐私政策概述，详细说明了信息收集、使用、保护及用户权利的相关规定。

- 🔒 隐私至关重要，因此制定了明确的政策，阐述如何收集、使用、沟通和披露个人信息。  
- 🎯 在收集个人信息前或当时，会明确说明收集目的。  
- 📝 仅出于指定目的或相关兼容目的收集和使用个人信息，除非获得同意或法律要求。  
- ⏳ 仅在必要期限内保留个人信息以实现收集目的。  
- ⚖️ 通过合法公正手段收集信息，并在适当情况下获得个人知情或同意。  
- ✔️ 确保个人数据与使用目的相关，且准确、完整、最新。  
- 🛡️ 采取合理安全措施保护个人信息，防止丢失、盗窃或未经授权的访问、披露等。  
- 📢 向客户公开有关个人信息管理的政策和实践。  
- 📧 仅收集电子邮件地址以发送每周通讯，不用于其他目的。  
- 🚸 遵守 COPPA，不故意收集或存储 13 岁以下儿童的信息，网站也不针对或吸引此类儿童。  
- 📬 用户可根据《数据保护法 1998》（英国）要求获取或删除存储的个人信息，联系邮箱：[email protected]。  
- 🚫 坚决反对垃圾邮件，提供随时退订选项。  
- ©️ 版权归 Bonobo Press 所有（2013-2025）。

---

### [媒体资料包——Bonobo 出版社](https://bonobopress.com/media-kit/)

**原文标题**: [Media Kit â Bonobo Press](https://bonobopress.com/media-kit/)

Bonobo Press 为技术从业者提供精心策划的每周通讯，涵盖软件开发、工程管理等领域，帮助广告商精准触达目标受众并提升转化率。  

- 📧 **Newsletters 与统计数据**：提供详细的通讯订阅数据、打开率和点击率，确保广告效果可衡量。  
- 🎯 **目标受众**：覆盖软件工程师、技术领导者、CTO 等不同角色，订阅者多来自欧美，任职于 Google、Amazon 等公司。  
- 💰 **广告费率**：不同通讯的赞助价格、预计点击量及 CPC 范围明确，如《Leadership in Tech》单期 $1,940，CPC $3.51-$5.83。  
- 📝 **广告格式**：纯文本内嵌广告，需提供链接、标题（<100 字符）和描述（<400 字符），4 天前提交。  
- 🔄 **订购流程**：提前数周预约档期，支付锁定日期，优化广告文案后投放并提供效果报告。  
- 🤝 **合作伙伴案例**：包括 Okta、GitLab、MongoDB 等知名企业，常重复预订赞助。  
- 🌍 **订阅者分布**：欧洲和美国占主要比例，受众涵盖不同经验层次和行业规模的公司。  
- 📅 **时间敏感提示**：广告档期紧张，建议尽早联系以确保空位。  
- ✉️ **联系方式**：欢迎咨询合作，提升产品曝光与转化。

---

