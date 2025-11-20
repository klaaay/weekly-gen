### [Node 周刊第 601 期：2025 年 11 月 18 日](https://nodeweekly.com/issues/601)

**原文标题**: [Node Weekly Issue 601: November 18, 2025](https://nodeweekly.com/issues/601)

Node.js 周报第 601 期（2025 年 11 月 18 日）技术动态汇总

- 🚀 Node.js v25.2.0 将类型剥离功能标记为稳定版，v25.2.1 修复了 localStorage 异常问题
- 📊 Memetria K/V 为 Node 应用提供实时 Redis 监控仪表盘
- ⚖️ Electron 与 Tauri 桌面应用开发框架对比研究结果公布
- 🔒 OpenJS 基金会发布 2025 年 10 月安全更新报告
- 💬 Reddit 社区对 NestJS 展开激烈讨论，/r/node 活跃度超越/r/javascript
- 📈 Error.captureStackTrace 提案进入 TC39 阶段 2
- 🐛 Node.js v24.11.1(LTS) 修复 Buffer.allocUnsafe 漏洞
- 🗑️ V8 引擎垃圾回收机制近年技术演进分析
- 🔄 GitHub Actions 实现 NPM 密钥自动轮换方案
- 📑 Node.js Utilities 官方弃用方法指南发布
- 🚀 Tinyglobby 模块现代化改造性能提升案例
- 🕵️ 印尼食品 NPM 垃圾软件包窃取事件分析
- 💡 JavaScript 安全编程实用技巧合集
- 🛠️ Inquirer.js 13.0 发布，仅支持 ESM 并集成 Node.styleText
- 📄 Foxit 推出 JSON 转 PDF 工作流解决方案
- 🔍 Globby 16.0 增强 glob 模式匹配，支持父级.gitignore
- 🌐 node-libcurl 5.0 升级至 libcurl 8.17.0，全平台启用 HTTP/3
- 📊 Ackee 3.5 自托管网站分析系统更新
- ⚡ Marked.js 17.0 高速 Markdown 解析器发布
- 📦 pnpm 10.22 新增信任策略排除选项
- 🗃️ MikroORM 6.6 增强关系过滤器与私有属性访问
- 🤖 OpenAI Node 6.9 支持 GPT-5.1 新模型
- 🔧 ESLint v10.0.0 Alpha 预览版发布
- 📝 LogTape 1.2 全 JS 运行时日志库更新
- 🎯 pg-boss 12.2 基于 Postgres 的任务队列系统
- 🏗️ Mercurius 16.6 优化 Fastify 的 GraphQL 支持
- ✨ FoalTS 5.1 全功能 Node.js 框架升级

---

### [获取失败](https://nodeweekly.com/link/177125/web)

**原文标题**: [Failed to retrieve](https://nodeweekly.com/link/177125/web)

无法总结：获取内容失败，状态码 503。

---

### [Node.js — Node.js v25.2.0（当前版本）](https://nodejs.org/en/blog/release/v25.2.0)

**原文标题**: [Node.js — Node.js v25.2.0 (Current)](https://nodejs.org/en/blog/release/v25.2.0)

Node.js v25.2.0 版本发布，包含多项功能增强、性能优化和错误修复，涵盖模块系统、网络、Node-API、V8 引擎等核心组件，同时更新了依赖项并改进了开发工具链。

- 🚀 模块系统：类型剥离功能标记为稳定状态
- ⏱️ 网络优化：网络家族自动选择超时时间增加至 500 毫秒
- 🔧 Node-API：新增 napi_create_object_with_properties 方法
- 📊 V8 引擎：HeapStatistics 新增 total_allocated_bytes 属性
- 🛠️ 工具函数：util.deprecate 新增选项配置
- 🗃️ 本地存储：缺失存储路径时 localStorage getter 抛出错误
- 🔍 调试增强：检查器支持 HTTP/2 请求和响应体检查
- ⚡ 性能提升：优化缓冲区连接和单字符串日志记录性能
- 📚 文档完善：更新多个模块文档和代码示例
- 🔄 依赖更新：升级 nghttp2、simdjson、corepack 等核心依赖版本

---

### [模块：TypeScript | Node.js v25.2.1 文档](https://nodejs.org/api/typescript.html)

**原文标题**: [Modules: TypeScript | Node.js v25.2.1 Documentation](https://nodejs.org/api/typescript.html)

Node.js v25.2.1 文档中关于 TypeScript 模块支持的概述，包含完整 TypeScript 功能支持和内置类型剥离两种方式，重点说明了配置要求、语法限制和运行机制。

- 📚 **启用方式**：可通过第三方包（如 tsx）获得完整 TypeScript 支持，或使用内置类型剥离功能
- 🧹 **类型剥离**：默认移除可擦除类型语法（替换为空白符），需通过 --experimental-transform-types 标志启用非擦除语法转换
- ⚙️ **模块系统**：根据文件扩展名（.ts/.mts/.cts）和 package.json 配置自动识别 CommonJS/ES 模块
- 🚫 **限制特性**：不支持需要代码生成的 TypeScript 语法（枚举/参数属性等），且不读取 tsconfig.json 配置
- 🔧 **导入规范**：类型导入必须使用 type 关键字，文件扩展名在 import/require 中强制要求
- 📁 **路径处理**：不支持 tsconfig 路径别名，建议使用子路径导入（以 # 开头）
- 🗂️ **依赖限制**：拒绝处理 node_modules 目录下的 TypeScript 文件
- 🗺️ **源码映射**：基础类型剥离无需源码映射，启用代码生成时会自动开启源码映射支持

---

### [使用 Memetria K/V 构建 — Memetria](https://dashboard.memetria.com/nodeweekly/)

**原文标题**: [Build with Memetria K/V — Memetria](https://dashboard.memetria.com/nodeweekly/)

Memetria 是一个提供键值存储服务的云平台，支持 Valkey 和 Redis OSS，具备无缝扩展、加密连接和详细监控功能，并提供从开发到高性能的多层级托管方案。

- 💾 兼容 Valkey 和 Redis OSS，支持轻松导入导出数据
- 📊 提供无缝扩展能力，可在不停机情况下调整规模
- 🔐 支持双重加密和 TLS 专用连接选项
- 📈 具备健康状态、内存及性能指标的详细监控图表
- 🌍 覆盖全球多个 AWS 区域部署选项
- 💰 提供开发版（14 美元起）、生产版（89 美元起）和高性能版（779 美元起）三档套餐
- 🚀 高性能套餐包含专属资源、高速 I/O 和最高配置容量

---

### [Electron 与 Tauri 对比 | DoltHub 博客](https://www.dolthub.com/blog/2025-11-13-electron-vs-tauri/)

**原文标题**: [Electron vs. Tauri | DoltHub Blog](https://www.dolthub.com/blog/2025-11-13-electron-vs-tauri/)

Dolt Workbench 团队在评估 Electron 和 Tauri 两种桌面应用框架的集成效果，分析了各自的优缺点及迁移可行性。

- 🖥️ Electron 基于 Chromium 引擎确保跨平台一致性，但会导致应用体积臃肿（基础应用 150MB+）
- ⚡ Tauri 利用系统原生 Webview 实现轻量化，但需面对不同系统 Webview 的兼容性风险
- 🔧 Next.js 在 Electron 中需通过 Nextron 等第三方工具适配，而 Tauri 直接支持静态导出配置
- 🛠️ Electron 使用 Node.js 作为主进程，适合前端开发者；Tauri 采用 Rust 需要额外学习成本
- 📦 Electron 内置 Node 运行时便于侧载进程管理，Tauri 需额外编译二进制文件作为侧载服务
- 🚧 Tauri 目前存在 Windows 应用包格式限制和 MacOS 通用二进制文件签名问题
- ⚖️ 尽管 Tauri 在体积和代码集成方面优势明显，团队因平台适配问题暂缓迁移计划

---

### [Tauri 2.0 | Tauri](https://v2.tauri.app/)

**原文标题**: [Tauri 2.0 | Tauri](https://v2.tauri.app/)

Tauri 2.0 是一个用于构建轻量、快速、安全跨平台应用程序的开发框架

- 🚀 支持创建小型快速且安全的跨平台应用
- 🛠️ 提供多种创建项目方式（Bash/PowerShell/npm/Cargo 等）
- 🌐 前端框架无关，可兼容现有网页技术栈
- 📱 支持多平台部署（Linux/macOS/Windows/Android/iOS）
- 🔒 高度重视安全性，采用系统原生网页渲染器
- 📦 应用体积最小可达 600KB
- ⚙️ 前端使用 JavaScript，应用逻辑使用 Rust 开发
- 🤝 支持通过 Swift 和 Kotlin 进行系统深度集成

---

### [OpenJS 安全更新：2025 年 10 月 | OpenJS 基金会](https://openjsf.org/blog/openjs-security-update-oct-2025)

**原文标题**: [OpenJS Security Update: October 2025 | OpenJS Foundation](https://openjsf.org/blog/openjs-security-update-oct-2025)

OpenJS 基金会于 2025 年 10 月在安全领域取得显著进展，涵盖生态系统协作、Node.js 安全增强和项目支持等方面。

- 🛡️ npm 可信发布风险研讨：社区针对关键软件包提出缓解方案，并通过安全协作空间公开讨论成果
- 🔧 Node.js 安全升级：向 v24.x LTS 版本回溯允许检查器功能，优化权限模型架构
- 📊 漏洞协同处理：通过 HackerOne 平台完成漏洞分类，协调全生态系统响应机制
- 🔐 OpenSSL 影响评估：及时分析安全版本对 Node.js 的潜在影响，修复依赖评估工具报告问题
- 🤝 维护者安全峰会：Node.js 与 Express 团队联合举办安全会议，强化事件协调与依赖管理实践
- 📋 Lodash 安全强化：正式采纳威胁模型与事件响应计划，遵循 Express 和 Webpack 最佳实践
- ⚡ 运行时安全更新：Node.js v25 引入网络权限控制、全局 ErrorEvent、默认启用 Web 存储等安全功能
- 🔄 依赖管理优化：为 Dependabot 添加冷却期属性，有效减少冗余依赖更新请求
- 📢 知识普及计划：筹备发布《重构安全：从漏洞到威胁模型》系列技术博客，推动 JS 生态系统安全实践

---

### [Reddit——互联网之心](https://www.reddit.com/r/node/comments/1ov6xrd/nestjs_is_bad_change_my_mind/?rdt=53747)

**原文标题**: [Reddit - The heart of the internet](https://www.reddit.com/r/node/comments/1ov6xrd/nestjs_is_bad_change_my_mind/?rdt=53747)

该文章作者表达了对 NestJS 框架的强烈不满，基于多年使用经验指出其存在过度设计、代码复杂、安全性差等系统性问题

- 🏗️ 过度工程化的依赖注入实现，相比 ECMAScript 原生方案更复杂且不利于初级开发者和 AI 工具使用
- 🕸️ 核心代码库复杂度过高，PR 审查耗时远超编写时间，修改易引发隐藏副作用
- 🔄 重复造轮子问题突出，例如自研类 EJS 模板语言存在长期未修复的安全漏洞
- 🚨 安全响应机制迟缓，作者提交的安全漏洞修复 PR 耗时数月才被接受
- 📦 生产环境包含非必要依赖（如 webpack），增加资源负担
- 🔗 与生态兼容性差，自定义依赖注入等实现阻碍了标准解决方案（Loader API/MJS规范）的集成

---

### [NestJS - 一个渐进的 Node.js 框架](https://nestjs.com/)

**原文标题**: [NestJS - A progressive Node.js framework](https://nestjs.com/)

NestJS 是一个渐进式 Node.js 框架，用于构建高效可靠的服务器端应用

- 🏗️ 采用模块化架构提供高度可扩展性
- 🚀 支持微服务架构和 Web 应用开发
- ⚡ 内置依赖注入系统提升可测试性
- 🛡️ 基于 TypeScript 提供类型安全支持
- 🌐 拥有丰富的工具生态系统
- 🏢 被众多企业采用，具备企业级可靠性
- 📚 提供官方课程和文档支持
- ☁️ 支持通过 Mau 平台快速部署到 AWS
- 💝 开源项目，接受社区赞助和支持
- 📧 提供新闻订阅服务保持更新同步

---

### [Reddit 编程社区对比 | 独立开发生活](https://strzibny.name/blog/comparing-programming-language-communities-on-reddit)

**原文标题**: [
        Comparing programming communities on Reddit | Indie Life
    ](https://strzibny.name/blog/comparing-programming-language-communities-on-reddit)

Reddit 平台近期更新了社区活跃度统计方式，从显示总订阅人数改为展示周访问量和周互动量，更真实反映编程语言社区的活跃情况。以下是基于周访问量排名的编程社区分析：

- 🐍 Python 以 23.6 万周访问量位居编程语言榜首，涵盖机器学习与 Web 开发等多领域
- 💎 C#以18.7万周访问量紧随其后，社区内容涵盖趣味帖文与技术讨论
- 🦀 Rust 社区以 18.4 万周访问量展现高互动性，技术新闻与争议话题并存
- 🔷 .NET 框架社区达 17.1 万访问量，企业级技术与趣味内容意外融合
- ⚡ Next.js 以 14.2 万访问量超越传统框架，反映现代前端开发趋势
- 🚀 Go 语言与 Next.js 持平，成功经验分享类内容最受欢迎
- 🗃️ SQL 虽非传统语言但以 12.1 万访问量成为重要参照标尺
- 📊 Node.js 保持 11.8 万访问量，仍是后端入门首选平台
- 🔧 C 语言以 10.7 万访问量展现经典语言的持久生命力
- ⚙️ C++ 以 9.7 万访问量略逊于 C 语言但互动更活跃
- ☕ Java 仅 8.5 万访问量，被.NET 生态反超显社区分流现象
- ⚛️ React 框架 7.9 万访问量反映其逐渐成为底层技术的现状
- 🌐 JavaScript 基础社区 6.1 万访问量，用户被细分框架分流
- 🎯 Django 框架 4.2 万访问量超越 PHP 整体社区
- 🐘 PHP 语言 3.8 万访问量与其网络普及度形成反差
- 💚 Vue 框架 3.7 万访问量保持稳定小众地位
- 💎 Rails 框架 2.6 万访问量见证技术迭代浪潮
- 🔷 Kotlin 与 Laravel 并列 2.5 万访问量
- ❤️ Ruby 语言 2.2 万访问量受社区分裂影响
- 🔮 Elixir 等新兴语言保持 1 万以下稳定社群

主要发现：企业级技术社区活跃度超预期，框架细分导致基础语言社区分流，传统语言仍保持稳定用户基础，Reddit 数据与 TIOBE 排名存在显著差异。

---

### [获取失败](https://nodeweekly.com/link/177134/web)

**原文标题**: [Failed to retrieve](https://nodeweekly.com/link/177134/web)

无法总结：获取内容失败，状态码 503。

---

### [GitHub - tc39/proposal-error-capturestacktrace：标准化Error.captureStackTrace](https://github.com/tc39/proposal-error-capturestacktrace)

**原文标题**: [GitHub - tc39/proposal-error-capturestacktrace: Standardizing Error.captureStackTrace](https://github.com/tc39/proposal-error-capturestacktrace)

该提案旨在标准化 JavaScript 引擎中的 Error.captureStackTrace 方法，该方法用于捕获自定义错误的堆栈跟踪信息，解决不同引擎间的兼容性问题。

- 🎯 **标准化目标** - 将 V8 和 JSC 引擎中已实现的非标准 Error.captureStackTrace 方法纳入 ECMAScript 标准
- 🔧 **功能说明** - 允许为任意对象添加堆栈跟踪属性，可选的 constructorOpt 参数可隐藏不必要的堆栈帧
- ⚠️ **兼容性问题** - V8 和 JSC 在实现上存在差异（访问器属性 vs 字符串属性），需要统一规范
- 📋 **提案状态** - 已进入 Stage 1 阶段，由 Mozilla 的 Matthew Gaudet 和 Daniel Minor 担任 champion
- 🔗 **相关提案** - 与 Error Stacks 和 Error Stack Accessor 提案相关但解决不同问题
- 📝 **实施细节** - 堆栈字符串格式由实现定义，不要求跨引擎一致性
- 📅 **历史进展** - 2025 年 2 月首次提出，同年 7 月再次讨论，10 月在 TG3 周会中审议
- 📊 **项目信息** - GitHub 仓库获得 10 星标、3 个分支，采用 MIT 许可证

---

### [Node.js — Node.js v24.11.1（长期支持版）](https://nodejs.org/en/blog/release/v24.11.1)

**原文标题**: [Node.js — Node.js v24.11.1 (LTS)](https://nodejs.org/en/blog/release/v24.11.1)

Node.js v24.11.1 (LTS) 版本发布，修复了 Buffer.allocUnsafe 内存初始化问题，包含多项性能优化、依赖更新及文档改进。

- 🐛 修复了 Buffer.allocUnsafe 未正确初始化内存的问题
- ⚡ 优化了基准测试工具和 V8 构建配置
- 📦 更新了 corepack、npm、simdjson 等核心依赖
- 📚 改进了文档准确性和代码示例
- 🔧 增强了 HTTP/2、inspector、vm 等模块功能
- 🧪 完善了测试框架和工具链支持
- 🌐 提供了全平台安装包和二进制文件下载

---

### [V8 垃圾收集器近两年进展 — wingolog](https://wingolog.org/archives/2025/11/13/the-last-couple-years-in-v8s-garbage-collector)

**原文标题**: [the last couple years in v8's garbage collector — wingolog](https://wingolog.org/archives/2025/11/13/the-last-couple-years-in-v8s-garbage-collector)

过去几年 V8 垃圾收集器主要围绕三大核心方向展开：内存安全沙盒建设、Oilpan 保守栈扫描集成，以及多线程内存管理支持。这些改进共同提升了 V8 的安全性和性能表现。

- 🛡️ 沙盒安全增强：通过 32/40 位指针偏移量隔离 JavaScript 堆，配合硬件内存保护机制，有效防止内存越界写入（约占 20% 开发资源）
- 🔄 Oilpan 集成：历经十年将 Blink 的保守栈扫描机制引入 V8，通过页面隔离和对象固定技术实现分代回收，同时支持更安全的直接句柄
- 🧵 多线程支持：为 WebAssembly 共享内存多线程场景优化对象对齐策略，确保 64 位字段原子访问安全性（约占 20% 开发资源）
- ⚖️ 启发式调优：针对不同平台（Android/iOS/Starboard）动态调整内存回收策略，涉及数百项参数优化（约占 10% 开发资源）
- 🔒 锁机制重构：全面改用 abseil 锁库解决 MacOS 上下文切换问题，提升多线程性能
- 🗑️ 第三方堆弃用：移除 MMTk 抽象层接口，专注浏览器特定场景优化

---

### [GitHub Actions 中自动轮换 NPM 密钥 | michaelheap.com](https://michaelheap.com/rotate-all-npm-tokens-github-actions/)

**原文标题**: [Automated NPM secret rotation in GitHub Actions | michaelheap.com](https://michaelheap.com/rotate-all-npm-tokens-github-actions/)

NPM 宣布撤销所有长期有效的令牌，并要求新令牌有效期不得超过 90 天，这对依赖访问令牌自动发布项目的开发者造成维护负担。虽然采用 OIDC 信任发布是根本解决方案，但作者通过自研工具实现批量更新密钥的临时方案。

- 🔐 NPM 强制要求访问令牌最长有效期为 90 天，影响自动化发布流程
- ⚙️ 作者开发 github-update-secret 工具批量更新 GitHub 仓库密钥
- 🔄 工具自动扫描用户所有仓库，识别指定密钥名称并更新其数值
- 🖥️ 支持通过环境变量或命令行参数传递 GitHub 身份验证信息
- 📝 提供调试模式可查看具体更新过程与受影响仓库列表
- ⏳ 该方案为临时过渡措施，最终仍需迁移至 OIDC 信任发布机制

---

### [npm 安全更新：经典令牌创建已禁用及细粒度令牌变更 - GitHub 更新日志](https://github.blog/changelog/2025-11-05-npm-security-update-classic-token-creation-disabled-and-granular-token-changes/)

**原文标题**: [npm security update: Classic token creation disabled and granular token changes - GitHub Changelog](https://github.blog/changelog/2025-11-05-npm-security-update-classic-token-creation-disabled-and-granular-token-changes/)

npm 宣布自 2025 年 11 月 5 日起实施令牌管理系统的安全升级措施，重点包括停用经典令牌和强化粒度令牌的安全设置。

- 🚫 经典令牌创建已全面禁用，现有令牌将在 11 月 19 日失效
- 🛡️ 新建粒度写入令牌默认强制启用双因素认证
- ⏳ 现有粒度写入令牌有效期统一调整为最长 90 天
- 🔄 用户需在 11 月 19 日前完成经典令牌到粒度令牌的迁移
- ⚙️ CI/CD工作流可选择性启用"绕过 2FA"选项
- 📅 2 月 3 日前需检查并更新到期令牌
- 🔒 GitHub 系列令牌不受本次变更影响
- ⚠️ 11 月 19 日将全面废止经典令牌并启用 2 小时会话令牌

---

### [如何利用 Node.js 工具“正式”弃用方法 | Stefan Judis 网页开发](https://www.stefanjudis.com/today-i-learned/deprecate-method-in-node-js/)

**原文标题**: [How to "officially" deprecate methods with Node.js utilities | Stefan Judis Web Development](https://www.stefanjudis.com/today-i-learned/deprecate-method-in-node-js/)

本文介绍了在 Node.js 中正式弃用方法的方式，包括使用 JSDoc 注释标记和 Node.js 内置的 util.deprecate 方法，帮助开发者更有效地向用户传达功能弃用信息。

- 📝 使用 JSDoc 的@deprecated 标记可在代码编辑器中显示弃用警告
- ⚠️ Node.js 提供 util.deprecate 方法，运行时会在控制台输出弃用警告
- 🔧 两种方式结合使用能确保开发者和用户都能及时获知弃用信息
- 📢 早期沟通功能变更可减少破坏性更新带来的负面影响
- 💡 作者建议维护库时积极采用这些弃用通知机制

---

### [工具集 | Node.js v25.2.1 文档](https://nodejs.org/docs/latest/api/util.html#utildeprecatefn-msg-code-options)

**原文标题**: [Util | Node.js v25.2.1 Documentation](https://nodejs.org/docs/latest/api/util.html#utildeprecatefn-msg-code-options)

Node.js v25.2.1 的 util 模块文档，提供了用于支持 Node.js 内部 API 的各种实用工具函数，这些工具对应用程序和模块开发者同样有用。

- 📚 **模块概述** - util 模块包含多种实用功能，支持调试、类型检查、格式化等操作
- 🔄 **回调与 Promise 转换** - 提供 `util.callbackify()` 将异步函数转换为回调风格，`util.promisify()` 将回调函数转换为 Promise 形式
- 🐛 **调试功能** - 包含 `util.debuglog()` 用于条件性调试输出，可根据环境变量控制日志显示
- ⚠️ **弃用管理** - `util.deprecate()` 用于标记已弃用的函数，调用时会发出警告
- 🔍 **对象检查** - `util.inspect()` 提供强大的对象检查功能，支持颜色输出、深度控制等多种选项
- 📊 **格式化工具** - `util.format()` 提供类似 printf 的字符串格式化功能，支持多种格式说明符
- 🔧 **类型检查** - 包含大量类型判断函数如 `util.types.isArrayBuffer()`、`util.types.isPromise()` 等
- 🌐 **编码处理** - 提供 `TextDecoder` 和 `TextEncoder` 类用于处理文本编码
- 📨 **参数解析** - `util.parseArgs()` 提供命令行参数解析功能，支持选项和位置参数
- 🎨 **文本样式** - `util.styleText()` 可为终端输出添加 ANSI 颜色和样式
- ⚡ **现代特性** - 包含 MIME 类型处理、差异比较、中止控制器等现代 JavaScript 功能

---

### [tinyglobby：现代化与性能优化的成功典范 | e18e](https://e18e.dev/blog/tinyglobby-migration.html)

**原文标题**: [tinyglobby: a success story in modernization and performance | e18e](https://e18e.dev/blog/tinyglobby-migration.html)

作者从 JavaScript 依赖管理问题出发，在优化 tsup 库时意外开启了对 glob 功能的深入研究，最终与社区共同开发出轻量级替代库 tinyglobby

- 🐛 作者因低配电脑安装依赖缓慢开始关注依赖膨胀问题
- 🔍 通过 e18e 社区学习优化方法，尝试用 fdir+picomatch 替换 globby
- ⚠️ 首次 PR 引发兼容性问题，促使专门开发 tinyglobby 库
- 📦 依赖包对比：tinyglobby 仅 3 个包/179KB，远少于 globby(24 包/637KB) 和 fast-glob(18 包/513KB)
- 🛡️ 更少依赖包显著降低供应链攻击风险（如 strip-ansi 事件）
- 🌐 已被 Vite、SWC、tsup 等主流构建工具和 React Router、SvelteKit 等框架采用
- 🚀 性能超越同类库，0.2.15 版速度提升 140%
- ✅ 具备 100+ 测试用例，活跃维护且文档完善
- 🙏 基于 fdir（最快目录遍历）和 picomatch（成熟 glob 实现）构建
- 👏 兼容部分 globby/fast-glob API，定位为轻量级替代方案

---

### [印尼大规模 TEA 窃取事件：剖析 NPM 垃圾邮件活动 | 博客 | Endor Labs](https://www.endorlabs.com/learn/the-great-indonesian-tea-theft-analyzing-a-npm-spam-campaign)

**原文标题**: [The Great Indonesian TEA Theft: Analyzing a NPM Spam Campaign | Blog | Endor Labs](https://www.endorlabs.com/learn/the-great-indonesian-tea-theft-analyzing-a-npm-spam-campaign)

文章概述了人工智能在现代社会中的广泛应用及其带来的影响。

- 🤖 人工智能技术已渗透到医疗、金融、教育等多个领域
- ⚡ 机器学习算法大幅提升了数据处理和模式识别效率  
- 🌐 自然语言处理技术推动了智能客服和翻译服务的发展
- ⚖️ 伦理规范和监管框架成为 AI 发展的重要议题
- 🔮 未来 AI 将与人类协同工作，创造新的就业形态

---

### [JavaScript 安全编码 - Stack Overflow](https://stackoverflow.blog/2025/10/15/secure-coding-in-javascript/)

**原文标题**: [Secure coding in JavaScript - Stack Overflow](https://stackoverflow.blog/2025/10/15/secure-coding-in-javascript/)

JavaScript 作为互联网前端核心技术，因其广泛使用而成为攻击者的主要目标。本文提出十项安全编码建议以增强 JavaScript 应用的安全性。

- 🎯 跨站脚本攻击是最常见的 JavaScript 安全威胁，需通过输入验证、输出编码和内容安全策略进行防范
- 🛡️ 选用具备自动输出编码功能的框架（如 React、Angular、Vue.js），并警惕危险函数的使用
- 📜 避免内联脚本，将 JavaScript 代码保存在独立外部文件中以提升安全性
- 🔒 启用严格模式编写更安全、规范的代码，预防潜在错误
- 🧰 利用开源安全工具（如 DomPurify、Retire.js、npm audit）进行代码检测和防护
- 📝 明确区分文本与可执行代码，使用 innerText/textContent 替代 innerHTML
- 🔧 仅将变量应用于安全静态属性，避免使用 onclick 等动态属性
- ⚙️ 在后端实施输入验证，防止请求被篡改
- 🚫 避免使用 eval()、document.write() 等危险函数处理用户数据
- 🔐 遵循安全开发生命周期，集成威胁建模、代码审查等安全实践

---

### [GitHub - SBoudrias/Inquirer.js：一套常见的交互式命令行用户界面集合。](https://github.com/SBoudrias/Inquirer.js)

**原文标题**: [GitHub - SBoudrias/Inquirer.js: A collection of common interactive command line user interfaces.](https://github.com/SBoudrias/Inquirer.js)

Inquirer.js 是一个用于构建交互式命令行界面的 JavaScript 工具库，提供多种常用提示组件和灵活的自定义功能。

- 📦 提供输入框、选择列表、复选框、密码框等常用命令行交互组件
- 🚀 支持通过 npm/yarn/pnpm/bun 快速安装使用
- ⚡ 全新重构版本，优化包体积和性能表现
- 🔧 支持自定义提示组件开发，提供完整 API 文档
- ⏰ 内置超时取消和异步控制功能
- 🎯 支持条件提问和答案对象化管理
- 🔄 提供社区扩展提示组件，如表格选择、文件选择器等
- 📝 兼容各种使用场景，包括 Git 钩子、脚本和 nodemon
- 🌐 可通过 npx 直接在 shell 脚本中使用
- 📄 采用 MIT 开源协议，拥有活跃的社区贡献

---

### [GitHub - sindresorhus/yoctocolors：互联网上最小最快的命令行着色包](https://github.com/sindresorhus/yoctocolors)

**原文标题**: [GitHub - sindresorhus/yoctocolors: The smallest and fastest command-line coloring package on the internet](https://github.com/sindresorhus/yoctocolors)

一个名为 yoctocolors 的极简命令行颜色包，具有最小体积和最快性能。

- 🌈 提供丰富的颜色和样式修饰功能，包括基本颜色、背景色和文本效果
- ⚡ 性能卓越，在同类库中速度领先，支持树摇优化
- 📦 无依赖、体积微小，支持 ESM 和 CommonJS 两种模块系统
- 🔧 支持嵌套颜色和强制颜色显示控制，兼容基础颜色检测
- 📄 采用 MIT 开源协议，持续维护更新
- 🏆 在 GitHub 上获得 836 个星标和 35 个分支，社区活跃度高

---

### [使用 Foxit API 从 JSON 生成动态 PDF - Foxit](https://developer-api.foxit.com/developer-blogs/use-cases-workflow-examples/automated-document-pipelines/generate-dynamic-pdfs-from-json-using-foxit-apis/?utm_source=cooperpress&utm_medium=Display&utm_campaign=11-18-25)

**原文标题**: [Generate Dynamic PDFs from JSON using Foxit APIs - Foxit](https://developer-api.foxit.com/developer-blogs/use-cases-workflow-examples/automated-document-pipelines/generate-dynamic-pdfs-from-json-using-foxit-apis/?utm_source=cooperpress&utm_medium=Display&utm_campaign=11-18-25)

在 API World 2025 大会上，Foxit 展示了如何通过其 API 构建可审计的 AI 驱动文档工作流程，包括现场演示的自动化系统实现过程。

- 🚀 通过 Foxit API 实现 AI 驱动的文档自动化系统
- 🤝 在 API World 2025 与开发者交流并展示应用案例
- 📄 结合 PDF 服务和文档生成 API 构建可审计工作流
- 🎤 现场演示了从简历生成到互动涂鸦的实际应用

---

### [GitHub - sindresorhus/globby：用户友好的全局模式匹配工具](https://github.com/sindresorhus/globby)

**原文标题**: [GitHub - sindresorhus/globby: User-friendly glob matching](https://github.com/sindresorhus/globby)

这是一个基于 fast-glob 的用户友好型 glob 匹配工具，提供扩展功能和易用 API

- 🚀 支持 Promise API 和多种匹配模式
- 📁 自动扩展目录并支持 .gitignore 忽略规则
- ⚡ 提供同步、异步和流式处理三种使用方式
- 🔧 支持路径转义和动态模式检测功能
- 📊 包含 Git 忽略检查等高级工具函数
- 🎯 兼容多种配置文件格式（ESLint/Prettier/Babel）
- 📦 采用 MIT 开源协议，被超过 2600 万项目使用

---

### [发布 v16.0.0 · sindresorhus/globby · GitHub](https://github.com/sindresorhus/globby/releases/tag/v16.0.0)

**原文标题**: [Release v16.0.0 · sindresorhus/globby · GitHub](https://github.com/sindresorhus/globby/releases/tag/v16.0.0)

这是一个名为"globby"的 GitHub 项目发布的 v16.0.0 版本更新内容

- 🚨 当启用 gitignore 选项时，现在会遵循父级.gitignore 文件的配置
- ✨ 新增支持仅包含否定模式的匹配规则
- 🔧 改进了错误提示信息，特别是针对无效 cwd 选项的情况
- 🐛 修复了启用 gitignore 选项时的性能问题
- 📦 解决了与打包工具的兼容性问题
- 🔍 优化了 isGitIgnored 函数的选项配置
- ⚡ 修复了父目录模式匹配和忽略模式的相关问题
- 📊 完善了 stats 选项的类型定义

---

### [GitHub - JCMais/node-libcurl：Node.js 的 libcurl 绑定库](https://github.com/JCMais/node-libcurl)

**原文标题**: [GitHub - JCMais/node-libcurl: libcurl bindings for Node.js](https://github.com/JCMais/node-libcurl)

这是一个用于 Node.js 的 libcurl 绑定库，提供快速且功能丰富的 URL 传输功能，支持多种协议和高级特性。

- 🌐 **支持多种协议** - 包括 HTTP、HTTPS、FTP、SMTP 等众多协议
- ⚡ **高性能传输** - 自称是 Node.js 中最快的 URL 传输库
- 🔧 **完整功能** - 支持 SSL 证书、代理、Cookie、认证等 libcurl 全部特性
- 📦 **预编译二进制** - 提供 Linux、macOS、Windows 的预编译版本
- 🎯 **TypeScript 支持** - 提供完整的类型定义
- 🔄 **多种安装方式** - 支持 npm、yarn、pnpm 安装
- 🛠️ **开发友好** - 提供详细的文档、示例代码和问题排查指南
- ⚠️ **环境要求** - 需要 libcurl 7.81.0 或更高版本，不支持浏览器环境
- 🔒 **安全可靠** - 提供企业级支持选项和安全策略
- 📚 **活跃社区** - 拥有详细的贡献指南和问题反馈渠道

---

### [libcurl - 您的网络传输库](https://curl.se/libcurl/)

**原文标题**: [libcurl - your network transfer library](https://curl.se/libcurl/)

libcurl 是一个免费易用的客户端 URL 传输库，支持数十种网络协议，具备 SSL 证书认证、多线程安全、IPv6 兼容等丰富功能，以其卓越的跨平台能力和稳定性成为全球应用最广泛的网络传输库。

- 🌐 支持 30+ 网络协议（HTTP/HTTPS/FTP/IMAP 等）及 HTTP/2/3
- 🔒 提供 SSL 加密、多种身份验证机制和代理隧道功能
- 📚 具备完整 C 语言 API 接口并严格保持 ABI 稳定性
- 🚀 以高性能、线程安全、IPv6 兼容为核心特性
- 💻 支持 50+ 操作系统平台（Windows/Linux/macOS 等）
- 🌍 被全球知名企业广泛采用且提供多语言绑定
- 📖 配备详尽文档教程和邮件列表技术支持
- ⬇️ 可通过官方下载页面获取最新版本

---

### [获取失败](https://nodeweekly.com/link/177152/web)

**原文标题**: [Failed to retrieve](https://nodeweekly.com/link/177152/web)

无法总结：获取内容失败，状态码 429。

---

### [自托管网站分析工具 | Ackee](https://ackee.electerious.com/)

**原文标题**: [Self-hosted website analytics | Ackee](https://ackee.electerious.com/)

overview summary
本文简要介绍了 Ackee 项目的核心资源导航，包含入门指南、技术文档和版本更新记录。

- 🚀 入门指南
- 📚 技术文档
- 📋 更新日志

---

### [发布 v3.0.0 · umami-software/umami · GitHub](https://github.com/umami-software/umami/releases/tag/v3.0.0)

**原文标题**: [Release v3.0.0 · umami-software/umami · GitHub](https://github.com/umami-software/umami/releases/tag/v3.0.0)

Umami v3.0.0 版本发布，带来全新界面、多项功能增强与改进，为应用未来发展奠定基础。

- 🎨 更新用户界面，导航栏支持快速查看网站内容与切换，报告页面独立便于访问
- 🔍 改进筛选功能，支持全局 URL 参数共享筛选条件，可同时编辑多个筛选器
- 📊 新增细分群组与同期群组功能，可保存筛选条件并分析用户留存行为
- 🔗 新增链接与像素追踪功能，分别用于监测点击量和嵌入外部内容流量
- ⚙️ 新增管理页面，支持查看和修改所有用户、网站及团队设置
- 🚧 预告看板功能将在下个版本推出，支持自定义数据仪表盘
- ⚠️ 不再支持 MySQL 数据库，仅保留 PostgreSQL，提供数据迁移指南
- 👥 感谢 15 位贡献者的代码提交与社区反馈

---

### [GitHub - electerious/Ackee：基于Node.js的自托管分析工具，专为注重隐私的用户设计。](https://github.com/electerious/Ackee)

**原文标题**: [GitHub - electerious/Ackee: Self-hosted, Node.js based analytics tool for those who care about privacy.](https://github.com/electerious/Ackee)

Ackee 是一款基于 Node.js 的自托管网站分析工具，专注于用户隐私保护，提供简洁的数据统计界面。

- 🛡️ 自托管隐私保护工具，无需收集用户个人数据即可提供网站流量分析
- 🚀 采用 Node.js 和 MongoDB 轻量级技术架构，支持多种部署方式
- 📊 提供最小化界面和 GraphQL API，支持自定义事件跟踪
- 🍪 无需使用 Cookie，避免触发 cookie 提示要求
- 🌐 拥有丰富的生态系统，支持多种框架和平台的集成插件
- 📄 采用 MIT 开源协议，目前获得 4.5k 星标和 383 个分支

---

### [标记文档](https://marked.js.org/)

**原文标题**: [Marked Documentation](https://marked.js.org/)

Marked 是一个高性能的 Markdown 编译器，支持多种 Markdown 规范，提供 CLI 和 JavaScript 使用方式，但需注意输出内容的安全过滤。

- ⚡ 专为速度设计的底层 Markdown 编译器，无缓存且非阻塞
- 📚 完整支持 Markdown、CommonMark 和 GitHub Flavored Markdown 规范
- 🌐 提供命令行工具、浏览器端和 Node.js 多种使用方式
- 🚨 输出 HTML 需自行过滤 XSS 攻击，推荐使用 DOMPurify 等工具
- ⚙️ 支持配置文件自定义选项，具备高度可配置性和扩展性
- 🔧 可处理特殊 Unicode 字符干扰，需注意零宽度字符清理
- 📊 被多个工具集成使用，如 zero-md、TeXMe 等单页面应用
- 🔒 重视安全问题，发现漏洞需通过指定渠道报告

---

### [发布 pnpm 10.22 · pnpm/pnpm · GitHub](https://github.com/pnpm/pnpm/releases/tag/v10.22.0)

**原文标题**: [Release pnpm 10.22 · pnpm/pnpm · GitHub](https://github.com/pnpm/pnpm/releases/tag/v10.22.0)

pnpm 10.22.0 版本发布，主要包含新功能添加和问题修复。

- 🔧 新增 trustPolicyExclude 配置支持，允许排除特定包或版本不受信任策略限制
- ⚙️ 发布时支持通过 publishConfig.engines 字段覆盖 engines 字段配置
- 🐛 修复多个 pnpm 进程同时硬链接目录内容时的崩溃问题
- 📦 版本号 v10.22.0，包含 95 次提交更新
- 👥 获得社区积极反馈，收到多种表情反应

---

### [MikroORM 6.6 | 微对象关系映射](https://mikro-orm.io/blog/mikro-orm-6-6-released)

**原文标题**: [MikroORM 6.6 | MikroORM](https://mikro-orm.io/blog/mikro-orm-6-6-released)

MikroORM 6.6 版本发布，重点增强了关系过滤器的配置灵活性，并扩展了实体生成器的功能，同时修复了先前版本中的问题。

- 🔧 关系过滤器现在支持在实体定义层级进行更精细的控制，可全局或按关系禁用过滤器，并支持设置默认参数
- 🚫 新增严格模式过滤器选项，用于处理可空关系场景（如租户过滤），丢弃不匹配的实体而非填充为 null
- 🔄 修复 select-in 策略下过滤器导致关系无法填充的问题，未初始化引用现会正确填充为 null
- 🛡️ 支持私有属性访问器配置，可通过 accessor 选项指定 ORM 直接使用后备属性或访问器方法
- 📝 实体生成器新增 defineEntity 定义方式，支持生成 InferEntity 类型和三种枚举模式（ts-enum/dictionary/union-type）
- 🗄️ 原生支持 PostgreSQL 枚举类型，生成独立文件供多实体复用
- 🔌 SQL 驱动增强 raw 助手，现支持 QueryBuilder 和 Knex.QueryBuilder 实例
- ⚡ 悲观锁自动跳过左连接关系，避免 PostgreSQL 等方言对可空关系加锁的限制

---

### [GitHub - openai/openai-node：OpenAI API 官方 JavaScript / TypeScript 库](https://github.com/openai/openai-node)

**原文标题**: [GitHub - openai/openai-node: Official JavaScript / TypeScript library for the OpenAI API](https://github.com/openai/openai-node)

这是 OpenAI 官方 JavaScript/TypeScript 库的 GitHub 仓库介绍，提供了访问 OpenAI REST API 的便捷方式。

- 📦 **官方库** - 这是 OpenAI 官方的 JavaScript/TypeScript 客户端库
- ⚡ **API 支持** - 支持 Responses API、Chat Completions API 和 Realtime API 等多种接口
- 🔄 **功能特性** - 包含流式响应、文件上传、Webhook 验证和自动分页等功能
- 🛠️ **安装方式** - 可通过 npm 安装或从 JSR 直接导入使用
- 🌐 **运行环境** - 支持 Node.js、Deno、Bun 和 Cloudflare Workers 等环境
- 🔒 **安全考虑** - 默认禁用浏览器支持以避免泄露 API 密钥
- 📚 **文档完善** - 提供详细的 API 文档、代码示例和迁移指南
- 🐛 **错误处理** - 内置完善的错误分类和重试机制
- ⚙️ **高级配置** - 支持超时设置、日志记录和自定义 fetch 客户端等

---

### [GPT-5.1：更智能、更会对话的 ChatGPT | OpenAI](https://openai.com/index/gpt-5-1/)

**原文标题**: [GPT-5.1: A smarter, more conversational ChatGPT | OpenAI](https://openai.com/index/gpt-5-1/)

OpenAI 发布 GPT-5.1 系列模型升级，包含更智能自然的对话体验和个性化设置优化，即日起向付费用户逐步推送。

- 🧠 GPT-5.1 Instant 模型默认更温暖智能，新增自适应推理能力，在数学编程任务中表现显著提升
- ⚡ GPT-5.1 Thinking 模型动态调整思考时间，复杂任务处理更深入，简单任务响应更迅速
- 🎭 新增六种对话风格预设（专业/直率/俏皮等），支持实时调整回复简洁度、温度等个性化参数
- 🔄 所有设置变更立即生效于全部对话，模型切换保留三个月过渡期供用户适应
- 🌐 API 服务将于本周内更新，企业版用户享有 7 天优先体验权限
- 📈 持续优化模型遵循用户指令的准确性，增强多轮对话一致性

---

### [ESLint v10.0.0-alpha.0 发布 - ESLint - 可插拔 JavaScript 代码检查工具](https://eslint.org/blog/2025/11/eslint-v10.0.0-alpha.0-released/)

**原文标题**: [ESLint v10.0.0-alpha.0 released - ESLint - Pluggable JavaScript Linter](https://eslint.org/blog/2025/11/eslint-v10.0.0-alpha.0-released/)

ESLint v10.0.0-alpha.0 作为主要版本发布，包含新功能、错误修复和多项重大变更，目前为预发布版本仅供测试反馈。

- 🚨 此为预发布版本，不建议用于生产环境，需通过指定标签安装
- 🔄 不再支持 Node.js v20.19.0 以下版本及 v21/v23，仅支持 v20.19.0+、v22.13.0+ 和 v24+
- 📁 配置文件查找逻辑更新，改为从被检测文件目录开始查找 eslint.config.*
- 🗑️ 完全移除 eslintrc 配置系统及相关环境变量、CLI 参数和文件支持
- ⚠️ 停止支持 jiti < v2.2.0 版本
- 📋 更新 eslint:recommended 配置，纳入新的重要规则
- 🔧 移除多个已弃用的 rule context 成员，需使用替代属性
- 🧪 删除 LintMessage#nodeType 和 TestCaseError#type 属性
- 🌐 Program AST 节点范围调整为覆盖整个源代码文本
- 🔭 要求自定义 ScopeManager 实现自动解析全局变量引用
- 📚 提供详细迁移指南协助升级适配

---

### [GitHub - dahlia/logtape：适用于Deno、Node.js、Bun、浏览器及边缘函数的零依赖简易日志库](https://github.com/dahlia/logtape)

**原文标题**: [GitHub - dahlia/logtape: Simple logging library with zero dependencies for Deno, Node.js, Bun, browsers, and edge functions](https://github.com/dahlia/logtape)

LogTape 是一个适用于 JavaScript 和 TypeScript 的轻量级日志库，具有零依赖、跨平台支持和结构化日志等特性。

- 🌱 **零依赖设计** - 无需担心依赖问题，可直接集成使用
- 🎯 **多环境支持** - 兼容 Deno、Node.js、Bun、浏览器和边缘函数
- 📊 **结构化日志** - 支持记录带结构化数据的日志消息
- 🏷️ **分层分类系统** - 通过层级分类管理记录器详细程度
- 📝 **模板字面量** - 支持使用模板字面量记录带占位符的日志
- 🔒 **数据脱敏功能** - 提供基于模式或字段的敏感信息脱敏能力
- 📦 **模块化包管理** - 通过 JSR 和 npm 提供核心包及多种适配器
- ⭐ **开源项目** - 获得 1.4k stars，采用 MIT 许可证

---

### [logtape/变更记录.md 位于主分支 · dahlia/logtape · GitHub](https://github.com/dahlia/logtape/blob/main/CHANGES.md#version-120)

**原文标题**: [logtape/CHANGES.md at main · dahlia/logtape · GitHub](https://github.com/dahlia/logtape/blob/main/CHANGES.md#version-120)

该页面为 GitHub 仓库界面，但内容加载出现异常。

- 🔄 页面加载时出现错误提示，需重新刷新
- 🔐 部分功能（如通知设置）需要登录才能操作
- 📊 仓库基础数据：获得 1.4k 星标、29 个复刻分支
- 🛠️ 项目管理板块包含代码、议题、拉取请求等常规功能
- ⚠️ 多个功能区（通知栏、安全分析）均显示加载异常
- 📱 页面提供额外的导航选项但功能受限

---

### [发布 12.2.0 版本 · timgit/pg-boss · GitHub](https://github.com/timgit/pg-boss/releases/tag/12.2.0)

**原文标题**: [Release 12.2.0 · timgit/pg-boss · GitHub](https://github.com/timgit/pg-boss/releases/tag/12.2.0)

pg-boss 项目发布了 12.2.0 版本更新，主要包含功能优化和问题修复

- 🔧 简化了 offWork 方法的重载形式，并新增 wait 选项支持等待工作器完成所有任务
- ⏱️ 新增 connectionTimeoutMillis 数据库配置项，默认超时时间设置为 10 秒
- 🐛 修复了 stop() 方法未能充分等待所有资源和计时器清理完成的问题
- 📋 完整更新日志可查看 12.1.1 到 12.2.0 版本的变更记录

---

### [GitHub - mercurius-js/mercurius：使用Fastify实现GraphQL服务器和网关](https://github.com/mercurius-js/mercurius)

**原文标题**: [GitHub - mercurius-js/mercurius: Implement GraphQL servers and gateways with Fastify](https://github.com/mercurius-js/mercurius)

Mercurius 是一个基于 Fastify 的 GraphQL 适配器，提供高性能的 GraphQL 服务器和网关实现。

- 🚀 支持查询解析和验证缓存，提升性能
- 🔄 自动加载器集成，避免 1+N 查询问题
- ⚡ 通过 graphql-jit 实现即时编译
- 📡 支持订阅功能和联邦架构
- 🌐 提供网关实现和批处理查询支持
- 🔧 可自定义持久化查询
- 📚 完善的文档和示例代码
- 🛡️ 采用 MIT 开源协议，由 NearForm 和 Platformatic 赞助开发

---

### [错误](https://nodeweekly.com/link/177166/web)

**原文标题**: [Error](https://nodeweekly.com/link/177166/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='nodeweekly.com', port=443): Max retries exceeded with url: /link/177166/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1000)')))

---

### [错误](https://nodeweekly.com/link/177167/web)

**原文标题**: [Error](https://nodeweekly.com/link/177167/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='nodeweekly.com', port=443): Max retries exceeded with url: /link/177167/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1000)')))

---

### [错误](https://nodeweekly.com/link/177168/web)

**原文标题**: [Error](https://nodeweekly.com/link/177168/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='nodeweekly.com', port=443): Max retries exceeded with url: /link/177168/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1000)')))

---

### [错误](https://nodeweekly.com/link/177169/web)

**原文标题**: [Error](https://nodeweekly.com/link/177169/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='nodeweekly.com', port=443): Max retries exceeded with url: /link/177169/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1000)')))

---

### [错误](https://nodeweekly.com/link/177170/web)

**原文标题**: [Error](https://nodeweekly.com/link/177170/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='nodeweekly.com', port=443): Max retries exceeded with url: /link/177170/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1000)')))

---

### [错误](https://nodeweekly.com/link/177171/web)

**原文标题**: [Error](https://nodeweekly.com/link/177171/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='nodeweekly.com', port=443): Max retries exceeded with url: /link/177171/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1000)')))

---

### [错误](https://nodeweekly.com/link/177172/web)

**原文标题**: [Error](https://nodeweekly.com/link/177172/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='nodeweekly.com', port=443): Max retries exceeded with url: /link/177172/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1000)')))

---

### [错误](https://nodeweekly.com/link/177173/web)

**原文标题**: [Error](https://nodeweekly.com/link/177173/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='nodeweekly.com', port=443): Max retries exceeded with url: /link/177173/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1000)')))

---

### [错误](https://nodeweekly.com/link/177174/web)

**原文标题**: [Error](https://nodeweekly.com/link/177174/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='nodeweekly.com', port=443): Max retries exceeded with url: /link/177174/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1000)')))

---

### [错误](https://nodeweekly.com/link/177175/web)

**原文标题**: [Error](https://nodeweekly.com/link/177175/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='nodeweekly.com', port=443): Max retries exceeded with url: /link/177175/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1000)')))

---

### [错误](https://nodeweekly.com/link/177176/web)

**原文标题**: [Error](https://nodeweekly.com/link/177176/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='nodeweekly.com', port=443): Max retries exceeded with url: /link/177176/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1000)')))

---

