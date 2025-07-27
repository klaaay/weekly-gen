### [Node 周刊第 587 期：2025 年 7 月 22 日](https://nodeweekly.com/issues/587)

**原文标题**: [Node Weekly Issue 587: July 22, 2025](https://nodeweekly.com/issues/587)

概述总结  
本期内容涵盖了 Node.js 生态系统的最新动态，包括安全更新、工具发布、技术整合以及开发者资源。重点介绍了 PHP 与 Node.js 的融合、Node.js 安全补丁、npm 包管理工具更新、以及多个开源项目的进展。此外，还包含了一些实用的开发技巧和安全提醒。  

- 🔒 **Node.js 安全更新** — 发布了 Node.js v24.4.1、v22.17.1 和 v20.19.4，修复了 Windows 路径遍历和 V8 哈希相关的安全漏洞。  
- 🌉 **PHP 与 Node.js 融合** — 通过 php-node 和 Watt 运行时，现在可以在 Node.js 应用中嵌入 PHP 并运行 Laravel 应用。  
- 🛠 **npm 包管理工具更新** — Bun v1.2.19 支持 pnpm 风格的 node_modules，pnpm 未来版本将支持锁定 Node.js 版本。  
- 📦 **创建 npm 包的最佳实践** — Matt Pocock 分享了 2025 年创建 npm 包的完整流程，并弃用了 CommonJS。  
- 🚀 **新工具发布** — Endor 允许通过 npm 安装和运行 Postgres 等服务，NAPI-RS v3 支持 Rust 构建 Node 插件并新增 WebAssembly 目标。  
- 📜 **静态站点生成器** — Eleventy 迁移案例显示性能提升 24%，适合静态站点开发。  
- ⚠️ **安全提醒** — eslint-config-prettier 包被入侵事件分析，提醒开发者警惕针对 npm 包开发者的钓鱼攻击。  
- 📹 **开发者资源** — Deno 团队发布 JavaScript 历史视频，Andy Wingo 总结了 WebAssembly 的现状。  
- 🔧 **工具更新** — 包括 Multer、Undici、Jasmine 等多个 Node.js 工具的最新版本发布。

---

### [Laravel 与 Node.js：Watt 运行环境中的 PHP](https://blog.platformatic.dev/laravel-nodejs-php-in-watt-runtime)

**原文标题**: [Laravel and Node.js: PHP in Watt Runtime](https://blog.platformatic.dev/laravel-nodejs-php-in-watt-runtime)

Laravel 应用现可通过 Platformatic PHP 堆栈在 Node.js 的 Watt 运行时中运行，实现 PHP 与 JavaScript 生态的无缝集成。

- 🚀 **核心优势**：Laravel 可直接在 Node.js 进程中运行，减少传统 PHP 与 Node.js 分离部署的复杂性。  
- 🔧 **技术原理**：通过 Rust 编写的 `@platformatic/php-node` 原生模块，在 Node.js 内嵌入多线程 PHP 运行时。  
- ⚡ **性能提升**：Laravel 作为堆栈模块运行，直接访问其他服务，显著降低延迟。  
- 📦 **快速入门**：  
  - 创建项目目录并初始化 `package.json`。  
  - 配置工作区，添加 Laravel 应用到 `web/laravel`。  
  - 通过 `platformatic.json` 设置文档根目录和 URL 重写规则。  
  - 安装依赖后使用 `npm run dev` 启动开发环境。  
- 🛠️ **配置详解**：  
  - `docroot` 指定 Laravel 的 `public` 目录。  
  - `rewriter` 确保所有请求通过 `index.php` 路由。  
  - 支持热重载和自定义 PHP 扩展。  
- 🌟 **未来潜力**：  
  - 统一部署 PHP 与 Node.js 服务。  
  - 资源复用，逐步迁移 PHP 至 JavaScript。  
- 📚 **资源推荐**：参考 GitHub 示例和官方文档，社区欢迎贡献。

---

### [无缝融合 PHP 与 Node.js](https://blog.platformatic.dev/seamlessly-blend-php-with-nodejs)

**原文标题**: [Seamlessly Blend PHP with Node.js](https://blog.platformatic.dev/seamlessly-blend-php-with-nodejs)

概述：  
文章介绍了@platformatic/php-node 模块，这是一个革命性的 Node.js 模块，旨在无缝集成 PHP 和 Node.js，使开发者能够在 Node.js 应用中直接嵌入 PHP 代码，从而结合两种语言的优势。文章详细说明了该模块的工作原理、关键特性、使用案例以及如何快速上手，并展示了如何在 Watt 和 Next.js 中运行 WordPress 的示例。

- 🚀 **模块介绍**：@platformatic/php-node 是一个基于 Rust 的 Node.js 模块，允许在 Node.js 环境中直接运行 PHP 代码，充分利用 PHP 的生态系统和 Node.js 的性能。  
- 🔧 **工作原理**：通过 Node.js 的 worker 池多线程处理 PHP 请求，使用 Rust 和 napi.rs 作为桥梁，实现高效的语言间通信。  
- ⚡ **关键特性**：无缝集成、多线程处理、性能提升、统一的开发环境。  
- 🏗️ **使用案例**：迁移遗留 PHP 应用到 Node.js、构建混合应用、创建高性能 Web 服务。  
- 📦 **快速上手**：通过 npm 安装@platformatic/php-node，详细文档见 GitHub 仓库。  
- 🛠️ **示例演示**：展示了如何在 Watt 中运行 PHP，并进一步演示了如何在 Node.js 中运行 WordPress。  
- 🔗 **混合开发**：结合 Next.js 和 WordPress，实现内容管理和前端展示的分离，提升性能和灵活性。  
- 📺 **更多资源**：提供了 GitHub 示例和 YouTube 视频教程链接，方便开发者进一步探索。  
- 📩 **支持与反馈**：鼓励开发者尝试并提出问题，联系方式为 hello@platformatic.dev。

---

### [wattpm - npm](https://www.npmjs.com/package/wattpm)

**原文标题**: [wattpm - npm](https://www.npmjs.com/package/wattpm)

Watt 是 Platformatic 的 Node.js 应用服务器，支持集中管理多个 Node.js 应用（服务），提供虚拟网格网络、快速日志记录、监控及多种流行技术栈集成。

- 🚀 **核心功能**：Watt 是 Node.js 应用服务器，支持多服务集中管理，提供虚拟网格网络、Pino 日志、Prometheus 监控和 OpenTelemetry 集成。  
- ⚡ **技术栈支持**：兼容 Next.js、Astro、Express 和 Fastify 等流行框架。  
- 📥 **安装方式**：可通过`npx wattpm@latest init`快速初始化或手动`npm install wattpm`安装。  
- 📚 **文档资源**：提供快速入门指南、参考文档和详细教程，详见[platformatic.dev](https://platformatic.dev)。  
- 🐞 **支持与反馈**：遇到问题可通过 GitHub 提交 issue 或加入 Discord 频道反馈。  
- 📜 **许可证**：采用 Apache 2.0 开源协议。  
- 📦 **包信息**：最新版本 2.72.0，周下载量 758,271，未打包大小 141kB。  
- 🔗 **资源链接**：代码仓库位于[GitHub](https://github.com/platformatic/platformatic)，主页提供快速入门指南。

---

### [Laravel - 为 Web 工匠打造的 PHP 框架](https://laravel.com/)

**原文标题**: [Laravel - The PHP Framework For Web Artisans](https://laravel.com/)

Laravel 是一个功能强大的 PHP 框架，提供完整的开发生态系统，包括框架、工具包、部署方案和监控服务，旨在提升开发者的生产力和应用性能。

- 🏗️ **核心框架**：Laravel 提供优雅的语法和丰富的功能，支持认证、授权、数据库操作（Eloquent）、文件存储等常见需求。
- 🧩 **扩展包**：包含 Scout（搜索）、Octane（高性能服务器）、Cashier（支付）等官方扩展包，覆盖多种开发场景。
- 🚀 **开发工具**：提供本地开发工具 Sail（Docker）、测试框架 Pest、调试工具 Telescope 等，优化开发体验。
- 🌐 **前端支持**：支持 Inertia（与 React/Vue 集成）、Livewire（动态 Blade 组件），适合不同技术栈。
- ☁️ **部署方案**：  
  - **Cloud**：全托管平台，按需付费。  
  - **Forge**：支持自托管 VPS（DigitalOcean、AWS 等），起价 $12/月。  
- 📊 **监控与测试**：  
  - **Nightwatch**：应用性能监控。  
  - **Pulse**：实时性能分析。  
- 📅 **社区与活动**：举办 Laracon 全球会议（如 2025 年美国丹佛、澳大利亚布里斯班场次）。
- 💬 **用户评价**：被开发者、企业广泛认可，誉为高效、灵活且社区活跃的框架。  
- 🛠️ **快速开始**：通过 Composer 安装 Laravel，一键生成新项目，文档齐全。

---

### [Node.js — 2025 年 7 月 15 日星期二安全发布](https://nodejs.org/en/blog/vulnerability/july-2025-security-releases)

**原文标题**: [Node.js — Tuesday, July 15, 2025 Security Releases](https://nodejs.org/en/blog/vulnerability/july-2025-security-releases)

Node.js 项目于 2025 年 7 月 15 日发布安全更新，修复了多个高严重性漏洞，影响 24.x、22.x 和 20.x 版本。

- 🚨 **Windows 设备名称路径遍历漏洞 (CVE-2025-27210)**  
  - 影响所有活跃版本（20.x、22.x、24.x），特别是 Windows 用户使用 `path.join` API 的情况。  
  - 感谢报告者 oblivionsage 和修复者 RafaelGSS。

- ⚠️ **V8 引擎 HashDoS 漏洞 (CVE-2025-27209)**  
  - 仅影响 24.x 版本，攻击者可通过控制字符串生成哈希碰撞。  
  - 感谢报告者 sharp_edged 和修复者 targos。

- 📥 **更新版本发布**  
  - 修复版本：Node.js v20.19.4、v22.17.1、v24.4.1。  
  - 建议用户尽快升级以确保系统安全。

- 📅 **发布时间**  
  - 安全更新于 2025 年 7 月 15 日或之后发布。

- 🔗 **更多信息**  
  - 安全政策及漏洞报告流程详见 Node.js 官网和 GitHub 文档。  
  - 订阅 nodejs-sec 邮件列表获取安全公告。

---

### [Node.js — Node.js v24.4.1（当前版本）](https://nodejs.org/en/blog/release/v24.4.1/)

**原文标题**: [Node.js — Node.js v24.4.1 (Current)](https://nodejs.org/en/blog/release/v24.4.1/)

Node.js v24.4.1（当前版本）发布，主要包含安全修复和更新。

- 🔒 **安全版本**：Node.js v24.4.1 是一个安全版本，修复了两个重要的安全问题。  
- 🚨 **CVE-2025-27209**：修复了 V8 引擎中新的 RapidHash 算法可能导致的 HashDoS 攻击。  
- 🛡️ **CVE-2025-27210**：修复了 Windows 设备名称（如 CON、PRN、AUX）绕过路径遍历保护的问题。  
- 🔧 **提交记录**：  
  - 回滚了 V8 引擎中的 RapidHash 相关提交（[c33223f1a5](https://github.com/nodejs-private/node-private/pull/713)）。  
  - 处理了所有 Windows 保留驱动名称的问题（[56f9db2aaa](https://github.com/nodejs-private/node-private/pull/721)）。  
- 📥 **下载链接**：提供了多个平台的安装包和二进制文件，包括 Windows、macOS、Linux、AIX 等。  
- 📜 **文档**：更新了 API 文档，可通过 [Node.js 官方文档](https://nodejs.org/docs/v24.4.1/api/) 查看。  
- 🔏 **SHASUMS**：提供了文件的哈希值和 PGP 签名，确保下载的安全性。

---

### [Node.js — Node.js v22.17.1（长期支持版）](https://nodejs.org/en/blog/release/v22.17.1/)

**原文标题**: [Node.js — Node.js v22.17.1 (LTS)](https://nodejs.org/en/blog/release/v22.17.1/)

Node.js v22.17.1 (LTS) 是一个安全版本，主要修复了 Windows 设备名称绕过路径遍历保护的问题，并提供了多种平台的安装包和二进制文件。

- 🔒 安全版本：修复了 CVE-2025-27210，涉及 Windows 设备名称（CON、PRN、AUX）绕过路径遍历保护的问题。
- 🛠️ 提交记录：包括处理 Windows 保留驱动名称的修复和解决 MSVS v17.14 编译问题。
- 💻 多平台支持：提供了 Windows、macOS、Linux、AIX 等多种平台的安装包和二进制文件。
- 📦 下载链接：包括 32 位、64 位和 ARM 架构的安装包和二进制文件。
- 📜 文档：提供了详细的 API 文档和发布文件列表。
- 🔏 安全验证：包含 SHASUMS 和 PGP 签名以确保文件完整性。

---

### [Node.js — Node.js v20.19.4（长期支持版）](https://nodejs.org/en/blog/release/v20.19.4/)

**原文标题**: [Node.js — Node.js v20.19.4 (LTS)](https://nodejs.org/en/blog/release/v20.19.4/)

Node.js v20.19.4 (LTS) 是一个安全版本，主要修复了 Windows 设备名称绕过路径遍历保护的问题，并提供了多个平台的安装包和二进制文件。

- 🔒 安全版本：修复了 Windows 设备名称（如 CON、PRN、AUX）绕过路径遍历保护的问题（CVE-2025-27210）。
- 🛠️ 提交记录：由 RafaelGSS 提交，处理了所有 Windows 保留驱动名称的问题。
- 💾 下载链接：提供了 Windows、macOS、Linux、AIX 等多个平台的安装包和二进制文件。
- 📜 文档：更新了 Node.js v20.19.4 的 API 文档。
- 🔏 PGP 签名：包含了所有文件的 SHASUMS 和 PGP 签名以确保下载安全。

---

### [eslint-config-prettier 遭篡改：下载量达 3000 万的 npm 包如何传播恶意软件——安全可信的开源生态](https://safedep.io/eslint-config-prettier-major-npm-supply-chain-hack/)

**原文标题**: [eslint-config-prettier Compromised: How npm Package with 30 Million Downloads Spread Malware — Safe and Trusted Open Source](https://safedep.io/eslint-config-prettier-major-npm-supply-chain-hack/)

eslint-config-prettier 等热门 npm 包遭供应链攻击，攻击者通过钓鱼手段入侵维护者账号并发布恶意版本，影响数百万开发者。

- 🚨 **攻击概述**：eslint-config-prettier 维护者账号被钓鱼攻击入侵，攻击者发布了 6 个带恶意代码的版本，波及 4 个 npm 包，周下载量达 7800 万次。  
- 📅 **时间线**：  
  - 7 月 18 日：GitHub 用户发现异常版本并提交 issue  
  - 7 月 19 日：维护者确认账号被钓鱼攻击入侵  
  - 7 月 20 日：SafeDep 团队开始调查并分析恶意载荷  
- 💻 **攻击手段**：  
  - 在 package.json 中添加 install 脚本执行 install.js  
  - 通过 install.js 加载恶意 PE32+ 文件 node-gyp.dll（仅影响 Windows 系统）  
  - 植入 Scavenger 恶意软件窃取文件、凭证等  
- 🛡️ **防护措施**：  
  - SafeDep 工具（vet/pmg）可自动检测恶意包并阻断安装  
  - 提供 CI/CD、AI 编码助手等多场景防护  
- 🔍 **技术分析**：  
  - node-gyp.dll 通过 CreateThread 执行混淆代码  
  - 详细逆向分析见 InvokRE 博客  
- 📌 **影响范围**：  
  - 涉及 eslint-config-prettier（3100 万周下载）等 4 个包  
  - 被入侵账号可访问总周下载量 1.8 亿的包  
- ⚠️ **结论**：事件暴露开源生态脆弱性，建议开发者采用安全工具防护供应链攻击

---

### [http,https: 在 http/https.request 和 Agent 中添加内置代理支持 by joyeecheung · Pull Request #58980 · nodejs/node · GitHub](https://github.com/nodejs/node/pull/58980)

**原文标题**: [http,https: add built-in proxy support in http/https.request and Agent by joyeecheung · Pull Request #58980 · nodejs/node · GitHub](https://github.com/nodejs/node/pull/58980)

Node.js 在 HTTP/HTTPS 模块中新增了内置代理支持，允许通过环境变量配置代理服务器。

- 🌐 新增 `NODE_USE_ENV_PROXY` 环境变量，启用后会自动解析 `HTTP_PROXY`/`HTTPS_PROXY`/`NO_PROXY` 配置
- 🔧 `http.Agent` 和 `https.Agent` 新增 `proxyEnv` 选项，支持自定义代理配置对象
- ⚙️ 代理支持包括 HTTP 直连和 HTTPS 隧道两种模式
- ⏱️ 隧道建立超时使用请求选项或代理的超时设置
- 🐛 代理错误会返回特定错误码和超时标记
- 📊 测试覆盖率达到 90% 以上，大部分现有 HTTP/HTTPS 用例可透明通过代理
- 📝 文档更新包含新选项和配置示例
- 🔄 向后兼容，不影响现有不使用代理的功能

---

### [Bun v1.2.19 | Bun 博客](https://bun.sh/blog/bun-v1.2.19)

**原文标题**: [Bun v1.2.19 | Bun Blog](https://bun.sh/blog/bun-v1.2.19)

Bun 是一个用于构建和测试全栈 JavaScript 和 TypeScript 应用程序的完整工具包。

- 🚀 **安装方式多样**：支持 curl、npm、powershell、scoop、brew 和 docker 安装。
- 🔄 **升级 Bun**：使用 `bun upgrade` 或 `bun install --linker=isolated` 进行升级。
- 📦 **包管理**：新增 `bun pm pkg` 命令，支持 `get`、`set`、`delete` 和 `fix` 子命令。
- ⚡ **性能优化**：修复了工作区包多次重新评估的问题，提升了安装速度。
- 🔄 **依赖解析优先级**：调整依赖解析优先级为 `devDependencies` > `optionalDependencies` > `dependencies` > `peerDependencies`。
- 🔇 **静默模式**：`bun pm pack` 新增 `--quiet` 标志，减少输出噪音。
- 🔗 **工作区包链接**：`bun install` 和 `bun add` 现在支持从 `.npmrc` 读取 `link-workspace-packages` 和 `save-exact` 设置。
- ❓ **依赖查询**：新增 `bun why <package>` 命令，用于查询依赖链。
- 📂 **顶层配置**：`bun install` 现在支持在 `package.json` 的顶层定义 `catalog` 和 `catalogs`。
- 🧪 **VS Code 测试集成**：Bun 的 VS Code 扩展现在集成了原生 Test Explorer UI。
- 🤖 **AI 代理支持**：`bun test` 输出现在更紧凑，适合 AI 代理使用。
- 🔧 **测试改进**：`test.each` 支持变量替换，`test.coveragePathIgnorePatterns` 支持忽略文件。
- 🐘 **PostgreSQL 客户端优化**：`Bun.sql` 现在支持自动管道查询，性能提升显著。
- ⏱️ **减少首次查询延迟**：新增 `--sql-preconnect` CLI 标志，用于预热数据库连接。
- 🏷️ **Windows 代码签名**：`bun build --compile` 生成的独立可执行文件现在支持 Authenticode 代码签名。
- ⚡ **启动优化**：Bun 现在启动快 1ms，内存使用减少 3MB。
- 🔍 **日志深度配置**：新增 `--console-depth` CLI 标志和 `bunfig.toml` 配置，用于控制 `console.log` 的深度。
- 🚀 **SIMD 加速**：JavaScript 和 TypeScript 解析器现在使用 SIMD 指令加速多行注释解析。
- 🌳 **树摇优化**：Bun 的打包器现在能更好地消除死代码路径中的 `try...catch...finally` 块。
- 🔄 **Node.js 兼容性改进**：支持更多 V8 C++ API，修复了 `os.networkInterfaces()` 和 `process.features.typescript` 等问题。
- 🐛 **Bug 修复**：修复了 `Bun.which()`、`fetch()`、`Bun.inspect` 等多个运行时和打包器问题。
- 🙏 **贡献者**：感谢 18 位贡献者的贡献！

---

### [Bluesky 上的@pnpm.io](https://bsky.app/profile/pnpm.io/post/3lud4fkjfes2j)

**原文标题**: [@pnpm.io on Bluesky](https://bsky.app/profile/pnpm.io/post/3lud4fkjfes2j)

这是一个关于 Bluesky 互动网页应用和 pnpm 工具更新的内容摘要。

- 🌐 这是一个高度互动的网页应用，需要 JavaScript 支持，简单的 HTML 界面无法满足需求。  
- 🔗 了解更多关于 Bluesky 的信息，请访问 bsky.social 和 atproto.com。  
- 📦 pnpm 的下一个版本将支持在 lockfile 中锁定 node.js 版本，类似于项目中的其他依赖。  
- ⏰ 相关信息发布于 2025-07-19T13:55:08.446Z。

---

### [如何创建 NPM 包 | 完全掌握 TypeScript](https://www.totaltypescript.com/how-to-create-an-npm-package)

**原文标题**: [How To Create An NPM Package | Total TypeScript](https://www.totaltypescript.com/how-to-create-an-npm-package)

本指南详细介绍了如何从零开始创建一个生产就绪的 npm 包，涵盖版本控制、代码编写、格式化、测试、CI 流程、版本管理和发布等全流程步骤。

- 🚀 初始化 Git 仓库，设置.gitignore，并推送到 GitHub
- 📦 创建 package.json 文件，配置基本信息、许可证和 README
- 🔧 安装 TypeScript，配置 tsconfig.json，设置构建脚本
- ✨ 集成 Prettier 进行代码格式化，并添加格式检查和格式化脚本
- 🧪 使用 Vitest 进行测试，配置测试和开发脚本
- ⚙️ 设置 GitHub Actions 工作流实现 CI 自动化
- 📌 使用 Changesets 管理版本和发布流程
- 🎉 最终发布包到 npm，包含完整的变更日志和版本管理

---

### [添加服务（如 Postgres）作为 Node 依赖项](https://endor.dev/blog/node-postgres)

**原文标题**: [Add services (like Postgres) as Node dependencies](https://endor.dev/blog/node-postgres)

开发环境设置是软件项目启动或参与现有项目的首要任务之一，涉及安装编程语言运行时、编译器及外部服务（如数据库）。Endor 允许将这些服务（如 Postgres、MariaDB 等）作为 Node 项目的常规 npm 依赖添加，通过 WebAssembly 实现跨平台（包括 Windows）快速启动（5 秒内）和完全隔离。

- 🚀 **Endor 简介**：将 Postgres 等第三方服务作为 npm 依赖集成到 Node 项目中，支持跨平台运行。
- ⚡ **快速启动**：服务启动时间少于 5 秒，完全隔离，基于 WebAssembly 技术。
- 📦 **安装步骤**：添加`@endorhq/cli`和`concurrently`为开发依赖，通过`endor run`命令选择并启动服务（如 Postgres 默认端口 5432）。
- 🔧 **配置示例**：更新`package.json`脚本，使用`concurrently`同时运行应用和数据库服务。
- 🛠️ **连接数据库**：示例代码展示如何通过`pg`库连接 Endor 启动的 Postgres（用户`root`，无密码）。
- 🌟 **开发者体验**：简化环境搭建，提升团队效率，支持所有操作系统（包括 Windows），无需复杂配置。
- 🔍 **示例资源**：完整示例可参考`@endorhq/node-demo`仓库。
- 💡 **核心优势**：通过熟悉生态（npm）快速启动服务，实现“下载 - 运行 - 开发”的无缝体验。

---

### [我们将网站迁移至 Eleventy，性能提升 24% | Etch 软件工作室](https://etch.co/blog/we-migrated-our-site-to-eleventy-and-increased-performance-by-24-percent)

**原文标题**: [We migrated our site to Eleventy and increased performance by 24% | Etch Software Studio](https://etch.co/blog/we-migrated-our-site-to-eleventy-and-increased-performance-by-24-percent)

将网站从 Next.js 迁移至 Eleventy 后，性能提升 24%，依赖项大幅减少，构建更稳定高效。

- 🚀 性能提升：Lighthouse 评分从 76 升至 97，主页 JavaScript 体积从 2161KB 降至 11.3KB  
- 📦 依赖简化：NPM 依赖从 1115 个减至 13 个，代码行数减少 37%  
- 🛠️ 工具选择：Eleventy 提供最小化工具集，专注 HTML/CSS/JS 静态生成  
- 🌐 浏览器优先：构建时完成所有处理，运行时零额外开销  
- ⏱️ 版本稳定：2018 年以来仅 3 次重大更新，维护成本低  
- 🧩 模板挑战：采用 WebC 语言替代 JSX，需适应新语法但更贴近原生 HTML  
- 🎨 样式打包：内置 Lightning CSS 实现自动压缩和浏览器兼容处理  
- 💡 交互方案：通过 Web Components 渐进增强静态内容  
- 🔧 服务定制：手动配置 Workbox 替代 next-pwa，精准控制缓存策略  
- 🔄 迁移启示：针对静态内容场景，轻量级方案比全功能框架更高效

---

### [Eleventy 是一个更简单的静态网站生成器](https://www.11ty.dev/)

**原文标题**: [Eleventy is a simpler static site generator](https://www.11ty.dev/)

Eleventy 是一个简单高效的静态网站生成器，支持多种模板语言，无需客户端 JavaScript，适合长期项目维护。

- 🚀 **快速构建** - Eleventy 构建速度极快，处理 4000 个 Markdown 文件仅需 1.93 秒，远超其他工具。
- 🛠️ **多模板支持** - 支持 HTML、Markdown、WebC、JavaScript 等多种模板语言，灵活组合使用。
- 🌍 **社区与信任** - 被 NASA、Google、Microsoft 等知名机构使用，GitHub 上有 82,000+ 仓库采用。
- 📦 **零配置启动** - 开箱即用，无需复杂配置，也支持深度自定义。
- 🔒 **无追踪** - 不收集用户数据，无需担心隐私问题。
- ⚡ **增量迁移** - 可逐步将现有项目迁移到 Eleventy，无需一次性重写。
- 📚 **丰富文档** - 提供详细的入门指南、教程和社区资源，帮助快速上手。
- 💬 **用户好评** - 受到 Addy Osmani、Lea Verou 等开发者的高度评价。
- 🔄 **生产就绪** - 稳定可靠，自 2017 年以来已发布 212 个版本，仅 3 个版本需开发者调整。

---

### [吕的主页](https://lui.ie/guides/semantic-search-fonts)

**原文标题**: [Lui's Homepage](https://lui.ie/guides/semantic-search-fonts)

好的，请提供需要总结的文本内容，我会按照您要求的格式生成概述和带表情符号的要点列表。  

示例格式：  

概述内容  

- 🌟 要点一  
- 📌 要点二  
- 🔍 要点三  

请提供具体文本，我会为您生成相应的总结。

---

### [200 行代码实现全功能代理——方法揭秘](https://cthiriet.com/blog/nano-claude-code)

**原文标题**: [A Full Code Agent in 200 Lines—Here’s How](https://cthiriet.com/blog/nano-claude-code)

概述：本文介绍了如何用 200 行代码构建一个名为 nano-claude-code 的简化版代码代理工具，类似于 Claude Code 或 OpenAI Codex CLI。作者详细展示了如何通过调用 Claude API、定义工具（如读写文件和执行 bash 命令）、构建循环逻辑以及优化提示工程来实现这一目标。

- 🚀 用 200 行代码构建简化版代码代理工具 nano-claude-code，功能类似 Claude Code 或 OpenAI Codex CLI  
- 🔧 第一步：使用 Bun 初始化 JavaScript 项目，调用 Claude API 并处理文件读取工具  
- 📂 定义工具：包括 read_file（读取文件）、write_file（写入文件）和 execute_bash（执行 bash 命令）  
- 🔄 核心逻辑：通过 while 循环实现代理的持续运行，根据停止原因决定是否继续使用工具或等待用户输入  
- 📝 提示工程：通过精心设计的 prompt.md 文件指导代理行为，特别是 execute_bash 工具的使用  
- 🏎️ 代理三要素：强大的 LLM 模型（车）、健壮的代码逻辑（路）和清晰的提示（交通标志）  
- 🎯 实际应用：演示了如何使用该代理从头开始构建一个小型市场项目

---

### [GitHub - lirantal/npq：通过预安装审计安全安装npm包](https://github.com/lirantal/npq)

**原文标题**: [GitHub - lirantal/npq: safely install npm packages by auditing them pre-install stage](https://github.com/lirantal/npq)

npq 是一个用于在安装 npm 包之前进行安全检查的工具，通过多种检查机制确保包的安全性。

- 🔍 **功能概述**：npq 在安装前对 npm 包进行安全检查，包括查询漏洞数据库、检查包年龄、下载量等。
- 🛡️ **安全检查项**：包括 Snyk 漏洞数据库、包年龄、下载量、README、LICENSE、安装脚本等。
- ⚠️ **免责声明**：npq 不能保证绝对安全，仍需谨慎。
- 📹 **演示**：提供演示视频展示功能。
- 📥 **安装**：通过 `npm install -g npq` 安装，推荐使用 npm 而非 yarn。
- 🔧 **使用方式**：通过 `npq install <package>` 安装包，支持嵌入日常 npm 使用。
- 🔄 **支持包管理器**：可通过环境变量指定 yarn、pnpm 等其他包管理器。
- 📊 **检查项（Marshalls）**：包括包年龄、作者、下载量、README、仓库 URL、安装脚本、漏洞等。
- 🚫 **禁用检查项**：可通过环境变量禁用特定检查项。
- 🧪 **干运行**：支持 `--dry-run` 参数检查包而不安装。
- 📜 **纯文本输出**：支持 `--plain` 参数强制纯文本输出。
- ❓ **FAQ**：解答常见问题，如与 npm audit 的区别、是否需要 Snyk API 密钥等。
- 👥 **贡献**：欢迎贡献，请参考 CONTRIBUTING 指南。
- 📚 **资源**：提供 README、许可证、行为准则和安全政策。

---

### [NAPI-RS v3 正式发布 – NAPI-RS](https://napi.rs/blog/announce-v3)

**原文标题**: [Announcing NAPI-RS v3 – NAPI-RS](https://napi.rs/blog/announce-v3)

NAPI-RS v3 正式发布，带来 WebAssembly 支持、更安全的 API 设计以及全新的跨平台编译功能。

- 🚀 **WebAssembly 支持**：V3 版本允许将项目编译为 WebAssembly，几乎无需代码更改，支持在浏览器中直接运行 Rust 代码。
- 🛠️ **API 改进**：引入生命周期管理，提升 API 的安全性和可用性，解决了 V2 版本中的一些设计问题。
- 🔄 **跨平台编译**：新增跨平台编译功能，支持多种目标平台，并优化了编译工具链，提升构建效率。
- 📦 **包管理支持**：新增对 pnpm 的支持，优化了包模板，提升了开发体验。
- 🌍 **社区增长**：NAPI-RS 已被广泛应用于多个领域，包括前端构建工具、AI 工具和桌面应用等。
- 💡 **功能增强**：改进了 `ThreadsafeFunction` 和 `Function` API，提升了类型安全性和易用性。
- 🤝 **赞助呼吁**：项目维护需要更多支持，呼吁社区赞助以持续改进和发展。

---

### [GitHub - napi-rs/napi-rs：一个通过Node-API用Rust构建编译型Node.js插件的框架](https://github.com/napi-rs/napi-rs)

**原文标题**: [GitHub - napi-rs/napi-rs: A framework for building compiled Node.js add-ons in Rust via Node-API](https://github.com/napi-rs/napi-rs)

napi-rs 是一个用于通过 Node-API 在 Rust 中构建编译型 Node.js 插件的框架，支持多平台且无需依赖 node-gyp。

- 🚀 **项目简介**: napi-rs 是一个开源框架，允许开发者使用 Rust 编写高性能的 Node.js 插件，并通过 Node-API 与 JavaScript 交互。
- 🌐 **平台支持**: 支持多种操作系统和架构，包括 Windows、macOS、Linux（x64、aarch64、arm 等）、FreeBSD 和 Android。
- ⚙️ **功能特性**: 提供异步支持、类型转换（如 Rust 类型到 Node.js 类型）、回调函数处理等，无需依赖 node-gyp。
- 📦 **工具链**: 提供 CLI 工具（@napi-rs/cli）简化构建流程，支持生成 .node 文件供 Node.js 直接调用。
- 📚 **示例与文档**: 包含丰富的代码示例和详细文档，帮助开发者快速上手。
- 🔧 **开发体验**: 支持 Cargo 构建，集成测试通过 JavaScript 编写，确保兼容性。
- 🏆 **生态相关**: 与 neon、node-bindgen 等项目类似，但强调纯 Rust/JavaScript 工具链的简洁性。
- 📜 **许可证**: 开源项目，代码托管在 GitHub，社区活跃（6.9k stars，318 forks）。

---

### [Node-API | Node.js v24.4.1 文档](https://nodejs.org/api/n-api.html#node-api)

**原文标题**: [Node-API | Node.js v24.4.1 Documentation](https://nodejs.org/api/n-api.html#node-api)

总结失败：Error code: 400 - {'error': {'message': "This model's maximum context length is 65536 tokens. However, you requested 66758 tokens (58758 in the messages, 8000 in the completion). Please reduce the length of the messages or completion.", 'type': 'invalid_request_error', 'param': None, 'code': 'invalid_request_error'}}

---

### [工程师产品 | Substack](https://newsletter.posthog.com?r=5ytvh5)

**原文标题**: [Product for Engineers | Substack](https://newsletter.posthog.com?r=5ytvh5)

概述：  
本文列出了多个面向工程师和开发者的文章标题，涵盖产品开发、市场营销、招聘、团队管理等多个主题，均来自“Product for Engineers”平台。

- 🚀 《40 个关于开发者营销的经验》——涵盖品牌、内容、付费广告、SEO 和 LLMs 等  
- 💼 《产品工程师求职指南》——为有抱负的开发者提供实用建议  
- 📅 《季度规划的错误方法》——避免常见错误  
- 🛠️《50 个成功产品开发经验》——产品构建的核心教训  
- 🔧 《产品管理已失效，工程师可以修复它》——工程师在管理中的角色  
- 🎨 《工程师的氛围设计指南（附提示）》——快速设计方法论  
- ❓ 《工程师面试该问但没问的问题》——如何选择合适初创公司  
- ✨ 《小型工程团队的魔力》——小团队的高效优势  
- 📖 《开发者文档的未言之秘》——打破文档误区  
- 📈 《PostHog 招聘 43 条经验》——12 个月招聘 65 人的实战总结  
- 🚢 《项目推进受阻的原因》——快速交付的警示信号  
- 🤝 《如何避免与联合创始人“分手”》——健康合作关系的维护  

（注：部分标题因原文为英文，翻译可能不完全精准，核心主题已保留。）

---

### [工程师产品 | Substack](https://newsletter.posthog.com?r=5ytvh5%20)

**原文标题**: [Product for Engineers | Substack](https://newsletter.posthog.com?r=5ytvh5%20)

概述：  
该内容为“Product for Engineers”平台的精选文章列表，涵盖工程师在产品开发、市场营销、求职技巧、团队管理等方面的经验分享，由 PostHog 团队及多位作者撰写。

- 🚀 《40 件我们学到的开发者营销经验》——关于品牌、内容、广告、SEO 和 LLM 的实用建议（7 月 21 日，Ian Vanagas）  
- 💼 《产品工程师求职指南》——为有抱负的开发者提供战术性建议（7 月 15 日，Andy Vandervell）  
- ❌ 《季度规划的错误方法》——避免重蹈覆辙（6 月 30 日，Ian Vanagas）  
- 🏆 《50 条成功产品构建经验》——高人气文章（2 月 27 日，Ian Vanagas）  
- 🔧 《工程师如何修复破碎的产品管理》——工程师视角的解决方案（2024 年 12 月 3 日，James Hawkins）  
- 🎨 《工程师的“氛围设计”指南》——快速设计方法论（6 月 16 日，Lior Neu-ner）  
- ❓ 《工程师面试该问却未问的问题》——加入初创公司的技巧（6 月 2 日，James Hawkins & Andy Vandervell）  
- ✨ 《小型工程团队的魔力》——高效协作的奥秘（2024 年 7 月 3 日，James Temperton）  
- 📄 《开发者文档的未言之秘》——打破文档误区（4 月 17 日，Ian Vanagas）  
- 🔍 《PostHog 招聘 43 条心得》——从 3 万份申请中总结的经验（4 月 10 日，Charles Cook）  

其他亮点：  
- 🌱 开源初创公司的隐藏优势（5 月 15 日）  
- 💡 联合创始人关系维护指南（5 月 4 日）  
- 🚢 《项目延迟交付的根源》——团队效率红绿灯（4 月 3 日）  

平台定位：帮助工程师和创始人提升产品能力，内容涵盖技术、设计、管理等多领域。

---

### [GitHub - LuanRT/YouTube.js: YouTube 私有 API（InnerTube）的 JavaScript 客户端](https://github.com/LuanRT/YouTube.js)

**原文标题**: [GitHub - LuanRT/YouTube.js: A JavaScript client for YouTube's private API, known as InnerTube.](https://github.com/LuanRT/YouTube.js)

YouTube.js 是一个基于 JavaScript 的 YouTube 私有 API（InnerTube）客户端，支持 Node.js、Deno 和现代浏览器，提供视频、评论、直播聊天等功能的程序化访问。

- 🚀 **项目简介**: YouTube.js 是一个非官方的 JavaScript 客户端，用于访问 YouTube 的私有 API InnerTube。  
- 📦 **安装方式**: 支持 NPM、Yarn、Git 和 Deno 安装，具体命令详见文档。  
- 💻 **基本用法**: 通过 `Innertube.create()` 初始化，提供详细的指南和 API 文档。  
- 🤝 **贡献指南**: 欢迎提交问题、功能请求或代码贡献，遵循项目指南。  
- ⚠️ **免责声明**: 该项目与 YouTube 无任何关联，所有商标归各自所有者所有。  
- 📜 **许可证**: 采用 MIT 许可证开源。  
- 🌟 **项目数据**: 4.2k 星标，298 个分支，66 位贡献者。  
- 🔧 **技术支持**: 主要使用 TypeScript 开发，占比 98.7%。

---

### [发布 v15.0.0 · LuanRT/YouTube.js · GitHub](https://github.com/LuanRT/YouTube.js/releases/tag/v15.0.0)

**原文标题**: [Release v15.0.0 · LuanRT/YouTube.js · GitHub](https://github.com/LuanRT/YouTube.js/releases/tag/v15.0.0)

GitHub 项目 YouTube.js 的 v15.0.0 版本更新内容，包含重大变更、新功能、错误修复及代码重构。

- 🚨 **重大变更**：放弃对 CommonJS 的支持，部分方法参数格式调整（如`Innertube.getInfo()`需传入对象而非字符串）。  
- ✨ **新功能**：  
  - 新增`CommentsView`的语音回复解析功能。  
  - `DashManifest`添加 DRM 信息支持。  
  - 解析器类新增多个节点类型（如`CompositeVideoPrimaryInfo`、`HypePointsFactoid`等）。  
- 🐛 **错误修复**：修复`Artist.getAllSongs`无法定位目标板块、社区标签 URL 更新等问题。  
- 🔧 **代码重构**：彻底移除 CommonJS 相关代码，优化模块导出逻辑。  
- 📅 **版本发布**：2025 年 7 月 18 日发布 v15.0.0，含 GitHub 签名验证。

---

### [Stripe 到 Postgres 同步引擎独立库](https://supabase.com/blog/stripe-engine-as-sync-library)

**原文标题**: [Stripe-To-Postgres Sync Engine as standalone Library](https://supabase.com/blog/stripe-engine-as-sync-library)

Supabase 宣布将 Stripe-Sync-Engine 作为独立 npm 包发布，支持直接集成到后端项目或 Supabase Edge Functions 中，用于将 Stripe webhook 数据同步到 Postgres 数据库。

- 🚀 **独立 npm 包发布**：Stripe-Sync-Engine 现可作为`@supabase/stripe-sync-engine`安装，支持 Node.js、Express 及 Supabase Edge Functions。  
- 🔄 **数据同步功能**：监听 Stripe webhook 事件（如发票支付失败、客户订阅更新等），并将数据规范化存储到 Postgres。  
- ⚡ **本地化优势**：相比 Stripe API，本地 Postgres 数据提供更低延迟、更好的关联查询能力及支持自定义逻辑（如欺诈检测、计费仪表盘）。  
- 📦 **快速集成**：通过简单配置即可初始化同步引擎，并处理 webhook 事件。  
- 🛠️ **Edge Function 支持**：需预先运行迁移脚本创建表结构，随后可通过 Edge Function 实现自动化数据同步。  
- 🔧 **部署指南**：提供从环境变量配置到 webhook 设置的完整流程，包括秘密管理及函数部署步骤。  
- 🌟 **应用场景**：适用于需要实时分析、高效计费工作流或简化集成的 Stripe+Supabase 项目。  
- 📅 **Launch Week 动态**：该发布作为 Supabase Launch Week 15 的第三天亮点，同期还有分支功能 2.0、边缘函数持久存储等新特性。

---

### [发布 Neutralinojs v6.2.0！· neutralinojs/neutralinojs · GitHub](https://github.com/neutralinojs/neutralinojs/releases/tag/v6.2.0)

**原文标题**: [Release Neutralinojs v6.2.0 released! · neutralinojs/neutralinojs · GitHub](https://github.com/neutralinojs/neutralinojs/releases/tag/v6.2.0)

Neutralinojs v6.2.0 版本发布，新增多项 API 功能与配置选项，并修复了一些问题。

- 🖨️ 新增 `Neutralino.window.print()` API，支持在所有平台调用原生打印对话框，特别是解决了 macOS webview 不支持`window.print()`的问题。  
- 🖱️ 引入 `window.beginDrag()` 函数，用于触发原生窗口拖拽功能，新的可拖拽区域 API 内部使用了此函数。  
- 📁 文件系统 API 新增：  
  - `filesystem.getJoinedPath(...paths: string[])` 合并多个路径字符串。  
  - `filesystem.getNormalizedPath()` 和 `filesystem.getUnnormalizedPath()` 实现 Windows 路径与 Unix 路径的转换（仅 Windows 平台生效）。  
- ⚙️ 新增配置选项 `window.webviewArgs`，支持为 Windows 平台的 WebView2 实例传递额外浏览器参数（如自定义用户代理）。  
- 🐛 改进与修复：  
  - 显示 WebView 初始化失败的 GUI 错误提示（如 Windows 未安装 WebView2 运行时或 Linux 未安装 WebKitGTK 库）。  
  - 更新配置文件选项 `cli.binaryVersion` 至 `6.2.0`，可通过 `neu update` 获取新版本。  
- 📚 快速开始文档链接：[Neutralino.js 官方文档](https://neutralino.js.org/docs)。  
- 🤖 本次发布由自动化工具 **ReleaseZri** 完成。

---

### [发布 v9.4.0 · panva/node-oidc-provider · GitHub](https://github.com/panva/node-oidc-provider/releases/tag/v9.4.0)

**原文标题**: [Release v9.4.0 · panva/node-oidc-provider · GitHub](https://github.com/panva/node-oidc-provider/releases/tag/v9.4.0)

GitHub 仓库 panva/node-oidc-provider 的 v9.4.0 版本更新内容  

- 🚀 新增实验性功能：支持基于证明的客户端认证（Attestation-Based Client Authentication）  
- 🔧 代码重构：统一使用小写请求头名称，并采用 req/res 别名  
- 🌐 更新默认基于客户端的 CORS 辅助工具配置  
- 🔄 协调 DPoP 和证明挑战的实现方式  
- 📚 更新了相关配置选项的文档  

该版本由 panva 于 7 月 17 日发布，包含 5 次提交至 main 分支。

---

### [GitHub - nodejs/corepack：作为Node项目与其包管理器间桥梁的零运行时依赖包](https://github.com/nodejs/corepack)

**原文标题**: [GitHub - nodejs/corepack: Zero-runtime-dependency package acting as bridge between Node projects and their package managers](https://github.com/nodejs/corepack)

Corepack 是一个零运行时依赖的 Node.js 工具，作为 Node.js 项目与包管理器（如 Yarn、npm 和 pnpm）之间的桥梁，帮助开发者更高效地管理项目依赖。

- 🚀 **功能概述**：Corepack 允许开发者无需单独安装 Yarn、pnpm 等包管理器即可在项目中使用它们。
- 📦 **安装方式**：
  - 默认随 Node.js 14.19.0 及以上版本分发（不包括 25.0.0）。
  - 可通过 `corepack enable` 启用，或手动通过 `npm install -g corepack` 安装。
- 🔄 **项目配置**：
  - 在 `package.json` 中通过 `packageManager` 字段指定包管理器及版本（支持 Yarn、npm、pnpm）。
  - 支持哈希校验增强安全性。
- 🌐 **离线支持**：
  - 提供 `corepack pack` 和 `corepack install -g --cache-only` 命令支持离线环境使用。
- ⚙️ **环境变量**：
  - 支持 `COREPACK_HOME` 设置缓存路径、`COREPACK_ENABLE_NETWORK` 控制网络访问等。
- 🔧 **实用命令**：
  - `corepack use` 更新项目包管理器版本。
  - `corepack up` 检查并更新到最新兼容版本。
- ❓ **故障排查**：
  - 设置 `DEBUG=corepack` 查看详细日志。
  - 检查网络连接、代理设置等常见问题。
- 📜 **许可与贡献**：
  - 采用 MIT 许可证，欢迎通过 `CONTRIBUTING.md` 参与贡献。

---

### [GitHub - eslint/markdown: 检查 Markdown 文档中的 JavaScript 代码块](https://github.com/eslint/markdown)

**原文标题**: [GitHub - eslint/markdown: Lint JavaScript code blocks in Markdown documents](https://github.com/eslint/markdown)

ESLint Markdown 语言插件，用于在 Markdown 文档中检查 JavaScript 代码块，支持 JS、JSX、TypeScript 等多种语言。

- 📦 **安装方式**：支持 npm、yarn、pnpm、bun 和 Deno 等多种包管理器安装。
- ⚙️ **配置选项**：提供 `recommended` 和 `processor` 两种配置，支持 CommonMark 和 GitHub Flavored Markdown 格式。
- 📜 **规则列表**：包含多种规则，如要求代码块语言、禁止重复标题、禁止空链接等，部分规则默认启用。
- 🌐 **语言支持**：支持 CommonMark 和 GitHub-Flavored Markdown 两种解析格式。
- 🛠️ **处理器功能**：可从 Markdown 中提取代码块单独检查，支持通过文件名元数据指定文件路径。
- 📝 **编辑器集成**：VSCode 的 vscode-eslint 插件已内置支持 Markdown 处理器。
- 🔧 **贡献指南**：提供克隆仓库、安装依赖和运行测试的详细步骤，遵循 ESLint 贡献准则。
- 💖 **赞助支持**：项目由多家公司和组织赞助，提供技术支持和资源。

---

### [GitHub - expressjs/multer: 用于处理 `multipart/form-data` 的 Node.js 中间件](https://github.com/expressjs/multer)

**原文标题**: [GitHub - expressjs/multer: Node.js middleware for handling `multipart/form-data`.](https://github.com/expressjs/multer)

Multer 是一个 Node.js 中间件，用于处理 `multipart/form-data` 类型的数据，主要用于文件上传。它基于 busboy 构建，以实现最高效率。

- 🚀 **功能概述**：Multer 是处理文件上传的 Node.js 中间件，支持 `multipart/form-data` 格式。  
- 📦 **安装**：通过 `npm install multer` 安装。  
- 📝 **基本用法**：Multer 将文件信息添加到 `req.file` 或 `req.files`，表单字段添加到 `req.body`。  
- ⚠️ **注意事项**：表单必须设置 `enctype="multipart/form-data"`，否则 Multer 不会处理。  
- 🔧 **配置选项**：支持 `dest`（存储路径）、`storage`（存储引擎）、`fileFilter`（文件过滤）等选项。  
- 💾 **存储引擎**：内置 `DiskStorage`（磁盘存储）和 `MemoryStorage`（内存存储），支持自定义引擎。  
- 📏 **限制设置**：可通过 `limits` 设置文件大小、数量等限制，防止 DoS 攻击。  
- ❌ **错误处理**：Multer 错误可通过 `multer.MulterError` 捕获，其他错误由 Express 处理。  
- 🌍 **多语言支持**：README 提供多种语言版本，包括中文、法语等。  
- 📜 **许可证**：采用 MIT 开源协议。

---

### [未找到标题](https://www.cve.org/CVERecord?id=CVE-2025-7338)

**原文标题**: [No title found](https://www.cve.org/CVERecord?id=CVE-2025-7338)

该网页提示用户需要启用 JavaScript 才能正常访问 CVE（常见漏洞与暴露）官方网站。

- 🔒 网页无法正常运行，因为 JavaScript 未启用  
- ⚠️ 用户需启用 JavaScript 以继续使用 CVE 网站功能

---

### [GitHub - jshttp/on-headers: 在响应即将写入头部时执行监听器](https://github.com/jshttp/on-headers)

**原文标题**: [GitHub - jshttp/on-headers: Execute a listener when a response is about to write headers.](https://github.com/jshttp/on-headers)

一个 Node.js 模块，用于在响应头即将写入时执行监听器。

- 🚀 **功能概述**：`on-headers` 模块允许开发者在 HTTP 响应头即将发送到客户端前执行自定义监听器。  
- 📦 **安装方式**：通过 npm 安装，命令为 `npm install on-headers`。  
- 🔧 **API 用法**：调用 `onHeaders(res, listener)`，其中 `listener` 会在响应头写入时触发，且上下文为响应对象。  
- 🔄 **执行顺序**：同一响应对象多次添加监听器时，按添加的逆序触发。  
- 💡 **示例场景**：自动添加未设置的响应头（如 `X-Powered-By`）。  
- 🧪 **测试方法**：运行 `npm test` 进行测试。  
- 📜 **许可证**：采用 MIT 开源协议。  
- 🌟 **项目数据**：160 星、28 分支，被超过 2380 万项目使用。  
- ⚠️ **错误提示**：页面加载失败时需手动刷新。

---

### [GitHub - express-rate-limit/express-rate-limit: Express 网页服务器的基础限速中间件](https://github.com/express-rate-limit/express-rate-limit)

**原文标题**: [GitHub - express-rate-limit/express-rate-limit: Basic rate-limiting middleware for the Express web server](https://github.com/express-rate-limit/express-rate-limit)

express-rate-limit 是一个用于 Express 的中间件，主要用于限制重复请求的频率，适用于公共 API 或密码重置等端点。  

- 🚀 **基本功能**：限制每个 IP 在指定时间窗口内的请求次数（如 15 分钟内 100 次）。  
- ⚙️ **配置灵活**：支持自定义窗口时间、请求限制、响应消息、状态码等。  
- 📊 **数据存储**：内置内存存储，并支持 Redis 等外部存储。  
- 📜 **标准兼容**：支持 `RateLimit` 和 `X-RateLimit-*` 标头（兼容不同草案版本）。  
- 🌐 **IPv6 支持**：可配置 IPv6 子网掩码位数（32-64）。  
- 🔧 **高级选项**：支持异步配置、自定义用户识别、跳过特定请求等。  
- 🛡️ **安全增强**：可限制错误请求或成功请求的计数。  
- 🤝 **社区支持**：由 Zuplo 赞助，文档托管在 Mintlify，欢迎贡献和反馈。  
- 📜 **开源协议**：采用 MIT 许可证，由 Nathan Friedly 和 Vedant K 维护。

---

### [茉莉花/发布说明/5.9.0.md 位于 main · jasmine/jasmine · GitHub](https://github.com/jasmine/jasmine/blob/main/release_notes/5.9.0.md)

**原文标题**: [jasmine/release_notes/5.9.0.md at main · jasmine/jasmine · GitHub](https://github.com/jasmine/jasmine/blob/main/release_notes/5.9.0.md)

概述总结  
Jasmine 是一个公开的 GitHub 仓库，包含代码、问题讨论和项目管理等功能，但目前页面加载时出现错误。  

- 🚀 **仓库状态** - 公开仓库，可 Fork 和 Star，已有 2.2k Fork 和 15.8k Star。  
- ⚠️ **错误提示** - 页面加载时出现错误，需重新加载。  
- 📂 **功能导航** - 提供代码、问题、拉取请求、讨论、Actions、项目、Wiki 和安全等选项。  
- 🔄 **操作建议** - 错误提示建议重新加载页面以解决问题。

---

### [Node-oracledb 6.9 新增支持无会话事务、实例主体认证等多项功能 | 作者：Sharad Chandran | 2025 年 7 月 | Medium](https://medium.com/@sharad-chandran/node-oracledb-6-9-66cd38deadff)

**原文标题**: [Node-oracledb 6.9 packs in support for Sessionless Transactions, Instance Principal Authentication and a lot more | by Sharad Chandran | Jul, 2025 | Medium](https://medium.com/@sharad-chandran/node-oracledb-6-9-66cd38deadff)

node-oracledb 6.9 版本发布，新增支持无会话事务、实例主体认证等多种功能，提升性能、安全性和灵活性。

- 🚀 **无会话事务支持**：新增 API 如`beginSessionlessTransaction`，适用于跨会话的无状态事务管理，提升交互式应用效率。  
- 🔒 **实例主体认证**：支持 OCI IAM 工作流，无需数据库用户凭证，增强云应用安全性。  
- 🛡️ **应用上下文设置**：通过`appContext`参数设置用户特定信息，实现细粒度数据访问控制。  
- 🛠️ **事务保护支持**：新增`connection.ltxid`属性，确保在意外中断时事务的完整性。  
- 📂 **集中配置提供程序扩展**：新增文件、OCI Vault 和 Azure Vault 配置支持，简化连接管理。  
- ⚙️ **其他更新**：最低 Node.js 版本要求提升至 14.17，修复多项问题，增强数据库对象属性访问。  
- 📦 **安装与资源**：可通过 npm 升级，文档和问题反馈渠道详见 GitHub 和 Slack。

---

### [发布 v7.12.0 · nodejs/undici · GitHub](https://github.com/nodejs/undici/releases/tag/v7.12.0)

**原文标题**: [Release v7.12.0 · nodejs/undici · GitHub](https://github.com/nodejs/undici/releases/tag/v7.12.0)

GitHub 上 Node.js 的 undici 项目发布了 v7.12.0 版本，包含多项更新和改进。

- 🚀 发布了 v7.12.0 版本，包含 18 项变更和 4 个新贡献者  
- 🛠️ 移除了测试中的 tspl，减少了中间函数数量  
- 🔧 禁用了共享内置 CI 测试，优化了 WebIDL 参数  
- 📝 为 fetch 函数添加了 JSDoc 注释，统一使用@returns 标签  
- 🐛 修复了拼写错误，澄清了缓存拦截器的类型选项  
- 🔄 允许缓存启发式可缓存的错误状态码  
- 🌐 更新了 undici 与 fetch 的对比文档  
- 🕸️ 改进了 WebSocket 处理，添加了 ping 工具和诊断通道  
- ⚡ 优化了性能，减少了不必要的 Promise 创建  
- 👋 欢迎了新贡献者@pimothyxd、@fredericDelaporte 和@bmeck  
- 📜 完整变更日志可查看 v7.11.0 到 v7.12.0 的差异

---

### [GitHub - vpulim/node-soap: node.js 的 SOAP 客户端与服务器实现](https://github.com/vpulim/node-soap)

**原文标题**: [GitHub - vpulim/node-soap: A SOAP client and server for node.js.](https://github.com/vpulim/node-soap)

node-soap 是一个用于 Node.js 的 SOAP 客户端和服务器模块，支持多种 SOAP 协议和安全功能。

- 🚀 **功能概述**: 提供简单 API，支持 RPC 和 Document 类型的 SOAP 消息，支持同步和异步方法处理。
- 🔒 **安全协议**: 支持 WS-Security、BasicAuth、Bearer Token、SSL 等多种安全协议。
- ⚙️ **客户端功能**: 支持从 WSDL 创建客户端，调用 SOAP 方法，设置请求头，处理 XML 属性等。
- 🛠️ **服务器功能**: 支持创建 SOAP 服务器，处理请求和响应，支持动态生成 SOAP 头。
- 📦 **安装**: 通过 npm 安装，简单易用。
- 📄 **WSDL 处理**: 支持直接实例化 WSDL 进行消息的编组和解组。
- 🔄 **自定义选项**: 支持覆盖命名空间、自定义反序列化、处理忽略的命名空间等。
- 🧪 **测试支持**: 提供 soap-stub 用于单元测试，方便模拟 SOAP 客户端。
- 👥 **贡献者**: 由社区维护，有多个活跃的维护者和贡献者。

---

### [SOAP - 维基百科](https://en.wikipedia.org/wiki/SOAP)

**原文标题**: [SOAP - Wikipedia](https://en.wikipedia.org/wiki/SOAP)

SOAP（简单对象访问协议）是一种用于在计算机网络中交换结构化信息的消息协议规范，主要用于实现 Web 服务。以下是关键点总结：

- 🌐 SOAP 最初代表“简单对象访问协议”，但在 1.2 版本中不再作为缩写。
- 📜 基于 XML 信息集的消息格式，通常通过 HTTP、SMTP 等应用层协议传输。
- 🏗️ 由三部分组成：信封（定义消息结构和处理方式）、编码规则（定义数据类型实例）、过程调用和响应的约定。
- 🔄 具有扩展性、协议中立性和编程模型独立性三大特点。
- 📅 最初于 1998 年 6 月作为 XML-RPC 发布，2003 年 6 月成为 W3C 推荐标准。
- 📦 SOAP 消息结构包括信封（必需）、头部（可选）、主体（必需）和错误（可选）。
- ⚡ 优点：协议中立、易于通过防火墙、国际化支持好；缺点：冗长、解析速度慢、缺乏标准化交互模型。
- 🔧 示例应用：通过 SOAP 请求查询股票价格，服务器返回 XML 格式的响应数据。

---

### [WebAssembly：是的，但用来做什么？ - ACM Queue](https://queue.acm.org/detail.cfm?id=3746171)

**原文标题**: [WebAssembly: Yes, but for What? - ACM Queue](https://queue.acm.org/detail.cfm?id=3746171)

WebAssembly（Wasm）诞生 10 周年，已从技术探索阶段进入实际应用，但发展不均衡。本文分析了 Wasm 的成功与失败案例，总结了其适用场景，并预测了未来 2-3 年的发展方向。

- 🌐 **Web 应用中的 Wasm**：在将桌面应用（如 Adobe Photoshop）移植到网页端时表现成功，但在游戏行业未成主流。部分组件（如 SQLite）成功替代了 Web 平台原有功能。  
- 🛠️ **工具链与语言支持**：C++/Rust 通过 LLVM 工具链编译为 Wasm 占据主流，但 JavaScript/TypeScript 仍是网页开发首选。新推出的 WasmGC 扩展为垃圾回收语言（如 Java、Kotlin）提供了可能。  
- 🔌 **非网页场景应用**：  
  - **插件隔离**：如 Firefox 用 RLBox 隔离不安全 C 库，提升安全性。  
  - **轻量级虚拟化**：如 WALI 将应用编译为 Wasm，降低短任务开销；物联网设备通过 Wasm 实现固件升级。  
  - **组件模型**：定义模块间高级交互标准，被 Shopify 等用于插件系统，并在云原生领域（如边缘计算）探索快速冷启动优势。  
- ☁️ **云计算的潜力**：Wasm 的毫秒级冷启动特性为边缘计算和 FaaS 提供了新可能，但技术尚未成熟。  
- 🔮 **未来方向**：  
  - **安全隔离场景**：如操作系统内核驱动、AI 敏感数据处理。  
  - **替代 eBPF**：扩展内核功能隔离能力。  
  - **Wasm 操作系统**：研究无进程切换的高效架构。  
- ⚠️ **挑战**：技术碎片化、生态兼容性（如字符串处理需底层适配），以及开发者更偏好 Web 原生语言。  

（作者 Andy Wingo 是编译器专家，参与 Firefox/Chrome 的 Wasm 实现，现居日内瓦。）

---

### [JavaScript 不为人知的故事 - YouTube](https://www.youtube.com/watch?v=TYsPrXWgNS8)

**原文标题**: [The untold story of JavaScript - YouTube](https://www.youtube.com/watch?v=TYsPrXWgNS8)

关于 YouTube 的相关信息与链接  
- 📢 关于：平台的基本介绍  
- 🗞️ 新闻：最新动态与公告  
- ©️ 版权：版权政策与保护  
- 📩 联系我们：用户反馈与支持渠道  
- 🎤 创作者：创作者资源与工具  
- 💼 广告：广告合作与投放信息  
- 👩💻 开发者：API 与开发支持  
- 📜 条款：服务条款与协议  
- 🔒 隐私：隐私政策与数据保护  
- ⚖️ 政策与安全：社区准则与安全措施  
- 🔧 YouTube 工作原理：平台运作机制  
- 🧪 测试新功能：体验最新推出的功能  
- © 2025 Google LLC：版权归属声明

---

### [JavaScript 简史 | Deno](https://deno.com/blog/history-of-javascript)

**原文标题**: [A brief history of JavaScript | Deno](https://deno.com/blog/history-of-javascript)

JavaScript 诞生 30 周年，从 10 天开发的脚本语言发展为全球最流行的编程语言，深刻塑造了现代互联网生态。以下是其发展历程的关键节点：

- 🚀 **1994 年 12 月**：Netscape 发布首款图形化浏览器 Netscape Navigator 1.0，为 JavaScript 诞生奠定基础  
- ⏱️ **1995 年 5 月**：Brendan Eich 用 10 天设计出 JavaScript，初衷是为网页添加轻量级交互  
- 🤝 **1995 年 12 月**：Netscape 与 Sun 联合发布 JavaScript，获 28 家科技公司支持  
- ⚔️ **1996 年 3 月**：微软推出 JScript 引发浏览器大战，Netscape 同期发布支持 DOM 的 JavaScript 1.0  
- 📜 **1997 年 6 月**：JavaScript 提交 ECMA 标准化，形成 ECMAScript 规范与 TC39 委员会  
- 🔓 **1998 年 1 月**：Netscape 开源浏览器代码，催生 Mozilla 项目与未来 Firefox  
- 🔌 **1999 年 3 月**：IE5 引入 XMLHttpRequest，为 AJAX 革命埋下伏笔  
- 📚 **1999 年 12 月**：ECMAScript 3 发布，确立 JavaScript 作为严肃编程语言的地位  

- 🌐 **2004 年 4 月**：Gmail 采用 AJAX 技术，开启 Web 2.0 时代  
- 🛠️ **2006 年 3 月**：jQuery 诞生，解决跨浏览器兼容性问题  
- 🚀 **2008 年 9 月**：Chrome 与 V8 引擎发布，大幅提升 JS 执行效率  
- 💻 **2009 年 3 月**：Ryan Dahl 创建 Node.js，使 JS 突破浏览器限制  

- 📦 **2010 年 1 月**：npm 1.0 发布，彻底改变 JS 代码共享方式  
- 🅰️ **2012 年 10 月**：TypeScript 公开，推动大规模 JS 开发  
- ⚛️ **2013 年 5 月**：React 发布，重塑前端开发范式  
- 🔄 **2014 年 9 月**：Babel 问世，解决 JS 版本兼容问题  

- ⚡ **2015 年 6 月**：ES6 发布，带来模块化、Promise 等现代特性  
- 🤖 **2017 年 3 月**：TensorFlow.js 将机器学习引入浏览器  
- 🦕 **2018 年 6 月**：Ryan Dahl 预告 Deno 项目，反思 Node.js 设计  

- 🛰️ **2020 年 5 月**：JavaScript 随 SpaceX 龙飞船进入太空  
- 🐰 **2022 年 6 月**：Bun 运行时挑战 Node.js 性能极限  
- ✊ **2024 年 9 月**：社区发起#FreeJavaScript 运动，要求 Oracle 释放商标权  

JavaScript 已从简单的网页脚本发展为涵盖前端、后端、移动端、AI 的全栈语言，其成功源于开源精神与社区创新。未来将聚焦更快的运行时、智能工具链和开放生态建设。

---

### [Git 快速统计：一种简单高效获取 Git 仓库各类统计信息的方法](https://git-quick-stats.sh/)

**原文标题**: [Git quick statistics is a simple and efficient way to access various statistics in git repository.](https://git-quick-stats.sh/)

概述总结：  
Git-quick-stats 是一个多平台的 Git 仓库统计工具，支持交互式和非交互式使用，提供丰富的统计功能和自定义选项。  

- 🚀 **快速开始**：提供简单的安装方式和多平台支持（Windows、Linux、macOS、Docker）。  
- 📊 **功能丰富**：包括贡献者统计、代码审查推荐、提交日志、分支历史等。  
- 🛠️ **安装便捷**：支持直接通过命令行安装或使用 Docker 镜像。  
- 📅 **自定义统计**：支持按时间范围、路径、合并提交等条件筛选数据。  
- 🎨 **主题切换**：提供默认和经典两种颜色主题可选。  
- 📜 **开源免费**：基于 MIT 许可证，完全开源。  
- 📂 **文档详细**：提供完整的命令行参数说明和使用示例。  
- ⚙️ **高级配置**：支持环境变量设置，如 `_GIT_SINCE`、`_GIT_UNTIL` 等，灵活控制统计范围。  
- 📌 **非交互模式**：支持直接通过命令行参数调用特定功能，适合脚本集成。

---

### [npm 钓鱼邮件通过仿冒域名瞄准开发者...](https://socket.dev/blog/npm-phishing-email-targets-developers-with-typosquatted-domain)

**原文标题**: [npm Phishing Email Targets Developers with Typosquatted Doma...](https://socket.dev/blog/npm-phishing-email-targets-developers-with-typosquatted-domain)

npm 的'is'软件包被劫持，成为持续供应链攻击的一部分，攻击者在多个版本中植入恶意软件。

- 📦 流行的 npm 软件包'is'被劫持，攻击者植入了恶意代码  
- 🚨 这是持续供应链攻击的一部分，影响多个软件包版本  
- ⚠️ 恶意软件可能通过依赖链传播，威胁开发者系统安全  
- 🔍 安全团队正在调查攻击范围，建议用户检查依赖项版本  
- 🛡️ 开发者应立即更新至安全版本或移除受影响依赖

---

