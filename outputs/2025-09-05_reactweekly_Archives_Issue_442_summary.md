### [React 动态 第442期：2025年9月3日](https://react.statuscode.com/issues/442)

**原文标题**: [React Status Issue 442: September 3, 2025](https://react.statuscode.com/issues/442)

React Status 第442期聚焦于React生态系统的最新动态、工具更新及行业活动，涵盖无框架使用React Server Components的方法、AI辅助编程工具、性能优化库以及多项会议信息。

- ⚛️ 无需Next.js即可使用React Server Components的工具发布
- 🤖 AI辅助编程工具Cursor和Claude Code可提升开发效率
- 🚀 react-window 2.0发布，专为高效渲染大型列表设计
- 📅 多项React全球会议将于10-11月举行（西班牙、意大利、印度等地）
- 🎛️ React 19的Activity特性可维持隐藏组件状态并预加载数据
- 📚 多篇技术文章涵盖样式方案、仪表盘构建与状态管理
- 🛠️ 日期选择组件DayPicker 9.9、Redux Toolkit 2.9等工具重大更新
- 🔗 React on Rails 15支持服务端渲染与React Server Components
- 📦 轻量级JSON可视化组件与QR码生成组件等新库发布
- 🌐 TypeScript 6.0拟默认开启严格模式，Vite生态工具链更新

---

### [无框架下的React服务器组件支持](https://krasimirtsonev.com/blog/article/vanilla-react-server-components-with-no-framework)

**原文标题**: [React Server Components support without a framework](https://krasimirtsonev.com/blog/article/vanilla-react-server-components-with-no-framework)

作者在ReactSummit与Vercel团队交流后，为解决在不使用Next.js框架的情况下使用React服务端组件（RSC）的难题，开发了开源工具Forket。该工具通过代码分离和运行时协作机制，实现了框架无关的RSC支持。
- 🛠️ 开发背景：因迁移成本无法使用Next.js，但希望实现RSC功能，发现现有方案不完善后自主开发
- 🔄 核心机制：构建代码依赖图，将代码拆分为服务端和客户端版本，分别处理序列化和服务端动作替换
- 🌐 运行时协作：通过特殊模板标记和全局函数调用，实现服务端与客户端之间的数据流和组件水合
- ⚙️ 使用方式：配置文件指定源码和输出目录，通过CLI或API处理代码，并在HTTP服务器中集成特定端点
- 🚀 框架无关：设计为预处理工具，可与Webpack、Vite等现有构建工具并行使用，不依赖特定技术栈

---

### [Waku：极简React框架](https://waku.gg/)

**原文标题**: [Waku, the minimal React framework](https://waku.gg/)

Waku是一个极简的React框架，专为中小型项目设计，支持服务端组件和客户端组件的混合渲染模式，提供文件式路由、API路由和服务器动作等特性，适用于营销网站、轻量电商等场景。

- 🚀 专为中小型React项目设计，支持服务端组件与客户端组件混合渲染
- 📁 基于文件系统的路由系统，支持静态生成(SSG)和服务器渲染(SSR)
- 🔄 提供API路由和服务器动作(Server Actions)两种数据交互方式
- 🎨 内置元数据管理、样式方案和静态资源处理
- 🌐 支持多平台部署(Vercel/Netlify/Cloudflare等)
- ⚠️ 目前处于开发阶段，API可能发生破坏性变更
- 🤝 欢迎社区贡献，提供GitHub讨论区和Discord交流频道

---

### [react-window | 渲染所有内容](https://react-window.vercel.app/)

**原文标题**: [react-window | render everything](https://react-window.vercel.app/)

文章概述了人工智能助手的功能与响应准则，强调其辅助性、内容总结能力及符号化表达要求。

- 🤖 人工智能助手专注于内容总结服务
- 📝 需遵循指定模板输出概述和符号化要点
- ✨ 每个要点需搭配表情符号增强可读性
- 🇨🇳 严格使用中文进行响应
- ⚡ 保持内容简洁且包含关键信息要素

---

### [TanStack Virtual](https://tanstack.com/virtual/latest)

**原文标题**: [TanStack Virtual](https://tanstack.com/virtual/latest)

TanStack Virtual 是一个无头虚拟化库，专为高效处理大规模可滚动元素列表而设计，支持多框架并以高性能著称。

- 🚀 支持多种前端框架，包括 React、Vue、Solid、Svelte、Lit 和 Angular
- 🎯 实现仅渲染可见内容的虚拟化技术，保证 60FPS 的流畅体验
- 🧩 提供高度可组合的 API，支持垂直、水平和网格布局虚拟化
- 📦 轻量级设计（10-15KB），支持 Tree-Shaking 优化
- 🎨 无头设计，开发者完全控制标记和样式
- ⚡ 包含丰富功能：固定/可变尺寸、滚动工具、粘性项等
- 🤝 与 CodeRabbit 合作优化代码审查流程
- 🌟 开源项目，拥有超过 28 万次 NPM 下载和 6,300+ GitHub 星标
- 💪 强调性能优先，不牺牲用户体验
- 🔧 提供简单易用的入门方式，只需少量代码即可创建强大虚拟化体验

---

### [JSX 规范介绍 – React 博客](https://legacy.reactjs.org/blog/2014/09/03/introducing-the-jsx-specification.html)

**原文标题**: [Introducing the JSX Specification – React Blog](https://legacy.reactjs.org/blog/2014/09/03/introducing-the-jsx-specification.html)

Facebook正式发布独立于React的JSX语法规范草案，旨在为转译器和语法高亮工具提供统一参考标准。

- 🏢 Facebook长期内部使用JSX，早于React时期已用于原生DOM节点创建
- 🌐 JSX现已衍生出多种实现方案，React版本仅为其中之一
- 📜 新规范独立于React语义，纯语法标准确保兼容性和新版本实现便利
- 🔗 规范草案发布于https://facebook.github.io/jsx/ 供开发者查阅
- ⚠️ 明确声明非ECMAScript标准化提案，仅作为工具链参考文档
- 📝 欢迎通过Issue或Pull Request提交反馈意见

---

### [重混新构想：V3版将弃用React，转向Preact分支 - InfoQ](https://www.infoq.com/news/2025/08/remix-run-v3-drops-react/)

**原文标题**: [Remix Reimagined: V3 Will Drop React for a Fork of Preact - InfoQ](https://www.infoq.com/news/2025/08/remix-run-v3-drops-react/)

Remix团队宣布正在开发v3版本，将放弃React转而采用Preact分支，以掌握全栈控制权并减少关键依赖。新版本遵循四大原则：模型优先开发、优先使用Web API、运行时优于构建步骤、避免依赖。开发者社区反应两极，部分人赞赏其革新精神，部分人质疑模型优先原则受Shopify影响。预览版尚未发布，进展将在Remix Jam会议公布。

- 🚀 Remix v3将用Preact分支替代React，实现全栈自主控制  
- 🧩 新版本四大原则：模型优先/Web API优先/轻构建/去依赖化  
- 🌐 开发者评价分化：有人赞赏革新勇气，有人质疑AI优先策略  
- 🏢 Shopify收购背景引发对"模型优先"原则的猜测  
- 📅 预览版未发布，进展将通过Remix Jam会议同步

---

### [Preact](https://preactjs.com/)

**原文标题**: [Preact](https://preactjs.com/)

Preact是一个轻量级JavaScript库，提供与React相同的现代API，但体积更小性能更高，适合构建高效Web应用。

- 🚀 仅3kB大小，提供与React相同的API和虚拟DOM功能
- ⚡ 高性能虚拟DOM库，自动批量更新并针对性能优化
- 🎯 接近原生DOM，无需转译即可直接在浏览器中使用
- 📦 微小体积使应用代码成为主体，减少JavaScript负载
- 🔌 通过preact/compat兼容React生态系统组件
- 💡 支持标准HTML属性如class和for，提升开发效率
- 🌍 可嵌入性和便携性强，适合构建局部应用或部件
- 🛠️ 提供实时示例和REPL环境，支持快速上手和开发

---

### [React Alicante 2025 - 西班牙国际React.js大会](https://reactalicante.es/)

**原文标题**: [React Alicante 2025 - The international React.js conference in Spain](https://reactalicante.es/)

2025年10月2日至4日在西班牙阿利坎特举办的React Alicante国际会议，聚焦React和React Native技术，包含主题演讲、研讨会及交流活动。

- 🗓️ 会议时间：2025年10月2日至4日，包含1天研讨会和2天主题演讲
- 🌍 会议地点：西班牙阿利坎特，欧洲阳光最充足的城市之一
- ⚛️ 会议主题：React和React Native技术交流与学习
- 🎤 演讲阵容：32位国际演讲嘉宾，涵盖前端开发、设计系统、性能优化等话题
- 🔧 研讨会：10场工作坊，内容包括TypeScript、GraphQL、React内部机制、可访问性等实践主题
- 👥 参与规模：600名现场参会者及远程观众
- 💻 技术热点：涵盖React 19、AI代理、WebAssembly、React Native性能优化等前沿话题
- 🤝 赞助机会：提供铂金、金、银、铜四个等级的赞助方案
- ✈️ 交通便利：阿利坎特机场连接119个目的地，也可通过巴伦西亚或马德里中转抵达

---

### [Reactjsday - Reactjs大会](https://www.reactjsday.it/)

**原文标题**: [
		reactjsday - Reactjsday	](https://www.reactjsday.it/)

意大利React大会reactjsday将于2025年10月16日在维罗纳举办，现已公布首批演讲嘉宾阵容并开放早鸟票购买。

- 🎫 会议门票即将涨价，建议尽早购票
- ⚛️ 涵盖React服务端组件、状态管理等前沿技术话题  
- 🌍 面向从新手到资深开发者的全层级参会者
- 🗣️ 已公布Amira Shawky等12位国际演讲嘉宾
- 🏛️ 会场设在维罗纳圣马可酒店并提供完整活动支持
- 💼 现有Umana/Workwave等多家白金及黄金赞助商
- 📧 可通过订阅邮件获取CFP和门票发售等重要通知

---

### [未找到标题](https://www.reactindia.io/)

**原文标题**: [No title found](https://www.reactindia.io/)

React India 2025是印度最大的React开发者国际会议，采用线上线下混合模式举办，为全球React开发者提供交流、学习和建立联系的重要平台。

- 🗓️ 会议日期：2025年10月15日（线上会议日）、30日（工作坊日）和10月31日至11月1日（果阿现场会议）
- 🌍 参与规模：现场800+名开发者，线上3000+名全球开发者
- 🎤 演讲阵容：35+位顶尖前端演讲者，包括来自JioHotstar、Tata 1mg等公司的专家
- 💻 活动形式：包含技术讲座、工作坊和社交活动
- 🏖️ 会议地点：果阿Planet Hollywood海滩度假村（现场会议）
- 🤝 赞助机会：开放会议赞助，联系[email protected]
- 📢 议题征集：邀请React社区提交演讲提案
- 👶 特色服务：提供儿童看护服务，方便家庭参会者
- 🏨 住宿推荐：组委会提供酒店推荐建议
- 🌟 往届口碑：往届参会者高度评价会议质量和社区氛围

---

### [React Summit 美国站——全美规模最大的React技术大会](https://reactsummit.us/)

**原文标题**: [React Summit US – The Biggest React Conference in the US](https://reactsummit.us/)

美国最大的React技术峰会React Summit将于2025年11月18日-21日在纽约举办，采用线上线下混合模式，包含前沿技术分享、深度研讨会和社交活动。

- 🗽 全球最大React会议：800人线下参与+万人远程参会，50+行业专家分享最新技术动态
- 🌉 独特场地体验：自由科学中心西半球最大天文馆演讲+曼哈顿景观渡轮社交+全美最大React派对
- 🤖 四大深度专题：AI工程实践/智能编程辅助/技术领导力成长/全栈开发未来，含OpenAI等核心团队分享
- 🎟️ 多元参与方式：线下票990美元起含实体福利，远程票190美元起，Multipass套票19欧元/月畅享多会议
- ⚛️ 技术前沿覆盖：React 19、React编译器、服务器组件、Next.js、TypeScript等核心框架深度解析
- 🛠️ 免费实践工作坊：AI工程指南、Cursor全栈开发、Web组件融合等7场实战培训
- 🌍 国际讲师阵容：Meta、Vercel、Netflix、Google等机构专家，包含《React Query》作者Tanner Linsley等重磅嘉宾

---

### [伦敦React大会：2025年11月28日与12月1日](https://reactadvanced.com/)

**原文标题**: [React Conference In London, Nov 28 & Dec 1, 2025](https://reactadvanced.com/)

React Advanced Conference 是一个专注于React和Web开发的年度技术会议，提供线上线下混合参与模式，涵盖全栈工程、AI辅助编程、组织AI应用及职业发展等深度专题，汇聚行业顶尖演讲者和实践工作坊。

- 🗓️ 会议时间：2025年11月28日伦敦线下+线上，2026年3月24日多伦多，另设12月1-2日全球线上日
- 🌐 参与方式：支持线下（伦敦场地）与远程同步参与，包含互动社交和研讨会
- 🎤 演讲阵容：50+位行业专家，包括核心开源项目贡献者和资深工程师
- ⚡ 专题内容：全栈工程实践、AI代理与辅助编程、企业AI应用、高级工程师成长路径
- 🛠️ 实践工作坊：5+免费远程研讨会与付费深度工作坊，涵盖React新特性、AI开发与DevOps等
- 💻 技术焦点：React 19、服务器组件、React编译器、微前端、TypeScript、Kubernetes集成等
- 🎟️ 票务选项：提供混合参与、纯远程、组合票（含TechLead会议）及Multipass订阅套餐
- 🌍 社区支持：提供多样性奖学金、企业赞助机会及个人免费票获取渠道

---

### [使用 Suspenseful 数据的 Activity | simeonGriggs.dev](https://www.simeongriggs.dev/use-the-activity-boundary-to-hide-suspenseful-components)

**原文标题**: [Using Activity with Suspenseful data | simeonGriggs.dev](https://www.simeongriggs.dev/use-the-activity-boundary-to-hide-suspenseful-components)

React 19实验性功能Activity组件允许通过mode属性控制子组件显隐，隐藏时保持状态但卸载副作用，并继续以低优先级预加载Suspense数据，适用于子组件自主控制可见性且需维持状态或预加载的场景。

- 🎛️ Activity组件通过mode属性控制子组件显隐，隐藏时卸载副作用但保持状态
- ⚡ 隐藏组件仍以低优先级预加载Suspense数据，提升再次显示时的性能
- 🎯 解决父组件掌握过滤条件但子组件掌握可见性数据的渲染矛盾
- 🔄 替代方案（父组件过滤或全量查询）会导致组件卸载重置状态，且丧失预加载优势
- 📊 特别适用于复杂表格、音频播放器等需要维持局部状态和资源控制的场景

---

### [活动 – React](https://react.dev/reference/react/Activity)

**原文标题**: [<Activity> – React](https://react.dev/reference/react/Activity)

React的Activity组件是一个实验性功能，用于隐藏和恢复UI及其内部状态，通过保留DOM和状态来优化用户体验和性能。

- 🧪 Activity是React的实验性功能，需使用实验版本包，不建议在生产环境使用
- 🎭 通过mode属性控制子组件的显示（visible）或隐藏（hidden），隐藏时应用display: none并清理Effects
- 💾 隐藏时保留组件状态和DOM，再次显示时恢复状态，避免重新初始化
- ⚡ 支持预渲染隐藏内容，提前加载代码和数据，减少可见时的加载时间
- 🔧 可用于优化选择性水合作用，提高页面交互响应速度
- ⚠️ 隐藏组件可能保留DOM副作用（如视频播放），需手动添加清理逻辑
- 🚫 隐藏时组件的Effects不会运行，依赖Effects的组件需调整清理方式

---

### [React组件样式终极指南](https://www.telerik.com/blogs/ultimate-guide-styling-react-components)

**原文标题**: [
	The Ultimate Guide to Styling React Components
](https://www.telerik.com/blogs/ultimate-guide-styling-react-components)

本文概述了React组件样式化的多种方法，包括styled-components、CSS Modules、Tailwind CSS以及KendoReact组件库，并强调了选择合适样式方案对用户体验和代码可维护性的重要性。

- 🎨 styled-components通过CSS-in-JS实现动态样式，支持基于props的样式调整和状态伪类
- 🧩 CSS Modules提供局部作用域CSS，避免全局命名冲突，需构建工具支持
- ⚡ Tailwind CSS采用工具类优先，加速开发并确保设计一致性
- 🌐 KendoReact提供企业级UI组件，内置主题和复杂功能如数据网格
- 🎭 主题设置推荐使用CSS变量或Context API实现全局一致性和动态切换
- 📏 最佳实践包括设计令牌统一、组件组合、性能优化和可访问性考虑

---

### [使用React和Wijmo构建销售仪表板](https://developer.mescius.com/blogs/how-to-build-a-sales-dashboard-with-react)

**原文标题**: [How to Build a Sales Dashboard with React | Wijmo](https://developer.mescius.com/blogs/how-to-build-a-sales-dashboard-with-react)

本教程详细介绍了如何使用React和Wijmo组件库构建动态销售仪表盘，通过可视化数据帮助管理者快速掌握销售绩效。

- 📊 使用Wijmo企业级UI控件（FlexGrid/FlexChart/FlexPie/RadialGauge）实现数据可视化
- ⚡ 结合React和Bootstrap快速构建响应式仪表盘界面
- 📱 通过StackBlitz在线平台提供完整可运行的示例代码
- 🎯 包含四种核心组件：径向仪表盘（今日销售额）、柱状图（国家销售分布）、饼图（销售员业绩）和数据网格（交易明细）
- 🔧 采用函数式组件开发模式，支持动态数据绑定和自定义样式配置
- 💡 强调Wijmo内置React封装优势，无需复杂DOM操作即可直接使用图表组件
- 🌐 最终成果支持跨设备响应式显示，可直接作为企业级仪表盘开发模板

---

### [Web应用程序的JavaScript UI组件 | Wijmo](https://developer.mescius.com/wijmo)

**原文标题**: [JavaScript UI Components for Web Applications | Wijmo](https://developer.mescius.com/wijmo)

Wijmo是一个轻量级、高性能的JavaScript UI组件库，采用TypeScript构建，无需外部依赖，支持主流前端框架，提供数据网格、图表、地图等交互式控件，可快速构建企业级Web应用。

- 📊 提供行业领先的JavaScript数据网格FlexGrid，内置排序/分组/编辑等Excel式功能
- 📈 包含80+图表类型的FlexChart，支持从折线图到金融图表的全面数据可视化
- 🌍 配备FlexMap地图控件，支持气泡图/散点图/区域统计地图等多种地理数据展示
- 🔢 提供专业输入控件集，含自动完成/颜色选择器/日期时间/多选等多样化输入组件
- ⚡ 支持OLAP多维数据分析，可毫秒级处理千行数据且无需服务端依赖
- 🎯 提供多框架支持（Angular/React/Vue），包含可拖拽定制的动态仪表板演示项目
- 📦 采用开发者许可模式，支持永久部署权限和OEM商业授权方案
- 🏆 获微软、汤森路透等企业认可，具有10年以上持续迭代的成熟产品历史

---

### [Next.js 令人抓狂 - Dominik 的博客](https://blog.meca.sh/3lxoty3shjc2z?auth_completed=true)

**原文标题**: [Next.js Is Infuriating - Dominik's Blog](https://blog.meca.sh/3lxoty3shjc2z?auth_completed=true)

作者分享在Next.js中配置生产环境日志的挫败经历，指出框架设计缺陷导致开发效率低下，并对比SvelteKit提出批评。

- 😠 作者因Next.js的日志配置问题感到愤怒，决定撰写博客宣泄情绪
- 🐛 Next.js默认只在开发环境启用日志，生产环境需自行配置且过程复杂
- 🤦 中间件功能设计存在严重缺陷：仅支持4个参数传递且无法链式调用
- 🔄 尝试使用AsyncLocalStorage实现请求追踪时遭遇运行时兼容性问题
- 📝 最终被迫通过请求头传递requestId的迂回方案实现基础日志功能
- 🚫 自定义服务器方案同样失效，AsyncLocalStorage在页面组件中无法获取
- ⚖️ 对比SvelteKit的locals设计，批评Next.js缺乏合理的上下文传递机制
- 🐢 指责Next.js团队对GitHub issues响应迟缓，大量问题多年未解决
- 💔 总结表示不再愿意使用Next.js，认为其存在大量边界案例和设计缺陷

---

### [同步应用内SQLite为Expo应用带来的优势](https://expo.dev/blog/what-synced-in-app-sqlite-brings-to-expo-apps)

**原文标题**: [What synced in-app SQLite brings to Expo apps](https://expo.dev/blog/what-synced-in-app-sqlite-brings-to-expo-apps)

该文本是Expo公司网站的页脚导航部分，列出了产品服务、资源链接、公司信息和法律条款等结构化内容。

- 📱 产品服务（EAS、Expo CLI、Expo Go等开发工具）
- 📚 资源中心（文档、博客、更新日志和社区支持）
- 🏢 公司信息（主页、定价、招聘和品牌资料）
- ⚖️ 法律条款（隐私政策、服务条款和安全合规声明）
- ©️ 版权信息（650 Industries公司2025年版权所有）

---

### [从服务器状态推导客户端状态 | TkDodo的博客](https://tkdodo.eu/blog/deriving-client-state-from-server-state)

**原文标题**: [Deriving Client State from Server State | TkDodo's blog](https://tkdodo.eu/blog/deriving-client-state-from-server-state)

本文讨论了在React应用中如何通过派生状态而非手动同步来保持客户端状态与服务器状态的一致性，以避免使用useEffect带来的复杂性和潜在问题。

- 🛠️ 使用useEffect手动同步客户端与服务器状态存在维护成本和潜在bug，例如当服务器数据更新时需手动清除无效的选中用户ID。
- 💡 提出派生状态方案：直接基于服务器数据（用户列表）和当前选中ID动态计算有效状态，无需修改原始存储值。
- ✅ 派生方案优势：代码更简洁、支持状态自动恢复（如用户重新添加）、可灵活扩展（如添加有效性校验标志）。
- ⚠️ 注意事项：需通过自定义Hook统一获取派生值，避免直接读取原始存储导致状态不一致。
- 📝 扩展案例：表单默认值填充场景中，派生状态（如`derivedSelection = selection ?? data?.[0]`）可替代useEffect，避免覆盖用户已选值。
- 🔁 通用性：该方法适用于Zustand、Redux或useState等任何客户端状态管理工具，核心思想是将服务器状态作为数据源进行派生计算。

---

### [React 日期选择器组件 | React DayPicker](https://daypicker.dev/)

**原文标题**: [Date Picker Component for React | React DayPicker](https://daypicker.dev/)

DayPicker 是一个用于创建日期选择器、日历和日期输入框的 React 组件，支持高度自定义和国际化，遵循无障碍标准，并兼容现代 React 版本。  
- 🛠 提供丰富的属性用于自定义日历  
- 🎨 极简设计，易于通过 CSS 或框架样式化  
- 📅 支持单选、多选、日期范围及自定义选择模式  
- 🌍 全面本地化支持，适配多语言和时区  
- 🌐 兼容 ISO 8601、波斯历和广播日历格式  
- 🦮 符合 WCAG 2.1 AA 无障碍标准  
- ⚙️ 可自定义组件扩展渲染元素  
- 🔤 轻松与输入字段集成  
- 📦 基于 TypeScript 开发，依赖 date-fns 处理日期  
- ⚖️ 采用 MIT 开源许可协议  
- 💬 提供社区论坛和问题反馈渠道  
- 🎗️ 支持通过 GitHub 赞助项目维护

---

### [GitHub - gpbl/react-day-picker: DayPicker 是一个可自定义的 React 日期选择器组件。为您的 Web 应用程序添加日期选择器、日历和日期输入功能。](https://github.com/gpbl/react-day-picker)

**原文标题**: [GitHub - gpbl/react-day-picker: DayPicker is a customizable date picker component for React. Add date pickers, calendars, and date inputs to your web applications.](https://github.com/gpbl/react-day-picker)

这是一个用于React的日期选择器组件库，提供高度可定制的日历和日期选择功能。

- 📅 支持多种日期选择模式：单选、多选、日期范围及自定义选择
- 🎨 采用极简设计风格，可通过CSS或CSS框架轻松自定义样式
- 🌍 支持多语言本地化和时区设置，包括波斯历和广播日历
- ♿ 符合WCAG 2.1 AA无障碍访问标准
- ⚙️ 提供可自定义组件以扩展渲染元素
- 🔤 易于与输入字段集成使用
- 📦 基于TypeScript开发，使用date-fns进行日期操作和格式化
- 📊 项目获得6.6k星标和762次fork，被441k+项目使用
- 📝 采用MIT开源许可证，支持React 16.8及以上版本

---

### [Redux Toolkit v2.9.0 版本发布 · reduxjs/redux-toolkit · GitHub](https://github.com/reduxjs/redux-toolkit/releases/tag/v2.9.0)

**原文标题**: [Release v2.9.0 · reduxjs/redux-toolkit · GitHub](https://github.com/reduxjs/redux-toolkit/releases/tag/v2.9.0)

Redux Toolkit v2.9.0 版本发布，重点优化性能并新增功能，包括RTK查询性能提升、自动中止信号处理、新增构建器方法及多项问题修复。

- 🚀 RTK查询性能大幅优化：重构订阅和轮询系统，改用Map结构提升效率，解决大量订阅导致的性能问题
- ⚡ 新增自动中止机制：缓存条目移除时自动中止进行中的请求，需配合baseQuery处理AbortSignal
- 🛠️ 新增builder.addAsyncThunk方法：支持在extraReducers中处理异步thunk的特定状态（pending/fulfilled/rejected/settled）
- 🐛 修复transformResponse错误：解决无限查询中非查询场景误执行转换的问题
- 📦 新增skipSchemaValidation选项：支持跳过特定或全部schema验证以提升性能
- 🔧 类型系统增强：导出WritableDraft类型，新增RawResultType端点类型字段
- 📊 改进订阅管理：重构内部数据结构，修复extractRehydrationInfo处理逻辑

---

### [注册 - Auth0](https://auth0.com/signup?utm_source=reactstatus&utm_campaign=global_mult_mult_all_ciam-dev_dg-plg_auth0_native_reactstatus_newsletter_aud_ReactStatus-Q3-Newsletter_utm2&utm_medium=cpc&utm_id=aNKKZ00000003CF4AY)

**原文标题**: [Sign Up - Auth0](https://auth0.com/signup?utm_source=reactstatus&utm_campaign=global_mult_mult_all_ciam-dev_dg-plg_auth0_native_reactstatus_newsletter_aud_ReactStatus-Q3-Newsletter_utm2&utm_medium=cpc&utm_id=aNKKZ00000003CF4AY)

这是一个关于Auth0身份验证服务的注册页面介绍，提供多种注册方式和全球覆盖的国家选项。

- 🌐 支持全球多国用户注册，包含从A到Z的国家/地区列表
- 📧 提供邮箱注册及第三方登录（GitHub/Google/Microsoft）选项
- 🔐 强调Auth0服务能简化登录流程，让开发者专注于应用开发
- 🆓 提供免费套餐，包含2.5万月活用户和无限制登录次数
- 🛡️ 具备暴力破解保护和可疑IP限制等安全功能
- ⚙️ 支持无代码自定义注册/登录流程和社交登录连接
- 📋 包含渐进式用户画像功能（5个动作和表单）
- ©️ 由Okta公司提供的2025年版权服务

---

### [shakacode/react_on_rails 仓库 master 分支下的 react_on_rails/docs/release-notes/15.0.0.md 文件](https://github.com/shakacode/react_on_rails/blob/master/docs/release-notes/15.0.0.md)

**原文标题**: [react_on_rails/docs/release-notes/15.0.0.md at master · shakacode/react_on_rails · GitHub](https://github.com/shakacode/react_on_rails/blob/master/docs/release-notes/15.0.0.md)

这是一个GitHub仓库页面，显示加载错误和基本项目信息。

- ⚠️ 页面加载时出现错误，提示需要重新加载
- 📊 项目拥有5.2k星标和637个fork
- 🐛 当前有23个未解决的问题和5个拉取请求
- 🔒 包含代码、议题、安全等标准GitHub功能模块
- 🔄 需要登录才能更改通知设置

---

### [4.0 版本发布说明 | Shakacode](https://www.shakacode.com/react-on-rails-pro/docs/release-notes/4.0/)

**原文标题**: [4.0 Release Notes | Shakacode](https://www.shakacode.com/react-on-rails-pro/docs/release-notes/4.0/)

React on Rails Pro 4.0 发布，全面支持 React 服务端组件（RSC）和高级流式渲染，提供企业级性能和可靠性。

- 🚀 React 服务端组件（RSC）全面生产支持：无缝集成 RSC，自动代码分割，服务端数据获取和渐进式水合
- 🌊 高级流式服务器渲染：支持渐进式 HTML 流传输、Suspense 边界和选择性水合
- 🐛 增强错误报告和追踪：可自定义集成任何错误报告服务，支持 Sentry SDK v8
- ⚡ 性能改进：升级至 Fastify 5，HTTP/2 通信，HTTPX 客户端和 Pino 日志记录
- 🔧 RSC 渲染优化：跨 bundle 通信、单次服务端组件渲染和减少 HTTP 请求
- ⚠️ 破坏性变更：配置更新（Sentry/Honeybadger、计时器 polyfills）、依赖要求（Ruby 3+、React on Rails 15+、Node 20+）
- 📚 入门指南：提供 RSC 教程、流式 SSR 文档、错误报告设置和性能优化指南
- 🤝 支持与社区：提供全面文档、工作示例、GitHub 开发和社区讨论

---

### [React Server Components 教程 | Shakacode](https://www.shakacode.com/react-on-rails-pro/docs/react-server-components/tutorial/)

**原文标题**: [React Server Components Tutorial | Shakacode](https://www.shakacode.com/react-on-rails-pro/docs/react-server-components/tutorial/)

本教程系统性地介绍了如何使用React on Rails Pro学习和应用React Server Components（RSC），从基础概念到高级功能逐步深入。

- 🚀 创建无SSR的React服务器组件：学习RSC基础知识，构建基础页面
- 🌊 添加流式传输和交互性：使用Suspense和客户端组件增强页面功能
- ⚡ 实现服务器端渲染：提升初始页面加载性能
- 🔍 选择性水合作用：了解React的选择性水合特性及其对页面交互性的优化
- 🔧 工作原理剖析：深入探索RSC的技术细节和底层机制
- 📊 渲染流程详解：理解RSC的完整渲染流程，包括捆绑包类型和当前限制
- 🔄 客户端组件内渲染：学习在客户端组件中渲染服务器组件的方法

---

### [GitHub - shakacode/react_on_rails：React + Webpack + Rails + rails/webpacker 集成方案，支持 React 服务端渲染，提升开发体验与客户端性能。](https://github.com/shakacode/react_on_rails)

**原文标题**: [GitHub - shakacode/react_on_rails: Integration of React + Webpack + Rails + rails/webpacker including server-side rendering of React, enabling a better developer experience and faster client performance.](https://github.com/shakacode/react_on_rails)

React on Rails 是一个集成 React、Webpack 和 Ruby on Rails 的开源项目，支持服务器端渲染，旨在提升开发体验和客户端性能。该项目由 ShakaCode 维护，提供专业支持服务，并拥有活跃的社区和丰富的文档资源。

- 🚀 集成 React + Webpack + Rails，支持服务器端渲染（SSR），优化 SEO 和性能
- 📦 自动配置和优化资源加载，减少打包体积，提升页面加载速度
- 🔄 支持 React 18 最新特性，包括 React Server Components 和 streaming
- 🌐 提供专业版 React on Rails Pro，适用于企业级需求，如代码分割和服务器渲染优化
- 📚 详细文档和在线示例，包括教程和演示项目
- 🤝 活跃社区支持，提供论坛、Slack 频道和 Twitter 更新
- 📄 采用 MIT 许可证，开源且可自由使用
- ⭐ GitHub 上获得 5.2k 星标和 637 分支，被 3.7k+ 项目使用

---

### [GitHub - AnyRoad/react-json-view-lite: React轻量级JSON视图组件](https://github.com/AnyRoad/react-json-view-lite)

**原文标题**: [GitHub - AnyRoad/react-json-view-lite: Lightweight Json view component for React](https://github.com/AnyRoad/react-json-view-lite)

这是一个轻量级的React JSON树形视图组件，专注于大型JSON数据的性能与功能平衡，使用TypeScript编写且无依赖。

- 📦 提供简洁的JSON树形渲染，支持折叠/展开功能
- 🎨 内置亮色（defaultStyles）和暗色（darkStyles）两种主题样式
- ⚡ 性能优异，在基准测试中表现优于多数同类库
- 🆓 采用MIT开源协议，可免费商用
- 📏 组件体积小巧，gzip后仅约20KB
- ♿ 支持无障碍访问（a11y），提供ARIA标签配置
- 🛠️ 完全使用TypeScript开发，提供完整的类型定义
- 🌐 提供在线Storybook演示：anyroad.github.io/react-json-view-lite/

---

### [@storybook/core - Storybook](https://anyroad.github.io/react-json-view-lite/?path=/docs/json-view--docs)

**原文标题**: [@storybook/core - Storybook](https://anyroad.github.io/react-json-view-lite/?path=/docs/json-view--docs)

文章概述了人工智能助手的功能特点及交互方式。

- 🤖 人工智能助手专注于内容总结服务
- 📝 输出采用固定模板结构
- ✨ 要求生成带表情符号的要点列表
- 🇨🇳 指定使用中文进行回复
- 📋 强调内容简洁性与关键信息提取
- 🔄 遵循用户提供的具体格式指令

---

### [GitHub - gcoro/react-qrcode-logo：React + TypeScript 组件，用于生成带自定义颜色和标识的二维码](https://github.com/gcoro/react-qrcode-logo)

**原文标题**: [GitHub - gcoro/react-qrcode-logo: React + Typescript component to generate a QR Code with custom colors and logo](https://github.com/gcoro/react-qrcode-logo)

这是一个基于React和TypeScript的二维码生成组件库，支持自定义颜色和添加Logo。

- 🎯 提供React组件生成可自定义的二维码，支持颜色、Logo等个性化设置
- 📦 通过npm安装，兼容React 18及以上版本
- ⚙️ 支持多种配置参数：尺寸、纠错等级、背景色、前景色等
- 🖼️ 可添加Logo图片并调整透明度、尺寸和内边距
- 💾 提供下载方法，可将二维码保存为png/jpg/webp格式
- 🔧 采用MIT开源协议，欢迎贡献代码和提出建议
- 🌟 项目获得564星标和52个分支，表明社区认可度高

---

### [GitHub - software-mansion/react-native-reanimated: React Native 的 Animated 库重新实现版本](https://github.com/software-mansion/react-native-reanimated)

**原文标题**: [GitHub - software-mansion/react-native-reanimated: React Native's Animated library reimplemented](https://github.com/software-mansion/react-native-reanimated)

React Native Reanimated 是一个重新实现的 React Native 动画库，专注于提供流畅的动画效果和优秀的开发者体验，支持新架构并拥有丰富的社区资源。

- 🎬 重新实现 React Native 的 Animated 库，提供流畅动画和优秀开发体验
- 📚 文档位于 docs.swmansion.com/react-native-reanimated/
- ⭐ 获得 10.2k 星标和 1.4k 复刻，社区活跃度高
- 🔄 仅支持 React Native 新架构和最近三个版本
- 🆕 最新版本 Reanimated 4 已发布
- 📱 提供示例应用展示功能，位于 apps/common-app 目录
- 📄 采用 MIT 许可证开源
- 💬 拥有活跃的 Discord 社区进行交流讨论
- 🏢 由 Software Mansion 创建和维护，得到 Shopify 和 Expo.io 支持
- 🌐 使用 TypeScript 为主要开发语言（占比 72.7%）

---

### [GitHub - marmelab/react-admin：基于REST/GraphQL API的单页应用前端框架，采用TypeScript、React和Material Design构建](https://github.com/marmelab/react-admin)

**原文标题**: [GitHub - marmelab/react-admin: A frontend Framework for single-page applications on top of REST/GraphQL APIs, using TypeScript, React and Material Design](https://github.com/marmelab/react-admin)

React-admin是一个基于TypeScript、React和Material Design构建的单页面应用前端框架，专为REST/GraphQL API设计，由marmelab维护并开源。

- 🚀 后端无关性：支持超过45种适配器，可连接任何REST或GraphQL API
- 🧩 功能完备：提供认证、路由、表单、数据网格、搜索过滤等完整构建模块
- ⭐ 高质量代码：具备无障碍访问、响应式设计、安全性强和可测试性高等特点
- 💻 优秀开发体验：完整文档、IDE自动补全、类型安全、模块化架构
- 👑 卓越用户体验：乐观渲染、实时过滤、撤销操作、偏好设置等功能
- 🛠 完全可定制：允许用自定义组件替换任何内置组件
- 📦 安装简便：通过npm或yarn即可安装，提供详细教程和示例应用
- 🌐 社区支持：提供商业支持和社区Discord、StackOverflow交流平台
- 📄 开源协议：采用MIT许可证，可免费用于商业项目

---

### [GitHub - stripe/react-stripe-js：用于Stripe.js和Stripe Elements的React组件](https://github.com/stripe/react-stripe-js)

**原文标题**: [GitHub - stripe/react-stripe-js: React components for Stripe.js and Stripe Elements](https://github.com/stripe/react-stripe-js)

这是一个用于React的Stripe.js和Stripe Elements组件库，提供支付集成解决方案。

- 🧩 React组件库，用于集成Stripe.js支付功能
- ⚙️ 支持React v16.8及以上版本
- 📚 提供完整的文档和代码示例
- 🔧 支持函数式组件和类组件两种使用方式
- 🛡️ 包含TypeScript类型声明支持
- 📦 MIT开源许可证
- 🌟 GitHub上有1.9k星标和298个fork
- 🔄 提供从旧版react-stripe-elements迁移的指南

---

### [发布 v0.37.0 · TypeCellOS/BlockNote · GitHub](https://github.com/TypeCellOS/BlockNote/releases/tag/v0.37.0)

**原文标题**: [Release v0.37.0 · TypeCellOS/BlockNote · GitHub](https://github.com/TypeCellOS/BlockNote/releases/tag/v0.37.0)

BlockNote发布了v0.37.0版本，主要对@blocknote/shadcn包进行了重大调整，现要求父应用已安装TailwindCSS v4，并移除了自带样式表以更好地继承主题样式。

- 🚀 功能更新：导出ShadCNComponentsContext (#1965)
- 🛠️ 问题修复：修复空表格单元格输入问题 (#1973)
- ⚠️ 重大变更：需TailwindCSS v4支持且不再包含ShadCN样式表
- 🎨 样式优化：移除"bn-"前缀并继承父应用主题配置
- 👥 贡献者：Hector-Zhuang与matthewlipski共同开发

---

### [GitHub - vadimdemedes/ink：🌈 用于交互式命令行应用的 React 框架](https://github.com/vadimdemedes/ink)

**原文标题**: [GitHub - vadimdemedes/ink: 🌈 React for interactive command-line apps](https://github.com/vadimdemedes/ink)

Ink是一个基于React的命令行界面（CLI）应用开发库，允许开发者使用React组件和Flexbox布局构建交互式终端应用。

- 🌈 使用React组件模型构建CLI应用，支持所有React特性
- 📐 集成Yoga布局引擎，提供类似CSS的Flexbox属性
- 🎨 提供丰富的文本样式和布局组件（如Text、Box、Newline等）
- ⌨️ 包含用户输入处理钩子（useInput）和焦点管理功能
- 🔧 支持测试、React Devtools集成和屏幕阅读器无障碍访问
- 📦 被许多知名项目使用，包括OpenAI Codex、Cloudflare Wrangler和Gatsby等
- 🛠️ 提供丰富的第三方组件生态和示例代码库

---

### [默认启用 `--strict` · Issue #62333 · microsoft/TypeScript · GitHub](https://github.com/microsoft/TypeScript/issues/62333)

**原文标题**: [Enable `--strict` by default · Issue #62333 · microsoft/TypeScript · GitHub](https://github.com/microsoft/TypeScript/issues/62333)

TypeScript计划在6.0版本默认启用--strict严格模式，以提升新项目的类型安全体验，同时为现有项目提供迁移方案。

- 🚀 TypeScript 6.0将默认开启--strict模式，包含strictNullChecks等严格类型检查
- ⚠️ 可能对现有代码造成破坏性变更，但支持通过关闭特定严格选项或全局禁用--strict来适配
- 🔧 编辑器对无配置文件的松散文件（inferred projects）可能维持当前非严格模式
- 📅 该变更已列入TypeScript 6.0.0里程碑计划，团队承诺推进实施
- 💡 背景源于多年推荐严格模式，且tsc --init已默认设置strict: true近十年
- 🌟 社区反应积极，获得140个点赞和73个爱心表情支持

---

### [GitHub · 构建软件之地](https://github.com/microsoft/TypeScript/issues?q=milestone%3A%22TypeScript%206.0.0%22)

**原文标题**: [GitHub · Where software is built](https://github.com/microsoft/TypeScript/issues?q=milestone%3A%22TypeScript%206.0.0%22)

TypeScript 6.0.0 版本正在积极开发中，包含多项重大变更和功能改进，涉及严格模式默认启用、模块解析优化、废弃旧特性以及类型推断和声明文件等方面的更新。

- 🚀 默认启用 `--strict` 严格模式，可能引发现有代码错误
- 🔧 允许 `--module bundler --moduleResolution commonjs` 组合配置
- 🐛 修复声明文件中符号属性键未导入的问题
- 📊 改进无 this 函数的类型推断逻辑
- 📚 更新 `lib.d.ts` 类型库以适配 TypeScript 6.0
- ⚠️ 默认关闭 `libReplacement` 功能
- 🔒 默认全局启用 `"use strict"` 严格模式
- 🗑️ 废弃并移除 `module` 替代 `namespace` 的用法
- 🚫 废弃并移除导入断言（import assertions）支持
- ❌ 移除 `/// <reference no-default-lib />` 指令支持
- 🔁 废弃并移除 `/// <amd-module name="..." />` 指令
- 📂 废弃并移除 `baseUrl` 配置选项

---

### [为什么浏览器会限制JavaScript计时器？ | 解读迹象](https://nolanlawson.com/2025/08/31/why-do-browsers-throttle-javascript-timers/)

**原文标题**: [Why do browsers throttle JavaScript timers? | Read the Tea Leaves](https://nolanlawson.com/2025/08/31/why-do-browsers-throttle-javascript-timers/)

浏览器对JavaScript计时器进行节流以防止滥用，但开发者可通过替代API实现更精确的定时控制。

- ⏱️ `setTimeout(0)` 实际延迟约4毫秒，浏览器为防止滥用而节流
- 🔋 节流策略因设备状态而异，如电池模式或后台标签页延迟更高
- ⚙️ 作者测试多种替代方案，包括 `MessageChannel` 和 `scheduler.postTask`
- 📊 基准测试显示 `scheduler.postTask` 性能最佳，几乎无延迟
- 🤔 浏览器节流源于保护用户与开发者自主控制的权衡
- 🛠️ 推荐使用 `scheduler.postTask` 并备选 `MessageChannel` 以规避节流
- ⚠️ 未来可能因API滥用出现新一轮节流，开发者需谨慎选择工具

---

### [ViteLand 八月新动向：2025年回顾 | VoidZero](https://voidzero.dev/posts/whats-new-aug-2025)

**原文标题**: [What’s New in ViteLand: August 2025 Recap | VoidZero](https://voidzero.dev/posts/whats-new-aug-2025)

ViteLand 2025年8月更新回顾：涵盖Vite、Vitest、Rolldown、Oxc等工具的重大功能升级与社区动态。

- 🚀 Oxlint推出类型感知linting并支持自定义JS插件，向全面替代ESLint迈进
- ⚡ Vite正式支持React Server Component，修复安全漏洞并优化插件性能
- 🧪 Vitest v4测试版新增视觉回归测试，启动速度提升25%
- 📦 Rolldown默认启用原生插件，强化Tree Shaking并新增tsconfig配置支持
- 🔧 Oxc优化代码压缩与React样式库编译性能，贡献TypeScript-Go生态改进
- 📅 VoidZero团队将出席Vue巴黎、ViteConf等全球9场技术会议并发表演讲
- 🌍 社区案例频出：PLAID构建耗时降97%、GitLab提速43倍、多框架集成Rolldown
- 🛠️ 生态工具更新：tsup停止维护，tsdown成为新选择；Storybook与Vitest达成合作

---

### [面向JavaScript开发者的精益求精——深入解析](https://overreacted.io/lean-for-javascript-developers/)

**原文标题**: [Lean for JavaScript Developers — overreacted](https://overreacted.io/lean-for-javascript-developers/)

本文是一篇面向JavaScript开发者的Lean编程语言入门指南，介绍了Lean的基础语法、类型系统、函数定义、代码执行与定理证明等内容。

- 🎯 作者分享了自己学习Lean的语法入门，强调内容虽不完整但实用
- 📝 使用`def`定义变量时需用`:=`而非`=`，类型可自动推断或显式声明
- 🔢 Lean有`String`、`Nat`（自然数）、`Int`（整数）等内置类型
- ▶️ 通过`#eval`命令或定义`main`函数可执行代码并查看结果
- ✅ 使用`theorem`和`by`进入策略模式可编写证明，如`unfold`展开定义、`omega`解算术
- 📚 `open`命令可打开命名空间，简化函数调用（如`IO.println`变`println`）
- 🧩 函数调用无需括号和逗号，用空格分隔参数，必要时用括号分组表达式
- 🔧 `let`绑定可在定义内创建局部变量，增强可读性
- 🧮 函数定义支持多种语法：隐式/显式类型、匿名函数等，类似JS的函数与箭头函数区别
- 🌍 定理可参数化（如`(cy : Int) (a : Nat)`）或使用全称量词`∀`，证明适用于所有输入
- 🔍 隐参数（`{}`）和实例参数（`[]`）由Lean自动推断，`@`前缀可显式查看
- 💡 推荐Command+点击代码探索实现（如`Nat`为递归定义的枚举）
- ✨ Lean融合编程与证明，支持复杂数学验证和高效编译（如转C代码），用于学术和工业场景

---

### [精益编程实现正确、可维护且经形式验证的代码](https://lean-lang.org/)

**原文标题**: [Lean enables correct, maintainable, and formally verified code](https://lean-lang.org/)

Lean 是一款开源编程语言和证明助手，能够帮助开发者编写正确、可维护且经过形式化验证的代码，广泛应用于数学研究、软件验证和自动化证明等领域。

- 🧠 提供强大的自动化工具（如 Grind），可高效处理复杂模式匹配、线性不等式求解及数学归纳证明
- 🔢 内置数学库（Mathlib）涵盖代数、分析、拓扑等领域的百万行形式化数学内容
- 🛡️ 通过最小化可信内核确保数学证明与软件验证的绝对正确性
- 🔧 支持元编程和领域特定扩展，允许用户自定义符号和证明策略
- 🌐 应用于前沿研究（如费马大定理形式化）和工业验证（如 AWS Cedar 权限系统、Google DeepMind AlphaProof）
- 🤝 促进跨领域协作，数学家、工程师和研究人员可共同构建可验证系统
- 📚 提供完整学习路径和社区资源，支持从基础到高级的验证开发

---

### [Rspack 1.5 版本发布 - Rspack](https://rspack.rs/blog/announcing-1-5)

**原文标题**: [Announcing Rspack 1.5 - Rspack](https://rspack.rs/blog/announcing-1-5)

Rspack 1.5 版本发布，带来多项性能优化和新功能，包括实验性 Barrel 文件优化、原生文件监听器、浏览器环境支持、Rust 扩展能力等，同时提升了安装包体积和构建阶段性能，并宣布了相关生态工具更新。

- 🚀 **Barrel 文件优化**：实验性功能 lazyBarrel 可延迟构建 Barrel 文件的重新导出，显著减少模块解析和构建开销，提升构建性能。
- ⚡ **更快的文件监听器**：基于 Rust 的原生文件系统监听器，HMR 性能提升高达 50%，支持增量更新和持续运行。
- 🌐 **浏览器环境支持**：推出 @rspack/browser，可在纯浏览器环境中运行 Rspack，支持在线打包和交互式演示。
- 🦀 **Rust 扩展支持**：允许使用 Rust 编写自定义插件和加载器，直接集成到 Rspack 核心，提升性能并保持 API 兼容性。
- 📦 **常量内联优化**：实验性功能 inlineConst 和 inlineEnum 实现跨模块常量内联，帮助压缩工具更精确地消除未使用代码。
- 🔍 **类型重新导出分析**：改进 TypeScript 类型重新导出的检测，避免误报警告，提升类型处理准确性。
- 🧩 **内置虚拟模块插件**：新增高性能 VirtualModulesPlugin，减少虚拟模块的读取和解析开销，兼容 webpack-virtual-modules API。
- 📉 **安装包体积优化**：通过多项优化措施，将安装包体积从 63.7MB 降至 49.9MB，并集成自动化体积检查。
- ⏱️ **Seal 阶段性能优化**：通过数据结构改进、并行化和热代码缓存，大幅提升大型项目的代码生成和优化效率。
- 🔧 **弃用 Node.js 16 支持**：停止对 Node.js 16 的支持，要求升级至 Node.js 18.12.0 或更高版本。
- 📚 **生态工具更新**：包括 Rslint 发布、Rsbuild 1.5 默认启用多项优化、Rslib 0.12 集成 Rstest、Rspress 2.0 Beta 新增 Markdown 复制功能等。

---

### [Angular 2025夏季更新。作者：延斯·库勒斯、马克·泰克森 | Angular官方 | 2025年8月 | Angular博客](https://blog.angular.dev/angular-summer-update-2025-1987592a0b42?gi=15f13c07ad84)

**原文标题**: [Angular Summer Update 2025. Authors: Jens Kuehlers Mark Techson | by Angular | Aug, 2025 | Angular Blog](https://blog.angular.dev/angular-summer-update-2025-1987592a0b42?gi=15f13c07ad84)

Angular 2025夏季更新带来多项重要功能发布和优化，涵盖无zone变更检测、动画增强、AI开发工具集成以及调试体验提升等方面。

- 🎉 无zone变更检测正式稳定，可通过provideZonelessChangeDetection配置启用
- ✨ 新增animate.enter/leave原生动画API，支持CSS动画和第三方动画库
- 🤖 强化AI开发生态，推出angular.dev/ai资源站和MCP服务器辅助代码生成
- 🔧 模板编写体验优化：支持@else if别名、Tailwind类名和更宽松的@语法
- 📊 DevTools新增路由可视化功能和信号依赖图调试工具
- 🧪 测试改进：TestBed.createComponent支持直接传入绑定对象，无需包装组件
- 🎪 MatMenu新增上下文菜单功能，NgComponentOutlet支持自定义环境注入器
- 📚 文档全面升级，新增路由指南并支持TypeScript 5.9
- 📅 宣布将于2025年9月16日举办Angular AI主题线上活动

---

