### [Node 周刊第 580 期：2025 年 6 月 3 日](https://nodeweekly.com/issues/580)

**原文标题**: [Node Weekly Issue 580: June 3, 2025](https://nodeweekly.com/issues/580)

概述总结  
本期内容涵盖了多个与 Node.js、JavaScript 及相关技术相关的新闻和工具更新，包括 PHP 与 Node.js 的混合开发、AI 工具、新发布的库和框架，以及一些开发者资源。  

- 🚀 **php-node 项目**：一个原生 Node 模块，允许在 Node 环境中运行 PHP 应用，适用于迁移遗留应用或构建混合应用。  
- 🤖 **Tonkotsu**：AI 工具帮助规划项目并分解任务，开发者可作为技术负责人审批 AI 生成的工作。  
- 📢 **Node.js 新闻**：包括 Joyee Cheung 关于 CommonJS 和 ESM 的演讲、OpenJS 基金会成为 CVE 编号机构等。  
- 🛠 **新工具与库**：  
  - **SQLite-JS**：支持用 JavaScript 编写自定义 SQLite 函数。  
  - **Llama Stack**：Meta 的框架，用于在 Node.js 等平台构建 AI 应用。  
  - **qnm**：CLI 工具，用于查看和分析`node_modules`内容。  
  - **Zigar**：支持在 Node 和 Electron 项目中使用 Zig 代码。  
- 🔄 **框架与库更新**：  
  - **OpenAI Client 5.x**：支持最新 OpenAI 模型和 Realtime API。  
  - **Opossum 8.5**：为异步函数提供熔断机制。  
  - **Bun v1.2.15**：新增`bun audit`工具用于依赖安全审计。  
- 📰 **其他新闻**：TC39 会议进展、Stack Overflow 开发者调查回归、Temporal API 前瞻等。

---

### [无缝融合 PHP 与 Node.js](https://blog.platformatic.dev/seamlessly-blend-php-with-nodejs)

**原文标题**: [Seamlessly Blend PHP with Node.js](https://blog.platformatic.dev/seamlessly-blend-php-with-nodejs)

概述总结  
Platformatic 推出了一款革命性的 Node.js 模块`@platformatic/php-node`，旨在无缝集成 PHP 和 Node.js，允许在 Node.js 应用中直接嵌入 PHP 作为请求处理器，从而结合两者的优势。  

- 🚀 **模块介绍**：`@platformatic/php-node`是一个基于 Rust 的 Node.js 原生模块，通过 Node.js 的工作线程池多线程运行 PHP 实例，实现高性能和可扩展性。  
- 🔧 **工作原理**：通过 Rust 和`lang_handler`系统，将 PHP 请求和响应转换为语言无关的格式，并在 Node.js 和 PHP 之间高效传输，避免网络延迟。  
- 🌟 **关键特性**：  
  - 无缝集成 PHP 与 Node.js  
  - 多线程处理 PHP 请求  
  - 提升应用性能  
  - 统一的开发环境  
- 🏗️ **使用场景**：  
  - 迁移遗留 PHP 应用到 Node.js  
  - 构建混合应用  
  - 创建高性能 Web 服务  
- 📦 **快速开始**：通过`npm install @platformatic/php-node`安装，详细文档见 GitHub 仓库。  
- 🛠️ **示例代码**：展示了如何在 Node.js 中实例化 PHP 并处理请求。  
- 💡 **进阶应用**：  
  - 在 Watt（Node.js 应用服务器）中运行 PHP，甚至支持 WordPress。  
  - 结合 Next.js 和 WordPress 构建无头 CMS，实现内容管理与前端展示的分离。  
- 🔗 **资源链接**：  
  - GitHub 示例仓库：[watt-next-wordpress](https://github.com/platformatic/watt-next-wordpress)  
  - 视频教程：[YouTube 演示](https://youtu.be/M4xgE--vALU)  
- 📌 **结论**：`php-node`为现代 Web 开发提供了灵活的工具，支持多语言协作，减少架构复杂性。

---

### [GitHub - platformatic/php-node: Node.js 的 PHP HTTP 请求处理器](https://github.com/platformatic/php-node)

**原文标题**: [GitHub - platformatic/php-node: PHP HTTP Request handler for Node.js](https://github.com/platformatic/php-node)

@platformatic/php-node 是一个允许在 Node.js 进程中运行 PHP 应用的库，支持 Node.js 和 PHP 之间的直接通信，无需网络连接。适用于如 WordPress 与 Next.js 前端结合的复杂场景。

- 🏗️ 项目特性：支持在 Node.js 进程中直接运行 PHP 应用，实现无网络通信。
- 🖥️ 平台支持：目前支持 x64 Linux 和 x64/arm64 macOS，未来可能扩展更多平台。
- 📦 依赖安装：Linux 需安装 libssl-dev 等库，macOS 需通过 Homebrew 安装 openssl@3 等。
- 🔧 安装方法：通过 npm 安装 `@platformatic/php-node`。
- 📝 基本用法：通过 `Php` 和 `Request` 类处理 PHP 请求，支持异步和同步处理。
- ⚙️ API 详解：提供 `Php`、`Request`、`Response` 和 `Headers` 类的详细配置和使用方法。
- 🔄 异步处理：推荐使用 `handleRequest` 方法异步处理请求，避免阻塞 Node.js 线程。
- ⚠️ 同步处理：提供 `handleRequestSync` 方法，但会阻塞线程，不推荐在 HTTP 请求中使用。
- 📜 响应构造：可以手动构造 `Response` 对象，用于测试或特定场景。
- 📌 头信息管理：`Headers` 类支持设置、添加、删除和遍历头信息。
- 🤝 贡献指南：项目属于 Platformatic 生态系统，贡献需参考主仓库指南。
- 📄 许可证：采用 Apache-2.0 许可证。
- ❓ 支持资源：提供 GitHub Issues、文档和 Discord 社区支持。

---

### [joyeecheung/talks · GitHub 上的 master 分支中的 talks/webhackfest_2025/bridging-commonjs-and-esm-in-nodejs.pdf](https://github.com/joyeecheung/talks/blob/master/webhackfest_2025/bridging-commonjs-and-esm-in-nodejs.pdf)

**原文标题**: [talks/webhackfest_2025/bridging-commonjs-and-esm-in-nodejs.pdf at master · joyeecheung/talks · GitHub](https://github.com/joyeecheung/talks/blob/master/webhackfest_2025/bridging-commonjs-and-esm-in-nodejs.pdf)

GitHub 用户 joyeecheung 的 talks 仓库概览，包含代码、关注和项目信息。

- 🏷️ 仓库名称：talks  
- 👥 公开状态：Public（公开）  
- 🔔 通知设置：需登录调整  
- � 派生数：9  
- ⭐ 星标数：232  
- 📜 代码：可访问  
- 🔄 拉取请求：0（无活跃请求）  
- 🏗️ Actions/Projects/Security：无数据或未配置  
- ❗ 错误提示：页面加载异常需刷新  
- 🔍 导航选项：提供 Code/Pull Requests 等常规入口

---

### [OpenJS 基金会成为 40 多个 JavaScript 项目的 CNA](https://socket.dev/blog/openjs-foundation-is-now-a-cna)

**原文标题**: [OpenJS Foundation Is Now a CNA for 40+ JavaScript Projects U...](https://socket.dev/blog/openjs-foundation-is-now-a-cna)

越南封禁 Telegram 后，恶意 Ruby 软件包通过仿冒 Fastlane 插件窃取 Telegram 机器人令牌和消息。  

- 🔍 **恶意软件包**：仿冒 Fastlane 插件的 Ruby gems，利用越南 Telegram 禁令后的需求激增。  
- 💻 **窃取数据**：目标为 Telegram bot 令牌、消息及文件，进行数据外泄。  
- 🚨 **安全威胁**：通过 typosquatting（误植域名）诱导开发者下载恶意包。  
- 📅 **时间节点**：2025 年 6 月 3 日披露，反映攻击者利用时事热点实施攻击。  
- ⚠️ **风险提示**：开发者需谨慎验证第三方依赖，避免供应链攻击。

---

### [GitHub - sqliteai/sqlite-js：用JavaScript创建自定义SQLite函数。直接在JavaScript中扩展数据库，支持标量、聚合、窗口函数和排序规则。](https://github.com/sqliteai/sqlite-js)

**原文标题**: [GitHub - sqliteai/sqlite-js: Create custom SQLite functions in JavaScript. Extend your database with scalars, aggregates, window functions, and collations directly in JavaScript.](https://github.com/sqliteai/sqlite-js)

SQLite-JS 是一个强大的扩展，允许在 SQLite 中使用 JavaScript 创建自定义函数、聚合函数、窗口函数和排序规则，从而直接在数据库中进行灵活的数据操作。

- 🚀 **功能概述**：SQLite-JS 支持标量函数、聚合函数、窗口函数和排序规则，扩展了 SQLite 的功能。
- 📥 **安装**：提供预构建的二进制文件，支持 Linux、macOS、Windows、Android 和 iOS 平台。
- 🔧 **加载扩展**：可以通过 SQLite CLI 或 SQL 语句加载扩展。
- 📊 **标量函数**：处理单行数据并返回单个值，适用于数据转换和计算。
- 📈 **聚合函数**：处理多行数据并返回聚合结果，如计算中位数。
- 🖼️ **窗口函数**：访问多行数据而不折叠为单行，如计算移动平均值。
- 🔠 **排序规则**：定义自定义文本排序规则，如不区分大小写的自然排序。
- 🔄 **同步功能**：与 sqlite-sync 结合使用时，用户定义的函数可以在 SQLite Cloud 集群中自动同步。
- 📜 **JavaScript 评估**：直接在 SQLite 查询中评估 JavaScript 代码。
- 🛠️ **示例**：包括字符串操作、统计聚合和自定义窗口函数等实用示例。
- 🔄 **更新函数**：需要通过单独的数据库连接修改现有函数。
- 🏗️ **从源码构建**：提供 Makefile 支持多平台构建。
- 📜 **许可证**：项目采用 MIT 许可证。

---

### [从提示到应用只需几分钟——DigitalOcean MCP 服务器简介 | DigitalOcean](https://www.digitalocean.com/community/tutorials/control-apps-using-mcp-server)

**原文标题**: [From Prompt to App in Minutes - Introducing the DigitalOcean MCP Server | DigitalOcean](https://www.digitalocean.com/community/tutorials/control-apps-using-mcp-server)

DigitalOcean 推出 MCP 服务器，通过自然语言指令实现 AI 工具与 App Platform 的无缝交互，简化应用部署和管理流程。

- 🚀 **MCP 协议**：Model Context Protocol（模型上下文协议）允许 AI 工具（如 Cursor 和 Claude Desktop）通过结构化方式安全连接外部服务，执行实际操作（如部署应用、查询日志等）。  
- 🔗 **核心功能**：MCP 服务器作为桥梁，支持通过自然语言指令管理 DigitalOcean 应用，包括列出部署、显示日志、创建/删除应用、重启服务等。  
- ⚙️ **快速设置**：需 Node.js 环境、DigitalOcean API 令牌及兼容的 MCP 客户端（如 Cursor 或 Claude Desktop），配置简单，仅需编辑 JSON 文件。  
- 💡 **典型用例**：从 GitHub 仓库直接部署应用、通过聊天指令调整资源配置、实时查看日志或强制重建应用，全程无需手动操作 API 或 YAML。  
- 🌟 **开源扩展**：项目完全开源，鼓励用户反馈以扩展功能（如支持 Droplets、负载均衡器等更多基础设施）。  
- 📚 **学习资源**：提供 MCP 协议教程、Python 实现指南及官方文档链接，助力开发者快速上手。  

（注：摘要已过滤原文中重复的导航菜单和页脚内容，聚焦核心信息。）

---

### [获取失败](https://nodeweekly.com/link/169983/web)

**原文标题**: [Failed to retrieve](https://nodeweekly.com/link/169983/web)

无法总结：获取内容失败，状态码 403。

---

### [获取失败](https://nodeweekly.com/link/169984/web)

**原文标题**: [Failed to retrieve](https://nodeweekly.com/link/169984/web)

无法总结：获取内容失败，状态码 403。

---

### [在 Express.js 中使用 Trunker 管理功能标志 | Blogliorelli](https://blog.migliorelli.dev/posts/managing-feature-flags-in-express-js-with-trunker)

**原文标题**: [Managing Feature Flags in Express.js with Trunker | Blogliorelli](https://blog.migliorelli.dev/posts/managing-feature-flags-in-express-js-with-trunker)

Trunker 是一个轻量级 Express.js 中间件，用于通过功能标志动态控制路由访问，简化功能开关管理。  

- 🚀 **Trunker 简介**  
  - 专为 Express.js 设计的中间件，支持静态或异步功能标志，适用于基于主干开发的场景。  

- 📦 **安装方式**  
  - 通过 `yarn add trunker` 或 `npm` 安装。  

- 🛠️ **基本用法**  
  - 导入后定义功能标志（如 `betaFeature1` 为静态，`betaFeature2` 异步校验用户权限）。  
  - 使用 `trunker.restrict()` 控制路由访问，支持字符串或数组形式标志。  

- 🔍 **手动检查标志状态**  
  - 调用 `isFlagActive(req, "flagName")` 异步验证标志是否启用，灵活处理逻辑分支。  

- 🌐 **了解更多**  
  - 完整文档和源码见 GitHub 仓库，欢迎贡献或反馈问题。

---

### [GitHub - migliorelli/trunker: 一款轻量级 Express.js 中间件，助您实现功能标志](https://github.com/migliorelli/trunker)

**原文标题**: [GitHub - migliorelli/trunker: A lightweight Express.js middleware to help you implement feature flags.](https://github.com/migliorelli/trunker)

一个轻量级的 Express.js 中间件，用于实现功能标志管理，支持静态和动态标志评估，并提供路由访问限制功能。

- 🚀 **功能特点**：简单 API 定义功能标志，支持静态/异步评估，集成环境变量，内置 TypeScript 支持。  
- 📦 **安装方式**：通过`npm install trunker`快速安装。  
- 🛠️ **基础用法**：创建中间件并配置标志（如`betaFeature`），通过`restrict`限制路由访问。  
- 🔧 **动态标志**：支持异步逻辑（如检查用户订阅状态）动态激活标志。  
- 🌐 **环境变量**：使用`TRUNKER_`前缀变量（如`TRUNKER_BETA=true`）动态配置标志。  
- ⚙️ **自定义错误**：可配置 JSON/纯文本错误响应，自定义状态码和提示模板。  
- 📜 **API 方法**：包括`createTrunker`、`fromEnv`、`isFlagActive`等核心方法。  
- 🔒 **TypeScript 支持**：扩展 Express 的`Request`类型，确保类型安全。  
- 📄 **开源协议**：采用 MIT 许可证，代码托管于 GitHub。

---

### [使用可选链编写更可靠的 JavaScript - Matt Smith](https://allthingssmitty.com/2025/06/02/write-more-reliable-javascript-with-optional-chaining/)

**原文标题**: [
    Write more reliable JavaScript with optional chaining - Matt Smith
  ](https://allthingssmitty.com/2025/06/02/write-more-reliable-javascript-with-optional-chaining/)

JavaScript 可选链操作符（?.）提供了一种简洁安全的方式来访问嵌套属性，避免因访问未定义属性而导致的运行时错误。

- 🚀 **可选链简介**：`?.`操作符在访问嵌套属性时，若中间值为`null`或`undefined`，会直接返回`undefined`而非抛出错误。  
- 🔍 **常见场景**：  
  - 🌐 **API 数据访问**：`response?.data?.user?.name`避免因数据缺失导致的错误。  
  - 🖥️ **DOM 操作**：`document.querySelector("#myInput")?.value`安全获取元素值。  
  - 📞 **方法调用**：`user?.sendMessage?.("Hello!")`确保方法存在后再调用。  
- ⚠️ **注意事项**：  
  - 仅对`null`或`undefined`短路，其他假值（如`0`、`""`）仍会继续访问。  
  - 过度使用可能掩盖数据结构问题。  
- 🔄 **替代方案对比**：  
  - 旧写法：`user && user.profile && user.profile.avatar`  
  - 新写法：`user?.profile?.avatar`更简洁清晰。  
- 🛠️ **结合空值合并**：`user?.profile?.avatar ?? "default.png"`提供默认值。  
- 🌍 **浏览器支持**：现代浏览器均支持，IE 需通过 Babel 等工具转换。  
- 💡 **优势总结**：减少冗余代码，提升可读性，避免运行时崩溃。

---

### [构建 Linux 版 Electron 应用 | DoltHub 博客](https://www.dolthub.com/blog/2025-05-29-building-a-linux-electron-app/)

**原文标题**: [Building a Linux Electron App | DoltHub Blog](https://www.dolthub.com/blog/2025-05-29-building-a-linux-electron-app/)

Dolt Workbench 是一个开源的 SQL 工作台，支持 MySQL 和 PostgreSQL 兼容数据库，包括 Dolt 和 DoltgreSQL 等版本控制数据库。团队已成功为 Mac 和 Windows 构建了该应用，但 Linux 用户的需求促使他们进一步开发 Linux 版本。本文详细介绍了构建 Linux 版 Electron 应用的过程，包括选择包格式、配置构建、处理用户数据存储、解决 Chromium 内存限制问题，以及在不同 Linux 系统上运行 AppImage 的方法。

- 🐧 **Linux 用户需求**：数据科学和 DevOps 用户主要使用 Linux，因此支持 Linux 成为重要任务。  
- 📦 **包格式选择**：评估了 AppImage（简单、跨发行版）、Flatpak（强沙盒）和 Snap（自动更新），最终选择 AppImage。  
- ⚙️ **构建配置**：调整 `electron-builder.yaml`，明确指定架构（x64/arm64）并处理 Linux 区分大小写的文件系统。  
- 💾 **用户数据存储**：Linux 使用 XDG 标准目录（如 `~/.local/share` 存放大数据），与 macOS/Windows 路径逻辑不同。  
- 🚨 **Chromium 内存限制**：通过 `disable-dev-shm-usage` 切换至 `/tmp` 避免 `/dev/shm` 崩溃。  
- 🖥️ **AppImage 运行问题**：  
  - Ubuntu 需临时解除沙盒限制或禁用沙盒运行。  
  - NixOS 需 `chmod +x` 并使用 `appimage-run` 工具。  
- 🌟 **社区贡献**：Joop Kiefte 实现了 NixOS 集成（AUR 和 Nixpkg 支持）。  
- 🎉 **跨平台完成**：Dolt Workbench 现全面支持三大平台，欢迎用户通过 Discord 或 GitHub 反馈。

---

### [使用 Pino 在 Node.js 中实现生产级日志记录 · Dash0](https://www.dash0.com/guides/logging-in-node-js-with-pino)

**原文标题**: [Production-Grade Logging in Node.js with Pino · Dash0](https://www.dash0.com/guides/logging-in-node-js-with-pino)

本文介绍了如何在 Node.js 应用中使用 Pino 进行高效的结构化日志记录，并探讨了其与 OpenTelemetry 的集成方法。

- 🌲 Pino 是一个高性能的 Node.js 日志库，以其速度和结构化 JSON 输出著称。
- 📊 支持多种日志级别（trace 到 fatal），默认级别为 info。
- 🎨 可通过 pino-pretty 格式化日志输出，便于开发时阅读。
- ⏱️ 提供多种时间戳格式选项，包括 Unix 时间戳和 ISO 8601。
- 🔍 支持上下文日志记录，可添加请求元数据等额外信息。
- 🚨 内置错误序列化功能，自动记录错误堆栈。
- 🔒 提供敏感数据过滤和脱敏功能，保护隐私信息。
- 📤 可通过传输功能将日志发送到多种目的地（文件、控制台、OTLP 等）。
- 🚀 与 Fastify 和 Express 等框架深度集成，支持请求上下文自动记录。
- 🌐 通过 pino-opentelemetry-transport 包支持 OpenTelemetry 日志数据模型。
- 📈 展示了如何将 Pino 日志发送到 Dash0 等可观测性平台进行集中分析。

---

### [GitHub - ranyitz/qnm: :mag: 用于查询 node_modules 目录的 CLI 工具](https://github.com/ranyitz/qnm)

**原文标题**: [GitHub - ranyitz/qnm: :mag: cli utility for querying the node_modules directory](https://github.com/ranyitz/qnm)

一个用于查询 node_modules 目录的 CLI 工具，支持快速查看模块版本、依赖关系及更多功能。

- 🔍 **功能概述**：快速查询 node_modules 目录中的模块版本，支持 npm 和 yarn。
- ⚡ **性能优势**：相比 `npm list` 更快且输出更简洁。
- 📦 **支持场景**：支持单仓库和查看模块安装原因。
- 🕒 **版本信息**：显示模块发布时间及最新版本。
- 🔎 **模糊搜索**：支持交互式模糊搜索，快速定位模块。
- 📊 **模块分析**：提供 `doctor` 命令分析 node_modules 中最重的模块。
- 📝 **命令列表**：包括 `list`、`match`、`homepage` 等多种实用命令。
- 🌍 **远程数据**：可选是否从 npm 获取远程数据以加快速度。
- 📜 **开源协议**：基于 MIT 许可证，欢迎贡献。
- 🚀 **推荐用法**：建议通过 `npx` 或 `bunx` 运行以获得最佳体验。

---

### [GitHub - chung-leong/zigar: 让 Zig 代码可用于 JavaScript 项目的工具包](https://github.com/chung-leong/zigar)

**原文标题**: [GitHub - chung-leong/zigar: Toolkit enabling the use of Zig code in JavaScript projects](https://github.com/chung-leong/zigar)

Zigar 是一个工具集，允许在 JavaScript 项目中集成 Zig 代码，支持多种平台和运行时环境。

- 🛠️ **功能特性**：支持所有 Zig 数据类型、双向调用、异步任务管理、多线程（原生和 WebAssembly）。
- 🌍 **平台支持**：兼容 MacOS/Linux/Windows（64/32位）、Node.js/Bun.js/Electron/NW.js（原生执行）、Webpack/Rollup/Vite（WebAssembly）。
- 🔢 **版本对应**：主次版本号与 Zig 编译器版本匹配（当前 0.14.0，即将发布 0.14.1）。
- 💬 **技术支持**：可通过项目讨论区或 [ziggit.dev](https://ziggit.dev) 论坛获取帮助。
- 📜 **开源协议**：采用 MIT 许可证，代码托管于 GitHub（271 stars，4 forks）。
- 📦 **相关生态**：提供 Rollup/Vite 插件、运行时库等模块，覆盖完整开发流程。

---

### [家
â¡
Zig 编程语言](https://ziglang.org/)

**原文标题**: [
      Home
      â¡
      Zig Programming Language
    ](https://ziglang.org/)

Zig 是一种通用编程语言和工具链，专注于构建健壮、高效且可复用的软件。

- 🚀 **简单语言**：专注于应用调试而非语言细节，无隐藏控制流、内存分配或预处理器。  
- ⚡ **编译时特性**：基于编译时代码执行的元编程，支持类型操作和跨架构模拟。  
- 🔧 **无缝维护**：可增量改进 C/C++/Zig 代码库，提供零依赖的跨平台 C/C++ 编译器支持。  
- 🌍 **社区驱动**：去中心化社区，鼓励自主创建和管理交流空间。  
- 💻 **开发透明**：主仓库托管于 GitHub，遵循行为准则，接受公开提案讨论。  
- ❤️ **基金会支持**：Zig 软件基金会（非营利组织）通过捐赠维持，资助核心贡献者。  
- 🤝 **企业赞助**：获多家公司及个人（如 GitHub Sponsors）定期资助，保持开源独立性。  
- 🌐 **多语言文档**：提供包括中文在内的多国语言版本。  

代码示例展示了 Zig 的测试功能（如解析整数），体现其简洁性和实用性。

---

### [Bun — 一款全功能高速 JavaScript 运行时](https://bun.sh/)

**原文标题**: [Bun — A fast all-in-one JavaScript runtime](https://bun.sh/)

Bun v1.2.15 是一个快速、全能的 JavaScript 工具包，集成了开发、测试、运行和打包功能，旨在提供极速体验并兼容 Node.js。

- 🚀 **Bun 简介**：Bun 是一个全能的 JavaScript 运行时和工具包，包含打包工具、测试运行器和兼容 Node.js 的包管理器。  
- ⚡ **性能优势**：在 HTTP 请求、WebSocket 消息和数据库查询等基准测试中，Bun 的性能显著优于 Deno 和 Node.js。  
- 📥 **安装方式**：支持 Linux、macOS 和 Windows，可通过 curl 或 PowerShell 一键安装。  
- 🔄 **Node.js 兼容性**：Bun 致力于实现 100% 的 Node.js 兼容性，方便开发者迁移项目。  
- 🏆 **性能对比**：  
  - HTTP 请求：Bun 59,026/s，Deno 25,335/s，Node.js 19,039/s。  
  - WebSocket 消息：Bun 2,536,227/s，Deno 1,320,525/s，Node.js 435,099/s。  
  - 数据库查询：Bun 50,251/s，Node.js 14,398/s，Deno 11,821/s。  
- 🔧 **使用场景**：已被 Express、Postgres 和 WebSocket 等流行工具和框架采用。

---

### [GitHub - openai/openai-node: OpenAI API 官方 JavaScript/TypeScript 库](https://github.com/openai/openai-node)

**原文标题**: [GitHub - openai/openai-node: Official JavaScript / TypeScript library for the OpenAI API](https://github.com/openai/openai-node)

OpenAI 官方提供的 JavaScript/TypeScript 库，用于访问 OpenAI REST API，支持多种运行时环境和高级功能。

- 🚀 **官方库**：OpenAI 提供的 JavaScript/TypeScript 库，用于访问 OpenAI REST API。
- 📦 **安装方式**：支持 npm 和 JSR 安装，适用于 Node.js、Deno 等环境。
- 📄 **文档齐全**：提供详细的 API 文档和代码示例，方便开发者快速上手。
- 🔄 **流式响应**：支持 Server Sent Events (SSE) 实现流式响应处理。
- 📁 **文件上传**：支持多种文件上传方式，包括 Node.js 的 `fs.ReadStream` 和 Web 的 `File` API。
- 🛠 **错误处理**：提供详细的错误类型和状态码，方便调试和处理异常。
- 🔄 **自动重试**：默认对连接错误、超时等自动重试，可配置重试次数。
- ⏱ **超时设置**：支持自定义请求超时时间，默认 10 分钟。
- 🔍 **请求 ID**：每个响应包含 `_request_id`，便于跟踪和调试请求。
- 📡 **实时 API**：支持低延迟、多模态的实时对话体验（目前为 Beta 版本）。
- ☁ **Azure 支持**：提供 `AzureOpenAI` 类，支持 Microsoft Azure OpenAI 服务。
- 📝 **高级用法**：支持自定义 fetch 客户端、代理配置、日志记录等。
- ❓ **常见问题**：详细解答版本兼容性、运行时环境要求等问题。
- 🤝 **贡献指南**：欢迎开发者参与贡献，提供详细的贡献文档。

---

### [发布 v5.0.0 · openai/openai-node · GitHub](https://github.com/openai/openai-node/releases/tag/v5.0.0)

**原文标题**: [Release v5.0.0 · openai/openai-node · GitHub](https://github.com/openai/openai-node/releases/tag/v5.0.0)

OpenAI 的 openai-node 仓库发布了 v5.0.0 版本，包含多项新功能、错误修复和性能改进。

- 🚀 **新功能**：新增音频助手、迁移指南、多个 API 端点（如`/v1/responses`和`/chat/completions`），支持 GPT-4.5 预览版和新图像模型。
- 🐛 **错误修复**：修正了类型解析、音频转录流处理、文件上传等问题，优化了 SSE 块读取。
- ⚡ **性能改进**：默认使用 base64 编码创建嵌入，提高了性能。
- 📚 **文档更新**：添加了示例到 TSDocs，修正了拼写错误，更新了迁移指南。
- ♻️ **重构**：移除了弃用的`runFunctions`方法，重命名了函数助手方法以包含工具。
- 🛠️ **维护**：更新了 CI 配置，修复了测试和内部工具，移除了不再使用的功能。

---

### [负鼠 8.1.3 | 文档](https://nodeshift.dev/opossum/)

**原文标题**: [opossum 8.1.3 | Documentation](https://nodeshift.dev/opossum/)

Opossum 是一个 Node.js 的熔断器库，用于执行异步函数并监控其执行状态。当错误发生时，它会快速失败并支持回退函数。

- 🛠 **功能特性**  
  - 支持熔断器模式，快速失败并自动恢复  
  - 提供回退函数（fallback）处理失败状态  
  - 支持超时、并发控制和健康检查  

- 📊 **监控与统计**  
  - 内置滚动时间窗口统计（如错误率、请求量）  
  - 支持 Prometheus 和 Hystrix 指标导出  

- ⚙️ **配置选项**  
  - 可自定义超时时间、错误阈值、重置时间等  
  - 支持缓存结果和自定义缓存键  

- 🌐 **多环境支持**  
  - 适用于 Node.js 和浏览器端（如 AJAX 调用）  
  - 支持服务器无状态初始化（如 AWS Lambda）  

- 🔊 **事件驱动**  
  - 提供丰富事件（如 `open`、`close`、`fallback`）  
  - 可监听熔断器状态变化和统计快照  

- 🔧 **高级功能**  
  - 支持 AbortController 中止请求  
  - 允许预热期和最小请求量阈值  

- 📦 **扩展性**  
  - 可自定义缓存实现和健康检查逻辑  
  - 提供 TypeScript 类型定义  

示例代码：  
```javascript
const breaker = new CircuitBreaker(apiCall, { 
  timeout: 10000, 
  errorThresholdPercentage: 50 
});
breaker.fire().catch(handleError);
```

---

### [GitHub - nodeshift/opossum: Node.js 断路器 - 快速失败 ⚡️](https://github.com/nodeshift/opossum)

**原文标题**: [GitHub - nodeshift/opossum: Node.js circuit breaker - fails fast  ⚡️](https://github.com/nodeshift/opossum)

Opossum 是一个 Node.js 的熔断器库，用于执行异步函数并监控其执行状态。当出现故障时，Opossum 会快速失败，并支持提供回退函数。该项目适用于浏览器和服务器环境，支持 Prometheus 和 Hystrix 的指标输出。

- ⚡️ **功能特性**：Opossum 是一个 Node.js 熔断器，支持快速失败和回退函数。
- 📜 **许可证**：Apache-2.0 许可证。
- 🌐 **文档**：详细文档可在 [nodeshift.dev/opossum/](https://nodeshift.dev/opossum/) 查看。
- 🛠️ **使用场景**：适用于网络请求、磁盘读取等可能失败的操作。
- ⏱️ **超时设置**：支持设置超时时间、错误阈值百分比和重置超时时间。
- 🚦 **状态管理**：支持断路器状态的初始化和恢复，适用于无服务器环境。
- 📊 **指标输出**：支持 Prometheus 和 Hystrix 的指标输出。
- 🐛 **问题排查**：提供常见问题的解决方案，如 EventEmitter 监听器过多的问题。
- 🌍 **浏览器支持**：可在浏览器中使用，保护 AJAX 调用免受网络故障影响。
- 🔄 **事件监听**：支持多种事件的监听，如成功、失败、超时等。

---

### [GitHub - sebastiancarlos/beachpatrol: 一款替代并自动化日常网页浏览的 CLI 工具](https://github.com/sebastiancarlos/beachpatrol)

**原文标题**: [GitHub - sebastiancarlos/beachpatrol: A CLI tool to replace and automate your daily web browser.](https://github.com/sebastiancarlos/beachpatrol)

Beachpatrol 是一个 CLI 工具，旨在替代并自动化日常网页浏览器的使用，通过 Playwright 脚本实现外部控制，支持 Chromium 和 Firefox，并提供浏览器扩展以增强用户体验。

- 🚀 **功能概述**：Beachpatrol 允许用户通过 CLI 或浏览器扩展自动化浏览器任务，如检查邮件、填写表单、下载文件等。
- 🛠️ **技术细节**：基于 Playwright，使用 patchright 和 puppeteer-extra-plugin-stealth 插件来隐藏自动化痕迹，避免被网站检测到。
- 📂 **安装与使用**：通过克隆仓库、安装依赖并运行 make 命令来安装，支持多配置文件和无痕模式。
- 🤖 **自动化脚本**：用户可以在 beachpatrol/commands 文件夹中创建自定义 Playwright 脚本，并通过 beachmsg 命令运行。
- 🌐 **浏览器扩展**：提供图形界面和热键支持，方便用户调用自动化脚本。
- ⚠️ **已知问题**：Firefox 用户可能会遇到 Cloudflare 误报和额外的 Google 验证码问题。
- 📜 **许可证**：MIT 许可证，欢迎贡献。
- 🔄 **项目状态**：目前处于 alpha 阶段，仅支持 Linux 和 macOS，未来将增加更多功能。

---

### [ESLint v9.28.0 发布 - ESLint - 可插拔的 JavaScript 代码检查工具](https://eslint.org/blog/2025/05/eslint-v9.28.0-released/)

**原文标题**: [ESLint v9.28.0 released - ESLint - Pluggable JavaScript Linter](https://eslint.org/blog/2025/05/eslint-v9.28.0-released/)

ESLint v9.28.0 是一个小版本升级，引入了新功能和错误修复，包括对 TypeScript 语法支持的增强和新的 CLI 选项。

- 🚀 **新增 CLI 选项**：`--pass-on-unpruned-suppressions` 允许忽略未使用的抑制规则，不影响退出代码。  
- 📜 **TypeScript 语法支持**：新增五个核心规则支持 TypeScript 语法，包括 `func-style`、`no-magic-numbers`、`no-shadow`、`no-use-before-define` 和 `prefer-arrow-callback`。  
- 🛠 **功能改进**：包括自定义语言选项序列化、忽略 TypeScript 重载函数声明等。  
- 🐞 **错误修复**：修复全局变量配置、`no-unassigned-vars` 误报等问题。  
- 📚 **文档更新**：新增配置数组说明、插件文档补充等。  
- 🔧 **维护工作**：依赖升级、测试更新、代码重构等。

---

### [发布 v24.0.0 · RobinTail/express-zod-api · GitHub](https://github.com/RobinTail/express-zod-api/releases/tag/v24.0.0)

**原文标题**: [Release v24.0.0 · RobinTail/express-zod-api · GitHub](https://github.com/RobinTail/express-zod-api/releases/tag/v24.0.0)

express-zod-api 发布了 v24.0.0 版本，主要针对 Zod 4 的支持进行了多项更新和破坏性变更。

- 🚀 **Zod 4 支持**：最低要求 zod 版本为 3.25.35，但必须从 `zod/v4` 导入。  
- 🔄 **破坏性变更**：  
  - `IOSchema` 类型简化为仅支持解析为对象的模式。  
  - `ZodType::example()` 方法参数改为输出类型，需在 `transform()` 前调用。  
  - 移除了 `numericRange` 选项和 `optionalPropStyle` 选项。  
- 📚 **文档生成改进**：使用 Zod 4 的 `toJSONSchema()` 方法，并适配 OpenAPI 3.1。  
- ✨ **新增功能**：  
  - 添加了 `ez.buffer()` 专有模式。  
  - 移除了 `ez.file()`，建议使用 `z.string()` 或 `ez.buffer()` 替代。  
- ⚠️ **迁移提示**：可通过 ESLint 自动迁移工具调整代码，如更新导入路径和示例设置方式。  
- 🔧 **其他调整**：  
  - `Depicter` 类型签名变更，改为后处理函数。  
  - 响应中的未知类型从 `any` 改为 `unknown`。  
  - 移除了 `getExamples()` 辅助函数，推荐使用 `.meta()?.examples`。

---

### [Zod 4 发布 | Zod](https://zod.dev/v4)

**原文标题**: [Introducing Zod 4 | Zod](https://zod.dev/v4)

Zod 4 正式发布，带来性能提升、体积优化和新功能。

- 🚀 **性能提升**：Zod 4 解析速度显著提升，字符串解析快 14 倍，数组解析快 7 倍，对象解析快 6.5 倍。
- 📉 **体积优化**：核心包体积减少 2 倍，Zod Mini 版本体积更小，适合严格限制包大小的项目。
- 🔄 **版本迁移**：Zod 4 初始与 Zod 3 并行发布，通过 `zod/v4` 子路径导入，未来将全面过渡到 `zod@4.0.0`。
- 📚 **新功能**：
  - 元数据系统：支持强类型元数据，与 JSON Schema 兼容。
  - 递归对象：改进递归类型推断，无需类型转换。
  - 文件验证：新增 `z.file()` 支持文件验证。
  - 国际化：支持多语言错误消息。
  - 错误美化：新增 `z.prettifyError` 美化错误输出。
  - 模板字面量：新增 `z.templateLiteral()` 支持模板字面量类型。
  - 数字格式：新增多种数字和 BigInt 格式支持。
  - 字符串布尔值：新增 `z.stringbool()` 支持更灵活的布尔值解析。
- 🛠 **API 改进**：
  - 错误自定义简化，统一使用 `error` 参数。
  - 判别联合支持更多模式类型和组合。
  - 字面量支持多值。
  - 精炼内置在模式中，支持与其他方法链式调用。
  - 新增 `.overwrite()` 方法，不改变推断类型的情况下转换值。
- 🏗 **可扩展基础**：新增 `zod/v4/core` 作为共享基础包，支持构建其他模式库。

---

### [Bun v1.2.15 | Bun 博客](https://bun.sh/blog/bun-v1.2.15)

**原文标题**: [Bun v1.2.15 | Bun Blog](https://bun.sh/blog/bun-v1.2.15)

本次发布修复了 11 个问题（261 个👍），包含多项功能更新与改进。

- 🛠️ **bun audit**：扫描依赖项的安全漏洞，类似 npm audit 但专为 Bun 设计。  
- 📦 **bun pm view**：查看 npm 包的元数据（如版本、依赖等），支持属性过滤和 JSON 输出。  
- 🚀 **bun init**：新增 Cursor 规则，引导使用 Bun 替代 Node.js/Vite/npm/pnpm。  
- ⚙️ **Node.js 兼容性**：  
  - 实现`node:vm`的`SourceTextModule`（支持 ES 模块沙盒化运行）。  
  - 新增`node:perf_hooks`的`createHistogram`（统计分布追踪）。  
  - 支持`node:worker_threads`的`Worker.getHeapSnapshot`（堆内存快照）。  
- 📥 **安装方式**：支持`curl`、`npm`、`PowerShell`、`scoop`、`brew`和`docker`一键安装。  
- 🔄 **升级依赖**：  
  - `bun update`更新至兼容版本，`--latest`包含破坏性变更。  
- 🌐 **前端开发**：Chrome DevTools 支持自动工作区文件夹，可直接在浏览器编辑文件。  
- 🔧 **环境变量**：新增`BUN_OPTIONS`，类似`NODE_OPTIONS`，预置命令行参数。  
- 🐞 **Bug 修复**：  
  - 修复 JavaScript 解析器问题（如 JSX 属性、`await using`等）。  
  - 解决运行时稳定性（插件崩溃、`BunRequest.clone()`保留参数等）。  
  - 改进 Node.js 兼容性（DNS 内存泄漏、TLS 加密套件错误等）。  
- ✨ **其他**：JavaScriptCore 引擎升级，修复`await`崩溃等边缘问题。  
- 🙏 **致谢**：感谢 15 位贡献者的代码提交！

---

### [GitHub - shebinleo/pdf2html: pdf2html 是一个使用 Apache Tika 将 PDF 文件转换为 HTML 页面的模块。该模块还支持利用 Apache PDFBox 为 PDF 文件生成缩略图。](https://github.com/shebinleo/pdf2html)

**原文标题**: [GitHub - shebinleo/pdf2html: pdf2html is a module which helps to convert PDF file to HTML pages using Apache Tika. This module also helps to generate thumbnail image for PDF file using Apache PDFBox.](https://github.com/shebinleo/pdf2html)

pdf2html 是一个基于 Apache Tika 和 PDFBox 的 Node.js 模块，用于将 PDF 文件转换为 HTML 页面、提取文本、生成缩略图以及提取元数据。

- 📦 **功能概述**  
  - 支持 PDF 转 HTML、文本提取、分页处理、元数据提取和缩略图生成  
  - 兼容文件路径或内存缓冲区输入  
  - 提供 TypeScript 类型定义和异步 API  

- 🛠️ **核心功能**  
  - 🖥️ PDF 转 HTML（保留格式和结构）  
  - ✂️ 文本内容提取（纯文本输出）  
  - 📄 分页处理（逐页生成 HTML 或文本）  
  - 🏷️ 元数据提取（作者、标题、创建日期等）  
  - 🖼️ 缩略图生成（支持 PNG/JPG 格式和尺寸调整）  

- ⚙️ **技术依赖**  
  - 需 Node.js ≥ 12.0 和 Java Runtime Environment (JRE) ≥ 8  

- 📥 **安装方式**  
  - 通过 npm/yarn/pnpm 安装，自动下载依赖的 Tika 和 PDFBox JAR 文件  

- 🐛 **问题排查**  
  - 常见问题：Java 未安装、文件路径错误、缓冲区不足  
  - 支持手动下载依赖和调试模式（`DEBUG=pdf2html`）  

- 📜 **开源协议**  
  - 采用 Apache-2.0 许可证，欢迎社区贡献  

- 🌟 **项目数据**  
  - GitHub 星标 174，分支 35，被 433 个项目使用

---

### [GitHub - vadimdemedes/ink：🌈 用于交互式命令行应用的 React](https://github.com/vadimdemedes/ink)

**原文标题**: [GitHub - vadimdemedes/ink: 🌈 React for interactive command-line apps](https://github.com/vadimdemedes/ink)

Ink 是一个基于 React 的命令行应用开发工具，允许开发者使用 React 组件构建交互式命令行界面。它支持 Flexbox 布局，并提供了丰富的组件和钩子来简化 CLI 开发。

- 🌈 **React for CLIs** - 使用 React 组件构建命令行应用，支持 Flexbox 布局。
- 📦 **安装简单** - 通过 `npm install ink react` 即可安装。
- 🛠 **组件丰富** - 提供 `<Text>`, `<Box>`, `<Newline>`, `<Spacer>`, `<Static>`, `<Transform>` 等组件。
- 🎮 **钩子支持** - 提供 `useInput`, `useApp`, `useStdin`, `useStdout`, `useStderr`, `useFocus`, `useFocusManager` 等钩子。
- 📊 **布局灵活** - 支持 `width`, `height`, `padding`, `margin`, `flexDirection`, `alignItems`, `justifyContent` 等布局属性。
- 🎨 **样式多样** - 支持文本颜色、背景色、粗体、斜体、下划线、删除线等样式。
- 🔍 **测试友好** - 支持 `ink-testing-library` 进行组件测试。
- 🛠 **开发者工具** - 支持 React Devtools，方便调试。
- 📂 **示例丰富** - 提供计数器、表单、表格、边框、焦点管理等示例。
- 🌍 **社区支持** - 被多个知名项目使用，如 Gatsby, Prisma, Shopify CLI 等。
- 📜 **MIT 许可** - 开源且免费使用。

---

### [GitHub - tsedio/tsed: Ts.ED 是一个基于 Express 的 Node.js 和 TypeScript 框架，用于使用 TypeScript（或 ES6）编写应用程序。它提供了大量装饰器和指南，使您的代码更易读且更少出错。⭐️ 点赞支持我们的工作！](https://github.com/tsedio/tsed)

**原文标题**: [GitHub - tsedio/tsed: Ts.ED is a Node.js and TypeScript framework on top of Express to write your application with TypeScript (or ES6). It provides a lot of decorators and guideline to make your code more readable and less error-prone. ⭐️ Star to support our work!](https://github.com/tsedio/tsed)

Ts.ED 是一个基于 Node.js 和 TypeScript 的框架，构建在 Express 之上，旨在通过装饰器和指南提升代码可读性并减少错误。它支持多平台开发，包括 Express.js、Koa.js、CLI 和 Serverless 架构，并提供丰富的功能和工具来简化开发流程。

- 🚀 **框架概述**：Ts.ED 是一个现代化的 Node.js 框架，支持 TypeScript 和 ES6，提供多种装饰器和开发指南。
- 🌍 **多平台支持**：兼容 Express.js、Koa.js、CLI 和 Serverless（如 AWS），支持 Node.js 和 Bun.js 运行时。
- ⚙️ **快速配置**：内置预配置，简化项目启动流程，支持 CLI 工具快速创建项目。
- 🏗️ **装饰器驱动**：通过装饰器定义控制器、服务、中间件等，简化代码结构。
- 📊 **类为基础**：支持通过类定义控制器、模型、依赖注入等，集成 JSON Schema 和 OpenAPI。
- 🧪 **内置测试支持**：提供测试工具，简化代码测试流程。
- 🔗 **丰富集成**：支持 TypeORM、Mongoose、GraphQL、Socket.io、Swagger-ui 等多种工具。
- 📜 **MIT 许可证**：开源项目，允许自由使用和修改。
- 🌟 **社区支持**：拥有活跃的社区和详细的文档，提供 Slack 和 Twitter 交流渠道。

---

### [GitHub - tinylibs/tinypool: 🧵 极简 Node.js 工作线程池实现（仅 38KB）](https://github.com/tinylibs/tinypool)

**原文标题**: [GitHub - tinylibs/tinypool: 🧵 A minimal and tiny Node.js Worker Thread Pool implementation (38KB)](https://github.com/tinylibs/tinypool)

Tinypool 是一个轻量级的 Node.js 工作线程池实现，体积小巧（38KB），无依赖，专注于提供高效的线程池功能。它是 Piscina 的一个分支，移除了部分非核心功能以减小体积，适用于需要轻量级解决方案的场景。

- 🧵 Tinypool 是一个 Node.js 工作线程池实现，体积仅 38KB，无依赖。
- 🔄 支持 `worker_threads` 和 `child_process` 两种运行时环境。
- 🚀 提供基本的线程池功能，但不支持利用率统计和操作系统特定的线程优先级设置。
- 📦 使用 TypeScript 编写，仅支持 ESM 模块，适用于 Node.js 18.x 及以上版本。
- ⚡ 示例代码展示了如何创建线程池、执行任务以及主线程与工作线程之间的通信。
- 📚 API 与 Piscina 类似，但增加了一些 Tinypool 特有的选项和方法。
- 🔄 支持动态回收工作线程以应对内存泄漏等问题。
- 👥 由 Vitest 团队维护，灵感来源于 Piscina 项目。

---

### [比特。可组合人工智能。](https://bit.cloud/?utm_source=NodeWeekly&utm_id=127&utm_medium=referral%20)

**原文标题**: [Bit. Composable AI.](https://bit.cloud/?utm_source=NodeWeekly&utm_id=127&utm_medium=referral%20)

好的，请提供需要总结的文本内容，我会按照您要求的格式生成概述和带表情符号的要点列表。  

示例格式：  

这里是文章的概述总结  

- 🌟 要点一  
- 📌 要点二  
- 🔍 要点三  

请提供具体内容，我会为您生成相应的总结。

---

### [获取失败](https://nodeweekly.com/link/170008/web)

**原文标题**: [Failed to retrieve](https://nodeweekly.com/link/170008/web)

无法总结：获取内容失败，状态码 429。

---

### [GitHub - tc39/proposal-seeded-random: 关于可生成可重现随机数序列的新 SeededPRNG 类的提案](https://github.com/tc39/proposal-seeded-random)

**原文标题**: [GitHub - tc39/proposal-seeded-random: Proposal for a new SeededPRNG class that yields reproducible sequences of random numbers.](https://github.com/tc39/proposal-seeded-random)

提案概述：该提案旨在为 JavaScript 引入一个新的`SeededPRNG`类，用于生成可重复的随机数序列，适用于需要确定性随机数的场景，如测试、游戏和 CSS 自定义绘制等。

- 🌱 **提案目标**：引入`Random.Seeded`类，提供可种子化的伪随机数生成器（PRNG），生成可重复的随机数序列。
- 🔧 **当前问题**：现有的`Math.random()`和`crypto.getRandomValues()`无法生成可重复的随机数序列，用户需自行实现 PRNG。
- 🎨 **使用场景**：CSS 自定义绘制、测试框架、游戏开发等需要确定性随机数的场景。
- 📜 **API 设计**：
  - `Random.Seeded`类：通过种子初始化，提供`.random()`方法生成随机数。
  - 工厂方法：`.fromSeed()`、`.fromState()`、`.fromFixed()`，用于不同初始化方式。
  - 状态管理：`.getState()`和`.setState()`用于序列化和恢复 PRNG 状态。
- 🔢 **随机数生成**：`.random()`方法生成`[0,1)`范围内的浮点数，使用 ChaCha12 算法确保跨平台一致性。
- 🔄 **种子生成**：`.seed()`方法生成随机种子，用于初始化多个 PRNG 实例。
- 📝 **算法选择**：使用 ChaCha12 算法，确保种子范围和随机数序列的稳定性。
- ❓ **FAQ**：解释了为何不通过`Math.random()`参数实现，并提到其他随机数方法提案的补充。
- 📄 **许可证**：MIT 许可证，代码和行为准则公开。

---

### [GitHub - tc39/proposal-is-error: ECMAScript 提案、规范及 Error.isError 的参考实现](https://github.com/tc39/proposal-is-error)

**原文标题**: [GitHub - tc39/proposal-is-error: ECMAScript Proposal, specs, and reference implementation for Error.isError](https://github.com/tc39/proposal-is-error)

该仓库是 ECMAScript 关于 Error.isError 的提案及实现，现已被归档为只读状态。

- 📅 **归档时间**：2025 年 5 月 28 日由所有者归档  
- 🏷 **项目状态**：提案处于 Stage 4（已完成阶段）  
- 📜 **许可协议**：MIT 许可证  
- ⭐ **关注度**：126 个 Star，2 个 Fork  
- 🛠 **核心功能**：提供`Error.isError`方法，用于可靠检测跨域/跨环境的原生 Error 实例  
- 🔍 **使用场景**：  
  - 🐞 调试与错误报告（识别真实原生错误）  
  - 📦 安全序列化（如 RunKit 平台）  
  - 🌐 `structuredClone`等特殊错误处理需求  
- ⚠ **背景问题**：  
  - `instanceof Error`在跨域（iframe/vm 模块）时失效  
  - `Symbol.toStringTag`导致`Object#toString`可靠性降低  
- 📄 **规范文档**：可通过 HTML 格式查看详细规范  
- 👥 **贡献者**：@ljharb（提案起草者）、@seahindeniz

---

### [不只是感觉，Stack Overflow 开发者调查真的来了 - Stack Overflow](https://stackoverflow.blog/2025/05/29/not-just-a-vibe-the-stack-overflow-developer-survey-is-really-here/)

**原文标题**: [Not just a vibe, the Stack Overflow Developer Survey is really here - Stack Overflow](https://stackoverflow.blog/2025/05/29/not-just-a-vibe-the-stack-overflow-developer-survey-is-really-here/)

Stack Overflow 第 15 届年度开发者调查正式启动，聚焦开发者幸福感、薪资趋势及 AI 工具影响，邀请全球开发者共同参与，揭示行业真实动态。

- 🎉 **15 周年纪念**：Stack Overflow 开发者调查迎来第 15 届，与 YouTube、Wikipedia 等长寿网络社区并肩，探讨 AI 时代开发者社群的演变。  
- 😔 **开发者幸福感**：80% 开发者对工作不满或麻木，混合/远程办公者满意度仅 7/10（8-10 为幸福区间），高薪资（前 25%）显著提升后端/全栈等岗位满意度。  
- 💰 **薪资波动明显**：2024 年多国开发者薪资下降 7%，英国工程经理（+21%）与乌克兰全栈（-44%）差异悬殊，德国薪资几乎无变化（0.3%）。  
- 🤖 **AI 工具渗透与争议**：76% 开发者计划或正使用 AI 工具（2023 年 70%），但信任度分化——印度开发者最信任（59%），德国最不信任（42%），资深开发者更认可其提升效率（84%）。  
- 🔍 **2025 年新焦点**：调查新增 AI 代理工作流、职业转型动机、社群生态变化等问题，探索技术趋势对开发者职业与学习方式的影响。  
- 🌍 **立即参与**：点击链接填写问卷，贡献真实数据，帮助全球开发者社群洞察行业现状。  

（注：关键数据与趋势已用**加粗**标出，emoji 强化核心主题）

---

### [JavaScript 即将推出的 Temporal API 及其解决的问题 | WaspDev](https://waspdev.com/articles/2025-05-24/temporal-api)

**原文标题**: [JavaScript's upcoming Temporal API and what problems it will solve | WaspDev](https://waspdev.com/articles/2025-05-24/temporal-api)

JavaScript 即将推出的 Temporal API 将解决现有 Date 对象的诸多问题，提供更强大、更灵活的日期和时间处理功能。

- 🕰️ JavaScript 的 Date 对象设计存在诸多问题，源于 1995 年匆忙借鉴 Java 的 java.util.Date 类，导致长期存在缺陷。
- 🌍 Date 对象的主要问题包括有限的时区支持、夏令时处理困难、可变性导致的副作用、不一致的解析行为以及 API 设计上的怪异之处（如月份从 0 开始）。
- 🛠️ Temporal API 旨在彻底解决这些问题，提供不可变的对象、一流的时区支持、一致的解析和更精确的时间处理。
- 📅 Temporal API 引入了多种新类型，如 Temporal.PlainDate（仅日期）、Temporal.PlainTime（仅时间）、Temporal.ZonedDateTime（带时区的日期时间）等，以满足不同场景需求。
- ⏱️ Temporal.Duration 用于表示时间间隔，支持复杂的时间算术运算。
- 📆 支持多种日历系统（如伊斯兰历、希伯来历等），满足国际化需求。
- 🚧 截至 2025 年，Temporal API 仅在 Firefox 139+ 中实验性支持，生产环境需使用 polyfill。
- 🎯 Temporal API 的推出将显著提升 JavaScript 日期时间处理的可靠性和易用性，减少开发中的常见错误。

---

### [高效单代码库的构成要素](https://blog.swgillespie.me/posts/monorepo-ingredients/)

**原文标题**: [The Ingredients of a Productive Monorepo](https://blog.swgillespie.me/posts/monorepo-ingredients/)

概述：本文探讨了构建高效 Monorepo 所需的关键要素，包括源控制、构建系统、测试、持续集成和持续交付的挑战与解决方案，并强调 Monorepo 虽能提升一致性，但也需权衡技术投入与组织需求。

- 🏗️ **Monorepo 动机**：追求一致性、组织协同和共享工具，而非盲目模仿大公司。  
- ⚠️ **现实挑战**：Monorepo 会引入新问题，需接受短期倒退才能长期获益。  
- 📜 **黄金法则**：所有操作必须为 O(change) 而非 O(repo)，确保性能随规模可控。  
- 🔧 **源控制选择**：Git 在大型 Monorepo 中性能受限，可考虑稀疏检出或虚拟文件系统（如 Google/Meta 方案）。  
- 🛠️ **构建系统**：优先使用单语言生态工具（如 Cargo/Go），避免过早采用 Bazel；需支持高效增量构建。  
- 🧪 **测试优化**：仅运行受影响测试、自动重试失败用例，降低海量测试的 flakes 影响。  
- 🔄 **持续集成**：需结合目标判定器动态触发任务，权衡吞吐量、正确性和延迟（如合并队列策略）。  
- 🚀 **持续交付**：代码原子性≠部署原子性，需验证服务合约避免破坏性变更。  
- 💡 **结论**：Monorepo 能强化工程文化，但需长期投入工具链迭代以适应增长。  

（注：Emoji 根据上下文匹配关键点，如🏗️代表基础动机，⚠️表警示，📜表核心原则等）

---

