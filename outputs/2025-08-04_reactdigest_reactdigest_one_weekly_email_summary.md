### [React 文摘：电子邮件通讯](https://reactdigest.net/)

**原文标题**: [React Digest: Email Newsletter](https://reactdigest.net/)

《React Digest》是一份为 React 开发者精心策划的周报，汇集了精选文章和简短摘要，帮助开发者节省时间并每周学习新知识。  

- 📰 每周一封邮件，服务 22,334 多名前端工程师  
- 🖊️ 精选文章配简短摘要，节省筛选时间  
- 📚 每周学习新知识，紧跟技术发展  
- 👍 读者好评：内容实用、更新及时（如 React 并发模式专题）  
- 🌍 全球前端工程师信赖的资讯来源  
- ©️ 由 Bonobo Press 发行（2013-2025）

---

### [无用的 useCallback | TkDodo 的博客](https://tkdodo.eu/blog/the-useless-use-callback)

**原文标题**: [The Useless useCallback | TkDodo's blog](https://tkdodo.eu/blog/the-useless-use-callback)

overview summary  
本文探讨了在 React 中过度使用`useCallback`和`useMemo`的问题，指出许多情况下这些优化是无效甚至有害的，并提出了替代方案如`useRef`和未来的`useEffectEvent`。

- 🏔️ **记忆化的艰难战斗**  
  使用`useCallback`和`useMemo`的主要目的是性能优化和避免不必要的重新渲染，但实际效果往往有限。

- 🚫 **无用的 useCallback**  
  当函数或值未传递给记忆化组件时，使用`useCallback`或`useMemo`是多余的，例如内置 React 组件（如`button`）不关心引用稳定性。

- ⚡ **性能开销**  
  不必要的记忆化会带来内部缓存和依赖比较的开销，尽管这种开销通常不是主要问题。

- 🔄 **依赖项问题**  
  将非原始类型的 props 用作内部依赖项（如`useEffect`的依赖数组）容易因引用不稳定而失效，导致记忆化失效。

- 🧩 **实际案例中的问题**  
  以 Sentry 代码库中的`useHotkeys`为例，展示了多层记忆化因底层数据未记忆化而完全失效的情况。

- 🛠️ **替代方案**  
  推荐使用`useRef`模式（如“最新引用模式”）或未来的`useEffectEvent`来避免不必要的记忆化，同时保持引用稳定性。

- 🚀 **未来解决方案**  
  React 即将引入的`useEffectEvent`将提供更优雅的方式处理副作用中的最新值访问，无需手动记忆化。  

- 💡 **总结建议**  
  避免过度依赖记忆化，优先考虑代码可维护性，并期待编译器或 React 原生方案（如`useEffectEvent`）解决引用稳定性问题。

---

### [一丝不苟](https://www.meticulous.ai/?utm_source=react_digest)

**原文标题**: [Meticulous](https://www.meticulous.ai/?utm_source=react_digest)

Meticulous AI 提供了一种无需编写或维护测试的自动化测试解决方案，通过记录用户交互并生成动态测试套件，覆盖所有边缘案例，提升开发效率和代码质量。

- 🚀 **自动化测试生成** - Meticulous AI 通过记录开发中的用户交互，自动生成覆盖所有代码分支和用户流程的测试套件。  
- 🔄 **持续演进** - 测试套件随应用更新自动调整，无需手动维护，确保测试始终与最新代码同步。  
- ⚡ **高效集成** - 支持与现有测试套件结合或完全替代，提供无副作用测试和快速反馈（120 秒内完成数千次测试）。  
- 🛡️ **零误报与稳定性** - 通过模拟后端响应和确定性调度引擎，彻底消除测试中的随机失败（Flakes）。  
- 🌟 **客户认可** - 被 Dropbox、Notion 等 100 多家组织信任，显著减少回归问题并提升开发信心。  
- 📦 **快速上手** - 提供多种前端框架（如 React、Vue、Angular）的脚本集成指南，几分钟即可开始使用。  
- 🔗 **灵活部署** - 支持本地开发、预发布及生产环境会话记录，按需扩展测试覆盖范围。

---

### [阿米莉亚·沃滕伯格](https://2019.wattenberger.com/blog/react-and-d3)

**原文标题**: [Amelia Wattenberger](https://2019.wattenberger.com/blog/react-and-d3)

该内容提示需要启用 JavaScript 才能运行应用程序。

- 🛠️ 需要启用 JavaScript 以运行此应用

---

### [如何在 React Router 中处理延迟数据 - sergiodxa](https://sergiodxa.com/tutorials/handle-deferred-data-in-react-router)

**原文标题**: [How to Handle deferred data in React Router by sergiodxa](https://sergiodxa.com/tutorials/handle-deferred-data-in-react-router)

React Router v7 允许在加载器中返回未解决的 Promise，从而实现在组件中直接处理加载状态，提升用户体验。React 19 进一步简化了异步数据渲染的流程。

- 🚀 **延迟数据处理**：React Router v7 允许从加载器返回 Promise，无需在加载器中等待，直接在组件中处理加载状态。  
- 🔄 **与 Remix 的对比**：类似 Remix v2 的 `defer` 和 `useDeferredValue`，但 React Router v7 无需额外工具，直接返回 Promise 即可。  
- ⏳ **使用 Await 组件**：通过 `Suspense` 和 `Await` 组件结合，优雅地处理异步数据加载和加载状态。  
- ⚡ **React 19 的 use 钩子**：React 19 引入 `use` 钩子，可直接在组件中消费 Promise，但需要额外封装组件。  
- ✨ **Promise 作为可渲染节点**：React 19 允许直接将 Promise 作为渲染节点，无需 `Await` 或额外组件，简化代码。  
- 📚 **相关教程**：包括复用路由模块、拆分路由配置和动态加载样式表等 React Router v7 相关教程。

---

### [Parcel 如何打包 React 服务器组件](https://devongovett.me/blog/parcel-rsc.html)

**原文标题**: [How Parcel bundles React Server Components](https://devongovett.me/blog/parcel-rsc.html)

Parcel v2.14.0 新增了对 React Server Components (RSCs) 的支持，本文深入探讨了 RSCs 如何与打包工具集成、指令如 "use client" 的内部工作原理、代码分割机制及其优化等内容。

- 🚀 **Parcel 支持 RSCs**  
  Parcel v2.14.0 新增对 React Server Components 的支持，通过统一的模块图实现跨环境代码分割。

- 📦 **打包工具的作用**  
  打包工具将多个 JavaScript 模块合并为更少的文件，优化加载性能，减少 HTTP 请求数量，并提升压缩效率。

- 🔄 **代码分割的重要性**  
  代码分割在初始加载性能和 HTTP 缓存之间取得平衡，避免下载未使用的代码，同时利用浏览器缓存共享公共依赖。

- 🌐 **动态加载的挑战**  
  单页应用 (SPA) 中动态加载模块可能导致网络瀑布问题，嵌套路由和异步数据加载会进一步加剧性能问题。

- ⚡ **React Server Components 的解决方案**  
  RSCs 通过服务器端渲染和预加载优化加载顺序，减少网络瀑布，提升用户体验。

- 🔧 **环境与指令**  
  Parcel 使用环境标识模块运行位置（服务器、浏览器等），"use client" 指令将模块环境切换为 react-client 并生成客户端引用。

- 🧩 **客户端组件的打包**  
  多个客户端组件会被打包到同一个 HTTP 请求中，减少请求数量，优化加载性能。

- ⏳ **条件渲染与代码分割**  
  动态 import() 支持条件渲染的代码分割，RSCs 自动预加载相关资源，避免网络瀑布。

- 🎨 **CSS 与其他资源的处理**  
  Parcel 自动注入 <link> 元素并利用 React 的优先级机制优化 CSS 加载，避免 FOUC 并支持资源捆绑。

- 🔮 **未来展望**  
  后续将探讨 Server Actions 和渐进式加载的导入映射等更多内容。

---

### [从零开始编写 React Hooks | 趣味编程](https://playfulprogramming.com/posts/react-write-hooks-from-scratch)

**原文标题**: [
	Let's Write React Hooks From Scratch | Playful Programming
](https://playfulprogramming.com/posts/react-write-hooks-from-scratch)

概述：本文深入探讨了 React Hooks 的内部实现机制，从数组存储到链表结构的演变，揭示了 Hooks 如何通过虚拟 DOM（VDOM）保持状态，并解释了为何必须遵循 Hooks 的调用顺序规则。

- 🧩 React Hooks 的持久化依赖于虚拟 DOM（VDOM），而非普通 JavaScript 函数的执行上下文。  
- 📚 早期 Hooks 状态通过数组存储，索引顺序决定状态对应关系，因此不能条件调用。  
- 🔄 实际 React 源码中，Hooks 以链表形式存储，每个节点包含状态和指向下一个 Hook 的引用。  
- 🏗️ 模拟实现中，通过全局变量`currentComponent`和`workInProgressHook`追踪当前组件和处理的 Hook 节点。  
- ⛓️ 链表结构解决了动态 Hook 调用的扩展性问题，确保状态与组件渲染周期绑定。  
- 📖 作者推荐其免费书籍《The Framework Field Guide》，涵盖 React、Angular 和 Vue 的深度学习。  
- ✉️ 文末附有订阅新闻和社区链接（GitHub、Discord），提供更多相关内容更新。

---

### [获取失败](https://css-tricks.com/making-a-masonry-layout-that-works-today/)

**原文标题**: [Failed to retrieve](https://css-tricks.com/making-a-masonry-layout-that-works-today/)

无法总结：获取内容失败，状态码 415。

---

### [HTML 爱好者](https://www.htmlhobbyist.com/)

**原文标题**: [The HTML Hobbyist](https://www.htmlhobbyist.com/)

万维网曾是一个开放、共享的信息空间，如今虽被商业化侵蚀，但创建个人网站依然简单且低成本。以下是关键点：

- 🌐 万维网初期是信息自由共享的开放社区，个人和机构均可轻松发布内容。  
- 💻 如今建站门槛极低：域名年费低于 20 美元，主机月费仅 2 美元，成本远低于一款游戏。  
- 📝 基础建站仅需 HTML 知识、电脑和上传文件至服务器的能力。  
- 🚀 快速建站步骤：注册主机（如 Dreamhost）、选择共享计划、绑定域名、上传 HTML 文件。  
- 🛠️ 手动编码示例：创建`index.html`，添加基础结构（标题、段落、图片链接），通过 FTP 上传至主机。  
- 🔄 现代网络问题：广告泛滥、算法控制、用户体验差，背离了早期开放精神。  
- ✨ 独立网络运动（如 indieweb）复兴 90 年代风格，倡导简单、去中心化的个人网站。  
- 🏆 HTML 爱好者宣言：鼓励纯手工编码，仅必要使用 CSS/JavaScript，拒绝模板化。  
- 🔗 可通过“网页圈”（Webrings）连接志同道合的独立站点，重建社区感。  

（注：Emoji 已按要求添加，内容保留了技术细节与批判性观点，并突出核心流程与价值观。）

---

### [现代 CSS 是时候终结单页应用了——乔诺·奥尔德森](https://www.jonoalderson.com/conjecture/its-time-for-modern-css-to-kill-the-spa/)

**原文标题**: [It's time for modern CSS to kill the SPA - Jono Alderson](https://www.jonoalderson.com/conjecture/its-time-for-modern-css-to-kill-the-spa/)

现代 CSS 技术（如视图过渡 API 和推测规则）已使单页应用（SPA）的核心优势过时，但开发者仍过度依赖 SPA 框架，导致性能下降和复杂性问题。

- 🚀 **SPA 的虚假承诺**：SPA 曾因提供流畅导航体验而流行，但实际常导致加载延迟、滚动恢复问题和高 JS 开销。  
- 🛠️ **平台成熟解决方案**：现代浏览器原生支持跨文档视图过渡和推测规则，无需 JS 即可实现平滑动画和预加载。  
- ⚡ **性能对比**：传统 SPA（如 Next.js）需数 MBJS 捆绑，而现代多页应用（MPA）结合原生特性可实现更快加载和更优 SEO。  
- 📉 **SPA 的滥用**：多数内容型网站（如电商、博客）无需 SPA 的复杂状态管理，却因“类应用体验”要求被迫采用，牺牲性能。  
- 🌐 **回归 Web 本质**：倡导使用语义 HTML、CSS 动画和原生浏览器功能，减少 JS 依赖，提升可维护性和可访问性。  
- ⚠️ **注意事项**：推测规则需谨慎使用——若页面本身臃肿，预加载反而加剧资源浪费。  
- 🔮 **未来方向**：浏览器如 Chrome/Edge 已支持视图过渡 API，但需等待 Firefox/Safari 全面兼容以实现跨平台统一体验。  

核心观点：**大多数网站应回归 MPA 架构，利用现代 CSS/浏览器能力，而非盲目追求 SPA**。

---

### [庆祝 MDN 二十周年 | MDN 博客](https://developer.mozilla.org/en-US/blog/mdn-turns-20/)

**原文标题**: [Celebrating 20 years of MDN | MDN Blog](https://developer.mozilla.org/en-US/blog/mdn-turns-20/)

MDN 庆祝成立 20 周年，回顾其作为开发者社区驱动的资源库的成长历程，并感谢全球贡献者的支持。

- 🎂 MDN 本月迎来 20 周年纪念，成为开发者构建开放网络生态的重要资源。  
- 🌐 最初作为社区维基，MDN 伴随网络平台成熟，现拥有近 1.4 万页文档和 3.3 万篇本地化文章。  
- 🏆 收录约 1.8 万项功能的兼容性数据，被公认为最全面、可信的开发者文档库。  
- 👩‍💻 20 年来服务不同背景的开发者，推动数十亿人使用的开放网络生态。  
- 🍰 遵循浏览器厂商传统，web.dev 团队赠送蛋糕庆祝，象征行业协作精神。  
- 💌 特别感谢超 10 万 GitHub 贡献者，强调社区是 MDN 持续发展的核心动力。  
- 📢 邀请用户通过社交平台分享与 MDN 的故事，并鼓励参与文档协作共创未来。  
- 📚 相关阅读推荐：MDN 过去 10 年、15 年的里程碑文章及技术类相邻内容。

---

### [缩小化并不那么重要 | Go Make Things](https://gomakethings.com/minification-doesnt-matter-much/)

**原文标题**: [Minification doesnt matter much | Go Make Things](https://gomakethings.com/minification-doesnt-matter-much/)

2025 年 7 月 25 日  
作者通过测试发现代码压缩（minification）在现代开发中的实际收益微乎其微，尤其是结合 gzip 后，节省的空间（0.8kb）与可读性牺牲不成正比，认为性能差异可忽略。

- � 观点转变：从坚持压缩代码转为认为不值得为微小节省牺牲可读性  
- 📊 测试数据：未压缩 58.2kb → 压缩后 43kb；gzip 后差异仅 0.8kb（8.2kb vs 7.4kb）  
- 🔍 可读性优先：压缩代码难调试，节省空间对 HTTP 往返影响极小  
- 💌 推广内容：推荐订阅《每日开发者技巧》邮件或加入会员获取更多前端优化建议  
- 🤖 互动提示：页面包含邮件订阅表单及 RSS 订阅选项

---

### [永远不要自己编写日期解析库—zachleat.com](https://www.zachleat.com/web/adventures-in-date-parsing/)

**原文标题**: [Never write your own Date Parsing Library—zachleat.com](https://www.zachleat.com/web/adventures-in-date-parsing/)

概述：作者分享了开发自定义日期解析库的经历，探讨了现有库的局限性，并介绍了新库的设计理念和优势。

- 🚫 作者强调不要自行编写日期解析库，但自己却开发了一个名为 `@11ty/parse-date-strings` 的新库。  
- 📅 最初使用 `luxon` 作为 Eleventy 的日期解析库，但由于其体积过大（4.7 MB）且不支持 tree-shaking，开始寻找替代方案。  
- 🔍 对比了多个日期库（`luxon`、`moment`、`dayjs`、`date-fns`），发现 `dayjs` 虽然体积小但不准确，无法通过大部分测试用例。  
- 🛠️ 新库基于 RFC 9557 标准，专注于严格的日期解析，确保与未来的 Temporal API 兼容。  
- 📉 新库显著减少了体积（仅 2.3 kB），使 `@11ty/client` 的包大小减少了约 230 kB，`node_modules` 安装体积从 21.3 MB 降至 16.6 MB。  
- ⚠️ 新库与 `luxon` 存在一些解析行为的差异，但这是为了未来兼容性而做的必要调整。  
- 💡 作者还推荐了其他日期库和 Temporal polyfill（如 `@js-temporal/polyfill`、`temporal-polyfill`），供开发者参考。  
- 🔄 讨论了是否应放弃双模式发布（ESM/CJS），但最终决定保留对 CJS 的支持以兼容旧版本。

---

### [过去十年中众多、众多、众多的 JavaScript 运行时 • Buttondown](https://buttondown.com/whatever_jamie/archive/the-many-many-many-javascript-runtimes-of-the-last-decade/)

**原文标题**: [The many, many, many JavaScript runtimes of the last decade • Buttondown](https://buttondown.com/whatever_jamie/archive/the-many-many-many-javascript-runtimes-of-the-last-decade/)

过去十年中，JavaScript 运行时和引擎的多样化发展使其能够适应各种场景，从云端到边缘计算，再到微控制器和智能设备。以下是关键点的总结：

- 🌐 **JavaScript 运行时的多样化**：过去十年见证了 JavaScript 运行时的爆炸式增长，使其能够在云端、边缘计算、智能电视、移动设备和微控制器等多种环境中运行。
- ⚡ **边缘计算的兴起**：从 AWS Lambda 到 Cloudflare Workers，JavaScript 在边缘计算中的应用迅速扩展，推动了低延迟运行时的需求。
- 📱 **移动设备与微控制器**：JavaScript 引擎如 JerryScript 和 Duktape 使 JavaScript 能够在资源有限的微控制器上运行，推动了物联网的发展。
- 🔄 **多语言引擎**：如 Graal.js 和 Rhino 等引擎支持 JavaScript 与其他语言（如 Java、C#、Python 等）的无缝互操作。
- 🖥️ **原生应用开发**：通过框架如 React Native、Electron 和 NativeScript，JavaScript 在移动和桌面应用开发中占据了重要地位。
- 📺 **智能电视平台**：JavaScript 在智能电视平台上的应用，如 HbbTV 和 webOS，展示了其在多样化设备中的广泛适用性。
- 🚀 **竞争与创新**：不同运行时和引擎之间的竞争推动了性能优化和新功能的开发，如 Hermes 和 QuickJS。
- 🔮 **未来展望**：JavaScript 继续在各种设备和应用场景中扩展，展示了其作为多用途语言的强大生态系统和适应性。

这篇文章虽然未能涵盖所有内容，但展示了 JavaScript 在多个领域中的广泛应用和持续创新。

---

### [介绍 Zustand（状态管理）—— Frontend Masters 博客](https://frontendmasters.com/blog/introducing-zustand/)

**原文标题**: [Introducing Zustand (State Management) – Frontend Masters Blog](https://frontendmasters.com/blog/introducing-zustand/)

Zustand 是一个简洁但功能强大的状态管理库，适用于 React 应用。它通过减少样板代码和优化渲染性能，提供了一种高效的状态管理方案。

- 🚀 **Zustand 简介**  
  Zustand 是一个已有五年历史的流行状态管理库，以其简洁和高效著称。

- 🛠️ **快速上手**  
  通过一个简单的任务管理应用示例，展示了 Zustand 的基本用法，并与 React Context 进行了对比。

- 🔄 **状态更新**  
  使用 `set` 函数可以轻松更新状态，支持部分更新和完全覆盖。

- 📖 **正确读取状态**  
  推荐使用选择器函数（selector）来读取状态，以避免不必要的重新渲染。

- ⚡ **性能优化**  
  Zustand 通过选择器函数和 `useShallow` 钩子，显著减少了不必要的组件重新渲染。

- 🌐 **异步支持**  
  Zustand 天然支持异步操作，可以在异步函数中调用 `set` 来更新状态。

- 🔍 **读取状态**  
  提供了多种方式读取状态，包括在组件内使用钩子，以及在非组件环境中使用 `getState()`。

- 📚 **更多功能**  
  Zustand 还支持手动订阅、与 Immer 集成等高级功能，适合复杂应用场景。

- 💡 **总结**  
  Zustand 是一个简单、有趣且高效的状态管理解决方案，适合各种规模的 React 应用。

---

### [编程文摘：电子邮件通讯](https://programmingdigest.net/?utm_source=web-archive&utm_campaign=react)

**原文标题**: [Programming Digest: Email Newsletter](https://programmingdigest.net/?utm_source=web-archive&utm_campaign=react)

《Programming Digest》是一份专为软件工程师精心挑选的每周通讯，旨在为读者节省时间并提供有价值的内容。  

- 📧 每周一封邮件，汇集精选文章与简短摘要  
- ⏳ 节省寻找优质内容的时间  
- 🎯 19,441+ 软件工程师订阅  
- 📖 读者反馈积极，认为内容实用且启发思考  
- 🌍 订阅者遍布全球，来自多家知名科技公司  
- ©️ 由 Bonobo Press 发行，涵盖隐私与广告政策

---

### [科技领导力：电子邮件通讯](https://leadershipintech.com/?utm_source=web-archive&utm_campaign=react)

**原文标题**: [Leadership in Tech: Email Newsletter](https://leadershipintech.com/?utm_source=web-archive&utm_campaign=react)

概述总结  
一份精心策划的每周通讯，帮助技术领导者提升领导力，内容涵盖精选文章、实用建议和行业洞察。  

- 📰 面向 CTO、工程经理和高级工程师的每周通讯，旨在提升领导力  
- ✉️ 超过 26,826 名工程领导者订阅，每周一封精选邮件  
- 🕒 节省时间，直接获取有价值的内容  
- 📚 每周学习新知识，涵盖架构讨论、会议规划、沟通技巧等主题  
- ❤️ 读者反馈：赞赏领导力建设文章，尤其是关于授权和沟通的内容  
- 🌍 来自全球科技领导者的信赖与阅读  
- ©️ 由 Bonobo Press 发布，2013-2025 年

---

### [C#文摘：电子邮件通讯](https://csharpdigest.net/?utm_source=web-archive&utm_campaign=react)

**原文标题**: [C# Digest: Email Newsletter](https://csharpdigest.net/?utm_source=web-archive&utm_campaign=react)

C# Digest 是一份专为.NET 开发者精心策划的每周通讯，旨在为开发者提供精选内容、节省时间并每周学习新知识。

- 📰 每周精选文章，附带简短摘要，帮助开发者高效获取有价值的内容  
- ⏳ 节省开发者寻找优质内容的时间  
- 📚 每周学习新知识，持续提升技能  
- 👥 拥有超过19,867名C#工程师订阅  
- 💬 读者反馈积极，内容包括实用技巧、新功能探索（如标准功能标志、LINQ）和实用模式（如操作结果模式）  
- 🌍 受到全球.NET 工程师的阅读和推荐  
- © 2013-2025 Bonobo Press 出品，涵盖新闻通讯、隐私和广告信息

---

### [让开发者与时俱进——Bonobo 出版社](https://bonobopress.com/)

**原文标题**: [Keeping developers up to date â Bonobo Press](https://bonobopress.com/)

Bonobo Press 是一家自 2013 年起为软件开发者和技术专业人士提供新闻资讯的出版商，拥有超过 88,000 名订阅者，提供简洁高效的每周通讯，并为企业提供广告服务以触达目标技术受众。

- 📰 自 2013 年起为 88,000+ 开发者、IT 专业人士提供最新技术资讯  
- ✉️ 每周发布精选通讯，涵盖开发者、工程经理、技术主管及 CTO 等受众  
- ⏱️ 以简洁、省时的内容获得技术人员喜爱  
- 📢 提供广告服务，精准触达软件工程师、团队领导及 IT 决策者  
- 📬 可通过媒体资料包了解广告合作详情  
- 📧 欢迎通过联系页面进行咨询、建议或广告合作

---

### [往期通讯：第 1 页](https://reactdigest.net/newsletters)

**原文标题**: [Past Newsletters: Page 1](https://reactdigest.net/newsletters)

React Digest 是一份专注于 React 技术动态的新闻简报，涵盖最佳实践、状态管理、性能优化、数据获取、模块联邦、手势识别等前沿话题，并提供丰富的实战案例和框架深度解析。

- 🎯 2025 年 8 月 3 日：探讨 useCallback 最佳实践、React Router 延迟数据处理及 Parcel 打包 React Server Components  
- � 2025 年 7 月 27 日：Zustand 状态管理深度解析、React 拖放看板构建及 React Router Action Routes  
- 🧩 2025 年 7 月 20 日：React 模块联邦技术探索、Astro 高效架构与 React 并发 API 实战  
- 🕰️ 2025 年 7 月 13 日：React 架构演进史、PDF.js 集成及 Server Components 创新测试方法  
- 🧱 2025 年 7 月 6 日：React 组件模块化哲学、AI 代理构建与数据获取核心技术  
- 🔄 2025 年 6 月 29 日：重渲染性能优化、Zero-UI 加速更新及 Server Components 在 Expo 的应用  
- ✋ 2025 年 6 月 22 日：视频会议实时手势识别、React 数据获取方案对比与自定义 useState 实现  
- ⚡ 2025 年 6 月 15 日：细粒度响应式 Store 类、Next.js 异步存储避坑及 URL 状态管理技巧  
- � 2025 年 6 月 8 日：现代 React 框架复杂性分析、Progressive JSON 创新及 Remix 未来展望  
- 🚀 2025 年 6 月 1 日：Dan Abramov 谈高效数据获取、TanStack 路由方案与 React 错误边界实践  
- 🎯 2025 年 5 月 25 日：flushSync 焦点控制、并发渲染实战与 AI 辅助 React 开发  
- 🔐 2025 年 5 月 18 日：React Router OpenAuth 集成、上下文效率真相与 Server Components 静态生成  
- 🏗️ 2025 年 5 月 11 日：复杂应用数据获取架构、色彩方案切换与媒体查询自定义 Hook  
- 🧩 2025 年 5 月 4 日：View Transitions 动画优化、useEffect 执行顺序与 Promise 序列化  
- 🧱 2025 年 4 月 27 日：Dan Abramov 谈"不可能组件"、React Query 状态简化与编译器生产化  
- 📡 2025 年 4 月 20 日：服务端渲染进阶、全栈 AI 聊天应用构建与 React 架构演进  
- 🎯 2025 年 4 月 13 日：生产级 React 优化、Query 原理与动态表单挑战  
- ⚖️ 2025 年 4 月 6 日：架构权衡实践、Zustand+Immer 最佳方案与无库表单三技法  
- 🔐 2025 年 3 月 30 日：Next.js 权限控制、View Transition API 及国际化实战  
- 🧩 2025 年 3 月 23 日：SSR 深度解析、TanStack 实时数据与 URL 状态管理迁移

---

### [隐私](https://reactdigest.net/privacy)

**原文标题**: [Privacy](https://reactdigest.net/privacy)

隐私政策概述，强调保护用户个人信息的重要性，明确信息收集、使用及保护的原则，并提供用户操作指南。

- 🔒 隐私至关重要，制定政策以明确如何收集、使用及披露个人信息。  
- 🎯 收集个人信息前会明确目的，仅用于指定或兼容用途，需用户同意或法律要求。  
- ⏳ 仅在必要时保留个人信息，确保数据使用期限合理。  
- 📝 通过合法公平手段收集信息，并在适当时获得用户知情或同意。  
- ✔️ 确保个人数据准确、完整且及时更新，以满足使用目的。  
- 🛡️ 采取合理安全措施保护信息，防止丢失、盗窃或未经授权访问。  
- 📢 向用户公开个人信息管理政策及实践，保持透明度。  
- ✉️ 仅收集用户邮箱地址用于发送周刊，不用于其他目的。  
- 🚸 严格遵守 COPPA，不收集或存储 13 岁以下儿童信息。  
- 📬 用户可依据《数据保护法》申请获取或删除存储的个人信息，联系邮箱：[email protected]。  
- 🚫 坚决反对垃圾邮件，提供随时退订选项，尊重用户选择权。  
- ©️ 版权归属 Bonobo Press（2013-2025），涵盖新闻通讯、隐私及广告相关条款。

---

### [媒体资料包——Bonobo 出版社](https://bonobopress.com/media-kit/)

**原文标题**: [Media Kit â Bonobo Press](https://bonobopress.com/media-kit/)

Bonobo Press 致力于为程序员和技术人员提供最新趋势、工具和技术信息，通过精心策划的每周新闻简报覆盖软件开发、工程管理等领域，帮助广告商精准触达目标受众并提升转化率。

- 📧 **新闻简报高参与度**：订阅用户互动率超行业标准两倍，严格清理非活跃用户，优先保证读者质量。  
- 🎯 **四大核心简报**：  
  - **《Leadership in Tech》**：面向技术领导者（CTO、工程经理等），订阅量 26,385，打开率 57.95%，点击率 11.38%，赞助费$1,940/期。  
  - **《Programming Digest》**：面向全栈和后端开发者，订阅量 18,263，点击率 14.83%，赞助费$875/期。  
  - **《C# Digest》**：专注.NET和C#开发，订阅量19,724，点击率21.63%（行业最高），赞助费$1,220/期。  
  - **《React Digest》**：聚焦前端 React 开发，订阅量 23,279，赞助费$1,320/期。  
- 🌍 **受众分布**：欧洲（35%-48%）和美国（30%-35%）为主，覆盖谷歌、亚马逊等企业及各类规模公司。  
- 💰 **广告计费透明**：按点击成本（CPC）计价，范围$1.95-$5.83，具体因简报类型而异。  
- ✍️ **广告格式**：纯文本内嵌（含标题、描述和链接），需提前 4 天提交文案，提供优化建议。  
- 📅 **预订流程**：需提前数周锁定档期，付款后确认排期，支持效果数据分析。  
- 🤝 **合作案例**：Okta、GitLab、MongoDB 等知名品牌多次复投。  
- 📩 **联系方式**：通过官网提交需求，获取定制化推广方案。

---

