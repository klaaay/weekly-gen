### [Node 周刊第 593 期：2025 年 9 月 16 日](https://nodeweekly.com/issues/593)

**原文标题**: [Node Weekly Issue 593: September 16, 2025](https://nodeweekly.com/issues/593)

本期通讯宣布下周停更，9 月 30 日恢复更新，重点内容包括 Node.js v24.8.0 支持 Chrome DevTools 调试 HTTP/2、pnpm 10.16 新增延迟依赖更新功能以防范恶意软件包，以及持续发生的 npm 供应链攻击事件。同时介绍了 Electron 38 版本升级、Express.js 5 生产环境配置指南，并推荐了多款开发工具更新。

- 🚨 npm 供应链攻击持续发生，最新事件影响@ctrl/tinycolor 等包，恶意载荷会窃取密钥令牌
- 🔧 Node.js v24.8.0 发布：新增 Chrome DevTools 对 HTTP/2 调用的调试支持，加密功能增强，npm 升级至 v11.6
- ⏰ pnpm 10.16 推出延迟依赖更新功能，可设置依赖包最低发布时间阈值避免安装快速撤回的恶意版本
- ⚡ Electron 38 升级至 Node 22.18，默认启用类型剥离功能，Chromium 从 138 升级至 140
- 📚 Express.js 5 生产环境配置教程发布，包含 TypeScript、ESLint、Prettier 和日志设置完整流程
- 🤖 多款开发工具更新：OpenAPI TypeScript 服务端代码生成器、终端图像显示工具 v4.0、jsdom 27.0 纯 JS DOM 实现等
- 🔍 Bun 项目深度解析包安装机制优化，Deno 2.5 支持权限组配置和测试功能改进
- 🌐 开发者实验性实现用一次性电子烟设备托管网站

---

### [Node.js](https://nodejs.org/en/blog/release/v24.8.0)

**原文标题**: [Node.js](https://nodejs.org/en/blog/release/v24.8.0)

Node.js v24.8.0 版本发布，主要新增了 HTTP/2 网络检查支持，并包含多项加密算法增强、性能优化和错误修复。

- 🔍 新增 Chrome DevTools 对 HTTP/2 网络调用的检查支持
- 🔐 加密模块新增 Ed448、ML-DSA、KMAC、Argon2 和 SLH-DSA 算法支持
- ⚙️ Worker 线程新增 CPU 性能分析 API
- 🛠️ 修复多个模块（fs、http、repl 等）的问题并优化性能
- 📦 更新了 npm 到 11.6.0 版本和多个依赖项
- 🌐 提供多平台（Windows、macOS、Linux 等）安装包和二进制文件下载

---

### [Node.js](https://nodejs.org/en/blog/release/v24.8.0#other-notable-changes)

**原文标题**: [Node.js](https://nodejs.org/en/blog/release/v24.8.0#other-notable-changes)

Node.js v24.8.0 版本发布，主要新增了 HTTP/2 网络检查支持，并增强了加密算法和 Web Cryptography API，同时包含多项性能优化和错误修复。

- 🔍 支持在 Chrome DevTools 中检查 HTTP/2 网络调用，需配合 `--experimental-network-inspection` 参数使用
- 🔐 加密模块新增对 Ed448、ML-DSA、KMAC、Argon2 和 SLH-DSA 算法的支持
- ⚙️ Worker 线程新增 CPU 性能分析 API
- 🛠️ 包含多项构建、文档、测试和工具链的更新与修复
- 📦 提供 Windows、macOS、Linux 等多平台安装包和二进制文件下载

---

### [pnpm 10.16 | pnpm](https://pnpm.io/blog/releases/10.16)

**原文标题**: [pnpm 10.16 | pnpm](https://pnpm.io/blog/releases/10.16)

pnpm 10.16 版本引入了新的安全设置和高级依赖搜索功能，同时修复了多个已知问题。

- 🛡️ 新增 minimumReleaseAge 设置，可延迟安装新发布的依赖包以降低安全风险
- 📋 支持通过 minimumReleaseAgeExclude 排除特定依赖包的延迟安装限制
- 🔍 新增 finder 函数功能，允许根据依赖包属性（如 peerDependencies）进行高级搜索
- 🖨️ finder 函数支持返回附加信息（如许可证）并在输出中显示
- ⚠️ 修复了 Node.js 24 下的弃用警告提示问题
- 🚫 现在要求 nodeVersion 必须设置为精确的 semver 版本
- 📦 改进了 pnpm publish 对.tar.gz 文件的支持
- ⌨️ 修复了 Ctrl-C 取消进程时 pnpm run 的退出码问题

---

### [npm 作者 Qix 因钓鱼邮件在重大供应链攻击中账号失陷](https://socket.dev/blog/npm-author-qix-compromised-in-major-supply-chain-attack)

**原文标题**: [npm Author Qix Compromised via Phishing Email in Major Suppl...](https://socket.dev/blog/npm-author-qix-compromised-in-major-supply-chain-attack)

Socket 发现多个 CrowdStrike npm 软件包遭恶意篡改，这是针对开源生态系统的持续性供应链攻击活动"Shai-Halud"的最新进展，此前已波及 Tinycolor 等 40 余个软件包。

- 🚨 持续供应链攻击活动"Shai-Halud"出现新变种
- 📦 多个 CrowdStrike 旗下 npm 软件包遭到入侵
- ⚠️ 攻击手法与先前入侵 Tinycolor 等 40 余个包的模式一致
- 🔍 Socket 安全团队率先检测到此次攻击活动
- 📅 最新攻击活动发生于 2025 年 9 月 16 日

---

### [获取失败](https://nodeweekly.com/link/174295/web)

**原文标题**: [Failed to retrieve](https://nodeweekly.com/link/174295/web)

无法总结：获取内容失败，状态码 403。

---

### [ctrl/tinycolor及40余个NPM包遭入侵 - StepSecurity 安全事件](https://www.stepsecurity.io/blog/ctrl-tinycolor-and-40-npm-packages-compromised)

**原文标题**: [ctrl/tinycolor and 40+ NPM Packages Compromised - StepSecurity](https://www.stepsecurity.io/blog/ctrl-tinycolor-and-40-npm-packages-compromised)

NPM 生态系统遭受名为"Shai-Hulud"的供应链攻击，涉及@ctrl/tinycolor 等 40 多个热门软件包，攻击者通过自我传播机制感染维护者的其他包，窃取云服务凭证并建立 GitHub Actions 后门。

- 🚨 攻击影响超过 40 个 NPM 包，包括每周下载量超 200 万的@ctrl/tinycolor
- 🔄 恶意软件具有自我传播功能，能自动感染维护者的其他包
- 🔍 使用 TruffleHog 工具扫描文件系统窃取 AWS/GCP/Azure 凭证
- ⚙️ 通过注入 GitHub Actions 工作流文件建立持久化后门
- 📤 将窃取的凭证数据上传到名为"Shai-Hulud"的公开 GitHub 仓库
- 🛡️ 主要针对 Linux/macOS 开发环境，刻意避开 Windows 系统
- 🔧 采用模块化设计，包含系统侦察、凭证收集和传播等多个功能模块
- ⚠️ 受影响用户需立即移除受感染包、轮换所有凭证并审计云基础设施

---

### [Electron 38.0.0 | Electron](https://www.electronjs.org/blog/electron-38-0)

**原文标题**: [Electron 38.0.0 | Electron](https://www.electronjs.org/blog/electron-38-0)

Electron 38.0.0 版本正式发布，包含 Chromium、V8 和 Node.js 的核心升级，新增多项功能并引入部分破坏性变更。

- 🚀 核心组件升级：Chromium 140.0.7339.41、V8 14.0、Node.js 22.18.0
- 🎨 新增系统强调色自定义和窗口边框高亮支持
- 💾 优化 macOS 内存信息查询和托盘图标持久化功能
- 🪟 新增跨进程窗口状态保存 API（Google Summer of Code 成果）
- ⚠️ 停止支持 macOS 11 系统，移除 ELECTRON_OZONE_PLATFORM_HINT 环境变量
- 🔌 移除 webContents 的 plugin-crashed 事件，弃用 routingId 相关接口
- 📅 Electron 35.x.y 版本已终止支持，建议升级至新版本

---

### [Node.js](https://nodejs.org/en/blog/release/v22.18.0/)

**原文标题**: [Node.js](https://nodejs.org/en/blog/release/v22.18.0/)

Node.js v22.18.0 LTS 版本发布，主要包含类型剥离功能默认启用、多项功能增强及错误修复。

- 🚀 默认启用类型剥离功能，无需额外配置即可直接运行 TypeScript 文件
- ⚠️ 该功能仍为实验性，可通过--no-experimental-strip-types 禁用
- 🔧 ESM 模块新增 import.meta.main 支持
- 📁 文件系统事件处理支持 AsyncIterator 异步迭代器
- 🛡️ 权限模型增强，支持 spawn 时传播权限标志
- 🗃️ SQLite 连接层新增 readBigInts 选项支持
- 🔗 新增 fileURLToPathBuffer API 用于 URL 路径转换
- 👀 监视模式增加--watch-kill-signal 终止信号标志
- 🧵 Worker 线程支持异步可销毁接口
- 📦 包含 npm 10.9.3 更新及多项依赖包版本升级

---

### [Node.js 手册，2025 年版](https://flaviocopes.com/the-nodejs-handbook-2025-edition/)

**原文标题**: [The Node.js Handbook, 2025 edition](https://flaviocopes.com/the-nodejs-handbook-2025-edition/)

《Node.js 手册》2025 版是一本面向初学者的全面指南，专注于 Node.js v22 LTS 的核心概念与实践应用，包含基础到进阶内容，强调原理理解与实战代码示例。

- 📘 手册最初发布于 2018 年，下载量数万次，曾作为 Node.js 官方文档基础
- 🎯 2025 版彻底重写，精简复杂内容，专注初学者友好性与实践性
- 📚 覆盖 40+ 主题：现代 JavaScript、内置 API、性能优化、安全实践及真实案例
- 🔧 详解核心模块（fs/path/os/http）、事件系统、流操作和加密功能
- ⚙️ 包含开发工具配置、环境变量管理、错误处理和测试方案
- 🌐 提供 HTTP 服务器搭建、网络编程及多线程（Worker Threads）等进阶内容
- 📥 可通过 https://flaviocopes.com/access/ 免费下载完整版

---

### [糟糕，又来了……关于 NPM 供应链攻击的思考 - 现代 Web 开发教程](https://tane.dev/2025/09/oh-no-not-again...-a-meditation-on-npm-supply-chain-attacks/)

**原文标题**: [Oh no, not again... a meditation on NPM supply chain attacks - Development tutorials for modern web development](https://tane.dev/2025/09/oh-no-not-again...-a-meditation-on-npm-supply-chain-attacks/)

文章概述了微软在软件供应链安全方面的失职，特别是 NPM 生态系统中的长期漏洞问题，作者结合历史案例和自身经验，指出微软缺乏对安全问题的重视，导致开发环境风险加剧，并呼吁行业重视供应链安全。

- 🚨 微软因长期忽视 NPM 安全漏洞而被视为威胁，类似 2000 年代浏览器垄断问题重现  
- 📦 NPM 已成为恶意软件传播的主要渠道，攻击目标从加密货币扩展到开发者密钥等关键资产  
- 🌐 作者回顾互联网早期历史，对比微软 IE 浏览器的安全缺陷与当前 NPM 问题的相似性  
- ⚠️ 2017 年作者曾通过 npx 工具演示过 postinstall 脚本的安全风险，但问题至今未解决  
- 💸 微软通过收购 GitHub 获得 NPM 控制权，虽保障了基础设施但未提升企业级安全措施  
- 🤖 当前依赖包仍无签名机制，AI 工具和脚本可轻易创建恶意仓库，2FA 认证也不足以防住攻击  
- 🔮 行业需协同建立默认安全的软件供应链，否则数据隐私风险将持续上升  
- 💡 建议企业重新评估开发工具安全性，避免客户与利益相关方面临潜在威胁

---

### [如何在 2025 年设置 Express 5 用于生产环境](https://www.reactsquad.io/blog/how-to-set-up-express-5-in-2025)

**原文标题**: [How To Set Up Express 5 For Production In 2025](https://www.reactsquad.io/blog/how-to-set-up-express-5-in-2025)

本文详细介绍了如何使用 TypeScript 设置 Express 5 生产环境应用，包括项目初始化、工具配置、测试驱动开发和完整 REST API 实现。

- 🚀 项目初始化与基础配置：创建项目目录、初始化 npm、配置 TypeScript 和模块设置
- 🛠️ 开发工具集成：设置 ESLint 和 Prettier 保证代码质量和一致性
- 🧪 测试环境搭建：配置 Vitest 和 Supertest 支持测试驱动开发
- 🔄 应用架构优化：分离服务器和应用逻辑，添加健康检查端点
- 📝 请求处理改进：创建异步处理包装器和日志中间件
- 🗂️ 功能模块组织：采用按功能分组的 MVC 模式结构
- 🔐 认证系统实现：JWT 令牌认证、密码哈希和 cookie 管理
- 🗃️ 数据库集成：使用 Prisma 与 PostgreSQL，创建数据门面模式
- 📊 数据验证：使用 Zod 验证查询参数和请求体
- 🧩 完整 CRUD 功能：实现用户配置文件的增删改查操作

---

### [桌面应用程序发布流程自动化 | DoltHub 博客](https://www.dolthub.com/blog/2025-09-11-automating-desktop-release-process/)

**原文标题**: [Automating the Release Process for a Desktop Application | DoltHub Blog](https://www.dolthub.com/blog/2025-09-11-automating-desktop-release-process/)

Dolt Workbench 团队通过 GitHub Actions 构建了自动化发布流水线，将原本需手动完成的六平台（Mac/Windows/Linux 等）应用打包流程简化为单按钮操作，实现了并行构建、版本管理及跨平台代码签名等功能的自动化。

- 🚀 通过 GitHub Actions 实现六平台并行构建，将原本耗时的手动流程压缩至单次触发
- 🔄 采用语义化版本管理，自动处理面向应用商店的单调递增构建版本号需求
- 📦 利用复合动作处理依赖安装和版本更新，确保构建环境可重现性
- 🔐 通过 API 自动下载证书和配置文件，解决 macOS 平台代码签名难题
- 🎯 保持可重试性设计：单平台构建失败时可独立重试，不影响其他平台
- 📮 最终生成版本 PR 自动合并，仅跳过 CI 的版本提交，避免测试流程冲突
- ⚡ 未来计划集成 Fastlane 实现应用商店自动上传，进一步完全自动化

---

### [dolt-workbench/.github/workflows 位于主分支 · dolthub/dolt-workbench · GitHub](https://github.com/dolthub/dolt-workbench/tree/main/.github/workflows)

**原文标题**: [dolt-workbench/.github/workflows at main · dolthub/dolt-workbench · GitHub](https://github.com/dolthub/dolt-workbench/tree/main/.github/workflows)

该页面显示 Dolt Workbench 项目在 GitHub 上的界面加载错误，需重新加载页面以访问完整功能。

- 🔄 页面加载时出现错误提示，建议用户重新刷新
- 🔐 通知设置需登录 GitHub 账户后方可调整
- 📊 项目数据概览：17 个分支、165 个星标、18 个议题、1 个拉取请求
- 🚫 安全模块和项目模块暂无可操作内容（显示 0）
- 📂 导航栏包含代码/议题/拉取请求/动作/项目/安全/洞察等标准 GitHub 功能分区

---

### [注册 - Auth0](https://auth0.com/signup?onboard_app=genai&ocid=7014z000001NyoxAAC-aPA4z0000008OZeGAM?utm_source=nodeweekly&utm_campaign=global_mult_mult_all_ciam-dev_dg-plg_auth_native_nodeweekly_newsletter_aud_NodeWeekly-Q3-Newsletter_utm2&utm_medium=cpc&utm_id=aNKKZ00000004Hz4AI)

**原文标题**: [Sign Up - Auth0](https://auth0.com/signup?onboard_app=genai&ocid=7014z000001NyoxAAC-aPA4z0000008OZeGAM?utm_source=nodeweekly&utm_campaign=global_mult_mult_all_ciam-dev_dg-plg_auth_native_nodeweekly_newsletter_aud_NodeWeekly-Q3-Newsletter_utm2&utm_medium=cpc&utm_id=aNKKZ00000004Hz4AI)

该内容是一个用户注册界面，包含基本信息填写、国家选择、服务条款同意及第三方登录选项，并介绍了 Auth for GenAI 的预览功能。

- 📧 需要填写邮箱和国家信息进行注册
- 🌍 提供全球国家/地区列表供选择  
- 📝 需同意服务条款和隐私政策  
- 🔐 支持 GitHub/Google/Microsoft 第三方账号快速登录  
- 🤖 宣传 Auth for GenAI 可安全实现用户认证、API 调用和文档获取功能  
- ©️ 页面底部显示 Okta 公司版权信息

---

### [如何控制 package.json | Val Town 博客](https://blog.val.town/gardening-dependencies)

**原文标题**: [How to keep package.json under control | Val Town Blog](https://blog.val.town/gardening-dependencies)

本文讨论了在复杂项目中如何有效管理 package.json 和依赖项，强调依赖管理的必要性和实用技巧。

- 📖 阅读新依赖的源码和文档，避免引入不必要的代码或安全风险
- 🔍 利用 npm ls 或 pnpm why 等工具分析依赖树，了解间接依赖并复用现有模块
- 📊 使用 Grand Perspective 或 rollup-plugin-visualizer 等工具分析包体积对开发和部署的影响
- ✅ 选择维护良好、有类型定义、测试完善的模块，避免使用已废弃或设计不匹配的依赖
- 🔄 用 Renovate 定期更新依赖，用 Knip 检测并删除未使用的模块
- 👥 关注优质模块作者（如 Sindre Sorhus、Rich Harris 等），积累可靠依赖来源
- 🌐 承认依赖不可避免，但需通过精细管理减少技术债务

---

### [Node.js 中 QUIC 协议现状 - Pavel Romanov 著 - Node Vibe](https://nodevibe.substack.com/p/state-of-quic-in-nodejs)

**原文标题**: [State of QUIC in Node.js - by Pavel Romanov - Node Vibe](https://nodevibe.substack.com/p/state-of-quic-in-nodejs)

Node.js 的 QUIC 实现历经六年延迟，主要因 OpenSSL 长期拒绝提供完整 QUIC 支持。随着 OpenSSL 3.5 发布关键 API，Node.js 25 计划于 2025 年 10 月首次集成 QUIC 协议。

- 🚧 QUIC 是基于 UDP 的传输层协议，旨在通过单次往返握手替代 TCP+TLS，提升连接效率
- ⚡ 协议特点包括 0-RTT 连接恢复和直接处理加密传输，但某些场景性能可能比 HTTP/2 低 45%
- 🔐 核心障碍是 OpenSSL 此前拒绝提供 QUIC 必需的 TLS 1.3 底层 API（密钥直取/记录层绕过）
- 📅 2018 年启动需求讨论，2019 年 James Snell 开始开发，但因依赖问题 2021 年 PR 被关闭
- 🛠️ 社区曾转向 OpenSSL 分支 quictls，最终 OpenSSL 3.5（2025 年 4 月）提供了关键支持
- 🎯 Node.js 25 计划 2025 年 10 月正式发布 QUIC 实现，比原计划延迟 4-5 年

---

### [使用 Node 18+ 原生测试运行器搭配 TypeScript 和 React - Matthew Brown](https://matthewbrown.io/2025/09/04/node-test-runner)

**原文标题**: [Using the node 18+ native test runner with TypeScript and React - Matthew Brown](https://matthewbrown.io/2025/09/04/node-test-runner)

Node.js 18+ 原生测试运行器支持 TypeScript 和 React，无需额外测试框架，通过配置脚本和依赖即可实现单元测试和组件测试。

- 🚀 Node.js 18 内置测试运行器，可替代 Jest/Mocha 等第三方框架
- ⚙️ 通过 package.json 脚本配置 TypeScript 编译、DOM 环境及实验性功能
- 📦 需安装@testing-library/react、global-jsdom 等开发依赖
- 🧪 使用 node:test 模块编写单元测试，搭配原生 assert 断言
- ⚛️ 结合 jsdom 与 React Testing Library 实现组件交互测试
- ▶️ 支持全量测试、监听模式及单文件运行
- ✅ 优势：零配置、原生 TypeScript 支持、依赖更轻量
- ⚠️ 限制：需 Node 18+、实验性功能依赖标志位、生态工具较少

---

### [获取失败](https://nodeweekly.com/link/174308/web)

**原文标题**: [Failed to retrieve](https://nodeweekly.com/link/174308/web)

无法总结：获取内容失败，状态码 415。

---

### [遇见 Feedsmith | Feedsmith](https://feedsmith.dev/)

**原文标题**: [Meet Feedsmith | Feedsmith](https://feedsmith.dev/)

Feedsmith 是一个快速、全能的 JavaScript 解析器和生成器，支持 RSS、Atom、RDF 和 JSON Feed 等主要格式，并提供智能命名空间处理和 OPML 文件支持。

- 🚀 全面支持所有主流 Feed 格式和命名空间
- 📦 保持原始 Feed 结构，便于数据访问
- 🔧 智能标准化自定义命名空间前缀
- ⚡ 解析和生成功能一体化，性能极速
- ♻️ 自动升级旧版元素到现代等效形式
- 🐪 不区分字段大小写，容错性强
- 🛡️ 基于 TypeScript 构建，提供完整类型安全
- 🌳 支持 Tree-shaking，减少打包体积
- ✅ 经过 2000+ 测试，代码覆盖率 99%
- 🌐 兼容 Node.js 和现代浏览器
- 📋 完整支持 RSS、Atom、JSON Feed 的解析和生成
- 🔗 支持多种命名空间包括 iTunes、Podcast、Media RSS 等
- 📊 相比其他库能更好地保留原始 Feed 结构信息

---

### [快速入门 | Feedsmith](https://feedsmith.dev/quick-start)

**原文标题**: [Quick Start | Feedsmith](https://feedsmith.dev/quick-start)

Feedsmith 是一个快速上手的 RSS/Atom/JSON Feed 解析和生成库，支持多种环境和格式，提供错误处理和详细 API 文档。

- 🚀 快速安装：支持 npm/yarn/pnpm/bun 安装或 CDN 引入，兼容 Node.js 和现代浏览器
- 🌐 通用解析：使用 parseFeed 函数自动识别 RSS/Atom/JSON/RDF 等多种订阅格式
- 🔧 格式专解：提供 parseRssFeed、parseAtomFeed 等特定格式解析方法
- 📋 OPML 支持：可解析 OPML 文件内容并提取订阅列表信息
- 🛠️ 生成功能：支持生成 RSS、Atom、JSON Feed 及 OPML 文件
- ⚠️ 错误处理：对无法识别或无效的 feed 内容会抛出描述性错误
- 📚 扩展学习：提供命名空间处理、API 参考和性能基准测试等进阶文档

---

### [GitHub - macieklamberski/feedsmith: 快速、全能的 RSS、Atom、RDF 和 JSON Feed 解析与生成器，支持播客、iTunes、Dublin Core 及 OPML 文件。](https://github.com/macieklamberski/feedsmith)

**原文标题**: [GitHub - macieklamberski/feedsmith: Fast, all-in-one parser and generator for RSS, Atom, RDF, and JSON Feed, with support for Podcast, iTunes, Dublin Core, and OPML files.](https://github.com/macieklamberski/feedsmith)

Feedsmith 是一个快速、全面的 JavaScript 库，用于解析和生成多种 Feed 格式，支持 RSS、Atom、RDF、JSON Feed 及 OPML 文件，具有高性能、类型安全和智能处理特性。

- 🎯 支持所有主流 Feed 格式和命名空间，包括 Podcast、iTunes 和 Dublin Core
- 📦 解析时保持原始 Feed 结构，便于数据访问
- 🧠 智能处理命名空间，规范化自定义前缀为标准格式
- ⚡ 超快速解析性能，是 JavaScript 中最快的 Feed 解析器之一
- 🛟 完全使用 TypeScript 构建，提供完整的类型定义
- 🐍 不区分大小写，优雅处理格式错误或不完整的 Feed
- 🔩 支持解析和生成功能，可用于读取和创建 Feed
- 📖 包含超过 2000 个测试，代码覆盖率达 99%

---

### [GitHub - sindresorhus/trash：将文件和目录移至回收站](https://github.com/sindresorhus/trash)

**原文标题**: [GitHub - sindresorhus/trash: Move files and directories to the trash](https://github.com/sindresorhus/trash)

这是一个名为“trash”的开源 Node.js 模块，用于安全地将文件和目录移至回收站而非永久删除，支持 macOS、Windows 和 Linux 系统。

- 🗑️ 提供比永久删除更安全的文件删除方式，支持跨平台操作
- 🌍 兼容 macOS（10.12+）、Windows（8+）和 Linux（但 Linux 支持较弱且需要维护）
- 📦 可通过 npm 安装，支持 Promise API 和 glob 模式匹配
- ⚠️ 特别说明 Windows 服务账户下的特殊回收行为和 Linux 需要维护协助
- 🔄 包含 CLI 工具和相关生态模块（如 trash-cli 和 empty-trash）
- 📄 采用 MIT 许可证，拥有 2.6k 星标和 79 个 fork

---

### [GitHub - jasonblanchard/openapi-typescript-server：基于OpenAPI生成TypeScript服务器的代码生成工具](https://github.com/jasonblanchard/openapi-typescript-server)

**原文标题**: [GitHub - jasonblanchard/openapi-typescript-server: Codegen TypeScript servers from OpenAPI](https://github.com/jasonblanchard/openapi-typescript-server)

这是一个基于 OpenAPI 规范生成 TypeScript 服务器接口的工具，通过代码生成确保服务器实现与 API 文档保持类型安全同步。

- 🛠️ 支持从 OpenAPI 3.0 和 3.1 规范生成服务器实现代码
- 🚀 框架无关设计，提供 Express 适配器
- 📦 运行时占用极小，依赖外部中间件进行验证
- ⚠️ 目前处于早期开发阶段，API 可能不稳定
- 🔄 修改 OpenAPI 规范后重新生成代码，TypeScript 会提示需要调整的实现
- 🎯 设计目标是通过代码生成减少运行时复杂性，保持轻量级
- ❌ 不处理模式验证、类型强制、安全认证和 Webhook 功能
- 🔧 提供错误处理和底层请求/响应对象访问机制

---

### [GitHub - sindresorhus/ow：人性化的函数参数验证工具](https://github.com/sindresorhus/ow)

**原文标题**: [GitHub - sindresorhus/ow: Function argument validation for humans](https://github.com/sindresorhus/ow)

ow 是一个用于函数参数验证的 JavaScript 库，提供直观的链式 API 和丰富的验证功能，专为提升开发体验设计。

- 🚀 提供表达性链式 API 和多种内置验证类型
- 🛠️ 支持自定义验证和自动标签推断（Node.js 环境）
- 📦 使用 TypeScript 开发，包含类型守卫和类型推断功能
- ⚡ 提供开发专用版本（ow/dev-only）以减少生产环境体积
- 🔧 可创建可复用验证器，并支持自定义错误消息
- 📊 包含性能优化建议（如显式指定标签提升性能）

---

### [GitHub - sindresorhus/terminal-image：在终端中显示图像](https://github.com/sindresorhus/terminal-image)

**原文标题**: [GitHub - sindresorhus/terminal-image: Display images in the terminal](https://github.com/sindresorhus/terminal-image)

这是一个用于在终端中显示图像的 Node.js 库，支持多种终端协议和图像格式。

- 🖼️ 支持在终端中显示 PNG、JPEG 和 GIF 图像
- 🖥️ 自动选择最佳显示协议：Kitty 图形协议、iTerm2 内联图像协议或 ANSI 块字符
- ⚙️ 可自定义图像尺寸，支持百分比或具体行列数设置
- 🔄 默认保持宽高比，也可选择不保持
- 📦 通过 npm 安装，提供 buffer 和 file 两种调用方式
- 🌟 拥有 1k 星标和 28 个分支，采用 MIT 许可证
- 📊 被 25.7k+ 项目使用，100% JavaScript 编写

---

### [小猫](https://sw.kovidgoyal.net/kitty/)

**原文标题**: [kitty](https://sw.kovidgoyal.net/kitty/)

kitty 是一款基于 GPU 的快速、功能丰富的终端模拟器，提供高性能、可扩展性和跨平台支持，通过创新技术提升终端体验。

- 🚀 采用 GPU 和 SIMD 向量指令实现顶级性能，支持线程渲染以最小化延迟
- 🎨 支持图形显示（图像/动画）、连字、表情符号和可变字体等高级排版功能
- 🔗 可配置超链接操作，支持从脚本或 shell 进行远程控制
- 🐍 通过 Python kittens 扩展功能，支持启动会话定义工作环境
- 🪟 提供可编程标签页、分割窗口和多布局管理，支持完整历史浏览
- 🌐 支持 SSH 会话中直接编辑/下载远程文件，兼容 Linux/macOS/BSD 系统
- 💡 首创终端图形协议和键盘处理方案，推动终端生态系统发展
- ⏯️ 提供快速入门指南和视频演示（包含分时段功能讲解：分页查看、文件操作、图像显示等）

---

### [发布 v4.0.0 · JS-DevTools/npm-publish · GitHub](https://github.com/JS-DevTools/npm-publish/releases/tag/v4.0.0)

**原文标题**: [Release v4.0.0 · JS-DevTools/npm-publish · GitHub](https://github.com/JS-DevTools/npm-publish/releases/tag/v4.0.0)

该存储库是一个用于 npm 包发布的 GitHub Action 工具，最新 v4.0.0 版本升级了运行环境并引入了重大变更。

- 🚀 版本升级至 v4.0.0，运行时环境更新为 Node 24 和 npm 11
- ⚠️ 重大变更：仅支持 Node≥20 环境，不再兼容 Node 16/18版本
- 📦 代码模块格式全面转为 ESM 规范
- 🔧 新增 Windows 系统下 npm CLI 的兼容支持
- 🐛 修复了 npm≥10 版本的模拟发布和冲突检测逻辑
- 📌 官方推荐使用固定版本号（@v4.0.0）确保安全性
- 🔒 启用不可变发布机制，仅允许修改版本说明标题和内容

---

### [发布版本 27.0.0 · jsdom/jsdom · GitHub](https://github.com/jsdom/jsdom/releases/tag/27.0.0)

**原文标题**: [Release Version 27.0.0 · jsdom/jsdom · GitHub](https://github.com/jsdom/jsdom/releases/tag/27.0.0)

jsdom 27.0.0 版本发布，主要更新包括最低 Node.js 版本要求提升至 v20、新增多个事件构造函数、改进虚拟控制台功能、更换 CSS 选择器引擎以及修复多项规范符合性问题。

- 🚀 最低 Node.js 版本要求提升至 v20
- ✨ 新增 BeforeUnloadEvent 等 7 个事件构造函数
- 🖱️ 为 MouseEvent 添加 movementX 和 movementY 属性
- 🔧 虚拟控制台功能优化：重命名 sendTo() 为 forwardTo()，改进错误处理机制
- 🐛 更换 CSS 选择器引擎，修复 20 多个选择器相关 bug
- 🍪 升级 tough-cookie，localhost 现在被视为安全上下文
- 💅 更新用户代理样式表，改为基于 HTML 标准
- ⚡ element.click() 现在触发 PointerEvent 而非 MouseEvent
- 🔄 修复 Window 对象规范符合性问题和 ElementInternals 可访问性 getter/setter
- 📝 包含多项 CSS 解析和样式解析的修复改进

---

### [GitHub - dahlia/logtape：适用于Deno、Node.js、Bun、浏览器及边缘函数的零依赖简易日志库](https://github.com/dahlia/logtape)

**原文标题**: [GitHub - dahlia/logtape: Simple logging library with zero dependencies for Deno, Node.js, Bun, browsers, and edge functions](https://github.com/dahlia/logtape)

LogTape 是一个适用于 JavaScript 和 TypeScript 的轻量级日志库，具有零依赖、跨运行时支持和结构化日志等特性。

- 🌟 零依赖设计，无需担心依赖问题
- 📚 支持库和应用使用，提供灵活的日志能力
- 🌐 跨运行时支持 Deno、Node.js、Bun、浏览器和边缘函数
- 🧱 支持结构化日志和分层类别管理
- 📝 提供模板字面量和内置数据脱敏功能
- 📦 可通过 JSR 和 npm 安装，支持多种包管理器
- 🔌 提供多种适配器和接收器，如 Pino、Sentry 和 OpenTelemetry 等

---

### [logtape/CHANGES.md 位于 main · dahlia/logtape · GitHub](https://github.com/dahlia/logtape/blob/main/CHANGES.md#version-110)

**原文标题**: [logtape/CHANGES.md at main · dahlia/logtape · GitHub](https://github.com/dahlia/logtape/blob/main/CHANGES.md#version-110)

该页面显示 GitHub 仓库"dahlia/logtape"的界面加载错误提示及基础项目数据。  
- ⚠️ 页面加载异常，需重新刷新  
- 🔐 用户需登录方可调整通知设置  
- 🍴 项目被复刻 26 次  
- ⭐ 获得 1.3k 星标收藏  
- 🐛 存在 6 个未处理议题  
- 🔀 有 6 个拉取请求待处理  
- 📊 提供 Actions/Insights 等高级功能入口

---

### [Node.js Undici v7.16.0 版本发布 · GitHub](https://github.com/nodejs/undici/releases/tag/v7.16.0)

**原文标题**: [Release v7.16.0 · nodejs/undici · GitHub](https://github.com/nodejs/undici/releases/tag/v7.16.0)

Node.js 的 Undici 库发布了 v7.16.0 版本，包含性能优化、错误修复和新功能改进。

- 🚀 使用 OIDC 替代 npm token 提升安全性
- ⚡ 将多个异步方法改为同步执行以提升性能（如 fetch、client.connect）
- 🐛 修复 HTTP2 cookie 支持和 IP 地址验证等问题
- 🔧 改进测试套件稳定性和跨平台兼容性
- 🌐 新增对 Agent 中源数量限制的支持功能
- 📦 包含依赖项更新和代码重构优化
- 👋 迎来 3 位新贡献者的首次代码提交

---

### [GitHub - hexojs/hexo：基于 Node.js 的快速、简洁且强大的博客框架](https://github.com/hexojs/hexo)

**原文标题**: [GitHub - hexojs/hexo: A fast, simple & powerful blog framework, powered by Node.js.](https://github.com/hexojs/hexo)

Hexo 是一个基于 Node.js 的快速、简洁且强大的博客框架，支持多种部署方式和丰富的扩展功能。

- 🚀 快速生成静态文件，支持 GitHub 风格的 Markdown 和 Octopress 插件
- 🌐 一键部署到 GitHub Pages、Heroku 等平台，提供强大的 API 扩展能力
- 📦 拥有数百个主题和插件，可通过 npm 或 Homebrew 快速安装
- 📖 提供详细文档、故障排除和社区支持（Google Group、Discord 等）
- 🤝 采用 MIT 许可证，欢迎贡献代码，已有 178 位贡献者和 40.8k 星标

---

### [GitHub - vpulim/node-soap: Node.js 的 SOAP 客户端与服务器](https://github.com/vpulim/node-soap)

**原文标题**: [GitHub - vpulim/node-soap: A SOAP client and server for node.js.](https://github.com/vpulim/node-soap)

node-soap 是一个用于 Node.js 的 SOAP 客户端和服务器库，支持创建和调用基于 WSDL 的 Web 服务，提供丰富的 API 和配置选项。

- 🚀 支持 SOAP 客户端和服务器功能，兼容 RPC 和 Document 类型的架构
- 🔧 提供同步和异步方法处理，支持 Express 服务器集成
- 🔐 内置多种安全协议，如 WS-Security、BasicAuth、SSL 等
- 📦 可通过 npm 安装，采用 MIT 许可证，社区活跃且有持续维护
- ⚙️ 支持自定义 XML 处理、消息日志、错误处理和头部管理
- 🌐 能够处理本地或远程 WSDL 文件，支持 MTOM 附件和流式响应
- 🧪 包含单元测试工具 soap-stub，便于模拟和测试 SOAP 调用

---

### [编程未来特卖 | Frontend Masters](https://frontendmasters.com/sale/?utm_source=classified&utm_medium=referral&utm_campaign=nodeweekly)

**原文标题**: [The Future of Coding Sale | Frontend Masters](https://frontendmasters.com/sale/?utm_source=classified&utm_medium=referral&utm_campaign=nodeweekly)

前端大师年度会员优惠，现价$290（原价$390），可节省$100。会员可获取 250+ 优质课程、多级别学习路径、移动端离线播放、实时研讨会问答、Discord 社区及全球课程搜索功能，相比月费节省$178。

- 🎯 年度会员特惠 $290（原价$390）立省$100
- 🚀 从中级到高级开发者的加速成长路径  
- 📚 250+ 精品课程与个性化学习路径
- 📱 支持离线播放的移动端应用
- 💬 实时研讨会互动问答功能
- 🌐 全新全球课程搜索引擎
- 👥 Discord 社区及个人学习档案
- 💰 较月费节省$178

---

### [编程未来特卖 | Frontend Masters](https://frontendmasters.com/sale/?utm_source=classified&utm_medium=referral&utm_campaign=nodeweekly)

**原文标题**: [The Future of Coding Sale | Frontend Masters](https://frontendmasters.com/sale/?utm_source=classified&utm_medium=referral&utm_campaign=nodeweekly)

年度会员优惠价 290 美元，原价 390 美元，帮助中级开发者快速晋升为高级开发者。会员可享受 250 多门优质课程、各技能级别学习路径、移动端离线播放、实时研讨会问答、Discord 社区访问及个人学习档案，新增全局与课程搜索功能。相比月费节省 178 美元，比正常年费优惠 100 美元。

- 💰 年度会员优惠：290 美元（原价 390 美元）
- 🚀 助力职业发展：从中级到高级开发者的加速路径
- 📚 海量课程资源：250+ 优质课程覆盖各技能等级
- 📱 移动学习支持：离线播放功能
- 💬 互动学习体验：实时研讨会问答+Discord 社区
- 🔍 智能搜索系统：新增全局与课程搜索功能
- ⭐ 超值节省：比月费省 178 美元/比年费省 100 美元

---

### [开始使用 Redis](https://redis.io/lp/get-started2/?utm_source=cooper-press&utm_medium=cpa&utm_campaign=2025-08-app_performance-node-weekly-2&utm_content=cloud_-_redis_cloud_users)

**原文标题**: [Get started with Redis](https://redis.io/lp/get-started2/?utm_source=cooper-press&utm_medium=cpa&utm_campaign=2025-08-app_performance-node-weekly-2&utm_content=cloud_-_redis_cloud_users)

Redis 是一个专注于高速数据处理的技术平台，提供云端和本地解决方案，帮助开发团队快速构建高性能应用程序。

- 🚀 全球最快的数据平台，支持向量数据库、缓存和 NoSQL 数据库，适用于各种环境
- 🧠 先进的向量数据库助力构建高效可靠的生成式 AI 应用
- ⚡ 内存键值存储支持多种数据结构，优化实时应用性能
- 🌩️ 通过 Redis Cloud 轻松创建和管理数据库，支持从实验到生产环境的无缝扩展
- 💻 提供开发者中心、多语言支持和专业架构师与 DevOps 资源
- 🆓 提供免费试用选项，方便快速开始构建项目

---

### [开始使用 Redis](https://redis.io/lp/get-started2/?utm_source=cooper-press&utm_medium=cpa&utm_campaign=2025-08-app_performance-node-weekly-2&utm_content=cloud_-_redis_cloud_users%20)

**原文标题**: [Get started with Redis](https://redis.io/lp/get-started2/?utm_source=cooper-press&utm_medium=cpa&utm_campaign=2025-08-app_performance-node-weekly-2&utm_content=cloud_-_redis_cloud_users%20)

Redis 是一个高速数据平台，提供云端和本地解决方案，帮助团队快速构建应用程序，支持向量数据库、缓存和 NoSQL 数据库等多种数据技术。

- 🚀 全球最快的数据平台，提供云端和本地解决方案，助力快速开发应用
- 🗄️ 支持向量数据库、缓存系统、NoSQL 数据库等多种数据技术
- ⚡ 内存键值存储设计，专为实时应用提供高效支持
- 🌐 提供免费试用和开发者资源，支持多种编程语言开发
- 📈 支持从实验到生产环境的无缝扩展，特别适合 AI 应用开发

---

### [Bun 安装幕后花絮 | Bun 博客](https://bun.com/blog/behind-the-scenes-of-bun-install)

**原文标题**: [Behind The Scenes of Bun Install | Bun Blog](https://bun.com/blog/behind-the-scenes-of-bun-install)

Bun 包管理器通过系统级优化显著提升安装速度，平均比 npm 快 7 倍、比 pnpm 快 4 倍、比 yarn 快 17 倍，尤其在大代码库中效果更明显。其核心突破在于将包安装视为系统编程问题而非 JavaScript 问题，通过最小化系统调用、二进制缓存清单、优化压缩包解压、利用原生文件复制和多核并行等技术实现性能飞跃。

- 🚀 **极速安装性能**：Bun 安装速度远超主流包管理器，大幅减少大型项目的依赖安装时间。
- ⚙️ **系统调用优化**：通过直接系统调用（Zig 语言实现）避免 Node.js 线程池和事件循环开销，减少模式切换（每次节省 1000-1500 CPU 周期）。
- 📦 **二进制清单缓存**：将 JSON 格式的包元数据转换为二进制存储，消除重复解析开销，缓存安装比 npm 快 39 倍。
- 🗜️ **高效压缩包处理**：预分配内存并利用 libdeflate 快速解压，避免传统流式解压中的多次数据复制。
- 🧠 **缓存友好数据布局**：采用结构数组（SoA）替代对象数组（AoS），提升 CPU 缓存命中率，减少内存访问延迟。
- 🔗 **智能文件复制策略**：根据不同操作系统使用原生优化（如 macOS 的 clonefile、Linux 的硬链接），减少系统调用和磁盘写入。
- ⚡ **多核并行处理**：基于工作窃取的线程池充分利用多核 CPU，并行处理网络请求、解压和依赖解析。
- 🌐 **异步 DNS 解析**：在 macOS 上使用原生异步 API 提前解析域名，避免线程阻塞。
- 🔒 **优化锁文件格式**：采用线性存储结构加速锁文件解析，避免传统 JSON 嵌套解析的性能瓶颈。
- 📊 **硬件适配设计**：针对现代 SSD、多核 CPU 和大内存环境重新设计，解决系统调用而非 I/O 等待的核心瓶颈。

---

### [Bun — 一款快速的全能 JavaScript 运行时](https://bun.sh/)

**原文标题**: [Bun — A fast all-in-one JavaScript runtime](https://bun.sh/)

Bun v1.2.22 是一个高性能的 JavaScript 全栈工具包，集成了运行时、打包器、测试运行器和包管理器，专注于速度和 Node.js 兼容性。

- 🚀 Bun 在 HTTP 请求性能测试中表现卓越，每秒处理 59,026 个请求，远超 Deno 和 Node.js
- 🌐 WebSocket 服务器性能突出，每秒发送 2,536,227 条消息，性能是 Deno 的近两倍
- 📊 数据库查询性能优异，每秒处理 50,251 次查询，大幅领先 Node.js 和 Deno
- 🔧 提供一体化开发解决方案，支持 JavaScript 和 TypeScript 项目的开发、测试、运行和打包
- ⚡ 专为速度优化设计，同时保持与 Node.js 的 100% 兼容性
- 📦 内置包管理器，支持 Linux、macOS 和 Windows 系统的一键安装

---

### [Deno 2.5：配置文件中的权限设置 | Deno](https://deno.com/blog/v2.5)

**原文标题**: [Deno 2.5: Permissions in the config file | Deno](https://deno.com/blog/v2.5)

Deno 2.5 版本引入了多项新功能和改进，包括权限配置文件管理、测试 API 增强、WebSocket 自定义标头支持、运行时打包 API、HTML 入口点打包、权限审计日志、任务列表显示优化、子进程输出简化、格式化一致性提升、依赖管理改进、Node.js 全局 API 兼容性、环境变量监听、TCP 连接队列设置、TypeScript 配置兼容性增强以及多项性能优化。

- 🔐 权限配置文件支持：可在 deno.json 中预定义权限集，通过 -P 标志快速应用不同场景的权限配置
- 🧪 测试增强 API：新增 beforeAll、beforeEach、afterAll、afterEach 钩子函数，简化测试环境的设置与清理
- 🌐 WebSocket 自定义标头：支持在建立 WebSocket 连接时添加认证和元数据标头，提升握手阶段的安全性
- 📦 运行时打包 API：提供 Deno.bundle() 编程接口，支持以代码方式打包 JavaScript 和 TypeScript 项目
- 📄 HTML 入口点打包：deno bundle 现在支持直接处理 HTML 文件，自动打包并更新引用的脚本和样式文件
- 📋 权限审计日志：通过 DENO_AUDIT_PERMISSIONS 环境变量生成权限使用记录的 JSONL 格式日志
- 📋 任务列表显示：运行 deno run 无参数时显示所有可用任务和脚本，提升命令行使用体验
- 🔧 子进程输出简化：为 Deno.ChildProcess 的 stdout/stderr 添加便捷方法（text()、json() 等），简化输出处理
- 🎨 格式化一致性：deno fmt 现在对 import/export 语句的花括号空格处理与属性声明保持一致
- 📦 依赖管理改进：优化 deno install 输出格式，增加版本号检查 lint 规则，禁止未版本化的导入
- ⏰ Node.js 定时器兼容：通过 --unstable-node-globals 标志使用 Node.js 风格的 setTimeout/setInterval API
- 🔄 环境变量监听：结合 --watch 和 --env-file 标志，环境文件修改时自动重新加载变量
- 🚀 TCP 连接队列设置：Deno.serve 新增 tcpBacklog 参数，支持自定义待处理连接队列大小
- 🔧 TypeScript 配置兼容：新增对 compilerOptions.rootDirs 和 "bundler" moduleResolution 的支持，提升框架兼容性
- ⚡ 性能优化：包括发射缓存优化、CommonJS 包装效率提升、JSX 条件编译、structuredClone 加速等多项改进
- 🔗 其他特性：包括禁用 TLS 主机名验证、Unix 套接字代理支持、LSP 拉取诊断、Node.js 异步钩子增强等
- 🚀 引擎升级：集成 V8 14.0 和 TypeScript 5.9.2，带来新的语言特性和性能提升

---

### [哪个 npm 包的版本号最大？](https://adamhl.dev/blog/largest-number-in-npm-package/)

**原文标题**: [Which npm package has the largest version number?](https://adamhl.dev/blog/largest-number-in-npm-package/)

作者通过分析 npm 注册表中 360 多万个包，发现版本号最大的包是 latentflip-test（版本号达 1000000000000000000.1000000000000000000.1000000000000000000），但该版本号并不符合实际语义版本规范。经过筛选遵循语义版本且版本号有实际意义的包后，最终胜出的是 all-the-package-names 包的 1.3905.0 版本。

- 🚀 作者发现 AWS SDK JavaScript 版本 v3.888.0 后，决定研究 npm 中版本号最大的包
- 🔍 通过 CouchDB 的复制 API 获取了 360 多万个包的信息，耗时约 12 小时
- 📊 分析显示许多高版本号包因自动化配置错误导致（如 GitHub Action 循环发布）
- 🏆 实际遵循语义版本且版本号最大的包是 all-the-package-names@1.3905.0
- ⚡ 使用 Bun 和 TypeScript 编写脚本处理数据，最终生成 886MB 的结果文件

---

### [在一次性电子烟上托管网站 :: BogdanTheGeek 的博客](https://bogdanthegeek.github.io/blog/projects/vapeserver/)

**原文标题**: [Hosting a WebSite on a Disposable Vape :: BogdanTheGeek's Blog](https://bogdanthegeek.github.io/blog/projects/vapeserver/)

作者利用从一次性电子烟中回收的 PY32 微控制器，成功运行了一个基于 ARM Cortex-M0+ 的 Web 服务器，通过半主机和 SLIP 协议实现网络连接，并优化传输性能使其达到 160 毫秒的页面加载速度。

- 🚬 作者收集废弃电子烟，发现内置 PUYA PY32 系列微控制器（24MHz Cortex-M0+、24KB 闪存、3KB RAM）
- 🔧 通过半主机 (semihosting) 调试技术和 SLIP 串行协议，将微控制器模拟为网络设备接入 TCP/IP 网络
- 🌐 移植 uIP 轻量级网络协议栈并搭建 HTTP 服务器，初期存在内存对齐问题和传输性能瓶颈（20 秒加载页面）
- ⚡ 通过添加环形缓冲区和批量写入优化，将页面加载时间缩短至 160ms，ping 延迟降至 20ms 且零丢包
- 💾 最终占用 FLASH 5.1KB(20.8%) 和 RAM 1.4KB(44.9%)，剩余空间可托管完整博客内容并支持动态 API 接口
- 📁 项目开源并提供代码资源，同时发现同类芯片可被识别为 PY32C642 型号

---

