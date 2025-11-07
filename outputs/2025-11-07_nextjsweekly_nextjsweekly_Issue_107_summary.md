### [在Next.js 16中实现next-intl国际化与'use cache'功能 | Aurora Scharff](https://aurorascharff.no/posts/implementing-nextjs-16-use-cache-with-next-intl-internationalization/)

**原文标题**: [Implementing Next.js 16 'use cache' with next-intl Internationalization | Aurora Scharff](https://aurorascharff.no/posts/implementing-nextjs-16-use-cache-with-next-intl-internationalization/)

Next.js 16的'use cache'指令与next-intl国际化库目前存在兼容性问题，本文探讨了问题根源、未来解决方案及当前可用的临时解决方法。

- 🚫 Next.js 16的'use cache'指令与next-intl库存在兼容性问题，因为getTranslations()默认依赖headers()读取请求头信息
- 🌐 next-intl通过中间件将locale作为请求头传递，避免手动在组件树中传递区域参数，但这会导致动态渲染
- 🔧 临时解决方案需要配置generateStaticParams和setRequestLocale启用静态渲染，并在使用缓存的组件中显式传递locale参数
- ⚡ 使用'use cache'的组件需要Suspense边界包装，支持部分预渲染功能，提升页面加载性能
- 🎯 未来next/root-params API将解决深层参数访问问题，使next-intl无需依赖headers()即可访问locale参数
- 📝 当前需在页面组件中提取locale参数并传递给缓存组件，同时保持非缓存组件的正常使用方式
- 🔗 作者提供了完整的代码示例和分支演示，展示了在Next.js 16电商demo中的具体实现方案

---

### [Next.js 16 有哪些新特性](https://www.trevorlasn.com/blog/whats-new-in-nextjs-16)

**原文标题**: [What's new in Next.js 16](https://www.trevorlasn.com/blog/whats-new-in-nextjs-16)

Next.js 16 正式发布，这是该框架的一个重要里程碑版本，专注于稳定实验性功能、提升性能并简化开发体验。此次更新引入了异步路由参数、默认启用 Turbopack 打包工具、改进缓存 API 等核心特性，同时移除了部分过时功能如 AMP 支持和运行时配置。

- 🚀 路由参数全面异步化，页面、布局和路由处理器需使用 `await` 获取参数，支持流式渲染和并发处理
- ⚡ Turbopack 打包工具成为默认选项，显著提升开发服务器启动速度和热更新响应能力
- 🧠 正式支持 React Compiler，自动优化组件重渲染，减少手动记忆化代码
- 💾 缓存 API 结束实验阶段，新增 `cacheLife` 和 `cacheTag` 提供精确的缓存控制
- 🔄 中间件更名为代理功能，仅支持 Node.js 运行时，强化请求拦截和重定向能力
- 🗑️ 移除 AMP 相关功能，简化框架体积
- 🛡️ 图像组件安全增强，默认缓存 TTL 延长至 4 小时，支持远程模式白名单
- ⚙️ 废弃运行时配置，全面转向环境变量管理
- 🔧 内置 ESLint 整合移除，需直接使用 ESLint 工具链
- 📦 构建适配器开放实验性接口，支持自定义部署目标

---

### [若你讨厌React服务器组件，请看这个 - YouTube](https://www.youtube.com/watch?v=C84YEp-8-hI)

**原文标题**: [Watch this if you hate React Server Components - YouTube](https://www.youtube.com/watch?v=C84YEp-8-hI)

这是YouTube网站页脚导航链接的概述，包含平台各项服务条款与功能说明。

- 📋 关于平台的基本信息与介绍
- 📰 媒体与新闻相关资源
- ©️ 版权声明与保护政策
- 📞 用户联系与客服渠道
- 🎬 内容创作者专属资源
- 💼 广告合作与商业推广
- 💻 开发者工具与API接口
- 📜 服务条款与使用协议
- 🔒 隐私保护与数据政策
- ⚖️ 平台政策与安全指南
- 🔧 YouTube运作机制解析
- 🧪 新功能测试与体验
- 🏢 2025年谷歌公司版权所有

---

### [React Server组件：它们真的能提升性能吗？](https://www.developerway.com/posts/react-server-components-performance)

**原文标题**: [React Server Components: Do They Really Improve Performance?](https://www.developerway.com/posts/react-server-components-performance)

本文通过数据驱动的方式比较了客户端渲染(CSR)、服务端渲染(SSR)和React服务端组件(RSC)在相同应用和测试环境下的性能表现，重点关注初始加载性能以及客户端与服务端数据获取的影响。

- 📊 **性能测试方法**：在6倍CPU降速和慢速4G网络环境下，使用Chrome性能面板测量LCP、侧边栏可见时间、消息可见时间和页面可交互时间
- ⚡ **客户端渲染表现**：初始加载LCP达4.1秒，但页面一旦加载即可完全交互，页面间切换最快
- 🚀 **服务端渲染优势**：将LCP从4.1秒大幅提升至1.61秒，但会产生2.39秒的"无交互间隙"
- 🔄 **服务端数据获取**：虽然会略微降低LCP至2.16秒，但能让完整页面体验更早可见
- 🔧 **Next.js迁移影响**：从Pages迁移到App Router可能使性能变差，需要重写数据获取逻辑
- ⚠️ **React服务端组件限制**：单独使用RSC不会改善性能，必须结合Streaming和Suspense才能看到改进
- 🎯 **关键发现**：Streaming和Suspense才是性能提升的关键，而非RSC本身
- 💡 **实施建议**：需要完整的应用重构和正确的Suspense边界设置才能获得性能收益

---

### [文档驱动开发：我如何无需手写一行代码构建生产级博客 | Daniel Kliewer | Daniel Kliewer](https://danielkliewer.com/blog/2025-11-03-document-driven-development-nextjs-blog)

**原文标题**: [Document-Driven Development: How I Built a Production Blog Without Writing a Single Line of Code By Hand | Daniel Kliewer | Daniel Kliewer](https://danielkliewer.com/blog/2025-11-03-document-driven-development-nextjs-blog)

本文介绍了一种名为"文档驱动开发"的AI辅助编程方法，作者通过详细文档规范和自然语言提示，在无需手动编写代码的情况下构建了完整的Next.js博客系统。该方法强调前期文档规划的重要性，通过14个核心文档定义项目架构，利用AI编码代理实现自动化开发，最终完成具备路由、响应式设计和语义搜索等功能的完整博客平台。

- 📝 重新定义"氛围编程"为使用自然语言创建软件，降低开发门槛
- 🏗️ 提出文档驱动开发理念，将文档作为系统架构蓝图
- 📋 建立14个核心文档规范，涵盖需求、架构、测试到部署全流程
- 🤖 采用预提示方法训练AI理解开发意图，提升需求分析质量
- 🔄 通过迭代式开发流程，配合检查清单确保代码质量
- ⚡ 实现从概念到可运行博客的完整构建，验证方法可行性
- 💡 强调前期规划比编码更重要，AI放大而非替代人类思考
- 🌟 展示AI辅助开发可产出更专业、可维护的软件产品

---

### [尽可能将状态封装在组件中](https://blacksheepcode.com/posts/encapsulate_as_much_state_as_possible)

**原文标题**: [Encapsulate as much state as possible in your component](https://blacksheepcode.com/posts/encapsulate_as_much_state_as_possible)

本文讨论了在React组件设计中应尽可能封装状态的理念，通过对比两种组件接口设计方式，说明将状态转换逻辑封装在组件内部能提升代码可维护性和使用便利性。

- 🚫 错误设计：通过props完全控制组件状态会使父组件承担状态转换逻辑
- 🔄 状态转换：测试时需额外创建包装组件来模拟状态变化，增加复杂度
- ✅ 正确方案：组件内部管理状态，仅暴露异步操作函数作为接口
- 🧪 测试优势：内部状态管理的组件测试更贴近实际使用场景
- 🔍 现实案例：自动完成组件封装搜索、防抖、取消等复杂逻辑
- 🛠️ 工具影响：TanStack Query等状态管理工具影响了组件接口设计模式
- 💡 核心思想：将固有复杂性封装在组件内部，简化消费者使用体验

---

### [升级至Solito 5 | Solito](https://solito.dev/v5)

**原文标题**: [Upgrade to Solito 5 | Solito](https://solito.dev/v5)

Solito 5 版本进行了重大更新，移除了对 react-native-web 的依赖，实现了 Web 端的零配置支持，同时保持 iOS 和 Android 平台无变化。更新内容包括组件直接返回 Next.js 组件、支持所有 Web 属性如 className 和 style，并采用了 Web 优先的文件策略。升级需注意样式调整和属性扁平化等破坏性变更。

- 🚀 **移除 react-native-web 依赖**：Solito 5 不再依赖 react-native-web，Web 端实现零配置
- 🌐 **Web 端组件优化**：组件直接返回 Next.js 组件，支持所有 DOM 属性如 className 和 style 对象
- 📱 **原生平台无变化**：iOS 和 Android 平台保持原有行为不变
- 🛠️ **文件策略调整**：采用 .native.tsx 扩展名，默认文件为 Web 优先
- ⚠️ **破坏性变更**：TextLink 和 Link 组件不再包含默认样式，需手动添加
- 🔄 **属性扁平化**：viewProps 和 textProps 被移除，属性直接传递给组件
- 📦 **升级指南**：安装 Solito 5、调整样式、为 TextLink 添加样式、检查破坏性变更
- 🎯 **设计理念**：受 Zeego 2 启发，采用 Web 优先的抽象方式，提升开发体验

---

### [civic-auth-examples/packages/civic-auth/nextjs 位于主分支 · civicteam/civic-auth-examples · GitHub](https://github.com/civicteam/civic-auth-examples/tree/main/packages/civic-auth/nextjs)

**原文标题**: [civic-auth-examples/packages/civic-auth/nextjs at main · civicteam/civic-auth-examples · GitHub](https://github.com/civicteam/civic-auth-examples/tree/main/packages/civic-auth/nextjs)

这是一个GitHub仓库页面，展示civicteam组织下的civic-auth-examples项目的基本信息

- 🔒 公开仓库，需要登录才能更改通知设置
- 🍴 项目被复刻3次
- ⭐ 获得3个星标收藏
- 💻 代码仓库正常显示
- 🐛 存在5个未解决的问题
- 🔄 有17个拉取请求待处理
- ⚡ 可执行自动化操作
- 📊 项目统计信息可查看
- 🚨 安全相关功能模块
- ❗ 页面加载时出现错误提示，需要重新加载
- 📋 提供代码、问题、拉取请求、操作、项目、安全、统计等导航选项

---

### [Storybook 10](https://storybook.js.org/blog/storybook-10/)

**原文标题**: [Storybook 10](https://storybook.js.org/blog/storybook-10/)

Storybook 10 发布，主要包含 ESM 独占支持、模块自动模拟、类型安全的 CSF 工厂等核心功能优化，同时引入实验性测试语法和 RSC 组件测试。

- ✂️ **ESM 独占支持**：唯一破坏性变更，安装体积减少 29%，需 Node 20.16+/22.19+/24+ 支持
- 🧩 **模块自动模拟**：与 Vitest 合作开发，兼容 Vite/Webpack，支持开发与生产环境
- 🏭 **类型安全 CSF 工厂**：减少模板代码，提供更优类型提示，目前仅支持 React
- 💫 **UI 编辑与共享优化**：新增二维码移动端预览和一键编辑器跳转功能
- 🏷️ **标签过滤增强**：支持排除特定标签故事，可配置默认过滤状态
- 🔀 **框架生态升级**：支持 Svelte 异步组件、Next.js 16 和 Vitest 4
- 🧪 **实验性测试语法**：通过 .test 方法附加测试，支持从侧边栏隐藏测试故事
- ⚛️ **实验性 RSC 测试**：与 React 生态合作推出服务端组件组件测试方案

---

### [GitHub - lazarv/typescript-plugin-directives：TypeScript语言服务插件，为“use…”指令添加内联提示和悬停信息](https://github.com/lazarv/typescript-plugin-directives)

**原文标题**: [GitHub - lazarv/typescript-plugin-directives: TypeScript LS plugin adding inline hints and hover info for \"use …\" directives](https://github.com/lazarv/typescript-plugin-directives)

这是一个为 TypeScript 语言服务开发的插件，专门用于增强 IDE 对 "use …" 指令的支持，提供内联提示、悬停信息和验证功能。

- 🎯 **指令检测** - 自动识别模块作用域和导出函数中的指令
- 💡 **内联提示** - 在声明和导入旁显示如 `<use server>` 的小型注释
- 📝 **悬停工具提示** - 为标记指令的导出提供详细的悬停信息
- ✅ **验证功能** - 检查无效指令并提供有用的错误信息
- 🔍 **导入追踪** - 识别导入函数是否源自指令标记的导出
- 🔌 **可扩展性** - 第三方包可通过声明合并添加自定义指令
- 🎨 **框架无关** - 纯静态分析，无运行时依赖或指令语义
- 📦 **通用支持** - 支持 .js、.ts、.jsx 和 .tsx 文件类型
- ⚙️ **简单安装** - 通过 npm 或 pnpm 安装，在 tsconfig.json 中配置插件
- 🔧 **开发友好** - 支持自定义指令扩展，自动获取智能提示和验证

---

### [GitHub - blazejkustra/react-compiler-marker: 在VSCode/Cursor中高亮显示经React编译器优化的组件 ✨](https://github.com/blazejkustra/react-compiler-marker)

**原文标题**: [GitHub - blazejkustra/react-compiler-marker: Highlights React components optimized by the React Compiler in VSCode/Cursor ✨](https://github.com/blazejkustra/react-compiler-marker)

这是一个用于VSCode/Cursor的React编译器标记扩展，可高亮显示被React编译器优化的React组件，提供优化状态可视化、悬停详情提示和编译输出预览功能。

- ✨ 显示组件优化状态（✨表示已优化，🚫表示编译失败）
- 🛠️ 支持通过命令面板激活/停用标记或单文件检查
- 📋 提供悬停工具提示显示详细优化信息
- 👁️ 可预览当前文件的编译输出结果
- ⚙️ 支持自定义Babel插件路径配置
- 🐛 已知问题包括匿名函数提示显示异常和大文件性能略降
- 🌐 MIT开源协议，支持问题提交和功能贡献

---

### [像分叉代码一样分叉存储桶 | Tigris 对象存储](https://www.tigrisdata.com/blog/fork-buckets-like-code/?utm_source=nextjs)

**原文标题**: [Fork Buckets Like You Fork Code | Tigris Object Storage](https://www.tigrisdata.com/blog/fork-buckets-like-code/?utm_source=nextjs)

Tigris对象存储引入桶分叉功能，可像代码分支一样快速创建数据集的独立副本，支持开发测试和实验场景。

- 🚀 即时创建数据分叉：无需全量复制即可获得生产数据的隔离副本，秒级完成创建与销毁
- 🕰️ 完整时间旅行能力：基于不可变对象存储和快照技术，实现整个存储桶的时间点版本控制
- 🔧 多样化应用场景：支持开发环境隔离、数据集版本控制、A/B测试和智能体沙箱等用例
- 💡 技术实现原理：通过FoundationDB全局有序日志记录元数据，分叉时仅需引用快照版本无需移动数据
- 🤖 智能体工作流示例：可为每个智能体创建独立数据分叉，避免冲突并确保结果可重现
- ⚡ 核心优势：数据隔离、即时回滚、完美一致性、调试友好，提升开发效率与数据安全性

---

### [平台之外：Vercel是否正在设计编程语言的未来？- DEV社区](https://dev.to/herrington_darkholme/the-new-programming-frontier-why-vercel-is-redefining-the-language-2ij0)

**原文标题**: [Beyond the Platform: Is Vercel Designing the Future of Programming Languages? - DEV Community](https://dev.to/herrington_darkholme/the-new-programming-frontier-why-vercel-is-redefining-the-language-2ij0)

Vercel正在通过引入新的语言级特性来重新定义编程语言的未来，这些特性旨在简化分布式系统中数据与计算的复杂性管理。

- 🌐 Vercel推出的新特性挑战了JavaScript语义，展示了编程语言可能向原生管理多运行时、网络透明性及任务持久性演进的方向
- 🔄 Server Actions通过序列化闭包实现客户端与服务器逻辑的无缝调用，使远程过程调用如同本地函数般简单
- 💾 'use cache'指令利用闭包和参数自动生成缓存键，提供了语言级别的缓存机制，优化数据访问性能
- ⚙️ 'use workflow'指令引入持久化函数概念，支持在分布式环境中暂停和恢复执行，确保任务可靠性和确定性重放
- 📜 编程语言历史表明其不断演进以处理新复杂度，Vercel的特性可能标志着语言开始内建数据管理能力
- 🔗 序列化闭包、代数效应和增量计算是支撑这一愿景的核心计算机科学概念，分别处理计算移动、资源安全访问和高效缓存
- 🚀 Vercel的举措可能预示未来语言将内建错误监控、数据隐私和可观测性，让开发者更专注于业务逻辑而非基础设施

---

### [你的网址即你的状态](https://alfy.blog/2025/10/31/your-url-is-your-state.html)

**原文标题**: [Your URL Is Your State](https://alfy.blog/2025/10/31/your-url-is-your-state.html)

作者通过PrismJS配置URL的发现，阐述了URL作为状态管理工具的强大功能，强调优秀URL设计能存储应用状态、实现分享与持久化，并提供了具体实现方法和最佳实践。

- 🔗 URL可编码完整应用状态，如PrismJS配置、GitHub代码高亮和地图坐标
- 🎯 路径段适合层级导航，查询参数处理筛选配置，锚点实现页面内定位
- ⚡ 现代API（URLSearchParams）和React路由简化了URL状态管理
- 📝 应将筛选、分页、视图模式等可分享状态存入URL，避免存储敏感数据或临时状态
- 🚫 常见误区包括内存态丢失、敏感信息泄露、命名不透明和过度复杂的状态编码
- 💡 优秀URL兼具状态容器、用户界面和数据契约三重价值，是Web原生解决方案

---

### [Octoverse：AI引领TypeScript登顶，每秒新增一位GitHub开发者 - GitHub官方博客](https://github.blog/news-insights/octoverse/octoverse-a-new-developer-joins-github-every-second-as-ai-leads-typescript-to-1/)

**原文标题**: [Octoverse: A new developer joins GitHub every second as AI leads TypeScript to #1 - The GitHub Blog](https://github.blog/news-insights/octoverse/octoverse-a-new-developer-joins-github-every-second-as-ai-leads-typescript-to-1/)

2025年GitHub开发者数量突破1.8亿，平均每秒新增一名开发者，AI技术推动TypeScript成为平台最常用编程语言，全球开发活动呈现爆发式增长。

- 👥 开发者规模达1.8亿，年增3600万，印度年增超500万成为最大增长源
- 🤖 AI驱动开发变革：80%新用户首周使用Copilot，110万仓库集成LLM SDK
- ⚡ TypeScript超越Python/JavaScript登顶，严格类型系统更适配AI辅助开发
- 🌍 全球协作加速：私有仓库贡献量达49.7亿，公有仓库年增1.21亿
- 📈 开发效能提升：合并PR超43.2亿次（+23%），代码推送近10亿次
- 🔧 AI基础设施爆发：vLLM、Ollama等AI工具仓库贡献者年增150%
- 🛡️ 安全自动化进阶：关键漏洞修复时间缩短30%，Dependabot配置仓库翻倍
- 📊 Python稳居AI领域主导：50%新AI仓库采用，Jupyter笔记本使用量增长75%
- 🌱 新兴市场崛起：巴西、印尼、尼日利亚开发者数量实现倍数级增长
- 🚀 智能代理普及：GitHub Copilot代理功能已生成超100万次PR

---

### [2025年抓取Next.js网站的秘籍——诡术开发者](https://www.trickster.dev/post/scraping-nextjs-web-sites-in-2025/)

**原文标题**: [Scraping Next.js web sites in 2025 – Trickster Dev](https://www.trickster.dev/post/scraping-nextjs-web-sites-in-2025/)

本文介绍了在2025年如何通过解析Next.js网站中的self.__next_f.push()调用来提取数据，并提供了使用njsparser库的具体方法和代码示例。

- 🚀 React作为主流前端框架，通过组件化和虚拟DOM解决Web应用状态与UI同步问题
- 🔗 Next.js扩展React功能，提供路由优化和服务器端渲染(SSR)支持全栈开发
- 💧 传统Next.js站点通过__NEXT_DATA__脚本实现数据水合，新版本改用React服务端组件
- 📦 新架构将数据分块序列化为React特有格式，通过self.__next_f.push()调用嵌入页面
- 🛠️ 使用njsparser Python库可解析Next.js飞行数据，文中提供了完整代码示例
- 🔍 通过CLI工具可检测网站是否包含可解析的Next.js数据
- 📊 解析得到的数据呈分块嵌套结构，需遍历提取所需字段

---

