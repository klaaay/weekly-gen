### [React 文摘：电子邮件通讯](https://reactdigest.net/)

**原文标题**: [React Digest: Email Newsletter](https://reactdigest.net/)

《React Digest》是一份面向 React 开发者精心筛选的周更简报，汇集前端开发领域优质内容，帮助开发者高效获取行业新知。

- 📮 每周为 22,627+ 前端工程师推送精选文章与摘要
- ⏱️ 节省筛选有价值内容的时间成本
- 🌱 每周持续学习 React 生态新知识
- 💬 用户评价认可内容质量和实用性（含并发模式等深度解析）
- 🌍 服务全球前端开发者社群的权威资讯平台

---

### [React 默认胜出——而这正扼杀前端创新 | 洛伦·斯图尔特](https://www.lorenstew.art/blog/react-won-by-default/)

**原文标题**: [React Won by Default – And It's Killing Frontend Innovation | Loren Stewart](https://www.lorenstew.art/blog/react-won-by-default/)

React 凭借默认选择而非技术优势主导前端生态，抑制了 Svelte、Solid、Qwik 等创新框架的发展，导致技术决策依赖网络效应而非实际需求，最终阻碍整体前端创新。

- 🚫 React 因生态惯性成为默认选择，而非技术优势
- ⚡ Svelte 通过编译时优化实现更小体积和更快性能（如案例从 187KB 降至 9KB）
- 🎯 Solid 采用细粒度响应式更新，性能可达 React 的 2-3 倍
- ⏱️ Qwik 通过可恢复性设计实现即时启动，适合大型应用
- 🔄 React 的虚拟 DOM 和 Hooks 引入运行时开销与复杂性
- 🌐 技术垄断导致人才市场单一化，抑制技能多样性
- 📉 默认选择造成机会成本，创新方案难以获得公平评估
- 💡 建议根据项目需求主动评估框架，打破默认选择惯性

---

### [客户 | 德文](https://devin.ai/customers?utm_medium=newsletter&utm_source=bonobos-react-digest&utm_campaign=20250919)

**原文标题**: [Customers | Devin](https://devin.ai/customers?utm_medium=newsletter&utm_source=bonobos-react-digest&utm_campaign=20250919)

Nubank 通过使用 Devin 人工智能工具，成功将原本需要 18 个月、涉及千名工程师的 ETL 系统重构项目大幅加速，实现了工程效率提升和成本节约。

- 🚀 工程效率提升 8-12 倍，迁移成本降低 20 倍以上
- ⚙️ 将 800 万行代码的单体 ETL 系统拆分为子模块，解决依赖混乱和扩展瓶颈
- 🤖 通过 Devin 自主学习处理重复性迁移任务，单任务时间从 40 分钟缩短至 10 分钟
- 📊 数据、风控等多个业务单元在数周内完成原本需要数月甚至数年的迁移工作
- 💡 工程师只需审核 Devin 的代码变更，大幅减少人工操作和错误率
- 🌱 为公司释放工程资源，专注于新业务开发和价值创造

---

### [React Router 中的中间件 | Remix](https://remix.run/blog/middleware)

**原文标题**: [Middleware in React Router | Remix](https://remix.run/blog/middleware)

React Router 7.9.0 版本通过 future.v8_middleware 标志正式稳定了中间件功能，解决了嵌套路由中数据加载的并行限制问题，允许顺序逻辑处理和短路操作，提升了开发体验和性能。

- 🎉 React Router 7.9.0 稳定推出中间件功能，通过 future.v8_middleware 标志启用
- 🔄 解决了嵌套路由中 loader 并行运行无法共享数据或短路的问题
- 🛠️ 中间件允许顺序执行逻辑，支持数据传递和提前重定向
- 📦 依赖 Single Fetch 架构实现请求上下文共享，减少数据库调用
- 🧪 经过社区 alpha 测试迭代，API 现已稳定
- 💡 常见用例包括认证检查、日志记录和响应头设置
- 📚 提供详细文档和示例，支持开发者探索新模式

---

### [styled-components 维护模式：速度提升 40% 的分支 | Sanity](https://www.sanity.io/blog/cut-styled-components-into-pieces-this-is-our-last-resort)

**原文标题**: [styled-components maintenance mode: A 40% faster fork | Sanity](https://www.sanity.io/blog/cut-styled-components-into-pieces-this-is-our-last-resort)

文章概述了人工智能在医疗领域的应用现状与未来趋势，重点分析了技术优势、现存挑战和伦理考量。

- 🤖 医疗影像诊断准确率提升至 95% 以上，大幅降低漏诊率
- ⚕️ 手术机器人实现微创精准操作，缩短患者康复时间
- 📊 基于大数据的个性化治疗方案制定效率提高 40%
- 🔒 患者隐私保护与数据安全成为行业重点关注问题
- 🌐 远程医疗系统突破地域限制，惠及农村地区医疗资源
- ⚠️ 算法偏见和医疗责任认定等伦理问题亟待解决
- 💊 新药研发周期从 5 年缩短至 2 年，降低研发成本
- 🏥 智慧医院管理系统优化就诊流程，减少候诊时间 30%

---

### [React Server Components (RSCs) 跨框架与库支持](https://rsc.krasimirtsonev.com/)

**原文标题**: [React Server Components (RSCs) support across frameworks and libraries](https://rsc.krasimirtsonev.com/)

多个 React 框架已支持 React Server Components（RSCs），其中 Next.js、Vite 和 Waku 实现 12 项测试用例的 100% 覆盖，Forket、Parcel、ReactRouter 和 RedwoodSDK 覆盖率达 83%。测试涵盖服务端异步组件渲染、混合组件使用、客户端水合及服务函数传递等核心场景。

- 🚀 Next.js、Vite 和 Waku 全面支持 12 项 RSC 功能测试
- ⚡ 服务端异步渲染和混合组件为基础核心功能
- 🔄 客户端组件水合与服务函数传递实现无缝交互
- 🧪 嵌套客户端组件和内联服务动作为高阶测试项
- 📦 Forket 等四款工具支持 10 项功能（83% 覆盖率）
- 💡 测试案例包含灵感生成器、音乐播放器等实际应用
- 🔧 支持表单操作、状态管理与服务端上下文访问

---

### [迁移至 TanStack Start](https://catalins.tech/migrating-to-tanstack-start/)

**原文标题**: [Migrating to TanStack Start](https://catalins.tech/migrating-to-tanstack-start/)

作者从全栈 React 框架转向客户端 - 服务器分离架构，但发现 SPA 缺乏 SSR 影响 SEO，最终选择迁移至 TanStack Start 实现选择性服务端渲染。

- 🚀 技术栈采用前后端分离：后端 Hono+Bun+PostgreSQL，前端 React+Vite+TypeScript
- 🔍 SEO 需求驱动迁移：课程平台需被搜索引擎收录核心页面（课程/作者/标签页）
- ⚖️ 评估两种方案：Astro 静态站点（需维护新应用）和 TanStack Router SSR（配置复杂）
- 🛠️ 迁移核心改动：路由文件重构、根路由集成服务端认证、Vite 配置替换插件
- 🧩 关键技术调整：认证客户端增加 baseURL 配置、Hono RPC 需显式传递 cookie 凭证
- 📌 待完成事项：按需认证获取、主题提供商适配、环境变量替换硬编码地址
- 🔗 迁移过程公开：提供 PR 链接供参考，并邀请读者支持创作

---

### [我们能用角落形状做什么？| CSS-Tricks](https://css-tricks.com/what-can-we-actually-do-with-corner-shape/)

**原文标题**: [What Can We Actually Do With corner-shape? | CSS-Tricks](https://css-tricks.com/what-can-we-actually-do-with-corner-shape/)

CSS corner-shape 属性为 border-radius 带来全新形状控制能力，目前仅 Chrome 139+ 支持，可与 border-radius 配合创造多种视觉特效。

- 🎨 斜角效果：使用 corner-shape: bevel 实现流行的剪角设计，搭配 border-radius 控制尺寸
- 🔺 倾斜区块：通过设置不同轴向值 (如 100% 50px) 创建动态斜切效果
- 🏷️ 促销标签：组合 round 和 bevel 值 (corner-shape: round bevel bevel round) 实现专业标签形状
- ➡️ 箭头导航：利用 bevel 形状和负边距创建连贯的箭头式面包屑导航
- 💬 工具提示：使用 corner-shape: scoop 配合锚点定位实现带凹陷效果的弹出框
- 🖍️ 荧光笔效果：squircle bevel 组合与不规则 border-radius 模拟手写高亮
- 📱 应用图标：squircle 单独使用可创建类似 iOS 的圆润图标造型
- ✂️ 背景裁剪：notch 值配合 50% 轴向设置可实现精准背景裁剪
- ⚠️ 边框限制：目前边框和轮廓在这些形状上显示效果仍不稳定

---

### [苹果拥有私有 CSS 属性，可为网页内容添加液态玻璃效果](https://alastair.is/apple-has-a-private-css-property-to-add-liquid-glass-effects-to-web-content/)

**原文标题**: [Apple has a private CSS property to add Liquid Glass effects to web content](https://alastair.is/apple-has-a-private-css-property-to-add-liquid-glass-effects-to-web-content/)

苹果在 WebKit 中开发了一个私有 CSS 属性，允许在 Web 内容中实现类似 iOS 系统的液态玻璃视觉效果，但目前仅限于内部使用，无法在公开的网页或通过 App Store 审核的应用中部署。

- 🔍 作者通过监测 WebKit 代码库发现苹果新增了私有 CSS 属性`-apple-visual-effect`，支持系统级模糊和玻璃材质效果
- 🚫 该功能无法在 Safari 浏览器中直接使用，且需要启用 WKWebView 的私有设置`useSystemAppearance`才会生效
- ⚠️ 若开发者强行启用该私有属性，应用将无法通过 App Store 审核流程
- 💡 通过`@supports`条件 CSS 可优雅实现兼容方案：支持时采用玻璃效果，否则回退到半透明背景
- 🧠 作者提出"假发理论"：优秀的 WebView 集成往往难以被用户察觉，暗示苹果可能已在某些系统组件中秘密使用此技术
- 🔮 该发现揭示了原生与 Web 技术融合的新方向，虽当前受限但具有未来生态整合的指示意义

---

### [不要继承盒模型 | OddBird](https://www.oddbird.net/2025/09/04/box-model/)

**原文标题**: [Don't Inherit the Box Model | OddBird](https://www.oddbird.net/2025/09/04/box-model/)

CSS 中不应继承盒模型设置，而应直接全局应用 border-box，并仅在需要时局部调整 content-box。

- 📦 全局设置`* { box-sizing: border-box; }`优于通过 html 根元素继承的方式
- 🚫 盒模型属性（如 border/padding）本身不应继承，这与文本属性（如 color/font）不同
- ⚙️ content-box 在现代布局中仍有实用价值，特别是在控制内容尺寸时
- 🧩 伪元素 (::before/::after) 默认不应改变盒模型，按需单独设置
- 🔧 继承盒模型会导致代码冗余，且解决的是几乎不存在的遗留组件问题

---

### [一统江湖的榜单 · 2025 年 9 月 10 日](https://nerdy.dev/cascading-secret-sauce)

**原文标题**: [One List To Rule Them All · September 10, 2025](https://nerdy.dev/cascading-secret-sauce)

这份资源为 CSS 学习者提供了全面的新特性索引，涵盖选择器、函数、属性等核心内容，帮助开发者系统化地跟进现代 CSS 技术发展。

- 📚 包含选择器、伪元素、@规则、颜色函数等 CSS 核心模块更新
- 🔍 提供每个特性的详细文档链接，方便深入学习
- 📱 新增容器查询、视口单位等响应式设计相关功能
- 🎨 引入 OKLCH 等现代色彩空间和颜色混合函数
- ⚡ 减少 JavaScript 依赖，增强原生 CSS 交互能力
- 🌐 涵盖国际化和可访问性相关特性（如语言伪类）
- 📊 新增数学函数和动画控制等高级功能
- 🔗 社区积极参与，提供反馈和建议渠道

---

### [Wasm 3.0 完成 - WebAssembly](https://webassembly.org/news/2025-09-17-wasm-3.0/)

**原文标题**: [Wasm 3.0 Completed - WebAssembly](https://webassembly.org/news/2025-09-17-wasm-3.0/)

WebAssembly 3.0 标准正式发布，引入多项重大功能升级，包括 64 位地址空间、多内存支持、垃圾回收、异常处理等，显著提升了对高级编程语言的支持，并已在主流浏览器中实现。

- 🌐 64 位地址空间：内存和表格现支持 i64 地址类型，理论寻址空间达 16EB，非 Web 生态可支持更大应用
- 🧠 多内存支持：单个模块可声明和访问多个内存空间，支持直接数据拷贝，提升静态链接工具兼容性
- ♻️ 垃圾回收：新增 GC 托管存储，支持结构体/数组类型和未装箱整型，为编译器提供内存管理基础能力
- 🔗 类型化引用：扩展类型系统支持精确堆值描述，减少运行时检查，支持安全间接函数调用
- 📞 尾调用优化：支持静态/动态调用，避免栈空间占用，满足函数式语言和内部实现需求
- 🚨 异常处理：原生支持异常标签声明和捕获机制，解决此前依赖宿主语言的低效问题
- ⚡ 宽松向量指令：新增允许平台相关行为的松弛指令变体以最大化性能
- 🎯 确定性执行模式：为浮点运算和松弛指令指定确定性行为，满足区块链等场景需求
- 📝 自定义注解语法：文本格式支持通用注解语法，支持人类可读写的自定义段信息
- 📎 JS 字符串内置库：JS API 扩展支持在 Wasm 中直接操作外部字符串值
- 🚀 多语言支持：Java/OCaml 等新语言利用 GC 特性 targeting Wasm
- 🔧 规范工具升级：首次采用 SpecTec 工具链生成更可靠的规范标准

---

### [获取流虽好，但不适用于衡量上传/下载进度 - JakeArchibald.com](https://jakearchibald.com/2025/fetch-streams-not-for-progress/)

**原文标题**: [Fetch streams are great, but not for measuring upload/download progress - JakeArchibald.com](https://jakearchibald.com/2025/fetch-streams-not-for-progress/)

本文讨论了 fetch 流在测量上传/下载进度方面的局限性，指出其可能产生不准确结果并影响浏览器性能优化，同时介绍了替代方案和未来 API 改进方向。

- 🌐 Fetch 流虽可用于实时数据处理，但不适合精确测量上传/下载进度
- ⚠️ 使用流测量进度会导致数据偏差（如压缩内容长度计算错误）
- 📦 请求流适用于并行处理（如视频转码 + 上传），但进度测量仅反映数据移交时刻而非实际传输完成
- 🔄 浏览器流缓冲机制（high water mark）可能导致进度显示与真实网络传输不同步
- 📊 当前推荐使用 XHR 的 onprogress 事件获取准确进度
- 🚀 未来将通过 fetch Observer API 提供原生进度支持（正在标准化进程中）
- 🔗 开发者可通过 Interop 2026 提案参与功能规划

---

### [Bun 安装幕后花絮 | Bun 博客](https://bun.com/blog/behind-the-scenes-of-bun-install)

**原文标题**: [Behind The Scenes of Bun Install | Bun Blog](https://bun.com/blog/behind-the-scenes-of-bun-install)

Bun 包管理器通过系统级优化实现极速安装，比 npm 快约 7 倍、pnpm 快 4 倍、yarn 快 17 倍，尤其在大代码库中优势显著。

- 🚀 **系统调用最小化**：Bun 将包安装视为系统编程问题，通过直接系统调用（而非 Node.js 的线程池和事件循环）减少模式切换开销，避免每秒数十亿次 CPU 周期浪费。
- ⚡️ **二进制清单缓存**：将 JSON 格式的包元数据转换为二进制存储，消除重复解析和字符串冗余，缓存安装速度比 npm 快 39 倍。
- 🗜️ **预分配内存解压**：下载完整压缩包后读取 gzip 末 4 字节获取解压大小，预分配内存避免多次拷贝，配合 libdeflate 高速解压。
- 🧠 **缓存友好数据布局**：采用结构数组（SoA）替代传统对象嵌套，数据连续存储提升 CPU 缓存命中率，减少内存随机访问延迟。
- 📑 **优化锁文件格式**：使用扁平化锁文件结构减少 JSON 解析深度，支持依赖顺序存储和预分配内存，提升解析效率。
- 💾 **系统原生文件复制**：macOS 使用 `clonefile()` 实现写时复制，Linux 优先采用硬链接或 `copy_file_range`，减少数据复制和系统调用次数。
- 🔄 **多核并行处理**：基于 Zig 的本地线程池自动扩展至所有 CPU 核心，采用无锁数据结构和线程独立内存池，最大化并行 I/O 和计算。
- 🌐 **异步 DNS 解析**：macOS 上使用原生异步 DNS API 提前解析域名，避免线程阻塞，网络请求与依赖分析并行。
- 📊 **实测性能优势**：Bun 仅需 16.5 万次系统调用（yarn 为 404 万），且 futex 同步调用占比仅 0.46%，极大减少线程等待开销。

---

### [如何控制 package.json | Val Town 博客](https://blog.val.town/gardening-dependencies)

**原文标题**: [How to keep package.json under control | Val Town Blog](https://blog.val.town/gardening-dependencies)

本文讨论了如何有效管理项目中的依赖项，强调在复杂项目中依赖不可避免，但可通过策略控制其影响。

- 📖 阅读新依赖的源码和文档，避免引入冗余代码，仅信任如 React 等大型依赖
- 🔍 利用 npm ls 或 pnpm why 等工具分析依赖树，识别可复用的间接依赖以减少体积
- 📊 使用 Grand Perspective 等工具分析 node_modules 磁盘占用，并通过打包分析器优化应用体积
- ✅ 选择维护良好、有类型定义和测试的模块，避免解决错误问题的依赖
- 🔄 用 Renovate 定期更新依赖，用 Knip 删除未使用的模块和文件
- 👥 关注优质模块作者（如 Sindre Sorhus），建立可信依赖清单
- 🌐 承认依赖是开发生态的必要部分，需持续维护而非完全避免

---

### [TanStack DB 交互式指南 | 大规模前端实践](https://frontendatscale.com/blog/tanstack-db/)

**原文标题**: [An Interactive Guide to TanStack DB | Frontend at Scale](https://frontendatscale.com/blog/tanstack-db/)

家庭待办事项提醒，包括与家人保持联系、规划度假和准备生日礼物。

- 📞 给妈妈打电话
- ✈️ 安排夏季旅行计划
- 🎁 购买生日礼物

---

### [编程文摘：电子邮件通讯](https://programmingdigest.net/?utm_source=web-archive&utm_campaign=react)

**原文标题**: [Programming Digest: Email Newsletter](https://programmingdigest.net/?utm_source=web-archive&utm_campaign=react)

这是一份为软件工程师精选的每周技术简报，提供高质量内容以节省读者时间并促进持续学习。

- 📧 每周邮件推送，已吸引超过 21,241 名软件工程师订阅
- 🔍 精选文章附简短摘要，节省筛选内容时间
- 🌱 每周持续学习新知识，获得用户积极反馈
- 🏢 由 Bonobo Press 运营，服务涵盖 2013-2025 年
- 👥 读者群体涵盖全球知名科技企业和高校开发者

---

### [科技领导力：电子邮件通讯](https://leadershipintech.com/?utm_source=web-archive&utm_campaign=react)

**原文标题**: [Leadership in Tech: Email Newsletter](https://leadershipintech.com/?utm_source=web-archive&utm_campaign=react)

一份面向技术领导者的精选周报，帮助 CTO、工程经理和高级工程师提升领导力。  
- 📧 超过 27,672 名工程领导者订阅每周邮件  
- 📖 精选文章附简短摘要，节省寻找优质内容的时间  
- 🌱 每周学习新知识，涵盖架构讨论、会议规划和沟通等主题  
- ❤️ 读者好评：内容精准实用，尤其赞赏关于授权技能的文章  
- 🌍 受到全球科技行业领导者阅读

---

### [C#文摘：电子邮件通讯](https://csharpdigest.net/?utm_source=web-archive&utm_campaign=react)

**原文标题**: [C# Digest: Email Newsletter](https://csharpdigest.net/?utm_source=web-archive&utm_campaign=react)

C# Digest 是一份专为.NET 开发者精心策划的周更简报，旨在通过筛选优质内容帮助开发者高效学习新知识。  
- 📧 拥有19,832+名C#工程师订阅的邮件列表  
- 🔍 每周推送含摘要的手选文章，节省信息筛选时间  
- 🚀 包含实用技术内容（如特性开关、LINQ、DiagnosticListener）  
- 💡 读者反馈证实内容具有工作实践价值  
- 🌐 服务全球.NET 工程师，由 Bonobo Press 运营

---

### [让开发者与时俱进——Bonobo 出版社](https://bonobopress.com/)

**原文标题**: [Keeping developers up to date â Bonobo Press](https://bonobopress.com/)

Bonobo Press 是一家自 2013 年起为软件开发者和技术专业人士提供新闻通讯服务的平台，拥有超过 88,000 名订阅用户，涵盖开发者、IT 专家及技术决策者群体。

- 📧 提供每周精选技术通讯，服务对象包括开发者、工程经理、技术主管和 CTO，以简洁高效节省时间著称
- 📢 支持广告投放，可精准触达软件工程师、团队领导、技术决策者等专业受众
- 📞 提供咨询、建议及广告合作联系渠道，可通过网站获取媒体资料并建立合作

---

### [往期通讯：第 1 页](https://reactdigest.net/newsletters)

**原文标题**: [Past Newsletters: Page 1](https://reactdigest.net/newsletters)

React Digest 是一份专注于 React 生态的技术简报，涵盖框架演进、性能优化、新特性解析及最佳实践，内容涉及状态管理、路由、服务端组件和并发特性等核心主题。

- 🏆 React 的统治地位可能抑制创新，同时探讨了 React Router 的新中间件和样式组件的性能问题
- 🛠️ 介绍了无框架实现 React Server Components 支持的方法及 React 19 的 Activity 组件
- ⚡ 深入分析了并发特性、缓存一致性策略以及使用 Web Workers 提升性能的方案
- 🧩 涵盖状态管理库（Zustand/TanStack）实践、模块联邦架构和手势识别等前沿应用
- 📊 持续关注渲染优化、数据获取架构和 TypeScript 集成等生产级解决方案
- 🔍 通过历史代码追溯 React 演进，并讨论微模块化哲学与 AI 辅助开发趋势

---

### [隐私](https://reactdigest.net/privacy)

**原文标题**: [Privacy](https://reactdigest.net/privacy)

我们高度重视用户隐私，制定了明确的隐私政策以确保个人信息得到妥善保护。我们仅收集必要信息用于指定目的，并采取严格安全措施保障数据安全，同时为用户提供信息查询和删除的渠道。

- 📧 仅收集邮箱地址用于发送周刊，绝不用于其他目的或垃圾邮件
- 🎯 信息收集前明确用途，仅用于实现指定目标或法律要求的兼容用途  
- ⏱️ 个人信息仅保留至实现目的所需的最短期限
- 🔒 通过合法公平方式收集信息，并采取合理安全措施防止数据泄露或滥用
- 📋 确保个人信息准确完整，并及时更新以符合使用目的
- 👶 严格遵守 COPPA 法案，不收集或存储 13 岁以下儿童信息
- 📬 用户可邮件联系[email protected]查询或删除个人数据
- 🚫 强烈反对垃圾邮件，提供每封邮件中的退订链接

---

### [媒体资料包 - Bonobo 出版社](https://bonobopress.com/media-kit/)

**原文标题**: [Media Kit â Bonobo Press](https://bonobopress.com/media-kit/)

Bonobo Press 是一家专注于为程序员和技术人员提供最新趋势、工具和技术资讯的媒体平台，通过精心策划的周报吸引高度参与的目标受众，并为广告商提供精准的广告投放服务。

- 📧 平台运营四份技术周报：Leadership in Tech（领导力技术）、Programming Digest（编程文摘）、C# Digest（C#文摘）和React Digest（React 文摘），覆盖不同技术领域和职位层级
- 👥 受众主要为欧美地区的技术决策者、工程师和管理人员，就职于谷歌、亚马逊等各类企业
- 📊 所有周报的打开率和点击率均高于行业基准，其中 C# Digest 点击率最高达 21.63%
- 💰 广告报价因周报而异，单期价格从 875 美元到 1940 美元不等，CPC 成本在 1.95-5.83 美元之间
- 📝 广告格式为纯文本，需包含链接、标题和描述，截止日期为发布前 4 天
- 🤝 合作流程包括需求沟通、档期确认、付款锁定、内容优化和效果报告
- ✅ 已服务 Okta、GitLab、MongoDB 等多家知名技术企业，重复合作率高

---

