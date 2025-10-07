### [Node 周刊第 595 期：2025 年 10 月 7 日](https://nodeweekly.com/issues/595)

**原文标题**: [Node Weekly Issue 595: October 7, 2025](https://nodeweekly.com/issues/595)

本期简报聚焦 Node.js 生态最新动态，涵盖性能优化、安全实践、工具更新及技术实践。

- 📦 Node.js 内置功能逐步替代第三方 npm 包，减少依赖负担
- 🔒 提供 npm 安全最佳实践指南，强化开发安全防护
- 🚀 Node.js 文件处理性能提升 78%，通过缓冲区优化实现高速数据处理
- 🛡️ Deno 运行时展示其安全模型如何防范 npm 生态安全风险
- 🧹 使用 Knip 工具安全移除 monorepo 中 120 个未使用依赖
- 📚 发布 Node.js API 设计视频课程，涵盖 RESTful 设计到生产部署
- ⚡ 多款工具更新：ESLint v10 前瞻、pnpm 10.18 网络监控、Bun 1.3 即将发布
- 🌐 创新工具集：Java 嵌入 Node.js 的 Javet、浏览器 RPC 系统 Cap'n Web、图像比对工具 Odiff
- 📊 技术分享：数组分组新方法、Eleventy 性能优化技巧、Node.js 包发布策略
- 🗓️ 行业动态：React 19.2 发布、多框架月度总结、JSConf 会议及 PostgreSQL 18 特性解析

---

### [15 个替代热门 npm 包的最新 Node.js 功能](https://nodesource.com/blog/nodejs-features-replacing-npm-packages)

**原文标题**: [15 Recent Node.js Features that Replace Popular npm Packages](https://nodesource.com/blog/nodejs-features-replacing-npm-packages)

Node.js 持续将常用功能集成到运行时核心中，取代了多个流行的 npm 包，从而减少依赖、提升安全性和维护性。

- 🌐 **全局 fetch()** - Node.js 18+ 内置 fetch API，替代 node-fetch
- 🔌 **全局 WebSocket 客户端** - Node.js 21+ 提供 WebSocket 类，替代 ws 包客户端功能
- 🧪 **内置测试运行器** - node:test 模块提供基础测试功能，替代 mocha/jest
- 💾 **实验性 SQLite 支持** - node:sqlite 模块正在开发中，未来可能替代 sqlite3 包
- 🎨 **控制台样式** - util.styleText() 提供文本颜色样式，替代 chalk/kleur
- 🧹 **ANSI 代码清理** - util.stripVTControlCharacters() 清除控制字符，替代 strip-ansi
- 📁 **文件模式匹配** - fs.glob() 支持通配符文件搜索，替代 glob 包
- 🗑️ **递归删除** - fs.rm() 支持 recursive 选项，替代 rimraf
- 📂 **递归创建目录** - fs.mkdir() 支持 recursive 选项，替代 mkdirp
- 🔐 **UUID 生成** - crypto.randomUUID() 生成 UUID，替代 uuid 包
- 🔄 **Base64 编码** - 内置 atob/btoa 全局函数，替代 base64-js 包
- 🛣️ **URL 模式匹配** - 实验性 URLPattern API，替代 url-pattern
- ⚙️ **环境文件加载** - --env-file 标志支持加载 .env 文件，替代 dotenv
- 🎯 **事件目标** - 全局 EventTarget 类，替代 event-target-shim
- 🔧 **TypeScript 支持** - 实验性类型剥离功能，简化 TypeScript 运行

---

### [GitHub - lirantal/npm-security-best-practices：npm包管理器安全最佳实践集锦](https://github.com/lirantal/npm-security-best-practices)

**原文标题**: [GitHub - lirantal/npm-security-best-practices: Collection of npm package manager Security Best Practices](https://github.com/lirantal/npm-security-best-practices)

该资源库收集了 npm 包管理器的安全最佳实践，旨在通过具体配置和工具使用来防范供应链攻击，确保依赖项的安全性和确定性。

- 🔒 禁用安装后脚本：通过设置 `ignore-scripts=true` 避免恶意脚本在安装时执行
- ⏳ 安装冷却期：使用 `--before` 标志或配置延迟安装新发布的包，降低安装恶意包风险
- 🛡️ 使用 npq 工具：在安装前对包进行安全审计，检查漏洞、包龄、拼写错误等
- 📜 锁文件防护：用 lockfile-lint 验证锁文件，确保依赖来源可信且使用 HTTPS
- 🔐 确定安装：使用 `npm ci` 而非 `npm install`，严格按锁文件版本安装
- ⚠️ 避免盲目升级：通过交互式工具或安全策略管理依赖更新，防止引入恶意包
- 🗝️ 避免明文密钥：使用密钥管理工具替代.env 文件存储敏感信息
- 📦 开发容器隔离：在容器中开发，限制恶意包对主机系统的访问
- 🔑 启用双因素认证：保护 npm 账户，防止未授权发布
- 📋 发布来源证明：使用 CI/CD 生成可验证的构建来源证明
- 🔄 OIDC 发布：用短期令牌替代长期 npm 令牌，提高发布安全性
- 🌳 减少依赖树：最小化依赖，使用原生 JavaScript 功能降低攻击面

---

### [ESLint v10.0.0 新特性前瞻 - ESLint：可插拔的 JavaScript 代码检查工具](https://eslint.org/blog/2025/10/whats-coming-in-eslint-10.0.0/)

**原文标题**: [What's coming in ESLint v10.0.0 - ESLint - Pluggable JavaScript Linter](https://eslint.org/blog/2025/10/whats-coming-in-eslint-10.0.0/)

ESLint v10.0.0 将于 2025 年 10 月发布，这是重大版本更新，包含多项破坏性变更。开发将分阶段进行：Alpha 版聚焦核心破坏性改动，Beta 版补充剩余功能。主要变更包括停止支持旧版 Node.js、完全移除 eslintrc 配置系统、更新推荐规则配置、优化 AST 节点范围计算等。最终版本计划于 2026 年 1 月发布。

- 🚨 停止支持 Node.js v20.19.0 以下版本，仅兼容 v20.19.0+/v22.13.0+/v24+
- 🗑️ 彻底移除 eslintrc 配置系统及相关命令行参数
- ⚙️ 更新 eslint:recommended 规则配置以提升代码质量
- 📜 Program AST 节点范围调整为覆盖完整源码（含注释）
- 🔧 移除规则上下文对象中已弃用的方法（如 getFilename()）
- 🗂️ 配置文件查找算法改为从被检测文件目录开始
- 🚫 删除 parserOptions.globalReturn 配置项
- 🧪 RuleTester 测试用例不再支持 type 属性
- 🔍 Beta 版将启用 JSX 引用追踪功能
- 🧹 移除 SourceCode 中多个已弃用方法（如 getTokenOrCommentBefore()）
- 🗓️ Alpha 版预计 2025 年 11 月发布，正式版目标 2026 年 1 月发布

---

### [pnpm 10.18 | pnpm](https://pnpm.io/blog/releases/10.18)

**原文标题**: [pnpm 10.18 | pnpm](https://pnpm.io/blog/releases/10.18)

pnpm 10.18 版本更新了网络性能监控功能，并修复了多项已知问题，提升了工具的稳定性和用户体验。

- 🚨 新增网络请求超时与低速警告功能，覆盖元数据获取和压缩包下载
- ⚙️ 添加可配置阈值参数 fetchWarnTimeoutMs 和 fetchMinSpeedKiBps
- 🔄 文件系统操作遇到 EAGAIN 错误时自动重试（PR #9959）
- 📅 outdated 命令现支持 minimumReleaseAge 配置（PR #10030）
- 🧹 修复 cleanupUnusedCatalogs 配置在移除依赖包时的应用问题
- 🐛 解决 scriptShell 设为 false 时报错问题（PR #8748）
- ✨ 优化 pnpm dlx 在设置 minimumReleaseAge 时的执行稳定性（PR #10037）

---

### [Bun — 一款快速的全能 JavaScript 运行时](https://bun.sh/)

**原文标题**: [Bun — A fast all-in-one JavaScript runtime](https://bun.sh/)

Bun v1.2.23 是一个高速的 JavaScript 全功能工具包，集开发、测试、运行和打包功能于一体，兼容 Node.js 生态系统。

- 🚀 Bun 在 HTTP 请求性能测试中表现卓越，每秒处理 59,026 次请求，远超 Deno 和 Node.js
- ⚡ WebSocket 服务器性能突出，每秒可发送 2,536,227 条消息，性能优势明显
- 📊 数据库查询性能优异，每秒处理 28,571 次查询，领先其他运行时
- 🔧 提供一体化开发体验，包含打包工具、测试运行器和包管理器
- 🌐 支持多种安装方式，支持 Linux、macOS 和 Windows 系统
- 📦 致力于实现 100% Node.js 兼容性，方便项目迁移
- 🏆 已被 Express、Postgres 等知名项目采用

---

### [Node.js 性能优化：通过缓冲区处理使 14GB 文件提速 78%](https://pmbanugo.me/blog/nodejs-1brc)

**原文标题**: [Node.js Performance: Processing 14GB Files 78% Faster with Buffer Optimization](https://pmbanugo.me/blog/nodejs-1brc)

通过优化 Node.js 处理 14GB 大文件的方法，将处理时间从 5 分 49 秒缩短至 1 分 14 秒，性能提升 78%。关键在于避免字符串转换、使用整数运算和延迟解码等技巧。

- 🔍 初始方案使用逐行读取和字符串分割，处理 10 亿行数据耗时 5 分 49 秒
- ⚡ 改用字节级解析和整数温度存储，避免 UTF-16 转换，性能提升 50%
- 🧠 采用哈希优先策略，使用 DJB2 哈希和碰撞链表延迟字符串解码，再获 2.25 倍加速
- 📊 性能分析显示 87% 时间消耗在数据处理函数，证明已优化至 CPU 瓶颈
- ⚖️ 对比运行时：Bun(1:05)、Node.js(1:14)、Deno(1:21)，算法优化比运行时选择更重要
- 🚀 进一步优化需使用 Worker 线程实现多核并行处理
- 💡 核心经验：性能优化是侦探工作，需逐步验证理论并消除隐藏开销

---

### [Deno 如何防范 npm 漏洞利用 | Deno](https://deno.com/blog/deno-protects-npm-exploits)

**原文标题**: [How Deno protects against npm exploits | Deno](https://deno.com/blog/deno-protects-npm-exploits)

Deno 通过默认沙箱权限机制、显式授权模式和透明审计功能，为 JavaScript/TypeScript 应用提供比 Node.js 更安全的依赖管理方案。

- 🛡️ **默认安全模型** - Deno 默认在无系统权限的沙箱中运行代码，需显式授权才能访问文件系统、网络或环境变量
- 🚫 **安装脚本控制** - 不会自动执行 postinstall 等安装脚本，需通过`--allow-scripts`标志按需授权特定包
- 🔍 **权限粒度控制** - 支持精细权限设置，如仅允许读取特定文件或访问指定网络端点
- 📝 **透明权限审计** - 通过环境变量可记录所有权限使用日志，便于监控代码行为
- 📚 **标准库支持** - 提供 40+ 官方标准库包，减少对第三方依赖的依赖，降低供应链攻击风险
- 🔐 **现代化包注册表** - JSR 提供 TypeScript 原生支持、发布授权验证和软件来源证明等安全功能
- 🌐 **实际应用场景** - 被 LangChain、LMStudio 等平台用于安全执行 LLM 生成的代码

---

### [Deno，下一代 JavaScript 运行时](https://deno.com/)

**原文标题**: [Deno, the next-generation JavaScript runtime](https://deno.com/)

Deno 是一个现代化的开源 JavaScript/TypeScript 运行时环境，专注于安全性、工具链完整性和 Web 标准兼容性。

- 🚀 原生支持 TypeScript/JSX，无需配置即可直接运行
- 🔒 默认安全机制，需显式授权才能访问文件/网络/环境变量
- 🛠️ 内置完整工具链（测试运行器、代码检查、格式化、编译）
- 📦 无缝 npm 兼容，支持直接导入 npm 包和 package.json
- 🌐 基于 Web 标准 API，实现浏览器与后端代码复用
- ⚡ 高性能网络支持（HTTP/2、WebSocket、自动压缩）
- ☁️ 专为云原生设计，提供 Deno Deploy 等部署方案
- 📊 活跃生态：GitHub 10 万 + 星标，40 万 + 活跃用户，200 万 + 社区模块
- 🏝️ 配套 Fresh 框架支持岛屿架构，实现最小化 JavaScript 加载

---

### [获取失败](https://nodeweekly.com/link/175251/web)

**原文标题**: [Failed to retrieve](https://nodeweekly.com/link/175251/web)

无法总结：获取内容失败，状态码 403。

---

### [清理 NX Monorepo 中的冗余依赖：安全移除 120 个未使用组件的实践](https://johnjames.blog/posts/cleaning-house-in-nx-monorepo-how-i-removed-120-unused-deps-safely)

**原文标题**: [cleaning house in nx monorepo, how i removed 120 unused deps safely](https://johnjames.blog/posts/cleaning-house-in-nx-monorepo-how-i-removed-120-unused-deps-safely)

概述：作者使用 Knip 工具安全地清理了 Nx 单体仓库中 120 个未使用的依赖包，使安装时间减少约 1 分钟，并降低了安全警报干扰。

- 🔍 使用 Knip 替代已过时的 depcheck 工具进行依赖扫描，该工具支持现代项目结构并能识别入口点
- 🧪 采用"删除 - 构建 - 测试 - 验证"的循环流程：移除可疑依赖后执行完整构建、测试并启动应用验证
- 📝 处理了约 40% 误报情况，通过忽略列表记录被误判的依赖（如配置文件中字符串引用、CLI 工具等）
- ⚙️ 配置了针对单体仓库的 Knip 设置，包含工作区忽略规则和特定依赖排除项
- 🚀 清理后依赖数量从 510 个降至 390 个，Yarn 安装时间缩短约 1 分钟
- 🔧 建议将 Knip 集成至 CI 流程，先作为报告工具运行，后续可设置为阻断新无用依赖
- 📁 工具还能检测未使用的文件、枚举和类型定义，便于后续死代码清理

---

### [精简你的 JavaScript 与 TypeScript 项目 | Knip](https://knip.dev/)

**原文标题**: [Declutter your JavaScript & TypeScript projects | Knip](https://knip.dev/)

Knip 是一款用于清理 JavaScript 和 TypeScript 项目中未使用依赖、导出和文件的自动化工具，通过精准的代码分析帮助优化项目结构。

- 🧹 自动检测并清理未使用的依赖项、导出和文件
- 🎯 支持 100+ 框架插件（包括 Next.js、Vite、Jest 等）
- ⚡ 被 Shopify 等知名团队用于删除数十万行冗余代码
- 🔧 提供在线演练场和故障排除指南
- 🌟 开发者社区评价其为"近 20 年最佳代码维护工具"

---

### [DevSecCon：保障向 AI 原生转型的安全 | 免费注册 | 2025 年 10 月 | Snyk](https://snyk.io/events/devseccon/?utm_campaign=dm_pp-cooperpress_251007_evt_251022_devseccon_flagship_2025&utm_medium=em-pa&utm_source=cooperpress-node-weekly&utm_content=evt_251022_devseccon_flagship_2025)

**原文标题**: [DevSecCon: Securing the Shift to AI Native | Register for Free | Oct '25 | Snyk](https://snyk.io/events/devseccon/?utm_campaign=dm_pp-cooperpress_251007_evt_251022_devseccon_flagship_2025&utm_medium=em-pa&utm_source=cooperpress-node-weekly&utm_content=evt_251022_devseccon_flagship_2025)

首届全球 AI 安全社区峰会将于 2025 年 10 月 22 日在伦敦举行，聚焦 AI 原生时代的安全转型。本次活动包含主题演讲、实践演示、开发者挑战赛等环节，汇聚 OpenAI、Snyk 等行业专家，探讨 AI 代理安全、MCP 协议防护、红队测试等前沿议题。

- 🗓️ 活动时间：2025 年 10 月 22 日 | 地点：伦敦&线上
- 🎤 核心议程：主论坛演讲、AI 安全研究、创新演示、开发者挑战赛
- 🔐 重点议题：AI 代理身份管理、MCP 服务器安全、红队测试框架、零信任架构
- 👥 明星讲者：OpenAI 前市场负责人 Zack Kass、SnykCEO Peter McKay 等 20+ 专家
- 🛠️ 特色环节：实时音乐派对、动手实验室、多租户 MCP 服务器构建实践
- 🏆 新增亮点：首届 AI 安全开发者挑战赛（具体内容保密）
- 💡 核心价值：获取 AI 原生开发安全实践方案，构建可信 AI 系统防护体系
- 🎯 参会对象：AI 开发者、安全工程师、企业技术决策者
- 🌐 社区资源：可观看 2024 年活动回放，持续获取 AI 安全前沿动态

---

### [DevSecCon：保障向 AI 原生转型的安全 | 免费注册 | 2025 年 10 月 | Snyk](https://snyk.io/events/devseccon/?utm_campaign=dm_pp-cooperpress_251007_evt_251022_devseccon_flagship_2025&utm_medium=em-pa&utm_source=cooperpress-node-weekly&utm_content=evt_251022_devseccon_flagship_2025)

**原文标题**: [DevSecCon: Securing the Shift to AI Native | Register for Free | Oct '25 | Snyk](https://snyk.io/events/devseccon/?utm_campaign=dm_pp-cooperpress_251007_evt_251022_devseccon_flagship_2025&utm_medium=em-pa&utm_source=cooperpress-node-weekly&utm_content=evt_251022_devseccon_flagship_2025)

首届全球 AI 安全社区峰会 DevSecCon25 将于 2025 年 10 月 22 日在伦敦举办，聚焦 AI 原生时代的安全转型。本次活动包含主题演讲、实践演示、安全研究等多元环节，汇聚 OpenAI、Snyk 等行业领袖，探讨 AI 代理安全、MCP 协议防护、红队测试等前沿议题。

- 🎯 **核心主题**：构建 AI 原生应用的安全防线
- 🗓️ **时间地点**：2025 年 10 月 22 日·伦敦线下 + 线上虚拟参会
- 🎤 **明星阵容**：OpenAI 前市场负责人 Zack Kass、Snyk CEO Peter McKay 等 20+ 行业专家
- 🔧 **实践专场**：AI 演示/安全研究/Snyk 创新三大技术轨道
- 🛡️ **安全焦点**：MCP 服务器防护、非人类身份管理、红队测试框架
- ⚡ **技术前沿**：语音编程工作流、容器化安全管道、多租户 MCP 架构
- 🏆 **特别环节**：AI 安全开发者挑战赛、现场音乐派对、开发狂欢乐园
- 💡 **核心洞察**：从代码中心到规范中心的开发范式转变
- 🌐 **社会视角**：探讨技术可行性与社会接受度的关键阈值
- 🆓 **参与方式**：免费注册，支持线上线下混合参与

---

### [获取失败](https://nodeweekly.com/link/175255/web)

**原文标题**: [Failed to retrieve](https://nodeweekly.com/link/175255/web)

无法总结：获取内容失败，状态码 429。

---

### [如何在 JavaScript 中不使用 reduce() 对数组进行分组 - Matt Smith](https://allthingssmitty.com/2025/10/06/grouping-arrays-in-modern-javascript-object-groupby-and-map-groupby/)

**原文标题**: [
    How to group arrays in JavaScript without reduce() - Matt Smith
  ](https://allthingssmitty.com/2025/10/06/grouping-arrays-in-modern-javascript-object-groupby-and-map-groupby/)

JavaScript ES2024 新增了 Object.groupBy() 和 Map.groupBy() 原生数组分组方法，无需再依赖 reduce() 手动实现分组逻辑。

- 🆕 ES2024 引入 Object.groupBy() 和 Map.groupBy() 原生分组方法
- 🔑 Object.groupBy() 返回普通对象，键为字符串，适合 JSON 序列化
- 🗺️ Map.groupBy() 返回 Map 对象，支持非字符串键并保持插入顺序
- ✂️ 替代传统 reduce() 分组写法，代码更简洁易读
- 📊 适用场景：按状态分组任务、按价格区间分组商品、按级别分组日志
- ⚠️ 注意：Object.groupBy() 会强制转换键为字符串，Map.groupBy() 不可 JSON 序列化
- 🌐 所有现代浏览器和 Node.js 21+ 均已支持，提供降级 polyfill 方案

---

### [11ty 趣味与性能优化技巧 - 偶有记录](https://infrequently.org/2025/10/11ty-hacks-for-fun-and-performance/)

**原文标题**: [11ty Hacks for Fun and Performance - Infrequently Noted](https://infrequently.org/2025/10/11ty-hacks-for-fun-and-performance/)

本文介绍了在 11ty 博客中提升页面性能的多种技术方案，包括资源按需加载、滚动触发代码加载、CSS 选择器优化等实践。

- 🧩 通过短代码和 Bundle 插件实现页面资源按需加载，避免全局引入未使用的 JS/CSS
- 🔄 利用 IntersectionObserver 和 MutationObserver 实现滚动触发的延迟代码加载
- ⚡ 优化语法高亮插件的 CSS 属性选择器，将[class*="language-"]改为[highlighted]提升性能
- 🖼️ 采用纯 CSS 低质量图片预览方案替代 base64 编码，减少 HTML 体积并加速渲染
- 📚 通过 Nunjucks 模板的 include 功能统一管理全局缩写词 (abbr) 定义
- ⏱️ Bundle 插件会使构建时间增加约 2 秒，适用于中小型站点
- 🐛 通过 fork 修复了 Bundle 插件在分页场景下的兼容性问题
- 📊 性能优化后页面加载瓶颈主要集中在网络连接阶段

---

### [Eleventy 是一款更简洁的静态网站生成器](https://www.11ty.dev/)

**原文标题**: [Eleventy is a simpler static site generator](https://www.11ty.dev/)

Eleventy 是一款简洁高效的静态网站生成器，支持多种模板语言，无需客户端 JavaScript 即可快速构建高性能网站。

- 🚀 构建速度极快，处理 4000 个 Markdown 文件仅需 1.93 秒
- 🛠️ 支持 11 种模板语言（HTML/Markdown/WebC/JavaScript 等）
- 🌐 被 NASA、Google、微软等知名机构采用
- 📦 零配置启动，支持渐进式采用现有项目结构
- 🔒 无遥测数据收集，注重用户隐私保护
- ⚡ 默认不注入客户端 JavaScript，生成预渲染模板
- 🎯 灵活控制输出结构，支持自定义目录布局
- 📈 已发布 216 个稳定版本，累计下载超 1400 万次
- 👥 拥有活跃社区，获众多开发者好评推荐
- 🔄 提供本地开发服务器和实时预览功能

---

### [Javet 5.0.0 文档](https://www.caoccao.com/Javet/)

**原文标题**: [Javet 5.0.0 documentation](https://www.caoccao.com/Javet/)

Javet 是一个将 Node.js 和 V8 引擎嵌入 Java 的开源项目，支持多平台架构与 JavaScript/Java 互操作，提供丰富的开发工具和 Spring 集成能力。

- 🚀 支持 Node.js v24.8.0 和 V8 v14.1.146.11，可在 Java 中动态切换两种运行模式
- 🌍 兼容多平台（Linux/MacOS/Windows）和 CPU 架构（x86_64/arm64），Android 仅支持 arm/arm64
- 🔧 提供 V8 API 暴露、JavaScript/Java 互操作、原生 BigInt/Date 支持等核心功能
- 🛠️ 集成 Chrome DevTools 实时调试、AST 分析、TypeScript 转译及字节码增强工具
- 📦 支持 Maven/Gradle 依赖管理，需同时引入核心库与对应平台模块
- 💡 包含引擎池、交互式 Shell 等进阶特性，适用于服务端渲染等场景
- 📄 采用 Apache 2.0 许可证，提供完整文档和性能对比报告

---

### [Javet 5.0.0 文档](https://www.caoccao.com/Javet/#major-features)

**原文标题**: [Javet 5.0.0 documentation](https://www.caoccao.com/Javet/#major-features)

Javet 是一个将 Node.js 和 V8 引擎嵌入 Java 的开源项目，支持多平台架构与 JavaScript/Java 互操作，提供丰富的开发工具和集成方案。

- 🚀 支持 Node.js v24.8.0 和 V8 v14.1.146.11，可在 Java 中动态切换运行模式
- 🌍 兼容多平台（Linux/MacOS/Windows）与 CPU 架构（x86_64/arm64），Android 仅支持 arm 架构
- 🔧 提供 V8 API 暴露、JavaScript/Java 互操作、原生 BigInt 和 Date 支持
- 🛠️ 集成 Spring 框架、Chrome DevTools 实时调试、AST 分析与代码转译功能
- 📦 支持 Maven/Gradle 依赖管理，需按平台选择对应模块安装
- 💡 包含引擎池、字节码增强、交互式命令行等进阶特性
- ❤️ 开发者呼吁通过捐赠或关注支持项目持续维护

---

### [GitHub - caoccao/Javet: Javet 即 Java + V8（JAVa + V + EighT），是在 Java 中嵌入 Node.js 和 V8 的绝佳方式。](https://github.com/caoccao/Javet)

**原文标题**: [GitHub - caoccao/Javet: Javet is Java + V8 (JAVa + V + EighT). It is an awesome way of embedding Node.js and V8 in Java.](https://github.com/caoccao/Javet)

Javet 是一个将 Node.js 和 V8 引擎嵌入 Java 的开源项目，支持多平台运行和 JavaScript 与 Java 的高效互操作。

- 🚀 项目名称 Javet 代表 Java + V8，提供在 Java 中嵌入 Node.js 和 V8 引擎的能力
- 🌍 支持多平台包括 Linux、macOS、Windows 和 Android，兼容 x86、x86_64、arm 和 arm64 架构
- 🔄 动态切换 Node.js 和 V8 模式，支持 JavaScript 和 Java 互操作
- 🛠️ 提供丰富的功能包括 Javet 引擎池、Spring 集成、Chrome DevTools 实时调试
- 📚 支持 AST 分析、JS/TS/JSX/TSX 转换和字节码增强
- 📦 通过 Maven 和 Gradle 提供依赖管理，当前版本为 5.0.0
- ⭐ 项目获得 890 个星标，94 个分支，采用 Apache 2.0 开源协议

---

### [Cap'n Web：面向浏览器与网页服务器的新型 RPC 系统](https://blog.cloudflare.com/capnweb-javascript-rpc-library/)

**原文标题**: [Cap'n Web: a new RPC system for browsers and web servers](https://blog.cloudflare.com/capnweb-javascript-rpc-library/)

Cap'n Web 是一款基于 TypeScript 的 RPC 系统，专为浏览器和 Web 服务器设计，采用无模式架构和 JSON 序列化，支持双向调用、对象引用传递和 Promise 流水线操作，适用于实时交互应用和微服务场景。

- 🌐 **纯 TypeScript 实现**：专为 Web 生态系统设计的轻量级 RPC 协议，压缩后小于 10kB  
- 🚫 **无模式架构**：无需定义接口模板，支持类似原生 JavaScript 的直观开发体验  
- 🔄 **双向调用与对象传递**：支持客户端与服务器间相互调用，可传递函数和对象引用  
- ⚡ **Promise 流水线**：允许链式调用在单次网络往返中完成，显著降低延迟  
- 🔒 **能力安全模型**：通过对象能力模式实现天然授权机制，例如会话对象不可伪造  
- 🔧 **多传输协议支持**：默认兼容 HTTP、WebSocket 和 postMessage，易于扩展其他传输方式  
- 📜 **JSON 序列化**：采用人类可读的 JSON 格式，支持结构化克隆类型  
- 🛠️ **TypeScript 深度集成**：提供端到端类型检查，保持开发时类型安全  
- 💡 **替代 GraphQL 方案**：通过 Promise 流水线解决数据瀑布问题，无需额外查询语言  
- 🧩 **数组操作优化**：支持服务端同步映射处理，避免客户端循环的网络开销

---

### [Cap'n Proto：简介](https://capnproto.org/)

**原文标题**: [Cap'n Proto: Introduction](https://capnproto.org/)

Cap'n Proto 是一种极快的数据交换格式和基于能力的 RPC 系统，其编码无需编解码步骤，支持跨平台兼容性、安全验证和高效压缩，并提供随机访问、多语言互操作等高级特性。

- 🚀 无需编解码步骤，直接读写内存数据实现无限快速度
- 🌍 字节级平台无关编码，支持小端序整数和偏移指针
- 🔄 向后兼容设计，新字段始终添加到结构体末尾
- 📦 支持快速压缩方案（打包）消除零值字节浪费
- 🛡️ 访问器方法验证指针安全性，通过模糊测试和专家审查
- ⏱️ 支持增量读取和随机访问字段
- 💾 内存映射读取大文件，操作系统按需加载
- 🔗 多语言共享内存结构，进程间通信无需内核转发
- 🧠 竞技场分配提升缓存局部性，减少内存分配
- 📐 生成代码量极小，运行时库非常精简
- ⏪ RPC 系统支持时间旅行，提前返回调用结果

---

### [GitHub - sindresorhus/globby：用户友好的全局模式匹配工具](https://github.com/sindresorhus/globby)

**原文标题**: [GitHub - sindresorhus/globby: User-friendly glob matching](https://github.com/sindresorhus/globby)

globby 是一个基于 fast-glob 的用户友好型 glob 匹配库，提供扩展功能和易用 API

- 🚀 基于 fast-glob 并扩展了多项实用功能
- 📁 支持自动展开目录和多种匹配模式
- ❌ 提供否定模式支持，可排除特定文件
- 🔧 兼容 .gitignore 及其他忽略配置文件
- ⚡ 提供同步、异步和流式处理多种 API
- 📦 支持通过 npm 快速安装使用
- 🎯 包含路径匹配检测和忽略文件检查工具函数
- 🔍 支持动态模式识别和批量任务生成
- 📄 采用 MIT 开源许可证，社区活跃度高

---

### [GitHub - hyparam/icebird: Icebird：JavaScript 冰山客户端](https://github.com/hyparam/icebird)

**原文标题**: [GitHub - hyparam/icebird: Icebird: JavaScript Iceberg Client](https://github.com/hyparam/icebird)

Icebird 是一个用于在 JavaScript 中读取 Apache Iceberg 数据表的开源库，基于 hyparquet 构建，支持远程数据访问和元数据查询。

- 🐧 支持读取 Apache Iceberg v1/v2格式数据表，暂不支持v3版本
- 📚 提供元数据查询功能，可获取表结构和版本信息
- 🌐 支持通过 URL 访问远程数据表，可配置认证信息
- ⏰ 具备时间旅行功能，可读取历史版本数据
- 📊 支持 Parquet 和 Avro 存储格式，暂不支持 ORC 和 Puffin
- 🗂️ 支持文件目录和基础删除操作，暂不支持高效分区查询
- 🔧 提供 React 集成示例和在线演示应用
- 📄 采用 MIT 开源协议，GitHub 获 79 星标和 2 个分支

---

### [GitHub - dmtrKovalenko/odiff：超高速SIMD优先图像对比库（含Node.js API）](https://github.com/dmtrKovalenko/odiff)

**原文标题**: [GitHub - dmtrKovalenko/odiff: A very fast SIMD-first image comparison library (with nodejs API)](https://github.com/dmtrKovalenko/odiff)

odiff 是一个基于 Zig 语言开发的超高速图像对比库，通过 SIMD 指令集优化实现毫秒级像素级差异检测，支持多平台和多种图像格式。

- 🚀 全球最快的单线程像素级图像差异检测工具，比 ImageMagick 快 6 倍
- 🖼️ 支持 PNG/JPEG/TIFF 等格式的跨格式对比，兼容不同图像布局
- ⚙️ 提供 Node.js API 及 CLI 工具，集成 Cypress 等可视化测试框架
- 🎯 采用 YIQ NTSC 传输算法，支持抗锯齿检测和忽略区域设置
- 🔧 支持 SSE2/AVX2/AVX512/NEON 等 SIMD 指令集优化，内存控制精准
- 📊 具备 100% 测试覆盖率，被 LostPixel、Argos CI 等主流视觉测试服务采用
- 📦 通过 npm 安装 odiff-bin 即可跨平台使用，MIT 开源协议

---

### [GitHub - isomorphic-git/isomorphic-git：适用于Node和浏览器的纯JavaScript Git 实现！](https://github.com/isomorphic-git/isomorphic-git)

**原文标题**: [GitHub - isomorphic-git/isomorphic-git: A pure JavaScript implementation of git for node and browsers!](https://github.com/isomorphic-git/isomorphic-git)

这是一个用纯 JavaScript 实现的 Git 库，可在 Node.js 和浏览器环境中运行，提供完整的 Git 操作功能。

- 🚀 纯 JavaScript 实现的 Git 工具，兼容 Node.js 和浏览器环境
- 🔄 提供完整的 Git 操作功能，包括克隆、提交、推送等
- 📦 采用模块化设计，支持按需引入以减小打包体积
- 🌐 需要自行提供文件系统和 HTTP 客户端适配
- 🛠️ 包含 CLI 工具 isogit 用于快速测试
- 📚 拥有完善的 TypeScript 类型定义
- 👥 由社区驱动维护，支持通过 OpenCollective 赞助开发
- ✅ 测试覆盖主流浏览器和 Node.js 环境
- 🔗 支持 CORS 代理解决跨域问题
- 📄 采用 MIT 开源协议

---

### [GitHub - withcatai/node-llama-cpp：在本地机器上使用node.js绑定llama.cpp运行AI模型，并在生成级别对模型输出强制执行JSON模式。](https://github.com/withcatai/node-llama-cpp)

**原文标题**: [GitHub - withcatai/node-llama-cpp: Run AI models locally on your machine with node.js bindings for llama.cpp. Enforce a JSON schema on the model output on the generation level](https://github.com/withcatai/node-llama-cpp)

node-llama-cpp 是一个基于 Node.js 的本地 AI 模型运行工具，通过 llama.cpp 绑定实现在个人设备上运行大型语言模型，支持强制 JSON 格式输出和硬件自适应。

- 🚀 支持在本地运行 AI 模型，无需联网即可使用
- 🔧 提供预构建二进制文件，并支持从源码自动编译
- ⚡ 兼容多种硬件加速（Metal/CUDA/Vulkan），自动适配配置
- 📝 可强制模型生成结构化输出（如 JSON 格式）
- 🛠️ 包含完整开发工具链，支持 TypeScript 和详细文档
- 💬 提供命令行工具，无需编码即可与模型对话
- 🔒 具备安全防护机制，防止特殊标记注入攻击
- 📦 支持函数调用、嵌入和重排序等高级功能

---

### [GitHub - vitaly-t/pg-promise：Node.js 的 PostgreSQL 接口](https://github.com/vitaly-t/pg-promise)

**原文标题**: [GitHub - vitaly-t/pg-promise: PostgreSQL interface for Node.js](https://github.com/vitaly-t/pg-promise)

pg-promise 是一个基于 node-postgres 构建的 Node.js PostgreSQL 接口库，提供自动连接管理、强大的查询格式化引擎和声明式查询结果处理等功能。

- 🚀 基于 node-postgres 构建，支持自动连接和事务管理
- 🔧 内置强大的查询格式化引擎，支持索引变量和命名参数
- 📝 提供声明式查询结果处理方法（none/one/many 等）
- 📁 支持外部 SQL 文件加载和动态重载
- 🔄 通过 task/tx 方法实现共享连接和自动事务控制
- 🛡️ 支持嵌套事务和可配置事务模式
- 💡 提供自定义类型格式化和查询过滤功能
- ⚡ 包含连接池管理和库销毁方法

---

### [GitHub - taskforcesh/bullmq: BullMQ - 基于 Redis 的 NodeJS 与 Python 消息队列及批处理系统](https://github.com/taskforcesh/bullmq)

**原文标题**: [GitHub - taskforcesh/bullmq: BullMQ - Message Queue and Batch processing for NodeJS and Python based on Redis](https://github.com/taskforcesh/bullmq)

BullMQ 是一个基于 Redis 的高性能分布式消息队列和批处理系统，支持 Node.js 和 Python 开发，提供稳定的任务管理和原子操作保障。

- 🚀 基于 Redis 的快速可靠分布式队列，适用于 Node.js 和 Python
- 🛠️ 提供队列管理、工作进程、任务事件监听和父子任务依赖关系
- 📊 支持延迟任务、优先级、并发控制、速率限制和可重复任务
- 🌐 提供专业管理界面 Taskforce.sh，用于监控队列、任务统计和操作
- 🔄 与 BullMQ-Pro 相比，具备基础的消息队列功能，支持任务去重和依赖管理
- 📄 采用 MIT 许可证，拥有活跃的社区和持续更新
- ⭐ 在 GitHub 上获得 7.7k 星标，被多家知名机构使用

---

### [GitHub - tediousjs/node-mssql：适用于 Node.js 的 Microsoft SQL Server 客户端](https://github.com/tediousjs/node-mssql)

**原文标题**: [GitHub - tediousjs/node-mssql: Microsoft SQL Server client for Node.js](https://github.com/tediousjs/node-mssql)

这是一个用于 Node.js 的 Microsoft SQL Server 客户端库，支持多种驱动程序和连接方式，提供丰富的数据库操作功能。

- 🗄️ 支持多种 TDS 驱动程序，包括默认的 Tedious（纯 JavaScript）和可选的 MSNodeSQLv8（Windows 认证）
- 📦 提供连接池管理，支持全局连接池和自定义连接池配置
- 🔄 支持多种编程模式：Async/Await、Promise、ES6 标签模板、回调函数和流式处理
- 🛡️ 内置 SQL 注入防护，支持参数化查询和存储过程调用
- 📊 支持事务处理、预处理语句和批量操作
- 🌐 支持 Azure Active Directory 多种认证方式
- 📋 提供表值参数（TVP）和地理空间数据类型支持
- ⚡ 支持 JSON 数据解析和重复列名处理
- 🐛 完善的错误处理机制，包含连接错误、事务错误、请求错误等分类
- 📖 提供详细的文档和丰富的代码示例
- 🔧 支持 CLI 命令行工具，便于脚本操作
- 📈 持续维护更新，支持最新 Node.js 版本和 SQL Server 特性

---

### [GitHub - vpulim/node-soap：适用于 Node.js 的 SOAP 客户端与服务器](https://github.com/vpulim/node-soap)

**原文标题**: [GitHub - vpulim/node-soap: A SOAP client and server for node.js.](https://github.com/vpulim/node-soap)

这是一个用于 Node.js 的 SOAP 客户端和服务器库，支持创建 SOAP 客户端和服务器，处理 WSDL 文件，并提供多种安全协议和自定义选项。

- 🚀 **功能丰富**：支持 RPC 和 Document 类型的 SOAP 消息，提供同步和异步方法处理，兼容 Express 服务器
- 🔒 **安全协议**：内置多种安全机制，包括 BasicAuth、WSSecurity、SSL 等，支持自定义认证
- ⚙️ **高度可配置**：允许覆盖命名空间、XML 属性键值，支持自定义反序列化和空标签格式
- 📡 **客户端操作**：可通过 WSDL 创建客户端，调用远程方法，管理 SOAP 头信息，支持附件和 MTOM
- 🖥️ **服务器功能**：能够创建 SOAP 服务器，定义服务方法，处理请求和响应事件，支持日志记录
- 🔄 **灵活数据处理**：提供 XML 与对象间的转换功能，支持覆盖导入路径和相对路径处理
- 🛠️ **扩展性强**：允许使用自定义 HTTP 客户端、缓存实现，以及通过事件机制进行深度定制

---

### [GitHub - pinojs/pino：🌲 超快速、纯天然的 JSON 日志记录器](https://github.com/pinojs/pino)

**原文标题**: [GitHub - pinojs/pino: 🌲 super fast, all natural json logger](https://github.com/pinojs/pino)

Pino 是一个专为 Node.js 设计的超高性能 JSON 日志记录库，具有极低开销和丰富的生态系统支持。

- 🌲 超快速且纯天然的 JSON 日志记录器
- ⚡ 极低开销，性能超过其他日志库 5 倍以上
- 📝 支持异步日志记录和子日志记录器
- 🔧 提供传输机制，建议在独立线程中处理日志
- 🌐 兼容 Node.js、Bare 和 Pear 运行时环境
- 📦 支持通过 webpack 或 esbuild 进行打包
- 🛠️ 提供丰富的 API 和文档支持
- 📊 包含基准测试和开发格式化工具
- 🔒 采用 MIT 开源许可证
- 👥 由 nearForm 和 Platformatic 赞助的开源项目

---

### [发布 v4.6.0 · NodeBB/NodeBB · GitHub](https://github.com/NodeBB/NodeBB/releases/tag/v4.6.0)

**原文标题**: [Release v4.6.0 · NodeBB/NodeBB · GitHub](https://github.com/NodeBB/NodeBB/releases/tag/v4.6.0)

NodeBB v4.6.0 版本发布，包含功能更新、错误修复和依赖升级

- 🆕 新增远程分类昵称功能，支持用户自动分类规则
- 🌐 允许活动内容标记为公开，改进 HTML 标题元素预处理
- 🔧 修复登录处理、权限检查及远程分类删除等多项问题
- 📦 更新 webpack、mongodb 等多项依赖至最新版本
- ⚡ 优化旧版升级脚本性能，重构部分代码逻辑
- 🔄 调整文章/摘要生成逻辑，恢复部分测试相关设置

---

### [ESLint v9.37.0 发布 - ESLint - 可插拔 JavaScript 代码检查工具](https://eslint.org/blog/2025/10/eslint-v9.37.0-released/)

**原文标题**: [ESLint v9.37.0 released - ESLint - Pluggable JavaScript Linter](https://eslint.org/blog/2025/10/eslint-v9.37.0-released/)

ESLint v9.37.0 版本发布，作为一次小版本升级，引入了新功能并修复了之前版本中的多个错误。

- 🚀 **no-restricted-imports 规则新增 allowTypeImports 选项**：允许在 TypeScript 文件中仅导入类型，同时禁止常规导入，与 typescript-eslint 规则保持一致。
- ⚡ **改进 --concurrency=auto 的启发式算法**：优化多线程 linting 性能，避免在结果已缓存时启用多线程模式带来的不必要开销。
- 🛠️ **preserve-caught-error 规则支持计算属性语法**：正确识别使用计算属性语法抛出的错误中的 cause 选项。
- 🐛 **修复 no-loss-of-precision 规则误报**：解决前导零导致的误报问题。
- 📚 **更新文档和类型定义**：修复文档中的拼写错误，改进可访问性，并更新 ESLint 类型定义。
- 🔧 **内部优化和依赖更新**：包括性能提升、测试清理和依赖版本管理。

---

### [Holepunch - 高级 Node.js 软件工程师（全球远程，全职）](https://holepunch.recruitee.com/o/senior-node-engineer?source=Node-Weekly)

**原文标题**: [Holepunch - Senior Node.js Software Engineer (100% Remote, Worldwide)](https://holepunch.recruitee.com/o/senior-node-engineer?source=Node-Weekly)

Holepunch 是一家专注于构建去中心化互联网架构的科技公司，通过其开源技术栈 Pear 开发点对点（P2P）平台，旨在赋予用户数据控制权并提升隐私保护。公司正在招聘远程 Node.js 软件工程师，以推动 P2P 技术生态系统的扩展。

- 🌐 公司使命是重新定义互联网架构，强调用户数据自主和隐私保护，采用 P2P 技术消除传统服务器依赖。
- 💻 核心平台 Pear 支持从开发者机器直接部署应用，实现可扩展的 P2P 连接和数据复制，类似 BitTorrent 的 Node.js 技术。
- 📱 旗舰应用 Keet 展示 P2P 通信潜力，涵盖消息传递、文件共享等功能，体现去中心化技术的灵活性和用户主权。
- 🔧 招聘职位要求 Node.js 经验，熟悉模块化开发、测试调试，并对 P2P 技术有热情，C/C++ 和远程协作经验为加分项。
- 🚀 工作机会提供前沿技术挑战，团队协作重塑数字世界，致力于构建安全、包容的去中心化未来。

---

### [Holepunch - 高级 Node.js 软件工程师（全球远程，全职）](https://holepunch.recruitee.com/o/senior-node-engineer?source=Node-Weekly)

**原文标题**: [Holepunch - Senior Node.js Software Engineer (100% Remote, Worldwide)](https://holepunch.recruitee.com/o/senior-node-engineer?source=Node-Weekly)

Holepunch 是一家专注于构建去中心化互联网架构的科技公司，通过其开源技术栈 Pear 开发点对点（P2P）平台，旨在赋予用户数据自主权并提升隐私保护。公司正在招聘远程 Node.js 软件工程师，共同推动 P2P 技术发展。

- 🚀 公司使命：通过 P2P 技术重塑互联网架构，确保用户数据隐私与去中心化控制  
- 🌐 核心技术：基于开源平台 Pear 开发，支持应用从本地直接部署，无需传统服务器  
- 📱 旗舰产品：Keet 通讯应用展示 P2P 技术在消息、文件共享等场景的潜力  
- 💻 职位需求：Node.js 开发经验，熟悉模块化代码、测试调试，热爱 P2P 技术  
- 🌍 工作模式：全球远程协作，需具备分布式团队合作能力  
- ⚙️ 技术生态：维护超 1500 个 npm 模块，构建模块化代码库  
- 🔑 加分技能：C/C++ 或 Node 本地绑定开发经验（非必需）  
- ✨ 团队文化：与创新者共同打造以用户为中心的去中心化未来

---

### [Postgres 周刊](https://postgresweekly.com/)

**原文标题**: [Postgres Weekly](https://postgresweekly.com/)

每周通过电子邮件汇总 PostgreSQL 相关资讯和技术文章的订阅服务
- 📧 17280 位订阅者定期接收邮件推送
- 📰 已发布 618 期内容并持续更新
- 🔗 提供 RSS 订阅方式及最新期刊预览
- 🏢 由 Cooperpress 独立运营发布
- 🛡️ 严格执行隐私保护及反垃圾邮件政策
- ⚠️ 声明与 PostgreSQL 社区协会无隶属关系

---

### [React 19.2 – React](https://react.dev/blog/2025/10/01/react-19-2)

**原文标题**: [React 19.2 – React](https://react.dev/blog/2025/10/01/react-19-2)

React 19.2 版本正式发布，这是继 React 19 和 19.1 后的第三次年度更新，新增多项核心功能与优化，涵盖组件控制、性能调试及服务端渲染增强等领域。

- 🎭 **Activity 组件**：通过`visible`/`hidden`模式控制组件渲染状态，隐藏时暂停副作用与更新，提升预渲染效率与导航体验
- 🚀 **useEffectEvent Hook**：分离 Effect 中的事件逻辑，解决非必要依赖（如 theme 变更）导致的重复执行问题，需配合 eslint-plugin-react-hooks@6.1.1 使用
- 🗂️ **cacheSignal API**：专为服务端组件设计，通过信号机制感知缓存生命周期，支持渲染中止或失败时的资源清理
- 📊 **性能追踪工具**：新增 Chrome DevTools 定制轨道，可监控调度器任务优先级与组件渲染/副作用执行时序
- 🌐 **局部预渲染**：支持将静态内容预渲染至 CDN，通过`resume`系列 API 动态填充内容，提升首屏加载速度
- ⚡ **SSR 批量处理**：服务端渲染时对 Suspense 边界内容进行批量揭示，改善流式渲染体验并为 ViewTransition 动画做准备
- 🔄 **Node.js Web Streams 支持**：新增`renderToReadableStream`等 Web Streams API，同时推荐优先使用性能更优的 Node Streams 方案
- 🔧 **工具链升级**：eslint-plugin-react-hooks 升级至 v6，默认启用扁平配置，新增 React 编译器规则选项
- 🆔 **useId 前缀更新**：默认前缀改为`_r_`，确保与 View Transitions 及 XML 1.0 规范的兼容性
- 🐞 **多项问题修复**：涵盖 useDeferredValue 循环、表单提交崩溃、脱水边界重悬停等核心场景稳定性提升

---

### [Svelte 2025 年 10 月更新亮点](https://svelte.dev/blog/whats-new-in-svelte-october-2025)

**原文标题**: [What’s new in Svelte: October 2025](https://svelte.dev/blog/whats-new-in-svelte-october-2025)

2025 年 10 月 Svelte 生态更新概览：远程函数功能增强、新增从 Playground 创建项目功能、实验性异步 SSR 上线，并收录了大量社区优秀项目与工具。

- 🚀 远程函数新增批处理工具与惰性发现机制，提升性能与树摇优化
- 🎮 支持通过 npx sv create --from-playground 从 Playground 直接创建项目
- ⚡ 实验性异步 SSR 功能开放测试，可在配置中启用 experimental.async 选项
- 🔗 导航事件属性增强，新增 SvelteKit 版本占位符功能
- 📊 社区展示涵盖 Windframe 设计工具、pgpad 数据库客户端等创新应用
- 🎓 学习资源新增 Svelte 5 完整课程、多语言教程与技术分享视频
- 🛠️ 工具生态推出 SVAR UI 组件库、拖拽库 dnd-kit 等开发工具
- 🌐 框架支持扩展，Astro 已原生支持 Svelte 异步渲染

---

### [Astro 2025 年 9 月更新亮点 | Astro](https://astro.build/blog/whats-new-september-2025/)

**原文标题**: [What’s new in Astro - September 2025 | Astro](https://astro.build/blog/whats-new-september-2025/)

Astro 生态系统在 2025 年 9 月迎来多项重要进展：月 npm 安装量突破 300 万，与 Cloudflare 等平台达成合作，发布 5.14 版本更新，新增 AI 工具集成与社区主题资源，并涌现大量创新应用案例。

- 🚀 Astro 月 npm 安装量突破 300 万次
- 🤝 与 Cloudflare、Webflow、Mux 建立合作伙伴关系
- 📦 发布 Astro 5.14 版本，支持 Svelte 异步渲染和 React 19 操作
- 🌐 谷歌、Genkit 等知名机构采用 Astro 构建项目
- 🎨 新增 RenderAI 绘图转换、学习阅读网站等创新应用
- 👥 迎来新维护者 Louis Escher，社区持续壮大
- 🛠️ 推出 Astro Takumi 等十余款开发工具与组件库
- 🎪 预告 ViteConf 大会及 React Advanced 演讲活动
- 📚 发布多款 Starlight 主题模板与企业级案例
- 📈 优化 PR 工作流，提升代码变更文档质量

---

### [ViteLand 九月 2025 回顾：VoidZero 版新特性一览](https://voidzero.dev/posts/whats-new-sep-2025)

**原文标题**: [What’s New in ViteLand: September 2025 Recap | VoidZero](https://voidzero.dev/posts/whats-new-sep-2025)

ViteLand 2025 年 9 月更新回顾：Rolldown 性能提升高达 45%，各项目推出新功能与社区活动丰富

- 🚀 Rolldown 在 Windows 和 macOS 平台分别实现 10-30% 和 10-45% 的构建速度提升，二进制体积减少 200KB
- ⚡ Vite 创建工具新增 Rolldown 选项，Vitest 浏览器测试支持调试和 Playwright 跟踪功能
- 🔧 Oxlint 性能提升 5-50%，新增错误保留规则自动修复，解决内存泄漏问题
- 📅 VoidZero 团队将在 10-11 月参与 ViteConf、JSConf 等 6 场国际技术大会进行分享
- 🌟 社区动态：Framer 全面部署 Rolldown，Qwik playground 性能提升 4 倍，date-fns 等知名项目转向 Oxlint
- 🎙️ 团队成员参与 SyntaxFM 等知名播客访谈，分享现代 JavaScript 工具链洞察

---

### [Angular 现支持在 Google AI Studio 中生成应用 | Angular 官方博客 | 2025 年 10 月](https://blog.angular.dev/angular-support-for-generating-apps-in-google-ai-studio-is-now-available-3a3afde38f58?gi=52e7b6ef6da9)

**原文标题**: [Angular support for generating apps in Google AI Studio is now available | by Angular | Oct, 2025 | Angular Blog](https://blog.angular.dev/angular-support-for-generating-apps-in-google-ai-studio-is-now-available-3a3afde38f58?gi=52e7b6ef6da9)

Google AI Studio 现已支持生成 Angular 应用，为开发者提供利用 Gemini 模型快速创建、部署和分享 Angular 项目的新方式。

- 🎉 宣布 Angular 与 Google AI Studio 集成，开发者现可利用 Gemini 模型生成 Angular 应用代码
- 🚀 支持快速原型开发：通过 AI 生成书店库存界面等应用，将开发周期从数周缩短至数天
- 🔧 简易操作流程：在 AI Studio 高级设置中选择 Angular 模板，输入提示词即可生成应用
- 🌐 集成部署功能：支持直接通过 Cloud Run 部署应用，并提供 GitHub 代码导出版本管理
- 💡 拓展 AI 能力：除代码生成外，还可利用 Gemini API 开发具备 AI 功能的应用
- 📢 协作分享机制：支持将生成的应用代码分享给团队成员或利益相关者进行协作
- 🆓 免费使用：开发者可立即通过 build.g.google.com 免费开始使用此功能

---

### [JSConf | LF 活动](https://events.linuxfoundation.org/jsconf-north-america/)

**原文标题**: [JSConf | LF Events](https://events.linuxfoundation.org/jsconf-north-america/)

JSConf 北美大会将于 2025 年 10 月 14-16 日在马里兰州切萨皮克湾举办，这是 OpenJS 基金会主办的 JavaScript 社区顶级盛会。活动包含主题演讲、分组会议和独特的自主探险日，提供家庭友好服务，并与 ng-conf 联合举办，为参与者打造沉浸式技术交流体验。

- 🗓️ 活动时间：2025 年 10 月 14-16 日（含 13 日欢迎酒会）
- 🌊 举办地点：马里兰州切萨皮克湾凯悦度假酒店（含机场接送）
- 🎯 核心特色：主题演讲/分组会议 + 自主探险日（高尔夫/划艇/螃蟹宴等）
- 👨‍👩‍👧 家庭友好：提供嘉宾通行证与免费儿童看护服务
- 🤝 特别合作：与 ng-conf 联合举办，注册 JSConf 可获 Angular 会议折扣票
- 🚀 行业影响：曾是革命性库与商业合作的发源地
- 🎤 演讲嘉宾：包含 Evan You（Vue.js 创始人）、Robin Bender Ginn（OpenJS 基金会执行董事）等 12 位行业领袖
- ⏳ 紧迫提示：活动与酒店名额有限，预计很快售罄

---

### [PostgreSQL：PostgreSQL 18 发布！](https://www.postgresql.org/about/news/postgresql-18-released-3142/)

**原文标题**: [PostgreSQL: PostgreSQL 18 Released!](https://www.postgresql.org/about/news/postgresql-18-released-3142/)

PostgreSQL 18 正式发布，这是全球最先进的开源数据库的最新版本，通过异步 I/O 子系统显著提升性能，支持虚拟生成列和 OAuth 2.0 认证，并优化了版本升级流程与查询效率。

- 🚀 异步 I/O 子系统实现存储读取性能提升高达 3 倍，支持并发 I/O 请求
- 📊 支持跨大版本升级保留规划器统计信息，减少升级后性能波动
- 🔍 多列 B 树索引支持"跳跃扫描"，优化 OR 条件查询与表连接性能
- 💡 新增虚拟生成列（默认选项）和 UUIDv7 函数，提升开发效率
- 🔐 引入 OAuth 2.0 认证机制，弃用 MD5 密码验证
- 📝 增强全文搜索与 Unicode 排序性能，新增 PG_UNICODE_FAST 排序规则
- 🔄 逻辑复制默认启用并行流式传输，支持自动清理空闲复制槽
- 📈 EXPLAIN 分析功能新增缓冲区统计与索引查找次数显示
- ⚙️ 默认启用页面校验和，新增 PostgreSQL 有线协议 3.2 版本

---

### [深入探索 Postgres 18 新特性 | xata](https://xata.io/blog/going-down-the-rabbit-hole-of-postgres-18-features)

**原文标题**: [Going down the rabbit hole of Postgres 18 features | xata](https://xata.io/blog/going-down-the-rabbit-hole-of-postgres-18-features)

PostgreSQL 18 已发布稳定版，带来异步 I/O 架构、OAuth 2.0 支持、UUIDv7 原生生成等核心功能，涵盖性能优化、运维效率提升及开发者工具增强，包含超过 3000 项提交。

- 🚀 异步 I/O 框架支持并行请求与直接 I/O，显著提升顺序扫描性能（2-3 倍），尤其适用于高并行存储场景
- 🔐 内置 OAuth 2.0 认证，支持 SSO 登录和应用令牌连接，替代传统静态密码
- ⚡ 原生 UUIDv7 支持时间排序主键，改善索引局部性与压缩效率
- 🔄 RETURNING 子句支持 OLD/NEW 显式返回旧值/新值，简化数据更新逻辑
- 💾 生成列默认改为 VIRTUAL（按需计算），支持逻辑复制传输
- ⏳ 时序数据库功能增强，支持 WITHOUT OVERLAPS 约束防止时间区间重叠
- 🛠️ NOT NULL 约束支持 NOT VALID 模式，实现无锁表约束验证
- 📈 并行化 pg_upgrade 大幅提升升级速度，支持统计信息迁移
- 🔍 EXPLAIN ANALYZE 默认启用 BUFFERS 选项，增强查询性能诊断
- 📊 新增进程级统计（pg_stat_get_backend_io）与连接建立时长日志
- 🧩 B-tree 跳跃扫描优化多列索引查询，支持非前缀列条件检索
- 💡 SQL 函数启用计划缓存，自连接消除与 DISTINCT 列重排序提升执行效率
- 🌀 新增 casefold() 函数与加速的 lower()/upper() 实现，优化字符处理
- 📋 新增数组反转排序（array_reverse/array_sort）与 ACL 权限查询（pg_get_acl）工具函数

---

