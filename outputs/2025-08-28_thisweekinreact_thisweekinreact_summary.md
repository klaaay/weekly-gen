### [Nx 及部分支持插件的恶意版本已发布 · 咨询通告 · nrwl/nx · GitHub](https://github.com/nrwl/nx/security/advisories/GHSA-cxm3-wv7p-598c)

**原文标题**: [Malicious versions of Nx and some supporting plugins were published · Advisory · nrwl/nx · GitHub](https://github.com/nrwl/nx/security/advisories/GHSA-cxm3-wv7p-598c)

Nx 及相关插件包在 npm 上发布了恶意版本，涉及多个包和版本，这些版本会窃取用户凭证并修改系统文件。恶意包已被 npm 删除，团队已采取多项措施修复和预防。

- 🚨 **恶意版本发布**：多个 Nx 包（如 nx、@nx/devkit 等）的特定版本被植入恶意代码，用于扫描文件系统并窃取凭证。
- 📁 **凭证泄露**：恶意代码将收集的凭证信息上传至 GitHub 仓库，仓库名包含 "s1ngularity-repository"。
- ⚠️ **系统修改**：恶意脚本修改用户的 .zshrc 和 .bashrc 文件，添加关机命令，可能导致系统立即关闭。
- 🔄 **触发方式**：不仅通过手动安装触发，还通过 Nx Console 编辑器扩展自动安装最新版本时触发。
- ⏰ **时间线**：漏洞于 8 月 21 日引入，8 月 24 日被利用，恶意包于 8 月 26 日发布，当晚被移除。
- 🔧 **修复措施**：团队撤销了所有受影响版本，强制启用 2FA，使用 Trusted Publishers 机制，并旋转了所有令牌。
- 📋 **用户行动**：检查是否受影响，更新到安全版本，旋转所有凭证，并检查系统配置文件。

---

### [@sebastienlorber.com 在 Bluesky](https://bsky.app/profile/sebastienlorber.com/post/3lxfjznoq522k)

**原文标题**: [@sebastienlorber.com on Bluesky](https://bsky.app/profile/sebastienlorber.com/post/3lxfjznoq522k)

这是一个关于 React 和 React Native 每周动态的技术资讯摘要，主要分享最新工具、库和更新。

- 🚀 本期重点推荐 nuqs 状态管理库和 Concurrent React 并发特性
- 🔧 开发工具更新包括 shadcn CLI、Apollo、Waku 和 React-Aria 组件库
- 📱 React Native 领域关注 Expo 发布、Maestro 测试工具和 SPM 包管理
- 📅 资讯发布时间为 2025 年 8 月 27 日
- 🌐 需要 JavaScript 支持交互式网页应用
- 📖 完整内容可通过 thisweekinreact.com 订阅获取

---

### [未找到标题](https://x.com/sebastienlorber/status/1960754224087601240)

**原文标题**: [No title found](https://x.com/sebastienlorber/status/1960754224087601240)

浏览器检测到 JavaScript 被禁用，无法正常使用 X 平台
- 🚫 JavaScript 未启用导致功能受限
- 🌐 需启用 JavaScript 或更换支持浏览器
- 📖 支持浏览器列表可查看帮助中心
- 🔧 隐私扩展可能导致异常需暂时禁用
- 🔄 建议尝试重新加载页面恢复功能

---

### [LinkedIn 登录，登入 | LinkedIn](https://www.linkedin.com/uas/login?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fin%2Fsebastienlorber%2Frecent-activity%2Fall%2F)

**原文标题**: [
            
          LinkedIn Login, Sign in | LinkedIn
      
        ](https://www.linkedin.com/uas/login?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fin%2Fsebastienlorber%2Frecent-activity%2Fall%2F)

概述 LinkedIn 登录页面的功能和选项，包括多种登录方式、密码管理、一次性链接登录及新用户注册流程。  
- 🔐 支持多种登录方式：Apple 账号、通行密钥或邮箱/手机号  
- 👀 提供密码显示选项及忘记密码功能  
- 📧 可通过一次性邮件链接快速登录，建议检查垃圾邮件  
- 🔄 支持重新发送验证邮件  
- 👥 包含新用户注册入口及服务条款同意选项

---

### [Reddit——互联网之心](https://www.reddit.com/user/sebastienlorber/submitted/?rdt=36715)

**原文标题**: [Reddit - The heart of the internet](https://www.reddit.com/user/sebastienlorber/submitted/?rdt=36715)

本周 React Native 社区发布了第 246 期周报，重点介绍了多项框架更新和工具发布，涵盖性能优化、新特性以及生态系统动态。

- 📱 FlashList 2 发布，带来更高效的列表渲染性能
- 🔄 React Native 0.81 版本更新，包含重要功能改进
- 🛠️ Expo 开发平台推出新工具和服务支持
- ⚡ Radon 库新增，专注于状态管理优化
- 👆 Gesture Handler 手势库升级交互体验
- 🔊 Audio 音频组件增强多媒体处理能力
- 🎨 Skia 图形引擎集成提升渲染性能
- 🚀 Nitro 编译器优化应用启动速度
- 🌐 Strict DOM 模式强化类型检查规范

---

### [未找到标题](https://x.com/jherr/status/1666578571912171520)

**原文标题**: [No title found](https://x.com/jherr/status/1666578571912171520)

JavaScript 功能未启用，检测到当前浏览器禁用了 JavaScript。请启用 JavaScript 或切换至支持的浏览器以继续使用 x.com，支持浏览器列表可在帮助中心查看。遇到问题无需担心，可尝试重新操作或暂时禁用隐私相关扩展。

- 🌐 浏览器 JavaScript 功能已禁用
- 🔄 建议启用 JavaScript 或更换支持浏览器
- 📖 支持浏览器列表详见帮助中心
- ⚠️ 隐私扩展插件可能导致访问异常
- 🔧 可尝试禁用扩展后重新加载页面

---

### [未找到标题](https://x.com/jherr)

**原文标题**: [No title found](https://x.com/jherr)

JavaScript 功能未启用，导致无法正常使用 x.com 平台。

- 🌐 浏览器已禁用 JavaScript 功能
- 🔧 建议启用 JavaScript 或更换支持浏览器
- 📖 支持浏览器列表可查看帮助中心
- 🛡️ 隐私扩展插件可能造成访问异常
- 🔄 页面提供"重试"功能进行再次尝试
- ©️ 页面底部包含版权信息和政策链接

---

### [JavaScript 图表 | AG Charts](https://www.ag-grid.com/charts/?utm_source=thisweekinreact&utm_medium=newsletter&utm_campaign=2025-email-4)

**原文标题**: [JavaScript Charts | AG Charts](https://www.ag-grid.com/charts/?utm_source=thisweekinreact&utm_medium=newsletter&utm_campaign=2025-email-4)

AG Charts 是一款专业级 JavaScript 图表库，提供丰富的图表类型和高度定制化功能，专为企业级应用设计。

- 📊 支持超过 25 种图表类型，包括柱状图、折线图、饼图、金融蜡烛图、桑基图等
- 🌍 提供地图图表功能，支持地理区域可视化、路线标记和点位数据展示  
- ⚡ 具备实时数据更新能力，支持大规模数据集的高性能渲染
- 🔧 提供 React/Vue/Angular 等框架的官方集成套件
- 💼 与 AG Grid 数据表格深度集成，被 90% 财富 500 强企业使用
- 🎨 支持高度自定义样式，包含响应式设计和无障碍访问功能
- 📅 保持频繁更新，最新版本 12.1.0 提供轴标签截断、交替带阴影等新特性
- 💡 内置图表导出功能，支持 PNG 格式输出

---

### [AG Grid：一款快速、强大且灵活的 React 数据表格](https://www.ag-grid.com/react-table/?utm_source=thisweekinreact&utm_medium=newsletter&utm_campaign=2025-email-4)

**原文标题**: [AG Grid: A Fast, Powerful, and Flexible React Data Table](https://www.ag-grid.com/react-table/?utm_source=thisweekinreact&utm_medium=newsletter&utm_campaign=2025-email-4)

AG Grid 是一个高性能、功能丰富的 React 表格库，提供免费社区版和付费企业版，广泛应用于多个行业。

- 🚀 快速集成：通过 npm 安装，仅需少量代码即可创建功能完整的 React 表格
- 💪 高性能处理：支持数百万行数据，提供客户端和服务器端行模型
- 🎛️ 功能丰富：内置排序、过滤、编辑、导出等 100+ 功能
- 🏢 企业级应用：被 90% 财富 500 强企业使用，每周超 100 万次下载
- 🌐 多行业案例：广泛应用于金融（摩根大通）、AI（微软）、航空航天（NASA）等领域
- 🎨 高度可定制：支持主题定制和组件自定义，提供主题构建工具
- 💰 灵活授权：社区版免费，企业版提供高级功能和技术支持
- 📊 图表集成：完美兼容 AG Charts，实现数据可视化
- 🔧 开发友好：提供详细文档、示例和教程，支持快速上手

---

### [nuqs 2.5 | nuqs](https://nuqs.47ng.com/blog/nuqs-2.5)

**原文标题**: [nuqs 2.5 | nuqs](https://nuqs.47ng.com/blog/nuqs-2.5)

nuqs 2.5 版本发布，引入防抖、标准模式、键隔离等新功能，支持 TanStack Router，提供全局默认选项，并优化了包大小和性能。

- ⏱️ 防抖功能：限制高频率输入（如搜索框）的网络请求，仅在用户停止输入后发送
- 📋 标准模式：支持外部工具（如 tRPC）进行验证和类型推断
- ⚡ 键隔离：组件仅在相关 URL 参数变化时重新渲染，提升性能
- 🏝️ TanStack Router 支持：实验性兼容，提供类型安全路由
- 🌍 全局默认选项：可在适配器级别统一配置 shallow、scroll 等选项
- 📦 零依赖：库无运行时依赖，压缩后体积小于 5.5kB
- 🔧 Next.js 15.5 实验性支持：提供类型安全路由工具函数
- 🙌 社区贡献：感谢众多贡献者和赞助商的支持

---

### [全栈 Next.js 15 课程 - Next 之路](https://www.road-to-next.com/?utm_source=newsletter&utm_medium=email&utm_campaign=this_week_in_react_2.2)

**原文标题**: [Full-Stack Next.js 15 Course - The Road to Next](https://www.road-to-next.com/?utm_source=newsletter&utm_medium=email&utm_campaign=this_week_in_react_2.2)

这是一门由 Robin Wieruch 推出的 Next.js 全栈开发视频课程，包含开发者旅程和软件工程师旅程两个阶段，使用现代技术栈帮助学员从初级进阶到高级开发水平。

- 🎓 课程提供两个阶段：开发者旅程（$249）和软件工程师旅程（$349），包含视频课程、实战项目和社区支持
- ⚡ 技术栈涵盖 Next.js 15、React 19、Prisma、Supabase、TypeScript 等现代工具链
- 🛠️ 通过构建 SaaS 项目实战，学习服务端组件、数据库操作、身份验证、支付集成等全栈技能
- 👨‍🏫 讲师 Robin 拥有十年开发经验，曾与 MakerDAO、TRUMPF 等知名机构合作
- 🌍 适合前端转全栈、不同语言转型、自由职业者和技术创业者等不同背景学员
- 📝 提供 14 天退款保证、终身访问权限和完成证书
- 💬 配备 Discord 社区支持和英文字幕
- 🎯 学员反馈高度认可课程在项目架构、认证原理和技术深度方面的教学价值

---

### [RFC：通过上下文选择器（作者：gnoff）· Pull Request #119 · reactjs/rfcs · GitHub](https://github.com/reactjs/rfcs/pull/119#issuecomment-3214859601)

**原文标题**: [RFC: Context selectors by gnoff · Pull Request #119 · reactjs/rfcs · GitHub](https://github.com/reactjs/rfcs/pull/119#issuecomment-3214859601)

React RFC #119 提出了一个新的 `useContextSelector` API，用于从 Context 值中选择特定部分，以避免不必要的组件更新，从而提升性能并简化代码。

- 🎯 **动机**：解决并发 React 下的外部状态订阅问题，减少用户代码复杂性，提升应用性能，并提供比 `observedBits` 更优化的方案。
- ⚙️ **工作原理**：通过选择器函数从 Context 值中提取特定部分，仅当选择结果变化时才触发组件更新。
- 🔗 **依赖改进**：需要惰性的 Context 传播机制（见相关 RFC）来支持此 API。
- 📦 **示例与实现**：提供了代码示例和实现链接，展示其用法和效果。
- 💬 **社区反馈**：获得了大量积极反应（470 个赞），同时也有关于 API 设计和替代方案的讨论。
- 🔄 **后续发展**：React 团队转向通过编译器优化（如自动记忆化）来解决类似问题，并探索更高效的数据模型和存储方案。

---

### [[react] 由 eps1lon 添加 Fragment Refs · Pull Request #72348 · DefinitelyTyped/DefinitelyTyped · GitHub](https://github.com/DefinitelyTyped/DefinitelyTyped/pull/72348/files)

**原文标题**: [[react] Add Fragment Refs by eps1lon · Pull Request #72348 · DefinitelyTyped/DefinitelyTyped · GitHub](https://github.com/DefinitelyTyped/DefinitelyTyped/pull/72348/files)

GitHub 上的 DefinitelyTyped 项目合并了一个为 React Fragment 添加 ref 支持的功能，涉及多个 TypeScript 定义文件和测试用例的更新。

- 🚀 合并了#72348 拉取请求，为 React Fragment 组件新增了 ref 属性支持
- 🔧 在 react 和 react-dom 的类型定义文件中添加了 FragmentInstance 接口和 FragmentProps 类型
- 🧪 新增了详细的测试用例验证 Fragment ref 的各种用法（focus、observe、event 监听等）
- 📁 修改了 8 个文件，包括类型定义文件 (.d.ts) 和测试文件 (.tsx)
- ⚡ 特别为 TypeScript 5.0 版本提供了相应的类型更新
- 🔍 实现了 DOM 相关的功能方法（blur、focus、getClientRects 等）
- 👥 由贡献者 eps1lon 于 2025 年 4 月 2 日完成合并

---

### [[DevTools] 在组件树视图中显示 Suspense / Activity 的 name 属性 by sebmarkbage · Pull Request #34135 · facebook/react · GitHub](https://github.com/facebook/react/pull/34135)

**原文标题**: [[DevTools] Show name prop of Suspense / Activity in the Components Tree view by sebmarkbage · Pull Request #34135 · facebook/react · GitHub](https://github.com/facebook/react/pull/34135)

React 开发工具中新增了在组件树视图中显示 Suspense 和 Activity 组件的 name 属性功能，以帮助开发者更快速识别边界，同时支持对 key 和 name 属性进行搜索。

- 🚀 开发工具现在会在组件树视图中显示 Suspense 和 Activity 的 name 属性，帮助快速识别边界
- 🔍 新增对 key 和 name 属性的搜索功能，提升调试效率
- ⚙️ 该功能主要针对内置组件，因为自定义组件已有组件名作为标识
- ✅ 该拉取请求已通过代码审查，并于 2025 年 8 月 11 日合并到主分支
- 📊 更新未对生产包大小产生显著影响，各项性能指标保持稳定

---

### [lubieowoce 在 vercel/next.js 的 Pull Request #82905 中初步实现 `export const prefetch` · GitHub](https://github.com/vercel/next.js/pull/82905)

**原文标题**: [initial implementation of `export const prefetch` by lubieowoce · Pull Request #82905 · vercel/next.js · GitHub](https://github.com/vercel/next.js/pull/82905)

Next.js 项目在 GitHub 上关于 `export const prefetch` 功能的初始实现讨论和代码合并过程。

- 🚀 开发者 lubieowoce 在 canary 分支提交了关于 segment 级别 prefetch 配置的初始实现
- 🔧 代码变更涉及 429 行新增和 4 行删除，共修改 161 个文件
- ⚠️ 初始提交时出现测试失败，主要与 RSC 响应格式验证相关
- 📊 性能测试显示构建体积有小幅增加（node_modules 增加 41kB）
- 🔍 团队成员 ijjk 和 acdlite 参与了代码审查
- ✅ 最终通过了所有测试并成功合并到 canary 分支
- 🔄 后续有相关功能跟进实现 runtime prefetch 的优化

---

### [React DOM 组件 – React](https://react.dev/reference/react-dom/components#custom-html-elements)

**原文标题**: [React DOM Components – React](https://react.dev/reference/react-dom/components#custom-html-elements)

React 支持所有浏览器内置的 HTML 和 SVG 组件，包括常见组件、表单组件、资源与元数据组件等，并支持自定义 HTML 元素和事件处理。

- 🌐 React 支持所有内置浏览器 HTML 和 SVG 组件
- 📝 常见组件（如 div）支持 React 特定属性如 ref 和 dangerouslySetInnerHTML
- 🎛️ 表单组件（如 input、select、textarea）可通过 value 属性变为受控组件
- 📚 资源与元数据组件（如 link、meta、script）可渲染到文档头部并支持资源加载行为
- 🔧 自定义 HTML 元素支持属性（字符串值）和属性（任意 JavaScript 值）两种数据传递方式
- 🔊 自定义元素事件监听需使用 on 前缀（如 onspeak），注意事件名称大小写和短横线
- 📏 React 使用驼峰命名规范（如 tabIndex），SVG 命名空间属性需去除冒号（如 xlinkHref）

---

### [未找到标题](https://x.com/mjackson/status/1955083457144762729)

**原文标题**: [No title found](https://x.com/mjackson/status/1955083457144762729)

JavaScript 功能未启用，导致无法正常使用 x.com 平台。

- 🚫 浏览器已禁用 JavaScript 功能
- 🌐 需启用 JavaScript 或更换受支持浏览器
- 📖 支持浏览器列表可查看帮助中心
- 🔧 隐私扩展插件可能导致访问异常
- 🔄 建议尝试禁用插件后重新加载页面
- ℹ️ 页脚包含服务条款/隐私政策等法律信息

---

### [React 美国峰会——美国最大的 React 技术大会](https://reactsummit.us/?utm_source=Newsletter&utm_medium=ThisWeekinReact)

**原文标题**: [React Summit US – The Biggest React Conference in the US](https://reactsummit.us/?utm_source=Newsletter&utm_medium=ThisWeekinReact)

美国最大的 React 会议 React Summit 将于 2025 年 11 月 18 日和 21 日在纽约举行，采用线上线下混合模式，汇聚全球顶尖开发者和行业专家，聚焦 React 技术前沿与创新实践。

- 🗽 会议于 2025 年 11 月 18-21 日在纽约自由科学中心举行，毗邻自由女神像，拥有西半球最大天文馆
- 🌐 采用混合形式，首日线下活动含曼哈顿景观渡轮和全美最大 React 派对，次日及工作坊全程线上直播
- 🧠 深度专题涵盖 AI 工程（生成式 UI、AI 辅助编程）、职业成长（技术领导力提升）和全栈开发
- 👥 50+ 位行业领袖演讲，包括 Next.js、TypeScript、Remix、OpenAI 等核心团队成员
- 🛠️ 免费/付费工作坊覆盖 React Server Components、AI 工程、光标原型开发等实践内容
- 💻 提供多种票务选择：线下单场 990 美元起，线上通票 19 美元/月含多会议权限
- 🎁 特色体验：天文馆演讲、曼哈顿观景渡轮、开发者派对及数字/实体礼品包
- 🌍 预计吸引 1 万 + 全球开发者，800 人现场参会，支持远程互动网络和技术讨论室

---

### [搜索](https://jordaneldredge.com/notes/react-rebasing/)

**原文标题**: [Search](https://jordaneldredge.com/notes/react-rebasing/)

React 的 useTransition 和状态更新重排序机制允许在并发更新被同步更新中断时临时显示非时序中间值，但最终会稳定按正确时序渲染。

- ⚡ 并发特性下过渡更新允许延迟渲染至无 suspense 时才显示
- ⏱️ 同步更新会中断进行中的过渡更新并立即显示新值
- 🔄 React 19 会双重应用更新：先同步显示中断值，再重新计算最终值
- 📊 示例：计数器从 2 开始 → 过渡 +1(未完成) → 同步×2 → 先显示 4 → 最终显示 6
- ⚠️ 状态更新函数必须保持纯函数特性以确保计算准确性
- 💡 最佳实践：避免对同一状态混用同步/过渡更新优先级
- 🎯 核心原则：React 最终会按事件时序稳定渲染正确结果

---

### [React 社区反思 | 李·罗宾逊](https://leerob.com/reflections)

**原文标题**: [Reflections on the React community | Lee Robinson](https://leerob.com/reflections)

作者回顾了十年 React 使用及五年 Next.js 社区管理经历，表达了对 React 生态的深厚感情与思考

- 🎯 React 已成为稳定且广泛采用的"无聊技术"，其组合模型和向后兼容性持续推动生态繁荣
- 🤝 社区管理充满挑战，React 团队面临反馈过载与沟通压力，需平衡开源贡献与个人精力
- 💼 商业与非商业开源项目存在根本差异：Meta 无偿提供 React 而周边框架需寻求商业模式
- 🔄 React 服务端组件 (RSC) 的发展依赖 Vercel 等商业力量投入，但跨框架推广曾面临技术壁垒
- 🌱 2025 年 RSC 趋于稳定，Vite 等工具开始支持，但生态建设仍需时间
- 🧠 呼吁社区保持善意：开源是礼物而非义务，开发者应以建设性态度参与生态演进

---

### [不响的时钟 | Ethan Niser | 博客](https://ethanniser.dev/blog/a-clock-that-doesnt-snap/)

**原文标题**: [A Clock That Doesn't Snap | Ethan Niser | Blog](https://ethanniser.dev/blog/a-clock-that-doesnt-snap/)

本文讨论了静态预渲染页面中因客户端数据不同步导致的 UI 闪烁问题，并提出了通过内联脚本在浏览器解析阶段即时修正状态的解决方案。

- ⚡ 静态预渲染页面因缺乏实时数据导致 UI 显示空白或过期内容
- 🚀 服务端渲染 (SSR) 无法完全解决客户端专属数据 (如 localStorage) 的同步问题
- 🛠️ 通过在 HTML 中插入内联脚本，可在浏览器解析时立即修正元素状态
- ⚠️ 需保持 React 组件与内联脚本中的状态计算逻辑完全一致
- 🔧 可通过 window 全局变量传递初始状态避免 React 水合警告
- 📝 演示了时钟组件和输入框组件的具体实现方案
- 🤔 指出该模式存在代码重复和框架支持不足的局限性

---

### [获取失败](https://spin.atomicobject.com/toast-notifications-tanstack-query/)

**原文标题**: [Failed to retrieve](https://spin.atomicobject.com/toast-notifications-tanstack-query/)

无法总结：获取内容失败，状态码 403。

---

### [React Router 中的 React 服务器组件——初体验 - Raphaël Bronsveld](https://raphaelbronsveld.com/blog/rsc-in-rr-first-impressions)

**原文标题**: [React Server Components in React Router â First Impressions - RaphaÃ«l Bronsveld](https://raphaelbronsveld.com/blog/rsc-in-rr-first-impressions)

React Router 现已实验性支持 React Server Components，作者尝试将博客部分迁移至 RSC，本地设置相对顺利并快速实现运行。尽管一切仍不稳定，但 RSC 提供了服务器端渲染、减少客户端包大小和直接后端集成等优势，适合静态内容如博客。性能测试显示 RSC 路由处理请求更多，但需注意潜在性能问题如导航阻塞和 n+1 查询。

- 🚀 React Router 实验性支持 React Server Components（RSC），允许服务器端渲染组件
- 🌐 RSC 仅服务器渲染，减少客户端 JS 包大小，支持使用重型依赖如数据库客户端
- ⚡ 降低延迟，优化内容加载时间，提升用户体验
- 🔒 直接在组件中使用后端资源，无需暴露给客户端，增强后端集成
- 🛠️ 迁移需更新 Vite 配置、添加新入口点，本地运行相对顺畅
- ⚠️ 当前 API 不稳定，可能存在性能问题如导航阻塞和 n+1 查询
- 📊 性能测试显示 RSC 路由处理请求能力更强，但需谨慎实施
- 💡 适合静态内容（如博客），建议冒险尝试但预期可能出错

---

### [React 并发特性概述 - Certificates.dev 博客](https://certificates.dev/blog/react-concurrent-features-an-overview?friend=TWIR)

**原文标题**: [React Concurrent Features: An Overview - Certificates.dev Blog](https://certificates.dev/blog/react-concurrent-features-an-overview?friend=TWIR)

React 并发特性概述：useTransition、useDeferredValue、Suspense 和 useOptimistic 等核心功能协同工作，通过可中断渲染机制优先处理用户交互，实现流畅的用户体验。

- ⚡ useTransition 标记非紧急状态更新，配合 isPending 状态管理异步操作和渲染优化
- 📦 Suspense 提供声明式加载边界，支持代码分割和异步数据源的优雅处理
- ⏳ useDeferredValue 延迟频繁变化值的渲染，保持界面响应性
- 🚀 useOptimistic 实现乐观更新，在后台操作时提供即时 UI 反馈
- 🔄 这些特性可组合使用，如过渡与 Suspense 结合避免加载闪烁，延迟值与 Suspense 配合优化搜索体验
- 💡 建议根据具体场景选择合适特性，并随着应用复杂度增加逐步组合使用

---

### [使用 React 解锁 Web Workers：一步步指南 | Rahul 的博客](https://www.rahuljuliato.com/posts/react-workers)

**原文标题**: [Unlocking Web Workers with React: A Step-by-Step Guide | Rahul's Blog](https://www.rahuljuliato.com/posts/react-workers)

本文介绍了如何在 React 中使用 Web Workers 来提升应用性能，通过分步指南展示了从解决 UI 冻结问题到实现多任务管理和跨标签共享的全过程。

- 🚀 使用 Web Workers 将计算密集型任务（如斐波那契数列计算）移至后台线程，避免阻塞主线程导致 UI 冻结
- 🔄 通过队列机制控制任务执行顺序，确保多请求场景下的处理有序性
- 🌐 利用 Shared Workers 实现跨浏览器标签的状态共享和缓存功能，提升多标签应用体验
- 📊 对比三种 Worker 类型：Web Worker 适用于单页计算卸载，Shared Worker 用于跨标签协调，Service Worker 专注网络代理和 PWA 功能
- ⚠️ 强调 Worker 无法直接操作 DOM，需通过消息机制与主线程通信，推荐使用 Comlink 等库简化调用
- 💡 提供完整 GitHub 代码示例，包含从基础实现到高级功能的渐进式演示

---

### [如何使用 React 19 和 Strapi 5 构建现代化博客](https://strapi.io/blog/how-to-build-a-modern-blog-with-react-19-and-strapi-5?utm_campaign=19282052-Newsletter%20Sponsorships&utm_source=React&utm_medium=2nd%20sponsor&utm_term=tutorial)

**原文标题**: [How to Build a Modern Blog with React 19 and Strapi 5](https://strapi.io/blog/how-to-build-a-modern-blog-with-react-19-and-strapi-5?utm_campaign=19282052-Newsletter%20Sponsorships&utm_source=React&utm_medium=2nd%20sponsor&utm_term=tutorial)

本文介绍了一个使用 React 19 和 Strapi 5 构建现代博客的全栈项目，包含动态内容管理和 SEO 优化功能。

- 🚀 项目采用 React 19+React Router 7 前端和 Strapi 5 无头 CMS 的全栈技术组合
- 🎨 前端使用 Shadcn/ui 和 Tailwind CSS 实现响应式设计
- 🔄 支持动态内容块管理，非技术人员可通过后台自由调整页面模块
- 📱 包含首页、文章列表页和文章详情页三种页面类型
- ⚡ 具备服务端渲染、TypeScript 全栈类型支持和 SEO 优化功能
- 🛠️ 项目采用 monorepo 结构，包含 client 前端和 server 后端目录
- 📂 前端采用基于文件的路由系统和模块化组件架构
- 🌐 通过 Strapi SDK 实现类型安全的 API 调用，简化数据获取流程

---

### [发布 @apollo/client@4.0.0 · apollographql/apollo-client · GitHub](https://github.com/apollographql/apollo-client/releases/tag/%40apollo/client%404.0.0)

**原文标题**: [Release @apollo/client@4.0.0 · apollographql/apollo-client · GitHub](https://github.com/apollographql/apollo-client/releases/tag/%40apollo/client%404.0.0)

Apollo Client 4.0 是一个重大版本更新，专注于提供更现代、高效和类型安全的 GraphQL 客户端体验，通过架构改进和 API 优化提升开发者体验、减少包体积并增强框架灵活性。

- 🎯 框架无关核心：React 功能从核心库分离，使 `@apollo/client` 真正框架无关，React 导出移至 `@apollo/client/react`
- 📦 更小包体积：通过可选本地状态管理、现代构建目标和改进的 Tree-Shaking 实现
- 💥 统一错误处理：移除 `ApolloError`，引入特定错误类，支持更清晰的错误处理和调试
- 🔧 增强 TypeScript 支持：类型与 API 共置，更精确的返回类型和更严格的类型安全
- ⚡ 现代 Observable 实现：从 `zen-observable` 迁移到 `RxJS`，提供行业标准实现
- 🚀 新功能：包括 `dataState` 属性、可插拔增量交付（`@defer` 支持）和本地状态管理改进
- ⚛️ React 特定改进：更可预测的 Hooks、新的 SSR API 和 React 编译器支持
- 🔗 链接系统演进：所有链接现在都是类，错误链接更改
- 🛠️ 迁移工具：提供自动化代码修改工具（codemod）帮助从 3.x 迁移到 4.0
- ⚠️ 破坏性变更：包括安装要求（RxJS 作为对等依赖）、ApolloClient 构造函数更改和类型系统更新

---

### [流下](https://streamdown.ai/)

**原文标题**: [Streamdown](https://streamdown.ai/)

Streamdown 是专为 AI 流式传输设计的 react-markdown 替代方案，具备安全渲染、未完成标记解析和内置样式等特性，适用于现代 Web 开发场景。

- 🚀 专为 AI 流式传输设计，支持实时解析未完成的 Markdown 语法（如未闭合的代码块和列表）
- 🎨 内置 Tailwind 样式，自动渲染标题、列表、代码块等元素的排版效果
- 📋 原生支持 GitHub Flavored Markdown（GFM），包含任务列表、表格等扩展功能
- 💻 集成 Shiki 代码高亮引擎，提供可复制的交互式代码块
- ∫ 通过 KaTeX 支持 LaTeX 数学公式渲染
- 📊 支持 Mermaid 图表，可流式传输并提供渲染按钮
- 🔒 内置安全防护机制，可限制图片和链接的来源域名
- ⚙️ 提供灵活配置选项，包括自定义组件、主题插件和白名单设置
- 📦 可作为独立包安装（npm i streamdown），也可通过 AI Elements 集成使用

---

### [和博客](https://waku.gg/blog)

**原文标题**: [Waku blog](https://waku.gg/blog)

Waku 框架版本更新历史概述，重点介绍了从 v0.18 到 v0.26 版本的核心功能演进，包括 React 服务器组件支持、路由系统优化、API 功能扩展以及架构简化等关键改进。

- 🗑️ v0.26 版本移除了过时功能并简化核心架构，为未来更新做准备（2025 年 8 月 25 日）
- 🧩 v0.25 版本引入"切片组件"API，重新设计细粒度组件渲染方案（2025 年 8 月 12 日）
- ⚡ v0.24 版本迁移至@vitejs/plugin-rsc，采用 Vite 官方 RSC 插件和环境 API（2025 年 8 月 5 日）
- 🎯 v0.23 版本扩展细粒度组件渲染模式，增强 Waku 路由器的功能（2025 年 5 月 14 日）
- 🌐 v0.22 版本宣布 API 路由功能，支持为项目添加公共 API 端点（2025 年 4 月 2 日）
- 👥 项目迁移至 GitHub 组织，迈向社区驱动开发模式（2025 年 3 月 16 日）
- 📝 v0.21 版本支持渐进式表单，实现无 JavaScript 运行（2025 年 2 月 20 日）
- 🔒 提供类型安全路由功能，确保路由和导航 API 的类型安全（2024 年 12 月 31 日）
- 🏗️ 引入根元素 API，支持自定义项目的根元素（2024 年 12 月 3 日）
- ⚡ v0.21 版本全面支持 React 19 服务器动作 API（2024 年 8 月 20 日）
- 📖 v0.20 版本引入"页面路由器"，为现代 React 服务器组件时代提供极简 API（2024 年 3 月 26 日）
- 🛠️ v0.19 版本推出 createPages API，支持以编程方式创建布局和页面（2024 年 1 月 16 日）
- 🚀 v0.18 版本首次推出 Waku，作为支持 RSC 功能的极简 React 框架（2023 年 12 月 12 日）

---

### [更新日志 - shadcn/ui](https://ui.shadcn.com/docs/changelog)

**原文标题**: [Changelog - shadcn/ui](https://ui.shadcn.com/docs/changelog)

shadcn CLI 3.0 发布，支持命名空间注册表、私有注册表、搜索功能，并全面优化性能和错误处理。同时，项目持续更新组件、支持多框架、Tailwind v4 及 React 19，提供更强大的开发体验。

- 🚀 CLI 3.0 支持命名空间注册表，可使用 @registry/name 格式安装组件
- 🔒 私有注册表支持认证，保护企业专属组件
- 🔍 新增搜索、查看和列表命令，方便组件发现与管理
- ⚡ 完全重写的注册表引擎，依赖解析速度提升 3 倍
- 🛠️ 改进错误处理，提供更清晰的错误提示和解决方案
- 📦 支持通用注册表项，可分发代码、配置等到任意项目
- 📁 新增本地文件支持，无需远程注册表即可初始化和添加组件
- 🔄 新增迁移命令，支持更新到 radix-ui 包
- 📅 升级日历组件，集成 React DayPicker 最新版本
- 🌐 网站升级至 Next.js 15.3 和 Tailwind v4，使用 new-york 风格组件
- 🤖 正在开发零配置 MCP 支持，增强与 AI 代理的协作
- 🏗️ 支持跨框架路由和 monorepo，提升多项目开发效率
- 🎨 更新注册表模式，支持自定义样式、主题和第三方组件扩展
- 🧩 推出 Blocks 功能，提供现成的布局和页面组件，支持社区贡献
- 📐 新增 Breadcrumb 和 Input OTP 组件，增强导航和输入体验
- 🧪 持续更新组件库，包括 Carousel、Drawer、Pagination 等
- ⚙️ CLI 支持自定义 Tailwind 前缀和配置，适配不同项目结构
- 🎭 提供两种主题风格：default 和 new-york，支持 CSS 变量或实用类
- ⏪ 所有组件添加退出动画，提升交互体验
- 📘 提供详细升级指南和迁移说明，确保平滑过渡

---

### [2025 年 8 月 25 日发布——React Spectrum 版本更新](https://react-spectrum.adobe.com/releases/2025-08-25.html)

**原文标题**: [August 25, 2025 Release â React Spectrum Releases](https://react-spectrum.adobe.com/releases/2025-08-25.html)

2025 年 8 月 25 日发布的新版本带来了多项功能增强和问题修复，包括新增源感知覆盖动画、自动完成功能升级至 RC 阶段，以及为 GridList、Table 和 TagGroup 添加过滤支持等。

- 🎯 新增 Popover 和 Tooltip 的源感知覆盖动画支持，实现从触发元素出现的缩放过渡效果
- 🚀 自动完成（Autocomplete）功能升级至 RC 阶段
- 🔍 为 GridList、Table 和 TagGroup 添加过滤支持（虚拟焦点支持尚待开发）
- 📊 GridList 新增分区支持（alpha 阶段），为 Tree 和 Table 的类似功能奠定基础
- 🛠️ 包含多个组件的问题修复和功能优化，如 Button、ComboBox、DatePicker 等
- 📚 更新了文档和示例代码
- 📦 发布了多个更新包，包括@adobe/react-spectrum@3.44.0 等

---

### [从 Preact 10.x 升级 – Preact 指南 v11](https://preactjs.com/guide/v11/upgrade-guide/)

**原文标题**: [Upgrading from Preact 10.x – Preact Guide v11](https://preactjs.com/guide/v11/upgrade-guide/)

Preact 11.x 是从 Preact 10.x 升级的版本，主要目标是尽量减少破坏性变更，同时提升浏览器兼容性并清理遗留代码。升级过程对大多数用户来说简单快捷，仅需注意少量变更。

- 🚀 升级指南：Preact 11.x 旨在最小化破坏性变更，支持从 10.x 平滑升级，仅需关注少量变更。
- 🌐 浏览器支持：支持 Chrome >= 40、Safari >= 9、Firefox >= 36 和 Edge >= 12，旧版浏览器需使用 polyfills。
- 🔧 TypeScript 要求：最低支持 TypeScript v5.1，以利用 JSX 类型改进。
- 📦 模块分发：ESM 包使用 .mjs 扩展，不再提供 .module.js，CJS 和 UMD 包保持不变。
- 💧 水合改进：Hydration 2.0 支持更灵活的组件设计，允许异步边界返回 0 或多个 DOM 节点。
- ⚖️ Hook 相等性检查：使用 Object.is 进行 Hook 参数相等性检查，支持 NaN 作为状态值或依赖项。
- 🔄 Ref 转发默认启用：Ref 现在默认转发，无需使用 forwardRef，但 preact/compat 中类组件不转发以匹配 React 行为。
- 🎨 样式单位处理：自动 px 后缀功能移至 preact/compat，核心不再添加。
- ⚙️ defaultProps 移至 compat：defaultProps 支持移至 preact/compat，因函数组件和 Hook 使用增多。
- 🗑️ 移除 replaceNode 参数：render() 的第三个参数已移除，推荐使用 preact-root-fragment 包替代。
- ❌ 移除 Component.base：不再提供 Component.base，可通过 this.__v.__e 访问 DOM 节点。
- 🧩 移除 SuspenseList：preact/compat 中移除 SuspenseList，因实现不完整。
- 📘 useRef 需初始值：useRef 类型要求初始值，简化类型推断。
- 🔍 JSX 命名空间简化：JSX 命名空间仅保留 TypeScript 必需类型，其他类型移至 preact 命名空间。

---

### [Next.js 身份验证进阶：优质入门指南 - YouTube](https://www.youtube.com/watch?v=ngzLhaT3IzQ)

**原文标题**: [Better Auth with Next.js: A very good introduction - YouTube](https://www.youtube.com/watch?v=ngzLhaT3IzQ)

这是 YouTube 网站页脚常见链接列表的概述。

- ℹ️ 关于平台的基本信息
- 📰 新闻与媒体相关资源
- ©️ 版权声明与信息
- 📞 用户联系渠道
- 🎬 内容创作者相关资源
- 💼 广告合作与商业推广
- 👨‍💻 开发者工具与资源
- 📑 服务条款与使用协议
- 🔒 隐私保护政策
- ⚖️ 平台政策与安全指南
- 🔧 YouTube 功能运作说明
- 🧪 新功能测试信息
- ®️ 公司版权与年份标识

---

### [我用 TanStack 开发者工具在 10 分钟内让你惊叹不已。- YouTube](https://www.youtube.com/watch?v=wQ-X501kgpg)

**原文标题**: [I blow your mind with TanStack Devtools in under 10 minutes. - YouTube](https://www.youtube.com/watch?v=wQ-X501kgpg)

这是 YouTube 网站页脚常见链接列表的概述。

- ℹ️ 关于平台的基本信息
- 📰 新闻与媒体相关资源
- ©️ 版权声明与政策
- 📞 用户联系渠道
- 🧑‍🎨 内容创作者相关信息
- 💼 广告合作与投放
- 👨‍💻 开发者资源与 API
- 📑 服务条款与使用协议
- 🔒 隐私保护政策
- ⚖️ 平台政策与安全规范
- 🔧 平台功能运作说明
- 🧪 新功能测试信息
- ®️ 公司版权与年份标识

---

### [为什么每个开发者都应避免使用 React - YouTube](https://www.youtube.com/watch?v=wOHqwYtZ_90)

**原文标题**: [Why every dev should avoid React - YouTube](https://www.youtube.com/watch?v=wOHqwYtZ_90)

这是一个关于 YouTube 平台信息与政策的概览页面。

- ℹ️ 关于平台的基本信息
- 📰 新闻与媒体相关资源
- ©️ 版权声明与政策
- 📞 联系与支持渠道
- 🎬 内容创作者相关信息
- 💼 广告与商业合作机会
- 👨‍💻 开发者资源与 API
- 📑 服务条款与使用协议
- 🔒 隐私保护政策
- ⚖️ 平台安全政策与指南
- 🔧 平台运作机制说明
- 🧪 新功能测试信息
- ®️ 版权归属与公司信息（谷歌 2025）

---

### [TanStack Start 上的 AI SDK 第 5 版！ - YouTube](https://www.youtube.com/watch?v=obppWNA4NyI)

**原文标题**: [AI SDK Version 5 on TanStack Start! - YouTube](https://www.youtube.com/watch?v=obppWNA4NyI)

这是 YouTube 网站页脚常见链接列表的摘要概述。

- ℹ️ 关于平台的基本信息和背景
- 📰 新闻稿和媒体相关资源
- ©️ 版权声明与知识产权信息
- 📞 用户联系与客服渠道
- 🎬 内容创作者专属资源与支持
- 💼 广告合作与商业推广机会
- 👨‍💻 开发者工具与 API 资源
- 📑 服务条款与使用协议
- 🔒 隐私政策与数据保护措施
- ⚖️ 平台政策与安全指南
- 🔧 平台运作机制说明
- 🧪 新功能测试与体验计划
- ®️ 2025 年谷歌有限责任公司版权所有

---

### [React 性能优化的错误方式 - YouTube](https://www.youtube.com/watch?v=iFtF2jZX3uA)

**原文标题**: [The Wrong Way to Optimize Performance in React - YouTube](https://www.youtube.com/watch?v=iFtF2jZX3uA)

这是一个关于 YouTube 平台信息与政策的概览页面。

- ℹ️ 关于平台的基本信息
- 📢 新闻与媒体相关资源
- ©️ 版权信息与政策
- 📞 联系与支持方式
- 🎬 内容创作者相关信息
- 💼 广告与商业合作
- 💻 开发者资源与 API
- 📑 服务条款与使用协议
- 🔒 隐私政策与数据保护
- ⚖️ 平台政策与安全指南
- 🔧 平台运作机制说明
- 🧪 新功能测试与更新
- ®️ 版权归属与公司信息（谷歌 2025）

---

### [PodRocket - LogRocket 网络开发播客：现代 React 模式：Aurora Scharff 谈并发渲染与操作](https://podrocket.logrocket.com/modern-react-patterns-concurrent-rendering-actions-aurora-scharff)

**原文标题**: [PodRocket - A web development podcast from LogRocket: Modern React Patterns: Concurrent Rendering & Actions with Aurora Scharff](https://podrocket.logrocket.com/modern-react-patterns-concurrent-rendering-actions-aurora-scharff)

React 18 和 19 带来的现代并发渲染模式与 Actions 应用，由 Aurora Scharff 分享实战经验与技术演进方向。

- ⚡ 并发渲染模式提升异步 UI 响应与性能表现
- 🔄 useTransition 在真实场景中的具体应用案例
- 🚀 useOptimistic 实现即时 UI 反馈优化用户体验
- 🌐 React 服务端组件与 Next.js 的深度集成方案
- 🧩 Aria Kit 和 Redwood SDK 等工具重塑 React 开发生态
- 📊 重点关注异步渲染模式对用户体验的实际改善效果

---

### [PodRocket - LogRocket 网络开发播客：超越 DOM 的 React 探索，与 Erik Rasmussen 一起了解自定义渲染器](https://podrocket.logrocket.com/react-beyond-the-dom-custom-renderers-erik-rasmussen)

**原文标题**: [PodRocket - A web development podcast from LogRocket: React beyond the DOM: exploring custom renderers with Erik Rasmussen](https://podrocket.logrocket.com/react-beyond-the-dom-custom-renderers-erik-rasmussen)

概述 React 在 DOM 之外的扩展应用，探讨自定义渲染器如何赋能跨平台开发。  
- 🌐 讨论 React 在物联网和硬件领域的自定义渲染器应用  
- 🛡️ 介绍基于 iframe 和 JSON 渲染的安全插件架构  
- 🔄 解析平台无关渲染机制和 React 协调器原理  
- ⚙️ 展示 Attio 如何让开发者用 React 构建第三方应用  
- 🚀 探讨 React 在非 DOM 环境下的未来发展潜力

---

### [未找到标题](https://x.com/Baconbrix/status/1622655092657688576)

**原文标题**: [No title found](https://x.com/Baconbrix/status/1622655092657688576)

JavaScript 功能未启用，导致网页无法正常运行。

- 🌐 浏览器已禁用 JavaScript 功能
- 🔧 建议启用 JavaScript 或更换受支持浏览器
- 📖 支持浏览器列表可查看帮助中心
- 🛡️ 隐私扩展插件可能造成访问异常
- 🔄 提示尝试刷新页面或禁用插件后重试
- ©️ 页面底部包含版权声明和政策链接

---

### [未找到标题](https://x.com/Baconbrix)

**原文标题**: [No title found](https://x.com/Baconbrix)

浏览器检测到 JavaScript 被禁用，无法正常使用 X 平台功能

- 🚫 JavaScript 未启用导致功能受限
- 🌐 建议启用 JavaScript 或更换支持浏览器
- 📖 支持浏览器列表可查看帮助中心
- 🔧 隐私扩展可能导致冲突需暂时禁用
- 🔄 页面操作失败时可尝试重新加载

---

### [Wallaby - 编辑器内即时反馈的 AI 就绪测试运行器](https://wallabyjs.com/?referrer=ThisWeekInReactAug25)

**原文标题**: [Wallaby - AI-Ready Test Runner with Instant Feedback in Your Editor](https://wallabyjs.com/?referrer=ThisWeekInReactAug25)

Wallaby.js 是一款实时 JavaScript 和 TypeScript 测试运行工具，可在编码时即时显示测试结果和覆盖率，提供智能调试功能并支持 AI 工具集成，显著提升开发效率和测试体验。  
- 🚀 实时测试反馈：输入代码时立即运行测试，结果和覆盖率实时显示在代码旁  
- 🔍 智能调试工具：支持时间旅行调试、值查看器和实时错误追踪，快速定位问题  
- 🤖 AI 深度集成：通过 MCP 服务器为 AI 工具提供运行时上下文，增强代码理解和问题解决能力  
- ⚡ 极速测试执行：仅运行受代码更改影响的最小测试集，大幅减少等待时间  
- 🛠️ 无绑定设计：作为现有测试框架和 IDE 的插件，无需更改项目结构或依赖特定供应商  
- 📊 交互式洞察：提供测试分析、性能剖析和差异管理，支持深入查看测试执行细节和覆盖率  
- 💬 开发者好评：被众多开发者和公司推荐，显著提升生产力和测试编写体验

---

### [Wallaby - 集成即时反馈的 AI 就绪测试运行器](https://wallabyjs.com/?referrer=ThisWeekInReactAug25)

**原文标题**: [Wallaby - AI-Ready Test Runner with Instant Feedback in Your Editor](https://wallabyjs.com/?referrer=ThisWeekInReactAug25)

Wallaby.js 是一款实时 JavaScript 和 TypeScript 测试运行工具，可在编码时即时显示测试结果和覆盖率，支持主流编辑器和测试框架，并提供高级调试和 AI 集成功能，显著提升开发效率和测试体验。

- 🚀 实时测试反馈：输入代码时立即运行测试，结果和覆盖率实时显示在代码旁
- ⚡ 智能最小化测试：仅运行受代码更改影响的最小测试集，速度极快
- 🐛 高级调试功能：支持时间旅行调试、实时值查看和深度对象检查
- 🤖 AI 集成支持：通过 MCP 服务器为 AI 工具提供实时运行时上下文，辅助代码编写和修复
- 🔓 无锁定设计：作为现有测试框架和 IDE 的插件，无需担心供应商或框架锁定
- 📊 丰富可视化：内置测试分析器、性能分析、差异管理和交互式测试输出视图
- 💰 效率提升：据估算可提高 10.84% 的编码效率，每年节省约 2396 美元
- 🌍 广泛认可：被 10,000+ 公司使用，包括财富 500 强企业，开发者评价极高

---

### [介绍 Expo Launch：通往应用商店的全新方式](https://expo.dev/blog/introducing-expo-launch)

**原文标题**: [Introducing Expo Launch: a new way to get to the app store](https://expo.dev/blog/introducing-expo-launch)

该文本是 Expo 公司网站的页脚导航内容，列出了产品、资源、公司信息及法律条款等主要板块。

- 📱 产品服务（包括 EAS、Expo Go 等核心工具）
- 📚 资源中心（提供文档、博客和技术支持）
- 🏢 公司信息（含定价、招聘和品牌资料）
- ⚖️ 法律条款（隐私政策、服务条款等合规内容）
- 📊 状态提示（显示系统运行正常状态）
- ©️ 版权信息（650 Industries 公司 2025 年版权声明）

---

### [React Universe 大会 - 由 Callstack 驱动](https://www.reactuniverseconf.com/?utm_campaign=10_years_panel&utm_source=TWIR&utm_medium=mail&utm_content=post_22_08_2025#panel)

**原文标题**: [React Universe Conf - Powered by Callstack](https://www.reactuniverseconf.com/?utm_campaign=10_years_panel&utm_source=TWIR&utm_medium=mail&utm_content=post_22_08_2025#panel)

React Universe Conf 2025 是庆祝 React Native 十周年的技术大会，将于 2025 年 9 月 2-4 日在波兰弗罗茨瓦夫举行，聚焦 React 和 React Native 的最新发展、AI 集成及跨平台开发实践，汇聚行业顶尖专家和开发者。

- 🎉 庆祝 React Native 十周年，提供 10% 门票折扣（有效期至 2025 年 8 月 22 日）
- 📅 活动时间：2025 年 9 月 2-4 日（含会前研讨会和核心贡献者峰会）
- 📍 地点：波兰弗罗茨瓦夫
- 👥 规模：600+ 全球开发者、25+ 来自 Meta、Vercel 等顶级科技公司的演讲者
- 🧠 主题：涵盖 React 19、AI SDK、移动微前端、性能优化、跨平台迁移实践等前沿技术
- 🤖 特色内容：AI 集成（如本地 LLM）、React Native 未来十年展望、Node-API 与 Hermes 整合
- 🎤 演讲嘉宾：包括 Meta React Native 核心团队成员、Vercel 高管、SQLite 创建者等行业领袖
- 🛠️ 相关活动：免费 AI 交流会、React Native 十周年庆典派对、工作坊和社交会议
- 🌐 主办方：Callstack，专注于 React 和 React Native 的软件咨询公司
- 💡 目标：推动 React 生态系统创新，促进开发者社区交流和知识分享

---

### [为 iOS 添加对 Swift Package Manager（SPM）作为依赖管理器的支持 · Issue #587 · react-native-community/discussions-and-proposals · GitHub](https://github.com/react-native-community/discussions-and-proposals/issues/587#issuecomment-3200592526)

**原文标题**: [Add support for Swift Package Manager (SPM) as the dependency manager for iOS · Issue #587 · react-native-community/discussions-and-proposals · GitHub](https://github.com/react-native-community/discussions-and-proposals/issues/587#issuecomment-3200592526)

该文章是关于在 React Native 社区中提议弃用 CocoaPods 并支持 Swift Package Manager（SPM）作为 iOS 依赖管理器的讨论。  
- 📱 提议弃用 CocoaPods，并支持 SPM 作为 iOS 依赖管理器  
- 📊 基于 JetBrains 2022 年调查数据，SPM 使用率已达 47%，CocoaPods 为 61%  
- 🔄 28% 的开发者计划在未来 12 个月内用 SPM 替换 CocoaPods  
- 🚀 SPM 于 2016 年随 Swift 3.0 发布，旨在取代 2011 年的 CocoaPods  
- 💡 当前 CocoaPods 是 React Native iOS 集成的唯一选项，可能阻碍开发者尝试

---

### [RFC：将 Jest 从 React Native 核心中分离出来 by kitten · Pull Request #926 · react-native-community/discussions-and-proposals · GitHub](https://github.com/react-native-community/discussions-and-proposals/pull/926)

**原文标题**: [ RFC: Split Jest from React Native Core by kitten · Pull Request #926 · react-native-community/discussions-and-proposals · GitHub](https://github.com/react-native-community/discussions-and-proposals/pull/926)

该提案建议将 Jest 从 React Native 核心中分离，转为独立的包管理，以降低维护负担并鼓励更多测试框架支持 React Native。

- 🚀 提议将`react-native/jest-preset`移至独立的`@react-native/jest-preset`包
- ⚖️ 当前方案可避免继续承担 Jest 预设的维护负担
- 🔄 替代方案包括继续包含 Jest、更换测试框架或创建通用测试接口
- 🌟 分离后能促进其他测试运行器（如 Vitest）对 React Native 的支持
- 📦 采用单次发布策略确保平稳迁移
- 🧪 强调`@testing-library/react-native`已提供框架无关的测试能力
- 🔧 主要复杂点在于打包支持，但新项目正逐步解决该问题

---

### [在 iOS 上实现缺失的 CSS 滤镜 · Issue #927 · react-native-community/discussions-and-proposals · GitHub](https://github.com/react-native-community/discussions-and-proposals/issues/927)

**原文标题**: [Implementing missing CSS filters on iOS · Issue #927 · react-native-community/discussions-and-proposals · GitHub](https://github.com/react-native-community/discussions-and-proposals/issues/927)

这是一个关于在 React Native iOS 平台上实现缺失 CSS 滤镜功能的讨论提案，主要探讨了两种技术方案及其优缺点。

- 🚫 私有 API 方案：使用 CAFilter 实现简单但存在审核风险，仅支持部分滤镜且缺乏官方文档
- ✅ SwiftUI 方案：使用公共 API 更安全且支持多种滤镜，但实现复杂且缺少 sepia/invert/dropShadow 等效果
- 🖼️ 其他方案：CIFilter 仅适用于静态图像，不适用于动态视图
- 💡 当前进展：已有相关 PR 寻求社区反馈，重点关注 SwiftUI 实现方案的改进思路
- 👥 参与人员：邀请@NickGerleman 和@joevilches 等核心贡献者参与技术讨论

---

### [Android 上的 Bridging Trace API • 安德烈·卡拉赞斯](https://andrei-calazans.com/posts/bridging-trace-on-android/)

**原文标题**: [Bridging Trace API on Android • Andrei Calazans](https://andrei-calazans.com/posts/bridging-trace-on-android/)

本文介绍了如何在 React Native 应用中通过桥接 Android 的 Trace API 来实现性能追踪功能，并详细说明了原生模块的创建和集成方法。

- 📱 Android Trace API 可用于测量代码执行时间，在 Perfetto 中可视化性能数据
- ⚡ 主要应用场景包括测量 UI 性能、跟踪启动阶段代码执行、调试卡顿问题
- 🔧 React Native 默认未桥接 Trace API，需要自行实现原生模块
- 📝 创建 TracingModule 类封装 beginSection 和 endSection 方法
- 📦 配置 TracingPackage 并将包添加到 MainApplication 中
- 🖥️ 在 JS/TS 代码中通过 Platform.OS 判断调用原生追踪方法
- 🎯 最终实现 React Native 与 Android 性能追踪系统的集成

---

### [隔离 React Native 实例间的直接通信](https://www.callstack.com/blog/secure-communication-between-isolated-react-native-instances)

**原文标题**: [Direct Communication Between Isolated React Native Instances](https://www.callstack.com/blog/secure-communication-between-isolated-react-native-instances)

react-native-sandbox 库新增了沙盒实例间的直接通信功能，允许隔离的 React Native 实例之间安全高效地直接传递消息，无需通过宿主应用中转，同时保持原有的安全隔离特性。

- 🚀 新增直接通信模式：沙盒间可直接双向通信，无需宿主应用作为消息分发中介
- ⚡ 提升性能表现：消除中转环节，减少通信延迟和冗余代码
- 🔧 简化开发配置：通过 allowedOrigins 属性简单声明允许通信的沙盒来源
- 🛡️ 保持安全控制：采用基于来源的访问控制机制，通信需双向授权
- 🔄 支持动态权限：允许运行时动态更新通信权限配置
- 📱 适用复杂场景：支持微前端架构、插件系统等多实例应用开发
- 🌐 仿 Web 安全模型：借鉴 postMessage API 的设计理念，提供熟悉的开发体验

---

### [伊凡 - 无需苹果开发者计划即可创建开发版本](https://yvainee.com/blog/create-development-builds-without-an-Apple-Developer-Program)

**原文标题**: [Yvaine - Create Development Builds Without an Apple Developer Program](https://yvainee.com/blog/create-development-builds-without-an-Apple-Developer-Program)

本文概述了在没有个人 Apple 开发者计划的情况下，如何通过团队协作和本地配置实现 iOS 开发测试版的创建与真机调试。

- 🍎 无需个人 Apple 开发者计划，借助同事的付费账户实现真机调试
- 🔧 使用 expo-dev-client 和本地构建替代受限的 Expo Go
- 📱 通过设备 UDID 注册和配置文件更新实现多设备兼容
- 💻 利用 eas build --local 命令进行本地构建，节省云构建次数
- ⚠️ 注意更新 appleTeamId 和 associatedDomains 以匹配团队配置
- 🔄 安装含原生代码的库后需重新构建，热更新仅刷新 JS 层
- 🎯 目前方案虽繁琐但可行，作者仍在排查 expo run:ios 的设备兼容问题

---

### [EAS 工作流：专为您的应用打造的 React Native CI/CD](https://expo.dev/blog/expo-workflows-automate-your-release-process)

**原文标题**: [EAS Workflows: React Native CI/CD built for your app](https://expo.dev/blog/expo-workflows-automate-your-release-process)

该内容为 Expo 技术平台的网站导航与页脚信息，展示了其产品服务、资源链接及公司条款。

- 🚀 产品服务包括 EAS、Expo Go、Orbit 和 Snack 等开发工具
- 📚 资源板块提供文档、博客、更新日志和技术支持入口
- 👥 社区渠道含 GitHub 星标、Discord 社群和新闻订阅
- 🏢 公司信息涵盖定价、客户案例、招聘和品牌指南
- ⚖️ 法律条款包含隐私政策、服务协议和安全合规声明
- 📅 版权归属 650 Industries 公司（2025 年）

---

### [Apple 设备上基于 AI SDK 的本地文本转语音](https://www.callstack.com/blog/on-device-text-to-speech-on-apple-devices-with-ai-sdk)

**原文标题**: [On-Device Text To Speech on Apple Devices with AI SDK](https://www.callstack.com/blog/on-device-text-to-speech-on-apple-devices-with-ai-sdk)

Callstack 宣布在 AI SDK 中为 Apple 设备新增本地文本转语音功能，使 React Native 开发者能够构建完全离线、低延迟且保护隐私的语音合成应用。

- 🎯 利用 Apple 的 AVSpeechSynthesizer 实现完全本地化的文本转语音合成，无需网络连接
- ⚡ 通过直接处理音频数据流避免磁盘 I/O，实现低延迟和高性能
- 🌍 支持多语言和丰富语音选择，包括系统内置语音和 iOS 17+ 的个性化语音
- 🔒 所有处理均在设备本地完成，确保用户数据隐私和安全
- 📦 语音资源由操作系统管理，不增加应用包大小
- 🔧 提供简单 API，支持返回 WAV 格式的音频字节流，方便集成使用

---

### [React Native 性能优化策略：现代方法与工具 | 产品博客 • Sentry](https://blog.sentry.io/react-native-performance-strategies-tools/)

**原文标题**: [React Native performance tactics: Modern strategies and tools | Product Blog • Sentry](https://blog.sentry.io/react-native-performance-strategies-tools/)

本文概述了 2025 年 React Native 性能优化的现代策略与工具，强调在全新架构稳定和用户对流畅体验要求提升的背景下，通过工具和技巧提升应用性能的重要性。

- 🚀 优化启动时间：减少启动时的繁重计算，使用 React Native DevTools 和 Sentry 性能分析工具监控并改进 TTI（可交互时间）。
- 📦 减小包体积：利用 Expo Atlas 分析包大小，识别并优化主要贡献者，提升启动速度。
- ⚛️ React 优化：使用 React DevTools 高亮重渲染组件，启用 React 编译器自动优化，避免手动记忆化错误。
- 🧠 避免内存泄漏：清理事件监听器、定时器和 WebSocket 连接，使用 AbortController 取消异步操作。
- 🎬 保持 60 FPS：实时监控 FPS，避免阻塞 JavaScript 线程，使用 React 18 的并发特性或工作线程处理繁重计算。
- 📊 性能监控工具：集成 Sentry 追踪功能，分析生产环境中的性能问题，使用 Flashlight（Android）获取应用性能评分。
- 📋 列表性能优化：用 FlashList 或 LegendList 替代 FlatList，预计算数据，使用记忆化组件减少重渲染。
- 🧩 谨慎状态管理：避免 Context 滥用导致不必要的重渲染，使用 Jotai 或 Zustand 等原子状态库进行精细控制。
- 🔧 工具生态：利用 Expo Router、Reanimated 4、Sentry 等现代工具，系统化优化并持续监控应用性能。

---

### [Maestro CLI 2.0.0 版本说明，Java 17，GraalJS](https://maestro.dev/blog/introducing-maestro-2-0-0)

**原文标题**: [Maestro CLI 2.0.0 Release Notes, Java 17, GraalJS](https://maestro.dev/blog/introducing-maestro-2-0-0)

总体介绍了 Maestro 2.0 的命名含义及其作为重大版本更新的特殊性。

- 🔄 解释 2.0 版本并非普通迭代更新
- ⏳ 强调需要回溯产品历史背景才能理解其重要性
- 🚀 暗示本次更新具有里程碑式的突破性意义

---

### [Release 4.15.0 · software-mansion/react-native-screens · GitHub](https://github.com/software-mansion/react-native-screens/releases/tag/4.15)

**原文标题**: [Release 4.15.0 · software-mansion/react-native-screens · GitHub](https://github.com/software-mansion/react-native-screens/releases/tag/4.15)

React Native Screens 4.15 版本发布，主要针对底部标签栏和实验性原生组件进行了多项功能增强与错误修复。

- 🆕 安卓平台支持从外部源加载底部标签图标
- 🔄 iOS 标签栏和屏幕堆栈新增方向支持功能
- 📱 iOS 标签栏新增系统项支持能力
- 🎨 重构了标签栏外观 API，支持外观类型、布局和状态
- 🐛 修复了 iOS 26 系统中 RNSScreen 被导航栏部分遮挡的问题
- 🔧 解决了 iOS 模态手势交互导致的崩溃问题
- 📊 新增 SplitView 与 NativeStack 集成的测试用例
- 👥 本次更新由 4 位主要贡献者共同完成

---

### [发布 v0.5.0 🚀 · software-mansion/react-native-executorch · GitHub](https://github.com/software-mansion/react-native-executorch/releases/tag/v0.5.0)

**原文标题**: [Release v0.5.0 🚀 · software-mansion/react-native-executorch · GitHub](https://github.com/software-mansion/react-native-executorch/releases/tag/v0.5.0)

React Native ExecuTorch 发布 v0.5.0 版本，包含性能优化、新功能支持及 API 改进。

- 🚀 基于 C++ JSI 绑定的全原生代码重写，实现原生代码与 JS 间的零拷贝数据传输
- 🔥 iOS 端 Whisper 转录速度提升高达 2 倍
- 📷 新增 CLIP 图像语义提取功能
- 🚴 文本嵌入性能显著提升
- 🧘 重构 STT 流式 API，提供更优质量结果和开发体验
- 🐐 支持使用 zod 指定 LLM 结构化输出模式
- 👌 LLM 现在能正确处理输出中的 Unicode/表情符号
- ⚠️ 突破性变化：支持多模型实例运行，移除静态单例限制
- 📦 改用捆绑模型对象替代单独 URL 导入，简化 API 调用

---

### [GitHub - watadarkstar/react-native-parlant：一个用于将 Parlant AI 代理集成到 React Native / Expo / React 应用中的 React Native 库。](https://github.com/watadarkstar/react-native-parlant)

**原文标题**: [GitHub - watadarkstar/react-native-parlant: A React Native library for integrating Parlant AI agents into your React Native / Expo / React applications.](https://github.com/watadarkstar/react-native-parlant)

这是一个用于在 React Native/Expo/React应用中集成Parlant AI 智能体的开源库，采用 MIT 许可证，提供实时聊天功能和完整的 TypeScript 支持。

- 🤖 实时 AI 聊天 - 支持与 Parlant AI 智能体进行实时消息交互
- 📱 跨平台兼容 - 适用于 React Native、Expo 和 React 应用程序
- 🔄 自动重连 - 内置自动重试机制确保连接稳定性
- 🎯 TypeScript 支持 - 提供完整的类型定义文件
- 💾 会话管理 - 自动创建和管理聊天会话
- 🔒 内容审核 - 内置消息审核功能支持
- ⚡ 长轮询技术 - 采用高效的消息获取机制
- 🎨 高度可定制 - 支持消息和用户界面的灵活自定义
- 📦 简单安装 - 支持 yarn、npm 和 Expo 多种安装方式
- 🌟 活跃维护 - 拥有 25 个 star，持续更新发布新版本

---

### [发布版本 5.2.0 · gorhom/react-native-bottom-sheet · GitHub](https://github.com/gorhom/react-native-bottom-sheet/releases/tag/v5.2.0)

**原文标题**: [Release Release 5.2.0 · gorhom/react-native-bottom-sheet · GitHub](https://github.com/gorhom/react-native-bottom-sheet/releases/tag/v5.2.0)

这是一个 GitHub 仓库页面，主要展示了 react-native-bottom-sheet 库的 v5.2.0 版本发布内容。

- 📱 React Native 底部弹窗组件库发布 5.2.0 版本更新
- ✨ 新增可滚动创建器钩子以支持第三方列表库集成
- 🐛 修复回调钩子缺失依赖项的问题
- 🔧 优化动画状态、布局状态和滚动状态等多个核心模块
- 📦 更新示例项目依赖和类型定义
- ❤️ 获得 11 位用户的表情反应（4 个赞和 7 个爱心）

---

### [Re.Pack 5.2 新特性：更快的 Babel 转换、支持 RN 0.80 和 0.81、类型化配置及 Rozenite 兼容性](https://www.callstack.com/blog/re-pack-5-2-faster-babel-transforms-support-for-rn-0-80-0-81-rozenite)

**原文标题**: [New in Re.Pack 5.2: Faster Babel Transforms, Support for RN 0.80 & 0.81, Typed Configs & Rozenite compatibility](https://www.callstack.com/blog/re-pack-5-2-faster-babel-transforms-support-for-rn-0-80-0-81-rozenite)

Re.Pack 5.2 是一个非破坏性重大版本更新，专注于提升构建性能和开发体验，引入新的 Babel 和 SWC 混合转换管道，并正式支持 React Native 0.80 和 0.81 版本。

- 🚀 新的混合转换管道：结合 Babel 和 SWC，通过并行处理大幅提升构建性能，冷编译时间减少 2.6 倍
- 🔧 官方支持 React Native 0.80 和 0.81：移除旧版自定义解决方案，采用标准 Babel 插件处理
- 📝 全面类型化配置：新增 defineRspackConfig 和 defineWebpackConfig 助手，提供端到端类型支持
- 🧩 Rozenite 集成：支持 React Native DevTools 插件框架，增强调试体验（如网络活动面板、Redux 状态检查）
- ⚡ 其他优化：包括编译进度条显示、错误堆栈直接跳转编辑器、Terser 插件预配置等
- 📦 升级指南：无破坏性变更，建议替换旧版转换规则并更新相关依赖至最新版本

---

### [未找到标题](https://reactnativereusables.com/)

**原文标题**: [No title found](https://reactnativereusables.com/)

文章概述了人工智能在医疗领域的应用现状与未来趋势，重点讨论了技术突破、实际应用场景和面临的挑战。

- 🤖 AI 辅助诊断系统显著提升医学影像分析准确率
- 🧬 基因测序与大数据分析助力个性化治疗方案制定
- ⚕️ 手术机器人实现微创精准操作，减少手术风险
- 📊 智能健康监测设备实现慢性病日常管理
- 🔒 数据隐私保护和算法透明度成为行业关注焦点
- 🌐 跨机构医疗数据共享仍存在技术壁垒

---

### [Expo SDK 54 发布！全面解析新特性 - YouTube](https://www.youtube.com/watch?v=zWSWurwPmVE)

**原文标题**: [Expo SDK 54 is out! Everything that's new - YouTube](https://www.youtube.com/watch?v=zWSWurwPmVE)

这是 YouTube 平台页脚常见的服务条款与功能链接集合。

- ℹ️ 关于平台基本信息
- 📢 新闻与媒体相关
- ©️ 版权声明信息  
- 📞 用户联系渠道
- 🎬 内容创作者资源
- 💼 广告合作业务
- 👨‍💻 开发者工具支持
- 📑 使用条款说明
- 🔒 隐私保护政策
- ⚖️ 平台安全规范
- 🔧 产品运作机制
- 🧪 新功能测试计划
- Ⓜ️ 谷歌版权标识（2025）

---

### [iOS 应用中逐步采用 React Native - YouTube](https://www.youtube.com/watch?v=siA6LuGxaAI)

**原文标题**: [Incremental React Native Adoption in iOS Apps - YouTube](https://www.youtube.com/watch?v=siA6LuGxaAI)

这是 YouTube 网站页脚常见链接列表的概述。

- ℹ️ 关于平台的基本信息和公司背景
- 📰 相关的新闻和公告信息
- ©️ 版权声明与知识产权相关条款
- 📞 用户联系与客户支持渠道
- 🎬 内容创作者相关的资源与计划
- 📢 广告投放与商业合作机会
- 💻 面向开发者的 API 与技术资源
- 📑 平台服务条款与使用协议
- 🔒 隐私政策与数据保护措施
- ⚖️ 政策安全与社区准则说明
- 🔧 YouTube 功能运作机制介绍
- 🧪 新功能测试与体验信息
- ®️ 版权归属与公司标识（谷歌 2025）

---

### [何时使用空中更新 | 三个重要的 OTA 应用场景 - YouTube](https://www.youtube.com/watch?v=PMRekmaeb1o)

**原文标题**: [When to use over the air updates | Three important OTA use cases - YouTube](https://www.youtube.com/watch?v=PMRekmaeb1o)

这是 YouTube 网站页脚常见链接列表的摘要概述。

- ℹ️ 关于平台的基本信息和公司详情
- 📰 新闻稿和媒体相关资源
- ©️ 版权声明与知识产权信息
- 📞 用户联系与客户支持渠道
- 🎬 内容创作者专属资源与工具
- 💼 广告合作与商业推广机会
- 💻 开发者 API 与技术文档
- 📑 服务条款与使用协议
- 🔒 隐私政策与数据保护措施
- ⚖️ 平台政策与安全指南
- 🔧 YouTube 功能运作机制说明
- 🧪 新功能测试与体验计划
- ®️ 版权归属与公司标识（谷歌 2025）

---

### [使用 Expo 路由器实现带嵌套标签页的抽屉导航 - YouTube](https://www.youtube.com/watch?v=A3NyYsNxMGM)

**原文标题**: [Drawer Navigation with Nested Tabs using Expo Router - YouTube](https://www.youtube.com/watch?v=A3NyYsNxMGM)

这是 YouTube 网站页脚常见链接列表的摘要概述。

- ℹ️ 关于平台的基本信息
- 📢 新闻与媒体相关资源
- ©️ 版权声明与政策
- 📞 用户联系渠道
- 🎬 内容创作者相关信息
- 💼 广告合作与投放
- 👨‍💻 开发者资源与 API
- 📑 服务条款与使用协议
- 🔒 隐私保护政策
- ⚖️ 平台安全政策与运作方式
- 🧪 新功能测试信息
- ®️ 版权归属与公司信息（注明至 2025 年）

---

### [React Native 电台 - RNR 341 - 与大师莱兰·高岭同行特辑](https://infinite.red/react-native-radio/rnr-341-catching-up-with-maestro-featuring-leland-takamine)

**原文标题**: [React Native Radio - RNR 341 - Catching Up With Maestro Featuring Leland Takamine](https://infinite.red/react-native-radio/rnr-341-catching-up-with-maestro-featuring-leland-takamine)

React Native Radio 播客第 341 集邀请 Maestro CEO Leland Takamine 讨论其移动端 UI 测试工具的发展历程、新功能及未来规划。

- 🎙️ Maestro 三年前推出，现已成为 DoorDash、微软等大型企业的首选端到端测试工具
- 💻 新推出 Maestro Studio 桌面应用，提升测试可访问性和集成体验
- 🤖 放弃运行时 AI 测试方案，转向通过 MCP 工具实现 AI 辅助编写确定性测试脚本
- 📱 已支持 Web 测试，正逐步扩展物理设备云端测试能力
- ⚡ 测试可靠性是核心优势，支持万级测试套件稳定运行
- 🔧 开源社区超 5000 人，被 Meta 等团队用于框架自身测试
- 🚀 未来重点发展测试自修复功能和云端并行测试服务

---

### [火箭飞船 | #079 - 新架构、AI 影响及 React Native 创新浪潮与 Jamon Holmgren 对话](https://share.transistor.fm/s/d0d2fba0)

**原文标题**: [Rocket Ship | #079 - New Architecture, AI Impact, and the Next Wave of React Native Innovation with Jamon Holmgren](https://share.transistor.fm/s/d0d2fba0)

该内容为播客平台的功能与操作选项列表。

- 🎧 播客订阅渠道（苹果播客/Spotify 等平台）
- 📤 内容分享与嵌入功能
- ⏯️ 播放控制（从指定时间点开始）
- 📝 完整文字稿查看
- 🌐 官方网站访问入口
- 📋 章节分段功能
- 📱 多平台兼容支持（覆盖 20+ 个播客应用）
- 🔗 链接复制快捷操作

---

### [大 O 表示法](https://samwho.dev/big-o/)

**原文标题**: [Big O](https://samwho.dev/big-o/)

大 O 符号用于描述函数输入规模与执行时间增长之间的关系，涵盖常数、对数、线性和二次复杂度等常见类型，并通过实际代码示例说明如何优化算法时间复杂度。

- 📊 大 O 符号通过输入规模增长描述函数性能，而非实际计时  
- ⏱️ 线性复杂度 O(n) 示例：循环求和函数耗时随输入倍数增加  
- 🚀 常数复杂度 O(1) 示例：数学公式求和几乎无时间增长  
- 🔄 二次复杂度 O(n²) 示例：冒泡排序在最坏情况下需 n²次操作  
- 🔍 对数复杂度 O(log n) 示例：二分查找每次排除一半可能性  
- ⚠️ 大 O 默认描述最坏情况，且忽略常数项（如 O(2n) 简化为 O(n)）  
- 💡 优化实践：用 Set 替代数组查找（O(1)）、避免循环内嵌套 O(n) 操作  
- 💾 缓存中间结果（如阶乘计算）可提升平均性能但增加内存消耗  
- 📈 复杂度增长顺序：O(1) < O(log n) < O(n) < O(n²)

---

### [我们如何将 Rush.js 单体仓库迁移至 Node 类型剥离——Calm 博客](https://blog.calm.com/engineering/how-we-migrated-our-rushjs-monorepo-to-node-type-stripping)

**原文标题**: [How we migrated our Rush.js monorepo to Node type stripping — Calm Blog](https://blog.calm.com/engineering/how-we-migrated-our-rushjs-monorepo-to-node-type-stripping)

概述了将 Rush.js monorepo 迁移到 Node 类型剥离的过程，包括动机、挑战、实施步骤和成果。

- 🚀 通过跳过转译直接运行 TypeScript 文件，本地开发任务速度提升 30-40%，CI 流程节省 3-6 分钟
- ⚠️ 主要挑战是 ESM 模块不可变特性与测试库（如 Sinon）模块存根实践的冲突
- 💡 关键突破是采用"存根类而非模块"策略，将函数重构为类或命名对象导出
- 🔧 迁移过程分阶段：升级 Node 版本、ESM 准备（修复文件扩展名/JSON 导入/第三方 CJS 模块）、类型剥离准备（重构枚举等特性）
- 📦 针对 Rush.js monorepo 的特殊处理：使用条件导出解决工作区导入的文件扩展名问题
- 🧪 创建自定义 ESLint 规则和 codemod 工具实现增量重构并防御回归
- ⚡ 成果包括应用启动速度提升 40%、单元测试运行速度提升 35%，以及 CI 流水线显著时间节省

---

### [CSS random() 的随机探索 | WebKit](https://webkit.org/blog/17285/rolling-the-dice-with-css-random/)

**原文标题**: [  Rolling the Dice with CSS random() | WebKit](https://webkit.org/blog/17285/rolling-the-dice-with-css-random/)

CSS 的 random() 函数即将推出，它允许开发者在无需 JavaScript 的情况下生成随机数，用于动画延迟、布局位置、颜色生成等多种场景。该函数支持定义范围、步长参数，并可通过命名标识或 element-shared 实现随机值的共享。目前已在 Safari Technology Preview 中提供测试，开发团队正积极收集用户反馈以优化功能设计。

- 🌟 CSS random() 函数支持生成随机数值，无需依赖 JavaScript
- 🎯 函数格式为 random(min, max, step)，支持百分比、像素等多种单位
- ✨ 通过命名标识（如 --foo）可在单个元素内共享随机值
- 🔗 使用 element-shared 可实现跨元素属性级随机值共享
- 🌌 实际应用案例包括星空背景、网格随机布局、照片堆叠效果和幸运转盘动画
- 🧪 当前仅在 Safari Technology Preview 中可用，功能尚处于草案阶段
- 📣 开发团队邀请开发者通过社交媒体或错误报告渠道提供使用反馈

---

### [una.im | 5 个实用的 CSS 函数：运用全新@function 规则](https://una.im/5-css-functions/)

**原文标题**: [una.im | 5 Useful CSS functions using the new @function rule](https://una.im/5-css-functions/)

CSS 自定义函数功能已在 Chrome 139 中实现，通过@function 规则可创建具有逻辑处理能力的自定义函数，使 CSS 代码更整洁且支持动态样式生成，目前仅 Chrome 支持该特性。

- 🎯 反值函数：通过--negate() 函数可计算值的负数，简化样式中的负值计算
- 🎨 透明度函数：--opacity() 函数可将任何颜色转换为指定透明度的变体，支持 RGB 色彩空间
- 📱 流式排版函数：--fluid-type() 使用 clamp() 实现响应式文字大小，支持根据标题/正文类型设置不同缩放比率
- 🔄 条件圆角函数：--conditional-radius() 实现视口边缘自适应圆角，无需媒体查询即可防止布局异常
- 📐 布局侧边栏函数：--layout-sidebar() 通过媒体查询创建响应式网格布局，默认侧边栏宽度为 20ch
- 🌗 明暗主题函数：扩展 light-dark() 功能，支持非颜色属性的主题化控制，通过数据属性实现主题切换

---

### [ESLint 新增并行检查支持，终结长达十年的...](https://socket.dev/blog/eslint-adds-support-for-parallel-linting)

**原文标题**: [ESLint Adds Support for Parallel Linting, Closing 10-Year-Ol...](https://socket.dev/blog/eslint-adds-support-for-parallel-linting)

Nx npm 软件包在供应链攻击中被劫持，利用 AI CLI 工具窃取用户机密信息与钱包数据，Socket 的 AI 扫描器成功检测并标记了该恶意软件。
- 🔍 恶意 Nx npm 版本通过 AI 命令行工具窃取敏感数据和钱包信息
- ⚠️ Socket 的 AI 安全扫描器及时发现并阻断了这场供应链攻击
- 📅 该安全事件发生于 2025 年 8 月 27 日，由安全研究人员 Sarah Gooding、Olivia Brown 和 Peter van der Zee 联合披露

---

### [发布 v4.1.0 · colinhacks/zod · GitHub](https://github.com/colinhacks/zod/releases/tag/v4.1.0)

**原文标题**: [Release v4.1.0 · colinhacks/zod · GitHub](https://github.com/colinhacks/zod/releases/tag/v4.1.0)

Zod 4.1.0 版本发布，引入 Codecs 双向转换 API、safeExtend 安全扩展方法、哈希验证功能及多项改进。

- 🎯 新增 Codecs API 支持双向数据转换（解码/编码），解决类型安全转换需求
- 🔒 引入.safeExtend() 方法确保对象扩展时类型安全，保留原有校验规则
- 🔢 新增 z.hash() 验证常见哈希算法（MD5/SHA 系列），支持 hex/base64 编码格式
- 🧪 提供 z.hex() 通用十六进制字符串验证和 z.uuid() 对 Max UUID 的支持
- ⚡ 新增异步处理方法（decodeAsync/encodeAsync）和安全验证变体（safeDecode/safeEncode）
- 📦 为控制体积，新方法未加入 Zod Mini，通过顶级函数提供等效功能

---

### [Rspack 1.5 版本发布 - Rspack](https://rspack.rs/blog/announcing-1-5)

**原文标题**: [Announcing Rspack 1.5 - Rspack](https://rspack.rs/blog/announcing-1-5)

Rspack 1.5 版本发布，带来多项性能优化和新特性，包括实验性的 Barrel 文件优化、更快的文件监听器、浏览器环境支持、Rust 扩展能力、常量内联优化等，同时宣布停止对 Node.js 16 的支持并更新了 Rstack 生态工具链。

- 🚀 **Barrel 文件优化**：实验性功能 lazyBarrel 可延迟构建无副作用的 Barrel 文件，显著减少模块解析和构建时间，提升构建性能。
- ⚡ **更快的文件监听器**：基于 Rust 的原生文件监听器替代 watchpack，HMR 性能提升高达 50%，支持增量更新和持续运行。
- 🌐 **浏览器环境支持**：推出 @rspack/browser，可在纯浏览器环境中运行 Rspack，支持在线打包和交互式演示。
- 🦀 **Rust 扩展支持**：允许使用 Rust 编写插件和加载器，直接与 Rspack Rust 核心集成，提升性能并保持 JavaScript API 兼容性。
- 🔧 **常量内联优化**：实验性功能 inlineConst 和 inlineEnum 支持跨模块内联常量和 TypeScript 枚举，帮助压缩工具更精确地消除未使用代码。
- 📦 **类型重导出分析**：改进 TypeScript 类型重导出的检测，避免误报警告，提升类型处理的准确性。
- 🧩 **内置虚拟模块插件**：新增高性能的 VirtualModulesPlugin，减少虚拟模块的读取和解析开销，提升处理大量虚拟模块的性能。
- 🔗 **Module Federation 运行时提升**：将 Module Federation 运行时代码集成到 Rspack 运行时并提升至运行时块，减少多入口场景下的包体积并修复初始化错误。
- 📉 **安装包体积优化**：通过多项优化措施，将安装包体积从 63.7MB 减少至 49.9MB，并集成自动化体积检查。
- ⏱️ **Seal 阶段性能优化**：通过改进数据结构、增加并行化和引入热代码缓存，Seal 阶段性能提升显著，大型项目构建效率大幅提高。
- ⚠️ **停止支持 Node.js 16**：由于 Node.js 16 已结束生命周期，Rspack 1.5 不再支持，建议升级至 Node.js 18.12.0 或更高版本。
- 🔍 **解析器 JavaScript API**：集成 rspack-resolver 到 JavaScript API，提供模块解析功能，便于用户利用 Rspack 的模块解析能力。
- 🛠️ **Rstack 生态更新**：包括 Rslint 发布、Rsbuild 1.5 默认启用多项新特性、Rslib 0.12 集成 Rstest、Rspress 2.0 beta 引入 Markdown 文本复制功能、Rsdoctor 1.2 增强构建分析能力、Rstest 0.2 提升测试框架功能和稳定性。

---

### [Bun v1.2.21 | Bun 博客](https://bun.com/blog/bun-v1.2.21)

**原文标题**: [Bun v1.2.21 | Bun Blog](https://bun.com/blog/bun-v1.2.21)

Bun 发布新版本，修复了 69 个问题，引入了多项新功能和优化，包括统一的 SQL 客户端 Bun.SQL、原生 YAML 支持、性能提升、安全增强和开发者工具改进。

- 🐛 修复了 69 个问题，涉及运行时、包管理器、Node.js 兼容性和错误处理
- 🗄️ 新增 Bun.SQL，统一支持 MySQL、SQLite 和 PostgreSQL，无需额外依赖
- 📄 添加原生 YAML 支持，可直接导入和解析 YAML 文件
- ⚡ 优化了 postMessage 和 structuredClone，字符串传输速度提升 500 倍
- 🔒 引入 Bun.secrets，用于安全存储和管理敏感信息
- 🔍 bun install 新增安全扫描 API，可在安装前检测漏洞
- 🎛️ bun audit 新增过滤选项，支持按严重级别和依赖类型筛选
- 📦 bun install --lockfile-only 速度大幅提升，减少网络带宽使用
- 🖱️ bun update --interactive 支持滚动和响应式布局
- 💤 减少 Bun.serve 空闲时的 CPU 使用
- 🛠️ Bun.build() 支持编译独立可执行文件，包括跨平台和元数据设置
- 🧹 新增 Bun.stripANSI()，高性能去除 ANSI 转义码
- 🪟 Windows 版 bun.exe 现已代码签名，消除安全警告
- 📦 bunx 新增 --package 标志，支持运行特定包中的二进制文件
- 🌳 package.json 的 sideEffects 字段现支持 glob 模式，优化 tree-shaking
- 🌐 新增 --user-agent CLI 标志，可自定义所有 fetch 请求的 User-Agent 头
- 🔧 多项 Node.js 兼容性改进和错误修复

---

### [客户挑战](https://www.firefox.com/en-US/firefox/142.0/releasenotes/)

**原文标题**: [Client Challenge](https://www.firefox.com/en-US/firefox/142.0/releasenotes/)

浏览器中 JavaScript 被禁用，导致网站核心功能无法加载，可能原因包括浏览器扩展、网络问题或设置问题。

- 🚫 JavaScript 被禁用
- 🌐 网络连接问题
- 🔧 浏览器扩展干扰
- 🛡️ 广告拦截器影响
- 🔄 建议更换浏览器尝试

---

### [未找到标题](https://x.com/grabbou/status/1829126194022715617)

**原文标题**: [No title found](https://x.com/grabbou/status/1829126194022715617)

JavaScript 功能未启用，检测到当前浏览器禁用了 JavaScript。请启用 JavaScript 或切换至支持的浏览器以继续使用 x.com，支持的浏览器列表可在帮助中心查看。遇到问题无需担心，可尝试重新操作或暂时禁用隐私相关扩展插件。

- 🌐 浏览器 JavaScript 被禁用
- 🔧 需启用 JS 或更换支持浏览器
- 📖 支持浏览器列表详见帮助中心
- ⚠️ 隐私扩展插件可能导致访问异常
- 🔄 建议尝试刷新或禁用插件后重试

---

### [未找到标题](https://x.com/grabbou)

**原文标题**: [No title found](https://x.com/grabbou)

浏览器检测到 JavaScript 被禁用，无法正常使用 X 平台
- 🚫 JavaScript 未启用导致功能受限
- 🌐 建议启用 JavaScript 或更换支持浏览器
- 📖 支持浏览器列表可查看帮助中心
- 🔧 隐私扩展可能导致问题，建议暂时禁用
- 🔄 尝试重新加载页面解决问题

---

