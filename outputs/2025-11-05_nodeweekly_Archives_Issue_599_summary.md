### [Node周刊第599期：2025年11月4日](https://nodeweekly.com/issues/599)

**原文标题**: [Node Weekly Issue 599: November 4, 2025](https://nodeweekly.com/issues/599)

本期通讯主要涵盖Node.js版本更新、开发工具和实用资源，重点介绍了Node v24成为LTS版本及相关迁移指南。

- 🚀 Node.js v24正式成为长期支持版本，v24.11.0作为LTS版本无新增功能但包含与v22的差异说明
- 📚 提供Node版本迁移指南（v22→v24/v20→v22）及官方代码修改工具辅助升级
- 🌐 实验性功能：通过BitTorrent导入Node模块展示自定义钩子能力
- ⚡ Node生态更新：v25.1.0发布、npm令牌即将失效、Vercel新增Bun运行时和Fastify支持
- ☁️ 部署方案：Hugging Face Spaces可作为Glitch替代方案托管Node应用
- 🛠️ 开发工具：图像尺寸检测库、类型化命令行解析器、Electron 39.0更新
- 📦 工具链更新：依赖可视化工具、pnpm包管理器、Express中间件等多项开发工具版本迭代

---

### [Node.js — Node.js v22 至 v24 版本](https://nodejs.org/en/blog/migrations/v22-to-v24)

**原文标题**: [Node.js — Node.js v22 to v24](https://nodejs.org/en/blog/migrations/v22-to-v24)

本文介绍了从Node.js v22迁移至v24的部分内容，包括平台支持变更、破坏性变化、源码构建要求以及可用的自动化代码迁移工具。

- 🚀 Node.js 24.11.0已进入长期支持阶段，支持将持续至2028年4月
- 🖥️ 平台支持变更：停止提供32位Windows和Linux armv7预构建版本，macOS最低要求13.5
- 🔐 OpenSSL 3.5安全升级：默认安全级别提升至2，禁用弱密钥和RC4加密套件
- ⚠️ 行为变更：强化fetch合规性、AbortSignal验证、流错误处理等多项改进
- 🔧 构建要求更新：Linux/gcc最低12.2，macOS/Xcode最低16.1
- 🛠️ 提供6个自动化代码迁移工具：
  - 📁 fs常量访问方式更新（DEP0176）
  - 📝 util.log迁移至console.log（DEP0059）
  - 📊 zlib.bytesRead更名为bytesWritten（DEP0108）
  - ✂️ fs.truncate替换为fs.ftruncate（DEP0081）
  - 🔑 RSA-PSS密钥生成参数名更新（DEP0154）
- 🔄 开发团队持续完善迁移工具，建议关注项目进展

---

### [Node.js — 从 v20 到 v22 版本](https://nodejs.org/en/blog/migrations/v20-to-v22)

**原文标题**: [Node.js — Node.js v20 to v22](https://nodejs.org/en/blog/migrations/v20-to-v22)

本文介绍了从Node.js v20迁移到v22的部分内容，用户端迁移团队正在开发更多代码修改工具以协助迁移。

- 🔄 import断言功能已被with属性替代，JSON模块导入需使用新语法
- ⚠️ with关键字自Node.js 18.20引入，但在v22中成为强制要求
- 🛠️ 可通过npx运行@nodejs/import-assertions-to-attributes代码修改工具自动转换
- 📚 完整源代码可在import-assertions-to-attributes目录中查看
- 🌐 所有代码修改工具均收录在Codemod Registry中供开发者使用

---

### [Node.js — 从 v14 到 v16 版本](https://nodejs.org/en/blog/migrations/v14-to-v16)

**原文标题**: [Node.js — Node.js v14 to v16](https://nodejs.org/en/blog/migrations/v14-to-v16)

本文介绍了从Node.js v14迁移到v16的部分内容，提供了四个自动化代码迁移工具来帮助开发者更新已弃用的API。

- 🔄 `create-require-from-path` 代码迁移工具将已弃用的`createRequireFromPath`函数替换为现代的`createRequire`函数
- 📦 `process-main-module` 代码迁移工具将`process.mainModule`属性替换为`require.main`
- 🗂️ `rmdir` 代码迁移工具将`fs.rmdir`函数替换为`fs.rm`并添加`{ recursive: true }`选项
- 📁 `tmpDir-to-tmpdir` 代码迁移工具将`tmpDir`函数重命名为`tmpdir`
- 🛠️ 所有迁移工具都可通过npx命令运行，源代码可在Codemod Registry中找到

---

### [Node.js — 从 v12 到 v14 版本](https://nodejs.org/en/blog/migrations/v12-to-v14)

**原文标题**: [Node.js — Node.js v12 to v14](https://nodejs.org/en/blog/migrations/v12-to-v14)

本文介绍了从Node.js v12迁移到v14的部分内容，用户端迁移团队正在开发更多代码修改工具以协助迁移过程。

- 🔄 提供代码修改工具帮助从Node.js v12迁移至v14
- 📝 将弃用的util打印函数转换为现代console方法
- ⚠️ 涉及DEP0026-DEP0029四个废弃功能的替换
- 🔧 支持util.print/puts转console.log，util.debug/error转console.error
- 📂 源代码存放于util-print-to-console-log目录
- 🌐 可通过Codemod Registry获取该工具
- 💻 使用命令npx codemod run @nodejs/create-require-from-path执行

---

### [Node.js — 用户态迁移](https://nodejs.org/en/learn/getting-started/userland-migrations)

**原文标题**: [Node.js — Userland Migrations](https://nodejs.org/en/learn/getting-started/userland-migrations)

Node.js用户端迁移项目通过官方代码修改工具帮助开发者升级代码库以适应新版本，包含功能迁移、破坏性变更处理和最佳实践指南。

- 🛠️ 提供官方代码修改工具，协助处理Node.js版本升级中的废弃功能和破坏性变更
- 🔍 通过Codemod平台发布经Node.js团队审核的迁移工具，确保可靠性
- 📋 建议在独立分支运行迁移，便于代码审查和测试验证
- 🧪 强调迁移后需进行代码测试、格式化和质量检查
- 📚 提供完整的迁移指南和进度看板，支持社区贡献和反馈
- 🌐 可通过GitHub项目板跟踪各类迁移任务的状态和版本信息

---

### [从BitTorrent导入Node模块：import myModule from "./my-module.torrent"](https://evanhahn.com/node-torrent-import/)

**原文标题**: [import myModule from "./my-module.torrent": requiring Node modules from BitTorrent](https://evanhahn.com/node-torrent-import/)

Evan Hahn开发了一个名为torrent-import的实验性工具，允许通过Node.js的Customization Hooks功能从BitTorrent网络导入JavaScript模块。

- 🧩 利用Node.js新特性Customization Hooks实现模块加载机制重写
- 🌐 通过WebTorrent库实现.torrent文件和磁力链接的模块下载
- 🔍 探索基于内容寻址(content-addressed)的模块管理替代方案
- 📦 演示案例支持从Internet Archive托管的种子文件导入greet模块
- ⚠️ 当前存在稳定性、安全性、工具兼容性和种子可用性等限制
- 🎯 主要作为概念验证展示Customization Hooks的潜力与BitTorrent技术可能性

---

### [模块：node:module API | Node.js v21.7.3 文档](https://nodejs.org/docs/latest-v21.x/api/module.html#customization-hooks)

**原文标题**: [Modules: node:module API | Node.js v21.7.3 Documentation](https://nodejs.org/docs/latest-v21.x/api/module.html#customization-hooks)

Node.js v21.7.3 文档中关于模块系统的核心 API 和自定义功能说明，重点介绍了 node:module 模块的接口与钩子机制。

- 📚 **模块对象** - 提供与 Module 实例交互的通用工具方法，支持 CommonJS 和 ES 模块
- 📦 **内置模块检测** - 通过 builtinModules 和 isBuiltin() 方法识别 Node.js 核心模块
- 🔗 **创建 require 函数** - createRequire() 可在 ES 模块中构造 CommonJS 风格的 require 方法
- ⚡ **同步 ESM 导出** - syncBuiltinESMExports() 同步内置 ES 模块与 CommonJS 导出的实时绑定
- 🎯 **模块注册机制** - register() 方法允许注册自定义解析和加载钩子
- 🔧 **自定义钩子系统** - 支持 initialize、resolve 和 load 三个核心钩子函数
- 🔄 **钩子链式调用** - 支持多个钩子注册，按后进先出顺序形成处理链
- 🌐 **线程隔离设计** - 钩子运行在独立线程，需通过消息通道与主线程通信
- 📝 **源映射支持** - 提供 SourceMap 类和相关方法，支持源代码调试映射
- 💡 **实用示例** - 包含 HTTPS 导入、代码转译、导入映射等实际应用场景

---

### [Node.js 24 成为长期支持版本：你需要了解的内容](https://nodesource.com/blog/nodejs-24-becomes-lts)

**原文标题**: [Node.js 24 Becomes LTS: What You Need to Know](https://nodesource.com/blog/nodejs-24-becomes-lts)

Node.js 24版本正式进入长期支持阶段，带来更强的安全默认设置、更严格的运行时验证、增强的Web API支持以及模块系统优化，同时N|Solid平台已全面兼容该版本并提供企业级观测能力。

- 🔒 **安全升级** - 默认采用OpenSSL 3.5并提升安全等级至2级，禁用弱加密算法
- 🛡️ **运行时强化** - Buffer/fs/timers等核心API增加严格参数验证，提前拦截错误
- 🌐 **Web标准对齐** - 新增CloseEvent/Float16Array等全局对象，完善fetch规范
- 📦 **模块系统优化** - ESM与CommonJS互操作性提升，默认导出module.exports
- 🚀 **流处理增强** - 改进stream错误传播机制，readline支持Unicode行分隔符
- 🔧 **构建要求更新** - 编译环境需GCC 12.2+或Xcode 16.1+，采用C++20标准
- 📋 **平台支持调整** - 停止32位Windows/armv7支持，macOS最低要求13.5
- ⚡ **N|Solid集成** - 6.0.2版本全面兼容Node.js 24，提供gRPC通信优化和持续性能分析
- 🗓️ **长期支持规划** - 维护至2028年4月，与Node.js 22/20版本形成阶梯式支持体系

---

### [Node.js — Node.js v24.11.0（长期支持版）](https://nodejs.org/en/blog/release/v24.11.0)

**原文标题**: [Node.js — Node.js v24.11.0 (LTS)](https://nodejs.org/en/blog/release/v24.11.0)

Node.js 24.11.0版本正式进入长期支持阶段，代号为"Krypton"，将持续获得更新支持至2028年4月。

- 🚀 Node.js 24.11.0版本进入长期支持阶段，代号"Krypton"
- 📅 LTS支持将持续至2028年4月底
- 🔄 除更新元数据外，与24.10.0版本无功能变化
- ⚠️ 已知问题：Buffer.allocUnsafe意外返回零填充缓冲区
- 🔧 计划在下个LTS版本修复该问题以恢复文档定义行为
- 🌐 提供Windows、macOS、Linux等多平台安装包和二进制文件
- 📚 完整文档和源代码已同步发布

---

### [Node.js — Node.js v25.1.0（当前版本）](https://nodejs.org/en/blog/release/v25.1.0)

**原文标题**: [Node.js — Node.js v25.1.0 (Current)](https://nodejs.org/en/blog/release/v25.1.0)

Node.js v25.1.0 版本发布，主要包含 HTTP 服务器优化、SQLite 防御标志支持、新增监视配置命名空间等特性更新，同时涵盖依赖项升级、文档修正和多项测试改进。

- 🚀 HTTP 服务器新增 optimizeEmptyRequests 选项以优化空请求处理
- 🛡️ SQLite 模块支持设置 defensive 标志增强安全性  
- ⚙️ 新增 src 监视配置命名空间便于运行时配置管理
- 📦 升级核心依赖项（simdjson 4.0.7、corepack 0.34.1、V8 引擎）
- 📚 完善文档内容（DNS 解析类型、装饰器策略说明等）
- 🧪 新增多个基准测试模块（vm.SourceTextModule、leaf source text）
- 🔧 工具链优化（生成轻量归档、测试通配符执行加速）
- 🐛 修复多项问题（快照序列化时机、内存泄漏、类型定义）
- 🌐 支持 Inspector 协议 WebSocket 握手响应
- 📦 提供全平台安装包（Windows/macOS/Linux/AIX）

---

### [加强npm安全性：认证与令牌管理的重要更新 - GitHub更新日志](https://github.blog/changelog/2025-09-29-strengthening-npm-security-important-changes-to-authentication-and-token-management/)

**原文标题**: [Strengthening npm security: Important changes to authentication and token management - GitHub Changelog](https://github.blog/changelog/2025-09-29-strengthening-npm-security-important-changes-to-authentication-and-token-management/)

npm将于2025年9月至11月期间实施三项关键安全改进措施，旨在强化软件包生态系统安全防护能力。

- 🔐 精细化令牌有效期调整：新创建的写入权限令牌默认有效期缩短至7天，最长不超过90天
- 🚫 经典令牌全面停用：五周内逐步撤销所有传统经典令牌并永久禁用生成功能
- 🔑 双因素认证升级：停止新增TOTP验证方式，推荐迁移至WebAuthn/通行密钥方案
- ⏳ 分阶段实施计划：10月初启用新令牌规则，11月中旬完成经典令牌淘汰
- 🤝 推荐信任发布模式：支持GitHub Actions/GitLab CI/CD的OIDC临时凭证机制
- 📚 官方支持渠道：提供更新文档、社区讨论区和专属支持邮箱协助用户迁移

---

### [Bun — 一款快速的全能JavaScript运行时](https://bun.sh/)

**原文标题**: [Bun — A fast all-in-one JavaScript runtime](https://bun.sh/)

Bun v1.3.1 是一个高性能的 JavaScript 全栈工具包，具备渐进式采用特性，包含运行时、打包器、测试运行器和包管理器，并致力于实现完全的 Node.js 兼容性。

- 🚀 性能表现卓越：在多项基准测试中，Bun 在打包速度、HTTP 请求处理、WebSocket 消息传输和数据库查询方面均显著领先于 Node.js 和 Deno
- 🧩 渐进式采用：可单独使用 bun test 或 bun install 等工具，也可完整采用其全栈解决方案
- 🔧 全功能工具包：集成了 JavaScript 运行时、打包器、测试运行器和包管理器
- 📦 高效打包：在打包 10,000 个 React 组件时仅需 269.1 毫秒，比 esbuild 快约 2 倍
- 🌐 网络性能优异：Express.js 测试达到 59,026 请求/秒，WebSocket 处理达 2,536,227 消息/秒
- ⚡ 数据库性能：在负载测试中达到 28,571 查询/秒，比 Node.js 快约 2 倍
- 🔄 完全兼容：致力于实现 100% Node.js 兼容性，支持在现有 Node.js 项目中逐步采用

---

### [Vercel 现已支持 Bun 运行时 | Bun 博客](https://bun.com/blog/vercel-adds-native-bun-support)

**原文标题**: [Vercel now supports the Bun Runtime | Bun Blog](https://bun.com/blog/vercel-adds-native-bun-support)

Vercel现已全面支持Bun运行时，开发者可在部署时选择使用Bun作为JavaScript运行环境。该功能目前处于公开测试阶段，支持Next.js、Hono等框架，通过简单配置即可启用。

- 🚀 只需在vercel.json中添加"bunVersion": "1.x"即可启用Bun运行时
- 📦 支持原生调用Bun API（Bun.SQL、Bun.S3等）和Web API
- ⚡ 基于Zig语言开发，具有更低的内存和CPU占用
- 🔧 Next.js项目需在package.json脚本中添加bun --bun前缀
- 🌐 支持在Server Functions和React Server Components中直接使用Bun功能
- 🧪 当前为公开测试版，后续将扩展更多框架支持
- 📚 提供完整文档支持和Discord社区协助

---

### [Fastify 零配置支持 - Vercel](https://vercel.com/changelog/zero-configuration-support-for-fastify)

**原文标题**: [Zero-configuration support for Fastify - Vercel](https://vercel.com/changelog/zero-configuration-support-for-fastify)

Vercel现已支持Fastify框架部署，提供零配置的服务器端应用托管服务。

- 🚀 Vercel平台正式集成Fastify框架，实现零配置快速部署
- 💻 支持通过server.ts文件创建轻量级Fastify应用（含示例代码）
- ⚡ 默认启用Fluid计算架构，根据流量自动弹性伸缩
- 💰 采用Active CPU计费模式，按实际使用量付费
- 📚 提供官方部署指南和详细技术文档支持

---

### [在Hugging Face空间中运行Node.js](https://blog.tomayac.com/2025/11/03/running-nodejs-in-a-hugging-face-space/)

**原文标题**: [Running Node.js in a Hugging Face Space](https://blog.tomayac.com/2025/11/03/running-nodejs-in-a-hugging-face-space/)

本文介绍了如何在Hugging Face Space中创建可长期使用的Node.js服务器模板，作为Glitch关闭后的替代方案。

- 🐢 使用Docker SDK创建空白Space，选择免费方案
- 📦 通过package.json配置Express.js最新版本依赖
- 🐳 基于lts-alpine标签创建轻量级Dockerfile
- ⚡ 默认监听7860端口并动态显示运行版本信息
- 🔄 复制模板后可固定Node.js和Express.js版本号
- 🌐 支持git克隆本地开发和自定义响应头配置
- 🚀 应用运行在独立浏览器上下文而非iframe中

---

### [Glitch即将迎来重大更新](https://blog.glitch.com/post/changes-are-coming-to-glitch)

**原文标题**: [Important changes are coming to Glitch](https://blog.glitch.com/post/changes-are-coming-to-glitch)

Glitch平台宣布将停止应用托管服务，这是为适应开发生态变化而做出的战略调整，旨在更有效地服务开发者社区。

- 🗓️ 2025年7月8日停止项目托管和用户资料服务，仪表盘保留至年底供代码下载
- 🔗 新增子域名重定向功能，确保现有链接持续有效至2026年底
- 💰 立即停止新Pro订阅，现有订阅服务延续至7月并退还未使用费用
- 📚 正在编写项目迁移指南，社区论坛提供技术支持和交流平台
- 🌍 因运维成本攀升及新兴平台涌现，决定聚焦更具价值的服务方向
- ✉️ 创始人开放邮箱anil@glitch.com接收社区反馈

---

### [Spaces - 拥抱未来](https://huggingface.co/spaces)

**原文标题**: [Spaces - Hugging Face](https://huggingface.co/spaces)

该页面展示了AI应用平台上的各类工具和项目，涵盖图像生成、视频处理、文本分析等人工智能技术领域，并按运行状态和热度排序。

- 🖼️ 图像生成与编辑工具，如FIBO和ImageEditPro，支持文本或图像生成及增强功能
- 🎬 视频处理应用，包括Wan2.2系列和LongCat，实现文本或图像到视频的转换
- 📝 文本分析与生成工具，如文本摘要、代码生成和金融洞察提取
- 🔧 开发与训练资源，提供LLM训练指南、模型微调和数据集创建方法
- 🎨 多媒体创作工具，支持语音合成、3D建模和风格转换等功能
- 🤖 智能应用演示，包括OCR识别、问答系统和机器人学习教程

---

### [使用Foxit PDF Services API自动将Office文档转换为PDF - Foxit](https://developer-api.foxit.com/developer-blogs/use-cases-workflow-examples/automated-document-pipelines/convert-office-docs-to-pdfs-automatically-with-foxit-pdf-services-api/?utm_source=cooperpress&utm_medium=Display&utm_campaign=11-04-25)

**原文标题**: [Convert Office Docs to PDFs Automatically with Foxit PDF Services API - Foxit](https://developer-api.foxit.com/developer-blogs/use-cases-workflow-examples/automated-document-pipelines/convert-office-docs-to-pdfs-automatically-with-foxit-pdf-services-api/?utm_source=cooperpress&utm_medium=Display&utm_campaign=11-04-25)

在API World 2025展会上，我们展示了如何利用Foxit API构建可审计的智能文档工作流，通过实际演示呈现了从文档生成到自动化处理的全流程解决方案。

- 📄 现场演示了基于Foxit PDF服务和文档生成API的可审计文档自动化系统
- 🤖 展示了AI技术如何驱动从简历生成到互动涂鸦等多样化文档应用
- 🌐 通过API World平台与开发者深入交流，分享创新理念和技术实践
- 🔧 重点介绍如何构建具备审计追踪功能的智能文档处理工作流
- 💡 呈现了Jorge Euceda在大会现场的实机操作演示全流程

---

### [我们为何从Python迁移至Node.js](https://blog.yakkomajuri.com/blog/python-to-node)

**原文标题**: [Why we migrated from Python to Node.js](https://blog.yakkomajuri.com/blog/python-to-node)

一家初创公司在发布一周后将后端从Python迁移至Node.js，主要因为Python异步编程生态不成熟导致开发效率低下。

- 🚀 为应对高并发需求放弃Django框架，因Python异步支持存在先天缺陷
- ⚡ 迁移后吞吐量提升3倍，且为未来并行处理预留优化空间  
- 🔄 统一代码库结构，将Express服务与后台Worker合并提升维护性
- 🛠️ 选用MikroORM替代Django ORM，保持合理的开发体验
- 📉 失去Python生态优势，但通过TypeScript SDK维持核心功能
- 🧪 迁移过程促使测试覆盖率大幅提升
- ⏱️ 耗时3天完成重写，早期迁移降低技术债务累积

---

### [MikroORM：基于数据映射器、工作单元和身份映射模式的Node.js TypeScript ORM。 | MikroORM](https://mikro-orm.io/)

**原文标题**: [MikroORM: TypeScript ORM for Node.js based on Data Mapper, Unit of Work and Identity Map patterns. | MikroORM](https://mikro-orm.io/)

MikroORM 是一个功能强大的 Node.js ORM 框架，提供自动事务管理、多数据库支持、数据库同步工具、数据填充、查询优化等特性，帮助开发者高效进行数据库操作。

- 🔄 自动事务处理：通过 em.flush() 自动将计算变更包装在数据库事务中
- 📝 智能实体定义：通过源码分析自动推断 TypeScript 类型，避免重复定义
- 🗄️ 多数据库支持：兼容 MongoDB、MySQL、PostgreSQL、SQLite 等主流数据库
- 🔄 数据库同步：支持通过 SchemaGenerator 快速生成原型，Migrator 生成迁移差异，EntityGenerator 从数据库逆向生成实体
- 🌱 数据填充：通过 Seeder 和工厂模式轻松生成任意规模和形状的假数据
- ⚡ 自动批处理：UnitOfWork 自动批量处理所有插入、更新、删除等查询操作
- 🎯 事件系统：强大的事件机制支持实体生命周期钩子和 UnitOfWork 自定义处理
- 🔍 智能查询构建器：支持元数据感知和自动连接的 QueryBuilder，提供灵活查询
- 🎛️ 全局过滤器：可定义全局过滤器实现多租户数据隔离、软删除实体自动隐藏等功能

---

### [为什么在 JavaScript 中 NaN 不等于 NaN（及其背后的 IEEE 754 标准故事） | Piotr Zarycki - 编程博客](https://pzarycki.com/en/posts/js-nan/)

**原文标题**: [Why NaN !== NaN in JavaScript (and the IEEE 754 story behind it) | Piotr Zarycki - Programming Blog](https://pzarycki.com/en/posts/js-nan/)

JavaScript中的NaN不等于NaN源于IEEE 754浮点数标准的硬件级设计，该标准通过特殊数值表示无效运算结果，并利用自比较特性实现错误检测。

- 🔍 NaN在JavaScript中属于number类型，但代表无效数学运算结果
- ⚙️ 硬件层面通过ucomisd指令实现NaN检测，设置标志位进行判断
- 🌍 IEEE 754标准于1985年制定，统一了各硬件厂商的浮点数处理方式
- 🎯 NaN !== NaN是刻意设计，便于在没有isnan()函数时检测异常值
- 🔄 任何涉及NaN的运算都会返回NaN，实现错误传播机制
- 🛡️ 相比程序崩溃或返回错误值，NaN能保持程序继续运行
- 📊 浮点数运算中0/0、∞-∞等特殊情况都会产生NaN
- 💡 使用Number.isNaN()是检测NaN的推荐方法

---

### [在Node 24中使用URLPattern作为无框架路由器](https://jsdev.space/urlpattern-router-node24/)

**原文标题**: [Using URLPattern as a Framework-Free Router in Node 24](https://jsdev.space/urlpattern-router-node24/)

URLPattern 是 Node.js 24 和浏览器中原生支持的跨平台路由解决方案，无需依赖任何框架即可实现统一的路由匹配逻辑。

- 🌐 **跨平台支持** - 在 Node.js 24 和主流浏览器中均可直接使用，无需导入依赖
- 🔧 **灵活路由匹配** - 支持协议、主机名、路径名等 URL 各部分匹配，提供命名参数和正则验证
- 📦 **轻量级路由器** - 通过 PathRule 和 SmartRouter 类构建无依赖的类型安全路由器
- 🛠️ **多环境适配** - 同一套路由规则可同时用于 Service Worker 和 Node.js HTTP 服务器
- ⚡ **性能优化** - 建议预编译 URLPattern 实例复用，避免每个请求重新创建
- 🔒 **安全考虑** - 避免使用用户提供的正则表达式，仅匹配自有域名
- 📊 **基准测试** - 性能足以满足生产需求，虽不及高度优化的专用路由器
- 🔄 **统一处理契约** - 客户端和服务端使用相同的处理上下文和响应格式
- 🎯 **实用场景** - 特别适合轻量级 API、服务工作者和需要共享客户端-服务端逻辑的应用

---

### [GitHub - sindresorhus/image-dimensions：获取图片尺寸](https://github.com/sindresorhus/image-dimensions)

**原文标题**: [GitHub - sindresorhus/image-dimensions: Get the dimensions of an image](https://github.com/sindresorhus/image-dimensions)

这是一个用于获取图像尺寸的JavaScript工具库，支持多平台运行并涵盖主流图像格式

- 📏 支持JPEG/PNG/GIF/WebP/AVIF/HEIF等常见图像格式的尺寸检测
- 🌐 兼容浏览器/Node.js/Bun/Deno等现代JavaScript运行环境
- ⚡ 通过流式处理仅读取图像头部数据，无需加载完整文件
- 📦 提供两种API：imageDimensionsFromStream（流处理）和imageDimensionsFromData（内存数据处理）
- 🛠️ 附带命令行工具，可通过npx直接使用
- 📄 返回包含宽度、高度和图像类型的对象信息
- 🆓 零依赖、体积小巧，采用MIT开源协议
- ⚠️ 注意不包含EXIF方向信息处理，返回原始像素尺寸

---

### [GitHub - image-size/image-size: 用于检测图像尺寸的Node模块](https://github.com/image-size/image-size)

**原文标题**: [GitHub - image-size/image-size: Node module for detecting image dimensions](https://github.com/image-size/image-size)

一个用于检测图像尺寸的Node.js模块，支持多种图像格式，具有零依赖、轻量级和高性能的特点。

- 🖼️ 支持多种图像格式，包括BMP、GIF、JPEG、PNG、SVG、WebP等主流格式
- ⚡ 零依赖设计，快速读取仅需处理图像头部信息，内存占用极小
- 📁 支持从缓冲区、本地文件和URL获取图像尺寸
- 🔄 提供异步文件读取和并发控制功能，默认并发限制为100
- 📏 对于多图像文件（如ICO、CUR）可返回所有图像的尺寸信息
- 🎯 支持禁用特定图像类型和获取JPEG方向信息
- 📦 提供命令行工具和TypeScript类型支持
- ⚠️ 存在部分限制：SVG不支持百分比值，某些格式需要完整头部缓冲区
- 📄 采用MIT开源协议，被超过600万个项目使用

---

### [GitHub - privatenumber/type-flag: ⛳️ Node.js 类型化命令行参数解析器](https://github.com/privatenumber/type-flag)

**原文标题**: [GitHub - privatenumber/type-flag: ⛳️ Typed command-line arguments parser for Node.js](https://github.com/privatenumber/type-flag)

type-flag 是一个轻量级、强类型的 Node.js 命令行参数解析库，具有无依赖、可摇树优化等特点，支持 TypeScript 类型推断和多种高级解析功能。

- 🚀 **轻量高效** - 无第三方依赖，压缩后仅 1.4kB，支持摇树优化
- ⚡ **快速上手** - 简单 API 设计，支持 `typeFlag` 和 `getFlag` 两种使用方式
- 🎯 **强类型支持** - 完整的 TypeScript 类型推断，自动映射命令行参数到指定类型
- 🔧 **丰富功能** - 支持数组类型、别名、默认值、未知参数处理、自定义分隔符等
- 📝 **灵活配置** - 可自定义类型解析函数，支持参数验证和复杂数据结构处理
- 🛠️ **高级特性** - 支持标志值分隔符（=、:、.）、参数截断、argv 数组变异等
- 📦 **生态集成** - 作为 Cleye CLI 开发工具的基础解析引擎

---

### [Electron 39.0.0 版本发布 | Electron](https://www.electronjs.org/blog/electron-39-0)

**原文标题**: [Electron 39.0.0 | Electron](https://www.electronjs.org/blog/electron-39-0)

Electron 39.0.0 正式发布，包含 Chromium、Node.js 和 V8 的核心组件升级，新增多项功能改进并引入破坏性变更。

- 🚀 核心组件版本升级：Chromium 142.0.7444.52、Node.js 22.20.0、V8 14.2
- 🛡️ ASAR 完整性校验功能结束实验阶段，现已稳定可用
- ✨ 新增硬件加速检测、HDR色彩支持、Linux系统主题色获取等实用功能
- ⚠️ 存在三项破坏性变更：弃用--host-rules参数、窗口弹窗默认可调整大小、共享纹理数据结构更新
- 📅 Electron 36.x.y 系列版本已停止官方支持
- 🔮 开发团队将持续跟进Chromium/Node/V8的生态演进

---

### [Node.js — Node.js v22.20.0（长期支持版）](https://nodejs.org/en/blog/release/v22.20.0)

**原文标题**: [Node.js — Node.js v22.20.0 (LTS)](https://nodejs.org/en/blog/release/v22.20.0)

Node.js v22.20.0 (LTS) 版本发布，代号"Jod"，包含 OpenSSL 升级至 3.5.2 以延长支持周期至 2027-04-30，并引入多项功能增强与错误修复。

- 🔐 OpenSSL 更新至 3.5.2，确保长期支持兼容性
- 🌐 HTTP/2 支持原始头数组及代理保持活动超时缓冲选项
- 📦 SEA（单可执行应用）新增 execArgv 配置与扩展支持
- 🔄 流处理增加 Brotli 压缩与解压缩支持
- 🧪 测试运行器引入对象属性模拟功能
- 👷 Worker 线程新增 CPU 性能分析 API
- 🛠️ 多项模块加载、文件系统与加密功能优化与修复

---

### [GitHub - sindresorhus/on-change：监听对象或数组变化的工具](https://github.com/sindresorhus/on-change)

**原文标题**: [GitHub - sindresorhus/on-change: Watch an object or array for changes](https://github.com/sindresorhus/on-change)

这是一个用于监听对象或数组变化的JavaScript库，通过Proxy API实现递归监听，支持深度属性修改检测。

- 🎯 基于Proxy API实现对象/数组变化监听
- 🔍 支持递归检测深度属性修改（如obj.a.b[0].c）
- 📦 通过npm安装：npm install on-change
- ⚙️ 提供丰富配置选项：浅层监听、自定义相等比较、忽略特定键等
- 🎪 回调函数可获取路径、新值、旧值和操作详情
- 🔄 支持取消监听和访问原始对象
- 💡 典型应用场景：自动保存对象状态变化
- 📚 相关项目：known、negative-array等同类Proxy工具库
- 📄 采用MIT开源协议，支持Node.js环境

---

### [ConfigCat - 团队功能特性管理服务](https://configcat.com/promotions/node-weekly/?utm_source=cooperpress_newsletter&utm_medium=sponsor&utm_campaign=cooperpress_node_202510)

**原文标题**: [ConfigCat - Feature Flag Service for Teams](https://configcat.com/promotions/node-weekly/?utm_source=cooperpress_newsletter&utm_medium=sponsor&utm_campaign=cooperpress_node_202510)

ConfigCat是一个功能开关管理平台，帮助开发团队通过功能标志控制功能发布流程。

- 🚀 无风险功能发布 - 支持渐进式功能上线和即时回滚
- ⚡ 快速集成 - 10分钟完成设置，提供永久免费方案
- 🔒 安全隐私 - 客户端评估标志，不收集用户数据
- 💰 透明定价 - 提供免费版和三个付费层级（Pro/Smart/Enterprise）
- 🔧 技术友好 - 支持多环境配置、API集成和开源框架
- 🌟 客户认可 - 在G2 Crowd和TrustRadius获得高分评价
- 🆓 免费起步 - 包含10个功能标志和500万次配置下载
- 🔄 无厂商锁定 - 支持数据导出和OpenFeature标准

---

### [ConfigCat - 团队功能特性开关服务](https://configcat.com/promotions/node-weekly/?utm_source=cooperpress_newsletter&utm_medium=sponsor&utm_campaign=cooperpress_node_202510)

**原文标题**: [ConfigCat - Feature Flag Service for Teams](https://configcat.com/promotions/node-weekly/?utm_source=cooperpress_newsletter&utm_medium=sponsor&utm_campaign=cooperpress_node_202510)

ConfigCat是一个功能开关管理平台，帮助开发团队通过功能标志控制功能发布流程。

- 🚀 无风险功能发布 - 支持渐进式发布和即时关闭问题功能
- ⚡ 快速集成 - 10分钟完成设置，提供永久免费方案
- 🔒 安全隐私 - 客户端评估标志，不收集用户数据
- 💰 透明定价 - 提供免费到企业级方案，支持25%优惠码NODE25
- 🔧 技术友好 - 支持多环境管理、OpenFeature标准和API集成
- 🌟 客户认可 - 获多家企业好评，在G2和TrustRadius评分优异
- 📊 灵活扩展 - 从10个功能标志到无限扩展，满足不同规模需求

---

### [GitHub - ekalinin/sitemap.js：Node.js 站点地图生成框架](https://github.com/ekalinin/sitemap.js)

**原文标题**: [GitHub - ekalinin/sitemap.js: Sitemap-generating framework for node.js](https://github.com/ekalinin/sitemap.js)

这是一个用于Node.js的站点地图生成框架，支持流式处理和多种高级功能。

- 🗺️ 支持生成标准站点地图和索引文件，可处理超过5万个URL的大型网站
- ⚡ 提供CLI工具和编程接口两种使用方式，支持一次性生成和持续更新
- 🔄 基于流式处理，内存效率高，可处理海量URL数据
- 🛠️ 丰富的配置选项，支持图片、视频、多语言链接等扩展功能
- 📦 支持Gzip压缩、XSL样式表自定义、XML命名空间配置
- 🎯 可与Express等Web框架集成，提供动态站点地图服务
- 🔍 支持站点地图解析和过滤，可选择性处理特定URL
- 📄 遵循站点地图协议标准，生成符合规范的XML文件
- 🆓 采用MIT开源协议，拥有活跃的社区维护

---

### [GitHub - sverweij/dependency-cruiser：依赖关系巡航器 - 验证并可视化依赖项。自定义规则，支持JavaScript、TypeScript、CoffeeScript，兼容ES6、CommonJS、AMD模块规范。](https://github.com/sverweij/dependency-cruiser)

**原文标题**: [GitHub - sverweij/dependency-cruiser: Validate and visualize dependencies. Your rules. JavaScript, TypeScript, CoffeeScript. ES6, CommonJS, AMD.](https://github.com/sverweij/dependency-cruiser)

这是一个用于分析和可视化JavaScript、TypeScript、CoffeeScript等项目依赖关系的开源工具，支持自定义依赖规则验证和多种格式的依赖图生成。

- 🔍 **依赖验证工具** - 可检测循环依赖、缺失依赖等违规情况
- 📊 **可视化依赖图** - 支持生成SVG、HTML、Mermaid等多种格式的依赖图表
- ⚙️ **自定义规则** - 通过配置文件定义项目特定的依赖关系规则
- 🛠️ **多语言支持** - 兼容JavaScript、TypeScript、CoffeeScript、JSX、TSX等
- 📦 **包管理器集成** - 支持npm、yarn、pnpm等主流包管理器
- 🔄 **持续维护** - 拥有6.2k星标，活跃开发和版本更新
- 📄 **开源协议** - 采用MIT许可，可自由使用和修改
- 🌐 **社区活跃** - 被4.6k+项目使用，拥有50+贡献者

---

### [pnpm 10.20 | pnpm](https://pnpm.io/blog/releases/10.20)

**原文标题**: [pnpm 10.20 | pnpm](https://pnpm.io/blog/releases/10.20)

pnpm 10.20版本更新内容概述

- 📋 `pnpm help` 新增 `--all` 参数，可列出全部命令 #8628
- 🕒 当 `latest` 版本不符合 `minimumReleaseAge` 要求时，自动选择符合成熟度要求的最高版本 #10100
- ⚡ `create` 命令不再验证补丁信息
- 🔄 切换 pnpm CLI 版本时自动禁用 `managePackageManagerVersions` 避免重复切换 #10063

---

### [GitHub - biggora/express-useragent：NodeJS用户代理中间件](https://github.com/biggora/express-useragent)

**原文标题**: [GitHub - biggora/express-useragent: NodeJS user-agent middleware](https://github.com/biggora/express-useragent)

这是一个用于Node.js的快速用户代理解析库，提供Express中间件和TypeScript支持，可在服务器端和浏览器端使用。

- 🚀 快速用户代理解析器，支持Express中间件和TypeScript类型定义
- 🌐 支持Node.js 18+和浏览器环境，提供轻量级IIFE包
- 📦 可通过npm安装：npm install express-useragent
- 🔧 提供多种导入方式：ESM命名导入、命名空间导入和CommonJS
- 🛠️ 主要API包括UserAgent构造函数、parse方法和express中间件方法
- 📱 解析结果包含设备类型、浏览器、操作系统等详细信息
- 📚 提供完整示例代码和迁移指南（v1.x到v2.x）
- 🧪 包含测试脚本、构建脚本和开发工具链
- 📄 采用MIT开源协议，欢迎贡献和问题报告

---

### [GitHub - jsdom/jsdom: 一个用于Node.js的多种Web标准的JavaScript实现](https://github.com/jsdom/jsdom)

**原文标题**: [GitHub - jsdom/jsdom: A JavaScript implementation of various web standards, for use with Node.js](https://github.com/jsdom/jsdom)

jsdom是一个用于Node.js的纯JavaScript实现的Web标准库，主要模拟WHATWG DOM和HTML标准，适用于测试和网页抓取场景。

- 🚀 **核心功能**：提供完整的DOM和HTML标准实现，支持在Node.js环境中模拟浏览器行为
- ⚙️ **配置选项**：支持URL、引用来源、内容类型等参数设置，可自定义资源加载和脚本执行策略
- ⚡ **脚本执行**：默认禁用内联脚本，可通过`runScripts`选项安全控制脚本执行权限
- 🎯 **资源加载**：支持配置资源加载器，可自定义代理、SSL验证和用户代理等参数
- 📊 **虚拟控制台**：提供完整的控制台系统，支持消息转发和自定义错误处理
- 🍪 **Cookie管理**：集成tough-cookie实现完整的Cookie存储和管理功能
- 🔧 **高级API**：提供序列化、节点定位、VM上下文访问等实用方法
- 📁 **便捷接口**：支持从URL、文件或HTML片段快速创建DOM实例
- 🎨 **Canvas支持**：通过canvas包扩展提供Canvas API功能
- 🔍 **编码检测**：自动检测和处理不同编码格式的输入数据

---

### [Immer 入门指南 | Immer](https://immerjs.github.io/immer/)

**原文标题**: [Introduction to Immer | Immer](https://immerjs.github.io/immer/)

Immer是一个简化JavaScript不可变数据操作的小型工具包，通过代理草案机制自动处理数据更新与拷贝，大幅减少样板代码。

- 🎯 简化不可变数据操作，支持普通JS对象/数组/集合
- 🚫 自动检测意外变更并抛出错误
- 📝 使用草案代理记录变更，自动生成不可变新状态
- 🏆 荣获2019年React开源突破奖和JS开源影响力奖
- 📚 提供免费视频教程和深度课程
- 🧩 完美兼容React状态管理和Redux
- ⚡ 仅3KB大小，支持结构共享和对象冻结
- 🔄 通过produce函数实现直观的变更逻辑

---

### [GitHub - express-rate-limit/express-rate-limit：Express Web 服务器的基本限速中间件](https://github.com/express-rate-limit/express-rate-limit)

**原文标题**: [GitHub - express-rate-limit/express-rate-limit: Basic rate-limiting middleware for the Express web server](https://github.com/express-rate-limit/express-rate-limit)

这是一个用于Express框架的基础速率限制中间件，用于限制重复请求以保护API和端点安全。

- 🛡️ 基础速率限制中间件，适用于Express Web服务器
- 📦 可通过npm安装，每周下载量达492k+
- ⚙️ 支持自定义配置：时间窗口、请求限制、响应消息等
- 🗄️ 内置内存存储，支持多种外部数据存储
- 🔧 与express-slow-down和ratelimit-header-parser兼容
- 🌐 支持IPv6子网配置，可调节限制粒度
- 📊 提供标准RateLimit头部信息支持
- 🐛 当前项目有6个未解决问题和2个拉取请求
- 📄 采用MIT开源许可证，由Nathan Friedly和Vedant K维护
- ⭐ GitHub上获得3.2k星标，239个复刻

---

### [GitHub - lirantal/npq：在预安装阶段通过审计安全地安装npm包](https://github.com/lirantal/npq)

**原文标题**: [GitHub - lirantal/npq: safely install npm packages by auditing them pre-install stage](https://github.com/lirantal/npq)

npq是一个在npm包安装前进行安全检查的工具，通过多种检测机制识别潜在风险，最终交由包管理器完成安装

- 🔍 检查Snyk漏洞数据库中的公开安全漏洞
- 📅 验证软件包在npm的发布时长（超过22天）
- 📊 分析软件包月度下载量（超过20次）
- 📖 确认软件包包含README文件
- ⚖️ 验证软件包包含LICENSE文件
- ⚠️ 检测软件包是否包含预安装/后安装脚本
- 🌐 检查软件包仓库URL有效性
- 📧 验证维护者邮箱域名有效性
- 🔐 支持软件包签名和来源证明验证
- 🆕 检测新版本发布时长（7天内警告）
- 🖥️ 监控新增命令行二进制文件
- 🔤 识别仿冒热门软件包的拼写错误攻击
- 🚫 检查软件包是否已被弃用
- 🛡️ 可通过环境变量禁用特定检查项
- 💻 支持npm、yarn、pnpm等包管理器
- 🎯 提供dry-run模式仅检查不安装
- 📝 支持纯文本输出模式

---

### [GitHub - isaacs/rimraf：Node.js 的 `rm -rf` 工具](https://github.com/isaacs/rimraf)

**原文标题**: [GitHub - isaacs/rimraf: A `rm -rf` util for nodejs](https://github.com/isaacs/rimraf)

这是一个用于 Node.js 的跨平台文件删除工具，功能类似 Unix 系统的 rm -rf 命令

- 🗑️ 提供多种删除实现方式：自动选择最佳方案/原生 Node.js 实现/手动 JavaScript 实现
- ⚡ 支持同步和异步操作，异步版本性能更优
- 🔧 丰富的配置选项：包含重试机制、过滤函数、中止信号等
- 🌍 跨平台支持，特别针对 Windows 系统优化了删除策略
- 📦 可通过 npm 安装使用，支持 ES6 模块和 CommonJS
- 🛡️ 提供命令行界面，支持多种参数和交互模式
- 📚 采用 BlueOak-1.0.0 许可证，项目活跃度高

---

### [GitHub - vadimdemedes/ink：🌈 用于交互式命令行应用的 React 框架](https://github.com/vadimdemedes/ink)

**原文标题**: [GitHub - vadimdemedes/ink: 🌈 React for interactive command-line apps](https://github.com/vadimdemedes/ink)

Ink是一个基于React的命令行界面(CLI)应用开发框架，允许开发者使用熟悉的React组件化方式构建交互式命令行应用。

- 🎯 **React渲染器** - 将React组件渲染到命令行界面，支持所有React特性
- 🎨 **Flexbox布局** - 使用Yoga引擎实现类似CSS的Flexbox布局系统
- 📦 **丰富组件** - 提供Text、Box、Newline、Spacer等核心组件
- ⌨️ **输入处理** - 通过useInput钩子简化用户输入处理
- 🎛️ **焦点管理** - 支持Tab键焦点切换和程序化焦点控制
- 🧪 **测试友好** - 提供ink-testing-library用于组件测试
- ♿ **无障碍支持** - 基础屏幕阅读器支持和ARIA属性
- 🔧 **开发工具** - 支持React Devtools调试
- 📚 **活跃生态** - 被GitHub Copilot CLI、Cloudflare Wrangler等知名项目使用
- 🛠️ **TypeScript** - 主要使用TypeScript开发，提供良好类型支持

---

### [ESLint v9.39.1 发布 - ESLint - 可插拔 JavaScript 代码检查工具](https://eslint.org/blog/2025/11/eslint-v9.39.1-released/)

**原文标题**: [ESLint v9.39.1 released - ESLint - Pluggable JavaScript Linter](https://eslint.org/blog/2025/11/eslint-v9.39.1-released/)

ESLint v9.39.1 作为补丁版本发布，修复了前版因规则访问器参数传递变更导致的第三方规则兼容性问题，并同步更新了文档与依赖项。

- 🐛 修复了 v9.39.0 中规则访问器意外传入两个参数导致 @typescript-eslint/unified-signatures 等第三方规则失效的问题  
- 🔧 恢复 JavaScript/TypeScript 语言访问器仅接收单节点参数的原有行为  
- 📚 文档新增关于 extends 与级联配置使用场景的说明章节  
- 📦 同步更新 @eslint/js 及相关依赖至兼容版本  
- 🧪 完善版本测试流程以适配 ESLint v10 的测试需求

---

