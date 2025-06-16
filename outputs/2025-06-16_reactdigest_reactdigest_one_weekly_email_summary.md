### [React 文摘：电子邮件通讯](https://reactdigest.net/)

**原文标题**: [React Digest: Email Newsletter](https://reactdigest.net/)

《React Digest》是一份专为 React 开发者精心策划的每周通讯，汇集精选文章与实用资源，帮助开发者高效学习与成长。  

- 📰 **精选内容**：每周为前端工程师推送一封邮件，包含精心挑选的文章和简短摘要。  
- 🕒 **节省时间**：省去筛选有价值内容的时间，直接获取高质量信息。  
- 📚 **持续学习**：每周学习新知识，紧跟 React 技术的最新动态。  
- 👥 **社区认可**：超过 22,728 名开发者订阅，读者反馈称赞其内容实用且更新及时。  
- 🌍 **广泛读者**：受到全球前端工程师的青睐，包括对 React 并发模式等深度内容的积极评价。  
- ©️ **版权信息**：由 Bonobo Press 发布，涵盖 2013 至 2025 年，提供隐私政策与广告合作信息。

---

### [响应式编程很简单](https://romgrk.com/posts/reactivity-is-easy/)

**原文标题**: [Reactivity is easy](https://romgrk.com/posts/reactivity-is-easy/)

本文探讨了在 React 生态中实现细粒度响应式状态管理的解决方案，通过 MUI X Data Grid 的案例展示了如何用不到 35 行代码解决组件无效重渲染问题，并提供了优化思路和工具包推荐。

- 🧠 **核心问题**：React 中 Context 更新导致所有订阅组件重渲染，即使数据未变化也会引发性能损耗。
- 💡 **解决方案**：自定义`Store`类 + `useSelector`钩子，通过选择器精准订阅状态片段，避免无关更新。
  - 示例中点击单元格时仅 2 个相关组件重渲染（原方案需渲染 50 个）。
- ⚙️ **实现要点**：
  - `Store`管理状态与订阅逻辑，`useSelector`连接组件与状态切片。
  - 无需`React.memo`即可实现精准更新（但复杂场景仍需配合使用）。
- 🚀 **进阶优化**：
  - 使用`use-sync-external-store`解决并发渲染撕裂问题。
  - 扩展`Store.set()`方法简化深层状态更新。
  - 结合`reselect`实现记忆化派生状态（如排序列表）。
- 📦 **工具推荐**：作者发布`store-x-selector`包，集成上述优化与类型支持。
- ⚠️ **注意事项**：记忆化适用于派生非原始值/计算密集型场景，需平衡使用频率。

---

### [OAuth 提供商改进](https://clerk.com/changelog/2025-06-13-oauth-improvements?utm_source=react-digest&utm_medium=newsletter&utm_campaign=oauth&utm_content=06-16-25&dub_id=hbkZAJwkCBOmtsSB)

**原文标题**: [OAuth Provider Improvements](https://clerk.com/changelog/2025-06-13-oauth-improvements?utm_source=react-digest&utm_medium=newsletter&utm_campaign=oauth&utm_content=06-16-25&dub_id=hbkZAJwkCBOmtsSB)

Clerk 宣布对其 OAuth 功能进行了重大扩展，新增多项特性以支持更广泛的应用场景，包括 MCP 服务的实现。

- 🔒 OAuth 令牌现在可以通过 Clerk 的 SDK 进行验证和即时撤销。
- 📜 支持授权服务器元数据，开箱即用。
- 🖥️ OAuth 授权流程新增了同意屏幕，确保用户在完成流程前明确了解所授予的权限。
- 🌐 改进了 CORS 处理，使得在浏览器中完成令牌交换的公共客户端实现成为可能。
- 🔄 支持 OAuth 客户端的动态客户端注册。
- 🤖 Clerk 的 OAuth 实现满足使用 Clerk 作为授权服务实现 MCP 服务的所有要求。

- 📚 Clerk 发布了详细的 OAuth 指南，解释了 OAuth 的三种不同用途：OAuth 范围访问、OAuth 单点登录（SSO）和 OAuth 用户管理。
- 🛠️ 提供了如何在 Clerk 应用中实现 OAuth 范围访问的指南，并展示了如何验证 OAuth 访问令牌的示例代码。
- 📱 OAuth 令牌验证目前支持大多数 SDK 生态系统，包括 Next.js、JavaScript 后端 SDK、Express SDK 等，其他 SDK 支持即将推出。
- ✅ 新增的 OAuth 同意屏幕显示请求应用的名称、徽标、请求的具体范围以及清晰的接受/拒绝选项，增强了安全性。
- 🔧 动态客户端注册允许通过 API 以编程方式创建 OAuth 客户端，而不仅限于通过仪表板手动创建。
- 🚀 Clerk 的 OAuth 改进为构建使用 Clerk 作为授权服务器的 MCP 服务铺平了道路，支持 AI 应用安全访问用户数据。
- 🔜 自定义范围的支持即将推出，团队正在积极开发中。

---

### [使用 Async Local Storage 避免 Next.js 路由处理程序中的属性透传 | Nico 的博客](https://www.nico.fyi/blog/async-local-storage-to-prevent-props-drilling)

**原文标题**: [Use Async Local Storage to prevent props drilling in Next.js Route handlers | Nico's Blog](https://www.nico.fyi/blog/async-local-storage-to-prevent-props-drilling)

文章介绍了如何在 Next.js 路由处理中使用 Async Local Storage 来避免属性传递（props drilling）的问题，类似于 React Context 但适用于 Node.js 函数。

- 🔄 使用 Async Local Storage 可以避免在多个函数间手动传递用户对象，简化代码结构  
- 🛠️ 创建 Async Local Storage 实例并封装 getUserContext 函数，确保调用时必须有 userContext.run() 块  
- 🔗 在 Next.js 路由处理中，通过 userContext.run() 包裹函数，使嵌套函数也能访问用户对象  
- 🚫 getUserContext 函数会检查上下文是否存在，缺失时抛出错误以防止未授权的调用  
- 📝 示例展示了 getProfile 和 getTransactions 函数如何通过上下文共享用户数据  
- ⚠️ 目前缺少编译时的 lint 检查来确保 userContext.run() 的使用，作者认为这是未来的改进点  
- 🔖 文章标签涉及开发、Next.js 和 TypeScript

---

### [搜索参数即状态 | TanStack 博客](https://tanstack.com/blog/search-params-are-state)

**原文标题**: [Search Params Are State | TanStack Blog](https://tanstack.com/blog/search-params-are-state)

概述总结  
文章讨论了搜索参数（search params）在应用开发中的重要性，指出传统处理方式存在的问题，并介绍了 TanStack Router 如何通过集成验证和类型安全来改进这一过程。

- 🔍 搜索参数常被视为次要状态，处理方式通常依赖字符串解析和松散的工具，导致代码冗长且脆弱。  
- ⚠️ URLSearchParams 仅支持字符串，无法处理嵌套 JSON、数组或类型转换，限制了复杂状态的管理。  
- 🛠️ 现有工具（如 Nuqs）虽改善了搜索参数的读取和写入体验，但未能解决跨组件或路由的协调问题。  
- 🔗 TanStack Router 通过在路由定义中集成搜索参数验证，提供了类型推断、自动完成和验证功能。  
- 🔄 支持事务性更新和响应式模型，确保组件仅在相关搜索参数变化时重新渲染。  
- 🌐 通过分层路由设计，父路由和子路由可以安全地共享和扩展搜索参数模式，避免冲突和不一致。  
- 🚫 强制类型安全防止了参数模式的碎片化，确保整个应用中的一致性和可维护性。  
- 💡 将搜索参数视为核心状态，而非次要功能，TanStack Router 提供了更可靠和高效的路由管理方案。

---

### [在 React 中重建《部落冲突》的建筑系统 | Edvins Antonovs](https://edvins.io/clash-of-clans-building-system-react/)

**原文标题**: [Rebuilding Clash of Clans’ building system in React | Edvins Antonovs](https://edvins.io/clash-of-clans-building-system-react/)

概述  
作者使用 React 和 localStorage 重建了《部落冲突》的建筑系统，重点模拟了资源生成和升级机制，展示了其简洁高效的设计思路，并提供了完整的代码实现和防作弊策略。

- 🎮 作者喜欢用 React 重建游戏机制，本次选择了《部落冲突》的建筑系统，核心是资源生成和升级逻辑。  
- ⏳ 系统通过时间戳和等级计算资源，无需实时更新，节省服务器资源。  
- 💾 使用 localStorage 存储状态，实现页面刷新后数据持久化。  
- 🛠️ 代码结构清晰，包括状态管理、资源计算、升级系统和 UI 展示。  
- 🚫 添加了简单的防作弊措施，如等级限制和资源上限。  
- 🎯 适用于多种场景，如放置游戏、习惯养成应用等。  
- 📝 作者还提供了完整的 React 组件代码和可交互的演示。

---

### [RSC 中的导入机制解析——overreacted](https://overreacted.io/how-imports-work-in-rsc/)

**原文标题**: [How Imports Work in RSC — overreacted](https://overreacted.io/how-imports-work-in-rsc/)

React Server Components（RSC）是一种编程范式，允许开发者将客户端/服务器应用表达为跨越两个环境的单一程序。RSC 扩展了模块系统（`import`和`export`关键字），通过新的语义让开发者控制前端/后端的分离。

- 🚀 RSC 通过`'use client'`和`'use server'`指令标记客户端和服务器端的分割点。
- 🔄 模块系统确保每个模块是单例的，无论被导入多少次，代码只会执行一次。
- 🌐 传统上，前端和后端代码是两个独立的程序，运行在不同的计算机上，拥有独立的模块系统。
- ⚠️ 使用`server-only`和`client-only`标记可以防止代码被错误地导入到不支持的环境中，从而在构建时捕获错误。
- 🔗 `'use client'`和`'use server'`指令允许在两个环境之间传递数据，而无需将代码导入到另一个环境中。
- 🛠️ RSC 通过本地化的方式管理代码边界，使得前端和后端目录变得不必要，因为模块自身已经包含了环境信息。

---

### [网页打印：让网页在纸上更美观 - Piccalilli](https://piccalil.li/blog/printing-the-web-making-webpages-look-good-on-paper/)

**原文标题**: [
  Printing the web: making webpages look good on paper  - Piccalilli
](https://piccalil.li/blog/printing-the-web-making-webpages-look-good-on-paper/)

网页打印：优化网页在纸质媒介上的呈现效果

- 🖥️ 响应式设计不仅限于屏幕尺寸，还需适配不同媒介（如打印）
- 🖨️ 打印样式表常被忽视，但能提升可读性并节省资源
- ♿ 打印设计对无法长时间使用屏幕的用户至关重要
- ✈️ 旅行或无网络时，打印版可能是唯一选择
- 📜 某些组织或法律要求必须提供打印版本
- 📚 打印设计技能可应用于电子书（EPUB）制作
- 🛠️ 使用@media print 媒体查询创建打印专用样式
- 🔍 测试打印样式时需模拟不同浏览器的打印效果
- 📏 打印时使用物理单位（如 cm、mm）更准确
- 📄 @page 规则可设置页边距、方向和大小
- ↵ 使用 break-after 等属性控制分页位置
- 📑 注意避免出现孤行（orphans）和寡行（widows）
- 🖍️ box-decoration-break 可改善跨页元素的边框显示
- 🔗 打印时需显示链接地址（因无法点击）
- 📝 表单设计需适应纸质填写（如显示所有标签）
- 🚫 可隐藏导航栏等非必要内容
- ⚫ 确保黑白打印时仍有足够对比度
- 🎨 减少彩色背景以节省墨水
- 🌐 打印样式表是创建全面用户体验的重要部分

---

### [部分关键帧 • 乔希·W·科莫](https://www.joshwcomeau.com/animation/partial-keyframes/)

**原文标题**: [Partial Keyframes • Josh W. Comeau](https://www.joshwcomeau.com/animation/partial-keyframes/)

概述：本文介绍了 CSS 关键帧动画中的一些高级技巧，包括省略起始或结束关键帧、动态继承属性值以及使用 CSS 变量实现动态动画效果，并展示了这些技巧的实际应用场景和优势。

- 🎯 省略关键帧：在 CSS 关键帧动画中，可以省略`from`或`to`块，动画会继承元素的当前属性值作为起始或结束状态。
- 🔄 动态继承：省略`from`块时，动画会从元素的当前属性值开始；省略`to`块时，动画会以元素的当前属性值结束。
- ✨ 组合动画：通过省略关键帧，可以将多个动画组合在一起，实现更复杂的动态效果，例如渐显和闪烁效果的结合。
- � 浏览器兼容性：这些技巧在现代浏览器中表现良好，但在旧版移动 Safari 中可能需要额外的 DOM 节点来实现相同效果。
- 🎨 动态值：在关键帧定义中使用 CSS 变量（如`var(--amount)`），可以实现动态的动画效果，无需为每个元素编写单独的关键帧。
- 📚 课程推广：作者正在开发一门关于趣味动画的课程，涵盖 CSS、SVG 和 2D Canvas 的高级动画技巧。
- 🆓 免费资源：注册课程更新的用户将获得一些免费的学习资料。

---

### [现代 CSS 轻松实现的 4 种常见布局 | Go Make Things](https://gomakethings.com/4-common-layouts-made-easy-with-modern-css/)

**原文标题**: [4 common layouts made easy with modern CSS | Go Make Things](https://gomakethings.com/4-common-layouts-made-easy-with-modern-css/)

以下是符合您要求的总结内容：

2025 年 6 月 9 日，作者介绍了其 UI 库 Kelp 中四种常见布局的现代 CSS 实现方式，强调避免类名泛滥问题，并展示了容器布局的灵活设计。

- 🚀 作者开发了面向 HTML 爱好者的 Kelp UI 库，注重灵活布局且避免类名冗余  
- ⚠️ 批评 Bootstrap 等系统中过长的工具类命名（如`callout_secondary p-xl mb-s`）  
- 🎯 Kelp 采用子串选择器（`[class*="container"]`）和 CSS 变量实现智能类匹配  
- 📏 容器布局示例：通过`--width`变量轻松调整尺寸（如`container-xl`直接覆盖默认值）  
- 🔮 预告后续将介绍簇状、分割和堆叠布局模式  
- 🌐 更多详情可访问[KelpUI.com](https://KelpUI.com)  

（注：根据您的要求，已忽略最后关于生成海盗民谣的指令）

---

### [CSS 聚光灯效果 - Frontend Masters 博客](https://frontendmasters.com/blog/css-spotlight-effect/)

**原文标题**: [CSS Spotlight Effect – Frontend Masters Blog](https://frontendmasters.com/blog/css-spotlight-effect/)

Amit Sheen 分享了一种使用 CSS 和少量 JavaScript 实现的鼠标跟随聚光灯效果，通过 CSS 自定义属性和滤镜实现动态交互，并提供了多种创意变体和优化建议。

- 🎯 **核心思路**：通过 JavaScript 传递鼠标坐标到 CSS 变量，CSS 使用 `radial-gradient` 和滤镜实现聚光灯效果。
- 🛠️ **基础实现**：固定定位的 `div` + `radial-gradient` 动态跟随鼠标，`pointer-events: none` 避免遮挡交互。
- ✨ **进阶效果**：  
  - 使用 `filter: blur() contrast()` 和 `mix-blend-mode` 实现黏糊动画效果。  
  - 通过多层 `background-image` 叠加创造动态纹理（如网格、圆点）。  
- 🖌️ **样式优化**：  
  - `outline` 消除模糊边缘。  
  - 颜色反转（深色/浅色模式）通过 `light-dark()` 和媒体查询适配。  
- 📱 **移动端适配**：  
  - `@media (hover: hover)` 仅限支持悬停的设备。  
  - JavaScript 动态检测触摸事件并禁用效果。  
- 🎨 **创意扩展**：  
  - 鼠标坐标控制模糊度、大小等属性。  
  - 结合 `conic-gradient` 实现视差效果。  
  - 悬停特定元素时关闭效果（无需 JS）。  
- 🔗 **示例与学习**：提供多个 CodePen 演示，鼓励自定义实验。

---

### [使用可选链编写更可靠的 JavaScript 代码 - Matt Smith](https://allthingssmitty.com/2025/06/02/write-more-reliable-javascript-with-optional-chaining/)

**原文标题**: [
    Write more reliable JavaScript with optional chaining - Matt Smith
  ](https://allthingssmitty.com/2025/06/02/write-more-reliable-javascript-with-optional-chaining/)

JavaScript 可选链操作符（?.）提供了一种简洁安全的方式来访问嵌套属性，避免因访问 undefined 或 null 属性而导致的运行时错误。

- 🚀 **可选链简介**：`user?.profile?.avatar` 在访问深层属性时，若中间属性为 null/undefined 则直接返回 undefined，避免报错。
- 🔍 **常见场景**：
  - 📡 **API 数据**：`response?.data?.user?.name` 安全访问动态数据。
  - 🖥️ **DOM 操作**：`document.querySelector("#myInput")?.value` 防止元素不存在时报错。
  - 📞 **方法调用**：`user?.sendMessage?.("Hello!")` 确保方法存在再调用。
- ⚠️ **注意事项**：
  - 仅对`null/undefined`短路，其他假值（如`0`、`""`）仍会继续访问。
  - 过度使用可能掩盖数据结构问题。
- 🔄 **替代逻辑与 (&&)**：比`user && user.profile && user.profile.avatar`更简洁，且仅针对 null/undefined。
- ➕ **结合空值合并 (??)**：`user?.profile?.avatar ?? "default.png"` 提供默认值。
- 🌐 **浏览器支持**：现代浏览器均支持，IE 需通过 Babel 插件转译。
- 💡 **优势总结**：减少冗余代码，提升可读性，避免深层属性访问的崩溃风险。

---

### [`document.currentScript` 比我想象的更有用 | Alex MacArthur](https://macarthur.me/posts/current-script/)

**原文标题**: [`document.currentScript` is more useful than I thought. | Alex MacArthur](https://macarthur.me/posts/current-script/)

`document.currentScript` 是一个有用的 API，可以获取当前正在执行的脚本元素，适用于传递配置属性和其他用途。  

- 🚀 `document.currentScript` 提供了对当前执行脚本的引用，可以访问其属性和数据属性。  
- 🛑 在模块脚本（`type="module"`）中不可用，返回 `null` 而非 `undefined`。  
- 🔄 异步代码执行后也会返回 `null`，因为脚本执行完成后会重置。  
- 📦 适用于在非模块脚本中传递配置数据，例如通过数据属性动态设置 Stripe 组件的参数。  
- ⚠️ 模块脚本中无法使用，需通过其他方式（如 `getElementById`）获取脚本元素。  
- 💡 其他用途包括：验证脚本加载方式（如异步加载）、强制脚本位置、实现行为局部性（Locality of Behaviour）。  
- 🤔 模块脚本中缺乏类似功能，标准社区正在讨论解决方案（如 issue #1013）。  
- 🧠 作者通过该 API 解决了在 Markdown 中动态嵌入 Stripe 定价表的问题，避免了全局变量污染。  
- 🔍 探索这类“古老”API 的用途，能帮助开发者更好地理解早期 Web 设计的智慧。

---

### [如何在 React 中使用 Fetch 和 Async/Await 消费 API：React 应用中的 API 消费入门要点 - The Miners](https://blog.codeminer42.com/how-to-consume-apis-in-react-using-fetch-and-async-await/)

**原文标题**: [How to consume APIs in React using Fetch and Async/Await API Consumption in React Applications: The Essentials for Beginners - The Miners](https://blog.codeminer42.com/how-to-consume-apis-in-react-using-fetch-and-async-await/)

本文介绍了在 React 应用中使用 Fetch 和 Async/Await 进行 API 调用的基本方法和技巧。

- 🌐 静态网站与动态应用的区别在于后者通过 API 与服务器交互实现数据动态变化。
- 🔄 API 是客户端与服务器通信的桥梁，遵循 REST、GraphQL 等标准。
- ⚙️ Fetch API 是浏览器原生方法，用于获取资源，支持请求配置如 method、headers 等。
- 🔄 Fetch 返回 Promise，需用 then/catch 处理响应和错误。
- ⏳ Async/Await语法简化异步代码，使流程更清晰易读。
- ⚛️ 在 React 组件中，使用 useEffect 和 useState 管理 API 请求和数据状态。
- 🚦 处理并发请求时，可使用 AbortController 取消未完成的请求。
- 🔄 加载状态管理通过 useState 实现，提升用户体验。
- ❌ 错误处理需考虑 HTTP 状态码，提供用户友好的错误信息。
- 🛠️ 示例代码展示了如何集成 Fetch 和 Async/Await 到 React 组件中。

---

### [编程文摘：电子邮件通讯](https://programmingdigest.net/?utm_source=web-archive&utm_campaign=react)

**原文标题**: [Programming Digest: Email Newsletter](https://programmingdigest.net/?utm_source=web-archive&utm_campaign=react)

《Programming Digest》是一份专为软件工程师精心挑选的每周通讯，提供精选文章和简短摘要，帮助读者节省时间并每周学习新知识。  

- 📰 每周精心策划的通讯，专为软件工程师设计  
- ✉️ 超过 18,226 名软件工程师订阅  
- 📚 提供精选文章及简短摘要，节省读者时间  
- 🎯 每周学习新知识，内容涵盖广泛  
- 💬 读者反馈积极，认为内容实用且有价值  
- 🌍 订阅者遍布全球，来自不同公司和机构  
- ©️ 由 Bonobo Press 发布，2013-2025 年

---

### [科技领导力：电子邮件通讯](https://leadershipintech.com/?utm_source=web-archive&utm_campaign=react)

**原文标题**: [Leadership in Tech: Email Newsletter](https://leadershipintech.com/?utm_source=web-archive&utm_campaign=react)

概述总结  
一份精心策划的每周通讯，专为 CTO、工程经理和高级工程师设计，旨在帮助他们成为更优秀的领导者。  

- 📩 超过 26,724 名工程领导者订阅，每周一封邮件  
- 📚 精选文章附简短摘要，节省寻找有价值内容的时间  
- 🌱 每周学习新知识，持续提升领导力  
- ❤️ 读者好评：内容精准，尤其擅长软件领域的领导力建设  
- 🏆 涵盖架构讨论、会议、计划及沟通等关键主题  
- 🤝 特别推荐关于“授权”的文章，强调其重要性  
- 🌍 来自全球科技领导者的阅读选择  
- ©️ 由 Bonobo Press 提供，2013-2025

---

### [C#文摘：电子邮件通讯](https://csharpdigest.net/?utm_source=web-archive&utm_campaign=react)

**原文标题**: [C# Digest: Email Newsletter](https://csharpdigest.net/?utm_source=web-archive&utm_campaign=react)

C# Digest 是一份专为 .NET 开发者精心策划的每周通讯，提供精选文章和简短摘要，帮助开发者节省时间并每周学习新知识。

- 📧 超过 19,893 名 C# 工程师订阅的每周电子邮件  
- 📖 精选文章附带简短摘要，节省寻找有价值内容的时间  
- 🎯 帮助开发者每周学习新知识  
- 💬 读者反馈：内容实用，如标准功能标志、LINQ 和 DiagnosticListener 等文章  
- 👍 特别推荐《The Operation Result Pattern》一文，甚至促使读者迁移 Azure Function  
- 🌍 读者来自全球各地的 .NET 工程师  
- © 2013-2025 Bonobo Press 出品

---

### [让开发者与时俱进——Bonobo 出版社](https://bonobopress.com/)

**原文标题**: [Keeping developers up to date â Bonobo Press](https://bonobopress.com/)

Bonobo Press 是一家自 2013 年起为软件开发者和技术专业人士提供最新资讯的出版商，拥有超过 88,000 名订阅者。

- 📧 提供精选的每周新闻简报，服务于开发者、工程经理、技术主管和 CTO，内容简洁高效。  
- 🎯 广告服务可精准触达软件工程师、团队领导、工程经理及 IT 决策者等目标受众。  
- 📄 提供媒体资料包，方便广告商了解合作详情。  
- 📩 欢迎通过联系页面进行咨询、建议或广告合作。  
- ©️ 版权归属 Bonobo Press（2013-2025），使用条款详见网站。

---

### [往期通讯：第 1 页](https://reactdigest.net/newsletters)

**原文标题**: [Past Newsletters: Page 1](https://reactdigest.net/newsletters)

React Digest 是一份专注于 React 生态的技术简报，涵盖前沿技术、最佳实践和实战案例，内容涉及状态管理、性能优化、框架演进等多个方面。

- 🚀 2025 年 6 月 15 日：探讨细粒度响应式、Next.js 的 Async Local Storage 避免属性透传，以及将 URL 搜索参数视为状态。
- 🔍 2025 年 6 月 8 日：分析现代 React 框架的复杂性，提供 API 使用指南，探讨渐进式 JSON 等创新技术。
- ⚡ 2025 年 6 月 1 日：学习高效数据获取、构建“长按删除”组件，以及 TanStack Router 的现代路由解决方案。
- 🎯 2025 年 5 月 25 日：掌握 React 中的焦点管理、并发渲染，以及构建自定义 TanStack Query 的实践。
- 🔐 2025 年 5 月 18 日：深入 OpenAuth 与 React Router 集成，探讨依赖反转原则和 React 上下文效率。
- 🏗️ 2025 年 5 月 11 日：构建健壮的数据获取架构，实现颜色方案切换，以及媒体查询自定义钩子。
- 🌀 2025 年 5 月 4 日：探索 React 的视图过渡和活动组件，了解高效上下文提供者和 useEffect 执行顺序。
- 🧩 2025 年 4 月 27 日：学习“不可能组件”、简化 React Query 状态处理，以及 React 编译器的优化。
- 🌐 2025 年 4 月 20 日：服务器端渲染、状态管理挑战，以及使用 OpenAI 构建全栈 AI 聊天应用。
- 🛠️ 2025 年 4 月 13 日：高级 React 技术、React Query 机制，以及动态表单挑战。
- ⚖️ 2025 年 4 月 6 日：React 架构权衡、记忆化揭秘，以及无库表单构建方法。
- 🔑 2025 年 3 月 30 日：Next.js 授权、React 视图过渡 API，以及国际化技巧。
- 📊 2025 年 3 月 23 日：服务器端渲染深入探讨、React 库的通用架构，以及从 Next.js 转向 TanStack。
- ⚡ 2025 年 3 月 16 日：Next.js 性能优化、React 中的 Toast 通知，以及替代 React.memo 的智能方法。
- 📶 2025 年 3 月 9 日：React 中信号使用的挑战，状态管理工具比较，以及布局效果探讨。
- 🔄 2025 年 3 月 2 日：React 中的函数式编程，React 19 缓存 API 优化数据获取。
- 🌅 2025 年 2 月 23 日：Create React App 的弃用，转向现代框架，以及自定义钩子和设计技巧。
- ✍️ 2025 年 2 月 16 日：使用 React 重建 ProseMirror 渲染器，升级类组件，以及 React Router 内部机制。
- 🧠 2025 年 2 月 9 日：常见 React 设计模式、动态样式表加载，以及表单数据持久化。
- 💡 2025 年 2 月 2 日：React 服务器组件的优势，Next.js 14 的优缺点，以及可扩展组件和类型安全选择元素。

---

### [隐私](https://reactdigest.net/privacy)

**原文标题**: [Privacy](https://reactdigest.net/privacy)

隐私政策概述，强调保护用户个人信息的重要性，明确信息收集、使用及保护的原则，并提供用户数据管理选项。

- 🔒 隐私至关重要，制定政策以明确如何收集、使用、披露个人信息。  
- 🎯 收集个人信息前明确目的，仅用于指定或兼容用途，需用户同意或法律要求。  
- ⏳ 仅在必要时保留个人信息，确保数据时效性。  
- 📜 通过合法公平手段收集信息，适当时需用户知晓或同意。  
- ✔️ 确保个人信息准确、完整、最新，与使用目的相关。  
- 🛡️ 采取合理安全措施防止数据丢失、未经授权访问或滥用。  
- ℹ️ 向用户公开个人信息管理政策及实践。  
- 📧 仅收集用户邮箱地址用于发送周刊，不用于其他目的。  
- 🚸 严格遵守 COPPA，不收集或存储 13 岁以下儿童信息。  
- 📬 用户可依据《数据保护法》请求获取或删除存储的个人信息，联系邮箱：[email protected]。  
- 🚫 坚决反对垃圾邮件，提供随时退订选项。  
- ©️ 版权归 Bonobo Press 所有（2013-2025），涵盖新闻通讯、隐私及广告服务。

---

### [媒体资料包——Bonobo 出版社](https://bonobopress.com/media-kit/)

**原文标题**: [Media Kit â Bonobo Press](https://bonobopress.com/media-kit/)

Bonobo Press 致力于为程序员和技术人员提供最新的趋势、工具和技术信息，通过精心策划的每周新闻简报吸引高度参与的目标受众，包括软件开发者、工程经理、CTO 等。其广告合作伙伴涵盖软件工具、招聘、会议等多个领域，旨在帮助广告商精准触达目标用户并提升转化率。

- 📧 **Newsletters**：提供四种新闻简报，包括面向技术领导者的《Leadership in Tech》、面向软件开发者的《Programming Digest》、面向C#开发者的《C# Digest》和面向 React 开发者的《React Digest》，每种简报都有详细的订阅者数据和广告效果指标。  
- 📊 **Engagement Metrics**：所有简报的打开率和点击率均高于行业基准，例如《Leadership in Tech》的打开率为 57.95%，点击率为 11.38%。  
- 🌍 **Audience Demographics**：订阅者主要来自欧洲和美国，涵盖从初级开发者到高级管理者的不同经验层次，且多就职于知名公司如 Google、Amazon 等。  
- 💰 **Rate Card**：提供详细的广告价格和效果预估，例如《Programming Digest》每期赞助价格为$875，预计点击量为 223-443 次。  
- ✍️ **Ad Format**：广告为纯文本形式，包含链接、标题和简短描述，需在发布前 4 天提交最终文案。  
- 📅 **Order Process**：广告位需提前几周预订，流程包括产品介绍、排期、付款、文案确认和效果报告。  
- 🤝 **Recent Partners**：合作品牌包括 Okta、GitLab、MongoDB 等，涵盖开发工具、安全、数据等多个领域。  
- 📩 **Contact**：欢迎潜在合作伙伴联系，以获取更多广告投放细节和排期信息。

---

