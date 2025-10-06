### [React文摘：电子邮件通讯](https://reactdigest.net/)

**原文标题**: [React Digest: Email Newsletter](https://reactdigest.net/)

这是一份为React开发者精心筛选的每周通讯，帮助工程师节省时间获取前端领域精选内容

- 📧 每周邮件推送，已服务23,824名前端工程师
- 🎯 精选文章配摘要，节省寻找优质内容的时间
- 📖 每周学习新知识，持续更新技术认知
- 👍 用户好评：内容实用、文笔优秀、紧跟技术演进
- 🌟 特别提及关于React并发模式的文章收获颇丰
- 🏢 由Bonobo Press发行，被多家知名科技公司工程师订阅

---

### [React 渲染行为与子组件关联的微妙之处](https://blacksheepcode.com/posts/nuance_of_react_rendering_behaviour)

**原文标题**: [The nuance of React rendering behaviour as it relates to children](https://blacksheepcode.com/posts/nuance_of_react_rendering_behaviour)

本文探讨了React组件中直接渲染子组件与通过props.children传递子组件时渲染行为的差异，并通过代码示例和React 19编译器特性说明了优化方案。

- 🔍 直接声明的子组件会在父组件状态更新时重新渲染，而通过props.children传递的则不会
- 🌳 React官方文档未区分这两种子组件渲染方式，但实际渲染行为存在差异
- ⚙️ JSX编译后，直接渲染的子组件每次都会生成新的React元素对象，而props.children传递的会保持相同引用
- 🔄 React通过浅比较(===)判断是否需要重新渲染子树，引用相同则跳过渲染
- 🚀 React 19编译器通过"use memo"注解可自动优化组件，消除不必要的重新渲染
- 💡 理解这种渲染差异有助于编写更高性能的React应用

---

### [将智能代理AI引入您的IGA | Lumos](https://www.lumos.com/events-page/agentic-ai-for-iga?utm_source=paved&utm_campaign=paved&utm_medium=newsletter&utm_term=reactdigest)

**原文标题**: [Bring Agentic AI to your IGA | Lumos](https://www.lumos.com/events-page/agentic-ai-for-iga?utm_source=paved&utm_campaign=paved&utm_medium=newsletter&utm_term=reactdigest)

本网络研讨会介绍了Lumos公司如何将智能体AI技术融入身份治理管理（IGA）领域，展示其AI原生自治平台及行业首个身份智能体Albus的应用。

- 🤖 演示AI原生自治平台，支持自然语言处理及全流程访问策略管理
- 🚫 解析传统AI封装方案的局限性，强调具备学习能力的可信智能体框架
- 🏗️ 提供灵活架构选择，兼容现有IGA系统与AI优先方案
- 📊 分享实施路线图与量化指标，实现人机协同的规模化部署
- 🔒 阐述AI安全信任体系，涵盖模型选择、数据保护与审计追溯
- 👨💼 由Lumos首席执行官与现场技术总监联袂主讲
- 🎯 提供实时演示注册通道，支持定制化产品体验

---

### [快速了解useEffectEvent | Nico的博客](https://www.nico.fyi/blog/quick-look-use-effect-event)

**原文标题**: [Quick look into the useEffectEvent | Nico's Blog](https://www.nico.fyi/blog/quick-look-use-effect-event)

React 19.2版本引入了useEffectEvent钩子，用于从Effect中提取非响应式逻辑，创建能始终访问最新状态但不会触发Effect重新运行的函数。

- 🔄 useEffectEvent能创建始终读取最新状态值的"不稳定"函数
- ⚡ 使用该钩子的函数不会导致包含它的Effect因依赖变化而重新执行
- 🚫 通过ESLint规则自动排除依赖项，无需手动声明函数依赖
- 🐛 解决了传统方法中函数闭包捕获旧状态值的问题
- 💡 适用于需要在Effect中访问最新状态但不希望触发重运行的场景
- 📝 通过包装函数创建Effect Event，确保始终使用最新值

---

### [如何使用React Router构建主从用户界面 - sergiodxa](https://sergiodxa.com/tutorials/build-a-master-detail-ui-with-react-router)

**原文标题**: [How to Build a Master-Detail UI with React Router by sergiodxa](https://sergiodxa.com/tutorials/build-a-master-detail-ui-with-react-router)

本文介绍了如何使用React Router构建主从界面，通过智能路由配置和上下文管理实现不同访问场景下的自适应布局。

- 🛣️ 创建双重路由结构：通过`/inbox/:issue`和`/:issue`两种路径访问相同内容，分别对应浏览模式和直接访问模式
- 🎯 使用上下文追踪布局状态：通过InboxContext区分组件是否在收件箱布局内渲染
- 📱 构建主从布局：收件箱路由采用两栏布局，左侧显示问题列表，右侧通过Outlet展示详情
- 🔄 实现智能重定向：基于Sec-Fetch-Dest请求头判断访问方式，直接访问时重定向到独立详情页
- 📋 添加空状态处理：当未选择问题时显示提示信息
- 🏠 设置根路径重定向：将根路径自动重定向到收件箱页面
- 🎪 保持用户体验一致性：客户端导航保持上下文，直接访问显示专注视图，确保URL可共享和可收藏

---

### [活动，React新组件——Agence Premier Octet](https://www.premieroctet.com/blog/en/activity-new-react-component)

**原文标题**: [Activity, the new React component - Agence Premier Octet](https://www.premieroctet.com/blog/en/activity-new-react-component)

React新推出的Activity组件能够简化条件渲染逻辑，在隐藏组件时自动保留状态并暂停副作用执行，特别适用于多步骤表单等需要保持状态的交互场景。

- 🚀 **组件特性**：通过`display: none`隐藏DOM节点，保持React状态完整，仅在可见时执行副作用
- ⚡ **使用场景**：解决多步骤表单中传统条件渲染导致的状态丢失问题
- 🛠️ **实现方式**：通过`<Activity mode="visible/hidden">`包裹组件，替代`&&`操作符或手动样式控制
- 📊 **效果管理**：被隐藏组件的`useEffect`和`useLayoutEffect`会自动暂停执行
- 🔄 **数据预加载**：配合`use`钩子可在组件实例化时立即触发异步数据请求
- 🎯 **优势对比**：比手动管理激活状态更简洁，避免组件重复挂载/卸载的复杂性

---

### [React Hooks 解密：深入理解 “useState” 机制 | Edaqa Mortoray 著 | 不可数工程 | 2025年9月 | Medium](https://medium.com/uncountable-engineering/react-hooks-demystified-the-mechanics-of-usestate-12ce9b925bbf)

**原文标题**: [React Hooks Demystified: The mechanics of “useState” | by Edaqa Mortoray | Uncountable Engineering | Sep, 2025 | Medium](https://medium.com/uncountable-engineering/react-hooks-demystified-the-mechanics-of-usestate-12ce9b925bbf)

React的useState钩子通过组件实例和状态索引机制实现状态持久化，其本质遵循JavaScript执行规则而非魔法。

- 🧠 useState依赖组件实例存储状态值，通过全局变量跟踪当前渲染实例
- 🔢 使用自增索引标记状态声明顺序，因此钩子不能条件调用
- 🎭 仅在首次渲染时使用初始值，后续更新通过setter函数触发重渲染
- 🧩 setter函数通过闭包锁定组件实例，确保更新目标正确
- ⚡ 状态更新标记组件为脏组件，触发协调重渲染流程
- 🌳 渲染结果与状态值解耦，每次渲染都使用当前状态快照
- 🔄 稳定的setter函数对性能优化至关重要
- ⚠️ 初始值仅使用一次的特性可能导致隐蔽的边界情况错误

---

### [你对媒体查询真正了解多少？——前端大师博客](https://frontendmasters.com/blog/learn-media-queries/)

**原文标题**: [How much do you really know about media queries? – Frontend Masters Blog](https://frontendmasters.com/blog/learn-media-queries/)

本文探讨了CSS媒体查询的多样性和深度应用，指出除了常见的响应式设计查询外，还有许多针对设备能力、用户偏好和可访问性的媒体查询描述符，并介绍了新的语法和嵌套功能。

- 🖱️ 通过组合 `hover`、`pointer`、`any-hover` 和 `any-pointer` 查询设备输入能力，可针对触摸屏、鼠标、操纵杆等不同输入机制优化交互体验
- 🎨 使用 `forced-colors` 媒体查询适配操作系统强制色彩模式，并通过 `forced-color-adjust: none` 保留特定颜色
- 📐 `width` 和 `height` 支持新的比较运算符语法（如 `width > 900px`），提供更精确的视口范围匹配
- 🔄 `inverted-colors` 可检测颜色反转模式，通过调整HSL色相值（h+180）还原阴影和媒体元素的视觉效果
- 📱 `orientation` 结合触摸设备描述符可针对横竖屏优化布局，但需避免用于设备类型检测
- 📜 `overflow-inline` 和 `overflow-block` 检测滚动支持，特别适用于分页媒体（如打印文档）的样式优化
- 🌙 `prefers-color-scheme` 配合CSS的 `light-dark()` 函数可实现明暗模式切换，提升用户体验
- ♿ `prefers-contrast`、`prefers-reduced-motion` 等偏好系列媒体查询遵循WCAG指南，为不同需求用户提供可访问性支持
- 🖼️ `resolution` 媒体查询可基于设备分辨率条件加载不同尺寸图像，优化显示效果
- 🔗 CSS原生嵌套支持媒体查询嵌套编写，提升代码组织性和可维护性

---

### [使用CSS为兄弟元素设置样式从未如此简单。尝试sibling-count和sibling-index | utilitybend](https://utilitybend.com/blog/styling-siblings-with-CSS-has-never-been-easier.-Experimenting-with-sibling-count-and-sibling-index/)

**原文标题**: [Styling siblings with CSS has never been easier. Experimenting with sibling-count and sibling-index | utilitybend](https://utilitybend.com/blog/styling-siblings-with-CSS-has-never-been-easier.-Experimenting-with-sibling-count-and-sibling-index/)

CSS的sibling-index()和sibling-count()函数为元素样式控制带来革新，通过动态计算兄弟元素位置和数量实现复杂布局效果。

- 🎬 使用sibling-index()创建交错动画，无需手动设置延迟时间
- 🌈 结合sibling-count()实现动态色彩光谱，自动计算色相分布
- ⭕ 通过三角函数和CSS函数实现圆形布局定位
- 🃏 利用兄弟元素索引创建对称的卡牌扇形展开效果
- 📊 额外实验包含条件判断的柱状图和3D彩虹框架演示

这些功能简化了传统需要JavaScript计算的复杂样式场景，使CSS具备更强的动态布局能力。

---

### [Coyier CSS入门指南 - Piccalilli版](https://piccalil.li/links/the-coyier-css-starter/)

**原文标题**: [
  The Coyier CSS starter - Piccalilli
](https://piccalil.li/links/the-coyier-css-starter/)

这是一篇对Chris Coyier的CSS入门模板的评论文章，作者Andy Bell在肯定其整体价值的同时，针对具体代码实现提出了个人见解和建议。

- 🎯 文章强调CSS入门模板应作为基础参考，开发者需根据实际需求调整使用
- ⚠️ 提醒谨慎使用@layer功能，需确保团队全面掌握其特性以避免潜在问题
- 📱 赞赏根元素字体大小采用clamp()实现响应式排版，但建议分离字体属性增强可读性
- 🚫 质疑在body元素设置全局内边距的做法，认为可能影响全宽元素布局
- 💝 特别推崇标点悬挂(hanging-punctuation)和智能断词(word-break)等细节处理
- 🎨 指出字体粗细和字间距设置需考虑字体家族特性，避免通用化配置
- 📐 认可使用ch单位定义列表缩进，但提醒注意嵌套列表的显示效果
- 🔧 肯定表单元素的继承字体设置和文本域自适应高度等实用样式
- 📊 建议表格字体尺寸采用相对单位(rem/em)保持整体一致性
- 🚫 对默认启用视图过渡动画持保留态度，但肯定平滑滚动行为的实用性

---

### [您的图片（可能）尺寸过大](https://reasonunderpressure.com/blog/posts/your-images-are-probably-oversized)

**原文标题**: [Your Images Are (Probably) Oversized](https://reasonunderpressure.com/blog/posts/your-images-are-probably-oversized)

概述：文章指出网页图片普遍存在尺寸过大的问题，即使使用NextJS的Image组件，若未正确设置sizes属性，仍会导致用户下载超出实际显示需求的图片，造成资源浪费。

- 🖼️ 网页图片常因未设置sizes属性而超出实际显示尺寸
- 📱 图片渲染尺寸直接受用户设备屏幕大小影响
- 💾 高分辨率原图在普通屏幕上会造成带宽与计算资源浪费
- ⚠️ NextJS Image组件需配合width/height参数才能实现基础响应式
- 🔍 实测显示425px视窗仍会加载3600px原图
- 📐 设计师提供3600x2400图片仅适合极少数大屏设备
- 🚫 盲目使用priority属性可能加剧资源消耗问题
- 💡 需通过sizes属性实现真正的按需加载优化

---

### [最佳CSS单位或许是一种组合 | OddBird](https://www.oddbird.net/2025/09/23/type-units/)

**原文标题**: [The Best CSS Unit Might Be a Combination | OddBird](https://www.oddbird.net/2025/09/23/type-units/)

CSS最佳单位可能是多种单位的组合，无需在px和rem之间做单一选择，可通过现代CSS函数实现灵活响应式设计

- 🎯 结合px与rem单位，使用max()/clamp()/calc()函数实现字体大小协商
- 📐 根据设计意图选择单位：em用于局部上下文适配，rem用于全局一致性
- 📏 间距处理采用lh（行高）单位保持文本节奏，结合vi单位响应可用空间
- 🧩 通过组合不同单位精确表达设计语义，如min(1lh, 2vi)实现智能间距
- 🎨 采用"诗意CSS架构"理念，善用整个CSS语言体系而非寻找"最佳单位"

---

### [从If-Else地狱到使用函数注册表模式的整洁架构](https://techhub.iodigital.com/articles/function-registry-pattern-react)

**原文标题**: [From If-Else Hell to Clean Architecture with Function Registry Pattern](https://techhub.iodigital.com/articles/function-registry-pattern-react)

本文介绍了如何使用函数注册表模式替代复杂的if-else条件判断，实现清晰可扩展的数据转换架构。

- 🚫 传统if-else代码块存在维护困难、测试复杂和违反SOLID原则等问题
- 🔧 通过类型守卫和提取转换函数进行初步优化，但仍存在扩展性问题
- 🎯 函数注册表模式通过注册机制自动匹配转换器，实现智能分发
- 📁 采用模块化文件结构：注册表、类型定义和独立转换器文件
- 🔄 支持递归转换，对象转换器可调用注册表处理嵌套属性
- 🧪 每个转换器可独立测试，提高了代码的可测试性
- 📦 提供单一导出接口，封装内部复杂性，使用简单
- ⚡ 按优先级注册转换器，采用首次匹配策略提升性能
- 🎨 适用于表单生成器等需要处理多种数据类型的复杂场景

---

### [无](https://blog.dochia.dev/blog/json-isnt-json/)

**原文标题**: [None](https://blog.dochia.dev/blog/json-isnt-json/)

JSON虽然作为通用数据交换格式被广泛采用，但在不同编程语言和库的实现中存在诸多细微差异，可能导致数据精度丢失、编码混乱和解析错误等问题。

- 🔢 **数字精度问题**：JavaScript对超过2^53-1的整数会丢失精度，而Python和Java能正确处理大整数
- 🌐 **字符串编码差异**：Unicode字符在不同语言中的规范化处理不一致，可能导致看似相同的字符串比较失败
- 🔑 **对象键顺序**：JSON规范不保证键顺序，但Go默认按字母排序，而JavaScript和Python保留插入顺序
- ❓ **空值处理**：不同语言对null、undefined和缺失属性的处理方式各不相同
- ⏰ **日期时间格式**：JSON无原生日期类型，导致ISO字符串、Unix时间戳等多种格式混用
- 🚨 **错误处理不一致**：不同解析器对尾随逗号、重复键、前导零等问题的处理策略不同
- 💸 **金融计算风险**：浮点数精度问题可能导致金额计算错误，需使用Decimal类型
- 🔐 **加密操作隐患**：键顺序不一致会破坏HMAC签名等加密操作的可靠性
- 🛡️ **解决方案**：通过模式验证、数据规范化、选择合适的库和跨语言测试来确保兼容性

---

### [停止使用.reverse().find()：认识findLast() - 马特·史密斯](https://allthingssmitty.com/2025/09/22/stop-using-reverse-find-meet-findlast/)

**原文标题**: [
    Stop using .reverse().find(): meet findLast() - Matt Smith
  ](https://allthingssmitty.com/2025/09/22/stop-using-reverse-find-meet-findlast/)

ES2023新增的findLast()和findLastIndex()方法可直接从数组末尾搜索元素，无需反转数组，提供更简洁高效的解决方案。

- 🔄 传统方法需使用.slice().reverse().find()组合，存在效率低和易出错问题
- 🎯 findLast()从数组末尾向前搜索，返回第一个满足条件的元素
- 📍 findLastIndex()返回匹配元素的索引位置
- 💡 适用于聊天记录、操作日志、表单验证等需要查找最后匹配项的场景
- ⚠️ 跳过稀疏数组空位但不跳过undefined值
- 🚫 不改变原数组，比reverse()更安全
- 📱 支持现代浏览器和Node.js 18.12+版本
- 🔧 旧环境可通过core-js polyfill实现兼容

---

### [GitHub - bodadotsh/npm-security-best-practices: 如何防范NPM供应链攻击确保安全](https://github.com/bodadotsh/npm-security-best-practices)

**原文标题**: [GitHub - bodadotsh/npm-security-best-practices: How to stay safe from NPM supply chain attacks](https://github.com/bodadotsh/npm-security-best-practices)

该资源库汇总了保护NPM生态系统免受供应链攻击、恶意软件和钓鱼等威胁的安全实践，涵盖npm、yarn、pnpm、deno和bun等工具。

- 🔒 **锁定依赖版本**：使用`--save-exact`或配置`save-exact=true`固定依赖版本，通过override/resolution字段覆盖传递依赖
- 📁 **提交锁文件**：将package-lock.json等锁文件纳入版本控制，在CI环境中使用`npm ci --frozen-lockfile`确保一致性
- ⚠️ **禁用生命周期脚本**：配置`ignore-scripts=true`防止恶意脚本在安装阶段执行
- ⏰ **设置发布冷却期**：通过`minimumReleaseAge`等配置避免安装刚发布的新包，降低风险
- 🛡️ **使用权限模型**：Node.js的`--permission`标志和Deno默认权限机制限制资源访问
- 📦 **减少外部依赖**：优先使用Node.js/bun/deno内置模块替代第三方库，降低攻击面
- 🔐 **启用双因素认证**：为npm账户配置2FA，推荐使用WebAuthn安全密钥
- 🔑 **创建受限令牌**：使用粒度访问令牌，设置过期时间、IP限制和最小权限
- 📋 **生成来源证明**：通过`--provenance`标志或CI/CD集成建立包构建可信链
- 📄 **审查发布文件**：利用package.json的files字段和`.npmignore`控制发布内容
- 👥 **组织安全管理**：在npm组织中强制2FA，按包分配团队权限
- 🌐 **备选注册表**：考虑JSR注册表或搭建私有注册表（Verdaccio等）增强控制
- 🔍 **安全审计监控**：使用`npm audit`、Socket.dev、Snyk等工具扫描漏洞和恶意包
- 💝 **支持开源维护**：通过GitHub Sponsors等平台资助开源项目，缓解维护者倦怠问题

---

### [2025年React状态管理：你真正需要掌握的核心要点](https://www.developerway.com/posts/react-state-management-2025)

**原文标题**: [React State Management in 2025: What You Actually Need](https://www.developerway.com/posts/react-state-management-2025)

本文探讨了2025年React状态管理的实际需求，指出大多数情况下并不需要专门的状态管理库，并针对不同状态类型推荐了相应解决方案。

- 🎯 远程状态处理推荐使用TanStack Query或SWR等数据获取库，它们能完善处理缓存、去重、重试等问题
- 🌐 URL状态管理建议使用nuqs库，可轻松实现查询参数与本地状态同步
- 🏠 本地状态直接使用React内置的useState或useReducer即可
- 🔗 共享状态可先尝试属性传递或Context，仅在复杂场景下考虑状态管理库
- ⚡ 推荐Zustand作为共享状态解决方案，因其简单易用且符合React开发模式
- 📊 强调应根据具体需求选择工具，没有"最佳"的通用解决方案

---

### [编程文摘：邮件通讯](https://programmingdigest.net/?utm_source=web-archive&utm_campaign=react)

**原文标题**: [Programming Digest: Email Newsletter](https://programmingdigest.net/?utm_source=web-archive&utm_campaign=react)

《编程文摘》是一份专为软件工程师精心筛选的每周电子报，汇集优质技术内容帮助读者高效学习

- 📧 超过21,510名软件工程师订阅的每周邮件推送
- 🎯 每期精选附带简短摘要的技术文章
- ⏱️ 帮助工程师节省筛选有价值内容的时间
- 🌱 每周持续学习新技术知识与行业动态
- 💬 读者反馈认可其内容精准度和实用价值
- 🌍 受到全球多家知名科技企业工程师的广泛阅读

---

### [科技领导力：电子邮件通讯](https://leadershipintech.com/?utm_source=web-archive&utm_campaign=react)

**原文标题**: [Leadership in Tech: Email Newsletter](https://leadershipintech.com/?utm_source=web-archive&utm_campaign=react)

这是一份面向技术领导者的精选周报，旨在帮助CTO、工程经理和高级工程师提升领导力

- 📧 拥有27,796+工程领导者订阅的每周邮件推送
- 📖 精选文章配简短摘要，节省寻找优质内容的时间
- 🎯 每周学习新知识，重点涵盖领导力建设与架构讨论
- 💬 特别关注沟通技巧和委派能力等关键领导技能
- 🌟 获得读者高度评价，被认为在软件领域内容编译最出色
- 🏢 服务对象包括来自各大科技公司的技术领导者

---

### [C#文摘：电子邮件通讯](https://csharpdigest.net/?utm_source=web-archive&utm_campaign=react)

**原文标题**: [C# Digest: Email Newsletter](https://csharpdigest.net/?utm_source=web-archive&utm_campaign=react)

这是一份专为.NET开发者精心筛选的每周C#技术简报服务

- 📧 超过19,847名C#工程师订阅的每周邮件推送
- 📖 精选文章配摘要，节省寻找优质内容的时间
- 🎯 每周学习新知识，涵盖LINQ、诊断监听器等实用功能
- 💼 实际工作应用案例，包括操作结果模式和Azure函数迁移
- 🌍 受到全球.NET工程师认可的专业技术资讯源

---

### [让开发者与时俱进——Bonobo出版社](https://bonobopress.com/)

**原文标题**: [Keeping developers up to date â Bonobo Press](https://bonobopress.com/)

Bonobo Press是一家自2013年起为软件开发者和技术专业人士提供服务的媒体公司，通过发布精选的每周通讯，帮助超过88,000名技术人员及时获取最新行业动态。

- 📧 每周精选通讯：为软件开发者、工程经理和CTO提供简洁高效的行业资讯
- 👥 庞大读者群体：服务超过88,000名IT专业人士和技术专家
- 💼 精准广告投放：帮助企业接触软件工程师、技术主管等目标决策者
- 📊 专业媒体资料：提供详细的媒体工具包支持广告合作
- 🤝 多元化联系渠道：支持咨询、建议和广告合作等各类业务需求

---

### [往期简讯：第一页](https://reactdigest.net/newsletters)

**原文标题**: [Past Newsletters: Page 1](https://reactdigest.net/newsletters)

React Digest 是一份专注于 React 生态的技术简报，涵盖渲染优化、状态管理、新特性解析及实战案例，帮助开发者掌握前沿技术和最佳实践。

- 🌀 深入解析 React 渲染机制与 useEffectEvent 钩子
- 🧩 探讨 React Router 构建主从界面与 Activity 组件
- 🚀 分析 2025 年状态管理趋势与 Elm 架构启示
- ⚡ 揭秘 useState 原理与 3D 天气应用开发
- 🔗 研究 TanStack DB 响应式存储与 Next.js SEO 优化
- 🌊 探索并发特性、服务端组件及表单提交钩子
- 💾 解析缓存一致性策略与多标签页状态同步
- 🧵 实践 Web Workers 性能优化与 React Key 机制
- 🛠️ 剖析 useCallback 使用场景与钩子开发原理
- 📚 涵盖模块联邦、动画实现与国际化方案
- 🎯 聚焦手势识别、零界面更新与本地优先架构
- 🔄 对比数据获取方案与渐进式 JSON 技术
- 🧭 掌握路由数据去重与错误边界处理
- 🤖 结合 AI 开发与视觉编辑器工具链实践

---

### [隐私](https://reactdigest.net/privacy)

**原文标题**: [Privacy](https://reactdigest.net/privacy)

本隐私政策概述了React Digest如何依法合规地收集、使用和保护用户个人信息，重点说明仅收集邮箱用于发送周刊，并提供用户数据查询与删除的途径。

- 🎯 明确说明收集邮箱的唯一用途是发送周刊，不作他用
- 🔒 承诺仅为实现指定目的收集信息，并采取合理安全措施保护数据
- ⏱️ 声明仅在必要期限内保留个人信息
- 📧 允许用户随时通过邮件退订，并强烈反对垃圾邮件
- 👶 明确不收集13岁以下儿童信息，符合COPPA法案
- 📋 用户可依法申请获取或删除个人数据（联系privacy@reactdigest.net）
- ⚖️ 遵循数据保护相关法律，确保信息收集手段合法公正

---

### [媒体资料包——Bonobo出版社](https://bonobopress.com/media-kit/)

**原文标题**: [Media Kit â Bonobo Press](https://bonobopress.com/media-kit/)

Bonobo Press为技术从业者提供精准的新闻通讯广告服务，通过四大专业通讯覆盖不同技术领域的决策者与开发者，帮助广告商高效触达目标用户并提升转化率。

- 📧《科技领导力》面向技术管理者，订阅量26,385，开信率57.95%，单期赞助$1,940，主要受众为欧美企业的CTO及工程总监
- 💻《编程文摘》服务全栈开发者，订阅量18,263，点击率14.83%，单期赞助$875，用户经验层级分布均衡
- ⚙️《C#文摘》专注.NET生态，订阅量19,724，点击率高达21.63%，单期赞助$1,220，受众多就职于金融、医疗等大型企业
- 🎯《React文摘》聚焦前端开发，订阅量23,279，单期赞助$1,320，35%用户来自欧洲地区
- 📊广告格式为纯文本嵌入，需提前4天提交包含标题、描述及链接的文案
- 🤝合作流程包含需求沟通、档期确认、发票支付、文案优化及效果追踪五个步骤
- ✨已服务Okta、MongoDB、GitLab等知名企业，重复合作率较高

---

