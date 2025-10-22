### [React文摘：电子邮件通讯](https://reactdigest.net/)

**原文标题**: [React Digest: Email Newsletter](https://reactdigest.net/)

这是一份面向React开发者的精选周报，提供高质量内容以节省学习时间

- 📧 每周为24,441+前端工程师推送精选文章
- ⏱️ 通过人工筛选文章和摘要帮助开发者节省内容搜寻时间
- 📖 每周持续学习React领域新知识
- 👍 读者反馈认可内容质量和实用性
- 🌍 受到全球前端工程师广泛阅读

---

### [序列化与反序列化：不破坏React的实践 | Ori Livni的笔记](https://www.orilivni.com/2025/10/serialization-and-deserialization/)

**原文标题**: [Serialization and deserialization without blowing React | Ori Livniâs Notes](https://www.orilivni.com/2025/10/serialization-and-deserialization/)

在React应用中处理序列化和反序列化数据时，直接使用JSON.parse/stringify可能导致性能问题。文章通过四个阶段逐步优化：从基础实现到按需订阅，再到单例数据源，最终通过结构共享技术解决重复渲染问题。

- 🔄 基础方案：在组件内直接使用JSON.parse解析数据，但多组件会导致重复解析和内存浪费
- 🗝️ 按需订阅：通过key值提取特定数据，但未解决重复解析和引用更新问题  
- 📦 单例数据源：全局维护反序列化数据，但非原始类型数据变更仍会触发不必要更新
- 🌳 结构共享：使用replaceEqualDeep深度对比新旧数据，保留未变更部分的引用，彻底解决重复渲染
- ⚡ 性能提升：结合按需订阅与结构共享，部分页面渲染时间减少达50%

---

### [开发者MCP认证指南——WorkOS篇](https://workos.com/blog/mcp-auth-developer-guide?utm_source=reactdigest&utm_medium=newsletter&utm_campaign=q32025)

**原文标题**: [A developerâs guide to MCP auth â WorkOS](https://workos.com/blog/mcp-auth-developer-guide?utm_source=reactdigest&utm_medium=newsletter&utm_campaign=q32025)

本文详细介绍了如何为MCP服务器配置安全的身份验证与授权系统，重点阐述了基于OAuth 2.1和PKCE的完整解决方案，涵盖服务发现、动态注册、令牌验证及权限控制等核心环节。

- 🔐 MCP通过OAuth 2.1实现认证授权，支持PKCE保护公共客户端，确保AI代理安全访问敏感系统
- 🌐 采用RFC 9728保护资源元数据和RFC 8414授权服务器元数据实现自动服务发现，消除手动配置
- 🤖 通过RFC 7591动态客户端注册实现自服务生态，支持新客户端自动注册授权服务器
- 🛡️ 基于JWT令牌验证机制，严格校验签名、有效期、发行方和受众等关键声明
- 👥 结合RBAC角色权限控制，将OAuth范围映射到具体操作权限，实现最小权限原则
- 🔄 提供WorkOS两种集成方案：自带用户体系的OAuth桥接模式或全托管的AuthKit方案
- 📋 实施路径从发布保护资源元数据开始，逐步完善令牌验证、角色映射和操作日志记录

---

### [使用React的useContext钩子与TypeScript告别属性钻取 | 作者：karan51ngh | Medium](https://karan51ngh.medium.com/stop-prop-drilling-the-ultimate-guide-to-reacts-usecontext-hook-with-typescript-6b98821870ee)

**原文标题**: [Stop Prop Drilling with React's useContext Hook & TypeScript | by karan51ngh | Medium](https://karan51ngh.medium.com/stop-prop-drilling-the-ultimate-guide-to-reacts-usecontext-hook-with-typescript-6b98821870ee)

本文介绍了如何使用React的useContext钩子结合TypeScript解决组件树深层传值问题，通过"创建-提供-消费"三步骤模式实现状态管理。

- 🎯 使用useContext可解决组件树深层传值问题，避免繁琐的属性传递
- 🔧 采用"创建-提供-消费"三步骤模式：创建Context、提供状态值、消费Context值
- 🌓 以主题切换为例演示具体实现，包含类型定义和状态管理
- 📶 通过Wi-Fi路由器的比喻解释Provider广播状态、Consumer接收状态的原理
- 🔐 扩展演示用户登录场景的应用，展示认证状态管理的完整实现
- 💡 useContext能集中管理状态逻辑，使嵌套组件直接访问共享数据，提升代码可维护性

---

### [如何在React Router中实现UI与数据库间FormData的转换 - sergiodxa](https://sergiodxa.com/tutorials/transform-formdata-between-ui-and-database-in-react-router)

**原文标题**: [How to Transform FormData Between UI and Database in React Router by sergiodxa](https://sergiodxa.com/tutorials/transform-formdata-between-ui-and-database-in-react-router)

本文介绍了在React Router应用中处理表单数据与数据库之间格式转换的最佳实践，通过三层架构实现关注点分离，确保代码的可维护性和可测试性。

- 🏗️ 采用三层架构：UI层负责渲染表单，HTTP层（actions/loaders）处理数据转换，数据层专注业务逻辑
- 🔄 Actions负责将FormData转换为数据库对象：解析表单字段、添加会话数据（如authorId）、处理文件上传
- 📥 Loaders将数据库数据转换为UI格式：编辑时预填充表单，如将标签数组转为逗号分隔字符串
- 🧩 处理复杂转换：同时处理文本字段和文件上传，构建完整数据传输对象
- 📝 创建专属校验模式：为每个action定义独立于数据库的Zod模式，仅验证实际接收字段
- 🛡️ 保持数据层独立性：数据函数仅处理业务规则和数据库操作，不涉及HTTP相关逻辑
- ⚡ 实现关注点分离：actions/loaders作为HTTP与业务逻辑间的转换器，提升代码可复用性

---

### [TanStack Router 中的上下文继承 | TkDodo 博客](https://tkdodo.eu/blog/context-inheritance-in-tan-stack-router)

**原文标题**: [Context Inheritance in TanStack Router | TkDodo's blog](https://tkdodo.eu/blog/context-inheritance-in-tan-stack-router)

TanStack Router 的上下文继承功能允许嵌套路由在类型安全的前提下，自动继承并合并父级路由的状态信息（包括路径参数、搜索参数和路由上下文），实现跨层级的类型传递与状态共享。

- 🧩 路径参数继承：子路由通过 `useParams()` 自动获取父路由解析后的参数类型，例如将字符串类型的 `dashboardId` 在父路由中定义为数字后，子路由会同步识别为数字类型
- 🔍 搜索参数合并：根路由定义的搜索参数（如 `debug` 布尔标志）可通过 `useSearch()` 在所有子路由中类型安全地访问，并支持通过中间件优化URL显示
- 🧳 路由上下文增强：通过 `beforeLoad` 在路由生命周期中扩展上下文对象（如添加 `{ hello: 'world' }`），子路由可通过 `useRouteContext()` 获取继承后的完整上下文
- 🌳 类型级联机制：所有父子路由间的状态继承均基于 TypeScript 类型推断，无需手动声明即可实现类型安全的深度状态合并
- ⚡ 适用多场景：该特性同时支持文件路由与代码路由，并可搭配标准校验库（如 ArkType）对参数进行类型校验与转换

---

### [错误](https://outbox.matthewphillips.info/archive/perils-of-reactivity)

**原文标题**: [Error](https://outbox.matthewphillips.info/archive/perils-of-reactivity)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='outbox.matthewphillips.info', port=443): Max retries exceeded with url: /archive/perils-of-reactivity (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [React Conf 2025 回顾（React 与 React Native 主题日）| Software Mansion](https://blog.swmansion.com/react-conf-2025-recap-922c50d97318?gi=e41caa19509c)

**原文标题**: [React Conf 2025  – Recap (React & React Native Days) | Software Mansion](https://blog.swmansion.com/react-conf-2025-recap-922c50d97318?gi=e41caa19509c)

React Conf 2025 总结了React生态的最新进展，涵盖React 19.1性能优化工具、React Compiler 1.0正式发布、React Foundation成立，以及React Native新架构全面启用、Hermes V1引擎性能提升等核心内容。

- 📈 React npm累计下载量突破60亿次，服务端组件获主流框架全面支持  
- 🔧 React 19.1新增错误追踪与数据预取优化，开发工具支持性能轨道可视化  
- 🎭 Activity组件实现UI隐藏时状态保持，ViewTransition封装原生动画API  
- 🚀 React Compiler 1.0实现自动记忆化，Meta实测交互性能提升2.5倍  
- 🤝 React Foundation由Meta、微软等七家机构联合成立  
- 📱 React Native周下载量同比增长100%，新架构成为唯一选项  
- ⚡ Hermes V1引擎性能提升60%，实验版已随RN 0.82发布  
- 🌐 React Strict DOM推动原生与Web生态对齐，共享代码能力增强  
- 🛠️ 开发工具链全面升级，支持网络监控、性能追踪和桌面端调试  
- 🏆 多家企业展示RN应用成果，Shopify迁移新架构后启动速度提升10%

---

### [渐进式图像渲染的现状与未来潜力 - JakeArchibald.com](https://jakearchibald.com/2025/present-and-future-of-progressive-image-rendering/)

**原文标题**: [The present and potential future of progressive image rendering - JakeArchibald.com](https://jakearchibald.com/2025/present-and-future-of-progressive-image-rendering/)

本文探讨了渐进式图像渲染的现状与未来发展，重点分析了不同图像格式在浏览器中的表现及技术潜力。

- 🦊 渐进式渲染允许在部分图像数据加载时显示初步画面，但实际体验受网络波动影响较大
- 🖼️ JPEG格式支持渐进渲染且文件质量无损失，但解码时间增加40%（约1.3毫秒）
- 🎨 PNG的交错模式会显著增大文件体积，不推荐使用
- 🌐 WebP在Firefox/Chrome中支持渐进渲染，但Safari需完整加载后才显示
- 🔬 AVIF通过实验性分层编码实现两阶段渲染（5.8kB预览+完整图像），仅Chromium浏览器支持
- ⚡ JPEG XL虽被寄予厚望，但Safari不支持渐进渲染，且解码速度比AVIF慢150%
- 📊 测试显示155kB的图像在飞机WiFi等不稳定网络中，数据往往呈突发式传输而非平稳渐进
- 💡 作者提出AVIF改进方案：在文件头部嵌入独立预览图（可配置模糊效果），实现零解码开销
- 🚫 研究否定了“用渐进渲染替代响应式图片”的方案，因网络延迟会导致多余数据传输
- 🔮 JPEG XL通过progressive_dc参数可实现多阶段渲染（6kB即可识别主体），但浏览器支持仍待完善

---

### [CSS :is() :where() 魔法发生之处 · 马蒂亚斯·奥特](https://matthiasott.com/notes/css-is-where-the-magic-happens)

**原文标题**: [ CSS :is() :where() the Magic Happens · Matthias Ott](https://matthiasott.com/notes/css-is-where-the-magic-happens)

CSS伪类函数:is()和:where()是现代CSS中功能强大但使用率较低的两个选择器，它们能简化代码结构并提升样式表的灵活性。

- 🪄 简化选择器语法，将冗长的选择器列表合并为简洁表达式
- 🛡️ 具备容错机制，单个选择器失效不会影响整个规则集
- ⚖️ :is()继承参数中最具体选择器的优先级，:where()始终保持零优先级
- 🎯 常用于组件样式重置，确保基础样式易于覆盖
- 🔗 可与:has()等选择器组合实现复杂条件样式
- 📊 实际使用率仅45%，仍有较大推广空间
- 💡 特别适合创建可扩展的CSS架构和设计系统

---

### [CSS中的新progress()函数——Amit Merchant——关于PHP、JavaScript等技术的博客](https://www.amitmerchant.com/the-progress-function-css/)

**原文标题**: [The new progress() function in CSS — Amit Merchant — A blog on PHP, JavaScript, and more](https://www.amitmerchant.com/the-progress-function-css/)

CSS新增的progress()函数能够根据视口宽度在最小和最大尺寸之间的变化程度，直接映射到透明度等属性上，实现响应式效果。

- 📐 函数定义：progress(当前值, 起始值, 结束值)返回0-1之间的归一化数值
- 🎯 核心优势：无需复杂calc()表达式或JavaScript即可实现跨单位数值映射
- 🖼️ 应用场景：视口尺寸关联的透明度调节、组件缩放、间距调整等响应式效果
- ⚡ 实际用例：图片在大屏完全显示，小屏渐变为半透明；卡片随视口增大轻微缩放
- 🌊 特殊功能：支持px/rem/vw等混合单位计算，实现平滑插值效果
- 🎮 技术类比：类似游戏引擎中的smoothstep()函数，用于数值平滑过渡
- 🚀 浏览器支持：目前Chromium和Safari 26已支持，Firefox暂未实现
- 💡 兼容方案：可通过clamp()和calc()组合实现类似效果作为降级方案

---

### [CSS Grid：一种实用的思维模型与网格线的强大功能 | WebKit](https://webkit.org/blog/17474/css-grid-a-helpful-mental-model-and-the-power-of-grid-lines/)

**原文标题**: [  CSS Grid: A helpful mental model and the power of grid lines | WebKit](https://webkit.org/blog/17474/css-grid-a-helpful-mental-model-and-the-power-of-grid-lines/)

CSS Grid 是一种强大的布局工具，通过网格线实现复杂设计。文章提出将网格视为电子表格的思维模型，强调先定义容器结构再放置元素，并详细介绍了网格线编号定位、跨行跨列操作及三种关键属性。

- 📊 将网格布局类比电子表格，先定义容器模板再填充内容
- 📐 使用 `grid-template-columns/rows` 设置行列结构，`fr` 单位实现弹性分割
- 🧭 通过网格线编号精确定位元素，如 `grid-row: 1/3` 实现跨行布局
- 🔄 默认流式布局与显式定位结合，优先处理显式定位元素
- 📏 掌握轨道（tracks）、网格区域（grid areas）等核心术语
- 🛠️ 使用 `grid-auto-rows/columns` 处理动态添加的未规划内容
- 🎯 网格线定位法比行列定位更灵活，为后续网格区域教学铺垫

---

### [错误](https://denodell.com/blog/html-best-kept-secret-output-tag)

**原文标题**: [Error](https://denodell.com/blog/html-best-kept-secret-output-tag)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='denodell.com', port=443): Max retries exceeded with url: /blog/html-best-kept-secret-output-tag (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [为什么 typeof null === object | Piotr Zarycki - 编程博客](https://pzarycki.com/en/posts/js-null/)

**原文标题**: [Why typeof null === object | Piotr Zarycki - Programming Blog](https://pzarycki.com/en/posts/js-null/)

JavaScript中`typeof null`返回`"object"`是源于1995年 Netscape 浏览器原始实现的类型标记机制缺陷。在32位系统中，对象指针的低3位标记为`000`，而`null`值表示为全零的指针地址`0x00000000`，导致类型检测宏错误地将`null`识别为对象类型。尽管存在简单的修复方案，但为保持与数十亿行现有代码的兼容性，ECMAScript标准委员会决定保留这一历史行为。

- 🏗️ JavaScript 原始实现采用32位类型标记机制，对象类型标记为低3位`000`
- 🕳️ `null`值被表示为全零指针`0x00000000`，与对象类型标记相同
- 🔍 类型检测宏`JSVAL_IS_OBJECT`无法区分真实对象和`null`值
- ⚠️ 1995年 Netscape Navigator 1.3 的`typeof`实现未使用现有的`JSVAL_IS_NULL`检测
- 🔧 2013年修复提案因破坏向后兼容性被ECMAScript标准委员会拒绝
- 💡 正确检测对象应使用：`value !== null && typeof value === 'object'`
- 📜 该行为成为JavaScript语言发展历程中的历史见证

---

### [如何在JavaScript中不使用reduce()对数组进行分组 - Matt Smith](https://allthingssmitty.com/2025/10/06/grouping-arrays-in-modern-javascript-object-groupby-and-map-groupby/)

**原文标题**: [
    How to group arrays in JavaScript without reduce() - Matt Smith
  ](https://allthingssmitty.com/2025/10/06/grouping-arrays-in-modern-javascript-object-groupby-and-map-groupby/)

ES2024引入了Object.groupBy()和Map.groupBy()方法，使JavaScript数组分组操作更简洁直观，无需再依赖复杂的reduce()方法。

- 📚 ES2024新增Object.groupBy()和Map.groupBy()静态方法，支持通过回调函数对数组元素进行分组
- 🍎 Object.groupBy()返回普通对象，键名为字符串，适用于需要JSON序列化的场景
- 🗺️ Map.groupBy()返回Map对象，支持非字符串键名并保持插入顺序
- ⚡ 相比传统reduce()方法，新语法减少模板代码，提升可读性和表达性
- 📊 典型应用场景包括：按状态分组任务、按价格区间分类产品、按级别整理日志
- ⚠️ 注意事项：Object.groupBy()会强制转换键为字符串，Map.groupBy()结果不可JSON序列化
- 🌐 主流现代浏览器和Node.js 21+均已支持，旧环境可通过polyfill实现兼容
- 📋 选择建议：需要字符串键或JSON输出时选Object.groupBy，需要非字符串键或保持顺序时选Map.groupBy

---

### [使用useSyncExternalStore进行并发水合 | Jacob 'Kurt' Groß](https://kurtextrem.de/posts/react-uses-hydration)

**原文标题**: [Concurrent Hydration with useSyncExternalStore | Jacob 'Kurt' Groß](https://kurtextrem.de/posts/react-uses-hydration)

本文探讨了在React服务端渲染中使用Suspense时如何通过改进useSyncExternalStore实现并发水合，避免水合不匹配问题并提升用户体验。

- 🚧 传统useSyncExternalStore会导致同步阻塞渲染，引发Suspense边界闪烁和 hydration 错误
- ⚡ 结合useDeferredValue可将useSyncExternalStore返回值转为并发模式，避免阻塞主线程
- 🎯 通过useMemo正确缓存组件，确保在并发渲染期间才返回新的子元素
- 📈 这种模式能显著改善INP指标，让React调度器能优先处理用户交互
- 🔧 已在Framer生产环境验证并获得React团队认可，未来并发存储将原生支持此特性

---

### [编程文摘：邮件通讯](https://programmingdigest.net/?utm_source=web-archive&utm_campaign=react)

**原文标题**: [Programming Digest: Email Newsletter](https://programmingdigest.net/?utm_source=web-archive&utm_campaign=react)

《编程文摘》是一份专为软件工程师精心挑选的每周通讯，汇集优质内容帮助读者高效学习新知。

- 📧 超过22,398名工程师订阅的每周邮件
- 🔍 含精选文章与摘要，节省筛选时间
- 🌱 每周持续学习新知识
- 💬 读者反馈认可内容精准实用（如API设计专题）
- 🏢 由Bonobo Press自2013年持续运营

---

### [科技领导力：电子邮件通讯](https://leadershipintech.com/?utm_source=web-archive&utm_campaign=react)

**原文标题**: [Leadership in Tech: Email Newsletter](https://leadershipintech.com/?utm_source=web-archive&utm_campaign=react)

该科技领导力周刊为技术管理者提供精选内容，帮助提升领导能力

- 📧 面向CTO、工程经理和高级工程师的每周邮件订阅服务
- 👥 已吸引27,906名工程领导者加入社群
- 📖 每周推送带摘要的精选文章
- ⏱️ 为用户节省内容筛选时间
- 🌱 每周持续学习新知识
- ❤️ 用户反馈认可其领导力建设内容和架构讨论价值
- 🤝 特别强调沟通与授权等关键管理技能
- 🌍 受到全球科技行业领导者的广泛阅读

---

### [错误](https://csharpdigest.net/?utm_source=web-archive&utm_campaign=react)

**原文标题**: [Error](https://csharpdigest.net/?utm_source=web-archive&utm_campaign=react)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='csharpdigest.net', port=443): Max retries exceeded with url: /?utm_source=web-archive&utm_campaign=react (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [让开发者与时俱进——Bonobo出版社](https://bonobopress.com/)

**原文标题**: [Keeping developers up to date â Bonobo Press](https://bonobopress.com/)

Bonobo Press 是一家面向技术专业人士的媒体公司，通过新闻通讯服务连接开发者群体并提供广告合作机会。

- 📧 自2013年起为超过93,000名软件开发者和IT从业者提供行业资讯
- 🗞️ 每周为工程师、技术主管等群体提供简洁高效的精选资讯
- 📢 提供精准广告服务，触达技术决策者与工程师群体
- 👥 支持广告合作、媒体资料获取与业务咨询等联系方式

---

### [错误](https://reactdigest.net/newsletters)

**原文标题**: [Error](https://reactdigest.net/newsletters)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='reactdigest.net', port=443): Max retries exceeded with url: /newsletters (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [隐私](https://reactdigest.net/privacy)

**原文标题**: [Privacy](https://reactdigest.net/privacy)

本隐私政策概述了React Digest如何通过合法透明的方式收集、使用和保护用户个人信息，重点说明仅收集邮箱用于发送周刊，并提供用户数据查询与删除的完整渠道。

- 🎯 明确说明收集个人信息前会告知使用目的
- 📧 仅收集邮箱地址用于发送周刊邮件
- 🛡️ 采用合理安全措施保护个人信息免遭泄露
- ⏱️ 仅在实现目的所需期限内保留个人信息
- 📋 承诺个人信息需保持准确完整且及时更新
- 🚫 严格禁止收集13岁以下儿童个人信息
- 📬 用户可邮件联系查询个人数据（[email protected]）
- 🗑️ 支持通过指定邮箱申请数据删除（[email protected]）
- 📮 每封邮件包含退订链接，反对任何垃圾邮件行为
- 🌐 定期公开个人信息管理政策与实践细则

---

### [媒体资料包——Bonobo出版社](https://bonobopress.com/media-kit/)

**原文标题**: [Media Kit â Bonobo Press](https://bonobopress.com/media-kit/)

Bonobo Press为技术领域专业人士提供精准的新闻通讯广告服务，通过四大专业通讯覆盖开发者、技术主管等群体，以高互动率和精准受众定位帮助广告商获取潜在客户与转化。

- 📧《技术领导力》通讯：面向技术管理者，订阅量27,818，开信率57.95%，单期赞助$2,235，受众多为欧美企业的CTO及工程总监
- 💻《编程文摘》通讯：服务全栈开发者，订阅量21,632，点击率14.83%，赞助成本$985，覆盖从初级到管理层的技术人员
- ⚙️《C#文摘》通讯：专注.NET开发者，订阅量19,856，点击率高达21.63%，单期$1,220，受众多就职于金融、医疗等大型企业
- 🌐《React文摘》通讯：针对前端工程师，订阅量23,831，开信率54.06%，赞助费$1,375，适合推广Web开发相关产品
- 📋 广告格式：纯文本嵌入式广告，需包含链接、标题（<100字符）及描述（<400字符），提前4天提交素材
- 🚀 合作流程：需求沟通→排期确认→付款锁定→素材优化→效果追踪，支持重复赞助
- 🌍 受众优势：欧美用户占比超70%，合作过Okta、MongoDB等知名科技企业

---

