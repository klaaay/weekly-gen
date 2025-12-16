### [Node 周刊第 605 期：2025 年 12 月 16 日](https://nodeweekly.com/issues/605)

**原文标题**: [Node Weekly Issue 605: December 16, 2025](https://nodeweekly.com/issues/605)

这是 Node Weekly 2025 年最后一期，回顾了 Node.js 在 2025 年的重要事件和年度最受欢迎内容，并宣布了简报将于 2026 年 1 月起改为每周四发布。

- 🗓️ **日程变更**：Node Weekly 简报将于 2026 年 1 月起改为每周四发布。
- 🚀 **版本更新**：Node.js v24.12.0 (LTS) 发布，其中对原生运行 TypeScript 的类型剥离功能支持已标记为稳定。Deno 2.6 同步发布，带来了类似 npx 的新工具 `dx` 等。
- 🔒 **安全发布**：原定于 12 月 15 日的 Node.js 安全版本发布已推迟至 12 月 18 日，预计将修复多个安全漏洞。
- 📊 **年度热门内容**：基于点击量汇总了 2025 年最受欢迎的文章，主题包括用 Node 内置功能替代 npm 包、文件操作指南、现代 Node 模式、测试最佳实践、V8 性能优化等。
- 📅 **年度月度回顾**：按月梳理了 2025 年 Node.js 生态的关键事件，如 TypeScript 支持进展、主要框架版本发布、安全事件、社区动态及版本发布周期讨论等。
- 🛠️ **工具与赞助**：提到了 Mongoose 9.0 更新、pnpm 10.26 发布，并穿插了 TimescaleDB、Foxit Software 等赞助商的内容。
- ✉️ **结尾与预告**：编辑送上节日祝福，并预告下一期简报将于 1 月 8 日（周四）发布。

---

### [出版物](https://cooperpress.com/publications/)

**原文标题**: [Publications](https://cooperpress.com/publications/)

我们通过一系列电子邮件摘要帮助开发者及其所在公司保持技术前沿，总订阅量超过 46 万，邮件打开率高达 30% 至 60%。

- 📧 **JavaScript 周刊**：最受欢迎的简报，面向 17 万以上 JavaScript 与全栈开发者，涵盖 React、Node.js 等生态
- 🎨 **前端聚焦**：专注网页设计与浏览器技术，涵盖 HTML、CSS 及 WebGL 等现代 Web API
- 💎 **Ruby 周刊**：Ruby 社区旗舰刊物，自 2010 年起持续提供 Rails 框架与开发动态
- 🟢 **Node 周刊**：Node.js 专项简报，已成为独立的重要技术媒体
- 🚀 **Golang 周刊**：Go 语言领域头部媒体，服务快速增长的后端开发生态
- ⚛️ **React 动态**：专注 React 与 React Native 的技术简报，订阅量近 4 万
- 🐘 **Postgres 周刊**：PostgreSQL 数据库专业媒体，覆盖全球开源数据库社区

---

### [Node.js — Node.js v24.12.0（长期支持版）](https://nodejs.org/en/blog/release/v24.12.0)

**原文标题**: [Node.js — Node.js v24.12.0 (LTS)](https://nodejs.org/en/blog/release/v24.12.0)

Node.js v24.12.0（LTS）版本“Krypton”发布，包含多项新功能、性能优化、错误修复及依赖项更新，涵盖 HTTP、模块、Node-API、SQLite、V8 等核心模块的改进，同时提供了各平台的安装包和二进制文件下载。

- 🚀 **HTTP 模块新增服务器选项**：添加`optimizeEmptyRequests`选项以优化空请求处理
- ⚙️ **工具函数增强**：为`util.deprecate`添加配置选项，提升弃用警告的灵活性
- 📦 **模块系统稳定化**：将类型剥离（type stripping）功能标记为稳定状态
- 🔧 **Node-API 扩展**：新增`napi_create_object_with_properties`函数，简化对象创建
- 🗄️ **SQLite 功能增强**：允许设置防御性标志（defensive flag），提升数据库安全性
- 👀 **监视配置支持**：在源代码中添加监视配置命名空间，便于监控调整
- 💾 **编译缓存可移植性**：新增选项使编译缓存可在不同环境间移植
- 🔍 **调试权限控制**：添加`--allow-inspector`选项，增强调试器访问权限管理
- 📊 **性能分析工具**：V8 引擎新增 CPU 性能分析功能，便于性能调优
- 🛠️ **多项错误修复与优化**：涵盖加密、控制台、调试器、流处理等模块的修复及性能提升

---

### [Node.js — 原生运行 TypeScript](https://nodejs.org/en/learn/typescript/run-natively)

**原文标题**: [Node.js — Running TypeScript Natively](https://nodejs.org/en/learn/typescript/run-natively)

Node.js v22.18.0 及以上版本支持直接运行仅包含可擦除 TypeScript 语法的代码，无需额外标志；较早版本需使用`--experimental-strip-types`标志。v22.7.0 引入的`--experimental-transform-types`标志可处理需转换的语法（如枚举和命名空间），并自动启用类型擦除功能。Node.js 的 TypeScript 加载器不依赖`tsconfig.json`，但建议配置编辑器与 TypeScript 5.7+ 以保持行为一致。

- 🚀 **Node.js v22.18.0+ 支持直接运行 TypeScript**：无需编译即可执行仅含可擦除语法的代码（如类型注解）。
- ⚙️ **旧版本需启用实验性标志**：v22.18.0 以下版本需使用`--experimental-strip-types`标志运行 TypeScript 文件。
- 🔄 **扩展语法支持**：v22.7.0 新增`--experimental-transform-types`标志，支持需转换的语法（如`enum`、`namespace`），并自动包含类型擦除功能。
- 🛑 **功能禁用选项**：可通过`--no-experimental-strip-types`标志禁用 TypeScript 支持。
- 📝 **配置建议**：Node.js 的 TypeScript 加载器不读取`tsconfig.json`，但推荐配置编辑器与 TypeScript 5.7+ 以匹配运行环境行为。

---

### [Deno 2.6：dx 是新的 npx | Deno](https://deno.com/blog/v2.6)

**原文标题**: [Deno 2.6: dx is the new npx | Deno](https://deno.com/blog/v2.6)

Deno 2.6 版本引入了多项重要更新，包括新的 `dx` 工具用于便捷运行 npm 和 JSR 包二进制文件，更细粒度的权限控制，以及通过 `tsgo` 实现更快的类型检查。此外，还新增了 Wasm 源阶段导入、CommonJS 模块的 `--require` 支持、安全审计命令 `deno audit`，以及依赖管理和 Node.js 兼容性的改进。性能优化、API 增强和生活质量提升也是本次更新的亮点。

- 🚀 **`dx` 工具**：类似 `npx`，用于运行 npm 和 JSR 包的二进制文件，默认使用 `--allow-all` 权限并提示下载确认。
- 🔒 **细粒度权限控制**：新增 `--ignore-read` 和 `--ignore-env` 标志，允许选择性忽略文件读取或环境变量访问，提升安全性。
- ⚡ **更快类型检查**：集成实验性 `tsgo` 类型检查器（用 Go 编写），类型检查速度提升约 2 倍，并改进语言服务器功能。
- 🧩 **Wasm 源阶段导入**：支持直接导入 Wasm 模块的原始源码，提升 WebAssembly 开发效率。
- 📦 **CommonJS 支持**：新增 `--require` 标志，用于在运行主模块前加载 CommonJS 模块，增强 Node.js 兼容性。
- 🛡️ **安全审计**：引入 `deno audit` 命令，扫描依赖中的安全漏洞，支持 GitHub CVE 数据库和 socket.dev 集成。
- 📊 **依赖管理改进**：新增 `deno approve-scripts` 命令控制生命周期脚本，支持设置依赖最小年龄，优化锁文件和工作流。
- 🔧 **捆绑器增强**：改进 Web Workers 支持，正确处理运行时特定说明符（如 `cloudflare:` 和 `bun:`），提升兼容性。
- 🔄 **Node.js 兼容性**：默认包含 `@types/node` 类型声明，修复大量 Node.js API 问题，覆盖文件系统、加密、进程等模块。
- 🆕 **API 变更**：稳定 `BroadcastChannel` API，支持 Web 流的可转移性，`ImageData` 新增 `Float16Array` 支持。
- 🚄 **性能优化**：修复 `fetch` API 内存泄漏，优化 V8 引擎集成，提升 Node.js 兼容层性能。
- ✨ **生活质量提升**：改进测试覆盖率收集、错误堆栈跟踪、命令行自动补全，新增 `--empty` 标志初始化空项目。
- 🔧 **V8 14.2 升级**：更新至 V8 引擎 14.2 版本，带来性能改进和新 JavaScript 特性。

---

### [CERN 如何利用 TimescaleDB 推动突破性物理研究 | 虎数据](https://www.tigerdata.com/blog/how-cern-powers-ground-breaking-physics-with-timescaledb)

**原文标题**: [How CERN Powers Ground-Breaking Physics with TimescaleDB | Tiger Data](https://www.tigerdata.com/blog/how-cern-powers-ground-breaking-physics-with-timescaledb)

欧洲核子研究中心（CERN）利用 TimescaleDB 替代传统 Oracle 数据库，构建下一代数据归档系统（NGA），以应对大型强子对撞机等实验产生的海量时间序列数据管理挑战。该系统显著提升了数据写入效率、存储压缩率和查询性能，并计划于 2027 年前全面投入生产环境。

- 🚀 **应对数据挑战**：CERN 原有基于 Oracle 的归档系统存在架构僵化、性能瓶颈等问题，无法高效处理每日数百 GB 的时间序列数据。
- 🔧 **新一代归档方案**：与西门子合作开发 NGA 系统，采用可插拔后端设计，支持 PostgreSQL 和 TimescaleDB，已部署约 500 套子系统。
- 📊 **性能优势显著**：TimescaleDB 写入吞吐量达每秒 7.7 万行（超需求 3 倍），列式压缩使存储空间减少 78%-95%，查询速度提升 10-40 倍。
- ⚙️ **核心功能应用**：通过超表自动分区简化架构，并利用持续聚合功能实现高效数据汇总，为高频率信号可视化提供关键技术支撑。
- 🎯 **生产部署规划**：基于数据库按需服务（DBOD）进行标准化部署，目标在 2027 年实现 CERN 全范围生产环境应用。

---

### [Node.js — 2025 年 12 月 18 日星期四安全版本发布](https://nodejs.org/en/blog/vulnerability/december-2025-security-releases)

**原文标题**: [Node.js — Thursday, December 18, 2025 Security Releases](https://nodejs.org/en/blog/vulnerability/december-2025-security-releases)

Node.js 项目将于 2025 年 12 月 18 日或稍后发布安全更新，涵盖多个版本线，以修复多个安全漏洞，并提醒用户关注版本生命周期以确保系统安全。

- 🚨 **安全更新延期**：原定 12 月 15 日的发布因技术挑战推迟至 12 月 18 日或稍后  
- 📅 **影响版本**：25.x、24.x、22.x、20.x 版本线均受多个高、中、低危漏洞影响  
- ⚠️ **漏洞统计**：共涉及 3 个高危、1 个中危和 1 个低危安全问题  
- 🔄 **版本支持**：已结束生命周期的版本仍可能受漏洞影响，建议及时更新  
- 📢 **信息渠道**：可通过官方安全页面、GitHub 安全流程及邮件列表获取更新

---

### [Mongoose 9.0：异步堆栈追踪、更简洁的中间件与更严格的 TypeScript 支持 | www.thecodebarbarian.com](https://thecodebarbarian.com/mongoose-9-async-stack-traces-cleaner-middleware-stricter-typescript.html)

**原文标题**: [Mongoose 9.0: Async Stack Traces, Cleaner Middleware, Stricter TypeScript | www.thecodebarbarian.com](https://thecodebarbarian.com/mongoose-9-async-stack-traces-cleaner-middleware-stricter-typescript.html)

Mongoose 9.0 版本引入了异步堆栈跟踪、完全异步的中间件以及更严格的 TypeScript 支持，显著提升了调试体验和开发效率。

- 🐛 **异步堆栈跟踪**：Mongoose 9 全面采用异步函数，使 Node.js 能显示完整的异步调用链，便于准确定位错误源头。
- 🔄 **中间件完全异步化**：移除了基于回调的 `next()` 和 `done()` 支持，强制使用基于 Promise 或 async/await 的中间件，确保异步堆栈跟踪的完整性。
- 📝 **更严格的 TypeScript 类型**：查询过滤器和创建操作的类型检查更加严格，提供了更好的自动补全和错误预防，提升了开发体验。

---

### [pnpm 10.26 | pnpm](https://pnpm.io/blog/releases/10.26)

**原文标题**: [pnpm 10.26 | pnpm](https://pnpm.io/blog/releases/10.26)

pnpm 10.26 版本引入了更严格的安全默认设置，包括对 Git 托管依赖的脚本执行限制、新增 `allowBuilds` 配置以精细控制构建脚本权限，以及阻止非标准协议传递依赖的功能，同时增强了锁文件完整性和打包命令的预览支持。

- 🔒 Git 托管依赖现在默认阻止运行 `prepare` 脚本，需在 `allowBuilds` 中显式允许，防止恶意代码执行
- ⚙️ 新增 `allowBuilds` 配置，支持按包名灵活允许或禁止脚本执行，取代 `onlyBuiltDependencies` 和 `ignoredBuiltDependencies`
- 🚫 新增 `blockExoticSubdeps` 设置，可阻止传递依赖使用非标准协议（如 `git+ssh:`），仅允许直接依赖使用
- 🔐 为 HTTP tarball 依赖计算并存储完整性哈希到锁文件，确保后续安装时内容未被篡改
- 📦 `pnpm pack` 命令新增 `--dry-run` 选项，可预览打包文件列表而不实际创建压缩包
- 📋 在表格/列表格式中显示已弃用版本的最新状态
- 🧹 在 `deploy` 命令中从锁文件移除 `injectWorkspacePackages` 设置
- 🔗 标准化锁文件中 tarball URL 的存储格式，修复重定向不可变依赖的 URL 处理问题

---

### [错误](https://nodeweekly.com/link/178475/web)

**原文标题**: [Error](https://nodeweekly.com/link/178475/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='nodeweekly.com', port=443): Max retries exceeded with url: /link/178475/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [Node.js 文件读写操作 - 现代完整指南](https://nodejsdesignpatterns.com/blog/reading-writing-files-nodejs/)

**原文标题**: [Reading and Writing Files in Node.js - The Complete Modern Guide](https://nodejsdesignpatterns.com/blog/reading-writing-files-nodejs/)

本文全面介绍了现代 Node.js 中文件读写的多种方法，涵盖从基础的 Promise API 到高级的流处理，旨在帮助开发者根据文件大小和场景选择最高效、最合适的技术。

- 📄 **使用 Promise API 处理中小文件**：通过`fs/promises`模块的`readFile`和`writeFile`方法，结合`async/await`语法，可以简洁地处理文本、JSON 或二进制文件。需用`try/catch`妥善处理`ENOENT`（文件不存在）、`EACCES`（权限不足）等常见错误。
- 🔀 **利用并发提升多文件处理性能**：使用`Promise.all()`或`Promise.allSettled()`可以并发读取或写入多个文件，显著提升 I/O 密集型操作的效率。`Promise.all()`在任一操作失败时立即拒绝，而`Promise.allSettled()`会等待所有操作完成。
- 🚫 **避免在并发环境中使用同步方法**：`readFileSync`和`writeFileSync`等同步方法会阻塞事件循环，仅适用于 CLI 工具或构建脚本等非并发场景，绝不能在 Web 服务器中使用。
- 🐘 **使用流（Streams）高效处理大文件**：对于超过 100MB 的大文件或内存受限的场景，应使用`createReadStream`和`createWriteStream`。流可以分块处理数据，内存占用恒定，并能通过`pipeline()`函数优雅地组合多个处理步骤，自动处理背压和错误。
- 🔧 **通过文件句柄进行底层精细控制**：`fs/promises`的`open()`方法返回文件句柄，配合`read()`和`write()`方法可以手动控制读写的位置与缓冲区大小，适用于需要精确操作的场景，但务必在`finally`块中调用`close()`以释放资源。
- 📁 **操作目录与路径**：使用`readdir`读取目录内容，`stat`获取文件信息，`mkdir`创建目录（`{ recursive: true }`可创建嵌套目录）。结合`path.join`和`import.meta.dirname`可以构建相对于当前脚本的可靠路径。
- ✅ **遵循最佳实践**：根据文件大小选择技术栈，妥善处理特定错误码，合理设置流的缓冲区大小（`highWaterMark`），并始终确保清理资源（关闭文件句柄或使用`pipeline`）。

---

### [如何使用 Foxit REST API 从 PDF 中提取文本 - Foxit](https://developer-api.foxit.com/developer-blogs/api-guides-tutorials/pdf-services-api/how-to-extract-text-from-pdfs-using-foxits-rest-apis/?utm_source=cooperpress&utm_medium=Display&utm_campaign=12-16-25)

**原文标题**: [How to Extract Text from PDFs using Foxit's REST APIs - Foxit](https://developer-api.foxit.com/developer-blogs/api-guides-tutorials/pdf-services-api/how-to-extract-text-from-pdfs-using-foxits-rest-apis/?utm_source=cooperpress&utm_medium=Display&utm_campaign=12-16-25)

我们很高兴在 API World 2025 与开发者交流，展示 Foxit API 如何驱动从 AI 简历生成到互动涂鸦应用的各种创新。本文将重现 Jorge Euceda 在台上演示的实操流程，介绍如何利用 Foxit PDF 服务和文档生成 API 构建一个可审计的 AI 驱动文档自动化系统。

- 📄 演示基于 Foxit API 构建可审计的 AI 驱动文档自动化流程
- 🤖 结合 PDF 服务和文档生成 API 实现智能文档处理
- 🛠️ 提供从 AI 简历生成到互动应用的实际案例参考
- 🔍 强调工作流的可追踪性与审计功能设计

---

### [错误](https://nodeweekly.com/link/178478/web)

**原文标题**: [Error](https://nodeweekly.com/link/178478/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='nodeweekly.com', port=443): Max retries exceeded with url: /link/178478/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [GitHub - goldbergyoni/nodejs-testing-best-practices: Node.js 测试进阶指南。包含一份超全面的最佳实践清单及示例应用（2025 年 4 月）](https://github.com/goldbergyoni/nodejs-testing-best-practices#readme)

**原文标题**: [GitHub - goldbergyoni/nodejs-testing-best-practices: Beyond the basics of Node.js testing. Including a super-comprehensive best practices list and an example app (April 2025)](https://github.com/goldbergyoni/nodejs-testing-best-practices#readme)

该资源是一份关于 Node.js 测试的全面最佳实践指南，包含超过 50 条详细建议、一个示例应用程序以及高级主题（如数据库、外部服务和消息队列测试）。它强调从组件/集成测试开始，覆盖功能而非函数，并在编码过程中编写测试，同时提供了从基础设施设置到具体测试编写的系统化指导。

- 🎯 **测试策略**：首先编写组件/集成测试，仅需少量端到端测试，单元测试仅用于复杂逻辑
- ⏱️ **编写时机**：在编码过程中编写测试，而非完成后，以提供即时反馈和安全网
- 🚪 **覆盖范围**：测试后端的五种可能输出：响应、新状态、外部服务调用、消息队列和可观测性
- 🐳 **基础设施**：使用 Docker Compose 管理测试数据库和基础设施，优化配置以提升性能
- 🔧 **服务器控制**：测试应控制 Web 服务器的启动和停止，并在测试中使用随机端口避免冲突
- 📝 **测试结构**：遵循单元测试最佳实践，使用纯 HTTP 客户端（如 axios）调用 API，按路由和故事组织测试
- 🌐 **外部服务**：使用 HTTP 拦截器（如 nock）隔离组件，模拟各种响应和网络异常
- 🗃️ **数据处理**：每个测试应操作自己的数据，通过公共 API 断言新状态，并选择清晰的数据清理策略
- 📨 **消息队列**：多数测试使用简化的假消息队列，测试消息确认、批处理、毒丸消息和幂等性
- 🎭 **模拟使用**：区分隔离模拟、仿真模拟和实现模拟，避免隐藏模拟，并在每个测试前清理模拟

---

### [我们如何让 JSON.stringify 提速超过两倍 · V8 引擎](https://v8.dev/blog/json-stringify)

**原文标题**: [How we made JSON.stringify more than twice as fast · V8](https://v8.dev/blog/json-stringify)

V8 引擎通过一系列底层优化，使 JSON.stringify 性能提升超过两倍，主要针对常见数据序列化场景实现加速。

- 🚀 新增无副作用快速路径：当序列化对象不会触发副作用（如执行用户代码或垃圾回收）时，采用迭代式专用序列化器，跳过冗余检查并支持更深嵌套结构
- 🔤 字符串编码模板化：针对单字节（ASCII）和双字节字符串分别编译优化版本，根据字符串类型自动切换，避免统一处理的分支开销
- ⚡ SIMD 加速字符串扫描：对长字符串使用硬件 SIMD 指令，短字符串采用 SWAR 位运算技术，批量检测需转义字符，提升扫描效率
- 🏷️ 隐藏类标记优化：对符合条件（无非符号键、可枚举、无转义字符）的对象隐藏类添加标记，后续同结构对象可直接复制键名无需重复验证
- 🔢 升级数字转换算法：用 Dragonbox 算法替换 Grisu3，优化数值到字符串的转换，同时惠及所有 Number.prototype.toString() 调用
- 🧩 分段缓冲区管理：用分块内存区域替代连续缓冲区，避免大型 JSON 序列化时的反复内存重分配和数据拷贝
- ⚠️ 优化适用条件：需使用默认参数（无 replacer/space）、序列化纯数据对象/数组、避免对象包含索引属性，复杂场景将自动回退通用序列化器

---

### [错误](https://nodeweekly.com/link/178481/web)

**原文标题**: [Error](https://nodeweekly.com/link/178481/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='nodeweekly.com', port=443): Max retries exceeded with url: /link/178481/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [利用弱引用颠覆控制](https://jlongster.com/subverting-control-weak-refs)

**原文标题**: [Subverting control with weak references](https://jlongster.com/subverting-control-weak-refs)

弱引用是一种强大的语言特性，它允许在不阻止垃圾回收的情况下引用对象，从而避免内存泄漏，并支持创建灵活的缓存和状态管理方案。

- 🧠 **弱引用的定义与作用**：弱引用不会阻止对象被垃圾回收，与强引用不同，它允许对象在不再被需要时被清理，从而避免内存泄漏。
- 🛠️ **JavaScript 中的弱引用 API**：主要包括`WeakMap`和`WeakRef`，其中`WeakMap`对键保持弱引用，而值保持强引用，常用于缓存场景。
- 💾 **WeakMap 的缓存应用**：通过`WeakMap`可以实现基于对象的缓存，例如缓存函数结果，当对象被垃圾回收时，缓存条目自动移除，无需手动管理内存。
- 🔄 **绕过抽象控制的技巧**：弱引用可用于在无法修改现有类或依赖网络层的情况下，添加缓存或状态管理功能，例如通过`WeakMap`关联额外数据到对象。
- 🧩 **扩展对象功能的模式**：使用`WeakMap`可以模拟“扩展”类，为现有对象添加新功能，而无需修改原始类或担心命名冲突。
- ⚠️ **使用注意事项**：弱引用应谨慎使用，尤其是在直接使用`WeakRef`时，因为它可能导致不可预测的行为，适合作为底层工具。
- 🧰 **实际应用场景**：适用于需要临时缓存、状态跟踪或在不侵入现有代码的情况下增强对象功能的场景，提升代码的灵活性和可维护性。

---

### [WeakRef - JavaScript | MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/WeakRef)

**原文标题**: [WeakRef - JavaScript | MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/WeakRef)

WeakRef 对象允许持有对另一个对象的弱引用，不会阻止该对象被垃圾回收机制回收，但需谨慎使用以避免依赖垃圾回收的具体行为。

- 🎯 WeakRef 持有对目标对象的弱引用，不会阻止垃圾回收器回收该对象
- ⚠️ 应尽量避免使用，因为垃圾回收行为因引擎和版本而异，不可预测
- 🔄 多个 WeakRef 指向同一目标时行为一致，deref() 结果相同
- 🛠️ 构造函数 WeakRef() 创建实例，实例方法 deref() 返回目标对象或 undefined
- 📝 可用于监测 DOM 元素是否存在，并在元素被移除时停止相关操作

---

### [过去十年中众多、众多、众多的 JavaScript 运行时 • Buttondown](https://buttondown.com/whatever_jamie/archive/the-many-many-many-javascript-runtimes-of-the-last-decade/)

**原文标题**: [The many, many, many JavaScript runtimes of the last decade • Buttondown](https://buttondown.com/whatever_jamie/archive/the-many-many-many-javascript-runtimes-of-the-last-decade/)

过去十年间，JavaScript 运行时环境呈现爆炸式增长，从云端、边缘计算到智能电视、移动设备乃至微控制器，JavaScript 已渗透到各种计算场景。这种多样性源于不同场景对性能、资源占用和平台适配的独特需求，使得单一运行时无法满足所有用途。以下是关键发展脉络：

- 🌐 **边缘计算的崛起**：从 2016 年 Lambda@Edge 推出到 Cloudflare Workers 引发技术淘金热，Deno、Bun、WinterJS 等运行时相继涌现，底层引擎也从 V8 扩展到 JavaScriptCore、SpiderMonkey 等
- 🔌 **微控制器上的轻量化引擎**：为适应仅 KB 级内存的硬件，Duktape、JerryScript、Elk 等超轻量引擎出现，催生了 IoT.js、low.js 等物联网运行时
- 🧬 **多语言互操作引擎**：基于 JVM 的 Rhino、Nashorn、Graal.js 实现 Java/JavaScript 双向调用，类似方案还覆盖.NET、Python、Rust 等语言生态
- 📱 **原生应用开发框架演进**：
  - WebView 方案：Cordova/PhoneGap（2009）开启移动跨端，Electron（2013）主导桌面开发，智能电视领域则依赖定制化 Web 运行时
  - 原生渲染方案：React Native（2015）凭借 Hermes 引擎优化启动性能，通过 JSI 实现多引擎支持；NativeScript（2014）提供直接平台绑定
- 🔄 **技术融合趋势**：Node-API 标准逐渐统一原生模块接口，使 React Native、NativeScript 等框架能适配 V8、JSC、Hermes、QuickJS 等多种引擎
- ⚡ **性能与资源权衡**：不同场景对启动速度、内存占用、包体积的要求催生专门优化方案，如面向边缘的 LLRT、面向微控制器的 Elk、面向 React Native 的 Static Hermes

这种繁荣景象证明：JavaScript 已从浏览器语言演变为全栈生态的核心，其成功既源于 Web 技术的普适性，也离不开开发者对"一次编写，处处运行"的不懈追求。未来随着 WASM、边缘计算等技术的发展，JavaScript 运行时生态将继续呈现多元化演进态势。

---

### [Node.js 现已默认支持 TypeScript | Total TypeScript](https://www.totaltypescript.com/typescript-is-coming-to-node-23)

**原文标题**: [Node.js Now Supports TypeScript By Default | Total TypeScript](https://www.totaltypescript.com/typescript-is-coming-to-node-23)

Node.js 23 将原生支持直接运行 TypeScript 文件，无需额外配置或转译步骤，标志着 TypeScript 在 Node.js 生态中的集成迈出重要一步。

- 🚀 **快速体验**：该功能已在 Node Nightly 版本中提供，并计划于 Node 23.6.0 正式发布。
- ⚙️ **运行机制**：Node.js 使用内置的 SWC 工具剥离类型注解后执行代码，但不会进行类型检查。
- 🔍 **类型检查**：开发者仍需通过 `tsc --watch` 等独立进程进行类型验证，确保代码质量。
- 📄 **配置建议**：提供了优化的 `tsconfig.json` 配置，以兼容 Node.js 的 TypeScript 支持，未来 TypeScript 5.8 将提供更便捷的兼容性标志。
- 🚫 **功能限制**：默认不支持枚举和命名空间等 TypeScript 特性，但可通过 `--experimental-transform-types` 标志启用部分扩展功能。
- 🏗️ **生产部署**：对于服务器应用，在冷启动敏感的场景建议转译和压缩代码；对于库和 monorepo 项目，仍推荐预转译为 JavaScript 以优化性能和兼容性。
- 🔄 **版本支持**：该功能将向后移植到 Node 22，但不支持 Node 20，为现有项目升级提供过渡路径。

---

### [Express.js 新篇章：2024 年的辉煌成就与雄心勃勃的 2025 年](https://expressjs.com/2025/01/09/rewind-2024-triumphs-and-2025-vision.html)

**原文标题**: [A New Chapter for Express.js: Triumphs of 2024 and an ambitious 2025](https://expressjs.com/2025/01/09/rewind-2024-triumphs-and-2025-vision.html)

Express.js 在 2024 年完成了治理革新、技术升级与安全强化，并发布了 Express 5.0，为 2025 年的自动化发布、性能优化和持续现代化奠定了坚实基础。

- 🏛️ 治理与社区里程碑：推出 Express Forward Plan，新增技术委员会成员，成立安全工作组，并获 OpenJS Foundation 认证为 Impact Project。
- 🚀 技术进展：发布期待已久的 Express 5.0，启动 Express 6.0 规划，采用新决策框架处理引擎使用和依赖管理。
- 🔒 安全强化：与 OpenJS Foundation 和 OSTIF 合作完成安全审计，快速响应多个 CVE 漏洞，并建立 Never-Ending Support 长期维护计划。
- 🤖 2025 年愿景：自动化 npm 发布流程，引入作用域包，加强安全报告与处理程序，实施性能监控与深度优化。
- 📚 现代化与文档：逐步淘汰猴子补丁和传递 API，更新安全文档，提升开发者体验与框架安全性。

---

### [NodeBB v4.0.0 — 联邦好时光，一起来吧！ | NodeBB 社区](https://community.nodebb.org/topic/18545/nodebb-v4.0.0-federate-good-times-come-on)

**原文标题**: [NodeBB v4.0.0 — Federate good times, come on! | NodeBB Community](https://community.nodebb.org/topic/18545/nodebb-v4.0.0-federate-good-times-come-on)

NodeBB v4.0.0 正式发布，为论坛软件引入了基于 ActivityPub 协议的联邦功能，使 NodeBB 实例之间以及更广泛的联邦宇宙（Fediverse）能够互联互通，用户无需从零培养受众即可接入现有社交网络。

- 🎉 **重大发布**：NodeBB v4.0.0 经过近一年的开发后正式推出，核心特性是支持联邦功能。
- 🌐 **联邦宇宙接入**：通过实现 ActivityPub 协议，NodeBB 论坛可以与其他 NodeBB 实例及任何支持 ActivityPub 的软件（如 Mastodon）进行交互。
- 💡 **开发初衷**：项目始于 2023 年中，初衷是连接不同的 NodeBB 论坛，后在研究过程中发现了 Mastodon 和 ActivityPub 协议，从而转向去中心化互联。
- 💰 **资金支持**：NLNet 基金会旗下的 NGI Zero Core 基金提供了关键资金，使得 NodeBB 能够全力投入并快速实现协议集成。
- ⚙️ **用户可控**：联邦功能作为核心特性内置，但为减少意外，从 v3.x 升级的用户默认禁用该功能，新论坛则默认启用。用户可在管理面板中随时开关或调整相关设置。
- 🤝 **行业协作**：ActivityPub 协议促进了不同组织间的合作，例如 NodeBB 与长期竞争对手 Discourse 的开发团队因此开始了直接交流。
- 📚 **文档与支持**：官方文档已更新以涵盖 v4 的 ActivityPub 功能，并设有专门的支持讨论串供用户咨询。
- 🔗 **快速体验**：现有 NodeBB 用户升级到 v4 后，只需将特定帖子 URL 粘贴到自家论坛的搜索栏，即可跨实例查看并回复内容，直观体验联邦功能。

---

### [TypeScript 5.8 发布公告](https://devblogs.microsoft.com/typescript/announcing-typescript-5-8/)

**原文标题**: [Announcing TypeScript 5.8 - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-5-8/)

TypeScript 5.8 正式发布，引入了多项新特性与优化，包括对条件表达式返回分支的精细类型检查、支持在 CommonJS 中 require() ECMAScript 模块、新增 --module node18 和 --erasableSyntaxOnly 等编译选项，提升了类型安全性、模块互操作性及构建性能。

- 🐛 **精细化的返回表达式分支检查**：在 return 语句中的条件表达式现在会分别检查每个分支是否符合函数声明的返回类型，有助于捕获之前遗漏的类型错误。
- 🔗 **支持 CommonJS 调用 require() 加载 ESM 模块**：在 --module nodenext 下，TypeScript 允许从 CommonJS 模块 require() 导入 ECMAScript 模块，简化了库作者提供 ESM 支持的工作。
- 🏷️ **新增 --module node18 稳定标志**：为 Node.js 18 用户提供了固定的模块解析行为，区别于 nodenext 的某些特性（如禁止 require() ESM 和导入断言）。
- 🧹 **引入 --erasableSyntaxOnly 选项**：此标志会检查并报错那些具有运行时行为的 TypeScript 特定语法（如枚举、命名空间等），确保代码可被安全地擦除为纯 JavaScript。
- ⚙️ **新增 --libReplacement 控制库替换行为**：允许开发者禁用或启用通过 @typescript/lib-* 包替换默认 lib 文件的功能，减少不必要的文件监视开销。
- 📄 **声明文件中保留计算属性名称**：在生成声明文件时，现在会保留类中计算属性名的原始标识符，而非总是转换为索引签名，提高了声明文件的可读性和准确性。
- ⚡ **程序加载与更新的性能优化**：通过减少路径规范化时的数组分配和避免重复验证项目配置，提升了大型项目的构建和编辑响应速度。
- 🚫 **限制在 nodenext 下使用导入断言**：由于 Node.js 22 已弃用 import assert 语法，TypeScript 5.8 在 --module nodenext 下会对使用 assert 的导入报错，推荐改用 import with 属性。

---

### [Node.js — Node.js 在 Discord 上推出官方社区空间](https://nodejs.org/en/blog/announcements/official-discord-launch-announcement)

**原文标题**: [Node.js — Node.js Launches Official Community Space on Discord](https://nodejs.org/en/blog/announcements/official-discord-launch-announcement)

Node.js 官方社区现已在 Discord 平台正式上线，通过与 Reactiflux 社区合作，将原有的 Nodeiflux 服务器升级为官方社区空间，旨在为全球开发者提供一个安全、活跃的交流平台。

- 🎉 Node.js 与 Reactiflux 合作，在 Discord 推出官方社区服务器
- 💬 社区将用于直播、技术讨论、项目分享及与维护者直接交流
- 🌱 这是一个由志愿者运营的有机社区，鼓励成员积极参与建设
- 🤝 服务器由 Node.js 项目与 Nodeiflux 社区共同管理，TSC 提供咨询支持
- 📢 欢迎开发者加入社区，获取最新发布动态、活动信息并反馈建议

---

### [Node.js TSC 投票决定停止分发 Corepack - Socket](https://socket.dev/blog/node-js-tsc-votes-to-stop-distributing-corepack)

**原文标题**: [Node.js TSC Votes to Stop Distributing Corepack - Socket](https://socket.dev/blog/node-js-tsc-votes-to-stop-distributing-corepack)

恶意 NuGet 包通过仿冒流行的.NET 追踪库 Tracer.Fody，利用字形混淆技术窃取 Stratis 钱包的 JSON 文件和密码，并将数据外泄至俄罗斯 IP 地址。

- 🕵️ 恶意包“Tracer.Fody.NLog”通过仿冒合法库“Tracer.Fody”及其作者进行钓鱼攻击
- 🔠 使用同形异义字（homoglyph）技巧伪装包名，诱骗开发者下载
- 💰 专门针对 Stratis 钱包，窃取其 JSON 配置文件和密码信息
- 🌐 将窃取的数据外泄至位于俄罗斯的 IP 地址
- ⚠️ 突显了软件供应链中依赖库安全验证的重要性

---

### [Express@5.1.0：现为 npm 默认版本，附带长期支持时间线](https://expressjs.com/2025/03/31/v5-1-latest-release.html)

**原文标题**: [Express@5.1.0: Now the Default on npm with LTS Timeline](https://expressjs.com/2025/03/31/v5-1-latest-release.html)

Express v5.0.0 已于去年 9 月发布，但直到现在才在 npm 上设为默认版本。团队在过去一年中致力于完善文档、提供迁移支持并确保生态系统兼容性，同时制定了长期支持策略，明确了版本的生命周期阶段。现在 v5.1.0 已成为 npm 上的最新版本，标志着 v5 进入活跃支持阶段，v4 则转入维护阶段。

- 📄 **文档与迁移指南更新**：团队更新了 v5 文档并提供了详细的迁移指南，帮助开发者顺利升级。
- 🔧 **自动化迁移工具**：推出了 codemod 包，自动化处理从 v4 到 v5 的代码迁移，减少手动工作量。
- 🌍 **生态系统兼容性**：考虑到 Express 庞大的生态系统和初学者用户，团队给予了足够时间让中间件和文档更新，确保平稳过渡。
- 🛡️ **长期支持策略**：引入了三个支持阶段：CURRENT（新版本发布后至少 3 个月）、ACTIVE（设为 npm 最新版本后至少 12 个月）和 MAINTENANCE（前一个主要版本进入 12 个月维护期），并提供了 v4 和 v5 的预计时间表。
- 🚀 **v5.1.0 主要更新**：包括支持 Uint8Array、更新依赖版本、添加资金字段、性能优化等，同时更新了多个依赖包。
- 👥 **社区贡献与未来计划**：感谢所有贡献者，并宣布了性能工作组、TypeScript 体验改进等计划，v6 的讨论也已开始。

---

### [Koa - Node.js 的下一代 Web 框架](https://koajs.com/)

**原文标题**: [Koa - next generation web framework for node.js](https://koajs.com/)

Koa 是由 Express 团队设计的新 Web 框架，旨在为 Web 应用和 API 提供更小巧、更具表现力且更稳健的基础。它利用异步函数消除回调并大幅提升错误处理能力，核心不捆绑任何中间件，提供优雅的方法套件使服务器开发快速而愉快。

- 🚀 由 Express 团队打造，追求更轻量、更健壮的 Web 开发基础
- ⚡ 基于异步函数，避免回调并增强错误处理能力
- 🧩 核心不内置中间件，保持高度可定制性
- ✨ 提供优雅 API 方法，提升开发效率与体验

---

### [威胁行为者滥用 Node.js 传播恶意软件及其他恶意负载 | 微软安全博客](https://www.microsoft.com/en-us/security/blog/2025/04/15/threat-actors-misuse-node-js-to-deliver-malware-and-other-malicious-payloads/)

**原文标题**: [Threat actors misuse Node.js to deliver malware and other malicious payloads | Microsoft Security Blog](https://www.microsoft.com/en-us/security/blog/2025/04/15/threat-actors-misuse-node-js-to-deliver-malware-and-other-malicious-payloads/)

自 2024 年 10 月起，微软观察到威胁行为者利用 Node.js 分发恶意软件，通过恶意广告、内联脚本执行等技术窃取信息并渗透数据。攻击链涉及初始访问、持久化、防御规避、数据收集与渗透以及有效载荷执行等多个阶段。

- 🚨 **恶意广告传播**：攻击者利用加密货币交易等主题的恶意广告，诱使用户访问虚假网站并下载伪装成合法软件的恶意安装程序。
- 🔗 **持久化机制**：安装程序中的恶意 DLL 会收集系统信息并创建计划任务，确保 PowerShell 命令持久运行，同时打开伪装的正规网站以迷惑用户。
- 🛡️ **防御规避**：通过计划任务执行 PowerShell 命令，将 PowerShell 进程和当前目录从 Microsoft Defender for Endpoint 扫描中排除，避免检测。
- 📊 **数据收集与渗透**：使用混淆的 PowerShell 脚本从远程 URL 获取并执行脚本，收集 Windows、BIOS、系统及操作系统详细信息，并通过 HTTP POST 发送至 C2 服务器。
- ⬇️ **有效载荷投递**：下载包含 Node.js 运行时、JSC 文件及支持库的压缩包，关闭 Windows 代理设置，并启动 JSC 文件进行下一阶段攻击。
- ⚙️ **内联脚本执行**：攻击者通过 Node.js 直接执行内联 JavaScript 代码，进行网络发现、伪装 C2 流量为 Cloudflare 活动，并通过修改注册表实现持久化。
- 🛠️ **防护建议**：教育用户避免从未经验证的来源下载软件；监控 Node.js 执行；启用 PowerShell 日志记录；部署端点保护；限制出站 C2 通信；并利用 Microsoft Defender XDR 的相关检测规则。

---

### [Node.js — 合作峰会报告：2025 年巴黎 Node.js 协作峰会](https://nodejs.org/en/blog/events/collab-summit-2025-paris)

**原文标题**: [Node.js — Trip report: Node.js collaboration summit (2025 Paris)](https://nodejs.org/en/blog/events/collab-summit-2025-paris)

2025 年巴黎 Node.js 协作峰会汇集了近 40 名现场参与者和十余名远程参与者，围绕 CI 可靠性、WASM 模块、内存安全、协作体验、AsyncLocalStorage 标准化、单可执行应用、Undici 集成、Chrome DevTools 支持等关键议题展开讨论与规划。

- 🛡️ CI 安全事件促使团队重新审视基础设施管理，并分享了自动化流程与稳定性检测方法
- ⚡ 实验性 WASM 模块即将解除标志，计划与浏览器协调后以 semver-minor 版本发布
- 🧠 集成 V8 Oilpan 库以提升内存安全性与垃圾回收效率
- 👥 讨论改进项目导师机制，计划收集反馈并更新 Next-10 计划
- 🔧 协作体验会议指出 CI 不稳定和决策共识过程冗长是主要痛点，提出表情符号投票、AI 总结等改进方案
- 🌐 AsyncLocalStorage 向 Web 标准推进面临安全模型与 API 传播复杂性挑战，enterWith() 替代方案受关注
- 📦 单可执行应用需解决 ESM 支持、工具链优化等问题，当前缺乏志愿者与资金是主要障碍
- 🔗 计划暴露 Undici 调度器配置以提升自定义能力，并探索 HTTP/2 自动升级与 QUIC 支持
- 🔍 与 Chrome DevTools 团队合作增强网络检查与多线程调试功能
- 📊 Next-10 调查问卷优化完成，将于五月开放收集社区意见
- 🧩 模块定制化将优化同步加载路径，并探索通过 AST 重写实现 ESM 插桩的新方案

---

### [Node.js — Node.js v24.0.0（当前版本）](https://nodejs.org/en/blog/release/v24.0.0)

**原文标题**: [Node.js — Node.js v24.0.0 (Current)](https://nodejs.org/en/blog/release/v24.0.0)

Node.js v24.0.0 正式发布，这是最新的“Current”版本，带来了多项重要更新，包括 V8 引擎升级至 13.6、npm 更新至 11，并引入了多项新特性与改进。该版本将于 10 月进入长期支持（LTS）阶段。

- 🚀 **V8 引擎升级至 13.6**：引入了 Float16Array、显式资源管理、RegExp.escape、WebAssembly Memory64 和 Error.isError 等新 JavaScript 特性。
- 📦 **npm 11 更新**：带来性能提升、安全功能增强及更好的现代 JavaScript 包兼容性。
- ⚙️ **Windows 编译工具变更**：移除了 MSVC 支持，现在在 Windows 上编译 Node.js 需使用 ClangCL。
- 🔗 **AsyncLocalStorage 默认使用 AsyncContextFrame**：提供了更高效的异步上下文跟踪实现，提升了性能与健壮性。
- 🌐 **URLPattern 成为全局 API**：无需显式导入即可使用，为 URL 提供了强大的模式匹配功能。
- 🛡️ **权限模型改进**：实验性标志从 `--experimental-permission` 简化为 `--permission`，表明其稳定性增强。
- 🧪 **测试运行器增强**：自动等待子测试完成，无需手动等待测试 Promise，使测试编写更直观。
- 🔄 **包含 Undici 7**：更新了 HTTP 客户端库，带来性能改进和新 HTTP 特性支持。
- ⚠️ **多项 API 弃用与移除**：包括 `url.parse()`、`tls.createSecurePair`、`SlowBuffer` 等的运行时弃用或移除。

---

### [Glitch 即将迎来重要更新](https://blog.glitch.com/post/changes-are-coming-to-glitch/)

**原文标题**: [Important changes are coming to Glitch](https://blog.glitch.com/post/changes-are-coming-to-glitch/)

Glitch 宣布将停止应用托管服务，这是基于平台生态变化和运营挑战的主动调整，旨在将资源集中于为开发者社区提供更高价值的服务。

- 🚫 **停止托管服务**：2025 年 7 月 8 日起，Glitch 将关闭项目托管和用户档案功能，不再提供应用托管服务。
- 💾 **数据保留与迁移**：用户仪表盘将持续开放至 2025 年底，支持代码下载，并新增子域名重定向功能，确保链接可用至 2026 年底。
- 💡 **转型原因**：运营成本上升、平台老化及滥用问题，加上新兴开发平台（如 Fly.io、Deno 等）提供了更优选择，促使 Glitch 重新定位核心价值。
- 🔄 **社区支持**：将提供项目迁移指南、社区论坛答疑，并立即停止新 Glitch Pro 订阅，现有订阅将按比例退款。
- 📧 **持续沟通**：创始人 Anil Dash 鼓励用户通过社区论坛或邮件分享反馈，团队将定期更新进展。

---

### [无缝融合 PHP 与 Node.js](https://blog.platformatic.dev/seamlessly-blend-php-with-nodejs)

**原文标题**: [Seamlessly Blend PHP with Node.js](https://blog.platformatic.dev/seamlessly-blend-php-with-nodejs)

Platformatic 发布了 @platformatic/php-node 模块，它允许在 Node.js 应用中直接嵌入并执行 PHP，实现两种语言的无缝集成，从而在单一环境中结合两者的优势，适用于迁移遗留应用、构建混合应用或创建高性能服务。

- 🚀 **革命性集成**：@platformatic/php-node 是一个基于 Rust 的 Node.js 原生模块，可直接在 Node.js 环境中嵌入 PHP，将其用作强大的请求处理器。
- ⚙️ **工作原理**：通过 Node.js 的工作线程池多线程运行 PHP 实例，使用 Rust 和 lang_handler 系统在语言间传输请求和响应，实现高效、低延迟的处理。
- 🧩 **核心特性**：提供无缝集成、多线程处理、性能提升以及统一的开发环境，减少认知负担并加快开发速度。
- 🛠️ **应用场景**：适用于将遗留 PHP 应用迁移至 Node.js、构建混合应用以及创建需要 PHP 处理的高性能 Web 服务。
- 📦 **快速上手**：通过 `npm install @platformatic/php-node` 安装，详细文档和示例代码可在 GitHub 仓库中找到。
- 🌐 **与 Watt 集成**：可在 Platformatic 的 Node.js 应用服务器 Watt 中运行 PHP，甚至支持复杂应用如 WordPress，并通过 @platformatic/composer 和 @platformatic/next 实现与 Next.js 的前后端分离架构。
- 🔗 **示例演示**：文章提供了完整的代码示例，展示如何创建 PHP 服务、集成 WordPress 以及结合 Next.js 构建现代化、高性能的 Web 应用。

---

### [提案 - 将 Node.js 转为年度主要版本发布并缩短 LTS 支持周期 · Issue #1113 · nodejs/Release · GitHub](https://github.com/nodejs/Release/issues/1113)

**原文标题**: [Proposal - Shift Node.js to Annual Major Releases and Shorten LTS Duration · Issue #1113 · nodejs/Release · GitHub](https://github.com/nodejs/Release/issues/1113)

Node.js 社区正在讨论一项提案，计划将主要版本发布周期从半年一次改为每年一次，并缩短长期支持（LTS）的持续时间，以减轻维护负担、简化版本管理，并为用户提供更清晰稳定的支持路线图。

- 🗓️ 提议将 Node.js 的主要版本发布周期从半年一次改为每年一次，以降低维护复杂性
- ⏳ 建议将长期支持（LTS）总时长从 30 个月缩短至 24 个月，包括 12 个月活跃支持和 12 个月维护支持
- 🧑‍💻 旨在减轻项目维护者的负担，减少多版本并发维护和向后移植修复的工作量
- 🧭 为用户和生态系统提供更简单、可预测的版本采用和支持框架
- ⚖️ 权衡在于可能减缓重大新功能的发布速度，并可能面临习惯较长支持周期的社区的阻力
- 📢 实施策略包括获得技术指导委员会和发布工作组的共识，并配合全面的沟通和文档更新

---

### [TypeScript 5.9 发布公告](https://devblogs.microsoft.com/typescript/announcing-typescript-5-9/)

**原文标题**: [Announcing TypeScript 5.9 - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-5-9/)

TypeScript 5.9 正式发布，带来了多项新功能和改进，包括更精简的 `tsc --init` 配置生成、支持 `import defer` 语法、新增 `--module node20` 选项、DOM API 的摘要描述、可扩展的悬停预览、可配置的悬停长度限制，以及性能优化和部分行为变更。

- 🛠️ `tsc --init` 现在生成更精简且预设了推荐选项的 `tsconfig.json` 文件，提升了新项目的启动体验。
- ⏳ 新增对 ECMAScript `import defer` 语法的支持，允许延迟执行模块及其依赖，直到首次访问其导出，有助于优化启动性能。
- 🖥️ 引入了稳定的 `--module node20` 编译器选项，用于模拟 Node.js v20 的行为，并默认设置 `--target es2023`。
- 📖 为许多 DOM API 添加了基于 MDN 文档的摘要描述，提升了编辑器中的文档提示体验。
- 🔍 预览了“可扩展悬停”功能，允许在编辑器中展开或折叠类型信息的详细视图，便于深入查看复杂类型。
- 📏 支持通过 `js/ts.hover.maximumLength` 设置配置悬停信息的最大长度，且默认长度显著增加，以显示更多内容。
- ⚡ 进行了多项性能优化，包括缓存类型实例化和减少文件存在检查中的闭包创建，提升了编译速度。
- ⚠️ 包含一些行为变更，例如 `lib.d.ts` 的更新可能导致与 `ArrayBuffer` 和 `Buffer` 相关的类型错误，以及类型推断的调整可能引入新错误。

---

### [npm 作者 Qix 因钓鱼邮件在重大供应链攻击中受侵](https://socket.dev/blog/npm-author-qix-compromised-in-major-supply-chain-attack)

**原文标题**: [npm Author Qix Compromised via Phishing Email in Major Suppl...](https://socket.dev/blog/npm-author-qix-compromised-in-major-supply-chain-attack)

恶意 NuGet 包通过字形混淆技术伪装成流行的.NET 追踪库 Tracer.Fody，旨在窃取 Stratis 钱包的 JSON 文件和密码，并将数据外泄至俄罗斯 IP 地址。

- 🕵️ 恶意包“Tracer.Fody.NLog”利用字形混淆技术伪装成合法库“Tracer.Fody”及其作者
- 📦 通过 NuGet 包管理器进行传播，针对.NET 开发者
- 💰 主要目标是窃取 Stratis 加密货币钱包的 JSON 配置文件和密码
- 🌐 窃取的数据被发送至位于俄罗斯的 IP 地址
- ⚠️ 攻击方式为典型的 typosquatting（域名抢注）攻击，利用用户拼写错误
- 🔒 提醒开发者注意软件供应链安全，验证包的真实性

---

### [pnpm 10.16 | pnpm](https://pnpm.io/blog/releases/10.16)

**原文标题**: [pnpm 10.16 | pnpm](https://pnpm.io/blog/releases/10.16)

pnpm 10.16 版本引入了两项主要新功能：一项用于延迟安装新发布的依赖包以增强安全性，另一项支持通过自定义查找器函数进行高级依赖项筛选。此外，该版本还包含多个问题修复。

- 🛡️ 新增 `minimumReleaseAge` 设置，可延迟安装新发布的依赖包（例如设为 1440 分钟即一天），以降低安装到被攻击的恶意包版本的风险，并可通过 `minimumReleaseAgeExclude` 排除特定依赖。
- 🔍 支持在 `.pnpmfile.cjs` 中定义“查找器函数”，使 `pnpm list` 和 `pnpm why` 能通过 `--find-by` 标志，依据依赖项属性（如特定 peerDependencies）进行高级搜索和筛选。
- 🐛 修复了在 Node.js 24 下运行时的弃用警告、`nodeVersion` 需为精确语义版本号的校验、`pnpm publish` 发布 `.tar.gz` 文件的能力，以及使用 Ctrl-C 取消进程后 `pnpm run` 应返回非零退出码的问题。

---

### [将 Node.js HTTP 服务器引入 Cloudflare Workers](https://blog.cloudflare.com/bringing-node-js-http-servers-to-cloudflare-workers/)

**原文标题**: [Bringing Node.js HTTP servers to Cloudflare Workers](https://blog.cloudflare.com/bringing-node-js-http-servers-to-cloudflare-workers/)

Cloudflare Workers 新增对 Node.js 的 `node:http` 客户端和服务器 API 的支持，使开发者能够将现有的 Express.js、Koa 等 Node.js 应用直接部署到边缘网络，享受零冷启动、自动扩展和更低延迟的优势，无需重写代码。

- 🌐 **支持 Node.js HTTP 客户端与服务器 API**：基于 Workers 原生的 `fetch()` API 实现，兼容 `http.get()` 和 `http.request()` 等常用方法，便于在边缘运行现有应用。
- 🔧 **服务器 API 的桥接方案**：通过 `handleAsNodeRequest` 手动集成或 `httpServerHandler` 自动处理，将 Node.js 服务器连接到 Workers 的请求处理模型，支持灵活的路由和中间件整合。
- 🚀 **框架兼容性**：全面支持 Express.js 和 Koa.js 等流行框架，允许直接迁移现有应用，同时可利用 Workers 的全局网络和自动扩展能力。
- ⚙️ **启用方式**：在 Workers 中启用 `nodejs_compat` 兼容性标志（兼容日期晚于 2025-08-15），即可使用 `node:http` 和 `node:https` 模块。
- 📦 **当前限制**：`Agent` API 为无操作，不支持 trailers、early hints、1xx 响应和 TLS 特定选项，但 Workers 自动处理 TLS 和网络优化。

---

### [Cloudflare Workers 中 Node.js 兼容性提升的一年](https://blog.cloudflare.com/nodejs-workers-2025/)

**原文标题**: [A year of improving Node.js compatibility in Cloudflare Workers](https://blog.cloudflare.com/nodejs-workers-2025/)

过去一年，Cloudflare Workers 团队显著提升了与 Node.js 生态系统的兼容性，实现了大量 Node.js 标准库 API 的原生支持，使众多 npm 模块（如 Express）能在 Workers 中无缝运行。这些实现基于 Workers 现有能力（如 Sockets API、Fetch）构建，并引入了虚拟文件系统等新功能，同时通过贡献 Node.js 项目回馈社区。用户可通过启用 `nodejs_compat` 兼容性标志来使用这些功能。

- 🚀 **Node.js 兼容性大幅提升**：Cloudflare Workers 过去一年实现了对 Node.js 广泛生态系统的兼容，支持包括 `express` 在内的数百个流行 npm 模块。
- 📚 **原生标准库支持**：在运行时原生实现了 Node.js 核心模块，如 `node:http`、`node:fs`、`node:crypto` 等，减少了对 polyfill 的依赖，提升了性能和内存效率。
- 🌐 **网络栈集成**：基于 Workers 的 Sockets API 和 Fetch 实现了 `node:http`、`node:https`、`node:net` 等模块，支持创建 HTTP 客户端/服务器及 TCP/TLS 连接。
- 💾 **虚拟文件系统**：为 `node:fs` 模块引入了内存中的虚拟文件系统，支持临时文件操作，并可结合 Durable Objects 实现跨请求共享。
- 🔐 **加密功能完整**：通过 `node:crypto` 模块提供了完整的加密 API，包括哈希、加密、签名等，基于与 Node.js 相同的 `ncrypto` 依赖实现。
- ⚙️ **进程与环境变量**：`node:process` 模块支持 `process.env` 访问环境变量，以及 `stdin/stdout/stderr` 流模拟，便于日志记录和配置管理。
- 🕐 **定时与压缩工具**：实现了 `node:timers` 和 `node:zlib` 模块，提供定时调度和数据压缩功能，增强应用灵活性。
- 🏷️ **灵活启用配置**：可通过 `nodejs_compat` 标志一键启用所有兼容功能，或使用独立标志精细控制模块的启用与禁用。
- 🔄 **生命周期管理**：提供 `remove_nodejs_compat_eol` 等标志，允许用户选择是否排除 Node.js 已终止支持的 API，确保长期兼容性。
- 🤝 **回馈开源生态**：Cloudflare 团队积极参与 Node.js 项目贡献，修复错误、提升性能，并通过 OpenJS 基金会支持关键基础设施。

---

### [基于 Electron 的应用程序在 macOS 26 上引发全系统严重卡顿问题 · Issue #48311 · electron/electron · GitHub](https://github.com/electron/electron/issues/48311)

**原文标题**: [Electron-based apps cause a huge system-wide lag on macOS 26 · Issue #48311 · electron/electron · GitHub](https://github.com/electron/electron/issues/48311)

Electron 应用在 macOS 26 上导致严重的系统卡顿问题。

- 🐛 **问题描述**：在 macOS 26 中，Electron 应用（如 Discord、VS Code）打开或未最小化时，会导致系统整体卡顿，即使 CPU 和 GPU 使用率较低。
- 🖥️ **影响范围**：主要影响 macOS 26（Tahoe RC）用户，尤其是使用 Apple Silicon（如 M1 Max）的设备，macOS 15 无此问题。
- 🎯 **具体表现**：窗口移动、滚动等操作出现卡顿，即使焦点在 Chrome 等其他应用上，只要 Electron 应用未最小化，卡顿仍会发生。
- 🔍 **排查情况**：维护者建议用户通过 Feedback Assistant 向苹果提交反馈，并附上系统诊断报告，初步怀疑是 macOS 问题。
- 📊 **社区反应**：该问题获得大量用户关注（61 个点赞），已标记为 bug 和性能问题，并关联到 Electron 37.x 和 38.x 版本。

---

### [Node.js — Node.js v25.0.0（当前版本）](https://nodejs.org/en/blog/release/v25.0.0)

**原文标题**: [Node.js — Node.js v25.0.0 (Current)](https://nodejs.org/en/blog/release/v25.0.0)

Node.js v25.0.0 正式发布，带来 V8 引擎升级至 14.1 版本，显著提升 JSON.stringify 性能，并内置 Uint8Array 的 base64/hex 转换功能。此版本进一步强化默认安全应用与 Web 标准 API 支持，包括权限模型新增 --allow-net 选项、默认启用 Web Storage，并将 ErrorEvent 设为全局对象。同时，清理了多个长期弃用的 API，并引入了便携式编译缓存等生活质量改进。

- 🚀 V8 引擎升级至 14.1，带来 JSON.stringify 性能大幅提升与内置 Uint8Array base64/hex 转换
- 🔒 权限模型新增 --allow-net 控制网络访问，加强应用默认安全性
- 🌐 Web Storage API 默认启用，ErrorEvent 成为全局对象，更贴近 Web 标准
- 🗑️ 移除或终结 SlowBuffer 等长期弃用的 API，优化代码库
- ⚙️ 新增便携式编译缓存选项，提升开发与部署效率
- 🛠️ 引入 JSPI（JavaScript Promise Integration）支持 WebAssembly，优化异步操作
- 📦 更新 npm 至 11.6.2，并包含多项错误修复与性能改进

---

### [Node.js 24 成为长期支持版本：你需要了解的关键信息](https://nodesource.com/blog/nodejs-24-becomes-lts)

**原文标题**: [Node.js 24 Becomes LTS: What You Need to Know](https://nodesource.com/blog/nodejs-24-becomes-lts)

Node.js 24 已进入长期支持（LTS）阶段，将持续维护至 2028 年 4 月，为生产环境带来更强的安全性、更严格的运行时验证及更完善的 Web API 支持。NodeSource 的 N|Solid 平台已全面支持此版本，确保企业用户能立即采用并享受其高级监控与性能分析功能。

- 🔒 **安全增强**：采用 OpenSSL 3.5，默认安全级别提升至 2，禁止使用弱密钥和 RC4 加密套件。
- 🛡️ **运行时验证更严格**：Buffer、fs.symlink() 等 API 加强参数校验，提前捕获错误。
- 🌐 **Web API 对齐**：新增 CloseEvent、Float16Array 等全局对象，fetch() 实现更规范。
- 📦 **模块互操作性改进**：ESM CommonJS 包装器默认导出 module.exports，简化混合模块使用。
- 📈 **流与 Readline 优化**：改进错误传播和 Unicode 行分隔符处理，提升 I/O 稳定性。
- 🔧 **编译要求更新**：需使用 GCC 12.2+ 或 Xcode 16.1+ 等现代编译器。
- 🗑️ **API 清理**：移除 util.is*() 等已弃用 API，保持核心轻量安全。
- 💻 **平台支持调整**：停止提供 32 位 Windows 二进制文件，macOS 需 13.5 以上版本。
- 🚀 **N|Solid 6.0.2 支持**：完全兼容 Node.js 24 LTS，提供增强的 gRPC 通信和 OpenTelemetry 集成。
- 📅 **多版本 LTS 支持**：N|Solid 同时支持 Node.js 24、22 和 20 LTS 版本，便于企业按需迁移。

---

### [Node.js — Node.js v25.2.1（当前版本）](https://nodejs.org/en/blog/release/v25.2.1)

**原文标题**: [Node.js — Node.js v25.2.1 (Current)](https://nodejs.org/en/blog/release/v25.2.1)

Node.js v25.2.1 版本发布，主要撤销了 localStorage 访问时可能抛出异常的规范兼容行为，将其推迟至 Node.js 26.0.0 实现，同时包含多项修复与更新。

- 🔄 撤销 localStorage 异常行为：因反馈该变更在实验性 API 中破坏性过大，已回退相关改动，计划在 Node.js 26.0.0 中引入
- 🔧 修复 crypto 模块：确保文档中 RSA-PSS 的 saltLength 默认值被正确使用
- 📚 依赖更新：V8 引擎已进行代码回溯
- 📄 文档与代码澄清：明确了 Web Storage 支持仍处于实验阶段的状态
- ⬇️ 提供多平台安装包：包括 Windows、macOS、Linux、AIX 等系统的 64 位及 ARM 架构版本
- 📜 包含完整源代码与文档：可通过官方链接获取详细版本信息和 API 文档

---

### [获取失败](https://nodeweekly.com/link/178508/web)

**原文标题**: [Failed to retrieve](https://nodeweekly.com/link/178508/web)

无法总结：获取内容失败，状态码 403。

---

### [GitLab 发现大规模 npm 供应链攻击](https://about.gitlab.com/blog/gitlab-discovers-widespread-npm-supply-chain-attack/)

**原文标题**: [GitLab discovers widespread npm supply chain attack](https://about.gitlab.com/blog/gitlab-discovers-widespread-npm-supply-chain-attack/)

最全面的 AI 驱动 DevSecOps 平台，提供一体化解决方案。

- 🛡️ 集成安全防护
- 🤖 人工智能驱动
- 🔄 全流程自动化
- 📊 统一管理平台

---

### [获取失败](https://nodeweekly.com/link/178510/web)

**原文标题**: [Failed to retrieve](https://nodeweekly.com/link/178510/web)

无法总结：获取内容失败，状态码 520。

---

### [全栈 Next.js 16 课程 - 通往 Next 之路](https://www.road-to-next.com/?utm_source=node_weekly&utm_medium=referral&utm_campaign=next_course)

**原文标题**: [Full-Stack Next.js 16 Course - The Road to Next](https://www.road-to-next.com/?utm_source=node_weekly&utm_medium=referral&utm_campaign=next_course)

《The Road to Next》是一门专注于使用 Next.js 16 和 React 19 的全栈 Web 开发视频课程，旨在帮助开发者从初级进阶到高级水平。课程包含两个学习路径：Web 开发者旅程和软件工程师旅程，通过构建真实的 SaaS 项目，教授高级 React 概念、后端开发、数据库管理、身份验证、支付集成等全栈技能。学员将获得实战经验、社区支持以及结业证书。

- 🚀 **课程目标**：帮助学员掌握 Next.js 和 React 19，成为全栈开发者或高级软件工程师。
- 🎥 **课程形式**：结合视频教学与实战项目，提供自定进度的学习体验和 Discord 社区支持。
- 💼 **适用人群**：适合前端开发者转型全栈、希望学习高级 React 技术、或计划成为自由职业者或技术创始人。
- 🛠️ **技术栈**：涵盖 Next.js 16、React 19、Prisma、Supabase、TypeScript、Tailwind、Stripe 等现代工具。
- 📚 **课程内容**：包括服务器组件、服务器操作、数据库设计、身份验证、文件上传、消息队列、支付集成等高级主题。
- 🏆 **学员反馈**：学员高度评价课程对服务器组件、身份验证和项目结构的清晰讲解，认为课程提升了他们的技术深度和实战能力。
- 💰 **价格与折扣**：提供两个课程包（$249 起），支持学生折扣、团队许可和分期付款，并附有 14 天退款保证。
- ❓ **常见问题**：课程适合初学者和进阶者，提供英文字幕，推荐使用大屏幕学习，并包含完整的项目启动套件。

---

