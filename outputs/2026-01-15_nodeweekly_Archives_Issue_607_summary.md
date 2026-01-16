### [Node 周刊第 607 期：2026 年 1 月 15 日](https://nodeweekly.com/issues/607)

**原文标题**: [Node Weekly Issue 607: January 15, 2026](https://nodeweekly.com/issues/607)

本期 Node.js 周报主要涵盖安全更新、新工具发布、框架集成及社区动态，重点包括 Node.js 多个版本的安全补丁发布、Clerk API 密钥公测、Microsoft Aspire 对 Node.js 的正式支持，以及一系列开发工具更新。

- 🚨 Node.js 多个版本发布安全更新，修复了与 async_hooks 相关的拒绝服务漏洞
- 🔑 Clerk 推出 API 密钥公测功能，支持用户创建和管理 API 密钥
- 📦 Node.js 官方发布软件包配置指南，帮助开发者构建和迁移软件包
- 🤝 Microsoft Aspire 13 将 Node.js 提升为一等公民，支持全栈 JS 应用开发
- ⚡ 文章推荐使用迭代器助手替代数组操作以提高性能
- 🛠️ 多款开发工具更新：Better SQLite3 12.6、memlab 2.0 内存检测框架、pnpm 10.28 等
- 📅 Node Congress 在线 JavaScript 活动将于 3 月 26-27 日举行
- 🎂 jQuery 庆祝成立 20 周年
- 📚 推荐阅读：TypeScript 简明指南、JavaScript 性能优化等文章

---

### [Node.js — 2026 年 1 月 13 日星期二安全版本发布](https://nodejs.org/en/blog/vulnerability/december-2025-security-releases)

**原文标题**: [Node.js — Tuesday, January 13, 2026 Security Releases](https://nodejs.org/en/blog/vulnerability/december-2025-security-releases)

Node.js 项目于 2026 年 1 月 13 日发布了安全更新，针对 20.x、22.x、24.x 和 25.x 等活跃发布线，共修复了 8 个安全问题，包括 3 个高危漏洞、4 个中危漏洞和 1 个低危漏洞，并更新了相关依赖。用户应尽快升级到最新版本以确保系统安全。

- 🚨 **高危漏洞**：修复了 3 个高危问题，包括缓冲区未初始化内存泄露（CVE-2025-55131）、权限模型绕过（CVE-2025-55130）和 HTTP/2 服务崩溃（CVE-2025-59465），影响所有活跃发布线。
- ⚠️ **中危漏洞**：解决了 4 个中危问题，涉及不可捕获的堆栈溢出错误（CVE-2025-59466）、TLS 内存泄露（CVE-2025-59464）、权限模型绕过（CVE-2026-21636）和 TLS 回调异常（CVE-2026-21637），部分仅影响特定版本。
- 🔧 **低危漏洞**：修复了 1 个低危问题（CVE-2025-55132），允许在只读权限下修改文件时间戳，影响权限模型用户。
- 📦 **依赖更新**：安全版本包含对 c-ares 和 undici 的更新，以解决公开漏洞。
- ⏰ **发布详情**：新版本（Node.js 20.20.0、22.22.0、24.13.0、25.3.0）已于 2025 年 12 月 15 日或之后发布，建议用户立即升级。
- 📢 **安全建议**：项目强调使用最新版本的重要性，并提供了安全政策、漏洞报告流程和邮件列表订阅方式，以保持更新。

---

### [Node.js — Node.js 25.3.0（当前版本）](https://nodejs.org/en/blog/release/v25.3.0)

**原文标题**: [Node.js — Node.js 25.3.0 (Current)](https://nodejs.org/en/blog/release/v25.3.0)

Node.js 25.3.0 是一个安全版本，主要修复了多个安全漏洞，并更新了依赖项，同时提供了各平台的安装包和二进制文件下载。

- 🔒 修复了 TLSSocket 默认错误处理器的安全漏洞（CVE-2025-59465）
- 🌐 在 pipe_wrap 连接时增加了网络权限检查（CVE-2026-21636）
- 🔗 要求对符号链接 API 具有完整的读写权限（CVE-2025-55130）
- ⏱️ 在权限模型启用时禁用了 futimes 功能（CVE-2025-55132）
- 📊 在 async_hooks 中重新抛出堆栈溢出异常（CVE-2025-59466）
- 🛡️ 重构了不安全的缓冲区创建以移除零填充切换（CVE-2025-55131）
- 🔄 将回调异常通过错误处理器路由（CVE-2026-21637）
- 🔄 更新了 c-ares 依赖至 v1.34.6 版本
- 🌐 更新了 undici 依赖至 7.18.2 版本
- 💾 提供了 Windows、macOS、Linux 等多平台的安装包和二进制文件下载

---

### [Node.js — Node.js 24.13.0（长期支持版）](https://nodejs.org/en/blog/release/v24.13.0)

**原文标题**: [Node.js — Node.js 24.13.0 (LTS)](https://nodejs.org/en/blog/release/v24.13.0)

Node.js 24.13.0（LTS）版本“Krypton”是一次安全更新，主要修复了多个安全漏洞，并更新了依赖库，同时提供了各平台的安装包和二进制文件下载。

- 🔐 修复了多个安全漏洞，包括 TLSSocket 默认错误处理、权限模型下的 futimes 禁用、符号链接 API 的读写权限要求等
- ⬆️ 更新了 c-ares 依赖至 v1.34.6 版本，并升级 undici 到 7.18.2
- 🛠️ 包含多项内部改进，如重构不安全的缓冲区创建以移除零填充切换，以及通过错误处理器路由回调异常
- 📦 提供了 Windows、macOS、Linux、AIX 等多平台的安装程序和二进制文件下载
- 📄 包含完整的源代码、文档和 SHASUMS 校验文件，确保下载文件的完整性和安全性

---

### [Node.js — Node.js 22.22.0（长期支持版）](https://nodejs.org/en/blog/release/v22.22.0)

**原文标题**: [Node.js — Node.js 22.22.0 (LTS)](https://nodejs.org/en/blog/release/v22.22.0)

Node.js 22.22.0（LTS）版本发布，代号“Jod”，主要是一次安全更新，修复了多个安全漏洞并更新了依赖库。

- 🔐 **安全修复**：包含六个 CVE 漏洞修复，涉及 TLS 错误处理、权限模型下的文件时间设置、符号链接 API 权限、异步钩子中的堆栈溢出异常处理、缓冲区创建优化以及 TLS 回调异常路由。
- 📦 **依赖更新**：升级了 c-ares 至 v1.34.6 和 undici 至 6.23.0，以提升网络解析和 HTTP 客户端性能。
- 🛠️ **多平台支持**：提供了 Windows、macOS、Linux、AIX 等多种操作系统的安装包和二进制文件，涵盖 x86、x64、ARM 等架构。
- 📄 **完整性验证**：发布了详细的 SHASUMS 校验和及 PGP 签名，确保下载文件的完整性和安全性。
- 🔗 **资源链接**：包含官方文档、源代码和其他发布文件的访问链接，方便开发者获取详细信息和进行验证。

---

### [Node.js — Node.js 20.20.0（长期支持版）](https://nodejs.org/en/blog/release/v20.20.0)

**原文标题**: [Node.js — Node.js 20.20.0 (LTS)](https://nodejs.org/en/blog/release/v20.20.0)

Node.js 20.20.0（LTS）版本发布，代号“Iron”，主要是一次安全更新，修复了多个安全漏洞并更新了依赖库。

- 🔒 修复了多个安全漏洞，包括权限模型启用时禁用 futimes、为 TLSSocket 添加默认错误处理程序等
- 📦 更新了 c-ares 依赖至 v1.34.6 版本
- 🔄 更新了 undici 依赖至 6.23.0 版本
- 💾 提供了 Windows、macOS、Linux 等多种操作系统的安装包和二进制文件下载
- 📄 包含完整的源代码和文档链接，以及 SHASUMS 校验和 PGP 签名确保文件完整性

---

### [Node.js — 为 React、Next.js 及 APM 用户缓解因不可恢复栈空间耗尽导致的拒绝服务漏洞](https://nodejs.org/en/blog/vulnerability/january-2026-dos-mitigation-async-hooks)

**原文标题**: [Node.js — Mitigating Denial-of-Service Vulnerability from Unrecoverable Stack Space Exhaustion for React, Next.js, and APM Users](https://nodejs.org/en/blog/vulnerability/january-2026-dos-mitigation-async-hooks)

Node.js 中存在一个安全漏洞，当启用 `async_hooks` 时，用户代码中的栈溢出会导致进程直接崩溃（退出码 7），而不是抛出可捕获的 `RangeError`。这影响了大量使用 `AsyncLocalStorage`（基于 `async_hooks`）的流行框架和工具，包括 React Server Components、Next.js 以及所有主流 APM（应用性能监控）工具，使得依赖未经验证输入控制递归深度的应用容易遭受拒绝服务攻击。Node.js 团队已发布安全更新修复此问题，但强调开发者不应依赖栈溢出恢复机制来保证服务可用性，而应主动验证输入并限制递归深度。

- 🐛 **漏洞概述**：当启用 `async_hooks` 时，用户代码中的栈溢出会导致 Node.js 进程直接崩溃（退出码 7），而非抛出可捕获的 `RangeError`。
- 🚨 **影响范围**：React Server Components、Next.js 以及所有使用 `AsyncLocalStorage` 或 `async_hooks` 的主流 APM 工具（如 Datadog、New Relic 等）均受影响。
- 🛡️ **修复版本**：Node.js 20.20.0、22.22.0、24.13.0 和 25.3.0 已包含修复补丁，建议用户尽快升级。
- ⚠️ **根本原因**：栈溢出行为并非 ECMAScript 规范的一部分，V8 引擎仅以“最大努力”尝试恢复，因此不能依赖其作为安全防御机制。
- 🔧 **开发者建议**：对于可能由攻击者控制递归深度的代码，应主动验证输入、限制递归深度，而非依赖运行时抛出可捕获错误。
- 📜 **版本差异**：Node.js 24+ 的 `AsyncLocalStorage` 已基于 `AsyncContextFrame` 重构，不再使用 `async_hooks`，因此不受此漏洞影响。
- ⏳ **时间线**：漏洞于 2025 年 12 月报告，2026 年 1 月 13 日发布安全更新并公开披露。

---

### [Node.js 修复可能导致崩溃的 AsyncLocalStorage 异步本地存储漏洞](https://socket.dev/blog/node-js-fixes-asynclocalstorage-crash-bug-that-could-take-down-production-servers)

**原文标题**: [Node.js Fixes AsyncLocalStorage Crash Bug That Could Take Do...](https://socket.dev/blog/node-js-fixes-asynclocalstorage-crash-bug-that-could-take-down-production-servers)

研究人员发现一款恶意 Chrome 扩展程序会窃取用户在 MEXC 交易所新创建的 API 密钥，通过 Telegram 外传数据，攻击者可借此完全控制用户账户并进行交易与提现操作。

- 🕵️ 恶意扩展程序伪装成合法工具，在用户创建 MEXC API 密钥时实施窃取
- 📨 被盗密钥通过 Telegram 机器人实时传输至攻击者控制的频道
- 💸 攻击者获得账户完全控制权后，可执行任意交易及资金转移操作
- ⚠️ 安全专家建议用户仅通过官方渠道安装扩展，并为 API 密钥设置严格的 IP 与权限限制

---

### [API 密钥公测版](https://clerk.com/changelog/2025-12-11-api-keys-public-beta?utm_source=cooper_press&utm_medium=newsletter&utm_campaign=api-keys&utm_content=01-15-26&dub_id=WtHryqtSS9kgBEGX)

**原文标题**: [API Keys Public Beta](https://clerk.com/changelog/2025-12-11-api-keys-public-beta?utm_source=cooper_press&utm_medium=newsletter&utm_campaign=api-keys&utm_content=01-15-26&dub_id=WtHryqtSS9kgBEGX)

Clerk 推出了 API 密钥公开测试版，允许用户创建代表其访问应用 API 的密钥，提供零代码 UI 组件和 SDK 集成支持，并包含细粒度权限控制与即时撤销功能，测试期间免费使用。

- 🔑 API 密钥现已支持授权，用户可通过预置组件或 SDK 创建、查看和撤销密钥
- 🧩 在 Clerk 仪表板启用后，用户档案和组织档案组件将显示 API 密钥管理标签
- ⚙️ 支持通过后端 SDK 以编程方式管理密钥，可自定义范围、声明和过期时间
- 🔐 使用 auth() 助手验证 API 密钥，并可通过范围检查实现精细访问控制
- 🚫 密钥采用不透明令牌，支持即时撤销，始终保持用户或组织的身份关联
- 💰 测试期间免费使用，正式发布后按密钥创建（$0.001/次）和验证（$0.00001/次）计费
- 📚 提供完整指南、SDK 参考、仪表板设置及分步教程等资源支持快速上手

---

### [引言 · Node.js 包配置指南](https://nodejs.github.io/package-examples/)

**原文标题**: [Introduction · Node.js package configuration guide](https://nodejs.github.io/package-examples/)

本文是关于如何为 Node.js 配置包的指南，涵盖包配置的基础知识，包括文件结构、package.json 文件的使用以及如何处理 CommonJS 和 ECMAScript 模块（ESM）。

- 📦 介绍 Node.js 包配置指南，涵盖文件结构、package.json 及模块系统
- 📄 解释 CommonJS 和 ESM 两种模块规范的基本概念与区别
- 🛠️ 展示单文件包配置方法，包括 CommonJS 和 ESM 格式的实现
- 📁 说明多文件包配置策略及模块间的互操作性
- 🔄 提供模块系统迁移指南，涵盖导入导出、上下文变量和 package.json 调整
- 📚 附带完整代码示例仓库供参考学习

---

### [节点大会](https://nodecongress.com/)

**原文标题**: [Node Congress](https://nodecongress.com/)

Node Congress 2026 是一场专注于现代 JavaScript 后端运行时和最佳实践的线上技术大会，将于 2026 年 3 月 26 日至 27 日举行，旨在帮助开发者提升技能、拓展人脉并探索职业机会。

- 🚀 **活动时间与形式**：2026 年 3 月 26 日至 27 日线上举行，支持高清直播、远程互动和网络交流。
- 🌍 **参与规模**：预计吸引全球超过 5000 名开发者，设有 20 多位演讲者和 5 个以上的研讨会及讨论室。
- 💻 **技术焦点**：涵盖 Bun、Deno、Cloudflare Workers、Node.js、WinterTC 等运行时，以及安全、DevOps、数据库、性能、架构等周边议题。
- 🎤 **演讲嘉宾**：包括 Node.js TSC 成员 Matteo Collina、Cloudflare 工程师 James Snell 和 Kenton Varda 等业界专家，目前仍开放演讲提案提交。
- 🎟️ **门票选项**：提供早鸟票（65 欧元）和包含全年 GitNation 会议访问权限的 Multipass 套票（200 欧元/年），均含研讨会、录制视频和参与证书。
- 🤝 **赞助与合作**：大会由 GitNation 组织，并得到 FocusReactive 等合作伙伴的支持，同时欢迎更多赞助机会。
- 📧 **持续更新**：可通过订阅通讯获取最新动态、专属优惠和折扣信息。

---

### [Vercel Sandbox 现已默认采用 Node.js 24 运行时版本](https://vercel.com/changelog/node-js-runtime-now-defaults-to-version-24-for-vercel-sandbox)

**原文标题**: [Node.js runtime now defaults to version 24 for Vercel Sandbox - Vercel](https://vercel.com/changelog/node-js-runtime-now-defaults-to-version-24-for-vercel-sandbox)

Vercel Sandbox 现已默认采用 Node.js 24 版本，确保运行时环境与最新的 Node.js 特性和性能改进保持同步。

- 🚀 **默认升级**：未明确配置运行时环境时，Sandbox 将自动使用 Node.js 24
- 📚 **文档支持**：详细配置和使用方法可查阅 Sandbox 官方文档
- ⚙️ **版本验证**：通过运行命令可轻松检查当前 Node.js 版本
- 🔄 **持续更新**：此举旨在保持与 Node.js 最新发展步伐一致

---

### [停止把所有东西都变成数组（并减少工作量）- 马特·史密斯](https://allthingssmitty.com/2026/01/12/stop-turning-everything-into-arrays-and-do-less-work-instead/)

**原文标题**: [
    Stop turning everything into arrays (and do less work instead) - Matt Smith
  ](https://allthingssmitty.com/2026/01/12/stop-turning-everything-into-arrays-and-do-less-work-instead/)

前端开发中，JavaScript 的迭代器助手提供了一种惰性处理数据的新方式，相比传统的数组方法，它能减少不必要的计算和内存分配，特别适合处理大型数据集、流式数据或 UI 渲染场景。

- 🔄 迭代器助手是链式方法，作用于迭代器对象而非数组，通过惰性求值仅在需要时处理数据
- 🛑 传统数组方法如 `map`、`filter` 会创建多个中间数组并处理所有数据，即使只需部分结果
- ⚡ 惰性处理避免不必要的工作，例如在渲染大型列表时只处理实际显示的项目
- 🌊 支持异步迭代器，适合分页 API 或流式数据，无需缓冲全部响应
- 📦 无需第三方库即可构建清晰的数据处理管道，代码更简洁原生
- ⚠️ 需注意迭代器为一次性使用、无随机访问、调试可能消耗数据等限制
- 🚀 已在现代浏览器和 Node.js 22+ 中广泛支持，适用于当前开发环境

---

### [迭代器助手 · V8](https://v8.dev/features/iterator-helpers)

**原文标题**: [Iterator helpers · V8](https://v8.dev/features/iterator-helpers)

迭代器助手是 ECMAScript 中新增的一组迭代器原型方法，旨在简化迭代器的通用操作，适用于所有继承自 Iterator.prototype 的对象（如数组迭代器）。以下通过博客归档页面的示例，介绍这些方法的功能与应用。

- 🗺️ **map 方法**：接受一个映射函数，返回对原迭代器每个值应用该函数后的新迭代器，例如提取博客标题列表。
- 🔍 **filter 方法**：接受筛选函数，返回原迭代器中使函数返回真值的元素，如筛选标题含“V8”的博客。
- 🔟 **take 方法**：接受整数参数，返回原迭代器前 N 个值，例如选取最近 10 篇博客。
- ⏬ **drop 方法**：接受整数参数，跳过前 N 个值后返回剩余迭代器，如忽略最近 10 篇后列出其他博客。
- 🧩 **flatMap 方法**：接受映射函数，将函数返回的多个迭代器扁平化为单一迭代器，例如提取所有博客标签。
- 🧮 **reduce 方法**：接受归约函数和初始值，对迭代器累计计算返回单个结果，如统计含“security”标签的博客数量。
- 📋 **toArray 方法**：将迭代器转换为数组，便于进一步处理，如将最近 10 篇博客转为数组。
- 🔁 **forEach 方法**：对每个元素应用函数，无返回值但可产生副作用，例如收集博客发布日期。
- ✅ **some 方法**：接受断言函数，若任一元素满足条件则返回 true，如检查是否有博客标题含“Iterators”。
- ✔️ **every 方法**：接受断言函数，仅当所有元素满足条件时返回 true，例如验证所有博客是否均含“V8”关键词。
- 🔎 **find 方法**：接受断言函数，返回首个满足条件的元素，如查找首篇含“V8”的博客标题。
- 🔄 **from 静态方法**：将可迭代对象或普通对象转换为迭代器，确保统一处理接口。

迭代器助手已在 V8 v12.2 中实现，Chrome 122+ 和 Babel 提供支持，而 Firefox、Safari 和 Node.js 暂未支持。

---

### [错误](https://nodeweekly.com/link/179273/web)

**原文标题**: [Error](https://nodeweekly.com/link/179273/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='devblogs.microsoft.com', port=443): Max retries exceeded with url: /aspire/aspire-for-javascript-developers/ (Caused by ProxyError('Unable to connect to proxy', RemoteDisconnected('Remote end closed connection without response')))

---

### [Aspire —— 您的技术栈，精简高效](https://aspire.dev/)

**原文标题**: [Aspire â Your stack, streamlined](https://aspire.dev/)

Aspire 13.1 已正式发布，这是一个面向开发者的免费开源平台，旨在通过代码定义和编排应用栈，实现前端、API、容器和数据库的无缝集成与部署，并提供开箱即用的可观测性。

- 🚀 **版本发布**：Aspire 13.1 已正式发布，带来新功能和改进。
- 🆓 **开源免费**：平台完全免费、开源，拥有活跃的开发者社区。
- 💻 **代码定义**：通过类型安全、可读的代码定义整个应用栈，支持本地运行和任意环境部署，无需架构更改。
- 🔧 **模块化扩展**：可轻松编排前端、API、容器和数据库，无需重写代码，并能灵活扩展以适应不同技术栈。
- 👁️ **内置可观测性**：集成 OpenTelemetry，自动提供日志、追踪和健康检查，无需额外配置即可快速调试。
- ☁️ **灵活部署**：支持部署到 Kubernetes、云平台或本地环境，适应性强，确保部署一致性。
- 🌐 **多语言支持**：支持 C#、Java、Python、JavaScript、TypeScript、Go 等多种编程语言。
- 🖥️ **本地优先**：在本地开发环境中模拟生产环境，消除“在我机器上能运行”的问题，实现平滑部署。
- 🔄 **环境一致性**：使用同一模型在不同环境（本地、测试、生产）中运行和部署，通过 CLI 轻松管理。
- 📊 **开发者仪表板**：内置 OpenTelemetry 仪表板，实时监控日志、指标和追踪，集成到工作流中。
- 🔗 **广泛集成**：支持与 Azure、AWS 及自有基础设施等多云环境连接，拥有丰富的集成生态。
- 👥 **用户好评**：受到从独立开发者到企业用户的广泛认可，帮助提升开发效率和部署信心。
- 🛠️ **快速上手**：通过安装 CLI 并查阅文档，即可开始建模、运行和部署应用。

---

### [Aspire 13 | Aspire 的新特性](https://aspire.dev/whats-new/aspire-13/)

**原文标题**: [What's new in Aspire 13 | Aspire](https://aspire.dev/whats-new/aspire-13/)

Aspire 13 标志着 Aspire 产品线的一个重要里程碑，它已从 .NET Aspire 演变为一个全面的多语言应用平台。此版本将 Python 和 JavaScript 提升为一等公民，并引入了多项新功能和改进，包括新的构建和部署管道、现代化的 CLI、VS Code 扩展以及对多语言基础设施的增强支持。

- 🚀 **平台转型**：Aspire 13 从 .NET 编排工具转变为真正的多语言应用平台，Python 和 JavaScript 成为与 .NET 并列的一等公民。
- 🐍 **Python 一流支持**：提供对 Python 模块、uvicorn 部署、灵活的包管理（uv、pip 或 venv）以及自动生成生产 Dockerfile 的全面支持。
- 📜 **JavaScript 一流支持**：支持基于 Vite 和 npm 的应用，具有包管理器自动检测、调试支持和基于容器的构建管道。
- 🔗 **多语言基础设施**：连接属性（URI、JDBC、独立属性）可在任何语言中工作，证书信任跨语言和容器。
- 📦 **容器文件作为构建产物**：引入新的构建范式，构建输出是容器而非文件夹，实现可重现、隔离和可移植的构建。
- ⚙️ **`aspire do` 新平台**：用于构建、发布和部署管道的新平台，支持并行执行、依赖跟踪和可扩展的工作流。
- 🛠️ **现代化 CLI**：新增 `aspire init` 命令以“Aspire 化”现有应用，并改进了跨运行记住配置的部署状态管理。
- 💻 **VS Code 扩展**：通过项目创建、集成管理、多语言调试和部署命令简化 Aspire 开发。
- 🌐 **新官方网站**：Aspire 的新家位于 aspire.dev，提供文档、入门指南和社区资源。
- ⚠️ **重大变更**：Aspire 13.0 是一个包含破坏性变更的主要版本，升级前需查看相关说明，建议使用 `aspire update` 命令进行升级。
- 📄 **简化的 AppHost 模板**：AppHost 项目模板结构简化，SDK 封装了 `Aspire.Hosting.AppHost` 包，项目文件更清晰。
- 🔄 **部署改进**：部署工作流基于 `aspire do` 完全重构，引入部署状态管理，自动持久化 Azure 配置等信息。
- ☁️ **Azure 增强**：引入交互式租户选择，Azure App Service 部署默认包含 Aspire 仪表板，并支持 Application Insights 集成。
- 🧪 **实验性功能**：包括 Dockerfile 构建器 API、C# 文件应用支持、动态输入和管道功能，需明确启用。

---

### [TimescaleDB：排名第一的 PostgreSQL 时序数据库 | 开源与云端 | Tiger Data](https://www.tigerdata.com/timescaledb?utm_source=cooperpress&utm_medium=referral&utm_campaign=node-weekly-newsletter)

**原文标题**: [TimescaleDB: #1 PostgreSQL Time-Series Database | Open Source & Cloud | Tiger Data](https://www.tigerdata.com/timescaledb?utm_source=cooperpress&utm_medium=referral&utm_campaign=node-weekly-newsletter)

TimescaleDB 是基于 PostgreSQL 构建的时序数据库，提供自动分区、行列混合存储、高达 95% 的压缩率、增量物化视图、自动化数据管理和专用时序函数等核心功能，适用于物联网、金融科技和实时分析等场景。其托管云服务 Tiger Cloud 提供弹性扩展、高可用性和安全管理，同时支持自托管部署。

- 🗂️ 自动分区：通过超表实现按时间或 ID 自动分区，支持快速数据摄入和大规模查询优化
- 💾 行列混合存储：结合行存储与列存储，自动转换格式，提升查询性能并降低存储成本
- 📉 高效压缩：采用列式编码技术，压缩率高达 95%，支持在压缩数据上直接过滤和聚合
- 🔄 增量物化视图：通过连续聚合实现增量刷新，支持实时数据更新和分层计算
- 🤖 自动化管理：内置任务调度器，自动处理列存储、数据保留和聚合刷新策略
- ⏱️ 专用时序函数：提供近 200 种超函数，简化高级时序分析并支持部分聚合
- ☁️ 托管云服务：Tiger Cloud 提供弹性计算、分级存储、高可用架构及安全合规支持
- 🏠 自托管选项：支持在自有基础设施部署，包含核心功能但需自行管理扩展与高可用

---

### [选择合适的 Node.js 作业队列](https://judoscale.com/blog/node-task-queues)

**原文标题**: [Choosing the Right Node.js Job Queue](https://judoscale.com/blog/node-task-queues)

现代 Node.js 应用常需执行后台任务，使用任务队列能有效保持 Web 性能。本文比较了多种 Node.js 任务队列方案，帮助开发者根据需求选择合适工具。

- 🐂 **BullMQ**：基于 Redis，功能丰富且性能强大，支持持久化、自动重试和优先级队列，适合大多数应用场景。
- 🐝 **Bee-Queue**：同样基于 Redis，设计简洁轻量，易于上手，但功能较少且近期维护不足。
- 📅 **Agenda**：基于 MongoDB，专注于任务调度（如定时任务），适合已使用 MongoDB 且需定时执行任务的场景。
- 🐰 **消息代理（如 RabbitMQ）**：外部消息队列服务，提供高可靠性和高级消息模式，适合需要强可靠性或不愿自管理基础设施的团队。
- 📈 **自动扩缩容**：通过水平扩展（增加工作进程）或垂直扩展（提升单进程性能）应对负载，推荐使用基于队列延迟的自动扩缩工具（如 Judoscale）。
- 🎯 **选择建议**：优先考虑开发体验和现有技术栈，多数情况下推荐 BullMQ；若已使用特定数据库（如 MongoDB），可选用对应集成方案（如 Agenda）。

---

### [JavaScript 的 for-of 循环实际上很快（V8）| WaspDev 博客](https://waspdev.com/articles/2026-01-01/javascript-for-of-loops-are-actually-fast)

**原文标题**: [JavaScript's for-of loops are actually fast (V8) | WaspDev Blog](https://waspdev.com/articles/2026-01-01/javascript-for-of-loops-are-actually-fast)

JavaScript 的 for-of 循环在现代 V8 引擎中性能已显著提升，通过多种数组类型和大小的基准测试发现，在多数情况下其性能接近传统索引循环，尤其在代码充分预热后表现更佳。

- 🔄 **for-of 循环性能接近传统循环**：基准测试显示，在数组大小为 5000 和 50000 时，for-of 循环与缓存长度的经典 for 循环性能几乎相同。
- 📊 **大规模数组性能波动**：当数组元素达到 500000 时，for-of 循环在初始测试中表现稍差，但经过 200 次重复预热后性能显著提升。
- ⚡ **预热对优化至关重要**：通过 1500 次重复测试，for-of 循环最终与传统循环性能持平，表明 V8 引擎的即时编译优化需要充分预热。
- 🏆 **经典循环仍最稳定**：缓存数组长度的经典 for 循环在所有测试中表现最一致，是性能敏感场景的可靠选择。
- 🚫 **避免使用 for-in 循环**：在所有测试中，for-in 循环性能始终最差，因其涉及额外的属性访问开销。
- 🔧 **forEach 性能中等**：forEach 方法在中小型数组中表现尚可，但在大规模数据下性能落后，且预热对其优化效果有限。

---

### [获取失败](https://nodeweekly.com/link/179279/web)

**原文标题**: [Failed to retrieve](https://nodeweekly.com/link/179279/web)

无法总结：获取内容失败，状态码 403。

---

### [GitHub - WiseLibs/better-sqlite3：Node.js中最快且最简单的SQLite3库。](https://github.com/WiseLibs/better-sqlite3)

**原文标题**: [GitHub - WiseLibs/better-sqlite3: The fastest and simplest library for SQLite3 in Node.js.](https://github.com/WiseLibs/better-sqlite3)

better-sqlite3 是 Node.js 中一个高性能、简单易用的 SQLite 库，以其同步 API 设计提供出色的并发性能，并支持多种高级功能。

- 🚀 **性能卓越**：相比其他 SQLite 库（如 node-sqlite3），在多数操作中速度显著更快，尤其在事务处理方面优势明显
- 🔄 **同步 API**：采用同步接口，简化使用且在某些场景下比异步 API 具有更好的并发性
- 🛡️ **功能全面**：完整支持事务、用户自定义函数、聚合、虚拟表和扩展，兼容 64 位整数和工作线程
- 📦 **易于安装**：通过 npm 即可安装，支持 Node.js v14.21.1 及以上版本，并提供预编译二进制文件
- ⚠️ **适用场景**：适用于大多数 SQLite 使用场景，但在高并发写入、超大数据库（接近 TB 级）或极高数据量读取时可能不适合
- 🔧 **升级注意**：升级时需关注版本变更可能带来的 API 破坏性变化或 SQLite 兼容性问题
- 📄 **开源许可**：采用 MIT 许可证，项目活跃，拥有大量用户和贡献者

---

### [错误](https://nodeweekly.com/link/179281/web)

**原文标题**: [Error](https://nodeweekly.com/link/179281/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='nodeweekly.com', port=443): Max retries exceeded with url: /link/179281/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [发布 v12.6.0 · WiseLibs/better-sqlite3 · GitHub](https://github.com/WiseLibs/better-sqlite3/releases/tag/v12.6.0)

**原文标题**: [Release v12.6.0 · WiseLibs/better-sqlite3 · GitHub](https://github.com/WiseLibs/better-sqlite3/releases/tag/v12.6.0)

better-sqlite3 项目发布了 v12.6.0 版本，主要更新是将 SQLite 升级至 3.51.2 版本。

- 🔄 版本更新：发布了 v12.6.0 版本，由 mceachen 于 1 月 9 日发布。
- ⬆️ 核心升级：将 SQLite 数据库引擎更新至版本 3.51.2。
- 🔗 变更关联：此次更新通过拉取请求 #1436 完成。
- 📊 项目概况：该项目在 GitHub 上拥有 6.8k 星标、435 个复刻，目前有 78 个议题和 16 个拉取请求。
- 🚨 显示问题：页面加载时多次出现错误提示，需要重新加载。
- 👍 社区反馈：版本发布后收到了来自社区成员的点赞（👍）和庆祝（🎉）反应。

---

### [better-sqlite3/docs/api.md 位于 master 分支 · WiseLibs/better-sqlite3 · GitHub](https://github.com/WiseLibs/better-sqlite3/blob/master/docs/api.md)

**原文标题**: [better-sqlite3/docs/api.md at master · WiseLibs/better-sqlite3 · GitHub](https://github.com/WiseLibs/better-sqlite3/blob/master/docs/api.md)

该页面显示了一个名为“better-sqlite3”的 GitHub 仓库界面，但加载时出现错误，提示用户重新加载页面以查看内容。

- 🔄 页面加载错误，需要重新加载才能正常显示
- 📂 这是一个名为“better-sqlite3”的公开 GitHub 仓库
- ⭐ 项目获得了 6.8k 星标，有 435 个复刻
- 🐛 仓库包含 78 个议题和 16 个拉取请求
- 🔔 用户需要登录才能更改通知设置
- 📊 页面提供了代码、议题、拉取请求、讨论、操作、安全和洞察等导航选项

---

### [GitHub - Lulzx/tinypdf：极简PDF生成库。代码少于400行，零依赖，可生成真实PDF文件。](https://github.com/Lulzx/tinypdf)

**原文标题**: [GitHub - Lulzx/tinypdf: Minimal PDF creation library. <400 LOC, zero dependencies, makes real PDFs.](https://github.com/Lulzx/tinypdf)

tinypdf 是一个极简的 PDF 生成库，代码量少于 400 行，无任何依赖，专注于核心的文本和图像添加功能，适用于生成发票、报告等常见文档。

- 📄 **极简轻量** – 库体积仅 3.3KB，无外部依赖，相比 jsPDF 缩小约 70 倍
- 🛠️ **核心功能齐全** – 支持文本、形状、图片、链接、多页面及自定义页面尺寸
- 📝 **Markdown 转换** – 内置将 Markdown 转换为 PDF 的功能，自动处理换行与分页
- 🚫 **专注常用场景** – 去除了字体、SVG、表单等高级特性，覆盖 95% 的基础 PDF 生成需求
- 📦 **简单易用** – 提供清晰的 API，快速集成，示例包含完整的发票生成代码
- ⚖️ **MIT 许可开源** – 可自由使用与修改，项目在 GitHub 上获得广泛关注

---

### [Ohm：适用于 JavaScript 和 TypeScript 的用户友好解析工具包](https://ohmjs.org/)

**原文标题**: [Ohm: a user-friendly parsing toolkit for JavaScript and Typescript](https://ohmjs.org/)

Ohm 是一个基于解析表达式语法（PEG）的解析工具包，包含专用语言和 JavaScript 库，支持快速构建解析器、解释器和编译器，适用于自定义文件格式或编程语言处理。

- ⚙️ 基于解析表达式语法（PEG），提供形式化语法描述能力
- 🔄 完整支持左递归，可自然定义左结合运算符
- 🧩 支持面向对象的语法扩展，便于扩展现有语言
- 📦 采用模块化语义动作设计，实现语法与语义分离
- 🖥️ 提供在线编辑器与可视化工具，支持即时反馈和解析过程交互式呈现
- 🛠️ 已应用于 Shopify 主题工具、Seymour 实时编程环境、Shadama 粒子模拟语言等多个实际项目
- 📚 相关学术成果发表于 SLE 2017、LIVE 2016 等国际会议

---

### [欧姆编辑器](https://ohmjs.org/editor/)

**原文标题**: [Ohm Editor](https://ohmjs.org/editor/)

本文介绍了人工智能在医疗领域的应用现状与前景，重点探讨了其在疾病诊断、药物研发和个性化治疗方面的突破性进展，同时简要提及了相关的伦理挑战。

- 🏥 AI 辅助诊断系统能通过分析医学影像快速识别病变，提升早期癌症等疾病的检出率
- 🔬 机器学习加速了新药研发过程，大幅缩短化合物筛选与临床试验周期
- 📊 基于患者数据的个性化治疗方案正成为现实，AI 能预测药物反应并优化治疗路径
- ⚖️ 数据隐私与算法透明度等伦理问题仍需在技术发展中同步解决

---

### [内存实验室](https://facebook.github.io/memlab/)

**原文标题**: [memlab](https://facebook.github.io/memlab/)

Memlab 是一个用于检测 JavaScript 内存泄漏的端到端测试和分析工具，支持通过自定义测试场景、命令行工具和编程 API 进行内存泄漏的发现与分析。

- 🧪 **定义测试场景**：通过编写 JavaScript 文件来定义浏览器交互的端到端测试，包括指定 URL、执行操作和返回步骤。
- 🖥️ **命令行运行**：使用`memlab run`命令执行自定义测试场景，以发现内存泄漏问题。
- 🔍 **内存分析**：提供多种分析命令，如检查堆中的重复字符串、未绑定对象增长和形状增长等，帮助深入诊断内存问题。
- 📚 **编程 API**：通过 Node.js API 进行内存堆快照的捕获与分析，支持自动化测试和集成到开发流程中。
- 🌐 **实际应用**：已被多个项目和组织用于检测和解决 JavaScript 内存泄漏问题。

---

### [MemLab：一个用于发现 JavaScript 内存泄漏的开源框架](https://engineering.fb.com/2022/09/12/open-source/memlab/)

**原文标题**: [MemLab: An open source framework for finding JavaScript memory leaks](https://engineering.fb.com/2022/09/12/open-source/memlab/)

Meta 开源了 MemLab，这是一个用于自动化检测 JavaScript 内存泄漏的测试框架，旨在帮助开发者识别和解决 Web 应用中的内存问题，提升用户体验和性能优化。

- 🛠️ **开源框架**：MemLab 是 Meta 开源的 JavaScript 内存测试框架，可自动检测内存泄漏，帮助优化客户端内存管理。
- 🌐 **背景与需求**：随着 Facebook.com 等单页应用（SPA）的普及，客户端内存管理变得复杂，内存泄漏虽不易察觉但会逐渐影响性能。
- 🔍 **工作原理**：通过无头浏览器运行测试场景，比较 JavaScript 堆快照，经过六步流程（如浏览器交互、堆差异分析、保留路径追踪）来定位泄漏对象。
- 📊 **核心功能**：包括内存泄漏检测、堆的图视图 API（支持自定义泄漏过滤器）、内存断言（用于 Node.js/Jest 测试）及内存工具箱（如对象形状分析、重复字符串检测）。
- 📈 **应用案例**：在 Meta 内部，MemLab 帮助将 Facebook.com 的 OOM 崩溃减少 50%，并通过 React Fiber 节点清理和 Relay 字符串驻留优化，显著降低了内存使用。
- 🚀 **社区推广**：开发者可通过 npm 安装 MemLab，并参考快速入门指南使用，Meta 鼓励社区反馈以拓展应用场景。

---

### [pnpm 10.28 | pnpm](https://pnpm.io/blog/releases/10.28)

**原文标题**: [pnpm 10.28 | pnpm](https://pnpm.io/blog/releases/10.28)

pnpm 10.28 版本引入了新的 beforePacking 钩子，允许在发布时自定义 package.json，同时优化了过滤安装的性能，并修复了若干错误。

- 🎣 新增 beforePacking 钩子，可在发布前修改 package.json 内容，不影响本地文件
- ⚡ 修复过滤安装性能问题，使其速度与完整安装相当或更快
- 🔗 修复项目存储库中符号链接的创建逻辑，避免在特定目录结构下产生冗余
- ⚙️ 支持在 pnpm-workspace.yaml 中声明 requiredScripts 设置

---

### [发布 v6.2.0 · actions/setup-node · GitHub](https://github.com/actions/setup-node/releases/tag/v6.2.0)

**原文标题**: [Release v6.2.0 · actions/setup-node · GitHub](https://github.com/actions/setup-node/releases/tag/v6.2.0)

该内容是关于 GitHub Actions 中 setup-node 项目 v6.2.0 版本的发布信息，主要包含文档更新、依赖升级及新贡献者的加入。

- 📄 文档更新涉及锁文件缺失、镜像选项拼写修正及版本说明优化
- ⬆️ 依赖项升级了@actions/cache 至 v5.0.1 版本
- 👋 新增六位首次贡献者参与项目改进
- 🏷️ 版本从 v6 升级至 v6.2.0，包含多项功能完善
- 🔄 发布过程中出现页面加载错误提示需重新刷新

---

### [GitHub - dahlia/logtape：适用于Deno、Node.js、Bun、浏览器及边缘函数的零依赖无侵入日志库](https://github.com/dahlia/logtape)

**原文标题**: [GitHub - dahlia/logtape: Unobtrusive logging library with zero dependencies for Deno, Node.js, Bun, browsers, and edge functions](https://github.com/dahlia/logtape)

LogTape 是一个专为 JavaScript 和 TypeScript 设计的日志库，采用库优先理念，无需配置即可在库中安全使用，同时为应用程序提供完全控制。它无依赖，支持 Deno、Node.js、Bun、浏览器和边缘函数等多种运行时。

- 🚀 **零依赖**：无需担心依赖问题，轻量且易于集成。
- 📚 **库友好设计**：专为库和应用程序设计，库开发者可安全添加日志功能。
- 🌐 **多运行时支持**：兼容 Deno、Node.js、Bun、浏览器及边缘函数，代码无需修改。
- 🏗️ **结构化日志**：支持记录带结构化数据的日志消息，便于处理和分析。
- 📊 **分层分类系统**：通过层级分类管理日志记录器，可灵活控制不同级别的日志详细程度。
- 🧩 **模板字面量**：支持使用模板字面量记录日志，方便插入占位符和值。
- 🔒 **内置数据脱敏**：提供基于模式或字段的敏感信息脱敏功能，增强安全性。
- 🔌 **简单接收器**：可轻松添加自定义接收器，扩展日志输出目标。
- 🛠️ **框架集成**：为 Express、Fastify、Hono、Koa 和 Drizzle ORM 等流行框架提供一流集成，支持自动 HTTP 请求和数据库查询日志记录。
- 📦 **模块化包结构**：核心包为 `@logtape/logtape`，另有多个适配器和集成包（如 CloudWatch、Sentry、OpenTelemetry 等）可供选择。
- 📄 **安装灵活**：可通过 JSR 或 npm 安装，支持 Deno、npm、pnpm、Yarn 和 Bun 等多种包管理器。
- 📖 **详细文档**：完整文档和 API 参考可在 logtape.org 和 jsr.io 上获取。

---

### [logtape/CHANGES.md 位于主分支 · dahlia/logtape · GitHub](https://github.com/dahlia/logtape/blob/main/CHANGES.md#version-200)

**原文标题**: [logtape/CHANGES.md at main · dahlia/logtape · GitHub](https://github.com/dahlia/logtape/blob/main/CHANGES.md#version-200)

该页面显示了一个 GitHub 仓库的界面，但加载时出现错误提示，需要重新加载页面才能正常访问。

- 🔄 页面加载出错，提示重新加载
- 🔐 需要登录才能更改通知设置
- 📊 仓库拥有 1.5k 星标和 38 个分支
- 🐛 当前有 4 个未解决的问题
- 🔀 存在 6 个拉取请求待处理
- 🛡️ 页面提供安全功能选项
- 📈 可查看仓库的洞察数据分析

---

### [GitHub - openai/openai-node: OpenAI API 官方 JavaScript / TypeScript 库](https://github.com/openai/openai-node)

**原文标题**: [GitHub - openai/openai-node: Official JavaScript / TypeScript library for the OpenAI API](https://github.com/openai/openai-node)

OpenAI Node.js 库是官方提供的 JavaScript/TypeScript 库，用于便捷访问 OpenAI REST API，支持多种运行时环境，并包含丰富的功能如流式响应、文件上传和错误处理。

- 📦 **官方库与安装** – 提供 npm 和 JSR 安装方式，支持 TypeScript 和 JavaScript。
- 🔌 **核心 API 使用** – 包含 Responses API 和 Chat Completions API，用于生成文本和对话。
- 🌊 **流式响应支持** – 通过 Server Sent Events (SSE) 实现实时流式输出。
- 📁 **多种文件上传方式** – 支持 File、fetch Response、fs.ReadStream 和 toFile 辅助方法。
- 🔐 **Webhook 验证** – 提供签名验证和解析功能，确保 webhook 请求的安全性。
- 🚨 **错误处理机制** – 针对不同 HTTP 状态码抛出特定错误类型，便于调试。
- 🔄 **自动重试与超时设置** – 默认对连接错误和特定状态码进行重试，可配置超时时间。
- 📄 **自动分页功能** – 支持通过 for await…of 语法或手动分页获取列表数据。
- 🌐 **实时 API 支持** – 通过 WebSocket 实现低延迟、多模态的实时对话体验。
- ☁️ **Azure OpenAI 集成** – 提供 AzureOpenAI 类以支持微软 Azure 平台。
- 🛠️ **高级功能** – 包括原始响应访问、自定义日志记录、代理配置和非文档化请求支持。
- ⚙️ **环境与要求** – 支持 Node.js、Deno、Bun 等运行时，需谨慎启用浏览器端支持。

---

### [GitHub - photostructure/exiftool-vendored.js: 快速、跨平台的 Node.js 访问 ExifTool](https://github.com/photostructure/exiftool-vendored.js)

**原文标题**: [GitHub - photostructure/exiftool-vendored.js: Fast, cross-platform Node.js access to ExifTool](https://github.com/photostructure/exiftool-vendored.js)

这是一个用于 Node.js 的快速、跨平台的 ExifTool 封装库，由 PhotoStructure 构建和支持，提供读取、写入和提取图像元数据的功能。

- 📦 **高性能封装**：相比其他 Node.js ExifTool 模块快一个数量级，已用于 PhotoStructure 及 1000 多个项目
- 🔧 **跨平台支持**：兼容 macOS、Linux 和 Windows 系统，功能全面且经过充分测试
- 📚 **开发者友好**：提供完整的 TypeScript 类型定义，支持数千个元数据字段的智能日期处理
- 📖 **丰富功能**：支持读取、写入元数据，提取缩略图、预览图和 RAW 文件中的 JPEG 图像
- ⚙️ **灵活配置**：提供库级全局设置和实例级选项，可调整并发进程数等参数
- ⏰ **智能时区**：使用多种启发式方法处理图像中通常缺失的时区信息
- 🧹 **资源管理**：支持自动资源清理，推荐在长运行应用中使用`.end()`进行优雅关闭
- 🏷️ **标签完整**：基于真实相机样本自动生成标签接口，包含 2500 多个元数据字段
- 📈 **高性能处理**：通过多进程配置可实现每秒处理 500+ 文件的高吞吐量

---

### [发布 v4.8.0 · NodeBB/NodeBB · GitHub](https://github.com/NodeBB/NodeBB/releases/tag/v4.8.0)

**原文标题**: [Release v4.8.0 · NodeBB/NodeBB · GitHub](https://github.com/NodeBB/NodeBB/releases/tag/v4.8.0)

NodeBB 发布了 v4.8.0 版本，主要引入了跨帖子功能、联邦活动增强、权限掩码支持及多项错误修复与优化。

- 🚀 新增跨帖子功能，支持用户将主题跨类别发布，并引入相关前端界面与 API
- 🔗 联邦功能增强，包括用户跨帖子作为“宣布”活动联邦、支持远程“不喜欢”活动等
- 🛡️ 引入权限掩码支持，优化类别级别的权限查询与管理
- 🐛 修复多项错误，包括 i18n 回退、自定义表情符号处理、跨帖子逻辑问题等
- 🔧 进行代码重构与测试更新，确保跨帖子与自动分类等功能的稳定性
- 📦 包含依赖更新与资产调整，提升系统整体性能与兼容性

---

### [注册 - Auth0](https://auth0.com/signup?onboard_app=auth_for_aa&ocid=701KZ000000cXXxYAM_aPA4z0000008OZeGAM?utm_source=cooperpress&utm_campaign=amer_namer_usa_all_ciam_dev_dg_plg_auth0_native_cooperpress_native_aud_jan_2026_placements_utm2&utm_medium=cpc&utm_id=aNKWR000002m8zp4AA)

**原文标题**: [Sign Up - Auth0](https://auth0.com/signup?onboard_app=auth_for_aa&ocid=701KZ000000cXXxYAM_aPA4z0000008OZeGAM?utm_source=cooperpress&utm_campaign=amer_namer_usa_all_ciam_dev_dg_plg_auth0_native_cooperpress_native_aud_jan_2026_placements_utm2&utm_medium=cpc&utm_id=aNKWR000002m8zp4AA)

Auth0 注册页面提供免费账户创建，包含多项安全与开发功能。

- 🔐 免费套餐支持高达 2.5 万月活跃用户
- ⚙️ 可自定义注册和登录流程
- 🤖 新增 AI 代理连接外部应用及敏感操作的人工审批功能
- 🔗 支持自定义社交登录和无密码连接
- 🛡️ 提供暴力破解防护和渐进式用户画像分析（含 5 种操作与表单）
- 👩‍💻 专为各阶段开发者设计
- 📧 注册需同意隐私政策，可选择接收营销信息
- 🔄 支持 GitHub、Google、Microsoft 账户快速登录

---

### [密歇根 TypeScript 创始人成功在 Ty...内运行《毁灭战士》](https://socket.dev/blog/typescript-types-running-doom)

**原文标题**: [Michigan TypeScript Founder Successfully Runs Doom Inside Ty...](https://socket.dev/blog/typescript-types-running-doom)

研究人员发现一款恶意 Chrome 扩展程序会窃取新创建的 MEXC 交易所 API 密钥，通过 Telegram 外传数据，并获取账户完全控制权以进行交易和提现操作。

- 🕵️ 恶意扩展程序针对 MEXC 交易所用户，专门窃取新生成的 API 密钥
- 📤 窃取的密钥通过 Telegram 渠道外传至攻击者控制的服务器
- 💸 攻击者可获得账户完全控制权限，包括交易和资金提现功能
- ⚠️ 该安全事件由安全研究员 Kirill Boychenko 于 2026 年 1 月 12 日披露

---

### [技术深度探索 | 用 TypeScript 类型实现《毁灭战士》 - YouTube](https://www.youtube.com/watch?v=9gqj7q1aEFs)

**原文标题**: [Technical Deep Dive | Doom in TypeScript types - YouTube](https://www.youtube.com/watch?v=9gqj7q1aEFs)

该页面为 YouTube 网站的页脚导航部分，列出了平台的关键政策、功能说明及法律信息。

- 📄 关于平台的基本信息与介绍
- 📢 媒体与新闻相关资源
- ©️ 版权声明与知识产权说明
- 📞 联系与反馈渠道
- 🧑‍🎨 创作者相关资源与服务
- 📢 广告合作与商业推广
- 👨‍💻 开发者工具与资源
- ⚖️ 服务条款与使用协议
- 🔒 隐私保护政策与措施
- ⚙️ 平台政策与安全指南
- 🔧 YouTube 功能运作说明
- 🆕 新功能测试与体验
- 🏢 公司版权与年份标识（谷歌 2026）

---

### [GitHub - gibbok/typescript-book: 《简明 TypeScript 手册》：TypeScript 高效开发的简明指南。免费开源。](https://github.com/gibbok/typescript-book)

**原文标题**: [GitHub - gibbok/typescript-book: The Concise TypeScript Book: A Concise Guide to Effective Development in TypeScript. Free and Open Source.](https://github.com/gibbok/typescript-book)

《The Concise TypeScript Book》是一本免费开源的 TypeScript 简明指南，全面覆盖 TypeScript 5.2 的核心概念与高级特性，适合从初学者到有经验的开发者使用。本书强调通过类型系统提升代码质量，并提供了从安装配置到类型操作、类与装饰器等实用内容。

- 📚 **开源免费** – 本书完全免费开源，支持多语言翻译（包括中文、意大利文），并提供 Epub 和在线版本
- 🛠️ **全面覆盖** – 从基础类型、类型系统、类、泛型到装饰器、异步特性等高级主题均有详细讲解
- 🧩 **类型系统深入** – 详细解释结构类型、类型推断、类型收窄、条件类型等核心概念，帮助开发者编写健壮代码
- ⚙️ **实用配置指南** – 包含 TypeScript 安装、tsconfig.json 配置、迁移建议及现代 JavaScript 特性支持
- 🧪 **高级特性** – 涵盖装饰器、泛型约束、可变元组类型、模板字面量类型等 TypeScript 5.x 新功能
- 🔗 **资源丰富** – 提供类型定义（@types）使用、JSX 支持、模块解析及错误处理等实际开发技巧
- 📖 **持续更新** – 作者积极维护，内容随 TypeScript 版本更新，并可通过赞助支持项目发展

---

### [@deno.land 在 Bluesky 上](https://bsky.app/profile/deno.land/post/3mbuirnjqxc22)

**原文标题**: [@deno.land on Bluesky](https://bsky.app/profile/deno.land/post/3mbuirnjqxc22)

这是一个关于 JavaScript 商标争议和 Bluesky 社交平台技术基础的说明，其中涉及法律程序和技术要求。

- 🚫 该网页应用高度依赖 JavaScript，无法在禁用 JavaScript 的环境下运行
- 🔗 相关资源可访问 Bluesky 官网 bsky.social 及其技术协议网站 atproto.com
- 📝 内容发布平台为 Deno 开发的 deno.land
- ⚖️ Oracle 已获准将 JavaScript 商标撤销案延期 60 天审理
- 🧾 Mozilla 正通过大量行业证据证明“JavaScript”已成为通用术语，与 Oracle 产品无关
- ⏰ 案件当前处于证据开示阶段，最新进展更新于 2026 年 1 月 7 日

---

