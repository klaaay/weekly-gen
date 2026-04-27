### [发布 · maizzle/framework · GitHub](https://github.com/maizzle/framework/releases?ref=tailwindweekly.com)

**原文标题**: [Releases · maizzle/framework · GitHub](https://github.com/maizzle/framework/releases?ref=tailwindweekly.com)

这是一个邮件框架 Maizzle 框架的版本发布记录，主要介绍了 v6.0.0-rc.14 到 v6.0.0-rc.5 的新功能、改进和修复。

- 🌙 **新增深色模式模拟器**：通过命令对话框（Ctrl/Cmd+K）可模拟邮件客户端在深色模式下反转颜色的效果，但注意与实际客户端的算法可能不完全一致。
- 🅰️ **新增 `<Font>` 组件**：可轻松引入 Google Fonts、Bunny Fonts 或自定义 URL 的网页字体，并自动添加到 `<head>` 中，支持 IDE 自动补全。
- 🧱 **更新布局组件**：Container、Section、Row、Column 组件现在完全支持 Tailwind 工具类，内部自动处理，使用更直观。
- ✅ **统一并改进检查功能**：合并了兼容性和 Linter 标签，支持自定义检查的邮件客户端（如 Outlook、Gmail），并可完全禁用检查。
- 🔥 **新增“跳转到编辑器”功能**：点击错误或警告可直接在默认代码编辑器中打开对应文件并定位到具体行。
- 🏷️ **新增 `raw` 和 `embed` 属性**：`raw` 属性可让特定 `<style>` 标签跳过 Tailwind 编译；`embed` 属性可让内联器跳过该标签。
- 🚫 **移除截图功能**：因维护成本高且收益有限，建议使用操作系统自带的截图工具。
- ✉️ **新增发送测试邮件功能**：在开发界面底部新增“Test”标签，可配置 SMTP 发送真实测试邮件，默认使用 Ethereal 服务。
- ⚡ **新增更多命令**：命令面板支持截图、复制代码到剪贴板，以及快速访问 Maizzle 文档和 Can I Email。
- 📝 **新增 `<Markdown>` 组件**：可直接渲染 Markdown 内容或通过 `src` 属性引入外部 .md 文件。
- 🧩 **新增骨架组件和布局组件**：包括 `<Html>`、`<Head>`、`<Body>` 以及 `<Container>`、`<Row>`、`<Column>`，简化邮件布局创建。
- 🖼️ **新增 `<Image>` 组件**：支持深色模式图片切换（通过 `<picture>` 元素）和 `prefers-reduced-motion` 偏好。
- 🔄 **新增 `<Overlap>` 组件**：方便在一个元素上叠加另一个元素。
- 📏 **更新 `<Spacer>` 组件**：现在支持水平间距。
- 🔧 **新增 Liquid 风格过滤器**：通过属性实现，已从 Maizzle 5 移植。
- 📡 **支持 `<Teleport>`**：可在 HTML 中任意位置推送内容。
- 💻 **新增代码组件**：`<CodeBlock>` 和 `<CodeInline>` 用于生成邮件优化、语法高亮的代码块。
- 👁️ **新增 `<Preview>` 组件和 `usePreviewText` 组合式函数**：用于定义邮件预览/预头文本。
- 🔄 **自动处理自闭合标签**：根据文档类型自动添加或省略斜杠。
- 🐛 **修复多项问题**：包括 Tailwind 工具类生成、CSS `calc()` 值处理、开发时预览更新等。

---

### [使用 Tailwind CSS v4 提升技能](https://shrutibalasa.gumroad.com/l/level-up-with-tailwind-css?ref=tailwindweekly.com)

**原文标题**: [Level up with Tailwind CSS v4](https://shrutibalasa.gumroad.com/l/level-up-with-tailwind-css?ref=tailwindweekly.com)

概述摘要  
- 📚 本文探讨了人工智能在医疗领域的应用，强调其提升诊断准确性和效率的潜力。  
- 🩺 通过分析大量医疗数据，AI 能辅助医生识别疾病模式，尤其擅长影像诊断。  
- ⚠️ 同时指出挑战，包括数据隐私、算法偏见及监管框架的缺失。  
- 💡 建议加强跨学科合作，确保 AI 工具的安全性与公平性。  
- 🌍 未来展望中，AI 有望实现个性化治疗和远程医疗的普及。

---

### [JavaScript 须知（2026 版）——前端大师博客](https://frontendmasters.com/blog/what-to-know-in-javascript-2026-edition/?ref=tailwindweekly.com)

**原文标题**: [What To Know in JavaScript (2026 Edition) – Frontend Masters Blog](https://frontendmasters.com/blog/what-to-know-in-javascript-2026-edition/?ref=tailwindweekly.com)

JavaScript 2026 年重要更新概览

- 🆕 **ECMAScript 2025 新特性**：新增迭代器辅助方法（如 `.map()`、`.filter()`、`.take()`），支持惰性求值，减少内存占用；Set 新增交集、并集、差集等方法；正则表达式新增 `RegExp.escape()` 和分组内联标志；`Promise.try()` 统一处理同步和异步错误；支持 JSON 和 CSS 的导入属性。

- 🗓️ **ECMAScript 2026 即将推出**：Temporal API 让日期时间处理更简单准确，无需第三方库；`using` 关键字实现资源自动清理；`Array.fromAsync` 和 `Iterator.concat` 支持异步迭代和惰性求值；`Error.isError()` 可靠检测错误对象；`Math.sumPrecise` 提升浮点数精度；新增 Base64 和十六进制编码方法。

- ⚛️ **React 生态**：React 19 引入 RSC（React 服务器组件）、服务器操作和编译器；React Native 接近 1.0 版本；但服务器相关技术曾出现严重安全漏洞。

- 🖖 **Vue 生态**：Vue 3.6 进入 alpha 阶段，新增 Vapor 模式提升性能；Nuxt 4.0 发布；VoidZero 公司整合 Vite+ 工具链，涵盖构建、格式化、测试等；Pinia v3 成为主流状态管理库。

- 🌀 **Svelte 生态**：Svelte 5 采用 Runes API 实现更精细的响应式，性能更高效；SvelteKit 与 Vercel 深度整合。

- 🚀 **JavaScript 运行时**：Node.js 原生支持 TypeScript 文件运行（无需标志）；Bun 1.3 提供快速开发服务器，被 Anthropic 收购；Deno v2 以安全性和稳定性著称，默认权限受限。

- 🛠️ **构建工具**：Vite v8 改用自研 Rolldown 打包器，推出 Vite+ 统一工具链；Turbopack 成为 Next.js 默认打包器，速度提升 5-10 倍；webpack 计划简化配置。

- 📝 **TypeScript**：v6 默认启用严格模式，v7 将改用 Go 编译器，速度提升约 10 倍；TypeScript 成为 GitHub 第一语言，AI 辅助编码普及率达 92%。

- 🧪 **测试框架**：Vitest 因与 Vite 集成而流行，支持浏览器模式；Playwright 在端到端测试中超越 Puppeteer 和 Cypress。

- 🌐 **元框架**：Next.js v16 默认使用 Turbopack；Remix 转向 React Router v7，未来将脱离 React；TanStack 推出独立框架；Astro 6.0 被 Cloudflare 收购，适合静态优先站点；npm 面临供应链安全挑战，建议使用 Socket 等工具防护。

- 📚 **学习建议**：掌握基础技能比追逐框架更重要，AI 辅助编码时代更需要理解原理的开发者。

---

### [使用 JavaScript 预加载图片的选项 | Alex MacArthur](https://macarthur.me/posts/preloading-images/?ref=tailwindweekly.com)

**原文标题**: [Your options for preloading images with JavaScript | Alex MacArthur](https://macarthur.me/posts/preloading-images/?ref=tailwindweekly.com)

本文介绍了使用 JavaScript 预加载图片的多种方法及其适用场景，并讨论了各自的优缺点。

- 📸 **new Image()**：经典方法，通过创建 Image 对象并设置 src 触发下载，可监听加载完成事件，但依赖 HTTP 缓存，若服务器设置`no-store`则无法缓存。
- 🔗 **<link rel="preload" />**：通过注入预加载标签，绕过 HTTP 缓存使用专用预加载缓存，即使服务器禁止缓存也能可靠工作，且浏览器会智能合并请求。
- 🚫 **隐藏 div + CSS 背景图**：通过隐藏元素触发请求，但需注意`display:none`会阻止下载，且优先级自动设为高。
- 🗃️ **Cache API**：提供精细控制，支持 Promise 确保加载顺序，但需手动管理缓存清理，否则会持续占用空间。
- 🌐 **fetch()**：类似 Cache API 但无需管理缓存，适合临时内存使用，但同样受`Cache-Control`头影响。
- ✅ **推荐选择**：`new Image()`适合需要加载回调的场景；`<link rel="preload" />`最可靠；Cache API 适合长期存储；`fetch()`适合短期使用；隐藏 div 方法不推荐。

---

### [过早的断点](https://ishadeed.com/article/too-early-breakpoint/?ref=tailwindweekly.com)

**原文标题**: [The Too Early Breakpoint](https://ishadeed.com/article/too-early-breakpoint/?ref=tailwindweekly.com)

一项新研究揭示了晨间锻炼的诸多益处，强调其对身心健康和日常效率的积极影响。

- 🕐 晨练能显著提升全天的新陈代谢率，帮助更高效地燃烧卡路里
- 🧠 早晨运动可增强大脑认知功能，改善专注力与决策能力
- 😊 晨间锻炼有助于释放内啡肽，提升情绪并减轻压力水平
- 💪 规律晨练能强化心血管健康，降低慢性疾病风险
- ⏰ 早起运动可建立更规律的作息，优化睡眠质量与生物钟

---

### [AI 驱动的支持团队帮助台 | There There](https://there-there.app/?ref=tailwindweekly.com)

**原文标题**: [AI-powered helpdesk for support teams | There There](https://there-there.app/?ref=tailwindweekly.com)

### 概述总结
一个以 AI 为核心的帮助台，旨在提升客服团队的响应速度与回复质量，由一支每天亲自处理客服的团队打造。

- 🤖 **AI 驱动的核心**：从第一天起就以 AI 为核心构建，自动向量化所有工单，AI 能理解上下文并基于团队工作方式生成回复草稿。
- 🔍 **语义搜索**：支持按含义而非关键词搜索，可跨工单、文档和团队知识库即时查找结果。
- 📝 **自动摘要与标题**：AI 自动为对话生成清晰标题和问题摘要，工单列表一目了然，且会随对话更新。
- 🗂️ **自定义侧边栏**：可连接外部系统（如账户状态、订阅详情），在对话旁直接显示客户上下文，无需切换标签页。
- 💬 **完整对话视图**：客户消息、团队回复、转发邮件和内部备注按时间线排列，旧消息自动折叠，可随时展开。
- 🧠 **AI 历史记忆**：支持提问“上次怎么解决的？”，AI 能从过往工单、文档和团队经验中提取答案，并连接外部工具（如错误追踪器）。
- 🎨 **自定义视图**：可按渠道、标签、负责人等过滤工单，保存为个人或团队共享视图，支持固定常用视图。
- ⚡ **实时界面**：快速、专注且简洁，新工单、回复和更新即时显示，无需刷新。
- 📚 **文档自动索引**：提供文档 URL 后，AI 自动抓取并分块索引，支持按含义搜索。
- 🔗 **MCP 集成**：通过模型上下文协议连接外部工具（如 Flare 错误追踪、Oh Dear 监控），AI 可直接获取上下文。
- 🤖 **自动化工作流**：可自动分配账单工单、标记错误报告、发送确认回复，处理流程让团队专注对话。
- 🗣️ **AI 可执行操作**：支持用自然语言让 AI 分配工单、添加标签、关闭对话或留下内部备注。
- 🛡️ **欧盟数据合规**：所有数据存储在芬兰 UpCloud，完全符合 GDPR，数据不离开欧盟。
- 🏢 **由 Spatie 团队打造**：来自比利时的团队，自身每天处理大量客服，产品基于真实客服经验设计。
- 🎯 **Beta 阶段**：提供完整产品访问权限，包括 AI 功能、工作流和集成，团队会积极听取反馈。

---

### [星风 UI](https://starwind.dev/?ref=tailwindweekly.com)

**原文标题**: [Starwind UI](https://starwind.dev/?ref=tailwindweekly.com)

概述总结
- 🚀 Starwind UI 可助您在创纪录时间内创建动画网站
- 🎨 提供 45+ 个动画、可定制且无障碍的 Astro 组件，使用 Astro 和原生 JS 构建
- ⚙️ 通过 CLI 命令`npx starwind@latest init`轻松安装，灵感来自 shadcn/ui
- 📦 核心特性包括：代码自主掌控（CLI 直接添加代码）、完全可定制（样式/功能/行为均可修改）、无障碍设计（键盘导航友好）、开源且 MIT 许可
- 🌟 立即开始使用 Starwind UI，打造用户喜爱的美观无障碍网站

---

### [WindyBase - 探索免费和高级的 Tailwind CSS 模板](https://windybase.com/?ref=tailwindweekly.com)

**原文标题**: [WindyBase - Explore free and premium Tailwind CSS templates ](https://windybase.com/?ref=tailwindweekly.com)

WindyBase 是一个每周精选的 Tailwind CSS 模板和工具目录，旨在帮助开发者快速构建现代网站和应用，提供免费和付费资源。

- 🧭 网站提供丰富的 Tailwind CSS 模板和组件库，包括落地页、SaaS、博客、仪表盘、电商等类别。
- 💰 模板价格从免费到 $249 不等，例如 Voyager、Amplify 等定价 $77，部分如 Accio 为 $39，也有免费模板如 Blogsmith Free。
- 🛠️ 组件库部分提供免费选项（如 HyperUI、Mamba UI）和付费专业版（如 Preline Pro 售价 $249）。
- 🔍 用户可通过搜索功能快速查找所需资源，并支持按类别浏览更多内容。
- 📧 提供新闻订阅功能，用户可获取新模板和组件更新通知。
- 🌐 网站还包含提交项目、联系方式和法律条款等额外功能，并支持 Twitter/X 和 Bluesky 社交平台。

---

### [Zoneless | 开源 Stripe Connect 替代方案](https://zoneless.com/?ref=tailwindweekly.com)

**原文标题**: [Zoneless | Open-Source Stripe Connect Alternative](https://zoneless.com/?ref=tailwindweekly.com)

Zoneless 是一个开源支付平台，为全球市场提供基于 USDC 的即时、低费用支付解决方案，可作为 Stripe Connect 的替代品。

- 💰 **近乎零费用**：每笔支付仅需约$0.002 的 SOL gas 费，无月费或百分比抽成
- 🔄 **Stripe 兼容**：API 与 Stripe 完全兼容，迁移只需少量代码修改
- 🔓 **开源自托管**：Apache 2.0 许可，可自行审计、托管，无供应商锁定
- 🌍 **全球覆盖**：支持 220+ 国家和地区，包括巴西、中国、澳大利亚等
- ⚡ **即时支付**：基于 Solana 区块链，USDC 结算仅需数秒，7x24 小时运行
- 🔑 **自我托管**：用户持有私钥，资金不经过第三方，完全自主控制
- 📊 **Express 仪表盘**：为卖家提供熟悉的支付追踪和管理界面
- 🏢 **实际应用**：已在拥有 45 万 + 用户的 PromptBase 市场成功运行，节省大量费用
- 🛠️ **开发者工具**：提供 Webhooks、幂等性、Node SDK 等完整开发功能
- 📈 **成本对比**：相比 Stripe Connect，月费、支付费、跨境费、汇率转换费均大幅降低

---

### [Instagit | 让您的代理即时理解任何 Git 仓库](https://instagit.com/?ref=tailwindweekly.com)

**原文标题**: [Instagit | Let Your Agents Instantly Understand Any Git Repo](https://instagit.com/?ref=tailwindweekly.com)

该工具能让 AI 代理直接理解任何 GitHub 仓库的源代码，提供精准的集成指导，避免基于幻觉或过时文档的错误。

- 🚀 **核心功能**：代理通过 MCP 协议直接读取源码，返回精确的文件路径和行号，而非依赖 README 或过时文档。
- ⚡ **快速集成**：支持 Claude、Cursor 等主流代理，提供一键安装命令（curl/npx），无需注册或 API 密钥即可免费使用。
- 🔍 **精准回答**：绕过网络搜索的噪音和过时信息，直接分析当前代码，确保函数签名、参数类型等细节准确无误。
- 📂 **广泛支持**：覆盖所有约 3000 万个公共 GitHub 仓库，免费版支持≤2GB 仓库，付费版无限制并可指定分支/标签。
- 🛠️ **技术亮点**：采用事件驱动架构、懒评估系统、KV 缓存等优化，确保大规模代码库的快速响应（常见问题秒级返回）。
- 🌐 **多场景应用**：从 DevTools 到 AI 框架，提供即时代码理解，例如 Redis ACL 安全模型、Vite 插件系统等深度分析示例。
- 📖 **知识库浏览**：将 GitHub URL 替换为 instagit.com 即可直接浏览仓库知识库，无需代理。
- 🏷️ **开源贡献**：维护者可通过添加 Instagit 徽章到 README，让仓库自动被 AI 代理发现并收录。

---

### [介绍 ArkRegex](https://arktype.io/docs/blog/arkregex?ref=tailwindweekly.com)

**原文标题**: [Introducing ArkRegex](https://arktype.io/docs/blog/arkregex?ref=tailwindweekly.com)

ArkRegex 是一个类型安全的正则表达式库，可作为 `new RegExp()` 的替代方案，支持从原生 JS 语法中静态解析类型，提升代码的类型安全性和可维护性。

- 🎯 **类型安全**：自动推断正则表达式的字符串类型，包括位置捕获和命名捕获，例如 `regex("^ok$", "i")` 会推断出 `"ok" | "oK" | "Ok" | "OK"` 类型。
- 🔄 **完全兼容**：支持 100% 的 `new RegExp()` 特性，可直接替换现有正则表达式。
- 🚨 **编译时错误检测**：将语法错误（如引用不存在的分组）转化为类型错误，提前发现问题。
- 📦 **零运行时开销**：仅提升类型安全，不影响最终打包体积。
- ⚡ **高性能**：在类型推断上平衡精度与性能，避免因复杂模式导致 TypeScript 类型爆炸。
- 🔧 **灵活处理复杂表达式**：对于超长或复杂正则，提供 `regex.as` 方法手动指定类型，避免类型推断过深。
- ✅ **经过严格测试**：使用 `attest` 进行广泛测试和基准测试，确保稳健性。
- 🎨 **语法高亮支持**：安装 ArkType 扩展可在 `regex` 调用中启用语法高亮。

---

