### [JavaScript 周刊第 788 期：2026 年 6 月 2 日](https://javascriptweekly.com/issues/788)

**原文标题**: [JavaScript Weekly Issue 788: June 2, 2026](https://javascriptweekly.com/issues/788)

以下是 JavaScript Weekly 第 788 期的内容摘要：

JavaScript Weekly 为您带来本周最新动态，涵盖工具、库、文章和社区新闻。

- 🚀 **Hocuspocus 4**：基于 Yjs 的实时协作后端，支持 Node、Bun、Deno 和 Cloudflare Workers，快速实现多用户协作功能。
- 🤖 **Meticulous AI**：自动生成 E2E UI 测试套件，提供全面覆盖率，无需开发者额外努力，已被 Notion、Dropbox 等采用。
- 📋 **如何评估 npm 包（2026 版）**：实用检查清单，涵盖来源证明、安装脚本、CI 质量和维护者响应性，帮助识别风险。
- 🕒 **date-fns 准备转向 Temporal**：v4.4 已发布，v5.0 进入 alpha 阶段，未来将成为“Temporal 优先”库。
- 🔒 **Red Hat npm 包被后门攻击**：最新安全事件中，数十个 Red Hat 包被植入后门。
- 🎉 **npm 11.16.0**：新增`allowScripts`安装脚本策略的初始支持（仅警告）。
- 📊 **Plotly 3.6**：声明式图表库，支持 50 多种可视化类型，如基本图表、地图和热力图。
- 🛠 **Expo UI 稳定版**：从 JS 原生调用 SwiftUI 和 Jetpack Compose，支持 7 个社区包的替代品。
- 🎉 **tsParticles 4**：粒子引擎，用于创建五彩纸屑、烟花等网页效果，支持所有主流框架。
- 📝 **officeParser 7.1**：解析 Office 文件（docx、pptx 等）为 AST，提供浏览器演示。
- 🔎 **Fuse.js 7.4**：模糊搜索库，新增基于 Web Workers 的并行搜索支持。
- 📄 **CSS vs JavaScript 动画**：性能差异对比及选择指南。
- 📄 **递归谎言**：ES2015 的尾调用优化在 2026 年多数引擎中未实现。
- 🛠 **Component Party**：UI 库代码对比工具，涵盖 React、Vue、Svelte 等框架。
- 🎧 **Anders Hejlsberg 访谈**：讨论 TypeScript、JavaScript 优缺点及 AI 使用。
- 🤖 **State of Web Dev AI 2026 调查结果**：来自 7000 多名开发者的 AI 使用统计数据。

---

### [Hocuspocus | Tiptap 协作文档](https://tiptap.dev/docs/hocuspocus/getting-started/overview)

**原文标题**: [Hocuspocus | Tiptap Collaboration Docs](https://tiptap.dev/docs/hocuspocus/getting-started/overview)

Hocuspocus 是一套基于 Y.js 的协作工具套件，旨在为应用添加实时同步、离线优先和冲突解决功能，支持从简单集成到百万级用户扩展。

- 🧩 基于 Y.js 构建，可实现无冲突的实时数据合并与同步
- ⚡ 采用 CRDT 技术，性能卓越，变更顺序不影响最终结果（类似 Git）
- 📡 提供 WebSocket 后端服务器，支持快速集成与扩展
- 🔄 支持离线优先应用，后期同步变更并自动解决冲突
- 🖊️ 集成协作文本编辑（兼容 Tiptap、Slate、Quill、Monaco 等编辑器）
- 🔗 可融入现有应用，并通过 Webhook 发送变更
- 📈 借助 Redis 可扩展至百万用户
- 💻 使用 TypeScript 编写，支持 Node.js、Bun、Deno 及 Cloudflare Workers
- ⚛️ 提供 React 官方绑定（@hocuspocus/provider-react）

---

### [Yjs | 首页](https://yjs.dev/)

**原文标题**: [Yjs | Homepage](https://yjs.dev/)

概述总结  
- 📚 Yjs 是一个用于构建实时协作应用的库，提供自动同步的共享数据类型。  
- 🔄 支持自动同步，共享类型像普通数据类型一样操作，但数据自动同步。  
- 📡 支持离线存储，数据可保存在本地数据库（如 IndexedDB），先渲染再同步。  
- 🌐 网络无关，无需中央服务器，支持去中心化系统，更快速、可扩展、容错性强。  
- 🧩 生态系统丰富，集成流行编辑器库和 Web 框架。  
- 💻 客户端层包括共享数据类型、意识 CRDT 和编辑器绑定。  
- 🔗 连接层支持多种协议，如 WebSocket、WebRTC、Matrix 等。  
- 💾 持久化层支持 IndexedDB、LevelDB、Redis 等数据库。  
- 🌍 语言绑定支持多种语言（如 Rust、Python、Swift 等）。  
- 🏢 服务提供商包括 Y-Sweet、Synergy Codes、Liveblocks、Hocuspocus 等。  
- 🎮 提供演示如 Prosemirror 编辑器、版本控制、实时追踪、绘图等。  
- 📈 每周下载量超过 90 万，被 Proton Docs、NextCloud、Evernote 等知名应用使用。  
- 👥 社区资源包括文档、GitHub、论坛、Discord 等。  
- 🏆 由 Kevin Jahns 构建和管理，网站由 Felicia Chang 贡献。

---

### [GitHub - ueberdosis/hocuspocus：用于应用中无冲突实时协作的Yjs CRDT WebSocket 后端。](https://github.com/ueberdosis/hocuspocus)

**原文标题**: [GitHub - ueberdosis/hocuspocus: The Yjs CRDT WebSocket backend for conflict-free real-time collaboration in your app. · GitHub](https://github.com/ueberdosis/hocuspocus)

Hocuspocus 是一个基于 Y.js 的即插即用协作后端，用于实现无冲突的实时协同编辑。

- 🔌 提供 WebSocket 服务器，支持快速集成实时协作功能
- 📖 完整文档位于 hocuspocus.dev/introduction
- ☁️ 提供云托管服务：Tiptap Collab
- 🧩 支持 SQLite 等扩展，示例配置简单易用
- 💬 社区支持通过 Tiptap Discord 服务器交流
- 💖 由 Tiptap、Cargo、Saga 等赞助商支持
- 🤝 欢迎贡献，初始作者为 kris
- 📜 采用 MIT 许可证开源
- ⭐ GitHub 上获得 2.4k 星标，200 个分支
- 🏷️ 标签包括实时、ProseMirror、自托管、CRDT、Yjs、协同编辑、SlateJS、Tiptap

---

### [Meticulous AI - 无需编写测试的自动化前端测试](https://www.meticulous.ai/?utm_source=jsweekly&utm_medium=referral&utm_campaign=26q2&utm_content=primary)

**原文标题**: [Meticulous AI - Automated Frontend Testing Without Writing Tests](https://www.meticulous.ai/?utm_source=jsweekly&utm_medium=referral&utm_campaign=26q2&utm_content=primary)

Meticulous 是一款自动化、全面且确定性的测试工具，能够零开发工作量地生成和维护测试套件，帮助团队快速、可靠地交付代码。

- 🚀 **零开发工作量**：自动录制开发交互，生成并维护覆盖所有代码路径和用户流程的测试套件。
- 🧪 **彻底且无碎片**：从 Chromium 级别构建确定性调度引擎，彻底消除测试碎片，确保测试快速且可靠。
- ⏱️ **闪电般快速**：测试在计算集群上高度并行化，可在 120 秒内测试数千个屏幕。
- 🔄 **自动演化**：测试套件随应用自动更新，新增或移除测试，无需手动干预。
- 🔒 **安全集成**：支持 NextJS、React、Vue 等主流框架，通过简单脚本标签即可集成。
- 🏢 **行业信赖**：已被 Dropbox、Notion 等超过 100 家组织采用，工程师反馈“无法想象没有它的工作”。
- 📈 **提升迭代速度**：大幅提高可靠、无回归代码的交付速度，支持与现有测试套件互补或完全替代。

---

### [如何评估一个 npm 包 - 2026 版](https://blog.gaborkoos.com/posts/2026-05-29-How-to-Evaluate-an-npm-Package-2026-Edition/)

**原文标题**: [How to Evaluate an npm Package - 2026 Edition](https://blog.gaborkoos.com/posts/2026-05-29-How-to-Evaluate-an-npm-Package-2026-Edition/)

### 概述总结
本文提供了评估 npm 包的详细流程，强调在安装前进行 5-10 分钟的安全与质量检查，以降低供应链攻击风险，并做出明智决策。

- 📦 **你真的需要这个包吗？** 先问自己是否必须依赖它。进行“移除测试”：如果包消失，替换难度有多大？小工具函数是否可自己实现？检查依赖数量，减少攻击面。
- 🔍 **它是否活跃维护？** 查看 GitHub Issues 中未回复的旧问题、排除机器人后的真实提交、维护者人数（避免单点故障）。检查 npm 版本发布节奏和 CHANGELOG 质量，好的 CHANGELOG 会说明变更原因。
- 🔐 **你能信任发布到 npm 的内容吗？** 检查“来源证明”（Provenance）徽章，确认发布包与 GitHub 提交对应。使用`npm audit signatures`验证。查看发布工作流是否使用 OIDC 信任发布（无长期令牌）。警惕安装脚本（preinstall/postinstall），无正当理由的脚本是危险信号。
- 🛠️ **CI 流水线是真实的还是装饰性的？** 检查 Actions 是否在 PR 上触发，PR 合并前是否通过 CI。查看测试配置文件是否有覆盖率阈值（如 90%）。测试文件结构是否与源码对应。
- 📝 **代码质量是否可见？** 检查 lint 配置是否非空、`package.json`的`exports`字段是否现代、`prepublishOnly`脚本是否存在。TypeScript 包检查`strict: true`，搜索`any`和`@ts-ignore`的滥用。
- ⚠️ **出问题时怎么办？** 查找`SECURITY.md`文件。查看 GitHub Security 选项卡的 Advisories。使用 osv.dev 或 snyk.io 检查已知漏洞。用 Socket.dev 进行行为分析（网络访问、文件系统操作、混淆代码）。检查安全问题的响应速度。
- ✅ **快速检查清单**：①真的需要吗？②有来源证明吗？③有无不明安装脚本？生产关键包额外检查：维护者是否响应。

---

### [date-fns - 现代 JavaScript 日期实用工具库](https://date-fns.org/)

**原文标题**: [date-fns - modern JavaScript date utility library](https://date-fns.org/)

概述摘要  
- 🧠 文章核心探讨了人工智能在医疗诊断中的革命性应用，强调其提升准确性与效率的潜力。  
- 📊 通过分析大量医学影像数据，AI 能识别早期病变，如癌症或视网膜疾病，比传统方法更敏感。  
- 🚀 深度学习模型在临床试验中表现优异，误诊率降低约 30%，尤其适用于资源匮乏地区。  
- ⚖️ 但文章也指出挑战：数据隐私、算法偏见及监管框架缺失可能阻碍广泛部署。  
- 🤝 最终建议人机协作模式，即 AI 辅助医生决策，而非完全替代，以平衡创新与安全。

---

### [date-fns - 现代 JavaScript 日期实用工具库](https://date-fns.org/you-dont-need-date-fns)

**原文标题**: [date-fns - modern JavaScript date utility library](https://date-fns.org/you-dont-need-date-fns)

概述总结：文章探讨了人工智能在医疗诊断中的最新应用，强调其提升准确性与效率的潜力，同时指出数据隐私和算法偏见等挑战。

- 🧠 人工智能通过深度学习分析医学影像，能比人类医生更早发现病变迹象。
- ⏱️ 自动化诊断系统大幅缩短了报告生成时间，使医生能更专注于复杂病例。
- 🔒 患者数据的安全存储与共享是主要障碍，需严格遵循隐私法规。
- ⚖️ 算法偏见可能导致对特定人群的诊断误差，需持续优化训练数据集。
- 🤝 人机协作模式被证明最有效，AI 辅助而非替代医生的决策过程。

---

### [发布 v4.4.0 · date-fns/date-fns · GitHub](https://github.com/date-fns/date-fns/releases/tag/v4.4.0)

**原文标题**: [Release v4.4.0 · date-fns/date-fns · GitHub](https://github.com/date-fns/date-fns/releases/tag/v4.4.0)

概述摘要  
date-fns 发布了 v4.4.0 版本，重点优化了 CDN 使用方式，通过引入新包 @date-fns/cdn 并弃用旧 CDN 脚本，显著减小了压缩包体积，同时为未来版本进一步优化奠定了基础。

- 📦 引入 @date-fns/cdn 包，取代旧 date-fns CDN 脚本，压缩包体积从 5.83 MB 降至 3.96 MB  
- 🚀 v5.0.0-alpha.0 中完全移除旧 CDN 脚本，体积进一步减至 2.89 MB  
- ⚠️ 旧 date-fns CDN 脚本已弃用，将在下一个主版本中移除，建议用户迁移至 @date-fns/cdn  
- 🗑️ 移除了旧 CDN 的源映射文件以减小体积，新包 @date-fns/cdn 仍包含它们  
- 🔮 这是体积优化的第一步，未来 v4 和 v5 版本将继续缩减大小

---

### [发布 v5.0.0-alpha.0 · date-fns/date-fns · GitHub](https://github.com/date-fns/date-fns/releases/tag/v5.0.0-alpha.0)

**原文标题**: [Release v5.0.0-alpha.0 · date-fns/date-fns · GitHub](https://github.com/date-fns/date-fns/releases/tag/v5.0.0-alpha.0)

date-fns v5.0.0-alpha.0 版本发布，主要聚焦于减小包体积，并将 CDN 脚本移至独立包。

- 📦 包体积大幅减小：从 v4.3.0 的 5.83 MB 压缩至 2.89 MB，优化显著。
- 🔄 CDN 脚本迁移：从 `date-fns` 包移至独立的 `@date-fns/cdn` 包，需更新引用链接。
- 🚀 持续优化预告：本次仅为第一步，未来版本将进一步减小包体积。
- ⚠️ 重要变更说明：旧版 CDN 链接（如 `cdn.jsdelivr.net/npm/date-fns/cdn.min.js`）将自动重定向至新路径，但建议用户手动更新。

---

### [迷你沙胡鲁德活动影响红帽云服务 npm 包...](https://socket.dev/blog/mini-shai-hulud-campaign-hits-red-hat-cloud-services-npm-packages)

**原文标题**: [Mini Shai-Hulud Campaign Hits Red Hat Cloud Services npm Pac...](https://socket.dev/blog/mini-shai-hulud-campaign-hits-red-hat-cloud-services-npm-packages)

概述：朝鲜黑客组织通过篡改 Packagist 上的 PHP 包和 GitHub 分支，针对 PHP 开发者分发恶意软件加载器，利用类似“传染性面试”的诱饵执行远程代码。

- 🎯 朝鲜黑客组织“千里马”瞄准 PHP 开发者，通过被攻陷的 Packagist 包传播恶意软件。
- 📦 恶意加载器隐藏在 Packagist 列表中的 PHP 包及其 GitHub 分支内。
- 🔄 该加载器用于获取并执行远程代码，实现远程控制。
- 🕵️ 攻击手法疑似采用“传染性面试”式诱饵，诱导开发者安装恶意包。
- ⚠️ 开发者需警惕来源不明的 PHP 包，尤其是涉及招聘或面试场景的。

---

### [数十个 Red Hat 软件包通过其官方 NPM 渠道被植入后门 - Ars Technica](https://arstechnica.com/security/2026/06/dozens-of-red-hat-packages-backdoored-through-its-offical-npm-channel/)

**原文标题**: [Dozens of Red Hat packages backdoored through its official NPM channel - Ars Technica](https://arstechnica.com/security/2026/06/dozens-of-red-hat-packages-backdoored-through-its-offical-npm-channel/)

### 概述总结
Red Hat 官方 NPM 账户遭入侵，导致数十个软件包被植入恶意蠕虫，窃取敏感凭证并横向传播，建议受影响者立即调查。

- 🔐 攻击通过入侵 Red Hat 官方 NPM 命名空间@redhat-cloud-services 实施，涉及 30 多个软件包。
- 🐛 恶意蠕虫“Shai-Hulud”在 npm 安装过程中执行，窃取 GitHub 密钥、npm 令牌、Kubernetes 凭证等敏感信息。
- 🔄 蠕虫具有自我传播能力，通过已感染设备访问的第三方账户重新发布后门软件包。
- ⚙️ 攻击重点针对 CI/CD 系统，利用 GitHub Actions OIDC 凭证传播，表明 Red Hat 的 CI/CD 管道可能已遭入侵。
- 🚨 Red Hat 已移除恶意软件包，并声称未影响客户或生产系统，但建议 36 小时内接触过受影响软件包的人员立即调查。
- 📋 安全公司 Socket 和 Aikido 提供了受影响软件包列表及入侵指标，供潜在受害者使用。
- ⚠️ 此类攻击可能源于此前供应链攻击，且恢复难度大，如 Checkmarx 案例所示，需彻底排查。

---

### [发布 v11.16.0 · npm/cli · GitHub](https://github.com/npm/cli/releases/tag/v11.16.0)

**原文标题**: [Release v11.16.0 · npm/cli · GitHub](https://github.com/npm/cli/releases/tag/v11.16.0)

npm CLI v11.16.0 版本发布，包含新功能、错误修复、文档更新和依赖升级。

- 🚀 新增 `publish --access=private` 别名，用于限制发布权限  
- 🛡️ 引入 `allowScripts` 选择性安装脚本策略的第一阶段，增强安全性  
- 🐛 修复 `fullMetadata` 拼写错误  
- ⏸️ 配置：在交互式编辑器启动时暂停进度旋转器，提升体验  
- 📚 记录 `npm_old_version` 和 `npm_new_version` 环境变量  
- 📦 更新多项依赖，包括 `undici@6.26.0`、`sigstore@4.1.1`、`lru-cache@11.5.1` 等  
- 🧹 清理开发依赖，并优化标志表中的换行符处理  
- 👥 感谢 claude、36degrees 等贡献者的参与

---

### [特性：`allowScripts` 可选安装脚本策略的第一阶段 —— JamieMagee · 拉取请求 #9360 · npm/cli · GitHub](https://github.com/npm/cli/pull/9360)

**原文标题**: [feat: Phase 1 of `allowScripts` opt-in install-script policy by JamieMagee · Pull Request #9360 · npm/cli · GitHub](https://github.com/npm/cli/pull/9360)

npm CLI 的 `allowScripts` 功能第一阶段已合并，使依赖安装脚本变为可选加入。

- 🚀 **新增 `allowScripts` 字段**：在 `package.json` 中新增 `allowScripts` 字段，用于管理依赖安装脚本的权限。
- ⚙️ **新增三个配置项**：`allow-scripts`、`strict-script-builds` 和 `dangerously-allow-all-scripts`，后两个在本阶段为无操作占位符。
- 🛠️ **新增命令**：`npm approve-scripts` 和 `npm deny-scripts`，用于批准或拒绝脚本，批准可固定版本，拒绝仅限名称。
- ⚠️ **安装时警告**：在 `npm install`、`ci`、`update` 和 `rebuild` 结束时，列出未审查安装脚本的包。
- 🆔 **身份匹配器**：在 `@npmcli/arborist` 中实现，覆盖注册表、Git、文件和远程压缩包，别名匹配底层注册包。
- 📦 **捆绑依赖处理**：有安装脚本的捆绑依赖被标记为未审查，且无法在第一阶段加入白名单。
- 🔄 **工作区警告**：当非根工作区声明自己的 `allowScripts` 时发出警告。
- 🚫 **故意推迟的功能**：实际阻止脚本运行（将在第二阶段实现），以及捆绑依赖的安全白名单语法。

---

### [Svelte 2026 年 6 月新特性](https://svelte.dev/blog/whats-new-in-svelte-june-2026)

**原文标题**: [What’s new in Svelte: June 2026](https://svelte.dev/blog/whats-new-in-svelte-june-2026)

Svelte 2026 年 6 月更新带来了 SvelteKit 表单与远程功能的重大改进，新增实时查询 API，并支持 TypeScript 6，同时社区生态也涌现了众多新工具和资源。

- 📋 SvelteKit 表单增强：`submit` 现在返回布尔值指示表单有效性，远程表单字段可直接接受布尔值和数字
- 🔄 远程查询 API 更新：新增 `query.live(...)` 支持长连接实时数据订阅，`requested(...)` 现在需要 `limit` 参数并返回 `{ arg, query }`
- ⚠️ 破坏性变更：`.run()` 方法已移除，需直接使用 `await query()`；增强回调现在接收远程函数实例副本而非 `{ form, data, submit }` 对象
- 🛠️ Svelte 编译器改进：模板现在允许直接在标记中声明变量（svelte@5.56.0）
- 🏷️ TypeScript 6 支持：语言工具（language-tools）全面支持 TypeScript 6.0
- 🚀 开发体验优化：vite-plugin-svelte 在开发环境中为服务器启用优化器，Svelte MCP 的 stdio 模式可直接读取文件内容
- 🌐 社区应用展示：包括 ASCII 风格浏览器游戏、电影猜谜游戏、开源 P2P 卡牌平台、画布构建器、微控制器编程工作区等
- 📚 学习资源：《This Week in Svelte》系列视频，以及关于 Svelte 优于 React、自动化 LinkedIn 轮播图、多人游戏开发等文章
- 🧩 新库与工具：Huey 颜色选择器、50+ 点阵加载器、纸片着色器、PDF 查看器、事件日历、Convex 认证 UI、Aphex CMS、SvelteESP32 v3.0 等
- 🔌 插件与集成：Tailwind CSS 自动引用注入、SvelteKit 代理、WebSocket 支持等

---

### [Ember 7.0 发布](https://blog.emberjs.com/ember-released-7-0/)

**原文标题**: [Ember 7.0 Released](https://blog.emberjs.com/ember-released-7-0/)

Ember 7.0 已发布，该版本移除了 6.x 系列中弃用的功能，并包含多项错误修复，同时 6.12 成为 LTS 版本。

- 🎉 新版本遵循主要版本政策，仅移除已弃用功能，无新增 API
- 📦 6.x 系列带来重大改进：Embroider+Vite 构建系统、严格模式组件、原生集合类型跟踪等
- 🛠️ 升级路径：建议逐步升级至 6.12，解决所有弃用警告后再升级至 7.0
- 🗑️ 7.0 移除的关键弃用：`import Ember from 'ember'`、AMD 包发布、`@ember/service` 的 `inject` 导入
- 🐛 包含多项错误修复：如 LinkTo 在 SVG 中的问题、跟踪集合的 delete() 行为、each 循环空值处理等
- 🧩 Ember CLI 7.0 仅移除已弃用 API，无新功能或修复
- 🙏 感谢社区贡献者支持，使这一主要版本周期成为可能

---

### [Node.js — Node.js 26.3.0（当前版本）](https://nodejs.org/en/blog/release/v26.3.0)

**原文标题**: [Node.js — Node.js 26.3.0 (Current)](https://nodejs.org/en/blog/release/v26.3.0)

Node.js 26.3.0 版本发布，包含多项新功能和改进，同时提醒 macOS 通用二进制可能面临变更。

- ⚠️ **macOS 通用二进制可能调整**：由于苹果逐步放弃 Intel 架构，Node.js 可能无法在 26 版本生命周期内持续提供通用二进制，但当前仍会尽力支持。
- 📦 **Buffer.poolSize 默认值提升至 64 KiB**：小幅提升内存分配效率。
- 🔒 **更新根证书至 NSS 3.123.1**：确保证书信任列表保持最新。
- 🛡️ **新增 httpValidation 选项**：可配置 HTTP 头值验证，增强安全性。
- 🔍 **暴露精确覆盖率起始信息**：Inspector 模块支持向 JS 运行时提供更细粒度的代码覆盖数据。
- 🚫 **新增 permission.drop 功能**：允许在运行时动态撤销权限，提升权限控制灵活性。
- 📈 **npm 升级至 11.16.0**：包含多项依赖更新和修复。
- 🚀 **QUIC 模块大量改进**：包括速率限制、主机名验证、流空闲超时、性能优化等。
- 🛠️ **Stream 模块多项修复**：修复同步 drain 挂起、迭代器抛出时拒绝待处理读取等问题。
- 🧪 **测试运行器优化**：修复重试失败测试的覆盖问题，改进事件报告和诊断通道。
- 🐛 **修复多个安全与稳定性问题**：包括 SAB-backed Buffer 编码竞态条件、WebCrypto 原型污染防护等。

---

### [文档：将 macOS x64 降级为二级支持（由 aduh95 提交）· 拉取请求 #63055 · nodejs/node · GitHub](https://github.com/nodejs/node/pull/63055)

**原文标题**: [doc: downgrade macOS x64 to Tier 2 by aduh95 · Pull Request #63055 · nodejs/node · GitHub](https://github.com/nodejs/node/pull/63055)

Node.js 将 macOS x64 支持降级为 Tier 2 级别，以应对 Apple 终止 Rosetta 模拟器的计划。

- 🍎 Apple 宣布即将终止 Rosetta 模拟器，导致 Node.js 无法在 macOS 27 生命周期内继续提供 x64 兼容二进制文件
- 📉 macOS x64 下载量（30 天内 148 万次）远低于 arm64 版本（571 万次），且约 40% 的 x64 流量来自 GitHub Actions 的 Intel Mac 镜像
- 🏗️ 降级为 Tier 2 意味着该平台仍会获得完整测试覆盖，但基础设施问题可能延迟二进制文件发布
- ⏰ 此变更已合并到 Node.js 26.3.0 版本，并将在 v26.x 分支中继续支持，但不会在 v22.x、v24.x 和 v25.x 中落地
- 🧪 社区讨论中，部分成员建议直接降级为 Experimental 级别，但最终决定保持 Tier 2 以确保当前基础设施能继续支持
- 🔧 Homebrew 和 nixpkgs 等依赖管理工具也计划在 2027 年前后停止 x86 支持，进一步推动此决策

---

### [Astro 6.4 | Astro](https://astro.build/blog/astro-640/)

**原文标题**: [Astro 6.4 | Astro](https://astro.build/blog/astro-640/)

Astro 6.4 正式发布，带来可插拔的 Markdown 处理管道、基于 Rust 的新 Markdown 处理器 Sätteri，以及 Cloudflare 高级路由辅助工具。

- 🚀 **新的 `markdown.processor` API**：允许完全替换 Markdown 处理管道，默认仍使用 unified，但支持自定义处理器，现有 remark/rehype 插件可迁移至处理器内配置。
- ⚡ **更快的 Markdown 构建**：引入基于 Rust 的 `@astrojs/markdown-satteri` 包，构建速度显著提升（如 Astro 和 Cloudflare 文档站点节省超一分钟），但暂不支持 unified 插件。
- ☁️ **Cloudflare 高级路由辅助**：`@astrojs/cloudflare` 新增 `cf()` 辅助函数，支持 SESSION KV 绑定、静态资源服务、`locals.cfContext`、客户端地址、`waitUntil` 及预渲染错误页面，适用于自定义 fetch 处理器和 Hono 中间件。
- 🔧 **升级指南**：可使用 `@astrojs/upgrade` CLI 工具自动升级，或通过 npm/pnpm/yarn 手动升级至最新版本。
- 🎉 **社区与贡献**：感谢所有贡献者，包括核心团队和众多社区成员，新 Astro 周边商品已上线商店。

---

### [发布 pnpm 11.5 · pnpm/pnpm · GitHub](https://github.com/pnpm/pnpm/releases/tag/v11.5.0)

**原文标题**: [Release pnpm 11.5 · pnpm/pnpm · GitHub](https://github.com/pnpm/pnpm/releases/tag/v11.5.0)

pnpm v11.5.0 发布，包含多项改进和错误修复。

- 🚀 **新增 `hoistingLimits` 设置**：用于 `nodeLinker: hoisted` 安装，支持 `none`、`workspaces` 和 `dependencies` 选项，控制依赖提升范围。
- 🖥️ **交互式提示升级**：用 `@inquirer/prompts` 替换 `enquirer`，修复 `pnpm update -i` 等命令的滚动溢出问题，并保持 `j`/`k` 键导航功能。
- 🔒 **阶段发布信任增强**：当包元数据包含 `approver` 字段时，视为最高信任级别（高于受信任发布者和来源证明），防止信任降级错误。
- 🐛 **修复对等依赖死锁**：解决别名安装中相互对等依赖循环导致的 pnpm 挂起问题，通过缓存短路避免死锁。
- 🔑 **修复 dist-tag 操作**：`pnpm dist-tag add` 和 `rm` 现在支持浏览器 2FA 流程，无需手动 `--otp` 参数。
- ⏳ **修复 `minimumReleaseAgeExclude` 处理**：确保排除的包不会因快速路径而固定到过时版本。
- 🗂️ **修复锁文件完整性丢失**：非注册表 HTTPS tarball 依赖项的 `integrity` 字段在重新安装后不再丢失，避免 `--frozen-lockfile` 失败。
- 🔄 **优化缺失锁文件恢复**：当 `pnpm-lock.yaml` 缺失但 `node_modules/.pnpm/lock.yaml` 存在时，直接复用快照生成锁文件，减少重新解析。

---

### [发布 pnpm 11.5.1 · pnpm/pnpm · GitHub](https://github.com/pnpm/pnpm/releases/tag/v11.5.1)

**原文标题**: [Release pnpm 11.5.1 · pnpm/pnpm · GitHub](https://github.com/pnpm/pnpm/releases/tag/v11.5.1)

pnpm v11.5.1 版本发布，主要修复了多个依赖管理和发布流程中的问题，并提升了性能。

- 🚀 提升 `pnpm audit` 性能：通过修剪非漏洞锁文件子树，并在漏洞发现达到路径上限时停止路径枚举。
- 🛠️ 修复工作区状态缓存问题：避免因缓存部分写入或格式错误导致程序崩溃。
- ⚙️ 改进生命周期脚本：在无头安装期间，为根生命周期脚本设置 `npm_config_user_agent` 环境变量。
- 🔒 保留远程 tarball 完整性：重建锁文件条目时，保留远程（非注册表）tarball 依赖的 `integrity` 字段，防止后续安装因缺失完整性而失败（#12067）。
- 📦 标准化仓库字段：将字符串类型的 `repository` 字段转换为 `{ type, url }` 对象形式，以兼容 Gitea/Codeberg 等注册表，避免 `pnpm publish` 时出现 500 错误（#12099）。
- 🧩 保留兼容的可选 peer 依赖：在解析依赖时，保留锁文件中已有的兼容可选 peer 版本。
- 🔍 修复钻石依赖解析不一致：当包同时 peer 依赖另一个包及其 peer 依赖（如 `@typescript-eslint/eslint-plugin` 依赖 `@typescript-eslint/parser` 和 `typescript`）时，不再重用针对不同版本解析的共享 peer 实例（#12079）。

---

### [ESLint v10.4.1 发布 - ESLint - 可插拔的 JavaScript 代码检查工具](https://eslint.org/blog/2026/05/eslint-v10.4.1-released/)

**原文标题**: [ESLint v10.4.1 released - ESLint - Pluggable JavaScript Linter](https://eslint.org/blog/2026/05/eslint-v10.4.1-released/)

ESLint v10.4.1 是一个补丁版本，修复了多个错误并更新了文档和测试。

- 🐛 修复了 `@eslint/plugin-kit` 版本更新到 0.7.2 的问题
- 🔧 修复了委托命令传播失败的错误
- ⚡ 修复了 `prefer-arrow-callback` 在 `async` 后换行时的自动修复无效问题
- ❌ 修复了 `finally` 块中引用的误报
- 📦 添加了缺失的 `CodePath` 和 `CodePathSegment` 类型
- 📝 从 `max-params` 相关规则中移除了废弃规则
- 📝 从相关规则部分移除了多个废弃规则
- 🛠️ 修复了广告的 `display: none` 问题
- 🖥️ 将构建切换到 Node.js 24
- 📄 更新了 README 文件
- 🔍 澄清了规则废弃对象中的语义版本字符串
- 🧪 为规则测试添加了 `data` 属性
- 🧪 增加了 `CodePath` 类型覆盖率测试
- 🔄 更新了 `eslint-plugin-eslint-comments` 测试数据
- 🔧 声明了 `update-readme` 工作流的 `contents:read` 权限
- 🌐 更新了生态系统插件
- 🔒 在 Renovate 中忽略 fflate 更新
- ⬆️ 升级了 `pnpm/action-setup` 到 6.0.8
- 📊 增加了生态系统测试的 `maxBuffer`
- ⚙️ 更新了生态系统更新 PR 设置
- 🧪 为 `message-count` 添加了单元测试
- 🧪 添加了 `@eslint/markdown` 和 typescript-eslint 生态系统测试
- 🔧 内部使用 `includeIgnoreFile`
- 📌 固定了 `fflate@0.8.2` 版本
- 🔔 为生态系统测试失败运行 Discord 警报

---

### [发布 22.0.0-rc.3 · angular/angular · GitHub](https://github.com/angular/angular/releases/tag/v22.0.0-rc.3)

**原文标题**: [Release 22.0.0-rc.3 · angular/angular · GitHub](https://github.com/angular/angular/releases/tag/v22.0.0-rc.3)

Angular v22.0.0-rc.3 发布，包含多项核心修复与安全增强
- 🚀 新增预发布版本 v22.0.0-rc.3，基于 main 分支的 247 次提交
- 🛠️ common 模块：仅移除 URL 中字面量的 /index.html 后缀
- 📦 compiler 模块：将投影属性移至常量中
- 🔒 core 模块：使用 Object.create(null) 创建 LOCALE_DATA 以增强安全性
- 🔄 migrations 模块：确保安全可选链操作幂等
- 🌐 platform-server 模块：对可疑 URL 抛出异常，并限制协议相关 URL
- 🎉 获得 9 个 🎉、5 个 🚀 和 3 个 👀 反应

---

### [使用 AI 更慢地编写更好的代码 | 品茶论道](https://nolanlawson.com/2026/05/25/using-ai-to-write-better-code-more-slowly/)

**原文标题**: [Using AI to write better code more slowly | Read the Tea Leaves](https://nolanlawson.com/2026/05/25/using-ai-to-write-better-code-more-slowly/)

AI 可用于编写更高质量的代码，但过程会更慢，通过多模型审查和深度理解来提升代码库健康度。

- 🤖 **AI 的灵活用法**：LLM 不仅能快速生成低质量代码（“slop cannon”），也能用于编写高质量代码，关键在于使用方式。
- 🐛 **强大的 Bug 发现能力**：像 Mythos 等 AI 模型在代码审查中能发现大量 Bug，包括关键安全漏洞、性能问题和误导性注释。
- 🛠️ **多模型协作审查**：使用 Claude、Codex、Cursor Bugbot 等多个 AI 模型并行审查 PR，可降低幻觉和误报率，按严重性分级报告。
- 📝 **典型工作流程**：先修复关键/高严重性 Bug，跳过性价比低的修复，若 PR 问题过多则直接放弃，并常发现预存 Bug 引发“支线任务”。
- 🧠 **深度理解代码库**：这种慢速编码方式能提升代码库整体健康度，帮助开发者了解架构的失败模式，而非仅关注“快乐路径”。
- 💬 **社区经验分享**：多位开发者验证了类似方法，包括使用不同角色（架构师、测试工程师）进行对抗性审查，以及用于新手上手代码库。
- 🎯 **需要领域知识**：该方法要求开发者具备足够知识来筛选和验证 AI 发现的 Bug，对初级开发者可能仍具挑战性。
- 📉 **非效率导向**：这种方式不追求原始代码行数或速度，而是注重代码质量、可维护性和团队学习，是一种更“超级”的编程方式。

---

### [GitHub - AllThingsSmitty/typescript-tips-everyone-should-know：精选实用TypeScript模式集，提升安全性、可读性、可维护性与开发者体验。](https://github.com/AllThingsSmitty/typescript-tips-everyone-should-know)

**原文标题**: [GitHub - AllThingsSmitty/typescript-tips-everyone-should-know: A curated collection of practical TypeScript patterns that improve safety, readability, maintainability, and developer experience. · GitHub](https://github.com/AllThingsSmitty/typescript-tips-everyone-should-know)

本指南提供了实用的 TypeScript 模式，旨在提升代码的安全性、可读性和可维护性。

- 🛡️ 优先使用 `unknown` 而非 `any`，强制进行类型验证，防止类型泄露。
- 🤖 让类型推断自动工作，减少显式类型注解，避免过度注解带来的维护负担。
- ✅ 使用 `satisfies` 替代 `as`，在验证类型的同时保留类型推断的精确性。
- 🔄 从值中派生类型，使用 `as const` 和 `typeof` 保持运行时值与类型同步。
- 🧩 用可辨识联合建模不可能状态，通过穷举检查（`never`）将未来重构错误转化为编译错误。
- 📌 对配置和常量使用 `as const`，将宽泛类型（如 `string`）缩小为字面量类型。
- 🔍 使用类型谓词连接运行时检查与编译时智能，尤其在 API 和外部输入边界处。
- 🏗️ 通过 `Pick`、`Omit` 等工具类型从现有类型构建新类型，避免重复。
- 🌐 在运行时验证外部数据（如 API 响应），因为 TypeScript 不保证运行时安全。
- 🚫 大多数情况下避免使用 `enum`，改用 `as const` 和字面量联合类型，更易重构和序列化。
- ⚙️ 优先使用可自动推断的泛型，减少手动指定泛型参数。
- 🔧 启用严格编译器选项（如 `strict`、`noUncheckedIndexedAccess`），显著提升代码正确性。
- 🎨 学习模板字面量类型，用于路由、事件名、CSS 工具类等场景。
- ⚠️ 记住“类型安全”不等于“运行时安全”，TypeScript 改善正确性但不替代验证。

---

### [适用于任何规模的时间序列工作负载的 Postgres | Tiger Data](https://www.tigerdata.com/go/trial?utm_source=content-syndication&utm_medium=referral&utm_campaign=javascript-weekly-newsletter)

**原文标题**: [Postgres for time-series workloads at any scale | Tiger Data](https://www.tigerdata.com/go/trial?utm_source=content-syndication&utm_medium=referral&utm_campaign=javascript-weekly-newsletter)

Timescale 的 Tiger Cloud 提供可扩展的 PostgreSQL 时间序列数据库服务，支持大规模数据管理，并强调高性能、高可用性和企业级合规。

- 📊 **超大规模处理能力**：每天处理 3 万亿个指标、3 PB 数据和 1 千万亿个数据点，展示真实世界的大规模能力。
- 💰 **免费试用与低成本入门**：新用户可获 $1,000 信用额度（30 天有效），无需信用卡。
- 🔄 **弹性扩展与成本优化**：通过分离读写操作（最多 10 个节点）和分层 SSD/S3 存储，实现无底容量且经济高效。
- 🚫 **避免闲置付费**：计算和存储解耦，可独立扩展，优化性能与成本，避免过度配置。
- 🛡️ **高可用性与企业级功能**：多可用区集群支持自动故障转移、时间点恢复和跨区域备份；符合 SOC 2、HIPAA、GDPR 标准，具备加密、SSO、RBAC 和审计日志。
- 🔍 **深度可观测性**：提供查询钻取和仪表盘，可集成 CloudWatch、Datadog、Prometheus 等监控工具。
- ⚡ **快速部署与灵活管理**：数分钟内完成数据库配置，支持 SQL、CLI、Terraform、Cursor 或 Claude Code 管理。
- 🔗 **企业级信任与支持**：提供合同化正常运行时间 SLA、区域数据隔离和 24/7 全球专家支持，确保企业响应时间。

---

### [使用 JavaScript 有意阻止渲染](https://www.jayfreestone.com/writing/intentional-render-blocking-javascript/)

**原文标题**: [Intentionally blocking rendering with JavaScript](https://www.jayfreestone.com/writing/intentional-render-blocking-javascript/)

本文探讨了如何通过 JavaScript 有意阻止页面渲染，以解决特定 UI 组件的布局闪烁问题，并介绍了`blocking="render"`属性的用法。

- 🚫 **传统阻塞脚本的局限**：传统内联脚本会阻塞 HTML 解析，但浏览器仍可能渲染已接收的部分内容，无法完全避免组件未样式化的“闪烁”现象。
- 🧩 **自定义元素的时序问题**：若在组件解析前注册自定义元素，构造函数和`connectedCallback`中无法访问子元素；延迟注册虽可行，但无法保证组件不显示默认状态。
- ✨ **`blocking="render"`属性**：该属性可确保脚本加载完成前不渲染任何内容，支持内联、模块脚本及外部脚本，且不阻塞 HTML 解析，优于传统阻塞方式。
- 🎯 **适用场景**：适用于依赖客户端 JavaScript 确定布局的组件（如优先级导航模式），可避免布局偏移和闪烁，但脚本需保持小巧内联，避免网络开销。
- ⚠️ **使用建议**：通常应优先显示内容并渐进增强，仅在 A/B 测试或布局依赖场景下使用渲染阻塞，且脚本应尽量轻量内联。

---

### [为什么 tsgo 占用这么多内存？](https://zackoverflow.dev/writing/why-does-tsgo-use-so-much-memory)

**原文标题**: [Why does tsgo use so much memory?](https://zackoverflow.dev/writing/why-does-tsgo-use-so-much-memory)

### 概述总结

`tsgo` 在多线程处理大型 TypeScript 项目时内存使用量巨大（可达数 GB），主要原因是每个线程独立维护完整的类型检查器状态，导致大量重复数据分配且永不释放。

- 🧠 **多线程架构导致内存膨胀**：每个线程创建独立的 `Checker` 实例，各自维护类型、符号等完整状态，线程间不共享数据以避免同步开销，导致重复内存分配

- 📊 **堆内存分析显示关键数据**：多线程时类型检查器占用约 400MB（单线程仅 50MB），其中 AST 节点占 45%（约 600MB），类型/签名计算占 30%（约 400MB）

- 🔄 **类型重复分配问题**：每个 `Checker` 维护大量类型缓存（如元组、联合类型等），递归泛型类型（如 `BuildTuple<100>`）会产生大量临时类型，在多线程下被重复创建 4 倍

- 🏷️ **符号重复创建**：如 `Array.prototype.at` 符号在多线程下创建数量是单线程的 2 倍以上（34500 vs 14600），每个类型参数实例化都会生成独立符号

- ⚠️ **内存永不释放**：类型分配后永久驻留，类似图灵完备的编译期值系统，缺乏垃圾回收机制

- 💡 **潜在优化方向**：引入类型垃圾回收、持久化共享数据结构、参考 Zig 编译器的 `InternPool` 实现（无锁读取 + 分片写入）

---

### [CSS 与 JavaScript • Josh W. Comeau](https://www.joshwcomeau.com/animation/css-vs-javascript/)

**原文标题**: [CSS vs. JavaScript • Josh W. Comeau](https://www.joshwcomeau.com/animation/css-vs-javascript/)

概述总结  
- 🎯 文章探讨 CSS 与 JavaScript 动画的性能差异，指出传统认知存在偏差，关键区别在于 CSS 动画运行在独立线程，不受主线程阻塞影响。  
- ⚙️ CSS 关键帧动画在独立线程运行，即使主线程繁忙也能保持流畅；而纯 JS 动画（如 requestAnimationFrame）在主线程执行，易受其他任务干扰导致卡顿。  
- 🚀 使用 Web Animations API 的库（如 Motion）能实现与 CSS 类似的独立线程运行，避免主线程问题；而 GSAP 等库仍受主线程限制，且动画可能不同步。  
- 📦 JS 动画库需额外下载和解析（如 Motion 48kB、GSAP 27kB），但通常对用户体验影响不大，除非需要立即执行动画。  
- 🛠️ 建议优先使用原生 CSS 动画，复杂场景选择 Motion 等利用 WAAPI 的库；避免使用仅封装 CSS 功能的 JS 库，因其无实质优势且增加负担。  
- 💡 现代 CSS（如 View Transitions、linear()、Animation Timeline）已能实现多数动画效果，减少对 JS 库的依赖。

---

### [你的递归在欺骗你](https://blog.gaborkoos.com/posts/2026-05-09-Your-Recursion-Is-Lying-to-You/)

**原文标题**: [Your Recursion Is Lying to You](https://blog.gaborkoos.com/posts/2026-05-09-Your-Recursion-Is-Lying-to-You/)

### 概览总结
递归在逻辑上优雅，但在 JavaScript 中因栈空间限制和尾调用优化（TCO）支持不一致，可能导致栈溢出。本文揭示了递归的隐藏风险，并提供了生产环境中的安全替代方案。

- 🧠 **递归的优雅与陷阱**：递归代码清晰自然，但每个调用消耗栈空间，深度过大时会导致`RangeError`（如`sum(100000)`崩溃）。
- 🔄 **尾递归的误解**：尾递归通过累加器避免待处理计算，理论上可复用栈帧，但多数 JS 引擎（如 V8、SpiderMonkey）未稳定实现 TCO，`sumTR(100000)`仍可能溢出。
- ⚡ **斐波那契的额外问题**：朴素递归版`fib(n)`因指数级时间复杂度（O(2ⁿ)）导致页面冻结，与栈溢出是不同问题；尾递归版虽线性时间，仍受 TCO 不确定性影响。
- 🖥️ **运行时现实（2026 年）**：Chrome、Node.js、Firefox、Deno 均不保证 TCO；Safari 和 Bun 因引擎版本差异，行为不稳定，生产环境不可依赖。
- 🛠️ **安全替代方案**：
  - **迭代**：如`sumIter`用循环避免栈增长，最安全。
  - **蹦床模式**：通过循环调用返回函数或结果，保留递归结构但避免栈溢出（如`trampoline(sumTrampoline)`）。
- ✅ **实用清单**：不假设 TCO；测试真实边界；深度增长时用迭代；递归仅用于可控小深度。
- 🎯 **核心结论**：递归本身无害，但需验证运行时行为。尾递归形状不保证栈安全，生产代码应优先选择显式、可移植的迭代设计。

---

### [我们如何通过删除 CMS 将构建时间缩短三分之二 | Sentry 博客](https://blog.sentry.io/cut-build-times-delete-cms/)

**原文标题**: [How we cut build times by two-thirds by deleting our CMS | Sentry Blog](https://blog.sentry.io/cut-build-times-delete-cms/)

## 概述总结

Sentry 团队通过将传统 Headless CMS 替换为 Astro、Markdown 和 AI 自动化，成功将构建时间从 14 分钟缩短至 4 分钟以下，并大幅提升了网站可靠性和开发效率。

- 🏗️ **解决“无头 CMS”痛点**：旧有 Gatsby+CMS 架构存在构建缓慢（日均 22 小时）、插件脆弱（每日 3-5 次故障）、模式受限（需额外购买插件）等问题
- ⚡ **Astro+ 文件系统方案**：迁移至 Astro 框架，采用 Markdown 和 Frontmatter 管理内容，构建时间减少三分之二，每日节省 15.8 小时构建时间
- 🤖 **AI 原生内容管理**：自建 Claude Skills 集成，实现零依赖的内容更新流程（引导填写→生成预览→创建 PR），避免 CMS 的 API 故障和模式限制
- 📋 **迁移过程亮点**：2.5 人团队在 2 个月内完成 2500 页迁移，利用 Claude Code 辅助编码，通过 AI 代理集群完成数据迁移、模板重建和测试
- 🔍 **DOM 检查器 MCP**：自建基于 Puppeteer 的 DOM 检查工具，结合 Playwright 视觉回归测试，精准检测和修复 UI 布局问题
- 🛠️ **Claude 技能优化**：为非技术人员创建命令行技能（/new-branch、/deploy-local-preview），并针对不同页面类型构建内容更新技能，包含图片大小检查和敏感区域保护
- 🔒 **解决速率限制问题**：使用 Vercel Blob 在构建开始时预取表单字段，将营销自动化 API 调用降至接近零，消除又一故障点
- 📈 **显著成果**：构建时间从 14 分钟降至 4 分钟内，Web Vitals 评分从 89 提升至 97，故障构建减少 95%，内容模式无限制

---

### [创建 VS Code 代理钩子以响应文件变化 - 编码者](https://humanwhocodes.com/blog/2026/05/vscode-agent-hooks/)

**原文标题**: [Creating a VS Code agent hook to respond to file changes - Human Who Codes](https://humanwhocodes.com/blog/2026/05/vscode-agent-hooks/)

### 概述摘要
本文介绍如何在 VS Code 中创建 Agent Hook，以在特定文件被编辑时自动触发确定性操作，无需依赖 AI 模型自行判断。

- 🤖 **Agent Hook 是什么**：VS Code 的确定性机制，可在 Agent 循环中监听事件并自动执行命令，无需模型主动调用。
- 📋 **支持的事件类型**：包括 SessionStart、UserPromptSubmit、PreToolUse、PostToolUse、PreCompact、SubagentStart、SubagentStop、Stop 等。
- ⚙️ **配置方式**：在 `.github/hooks` 目录创建 JSON 文件，指定事件类型和要执行的命令（如 bash 或 node 脚本）。
- 🔍 **输入输出机制**：Hook 通过 stdin 接收 JSON 格式的事件详情（含时间戳、工作目录、工具名等），通过 exit code 和 stdout 返回结果。
- 🛠️ **检测文件编辑**：通过检查 `PostToolUse` 事件的 `tool_name` 和 `tool_input.files`，判断是否使用了编辑工具修改目标文件。
- 📁 **示例场景**：当 `wrangler.jsonc` 文件被编辑时，自动运行 `wrangler types` 命令生成 TypeScript 类型定义。
- ✅ **优势总结**：提供确定性自动化，避免依赖 AI 模型记忆，确保工作流一致可靠。

---

### [Plotly JavaScript 图形库](https://plotly.com/javascript/)

**原文标题**: [
     Plotly javascript graphing library in JavaScript
](https://plotly.com/javascript/)

Plotly.js 是一个基于 d3.js 和 stack.gl 的开源 JavaScript 图表库，提供超过 40 种图表类型，包括 3D 图表、统计图和 SVG 地图。它通过声明式 JSON 描述图表，支持高度自定义，并利用 SVG 和 WebGL 实现高性能渲染。该库免费开源，可在 GitHub 上贡献或报告问题。以下为关键功能总结：

- 📊 **丰富图表类型**：支持统计、科学、金融、地图、3D 等 40 多种图表，如散点图、等高线图、烛台图等。
- 🔧 **完全可定制**：通过 JSON 属性控制颜色、网格线、图例等所有图表元素，示例包括自定义颜色刻度和误差条。
- ⚡ **高性能渲染**：使用 SVG 保证兼容性和矢量导出，同时通过 stack.gl 和 WebGL 加速 2D/3D 图表，如 scattergl 比 SVG 快一个数量级。
- 🌍 **跨平台通用**：图表以声明式 JSON 抽象，适用于浏览器及 Python、R、MATLAB 等语言。
- 🎓 **丰富教程资源**：提供基础、统计、科学、金融、地图、3D、子图、动画等各类教程，以及配置选项和事件处理指南。
- 🆓 **免费开源**：代码开源，可在 GitHub 上查看、贡献或报告问题，同时提供 Plotly Studio 用于快速创建交互式数据应用。

---

### [Expo UI 现已稳定：从单一导入实现 SwiftUI 和 Jetpack Compose](https://expo.dev/blog/expo-ui-stable-sdk-56?utm_source=react-status&utm_medium=email&utm_campaign=sdk-56)

**原文标题**: [Expo UI is now stable: SwiftUI and Jetpack Compose from a single import](https://expo.dev/blog/expo-ui-stable-sdk-56?utm_source=react-status&utm_medium=email&utm_campaign=sdk-56)

概述摘要：本文探讨了人工智能在医疗领域的最新应用，强调了其在诊断、治疗和患者护理中的潜力，同时指出了数据隐私和伦理挑战。

- 🩺 人工智能通过分析医学影像（如 X 光和 MRI）提高疾病诊断的准确性和速度。
- 💊 在个性化治疗中，AI 可基于患者基因数据推荐最佳药物方案，提升疗效。
- 🤖 智能机器人辅助手术，减少人为误差，并缩短患者恢复时间。
- 📊 电子健康记录系统利用 AI 预测疾病风险，实现早期干预。
- 🔒 数据隐私问题突出，需严格法规保护患者信息不被滥用。
- ⚖️ 伦理挑战包括算法偏见和决策透明度，需确保公平性和可解释性。

---

### [组件派对](https://component-party.dev/?f=react-vue3)

**原文标题**: [Component Party](https://component-party.dev/?f=react-vue3)

本概述总结了主流 Web 组件框架的对比与演进，涵盖 React、Vue、Angular、Svelte、Solid、Ember、Aurelia 等框架的语法、特性及版本差异。

- 🎯 **最受欢迎框架**：React、Vue、Angular 占据主导地位，社区活跃度高
- ⚔️ **React vs Vue**：React 强调灵活性与 JSX，Vue 注重易用性与模板语法
- 🛡️ **React vs Angular**：React 轻量灵活，Angular 提供完整框架与强类型支持
- 🌟 **Vue vs Angular**：Vue 学习曲线平缓，Angular 适合大型企业级应用
- 🔄 **Ember vs React/Vue**：Ember 强调约定优于配置，React/Vue 更灵活
- 🚀 **流行 vs 新兴框架**：React/Vue 稳定成熟，Svelte/Solid 以编译时优化崛起
- 💡 **React vs Svelte**：React 运行时虚拟 DOM，Svelte 编译时消除虚拟 DOM
- 🔥 **React vs Solid**：Solid 采用细粒度响应式，性能接近原生 JS
- 📦 **Vue vs Svelte**：Vue 提供选项式/组合式 API，Svelte 更简洁无运行时
- ⚡ **Vue vs Solid**：Vue 模板 + 虚拟 DOM，Solid 直接操作 DOM 无虚拟层
- 🏗️ **Angular vs Svelte**：Angular 全功能框架，Svelte 轻量编译输出
- 🧩 **Angular vs Solid**：Angular 依赖注入与模块化，Solid 函数式响应式
- 📜 **版本对比**：Svelte 4→5、Vue 2→3、Angular 经典→复兴版、Aurelia 1→2
- 🔮 **当前与未来**：Ember Octane 对比 Polaris，展示框架演进方向

---

### [tsParticles](https://particles.js.org/)

**原文标题**: [tsParticles](https://particles.js.org/)

快速上手体验
- 🚀 从最小化配置开始，逐步扩展到预设、插件和自定义形状
- ⚡ 强调快速启动与渐进式学习路径
- 🔧 支持灵活扩展：预设功能、插件系统及自定义形状
- 🎯 核心设计理念：低门槛入门，高上限定制

---

### [tsParticles 彩带 | 为您的网站添加 JavaScript 彩带动画](https://ribbons.js.org/)

**原文标题**: [tsParticles Ribbons | JavaScript Ribbon animations for your website](https://ribbons.js.org/)

tsParticles Ribbons 是一个用于在网页中添加丝带特效的插件，支持多种社交分享和脚本集成方式。

- 🔗 支持通过 Facebook、X、LinkedIn、Reddit、Telegram、WhatsApp、Email 和复制链接进行分享
- 📦 在纯 HTML/JS 页面中使用时，需通过 CDN 引入脚本文件：`https://cdn.jsdelivr.net/npm/@tsparticles/ribbons@4.1.2/tsparticles.ribbons.bundle.min.js`
- ⚙️ 该插件基于 tsParticles 库，可通过 `with` 和 `by` 参数进行配置
- 🍪 涉及 Cookie 偏好设置，可能用于管理用户隐私选项

---

### [游乐场预设 | tsParticles](https://particles.js.org/playground/presets)

**原文标题**: [Playground Presets | tsParticles](https://particles.js.org/playground/presets)

本页面提供了多种官方预设的粒子效果演示，包含从简单到复杂的动画场景。

- 🎮 提供多种官方预设演示，如 Ambient、Bubbles、Confetti、Fireworks 等
- 🖱️ 支持交互操作，包括点击添加粒子、拖拽吸收器等
- ⚙️ 每个预设都配有可编辑的 JSON 配置文件
- 🎨 预设覆盖不同视觉风格，从柔和背景到动态爆炸效果
- ▶️ 提供开始、暂停、恢复和销毁等播放控制功能
- 📋 支持复制 JSON 配置和分享链接

---

### [发布 v7.1.0 · harshankur/officeParser · GitHub](https://github.com/harshankur/officeParser/releases/tag/v7.1.0)

**原文标题**: [Release v7.1.0 · harshankur/officeParser · GitHub](https://github.com/harshankur/officeParser/releases/tag/v7.1.0)

officeParser v7.1.0 版本发布，专注于企业级可靠性、内存泄漏预防和精确解析，引入了取消控制、线程安全及健壮的实体解码功能。

- 🛡️ 新增原生取消功能：支持通过 `AbortSignal` 中断文档加载、解析循环、后台浏览器及 OCR 识别任务。
- ⏱️ 整合超时与内存安全：统一 OCR 超时配置，增加生成器超时，失败或取消时强制终止资源防止泄漏。
- 🔧 增强 XLSX 解析与实体解码：修复 XML 实体（如 `&#38;`）解析为原始字符串的 bug，并支持 `inlineStr` 属性。
- 🖥️ 升级可视化面板与合规性：添加超时和取消控制，采用 ESM 原生 `import()` 以符合严格 CSP 策略。
- 📦 快速上手：通过 `npm install officeparser@7.1.0` 安装，并提供 `AbortSignal` 和超时配置示例。
- ❤️ 项目支持：作为自 2019 年的志愿项目，已超 1000 万次下载，寻求赞助以支持核心维护、多运行时支持和企业集成。

---

### [officeParser | 最全能的 Node.js 与浏览器 Office 解析与生成工具](https://officeparser.harshankur.com/#visualizer)

**原文标题**: [officeParser | The Most Versatile Office Parser & Generator for Node.js & Browser](https://officeparser.harshankur.com/#visualizer)

该库是一个支持多格式文档解析与生成的一站式工具，专为 AI 工作流和开发者设计，提供结构化 AST、RAG 分块和高保真转换能力。

- 📦 每周下载量领先，支持 11+ 种格式（DOCX、XLSX、PPTX、PDF、ODT、ODS、ODP、RTF、CSV、MD、HTML）
- 🔄 提供统一 API（OfficeConverter.convert），实现一步式文档转换与智能同步
- 🧩 原生 RAG 分块策略，支持固定大小、结构化和语义分块，保留元数据
- 🌳 输出结构化 AST，可直接调用.to(format) 进行高保真转换
- 📎 高保真支持合并单元格、锚点、书签等复杂文档结构
- ⚡ 极致性能：ODP 解析加速 23 倍，RTF、PDF 和大 Excel 引擎优化
- 🔍 集成 OCR（Tesseract.js），可读取文档内图片文字
- ⚙️ 深度元数据提取，包括文档属性、作者信息和自定义 XML/ODF 属性
- 📑 分块时自动继承父级标题上下文，确保语义完整性
- 📍 每个分块包含物理来源（页码、幻灯片名或工作表索引）
- 📊 智能表格行级拆分，自动重复表头以保持结构清晰
- 🔒 隐私保障：所有解析和渲染在浏览器本地完成，不上传文件
- 🛠️ 提供 AST 可视化工具，支持拖放文件实时预览

---

### [发布 v7.4.0 · krisk/Fuse · GitHub](https://github.com/krisk/Fuse/releases/tag/v7.4.0)

**原文标题**: [Release v7.4.0 · krisk/Fuse · GitHub](https://github.com/krisk/Fuse/releases/tag/v7.4.0)

Fuse.js v7.4.0 稳定版发布，聚合了 7.4.0-beta.1 至 7.4.0-beta.8 的所有更新，包含新功能、错误修复、性能优化和文档改进。

- 🚀 **FuseWorker**：新增通过 Web Workers 实现并行搜索的 FuseWorker 类，支持分片集合、并行搜索并保持结果排序。
- 🔍 **token-search**：新增`tokenMatch: 'all' | 'any'`选项，支持 AND/OR 语义，默认'any'保持现有行为，'all'要求所有查询词匹配记录。
- ✂️ **自定义分词器**：新增可自定义的分词器选项，默认正则支持 CJK、西里尔、希腊、阿拉伯等字符的自动分割。
- 🐛 **错误修复**：修复 matches 中数组路径键报告为点号字符串、Bitap 高亮索引限制、文档索引对齐、搜索缓存失效、倒排索引重编号、Web Workers 全局 refIndex 保留等问题。
- ⚡ **性能优化**：复用 Bitap 搜索中的位数组、用 for 循环替换 forEach、快速路径 Math.pow、预分配记录数组、用 filter 替换 reverse-splice 等。
- 📚 **文档更新**：站点从 VuePress 迁移至 VitePress，新增 React 集成指南、语义搜索对比文章、模糊搜索交互式演示、Web Workers 文档及 Fuse Cloud 等待列表。
- ⚠️ **行为变更**：`FuseResultMatch.key`现在对数组路径键返回点号字符串（原为原始 string[]），需调整代码。

---

### [Fuse.js — 轻量级模糊搜索库 | Fuse.js](https://www.fusejs.io/)

**原文标题**: [Fuse.js — Lightweight Fuzzy-Search Library | Fuse.js](https://www.fusejs.io/)

Fuse.js 是一款轻量级模糊搜索库，零依赖，被多家知名企业采用，支持多种搜索模式，即将推出云端服务。

- 🔍 **模糊搜索** — 基于 Bitap 算法，可容错匹配拼写错误
- 🧩 **分词搜索** — 将多词查询拆分为词条，分别模糊匹配并计算 IDF 排名
- ⚙️ **扩展搜索** — 支持精确、前缀、后缀、反向和包含匹配运算符
- 🧠 **逻辑搜索** — 提供 `$and`/`$or` 表达式，用于结构化查询
- ⚖️ **加权键** — 可提升标题等字段的搜索权重，优于描述字段
- 🌐 **嵌套搜索** — 支持点号、数组符号或自定义 `getFn` 函数
- 🚫 **零依赖** — 可在浏览器、Node.js 和 Deno 中运行
- 📦 **双构建版本** — 完整版约 8.6 kB（gzip），基础版约 6.8 kB（gzip）
- ☁️ **Fuse Cloud** — 即将推出托管搜索 API，无需客户端开销

---

### [GitHub - nickjvandyke/eslint-plugin-react-you-might-not-need-an-effect: 捕获不必要的 React 副作用，实现更简洁、更快速、更安全的代码。](https://github.com/nickjvandyke/eslint-plugin-react-you-might-not-need-an-effect)

**原文标题**: [GitHub - nickjvandyke/eslint-plugin-react-you-might-not-need-an-effect: Catch unnecessary React effects for simpler, faster, safer code. · GitHub](https://github.com/nickjvandyke/eslint-plugin-react-you-might-not-need-an-effect)

这是一个 ESLint 插件，用于检测 React 中不必要的 `useEffect`，帮助开发者编写更简洁、高效和不易出错的代码。

- 📦 **安装简便**：支持 NPM 和 Yarn 安装，配置灵活，兼容 Flat Config 和 Legacy Config。
- ⚙️ **深度分析**：分析状态、属性、引用及其上游来源，考虑副作用运行时机，判断逻辑是否冗余。
- 🔎 **规则全面**：提供 9 条具体规则，如禁止派生状态、链式更新、事件处理、属性变化调整状态等。
- 🧪 **测试详尽**：每条规则都有大量有效和无效示例，确保高信噪比和边缘情况处理。
- 💬 **社区反馈**：鼓励用户提交问题和拉取请求，持续改进插件，覆盖更多真实代码中的误用模式。
- 📖 **学习资源**：链接到 React 官方文档，帮助开发者深入理解何时不需要使用副作用。

---

### [你可能不需要 Effect – React](https://react.dev/learn/you-might-not-need-an-effect)

**原文标题**: [You Might Not Need an Effect – React](https://react.dev/learn/you-might-not-need-an-effect)

### 概述总结
Effect 是 React 中用于与外部系统同步的“逃生舱”，但许多场景下并不需要它。通过移除不必要的 Effect，代码会更清晰、高效且不易出错。

- 📊 **避免数据转换用 Effect**：若数据可从现有 props 或 state 计算得出，应在渲染时直接计算，而非存入 state 或使用 Effect。例如，`fullName`应由`firstName`和`lastName`拼接而成。
- ⚡ **缓存昂贵计算用 useMemo**：对于耗时操作（如过滤长列表），使用`useMemo`替代 Effect，避免无关状态变化时重复计算。
- 🔄 **重置状态用 key 而非 Effect**：当 prop 变化需重置整个组件树状态时，给组件传递不同`key`，React 会自动重新创建 DOM 并清空状态。
- 🎛️ **调整部分状态在渲染时处理**：若仅需调整部分状态（如重置选择项），可在渲染过程中直接更新，避免 Effect 导致的额外渲染。
- 🖱️ **事件逻辑放在事件处理器**：由用户交互触发的代码（如点击按钮发送请求）应放在事件处理器中，而非 Effect。Effect 仅用于因组件显示而执行的逻辑（如分析事件）。
- 🔗 **避免 Effect 链式更新**：多个 Effect 链式调整状态会导致低效和脆弱。应尽量在渲染时计算或在事件处理器中统一更新。
- 📡 **数据获取需清理竞态条件**：在 Effect 中获取数据时，需添加清理函数忽略过期响应（如使用`ignore`标志），避免竞态问题。
- 🏗️ **应用初始化用顶层变量**：仅需运行一次的逻辑（如加载本地数据）应使用模块级变量控制，而非依赖 Effect。
- 🔔 **通知父组件在事件中处理**：子组件状态变化需通知父组件时，应在同一事件处理器中同时更新双方状态，避免 Effect 导致的延迟渲染。
- 📤 **数据流向应自上而下**：子组件不应通过 Effect 向父组件传递数据，而应由父组件获取后通过 props 下发，保持数据流可预测。
- 🔌 **订阅外部存储用 useSyncExternalStore**：订阅浏览器 API 或第三方库数据时，优先使用内置 Hook 而非手动 Effect，减少错误。

---

### [PGlite](https://pglite.dev/)

**原文标题**: [PGlite](https://pglite.dev/)

概述摘要：这是一个轻量级的 Postgres WASM 构建版本，压缩后体积小于 3MB。

- 🚀 极轻量级：完整的 Postgres WASM 构建，体积仅 3MB（Gzip 压缩后）
- 🔧 高效部署：适合在资源受限的环境或浏览器中运行
- 🌐 跨平台兼容：基于 WASM 技术，可在多种环境中无缝集成

---

### [发布 | TinyBase](https://tinybase.org/guides/releases/)

**原文标题**: [Releases | TinyBase](https://tinybase.org/guides/releases/)

TinyBase 的发布历史涵盖了从 v1.1 到 v8.4 的多个重要版本更新，主要包括对 React、Solid、Svelte 等框架的 UI 支持、新的数据持久化方式、同步功能、查询引擎、中间件、以及类型系统增强等。

- 🆕 **v8.4**: 新增 Solid DOM 组件和 Inspector 模块，支持在 Solid 应用中渲染和编辑表格数据。
- 🎯 **v8.3**: 推出 Solid 支持模块`ui-solid`，提供响应式绑定和视图组件；查询支持嵌套结果。
- 🧩 **v8.2**: 新增 Svelte DOM 组件和 Inspector 模块，完善 Svelte 生态支持。
- ⚡ **v8.1**: 引入 Svelte 5 runes 原生响应式绑定，提供`getCell`等函数和双向数据绑定。
- 📦 **v8.0**: 支持对象和数组类型作为 Cell/Value；引入中间件系统，可拦截和转换数据写入。
- 🔧 **v7.3**: 新增 React 状态钩子（如`useCellState`），简化读写操作。
- 🔍 **v7.2**: 支持参数化查询，允许动态更新查询参数而无需重新定义。
- 📐 **v7.1**: 引入 Schematizers，可将 Zod、TypeBox 等库的 Schema 转换为 TinyBase 格式。
- 🚫 **v7.0**: 支持`null`作为有效 Cell/Value 类型，并调整数据库持久化行为。
- 💾 **v6.7**: 支持浏览器 Origin Private File System（OPFS）持久化。
- 🛠️ **v6.6**: 改进 Inspector 工具，支持直接创建、复制、删除表格和行。
- 📱 **v6.5**: 新增 React Native MMKV 持久化模块。
- 🗄️ **v6.4**: 新增 React Native SQLite 持久化模块。
- ☁️ **v6.3**: 新增 Cloudflare Durable Object SQLite 持久化模块。
- 🌐 **v6.2**: 新增`omni`模块（全量导出），暴露 HLC 和哈希函数。
- 🐰 **v6.1**: 新增 Bun SQLite 持久化、子集加载、排序参数对象化等。
- 🏗️ **v6.0**: 更新依赖，仅支持 ESM，兼容 React 19。
- 🔄 **v5.4**: 新增 Durable Object WebSocket 同步和持久化。
- 🐘 **v5.2**: 新增 PostgreSQL 和 PGlite（浏览器端 PostgreSQL）持久化。
- 🧪 **v5.1**: 支持服务端持久化（通过`createWsServer`）。
- 🧬 **v5.0**: 引入 MergeableStore（CRDT）和 Synchronizer 同步框架；重构模块结构。
- 🎨 **v4.8**: 新增 PowerSync SQLite 持久化。
- 🗃️ **v4.7**: 新增 LibSQL（Turso）持久化。
- ⚡ **v4.6**: 新增 ElectricSQL 持久化。
- 📱 **v4.5**: 新增 Expo SQLite next 持久化。
- 👂 **v4.4**: 新增存在性监听器（如`addHasTableListener`）。
- ☁️ **v4.3**: 集成 PartyKit 实现云端协作持久化。
- 🗄️ **v4.2**: 新增 IndexedDB 持久化。
- 📊 **v4.1**: 新增`ui-react-dom`模块（预构建表格组件）和 Inspector。
- 🗃️ **v4.0**: 支持 SQLite、CRDT（Yjs/Automerge）持久化；新增`getContent`等方法。
- 📋 **v3.3**: 支持跨行获取 Cell ID（`getTableCellIds`）。
- 🚦 **v3.2**: 支持事务开始监听器（`addStartTransactionListener`）。
- 📝 **v3.1**: 引入基于 Schema 的类型系统（`with-schemas`）。
- 🔑 **v3.0**: 新增键值存储功能（Values）；升级 React 18。
- 🛠️ **v2.2**: 新增 tools 模块（生成 API 和 Schema）。
- 🔗 **v2.1**: 支持多切片索引（如关键词搜索）。
- 🧠 **v2.0**: 引入查询引擎（TinyQL）、排序和分页功能。
- ⏳ **v1.3**: 支持显式事务开始/结束和完成监听器。
- 🔄 **v1.2**: 支持事务回滚（`doRollback`）。
- ❌ **v1.1**: 支持无效数据监听器（`addInvalidCellListener`）。

---

### [未找到标题](https://www.solidjs.com/)

**原文标题**: [No title found](https://www.solidjs.com/)

概述摘要：本文探讨了人工智能在医疗领域的应用，包括诊断辅助、药物研发和个性化治疗，同时指出了数据隐私和伦理挑战。

- 🩺 人工智能辅助诊断：通过分析医学影像和患者数据，提高疾病检测的准确性和效率。
- 💊 加速药物研发：利用 AI 模拟分子相互作用，缩短新药从研发到上市的时间。
- 🧬 个性化治疗方案：根据患者基因和生活习惯，定制更有效的治疗策略。
- 🔒 数据隐私风险：医疗数据共享可能引发患者隐私泄露问题，需加强安全措施。
- ⚖️ 伦理挑战：AI 决策的透明度和责任归属问题，需制定明确监管框架。

---

### [糖分高涨](https://sugar-high.vercel.app/)

**原文标题**: [Sugar High](https://sugar-high.vercel.app/)

Sugar High 是一个超轻量级语法高亮工具，支持多种编程语言和自定义主题。

- ✨ 轻量级设计：体积小，专注于核心语法高亮功能，适合嵌入各种项目
- 🎨 支持多种语言：内置 JavaScript、TypeScript、Python、Rust、CSS、Java、Go 等多种语言预设
- 🌗 亮暗主题：提供 light.css 和 dark.css 主题，支持 CSS 变量自定义颜色
- 📏 行高亮功能：通过 CSS 选择器或自定义类名 `.sh__line` 实现特定行高亮
- 🔧 灵活集成：支持与 remark.js 等 Markdown 处理器配合使用，提供插件支持
- 📝 预设系统：通过 `sugar-high/presets` 导入不同语言预设，适应非 JavaScript/JSX 源码
- 🎯 代码示例丰富：展示了从简单变量到复杂正则表达式、类型定义、数据结构等多种场景的高亮效果

---

### [版本 v9.3.0 | Mantine](https://mantine.dev/changelog/9-3-0/)

**原文标题**: [Version v9.3.0 | Mantine](https://mantine.dev/changelog/9-3-0/)

概述摘要
- 📅 版本 v9.3.0 于 2026 年 6 月 2 日发布，支持通过 OpenCollective 赞助 Mantine 开发。
- 🔄 Pagination 组件新增 `layout="responsive"` 属性，利用 CSS 容器查询在页面按钮和紧凑标签间自适应切换。
- 📝 Text 和 Blockquote 组件新增 `textWrap` 属性，用于控制文本换行，可平衡行长或防止孤词。
- 🧩 新增 `use-splitter` 钩子，提供可调整大小的分割面板功能，支持拖拽、键盘导航、折叠及最小/最大约束。
- 🧩 新增 Splitter 组件，基于 `use-splitter` 钩子，提供声明式可调整分割面板布局。
- 🔢 CodeHighlight 组件新增 `withLineNumbers` 属性，支持显示行号。
- 📋 OverflowList 组件新增 `collapseFrom` 属性，可控制从开头或结尾折叠溢出项，适用于面包屑模式。
- 📝 Textarea 组件新增 `bottomSection` 属性，允许在输入框底部显示字符计数器等补充信息。
- 📋 Combobox、Select、MultiSelect、Autocomplete 和 TagsInput 新增 `floatingHeight="viewport"` 支持，使下拉菜单填满视口可用空间。
- 🖱️ Menu 子菜单使用安全多边形，允许光标在对角线移动时不意外关闭子菜单。
- 🔍 Menu 新增 `Menu.Search`，提供搜索输入框，可过滤项目而不失焦，支持键盘导航。
- ✅ Menu 新增 `Menu.CheckboxItem`、`Menu.RadioItem` 和 `Menu.RadioGroup`，用于构建选项菜单，并支持 `alignItemsLabels` 属性对齐标签。
- 🖱️ Menu 新增 `Menu.ContextMenu`，支持右键点击时在光标位置打开下拉菜单。
- 🖱️ Popover 新增 `Popover.ContextMenu`，支持右键点击时在光标位置打开下拉菜单，可包含任意内容。
- ⌨️ Menu 支持类型导航，按下可打印字符键可聚焦到以该字符开头的下一个项目。
- 🔍 Highlight 组件新增 `caseInsensitive` 和 `accentInsensitive` 属性，默认启用大小写和重音不敏感匹配。
- 📊 PieChart 和 DonutChart 组件新增 `labelsType="name"`，支持显示段名称作为标签。
- 🖱️ Tooltip、Popover 等组件新增 `arrowPosition="merge"`，使箭头与下拉菜单角落合并，形成直角三角形。
- 🔒 Popover 默认将 `preventPositionChangeWhenVisible` 设为 `true`，防止下拉菜单在打开时因滚动或内容变化而翻转。
- ⏰ DayView 和 WeekView 组件新增 `getCurrentTime` 属性，用于返回当前时间，支持自动更新时区指示器。

---

### [获取失败](https://javascriptweekly.com/link/186001/web)

**原文标题**: [Failed to retrieve](https://javascriptweekly.com/link/186001/web)

无法总结：获取内容失败，状态码 500。

---

### [Clerk CLI](https://clerk.com/cli?utm_source=cooper_press&utm_medium=newsletter&utm_campaign=cli&utm_content=06-02-26&dub_id=O8qysWw45cMD555c)

**原文标题**: [Clerk CLI](https://clerk.com/cli?utm_source=cooper_press&utm_medium=newsletter&utm_campaign=cli&utm_content=06-02-26&dub_id=O8qysWw45cMD555c)

Clerk CLI 让开发者与 AI 代理都能通过命令行快速完成应用的身份验证设置，无需离开终端或手动复制 API 密钥。

- 🔐 **三命令完成身份验证**：通过 `clerk init`、`clerk config`、`clerk deploy` 即可在现有仓库中检测框架、链接应用、管理设置并安全部署到生产环境。
- 🤖 **AI 代理可自主操作**：代理能利用 Clerk CLI 自动处理身份验证、租户上线及生产交接，从提示到部署全程无需人工干预。
- 🛠️ **多环境支持**：支持 npm、bun、pnpm、yarn、Homebrew 和 curl 等多种安装方式，适配不同开发习惯。
- 📦 **项目集成自动化**：`clerk init` 自动检测框架、安装对应包并添加认证文件，简化初始设置流程。
- 🌐 **生产就绪部署**：`clerk deploy` 帮助配置域名、OAuth 提供商和 DNS 记录，确保上线信心。
- ⚡ **专为 AI 时代设计**：CLI 同时面向开发者与 AI 代理，旨在让使用 AI 的开发团队快速且安全地交付产品。

---

### [GitHub - Agent-Field/SWE-AF: 面向生产级 PR 的 AI 代理自主软件工程舰队，在 AgentField 上实现规划、编码、测试与交付。](https://github.com/Agent-Field/SWE-AF)

**原文标题**: [GitHub - Agent-Field/SWE-AF: Autonomous software engineering fleet of AI agents for production-grade PRs on AgentField: plan, code, test, and ship. · GitHub](https://github.com/Agent-Field/SWE-AF)

SWE-AF 是一个基于 AgentField 构建的自主软件工程团队运行时，通过一次 API 调用即可启动完整的工程团队，实现从规划到交付的端到端自动化。

- 🤖 **一次 API 调用，全自动工程团队** — 只需一个请求，即可启动产品经理、架构师、程序员、审查员和测试员组成的完整团队，自动完成复杂软件的开发。
- 🏭 **工厂化架构** — 采用三层嵌套控制循环（内环/中环/外环），根据任务难度自适应调整，而非简单的单智能体重试。
- 📊 **卓越性能基准** — 在基准测试中以 haiku 和 MiniMax 模型均获得 95/100 分，远超 Claude Code Sonnet (73) 和 Codex o3 (62)。
- 🔧 **多模式与多仓库支持** — 支持单仓库和多仓库模式，可协调跨多个代码库的变更，支持 Claude、OpenRouter、OpenAI 和 Google 等多种运行时。
- 🚀 **快速部署选项** — 支持 Railway 一键部署、Docker 容器化部署和本地安装，几分钟内即可启动运行。
- 💰 **成本效益显著** — 使用 MiniMax M2.5 模型完成 95/100 分的任务仅需约 $6，比同类方案节省 70% 成本。
- 🔄 **持续学习与自适应** — 启用 `enable_learning` 后，系统可跨问题共享学习到的约定和失败模式，持续优化后续任务。
- 🛡️ **完整的 CI/CD 集成** — 自动创建 PR 并监控 CI 状态，失败时自动修复并重新推送，确保交付质量。

---

### [Anders Hejlsberg谈TypeScript、C#和Turbo Pascal - YouTube](https://www.youtube.com/watch?v=K-Xv8D8NjTk)

**原文标题**: [TypeScript, C# and Turbo Pascal with Anders Hejlsberg - YouTube](https://www.youtube.com/watch?v=K-Xv8D8NjTk)

本頁面為 YouTube 平台的綜合資訊頁，涵蓋了從版權、政策到創作者支援等核心面向。

- 📰 提供最新消息與公告的新聞中心
- ©️ 說明內容使用與版權相關的規範
- 📞 提供用戶與平台聯繫的聯絡方式
- 🎥 為內容創作者提供相關資源與支援
- 📢 說明廣告刊登的選項與合作方式
- 💻 提供開發者使用的技術文件與工具
- 📜 列出使用服務需遵守的條款與條件
- 🔒 說明用戶資料的處理與保護政策
- 🛡️ 涵蓋平台安全與內容審查的政策
- ⚙️ 解釋 YouTube 平台運作的基本機制
- 🧪 介紹正在測試中的新功能
- 🏢 顯示版權所有為 Google LLC（年份 2026）

---

### [GitHub - getify/You-Dont-Know-JS：关于JS语言的系列书籍（已出版两版）· GitHub](https://github.com/getify/you-dont-know-js)

**原文标题**: [GitHub - getify/You-Dont-Know-JS: A book series (2 published editions) on the JS language. · GitHub](https://github.com/getify/you-dont-know-js)

"你并不懂 JS"（第二版）是一套深入讲解 JavaScript 核心机制的书籍系列，可免费在线阅读，并支持赞助。

- 📚 系列包含多本主题书籍，推荐按《入门》《作用域与闭包》《对象与类》等顺序阅读。
- 🆓 所有书籍可在线免费阅读，同时提供付费购买选项（如 Leanpub、Amazon）。
- 💰 支持通过 GitHub Sponsorship、Patreon、PayPal 等方式进行财务赞助。
- 🚫 该系列已完稿，不再接受外部贡献。
- 🏆 前两本书由 Frontend Masters 独家赞助，该平台提供高质量前端视频培训。
- 📄 内容版权归 Kyle Simpson 所有，采用 CC BY-NC-ND 4.0 许可协议。
- ⭐ 仓库拥有 18.4 万星标、5.8 万关注者、3.35 万分支，资源丰富。

---

### [GitHub - gql-x/Composer：一个可扩展的DSL，用于以更佳开发者体验组合GraphQL字符串](https://github.com/gql-x/Composer)

**原文标题**: [GitHub - gql-x/Composer: An extensible DSL for composing GraphQL strings with nicer DX · GitHub](https://github.com/gql-x/Composer)

`@gql-x/composer` 是一个用于构建 GraphQL 查询字符串的 DSL，旨在提升开发者体验。它通过内联变量声明、动态组合和显式命名来简化查询构建，并支持 TypeScript。

- 📦 **核心特性**：提供 `createComposer()` 工厂函数，返回独立实例，包含 `$v`、`$f`、`$t`、`$m`、`$d` 等辅助工具，用于变量、字段、类型、映射和指令。
- 🔧 **变量管理**：变量类型在使用处内联声明（如 `$v("id", "ID")`），构建器自动提升到操作参数列表并去重，减少手动管理。
- 🔄 **动态组合**：查询单元（参数、选择集等）是普通 JS 值，可条件包含、命名、传递和组合，无需字符串模板或参数列表维护。
- 🏷️ **显式命名**：使用 `selectionSet`、`varArgs`、`litArgs` 等明确名称，替代 GraphQL 的位置约定，提升可读性。
- 📝 **查询构建**：通过 `query()`、`mutation()`、`subscription()` 等方法构建查询，支持 `root`、`operationName`、`directives` 等选项。
- 🌟 **字段与别名**：`$f` 支持字段别名和参数，如 `$f\`myPosts\`\`posts\${...}\``，可配合 `$m` 实现子选择。
- 🏷️ **类型条件选择**：`$f.on("TypeName")` 生成内联片段，用于接口或联合类型的类型窄化选择。
- 🎯 **指令支持**：`$d` 代理生成指令（如 `@skip`、`@nonreactive`），可附加到操作、根字段或选择字段，支持参数。
- 🔄 **两种形式**：辅助函数（如 `varArgs()`）和对象字面量形式可互换，混合使用也受支持。
- 📊 **结果对象**：构建器返回包含 `text`、`opName`、`resName` 和 `kind` 的对象，便于执行和调试。
- 🧩 **可扩展性**：提供扩展点，支持高层 DSL、自定义组合器和渲染行为，附带抽象 DB 层（`@gql-x/composer/db`）。
- 📜 **TypeScript 支持**：内置类型定义，覆盖完整 API，包括自动完成、类型检查和常见错误检测。
- 🧪 **测试与许可**：包含测试套件，使用 `npm test` 运行，采用 MIT 许可证。

---

### [网站有了新手段监视访客：分析其 SSD 活动 - Ars Technica](https://arstechnica.com/security/2026/05/websites-have-a-new-way-to-spy-on-visitors-analyzing-their-ssd-activity/)

**原文标题**: [Websites have a new way to spy on visitors: Analyzing their SSD activity - Ars Technica](https://arstechnica.com/security/2026/05/websites-have-a-new-way-to-spy-on-visitors-analyzing-their-ssd-activity/)

### 概述总结
网站现在可以通过分析固态硬盘（SSD）活动来监视用户，这是一种名为 FROST 的新型追踪技术，利用浏览器中的 JavaScript 测量 SSD 的 I/O 操作时间，从而推断用户打开的其他网站或应用。

- 🕵️ **新型间谍技术**：FROST 技术利用 SSD 的竞争侧信道，通过测量 I/O 操作时间，推断用户设备上的其他活动。
- 💻 **浏览器内执行**：该攻击完全在浏览器中运行，使用 JavaScript 与 OPFS（原始私有文件系统）交互，无需用户额外操作。
- 📊 **深度学习分析**：通过预训练的卷积神经网络（CNN）分析 SSD 延迟数据，分类出用户正在访问的网站或使用的应用。
- ⚠️ **局限性**：需要至少 1GB 的 OPFS 文件，可能被用户察觉；且 OPFS 文件必须存储在目标 SSD 上，无法检测使用独立 SSD 的应用。
- 🛡️ **防御措施**：及时关闭不用的标签页，监控 OPFS 文件创建和大小；浏览器制造商可限制文件最大大小。
- 🔬 **研究现状**：已在 M2 Mac 上完成完整攻击，Linux 上验证了基础原理，未测试 Windows，目前无野外攻击迹象。

---

### [2026 年人工智能现状](https://2026.stateofai.dev/en-US)

**原文标题**: [State of AI 2026](https://2026.stateofai.dev/en-US)

2026 年 Web 开发 AI 调查显示，AI 对开发者工作影响深远，基于 7,258 份回复总结出四大趋势。

- 📈 AI 采用率激增：AI 生成代码比例从 2025 年的 28% 跃升至 2026 年的 54%，频繁使用 AI 的开发者比例同比翻倍。
- 🤖 Claude Code 引领编码代理：Claude Code 在编码代理中获最高正面评价，Claude 成为开发者付费最多的模型。
- 💰 货币化加速：个人 AI 月支出明显增长，多数受访者认为当前 AI 市场存在泡沫。
- ⚠️ 风险因素增加：开发者担忧失业、军事应用、环境影响及 AI 幻觉不准确等痛点。

---

