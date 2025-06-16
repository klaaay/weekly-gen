### [Node 周刊第 581 期：2025 年 6 月 10 日](https://nodeweekly.com/issues/581)

**原文标题**: [Node Weekly Issue 581: June 10, 2025](https://nodeweekly.com/issues/581)

Node.js 生态系统更新、工具发布及 JavaScript 领域动态概览。

- 🚨 **Node.js 版本警告**：Matteo Collina 提醒用户 Node.js v18 及更早版本已终止支持，建议跳过 v20 直接升级至 v22 以获得最佳未来兼容性。  
- 💡 **TypeScript 支持讨论**：Matteo Collina 探讨是否应在 Node.js 22 中回溯支持 TypeScript。  
- 🏷 **Memetria K/V 服务**：提供 Redis 和 Valkey 托管服务，支持大键追踪和详细数据分析。  
- 🔄 **Node v24.2.0 新特性**：引入`import.meta.main`判断模块是否为入口点，移除 nghttp2 的 HTTP/2 优先级信号支持。  
- 📢 **TC39 提案进展**：包括`Array.fromAsync`、`Error.isError`等新特性讨论。  
- 🧪 **Jest 30 发布**：时隔多年迎来重大更新，包含多项改进。  
- 🔧 **SQLite-JS 扩展**：支持用 JavaScript 编写自定义 SQLite 函数。  
- ♻️ **原生热模块重载**：通过模块钩子实现高效热更新功能。  
- ⚙️ **环境变量管理**：Liran Tal 分享 Node.js 中配置与环境变量的最佳实践。  
- 🔐 **OAuth 解决方案**：Scalekit 推出 MCP Auth 模块，简化令牌管理与追踪。  
- 🛠 **工具推荐**：  
  - � **Orange ORM**：支持 Node、TypeScript 的多数据库 ORM。  
  - 🎭 **Mock Service Worker**：REST/GraphQL API 模拟库。  
  - 🌍 **tz-lookup**：快速根据经纬度估算时区。  
- 📦 **库与框架更新**：  
  - Babel 8 Beta、Prisma 6.9、OpenAI Node 5.2 等发布。  
- 📰 **其他动态**：  
  - Rolldown-Vite 实验版发布，构建速度显著提升。  
  - Gleam 语言编译至 JS 性能提升 30%。  
  - 《State of CSS 2025》调查启动。

---

### [错误](https://nodeweekly.com/link/170180/web)

**原文标题**: [Error](https://nodeweekly.com/link/170180/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='nodeweekly.com', port=443): Max retries exceeded with url: /link/170180/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [Bluesky 上的@nodeland.dev](https://bsky.app/profile/nodeland.dev/post/3lr6qoy5s3p2t)

**原文标题**: [@nodeland.dev on Bluesky](https://bsky.app/profile/nodeland.dev/post/3lr6qoy5s3p2t)

这是一个关于 Node.js 是否应默认支持 TypeScript 的讨论，涉及开发者、维护者及版本兼容性的不同观点。

- 🌐 这是一个高度交互的网络应用，需要 JavaScript 支持  
- 📚 了解更多关于 Bluesky 的信息：bsky.social 和 atproto.com  
- 💬 Matteo Collina（nodeland.dev）发表观点  
- 🔄 开发者呼吁 Node.js 默认支持 TypeScript  
- 🚀 Node.js v24 已默认启用 TypeScript 支持  
- ⚠️ 某流行库维护者反对，认为这会破坏生态系统  
- ❓ 讨论是否应将 TypeScript 支持回溯到 Node.js v22  
- ⏱️ 讨论时间：2025-06-09T15:59:23.849Z

---

### [Node.js — Node v24.2.0（当前版本）](https://nodejs.org/en/blog/release/v24.2.0)

**原文标题**: [Node.js — Node v24.2.0 (Current)](https://nodejs.org/en/blog/release/v24.2.0)

Node.js v24.2.0（Current）版本发布，包含多项重要更新和改进。

- 🚀 **移除 HTTP/2 优先级信号支持**：根据 RFC 9113，nghttp2 中移除了优先级信号支持，Node.js 24 也同步移除了该功能。  
- 🔍 **新增 import.meta.main**：ECMAScript 模块中新增布尔值，用于检测当前模块是否为进程的入口点。  
- 📜 **文档更新与弃用**：  
  - 弃用`util.isNativeError`，推荐使用`Error.isError`。  
  - 弃用向`options.shell`传递空字符串。  
  - 将`Symbol.dispose`和`asyncDispose`从实验性功能转为正式功能。  
- 🛠 **其他重要变更**：  
  - 新增`autoClose`选项到`FileHandle`的`readableWebStream`。  
  - 弃用不通过`new`实例化 HTTP 类。  
  - 新增`http2.server.stream.finish`诊断通道。  
  - 隐式允许应用入口点的`allow-fs-read`权限。  
- 🔧 **构建与依赖更新**：  
  - 更新 nghttp2 至 1.65.0。  
  - 更新 OpenSSL 生成容器至 Ubuntu 22.04。  
  - 更新 undici 至 7.10.0。  
- 📦 **下载与安装**：提供 Windows、macOS、Linux 等多平台的安装包和二进制文件。

---

### [错误](https://nodeweekly.com/link/170183/web)

**原文标题**: [Error](https://nodeweekly.com/link/170183/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='nodeweekly.com', port=443): Max retries exceeded with url: /link/170183/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [权限 | Node.js v24.2.0 文档](https://nodejs.org/api/permissions.html)

**原文标题**: [Permissions | Node.js v24.2.0 Documentation](https://nodejs.org/api/permissions.html)

Node.js 权限模型的文档概述，介绍了如何通过权限控制来限制 Node.js 进程对系统资源的访问。

- 🔒 **权限模型概述**：Node.js 权限模型用于限制进程对特定资源的访问，如文件系统、子进程、Worker 线程等，采用“安全带”机制防止代码无意间修改文件或访问未授权的资源。
- ⚠️ **安全警告**：该模型不针对恶意代码提供保护，恶意代码可能绕过权限限制执行任意操作。
- 🚦 **启用权限**：通过`--permission`标志启用权限模型，默认限制文件系统访问、进程生成、Worker 线程等操作。
- 🛠️ **运行时 API**：`process.permission.has()`用于检查运行时权限，如`fs.read`或`fs.write`。
- 📂 **文件系统权限**：通过`--allow-fs-read`和`--allow-fs-write`标志允许文件系统读写操作，支持通配符和路径指定。
- 🔄 **与 npx 结合使用**：通过`--node-options`传递权限标志，需注意全局`node_modules`或 npm 缓存的读取权限。
- ⛔ **约束条件**：权限不继承到子进程或 Worker 线程，且启用后限制原生模块、子进程、文件系统访问等功能。
- 🔗 **符号链接问题**：符号链接可能绕过权限限制，需确保授权路径不含相对符号链接。

---

### [TC39 推进 Array.fromAsync、Error.isError 及显式资源管理等提案](https://socket.dev/blog/tc39-advances-9-proposals)

**原文标题**: [TC39 Advances Array.fromAsync, Error.isError, and Explicit R...](https://socket.dev/blog/tc39-advances-9-proposals)

Node.js 正通过 Amaro 1.0 迈向稳定的 TypeScript 支持，为官方 .ts 加载功能奠定基础。

- 🚀 Amaro 1.0 发布，推动 Node.js 实现稳定的 TypeScript 支持  
- 🔧 为官方支持 .ts 文件加载功能铺平道路  
- 📅 发布于 2025 年 6 月 10 日，作者 Sarah Gooding

---

### [Jest 30：更快、更精简、更出色 · Jest](https://jestjs.io/blog/2025/06/04/jest-30)

**原文标题**: [Jest 30: Faster, Leaner, Better · Jest](https://jestjs.io/blog/2025/06/04/jest-30)

Jest 30 发布，带来显著性能提升、内存优化及多项新功能，同时包含部分破坏性变更和未来发展规划。

- 🚀 **Jest 30 发布**：重大版本更新，优化性能并减少内存占用，未来计划更频繁发布主版本。  
- ⚠️ **破坏性变更**：  
  - 放弃对 Node 14/16/19/21的支持  
  - 升级`jsdom`至 v26，TypeScript 最低版本要求 5.4  
  - 移除部分`expect`别名，默认排除不可枚举对象属性  
- 📊 **性能提升**：模块解析优化，实测某大型应用测试速度提升 37%，内存占用降低 77%。  
- 🧹 **全局变量清理**：新增警告机制检测未清理的全局变量，未来将自动清理以提升性能。  
- ✨ **新功能亮点**：  
  - 增强 ESM/TypeScript 支持（含`.mts`/`.cts`文件）  
  - 新增`expect.arrayOf`数组匹配器  
  - 支持`using`语法自动恢复 spy  
  - 可配置测试重试策略（延迟或立即重试）  
- 🔧 **实验性 API**：新增`jest.unstable_unmockModule()`和`jest.onGenerateMock()`等高级控制功能。  
- 🔮 **未来计划**：精简核心功能、定期发布周期、提高社区参与度及技术债务清理。  
- 🙏 **致谢**：感谢众多贡献者，特别点名首次提交代码的开发者。  

（注：已知问题涉及`jsdom`兼容性调整可能影响部分用例，如`window.location`模拟）

---

### [GitHub - sqliteai/sqlite-js：用JavaScript创建自定义SQLite函数。直接在JavaScript中扩展数据库，支持标量、聚合、窗口函数和排序规则。](https://github.com/sqliteai/sqlite-js)

**原文标题**: [GitHub - sqliteai/sqlite-js: Create custom SQLite functions in JavaScript. Extend your database with scalars, aggregates, window functions, and collations directly in JavaScript.](https://github.com/sqliteai/sqlite-js)

SQLite-JS 是一个强大的扩展，允许在 SQLite 中使用 JavaScript 创建自定义函数、聚合函数、窗口函数和排序规则，从而直接在数据库中进行灵活的数据操作。

- 🚀 **功能概述**：SQLite-JS 支持标量函数、聚合函数、窗口函数和排序规则，扩展了 SQLite 的功能。
- 📥 **安装**：提供预构建的二进制文件，支持 Linux、macOS、Windows、Android 和 iOS 平台。
- 🔧 **标量函数**：处理单行数据并返回单个值，适用于数据转换和计算。
- 📊 **聚合函数**：处理多行数据并返回聚合结果，如计算中位数。
- 🖼️ **窗口函数**：访问多行数据而不折叠为单行，如计算移动平均值。
- 🔠 **排序规则**：定义自定义文本排序规则，如不区分大小写的自然排序。
- 🔄 **跨设备同步**：与 sqlite-sync 结合使用时，用户定义的函数会自动在 SQLite Cloud 集群中同步。
- 📜 **JavaScript 评估**：直接在 SQLite 查询中评估 JavaScript 代码。
- 🛠️ **示例**：包括字符串操作、统计聚合和自定义窗口函数等实用示例。
- 🔄 **更新函数**：需要通过单独的数据库连接修改现有函数。
- 🏗️ **从源码构建**：提供 Makefile 支持多平台构建。
- 📜 **许可证**：项目采用 MIT 许可证。

---

### [Immaculata.dev - Node.js 中原生的 HMR（技术解析）](https://immaculata.dev/blog/native-nodejs-hmr.html)

**原文标题**: [Immaculata.dev - HMR natively in Node.js (technical write up)](https://immaculata.dev/blog/native-nodejs-hmr.html)

Node.js 中原生实现 HMR（热模块替换）的技术方案，通过模块钩子和依赖树管理实现高效的状态更新。

- 🚀 **快速开发关键**：最小化状态丢弃，避免全量重启，仅使变更模块及其依赖树失效。  
- 🔄 **传统方案缺陷**：使用 `node:vm` 创建次级模块系统，导致逻辑重复且与原生模块隔离。  
- 🛠️ **新方案核心**：通过 `node:module` 原生钩子实现，直接操作模块加载与解析流程。  
- 📂 **文件树管理**：`FileTree` 类内存缓存文件内容，监听变更并标记版本（`?ver=${timestamp}` 自动失效）。  
- ⚡ **依赖追踪**：利用模块钩子动态注册依赖关系，父模块随子模块更新自动失效。  
- 💡 **代码示例**：  
  ```js
  const tree = new FileTree('src', import.meta.dirname);
  registerHooks(useTree(tree));
  tree.watch().on('filesUpdated', async () => { /* 模块按需重执行 */ });
  ```
- 🧩 **扩展应用**：结合 `moduleInvalidated` 事件清理资源（如 Shiki 高亮库的 `dispose` 调用）。  
- 🌟 **优势总结**：无冗余加载、依赖感知、内存高效，且完全基于原生 Node.js 机制。

---

### [解析 Node.js 中的配置与环境变量](https://blog.platformatic.dev/stop-losing-sleep-over-nodejs-config-heres-how-to-get-it-right)

**原文标题**: [Unpacking Config & Env Variables in Node.js](https://blog.platformatic.dev/stop-losing-sleep-over-nodejs-config-heres-how-to-get-it-right)

Node.js 配置管理常被忽视，但错误的配置可能导致安全漏洞或运行时故障。本文探讨了常见问题及解决方案，强调应将配置视为代码同等重要。

- 🚨 **配置问题的普遍性**：几乎所有项目都存在环境变量问题，轻则功能缺失，重则泄露生产环境凭证。  
- 🔍 **问题根源**：开发者常将环境变量视为次要部分，缺乏验证和一致性管理。  
- ⚠️ **安全隐患**：配置错误可能导致密钥泄露、硬编码敏感信息或静默故障。  
- ✅ **最佳实践**：  
  - **立即验证**：使用`env-schema`或`zod`等工具，缺失关键变量时直接崩溃。  
  - **单一数据源**：集中管理多环境配置，避免重复。  
  - **保护密钥**：禁用代码和日志中的敏感信息，使用专业工具（如 AWS Parameter Store）。  
  - **代码化配置**：像对待代码一样版本控制、审核配置。  
- ☸️ **Kubernetes 注意事项**：区分敏感与非敏感配置，避免简单复制`.env`文件，利用原生机制（如 Secrets/ConfigMaps）。  
- 💤 **总结**：严格管理配置是稳定性和安全性的基础，需像应用代码一样重视。  

（附：[相关视频链接](https://www.youtube.com/watch?v=c0PFgihCm9A)）

---

### [MCP 服务器的 OAuth 授权服务 | Scalekit 文档](https://docs.scalekit.com/guides/mcp/oauth/?utm_source=nodeweekly&utm_medium=referral&utm_campaign=mcpauth)

**原文标题**: [OAuth authorization server for MCP servers | Scalekit Docs](https://docs.scalekit.com/guides/mcp/oauth/?utm_source=nodeweekly&utm_medium=referral&utm_campaign=mcpauth)

Scalekit 提供了一套生产就绪的 OAuth 2.1 授权服务器，用于保护 MCP 服务器，支持身份验证、细粒度权限控制和审计跟踪。  

- 🔒 **身份范围访问**：限制每个令牌仅限特定用户或代理使用。  
- 🛠️ **细粒度权限**：通过精细的作用域控制客户端可访问的工具和数据。  
- ✅ **OAuth 2.1 合规**：采用现代、安全且广泛采用的授权标准。  
- 📜 **全面审计跟踪**：记录访问者、时间及权限使用情况。  

### 工作原理  
- ⚙️ **Scalekit OAuth 授权服务器**：负责身份验证、令牌发放和管理 OAuth 2.1 流程。  
- 🛡️ **MCP 服务器**：验证访问令牌并强制执行权限，仅允许有效令牌的请求。  

### 快速入门  
1. **设置授权服务器**  
   - 📝 在 Scalekit 仪表板中配置 MCP 服务器名称、资源标识符和访问控制设置。  
2. **实现资源元数据发现**  
   - 🌐 提供 `.well-known/oauth-protected-resource` 端点，供客户端发现授权服务器。  
3. **在 MCP 服务器中实现授权检查**  
   - 🔑 使用中间件验证令牌，并通过作用域实施细粒度权限控制。  
4. **测试集成**  
   - 🧪 创建测试脚本验证令牌流和 MCP 服务器的响应。  

### 示例端点  
- 📡 **受保护资源元数据**：静态端点返回 MCP 服务器的元数据。  
- 🔗 **授权服务器元数据**：Scalekit 提供的端点，供客户端发现授权服务器功能。

---

### [MCP 服务器的 OAuth 授权服务 | Scalekit 文档](https://docs.scalekit.com/guides/mcp/oauth/?utm_source=nodeweekly&utm_medium=referral&utm_campaign=mcpauth)

**原文标题**: [OAuth authorization server for MCP servers | Scalekit Docs](https://docs.scalekit.com/guides/mcp/oauth/?utm_source=nodeweekly&utm_medium=referral&utm_campaign=mcpauth)

Scalekit 提供了一套生产就绪的 OAuth 2.1 授权服务器，用于保护 MCP 服务器，支持细粒度权限控制和身份验证。  

- 🔒 **身份范围访问**：限制每个令牌仅限特定用户或代理使用。  
- 🛠 **细粒度权限**：通过精细的作用域控制客户端对工具和数据的访问权限。  
- 📜 **OAuth 2.1 合规**：采用现代、安全且广泛采用的授权标准。  
- 📊 **全面审计跟踪**：记录访问者、时间及权限使用情况。  

### 工作原理  
- ⚙ **Scalekit OAuth 授权服务器**：负责身份验证、令牌发放及管理 OAuth 2.1 流程。  
- 🖥 **MCP 服务器**：验证令牌并执行权限控制，仅允许有效令牌的请求。  

### 快速入门  
1. **前提条件**  
   - 📋 拥有 Scalekit 账户及 API 凭证。  
   - 💻 安装 Scalekit SDK：`npm install @scalekit/sdk`。  

2. **设置授权服务器**  
   - 🏷 配置服务器名称、资源标识符（如 `https://your-mcp-server.com`）。  
   - ⚙ 设定令牌生命周期（访问令牌 5 分钟至 1 小时，刷新令牌 5 分钟至 24 小时）。  

3. **实现资源元数据发现**  
   - 🌐 提供 `.well-known/oauth-protected-resource` 端点，列出支持的授权服务器和作用域。  

4. **实施授权检查**  
   - 🔐 使用中间件验证令牌，确保请求携带有效令牌。  
   - 🎯 通过作用域检查实现细粒度权限控制（如 `mcp:tools:weather`）。  

5. **测试集成**  
   - 🧪 模拟客户端获取令牌并访问 MCP 接口，验证权限是否生效。  

### 示例端点  
- 📡 **受保护资源元数据**：`GET /.well-known/oauth-protected-resource`。  
- 🔗 **授权服务器元数据**：`GET /.well-known/oauth-authorization-server`（可选代理）。  

通过 Scalekit 的 OAuth 解决方案，MCP 服务器可快速实现安全、灵活的访问控制。

---

### [错误](https://nodeweekly.com/link/170190/web)

**原文标题**: [Error](https://nodeweekly.com/link/170190/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='nodeweekly.com', port=443): Max retries exceeded with url: /link/170190/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [构建 gRPC Node.js API - Honeybadger 开发者博客](https://www.honeybadger.io/blog/building-apis-with-node-js-and-grpc/)

**原文标题**: [Building a gRPC Node.js API - Honeybadger Developer Blog](https://www.honeybadger.io/blog/building-apis-with-node-js-and-grpc/)

构建更快、更可靠、可扩展且高效的 API 需要选择合适的框架和工具。通信协议对 API 的效能和速度有重要影响。gRPC 是一个强大的远程过程调用（RPC）框架，适用于多种环境，其高性能和低延迟特性使其成为构建 API 的热门选择。

- 🚀 **gRPC 简介**：由 Google 于 2015 年发布的开源 RPC 框架，使用 Protocol Buffers 作为接口定义语言，支持双向流和流量控制，适合微服务架构。  
- 🔧 **工作原理**：客户端通过 RPC 调用远程服务器函数，抽象网络通信复杂性，使用 Protocol Buffers 序列化数据，确保高效传输和强类型。  
- 📡 **HTTP/2支持**：利用 HTTP/2 的多路复用、流量控制和头部压缩，提升性能并降低延迟。  
- 📜 **Protocol Buffers**：高效的数据序列化机制，通过.proto 文件定义数据结构，生成多语言代码，支持前后兼容性。  
- 📚 **示例项目**：构建一个基于 gRPC 的书店 API，包含创建、读取、更新和删除书籍的功能。  
- 🛠️ **设置 Node.js 项目**：安装 Node.js 和 gRPC 依赖，创建 proto 文件定义服务结构和数据格式。  
- 💻 **创建服务器和客户端**：服务器处理数据请求，客户端调用服务方法，演示了创建、读取、更新和删除书籍的操作。  
- ⚖️ **gRPC vs REST vs GraphQL**：gRPC 适合高性能和微服务，REST 易于集成，GraphQL 适合复杂数据模型和客户端灵活性。  
- ✔️ **优点**：高性能、可扩展、强类型、多语言支持。  
- ❌ **缺点**：学习曲线陡峭、兼容性限制、浏览器支持有限。  
- 🌍 **实际应用**：gRPC 适合构建微服务和分布式系统，但不完全替代 REST，需根据项目需求选择协议。

---

### [在 Node.js 中使用 Sequelize 操作 SQL | AppSignal 博客](https://blog.appsignal.com/2025/06/11/using-sql-in-nodejs-with-sequelize.html)

**原文标题**: [Using SQL in Node.js with Sequelize | AppSignal Blog](https://blog.appsignal.com/2025/06/11/using-sql-in-nodejs-with-sequelize.html)

概述  
本文介绍了如何在 Node.js 中使用 Sequelize 操作 SQL 数据库，涵盖从基础设置到 CRUD 操作的完整流程。  

- 🚀 **Sequelize 简介**：Sequelize 是 Node.js 中流行的 ORM 库，支持多种 SQL 数据库，如 PostgreSQL、MySQL 等，允许开发者用 JavaScript 操作数据库。  
- 📚 **数据库基础**：解释了关系型数据库（如 PostgreSQL）与非关系型数据库的区别，强调 SQL 作为标准查询语言的重要性。  
- 🛠️ **项目设置**：演示了如何克隆示例项目、安装依赖，并通过 Fastify 框架启动开发服务器。  
- 🐘 **PostgreSQL 配置**：使用 Docker 快速部署 PostgreSQL 容器，并配置环境变量（如数据库名和密码）。  
- 🔌 **连接数据库**：通过 Sequelize 和`pg`驱动建立 Node.js 与 PostgreSQL 的连接，并测试连接状态。  
- 📝 **模型定义**：创建`Post`模型对应数据库表，定义字段（`id`、`title`、`content`）及同步表结构的方法（`sync()`）。  
- ✏️ **CRUD 操作**：  
  - **创建帖子**：通过`Post.create()`插入数据，并重定向到新帖子页面。  
  - **查询帖子**：使用`findByPk()`获取单条记录，`findAll()`获取全部（支持分页和排序）。  
  - **更新与删除**：通过`save()`和`destroy()`实现编辑和删除功能，可选软删除（`paranoid`模式）。  
- 🏁 **总结与扩展**：建议进一步学习事务、迁移等高级功能，并推荐 Sequelize 官方文档。  

- 💡 **生产建议**：强调分页查询的重要性（`offset`和`limit`），避免性能问题。  
- 🔗 **资源链接**：提供示例代码仓库和 Sequelize 文档参考，方便读者深入实践。

---

### [Node 与 TypeScript 的终极 ORM](https://orange-orm.io/)

**原文标题**: [The ultimate ORM for Node and Typescript](https://orange-orm.io/)

Orange ORM 是一个专为 Node.js、Bun 和 Deno 设计的终极对象关系映射器（ORM），支持多种流行数据库的无缝集成，并提供 TypeScript 和 JavaScript（包括 CommonJS 和 ECMAScript）的全面支持。

- 🚀 **核心特性**  
  - 提供强大且直观的查询模型，便于检索、筛选和操作数据库数据。  
  - 支持 Active Record 模式，语法简洁且富有表现力。  
  - 无需代码生成即可享受完整的 IntelliSense 支持。  
  - 可在浏览器中安全使用，通过 Express.js 插件保护敏感数据库凭证并防止 SQL 注入。  

- 🗃️ **支持的数据库和运行时**  
  - 支持 Node、Deno、Bun、Cloudflare 和 Web 环境。  
  - 兼容 Postgres、PGlite、MS SQL、MySQL、Oracle、SAP ASE、SQLite 和 Cloudflare D1。  

- 💰 **赞助**  
  - 如果认可 Orange 的价值并希望其持续发展，可以考虑赞助支持。  

- 📦 **安装**  
  - 通过 npm 安装：`npm install orange-orm`  

- 📝 **示例代码**  
  - 提供丰富的示例代码，包括表映射、插入、更新、删除和查询操作。  

- 🔄 **并发策略**  
  - 支持乐观并发、覆盖冲突和跳过冲突三种策略，可在表或列级别设置。  

- 🛠️ **高级功能**  
  - 支持批量操作、事务处理、数据验证和复合键。  
  - 提供列和公式鉴别器，用于区分同一表中的不同类型数据。  

- 📊 **聚合函数**  
  - 支持计数、求和、最小值、最大值和平均值等聚合操作。  

- 🔒 **安全性**  
  - 通过 `serializable(false)` 属性防止敏感数据序列化。  
  - 提供日志功能，便于调试和确保数据完整性。  

- ❌ **不支持的功能**  
  - 不处理数据库迁移，建议使用专用迁移工具。  
  - 不支持 NoSQL 数据库和 GraphQL。  

- 📜 **变更日志和行为准则**  
  - 提供详细的变更记录和社区行为准则。

---

### [模拟服务工作者 —— 用于浏览器和 Node.js 的 API 模拟库](https://mswjs.io/)

**原文标题**: [Mock Service Worker - API mocking library for browser and Node.js](https://mswjs.io/)

概述  
Mock Service Worker (MSW) 是一个用于 JavaScript 的 API 模拟库，支持跨框架、工具和环境的客户端无关模拟。它简化了网络行为描述，无需关注请求客户端的实现细节，并支持 REST 和 GraphQL API 的拦截。MSW 基于标准 Fetch API，无需配置或适配器，可在开发、测试和演示中复用相同的模拟逻辑。开发者反馈称其大幅提升了开发效率和测试可靠性，成为工作流程中不可或缺的工具。  

- 🚀 **行业标准** - MSW 是 JavaScript 中 API 模拟的行业标准，支持跨框架和环境的复用。  
- 🔧 **简化开发** - 通过描述网络行为而非模拟请求客户端，简化开发和测试流程。  
- 🌐 **平台兼容** - 基于 Fetch API，兼容 REST 和 GraphQL，无需依赖特定工具或实现细节。  
- 🔄 **高效复用** - 无需额外配置，可在 Vitest、Playwright、Storybook 等工具中复用模拟逻辑。  
- 💡 **开发者好评** - 开发者称赞 MSW 提升效率、简化测试，并成为开发流程中的关键工具。  
- 🛠️ **多场景应用** - 支持本地开发、集成测试、端到端测试和组件展示，覆盖全栈需求。  
- 📢 **社区认可** - 开发者社区广泛认可其易用性和对开发体验的显著改善。  
- 🆓 **开源免费** - 提供三步快速入门指南，开源且免费使用。

---

### [GitHub - mswjs/msw: JavaScript 行业标准的 API 模拟工具](https://github.com/mswjs/msw)

**原文标题**: [GitHub - mswjs/msw: Industry standard API mocking for JavaScript.](https://github.com/mswjs/msw)

Mock Service Worker (MSW) 是一个用于 JavaScript 的行业标准 API 模拟工具，支持浏览器和 Node.js 环境，提供无缝的请求拦截和模拟功能。

- 🚀 **功能强大**：支持 REST 和 GraphQL API 模拟，提供类似 Express 的路由语法，支持参数、通配符和正则表达式匹配。  
- 🔧 **多环境支持**：在浏览器和 Node.js 中均可使用，无需修改应用代码或测试逻辑。  
- 🛠 **开发与测试一体化**：同一套模拟定义可用于本地开发、单元测试、集成测试和 E2E 测试。  
- 📚 **文档丰富**：提供详细的官方文档、快速入门指南和常见问题解答。  
- 🌟 **社区认可**：被 Google、Microsoft、Spotify 等公司广泛使用，并获得多项社区奖项。  
- 💡 **创新技术**：在浏览器中利用 Service Worker API 拦截请求，在 Node.js 中通过低级拦截算法实现模拟。  
- 🤝 **开源支持**：项目依赖社区赞助，提供黄金、白银和青铜赞助等级，支持可持续发展。  
- 📦 **示例丰富**：提供多种使用示例，帮助开发者快速上手。  
- 🎓 **学习资源**：与 Egghead 合作提供付费课程，涵盖 API 模拟和 WebSocket 模拟的最佳实践。

---

### [GitHub - photostructure/tz-lookup：基于位置的时区查询JavaScript库](https://github.com/photostructure/tz-lookup)

**原文标题**: [GitHub - photostructure/tz-lookup: JavaScript Library for Timezone Lookup by Location](https://github.com/photostructure/tz-lookup)

这是一个基于 JavaScript 的时区查询库，通过经纬度快速估算时区，强调高效和小内存占用，但牺牲了一定的准确性。

- 🌍 **项目背景**：fork 自已废弃的 darkskyapp/tz-lookup，由 PhotoStructure 维护，更新了时区数据库至 2025b 版本并加入 TypeScript 支持。
- ⚡ **性能优势**：体积（72kb）比 geo-tz 小 10 倍，查询速度快 100 倍（约 0.05 毫秒/次）。
- ⚠️ **准确性局限**：随机地点误差率约 30%，居住区降至 10%，时区偏移一致时误差 5%（如欧洲维也纳和柏林）。
- 📦 **安装使用**：通过`npm install @photostructure/tz-lookup`安装，支持 Node.js 和浏览器环境，示例代码展示基础调用。
- 🔍 **数据来源**：基于 Evan Siroky 的 timezone-boundary-builder，需 GDAL 工具和 10-30 分钟重新生成数据库。
- 📜 **开源协议**：采用 CC0-1.0，放弃版权限制，衍生改动同样适用。
- 🛠️ **测试与验证**：测试套件对比 geo-tz 结果，提供基准数据，GitHub Actions 自动化测试。

---

### [Babel 8 测试版发布 · Babel](https://babel.dev/blog/2025/05/30/babel-8-beta)

**原文标题**: [Announcing Babel 8 Beta · Babel](https://babel.dev/blog/2025/05/30/babel-8-beta)

Babel 8 Beta 版本发布，标志着经过近两年的开发，所有计划中的破坏性变更已完成，并清理了大量技术债务。团队呼吁用户在实际项目中测试该版本，以确保稳定性。

- 🎉 Babel 8 Beta 发布：历时近两年开发，破坏性变更和技术债务清理完成。  
- 🧪 需要实际项目测试：团队自 Alpha 阶段已使用 Babel 8 转译自身代码，但需更多用户反馈。  
- 📚 升级资源丰富：提供用户迁移指南、API 开发者指南及 Babel 8 文档网站（暂托管于 next.babeljs.io）。  
- 🔄 破坏性变更设计友好：多数变更已在 Babel 7 中通过选项引入，便于提前适配。  
- 📦 ESM 专属包：Babel 8 仅支持 ESM 格式，得益于 Node.js 20 的 `require(esm)` 功能。  
- 🔍 详细变更记录：GitHub 上可查看各 Alpha 版本的完整更新日志。  
- 🚧 后续计划：与主流项目协作确保兼容性、分离 Babel 8 与 7 的代码分支，并修复 Beta 阶段的 Bug。  
- 🐞 呼吁用户参与：鼓励测试并反馈问题至 GitHub Issues。

---

### [发布 6.9.0 版本 · prisma/prisma · GitHub](https://github.com/prisma/prisma/releases/tag/6.9.0)

**原文标题**: [Release 6.9.0 · prisma/prisma · GitHub](https://github.com/prisma/prisma/releases/tag/6.9.0)

Prisma 发布了 6.9.0 稳定版本，主要亮点包括移除了 PostgreSQL 和 SQLite 的 Rust 引擎、本地 Prisma Postgres 的改进、支持其他 ORM 连接 Prisma Postgres、自动备份与恢复功能、VS Code 扩展新增数据库管理 UI，以及新增旧金山（us-west-1）作为 Prisma Postgres 的新区域。

- 🎉 Prisma 6.9.0 稳定版发布，移除 PostgreSQL 和 SQLite 的 Rust 引擎（预览版）  
- 🚀 本地 Prisma Postgres 功能增强，支持多实例并行运行和数据库持久化  
- 🔗 支持通过标准 PostgreSQL 连接字符串连接 Prisma Postgres，兼容其他 ORM 工具  
- 💾 新增自动备份与恢复功能，可通过 Prisma Console UI 操作  
- 🛠️ Prisma VS Code 扩展新增数据库管理 UI，支持远程和本地数据库操作  
- 🌍 新增旧金山（us-west-1）作为 Prisma Postgres 的新区域

---

### [发布 v5.2.0 · openai/openai-node · GitHub](https://github.com/openai/openai-node/releases/tag/v5.2.0)

**原文标题**: [Release v5.2.0 · openai/openai-node · GitHub](https://github.com/openai/openai-node/releases/tag/v5.2.0)

OpenAI 的 Node.js 库 v5.2.0 版本发布，包含新功能、错误修复和文档更新。  

- 🚀 **新功能**：在评估中添加了工具和结构化输出支持（提交 64844f1）。  
- 🐞 **错误修复**：移除了变更日志中的重复条目（提交 18484cc）。  
- 🛠️ **维护**：修复了特定环境下的类型错误问题（提交 44ac3d9）。  
- 📚 **文档更新**：变更日志中引用了 MIGRATION.md 文件（提交 b3d488f），解决了#1539 问题。  
- 🔖 **版本发布**：v5.2.0 于 2025 年 6 月 9 日发布，完整变更日志可查看 v5.1.1 到 v5.2.0 的更新。

---

### [发布 v6.17.0 · mongodb/node-mongodb-native · GitHub](https://github.com/mongodb/node-mongodb-native/releases/tag/v6.17.0)

**原文标题**: [Release v6.17.0 · mongodb/node-mongodb-native · GitHub](https://github.com/mongodb/node-mongodb-native/releases/tag/v6.17.0)

MongoDB Node.js 驱动版本 6.17.0 发布，移除对 MongoDB 4.0 的支持，新增多项功能与修复。

- 🚨 **移除 MongoDB 4.0 支持**：连接至 4.0 或更低版本时将抛出错误。  
- 🔄 **OIDC 机器工作流重试机制**：修复因缓存 OIDC 令牌过期导致的初始认证失败问题，影响环境包括 `azure`、`gcp` 和 `k8s`。  
- ⏱️ **配置 `keepAliveInitialDelay`**：支持在 `MongoClient` 级别设置此参数，默认 120 秒（需以毫秒为单位）。  
- 🔄 **`updateOne` 和 `replaceOne` 支持 `sort` 选项**：与 `find` 操作类似，现可在更新或替换时指定排序规则。  
- 🔌 **`MongoClient.close()` 改进**：关闭时会终止使用中的连接，确保事件循环正常退出。  
- ⏳ **DEK 缓存过期时间配置**：需配合 `mongodb-client-encryption >= 6.4.0`，默认值 60000 毫秒。  
- ❗ **`ignoreUndefined` 严格检查**：若更新操作全为 `undefined` 且启用此选项，将抛出错误以避免意外覆盖文档。  
- 🌐 **套接字错误统一视为网络错误**：修复因服务器断开导致的非网络错误误判问题。  

**修复与优化**：  
- 🐞 修复 OIDC 令牌过期重试逻辑（NODE-6962）。  
- 📄 更新 BSON 至 6.10.4 版本（NODE-6963）。  
- 📚 文档更新与 API 参考完善。  

用户可立即升级并反馈问题至 [NODE 项目](https://github.com/mongodb/node-mongodb-native)。

---

### [发布 v3.9.0 · withcatai/node-llama-cpp · GitHub](https://github.com/withcatai/node-llama-cpp/releases/tag/v3.9.0)

**原文标题**: [Release v3.9.0 · withcatai/node-llama-cpp · GitHub](https://github.com/withcatai/node-llama-cpp/releases/tag/v3.9.0)

node-llama-cpp 项目的 v3.9.0 版本发布，包含新功能、文档更新及错误修复。

- 🚀 **新特性**：引入推理预算（reasoning budget）功能  
- 🧠 **内存优化**：支持滑动窗口注意力（SWA），显著降低上下文内存消耗  
- 📚 **文档完善**：新增对 LLM 友好的文档文件 `llms.md` 和 `llms-full.md`  
- 🐞 **问题修复**：解决提示补全边缘案例和适配 `llama.cpp` 的变更  
- 🔄 **依赖更新**：搭载 `llama.cpp` 的 `b5590` 版本，支持通过命令更新至最新版本  
- ⏰ **发布时间**：2025 年 6 月 4 日，包含 2 次提交至 master 分支

---

### [GitHub - kafkas/firewalk: 一个轻量、快速且内存高效的 Firestore 与 Node.js 集合遍历库](https://github.com/kafkas/firewalk)

**原文标题**: [GitHub - kafkas/firewalk: A light, fast, and memory-efficient collection traversal library for Firestore and Node.js](https://github.com/kafkas/firewalk)

Firewalk 是一个轻量、快速且内存高效的 Firestore 和 Node.js 集合遍历库，适用于处理大规模文档集合的场景。

- 🚀 **核心功能**：提供可配置的遍历器（Traverser）和迁移器（Migrator），支持高效批量处理和并发控制。  
- 📦 **内存优化**：通过分批处理避免一次性加载大量文档导致内存爆炸，适合百万级文档操作。  
- 🔧 **使用场景**：数据库迁移脚本（如新增字段）、定时云函数检查或本地数据检索脚本。  
- 🔄 **兼容性**：需搭配 Firebase Admin SDK 使用，版本需匹配（如 v2 对应 firebase-admin v11-13）。  
- ⚡ **性能调优**：支持调整批次大小（`batchSize`）和并发批次数（`maxConcurrentBatchCount`）以平衡速度与内存。  
- 📚 **示例丰富**：包括批量发送邮件、字段更新/重命名、派生字段等常见操作代码片段。  
- 📜 **开源协议**：采用 MIT 许可证，支持自由使用与修改。  
- 🔗 **文档资源**：提供详细 API 文档和升级指南（如 SemVer 版本管理）。

---

### [GitHub - jhnns/rewire: Node.js 单元测试的简易猴子补丁工具](https://github.com/jhnns/rewire)

**原文标题**: [GitHub - jhnns/rewire: Easy monkey-patching for node.js unit tests](https://github.com/jhnns/rewire)

rewire 是一个用于 Node.js 单元测试的库，允许对模块进行猴子补丁（monkey-patching），以便更方便地注入模拟对象或修改私有变量。

- 🐒 **功能概述**  
  - 提供 `__set__` 和 `__get__` 方法，用于修改和获取模块内的私有变量或依赖。  
  - 支持全局变量（如 `process`、`console`）的局部覆盖，不影响其他模块。  
  - 可通过 `__with__` 临时修改变量，支持同步和异步（Promise）回调。  

- 📦 **安装与使用**  
  - 安装：`npm install rewire`  
  - 用法示例：替换 `fs` 模块、修改路径变量或静默 `console.log`。  

- ⚠️ **限制与注意事项**  
  - 仅支持 CommonJS 模块（不兼容 Babel 转译的 ES 模块）。  
  - 无法修改函数内部变量或模块导出的原始值（如 `module.exports = 2`）。  
  - 每次 `rewire()` 调用会重新执行模块，返回新实例。  

- 🔧 **API 方法**  
  - `rewiredModule.__set__(name, value)`：设置变量并返回还原函数。  
  - `rewiredModule.__with__(obj)`：临时修改变量，自动还原。  
  - 避免使用点符号（如 `myModule.__set__("console.log", fn)`），可能污染全局对象。  

- 🌐 **其他信息**  
  - 许可证：MIT  
  - 社区：3.1k Stars，126 Forks，58k+ 项目使用。  
  - 替代方案：`babel-plugin-rewire` 或 `rewire-webpack`（针对 webpack 场景）。

---

### [获取失败](https://nodeweekly.com/link/170204/web)

**原文标题**: [Failed to retrieve](https://nodeweekly.com/link/170204/web)

无法总结：获取内容失败，状态码 429。

---

### [GitHub - node-hid/node-hid: 通过 Node.js 访问 USB 和蓝牙 HID 设备](https://github.com/node-hid/node-hid)

**原文标题**: [GitHub - node-hid/node-hid: Access USB & Bluetooth HID devices through Node.js](https://github.com/node-hid/node-hid)

node-hid 是一个 Node.js 库，用于访问 USB 和蓝牙 HID 设备。它支持多种平台和 Node.js 版本，并提供了同步和异步 API 来读取和写入设备数据。

- 🔍 **功能概述**：node-hid 允许通过 Node.js 访问 USB 和蓝牙 HID 设备。
- 📜 **许可证**：使用 BSD-3-Clause 许可证。
- ⭐ **受欢迎程度**：在 GitHub 上有 1.5k 星和 288 个 fork。
- 🖥️ **平台支持**：支持 Windows、Mac OS X 10.9+、Linux 等多种平台。
- 🔌 **安装**：通过 `npm install node-hid` 安装，支持大多数标准用例。
- 📚 **示例**：提供多个示例程序，如显示设备列表、控制 LED 和读取输入设备。
- 🔄 **API 类型**：支持同步和异步 API，推荐使用异步 API 以避免阻塞。
- 📖 **文档**：详细说明如何列出设备、打开设备、读取和写入数据等操作。
- 🛠️ **编译支持**：提供从源代码编译的指南，支持多种操作系统。
- ❗ **限制**：无法读取被操作系统占用的设备，如键盘和鼠标。
- 🔧 **开发支持**：提供详细的开发指南和跨平台编译说明。
- 📦 **Electron 和 NW.js 支持**：提供在这些框架中使用 node-hid 的示例和指南。
- ❓ **支持**：通过 GitHub issues 页面提供支持和问题解答。

---

### [GitHub - mochajs/mocha: ☕️ 简单、灵活、有趣的 JavaScript 测试框架，适用于 Node.js 和浏览器](https://github.com/mochajs/mocha)

**原文标题**: [GitHub - mochajs/mocha: ☕️ simple, flexible, fun javascript test framework for node.js & the browser](https://github.com/mochajs/mocha)

Mocha 是一个简单、灵活且有趣的 JavaScript 测试框架，适用于 Node.js 和浏览器环境。它是一个独立且开源的项目，由志愿者维护，并在 npm 上拥有大量依赖。  

- ☕️ **简单灵活**：Mocha 是一个适用于 Node.js 和浏览器的 JavaScript 测试框架，强调简单性和灵活性。  
- 🌟 **受欢迎**：在 npm 上是最受依赖的模块之一，拥有 22.8k GitHub stars 和 3k forks。  
- 📜 **开源许可**：采用 MIT 许可证，由 OpenJS Foundation 及贡献者维护。  
- 🛠 **开发者友好**：提供丰富的文档、问题追踪和 Discord 社区支持，方便开发者参与贡献。  
- 💡 **社区驱动**：鼓励用户和公司赞助，以支持项目维护和新功能开发。  
- 🔍 **多语言支持**：主要使用 JavaScript 开发，同时包含 MDX、Astro 等辅助语言。  
- 🔗 **资源丰富**：提供详细的 README、行为准则、安全策略和贡献指南。

---

### [GitHub - lindell/JsBarcode: 一个用 JavaScript 编写的条形码生成库，适用于浏览器和 Node.js 环境](https://github.com/lindell/JsBarcode)

**原文标题**: [GitHub - lindell/JsBarcode: Barcode generation library written in JavaScript that works in both the browser and on Node.js](https://github.com/lindell/JsBarcode)

JsBarcode 是一个用 JavaScript 编写的条形码生成库，支持多种条形码格式，适用于浏览器和 Node.js 环境。

- 📦 **无依赖**：在网页中使用时无需依赖其他库，但支持与 jQuery 配合使用。
- 🏷 **支持的条形码格式**：包括 CODE128、EAN、UPC、CODE39、ITF、MSI、Pharmacode、Codabar 和 CODE93 等。
- 🌐 **浏览器示例**：通过简单的代码即可生成条形码，支持 SVG、Canvas 和 Image 元素。
- ⚙️ **灵活的配置选项**：可以自定义条形码的格式、颜色、尺寸、文本显示等。
- 📥 **安装方式**：支持通过 CDN、Bower 或 npm 安装，适用于不同开发需求。
- 🖥 **Node.js 支持**：可在 Node.js 环境中使用，支持 Canvas 和 SVG 输出。
- 📜 **开源许可**：采用 MIT 许可证，允许自由修改和商用。
- 🤝 **社区贡献**：欢迎反馈和贡献，提供详细的贡献指南和讨论渠道。
- 📊 **项目活跃**：拥有 5.7k 星标和 1.1k 分支，被 24.3k+ 项目使用。

---

### [发布 v6.4.0 · avajs/ava · GitHub](https://github.com/avajs/ava/releases/tag/v6.4.0)

**原文标题**: [Release v6.4.0 · avajs/ava · GitHub](https://github.com/avajs/ava/releases/tag/v6.4.0)

AVA v6.4.0 版本发布，包含多项更新和改进。

- 🚀 **Node.js 支持更新** - 现已测试支持 Node.js 24，不再支持 v23。  
- 🔒 **npm 发布改进** - 现在发布到 npm 时包含来源证明（provenance attestations）。  
- 🎛️ **交互式观察模式过滤器** - 新增通过 glob 模式过滤测试文件，以及通过匹配标题过滤测试功能。  
- 🧹 **移除 `.only()` 粘性行为** - 作为交互式观察模式改进的一部分，移除了此行为。  
- 📚 **示例更新** - 示例已更新至 AVA 6 版本。  
- 👏 **新贡献者** - 欢迎 @mmulet 和 @kebbell 的首次贡献。  
- 📦 **完整更新日志** - 包含从 v6.3.0 到 v6.4.0 的所有变更。

---

### [介绍 kafka-hooks：轻松连接 Kafka 与 HTTP](https://blog.platformatic.dev/introducing-platformatickafka-hooks-bridging-kafka-and-http-with-ease)

**原文标题**: [Introducing kafka-hooks: Bridging Kafka and HTTP with Ease](https://blog.platformatic.dev/introducing-platformatickafka-hooks-bridging-kafka-and-http-with-ease)

Platformatic 发布了@platformatic/kafka-hooks 库，旨在简化 Apache Kafka 与 HTTP 服务之间的集成，减少样板代码并提供强大的错误处理功能。

- 🚀 **发布消息**：Platformatic 推出@platformatic/kafka-hooks，轻松连接 Kafka 与 HTTP 服务。
- 🔗 **核心功能**：支持 Kafka 消息转发至 HTTP 端点，HTTP 服务发布至 Kafka 主题。
- ⚙️ **配置灵活**：提供可配置的重试策略、并发设置和死信队列（DLQ）功能。
- 🔄 **请求/响应模式**：简化将 Kafka 主题暴露为 HTTP API 的配置。
- 🐳 **快速启动**：提供 docker-compose.yml 文件，方便快速搭建 Kafka 集群。
- 📝 **独立应用**：通过生成器快速创建独立应用，支持通过 HTTP POST 发布消息至 Kafka 主题。
- 🏗️ **架构示例**：展示了如何在 Watt 中使用 kafka-hooks 构建公共 API 与内部服务的集成。
- 🛠️ **技术基础**：基于@platformatic/kafka、@platformatic/service 和 Undici 构建。
- 🔮 **未来计划**：支持更多认证方法、增强监控和集成 Schema Registry。
- 🤝 **社区参与**：欢迎贡献和反馈，项目已在 GitHub 上开源。

---

### [掌握 Node.js 流技术 - Erick Wendel](https://www.nodejsstreams.com/)

**原文标题**: [Mastering Node.js Streams with Erick Wendel](https://www.nodejsstreams.com/)

概述  
本文介绍了 Node.js Streams 的强大功能，适合中高级开发者学习如何高效处理大规模数据，包括视频、音频、数据库集成等，并提供实践项目和测试方法。课程由知名讲师 Erick Wendel 设计，包含独家福利和优惠。

- 🌊 学习 Node.js Streams，处理视频、音频、数据库等大规模数据  
- 🚀 解决性能、扩展性和高成本服务器问题  
- 💡 实践项目包括 CSV 文件处理、视频/音频流、数据库操作等  
- 🧪 学习测试 Streams（使用 Jest 和原生 Node.js）  
- 🌍 讲师 Erick Wendel 拥有全球 10 万 + 学员，获 Google 和微软认证  
- 💰 预注册优惠 50 美元，含 7 天退款保障  
- 📅 课程模块：Streams API、实战项目、多进程/线程等  
- 🎁 独家福利：Discord 社区支持、工作机会和挑战任务  
- 🔒 安全购买，100% 退款保证

---

### [卷下](https://rolldown.rs/)

**原文标题**: [Rolldown](https://rolldown.rs/)

Rolldown 能够轻松处理数以万计的模块，展现出卓越的性能表现。

- 🚀 高效处理：Rolldown 可轻松应对数万模块，性能强劲  
- ⚡ 速度优势：在大量模块处理中表现流畅，无压力  
- 🛠️ 稳定可靠：高负载下仍保持稳定运行，不易崩溃

---

### [宣布推出 Rolldown-Vite | VoidZero](https://voidzero.dev/posts/announcing-rolldown-vite)

**原文标题**: [Announcing Rolldown-Vite | VoidZero](https://voidzero.dev/posts/announcing-rolldown-vite)

Rolldown-Vite 是一个基于 Rust 的新一代打包工具，旨在提升 Vite 的性能，现已达到与当前 Vite 版本的功能对等，可作为直接替代方案使用。早期测试显示，生产构建时间减少了 3 倍至 16 倍，内存使用量降低了 100 倍。未来，Rolldown 将成为 Vite 的默认打包工具。

- 🚀 **性能提升**：Rolldown-Vite 作为 Vite 的替代方案，显著减少构建时间和内存使用。  
- 🔧 **简单替换**：通过修改 `package.json` 或使用 `overrides` 即可轻松切换到 `rolldown-vite`。  
- 🛠 **兼容性优先**：已通过生态系统 CI 测试，但部分框架或高级用例可能存在兼容性问题。  
- 📦 **去除 esbuild 依赖**：内部转换和压缩由 Oxc 处理，提升性能并减少依赖。  
- ⚡ **真实案例效果**：GitLab、Excalidraw 等企业应用构建时间大幅缩短，内存使用显著降低。  
- 🚧 **开发路线图**：分三个阶段逐步将 Rolldown 整合到 Vite 中，最终成为默认打包工具。  
- 💡 **反馈与支持**：鼓励用户试用并提供反馈，以帮助完善 Rolldown-Vite 的功能和稳定性。

---

### [Gleam 语言](https://gleam.run/)

**原文标题**: [Gleam language](https://gleam.run/)

Gleam 是一种结合了强大类型系统、函数式编程表达能力和高并发、容错的 Erlang 运行时的现代编程语言，具有简洁友好的语法和丰富的工具链支持。

- 💪 **强大可靠** - 基于久经考验的 Erlang 虚拟机，支撑过 WhatsApp 等全球级系统，轻松应对任意规模的工作负载
- 🚀 **极致并发** - 采用多核 Actor 模型，支持数百万并发任务，配合不可变数据结构和无停顿的并发垃圾回收
- 🛠️ **开箱即用** - 内置编译器、构建工具、格式化器、编辑器集成和包管理器，创建项目只需`gleam new`命令
- 📦 **生态互通** - 可无缝使用 Erlang/Elixir 生态的数千个开源包，支持跨语言调用
- 🛡️ **安全友好** - 无 null 值、无异常、清晰的错误信息和实用类型系统，显著降低维护成本
- 🌐 **多语言编译** - 除了 BEAM 字节码，还能编译为 JavaScript 并生成 TypeScript 定义，支持浏览器端运行
- 💜 **包容社区** - 欢迎全球不同背景的开发者，倡导友好平等的社区文化
- 📬 **保持联系** - 提供年度通讯订阅，及时获取项目动态

---

### [错误](https://nodeweekly.com/link/170214/web)

**原文标题**: [Error](https://nodeweekly.com/link/170214/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='nodeweekly.com', port=443): Max retries exceeded with url: /link/170214/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [CSS 2025 现状](https://survey.devographics.com/en-US/survey/state-of-css/2025)

**原文标题**: [State of CSS 2025](https://survey.devographics.com/en-US/survey/state-of-css/2025)

概述总结  
该内容主要介绍了 2025 年 CSS 调查的背景、目的、参与方式以及相关常见问题，同时呼吁开发者参与调查，并提供了多语言翻译支持的信息。  

- 🐢 2025 年 CSS 调查的核心愿望：希望 CSS 发展节奏放缓，以便开发者能更好地掌握近年新增的功能（如子网格、`:has()`、滚动驱动动画等）。  
- 📊 调查目的：追踪 CSS 新特性的采用情况，帮助开发者和技术公司决策技术方向，并为浏览器厂商提供优先级参考。  
- ⏳ 调查时间：2025 年 6 月 1 日至 7 月 1 日，结果将在结束后不久发布。  
- 👥 目标人群：任何编写 CSS 的人（职业、学生或爱好者均可参与）。  
- 📝 参与耗时：约 15-20 分钟（所有问题可跳过）。  
- 🌍 多语言支持：感谢全球志愿者提供的翻译（包括中文、日语、西班牙语等 20 余种语言）。  
- 🔍 数据公开：所有数据将公开，供开发者或企业使用。  
- 🏆 主办方：由 Devographics 联合贡献者、翻译者及志愿者共同运营。  
- ❓ 更多详情：可通过公告帖或 FAQ 进一步了解。

---

