### [错误](https://nodeweekly.com/link/176498/web)

**原文标题**: [Error](https://nodeweekly.com/link/176498/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='nodeweekly.com', port=443): Max retries exceeded with url: /link/176498/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1000)')))

---

### [Node.js — Node.js v22 至 v24 版本](https://nodejs.org/en/blog/migrations/v22-to-v24)

**原文标题**: [Node.js — Node.js v22 to v24](https://nodejs.org/en/blog/migrations/v22-to-v24)

本文介绍了从 Node.js v22 迁移到 v24 的部分内容，用户态迁移团队正在开发更多代码修改工具以协助迁移。Node.js 24.11.0 已进入长期支持阶段，支持将持续到 2028 年 4 月。迁移时需注意平台支持变更、破坏性变化及构建要求。

- 🚫 停止支持 32 位 Windows(x86) 和 32 位 Linux(armv7) 预构建二进制文件
- 🔐 OpenSSL 3.5 默认安全级别提升至 2，禁止使用弱密钥和 RC4 密码套件
- ⚠️ 行为变更包括更严格的 fetch 规范、AbortSignal 验证和流错误处理
- 🔧 C++ 插件需适配 V8 13.6，建议优先使用 N-API
- 🛠️ 源码构建要求 gcc 12.2 或 Xcode 16.1 以上版本
- 🔄 提供 6 个代码修改工具：fs 访问模式常量、util.log 转 console.log、zlib 属性重命名等
- 📅 团队将持续补充缺失的代码修改工具

---

### [Node.js — Node.js v20 到 v22](https://nodejs.org/en/blog/migrations/v20-to-v22)

**原文标题**: [Node.js — Node.js v20 to v22](https://nodejs.org/en/blog/migrations/v20-to-v22)

本文介绍了从 Node.js v20 迁移到 v22 的部分内容，用户端迁移团队正在开发更多代码修改工具以协助迁移。

- 🔄 import 断言功能已被 with 属性替代，JSON 模块导入需使用新语法
- ⚠️ with 关键字自 Node.js 18.20 引入，但在 v22 中成为强制要求
- 🛠️ 可通过 npx 运行@nodejs/import-assertions-to-attributes 自动转换代码
- 📚 完整源代码可在 Codemod Registry 的 import-assertions-to-attributes 目录获取
- 📝 迁移示例：将`import jsonData from './data.json' assert {type:'json'}`改为使用 with 属性语法

---

### [Node.js — 从 v14 到 v16 版本](https://nodejs.org/en/blog/migrations/v14-to-v16)

**原文标题**: [Node.js — Node.js v14 to v16](https://nodejs.org/en/blog/migrations/v14-to-v16)

本文介绍了从 Node.js v14 迁移到 v16 的部分内容，提供了四个自动化代码迁移工具来帮助更新已弃用的 API。

- 🔄 `create-require-from-path` 代码迁移工具将已弃用的`createRequireFromPath`函数替换为现代的`createRequire`函数
- 📦 `process-main-module` 代码迁移工具将`process.mainModule`属性替换为`require.main`的使用
- 🗂️ `rmdir` 代码迁移工具将`fs.rmdir`函数替换为`fs.rm`函数并添加`{ recursive: true }`选项
- 📁 `tmpDir-to-tmpdir` 代码迁移工具将`tmpDir`函数重命名为`tmpdir`

---

### [Node.js — 从 v12 到 v14 版本更新](https://nodejs.org/en/blog/migrations/v12-to-v14)

**原文标题**: [Node.js — Node.js v12 to v14](https://nodejs.org/en/blog/migrations/v12-to-v14)

本文介绍了从 Node.js v12 迁移到 v14 的部分内容，用户端迁移团队正在开发更多代码修改工具以协助迁移。

- 🔄 提供代码修改工具帮助从 Node.js v12 迁移至 v14
- 📝 将已弃用的 util 日志函数转换为现代 console 方法
- ⚠️ 涉及 DEP0026-DEP0029 四个弃用函数的替换规则
- 🔍 工具源码可在 util-print-to-console-log 目录查看
- 📚 可通过 Codemod Registry 获取该迁移工具
- 💻 支持使用 npx 命令直接运行迁移工具
- 📊 提供具体代码转换示例说明修改效果

---

### [Node.js — 用户态迁移](https://nodejs.org/en/learn/getting-started/userland-migrations)

**原文标题**: [Node.js — Userland Migrations](https://nodejs.org/en/learn/getting-started/userland-migrations)

Node.js 用户端迁移项目通过官方代码转换工具帮助开发者升级代码库以适应新版本，包含使用指南和最佳实践。

- 🛠️ 提供官方代码转换工具，协助处理废弃功能与重大变更
- 🤝 与 Codemod 平台合作开发，确保工具可靠性
- 📋 通过 GitHub 看板实时追踪迁移进度和任务状态
- ⚡ 使用 npx 命令快速执行代码转换
- 🔍 建议在独立分支运行迁移并仔细审查代码变更
- 🧪 迁移后需进行完整测试和代码格式化
- 📚 提供迁移指南文档库供参考查阅
- 💡 开放反馈渠道鼓励社区参与改进

---

### [从 JavaScript 迁移到 TypeScript | 前端大师](https://frontendmasters.com/courses/typescript-first-steps/?utm_source=email&utm_medium=nodeweekly&utm_content=typescript)

**原文标题**: [Migrate from JavaScript to TypeScript | Frontend Masters](https://frontendmasters.com/courses/typescript-first-steps/?utm_source=email&utm_medium=nodeweekly&utm_content=typescript)

本课程由 Anjana Vakil 主讲，时长近 8 小时，系统讲解从 JavaScript 迁移到 TypeScript 的全过程。课程通过实际项目演示静态类型的力量，涵盖类型注解、接口、泛型等核心概念，帮助开发者编写更安全可靠的代码，并配置 TypeScript 编译器实现全栈类型安全。

- 🎯 从 JavaScript 平稳过渡到 TypeScript，通过实际项目掌握静态类型编程
- 🛠️ 学习类型注解、接口和泛型等核心概念，提升代码质量与可维护性
- ⚙️ 配置 TypeScript 编译器，掌握 tsconfig.json 配置技巧
- 🔄 实现前后端代码的 TypeScript 转换，建立端到端类型安全
- 💡 深入理解联合类型、类型守卫和类型别名等高级特性
- 📚 通过实战练习巩固知识，包括错误修复和类型注解实践
- 🌐 学习使用 DefinitelyTyped 获取类型声明，集成社区资源
- 🚀 探索类型检查开发工作流，提升开发效率与代码可靠性

---

### [从 BitTorrent 导入 Node 模块：import myModule from "./my-module.torrent"](https://evanhahn.com/node-torrent-import/)

**原文标题**: [import myModule from "./my-module.torrent": requiring Node modules from BitTorrent](https://evanhahn.com/node-torrent-import/)

Evan Hahn 开发了一个名为 torrent-import 的实验性工具，允许通过 Node.js 的自定义钩子功能从 BitTorrent 网络导入 JavaScript 模块

- 🧩 利用 Node.js 自定义钩子功能实现模块加载机制创新
- 🌐 通过 WebTorrent 库实现.torrent 文件和磁力链接的模块下载
- 🔍 探索基于内容寻址的模块管理替代传统位置寻址方案
- 💾 具备数据完整性验证、去重和长期保存优势
- ⚠️ 存在稳定性、安全性、工具兼容性和种子可用性等限制
- 🎯 目前仅为概念验证，尚未达到生产环境使用标准
- 🚀 展示了 Node.js 自定义钩子在扩展模块系统方面的潜力

---

### [模块：node:module API | Node.js v21.7.3 文档](https://nodejs.org/docs/latest-v21.x/api/module.html#customization-hooks)

**原文标题**: [Modules: node:module API | Node.js v21.7.3 Documentation](https://nodejs.org/docs/latest-v21.x/api/module.html#customization-hooks)

Node.js v21.7.3 文档的模块系统部分，重点介绍了 node:module API 的功能和自定义钩子机制，用于扩展模块解析与加载行为。

- 📚 **模块对象工具** - 提供与 Module 实例交互的通用方法，支持 CommonJS 和 ES 模块
- 🔍 **内置模块检测** - 通过 builtinModules 和 isBuiltin() 验证模块来源
- 🎯 **自定义模块解析** - createRequire() 可创建针对特定文件的 require 函数
- ⚡ **实时绑定同步** - syncBuiltinESMExports() 同步内置 ES 模块与 CommonJS 导出的属性
- 🔧 **模块定制钩子** - 通过 register() 注册 resolve、load、initialize 钩子来自定义模块加载流程
- 🔗 **钩子链式调用** - 支持多个钩子注册，采用后进先出 (LIFO) 执行顺序
- 🌐 **多线程架构** - 钩子在独立线程运行，需通过消息通道与主线程通信
- 📝 **源映射支持** - 提供 SourceMap 类和相关工具函数，支持源码调试
- 💡 **实用示例** - 包含 HTTPS 导入、代码转译、导入映射等实际应用场景

---

### [Node.js 24 成为长期支持版本：你需要了解的内容](https://nodesource.com/blog/nodejs-24-becomes-lts)

**原文标题**: [Node.js 24 Becomes LTS: What You Need to Know](https://nodesource.com/blog/nodejs-24-becomes-lts)

Node.js 24 LTS "Krypton" 正式发布，进入长期支持阶段直至 2028 年 4 月，为生产环境带来更强安全性、严格运行时验证和增强的 Web API 支持。NodeSource 同时宣布 N|Solid 6.0.2 全面支持该版本，提供企业级监控与性能分析功能。

- 🔒 **安全升级** - 默认采用 OpenSSL 3.5 并设置安全等级 2，禁止弱加密算法
- ⚡ **运行时优化** - Buffer/fs/timers等API增强参数验证，提升错误捕获能力
- 🌐 **Web 标准对齐** - 新增 CloseEvent/Float16Array 等全局对象，强化 fetch 规范
- 🔄 **模块互通** - ESM CommonJS 包装器默认导出 module.exports，简化混合模块使用
- 📊 **流处理增强** - 改进 stream/readline 错误处理机制，提升 I/O 稳定性
- 🛠️ **构建要求更新** - 源码编译需 GCC 12.2+ 或 Xcode 16.1+ 等现代工具链
- 🚫 **API 清理** - 移除 util.is*() 等废弃接口，保持核心轻量化
- 📦 **平台支持调整** - 停止 32 位 Windows/armv7 支持，macOS 要求 13.5+
- 🎯 **N|Solid 集成** - 提供 gRPC 通信优化、OpenTelemetry 增强等企业级功能
- 📅 **多版本支持** - 同时维护 Node.js 20/22/24三个LTS版本的N|Solid兼容

---

### [Node.js — Node.js v24.11.0（长期支持版）](https://nodejs.org/en/blog/release/v24.11.0)

**原文标题**: [Node.js — Node.js v24.11.0 (LTS)](https://nodejs.org/en/blog/release/v24.11.0)

Node.js 24.11.0 版本正式进入长期支持阶段，代号"氪星"，将持续维护至 2028 年 4 月，本次更新主要调整了版本元数据并修复了已知问题。

- 🚀 Node.js 24.11.0 版本进入 LTS 长期支持阶段，代号"氪星"
- 📅 支持周期持续至 2028 年 4 月底
- 🔄 相比 24.10.0 版本仅更新了元数据信息
- ⚠️ 存在 Buffer.allocUnsafe 意外返回清零缓冲区的已知问题
- 🔧 计划在下个 LTS 版本恢复该 API 的原始行为
- 🌐 提供 Windows/macOS/Linux/AIX 等多平台安装包
- 📚 完整文档和源代码已同步发布

---

### [Node.js — Node.js v25.1.0（当前版本）](https://nodejs.org/en/blog/release/v25.1.0)

**原文标题**: [Node.js — Node.js v25.1.0 (Current)](https://nodejs.org/en/blog/release/v25.1.0)

Node.js v25.1.0 版本发布，主要包含 HTTP 服务器优化、SQLite 防御标志支持、源码监控配置等新功能，同时进行了多项依赖更新、错误修复和性能改进。

- 🚀 HTTP 服务器新增 optimizeEmptyRequests 选项，优化空请求处理
- 🛡️ SQLite 支持设置防御性标志，增强数据安全性  
- 👁️ 源码模块新增监控配置命名空间，便于开发调试
- 📦 更新核心依赖项，包括 V8 引擎、SIMDJSON 和 Corepack
- 🔧 修复多项测试用例和工具链问题，提升稳定性
- 📚 完善类型定义和文档，改进开发者体验
- ⚡ 优化模块加载和虚拟机执行性能
- 🐛 解决内存泄漏和错误处理相关缺陷

---

### [加强 npm 安全性：认证与令牌管理的重要更新 - GitHub 更新日志](https://github.blog/changelog/2025-09-29-strengthening-npm-security-important-changes-to-authentication-and-token-management/)

**原文标题**: [Strengthening npm security: Important changes to authentication and token management - GitHub Changelog](https://github.blog/changelog/2025-09-29-strengthening-npm-security-important-changes-to-authentication-and-token-management/)

npm 将于 2025 年 9 月至 11 月实施三项安全升级：缩短细粒度令牌有效期至 7-90 天、停用经典令牌、逐步淘汰 TOTP 双重验证，以强化生态系统安全。

- 🔐 细粒度令牌有效期缩短为 7 天（默认）至 90 天（最长），降低供应链攻击风险
- 🚫 经典令牌将全面停用，需立即更换为细粒度权限令牌
- ⏳ TOTP 双重验证将逐步淘汰，推荐迁移至 WebAuthn/通行密钥
- 🗓️ 变更分阶段实施：10 月初启用新令牌规则，11 月中旬废止经典令牌
- 🔄 推荐采用信任发布（OIDC）实现无令牌自动化流程
- 🤝 呼吁社区参与迁移并通过官方渠道反馈问题
- 📚 提供文档、社区讨论和技术支持协助过渡

---

### [Bun — 一款快速的全能 JavaScript 运行时](https://bun.sh/)

**原文标题**: [Bun — A fast all-in-one JavaScript runtime](https://bun.sh/)

Bun v1.3.1 是一个高性能的 JavaScript 全栈工具包，兼具运行时、打包器、测试运行器和包管理器功能，强调渐进式采用和与 Node.js 的完全兼容性。

- 🚀 **极速性能**：在多项基准测试中表现卓越，如打包 10,000 个 React 组件仅需 269.1 毫秒，远超其他工具
- 🔧 **全栈工具**：集成运行时、打包器、测试运行器和包管理器，支持 JavaScript、TypeScript 和 JSX
- 📦 **渐进式采用**：可单独使用工具（如 bun test 或 bun install），也可完整替换 Node.js 项目
- ⚡ **高效处理**：Express.js 服务器每秒处理 59,026 次请求，WebSocket 聊天服务器每秒发送 2,536,227 条消息
- 🗃️ **数据库性能**：加载大表时每秒处理 28,571 次查询，性能显著优于 Node.js 和 Deno
- 🔄 **完全兼容**：致力于 100% 兼容 Node.js 生态系统
- 💻 **跨平台支持**：提供 Linux、macOS 和 Windows 的安装脚本，支持 curl 和 PowerShell 安装方式

---

### [Vercel 现已支持 Bun 运行时 | Bun 博客](https://bun.com/blog/vercel-adds-native-bun-support)

**原文标题**: [Vercel now supports the Bun Runtime | Bun Blog](https://bun.com/blog/vercel-adds-native-bun-support)

Vercel 现已全面支持 Bun 运行时作为公开测试版，开发者可在部署时选择使用 Bun 作为 JavaScript 运行时环境。

- 🚀 通过在 vercel.json 配置中添加`"bunVersion": "1.x"`即可启用 Bun 运行时
- ⚡ 原生支持 Next.js、Hono 等框架，可直接在服务端调用 Bun API
- 🛠️ 集成 Bun 完整工具链（包管理器/运行时/打包器/测试运行器）
- 📦 自动依赖安装与原生执行，同时支持本地开发和生产环境
- 🧩 支持 Bun.SQL、Bun.S3 等专属 API 及 Web API 标准
- 🌱 作为公开测试版发布，持续优化框架兼容性与性能表现
- 📊 具备更低内存/CPU 占用率，采用 Zig 语言编写的高效运行时
- 🔄 与 Vercel 深度合作，未来将扩展更多框架支持范围

---

### [Fastify 零配置支持 - Vercel](https://vercel.com/changelog/zero-configuration-support-for-fastify)

**原文标题**: [Zero-configuration support for Fastify - Vercel](https://vercel.com/changelog/zero-configuration-support-for-fastify)

Vercel 现已支持 Fastify 框架部署，提供零配置的开发者体验和自动扩展功能。

- 🚀 Vercel 平台正式集成 Fastify 框架，支持快速部署
- ⚡ 具备极低开销的插件架构，提供最优开发者体验
- 🌐 默认采用 Fluid 计算和动态 CPU 计费模式
- 📊 根据流量自动弹性伸缩，按实际使用量计费
- 🎯 支持零配置部署，包含完整的 Hello World 示例代码
- 📚 提供详细的 Fastify on Vercel 官方文档指南

---

### [在 Hugging Face 空间中运行 Node.js](https://blog.tomayac.com/2025/11/03/running-nodejs-in-a-hugging-face-space/)

**原文标题**: [Running Node.js in a Hugging Face Space](https://blog.tomayac.com/2025/11/03/running-nodejs-in-a-hugging-face-space/)

本文介绍了在 Hugging Face Spaces 中创建可长期维护的 Node.js 服务器模板的方法，以替代已停止服务的 Glitch 平台。

- 🐢 使用 Docker 作为 Space SDK 创建空白模板，选择免费层级和公开/私有设置
- 📦 创建 package.json 文件时采用"latest"标签保持模板版本中立性
- 🐳 通过 lts-alpine 标签的 Dockerfile 确保始终使用 Node.js LTS 版本和轻量级 Alpine Linux
- ⚡ 默认 index.js 配置 Express 服务器运行在 7860 端口，并动态显示运行时版本信息
- 📝 通过 README.md 的 YAML 前置元数据配置 Space 参数和自定义响应头
- 🔧 支持 git 克隆到本地开发，复制模板后需手动固化 Node.js 和 Express 版本号
- 🌐 应用运行在独立浏览器上下文中，可配置 COOP/COEP 头启用 SharedArrayBuffer 等高级功能

---

### [Glitch 即将迎来重大更新](https://blog.glitch.com/post/changes-are-coming-to-glitch)

**原文标题**: [Important changes are coming to Glitch](https://blog.glitch.com/post/changes-are-coming-to-glitch)

Glitch 平台宣布将于 2025 年 7 月 8 日停止应用托管服务，用户可通过仪表盘下载代码并设置域名重定向至 2025 年底。此次调整源于维护成本激增及新兴开发平台的涌现，团队将专注于为开发者社区提供更有价值的服务。

- 🗓️ 2025 年 7 月 8 日终止项目托管与用户档案服务
- 💾 仪表盘持续开放至 2025 年底，支持代码下载与域名重定向设置
- 💰 立即停止 Glitch Pro 新订阅，现有会员服务延续至 7 月 8 日
- 🌐 维护成本攀升与行业竞争促使战略转型
- 📚 即将发布项目迁移指南，社区论坛提供技术支持
- ✉️ 欢迎通过论坛或 anil@glitch.com 邮箱反馈建议

---

### [Spaces - 拥抱未来](https://huggingface.co/spaces)

**原文标题**: [Spaces - Hugging Face](https://huggingface.co/spaces)

该页面展示了 Hugging Face 平台上当前运行的各类 AI 应用，涵盖图像生成、视频处理、文本分析等多元领域，并按热度排序呈现最新活跃项目。

- 🎬 视频生成工具占据主流，如 Wan2.2 系列支持通过图像/文本生成视频（Wan2.2 Animate、LongCat Video）
- 📚 大语言模型训练指南受关注（The Smol Training Playbook、The Ultra-Scale Playbook）
- 🖼️ 多模态应用丰富，包括图像生成（FIBO、Miragic AI）、3D 建模（Hunyuan3D-2.1）和图像编辑（ImageEditPro）
- 🔊 语音合成技术持续更新（KaniTTS、Ringg TTS 提供文本转语音服务）
- 🔧 开发工具多样化，涵盖浏览器端工具调用（Granite 4.0 Nano）、OCR 识别（DeepSeek OCR）和代码生成（DeepSite v3）
- 📊 专业领域应用涵盖金融分析（FIBO-Labs）、医学影像和机器人学习教程
- 🏆 模型优化技术活跃，包括模型蒸馏、嵌入优化（LFM2 ColBERT）和数据集构建（FineWeb）
- ⏱️ 实时性突出，多数应用在最近 24 小时内更新，部分项目标注具体更新时间（如 3 小时前）

---

### [使用 Foxit PDF Services API 自动将 Office 文档转换为 PDF - Foxit](https://developer-api.foxit.com/developer-blogs/use-cases-workflow-examples/automated-document-pipelines/convert-office-docs-to-pdfs-automatically-with-foxit-pdf-services-api/?utm_source=cooperpress&utm_medium=Display&utm_campaign=11-04-25)

**原文标题**: [Convert Office Docs to PDFs Automatically with Foxit PDF Services API - Foxit](https://developer-api.foxit.com/developer-blogs/use-cases-workflow-examples/automated-document-pipelines/convert-office-docs-to-pdfs-automatically-with-foxit-pdf-services-api/?utm_source=cooperpress&utm_medium=Display&utm_campaign=11-04-25)

概述了 Foxit 在 API World 2025 展示的智能文档工作流解决方案，重点演示了如何构建可审计的 AI 驱动文档自动化系统。

- 🌐 参与 API World 2025 技术盛会并与开发者深入交流
- 🤖 展示基于 Foxit API 的智能文档应用场景（AI 简历生成器/互动涂鸦应用）
- 📑 详解如何通过 PDF 服务和文档生成 API 构建可审计文档系统
- 🎤 现场演示由 Jorge Euceda 操作的实际工作流程
- ⚡ 强调 AI 驱动文档自动化技术的实践应用

---

### [我们为何从 Python 迁移至 Node.js](https://blog.yakkomajuri.com/blog/python-to-node)

**原文标题**: [Why we migrated from Python to Node.js](https://blog.yakkomajuri.com/blog/python-to-node)

一家初创公司在发布一周后将后端从 Python 迁移到 Node.js，主要因为 Python 异步编程的复杂性和性能限制

- 🚀 为应对高并发需求选择 Node.js，初期基准测试显示吞吐量提升约 3 倍
- 🐍 放弃 Django 因其异步支持不完善，包括 ORM 缺乏完整异步功能和复杂的同步/异步转换
- ⚡ 选择 Express+MikroORM 组合，看重 Node.js 事件循环的原生异步处理能力
- 🔄 统一了代码库，将 Express 服务器和后台工作程序合并，消除重复逻辑
- 📚 迁移过程耗时 3 天，虽面临客户需求压力但最终获得更好的测试覆盖和代码结构
- 🛠️ 失去 Python 生态优势但获得开发效率提升，特别是处理 LLM 和嵌入 API 时
- 💡 建议早期初创公司在代码库较小时考虑技术栈迁移，长期收益显著

---

### [MikroORM：基于数据映射器、工作单元和身份映射模式的 Node.js TypeScript ORM。 | MikroORM](https://mikro-orm.io/)

**原文标题**: [MikroORM: TypeScript ORM for Node.js based on Data Mapper, Unit of Work and Identity Map patterns. | MikroORM](https://mikro-orm.io/)

MikroORM 是一个功能丰富的 Node.js ORM 框架，支持自动事务管理、多种数据库类型、数据库同步工具、数据填充、查询优化和事件系统等特性。

- 🔄 自动事务处理：通过 `em.flush()` 自动将计算变更包装在数据库事务中
- 📝 简洁实体定义：利用源码分析技术，只需定义 TypeScript 类型即可完成实体配置
- 🗄️ 多数据库支持：兼容 MongoDB、MySQL、MariaDB、PostgreSQL、MS SQL Server、SQLite 等数据库
- 🔄 数据库同步工具：提供 SchemaGenerator 快速生成原型，Migrator 生成迁移差异，EntityGenerator 从数据库模式生成实体定义
- 🌱 数据填充功能：通过 Seeder 和种子工厂轻松生成任意规模和形状的假数据
- ⚡ 自动批处理：UnitOfWork 自动批量处理所有插入、更新、删除等查询操作
- 🔊 事件系统：强大的事件系统可挂钩实体生命周期，支持通过 onFlush 事件修改 UnitOfWork 行为
- 🔍 智能查询构建器：包含支持自动连接的元数据感知 QueryBuilder
- 🎯 全局过滤器：可定义和控制全局通用过滤器，支持多租户数据隔离和软删除实体自动隐藏

---

### [为什么在 JavaScript 中 NaN 不等于 NaN（及其背后的 IEEE 754 故事） | Piotr Zarycki - 编程博客](https://pzarycki.com/en/posts/js-nan/)

**原文标题**: [Why NaN !== NaN in JavaScript (and the IEEE 754 story behind it) | Piotr Zarycki - Programming Blog](https://pzarycki.com/en/posts/js-nan/)

JavaScript 中的 NaN 不等于 NaN 是 IEEE 754 标准的有意设计，通过硬件级实现来处理浮点数运算中的未定义结果，确保程序稳定运行并支持错误检测。

- 🔍 NaN 在 JavaScript 中被识别为数字类型，但所有数学运算结果仍为 NaN
- 🌐 浏览器通过 std::isnan 检测 NaN，源自 1985 年制定的 IEEE 754 国际标准
- ⚙️ 硬件层面通过 xmm 寄存器和 ucomisd 指令实现 NaN 的生成与比较
- 🚩 NaN !== NaN 是故意设计，便于用 x != x 检测无效数值
- 🛡️ IEEE 754 定义了静默 NaN（传播不报错）和信号 NaN（触发异常）
- ✈️ 未标准化前，类似 0/0 的运算会导致程序崩溃（如航空系统风险）
- 📊 采用 NaN 方案优于程序崩溃、返回错误值或 null 等替代方案
- 🔄 NaN 会在运算链中传播，允许最终统一检查而非逐操作验证
- 💡 现代编程语言（Python/C++/Rust）均遵循此标准实现 NaN 特性

---

### [在 Node 24 中使用 URLPattern 作为无框架路由器](https://jsdev.space/urlpattern-router-node24/)

**原文标题**: [Using URLPattern as a Framework-Free Router in Node 24](https://jsdev.space/urlpattern-router-node24/)

JavaScript 现已在 Node.js 24 和浏览器中原生支持 URLPattern API，提供跨平台、无框架的路由解决方案，支持命名参数、正则验证和统一语义。

- 🌐 **原生跨平台支持**：URLPattern 在 Node.js 24 中全局可用，无需导入，同时兼容主流浏览器，实现客户端与服务端路由逻辑统一
- 🔧 **灵活路由匹配**：支持协议、主机名、路径等 URL 各部分匹配，提供命名捕获组、大小写控制和简洁模式语法
- ⚡ **轻量路由实现**：通过 PathRule 和 SmartRouter 类构建无依赖类型安全路由器，支持参数类型转换和复用模式实例
- 🛠️ **多环境适配**：同一套路由规则可同时用于 Service Worker 响应拦截和 Node.js HTTP 服务器处理
- 📊 **性能优化建议**：预编译 URLPattern 实例避免重复创建，限制用户输入的正则模式，在 Node 中始终使用绝对 URL
- ⚖️ **权衡考量**：虽不及专用路由库的极致性能，但为共享逻辑和统一验证提供了理想方案
- 🔍 **实用功能示例**：支持主机协议匹配、路径参数验证、查询参数处理，提供完整的请求上下文对象
- 🚀 **生产就绪**：具备足够的性能表现，适合轻量级 API 和服务 worker 场景，实现全栈路由定义一体化

---

### [GitHub - sindresorhus/image-dimensions：获取图片尺寸](https://github.com/sindresorhus/image-dimensions)

**原文标题**: [GitHub - sindresorhus/image-dimensions: Get the dimensions of an image](https://github.com/sindresorhus/image-dimensions)

这是一个用于获取图像尺寸的 JavaScript 工具库，支持多种运行环境并涵盖主流图像格式

- 📏 支持 JPEG/PNG/GIF/WebP/AVIF/HEIF 等主流图像格式的尺寸获取
- 🌐 兼容浏览器/Node.js/Bun/Deno 等现代 JavaScript 运行环境
- ⚡ 提供流式处理 API，仅需读取少量数据即可获取尺寸信息
- 📦 零依赖、体积小巧，专为图像尺寸检测场景优化
- 🔧 提供 CLI 命令行工具和编程接口两种使用方式
- 📄 采用 MIT 开源协议，目前获得 478 星标和 12 个分支

---

### [GitHub - image-size/image-size: 用于检测图像尺寸的 Node 模块](https://github.com/image-size/image-size)

**原文标题**: [GitHub - image-size/image-size: Node module for detecting image dimensions](https://github.com/image-size/image-size)

这是一个用于检测图像尺寸的 Node.js 模块，支持多种图像格式，具有零依赖、轻量级和高性能的特点。

- 🚀 **零依赖设计** - 不依赖任何外部库，保持轻量级
- 🖼️ **广泛格式支持** - 支持 BMP、GIF、JPEG、PNG、WebP 等 20 多种图像格式
- 💾 **灵活输入方式** - 支持 Buffer/Uint8Array 和文件读取两种方式
- ⚡ **高效性能** - 仅读取图像头部信息，内存占用极小
- 📐 **多尺寸处理** - 支持 HEIF、ICO 等格式的多图像尺寸检测
- 🔧 **TypeScript 支持** - 内置 TypeScript 类型定义
- 📊 **EXIF 方向检测** - 可读取 JPEG 图像的 EXIF 方向信息
- ⚙️ **可配置性** - 支持禁用特定图像类型和调整并发限制
- 🌐 **网络支持** - 可通过 URL 获取远程图像尺寸
- 📜 **MIT 许可证** - 开源免费使用

---

### [GitHub - privatenumber/type-flag: ⛳️ Node.js 类型化命令行参数解析器](https://github.com/privatenumber/type-flag)

**原文标题**: [GitHub - privatenumber/type-flag: ⛳️ Typed command-line arguments parser for Node.js](https://github.com/privatenumber/type-flag)

这是一个用于 Node.js 的强类型命令行参数解析库，具有轻量化和类型安全的特点。

- 🚀 轻量无依赖，打包后最大仅 1.4kB
- ⚡ 支持 TypeScript 强类型推断
- 🔧 提供 typeFlag 和 getFlag 两种使用方式
- 📝 支持字符串、数字、布尔值、数组等多种数据类型
- 🔄 支持别名设置和默认值配置
- 🎯 自动将 kebab-case 标志名映射为 camelCase
- 📋 可解析未知标志和命令行参数
- 💡 支持自定义类型和验证逻辑
- 🛠️ 提供丰富的配置选项和灵活的使用场景

---

### [Electron 39.0.0 版本发布 | Electron](https://www.electronjs.org/blog/electron-39-0)

**原文标题**: [Electron 39.0.0 | Electron](https://www.electronjs.org/blog/electron-39-0)

Electron 39.0.0 正式发布，包含 Chromium、V8 和 Node.js 的版本升级，新增多项功能改进并引入破坏性变更。

- 🚀 核心组件升级至 Chromium 142.0.7444.52、Node.js 22.20.0 和 V8 14.2
- 🛡️ ASAR 完整性校验功能结束实验阶段，现已稳定可用
- ⚡ 新增硬件加速检测、HDR 色彩支持、Linux 系统主题色获取等特性
- ⚠️ 废弃 --host-rules 命令行参数，需改用 --host-resolver-rules
- 🖼️ window.open 弹窗默认调整为可调整尺寸
- 🔄 共享纹理离屏渲染事件数据结构优化
- 📅 Electron 36.x.y 版本已停止官方支持

---

### [Node.js — Node.js v22.20.0（长期支持版）](https://nodejs.org/en/blog/release/v22.20.0)

**原文标题**: [Node.js — Node.js v22.20.0 (LTS)](https://nodejs.org/en/blog/release/v22.20.0)

Node.js v22.20.0 (LTS) 版本发布，包含 OpenSSL 升级、多项功能增强及错误修复，确保长期支持至 2027 年。

- 🔐 OpenSSL 升级至 3.5.2，延长支持周期至 2027 年
- 🌐 HTTP/2 支持原始标头数组，提升网络处理能力
- 📦 SEA（单可执行应用）新增 execArgv 配置支持
- 🌀 流处理增加 Brotli 压缩算法支持
- 🧪 测试运行器支持对象属性模拟功能
- 👷 Worker 线程新增 CPU 性能分析 API
- 🔧 多项错误修复和性能优化

---

### [GitHub - sindresorhus/on-change：监听对象或数组变化的工具](https://github.com/sindresorhus/on-change)

**原文标题**: [GitHub - sindresorhus/on-change: Watch an object or array for changes](https://github.com/sindresorhus/on-change)

on-change 是一个用于监听对象或数组变化的 JavaScript 库，通过 Proxy API 实现递归监听，支持深度属性变化检测和自定义回调函数。

- 🎯 基于 Proxy API 实现对象/数组变化监听
- 🔍 支持递归监听深度属性变化
- 📦 通过 npm 安装使用，提供完整 API 文档
- ⚙️ 支持多种配置选项：浅监听、自定义相等比较、忽略特定属性等
- 🎪 提供 target() 方法获取原始对象，unsubscribe() 取消监听
- 💡 典型应用场景：自动保存数据变更，简化代码逻辑
- 🔗 相关项目：known、negative-array 等基于 Proxy 的实用工具
- 📄 采用 MIT 开源协议，由 Sindre Sorhus 等维护者共同开发

---

### [ConfigCat - 团队功能特性开关服务](https://configcat.com/promotions/node-weekly/?utm_source=cooperpress_newsletter&utm_medium=sponsor&utm_campaign=cooperpress_node_202510)

**原文标题**: [ConfigCat - Feature Flag Service for Teams](https://configcat.com/promotions/node-weekly/?utm_source=cooperpress_newsletter&utm_medium=sponsor&utm_campaign=cooperpress_node_202510)

ConfigCat 是一个功能开关管理平台，帮助开发团队通过功能标志控制功能发布流程，支持渐进式发布和即时回滚。

- 🚀 无风险功能发布 - 支持定向用户灰度发布，出现问题可立即关闭功能
- ⚡ 快速集成 - 10 分钟完成设置，无需信用卡，提供 NODE25 优惠码
- 💻 客户端评估 - 功能标志在客户端评估，不收集用户数据
- 🛡️ 安全保障 - 符合隐私合规要求，提供完整数据控制权
- 💰 透明定价 - 永久免费版含 10 个功能标志，付费版享 25% 折扣
- 🔄 无厂商锁定 - 支持数据导出和 OpenFeature 标准
- 🌟 客户认可 - 多家企业评价优于 LaunchDarkly，简单易用且成本更低
- 📊 多方案选择 - 从免费到企业级方案，满足不同规模团队需求

---

### [GitHub - ekalinin/sitemap.js: Node.js 站点地图生成框架](https://github.com/ekalinin/sitemap.js)

**原文标题**: [GitHub - ekalinin/sitemap.js: Sitemap-generating framework for node.js](https://github.com/ekalinin/sitemap.js)

这是一个用于 Node.js 的站点地图生成框架，支持流式处理和多种配置选项。

- 🗺️ 支持生成标准站点地图 XML 文件，包含 URL、更新频率和优先级等属性
- ⚡ 提供流式处理接口，可高效处理大量 URL 数据
- 🔧 支持 CLI 命令行工具和编程 API 两种使用方式
- 📦 可自动分割大文件，当 URL 超过 5 万条时自动创建站点地图索引
- 🎯 提供丰富的配置选项，包括主机名、XSL 样式表、XML 命名空间等
- 🖼️ 支持图片、视频、多语言链接等扩展站点地图功能
- 🔄 可与 Express 等 Web 框架集成，支持缓存和 gzip 压缩
- 📊 提供过滤功能，可在解析过程中筛选站点地图条目
- 📄 采用 MIT 开源协议，拥有活跃的社区维护

---

### [GitHub - sverweij/dependency-cruiser：依赖关系验证与可视化工具。自定义规则，支持JavaScript、TypeScript、CoffeeScript，兼容ES6、CommonJS、AMD模块规范。](https://github.com/sverweij/dependency-cruiser)

**原文标题**: [GitHub - sverweij/dependency-cruiser: Validate and visualize dependencies. Your rules. JavaScript, TypeScript, CoffeeScript. ES6, CommonJS, AMD.](https://github.com/sverweij/dependency-cruiser)

dependency-cruiser 是一个用于分析和可视化 JavaScript、TypeScript 等项目中依赖关系的工具，支持自定义规则验证依赖结构，并能生成多种格式的依赖图。

- 🔍 **依赖验证工具** - 可检测循环依赖、缺失依赖等问题
- 📜 **多语言支持** - 支持 JavaScript、TypeScript、CoffeeScript 等多种语言
- ⚙️ **自定义规则** - 通过配置文件定义依赖约束规则
- 📊 **可视化输出** - 生成 DOT、SVG、HTML 等多种格式的依赖图
- 🛠️ **命令行工具** - 通过 npm 安装使用，支持多种包管理器
- 🔄 **实时检测** - 在构建过程中自动验证依赖关系
- 🌐 **大型项目适用** - 已被 4600+ 项目使用，包含许多知名开源项目
- 📝 **丰富文档** - 提供详细的使用指南和规则编写教程
- 🔗 **扩展支持** - 支持 Webpack 别名、JSX/TSX 等高级特性
- 📄 **开源协议** - 采用 MIT 许可证开源

---

### [pnpm 10.20 | pnpm](https://pnpm.io/blog/releases/10.20)

**原文标题**: [pnpm 10.20 | pnpm](https://pnpm.io/blog/releases/10.20)

pnpm 10.20 版本更新了帮助命令功能并修复了若干问题，提升了包管理器的稳定性和用户体验。

- 📋 新增`pnpm help --all`选项，可列出所有命令
- 🎯 当`latest`版本不符合成熟度要求时，自动选择符合要求的最高版本
- ⚡ 优化`create`命令，不再验证补丁信息
- 🔧 切换 pnpm CLI 版本时自动禁用版本管理功能，避免重复切换

---

### [GitHub - biggora/express-useragent：NodeJS用户代理中间件](https://github.com/biggora/express-useragent)

**原文标题**: [GitHub - biggora/express-useragent: NodeJS user-agent middleware](https://github.com/biggora/express-useragent)

这是一个用于 Node.js 的快速用户代理解析库，提供 Express 中间件和 TypeScript 支持，支持服务端和浏览器端使用。

- 🚀 快速用户代理解析器，支持 Express 中间件和 TypeScript 类型定义
- 🌐 支持 Node.js 服务端和浏览器端使用（通过 IIFE 打包）
- 📦 要求 Node.js 18 或更高版本，可通过 npm 安装
- 🔧 提供多种导入方式：ESM 命名导入、命名空间导入和 CommonJS
- 📊 解析结果包含浏览器、操作系统、平台信息和设备类型判断
- 🛠️ 提供完整的开发工具链：测试、构建、代码检查等脚本
- 📄 采用 MIT 开源协议，支持社区贡献和问题反馈
- 🌍 支持浏览器端使用，提供全局脚本和模块导入两种方式

---

### [GitHub - jsdom/jsdom: 针对 Node.js 的多种 Web 标准的 JavaScript 实现](https://github.com/jsdom/jsdom)

**原文标题**: [GitHub - jsdom/jsdom: A JavaScript implementation of various web standards, for use with Node.js](https://github.com/jsdom/jsdom)

jsdom 是一个用于 Node.js 的纯 JavaScript 实现的 Web 标准库，主要用于模拟浏览器环境以支持测试和网页抓取。

- 🌐 提供完整的 DOM 和 HTML 标准实现，可在 Node.js 中模拟浏览器环境
- ⚙️ 支持自定义配置，包括 URL、引用来源、内容类型和资源加载等选项
- ⚠️ 默认禁用脚本执行，需显式启用 runScripts 选项（存在安全风险）
- 🔄 可通过虚拟控制台管理日志输出和错误信息
- 🍪 包含完整的 Cookie 管理功能，支持跨域请求
- 📄 提供多种便捷 API：fromURL()、fromFile() 和 fragment() 等
- 🔧 支持高级功能：节点位置追踪、VM 上下文访问和运行时重配置
- 🎯 主要用途：网页测试、内容抓取和前端自动化测试
- ⛔ 不支持可视化渲染和页面导航功能
- 📦 需要额外安装 canvas 包来支持 Canvas API

---

### [错误](https://nodeweekly.com/link/176533/web)

**原文标题**: [Error](https://nodeweekly.com/link/176533/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='nodeweekly.com', port=443): Max retries exceeded with url: /link/176533/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1000)')))

---

### [错误](https://nodeweekly.com/link/176534/web)

**原文标题**: [Error](https://nodeweekly.com/link/176534/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='nodeweekly.com', port=443): Max retries exceeded with url: /link/176534/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1000)')))

---

### [错误](https://nodeweekly.com/link/176535/web)

**原文标题**: [Error](https://nodeweekly.com/link/176535/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='nodeweekly.com', port=443): Max retries exceeded with url: /link/176535/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1000)')))

---

### [错误](https://nodeweekly.com/link/176536/web)

**原文标题**: [Error](https://nodeweekly.com/link/176536/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='nodeweekly.com', port=443): Max retries exceeded with url: /link/176536/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1000)')))

---

### [GitHub - vadimdemedes/ink：🌈 用于交互式命令行应用的 React 框架](https://github.com/vadimdemedes/ink)

**原文标题**: [GitHub - vadimdemedes/ink: 🌈 React for interactive command-line apps](https://github.com/vadimdemedes/ink)

Ink 是一个基于 React 的命令行界面 (CLI) 应用开发库，允许开发者使用熟悉的 React 组件化方式构建交互式命令行应用。

- 🎯 **React 生态兼容** - 完全支持 React 的所有特性，包括 Hooks 和组件化开发模式
- 🎨 **Flexbox 布局** - 基于 Yoga 引擎实现类似 CSS 的 Flexbox 布局系统
- 📦 **丰富组件库** - 提供 Text、Box、Newline、Spacer 等核心组件
- ⌨️ **输入处理** - 通过 useInput 钩子简化用户输入处理
- 🎛️ **焦点管理** - 支持 Tab 键焦点切换和程序化焦点控制
- 🛠️ **开发工具** - 支持 React Devtools 调试和测试工具
- ♿ **无障碍支持** - 提供屏幕阅读器支持和 ARIA 属性
- 📊 **流行应用** - 被 GitHub Copilot CLI、Cloudflare Wrangler、Gatsby 等知名项目使用
- 🔧 **灵活配置** - 支持自定义输出流、原始模式控制等高级功能
- 📚 **完善文档** - 提供详细的使用示例和 API 文档

---

### [ESLint v9.39.1 发布 - ESLint - 可插拔 JavaScript 代码检查工具](https://eslint.org/blog/2025/11/eslint-v9.39.1-released/)

**原文标题**: [ESLint v9.39.1 released - ESLint - Pluggable JavaScript Linter](https://eslint.org/blog/2025/11/eslint-v9.39.1-released/)

ESLint v9.39.1 作为补丁版本发布，修复了先前版本中因规则访问器参数传递变更导致的第三方规则兼容性问题，并同步更新了文档与依赖项。

- 🐛 修复了 v9.39.0 中规则访问器意外传入两个参数导致 @typescript-eslint/unified-signatures 等第三方规则失效的问题  
- 📚 文档新增关于 extends 与级联配置使用场景的说明章节  
- 🔧 更新 @eslint/js 依赖至 9.39.1 版本并调整相关工具链配置  
- ✅ 完善版本测试机制以适配 ESLint v10 的检测需求

---

