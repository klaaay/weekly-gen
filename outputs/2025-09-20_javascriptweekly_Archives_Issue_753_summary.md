### [JavaScript 周刊第753期：2025年9月19日](https://javascriptweekly.com/issues/753)

**原文标题**: [JavaScript Weekly Issue 753: September 19, 2025](https://javascriptweekly.com/issues/753)

npm生态系统面临名为“Shai-Hulud”的供应链攻击，涉及数百个恶意软件包窃取开发者令牌；同时出现工具更新、框架发布及社区倡议，如Deno筹款挑战JavaScript商标权，反映了JavaScript生态的安全与创新动态。

- 🐛 npm生态系统遭受“Shai-Hulud”供应链攻击，数百个包被植入恶意代码以窃取开发者令牌和机密信息
- 🛠️ pnpm 10.16发布新功能，支持延迟依赖更新以防范供应链攻击；多款工具和框架（如Bun、React Router）推出更新
- ⚖️ Deno发起筹款20万美元，旨在挑战Oracle对JavaScript商标的所有权
- 🌐 WebAssembly 3.0标准正式发布，增强与JavaScript的互操作性，支持垃圾回收和异常处理等功能
- 📦 多个JavaScript工具和库更新，包括Expo SDK 54、TypeBox 1.0等，聚焦性能提升和开发体验优化
- 🔒 文章讨论Fetch流进度测量局限性和TypeScript迁移案例，同时推广Auth0等安全解决方案
- 💡 社区观点碰撞：React主导地位被指抑制前端创新，而Solid.js等框架引发替代方案讨论
- 📚 资源推荐涵盖离线文档、媒体播放器插件系统及版本号探索等实用内容

---

### [获取失败](https://javascriptweekly.com/link/174584/web)

**原文标题**: [Failed to retrieve](https://javascriptweekly.com/link/174584/web)

无法总结：获取内容失败，状态码 403。

---

### [沙虫（沙丘） - 维基百科](https://en.wikipedia.org/wiki/Sandworm_(Dune))

**原文标题**: [Sandworm (Dune) - Wikipedia](https://en.wikipedia.org/wiki/Sandworm_(Dune))

沙虫是弗兰克·赫伯特在《沙丘》系列中创造的虚构外星生物，栖息于沙漠星球阿拉基斯，被弗里曼人尊称为“沙虫之神”（Shai-Hulud）。它们是香料（melange）的来源，而香料是宇宙中最珍贵的资源，能延长寿命、增强意识并实现星际航行。沙虫具有极强的攻击性和领地意识，会被有节奏的振动吸引。其生命周期从微小的沙浮游生物开始，经历沙鳟（sandtrout）阶段，最终成长为巨型的沙虫。沙虫在文化和生态上对《沙丘》宇宙至关重要，影响了从采矿到宗教仪式的各个方面。

- 🪱 沙虫是《沙丘》系列中的巨型外星生物，栖息于沙漠星球阿拉基斯，被弗里曼人尊为“沙虫之神”。
- 🌌 沙虫幼虫产生的香料（melange）是宇宙中最珍贵的资源，能实现星际航行、延长寿命并增强意识。
- ⚠️ 沙虫具有攻击性和领地意识，会被有节奏的振动吸引，对香料开采构成巨大威胁。
- 🔄 沙虫的生命周期从沙浮游生物开始，经历沙鳟阶段，最终成长为巨型沙虫；水对成年沙虫有毒。
- 🏜️ 沙虫在生态上塑造了阿拉基斯的沙漠环境，并通过香料生产影响了整个宇宙的政治和经济。
- 🧑🤝🧑 弗里曼人与沙虫有独特的关系，包括使用钩子骑乘沙虫的成人仪式，以及用沙虫牙齿制作神圣的晶牙匕。
- 🎬 沙虫在多个《沙丘》改编影视和游戏中出现，成为系列的标志性元素，设计历经多次演变。

---

### [pnpm 10.16 | pnpm](https://pnpm.io/blog/releases/10.16)

**原文标题**: [pnpm 10.16 | pnpm](https://pnpm.io/blog/releases/10.16)

pnpm 10.16版本引入了新的安全设置和高级依赖过滤功能，同时包含多项修复和改进。

- ⏳ 新增minimumReleaseAge设置，可延迟安装新发布的依赖包以降低安全风险
- 📋 支持通过minimumReleaseAgeExclude设置排除特定依赖的延迟安装限制
- 🔍 新增finder函数功能，支持按依赖属性进行高级搜索
- 📝 finder函数可返回附加信息（如许可证详情）增强输出内容
- 🐛 修复了Node.js 24下的弃用警告显示问题
- ⚠️ 对nodeVersion设置增加精确版本号校验
- 📦 改进pnpm publish命令支持发布.tar.gz格式文件
- ⌨️ 优化Ctrl-C取消进程时的非零退出码返回机制

---

### [缓解供应链攻击 | pnpm](https://pnpm.io/supply-chain-security)

**原文标题**: [Mitigating supply chain attacks | pnpm](https://pnpm.io/supply-chain-security)

npm包供应链攻击的缓解措施概述：通过禁用依赖项安装脚本、延迟更新依赖版本、锁定依赖文件等方式降低恶意软件安装风险。

- 🛡️ pnpm v10默认禁用依赖项的postinstall脚本自动执行，防止恶意代码立即运行
- ⚠️ 可通过dangerouslyAllowAllBuilds设置全局重新启用，但建议仅显式信任特定依赖
- ⏰ 使用minimumReleaseAge设置延迟安装新版本（如1440分钟=24小时），利用恶意软件通常被快速发现的特点
- 🔒 始终使用lockfile锁定依赖版本并提交到代码仓库，避免意外更新
- 🔍 推荐使用Socket、Snyk、Aikido等工具早期检测被篡改的软件包

---

### [糟糕，又来了……关于NPM供应链攻击的思考 - 现代Web开发教程](https://tane.dev/2025/09/oh-no-not-again...-a-meditation-on-npm-supply-chain-attacks/)

**原文标题**: [Oh no, not again... a meditation on NPM supply chain attacks - Development tutorials for modern web development](https://tane.dev/2025/09/oh-no-not-again...-a-meditation-on-npm-supply-chain-attacks/)

作者回顾了NPM供应链攻击的历史与现状，指出微软在收购NPM后未能有效解决安全问题，并警告当前软件生态存在严重脆弱性。

- 🚨 微软因长期忽视NPM安全漏洞被视作威胁源
- 📦 NPM成为恶意软件传播的主要渠道，攻击目标从加密货币扩展到核心凭证
- 🌐 以IE浏览器历史类比微软对安全问题的放任态度
- ⚠️ 2017年已发现npx工具和postinstall脚本的安全风险
- 💸 微软通过收购GitHub掌控NPM生态但未加强安全措施
- 🤖 AI技术可能被用于制造更复杂的供应链攻击
- 🔐 呼吁企业重新评估软件供应链安全性

---

### [不会发生的JavaScript更美好未来](https://drewdevault.com/2025/09/17/2025-09-17-An-impossible-future-for-JS.html)

**原文标题**: [A better future for JavaScript that won't happen](https://drewdevault.com/2025/09/17/2025-09-17-An-impossible-future-for-JS.html)

在经历了史上最大规模供应链攻击后，JavaScript生态系统可能迎来反思与变革的契机，但现实更可能延续既有模式。

- 🚨 供应链攻击暴露依赖管理机制存在根本性设计缺陷
- ⚠️ 长期存在的微库依赖树结构被指存在安全隐患
- 🌐 业界呼吁建立基于信任关系的软件分发体系
- 📚 期待谷歌和Mozilla推动JavaScript标准库开发
- 🔄 建议整合微库为具有完整功能的大型软件包
- 💰 呼吁微软等巨头投入资源重构npm包管理体系
- 🔐 建议采用Linux发行版的包管理安全实践
- ⚠️ 警告PyPI/RubyGems等生态存在同样风险
- 📉 预测实际变革有限，仅会有象征性安全措施
- 🔁 指出软件行业数十年未从安全事件中吸取教训

---

### [助力Deno筹集20万美元，让JavaScript摆脱Oracle束缚](https://deno.com/blog/javascript-tm-gofundme)

**原文标题**: [Help Us Raise $200k to Free JavaScript from Oracle | Deno](https://deno.com/blog/javascript-tm-gofundme)

Deno组织发起法律行动，旨在通过美国专利商标局撤销Oracle对"JavaScript"商标的所有权，目前进入关键证据收集阶段，并发起众筹以支付诉讼费用。

- 🚨 已向美国专利商标局提交撤销商标申请，案件进入关键证据发现阶段
- 💸 发起20万美元众筹，用于支付专家证人、法律文件及市场调研等诉讼成本
- ⚖️ 核心论点为"JavaScript"已成为通用术语，Oracle与语言发展无关却滥用商标权
- 📜 若败诉，Oracle将永久获得商标权，恐开创有害先例
- 🌐 胜诉将使"JavaScript"成为公共领域词汇，保障开发者自由使用
- 🔄 剩余资金将捐赠给OpenJS基金会，不会流向Deno组织自身
- ✍️ 呼吁开发者阅读请愿书并通过捐款/转发支持维权行动

---

### [JavaScript™](https://javascript.tm/)

**原文标题**: [JavaScript™](https://javascript.tm/)

使用“JavaScript”一词描述工作、产品或会议可能面临法律风险，因为甲骨文公司声称拥有该商标权，尽管其并非创造者或维护者。美国法律规定通用名称不可被垄断，此案旨在保护开发者自由使用该语言的权利。

- 🚨 使用“JavaScript”一词可能涉及法律风险，因甲骨文持有其商标权
- 📜 甲骨文通过收购Sun公司获得商标，但未参与语言开发与维护
- ⚖️ 美国法律明确规定通用术语和已被放弃的商标不可被私有化
- 🌍 本案关乎全球开发者、教育机构和企业能否自由使用JavaScript
- 💰 需要筹集20万美元用于法律取证阶段，包括公众意见调查
- 📮 剩余资金将全额捐赠给电子前沿基金会（EFF）
- 🤝 可通过捐款、签署公开信或社交媒体传播#FreeJavaScript参与支持
- 🦕 倡议方Deno公司作为JavaScript运行时开发商发起此公益诉讼

---

### [Wasm 3.0 完成 - WebAssembly](https://webassembly.org/news/2025-09-17-wasm-3.0/)

**原文标题**: [Wasm 3.0 Completed - WebAssembly](https://webassembly.org/news/2025-09-17-wasm-3.0/)

WebAssembly 3.0 标准正式发布，带来多项重大功能更新，显著提升了对高级编程语言的支持，并已在主流浏览器中开始部署。

- 🚀 64位地址空间：内存和表格现支持i64地址类型，理论寻址空间达16艾字节，非Web生态可处理更大型应用
- 🔗 多内存支持：单个模块可声明和访问多个内存空间，支持直接数据拷贝，提升静态链接工具兼容性
- ♻️ 垃圾回收机制：新增GC功能，支持结构体/数组类型的内存自动管理，为多语言编译提供底层基础
- 🧩 类型化引用：扩展类型系统支持精确堆值描述，新增call_ref指令实现无运行时检查的安全间接调用
- 🔁 尾调用优化：支持静态和动态函数尾调用，节省栈空间，满足函数式语言等场景需求
- 🚨 异常处理：新增原生异常处理机制，支持带标签的异常抛出和捕获，提升编译效率和跨平台一致性
- ⚡ 宽松向量指令：新增松弛型SIMD指令变体，允许在边缘情况下实现硬件优化行为
- 🎯 确定性执行模式：为浮点运算和松弛指令指定确定性行为，满足区块链等场景的可重现需求
- 📝 自定义注解语法：文本格式新增通用注解语法，支持人类可读的自定义元数据表达
- 🌐 JS字符串内置库：JS API扩展支持在Wasm中直接操作JavaScript字符串值
- 📅 工具链升级：首次采用SpecTec工具链生成标准，提升规范可靠性
- 🌍 多语言支持：Java/OCaml/Scala等新语言利用GC特性实现Wasm编译目标
- 🖥️ 生态支持：已登陆主流浏览器，独立引擎（如Wasmtime）支持持续推进

---

### [Evan You 2025访谈：谷歌、Vue、Vite、Nuxt、Next、Vercel与VoidZero - YouTube](https://www.youtube.com/watch?v=FS0Ds0nIC8E)

**原文标题**: [Evan You 2025 Interview: Google, Vue, Vite, Nuxt, Next, Vercel & VoidZero - YouTube](https://www.youtube.com/watch?v=FS0Ds0nIC8E)

YouTube平台提供了全面的用户支持与资源，涵盖服务条款、创作者支持及功能更新等方面。  
- 📄 关于平台介绍与基本信息  
- 📢 媒体与新闻相关资源  
- ©️ 版权政策与法律信息  
- 📞 用户联系与客服渠道  
- 🎬 创作者专属工具与支持  
- 💼 广告合作与商业机会  
- 👨‍💻 开发者资源与API信息  
- 📑 服务条款与使用规范  
- 🔒 隐私保护与数据政策  
- ⚖️ 平台安全与政策指南  
- 🔧 功能测试与更新动态  
- 🏢 公司信息与版权声明（©2025 Google LLC）

---

### [VoidZero | 下一代Web开发工具集](https://voidzero.dev/)

**原文标题**: [VoidZero | Next Generation Tooling for the Web](https://voidzero.dev/)

下一代JavaScript工具链应具备统一性、高性能、可组合性和运行时无关性，通过标准化技术栈和原生级性能优化提升开发体验。
- 🌐 统一性：采用相同AST解析器和模块交互机制，消除不一致性并减少重复解析成本
- ⚡ 高性能：基础组件采用原生编译语言编写，从底层设计追求极致运行效率
- 🧩 可组合性：每个工具链组件都可独立使用，提供高度定制化的构建模块
- 🔄 运行时无关：核心工具链不耦合特定JavaScript运行时，确保跨环境一致性

---

### [仙女座](https://tryandromeda.dev/)

**原文标题**: [Andromeda](https://tryandromeda.dev/)

Andromeda 是一个基于 Rust 构建的现代、快速且安全的 JavaScript 和 TypeScript 运行时，由 Nova 引擎驱动，具备零配置 TypeScript 支持、硬件加速图形和全面的 Web API。

- 🚀 基于 Rust 构建，提供高性能和内存安全保证
- ⚡ 零配置 TypeScript 支持，开箱即用
- 🎨 硬件加速的 2D Canvas API，支持 WGPU 后端
- 🔧 内置完整工具链（LSP、REPL、格式化、打包等）
- 🌐 完全兼容 WinterTC Web 标准
- 🔒 安全沙箱执行环境和权限控制
- 📊 低内存占用（约12MB），启动时间低于10ms
- 🖥️ 支持多平台（Linux、macOS、Windows）
- 📦 内置 SQLite 数据库和加密 API
- 🎯 适用于图形可视化、高性能脚本、Web 服务和科学计算

---

### [GitHub - alshdavid/ion：带正电荷的 JavaScript 运行时](https://github.com/alshdavid/ion)

**原文标题**: [GitHub - alshdavid/ion: A Positively Charged JavaScript Runtime](https://github.com/alshdavid/ion)

Ion.js 是一个基于 Rust 的 JavaScript 运行时，专为在 Rust 程序中嵌入 JavaScript 引擎而设计，适用于插件系统、SSR 服务和 FaaS 等场景。

- ⚡ 提供高级 API，支持多线程和事件循环（基于 Tokio）
- 🛠️ 允许通过解析器、扩展和预处理器自定义运行时功能
- 🔄 支持 Rust 与 JavaScript 相互调用，示例包括函数执行和 Promise 处理
- 🌐 兼容部分 Web API（如定时器和基础 console），但尚未支持 fetch、Worker 等
- 📦 采用分层架构（JsRuntime、JsWorker、JsContext），确保线程安全
- 🚫 区别于 Node.js/Deno/Bun，注重可嵌入性和静态编译，避免依赖复杂分发
- 🔧 技术栈为 Rust + V8 + Tokio，开源且采用 MIT 许可证

---

### [Webflow捐赠15万美元支持Astro的开源使命 | Astro](https://astro.build/blog/webflow-official-partner/)

**原文标题**: [Webflow Donates $150,000 to Support Astro’s Open Source Mission | Astro](https://astro.build/blog/webflow-official-partner/)

Webflow宣布向Astro开源项目捐赠15万美元并达成技术合作，双方将共同推动AI应用开发与无代码平台的深度融合。

- 💰 Webflow向Astro开源项目捐赠15万美元用于长期维护
- 🤝 Webflow选择Astro作为其AI应用生成功能的核心技术
- 🌐 Webflow Cloud平台已支持通过Astro构建动态网站体验
- ⚡ AI生成的Web应用将全部采用Astro框架，确保性能优势
- 🚀 合作将结合可视化建站与代码开发，拓展创意可能性
- 🔧 开发者可通过Webflow AI测试版构建Astro组件和应用
- 📈 资金将直接投入开源项目，保障可持续发展

---

### [Safari 26.0 中的 WebKit 功能 | WebKit](https://webkit.org/blog/17333/webkit-features-in-safari-26-0/)

**原文标题**: [  WebKit Features in Safari 26.0 | WebKit](https://webkit.org/blog/17333/webkit-features-in-safari-26-0/)

Safari 26.0 引入了大量新功能和改进，包括 CSS 锚点定位、滚动驱动动画、HDR 图像支持、HTML `<model>` 元素、数字凭证 API、SVG 图标、WebGPU 集成等，同时提升了网站兼容性、隐私保护和开发者工具。

- 🎯 CSS 锚点定位（Anchor Positioning）允许元素基于另一个元素进行定位，支持响应式菜单和提示框
- 🖼️ 支持 HDR 图像，提供更广的动态范围和色彩表现，增强视觉体验
- 🌐 iOS/iPadOS 上所有网站均可作为 Web App 添加到主屏幕，无需依赖 Manifest 文件
- 📦 新增 HTML `<model>` 元素，支持在网页中嵌入交互式 3D 模型（仅限 visionOS）
- 🔐 数字凭证 API（Digital Credentials API）支持安全请求身份文档（如驾驶证）
- ⚡ WebGPU 正式支持，提供更高效的 GPU 计算和图形渲染能力
- 🖋️ SVG 图标全面支持，包括 Favicon，支持无限缩放和更小的文件体积
- 🛠️ Web Inspector 增强，支持自动检查 Service Worker、时间线记录和多目标调试
- 📱 WebKit 新增 SwiftUI API（WebView 和 WebPage），简化原生应用集成
- 🧩 扩展功能更新，包括 Web Extension Packager 和命令菜单支持
- 🔒 隐私保护加强，阻止已知指纹脚本并改进 Lockdown 模式的字体解析
- 🐞 修复大量 CSS、JavaScript、媒体、表单和可访问性相关问题

---

### [Bun v1.2.22 | Bun 博客](https://bun.com/blog/bun-v1.2.22)

**原文标题**: [Bun v1.2.22 | Bun Blog](https://bun.com/blog/bun-v1.2.22)

Bun 最新版本带来多项安装方式优化、异步堆栈追踪增强、性能提升及兼容性改进，涵盖运行时、打包器、数据库支持和工具链更新。

- 🚀 新增多种Bun安装方式，包括curl、npm、PowerShell、scoop、brew和docker
- 🐛 异步堆栈追踪现在包含完整异步调用帧，调试async/await更便捷
- ⚡ postMessage和structuredClone对纯值对象提速最高达240倍
- 🛠️ 新增Bun.YAML.stringify方法，支持JavaScript对象转YAML格式
- 💻 修复TTY交互支持，正确处理/dev/tty流和事件循环引用
- 🗄️ Bun.SQL增强：MySQL适配器支持affectedRows、lastInsertRowid和TLS连接
- 📦 打包器优化：自动移除无效new关键字、压缩typeof检查、新增onEnd钩子
- ⚙️ 新增jsxSideEffects选项，确保带副作用的JSX组件不被误删
- 📊 实现Node.js兼容的perf_hooks.monitorEventLoopDelay()事件循环监控
- 🔌 WebSocket客户端现支持RFC 6455子协议协商和自定义头部覆盖
- 🧩 Redis客户端支持数据库编号直连和新增hget()命令
- 🔧 修复大量Node.js兼容性问题，涵盖N-API、crypto、buffer等模块
- 🐞 解决打包器、运行时、Shell和安装工具的多项稳定性问题

---

### [React Router 中间件 | Remix](https://remix.run/blog/middleware)

**原文标题**: [Middleware in React Router | Remix](https://remix.run/blog/middleware)

React Router 7.9.0版本通过future.v8_middleware标志正式稳定了中间件功能，解决了嵌套路由中数据加载并行执行导致的逻辑顺序和短路问题，并引入了单次请求架构优化性能。

- 🎉 React Router 7.9.0稳定版支持中间件功能，通过future.v8_middleware标志启用
- 🔄 解决了嵌套路由中父/子加载器并行执行时无法共享数据或短路的问题
- ⚡ 单次请求（Single Fetch）架构合并并行HTTP请求，优化服务器渲染应用性能
- 🛠️ 提供类型安全的Context API，改进数据传递和类型支持
- 📚 常见用例包括认证检查、请求日志、404重定向和响应头设置
- 🔗 社区已有实用中间件库（如remix-utils），官方提供详细文档和示例

---

### [获取流虽好，但不适用于测量上传/下载进度 - JakeArchibald.com](https://jakearchibald.com/2025/fetch-streams-not-for-progress/)

**原文标题**: [Fetch streams are great, but not for measuring upload/download progress - JakeArchibald.com](https://jakearchibald.com/2025/fetch-streams-not-for-progress/)

Fetch流虽然有助于并行处理数据，但不适合用于准确测量上传/下载进度，使用不当可能导致浏览器实现问题，目前推荐使用XHR监测进度，未来可能有专用API。

- 🚫 Fetch流不适合测量上传/下载进度，数据可能因编码压缩导致计算偏差
- 📦 响应流支持分块处理数据，但Content-Length与解码后数据量不匹配
- ⬆️ 请求流可实现并行处理与上传（如视频转码+传输），但无法反映真实网络传输进度
- ⚠️ 错误使用流测量进度可能限制浏览器未来性能优化空间
- 📊 当前推荐使用XMLHttpRequest的onprogress事件监测进度
- 🔮 Igalia团队正在开发Fetch专用进度事件API，未来将弥补功能缺失
- 📋 开发者可通过调查反馈对请求流功能的兴趣（Interop 2026提案）

---

### [告别TypeScript。我们依然爱你，TypeScript | 作者：Chander Ramesh | 2025年9月 | Motion工程博客](https://engineering.usemotion.com/moving-off-of-typescript-e7bb1f3ad091?gi=d7e517bb57b4)

**原文标题**: [Moving off of TypeScript. We Love You, TypeScript | by Chander Ramesh | Sep, 2025 | Motion Engineering Blog](https://engineering.usemotion.com/moving-off-of-typescript-e7bb1f3ad091?gi=d7e517bb57b4)

Motion公司分享了从TypeScript迁移到C#的决策过程，强调了对TypeScript的感激但出于技术需求转向更成熟的企业级语言。

- 🚀 TypeScript曾助力快速迭代和全栈开发，但大型代码库出现性能瓶颈和工具链问题
- ⚠️ 面临移动端兼容性、编译速度慢、第三方库依赖等痛点
- 🛡️ 选择C#因Entity Framework等成熟ORM、强类型安全和稳定运行时
- 🤖 AI编程支持更好，编译器严格性和文档规范提升代码生成质量
- 🌍 .NET生态虽非最流行但足够成熟，适合企业级CRUD应用开发
- 🔄 语言相似性降低迁移成本，最终追求"无聊但可靠"的技术方案

---

### [注册 - Auth0](https://auth0.com/signup?onboard_app=genai&ocid=7014z000001NyoxAAC-aPA4z0000008OZeGAM?utm_source=jsweekly&utm_campaign=amer_mult_mult_all_ciam-dev_dg-plg_auth0_native_jsweekly_newsletter_aud_JSWeeklyNewsletter-Q3_utm2&utm_medium=cpc&utm_id=aNKKZ000000047Q4AQ)

**原文标题**: [Sign Up - Auth0](https://auth0.com/signup?onboard_app=genai&ocid=7014z000001NyoxAAC-aPA4z0000008OZeGAM?utm_source=jsweekly&utm_campaign=amer_mult_mult_all_ciam-dev_dg-plg_auth0_native_jsweekly_newsletter_aud_JSWeeklyNewsletter-Q3_utm2&utm_medium=cpc&utm_id=aNKKZ000000047Q4AQ)

这是一个用户注册界面，提供多种注册方式和全球国家/地区选择，并强调通过Auth for GenAI服务实现安全认证功能。

- 📧 需要输入邮箱和选择国家/地区进行注册
- 🌍 提供全球所有国家/地区的完整选择列表
- 🔐 支持第三方账号登录（GitHub/Google/Microsoft）
- ⚠️ 注册需同意服务条款和隐私政策
- 🤖 突出展示Auth for GenAI的四大安全功能：用户认证、API调用、文档获取和异步授权
- ℹ️ 底部显示版权信息和开发者预览状态说明

---

### [React 默认胜出——它正在扼杀前端创新 | 洛伦·斯图尔特](https://www.lorenstew.art/blog/react-won-by-default)

**原文标题**: [React Won by Default – And It's Killing Frontend Innovation | Loren Stewart](https://www.lorenstew.art/blog/react-won-by-default)

React因默认选择而非技术优势主导前端生态，抑制了Svelte、Solid、Qwik等创新框架的发展，导致技术决策依赖网络效应而非实际需求，最终阻碍整体前端创新。

- 🚫 React因生态惯性成为默认选择，而非技术优势
- ⚡ Svelte通过编译时优化减少运行时开销，性能提升显著（如Bundle大小从187KB降至9KB）
- 🧩 Solid采用细粒度响应式更新，避免虚拟DOM开销，效率比React高2-3倍
- ⏩ Qwik通过可恢复性实现即时启动，特别适合大型应用和慢速网络
- 🔄 React的虚拟DOM和Hooks模式引入性能与复杂度代价（如依赖数组陷阱、闭包问题）
- 🌐 默认选择导致技术单一化：招聘需求、教育方向、组件库生态形成自我强化循环
- 📉 实际案例：Cloudflare 2025年9月 outage 因useEffect依赖问题触发API过载
- 🧠 解决方案：基于项目约束评估框架，采用创新预算试点替代方案
- 🌱 生态健康需要多样性，避免单一框架约束Web平台进化

---

### [超越视界：Angular如何拥抱AI打造下一代应用 | Angular | 2025年9月 | Angular博客](https://blog.angular.dev/beyond-the-horizon-how-angular-is-embracing-ai-for-next-gen-apps-7a7ed706e1a3?gi=078f48236679)

**原文标题**: [Beyond the Horizon: How Angular is Embracing AI for Next-Gen Apps | by Angular | Sep, 2025 | Angular Blog](https://blog.angular.dev/beyond-the-horizon-how-angular-is-embracing-ai-for-next-gen-apps-7a7ed706e1a3?gi=078f48236679)

Angular团队正在积极整合人工智能技术，通过开发创新工具和跨框架合作，为开发者提供更强大的AI辅助开发体验，同时确保框架在AI时代的适应性和代码质量。

- 🛠️ Angular推出Web Codegen Scorer工具，用于评估和优化LLM生成的Web代码质量，支持即时适配新特性（如Signal表单）
- 🤝 与SolidJS团队合作并开源该工具，鼓励跨框架社区共同提升AI代码生成能力
- ⚡ 推出Angular MCP Server（v20.2），为AI编程代理提供内置工具，未来将集成现代化迁移功能和RAG技术以更新LLM知识库
- 🌐 在Google AI产品中扩展Angular支持：Gemini Canvas和Google AI Studio均已提供Angular模板选项
- 🔮 探索AI优先框架设计，研究如何优化框架结构同时兼顾人类开发者和LLM的协作效率
- 🚀 强调Angular的约定式架构（服务/依赖注入）天然适合LLM理解，将持续确保开发者体验平滑过渡

---

### [获取失败](https://javascriptweekly.com/link/174555/web)

**原文标题**: [Failed to retrieve](https://javascriptweekly.com/link/174555/web)

无法总结：获取内容失败，状态码 429。

---

### [使用React Three Fiber打造沉浸式3D天气可视化 | Codrops](https://tympanus.net/codrops/2025/09/18/creating-an-immersive-3d-weather-visualization-with-react-three-fiber/)

**原文标题**: [Creating an Immersive 3D Weather Visualization with React Three Fiber | Codrops](https://tympanus.net/codrops/2025/09/18/creating-an-immersive-3d-weather-visualization-with-react-three-fiber/)

使用React Three Fiber创建沉浸式3D天气可视化应用，通过实时API数据驱动太阳、雨雪和风暴等动态天气效果的交互式3D场景。

- 🌐 基于React Three Fiber和@react-three/drei技术栈构建，集成WeatherAPI实时气象数据
- ☀️ 实现动态日月系统：采用球体贴图与点光源模拟，支持根据当地时间自动切换昼夜效果
- 🌧️ 高性能粒子系统：使用实例化网格(instancedMesh)实现降雨（圆柱体）和降雪（带漂移旋转）效果
- ⚡ 复合风暴系统：结合暗色云层、强降雨和随机闪电效果，通过点光源闪烁模拟雷暴场景
- 📡 API驱动逻辑：将气象文本描述映射为3D组件，支持晴天/多云/降雨/暴风雪等8种天气类型
- 🌅 智能天空系统：根据日出/日暮/白天/黑夜四个时段动态调整Drei Sky组件的大气参数
- 🔮 三维预报门户：使用MeshPortalMaterial创建可交互的天气预报门户，支持沉浸式天气预览
- ✨ 电影级镜头光晕：集成R3F-Ultimate-Lens-Flare库，仅在晴朗天气条件下显示光晕效果
- ⚡ 性能优化：采用实例化渲染、条件加载和门户模式降级（减少87.5%粒子数量）确保流畅体验
- 💾 智能缓存机制：实现10分钟API缓存和降级方案，保证应用在API限流时的正常使用

---

### [GitHub - raineorshine/npm-check-updates: 查找比 package.json 允许更新的包依赖版本](https://github.com/raineorshine/npm-check-updates)

**原文标题**: [GitHub - raineorshine/npm-check-updates: Find newer versions of package dependencies than what your package.json allows](https://github.com/raineorshine/npm-check-updates)

npm-check-updates 是一个用于检查和升级 package.json 中依赖包版本的工具，支持多种包管理器和丰富的自定义选项。

- 🔍 检查并升级 package.json 中的依赖到最新版本，保持现有语义版本策略
- ⚙️ 支持 npm、yarn、pnpm、deno 和 bun 等多种包管理器
- 🎯 提供多种升级目标选项：latest、greatest、minor、patch 等
- 🔧 丰富的过滤和排除选项，支持通配符、正则表达式和自定义函数
- 🛡️ 提供冷却期选项，减少供应链攻击风险
- 🧪 医生模式可迭代测试升级，确保兼容性
- 📁 支持配置文件 (.ncurc)，可自定义各种选项
- 📊 多种输出格式选项，支持分组显示和额外信息展示
- 🔌 支持模块化编程使用方式
- 🌟 开源项目，拥有 9.9k stars 和活跃的社区贡献

---

### [Expo SDK 54 - 更新日志](https://expo.dev/changelog/sdk-54)

**原文标题**: [Expo SDK 54 - Expo Changelog](https://expo.dev/changelog/sdk-54)

Expo SDK 54 正式发布，包含 React Native 0.81，带来 iOS 预编译框架、iOS 26 Liquid Glass 支持、Android 16 目标适配、Expo Updates 功能增强、包管理器与自动链接优化、React Native 新架构强制迁移等多项核心更新与改进。

- 🚀 iOS 预编译 React Native 框架，大幅减少构建时间（M4 Max 设备上从 120 秒降至 10 秒）
- 🎨 支持 iOS 26 Liquid Glass 图标与应用内玻璃视觉效果，提供 expo-glass-effect 库与 SwiftUI 支持
- 🤖 Android 默认启用 edge-to-edge 显示，并可选启用 Predictive Back 手势
- 🔄 Expo Updates 支持运行时覆盖请求头与下载进度追踪，优化更新体验
- 📦 改进包管理器与自动链接，支持嵌套依赖与统一模块链接行为
- ⚙️ React Native 新架构成为唯一选项，Legacy 架构支持将在 SDK 55 移除
- 🧪 实验性功能包括 React Compiler 默认启用、自动链接模块解析与 ESM 支持改进
- 📱 其他更新：expo-file-system 新 API 稳定、expo-sqlite 支持 localStorage API、expo-app-integrity 新增应用完整性验证
- 🛠️ 开发工具优化：Expo CLI 默认启用导入堆栈跟踪与 CSS 自动前缀，支持 TypeScript 5.9.2
- 📉 移除与弃用：expo-av 将在 SDK 55 移除，SafeAreaView 等组件被弃用
- ⚠️ 已知问题：use_frameworks! 暂不兼容预编译框架，需等待后续支持

---

### [世博会](https://expo.dev/)

**原文标题**: [Expo](https://expo.dev/)

Expo是一个全栈React Native框架，提供云端服务以加速应用开发全周期，支持跨平台部署和高效开发工具。

- 🚀 全栈React Native框架，集成云端服务加速应用开发周期
- 📱 支持使用React、Kotlin、Swift编写代码，兼容Expo模块API和配置插件
- 🌐 单一代码库部署Android、iOS和Web应用，支持空中更新(OTA)快速迭代
- ⚡ 开发体验优化：真机调试、一键启动模拟器、可视化包分析工具
- 👥 拥有5万+Discord社区成员，80%的React Native开发者选择使用
- 🏢 企业级安全合规(SOC 2 Type 2/GDPR)，服务数亿终端用户
- 📊 内置监控洞察功能，实时追踪用户数据、API请求和错误率
- 🛠️ 自动化构建测试流程，应用商店提交时长控制在10分钟内
- ⭐ 受到开发者广泛推荐，简化原生代码操作并提升开发效率

---

### [Expo 文件系统在 SDK 54 中获得重大升级](https://expo.dev/blog/expo-file-system)

**原文标题**: [Expo File System gets a major upgrade in SDK 54](https://expo.dev/blog/expo-file-system)

该文本是Expo公司网站的页脚导航内容，列出了产品服务、资源链接、公司信息和法律条款等板块。

- 📱 产品服务包括应用开发工具和云服务等
- 📚 资源区域提供文档、博客和技术支持入口
- 🏢 公司信息涵盖定价、客户案例和招聘信息
- ⚖️ 法律板块包含隐私政策和服务条款等法律文档
- ©️ 版权信息显示为650 Industries公司2025年所有

---

### [订阅免费试用](https://clerk.com/changelog/2025-09-02-free-trials?utm_source=cooper-press&utm_medium=newsletter&utm_campaign=free-trials&utm_content=09-19-25&dub_id=AAeQIsxPF9Ht9k4L)

**原文标题**: [Free trials for subscriptions](https://clerk.com/changelog/2025-09-02-free-trials?utm_source=cooper-press&utm_medium=newsletter&utm_campaign=free-trials&utm_content=09-19-25&dub_id=AAeQIsxPF9Ht9k4L)

Clerk Billing推出免费试用功能，让用户通过设置试用期提升转化率，支持灵活配置和管理，并内置防滥用机制。

- 🆓 免费试用可提升用户转化率，帮助用户体验产品价值
- ⚙️ 支持在仪表盘灵活配置单个或批量计划的试用时长
- 🔄 新注册用户自动享受试用，现有用户不受影响
- 🎛️ 可随时手动终止试用或设置试用结束后自动停止订阅
- 🛡️ 内置防滥用机制：要求绑定信用卡且禁止重复试用
- 📚 提供详细文档和博客指南供用户参考使用
- 💬 开放反馈渠道和社区讨论持续优化功能

---

### [GitHub - LeaVerou/bluesky-likes：用于展示Bluesky点赞的灵活组件](https://github.com/LeaVerou/bluesky-likes)

**原文标题**: [GitHub - LeaVerou/bluesky-likes: Flexible components for displaying Bluesky likes](https://github.com/LeaVerou/bluesky-likes)

这是一个用于展示BlueSky帖子点赞情况的Web组件库，提供灵活且轻量级的解决方案。

- 🎯 提供两个核心组件：bluesky-likes显示点赞数，bluesky-likers显示点赞用户头像
- ⚡ 超轻量级设计，整个包仅约2KB，无依赖
- 💾 支持动态响应和跨实例的激进缓存机制
- ♿ 具备无障碍访问支持和国际化友好设计
- 🎨 高度可定制化，通过CSS属性、插槽和部件进行样式定制
- 🔧 提供自动加载器简化使用，支持CDN和npm安装
- 📱 响应式设计，支持RTL语言和本地化数字格式化
- 🔌 内置BlueSky API包装器，支持获取用户资料和帖子信息
- 📄 MIT许可证，鼓励盈利使用时资助开发

---

### [Bluesky喜爱Web组件](https://projects.verou.me/bluesky-likes/)

**原文标题**: [Bluesky Likes Web Components](https://projects.verou.me/bluesky-likes/)

Bluesky Likes Web Components 是一个开源项目，提供可嵌入的组件用于展示Bluesky社交平台的点赞数据，由Lea Verou和Dmitry Sharabin开发，与Bluesky官方无关联。

- 📄 提供详细文档和资源访问
- 🐛 支持提交错误反馈与创意建议
- 💻 开源代码托管于GitHub平台
- 📦 可通过npm包管理器安装使用
- 🔗 组件内嵌链接时可覆盖默认跳转行为
- ⚠️ 明确声明与Bluesky官方无隶属关系
- ®️ 注明Bluesky商标权属信息

---

### [Svedit - 基于Svelte 5构建富文本编辑器的小型库](https://svedit.vercel.app/)

**原文标题**: [Svedit - A tiny library for building rich content editors with Svelte 5](https://svedit.vercel.app/)

Svedit 是一个专为 Svelte 5 设计的轻量级富内容编辑器库，采用 JSON 建模和可视化就地编辑，支持嵌套节点和事务性操作，目前处于 Alpha 版本。

- 🚀 专为 Svelte 5 构建，无需第三方渲染 API，原生集成
- 🧩 突破线性文本模型，支持文本与结构化内容混合编辑
- 🎨 基于 JSON 内容模型，通过 Svelte 组件直接可视化编辑
- 📦 仅约 2000 行代码，可替代传统内容管理系统
- 🔗 注解作为节点处理，支持路径寻址和安全复制粘贴
- 🌳 支持嵌套节点和图形优先内容模型，适应复杂结构
- ⚡ DOM 与模型选择精确匹配，避免映射层问题
- 🌍 Unicode 安全，支持表情符号、变音符号和 CJK 输入
- ⏪ 事务性编辑支持时间旅行，所有更改可撤销
- 📱 移动端支持实验性，Chrome 兼容性最佳
- 🐛 当前为 Alpha 版本，存在已知问题待修复
- ⭐ 开源项目，采用 MIT 许可证，鼓励社区参与

---

### [GitHub - michael/svedit](https://github.com/michael/svedit)

**原文标题**: [GitHub - michael/svedit](https://github.com/michael/svedit)

Svedit是一个基于Svelte 5的轻量级富文本编辑器库，允许通过JSON建模内容并使用自定义组件进行渲染和直接编辑。

- 📝 基于Svelte 5构建的轻量级富文本编辑器库
- 🎯 使用JSON数据模型定义文档结构和内容
- ✨ 支持直接在布局中进行内容编辑，无需外部CMS
- 📊 采用图形数据模型，支持跨文档内容共享
- 🔧 提供完整的文档API和事务处理系统
- 🖱️ 支持三种选择类型：文本选择、节点选择和属性选择
- 🎨 采用无边框画布设计，编辑工具通过悬浮层显示
- ⚙️ 支持自定义节点类型、工具栏和覆盖层组件
- 📦 目前处于测试阶段，代码总量不足3000行

---

### [GitHub - sinclairzx81/typebox: JavaScript 运行时类型系统](https://github.com/sinclairzx81/typebox)

**原文标题**: [GitHub - sinclairzx81/typebox: A Runtime Type System for JavaScript](https://github.com/sinclairzx81/typebox)

TypeBox 是一个用于 JavaScript 的运行时类型系统，它通过创建内存中的 Json Schema 对象来推断 TypeScript 类型，提供静态类型检查和运行时验证的统一解决方案。

- 🚀 TypeBox 是一个运行时类型系统，生成与 TypeScript 编译器静态检查规则匹配的 Json Schema 对象
- 📦 可通过 npm 安装，支持 TypeScript 和 JavaScript 项目
- 🔧 提供多种函数来创建和组合 Json Schema 类型，支持复杂类型建模
- 📝 包含 Script 功能，允许使用原生 TypeScript 语法创建类型
- ✅ Value 模块提供值检查、解析和其他结构操作功能
- ⚡ Compile 模块可将类型编译为高性能验证器
- 🌐 采用 MIT 许可证，开放社区贡献
- 📊 项目拥有 6k stars 和 189 forks，被超过 970 万项目使用

---

### [Vue Frimousse](https://vue-frimousse.robertshaw.id/)

**原文标题**: [Vue Frimousse](https://vue-frimousse.robertshaw.id/)

文章概述了人工智能在医疗领域的应用现状与未来潜力，重点分析了其对疾病诊断、药物研发和医疗效率的提升作用，同时探讨了技术发展面临的挑战和伦理考量。

- 🤖 人工智能辅助医生进行疾病诊断，提高准确性和效率
- 💊 加速新药研发进程，通过数据分析预测药物效果
- ⚡ 优化医疗资源分配，减少患者等待时间
- 🛡️ 面临数据隐私保护和算法透明度等伦理挑战
- 🔮 未来将与人类医生协同工作，而非完全取代

---

### [GitHub - jeffbski/wait-on：wait-on 是一个跨平台命令行工具和 Node.js API，用于等待文件、端口、套接字及 HTTP(S) 资源变为可用状态](https://github.com/jeffbski/wait-on)

**原文标题**: [GitHub - jeffbski/wait-on: wait-on is a cross-platform command line utility and Node.js API which will wait for files, ports, sockets, and http(s) resources to become available](https://github.com/jeffbski/wait-on)

wait-on 是一个跨平台命令行工具和 Node.js API，用于等待文件、端口、套接字和 HTTP(S) 资源变为可用或不可用（反向模式），支持稳定性检测和超时配置。

- 📦 **跨平台工具** - 可在所有 Node.js 环境（Linux、Unix、macOS、Windows）运行，提供 CLI 和 Node.js API 两种使用方式  
- ⏳ **多资源等待** - 支持文件、TCP 端口、Unix 套接字、HTTP/HTTPS 请求（HEAD/GET 返回 2XX 响应）  
- 🔁 **反向模式** - 通过 `-r` 参数等待资源变为不可用，适用于服务关闭场景  
- ⚙️ **灵活配置** - 可设置延迟检测、轮询间隔、超时时间、并发数及稳定性窗口（文件大小变化监测）  
- 📊 **状态追踪** - 支持日志输出和调试模式，实时显示资源等待状态  
- 🔗 **高级 HTTP 选项** - 支持代理配置、SSL 证书、自定义请求头和重定向控制  
- 📜 **开源协议** - 采用 MIT 许可证，已有 1.9k GitHub stars 和 83 forks

---

### [GitHub - gpbl/react-day-picker: DayPicker 是一个可自定义的 React 日期选择器组件。为您的 Web 应用程序添加日期选择器、日历和日期输入功能。](https://github.com/gpbl/react-day-picker)

**原文标题**: [GitHub - gpbl/react-day-picker: DayPicker is a customizable date picker component for React. Add date pickers, calendars, and date inputs to your web applications.](https://github.com/gpbl/react-day-picker)

React DayPicker 是一个高度可定制的 React 日期选择器组件，支持多种日历类型和本地化选项，适用于构建现代化的日期选择界面。

- 🌟 用于 React 的日期选择器、日历和日期输入组件
- 🛠 提供丰富的自定义属性和样式选项
- 📅 支持单选、多选、日期范围和自定义选择模式
- 🌍 支持多语言本地化和时区设置
- ♿ 符合 WCAG 2.1 AA 无障碍访问标准
- 📦 基于 TypeScript 开发，依赖 date-fns 进行日期处理
- 🔧 提供组件自定义和输入框集成功能
- 📊 获得 6.6k 星标和 761 次 fork，被 442k+ 项目使用
- 📄 采用 MIT 开源许可证

---

### [发布 v0.18.0 · wasp-lang/wasp · GitHub](https://github.com/wasp-lang/wasp/releases/tag/v0.18.0)

**原文标题**: [Release v0.18.0 · wasp-lang/wasp · GitHub](https://github.com/wasp-lang/wasp/releases/tag/v0.18.0)

Wasp编程语言发布了0.18.0版本更新，包含重大变更、新功能、错误修复和多项优化改进。

- ⚠️ 需要Node.js版本≥v22.12，Tailwind配置改用ESM模块，Vite升级至7版本
- 🚀 新增wasp build start命令，支持本地模拟生产环境运行
- 🐛 修复JSON环境变量解析、Bash补全循环和EmailSignupData字段错误
- 🔧 支持Prisma三斜杠注释、移除Stitches减少包体积、优化移动端字体显示
- 📚 新增自定义身份验证操作的代码示例文档

---

### [黄蜂](https://wasp.sh/)

**原文标题**: [Wasp](https://wasp.sh/)

Wasp是一个全栈Web开发框架，通过声明式配置和代码生成技术提升React/Node.js/Prisma应用的开发效率。

- 🚀 基于声明式配置语言快速构建全栈应用，支持一键部署
- 🔐 内置完整身份验证系统，支持社交登录和邮箱登录
- 🎯 提供类型安全的RPC通信层，自动同步服务端与客户端
- ⚡ 集成Prisma数据模型，支持自动缓存失效和乐观更新
- 📧 内置邮件发送功能和后台任务调度系统
- 🌐 完全开源，支持自定义API路由和数据库种子数据
- 🛠️ 保留90%React/Node.js代码编写自由度，仅自动化样板代码
- 📊 提供实时投票、待办应用等多个类型安全示例项目

---

### [GitHub - sindresorhus/pretty-ms：将毫秒转换为人类可读字符串：`1337000000` → `15天11小时23分20秒`](https://github.com/sindresorhus/pretty-ms)

**原文标题**: [GitHub - sindresorhus/pretty-ms: Convert milliseconds to a human readable string: `1337000000` → `15d 11h 23m 20s`](https://github.com/sindresorhus/pretty-ms)

这是一个名为 pretty-ms 的开源 JavaScript 库，用于将毫秒数转换为人类可读的时间格式，支持多种自定义选项和格式化方式。

- ⏱️ 核心功能是将毫秒转换为易读的时间字符串，例如将 1337000000 转换为 "15d 11h 23m 20s"
- 📦 通过 npm 安装，支持 ESM 导入方式，兼容 number 和 bigint 类型输入
- ⚙️ 提供丰富的配置选项：紧凑模式、详细模式、冒号表示法、微秒/纳秒格式化等
- 📄 采用 MIT 开源许可证，项目托管在 GitHub 上，拥有 1.2k 星标和 67 个分支
- 🔧 支持 TypeScript，提供完整的类型定义文件，测试覆盖率高
- 🌐 被广泛使用，已有超过 68.7 万个项目依赖此库
- 📚 提供相关工具链：CLI 版本、时间解析工具和字节格式化工具等配套模块

---

### [发布 v4.0.0 · JS-DevTools/npm-publish · GitHub](https://github.com/JS-DevTools/npm-publish/releases/tag/v4.0.0)

**原文标题**: [Release v4.0.0 · JS-DevTools/npm-publish · GitHub](https://github.com/JS-DevTools/npm-publish/releases/tag/v4.0.0)

JS-DevTools的npm-publish工具发布了v4.0.0版本，主要更新了运行环境和模块格式，包含一些功能改进和错误修复。

- 🚀 更新运行环境至Node 24和npm 11
- ⚠️ 不再支持Node 16和18，仅支持Node 20及以上版本
- 📦 库现在仅支持ESM模块格式
- 🐛 修复了Windows系统上npm CLI的生成问题
- 🔧 更新了dry-run和发布冲突逻辑以适配npm>=10
- 📚 更新了tar和semver依赖项
- 🔒 启用了不可变发布，建议固定使用具体版本号

---

### [GitHub - hexojs/hexo：一个基于 Node.js 的快速、简洁且强大的博客框架](https://github.com/hexojs/hexo)

**原文标题**: [GitHub - hexojs/hexo: A fast, simple & powerful blog framework, powered by Node.js.](https://github.com/hexojs/hexo)

Hexo是一个基于Node.js的快速、简洁且强大的博客框架，提供高效的静态网站生成和丰富的扩展功能。

- 🚀 基于Node.js的快速静态网站生成器，支持GitHub风格Markdown和Octopress插件
- 🌐 一键部署到GitHub Pages/Heroku等平台，拥有数百个主题和插件生态
- 📝 简洁命令行操作：支持博客初始化、本地服务器启动、文章创建和静态文件生成
- 🤝 开源MIT协议，拥有40.8k星标和5k分叉，社区活跃并提供多语言支持
- 🔧 提供完整API文档、故障排查指南和多种社区交流渠道（Discord/Telegram等）

---

### [GitHub - denoland/fresh：下一代 Web 框架](https://github.com/denoland/fresh)

**原文标题**: [GitHub - denoland/fresh: The next-gen web framework.](https://github.com/denoland/fresh)

Fresh 是一个基于 Deno 构建的下一代 Web 框架，专注于速度、可靠性和简洁性，提供零配置、TypeScript 原生支持及边缘渲染等特性。

- 🚀 下一代 Web 框架，专为速度、可靠性和简洁性设计
- ⚡ 支持边缘即时渲染和基于岛屿模型的客户端水合
- 📦 默认零运行时开销（不向客户端发送 JS）
- 🛠️ 无需配置，开箱即用 TypeScript 支持
- 🗂️ 类 Next.js 的文件系统路由机制
- 🌐 通过 Deno Deploy 轻松部署到生产环境
- 📚 提供详细文档和快速入门指南
- 🤝 支持社区贡献和项目展示
- 🔖 推荐使用 #denofresh 和 #deno 标签进行社交分享

---

### [细致入微](https://www.meticulous.ai/?utm_source=javascript_weekly&utm_campaign=september19th2025%20)

**原文标题**: [Meticulous](https://www.meticulous.ai/?utm_source=javascript_weekly&utm_campaign=september19th2025%20)

Meticulous AI 是一款革命性的自动化测试工具，通过记录用户交互行为自动生成并维护测试套件，无需编写代码即可全面覆盖应用的各种边缘情况和用户流程，显著提升开发效率和软件质量。

- 🚀 自动生成测试：通过记录开发、预演和生产环境中的用户交互，AI引擎自动创建并持续更新可视化端到端测试套件
- ⚡ 零维护测试：测试随应用迭代自动演化，无需人工编写、修复或维护任何测试代码
- 🛡️ 无抖动测试：从Chromium底层构建的确定性调度引擎，彻底消除测试中的随机失败问题
- 🔍 预合并验证：在代码合并前即可查看PR对用户工作流程的影响，避免回归问题
- 🌐 广泛框架支持：支持NextJS、React、Vue、Angular、Nuxt、SvelteKit等主流前端框架
- 📊 企业级应用：已被Dropbox、Notion、Lattice等100多家组织采用，大幅提升工程团队信心和交付速度
- ⚙️ 灵活集成：既可补充现有测试套件，也可完全替代传统测试方案

---

### [开始使用 Redis](https://redis.io/lp/get-started2/?utm_source=cooper-press&utm_medium=cpa&utm_campaign=2025-08-app_performance-javascript-weekly-2&utm_content=cloud_-_redis_cloud_users)

**原文标题**: [Get started with Redis](https://redis.io/lp/get-started2/?utm_source=cooper-press&utm_medium=cpa&utm_campaign=2025-08-app_performance-javascript-weekly-2&utm_content=cloud_-_redis_cloud_users)

Redis 是一个高速数据平台，提供云端和本地解决方案，帮助团队快速开发应用，支持向量数据库、缓存和 NoSQL 数据库等多种配置。

- 🚀 全球最快的数据平台，助力快速构建应用
- 🌩️ 提供云端和本地部署解决方案
- 🧠 先进的向量数据库支持高性能生成式 AI 应用
- ⚡ 内存数据库实现极速缓存，加速应用性能
- 🗃️ 键值存储 NoSQL 数据库，适用于实时应用
- 🔧 支持多种开发语言和轻松扩展至生产环境
- 🆓 提供免费开始构建的选项

---

### [开始使用 Redis](https://redis.io/lp/get-started2/?utm_source=cooper-press&utm_medium=cpa&utm_campaign=2025-08-app_performance-javascript-weekly-2&utm_content=cloud_-_redis_cloud_users)

**原文标题**: [Get started with Redis](https://redis.io/lp/get-started2/?utm_source=cooper-press&utm_medium=cpa&utm_campaign=2025-08-app_performance-javascript-weekly-2&utm_content=cloud_-_redis_cloud_users)

Redis是一个高速数据平台，提供云端和本地解决方案，帮助团队快速开发应用，支持向量数据库、缓存和NoSQL数据库等多种数据技术。

- 🚀 全球最快数据平台，加速应用开发
- 🌩️ 支持云端与本地部署，开箱即用
- 🧠 向量数据库助力生成式AI应用
- ⚡ 内存缓存技术提升应用响应速度
- 🗃️ 键值对NoSQL数据库支持实时应用
- 📊 无缝从实验扩展到生产级AI应用
- 💻 提供多语言开发和全角色支持资源
- 🆓 提供免费构建入口和演示服务

---

### [JetBrains JavaScript 日 2025](https://lp.jetbrains.com/javascript-day-2025/?utm_source=cooperpress&utm_medium=cpc&utm_campaign=js_weekly_javascript_day_2025&utm_content=3%20)

**原文标题**: [JetBrains JavaScript Day 2025](https://lp.jetbrains.com/javascript-day-2025/?utm_source=cooperpress&utm_medium=cpc&utm_campaign=js_weekly_javascript_day_2025&utm_content=3%20)

JetBrains将于2025年10月2日在线举办JavaScript Day免费技术大会，汇聚行业专家分享前沿技术与实践经验，包含主题演讲、实时问答及多场专题讨论。

- 🗓️ 活动时间：2025年10月2日线上举行（中欧时间15:00开始）
- 🎫 参与方式：免费注册，通过YouTube平台直播/回放
- 👥 特邀讲者：包含Ryan Carniato（SolidJS作者）、Kent C. Dodds（前端教育家）、Lydia Hallie（Bun核心成员）等9位行业领袖
- 🚀 技术主题：涵盖量子计算与JavaScript应用、现代构建工具优化、微前端SSR架构、信号机制演进、AI交互新模式等前沿领域
- ⚡ 专项议题：包含Bun运行时性能解析、开源项目维护实践、WebStorm产品幕后决策揭秘等实战内容
- 📺 后续支持：所有会议录制视频将在YouTube发布，支持实时聊天提问
- ✨ 特色环节：设有开幕欢迎、量子算法趣味演讲及闭幕总结环节

---

### [JetBrains JavaScript 日 2025](https://lp.jetbrains.com/javascript-day-2025/?utm_source=cooperpress&utm_medium=cpc&utm_campaign=js_weekly_javascript_day_2025&utm_content=3%20)

**原文标题**: [JetBrains JavaScript Day 2025](https://lp.jetbrains.com/javascript-day-2025/?utm_source=cooperpress&utm_medium=cpc&utm_campaign=js_weekly_javascript_day_2025&utm_content=3%20)

JetBrains将于2025年10月2日在线举办JavaScript Day免费技术大会，汇聚行业专家分享前沿技术与实践经验，包含主题演讲和实时问答环节。

- 🗓️ 活动时间：2025年10月2日线上举行
- 🎫 参与方式：免费注册，通过YouTube直播观看
- 👨‍💼 特邀讲者：包括Ryan Carniato（SolidJS创建者）、Kent C. Dodds（软件教育家）、Lydia Hallie（Bun核心成员）等9位行业领袖
- 🚀 技术主题：涵盖量子算法JavaScript应用、现代构建工具优化、微前端SSR架构、信号机制演进、AI交互新模式等前沿领域
- ⚡ 特别亮点：Bun运行时性能解析、WebStorm开发工具幕后揭秘、大型开源项目维护实践
- 📺 后续支持：所有演讲将录制发布，支持回看
- 🤝 社区准则：活动遵循行为准则，鼓励实时互动问答

---

### [IINA - macOS 现代媒体播放器](https://iina.io/)

**原文标题**: [IINA - The modern media player for macOS](https://iina.io/)

IINA是一款基于开源媒体播放器mpv的强大播放器，几乎支持所有本地媒体格式，并可通过浏览器扩展一键播放各类在线流媒体。

- 🎬 基于开源mpv，支持几乎所有媒体文件格式
- 🌐 集成youtube-dl，支持在线流媒体播放
- 🖱️ 提供浏览器扩展，实现一键播放功能

---

### [插件系统 | IINA - macOS 现代媒体播放器](https://iina.io/plugins/)

**原文标题**: [Plugin System | IINA - The modern media player for macOS](https://iina.io/plugins/)

IINA 1.4.0版本引入了基于JavaScript的插件系统，允许用户通过编写代码扩展播放器功能，包括播放控制、界面定制和系统交互等。

- 🧩 插件系统支持JavaScript编写，可调用mpv API、控制播放、访问网络/文件系统及添加UI元素
- ⚡ 提供简洁高效的API，仅需少量代码即可实现定制功能，支持直接粘贴代码片段使用
- 🎬 示例1：视频加载时在画面顶部以大字体显示标题（使用overlay模块）
- 🪟 示例2：视频暂停时自动最小化窗口，恢复窗口时继续播放（通过事件监听实现）
- 🔧 核心功能覆盖：播放控制、MPV接口、事件监听、网络请求、字幕下载、菜单扩展等12个模块
- 🛠️ 提供官方命令行工具iina-plugin辅助开发，包含完整文档和TypeScript类型定义
- 🌐 支持用户脚本插件(iina-plugin-userscript)免打包安装，提供多语言翻译和开源资源

---

### [哪个npm包的版本号最大？](https://adamhl.dev/blog/largest-number-in-npm-package/)

**原文标题**: [Which npm package has the largest version number?](https://adamhl.dev/blog/largest-number-in-npm-package/)

作者通过分析npm注册表中的360多万个包，探索了版本号中最大数字的包，最终发现遵循语义化版本控制且版本号最大的包是all-the-package-names，其版本为1.3905.0。

- 🔍 作者因AWS SDK v3.888.0的版本号引发好奇，开始研究npm中版本号最大的包
- 🌐 通过CouchDB的复制API获取了超过360万个包的数据，耗时约12小时
- 📊 分析显示许多高版本号包因自动化配置错误（如GitHub Actions循环发布）导致版本数虚高
- 🏆 经过筛选，all-the-package-names以3905的版本号成为实际遵循语义化版本控制的获胜者
- ⚙️ 使用TypeScript编写脚本处理数据，排除了已知的问题包（如@mahdiarjangi/phetch-cli等）

---

### [下载离线MDN文档 - CSS、HTML、JavaScript、HTTP、SVG - Kapeli](https://kapeli.com/mdn_offline)

**原文标题**: [Download Offline MDN Documentation - CSS, HTML, JavaScript, HTTP, SVG - Kapeli](https://kapeli.com/mdn_offline)

该网站提供MDN离线文档下载，包含CSS、HTML、JavaScript、HTTP和SVG等开发文档，支持无网络环境下使用，每月更新并建议搭配专用文档浏览器获得更佳体验。

- 📁 提供CSS/HTML/JavaScript/HTTP/SVG五大离线文档集下载
- 📅 所有文档均于2025年9月2日完成最新更新
- 🌐 支持直接解压后用浏览器查看，无需安装专用应用
- ⚡ 推荐搭配Dash(macOS)/Velocity(Win)/Zeal(Linux)使用增强搜索功能
- 🔄 文档档案每月定期更新保持内容最新
- ⚠️ 若使用文档应用需通过应用内置功能下载专用版本

---

### [工人所有的技术咨询公司——博库](https://www.bocoup.com/blog/the-webs-most-tolerated-feature)

**原文标题**: [A Worker-Owned Tech Consultancy - Bocoup](https://www.bocoup.com/blog/the-webs-most-tolerated-feature)

文章回顾了Internet Explorer的`zoom`属性从非标准功能到最终被现代CSS标准采纳的曲折历程，强调了其在Web发展中的复杂影响和最终标准化的重要性。

- 🕰️ 2000年6月19日，微软发布IE 5.5，引入非标准功能`zoom`，允许开发者缩放元素但缺乏正式规范。
- 🌐 早期Web平台碎片化导致`zoom`未被广泛采纳，仅作为装饰性功能存在。
- 🔄 Mozilla在Firefox中忽略`zoom`，转而支持标准化的CSS `transform`属性，提供更高效和可控的缩放功能。
- 📊 通过多项指标（如开发者调查、MDN流量、Stack Overflow提及等）发现`zoom`看似流行，但实际使用中94%为无效值（如`zoom: 1`，用于修复旧版IE问题）。
- ⚙️ 2023年CSS工作组提出新`zoom`规范，减少缺陷，并于2025年被Interop项目采纳，获得广泛浏览器支持。
- 💡 启示：Web共识虽慢但促创造性解决方案；避免依赖专有技术；旧功能需谨慎处理兼容性。

---

