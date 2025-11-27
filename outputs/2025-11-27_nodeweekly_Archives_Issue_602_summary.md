### [Node周刊第602期：2025年11月25日](https://nodeweekly.com/issues/602)

**原文标题**: [Node Weekly Issue 602: November 25, 2025](https://nodeweekly.com/issues/602)

本期简报主要涵盖Node.js技术动态、安全警告及开发工具更新，重点包括npm供应链攻击风险、Node.js新版本特性以及多种开发工具发布。

- 🚨 Shai Hulud 2.0蠕虫攻击再度爆发，通过受感染的npm包窃取凭证并传播恶意软件
- 🔧 Node.js v20.19.6 LTS发布，更新根证书和OpenSSL，弃用HTTP/2优先级信号
- ☁️ Node.js 24现支持AWS Lambda运行时，支持期至2028年4月
- 🎙️ TypeScript团队透露6.0和7.0版本新特性规划
- 🛠️ Gluegun工具包发布，助力快速构建Node命令行界面应用
- 📦 tshy 3.1工具实现ESM与CommonJS混合模块无缝兼容
- ⚡ Prisma 7.0正式采用无Rust客户端，Mongoose 9.0同步更新
- 🌐 Ecma TC39委员会推进迭代器序列化、异步字典等新提案
- ⚡ Angular v21发布，新增复古游戏主题功能导览
- 📊 State of React年度开发者调查正式启动

---

### [获取失败](https://nodeweekly.com/link/177477/web)

**原文标题**: [Failed to retrieve](https://nodeweekly.com/link/177477/web)

无法总结：获取内容失败，状态码 403。

---

### [Node.js — 原生运行 TypeScript](https://nodejs.org/en/learn/typescript/run-natively)

**原文标题**: [Node.js — Running TypeScript Natively](https://nodejs.org/en/learn/typescript/run-natively)

Node.js 从特定版本开始逐步支持原生运行 TypeScript 代码，无需预先转译处理。

- 🚀 自 v22.18.0 起默认启用类型清除功能，可直接运行仅含可擦除类型语法的 TypeScript 文件
- 🧪 v22.6.0 引入实验性类型标注清除功能，通过 --experimental-strip-types 标志运行 .ts 文件
- 🔄 v22.7.0 新增 --experimental-transform-types 标志，支持转换 enum 和 namespace 等 TypeScript 专属语法
- ⚠️ 当前实验功能存在限制，复杂语法仍需使用实验性标志
- ⚙️ 无需 tsconfig.json 配置，但建议编辑器与 tsc 采用兼容 Node.js 的编译器选项
- 📌 推荐使用 TypeScript 5.7 或更高版本，该功能由社区志愿者维护且不提供担保

---

### [命令行 API | Node.js v25.2.1 文档](https://nodejs.org/api/cli.html#--experimental-config-fileconfig)

**原文标题**: [Command-line API | Node.js v25.2.1 Documentation](https://nodejs.org/api/cli.html#--experimental-config-fileconfig)

Node.js v25.2.1 命令行选项和环境变量文档，详细介绍了运行 Node.js 时的各种配置参数及其功能。

- 📋 **命令行选项概述**：文档列出了 Node.js 支持的所有命令行标志，包括调试、执行脚本和运行时配置选项。
- 🔧 **权限模型**：通过 `--permission` 和相关标志（如 `--allow-fs-read`、`--allow-net`）限制文件系统、网络、子进程等操作的访问权限。
- 🐛 **调试与分析**：提供 `--inspect`、`--cpu-prof`、`--heap-prof` 等工具，支持 V8 检查器、CPU 和堆内存分析。
- ⚡ **实验性功能**：包括 `--experimental-loader`、`--experimental-shadow-realm` 等标志，用于启用尚未稳定的特性。
- 📦 **模块系统**：通过 `--input-type`、`--require`、`--import` 等选项配置 CommonJS 和 ES 模块的加载行为。
- 🧪 **测试运行器**：集成 `--test` 及相关标志（如 `--test-coverage`、`--test-reporter`），支持自动化测试和覆盖率报告。
- 🔒 **安全与加密**：提供 `--enable-fips`、`--tls-cipher-list` 等选项，用于配置加密和 TLS 相关设置。
- 🌐 **网络与协议**：支持 `--dns-result-order`、`--max-http-header-size` 等网络相关配置。
- 📁 **环境变量**：包括 `NODE_OPTIONS`、`NODE_DEBUG`、`NODE_PATH` 等，用于自定义 Node.js 进程行为。
- 🛠️ **V8 引擎选项**：允许传递 V8 特定标志，如 `--max-old-space-size`，以调整 JavaScript 引擎性能。

---

### [我们教会AI编写真实的Postgres代码（并开源）| Tiger Data](https://www.tigerdata.com/blog/we-taught-ai-to-write-real-postgres-code-open-sourced-it)

**原文标题**: [We Taught AI to Write Real Postgres Code (And Open Sourced It) | Tiger Data](https://www.tigerdata.com/blog/we-taught-ai-to-write-real-postgres-code-open-sourced-it)

Timescale公司开源了pg-aiguide项目，旨在提升AI生成PostgreSQL代码的质量，通过提供专业指导技能和版本感知文档检索，帮助开发者获得可直接用于生产环境的高质量SQL代码。

- 🎯 解决AI生成SQL质量不佳问题：现有AI工具生成的PostgreSQL代码存在数据类型混用、索引错误等隐患
- 🛠️ 提供双重核心功能：包含专业指导技能库和版本感知的语义搜索系统
- 📚 技能库包含实战经验：收录外键索引、时间戳处理等35年PostgreSQL最佳实践
- 🔍 智能文档检索：支持PostgreSQL 15-18版本及TimescaleDB等扩展的精准文档查询
- ⚡ 便捷集成方式：通过MCP协议或Claude插件免费接入各类AI编程助手
- 📊 实测效果显著：启用后生成的表结构更规范，索引策略更合理
- 🌱 社区共建计划：邀请开发者贡献扩展文档、专业技能和性能调优经验
- 🆓 完全开源：项目托管在GitHub，欢迎社区参与改进PostgreSQL的AI编程体验

---

### [GitLab发现大规模npm供应链攻击](https://about.gitlab.com/blog/gitlab-discovers-widespread-npm-supply-chain-attack/)

**原文标题**: [GitLab discovers widespread npm supply chain attack](https://about.gitlab.com/blog/gitlab-discovers-widespread-npm-supply-chain-attack/)

平台提供全面的AI驱动开发安全运维解决方案
- 🛡️ 集成开发安全运维全流程
- 🤖 采用人工智能技术赋能
- 🔄 实现持续集成与交付
- 📊 提供全方位安全监控
- 🚀 支持高效开发运维协同

---

### [更新且持续进行的供应链攻击瞄准CrowdStrike...](https://socket.dev/blog/ongoing-supply-chain-attack-targets-crowdstrike-npm-packages)

**原文标题**: [Updated and Ongoing Supply Chain Attack Targets CrowdStrike ...](https://socket.dev/blog/ongoing-supply-chain-attack-targets-crowdstrike-npm-packages)

Socket CEO Feross Aboukhadijeh 与 a16z 合伙人 Joel de la Garza 探讨了氛围编程、AI驱动的软件开发，以及尽管存在风险，但LLM的兴起仍指向更安全与创新的未来。

- 🎧 探讨氛围编程与AI驱动开发的未来趋势  
- ⚠️ 承认大型语言模型带来的安全风险  
- 🛡️ 强调AI技术推动软件安全创新的潜力  
- 🔄 指出技术进步与风险管控需同步发展  
- 🌟 展望人机协作提升开发效率的新模式

---

### [沙一-哈卢德2.0供应链攻击：逾2.5万个代码库暴露 | Wiz博客](https://www.wiz.io/blog/shai-hulud-2-0-ongoing-supply-chain-attack)

**原文标题**: [Sha1-Hulud 2.0 Supply Chain Attack: 25K+ Repos Exposed | Wiz Blog](https://www.wiz.io/blog/shai-hulud-2-0-ongoing-supply-chain-attack)

Wiz研究团队发现新一轮Shai-Hulud供应链攻击，攻击者通过劫持npm维护者账户发布木马化软件包，在安装阶段窃取开发者凭证并创建恶意仓库，已影响超过2.5万个代码仓库。

- 🚨 **攻击规模**：约700个npm包被篡改，波及Zapier、PostHog等知名项目，27%的云环境存在受影响包
- 📈 **扩散速度**：每30分钟新增约1000个恶意仓库，攻击范围持续扩大
- 🔐 **凭证窃取**：已发现775个GitHub令牌、373组AWS凭证、300组GCP凭证及115组Azure凭证泄露
- ⚙️ **攻击手法**：利用preinstall生命周期脚本执行，新增setup_bun.js等载荷文件，支持多平台运行
- 🌐 **数据交叉泄露**：受害者数据被上传至无关用户的公开仓库，形成跨账户扩散
- 🐳 **权限提升**：尝试通过Docker特权容器突破隔离，获取主机root权限
- 🔄 **持久化机制**：植入discussion.yaml后门工作流，可通过仓库讨论功能远程执行命令
- ⏱️ **环境感知**：自动识别CI环境并调整执行策略，在CI中同步执行、非CI环境中后台运行
- 🛡️ **防护建议**：清理npm缓存、回滚依赖版本、全面轮换凭证、审核GitHub仓库、禁用生命周期脚本

---

### [SHA1-Hulud，npm供应链事件 | Snyk](https://snyk.io/blog/sha1-hulud-npm-supply-chain-incident/)

**原文标题**: [SHA1-Hulud, npm Supply Chain Incident  | Snyk](https://snyk.io/blog/sha1-hulud-npm-supply-chain-incident/)

2025年11月24日发现的SHA1-Hulud是继同年9月Shai-Hulud攻击后的第二轮npm供应链蠕虫攻击，已感染超600个主流npm包，通过隐藏预安装脚本将受控机器转为恶意GitHub Actions运行器，窃取云凭证并注入破坏性工作流。

- 🐛 新型供应链蠕虫通过npm包的隐藏预安装脚本自动传播
- ⚠️ 感染超过600个主流npm包（含Zapier/Posthog等）
- 🔄 将受控机器转为恶意GitHub Actions自托管运行器
- 🗂️ 自动注入工作流窃取GitHub/npm密钥与三大云凭证
- 💥 具备容器逃逸、权限提升及用户主目录删除等破坏行为
- 📈 相比初代攻击具有更快的传播速度和自动化程度
- 🔍 Snyk持续监控并通过信任中心更新受影响包列表
- 🛡️ 建议开发者立即检查项目依赖是否在受影响包清单中

---

### [沙虫再袭（v2）- 插槽](https://socket.dev/blog/shai-hulud-strikes-again-v2)

**原文标题**: [Shai Hulud Strikes Again (v2) - Socket](https://socket.dev/blog/shai-hulud-strikes-again-v2)

研究发现朝鲜黑客组织OtterCookie通过npm软件包供应链发起攻击，利用GitHub和Vercel平台部署了197个恶意软件包。

- 🕵️‍♂️ 揭露朝鲜黑客组织OtterCookie的攻击链条
- 📦 发现197个恶意npm软件包
- 🔗 利用GitHub与Vercel平台构建攻击基础设施
- ⚠️ 通过软件供应链进行隐蔽攻击
- 📅 攻击活动持续至2025年11月

---

### [沙虫2.0再度出击：恶意软件供应链攻击波及Zapier与ENS域名](https://www.aikido.dev/blog/shai-hulud-strikes-again-hitting-zapier-ensdomains)

**原文标题**: [Shai Hulud 2.0 Strikes Again: Malware Supply-Chain Attack Hits Zapier & ENS Domains](https://www.aikido.dev/blog/shai-hulud-strikes-again-hitting-zapier-ensdomains)

Shai Hulud恶意软件在npm生态系统发起第二次供应链攻击，波及Zapier、ENS、AsyncAPI、PostHog、Postman等492个主流软件包，累计月下载量达1.32亿次。攻击者利用npm传统令牌撤销前的空窗期，通过自动窃取开发者密钥并自我复制的蠕虫程序，已造成2.63万个GitHub仓库数据泄露。

- 🕵️♂️ 攻击手法：通过setup_bun.js安装Bun环境后执行恶意脚本，使用TruffleHog扫描API密钥并上传至标注"Sha1-Hulud: The Second Coming"的公开GitHub仓库  
- ⚡ 攻击规模：较首次攻击感染包数量提升5倍（100个），新增Home目录文件擦除等破坏性功能  
- 🚨 影响范围：AsyncAPI、PostHog、Postman等开发工具链核心组件，攻击始于11月24日GMT+0时区凌晨  
- 🔧 防御建议：立即轮换GitHub/npm/云凭证、禁用postinstall脚本、启用多因素认证、使用Safe-Chain拦截恶意包  
- 🐛 攻击缺陷：部分恶意包未正确捆绑bun_environment.js主蠕虫代码，一定程度限制了攻击扩散

---

### [HelixGuard — 开源安全研究](https://helixguard.ai/blog/malicious-sha1hulud-2025-11-24)

**原文标题**: [HelixGuard — Open Source Security Research](https://helixguard.ai/blog/malicious-sha1hulud-2025-11-24)

文章概述了人工智能在现代社会中的广泛应用及其带来的机遇与挑战。

- 🤖 人工智能技术正迅速渗透各行各业，提升生产效率
- 💡 机器学习算法通过数据分析为决策提供有力支持
- 🌐 自然语言处理技术改善了人机交互体验
- ⚠️ 数据隐私和算法偏见是需要关注的重要问题
- 🔧 企业需建立完善的AI伦理规范和使用准则
- 📈 合理运用AI将创造新的商业价值和社会效益

---

### [走廊](https://corridor.dev/shai-check/)

**原文标题**: [Corridor](https://corridor.dev/shai-check/)

文章概述了人工智能在现代社会中的广泛应用及其带来的机遇与挑战。

- 🤖 人工智能技术正迅速渗透到医疗、金融、交通等多个领域
- 💡 机器学习算法通过数据分析为决策提供支持，提升行业效率  
- ⚠️ 数据隐私保护与算法偏见是当前亟待解决的核心问题
- 🌍 全球各国正加快制定相关法规以规范人工智能发展
- 🔮 未来需在技术创新与伦理约束间寻求平衡发展路径

---

### [Node.js — Node.js v20.19.6（长期支持版）](https://nodejs.org/en/blog/release/v20.19.6)

**原文标题**: [Node.js — Node.js v20.19.6 (LTS)](https://nodejs.org/en/blog/release/v20.19.6)

Node.js v20.19.6 (LTS) 版本发布，包含安全更新、依赖项升级、文档改进和多项错误修复。

- 🔐 **安全增强** - 更新根证书至 NSS 3.114/3.116 版本
- 📚 **文档优化** - 更新发布验证说明并新增安全响应策略
- ⚠️ **功能弃用** - 标记 HTTP/2 优先级信令为弃用状态
- 🔄 **依赖更新** - 升级 undici 至 6.22.0、uvwasi 至 0.0.23 等核心依赖
- 🐛 **错误修复** - 修复 REPL 大字符串粘贴性能问题及进程异步上下文错误
- 🛠️ **构建改进** - 更新 Windows 构建环境至 windows-2025 运行器
- 📦 **平台支持** - 提供 Windows、macOS、Linux 等多平台安装包和二进制文件
- 🔧 **工具更新** - 升级 Corepack 至 0.34.1 并移除过时构建工具

---

### [RFC 9113：HTTP/2](https://www.rfc-editor.org/rfc/rfc9113.html)

**原文标题**: [RFC 9113: HTTP/2](https://www.rfc-editor.org/rfc/rfc9113.html)

RFC 9113是HTTP/2协议的标准文档，于2022年6月发布，取代了RFC 7540和8740。该协议通过引入多路复用、头部压缩和流优先级等机制，优化了网络资源利用并降低了延迟。

- 🚀 **多路复用**：允许在单一连接上并发处理多个请求和响应，减少延迟并避免队头阻塞。
- 📦 **头部压缩**：使用HPACK算法压缩HTTP头部，减少冗余数据传输，提升效率。
- 🔄 **流控制**：通过WINDOW_UPDATE帧实现基于信用的流量控制，防止接收方过载。
- ⚠️ **错误处理**：定义连接错误和流错误，使用特定错误码如PROTOCOL_ERROR和FLOW_CONTROL_ERROR。
- 🛑 **服务器推送**：服务器可主动向客户端推送资源，但需客户端配置允许且推送内容必须安全可缓存。
- 🔒 **TLS要求**：必须使用TLS 1.2或更高版本，禁用压缩和重协商，并限制密码套件以增强安全性。
- 📏 **帧结构**：协议基于二进制帧，包括HEADERS、DATA、SETTINGS等类型，每个帧有特定格式和语义。
- 🔧 **协议协商**：通过TLS的ALPN扩展或直接连接的前言来确认HTTP/2支持，h2用于TLS，h2c已弃用。

---

### [TypeScript.fm - 面向TypeScript开发者的友好播客 | TypeScript 6/7新特性前瞻 | Daniel Rosenwasser与Jake Bailey对谈 | 第43B期](https://share.transistor.fm/s/ad05eae6)

**原文标题**: [TypeScript.fm - The Friendly Show for TypeScript Developers | What's Coming in TypeScript 6/7 | Daniel Rosenwasser | Jake Bailey | Ep 43B](https://share.transistor.fm/s/ad05eae6)

该内容为播客平台的界面选项和功能列表，提供多种收听和管理播客的方式。

- 🎧 支持通过Apple Podcasts、Spotify等主流平台订阅节目
- 📥 提供预告片、完整剧集及附赠内容的下载选项
- 🔗 具备分享功能，可复制链接或嵌入代码快速传播
- 🕒 支持从指定时间点开始播放，包含完整文字稿
- 🌐 内置章节导航功能，可直接访问节目官网

---

### [@openjsf.org 在蓝天上](https://bsky.app/profile/openjsf.org/post/3m633hsxh4k27)

**原文标题**: [@openjsf.org on Bluesky](https://bsky.app/profile/openjsf.org/post/3m633hsxh4k27)

Bluesky是一个高度交互式网络应用，需要JavaScript支持。Node.js构建团队从树莓派本地部署发展到全自动化发布流程。

- 🌐 交互式网络应用需要JavaScript支持，不支持简单HTML界面
- 🚀 Node.js构建团队实现从20个手动步骤到单命令发布的自动化升级
- 📈 团队发展历程：从个人车库的树莓派集群到完整自动化发布系统
- 👥 核心贡献者：@ulisesgascon.com 和 @rafaelgss.dev
- 🔗 相关资源：bsky.social / atproto.com / github.com/nodejs/build
- ⚙️ 技术基础：OpenJS基金会提供支持（openjsf.org）
- 🗓️ 发布时间：2025年11月20日

---

### [实验：使TypeScript默认不可变](https://evanhahn.com/typescript-immutability-experiment/)

**原文标题**: [Experiment: making TypeScript immutable-by-default](https://evanhahn.com/typescript-immutability-experiment/)

作者尝试在TypeScript中实现默认不可变变量，通过禁用内置库并自定义类型定义，成功使数组和Record类型默认不可变，但未能实现普通对象的默认不可变性。

- 🚫 禁用TypeScript内置库，使用noLib配置移除默认类型定义
- 🧩 创建基础类型定义文件lib.d.ts，包含空接口作为替代
- 🔒 通过readonly属性使数组默认不可变，同时定义MutableArray支持显式可变
- 📝 自定义Record和MutableRecord类型，实现键值对的默认不可变与显式可变
- ❌ 未能找到使普通对象字面量默认不可变的解决方案
- 💡 建议使用lint规则或其他工具补充实现完全默认不可变性

---

### [Node.js错误处理全面指南 - Honeybadger开发者博客](https://www.honeybadger.io/blog/errors-nodejs/)

**原文标题**: [A comprehensive guide to error handling In Node.js - Honeybadger Developer Blog](https://www.honeybadger.io/blog/errors-nodejs/)

本文介绍了Node.js中错误处理的核心概念、错误类型、传递方式及最佳实践，涵盖从基础错误对象到生产环境错误监控的完整流程。

- 🐛 Node.js错误是Error对象的实例，包含内置错误类（如TypeError）和自定义错误类，通过throw抛出后若未被捕获将导致应用崩溃
- 🎯 错误传递的四种模式：同步操作使用异常抛出、异步操作使用错误优先回调、现代异步方案采用Promise拒绝、长时操作采用事件发射器
- 🛠️ 自定义错误类可通过继承Error对象实现，添加特定属性（如cause）并使用instanceof进行类型检查
- ⚡ 错误分为操作错误（外部因素导致）和程序员错误（代码缺陷），前者需设计处理策略，后者需通过测试和TypeScript预防
- 🚨 未捕获异常和未处理的Promise拒绝应通过日志记录后优雅退出进程，避免继续运行导致内存泄漏
- 📊 集中式错误报告工具（如Honeybadger）可配置API密钥自动捕获和通知生产环境中的错误
- ✅ 最佳实践包括：始终使用Error对象、区分错误类型、禁止忽略错误、异步操作使用async/await配合try/catch、实现统一错误处理中间件

---

### [GitHub - infinitered/gluegun：一个用于构建TypeScript驱动的命令行应用程序的优雅工具包。](https://github.com/infinitered/gluegun)

**原文标题**: [GitHub - infinitered/gluegun: A delightful toolkit for building TypeScript-powered command-line apps.](https://github.com/infinitered/gluegun)

Gluegun 是一个用于构建基于 TypeScript 或现代 JavaScript 的命令行界面（CLI）工具包，提供丰富的开发工具和插件支持，目前处于稳定维护阶段。

- 🛠️ 核心功能 - 支持参数解析、文件模板生成、文件内容修改、系统命令执行等多样化 CLI 开发需求
- 🎯 开发优势 - 整合了 ejs、semver、fs-jetpack 等优质第三方库，提供开箱即用的开发体验
- 🚀 快速入门 - 通过 npx gluegun new 命令可快速搭建项目骨架，支持 TypeScript 和 JavaScript
- 🔌 生态扩展 - 支持通过插件机制扩展功能，社区已提供菜单组件和项目模板等资源
- ⭐ 应用实例 - 已被 Ignite CLI、Solidarity、Graph CLI 等多个知名项目采用
- 📋 系统要求 - 需要 Node.js 12.0 及以上版本运行环境
- 🌐 社区支持 - 目前由社区维护，推荐 Rust CLI、oclif 等作为备选方案
- 📄 开源协议 - 采用 MIT 开源许可证，拥有 3.1k GitHub 星标和活跃的开发者社区

---

### [GitHub - isaacs/tshy](https://github.com/isaacs/tshy)

**原文标题**: [GitHub - isaacs/tshy](https://github.com/isaacs/tshy)

tshy是一个用于构建混合（CommonJS/ESM）TypeScript Node包的工具，可简化模块在两种模块系统中的兼容性处理。

- 🛠️ **构建工具**：自动管理package.json的exports字段，使用tsc编译TypeScript代码为ESM和CommonJS两种格式
- 📁 **目录结构**：源代码放在./src目录，构建产物分别输出到./dist/esm和./dist/commonjs
- ⚡ **快速开发**：支持liveDev模式，通过硬链接实现实时编辑和构建
- 🔧 **配置灵活**：支持自定义exports配置、glob模式导出、多方言构建（如browser、deno等）
- 🎯 **方言处理**：支持通过文件后缀（.cts/.mts）和方言特定文件实现不同环境的代码替换
- 📦 **包管理**：自动处理package.json的imports字段，支持本地包导出和自链接功能
- 🚫 **排除控制**：可通过配置排除特定文件不参与构建
- 🔄 **原子构建**：在临时目录构建，成功后才复制到目标目录，确保构建可靠性
- ⚙️ **TypeScript配置**：提供合理的tsconfig默认值，同时支持自定义配置扩展

---

### [转向仅支持ESM](https://antfu.me/posts/move-on-to-esm-only)

**原文标题**: [Move on to ESM-only](https://antfu.me/posts/move-on-to-esm-only)

作者从过去支持双格式包转向现在倡导ESM-only，认为生态系统已成熟，工具链完善，ESM采用率显著提升，且Node.js新特性解决了CJS与ESM互操作问题，建议新包、浏览器包和CLI工具优先采用ESM-only以简化维护和优化性能。

- 🚀 ESM采用率从2021年的7.8%增长至2024年的25.8%，生态明显转向ESM  
- 🛠️ 现代工具如Vite、Vitest、tsx等原生支持ESM，简化开发配置  
- 🔄 Node.js v22支持`require(ESM)`，实现CJS与ESM无缝互操作，避免异步感染  
- ⚠️ 双格式包存在互操作、依赖解析和包体积问题，增加维护复杂度  
- ✅ 新包、浏览器定向包和独立CLI工具应优先采用ESM-only  
- 📊 作者开发Node Modules Inspector工具，帮助分析依赖的ESM采用状态

---

### [获取失败](https://nodeweekly.com/link/177496/web)

**原文标题**: [Failed to retrieve](https://nodeweekly.com/link/177496/web)

无法总结：获取内容失败，状态码 202。

---

### [GitHub - isaacs/node-glob: Node.js 的 glob 功能](https://github.com/isaacs/node-glob)

**原文标题**: [GitHub - isaacs/node-glob: glob functionality for node.js](https://github.com/isaacs/node-glob)

Node.js 的 glob 模块提供了基于 shell 模式的文件匹配功能，支持异步、同步、流式等多种操作方式，并具有高准确性和优秀的性能表现。

- 🌟 提供多种匹配模式：支持异步 glob、同步 globSync、流式 globStream 等多种文件匹配方式
- 📁 丰富的配置选项：支持忽略模式、大小写敏感、最大深度、符号链接跟踪等多项配置
- 🔧 灵活的路径处理：支持绝对路径、相对路径、Windows 路径特殊处理等功能
- ⚡ 高性能设计：采用缓存优化，在保持 Bash 语义准确性的同时提供快速的匹配性能
- 🎯 准确的模式匹配：严格遵循 Bash 的 glob 模式语义，支持通配符、字符类、扩展模式等
- 📊 全面的 API：提供 Glob 类、迭代器、流处理等完整的编程接口
- 🆚 兼容性优秀：在基准测试中表现优异，相比其他 JavaScript glob 实现具有更好的准确性和稳定性
- 🐛 错误处理完善：支持取消信号、提供详细的错误信息和调试支持

---

### [GitHub - sindresorhus/is-online：检测互联网连接状态](https://github.com/sindresorhus/is-online)

**原文标题**: [GitHub - sindresorhus/is-online: Check if the internet connection is up](https://github.com/sindresorhus/is-online)

这是一个用于检测互联网连接状态的JavaScript库，支持Node.js和浏览器环境，提供多种配置选项和诊断功能。

- 🌐 支持Node.js和浏览器环境，弥补了navigator.onLine仅检测本地连接的不足
- ⚡ 提供超时设置、中止信号和备用URL等灵活配置选项
- 🔧 采用多路并行检测机制，包括HTTPS请求、DNS查询和门户测试
- 📊 内置诊断通道，可输出详细的连接失败信息用于调试
- 🔄 支持IPv4/IPv6协议版本选择和代理服务器配置
- 📦 包含CLI工具和关联模块，形成完整的连接检测解决方案
- 🛡️ 采用MIT开源协议，被26.5k+项目使用，社区活跃度高

---

### [GitHub - sindresorhus/open：跨平台打开工具，可打开URL、文件、可执行程序等。](https://github.com/sindresorhus/open)

**原文标题**: [GitHub - sindresorhus/open: Open stuff like URLs, files, executables. Cross-platform.](https://github.com/sindresorhus/open)

这是一个名为"open"的开源跨平台工具库，用于在命令行工具和脚本中打开URL、文件和可执行程序。

- 🌐 跨平台支持，在macOS使用open命令，Windows使用start命令，Linux使用xdg-open
- 📦 通过npm安装，仅支持ESM模块，不再提供CommonJS导出
- 🔧 支持打开特定应用程序并传递参数，可等待应用程序退出
- 🛡️ 使用spawn而非exec，安全性更高
- 🐧 包含最新的xdg-open脚本，支持WSL路径
- 📱 提供预定义的常用应用程序名称，如Chrome、Firefox等
- ⚠️ 不提供安全保证，需要用户自行处理不可信输入

---

### [GitHub - digitalbazaar/jsonld.js：JavaScript 实现的 JSON-LD 处理器与 API](https://github.com/digitalbazaar/jsonld.js)

**原文标题**: [GitHub - digitalbazaar/jsonld.js: A JSON-LD Processor and API implementation in JavaScript](https://github.com/digitalbazaar/jsonld.js)

这是一个用JavaScript实现的JSON-LD处理器和API库，支持JSON-LD规范，用于在Web环境中处理和转换结构化数据。

- 🚀 支持JSON-LD 1.0/1.1规范及处理算法
- 📦 提供Node.js、浏览器、CDN等多种安装方式
- 🔧 具有数据压缩、扩展、扁平化、框架化等核心功能
- 🔄 支持RDF序列化与反序列化（N-Quads格式）
- ⚡ 提供自定义RDF解析器和文档加载器
- 🛡️ 包含安全模式，适用于数字签名等场景
- 📱 兼容React Native（需配合polyfill使用）
- ✅ 包含完整的测试套件和基准测试工具
- 🌐 支持关联数据、语义网等Web数据结构模型

---

### [JSON-LD - 关联数据的JSON格式](https://json-ld.org/)

**原文标题**: [JSON-LD - JSON for Linked Data](https://json-ld.org/)

JSON-LD是一种轻量级的关联数据格式，基于JSON标准，旨在组织和连接网络数据，使其更易于机器读取和跨网站互操作。

- 🌐 关联数据技术通过标准化格式连接分散的网络数据，实现跨站点机器可读
- 🎯 采用JSON兼容语法，示例展示如何通过@context定义语义、@id标识实体及属性关联
- 🛠️ 提供在线调试平台和多语言开发工具（JavaScript/Python/Java等），支持流式处理与测试套件
- 📜 由W3C社区组维护，已成为正式推荐标准，通过GitHub/邮件列表/IRC等多渠道开放协作
- 📚 网站提供视频教程与技术文档，内容采用CC0许可开放共享

---

### [发布 7.0.0 版本 · prisma/prisma · GitHub](https://github.com/prisma/prisma/releases/tag/7.0.0)

**原文标题**: [Release 7.0.0 · prisma/prisma · GitHub](https://github.com/prisma/prisma/releases/tag/7.0.0)

Prisma ORM 7.0.0 稳定版发布，带来多项重大改进，包括默认采用无 Rust 的 Prisma Client 以提升性能和简化部署，生成文件移至项目目录，引入驱动适配器配置，移除过时功能，并新增映射枚举支持。同时优化了 Prisma Accelerate 和 Prisma Postgres 的集成，更新了 Prisma Studio，并提供了企业级支持选项。

- 🚀 默认启用无 Rust Prisma Client，实现约 90% 更小的包体积和最高 3 倍查询速度提升
- 📁 生成客户端和类型文件移至项目目录，需在 schema 中配置 output 路径
- 🔧 引入驱动适配器，需显式安装并配置数据库连接
- 🗑️ 移除 prisma generate 的多个过时标志和隐式种子脚本执行
- ⚙️ 配置迁移至 prisma.config.ts，不再支持 package.json 中的 prisma 字段
- 🗺️ 新增枚举映射支持，可使用 @map 属性自定义运行时值
- 🔄 Prisma Accelerate 改为通过 accelerateUrl 配置，专注于缓存功能
- 🖥️ CLI 集成新版 Prisma Studio，支持远程数据库检查和关系可视化
- 💾 Prisma Postgres 原生支持连接池，提供无服务器驱动和简化连接流程
- 🏢 推出企业支持计划，提供优先问题处理和定制培训服务

---

### [发布9.0.0版本 · Automattic/mongoose · GitHub](https://github.com/Automattic/mongoose/releases/tag/9.0.0)

**原文标题**: [Release 9.0.0 · Automattic/mongoose · GitHub](https://github.com/Automattic/mongoose/releases/tag/9.0.0)

Mongoose 9.0.0版本发布，包含多项重大变更和功能更新

- 🚨 移除回调式pre中间件支持，改用异步模式
- 🔄 升级MongoDB Node驱动至v7版本
- ⚠️ UUID模式类型现在返回bson格式UUID
- 🎯 findOne(null)等查询现在会抛出错误而非返回首个文档
- 📝 默认禁用更新管道，需显式启用updatePipeline选项
- 🔧 虚拟引用函数现在接收子文档而非顶层文档参数
- 📊 TypeScript类型定义更加严格，移除泛型推断
- 🏗️ 将id字段改为TypeScript中的虚拟属性
- ⚡ 异步化更新验证器和保存钩子以改进堆栈追踪
- 🗑️ 移除bson直接依赖，改用mongodb/lib/bson
- 🌐 移除浏览器构建版本，移至@mongoosejs/browser包
- ✨ 新增Schema.create() TypeScript类型推断功能
- 📚 移除示例目录，修复复数化规则

---

### [GitHub - photostructure/exiftool-vendored.js：跨平台Node.js快速访问ExifTool](https://github.com/photostructure/exiftool-vendored.js)

**原文标题**: [GitHub - photostructure/exiftool-vendored.js: Fast, cross-platform Node.js access to ExifTool](https://github.com/photostructure/exiftool-vendored.js)

这是一个用于Node.js的快速跨平台ExifTool封装库，提供高性能的图片元数据读写功能。

- 📦 **高性能封装** - 相比其他Node.js ExifTool模块快一个数量级，已支持1000多个项目
- 🔧 **跨平台兼容** - 支持macOS、Linux和Windows系统
- 📖 **完整类型支持** - 提供TypeScript类型定义，涵盖数千个元数据字段
- 📝 **元数据操作** - 支持读取、写入和删除图片的EXIF、GPS、IPTC等元数据
- 🖼️ **图片提取** - 可从原始文件中提取缩略图、预览图和JPEG图像
- ⏰ **智能时间处理** - 提供时区感知的日期时间处理功能
- 🧹 **资源管理** - 支持自动资源清理，防止进程泄漏
- ⚡ **高并发处理** - 支持多进程并发，处理速度可达每秒500+文件
- 📚 **完善文档** - 提供详细的安装指南、使用示例和API参考
- 🔒 **开源许可** - 采用MIT许可证，包含安全策略

---

### [GitHub - vercel/nft: Node.js 依赖追踪工具](https://github.com/vercel/nft)

**原文标题**: [GitHub - vercel/nft: Node.js dependency tracing utility](https://github.com/vercel/nft)

这是一个用于分析Node.js应用运行时依赖文件的工具，能够精确追踪项目所需的全部文件（包括node_modules）

- 📦 通过静态分析确定应用运行所需的完整文件列表
- 🔍 支持Node.js的exports/imports字段解析和条件导出
- ⚡ 提供多种配置选项（路径映射、缓存机制、并发控制等）
- 📁 可自定义文件解析逻辑和忽略规则
- 🎯 输出包含详细的依赖关系原因分析
- 🔧 内置TypeScript文件解析支持
- 📊 默认启用深度分析确保依赖完整性
- 🚀 类似ncc的tree-shaking效果但无需打包

---

### [GitHub - OP-Engineering/link-preview-js：⛓ 提取网页链接信息：标题、描述、图片、视频等 [通过OpenGraph]，可在移动设备和Node上运行。](https://github.com/OP-Engineering/link-preview-js)

**原文标题**: [GitHub - OP-Engineering/link-preview-js: ⛓ Extract web links information: title, description, images, videos, etc. [via OpenGraph], runs on mobiles and node.](https://github.com/OP-Engineering/link-preview-js)

这是一个用于提取网页链接信息的JavaScript库，通过OpenGraph协议获取标题、描述、图片和视频等元数据，支持移动端和Node.js环境运行。

- 🔗 基于OpenGraph协议提取网页链接的元数据信息
- 📱 支持Node.js和移动端运行时环境
- ⚠️ 受CORS限制，无法直接在浏览器中使用
- 🔧 提供getLinkPreview和getPreviewFromContent两种API调用方式
- 🛡️ 内置SSRF攻击防护和重定向安全处理机制
- 📊 返回包含标题、描述、图片、媒体类型等完整信息的对象
- ⭐ 采用MIT开源协议，拥有848个星标和128个分支
- 🐛 支持自定义请求头、超时设置和响应处理等高级配置选项

---

### [发布 redis@5.10.0 · redis/node-redis · GitHub](https://github.com/redis/node-redis/releases/tag/redis%405.10.0)

**原文标题**: [Release redis@5.10.0 · redis/node-redis · GitHub](https://github.com/redis/node-redis/releases/tag/redis%405.10.0)

Redis Node.js客户端5.10.0版本发布，包含新功能添加、实验性功能扩展及多项问题修复。

- 🚀 新增MSETEX命令支持和XREADGROUP命令的CLAIM属性
- 🔬 实验性支持CAS/CAD命令和混合搜索功能
- 🐞 修复版本发布流程和套接字握手错误问题
- 🛠️ 更新代理配置并标记8.4特性为实验状态
- 👥 感谢5位贡献者共同完成本次版本更新

---

### [GitHub - P4sca1/cron-schedule：适用于Node.js、Deno、Bun及浏览器的零依赖cron解析器与调度器。](https://github.com/P4sca1/cron-schedule)

**原文标题**: [GitHub - P4sca1/cron-schedule: A zero-dependency cron parser and scheduler for Node.js, Deno, Bun and the browser.](https://github.com/P4sca1/cron-schedule)

这是一个零依赖的cron解析器和调度器，支持Node.js、Deno、Bun和浏览器环境，提供灵活的定时任务管理功能。

- ⏰ 支持解析cron表达式并计算下次/上次执行时间
- 🚀 提供两种调度器：基于定时器的精确调度和基于间隔的高性能调度  
- 📦 轻量级且支持tree-shaking，可通过npm、CDN等多种方式安装
- 🌐 兼容多平台：Node.js 18.20+/20.12+、Deno、Bun和浏览器ESM
- 🔧 支持完整cron语法：秒级精度、时间昵称、范围步长等特性
- ⚡ 提供迭代器接口，可灵活获取未来或过去的执行时间序列
- 🛡️ 包含错误处理机制，任务执行异常时仍保持调度稳定性

---

### [发布 v0.19.0 · wasp-lang/wasp · GitHub](https://github.com/wasp-lang/wasp/releases/tag/v0.19.0)

**原文标题**: [Release v0.19.0 · wasp-lang/wasp · GitHub](https://github.com/wasp-lang/wasp/releases/tag/v0.19.0)

Wasp语言发布了v0.19.0版本更新，包含多项功能改进和问题修复

- ⚠️ 重大变更：项目package.json需添加workspaces配置，CORS来源类型改为正则表达式数组
- 🎉 新增功能：采用npm工作区管理代码，支持自定义PostgreSQL镜像和数据库挂载路径
- 🐞 错误修复：解决了类型错误、部署兼容性和路由配置等问题
- 🔧 性能优化：OpenSaaS项目创建速度提升约20倍，开发模式增加引导提示
- 📖 文档更新：完善了Tailwind安装指南和开发工具配置说明
- 🧩 结构调整：将示例项目移至公开目录便于参考

---

### [黄蜂](https://wasp.sh/)

**原文标题**: [Wasp](https://wasp.sh/)

Wasp是一个全栈Web开发框架，通过声明式配置和代码生成技术，帮助开发者快速构建基于React、Node.js和Prisma的应用程序。

- 🚀 通过简单的.wasp配置文件快速搭建全栈应用，支持一键部署
- 🔐 内置完整身份验证系统，支持Google/GitHub/邮箱登录
- 🎯 提供类型安全的RPC层，自动同步客户端与服务端数据模型
- ⚡ 支持实时WebSocket通信、后台任务调度和邮件发送功能
- 🔄 自动缓存失效机制，与Prisma数据模型深度集成
- 📦 开源框架，支持自定义API路由和数据库种子数据
- 🛠️ 保留90%React/Node.js/Prisma开发体验，仅自动化样板代码
- 🌟 提供待办应用、实时投票系统等多个完整示例项目
- 🏗️ 采用编译器架构，根据配置自动生成前端、后端和部署代码

---

### [GitHub - pnpm/pnpm：快速、节省磁盘空间的包管理器](https://github.com/pnpm/pnpm)

**原文标题**: [GitHub - pnpm/pnpm: Fast, disk space efficient package manager](https://github.com/pnpm/pnpm)

pnpm是一个快速且节省磁盘空间的包管理器，具有高效存储和严格依赖管理的特点。

- 🚀 速度比npm和Yarn快2倍，适用于大型项目
- 💾 采用内容寻址存储，相同文件只保存一次，节省磁盘空间
- 📦 严格的依赖管理，仅允许访问package.json中声明的依赖
- 🔒 使用pnpm-lock.yaml确保安装确定性
- 🌍 支持Windows、Linux和macOS多平台
- 🏢 特别适合monorepo项目，被微软等大型团队使用
- 📚 自2016年起经过生产环境充分测试
- ⚡ 通过硬链接或写时复制技术实现快速安装

---

### [未找到标题](https://x.com/robpalmer2/status/1991425006530884070/photo/1)

**原文标题**: [No title found](https://x.com/robpalmer2/status/1991425006530884070/photo/1)

检测到浏览器中JavaScript功能未启用，请启用JavaScript或切换至受支持的浏览器以继续使用x.com平台。相关解决方案可查阅帮助中心获取支持信息。

- 🌐 启用JavaScript或更换浏览器解决访问问题
- 📚 帮助中心提供受支持浏览器列表
- 🔧 隐私扩展插件可能导致异常，建议暂时禁用
- 🔄 遇到错误时可尝试重新加载页面
- ⚖️ 平台服务受服务条款与隐私政策约束

---

### [GitHub - tc39/proposal-iterator-sequencing：一项通过顺序组合现有迭代器来创建新迭代器的TC39提案](https://github.com/tc39/proposal-iterator-sequencing)

**原文标题**: [GitHub - tc39/proposal-iterator-sequencing: a TC39 proposal to create iterators by sequencing existing iterators](https://github.com/tc39/proposal-iterator-sequencing)

该提案旨在为JavaScript引入迭代器顺序连接功能，通过Iterator.concat方法将多个迭代器按顺序合并为单一迭代器，提升代码简洁性和功能性。

- 🎯 提案核心：通过Iterator.concat方法实现多个迭代器的顺序连接
- 🔄 解决场景：替代生成器函数中手动使用yield*拼接迭代器的繁琐操作
- 💡 语法示例：`Iterator.concat(iter1, [值1, 值2], iter2)` 支持混合迭代器和直接值
- 🌐 语言借鉴：参考Python的chain、Rust的chain等多语言类似实现
- 📊 当前状态：已进入TC39标准流程第3阶段
- ⚡ 特殊处理：无限迭代器场景建议使用flatMap搭配恒等函数
- 🛠️ 开发信息：GitHub仓库获得84星标，由3位主要贡献者维护
- 📝 代码构成：项目采用JavaScript(58.4%)和TypeScript(41.6%)混合开发

---

### [GitHub - tc39/proposal-await-dictionary：关于向ECMAScript添加Promise.allKeyed的提案](https://github.com/tc39/proposal-await-dictionary/)

**原文标题**: [GitHub - tc39/proposal-await-dictionary: A proposal to add Promise.allKeyed to ECMAScript](https://github.com/tc39/proposal-await-dictionary/)

该提案旨在为ECMAScript添加Promise.allKeyed方法，用于并行处理包含多个Promise的字典对象，解决现有方案中顺序执行、变量污染和未处理拒绝等问题。

- 🎯 **核心功能**：新增Promise.allKeyed方法，可并行执行字典中的Promise并保持键值对应关系
- ⚡ **性能优化**：避免使用连续await造成的"瀑布式"执行，提升异步操作效率
- 🛡️ **错误处理**：防止未处理的Promise拒绝错误，提供更安全的异步操作
- 🔄 **扩展API**：同时提供Promise.allSettledKeyed方法用于处理所有Promise的完成状态
- 🔑 **键值保留**：保持原始字典的键名结构，避免顺序混淆问题
- 📚 **语法兼容**：支持字符串和Symbol作为键名，遵循JavaScript枚举属性标准
- 🚫 **设计选择**：仅处理自有可枚举属性，不提供深拷贝功能
- 💡 **替代方案**：考虑过Promise.ownProperties、Promise.fromEntries等方案，最终选择allKeyed作为最佳实现

---

### [GitHub - tc39/proposal-joint-iteration：一项TC39提案，旨在同步多个迭代器的推进](https://github.com/tc39/proposal-joint-iteration)

**原文标题**: [GitHub - tc39/proposal-joint-iteration: a TC39 proposal to synchronise the advancement of multiple iterators](https://github.com/tc39/proposal-joint-iteration)

这是一个TC39提案，旨在为JavaScript添加同步多个迭代器的方法，通常称为zip操作，目前处于第2阶段。

- 🎯 **提案目标**：通过Iterator.zip和Iterator.zipKeyed方法实现多个迭代器的同步遍历
- 🔄 **核心功能**：zip方法处理数组迭代器，zipKeyed方法处理对象键值迭代器
- ⚙️ **三种模式**：支持"shortest"(默认)、"longest"和"strict"三种迭代终止模式
- 📦 **填充选项**：在longest模式下可为较短迭代器指定填充值
- 🌍 **语言借鉴**：参考了Python、Haskell、Rust等多种编程语言的类似功能
- 📊 **当前状态**：获得106个星标，由TypeScript(68.5%)和JavaScript(31.5%)实现
- 🔗 **资源链接**：提供在线演示和规范文档供开发者参考

---

### [GitHub - tc39/proposal-iterator-join：JS 迭代器内容连接成字符串的提案](https://github.com/tc39/proposal-iterator-join)

**原文标题**: [GitHub - tc39/proposal-iterator-join: JS proposal for a means to concatenate the contents of an iterator into a string](https://github.com/tc39/proposal-iterator-join)

该提案旨在为JavaScript迭代器添加字符串拼接功能，使其能像数组的join方法一样便捷地处理迭代器元素。

- 🚀 提案状态：已进入TC39流程第2.7阶段，正等待Test262测试
- 🎯 核心功能：为Iterator.prototype添加join方法，实现迭代器元素的字符串拼接
- 💡 解决痛点：避免现有方案（如Array.from或reduce）产生的中间字符串分配或数组转换开销
- 🔗 应用场景：适用于所有可迭代对象（如Set、Map、生成器）的字符串拼接需求
- 📄 技术规范：方法行为与Array.prototype.join保持一致，专门针对迭代器特性优化
- 👥 开发团队：由Kevin Gibbons担任作者和提案 champion
- 🌐 项目信息：MIT开源协议，GitHub仓库包含规范文档和测试脚本

---

### [TC-39 类型数组提案 - Google 幻灯片](https://docs.google.com/presentation/d/1RIhMpf4gY2wX0KZcmCUU6i9l9Ay7WBu0vY4vIsJUwTg/edit?slide=id.g38e87ed9df8_0_0#slide=id.g38e87ed9df8_0_0)

**原文标题**: [TC-39 TypedArray Proposals - Google 幻灯片](https://docs.google.com/presentation/d/1RIhMpf4gY2wX0KZcmCUU6i9l9Ay7WBu0vY4vIsJUwTg/edit?slide=id.g38e87ed9df8_0_0#slide=id.g38e87ed9df8_0_0)

该页面显示浏览器兼容性问题及功能限制提示，并包含TC-39提案相关导航选项。

- 🌐 浏览器JavaScript未启用导致文件无法打开
- ⚠️ 当前浏览器版本已停止支持需升级
- 📑 页面涉及TC-39类型数组提案内容
- 🗂️ 提供幻灯片/文件/编辑等导航功能菜单
- ☁️ 云端硬盘保存功能出现异常
- 👁️ 当前处于只读模式无法编辑

---

### [获取失败](https://nodeweekly.com/link/177518/web)

**原文标题**: [Failed to retrieve](https://nodeweekly.com/link/177518/web)

无法总结：获取内容失败，状态码 403。

---

### [Angular v21 版本发布 • Angular](https://angular.dev/events/v21)

**原文标题**: [Angular v21 Release • Angular](https://angular.dev/events/v21)

Angular v21 以互动游戏形式发布新版本，通过探索游戏世界展示四大核心功能更新。

- 🎮 通过互动游戏世界体验新功能，包含四个可探索地点对应不同技术演示
- 🤖 新增 Angular MCP 服务器工具，提升 AI 工作流和代码生成能力  
- 📝 推出 Signal Forms 基于信号的表单处理方案
- ♿ 发布 Angular Aria 无障碍功能包
- 🏰 收集三个钥匙后解锁吉祥物彩蛋功能
- 🎯 采用现代游戏化方式展示技术特性，包含完整的方向控制和动画系统

---

### [React 2025 现状报告](https://survey.devographics.com/en-US/survey/state-of-react/2025)

**原文标题**: [State of React 2025](https://survey.devographics.com/en-US/survey/state-of-react/2025)

React 2025 年度调查现已开放，旨在收集开发者对 React 生态系统的使用反馈，推动框架未来发展。

- 🐢 React 从“快速迭代”转变为“稳步演进”，通过渐进式创新让社区自主适配新功能  
- 🚀 2025 年将正式推出备受期待的 React Compiler，并成立 React Foundation 管理机构  
- 📊 调查目标：衡量 React API 及生态库的认知度与流行度，所有数据将公开供行业参考  
- ⏱️ 参与耗时约 15-20 分钟，面向所有React使用者（职业/学习/兴趣），含多语言版本支持  
- 🌍 由 Devographics 联合社区志愿者运营，翻译团队覆盖简体中文等超30种语言版本  
- 📅 调查周期：10月25日至11月25日，结果将在结束后及时发布

---

### [从零开始学WebAssembly](https://wasmgroundup.com/)

**原文标题**: [WebAssembly from the Ground Up](https://wasmgroundup.com/)

这是一本通过实践构建WebAssembly解释器来深入理解其原理的教程书籍，采用JavaScript逐步实现编译器，无需编译原理基础即可学习。

- 🎯 通过构建编译器深入理解WebAssembly指令集和模块格式
- 🛠️ 使用JavaScript和Ohm解析工具包实现简单编程语言到Wasm的编译
- 📚 包含15章技术内容、完整源代码及测试案例
- 💻 提供交互式网页版和PDF版本，附带私人Discord社区
- 🆓 采用MIT许可证，代码可自由用于个人项目
- ⏱️ 提供30天退款保障和免费试读章节
- 👨‍💻 适合具备JavaScript基础的程序员，无需编译经验
- ✨ 包含外部函数调用、内存管理和安全模型等核心概念解析

---

### [非 HTML 内容](https://wasmgroundup.com/WebAssembly_from_the_Ground_Up_sample.pdf)

**原文标题**: [Non-HTML content](https://wasmgroundup.com/WebAssembly_from_the_Ground_Up_sample.pdf)

无法总结：非 HTML 内容。

---

### [AWS CodeCommit 的未来 | AWS DevOps 与开发者生产力博客](https://aws.amazon.com/blogs/devops/aws-codecommit-returns-to-general-availability/)

**原文标题**: [The Future of AWS CodeCommit | AWS DevOps & Developer Productivity Blog](https://aws.amazon.com/blogs/devops/aws-codecommit-returns-to-general-availability/)

AWS宣布恢复CodeCommit的全面可用性，基于客户反馈重新评估了该服务对集成化代码仓库的需求。

- 🔄 重新开放新客户注册，现有用户可继续使用或回归服务
- 🎯 保留核心优势：深度IAM集成、VPC端点支持、CloudTrail日志记录
- 🗓️ 2026年Q1将新增Git LFS大文件支持功能
- 🌍 2026年Q3计划扩展至eu-south-2和ca-west-1新区域
- 💰 维持现有定价策略和99.9%运行时间SLA承诺
- 📚 提供迁移协助和入门指南支持用户过渡

---

