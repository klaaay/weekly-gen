### [JavaScript 周刊第 782 期：2026 年 4 月 21 日](https://javascriptweekly.com/issues/782)

**原文标题**: [JavaScript Weekly Issue 782: April 21, 2026](https://javascriptweekly.com/issues/782)

本期的 JavaScript Weekly 涵盖了视频框架、安全事件、工具更新和最佳实践等内容。

- 🎬 **HyperFrames**：一个开源框架，允许使用 HTML 和 JavaScript 创建和渲染视频，是 Remotion 的轻量替代方案，内置多种视频效果组件。
- 🔒 **Vercel 安全事件**：因员工使用捆绑了 Roblox 作弊软件的第三方工具，导致 OAuth 授权被利用，部分客户环境变量泄露，提醒用户注意第三方工具授权风险。
- 📅 **Node.js 即将默认支持 Temporal API**：预计在 Node v26 中实现，该版本有望下周发布。
- 🚀 **Bun v1.3.13 发布**：改进了测试功能（支持 --isolate、--parallel 等选项），减少 5% 内存使用，并优化了安装速度。
- 📖 **解决 15K 循环依赖**：一位微软工程师分享了在 700 万行 TypeScript 单体仓库中清除约 15,000 个循环依赖的经验，提供了可复用的思路。
- 🧩 **垂直代码库架构**：Dominik Dorfmeister 提倡按领域而非功能（如 components/、hooks/）组织代码，以提升可维护性。
- 🔧 **Angular 编译器加速**：VoidZero 团队利用 AI 技术大幅提升了 Angular 编译器的速度。
- 🎨 **Animata**：一个包含 100 多个动画 React 组件的库，提供光束动画、展开卡片等新颖效果。
- 📝 **officeParser**：一个用于解析 docx、pptx、xlsx 等办公文档格式的库，支持浏览器和服务端使用。
- 🎵 **tiks**：一个使用 Web Audio API 合成点击、弹出等 UI 声音的微型库。
- 🛡️ **OWASP NPM 安全最佳实践**：一份持续更新的清单，涵盖禁用生命周期脚本、防域名抢注、依赖混淆等安全建议。
- 📰 **Git 2.54 发布**：新增 `git history` 命令以轻松编辑提交信息，支持在配置文件中定义钩子，并允许为同一事件运行多个钩子。
- 💡 **虚假星标经济**：分析指出 GitHub 上存在大量付费虚假星标项目，提醒开发者注意项目真实热度。

---

### [HyperFrames — 通过氛围编码编辑视频](https://hyperframes.heygen.com/)

**原文标题**: [HyperFrames — Edit Videos By Vibe-Coding](https://hyperframes.heygen.com/)

HyperFrames 让 AI 代理通过编写 HTML、CSS 和 JS 来创作视频，采用 Apache 2.0 开源许可。

- 🎬 HyperFrames 允许 AI 代理通过编写 HTML、CSS 和 JS 来合成视频。
- 🔓 项目采用 Apache 2.0 开源许可。
- 🚀 提供“Get Started”快速上手入口。
- 📄 包含示例文件 `compositions/product-promo.html`，如“Product Promo”。
- 🤖 支持通过 Claude Code 编辑视频，安装命令为 `npx skills add heygen-com/hyperframes`。

---

### [Remotion | 以编程方式制作视频](https://www.remotion.dev/)

**原文标题**: [Remotion | Make videos programmatically](https://www.remotion.dev/)

📹 Remotion 是一个用 React 代码编程生成 MP4 视频的工具，支持服务器端渲染和动态参数化。

- 🎬 使用 React 创建专业级 MP4 视频，支持代码编程和模板化
- ⚙️ 动态编辑：通过传递数据参数化视频内容，或嵌入应用构建界面
- 🚀 可扩展渲染：支持本地、服务器或无服务器渲染为 .mp4 等格式
- 🎨 应用场景：音乐可视化、字幕、屏幕录制、年度回顾等
- 💰 定价分层：免费版（个人及3人以下团队）、公司版（4人以上）、创作者版（$25/月/席位）、自动化版（$100/月起）、企业版（$500/月起）
- 🌐 社区支持：44000 GitHub 星标、8000+ Discord 成员、300+ 贡献者、800页文档
- 🛠️ 提供 Editor Starter 模板，用于构建自定义视频编辑应用

---

### [Instagram 关注 - HyperFrames](https://hyperframes.heygen.com/catalog/blocks/instagram-follow)

**原文标题**: [Instagram Follow - HyperFrames](https://hyperframes.heygen.com/catalog/blocks/instagram-follow)

该页面是HyperFrames平台的文档，提供多种动画组件和过渡效果，重点介绍了Instagram关注叠加组件的安装、属性、文件和使用方法。

- 🏠 **平台概述**：HyperFrames提供社交叠加、着色器过渡、CSS过渡等动画组件，支持搜索和AI查询功能。
- 📱 **社交叠加组件**：包括Instagram关注、macOS通知、Reddit帖子卡片、Spotify播放中、TikTok关注、X帖子卡片和YouTube底部三分等。
- 🎨 **着色器过渡效果**：包含色散、电影变焦、交叉扭曲、闪光、故障、引力透镜、光泄漏、波纹、漩涡、热变形等20种视觉效果。
- 🔄 **CSS过渡分类**：涵盖3D、模糊、覆盖、破坏、溶解、扭曲、网格、灯光、机械、推动、径向和缩放等12种过渡类型。
- 📊 **其他功能**：提供应用展示、3D UI展示、数据图表、颗粒覆盖、像素擦除、闪光扫掠、流程图和Logo结尾等模块。
- 📝 **Instagram关注组件**：动画化的Instagram关注叠加，包含个人资料卡片和关注按钮，尺寸为1080×1920，时长4.5秒。
- ⚙️ **安装与使用**：通过命令`npx hyperframes add instagram-follow`安装，包含HTML文件和头像图片，使用时需在宿主组件中添加特定数据属性。

---

### [作品 - 超帧](https://hyperframes.heygen.com/concepts/compositions)

**原文标题**: [Compositions - HyperFrames](https://hyperframes.heygen.com/concepts/compositions)

HyperFrames 中的 Compositions 是构建视频的基本单元，每个 Composition 都是一个定义视频时间线的 HTML 文档。

- 📄 **核心结构**：每个 Composition 需要一个带有 `data-composition-id` 的根元素，`index.html` 是顶层 Composition，可包含嵌套 Composition。
- 🎬 **片段类型**：视频、图片、音频和嵌套 Composition 都作为 HTML 元素存在，通过 `data attributes` 定义时间线行为。
- 🔄 **嵌套 Composition**：可通过外部文件（推荐）或内联方式嵌入，外部文件使用 `data-composition-src` 引用，内联则直接写在父元素中。
- 🏗️ **项目结构**：典型项目包含 `index.html` 和 `compositions/` 文件夹，用于存放可复用的 Composition 文件。
- 🧩 **双层架构**：HTML 层负责声明式媒体播放（由框架自动管理），脚本层（如 GSAP）仅负责动画和创意效果，不应控制媒体播放。
- 📝 **变量传递**：通过 `data-variable-values` 为 Composition 传递自定义值，在脚本中读取并应用到 DOM 或 CSS 中。
- 🔍 **列出 Compositions**：使用 CLI 命令 `npx hyperframes compositions` 可查看项目中所有 Composition。

---

### [GitHub - heygen-com/hyperframes: 编写HTML，渲染视频，为智能体而生。](https://github.com/heygen-com/hyperframes#readme)

**原文标题**: [GitHub - heygen-com/hyperframes: Write HTML. Render video. Built for agents. · GitHub](https://github.com/heygen-com/hyperframes#readme)

Hyperframes 是一个开源视频渲染框架，支持用 HTML 编写视频，并针对 AI 代理进行了优化。

- 🎬 **核心功能**：通过 HTML 和 GSAP 动画创建、预览和渲染视频，无需构建步骤，支持实时预览和 MP4 输出
- 🤖 **AI 集成**：为 AI 代理（如 Claude、Cursor、Codex）提供技能包，可通过自然语言描述生成视频，支持迭代编辑
- 📦 **丰富组件库**：包含 50+ 即用型模块（社交覆盖、着色器过渡、数据可视化等），可通过 `npx hyperframes add` 安装
- ⚙️ **工作原理**：使用 HTML 数据属性定义视频元素（视频、图片、音频），通过 Puppeteer + FFmpeg 确定性渲染
- 🔄 **与 Remotion 对比**：采用 HTML 而非 React，完全开源（Apache 2.0），无需许可费用，适合商业使用
- 📚 **多包架构**：包含 CLI、核心库、引擎、播放器、编辑器 UI 等独立包，支持 WebGL 着色器过渡
- 🚀 **快速入门**：支持通过 AI 代理或手动 `npx hyperframes init` 启动项目，需 Node.js >= 22 和 FFmpeg

---

### [Meticulous AI - 无需编写测试的自动化前端测试](https://www.meticulous.ai/?utm_source=jsweekly&utm_medium=referral&utm_campaign=26q2&utm_content=primary)

**原文标题**: [Meticulous AI - Automated Frontend Testing Without Writing Tests](https://www.meticulous.ai/?utm_source=jsweekly&utm_medium=referral&utm_campaign=26q2&utm_content=primary)

Meticulous AI 是一款自动化、全面且确定性的测试工具，旨在帮助开发团队以AI编写代码的速度发布代码，无需手动编写、修复或维护测试用例。

- 🤖 **AI 驱动测试生成**：通过记录开发环境中的日常交互，AI引擎自动生成覆盖所有代码分支和用户流程的端到端测试，并随应用演变而更新。
- ⚡ **闪电般快速**：测试在计算集群上高度并行化，可在120秒内完成数千个屏幕的测试，大幅提升发布速度。
- 🚫 **彻底消除不稳定测试**：基于Chromium构建的确定性调度引擎，从根源上杜绝测试结果不稳定的问题，并支持极速执行。
- 🔌 **无缝集成与易用性**：只需添加脚本标签到本地开发、预发布或预览URL环境，即可开始录制；支持NextJS、React、Vue、Angular等主流框架。
- 🛡️ **无副作用测试**：默认模拟后端响应，通过保存和重放原始记录，避免因数据变化导致的误报，无需特殊测试账户或模拟数据。
- 💼 **企业级信任**：被超过100家组织（包括Dropbox和Notion）采用，工程师反馈“无需再调试合并后的代码，零维护，无不稳定测试”。
- 🔄 **灵活兼容**：可补充或完全替代现有测试套件，自动添加新测试、移除过时测试，确保测试套件始终完整且最新。

---

### [Vercel 2026年4月安全事件 | Vercel知识库](https://vercel.com/kb/bulletin/vercel-april-2026-security-incident)

**原文标题**: [Vercel April 2026 security incident | Vercel Knowledge Base](https://vercel.com/kb/bulletin/vercel-april-2026-security-incident)

### 概述总结
Vercel 在2026年4月遭遇一起安全事件，涉及未经授权访问其内部系统。攻击源于第三方AI工具Context.ai被入侵，导致一名员工的Vercel账户被接管，进而访问并解密了非敏感环境变量。Vercel已展开调查、通知受影响客户，并发布安全建议和IOC。

- 🔒 **事件概述**：Vercel于2026年4月发生安全事件，攻击者通过第三方AI工具入侵员工账户，访问内部系统并解密非敏感环境变量。
- 🕵️ **攻击来源**：事件起源于Context.ai（第三方AI工具）被攻破，攻击者利用该访问权限接管了员工的Google Workspace和Vercel账户。
- 📊 **受影响范围**：最初发现少量客户的非敏感环境变量被泄露，后续调查又发现少量额外账户受影响，但部分迹象显示与本次事件无关。
- ✅ **npm包安全**：经与GitHub、Microsoft等合作确认，Vercel发布的npm包未被篡改，供应链安全。
- 🛡️ **安全建议**：建议用户启用多因素认证、审查并轮换环境变量（尤其是非敏感变量）、检查活动日志和部署记录，并设置部署保护。
- 🔍 **IOC信息**：公布了一个Google Workspace OAuth应用ID，用于检测潜在恶意活动。
- 🚀 **产品增强**：Vercel正在推出环境变量管理、活动日志等安全功能更新，帮助用户加强防护。

---

### [一个Roblox作弊工具和一个AI工具如何导致Vercel整个平台崩溃 | techwizardrino | Webmatrices](https://webmatrices.com/post/how-a-roblox-cheat-and-one-ai-tool-brought-down-vercel-s-entire-platform)

**原文标题**: [how a roblox cheat and one AI tool brought down vercel's entire platform | techwizardrino | Webmatrices](https://webmatrices.com/post/how-a-roblox-cheat-and-one-ai-tool-brought-down-vercel-s-entire-platform)

### 概述总结
- 🎮 一篇关于Vercel安全事件的深度分析：起因于一名员工下载Roblox作弊软件，导致Lumma Stealer窃取凭证，最终攻击者通过Context.ai的OAuth权限入侵Vercel内部系统，获取了非敏感环境变量。
- 🔐 Vercel的环境变量加密机制存在隐患：非敏感变量可通过后端解密，而敏感变量仅构建时可读。攻击者利用了默认非敏感设置，导致大量未标记为“敏感”的密钥暴露。
- 🤖 AI工具授权是安全漏洞的放大器：每个AI工具都需要广泛权限，用户往往不阅读权限就点击授权。作者发现自己已授权23个OAuth应用，其中9个拥有完全邮件和Drive访问权。
- ⏱️ 事件修复成本巨大：每个Vercel项目需要6+小时轮换密钥，预计全球开发者将耗费数百万小时。攻击者正在出售数据，加密货币项目受影响严重。
- 🔄 安全与便利的永恒矛盾：尽管有AWS Secrets Manager等安全方案，但用户仍倾向于使用便捷的文本字段。作者提出“12倍审计”原则：对每个AI工具授权前花2分钟阅读权限，而非10秒。
- 💥 讽刺的是，攻击并非源于高级漏洞，而是一个游戏作弊软件。这揭示了整个AI工具行业的核心产品其实是“便利性”，而非真正的安全。

---

### [Vercel 2026年4月安全事件 | Vercel 知识库](https://vercel.com/kb/bulletin/vercel-april-2026-security-incident#recommendations)

**原文标题**: [Vercel April 2026 security incident | Vercel Knowledge Base](https://vercel.com/kb/bulletin/vercel-april-2026-security-incident#recommendations)

### 概述总结
Vercel在2026年4月遭遇了一起安全事件，涉及对某些内部系统的未授权访问。攻击源于第三方AI工具Context.ai的入侵，导致一名员工的Google Workspace账户被接管，进而访问了Vercel环境并解密了非敏感环境变量。Vercel已展开调查，通知了受影响客户，并发布了安全建议和入侵指标。

- 🔒 **事件起源**：攻击始于第三方AI工具Context.ai的入侵，攻击者利用其访问权限接管了Vercel员工的Google Workspace账户。
- 🕵️ **攻击范围**：攻击者通过员工账户进入Vercel环境，枚举并解密了非敏感环境变量，但未影响npm包或供应链安全。
- 📢 **受影响用户**：最初少数客户的环境变量被泄露，后续调查发现少量额外账户被入侵，但部分迹象显示与本次事件无关。
- 🛡️ **安全建议**：建议启用多因素认证、轮换非敏感环境变量、审查活动日志和部署记录，并设置敏感环境变量保护。
- 🔍 **入侵指标**：发布了OAuth应用ID（`110671459871-30f1spbu0hptbs60cb4vsmv79i7bbvqj.apps.googleusercontent.com`），供社区排查潜在恶意活动。
- 🚀 **产品改进**：Vercel正在推出增强的环境变量管理、活动日志和团队安全概览功能，以提升安全防护。

---

### [构建：默认启用 Temporal —— 来自 richardlau 的拉取请求 #61806 · nodejs/node · GitHub](https://github.com/nodejs/node/pull/61806)

**原文标题**: [build: enable Temporal by default by richardlau · Pull Request #61806 · nodejs/node · GitHub](https://github.com/nodejs/node/pull/61806)

Node.js 已默认启用 Temporal 支持，但需要 Rust 工具链。

- 🎯 默认启用 Temporal：Node.js 现在默认启用 Temporal API，但需要 `cargo` 和 `rustc` 工具链。
- ⚙️ 新增配置选项：添加 `--v8-disable-temporal-support` 选项可显式禁用 Temporal，无需 Rust。
- 🔍 自动检测机制：若未指定选项，`configure.py` 会自动检测 `cargo` 和 `rustc`，存在则启用，否则禁用并发出警告。
- ❌ 强制启用检查：若指定 `--v8-enable-temporal-support` 但未检测到 `cargo`/`rustc`，构建将报错停止。
- 🚫 避免冲突：同时使用 `--v8-disable-temporal-support` 和 `--v8-enable-temporal-support` 会导致错误。
- 🐛 已知问题：Temporal 在 `--with-intl=none` 或 `--with-intl=system-icu` 时存在构建问题，已另开 issue 处理。
- 🛠️ 逐步部署：此自动检测机制允许在 CI 机器上逐步部署 Rust，目标为 Node.js 26 版本。

---

### [2026-04-28，版本 26.0.0（当前版），作者：RafaelGSS · 拉取请求 #62526 · nodejs/node · GitHub](https://github.com/nodejs/node/pull/62526#issuecomment-4282061307)

**原文标题**: [2026-04-28, Version 26.0.0 (Current) by RafaelGSS · Pull Request #62526 · nodejs/node · GitHub](https://github.com/nodejs/node/pull/62526#issuecomment-4282061307)

Node.js 26.0.0 版本（2026年4月28日发布）的合并请求正在处理中，包含多项更新和待解决问题。

- 🚀 **版本发布**：Node.js 26.0.0（Current）计划于2026年4月28日发布，由RafaelGSS负责合并。
- 🛠️ **待解决问题**：包括macOS 15夜间构建libffi失败、AIX libc++文件系统bug、Clang构建支持等。
- 📦 **依赖更新**：更新V8至14.6版本、undici至8.0.2，并合并相关补丁。
- 🔒 **安全与质量**：代码覆盖率达89.71%，所有修改行均通过测试。
- ⏳ **发布延迟**：因V8 14.6集成问题，发布从4月22日推迟至28日。
- 👥 **审查状态**：已获得mcollina和avivkeller批准，但targos要求更改，需解决V8更新等问题。
- 🔧 **其他变更**：包括运行时弃用module.register()、移除extensionless CJS异常、统一非对称密钥导入等。

---

### [获取失败](https://javascriptweekly.com/link/184053/web)

**原文标题**: [Failed to retrieve](https://javascriptweekly.com/link/184053/web)

无法总结：获取内容失败，状态码 403。

---

### [获取失败](https://javascriptweekly.com/link/184054/web)

**原文标题**: [Failed to retrieve](https://javascriptweekly.com/link/184054/web)

无法总结：获取内容失败，状态码 404。

---

### [crates.io：帮助测试我们的新网页前端 | Rust 内部博客](https://blog.rust-lang.org/inside-rust/2026/04/17/crates-io-svelte-public-testing/)

**原文标题**: [crates.io: Help test our new web frontend | Inside Rust Blog](https://blog.rust-lang.org/inside-rust/2026/04/17/crates-io-svelte-public-testing/)

crates.io 正在测试基于 Svelte 5 的新前端，并邀请社区参与测试。

- 🧪 crates.io 前端已从 Ember.js 迁移至 Svelte 5，现于 https://crates.io/svelte/ 公开测试
- 🔄 新前端旨在 1:1 复现原版功能，外观与行为应保持一致，任何差异均视为需报告的 Bug
- 🔗 新旧应用共享同一域名、会话状态和数据，无需重新登录即可直接使用测试版
- 🐛 若发现异常，可通过 GitHub 或 Zulip（#t-crates-io）反馈
- 🎯 测试顺利的话，未来几周内 Svelte 版将设为默认前端
- 🙏 感谢 Ember.js 团队多年支持，以及 Svelte 团队和 @eth3lbert 对迁移工作的贡献

---

### [Node.js — Node.js 24.15.0（长期支持版）](https://nodejs.org/en/blog/release/v24.15.0)

**原文标题**: [Node.js — Node.js 24.15.0 (LTS)](https://nodejs.org/en/blog/release/v24.15.0)

Node.js 24.15.0 (LTS) 版本发布，代号 "Krypton"，包含多项新功能、性能优化和错误修复。

- 🚀 **新增CLI选项**：添加 `--max-heap-size` 和 `--require-module`/`--no-require-module` 选项，提升配置灵活性
- 🔐 **加密增强**：KeyObject API 新增原始密钥格式支持，并更新根证书至 NSS 3.121
- 📁 **文件系统改进**：`fs.stat` 和 `fs.promises.stat` 新增 `throwIfNoEntry` 选项
- 🌐 **HTTP/2 优化**：添加 `http1Options` 用于 HTTP/1 回退配置，并增加 `strictSingleValueFields` 选项
- 🧪 **测试运行器升级**：支持模块模拟的 `exports` 选项、暴露 worker ID、在 SIGINT 时显示中断测试
- 📦 **模块系统稳定**：`require(esm)` 和模块编译缓存标记为稳定
- 🔌 **网络功能扩展**：`Socket` 新增 `setTOS` 和 `getTOS` 方法
- 🗄️ **SQLite 改进**：`DatabaseSync` 新增 `limits` 属性，并标记为候选发布版
- ⚡ **性能优化**：改进 `Buffer` 操作、`stream` 管道、`assert` 比较等性能
- 🛠️ **依赖更新**：升级 npm 至 11.12.1、V8、SQLite 至 3.51.3、ada 至 3.4.4 等
- 🐛 **错误修复**：修复 HTTP 请求路径验证、`zlib` 重置时释放后使用、`fs.cpSync` 非 ASCII 字符处理等

---

### [寓言 · 你可以引以为傲的JavaScript！](https://fable.io/)

**原文标题**: [Fable · JavaScript you can be proud of!](https://fable.io/)

这段代码定义了扑克牌的类型系统，并使用模式匹配进行识别和输出。

- 🃏 定义了 `Face` 类型，包含 `Ace`、`King`、`Queen`、`Jack` 和数字牌（`Number of int`）
- ♠️ 定义了 `Color` 类型，包含 `Spades`、`Hearts`、`Diamonds`、`Clubs`
- 🎴 定义了 `Card` 类型，由 `Face` 和 `Color` 组合而成
- ❤️ 创建了红心A（`Ace, Hearts`）和黑桃10（`Number 10, Spades`）的实例
- 🔍 使用 `match` 表达式对牌进行模式匹配，分别处理红心A、红心牌、黑桃数字牌、方块或梅花牌
- ⚠️ 编译器发出警告，指出模式匹配不完整，例如 `(_,Spades)` 可能未被覆盖

---

### [发布 5.0.0 · fable-compiler/Fable · GitHub](https://github.com/fable-compiler/Fable/releases/tag/5.0.0)

**原文标题**: [Release 5.0.0 · fable-compiler/Fable · GitHub](https://github.com/fable-compiler/Fable/releases/tag/5.0.0)

Fable 编译器发布 5.0.0 版本，主要修复了多个后端（Python、Dart、Rust、JS/TS、Beam）中的错误，涉及类型比较、集合操作和字符串处理等问题。

- 🐛 修复 Python 中泛型抽象类的派生类实例化问题（方法名不匹配）
- 🔧 修复 Dart/Rust 中 `ResizeArray` 的引用相等性
- 🛠️ 修复 JS/TS/Python/Beam 中 `ResizeArray` 的相等性改为引用比较
- 📦 修复 Beam 中 `List.Cons` 调用替换
- 🔍 修复 Beam/Dart/Python/TypeScript 中 `Array.Equals` 改为引用比较
- 📊 修复 Dart/Python/TypeScript/Rust 中 `Seq.foldBack2` 对不同长度序列的处理
- 🧩 修复所有后端中缺失的 `HashSet` 实现和测试
- 🗂️ 修复 Rust 中 `Array/HashMap/HashSet` 的内部表示
- 🔗 修复 Rust 中 F# 类的引用相等语义
- 🐍 修复 Python 中缺失的 `Array` 模块实现和测试
- 🎭 修复 Python 中对象表达式实现带有 `[<CLIEvent>]` 成员的接口问题
- ⏰ 修复 Python 中 `DateTime.TryParse` 对朴素日期时间字符串的错误赋值
- 🔤 修复 JS/TS 和 Python 中 `String.Contains` 忽略 `StringComparison` 参数的问题
- 🚫 修复 `--noRestore` 未跳过 MSBuildCracker 恢复的问题

---

### [GitHub - uuidjs/uuid: 在JavaScript中生成符合RFC标准的UUID · GitHub](https://github.com/uuidjs/uuid)

**原文标题**: [GitHub - uuidjs/uuid: Generate RFC-compliant UUIDs in JavaScript · GitHub](https://github.com/uuidjs/uuid)

uuidjs/uuid 是一个用于生成符合 RFC9562（原 RFC4122）标准的 UUID 的 JavaScript 库，功能全面且跨平台。

- 🎯 **完整支持**：涵盖所有 RFC9562 UUID 版本（v1 至 v8），包括 NIL 和 MAX 特殊 UUID。
- 🌐 **跨平台**：支持 TypeScript、Chrome、Safari、Firefox、Edge、NodeJS 和 React Native/Expo。
- 🔒 **安全可靠**：使用现代 crypto API 生成随机值，确保安全性。
- 📦 **轻量高效**：零依赖、支持 tree-shaking，并附带命令行工具 `uuid`。
- 🚀 **快速上手**：通过 `npm install uuid` 安装，使用 `import { v4 as uuidv4 } from 'uuid'` 即可生成 UUID。
- 📋 **API 丰富**：提供 `parse()`、`stringify()`、`validate()`、`version()` 等实用函数，以及版本转换功能（如 `v1ToV6`）。
- ⚙️ **版本特性**：v12 起不再支持 CommonJS；v11 起优化了时间戳 UUID 的内部状态管理。
- 🛠️ **CLI 支持**：通过 `npx uuid` 在命令行直接生成 UUID，支持指定版本和参数。
- 🐛 **已知问题**：在缺少 `crypto.getRandomValues()` 的环境（如 React Native）中需添加 polyfill。

---

### [尤雨溪 - Vue 2026 现状 - YouTube](https://www.youtube.com/watch?v=a9_Ud5MFTjU)

**原文标题**: [Evan You - State of Vue 2026 - YouTube](https://www.youtube.com/watch?v=a9_Ud5MFTjU)

本頁面概述了 YouTube 平台相關的資訊與政策，包括版權、聯絡方式、使用條款及私隱等核心內容。

- 📰 **新聞中心**：提供 YouTube 的最新消息與動態
- ©️ **版權**：說明內容創作者與平台間的版權規範
- 📞 **聯絡我們**：列出與 YouTube 團隊聯繫的方式
- 🎥 **創作者**：針對內容創作者提供的資源與支援
- 📢 **刊登廣告**：介紹在 YouTube 上投放廣告的選項
- 👨‍💻 **開發人員**：為開發者提供的 API 與技術文件
- 📜 **條款**：使用 YouTube 服務需遵守的條款與條件
- 🔒 **私隱**：說明用戶資料的收集與使用方式
- 🛡️ **政策及安全**：平台的安全規範與社群準則
- ⚙️ **YouTube 的運作方式**：解釋推薦系統與平台功能
- 🧪 **測試新功能**：介紹 YouTube 正在測試的實驗性功能
- 📅 **© 2026 Google LLC**：版權歸屬與年份標示

---

### [发布 v3.6.0-beta.1 · vuejs/core · GitHub](https://github.com/vuejs/core/releases/tag/v3.6.0-beta.1)

**原文标题**: [Release v3.6.0-beta.1 · vuejs/core · GitHub](https://github.com/vuejs/core/releases/tag/v3.6.0-beta.1)

Vue 3.6.0-beta.1 发布，Vapor 模式进入测试阶段，带来性能提升和新功能。

- 🚀 **Vapor 模式功能完整**：Vapor 模式已实现与虚拟 DOM 模式所有稳定功能的功能对等，但 Suspense 暂不支持。
- ⚡ **响应式系统性能提升**：基于 `alien-signals` 重构 `@vue/reactivity`，大幅改善性能和内存占用。
- 🐛 **多项错误修复**：包括编译器、HMR、keep-alive、transition 和运行时核心的多个 bug 修复。
- 🧩 **Vapor 模式可选加入**：通过 `<script setup vapor>` 启用，支持在现有应用或全新应用中使用。
- 🔗 **VDOM 互操作**：通过 `vaporInteropPlugin` 插件实现 Vapor 与 VDOM 组件嵌套，但存在部分限制。
- 📋 **功能兼容性**：Vapor 模式支持 Vue API 子集，不支持 Options API、`getCurrentInstance()` 等，自定义指令接口不同。

---

### [Vite 8.0 正式发布！ | Vite](https://vite.dev/blog/announcing-vite8)

**原文标题**: [Vite 8.0 is out! | Vite](https://vite.dev/blog/announcing-vite8)

Vite 8.0 正式发布，采用 Rust 驱动的 Rolldown 作为统一打包器，带来 10-30 倍更快的构建速度。

- 🚀 **核心架构变革**：Vite 8 从双打包器（esbuild + Rollup）迁移到单一 Rust 打包器 Rolldown，构建速度提升 10-30 倍，并保持完全插件兼容。
- 📈 **生态系统增长**：Vite 每周下载量达 6500 万次，并推出 plugin 目录 registry.vite.dev，方便开发者搜索插件。
- ⚡ **真实性能提升**：多家公司报告生产构建时间大幅缩短，如 Linear 从 46 秒降至 6 秒，Ramp 减少 57%，Beehiiv 减少 64%。
- 🔧 **统一工具链**：Vite 8 整合了构建工具（Vite）、打包器（Rolldown）和编译器（Oxc），实现端到端一致行为，支持更优优化。
- 🆕 **新增功能**：集成开发者工具、内置 tsconfig paths 支持、emitDecoratorMetadata 支持、Wasm SSR、浏览器控制台转发等。
- 📦 **安装体积变化**：Vite 8 比 Vite 7 大约 15 MB，主要来自 lightningcss（~10 MB）和 Rolldown（~5 MB）。
- 📋 **迁移指南**：大多数项目可平滑升级，建议先使用 rolldown-vite 包在 Vite 7 上测试，再升级到 Vite 8。
- 🙏 **致谢**：感谢 Rollup 和 esbuild 的贡献，它们为 Vite 奠定了基础；同时感谢社区贡献者和早期测试者的反馈。

---

### [Vite+ | 统一的Web工具链](https://viteplus.dev/)

**原文标题**: [Vite+ | The Unified Toolchain for the Web](https://viteplus.dev/)

Vite+ 是一个统一的 Web 开发工具链，可管理运行时、包管理器及前端框架，基于 MIT 开源协议发布。

- 🛠️ **一站式管理**：自动选择项目所需的 Node 运行时和包管理器（pnpm/npm/yarn/bun），简化日常开发流程。
- 🚀 **极致性能**：底层采用 Rust 编写，构建速度比 webpack 快 40 倍，代码检查比 ESLint 快 50-100 倍，格式化比 Prettier 快 30 倍。
- 🧩 **框架兼容**：支持所有基于 Vite 构建的框架（如 Vue、React、Svelte 等 20+ 框架），并提供统一配置和命令流。
- 🔒 **安全可靠**：基于成熟开源标准构建，由行业专家维护，每周 npm 下载量超 6900 万次，GitHub 星标超 7.8 万。
- ⚡ **核心功能**：集成 dev/build（极速构建与 HMR）、check（格式化/代码检查/类型检查）、test（兼容 Jest 的测试运行器）、run（依赖感知的脚本执行）、pack（库打包与 DTS 生成）。
- 🌐 **全栈支持**：可作为 SPA 或全栈元框架的基础，支持 Vercel、Netlify、Cloudflare 等平台部署。
- 💡 **专注交付**：减少工具维护时间，提升跨团队协作效率，标准化最佳实践，支持 AI 辅助工作流。

---

### [虚空](https://void.cloud/)

**原文标题**: [Void](https://void.cloud/)

概述总结  
- 🚀 Void是一个专为Vite应用设计的部署平台，提供全栈开发能力，支持一键部署到生产环境。  
- ⚡ 只需`void deploy`命令，即可自动构建、运行迁移、配置资源并部署应用。  
- 🛠️ 内置数据库、KV存储、对象存储、AI推理、认证、队列和定时任务等全栈功能，按需导入即可。  
- 📂 代码即基础设施：Void自动扫描源码，检测使用情况并自动配置所有资源，无需配置文件或手动操作。  
- 🌐 基于Cloudflare全球网络，确保高性能、安全性和高可用性。  
- 🎨 支持React、Vue、Svelte、Solid等框架，以及SSR、SSG、ISR、岛屿架构和Markdown渲染。  
- 🤖 AI原生支持：内置技能、MCP和参考提示，让编码代理通过单个提示即可构建和部署全栈应用。  
- 🔗 开源项目，与Vite、Vitest、Rolldown、Oxc等工具生态集成。

---

### [获取失败](https://javascriptweekly.com/link/184065/web)

**原文标题**: [Failed to retrieve](https://javascriptweekly.com/link/184065/web)

无法总结：获取内容失败，状态码 404。

---

### [Ghost —— 首个为智能体设计的数据库](https://ghost.build/?utm_source=content-syndication&utm_medium=referral&utm_campaign=javascript-weekly-newsletter)

**原文标题**: [Ghost â The first database designed for agents](https://ghost.build/?utm_source=content-syndication&utm_medium=referral&utm_campaign=javascript-weekly-newsletter)

专为AI代理设计的首个数据库服务，提供无限Postgres数据库，支持自由创建、分支和丢弃，专为代理工作模式优化。

- 🚀 提供无限Postgres数据库，可自由创建、分支和丢弃
- 💻 支持通过curl命令快速安装：`curl -fsSL https://install.ghost.build | sh`
- 📧 提供每周摘要订阅，也可通过邮件发送安装链接
- 🆓 免费套餐包含：无限数据库、无限分支、100小时/月、1TB存储
- 💰 设有硬性消费上限，避免意外费用
- 🤖 支持Claude Code集成，通过MCP协议创建数据库
- 🏷️ 示例数据库名称：hot-takes（热点观点）、things-i-pretend-to-understand（假装理解的事物）、vibe-check（氛围检查）
- 🔗 每个数据库提供独立连接字符串，格式为：`postgresql://ghost:密码@数据库名.ghost.build/postgres`

---

### [垂直代码库](https://tkdodo.eu/blog/the-vertical-codebase)

**原文标题**: [The Vertical Codebase](https://tkdodo.eu/blog/the-vertical-codebase)

### 概述总结
本文探讨了如何通过垂直结构（按功能/领域分组）替代传统的水平结构（按类型分组，如components/hooks/utils）来组织代码库，以提高可维护性、可扩展性和团队协作效率。

- 📂 **水平结构的问题**：按类型分组（如components/hooks/utils）导致代码按技术类型而非功能领域组织，随着代码库增长，文件数量激增（如Sentry有200+组件文件），难以导航和定位。
- 🤖 **AI与代码结构**：AI代理（如代码生成工具）同样需要清晰的边界、约束和快速反馈循环，垂直结构有助于代理高效工作，尤其在大型、有机增长的代码库中。
- 🔗 **代码共置原则**：一起变更的代码应放在一起，例如组件的props、数据获取逻辑（如queryOptions）应与其组件共置，而非分散到不同目录。
- 📈 **垂直结构优势**：按功能/领域分组（如`src/widgets/`）提高内聚性，降低耦合，使代码易于发现和归属，并自然对齐团队结构和代码所有权。
- 🧩 **共享代码处理**：共享代码（如跨页面使用的组件）应作为独立垂直领域（如`PageFilters`），或归入设计系统（`/design-system`），避免分散在不同目录。
- 🚧 **边界与公共接口**：通过monorepo（如pnpm workspaces）或ESLint规则（如`eslint-plugin-boundaries`）定义垂直间的公共接口，强制私有代码不被外部依赖，减少耦合风险。
- ⚠️ **挑战与权衡**：垂直结构需要更多思考和团队沟通（如选择正确的分组、避免重复实现），但长期来看能提升代码库的可维护性和扩展性。

---

### [NPM 安全 - OWASP 速查表系列](https://cheatsheetseries.owasp.org/cheatsheets/NPM_Security_Cheat_Sheet.html)

**原文标题**: [NPM Security - OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/cheatsheets/NPM_Security_Cheat_Sheet.html)

本文件是OWASP NPM安全速查表，提供了全面的JavaScript和Node.js项目安全最佳实践，涵盖从发布、依赖管理到供应链安全的多个方面。

- 📋 **避免向npm注册表泄露密钥**：使用`.npmignore`或`files`属性控制发布内容，并通过`--dry-run`预览tarball，防止敏感文件意外发布。
- 🔒 **强制使用锁文件**：通过`npm ci`或`yarn install --frozen-lockfile`确保依赖版本一致，防止因`package.json`与锁文件不一致而引入意外版本。
- 🛡️ **最小化攻击面：忽略运行脚本**：使用`--ignore-scripts`禁用第三方包的脚本执行，并通过`@lavamoat/allow-scripts`创建白名单，允许必要包运行生命周期脚本。
- 🩺 **评估npm项目健康**：使用`npm outdated`检查依赖更新状态，使用`npm doctor`诊断npm安装和环境健康，确保开发环境正常。
- 🔍 **审计开源依赖漏洞**：持续扫描第三方开源项目的安全漏洞，并通过OWASP Dependency-Track等工具监控项目清单，及时接收新CVE警报。
- 🏗️ **制品治理与供应链保护**：使用本地npm代理（如Verdaccio）缓存依赖，生成SBOM（如CycloneDX），签名制品（如Sigstore），并限制CI令牌权限，加强供应链安全。
- 📢 **负责任地披露安全漏洞**：遵循负责任披露流程，与维护者协调修复和发布日期，确保用户在漏洞公开前有升级路径。
- 🔑 **启用双因素认证（2FA）**：通过npm CLI或界面启用2FA（`auth-and-writes`或`auth-only`），保护账户免受未授权访问。
- 🎫 **使用npm作者令牌**：创建只读、IP范围受限的令牌用于CI，并通过`npm token list`和`npm token revoke`管理令牌，减少泄露风险。
- 🎣 **理解打字错误和懒惰错误攻击**：警惕打字错误攻击（利用拼写错误）和懒惰错误攻击（利用AI幻觉的包名），安装前通过`npm view`验证包存在性和下载量。
- 🔐 **使用可信发布者安全发布包**：通过OpenID Connect（OIDC）建立信任关系，使用短期工作流凭证发布，并自动生成来源证明，消除长期令牌风险。
- 🚫 **防止依赖混淆攻击**：使用作用域包名（如`@yourorg/package-name`），配置`.npmrc`指向私有注册表，并在公共注册表预留内部包名作为占位符。
- 📝 **复制文档示例前验证安全性**：审查README示例中的安全模式（如密钥派生、正则锚定、随机数生成），优先采用库内部安全默认值，并报告不安全的文档。
- 🛠️ **最终建议**：安装前通过`npm info`验证包元数据，日常使用注销用户，安装时附加`--ignore-scripts`，减少命令执行和账户泄露风险。

---

### [我们如何利用AI加速Angular编译器 | VoidZero](https://voidzero.dev/posts/oxc-angular-compiler)

**原文标题**: [How we made the Angular Compiler faster using AI | VoidZero](https://voidzero.dev/posts/oxc-angular-compiler)

概述：VoidZero团队利用AI编码代理，在两个月内开发出基于Rust的Oxc Angular编译器，实现了最高20.7倍的编译速度提升，并展示了AI辅助大型开源项目开发的潜力。

- 🚀 **性能飞跃**：Oxc Angular编译器在Super Productivity项目上比Angular CLI快6.4倍，在Bitwarden项目上比Webpack+@ngtools/webpack快20.7倍，主要得益于绕过TypeScript语义检查、原生Rust实现和Vite集成。
- ⚙️ **技术架构**：基于VoidZero的Oxc（Rust语言工具链），通过NAPI-RS与Vite 8+集成，支持完整HMR和Angular原生特性，但不支持跨文件优化和模板类型检查。
- 🧪 **实验性质**：该项目为研究性实验，不会持续维护，但展示了完全用Rust实现Angular单文件编译的参考方案，未来可能整合进Angular官方编译器。
- 🤖 **AI协作开发**：开发者Brooklyn使用Claude Code和Codex，通过“计划模式→自动化循环→详细对齐→架构审查”四阶段流程，让AI代理自主运行4-6小时完成大部分开发工作。
- 📋 **测试系统设计**：关键成功因素包括：复用Oxc现有测试框架（单元测试/快照测试/一致性测试）、严格1:1移植Angular TypeScript编译器逻辑、使用Compare测试工具对比真实项目输出。
- 🔍 **Codex架构审查**：在后期阶段，使用Codex进行系统性审查，发现了`@for` track优化缺少根视图守卫、`@switch`默认分支顺序调整等未覆盖测试的细微问题。
- 🎯 **最终成果**：经过约5周迭代开发，Oxc Angular编译器能编译Bitwarden等大型项目，生成与Angular CLI语义完全等效的代码，且所有测试无回归。

---

### [我为什么不再在JavaScript中链式调用所有东西 - Matt Smith](https://allthingssmitty.com/2026/04/20/why-i-dont-chain-everything-in-javascript-anymore/)

**原文标题**: [
    Why I don't chain everything in JavaScript anymore - Matt Smith
  ](https://allthingssmitty.com/2026/04/20/why-i-dont-chain-everything-in-javascript-anymore/)

概述总结  
- 📉 长链式调用看似简洁，但调试和阅读时反而增加认知负担  
- 🧩 将链式操作拆分为命名变量步骤，代码更清晰易维护  
- 🔍 链式处理会遍历整个数组，而分步写法可提前终止（如使用`find`）  
- 🐛 调试时链式调用需混入日志代码，破坏逻辑纯粹性  
- 🚀 处理大数组或性能敏感路径时，分步写法能减少不必要计算  
- ⚡ 异步链式调用（如Promise链）混合控制流与数据转换，拆分后更易理解  
- 📏 经验法则：1-2步链式安全，3-4步考虑拆分，5步以上必须拆分  
- 🛠 通过命名中间变量、分离逻辑步骤、保留短链来平衡简洁与可读性

---

### [类型守卫和断言函数的作用范围 | Stefan Judis 网络开发](https://www.stefanjudis.com/today-i-learned/the-scope-of-type-guards-and-assertion-functions/)

**原文标题**: [The scope of type guards and assertion functions | Stefan Judis Web Development](https://www.stefanjudis.com/today-i-learned/the-scope-of-type-guards-and-assertion-functions/)

### 概述总结
类型守卫和断言函数在TypeScript中的作用范围不同：类型守卫仅在条件块内缩小类型，而断言函数会在整个当前作用域内调整类型。

- 🔍 **类型守卫**：通过 `value is Type` 语法实现，仅在条件判断块（如 `if` 语句）内缩小类型范围，离开该块后类型恢复为原始类型。
- ⚡ **断言函数**：使用 `asserts value is Type` 语法，若函数不抛出异常，则在整个当前作用域内永久调整类型，无需条件包裹。
- 📌 **使用场景**：类型守卫适合需要条件分支处理的场景；断言函数适合在验证后直接使用类型化数据的场景（如解析未知数据后立即调用）。
- 🛡️ **安全建议**：处理未知来源数据（如 `fetch` 或 `JSON.parse`）时，推荐使用 Zod 等验证库进行运行时校验，而类型守卫/断言函数主要用于类型层面的缩小。
- 🔄 **关键区别**：类型守卫缩小类型的作用域是局部的（条件块内），断言函数的作用域是全局的（当前作用域内）。

---

### [Bun v1.3.13 | Bun 博客](https://bun.com/blog/bun-v1.3.13)

**原文标题**: [Bun v1.3.13 | Bun Blog](https://bun.com/blog/bun-v1.3.13)

Bun 发布了多项性能优化和新功能，包括测试、安装、构建和运行时方面的改进。

- 🚀 **测试性能大幅提升**：新增 `--isolate` 和 `--parallel` 标志，`--isolate` 在每个测试文件间创建全新全局环境，`--parallel` 可跨 CPU 核心并行运行测试，显著加速大型测试套件。
- 🔀 **CI 分片与变更测试**：`--shard=M/N` 支持在 CI 作业间拆分测试文件；`--changed` 标志仅运行受 Git 变更影响的测试，并可结合 `--watch` 实时重筛。
- 📦 **安装与链接优化**：`bun install` 流式解压 tarball，内存减少 17 倍；隔离链接器 (`--linker=isolated`) 在 peer 依赖多的 monorepo 中速度提升约 8.5 倍。
- 🧠 **内存与引擎升级**：源码映射内存占用降低 8 倍；升级 mimalloc v3 和 libpas，运行时内存减少 5%；JavaScriptCore 引擎合并 1316 个上游提交，带来多项性能与稳定性修复。
- ⚡ **压缩与迭代加速**：zlib 升级至 zlib-ng 2.3.3，gzip 压缩速度提升最高 5.5 倍；内部数组迭代优化，`toContain` 等操作速度提升 1.43 倍。
- 🌐 **Web 标准与 API 增强**：新增 SHA3 哈希算法、X25519 密钥派生支持；`Bun.serve()` 支持 Range 请求和文件流式响应；WebSocket 客户端支持 Unix 域套接字。
- 🛠️ **构建与修复**：`bun build --compile --target browser` 现在正确内联 JS 导入的文件加载器资源；修复了大量 Node.js 兼容性、Bun API、Web API 和 Windows 平台的崩溃与错误。

---

### [Bun — 一个快速的全能JavaScript运行时](https://bun.com/)

**原文标题**: [Bun — A fast all-in-one JavaScript runtime](https://bun.com/)

Bun v1.3.13 发布，这是一款快速的全能 JavaScript 工具包，支持逐步采用，兼容 Node.js。

- 🚀 Bun 是一个集 JavaScript 运行时、打包器、测试运行器和包管理器于一体的快速工具包
- 📦 支持在 Node.js 项目中单独使用 bun test 或 bun install 等工具，或采用完整堆栈
- ⚡ 打包 10,000 个 React 组件仅需 269.1 毫秒（Bun v1.3.0），远快于 Rolldown、esbuild 等
- 🔥 Express.js "hello world" 基准测试达 59,026 请求/秒，远超 Deno (25,335) 和 Node.js (19,039)
- 💬 WebSocket 聊天服务器每秒发送 2,536,227 条消息，性能是 Deno 的 1.9 倍、Node.js 的 5.8 倍
- 📊 加载大表（100 行 x 100 并行查询）达 28,571 查询/秒，优于 Node.js (14,522) 和 Deno (11,169)
- 💻 支持 Linux、macOS 和 Windows 安装，提供 curl 和 PowerShell 脚本

---

### [Bun v1.3.12 | Bun 博客](https://bun.com/blog/bun-v1.3.12)

**原文标题**: [Bun v1.3.12 | Bun Blog](https://bun.com/blog/bun-v1.3.12)

Bun 发布了一系列重大更新，涵盖浏览器自动化、终端渲染、性能优化和大量 Bug 修复。

- 🚀 **Bun.WebView 原生浏览器自动化**：内置无头浏览器自动化，支持 WebKit (macOS) 和 Chrome (跨平台) 双后端。所有输入事件（如点击、滚动）均为 OS 级事件，网站无法区分。提供 `navigate`、`click`、`screenshot`、`evaluate` 等完整 API，并支持 Playwright 风格的可操作性自动等待。
- 🖥️ **终端 Markdown 渲染**：`bun ./file.md` 可直接在终端渲染 Markdown 文件为精美的 ANSI 输出。同时提供 `Bun.markdown.ansi()` API，支持颜色、超链接、Kitty 图形协议及自定义列宽。
- ⏰ **进程内 Bun.cron() 调度器**：支持在运行时内直接运行定时任务回调，适用于长期运行的服务器。关键特性包括：无重叠执行、UTC 时间、`--hot` 安全、`Disposable` 支持、以及 `ref`/`unref` 控制进程生命周期。
- 🧩 **异步堆栈追踪**：原生 API（如 `node:fs`、`Bun.write`、`node:http`）现在支持异步堆栈追踪，极大简化调试过程。
- 📡 **UDP Socket 改进**：ICMP 错误不再静默关闭 socket，而是通过 `error` 处理器上报，socket 保持打开。新增 `flags.truncated` 参数，用于检测接收数据报是否被截断。
- 🔌 **Unix 域套接字生命周期修正**：现在匹配 Node.js 行为。绑定已存在的 socket 文件会正确返回 `EADDRINUSE`，关闭监听器后自动清理 `.sock` 文件。
- ⚡ **JavaScriptCore 引擎升级**：包含 1650+ 上游提交，带来性能提升和新特性。支持 `using`/`await using` 显式资源管理，JIT 编译器优化（快速升级、`Array.isArray` 内联、更快的 `String#includes` 等），以及 WebAssembly 改进。
- 🏎️ **URLPattern 性能提升 2.3 倍**：通过直接调用编译后的正则引擎，消除了每次调用多达 24 次 GC 分配。`test()` 方法在命名分组匹配场景下从 1.05µs 降至 487ns。
- 📏 **Bun.stripANSI 和 Bun.stringWidth 大幅加速**：通过 SIMD 优化，`stripANSI` 处理纯 ASCII 字符串速度提升约 4 倍，`stringWidth` 处理含超链接和 emoji 的 UTF-16 字符串速度提升约 11 倍。
- 🐢 **低核心机器上 bun build 速度提升**：修复了线程池 Bug，在 2 核机器上构建速度提升 1.43–1.47 倍。
- 🔍 **Bun.Glob.scan() 加速**：对于 `**/X/...` 边界模式，性能提升高达 2 倍。Windows 上通过 `NtQueryDirectoryFile` 下推通配符过滤，简单模式性能提升高达 2.4 倍。
- 🐳 **Cgroup 感知的 availableParallelism**：在 Linux 上，线程池和 JIT 线程现在遵循 cgroup CPU 限制，优化 Docker 和 k8s 环境下的资源利用。
- 🔗 **HTTPS 代理 CONNECT 隧道保活**：对同一目标的多个 HTTPS 请求复用单个 CONNECT 隧道，大幅降低延迟。修复了 `fetch` 与 HTTPS 代理一起使用时偶发的 `Malformed_HTTP_Response` 错误。
- ⚙️ **Bun.serve() 启用 TCP_DEFER_ACCEPT**：在 Linux 上使用 nginx 相同的优化，将连接接受和读取数据合并为一次事件循环唤醒，对短连接尤其有效。
- 🐛 **大量 Bug 修复**：包括 `process.env` 在无权限目录下为空、`vm.Script` 内存泄漏、`pipeline` 与 `fetch` 响应体组合时的死锁、`node:dns` 导出缺失、`fs.stat` 在 seccomp 过滤下抛出 `EPERM`、`process.stdout.end` 回调过早触发、`AbortController.signal.reason` 被 GC 清空、`String.raw` 破坏空字节、WebSocket 连接因非 ASCII 字符崩溃等。

---

### [Bun v1.3.13 | Bun 博客](https://bun.com/blog/bun-v1.3.13#bun-s-runtime-uses-5-less-memory)

**原文标题**: [Bun v1.3.13 | Bun Blog](https://bun.com/blog/bun-v1.3.13#bun-s-runtime-uses-5-less-memory)

以下是对 Bun 新版本功能的概述总结：

- 🚀 Bun 测试新增 `--isolate` 和 `--parallel` 标志，大幅提升大型测试套件的运行速度，支持每个测试文件独立环境及多进程并行执行。
- 📊 新增 `--shard` 标志，支持将测试文件按分片分配到不同 CI 任务中运行，与 Jest、Vitest 等工具兼容。
- 🔍 `bun test` 支持 `--changed` 标志，仅运行受 Git 变更影响的测试文件，并可与 `--watch` 结合使用。
- 📦 `bun install` 实现流式解压 tarball，无需将整个压缩包加载到内存，在大型仓库中内存占用减少 17 倍。
- ⚡ 隔离链接器 (`--linker=isolated`) 在依赖多的 monorepo 中可将安装时间从 20.5 秒降至 2.4 秒。
- 🧠 源映射内存占用最高减少 8 倍，采用紧凑的位打包二进制格式，解码成本接近零。
- 💾 JavaScript 运行时内存占用降低 5%，得益于 mimalloc v3 和 libpas 回收器改进。
- 🔧 升级 JavaScriptCore 引擎，合并 1316 个上游提交，带来多项性能优化和错误修复。
- 🎯 `addEventListener`、`dispatchEvent` 等 DOM 事件性能提升，合并约 270 个上游 WebKit 提交。
- 📁 文件流式传输改进：SSL 和 Windows 环境下的大文件响应不再缓冲整个文件到内存。
- 📐 `Bun.serve()` 支持 Range 请求，自动处理字节范围请求并返回 206 状态码。
- 🗜️ gzip 压缩速度最高提升 5.5 倍，得益于升级到 zlib-ng 2.3.3。
- 🔄 内部数组迭代速度提升最高 1.43 倍，通过直接读取 JSC butterfly 内存实现。
- 🔐 新增 SHA3 哈希算法支持（SHA3-224/256/384/512），涵盖 Web Crypto API 和 `node:crypto`。
- 🔑 SubtleCrypto 的 `deriveBits()` 现支持 X25519 算法，完成密钥协商功能。
- 🌐 WebSocket 客户端支持 `ws+unix://` 和 `wss+unix://` 协议，可通过 Unix 域套接字连接。
- 🖼️ 独立 HTML 构建现内联从 JavaScript 导入的文件加载器资源为 data: URI。
- 🐛 修复大量 Node.js 兼容性问题、Bun API 错误、Web API 问题、Windows 平台崩溃及 JavaScript 引擎错误。

---

### [使用Clerk的B2B SaaS](https://clerk.com/organizations?utm_source=cooper_press&utm_medium=newsletter&utm_campaign=b2b-auth&utm_content=04-21-26&dub_id=dcaTygxEeTZ5iFpN)

**原文标题**: [B2B SaaS with Clerk](https://clerk.com/organizations?utm_source=cooper_press&utm_medium=newsletter&utm_campaign=b2b-auth&utm_content=04-21-26&dub_id=dcaTygxEeTZ5iFpN)

Clerk 提供企业级 B2B 身份验证解决方案，帮助快速构建多租户 SaaS 产品，包含组织管理、邀请、RBAC、SSO 等开箱即用功能，并支持计费与洞察。

- 🏢 **快速创建组织**：自动检测用户邮箱域名并预填组织名称，简化创建流程。
- 📧 **无摩擦邀请**：支持手动或基于邮箱域名的自动邀请，让团队加入更顺畅。
- 👥 **多团队支持**：用户可加入多个组织，并在它们之间安全、即时切换。
- 🔒 **企业级安全**：支持 SAML、OIDC 等 SSO 协议，以及 SCIM 自动用户生命周期管理。
- 🛡️ **细粒度权限控制**：通过 RBAC 定义角色和权限，支持自定义角色集。
- 💳 **B2B 计费集成**：内置计费功能，按组织收费，无需自定义逻辑，支持订阅管理与收入洞察。
- 📊 **数据驱动增长**：提供组织活跃度、新增、留存等分析，帮助发现扩展机会。
- 🧩 **可定制 UI 组件**：提供 `<OrganizationSwitcher>` 等预构建组件，也可自定义认证流程。
- 🚀 **快速落地与扩展**：从基础邀请和权限开始，后续可无重构添加 SSO、审计日志等高级功能。
- 🏆 **客户信赖**：被 Inngest、Chasi、Alter 等公司采用，快速实现了 MFA、SSO 等企业必备功能。

---

### [免费开源动画ReactJS组件 | animata](https://animata.design/)

**原文标题**: [Free & Open Source Animated ReactJS Components | animata](https://animata.design/)

该页面介绍了一个提供158+动画React组件的开源库，旨在帮助开发者更快、更美观地构建界面。

- 🚀 **加速开发**：提供158+个动画React组件，可直接复制到任何项目中，无需安装，即拿即用。
- ⭐ **社区认可**：已获得2,506+个GitHub星标，受到全球开发者信赖，来自印度、德国、美国等多国用户好评。
- 🧩 **丰富分类**：组件涵盖背景、按钮、卡片、图表、英雄区、列表、进度条、标签页、文本等20多种类别，功能全面。
- 🔧 **实战验证**：每个组件均源自真实产品，已包含键盘焦点、屏幕阅读器标签、减少动效回退等无障碍支持。
- 💻 **广泛兼容**：支持Next.js、Remix、Vite、Astro、Gatsby、TanStack等主流框架。
- 📜 **MIT开源许可**：永久免费，由社区驱动，已有众多贡献者和分支，界面生动且充满活力。

---

### [动画光束 | 免费且开源的动画ReactJS组件](https://animata.design/docs/background/animated-beam)

**原文标题**: [Animated Beam | Free & Open Source Animated ReactJS Components](https://animata.design/docs/background/animated-beam)

以下是您提供的文字内容的摘要概述和要点列表：

概述摘要  
此内容为Animata设计系统的组件文档与使用指南，涵盖背景、按钮、卡片、文本动画等数十种UI组件，并提供安装、本地运行及最佳实践说明。

- 🚀 **快速开始**：包含安装、本地运行、添加组件及文件夹结构等入门指南。
- 🎨 **背景组件**：提供8种背景效果，如动态光束、模糊斑点、对角线、网格等。
- 📦 **按钮组件**：13种按钮样式，包括AI按钮、Duolingo风格、涟漪效果等。
- 🃏 **卡片组件**：9种卡片设计，涵盖评论卡片、翻转卡片、发光卡片等。
- 🖼️ **容器组件**：5种容器效果，如动画边框轨迹、滚动公告、鼠标追踪等。
- 📊 **图表组件**：7种图表类型，包括条形图、提交图、环形图等。
- 🎭 **文本动画**：40种文本动画，如渐变文字、闪烁文字、打字效果等。
- 📱 **小部件组件**：34种小部件，如闹钟、电池、日历、天气卡片等。
- ⚙️ **安装与使用**：提供CLI或手动安装方式，并附代码示例与CSS配置。
- 📝 **最佳实践**：包含模糊斑点组件的使用建议与注意事项。

---

### [卡片布局 | 免费开源动画ReactJS组件](https://animata.design/docs/card/card-spread)

**原文标题**: [Card Spread | Free & Open Source Animated ReactJS Components](https://animata.design/docs/card/card-spread)

以下是您提供的文本内容的摘要：

该文档是一个UI组件库的目录和文档，包含多个组件类别（如背景、按钮、卡片等）及其子组件，并提供了“卡片展开”组件的具体实现代码。

- 📚 **组件库总览**：包含背景、Bento网格、按钮、卡片、容器、功能卡片、浮动操作按钮、图表、英雄区、图标、图像、列表、叠加层、预加载器、进度条、骨架屏、标签页、文本动画和微件等20多个类别，每个类别下有多个子组件。
- 🃏 **卡片展开组件**：位于“卡片”类别下，展示一个卡片堆叠效果，悬停时揭示，点击时展开，使用React和状态管理实现交互。
- 🔧 **安装方式**：支持CLI命令（`pnpm dlx shadcn@latest add ...`）或手动创建文件并粘贴代码，代码位于`components/animata/card/card-spread.tsx`。
- 💻 **代码实现**：包含`CardSpread`函数组件，使用`useState`管理展开状态，通过CSS类控制旋转和揭示动画，引用`Notes`、`ShoppingList`等微件组件作为卡片内容。
- 🎨 **样式与交互**：卡片在未展开时堆叠并旋转，展开时平铺并显示间隙，使用`group-hover/spread`和`ease-in-out`过渡实现平滑动画。
- 👤 **贡献者**：组件由“sudha”构建，文档页面提供GitHub编辑链接。

---

### [Slack 的引导界面 | 免费且开源的动画 ReactJS 组件](https://animata.design/docs/hero/slack-intro)

**原文标题**: [Slack's intro screen | Free & Open Source Animated ReactJS Components](https://animata.design/docs/hero/slack-intro)

该文档是 Animata 组件库的完整目录与使用指南，重点介绍了“Slack 风格介绍页”组件的安装和代码实现。

- 📋 组件库包含背景、按钮、卡片、容器、图表、文本动画、微件等 15 大类，每类下细分多个子组件（如文本动画有 40 种效果）。
- 🎨 “Slack 风格介绍页”组件通过彩色几何形状（圆形、圆柱）和波浪文字动画，模拟 Slack 的炫酷开场效果。
- ⚙️ 安装方式：支持 CLI 命令 `pnpm dlx shadcn@latest add ...` 或手动创建文件并粘贴代码（依赖 WaveReveal 组件）。
- 🧩 核心代码：定义了 `Circle`、`Cylinder`、`LineOne` 至 `LineFive` 等组件，通过 CSS 动画实现线条的滑入/滑出效果。
- 🔄 动画控制：通过 `animateOut` 属性触发 3 秒后的退出动画，使用 `useEffect` 和 `setTimeout` 管理状态。
- 📁 文件结构：组件位于 `components/animata/hero/slack-intro.tsx`，并引用了 `@/lib/utils` 工具库。
- 👤 致谢：组件由 Aashish Katila 构建，灵感来源于 Slack 视频。

---

### [officeParser | 最通用的Node.js和浏览器Office解析器](https://officeparser.harshankur.com/)

**原文标题**: [officeParser | The Most Versatile Office Parser for Node.js & Browser](https://officeparser.harshankur.com/)

概述总结
- 📊 每周下载量超过26万次，总下载量突破1000万次
- 📁 支持8种以上文档格式：DOCX、XLSX、PPTX、PDF、ODT、ODS、ODP、RTF
- 🌳 提供结构化抽象语法树（AST）输出，反映文档真实层级
- 📎 支持提取嵌入的图片、图表和对象等附件
- 🔍 集成OCR功能，可通过Tesseract.js读取文档内图像文字
- ℹ️ 获取完整元数据，包括文档属性、作者信息和创建日期
- ⚡ 针对服务器端和浏览器端均进行了性能优化
- ⚙️ 提供可自定义的解析选项，如分隔符、注释处理和解析深度
- 📄 包含详细的技术文档：配置说明、AST参考和调试指南
- 🖥️ 提供AST可视化工具，支持拖拽文件预览并生成JSON和纯文本输出

---

### [GitHub - harshankur/officeParser：一个健壮、严格类型的Node.js和浏览器库，用于解析办公文件（docx、pptx、xlsx、odt、odp、ods、pdf、rtf）。它生成一个清晰、分层的抽象语法树（AST），包含丰富的元数据、文本格式和完整的附件支持。](https://github.com/harshankur/officeParser)

**原文标题**: [GitHub - harshankur/officeParser: A robust, strictly-typed Node.js and Browser library for parsing office files (docx, pptx, xlsx, odt, odp, ods, pdf, rtf). It produces a clean, hierarchical Abstract Syntax Tree (AST) with rich metadata, text formatting, and full attachment support. · GitHub](https://github.com/harshankur/officeParser)

officeParser 是一个功能强大的办公文件解析库，支持多种格式并生成结构化的抽象语法树（AST），便于提取文本、元数据和附件。

- 📄 **多格式支持**：可解析 docx、pptx、xlsx、odt、odp、ods、pdf、rtf 等多种办公文件格式。
- 🌳 **结构化 AST 输出**：生成层级分明的抽象语法树，包含元数据、文本格式和附件信息。
- 🔧 **灵活配置**：支持 OCR 识别、附件提取、原始内容保留等丰富配置选项。
- 🖥️ **跨平台使用**：同时支持 Node.js 和浏览器环境，提供 CLI 工具和库两种使用方式。
- 📊 **高级功能**：支持表格、列表、图表、脚注等复杂文档元素的解析与操作。
- 🚀 **性能优化**：内置智能 OCR 工作池管理，自动处理资源分配和回收。
- 📝 **详细文档**：提供在线 AST 可视化工具和完整的 API 文档，便于调试和学习。
- 🔍 **实用示例**：包含文本搜索、图片提取、Markdown 转换等常见场景的代码示例。

---

### [tiks — 网页程序化UI音效](https://rexa-developer.github.io/tiks/)

**原文标题**: [tiks — Procedural UI Sounds for the Web](https://rexa-developer.github.io/tiks/)

该网页介绍了一个名为“tiks”的轻量级UI音效库，无需音频文件，纯合成生成。

- 🔇 网络原本无声，tiks通过程序化UI音效让其“歌唱”
- 🎵 零音频文件，纯合成生成，体积仅约2KB（gzip后）
- 🛠️ 无依赖，基于Web Audio API，支持音量调节（默认30%）
- 🎨 提供多种主题（Soft/Crisp）和音效：点击、成功、错误、警告、悬停、弹出、嗖声、通知、切换
- 📦 安装命令：`npm install @rexa-developer/tiks`，需在首次手势后初始化
- 📄 开源协议：MIT，托管于GitHub

---

### [GitHub - software-mansion/TypeGPU：一个模块化且开放式的WebGPU工具包，具备高级类型推断功能，并支持使用TypeScript编写着色器 · GitHub](https://github.com/software-mansion/TypeGPU)

**原文标题**: [GitHub - software-mansion/TypeGPU: A modular and open-ended toolkit for WebGPU, with advanced type inference and the ability to write shaders in TypeScript · GitHub](https://github.com/software-mansion/TypeGPU)

TypeGPU 是一个模块化、开源的 WebGPU 工具包，支持在 TypeScript 中编写着色器，并提供高级类型推断，可无缝集成到现有项目中。

- ⚙️ **基础工具**：提供抽象层解决 WebGPU 常见问题，同时支持细粒度降级到原生 WebGPU，避免锁定风险。
- 🧩 **灵活集成**：类型安全 API 可单独或组合使用，只需少量代码即可融入现有应用。
- 📖 **库间互操作**：作为不同 WebGPU 库的互操作层，无需复制数据到 CPU 内存即可传递类型化值。
- 🚀 **文档与社区**：提供官方文档和 Discord 社区支持，助力快速上手和问题解决。
- 🛠️ **生态项目**：包括 Vivarium、wayfare 等库，以及 ComfyUI、Chaos Master 等应用和演示。
- 📂 **仓库结构**：包含核心库、颜色/噪声辅助包、构建工具（如 unplugin-typegpu）和内部解析器。
- 💡 **核心特性**：支持 WGSL 语法镜像、类型推断、着色器生成和 GPU 执行，降低 WebGPU 学习曲线。

---

### [GitHub - shaka-project/shaka-player: JavaScript播放器库 / DASH和HLS客户端 / MSE-EME播放器 · GitHub](https://github.com/shaka-project/shaka-player)

**原文标题**: [GitHub - shaka-project/shaka-player: JavaScript player library / DASH & HLS client / MSE-EME player · GitHub](https://github.com/shaka-project/shaka-player)

Shaka Player 是一个开源的 JavaScript 自适应媒体播放库，支持 DASH 和 HLS 格式，无需插件即可在浏览器中运行，并支持离线存储、多种 DRM 和广告集成。

- 📦 **核心功能**：使用 MediaSource Extensions 和 Encrypted Media Extensions 播放自适应媒体，支持离线存储和回放。
- 🌐 **平台支持**：兼容 Chrome、Firefox、Safari、Edge 等主流浏览器，以及 Chromecast、Tizen TV、Xbox One 等设备。
- 📺 **格式支持**：全面支持 DASH（VOD、直播、录制）和 HLS（VOD、直播、事件），包括低延迟流和章节功能。
- 🔒 **DRM 支持**：支持 Widevine、PlayReady、FairPlay、WisePlay 和 ClearKey，覆盖 DASH 和 HLS 内容。
- 🎬 **媒体容器**：支持 ISO-BMFF/MP4、WebM、MPEG-2 TS，以及 WebVTT、TTML、CEA-608/708 字幕。
- 🛠️ **高级特性**：支持内容转向、VR（360° 投影）、缩略图、广告集成（IMA、AWS MediaTailor）和实验性 MOQT 流。
- 📂 **构建版本**：提供 UI 版、无 UI 版、DASH 专用版和 HLS 专用版，包括实验性功能。
- 📚 **文档与集成**：提供 API 文档、教程和框架集成指南（React、Vue、Angular 等）。

---

### [Shaka Player 演示](https://shaka-project.github.io/shaka-player/demo/)

**原文标题**: [Shaka Player Demo](https://shaka-project.github.io/shaka-player/demo/)

概述摘要  
该页面提供了jQuery项目的多种资源链接，包括文档、许可证、源代码、包管理器、浏览器支持测试、CDN服务以及不同编译版本的演示模式。

- 📄 文档链接：提供官方文档入口  
- 📜 Apache许可证：项目采用Apache开源许可  
- 💻 GitHub源码：托管在GitHub上的源代码  
- 📦 NPM包：通过NPM安装的软件包  
- 🌐 浏览器支持测试：检查浏览器兼容性  
- 🚀 CDN服务：包括Google Hosted Libraries和jsDelivr  
- 🎮 演示模式：提供编译版（Release/Debug）和未编译版

---

### [TiddlyWiki v5.4.0 — 非线性个人网页笔记本](https://tiddlywiki.com/)

**原文标题**: [TiddlyWiki  v5.4.0 — a non-linear personal web notebook](https://tiddlywiki.com/)

概述总结  
TiddlyWiki v5.4.0 是一款无需服务器、开源的交互式信息管理工具，通过将信息切分为最小语义单元（tiddlers）并利用链接、标签、列表和宏进行结构化，帮助用户灵活组织和复用复杂数据。它提供流畅的界面，支持WikiText格式，并拥有活跃的开源社区。

- 📦 TiddlyWiki v5.4.0 正在加载，但浏览器未启用JavaScript，可改用静态HTML版本浏览内容
- 🔗 静态版本包括：单独页面浏览tiddlers（static.html）或单文件包含所有tiddlers（alltiddlers.html）
- 🧠 核心设计理念：将信息切分为最小语义单元（tiddlers），通过标题、链接、标签、列表和宏进行结构化
- ✍️ 使用WikiText符号，简洁表示文本格式和超文本功能，提供流畅的交互界面
- 🌍 无需复杂服务器基础设施，开源且自由，让用户完全掌控自己的信息
- 👥 由@Jermolene创建，现为活跃的开源项目，拥有繁忙的独立开发者社区

---

### [GitHub - TiddlyWiki/TiddlyWiki5: 一个自包含的JavaScript维基，适用于浏览器、Node.js、AWS Lambda等。](https://github.com/TiddlyWiki/TiddlyWiki5)

**原文标题**: [GitHub - TiddlyWiki/TiddlyWiki5: A self-contained JavaScript wiki for the browser, Node.js, AWS Lambda etc. · GitHub](https://github.com/TiddlyWiki/TiddlyWiki5)

TiddlyWiki是一个非线性的个人网络笔记本，可独立于任何公司永久使用，支持浏览器单HTML文件或Node.js应用运行，高度可定制。

- 📝 **核心功能**：TiddlyWiki是一个完整的交互式JavaScript维基，可作为个人笔记工具，所有界面均可用WikiText修改
- 🌐 **使用方式**：支持浏览器直接运行（单HTML文件）或Node.js服务器模式，适合不同用户需求
- 🚀 **安装简便**：通过npm全局安装（`npm install -g tiddlywiki`），支持Linux、Mac、Android等平台
- 🔧 **高级功能**：Node.js版本提供命令行操作，可加载插件、管理文件夹、生成静态站点等
- 💬 **社区支持**：拥有官方论坛、Discord聊天、Reddit子版块和GitHub讨论区，方便用户交流
- 📦 **版本管理**：支持安装特定版本（如`tiddlywiki@5.1.13`）和通过`npm update`升级
- 🎨 **高度可定制**：用户可自定义插件、主题、文件命名规则，甚至整个用户界面
- 📚 **文档完善**：提供官方开发文档（tiddlywiki.com/dev）和贡献指南，便于开发者参与

---

### [发布 6.6.0 版本 · webpro-nl/knip · GitHub](https://github.com/webpro-nl/knip/releases/tag/knip%406.6.0)

**原文标题**: [Release Release 6.6.0 · webpro-nl/knip · GitHub](https://github.com/webpro-nl/knip/releases/tag/knip%406.6.0)

概述摘要  
Knip 6.6.0 版本发布，包含性能优化、依赖替换、Bug 修复及新插件支持。

- 🚀 性能小幅提升，通过替换依赖实现优化（如 picocolors → styleText，@nodelib/fs.walk → fdir）
- 🐛 修复主包中裸说明符的入口提示问题（解决 issue #1693）
- 🔧 从 Astro 配置 AST 中提取 vite.resolve.alias（解决 issue #1692）
- 📦 新增 @sveltejs/package 插件支持（解决 issue #1690）
- 🗺️ 添加插件贡献的源映射规则
- ❤️ 改进 Windows 兼容性

---

### [GitHub - estie-inc/wasm-xlsxwriter: 在浏览器中使用WebAssembly生成Excel文件](https://github.com/estie-inc/wasm-xlsxwriter)

**原文标题**: [GitHub - estie-inc/wasm-xlsxwriter: Generate Excel files in-browser with WebAssembly. · GitHub](https://github.com/estie-inc/wasm-xlsxwriter)

wasm-xlsxwriter 是一个轻量级库，封装了 Rust 的 rust_xlsxwriter 写入 API，并编译为 WebAssembly，使 JavaScript 或 Node.js 能轻松生成 Excel 文件，支持自定义格式、公式、链接和图片等功能。

- 📦 通过 npm 安装 `wasm-xlsxwriter` 库，可在浏览器或 Node.js 环境中使用
- 🚀 Web 示例展示如何创建 Workbook、设置格式（如粗体、日期、边框）并写入数据、公式、链接和图片
- 💻 Node.js 示例演示生成带表头、数据行、自动过滤和冻结窗格的 Excel 文件
- 🌐 兼容 Chrome 75+、Firefox 79+ 和 Safari 15+，通过特定 WebAssembly 特性确保广泛支持
- 📁 提供 Vite、Next.js 和 Node.js 的完整工作示例，位于 `examples/` 目录
- ⚖️ 采用 MIT 许可证，代码仓库在 GitHub 上开源，拥有 146 星标和 4 个复刻

---

### [发布 v9.6.0 - 日落 X · pmndrs/react-three-fiber · GitHub](https://github.com/pmndrs/react-three-fiber/releases/tag/v9.6.0)

**原文标题**: [Release v9.6.0 - Sunset X · pmndrs/react-three-fiber · GitHub](https://github.com/pmndrs/react-three-fiber/releases/tag/v9.6.0)

pmndrs/react-three-fiber 发布了 v9.6.0 版本，主要修复了 ShaderMaterial 的 uniforms 稳定性问题，提升了 HMR 和 React 编译器兼容性，并更新了文档。

- 🔧 **uniforms 稳定性修复**：ShaderMaterial 的 uniforms 对象现在具有稳定引用，避免了 HMR 时的反序列化问题，并支持内联属性和穿透更新。
- 🚀 **React 编译器兼容性提升**：稳定引用使自动记忆化更完整，简化了 JSX 使用，无需额外工具。
- 📚 **文档与示例更新**：修复了“性能陷阱”文档的链接，修正了拼写错误，并提供了新的 ShaderMaterial 示例。
- 🆕 **新贡献者加入**：@simonKristensen 和 @NssGourav 首次贡献，分别修复了文档链接和文字错误。

---

### [GitHub - sindresorhus/np: 更好的 `npm publish` 工具 · GitHub](https://github.com/sindresorhus/np)

**原文标题**: [GitHub - sindresorhus/np: A better `npm publish` · GitHub](https://github.com/sindresorhus/np)

`np` 是一个改进的 `npm publish` 工具，提供交互式发布流程，并包含多项安全检查和自动化功能。

- 🚀 提供交互式 UI，引导用户完成发布流程，简化操作。
- ✅ 确保从正确的发布分支（如 main 或 master）发布，并检查工作目录是否干净。
- 🔄 重新安装依赖，确保项目与最新的依赖树兼容，并验证 Node.js 和 npm 版本。
- 🧪 自动运行测试，并在发布前确保测试通过。
- 📦 自动更新 package.json 中的版本号，创建 Git 标签，并防止意外发布预发布版本。
- 🛡️ 支持双因素认证（2FA），并在发布失败时自动回滚项目状态。
- 🌐 支持 GitHub Packages、npm 9+、Yarn、pnpm 8+ 和 Bun 等包管理器。
- 📝 发布后自动打开 GitHub Releases 草稿，并支持 dry-run 模式预览操作。
- ⚙️ 可通过配置文件（如 .np-config.js 或 package.json 中的 np 字段）自定义行为。
- ❌ 不支持 monorepo，且不适合 CI 环境，建议本地交互使用。

---

### [HyperFormula AI SDK | HyperFormula (v3.2.0)](https://hyperformula.handsontable.com/guide/ai-sdk.html?utm_campaign=378339534-Partner%20Newsletter%20-%20JS%20Weekly%2FFront%20End%20Nation%20-%20Q2-2026&utm_source=JSWeekly&utm_medium=classifieds)

**原文标题**: [HyperFormula AI SDK | HyperFormula (v3.2.0)](https://hyperformula.handsontable.com/guide/ai-sdk.html?utm_campaign=378339534-Partner%20Newsletter%20-%20JS%20Weekly%2FFront%20End%20Nation%20-%20Q2-2026&utm_source=JSWeekly&utm_medium=classifieds)

HyperFormula AI SDK 让大语言模型通过确定性引擎安全读写电子表格并计算公式。

- 📊 **即时公式计算**：调用 `calculateFormula()` 可评估任意 Excel 兼容公式，无需将其放入单元格。
- ✏️ **读写单元格与区域**：支持获取或设置单个单元格及多单元格范围，方便 LLM 程序化检查、填充或修改数据。
- 🔗 **追踪依赖关系**：通过 `getCellDependents()` 和 `getCellPrecedents()` 了解哪些单元格影响公式，以及下游值会如何变化。
- 🚀 **快速集成示例**：提供从创建 HyperFormula 实例到使用工具（如 evaluate、setCellContents、getRange、getDependents）的完整代码演示。
- 💡 **多种应用场景**：包括解释电子表格、生成假设分析、验证清理数据以及从自然语言创建公式。
- 🔑 **Beta 访问**：可注册 Beta 版试用，并支持反馈改进。

---

### [网络研讨会注册 - Zoom](https://us06web.zoom.us/webinar/register/1617760893475/WN_P79TrYY5R8Cru6xEDkwKcw)

**原文标题**: [Webinar Registration - Zoom](https://us06web.zoom.us/webinar/register/1617760893475/WN_P79TrYY5R8Cru6xEDkwKcw)

本内容为Zoom官网的页脚信息，包含多语言支持、版权声明及法律政策链接。

- 🌐 提供多种语言选项，包括英语、西班牙语、德语、简体中文等
- 📅 版权归属Zoom Video Communications, Inc.，时间标注为2026年
- 🔒 包含隐私与法律政策链接，以及“请勿出售我的个人信息”选项
- 🍪 设有Cookie偏好设置功能

---

### [开始注册：2026年旧金山SIGNAL大会](https://signal.twilio.com/2026/begin?utm_campaign=signal&utm_medium=referral&utm_source=javascriptweekly&code=DEVNET26)

**原文标题**: [Begin Registration: SIGNAL San Francisco 2026](https://signal.twilio.com/2026/begin?utm_campaign=signal&utm_medium=referral&utm_source=javascriptweekly&code=DEVNET26)

活动概述：Twilio SIGNAL 2026将于5月4日至7日在旧金山举行，涵盖多个注册通道和活动安排。

- 📅 活动日期：5月4-7日（主要活动），5月7日有Twilio用户组专场
- 📝 注册通道：包含赞助商、供应商、用户组、全球连接、合作伙伴等多个注册选项
- 🔗 联动注册：用户组注册自动包含5月6-7日SIGNAL主会场门票
- 📧 注册要求：必须使用收到邀请的工作邮箱进行注册
- 🏨 注意事项：需特别关注交通与住宿部分的填写
- 🤝 支持联系：如有疑问可联系Kandarp Pandit (kpandit@twilio.com)
- 🎤 活动亮点：包括ISV峰会、分析师峰会、合作伙伴连接等多个专题活动
- 🔄 持续更新：将定期公布精彩的演讲嘉宾和活动主题阵容

---

### [Git 2.54 亮点 - GitHub 博客](https://github.blog/open-source/git/highlights-from-git-2-54/)

**原文标题**: [Highlights from Git 2.54 - The GitHub Blog](https://github.blog/open-source/git/highlights-from-git-2-54/)

概述总结
Git 2.54 版本带来了多项新功能和改进，包括实验性的 `git history` 命令、配置化钩子、默认几何重打包、以及众多用户体验和性能优化。

- 🔄 **重写历史新命令 `git history`**：实验性命令，支持 `reword`（修改提交信息）和 `split`（拆分提交），无需触碰工作树或索引，适合简单历史修改。
- 🔧 **配置化钩子系统**：现在可在 Git 配置中定义钩子，支持多钩子、跨仓库共享，并可单独启用/禁用，无需脚本文件。
- 📦 **默认几何重打包**：`git maintenance run` 默认使用几何策略，增量合并包文件，避免全量 GC，提高仓库维护效率。
- 🎨 **`git add -p` 交互改进**：新增 `J`/`K` 键显示已决策状态，以及 `--no-auto-advance` 选项，允许手动切换文件。
- 🔁 **`git replay` 功能增强**：支持原子引用更新、`--revert` 模式、丢弃空提交，并可重放到根提交。
- 🌐 **HTTP 429 重试支持**：Git 现在能处理“请求过多”响应，根据 `Retry-After` 头或 `http.retryAfter` 设置自动重试。
- 🔍 **`git log -L` 兼容性提升**：现在支持 `-S`、`-G` 等选项，可结合行范围追踪和内容搜索。
- 🗂️ **增量多包索引压缩**：MIDX 支持层压缩，合并小层以控制链长度，提升长期仓库性能。
- 📊 **`git status` 分支比较配置**：新增 `status.compareBranches` 选项，可同时比较上游和推送远程。
- 🏷️ **`git rebase --trailer` 选项**：自动为所有重放提交添加尾部，简化批量操作。
- ✅ **过期密钥签名显示修复**：有效签名即使使用过期密钥也不再显示为红色，避免误导。
- ⚙️ **`git blame --diff-algorithm`**：支持选择 diff 算法（如 histogram、patience），优化归因结果。
- 🧩 **对象数据库重构**：ODB 采用可插拔后端设计，为未来存储后端奠定基础。
- 📥 **`git backfill` 范围支持**：可指定修订范围和路径模式，仅下载部分历史中的缺失 blob。
- 🌍 **别名支持非 ASCII 字符**：通过新子节语法，别名可包含任意字符（如中文或瑞典语）。
- 🎯 **直方图 diff 算法修复**：修正压缩阶段可能跨越锚定行的问题，输出更紧凑的差异。

---

### [现在你看到了：无需代理的 Rails 上的 Vite——火星编年史，Evil Martians 团队博客](https://evilmartians.com/chronicles/now-you-see-it-vite-on-rails-without-the-proxy)

**原文标题**: [Now you see it: Vite on Rails without the proxy—Martian Chronicles, Evil Martians’ team blog](https://evilmartians.com/chronicles/now-you-see-it-vite-on-rails-without-the-proxy)

## 概述总结

本文介绍了如何在不使用代理的情况下，将 Vite 集成到 Rails 中，通过巧妙的“存根文件”技术，让 Propshaft 和 Vite 无缝协作，实现热模块替换、即时 CSS 反馈等现代前端开发体验。

- 🚀 **Vite 的优势**：提供热模块替换（HMR）、即时 CSS 反馈、单进程处理 JS/CSS、自动代码分割，以及丰富的插件生态（React、Vue、Svelte 等）。
- 🧩 **核心创新**：通过一个存根文件（stub）在 `app/assets/builds/` 中，将浏览器请求重定向到 Vite 开发服务器，Propshaft 无需感知 Vite 的存在。
- 🎨 **CSS 处理技巧**：CSS 通过 JS 导入注入 `<style>` 标签，实现无刷新样式更新；生产环境则生成真实 CSS 文件。
- 🔄 **生产环境双重文件**：Vite 输出哈希文件后，存根文件重新导出真实包，确保模块身份一致，避免缓存问题。
- 🛠️ **迁移示例**：从 esbuild 迁移只需三步：安装 npm 包、配置 Vite、更新 Procfile；Tailwind 用户可替换为 `@tailwindcss/vite`。
- 📦 **部署不变**：`yarn build` 改为 `vite build`，CI/Docker/Heroku 等流程无需调整。
- 💎 **Gem 模式**：提供 `vite_tags` 等辅助方法，直接输出指向 Vite 的标签，支持 CSP nonce、`vite_image_tag` 等高级功能，无存根层。
- 🔍 **注意事项**：存根模式增加一次开发跳转；CSS 绕过 `stylesheet_link_tag` 可能影响 CSP；`package.json` 需添加 `"type": "module"`。
- 🎭 **魔术揭秘**：整个方案让 Vite 对 Rails 透明，两者互不妥协，已在 Evil Martians 客户项目和生产环境中验证。

---

### [Vite | 下一代前端工具](https://vite.dev/)

**原文标题**: [Vite | Next Generation Frontend Tooling](https://vite.dev/)

Vite 是一个为现代 Web 应用提供极速体验的开源前端构建工具。

- 🚀 **极速开发体验**：基于原生 ESM 实现按需文件服务，依赖预构建极快，并支持闪电般的热模块替换（HMR）。
- 🛠️ **开箱即用的丰富功能**：原生支持 TypeScript、JSX、CSS、WebAssembly 等，并通过插件系统轻松扩展。
- ⚡ **优化的构建输出**：利用 Rolldown 实现高级 tree-shaking、内置压缩和精细的代码分割控制。
- 🔌 **灵活且强大的插件系统**：继承 Rollup 的插件接口并添加 Vite 专属选项，支持完全类型化的 API 和一流 SSR 支持。
- 🤝 **社区与生态系统**：拥有 80k+ GitHub 星标和 80m+ 周 npm 下载量，被众多主流框架和工具采用，如 SolidJS、Svelte、React 等。
- 💬 **社区赞誉**：多位技术领袖（如 Ryan Carniato、Rich Harris）称赞 Vite 是 JavaScript 世界的“联合国”，带来纯粹的开发愉悦感。
- 🆓 **免费开源**：采用 MIT 许可，永远免费开源，由贡献者和赞助商支持。

---

### [GitHub 虚假星标经济内幕 | 了不起的智能体](https://awesomeagents.ai/news/github-fake-stars-investigation/)

**原文标题**: [Inside GitHub's Fake Star Economy | Awesome Agents](https://awesomeagents.ai/news/github-fake-stars-investigation/)

## 概述总结
GitHub 虚假星标经济已形成成熟产业链，通过购买星标可人为推高项目热度，进而影响VC投资决策，而平台和监管的滞后使得这一问题持续恶化。

- 🔍 **规模惊人**：CMU研究发现GitHub上存在约**600万虚假星标**，分布于18,617个仓库，涉及30.1万个账号，2024年问题急剧恶化
- 💰 **价格透明**：星标售价从**0.03美元到0.85美元**不等，通过Fiverr、Telegram等公开渠道即可购买，无需暗网
- 📊 **检测信号**：我们的分析发现，被操纵仓库的**fork与星标比**极低（如FreeDomain仅0.017），且**36-76%的星标用户零粉丝**
- 🏢 **AI/区块链重灾区**：AI和LLM仓库是最大非恶意虚假星标接收类别，区块链项目则呈现最明显的操纵特征
- 💼 **投资转化链**：VC明确将星标数作为投资信号（种子轮中位数2,850星），购买星标成本仅需85-285美元，而种子轮融资可达100-1000万美元
- ⚖️ **法律风险**：FTC 2024年新规禁止虚假社交影响力指标，每次违规罚款**53,088美元**；SEC已对夸大融资指标的创始人提起欺诈诉讼
- 🔧 **平台应对不足**：GitHub虽禁止虚假互动，但仅删除90%被标记仓库，57%的虚假账号仍保留，且未实施加权流行度指标
- 🚨 **替代方案**：VC应关注**月活跃贡献者**、包下载量、问题质量等真实指标，fork与星标比是最简单的一阶检测工具

---

### [从DigitalOcean迁移到Hetzner：月费从1432美元降至233美元，零停机时间 :: Isa Yeter](https://isayeter.com/posts/digitalocean-to-hetzner-migration/)

**原文标题**: [Migrating from DigitalOcean to Hetzner: From $1,432 to $233/month With Zero Downtime :: Isa Yeter](https://isayeter.com/posts/digitalocean-to-hetzner-migration/)

### 概述总结
从DigitalOcean迁移到Hetzner的完整实战记录，成功将月费从$1,432降至$233，实现零停机迁移248GB MySQL数据库、34个Nginx站点及多个生产级服务。

- 💰 **成本节省显著**：迁移后每月节省$1,199（年省$14,388），新服务器配置更高（96核CPU/256GB DDR5/2TB NVMe RAID1）
- 🚀 **零停机策略**：采用6阶段迁移方案（安装→同步→主从复制→DNS优化→反向代理→切换），全程无服务中断
- 🗄️ **MySQL高效迁移**：使用mydumper并行导出（32线程）替代mysqldump，将数天工作缩短至数小时；通过主从复制实现实时同步
- 🔧 **关键问题解决**：处理了MySQL 5.7→8.0的sys表结构异常、SUPER权限绕过read_only限制、重复键错误等迁移陷阱
- 🌐 **DNS平滑过渡**：通过DigitalOcean API批量降低A/AAAA记录TTL至300秒，配合反向代理确保DNS传播期间请求不中断
- 📜 **自动化脚本**：开源所有Python脚本（DNS管理/配置转换/数据校验），支持DRY_RUN模式安全预览变更
- ⚡ **性能提升**：MySQL 8.0优化器显著提升查询速度，GitLab webhooks自动更新，最终实现24小时完成迁移且用户无感知

---

### [为Cloudflare构建CLI](https://blog.cloudflare.com/cf-cli-local-explorer/)

**原文标题**: [Building a CLI for all of Cloudflare](https://blog.cloudflare.com/cf-cli-local-explorer/)

Cloudflare 正在重建其 CLI 工具 Wrangler，使其成为覆盖所有 Cloudflare 产品的统一命令行界面，并引入本地开发探索器，以提升开发者和 AI 代理的使用体验。

- 🔧 重建 Wrangler CLI：目标是为所有 Cloudflare 产品提供统一的 CLI 命令，支持基础设施即代码配置，当前已发布技术预览版（可通过 `npx cf` 或 `npm install -g cf` 试用）。
- 📜 引入 TypeScript 模式：为解决 OpenAPI 模式局限性，Cloudflare 创建了新的 TypeScript 模式，用于定义 API、CLI 命令和上下文，确保生成接口的一致性，并仍能生成 OpenAPI 模式。
- 🤖 针对 AI 代理优化：强调 CLI 命令一致性（如统一使用 `get` 而非 `info`），并确保输出清晰指示操作作用于本地还是远程资源，避免代理混淆。
- 🖥️ 发布 Local Explorer：在 Wrangler 和 Vite 插件中开放测试，允许开发者本地查看和管理 KV、R2、D1 等模拟资源，无需逆向工程或第三方工具。
- 🔗 本地 API 镜像：通过 `/cdn-cgi/explorer/api` 提供本地 OpenAPI 接口，代理可直接管理本地资源，实现本地与远程 API 形状一致。
- 💡 征求反馈：鼓励用户分享对 Cloudflare 全平台 CLI 的期望，如希望简化的一行命令或配置项，并加入 Discord 社区提供建议。

---

