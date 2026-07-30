### [](https://evilmartians.com/chronicles/the-secure-way-to-release-an-npm-package)

**原文标题**: [The secure way to release an npm package in 2026—Martian Chronicles, Evil Martians’ team blog](https://evilmartians.com/chronicles/the-secure-way-to-release-an-npm-package)

npm 包的安全发布正面临供应链攻击的严峻挑战，本文提供了 2026 年的最佳实践指南，涵盖从基础设施配置到日常开发习惯的完整防护方案。

- 🛡️ 使用 npm Trusted Publishing 彻底消除令牌泄露风险，并配合 Staged Publishing 实现手动审核
- 🔐 启用 npm Provenance 签名，证明包来自指定 CI 流程，并获取安全徽章
- ⚙️ 加固 CI 工作流：用 zizmor 或 CodeQL 检测漏洞，删除旧分支，防止“历史攻击”
- 📌 通过 SHA 提交哈希锁定第三方 CI 动作，使用 actions-up 工具管理，避免标签被篡改
- ⏳ 为依赖设置 3 天冷却期（npm/pnpm/yarn/bun 均有配置），拦截 94% 的恶意包
- 🔍 减少依赖数量，优先替换深层嵌套的大型包，使用 e18e 工具分析并寻找替代品
- 🖥️ 采用 Dev Container 隔离开发环境，限制 IDE 扩展和依赖对系统的访问
- 🚫 在发布作业中最小化依赖：仅安装构建必需的工具，禁用脚本和缓存，防止注入
- 🏷️ 在 GitHub 上设置标签创建规则（仅管理员），配合 Staged Publishing 加强发布控制
- 🧹 审查所有环境（Docker 镜像、IDE 扩展、Python 包等），管理更新并保持锁文件

---

### [获取失败](https://www.npmjs.com/package/postcss)

**原文标题**: [Failed to retrieve](https://www.npmjs.com/package/postcss)

无法总结：获取内容失败，状态码 403。

---

### [](https://github.com/ai/nanoid)

**原文标题**: [GitHub - ai/nanoid: A tiny (118 bytes), secure, URL-friendly, unique string ID generator for JavaScript · GitHub](https://github.com/ai/nanoid)

概述摘要  
Nano ID 是一款小巧（118字节）、安全、URL友好的唯一字符串ID生成器，专为JavaScript设计，性能比原生 crypto.randomUUID() 快50%，支持自定义字母表、随机生成器，并已移植到超过20种编程语言。

- 📏 极小体积：仅118字节（压缩后），无依赖，由Size Limit控制大小。  
- ⚡ 高性能：比原生 crypto.randomUUID() 快50%，基准测试显示每秒超2000万次操作。  
- 🔒 高安全性：使用硬件随机生成器（Node.js crypto 模块或 Web Crypto API），适用于集群环境。  
- 🔤 短ID：采用更大字母表（A-Za-z0-9_-），ID长度从36符号缩减到21符号，碰撞概率与UUID v4相近。  
- 🌐 可移植性：已移植到C、C#、Go、Python、Rust等20多种语言，支持前后端统一ID生成。  
- 🛠 定制灵活：支持自定义字母表、ID大小和随机生成器（如种子生成器），且提供非安全版本用于无硬件随机源的环境。  
- 📦 安装多样：通过npm、JSR、CDN均可安装，也可通过CLI（npx nanoid）直接生成ID。  
- ⚛️ 使用注意：React中不推荐用 nanoid() 作为 key 或替代 stable ID；React Native 需安装 polyfill。  
- 💻 类型支持：TypeScript 可利用 opaque types 进行类型安全，支持将生成字符串强制转换为特定类型。  
- 🧰 配套工具：提供ID碰撞概率计算器、常用字母表字典、以及过滤敏感词的 nanoid-good。

---

### [](https://dashboard.render.com/register?utm_source=email&utm_medium=newsletter&utm_campaign=2026_newsletter_cooperpress&utm_content=nodejs_weekly)

**原文标题**: [Render · The Easiest Cloud For All Your Apps](https://dashboard.render.com/register?utm_source=email&utm_medium=newsletter&utm_campaign=2026_newsletter_cooperpress&utm_content=nodejs_weekly)

该文本指示用户启用JavaScript以运行应用程序。  
- ⚙️ 需要启用JavaScript才能运行此应用

---

### [npm 发布时的恶意软件扫描与双用途元数据 - GitHub 变更日志](https://github.blog/changelog/2026-07-28-npm-publish-time-malware-scanning-and-dual-use-metadata/)

**原文标题**: [npm publish-time malware scanning and dual-use metadata - GitHub Changelog](https://github.blog/changelog/2026-07-28-npm-publish-time-malware-scanning-and-dual-use-metadata/)

npm 在发布时引入自动恶意软件扫描，并新增双用途内容元数据要求，以加强供应链安全性。

- 🔍 新发布的包在可用前会自动扫描，根据结果正常发布、人工审查或阻止
- ⏳ 发布后会有约5分钟的延迟，高峰时可能达15分钟以上，需更新自动化流程以适应
- 🚫 被阻止的包可申诉，npm 将持续改进检测能力
- 📄 引入 `contentPolicy` 字段和 `DISCLOSURE` 文件，声明双用途内容（兼具安全相关功能的合法包）
- 🔐 双用途包必须通过强制2FA的方式发布（如OIDC、交互式会话或分阶段发布）
- 📑 双用途元数据声明必须持续保留，新版本不可移除，否则将被拒绝

---

### [Node.js — 2026年7月29日，星期三 安全发布](https://nodejs.org/en/blog/vulnerability/july-2026-security-releases)

**原文标题**: [Node.js — Wednesday, July 29, 2026 Security Releases](https://nodejs.org/en/blog/vulnerability/july-2026-security-releases)

Node.js 项目发布了针对 26.x、24.x、22.x 版本的安全更新，修复了从高到低多个严重级别的漏洞，包括 HTTP/2 内存耗尽、堆释放后重用、权限模型绕过等问题，建议用户尽快升级。

- 🛡️ 安全版本发布：Node.js 26.5.1、24.18.1、22.23.2 已推出，修复 11 个安全漏洞。
- ⚙️ 依赖更新：升级 undici（6.28.0/7.29.0/8.9.0）和 llhttp（9.4.3），修复已知公开漏洞。
- 🚨 **高危漏洞**：
  - HTTP/2 保留头可绕过 `maxSessionMemory` 限制导致远程内存耗尽（CVE-2026-56846），影响 24.x、22.x。
  - HTTP/2 重入发送导致堆释放后重用（CVE-2026-56848），影响 26.x、24.x、22.x。
  - 权限模型路径匹配可越权访问文件系统（CVE-2026-58043），影响 22.x、24.x、26.x。
- ⚠️ **中危漏洞**：
  - HTTPS Agent 多 PFX 证书碰撞导致 mTLS 身份重用（CVE-2026-56850）。
  - HTTPS Agent 会话重用跳过主机名校验（CVE-2026-58040）。
  - `node:sqlite` 的 SQLTagStore 迭代器可重复执行写操作（CVE-2026-58041），影响 26.x、24.x。
  - `dns.resolveAny()` 遇到超过 256 条 A 记录时可中止进程（CVE-2026-58042）。
  - `node:zlib` 同步 API 处理伪造的 TypedArray 长度可崩溃（CVE-2026-58045）。
- 🟢 **低危漏洞**：
  - 权限模型允许 trace 事件写入白名单外路径（CVE-2026-56847）。
  - 权限模型允许 `process.report` 写入白名单外文件（CVE-2026-58039）。
  - HTTP 解析器头截断可导致请求走私（CVE-2026-58044）。
- 📅 发布时间调整：因基础设施问题，原定 7 月 29 日的发布推迟至 7 月 28 日。
- 🔧 建议所有用户升级到受支持的最新版本（26.x/24.x/22.x），End-of-Life 版本也存在风险。

---

### [Node.js — Node.js 26.5.1 (当前)](https://nodejs.org/en/blog/release/v26.5.1)

**原文标题**: [Node.js — Node.js 26.5.1 (Current)](https://nodejs.org/en/blog/release/v26.5.1)

Node.js 26.5.1 是一个安全发布版本，修复了多个高危、中危和低危漏洞，并更新了关键依赖。

- 🔒 高危：修复 http2 中的作用域内延迟 rst 流问题（CVE-2026-56848）
- 🔒 高危：修复 permission 模块中避免授予 radix 分割节点权限（CVE-2026-58043）
- 🛡️ 中危：修复 https 中区分 PFX 对象数组代理键（CVE-2026-56850）
- 🛡️ 中危：修复 https 中绑定身份检查以复用会话（CVE-2026-58040）
- 🛡️ 中危：修复 sqlite 中重置语句时标签存储迭代器失效（CVE-2026-58041）
- 🛡️ 中危：修复 dns 中处理大型 resolveAny 地址回复（CVE-2026-58042）
- 🛡️ 中危：修复 zlib 中越界写入缓冲区抛出异常（CVE-2026-58045）
- 🟢 低危：修复 permission 中针对 trace events 强制执行写权限（CVE-2026-56847）
- 🟢 低危：修复 permission 中检查最终报告输出路径（CVE-2026-58039）
- 🟢 低危：修复 http 中拒绝超过最大 header 数量的请求（CVE-2026-58044）
- 📦 依赖更新：llhttp 更新至 9.4.3
- 📦 依赖更新：undici 更新至 8.9.0

---

### [Node.js — Node.js 24.18.1 (LTS)](https://nodejs.org/en/blog/release/v24.18.1)

**原文标题**: [Node.js — Node.js 24.18.1 (LTS)](https://nodejs.org/en/blog/release/v24.18.1)

Node.js 24.18.1 (LTS) 是一个安全发布版本，修复了多个高危、中危和低危漏洞，并更新了依赖包。

- 🔒 修复了两个高危 HTTP/2 漏洞：保留会话内存中的标头（CVE-2026-56846）和延迟作用域内的 RST_STREAM（CVE-2026-56848）
- 🛡️ 修复了高危权限漏洞：避免授予进制拆分节点（CVE-2026-58043）
- ⚠️ 修复了三个中危漏洞：HTTPS 的 PFX 对象数组代理键区分（CVE-2026-56850）、HTTPS 身份检查绑定到会话复用（CVE-2026-58040）、SQLite 标签存储迭代器在重置语句时失效（CVE-2026-58041）
- 📦 修复了其他中危漏洞：DNS 处理大型 resolveAny 地址回复（CVE-2026-58042）和 zlib 对越界写入缓冲区抛出错误（CVE-2026-58045）
- 🔧 修复了三个低危漏洞：权限模块的 fs 写入权限检查（CVE-2026-56847）、最终报告输出路径检查（CVE-2026-58039）、HTTP 拒绝超过最大标头数的请求（CVE-2026-58044）
- 🔄 更新了核心依赖：llhttp 升级至 9.4.3，undici 升级至 7.29.0
- 💻 提供了各平台的安装包和二进制文件，包括 Windows、macOS、Linux、AIX 等
- 📝 发布了 SHA256 校验和及 PGP 签名，确保下载完整性

---

### [Node.js — Node.js 22.23.2 (LTS)](https://nodejs.org/en/blog/release/v22.23.2)

**原文标题**: [Node.js — Node.js 22.23.2 (LTS)](https://nodejs.org/en/blog/release/v22.23.2)

Node.js 22.23.2（LTS）为安全发布版本，修复了多个高危、中危和低危漏洞，并更新了llhttp和undici依赖。

- 🔒 修复三个高危漏洞：http2内存管理、rst_stream作用域及权限问题（CVE-2026-56846/56848/58043）
- ⚠️ 修复四个中危漏洞：https密钥区分、身份检查、dns大响应处理及zlib写入边界检查（CVE-2026-56850/58040/58042/58045）
- 🛡️ 修复三个低危漏洞：权限检查、请求头超限拒绝等（CVE-2026-56847/58039/58044）
- 📦 更新llhttp至9.4.3，undici至6.28.0
- 📋 提供各平台安装包及SHA256校验值

---

### [](https://devblogs.microsoft.com/ifdef-windows/a-new-way-to-bring-native-windows-apis-to-javascript-introducing-dynamic-api-projections-for-node-js/)

**原文标题**: [A new way to bring native Windows APIs to JavaScript - introducing dynamic API projections for Node.js - #ifdef Windows](https://devblogs.microsoft.com/ifdef-windows/a-new-way-to-bring-native-windows-apis-to-javascript-introducing-dynamic-api-projections-for-node-js/)

概述：微软推出了动态Windows Runtime API（WinRT）投影的公开预览版，使 Electron 或纯 Node.js 应用能直接从 JavaScript/TypeScript 调用原生 Windows API，无需编写 C++ 或 C# 桥接。该投影通过代码生成 JavaScript 包装和类型声明，依赖共享运行时执行调用，支持非 UI 的 WinRT API，包括设备端 AI、通知、存储等，可灵活扩展。

- 🚀 全新方式：动态 WinRT 投影让 Node.js/Electron 直接调用 Windows API，无需 C++ 桥接或 node-gyp 配置。
- 📦 核心组件：三个 npm 包——@microsoft/winappcli（协调）、@microsoft/dynwinrt-codegen（生成 JS 包装和 .d.ts 声明）、@microsoft/dynwinrt（共享运行时）。
- 🔧 无需编译：代码生成 JavaScript 包装，而非逐类原生插件，更新 API 元数据只需重新生成而非重新编译。
- 💡 支持场景：设备端 AI（Phi Silica）、通知、文件选择器、剪贴板、网络等非 UI 的 WinRT API，并可自定义 WinRT 组件。
- 📋 示例一：通过 AppNotificationBuilder 和 AppNotificationManager 显示原生 Windows 通知（含进度条）。
- 🤖 示例二：在 Copilot+ PC 上调用 Phi Silica 语言模型，实现文本摘要（支持流式输出）。
- ⚙️ 项目设置：使用 `npx winapp init` 创建项目，自动生成清单、绑定文件和导入映射；调试时需添加临时包标识。
- 🔄 扩展性：在 package.json 中添加额外命名空间或 .winmd 文件路径，可包含 Windows SDK 或第三方组件 API。
- 🖥 纯 Node.js：也可在普通 Node.js 进程中使用，通过 `npx winapp run` 注册临时包标识运行。
- 📚 反馈与资源：公共预览阶段，API 映射或类型声明问题可提交到微软 WinApp CLI 或 dynwinrt 仓库。

---

### [](https://aws.amazon.com/blogs/security/amazon-identifies-north-korean-hacker-group-behind-open-source-supply-chain-attacks/)

**原文标题**: [Amazon identifies North Korean hacker group behind open-source supply chain attacks | AWS Security Blog](https://aws.amazon.com/blogs/security/amazon-identifies-north-korean-hacker-group-behind-open-source-supply-chain-attacks/)

亚马逊安全博客指出，一个与朝鲜有关联的黑客组织正通过社会工程学攻击开源软件供应链，已入侵多个流行的NPM库（如axios、debug、chalk和typo-crypto）。攻击手法不断进化，包括碎片化恶意代码、长期信任积累、动态远程加载及强加密。生成式AI使攻击更易扩散，而AWS正通过威胁情报、Amazon Inspector及行业合作加强防御。

- 🔍 亚马逊威胁情报确认，同一朝鲜黑客组织（SAPPHIRE SLEET等）先后入侵了typo-crypto（2025年3月）、debug和chalk（2025年9月）以及axios（2026年3月）等热门NPM库，通过社会工程学骗取维护者权限后发布恶意更新。
- 🧩 攻击手法从单一恶意包转向碎片化：将恶意行为拆分到多个看似无害的包中，只有组合使用时才触发，以规避静态扫描。
- ⏳ 长期信任积累：攻击者先发布有用代码并长期维护，甚至成为项目贡献者，之后才在关键时刻植入后门（类似XZ Utils案例）。
- 🛠️ 恶意行为与包解耦：代码看似干净，但实际行为依赖于攻击者控制的远程服务器或文件，可随时切换，无需发布新版本。
- 🔒 强加密与多阶段载荷：使用AES-GCM、RC4、多层XOR等加密技术，解密密钥不在包内，需运行时从环境或远程获取，静态分析难以还原。
- 🕵️ 沙箱逃逸：恶意代码通过检查交互式终端、真实环境特征（用户名、主机名、云元数据等）决定是否执行，避免在分析环境中触发。
- 🤖 生成式AI改变攻防：攻击者利用AI生成逼真的代码、文档和提交历史，难以通过模式匹配检测；出现“slopsquatting”（利用AI幻觉注册不存在的包名）；攻击者还可能在代码中嵌入提示注入，欺骗AI审查系统。
- 🛡️ AWS应对措施：Amazon Threat Intelligence与Amazon Inspector更新检测逻辑，通过GuardDuty告警客户，加入Akrites倡议（由Linux基金会领导），并联合投资1250万美元保护开源生态免受AI驱动攻击。

---

### [针对你的](https://developers.cloudflare.com/changelog/post/2026-07-21-integration-test-harness/)

**原文标题**: [Run integration tests against your Worker's production build Â· Changelog](https://developers.cloudflare.com/changelog/post/2026-07-21-integration-test-harness/)

概述总结  
Cloudflare Wrangler 发布 `createTestHarness()` API，用于在 Node.js 测试运行器中对 Worker 的生产构建进行集成测试，支持多 Worker 路由、模拟外部请求、Playwright 测试等，并推荐替代旧版 API。

- 🚀 新增 `createTestHarness()` API，支持对 Wrangler 或 Vite 插件构建的 Worker 运行集成测试  
- 🧪 测试工具启动本地 Worker 服务器，提供请求分发、存储重置、运行时日志检查等帮助函数  
- 🎯 适用场景：多 Worker 间路由请求、用 MSW 模拟 `fetch()`、运行 Playwright 测试  
- 📝 示例代码展示如何启动两个 Worker 并模拟上游 API，使用 Vitest 和 MSW 进行断言  
- ⚠️ 推荐使用 `createTestHarness()` 代替旧的 `unstable_startWorker()` 或 `unstable_dev()`  
- 📘 详细用法请参考“集成测试指南”

---

### [Node.js — 查看新的 Node.js API 文档预览](https://nodejs.org/en/blog/announcements/new-api-docs-beta)

**原文标题**: [Node.js — Check out the New Node.js API Documentation Preview](https://nodejs.org/en/blog/announcements/new-api-docs-beta)

Node.js API 文档预览版已上线 beta.docs.nodejs.org，内容不变但重构了导航、布局和搜索，并统一了设计系统，现面向社区征集反馈。

- 🔍 新增内置搜索：每页提供搜索框及快捷键，无需借助搜索引擎即可跳转任意 API
- 🎨 统一设计系统：采用与 nodejs.org 相同的设计，包含持久侧边栏、始终可见页面目录及响应式布局
- 📄 新增 llms.txt：为 AI 工具提供结构化 API 参考入口
- ⏱️ 附加功能：显示阅读时间和公告栏，提升使用体验
- ♿ 无障碍设计：即使禁用 JavaScript 或离线也能正常使用
- ⚙️ 基于 doc-kit 构建：独立工具替代旧版文档生成器，可在其仓库报告问题
- 💬 征集反馈：欢迎在 nodejs/doc-kit 仓库提交任何建议，开发进入最终阶段
- 🙏 致谢团队：感谢 Node.js Web 团队及社区贡献者的共同协作

---

### [Node.js — 随处运行 JavaScript](https://nodejs.org/en)

**原文标题**: [Node.js — Run JavaScript Everywhere](https://nodejs.org/en)

Node.js® 是一个免费、开源、跨平台的 JavaScript 运行时环境，可用于构建服务器、Web 应用、命令行工具和脚本。提供安全支持和学习资源，并附有简单 HTTP 服务器的代码示例。

- 🌐 免费、开源、跨平台，让 JavaScript 运行在服务器端
- 🛠️ 可创建服务器、Web 应用、命令行工具和脚本
- 🔒 为已停止支持的 Node.js 版本提供安全更新
- 🤝 由多家合作伙伴支持
- 📄 提供 HTTP 服务器示例代码：监听 3000 端口返回 "Hello World!"
- 📚 提供学习资料供深入探索

---

### [索引 | Node.js 26.5](https://beta.docs.nodejs.org/)

**原文标题**: [Index | Node.js 26.5.0 Documentation](https://beta.docs.nodejs.org/)

Node.js的API列表中，大多数模块（如HTTP、File system、Crypto等）状态为“稳定”，少数如Async hooks、FFI、Trace events等为“实验性”，Domain和Punycode已弃用，SQLite处于候选发布阶段，Single executable applications在积极开发中。

- 📦 稳定模块：包括Buffer、Child process、Cluster、Console、Crypto、DNS、Events、File system、HTTP、HTTP/2、HTTPS、Inspector、Modules、Net、Node-API、OS、Path、Performance、Query string、Readline、REPL、Stream、String decoder、Test runner、Timers、TLS、TTY、UDP/datagram、URL、Util、VM、Web Crypto API、Web Streams API、Worker threads、Zlib等
- 🧪 实验性模块：Async hooks、FFI、Iterable Streams、Trace events、Virtual File System、WASI
- ⚠️ 已弃用模块：Domain、Punycode
- 🔄 活跃开发中：Single executable applications（状态1.1）
- 🏗️ 候选发布：SQLite（状态1.2）

---

### [阻断npm和GitHub Actions上的供应链攻击 - GitHub博客](https://github.blog/security/supply-chain-security/disrupting-supply-chain-attacks-on-npm-and-github-actions/)

**原文标题**: [Disrupting supply chain attacks on npm and GitHub Actions - The GitHub Blog](https://github.blog/security/supply-chain-security/disrupting-supply-chain-attacks-on-npm-and-github-actions/)

过去几个月，npm和GitHub Actions针对供应链攻击发布了多项安全改进，从初始入侵、凭据窃取到攻击传播和响应，多层次破坏常见攻击手法并限制其影响。

- 🔒 高影响力npm账户在更换邮箱或使用2FA恢复码后，进入72小时只读模式，防止账户被盗后立即发起攻击
- 🛡️ 改动 `actions/checkout` 默认行为，阻止从分叉检出不可信代码，切断“pwn请求”攻击路径
- ⚙️ 新增企业/组织/仓库级别策略，限制谁可以触发工作流及触发类型，减少CI/CD攻击面
- 🚫 针对不可信触发器的Actions缓存设为只读，阻止攻击者通过缓存投毒提升权限
- 🔑 npm可信发布新增CircleCI支持，消除CI/CD流水线中的长期凭据，从源头减少凭据泄露风险
- 🕵️ Actions网络防火墙（技术预览版）记录所有出站流量，便于检测恶意下载或凭据外传
- 📦 npm分阶段发布：即使拥有凭据，新包也需额外审批和2FA认证才能发布，切断CI/CD到恶意分发的链条
- ⚠️ npm v12默认禁用安装脚本（及git/远程URL依赖），阻止攻击者在安装时执行代码窃取凭据
- ⏳ Dependabot版本更新默认等待3天再创建PR（安全更新除外），给检测信号留出时间，减慢恶意版本扩散
- 🔐 自服务凭据撤销功能：企业成员可即时撤销自己所有凭据，用于事件响应
- 🛠️ 凭据撤销API扩展支持GitHub OAuth和App token，方便社区快速撤销泄露的凭据

---

### [在六小时内发现NodeBB中的八个高严重性漏洞](https://www.aikido.dev/blog/eight-high-severity-vulnerabilities-nodebb)

**原文标题**: [Finding eight high-severity vulnerabilities in NodeBB in six hours](https://www.aikido.dev/blog/eight-high-severity-vulnerabilities-nodebb)

在 NodeBB 版本低于 4.14.0 中发现了八个高危漏洞，涉及 XSS、权限绕过、数据泄露和操作篡改，所有漏洞均已在最新版本中修复。以下是各漏洞的要点总结：

- 💻 **自定义联邦服务器头像 XSS**：通过搭建恶意服务器返回含 XSS 的图片 URL，触发任意 JavaScript 执行。
- 📋 **联邦错误日志 XSS**：向管理员错误日志注入未转义的 HTML 代码，利用签名验证绕过实现攻击。
- 🔀 **翻译模板注入 XSS**：利用翻译机制在 URL 或表单参数中嵌入 `[[...]]` 语法，结合模板漏洞执行脚本。
- 🚪 **自定义首页绕过管理员权限**：设置首页为 `/admin` 即可跳过中间件权限检查，访问管理面板及部分 API。
- 🕵️ **用户 ID 伪造读取私信**：通过未验证签名的 GET 请求，冒用任意用户 ID 获取私密消息。
- ✏️ **PID 批量赋值劫持帖子**：在创建主题时指定 `pid` 参数，覆盖已有帖子内容，用于篡改信息。
- 🔓 **未认证读取所有分类**：使用 ActivityPub 头访问 `/category/:cid/outbox`，无需登录即可获取私有分类的全部内容。
- 📈 **未检查行为者无限点赞**：通过 `Announce` 消息封装 `Like` 操作，绕过签名验证，批量伪造点赞。

---

### [](https://nodogmablog.bryanhogan.net/2026/07/running-npm-in-a-separate-container-when-using-claude/)

**原文标题**: [Running npm in a Separate Container when using Claude | no dogma blog](https://nodogmablog.bryanhogan.net/2026/07/running-npm-in-a-separate-container-when-using-claude/)

使用临时容器运行 npm 来生成 `package-lock.json`，避免在主容器或主机上安装 Node 和 npm。

- 🐳 创建临时容器，挂载与 Claude 容器相同的源码目录
- 📦 在临时容器内安装 Node 和 npm (`apk add nodejs npm`)
- 🔒 运行 `npm install` 生成 `package-lock.json` 锁定依赖版本
- 🗑️ 关闭临时容器后，Node 和 npm 随之消失，但锁文件保留在宿主机上
- 🔄 此方法可推广到其他临时工具需求

---

### [使用Testcontainers对Node.js进行集成测试](https://flaviocopes.com/nodejs-testcontainers/)

**原文标题**: [Integration testing Node.js with Testcontainers](https://flaviocopes.com/nodejs-testcontainers/)

本教程展示了如何使用Testcontainers在Node.js中针对真实PostgreSQL数据库编写集成测试，涵盖容器启动、数据库创建、测试隔离、约束验证、迁移同步及CI集成。

- 🐳 使用Testcontainers在测试中启动临时PostgreSQL容器，提供真实数据库连接，避免模拟缺失的类型约束和SQL行为
- 🛠️ 通过`PostgreSqlContainer`启动容器并获取动态映射端口，无需硬编码5432，避免端口冲突
- 📋 在`beforeAll`中创建数据库表，`beforeEach`中通过`TRUNCATE TABLE RESTART IDENTITY`实现隔离，确保每个测试独立
- 🔍 编写真实SQL查询的集成测试，验证`createBooksRepository`的`create`和`findByAuthor`方法，确保语法和约束正确
- ⛔ 测试数据库约束，如NOT NULL违反，通过检查PostgreSQL错误码（如23502）而非易变的错误消息
- 🔄 在测试中运行与生产相同的迁移脚本，确保迁移执行顺序和数据库模式一致性，避免旧开发数据库隐藏问题
- 🧹 在`afterAll`中安全关闭客户端并停止容器，使用可选链处理部分失败场景，Testcontainers资源回收器辅助清理
- 🚀 在CI（如GitHub Actions）中无需额外PostgreSQL服务，测试自身管理依赖，确保可重复环境

---

### [scriptc | TypeScript到原生编译器](https://scriptc.dev/)

**原文标题**: [scriptc | TypeScript-to-Native Compiler](https://scriptc.dev/)

scriptc 将普通 TypeScript 编译为小型、快速的原生二进制文件，无需 Node 或 V8 引擎。它采用三层架构确保透明性：静态编译（默认）、动态运行（可选嵌入约 620KB 引擎）、编译时拒绝。支持绝大多数 TypeScript 语法，二进制文件仅约 320KB，启动约 4ms，并提供覆盖率报告和差异性测试来保证正确性。

- 🧊 **默认静态编译**：类、闭包、async/await 等直接转为原生代码，行为与 Node 完全一致，不依赖任何引擎。
- ⚙️ **动态降级**：通过 `--dynamic` 选项嵌入小型 JS 引擎（~620KB），处理无法静态编译的 npm 依赖或任意类型代码，静态部分仍保持高速。
- ❌ **编译时拒绝**：无法编译的构造会给出明确错误码、代码片段和重写提示，杜绝静默误编译。
- ✅ **零代码改动**：直接使用标准 TypeScript，无需添加注解或更改语法，与普通 Node 项目兼容。
- 🚀 **小巧快速**：hello-world 二进制仅约 320KB，启动约 4ms，仅依赖 libSystem；对比 Node 需要 ~120MB 运行时和 ~35ms。
- 📊 **可测量覆盖率**：`scriptc coverage` 逐语句展示静态编译与动态需求，定位具体需要引擎的代码位置。
- 🔬 **差异性测试**：所有程序同时在 Node 和原生二进制中运行，stdout、stderr 和退出码必须逐字节匹配，且通过 AddressSanitizer 检测。

---

### [GitHub - vercel-labs/scriptc: TypeScript到原生编译器 · GitHub](https://github.com/vercel-labs/scriptc)

**原文标题**: [GitHub - vercel-labs/scriptc: TypeScript-to-Native Compiler · GitHub](https://github.com/vercel-labs/scriptc)

scriptc 是一个将 TypeScript 直接编译为原生可执行文件的零运行时编译器，无需 Node.js 或 JavaScript 引擎，生成的二进制文件小巧且启动迅速。

- 🚀 **零运行时编译**：scriptc 将普通 TypeScript 编译成原生二进制（约 178KB），启动时间仅约 2ms，无需 Node.js 或 V8。
- 📦 **安装与平台**：通过 `npm install -g scriptc` 安装，需 clang，主要支持 macOS arm64，Linux 和 Windows 通过交叉编译。
- 🔍 **三个编译层级**：静态编译（默认，原生代码）、动态运行（嵌入 quickjs-ng 引擎，约 620KB）、拒绝编译（给出错误码和改写提示）。
- ⚙️ **支持的语言特性**：类、闭包、泛型、async/await、异常、解构、正则表达式等，以及 Node 核心 API（fs、http、crypto 等）。
- ✅ **正确性保障**：通过差异化测试（与 Node 逐字节对比）和 AddressSanitizer 内存安全检测，所有变更需通过双重验证。
- 🏎️ **性能优秀**：启动约 2.4ms（对比 Node 的 47ms），内存占用 1-4MB（对比 Node 的 67-116MB），运行时速度与系统语言相当。
- 🔧 **逃生舱机制**：`comptime` 宏、原生 FFI、动态模式、运行时类型校验，灵活处理无法静态编译的代码。
- 🏗️ **模块化架构**：编译器前端（TypeScript → IR）、运行时（C 语言实现引用计数、纤程等）、CLI 工具，链接时按需加载。
- ⚡ **开发流程**：使用 pnpm 构建，支持差异化测试、ASan 检查、Sandbox 并行测试，合并前需两个测试通道均为绿色。

---

### [适用于任意规模时间序列工作负载的Postgres | Tiger Data](https://www.tigerdata.com/go/trial?utm_source=content-syndication&utm_medium=referral&utm_campaign=node-weekly-newsletter)

**原文标题**: [Postgres for time-series workloads at any scale. | Tiger Data](https://www.tigerdata.com/go/trial?utm_source=content-syndication&utm_medium=referral&utm_campaign=node-weekly-newsletter)

Tiger Cloud 提供可大规模扩展的 Postgres 时间序列服务，支持 IoT 等场景，具备企业级合规、高可用和深度可观测性，并附带 1000 美元试用额度。

- 🚀 单实例支持每天 3 万亿指标、3 PB 数据、1 千万亿数据点，展示真实扩展能力
- 💰 新用户获 1000 美元信用额度（30 天有效），无需信用卡
- 🔄 弹性扩展：读写分离（最多 10 个副本节点），结合 SSD/S3 分层存储，降低成本
- ⚡ 独立扩展计算与存储，避免为闲置容量付费
- 🔒 高可用：多可用区集群、自动故障转移、时间点恢复与跨区域备份
- 🛡️ 企业级合规：SOC 2、HIPAA、GDPR，自带加密、SSO、RBAC 和审计日志
- 📊 深度可观测：查询下钻与仪表盘，支持 CloudWatch、Datadog、Prometheus 等指标导出
- ⏱️ 快速部署：数分钟内创建数据库，支持 SQL、CLI、Terraform、Cursor 或 Claude Code 管理
- 🔌 集成主流云提供商和 Postgres 生态系统
- 🏢 企业特性：SLA 保障、区域数据隔离、24/7 全球专家支持

---

### [](https://tslog.js.org/)

**原文标题**: [tslog: Beautiful logging experience for TypeScript and JavaScript](https://tslog.js.org/)

tslog v5 是一个为 TypeScript 和 JavaScript 设计的高性能、零依赖的通用日志库，支持 Node.js、浏览器、Deno、Bun 等平台，默认提供彩色可读输出，并可选结构化 JSON 格式，内置秘密遮罩、子日志器、传输和中间件等功能，旨在同时满足开发和生产环境的需求。

- 🧩 **跨平台统一日志**：一套代码可在 Node.js、浏览器、Deno、Bun、React Native 等任意环境运行，无需额外适配。
- 🚀 **零依赖与高性能**：运行时无外部依赖，通过批处理 stdout、懒加载栈捕获等优化提升速度，预设和传输可摇树优化。
- 🌈 **默认美观输出**：交互终端带颜色，管道/CI 时自动去色，浏览器中支持 CSS 样式和可折叠对象。
- 📊 **结构化 JSON 输出**：通过 `type: "json"` 切换为扁平、字段优先的 JSON，适配日志管道，支持自定义字段名。
- 🛡️ **内置秘密遮罩**：支持按键名、路径、正则表达式遮罩敏感信息，可替换为占位符或哈希值。
- 👨‍👩‍👧 **子日志器与继承**：通过 `child()` 或 `getSubLogger()` 创建子日志器，继承父级设置并累积名称，便于模块/请求级追溯。
- 🔌 **可插拔传输与中间件**：内置文件、HTTP、环形缓冲、工作线程传输，支持自定义传输和中间件来修改/丢弃日志。
- 🔗 **OpenTelemetry 与 AI 支持**：提供 OTel-GenAI 预设、异步上下文关联，适合 LLM 和智能体场景。

---

### [GitHub - fullstack-build/tslog: 📝 tslog - 适用于 TypeScript 和 JavaScript 的通用日志记录器 · GitHub](https://github.com/fullstack-build/tslog)

**原文标题**: [GitHub - fullstack-build/tslog: 📝 tslog - Universal Logger for TypeScript and JavaScript · GitHub](https://github.com/fullstack-build/tslog)

tslog v5 是一个通用的 TypeScript/JavaScript 日志库，支持 Node.js、浏览器、Deno、Bun 等多种运行时，提供漂亮的终端输出、结构化 JSON、秘密屏蔽、子日志器、中间件和传输等功能，旨在成为一站式的日志解决方案。

- 🌍 **通用运行时** — 一个日志库即可覆盖 Node.js、浏览器、Deno、Bun、React Native 等环境
- 📦 **结构化字段优先 JSON** — 扁平化的 JSON 输出，可直接接入日志管道，支持自定义时间戳和字段名
- 🎨 **默认漂亮输出** — 终端自动配色，管道/CI 环境自动去色，无需额外配置
- 🔒 **秘密屏蔽** — 支持键名、路径、正则表达式和哈希屏蔽，防止敏感信息泄露
- 👨‍👧‍👦 **子日志器继承** — `child()` / `getSubLogger()` 继承父配置，名称自动累积
- 🔌 **可插拔传输与中间件** — 支持文件、HTTP、环形缓冲区和 worker 线程传输，可自定义每传输级别/格式，`use()` 中间件用于日志修改
- 🤖 **AI/Agent 优先** — 提供 OTel-GenAI 预设、字段优先调用、会话关联、`runInContext()`，用于 LLM 和代理日志
- ⚡ **高性能** — 栈捕获按需（“auto”/“off”），JSON 输出在 Node 上批量写入 stdout，无运行时依赖
- 🗂️ **预设与集成** — 内置 pino、OpenTelemetry 和 GenAI 预设，可无缝对接 Sentry、Better Stack 等平台
- 🔧 **零配置开发体验** — 开箱即用，`type` 省略时自动选择漂亮输出；支持 `tslog/slim` 瘦身版和 `tslog/testing` 测试工具

---

### [GitHub - raineorshine/npm-check-updates: 查找比你的package.json允许的更新的包依赖版本 · GitHub](https://github.com/raineorshine/npm-check-updates)

**原文标题**: [GitHub - raineorshine/npm-check-updates: Find newer versions of package dependencies than what your package.json allows · GitHub](https://github.com/raineorshine/npm-check-updates)

npm-check-updates 是一个用于将 package.json 中的依赖项升级到最新版本的工具，支持多种包管理器，提供灵活的配置和过滤选项。

- 🔧 自动升级 package.json 依赖到最新版本，并保留原有的语义化版本策略（如 ^、~ 等）
- 📦 支持全局安装（`npm install -g npm-check-updates`）或通过 npx 临时使用
- 🚀 基本命令：`ncu` 检查可更新列表，`ncu -u` 直接写入升级后的 package.json
- 🔄 交互模式（`ncu -i`）可手动选择需要升级的依赖包
- 🔍 支持通过 `--filter` 包含、`--reject` 排除特定包，支持通配符、正则和函数
- 🎯 通过 `--target` 指定升级目标（latest、greatest、minor、patch 等），也可自定义函数
- 🛡️ `--cooldown` 选项可设置版本发布时间门槛，防止安装最新但可能不稳定的包（防供应链攻击）
- 🔬 `--doctor` 模式可自动运行测试，识别破坏性升级并回退
- ⚙️ 支持多种配置文件格式（JSON、YAML、JS），可在项目级或用户级配置
- 💻 可作为纯 ESM 或 CommonJS 模块导入使用，便于集成到自定义脚本或 CI 流程
- 🤝 开源项目（Apache-2.0 许可），欢迎贡献和报告问题

---

### [](https://github.com/raineorshine/npm-check-updates/releases/tag/v23.0.0)

**原文标题**: [Release v23.0.0 · raineorshine/npm-check-updates · GitHub](https://github.com/raineorshine/npm-check-updates/releases/tag/v23.0.0)

npm-check-updates v23.0.0 版本发布，包含多项重大变更、迁移指南、性能改进和 bug 修复。

- 🚨 **Node.js 最低版本提升至 22**：不再支持旧版 Node，需升级环境。
- 📦 **改为纯 ESM 包**：删除 CJS 构建，默认导出可直接调用 (`ncu()`)，并提供 CommonJS 迁移方法。
- 🔄 **`filterVersion`/`rejectVersion` 废弃函数参数**：需改用 `filter`/`reject` 选项，以支持字符串或正则筛选。
- 📊 **输出默认分组显示**：按 major/minor/patch 分组，可用 `--format no-group` 恢复旧式平铺输出。
- 🎯 **`--target semver` 尊重显式上界**：范围中的上限不再被突破，如 `^9.5.0 <10` 会保持在 `<10` 内。
- ✨ **其他改进**：原生 TypeScript 加载、延迟加载 `npm-registry-fetch` 提速、减少依赖。
- 🐛 **多项 bug 修复**：修复 scoped 包 404、`--doctor`+`--errorLevel` 崩溃、registry 设置被忽略、YAML 目录保留、packument 流提前中止、`--deep` 模式 CLI 选项被覆盖等问题。

---

### [GitHub - jsdom/jsdom: 多种Web标准的JavaScript实现，用于Node.js · GitHub](https://github.com/jsdom/jsdom)

**原文标题**: [GitHub - jsdom/jsdom: A JavaScript implementation of various web standards, for use with Node.js · GitHub](https://github.com/jsdom/jsdom)

jsdom 是一个纯 JavaScript 实现的 Web 标准库，专为 Node.js 设计，用于模拟浏览器的 DOM 和 HTML 行为，常被用于测试和网页抓取。它提供了丰富的配置选项和 API，允许用户自定义环境、执行脚本、加载资源、管理虚拟控制台和 Cookie，并支持多种便捷的创建方式。

- 📖 概述：jsdom 是 Node.js 环境下纯 JavaScript 实现的 DOM/HTML 标准，适用于测试与爬虫。
- 🛠️ 基本用法：通过 `JSDOM` 构造函数传入 HTML 字符串，获取 `window` 对象操作 DOM。
- ⚙️ 自定义选项：支持设置 `url`、`referrer`、`contentType`、`includeNodeLocations`、`storageQuota` 等。
- ⚡ 脚本执行：默认不执行，通过 `runScripts: "dangerously"` 启用（有安全风险），或 `"outside-only"` 从外部执行。
- 👁️ 假装视觉：设置 `pretendToBeVisual: true` 模拟可视浏览器，改变 `document.hidden` 并启用 `requestAnimationFrame`。
- 📦 加载子资源：默认不加载，使用 `resources: "usable"` 加载框架、样式、脚本及图片；可进一步配置 `userAgent`、`dispatcher`、`interceptors`。
- 🖥️ 虚拟控制台：通过 `VirtualConsole` 自定义日志处理，支持转发到 Node.js 控制台或过滤特定错误。
- 🍪 Cookie jar：可自定义 `CookieJar` 共享或预置 Cookie，基于 `tough-cookie` 并默认启用 `looseMode`。
- ⏳ 干预解析前：`beforeParse` 回调允许在 HTML 解析前修改 `window` 对象，如添加 shim。
- 🔧 JSDOM API：包含 `serialize`、`nodeLocation`、`getInternalVMContext`、`reconfigure` 等方法，支持序列化、获取源码位置、访问 VM 上下文、重新配置 URL 等。
- 🌐 便捷 API：提供 `fromURL`、`fromFile`、`fragment` 工厂方法，分别从 URL、文件或字符串片段创建 jsdom 文档。
- 🎨 其他特性：支持 Canvas（需额外安装 `canvas` 包）、编码嗅探、通过 `window.close()` 关闭及清理定时器、可用 Chrome DevTools 调试。
- ⚠️ 注意事项：异步脚本加载需手动处理；导航与布局功能未实现；需警惕 `runScripts: "dangerously"` 的安全风险。

---

### [GitHub - sindresorhus/crypto-random-string: 生成一个加密安全的随机字符串](https://github.com/sindresorhus/crypto-random-string)

**原文标题**: [GitHub - sindresorhus/crypto-random-string: Generate a cryptographically strong random string · GitHub](https://github.com/sindresorhus/crypto-random-string)

crypto-random-string 是一个用于生成加密强度随机字符串的库，支持多种字符集和自定义选项，适用于标识符、盐值、验证码等场景。

- 🔐 生成加密强度高的随机字符串，用于标识符、密码盐、验证码等
- 📦 支持 Node.js 和浏览器，通过 `npm install crypto-random-string` 安装
- 🧩 提供多种预设字符类型：hex（默认）、base64、url-safe、numeric、distinguishable、ascii-printable、alphanumeric
- ✏️ 可自定义字符集，通过 `characters` 选项指定，支持 emoji 等多字节字符
- 📏 必须指定 `length` 参数（非负整数），注意非 BMP 字符可能占用更多长度
- 🎯 `distinguishable` 类型选用不易混淆的大写字符和数字，适合人工输入
- 🔑 `ascii-printable` 类型包含除空格外的所有可打印 ASCII 字符，适合生成密码
- 🔄 `alphanumeric` 类型包含大小写字母和数字，适合生成 nonce 值
- 🔗 相关工具：random-int、random-float、random-item、unique-random 等
- 🌟 开源项目，MIT 许可，在 GitHub 上有 581 星

---

### [宣布 Ada v4：每秒验证 3560 万 URL - Yagiz Nizipli 的博客](https://www.yagiz.co/release-of-ada-v4)

**原文标题**: [Announcing Ada v4: Validating 35.6M URLs per second - Yagiz Nizipli's blog](https://www.yagiz.co/release-of-ada-v4)

Ada v4.0.0 发布，这是最快的 WHATWG 兼容 URL 解析器，在性能、IDNA 体积和安全性方面取得重大突破。

- 🚀 性能大幅提升：`can_parse` 达到每秒 3560 万 URL，`ada::url` 和 `url_aggregator` 分别提速 19% 和 17%，搜索参数解码提速 44%。
- 📦 IDNA 体积缩减 41%：`ada_idna.cpp` 从 683 KiB 降至 400 KiB，共享库 `.dylib` 缩小 31%，静态库缩小 21%。
- 🔒 安全与正确性增强：拒绝之前的错误输入，防止 `set_hostname` 悄悄截断主机，修复十六进制 IPv4 溢出和组件偏移绕回问题。
- ⚠️ 破坏性变更：共享库 soname 从 3 升至 4，新增可配置最大 URL 长度（默认约 4 GB），C API 文档明确 `ada_string` 的生命周期。
- 🏆 其他改进：改进 URLPattern 的 DoS 防御，新增 Kotlin 绑定，感谢社区贡献。

---

### [发布 v0.25.0 · wasp-lang/wasp · GitHub](https://github.com/wasp-lang/wasp/releases/tag/v0.25.0)

**原文标题**: [Release v0.25.0 · wasp-lang/wasp · GitHub](https://github.com/wasp-lang/wasp/releases/tag/v0.25.0)

wasp v0.25.0 版本发布，包含多个重大变更、新功能、Bug 修复及小改进，升级了核心依赖并引入了新工具与平台支持。

- ⚠️ 重大变更：升级 Vite 至 v8、TypeScript 至 v6、React Router 至 v8；移除未公开的 `wasp/...` 私有路径；移除 Wasp 语言服务器功能
- 🎉 新功能：新增 Linux ARM64 构建支持；路由 `prerender` 选项支持数组传参；新增 Resend 邮件发送提供商；新增 `wasp doctor` 诊断命令
- 🐞 Bug 修复：修复了 `useAuth()` 在修改 User 实体后可能返回过期数据的竞态条件
- 🔧 小改进：`wasp compile` 命令现出现在帮助与补全中；`wasp deps` 不再显示内部包；`tsconfig.wasp.json` 支持额外 glob；改善预渲染性能；Wasp Spec 包现允许抛出 `WaspSpecUserError` 并导出配置类型；Spec 包已发布至 npm；重复实体列出会报明确错误

---

### [](https://github.com/ayuhito/modern-tar)

**原文标题**: [GitHub - ayuhito/modern-tar: 🗄 Zero dependency streaming tar parser and writer for every JavaScript runtime. · GitHub](https://github.com/ayuhito/modern-tar)

modern-tar 是一个零依赖、跨平台、基于 Web Streams API 的流式 tar 归档库，支持所有主流 JavaScript 运行时（浏览器、Node.js、Cloudflare Workers 等），并提供完善的 USTAR/PAX 格式兼容、gzip 压缩/解压和 TypeScript 类型支持。

- 🚀 流式架构：支持大文件归档，无需将全部数据加载到内存  
- 📋 标准兼容：完整支持 USTAR 格式与 PAX 扩展，兼容 GNU/BSD tar  
- 🗜️ 压缩支持：内置 gzip 压缩/解压，利用原生压缩流  
- 📝 TypeScript 优先：全类型安全，附带详细 TypeDoc 文档  
- ⚡ 零依赖：无外部依赖，极小的包体积  
- 🌐 跨平台：浏览器、Node.js、Cloudflare Workers 等均可运行  
- 📁 Node.js 集成：提供高阶文件系统 API，支持目录打包与解包  
- 📦 核心 API：`packTar`/`unpackTar` 用于简单打包/解包，`createTarDecoder`/`createTarPacker` 用于流式处理  
- 🗂️ Node.js 文件系统：支持过滤、映射、剥离目录、权限控制等高级选项  
- 🏗️ 多源打包：可混合文件、目录、内容字符串、流等多种输入源  
- ⚖️ 高性能：小文件归档速度远超同类库，大文件接近 I/O 瓶颈  
- 🌟 兼容性：Node.js 18+，浏览器 Chrome 85+/Edge 85+/Firefox 102+/Safari 14.1+  
- 🔗 开源协议：MIT 许可

---

### [](https://github.com/tinylibs/tinyclip)

**原文标题**: [GitHub - tinylibs/tinyclip: A tiny, cross-platform clipboard utility. · GitHub](https://github.com/tinylibs/tinyclip)

tinyclip 是一个轻量级的跨平台剪贴板库，基于 Node.js 原生剪贴板功能，支持在浏览器中使用原生 Clipboard API。安装简单，使用 Promise 风格的读取和写入方法。

- 📋 核心功能：跨平台剪贴板读取与写入，支持 Node.js 和浏览器环境
- ⚡ 安装命令：`npm install tinyclip`
- 🖥️ 使用示例：`import { readText, writeText } from 'tinyclip'`
- 🔧 API 简介：`readText()` 返回 Promise 字符串，`writeText(text)` 返回 Promise void
- 📜 开源协议：MIT 许可，欢迎贡献
- ⭐ 社区数据：54 个 Star，4 个 Watching，2 个 Fork
- 📦 仓库资源：包含源码、测试、贡献指南、CI 配置等

---

### [发布 v0.6.0 · nubjs/nub · GitHub](https://github.com/nubjs/nub/releases/tag/v0.6.0)

**原文标题**: [Release v0.6.0 · nubjs/nub · GitHub](https://github.com/nubjs/nub/releases/tag/v0.6.0)

nub v0.6.0 发布，带来了多项重要变更和修复，包括脚本执行方式调整、安全增强、新发布通道及交互式工具改进。

- 🐚 所有平台的脚本体现在通过 POSIX shell 执行（Windows 使用内置 busybox，约 700 KB），旧的 cmd 语法不再工作，需重写或配置 `script-shell=cmd`
- 🔒 `minimumReleaseAge` 保护窗口改为“失败关闭”：若范围内所有版本发布未满 24 小时则安装错误，可通过 `minimumReleaseAgeStrict=false` 恢复旧行为
- 🚀 新增 Canary 发布通道：每次向 `main` 分支推送代码都会自动构建并发布 8 平台版本，支持 `nub upgrade --canary/--stable` 切换
- 🎛️ `nub update -i` 交互式更新器改用表格展示，可逐项选择保留或更新，空选不再更新任何内容
- 🗂️ 安装缓存（全局虚拟存储、副作用缓存、新鲜度与增量门）基于项目 Node 引擎键控，切换 Node 版本不再重用旧缓存
- 🐛 修复多个问题：`approve-builds` 现在能列出并批准本地源依赖；修复 repo 控制的 `.npmrc` 中环境变量展开的安全问题；作用域包名在 `nub init` 中得以保留；工作区成员依赖构建脚本锚定到工作区根目录等
- 🛠️ 其他改进：默认信任构建警告精简为单行；`nub init --name @scope/pkg` 不再扁平化作用域；开发预加载从源码根目录解析；内部工具链更新经过 7 天浸泡期等

---

### [GitHub - verdaccio/verdaccio: 一个轻量级的](https://github.com/verdaccio/verdaccio)

**原文标题**: [GitHub - verdaccio/verdaccio: A lightweight Node.js private proxy registry · GitHub](https://github.com/verdaccio/verdaccio)

Verdaccio 是一个轻量级、零配置的本地私有 npm registry，自带数据库并支持缓存代理，适用于私有包管理、多 registry 链接及 E2E 测试等场景。

- 📦 零配置轻量级私有 npm registry，无需数据库即可运行
- 🔄 支持代理并缓存 npmjs.org 等 registry，提升速度与可靠性
- 🔌 通过社区插件扩展存储（如 S3、Google Cloud Storage）
- 🛠 安装方式多样：npm/yarn/pnpm 全局安装、Docker、Helm Chart
- 🧪 E2E 测试覆盖 npm（7-11）、yarn（1-4）、pnpm（9-11）等多版本
- 🔑 完整支持 npm 基础功能：安装、发布、取消发布、标签、用户管理等
- 💡 可覆盖公共包，发布修改版私有包
- 🎥 提供多个技术会议演讲视频（Docker、React 集成等）
- 🤝 由志愿者维护，支持赞助，企业提供免费开源许可（JetBrains、Crowdin 等）
- ⭐ 被大量知名项目采用，如 create-react-app、Grafana、Babel.js 等
- 📄 采用 MIT 许可证，文档和 Logo 采用 CC 许可证

---

