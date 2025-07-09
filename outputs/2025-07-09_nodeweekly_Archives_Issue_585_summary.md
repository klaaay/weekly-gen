### [Node 周刊第 585 期：2025 年 7 月 8 日](https://nodeweekly.com/issues/585)

**原文标题**: [Node Weekly Issue 585: July 8, 2025](https://nodeweekly.com/issues/585)

概述总结  
- 📧 提供订阅服务，可随时退订，保障邮箱安全  
- 🔧 JSON 修复工具，支持处理异常 JSON 数据，适用于 LLM 输出或非标准 JSON  
- 🚀 Memetria 提供优化的 Redis 和 Valkey 托管服务，提升 Node.js 应用性能  
- 🐛 使用代码点安全截断解决 Node 中 Emoji 截断问题  
- 📚 Node.js 团队正在改进 API 文档设计和构建工具  
- 💰 比较 40 多家云服务提供商的数据出口费用  
- 🎨 构建 AI 驱动的颜色搜索引擎教程  
- 🤖 创建 MCP 服务器连接 AI 助手与实时天气数据  
- 🔍 区分普通函数与箭头函数的差异  
- 🌐 检查应用是否真正在线的方法  
- 🛠️ Bruno：轻量级 HTTP API 测试 IDE  
- 🧵 Poolifier 5.0 支持 Worker 线程和集群工作池  
- 📊 AppSignal 帮助快速诊断 Node.js 应用性能问题  
- 🤖 grammY：简单易用的 Telegram 机器人框架  
- 🔥 0x 6.0：单命令生成 Node 火焰图  
- ⚙️ Babel 7.28.0 新增 TypeScript 配置支持和 ES2026 资源管理  
- 📌 PinMe CLI 工具免费部署静态站点  
- 🐱 ConfigCat 功能标志服务优惠 25%  
- 🦕 Deno 2.4 发布，改进 Node.js API 支持  
- 🏌️ JS1024 代码高尔夫比赛开放提交  
- 🦀 JavaScript 工具逐渐转向 Rust 开发  
- ⚡ Rspack 1.4 支持浏览器运行  
- 💻 微软开源 GitHub Copilot Chat 扩展

---

### [GitHub - josdejong/jsonrepair: 修复无效的 JSON 文档](https://github.com/josdejong/jsonrepair)

**原文标题**: [GitHub - josdejong/jsonrepair: Repair invalid JSON documents](https://github.com/josdejong/jsonrepair)

jsonrepair 是一个用于修复无效 JSON 文档的库，支持多种修复功能，包括添加缺失的引号、转义字符、逗号等，并支持流式处理大型文档。

- 🛠️ 修复功能：支持修复缺失引号、转义字符、逗号、闭合括号等常见 JSON 错误。
- 🔄 流式处理：支持处理无限大的 JSON 文档，适用于 Node.js 环境。
- 📦 多格式支持：提供 ESM、UMD 和 CommonJS 格式的构建版本。
- 🐍 Python 支持：通过 PythonMonkey 在 Python 中使用。
- 📜 CLI 工具：提供命令行工具，支持文件修复和流式处理。
- 🔍 替代方案：提供类似库的链接，如 dirty-json。
- 🏗️ 开发支持：提供详细的开发脚本和测试流程。
- 📄 许可证：基于 ISC 许可证发布。

---

### [jsonrepair 游乐场](https://josdejong.github.io/jsonrepair/)

**原文标题**: [jsonrepair playground](https://josdejong.github.io/jsonrepair/)

JSON 修复工具，用于修正无效的 JSON 文档。

- 🔧 修复无效的 JSON 文档，确保格式正确。
- 📄 文档链接：[jsonrepair GitHub](https://github.com/josdejong/jsonrepair)。
- ✍️ 示例输入（无效 JSON）：包含单引号、缺失引号、非法字符等问题。
- ✅ 示例输出（修复后 JSON）：自动修正为有效的 JSON 格式。
- 🛠️ 支持处理数组、字符串拼接等常见 JSON 错误。

---

### [JavaScript 字符串 slice() 方法的危害性 | Attio](https://attio.com/engineering/blog/javascript-string-slice-considered-harmful)

**原文标题**: [JavaScript string slice() considered harmful | Attio](https://attio.com/engineering/blog/javascript-string-slice-considered-harmful)

Attio 的 CSV 导入工具在处理用户数据时，发现了一个由 JavaScript 字符串 slice() 方法导致的 bug，涉及 UTF-16 编码和 protobuf 序列化问题。通过深入分析，团队找到了解决方案。

- 🐞 **问题发现**：gRPC 调用 Google Spanner 时出现错误，原因是字符串截断函数在处理 Unicode 字符（如国旗 emoji）时，错误地切分了 UTF-16 编码单元。  
- 🔍 **问题分析**：JavaScript 的 slice() 方法基于 UTF-16 编码单元操作，而非 Unicode 码点，导致截断后的字符串无法正确序列化为 protobuf 格式。  
- 💡 **解决方案**：利用字符串的迭代器（基于码点）重新实现截断函数 safeHead()，确保截断后的字符串仍是有效的 Unicode 字符。  
- 🛠 **修复实施**：替换原有的 slice() 方法为 safeHead()，成功解决了导入工具的错误。  
- 🌍 **Unicode 知识**：深入探讨了 JavaScript 字符串的 UTF-16 编码、码点与编码单元的区别，以及字形簇的概念。  
- 🔧 **技术细节**：通过 protobufjs 和 Buffer.from 的测试，验证了截断字符串在序列化和反序列化过程中的问题。  
- 🚀 **结果**：修复后的代码确保了数据在各种编码和传输场景下的正确性。

---

### [索引 | Node.js v24.3.0 文档](https://nodejs.org/api/)

**原文标题**: [Index | Node.js v24.3.0 Documentation](https://nodejs.org/api/)

Node.js v24.3.0 官方文档目录结构概览，包含核心模块、API 及工具分类。

- 📚 **核心模块** - 包含文件系统 (File system)、路径处理 (Path)、操作系统交互 (OS) 等基础功能  
- 🔗 **网络通信** - 涵盖 HTTP/HTTPS/HTTP2、TCP/UDP(Net/Datagram)、DNS 解析等网络相关 API  
- ⚙️ **系统交互** - 子进程 (Child processes)、集群 (Cluster)、进程控制 (Process) 等系统级操作  
- 🔐 **安全加密** - 提供 Crypto 加密、TLS/SSL 安全传输、Web Crypto API 等安全功能  
- 📦 **模块系统** - 支持 CommonJS/ECMAScript 模块、TypeScript 及包管理 (Packages)  
- 🛠️ **开发工具** - 调试器 (Debugger)、断言测试 (Assertion)、性能钩子 (Performance hooks) 等  
- 🌐 **国际化** - 国际化 (Internationalization) 支持多语言处理  
- 📊 **数据处理** - 包含流 (Stream)、缓冲区 (Buffer)、查询字符串 (Query strings) 等数据处理工具  
- ⏱️ **异步控制** - 异步上下文跟踪 (Async hooks)、定时器 (Timers)、事件循环 (Events) 机制  
- 📝 **实用工具** - 控制台 (Console)、实用函数 (Utilities)、REPL 交互环境等辅助功能  
- 🔄 **版本信息** - 文档同时提供 v24.3.0 及其他历史版本 (LTS/16.x/12.x 等) 的查阅入口

---

### [GitHub - nodejs/api-docs-tooling: Node.js API 文档生成工具](https://github.com/nodejs/api-docs-tooling)

**原文标题**: [GitHub - nodejs/api-docs-tooling: Node.js's tooling for API generation](https://github.com/nodejs/api-docs-tooling)

这是一个关于 Node.js API 文档生成工具的 GitHub 仓库，提供了工具的使用方法和相关信息。

- 📌 **仓库信息**: 这是一个公共仓库，拥有 17 颗星和 12 个分支，采用 MIT 许可证。
- 🛠️ **工具用途**: 用于生成和检查 Node.js API 文档的工具。
- 📄 **使用说明**: 提供了本地调用的命令行工具，支持生成、检查、交互式向导等功能。
- 🔧 **生成选项**: 支持多种生成模式，如 JSON、HTML、man-page 等，并可指定输入输出路径和线程数。
- ✅ **检查功能**: 可以独立运行检查功能，支持禁用特定规则和干运行模式。
- 🔄 **交互式向导**: 提供交互式命令行向导，方便用户操作。
- 📊 **资源**: 包含 README、MIT 许可证、行为准则和安全政策等文档。
- 🌍 **语言分布**: 主要使用 JavaScript（92.3%），辅以 CSS 和 HTML。

---

### [非 HTML 内容](https://pbs.twimg.com/media/GvGBdD7WIAAGoif?format=jpg&name=900x900)

**原文标题**: [Non-HTML content](https://pbs.twimg.com/media/GvGBdD7WIAAGoif?format=jpg&name=900x900)

无法总结：非 HTML 内容。

---

### [功能 (web): 由 avivkeller 添加网页生成器 · Pull Request #285 · nodejs/api-docs-tooling · GitHub](https://github.com/nodejs/api-docs-tooling/pull/285)

**原文标题**: [feat(web): add web generator by avivkeller · Pull Request #285 · nodejs/api-docs-tooling · GitHub](https://github.com/nodejs/api-docs-tooling/pull/285)

Node.js API 文档工具库中新增了一个 Web 生成器功能，该功能支持生成静态文档网站，并具备搜索功能。以下是关键点总结：

- 🚀 新增 Web 生成器功能，支持生成静态文档网站  
- 🔍 支持搜索功能，可通过指定索引文件优化搜索体验  
- ⚡ 使用 React 服务端渲染（SSR），支持无 JavaScript 环境下的文档浏览  
- 🛠️ 修复了多个问题，包括 Markdown 渲染不正确和样式问题  
- 📊 代码覆盖率报告显示当前覆盖率为 70.07%，部分文件缺失覆盖率  
- 👥 多位开发者参与代码审查和讨论，提出了改进建议  
- 🔄 经历了多次代码提交和强制推送，解决了部署问题  
- 📌 仍有一些待完成任务，如移除 mustache 依赖和优化性能

---

### [数据出口：它是什么以及成本是多少？](https://getdeploying.com/reference/data-egress)

**原文标题**: [Data Egress: What is it and how much does it cost?](https://getdeploying.com/reference/data-egress)

云计算数据出口费用对比：不同服务商的免费额度与超额费用差异显著，部分厂商提供完全免费出口带宽，而主流大厂如 AWS/Azure/GCP 收费较高。

- 🌐 **数据出口定义**：指数据从云服务商网络传输至公网产生的费用，下载、跨云传输均属此类  
- 💰 **费用差异大**：1TB 超额费用从免费（UpCloud/Runpod 等）到$550（Netlify）不等  
- 🆓 **免费额度对比**：  
  - 完全免费：Civo/OVH/Lambda Labs 等 15 家  
  - 有限免费：Heroku(2TB/月)、Hetzner(1-60TB/月)、AWS/Azure(100GB/月)  
- 🚀 **降费策略**：使用 CDN、数据压缩、私有网络传输、设置用量监控警报  
- ⚠️ **隐藏限制**：部分服务商超额后降速（如 Paperspace 从 10Gbps 降至 900Mbps）  
- 🌍 **区域影响**：价格基于北美/欧洲区域测算，其他地区可能不同  
- 🔍 **核心原因**：云商需覆盖带宽成本，并通过收费抑制数据迁移和网络滥用

---

### [Reddit - 互联网的核心](https://www.reddit.com/r/node/comments/1lstbp1/best_scalable_file_structure_for_unopinionated/)

**原文标题**: [Reddit - The heart of the internet](https://www.reddit.com/r/node/comments/1lstbp1/best_scalable_file_structure_for_unopinionated/)

Node.js 非官方子论坛，讨论 Node.js、JavaScript、TypeScript 及相关生态内容。

- 🏠 **社区性质**：非官方的 Node.js 讨论区  
- 💬 **讨论主题**：涵盖 Node.js、JavaScript、TypeScript 及生态相关内容  
- � **用户提问**：寻求适用于非限定性 Node 框架（如 Express、Hono）的可扩展生产级后端文件夹结构  
- 🏗️ **参考示例**：用户提到 React 的"bulletproof"项目结构（如 bulletproof-react），希望找到类似的后端实践  
- 🧩 **架构倾向**：倾向于领域驱动设计（DDD）、模块化单体架构（通过代码而非独立服务实现微服务）  
- 🏢 **多租户支持**：考虑多租户场景，结合更好的身份验证方案和 Drizzle ORM  
- 🔍 **需求明确**：用户希望找到一个优质的可扩展后端结构示例

---

### [吕的主页](https://lui.ie/guides/semantic-search-colors)

**原文标题**: [Lui's Homepage](https://lui.ie/guides/semantic-search-colors)

好的，请提供需要总结的文本内容，我会按照您要求的模板进行整理，包括概述总结和带表情符号的要点列表。  

示例模板：  

这里是文章的概述总结，简明扼要地概括全文核心内容。  

- 🌟 第一个关键点，用简短的语言描述。  
- 🔍 第二个关键点，突出重要细节。  
- 📌 第三个关键点，总结核心结论或建议。  

请提供您的文本内容，我会立即为您生成结构化总结！

---

### [brandmint.ai](https://brandmint.ai/color-genie)

**原文标题**: [brandmint.ai](https://brandmint.ai/color-genie)

好的，请提供需要总结的文本内容，我会按照您要求的模板进行整理和输出。  

示例格式：  

这里是文章的概述总结  

- 🌟 第一个关键点  
- 📊 第二个关键点  
- 🔍 第三个关键点  

请提供具体文本内容，我会为您生成相应的总结。

---

### [构建你的第一个 MCP 服务器：新手教程 - YouTube](https://www.youtube.com/watch?v=egVm_z1nnnQ)

**原文标题**: [Build your first MCP Server: Tutorial for Beginners. - YouTube](https://www.youtube.com/watch?v=egVm_z1nnnQ)

这是一个关于 YouTube 网站相关链接和信息的概览。

- 📌 概要  
- 📰 プレスルーム（新闻发布室）  
- ©️ 著作権（版权信息）  
- 📧 お問い合わせ（联系方式）  
- � クリエイター向け（创作者资源）  
- 📢 広告掲載（广告投放）  
- 💻 開発者向け（开发者资源）  
- 📜 利用規約（使用条款）  
- 🔒 プライバシー（隐私政策）  
- 🛡️ ポリシーとセキュリティ（政策与安全）  
- ⚙️ YouTube の仕組み（YouTube 运作机制）  
- 🆕 新機能を試してみる（试用新功能）  
- ®️ © 2025 Google LLC（版权归属）

---

### [JavaScript 中普通函数和箭头函数有什么区别？](https://jrsinclair.com/articles/2025/whats-the-difference-between-named-functions-and-arrow-functions/)

**原文标题**: [What’s the difference between ordinary functions and arrow functions in JavaScript?](https://jrsinclair.com/articles/2025/whats-the-difference-between-named-functions-and-arrow-functions/)

JavaScript 中普通函数与箭头函数的区别  

- 🏗️ **函数声明与函数表达式**：普通函数可以通过`function`关键字声明或表达式创建，而箭头函数始终是匿名表达式。  
- 🏷️ **命名与提升**：普通函数声明会被提升（hoisted），可在定义前调用；箭头函数不会提升，必须先定义后使用。  
- 🏹 **简洁性**：箭头函数语法更简洁，单参数可省略括号，单行代码可省略`return`和花括号。  
- 🚫 **`this`绑定**：箭头函数没有自己的`this`，继承外层作用域的`this`；普通函数的`this`由调用方式决定。  
- 🔨 **构造函数**：普通函数可作为构造函数用`new`调用；箭头函数不能用作构造函数，会抛出错误。  
- 🔄 **生成器**：普通函数可用`function*`定义生成器；箭头函数不能使用`yield`关键字。  
- 📌 **适用场景**：箭头函数适合匿名回调（如`map`、`Promise`）；普通函数适合需要`this`绑定或构造对象的场景。  
- 📜 **代码组织**：普通函数声明支持“先调用后定义”的代码结构，提升可读性。

---

### [我在线吗？](https://antonz.org/is-online/)

**原文标题**: [Am I online?](https://antonz.org/is-online/)

文章探讨了如何检测网络连接的有效方法，并比较了不同公司提供的连接检测服务端点。

- 🌐 传统方法通过 ping DNS 服务器（如 8.8.8.8 或 1.1.1.1）检测网络连接，但仅使用 ICMP 协议，无法全面测试 HTTP 客户端所需的完整协议栈。
- 🔍 作者发现 Google 提供的 http://google.com/generate_204 端点可以返回 204 No Content 状态，快速且可靠，适合检测网络连接。
- 📌 其他公司也提供类似端点，如 Cloudflare、Microsoft、Ubuntu 和 Xiaomi 等，部分返回 204 状态，部分返回 200 OK 状态。
- 💻 文章提供了 Python、JavaScript、Shell 和 Go 等多种编程语言的实现代码，用于检测网络连接。
- 👍 作者赞赏 Google 等公司公开提供网络连接检测端点，方便开发者使用。
- ❓ 最后，作者询问读者是否知道其他类似的端点，并提供了联系方式。

---

### [GitHub - usebruno/bruno: 开源 API 探索与测试 IDE（Postman/Insomnia 的轻量级替代品）](https://github.com/usebruno/bruno)

**原文标题**: [GitHub - usebruno/bruno: Opensource IDE For Exploring and Testing API's (lightweight alternative to Postman/Insomnia)](https://github.com/usebruno/bruno)

Bruno 是一个开源的 API 探索和测试工具，旨在替代 Postman 和 Insomnia，注重数据隐私和本地化操作。

- 🚀 **开源 IDE**：Bruno 是一个轻量级的开源 API 测试工具，支持多平台运行（Mac、Windows、Linux）。
- 🔒 **数据隐私**：Bruno 离线运行，不提供云同步功能，确保用户数据仅保存在本地设备。
- 📂 **文件存储**：API 集合以纯文本格式（Bru 语言）存储在本地文件夹中，便于版本控制（如 Git）协作。
- 🌍 **多语言支持**：提供多种语言界面，包括英语、中文、法语等。
- 📥 **多种安装方式**：支持 Homebrew、Chocolatey、Scoop、Snap、Flatpak 和 Apt 等包管理器安装。
- 💡 **核心功能**：跨平台运行、Git 协作、支持 REST API 和 OpenAPI 等。
- 💰 **商业模式**：主要功能免费，同时提供付费版本以支持可持续发展。
- 📢 **社区活跃**：鼓励用户提交反馈和测试用例，提供 Discord、Twitter 等社区交流渠道。
- 📜 **开源协议**：采用 MIT 许可证，允许自由使用和修改。

---

### [GitHub - poolifier/poolifier：快速轻量的Node.js worker_threads 与集群工作线程池](https://github.com/poolifier/poolifier)

**原文标题**: [GitHub - poolifier/poolifier: Fast and small Node.js worker_threads and cluster worker pool](https://github.com/poolifier/poolifier)

Poolifier 是一个快速且轻量的 Node.js worker_threads 和 cluster 工作池库，旨在提升服务器性能和解决事件循环相关问题。

- 🚀 **高性能**：通过 worker_threads 和 cluster 模块实现 CPU 和 I/O 密集型任务的高效处理。
- 🔧 **易用性**：提供简洁的 API，支持固定大小和动态大小的线程池，并可轻松切换池类型。
- 📊 **动态扩展**：动态线程池可根据负载自动增减工作线程数量，支持空闲超时回收。
- 🔄 **任务调度**：支持多种任务分发策略，包括空闲任务窃取、背压任务窃取和错误重分配。
- ⚡ **多任务支持**：支持同步/异步任务、可中止任务，以及多任务函数的动态管理和优先级队列。
- 🛡️ **健壮性**：内置错误处理，与 Node.js async_hooks 深度集成，严格测试确保稳定性。
- 📦 **无依赖**：零运行时依赖，支持 CommonJS、ESM 和 TypeScript。
- 🌍 **活跃社区**：拥有活跃的开发和维护团队，持续更新和改进。
- 📜 **开源许可**：采用 MIT 许可证，代码开放且自由使用。

---

### [Ruby on Rails、Elixir、Node.js 和 Python 应用监控 | AppSignal APM](https://www.appsignal.com/?utm_source=cooperpress&utm_medium=cooperpress&utm_term=node_nl)

**原文标题**: [Application Monitoring for Ruby on Rails, Elixir, Node.js & Python | AppSignal APM](https://www.appsignal.com/?utm_source=cooperpress&utm_medium=cooperpress&utm_term=node_nl)

APM（应用性能监控）工具 AppSignal 提供全面的监控解决方案，支持多种编程语言和框架，帮助企业快速定位和解决问题。

- 🚀 **核心功能**：错误追踪、性能监控、主机监控、异常检测、正常运行时间监控、指标仪表盘、日志管理、检查点等  
- 🛠️ **高级工具**：工作流、自动化仪表盘、时间侦探等  
- 🌍 **支持语言**：Ruby（Rails）、Elixir、Node.js、JavaScript、Python 等  
- 🏢 **企业级服务**：大规模部署、企业支持、附加功能（长期日志存储、HIPAA 合规、SAML SSO）  
- 📚 **资源**：文档、博客、定价、免费试用  
- 💡 **特点**：轻量级代理、开发者支持、GDPR 合规、99.999% 正常运行时间  
- 📈 **客户评价**：1500+ 开发团队信赖，提供快速安装和低学习曲线  
- 🆓 **免费试用**：30 天免费试用，无需信用卡，所有功能可用

---

### [grammY](https://grammy.dev/)

**原文标题**: [grammY](https://grammy.dev/)

grammY 让创建 Telegram 机器人变得非常简单，即使新手也能轻松上手。

- 🤖 简单易用：grammY 使创建 Telegram 机器人变得极其简单  
- 🎯 快速上手：即使没有经验，用户也能迅速掌握使用方法  
- 🚀 高效开发：简化了机器人开发流程，提升开发效率

---

### [GitHub - grammyjs/grammY：Telegram 机器人框架](https://github.com/grammyjs/grammY)

**原文标题**: [GitHub - grammyjs/grammY: The Telegram Bot Framework.](https://github.com/grammyjs/grammY)

grammY 是一个 Telegram 机器人框架，适用于初学者和大规模应用开发，支持 TypeScript 和 JavaScript，可在 Node.js 和 Deno 上运行。

- 🤖 grammY 是一个易于使用且功能强大的 Telegram 机器人框架。  
- 📚 提供优秀的文档和 API 参考，支持代码编辑器集成（如 VS Code）。  
- 🚀 支持 TypeScript 和 JavaScript，运行于 Node.js 或 Deno 环境。  
- 🔌 拥有丰富的插件生态系统和友好的社区聊天支持。  
- 🌐 提供多种资源，包括官方网站、API 参考、示例仓库和社区聊天。  
- 📦 支持 JavaScript 打包，适用于浏览器和 Cloudflare Workers。  
- 👥 社区活跃，有多个贡献者和多语言支持（包括俄语社区）。  
- 📜 采用 MIT 许可证，欢迎各种形式的贡献。

---

### [GitHub - davidmarkclements/0x: 🔥 单命令火焰图性能分析 🔥](https://github.com/davidmarkclements/0x)

**原文标题**: [GitHub - davidmarkclements/0x: 🔥 single-command flamegraph profiling 🔥](https://github.com/davidmarkclements/0x)

0x 是一个单命令火焰图分析工具，用于发现 Node.js 代码中的性能瓶颈和热点路径。

- 🔥 支持单命令生成火焰图，适用于 Node.js 进程
- 🌍 跨平台支持（macOS、Linux、Windows、Android 等）
- 📊 可视化堆栈跟踪，帮助分析性能问题
- ⚡ 支持 Node v20.x 及以上版本
- 🛠️ 提供命令行和编程 API 两种使用方式
- 📂 生成包含 flamegraph.html 的配置文件
- 🚀 支持生产服务器轻量级分析
- 🔧 提供多种命令行选项，如自动打开浏览器、自定义输出目录等
- 🐛 支持调试和内存问题排查
- 📜 开源项目，采用 MIT 许可证

---

### [7.28.0 版本发布：`babel.config.ts`、显式资源管理及废弃绑定提案 · Babel](https://babeljs.io/blog/2025/06/30/7.28.0)

**原文标题**: [7.28.0 Released: `babel.config.ts`, explicit resource management, and discard binding proposal · Babel](https://babeljs.io/blog/2025/06/30/7.28.0)

Babel 7.28.0 版本发布，新增了对 `babel.config.ts` 和 `babel.config.mts` 的原生支持，引入了 ES2026 显式资源管理功能、丢弃绑定提案以及 `sourceType: "commonjs"` 选项。

- 🚀 **Babel 7.28.0 发布**：支持 `babel.config.ts` 和 `babel.config.mts`，推荐使用 Node.js 24 以获得最佳效果。
- 🔧 **显式资源管理默认启用**：ES2026 显式资源管理功能现已默认启用，无需额外插件。
- 🗑️ **丢弃绑定提案支持**：通过 `@babel/plugin-proposal-discard-binding` 插件支持 `void` 绑定，用于表示未使用的变量或参数。
- 📜 **CommonJS 支持**：新增 `sourceType: "commonjs"` 选项，适用于 CommonJS 环境，如 Node.js。
- 💡 **Babel 8 兼容性**：所有新功能已包含在 Babel 8.0.0-beta.1 版本中。
- 💰 **支持 Babel**：欢迎通过 Open Collective 捐赠或直接参与新 ECMAScript 提案的实现。

---

### [GitHub - SBoudrias/Inquirer.js: 一系列常见的交互式命令行用户界面](https://github.com/SBoudrias/Inquirer.js)

**原文标题**: [GitHub - SBoudrias/Inquirer.js: A collection of common interactive command line user interfaces.](https://github.com/SBoudrias/Inquirer.js)

Inquirer.js 是一个常见的交互式命令行用户界面集合，用于在终端中提供丰富的用户交互体验。

- 🚀 **项目概述**: Inquirer.js 是一个流行的命令行交互工具库，支持多种交互式提示类型，如输入、选择、确认等。  
- 📦 **安装方式**: 可通过 npm 或 yarn 安装，命令为 `npm install @inquirer/prompts` 或 `yarn add @inquirer/prompts`。  
- 🔄 **版本更新**: 项目已进行重写，优化了包大小和性能，旧版本仍维护但不再活跃开发。  
- 💡 **核心功能**: 提供多种提示类型，包括输入、选择、复选框、密码等，每种提示都有详细的文档和示例。  
- ⚙️ **高级用法**: 支持自定义上下文配置，如输入输出流、清除提示、异步取消等。  
- ❌ **错误处理**: 提供了处理用户强制退出（如 Ctrl+C）的优雅方式，避免堆栈跟踪影响用户体验。  
- 🔗 **社区支持**: 支持社区贡献的扩展提示，如交互式列表、文件选择器等，丰富了功能生态。  
- 📜 **许可证**: 采用 MIT 许可证，开源且允许自由使用和修改。  
- 🌟 **受欢迎程度**: 项目拥有 21k+ stars 和 1.3k+ forks，被超过 1000 万项目使用。  
- 👥 **贡献者**: 由 216 位贡献者共同维护，社区活跃。

---

### [发布 v1.1.0 · yamadashy/repomix · GitHub](https://github.com/yamadashy/repomix/releases/tag/v1.1.0)

**原文标题**: [Release v1.1.0 · yamadashy/repomix · GitHub](https://github.com/yamadashy/repomix/releases/tag/v1.1.0)

Repomix 发布了 v1.1.0 版本，新增 Bun 运行时支持，优化了性能并减少了包体积。

- 🚀 新增 Bun 运行时支持，可通过 `bunx repomix@latest` 或 `bun --bun repomix@latest` 运行  
- 📦 从 Piscina 迁移到 Tinypool，减少了 700KB 的包体积，同时保持 API 兼容性和性能  
- 🔄 更新方式：使用 `npm update -g repomix` 或 `bun add -g repomix`  
- 💬 用户可通过 GitHub issues 或 Discord 社区反馈问题或建议  
- 🎉 发布后获得社区积极反响，多个用户用表情（👍😄🎉❤️🚀）表示支持

---

### [发布 v10.2.0 · secretlint/secretlint · GitHub](https://github.com/secretlint/secretlint/releases/tag/v10.2.0)

**原文标题**: [Release v10.2.0 · secretlint/secretlint · GitHub](https://github.com/secretlint/secretlint/releases/tag/v10.2.0)

secretlint 项目发布了 v10.2.0 版本，包含新特性、修复和依赖更新。

- 🚀 新增数据库连接字符串检测规则，支持 MongoDB、MySQL 和 PostgreSQL 多种格式  
- 🔧 修复了基础认证规则中协议检测范围，避免与数据库规则重叠  
- 🤖 通过 CI 工作流添加了 merge-gatekeeper，并更新了多个 GitHub Actions 版本  
- 📦 依赖项更新，包括 read-pkg 从 v8 升级到 v9，以及多个其他依赖的版本更新  
- 👥 贡献者包括 azu、renovate 和 noritaka1166

---

### [GitHub - faker-js/faker: 在浏览器和 Node.js 中生成大量虚假数据](https://github.com/faker-js/faker)

**原文标题**: [GitHub - faker-js/faker: Generate massive amounts of fake data in the browser and node.js](https://github.com/faker-js/faker)

Faker 是一个用于在浏览器和 Node.js 中生成大量假数据的开源库，支持多语言和多种数据类型。

- 🚀 **功能丰富** - 支持生成人物、地点、日期、金融、商业等多种假数据。
- 🌏 **多语言支持** - 提供超过 70 种语言的本地化数据生成。
- 📦 **安装简单** - 通过 npm 安装 `@faker-js/faker` 即可使用。
- 🪄 **使用灵活** - 支持 ESM 和 CJS 模块，提供多种 API 方法。
- 💎 **模块化设计** - 包含多个模块，如人物、地点、金融等，详细 API 文档可供查阅。
- 🌏 **本地化实例** - 可以导入不同语言的实例，如德语 (`fakerDE`)。
- ⚙️ **随机种子设置** - 通过设置种子可以保证生成数据的可重复性。
- 🤝 **开源支持** - MIT 许可，由社区赞助和支持，欢迎贡献。
- 📜 **历史背景** - 原始 `faker.js` 的后续版本，团队更新于 2022 年 1 月 14 日。
- 🔑 **许可证** - 采用 MIT 许可证，可自由使用和修改。

---

### [发布 oxlint v1.6.0 · oxc-project/oxc · GitHub](https://github.com/oxc-project/oxc/releases/tag/oxlint_v1.6.0)

**原文标题**: [Release oxlint v1.6.0 · oxc-project/oxc · GitHub](https://github.com/oxc-project/oxc/releases/tag/oxlint_v1.6.0)

oxc-project/oxc 发布了 oxlint v1.6.0 版本，包含错误修复、重构、文档更新和性能优化。

- 🐛 **Bug 修复**：修复了多个规则中的不一致行为和错误，如 `no-duplicate-imports` 和 `consistent-index-object-style`。  
- 🚜 **代码重构**：优化了语义分析、语言服务器和 AST 相关代码，移除冗余选项和方法。  
- 📚 **文档更新**：为多个 Next.js 相关规则添加了示例和说明，提升可读性。  
- ⚡ **性能优化**：通过减少迭代次数、提前检查文件路径等方式提升规则执行效率。  
- 🎉 **社区反馈**：获得 7 个点赞（👍）、6 个爱心（❤️）等积极反应。

---

### [GitHub - glitternetwork/pinme：一键部署你的前端应用](https://github.com/glitternetwork/pinme)

**原文标题**: [GitHub - glitternetwork/pinme: Deploy Your Frontend in a Single Command](https://github.com/glitternetwork/pinme)

PinMe 是一个简单易用的命令行工具，用于将文件和目录上传到 IPFS 网络。

- 🚀 快速上传文件和目录到 IPFS  
- 📂 支持多种文件类型和大小  
- 📊 查看和管理上传历史  
- 🔗 自动生成可访问的 IPFS 链接  
- 🌐 预览上传内容  
- 📦 安装方式：`npm install -g pinme` 或 `yarn global add pinme`  
- ⚙️ 主要命令：`upload`（上传）、`rm`（删除）、`list`（查看历史）、`help`（帮助）  
- 📌 单文件大小限制：20MB，目录总大小限制：500MB  
- 📍 日志和配置文件存储路径：Linux/macOS `~/.pinme/`，Windows `%USERPROFILE%\.pinme\`  
- 📜 许可证：MIT License  
- 📧 联系方式：GitHub Issues 或邮箱 pinme@glitterprotocol.io  
- 🌟 由 Glitter Protocol 团队开发和维护

---

### [GitHub - glitternetwork/pinme：一键部署你的前端应用](https://github.com/glitternetwork/pinme)

**原文标题**: [GitHub - glitternetwork/pinme: Deploy Your Frontend in a Single Command](https://github.com/glitternetwork/pinme)

PinMe 是一个简单易用的命令行工具，用于将文件和目录上传到 IPFS 网络，具有上传、管理和查看历史记录等功能。

- 🚀 快速上传文件和目录到 IPFS 网络  
- 📂 支持多种文件类型和大小  
- 📊 可查看和管理上传历史记录  
- 🔗 自动生成可访问的 IPFS 链接  
- 🌐 预览上传内容  

安装方式：  
- 📦 使用 npm：`npm install -g pinme`  
- 🧶 使用 yarn：`yarn global add pinme`  

主要命令：  
- ⬆️ 上传文件或目录：`pinme upload [path]`  
- ❌ 从 IPFS 删除文件：`pinme rm [hash]`  
- 📜 查看上传历史：`pinme list` 或 `pinme ls`  
- ❓ 获取帮助：`pinme help`  

上传限制：  
- ⚠️ 单文件大小限制：20MB  
- ⚠️ 目录总大小限制：500MB  

存储与日志：  
- 💾 上传文件存储在 IPFS 网络，可通过 Glitter Protocol 的 IPFS 网关访问  
- 📝 日志和配置文件存储在`~/.pinme/`（Linux/macOS）或`%USERPROFILE%\.pinme\`（Windows）  

许可证：  
- 📜 MIT 许可证  

联系方式：  
- 📧 邮箱：pinme@glitterprotocol.io  
- 🐱 GitHub Issues：https://github.com/glitternetwork/pinme/issues

---

### [定价 | ConfigCat 功能开关](https://configcat.com/pricing/?utm_source=cooperpress_newsletter&utm_medium=sponsor&utm_campaign=cooperpress_node_202506)

**原文标题**: [Pricing | ConfigCat Feature Flags](https://configcat.com/pricing/?utm_source=cooperpress_newsletter&utm_medium=sponsor&utm_campaign=cooperpress_node_202506)

ConfigCat 是一个功能管理和远程配置服务，提供多种定价方案和功能，适合不同规模的企业和团队使用。

- 🚀 **产品概述**：ConfigCat 提供功能标志和远程配置服务，支持多种开发环境和团队协作。
- 💰 **定价方案**：提供免费、专业、智能、企业和专用等多种方案，价格从€0/月到€4,500/月不等。
- 🔄 **功能**：包括无限功能标志读取、团队管理、安全合规、审计日志和多种集成选项。
- 🌍 **全球支持**：支持欧元和美元计价，提供月度或年度计费选项。
- 📊 **资源限制**：不同方案提供不同的 config.json 下载量和网络流量，从 5 百万/月到 6 亿+/月不等。
- 🔒 **安全与合规**：支持 2FA、SSO、SAML、GDPR 和 ISO 27001:2013 等安全标准。
- 🌱 **环保承诺**：每订阅一次即种植树木，支持环保。
- 🎓 **教育优惠**：为学生和教师提供特别方案。
- 📅 **审计日志**：记录所有功能标志的变更历史，支持强制修改理由，提高透明度。
- 🏢 **企业服务**：提供软件托管服务，确保业务连续性。
- 📞 **支持**：提供从社区支持到高级 SLA 支持的不同级别服务。
- 🛠️ **开发工具**：提供多种 SDK 和集成，支持多种编程语言和平台。
- 📚 **文档与资源**：详尽的 API 文档、教程和博客，帮助用户快速上手。

---

### [Deno 2.4：deno bundle 回归 | Deno](https://deno.com/blog/v2.4)

**原文标题**: [Deno 2.4: deno bundle is back | Deno](https://deno.com/blog/v2.4)

Deno 2.4 版本发布，重新引入了 `deno bundle` 命令，并新增多项功能改进，包括文本和二进制导入、稳定的 OpenTelemetry 支持、更简单的依赖管理等。

- 🚀 **Deno 2.4 发布**：升级命令为 `deno upgrade`，新增多项功能优化开发者体验。  
- 🔄 **`deno bundle` 回归**：支持单文件打包，自动树摇和压缩，适用于服务器和浏览器端。  
- 📝 **文本和二进制导入**：通过 `--unstable-raw-imports` 标志直接导入非 JavaScript 文件（如 `.txt`、`.png`）。  
- 📊 **稳定的 OpenTelemetry**：无需 `--unstable-otel` 标志，简化项目可观测性。  
- ⚙️ **新 `--preload` 标志**：允许在运行主脚本前执行代码，适用于环境修改或数据预加载。  
- 🔄 **依赖管理改进**：新增 `deno update` 命令，简化依赖版本更新。  
- 📊 **覆盖率收集**：`deno run --coverage` 支持子进程覆盖率收集，HTML 报告支持暗黑模式。  
- 🔧 **环境变量 `DENO_COMPAT=1`**：简化 Node.js 兼容性配置，减少标志使用。  
- 🌐 **权限改进**：`--allow-net` 支持子域名通配符和 CIDR 范围，新增 `--deny-import` 限制导入。  
- 📦 **`package.json` 条件导出**：支持 React 生态的 `react-server` 等条件导出。  
- 🏷️ **裸说明符支持**：`deno run` 可直接运行 `deno.json` 中定义的导入别名。  
- ✨ **格式化支持**：`deno fmt` 新增对 `.xml`、`.svg` 和 `.mustache` 文件的支持。  
- 📂 **更好的 `tsconfig.json` 支持**：支持 `references`、`extends` 等选项，提升前端框架兼容性。  
- 🌍 **Node.js 全局简化**：`Buffer`、`setImmediate` 等全局变量默认可用，减少兼容性配置。  
- 🔗 **本地 npm 包支持**：`deno.json` 中的 `patch` 选项更名为 `links`，更符合 `npm link` 行为。  
- 🛠️ **Node.js API 改进**：新增 `glob` API，多模块兼容性达 95% 以上。  
- 🧩 **LSP 增强**：改进自动导入、配置处理和大型文件格式化性能。  
- 🎉 **其他功能**：`fetch` 支持 Unix/Vsock 套接字、`deno serve` 新增 `onListen` 回调、Jupyter 内核管理等。  
- 🙏 **致谢**：感谢社区贡献者，详细更新列表见 GitHub。

---

### [Deno 2.4：deno bundle 回归 | Deno](https://deno.com/blog/v2.4#simpler-node-globals)

**原文标题**: [Deno 2.4: deno bundle is back | Deno](https://deno.com/blog/v2.4#simpler-node-globals)

Deno 2.4 版本发布，重新引入了 `deno bundle` 命令，并新增多项功能改进，包括导入文本和字节、内置 OpenTelemetry 稳定化、环境预加载、依赖管理优化等。

- 🚀 **Deno 2.4 升级**：通过 `deno upgrade` 升级，或使用 Shell/PowerShell 安装新版本。  
- 🔄 **`deno bundle` 回归**：支持单文件打包，自动树摇和压缩，适用于服务器和浏览器平台。  
- 📄 **导入文本和字节**：通过 `--unstable-raw-imports` 标志直接导入文本、二进制文件（如 PNG）。  
- 📊 **内置 OpenTelemetry 稳定化**：无需 `--unstable-otel` 标志，简化项目可观测性。  
- ⚙️ **环境预加载**：新增 `--preload` 标志，允许在运行主脚本前执行代码（如修改全局变量）。  
- 🔄 **依赖管理优化**：新增 `deno update` 命令，支持更新 npm 和 JSR 依赖到最新版本。  
- 📊 **覆盖率收集**：`deno run --coverage` 支持收集子进程覆盖率，HTML 报告新增暗黑模式。  
- 🔧 **权限改进**：`--allow-net` 支持子域名通配符和 CIDR 范围，`--deny-import` 显式禁止导入特定主机。  
- 📦 **Node.js 兼容性增强**：支持 `Buffer`、`setImmediate` 等全局变量，改进 `node:` 模块兼容性（如 `node:buffer` 达 95%）。  
- 🛠️ **工具链改进**：`deno fmt` 支持 XML/SVG 文件，`deno run` 支持裸说明符入口，LSP 功能优化。  
- 🎉 **其他亮点**：`fetch` 支持 Unix/Vsock 套接字，`deno serve` 新增 `onListen` 回调，Jupyter 内核管理增强。  
- 🙏 **致谢**：感谢社区贡献者，包括问题反馈、代码提交等。  

更多详情可查看 [GitHub 完整更新列表](https://github.com/denoland/deno/pulls?q=is%3Apr+merged%3A2025-07-02)。

---

### [机器人验证](https://js1024.fun/)

**原文标题**: [Bot Verification](https://js1024.fun/)

验证中，请稍候...  

- 🔍 系统正在确认您是否为真人用户  
- ⏳ 此过程可能需要短暂等待  
- 🤖 防止自动化程序滥用是主要目的  
- ✅ 完成验证后即可正常访问

---

### [JavaScript 正在用 Rust 重写](https://endform.dev/blog/js-is-being-rewritten-in-rust/)

**原文标题**: [JavaScript is being rewritten in Rust](https://endform.dev/blog/js-is-being-rewritten-in-rust/)

JavaScript 工具生态正逐步从 JavaScript 转向 Rust，以提高性能和开发体验。

- 🚀 ESBuild 的出现展示了速度对开发工具的重要性，开启了 JavaScript 工具用其他语言编写的趋势。  
- 🦀 多个 JavaScript 工具如 Biome、OXC、Rolldown、Turbopack、Turborepo 和 Deno 已转向 Rust 开发。  
- 💰 Void Zero 公司获得 460 万美元种子轮融资，表明 Rust 工具已进入主流并得到资金支持。  
- 🔍 实际案例：Endform 使用 OXC 进行依赖分析，展示了 Rust 工具在性能和易用性上的优势。  
- 🐘 TypeScript 的类型检查是目前 Rust 工具生态中的一大挑战，微软选择用 Go 而非 Rust 重写 TypeScript。  
- 🛠️ 扩展性和依赖共享是 Rust 工具面临的另外两大挑战。  
- 📊 Rust 编写的 JavaScript 工具如 Deno 和 Turborepo 在 GitHub 上获得了极高的关注度。  
- 🔮 未来趋势：Rust 可能成为 JavaScript 工具生态的支柱，尽管完全取代 JavaScript 的可能性不大。  
- ⚡ Rust 工具带来的性能提升、稳定性和开发体验改善是推动这一趋势的主要因素。

---

### [使用 JavaScript 代理构建轻量级响应式状态管理器 | Loren Stewart](https://www.lorenstew.art/blog/reactive-state-manager-with-proxies)

**原文标题**: [Building a Lightweight Reactive State Manager with JavaScript Proxies | Loren Stewart](https://www.lorenstew.art/blog/reactive-state-manager-with-proxies)

Loren Stewart 是一位软件开发者，近期分享了多篇关于前端架构和状态管理的技术文章，重点介绍了如何利用 JavaScript 原生特性简化开发流程。

- 🛠️ 使用 JavaScript Proxy 构建轻量级响应式状态管理器，无需复杂库即可实现 UI 与状态自动同步  
- 🎯 核心思路：通过 Proxy 拦截状态对象的 set 操作，自动触发 UI 更新函数，减少样板代码  
- 📝 实战案例：媒体提交表单中，通过 Proxy 自动处理照片/视频选择、按钮状态和表单输入更新  
- 🔄 支持复杂交互：如拖拽重新排序照片，仅需更新状态即可自动刷新 UI  
- 🧩 架构设计：配套公开 API 函数（addPhoto/setVideo）和状态查询模块（StateQueries）保持代码整洁  
- 💡 优势：无依赖、低耦合、代码量少，适合替代重型状态管理库  
- 🏷️ 相关技术标签：前端开发、JavaScript、状态管理、Proxy 对象  

近期其他技术文章：
- 🏗️ 约束条件下的架构设计指南（7 月 2 日）  
- 🚀 用自定义事件总线增强 HTMX（6 月 19 日）  
- ⚡ 从零构建现代前端事件系统（6 月 18 日）  
- 🌐 基于 NestJS WebSockets 实现实时交互（6 月 15 日）

---

### [宣布 Rspack 1.4 - Rspack](https://rspack.rs/blog/announcing-1-4)

**原文标题**: [Announcing Rspack 1.4 - Rspack](https://rspack.rs/blog/announcing-1-4)

Rspack 1.4 版本发布，带来多项性能优化和新功能，包括浏览器运行支持、更快的 SWC、更小的打包体积、默认增量构建等，同时生态系统工具链也同步更新。

- 🚀 **Rspack 1.4 发布**：新增多项功能，包括浏览器运行支持、性能优化和工具链升级。
- 🌐 **浏览器运行支持**：通过 Wasm 目标支持，Rspack 现可在浏览器环境中运行，如 StackBlitz 等平台。
- ⚡ **更快的 SWC**：JavaScript 解析器速度提升 30%-35%，压缩器速度提升 10%。
- 📦 **更小的打包体积**：SWC 增强死代码消除能力，结合 Rspack 的 tree shaking，生成更小的包。
- 🔄 **默认增量构建**：显著提升重建速度，HMR 性能提高 30%-40%。
- 🎨 **新的 CssChunkingPlugin**：实验性插件，专门处理 CSS 代码分割，确保样式加载顺序正确。
- 🛠️ **增强的懒编译**：支持在 MultiCompiler 中独立配置每个编译器的懒编译选项。
- 📂 **自定义输入文件系统**：允许自定义 compiler.inputFileSystem，支持虚拟模块等场景。
- 📊 **性能分析工具**：引入基于 perfetto 的精确追踪功能，帮助识别构建性能瓶颈。
- 🔗 **依赖升级**：升级了 Zod v4 和 Biome v2 等主要依赖。
- 🔧 **Rstack 进展**：包括 Rsbuild 1.4、Rslib 0.10、Rspress 2.0 beta 等工具的更新和新功能。
- 🧪 **Rstest 发布**：基于 Rspack 的新测试框架，提供 Node.js 和 UI 组件测试支持。
- 🌱 **生态系统更新**：next-rspack 测试覆盖率提升，Kmi 框架集成 Rspack 带来性能提升。
- ⬆️ **升级指南**：包括升级 SWC 插件和懒编译中间件变更等注意事项。

---

### [开源 AI 编辑器：首个里程碑](https://code.visualstudio.com/blogs/2025/06/30/openSourceAIEditorFirstMilestone)

**原文标题**: [Open Source AI Editor: First Milestone](https://code.visualstudio.com/blogs/2025/06/30/openSourceAIEditorFirstMilestone)

VS Code 团队宣布 GitHub Copilot Chat 扩展已开源，这是实现开源 AI 编辑器计划的首个里程碑，旨在促进社区创新和数据透明度，未来将进一步整合至 VS Code 核心代码库。

- 🎉 VS Code 团队达成首个里程碑：GitHub Copilot Chat 扩展现已开源，采用 MIT 许可证  
- 🤝 开源动机：推动社区驱动创新、增强数据透明度，延续 VS Code 开源成功模式  
- 🔍 探索机会：开发者可查看代码库，了解代理模式实现、LLM 上下文传递及提示词工程细节  
- 📝 参与贡献：欢迎提交 PR 和 Issue，长期目标是将扩展代码整合至 VS Code 核心  
- ⚙️ 后续计划：重构扩展组件至核心，逐步将原 Copilot 内联补全功能迁移至开源版本  
- 🌐 社区合作：携手开源 AI 社区完善方案，保持性能、扩展性和用户体验核心优先级

---

