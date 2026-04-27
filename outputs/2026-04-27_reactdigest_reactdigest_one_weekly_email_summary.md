### [React 文摘：电子邮件通讯](https://reactdigest.net/)

**原文标题**: [React Digest: Email Newsletter](https://reactdigest.net/)

这是一份为React开发者精心策划的每周通讯，已吸引超过22,858名前端工程师订阅，旨在通过精选文章和简短摘要节省阅读时间，每周学习新知识。

- 📬 每周一封邮件，精选React相关优质文章并附简短摘要
- ⏱️ 帮助开发者节省筛选内容的时间，聚焦有价值信息
- 🧠 每周都能学到新知识，保持技术更新
- 👍 读者反馈积极，称赞文章实用且紧跟技术演进（如Concurrent Mode）
- 🌍 读者来自全球各大公司前端团队
- 📅 自2013年起持续运营，提供新闻通讯、隐私及广告服务

---

### [React编译器十八个月：历程、争议与未来展望 | Sascha Becker](https://saschb2b.com/blog/react-compiler-year-in-review)

**原文标题**: [The React Compiler at Eighteen Months: The Arc, the Debates, and What's Next | Sascha Becker](https://saschb2b.com/blog/react-compiler-year-in-review)

React 19 编译器发布十八个月后，生态系统经历了框架集成、工具成熟和社区辩论等阶段，当前状态是：新项目已解决，旧项目仍需努力。

- 📅 **十八个月历程**：从发布配置、框架集成，到早期采用者报告“无聊”的胜利（减少重渲染bug），再到2025年底生态系统的反思——许多旧库实际上一直违反React规则。
- ⚙️ **编译器核心功能**：构建时自动插入记忆化，消除手动`useMemo`/`useCallback`/`memo`，提升重渲染扩展性，但会增加构建时间和少量包体积。
- ❌ **编译器失效场景**：渲染时修改props/闭包、渲染时读取ref、遗留类组件、以及`"use no memo"`逃生口（应视为TODO而非永久标记）。
- 🛤️ **推荐迁移路径**：先更新React→安装ESLint插件修复违规→注释驱动模式测试→推理模式全量启用→批量删除手动记忆化→考虑严格模式。
- 🔥 **持续争议**：React规则从“理想”变为“可执行合约”的强制性、`"use no memo"`成为技术债务指标、编译器与运行时优化器（如Million.js）的互补关系。
- 🔮 **未来方向**：更细粒度的编译控制、编译器感知的服务器组件、`useEvent`收敛、React Native优化、以及开发者工具可视化编译器行为。
- 💡 **个人观点**：编译器的最大遗产是淘汰了“忘记`useCallback`依赖”这类bug，但更关键的是推动整个库生态系统遵守React规则。新项目应直接启用，旧项目需权衡修复遗留代码或使用逃生口。

---

### [网络研讨会：移动应用安全事件的经验教训](https://www.guardsquare.com/webinar-lessons-learned-from-security-incidents-in-mobile-apps?utm_campaign=31454753-2026%20Real%20Attacks.%20Real%20Defenses.&utm_source=ReactDigest&utm_medium=newsletter)

**原文标题**: [Webinar: Lessons Learned from Security Incidents in Mobile Apps](https://www.guardsquare.com/webinar-lessons-learned-from-security-incidents-in-mobile-apps?utm_campaign=31454753-2026%20Real%20Attacks.%20Real%20Defenses.&utm_source=ReactDigest&utm_medium=newsletter)

本次网络研讨会总结了移动应用安全事件中的关键教训，涵盖银行、外卖和电商领域的真实案例，旨在帮助开发者避免常见漏洞。

- 📱 移动应用已成为全球商业的主要入口，处理76%的活跃银行用户和63%的电商收入
- 🔒 网络研讨会由安全研究员Jan Seredynski主持，深入分析近期移动应用安全事件
- 🛡️ 涵盖人脸验证绕过、位置欺骗和活动注入等高级攻击手段
- 📋 通过银行、外卖和电商的真实案例，解析漏洞发生原因及防范方法
- 🧠 明确开发过程中引入的漏洞类型
- ✅ 评估现代移动应用中安全原则的有效性及失效情况
- 💡 提供来自真实世界案例的实用见解
- 🚀 鼓励注册以创建安全的移动电商体验

---

### [将铁路前端从Next.js迁移](https://blog.railway.com/p/moving-railways-frontend-off-nextjs)

**原文标题**: [Moving Railway's Frontend Off Next.js](https://blog.railway.com/p/moving-railways-frontend-off-nextjs)

概述总结  
- 🚄 Railway的前端从Next.js迁移到了Vite + TanStack Start，通过两个PR实现零停机切换。  
- ⏱️ 构建时间从10分钟以上缩短到2分钟以内，开发服务器启动接近即时。  
- 🧩 采用客户端优先架构，利用类型安全路由、一级布局和显式模型，减少框架魔法。  
- 🖼️ 放弃内置图片优化，改用`<img>`标签和Fastly边缘优化。  
- 🔧 替换了部分生态工具（如next-seo），用自建方案替代。  
- 🌐 前端部署在Railway自身平台上，利用Fastly边缘缓存和ISR，资产按内容哈希分块，更新仅影响相关模块。  
- 🎯 迁移后迭代速度显著提升，团队享受更快的反馈循环和更明确的控制权。

---

### [Next.js中的'use client'：作用、代价与使用时机](https://punits.dev/blog/use-client-in-nextjs/)

**原文标题**: ['use client' in Next.js: What It Does, What It Costs, and When to Use It](https://punits.dev/blog/use-client-in-nextjs/)

`use client` 指令让 Next.js 组件在保留服务端渲染的同时，也能够在浏览器端运行，以支持交互功能（如 React hooks 和事件处理）。但启用它需要付出 JavaScript 包体积增大、客户端水合开销增加以及数据获取瀑布流等代价，因此应谨慎使用，并优先将其放在叶子组件中。

- 📦 **增加包体积**：Client Component 的 JavaScript 会被发送到浏览器，导致包体积增大（示例中从 157 kB 增至 215 kB）。
- ⚡ **水合成本**：浏览器需要水合 Client Component 使其可交互，这会占用主线程，可能延迟交互并影响 INP 指标。
- 🌊 **数据获取瀑布流**：Client Component 中数据获取通常使用 `useEffect`，导致内容在客户端水合后才开始加载，延迟显示并破坏流式渲染。
- 🔍 **SEO 影响有限**：`use client` 本身不损害 SEO，但若组件在 `useEffect` 中获取数据，初始 HTML 可能缺少内容，影响搜索引擎抓取。
- 🧩 **最佳模式**：将 `use client` 放在需要交互的叶子组件中，并通过 props 传递 Server Component，以保持大部分组件树为 Server Component。
- ✅ **使用时机**：当组件需要 React hooks、事件处理或浏览器 API 时使用。
- ❌ **避免时机**：当组件仅渲染数据或可在服务端获取数据时，优先使用 Server Component。

---

### [我基准测试了五种包膨胀模式并扫描了500个仓库，实际上只有两种真正重要。](https://stackinsight.dev/blog/bundle-bloat-empirical-study/)

**原文标题**: [I Benchmarked Five Bundle Bloat Patterns and Scanned 500 Repos. Only Two Actually Matter.](https://stackinsight.dev/blog/bundle-bloat-empirical-study/)

概述总结：
一项针对五种常见打包膨胀模式的基准测试和500个仓库的扫描显示，只有两种模式（lodash和moment.js）会显著增加打包体积，而其他模式（如桶导入）在现代打包工具下影响微乎其微。

- 📊 基准测试结果：lodash默认导入比tree-shakeable替代方案大17.6倍（25.3 KB gzip），moment.js比dayjs大5.9倍（16.8 KB gzip），而MUI、antd和react-icons的导入模式差异为零。
- 🔍 扫描发现：在500个仓库中，21.2%存在至少一种膨胀模式，共17,594个发现。桶导入占74.7%但无实际影响，而高严重性的lodash和moment导入占20.7%，总计3,637个实例。
- 💡 关键建议：优先替换lodash为lodash-es，moment为dayjs，可节省大量体积。停止将桶导入转换为路径导入，因为现代打包工具（esbuild、Vite、webpack 5）已能正确处理。
- 🛠️ 实操指南：使用grep命令快速查找高影响模式，或使用打包分析工具。更新ESLint规则，专注于lodash和moment导入的检查。
- ⚠️ 注意事项：基准测试仅使用esbuild，结果可能因打包工具版本而异。扫描中的许多发现位于库源代码或测试文件中，不一定影响生产环境。

---

### [预计算模式：在Next.js中将动态数据编码到URL中 | Aurora Scharff](https://aurorascharff.no/posts/the-precompute-pattern-encoding-dynamic-data-into-urls-in-nextjs/)

**原文标题**: [The Precompute Pattern: Encoding Dynamic Data into URLs in Next.js | Aurora Scharff](https://aurorascharff.no/posts/the-precompute-pattern-encoding-dynamic-data-into-urls-in-nextjs/)

### 概述总结

本文介绍了 Next.js 中“预计算模式”（Precompute Pattern），这是一种通过将动态数据编码到 URL 中来避免动态渲染的技术，适用于需要静态生成但包含用户特定数据的场景。文章详细阐述了其工作原理、实现步骤、与 Vercel Flags SDK 的关联、电商场景下的高基数问题，以及 Next.js 16 中 `'use cache'` 如何使其在某些情况下不再必要。

- 📝 **核心问题**：在 Next.js 中，`cookies()` 或 `headers()` 等动态 API 调用会使整个页面树变为动态渲染，影响性能。
- 🔄 **预计算模式**：通过在中间件（proxy）中解析动态数据（如登录状态），将其编码为 URL 段，使页面仅依赖 `params` 实现静态生成。
- 🛠️ **实现步骤**：定义上下文类型与编解码函数 → 在中间件中重写 URL → 组件从 `params` 读取数据 → 使用 `generateStaticParams` 预生成变体。
- 🔒 **Vercel Flags SDK**：该模式被 SDK 正式化，提供 `precompute` 和 `generatePermutations` 函数，支持加密和构建时生成。
- ⚠️ **高基数权衡**：电商场景中，预计算维度（如语言、货币）会指数级增加页面变体，导致构建时间过长和 ISR 缓存命中率下降。
- 🚀 **`'use cache'` 替代方案**：Next.js 16 的 `'use cache'` 允许组件级缓存，避免动态渲染，但预计算模式在需要根据区域、货币等变化缓存内容时仍有用。
- 🧩 **rootParams 未来改进**：即将推出的 `rootParams` 功能可消除 `requestContext` 的 prop drilling，使组件直接访问顶层参数，简化代码。
- 📚 **实际应用**：该模式已用于大型电商团队，结合 ISR 和选择性预计算来平衡性能与灵活性。

---

### [JavaScript 中真正的新特性（以及即将到来的更新）—— Neciu Dan](https://neciudan.dev/whats-new-in-javascript)

**原文标题**: [What's actually new in JavaScript (and what's coming next) — Neciu Dan](https://neciudan.dev/whats-new-in-javascript)

以下是您提供的文章摘要：

ES2025已发布，ES2026即将到来。本文介绍了JavaScript中可立即使用的新特性、即将推出的功能，以及如何让AI编码助手也掌握这些新语法。

- 📜 **TC39委员会**：由浏览器厂商和公司代表组成，通过共识决定JavaScript的演进，提案需经历从Stage 0到Stage 4的严格流程才能成为正式特性。
- 🚀 **ES2025核心新特性**：包括迭代器辅助方法（`.map`、`.filter`、`.take`等，支持惰性求值）、Set方法（`union`、`intersection`等）、JSON模块原生导入、`Promise.try`、`RegExp.escape`和`Float16Array`。
- 🔮 **ES2026即将落地**：`Math.sumPrecise`（高精度浮点求和）、`Uint8Array`的base64/hex方法、`Error.isError`（跨领域错误检测）、`Iterator.concat`、`Map.getOrInsert`、`Array.fromAsync`和带源文本的`JSON.parse`。
- ⏳ **引擎已实现但未入ES2026**：`Temporal`（日期时间终极方案，预计ES2027）、`using`关键字（资源自动清理）和`import defer`（模块延迟求值）已在浏览器中成熟，但未赶上ES2026快照。
- 🤖 **AI编码助手适配**：由于训练数据老旧，AI常输出过时模式。文章提供了可嵌入提示词的“现代JavaScript偏好”规则，指导AI优先使用ES2025/ES2026新API。

---

### [我为什么不再在JavaScript中链式调用一切 - 马特·史密斯](https://allthingssmitty.com/2026/04/20/why-i-dont-chain-everything-in-javascript-anymore/)

**原文标题**: [
    Why I don't chain everything in JavaScript anymore - Matt Smith
  ](https://allthingssmitty.com/2026/04/20/why-i-dont-chain-everything-in-javascript-anymore/)

### 概述总结
作者分享了自己从习惯使用JavaScript方法链到逐步拆分代码的经验，强调链式调用虽然简洁，但在可读性、调试和性能上存在隐患，建议根据步骤数量合理拆分。

- 📉 **链式调用的陷阱**：长链（如`filter→map→sort→slice`）需要脑力解析每一步，增加阅读负担。
- 🧩 **分步代码更清晰**：将链式调用拆分为命名变量（如`activeUsers`、`names`），每步独立，无需解码。
- 🔍 **调试困难**：链式代码中插入`console.log`会污染逻辑，而分步代码可单独检查每一步。
- ⚡ **性能浪费**：链式调用会处理整个数组（如`filter→map→[0]`），而`find`或`for`循环可提前终止。
- 🔄 **异步链式同样问题**：`.then()`链混合了异步控制流与数据转换，拆分后更易理解。
- 📏 **实用规则**：1-2步链式可接受，3-4步需考虑拆分，5步以上必须拆分。
- 🛠️ **拆分方法**：命名中间值（如`const activeUsers = ...`）、按逻辑分离转换、仅保留短链。
- 💡 **核心观点**：快速编码时链式方便，但长期维护时分步代码更可靠。

---

### [font-family 的回退方式并非你所想 – CSS Wizardry](https://csswizardry.com/2026/04/font-family-doesnt-fall-back-the-way-you-think/)

**原文标题**: [font-family Doesn’t Fall Back the Way You Think – CSS Wizardry](https://csswizardry.com/2026/04/font-family-doesnt-fall-back-the-way-you-think/)

概述总结
- 📊 Harry Roberts 是一位独立顾问，专门从事网页性能工程，帮助各类公司发现并解决网站速度问题。

---

### [构建无断点的用户界面 – 前端大师博客](https://frontendmasters.com/blog/building-a-ui-without-breakpoints/)

**原文标题**: [Building a UI Without Breakpoints – Frontend Masters Blog](https://frontendmasters.com/blog/building-a-ui-without-breakpoints/)

本文探讨了现代响应式设计如何从依赖断点转向基于内在布局和容器特性的自适应系统，并提供了具体实现方法和迁移建议。

- 📉 断点模式局限性：传统基于视口宽度的断点设计在组件化、嵌套化场景中导致CSS冗余、耦合度高，且难以适应多样化的设备环境。
- 🧩 内在布局优先：使用CSS Grid的`auto-fit`和`minmax()`实现自适应网格，或通过Flexbox的`flex-wrap`和弹性值创建流畅的两栏布局，无需断点即可自动调整列数。
- 📏 流体值替代阶梯值：利用`clamp()`函数让字号、间距等属性在视口变化时连续缩放，避免离散断点导致的突兀变化，同时减少CSS代码量。
- 📦 容器单位实现局部响应：通过`container-type`和`cqi`单位，使组件尺寸基于自身实际宽度而非视口，提升组件在不同容器（如侧边栏、模态框）中的复用性。
- 🔄 容器查询处理结构变化：当组件空间变窄时，使用`@container`查询改变布局方向、隐藏次要内容，实现精准的局部结构切换，而非依赖全局断点。
- 🎯 媒体查询回归本质：将媒体查询用于设备能力（如悬停、指针精度）和用户偏好（如深色模式、减少动效），而非作为主要布局工具，以提升可访问性和适应性。
- 🛠️ 迁移实践清单：审计现有断点、用`clamp()`替换标量分支、采用内在布局、添加容器单位、仅在结构变化时使用容器查询、保留环境意图的媒体查询，并逐步测试组件在不同上下文中的表现。

---

### [MDN新前端的内幕](https://developer.mozilla.org/en-US/blog/mdn-front-end-deep-dive/)

**原文标题**: [Under the hood of MDN's new frontend](https://developer.mozilla.org/en-US/blog/mdn-front-end-deep-dive/)

MDN 前端架构全面重构，采用 Web Components 和自研服务端组件，大幅提升性能和开发体验。

- 🏗️ 旧架构问题：React SPA 技术债务严重，CSS 混乱，无法有效处理静态内容中的交互
- 🔧 核心解决方案：采用 Lit 构建 Web Components，实现内容中的交互岛，避免重复渲染
- 🎯 Scrimba 集成：首个 Web Component 原型，通过自定义元素 `<scrim-inline>` 嵌入交互式教程
- 💻 交互示例重构：将 Playground 拆分为多个 `<play-*>` 子组件，简化维护并支持宏语法直接嵌入
- 🚀 自研服务端组件：基于 Lit 模板语法构建，无客户端 JS 负担，支持 Declarative Shadow DOM
- 📦 按需加载：通过组件名自动懒加载 Web Component JS，仅加载页面所需 CSS/JS
- ⚡ 性能优化：HTTP/2/3 下多小文件并行加载，缓存友好，组件更新不影响其他组件
- 🌐 Baseline 策略：广泛可用特性直接使用，新特性渐进增强，减少 polyfill 开销
- 🛠️ 开发体验飞跃：使用 Rspack 构建，启动时间从 2 分钟降至 2 秒，单一命令即可运行
- 🔄 架构简化：统一构建流程，开发环境与生产环境高度一致，无需频繁重启

---

### [编程文摘：邮件通讯](https://programmingdigest.net/?utm_source=web-archive&utm_campaign=react)

**原文标题**: [Programming Digest: Email Newsletter](https://programmingdigest.net/?utm_source=web-archive&utm_campaign=react)

本内容介绍了一份面向软件工程师的精选周刊通讯《Programming Digest》。

- 📬 每周一封邮件，精选编程文章并附简短摘要，帮助节省筛选时间
- 🧠 旨在让读者每周都能学到新知识，涵盖API设计等热门话题
- ⭐ 读者反馈积极，称每期都有收获，如“Moving Faster”等文章备受好评
- 👥 订阅者超过23,331人，读者来自多家知名软件公司
- 📅 由Bonobo Press运营，提供新闻通讯、隐私及广告服务

---

### [科技领域的领导力：电子邮件通讯](https://leadershipintech.com/?utm_source=web-archive&utm_campaign=react)

**原文标题**: [Leadership in Tech: Email Newsletter](https://leadershipintech.com/?utm_source=web-archive&utm_campaign=react)

本内容介绍了一份专为CTO、工程经理及资深工程师设计的领导力技术周刊。

- 📧 每周一、四发送一封邮件，内容精选自手写文章并附简短摘要
- 👥 已有超过28,853名工程领导者订阅，帮助节省寻找优质内容的时间
- 🎯 涵盖领导力建设、架构讨论、会议规划、沟通技巧及授权等关键主题
- 💬 读者反馈积极，称赞内容精准且聚焦软件领域的领导力提升
- 🌐 读者来自全球顶尖科技公司，并附有隐私与广告声明

---

### [C# 文摘：电子邮件通讯](https://csharpdigest.net/?utm_source=web-archive&utm_campaign=react)

**原文标题**: [C# Digest: Email Newsletter](https://csharpdigest.net/?utm_source=web-archive&utm_campaign=react)

本内容介绍了C# Digest，一份面向.NET开发者的每周精选邮件通讯。

- 📬 每周一封邮件，精选C#文章并附简短摘要，节省开发者筛选时间
- 👥 已有超过20,268名C#工程师订阅，读者来自多家知名公司
- 💡 读者反馈：文章实用性强，如Operation Result Pattern、LINQ、DiagnosticListener等被实际应用于工作中
- ⏱️ 帮助开发者每周学习新知识，无需自行寻找优质内容
- 📅 由Bonobo Press自2013年起持续运营，提供新闻通讯、隐私及广告服务

---

### [保持开发者更新 – Bonobo Press](https://bonobopress.com/)

**原文标题**: [Keeping developers up to date â Bonobo Press](https://bonobopress.com/)

概述摘要  
- 📰 Bonobo Press 自2013年起发布软件新闻通讯，服务超过80,000名开发者、IT专业人士和技术人员。  
- 📬 提供面向软件开发者、工程经理、技术主管和CTO的简洁新闻通讯，深受技术人士喜爱。  
- 📢 提供广告服务，帮助客户精准触达软件工程师、团队领导、CTO等专业技术受众。  
- 📞 如有问题、建议或广告需求，可通过网站联系。

---

### [过往新闻简报：第1页](https://reactdigest.net/newsletters)

**原文标题**: [Past Newsletters: Page 1](https://reactdigest.net/newsletters)

以下是您提供的React Digest新闻摘要，涵盖了从2026年1月到4月的关键内容：

React Digest 2026年1月至4月新闻摘要，涵盖了性能优化、架构革新、工具升级和最佳实践等多个方面。

- 🚄 Railway用Vite替换Next.js，将10分钟构建缩短至2分钟；研究发现只有lodash和moment.js才真正导致包体积膨胀，而非普遍认为的桶导入。
- ⚡ MDN弃用React SPA，改用服务端HTML和Lit Web组件，开发构建从2分钟降至2秒；GitHub通过减少DOM和虚拟化加速大型PR差异对比。
- 🧵 React Fiber将渲染拆分为约5ms的块，确保点击等紧急更新优先；实用技巧包括useReducer优于useState的场景、startTransition与防抖的区别，以及避免无意义的memoization。
- 📘 一份指南为初级Web开发者梳理了隐性知识；同时文章揭示了信号并未真正解决React的怪癖，并展示了如何在Next.js App Router中优雅处理错误。
- 🪝 React的use()钩子打破常规，可在渲染时读取Promise并与Suspense协同工作，消除了经典的useEffect数据获取反模式；测试ID可能暗示可访问性问题，以及为useEffect函数命名的重要性。
- 🛠️ 重建18个月代码的经验教训：未经测试的代码库会伤害真实用户；Bippy工具允许在运行时访问React Fiber树而无需修改代码；单例模式可与React钩子良好搭配。
- 🔄 React状态更新是异步的——调用setState会排队重渲染，而非立即生效；AsyncLocalStorage允许任何函数获取React Router上下文，无需逐层传递。
- 💾 86%的前端项目存在内存泄漏，500个仓库中发现55,864种泄漏模式，主要源于定时器和事件清理缺失；React Fiber将渲染拆分为小块以保持浏览器响应，RSC在三种不同环境中处理错误。
- 🤖 本期探索了AI驱动的框架vinext、React Doctor代码诊断工具、查询抽象和多目录路由等创新进展。
- 📜 本期介绍虚拟滚动处理数十亿行数据、React Router加载器集成、微前端见解、Next.js AI增强以及构建稳健React组件的技巧。
- ❤️ 一个心形表情符号导致Web应用变慢的调试故事，React Native的最新改进，退出动画优化技巧，以及应对应用交互卡顿的方法。
- 🤖 AI在React调试中的能力，React新的ViewTransition元素，有效单元测试的见解，Copilot CLI ASCII横幅工程，以及避免过度使用useCallback的时机。
- 😅 useOptimistic钩子的复杂性，React Compiler在库更新中的问题，Turbopack的高效编译，新的开源React桥接工具，以及创新的组合模式。
- 🏆 Vercel的React最佳实践，2025年React生态系统演变，通过客户端组件和React过渡提升性能，以及TanStack表单的常见陷阱。
- 🕵️ 无需源码即可重现React组件，性能优化，使用新的useEffectEvent管理状态，以及React Conf 2025的最新演讲。
- 🤖 AI在React编码中的混合表现，Web开发30年演变，编写有效前端测试的技巧，React过渡和类型安全组件的见解。
- 🎉 2025年最佳React文章：涵盖设计模式、状态管理、重渲染和函数式编程。
- 🛡️ React近期漏洞的教训，React Server Components，性能优化，以及节日祝福。
- ⚙️ React 19.2的INP优化，TanStack Router见解，TanStack Start与Next.js对比，以及useEffectEvent的重要提示。
- ⚠️ React和Next.js的关键漏洞，设计系统最佳实践，React钩子改进，以及MDX文档的“复制为Markdown”功能。

---

### [隐私](https://reactdigest.net/privacy)

**原文标题**: [Privacy](https://reactdigest.net/privacy)

本隐私政策概述了React Digest如何收集、使用和保护您的个人信息，强调透明度和数据安全。

- 🔒 我们仅在收集信息前明确告知用途，并仅用于指定目的或法律要求。
- 📧 我们收集您的电子邮件地址仅用于发送新闻通讯，绝不用于其他目的或发送垃圾邮件。
- 🛡️ 我们通过合理的安全措施保护个人信息，防止丢失、盗窃或未经授权的访问。
- 👶 我们不收集13岁以下儿童的信息，若发现请立即联系我们。
- 📋 您有权根据英国《数据保护法》请求访问我们存储的您的所有信息。
- ❌ 如需删除数据，请发送邮件至指定地址，我们将按请求处理。
- 🚫 我们强烈反对垃圾邮件，您可随时通过邮件中的取消订阅链接退订。

---

### [媒体资料包 – 倭黑猩猩出版社](https://bonobopress.com/media-kit/)

**原文标题**: [Media Kit â Bonobo Press](https://bonobopress.com/media-kit/)

本媒体工具包介绍了Bonobo Press旗下四份面向技术人群的新闻通讯的广告合作详情，涵盖订阅数据、定价、广告格式及合作流程。

- 📊 **高参与度受众**：新闻通讯的打开率和点击率均高于行业基准，订阅者多为技术决策者，来自Google、Amazon等知名企业。
- 📧 **Leadership in Tech**：面向CTO、工程经理等领导层，订阅22,325人，打开率57.95%，每期赞助$2,235，预估点击365-585次。
- 💻 **Programming Digest**：面向软件工程师，订阅20,032人，打开率50.41%，每期赞助$985，CPC低至$2.00。
- 🖥️ **C# Digest**：专注.NET/C#开发者，订阅17,098人，打开率54.92%，点击率21.63%，每期赞助$1,220。
- 🌐 **React Digest**：面向React前端开发者，订阅20,075人，打开率54.06%，每期赞助$1,375，支持次级广告位。
- 📝 **纯文本广告格式**：仅支持文字内容，需提供链接、标题和描述，截止日期为发布前4天。
- 🚀 **合作流程**：从沟通需求、排期、付款锁定、素材交付到上线报告，建议提前数周联系。
- 🤝 **成功案例**：合作伙伴包括Okta、GitLab、Datadog、MongoDB等，常进行重复赞助。

---

