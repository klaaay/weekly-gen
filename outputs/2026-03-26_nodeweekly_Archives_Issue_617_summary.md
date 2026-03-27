### [错误](https://nodeweekly.com/link/182808/web)

**原文标题**: [Error](https://nodeweekly.com/link/182808/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='nodeweekly.com', port=443): Max retries exceeded with url: /link/182808/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1000)')))

---

### [TypeScript 6.0 发布公告 - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-6-0/)

**原文标题**: [Announcing TypeScript 6.0 - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-6-0/)

TypeScript 6.0 正式发布，这是一个独特的过渡版本，旨在为基于 Go 重写的原生 TypeScript 7.0 铺平道路。此版本包含多项新特性、改进以及为迎接 7.0 所做的重大变更和弃用，包括默认配置的更新、模块解析的调整以及对现代 JavaScript 特性的支持。

- 🚀 **发布与定位**：TypeScript 6.0 是当前 JavaScript 代码库的最后一个主要版本，作为 5.9 与即将到来的原生 7.0 版本之间的桥梁。
- 🧠 **类型推断优化**：对不含 `this` 使用的方法减少了上下文敏感性，提升了在泛型调用中类型推断的准确性。
- 📁 **子路径导入支持**：现在支持以 `#/` 开头的子路径导入，与 Node.js 的新特性保持一致，简化了项目内部的模块别名配置。
- ⚙️ **模块解析组合**：允许将 `--moduleResolution bundler` 与 `--module commonjs` 组合使用，为许多项目提供了更合适的升级路径。
- 🔢 **稳定的类型排序**：引入了 `--stableTypeOrdering` 标志，使 6.0 的类型排序行为与 7.0 保持一致，便于版本迁移对比，但可能会带来性能开销。
- 🎯 **新的编译目标**：增加了 `es2025` 作为 `target` 和 `lib` 的选项，并引入了新的内置 API 类型。
- ⏳ **Temporal API 类型**：为已达到 Stage 4 的 Temporal API 提供了内置类型支持，可用于处理日期和时间。
- 🗺️ **Map 新增方法**：为 `Map` 和 `WeakMap` 添加了 `getOrInsert` 和 `getOrInsertComputed` 方法，简化了“检查 - 插入 - 获取”模式。
- 🛡️ **RegExp.escape**：新增 `RegExp.escape` 函数，用于安全地转义正则表达式中的特殊字符。
- 🌐 **DOM 库更新**：`dom` 库现在默认包含 `dom.iterable` 和 `dom.asynciterable` 的内容，简化了配置。
- ⚠️ **重大变更与弃用**：包含多项默认值变更（如 `strict` 默认为 `true`，`module` 默认为 `esnext`）和功能弃用（如弃用 `target: es5`、`--moduleResolution node`、`--baseUrl`、`--outFile` 等），旨在使 TypeScript 更符合现代开发实践并为 7.0 做准备。
- 🛠️ **迁移准备**：强调 TypeScript 6.0 是一个过渡版本，建议开发者解决所有弃用警告，并尝试 TypeScript 7.0 的原生预览版，以便顺利迁移。

---

### [Node.js — 2026 年 3 月 24 日星期二安全版本发布](https://nodejs.org/en/blog/vulnerability/march-2026-security-releases)

**原文标题**: [Node.js — Tuesday, March 24, 2026 Security Releases](https://nodejs.org/en/blog/vulnerability/march-2026-security-releases)

Node.js 项目于 2026 年 3 月 24 日发布了针对多个版本的安全更新，修复了包括高、中、低严重性在内的多个安全漏洞，并提供了相应的修复版本下载。

- 🛡️ **安全更新发布**：Node.js 为 25.x、24.x、22.x、20.x 版本发布了安全更新，修复了多个安全漏洞。
- ⚠️ **高严重性漏洞**：包括 TLS SNI 回调未捕获异常导致远程拒绝服务（CVE-2026-21637）和 HTTP 头部 `__proto__` 导致进程崩溃（CVE-2026-21710）。
- ⚠️ **中严重性漏洞**：涉及权限模型绕过、URL 解析崩溃、HMAC 验证时序侧信道、HTTP/2 内存泄漏和 V8 HashDoS 攻击。
- ⚠️ **低严重性漏洞**：包括权限模型中的文件存在泄露和文件权限修改绕过问题。
- 📥 **更新版本**：提供了 Node.js v20.20.2、v22.22.2、v24.14.1、v25.8.2 等修复版本的下载链接。
- 📅 **发布计划**：安全更新于 2026 年 3 月 24 日或之后发布，建议用户及时更新以确保系统安全。
- 📢 **安全联系**：用户可通过 Node.js 安全政策页面和 GitHub 安全流程报告漏洞，或订阅安全邮件列表获取更新。

---

### [Node.js — Node.js 25.8.2（当前版本）](https://nodejs.org/en/blog/release/v25.8.2)

**原文标题**: [Node.js — Node.js 25.8.2 (Current)](https://nodejs.org/en/blog/release/v25.8.2)

Node.js 25.8.2 是一个安全版本，主要修复了多个安全漏洞，包括高、中、低不同严重级别的 CVE 问题，并更新了依赖项。

- 🛡️ 修复了两个高危安全漏洞：CVE-2026-21637（包装 SNICallback 调用）和 CVE-2026-21710（为 headersDistinct/trailersDistinct 使用 null 原型）
- 🔧 修复了五个中危安全漏洞，涉及权限检查、URL 格式处理、加密比较和 HTTP/2 错误处理
- 📝 修复了两个低危安全漏洞，均与文件系统操作的权限检查相关
- 🔄 更新了多个依赖项，包括 undici 到 7.24.4、npm 到 11.11.1，并调整了 V8 的 depot_tools 版本
- 📦 提供了 Windows、macOS、Linux、AIX 等多种操作系统和架构的安装包与二进制文件下载链接

---

### [Node.js — Node.js 24.14.1（长期支持版）](https://nodejs.org/en/blog/release/v24.14.1)

**原文标题**: [Node.js — Node.js 24.14.1 (LTS)](https://nodejs.org/en/blog/release/v24.14.1)

Node.js 24.14.1（LTS）版本发布，代号“Krypton”，这是一个安全更新版本，主要修复了多个安全漏洞并包含依赖项更新。

- 🔒 修复了多个安全漏洞，包括两个高危漏洞（CVE-2026-21710 和 CVE-2026-21637）
- 📦 更新了多个依赖项，包括 undici 升级至 7.24.4 和 npm 升级至 11.11.0
- 🛠️ 包含对 V8 引擎的多个补丁更新
- 📄 提供了 Windows、macOS、Linux 和 AIX 等多个平台的安装包和二进制文件
- 📋 包含完整的发布文件 SHA256 校验和及 PGP 签名

---

### [Node.js — Node.js 22.22.2（长期支持版）](https://nodejs.org/en/blog/release/v22.22.2)

**原文标题**: [Node.js — Node.js 22.22.2 (LTS)](https://nodejs.org/en/blog/release/v22.22.2)

Node.js 22.22.2（LTS）版本是一个安全更新，主要修复了多个安全漏洞，包括高、中、低风险级别的问题，并包含依赖项升级和其他改进。

- 🛡️ 修复了高风险的 CVE-2026-21637 漏洞，通过 try/catch 包装 SNICallback 调用以增强 TLS 安全性
- 🛡️ 修复了高风险的 CVE-2026-21710 漏洞，对 headersDistinct/trailersDistinct 使用 null 原型以防止原型污染
- 🛡️ 修复了中风险的 CVE-2026-21713 漏洞，在 Web Cryptography HMAC 中采用时序安全比较
- 🛡️ 修复了中风险的 CVE-2026-21714 漏洞，处理 NGHTTP2_ERR_FLOW_CONTROL 错误代码
- 🛡️ 修复了中风险的 CVE-2026-21717 漏洞，测试数组索引哈希碰撞问题
- 🔒 修复了低风险的 CVE-2026-21715 漏洞，为 realpath.native 添加权限检查
- 🔒 修复了低风险的 CVE-2026-21716 漏洞，在 lib/fs/promises 中包含权限检查
- 📦 升级了 npm 到 10.9.7 版本，并更新了 undici 到 v6.24.1
- 🔧 包含了多个 V8 引擎的补丁和依赖项更新，提升了整体稳定性和安全性
- 🌐 提供了 Windows、macOS、Linux 等多种操作系统的安装包和二进制文件下载链接

---

### [Node.js — Node.js 20.20.2（长期支持版）](https://nodejs.org/en/blog/release/v20.20.2)

**原文标题**: [Node.js — Node.js 20.20.2 (LTS)](https://nodejs.org/en/blog/release/v20.20.2)

Node.js 20.20.2（LTS）版本发布，代号“Iron”，这是一个安全更新版本，主要修复了多个安全漏洞，并包含一些依赖项更新。

- 🔒 修复了数组索引哈希碰撞漏洞（CVE-2026-21717）
- ⏱️ 在 Web 加密的 HMAC 和 KMAC 中采用时序安全比较（CVE-2026-21713）
- 🛡️ 为 headersDistinct/trailersDistinct 使用 null 原型（CVE-2026-21710）
- 📁 在 lib/fs/promises 中添加权限检查（CVE-2026-21716）
- 🔍 为 realpath.native 添加权限检查（CVE-2026-21715）
- 🌐 处理 NGHTTP2_ERR_FLOW_CONTROL 错误代码（CVE-2026-21714）
- 🚧 在 SNICallback 调用中包装 try/catch（CVE-2026-21637）
- 📦 更新了 undici 依赖至 v6.24.1 版本
- 💾 提供了 Windows、macOS、Linux 等多平台的安装包和二进制文件下载

---

### [Node.js — 为 V8 开发一种最小化 HashDoS 抵抗且快速可逆的整数哈希算法](https://nodejs.org/en/blog/vulnerability/march-2026-hashdos)

**原文标题**: [Node.js — Developing a minimally HashDoS resistant, yet quickly reversible integer hash for V8](https://nodejs.org/en/blog/vulnerability/march-2026-hashdos)

本文介绍了为应对 CVE-2026-21717 漏洞，在 V8 中开发一种既具备最小 HashDoS 抵抗能力又能快速逆向的整数哈希方案的过程。该方案通过结合随机密钥的异或移位和乘法运算，在保证哈希值不可预测以防止攻击者触发严重性能退化的同时，保持了可逆性以支持 V8 的关键性能优化。

- 🔐 **HashDoS 攻击与缓解**：哈希表碰撞可导致服务拒绝攻击，Node.js/V8 通过引入随机种子哈希来防御，但数组索引字符串此前使用确定性哈希，易受攻击。
- 🧩 **哈希方案设计挑战**：需平衡安全性与性能，新哈希必须在抵抗攻击的同时可逆，以维持 V8 内部优化（如快速字符串转整数）。
- 🔄 **可逆哈希结构**：采用基于异或移位和乘法的可逆结构（xorshift-multiply），利用随机生成的乘法器实现位扩散，确保哈希不可预测且可高效逆向。
- 📊 **统计评估与优化**：通过雪崩效应测试评估哈希质量，最终采用三轮异或移位 - 乘法结构，显著提升扩散稳定性，偏差均值降至 0.50。
- ⚙️ **实现与性能**：在 V8 中整合新哈希方案，优化秘密访问对齐，性能测试显示影响可忽略（基准测试变化在±0.2% 内），已部署至 Node.js LTS 版本。

---

### [碰撞攻击 - 维基百科](https://en.wikipedia.org/wiki/Collision_attack#Hash_flooding)

**原文标题**: [Collision attack - Wikipedia](https://en.wikipedia.org/wiki/Collision_attack#Hash_flooding)

碰撞攻击是一种针对密码哈希函数的攻击方式，旨在找到两个不同的输入产生相同的哈希值。与针对特定哈希值的原像攻击不同，碰撞攻击关注于发现任意两个具有相同哈希的输入。攻击主要分为经典碰撞攻击和选择前缀碰撞攻击，前者寻找两个完全不同的消息，后者允许攻击者指定两个不同的前缀并找到对应的后缀使哈希一致。由于生日攻击的存在，攻击速度远快于暴力破解。历史上，MD5 和 SHA-1 等常用哈希函数因此类攻击而被认为不安全，可能被用于伪造数字签名、证书等，威胁网络安全。尽管部分应用（如 HMAC）不受影响，但哈希碰撞在数字签名和哈希洪水攻击等场景中具有实际风险。

- 🔍 碰撞攻击旨在发现两个不同输入产生相同哈希值，区别于针对特定哈希的原像攻击
- ⚔️ 主要分为经典碰撞攻击和选择前缀碰撞攻击，后者攻击更复杂但威力更大
- 🎂 生日攻击使碰撞发现速度远快于暴力破解，n 位哈希可在约 2^(n/2) 次操作内破解
- ⚠️ MD5 和 SHA-1 等算法因高效碰撞攻击而被认为不安全，MD5 碰撞可在数秒内生成
- 📄 攻击可通过文件格式的动态构造（如条件语句、裁剪图像）实现恶意文档伪造
- 📜 选择前缀碰撞曾用于伪造 X.509 证书，冒充证书颁发机构，威胁 SSL/TLS 安全
- 🔐 数字签名易受哈希碰撞影响，攻击者可替换文档内容而保持签名有效
- 🌊 哈希洪水攻击利用碰撞触发哈希表最坏情况性能，进行拒绝服务攻击
- 🛡️ 部分应用（如 HMAC）不依赖抗碰撞性，因此不受此类攻击影响

---

### [JWT 格式对 M2M 令牌的支持](https://clerk.com/changelog/2026-02-24-m2m-jwt-tokens?utm_source=cooper_press&utm_medium=newsletter&utm_campaign=jwt-m2m&utm_content=03-26-26&dub_id=wAfGEfiZ4fSE804T)

**原文标题**: [JWT format support for M2M tokens](https://clerk.com/changelog/2026-02-24-m2m-jwt-tokens?utm_source=cooper_press&utm_medium=newsletter&utm_campaign=jwt-m2m&utm_content=03-26-26&dub_id=wAfGEfiZ4fSE804T)

Clerk 现已支持将 M2M 令牌以 JWT 格式签发，实现无网络验证并消除每次验证成本。

- 🔑 **JWT 格式优势**：支持本地验证，无需请求 Clerk 服务器，降低延迟且无验证费用
- 🛡️ **不透明令牌适用场景**：适用于需要即时撤销或最高安全性的敏感场景
- 📊 **启用方式**：可通过仪表板切换 JWT 格式，或使用 SDK 指定 tokenFormat: 'jwt'
- 💰 **定价调整**：自 2026 年 3 月 16 日起，令牌创建将收费 $0.001，不透明令牌验证收费 $0.00001

---

### [发布 pnpm 11 Beta 0 · pnpm/pnpm · GitHub](https://github.com/pnpm/pnpm/releases/tag/v11.0.0-beta.0)

**原文标题**: [Release pnpm 11 Beta 0 · pnpm/pnpm · GitHub](https://github.com/pnpm/pnpm/releases/tag/v11.0.0-beta.0)

pnpm 11 Beta 0 版本发布，引入了多项重大变更，包括存储优化、全局包隔离、配置格式调整、废弃功能移除及新命令添加，旨在提升性能、安全性和开发者体验。

- 🚀 存储优化：运行时依赖始终从全局虚拟存储链接，索引文件格式优化，使用 SQLite 存储包元数据以减少 I/O 开销。
- 🌍 全局包隔离：全局安装的包现在各自拥有独立的安装目录，防止包间冲突。
- ⚙️ 配置变更：默认配置值调整，配置输出格式改为 JSON，并移除了对非 camelCase 选项的支持。
- 🔗 锁文件简化：`patchedDependencies` 格式简化，自动迁移旧格式。
- 🗑️ 功能移除：移除了 `pnpm server` 命令、`useNodeVersion` 等已弃用功能，并默认启用 `strictDepBuilds` 和 `blockExoticSubdeps`。
- 📦 新命令：新增 `pnpm sbom` 生成软件物料清单、`pnpm clean` 清理工作区项目、`pnpm runtime set` 管理运行时环境。
- 🔧 配置增强：支持全局 YAML 配置文件、环境变量覆盖配置、`allowBuilds` 设置及 `virtualStoreOnly` 模式。
- 📝 钩子与 Pnpmfiles：支持 ESM 格式的 `.pnpmfile.mjs`，优先于 `.pnpmfile.cjs` 加载。
- 🛠️ 补丁与修复：改进了非 npm 托管包的安装检查、YAML 格式保留、补丁错误处理及 CI 中的锁文件兼容性检查。

---

### [Deno，下一代 JavaScript 运行时](https://deno.com/)

**原文标题**: [Deno, the next-generation JavaScript runtime](https://deno.com/)

Deno 是一个开源的现代 JavaScript 运行时，基于 Web 标准构建，内置 TypeScript 支持、强大的安全性和完整的工具链，旨在简化 JavaScript 开发。

- 🚀 **现代 JavaScript 运行时**：Deno 基于 Web 标准，提供零配置的 TypeScript、JSX 和现代 ECMAScript 功能支持，无需额外工具。
- 🔒 **默认安全**：程序默认无文件、网络或环境访问权限，需显式授权，防止供应链攻击。
- 🛠️ **内置工具链**：包含代码检查器、测试运行器、格式化器和独立可执行文件生成器，简化开发流程。
- 🌐 **Web 标准兼容**：实现大量 Web API，确保浏览器与服务器代码一致性，支持 TC39 和 WinterCG 标准。
- 📦 **Node.js 和 npm 兼容**：无缝支持 package.json 和直接 npm 包导入，便于现有项目迁移。
- ☁️ **云原生设计**：优化云部署，支持 Deno Deploy 等平台，提供高性能网络和容器化支持。
- ⚡ **高性能**：在基准测试中表现优于 Node.js，支持 HTTPS、WebSocket 和 HTTP/2。
- 🏝️ **框架生态**：内置 Fresh 框架，采用岛屿架构，减少 JavaScript 负载，提升渲染速度。
- 👥 **活跃社区**：拥有大量 GitHub 星标、用户和模块，受到开发者广泛好评。

---

### [@collinsworth.dev 在 Bluesky](https://bsky.app/profile/collinsworth.dev/post/3mhdpgmoao22j)

**原文标题**: [@collinsworth.dev on Bluesky](https://bsky.app/profile/collinsworth.dev/post/3mhdpgmoao22j)

Deno 公司因经济困难裁员，但 Deno 项目本身将继续运营，旨在澄清外界猜测并强调当前只是面临艰难时期。

- 🚀 Deno 项目持续发展，不受公司裁员影响
- 💼 裁员仅因残酷的商业现实，无其他原因
- 🌐 Bluesky 为高度交互式应用，需 JavaScript 支持
- 🔗 可通过 bsky.social 和 atproto.com 了解更多信息
- 📅 该声明发布于 2026 年 3 月 18 日

---

### [快速且低开销的 Node.js Web 框架 | Fastify](https://fastify.dev/)

**原文标题**: [Fast and low overhead web framework, for Node.js | Fastify](https://fastify.dev/)

Fastify 是一个高性能的 Node.js Web 框架，专注于提供最佳开发者体验和极低的开销，拥有强大的插件架构。它强调性能、可扩展性和安全性，支持 JSON Schema 验证、高效日志记录和 TypeScript，每月下载量超过 1000 万次，被众多组织广泛使用。

- 🚀 **高性能**：Fastify 是目前最快的 Web 框架之一，每秒可处理高达 3 万次请求。
- 🔌 **可扩展性**：通过钩子、插件和装饰器实现完全可扩展。
- 📝 **基于模式**：推荐使用 JSON Schema 验证路由和序列化输出，内部编译为高性能函数。
- 📊 **高效日志**：集成 Pino 日志库，几乎无性能损耗。
- 👨‍💻 **开发者友好**：设计注重表达性和易用性，同时不牺牲性能和安全。
- 💻 **TypeScript 支持**：提供完整的类型声明文件，支持 TypeScript 开发。
- 🌐 **广泛采用**：每月下载量超过 1000 万次，被众多公司和产品使用。
- 🛠️ **快速上手**：通过 npm 安装，简单几行代码即可创建服务器，支持 CLI 生成项目脚手架。
- 🔒 **验证与钩子**：支持请求/响应验证，可在处理程序执行前执行特定操作（如身份验证）。
- 📚 **丰富生态**：拥有不断增长的插件生态系统，涵盖数据库、模板语言等多种需求。

---

### [发布 · fastify/fastify · GitHub](https://github.com/fastify/fastify/releases)

**原文标题**: [Releases · fastify/fastify · GitHub](https://github.com/fastify/fastify/releases)

Fastify 项目近期发布了多个版本更新，主要涉及安全修复、性能优化、文档改进和新功能引入，社区贡献活跃。

- 🔒 **安全修复**：多个版本（如 v5.8.3、v5.8.1、v5.7.3）修复了安全漏洞，包括 CVE-2026-3635 和 CVE-2026-3419 等，增强了内容类型验证和请求处理的安全性。
- 📚 **文档完善**：更新了插件指南、安全威胁模型和性能优化建议，修复了示例代码和链接，提升了文档的准确性和可读性。
- 🚀 **性能提升**：引入了原生 WebStream API 支持、自定义编译器加速加载，并优化了路由选项和日志处理，提高了框架的整体性能。
- 👥 **社区贡献**：多个版本吸引了新贡献者加入，修复了类型定义、测试用例和代码示例，体现了活跃的社区协作。
- 🛠️ **功能增强**：新增了处理程序级超时支持、条件请求日志记录等特性，同时改进了错误处理和内容类型解析的严格性。

---

### [fastify：通过不可信连接的 X-Forwarded-Proto/Host 可伪造 request.protocol 和 request.host · CVE-2026-3635 · GitHub 咨询数据库 · GitHub](https://github.com/advisories/GHSA-444r-cwp2-x5xf)

**原文标题**: [fastify: request.protocol and request.host Spoofable via X-Forwarded-Proto/Host from Untrusted Connections · CVE-2026-3635 · GitHub Advisory Database · GitHub](https://github.com/advisories/GHSA-444r-cwp2-x5xf)

Fastify 框架在配置了限制性信任代理（如特定 IP、子网、跳数或自定义函数）时，存在一个安全漏洞，允许攻击者通过直接连接并伪造 X-Forwarded-Proto 和 X-Forwarded-Host 头部，欺骗应用程序识别的协议和主机信息，影响版本为 5.8.2 及以下，已修复于 5.8.3 版本。

- 🛡️ **漏洞概述**：当`trustProxy`配置为限制性信任函数时，`request.protocol`和`request.host`可能被来自不可信连接的伪造头部欺骗。
- ⚠️ **影响版本**：Fastify 版本≤5.8.2，已通过 5.8.3 版本修补。
- 🔒 **安全风险**：使用这些属性进行 HTTPS 强制、安全 Cookie 设置或 CSRF 检查的应用程序可能面临安全决策被绕过风险。
- 🌐 **攻击场景**：攻击者可直接连接 Fastify 服务器，绕过代理，伪造协议和主机信息。
- 📊 **严重程度**：中等（CVSS 评分 6.1），主要影响数据机密性，攻击复杂度较高。
- 🔗 **相关资源**：漏洞编号 CVE-2026-3635，详细信息可参考 GitHub Advisory 和 NVD 数据库。

---

### [400 MiB 去哪儿了？](https://frn.sh/pmem/)

**原文标题**: [Where did 400 MiB go?
](https://frn.sh/pmem/)

本文探讨了一个 Node.js WebSocket 应用在重启后，其中一个 Pod 内存异常翻倍至 640 MiB 的问题。通过分析发现，内存异常增长并非由 V8 堆内存直接导致，而是由 V8 未及时垃圾回收和 glibc 内存碎片共同引起。最终通过限制 V8 老生代堆大小和 glibc 内存区域数量，成功将内存降至正常水平。

- 🧠 **内存异常现象**：重启后一个 Pod 内存翻倍至 640 MiB，而其他 Pod 稳定在 330 MiB，表现为阶梯式增长而非缓慢上升。
- 🔍 **问题定位**：通过对比健康与异常 Pod，发现 412 MiB 差异全部来自 Node.js 进程的私有脏匿名内存，而非 V8 堆或外部缓冲区。
- 📊 **深入分析**：使用`smaps_rollup`和 V8 Inspector 检查，发现 V8 堆仅差 20 MiB，但 RSS 差 397 MiB，表明大量内存存在于 V8 之外。
- 🛠️ **根本原因**：V8 持有 252 MiB 可回收垃圾未及时清理，同时 glibc 内存碎片贡献约 70 MiB，两者共同导致内存滞留。
- ⚙️ **解决方案**：设置`MALLOC_ARENA_MAX=2`限制 glibc 内存区域，以及`--max-old-space-size=256`强制 V8 及时垃圾回收，成功将内存恢复至正常范围。

---

### [JavaScript 臃肿的三大支柱](https://43081j.com/2026/03/three-pillars-of-javascript-bloat)

**原文标题**: [The Three Pillars of JavaScript Bloat](https://43081j.com/2026/03/three-pillars-of-javascript-bloat)

本文探讨了 JavaScript 生态中依赖膨胀的三个主要原因：为支持老旧运行环境而引入的冗余代码、过度原子化的包设计以及长期未移除的“小马填充”库。这些因素导致现代项目中充斥着大量不必要的依赖，增加了维护成本和安全隐患。

- 🧓 **老旧环境兼容**：为支持 ES3 等过时引擎、防止全局命名空间污染或处理跨域值，许多包引入了本应由平台原生提供的功能，但绝大多数现代项目已无需这些兼容层。
- 🧩 **原子化架构过度**：将代码拆分为极细粒度的包（如`arrify`、`is-wsl`）本意是促进复用，却导致大量单次使用或重复的依赖，增加了供应链风险和维护负担。
- 🦄 **“小马填充”库滞留**：用于在不污染全局环境的前提下模拟未来 API 的库（如`object.entries`），在功能已被广泛支持后仍未被移除，造成无意义的依赖累积。

文章建议开发者主动审查依赖必要性，利用工具如`knip`清理未使用依赖、`e18e CLI`检测可替代模块，并通过`npmgraph`可视化依赖树来识别膨胀源头。社区项目如`module-replacements`提供了替代方案数据库，帮助迁移到更轻量的实现。最终目标是让仅少数人需要的兼容性方案独立存在，使主流项目能轻装上阵。

---

### [GitHub - sindresorhus/ponyfill: 🦄 如同 polyfill 但具备 pony 的纯粹性 · GitHub](https://github.com/sindresorhus/ponyfill)

**原文标题**: [GitHub - sindresorhus/ponyfill: 🦄 Like polyfill but with pony pureness · GitHub](https://github.com/sindresorhus/ponyfill)

本文介绍了 Ponyfill 的概念，它是一种不修改全局环境的标准化功能实现方式，与 Polyfill 不同，Ponyfill 通过显式导入提供功能，避免副作用，适用于 JavaScript、HTML 和 CSS 等场景。

- 🦄 Ponyfill 是一种不伪装成原生 API 的标准实现，通过显式导入提供功能，保持代码纯净
- 🐒 Polyfill 通过修改全局环境（如 Array.prototype）添加功能，可能导致兼容性和冲突问题
- ⚖️ Ponyfill 与 Polyfill 对比：前者不污染全局、不要求完全符合规范、无需后期移除且无副作用
- 💡 Ponyfill 适用于可控代码，而 Polyfill 可能在依赖链不支持时作为备选方案
- 🔧 创建 Ponyfill 需独立实现功能、避免依赖原生 API、进行测试并发布为独立模块
- 🌐 可通过 npm 搜索 Ponyfill 资源，相关讨论和定义可在 ponyfill.com 等平台找到

---

### [Knip v6 发布公告 | Knip](https://knip.dev/blog/knip-v6)

**原文标题**: [Announcing Knip v6 | Knip](https://knip.dev/blog/knip-v6)

Knip v6 发布，核心改进是彻底替换了 TypeScript 后端，转而采用 oxc-parser 和 oxc-resolver，从而大幅提升了性能。此次更新还包括性能调优、支持 TypeScript 命名空间，并引入了一些破坏性变更，如放弃对 Node.js v18 的支持和移除 `classMembers` 问题类型。整体上，Knip 在多个项目中的运行速度提升了 2-4 倍。

- 🚀 Knip v6 发布，完全用 oxc-parser 和 oxc-resolver 替换 TypeScript 后端，显著提升性能
- ⚡ 性能调优使运行速度在多个项目中提升 2-4 倍，部分插件改为静态分析配置文件
- 🆕 新增对 TypeScript 命名空间（和模块）的支持，引入新的问题类型 `namespaceMembers`
- ⚠️ 破坏性变更：放弃 Node.js v18 支持，移除 `classMembers` 问题类型，调整部分命令行选项和报告器行为
- 🔧 编辑器扩展受益于核心升级，更快速且内存效率更高，建议升级依赖中的 `knip`
- 📉 移除 `classMembers` 因依赖即将淘汰的 TypeScript API，用户可反馈以寻求替代方案
- 📦 升级指南：通过 `npm install -D knip@latest` 安装最新版本

---

### [错误](https://nodeweekly.com/link/182828/web)

**原文标题**: [Error](https://nodeweekly.com/link/182828/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='nodeweekly.com', port=443): Max retries exceeded with url: /link/182828/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1000)')))

---

### [错误](https://nodeweekly.com/link/182829/web)

**原文标题**: [Error](https://nodeweekly.com/link/182829/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='nodeweekly.com', port=443): Max retries exceeded with url: /link/182829/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1000)')))

---

### [TimescaleDB — 排名第一的时序数据库 | 泰格数据](https://www.tigerdata.com/timescaledb?utm_source=cooperpress&utm_medium=referral&utm_campaign=node-weekly-newsletter)

**原文标题**: [TimescaleDB — The #1 Time-Series Database | Tiger Data](https://www.tigerdata.com/timescaledb?utm_source=cooperpress&utm_medium=referral&utm_campaign=node-weekly-newsletter)

TimescaleDB 是一个基于 Postgres 构建的时序数据库，提供高性能时序数据处理、实时分析和事件管理，适用于初创公司和企业，具备开源特性与强大社区支持。

- 🚀 核心功能：自动分区（Hypertables）、行列混合存储、高达 95% 的数据压缩、增量物化视图、自动化管理及丰富的时序分析函数
- ⏱️ 时序优化：专为时序数据设计，支持快速写入与查询，兼容 PostgreSQL，实现生产级实时分析
- ☁️ 弹性云平台：提供 Tiger Cloud 云服务，适用于加密、能源遥测、油气运营等行业，具备企业级可扩展性
- 🛠️ 开源社区：拥有 22K+ GitHub 星标和 12,000+ Slack 成员，支持开发者贡献代码、讨论架构并参与路线图规划
- 📈 客户案例：被 Cloudflare、Replicated、orca.so 等企业采用，平衡了数据存储简便性与 OLAP 系统性能
- 🔧 部署便捷：支持 Helm 快速安装，提供免费试用和企业销售咨询，助力用户毫秒级查询数十亿行数据

---

### [JavaScript SQL 查询构建器 | Knex.js](https://knexjs.org/)

**原文标题**: [SQL Query Builder for Javascript | Knex.js](https://knexjs.org/)

本文概述了多种数据库系统及其相关资源。

- 🗄️ 支持多种数据库系统，包括 MySQL、MariaDB、PostgreSQL、CockroachDB、Amazon Redshift、SQLite3、OracleDB 和 MSSQL
- 🔍 提供搜索功能，方便用户快速查找信息
- 📚 包含主要导航、指南、博客、常见问题解答和更新日志等资源板块
- 🎨 允许用户自定义界面外观

---

### [Knex、花园与漫长的回归之路 | Knex.js](https://knexjs.org/blog/posts/2026-03-23-welcome/)

**原文标题**: [Knex, the Garden, and the Long Road Back | Knex.js](https://knexjs.org/blog/posts/2026-03-23-welcome/)

Knex 项目在经历一段低活跃期后，现已进入密集开发阶段，团队正着力清理积压问题、合并有价值的拉取请求，并计划修复所有已知缺陷，以巩固代码库的稳定性，为未来的功能改进奠定基础。

- 🗂️ 清理了 1079 个积压问题，通过分类、去重和 AI 摘要整理，明确了后续工作方向。
- 🔄 正在审查待处理的拉取请求，根据其状态和价值决定合并、关闭或转为议题。
- 🐛 下一步将优先修复标记为“缺陷”的问题，确保 Knex 的可靠性和稳定性。
- 🌐 改进了官方文档网站，新增了各数据库方言生成的真实 SQL 示例，提升了文档的实用性。
- 🛠️ 未来计划包括增强 TypeScript 支持、优化方言特定的查询生成、统一 API，并建立更清晰的长期维护机制。

---

### [GitHub - cyco130/vavite：使用Vite开发服务器端应用程序 · GitHub](https://github.com/cyco130/vavite)

**原文标题**: [GitHub - cyco130/vavite: Develop server-side applications with Vite · GitHub](https://github.com/cyco130/vavite)

vavite 是一个 Vite 插件，用于开发和构建服务器端应用，它利用 Vite 作为转译器/打包工具，简化了 SSR 工作流，并支持在开发和生产环境中统一处理服务器端代码的转译。

- 🚀 **核心功能**：vavite 让 Vite 能够转译服务器端代码，支持开发和生产环境的一致构建流程，无需额外工具如 ts-node 或 nodemon。
- 📁 **入口类型**：支持两种入口类型——处理器入口（`runnable-handler`）和服务器入口（`runnable-server`），分别适用于中间件集成和独立服务器场景。
- ⚙️ **配置灵活**：通过 `entries` 选项可配置多个入口，并利用 `order` 属性（`pre` 或 `post`）控制请求处理顺序，适应服务器专用或 SSR 设置。
- 🔄 **热重载支持**：内置 HMR 功能，允许在开发时热更新服务器代码，并提供资源清理和配置重用的模式。
- 🛠️ **环境信息**：通过 `import.meta.env` 提供环境变量（如 `COMMAND` 和 `ENVIRONMENT`），并可访问 Vite 开发服务器实例。
- 📚 **丰富示例**：提供多种框架集成示例（如 Express、Fastify、Koa、Nest.js）和 SSR 设置，帮助快速上手。
- 🔄 **迁移指南**：v6 版本完全重写，基于 Vite 7 和 Node 20+，移除了旧包和配置选项，需调整代码以适应新 API。
- 🌐 **开源活跃**：项目在 GitHub 上开源，拥有 507 星标和 15 个分支，采用 MIT 许可证，社区贡献活跃。

---

### [GitHub - fb55/htmlparser2：快速且容错的HTML与XML解析器 · GitHub](https://github.com/fb55/htmlparser2)

**原文标题**: [GitHub - fb55/htmlparser2: The fast & forgiving HTML and XML parser · GitHub](https://github.com/fb55/htmlparser2)

htmlparser2 是一个快速且容错性强的 HTML/XML 解析器，适用于 JavaScript 环境，提供回调接口和 DOM 构建功能，支持流式处理和多种解析选项。

- 🚀 **快速解析**：作为最快的 HTML 解析器之一，通过优化实现高性能，适合处理大量数据。
- 🔧 **灵活用法**：提供回调接口用于事件驱动解析，也支持通过 `parseDocument` 获取完整的 DOM 树。
- 🌐 **生态系统丰富**：与 `domhandler`、`domutils`、`css-select`、`cheerio` 等库集成，便于 DOM 操作和查询。
- ⚙️ **可配置选项**：支持 XML 模式、实体解码、标签大小写控制等，适应不同解析需求。
- 📊 **性能优异**：在真实场景的基准测试中表现领先，解析速度优于多数同类工具。
- 🔒 **安全支持**：通过 Tidelift 提供安全漏洞报告和协调修复，确保项目安全性。
- 📦 **广泛使用**：被超过 1850 万个项目使用，拥有活跃的社区和持续的版本发布。

---

### [AST 浏览器](https://astexplorer.net/#/2AmVrGuGVJ)

**原文标题**: [AST explorer](https://astexplorer.net/#/2AmVrGuGVJ)

该网站是一个基于现代前端技术栈构建的在线代码编辑器或开发工具。

- 🛠️ 使用 React、Babel、Font Awesome、CodeMirror、Express 和 webpack 等技术构建
- 🔗 项目托管在 GitHub 上
- 🔢 当前构建版本号为 8888701

---

### [发布 · denoland/deno · GitHub](https://github.com/denoland/deno/releases)

**原文标题**: [Releases · denoland/deno · GitHub](https://github.com/denoland/deno/releases)

Deno 2.7.8 版本发布，主要包含多项功能增强、错误修复和性能优化，涉及核心模块、Node.js 兼容性、加密、OpenTelemetry 集成等多个方面。

- 🚀 核心模块新增 NodeRuntime CDP 域支持，并修复了 `--inspect-brk` 阻塞问题
- 🔐 加密扩展实现了 P-521 签名、验证和 ECDH 密钥派生功能
- 🔧 Node-API 扩展新增 `node_api_create_object_with_named_properties` 方法
- 📊 OpenTelemetry 扩展新增控制台导出器，并将相关跨度属性复制到 HTTP 指标中
- 📦 全局安装时使用 JSR 包的锁文件
- 🐛 修复了多项 Node.js 兼容性问题，包括子进程、文件系统、TLS、HTTP/2、Buffer 等模块
- 🛡️ 审计功能现在在漏洞检查中尊重 package.json 的覆盖设置
- 🖥️ 修复了 Windows 上交互式选择器中箭头键的问题
- ⚡ 多项性能优化，包括使用 SIMD 加速 Base64 编解码、升级 jsonc-parser 等
- 🌐 Web 扩展修复了 AbortSignal.any() 内存泄漏和事件监听器选项处理问题
- 🔄 格式化工具更新了 markup_fmt 和 malva 版本，并修复了组件表达式格式化问题

---

### [GitHub - pnpm/action-setup：安装 pnpm 包管理器 · GitHub](https://github.com/pnpm/action-setup)

**原文标题**: [GitHub - pnpm/action-setup: Install pnpm package manager · GitHub](https://github.com/pnpm/action-setup)

这是一个用于在 GitHub Actions 工作流中安装和设置 pnpm 包管理器的官方 GitHub Action。它支持指定版本、自动安装依赖、缓存优化以及独立安装模式，以提升 CI/CD 流程的效率。

- 📦 **安装 pnpm**：在 GitHub Actions 中自动安装 pnpm 包管理器，支持通过 `version` 输入指定版本或从 `package.json` 的 `packageManager` 字段读取。
- ⚙️ **灵活配置**：提供多个输入选项，如 `run_install` 控制是否运行 `pnpm install`，`cache` 启用存储目录缓存以加速安装，以及 `standalone` 模式支持无需 Node.js 环境运行。
- 🔄 **依赖安装与缓存**：可配置递归安装、工作目录和额外参数；通过缓存 `pnpm-lock.yaml` 文件内容哈希来减少重复安装时间，自动处理存储清理。
- 📚 **使用示例丰富**：文档包含多种常见使用场景的示例，如仅安装 pnpm、结合 `packageManager` 字段安装、安装全局包及启用缓存优化工作流。
- ⚠️ **升级提示**：强调需从 v2 升级到最新版本以兼容新 Node.js 版本，避免因旧版不兼容导致的工作流错误。

---

### [快速、节省磁盘空间的包管理器 | pnpm](https://pnpm.io/)

**原文标题**: [Fast, disk space efficient package manager | pnpm](https://pnpm.io/)

pnpm 是一款高效、安全的 Node.js 包管理器，专注于提升安装速度、节省磁盘空间并优化 monorepo 管理，同时通过创新设计增强依赖管理的安全性和开发者体验。

- 🚀 安装速度极快，优化等待时间，提升开发效率
- 💾 高效节省磁盘空间，通过共享依赖减少存储占用
- 🏢 内置 monorepo 支持，优化多包项目管理流程
- 🔒 增强安全性，减少供应链攻击风险，支持延迟更新新版本
- ⏱️ 内置并行任务处理，显著缩短 CI/CD 构建时间
- 🌟 受到众多知名开源项目（如 Next.js、Vue、Vite 等）的广泛采用
- 💬 社区反馈积极，用户体验显著提升，安装和依赖解析更可靠

---

### [发布 pnpm 10.33 · pnpm/pnpm · GitHub](https://github.com/pnpm/pnpm/releases/tag/v10.33.0)

**原文标题**: [Release pnpm 10.33 · pnpm/pnpm · GitHub](https://github.com/pnpm/pnpm/releases/tag/v10.33.0)

pnpm 发布了 10.33.0 版本，引入了新的 `dedupePeers` 设置以减少对等依赖的重复，并修复了多项问题，包括 CI 环境下的锁定文件处理、并发 `pnpm dlx` 调用、Windows 路径解析及缓存清除功能等。

- 🆕 新增 `dedupePeers` 设置，通过简化对等依赖标识符显著减少包实例数量
- 🔧 修复了在 CI 中启用冻结锁定文件模式时对不兼容锁文件的处理
- 🐛 改进了包元数据获取失败时的错误信息显示
- ⚡ 解决了并发 `pnpm dlx` 调用时的间歇性故障问题
- 🪟 增强了 Windows 上二进制文件创建时的权限容错处理
- 🔄 修正了 `hoistPeers` 中非字符串版本选择器的处理逻辑
- 💡 为非交互式模块清理错误添加了 `confirmModulesPurge=false` 的解决提示
- 🛠️ 修复了 Windows 上因命令非零退出码导致的“命令未找到”误报
- 📄 改进了对包含双文档的 `pnpm-lock.yaml` 文件的兼容性处理
- 🧹 解决了 `createNpmResolver` 返回的 `clearCache` 函数无法正确清除元数据缓存的问题

---

### [发布 v10.4.0 · faker-js/faker · GitHub](https://github.com/faker-js/faker/releases/tag/v10.4.0)

**原文标题**: [Release v10.4.0 · faker-js/faker · GitHub](https://github.com/faker-js/faker/releases/tag/v10.4.0)

Faker.js 项目发布了 v10.4.0 版本，主要更新包括新增多语言本地化内容、修复已知问题、依赖项更新及文档改进，并迎来了三位新贡献者。

- 🌍 新增挪威语国家定义、日语动物品种定义及芬兰语电话号码支持
- 🔧 修复了西班牙语墨西哥地区街道名称的拼写和大小写错误
- 📚 重构了文档代码逻辑并迁移至新版 Vitepress
- ⬆️ 更新了多个开发和生产依赖项至最新版本
- 👋 三位新贡献者首次提交了代码合并请求

---

### [GitHub - websockets/ws: Node.js 的简单易用、速度极快且经过全面测试的 WebSocket 客户端和服务器 · GitHub](https://github.com/websockets/ws)

**原文标题**: [GitHub - websockets/ws: Simple to use, blazing fast and thoroughly tested WebSocket client and server for Node.js · GitHub](https://github.com/websockets/ws)

ws 是一个用于 Node.js 的 WebSocket 库，提供简单易用、性能优异且经过全面测试的客户端和服务器实现，支持多种 WebSocket 协议版本，并包含压缩、身份验证等高级功能。

- 🚀 **高性能实现**：经过 Autobahn 测试套件验证，支持 WebSocket 协议的多个草案版本。
- 📦 **安装与优化**：通过 npm 安装，可选择性添加 bufferutil 和 utf-8-validate 模块以提升性能。
- 🔧 **压缩支持**：默认在客户端启用 permessage-deflate 扩展，服务器端需手动配置，但需注意性能影响。
- 📖 **丰富文档**：提供详细的 API 文档和多种使用示例，包括发送文本/二进制数据、服务器广播等。
- 🛡️ **安全与认证**：支持客户端身份验证，并提供代理连接和心跳检测机制以维护连接稳定性。
- 🌐 **多场景应用**：可创建独立服务器、与外部 HTTP/S 服务器集成，或实现多服务器共享同一 HTTP/S 服务器。
- ❓ **常见问题解答**：涵盖如何获取客户端 IP、检测断开连接及通过代理连接等实用解决方案。

---

### [发布 v6.33.0 · openai/openai-node · GitHub](https://github.com/openai/openai-node/releases/tag/v6.33.0)

**原文标题**: [Release v6.33.0 · openai/openai-node · GitHub](https://github.com/openai/openai-node/releases/tag/v6.33.0)

OpenAI Node.js 客户端库发布了 v6.33.0 版本，包含新功能、错误修复及多项内部优化。

- 🚀 新增功能：为计算机操作类型添加了 keys 字段，并为 WebSocket 类引入了异步迭代器和 stream() 方法
- 🐛 错误修复：调整了 SDK 响应类型以匹配扩展的项目模式，并明确了 ResponseInputMessageItem 中 type 字段的必要性
- 🔧 内部优化：更新了持续集成流程以跳过仅涉及元数据的更改检查，重构了导入方式并更新了 .gitignore 配置
- 🧪 测试改进：将测试工具从 prism 切换为 steady，并升级 steady 到多个新版本以提升测试稳定性

---

### [TypeScript/src/compiler at main · microsoft/TypeScript · GitHub](https://github.com/microsoft/TypeScript/tree/main/src/compiler)

**原文标题**: [TypeScript/src/compiler at main · microsoft/TypeScript · GitHub](https://github.com/microsoft/TypeScript/tree/main/src/compiler)

TypeScript 是一个由微软开发的开源编程语言，它在 GitHub 上拥有活跃的社区和丰富的编译器源代码结构。

- 🏢 **项目归属** – 由微软维护，是一个公开的 TypeScript 语言项目
- ⭐ **社区热度** – 在 GitHub 上获得 108k 星标和 13.3k 分支，显示出广泛的使用和贡献
- 🔧 **代码结构** – 编译器核心代码位于 `src/compiler/` 目录，包含模块解析、类型检查、发射器等关键组件
- 📁 **文件组织** – 目录下有多个重要文件，如 `checker.ts`（类型检查）、`parser.ts`（语法解析）、`emitter.ts`（代码生成）
- 🔄 **开发活跃** – 项目中有 5k 个议题和 13 个拉取请求，表明持续的开发和问题处理
- 🛡️ **安全状态** – 当前安全警报显示为 0，反映项目在安全方面的稳定性
- 📚 **文档资源** – 提供 Wiki、项目、模型等额外导航选项，支持开发者深入了解

---

### [10 倍速 TypeScript - TypeScript](https://devblogs.microsoft.com/typescript/typescript-native-port/)

**原文标题**: [A 10x Faster TypeScript - TypeScript](https://devblogs.microsoft.com/typescript/typescript-native-port/)

TypeScript 团队宣布正在开发原生版本编译器，旨在将性能提升高达 10 倍，大幅缩短编辑器启动和构建时间，并降低内存占用，预计 2025 年中发布预览版，年底实现功能完整的语言服务。

- 🚀 性能大幅提升：原生版本在多个流行代码库测试中实现约 10 倍速度提升，如 VS Code 从 77.8 秒缩短至 7.5 秒
- ⏱️ 编辑器体验优化：项目加载时间提升 8 倍，内存占用减少约一半，语言服务操作响应更快
- 🗓️ 版本规划：当前 TypeScript 6.x 系列继续开发，原生版本将作为 TypeScript 7.0 发布，两者将并行维护
- 🔧 技术路线：基于 Go 语言重写编译器，支持语言服务器协议（LSP），代码库已开源供社区测试
- 🤖 未来展望：高性能为 AI 工具集成和高级重构功能奠定基础，提升大规模代码库的开发体验

---

### [TypeScript 6.0 发布公告 - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-6-0/#types-now-defaults-to-%5B%5D)

**原文标题**: [Announcing TypeScript 6.0 - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-6-0/#types-now-defaults-to-%5B%5D)

TypeScript 6.0 正式发布，这是一个过渡版本，旨在为基于 Go 重写的原生 TypeScript 7.0 铺平道路。本次更新包含多项新特性、改进以及为迎接 7.0 所做的准备性调整，同时也引入了一些破坏性变更和弃用项。

- 🚀 **发布与定位**：TypeScript 6.0 已正式可用，它是基于当前 JavaScript 代码库的最后一个主要版本，作为 5.9 与未来的原生版本 7.0 之间的桥梁。
- 🛠️ **新特性与改进**：包括对无 `this` 使用的函数减少上下文敏感性、支持以 `#/` 开头的子路径导入、允许 `--moduleResolution bundler` 与 `--module commonjs` 组合等。
- 🧪 **新增编译选项**：引入了 `--stableTypeOrdering` 标志，使 6.0 的类型排序行为与 7.0 一致，便于迁移对比，但可能会带来性能开销。
- 📚 **库与目标更新**：新增 `es2025` 作为 `target` 和 `lib` 选项，并为 Temporal API、Map 的 `getOrInsert`（upsert）方法以及 `RegExp.escape` 添加了新的类型定义。
- 🌐 **DOM 库整合**：`dom` 库现在默认包含 `dom.iterable` 和 `dom.asynciterable` 的内容，简化了配置。
- ⚠️ **破坏性变更与弃用**：多项默认值被更新（如 `strict` 默认为 `true`，`module` 默认为 `esnext`），并且弃用了 `target: es5`、`--moduleResolution node`、`--baseUrl`、`--outFile` 等大量旧选项和语法。`tsconfig.json` 中的 `types` 字段现在默认为空数组，`rootDir` 的默认推断逻辑也发生了变化。
- 🔮 **为 7.0 做准备**：团队鼓励开发者在升级到 6.0 后，尝试 TypeScript 7.0 的原生预览版。6.0 中已弃用的选项在 7.0 中将完全移除。

---

### [TypeScript 6.0 发布公告 - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-6-0/#simple-default-changes)

**原文标题**: [Announcing TypeScript 6.0 - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-6-0/#simple-default-changes)

TypeScript 6.0 正式发布，这是一个过渡版本，旨在为基于 Go 重写的原生 TypeScript 7.0 铺平道路。本次更新包含多项新特性、改进以及为迎接 7.0 所做的准备性调整，同时引入了多项破坏性变更和弃用项。

- 🚀 **发布与定位**：TypeScript 6.0 是当前 JavaScript 代码库的最后一个主要版本，作为 5.9 与未来原生版本 7.0 之间的桥梁。
- 🧠 **类型推断优化**：对未使用 `this` 的函数减少了上下文敏感性，提升了在泛型调用中（尤其是方法语法）的类型推断能力。
- 📁 **子路径导入支持**：现在支持以 `#/` 开头的子路径导入（Subpath Imports），与 Node.js 20+ 及打包器行为对齐。
- ⚙️ **模块解析组合**：`--moduleResolution bundler` 现在可与 `--module commonjs` 组合使用，为许多项目提供了合适的升级路径。
- 🔢 **稳定的类型排序**：新增 `--stableTypeOrdering` 标志，使 6.0 的类型排序行为与 7.0 保持一致，便于迁移对比，但可能会带来性能开销。
- 🎯 **新的编译目标**：增加了 `es2025` 作为 `target` 和 `lib` 的选项，包含新的内置 API 类型。
- ⏳ **Temporal API 类型**：为已进入 Stage 4 的 Temporal API 提供了内置类型支持，可通过 `esnext` 或 `esnext.temporal` 使用。
- 🗺️ **Map 新增方法**：为 `Map` 和 `WeakMap` 添加了 `getOrInsert` 和 `getOrInsertComputed` 方法类型，简化了“检查 - 插入”模式。
- 🛡️ **RegExp.escape**：新增 `RegExp.escape` 函数类型，用于安全地转义正则表达式中的特殊字符。
- 🌐 **DOM 库整合**：`dom` 库现在默认包含了 `dom.iterable` 和 `dom.asynciterable` 的内容，简化了配置。
- ⚠️ **多项破坏性变更与弃用**：包括默认启用 `strict` 模式、`module` 默认改为 `esnext`、`types` 默认改为空数组、弃用 `target: es5`、`--moduleResolution node`、`--baseUrl`、`--outFile` 等大量旧选项和语法，旨在简化编译器并适应现代开发生态。
- 🚧 **为 7.0 做准备**：强烈建议在升级到 6.0 后解决所有弃用警告，以便顺利过渡到即将发布的 TypeScript 7.0 原生版本。

---

### [TypeScript 6.0 发布公告 - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-6-0/#deprecated:---moduleresolution-node-(a.k.a.---moduleresolution-node10))

**原文标题**: [Announcing TypeScript 6.0 - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-6-0/#deprecated:---moduleresolution-node-(a.k.a.---moduleresolution-node10))

TypeScript 6.0 正式发布，作为当前 JavaScript 代码库的最后一个主要版本，它充当了 TypeScript 5.9 与即将到来的、基于 Go 原生重写的 TypeScript 7.0 之间的桥梁。此版本主要旨在为平稳过渡到 7.0 做准备，包含了对齐性改进、新功能以及多项旨在反映现代 JavaScript 生态的破坏性变更和弃用。

- 🚀 **版本定位与过渡**：TypeScript 6.0 是当前代码库的最终版本，核心目标是作为通往基于 Go 原生重写的 TypeScript 7.0 的过渡桥梁。
- 🛠️ **主要新特性与改进**：包括减少无 `this` 使用函数的上下文敏感性、支持以 `#/` 开头的子路径导入、允许 `--moduleResolution bundler` 与 `--module commonjs` 组合使用等。
- 🧪 **新增 `--stableTypeOrdering` 标志**：此标志用于使 6.0 的类型排序行为与 7.0 保持一致，帮助诊断版本间差异，但可能带来性能开销。
- 📦 **支持新的 ECMAScript 特性**：添加了 `es2025` 作为 `target` 和 `lib` 的新选项，并引入了 `Temporal` API、`Map`/`WeakMap` 的 `getOrInsert`（upsert）方法以及 `RegExp.escape` 的新类型。
- 🔄 **DOM 库更新**：`dom` 库现在默认包含 `dom.iterable` 和 `dom.asynciterable` 的内容，简化了配置。
- ⚠️ **多项破坏性变更与弃用**：包括默认启用 `strict` 模式、`module` 默认改为 `esnext`、`target` 默认改为 `es2025`、`rootDir` 和 `types` 的默认值变更，以及弃用 `target: es5`、`--moduleResolution node`、`--baseUrl`、`--outFile` 等大量旧选项和语法。
- 🧭 **为 TypeScript 7.0 做准备**：6.0 中标记为弃用的选项在 7.0 中将完全移除，建议用户尽快处理相关警告。团队鼓励开发者尝试 7.0 的原生预览版。

---

### [TypeScript 6.0 发布公告 - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-6-0/#subpath-imports-starting-with-#/)

**原文标题**: [Announcing TypeScript 6.0 - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-6-0/#subpath-imports-starting-with-#/)

TypeScript 6.0 正式发布，这是一个过渡版本，旨在为基于 Go 重写的 TypeScript 7.0 原生编译器铺平道路。本次更新包含多项新特性、改进以及为迎接 7.0 而做的重大变更和弃用。

- 🚀 **发布与定位**：TypeScript 6.0 是当前 JavaScript 代码库的最后一个主要版本，作为 5.9 和未来 7.0 之间的桥梁，主要变化旨在为迁移到 7.0 做准备。
- 🧠 **类型推断优化**：对未使用 `this` 的函数减少了上下文敏感性，改善了在泛型调用中方法语法的类型推断能力。
- 📁 **子路径导入支持**：现在支持 Node.js 中以 `#/` 开头的子路径导入，与 `--moduleResolution nodenext` 或 `bundler` 选项配合使用。
- ⚙️ **模块解析组合**：现在允许将 `--moduleResolution bundler` 与 `--module commonjs` 组合使用，为许多项目提供了合适的升级路径。
- 🔢 **稳定的类型排序**：新增 `--stableTypeOrdering` 标志，使 6.0 的类型排序行为与 7.0 保持一致，有助于减少版本间差异，但可能会带来性能开销。
- 🎯 **新的编译目标**：增加了 `es2025` 作为 `target` 和 `lib` 的选项，包含新的内置 API 类型（如 `RegExp.escape`）并将一些声明从 `esnext` 移入。
- ⏳ **Temporal API 类型**：为已达到 Stage 4 的 Temporal API 提供了内置类型支持，可通过 `--target esnext` 或 `"lib": ["esnext"]` 使用。
- 🗺️ **新增 Map 方法类型**：为 `Map` 和 `WeakMap` 新增了 `getOrInsert` 和 `getOrInsertComputed` 方法的类型定义，简化了“检查 - 设置”模式。
- 🛡️ **RegExp.escape**：增加了 `RegExp.escape` 函数的类型支持，用于转义正则表达式中的特殊字符。
- 🌐 **DOM 库整合**：`dom` 库现在默认包含了 `dom.iterable` 和 `dom.asynciterable` 的内容，简化了配置。
- ⚠️ **重大变更与弃用**：引入了多项默认值变更和弃用，包括 `strict` 默认为 `true`、`module` 默认为 `esnext`、默认 `target` 更新、弃用 `target: es5`、`--moduleResolution node`、`--baseUrl`、`--outFile` 等，旨在反映现代开发生态并提升性能。建议使用 `"ignoreDeprecations": "6.0"` 暂时忽略警告，但这些选项将在 7.0 中完全移除。
- 🧪 **为 7.0 做准备**：团队鼓励开发者在升级到 6.0 后，积极尝试 TypeScript 7.0 的原生预览版，并反馈问题，以帮助其尽快稳定。

---

### [模块：允许以 `#/` 开头的子路径导入 by hybrist · Pull Request #60864 · nodejs/node · GitHub](https://github.com/nodejs/node/pull/60864)

**原文标题**: [module: allow subpath imports that start with `#/` by hybrist · Pull Request #60864 · nodejs/node · GitHub](https://github.com/nodejs/node/pull/60864)

Node.js 项目合并了一个 PR，允许子路径导入以 `#/` 开头，这为映射源码根目录提供了一种更现实的替代方案，无需特殊工具支持。

- 🚀 允许子路径导入以 `#/` 开头，作为映射源码根目录（如 `@/`）的替代方案
- 🔄 将原本会报错的导入情况转为正常，属于向后兼容的次要版本更新
- ✅ 代码变更通过了完整的 CI 测试，且测试覆盖率保持稳定
- 💬 社区反应积极，获得了多位贡献者的认可与批准
- 📅 该 PR 于 2025 年 12 月 4 日合并至主分支

---

### [TypeScript 6.0 发布公告 - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-6-0/#rootdir-now-defaults-to-.)

**原文标题**: [Announcing TypeScript 6.0 - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-6-0/#rootdir-now-defaults-to-.)

TypeScript 6.0 正式发布，这是一个过渡版本，旨在为基于 Go 重写的原生编译器 TypeScript 7.0 铺平道路。本次更新包含多项新特性、改进以及为迎接 7.0 而进行的调整，同时引入了多项破坏性变更和弃用，以反映现代 JavaScript 生态的发展。

- 🚀 **发布与定位**：TypeScript 6.0 已正式可用，它是基于当前代码库的最后一个主要版本，作为 5.9 与未来的原生版本 7.0 之间的桥梁。
- 🛠️ **上下文敏感性优化**：对于未使用 `this` 的函数，TypeScript 6.0 在类型推断时不再将其视为“上下文敏感函数”，从而解决了某些方法语法中参数类型无法正确推断的问题。
- 📁 **子路径导入支持**：现在支持 Node.js 中以前导 `#/` 开头的子路径导入（如 `#/*`），需在 `--moduleResolution` 设置为 `nodenext` 或 `bundler` 时使用。
- 🔀 **模块解析组合**：现在允许将 `--moduleResolution bundler` 与 `--module commonjs` 组合使用，为许多项目提供了合适的升级路径。
- 🧮 **稳定类型排序标志**：新增 `--stableTypeOrdering` 标志，使 6.0 的类型排序行为与 7.0 保持一致，有助于减少版本间差异，但可能会带来性能开销。
- 🎯 **新的编译目标**：新增 `es2025` 选项用于 `target` 和 `lib`，虽然未引入新语法，但包含了新的内置 API 类型。
- ⏳ **Temporal API 类型**：为已达到 Stage 4 的 Temporal API 提供了内置类型支持，可通过 `esnext` 或 `esnext.temporal` 库使用。
- 🗺️ **新增 Map 方法类型**：为 `Map` 和 `WeakMap` 新增了 `getOrInsert` 和 `getOrInsertComputed` 方法的类型定义，这两个方法来自已进入 Stage 4 的提案。
- 🛡️ **RegExp.escape**：新增 `RegExp.escape` 函数的类型，用于转义正则表达式中的特殊字符，包含在 `es2025` 库中。
- 🌐 **DOM 库整合**：`dom` 库现在默认包含了 `dom.iterable` 和 `dom.asynciterable` 的内容，简化了配置。
- ⚠️ **多项破坏性变更与弃用**：包括默认启用 `strict` 模式、`module` 默认改为 `esnext`、`target` 默认改为最新 ES 版本、`types` 默认改为空数组、弃用 `target: es5`、`--moduleResolution node`、`--baseUrl`、`--outFile` 等多项旧有选项和语法，旨在提升性能并适应现代开发实践。
- 🧪 **为 7.0 做准备**：TypeScript 6.0 中的弃用项在设置 `"ignoreDeprecations": "6.0"` 后仍可工作，但将在 7.0 中被完全移除，建议用户尽快处理相关警告。团队鼓励开发者尝试 TypeScript 7.0 的原生预览版。

---

### [TypeScript 6.0 发布公告 - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-6-0/#deprecated:---esmoduleinterop-false-and---allowsyntheticdefaultimports-false)

**原文标题**: [Announcing TypeScript 6.0 - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-6-0/#deprecated:---esmoduleinterop-false-and---allowsyntheticdefaultimports-false)

TypeScript 6.0 正式发布，这是一个过渡版本，旨在为基于 Go 重写的原生 TypeScript 7.0 做准备。它包含多项新特性、改进以及为对齐 7.0 而引入的重大变更和弃用。

- 🚀 **版本定位**：TypeScript 6.0 是当前 JavaScript 代码库的最后一个主要版本，作为 5.9 和未来的原生 7.0 之间的桥梁。
- 🧠 **类型推断优化**：对未使用 `this` 的函数减少了上下文敏感性，改善了在泛型调用中方法语法的类型推断。
- 📁 **子路径导入支持**：现在支持 Node.js 中以前导 `#/` 开头的子路径导入，与 `--moduleResolution` 的 `nodenext` 和 `bundler` 选项兼容。
- ⚙️ **模块解析组合**：现在允许将 `--moduleResolution bundler` 与 `--module commonjs` 组合使用，为许多项目提供了合适的升级路径。
- 🔢 **稳定的类型排序**：引入了 `--stableTypeOrdering` 标志，使 6.0 的类型排序行为与 7.0 保持一致，以帮助迁移诊断，但可能会带来性能开销。
- 🎯 **新的编译目标**：增加了 `es2025` 作为 `target` 和 `lib` 的选项，包含了新的内置 API 类型。
- ⏳ **Temporal API 类型**：为已达到 Stage 4 的 Temporal API 提供了内置类型支持，可通过 `esnext` 或 `esnext.temporal` 使用。
- 🗺️ **Map 新增方法**：为 `Map` 和 `WeakMap` 添加了 `getOrInsert` 和 `getOrInsertComputed` 方法类型，简化了“检查 - 设置”模式。
- 🛡️ **RegExp.escape**：增加了 `RegExp.escape` 函数的类型，用于转义正则表达式中的特殊字符，包含在 `es2025` 库中。
- 🌐 **DOM 库整合**：将 `dom.iterable` 和 `dom.asynciterable` 的内容完全整合到 `dom` 库中，简化了配置。
- ⚠️ **多项重大变更与弃用**：包括默认启用 `strict` 模式、`module` 默认改为 `esnext`、弃用 `target: es5`、`--moduleResolution node`、`--baseUrl`、`--outFile` 等，旨在反映现代开发现状并为 7.0 铺路。可通过 `"ignoreDeprecations": "6.0"` 暂时忽略，但这些选项将在 7.0 中移除。
- 📄 **配置默认值调整**：`rootDir` 现在默认是 `tsconfig.json` 所在目录；`types` 默认改为空数组 `[]`，需要显式声明所需的 `@types` 包（如 `["node"]`）以提升性能。
- 🚫 **命令行行为变更**：当存在 `tsconfig.json` 时，在命令行中指定文件进行编译现在会报错，需使用 `--ignoreConfig` 标志来忽略配置。
- 🔜 **鼓励尝试 7.0 预览版**：团队鼓励用户在升级到 6.0 后尝试 TypeScript 7.0 的原生预览版，并期待在几个月内正式发布。

---

