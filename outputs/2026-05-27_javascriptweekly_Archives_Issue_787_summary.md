### [JavaScript 周刊第 787 期：2026 年 5 月 26 日](https://javascriptweekly.com/issues/787)

**原文标题**: [JavaScript Weekly Issue 787: May 26, 2026](https://javascriptweekly.com/issues/787)

以下是您提供的 JavaScript Weekly 第 787 期内容的总结摘要：

JavaScript Weekly 第 787 期涵盖了多项重要更新、工具发布和文章，重点包括 npm 的阶段性发布功能、Expo UI 的稳定版、以及 Deno 2.8 的重大改进。

- 📰 **npm 推出阶段性发布功能**：npm 11.15.0 和 pnpm 11.3 支持“阶段性发布”，允许在包上线前进行审核，并新增`--allow-*`选项控制包来源。
- 📱 **Expo UI 稳定版发布**：通过单一导入，Expo UI 可在 iOS 上使用 SwiftUI、在 Android 上使用 Jetpack Compose，并作为七个常见 React Native 包的本地替代品。
- 🦊 **Firefox 151 支持 Web Serial**：允许 JavaScript 连接微控制器、3D 打印机等串行硬件，同时 Firefox 默认禁用 asm.js 优化。
- 🚀 **Deno 2.8 发布**：Node.js 兼容性从 42% 提升至 76.4%，新增`audit fix`、`pack`、`why`命令，支持 OffscreenCanvas、CPU 分析器、V8 14.9 和 TypeScript 6.0.3。
- 🛠️ **Chrome 预览声明式部分更新**：通过`<template for>`和`setHTML`/`streamHTML` API 实现 HTML 无序更新，实验性支持 Chrome 148。
- ⚡ **Yelp 迁移至 Rspack**：将构建工具从 Webpack 迁移到 Rust 驱动的 Rspack，构建时间减半，并分享了关于 barrel 文件和重导出的经验。
- 🔒 **微软分析“Mini Shai-Hulud”安全事件**：详细回顾了 npm 供应链安全漏洞，并提供了防范建议。
- 🤖 **AI 辅助工程师面临倦怠风险**：文章探讨了 AI 辅助编码的负面影响及避免方法。
- 📄 **DOCX 9.7 发布**：用于在客户端和服务器端生成 Word .docx 文件的成熟库，提供超过 100 个示例脚本。
- 🎮 **JS 填字游戏提示**：提供教育性技巧，如利用`window`全局对象、数字的不同表示方式、标记模板字面量等。

---

### [JS 填字游戏](https://lyra.horse/fun/jscrossword/)

**原文标题**: [JS Crossword](https://lyra.horse/fun/jscrossword/)

概述摘要  
这是一个基于 JavaScript 的填字游戏，每个线索都是对答案执行`eval()`的结果，允许使用特定字符集，最终答案需为英文单词。  
- 🧩 游戏规则：每个填字线索是答案的 JavaScript `eval()`表达式，例如`7`可解为`3+4`。  
- 🔤 允许字符：仅限`A-Za-z0-9!"()*+-./<=>[]`{}`，无空格、逗号或分号。  
- 🎯 最终答案：必须由纯英文字母组成（`A-Za-z`），区分大小写。  
- 🛠️ 工具支持：答案在`eval()`沙箱中运行，提供游乐场测试，允许使用 DevTools、MDN 等资源。  
- 🧠 难度提示：涉及冷门和“诅咒”级 JS 特性，适合熟悉 JavaScript 的玩家。  
- 🖱️ 操作方式：点击方块或按 Ctrl 切换方向，进度自动保存。  
- 🎨 颜色图例：绿色（可能正确）、红色（无效字符）、黄色（错误）、灰色（预填）。  
- 📢 分享渠道：支持 fedi、bsky、twitter，可清除或隐藏字母用于截图。

---

### [Expo UI 现已稳定：从单一导入实现 SwiftUI 和 Jetpack Compose](https://expo.dev/blog/expo-ui-stable-sdk-56?utm_source=jsweekly&utm_medium=email&utm_campaign=sdk-56)

**原文标题**: [Expo UI is now stable: SwiftUI and Jetpack Compose from a single import](https://expo.dev/blog/expo-ui-stable-sdk-56?utm_source=jsweekly&utm_medium=email&utm_campaign=sdk-56)

概述摘要：本文讨论了人工智能在医疗诊断中的应用，强调了其提升准确性和效率的潜力，同时指出了数据隐私和算法偏见等挑战。

- 🔬 人工智能通过分析医学影像和患者数据，能快速识别疾病模式，提高诊断速度。
- 📊 深度学习算法在癌症检测等领域表现出色，准确率有时甚至超过人类专家。
- 🛡️ 数据隐私问题突出，患者信息需严格保护，防止泄露和滥用。
- ⚖️ 算法偏见可能导致诊断不公，需确保训练数据多样性和算法透明性。
- 🤝 人机协作是关键，AI 应辅助医生而非取代，最终决策仍需人类负责。

---

### [npm 包的分阶段发布 | npm 文档](https://docs.npmjs.com/staged-publishing/)

**原文标题**: [Staged publishing for npm packages | npm Docs](https://docs.npmjs.com/staged-publishing/)

npm 的分阶段发布功能允许在包公开发布前增加一个审批步骤，通过暂存、审查和批准三个环节提升安全性。

- 📦 **分阶段发布流程**：通过 `npm stage publish` 将包提交到暂存区，然后由维护者审查并批准后才能正式发布到注册表。
- 🔐 **前置条件**：使用此功能需要 npm CLI 11.15.0+、Node 22.14.0+、对包有发布权限、包已存在且账户已启用双因素认证（2FA）。
- 🖥️ **CLI 审查方式**：可使用 `npm stage list` 列出暂存包，`npm stage view` 查看详情，`npm stage download` 下载 tarball 进行检查。
- 🌐 **npmjs.com 审查方式**：在“Staged Packages”标签页中查看暂存包，并可直接点击“Approve”进行批准。
- ✅ **批准要求**：无论通过 CLI 还是 npmjs.com 批准，都需要进行 2FA 验证才能将包发布到注册表。
- 🔗 **与可信发布集成**：支持与 OIDC 可信发布结合，在 CI/CD 流程中先暂存包，再由维护者用 2FA 审批后上线。

---

### [发布 v11.15.0 · npm/cli · GitHub](https://github.com/npm/cli/releases/tag/v11.15.0)

**原文标题**: [Release v11.15.0 · npm/cli · GitHub](https://github.com/npm/cli/releases/tag/v11.15.0)

npm CLI v11.15.0 版本发布，包含新功能、错误修复和依赖更新。

- 🚀 新增 `npm stage` 命令，支持暂存操作
- 🔐 为信任命令添加权限支持，增强安全性
- ⚙️ 新增 allow-git/allow-file/allow-directory/allow-remote 配置项
- 🐛 修复 `stage download --json` 输出按包名分组的问题
- 🛠️ 修复 min-release-age 与 --before 配置的共存问题
- 🔒 修复 allow-remote=none 不阻止注册表 tarball 的 bug
- 📦 更新多个依赖包：socks、lru-cache、ip-address、brace-expansion、bin-links、tar、semver、hosted-git-info
- 🧹 更新开发依赖，优化工作区包版本
- 👥 贡献者：reggi、owlstronaut、raazkhnl

---

### [pnpm 11.3 | pnpm](https://pnpm.io/blog/releases/11.3)

**原文标题**: [pnpm 11.3 | pnpm](https://pnpm.io/blog/releases/11.3)

pnpm 11.3 版本发布，新增多项功能和优化，包括支持 npm 的 staged publishing、新的 trustLockfile 设置、原生实现的 pnpm pkg/repo/set-script 命令，以及性能改进和错误修复。

- 🎭 **pnpm stage 命令**：支持 npm 的阶段性发布工作流，允许发布隐藏版本，待审核后再批准公开，适用于发布前验证、CI 测试或多包协调发布。
- 🔒 **trustLockfile 设置**：新增配置项，当设为 true 时，安装时跳过对锁文件中条目的 minimumReleaseAge/trustPolicy 验证，适合闭源项目；同时大幅降低验证过程的内存占用，修复了大型工作区（约 4000 条锁文件条目）可能导致的 OOM 问题。
- 🛠️ **原生实现 pnpm pkg/repo/set-script**：三个命令不再依赖 npm，而是原生实现：pnpm pkg 用于操作 package.json 字段，pnpm repo 打开包仓库 URL，pnpm set-script 添加/更新脚本，支持多种清单格式。
- 📦 **--skip-manifest-obfuscation 标志**：为 pack 和 publish 命令新增该标志，打包或发布时保留原始 packageManager 字段和生命周期脚本，不再剥离。
- 🐛 **错误修复**：修复 pnpm dlx 在缺少 package.json 时失败的问题；修复 pnpm dedupe/install 在依赖图包含相互传递的 peer 依赖时的非确定性行为；修复 pnpm add <github-shorthand> 被静默忽略的回归问题；修复 pnpm add --config 导致锁文件环境 yaml 留下孤立条目的问题。

---

### [npm 的分阶段发布与新的安装时控制 - GitHub 更新日志](https://github.blog/changelog/2026-05-22-staged-publishing-and-new-install-time-controls-for-npm/)

**原文标题**: [Staged publishing and new install-time controls for npm - GitHub Changelog](https://github.blog/changelog/2026-05-22-staged-publishing-and-new-install-time-controls-for-npm/)

npm 发布两项供应链安全更新：分阶段发布功能正式上线，并新增安装源控制标志。

- 🚀 **分阶段发布正式可用**：npm 包发布不再直接生效，而是先进入暂存队列，需要维护者通过 2FA 验证后手动批准才能安装，增强发布安全性。
- 🔒 **推荐搭配 OIDC 使用**：建议将分阶段发布与信任发布（OIDC）结合，CI 工作流可配置为仅允许 `npm stage publish`，确保非交互式发布也需人工审核。
- 🛠️ **新增安装源控制标志**：在 `--allow-git` 基础上，新增 `--allow-file`、`--allow-remote`、`--allow-directory` 三个标志，可分别控制本地文件、远程 URL 和目录的安装来源。
- ⚙️ **标志可配置为 all 或 none**：每个标志默认允许所有来源（`all`），可设为 `none` 以严格限制，未来 v12 版本中 `--allow-git` 默认值将改为 `none`。
- 📋 **最低要求 npm 11.15.0**：所有新功能均需 npm CLI 11.15.0 或更高版本，CI 工作流需更新命令为 `npm stage publish`。
- 💬 **社区反馈渠道开放**：鼓励用户通过 GitHub 社区讨论分享使用体验和问题。

---

### [获取失败](https://javascriptweekly.com/link/185668/web)

**原文标题**: [Failed to retrieve](https://javascriptweekly.com/link/185668/web)

无法总结：获取内容失败，状态码 403。

---

### [告别 asm.js | SpiderMonkey JavaScript/WebAssembly引擎](https://spidermonkey.dev/blog/2026/05/20/saying-goodbye-to-asmjs.html)

**原文标题**: [Saying goodbye to asm.js | SpiderMonkey JavaScript/WebAssembly Engine](https://spidermonkey.dev/blog/2026/05/20/saying-goodbye-to-asmjs.html)

概述总结
- 🛑 自 Firefox 148 起，SpiderMonkey 默认禁用 asm.js 优化，并计划未来移除相关代码。
- ✅ asm.js 代码仍可正常运行，但建议重新编译为 WebAssembly 以获得更快速度和更小体积。
- 📜 asm.js 是 Mozilla 对 NaCl/PNaCl 的回应，通过 JavaScript 子集实现接近原生速度，于 2013 年在 Firefox 22 中推出。
- 🎮 asm.js 成功让 Unity、Unreal 等引擎首次通过标准 Web 技术移植 C/C++ 代码（如 Epic Citadel 演示）。
- 🔄 asm.js 为 WebAssembly 铺平了道路，后者在 Firefox 52 中推出，且已取代 asm.js 的主流使用。
- ⏳ 关闭 asm.js 的原因是 WebAssembly 已成功，维护 asm.js 增加成本且带来额外攻击面。
- ⚔️ asm.js 编译器 OdinMonkey 将迎来“诸神黄昏”（Ragnarök），其功能由 WebAssembly 优化编译器 BaldrMonkey 和基线编译器 RabaldrMonkey 继承。
- 🎉 感谢 OdinMonkey 十三年的服务，建议用户迁移至 WebAssembly。

---

### [现代 Web 指南 | Chrome 开发者](https://developer.chrome.com/docs/modern-web-guidance)

**原文标题**: [Modern Web Guidance  |  Chrome for Developers](https://developer.chrome.com/docs/modern-web-guidance)

本指南提供了一套经过专家验证的现代 Web 开发技能，可指导 AI 编码代理构建可访问、高性能且安全的 Web 体验。它支持多种 AI 编码代理，并提供了丰富的示例提示，用于构建新功能、现代化旧代码以及提升应用性能。

- 🚀 **概述**：Modern Web Guidance 是一套常青且经过专家验证的技能，可指导 AI 编码代理构建现代 Web 体验。
- 💻 **安装方式**：支持通过 CLI（`npx modern-web-guidance@latest install`）或与 Vercel、Claude Code、Copilot CLI、Antigravity CLI 等 AI 编码代理集成安装。
- 🏗️ **构建新体验**：提供示例提示，如创建动画手风琴组件、使用 CSS 锚点定位的标签栏，以及利用容器查询的自适应仪表板卡片。
- 🔄 **现代化旧代码**：指导将旧版模态窗口更新为`<dialog>`元素，并将旧版工具提示迁移至 Popover API 和 CSS 锚点定位。
- 🔒 **提升安全性**：支持实现基于 WebAuthn 的通行密钥登录流程，以及设置内容安全策略（CSP）而不会破坏应用。
- ⚡ **改善性能**：提供提示以预加载悬停链接、优化长任务以改善 INP，以及提升 LCP 指标。
- 🎥 **Google I/O 相关**：可观看 Google I/O 上的 Modern Web Guidance 会议，深入了解这些技能如何改进 AI 辅助 Web 开发工作流。
- 🔧 **Chrome DevTools 集成**：可结合 Chrome DevTools for agents，实时运行性能审计、检查无障碍树并捕获控制台日志，自动应用精确的现代 Web 代码修复。
- 🤝 **贡献方式**：欢迎通过 GitHub 提供反馈或贡献，以改进 Modern Web Guidance。

---

### [议程/2026/05.md 主分支 · tc39/议程 · GitHub](https://github.com/tc39/agendas/blob/main/2026/05.md)

**原文标题**: [agendas/2026/05.md at main · tc39/agendas · GitHub](https://github.com/tc39/agendas/blob/main/2026/05.md)

这是 Ecma TC39 第 114 次会议的议程安排，会议将于 2026 年 5 月 19 日至 21 日在荷兰阿姆斯特丹举行，由 JetBrains 主办。

- 📅 **会议时间与地点**：2026 年 5 月 19-21 日，荷兰阿姆斯特丹，每天 10:00-17:00 CEST（最后一天至 16:00）。
- 📋 **议程结构**：包括开场、秘书报告、编辑报告、工作组报告、Web 兼容性 PR、提案讨论（按阶段降序）及长时间讨论。
- 🚀 **提案推进**：多个提案寻求阶段推进，如 Temporal（Stage 4）、Joint Iteration（Stage 3→4）、Decorators（Stage 2.7）、Atomics.pause（Stage 4）等。
- ⏰ **时间限制**：提案推进需在截止日期前提交材料，否则代表可反对；紧急规范变更可酌情放宽。
- 🔒 **日程约束**：部分演讲者有时间限制，如 Guy Bedford 仅下午 3 点后可用，Matthew Gaudet 的 Thenable Curtailment 需在 15:00 后。
- 🗣️ **长时间讨论**：包括 RegExp 提案对线性实现的影响、欧盟 CRA 介绍及问答（60 分钟）。
- 📌 **其他事项**：包括感谢主办方、会议结束等。

---

### [Storybook 10.4](https://storybook.js.org/blog/storybook-10-4/)

**原文标题**: [Storybook 10.4](https://storybook.js.org/blog/storybook-10-4/)

Storybook 10.4 带来了多项重大更新，包括 AI 自动配置、变更检测、快速分享、新框架支持及实验性功能。

- 🤖 **自动化设置**：AI 代理现在可以自动分析项目结构，生成配置、模拟数据和故事，并测试渲染效果，大幅降低组件开发的前期成本。
- 🔍 **变更检测**：新增侧边栏过滤器，可快速筛选出新增、修改或受代码变更影响的故事，帮助开发者聚焦审查 UI 变化。
- 🤝 **快速分享**：一键将 Storybook 发布到云端（由 Chromatic 托管），无需提交代码或等待 CI，即可让团队成员即时查看开发中的 UI。
- 🌴 **TanStack React 框架支持**：与 TanStack 团队合作推出`@storybook/tanstack-react`，提供零配置的类型安全路由、服务器函数等核心功能。
- 📱 **React Native 优化**：新增独立应用入口点，通过`STORYBOOK_ENABLED=true`环境变量实现更干净的隔离设置，并保持向后兼容。
- 🧪 **React 组件元数据（实验性）**：基于 Volar 和 TypeScript 语言服务器的新分析器`react-component-meta`，提供更快、更高质量的组件元数据，未来将替代现有方案。
- ⚡ **升级指南**：新用户可通过`npm create storybook@latest`创建项目，现有用户使用`npx storybook@latest upgrade`自动迁移，并附有详细迁移文档。

---

### [Node.js — Node.js 26.2.0（当前版本）](https://nodejs.org/en/blog/release/v26.2.0)

**原文标题**: [Node.js — Node.js 26.2.0 (Current)](https://nodejs.org/en/blog/release/v26.2.0)

Node.js 26.2.0 版本发布，包含多项新功能、性能优化和错误修复。

- 📌 `stream.compose` 标记为稳定功能
- 🕐 `fs` 模块为 `Stats` 和 `BigIntStats` 新增 `Temporal.Instant` 支持
- 📨 `http` 模块新增 `writeInformation` 方法，可发送任意 1xx 状态码
- 🔒 `crypto` 模块增强安全性：加固 `CryptoKey` 和 `KeyObject` 内部插槽，拒绝无效原始密钥导入
- 🔐 使用 BoringSSL 时，支持 ML-DSA、ML-KEM、ChaCha20-Poly1305 和 AES-KW
- 📦 更新依赖：undici 8.3.0、corepack 0.35.0、sqlite 3.53.1、simdjson 4.6.4、ngtcp2 1.22.1
- 🐛 修复 `stream` 模块中的多个问题，包括广播背压、管道写入重试、同步可迭代对象处理等
- 🛠️ 改进 `quic` 模块，完成内部实现，支持 `--allow-net` 权限
- 🧪 测试运行器新增 `tags` 选项和标签名称过滤器
- 📝 文档更新：移除过时内容，添加大型 PR 贡献指南，修复多处错误

---

### [Node.js — Node.js 24.16.0（长期支持版）](https://nodejs.org/en/blog/release/v24.16.0)

**原文标题**: [Node.js — Node.js 24.16.0 (LTS)](https://nodejs.org/en/blog/release/v24.16.0)

Node.js 24.16.0 'Krypton' LTS 版本发布，包含多项新功能和修复。

- 🔐 **加密模块增强**：新增 `randomUUIDv7()` 函数，支持 Ed25519 上下文参数，并改进密钥类型验证。
- 🐛 **调试器改进**：`node inspect` 新增免编辑运行时表达式探针功能。
- 📁 **文件系统更新**：`fs.stat()` 支持信号选项，`statfs` 暴露 `frsize` 字段，`glob` 新增 `followSymlinks` 选项。
- 🌐 **HTTP 优化**：强化 `ClientRequest` 选项合并，`IncomingMessage` 新增 `req.signal` 属性。
- 🧪 **测试运行器升级**：支持测试顺序随机化、模拟超时 API 对齐，以及 `AbortSignal.timeout` 的模拟定时器支持。
- 🎨 **工具函数扩展**：`util` 模块支持使用十六进制颜色为文本着色。
- 🚀 **QUIC 协议进展**：多项改进，包括多 ALPN 协商、SNI 支持，并移至编译时标志控制。
- 📦 **依赖更新**：升级 npm 至 11.13.0、OpenSSL 至 3.5.6、V8 等核心依赖。
- 🛠️ **其他修复**：修复 URL 解析崩溃、流错误传播、SQLite 扩展等多项问题。

---

### [发布 v12.0.0-pre.0.0 · npm/cli · GitHub](https://github.com/npm/cli/releases/tag/v12.0.0-pre.0.0)

**原文标题**: [Release v12.0.0-pre.0.0 · npm/cli · GitHub](https://github.com/npm/cli/releases/tag/v12.0.0-pre.0.0)

npm v12.0.0-pre.0.0 预发布版本，包含多项破坏性变更、新功能和错误修复。

- ⚠️ **破坏性变更**：`npm view --json` 输出始终为数组；`npm sbom` 报告包名而非目录名；全局安装不再注册 man 手册；`npm pkg` 输出不再强制 JSON；移除 `npm shrinkwrap` 命令及支持；删除 Twitter 和 Freenode 个人资料字段；不再通过 `which node` 解析路径；`npm pack` 和 `npm publish` 的 JSON 输出格式统一；移除 `star`、`stars` 和 `unstar` 命令；移除 `npm adduser` 命令。
- ✨ **新功能**：新增 `npm stage` 命令；为信任命令添加权限支持；新增 `allow-git`、`allow-file`、`allow-directory`、`allow-remote` 配置；移除 `npm-shrinkwrap.json` 支持；删除 Twitter 和 Freenode 字段；移除星标命令；添加 `u` 作为 `update` 命令别名；新增 backport 脚本。
- 🐛 **错误修复**：按包名键控 `stage download --json` 输出；允许 `min-release-age` 与 `--before` 共存；`allow-remote=none` 不阻止注册表 tarball；移除设置；SBOM 去重依赖关系；不展开单元素数组；对齐 CycloneDX 组件名与 SPDX；不安装 man 页面到系统位置；`pkg` 输出类似 `npm view`；忽略预期错误码；停止通过 `which node` 解析路径；同步 `pack` 和 `publish` 的 JSON 输出；移除 `npm adduser` 命令。
- 📚 **文档**：为 `optionalDependencies` 添加示例；更新 `npm view` 的 JSON 输出文档。
- 📦 **依赖更新**：更新 `socks`、`lru-cache`、`ip-address`、`brace-expansion`、`bin-links`、`tar`、`semver`、`hosted-git-info`、`node-gyp`、`is-cidr`、`@sigstore/protobuf-specs`、`tinyglobby`、`picomatch`、`diff`、`minimatch`、`minipass-flush` 等。
- 🔧 **杂项**：更新开发依赖；添加 CLI 分类团队为代码所有者；重构测试；修复代码库中的拼写错误；添加 backport 工作流的操作权限；backport 可触发 CI；不在 CI 中运行 `npm update`；启用预发布模式。

---

### [发布 6.1.0 · apache/echarts · GitHub](https://github.com/apache/echarts/releases/tag/6.1.0)

**原文标题**: [Release 6.1.0 · apache/echarts · GitHub](https://github.com/apache/echarts/releases/tag/6.1.0)

Apache ECharts 6.1.0 版本发布，包含多项新功能、修复和优化。

- 🚀 新增功能：支持轴的数据最小/最大值选项，以及所有轴类型（数值/时间/类别/对数）的无溢出渲染，并提供 `containShape` 和 `clip` 选项。
- 🎨 新功能：对数轴自动排除非正值，轴标签格式化支持索引，折线图新增 `triggerEvent` 事件控制，饼图标签旋转模式增加 `tangential-noflip`。
- 🔧 仪表盘进度颜色支持 `'auto'`，雷达图新增 `clockwise` 选项，K 线图和 dataZoom 增加光标控制选项。
- 📊 散点图和效果散点图在 geo 上支持 `clip`，visualMap 新增 `seriesTargets` 多系列维度映射，矩阵支持便捷创建和事件触发。
- 🌐 新增拉脱维亚语翻译，修复时间轴、类别轴、数值轴等多个轴相关问题，包括重复刻度、精度和边界处理。
- 🐛 修复条形图标签位置、散点图渐进渲染冻结、折线图效果翻转、K 线图水平布局错误、平行坐标轴范围、饼图在网格中的中心对齐、树图缩放限制等问题。
- 🔒 修复折线图 tooltip 的 XSS 漏洞，以及地图/地理坐标系的同步和视觉伪影。
- 🛠️ 修复 tooltip 内容刷新、`valueFormatter` 参数、axisPointer 阴影和裁剪、hoverLayer 视觉伪影、标记渲染、dataZoom 位置和拖动行为。
- 📝 修复面积图、旭日图、矩阵标签、工具箱强调颜色和暗模式、渐进渲染、标签线平滑、SVG 编码兼容性、Vue 实例标记、和弦图导出、德语翻译和 TypeScript 类型兼容性。
- ⚠️ 破坏性变更：`tooltip.valueFormatter` 的 `dataIndex` 参数改为原始数据索引，`axis.startValue` 不再隐式作为 `axis.min`，条形图等系列默认消除溢出（可通过 `axis.containShape: false` 恢复旧行为）。

---

### [示例 - Apache ECharts](https://echarts.apache.org/examples/en/index.html)

**原文标题**: [Examples - Apache ECharts](https://echarts.apache.org/examples/en/index.html)

无法总结：未找到主要内容。

---

### [声明式部分更新 | 博客 | Chrome 开发者](https://developer.chrome.com/blog/declarative-partial-updates)

**原文标题**: [Declarative partial updates  |  Blog  |  Chrome for Developers](https://developer.chrome.com/blog/declarative-partial-updates)

Chrome 团队发布了“声明式局部更新”API，包含两组新功能，旨在解决 HTML 按顺序传输的局限性，提升 Web 应用性能和开发体验。该功能从 Chrome 148 开始支持，并提供了 Polyfill。

- 🧩 **无序流式更新**：通过 `<template for>` 和 `<?marker>` 处理指令，允许 HTML 内容在文档中任意位置定义，并在解析后替换到指定占位符，实现组件化、按需加载和性能优化。
- ⏳ **流式占位与渐进增强**：支持 `<?start>` 和 `<?end>` 范围标记，可在模板加载前显示临时内容（如“加载中…”），提升用户体验。
- 🏝️ **岛屿架构支持**：允许静态内容与动态组件独立流式注入，无需复杂 JavaScript 框架，简化了 Astro 等框架的岛屿模式实现。
- 📦 **按需内容交付**：内容可在准备就绪后流式插入，无需等待所有数据（如数据库查询）完成，避免阻塞首屏渲染。
- 🚀 **优化加载顺序**：可将非关键内容（如大型菜单）延迟到文档末尾传输，优先加载首屏所需 HTML，突破传统顺序限制。
- 🛡️ **安全与限制**：`<template for>` 仅能更新同一父元素内的占位符；动态插入（如 `setHTML`）时无法修改现有 DOM，但流式方法（如 `streamHTMLUnsafe`）可以。
- 🔮 **未来扩展**：考虑添加客户端包含（如 `<template for="footer" patchsrc="...">`）、批量更新、版本控制防覆盖、安全补丁等功能。
- 🧪 **Polyfill 可用**：`template-for-polyfill`（npm）支持立即使用，但无法直接更新浏览器解析器，存在部分限制。
- 🆕 **新增 HTML 插入与流式 API**：引入 `setHTML`、`streamHTML`、`replaceWithHTML`、`appendHTML` 等系列方法，统一命名规范，支持静态和流式操作，并集成 Sanitizer API 和 Trusted Types。
- ⚡ **流式性能优势**：`streamHTMLUnsafe` 等方法允许从 fetch 响应或写入器流式注入 HTML，无需等待完整内容，适用于单页应用动态加载大型内容。
- ⚠️ **不安全方法**：`setHTMLUnsafe` 等“Unsafe”版本默认关闭消毒器，可启用 `runScripts` 执行脚本，需开发者自行评估输入信任度。
- 🔗 **组合使用**：将 `<template for>` 与流式 API 结合，可实现动态更新不同内容区域，无需单独 DOM 引用，简化 SPA 页面加载。
- 📚 **Polyfill 支持**：`html-setters-polyfill`（npm）提供 API 形状模拟，但流式功能需缓冲后一次性应用；安全设置依赖 `setHTML` 和 Sanitizer API（Safari 不支持）。

---

### [GitHub - GoogleChromeLabs/html-setters-polyfill · GitHub](https://github.com/GoogleChromeLabs/html-setters-polyfill)

**原文标题**: [GitHub - GoogleChromeLabs/html-setters-polyfill · GitHub](https://github.com/GoogleChromeLabs/html-setters-polyfill)

HTML Setters Polyfill 是一个由 Google Chrome 实验室开发的 polyfill，用于实现新的 HTML 设置器方法，支持安全与不安全的 HTML 插入、流式处理，并兼容 TypeScript。

- 📦 支持多种 HTML 插入方法：如 `setHTML`、`appendHTML`、`beforeHTML` 等，适用于 Element 和 ShadowRoot。
- 🚫 提供不安全变体：如 `setHTMLUnsafe`、`appendHTMLUnsafe`，可执行脚本（通过 `runScripts: true`）。
- 🌊 支持流式 HTML：如 `streamHTML` 返回 `WritableStream`，可缓冲并在关闭时应用 HTML。
- 🔒 依赖无额外库：无依赖项，但流式处理不支持 Trusted Types。
- ⚠️ 存在限制：流式处理非原生流式（先缓冲），安全流式需要浏览器支持 `setHTML`，DSD 依赖 `createContextualFragment`。
- 📜 许可与贡献：采用 Apache 2.0 许可，欢迎贡献，但非 Google 官方产品。

---

### [GitHub - GoogleChromeLabs/polyfill模板 · GitHub](https://github.com/GoogleChromeLabs/template-for-polyfill)

**原文标题**: [GitHub - GoogleChromeLabs/template-for-polyfill · GitHub](https://github.com/GoogleChromeLabs/template-for-polyfill)

这是一个用于实现声明式部分更新 API 的 polyfill 模板项目。

- 📦 提供对 `<template for>` 指令的 polyfill 支持，实现声明式修补功能
- 🌐 需要支持 ES6/ES2015 的浏览器环境，通过 npm 或 unpkg 均可引入使用
- ⚠️ 无法对 `innerHTML` 等 API 进行猴子补丁，但会通过 MutationObserver 处理后续 DOM 操作中的模板指令
- 🚀 新添加的 `<template for>` 指令通过 MutationObserver 异步处理，不会在 HTML 解析时立即生效，可能导致 `<?start>`/`<?end>` 占位内容短暂显示
- 📚 提供完整的使用说明：npm 安装、unpkg 引入、从源码构建（`npm i && npm test && npm run build`）
- 📄 项目采用 Apache 2.0 许可证，欢迎贡献，但非 Google 官方支持产品，不参与漏洞奖励计划
- 🛠️ 技术栈包括 HTML、JavaScript、TypeScript 和 Shell，包含测试、构建和代码质量配置

---

### [通过从 Webpack 迁移到 Rspack 优化构建时间](https://engineeringblog.yelp.com/2026/05/optimizing-our-build-times-by-migrating-from-webpack-to-rspack.html)

**原文标题**: [Optimizing Our Build Times by Migrating from Webpack to Rspack](https://engineeringblog.yelp.com/2026/05/optimizing-our-build-times-by-migrating-from-webpack-to-rspack.html)

### 概述总结
Yelp 团队通过将构建工具从 Webpack 迁移到 Rspack，实现了约 50% 的构建时间缩减，并分享了迁移策略、优化技巧及未来改进方向。

- 🚀 **迁移动机**：Webpack 在大型单体仓库中成为性能瓶颈，而 Rspack 因高度兼容 Webpack 配置，降低了迁移风险和成本。
- 🔧 **分阶段迁移**：采用“适配器模式”保留原有 Webpack 配置，逐步让开发者选择 Rspack，并通过部署预览验证页面，最终实现单 PR 完成迁移。
- ⚡ **核心优化**：迁移本身带来约 25% 的构建加速；修复“桶文件”（barrel files）中的星号导出和间接重导出模式，额外节省约 30 秒；启用 Rspack 持久缓存后，二次构建时间减少高达 80%。
- 📚 **Storybook 集成**：通过 Rsbuild 框架集成 Storybook，但需清除其默认插件以避免冲突，确保构建输出稳定。
- 🔮 **未来计划**：计划用 Rust 编写的 SWC 编译器替代 Babel，并利用 Rspack 内置的 swc-loader 进一步提升性能。

---

### [Rspack](https://rspack.rs/)

**原文标题**: [Rspack](https://rspack.rs/)

Rspack 是一个基于 Rust 的高性能 Web 打包工具，旨在无缝替代 webpack，提供更快的构建速度和开发者体验。

- 🚀 **极速性能**：使用 Rust 和并行化架构，开发启动仅 1.36 秒，构建 3.35 秒，HMR 仅 160 毫秒，远超 Vite 和 webpack。
- 🔄 **Webpack 兼容**：完全兼容 webpack 插件和加载器，可无缝迁移。
- ⚡ **闪电 HMR**：内置增量构建，实现超快热模块替换。
- 🧩 **框架无关**：支持任何前端 UI 框架，灵活通用。
- ✂️ **代码分割**：将代码拆分为小包，实现按需加载，提升性能。
- 🌳 **Tree Shaking**：自动检测并消除未使用代码，减小输出体积。
- 🔌 **丰富插件**：提供强大插件钩子，兼容大多数 webpack 插件。
- 🌐 **模块联邦**：在 Web 应用间共享代码，促进协作。
- 🖼️ **资源管理**：处理并优化图片、字体和样式表等静态资源。
- 🔥 **HMR**：运行时热更新模块，无需完全刷新。
- 🖥️ **开发服务器**：提供成熟高性能的开发服务器。
- 🏗️ **并行构建**：支持多目标或环境并行构建。
- ⚙️ **SWC 集成**：使用基于 Rust 的 SWC 加速 JavaScript/TypeScript 转译。
- 💡 **Lightning CSS**：集成 Lightning CSS 实现快速 CSS 处理和优化。
- 📡 **JavaScript API**：提供编程式构建 API，自定义构建流程。
- 🛠️ **Rstack 工具链**：包含 Rspack、Rsbuild、Rslib、Rspress、Rsdoctor 等统一工具链，覆盖构建、开发、库、文档和分析。
- 🏢 **受信赖**：被 bit.dev 等创新者采用，开源且基于 MIT 许可。

---

### [Ghost —— 面向智能体的数据库](https://ghost.build/?utm_source=content-syndication&utm_medium=referral&utm_campaign=javascript-weekly-newsletter)

**原文标题**: [Ghost â the database for agents](https://ghost.build/?utm_source=content-syndication&utm_medium=referral&utm_campaign=javascript-weekly-newsletter)

概述摘要  
- 🧳 正在打开行李，准备整理物品。  
- 📦 可能涉及旅行或搬家后的物品分类与收纳。  
- 🔍 强调“拆包”过程，暗示后续需要整理或检查内容。

---

### [小沙虫：受损的@antv npm 包导致 CI/CD 凭证窃取 | 微软安全博客](https://www.microsoft.com/en-us/security/blog/2026/05/20/mini-shai-hulud-compromised-antv-npm-packages-enable-ci-cd-credential-theft/)

**原文标题**: [Mini Shai Hulud: Compromised @antv npm packages enable CI/CD credential theft | Microsoft Security Blog](https://www.microsoft.com/en-us/security/blog/2026/05/20/mini-shai-hulud-compromised-antv-npm-packages-enable-ci-cd-credential-theft/)

Microsoft 发现了一起针对 @antv npm 包生态系统的活跃供应链攻击，攻击者通过窃取维护者账户，发布恶意版本的数据可视化包，导致下游依赖链广泛受影响，包括每周下载量超百万的 echarts-for-react。恶意载荷在 npm install 时自动执行，专门窃取 GitHub Actions 环境中的凭证，具备多平台凭证窃取、进程内存抓取、权限提升、双通道数据外泄及 SLSA 来源伪造等能力。GitHub 已移除 640 个恶意包并作废 6 万多个 npm 令牌，微软建议用户立即审查依赖树、轮换凭证并启用防护措施。

- 🎯 攻击概述：攻击者通过窃取 @antv 维护者账户，发布恶意 npm 包版本，通过依赖链（如 echarts-for-react）传播，影响 CI/CD 管道和云工作负载。
- 🔍 恶意载荷：约 499KB 的混淆 JavaScript 文件，在 npm install 时通过 preinstall 钩子自动执行，使用 Bun 运行时运行，具备多层混淆和环境检测。
- 🛡️ 凭证窃取：目标包括 GitHub、AWS、HashiCorp Vault、npm、Kubernetes 和 1Password，通过环境变量、文件扫描和 API 调用窃取令牌和密钥。
- 💾 内存抓取：通过 /proc 扫描定位 GitHub Actions Runner.Worker 进程，直接从进程内存中提取运行时秘密，绕过正常屏蔽机制。
- ⚡ 权限提升：通过 bind mount 注入 sudoers 规则实现无密码 sudo，并修改 /etc/hosts 进行 DNS 重定向。
- 📤 数据外泄：主要使用 HTTPS 加密 C2 通信，备用通道通过 Git Data API 在受害者仓库中创建 blob/tree/commit，第三通道在受害者账户下创建公开仓库。
- ⚠️ 影响范围：直接感染 @antv 包，通过下游依赖放大到数千个项目，窃取的令牌可导致进一步包投毒、仓库操控和云访问，SLSA 来源伪造破坏供应链信任。
- 🛠️ GitHub 响应：移除 640 个恶意包，作废 61,274 个具有写权限和 2FA 绕过的 npm 令牌，发布安全公告并通过 Dependabot 和 npm audit 提醒社区。
- ✅ 缓解措施：审查依赖树，固定已知安全版本，使用 --ignore-scripts 安装，轮换所有可能暴露的凭证，审计 GitHub 账户和 CI/CD 日志，启用 Microsoft Defender 防护。

---

### [迷你沙虫再度出击：317 个 npm 包被篡改——实时开源软件供应链安全](https://safedep.io/mini-shai-hulud-strikes-again-314-npm-packages-compromised/)

**原文标题**: [Mini Shai-Hulud Strikes Again: 317 npm Packages Compromised - Real-time Open Source Software Supply Chain Security](https://safedep.io/mini-shai-hulud-strikes-again-314-npm-packages-compromised/)

2026 年 5 月 19 日，npm 账户`atool`遭入侵，攻击者在 22 分钟内发布了 317 个包的 637 个恶意版本，植入“Mini Shai-Hulud”恶意软件，用于窃取凭证、持久化控制并横向传播。

- 🚨 **大规模供应链攻击**：`atool`账户被入侵，22 分钟内发布 637 个恶意版本，影响 317 个 npm 包，包括`size-sensor`（420 万月下载）、`echarts-for-react`（380 万）、`@antv/scale`（220 万）等高流量包。
- 🕵️ **恶意载荷功能全面**：498KB 的混淆 Bun 脚本，可窃取 AWS、GCP、Azure、Kubernetes、HashiCorp Vault、GitHub PAT、npm 令牌、SSH 密钥及 1Password/Bitwarden 等密码管理器凭证。
- 📤 **双重数据外泄通道**：窃取数据通过 Git 对象提交至公共 GitHub 仓库（伪装为`python-requests/2.31.0`），以及 RSA+AES 加密的 HTTPS POST 至`t.m-kosche[.]com`（伪装为 OpenTelemetry 追踪数据）。
- 🛡️ **持久化与横向移动**：注入 CI/CD 工作流（`codeql.yml`）窃取 GitHub Secrets；劫持 Claude Code、Codex 和 VS Code，通过`SessionStart`钩子和`folderOpen`任务自动执行；安装系统服务`kitty-monitor`作为 GitHub 死信 C2 后门。
- 🔗 **冗余执行路径**：除`preinstall`钩子外，630 个版本还通过`optionalDependencies`引用`antvis/G2`仓库中的伪造孤立提交，即使`preinstall`被阻止也能执行。
- 🖥️ **容器逃逸与本地感染**：尝试通过 Docker 套接字进行特权容器逃逸，并将恶意文件复制到本地其他 Node.js 项目中。
- ⚠️ **影响与应对**：使用语义化版本范围的项目自动解析至恶意版本；建议立即检查 lockfile、轮换所有凭证、封锁 C2 域名、删除持久化服务及钩子文件，并使用`pmg`等工具进行实时防护。

---

### [AI 辅助的工程师正在精疲力竭，这真的没问题吗？——火星编年史，邪恶火星人团队博客](https://evilmartians.com/chronicles/ai-assisted-engineers-are-burning-out-is-this-fine)

**原文标题**: [AI-assisted engineers are burning out, is this fine?—Martian Chronicles, Evil Martians’ team blog](https://evilmartians.com/chronicles/ai-assisted-engineers-are-burning-out-is-this-fine)

AI 辅助工程师正在经历新型职业倦怠，这种倦怠源于认知过载、工作强度激增和成就感缺失的恶性循环。文章分析了 AI 工具如何改变工作本质，并提出可持续使用 AI 的实践建议。

- 🔥 **新型倦怠现象**：AI 辅助编程导致高强度认知负荷，开发者每天仅能维持 4-5 小时高效工作，之后大脑完全疲劳
- ⚡ **效率陷阱**：AI 看似提升 2 倍速度，但实际将工作强度提升至传统编程的 2 倍，且剥夺了自然休息时间
- 🧠 **认知债务**：开发者失去对代码库的直觉理解，从创作者退化为监督者，监督自己不懂的系统极其消耗精力
- 💔 **成就感流失**：AI 生成代码取代了编程中"规划→创作→成果"的愉悦过程，导致工作满足感大幅降低
- 🎭 **隐性职业转型**：工程师角色悄然转变为 AI 协调员，但职位名称未变，造成身份认知冲突
- 📉 **虚假期望陷阱**：AI 带来的初始高效会形成不切实际的基准线，当效率回落时产生巨大压力
- 🔄 **审查瓶颈**：AI 生成代码量远超人工审查能力，高级工程师被迫承担不成比例的风险和认知负荷
- 🛠️ **可持续方案**：记录每日成就、规划 AI 使用时段、保留纯手工编码时间、严格执行工作边界、探索新技能领域

---

### [一种简单的列表聚类算法](https://cassidoo.co/post/clustering-tiles/)

**原文标题**: [A simple clustering algorithm for lists](https://cassidoo.co/post/clustering-tiles/)

本文介绍了一种基于子列表反转的直观聚类算法，灵感来源于作者与孩子玩磁力片的经验。该算法通过反复反转列表中相同元素之间的子列表，逐步将相同元素聚集在一起，最终实现完全聚类。虽然时间复杂度为 O(n²)，效率不高，但算法设计巧妙，易于人类理解和操作。

- 🧩 **算法灵感**：源于与孩子玩 Magna-Tiles 时手动排序和分组磁力片的模式，将物理操作转化为算法。
- 🔄 **核心步骤**：从列表末尾开始，找到与末尾值相同的最近元素，反转两者之间的子列表，重复此过程直到所有相同元素聚集。
- 📉 **时间复杂度**：O(n²)，使用嵌套 while 循环实现，作者尝试递归未果后选择了迭代方法。
- 🧠 **人类优势**：人类能直观地 O(1) 识别并翻转物理对象，而计算机处理此问题更复杂，体现了人类直觉与计算机逻辑的差异。
- 🛠️ **代码实现**：提供了 JavaScript 函数`cassidyCluster`，支持字符串和数组输入，通过辅助函数`reverse`反转子列表，并处理不同聚类状态。
- 🎯 **算法特性**：贪心策略，每次只优化当前步骤，与煎饼排序（pancake sort）有相似概念，但更侧重于分组而非排序。
- 🤗 **趣味性**：作者强调该算法虽低效但有趣，是亲子互动中的数学探索，鼓励实践与创造。

---

### [Deno 2.8](https://deno.com/blog/v2.8#new-subcommands)

**原文标题**: [Deno 2.8 | Deno](https://deno.com/blog/v2.8#new-subcommands)

Deno 2.8 版本发布，这是迄今为止最大的次要版本，带来了众多新功能、性能提升和兼容性改进。

- 🚀 **新增子命令**：新增 `deno audit fix`（自动修复漏洞）、`deno bump-version`（版本号管理）、`deno ci`（CI 环境专用安装）、`deno pack`（打包为 npm tarball）、`deno transpile`（TypeScript 转译）、`deno why`（依赖溯源）等实用命令。
- 📦 **默认 npm 支持**：`deno add` 和 `deno install` 现在默认将无前缀包名视为 npm 包，无需再手动添加 `npm:` 前缀，与 Node 生态习惯对齐。
- ⚡ **性能大幅提升**：冷缓存 npm 安装速度提升 3.66 倍；`node:http` 吞吐量提升 2.21 倍；`node:buffer` base64 处理速度提升 3.07 倍；`node:crypto` scrypt 速度提升 2.12 倍。
- 🔧 **Node.js 兼容性飞跃**：Node 官方测试套件通过率从 42% 提升至 76.4%（3,405/4,457 项测试），远超 Bun 的 40.6%。
- 🧩 **新功能与 API**：支持 `import defer` 提案（延迟模块求值）、TypeScript 6.0.3、`OffscreenCanvas`、几何接口（`DOMPoint`、`DOMRect` 等）、`catalog:` 协议（工作空间依赖版本统一管理）。
- 🐛 **调试与诊断**：Chrome DevTools 可检查 Deno 网络流量；内置 CPU 分析器，支持生成火焰图 SVG 和 Markdown 报告。
- 🧪 **测试与覆盖率**：测试清理器默认关闭；支持单测试超时；`deno coverage` 新增函数覆盖率报告。
- 📦 **包管理增强**：支持跨平台 npm 安装（`--os`/`--arch`）、`--prod` 跳过开发依赖、hoisted `node_modules` 布局、`.npmrc` 更多配置项、`file:`/`link:` 依赖静默忽略。
- 🔄 **其他改进**：`deno task` 输出带任务名前缀；`deno upgrade` 支持增量更新（下载量减少 87-93%）和从 PR 安装；`setTimeout`/`setInterval` 返回 Node 的 `Timeout` 对象；`lib.node` 默认包含 Node 类型定义。

---

### [Deno 2.8](https://deno.com/blog/v2.8#performance)

**原文标题**: [Deno 2.8 | Deno](https://deno.com/blog/v2.8#performance)

Deno 2.8 是迄今为止最大的次要版本，带来了大量新功能、性能提升和 Node.js 兼容性改进。

- 🚀 **新增子命令**：包括 `deno audit fix`（自动修复漏洞）、`deno bump-version`（自动更新版本号）、`deno ci`（可重现的 CI 安装）、`deno pack`（构建 npm 包）、`deno transpile`（仅转译 TypeScript）、`deno why`（解释依赖来源）。
- ⚡ **性能大幅提升**：冷 npm 安装速度提升 3.66 倍；`node:http` 吞吐量提升 2.21 倍；`node:buffer` base64 操作快 3.07 倍；`node:crypto` scrypt 快 2.12 倍。
- 🧪 **Node.js 兼容性飞跃**：Node 官方测试套件通过率从 42% 跃升至 76.4%（远超 Bun 的 40.6%）；许多 `node:*` 模块实现懒加载，启动更快。
- 🔧 **包管理增强**：`deno add` 和 `deno install` 默认使用 npm 前缀；支持 `catalog:` 协议管理 monorepo 依赖；新增 `--prod`、`--os`、`--arch` 等标志；支持 hoisted `node_modules` 布局和 `.npmrc` 配置。
- 🛠️ **调试与性能分析**：Chrome DevTools 可检查网络请求；内置 CPU 分析器支持火焰图 SVG 和 Markdown 报告输出。
- 🌐 **Web API 完善**：新增 `OffscreenCanvas` 和几何接口（`DOMPoint`、`DOMRect` 等）；支持更多可转移和可序列化对象；`fetch` 和 WebSocket 修复。
- 📦 **TypeScript 6.0.3**：默认包含 `lib.node` 类型，无需额外配置即可使用 Node 全局类型。
- 🧪 **测试改进**：sanitizer 默认关闭；支持单测试超时；覆盖率报告新增函数覆盖率。
- 🎯 **`import defer` 支持**：延迟模块评估，优化启动时间。
- 🔄 **`deno upgrade` 改进**：支持增量更新（下载量减少 87-93%）；可从 PR 直接安装构建产物。
- 🔗 **模块加载钩子**：实现 `module.registerHooks()`，支持自定义模块加载逻辑。
- ⏱️ **`setTimeout`/`setInterval` 返回 `Timeout` 对象**：匹配 Node.js 行为，提升性能并减少技术债务。
- 🐛 **大量 Bug 修复**：涵盖包管理、`deno compile`、OpenTelemetry、任务运行器等多个领域。

---

### [Deno 2.8](https://deno.com/blog/v2.8#web-apis)

**原文标题**: [Deno 2.8 | Deno](https://deno.com/blog/v2.8#web-apis)

Deno 2.8 发布，这是迄今为止最大的次要版本，带来了众多新功能、性能提升和兼容性改进。

- 🚀 **新增子命令**：`deno audit fix` 自动修复漏洞，`deno bump-version` 管理版本号，`deno ci` 用于 CI 环境，`deno pack` 打包为 npm tarball，`deno transpile` 去除类型，`deno why` 解释依赖来源。
- 📦 **npm 默认支持**：`deno add` 和 `deno install` 默认将无前缀名称视为 npm 包，`deno install` 冷缓存安装速度提升 3.66 倍。
- ⚡ **性能飞跃**：`node:http` 吞吐量提升 2.21 倍，`node:buffer` base64 处理快 3.07 倍，`node:crypto` scrypt 快 2.12 倍，`node:fs` cpSync 快 1.49 倍。
- 🧪 **Node.js 兼容性**：Node 官方测试套件通过率从 42% 跃升至 76.4%，远超 Bun 的 40.6%。
- 🔧 **调试增强**：Chrome DevTools 可检查 Deno 网络流量，新增内置 CPU 分析器（支持火焰图和 Markdown 报告）。
- 📐 **TypeScript 6.0.3**：内置 TypeScript 编译器更新，`lib.node` 默认包含，无需额外配置。
- 🧩 **import defer**：支持 TC39 提案，延迟模块评估以优化启动时间。
- 🗂️ **包管理改进**：支持 `catalog:` 协议、跨平台 npm 安装、`--prod` 标志、`--os`/`--arch` 选项、`.npmrc` 增强。
- 🛠️ **测试与覆盖率**：测试清理器默认关闭，新增每测试超时和函数覆盖率报告。
- 🌐 **Web API 扩展**：新增 `OffscreenCanvas` 和几何接口，支持更多可转移和可序列化类型。
- 📝 **其他亮点**：`deno task` 输出带任务名前缀，`deno upgrade` 支持增量更新和从 PR 安装，模块加载器钩子，`setTimeout`/`setInterval` 返回 Node 的 `Timeout` 对象。

---

### [Deno 2.8](https://deno.com/blog/v2.8#module-loader-hooks)

**原文标题**: [Deno 2.8 | Deno](https://deno.com/blog/v2.8#module-loader-hooks)

Deno 2.8 是迄今為止最大的次要版本更新，帶來了大量新功能、效能提升和相容性改進。

- 🚀 **全新子命令**: 新增 `deno audit fix` (自動修復漏洞)、`deno bump-version` (自動更新版本號)、`deno ci` (鎖定檔案安裝)、`deno pack` (打包成 npm tarball)、`deno transpile` (純 TypeScript 轉譯) 和 `deno why` (解釋依賴原因)。
- 📦 **npm 預設化**: `deno add` 和 `deno install` 現在預設將無前綴的套件名稱視為 npm 套件，並支援 `--prod`、`--os`/`--arch` 和 `catalog:` 協定。
- ⚡ **效能飛躍**: 冷 npm 安裝速度提升 **3.66 倍**，`node:http` 吞吐量提升 **2.21 倍**，`node:buffer` base64 編碼速度提升 **3.07 倍**。
- 🧩 **Node.js 相容性**: Node.js 官方測試套件通過率從 42% 大幅提升至 **76.4%**，遠超 Bun 的 40.6%。
- 🐞 **除錯與分析**: Chrome DevTools 現在可檢查 Deno 的網路流量，並內建 CPU 分析器，支援生成火焰圖和 Markdown 報告。
- 📝 **TypeScript 6.0.3**: 內建 TypeScript 編譯器更新至 6.0.3，並預設包含 `lib.node` 類型定義。
- 🔄 **import defer**: 支援 TC39 提案，允許模組延遲評估，優化啟動時間。
- 🧪 **測試與覆蓋率**: 測試清理器預設關閉，新增每測試逾時設定，`deno coverage` 支援函數覆蓋率報告。
- 🌐 **Web API 增強**: 新增 `OffscreenCanvas` 和 DOM 幾何圖形介面，並改進了 `structuredClone` 和 `postMessage` 的傳輸與序列化支援。
- 📦 **其他改進**: 支援 `.npmrc` 的 `min-release-age`、`file:`/`link:` 依賴跳過、`deno upgrade` 支援增量更新和從 PR 安裝、`module.registerHooks()` API 等。

---

### [Deno 2.8](https://deno.com/blog/v2.8#debugging)

**原文标题**: [Deno 2.8 | Deno](https://deno.com/blog/v2.8#debugging)

Deno 2.8 版本发布，这是迄今为止最大的次要版本，带来了众多新功能、性能提升和兼容性改进。

- 🚀 **新增子命令**：新增 `deno audit fix`（自动修复漏洞）、`deno bump-version`（自动更新版本号）、`deno ci`（CI 环境专用安装）、`deno pack`（构建 npm 可发布 tarball）、`deno transpile`（仅转译 TypeScript 为 JavaScript）和 `deno why`（解释依赖来源）。
- 📦 **默认 npm 支持**：`deno add` 和 `deno install` 现在默认将无前缀名称视为 npm 包，无需再手动添加 `npm:` 前缀。
- ⚡ **性能大幅提升**：冷 npm 安装速度提升 3.66 倍，`node:http` 吞吐量提升 2.21 倍，`node:buffer` base64 处理速度提升 3.07 倍，以及多项其他优化。
- 🧩 **Node.js 兼容性飞跃**：Node.js 官方测试套件通过率从 42% 跃升至 76.4%，远超 Bun 的 40.6%。
- 🛠️ **调试与性能分析**：Chrome DevTools 可检查网络流量；内置 CPU 分析器支持生成 `.cpuprofile`、交互式 SVG 火焰图和 Markdown 报告。
- 📝 **`import defer` 支持**：实现 TC39 提案，允许延迟加载和评估模块，优化启动时间。
- 🏗️ **包与工作区管理**：新增 `catalog:` 协议统一管理 monorepo 依赖版本；支持跨平台 npm 安装（`--os`/`--arch`）；支持 `--prod` 跳过开发依赖；支持 `hoisted` 模式的 `node_modules`；完善 `.npmrc` 支持。
- 🧪 **测试与覆盖率**：测试清理器默认关闭；支持每测试超时；覆盖率报告新增函数覆盖率。
- 🌐 **Web API 完善**：新增 `OffscreenCanvas` 和几何接口（`DOMPoint`、`DOMRect` 等）；改进结构化克隆和可转移对象支持；支持更多 Web Crypto 算法。
- 🔧 **其他改进**：`deno task` 输出带任务名前缀；`deno upgrade` 支持增量更新和从 PR 安装；实现 `module.registerHooks()` 加载器钩子；`setTimeout`/`setInterval` 返回 Node.js 的 `Timeout` 对象。

---

### [Deno 2.8](https://deno.com/blog/v2.8#cpu-profiling)

**原文标题**: [Deno 2.8 | Deno](https://deno.com/blog/v2.8#cpu-profiling)

Deno 2.8 是迄今为止最大的次要版本，带来了大量新功能、性能提升和兼容性改进。

- 🚀 **新子命令**：新增 `deno audit fix`（自动修复漏洞）、`deno bump-version`（版本号管理）、`deno ci`（CI 专用安装）、`deno pack`（打包为 npm tarball）、`deno transpile`（仅类型擦除）、`deno why`（依赖溯源）。
- 🏎️ **性能大幅提升**：冷 npm 安装快 3.66 倍，`node:http` 吞吐量提升 2.21 倍，`node:buffer` base64 快 3.07 倍，`node:crypto` scrypt 快 2.12 倍。
- 🧪 **Node.js 兼容性飞跃**：Node 官方测试套件通过率从 42% 跃升至 76.4%（远超 Bun 的 40.6%），并默认包含 `lib.node` 类型。
- 🛠️ **包管理增强**：`deno add`/`deno install` 默认使用 `npm:` 前缀，支持 `catalog:` 协议、跨平台安装（`--os`/`--arch`）、`--prod` 标志、hoisted `node_modules`、`.npmrc` 增强（如 `min-release-age`）。
- 🧩 **新 Web API**：稳定支持 `OffscreenCanvas`（无 DOM 画布）、`DOMPoint`/`DOMRect`/`DOMMatrix` 等几何接口，以及 `structuredClone` 和 `postMessage` 的可转移/可序列化对象。
- 🔍 **调试与性能分析**：Chrome DevTools 可检查网络流量（`fetch`、`node:http`、WebSocket），内置 CPU 分析器支持火焰图（SVG）和 Markdown 报告。
- ⏳ **import defer**：支持 TC39 提案，延迟模块评估以优化启动时间。
- 📦 **deno compile 改进**：自动检测框架（Next.js、Astro、Fresh 等）、进度条显示、修复自启动 CLI 问题。
- 📊 **测试与覆盖率**：sanitizers 默认关闭、支持单测超时、新增函数覆盖率报告。
- 🔗 **模块加载器钩子**：实现 Node.js `module.registerHooks()` API，可自定义模块加载行为。
- 🔄 **其他重要更新**：`setTimeout`/`setInterval` 返回 `Timeout` 对象、TypeScript 6.0.3、V8 14.9、OpenTelemetry 新增控制台和 gRPC 导出器、`deno upgrade` 支持增量更新和从 PR 安装。

---

### [Deno 2.8 | Deno](https://deno.com/blog/v2.8#import-defer)

**原文标题**: [Deno 2.8 | Deno](https://deno.com/blog/v2.8#import-defer)

Deno 2.8 是迄今为止最大的一次次要版本发布，带来了大量新功能、性能提升和 Node.js 兼容性改进。

- 🚀 **新增子命令**：包括 `deno audit fix`（自动修复漏洞）、`deno bump-version`（自动版本号更新）、`deno ci`（CI 专用安装命令）、`deno pack`（打包为 npm tarball）、`deno transpile`（仅转译 TypeScript）、`deno why`（解释依赖来源）。
- 📦 **默认使用 npm**：`deno add` 和 `deno install` 现在默认将无前缀名称视为 npm 包，无需再输入 `npm:` 前缀。
- ⚡ **性能大幅提升**：冷 npm 安装速度提升 3.66 倍，`node:http` 吞吐量提升 2.21 倍，`node:buffer` base64 处理速度提升 3.07 倍，`node:crypto` scrypt 速度提升 2.12 倍。
- 🧪 **Node.js 兼容性飞跃**：Node 官方测试套件通过率从 42% 提升至 76.4%（3405/4457 测试通过），远超 Bun 的 40.6%。
- 🛠️ **调试与性能分析**：Chrome DevTools 现在可检查 Deno 的网络流量；新增内置 CPU 分析器，支持生成 `.cpuprofile`、火焰图 SVG 和 Markdown 报告。
- 📚 **TypeScript 6.0.3**：集成了最新的 TypeScript 编译器，并默认包含 `lib.node` 类型定义。
- 🔒 **安全与包管理**：支持 `catalog:` 协议、跨平台 npm 安装、`--prod` 标志、`nodeModulesLinker` 配置、`.npmrc` 增强支持。
- 🧪 **测试与覆盖率**：测试清理器默认关闭；新增超时选项；覆盖率报告新增函数覆盖率。
- 🌐 **Web API 增强**：新增 `OffscreenCanvas` 和几何接口（`DOMPoint`、`DOMRect` 等）；支持更多 Web Crypto 算法；`structuredClone` 和 `postMessage` 支持更多可传输和可序列化类型。
- 🧩 **模块加载器钩子**：实现了 Node 的 `module.registerHooks()` API，允许自定义模块加载行为。
- 🔄 **`setTimeout`/`setInterval` 变更**：现在返回 Node 的 `Timeout` 对象而非数字，提升性能并简化模型。
- 🎯 **其他改进**：Delta 更新减少下载量 87-93%；可从 PR 安装构建；`deno task` 输出带任务名前缀；`deno upgrade` 支持 PR 构建安装。

---

### [逐个库修复 JavaScript 可观测性 | Sentry 博客](https://blog.sentry.io/fixing-javascript-observability/?utm_source=javascriptweekly&utm_medium=paid-community&utm_campaign=observability-fy27q2-evergreen&utm_content=newsletter-sponsored-link-javascript-blog-learnmore)

**原文标题**: [Fixing JavaScript observability, one library at a time | Sentry Blog](https://blog.sentry.io/fixing-javascript-observability/?utm_source=javascriptweekly&utm_medium=paid-community&utm_campaign=observability-fy27q2-evergreen&utm_content=newsletter-sponsored-link-javascript-blog-learnmore)

## 概述总结

JavaScript 可观测性正经历从“猴子补丁”到内置运行时 API 的范式转变，Sentry 团队正主导推动 TracingChannel 在 44 个主流库中的原生支持，目前已合并 10 个 PR，剩余 34 个在推进中。

- 🐒 **猴子补丁不可扩展**：所有 JS APM 工具依赖的运行时拦截方法（IITM/RITM）在 ESM、非 Node 运行时、打包器等场景下频繁失效，且存在初始化顺序依赖问题
- 🔌 **TracingChannel 方案**：Node.js 内置的 diagnostics_channel API 让库原生发布结构化事件，APM 工具无需补丁即可订阅，零开销且跨运行时兼容（Node/Bun/Deno）
- 🤝 **社区共识但缺乏行动**：OpenTelemetry 团队认可此方案但未推动生态落地，Sentry 主动承担上游 PR 工作，采用“帮你实现并协助维护”的策略说服库维护者
- 🤖 **AI 规模化推进**：利用 Claude Code 构建反馈循环，覆盖研究提案、实现代码、审查反馈、进度追踪四个环节，将单人多年工作量转化为每日产出流水线
- 📊 **当前进展**：44 个目标库中 10 个已合并（含 mysql2、node-redis、ioredis 等关键驱动），4 个 PR 进行中，8 个在讨论，22 个未启动
- 🏢 **对 Sentry 的意义**：彻底解决 ESM 兼容性、初始化顺序、运行时锁定、打包器冲突等问题，简化 APM 工具代码，且方案中立不偏向任何厂商
- 🔄 **飞轮效应启动**：node-redis 团队主动对齐 TracingChannel 与自有 OTel 方案，mysql2 社区已出现纯 diagnostics_channel 订阅者替代猴子补丁方案
- 🗺️ **下一步计划**：推进 Express、PostgreSQL、Knex、GraphQL 等关键库，设计共享映射器注册表将 TracingChannel 事件自动转换为标准 OTel 跨度，最终实现“库原生发布事件 + 社区维护映射器 + APM 工具专注数据分析”的生态愿景

---

### [docx - 使用 JavaScript 生成.docx 文档](https://docx.js.org/)

**原文标题**: [docx - Generate .docx documents with JavaScript](https://docx.js.org/)

概述：本文探讨了人工智能在医疗诊断中的应用，强调了其提高准确性和效率的潜力，同时指出了数据隐私和算法偏见等挑战。

- 🩺 人工智能通过分析医学影像（如 X 光片和 CT 扫描），能辅助医生更快速、准确地检测疾病，如癌症和骨折。
- 📊 机器学习模型可处理大量患者数据，预测疾病风险，帮助实现早期干预和个性化治疗。
- 🔒 数据隐私问题突出，医疗数据的收集和使用需严格遵守法规，防止患者信息泄露。
- ⚖️ 算法偏见可能导致诊断不公，需确保训练数据多样性和模型透明度，以减少种族、性别等因素的影响。
- 🤝 人机协作是关键，AI 应作为辅助工具，而非替代医生，最终决策仍需专业医疗人员把关。

---

### [获取失败](https://javascriptweekly.com/link/185696/web)

**原文标题**: [Failed to retrieve](https://javascriptweekly.com/link/185696/web)

无法总结：获取内容失败，状态码 403。

---

### [docx/demo 在 master 分支 · dolanmiu/docx · GitHub](https://github.com/dolanmiu/docx/tree/master/demo)

**原文标题**: [docx/demo at master · dolanmiu/docx · GitHub](https://github.com/dolanmiu/docx/tree/master/demo)

这是一个名为 docx 的 GitHub 开源项目，拥有 5.7k 星标和 604 个复刻，用于生成和操作 Word 文档。

- 📁 项目包含丰富的示例代码（demo 目录），覆盖从基础到高级的 Word 文档功能
- 🎨 支持声明式样式、表格、图片、页眉页脚、编号列表等核心功能
- 🌐 提供多语言支持（如日语、中文）和国际化特性
- 🔧 包含高级功能：书签、超链接、评论、修订跟踪、自定义字体等
- 📊 支持复杂表格操作：合并单元格、边框设置、浮动表格等
- 📄 提供页面设置功能：分节、页边距、多列布局、页码等
- 🖼️ 支持多种图片处理方式：缓冲图片、Base64 编码、表格内嵌图片等
- 📝 包含模板文档生成和自定义属性功能
- 🧮 支持数学公式、文本框、复选框等特殊元素
- 🔄 提供流式处理（Node.js 流）和导出为 Base64 的功能

---

### [tinykeys](https://jamiebuilds.github.io/tinykeys/)

**原文标题**: [tinykeys](https://jamiebuilds.github.io/tinykeys/)

tinykeys 是一个轻量级（约 1KB）的现代键盘快捷键绑定库，支持通过 npm 安装，并提供简洁的 API 来监听组合键、序列键和修饰键。

- 📦 **轻量级库**：tinykeys 体积仅约 1KB，适合现代 Web 应用，通过 `npm install tinykeys` 即可安装。
- ⌨️ **多类型键绑定**：支持同时按下（如 `Shift+D`）、顺序按键（如 `y e e t`）以及修饰键组合（如 `$mod+([1-9])` 匹配 Control 或 Command 键）。
- 🎉 **实用示例**：可绑定 Konami 秘籍代码（方向键序列加 B、A、Enter）触发彩纸特效（需配合 `canvas-confetti` 库）。
- 🔍 **调试功能**：提供事件调试器，记录按键的 `key`、`code`、修饰键状态、重复状态等详细信息，便于开发测试。
- ⚠️ **注意事项**：`event.getModifierState(event.key)` 用于检测按下的键是否为修饰键（如 Shift、Ctrl 等）。

---

### [nodejs/axios-to-whatwg-fetch - Codemod 注册表](https://app.codemod.com/registry/@nodejs/axios-to-whatwg-fetch)

**原文标题**: [nodejs/axios-to-whatwg-fetch - Codemod Registry](https://app.codemod.com/registry/@nodejs/axios-to-whatwg-fetch)

概述总结  
该内容介绍了 Registry 平台，一个社区驱动的代码迁移工具集，支持搜索、发布和贡献代码转换工具。  
- 🔍 探索社区主导的代码迁移工具，用于迁移、优化和转换代码库  
- 📦 搜索包，例如使用筛选条件如"scope:acme tag:migration by:codemod react"  
- ⌨️ 输入"/"快速搜索  
- 🤝 准备贡献？构建自己的代码转换工具并与社区分享  
- 📤 发布代码转换工具  
- 🌐 加入社区

---

### [用户态迁移 | Node.js 学习](https://nodejs.org/learn/getting-started/userland-migrations)

**原文标题**: [Userland Migrations | Node.js Learn](https://nodejs.org/learn/getting-started/userland-migrations)

Node.js 用户空间迁移工具帮助开发者轻松应对版本升级，通过官方审核的代码转换脚本简化弃用功能处理和新特性适配。

- 🚀 **核心目标**：协助开发者将代码库迁移至最新 Node.js 版本，简化弃用处理、新特性适配和破坏性变更应对
- 📦 **官方迁移工具**：通过 `npx codemod <名称>` 命令运行，例如 `@nodejs/import-assertions-to-attributes`，所有官方迁移脚本均发布在 Codemod 注册表的 `@nodejs` 作用域下
- ✅ **最佳实践**：在独立分支运行迁移、审查代码变更、运行测试套件、格式化/检查代码，确保迁移安全可靠
- 🔍 **注册表使用**：Codemod 注册表提供完整迁移脚本列表，部分脚本可能未在文档中列出，需自行探索；登录后可点赞反馈
- 💬 **反馈渠道**：通过 Node.js Userland Migrations 仓库提交建议或问题
- 📊 **进度追踪**：GitHub 项目看板按迁移类型、Node.js 版本和状态（待办/进行中/完成/未计划）分类管理，欢迎查看"待办"列参与贡献
- 📖 **迁移指南**：完整指南位于迁移指南专区，重大版本更新仅包含生命周期结束的弃用和破坏性变更

---

### [热更新器 - React Native 的自托管 OTA 更新](https://hot-updater.dev/)

**原文标题**: [Hot Updater - Self-hosted OTA updates for React Native](https://hot-updater.dev/)

Hotupdater 是一个自托管的 React Native OTA 更新工具，提供即时部署、回滚和版本管理功能，支持新旧架构和插件扩展。

- 🚀 支持即时部署 OTA 更新，无需经过应用商店审核
- ♻️ 提供可靠的回滚机制，可快速恢复到先前版本
- 🛠️ 内置插件系统，可自定义构建和部署流程
- 📦 兼容新旧版 React Native 架构
- 🔖 支持语义化版本控制和自定义目标规则
- 🖥️ 提供 Web 控制台，方便管理部署和监控更新

---

### [GitHub - perspective-dev/perspective: 一款数据可视化与分析组件，特别适用于大型和/或流式数据集。](https://github.com/perspective-dev/perspective)

**原文标题**: [GitHub - perspective-dev/perspective: A data visualization and analytics component, especially well-suited for large and/or streaming datasets. · GitHub](https://github.com/perspective-dev/perspective)

Perspective 是一個專為大規模和串流數據設計的互動式分析與資料視覺化元件，支援 WebAssembly、Python 和 Rust 高效查詢引擎。

- 📊 提供框架無關的 UI 元件（自訂元素），可連接瀏覽器內（WebAssembly）或遠端（WebSocket）的數據模型，包含資料網格及 10+ 種圖表類型
- 🔌 具備可插拔引擎的數據模型 API，能讓 Perspective UI 查詢外部資料源（如 DuckDB），並將視圖配置轉換為原生查詢
- ⚡ 內建以 C++ 編寫、編譯至 WebAssembly/Python/Rust 的高效記憶體串流數據模型，支援 Apache Arrow 讀寫與串流
- 📓 提供 JupyterLab 小工具與 Python 客戶端函式庫，便於筆記本進行互動式數據分析
- 🌐 支援多語言 API：JavaScript、Python、Rust，並整合 ClickHouse 與 DuckDB 虛擬伺服器
- 🎯 包含豐富範例（如編輯、DuckDB、市場、串流等），並隸屬於 OpenJS Foundation

---

### [引言](https://partytown.qwik.dev/)

**原文标题**: [Introduction](https://partytown.qwik.dev/)

### 概述总结
Partytown 是一个将第三方脚本迁移至 Web Worker 的轻量库，旨在释放主线程资源以提升网站性能，目前仍处于 Beta 阶段。

- 🚀 **核心目标**：将第三方脚本（如分析工具、广告）从主线程卸载到 Web Worker，减少主线程负担。
- ⚙️ **工作原理**：通过 Web Worker 同步读写 DOM，支持未修改的第三方脚本直接运行。
- 🛡️ **沙箱与限制**：可控制第三方脚本对主线程 API 的访问，并批处理 DOM 操作以减少布局抖动。
- 📉 **性能影响**：解决第三方脚本导致的网络请求过多、CPU 密集、DOM 阻塞、缓存不足等问题。
- 🧩 **适用场景**：适合非关键渲染路径的脚本（如分析、跟踪、A/B 测试），异步执行不阻塞首屏。
- ✅ **已验证服务**：支持 Google Tag Manager、Facebook Pixel、Mixpanel 等常见服务，且不硬编码特定 API。
- 🔌 **插件生态**：维护“Ready to Party”插件列表，鼓励开发者贡献集成测试和配置。
- 📚 **学习资源**：提供文档、常见问题、权衡说明及多框架集成指南（如 React、Next.js、Angular）。

---

### [TypeScript SDK 升级 - AT 协议](https://atproto.com/blog/ts-sdk-upgrades)

**原文标题**: [TypeScript SDK Upgrades - AT Protocol](https://atproto.com/blog/ts-sdk-upgrades)

### 概述总结

TypeScript SDK 团队宣布了重大升级，包括所有包迁移至 ESM、放弃对 Node 18/20的支持，以及正式推荐lex SDK 用于新开发。lex SDK 进入稳定预览阶段（0.1.0），但部分 Bluesky 特定辅助方法尚未兼容，团队计划构建新辅助包填补空白。字符串类型系统强化可能带来迁移挑战，但现有@atproto/xrpc 和@atproto/api 包将继续维护。

- 🔧 **核心升级**：所有@atproto 包已重构并重新发布，全面支持 ESM，放弃 Node 18/20，承诺支持Node LTS 版本
- 🚀 **lex SDK 推广**：移除预览警告，正式推荐 lex 和 lex-server 用于新开发，标记为 0.1.0 稳定预览版
- ⚠️ **辅助功能缺口**：部分 Bluesky 特定功能（如偏好设置、标签处理）尚未兼容 lex，计划开发新辅助包
- 🧩 **字符串类型强化**：lex 引入严格字符串类型区分（如 DidString、AtUriString），可能影响现有项目迁移
- 📦 **向后兼容**：现有@atproto/xrpc 和@atproto/api 包将继续维护至 lex 1.0 后进入维护模式
- 🌳 **性能优化**：ESM 构建支持更好的 tree-shaking，减少包体积，TypeScript 6 升级为 TypeScript 7 做准备
- 💬 **社区反馈**：lex 1.0 发布时间取决于社区反馈，欢迎开发者提出意见或提交 issue

---

### [发布 0.29.0 · kysely-org/kysely · GitHub](https://github.com/kysely-org/kysely/releases/tag/v0.29.0)

**原文标题**: [Release 0.29.0 · kysely-org/kysely · GitHub](https://github.com/kysely-org/kysely/releases/tag/v0.29.0)

Kysely v0.29.0 版本发布，引入了多项新功能、改进和破坏性变更。

- 💥 新增 `$pickTables` 和 `$omitTables` 编译时辅助函数，用于缩小下游查询的数据库视图，降低编译复杂度。
- 🔒 引入 `ReadonlyKysely<DB>` 类型，将数据库实例变为只读，禁止写操作（如 `deleteFrom`、`insertInto`）。
- 🟨 新增 PGlite 方言，并引入 `supportsMultipleConnections` 标志，用于简化 SQLite 方言的连接管理。
- 🎯 `$narrowType` 支持嵌套缩小和判别联合类型，提升类型推断精度。
- 🛑 支持基于 Web 标准的查询取消，可传递 `AbortSignal` 并选择不同的中止策略（忽略、取消查询或终止会话）。
- 🛡️ 新增 `SafeNullComparisonPlugin`，当右操作数为 `null` 时，自动将 `=` 和 `!=` 转换为 `IS` 和 `IS NOT`。
- ⚙️ `ParseJSONResultsPlugin` 新增 `shouldParse(value, path)` 选项，允许通过 JSON 路径精细控制哪些字段被 `JSON.parse`。
- 🚀 多项功能增强：迁移器支持禁用事务、`eb.case` 新增 `thenRef`/`whenRef`/`elseRef`、`$extendTables`、表达式支持索引创建等。
- 🐘🐬 数据库特定改进：PostgreSQL/MySQL 支持外部表、PostgreSQL 支持 `ALTER TYPE`、MySQL 支持临时表等。
- ⚠️ 破坏性变更：迁移相关导出移至 `'kysely/migration'`、最低 TypeScript 版本升至 5.4、停止提供 CommonJS 文件、移除多项弃用 API。

---

### [GitHub - sockmaster27/svader: 创建 GPU 渲染的 Svelte 组件](https://github.com/sockmaster27/svader)

**原文标题**: [GitHub - sockmaster27/svader: Create GPU-rendered Svelte components · GitHub](https://github.com/sockmaster27/svader)

Svader 是一个用于创建 GPU 渲染 Svelte 组件的工具，支持 WebGL 和 WebGPU 片段着色器。

- 🎨 **核心功能**：通过 WebGL 和 WebGPU 片段着色器，在 Svelte 中创建 GPU 加速的图形组件
- 📦 **安装方式**：支持 npm、pnpm、Bun 和 Yarn 包管理器安装
- 🖥️ **WebGL 使用**：提供 `<WebGlShader>` 组件，支持 GLES 着色器代码和内置参数（如 resolution、time、offset）
- 🚀 **WebGPU 使用**：提供 `<WebGpuShader>` 组件，支持 WGSL 着色器代码和内置参数（如 resolution、time、offset）
- ⚙️ **参数系统**：支持自定义 uniform 参数，WebGL 需指定 name/type/value，WebGPU 需指定 label/binding/value
- 🔄 **内置值**：包含 resolution、scale、time、offset 等常用内置参数，可自动处理渲染更新
- 🛡️ **兼容性**：WebGL 支持所有现代浏览器，WebGPU 仍处于实验阶段
- 📊 **项目状态**：453 颗星、8 个分支、16 个版本发布，采用 MIT 许可证

---

### [福昕 MCP 服务器：面向 AI 代理的 30 多种 PDF 工具](https://developer-api.foxit.com/developer-blogs/use-cases-workflow-examples/automated-document-pipelines/foxit-mcp-server-ai-pdf-tools/?utm_source=draftdev&utm_campaign=jsweekly)

**原文标题**: [Foxit MCP Server: 30+ PDF Tools for AI Agents](https://developer-api.foxit.com/developer-blogs/use-cases-workflow-examples/automated-document-pipelines/foxit-mcp-server-ai-pdf-tools/?utm_source=draftdev&utm_campaign=jsweekly)

概述总结  
Foxit 的高级 PDF 提取引擎能处理扫描件、复杂表格和表单字段，通过 OCR、布局识别和 AI 解析将 12 种 PDF 元素转化为结构化 JSON 数据，适用于 RAG、BI 和 CRM 工作流。  

- 📄 解决基础 PDF 库无法处理扫描文档、复杂表格和表单字段的痛点  
- 🔍 集成 OCR、布局识别和 AI 解析技术，确保数据提取完整性  
- 🧩 支持提取 12 种 PDF 元素类型，输出结构化 JSON 格式  
- 🚀 可直接用于 RAG（检索增强生成）、BI（商业智能）和 CRM（客户关系管理）工作流

---

### [GitHub - Agent-Field/agentfield: 像 API 和微服务一样构建、运行和扩展 AI 代理——从第一天起即可观测、可审计且具备身份感知。](https://github.com/Agent-Field/agentfield)

**原文标题**: [GitHub - Agent-Field/agentfield: Build, run and scale AI agents like API and microservices - observable,auditable and identity-aware from day one. · GitHub](https://github.com/Agent-Field/agentfield)

AgentField 是一个开源的控制平面，用于将 AI 代理构建和扩展为类似 API 的后端基础设施，支持部署、观察和审计。

- 🧠 **核心功能**：将 Python、Go 或 TypeScript 编写的代理逻辑转化为生产级 REST 端点，支持路由、协调、内存、异步执行和加密审计。
- 🚀 **快速上手**：提供 CLI 工具（`af init`）和“提示到生产”模式，可一键生成多代理后端，支持 Docker Compose 部署。
- ⚙️ **关键特性**：包括结构化 AI 输出（`app.ai(schema=...)`）、人类审批暂停（`app.pause()`）、跨代理调用（`app.call()`）和自动注册。
- 🔐 **身份与治理**：每个代理拥有 W3C 去中心化身份（DID）和 Ed25519 密钥，支持可验证凭证（VC）和基于标签的策略执行。
- 📊 **可观测性**：自动生成工作流 DAG 图、Prometheus 指标、结构化日志和执行时间线，支持健康检查和关联 ID。
- 🧪 **高级部署**：支持金丝雀部署、A/B 测试、蓝绿部署，以及流量权重路由和版本健康追踪。
- 🧩 **多语言支持**：提供 Python、Go 和 TypeScript SDK，以及 MCP 服务器集成。
- 🛠️ **构建案例**：包括自主工程团队、深度研究引擎、安全审计和云安全扫描等实际项目。

---

### [Meticulous AI - 无需编写测试的自动化前端测试](https://www.meticulous.ai/?utm_source=jsweekly&utm_medium=referral&utm_campaign=26q2&utm_content=classified)

**原文标题**: [Meticulous AI - Automated Frontend Testing Without Writing Tests](https://www.meticulous.ai/?utm_source=jsweekly&utm_medium=referral&utm_campaign=26q2&utm_content=classified)

Meticulous 是一款自动化、全面且确定性的测试工具，让开发者无需手动编写或维护测试，即可在代码合并前发现所有回归问题。

- 🚀 **零开发者投入**：只需添加脚本标签，Meticulous 会自动录制日常交互并生成覆盖所有代码路径的测试套件。
- 🧪 **全面且确定性**：从 Chromium 层面构建，消除测试不稳定因素，确保测试快速且可靠。
- ⚡ **闪电般快速**：通过计算集群并行测试，可在 120 秒内完成数千个屏幕的测试。
- 🔄 **自动演化**：测试套件随应用自动更新，无需手动维护，确保始终覆盖最新功能。
- 🔒 **安全集成**：支持 NextJS、React、Vue、Angular 等主流框架，且可搭配现有测试套件或完全替代。
- 🏢 **受信赖**：已被 Dropbox、Notion 等超过 100 家组织采用，开发者反馈“无法想象没有它的工作”。
- 📈 **加速迭代**：大幅提升代码发布速度，确保无回归问题，同时降低调试和测试维护成本。

---

### [模板字面量（模板字符串）- JavaScript | MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals#tagged_templates)

**原文标题**: [Template literals (Template strings) - JavaScript | MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals#tagged_templates)

模板字面量（Template literals）是使用反引号（`）分隔的字符串，支持多行文本、字符串插值和标签模板等高级功能，自 2015 年起已广泛兼容于各浏览器。

- 📝 **基本语法**：使用反引号替代引号，通过`${expression}`嵌入表达式，支持多行文本和转义（如`\``转义反引号）
- 🔗 **字符串插值**：自动将表达式转换为字符串并嵌入，比传统拼接更简洁易读，例如`${a + b}`替代`"Fifteen is " + (a + b)`
- 📐 **多行字符串**：直接换行即可创建多行文本，无需`\n`，也可用反斜杠转义换行保持单行
- 🪆 **嵌套模板**：可在占位符内嵌套模板字面量，实现条件逻辑的简洁写法，如`icon-${condition ? "expander" : "collapser"}`
- 🏷️ **标签模板**：通过自定义函数处理模板，函数接收字符串数组和表达式值，可返回任意结果（不限于字符串）
- 🧊 **原始字符串**：通过`strings.raw`访问未转义的原始字符串，`String.raw()`方法可直接创建原始字符串
- ⚠️ **转义序列**：标签模板中允许非法转义序列（如`\unicode`），但“熟”字符串会显示为`undefined`；未标签模板中非法转义会报错
- 🔄 **缓存特性**：标签函数每次调用时字符串数组相同（冻结），可用于缓存优化

---

