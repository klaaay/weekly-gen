### [Node 周刊第 629 期：2026 年 6 月 18 日](https://nodeweekly.com/issues/629)

**原文标题**: [Node Weekly Issue 629: June 18, 2026](https://nodeweekly.com/issues/629)

本期的 Node Weekly 涵盖了 Node.js 安全更新、新工具发布以及开发实践等多个方面。

- 🔒 **Node.js 26.3.1 等版本发布**：修复了 11 个安全漏洞，其中两个为高危，涉及 TLS 主机名检查和 WebCrypto。
- 🛠️ **Nub：增强 Node 的工具包**：由 Zod 创建者开发，提供更完善的 TypeScript 支持、更快的包安装和更好的.env 处理，而非替代 Node。
- 🧠 **Claude Code 免费课程**：Anthropic 与 Master.dev 合作，提供免费课程教授如何利用 AI 进行编码。
- 🚨 **LinkedIn 招聘骗局**：黑客伪装成招聘人员，在 Node 项目中植入后门，提醒开发者警惕供应链攻击。
- 📦 **npm 将默认禁用安装脚本**：Andrew Nesbitt 探讨了其他工具和生态系统如何处理安装脚本的白名单机制。
- 🌐 **Iroh 1.0 发布**：基于 Rust 的 P2P 加密网络栈，提供官方 Node.js 绑定，可穿透 NAT 和防火墙。
- ⚡ **Babel 8.0 发布**：专注于现代化，仅支持 ESM，默认不再编译为 ES5 和 CommonJS，并附带 TypeScript 类型。
- 🗄️ **纯 TypeScript Postgres 客户端**：Neon 团队展示了如何用 TypeScript 实现 psql CLI，无需二进制依赖。
- 🔧 **Git Worktrees 介绍**：Cassidy Williams 解释了这一古老 Git 功能在 AI 代理时代的新用途。
- 📧 **Nodemailer 9.0 发布**：流行的邮件发送库，v9.0 默认验证 TLS 连接。
- 🧪 **zod-compiler：编译时优化验证器**：将 Zod 模式编译为零开销的验证器，支持 Vite 和 webpack。
- 🤖 **Node Telegram Bot API 1.0/1.1**：重写为 TypeScript，仅支持 ESM，支持 Telegram Bot API 10.1。
- 📏 **eslint-plugin-unicorn 67.0**：包含 200+ 条规则，可显著改善代码质量，如强制使用 Temporal 而非 Date。

---

### [介绍 Nub：Node.js 的全能工具包 — Nub](https://nubjs.com/blog/introducing-nub)

**原文标题**: [Introducing Nub: an all-in-one toolkit for Node.js — Nub](https://nubjs.com/blog/introducing-nub)

## 概述总结
Nub 是一个基于 Rust 构建的 Node.js 一体化工具包，通过在现有 Node.js 上添加功能层而非替代它，提供 TypeScript 直接运行、更快的脚本执行和二进制文件运行等能力。

- 🚀 **核心定位**：Nub 不是替代 Node.js 的新运行时，而是增强现有 Node.js 的工具包，在 Deno 兼容性测试中达到 98.8% 通过率（Deno 77.4%，Bun 40.5%）

- ⚡ **性能优势**：脚本运行比 pnpm run 快 24 倍（14.7ms vs 442.7ms），二进制运行比 npx 快 19 倍（11ms vs 226ms）

- 🎯 **TypeScript 原生支持**：使用 oxc 编译器在内存中转译，支持枚举、命名空间、参数属性等 Node 原生不支持的特性，运行速度比 tsx 快 2.9 倍

- 🔧 **内置工具集**：包含文件运行器、脚本运行器、二进制运行器、文件监听器、包管理器、版本管理器六大功能

- 📦 **包管理**：兼容 pnpm/npm/yarn/bun 的锁文件格式，支持双向读写，默认启用最强安全配置（生命周期脚本默认禁止、新版本 24 小时冷却期）

- 🔄 **零锁定设计**：无 Nub 专用 API、模块命名空间或配置文件，移除 Nub 后代码仍可正常运行

- 🛡️ **安全优先**：默认阻止非注册表依赖、要求发布后 24 小时冷却期、阻止签名降级攻击，支持偏执模式（沙盒构建脚本）

- 🌐 **现代 API 支持**：内置 Worker、Temporal、URLPattern、WebSocket 等 API，自动在旧版 Node 上注入 polyfill

- 🔍 **智能文件监听**：基于实际依赖图而非 glob 模式监听文件变化，自动排除构建产物

- 📁 **工作区感知**：支持 pnpm 的--filter 选择器语法，自动按依赖顺序执行包任务

---

### [免费的 Claude Code 课程！| Frontend Masters](https://frontendmasters.com/courses/claude-code/?utm_source=email&utm_medium=nodeweekly&utm_content=claudecooper)

**原文标题**: [Free Claude Code course! | Frontend Masters](https://frontendmasters.com/courses/claude-code/?utm_source=email&utm_medium=nodeweekly&utm_content=claudecooper)

本课程提供免费的 Claude Code 深度教学，帮助开发者通过高级代理技术优化编码工作流，涵盖配置、权限管理、多代理系统及扩展集成等核心内容。

- 🎓 课程由 Anthropic 的 Lydia Hallie 主讲，她拥有十年软件工程与开发者体验经验，适合从入门到日常使用的所有开发者
- ⚙️ 学习如何通过 CLAUDE.md 文件、技能和钩子配置 Claude Code，自动化重复任务并提升代码质量
- 🔒 掌握权限与模型配置，使用计划模式、拒绝模式及调整努力级别，平衡输出质量与成本
- 🤖 探索多代理系统编排，利用子代理和代理团队并行处理复杂工作流，保持上下文清晰
- 🔌 扩展与集成 Claude Code，通过插件、MCP 和 Agent SDK 连接外部工具和服务
- 📚 课程包含 16 节课、1.9 小时内容，提供完成证书，支持自定进度学习
- 🧠 学习如何通过结构化配置文件赋予 Claude 深度代码库上下文，更快写出更优代码
- 🎯 涵盖权限、技能、钩子、插件及 Claude Desktop 等模块，总时长约 1 小时 56 分钟
- 🏆 完成课程后可获得证书，便于在 LinkedIn 上展示专业发展成果
- 💬 课程获得 4.6 评分，开发者评价其提供了关于插件生态、Coworker 和 Claude SDK 的宝贵见解

---

### [Node.js — Node.js 26.3.1（当前版本）](https://nodejs.org/en/blog/release/v26.3.1)

**原文标题**: [Node.js — Node.js 26.3.1 (Current)](https://nodejs.org/en/blog/release/v26.3.1)

Node.js 26.3.1 是一个安全更新版本，修复了多个高危和中危漏洞，并更新了依赖库。

- 🛡️ 修复了 TLS 模块中的主机名校验漏洞 (CVE-2026-48618)，等级为高
- 🔐 修复了 WebCrypto 密码输出长度保护问题 (CVE-2026-48933)，等级为高
- 🎭 在隧道错误中隐藏代理凭据 (CVE-2026-48615)，等级为中
- 📊 限制 HTTP/2 originSet 大小以防止内存无限增长 (CVE-2026-48619)，等级为中
- 🔍 修复了 TLS SNI 上下文匹配的大小写敏感问题 (CVE-2026-48928)，等级为中
- 🚫 拒绝包含空字节的主机名 (CVE-2026-48930)，等级为中
- 🔗 将会话绑定到已验证的主机 (CVE-2026-48934)，等级为中
- ⚙️ 修复了权限模型中的多个低危问题 (CVE-2026-48617, CVE-2026-48931, CVE-2026-48935, CVE-2026-48936)
- 📦 更新了 llhttp、undici 和 OpenSSL 等依赖库
- 💻 提供 Windows、macOS、Linux 等多平台安装包

---

### [Node.js — 2026 年 6 月 18 日，星期四 安全发布](https://nodejs.org/en/blog/vulnerability/june-2026-security-releases)

**原文标题**: [Node.js — Thursday, June 18, 2026 Security Releases](https://nodejs.org/en/blog/vulnerability/june-2026-security-releases)

Node.js 於 2026 年 6 月 18 日發布了針對 22.x、24.x 和 26.x 版本線的安全更新，修復了多個漏洞，最高嚴重等級為高（HIGH）。

- 🔒 **高嚴重性漏洞**：CVE-2026-48933（WebCrypto AES 整數溢出導致遠程進程中止）和 CVE-2026-48618（Unicode 點分隔符導致 TLS 通配符深度認證繞過）影響所有支援版本線。
- 🛡️ **中等嚴重性漏洞**：包括代理憑證洩漏（CVE-2026-48615）、HTTP/2 無限制 ORIGIN 幀導致記憶體耗盡（CVE-2026-48619）、GOAWAY 後未清理連線（CVE-2026-48937）、大寫 SNI 上下文匹配繞過（CVE-2026-48928）、嵌入式空主機名繞過（CVE-2026-48930）、TLS 會話重用繞過（CVE-2026-48934）等。
- ⚠️ **低嚴重性漏洞**：包括權限模型繞過（CVE-2026-48617、CVE-2026-48935、CVE-2026-48936）和 HTTP 響應隊列中毒（CVE-2026-48931）。
- 📦 **依賴更新**：所有版本線更新了 llhttp、nghttp2 和 openssl，特定版本線更新了 undici。
- 🆕 **新版本發布**：Node.js v22.23.0、v24.17.0 和 v26.3.1 已可用。
- 🗓️ **安全政策**：請參考 https://nodejs.org/en/security/，並訂閱 nodejs-sec 郵件列表以獲取未來安全公告。

---

### [Node.js — Node.js 24.17.0 (长期支持版)](https://nodejs.org/en/blog/release/v24.17.0)

**原文标题**: [Node.js — Node.js 24.17.0 (LTS)](https://nodejs.org/en/blog/release/v24.17.0)

Node.js 24.17.0 (LTS) 是一个安全更新版本，修复了多个漏洞，包括高危、中危和低危问题。

- 🔒 修复了两个高危漏洞：tls 服务器身份检查中的主机名规范化问题，以及 WebCrypto 密码输出长度保护
- 🛡️ 修复了六个中危漏洞：代理凭证泄露、http2 内存增长、SNI 上下文匹配、NUL 字节拒绝、会话绑定和 nghttp2 集成问题
- ⚠️ 修复了三个低危漏洞：process.chdir 权限处理、http.Agent 响应队列中毒和 FileHandle utimes 权限禁用
- 📦 更新了多个依赖库：llhttp 9.4.2、nghttp2 1.69.0、openssl 3.5.7 和 undici 7.28.0
- 💻 提供 Windows、macOS、Linux、AIX 和 ARM 等多种平台的安装包和二进制文件

---

### [Node.js — Node.js 22.23.0（长期支持版）](https://nodejs.org/en/blog/release/v22.23.0)

**原文标题**: [Node.js — Node.js 22.23.0 (LTS)](https://nodejs.org/en/blog/release/v22.23.0)

Node.js 22.23.0（LTS）是一个安全更新版本，代号“Jod”，发布于 2026 年 6 月 18 日，主要修复了多个高危和中危安全漏洞，并更新了相关依赖。

- 🔒 修复 tls 模块中的主机名规范化问题，增强服务器身份验证安全性（高危）
- 🔐 修复 WebCrypto 加密输出长度检查，防止数据泄露（高危）
- 📦 更新 nghttp2 依赖，解决集成问题（中危）
- 🚫 拒绝包含嵌入 NUL 字节的主机名，防止 DNS/网络攻击（中危）
- 📉 限制 http2 的 originSet 大小，避免内存无限增长（中危）
- 🕵️ 在隧道错误中隐藏代理凭据，保护敏感信息（中危）
- 🔗 将可复用的 TLS 会话绑定到已验证主机，防止会话劫持（中危）
- 🔍 修复 TLS SNI 上下文匹配的大小写敏感问题（中危）
- 📝 修复权限模型中 process.chdir 对 writereport 的影响（低危）
- 🧹 修复 http.Agent 中的响应队列污染问题（低危）
- 🚫 在权限模型下禁用 FileHandle 的 utimes 操作（低危）
- ⬆️ 更新 llhttp 到 9.4.2、undici 到 6.27.0、OpenSSL 到 3.5.7 等多个依赖
- 🗑️ 移除 http2 中的优先级信号支持（重大变更）
- 🖥️ 提供 Windows、macOS、Linux、AIX 等多平台安装包和二进制文件

---

### [tls: 规范化服务器身份验证的主机名 · nodejs/node@ebda734 · GitHub](https://github.com/nodejs/node/commit/ebda73470d)

**原文标题**: [tls: normalize hostname for server identity checks · nodejs/node@ebda734 · GitHub](https://github.com/nodejs/node/commit/ebda73470d)

该提交修复了 TLS 服务器身份验证中的一个安全漏洞（CVE-2026-48618），涉及主机名规范化处理。

- 🔒 **安全漏洞修复**：修复了主机名验证中的安全漏洞（CVE-2026-48618），该漏洞由 HackerOne 报告（编号 3688064）
- 🌐 **IDN 主机名规范化**：引入`domainToASCII`函数，将国际化域名（IDN）转换为 ASCII 格式，确保正确匹配证书
- 🧹 **移除尾随点**：在验证前移除主机名尾随点（FQDN 格式），统一比较标准
- ✅ **新增测试用例**：添加针对中文句号（。）等特殊字符的测试，验证 IDN 主机名验证的正确性
- 📁 **文件变更**：修改`lib/tls.js`（+13/-7 行）和`test/parallel/test-tls-check-server-identity.js`（+9 行）
- 👨‍💻 **贡献者**：由 Matteo Collina 提交，Antoine du Hamel 审核

---

### [Web Crypto API | Node.js v26.3.1 文档](https://nodejs.org/api/webcrypto.html)

**原文标题**: [Web Crypto API | Node.js v26.3.1 Documentation](https://nodejs.org/api/webcrypto.html)

Node.js v26.3.1 的 Web Crypto API 文档提供了对 Web 加密标准的完整实现，并扩展了现代算法与安全曲线支持，涵盖了密钥生成、加密解密、签名验证、密钥派生、封装等核心功能。

- 🔑 **密钥生成与管理**：支持生成对称密钥（如 AES、HMAC）和非对称密钥对（如 RSA、ECDSA、Ed25519、X25519），并提供导入、导出、封装/解封密钥的功能。
- 🔒 **加密与解密**：支持多种加密算法，包括 AES-CBC/CTR/GCM/OCB、ChaCha20-Poly1305 和 RSA-OAEP，确保数据机密性。
- ✍️ **签名与验证**：支持 ECDSA、Ed25519、HMAC、RSA-PSS 等算法，用于数字签名和完整性验证。
- 🔗 **密钥派生**：支持 PBKDF2、HKDF、ECDH、X25519 和 Argon2 等算法，用于从密码或共享秘密派生密钥。
- 🧩 **摘要与哈希**：支持 SHA-1/256/384/512、SHA-3 系列、SHAKE、cSHAKE、TurboSHAKE 和 KangarooTwelve 等哈希算法。
- 🆕 **现代算法**：新增对 ML-KEM（密钥封装）、ML-DSA（数字签名）、KMAC、Argon2、AES-OCB、ChaCha20-Poly1305 等现代算法的支持，需特定 OpenSSL 版本。
- 🔍 **运行时检测**：通过 `SubtleCrypto.supports()` 方法可在运行时检测算法支持情况，便于编写兼容代码。
- 📦 **密钥格式**：支持 `raw`、`pkcs8`、`spki`、`jwk` 以及 `raw-secret`、`raw-public`、`raw-seed` 等格式的导入导出。
- 🧰 **核心类**：包括 `Crypto`（提供 `subtle`、`getRandomValues`、`randomUUID`）、`CryptoKey`（算法、可提取性、类型、用途）和 `SubtleCrypto`（所有加密操作）。
- 📚 **算法参数**：详细定义了各算法所需的参数类，如 `AesCbcParams`、`EcdsaParams`、`HkdfParams`、`Argon2Params` 等，确保正确调用。

---

### [发布 v8.5.0 · nodejs/undici · GitHub](https://github.com/nodejs/undici/releases/tag/v8.5.0)

**原文标题**: [Release v8.5.0 · nodejs/undici · GitHub](https://github.com/nodejs/undici/releases/tag/v8.5.0)

Undici v8.5.0 是一个重要的安全更新版本，修复了 8 个安全漏洞，其中包括多个高危漏洞，建议所有用户立即升级。

- 🚨 **高危漏洞**：修复了 WebSocket 拒绝服务攻击（CVE-2026-12151 和 CVE-2026-9675），攻击者可通过发送大量小片段或空片段导致内存耗尽
- 🔒 **TLS 证书绕过**：修复了 SOCKS5 代理中 TLS 证书验证被忽略的问题（CVE-2026-9697），防止中间人攻击
- 🌐 **跨源请求路由**：修复了 SOCKS5 代理池跨源复用问题（CVE-2026-6734），防止凭据泄露到错误目标
- ⚠️ **中等风险**：修复了共享缓存中因空白字符导致的跨用户信息泄露（CVE-2026-9678）
- 🛡️ **HTTP 头注入**：修复了 Set-Cookie 解析中的百分号解码漏洞（CVE-2026-9679），防止会话固定和缓存投毒
- 🔑 **SameSite 属性降级**：修复了 Cookie 解析中 SameSite 属性匹配过于宽松的问题（CVE-2026-11525）
- ⏱️ **响应队列投毒**：修复了 HTTP/1.1 keep-alive 连接中响应错配的竞态条件漏洞（CVE-2026-6733）
- 📦 **其他改进**：包含 HTTP/2 改进、新增 bodyMixin.textStream() 方法、EventSource 规范对齐等非安全更新

---

### [npm v12 即将到来的重大变更 - GitHub 更新日志](https://github.blog/changelog/2026-06-09-upcoming-breaking-changes-for-npm-v12/)

**原文标题**: [Upcoming breaking changes for npm v12 - GitHub Changelog](https://github.blog/changelog/2026-06-09-upcoming-breaking-changes-for-npm-v12/)

npm v12 将于 2026 年 7 月发布，引入多项安全相关的默认变更，旨在将自动执行的安装行为改为显式选择加入，用户可在当前版本中提前准备。

- 🔒 `allowScripts` 默认关闭：`npm install` 不再自动执行依赖中的 `preinstall`、`install` 或 `postinstall` 脚本（包括原生 `node-gyp` 构建），需通过 `npm approve-scripts` 显式授权信任的包，并提交 `package.json` 中的白名单。
- 🚫 `--allow-git` 默认设为 `none`：`npm install` 不再解析 Git 依赖（直接或间接），以防止通过 `.npmrc` 覆盖 Git 可执行文件的代码执行风险。
- 🌐 `--allow-remote` 默认设为 `none`：`npm install` 不再解析远程 URL 依赖（如 https tarballs），需通过 `--allow-remote` 显式允许。
- ⚙️ 准备方法：升级到 npm 11.16.0+，运行安装并检查警告；使用 `npm approve-scripts --allow-scripts-pending` 查看脚本包，批准信任的包并提交更新；未批准的脚本将在升级后停止运行。

---

### [安装脚本允许列表 | Andrew Nesbitt](https://nesbitt.io/2026/06/05/install-script-allowlists.html)

**原文标题**: [Install-script allowlists | Andrew Nesbitt](https://nesbitt.io/2026/06/05/install-script-allowlists.html)

### 概述总结
本文全面梳理了各类包管理器对依赖安装时脚本执行的安全控制机制，重点对比了基于白名单的逐包许可模式与全局沙箱模式，并涵盖了 JavaScript、Python、Ruby、系统语言、JVM、.NET、操作系统包管理器及用户级包管理器等生态的现状。

- 📦 **npm/pnpm/Bun/Deno** 采用逐包许可白名单模式，通过 `allowScripts`、`onlyBuiltDependencies`、`trustedDependencies` 等字段控制脚本执行，Deno 和 Bun 默认禁止依赖脚本运行
- 🛡️ **全局沙箱方案**（opam、SwiftPM、Nix、Guix、Portage）对所有包执行脚本但限制其系统访问能力，如 Nix 使用 chroot 和网络隔离
- 🔑 **身份签名验证**（RubyGems、Gradle、NuGet、apt-secure）仅验证发布者身份，不限制脚本执行能力，属于不同安全维度
- ⚠️ **Python 生态** 缺乏原生白名单机制，pip 仅提供全局 `--only-binary :all:` 控制，uv 和 Poetry 通过组合配置实现逐包源构建许可
- 🚫 **Go 和 Bazel** 设计上避免第三方代码执行，Go 仅编译不运行下载代码，Bazel 使用 Starlark 沙箱语言限制构建脚本能力
- 🔓 **高风险领域** 包括 CPAN、RubyGems、Cargo、Zig、Conan、OS 包管理器（dpkg/RPM/pacman）等，缺乏逐包许可或沙箱保护
- 🧩 **JVM 生态** 依赖被动 JAR 文件，构建插件（Maven/Gradle/SBT）在配置阶段执行任意代码，无内置白名单机制
- 📋 **新兴改进** 包括 npm 11.x 的 advisory 模式、pnpm v11 的 `allowBuilds`、Deno 的 `approve-scripts`、Composer 2.2 的 `allow-plugins` 等

---

### [Iroh 1.0 - 拨号键，而非 IP 地址 - Iroh](https://www.iroh.computer/blog/v1)

**原文标题**: [Iroh 1.0 - Dial Keys, not IPs - Iroh](https://www.iroh.computer/blog/v1)

Iroh 1.0 发布，核心概念是“拨号密钥，而非 IP 地址”，旨在构建更安全、高效、直接的互联网连接方式。

- 🔑 **核心创新**：用用户控制的密钥替代易变的 IP 地址，实现设备在任何网络环境下都可安全寻址。
- 🚀 **版本里程碑**：经过 65 个版本迭代后发布 1.0 稳定版，过去 30 天公共中继已创建超 2 亿个端点。
- 🌐 **开放标准**：基于 IETF 草案构建，实现 QUIC 多路径与 NAT 穿透，支持本地优先配置和 WASM 编译。
- 🔌 **自定义传输**：支持蓝牙低功耗、LoRa、WiFi Aware 甚至 Tor 等自定义传输层，统一在“拨号密钥”抽象下。
- 💻 **多语言支持**：除 Rust 外，正式支持 Python、Node.js、Swift 和 Kotlin，便于嵌入 iOS/Android 应用。
- 🛡️ **稳定性承诺**：v1.0 保证线缆协议和语言 API 的稳定性，未来可能独立版本化，重大变更将伴随主版本更新。
- 📅 **支持计划**：v1.0 提供长期支持，v0.35x 公共中继支持至 2026 年底，v0.9x 及 RC 版本支持至 2026 年 9 月。
- ⚡ **效率优势**：95% 的数据通过设备直连传输，减少云中转次数，降低出口费用并提升网络效率。
- 🎯 **应用场景**：已用于流媒体、大语言模型训练、安全聊天、游戏、文件传输等，运行在数百万设备上。

---

### [JavaScript - iroh](https://docs.iroh.computer/languages/javascript)

**原文标题**: [JavaScript - iroh](https://docs.iroh.computer/languages/javascript)

本页介绍了通过 JavaScript 绑定使用 iroh 库的方法，支持多平台安装、基础示例（单节点和双节点通信）以及后续学习资源。

- 📦 **安装要求**：通过 npm 安装 `@number0/iroh`，需 Node.js 20.3.0+，支持 macOS（arm64）、Linux（x86_64/aarch64/armv7）、Windows（x86_64/aarch64）和 Android（aarch64/armv7），无需 Rust 工具链。
- 🚀 **基础示例**：使用 `Endpoint.bind` 创建节点，通过 ALPN 协议标识连接，演示了单节点打印 ID 和双节点双向流通信（发送/接收消息）。
- 🔄 **双节点回声**：接收端监听连接并回传消息，发送端通过 ticket 连接并发送 "hello"，实现简单回声功能。
- 📚 **后续资源**：提供端点连接教程、示例应用（hello-iroh-ffi）、JavaScript API 文档和 GitHub 源码仓库，支持多语言学习。

---

### [今日发布 Babel 8：仅支持 ESM，放弃 ES5 默认，并提供平滑迁移路径 · Babel](https://babeljs.io/blog/2026/06/16/8.0.0/)

**原文标题**: [Releasing Babel 8 today: ESM-only, drop ES5 default, and a smooth migration path · Babel](https://babeljs.io/blog/2026/06/16/8.0.0/)

Babel 8 今日发布：仅支持 ESM、放弃 ES5 默认配置，并提供平滑迁移路径

- 🎉 Babel 8 正式发布，距离 Babel 7 已过去 8 年，此次更新聚焦核心现代化，为未来 8 年做准备
- 📈 Babel 周下载量从 2018 年的 170 万增长到 2026 年 6 月的 6.51 亿，过去一年翻倍，用户基础持续扩大
- 🚀 主要变更：Babel 8 仅支持 ESM（要求 Node.js 22+）、默认不再编译到 ES5（改用 Browserslist 默认值）、为所有包提供 TypeScript 类型
- 🔧 废弃 `loose` 和 `spec` 选项，推荐使用更精细的 `assumptions` 配置；polyfill 注入移至独立包 `babel-plugin-polyfill-corejs3`
- 💡 迁移路径简化：建议在升级前先迁移到 `assumptions` 和独立 polyfill 插件，Babel 7 用户可参考官方升级指南
- 💸 资金挑战：捐款持续下降，尽管下载量增长，核心团队呼吁用户和企业通过 Open Collective 或 GitHub Sponsors 支持，或参与新 ECMAScript 提案开发
- 🛡️ Babel 7 将停止新功能更新，但提供一年安全支持（至 2027 年 6 月），如有需要可联系团队讨论回滚

---

### [在 neonctl 中实现无需 psql 的纯 TypeScript 客户端](https://neon.com/blog/shipping-psql-without-psql)

**原文标题**: [Shipping psql without psql: a pure-TypeScript client in neonctl - Neon](https://neon.com/blog/shipping-psql-without-psql)

### 概述总结
Neon 团队通过 AI 编码助手（Claude Code）构建了一个纯 TypeScript 的嵌入式 psql 客户端，实现了与原生 psql 的字节级行为一致性，并建立了严格的验证框架。

- 🚀 **核心创新**：在 neonctl 中嵌入纯 TypeScript 的 psql 实现，无需安装原生依赖即可在任意平台运行
- 🔍 **验证框架**：构建了字节级一致性测试框架，直接对比 PostgreSQL 官方回归测试套件的输出结果
- ⚠️ **安全审查**：对 AI 生成的代码进行对抗性安全审查，发现了静默降级 sslmode、可跳过的 SCRAM 认证等关键漏洞
- 🧪 **测试矩阵**：在 PostgreSQL 14-18 版本上运行 CI 矩阵测试，确保跨版本兼容性
- 📋 **功能覆盖**：实现了完整的 REPL、46 种反斜杠命令、所有输出格式、连接层和认证 TLS 功能
- 💡 **关键发现**：纯 TS 客户端的 TLS 行为取决于运行时的加密库（Bun 使用 BoringSSL，Node 使用 OpenSSL）
- 🎯 **设计取舍**：故意不支持 GSSAPI/SSPI 和某些 keepalive 参数，保持零原生依赖
- 🔒 **信任机制**：信任来自测试框架而非 AI 模型，字节级差异比较和对抗性审查是安全保证

---

### [LinkedIn 工作邀请中的后门 - Roman Imankulov](https://roman.pt/posts/linkedin-backdoor/)

**原文标题**: [A backdoor in a LinkedIn job offer - Roman Imankulov](https://roman.pt/posts/linkedin-backdoor/)

### 概述总结
一名 Python 开发者收到伪装成招聘测试的恶意 GitHub 仓库，通过只读 AI 工具发现其中隐藏的后门代码，该攻击利用 npm 自动安装脚本触发远程控制，并盗用真实开发者身份和记者账号进行伪装。

- 🕵️ 攻击伪装：通过 LinkedIn 发送"检查废弃 Node 模块"的招聘测试，诱导开发者运行`npm install`
- 🔍 检测过程：使用只读 AI 工具（Pi）扫描代码库，立即在`app/test/index.js`中发现可疑 URL 拼接
- 🚨 后门机制：`package.json`的`prepare`脚本在安装依赖时自动执行，从远程服务器获取恶意载荷
- 👤 身份盗用：GitHub 提交记录冒用真实开发者身份（39 次提交），LinkedIn 账号盗用文化记者身份
- ⚠️ 安全建议：对招聘方发送的代码库保持警惕，使用只读环境审查代码，避免直接运行`npm install`
- 📊 攻击现状：报告给 GitHub 和 LinkedIn 后，恶意仓库和账号仍未被处理

---

### [LinkedIn 如何借助 Orkes 将代码审查转变为多智能体管道，并实现 18 倍吞吐量提升 - YouTube](https://www.youtube.com/watch?v=yoCQuX1zbho)

**原文标题**: [How LinkedIn Turned Code Review Into a Multi Agent Pipeline With Orkes and Unlocked 18x Throughput - YouTube](https://www.youtube.com/watch?v=yoCQuX1zbho)

本頁面為 YouTube 平台的綜合資訊頁面，涵蓋了從版權、聯絡方式到政策與安全等核心運作規範。

- 📰 提供新聞中心入口，供使用者獲取最新官方資訊與公告。
- ©️ 明確版權相關資訊，保障內容創作者與平台的權益。
- 📞 設有聯絡我們管道，方便使用者與平台溝通。
- 🎥 為創作者提供專屬資源與支援，協助內容產出與成長。
- 📢 說明刊登廣告的選項，讓品牌與創作者能進行合作。
- 👨‍💻 提供開發人員相關資源，如 API 與技術文件。
- 📜 列出使用條款，規範使用者與平台間的權利義務。
- 🔒 強調私隱政策，保護用戶個人資料安全。
- 🛡️ 說明政策及安全措施，確保平台使用環境健康。
- ⚙️ 解釋 YouTube 的運作方式，包括演算法與內容推薦機制。
- 🧪 測試新功能，持續優化使用者體驗。
- ©️ 版權年份為 2026 Google LLC，確認平台歸屬。

---

### [什么是 Git 工作树，以及为什么我应该使用它们？ - GitHub 博客](https://github.blog/ai-and-ml/github-copilot/what-are-git-worktrees-and-why-should-i-use-them/)

**原文标题**: [What are git worktrees, and why should I use them? - The GitHub Blog](https://github.blog/ai-and-ml/github-copilot/what-are-git-worktrees-and-why-should-i-use-them/)

### 概述总结
Git 工作树（worktrees）是自 2015 年就存在的功能，但近期因 AI 和并行开发需求而流行。它允许开发者在不切换分支或暂存代码的情况下，同时处理多个任务，减少上下文切换开销。

- 🧠 **降低心智负担**：无需 `git stash` 或切换分支，避免重新加载文件和依赖，保持编辑器上下文不变。
- 🚀 **并行工作流**：通过 `git worktree add` 创建独立文件夹，可同时处理多个任务（如紧急修复和功能开发），互不干扰。
- 🤖 **AI 时代适配**：AI 工具（如 GitHub Copilot）默认使用工作树，支持人机并行协作，适应现代“代码评审文化”。
- ⚠️ **潜在问题**：每个工作树需独立依赖副本（如 `node_modules`），可能占用大量磁盘空间；需手动管理文件夹避免混乱。
- 🛠️ **使用场景**：适合需要频繁切换上下文、并行处理多个分支的开发者，但并非万能，需根据个人习惯选择。

---

### [在 Cloudflare Workers 中程序化设置 Node 和 PNPM 版本](https://senhongo.com/blog/cloudflare-workers-node-pnpm/)

**原文标题**: [Setting Node and PNPM versions in Cloudflare Workers programmatically](https://senhongo.com/blog/cloudflare-workers-node-pnpm/)

概述总结  
- 📅 文章发布于 2026 年 6 月 15 日，涉及 dev、node、pnpm 和 Cloudflare Workers 等类别。  
- ⚙️ 在 Cloudflare Workers 中，可通过环境变量`NODE_VERSION`和`PNPM_VERSION`设置 Node 和 PNPM 版本，但作者更倾向在代码中设置版本范围。  
- 📄 Node 版本必须通过`.nvmrc`文件指定，支持具体版本（如 24.16.0）或 LTS 最新版（如`lts/*`），但`lts/krypton`在 Workers 中无效。  
- 📦 PNPM 版本需在`package.json`中添加`packageManager`字段（如`pnpm@11.6.0`），并建议同时设置`devEngines.packageManager`，但该字段不支持版本范围。  
- ❌ `packageManager`字段由 Corepack 强制执行，不支持范围；PNPM 的`devEngines.packageManager`虽支持范围，但与 Corepack 策略冲突，需指定单一版本。  
- 🚫 `wrangler.jsonc`中的`vars`字段对环境变量无效，不能用于 Node 和 PNPM 版本设置。

---

### [Wasp 现在允许你用 TypeScript 编写全栈逻辑规范 | Wasp](https://wasp.sh/blog/2026/06/15/wasp-typescript-spec)

**原文标题**: [Wasp now lets you write your full-stack logic as a spec in TypeScript | Wasp](https://wasp.sh/blog/2026/06/15/wasp-typescript-spec)

Wasp 现在允许你使用 TypeScript 规范来定义全栈逻辑，取代了之前的自定义 DSL，使规范层更灵活、可编程且与 TypeScript 生态兼容。

- 🎯 **核心升级**：Wasp 用 TypeScript 规范（TS Spec）替代了旧的自定义 DSL，开发者现在通过 `*.wasp.ts` 文件编写全栈逻辑，使用 `@wasp.sh/spec` 中的构造器（如 `page`、`route`、`query`）定义应用。
- 🔧 **TypeScript 原生能力**：TS Spec 支持使用第三方库、拆分文件、自定义函数、读取环境变量等，仅需从 `main.wasp.ts` 导出 `app` 规范对象。
- 🧩 **实现与规范分离**：通过 `with { type: "ref" }` 导入将规范与 React、Node.js、Prisma 实现连接，不会实际执行导入，而是转换为引用对象。
- 🚀 **独特示例**：TS Spec 允许实现文件路由，例如通过读取 `src/` 目录动态生成 `route` 和 `page` 对象，这是旧 DSL 无法做到的。
- 💡 **规范作为一等公民**：Wasp 将规范显式化、可编程、独立于栈，支持组织、重用和分发，未来计划引入“可扩展规范”和“全栈模块（FSM）”。
- 🤖 **AI 友好**：规范提供应用高级概览，避免实现细节干扰，并支持全栈模块，确保 AI 使用更大构建块时不会出错。
- 📅 **未来计划**：包括改进 TS Spec（如引入数据模型）、全栈模块、Wasp 1.0 核心重构、支持其他 ORM（如 Drizzle）和前端库（如 Svelte、Vue）。

---

### [pnpm 为何不再在仓库的 .npmrc 中展开环境变量 | pnpm](https://pnpm.io/blog/2026/06/11/env-variables-in-repository-npmrc)

**原文标题**: [Why pnpm no longer expands environment variables in a repository's .npmrc | pnpm](https://pnpm.io/blog/2026/06/11/env-variables-in-repository-npmrc)

pnpm 在 v10.34.2 和 v11.5.3 版本中停止了在仓库的 .npmrc 文件中展开环境变量，这是一项安全修复。
- 🛡️ **安全漏洞修复**：恶意仓库可通过在 .npmrc 中使用 `${ENV_VAR}` 占位符，在依赖解析阶段窃取环境中的令牌，无需运行任何脚本。
- 🔒 **信任感知变更**：pnpm 现在对仓库控制的文件（如项目 .npmrc 和 pnpm-workspace.yaml）中的 registry、认证令牌等设置，不再展开环境变量，仅信任用户级配置、全局配置、命令行选项和环境配置。
- ⚠️ **迁移方法**：将令牌从仓库的 .npmrc 移至用户/全局配置（使用 `pnpm config set`）、环境变量（如 `pnpm_config_//registry.npmjs.org/:_authToken=$NPM_TOKEN`）或用户级 ~/.npmrc 中。
- 🚀 **新功能支持**：v11.7 支持按包作用域选择不同认证令牌，无需使用环境变量占位符；v11.6 支持通过环境变量直接提供凭证。
- 💔 **致歉与解释**：在补丁版本中引入破坏性变更是不得已之举，但为了修复已验证的安全漏洞，必须立即行动，避免用户秘密被窃取。

---

### [Nodemailer](https://nodemailer.com/)

**原文标题**: [Nodemailer](https://nodemailer.com/)

Nodemailer 是 Node.js 最流行的邮件发送库，零依赖、安全可靠，支持多种传输方式和高级功能。

- 📧 **核心功能**：通过 SMTP、Sendmail、Amazon SES 等多种传输方式发送邮件，支持 HTML/纯文本、附件和嵌入图片。
- 🔒 **安全特性**：内置 TLS/STARTTLS 加密、DKIM 签名和 OAuth2 认证，防止远程代码执行漏洞。
- 🌍 **跨平台兼容**：无需原生依赖，完美运行于 Linux、macOS、Windows 及云环境（如 Azure），支持全 Unicode 和 emoji。
- 🚀 **快速上手**：三步即可发送邮件：创建 transporter（配置 SMTP）、编写消息（发件人/收件人/内容）、调用 `sendMail()`。
- 🔧 **高级功能**：支持代理、插件 API、Ethereal.email 测试账户、流式传输和 JSON 输出，满足复杂场景需求。
- 📊 **响应处理**：返回 `messageId`、`envelope`、`accepted`/`rejected` 数组，支持部分成功和详细错误码（如 ECONNECTION、EAUTH）。
- 📡 **事件监听**：提供 `idle`（池化连接空闲）、`error`（传输错误）、`token`（OAuth2 令牌更新）等事件。
- 📜 **开源许可**：基于 MIT-0 许可证，无需署名，可自由使用，源码托管于 GitHub。

---

### [GitHub - gajus/zod-compiler: 在构建时将 Zod 模式编译为零开销的验证函数。支持 Vite、webpack、esbuild、Rollup 等](https://github.com/gajus/zod-compiler)

**原文标题**: [GitHub - gajus/zod-compiler: Compile Zod schemas into zero-overhead validation functions at build time. Works with Vite, webpack, esbuild, Rollup, etc · GitHub](https://github.com/gajus/zod-compiler)

## 概述摘要
zod-compiler 是一个构建时工具，能将 Zod 模式编译成零开销的验证函数，实现 2-75 倍的性能提升，同时保持与现有 Zod 模式的完全兼容。

- 🚀 **核心功能**：在构建时自动编译 Zod 模式，生成优化的验证函数，无需修改源代码
- 🔧 **多种使用方式**：支持自动模式（默认）、显式 compile() 包装和 CLI 生成三种方式
- ⚡ **性能提升**：在各类场景下实现 2-75 倍加速，特别是嵌套对象和数组场景提升最显著
- 🛠️ **广泛兼容**：支持 Vite、webpack、esbuild、Rollup 等主流构建工具
- 📦 **模式提升**：自动将函数内定义的模式提升到模块作用域，避免重复构建
- 🔍 **诊断工具**：提供 `npx zod-compiler check` 命令分析模式编译覆盖率和快速路径资格
- 🎯 **双阶段验证**：生成快速路径（零分配布尔链）和慢速路径（错误收集）的优化验证器
- 🔗 **完全兼容**：保持原始 Zod 对象身份，支持 tRPC、Hono、React Hook Form 等框架
- 🧩 **智能降级**：不支持编译的特性（如带捕获的 transform）自动回退到 Zod 运行时验证
- 📉 **包体积优化**：通过共享运行时、结构去重和紧凑输出模式显著减小生成代码体积

---

### [发布 · yagop/node-telegram-bot-api · GitHub](https://github.com/yagop/node-telegram-bot-api/releases)

**原文标题**: [Releases · yagop/node-telegram-bot-api · GitHub](https://github.com/yagop/node-telegram-bot-api/releases)

node-telegram-bot-api 库的版本发布记录，展示了从 v0.26.0 到 v1.1.0 的主要更新，包括重大重写、新功能支持和 API 兼容性改进。

- 🚀 **v1.1.0 最新版**：支持 Telegram Bot API 10.1，新增富消息、加入请求查询和投票类型，无破坏性变更。
- 🔄 **v1.0.0 重大重写**：从 JavaScript 重写为 TypeScript，改为 ESM-only，要求 Node.js ≥ 18，移除旧版选项和 CJS 支持。
- 📦 **类型系统升级**：v1.0.0 提供完整 TypeScript 类型，替换社区 @types 包，类型改为扁平命名导出。
- 📝 **旧版 v0.67.0**：支持 Bot API v7.4 至 v9.1，新增支付、礼物、商业账户和故事功能。
- 🎲 **v0.50.0 功能扩展**：支持 Bot API v4.4 至 v4.8，新增掷骰子、命令管理和权限设置方法。
- 🛠️ **v0.30.0 增强**：支持 Bot API v3.4 和 v3.5，新增媒体组、文件流和实时位置编辑，修复偏移无限循环 bug。
- 📜 **早期版本**：v0.26.0 至 v0.29.0 包含基础 API 支持和错误修复，详情见 CHANGELOG.md。

---

### [Telegram 机器人 API](https://core.telegram.org/bots/api)

**原文标题**: [Telegram Bot API](https://core.telegram.org/bots/api)

Telegram Bot API 是一个基于 HTTP 的接口，用于开发者构建 Telegram 机器人。它提供了丰富的功能，包括发送和接收消息、管理群组、处理支付、游戏和富文本消息等。API 支持通过轮询或 Webhook 接收更新，并提供了多种方法来管理机器人的命令、名称和描述。

- 🤖 **核心功能**：Bot API 允许开发者通过 HTTP 接口构建机器人，支持发送文本、媒体、轮询、游戏、发票等多种消息类型。
- 📡 **更新接收**：支持两种互斥的更新接收方式：`getUpdates`（长轮询）和 `setWebhook`（Webhook）。更新以 JSON 格式的 `Update` 对象返回。
- 📝 **消息格式化**：支持 MarkdownV2、HTML 和 Markdown 三种解析模式，用于格式化消息文本，包括粗体、斜体、下划线、删除线、代码块等。
- 📦 **富消息**：Bot API 10.1 引入了富消息功能，允许机器人发送高度结构化的文本，包括标题、列表、表格、媒体、引用、公式等，并支持流式传输部分内容。
- 👤 **用户与聊天管理**：提供了丰富的用户和聊天对象，包括 `User`、`Chat`、`ChatFullInfo`、`Message` 等，用于管理聊天成员、权限、邀请链接等。
- 🎮 **游戏与支付**：支持发送游戏、设置分数、获取高分榜；支持通过 Telegram Stars 或第三方支付提供商处理支付和发票。
- 🎁 **礼物与订阅**：支持发送和接收礼物（普通和独特礼物），以及 Telegram Premium 订阅的赠送和管理。
- 🛠️ **机器人管理**：提供管理机器人命令、名称、描述、个人资料照片、菜单按钮和默认管理员权限的方法。
- 🔒 **安全与验证**：支持通过 `secret_token` 验证 Webhook 请求，以及通过 Telegram Passport 处理身份验证数据。
- 🌐 **本地服务器**：可以运行本地 Bot API 服务器，以获得更大的文件上传限制、更灵活的 Webhook 配置等高级功能。

---

### [GitHub - sindresorhus/eslint-plugin-unicorn：超过200条强大的ESLint规则 · GitHub](https://github.com/sindresorhus/eslint-plugin-unicorn)

**原文标题**: [GitHub - sindresorhus/eslint-plugin-unicorn: More than 200 powerful ESLint rules · GitHub](https://github.com/sindresorhus/eslint-plugin-unicorn)

eslint-plugin-unicorn 是一个包含超过 200 条强大 ESLint 规则的插件，主要针对 JavaScript 和 TypeScript，也支持 CSS、HTML、JSON 和 Markdown 文件的检查。

- 📦 **安装与要求**：需安装 ESLint >=10.4，使用 flat config 和 ESM，可通过 `npm install --save-dev eslint eslint-plugin-unicorn` 安装。
- ⚙️ **配置使用**：支持预设配置或手动配置规则，需在 `eslint.config.js` 中设置 `languageOptions` 和 `plugins`，并提供 TypeScript 配置示例。
- 📋 **规则分类**：规则分为推荐配置（✅）、非推荐配置（☑️）、可自动修复（🔧）、手动修复（💡）和需要类型信息（💭），涵盖命名、语法、DOM、数组、字符串等众多方面。
- 🌐 **多语言支持**：部分规则可配合 ESLint 语言插件（如 `@eslint/css`）检查 CSS、HTML、JSON 和 Markdown 文件，需在配置中按文件类型隔离规则。
- 🗂️ **预设配置**：提供 `recommended` 和 `all` 预设，分别启用良好实践规则或所有非废弃规则，可扩展使用。
- 👥 **维护与社区**：由 Sindre Sorhus 和 Fisker Cheung 维护，拥有 5.1k 星标和 487 个分支，遵循 MIT 许可证，不接收拉取请求。

---

### [获取失败](https://nodeweekly.com/link/186748/web)

**原文标题**: [Failed to retrieve](https://nodeweekly.com/link/186748/web)

无法总结：获取内容失败，状态码 429。

---

### [eslint-plugin-unicorn/docs/rules/max-nested-calls.md 在 main 分支 · sindresorhus/eslint-plugin-unicorn · GitHub](https://github.com/sindresorhus/eslint-plugin-unicorn/blob/main/docs/rules/max-nested-calls.md)

**原文标题**: [eslint-plugin-unicorn/docs/rules/max-nested-calls.md at main · sindresorhus/eslint-plugin-unicorn · GitHub](https://github.com/sindresorhus/eslint-plugin-unicorn/blob/main/docs/rules/max-nested-calls.md)

概述摘要：该规则限制嵌套调用的深度，以提高代码可读性，建议将中间结果提取为命名变量。

- 📝 规则`max-nested-calls`用于限制嵌套调用的最大深度
- 💼🚫 在`recommended`配置中启用，在`unopinionated`配置中禁用
- 🧠 深层嵌套调用使代码难以阅读，应提取中间结果为命名变量
- 🔍 规则统计传入其他调用或构造器的调用和构造函数调用，忽略流畅接收器链和 JSX 包装器
- 📋 示例展示了错误和正确的写法，以及忽略的流畅链式调用
- ⚙️ 选项`max`为整数，默认值为 3，可自定义最大允许嵌套深度

---

### [获取失败](https://nodeweekly.com/link/186750/web)

**原文标题**: [Failed to retrieve](https://nodeweekly.com/link/186750/web)

无法总结：获取内容失败，状态码 429。

---

### [clerk 部署：引导式、可恢复、支持代理](https://clerk.com/changelog/2026-06-10-clerk-deploy?utm_source=cooper_press&utm_medium=newsletter&utm_campaign=cli-deploy&utm_content=06-18-26&dub_id=u8uvJJsU7QkGbfBg)

**原文标题**: [clerk deploy: guided, resumable, agent-ready](https://clerk.com/changelog/2026-06-10-clerk-deploy?utm_source=cooper_press&utm_medium=newsletter&utm_campaign=cli-deploy&utm_content=06-18-26&dub_id=u8uvJJsU7QkGbfBg)

概述摘要  
- 🚀 **clerk deploy 发布**：通过一条命令将应用从开发环境部署到生产环境，支持 DNS 和 OAuth 设置引导。  
- ⚙️ **自动化生产配置**：自动创建生产实例、提示输入生产域名、显示 DNS CNAME 记录并支持导出为区域文件。  
- 🔑 **OAuth 凭据集成**：检测开发中的社交连接，引导设置 Google 和 Apple 凭据（支持导入 JSON 或 .p8 密钥），其他提供商在仪表盘标记。  
- ✅ **验证与检查**：循环验证 DNS、SSL 和邮件 DNS，并报告待处理项。  
- 🤖 **代理模式支持**：在非 TTY 环境或使用 `--mode agent` 时，输出只读 JSON 状态而非交互提示。  
- 📘 **快速开始**：更新 CLI、链接项目后运行 `clerk deploy`，完整文档提供所有命令和选项。

---

### [GitHub - Agent-Field/pr-af: 基于 AgentField 构建的 AI 原生多智能体代码审查工具 · GitHub](https://github.com/Agent-Field/pr-af)

**原文标题**: [GitHub - Agent-Field/pr-af: AI-Native multi-agent Code Reviewer Built on AgentField · GitHub](https://github.com/Agent-Field/pr-af)

PR-AF 是一个基于 AgentField 构建的开源 AI 代码审查工具，能够为每个 PR 动态生成定制化的审查策略，并通过多阶段认知管道确保审查结果的高准确性和深度。

- 🧠 **动态审查策略**：PR-AF 不依赖固定检查清单，而是分析 PR 变更内容，动态编译审查维度并生成专门的审查 Agent，实现每 PR 一策略。
- 🔍 **零误报证据锚定**：通过程序化 AST 提取代码片段，在独立验证层核实审查发现，无法证实的主张会被静默剔除，确保零误报。
- 🔗 **复合漏洞合成**：跨文件关联分析孤立异常，识别组合风险，例如将未保护的 API 密钥与数据库漏洞合并为高严重性“协同注入”发现。
- ✅ **可证伪性门控**：审查发现必须通过系统自身主动尝试推翻的严格验证，只有经受住自检的发现才会呈现给开发者。
- 💰 **成本低廉**：深度审查 500 行 PR 的 LLM 调用成本仅约 $0.80，完全开源免费。
- ⚡ **一键调用**：支持 `af` CLI 或原始 HTTP API 触发，实时流式输出进度和结果，并自动发布带有证据的 GitHub 内联评论。
- 🐳 **快速部署**：通过 Docker Compose 一键启动，并提供 GitHub Actions 集成，只需添加 `pr-af` 标签即可自动触发深度审查。
- ⏱ **执行时间**：全面并行管道执行约需 35-50 分钟，适合 CI/CD 门控场景，而非快速交互式开发。

---

### [发布 v3.0.0 · xojs/xo · GitHub](https://github.com/xojs/xo/releases/tag/v3.0.0)

**原文标题**: [Release v3.0.0 · xojs/xo · GitHub](https://github.com/xojs/xo/releases/tag/v3.0.0)

概述摘要  
- 🔥 **重大变更**：要求 Node.js 22，移除内置 React 支持，需单独配置 `eslint-config-xo-react`。  
- 📦 **规则整合**：所有规则统一到 `eslint-config-xo` 包中，合并了 `eslint-config-xo-typescript`。  
- 🛠 **集成更新**：`xoToEslintConfig` 导出替换为 `xo/eslint-adapter` 导入，简化 ESLint 集成。  
- 🌟 **新功能**：支持 CSS、Markdown、HTML、JSDoc 注释和正则表达式检查；新增 `--max-warnings` 标志和 ESLint 批量抑制功能。  
- 🚫 **错误优先**：有错误时隐藏警告，帮助聚焦关键问题；尊重全局 gitignore 并支持否定模式覆盖默认忽略。  
- 📋 **新规则**：添加了 `no-shadow`、`strict-boolean-expressions` 等大量新规则，涵盖 TypeScript、Unicorn 和 XO 专属规则。

---

### [发布说明 | Playwright](https://playwright.dev/docs/release-notes#version-161)

**原文标题**: [Release notes | Playwright](https://playwright.dev/docs/release-notes#version-161)

Playwright 发布了多个新版本，引入了大量新功能和改进，包括 WebAuthn 虚拟验证器、Web Storage API、HAR 录制、拖放 API、Aria 快照、屏幕录制、浏览器绑定、CLI 调试与追踪分析、测试代理、以及多项测试运行器和 UI 改进。

- 🔑 **WebAuthn 虚拟验证器**：新增 `browserContext.credentials` API，允许测试注册和响应 passkey 验证，无需真实硬件密钥。
- 🗃️ **Web Storage API**：新增 `page.localStorage` 和 `page.sessionStorage`，方便读写页面存储。
- 🌐 **HAR 录制集成**：`tracing.startHar()` 和 `tracing.stopHar()` 将 HAR 录制作为一等追踪 API，支持 `await using` 语法。
- 🪝 **拖放 API**：新增 `locator.drop()`，可模拟文件或剪贴板数据拖放，支持跨浏览器。
- 🎯 **Aria 快照增强**：`expect(page).toMatchAriaSnapshot()` 支持在 Page 上使用，新增 `boxes` 选项用于 AI 消费。
- 🛑 **测试中止**：新增 `test.abort()`，允许从 fixture、钩子或路由处理程序中中止当前测试。
- 🎬 **屏幕录制**：全新的 `page.screencast` API，支持视频录制、动作注释、视觉叠加和实时帧捕获。
- 🔗 **浏览器绑定**：新增 `browser.bind()` API，使启动的浏览器可被 `playwright-cli`、`@playwright/mcp` 等客户端连接。
- 📊 **可观测性仪表盘**：`playwright-cli show` 命令可打开仪表盘，查看所有绑定浏览器的状态并进行交互。
- 🐛 **CLI 调试器**：`npx playwright test --debug=cli` 允许编码代理通过 `playwright-cli` 附加和调试测试。
- 📋 **CLI 追踪分析**：`npx playwright trace` 命令允许从命令行探索 Playwright Trace，理解失败或片状测试。
- ♻️ **`await using` 支持**：许多 API 返回异步可释放对象，支持 `await using` 语法进行自动清理。
- 🎭 **Playwright 测试代理**：引入 Planner、Generator 和 Healer 三个自定义代理，指导 LLM 构建 Playwright 测试。
- ⏱️ **时间线视图**：合并报告中的 HTML 报告 Speedboard 选项卡现在显示时间线。
- 🖥️ **UI 模式和追踪查看器改进**：新增系统主题、搜索功能、网络面板重组、JSON 自动格式化。
- 🚀 **Chrome for Testing**：Playwright 现在运行在 Chrome for Testing 构建版本上，而非 Chromium。
- ⏳ **等待 Web 服务器输出**：`testConfig.webServer` 新增 `wait` 字段，支持正则表达式匹配服务器日志。
- 🏎️ **Speedboard**：HTML 报告中新增 Speedboard 选项卡，按执行时间排序显示测试。
- 🧪 **测试运行器改进**：新增 `--only-changed`、`--fail-on-flaky-tests`、`--last-failed` 等 CLI 选项，以及 `test.step.skip()`、`test.fail.only()` 等方法。
- 🔒 **TLS 客户端证书**：支持通过 `clientCertificates` 选项提供客户端证书。
- 🕰️ **时钟 API**：新增 `page.clock` API，允许在测试中操纵和控制时间。
- 🧩 **组件测试**：支持 React 和 Vue 组件测试，新增 `router` fixture 用于拦截网络请求。
- 🛠️ **其他改进**：支持 Ubuntu 26.04/24.04，移除对旧版 macOS 和 Node.js 的支持，弃用并移除了一些旧 API。

---

### [WebStorage | Playwright](https://playwright.dev/docs/api/class-webstorage)

**原文标题**: [WebStorage | Playwright](https://playwright.dev/docs/api/class-webstorage)

WebStorage 提供异步、浏览器一致的 API 来操作页面当前源的 localStorage 或 sessionStorage，可通过 page.localStorage 和 page.sessionStorage 访问。

- 🌐 **访问存储实例**：通过 `page.localStorage` 和 `page.sessionStorage` 获取存储对象。
- 📝 **设置项目**：使用 `setItem(name, value)` 存储键值对，若已存在则覆盖。
- 🔍 **获取项目**：使用 `getItem(name)` 返回指定名称的值，若不存在则返回 `null`。
- 📋 **列出所有项目**：使用 `items()` 返回所有键值对数组，包含 `name` 和 `value` 属性。
- ❌ **删除项目**：使用 `removeItem(name)` 移除指定项，若不存在则不执行任何操作。
- 🧹 **清空存储**：使用 `clear()` 移除所有存储项目。

---

### [ESLint v10.5.0 发布 - ESLint - 可插拔的 JavaScript 代码检查工具](https://eslint.org/blog/2026/06/eslint-v10.5.0-released/)

**原文标题**: [ESLint v10.5.0 released - ESLint - Pluggable JavaScript Linter](https://eslint.org/blog/2026/06/eslint-v10.5.0-released/)

ESLint v10.5.0 发布，这是一个次要版本升级，新增了一些功能并修复了多个错误。

- 🎯 五个核心规则现在高亮更小的代码范围，避免在编辑器中遮蔽其他问题
- 📏 `max-lines-per-function`、`max-nested-callbacks` 和 `max-statements` 规则仅高亮函数头部而非整个函数
- 🔍 `max-depth` 和 `no-with` 规则现在仅高亮第一个关键字
- 🐛 修复了 `max-depth` 和 `max-nested-callbacks` 规则中的计算错误，可能导致现有代码报告更多 lint 错误
- ✨ 新增功能：改进堆栈跟踪、在关键字处报告违规、修正 `else-if` 链处理等
- 📚 更新文档，包括 Node.js 先决条件（ICU 支持）和 parserOptions 优先级说明
- 🔧 杂项改进：更新生态系统插件、重构代码、增强配置规则支持、添加单元测试等

---

### [发布 v1.18.0 · axios/axios · GitHub](https://github.com/axios/axios/releases/tag/v1.18.0)

**原文标题**: [Release v1.18.0 · axios/axios · GitHub](https://github.com/axios/axios/releases/tag/v1.18.0)

axios v1.18.0 版本发布，重点强化了安全防护、修复了状态验证逻辑，并更新了依赖与文档。
- 🔒 安全增强：Node HTTP 适配器现在会在跨域重定向时剥离调用方指定的敏感请求头（如 API 密钥），防止信息泄露；同时拒绝缺少 `//` 的畸形 `http:` 和 `https:` URL，并加强原型污染防护、流大小限制、FormData 深度处理、数据 URL 大小限制和本地 `NO_PROXY` 匹配。
- 🐛 错误修复：新增 `transitional.validateStatusUndefinedResolves` 配置，允许应用将 `validateStatus: undefined` 视为未设置该选项（与 `validateStatus: null` 显式接受所有状态码区分）。
- 🔧 维护与杂项：更新了 v1.17.0 发布说明、修复了更新日志中的拼写错误、明确了包更新 PR 策略，并在高级文档中标记 `proxy` 请求配置仅适用于 Node.js；升级了多个开发依赖（如 `@babel/core`、`eslint`、`rollup`、`vitest` 等）以及 GitHub Actions 的 `actions/checkout`。
- 🌟 新贡献者：欢迎 `drori12`、`eyupcanakman` 和 `Adi-Beker` 首次为 axios 做出贡献。

---

### [GitHub - nodejs/node-gyp: Node.js 原生插件构建工具](https://github.com/nodejs/node-gyp)

**原文标题**: [GitHub - nodejs/node-gyp: Node.js native addon build tool · GitHub](https://github.com/nodejs/node-gyp)

node-gyp 是一个跨平台命令行工具，用于编译 Node.js 原生附加模块，支持所有当前和长期支持的 Node.js 版本，并包含 gyp-next 的副本。

- 🛠️ **核心功能**：跨平台编译 Node.js 原生附加模块，支持不同 Node.js 版本
- 📦 **安装方式**：通过 `npm install -g node-gyp` 全局安装，需依赖 Python、make 和 C++ 编译器
- 💻 **平台依赖**：Unix 需 GCC，macOS 需 Xcode 命令行工具，Windows 需 Visual Studio 和 Python
- ⚙️ **配置 Python**：可通过 `--python` 参数、`npm_config_python` 环境变量或 `PYTHON` 变量指定 Python 版本
- 🎯 **第三方运行时**：支持 Electron 等运行时，使用 `--dist-url` 或 `--nodedir` 指定头文件
- 📝 **使用流程**：`node-gyp configure` 生成构建文件，`node-gyp build` 编译，生成 `.node` 绑定文件
- 📄 **binding.gyp 文件**：JSON 格式配置文件，描述模块构建配置，包含目标名称和源文件
- 🔧 **命令列表**：包括 help、build、clean、configure、rebuild、install、list、remove 等
- 🎛️ **命令选项**：支持并行构建、目标版本、日志级别、调试模式、架构设置等
- 📋 **配置方式**：可通过 package.json 的 `config` 对象、环境变量或 npm 配置设置选项
- 📜 **许可证**：MIT 许可证，开源社区支持

---

### [GitHub - graphql/graphql-js: GraphQL 的 JavaScript 参考实现](https://github.com/graphql/graphql-js)

**原文标题**: [GitHub - graphql/graphql-js: A reference implementation of GraphQL for JavaScript · GitHub](https://github.com/graphql/graphql-js)

GraphQL.js 是 GraphQL 查询语言的 JavaScript 官方参考实现，由 Facebook 创建，提供构建类型模式和查询服务的能力。

- 🌟 拥有 20.4k 星标和 2k 分支，是社区广泛使用的开源项目
- 📦 支持通过 npm、yarn、bun 安装，并兼容 CommonJS 和 ESModule
- 🛠️ 核心功能：构建类型模式（如 GraphQLSchema）和执行查询（如 graphql 函数）
- 🌐 可在 Node 服务器和浏览器中使用，例如 GraphiQL 工具
- 🤝 欢迎贡献，需签署 GraphQL 规范会员协议
- 📜 遵循语义化版本，支持最新主版本和上一主版本（12 个月），无长期支持
- 🔒 优先处理安全更新，覆盖当前和上一主版本
- 🗓️ 主版本结束生命周期前至少 6 个月通知
- 💬 提供社区论坛（Discord）和迁移指南协助升级

---

### [GitHub - faker-js/faker：在浏览器和Node.js中生成海量假数据 · GitHub](https://github.com/faker-js/faker)

**原文标题**: [GitHub - faker-js/faker: Generate massive amounts of fake data in the browser and node.js · GitHub](https://github.com/faker-js/faker)

Faker 是一个用于生成大量逼真测试数据的开源工具库，支持浏览器和 Node.js 环境，拥有丰富的模块和 70 多种语言本地化支持。

- 🧍 **人物数据** - 生成姓名、性别、个人简介、职位等个人信息
- 📍 **位置数据** - 生成地址、邮编、街道名、州和国家
- ⏰ **日期数据** - 生成过去、现在、未来、近期等各类时间
- 💸 **财务数据** - 创建账户详情、交易记录和加密货币地址
- 👠 **商业数据** - 生成价格、产品名、形容词和描述
- 👾 **黑客风格** - 生成技术相关的随机语句
- 🔢 **数字与字符串** - 生成随机数字和字符串
- 🌏 **多语言支持** - 支持超过 70 种语言本地化
- 📦 **安装简单** - 通过 npm 安装 `@faker-js/faker`
- 🎲 **种子随机** - 支持设置种子值以获得可重复的结果
- 🤝 **开源社区** - MIT 许可证，由赞助商和贡献者支持

---

### [发布 23.0.0 · nrwl/nx · GitHub](https://github.com/nrwl/nx/releases/tag/23.0.0)

**原文标题**: [Release 23.0.0 · nrwl/nx · GitHub](https://github.com/nrwl/nx/releases/tag/23.0.0)

Nx 23.0.0 版本发布，包含大量新功能、问题修复和破坏性变更。

- 🚀 核心功能：新增 `--mode` 和 `--multi-major-mode` 标志，支持 shell 标签补全，以及智能迁移模式
- ⚠️ 破坏性变更：移除多个 Angular 弃用功能（如 `@nx/angular/module-federation` 入口点、`ngrx` 生成器、`move` 生成器）
- 🗑️ 移除功能：删除 Tailwind CSS `setup-tailwind` 生成器、弃用的样式表选项、`initTasksRunner` API 及 `self`/`dependencies` 魔法字符串
- 🛠️ 修复：大量问题修复，包括 Angular、打包、核心、检测、Gradle、JS、测试等多个模块
- 📦 多版本支持：确保 `@nx/detox`、`@nx/expo`、`@nx/react-native` 和 `@nx/remix` 的兼容性
- 🧪 测试改进：弃用 `@nx/cypress:cypress` 执行器，添加 Jest 30 快照指南链接迁移
- 🔄 迁移增强：支持 `prompt` 字段、`--trustThirdPartyPreset` 标志，以及 JSON schema 验证
- 🧹 清理工作：移除 v21 之前的迁移，优化代码库并修复多个安全漏洞（如 CVE-2026-44705）
- 📚 文档更新：添加 AI 仓库会议顶部横幅，跟踪代码复制和 LLM 提示的分析数据

---

### [GitHub - mongodb/js-bson: 适用于 Node 和浏览器的 BSON 解析器](https://github.com/mongodb/js-bson)

**原文标题**: [GitHub - mongodb/js-bson: BSON Parser for node and browser · GitHub](https://github.com/mongodb/js-bson)

BSON（Binary JSON）是 JSON 文档的二进制编码序列化格式，用于 Node.js 和浏览器的 BSON 解析器，支持多种版本兼容性和安全验证。

- 📦 **核心功能**：BSON 是 JSON 的二进制序列化格式，支持在 Node.js 和浏览器中解析和生成 BSON 数据
- 🔒 **发布完整性**：所有版本都使用 GPG 密钥签名，可通过 npm audit 验证来源和构建工作流
- 🐛 **问题反馈**：通过 MongoDB JIRA 系统提交 bug 或功能请求，NODE 项目公开可见
- 🚀 **使用方式**：支持 npm 安装，可通过 import 或 require 引入 BSON、EJSON、ObjectId 等模块
- 🌐 **浏览器支持**：可直接使用.mjs bundle，无需打包工具
- 📊 **版本兼容**：bson@7.x 与 mongodb@7.x 稳定兼容，其他版本有明确对应关系
- 📚 **文档丰富**：提供 EJSON 的 parse、stringify、serialize、deserialize 等完整 API 文档
- ⚠️ **错误处理**：推荐使用 BSONError.isBSONError() 检查错误，避免依赖错误消息字符串
- 📱 **React Native 支持**：需要 atob、btoa、TextEncoder 全局对象，推荐安装 crypto.getRandomValues
- ❓ **常见问题**：undefined 会转为 null，支持通过 toBSON() 函数自定义序列化逻辑

---

