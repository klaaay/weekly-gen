### [React 状态周报 第 450 期：2025 年 11 月 5 日](https://react.statuscode.com/issues/450)

**原文标题**: [React Status Issue 450: November 5, 2025](https://react.statuscode.com/issues/450)

本期简报聚焦于 React 生态系统的最新动态，包括 Storybook 10 的重大更新、安全漏洞警示、开发工具升级以及社区技术实践分享。

- 📢 Storybook 10 发布：全面转向 ESM 模块，体积减少 29%，新增模块自动模拟功能并支持 Next.js 16 与 Vitest 4
- ⚠️ React Native 社区 CLI 发现高危漏洞：JFrog 安全团队披露可能导致远程代码执行的安全风险
- 📊 技术趋势分析：Evil Martians 统计显示 React 在初创公司中仍占主导地位，Facebook 内部使用 140 层上下文提供器
- 🛠️ 开发工具更新：React Native Big Calendar 发布 v4.19，React Uploady 升级至 1.12 版本，新增文件上传组件
- 🎨 创意实践：Three.js 与 React 结合生成艺术创作，Next.js 实现 ChatGPT 集成演示
- 📦 基础设施动态：Node.js v24 成为新 LTS 版本，Vercel 正式支持 Bun 运行时
- 🔧 组件生态：推出 react-jsonschema-form 6.0 表单构建工具，React Syntax Highlighter 代码高亮组件更新
- ⚡ 性能优化：React Compiler 1.0 配合 TanStack Start 实现自动记忆化优化
- 🎮 游戏开发：开源项目 Godot Engine 支持嵌入 React Native 应用，实现 JavaScript 全 API 调用

---

### [Storybook 10](https://storybook.js.org/blog/storybook-10/)

**原文标题**: [Storybook 10](https://storybook.js.org/blog/storybook-10/)

Storybook 10 发布，主要特性包括仅支持 ESM 模块、安装体积减少 29%、模块自动模拟、类型安全的 CSF 工厂等核心改进，同时引入实验性测试语法和 RSC 组件测试功能。

- ✂️ 仅支持 ESM 模块：唯一破坏性变更，安装体积减少 29%，需 Node 20.16+/22.19+/24+ 版本支持
- 🧩 模块自动模拟：与 Vitest 协作开发，兼容 Vite/Webpack，支持开发与生产环境
- 🏭 类型安全 CSF 工厂：减少样板代码，提供更优类型提示，目前仅支持 React
- 💫 界面编辑与共享优化：新增二维码分享功能，支持快速跳转编辑器
- 🏷️ 标签过滤排除：支持通过标签隐藏故事，可配置默认过滤状态
- 🔀 Svelte 异步组件支持：新增 Svelte 异步组件和状态模拟功能
- ⚙️ 生态集成：支持 Next.js 16 和 Vitest 4，保持向后兼容
- 🧪 实验性功能：推出测试语法减少侧边栏杂乱，开展 RSC 组件测试早期访问计划

---

### [错误](https://react.statuscode.com/link/176572/web)

**原文标题**: [Error](https://react.statuscode.com/link/176572/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='vitest.dev', port=443): Max retries exceeded with url: / (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1000)')))

---

### [组件故事格式 (CSF) | Storybook 文档](https://storybook.js.org/docs/api/csf/csf-next?ref=storybookblog.ghost.io)

**原文标题**: [Component Story Format (CSF) | Storybook docs](https://storybook.js.org/docs/api/csf/csf-next?ref=storybookblog.ghost.io)

CSF Next 是 Storybook 组件故事格式的新演进版本，通过工厂函数模式提供完整的类型安全支持，简化插件配置并增强开发体验。

- 🧪 CSF Next 是预览功能，采用工厂函数模式实现全类型安全的故事编写
- ⚙️ 通过 defineMain 定义类型安全的主配置文件，自动推断项目类型
- 🔧 使用 definePreview 配置预览环境，支持插件类型自动补全
- 📝 通过 preview.meta() 定义组件元数据，支持绝对路径导入
- 🎭 使用 meta.story() 创建故事，支持参数合并和装饰器串联
- 🔄 提供 .extend() 方法基于现有故事创建新故事，支持属性智能合并
- 🧪 实验性 .test() 方法支持为故事附加测试用例
- ⬆️ 支持从 CSF 3 自动升级或从旧版本手动迁移
- ✅ 兼容现有 MDX 文档页面，支持渐进式迁移
- 🔧 更新 Vitest 配置以适配新格式，简化测试设置
- 📚 提供详细迁移指南和常见问题解答

---

### [SurveyJS - 用于调查与表单的 JavaScript 库](https://surveyjs.io/?utm_source=react_status&utm_medium=referral)

**原文标题**: [SurveyJS - JavaScript Libraries for Surveys and Forms](https://surveyjs.io/?utm_source=react_status&utm_medium=referral)

SurveyJS 是一个开源 JavaScript 表单构建库套件，提供完整的自托管表单管理系统解决方案，支持多行业数据收集需求。

- 📜 表单库：免费开源的 JavaScript 库，通过 JSON 动态渲染表单并收集响应
- 🎨 调查创建器：拖拽式表单构建器，实时生成 JSON 表单定义，需商业许可证
- 📊 仪表板：交互式数据可视化工具，提供图表和表格分析调查结果
- 🖨️ PDF 生成器：将表单转换为可编辑或只读 PDF 文件，支持无纸化办公
- 🔒 数据安全：支持自托管部署，确保敏感数据完全自主控制
- 🎯 完全定制：基于 CSS 的主题编辑器，可深度定制品牌视觉风格
- 🔗 框架集成：支持 React、Angular、Vue 等主流前端框架
- 💼 永久授权：一次性付费的永久开发者许可证，无版权费用
- 🏥 多行业适用：涵盖医疗、教育、金融、电商等十余个行业场景
- 🌐 后端兼容：可与任意服务器和数据库组合使用，提供完整集成示例

---

### [GitHub - borndotcom/react-native-godot：React Native Godot - 在 React Native 应用中嵌入 Godot 引擎](https://github.com/borndotcom/react-native-godot)

**原文标题**: [GitHub - borndotcom/react-native-godot: React Native Godot - Embed Godot Engine in React Native apps](https://github.com/borndotcom/react-native-godot)

这是一个允许在 React Native 应用中嵌入 Godot 引擎的开源项目，支持 Android 和 iOS 平台，采用 MIT 许可证。

- 🎮 支持在 React Native 应用中嵌入 Godot 游戏引擎
- 📱 兼容 Android 和 iOS 双平台
- 🔄 支持启动、停止、重启和暂停/恢复 Godot 实例
- 🧵 Godot 运行在独立线程，不影响主线程性能
- 🎯 可将 Godot 窗口嵌入到 React Native 界面中
- 🔧 支持从 TypeScript/JavaScript 调用完整 Godot API
- 📦 通过 NPM 包@borndotcom/react-native-godot 分发
- 🛠️ 提供详细的示例应用和配置指南
- 🐛 支持原生代码调试和远程调试功能
- 📚 包含完整的文档说明和进阶使用指南

---

### [Godot 引擎 - 免费开源的 2D 与 3D 游戏引擎](https://godotengine.org/)

**原文标题**: [Godot Engine - Free and open source 2D and 3D game engine](https://godotengine.org/)

Godot 是一款免费开源的跨平台游戏引擎，支持 2D/3D 游戏及 XR 内容开发，具有创新场景系统和多语言编程支持，并拥有活跃的开源社区。

- 🎮 支持 2D/3D 游戏开发与 XR 创意实现
- 🔄 提供跨平台部署能力（桌面/移动/网页/主机）
- 💡 采用创新节点场景设计架构
- 🛠️ 支持 GDScript/C#/C++/GDExtension 多语言开发
- 🌐 持续更新版本（当前稳定版 4.5.1，开发版 4.6 进行中）
- 📚 提供完善文档并鼓励社区参与改进
- 💝 接受个人与企业赞助支持发展
- 🐞 设有问题反馈机制保障引擎稳定性

---

### [CVE-2025-11953 React Native CLI 严重远程代码执行漏洞](https://jfrog.com/blog/CVE-2025-11953-critical-react-native-community-cli-vulnerability/)

**原文标题**: [CVE-2025-11953 Critical RCE in React Native CLI](https://jfrog.com/blog/CVE-2025-11953-critical-react-native-community-cli-vulnerability/)

JFrog 安全团队发现 React Native 开发工具包存在关键 RCE 漏洞 CVE-2025-11953，攻击者可通过开发服务器执行任意系统命令，影响每周下载量达 200 万次的@react-native-community/cli 组件。

- 🚨 漏洞评级为 CVSS 9.8 分，影响@react-native-community/cli-server-api 组件 4.8.0 至 20.0.0-alpha.2 版本
- 💻 默认情况下运行 Metro 开发服务器的 React Native 项目均受影响，涉及 npm start 等启动命令
- 🌐 结合 React Native 核心代码的网络安全问题，开发服务器会暴露至外部网络
- ⚡ Windows 平台可实现完整命令执行，macOS/Linux 平台存在受限执行风险
- 🔧 解决措施：升级至 20.0.0 以上版本或启动时添加--host 127.0.0.1 参数
- 📮 攻击原理：/open-url 端点未过滤用户输入，直接传递给 open() 函数触发命令执行
- ⚠️ 开发服务器默认绑定所有网络接口，加剧攻击风险

---

### [GitHub - react-native-community/cli: React Native 社区命令行工具 - 助您构建 RN 应用的工具集](https://github.com/react-native-community/cli)

**原文标题**: [GitHub - react-native-community/cli: The React Native Community CLI - command line tools to help you build RN apps](https://github.com/react-native-community/cli)

React Native Community CLI 是一个独立于 React Native 核心的命令行工具集，用于帮助开发者构建 React Native 应用，作为 @react-native-community/cli NPM 包发布。

- 🛠️ 项目性质：从 React Native 核心中提取的独立命令行工具，遵循 "Lean Core" 理念
- 📦 发布方式：通过 @react-native-community/cli NPM 包分发
- ⭐ 项目热度：获得 2.8k 星标和 931 个复刻
- 📄 许可证：采用 MIT 开源许可证
- 🔄 兼容性：与不同版本的 React Native 保持兼容（从 ^0.59.0 到 ^0.82.0）
- 🚀 主要功能：包含项目初始化、启动、配置管理等命令
- 👥 维护团队：由 Callstack 和 Meta 的开发者共同维护
- 💻 技术支持：提供创建新项目和在现有项目中使用的方法
- ⚠️ 注意事项：建议不要独立于 React Native 更新 CLI 版本
- 📚 文档完善：包含配置、命令、插件等详细文档说明

---

### [Facebook.com 拥有 140 层上下文提供者：reactjs](https://old.reddit.com/r/reactjs/comments/1onblrs/facebookcom_has_140_layers_of_context_providers/)

**原文标题**: [Facebook.com has 140 layers of context providers : reactjs](https://old.reddit.com/r/reactjs/comments/1onblrs/facebookcom_has_140_layers_of_context_providers/)

一项对主流社交媒体网站 React Context 层数的调查显示，Facebook 以 140 层位居榜首，Bluesky 和 Pinterest 分别以 125 层和 116 层紧随其后。Facebook 工程师解释这是为优化性能而拆分的细粒度状态管理策略，通过减少重渲染提升体验。尽管存在开发体验问题，但目前未造成显著性能瓶颈。

- 🔍 Facebook 工程师证实拆分 Context 是为精准控制重渲染范围
- ⚡ 性能优化策略：将路由等复合上下文拆分为独立上下文避免连锁更新
- 🛠️ 当前依赖 React DevTools 分析重渲染原因，暂未采用 Context Selectors 方案
- 📊 前三名平台均超过 100 层 Context，Instagram(99) 和 Threads(87) 次之
- 🎯 细粒度 Context 通常仅包含布尔值等简单数据，最小化值变更影响范围
- 🔄 工程师通过 Chrome 性能面板→React DevTools 的流程定位渲染问题
- 💡 React 团队转向并发存储方案，Context Selectors 提案已被编译器优化替代

---

### [为何初创公司选择 React（以及何时不应选择）——来自 Evil Martians 团队博客的《火星纪事》](https://evilmartians.com/chronicles/why-startups-choose-react-and-when-you-should-not)

**原文标题**: [Why startups choose React (and when you shouldn't)—Martian Chronicles, Evil Martians’ team blog](https://evilmartians.com/chronicles/why-startups-choose-react-and-when-you-should-not)

2025 年数据显示 React 在初创企业中获得 88.6% 的融资份额，但各框架生态系统普遍存在 85% 的项目废弃率。小框架在项目存活率和开发者满意度方面表现更优，选择框架应综合考虑团队规模、招聘需求和技术特点。

- 🚀 React 占据初创企业融资的 88.6%（28.4 亿美元/28.5 亿美元），主要优势在于庞大的人才库和生态系统
- ⚰️ 所有框架平均 85% 的 GitHub 项目已停止维护，但 React 仍有 110 万个活跃项目
- 🌱 Svelte 高质量项目存活率最高（36.1%），其开发者满意度达 88%
- 📊 Vue 在管理后台领域表现突出，开发者满意度一年增长 12% 达 87%
- 🔄 跨框架项目平均星标数达 1.5 万，表明框架无关架构更易成功
- 💡 选择建议：快速扩张团队选 React，稳定团队可选 Vue，性能关键应用考虑 Svelte
- 🏢 大型企业适合 Angular 的强约束架构，满意度回升至 54%
- 📈 数据显示"融资选择"与"开发者偏好"存在显著差距

---

### [React 网络 - 示例](https://react-networks-lib.rackout.net/)

**原文标题**: [React Networks - Example](https://react-networks-lib.rackout.net/)

文章概述了人工智能在现代社会中的广泛应用及其带来的影响。

- 🤖 人工智能技术正迅速渗透到各行各业，从医疗诊断到金融分析
- 💡 机器学习算法通过大数据训练不断提升准确性和效率
- 🌐 自然语言处理技术使机器能够理解和生成人类语言
- ⚖️ 人工智能发展也引发隐私保护和就业结构变化的讨论
- 🔮 未来人工智能将与人类智慧深度融合，创造新的可能性

---

### [React Compiler 1.0 与 TanStack Start 联袂登场！ - YouTube](https://www.youtube.com/watch?v=-3-17PRN7jg)

**原文标题**: [React Compiler 1.0 with TanStack Start! - YouTube](https://www.youtube.com/watch?v=-3-17PRN7jg)

这是 YouTube 平台页脚导航链接的简要说明。

- ℹ️ 关于平台的基本信息
- 📰 媒体相关新闻与公告
- ©️ 版权政策与保护措施
- 📞 用户联系渠道
- 🎬 内容创作者资源
- 💼 广告合作机会
- 👨‍💻 开发者工具与 API
- 📑 服务条款说明
- 🔒 隐私保护政策
- ⚖️ 平台政策与安全指南
- 🔧 平台运作机制介绍
- 🧪 新功能测试信息
- 🏢 2025 年谷歌公司版权所有

---

### [全栈 Next.js 15 课程 - Next 之路](https://www.road-to-next.com/?utm_source=react_weekly&utm_medium=referral&utm_campaign=next_course)

**原文标题**: [Full-Stack Next.js 15 Course - The Road to Next](https://www.road-to-next.com/?utm_source=react_weekly&utm_medium=referral&utm_campaign=next_course)

这是一门由 Robin Wieruch 推出的全栈 Web 开发视频课程，专注于 Next.js 15 和 React 19，旨在帮助开发者从初级进阶到高级水平，掌握构建现代 SaaS 产品所需的技能。

- 🚀 课程通过两个学习路径（Web 开发者之旅和软件工程师之旅）系统教授全栈开发，涵盖服务器组件、数据库操作、身份验证等核心概念
- 🛠️ 采用现代技术栈，包括 Next.js 15、React 19、Prisma、Supabase、TypeScript 等业界流行工具
- 💼 包含实际项目实践，学员将逐步构建并部署自己的 SaaS 入门套件，获得真实开发经验
- 👨‍🏫 讲师 Robin Wieruch 拥有十余年开发经验，是畅销 JavaScript 书籍作者，曾与多家知名企业和政府机构合作
- 🎯 适合前端转全栈、不同编程语言背景、想要成为高级开发者或技术创始人的各类学员
- 💬 提供 Discord 社区支持、完成证书和 14 天退款保证，现有 1720 名学员参与学习
- 💰 提供两个套餐选择：开发者之旅$249，软件工程师之旅$349，包含更多高级内容和 SaaS 入门套件

---

### [使用 Three.js 创作生成艺术作品](https://tympanus.net/codrops/2025/01/15/creating-generative-artwork-with-three-js/)

**原文标题**: [Creating a Generative Artwork with Three.js](https://tympanus.net/codrops/2025/01/15/creating-generative-artwork-with-three-js/)

本教程指导使用 Three.js 和网格系统创建生成艺术，灵感源自 Lygia Clark 的极简几何设计，涵盖项目搭建、网格生成、规则打破、色彩应用及交互界面实现。

- 🎨 从 Lygia Clark 的几何绘画中提取灵感，构建动态生成艺术
- 📐 利用 50×86 网格系统，通过实例化网格高效渲染几何元素
- 🔄 引入噪声函数打破规则网格，创造自然随机布局
- 🎨 提取九色调色板，按列宽动态分配色彩分布
- 🛠️ 集成 Leva GUI 实现参数实时调整，增强创作灵活性
- 🌐 展示网格系统多样性，可模拟 Gerhard Richter 等艺术家风格
- 📚 推荐 GSAP 动画课程辅助深入学习 JavaScript 动画技术

---

### [获取失败](https://react.statuscode.com/link/176584/web)

**原文标题**: [Failed to retrieve](https://react.statuscode.com/link/176584/web)

无法总结：获取内容失败，状态码 403。

---

### [在 ChatGPT 中运行 Next.js：深入探讨原生应用集成 - Vercel](https://vercel.com/blog/running-next-js-inside-chatgpt-a-deep-dive-into-native-app-integration)

**原文标题**: [Running Next.js inside ChatGPT: A deep dive into native app integration - Vercel](https://vercel.com/blog/running-next-js-inside-chatgpt-a-deep-dive-into-native-app-integration)

本文介绍了如何将完整的 Next.js 应用嵌入 ChatGPT 的三层 iframe 架构中，通过七个关键技术补丁解决了静态资源加载、路由导航、CORS 跨域等兼容性问题，使开发者能够直接部署现有 Next.js 应用到 ChatGPT 平台。

- 🚪 **架构突破** - 通过 MCP 协议实现 Next.js 应用在 ChatGPT 三层 iframe 中的原生运行，支持客户端导航和 React 服务端组件
- 🛡️ **安全隔离** - ChatGPT 采用沙盒域名嵌套 iframe 保护主界面，但导致 Next.js 资源路径解析错误
- 🔧 **资产重定向** - 配置 assetPrefix 和<base>标签强制所有静态资源请求指向实际域名
- 📜 **历史记录修补** - 拦截 history API 调用，仅保留路径参数避免真实域名泄露
- 🔄 **请求重写** - 劫持 fetch 请求将沙盒域名指向应用真实域名，并启用 CORS 模式
- 🌐 **跨域处理** - 通过 Next.js 中间件添加 CORS 头部，正确处理 OPTIONS 预检请求
- 🎯 **DOM 保护** - 使用 MutationObserver 防止父框架修改 HTML 元素导致的 React 水合错误
- 🔗 **外部链接处理** - 通过 openai.openExternal() API 确保外部链接在用户浏览器打开
- ⚡ **开发体验** - 提供 React Hooks 封装 ChatGPT 集成，保持原生 Next.js 开发流程不变
- 📦 **即用模板** - 开源 starter 模板自动处理所有兼容性问题，支持一键部署到 Vercel

---

### [GitHub - rjsf-team/react-jsonschema-form：基于JSON Schema 构建 Web 表单的 React 组件。](https://github.com/rjsf-team/react-jsonschema-form)

**原文标题**: [GitHub - rjsf-team/react-jsonschema-form: A React component for building Web forms from JSON Schema.](https://github.com/rjsf-team/react-jsonschema-form)

这是一个基于 JSON Schema 构建 Web 表单的 React 组件开源项目，具有丰富的主题支持和完整的文档生态。

- 🚀 项目已获得 15.4k 星标和 2.3k 分支，显示其受欢迎程度
- ⚛️ 基于 React 框架，使用 TypeScript 和 JavaScript 开发
- 📝 通过 JSON Schema 声明式构建和自定义 Web 表单
- 🎨 支持多种 UI 主题包括 Ant Design、Material UI、Bootstrap 等
- 📚 提供完整文档、在线演示和贡献指南
- 🔧 包含问题跟踪、拉取请求和讨论等协作功能
- 📄 采用 Apache-2.0 开源许可证
- 🌐 托管在 GitHub Pages 上的实时演示环境
- 🤝 拥有活跃的社区贡献者群体（386 位贡献者）

---

### [react-jsonschema-form 演示平台](https://rjsf-team.github.io/react-jsonschema-form/)

**原文标题**: [react-jsonschema-form playground](https://rjsf-team.github.io/react-jsonschema-form/)

文章概述了人工智能在现代社会中的广泛应用及其带来的影响。

- 🤖 人工智能技术正迅速渗透到各行各业，提升生产效率
- 💡 机器学习算法通过数据分析为决策提供支持，优化业务流程
- 🌐 自然语言处理技术改善了人机交互体验，使沟通更便捷
- ⚠️ 同时也引发了对就业结构变化和数据隐私保护的关注
- 🔮 未来需要建立完善的法律法规来引导 AI 技术的健康发展

---

### [React 语法高亮演示](https://react-syntax-highlighter.github.io/react-syntax-highlighter/demo/)

**原文标题**: [React Syntax Highlighter Demo](https://react-syntax-highlighter.github.io/react-syntax-highlighter/demo/)

文章概述了人工智能在现代社会中的广泛应用及其带来的影响。

- 🤖 人工智能技术正迅速渗透到各行各业，提升生产效率
- 💡 机器学习算法通过数据分析为决策提供支持，优化业务流程
- 🌐 自然语言处理技术改善了人机交互体验，使沟通更便捷
- ⚠️ 同时也引发了关于数据隐私和就业岗位变化的担忧
- 🔮 未来需要建立完善的法律法规来规范人工智能的发展应用

---

### [GitHub - react-syntax-highlighter/react-syntax-highlighter：基于 prismjs 或 highlightjs AST 的 React 语法高亮组件（使用内联样式）](https://github.com/react-syntax-highlighter/react-syntax-highlighter)

**原文标题**: [GitHub - react-syntax-highlighter/react-syntax-highlighter: syntax highlighting component for react with prismjs or highlightjs ast using inline styles](https://github.com/react-syntax-highlighter/react-syntax-highlighter)

这是一个用于 React 的语法高亮组件，支持 highlight.js 和 Prism.js 两种语法解析引擎，采用内联样式实现代码高亮显示。

- 🚀 支持 highlight.js 和 Prism.js 双引擎语法解析
- 💅 提供 JavaScript 样式和 CSS 样式两种使用方式
- 📦 提供完整版、轻量版和异步版三种构建版本
- 🌈 内置丰富的主题样式和语言支持
- 🔧 支持行号显示、代码换行、自定义渲染等高级功能
- 📱 支持 React Native 版本（react-native-syntax-highlighter）
- 📄 采用 MIT 开源协议，已被 25 万 + 项目使用
- ⭐ GitHub 获得 4.5k 星标，314 个分支

---

### [SlimSelect - 高级 JavaScript 下拉选择框库 | 原生 JS 多选功能](https://slimselectjs.com/)

**原文标题**: [SlimSelect - Advanced JavaScript Select Dropdown Library | Vanilla JS Multi-select](https://slimselectjs.com/)

该网站需要启用 JavaScript 才能正常运行。

- 🚫 无法访问：未启用 JavaScript 时网站功能受限
- ⚙️ 技术要求：必须开启 JavaScript 支持才能继续使用
- 📱 功能依赖：网站核心功能完全依赖 JavaScript 实现

---

### [发布 v3.0.0 · brianvoe/slim-select · GitHub](https://github.com/brianvoe/slim-select/releases/tag/v3.0.0)

**原文标题**: [Release v3.0.0 · brianvoe/slim-select · GitHub](https://github.com/brianvoe/slim-select/releases/tag/v3.0.0)

Slim Select 3.0.0 版本发布，新增 React 组件支持并带来多项重要改进

- ⚛️ 新增官方 React 组件，支持 TypeScript 和完整功能集成
- ♿ 全面增强无障碍支持，添加 ARIA 属性兼容屏幕阅读器
- 🎯 改进动画效果，修复滑动过渡问题
- 🔍 优化搜索功能，修复特殊字符高亮和异步搜索行为
- ⌨️ 增强键盘导航，支持多选操作和焦点管理
- ✅ 添加原生 required 属性支持，完善表单验证
- 🐛 修复 Vue 响应式冲突和 TypeScript 类型问题
- 📱 改进移动端布局，修复占位符溢出和箭头图标显示问题

---

### [GitHub - acro5piano/react-native-big-calendar：适用于 React Native 的类 gcal/outlook 日历组件](https://github.com/acro5piano/react-native-big-calendar)

**原文标题**: [GitHub - acro5piano/react-native-big-calendar: gcal/outlook like calendar component for React Native](https://github.com/acro5piano/react-native-big-calendar)

这是一个用于 React Native 的跨平台日历组件，类似 Google 日历和 Outlook 的界面风格，支持 Web、iOS 和 Android 平台。

- 📱 **跨平台支持** - 基于 React Native 开发，可在 Web、iOS 和 Android 上运行
- 🎯 **类型安全** - 完全使用 TypeScript 编写
- 🎨 **高度可定制** - 支持自定义主题和事件渲染组件
- 📦 **轻量级** - 仅约 9KB 大小，依赖 dayjs 和 calendarize
- 🔧 **丰富功能** - 支持月视图、周视图、日视图等多种显示模式
- ⚡ **性能优化** - 提供事件丰富化逻辑提升渲染性能
- 🌍 **国际化** - 支持多语言本地化
- ♿ **无障碍支持** - 完整的可访问性属性配置
- 📊 **事件管理** - 支持全天事件、多日事件和自定义事件渲染
- 🎭 **主题定制** - 可自定义颜色、字体等主题样式

---

### [@storybook/core - Storybook](https://react-native-big-calendar.vercel.app/?path=/story/showcase-desktop--month-mode)

**原文标题**: [@storybook/core - Storybook](https://react-native-big-calendar.vercel.app/?path=/story/showcase-desktop--month-mode)

文章概述了人工智能在现代社会中的广泛应用及其带来的影响。

- 🤖 人工智能技术正迅速渗透到各行各业，提升生产效率
- 💡 机器学习算法通过数据分析为决策提供支持，优化业务流程
- 🌐 自然语言处理技术改善了人机交互体验，使沟通更便捷
- ⚠️ 同时也引发了对就业结构变化和数据隐私保护的关注
- 🔮 未来需要建立完善的法律法规来引导 AI 技术的健康发展

---

### [GitHub - wcandillon/react-native-webgpu: 基于 Dawn 的 React Native WebGPU 实现](https://github.com/wcandillon/react-native-webgpu)

**原文标题**: [GitHub - wcandillon/react-native-webgpu: React Native implementation of WebGPU using Dawn](https://github.com/wcandillon/react-native-webgpu)

这是一个使用 Dawn 实现 WebGPU 的 React Native 技术预览项目，支持在移动端进行高性能图形渲染。

- 🚀 基于 Dawn 实现的 React Native WebGPU 技术预览版，需要 React Native 0.81+ 版本
- ⭐ GitHub 项目获得 840 星标和 40 个分支，采用 MIT 开源协议
- 🎮 完整支持 Three.js 和 react-three-fiber，提供 WebGPU 构建配置
- 📱 提供 visionOS 和 macOS 预编译二进制文件，支持 iOS 模拟器运行
- 🔧 API 设计与 Web 平台完全对称，包含手动帧呈现和外部纹理处理功能
- 🛠️ 支持本地构建 Dawn 或安装预编译版本，包含完整的开发测试流程
- 📐 画布尺寸和像素密度处理与 Web 平台保持一致的行为规范
- 🐛 iOS 模拟器运行需禁用 Metal 验证 API，提供详细故障排除指南

---

### [黎明 - 谷歌的 Git 实践](https://dawn.googlesource.com/dawn)

**原文标题**: [dawn - Git at Google](https://dawn.googlesource.com/dawn)

Dawn 是一个开源的跨平台 WebGPU 标准实现，提供 C/C++ 头文件、原生 GPU API 支持及客户端 - 服务器架构，主要用于 Chromium 等大型系统集成。

- 🌐 实现 WebGPU 标准，提供 webgpu.h 头文件映射
- 🔧 支持多平台原生 GPU API（D3D12/Metal/Vulkan/OpenGL）
- 🏗️ 包含 Tint 着色器编译器，支持 WGSL 语言转换
- 📚 提供开发者文档、测试指南和调试工具
- 🐛 设有独立问题追踪系统（Dawn/Tint 分开）
- 💬 通过邮件列表和 Matrix 聊天室提供社区支持
- ⚖️ 采用 BSD 3-Clause 开源协议

---

### [GitHub - Clariity/react-chessboard：适用于React应用的现代化响应式棋盘组件。](https://github.com/Clariity/react-chessboard)

**原文标题**: [GitHub - Clariity/react-chessboard: A modern, responsive chessboard component for React applications.](https://github.com/Clariity/react-chessboard)

这是一个用于 React 应用的现代化响应式国际象棋棋盘组件，提供丰富的自定义功能和开发工具。

- ♟️ 项目拥有 473 个星标和 143 个分支，显示其受欢迎程度
- 🎯 支持拖放操作、自定义棋子样式和备用棋子
- 🎨 提供自定义棋盘尺寸、动画效果和事件处理功能
- 📱 具备移动端支持和响应式设计，确保无障碍访问
- 🔷 基于 TypeScript 开发，提供实用的工具函数
- 📦 可通过 npm、yarn 或 pnpm 快速安装使用
- 📚 提供详细文档网站和多种框架集成指南
- 🤝 欢迎社区贡献，设有 Discord 交流服务器
- 📄 采用 MIT 开源协议，由 Ryan Gregory 维护

---

### [首页 | React-Uploady](https://react-uploady.org/)

**原文标题**: [Home | React-Uploady](https://react-uploady.org/)

React-Uploady 是一个简化复杂上传流程的 React 库，提供开箱即用的上传组件与高度可定制性。

- 🚀 **快速上手**：无需编写大量代码即可实现高级文件上传功能
- ⚙️ **灵活配置**：所有功能均可开箱即用，同时支持完全自定义和扩展
- 🧱 **模块化设计**：提供基础组件和钩子，支持按需构建上传流程
- 👍 **用户好评**：开发者称赞其简洁易用、文档完善、设计优雅
- 📦 **核心组件**：包含上传按钮、预览组件、拖放区域和 URL 输入等实用组件
- 💝 **社区支持**：通过 Open Collective 和 GitHub 获得开源社区支持

---

### [Webpack 应用](https://doist.github.io/reactist/?path=/story/reactist--page)

**原文标题**: [Webpack App](https://doist.github.io/reactist/?path=/story/reactist--page)

文章概述了人工智能在现代社会中的多领域应用及其带来的效率提升。

- 🤖 自动化流程优化生产力
- 🏥 医疗诊断辅助提高精准度  
- 🎓 个性化学习适配学生需求
- 🛒 智能推荐系统提升消费体验
- 🔒 数据安全防护强化隐私保护
- 🌐 自然语言处理打破交流障碍
- 📊 大数据分析驱动商业决策

---

### [GitHub - reagent-project/reagent: 一个极简的 ClojureScript 与 React.js 交互接口](https://github.com/reagent-project/reagent)

**原文标题**: [GitHub - reagent-project/reagent: A minimalistic ClojureScript interface to React.js](https://github.com/reagent-project/reagent)

这是一个基于 ClojureScript 的轻量级 React.js 接口库，提供简洁的函数式组件开发方式。

- 🧪 项目采用 MIT 开源协议，拥有 4.8k 星标和 412 个复刻
- ⚡ 通过类似 Hiccup 的标记语法替代 JSX，支持嵌套组件和属性传递
- 🔄 内置响应式原子状态管理，自动触发组件重新渲染
- 🎯 支持 React 19 等渲染器，可与 Shadow-cljs 等构建工具集成
- 📚 提供详细文档、示例项目和社区支持渠道
- 🚀 利用 ClojureScript 特性优化渲染性能，代码体积控制在 79KB 左右
- 🔧 包含 91 位贡献者，项目活跃度较高，持续维护更新

---

### [ESLint v9.39.1 发布 - ESLint - 可插拔 JavaScript 代码检查工具](https://eslint.org/blog/2025/11/eslint-v9.39.1-released/)

**原文标题**: [ESLint v9.39.1 released - ESLint - Pluggable JavaScript Linter](https://eslint.org/blog/2025/11/eslint-v9.39.1-released/)

ESLint v9.39.1 作为补丁版本发布，修复了上一版本中因规则访问器参数传递变更导致的第三方规则兼容性问题，并同步更新了文档与依赖项。

- 🐛 修复了 ESLint v9.39.0 中规则访问器意外传入两个参数导致第三方规则（如 @typescript-eslint/unified-signatures）崩溃的问题  
- 🔧 恢复 JavaScript/TypeScript 语言访问器仅接收单节点参数的原设计  
- 📚 新增关于 extends 与级联配置使用场景的文档说明  
- 📦 同步更新 @eslint/js 等依赖至兼容版本  
- ✅ 完善版本测试与持续集成配置

---

### [Tuple：macOS 和 Windows 上最佳的远程结对编程应用](https://tuple.app?utm_source=cooperpress&utm_medium=referral&utm_campaign=react_status_classified_20251105)

**原文标题**: [Tuple: the best remote pair programming app on macOS and Windows](https://tuple.app?utm_source=cooperpress&utm_medium=referral&utm_campaign=react_status_classified_20251105)

Tuple 是一款专为远程结对编程设计的应用程序，提供高清屏幕共享、流畅音频和远程控制功能，支持 macOS 和 Windows 系统，即将推出 Linux 版本。

- 🐧 即将推出 Linux 版本，现已开放等候名单
- 🖥️ 专为远程结对编程打造，提供超高清（最高 5K）屏幕共享
- 🔒 端到端加密所有数据传输，保障用户隐私安全
- ⚡ 原生 C++ 引擎开发，性能优化，资源占用少
- 🎮 一键切换屏幕共享者，支持无缝远程协作
- ⌨️ 完全可自定义的键盘快捷键，保持工作流程
- 🎨 内置屏幕标注、表情反应和动画特效功能
- 🔌 支持自动化触发器，可对接代码事件
- 💬 获 Shopify、PlanetScale 等企业工程师好评
- 🆓 提供 14 天免费试用，支持随时取消

---

### [STRICH：适用于网页应用的条码扫描工具](https://strich.io/?ref=react-status)

**原文标题**: [STRICH: Barcode Scanning for Web Apps](https://strich.io/?ref=react-status)

STRICH 是一款用于网页应用的 JavaScript 条码扫描库，支持实时 1D/2D 条码识别，无需原生应用或后端支持。

- 📱 支持所有主流浏览器和移动设备，基于 WebAssembly 和 WebGL 技术
- 💰 提供透明定价（基础版 99 美元/月起）和 30 天免费试用
- 🔧 零依赖、易于集成，支持所有主流前端框架
- 🏢 已被多个行业客户采用（图书馆、医疗、零售、物流等）
- 📊 支持多种条码类型（Code128/EAN/QR 码/Data Matrix 等）
- 🌐 具备离线功能、白标定制和企业级安全合规选项
- ⚡ 相比免费方案（ZXing/Quagga）在识别率和性能方面更具优势
- 📦 提供弹出式扫描界面和完整的开发文档

---

### [JavaScript 源码映射的内部机制](https://www.polarsignals.com/blog/posts/2025/11/04/javascript-source-maps-internals)

**原文标题**: [The Inner Workings of JavaScript Source Maps](https://www.polarsignals.com/blog/posts/2025/11/04/javascript-source-maps-internals)

源映射通过 JSON 格式文件将压缩后的 JavaScript 代码位置映射回原始源代码位置，帮助开发者在浏览器中直接调试原始代码。

- 🧩 源映射核心功能是将压缩文件中的符号和位置映射回原始源代码，使开发者能在浏览器中看到带有正确变量名和格式的源码
- 🔄 在 TypeScript 构建流程中，源映射在转译、打包和压缩每个阶段都保持与原始代码的关联
- 📄 源映射文件采用 JSON 格式，包含版本号、生成文件名、源文件路径、原始标识符数组和编码后的映射数据等关键字段
- 🗜️ 映射数据使用 VLQ 编码和 Base64 字符进行高效压缩，通过分号表示行分隔，逗号分隔同一行内的不同段
- 📍 每个映射段包含生成文件列位置、源文件索引、源行号和源列号，可能还包含原始名称索引
- 🔢 VLQ 编码通过符号位、5 位数据分组和 Base64 转换三个步骤，用最少的字节表示位置差异值
- 🚀 源映射技术即将扩展到性能分析工具，为性能剖析工作流带来同样的调试便利

---

### [加强 npm 安全性：认证与令牌管理的重要更新 - GitHub 更新日志](https://github.blog/changelog/2025-09-29-strengthening-npm-security-important-changes-to-authentication-and-token-management/)

**原文标题**: [Strengthening npm security: Important changes to authentication and token management - GitHub Changelog](https://github.blog/changelog/2025-09-29-strengthening-npm-security-important-changes-to-authentication-and-token-management/)

npm 将于 2025 年 9 月至 11 月实施三项安全升级：细化访问令牌有效期缩短至 7-90 天、全面停用传统令牌、逐步淘汰 TOTP 双因素认证。这些措施旨在防范供应链攻击，维护者需及时调整工作流程。

- 🔐 细化令牌有效期缩短：新建写入令牌默认 7 天，最长 90 天（原为无限期）
- 🚫 传统令牌全面停用：五周内撤销所有传统令牌并禁用生成功能
- ⏰ TOTP 认证逐步淘汰：新配置已禁止，现有配置将在数月后废止
- 📅 分阶段实施：10 月初启用新令牌规则，11 月中旬完成传统令牌清理
- 🌟 推荐信任发布模式：支持 GitHub/GitLab CI/CD，实现零令牌自动验证
- 🤝 呼吁社区协作：立即迁移传统令牌，参与社区讨论更新实践
- 📚 支持渠道：官方文档、社区讨论区及 npm 支持团队提供协助

---

### [Node.js — Node.js v24.11.0（长期支持版）](https://nodejs.org/en/blog/release/v24.11.0)

**原文标题**: [Node.js — Node.js v24.11.0 (LTS)](https://nodejs.org/en/blog/release/v24.11.0)

Node.js 24.11.0 版本正式进入长期支持阶段，代号为"氪星"，将持续提供更新至 2028 年 4 月，此版本主要更新了 LTS 元数据，并修复了已知的 Buffer 内存分配问题。

- 🚀 Node.js 24.11.0 版本正式进入长期支持阶段，代号"氪星"
- 📅 LTS 支持周期将持续至 2028 年 4 月底
- 🔄 本次更新主要调整了版本元数据，无功能性变更
- ⚠️ 存在已知问题：Buffer.allocUnsafe 意外返回清零缓冲区
- 🔧 计划在后续版本恢复 Buffer.allocUnsafe 的原始行为
- 🌐 提供 Windows、macOS、Linux 等多平台安装包和二进制文件
- 📚 完整文档和源代码已同步发布

---

### [Node.js — Node.js v22 至 v24 版本](https://nodejs.org/en/blog/migrations/v22-to-v24)

**原文标题**: [Node.js — Node.js v22 to v24](https://nodejs.org/en/blog/migrations/v22-to-v24)

本文介绍了从 Node.js v22 迁移至 v24 的部分内容，包括平台支持变更、破坏性变化、构建要求更新以及可用的自动化代码迁移工具。

- 🚀 Node.js 24.11.0 已进入长期支持阶段，支持将持续至 2028 年 4 月
- 🖥️ 平台支持变更：停止提供 32 位 Windows 和 Linux armv7 预构建版本，macOS 最低要求 13.5
- 🔐 OpenSSL 3.5 安全升级：默认安全级别提升至 2，禁止使用弱密钥和 RC4 密码套件
- ⚡ 行为变更：强化 fetch() 合规性、AbortSignal 验证、流错误处理等核心模块改进
- 🔧 构建要求更新：Linux 需 gcc 12.2+，macOS 需 Xcode 16.1+
- 🔄 提供 6 个代码迁移工具：涵盖 fs 常量、util.log 替换、zlib 属性重命名等常见兼容性问题
- 📦 建议优先使用 NODE-API 开发 C++ 插件以减少重建需求
- ⚠️ 用户需测试弱密钥依赖场景，确保兼容新安全标准

---

### [错误](https://react.statuscode.com/link/176606/web)

**原文标题**: [Error](https://react.statuscode.com/link/176606/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='react.statuscode.com', port=443): Max retries exceeded with url: /link/176606/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1000)')))

---

### [错误](https://react.statuscode.com/link/176607/web)

**原文标题**: [Error](https://react.statuscode.com/link/176607/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='react.statuscode.com', port=443): Max retries exceeded with url: /link/176607/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1000)')))

---

### [错误](https://react.statuscode.com/link/176608/web)

**原文标题**: [Error](https://react.statuscode.com/link/176608/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='react.statuscode.com', port=443): Max retries exceeded with url: /link/176608/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1000)')))

---

