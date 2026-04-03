### [Node 周刊第 618 期：2026 年 4 月 2 日](https://nodeweekly.com/issues/618)

**原文标题**: [Node Weekly Issue 618: April 2, 2026](https://nodeweekly.com/issues/618)

本期 Node Weekly 简报涵盖 Node.js 25.9.0 发布、Axios 供应链攻击分析、npm 工作空间指南、AI 工具更新及多个开发工具发布。

- 🚀 Node.js 25.9.0 发布：新增`--max-heap-size`堆内存控制选项，实验性 stream/iter 流 API 落地，测试运行器模块模拟功能改进
- 🔒 Axios 供应链攻击影响分析：探讨攻击机制及远超预期的辐射范围，附 npm 等包管理器"最小发布冷却期"缓解指南
- 📦 npm 工作空间入门指南：详解单仓库多包管理方案，支持本地包链接与依赖提升去重
- 🤖 AI 开发工具更新：Transformers.js v4 支持 WebGPU 运行 Hugging Face 模型，Vercel AI SDK 构建智能体教程
- 🛠️ 安全与性能工具：node-re2 集成 Google 防 ReDoS 正则库，dotenv 17.4 环境变量管理，Bun 替换 Node 实现 5 倍吞吐案例
- 🌐 生态动态：Cloudflare 发布 EmDash 建站工具，Deno v2.7.11 增强 Node 兼容性，wasm-git 提供 WebAssembly 版 Git 操作

---

### [Node.js — Node.js 25.9.0（当前版本）](https://nodejs.org/en/blog/release/v25.9.0)

**原文标题**: [Node.js — Node.js 25.9.0 (Current)](https://nodejs.org/en/blog/release/v25.9.0)

Node.js 25.9.0 版本发布，主要改进了测试运行器的模块模拟功能，并引入了多项新特性与优化，包括 AsyncLocalStorage 的作用域支持、新的命令行选项、加密算法增强以及 REPL 和流模块的改进。

- 🧪 测试运行器模块模拟选项 `MockModuleOptions.defaultExport` 和 `MockModuleOptions.namedExports` 合并为 `MockModuleOptions.exports`，以符合用户预期并与其他测试运行器保持一致。
- 🔗 `async_hooks` 模块为 `AsyncLocalStorage` 新增了 `using` 作用域支持，便于资源管理。
- ⚙️ 命令行新增 `--max-heap-size` 选项，允许用户设置最大堆大小。
- 🔐 `crypto` 模块添加了 TurboSHAKE 和 KangarooTwelve Web Cryptography 算法支持。
- 🖥️ REPL 增加了可自定义的错误处理功能，并移除了对 `node:domain` 模块的依赖。
- 📦 SEA（Single Executable Applications）支持为 ESM 入口点生成代码缓存，提升启动性能。
- 🌊 `stream` 模块新增了 `stream/iter` 实现，提供了迭代器接口。
- 🛠️ 包含多项错误修复、性能优化及依赖项更新（如 npm 升级至 11.12.1，V8 引擎更新等）。

---

### [我们值得为 JavaScript 拥有一个更好的流 API。](https://blog.cloudflare.com/a-better-web-streams-api/)

**原文标题**: [We deserve a better streams API for JavaScript](https://blog.cloudflare.com/a-better-web-streams-api/)

本文探讨了当前 Web Streams API 存在的根本性可用性和性能问题，并提出了一种基于现代 JavaScript 语言特性的替代方案。该方案通过简化设计、利用异步迭代和明确背压策略，显著提升了性能，并在多个运行时中展现出 2 倍至 120 倍的性能提升。

- 🚀 **性能瓶颈**：Web Streams API 因设计复杂、过度依赖 Promise 和锁机制，导致高开销和性能问题，尤其在服务器端和高频场景下表现不佳。
- 🔄 **异步迭代支持不足**：API 设计早于 ES2018 的异步迭代，导致使用模式繁琐，如手动获取读取器、管理锁和复杂的`{ value, done }`协议。
- 🔒 **锁机制易出错**：手动锁管理（如`getReader()`和`releaseLock()`）容易导致流被永久锁定或资源泄漏，增加开发复杂度。
- 🛠️ **BYOB 复杂度高**：BYOB（自带缓冲区）读取 API 复杂且使用率低，增加了实现和使用的难度，而实际优化收益有限。
- ⚖️ **背压机制缺陷**：背压信号（如`desiredSize`）仅为建议性，缺乏强制执行力，容易导致内存无界增长，尤其在`tee()`和`TransformStream`中问题突出。
- 🧩 **实现优化困难**：各运行时（如 Node.js、Deno、Bun）需依赖非标准内部优化来提升性能，导致行为不一致和可移植性问题。
- 💡 **替代方案核心**：提出以异步迭代为基础的新 API，强调流即迭代、拉取式转换、明确背压策略和批处理块，简化设计并提升性能。
- ⚡ **性能对比显著**：新方案在基准测试中表现优异，如链式转换场景提升 80-90 倍，归功于拉取语义和同步快速路径的引入。
- 🔗 **兼容与迁移**：新 API 可与现有 Web Streams 互操作，提供同步和异步版本，支持逐步迁移，并已在 GitHub 发布参考实现供社区试用。

---

### [可迭代流 | Node.js v25.9.0 文档](https://nodejs.org/docs/latest/api/stream_iter.html#iterable-streams)

**原文标题**: [Iterable Streams | Node.js v25.9.0 Documentation](https://nodejs.org/docs/latest/api/stream_iter.html#iterable-streams)

Node.js 的 `node:stream/iter` 模块提供了一种基于可迭代协议（而非传统事件驱动或 Web Streams API）的流处理方式，将数据表示为 `Uint8Array` 批处理，支持拉取和推送两种模型，并包含丰富的转换、消费和工具函数。

- 🧪 **实验性功能**：该模块目前处于实验阶段，需通过 `--experimental-stream-iter` CLI 标志启用。
- 🔄 **基于可迭代协议**：流数据表示为 `AsyncIterable<Uint8Array[]>` 或 `Iterable<Uint8Array[]>`，无需继承特定基类，任何实现可迭代协议的对象均可参与。
- 📦 **批处理数据**：每次迭代产生一个 `Uint8Array[]` 批次，以分摊异步操作开销，提升性能。
- ⚙️ **灵活的转换器**：支持无状态函数或有状态对象（含 `transform` 方法）作为转换器，可处理压缩、加密等需跨批次缓冲的操作。
- ⏳ **支持拉取与推送模型**：`pull()` 实现按需拉取的数据流，自然具备背压；`push()` 允许显式写入数据，需通过 `highWaterMark` 和 `backpressure` 选项管理背压。
- 🚦 **多种背压策略**：提供 `strict`（默认）、`block`、`drop-oldest` 和 `drop-newest` 四种策略，分别适用于严格防内存增长、传统阻塞、保留最新数据和丢弃新数据等场景。
- 🔧 **丰富的工具函数**：包括 `from()` 创建源流、`pipeTo()` 构建管道、`text()`/`bytes()` 等消费者函数，以及 `merge()`、`tap()`、`broadcast()`、`share()` 等高级功能。
- 🔗 **协议符号集成**：通过 `Stream.toAsyncStreamable` 等协议符号，允许第三方对象无缝集成到流处理管道中，无需直接导入模块。
- 📚 **同步与异步版本**：关键函数如 `from()`、`pull()`、`text()` 等均提供同步（`Sync`后缀）和异步版本，适应不同场景需求。

---

### [使用 Memetria K/V 构建 — Memetria](https://dashboard.memetria.com/nodeweekly/)

**原文标题**: [Build with Memetria K/V — Memetria](https://dashboard.memetria.com/nodeweekly/)

Memetria 是一个提供兼容 Valkey 和 Redis OSS 的键值存储托管服务平台，支持无缝扩展、加密连接和详细监控，并提供从开发到高性能的多层级定价方案。

- 🗄️ 兼容 Valkey 和 Redis OSS，支持轻松导入导出数据
- 📈 支持无缝扩展，调整规模无需停机
- 🔐 提供双重和仅 TLS 加密连接选项
- 📊 具备详细的健康、内存和性能监控图表
- 💰 提供三种主要方案：开发版（$14/月起）、生产版（$89/月起）和性能版（$779/月起），各含不同资源配置
- 🌍 支持多个 AWS 区域部署，包括亚洲、欧洲、美洲等地
- 📝 注册需同意服务条款、隐私政策和最终用户许可协议

---

### [Axios 妥协的隐秘冲击范围 - Socket](https://socket.dev/blog/hidden-blast-radius-of-the-axios-compromise)

**原文标题**: [The Hidden Blast Radius of the Axios Compromise - Socket](https://socket.dev/blog/hidden-blast-radius-of-the-axios-compromise)

Axios 维护者确认 npm 包被篡改事件源于社会工程学攻击，揭示了针对维护者的攻击如何绕过安全控制并威胁软件供应链安全。

- 🎭 攻击者通过社会工程学手段获取 Axios 维护者账户权限
- 🔓 利用维护者身份绕过 npm 的双因素认证等安全控制
- 📦 成功发布包含恶意代码的 Axios 测试版本（0.0.1-berzerk）
- ⛓️ 事件暴露软件供应链中维护者账户的薄弱环节
- 🛡️ 凸显需要加强开源项目维护者的账户安全防护
- ⏱️ 攻击发生在 2026 年 4 月 2 日，被迅速发现并修复

---

### [Axios 供应链攻击：恶意依赖包被植入...](https://socket.dev/blog/axios-npm-package-compromised)

**原文标题**: [Supply Chain Attack on Axios Pulls Malicious Dependency from...](https://socket.dev/blog/axios-npm-package-compromised)

攻击者通过 PyPI 平台发布恶意版本的 Telnyx Python SDK，利用供应链攻击窃取用户凭证。

- 🐍 恶意 Python 包伪装成 Telnyx 官方 SDK，通过 PyPI 平台传播
- 🔗 采用多阶段供应链攻击，依赖链中隐藏恶意代码
- 📦 软件包下载后执行凭证窃取程序，收集敏感信息
- ⚠️ 攻击组织 TeamPCP 疑似专业黑客团队，持续活跃
- 🔍 Socket 研究团队于 2026 年 3 月 27 日发现并披露该威胁

---

### [axios 在 npm 上遭入侵 - 恶意版本植入远程访问木马 - StepSecurity](https://www.stepsecurity.io/blog/axios-compromised-on-npm-malicious-versions-drop-remote-access-trojan#am-i-affected)

**原文标题**: [axios Compromised on npm - Malicious Versions Drop Remote Access Trojan - StepSecurity](https://www.stepsecurity.io/blog/axios-compromised-on-npm-malicious-versions-drop-remote-access-trojan#am-i-affected)

2026 年 3 月 30 日，StepSecurity 发现 npm 上发布的两个恶意 axios 版本（1.14.1 和 0.30.4）。攻击者通过劫持维护者账户，注入了一个隐藏依赖（plain-crypto-js@4.2.1），该依赖在安装后执行脚本，投放跨平台远程访问木马（RAT），并能在感染后自我清除痕迹。

- 🚨 **恶意版本发布** - 攻击者通过劫持的 axios 维护者账户（jasonsaayman）发布了恶意版本 axios@1.14.1 和 axios@0.30.4。
- 🔗 **隐藏依赖注入** - 恶意版本注入了一个从未在 axios 源码中使用的依赖包 plain-crypto-js@4.2.1，其唯一目的是通过 postinstall 脚本触发攻击。
- 🐛 **RAT 投放机制** - 该依赖的 postinstall 脚本（setup.js）是一个经过混淆的投放器，会根据操作系统（macOS、Windows、Linux）下载并执行相应的第二阶段 RAT 载荷。
- 🕵️ **反取证设计** - 攻击执行后，恶意脚本会删除自身，并用一个干净的版本存根（package.md）替换 package.json，以掩盖攻击痕迹。
- ⏱️ **精准攻击时间线** - 攻击经过了精心策划：恶意依赖包提前 18 小时发布，两个 axios 恶意版本在 39 分钟内相继发布，均在约 3 小时后被 npm 下架。
- 🌐 **C2 通信与检测** - 投放器会联系攻击者的命令与控制服务器（sfrclak.com:8000）。StepSecurity 的 Harden-Runner 在 CI/CD 流程中检测到了此次异常外联。
- 🔍 **影响与检测** - 如果系统安装了 axios@1.14.1 或 axios@0.30.4，或存在 node_modules/plain-crypto-js 目录，则应视为已受影响。
- 🛡️ **缓解与建议** - 建议立即降级到安全版本（如 axios@1.14.0），检查并清理系统，在 CI/CD 中使用--ignore-scripts 标志，并考虑实施包版本发布冷却期策略。

---

### [最低发布年龄：供应链防御中被低估的一环 | 丹尼·阿卡什](https://daniakash.com/posts/simplest-supply-chain-defense/)

**原文标题**: [Minimum Release Age is an Underrated Supply Chain Defense | Dani Akash](https://daniakash.com/posts/simplest-supply-chain-defense/)

设置最低发布年龄是一种被低估的软件供应链防御策略，通过延迟安装新发布的包版本，可以自动过滤掉大多数短期恶意攻击，因为这类攻击通常在几小时到几天内就会被发现并下架。

- 🛡️ **axios 等攻击案例**：2026 年 3 月的 axios 供应链攻击中，恶意版本仅存活 4 小时就被下架，若设置 7 天发布延迟即可完全避免安装。
- 📊 **历史数据分析**：回顾过去 8 年 21 起知名供应链事件，7 天延迟策略能成功拦截其中 11 起短期恶意发布攻击，并缩短另外 2 起的暴露窗口。
- ⏳ **防御原理**：大多数恶意包攻击属于“打了就跑”模式，从发布到被社区发现通常只需数小时，7 天等待期让包先经受社区检验。
- 🔧 **配置方式**：主流 JavaScript 包管理器（Bun/npm/pnpm/Yarn）及 Python 的 uv/pip 均已支持该功能，但配置参数和单位不统一。
- ⚠️ **适用场景**：最适合使用语义化版本范围并定期更新的项目，对内部包或紧急安全更新需设置例外。
- 🚫 **局限性**：无法防御长期渗透（如 XZ Utils）、维护者蓄意破坏、构建系统入侵、CDN 劫持或合法代码漏洞（如 Log4Shell）。
- 🌐 **生态支持差异**：JavaScript 和 Python 生态支持较好，Go/Java/PHP/Ruby 等生态尚无原生支持。
- 🔄 **自动化集成**：Renovate 和 Dependabot 等依赖更新工具支持延迟机制，并自动豁免安全更新。
- 📝 **标准化呼吁**：各工具配置参数命名和单位混乱，需要行业统一规范以提升可用性。
- 💡 **建议行动**：支持该功能的包管理器应考虑将 7 天延迟设为默认值，开发者应主动配置此基础防御层。

---

### [2026 年发布至 npm · GitHub](https://gist.github.com/kettanaito/debde3cabfae4f68d37cf0f8f3a6a666)

**原文标题**: [Publishing to npm in 2026 · GitHub](https://gist.github.com/kettanaito/debde3cabfae4f68d37cf0f8f3a6a666)

该文章介绍了在 2026 年使用 GitHub Actions 自动化发布 npm 包的完整流程，重点包括设置访问令牌、配置工作流权限以及启用可信发布和双因素认证等安全措施。

- 🚀 发布前需生成具有读写权限的 npm 访问令牌，并在 GitHub 仓库中设置为密钥
- 🔧 在 package.json 中配置 publishConfig.access 为"public"，并可选设置 repository.url 以支持来源证明
- 🛡️ 在 GitHub Actions 工作流中设置 permissions.id-token 为 write，启用可信发布功能
- ⚙️ 首次发布需在 actions/setup-node 中配置 always-auth 和 registry-url 参数
- 🔐 发布后删除临时令牌，在 npm 包设置中添加可信发布者并启用双因素认证保护
- 💬 有用户评论表示该流程步骤较多，对每个包都需重复操作

---

### [克劳德代码源泄露：虚假工具、令人沮丧的正则表达式、卧底模式及其他 | 亚历克斯·金的博客](https://alex000kim.com/posts/2026-03-31-claude-code-source-leak/)

**原文标题**: [The Claude Code Source Leak: fake tools, frustration regexes, undercover mode, and more | Alex Kim's blog](https://alex000kim.com/posts/2026-03-31-claude-code-source-leak/)

Anthropic 意外泄露了 Claude Code 的完整源代码，揭示了多项内部功能和技术细节，包括反蒸馏机制、隐身模式、客户端认证等，暴露了产品路线图和潜在安全风险。

- 🕵️♂️ **反蒸馏机制**：通过注入虚假工具定义污染竞争对手的训练数据，并采用服务器端文本摘要技术保护推理链。
- 🎭 **隐身模式**：强制 AI 在外部项目中隐藏所有 Anthropic 内部痕迹，包括避免提及内部代号和工具名称。
- 😤 **用户挫折检测**：使用正则表达式识别用户不满情绪，以低成本实现情感分析。
- 🔐 **原生客户端认证**：在 JavaScript 运行时下层实现加密哈希验证，确保请求来自正版客户端。
- 💸 **API 调用浪费**：因自动压缩功能故障导致每日约 25 万次 API 调用浪费，已通过限制失败次数修复。
- 🤖 **未发布的自主代理模式**：代码中出现了名为 KAIROS 的未发布功能，具备后台运行、记忆蒸馏等高级能力。
- 🎮 **隐藏的彩蛋功能**：包含类似电子宠物的伴侣系统，以及为愚人节准备的玩笑功能。
- 🛡️ **严格的安全检查**：对 bash 命令执行 23 项安全检查，包括防御 Zsh 特定攻击向量。
- 📊 **提示缓存优化**：采用游戏引擎技术优化终端渲染，并通过精细的缓存管理降低 API 成本。
- 🐛 **泄露根源**：可能源于 Anthropic 收购的 Bun 工具链中已知的源码映射文件服务漏洞。

---

### [Bun 前端开发服务器 - 生产环境下源映射服务异常 · 第 28001 号问题 · oven-sh/bun · GitHub](https://github.com/oven-sh/bun/issues/28001)

**原文标题**: [Bun's frontend development server - Source map incorrectly served when in production · Issue #28001 · oven-sh/bun · GitHub](https://github.com/oven-sh/bun/issues/28001)

Bun 前端开发服务器在生产模式下错误地提供了源映射文件，这是一个已报告的问题。

- 🐛 用户在使用 Bun 的`Bun.serve`函数并设置`development: false`时，服务器仍然为 JavaScript 文件提供源映射
- 🔍 问题复现步骤包括创建一个简单的服务器、HTML 文件和包含错误的 JS 文件，访问页面后发现 JS 代码被捆绑且附带了源映射 URL
- 📄 根据 Bun 官方文档，生产模式下应禁用源映射，但实际行为与预期不符
- 🏷️ 该问题已被标记为“bug”和“needs triage”，表明它是一个待确认和处理的故障
- ⚙️ 环境信息显示用户使用的是 Bun 1.3.10 版本和 Windows 操作系统

---

### [源映射：通过标准发布功能 | 彭博 JS 博客](https://bloomberg.github.io/js-blog/post/standardizing-source-maps/)

**原文标题**: [Source Maps: Shipping Features Through Standards | Bloomberg JS Blog](https://bloomberg.github.io/js-blog/post/standardizing-source-maps/)

Source Maps 是现代 Web 开发的关键工具，用于将编译、压缩后的代码映射回原始源代码，以方便调试。文章回顾了其发展历程，从最初的非标准格式到 2024 年成为 ECMA-426 标准，并介绍了其工作原理、核心字段（如 mappings 的编码方式）以及未来的新特性提案（如 Scopes 和 Range Mappings）。

- 🗺️ **Source Maps 的作用**：在复杂 Web 开发中，将优化、压缩后的生成代码映射回原始源代码，使开发者能在浏览器调试工具中直接查看和调试原始代码。
- 📜 **发展历程**：最初十年没有官方标准，依赖共享文档协作；2023 年成立 TC39-TG4 任务组，2024 年正式标准化为 ECMA-426。
- 🔍 **文件结构**：Source Map 是一个 JSON 文件，包含版本、源文件列表、映射数据（mappings 字段使用 Base64 VLQ 编码）等关键字段。
- ⚙️ **映射原理**：Revision 3 改用基于段的映射和相对编码，大幅减小文件体积，仅记录映射发生变化的位点，而非每个字符。
- 🚀 **新特性演进**：在缺乏标准时，通过 x_ 前缀（如 x_google_ignoreList）实验性添加功能；标准化后，正提案 Scopes（提供作用域和变量信息）和 Range Mappings（提高映射精度）等新特性。
- 🤝 **社区协作**：标准化过程汇聚了 Bloomberg、Google、Mozilla 等公司的工程师，体现了开源生态的合作精神，旨在为工具开发者和使用者提供更稳定、可扩展的基础。

---

### [介绍 EmDash——WordPress 的精神继承者，解决插件安全难题](https://blog.cloudflare.com/emdash-wordpress/)

**原文标题**: [Introducing EmDash â the spiritual successor to WordPress that solves plugin security](https://blog.cloudflare.com/emdash-wordpress/)

EmDash 是 WordPress 的精神继承者，旨在解决插件安全等核心问题，采用 TypeScript 编写，支持无服务器架构，并内置 AI 代理和支付功能，以适应当代网络需求。

- 🛡️ 解决插件安全危机：通过沙盒隔离和权限声明，确保插件仅能执行预设操作，消除安全隐患
- 🔓 打破市场锁定：插件可自由选择许可证，且代码在安全沙箱中独立运行，减少对集中式市场的依赖
- 💰 内置 x402 支付支持：允许内容创作者按使用收费，无需订阅或额外开发工作
- ⚡ 实现零扩展托管：基于无服务器架构，可随需求自动扩缩容，仅在执行时计费
- 🎨 现代化主题架构：采用 Astro 框架，使主题开发更安全、高效，且易于前端开发者和 AI 代理操作
- 🤖 AI 原生 CMS：提供 CLI、MCP 服务器和技能库，支持 AI 代理自动化管理内容和插件开发
- 🔑 可插拔身份验证：默认使用通行密钥，支持 SSO 集成，并提供基于角色的访问控制
- 🔄 支持 WordPress 迁移：提供导出工具和自定义模式，便于将现有站点内容导入 EmDash

---

### [npm 工作区简明图解入门 | Wasp](https://wasp.sh/blog/2026/03/25/gentle-intro-npm-workspaces)

**原文标题**: [A gentle intro to npm workspaces, with visuals | Wasp](https://wasp.sh/blog/2026/03/25/gentle-intro-npm-workspaces)

本文介绍了 npm 工作区（workspaces）的概念、历史背景、工作原理及其适用场景，旨在帮助开发者理解如何利用工作区管理多包项目，避免依赖重复和版本冲突，并提升开发效率。

- 🏗️ **工作区定义与作用**：工作区是 npm、Yarn、pnpm 等包管理器的功能，允许在单个项目中管理多个 JavaScript 包，实现依赖共享和跨包导入，避免依赖重复安装和版本不一致问题。
- 📜 **历史演变**：工作区概念起源于 2015 年 Babel 项目对代码库的模块化需求，随后由 Lerna 工具推广，并在 2017 年由 Yarn 首次作为一等公民功能引入。如今主流包管理器均已支持工作区。
- 🔧 **核心功能**：工作区提供三大特性：每个工作区是独立包（自有 package.json）、依赖全局解析共享（相同依赖只安装一次）、工作区可通过名称相互依赖（无需发布或手动路径配置）。
- 🧩 **依赖解析机制**：包管理器通过将工作区视为“虚拟根包”的依赖，复用现有依赖去重算法，确保跨工作区的相同依赖仅安装一次，避免因多副本导致的运行时错误（如 React 状态不一致）。
- 🔗 **跨包导入实现**：利用符号链接（symlinks）在根目录的 node_modules 中创建指向各工作区的链接，结合 Node.js 的模块查找规则（向上遍历 node_modules），使工作区能通过名称直接导入其他工作区。
- ⚠️ **适用与不适用场景**：工作区最适合多包协同开发、依赖共享频繁的项目（如单体仓库）。不适用于无明确分包需求的代码库、独立性强且依赖不共享的包、存在循环依赖或多仓库拆分的情况。
- 🐝 **Wasp 框架实践**：Wasp 自 v0.19 起利用工作区管理生成的 SDK、前端和后端包，解决紧密耦合包间的依赖匹配问题，提升安装速度和开发体验，同时允许用户自定义工作区集成。

---

### [工作区 | npm 文档](https://docs.npmjs.com/cli/v8/using-npm/workspaces/)

**原文标题**: [workspaces | npm Docs](https://docs.npmjs.com/cli/v8/using-npm/workspaces/)

npm 工作区是一组功能，用于从本地文件系统管理多个包，通过根包自动链接嵌套包，简化多包项目的开发流程。

- 🏗️ 工作区通过根`package.json`中的`workspaces`属性定义，列出嵌套包的路径
- 🔗 运行`npm install`时，工作区包会自动符号链接到根`node_modules`，无需手动`npm link`
- 🛠️ 使用`npm init -w <路径>`可快速创建新工作区并自动配置
- 📦 通过`-w`参数可为特定工作区添加依赖，如`npm install abbrev -w a`
- 📂 工作区包可通过其`package.json`中定义的名称直接引用，支持模块化开发
- 🏃 使用`--workspace`参数可在特定工作区运行命令，如`npm run test --workspace=a`
- 🔄 使用`--workspaces`参数可在所有工作区运行相同命令
- ⚙️ 结合`--if-present`标志可忽略缺少脚本的工作区，避免运行中断

---

### [牛 - 生产级沙盒环境](https://www.ox.build?utm_source=cooperpress&utm_medium=referral&utm_campaign=node-weekly-newsletter)

**原文标题**: [Ox - Production-fidelity sandboxes](https://www.ox.build?utm_source=cooperpress&utm_medium=referral&utm_campaign=node-weekly-newsletter)

本文介绍了人工智能在医疗领域的应用现状与前景，重点探讨了其在疾病诊断、治疗方案优化及医疗管理效率提升方面的作用，并简要提及了相关的伦理挑战。

- 🏥 AI 辅助诊断系统能通过分析医学影像快速识别病灶，提升早期疾病检出率
- 💊 基于机器学习的个性化治疗方案可结合患者数据优化用药与治疗路径
- 📊 智能医疗管理平台能自动化处理病历、预约及药物配送，减轻医护负担
- ⚖️ 数据隐私与算法透明度等伦理问题仍需在技术发展中同步完善规范

---

### [多数开发者对生产环境中的 Node.js 存在误解（与 TC39 代表 Ulises 合作）- YouTube](https://www.youtube.com/watch?v=rqmTDVdnMT8)

**原文标题**: [Most Developers Misunderstand Node.js in Production (with Ulises, TC39 Delegate) - YouTube](https://www.youtube.com/watch?v=rqmTDVdnMT8)

该内容为 YouTube 网站底部的导航链接列表，展示了平台的主要信息与功能入口。

- 📄 概要 - 平台基本介绍与说明
- 🗞️ プレスルーム - 新闻发布与媒体资料
- ©️ 著作権 - 版权政策与保护信息
- 📮 お問い合わせ - 用户联系与客服渠道
- 🎨 クリエイター向け - 创作者支持与资源
- 📢 広告掲載 - 广告投放与合作
- 💻 開発者向け - 开发者工具与 API
- 📜 利用規約 - 平台使用条款
- 🔒 プライバシー - 隐私保护政策
- ⚙️ ポリシーとセキュリティ - 政策与安全指南
- 🔧 YouTube の仕組み - 平台运作机制说明
- 🆕 新機能を試してみる - 新功能测试体验
- 🏢 © 2026 Google LLC - 版权归属声明

---

### [Vercel AI SDK 在 Node.js 中的智能体入门指南 | www.thecodebarbarian.com](https://thecodebarbarian.com/getting-started-with-the-vercel-ai-sdk-agents-in-nodejs.html)

**原文标题**: [Getting Started with the Vercel AI SDK Agents in Node.js | www.thecodebarbarian.com](https://thecodebarbarian.com/getting-started-with-the-vercel-ai-sdk-agents-in-nodejs.html)

本文介绍了如何使用 Vercel AI SDK 的 ToolLoopAgent 类构建一个能玩“20 个问题”游戏的 AI 代理，通过结合工具调用与 LLM 决策循环实现交互式任务。

- 🤖 AI 代理是一个循环执行 LLM 调用的系统，每步可调用工具或生成文本，直到输出最终结果
- 🛠️ 工具是代理可调用的函数，需定义输入模式，能执行读取文件、API 调用等操作，甚至可通过命令行与用户交互
- 🔄 代理通过`stepCountIs()`设置停止条件防止无限循环，示例中限制为 20 轮提问
- 🎮 实战演示了构建“20 个问题”游戏代理：结合提问工具、游戏规则指令和循环控制机制
- 📊 代理执行结果包含详细步骤记录，便于调试模型决策过程与工具调用参数
- 🌟 该模式可扩展至实际工作流（如日志查询、变更记录生成），形成“LLM 决策→工具获取数据→循环直至完成”的通用范式

---

### [Nodejs Brotli UAF | maitai 的博客](https://blig.one/2026/03/29/nodejs-brotli-uaf.html)

**原文标题**: [Nodejs Brotli UAF | maitai's blog](https://blig.one/2026/03/29/nodejs-brotli-uaf.html)

本文介绍了作者利用 Claude AI 辅助在 Node.js 中发现并利用 Brotli 压缩模块中的 use-after-free 漏洞，最终绕过 Node.js 权限模型实现任意代码执行的过程。

- 🧠 作者借助 Claude AI 快速理解 Node.js 权限模型的工作原理，发现其本质是一系列运行时检查，易被内存破坏漏洞绕过
- 🐛 在 zlib 模块中发现一个教科书级的 use-after-free 漏洞：异步压缩过程中调用 reset() 会释放 BrotliEncoderState，而工作线程仍在使用该内存
- 🔧 漏洞利用涉及堆喷技术，通过大量分配相同大小的内存来覆盖已释放的 BrotliEncoderState 结构体
- 🎯 关键目标是篡改 MemoryManager 结构体中的函数指针，将 alloc_func 指向 system()，opaque 指向命令字符串
- 🗺️ 通过 Buffer.allocUnsafe() 泄漏 libc 地址，利用 tls.createSecureContext() 泄漏命令字符串地址，绕过 ASLR 保护
- ⚡ 完整利用链结合了信息泄漏、堆喷和竞争条件，最终实现在 aarch64 架构上的任意命令执行
- 🛡️ 该漏洞成功绕过了 Node.js 的权限模型，尽管官方认为需要任意代码执行权限故不在威胁模型内，但作者仍建议修复
- 🔗 漏洞已提交并修复，相关代码提交可在 GitHub 上查看

---

### [为何我们用 Bun 替代 Node.js 以实现 5 倍吞吐量 | Trigger.dev](https://trigger.dev/blog/firebun)

**原文标题**: [Why we replaced Node.js with Bun for 5x throughput | Trigger.dev](https://trigger.dev/blog/firebun)

Trigger.dev 团队将关键服务 Firestarter 从 Node.js 迁移至 Bun，实现了 5 倍的吞吐量提升，并解决了 Bun 特有的内存泄漏问题。通过四阶段优化，包括替换 SQLite 为 Map 数据结构、迁移至 Bun.serve()、优化热点代码路径以及编译为独立二进制文件，最终使吞吐量从 2,099 req/s提升至约10,700 req/s，延迟大幅降低，容器镜像体积从180MB缩减至68MB。

- 🔍 通过性能分析发现 SQLite 查询占 31% CPU 时间，改用 Map 后吞吐量提升 2.2 倍
- ⚡ 迁移至 Bun.serve() 使吞吐量再翻倍，延迟降低一半以上
- 🛠️ 优化 Zod 验证、头信息处理和日志逻辑，减少 40% CPU 使用
- 📦 编译为独立二进制文件进一步提升 14% 吞吐量，镜像体积减小 43%
- 🚨 发现并修复 Bun 中因未解析 Promise 导致的客户端断开连接内存泄漏
- 📊 生产环境数据显示 CPU 和内存使用更稳定，最大延迟改善 28 倍
- 🧪 强调分阶段基准测试的重要性，并分享了 Bun 调试和负载测试实践

---

### [发布 4.0.0 版本 · huggingface/transformers.js · GitHub](https://github.com/huggingface/transformers.js/releases/tag/4.0.0)

**原文标题**: [Release 4.0.0 · huggingface/transformers.js · GitHub](https://github.com/huggingface/transformers.js/releases/tag/4.0.0)

Transformers.js v4 正式发布，引入全新 WebGPU 后端、新增大量模型支持、优化代码库结构，并提升开发体验与性能。

- 🚀 **全新 WebGPU 后端**：采用 C++ 重写的 WebGPU 运行时，支持浏览器、Node.js、Bun、Deno 等多种 JavaScript 环境，性能显著提升，部分模型加速达 4 倍。
- 🤖 **新增模型架构**：支持 GPT-OSS、Chatterbox、GraniteMoeHybrid、LFM2-MoE 等先进模型，涵盖 Mamba、MLA、MoE 等复杂架构，并兼容超过 8B 参数的大模型。
- 📦 **ModelRegistry API**：提供生产级工作流支持，可查看管道文件、元数据、缓存状态及可用精度类型，优化资源管理与加载进度跟踪。
- ⚙️ **环境与日志控制**：新增 `env.useWasmCache` 和 `env.fetch` 配置，支持离线缓存与自定义请求；改进日志级别管理，减少控制台噪音。
- 🏗️ **代码库重构**：转为 PNPM 工作区管理，拆分模型逻辑至模块化文件，迁移示例至独立仓库，并统一代码格式化工具。
- 🔤 **独立 Tokenizers.js**：推出轻量级（8.8kB）且无依赖的 tokenizer 库，支持跨平台使用，提升 tokenization 的灵活性与性能。
- ⚡ **构建系统升级**：从 Webpack 迁移至 esbuild，构建时间减少 90%，捆绑包体积平均缩小 10%，显著提升开发效率与加载速度。
- 🛠️ **类型与文档改进**：增强动态管道类型安全，修复多项 Bug，并更新教程、集成指南与贡献文档，提升开发者体验。

---

### [错误](https://nodeweekly.com/link/183201/web)

**原文标题**: [Error](https://nodeweekly.com/link/183201/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='huggingface.co', port=443): Max retries exceeded with url: / (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1000)')))

---

### [Transformers.js V4 演示 - 一个 webml-community 合集](https://huggingface.co/collections/webml-community/transformersjs-v4-demos)

**原文标题**: [Transformers.js V4 demos - a webml-community Collection](https://huggingface.co/collections/webml-community/transformersjs-v4-demos)

Transformers.js V4 演示合集展示了多个基于 WebGPU 在浏览器中本地运行的 AI 模型应用，涵盖文本生成、语音转录、视频处理、翻译和图像分割等多种功能。

- 💧 **LFM2.5 1.2B Thinking WebGPU** – 在浏览器中通过 WebGPU 直接运行 LFM2.5-1.2B-Thinking 模型
- 💬 **Voxtral Realtime WebGPU** – 完全在浏览器内实现的实时语音转录
- ⚛ **Nemotron 3 Nano WebGPU** – 在浏览器中运行的紧凑型推理模型
- ⚡ **GPT OSS WebGPU** – 在浏览器本地通过 WebGPU 运行 GPT-OSS-20B 模型
- 😻 **Qwen3.5 WebGPU** – 在浏览器中使用 Transformers.js 运行 Qwen3.5（0.8B、2B、4B）模型
- 📹 **LFM2 VL WebGPU** – 浏览器内的实时视频字幕生成
- 🎥 **Text Behind Video** – 在浏览器本地创建电影视频设计
- 🌐 **TranslateGemma 4B WebGPU** – 支持 56 种语言的私有浏览器翻译器
- ⚡ **Cohere Transcribe WebGPU** – 在浏览器本地通过 WebGPU 运行 Cohere Transcribe
- 🔮 **Nanbeige 4.1 3B** – 在浏览器本地与 Nanbeige AI 聊天
- 🎯 **SAM3 Tracker WebGPU** – 通过点击点分割图像并下载裁剪部分
- 💧 **LFM2 MoE WebGPU** – WebGPU 加速的混合专家模型
- ⚡ **RF DETR Medium WebGPU** – 在浏览器中运行的实时检测 Transformer 模型
- 🦙 **Olmo Hybrid WebGPU** – 在浏览器本地通过 WebGPU 100% 运行 Olmo-Hybrid-7B 模型
- 🗣 **Granite 4.0 1b Speech WebGPU** – 在 WebGPU 上使用 Transformers.js 运行 granite-4.0-1b-speech 模型
- 🌍 **TinyAya WebGPU** – 在浏览器本地使用 Transformers.js 运行 TinyAya 模型
- ✖ **QED-Nano WebGPU** – 在浏览器本地使用 Transformers.js 运行 QED-Nano 模型
- 🚀 **voyage-4-nano WebGPU** – 在交互式散点图中可视化句子嵌入
- ⚡ **RF DETR Nano WebGPU** – 在浏览器中运行的实时检测 Transformer 模型
- 🦅 **Falcon-H1-Tiny-90M WebGPU** – 展示 Falcon-H1 架构（Mamba + Attention）的示例
- 🎠 **Perplexity Embed Web** – 语义搜索文档并在 3D 旋转木马中查看结果
- 🚀 **LFM2.5 WebGPU Summarizer** – 在浏览器本地总结网页内容（演示）
- 🚀 **Gemma 4 WebGPU** – 在浏览器中通过 WebGPU 使用 Transformers.js 运行 Gemma 4 模型

---

### [Voxtral 实时 WebGPU - 由 mistralai 创建的 Hugging Face 空间](https://huggingface.co/spaces/mistralai/Voxtral-Realtime-WebGPU)

**原文标题**: [Voxtral Realtime WebGPU - a Hugging Face Space by mistralai](https://huggingface.co/spaces/mistralai/Voxtral-Realtime-WebGPU)

清爽感是一种令人愉悦的体验，通常与洁净、凉爽和活力相关，能带来身心舒畅的感受。

- 🌊 洁净与凉爽：常与清水、微风或清凉环境相联系，带来感官上的舒适
- 🌿 自然元素：植物、绿叶和清新空气常能营造清爽氛围
- 🧘 身心舒畅：不仅指身体感觉，也包含精神上的轻松与焕然一新
- 🍃 简单纯粹：避免复杂或厚重，追求简单、轻盈的状态
- 🌞 活力复苏：像晨露或凉风般唤醒感官，恢复精力与清醒

---

### [Qwen3.5 WebGPU - 由 webml-community 创建的 Hugging Face 空间](https://huggingface.co/spaces/webml-community/Qwen3.5-WebGPU)

**原文标题**: [Qwen3.5 WebGPU - a Hugging Face Space by webml-community](https://huggingface.co/spaces/webml-community/Qwen3.5-WebGPU)

清爽感是一种令人愉悦的体验，通常与清新、洁净和活力相关，能带来身心舒畅的感觉。

- 🌊 带来清新与洁净的感受
- 💧 常用于描述水、空气或气味
- 🌿 与自然元素紧密相连
- 😌 引发放松与舒适的情绪
- 🍃 象征更新与活力

---

### [LFM2 VL WebGPU - LiquidAI 在 Hugging Face 上的空间](https://huggingface.co/spaces/LiquidAI/LFM2-VL-WebGPU)

**原文标题**: [LFM2 VL WebGPU - a Hugging Face Space by LiquidAI](https://huggingface.co/spaces/LiquidAI/LFM2-VL-WebGPU)

清爽感是一种令人愉悦的体验，通常与清新、洁净和活力相关，能带来身心舒畅的感觉。

- 🌊 带来清新与洁净的感受
- 💧 常用于描述水、空气或食物的品质
- 🌿 引发轻松与活力的情绪
- 🍃 在炎热或沉闷环境中尤为珍贵
- 🧼 与简洁、纯粹的设计或风格相关联

---

### [GitHub - uhop/node-re2: Node.js 的 RE2 绑定：快速、安全的回溯正则表达式引擎替代方案。 · GitHub](https://github.com/uhop/node-re2)

**原文标题**: [GitHub - uhop/node-re2: node.js bindings for RE2: fast, safe alternative to backtracking regular expression engines. · GitHub](https://github.com/uhop/node-re2)

node-re2 是一个为 Node.js 提供 RE2 正则表达式引擎绑定的项目，旨在提供快速且安全的正则表达式匹配，有效防止正则表达式拒绝服务攻击。

- 🛡️ **安全防护** – 使用 RE2 引擎替代 Node.js 内置引擎，避免因回溯导致的指数级时间复杂度和 ReDoS 攻击。
- 🔄 **兼容性** – 模拟标准 RegExp API，支持常用标志、属性及方法，可作为大多数场景的直接替代品。
- 📦 **扩展功能** – 支持从 RegExp 对象构造、Buffer 直接处理、RE2.Set 多模式匹配以及 Unicode 字符长度计算等工具。
- ⚠️ **功能限制** – 不支持反向引用和前瞻断言等复杂特性，遇到时会抛出 SyntaxError。
- 🌍 **Unicode 模式** – 始终在 Unicode 模式下工作，可通过 RE2.unicodeWarningLevel 控制非 Unicode 正则表达式的处理方式。
- 📄 **安装与使用** – 通过 npm 安装，支持预编译包下载，使用方式与 RegExp 基本一致。

---

### [RE2（软件） - 维基百科](https://en.wikipedia.org/wiki/RE2_(software))

**原文标题**: [RE2 (software) - Wikipedia](https://en.wikipedia.org/wiki/RE2_(software))

RE2 是 Google 开发的一个 C++ 正则表达式库，采用基于有限状态自动机的算法，旨在提供线性时间复杂度的匹配并防止正则表达式拒绝服务攻击。

- 🏢 **Google 开发** – 由 Google 创建并用于其产品，如 Google 文档和表格
- ⚙️ **基于有限状态自动机** – 使用确定性有限状态自动机算法，避免回溯问题
- 🛡️ **防止 ReDoS 攻击** – 设计上保证线性时间增长，避免指数级运行时风险
- 🔄 **与 PCRE 对比** – 不支持回溯引用和递归等特性，但内存和运行时间更可控
- 🌐 **跨平台支持** – 使用 C++17 编写，依赖 Google 的 Abseil 库
- 🐍 **多语言绑定** – 提供 Python、Go、Rust 等官方或社区封装版本
- 📈 **实际应用** – 被 CloudFlare 等用于网络安全防护，适合服务器环境

---

### [正则表达式拒绝服务攻击 - ReDoS | OWASP 基金会](https://owasp.org/www-community/attacks/Regular_expression_Denial_of_Service_-_ReDoS)

**原文标题**: [Regular expression Denial of Service - ReDoS | OWASP Foundation](https://owasp.org/www-community/attacks/Regular_expression_Denial_of_Service_-_ReDoS)

正则表达式拒绝服务攻击是一种利用正则表达式引擎在特定极端情况下处理速度急剧下降（与输入规模呈指数级关系）的拒绝服务攻击方式。攻击者通过精心构造的输入使使用正则表达式的程序陷入长时间挂起状态。

- 🔍 **攻击原理**：正则表达式引擎采用回溯算法，当匹配失败时会尝试其他路径，低效的正则模式会导致路径数量爆炸式增长
- ⚠️ **恶意正则特征**：包含重复分组、内部重复或重叠交替结构的正则表达式（如 `(a+)+$`）容易受到攻击
- 🌐 **攻击范围**：影响网络浏览器、Web 应用防火墙、数据库乃至服务器等各个使用正则表达式的层面
- 🎯 **攻击方式**：攻击者寻找使用恶意正则表达式的应用，或通过用户输入注入恶意正则表达式
- 📧 **实际案例**：邮件验证正则 `^([a-zA-Z0-9])(([\-.]|[_]+)?([a-zA-Z0-9]+))*(@){1}[a-z0-9]+[.]{1}(([a-z]{2,3})|([a-z]{2,3}[.]{1}[a-z]{2,3}))$` 可被输入 `aaaaaaaaaaaaaaaaaaaaaaaa!` 攻击
- 🔐 **注入示例**：密码验证场景中，攻击者可通过用户名输入恶意正则表达式导致系统挂起
- 🛡️ **防护建议**：使用高效正则算法、避免使用扩展正则功能、对用户输入进行严格过滤

---

### [GitHub - kepano/defuddle：以Markdown格式获取任意页面的主要内容。· GitHub](https://github.com/kepano/defuddle)

**原文标题**: [GitHub - kepano/defuddle: Get the main content of any page as Markdown. · GitHub](https://github.com/kepano/defuddle)

Defuddle 是一个用于提取和清理网页主要内容的开源工具，它能移除页面中的非必要元素（如侧边栏、页脚、广告等），并支持输出为标准化 HTML 或 Markdown 格式。

- 📦 **核心功能**：自动提取网页正文，移除广告、导航栏等干扰元素，保留核心内容。
- 🛠️ **多环境支持**：可在浏览器、Node.js 环境和命令行（CLI）中使用。
- 📄 **输出格式灵活**：支持输出为 HTML、Markdown 或 JSON，并可提取标题、作者、描述等元数据。
- 🔧 **高度可配置**：提供调试模式、内容选择器覆盖、异步提取等选项，便于定制化处理。
- 📚 **内容标准化**：自动标准化代码块、脚注、数学公式和提示框等元素，确保输出一致性。
- 🌐 **第三方服务集成**：支持通过 API 获取客户端渲染页面的内容（如 Twitter）。
- 🧪 **开发友好**：提供详细的调试信息和管道步骤控制，便于排查内容提取问题。

---

### [Defuddle — 将任何网页主要内容转换为 Markdown 格式。](https://defuddle.md/)

**原文标题**: [Defuddle — Get the main content of any page as Markdown.](https://defuddle.md/)

Defuddle 是一个将网页内容转换为 Markdown 格式的工具，支持通过 URL、HTML 输入或浏览器扩展快速提取并清理页面核心信息，适用于笔记整理和内容存档。

- 🌐 支持通过 URL、HTML 或浏览器扩展将任意网页转换为 Markdown 格式
- 🔧 专为 Obsidian Web Clipper 设计，可本地运行并处理私有内容或 JavaScript 渲染页面
- 📖 提供书签工具、API 接口及 NPM 包，方便集成到工作流中
- 📄 输出包含 YAML 元数据的 Markdown 文档，支持自定义路径附加
- ⚖️ 遵循 MIT 开源协议，提供免费基础服务及透明条款

---

### [GitHub - motdotla/dotenv：为Node.js项目从.env文件加载环境变量。 · GitHub](https://github.com/motdotla/dotenv)

**原文标题**: [GitHub - motdotla/dotenv: Loads environment variables from .env for nodejs projects. · GitHub](https://github.com/motdotla/dotenv)

dotenv 是一个零依赖的 Node.js 模块，用于将 .env 文件中的环境变量加载到 process.env 中，遵循十二要素应用原则，实现配置与代码分离。

- 🚀 **核心功能**：从 .env 文件加载环境变量到 Node.js 的 process.env 对象
- 📦 **安装简单**：通过 npm install dotenv 即可安装，支持 ES6 导入
- ⚙️ **配置灵活**：支持自定义文件路径、多环境配置、多行值和注释
- 🔧 **高级特性**：提供解析引擎、预加载、变量扩展（通过 dotenvx）、加密和同步功能
- 🛡️ **安全建议**：推荐使用 dotenvx 加密 .env 文件后再提交到代码仓库
- 🌐 **多环境支持**：可为不同环境（如开发、生产）创建独立的 .env 文件
- ⚠️ **注意事项**：默认不覆盖已存在的环境变量，可通过 override 选项修改此行为
- 📚 **广泛适用**：与多种框架和工具集成，包括 React、Webpack、Express 等
- 🔍 **调试支持**：提供 debug 模式帮助排查环境变量加载问题

---

### [环境变量 | Node.js v25.9.0 文档](https://nodejs.org/api/environment_variables.html#cli-options)

**原文标题**: [Environment Variables | Node.js v25.9.0 Documentation](https://nodejs.org/api/environment_variables.html#cli-options)

Node.js 环境变量文档概述了环境变量的定义、使用方式及相关 API，重点介绍了通过.env 文件管理环境变量的规范与操作方法。

- 🌍 环境变量是与 Node.js 进程运行环境关联的变量，可通过`process.env`对象进行访问和修改
- 📄 `.env`文件用于定义环境变量，支持键值对格式，变量名需符合字母、数字和下划线的组合规则
- 🔤 变量值可以是任意文本，支持单引号或双引号包裹，引号内的内容可跨行，未加引号则仅限于单行
- ✂️ 解析时会自动忽略键值对周围的空白字符，除非这些字符被包含在引号内
- 💬 以`#`开头的行表示注释，但引号内的`#`会被视为普通字符
- 🔧 支持在变量前添加`export`关键字，便于在 shell 终端中直接使用文件内容
- ⚙️ 可通过 CLI 选项`--env-file`或`--env-file-if-exists`加载.env 文件来填充`process.env`
- 🛠️ 提供`process.loadEnvFile()`和`util.parseEnv()`等编程接口，用于动态加载和解析.env 文件内容

---

### [发布 v1.2.0 · dupontcyborg/numpy-ts · GitHub](https://github.com/dupontcyborg/numpy-ts/releases/tag/v1.2.0)

**原文标题**: [Release v1.2.0 · dupontcyborg/numpy-ts · GitHub](https://github.com/dupontcyborg/numpy-ts/releases/tag/v1.2.0)

该 GitHub 仓库发布了 numpy-ts 库的 v1.2.0 版本，主要包含性能优化、功能增强和错误修复。

- 🚀 **捆绑简化**：通过减少依赖和优化打包流程提升库的加载效率。
- 🆕 **新增 Float16 支持**：扩展数据类型以增强数值计算灵活性。
- ⚡ **优化 FFT 性能**：改进快速傅里叶变换算法的执行速度。
- 🐛 **修复 Node 20/22的float16测试问题**：确保在不同 Node 版本下的兼容性。
- 🔧 **杂项性能改进与清理**：整体代码优化和冗余清理。
- 🎲 **随机 WASM 内核**：引入 WebAssembly 随机数生成功能以提升性能。
- 📊 **集合优化**：改进数据处理中的集合操作效率。
- 🚧 **1.2.0 版本准备**：完成发布前的最终调整和测试。

---

### [numpy-ts - numpy-ts](https://numpyts.dev/)

**原文标题**: [numpy-ts - numpy-ts](https://numpyts.dev/)

numpy-ts 是一个为 TypeScript 和 JavaScript 设计的完整 NumPy 实现，提供与 Python NumPy 高度一致的 API，具备类型安全、可树摇优化、无依赖和跨运行时支持等特点。

- 📊 **高 API 覆盖率** – 实现了 476 个 NumPy 函数中的 94%，涵盖算术、线性代数、随机分布等领域。
- 🛡️ **类型安全** – 为所有函数、数据类型和数组操作提供完整的 TypeScript 类型定义，可在编译时捕获错误。
- 🌳 **可树摇优化** – 支持按需导入，打包工具会自动移除未使用代码，保持生产构建体积小巧。
- ✅ **NumPy 验证** – 通过超过 6000 项测试直接与 NumPy 输出对比，确保结果一致。
- 📦 **零依赖** – 纯 TypeScript 实现，无需原生模块、WebAssembly 或重型运行时，可在任何 JavaScript 环境运行。
- 🌐 **跨运行时支持** – 兼容 Node.js、Bun、Deno 及所有现代浏览器，适用于服务器和客户端。
- 🔄 **无缝迁移** – API 设计尽可能贴近 NumPy，大部分代码可直接从 Python 移植，并提供详细的迁移指南。

---

### [GitHub - pillarjs/path-to-regexp：将路径字符串（如 `/user/:name`）转换为正则表达式 · GitHub](https://github.com/pillarjs/path-to-regexp)

**原文标题**: [GitHub - pillarjs/path-to-regexp: Turn a path string such as `/user/:name` into a regular expression · GitHub](https://github.com/pillarjs/path-to-regexp)

这是一个用于将路径字符串（如 `/user/:name`）转换为正则表达式的 JavaScript 库，常用于 Node.js 路由处理（如 Express.js）。

- 🛠️ **核心功能**：将路径模式（含参数、通配符等）转换为正则表达式，并支持路径匹配与生成。
- 📦 **安装方式**：通过 npm 安装 `path-to-regexp` 包即可使用。
- 🔧 **主要函数**：包括 `match`（路径匹配）、`pathToRegexp`（生成正则）、`compile`（反向生成路径）、`parse`（解析路径结构）和 `stringify`（序列化令牌数据）。
- 🎯 **参数类型**：支持命名参数（`:foo`）、通配符（`*splat`）和可选部分（使用 `{}` 包裹），增强路径表达的灵活性。
- ⚠️ **使用注意**：该库适用于有序数据（如路径），不适用于查询字符串、URL 片段等无序数据；与 Express 4.x 及以下版本存在兼容性差异。
- 📄 **许可证与资源**：采用 MIT 许可证，提供完整的 API 文档、历史记录和安全策略，社区活跃（8.6k 星标）。

---

### [GitHub - sindresorhus/globby：用户友好的通配符匹配工具 · GitHub](https://github.com/sindresorhus/globby)

**原文标题**: [GitHub - sindresorhus/globby: User-friendly glob matching · GitHub](https://github.com/sindresorhus/globby)

Globby 是一个基于 fast-glob 构建的 Node.js 库，提供用户友好的 glob 模式匹配功能，支持 Promise API、多模式、否定模式、目录扩展、.gitignore 忽略文件以及 URL 作为工作目录等特性。

- 🚀 基于 fast-glob，提供更友好的 glob 匹配功能，支持 Promise API 和多种模式
- 🔍 支持否定模式与仅否定模式，可灵活排除特定文件
- 📁 自动扩展目录匹配，并兼容 .gitignore 等忽略配置文件
- ⚙️ 提供同步、流式及路径转换等多种 API，适应不同使用场景
- 🛡️ 包含 gitignore 检查工具，可判断文件是否被忽略
- 📦 可通过 npm 安装，广泛应用于 JavaScript 和 Node.js 项目

---

### [GitHub - sindresorhus/globby：用户友好的通配符匹配工具 · GitHub](https://github.com/sindresorhus/globby?tab=readme-ov-file#globalgitignore)

**原文标题**: [GitHub - sindresorhus/globby: User-friendly glob matching · GitHub](https://github.com/sindresorhus/globby?tab=readme-ov-file#globalgitignore)

Globby 是一个基于 fast-glob 的 Node.js 库，提供用户友好的 glob 模式匹配功能，支持 Promise API、多模式匹配、目录扩展、.gitignore 忽略文件以及路径转换等特性。

- 🚀 **基于 fast-glob 构建** – 在 fast-glob 的基础上增加了更多实用功能，如 Promise API 和目录自动扩展。
- 🔍 **支持多种匹配模式** – 允许使用多个 glob 模式、否定模式（如 `!foobar`）以及仅否定模式，并自动扩展目录（如 `foo` 扩展为 `foo/**/*`）。
- 📁 **集成忽略文件支持** – 可配置以遵循 `.gitignore`、`.eslintignore` 等忽略文件的规则，提升匹配性能。
- ⚙️ **灵活的配置选项** – 提供 `expandDirectories`、`gitignore`、`ignoreFiles` 等选项，支持自定义文件系统适配器（`fs` 选项）。
- 🔄 **多种使用方式** – 除了主要的 `globby()` 异步函数，还提供同步版本 `globbySync()`、流式接口 `globbyStream()` 以及工具函数如 `convertPathToPattern()`。
- 🛠️ **高级工具函数** – 包括 `generateGlobTasks()` 用于生成 glob 任务、`isDynamicPattern()` 检测动态模式，以及 `isGitIgnored()` 检查文件是否被忽略。
- 📚 **详细的文档与示例** – 提供丰富的 API 说明、用法示例和 glob 模式指南，涵盖基本通配符到复杂否定模式的使用。

---

### [GitHub - bloomberg/ts-blank-space: 一款小巧、快速、纯 JavaScript 的类型剥离器，采用官方 TypeScript 解析器。· GitHub](https://github.com/bloomberg/ts-blank-space)

**原文标题**: [GitHub - bloomberg/ts-blank-space: A small, fast, pure JavaScript type-stripper that uses the official TypeScript parser. · GitHub](https://github.com/bloomberg/ts-blank-space)

ts-blank-space 是一个使用官方 TypeScript 解析器的小型、快速、纯 JavaScript 类型擦除工具，它通过移除 TypeScript 代码中的类型注解来生成纯 JavaScript 代码，同时保持原始代码的结构和位置不变。

- 🚀 **快速高效**：性能接近原生多线程转换器，是 JavaScript 或 Wasm 方案中最快的选择。
- 📦 **轻量简洁**：约 700 行代码，仅依赖 TypeScript 官方解析器，易于维护。
- 🔧 **灵活 API**：支持字符串到字符串转换，也允许用户提供自己的 AST 进行处理。
- 🧩 **Node.js 加载器**：提供模块加载器钩子，可直接在 Node.js 中预处理导入的 `.ts` 和 `.mts` 文件。
- 🗺️ **保留源码映射**：输出代码位置与原始源码一致，无需额外 SourceMap 处理。
- ⚠️ **处理边缘情况**：自动处理 ASI（自动分号插入）和箭头函数多行类型注解等特殊情况。
- ❌ **部分语法不支持**：无法擦除具有运行时语义的 TypeScript 语法（如参数属性），遇到时会触发错误回调。
- ⚙️ **推荐配置**：提供了优化的 `tsconfig.json` 编译器设置建议，以确保最佳兼容性。
- 🔄 **支持 TSX/JSX**：`.tsx` 文件会生成 `.jsx` 输出，JSX 部分会被保留而不进行转换。
- 🤝 **开源贡献**：项目欢迎问题报告和代码贡献，并提供了行为准则和安全漏洞报告渠道。

---

### [GitHub - moscajs/aedes：基于流的轻量级MQTT代理，适用于任何流服务器，Node.js风格 · GitHub](https://github.com/moscajs/aedes)

**原文标题**: [GitHub - moscajs/aedes: Barebone MQTT broker that can run on any stream server, the node way · GitHub](https://github.com/moscajs/aedes)

Aedes 是一个基于 Node.js 的轻量级 MQTT 代理服务器，可在任何流服务器上运行，支持 MQTT 3.1 和 3.1.1 协议，提供集群、持久化、插件扩展等功能，并具有较高的性能表现。

- 🚀 **核心特性**：支持 MQTT 3.1/3.1.1、TCP/SSL/WebSocket、消息持久化、集群、身份验证与授权、$SYS 主题及插件化中间件。
- 🛠️ **安装与使用**：可通过 npm 安装（`npm install aedes`），提供 Docker 支持及详细的 API 文档。
- 🔌 **扩展与插件**：提供多种持久化后端（如 MongoDB、Redis、LevelDB）和消息队列发射器（如 mqemitter-redis），支持自定义中间件。
- 📊 **性能基准**：基准测试显示 Aedes 在集群模式下（如搭配 Redis 持久化与 Redis 发射器）性能优于前身 Mosca，吞吐量更高。
- 🌐 **应用案例**：被多个项目采用，如 Node-RED 的 MQTT 代理插件、Kuzzle IoT 后端等，社区活跃且有商业支持选项。
- ⚠️ **安全提示**：消息在授权发布回调后即视为有效，权限变更不影响已通过的消息；建议对敏感数据使用 QoS 0 或清洁会话。
- 📜 **开源与贡献**：基于 MIT 许可证开源，欢迎提交问题或拉取请求，并提供付费支持选项。

---

### [发布 v2.0.0-0 · sindresorhus/ky · GitHub](https://github.com/sindresorhus/ky/releases/tag/v2.0.0-0)

**原文标题**: [Release v2.0.0-0 · sindresorhus/ky · GitHub](https://github.com/sindresorhus/ky/releases/tag/v2.0.0-0)

Ky 库发布了 v2.0.0-0 预发布版本，这是下一个主要版本的先行版，包含多项重大变更、新功能和修复，旨在提升稳定性和开发体验。

- 🚨 **重大变更**：要求 Node.js 22，统一钩子函数签名，`prefixUrl` 更名为 `prefix`，`beforeError` 钩子现在接收所有错误类型，空响应时 `.json()` 返回 `undefined`，`searchParams` 改为合并而非替换查询参数，`HTTPError` 的响应体已自动解析并可通过 `error.data` 访问。
- ✨ **新增功能**：引入 `totalTimeout` 选项以设置总体超时，添加 `baseUrl` 选项用于标准 URL 解析，新增 `init` 钩子，添加 `NetworkError` 类并优化重试逻辑，支持 `.json()` 的 Standard Schema 验证，提供 `replaceOption` 辅助函数用于 `.extend()`，为 `beforeError` 钩子添加请求和选项上下文，为 `parseJson` 选项添加上下文，优化 `no-cors` 请求的错误处理，并优雅处理不支持的 `onUploadProgress`。
- 🔧 **问题修复**：修复了 `beforeRequest` 钩子在返回 `Request` 时被跳过的问题，忽略 `beforeError` 钩子返回的非 Error 对象，并剥离传递给钩子的选项中的 Ky 特定属性。
- 📘 **迁移指南**：详细说明了从 v1 升级到 v2 所需的代码调整，包括钩子签名、选项重命名、错误处理、响应解析和参数合并等方面的变化。

---

### [发布 v15.0.0 · sindresorhus/got · GitHub](https://github.com/sindresorhus/got/releases/tag/v15.0.0)

**原文标题**: [Release v15.0.0 · sindresorhus/got · GitHub](https://github.com/sindresorhus/got/releases/tag/v15.0.0)

Got 库发布了 v15.0.0 版本，包含多项重大变更和性能改进，需注意升级迁移。

- 🚨 **Node.js 22 成为最低要求** – 必须升级 Node.js 版本才能使用。
- 🗑️ **移除了 promise.cancel() API** – 需改用 AbortController 和 signal 选项。
- 📡 **isStream 选项被移除** – 直接使用 got.stream() 替代。
- 🌐 **使用原生 FormData 全局对象** – 不再依赖 form-data 包，需在 Node.js 18+ 环境中使用。
- 🔄 **responseType: 'buffer' 返回 Uint8Array** – 替代 Buffer，多数代码兼容，但严格类型检查需更新。
- 📏 **strictContentLength 默认启用** – 若内容长度不匹配会抛出错误，可设为 false 恢复旧行为。
- 🔁 **retry.enforceRetryRules 默认启用** – 自定义重试延迟函数仅在符合重试规则时调用，可设为 false 覆盖。
- 📋 **管道流头部复制改为可选** – 默认不再自动复制头部，需设置 copyPipedHeaders: true 启用。
- 🧩 **options 对象中移除 url 属性** – 在钩子中改用 response.url 或 request.requestUrl。
- 🔀 **不再自动跟随 300 和 304 响应** – 需手动处理这些状态码。
- 💾 **流式解码大文本/JSON 响应** – 降低内存峰值使用。
- 📊 **上传进度事件更细化** – 针对 JSON 和表单请求体提供分块事件。

---

### [GitHub - eslint/markdown：在Markdown文档中检查JavaScript代码块 · GitHub](https://github.com/eslint/markdown)

**原文标题**: [GitHub - eslint/markdown: Lint JavaScript code blocks in Markdown documents · GitHub](https://github.com/eslint/markdown)

ESLint Markdown 语言插件是一个用于在 Markdown 文件中进行代码检查的工具，支持对 Markdown 本身以及其中嵌入的 JavaScript、JSX、TypeScript 等代码块进行 linting。

- 📦 **安装与配置**：可通过 npm、yarn、pnpm 或 bun 安装，支持在 ESLint 配置中通过 `@eslint/markdown` 插件和 `markdown/recommended` 预设快速启用。
- ⚙️ **规则与语言**：提供一系列针对 Markdown 的 linting 规则（如检查代码块语言、标题层级、链接有效性等），并支持 CommonMark 和 GitHub Flavored Markdown 两种解析格式。
- 🔧 **高级功能**：支持通过语言选项启用 Front Matter（YAML、TOML、JSON）和数学公式（LaTeX）解析，以及使用处理器单独检查 Markdown 中的代码块。
- 🛠️ **编辑器集成**：与 VSCode 的 `vscode-eslint` 扩展兼容，并支持通过代码块元数据指定文件名以应用特定的 linting 配置。
- 🤝 **社区与贡献**：项目遵循 ESLint 贡献指南，接受社区代码提交，并由多个赞助商提供支持。

---

### [发布 v22.0.0 · sindresorhus/file-type · GitHub](https://github.com/sindresorhus/file-type/releases/tag/v22.0.0)

**原文标题**: [Release v22.0.0 · sindresorhus/file-type · GitHub](https://github.com/sindresorhus/file-type/releases/tag/v22.0.0)

file-type 库发布了 v22.0.0 版本，这是一个重大更新，要求 Node.js 22 环境，并移除了对 Node.js stream.Readable 的支持，同时修正了多个 MIME 类型，新增了对 Apple iWork 文件格式的检测支持。

- 🚨 **重大变更**：需要 Node.js 22 环境，并移除了对 Node.js stream.Readable 的支持，相关函数现仅接受 Web ReadableStream。
- 🔧 **API 调整**：移除了子导出（如 `file-type/core`），所有功能需直接从 `file-type` 导入；`ReadableStreamWithFileType` 类型被移除，改用 `AnyWebReadableByteStreamWithFileType`。
- 📝 **MIME 类型修正**：多个文件类型的 MIME 类型被更正或规范化，例如 lz、lnk、Apple Alias 等，部分使用自定义的 `x-ft-` 前缀。
- 🍎 **新增检测支持**：添加了对 Apple iWork 文件（.key、.pages、.numbers）的格式检测能力。
- 🐛 **问题修复**：修复了从流中读取 LibreOffice OOXML 文件时被错误检测为 ZIP 的问题。

---

### [终极 PaaS 定价比较计算器](https://judoscale.com/tools/paas-pricing-calculator?utm_source=node-weekly&utm_medium=referral&utm_campaign=calculator&utm_content=paas-alternatives-head-to-head)

**原文标题**: [The Ultimate PaaS Pricing Comparison Calculator](https://judoscale.com/tools/paas-pricing-calculator?utm_source=node-weekly&utm_medium=referral&utm_campaign=calculator&utm_content=paas-alternatives-head-to-head)

本文介绍了一款 PaaS 定价计算器，旨在帮助团队比较不同云托管选项的成本。计算器基于固定月度规模，强调通过自动扩展节省 33% 或更多成本，并建议根据应用需求调整 CPU 核心、内存、实例数量和月度出口流量等参数，以实现成本效益最大化。

- 🧮 计算器支持比较 Heroku、Render、Railway、Fly 和 Amazon ECS Fargate 等 PaaS 提供商的月度成本
- 💡 建议优先水平扩展（增加实例）而非过度配置 CPU/内存，以提升成本效率
- ⚙️ CPU 核心选择需结合应用架构，避免为无法利用多核的服务支付额外费用
- 🧠 内存配置推荐从 1GB 起步，并根据实际需求调整预留空间
- 🌐 月度出口流量需估算，未使用 CDN 时可能显著增加成本
- 🔍 各提供商计费方式差异大，需注意团队规模、出口费用和 CPU 类型等隐藏成本

---

### [申请 Gauntlet AI - 精英 AI 工程奖学金项目](https://gauntletai.com/apply?utm_source=node_weekly&utm_medium=referral&utm_campaign=april_1&utm_content=learn_more.)

**原文标题**: [Apply to Gauntlet AI - Elite AI Engineering Fellowship Program](https://gauntletai.com/apply?utm_source=node_weekly&utm_medium=referral&utm_campaign=april_1&utm_content=learn_more.)

这是一个为期十周的强化 AI 工程训练营，旨在通过高强度、全沉浸式的实战项目，将参与者从 AI 爱好者转变为能设计并交付生产级 AI 系统的专业人才。项目全程免费，由招聘合作伙伴承担费用，并提供前沿模型访问和高薪工作机会。

- 🚀 **高强度实战训练**：十周全职项目，前 3 周远程建立基础，后 7 周在奥斯汀线下集中，通过每周交付真实项目来快速提升 AI 工程能力。
- 💼 **就业直通车**：招聘合作伙伴全程观察参与者的实际构建过程，提供 20 万至 95 万美元的起薪，确保毕业生直接获得工作机会。
- 🛠️ **前沿技术栈**：涵盖 AI 优先开发、RAG 系统、多智能体协调、企业级微调、多模态 AI 及强化学习等前沿技术，每周挑战逐步升级。
- 🏆 **严格选拔标准**：面向有 3 年以上专业经验的工程师（Gauntlet Prime）或愿为美国政府工作的工程师（Gauntlet for America），要求全情投入并具备美国工作授权。
- 📅 **滚动录取机制**：提供多个入学批次（2026 年 4 月、7 月、9 月），采取先到先得原则，鼓励尽早申请以避免错失机会。

---

### [SerpApi：谷歌搜索 API](https://serpapi.com/?utm_source=cooperpress&utm_campaign=node_classified)

**原文标题**: [SerpApi: Google Search API](https://serpapi.com/?utm_source=cooperpress&utm_campaign=node_classified)

本文介绍了人工智能在医疗领域的应用现状与前景，重点探讨了其在疾病诊断、治疗方案优化及医疗管理效率提升方面的作用，并简要提及了相关的技术挑战和伦理考量。

- 🤖 AI 辅助诊断系统能通过分析医学影像快速识别病灶，提高早期疾病检出率
- 💊 基于机器学习的个性化治疗方案可结合患者数据优化用药与治疗路径
- 📊 智能医疗管理平台整合临床数据，显著降低医院运营成本并减少人为失误
- ⚠️ 数据隐私保护与算法透明度仍是当前技术推广面临的主要伦理挑战
- 🔮 未来 AI 或将成为远程医疗和预防性医疗体系的核心支撑技术

---

### [GitHub - google/wwwbasic: wwwBASIC 是一个可在 Node.js 和 Web 上运行的 BASIC 语言实现。 · GitHub](https://github.com/google/wwwbasic)

**原文标题**: [GitHub - google/wwwbasic: wwwBASIC is an implementation of BASIC that runs on Node.js and the Web. · GitHub](https://github.com/google/wwwbasic)

wwwBASIC 是一个专为在 Web 上轻松运行而设计的 BASIC 语言实现，支持在网页中直接嵌入或作为 Node.js 模块使用，具备图形绘制、输入处理等功能，并附带示例程序和可定制的绑定选项。

- 🌐 **Web 集成**：可直接在 HTML 中通过 `<script>` 标签嵌入，或作为 Node.js 模块导入运行。
- 🎨 **图形功能**：支持 24 位彩色、PSET、LINE、CIRCLE 等图形绘制指令。
- ⌨️ **输入处理**：提供 INKEY$、GETMOUSE 等输入方法，增强交互性。
- ⚙️ **灵活配置**：允许通过绑定选项自定义外部函数和行为，支持调试模式。
- 📚 **丰富示例**：包含经典程序如 DONKEY.BAS、图形演示和实时编辑器等示例。
- 🧪 **测试套件**：提供“进行中”的测试框架，可通过脚本运行验证功能。
- 📜 **开源许可**：采用 Apache 2.0 许可证，所有源文件均包含明确的版权和许可信息。

---

### [BASIC - 维基百科](https://en.wikipedia.org/wiki/BASIC)

**原文标题**: [BASIC - Wikipedia](https://en.wikipedia.org/wiki/BASIC)

BASIC 是一种为初学者设计的高级编程语言，由约翰·凯梅尼和托马斯·库尔茨于 1964 年在达特茅斯学院创建，旨在让非科学领域的学生也能使用计算机。它最初在分时系统上运行，后来随着微型计算机的普及，成为家用计算机的标准编程语言，尤其在 20 世纪 70 年代和 80 年代。尽管在 20 世纪 90 年代因更强大的编程语言出现而衰落，但微软在 1991 年发布的 Visual Basic 使其复兴，至今仍以 VB.NET 等形式存在。BASIC 以其易用性和广泛的应用而闻名，对编程教育和个人计算发展产生了深远影响。

- 🎓 **起源与设计**：BASIC 由约翰·凯梅尼和托马斯·库尔茨于 1964 年创建，旨在为非科学专业学生提供易用的编程语言，最初在达特茅斯分时系统上运行。
- 💻 **普及与扩展**：随着微型计算机的兴起，BASIC 成为家用计算机的标准语言，微软 BASIC 等方言广泛集成于系统中，并通过杂志和书籍传播程序代码。
- 📉 **衰落与复兴**：20 世纪 90 年代，BASIC 因更高级语言（如 Pascal 和 C）的普及而衰落，但微软在 1991 年发布 Visual Basic，结合可视化表单构建器，使其重新流行。
- 🔧 **现代变体**：BASIC 衍生出多种现代版本，如 Visual Basic .NET、QB64、FreeBASIC 等，并应用于游戏开发、教育计算器和移动设备编程。
- 📚 **语法与特点**：BASIC 语法简单，支持行号、控制结构（如 FOR 循环、IF 语句）和基本输入输出，后期版本增加了结构化编程和面向对象功能。
- 🌍 **影响与遗产**：BASIC 推动了编程普及，对早期计算机教育和个人计算发展有重要贡献，其教学用途后来被 Pascal、Java 和 Python 等语言继承。

---

### [GitHub - elixir-volt/quickbeam：适用于BEAM的JavaScript运行时——由OTP支持、原生DOM及内置TypeScript工具链驱动的Web API。· GitHub](https://github.com/elixir-volt/quickbeam)

**原文标题**: [GitHub - elixir-volt/quickbeam: JavaScript runtime for the BEAM — Web APIs backed by OTP, native DOM, and a built-in TypeScript toolchain. · GitHub](https://github.com/elixir-volt/quickbeam)

QuickBEAM 是一个为 BEAM 虚拟机设计的 JavaScript 运行时，它通过 OTP 提供 Web API 支持，内置原生 DOM 和 TypeScript 工具链，使 JavaScript 运行时能够作为 GenServer 运行在监督树中，并与 Erlang/OTP 库无缝交互。

- 🚀 **快速启动**：通过简单的 `QuickBEAM.start()` 和 `eval`/`call` 函数即可执行 JavaScript 代码，状态在调用间持久化。
- 🔗 **BEAM 集成**：JavaScript 可以调用 Elixir 函数、访问 OTP 库，并向任何 BEAM 进程发送消息，支持进程监控和分布式节点通信。
- 🧩 **监督与资源管理**：运行时和上下文池可作为 OTP 子进程，支持崩溃恢复；提供内存和操作限制，确保资源可控。
- 🌐 **API 支持**：可选择加载浏览器 API、Node.js API 或两者，提供完整的 Web API 实现（如 fetch、DOM、WebSocket 等）。
- 📦 **TypeScript 工具链**：内置 TypeScript 编译、压缩和打包功能，无需外部构建工具，支持直接运行和打包 TypeScript 代码。
- 🧠 **高性能与轻量级**：相比其他方案性能更优，上下文池设计支持高并发场景，显著降低内存和线程开销。
- 🔧 **开发与示例**：提供完整的开发质量检查（如格式化、测试）和多个示例（如实时聊天、AI 代理、SSR 等），便于集成和使用。

---

### [Elixir 编程语言](https://elixir-lang.org/)

**原文标题**: [The Elixir programming language](https://elixir-lang.org/)

Elixir 是一种动态函数式编程语言，专为构建可扩展且可维护的应用程序而设计。它运行在 Erlang 虚拟机上，支持高并发、分布式和容错系统，适用于 Web 开发、嵌入式软件、机器学习等多个领域。

- 🚀 **可扩展性**：Elixir 代码在轻量级进程（称为 processes）中运行，支持垂直和水平扩展，可高效利用多核、集群和 GPU 资源。
- 🛡️ **容错性**：通过监督者（supervisors）机制自动重启故障组件，确保系统从已知正常状态恢复，适合事件驱动和物联网等可靠架构。
- 🧩 **函数式编程**：采用模式匹配等特性，使代码简洁、可维护，并能强制约束条件，提升软件稳定性。
- 🔧 **可扩展性与 DSL**：语言设计灵活，支持领域特定语言（DSL），可轻松扩展以适应不同场景，如测试框架 ExUnit 支持并行测试和智能断言。
- 📦 **丰富的工具生态**：内置 Mix 构建工具，支持项目管理、测试和依赖管理（通过 Hex 包管理器），并与 Erlang 生态系统完全兼容。
- 💻 **交互式开发**：提供 IEx 交互式 Shell，支持自动补全、调试和代码重载；Livebook 代码笔记本允许浏览器中直接操作，集成绘图、机器学习等功能。
- 🌐 **生产实践**：被众多公司用于生产环境，涵盖 Web、流媒体、物联网等领域，依托 Erlang VM 实现分布式和高容错应用。

---

### [发布 v2.7.11 · denoland/deno · GitHub](https://github.com/denoland/deno/releases/tag/v2.7.11)

**原文标题**: [Release v2.7.11 · denoland/deno · GitHub](https://github.com/denoland/deno/releases/tag/v2.7.11)

Deno 项目在 GitHub 上的最新版本 v2.7.11 发布页面，展示了该版本的更新内容、社区互动及项目基本信息。

- 🚀 新增对 alpha 和 beta 发布通道的支持 (#33098)
- 🔧 修复了 ext/node 模块中 fs.watch 对即时写入事件触发的问题 (#32935, #32989)
- ⏱️ 将 watch 功能的优雅关闭超时时间从 5 秒缩短至 500 毫秒 (#33099)
- 📊 项目拥有 106k 星标、6k 复刻、2.1k 个议题和 200 个拉取请求，显示出活跃的社区参与
- 👍 发布获得了社区积极反馈，包括 7 个点赞、6 个爱心、5 个火箭和 1 个庆祝表情等互动

---

### [修复 (ext/node)：重写 Windows TTY 读取以匹配 libuv（控制台模式、编码、原始 + 行模式）by bartlomieju · Pull Request #32999 · denoland/deno · GitHub](https://github.com/denoland/deno/pull/32999)

**原文标题**: [fix(ext/node): rewrite Windows TTY reading to match libuv (console mode, encoding, raw + line mode) by bartlomieju · Pull Request #32999 · denoland/deno · GitHub](https://github.com/denoland/deno/pull/32999)

该拉取请求全面重写了 Deno 在 Windows 平台上的 TTY（终端）读写实现，以匹配 libuv 的行为，修复了之前 node:tty 重写引入的多个回归问题，确保交互式命令行工具（如 vite、inquirer）在 Windows 上能正常工作。

- 🛠️ **修复控制台模式恢复**：现在会正确保存并恢复原始的 Windows 控制台模式标志（包括快速编辑、插入模式等），避免交互式多步提示在首次原始模式切换后失效。
- 🌐 **统一 TTY 输出编码**：将 WriteFile 改为 WriteConsoleW，并转换 UTF-8 至 UTF-16，解决了非 UTF-8 代码页下 Unicode 字符（如框线、CJK 文字）显示乱码的问题。
- ⌨️ **重写原始模式读取**：使用 ReadConsoleInputW 替代 ReadFile，可正确处理所有输入事件（包括方向键、功能键），并映射为 VT100 转义序列，避免因 KEY_UP 等事件阻塞事件循环。
- 🧵 **实现行模式线程化读取**：将阻塞的 ReadConsoleW 移至工作线程执行，匹配 libuv 的 QueueUserWorkItem 方案，确保行模式输入（如 vite create）不会冻结整个事件循环。
- 🔔 **添加异步输入通知机制**：通过 RegisterWaitForSingleObject 注册控制台输入的单次等待，在输入可用时唤醒 tokio 事件循环，避免首次按键后事件循环休眠。
- 🚧 **完善资源清理与线程安全**：在关闭 TTY 时先拆除异步读取机制（取消等待注册、分离工作线程），再关闭控制台句柄，防止竞态条件和使用后释放问题。
- ✅ **新增多项测试验证**：包括原始模式切换、Unicode 输出、行模式读取、方向键映射、Ctrl+C 处理等 PTY 测试，确保各项修复功能稳定可靠。

---

### [GitHub - petersalomonsen/wasm-git：适用于Node.js和浏览器的GIT，使用通过https://emscripten.org编译为WebAssembly的https://libgit2.org · GitHub](https://github.com/petersalomonsen/wasm-git)

**原文标题**: [GitHub - petersalomonsen/wasm-git: GIT for nodejs and the browser using https://libgit2.org compiled to WebAssembly with https://emscripten.org · GitHub](https://github.com/petersalomonsen/wasm-git)

Wasm-git 是一个将 libgit2 编译为 WebAssembly 的项目，使 Git 功能能在 Node.js 和浏览器中运行，主要用于在浏览器中本地存储 Web 应用数据，并可选择与远程服务器同步。

- 🚀 **项目目的**：将 Git 引入浏览器，支持 Web 应用数据的本地存储和远程同步。
- 🔧 **技术栈**：基于 libgit2（v1.7.1）和 Emscripten（4.0.23），兼容 Node.js v18+ 和现代浏览器。
- 🌐 **演示与示例**：提供在线演示、示例视频和代码示例，展示克隆、编辑、提交、推送等操作。
- 📦 **构建版本**：支持同步、异步和 OPFS 三种版本，分别适用于不同场景（如 Web Worker、Asyncify、持久化存储）。
- 🛠️ **开发与构建**：提供完整的开发指南，包括环境设置、构建命令和测试方法，支持 GitHub Codespaces 快速上手。
- 💾 **文件系统后端**：支持 MEMFS、IDBFS、NODEFS 和 OPFS，其中 OPFS 版本性能更优，但需在 Web Worker 中运行并配置特定 HTTP 头。
- ⚠️ **故障排除**：列出常见问题（如构建错误、测试失败）和所需的 Emscripten 修复补丁。

---

