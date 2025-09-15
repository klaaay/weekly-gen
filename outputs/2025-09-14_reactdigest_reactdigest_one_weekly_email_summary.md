### [React 文摘：电子邮件通讯](https://reactdigest.net/)

**原文标题**: [React Digest: Email Newsletter](https://reactdigest.net/)

React Digest 是一份为 React 开发者精心策划的周报，汇集高质量内容帮助前端工程师高效学习。

- 📧 拥有超过 22,010 名前端软件工程师订阅的每周邮件
- ✂️ 提供精选文章与简短摘要节省用户时间
- 🎯 每周推送值得阅读的技术内容避免信息过载
- 📚 保证订阅者每周都能学习到新知识
- 👍 获得用户好评，被认为是有用且撰写精良的资讯源
- 🌍 被全球前端工程师广泛阅读的权威资讯

---

### [TanStack DB 交互式指南 | 大规模前端实践](https://frontendatscale.com/blog/tanstack-db/)

**原文标题**: [An Interactive Guide to TanStack DB | Frontend at Scale](https://frontendatscale.com/blog/tanstack-db/)

家庭待办事项提醒，包括与家人保持联系和活动安排。

- 📞 给妈妈打电话
- ✈️ 计划夏季旅行
- 🎁 购买生日礼物

---

### [细致](https://www.meticulous.ai/?utm_source=react_digest)

**原文标题**: [Meticulous](https://www.meticulous.ai/?utm_source=react_digest)

Meticulous AI 是一款通过记录用户交互自动生成并维护测试套件的工具，旨在帮助开发者无需编写测试代码即可全面覆盖应用的各种边缘情况，提升开发效率和代码质量。

- 🚀 自动记录用户交互并生成测试，无需编写或维护任何测试代码
- 🔍 全面覆盖所有代码分支、用户流程和边缘情况
- ⚡ 集成 CI 后即时查看 PR 对现有工作流的影响，避免回归问题
- 🛡️ 通过模拟后端响应实现无副作用测试，消除误报
- 📊 支持与现有测试套件结合使用或完全替代
- 🌐 兼容主流前端框架（NextJS、React、Vue 等）
- ⏱️ 高度并行化测试，数千个测试可在 120 秒内完成
- 💡 获得 Dropbox、Notion 等 100 多家企业信任使用

---

### [迁移至 React Native 新架构（2025）- Shopify](https://shopify.engineering/react-native-new-architecture)

**原文标题**: [Migrating to React Native's New Architecture (2025) - Shopify](https://shopify.engineering/react-native-new-architecture)

Shopify 成功将 Shopify Mobile 和 POS 两大应用迁移至 React Native 新架构，在维持每周发布节奏和服务数百万商家的同时，完成了对复杂代码库的改造。迁移过程采用双架构兼容策略，聚焦最小化代码变更，并通过分阶段发布控制风险。新架构带来启动性能提升和渲染优化，但也暴露出部分组件性能问题，团队通过社区协作和渐进式优化逐一解决。

- 🚀 双架构并行开发：通过 TopHat 工具实现 PR 级别的双架构构建测试，确保迁移期间功能不中断
- ⚙️ 最小化代码改动：优先确保新架构兼容性，延后重构优化，减少对开发进度的影响  
- 📱 性能提升成果：Android 启动时间优化 10%，iOS 提升 3%，状态批处理减少冗余渲染
- 🐛 常见问题解决方案：针对空白屏幕、视图扁平化等问题提供具体调试和代码调整方案
- 🌐 生态协作：与 Meta、Software Mansion 合作解决 Reanimated 性能问题，推动上游修复
- 📊 渐进式发布策略：利用 Android 应用商店更灵活的发布控制，分阶段验证稳定性
- ⚠️ 后续挑战：部分复杂组件加载时间增加 20%，通过持续优化和 TurboModule 迁移应对

---

### [React Fast Refresh：新一代热重载技术解析 | Leapcell](https://leapcell.io/blog/react-fast-refresh)

**原文标题**: [React Fast Refresh: Next-Gen Hot Reloading Explained | Leapcell](https://leapcell.io/blog/react-fast-refresh)

React Fast Refresh 是 React 官方推出的新一代热重载方案，支持模块级和组件级局部刷新，保留应用状态，提升开发体验。

- 🔄 支持模块级热更新，仅更新修改的模块代码并重新渲染组件
- ⚡ 针对仅导出 React 组件的文件，实现局部刷新并保留状态
- 🚨 错误处理友好：修复语法或运行时错误后无需重载应用
- 📦 依赖 HMR 机制，结合 Babel 插件和运行时实现深度集成
- ⚙️ 支持函数组件和 Hooks 状态保留，类组件状态会重置
- 🌐 核心实现与平台无关，既支持 React Native 也适用于 Web
- 🔧 提供 // @refresh reset 指令可强制组件重新挂载
- 📊 运行时通过注册函数和签名收集实现组件与 Hooks 的更新追踪

---

### [Next.js 应用快速 SEO 指南 | 趣味编程](https://playfulprogramming.com/posts/seo-nextjs-guide)

**原文标题**: [
	Quick SEO Guidelines for Your Next.js App | Playful Programming
](https://playfulprogramming.com/posts/seo-nextjs-guide)

Next.js 应用 SEO 优化指南，涵盖元数据、结构化数据、站点地图等关键策略，提升搜索引擎可见性和用户体验。

- 📝 使用内置 Metadata 类型在 layout.tsx 中定义全局元数据，确保在搜索引擎和社交平台正确显示
- 🎯 通过 next/head 组件实现页面特定 SEO，如自定义标题和描述，适用于博客和电商页面
- 🧠 添加 JSON-LD 结构化数据生成富媒体摘要，提高搜索结果的点击率
- 🗺️ 利用 sitemap.ts 自动生成站点地图，支持动态内容更新和搜索引擎高效爬取
- 🤖 配置 robots.txt 文件控制搜索引擎爬虫权限，保护敏感页面不被索引
- 🖼️ 使用 next/image 组件优化图片，提供 alt 文本并采用 WebP/AVIF 格式提升性能
- ⚡ 通过 SSR/SSG、代码拆分和缓存优化核心 Web 指标，改善加载速度和交互体验

---

### [使用 Bun 构建 React 应用：现代化开发体验](https://pmbanugo.me/blog/react-app-with-bun)

**原文标题**: [Building React Apps with Bun: A Modern Development Experience](https://pmbanugo.me/blog/react-app-with-bun)

Bun 作为现代 JavaScript 运行时，为 React 开发提供了高效的一体化工具链，通过内置打包、测试和包管理功能简化开发流程，显著提升开发体验和构建速度。

- 🚀 Bun 提供比 Node.js 更快的性能，并集成打包、测试和包管理功能
- ⚡ 通过单一命令快速创建 React+Tailwind 项目：bun init --react=tailwind
- 📁 自动生成优化的项目结构，依赖项极少，无需配置 Webpack 或 Babel
- 🛣️ 支持使用 wouter 进行路由管理，可快速构建多页面应用
- 🎨 无缝集成 Tailwind CSS，自动处理样式优化和代码净化
- 🔥 开发服务器启动极快，热重载近乎即时，TypeScript 开箱即用
- 📦 生产构建自动进行代码分割、摇树优化和压缩，部署简单
- ⚠️ 目前仍较新，复杂企业级项目建议暂用成熟工具链

---

### [终于，JavaScript 中的安全数组方法 - 马特·史密斯](https://allthingssmitty.com/2025/09/08/finally-safe-array-methods-in-javascript/)

**原文标题**: [
    Finally, safe array methods in JavaScript - Matt Smith
  ](https://allthingssmitty.com/2025/09/08/finally-safe-array-methods-in-javascript/)

JavaScript ES2023 引入了三种新的非变异数组方法，用于替代传统会改变原数组的方法，提升代码安全性和可维护性。

- 🛡️ 传统方法如.sort()、.reverse() 和.splice() 会直接改变原数组，可能导致难以追踪的 bug
- 🔄 toSorted() 方法返回排序后的新数组，原数组保持不变
- ↪️ toReversed() 生成反转数组的副本，不影响原始数据
- ✂️ toSpliced() 安全地实现元素增删操作，返回新数组
- ⚛️ 在 React 中特别有用，遵循不可变原则确保状态更新触发重新渲染
- 🌐 所有现代浏览器和 Node.js 20+ 版本都已支持这些新方法
- 📦 旧环境可通过 core-js 等 polyfill 实现兼容

---

### [JS fetch 将字符串请求体转换为 UTF-8 编码](https://evanhahn.com/js-fetch-converts-strings-to-utf8/)

**原文标题**: [JS fetch converts string request bodies to UTF-8](https://evanhahn.com/js-fetch-converts-strings-to-utf8/)

当 fetch 请求体为字符串时，服务器会收到 UTF-8 编码的字节序列，这是现代 JavaScript 运行时的标准行为。

- 🧪 测试验证：通过 Crystal 服务器捕获字节流，字符串"🍉"被编码为 UTF-8 字节序列 f0 9f 8d 89
- 📜 规范依据：Fetch 规范虽未直接规定，但推荐使用 UTF-8 编码（"using UTF-8 encode is encouraged"）
- 🌐 环境兼容：在 Firefox 142、Node 24 和 Deno 2.4 等主流环境中测试结果一致
- ⚠️ 注意事项：可能存在少数运行环境采用其他编码方式（如 isomorphic encode）
- 💡 创作动机：作者因未找到明确文档而进行实践验证，旨在为开发者提供参考

---

### [使用`Intl.Segmenter` API 实现精确文本长度 | 自动魔法](https://blog.sangeeth.dev/posts/accurate-text-lengths-with-intl-segmenter-api/)

**原文标题**: [
    
    Accurate text lengths with `Intl.Segmenter` API | Automagic
    
](https://blog.sangeeth.dev/posts/accurate-text-lengths-with-intl-segmenter-api/)

JavaScript 中字符串长度计算因 UTF-16 编码存在偏差，如表情符号和某些语言字符会返回异常长度值，可通过 Intl.Segmenter API 实现符合人类感知的字符计数。

- 🧠 JavaScript 的 String.length 基于 UTF-16 编码单元计数，导致表情符号（如👨‍👩‍👧‍👦显示长度为 11）和非拉丁字符（如印地语"दरबार"显示 5 而非实际 4）长度计算错误
- 🍎 Swift 语言的 String.count 通过扩展字素簇（extended grapheme cluster）实现符合人类感知的字符计数，所有测试字符均返回预期长度
- 🌐 Intl.Segmenter API 提供解决方案：通过设置 granularity: "grapheme"可准确分割字符，realLength() 函数实现跨浏览器兼容的精确计数
- ⚠️ 注意事项：控制字符仍会导致计数偏差（如"text\u0001\u0002"返回 6 而非 4），且计算复杂度为 O(n) 需谨慎替换原有 length 方法
- 💡 开发建议：面向国际用户的应用应避免基于 String.length 进行长度限制，特别是姓名输入框和社交平台字符数统计场景

---

### [浏览器中的液态玻璃：利用 CSS 与 SVG 实现折射效果 — kube.io](https://kube.io/blog/liquid-glass-css-svg/)

**原文标题**: [Liquid Glass in the Browser: Refraction with CSS and SVG — kube.io](https://kube.io/blog/liquid-glass-css-svg/)

本文探讨了如何使用 CSS 和 SVG 置换图在网页上模拟苹果 WWDC 2025 推出的液态玻璃效果，通过物理折射计算实现类似弯曲折射玻璃的 UI 视觉效果，并提供了交互式演示和组件示例。

- 🔍 基于斯涅尔定律模拟光线在玻璃中的折射行为，使用四种表面函数（凸圆、凸方圆形、凹形、唇形）控制玻璃曲率
- 🎨 通过 SVG 置换图将折射向量场转换为图像，利用<feDisplacementMap>实现像素位移效果，支持参数化调节
- ⚡ 当前仅 Chrome 支持 backdrop-filter 调用 SVG 滤镜，其他浏览器可查看基础演示但无法体验完整效果
- 💡 包含实际 UI 组件实现：放大镜、搜索框、开关、滑块和音乐播放器，展示不同参数下的折射表现
- ✨ 添加高光特效增强视觉真实感，通过法线角度计算边缘光照强度
- 📊 采用预计算和归一化优化性能，127 条射线模拟单半径折射，通过旋转实现整体效果
- ⚠️ 存在跨浏览器限制和性能瓶颈，动态调整形状需重建置换图，目前仅建议实验性使用

---

### [为何我更偏爱 ems 而非 rems | Go Make Things](https://gomakethings.com/why-i-still-prefer-ems-over-rems/)

**原文标题**: [Why I still prefer ems over rems | Go Make Things](https://gomakethings.com/why-i-still-prefer-ems-over-rems/)

本文讨论了作者为何在 CSS 中仍偏爱使用 em 单位而非 rem 单位，并解释了其 UI 库 Kelp 全面采用 em 的原因。

- 🌊 em 单位基于当前元素的字体大小计算，而 rem 始终基于根元素字体大小
- ⚖️ em 能使内边距、外边距等属性随字体大小按比例缩放，保持设计一致性
- 🧩 通过父元素统一设置 em 单位，可批量调整子元素尺寸，减少重复代码
- ⚠️ em 单位存在嵌套叠加效应，需注意避免意外多重放大
- 🚀 作者认为 em 的复合特性反而是其优势，可通过合理设计规避问题

---

### [CSS 颜色变换 • 乔希·W·科莫](https://www.joshwcomeau.com/animation/color-shifting/)

**原文标题**: [Color Shifting in CSS • Josh W. Comeau](https://www.joshwcomeau.com/animation/color-shifting/)

本文介绍了在 CSS 中实现粒子颜色动态变换效果的技巧，包括使用 HSL 颜色格式生成随机色调、通过 CSS 滤镜 hue-rotate 实现颜色旋转动画，以及解决浏览器在 RGB 颜色空间插值导致的中间色调灰暗问题。

- 🎨 使用 HSL 格式生成协调的随机颜色，通过固定饱和度和亮度确保色调统一
- 🔄 传统 background-color 动画在 RGB 空间插值会导致中间色调灰暗，限制颜色旋转角度
- 🌈 采用 filter: hue-rotate() 滤镜实现完整颜色旋转，性能更优且支持任意角度变化
- ⚡ CSS 滤镜方案比传统颜色动画具有更好的性能表现
- ✨ 介绍了使用@property 定义类型化自定义属性实现颜色变换的替代方案
- 💫 通过添加随机闪烁效果和变化参数增强粒子动画的生动性
- 📚 作者将在 9 月 24 日推出动画课程，分享更多特效实现技巧

---

### [无框架下的 React 服务器组件支持](https://krasimirtsonev.com/blog/article/vanilla-react-server-components-with-no-framework)

**原文标题**: [React Server Components support without a framework](https://krasimirtsonev.com/blog/article/vanilla-react-server-components-with-no-framework)

作者在 ReactSummit 与 Vercel 团队交流后，为解决在非 Next.js 框架中使用 React Server Components（RSC）的难题，开发了开源工具 Forket。该工具通过代码分拆和运行时协作，实现了无框架的 RSC 支持。

- 🛠️ Forket 在构建时将代码拆分为服务端和客户端版本，通过 AST 分析建立组件依赖图并标注文件角色
- 🌐 服务端版本处理客户端边界：序列化 props、提取 children 并注入水合逻辑，通过流式渲染输出 HTML
- 🔄 客户端版本替换服务端动作为代理调用，通过全局函数 FSA_call 实现前后端通信
- 🧩 采用"岛屿架构"模式，要求至少一个客户端入口文件（use client）用于组件水合
- ⚙️ 提供 CLI 和 JS API 两种使用方式，需配置源目录和输出目录，并集成 Express 等 HTTP 服务器
- 🚀 工具与构建工具链解耦，支持 Vite/Webpack 等生态，目前已开源并邀请社区测试反馈

---

### [编程文摘：邮件通讯](https://programmingdigest.net/?utm_source=web-archive&utm_campaign=react)

**原文标题**: [Programming Digest: Email Newsletter](https://programmingdigest.net/?utm_source=web-archive&utm_campaign=react)

一份为软件工程师精心筛选的每周通讯，提供精选文章和简短摘要，帮助订阅者节省时间并每周学习新知识。

- 📧 超过 20,943 名软件工程师订阅的每周电子邮件通讯
- 🎯 提供经过人工筛选的优质技术文章与摘要
- ⏱️ 帮助工程师节省内容筛选时间，提升学习效率
- 🌟 读者反馈积极，认可其内容价值和学习效果
- 👥 受到全球软件工程师群体的广泛阅读和认可
- 📚 由 Bonobo Press 自 2013 年持续运营至今

---

### [科技领导力：电子邮件通讯](https://leadershipintech.com/?utm_source=web-archive&utm_campaign=react)

**原文标题**: [Leadership in Tech: Email Newsletter](https://leadershipintech.com/?utm_source=web-archive&utm_campaign=react)

一份为技术主管、工程经理和高级工程师精心策划的每周通讯，旨在帮助他们成为更优秀的领导者。

- 📧 每周一封邮件，已吸引超过 27,641 名工程领导者加入
- 📖 精选文章并附简短摘要，节省寻找有价值内容的时间
- 🌱 每周学习新知识，持续提升领导力技能
- 💬 读者好评：内容精准，涵盖架构讨论、会议规划及沟通等关键话题
- 🎯 特别推荐关于授权技巧的文章，强调其重要性

---

### [C#文摘：电子邮件通讯](https://csharpdigest.net/?utm_source=web-archive&utm_campaign=react)

**原文标题**: [C# Digest: Email Newsletter](https://csharpdigest.net/?utm_source=web-archive&utm_campaign=react)

C# Digest 是一份专为.NET 开发者精心策划的每周通讯，旨在通过筛选优质内容为开发者节省时间并持续学习新知识。  
- 📧 订阅人数超过19,813名C#工程师  
- 📖 每周推送精选文章与简短摘要  
- ⏱️ 帮助开发者节省内容筛选时间  
- 🌟 读者反馈实用性强（如功能标志、LINQ 技术分享）  
- 🔧 内容涵盖.NET 新版本特性与实战案例（如诊断监听器、操作结果模式）  
- 🌍 被全球多家企业.NET 工程师阅读

---

### [让开发者与时俱进——Bonobo 出版社](https://bonobopress.com/)

**原文标题**: [Keeping developers up to date â Bonobo Press](https://bonobopress.com/)

Bonobo Press 是一家专注于软件开发者资讯服务的媒体公司，自 2013 年起通过每周简报为超过 88,000 名技术人员提供最新行业动态。

- 📧 提供多份面向开发者、工程经理和技术决策者的精选周报，以简洁高效著称
- 👥 覆盖 8.8 万 + 软件工程师、技术主管及 IT 决策者等垂直领域受众  
- 📢 提供广告合作机会，可通过媒体资料包了解详情并建立商业联系
- 📮 开放业务咨询通道，支持广告投放、问题反馈与合作建议

---

### [往期通讯：第 1 页](https://reactdigest.net/newsletters)

**原文标题**: [Past Newsletters: Page 1](https://reactdigest.net/newsletters)

本期 React Digest 汇总了 2025 年 5 月至 9 月的技术通讯内容，涵盖 React 生态的最新工具、性能优化和开发实践。

- 🚀 探索 TanStack DB 响应式客户端存储和 Shopify 的 React Native 迁移实践
- ⚡ 了解无框架的 React Server 组件支持和 React 19 新 Activity 组件
- 🔄 深入研究 React 并发特性及 Next.js 大规模自托管方案
- 💾 探讨缓存一致性策略和多标签 React 应用状态同步技术
- 📱 学习通过 Web Workers 提升性能及 React 密钥的深层应用
- 🛠️ 掌握 useCallback 最佳实践和自定义 Hook 开发技巧
- 🧩 深入 Zustand 状态管理和 React 模块联邦架构设计
- 📊 优化重新渲染性能及 Server Components 在 Expo 中的应用
- 🤖 实现实时手势识别和本地优先数据策略
- 🏗️ 构建稳健数据获取架构和响应式状态管理方案

---

### [隐私](https://reactdigest.net/privacy)

**原文标题**: [Privacy](https://reactdigest.net/privacy)

我们高度重视用户隐私，制定了明确的隐私政策以规范个人信息收集、使用及保护方式，确保数据处理的合法性与透明度。

- 📧 仅收集邮箱地址用于发送周刊，不作其他用途
- 🎯 信息收集前明确告知用途，严格遵循目的限定原则
- 🔒 采用合理安全措施防止数据泄露或滥用
- ⏳ 仅在必要期限内保留个人信息
- 🚫 坚决反对垃圾邮件，提供一键退订功能
- 👶 严格遵守 COPPA 法案，不收集 13 岁以下儿童信息
- 📬 支持用户通过指定邮箱查询或删除个人数据（依据英国《数据保护法》）
- 📋 公开个人信息管理政策供用户随时查阅

---

### [媒体资料包 - Bonobo 出版社](https://bonobopress.com/media-kit/)

**原文标题**: [Media Kit â Bonobo Press](https://bonobopress.com/media-kit/)

Bonobo Press 是一家专注于为程序员和技术人员提供最新趋势、工具和技术资讯的媒体平台，通过精心策划的周报吸引高度参与的专业读者，并为广告商提供精准的目标受众触达和转化机会。

- 📧 提供四类技术周报：Leadership in Tech（26,385 订阅者，57.95% 打开率）、Programming Digest（18,263 订阅者，51.83% 打开率）、C# Digest（19,724 订阅者，52.61% 打开率）和 React Digest（23,279 订阅者，47.56% 打开率）
- 🌍 读者主要来自欧美地区，涵盖不同职级的技术人员、管理者和决策者
- 💰 广告报价因周报而异，单期价格从$875 到$1,940 不等，CPC 范围$1.95-$5.83
- 📝 广告格式为纯文本，需包含链接、标题（<100 字符）和描述（<400 字符），截止日期为发布前 4 天
- 🔄 合作流程包括需求沟通、档期确认、发票支付、内容优化和效果报告
- 🤝 已有 Okta、MongoDB、Twilio 等多家知名技术公司重复投放广告

---

