### [Maizzle / 现代电子邮件开发框架](https://maizzle.com/?ref=tailwindweekly.com)

**原文标题**: [Maizzle / The modern email development framework](https://maizzle.com/?ref=tailwindweekly.com)

Maizzle 是一个现代化的电子邮件开发框架，支持 Vue 和 Tailwind CSS，提供高效的开发、预览和构建流程。

- 🚀 **快速入门**：通过 `npx maizzle new` 命令即可创建新项目，简化电子邮件开发流程。
- 🧩 **组件化构建**：提供丰富的可复用组件（如布局、按钮、图片等），并经过邮件客户端兼容性测试。
- 🎨 **Tailwind CSS 集成**：将 Tailwind CSS 作为一等公民，针对邮件客户端进行优化，实现快速样式开发。
- 👁️ **实时预览**：内置开发界面，支持实时预览、设备尺寸调整、调试工具和命令面板。
- 🔧 **灵活工作流**：可集成到现有 Vite 项目，或作为独立工具使用，支持命令行和库调用。
- 📤 **任意平台部署**：编译为纯 HTML，兼容任何邮件服务提供商，适用于各类企业邮件构建。
- 🛍️ **扩展功能**：提供 Mailviews 模板库，包含高质量的生产级邮件模板和组件，一次性购买永久使用。

---

### [发布 v4.3.1 · tailwindlabs/tailwindcss · GitHub](https://github.com/tailwindlabs/tailwindcss/releases/tag/v4.3.1?ref=tailwindweekly.com)

**原文标题**: [Release v4.3.1 · tailwindlabs/tailwindcss · GitHub](https://github.com/tailwindlabs/tailwindcss/releases/tag/v4.3.1?ref=tailwindweekly.com)

Tailwind CSS v4.3.1 版本发布，包含多项新增功能、问题修复和优化改进。

- 🆕 新增 `--silent` 选项，可在 `@tailwindcss/cli` 中抑制输出 (#20100)
- 🔧 移除 Node 26+ 上的弃用警告，改用 `Module#registerHooks` (#20028)
- 🐛 修复插件工具对不支持值抛出异常时的崩溃问题 (#20052)
- ✅ 允许 `@apply` 与 CSS 混入一起使用 (#19427)
- 🚫 确保 `not-*` 正确否定 `@container` 查询，包括 `style(…)` 查询 (#20059)
- 🎨 修复 `drop-shadow-*` 颜色工具与包含 `calc(…)` 的自定义阴影值配合使用的问题 (#20080)
- 📍 修复 `@tailwindcss/vite` 中的“Sourcemap 可能不正确”警告 (#20103)
- 📦 确保 `@tailwindcss/webpack` 可在 Rspack 项目中安装，无需将 `webpack` 作为对等依赖 (#20027)
- 🧮 规范化：避免建议无效的 `calc(…)` 表达式 (#20127)
- 📏 规范化：避免为任意长度建议过大的间距比例值 (#20130)
- 🔄 确保 `@tailwindcss/cli` 在 `--watch` 模式下，当跟踪的依赖项被删除并恢复时能正常恢复 (#20137)
- 🚫 确保独立版 `@tailwindcss/cli` 二进制文件在扫描类候选时被忽略 (#20139)
- 🔍 确保从 Twig 的 `addClass(…)` 和 `removeClass(…)` 调用中提取类候选 (#20198)
- 🧪 修复 Ruby 或 Vue 预处理器在扫描包含无效 UTF-8 字节的文件时崩溃的问题 (#19588)
- 🏷️ 允许在 `addBase` 内部使用 `@variant` (#19480)
- 🔗 确保包含符号链接的 `@source` 通配符得以保留 (#20203)
- 🚫 确保后续的 `@source` 规则可以重新包含被早期 `@source not` 规则排除的文件 (#20203)
- ⬆️ 升级：不将空类规则迁移为无效的 `@utility` 规则 (#20205)
- 🌗 确保 `inset-shadow-none` 与其他内嵌阴影之间的过渡正常工作 (#20208)
- 📂 确保明确引用的 `@source` 目录即使被 git 忽略也会被扫描 (#20214)
- 🗂️ 确保以 `**/*` 结尾的 `@source` 通配符保留动态路径段，避免扫描过多文件 (#20217)
- 📐 规范化：不折叠需要高精度的 `calc(…)` 除法 (#20221)
- 📦 为 `@tailwindcss/postcss` 的 ESM 导入者提供 ESM 类型声明 (#20228)
- 🧹 间距工具：为 `m-0` 和 `left-0` 生成 `0` 而非 `calc(var(--spacing) * 0)` (#20196)
- 🧹 间距工具：为 `m-1` 和 `left-1` 生成 `var(--spacing)` 而非 `calc(var(--spacing) * 1)` (#20196)

---

### [Cap — 精美的屏幕录制，由你掌控。](https://cap.so/?via=vivian-guillen&dub_id=gW5wJNueCA4ET0se&ref=tailwindweekly.com)

**原文标题**: [Cap — Beautiful screen recordings, owned by you.](https://cap.so/?via=vivian-guillen&dub_id=gW5wJNueCA4ET0se&ref=tailwindweekly.com)

Cap 是一款集录制、编辑、截图和视频托管于一体的开源屏幕录制工具，提供三种模式，支持本地或云端存储，注重隐私与协作。

- 🎬 **三种录制模式**：Instant Mode（快速分享）、Studio Mode（专业编辑）、Screenshot Mode（截图），满足不同工作流程。
- 🔓 **完全开源**：代码在 GitHub 上公开，可自托管或贡献功能，确保透明度和可审计性。
- ☁️ **灵活存储**：支持连接自有 S3 存储、使用 Cap Cloud 或本地保存，用户完全掌控数据。
- 🔒 **隐私优先**：默认本地录制，可选公开或私密分享，支持密码保护，符合 GDPR/HIPAA 要求。
- 🤝 **异步协作**：支持评论、反应和转录，减少会议，将录制内容转化为可操作任务。
- 💻 **跨平台原生应用**：提供 macOS 和 Windows 原生应用，支持 4K 60fps 录制，性能流畅。
- 💰 **简单定价**：免费版支持 5 分钟本地录制；付费版（Cap Pro/Desktop License）提供商业使用、云端功能和无限 AI 功能。
- 🏢 **团队功能**：Pro 版包含团队工作区、权限管理和批量折扣，支持 Loom 视频导入。
- ❓ **常见问题**：明确区分免费与付费功能，强调数据所有权、安全性和合规性（如 HIPAA）。

---

### [如何在不影响网页性能的情况下使用懒加载 | DebugBear](https://www.debugbear.com/blog/lazy-loading-performance?utm_campaign=tailwind-weekly-219&utm_source=Tailwind+Weekly)

**原文标题**: [How to Use Lazy Loading Without Hurting Web Performance | DebugBear](https://www.debugbear.com/blog/lazy-loading-performance?utm_campaign=tailwind-weekly-219&utm_source=Tailwind+Weekly)

本文探讨了懒加载技术对网页性能的双面影响，并提供了最佳实践指南。

- 📉 懒加载可能损害性能：不当使用会延迟 LCP（最大内容绘制）、引发 CLS（累积布局偏移）和 INP（交互到下次绘制）问题，反而降低用户体验。
- ✅ 正确使用能提升性能：对首屏以下内容、长列表、无限滚动和第三方嵌入（如视频、地图）使用懒加载，可减少初始加载量、加快首屏渲染并降低带宽消耗。
- 🚫 避免懒加载关键内容：切勿对首屏图片（如英雄图）、关键 UI 元素使用懒加载，应使用`fetchpriority="high"`和`loading="eager"`确保优先加载。
- 📐 预留空间防止布局偏移：为图片和嵌入内容设置固定宽高或使用 CSS `aspect-ratio`，避免内容加载时发生布局跳动。
- ⚡ 注意交互性能影响：懒加载会将网络请求和解码工作推迟到用户滚动时，可能导致主线程堵塞，拖慢 INP 响应速度。
- 🛠 优先使用原生懒加载：推荐使用`loading="lazy"`属性，避免过度依赖基于 JavaScript 的 IntersectionObserver 或滚动监听库，以减少额外开销。
- 🔍 有选择地应用懒加载：不要全局启用，应针对非关键资源（如首屏以下图片、无限滚动内容）进行策略性延迟加载。
- 📊 用真实数据衡量效果：通过工具（如 DebugBear）检测 LCP 延迟、布局偏移和网络瀑布图，验证懒加载的实际影响。
- 💡 核心原则：懒加载不减少工作量，只是推迟执行——关键在于“何时”与“如何”使用，而非“是否”使用。

---

### [获取失败](https://css-tricks.com/almanac/pseudo-selectors/s/search-text/?ref=tailwindweekly.com)

**原文标题**: [Failed to retrieve](https://css-tricks.com/almanac/pseudo-selectors/s/search-text/?ref=tailwindweekly.com)

无法总结：获取内容失败，状态码 415。

---

### [如何评估一个 npm 包 - 2026 版](https://blog.gaborkoos.com/posts/2026-05-29-How-to-Evaluate-an-npm-Package-2026-Edition/?ref=tailwindweekly.com)

**原文标题**: [How to Evaluate an npm Package - 2026 Edition](https://blog.gaborkoos.com/posts/2026-05-29-How-to-Evaluate-an-npm-Package-2026-Edition/?ref=tailwindweekly.com)

### 概述总结
本文提供了在 2026 年评估 npm 包安全性和可靠性的系统化流程，强调不能仅依赖下载量和星标数，而应从实际需求、维护状态、发布可信度、CI 质量、代码质量和应急处理能力六个维度进行 5-10 分钟的快速审查。

- 📦 **先问是否真的需要**：进行"移除测试"，评估替代难度；小工具尽量自己实现；检查依赖树大小，减少攻击面
- 🔍 **检查维护活跃度**：查看 GitHub Issues 回复情况、人工提交记录、维护者数量（避免单点故障），以及 Changelog 质量
- 🔐 **验证 npm 发布可信度**：检查"Provenance"绿色徽章（来源证明），使用`npm audit signatures`验证签名，警惕安装脚本（preinstall/postinstall）
- 🛠️ **评估 CI 流水线真实性**：确认 CI 在 PR 合并前运行（而非仅推送到 main），检查测试覆盖率阈值（如 90%），查看测试文件结构是否完整
- 📝 **评估代码质量信号**：检查 ESLint 配置、package.json 的 exports 字段、prepublishOnly 脚本、TypeScript 的 strict 模式及 any/ts-ignore 使用频率
- 🚨 **检查安全应急能力**：确认 SECURITY.md 存在、查看历史安全公告处理速度、使用 Socket.dev 进行行为分析，必要时考虑 Socket Firewall 等强制策略

---

### [Brew - AI 电子邮件营销平台 | 秒速生成邮件 | Brew](https://brew.new/?ref=tailwindweekly.com)

**原文标题**: [Brew - AI Email Marketing Platform | Generate Emails in Seconds | Brew](https://brew.new/?ref=tailwindweekly.com)

概述摘要：本文探讨了人工智能在医疗领域的应用现状与未来潜力，重点分析了诊断辅助、药物研发和个性化治疗等关键方向，同时指出了数据隐私和伦理挑战。

- 🩺 人工智能在医学影像分析中展现出高准确率，可辅助医生快速识别肿瘤、骨折等异常。
- 💊 通过机器学习加速药物筛选过程，将新药研发周期从数年缩短至数月。
- 🧬 基于患者基因和病史数据，AI 能制定个性化治疗方案，提升慢性病管理效率。
- 🔒 医疗数据共享面临隐私泄露风险，需建立严格的数据加密和匿名化标准。
- ⚖️ 算法偏见可能导致诊断不公，需确保训练数据覆盖多元人群并接受伦理审查。

---

### [Curlwind | Tailwind 实用工具生成器](https://curlwind.com/?ref=tailwindweekly.com)

**原文标题**: [Curlwind | Tailwind Utility Generator](https://curlwind.com/?ref=tailwindweekly.com)

本工具提供按需生成 Tailwind CSS 样式表的功能，只包含你需要的工具类，无需构建步骤。

- 🎯 按需生成：通过 URL 参数指定所需 CSS 类，只获取实际使用的工具类，避免冗余
- 🔗 简单集成：只需在 HTML 的 head 标签中添加一个 link 标签即可使用
- ⚡ 缓存优化：生成的样式表会无限期缓存，确保网站加载速度
- 🎨 通配符支持：使用星号 (*) 通配符匹配多个类，如`p-*`匹配所有内边距类
- 🔄 变体生成：在类名后加冒号 (:) 可生成响应式变体，如`p-*:sm|md`
- 🚫 预检排除：通过`preflight=0`参数可排除 Tailwind 的 Preflight CSS
- 🏷️ 前缀设置：使用`prefix=tw`参数为工具类添加自定义前缀
- 📄 未压缩输出：通过`minify=0`参数生成未压缩的 CSS 文件
- 🔌 插件支持：通过`plugins`参数启用内置插件，如 forms、typography 等

---

### [PikaPods - 即时开源应用托管](https://www.pikapods.com/?ref=tailwindweekly.com)

**原文标题**: [PikaPods - Instant Open Source App Hosting](https://www.pikapods.com/?ref=tailwindweekly.com)

### 概述总结
PikaPods 提供开源应用托管服务，强调隐私保护、简单易用和透明定价，支持用户自选应用并管理数据。

- 🚀 **低成本入门**：每月仅需 $1.20 起，新用户可获 $5 欢迎信用额度，无需系统管理技能。
- 🔒 **隐私优先**：无追踪、无广告、无数据监控，支持欧盟和美国服务器位置，数据完全归用户所有。
- 📱 **精选应用**：包括 FreeScout（客服系统）、Immich（Google Photos 替代品）、Actual（财务管理）等开源工具，可一键部署。
- 🛠️ **简易管理**：统一界面管理所有应用，支持自动更新、数据库配置、自定义域名及资源调整。
- 💰 **透明定价**：按需付费（CPU/内存/存储灵活组合），无隐藏费用，20% 收入分成给开源开发者。
- 🔄 **无供应商锁定**：通过 SFTP 随时下载数据，可迁移至其他主机，支持备份到自有存储。
- 🛡️ **安全设计**：隔离容器、加密连接、内置防火墙，结合自建服务器的隐私与云服务的便捷性。
- 🌍 **全球覆盖**：提供欧盟和美国服务器位置，适用于不同地区的用户需求。

---

### [获取失败](https://github.com/h5bp/obs.js?ref=tailwindweekly.com)

**原文标题**: [Failed to retrieve](https://github.com/h5bp/obs.js?ref=tailwindweekly.com)

无法总结：获取内容失败，状态码 404。

---

### [获取失败](https://api.snhtml.com/?ref=tailwindweekly.com)

**原文标题**: [Failed to retrieve](https://api.snhtml.com/?ref=tailwindweekly.com)

无法总结：获取内容失败，状态码 404。

---

### [2026 年人工智能现状](https://2026.stateofai.dev/en-US?ref=tailwindweekly.com)

**原文标题**: [State of AI 2026](https://2026.stateofai.dev/en-US?ref=tailwindweekly.com)

2026 年 AI 开发者调查显示，AI 对开发工作的影响日益深远，以下是四个关键趋势：

- 📈 **AI 采用率大幅增长**：受访者生成的代码中，AI 生成比例从 2025 年的 28% 跃升至 2026 年的 54%，频繁使用 AI 的开发者比例同比翻倍。
- 🤖 **Claude Code 引领编码代理崛起**：Claude Code 在编码代理中获最高正面评价，Claude 成为开发者付费最多的模型，超越 ChatGPT。
- 💰 **AI 工具货币化加速**：个人 AI 支出明显增加，但多数受访者认为当前市场存在 AI 泡沫。
- ⚠️ **风险因素增加**：开发者担忧 AI 威胁工作安全，主要风险包括岗位取代、军事用途和环境影响，幻觉和不准确是最大痛点。

---

