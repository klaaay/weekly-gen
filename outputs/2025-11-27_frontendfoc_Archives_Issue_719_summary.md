### [前端聚焦 第 719 期：2025 年 11 月 26 日](https://frontendfoc.us/issues/719)

**原文标题**: [Frontend Focus Issue 719: November 26, 2025](https://frontendfoc.us/issues/719)

本期前端技术通讯聚焦 CSS Subgrid 布局革新、WebGPU 全面支持及多项开发工具更新，涵盖性能优化与创新设计实践。

- 🎨 CSS Subgrid 解决长期布局难题，解锁全新 UI 可能性
- 🐛 Macroscope 代码审查工具提供高精度错误检测，开源项目免费使用
- 🌐 维基百科统一移动端与桌面端域名，实现 20% 响应速度提升
- 📐 样式查询新增范围语法支持，增强响应式设计能力
- ⚡ WebGPU 获主流浏览器全面支持，提升图形计算性能
- 🛠️ overscroll-behavior 行为变更，CSS 背景模块发布新草案
- 🎬 标准化动画密钥帧系统，实现跨项目动画统一管理
- 🖼️ 利用 CSS 透视变换创建立体图像效果
- 🗺️ grid-template-areas 属性提供可视化布局解决方案
- 🚀 Driver.js v1.4 发布，提供流畅的页面导览功能
- 🔥 Heat.js 轻量级热力图库，支持主题定制与响应式设计
- 🔤 fontless 字体优化插件，有效降低布局偏移

---

### [全新 CSS 子网格布局设计 • 乔希·W·科莫](https://www.joshwcomeau.com/css/subgrid/)

**原文标题**: [Brand New Layouts with CSS Subgrid • Josh W. Comeau](https://www.joshwcomeau.com/css/subgrid/)

CSS Subgrid 是一种强大的布局工具，它允许嵌套元素继承父级网格结构，从而创建更灵活和响应式的设计。

- 🎨 **子网格基础**：通过 `grid-template-rows: subgrid` 和 `grid-template-columns: subgrid` 继承父网格的列和行定义，使嵌套元素参与同一网格布局。
- 🚀 **新布局可能**：子网格解决了兄弟元素在复杂布局中相互响应的问题，例如动态调整卡片内图像和文本列宽，实现内容自适应。
- ⚠️ **常见陷阱**：使用子网格时必须显式指定行或列的跨度（如 `grid-row: span 6`），否则内容会挤在单一单元格内。
- 🔢 **行号重置**：子网格继承模板但行号索引从 1 开始重新编号，需注意在嵌套网格中调整位置分配。
- 🌊 **流体布局限制**：子网格目前与 `auto-fill` 或 `auto-fit` 等流体网格设计不兼容，需明确指定列数。
- 🛠️ **浏览器兼容**：虽然主流浏览器已支持子网格，但使用 `@supports` 查询为旧浏览器提供备用布局（如垂直堆叠）是必要的。
- 🛠️ **开发工具**：浏览器开发者工具中的网格覆盖功能极大简化了子网格的调试和可视化过程。

---

### [子网格 - CSS | MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Subgrid)

**原文标题**: [Subgrid - CSS | MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Subgrid)

CSS Subgrid 是 CSS Grid Layout 模块中的功能，允许嵌套网格继承父网格的轨道尺寸，实现子网格与父网格的对齐。该功能于 2023 年 9 月广泛可用，支持现代浏览器。

- 🎯 **功能定义**：通过 `grid-template-columns: subgrid` 或 `grid-template-rows: subgrid` 让嵌套网格共享父网格的轨道尺寸
- 🔄 **对齐优势**：解决传统嵌套网格与父网格无法对齐的问题，子网格项目可直接基于父网格定位
- 📏 **灵活应用**：可单独应用于行或列，也可同时应用于两个维度，支持自定义间距和命名网格线
- ⚠️ **注意事项**：子网格维度会禁用隐式轨道创建，需注意内容溢出问题
- 🛠️ **开发适配**：支持覆盖父网格的间距属性，并可混合使用父网格和子网格的命名线进行定位

---

### ["子网格" | 我能用吗... HTML5、CSS3 等支持表格](https://caniuse.com/?search=subgrid)

**原文标题**: ["subgrid" | Can I use... Support tables for HTML5, CSS3, etc](https://caniuse.com/?search=subgrid)

CSS Subgrid 是 CSS 网格布局模块第二级中的一项功能，它允许具有自身网格的网格项在一个或两个维度上与其父网格对齐。

- 🎯 允许网格项与父网格对齐
- 📐 支持单维度或双维度对齐
- 💻 CSS 属性：grid-template-columns: subgrid
- 📏 CSS 属性：grid-template-rows: subgrid

---

### [乔希·W·科莫在蓝天的博客](https://bsky.app/profile/joshwcomeau.com/post/3m6hrso6kas2f)

**原文标题**: [@joshwcomeau.com on Bluesky](https://bsky.app/profile/joshwcomeau.com/post/3m6hrso6kas2f)

这是一个需要 JavaScript 的重度交互式网页应用，无法使用简单 HTML 界面操作。文章介绍了 Josh W. Comeau 新发布的关于 CSS 子网格功能的博客文章，强调该功能解决了长期存在的 CSS 布局难题。

- 🌐 需要启用 JavaScript 才能正常使用此交互式网页应用
- 📖 可通过 bsky.social 和 atproto.com 了解更多关于 Bluesky 的信息  
- 🎨 Josh W. Comeau 发布了关于 CSS 子网格功能的新技术文章
- 💡 子网格功能解决了作者长期困扰的 CSS 布局问题
- 🔗 技术文章详情请访问：https://www.joshwcomeau.com/css/subgrid/
- ⏰ 文章发布于 2025 年 11 月 25 日

---

### [Macroscope - AI 代码审查与状态更新](https://macroscope.com/?utm_medium=newsletter&utm_source=frontendfocus&utm_content=primarysponsor)

**原文标题**: [Macroscope - AI Code Review & Status Updates](https://macroscope.com/?utm_medium=newsletter&utm_source=frontendfocus&utm_content=primarysponsor)

Macroscope 是一款 AI 驱动的工程效率平台，通过自动分析代码库帮助团队提升开发效率。它能够自动生成提交摘要、代码审查、项目跟踪，并提供基于代码库的智能问答功能。

- 🔍 **智能代码分析**：通过 AST 解析构建动态知识图谱，精准检测代码问题并减少误报
- 🤖 **自动化代码审查**：自动生成 PR 描述，在合并前发现并修复 bug，支持多模型协作审查
- 📊 **项目可视化**：自动跟踪工程活动，显示时间分配、项目进展和团队贡献度
- 💬 **智能问答系统**：在 Slack 中直接提问，基于完整代码库和 git 历史提供准确答案
- ⚡ **快速集成**：10 秒内连接 GitHub，30 秒内配置 Slack，支持 Jira/Linear 等工具
- 🔒 **企业级安全**：SOC 2 Type II 认证，数据加密隔离，不使用客户代码训练模型
- 💰 **灵活定价**：团队版每位开发者 30 美元/月，开源项目免费，支持 2 周免费试用
- 🎯 **用户认可**：多家科技公司 CEO/CTO 推荐，显著提升工程团队效率和协作透明度

---

### [统一我们的移动与桌面领域 – [[WM:TECHBLOG]]](https://techblog.wikimedia.org/2025/11/21/unifying-mobile-and-desktop-domains/)

**原文标题**: [Unifying our mobile and desktop domains – [[WM:TECHBLOG]]](https://techblog.wikimedia.org/2025/11/21/unifying-mobile-and-desktop-domains/)

维基媒体工程团队通过统一移动端和桌面端域名，实现了性能提升、搜索引擎优化和基础设施负载降低。

- 🚀 移动端响应速度提升 20%，消除重定向延迟
- 🔍 Google 搜索索引量增长 140%，Commons 周浏览量翻倍
- 🌐 所有用户共享同一域名，自动适配设备版本
- ⚡ CDN 缓存清除量日均减少 40 亿次，负载降低 50%
- 🔗 历史移动端链接自动跳转标准域名，改善分享体验
- 📈 恢复因 Google 爬虫变更导致的性能衰退并实现净提升
- 🗓️ 2025 年 10 月完成全 wiki 部署，24 小时内移动域名流量趋零

---

### [una.im | 样式查询的范围语法](https://una.im/range-style-queries)

**原文标题**: [una.im | Range Syntax for Style Queries](https://una.im/range-style-queries)

样式查询新增范围语法功能，允许通过比较运算符实现动态样式匹配。

- 🌟 样式查询现支持范围匹配（>、<、>=、<=），不再局限于精确值匹配
- 🚀 适用于@container style() 查询和 CSS if() 函数，增强组件响应能力
- 🌧️ 通过天气卡片示例展示：当降雨概率>45% 时自动切换背景渐变
- 🔧 支持 attr() 函数转换数据类型，如将 data-rain-percent 属性转为百分比值
- 🎛️ 在 if() 函数中实现条件样式：根据数据列数动态切换网格背景色
- ⚡ 已於 Chrome 142 版本实现，可用于网格布局、动画效果等多样化场景

---

### [主流浏览器现已支持 WebGPU  |  Blog  |  web.dev](https://web.dev/blog/webgpu-supported-major-browsers?hl=en)

**原文标题**: [WebGPU is now supported in major browsers  |  Blog  |  web.dev](https://web.dev/blog/webgpu-supported-major-browsers?hl=en)

WebGPU 现已在主流浏览器中全面支持，为网页高性能图形计算开启新纪元。

- 🚀 WebGPU 成为新一代网页 GPU 接口标准，支持 Chrome/Edge/Firefox/Safari 等主流浏览器
- 🎮 突破 WebGL 限制，支持 AAA 级游戏、复杂 3D 建模和高级 AI 应用等高性能场景
- ⚡ 提供通用 GPU 计算能力，显著提升机器学习推理/训练、视频处理和物理模拟性能
- 🌍 由 W3C 工作组联合苹果/谷歌/英特尔/微软/ Mozilla 等企业共同开发
- 📱 支持多平台：Windows/macOS/ChromeOS（Chrome 113+）、Android 12+（Chrome 121+）、iOS/iPadOS 26+
- 🔧 集成主流开发框架：Babylon.js/Three.js/Unity/ONNX Runtime/Transformers.js等
- 💫 引入渲染包（Render Bundles）技术，部分场景渲染速度提升约 10 倍
- 🛠️ 提供 Dawn 和 wgpu 底层引擎，支持 Wasm/emscripten/Rust 等跨平台开发工具

---

### [使用 overscroll-behavior: contain 防止 dialog 打开时页面滚动 –Bram.us](https://www.bram.us/2025/11/25/use-overscroll-behavior-contain-to-prevent-a-page-from-scrolling-while-a-dialog-is-open/)


Chrome 144 版本更新后，overscroll-behavior 属性现可作用于非滚动容器，解决了模态对话框打开时底层页面滚动的问题。

- 🎯 通过设置`overscroll-behavior: contain`可阻止滚动穿透现象
- 🚀 新增对非滚动容器的支持（如设置 overflow 但无滚动内容的情况）
- 💡 实现方案：对`<dialog>`及其背景层同时应用滚动控制
- ⚙️ 关键代码需搭配`::backdrop { overflow: hidden }`创建非滚动容器
- 🌐 目前仅 Chrome 144+ 支持，其他浏览器尚未跟进此特性
- 🔧 开发者无需再使用设置 html 元素 overflow 的临时解决方案

---

### [获取失败](https://frontendfoc.us/link/177579/web)

**原文标题**: [Failed to retrieve](https://frontendfoc.us/link/177579/web)

无法总结：获取内容失败，状态码 403。

---

### [获取失败](https://frontendfoc.us/link/177580/web)

**原文标题**: [Failed to retrieve](https://frontendfoc.us/link/177580/web)

无法总结：获取内容失败，状态码 403。

---

### [DOCTYPE 杂志 🚀⌨️](https://vole.wtf/doctype/)

**原文标题**: [DOCTYPE magazine 🚀⌨️](https://vole.wtf/doctype/)

这是一本复古风格的 HTML 代码输入杂志，内含 10 款网页应用，无需编程基础即可通过手动输入代码获得互动体验。

- 📚 杂志包含 10 个网页应用清单（游戏/工具/谜题等）
- ⌨️ 采用 80 年代手动输入代码的复古交互形式
- 🎨 内含精美插画与彩色光面封面
- 💻 本地文件直接运行，无需服务器
- 🚫 仅提供实体杂志，无电子版
- 👨‍💻 由多位开发者共同贡献代码
- 🛒 通过 Lulu 平台独家销售

---

### [说“CSS 变量”而非（或同时使用）“自定义属性”也无妨——罗马的未打磨文章](https://blog.kizu.dev/css-variables/)

**原文标题**: [It is OK to Say “CSS Variables” Instead of (or Alongside) “Custom Properties” — Roma’s Unpolished Posts](https://blog.kizu.dev/css-variables/)

本文讨论了在 CSS 中使用"CSS 变量"这一术语的合理性，强调其与"自定义属性"的等价性，并指出官方文档和实际特性都支持这种表述。

- 🎯 官方 CSS 模块名称为"CSS Custom Properties for Cascading Variables"，URL 中包含 css-variables
- 🔄 CSS 变量具有级联特性，值会随规则匹配动态覆盖更新
- 🌊 支持响应式动画，可根据视口/容器等条件动态变化数值
- 📝 通过@property 可显式定义类型，增强类型安全性
- 💻 强调 CSS 与 HTML 同属编程语言范畴的立场
- ✍️ 作者在 TPAC 2025 会议后处于疲惫但灵感迸发的创作状态

---

### [关于继承与共享属性值 | CSS 技巧](https://css-tricks.com/on-inheriting-and-sharing-property-values/)

**原文标题**: [On Inheriting and Sharing Property Values | CSS-Tricks](https://css-tricks.com/on-inheriting-and-sharing-property-values/)

本文探讨了在 CSS 中获取其他属性值的现有方法和未来可能性，重点介绍了通过自定义属性、CSS 函数和单位实现属性值复用的技术方案。

- 🎯 目前 CSS 缺乏直接获取其他属性值的通用函数，但可通过自定义属性配合 calc() 实现动态计算
- 🔮 未来可能引入 inherit() 函数，支持获取父元素任意属性值并进行数学运算
- 📐 aspect-ratio 属性可建立宽高比例关系，无需知道具体数值
- 🎨 currentColor 关键字可复用 color 属性值，适用于所有颜色相关属性
- 📏 字体相关单位 (ex/ch/lh 等) 和视口单位 (vw/vh) 提供相对尺寸控制
- 📦 容器查询单位 (cqw/cqh) 允许在容器上下文中使用相对尺寸
- 💡 作者建议未来增加 compute() 函数或更多 currentColor 式关键字来简化属性值复用

---

### [关键帧令牌：跨项目动画标准化 — Smashing Magazine](https://www.smashingmagazine.com/2025/11/keyframes-tokens-standardizing-animation-across-projects/)

**原文标题**: [Keyframes Tokens: Standardizing Animation Across Projects — Smashing Magazine](https://www.smashingmagazine.com/2025/11/keyframes-tokens-standardizing-animation-across-projects/)

本文介绍了通过创建统一的关键帧令牌系统来标准化和管理 CSS 动画的方法，解决项目中动画重复定义和全局作用域冲突的问题。

- 🎯 **问题根源**：项目中常存在多个相同动画的关键帧重复定义，导致代码冗余和维护困难
- 🌍 **全局冲突**：CSS 关键帧始终处于全局作用域，同名动画会被覆盖，造成不可预测的行为
- 🛠️ **解决方案**：建立统一的关键帧令牌文件，使用 kf-前缀命名空间避免冲突
- 🎨 **动态定制**：通过 CSS 自定义属性实现动画参数动态调整，如方向、大小等
- 🔄 **动画组合**：支持多个动画组合使用，通过 animation-composition 属性处理相同属性冲突
- ♿ **无障碍支持**：内置减少动画偏好支持，提供即时显示和柔和动画替代方案
- 📝 **最佳实践**：逐步采用、统一命名、完善文档、保持灵活性、考虑无障碍性
- 💡 **核心价值**：将动画从杂乱无章的技巧转变为可预测的设计系统，提升产品一致性和用户体验

---

### [Next.js 企业级样板](https://blazity.com/open-source/nextjs-enterprise-boilerplate)

**原文标题**: [Next.js Enterprise Boilerplate](https://blazity.com/open-source/nextjs-enterprise-boilerplate)

该网站展示了一个专注于 Next.js 企业级解决方案的技术服务公司，提供全栈开发工具、性能优化服务和专业咨询。

- 💼 提供企业级 Next.js 样板项目，集成 Tailwind CSS/TypeScript等现代化工具链
- 🛒 推出高性能电商前端解决方案，支持 Shopify 和 Algolia 集成
- 📚 发布 Next.js 性能优化电子书，涵盖核心网页指标优化策略
- 🚀 预置完整 AWS 基础设施方案，包含 Terraform 和 CI/CD 流水线
- 🧪 配备完整测试套件，支持 Jest/Playwright 等多种测试方案
- 🎨 集成 Storybook 和 Radix UI，提供组件化开发体验
- 📊 内置性能监控工具，支持 OpenTelemetry 和 Lighthouse 评分
- 🔄 支持多种渲染模式，包括 SSR、SSG 和增量静态再生
- 🔧 提供技术审计、团队培训和咨询等专业服务
- 📈 即将推出高级部署方案，包含 WAF 防护和缓存优化

---

### [如何在 CSS 中使用分层模式创建 3D 图像 – Frontend Masters 博客](https://frontendmasters.com/blog/how-to-create-3d-images-in-css-with-the-layered-pattern/)

**原文标题**: [How to Create 3D Images in CSS with the Layered Pattern – Frontend Masters Blog](https://frontendmasters.com/blog/how-to-create-3d-images-in-css-with-the-layered-pattern/)

本文介绍了使用 CSS 分层模式创建 3D 图像的技术，通过堆叠多个图像层并调整 Z 轴位置和颜色来营造立体视觉效果。

- 🎨 3D CSS 技术已有 15 年历史，分层模式通过堆叠元素并调整 Z 轴位置创造立体错觉
- 🖼️ 可将分层模式应用于图像，通过重复图像层并设置不同 Z 轴位移实现 3D 效果
- ⚙️ 关键技术点：设置 CSS 透视视角、理解 3D 坐标系、使用 transform-style: preserve-3d
- ♿ 需注意可访问性问题，通过设置 aria-hidden="true"隐藏重复内容
- 📐 核心实现：计算每层 translateZ 位移值，使用滤镜调整亮度和饱和度
- 🎮 可添加交互控制功能，实时调整透视距离、层偏移和旋转角度
- 🔄 通过 JavaScript 实现动态控制，支持切换不同图像和实时参数调整
- 🥩 该技术可扩展应用，如创建 3D 牛排等复杂视觉效果

---

### [网格：grid-template-areas 如何为代码提供可视化解决方案 | WebKit](https://webkit.org/blog/17620/grid-how-grid-template-areas-offer-a-visual-solution-for-your-code/)

**原文标题**: [  Grid: how grid-template-areas offer a visual solution for your code | WebKit](https://webkit.org/blog/17620/grid-how-grid-template-areas-offer-a-visual-solution-for-your-code/)

grid-template-areas 提供了一种通过视觉化命名和布局网格元素的方法，使代码更直观且易于调整。

- 🎨 通过为每个元素分配 grid-area 名称，实现视觉化布局
- 📐 使用 grid-template-areas 属性在单个属性中定义整个网格布局
- 🔄 相比基于网格线的布局方式，更直观且易于修改
- 📱 示例中实现了跨行跨列的复杂布局需求
- ⚡ 需要前期命名工作，但后期维护和调整更简单
- 💡 布局调整只需移动元素名称到不同"单元格"即可完成

---

### [网页浏览器状态栏的设计令人费解。](https://lapcatsoftware.com/articles/2025/11/4.html)

**原文标题**: [Web browser status bars are nuts](https://lapcatsoftware.com/articles/2025/11/4.html)

主要浏览器在状态栏和地址栏中显示 URL 方案时存在不一致且令人困惑的行为。

- 🔍 Safari 状态栏显示完整 HTTPS 链接但省略 HTTP 方案，而地址栏默认隐藏 HTTPS 方案
- 🌐 Chrome 状态栏行为与 Safari 相同，地址栏可通过设置显示完整 URL
- 🦊 Firefox 状态栏显示完整 HTTP 链接但省略 HTTPS 方案，地址栏用锁图标代替 HTTPS 方案
- ⚠️ 三大浏览器在 URL 方案显示上互相矛盾且各自存在内部不一致
- 🚫 浏览器厂商试图逐步取消 URL 方案显示的做法缺乏统一规划且用户体验混乱

---

### [网页货币化仍在缓慢推进，但依然困难重重——Frontend Masters 博客](https://frontendmasters.com/blog/web-monetization-is-still-inching-along-but-still-too-difficult/)

**原文标题**: [Web Monetization is Still Inching Along, But Still Too Difficult – Frontend Masters Blog](https://frontendmasters.com/blog/web-monetization-is-still-inching-along-but-still-too-difficult/)

作者回顾了 Web Monetization 的发展历程，表达了对浏览器原生集成该功能的期待，但通过实际体验指出当前支付流程仍存在诸多障碍。

- 🕸️ Coil 通过浏览器扩展实现网站微支付，用户可自动打赏支持的内容创作者
- 🌐 作者更期待该技术成为 Web 标准并内置到浏览器中，无需安装扩展
- 💳 理想中的支付系统应具备：操作便捷如 Apple Pay、支付安全、支持匿名订阅、兼容多种支付方式
- 🔄 Coil 关闭后将技术移交 Interledger 基金会，Chromium 已开始原生支持实验
- 🚫 实际测试遇到问题：GateHub 钱包地址格式不符、无法存入美元、地区限制（美国不支持 Interledger 钱包）
- 📱 其他钱包选项存在平台限制（如 Chimoney 仅支持原生应用）
- 💡 作者认为需先完善用户体验，再推进开发者生态和标准制定
- 💬 文末评论区提供了部分技术问题的解决方案，但地区限制问题依然存在

---

### [如何使用 GSAP 打造电影级 3D 滚动体验 | Codrops](https://tympanus.net/codrops/2025/11/19/how-to-build-cinematic-3d-scroll-experiences-with-gsap/)

**原文标题**: [How to Build Cinematic 3D Scroll Experiences with GSAP | Codrops](https://tympanus.net/codrops/2025/11/19/how-to-build-cinematic-3d-scroll-experiences-with-gsap/)

本教程介绍如何使用 GSAP、WebGL 和 Three.js 构建电影级 3D 滚动交互体验，通过滚动控制实现摄像机运动、粒子效果和动态排版。

- 🎬 通过 GSAP 连接滚动与 3D 场景，实现摄像机路径、光照和着色器效果的同步控制
- ⚙️ 配置 ScrollTrigger 和 ScrollSmoother 插件，创建自定义缓动曲线控制视觉节奏
- 🌀 构建圆柱形 WebGL 场景，使用图像图集实现无缝图像切换和粒子环绕效果
- 📜 设置 500vh 滚动容器，通过时间轴动画实现摄像机多段位移动画
- ✨ 添加响应式粒子系统，根据圆柱旋转速度动态调整透明度和运动轨迹
- 🖋️ 使用 SplitText 实现文字字符级动画，与滚动进度精准同步
- 🎮 在 Three.js 场景中实现可交互的赛博朋克建筑，配合雾效和动态灯光
- 📊 创建进度指示器和滚动提示界面，通过 quickSetter 高效更新 UI 状态
- 🎯 将滚动视为导演工具，通过时序控制和缓动函数营造电影级叙事节奏

---

### [容器溢出时更新 CSS 圆角边框 - PQINA](https://pqina.nl/blog/update-container-border-radius-scrollbar-overflow/)

**原文标题**: [Updating CSS Border Radius When A Container Is Overflowing - PQINA](https://pqina.nl/blog/update-container-border-radius-scrollbar-overflow/)

本文介绍了一种使用纯 CSS 检测容器内容溢出并动态调整边框圆角的方法。

- 🎯 通过 CSS 动画和自定义属性检测水平和垂直方向溢出
- ⚙️ 利用`--overflows-x`和`--overflows-y`变量记录溢出状态（0 或 1）
- 📐 根据溢出情况动态计算四个角的边框圆角值
- 🧩 使用`max()`函数确保任一方向溢出时都能降低圆角
- 🌐 目前仅支持 Chrome 和 Safari 浏览器
- 📱 提供四种溢出场景演示：无滚动条、垂直滚动、水平滚动、双向滚动
- 🔧 通过`@supports`规则确保渐进增强，提供回退样式

---

### [CloudFlare 服务中断事件实为幸事 · GitHub](https://gist.github.com/jbreckmckye/32587f2907e473dd06d68b0362fb0048)

**原文标题**: [The CloudFlare outage was a good thing · GitHub](https://gist.github.com/jbreckmckye/32587f2907e473dd06d68b0362fb0048)

CloudFlare 服务中断事件揭示了互联网过度中心化的风险，并提醒我们应建立冗余系统以增强社会韧性。

- 🌐 互联网服务过度依赖少数提供商（如 CloudFlare、AWS），形成系统性脆弱点
- ⚡ 本次中断由配置文件错误触发级联故障，暴露单点失效风险
- 🏦 数字基础设施已渗透生活各领域（支付、交通、医疗），中断可能引发连锁反应
- 🚨 类比新冠疫情对供应链的冲击，需在效率与韧性间取得平衡
- 🔄 评论建议采用多供应商策略、冷备份方案和解耦系统架构
- 💡 应像应对疫情那样，为数字系统建立弹性机制和离线备选方案
- 🌱 推动去中心化架构和自建服务，避免“数字香蕉灭绝”式危机

---

### [AI 时代的关键思考——艾迪·奥斯马尼著](https://addyo.substack.com/p/critical-thinking-during-the-age)

**原文标题**: [Critical Thinking during the age of AI - by Addy Osmani](https://addyo.substack.com/p/critical-thinking-during-the-age)

在 AI 时代，人类批判性思维的重要性愈发凸显。本文通过"谁、何事、何地、何时、为何、如何"框架，为技术团队提供系统性思考指南，强调在 AI 辅助开发中保持独立判断和证据导向的决策方式。

- 👥 明确参与者：识别相关利益方并纳入多元视角，避免群体思维，对 AI 输出保持验证态度
- 🎯 定义真问题：避免解决表面症状，通过证据收集确认核心问题，像科学家般检验假设
- 🌍 关注上下文：考虑解决方案的运行环境和使用场景，预判可能产生的连锁影响
- ⏰ 把握时机：区分紧急修复与深度分析，在时间压力下保持关键决策的严谨性
- ❓ 追溯根源：运用"五个为什么"方法挖掘根本原因，警惕确认偏误和贸然下结论
- 🔍 系统化实践：采用科学方法验证证据，用数据支撑沟通，建立持续改进的思考习惯

---

### [driver.js](https://driverjs.com/)

**原文标题**: [driver.js](https://driverjs.com/)

driver.js 是一个轻量级 JavaScript 库，用于创建产品导览、高亮显示和上下文帮助，引导用户了解产品功能。

- 🚀 提供产品导览功能，支持动画/非动画演示、异步操作和进度显示
- 🎯 具备高亮显示能力，可搭配弹出框使用，支持自定义覆盖层颜色和定位
- ⚙️ 拥有丰富 API 和钩子函数，支持防止意外关闭等自定义功能
- 👥 适用于用户引导、消除干扰、上下文帮助和功能推广等多种场景
- 🌍 作为 MIT 开源项目，已获得 2.5 万 GitHub 星标，被全球数千家企业使用

---

### [将静态站点部署到任意云端](https://www.cloud66.com/products/static-sites/)

**原文标题**: [Deploy Static Sites to Any Cloud](https://www.cloud66.com/products/static-sites/)

Cloud 66 静态站点服务平台支持用户将静态网站部署到任意支持 S3 兼容存储的云平台，通过自带存储和 CDN 实现成本节约与完整控制。

- ☁️ 支持任意 S3 兼容云存储，可将静态资源上传至自选云服务商
- 🌐 兼容所有 CDN 服务，可灵活配置内容分发网络
- 💰 结合自有存储可节省最高 40% 的静态站点成本
- 🛠️ 支持主流静态站点生成器（Jekyll/Hugo/Gatsby 等）和自定义构建流程
- 🚦 提供精细化流量控制，支持基于地理位置、设备类型的访问规则
- 📊 实时监控站点流量，完整记录请求来源与状态信息
- 🔒 自动管理 SSL 证书，支持预览部署和密钥管理
- 🌍 已支持 AWS/GCP/Azure/DigitalOcean/Hetzner 等主流云平台

---

### [GitHub - aniftyco/awesome-tailwindcss: 😎 关于 Tailwind CSS 的超赞资源合集](https://github.com/aniftyco/awesome-tailwindcss)

**原文标题**: [GitHub - aniftyco/awesome-tailwindcss: 😎 Awesome things related to Tailwind CSS](https://github.com/aniftyco/awesome-tailwindcss)

这是一个关于 Tailwind CSS 资源的 GitHub 仓库集合，收录了与 Tailwind CSS 相关的工具、组件库和插件等优质内容。

- 📚 官方资源：包含 Tailwind CSS 官网、代码仓库、UI 套件和无样式组件库等核心资源
- 🔧 开发工具：提供代码智能提示、颜色生成器、类名排序等辅助开发工具
- 🎨 UI 组件库：收录 Tailwind UI、Headless UI、shadcn/ui 等多个流行的 UI 组件库和模板
- 🧩 功能插件：包含官方和社区的各类插件，如排版美化、表单样式、主题定制等
- 🌟 社区活跃：获得 14.7k 星标和 991 次分叉，由 337 位贡献者共同维护
- 📄 开放许可：采用 CC0-1.0 许可证，鼓励自由使用和贡献
- 🔄 持续更新：仓库保持活跃更新，欢迎社区贡献新资源

---

### [GitHub - annoyingmouse/wc-pagination](https://github.com/annoyingmouse/wc-pagination)

**原文标题**: [GitHub - annoyingmouse/wc-pagination](https://github.com/annoyingmouse/wc-pagination)

这是一个名为 wc-pagination 的开源 Web 组件项目，用于创建分页元素，采用 MIT 许可证。

- 📄 **项目简介** - 提供可访问的分页 Web 组件，支持自定义配置
- ⚙️ **配置参数** - 通过 total（总记录数）、current（当前页码）和 page-size（每页记录数）三个属性进行配置
- 🌐 **演示地址** - 可在 CodePen 上查看组件演示效果
- ♿ **可访问性** - 已添加多项无障碍功能，持续优化中
- 📜 **许可证** - 采用 MIT 开源许可证
- 📊 **项目数据** - 获得 5 个星标，1 个分支，包含 13 个版本发布
- 💻 **技术栈** - 主要使用 HTML（56.2%）、JavaScript（34.4%）和 CSS（9.4%）开发

---

### [获取失败](https://frontendfoc.us/link/177598/web)

**原文标题**: [Failed to retrieve](https://frontendfoc.us/link/177598/web)

无法总结：获取内容失败，状态码 403。

---

### [Heat.js - JavaScript 热力图](https://www.william-troup.com/heat-js/)

**原文标题**: [Heat.js - JavaScript Heat Map](https://www.william-troup.com/heat-js/)

这是一个开源数据可视化工具的功能介绍，主要特点包括免费开源、多语言支持和丰富的数据处理功能。

- 🆓 免费开源（MIT 许可证）且零依赖
- ⚡ 基于 TypeScript 开发，完美支持 React 和 Angular 等框架
- 🌍 默认支持 51 种语言，可自定义文本翻译
- 📊 提供地图、图表、日期和统计四种视图模式
- ⚙️ 每个视图都支持独立配置对话框
- 📈 支持趋势类型数据拆分和切换器功能
- 💾 支持 CSV/JSON/XML/TXT 格式数据导入导出
- 🎨 提供 12 种主题（支持深色/浅色模式）
- 🔄 支持数据拉取功能（不含趋势类型）
- 🏗️ 网站核心功能已完成，将持续更新示例和文档

---

### [Heat.js | 示例 | 按钮](https://www.william-troup.com/heat-js/examples/buttons.html)

**原文标题**: [Heat.js | Example | Buttons](https://www.william-troup.com/heat-js/examples/buttons.html)

网页开发基础示例
- 🌐 页面源代码展示
- 💻 核心编程结构
- 📄 超文本标记语言实例
- 🔍 可查看原始代码实现
- 🛠️ 开发技术参考范例

---

### [GitHub - williamtroup/Heat.js：🌞 轻量级 JavaScript 库，用于生成可自定义的热图、图表和统计数据，以可视化基于日期的活动与趋势。](https://github.com/williamtroup/Heat.js)

**原文标题**: [GitHub - williamtroup/Heat.js: 🌞 A lightweight JavaScript library that generates customizable heat maps, charts, and statistics to visualize date-based activity and trends.](https://github.com/williamtroup/Heat.js)

Heat.js 是一个轻量级 JavaScript 库，用于生成可自定义的热图、图表和统计数据，以可视化基于日期的活动与趋势。

- 🌞 轻量级无依赖的 JavaScript 库，支持热图、图表和统计数据可视化
- 📊 提供四种视图模式：地图、图表、日期和统计，支持数据导入/导出
- 🎨 完全可定制样式，支持 CSS 主题和暗黑/明亮模式，兼容 Bootstrap
- 🌍 支持 51 种语言翻译，适配所有现代浏览器
- ⚙️ 基于 TypeScript 开发，提供完整 API 和配置选项
- 📦 可通过 npm 安装或 CDN 引用，当前版本 v4.4.0
- 📄 采用 MIT 开源协议，拥有 728 个星标和 16 个分支

---

### [Polypane 27：项目集锦、片段面板与 Chromium 142 | Polypane](https://polypane.app/blog/polypane-27-projects-a-snippets-panel-and-chromium-142/)

**原文标题**: [Polypane 27: Projects, a Snippets Panel and Chromium 142 | Polypane](https://polypane.app/blog/polypane-27-projects-a-snippets-panel-and-chromium-142/)

Polypane 27 版本引入了项目工作流、代码片段面板、增强的 DOM 编辑功能，并基于 Chromium 142 构建，全面提升开发效率。

- 🗂️ 新增项目功能，可分组管理标签页、书签和会话设置
- 💾 代码片段面板支持保存和运行 CSS/JavaScript 代码块
- 🎨 元素面板新增行号显示、元素复制删除和强制起始样式功能
- 🐛 新增视图过渡减速和强制悬停样式调试工具
- 🌐 支持 Punycode 国际化域名显示
- 📥 下载操作增加开始/结束/错误状态通知
- 🔧 修复 Widevine DRM 启动阻塞和 Windows 页面缩放快捷键失效问题
- ⚡ 底层升级至 Chromium 142 并优化全局性能

---

### [获取失败](https://frontendfoc.us/link/177602/web)

**原文标题**: [Failed to retrieve](https://frontendfoc.us/link/177602/web)

无法总结：获取内容失败，状态码 403。

---

### [弗兰无衬线体随笔 — 艾米莉·斯内登](https://emilysneddon.com/fran-sans-essay)

**原文标题**: [Fran Sans Essay — Emily Sneddon](https://emilysneddon.com/fran-sans-essay)

本文介绍了设计师 Emily Sneddon 受旧金山轻轨车辆目的地显示屏启发创作 Fran Sans 字体的过程，探讨了城市公共设施中实用性与独特魅力的共生关系。

- 🚋 字体灵感源自旧金山 Muni 轻轨的 Breda 车辆 LCD 显示屏，其 3×5 网格构成的几何模块字母兼具机械感与人文温度
- 🎨 设计师通过探访 SFMTA 车间发现，这些由 Trans-Lite 公司 1999 年制造的显示屏采用分段照明原理，仅包含实际所需字符
- 🔤 Fran Sans 字体保留原显示屏的非常规特征：粗斜线的 N/0、细斜线的 Z/7，并提供 Solid/Tile/Panel 三种渐增复杂度的样式
- 📚 创作过程受到 Bell Shakespeare 剧团字体 Hotspur 的多功能启发，并在 Letterform 档案馆研习了 Tipo Veloz、Lo-Res 等模块化字体遗产
- 🌉 字体设计呼应旧金山城市特质：金门大桥防锈漆成为标志色、彩绘女士建筑群等案例体现实用向美学的转化
- ⏳ 随着 2025 年底 Breda 车辆退役，原装显示屏将被 LED 点阵取代，字体成为城市记忆的保存载体
- ✨ 项目强调在效率至上的时代保留不完美带来的独特魅力，倡导关注日常环境中的设计诗意

---

### [非 HTML 内容](https://frontendfoc.us/open/719/*%7CUID%7C*?ipx=t)

**原文标题**: [Non-HTML content](https://frontendfoc.us/open/719/*%7CUID%7C*?ipx=t)

无法总结：非 HTML 内容。

---

