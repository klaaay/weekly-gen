### [JavaScript 周刊第 763 期：2025 年 11 月 28 日](https://javascriptweekly.com/issues/763)

**原文标题**: [JavaScript Weekly Issue 763: November 28, 2025](https://javascriptweekly.com/issues/763)

这是一份关于前端开发、JavaScript 生态及工具更新的技术资讯简报，涵盖安全威胁、新版本发布、性能优化和开发资源等内容。

- 🐛 **npm 蠕虫病毒分析**：Shai-Hulud 2.0 蠕虫通过感染 npm 包窃取开发者凭证并自我传播
- 🚀 **重要版本更新**：Node.js 24 已在 AWS Lambda 支持、Prettier 3.7、Playwright 1.57 等工具发布新版本
- ⚡ **性能优化警示**：Alex Russell 指出 JavaScript 打包体积过大导致的性能不平等问题
- ⚛️ **React 生态探讨**：Jeremy Keith 讨论 React 在现代前端的作用及 Preact 的替代可能
- 🛠️ **开发工具推荐**：FullCalendar 日历控件、Better Auth 认证框架、Ant Design 6.0 等新工具发布
- 📚 **免费学习资源**：Piccalilli 团队免费开放异步 JavaScript 课程章节，社区推出黑五优惠
- 🔐 **安全漏洞提醒**：Next.js 服务器漏洞已修复，GitHub 开始报告 Gist 中的密钥泄露
- 🤖 **AI 开发应用**：Vercel 推出 React Native 移动应用，Claude Code 用于邮件分析等 AI 实践案例
- 🌐 **技术趋势追踪**：CSS subgrid 功能全面支持、Zig 语言迁移至 Codeberg、Gemini 3.0 新特性汇总

---

### [GitHub - trekhleb/javascript-algorithms：📝 基于 JavaScript 的算法与数据结构实现，含解释及延伸阅读链接](https://github.com/trekhleb/javascript-algorithms)

**原文标题**: [GitHub - trekhleb/javascript-algorithms: 📝 Algorithms and data structures implemented in JavaScript with explanations and links to further readings](https://github.com/trekhleb/javascript-algorithms)

这是一个包含 JavaScript 实现的各种算法和数据结构的开源项目，提供详细解释和进一步阅读链接。

- 📚 项目包含大量 JavaScript 实现的算法和数据结构，涵盖从基础到高级的内容
- 🌐 支持多语言文档，包括中文、英文、日文等多种语言的 README 文件
- 🏗️ 涵盖数据结构如链表、树、图、堆、哈希表等，并标注难度级别
- ⚡ 包含数学、字符串、排序、搜索、加密、机器学习等多个领域的算法
- 📊 提供算法复杂度分析和大 O 表示法参考图表
- 🧪 包含测试环境和代码质量检查工具，支持开发者学习和实验
- 🤝 开源社区活跃，拥有大量星标和分支，欢迎贡献者参与
- 📄 采用 MIT 许可证，提供完整的代码规范和贡献指南

---

### [从 JavaScript 迁移到 TypeScript | 前端大师](https://frontendmasters.com/courses/typescript-first-steps/?utm_source=email&utm_medium=javascriptweekly&utm_content=typescript)

**原文标题**: [Migrate from JavaScript to TypeScript | Frontend Masters](https://frontendmasters.com/courses/typescript-first-steps/?utm_source=email&utm_medium=javascriptweekly&utm_content=typescript)

本课程由 Anjana Vakil 主讲，时长约 8 小时，系统讲解从 JavaScript 迁移到 TypeScript 的全过程。课程通过实际项目演示如何利用静态类型提升代码质量，涵盖类型注解、接口、泛型等核心概念，并指导配置 TypeScript 编译器和实现全栈类型安全。

- 🎯 从 JavaScript 平滑过渡到 TypeScript，通过实际项目掌握静态类型优势
- 🛠️ 学习类型注解、接口与泛型，编写更安全可靠的代码
- ⚙️ 配置 TypeScript 编译器，实现跨文件类型复用
- 🚀 转换前后端代码至 TypeScript，构建全栈类型安全体系
- 📚 包含编译器配置、类型收窄、工具集成等进阶内容
- 💡 通过 EventMe 全栈项目实战演示类型系统应用
- 🌟 推荐官方文档和专家资源助力持续学习

---

### [沙虫 2.0 npm 蠕虫：深度解析与必备防护指南 | Datadog 安全实验室](https://securitylabs.datadoghq.com/articles/shai-hulud-2.0-npm-worm/)

**原文标题**: [
  The Shai-Hulud 2.0 npm worm: analysis, and what you need to know | Datadog Security Labs
](https://securitylabs.datadoghq.com/articles/shai-hulud-2.0-npm-worm/)

2025 年 9 月和 11 月相继发现两个自复制 npm 蠕虫 Shai-Hulud，其中 Shai-Hulud 2.0 感染了 796 个 npm 软件包（周下载量超 2000 万），通过窃取凭证、建立 GitHub 命令控制通道、篡改合法包实现传播，并在失败时销毁用户数据。

- 🪱 发现两个自复制 npm 蠕虫（Shai-Hulud 和 2.0 版），感染 796 个包影响超 500 名 GitHub 用户
- 📁 注入恶意文件 setup_bun.js 和 bun_environment.js，通过预安装脚本触发攻击流程
- 🔑 窃取本地与云环境凭证（AWS/Azure/GCP），使用 Trufflehog 主动搜索密钥
- 📤 通过 GitHub 公开仓库外泄数据，支持盗用其他受害者令牌作为备用方案
- ⚙️ 在受控机器部署自托管 GitHub 运行器，利用漏洞远程执行代码
- 🔄 使用 npm 凭证自动篡改用户名下 100 个包实现自我传播
- 💥 传播失败时彻底删除用户主目录文件
- 📊 通过 GHArchive 评估影响（至少 500 用户/150 组织数据外泄）
- 🔍 提供 796 个受影响包列表及文件哈希等入侵指标（IOCs）
- 🛡️ Datadog 提供供应链防火墙、代码安全检测和运行时防护方案

---

### [更新且持续进行的供应链攻击瞄准 CrowdStrike...](https://socket.dev/blog/ongoing-supply-chain-attack-targets-crowdstrike-npm-packages)

**原文标题**: [Updated and Ongoing Supply Chain Attack Targets CrowdStrike ...](https://socket.dev/blog/ongoing-supply-chain-attack-targets-crowdstrike-npm-packages)

Socket CEO Feross Aboukhadijeh 与 a16z 合伙人 Joel de la Garza 探讨了氛围编程、AI 驱动的软件开发，以及尽管存在风险，但 LLM 的兴起仍指向更安全与创新的未来。

- 🎧 氛围编程与 AI 驱动开发成为焦点，强调人机协作的新模式  
- ⚠️ 大型语言模型存在安全风险，但整体推动软件安全进步  
- 🚀 AI 技术助力开发者提升效率，加速创新周期  
- 🔒 通过工具链改进与风险管控，构建更可靠的开发生态  
- 🌟 人机协同被视为未来软件行业演进的核心路径

---

### [TanStack 现状：两年全职开源之路 | TanStack 博客](https://tanstack.com/blog/tanstack-2-years)

**原文标题**: [The State of TanStack, Two Years of Full-Time OSS | TanStack Blog](https://tanstack.com/blog/tanstack-2-years)

TanStack 创始人回顾两年全职投入开源项目的历程，分享从个人项目发展为生态系统的成长轨迹，涵盖团队建设、可持续发展模式与未来规划。

- 🚀 全职投入开源两年，构建覆盖超 1300 万仓库的 13 个活跃项目生态系统
- 💡 核心挑战在于独立开发全栈框架 TanStack Start，突破资金限制实现多运行时适配
- 👨‍👩‍👧‍👦 家庭支持成为抵御 burnout 的重要基石，坚持工作与生活平衡
- 🤝 建立 36 人核心团队，通过 16 家合作伙伴实现可持续运营模式
- 📊 累计 40 亿次下载、11.2 万 GitHub 星标，年度 300 万用户访问官网
- 🏢 9000 家企业正式使用，33000 家处于评估阶段，覆盖各行业头部公司
- 🌱 未来发展聚焦 TanStack Start 1.0、路由功能升级及全新重量级库开发
- ❤️ 社区文化强调友善包容，多位贡献者曾出于原则拒绝报酬
- 🤲 通过 GitHub 星标、Discord 参与和商业赞助获得持续支持

---

### [TanStack | 面向 Web 开发者的高质量开源软件](https://tanstack.com/)

**原文标题**: [TanStack | High Quality Open-Source Software for Web Developers](https://tanstack.com/)

TanStack 是一个为 Web 开发者提供高质量开源工具套件的项目，专注于无头 UI 设计、类型安全和强大的功能，涵盖路由、状态管理、数据可视化等领域。

- 🚀 **全栈框架** - 基于 TanStack Router 和 Vite，支持服务端渲染和流式传输
- 🧭 **类型安全路由** - 为 React 和 Solid 应用提供完整的类型安全 API
- 🔄 **异步状态管理** - 强大的服务器状态工具和数据获取能力
- 💾 **响应式数据存储** - 客户端优先的 API 数据存储解决方案
- 📊 **无头表格组件** - 完全控制标记和样式的强大表格/数据网格
- 📝 **高性能表单** - 类型安全的无头表单状态管理
- 🖥️ **虚拟化列表** - 大规模可滚动 DOM 节点的高性能渲染
- ⚡ **性能优化工具** - 防抖、节流、速率限制等核心性能原语
- 🔧 **开发工具** - 统一的开发工具面板和自定义集成
- 📦 **包管理工具** - 用于发布和维护高质量 JavaScript 包的工具链

---

### [异步 JavaScript 入门指南 - Piccalilli](https://piccalil.li/javascript-for-everyone/lessons/48)

**原文标题**: [
  Introduction to Asynchronous JavaScript - Piccalilli
](https://piccalil.li/javascript-for-everyone/lessons/48)

这是一门关于 JavaScript 异步编程的课程模块，重点解释了 JavaScript 的单线程特性、事件循环机制以及异步任务的处理方式。

- 🧵 JavaScript 采用单线程执行模型，每个执行环境（realm）拥有独立的主线程
- 🌐 浏览器标签页、iframe 和 Web Worker 都是独立的执行环境
- ⏱️ 异步任务（如 setTimeout、fetch）通过回调函数实现，不会阻塞主线程执行
- 🔄 事件循环机制管理回调队列和微任务队列，按优先级处理异步任务
- 📞 回调函数在条件满足后被放入队列，等待调用栈清空后执行
- ⚡ 微任务队列优先级高于回调队列，用于处理 Promise 等高级异步操作
- 🎯 异步模块作为课程最后部分，将深入讲解 Promise 对象的使用
- 💰 课程提供 Black Friday 优惠活动，可使用折扣码购买完整内容

---

### [面向所有人的 JavaScript - 课程概览 - Piccalilli](https://piccalil.li/javascript-for-everyone/lessons)

**原文标题**: [
  JavaScript for Everyone - Course overview - Piccalilli
](https://piccalil.li/javascript-for-everyone/lessons)

这是一门名为《JavaScript for Everyone》的完整课程，由 Piccalilli 设计，涵盖从基础语法到高级概念的 JavaScript 全栈知识体系。

- 🚀 课程从 JavaScript 发展历程和严格模式开始，建立语言认知基础
- 📚 系统讲解词法分析、空白符、表达式等核心语法规则
- 🔢 深入解析数字、字符串、布尔值等原始数据类型
- 🏷️ 涵盖变量声明、作用域、解构赋值等变量管理机制
- 📊 包含数组创建、元素访问、扩展语法等集合操作
- 🔑 详解 Set/Map 等键值集合与对象属性管理
- 🔄 涉及迭代器、生成器函数等高级编程概念
- 🏛️ 全面介绍函数定义、类定义、继承等面向对象特性
- ⚡ 包含 Promise、异步函数等现代异步编程解决方案
- 🎯 课程结构完整，包含 53 个章节，涵盖免费阅读内容

---

### [2025 年黑色星期五特惠 - Piccalilli 精选](https://piccalil.li/links/black-friday-deals-2025/)

**原文标题**: [
  Black Friday deals 2025 - Piccalilli
](https://piccalil.li/links/black-friday-deals-2025/)

2025 年黑色星期五期间，多家独立开发者与教育平台推出重磅优惠活动，涵盖网页开发、编程课程与设计工具等领域。

- 💻 Polypane 开发浏览器限时 22% 折扣，新增项目功能提升响应式网站建设效率  
- 🎓 Josh Comeau 推出多重优惠套餐：CSS 课程基础/专业/终极版分别享 13%/22%/40% 折扣，React 课程套餐优惠达 16%-42%  
- 📚 Joy for JavaScript 开发者捆绑包直降 50%，原价$998 现仅$498  
- ♿ Sara Soueidan 无障碍设计课程提供 30% 专属折扣  
- 🔬 Brad 与 Ian Frost 推出$1000 全课程超级捆绑包，另设$500 原子设计认证组合套餐  
- 🎨 Kevin Powell 的 CSS 课程体系推出阶梯优惠：CSS Demystified 三个套餐折后价£150/£66/£30  
- ⚡ Remy Sharp 终端训练课程立省$66，仅需$33 即可提升命令行技能  
- 👨‍🏫 Scott Jehl 课程使用优惠码 TWENTYFIVE 仅需$25（原价$150）  
- 📱 Sindre Sorhus 多款应用程序参与黑五促销  
- 🎯 Every Layout 平台使用优惠码 BLACK_FRIDAY 享 50% 折扣  
- 🚀 Ankita Kulkarni 课程组合优惠：Next.js 课程用码省 46%，开发者领导力课程省 52%  
- 📖 Julia Evans 所有知识手册 PDF 版 5 折，印刷版 7 折  
- 🎪 Piccalilli 平台购课即赠 50% 优惠券，单课程£189 起，叠加优惠后双课程可省£180

---

### [Prettier 3.7：提升格式化一致性与新增插件功能！· Prettier](https://prettier.io/blog/2025/11/27/3.7.0)

**原文标题**: [Prettier 3.7: Improved formatting consistency and new plugin features! · Prettier](https://prettier.io/blog/2025/11/27/3.7.0)

Prettier 3.7 版本发布，主要优化了 TypeScript 和 Flow 的格式化一致性，修复了多项错误，并新增了对 Angular 21 和 GraphQL 16.12 的支持，同时为插件开发者提供了更多 API 控制权。

- 🎯 统一类和接口的格式化规则，提升 TypeScript 和 Flow 代码的一致性
- 🐛 修复了 JavaScript 中注释处理、导入属性换行及逻辑表达式打印等多个错误
- 🔧 新增对 Angular 21 新赋值运算符和正则表达式的支持，以及 GraphQL 可执行描述功能
- 📦 为插件开发者新增评论附加和忽略节点处理的 API，增强自定义能力
- 🛠️ 改进了 CSS、SCSS、HTML 等语言的格式化细节，如选择器大小写和事件处理程序
- 📝 优化了 Markdown 表格对齐和 Front Matter 解析，支持 TOML 格式
- ⚡ 提升了 CLI 性能，避免在不启用缓存时创建不必要的目录

---

### [pnpm 10.24 | pnpm](https://pnpm.io/blog/releases/10.24)

**原文标题**: [pnpm 10.24 | pnpm](https://pnpm.io/blog/releases/10.24)

pnpm 10.24 版本发布，主要优化网络并发自动调节并修复多项可靠性问题  
- 🚀 网络并发数现根据 CPU 核心数自动调整（16-64 区间），提升多核机器性能  
- 🔒 正式版安装时忽略预发布版本的信任策略，避免依赖冲突  
- 🐛 修复容器环境中文件链接异常，自动降级为文件复制操作  
- ↩️ 撤销自更新功能中从 npm 仓库下载 pnpm 的设计  
- 📦 优化无 package.json 文件的包管理，减少重复导入  
- 🔑 修复带下划线 URL 的认证令牌读取问题

---

### [Bun v1.3.3 | Bun 博客](https://bun.sh/blog/bun-v1.3.3)

**原文标题**: [Bun v1.3.3 | Bun Blog](https://bun.sh/blog/bun-v1.3.3)

本次 Bun 版本更新修复了 95 个问题，涵盖安装优化、新功能增加及多项问题修复。

- 🚀 新增压缩流 API，支持 gzip/deflate/zstd 等格式的流式压缩处理
- ⚙️ 独立可执行文件支持禁用.env 和 bunfig.toml 自动加载
- 🧪 测试框架新增 retry 和 repeats 选项处理不稳定测试
- 🚫 新增--no-env-file 标志禁用.env 文件自动加载
- 🗄️ SQLite 升级至 3.51.0 版本
- 📦 内部升级 Zig 0.15.2，减小二进制文件体积
- 🔧 修复打包器、安装过程、Windows 兼容性等问题
- 🌐 改进 Node.js 兼容性，修复 N-API 问题
- 🛠️ 修复 Web API、Bun.serve、网络模块等内存泄漏问题
- 📝 完善 TypeScript 类型定义，更新根证书安全列表
- 📊 bun upgrade 显示人性化下载大小单位
- 👥 感谢 19 位贡献者的代码贡献

---

### [发布 v1.57.0 · microsoft/playwright · GitHub](https://github.com/microsoft/playwright/releases/tag/v1.57.0)

**原文标题**: [Release v1.57.0 · microsoft/playwright · GitHub](https://github.com/microsoft/playwright/releases/tag/v1.57.0)

Playwright v1.57.0 版本发布，主要包含性能分析工具增强、浏览器内核升级、服务等待机制优化等新特性，同时移除了已弃用 API 并引入多项新功能。

- 🐢 新增 HTML 报告器中的"Speedboard"功能，可排序显示最慢的测试用例
- 🔄 将默认浏览器从 Chromium 切换为 Chrome for Testing（Linux Arm64 除外）
- ⏳ 为 webServer 配置新增 wait 字段，支持通过正则表达式等待服务就绪
- 🚫 正式移除已弃用三年的 Page#accessibility API
- 🏷️ 新增 testConfig.tag 属性，便于在合并报告时标记测试运行
- 📢 新增 worker.on('console') 事件监听工作线程的 console 输出
- 🎯 locator.description() 方法可返回定位器描述信息
- 🖱️ 为 click() 和 dragTo() 操作新增 steps 参数控制鼠标移动事件频率
- 🌐 支持拦截 Service Worker 发起的网络请求（仅 Chromium）
- 🔧 浏览器版本更新：Chromium 143.0.7499.4、Firefox 144.0.2、WebKit 26.0

---

### [Chrome 测试版：为浏览器自动化提供可靠下载 | 博客 | Chrome 开发者专区](https://developer.chrome.com/blog/chrome-for-testing/)

**原文标题**: [Chrome for Testing: reliable downloads for browser automation  |  Blog  |  Chrome for Developers](https://developer.chrome.com/blog/chrome-for-testing/)

谷歌推出专为自动化测试设计的 Chrome for Testing 版本，解决开发者因浏览器自动更新导致的测试结果不一致问题，并提供版本化二进制文件下载。

- 🎯 专为测试场景设计，移除了自动更新功能，确保测试结果可复现
- 🔄 与 Chrome 正式版同步发布流程，覆盖稳定版/测试版/开发版/Canary 渠道
- 📦 通过@puppeteer/browsers 命令行工具可快速下载指定版本
- 🔗 同步提供匹配版本的 ChromeDriver，解决兼容性问题
- 🌐 提供 JSON API 接口和版本状态仪表板供自动化脚本调用
- ⚠️ 明确禁止用于日常浏览，仅适用于可信内容的自动化测试
- 💡 替代原本不稳定的 Chromium 二进制文件下载方案

---

### [Valibot v1.2 版本发布说明 | Valibot](https://valibot.dev/blog/valibot-v1.2-release-notes/)

**原文标题**: [Valibot v1.2 release notes | Valibot](https://valibot.dev/blog/valibot-v1.2-release-notes/)

Valibot v1.2 版本发布，新增类型转换操作、AI 工具集成元数据功能、ISBN 验证，并修复安全漏洞，持续优化稳定性和开发体验。

- 🚀 新增五种类型转换操作（toBigint/toBoolean/toDate/toNumber/toString），支持表单/API 数据自动类型转换
- 🤖 引入示例元数据功能（examples/getExamples），提升 AI 工具集成与文档生成能力  
- 📚 新增 ISBN 验证操作，支持 ISBN-10/13 格式校验与校验和验证
- 🔒 修复 emoji 操作中的 ReDoS 正则表达式安全漏洞
- ⚡ 构建工具切换至 tsdown，显著提升编译速度
- 🙏 致谢核心贡献者@EskiMojo14 与专业图书馆员@ysknsid25
- 🤝 新增云测试平台 LambdaTest 作为官方合作伙伴

---

### [发布 v10.1.0 · storybookjs/storybook · GitHub](https://github.com/storybookjs/storybook/releases/tag/v10.1.0)

**原文标题**: [Release v10.1.0 · storybookjs/storybook · GitHub](https://github.com/storybookjs/storybook/releases/tag/v10.1.0)

Storybook 10.1 版本发布，主要聚焦安装流程优化和可访问性提升，同时包含多项框架兼容性改进和实验性功能。

- 🚀 安装体验优化：CLI 全面升级，实现更快速可靠的初始化流程
- ♿ 可访问性增强：界面重构修复数百项无障碍访问问题
- 📝 新手引导：新增基于检查清单的入门指南
- 🅰️ 框架支持：新增 Angular 21 兼容支持
- 🛠️ 构建工具：CLI 新增 RSbuild 安装支持
- ⚡ 测试集成：Preact 框架支持 Vitest 插件
- 🔬 实验功能：引入组件清单功能和改进的 React JSX 代码片段
- 🐛 问题修复：涵盖 CLI、核心功能、UI 组件等多方面优化

---

### [发布 v16.0.5 · vercel/next.js · GitHub](https://github.com/vercel/next.js/releases/tag/v16.0.5)

**原文标题**: [Release v16.0.5 · vercel/next.js · GitHub](https://github.com/vercel/next.js/releases/tag/v16.0.5)

Next.js 项目发布了 v16.0.5 版本更新，主要包含错误修复和性能优化

- 🐛 修复了 Node.js 中间件中 body 克隆未正确完成的问题 (#85418)
- ⚠️ 本次为补丁版本，仅包含错误修复未引入新功能
- 👨‍💻 由开发者 @lucasadrianof 贡献主要修复
- 📅 版本于 11 月 26 日发布，基于 canary 分支的 372 次提交
- 🎉 获得社区 40 位开发者积极反馈（19 个喝彩/17 个点赞/7 个火箭/3 个爱心）

---

### [发布 v11.0.0 · immerjs/immer · GitHub](https://github.com/immerjs/immer/releases/tag/v11.0.0)

**原文标题**: [Release v11.0.0 · immerjs/immer · GitHub](https://github.com/immerjs/immer/releases/tag/v11.0.0)

GitHub 上 Immer 库 v11.0.0 版本发布页面因加载异常无法正常显示内容，但可见版本基础信息和部分更新记录。

- 🚀 性能优化：重构终结系统，采用回调机制替代树遍历方案
- ⚠️ 重大变更：默认启用宽松迭代模式并简化迭代检查
- 🔧 功能增强：支持通过类型参数跳过原型查找，优化工具函数
- 🧩 架构改进：移植 Mutative 的终结回调机制，实现精准化处理
- 📦 代码优化：压缩对象引用和字段名称，减少代码体积
- 🐛 测试更新：调整自引用测试用例以适配新行为
- 👥 社区反馈：获得 11 位开发者点赞认可

---

### [2026 年性能差距问题——偶有提及](https://infrequently.org/2025/11/performance-inequality-gap-2026/)

**原文标题**: [The Performance Inequality Gap, 2026 - Infrequently Noted](https://infrequently.org/2025/11/performance-inequality-gap-2026/)

2026 年网络性能预算分析显示，设备与网络条件持续改善但性能差距仍在扩大，前端开发文化导致网站臃肿化问题加剧。

- 📱 测试基准更新：三星 Galaxy A24 4G 和 HP 14 作为标准测试设备，模拟全球 75% 用户设备性能
- 🌐 网络参数调整：2026 年基准网络设置为 9Mbps 下行/3Mbps 上行/100ms 延迟
- 📊 资源预算标准：3 秒加载目标下 JS 轻量页需≤2.0MiB，JS 重度页需≤1.2MiB
- 🚀 协议优化建议：采用 HTTP/2 或 HTTP/3 协议可提升 350-500KiB 预算空间
- 📈 网站膨胀现状：移动端页面中位数达 2.6MiB，十年增长 2.5 倍
- ⚠️ JavaScript 危机：移动端 JS 载荷较 2015 年翻倍，P75 设备达 1.3MiB
- 📉 核心指标停滞：仅不到半数网站通过 Core Web Vitals 移动端测评
- 💸 设备性能鸿沟：低端 Android 单核性能仅为 iPhone 的 1/9
- 🔄 市场动态：智能手机年更换率 23.7%，低端设备占比超 30%
- 📡 网络演进缓慢：5G 实际覆盖仍有限，4G 将继续主导多年
- 💡 解决方案：需通过工具约束、架构优化和性能意识重建健康生态

---

### [Adactio：日志——为何选用 React？](https://adactio.com/journal/22265)

**原文标题**: [Adactio: Journal—Why use React?](https://adactio.com/journal/22265)

。端前在架框用使要不户用响影不前提在，器务服在架框用使以可仍们我明说 Astro 而，户用罚惩不并境环写撰 JSX 留保以可员发开，法方同不取采 Astro 🛠️
- 器务服在 React 行运仅以可但，器务服在 React 用使续继以可员发开，端前在 React 用使开离换切议建 🚀
- 能性可的户用制限要架框让要不，境环写撰为作 React 住抓想会能可你解理全完，器览浏在 JavaScript 生原用使励鼓 🎯
- 态状理管要需仅，用应页单是若但，户用给送传 React 要需没并，化文是若因原用使果如 🌐
- 器务服在 React 持保以可，端前在 React 用使免避该应，户用响影接直会端前在架框何任何任：题问的心核出提章文 🧩
- 性效高求追以可更户用为，器务服在 React 行运议建者作，端前在架框何任是都户用端终对税种一 🏗️
- 性惯惯习是还由理选择选，境环业企是时多很 React，择选己自是不但架框用使些有 👥
- 性惯是因原要主，户用验体好更生产员发开心开为因是不，验体户用善改接直有没 React 用使 🌀

章文析分 React 用使何为讨探要主，端前在架框用使于关点观同不出提者作。

---

### [Preact](https://preactjs.com/)

**原文标题**: [Preact](https://preactjs.com/)

Preact 是一个轻量级的 React 替代方案，提供相同的现代 API 和虚拟 DOM 功能，具有高性能、小体积和生态系统兼容性等特点。

- 🚀 轻量高效：仅 3kB 大小，提供快速的虚拟 DOM 实现和自动性能优化
- 🏗️ 现代 API：完全兼容 React 的 Hooks 和组件模式，支持 useState 等特性
- 🌐 直接运行：无需转译即可在浏览器中直接使用，支持标准 HTML 属性
- 🔄 生态兼容：通过 preact/compat 层可无缝使用 React 生态系统中的数千个组件
- 📦 易于嵌入：小巧的体积使其可以轻松嵌入现有应用或构建独立部件
- ⚡ 开发高效：提供完整的开发工具链，包含实时预览和示例代码库
- 🌍 多语言支持：文档支持中文等十多种语言，方便全球开发者使用

---

### [Wallaby - 集成即时反馈的 AI 就绪测试运行器，内置于编辑器](https://wallabyjs.com/?utm_source=cooperpress&utm_medium=javascriptweekly&utm_content=javascriptweekly)

**原文标题**: [Wallaby - AI-Ready Test Runner with Instant Feedback in Your Editor](https://wallabyjs.com/?utm_source=cooperpress&utm_medium=javascriptweekly&utm_content=javascriptweekly)

Wallaby.js 是一款实时 JavaScript/TypeScript 测试运行工具，可在编码时即时显示测试结果和覆盖率，并提供高级调试功能和 AI 集成支持，显著提升开发效率。

- 🚀 **实时测试反馈** - 输入代码时立即运行相关测试，结果实时显示在编辑器旁
- 🎯 **智能测试执行** - 仅运行受代码更改影响的最小测试集，大幅提升速度
- 🔍 **高级调试功能** - 支持时间旅行调试、实时值查看和代码覆盖率显示
- 🤖 **AI 工具集成** - 为 AI 助手提供实时运行时上下文，辅助代码编写和修复
- 💻 **多编辑器支持** - 作为插件集成到现有 IDE 和测试框架，无供应商锁定
- 📊 **丰富可视化** - 内联错误报告、代码覆盖率指示器和交互式测试输出
- ⚡ **性能优化** - 支持选择性测试运行、性能分析和快照管理
- 💰 **效率提升** - 据估计可提升 10% 以上编码效率，被 10,000+ 公司采用

---

### [什么是 Invokers？无需 JavaScript 的交互性 - YouTube](https://www.youtube.com/watch?v=1NRx7PVupbQ)

**原文标题**: [What Are Invokers? Interactivity Without JavaScript - YouTube](https://www.youtube.com/watch?v=1NRx7PVupbQ)

这是 YouTube 网站页脚导航链接的概述，包含平台各项服务条款与功能说明。

- 📋 关于平台的基本信息和背景介绍
- 📰 官方新闻发布和媒体资源
- ©️ 版权声明与知识产权保护
- 📞 用户联系与客服渠道
- 🎬 内容创作者专属资源
- 💼 广告合作与商业推广
- 💻 开发者工具与 API 接口
- 📜 服务条款与使用协议
- 🔒 隐私政策与数据保护
- ⚖️ 平台政策与安全指南
- 🔧 YouTube 运作机制解析
- 🧪 新功能测试与体验
- 🏢 2025 年谷歌公司版权所有声明

---

### [调用者命令 API - 网络 API | MDN](https://developer.mozilla.org/en-US/docs/Web/API/Invoker_Commands_API)

**原文标题**: [Invoker Commands API - Web APIs | MDN](https://developer.mozilla.org/en-US/docs/Web/API/Invoker_Commands_API)

Invoker Commands API 允许通过声明式方式为按钮分配行为，无需 JavaScript 即可控制交互元素。

- 🎯 通过 commandfor 属性指定被控制的元素 ID，command 属性定义要执行的操作
- ⚡ 实现无 JavaScript 交互，提升页面加载速度和用户体验
- 🎪 支持控制弹窗 (popover)、对话框 (dialog) 等交互元素
- 🔧 提供 CommandEvent 接口处理自定义命令事件
- 💡 示例包含切换弹窗、显示模态框和图片旋转功能
- 🌐 兼容现代浏览器，包含 HTMLButtonElement 扩展属性
- 📚 规范定义完整，支持标准化和自定义命令类型

---

### [我们如何构建 v0 iOS 应用 - Vercel](https://vercel.com/blog/how-we-built-the-v0-ios-app)

**原文标题**: [ How we built the v0 iOS app - Vercel](https://vercel.com/blog/how-we-built-the-v0-ios-app)

Vercel 团队使用 React Native 和 Expo 开发了首款 iOS 原生应用 v0，旨在打造具有苹果设计奖水准的移动端 AI 代码生成工具。通过组合式架构实现流畅的聊天体验，并针对键盘交互、浮动输入框、内容动画等细节进行深度优化。

- 🎯 **目标定位** - 构建能与 iMessage 等原生应用媲美的移动端 AI 代码生成工具，而非功能完整的移动 IDE  
- 🛠️ **技术选型** - 经过多轮实验后选择 React Native+Expo，实现接近原生体验的跨平台开发  
- 💬 **聊天体验** - 采用组合式架构设计，通过多个自定义 Hook 协调消息动画、键盘交互和滚动逻辑  
- ⌨️ **键盘优化** - 集成 react-native-keyboard-controller，处理 iOS 系统更新导致的交互问题，实现自然的内容偏移  
- 🎭 **动画系统** - 使用 React Native Reanimated 实现消息渐入、错位浮现等精细动画效果  
- 🌊 **视觉设计** - 采用 Liquid Glass 毛玻璃效果，输入框支持图片粘贴和手势交互  
- 🔗 **代码共享** - 通过 OpenAPI 规范实现 Web 与移动端 API 类型共享，业务逻辑向服务端迁移  
- 📱 **原生集成** - 使用 Zeego 实现原生菜单，修复 Alert 显示问题，优化底部弹窗交互体验  
- 🚀 **未来规划** - 持续投入 React Native 生态建设，计划开源 AI 聊天应用开发库

---

### [Vercel 的 v0 版本](https://v0.app/)

**原文标题**: [v0 by Vercel](https://v0.app/)

这是一个展示 v0 平台模板库和功能的页面，提供多种可快速部署的网站模板和开发工具。

- 🎨 提供多样化模板库，涵盖仪表盘、登录页、作品集等 30 余种设计类型
- 🚀 支持 AI 快速生成应用，一键部署至 Vercel 平台实现秒级上线
- 🔧 集成开发工具链，包含 GitHub 同步、可视化编辑和设计系统管理
- 📱 具备多端适配能力，支持移动端构建和 iOS 应用实时开发
- 🎯 突出智能开发特性，内置 AI 代理可自动规划任务并连接数据库
- 💫 展示热门模板数据，如金融仪表盘 (26.5K 使用) 和 Cyberpunk 设计 (13.6K 使用) 等标杆案例
- 🔄 强调工作流整合，从提示词输入到发布部署形成完整闭环

---

### [用 Claude 代码管理我的邮件](https://jlongster.com/wrangling-email-claude-code)

**原文标题**: [Wrangling my email with Claude Code](https://jlongster.com/wrangling-email-claude-code)

作者通过 Claude Code 构建 Gmail 管理技能，利用 AI 技术解决邮件处理难题，显著提升工作效率。

- 📧 作者因不擅长邮件管理而错过重要机会，决定借助 AI 优化工作流程
- 🤖 放弃复杂的 n8n 自动化方案，选择通过 Claude Code 开发定制化邮件处理工具
- 🔧 使用 Skills 功能创建 Gmail 技能，通过 markdown 文档和 JavaScript 脚本实现邮件读取与搜索
- 🎯 成功实现两大核心需求：识别未回复邮件线程和自动生成公司信息电子表格
- 🔄 发现 AI 在保持对话上下文方面的强大能力，可连续进行数据追问和细化分析
- ⚠️ 遇到在技能目录内运行时指令失效的技术问题，通过切换目录解决
- ✨ 最终建立起高效的邮件管理系统，能自动追踪未回复邮件并生成公司调研报告

---

### [介绍代理技能 | Claude](https://www.claude.com/blog/skills)

**原文标题**: [Introducing Agent Skills | Claude](https://www.claude.com/blog/skills)

Anthropic 推出 Agent Skills 功能，让 Claude 通过加载包含指令、脚本和资源的技能文件夹来提升特定任务执行能力，该功能支持跨平台使用并具备按需调用特性。

- 🧩 可组合性：技能可堆叠使用，Claude 自动识别并协调所需技能
- 📦 跨平台兼容：同一技能格式适用于 Claude 应用、Claude Code 和 API
- ⚡ 高效运行：仅在需要时加载必要资源，保持系统响应速度
- 💻 代码执行：支持嵌入可执行代码，处理传统编程更可靠的任务
- 🛠️ 简易创建：通过交互式技能创建工具自动生成文件夹结构和配置文件
- 🔒 安全提醒：需注意代码执行权限，建议仅使用可信来源技能
- 🌐 多平台支持：面向 Pro/Max/Team/Enterprise 用户，提供官方技能库和自定义功能

---

### [获取失败](https://javascriptweekly.com/link/177765/web)

**原文标题**: [Failed to retrieve](https://javascriptweekly.com/link/177765/web)

无法总结：获取内容失败，状态码 403。

---

### [和谐智能——以每次 0.0001 美分的成本击溃 Next.js 服务器](https://www.harmonyintelligence.com/taking-down-next-js-servers)

**原文标题**: [Harmony Intelligence - Taking down Next.js servers for 0.0001 cents a pop](https://www.harmonyintelligence.com/taking-down-next-js-servers)

研究人员发现 Next.js 存在未授权拒绝服务漏洞，可通过单个 HTTP 请求使自托管服务器崩溃
- 🚨 漏洞影响：自托管 Next.js 中间件服务器（Vercel 托管不受影响），攻击成本极低仅需 0.0001 美分
- 🤖 发现方式：由 AI 应用安全代理在测试过程中自主发现并验证
- 💥 攻击原理：cloneBodyStream 函数无内存限制，攻击者可通过无限数据流耗尽服务器内存
- 🛡️ 修复方案：升级至 Next.js 15.5.5/16.0.0+ 或配置反向代理限制请求体大小
- ⚠️ 防护注意：基于代码的速率限制和 bodyParser 配置均无法防御此漏洞
- 📊 影响范围：全球约 55% 自托管 Next.js 应用受影响，CVSS 评分 7.5（高危）
- 📅 时间节点：2025 年 8 月 7 日披露，10 月 13 日发布补丁，11 月 26 日公开披露

---

### [tinyglobby：现代化与性能提升的成功典范 | e18e](https://e18e.dev/blog/tinyglobby-migration.html)

**原文标题**: [tinyglobby: a success story in modernization and performance | e18e](https://e18e.dev/blog/tinyglobby-migration.html)

作者从 JavaScript 依赖管理问题出发，通过参与 e18e 社区优化依赖数量，在修复 tsup 的 globby 替换问题时意外开启 tinyglobby 开源项目开发之旅。

- 🚀 为解决依赖臃肿问题而创建 tinyglobby，安装体积仅 179KB（globby 为 637KB）
- 🔒 依赖包数量从 24 个降至 3 个，显著降低供应链攻击风险
- 📈 已被 Vite/SWC/tsup 等主流构建工具和 React Router/SvelteKit等框架采纳
- ⚡ 经过持续优化，在多数场景下性能超越 fast-glob 和原生 glob
- 🧪 具备 100+ 测试用例，高活跃度维护且已实现零回归版本
- 🤝 基于 fdir 和 picomatch 两个核心依赖，致敬 globby 和 fast-glob 前辈项目
- 🎯 专注提供轻量级替代方案，覆盖大多数项目的核心 glob 需求

---

### [管理副作用：30 行代码内的 JavaScript 效应系统](https://lackofimagination.org/2025/11/managing-side-effects-a-javascript-effect-system-in-30-lines-or-less/)

**原文标题**: [Managing Side Effects: A JavaScript Effect System in 30 Lines or Less](https://lackofimagination.org/2025/11/managing-side-effects-a-javascript-effect-system-in-30-lines-or-less/)

传统应用程序代码常将业务逻辑与数据库操作等副作用耦合，导致测试困难且控制流不透明。本文提出通过声明式效果系统将操作描述与执行分离，使用纯函数构建可测试的业务流，并通过解释器统一处理副作用。

- 🧪 传统代码中业务逻辑与副作用紧密耦合，导致单元测试需依赖模拟环境
- 📝 效果系统通过 Success/Failure/Command 三种对象描述程序状态，延迟执行实际操作
- 🔗 通过 chain 函数和 effectPipe 组合器连接各个操作步骤
- 🎯 重构后的注册流程将验证、数据库查询、保存等步骤拆分为纯函数
- ✅ 可实现无模拟测试，直接验证返回的数据结构而非实际执行结果
- 📊 在解释器中统一添加日志记录和性能监控等横切关注点
- 🧩 实现了 Either Monad 错误处理和 Free Monad 副作用管理
- 🏗️ 遵循"功能性核心 + 命令式外壳"架构模式，提升代码可维护性

---

### [如何用 GSAP 打造电影级 3D 滚动体验 | Codrops](https://tympanus.net/codrops/2025/11/19/how-to-build-cinematic-3d-scroll-experiences-with-gsap/)

**原文标题**: [How to Build Cinematic 3D Scroll Experiences with GSAP | Codrops](https://tympanus.net/codrops/2025/11/19/how-to-build-cinematic-3d-scroll-experiences-with-gsap/)

本教程详细介绍了如何利用 GSAP、WebGL 和 Three.js 构建电影级 3D 滚动交互体验，通过滚动触发相机运动、光影变化和粒子特效，将静态场景转化为沉浸式视觉叙事。

- 🎬 通过 GSAP 控制滚动时间轴，将页面滚动与 3D 相机运动、物体旋转精准同步
- 🛠️ 集成 ScrollTrigger 和 ScrollSmoother 插件实现平滑滚动与动画触发机制
- 🌀 构建圆柱体 WebGL 场景，采用图像图谱技术实现无缝图片轮播效果
- ✨ 添加响应式粒子系统，通过旋转惯性算法增强视觉动态反馈
- 🎥 使用 Three.js 创建可交互 3D 场景，配合雾效和多重光源营造空间层次
- 📝 运用 SplitText 实现文字字符级动画，与滚动进度形成精准联动
- 🎛️ 通过自定义缓动函数精细控制动画节奏，创造电影级运动质感
- 📊 设计可视化进度指示器，实时反馈用户在场景中的浏览位置
- 🎞️ 采用分镜式场景规划，将长滚动页面转化为连贯的视觉叙事序列
- ⚡ 通过 WebGL 着色器编程优化渲染性能，确保复杂场景的流畅体验

---

### [博客 > 使用 AI 代理与 AST 迁移 6000 个 React 测试](https://eliocapella.com/blog/ai-library-migration-guide/)

**原文标题**: [Blog > Migrating 6000 React tests using AI Agents and ASTs](https://eliocapella.com/blog/ai-library-migration-guide/)

本文介绍了使用 AI 代理和 AST 技术迁移 6000 个 React 测试案例的完整流程，通过分阶段策略成功将 React Testing Library 从 v13 升级至 v14。

- 🗺️ 初始尝试直接使用 AI 迁移失败，转而通过深入研究制定详细迁移指南
- 🔧 采用双版本并行方案，通过 npm 同时安装 v13 和 v14 版本确保平稳过渡
- 🌳 利用 jscodeshift 工具构建 AST 代码转换器，并编写测试用例验证转换准确性
- 🤖 设计迭代式 AI 提示词，分批次迁移测试文件（每次 10 个），持续优化代码转换器
- 📈 迁移过程中代码转换器从 271 行扩展到 992 行，测试用例从 1 个增加到 14 个
- ⚠️ 发现 AI 存在上下文限制、倾向跳过难题等局限性，需人工监督确保质量
- ✅ 最终通过 50 个 PR 在一周内完成迁移，相比手动操作节省数月时间
- 💡 验证了 AI 在自动化重复性维护任务中的巨大潜力，让开发者能更专注于解决实际问题

---

### [FullCalendar - JavaScript 事件日历](https://fullcalendar.io/)

**原文标题**: [FullCalendar - JavaScript Event Calendar](https://fullcalendar.io/)

一款功能强大的 JavaScript 日历组件 FullCalendar，支持多种前端框架并具备高度可定制性

- 📅 支持多框架集成（React/Vue/Angular/原生 JS）
- ⚙️ 提供 300+ 配置项满足多样化需求
- 📦 采用模块化插件架构控制打包体积
- 🆓 拥有 10 年开源历史与 120+ 贡献者
- 💪 提供付费插件和技术支持增值服务
- 📊 每月超 200 万 NPM 下载和 7000 万 CDN 下载
- ⭐ 在 GitHub 获得 1.7 万星标认可
- 🔧 通过 npm 安装简单快捷（@fullcalendar/系列包）
- 🎯 默认显示月视图并支持事件标注
- 🔌 支持工具栏配置和视图切换功能

---

### [更佳认证](https://www.better-auth.com/)

**原文标题**: [Better Auth](https://www.better-auth.com/)

Better Auth 是一个专为 TypeScript 设计的全面身份验证框架，提供快速集成、多框架支持和丰富的功能，让开发者能够轻松构建安全可靠的身份验证系统。

- 🚀 **快速集成** - 一次性设置即可快速运行，支持多种流行框架
- 🔧 **框架无关** - 兼容 React、Vue、Svelte、Astro、Solid、Next.js 等主流框架
- 📧 **邮箱密码认证** - 内置邮箱密码认证功能，支持会话和账户管理
- 🌐 **社交登录** - 支持 GitHub、Google、Discord、Twitter 等 OAuth 提供商
- 🔒 **双重认证** - 提供多因素身份验证功能，增强账户安全性
- 🏢 **多租户支持** - 支持组织、成员、团队和邀请功能，具备访问控制
- 🧩 **插件生态** - 提供官方和社区插件，扩展应用功能
- ⭐ **用户好评** - 获得众多开发者认可，GitHub 星标超过 23.5K

---

### [更好的认证 1.4](https://www.better-auth.com/blog/1-4)

**原文标题**: [Better Auth 1.4](https://www.better-auth.com/blog/1-4)

Better Auth 1.4 版本发布，带来无状态认证、SCIM 配置、数据库查询优化、OAuth 流程增强、性能提升、SSO 域名验证等多项新功能和改进。

- 🚀 新增无状态认证功能，无需数据库即可管理会话
- 🔄 支持 SCIM 配置，简化多域场景下的身份管理
- ⚡ 数据库连接优化，端点延迟降低 2-3 倍
- 🔧 OAuth 流程支持自定义状态数据传递
- 🛡️ 新增 SSO 域名自动验证功能
- 📦 包体积优化，提供最小化版本
- 🔑 API 密钥插件支持二级存储
- 🆔 原生支持 UUID 作为主键类型
- 📧 改进邮箱变更流程，增加安全确认环节
- 📱 新增设备授权插件，支持受限设备登录
- 🍪 支持基于 Cookie 的账户存储
- 🐛 包含 250+ 项错误修复和性能改进
- ⚠️ 包含多项破坏性变更，需注意升级兼容性

---

### [我们教会 AI 编写真实的 Postgres 代码（并开源）| 泰格数据](https://www.tigerdata.com/blog/we-taught-ai-to-write-real-postgres-code-open-sourced-it)

**原文标题**: [We Taught AI to Write Real Postgres Code (And Open Sourced It) | Tiger Data](https://www.tigerdata.com/blog/we-taught-ai-to-write-real-postgres-code-open-sourced-it)

Timescale 公司开源了 pg-aiguide 项目，旨在提升 AI 生成 PostgreSQL 代码的质量。该项目通过提供专业优化的技能库和版本感知的文档检索，解决 AI 因训练数据混杂导致的代码质量问题，使 AI 能自动生成符合生产环境要求的 PostgreSQL 代码。

- 🎯 解决 AI 生成 SQL 的质量问题：传统 AI 工具从混杂网络数据学习的 SQL 存在数据类型混乱、索引错误等隐患
- 🛠️ 核心功能组合：提供 AI 优化技能库 + 版本感知文档检索 + 扩展生态文档支持
- 📚 智能技能库：包含 35 年 PostgreSQL 实战经验的最佳实践，如外键自动索引、时间戳规范等
- 🔍 精准文档检索：支持 PostgreSQL 15-18 版本特性识别，避免功能幻觉
- ⚡ 无缝集成：通过 MCP 协议和 Claude 插件实现免配置接入主流编程助手
- 📊 实测效果提升：生成的 SQL 在数据类型、索引策略、时间处理等方面显著优化
- 🌱 开源共建：邀请社区贡献扩展文档、专业技能和优化建议
- 🚀 应用场景：帮助开发者避免数据库设计陷阱，提升 AI 编程效率

---

### [Heat.js - JavaScript 热力图](https://www.william-troup.com/heat-js/)

**原文标题**: [Heat.js - JavaScript Heat Map](https://www.william-troup.com/heat-js/)

这是一个免费开源的数据可视化工具，具有丰富的功能和灵活的配置选项。

- 🆓 免费开源，采用 MIT 许可证
- 📦 零依赖，轻量级设计
- ⚡ 基于 TypeScript 开发，完美支持 React 和 Angular 等框架
- 🌍 默认支持 51 种语言
- ⚙️ 高度可配置，支持自定义触发器和文本翻译
- 📊 提供地图、图表、日期和统计等多种视图模式
- 🔧 每个视图都支持配置对话框
- 📈 支持趋势类型数据拆分
- 🎛️ 灵活的切换功能，便于数据细分分析
- 💾 支持导出 CSV、JSON、XML 等多种格式
- 📥 可从 JSON、TXT、CSV 等格式导入数据（支持拖拽）
- 🎨 提供 12 种主题，支持深色和浅色模式
- 🎯 每个视图可配置颜色范围
- 🔄 支持数据拉取功能
- 📅 支持自定义年度月份范围
- 🚀 持续更新，网站核心功能已完成，后续将不断完善文档和示例

---

### [Heat.js | 示例 | 按钮](https://www.william-troup.com/heat-js/examples/buttons.html)

**原文标题**: [Heat.js | Example | Buttons](https://www.william-troup.com/heat-js/examples/buttons.html)

网页开发基础示例
- 🌐 HTML 文档结构展示
- 📝 源代码查看功能
- 💻 网页编程入门实例
- 🔍 基础标签用法演示

---

### [GitHub - williamtroup/Heat.js：🌞 轻量级 JavaScript 库，用于生成可自定义的热图、图表和统计数据，以可视化基于日期的活动与趋势。](https://github.com/williamtroup/Heat.js)

**原文标题**: [GitHub - williamtroup/Heat.js: 🌞 A lightweight JavaScript library that generates customizable heat maps, charts, and statistics to visualize date-based activity and trends.](https://github.com/williamtroup/Heat.js)

Heat.js 是一个轻量级 JavaScript 库，用于生成可自定义的热图、图表和统计数据，以可视化基于日期的活动与趋势。

- 🌞 轻量级且无依赖，支持 TypeScript 开发
- 📊 提供四种视图模式：地图、图表、日期和统计
- 🎨 完全可定制，支持 CSS 主题和 12 种额外主题
- 🌍 支持 51 种语言，兼容所有现代浏览器
- 📥 支持从 JSON、CSV 等格式导入数据
- 📤 可将数据导出为 CSV、JSON、XML 等多种格式
- 🔧 提供完整的 API 和配置选项
- 📦 可通过 npm 安装或使用 CDN 链接
- 📄 采用 MIT 许可证，开源且免费使用

---

### [🎉 Ant Design 6.0 震撼发布！🎉 · Issue #55804 · ant-design/ant-design · GitHub](https://github.com/ant-design/ant-design/issues/55804)

**原文标题**: [🎉 Ant Design 6.0 is Here! 🎉 · Issue #55804 · ant-design/ant-design · GitHub](https://github.com/ant-design/ant-design/issues/55804)

Ant Design 6.0 正式发布，这是经过广泛讨论和多轮测试后的稳定版本。本次升级聚焦于技术优化和兼容性提升，支持 React 18 及以上版本，采用纯 CSS 变量架构，并全面实现组件语义化。升级过程平滑，v5 用户可直接升级至 v6，无需兼容工具。v5 将进入一年维护期。同时新增了 Masonry 布局、Tooltip 滑动等组件功能，并宣布了 Ant Design X 2.0 的发布。

- 🎉 **版本发布**：Ant Design 6.0 正式推出，基于大量社区反馈和测试迭代，提供稳定体验
- ⚛️ **技术升级**：最低 React 版本要求提升至 18，移除旧版兼容代码，推荐使用 React 19
- 📦 **性能优化**：默认启用 React Compiler，提升运行时效率，支持按需配置
- 🌈 **样式架构**：采用纯 CSS 变量模式，支持实时主题切换和零运行时样式生成
- 🚫 **兼容调整**：彻底停止对 IE 浏览器的支持，移除相关兼容逻辑
- 🧩 **语义化组件**：所有组件完成 DOM 结构语义化改造，支持 RTL 和动态样式配置
- 🔥 **新增功能**：引入 Masonry 瀑布流布局、Tooltip 滑动支持、InputNumber 旋钮模式等
- 📋 **升级指南**：v6 完全兼容 v5，直接升级即可，需确保运行环境为 React 18+
- 🚀 **生态扩展**：同步发布 Ant Design X 2.0，专为 AI 场景设计，增强交互与渲染能力
- 💝 **社区致谢**：感谢众多贡献者的参与，项目已积累 96.6K Stars 和 2314 位贡献者

---

### [chroma.js API 文档！](https://gka.github.io/chroma.js/)

**原文标题**: [chroma.js api docs!](https://gka.github.io/chroma.js/)

chroma.js 是一个轻量级、无依赖的 JavaScript 颜色处理库，支持多种颜色格式转换、颜色操作和插值功能，适用于数据可视化和色彩设计。

- 🎨 支持多种颜色格式读取与转换（十六进制、RGB、HSL、Lab 等）
- 🔄 提供颜色操作功能（明暗调整、饱和度修改、混合等）
- 📏 包含多种颜色插值模式（线性、贝塞尔曲线、不同色彩空间）
- 🛠️ 内置色阶生成与色彩比例计算工具
- 🌐 支持 Node.js 与浏览器环境，可部分导入以减少打包体积
- 📚 集成 ColorBrewer 配色方案，便于数据可视化应用
- 🧪 提供色彩对比度、色差计算等辅助功能

---

### [GitHub - vercel/nft: Node.js 依赖追踪工具](https://github.com/vercel/nft)

**原文标题**: [GitHub - vercel/nft: Node.js dependency tracing utility](https://github.com/vercel/nft)

这是一个用于确定应用程序运行时所需文件的 Node.js 依赖追踪工具，类似于@vercel/ncc 但不进行打包，通过树摇优化实现相同效果。

- 📦 追踪 Node.js 应用运行所需的全部文件（包括 node_modules）
- 🔍 支持条件导出和导入字段的自动分析
- ⚙️ 提供多种配置选项（基础路径、处理目录、自定义解析等）
- 🎯 默认支持 TypeScript 文件解析
- 📊 可输出文件包含原因分析报告
- 🚀 支持文件 IO 并发控制（默认 1024）
- 🔧 允许通过钩子函数自定义文件系统操作
- 💾 提供缓存机制提升构建性能
- ❌ 支持自定义忽略规则排除特定文件
- 📄 采用 MIT 开源协议，项目包含 1.5k 星标和 163 个分支

---

### [发布 v1.0.0 · cedarjs/cedar · GitHub](https://github.com/cedarjs/cedar/releases/tag/v1.0.0)

**原文标题**: [Release v1.0.0 · cedarjs/cedar · GitHub](https://github.com/cedarjs/cedar/releases/tag/v1.0.0)

CedarJS 框架发布 v1.0.0 稳定版本，这是从 RedwoodJS 迁移而来的重要里程碑，包含 ESM 实验性支持、安全更新和多项功能优化。

- 🎉 正式发布 v1.0.0 稳定版本，标志着从 RedwoodJS 到 CedarJS 的平滑迁移完成
- 🔄 与 RedwoodJS v8.9.0 完全兼容，无破坏性变更，多家大型企业已投入生产环境使用
- ⚡ 新增实验性 ESM 项目支持，可通过在 package.json 中添加"type": "module"启用
- 🛡️ 包含多项第三方包安全更新，提升项目安全性
- ⏰ 支持 Cron 定时调度后台任务，增强任务管理能力
- 🤖 文档优化 AI 友好性，新增 LLMs 专用文档和 AI 工具集成功能
- 🐛 修复了 CLI 工具、Storybook、Vite 服务器等多个组件的错误和兼容性问题
- 📚 更新了身份验证文档，修复了 Netlify Identity 配置说明
- 🔧 完成 Redwood 到 Cedar 的品牌重命名，统一使用 yarn cedar 命令
- 📦 升级了 NX 等依赖版本，确保与 Node.js v20.19+ 的兼容性

---

### [GitHub - caoccao/swc4j: swc4j (Java 版 SWC) 是一款基于 JVM 的超高速 JavaScript 与 TypeScript 编译打包工具。](https://github.com/caoccao/swc4j)

**原文标题**: [GitHub - caoccao/swc4j: swc4j (SWC for Java) is an ultra-fast JavaScript and TypeScript compilation and bundling tool on JVM.](https://github.com/caoccao/swc4j)

swc4j 是一个基于 JVM 的超快速 JavaScript 和 TypeScript 编译与打包工具，属于 Javet 项目的一部分，支持多平台运行和多种代码处理功能。

- 🚀 超快速编译工具，支持 JavaScript、TypeScript、JSX、TSX 等多种语言
- 🌍 跨平台兼容，支持 Android、Linux、macOS 和 Windows 系统
- 🔧 提供丰富功能，包括语法解析、AST 访问、代码转换、压缩和源码映射
- ⚡ 支持 TypeScript 到 JavaScript 的转译，以及 JSX/TSX 的处理
- 🛡️ 内置代码净化器，提供对象保护、关键字限制和标识符管理等安全功能
- 📦 提供 Maven 和 Gradle 依赖配置，支持多种架构的本地库
- 📚 包含详细文档、教程和博客，帮助开发者快速上手和使用

---

### [GitHub - ibrahimcesar/react-lite-youtube-embed：📺 专为 React 应用打造的默认私密、更快速、更简洁的 YouTube 嵌入组件](https://github.com/ibrahimcesar/react-lite-youtube-embed)

**原文标题**: [GitHub - ibrahimcesar/react-lite-youtube-embed: 📺 ‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎< A private by default, faster and cleaner YouTube embed component for React applications />](https://github.com/ibrahimcesar/react-lite-youtube-embed)

这是一个用于 React 应用的轻量级 YouTube 嵌入组件，默认保护隐私，加载更快且界面更简洁。

- 📦 轻量高效 - 压缩后体积小于 5KB，仅加载缩略图直到用户点击播放
- 🛡️ 隐私保护 - 默认不加载 YouTube cookies 和跟踪代码
- ⚡ 性能优化 - 相比标准 iframe 减少 500KB 负载和数十个网络请求
- 🔍 SEO 友好 - 支持结构化数据和 JSON-LD VideoObject
- ♿ 无障碍访问 - 完整的键盘导航和屏幕阅读器支持
- 📱 响应式设计 - 适配各种设备屏幕尺寸
- 🎯 功能丰富 - 支持懒加载、播放器事件监听、高质量缩略图
- 🔒 安全可靠 - 包含 SLSA 构建证明和 CodeQL 安全扫描
- 📚 完善文档 - 提供完整 API 参考、实时示例和性能指南

---

### [首页 | React Lite YouTube 嵌入](https://ibrahimcesar.github.io/react-lite-youtube-embed/)

**原文标题**: [Home | React Lite YouTube Embed](https://ibrahimcesar.github.io/react-lite-youtube-embed/)

React Lite YouTube Embed 是一个轻量级、高性能的 YouTube 视频嵌入组件，通过延迟加载和隐私保护优化用户体验。

- ⚡ 极速加载：仅预载轻量缩略图（约 10-30KB），相比标准 iframe 节省超过 500KB 资源
- 🔒 隐私保护：默认使用 youtube-nocookie.com 域名，用户点击播放前完全阻断 Cookie 追踪
- 📦 超小体积：压缩后 JS+CSS 总计小于 5KB，支持摇树优化且无第三方依赖
- ♿ 无障碍设计：完整键盘导航、屏幕阅读器支持，符合 WCAG 2.1 标准
- 🎬 功能完整：支持播放列表、程序化控制、自定义缩略图及 SEO 结构化数据
- 📘 TypeScript 原生：提供完整类型定义，支持智能提示和类型检查
- 🚀 快速集成：通过 npm 安装后即可使用基础嵌入组件

---

### [GitHub - P4sca1/cron-schedule：适用于Node.js、Deno、Bun及浏览器的零依赖cron解析与调度器](https://github.com/P4sca1/cron-schedule)

**原文标题**: [GitHub - P4sca1/cron-schedule: A zero-dependency cron parser and scheduler for Node.js, Deno, Bun and the browser.](https://github.com/P4sca1/cron-schedule)

这是一个零依赖的 cron 解析器和调度器，支持 Node.js、Deno、Bun 和浏览器环境，提供灵活的定时任务管理功能。

- ⏰ 支持解析 cron 表达式并获取未来/过去的执行时间
- 🚀 提供两种调度器：基于定时器的精确调度和基于间隔的批量调度
- 📦 零依赖、轻量级且支持 tree-shaking
- 🌐 兼容多种运行环境：Node.js、Deno、Bun 和浏览器
- 🔧 支持完整的 cron 语法特性，包括列表、范围、步长值和时间别名
- ⚡ 提供丰富的 API：获取下一个/上一个执行时间、匹配日期、迭代器等
- 📚 通过 npm、yarn、pnpm 和 CDN 多种方式安装使用
- 🛡️ 采用 MIT 开源协议，支持错误处理和任务取消功能

---

### [发布 v3.11.0 · vuetifyjs/vuetify · GitHub](https://github.com/vuetifyjs/vuetify/releases/tag/v3.11.0)

**原文标题**: [Release v3.11.0 · vuetifyjs/vuetify · GitHub](https://github.com/vuetifyjs/vuetify/releases/tag/v3.11.0)

Vuetify 3.11.0 版本发布，包含组件升级、新功能添加和多项问题修复。

- 🏅 VCalendar 和 VHotkey 组件从实验室升级为核心框架组件
- 🚀 新增主题层级选项、数据表多排序模式和键盘修饰符支持
- 📅 日期选择器支持事件标记和横屏模式
- 🔧 修复无限滚动、评分组件键盘控制等多项问题
- 🎯 实验室组件 VHotkey 改进对齐方式和分隔符显示
- 📝 文本域新增最大高度属性，工具栏添加折叠位置控制
- 🎨 进度环组件支持圆角样式，分割线新增渐变效果
- ⚡ 树视图优化大型数据交互性能，添加无数据状态插槽
- 🔒 覆盖层新增视口边距属性，保持与激活器连接
- 📊 数据表支持初始排序顺序，应用颜色到内部控件

---

### [GitHub - fable-compiler/Fable: F# 转 JavaScript、TypeScript、Python、Rust 和 Dart 编译器](https://github.com/fable-compiler/Fable)

**原文标题**: [GitHub - fable-compiler/Fable: F# to JavaScript, TypeScript, Python, Rust and Dart Compiler](https://github.com/fable-compiler/Fable)

Fable是一个将F#语言编译为JavaScript、TypeScript、Python、Rust和Dart的开源编译器项目，基于FSharp编译器服务构建，旨在让F#成为JavaScript生态系统中的一等公民。

- 🌐 项目主页：fable.io/，采用 MIT 开源协议
- ⭐ GitHub 获得 3k 星标，314 个复刻分支
- 🔄 支持多语言输出：JavaScript、TypeScript、Python、Rust、Dart
- 🛠️ 开发环境要求：.NET SDK 6+、Node.js、Python 3、Uv、Rust、Dart
- 📚 提供详细入门指南和构建脚本（build.sh/build.cmd）
- 🐛 支持通过 GitHub 提交问题报告和功能请求
- 👥 拥有 152 位贡献者，社区活跃度较高
- 💻 主要使用F#开发（占比94%），辅以Rust、Python等语言
- 🔄 项目包含多个子模块：fable-standalone、Fable.Core、Fable.Cli 等

---

### [精密 AI——无需编写测试的自动化前端测试](https://www.meticulous.ai/?utm_source=jsweekly&utm_medium=referral&utm_campaign=q4)

**原文标题**: [Meticulous AI - Automated Frontend Testing Without Writing Tests](https://www.meticulous.ai/?utm_source=jsweekly&utm_medium=referral&utm_campaign=q4)

Meticulous AI 是一款通过记录用户操作自动生成测试用例的智能测试平台，无需人工编写或维护测试代码，帮助企业实现零维护、无卡顿的自动化测试覆盖。

- 🚀 自动记录用户在开发/测试环境中的操作行为并生成持续进化的可视化端到端测试套件
- 🧩 支持主流前端框架（NextJS/React/Vue/Angular 等），通过添加脚本标签快速集成
- ⚡ 基于 Chromium 的确定性调度引擎，消除测试波动，实现闪电级测试执行速度
- 🔄 自动更新测试用例：新增功能时自动补充测试，过时用例自动淘汰
- 🛡️ 默认采用后端响应模拟机制，避免测试数据干扰，无需配置测试账户
- 📊 在代码合并前预览对现有工作流的影响，已被 Dropbox、Notion 等 100 多家组织采用
- 🎯 可并行执行数千次测试，120 秒内返回结果，有效预防代码回归问题

---

### [GitHub Actions 分析功能现已推出](https://depot.dev/blog/now-available-github-actions-analytics?utm_source=fnf&utm_medium=newsletter&utm_campaign=depot-november&utm_term=jsweekly&utm_content=github-actions-analytics)

**原文标题**: [Now available: GitHub Actions analytics](https://depot.dev/blog/now-available-github-actions-analytics?utm_source=fnf&utm_medium=newsletter&utm_campaign=depot-november&utm_term=jsweekly&utm_content=github-actions-analytics)

Depot 推出了 GitHub Actions 分析功能，帮助开发者全面监控和优化 CI/CD 流水线性能。

- 📊 **性能趋势追踪**：可视化查看任务时长、成功率与失败率随时间的变化
- 💻 **资源使用监控**：实时掌握所有任务的 CPU 和内存使用情况
- 🔍 **智能任务分析**：快速定位最慢任务和最高 CPU 消耗任务
- ⚡ **深度钻取功能**：支持按仓库、运行器类型或具体任务进行筛选
- 📈 **详细性能指标**：点击单个任务即可查看日志、指标和性能数据
- 💡 **优化建议系统**：自动提供提升构建性能的具体建议
- 🎯 **智能洞察功能**：自动分析任务资源使用情况，推荐运行器规格调整方案
- 💰 **成本效益分析**：显示相比 GitHub 托管运行器的预估节省成本
- 📱 **实时数据更新**：所有 Depot 客户现已可用该功能

---

### [Pintura 图像编辑器，一款强大的 JavaScript 图像编辑器 SDK](https://pqina.nl/pintura/)

**原文标题**: [Pintura Image Editor, a Powerful JavaScript Image Editor SDK](https://pqina.nl/pintura/)

Pintura Image Editor 是一款功能强大的 JavaScript 图像编辑 SDK，支持跨平台集成和高度自定义配置，帮助开发者快速实现专业级图像编辑功能。

- 🖼️ 支持裁剪、旋转、滤镜、标注等完整图像编辑功能
- 📱 响应式设计，完美适配移动端和桌面端
- 🔧 提供丰富配置选项，可自定义界面语言和图标
- 🚀 支持多种前端框架和文件上传库集成
- 💾 具备浏览器端图像压缩和格式转换能力
- 🎯 可设置裁剪比例限制和叠加引导图层
- 🖋️ 提供强大的标注工具和形状绘制功能
- 🌙 支持明暗主题切换和 CSS 自定义样式
- 🔗 可集成 AI 服务和视频编辑扩展功能
- ⭐ 被全球 3,137 家公司使用，评分 4.9/5

---

### [TSDiagram - 使用 TypeScript 将图表代码化](https://tsdiagram.com/)

**原文标题**: [TSDiagram - Diagrams as code with TypeScript](https://tsdiagram.com/)

文章概述了人工智能在现代社会中的广泛应用及其带来的机遇与挑战。

- 🤖 人工智能技术正迅速渗透各行各业，提升生产效率
- 💡 机器学习算法通过数据分析为决策提供有力支持
- 🌐 自然语言处理技术改善了人机交互体验
- ⚠️ 数据隐私和算法偏见是需要关注的重要问题
- 🔧 企业需建立完善的 AI 伦理规范和监管机制
- 📈 合理运用 AI 将创造新的经济增长点和社会价值

---

### [GitHub - 3rd/tsdiagram：使用TypeScript创建图表并规划代码。](https://github.com/3rd/tsdiagram)

**原文标题**: [GitHub - 3rd/tsdiagram: Create diagrams and plan your code with TypeScript.](https://github.com/3rd/tsdiagram)

TSDiagram 是一个基于 TypeScript 的在线图表工具，用于快速绘制数据模型图并支持代码规划。

- 🚀 通过 TypeScript 类型别名、接口和类定义数据模型
- 🎯 自动高效布局节点，手动调整后保持其他节点自动排列
- 💾 通过 URL 和本地存储持久化文档状态
- 📤 支持将图表导出为 SVG 格式
- 🛠️ 未来规划包含函数调用展示、自定义 TypeScript 上下文等功能
- 🌟 最终目标发展为代码可视化平台，展示代码连接与数据流
- 📊 项目采用 GPL-3.0 许可证，包含 498 个星标和 21 个复刻

---

### ["子网格" | 我能用吗... HTML5、CSS3 等支持表格](https://caniuse.com/?search=subgrid)

**原文标题**: ["subgrid" | Can I use... Support tables for HTML5, CSS3, etc](https://caniuse.com/?search=subgrid)

CSS Subgrid 是 CSS Grid Layout Module Level 2 的功能，允许具有自身网格的网格项在一个或两个维度上与父网格对齐。

- 🎯 实现网格项与父网格的精确对齐
- 🔄 支持单维度或双维度的网格继承
- 💻 通过 grid-template-columns: subgrid 属性控制列对齐
- 📏 通过 grid-template-rows: subgrid 属性控制行对齐

---

### [全新 CSS 子网格布局设计 • 乔希·W·科莫](https://www.joshwcomeau.com/css/subgrid/)

**原文标题**: [Brand New Layouts with CSS Subgrid • Josh W. Comeau](https://www.joshwcomeau.com/css/subgrid/)

CSS Subgrid 是 CSS Grid 布局的重要扩展，允许子元素继承父网格的布局结构，解决了嵌套元素无法直接参与网格布局的问题。它不仅简化了复杂布局的实现，还开启了新的设计可能性，使兄弟元素能够动态响应彼此的内容变化。

- 🎨 **子网格基础**：通过 `grid-template-rows: subgrid` 和 `grid-template-columns: subgrid` 继承父网格的轨道定义，使嵌套元素参与同一网格布局
- 🚀 **新布局可能**：子网格允许不同层级的元素共享网格结构，实现内容动态对齐和响应式设计，如图片和文本列的自适应调整
- ⚠️ **常见陷阱**：子网格默认仅占用单一行/列，需使用 `grid-row: span X` 显式预留多行空间，且网格线编号在子网格中会重置
- 🛠️ **开发工具**：现代浏览器（Firefox、Chrome、Safari）都提供了网格开发工具，可可视化调试子网格结构
- 📱 **浏览器支持**：自 2023 年起所有主流浏览器均支持子网格，但全球支持率仍低于 90%，可使用 `@supports` 特性查询提供降级方案
- 🔄 **布局限制**：子网格与流体网格（如 `auto-fill`/`auto-fit`）不兼容，需要明确定义网格轨道数量
- 💡 **实用案例**：适用于价格表对齐、作品集卡片布局等需要深层嵌套元素对齐的场景，比传统 Flexbox/Grid 组合更灵活

---

### [未列出的 GitHub Gist 中的秘密已报告给秘密扫描合作伙伴 - GitHub 更新日志](https://github.blog/changelog/2025-11-25-secrets-in-unlisted-github-gists-are-now-reported-to-secret-scanning-partners/)

**原文标题**: [Secrets in unlisted GitHub gists are reported to secret scanning partners - GitHub Changelog](https://github.blog/changelog/2025-11-25-secrets-in-unlisted-github-gists-are-now-reported-to-secret-scanning-partners/)

GitHub 宣布从 2025 年 11 月 25 日起，将把在未列出的 GitHub Gist 中发现的公开泄露密钥报告给相应的密钥扫描合作伙伴。

- 🔍 GitHub Gist 分为公开（带 public 标签）和未列出（带 secret 标签）两种类型
- ⚠️ 所有 Gist 都能通过 URL 被任何人查看，不存在真正私密的 Gist
- 🚨 未列出的 Gist 因常被误认为私密而成为密钥泄露的盲区
- 🤝 GitHub 与 AWS、OpenAI、Stripe 等数百家合作伙伴建立密钥扫描计划
- 📧 发现泄露密钥时会通知密钥发行方，并向启用扫描的仓库开发者发送警报
- 💡 Gist 是分享代码片段的工具，未列出的 Gist 不会出现在 Discover 中且不可搜索
- 🔗 未列出的 Gist 仅通过 URL 分享，任何获得 URL 的人都能查看内容
- 💡 如需真正私密代码存储，建议创建私有仓库而非使用 Gist

---

### [适用于复古电脑与游戏机的在线 C、BASIC 及汇编语言 IDE - Retro Game Coders](https://ide.retrogamecoders.com/)

**原文标题**: [Online C, BASIC, and Assembler IDE for Vintage Computers and Consoles - Retro Game Coders](https://ide.retrogamecoders.com/)

这是一个复古游戏开发集成环境 (IDE) 的界面功能概述，主要面向 8 位游戏平台开发

- 📁 文件管理功能：新建程序、导入文件、重命名、删除文件等操作
- 🔄 版本控制：同步、发布项目、推送/拉取服务器代码
- 💾 下载选项：支持源代码、程序文件、磁盘映像等多种格式下载
- 🌐 分享功能：生成可玩链接和嵌入式代码
- 🎮 多平台支持：涵盖 Atari、NES、Sega 等经典游戏机和 Commodore、Apple 等老式电脑
- ⌨️ 输入控制：支持摇杆、手柄、键盘等多种输入设备映射
- ❓ 帮助系统：提供 IDE 使用说明和关于信息
- 👥 社区功能：用户注册登录、项目发布等社交功能
- ⚙️ 调试工具：包含断点表达式设置等开发调试功能

---

### [AddyOsmani.com - Gemini 3.0 新特性详解](https://addyosmani.com/blog/gemini-3/)

**原文标题**: [AddyOsmani.com - What's New in Gemini 3.0](https://addyosmani.com/blog/gemini-3/)

Gemini 3.0 作为谷歌最新发布的多模态 AI 模型，在推理能力、编程辅助和图像生成三大领域实现突破性升级，并深度集成至搜索、开发工具和创意平台中。

- 🧠 核心推理能力显著提升，在数学、科学及对话基准测试中全面超越前代，支持百万 token 多模态上下文处理
- 💻 编程能力革新，支持自然语言生成完整应用（Vibe Coding），在 WebDev Arena 等开发基准中位列榜首
- 🤖 推出 Antigravity 智能 IDE，可实现多代理并行编程，具备代码编辑、终端操作和浏览器测试一体化能力
- 🖥️ 增强版 Gemini CLI 终端工具支持代码重构、环境部署等实际操作，大幅提升开发效率
- 🎨 全新图像模型 Nano Banana Pro 支持 4K 生成、智能修图和跨场景角色一致性，成为真正的设计合作伙伴
- 🔗 深度多模态架构实现文本、图像、代码的统一处理，支持跨模态复杂问题推理
- 🌐 首发即全面集成至 Google 搜索、Gemini 应用、AI Studio 等产品，提供免费使用层级

---

### [介绍克劳德·奥普斯 4.5 版 \ 安瑟瑞克](https://www.anthropic.com/news/claude-opus-4-5)

**原文标题**: [Introducing Claude Opus 4.5 \ Anthropic](https://www.anthropic.com/news/claude-opus-4-5)

Anthropic 发布新一代 AI 模型 Claude Opus 4.5，该模型在编程、智能体操作和计算机应用领域表现卓越，并在日常办公任务中实现显著效能提升。通过优化定价策略和增强多平台集成，为开发者和企业用户提供更高效的 AI 解决方案。

- 🚀 核心升级：在编程、智能体工作流和计算机操作领域达到全球顶尖水平，深度研究与办公文档处理能力显著提升
- 💰 定价优化：输入/输出 token 价格降至$5/$25 每百万，大幅降低 Opus 级能力的使用门槛
- 🛠️ 平台扩展：全面覆盖 API、三大云平台及桌面应用，支持 Excel/Chrome 集成与长对话自动摘要
- 🧠 智能突破：内部测试显示其能自主解决复杂系统故障，在 30 分钟编码会话中保持稳定表现
- 📊 效能飞跃：多项基准测试领先，SWE-bench 多语言测试中 7/8 编程语言排名第一，Aider 多语言测试性能提升 10.6%
- 🎯 精准控制：新增"effort"参数实现动态算力分配，中档效能即可用 76% 更少 token 达到 Sonnet 4.5 最佳水平
- 🔒 安全增强：抗提示注入攻击能力行业领先，被评估为目前对齐程度最高的前沿模型
- ⚡ 效率提升：终端测试显示任务完成速度提升 2-4 倍，部分场景 token 消耗降低 65%
- 🤖 智能体进化：支持自主能力迭代优化，在办公自动化任务中仅需 4 轮迭代即达峰值性能
- 🌐 生态整合：Claude Code 新增计划模式与桌面端并行会话，浏览器扩展面向 Max 用户全面开放

---

### [从 GitHub 迁移至 Codeberg
⚡
Zig 编程语言](https://ziglang.org/news/migrating-from-github-to-codeberg/)

**原文标题**: [
      Migrating from GitHub to Codeberg
      â¡
      Zig Programming Language
    ](https://ziglang.org/news/migrating-from-github-to-codeberg/)

Zig 编程语言项目宣布从 GitHub 迁移至 Codeberg 平台，主要基于对 GitHub 工程质量下降、持续集成系统故障频发以及违反项目无 AI 政策等问题的考量。

- 🚫 **平台质量恶化** - GitHub 被微软收购后工程文化衰退，界面卡顿且功能故障频发
- 🔧 **持续集成失效** - GitHub Actions 出现随机调度等严重缺陷，导致主分支提交无法正常检测
- 🤖 **违反 AI 政策** - GitHub 强制推广 Copilot 功能与项目严格的无 AI/无 LLM 政策相冲突
- 💸 **赞助模式调整** - 逐步弃用 GitHub Sponsors，呼吁赞助者转向非营利平台 Every.org
- 📦 **迁移方案实施** - 立即将主代码库设为只读，新问题编号从 30000 开始计数
- 📋 **问题处理原则** - 保留现有 GitHub 工单和 PR，仅需修改时再迁移至新平台
- 🌱 **支持开源生态** - 选择非营利平台 Codeberg 以捍卫开源共同体价值

---

