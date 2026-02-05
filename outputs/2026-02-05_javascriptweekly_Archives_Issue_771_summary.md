### [JavaScript 周刊第 771 期：2026 年 2 月 3 日](https://javascriptweekly.com/issues/771)

**原文标题**: [JavaScript Weekly Issue 771: February 3, 2026](https://javascriptweekly.com/issues/771)

本期 JavaScript 周刊重点报道了多个重要框架和工具的更新动态，以及社区中的热点项目与安全事件。

- 🚀 **四大 JavaScript 重量级项目发布更新**：Gatsby v5.16 支持 React 19，Babel 8 进入发布候选阶段，Rspress 2.0 静态站点生成器发布，Lodash 推出安全修复版本。
- 🤖 **AI 助手项目 OpenClaw 引发热潮**：开源 TypeScript 项目在 GitHub 获 15 万星标，经历两次更名，并衍生出自主运行的社交网络等生态应用。
- 🔧 **工具与库版本更新**：Node.js v25.6.0 优化异步钩子性能，jQuery UI 兼容 jQuery 4.0，Bun 新增原生 Markdown 解析功能，另有多项主流工具发布新版本。
- 📚 **技术文章与教程精选**：涵盖 JavaScript 数字解析陷阱、Node.js 版本性能对比、ESLint 配置实践、WebGL 视觉效果实现等深度内容。
- 🛠️ **新工具与代码库推荐**：包括热力图生成库 Heat.js 5.0、Cron 调度工具 Croner 10.0、React日历组件DayFlow，以及TypeScript转C#编译器等创新项目。
- ⚠️ **安全与社区事件**：OpenJS 基金会发布年度安全报告，Notepad++ 编辑器疑似遭遇国家级攻击，GitHub 探讨低质量贡献解决方案。

---

### [v5.16 版本发布说明 | Gatsby](https://www.gatsbyjs.com/docs/reference/release-notes/v5.16/)

**原文标题**: [v5.16 Release Notes | Gatsby](https://www.gatsbyjs.com/docs/reference/release-notes/v5.16/)

Gatsby 5.16.0 版本于 2026 年 1 月发布，主要新增对 React 19 和 Node.js 24 的官方支持，同时包含多项错误修复与改进。

- 🚀 **支持 React 19**：Gatsby 及其官方维护的所有 `gatsby-` 包现已正式兼容 React 19，升级非破坏性，可安全使用 React 18 或 19。
- ⚠️ **升级注意事项**：社区插件可能尚未更新支持 React 19，需自行检查；部分新功能如文档元数据提升暂不可用，且实验性功能“部分水合”与 React 19 不兼容。
- 🛡️ **错误处理增强**：新增支持 React 19 的根错误回调（`onCaughtError` 和 `onUncaughtError`），可通过 `gatsby-browser.js` 自定义错误处理。
- 📦 **支持 Node.js 24**：Gatsby 现已官方支持 Node.js 24 版本。
- 🔧 **修复与改进**：包括更新 `body-parser` 以解决安全警告、清理过时的贡献指南等多项优化。

---

### [GatsbyJS 是否正式宣告死亡？· gatsbyjs/gatsby · 讨论 #39062 · GitHub](https://github.com/gatsbyjs/gatsby/discussions/39062)

**原文标题**: [Is GatsbyJS Officially Dead? · gatsbyjs/gatsby · Discussion #39062 · GitHub](https://github.com/gatsbyjs/gatsby/discussions/39062)

GatsbyJS 在 Netlify 收购后开发活动显著减少，社区普遍认为该项目已进入维护停滞状态，许多开发者因缺乏官方更新和支持而选择迁移至其他框架。

- 🏗️ 开发者反映 GatsbyJS 在 Netlify 收购后核心团队解散，项目开发近乎停滞，仅进行少量安全修复和依赖更新。
- 🔍 社区多次询问项目未来路线图，但官方未提供明确规划，仅表示会维持基本维护，引发对项目长期可靠性的担忧。
- 🚀 许多用户已开始迁移至替代框架，如 Next.js、Astro、Nuxt.js 等，其中 Next.js 因生态丰富成为热门选择，Astro 则因静态站点生成优势受到关注。
- ⚠️ 关键插件（如 gatsby-source-shopify）面临 API 过时风险，虽官方承诺更新，但整体插件生态支持不足，影响生产项目稳定性。
- 😔 社区对 Netlify 的处理方式表示失望，认为缺乏透明度和支持损害了开源项目的信誉，导致开发者流失和信任危机。

---

### [7.29.0 版本发布：Babel 7 的最后一个小版本更新](https://babeljs.io/blog/2026/01/31/7.29.0)

**原文标题**: [7.29.0 Released: The last Babel 7 minor release · Babel](https://babeljs.io/blog/2026/01/31/7.29.0)

Babel 7.29.0 作为 Babel 7 的最后一个次要版本发布，同时推出了 Babel 8.0.0 的候选版本，标志着向 Babel 8 的过渡。此版本主要增强了 @babel/standalone 的功能，并提供了迁移支持，以帮助用户顺利升级到 Babel 8。

- 🚀 **Babel 7.29.0 发布**：这是 Babel 7 的最后一个次要版本，同时推出了 Babel 8.0.0 的候选版本，鼓励用户提前试用。
- 🎯 **@babel/standalone 新特性**：支持通过 `<script>` 元素的 `data-target` 属性定义转译目标，并添加了异步 API 支持，便于从 Babel 7 迁移到 Babel 8。
- 📝 **迁移指南与资源**：提供了详细的迁移指南，包括针对普通用户和开发者的文档，帮助用户提前适应 Babel 8 的变更，如默认目标从 ES5 改为 Browserslist 的默认查询。
- 🔄 **Babel 8 的重大变化**：Babel 8 将仅作为 ESM 包发布，基于 Node.js 20 的 `require(esm)` 支持，不再提供 CommonJS 版本，但升级过程设计为平滑过渡。
- 💡 **社区支持呼吁**：鼓励个人或公司通过 Open Collective 捐赠或直接参与 ECMAScript 提案的实现，以支持 Babel 的持续发展。

---

### [发布 v8.0.0-rc.1 · babel/babel · GitHub](https://github.com/babel/babel/releases/tag/v8.0.0-rc.1)

**原文标题**: [Release v8.0.0-rc.1 · babel/babel · GitHub](https://github.com/babel/babel/releases/tag/v8.0.0-rc.1)

Babel 发布了 v8.0.0-rc.1 预发布版本，包含多项重大变更、新功能、错误修复及性能优化。

- 💥 **重大变更**：包括移除对 ESLint v7-v8 的支持、默认启用实验性 worker 解析器、删除部分插件及功能等。
- 🚀 **新功能**：新增代码帧起始行指定、导入/导出构建器属性增强、独立版本支持异步转换等。
- 🐛 **错误修复**：修正解析器类型断言处理、遍历器变量遮蔽检查、插件参数类型等问题。
- 💅 **代码优化**：改进解析器错误类型提示，提升开发者体验。
- 🏠 **内部调整**：替换颜色库为 Node.js 原生模块、增强包发布检查、改进异常处理等。
- 🏃‍♀️ **性能提升**：优化代码生成器性能，提升转换效率。

---

### [Rspress 2.0 正式发布 - Rspress](https://rspress.rs/blog/rspress-v2)

**原文标题**: [Announcing Rspress 2.0 - Rspress](https://rspress.rs/blog/rspress-v2)

Rspress 2.0 正式发布，这是一款基于 Rsbuild 的静态站点生成器，专为开发者文档站点设计。新版本在主题美学、AI 原生支持、文档开发体验、与 Rslib 集成等方面进行了重大升级，提供了更快的编译性能、全新的默认主题、内置多语言支持以及创新的 SSG-MD 功能，旨在提升文档站点的美观性、可访问性和开发效率。

- 🎨 **全新主题设计**：默认主题全面升级，视觉和阅读体验显著提升，支持通过 CSS 变量、BEM 类名、ESM 重导出和组件弹出四种方式进行深度定制。
- 🤖 **AI 原生支持**：内置 llms.txt 生成和 SSG-MD 功能，将页面渲染为高质量 Markdown，优化 AI Agent 对文档内容的理解和使用。
- ⚡ **即时启动与懒编译**：默认启用 lazyCompilation 和持久化缓存，实现毫秒级冷启动，结合链接悬停预加载，提升开发体验。
- 🌈 **Shiki 代码高亮**：默认集成 Shiki，在构建时完成语法高亮，支持多主题切换和扩展（如 twoslash），提供更丰富的代码块显示效果。
- 🔗 **文档开发体验优化**：默认启用死链检查，支持文件代码块引用，改进 HMR 对配置文件的响应，插件预览和播放器可同时使用。
- 📚 **内置多语言支持**：主题内置中文、英文、日文等多语言翻译，自动进行 Tree Shaking，支持通过配置扩展或覆盖翻译文本。
- 🧩 **Rslib 集成**：使用 create-rslib 创建组件库项目时，可选择 Rspress 快速搭建组件文档站点，实现一体化开发体验。
- 🛠️ **官方插件丰富**：新增 @rspress/plugin-algolia、@rspress/plugin-twoslash 等官方插件，增强搜索、类型提示和 SEO 功能。
- ⚠️ **破坏性变更**：移除 mdxRs 配置，合并包名为 @rspress/core，要求 Node.js 20+ 和 React 18+，提供详细迁移指南。

---

### [深入 Lodash 安全重置与维护重启内部——Sock...](https://socket.dev/blog/inside-lodash-security-reset)

**原文标题**: [Inside Lodash’s Security Reset and Maintenance Reboot - Sock...](https://socket.dev/blog/inside-lodash-security-reset)

Open VSX 宣布将实施预发布安全检查机制，以应对近期多次恶意扩展程序事件，旨在提前识别和阻止高风险上传。

- 🔒 引入预发布安全检查，防止恶意扩展程序上传
- 🛡️ 针对多次供应链安全事件，加强平台防护措施
- ⏰ 提前检测风险，在发布前拦截可疑扩展程序
- 📈 提升 Open VSX 平台整体安全性和用户信任度

---

### [Lodash](https://lodash.com/)

**原文标题**: [Lodash](https://lodash.com/)

Lodash 是一个现代化的 JavaScript 实用工具库，提供模块化、高性能和额外功能，简化了数组、数字、对象和字符串等数据类型的处理。

- 🛠️ **功能丰富**：提供多种实用方法，用于迭代数组、对象和字符串，操作和测试值，以及创建复合函数。
- 📦 **模块化设计**：支持多种构建版本，包括核心构建（约 4kB）、完整构建（约 24kB）和按需加载的方法包，适合不同项目需求。
- 🌐 **多环境支持**：可在浏览器、Node.js 等环境中使用，支持通过 npm、CDN 或直接引入脚本安装。
- 🔄 **函数式编程**：提供专门的 FP 版本，支持不可变、自动柯里化、迭代优先和数据最后的方法。
- 📄 **开源许可**：基于 MIT 许可证发布，支持现代 JavaScript 环境，兼容多种浏览器和 Node.js 版本。
- 🛡️ **社区维护**：由核心团队和贡献者维护，拥有详细的文档、指南和社区支持资源。

---

### [精密 AI——无需编写测试的自动化前端测试](https://www.meticulous.ai?utm_source=jsweekly&utm_medium=referral&utm_campaign=26q1&utm_content=primary)

**原文标题**: [Meticulous AI - Automated Frontend Testing Without Writing Tests](https://www.meticulous.ai?utm_source=jsweekly&utm_medium=referral&utm_campaign=26q1&utm_content=primary)

Meticulous AI 是一款创新的自动化测试工具，通过记录用户与应用交互生成并维护测试套件，无需手动编写或修复测试，帮助团队高效交付无回归的可靠代码。

- 🚀 **无需编写测试**：通过记录用户交互自动生成覆盖所有代码分支和边缘情况的测试套件，无需手动编写或维护测试。
- 🔄 **自动演化测试**：随着应用更新，测试套件自动添加新功能测试并淘汰过时测试，保持测试始终最新且完整。
- ⚡ **闪电般执行速度**：基于 Chromium 构建的确定性调度引擎，实现无抖动测试，并通过并行计算在 120 秒内完成数千次测试。
- 🛡️ **零副作用测试**：通过模拟后端响应进行测试，无需设置测试账户或模拟数据，避免误报和数据变更影响。
- 🔗 **无缝集成**：支持与现有测试套件结合使用或完全替代，提供与主流框架（如 React、Vue、Angular 等）的快速集成方案。
- 📈 **提升开发效率**：被 Dropbox、Notion 等超过 100 家组织信任，帮助工程师减少调试时间，加速可靠代码的交付流程。

---

### [OpenClaw — 个人 AI 助手](https://openclaw.ai/)

**原文标题**: [OpenClaw — Personal AI Assistant](https://openclaw.ai/)

OpenClaw 是一款开源的个人 AI 助手，能够通过常用聊天应用（如 WhatsApp、Telegram）进行操作，具备持久记忆和系统控制能力，让用户拥有一个可自我扩展的私人 AI 伙伴。

- 🦞 **开源可自控** – 数据存储在本地，非云端托管，用户拥有完全控制权，可自行修改和扩展。
- 🤖 **多功能自动化** – 可管理邮件、日历、文件，运行脚本，控制智能家居，甚至处理代码测试和错误修复。
- 💬 **全平台聊天集成** – 支持 WhatsApp、Telegram、Discord、Slack 等常用通讯工具，通过自然对话进行操作。
- 🧠 **持久记忆与个性化** – 具备长期记忆能力，能够学习用户习惯，成为个性化的“第二大脑”。
- 🔧 **技能自扩展** – 可通过对话让 AI 自行创建新技能或插件，社区也在不断贡献新功能。
- ⚡ **快速部署** – 提供一键安装脚本，支持 macOS、Windows、Linux，几分钟内即可完成设置。
- 🌐 **未来感体验** – 许多用户形容使用体验如同“活在未来”，感觉像是早期 AGI 或数字同事。

---

### [GitHub - openclaw/openclaw：您的专属AI助手。跨操作系统。跨平台。以龙虾之道，行智能之事。🦞](https://github.com/openclaw/openclaw)

**原文标题**: [GitHub - openclaw/openclaw: Your own personal AI assistant. Any OS. Any Platform. The lobster way. 🦞](https://github.com/openclaw/openclaw)

OpenClaw 是一个可在本地设备上运行的个人 AI 助手，支持通过多种即时通讯平台（如 WhatsApp、Telegram、Slack 等）进行交互，并具备语音、画布、多代理路由等高级功能。

- 🦞 **个人 AI 助手** - 可在自有设备上运行，通过多种通讯渠道与用户交互。
- 🌐 **多平台支持** - 兼容 WhatsApp、Telegram、Slack、Discord、Google Chat、Signal、iMessage、Microsoft Teams、WebChat 等。
- 🗣️ **语音与画布** - 支持语音唤醒、对话模式以及实时的可视化画布（Canvas）控制。
- 🔧 **工具与自动化** - 内置浏览器控制、定时任务、节点操作（如相机、录屏）及技能平台。
- 🛡️ **安全与沙箱** - 默认提供主机工具访问，可为非主会话配置 Docker 沙箱以增强安全性。
- 🚀 **便捷部署** - 提供向导式安装（`openclaw onboard`），支持 npm/pnpm/bun 及 Docker、Nix 等多种部署方式。
- 📱 **可选客户端** - 提供 macOS 菜单栏应用、iOS 和 Android 节点应用，以扩展功能。
- 🔌 **远程网关** - 支持通过 Tailscale 或 SSH 隧道实现远程访问，可在 Linux 服务器上运行网关。
- 📚 **完善文档** - 涵盖从入门、配置到安全、故障排查的详细指南。

---

### [Moltbook 是当前互联网上最有趣的地方。](https://simonwillison.net/2026/Jan/30/moltbook/)

**原文标题**: [Moltbook is the most interesting place on the internet right now](https://simonwillison.net/2026/Jan/30/moltbook/)

文章介绍了当前 AI 领域最热门的开源项目 OpenClaw（曾用名 Clawdbot、Moltbot），它是一个数字个人助理，通过技能系统实现强大功能，并重点描述了基于其技能构建的创意社交平台 Moltbook，该平台让 AI 助理之间能够互动交流。作者在肯定其创新价值与社区活力的同时，也表达了对安全风险的担忧，包括提示注入攻击、技能潜在恶意性以及缺乏可靠安全方案等问题。

- 🤖 OpenClaw 是一个开源数字个人助理项目，两个月内 GitHub 获星超 11.4 万，通过技能系统实现功能扩展
- 🔗 Moltbook 是基于 OpenClaw 技能构建的社交平台，AI 助理可在此互动、发帖和创建子论坛
- ⚠️ 作者指出该类软件存在提示注入等安全风险，技能可能窃取信息，且缺乏有效安全方案
- 🛠️ 社区通过 clawhub.ai 分享数千种技能，用户可远程控制手机、处理音频等，展现强大应用潜力
- 🔐 用户为降低风险使用独立设备运行，但作者认为“致命三重威胁”依然存在，安全建设迫在眉睫

---

### [JS Bin - 协作式 JavaScript 调试工具](https://jsbin.com/)

**原文标题**: [JS Bin - Collaborative JavaScript Debugging](https://jsbin.com/)

JS Bin 是一个在线代码编辑和实时预览工具，支持 HTML、CSS 和 JavaScript 等多种语言，并提供丰富的功能如代码分享、嵌入和协作编辑。

- 🛠️ **功能丰富** – 支持多种处理器（如 Markdown、Sass、TypeScript）和实时控制台输出
- 🔗 **分享便捷** – 可通过链接、嵌入代码或导出为 Gist 轻松分享作品
- ⌨️ **快捷键高效** – 提供多种键盘快捷键，提升编辑效率（如 Ctrl+S 保存、Ctrl+Enter 重新渲染）
- 🌐 **URL 灵活** – 不同 URL 后缀对应特定功能（如`/edit`编辑、`/embed`生成嵌入版本）
- 👥 **协作与账户** – 支持登录注册、代码存档、克隆和模板保存，便于团队协作
- 📚 **资源与支持** – 提供博客、帮助文档和社区支持，用户可升级 Pro 版本获取更多功能

---

### [JS Bin 将于 2026 年下线](https://remysharp.com/2026/02/02/js-bin-down-in-2026)

**原文标题**: [JS Bin down in 2026](https://remysharp.com/2026/02/02/js-bin-down-in-2026)

JS Bin 在 2026 年 1 月底遭遇了持续数天的严重宕机，作者通过升级 Node.js 版本、优化 nginx 配置、引入 CloudFlare 防护以及调整防火墙规则等一系列措施，最终解决了因异常流量攻击导致的服务器过载问题，并反思了在危机中过度依赖 AI 工具可能带来的配置复杂化风险。

- 🚨 **严重宕机事件**：JS Bin 在 2026 年 1 月底遭遇持续数天的宕机，服务器因异常流量攻击导致内存和 CPU 过载，无法通过常规重启恢复。
- 🛠️ **维护模式遗留问题**：JS Bin 已运行近 18 年，长期处于“维护模式”，服务器资源仅为 1GB 内存的单核 AWS 实例，且 Node.js 版本停留在古老的 v7。
- 📈 **异常流量攻击**：监控显示入站网络流量飙升至 100MB 峰值，持续高并发请求导致服务器崩溃，作者推测可能是 AI 爬虫大规模抓取所致。
- 🔧 **技术升级与优化**：将 Node.js 从 v7 升级至 v22，优化 nginx 配置（调整工作进程、超时设置等），并配置系统在内存不足时优先终止 Node 进程以保留 SSH 访问能力。
- 🛡️ **引入 CloudFlare 防护**：将 DNS 解析迁移至 CloudFlare 以过滤恶意流量，但初期因配置错误导致合法用户收到 520 错误（TLS 版本不匹配）。
- 🔐 **防火墙与安全组配置**：通过服务器 ufw 规则和 AWS 安全组批量添加 CloudFlare IP 白名单，彻底屏蔽非代理流量，缓解服务器压力。
- 🤖 **AI 工具使用反思**：作者在紧急调试中过度依赖 ChatGPT 等 AI 工具，导致配置复杂化（如 nginx 规则冲突），反而延长了故障排查时间。
- ✅ **根本问题解决**：禁用 CloudFlare 的 TLS 1.3 支持以匹配服务器旧版 nginx，并清理错误配置后，服务完全恢复，服务器负载降至正常水平（CPU 使用率约 4.6%）。
- 📊 **防护效果显著**：CloudFlare 成功拦截大量攻击流量（仅香港地区 24 小时内就有 1000 万请求），作者后悔未尽早部署防护措施。

---

### [错误](https://javascriptweekly.com/link/180175/web)

**原文标题**: [Error](https://javascriptweekly.com/link/180175/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='openjsf.org', port=443): Max retries exceeded with url: /blog/openjs-security-annual-report-2025 (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1000)')))

---

### [RFC：将 OnPush 设为默认变更检测策略 · angular/angular · 讨论 #66779 · GitHub](https://github.com/angular/angular/discussions/66779)

**原文标题**: [RFC: Setting OnPush as the default Change Detection Strategy · angular/angular · Discussion #66779 · GitHub](https://github.com/angular/angular/discussions/66779)

Angular 团队计划在 v22 版本中将组件的默认变更检测策略改为 OnPush，并将现有的 Default 策略重命名为 Eager，以更好地支持无区域（zoneless）应用并提升性能。

- 🚀 **默认策略变更**：从 Angular v22 开始，新组件的默认变更检测策略将改为 OnPush，以提升性能并适配无区域应用。
- 🔄 **策略重命名**：现有的 Default 策略将重命名为 Eager，以更清晰地表达其“主动检查”的含义，避免与“推荐默认”混淆。
- ⏳ **迁移计划**：现有代码库将通过自动迁移工具将未指定策略的组件显式设置为 Eager，以保持原有行为不变。
- 📅 **发布时间**：此变更计划于 2026 年 5 月随 Angular v22 发布，团队正在征求社区反馈。
- 💬 **社区反响**：多数开发者对此变更表示支持，认为这是期待已久的改进，能简化项目配置并提升代码一致性。

---

### [Astro 2026 年 1 月更新亮点 | Astro](https://astro.build/blog/whats-new-january-2026/)

**原文标题**: [What’s new in Astro - January 2026 | Astro](https://astro.build/blog/whats-new-january-2026/)

Astro 2026 年 1 月动态更新，涵盖技术进展、社区贡献、新工具与模板，以及丰富的用户案例展示。

- 🚀 Astro 技术公司加入 Cloudflare，v6 Beta 版本发布，并解释了项目的资金模式
- 📈 Astro 在 GitHub 和 JavaScript Rising Stars 2025 中表现突出，发布了 2025 年度回顾
- 🏛️ 知名机构如哈佛大学和瑞士媒体 Tages-Anzeiger 已采用 Astro 构建网站
- 🌐 展示了多个创新网站案例，包括伦敦烤肉餐厅指南和民主风险追踪器等特色项目
- 🎨 通过视觉惊艳的网站如 ASTRO_INFINITY，证明了 Astro 在动画和视觉效果上的强大能力
- 👥 欢迎新维护者 Shinya Fujino 加入，并表彰了多位社区贡献者的工作
- 📚 社区产出了大量实用内容，包括迁移经验、技术教程和性能优化案例
- 🛠️ 发布了众多新工具与集成，如 Sitepins CMS、StudioCMS UI 和一系列 Astro 专用组件
- 🎭 新增了大量主题与模板，涵盖博客、企业站、电商等多种类型，方便快速启动项目
- 🌍 展示了全球范围内使用 Astro 构建的多样化网站，从个人博客到企业平台应有尽有
- 📖 发现了更多使用 Starlight 构建的文档站点，体现了其作为文档框架的流行度

---

### [Svelte 2026 年 2 月更新亮点](https://svelte.dev/blog/whats-new-in-svelte-february-2026)

**原文标题**: [What’s new in Svelte: February 2026](https://svelte.dev/blog/whats-new-in-svelte-february-2026)

Svelte 和 SvelteKit 在 2026 年 2 月迎来多项更新，包括自定义选择元素、远程函数按钮属性调整及适配器改进，同时社区涌现出丰富的应用、学习资源和工具库。

- 🎨 现可通过 CSS 和富 HTML 内容自定义 `<select>` 元素，支持现代浏览器
- 🔧 Svelte 的 CSS 解析器 `parseCss` 现已从 `svelte/compiler` 导出，提供轻量级 CSS AST 解析
- 🌑 创建自定义元素时，可向 `attachShadow()` 传递 `ShadowRootInit` 对象以配置影子根
- ⚠️ SvelteKit 远程函数存在一项破坏性变更：移除了 `buttonProps`，需改用 `{...myForm.fields.action.as()}` 语法处理多提交按钮
- 🖥️ Node 适配器现支持通过环境变量配置服务器的 `keepAliveTimeout` 和 `headersTimeout` 选项
- 👁️ Vercel 适配器现在可在 `/_app/remote` 路由下追踪远程函数调用，便于观察
- 🛠️ 社区展示包括高性能媒体转换工具 Frame、开源日志平台 LogTide、P2P 通话游戏应用 funcalling 等多个新应用和站点
- 📚 学习资源涵盖播客“This Week in Svelte”最新两期及关于将 SvelteKit 应用打包成单一二进制文件的文章
- 📦 新发布的工具库涉及 UI 组件、状态管理、插件与编译器等多个领域，例如 mapcn-svelte、Reddo.js、fastify-svelte-view 等

---

### [Node.js — Node.js 25.6.0（当前版本）](https://nodejs.org/en/blog/release/v25.6.0)

**原文标题**: [Node.js — Node.js 25.6.0 (Current)](https://nodejs.org/en/blog/release/v25.6.0)

Node.js 25.6.0 版本发布，包含多项新功能、性能优化和依赖项更新，主要改进涉及异步钩子、网络模块、ESM 嵌入支持、流处理和测试运行器等方面。

- 🚀 **异步钩子增强**：新增 `trackPromises` 选项至 `createHook()`，便于更精细地追踪 Promise 生命周期。
- 🌐 **网络功能扩展**：为 `Socket` 添加 `setTOS` 和 `getTOS` 方法，支持设置和获取服务类型（Type of Service）。
- 📦 **ESM 嵌入支持**：在嵌入器 API 中初步支持 ECMAScript 模块，提升模块化集成能力。
- ⚡ **性能优化**：通过 `simdutf` 库提升 `TextEncoder` 编码性能，并优化 `TextDecoder` 的 UTF-8 快速路径处理。
- 🔄 **流处理新增方法**：在 `node:stream/consumers` 中引入 `bytes()` 方法，增强流数据消费功能。
- 🧪 **测试运行器改进**：为 `run` 函数添加 `env` 选项，支持自定义测试环境变量。
- 🔗 **依赖项更新**：升级 Ada URL 解析器至 v3.4.2，支持 Unicode 17，并更新 OpenSSL、Undici 等核心依赖。
- 🐛 **问题修复与优化**：包括修复断言、缓冲区处理、构建配置及跨平台测试稳定性等问题。

---

### [jQuery UI 1.14.2 版本发布 | jQuery UI 博客](https://blog.jqueryui.com/2026/01/jquery-ui-1-14-2-released/)

**原文标题**: [jQuery UI 1.14.2 released | jQuery UI Blog](https://blog.jqueryui.com/2026/01/jquery-ui-1-14-2-released/)

jQuery UI 1.14.2 版本已发布，主要修复了标签页 ID 包含 Unicode 字符及支持带 URL 凭证页面的标签页问题，并移除了对 jQuery Mousewheel 插件的依赖。此版本还修复了缓动演示并迁移了测试基础设施至 jquery-test-runner。该版本已测试兼容 jQuery 1.12.4 至 4.0.0，且 jQuery UI 目前处于维护状态，仅进行兼容性更新和安全修复，不计划新增重要功能。

- 🐛 修复了标签页 ID 包含 Unicode 字符及支持带 URL 凭证页面的问题
- 🔧 移除了对 jQuery Mousewheel 插件的依赖
- 🛠️ 修复了缓动演示并迁移测试基础设施至 jquery-test-runner
- ✅ 已测试兼容 jQuery 1.12.4、2.2.4、3.6.4、3.7.1 及 4.0.0 版本
- ⚠️ jQuery UI 处于维护状态，仅进行兼容性更新和安全修复，无新功能计划
- 📦 提供多种下载方式：开发包、主题包、npm、bower 及 CDN 链接
- 📄 包含详细变更日志和升级指南供用户参考

---

### [Bun v1.3.8 | Bun 博客](https://bun.com/blog/bun-v1.3.8)

**原文标题**: [Bun v1.3.8 | Bun Blog](https://bun.com/blog/bun-v1.3.8)

本文介绍了 Bun 的安装与升级方法，以及其最新版本中新增的 Markdown 解析功能和构建分析工具。

- 📦 **安装 Bun**：支持多种安装方式，包括 curl、npm、PowerShell、scoop、Homebrew 和 Docker。
- 🔄 **升级 Bun**：使用 `bun upgrade` 命令即可轻松升级。
- 📝 **内置 Markdown 解析器**：Bun 新增了基于 Zig 的快速、符合 CommonMark 标准的 Markdown 解析器，提供 `html()`、`render()` 和 `react()` 三种渲染方式。
- 🧩 **GFM 扩展支持**：默认支持 GitHub Flavored Markdown 扩展，如表格、删除线、任务列表等。
- 📊 **构建分析工具**：`bun build` 新增 `--metafile-md` 选项，可生成 Markdown 格式的模块图分析报告，便于优化构建。
- 🐛 **错误修复**：修复了包括 `napi_typeof` 返回值错误、堆快照生成崩溃、HTTP/2 流状态处理问题及 Windows 安装失败等多个问题。

---

### [Astro 5.17 | Astro](https://astro.build/blog/astro-5170/)

**原文标题**: [Astro 5.17 | Astro](https://astro.build/blog/astro-5170/)

Astro 5.17 版本引入了多项新功能和改进，包括可配置的开发工具栏位置、异步文件解析、分区化 Cookie 支持、图像优化升级等，旨在提升开发体验和项目性能。

- 🛠️ **可配置开发工具栏位置**：新增 `devToolbar.placement` 配置选项，允许设置项目级的默认工具栏位置，避免与页面底部元素（如聊天窗口）冲突，同时仍支持开发者通过 UI 覆盖此设置。
- ⚡ **异步文件解析**：`file()` 加载器的 `parser()` 选项现在支持异步函数，便于在加载文件数据时执行复杂操作（如 API 调用），而现有同步解析器无需修改即可继续使用。
- 🍪 **分区化 Cookie 支持**：通过 `Astro.cookies.set()` 的新 `partitioned` 选项，支持在嵌入式场景（如 iframe）中设置分区化 Cookie，增强隐私控制并符合现代隐私标准。
- 🎨 **图像背景色控制**：图像转换新增 `background` 属性，允许在转换为不支持透明度的格式（如 JPEG）时指定背景颜色，支持 CSS 颜色语法，避免默认黑色背景。
- 🔍 **Sharp 内核选择**：Sharp 图像服务新增 `kernel` 配置选项，允许选择不同的重采样算法（如 `mks2021`），以精细控制图像缩放的质量和效果，适用于所有站点图像。
- 📦 **优化数据存储**：`glob()` 加载器新增 `retainBody` 选项（默认 `true`），设置为 `false` 时可避免存储原始文件内容，显著减少大型内容集合的数据存储大小。
- 🔄 **升级指南**：推荐使用 `@astrojs/upgrade` CLI 工具自动升级项目，或手动运行包管理器的升级命令（如 `npm install astro@latest`）以获取最新版本。
- 🐛 **错误修复与社区贡献**：版本包含自 5.16 以来的多项错误修复，详细更新请查阅变更日志；感谢核心团队及众多社区贡献者的代码与文档改进。

---

### [ESLint v10.0.0-rc.2 发布 - ESLint - 可插拔的 JavaScript 代码检查工具](https://eslint.org/blog/2026/01/eslint-v10.0.0-rc.2-released/)

**原文标题**: [ESLint v10.0.0-rc.2 released - ESLint - Pluggable JavaScript Linter](https://eslint.org/blog/2026/01/eslint-v10.0.0-rc.2-released/)

ESLint v10.0.0-rc.2 是一个预发布版本，主要修复了先前版本中的多个错误，并移除了部分实验性导出，同时提供了详细的迁移指南以帮助用户应对重大变更。

- 🐛 修复了核心 `strict` 规则中的回归问题
- 🗑️ 完全移除了 `/use-at-your-own-risk` 入口中的 `LegacyESLint` 和 `FlatESLint` 导出
- 📦 需通过指定 `next` 标签或版本号手动安装此预发布版本
- 📘 提供了详细的迁移指南，帮助用户处理版本升级中的破坏性变更
- 🔧 更新了文档，包括支持 `:is` 选择器别名和 ESM 依赖策略说明
- 🧹 进行了代码维护，如修复文档和注释中的拼写错误

---

### [GitHub - trpc/trpc: 🧙‍♀️ 快速推进，稳如磐石。轻松构建端到端类型安全的 API。](https://github.com/trpc/trpc)

**原文标题**: [GitHub - trpc/trpc: 🧙‍♀️  Move Fast and Break Nothing. End-to-end typesafe APIs made easy.](https://github.com/trpc/trpc)

tRPC 是一个用于构建端到端类型安全 API 的框架，无需模式或代码生成，强调开发效率和类型安全。

- 🧙‍♀️ 提供端到端类型安全的 API 开发方案，无需代码生成或额外模式定义
- 🚀 开发体验流畅，无运行时膨胀，客户端占用空间小
- 🔧 支持 React.js/Next.js/Express.js/Fastify 等适配器，并拥有社区开发的其他库适配器
- 📦 功能全面，包括订阅支持、请求批处理和丰富的示例项目
- 🌟 项目成熟度高，拥有 39.5k GitHub 星标和活跃的社区贡献
- 📄 采用 MIT 许可，提供详细的文档和快速入门指南

---

### [GitHub - facebook/lexical: Lexical 是一个可扩展的文本编辑器框架，提供卓越的可靠性、可访问性和性能。](https://github.com/facebook/lexical)

**原文标题**: [GitHub - facebook/lexical: Lexical is an extensible text editor framework that provides excellent reliability, accessibility and performance.](https://github.com/facebook/lexical)

Lexical 是一个由 Meta 开发的开源、可扩展的文本编辑器框架，专注于可靠性、可访问性和高性能，提供丰富的功能与跨浏览器支持，并拥有活跃的社区。

- 🧩 **框架无关的核心** – 可与任何 UI 框架配合使用，并提供了官方的 React 绑定。
- ♿ **可靠且易于访问** – 内置无障碍支持，符合 WCAG 标准。
- 🔌 **高度可扩展** – 采用基于插件的架构，提供强大的扩展点。
- ⏳ **不可变状态模型** – 内置撤销/重做功能，支持时间旅行调试。
- 👥 **协同编辑** – 通过 Yjs 集成支持实时协作编辑。
- 📄 **序列化支持** – 支持从 JSON、Markdown 和 HTML 格式导入/导出内容。
- 🎨 **支持富文本内容** – 支持表格、列表、代码块、图像和自定义节点。
- 🌐 **跨浏览器兼容** – 支持 Firefox 52+、Chrome 49+、Safari 11+、Edge 79+。
- 🛡️ **类型安全** – 使用 TypeScript 编写，提供全面的类型定义。
- 🚀 **快速开始** – 可通过 npm 安装，并提供了简单的 React 集成示例。
- 🛠️ **完善的开发与社区支持** – 提供详细的文档、开发指南、示例项目，并拥有 Discord 社区和 GitHub 讨论区。

---

### [Reka UI - 无样式、完全可访问的 UI 库 | Reka UI](https://reka-ui.com/)

**原文标题**: [Reka UI - Unstyled, fully accessible UI library | Reka UI](https://reka-ui.com/)

Reka UI v2 版本发布，这是一个基于 Vue 的开源库，提供无样式、基础的组件，帮助开发者快速构建可访问的 Web 应用。

- 🎉 **v2 版本发布**：推出新版开源库，专注于 Vue 框架的可访问性组件开发。
- 🧩 **无样式基础组件**：提供 40 多个原始组件，支持完全自定义样式，API 设计友好。
- ♿ **开箱即用的可访问性**：遵循 WAI-ARIA 设计模式，支持键盘导航、屏幕阅读器等辅助技术。
- 🌍 **国际化支持**：包含 RTL 布局、多语言和数字系统适配，适合全球用户。
- ⚡ **提升开发效率**：组件库旨在节省开发时间，加速项目交付，已有 160 万 + 月下载量。
- 📚 **丰富的资源**：提供组件示例、用例和详细文档，便于集成和学习。
- 🛠️ **易于上手**：支持快速安装和设置，开发者可浏览组件和样式示例开始使用。

---

### [精准解析器 - 每日 WTF](https://thedailywtf.com/articles/a-percise-parser)

**原文标题**: [A Percise Parser - The Daily WTF](https://thedailywtf.com/articles/a-percise-parser)

本文介绍了网站的几个主要栏目及其内容。

- 📰 专题文章：深入探讨特定主题或事件的详细报道。
- 💻 代码片段：分享实用或有趣的编程代码示例。
- ❌ 错误排查：提供常见技术问题的诊断与解决方案。
- 💬 论坛讨论：用户交流观点、提问和分享经验的社区平台。
- 📚 其他文章：涵盖各类主题的多样化文章集合。
- 🎲 随机文章：随机推荐一篇网站内的文章供读者探索。

---

### [Node.js 16 至 25 性能基准测试：性能随时间如何演变](https://www.repoflow.io/blog/node-js-16-to-25-benchmarks-how-performance-evolved-over-time)

**原文标题**: [Node.js 16 to 25 Benchmarks: How Performance Evolved Over Time](https://www.repoflow.io/blog/node-js-16-to-25-benchmarks-how-performance-evolved-over-time)

本文对 Node.js 16 至 25 版本进行了性能基准测试，重点关注 HTTP 吞吐量、JSON 处理、加密哈希、内存操作及循环计算等核心场景，揭示了各版本间的性能演进趋势。

- 📊 **HTTP GET 吞吐量测试**：测量本地 HTTP 服务器在保持连接和 32 个并发请求下的每秒请求处理能力。
- 🔍 **JSON 解析与序列化速度**：评估 Node.js 解析小型 JSON 数据及将对象序列化为 JSON 字符串的性能。
- 🔐 **SHA-256 哈希计算**：通过 crypto.createHash("sha256") 测试哈希生成的处理吞吐量。
- 💾 **缓冲区复制性能**：使用 Buffer.copy 方法测量 64KB 缓冲区的内存复制效率。
- 🔄 **数组映射与归约操作**：针对常见 JavaScript 模式（数组 map 后接 reduce）进行性能分析。
- 🧵 **字符串拼接效率**：测试通过重复拼接操作构建字符串的性能表现。
- ➗ **整数循环与算术运算**：通过紧凑整数循环执行基础算术运算，评估 JavaScript 引擎的数值代码优化效果。
- 🎲 **随机化整数循环测试**：在循环中引入 Math.random() 随机性，验证 Node 25 在真实数据依赖场景下的性能提升是否稳定。
- ⚙️ **测试方法与环境**：所有测试在 Apple M4 硬件上运行五次取中位数，测试间进行冷却以避免热偏差影响结果。
- 🚀 **核心结论**：Node.js 各版本性能持续稳步提升，Node 25 在数值计算和循环密集型任务中表现尤为突出，实际应用性能提升取决于具体工作负载特性。

---

### [B2B 企业就绪实用清单](https://hello.descope.com/b2b-enterprise-readiness-checklist?utm_source=cooperpress-newsletters&utm_medium=display&utm_campaign=javascript-weekly-newsletter-02-2026&utm_content=enterprise-checklist)

**原文标题**: [A Practical Checklist for B2B Enterprise Readiness](https://hello.descope.com/b2b-enterprise-readiness-checklist?utm_source=cooperpress-newsletters&utm_medium=display&utm_campaign=javascript-weekly-newsletter-02-2026&utm_content=enterprise-checklist)

本文介绍了一份面向快速增长的 B2B 公司的企业级准备清单，旨在帮助它们更高效地满足企业客户的身份验证需求，从而让开发团队能更专注于产品开发。

- 🔍 识别企业级准备就绪的信号
- 🏛️ 从六个基础支柱评估组织能力
- ⏱️ 获取最佳实践以释放工程团队时间
- 📥 提供可下载的实用检查清单

---

### [JavaScript 中的显式资源管理 - Matt Smith](https://allthingssmitty.com/2026/02/02/explicit-resource-management-in-javascript/)

**原文标题**: [
    Explicit resource management in JavaScript - Matt Smith
  ](https://allthingssmitty.com/2026/02/02/explicit-resource-management-in-javascript/)

JavaScript 终于引入了显式资源管理，提供了一种语言级别的机制来自动清理资源，减少了手动处理 `try/finally` 的繁琐和错误风险。

- 🧹 **资源清理问题**：传统 JavaScript 中，开发者需手动管理资源（如文件、锁）的清理，使用 `try/finally` 容易出错且代码冗长。
- 🆕 **`using` 声明**：通过 `using` 或 `await using` 声明资源，可自动在作用域结束时清理，无需显式调用清理方法。
- 🔧 **清理机制**：资源需实现 `Symbol.dispose`（同步）或 `Symbol.asyncDispose`（异步）方法，`using` 会自动调用这些方法。
- 📚 **多资源管理**：支持同时管理多个资源，清理按声明顺序反向自动执行，简化了错误处理和代码结构。
- 🎯 **作用域限定**：`using` 声明的资源遵循块级作用域，促使代码结构更清晰，资源生命周期更明确。
- 🔄 **灵活替代方案**：对于复杂场景，可使用 `DisposableStack` 或 `AsyncDisposableStack` 手动管理资源堆栈。
- 🌐 **跨平台应用**：该特性不仅适用于后端，也适用于前端（如 Web Streams、IndexedDB），提升代码可读性和可维护性。
- ⏳ **浏览器支持**：截至 2026 年初，Chrome、Firefox 和 Node.js 已支持，Safari 支持待定，适合库开发和实验性使用。

---

### [安德斯·海尔斯伯格（C#和TypeScript的设计师）的七点心得——GitHub博客](https://github.blog/developer-skills/programming-languages-and-frameworks/7-learnings-from-anders-hejlsberg-the-architect-behind-c-and-typescript/)

**原文标题**: [7 learnings from Anders Hejlsberg: The architect behind C# and TypeScript - The GitHub Blog](https://github.blog/developer-skills/programming-languages-and-frameworks/7-learnings-from-anders-hejlsberg-the-architect-behind-c-and-typescript/)

本文总结了编程语言设计师 Anders Hejlsberg（C#和TypeScript的创造者）在职业生涯中的核心洞见，强调构建能适应规模、持久耐用的工具与系统的关键原则。

- 🚀 **快速反馈至关重要**：从 Turbo Pascal 到 TypeScript，缩短编码与运行间的反馈循环能显著提升开发效率，鼓励更多实验与重构。
- 🤝 **规模化需放弃个人偏好**：成功系统需适应团队协作，而非追求个人理想中的完美设计，如C#平衡了不同开发者群体的需求。
- 🔄 **兼容现有生态优于取代**：TypeScript 选择扩展 JavaScript 而非另起炉灶，体现了尊重开发现实工作流程的务实妥协。
- 👁️ **开源项目的透明度建立信任**：公开决策过程、优先处理社区反馈能增强项目可信度与协作效率。
- ⚙️ **必要时更换实现语言以突破性能瓶颈**：TypeScript 编译器从 JavaScript 迁移到 Go，在保持行为一致性的同时解锁了并行计算与性能提升。
- 🧠 **AI 时代工具更需提供准确约束**：在 AI 辅助编程中，强类型系统、可靠重构工具等确定性工具比代码生成能力更重要，它们为 AI 输出提供校验基础。
- 📚 **开放协作保留机构记忆**：公开的讨论历史与决策记录帮助新成员理解系统演进背景，促进项目的长期健康发展。

---

### [我的 Vue 项目 ESLint 配置观点 | alexop.dev](https://alexop.dev/posts/opinionated-eslint-setup-vue-projects/)

**原文标题**: [My Opinionated ESLint Setup for Vue Projects | alexop.dev](https://alexop.dev/posts/opinionated-eslint-setup-vue-projects/)

本文分享了一套针对 Vue 项目的 ESLint 配置方案，旨在通过自动化规则强制执行代码规范，提升代码可读性、可维护性，并适应 AI 辅助编程时代的需求。该方案结合了 Oxlint 的速度优势和 ESLint 的全面性，并包含一系列核心规则、自定义规则及最佳实践。

- 🚀 **双检查器策略**：结合 Oxlint（快速检查）和 ESLint（全面检查），实现高效且完整的代码质量保障。
- 🛡️ **核心代码质量规则**：包括限制函数复杂度、禁止嵌套三元表达式、避免类型断言（`as`）、使用联合类型替代枚举、提倡提前返回替代`else/else-if`。
- 🔗 **架构与边界控制**：通过导入路径限制，强制实施功能模块隔离和单向数据流，防止跨功能模块的依赖。
- 🧩 **Vue 组件规范**：强制执行组件多词命名、属性命名约定、检测未使用的属性/引用/事件，并推荐使用 Vue 3.5+ 的新 API（如属性解构）。
- 🌐 **国际化与路由规范**：禁止硬编码文本字符串，强制使用国际化函数；禁止硬编码路由路径，提倡使用命名路由。
- 🧪 **测试代码规范**：统一测试结构（如使用`it`、钩子置顶），禁止直接使用`mount`/`render`而改用集中式测试助手，推荐使用 Vitest 定位器。
- 🦄 **现代 JavaScript 模式**：通过`eslint-plugin-unicorn`启用一系列提升代码质量的规则（如更好的正则表达式、一致的解构）。
- 🛠️ **自定义规则**：包括确保组合式函数正确使用 Vue、禁止硬编码 Tailwind 颜色、禁止在测试描述块中使用`let`、提取复杂条件为变量、强制对仓库调用进行错误包装。

---

### [使用 GSAP、Three.js、Astro 和 Barba.js 构建滚动触发的 WebGL 画廊 | Codrops](https://tympanus.net/codrops/2026/02/02/building-a-scroll-revealed-webgl-gallery-with-gsap-three-js-astro-and-barba-js/)

**原文标题**: [Building a Scroll-Revealed WebGL Gallery with GSAP, Three.js, Astro and Barba.js | Codrops](https://tympanus.net/codrops/2026/02/02/building-a-scroll-revealed-webgl-gallery-with-gsap-three-js-astro-and-barba-js/)

本文介绍了如何使用 GSAP、Three.js、Astro 和 Barba.js 构建一个多页面的 WebGL 图片画廊，实现滚动触发的着色器显示效果、平滑滚动和无缝页面过渡。

- 🎨 **技术栈组合**：结合 GSAP（驱动动画）、Three.js（WebGL 渲染）、Astro（轻量级多页面结构）和 Barba.js（页面过渡控制），打造现代创意开发项目。
- 🖼️ **DOM 与 WebGL 同步**：通过将 Three.js 平面与 HTML 图片精确匹配，确保滚动时视觉元素完美对齐。
- 🌀 **平滑滚动集成**：使用 GSAP 的 ScrollSmoother 插件实现与渲染循环协调的平滑滚动，避免原生滚动与 WebGL 更新不同步的问题。
- ⚡ **滚动触发着色器动画**：利用 ScrollTrigger 在图片进入视口时，通过着色器 uniform 控制实现动态显示效果。
- 🔄 **无缝页面过渡**：借助 Barba.js 管理导航，结合 Flip 插件实现点击图片时视觉上跨页面的平滑过渡效果。
- 📝 **文本动画增强**：使用 SplitText 插件对页面文字进行分行处理，并添加滚动触发的渐入渐出动画，提升用户体验。
- 🛠️ **环境与代码结构**：详细说明了项目初始化、页面模板、样式布局以及核心类（如 Canvas、Media、TextAnimation）的实现逻辑。
- ⚙️ **性能与清理**：强调在页面过渡时需妥善处理 GSAP 实例、Three.js 资源（如几何体、材质）以避免内存泄漏，确保应用高效运行。

---

### [使用 GSAP、Three.js 与 Astro 实现滚动时的 WebGL 像素特效](https://pixelimageeffect.pages.dev/)

**原文标题**: [WebGL Pixel Effect on Scroll with GSAP, Three.js and Astro](https://pixelimageeffect.pages.dev/)

本文介绍了一个结合 WebGL、GSAP 和 Three.js 实现的滚动像素化特效教程，并嵌入了一段北方探险的文学描写，展示了技术与创意叙事的结合。

- 🎨 教程使用 WebGL、GSAP 和 Three.js 创建滚动触发的像素化视觉效果
- 📜 内容包含北方探险（1970-1978）的文学片段，描绘了荒凉寒冷的自然环境
- 🧑‍🤝‍🧑 故事中出现了穿越荒野的男人、女人和孩子，突显生存的坚韧
- 🔗 提供了相关演示链接、GitHub 资源和更多类似教程推荐
- ❄️ 环境描写强调北地的孤寂、寒冷与自然力量的威严

---

### [[SMT][Z3] 使用 Z3 SMT 求解器预测 Firefox 中的 Math.random()](https://yurichev.com/blog/xorshift/)

**原文标题**: [[SMT][Z3] Predicting Math.random() in Firefox using Z3 SMT-solver](https://yurichev.com/blog/xorshift/)

本文介绍了如何利用 Z3 SMT 求解器预测 Firefox 浏览器中 Math.random() 函数的输出，通过分析其采用的 Xorshift128+ 伪随机数生成算法，仅需前三个随机数即可恢复初始状态，并验证了生成连续接近零值的随机数序列的可能性。

- 🔍 Firefox 使用 Xorshift128+ 算法生成伪随机数，其源码可通过链接查看
- 🧩 仅需前三个 Math.random() 输出值，即可利用 Z3 求解器唯一确定初始状态
- ✅ 实验成功恢复初始状态并准确预测后续 20 个随机数，验证了方法的有效性
- 🔬 通过修改 Z3 脚本，探索了生成连续接近零值随机数序列的可能性
- 📝 本文灵感来源于 Douglas Goddard 的相关文章，并提供了完整的代码示例

---

### [保障 npm 安全是基础要求——与尼古拉斯·C·扎卡斯对话（Changelog 访谈第 674 期）](https://changelog.com/podcast/674)

**原文标题**: [Securing npm is table stakes with Nicholas C. Zakas (Changelog Interviews #674)](https://changelog.com/podcast/674)

本期节目探讨了 npm 包管理器的安全现状及改进方向。ESLint 创始人 Nicholas C. Zakas 批评 GitHub 对 npm 安全问题的应对不足，并提出具体改进建议，同时分析了 JSR 等替代方案的局限性，表达了对关键基础设施缺乏重视的担忧。

- 🔐 Nicholas 认为 GitHub 对 npm 安全漏洞的回应不够充分，需采取更严格措施
- 💡 建议实施可信发布机制，通过自动化流程和多重验证提升包安全性
- ⚠️ 指出 npm 面临严重安全风险，可能因一次重大攻击导致生态系统崩溃
- 👥 质疑 npm 团队人员配置是否充足，担忧维护资源不足
- 🔄 讨论安装钩子的安全隐患，建议限制或移除高风险功能
- 🏷️ 提出验证发布者身份的方案，增强包来源的可信度
- 🌐 分析 JSR 等替代注册表的局限性，难以取代 npm 的生态地位
- 💰 探讨商业模式对安全的影响，建议建立可持续的资金支持机制
- 🤖 提及 AI 工具在代码安全中的潜在作用，超越炒作的实际价值
- 📢 呼吁社区关注基础设施安全，共同推动行业标准提升

---

### [使用 Astro 构建 RSS 聚合器](https://www.raymondcamden.com/2026/02/02/building-an-rss-aggregator-with-astro)

**原文标题**: [Building an RSS Aggregator with Astro](https://www.raymondcamden.com/2026/02/02/building-an-rss-aggregator-with-astro)

本文介绍了作者使用 Astro 框架构建一个 RSS 聚合器的过程，该应用允许用户自定义订阅源，并通过服务器端路由获取和解析内容，同时利用本地存储和缓存技术提升体验。

- 🛠️ 使用 Astro 框架构建 RSS 聚合器，支持用户自定义订阅源并通过服务器端路由获取和解析内容
- 🎨 前端采用 Simple.css 美化界面，通过原生对话框元素管理订阅源，利用 localStorage 持久化用户数据
- 🔄 实现订阅项的混合排序与缓存机制，使用 Netlify Blobs 进行一小时缓存以减少重复请求
- ⚡ 强调 Astro 在 Netlify 上的出色开发体验，仅需简单配置即可实现服务器端渲染和 Blob 存储功能
- 📦 项目代码已开源，提供在线演示链接供用户体验和进一步开发参考

---

### [Heat.js：JavaScript 热力图](https://www.heatjs.com/)

**原文标题**: [Heat.js : JavaScript Heat Map](https://www.heatjs.com/)

该工具是一款完全免费开源的日历组件，支持多框架集成、多语言与视图，提供数据导入导出及动态调整功能，便于趋势分析与定制使用。

- 📄 完全免费开源，遵循特定许可证
- 🔗 支持导出数据以集成 React、Vue、Angular 等框架
- ⚙️ 高度可配置，含自定义触发器和多语言文本支持
- 🌍 默认支持 60 种语言
- 📊 提供地图、折线、图表、日期、月份和色域等多种视图
- 📤 支持导出多种文件格式，含系统剪贴板设置
- 📥 支持从多种文件格式导入数据
- 🔄 组件可动态调整尺寸以适应不同布局或屏幕（默认关闭）
- 📈 可对比去年每日数据，快速查看百分比变化以识别趋势
- 🗓️ 推荐轻量级 JavaScript 库 Calendar.js 用于构建交互式日历
- 🆘 提供专门支持服务，承诺 48 小时内回复用户请求

---

### [线视图：演示：Heat.js](https://www.heatjs.com/demos/views/line)

**原文标题**: [Line View : Demos : Heat.js](https://www.heatjs.com/demos/views/line)

Heat.js 是一个用于创建热图日历的 JavaScript 库，提供多种视图和自定义选项，便于展示数据趋势。

- 🌐 **基础设置**：支持默认视图、自定义触发器和动态颜色等基本配置。
- 🎨 **主题与布局**：提供多语言支持、主题定制和年度统计功能。
- 📊 **视图选项**：包括地图、折线、图表等多种视图，可调整日期范围和颜色区间。
- ⚙️ **高级功能**：允许缩放、调整大小、显示计数、编辑趋势类型等自定义操作。
- 📄 **快速入门**：通过引入 CSS 和 JS 文件，创建 DOM 元素即可快速启用折线视图示例。

---

### [图表视图：演示：Heat.js](https://www.heatjs.com/demos/views/chart)

**原文标题**: [Chart View : Demos : Heat.js](https://www.heatjs.com/demos/views/chart)

Heat.js 是一个用于创建热图的可配置 JavaScript 库，提供多种视图和自定义选项。

- 🗺️ **基本视图**：支持地图、折线图、图表、天和月等多种视图类型。
- 🎨 **动态颜色与主题**：允许自定义颜色范围和主题，适应不同语言和布局需求。
- ⚙️ **高级配置**：包括缩放、调整大小、年度统计、标题栏按钮和可编辑趋势类型等功能。
- 📊 **图表视图示例**：通过包含特定 CSS 和 JS 文件，并在 DOM 中添加元素，可快速创建默认显示图表视图的热图实例。
- 🔗 **扩展文档**：更多高级功能和详细配置可查阅完整文档。

---

### [演示：Heat.js](https://www.heatjs.com/demos)

**原文标题**: [Demos : Heat.js](https://www.heatjs.com/demos)

该库提供了一套全面的数据可视化组件，包含多种图表类型和高度可定制的配置选项，帮助用户快速集成并适应不同的项目需求。

- 🧭 通过左侧导航可访问示例和指南，涵盖从基础设置到高级配置的全流程
- 🛠️ 初始设置包括安装、导入和核心组件初始化，附带可直接运行的代码片段
- 🌍 高级示例展示真实应用场景，如复杂工作流整合和外部数据源对接
- ⚙️ 配置选项支持模块开关、性能优化和默认行为定义，提供环境预设和参数微调
- 🎨 可视化定制涵盖动态颜色、多语言主题、布局调整和多种图表视图（地图/折线/日历）
- 📊 功能增强包括年度统计、缩放控制、标题栏按钮和可编辑趋势类型
- 🔧 细节优化提供显示计数、移除地图间隔、单视图模式等实用选项

---

### [GitHub - williamtroup/Heat.js: 🌞 一个高度可定制的 JavaScript 库，用于生成交互式热力图。它能将数据转化为平滑、视觉直观的热力层，让模式和强度一目了然。](https://github.com/williamtroup/Heat.js)

**原文标题**: [GitHub - williamtroup/Heat.js: 🌞 A highly customizable JavaScript library for generating interactive heatmaps. It transforms data into smooth, visually intuitive heat layers, making patterns and intensity easy to spot at a glance.](https://github.com/williamtroup/Heat.js)

Heat.js 是一个高度可定制的 JavaScript 库，用于生成交互式热力图，可将数据转换为平滑、直观的热力图层，便于快速识别数据模式和强度。

- 🌞 高度可定制且轻量级的 JavaScript 热力图生成库
- 🛠️ 提供 6 种视图模式：地图、折线、图表、日、月和颜色范围
- 🌈 支持 31 种默认主题（深色/浅色）和完整的 CSS 主题定制
- 📊 支持 9 种导出格式和 7 种导入格式，包括 CSV、JSON、XML 等
- 🌍 提供 60 种语言支持，适配多语言环境
- 📱 完全响应式设计，兼容 Bootstrap 等前端框架
- 🔧 基于 TypeScript 开发，提供完整的 API 和 React、Angular 等库的集成支持
- 📦 可通过 npm、CDN 或直接下载安装，部署简单快捷

---

### [MCP 服务器安全认证 — WorkOS](https://workos.com/mcp?utm_source=cpjavascript&utm_medium=referral&utm_campaign=q12026)

**原文标题**: [Secure auth for MCP servers — WorkOS](https://workos.com/mcp?utm_source=cpjavascript&utm_medium=referral&utm_campaign=q12026)

WorkOS AuthKit 为 MCP 服务器提供基于 OAuth 2.1 的安全授权解决方案，简化了为 AI 代理和应用添加身份验证与权限管理的过程。

- 🔐 **安全授权**：通过 OAuth 2.1 流程、工具权限、PKCE 和范围控制，为 MCP 服务器提供企业级安全认证。
- ⚡ **快速集成**：支持所有语言和框架，提供开源模板，可在 10 分钟内为 MCP 服务器添加身份验证功能。
- 🧩 **灵活兼容**：可作为独立的中间件运行，支持现有用户系统，无需迁移即可提供 MCP OAuth 流程。
- 📚 **丰富资源**：提供详细的文档、架构图、专家指南以及社区活动，帮助开发者深入掌握 MCP。
- 🛠️ **简化开发**：由 AuthKit 处理 OAuth 授权服务器的所有复杂性，开发者只需专注于构建 MCP 工具和资源端点。
- 🌐 **社区支持**：拥有活跃的 Discord 社区和定期活动，方便开发者交流项目并获取最新信息。

---

### [Croner - 概述](https://croner.56k.guru/)

**原文标题**: [Croner - Overview](https://croner.56k.guru/)

Croner 是一个用于 JavaScript 和 TypeScript 的无依赖、功能全面的 cron 表达式解析与任务调度库，支持 Node.js、Deno、Bun 及浏览器环境，并遵循 OCPS 规范提供高级特性。

- ⚙️ **功能全面**：支持触发函数、计算下次运行时间、时区设定、内置超时保护和错误处理，并兼容异步函数。
- 🚀 **跨平台运行**：可在 Node.js（≥18）、Deno（≥2）、Bun（≥1）和浏览器中作为独立、UMD 或 ES 模块使用。
- 📅 **高级语法支持**：完全遵循 OCPS 1.0-1.4，支持秒/年字段及 L（最后一天）、W（最近工作日）、#（第 n 次出现）和 +（AND 逻辑）等操作符。
- 🛡️ **内置保护机制**：提供任务超时防护和错误处理，支持暂停、恢复或停止已调度的任务。
- 📦 **零依赖与类型安全**：无需外部数据库或配置文件，包含 TypeScript 类型定义，被 pm2、Uptime Kuma 等知名项目使用。
- 🌐 **即时示例**：可每 5 秒运行任务、计算未来 100 个周日的日期、显示到特定日期的剩余天数，并支持指定时区运行。

---

### [cron - 维基百科](https://en.wikipedia.org/wiki/Cron#CRON_expression)

**原文标题**: [cron - Wikipedia](https://en.wikipedia.org/wiki/Cron#CRON_expression)

cron 是一个用于在 Unix 和类 Unix 操作系统中调度周期性任务的命令行工具，通过 crontab 文件配置任务执行时间，广泛应用于系统维护和任务自动化。

- ⏰ **基本功能**：cron 用于调度周期性任务（称为 cron 作业），通过 crontab 文件定义任务执行时间，语法包含五个时间字段（分钟、小时、日期、月份、星期）。
- 📁 **配置文件**：用户可编辑个人 crontab 文件，系统级 crontab 通常位于 `/etc/cron.d`，管理员可通过 `crontab -e` 命令修改配置。
- 🕐 **时间语法**：时间字段支持通配符（`*`）、范围（`-`）、列表（`,`）和步长（`/`），例如 `*/5 * * * *` 表示每 5 分钟执行一次。
- 🔧 **特殊宏**：部分实现支持非标准宏如 `@yearly`（每年一次）、`@monthly`（每月一次）、`@weekly`（每周一次）、`@daily`（每天一次）、`@hourly`（每小时一次）和 `@reboot`（启动时执行）。
- 👥 **权限管理**：通过 `/etc/cron.allow` 和 `/etc/cron.deny` 文件控制用户访问权限，若无这些文件则根据系统设置决定用户权限。
- 🌍 **时区处理**：cron 默认使用系统时区，但可通过 `CRON_TZ=<时区>` 在 crontab 中指定特定时区，适用于多时区环境。
- 📜 **历史发展**：cron 最初于 1975 年在 AT&T Bell 实验室开发，后续版本扩展了多用户支持，现代实现如 Vixie cron（用于 Linux）和 mcron（基于 Guile）增加了灵活性和功能。
- 🔄 **标准化**：2025 年发布的 Open Cron Pattern Specification (OCPS) 旨在统一不同实现的 cron 语法，提供向后兼容的规范。
- ⚙️ **高级特性**：部分实现支持额外字段（如秒或年份）和非标准字符（如 `L` 表示“最后”、`W` 表示最近工作日、`#` 表示第几周），用于复杂调度需求。
- 🔗 **相关工具**：类似工具包括 `at`（一次性任务调度）、`systemd timers`（系统服务调度）和 `Windows Task Scheduler`（Windows 任务调度）。

---

### [发布 10.0.0 版本 · Hexagon/croner · GitHub](https://github.com/Hexagon/croner/releases/tag/10.0.0)

**原文标题**: [Release 10.0.0 · Hexagon/croner · GitHub](https://github.com/Hexagon/croner/releases/tag/10.0.0)

Croner 10.0.0 是一个重大版本更新，实现了完整的 OCPS 1.4 合规性，引入了新的调度功能，并提升了可靠性。此次更新包含了对年份字段的支持、新的模式匹配方法、日期偏移功能、反向历史查询以及关键的错误修复。同时，它也引入了一些破坏性变更，如问号字符行为的改变和更严格的解析规则。

- 🎯 **OCPS 合规性**：全面支持 OCPS 1.2 至 1.4 标准，包括年份字段、W（工作日）修饰符、+（AND 逻辑）修饰符以及模式昵称。
- 🔍 **新功能方法**：新增 `match()` 方法用于检查日期是否匹配 cron 模式，`previousRuns()` 方法用于枚举过去的计划执行时间。
- 📅 **灵活调度**：引入 `dayOffset` 选项，支持相对于模式匹配日期的调度（如“前一天”或“后一天”）。
- 🛠️ **配置与控制**：新增 `mode` 选项以精确控制模式解析，`sloppyRanges` 选项用于保持与非标准语法的向后兼容性。
- ⚠️ **破坏性变更**：问号字符 `?` 现作为通配符别名（同 `*`）；最低 Deno 版本要求提升至 2.0；默认采用更严格的解析规则。
- 🐛 **关键修复**：解决了夏令时过渡期间可能导致重复执行或跳过小时的严重错误，并修复了其他多个问题。
- 📚 **文档与迁移**：提供了完整的 OCPS 合规文档和从 9.x 版本升级的详细迁移指南。

---

### [DayFlow - 产品团队日历工具包](https://dayflow-js.github.io/calendar/)

**原文标题**: [DayFlow - Calendar toolkit for product teams](https://dayflow-js.github.io/calendar/)

DayFlow 是一个轻量优雅的 React 全功能日历组件，专为产品团队设计，提供生产就绪的日历视图、拖放功能和模块化架构，帮助团队专注于产品开发而非日期计算。

- 📅 提供多种日历视图（日、周、月、年）和拖放事件功能
- ⚙️ 采用模块化架构，支持通过插件和钩子自定义界面
- 🚀 可直接在浏览器中试用，支持实时切换视图和探索插件
- 🎯 适用于产品团队、个人、学习、旅行、健康、营销和支持等多种场景
- 📦 提供详细文档和 GitHub 仓库，方便快速集成和定制

---

### [GitHub - dayflow-js/calendar: 一款轻量优雅的 React 全日历（或 React-big-calendar）网页组件，可轻松集成 shadcn-ui 或任何基于 Tailwind 的 UI 库 🌟 喜欢的话请点星支持！](https://github.com/dayflow-js/calendar)

**原文标题**: [GitHub - dayflow-js/calendar: A lightweight and elegant React full calendar(or React-big-calendar) component for the web, easily integrated with shadcn-ui or any Tailwind-based UI library 🌟 Star if you like it!](https://github.com/dayflow-js/calendar)

DayFlow 是一个轻量优雅的 React 日历组件库，支持多种视图和拖拽操作，易于与 Tailwind CSS 或 shadcn-ui 集成。

- 📅 提供月、周、日等多种视图类型，灵活展示日程安排
- 🎯 支持事件的拖拽调整和范围编辑，操作直观便捷
- 🧩 采用插件化架构，可扩展性强，便于自定义功能
- 🎨 专为 Tailwind CSS 设计，轻松适配 shadcn-ui 等现代 UI 库
- 🌐 已获得 253 个星标和 9 个分支，社区活跃度较高
- 📄 项目遵循 MIT 开源协议，欢迎提交问题报告和功能贡献

---

### [首页 | Tsonic](https://tsonic.org/)

**原文标题**: [Home | Tsonic](https://tsonic.org/)

Tsonic 是一款将 TypeScript 编译为 C# 并通过 .NET NativeAOT 生成原生可执行文件的编译器，允许开发者编写 TypeScript 代码并直接获得高性能的原生二进制文件。

- 🚀 **编译为原生二进制文件**：将 TypeScript 代码编译为无需 JavaScript 运行时的原生可执行文件，支持 x64 和 ARM64 架构。
- 🔧 **可选 JavaScript/Node API**：通过 `@tsonic/js` 和 `@tsonic/nodejs` 包按需启用 JavaScript 运行时或 Node.js 风格的 API。
- 📦 **直接访问 .NET 生态**：完整利用 .NET 基础类库（BCL），提供文件操作、网络、加密、并发等原生功能。
- ⚙️ **保留 TypeScript 特性**：代码仍可通过 `tsc` 进行类型检查，并支持 CLR 风格的数值类型（如 `int`、`uint`）。
- 🔒 **增强安全性**：基于广泛使用且定期更新的 .NET 运行时和标准库构建。
- 📁 **单文件可执行文件**：通过 NativeAOT 编译生成自包含的原生二进制文件，便于分发。
- 🛠️ **便捷的工具链**：提供 CLI 命令（如 `tsonic init`、`tsonic build`）和项目初始化模板，支持快速创建和构建项目。
- 🔗 **完整的 .NET 互操作**：可导入和使用任何 .NET 库，并支持通过 `tsbindgen` 自动生成 CLR 绑定。
- 📚 **模块化工作区**：基于 npm workspaces 支持多程序集仓库结构，每个项目可独立配置和输出。

---

### [GitHub - embedpdf/embed-pdf-viewer：一款能与任何JavaScript项目无缝集成的PDF查看器](https://github.com/embedpdf/embed-pdf-viewer)

**原文标题**: [GitHub - embedpdf/embed-pdf-viewer: A PDF viewer that seamlessly integrates with any JavaScript project](https://github.com/embedpdf/embed-pdf-viewer)

EmbedPDF 是一个开源的、与框架无关的 JavaScript PDF 查看器，可轻松集成到任何 JavaScript 项目中，提供流畅的阅读体验和简洁的开发者 API。

- 📄 **开源项目**：一个 MIT 许可的 PDF 查看器，拥有 3.3k 星标和 180 个分支。
- 🔌 **框架无关**：可无缝集成到 React、Vue、Svelte、Preact 或原生 JavaScript 项目中。
- ✨ **丰富功能**：支持标注、真实内容擦除、搜索、文本选择、缩放、旋转和虚拟化滚动。
- 📚 **完整文档**：提供详细的安装指南、API 参考和示例，文档网站为 embedpdf.com。
- 🚀 **在线演示**：可通过 app.embedpdf.com 立即体验，支持上传自有 PDF 或使用示例文件。
- 🤝 **欢迎贡献**：项目鼓励社区贡献，提供贡献指南和 GitHub 讨论区供交流。
- ⚖️ **许可信息**：项目基于 MIT 许可证，并包含遵循 Apache 2.0 许可的 PDFium 组件。

---

### [嵌入 PDF](https://app.embedpdf.com/)

**原文标题**: [EmbedPDF](https://app.embedpdf.com/)

本文介绍了人工智能在医疗领域的应用现状与前景，重点探讨了其在疾病诊断、治疗方案优化及医疗管理效率提升方面的作用，同时简要提及了相关的伦理挑战。

- 🩺 AI 在医学影像分析中表现出色，能辅助医生更早、更准确地识别肿瘤等病变
- 💊 通过分析患者数据，人工智能可帮助制定个性化治疗方案，提高治疗效果
- ⚙️ 智能系统能优化医院资源分配，简化管理流程，降低运营成本
- 🤖 机器人辅助手术日益普及，提升复杂手术的精确度与安全性
- 🧬 在基因组学和药物研发中，AI 加速了新药发现和靶点识别过程
- ⚖️ 应用同时面临数据隐私、算法偏见等伦理与监管方面的挑战

---

### [GitHub - swiftwasm/JavaScriptKit：通过WebAssembly与JavaScript交互的Swift框架。](https://github.com/swiftwasm/JavaScriptKit)

**原文标题**: [GitHub - swiftwasm/JavaScriptKit: Swift framework to interact with JavaScript through WebAssembly.](https://github.com/swiftwasm/JavaScriptKit)

JavaScriptKit 是一个 Swift 框架，用于在 WebAssembly 环境中与 JavaScript 进行交互，提供类型安全和便捷的互操作功能。

- 🚀 **快速开始**：提供 Hello World 教程，帮助开发者快速上手。
- 🔗 **核心功能**：支持访问 JavaScript 对象和函数、创建可从 JavaScript 调用的闭包、数据类型转换，以及使用 async/await 处理 JavaScript Promise。
- 🧩 **BridgeJS 插件**：实验性功能，支持将 Swift API 导出到 JavaScript，并从 TypeScript 导入 API 到 Swift，实现双向类型安全互操作。
- 📚 **示例丰富**：包含多个示例，展示不同使用模式和场景。
- 🤝 **开源贡献**：欢迎社区贡献，提供详细的贡献指南（CONTRIBUTING.md）。
- ⭐ **项目活跃**：拥有 844 个星标、63 个分支，采用 MIT 许可证，支持多线程操作。

---

### [GitHub - flozz/StackBlur: 快速且近似高斯模糊](https://github.com/flozz/StackBlur)

**原文标题**: [GitHub - flozz/StackBlur: Fast and almost Gaussian blur](https://github.com/flozz/StackBlur)

StackBlur 是一个快速且近似高斯模糊的 JavaScript 库，适用于图像和画布处理，支持多种使用方式和 API 调用。

- 🚀 **快速近似高斯模糊**：提供高效的模糊算法，接近高斯模糊效果。
- 📦 **多平台支持**：可在浏览器中作为独立脚本使用，也支持 Node.js 和 ES6 模块导入。
- 🛠️ **灵活的 API**：支持从图像、画布或 ImageData 进行模糊处理，并区分 RGBA 和 RGB 模式。
- 📚 **详细文档**：包含完整的 API 说明和示例，便于开发者集成和使用。
- 🔧 **易于构建**：使用 Rollup 构建工具，修改源代码后可快速重新生成分发文件。
- 📄 **开源许可**：基于 MIT 许可证发布，可自由使用和修改。

---

### [精简你的 JavaScript 与 TypeScript 项目 | Knip](https://knip.dev/)

**原文标题**: [Declutter your JavaScript & TypeScript projects | Knip](https://knip.dev/)

Knip 是一款用于 JavaScript 和 TypeScript 项目的自动化工具，旨在通过检测和清理未使用的依赖、导出和文件来优化代码库，提升项目性能和可维护性。

- 🧹 **清理未使用项**：自动发现并移除项目中未使用的依赖、导出和文件，减少代码冗余。
- 🛠️ **广泛兼容性**：提供 100 多个插件，支持 Astro、Next.js、Vite 等主流框架和工具。
- 🧪 **实战验证**：已在数千个项目中应用，效果显著，如帮助 Vercel 删除约 30 万行未使用代码。
- 🎯 **精准分析**：基于项目实际入口点进行高级分析，确保结果准确且可操作，极少误报。
- 🌐 **社区认可**：受到 Shopify 等顶级团队及众多开发者的高度评价，被誉为代码维护的“必备工具”。
- 🆓 **开源免费**：项目基于 ISC 许可证开源，提供在线 Playground 和详细文档，便于快速上手。

---

### [GitHub - parallax/jsPDF：面向所有人的客户端JavaScript PDF 生成工具。](https://github.com/parallax/jsPDF)

**原文标题**: [GitHub - parallax/jsPDF: Client-side JavaScript PDF generation for everyone.](https://github.com/parallax/jsPDF)

jsPDF 是一个客户端 JavaScript 库，用于在浏览器中生成 PDF 文档，支持多种模块格式和高级功能，并拥有活跃的开源社区。

- 📄 **客户端 PDF 生成**：纯 JavaScript 库，可在浏览器中直接创建和保存 PDF 文件。
- 📦 **多种安装方式**：可通过 npm、yarn 安装，或从 CDN 加载，支持 ES 模块、UMD 和 Node.js 版本。
- ⚙️ **灵活配置**：可自定义页面大小、方向和单位，并支持添加自定义字体以显示 UTF-8 字符。
- 🔒 **安全提示**：建议对用户输入进行清理，并提供 Node.js 环境下的文件读取权限管理方案。
- 🔧 **高级功能**：提供两种 API 模式（兼容模式和高级模式），支持矩阵变换、图案等高级特性。
- 🌐 **社区与支持**：拥有丰富的文档、在线演示和活跃的 Stack Overflow 社区，欢迎贡献代码和报告问题。
- 📜 **开源许可**：基于 MIT 许可证开源，由 James Hall 和 yWorks GmbH 等多个贡献者维护。

---

### [jsPDF - 使用 HTML5 JavaScript 库创建 PDF 文件](https://raw.githack.com/MrRio/jsPDF/master/index.html)

**原文标题**: [jsPDF - Create PDFs with HTML5 JavaScript Library](https://raw.githack.com/MrRio/jsPDF/master/index.html)

一款用于在浏览器中生成 PDF 的 HTML5 JavaScript 库，无需服务器支持，适用于创建票据、报告、证书等多种文档。

- 📄 基于 HTML5 的客户端 PDF 生成方案
- 🎫 适用于活动票据、报告、证书等文档制作
- 🌐 纯前端实现，无需服务器参与
- 🔧 提供在线演示和代码运行功能
- 📥 支持即时下载生成的 PDF 文件
- 🔄 可设置代码自动刷新选项

---

### [GitHub - scopewu/qrcode.vue: 一款支持 Vue 2 和 Vue 3 的二维码生成组件。](https://github.com/scopewu/qrcode.vue)

**原文标题**: [GitHub - scopewu/qrcode.vue: A Vue component to generate qrcode. Supports both Vue 2 and Vue 3. 一款同时支援 Vue 2 和 Vue 3 的二维码组件。](https://github.com/scopewu/qrcode.vue)

这是一个用于 Vue.js 的二维码生成组件，支持 Vue 2 和 Vue 3，提供丰富的自定义选项，包括颜色、渐变、Logo 图片等。

- 🎯 **支持 Vue 2 和 Vue 3** - 明确区分版本使用，Vue 3 需使用 3.x 版本，Vue 2 则使用 1.x 版本。
- 📦 **易于安装与使用** - 可通过 npm 或 yarn 安装，并提供了多种导入和使用方式，包括单文件组件和 TypeScript 支持。
- 🎨 **高度可定制** - 提供多种属性来自定义二维码，如尺寸、纠错等级、背景/前景色、边距、渲染方式（Canvas 或 SVG）等。
- 🖼️ **支持 Logo 与渐变** - 可通过 `image-settings` 属性在二维码中心添加 Logo，并支持线性或径向渐变填充。
- 📄 **组件化导出** - 从 3.5 版本起，除了默认的 `QrcodeVue` 组件，还单独导出了 `QrcodeCanvas` 和 `QrcodeSvg` 组件，以满足不同使用场景。
- 📖 **完善的文档** - 提供了详细的属性说明、使用示例，并包含中文、日文等多语言 README。
- ⚖️ **开源许可** - 项目基于 MIT 许可证开源，代码托管在 GitHub 上，拥有活跃的社区（802 个星标，91 个复刻）。

---

### [GitHub - focus-trap/focus-trap: 将焦点限制在 DOM 节点内。](https://github.com/focus-trap/focus-trap)

**原文标题**: [GitHub - focus-trap/focus-trap: Trap focus within a DOM node.](https://github.com/focus-trap/focus-trap)

focus-trap 是一个用于在 DOM 节点内捕获焦点的 JavaScript 库，主要用于构建无障碍模态框等交互组件，确保用户无法通过 Tab 键或点击操作跳出指定的焦点循环区域。

- 🎯 **核心功能**：将焦点限制在指定的 DOM 节点内，防止用户通过 Tab、Shift+Tab 或点击操作跳出该区域。
- 🛠️ **使用场景**：常用于实现无障碍模态框，确保交互内容可访问且符合用户体验规范。
- 📦 **安装方式**：支持 npm 安装、UMD 脚本引入，并可搭配 React 封装库 focus-trap-react 使用。
- 🌐 **浏览器兼容**：支持主流桌面浏览器（Chrome、Edge、Firefox、Safari、Opera），需注意 Safari 需启用特定设置才能正常使用。
- ⚙️ **配置选项**：提供丰富的配置参数，如初始焦点设置、外部点击处理、ESC 键行为控制、焦点返回逻辑等。
- 🔄 **操作方法**：支持激活（activate）、暂停（pause）、恢复（unpause）、更新容器元素（updateContainerElements）等动态操作。
- ⚠️ **注意事项**：避免在 Shadow DOM 内使用选择器字符串，谨慎处理正数 tabindex 和多容器陷阱的兼容性问题。
- 🧪 **开发与测试**：推荐使用 Cypress 等完整浏览器环境进行测试，JSDom 支持有限且需额外配置。
- 🤝 **贡献与支持**：项目遵循 MIT 许可，欢迎社区贡献，已获得大量开发者维护和优化。

---

### [焦点陷阱演示](https://focus-trap.github.io/focus-trap/)

**原文标题**: [focus-trap demo](https://focus-trap.github.io/focus-trap/)

本文档展示了 focus-trap 库的各种功能演示，涵盖基础用法、动画效果、配置选项、特殊场景及高级功能，帮助用户理解如何在不同情境下实现和管理焦点陷阱。

- 🎯 默认行为：演示基础焦点陷阱的激活与停用，通过按钮或 Escape 键控制。
- 🎭 动画效果：支持激活/停用时的淡入淡出动画，需用户自定义实现。
- ⚙️ 可配置选项：包括初始焦点设置、Escape 键行为、外部点击处理等灵活配置。
- 🧩 特殊场景：处理嵌套陷阱、隐藏元素、iframe、Shadow DOM 等复杂结构。
- 🔧 高级功能：支持多元素陷阱、动态焦点控制、自定义键盘导航等进阶用法。
- 📱 浏览器适配：针对不同浏览器和操作系统（如 macOS 键盘导航）提供兼容性说明。

---

### [探索解决 GitHub 低质量贡献的方案 · 社区 · 讨论 #185387 · GitHub](https://github.com/orgs/community/discussions/185387)

**原文标题**: [Exploring Solutions to Tackle Low-Quality Contributions on GitHub · community · Discussion #185387 · GitHub](https://github.com/orgs/community/discussions/185387)

GitHub 正在探索应对低质量贡献的解决方案，以减轻维护者的运营负担，包括短期措施如可配置的拉取请求权限和从界面删除 PR 的功能，以及长期方向如增强权限模型、改进分类工具和 AI 辅助贡献的透明度。

- 🔧 **可配置的拉取请求权限**：允许仓库所有者更精细地控制 PR 访问，例如限制仅协作者可提交或针对镜像仓库禁用 PR。
- 🗑️ **从界面删除 PR**：维护者可直接删除垃圾或低质量 PR，以改善仓库组织。
- 🛡️ **增强权限模型**：探索更精细的控制，例如定义 PR 必须满足的标准才能被创建。
- 🤖 **改进分类工具**：可能利用 AI 评估贡献是否符合项目指南，帮助维护者优先审查。
- 🔍 **AI 辅助贡献的透明度**：提升 AI 工具在 PR 生命周期中使用的可见性和归属。
- 📝 **社区反馈与探索**：GitHub 鼓励用户分享反馈，并继续研究即时改进和长期解决方案。

---

### [限制单个网络请求 | 博客 | Chrome 开发者](https://developer.chrome.com/blog/throttle-individual-network-requests)

**原文标题**: [Throttle individual network requests  |  Blog  |  Chrome for Developers](https://developer.chrome.com/blog/throttle-individual-network-requests)

Chrome 145 开发者工具新增了针对单个网络请求进行节流或阻塞的功能，使开发者能更精确地模拟特定资源（如缓慢的第三方 API 或大图）的加载情况，而无需降低整个页面的速度。

- 🛠️ **新增功能**：Chrome 145 开发者工具现支持对单个网络请求进行节流或阻塞，取代了过去只能全局节流或完全阻塞请求的限制。
- 📁 **操作位置**：在“网络”面板中右键点击任一请求，即可选择“阻塞请求”或“节流请求”，操作会自动打开“请求条件”抽屉并创建相应规则。
- ⚙️ **自定义设置**：在“请求条件”抽屉中，可使用预设（如慢速 3G）或自定义配置文件，并通过通配符编辑 URL 模式来针对特定资源或请求组。
- 🚦 **规则优先级**：若请求匹配多个模式，开发者工具会应用找到的第一条规则；可使用抽屉中的箭头按钮调整规则优先级顺序。
- 🟡 **识别效果**：被节流的请求在“网络”面板中显示为黄色/金色，时间列带时钟图标；被阻塞的请求显示为红色，状态列为“(blocked:devtools)”。
- 📊 **性能影响**：节流请求会影响页面性能；在录制性能配置文件时，可将鼠标悬停在网络轨道的请求上查看具体应用的网络条件详情。

---

### [介绍 Codex 应用 | OpenAI](https://openai.com/index/introducing-the-codex-app/)

**原文标题**: [Introducing the Codex app | OpenAI](https://openai.com/index/introducing-the-codex-app/)

OpenAI 推出专为 macOS 设计的 Codex 应用程序，这是一个强大的新界面，旨在同时管理多个智能体、并行处理任务，并支持在长时间运行的任务中与智能体协作。该应用改变了软件的构建方式和构建者范围，从与单个编码智能体进行针对性编辑，到监督协调的智能体团队，涵盖软件设计、构建、发布和维护的全生命周期。此外，OpenAI 宣布限时向 ChatGPT Free 和 Go 用户提供 Codex，并为付费计划用户加倍速率限制。

- 🖥️ **Codex 应用程序发布**：推出 macOS 版 Codex 应用，作为智能体的指挥中心，支持并行管理多个智能体、长时间任务协作和项目线程切换。
- 🔄 **并行工作与技能扩展**：应用支持多智能体并行工作，使用工作树避免冲突，并通过“技能”功能扩展 Codex 能力，使其超越代码生成，涵盖信息收集、问题解决和写作等任务。
- 🎮 **智能体能力展示**：Codex 利用图像生成和网页游戏开发技能，独立创建了一款名为“Voxel Velocity”的 3D 体素卡丁车赛车游戏，展示了其在复杂项目中的端到端处理能力。
- 📚 **内置技能库与自动化**：应用包含 OpenAI 内部流行的工具和工作流技能库，如 Figma 设计实现、Linear 项目管理等，并支持设置自动化任务，让 Codex 按计划在后台处理重复性工作。
- ⚙️ **个性化与安全性**：开发者可选择智能体的交互风格（简洁务实或对话共情），且应用默认集成安全沙箱，限制文件编辑和权限，支持配置规则以确保安全可控的使用环境。
- 💻 **可用性与定价**：Codex 应用现已上线 macOS，ChatGPT 付费订阅用户可直接使用，限时向免费用户开放，并加倍所有付费计划的速率限制，未来计划扩展至 Windows 平台。

---

### [未找到标题](https://x.com/robzolkos/status/2018412778965315965)

**原文标题**: [No title found](https://x.com/robzolkos/status/2018412778965315965)

该页面提示用户浏览器中 JavaScript 功能未启用或存在兼容性问题，导致无法正常使用 X 平台（原 Twitter），并提供了相应的解决建议。

- 🚫 JavaScript 未启用导致功能受限
- 🌐 建议启用 JavaScript 或更换受支持的浏览器
- 📖 支持浏览器列表可在帮助中心查询
- 🔧 部分隐私扩展可能引发冲突，建议暂时禁用
- 🔄 页面提供“重试”功能供用户再次尝试访问

---

### [错误](https://javascriptweekly.com/link/180159/web)

**原文标题**: [Error](https://javascriptweekly.com/link/180159/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='notepad-plus-plus.org', port=443): Max retries exceeded with url: / (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1000)')))

---

### [错误](https://javascriptweekly.com/link/180160/web)

**原文标题**: [Error](https://javascriptweekly.com/link/180160/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='notepad-plus-plus.org', port=443): Max retries exceeded with url: /news/hijacked-incident-info-update/ (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1000)')))

---

### [GitHub - BCsabaEngine/svelteesp32：将任意Web应用嵌入ESP32——单一二进制文件，零文件系统困扰 将您的 Svelte、React、Angular 或 Vue 前端转换为单个 C++ 头文件。通过自动 gzip 压缩、ETag 缓存和无缝 OTA 更新，直接从 ESP32/ESP8266 闪存提供精美的 Web 界面。](https://github.com/BCsabaEngine/svelteesp32)

**原文标题**: [GitHub - BCsabaEngine/svelteesp32: Embed Any Web App in Your ESP32 — One Binary, Zero Filesystem Hassle Turn your Svelte, React, Angular, or Vue frontend into a single C++ header file. Serve beautiful web interfaces directly from ESP32/ESP8266 flash memory with automatic gzip compression, ETag caching, and seamless OTA updates.](https://github.com/BCsabaEngine/svelteesp32)

SvelteESP32 是一个开源工具，可将 Svelte、React、Angular 或 Vue 等前端应用编译成单个 C++ 头文件，并直接嵌入 ESP32/ESP8266 固件中，实现无需文件系统的 Web 界面服务。

- 🚀 **一键嵌入前端**：将整个 Web 应用打包成单个 C++ 头文件，简化固件部署和 OTA 更新流程。
- ⚡ **自动优化与压缩**：构建时自动对大于 1KB 且压缩率超过 15% 的文件进行 gzip 压缩，减少传输体积。
- 🏷️ **智能缓存支持**：内置 SHA256 ETag 验证，支持 HTTP 304 响应，显著节省带宽。
- 🔧 **多引擎兼容**：支持 PsychicHttp V1/V2、ESPAsyncWebServer 和原生 ESP-IDF 四种 Web 服务器引擎。
- 📦 **零运行时开销**：资源直接存储在 Flash 中，无需文件系统读取，不占用额外 RAM。
- 🛠️ **便捷集成**：提供 CLI 工具和配置文件，轻松融入 CI/CD 流程，支持文件排除、多前端路径等高级功能。

---

