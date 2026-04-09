### [Node 周刊第 619 期：2026 年 4 月 9 日](https://nodeweekly.com/issues/619)

**原文标题**: [Node Weekly Issue 619: April 9, 2026](https://nodeweekly.com/issues/619)

本期 Node Weekly 通讯涵盖安全事件、工具更新、技术文章及行业动态，重点关注 Axios 供应链攻击分析、Node.js 安全漏洞赏金计划暂停、以及多项开源工具的新版本发布。

- ⚠️ **Axios 供应链攻击分析**：Axios 团队详细复盘了近期因恶意依赖导致的安全事件，攻击涉及精心策划的社会工程手段，提醒 npm 包维护者警惕类似手法。
- 🛡️ **Node.js 安全漏洞赏金计划暂停**：由于资助方“互联网漏洞赏金”项目调整，Node.js 自 2016 年运行的安全漏洞赏金计划暂时停止，但仍可提交无奖金报告。
- 📦 **工具更新速递**：tsdown 新增 Node 单文件应用打包支持；web-audio-api 为 Node 提供完整的 Web Audio API 兼容；TinyTTS 推出 3.4MB 轻量文本转语音模型。
- 🔧 **开发库版本升级**：包括 ky HTTP 客户端 2.0 版、ESLint 10.2 语言感知规则支持、Ink 7.0 基于 React 19 的 CLI 框架，以及 Axios 1.15.0 新增 Bun/Deno 支持。
- 🗣️ **技术社区动态**：Postgres 虚拟会议 POSETTE 2026 开放报名；npmx 项目访谈探讨 npm registry 浏览工具；开发者需警惕 npm 包中 postinstall 脚本的潜在风险。

---

### [事后分析：axios npm 供应链安全事件 · Issue #10636 · axios/axios · GitHub](https://github.com/axios/axios/issues/10636)

**原文标题**: [Post Mortem: axios npm supply chain compromise · Issue #10636 · axios/axios · GitHub](https://github.com/axios/axios/issues/10636)

axios 项目于 2026 年 3 月 31 日发生 npm 供应链攻击，两个恶意版本（1.14.1 和 0.30.4）通过维护者被入侵的账户发布，其中注入了包含远程访问木马的依赖包，恶意版本在约 3 小时后被移除。

- 🔍 **影响检查**：通过命令检查是否安装恶意版本，若受影响需立即降级、删除依赖、轮换所有密钥并检查网络连接
- 🕵️ **攻击过程**：攻击者通过社会工程和远程木马入侵维护者电脑，获取 npm 账户权限后发布恶意包
- 🛡️ **应对措施**：彻底重置维护者所有设备与凭证，计划采用 OIDC 发布流程、不可变发布设置等安全改进
- ⏳ **时间线**：攻击始于 3 月 30 日，恶意包在 3 月 31 日 00:21 至 03:15 UTC 间活跃，随后被安全团队移除
- 📚 **经验总结**：需避免从个人账户直接发布、建立自动检测机制，开源维护者需警惕社会工程攻击

---

### [axios 在 npm 上遭入侵——恶意版本植入远程访问木马 - StepSecurity](https://www.stepsecurity.io/blog/axios-compromised-on-npm-malicious-versions-drop-remote-access-trojan)

**原文标题**: [axios Compromised on npm - Malicious Versions Drop Remote Access Trojan - StepSecurity](https://www.stepsecurity.io/blog/axios-compromised-on-npm-malicious-versions-drop-remote-access-trojan)

2026 年 3 月 30 日，StepSecurity 发现 npm 上发布的两个恶意 axios 版本（1.14.1 和 0.30.4），它们通过被劫持的维护者账户发布，并注入了一个隐藏依赖`plain-crypto-js@4.2.1`。该依赖的唯一目的是执行一个`postinstall`脚本，部署跨平台远程访问木马（RAT）。攻击具有高度预谋和隐蔽性，在安装后会自动删除证据。StepSecurity 通过其安全工具检测并协助缓解了此次攻击。

- 🔐 **账户劫持**：攻击者入侵了 axios 主要维护者的 npm 账户，并更改了注册邮箱，随后发布了恶意版本。
- 📦 **依赖注入**：恶意 axios 版本注入了从未在源码中使用的依赖`plain-crypto-js@4.2.1`，其`postinstall`脚本会触发 RAT 投放器。
- 🛡️ **跨平台攻击**：投放器会根据操作系统（macOS、Windows、Linux）下载并执行相应的第二阶段恶意载荷，同时会联系活跃的命令与控制服务器。
- 🧹 **证据销毁**：执行后，恶意脚本会删除自身，并用一个干净的`package.json`存根替换原文件，以逃避取证检测。
- ⏱️ **精心策划**：攻击提前 18 小时准备，恶意依赖先发布为“干净”版本以建立历史记录，两个 axios 恶意版本在 39 分钟内相继发布。
- 🔍 **检测与响应**：StepSecurity 的 AI Package Analyst 和 Harden-Runner 检测到异常网络连接（如对 sfrclak.com:8000 的调用），并协助项目维护者和 npm 迅速下架恶意包。
- 📋 **影响与应对**：如果安装了受影响版本，应假设系统已入侵，需检查代码库、CI/CD 流水线和开发机器，移除恶意包，旋转所有可能泄露的凭证，并考虑实施包版本冷却期等防御策略。

---

### [Axios 供应链攻击采用了个性化定向社交工程手段](https://simonwillison.net/2026/Apr/3/supply-chain-social-engineering/)

**原文标题**: [The Axios supply chain attack used individually targeted social engineering](https://simonwillison.net/2026/Apr/3/supply-chain-social-engineering/)

Axios 团队发布了对供应链攻击的详细事后分析，该攻击通过针对其维护者的高度定制化社交工程手段，成功植入恶意依赖包。

- 🎭 攻击者伪装成某公司创始人，克隆其形象并创建仿冒公司，通过精心设计的 Slack 工作区邀请目标加入
- 👥 在 Slack 中设置虚假团队频道和伪造的 OSS 维护者资料，营造高度可信的协作环境
- 📅 通过 Microsoft Teams 安排会议，利用时间压力诱导安装伪装成更新程序的远程访问木马（RAT）
- 🔐 被盗凭证最终导致恶意软件包被发布到官方渠道
- ⚠️ 作者指出这种针对开源维护者的定向攻击策略需要引起所有重要项目维护者的警惕

---

### [攻击者正瞄准高影响力 Node.js 维护者展开 C...](https://socket.dev/blog/attackers-hunting-high-impact-nodejs-maintainers)

**原文标题**: [Attackers Are Hunting High-Impact Node.js Maintainers in a C...](https://socket.dev/blog/attackers-hunting-high-impact-nodejs-maintainers)

Socket CEO Feross Aboukhadijeh 详细分析了朝鲜如何通过供应链攻击劫持了 Axios 库，并探讨了此类事件对未来软件供应链安全的深远影响。

- 🕵️ 朝鲜黑客通过劫持 Axios 库维护者账户，植入恶意代码进行供应链攻击
- 🔓 攻击利用了 npm 生态系统的信任机制，通过依赖更新广泛传播恶意软件
- ⚠️ 此次事件暴露了开源软件维护环节的脆弱性和账户安全的重要性
- 🛡️ 企业需要加强依赖监控、采用安全工具并实施多重验证等防护措施
- 🌐 软件供应链安全已成为全球性挑战，需要开发者、企业和社会共同应对

---

### [日程安排 | POSETTE：2026 年 Postgres 大会 - POSETTE](https://posetteconf.com/2026/schedule/)

**原文标题**: [Schedule | POSETTE: An Event for Postgres 2026 - POSETTE](https://posetteconf.com/2026/schedule/)

该内容是关于 POSETTE: An Event for Postgres 2026 线上会议的日程安排和主题介绍，涵盖多个直播流，聚焦于 PostgreSQL 的最新发展、性能优化、云集成、AI 应用及社区动态。

- 🗓️ 会议于 6 月 10 日至 18 日分四个直播流进行，包含主题演讲、技术分享和总结环节
- 🗣️ 主题演讲涉及微软对 Postgres 的投入、Postgres 19 新特性讨论及社区贡献者见解
- 🛠️ 技术主题包括 JSON 数据处理、查询优化参数、模糊测试、设计模式及 AI 工具集成（如 MCP 协议）
- ☁️ 多个议题聚焦 Azure 云平台，涵盖迁移策略、性能提升（如 Azure HorizonDB）和托管服务优化
- 📊 分享内容涉及数据库扩展（如图计算 Apache AGE）、逻辑复制、分区管理、安全模型及版本性能对比
- 🤖 探讨 PostgreSQL 在 AI 时代的应用，包括生产级 RAG 系统、智能代理和数据检索优化
- 🧩 社区与实践主题涵盖贡献指南、认证历史、约束改进、队列实现及测试覆盖工具
- 📢 会议鼓励参与社区互动，提供 Discord、社交媒体等交流渠道，由微软 Postgres 团队组织

---

### [你不能取消一个 JavaScript 承诺（除了有时可以）- Inngest 博客](https://www.inngest.com/blog/hanging-promises-for-control-flow)

**原文标题**: [You can't cancel a JavaScript promise (except sometimes you can) - Inngest Blog](https://www.inngest.com/blog/hanging-promises-for-control-flow)

JavaScript Promise 本身没有内置的取消机制，但可以通过返回一个永不解析的 Promise 来中断异步函数的执行，这种方法不会抛出异常，而是让函数在等待中停止，最终由垃圾回收器清理。

- 🚫 JavaScript Promise 没有原生的 `.cancel()` 方法，因为取消执行可能留下资源脏状态，需要协作清理
- ⏸️ 通过返回永不解析的 Promise 来中断 `async/await` 函数，函数会停止在 `await` 处，不会继续执行后续代码
- 🧩 使用生成器（Generators）可以实现更干净的中断控制，但语法不够直观，且并发处理复杂
- 🔄 结合步骤记忆（Memoization）和永不解析的 Promise，可以实现分步执行和恢复，适用于工作流场景
- 🗑️ 中断后，未解析的 Promise 和函数状态会被垃圾回收器清理，前提是没有外部引用保持
- ⚠️ 这种方法依赖于垃圾回收的非确定性，且需确保没有意外引用链，否则可能导致内存泄漏

---

### [[RFC] JSIR：面向 JavaScript 的高级中间表示 - MLIR - LLVM 讨论论坛](https://discourse.llvm.org/t/rfc-jsir-a-high-level-ir-for-javascript/90456)

**原文标题**: [[RFC] JSIR: A High-Level IR for JavaScript - MLIR - LLVM Discussion Forums](https://discourse.llvm.org/t/rfc-jsir-a-high-level-ir-for-javascript/90456)

JSIR 是一种基于 MLIR 框架的高层次 JavaScript 中间表示，旨在填补 JavaScript 工具链中缺乏公开、稳定 IR 的空白。它通过保留 AST 的全部信息并支持高保真的双向转换，为代码分析和转换提供了强大的数据流分析能力。

- 🎯 **填补 IR 空白**：JavaScript 社区已有大量基于 AST 的工具（如 Babel、ESLint），但缺乏公开的 IR 工具，JSIR 旨在解决这一问题。
- 🔄 **高保真双向转换**：JSIR 设计支持无损的“源代码 ↔ AST ↔ JSIR”转换，便于源代码到源代码的转换和反编译。
- 🏗️ **基于 MLIR 构建**：利用 MLIR 的区域（region）表示控制流结构，并提供数据流分析 API，提升分析能力。
- 🛠️ **实际应用场景**：在 Google 内部已用于生产环境，支持反编译 Hermes 字节码、代码反混淆等任务。
- 🌐 **开源与社区贡献**：项目已在 GitHub 开源，并希望与 MLIR 社区合作，改进数据流分析等功能，探讨上游集成的可能性。

---

### [GitHub - google/jsir：下一代JavaScript分析工具集 · GitHub](https://github.com/google/jsir)

**原文标题**: [GitHub - google/jsir: Next-generation JavaScript analysis tooling · GitHub](https://github.com/google/jsir)

JSIR 是一个基于 MLIR 的下一代 JavaScript 分析工具，其核心是一个高级中间表示，支持数据流分析和无损转换回源代码，适用于源码到源码的转换。它在 Google 被用于反编译和反混淆等场景，通过结合高级 AST 表示和低级数据流分析能力，平衡了可读性与分析效率。

- 🛠️ **核心设计**：基于 MLIR 的高级中间表示，支持数据流分析和无损源码转换，适用于源码到源码转换。
- 🔍 **应用场景**：在 Google 用于 JavaScript 反编译（如 Hermes 字节码）和反混淆，结合 Gemini LLM 提升效果。
- ⚖️ **设计亮点**：平衡高级 AST 可逆性与低级数据流分析需求，使用 MLIR 区域精确建模控制流结构。
- 🐳 **快速开始**：推荐使用 Docker 构建和运行，支持通过 `jsir_gen` 工具分析 JavaScript 文件。
- 🏗️ **本地构建**：需安装 clang 和 Bazel（建议用 Bazelisk），构建过程耗时且占用存储空间，可测试 LLVM 集成。
- 🧪 **测试与运行**：提供完整的测试命令，支持转换 JavaScript 源码到 JSHIR，示例命令包含输入文件和处理流程。
- 📚 **资源链接**：包含 LLVM 开发者会议演讲和结合 LLM 的反混淆论文，项目声明非官方 Google 产品。

---

### [Azure SDK for JavaScript 中 Node.js 20.x 支持终止公告 - Azure SDK 博客](https://devblogs.microsoft.com/azure-sdk/announcing-the-end-of-support-for-node-js-20-x-in-the-azure-sdk-for-javascript/)

**原文标题**: [Announcing the end of support for Node.js 20.x in the Azure SDK for JavaScript - Azure SDK Blog](https://devblogs.microsoft.com/azure-sdk/announcing-the-end-of-support-for-node-js-20-x-in-the-azure-sdk-for-javascript/)

Azure SDK for JavaScript 将于 2026 年 7 月 9 日起停止支持 Node.js 20.x，建议用户升级至活跃的 Node.js LTS 版本以继续获得功能更新和安全维护。

- 🚨 **停止支持时间**：2026 年 7 月 9 日起，Azure SDK for JavaScript 将不再支持 Node.js 20.x（该版本于 2026 年 4 月 30 日终止生命周期）。
- 📅 **原因说明**：遵循 Node.js 的发布周期，版本结束维护后将不再接收漏洞修复或安全更新，为确保库的现代性与安全性，SDK 将定期弃用已终止生命周期的 Node.js 版本。
- ⚠️ **影响与警告**：从该日期起，SDK 将设置 Node.js 22.x 为最低支持版本；使用 Node.js 20.x 安装新版 SDK 时会触发引擎弃用警告，若设置 `engine-strict=true` 则会导致安装错误。
- 🔄 **升级建议**：强烈建议用户升级至最新的活跃 Node.js LTS 版本，以持续获得 SDK 的最新功能与安全更新。
- 📘 **政策参考**：此次变更符合 Azure SDK 支持政策，无需升级 SDK 主版本；用户可查阅 Azure SDK 及 JavaScript 专项支持政策了解更多详情。

---

### [npm 可信发布现已支持 CircleCI - GitHub 更新日志](https://github.blog/changelog/2026-04-06-npm-trusted-publishing-now-supports-circleci/)

**原文标题**: [npm trusted publishing now supports CircleCI - GitHub Changelog](https://github.blog/changelog/2026-04-06-npm-trusted-publishing-now-supports-circleci/)

npm 现已支持 CircleCI 作为可信发布的 OIDC 提供商，进一步扩展了 CI/CD 管道的安全发布能力，同时推出了 npmjs.com 网站的深色模式，以提升用户体验。

- 🔐 npm 可信发布新增支持 CircleCI，与 GitHub Actions 和 GitLab CI/CD 并列，维护者可直接通过 CI/CD 流程认证，无需存储凭据
- 🌐 配置可通过 npm 官网或 `npm trust` CLI 命令完成，相关设置指南已更新至可信发布文档
- 🌙 npmjs.com 网站推出深色模式，该功能通过 GitHub Copilot 代理模式高效开发，大幅减少了工程时间
- 🛡️ 团队持续聚焦于强化 npm 的安全性和维护者对软件包发布的控制权
- 💬 用户可通过社区讨论提供反馈或提问

---

### [npmx：人民驱动的软件包索引 | Igalia](https://www.igalia.com/chats/npmxyz)

**原文标题**: [npmx : The PeopleâPowered Package Index | Igalia](https://www.igalia.com/chats/npmxyz)

npmx 是一个由社区驱动的开源项目，旨在为 npm 注册表提供一个更现代化、功能更丰富的网站浏览界面，以替代 npmjs.com。它强调用户体验、社区协作和开源精神，通过集成社交功能、生态清理工具（如 e18e）和去中心化身份协议（AT Proto），致力于提升包管理的透明度、可访问性和可持续性。

- 🌐 **替代浏览界面**：npmx 是 npmjs.com 的替代网站，专注于改进包浏览和管理体验，支持暗色模式、更友好的管理界面和更多包信息展示。
- 👥 **社区驱动开发**：项目由 Daniel Roe 和 Matias Capeletto 发起，通过 Discord 社区快速吸引了大量贡献者，强调协作、欢迎文化和团队力量。
- 🔗 **集成生态工具**：与 e18e 项目深度集成，展示包的安装大小、漏洞报告、依赖树变化等信息，帮助开发者选择更优的包。
- 🌍 **去中心化社交功能**：基于 AT Proto 协议实现社交功能（如点赞包），允许用户通过个人数据服务器（PDS）自主管理数据，增强身份和信任网络。
- 💡 **提升信任与透明度**：计划通过项目分组、维护者活动、社交图谱等方式，更全面地展示包的健康状况和社区信任度。
- 💰 **可持续性与资助**：项目旨在长期可持续，考虑通过基金会、数据主权倡议和开放集体（Open Collective）获取资助，以支持核心贡献者。
- 🛠 **扩展功能**：提供包管理辅助工具（如通过 CLI 代理发布包）、批量操作支持，并计划整合更多开发者工具数据（如 GitHub）。
- 🌱 **健康开源实践**：倡导团队协作、定期休假（如项目间协调的“休假周”），关注开源开发者的身心健康和项目治理。

---

### [npmx - npm 注册表的包浏览器](https://npmx.dev/)

**原文标题**: [npmx - Package Browser for the npm Registry](https://npmx.dev/)

npmx 是一款专为 npm 注册表设计的快速现代浏览器，旨在优化包搜索体验，支持即时搜索功能，并基于多种前端框架构建。

- 🔍 **即时搜索功能** – 提供快速搜索 npm 包的能力，用户可自由开启或关闭该功能
- 🛠️ **技术栈多样** – 基于 Nuxt、Vue、React、Svelte、TypeScript 等多种流行前端框架与工具构建
- 📅 **持续更新** – 最新版本 v0.8.1 于 2026 年 4 月 8 日发布，保持活跃开发
- 🤝 **社区参与** – 鼓励用户通过 GitHub 贡献代码，或在 Discord 社区交流想法、获取帮助
- 📢 **信息同步** – 可通过 Bluesky 关注项目最新动态，及时获取更新信息

---

### [Node.js — 因资金短缺暂停安全漏洞赏金计划](https://nodejs.org/en/blog/announcements/discontinuing-security-bug-bounties)

**原文标题**: [Node.js — Security Bug Bounty Program Paused Due to Loss of Funding](https://nodejs.org/en/blog/announcements/discontinuing-security-bug-bounties)

Node.js 安全漏洞赏金计划因外部资金中断而暂停，但安全报告流程与团队承诺保持不变。

- 🛑 漏洞赏金计划暂停：因互联网漏洞赏金（IBB）项目资金中断，Node.js 暂停了通过 HackerOne 提供的漏洞赏金奖励计划
- 💰 缺乏独立预算：作为志愿者驱动的开源项目，Node.js 目前无法自行承担赏金计划的资金支持
- 🚨 安全报告持续接收：仍通过 HackerOne 接受漏洞报告，安全团队会继续及时处理与响应
- 🔒 安全承诺不变：Node.js 安全团队保持最高优先级处理安全问题，披露政策与发布流程维持原标准
- 🙏 感谢研究人员：诚挚感谢过往通过赏金计划报告漏洞的研究人员，他们的贡献提升了 Node.js 的安全性
- 🔮 未来展望：若获得专项资助将考虑重启计划，鼓励依赖 Node.js 的组织通过 OpenJS 基金会联系赞助事宜

---

### [黑客一号](https://hackerone.com/ibb?type=team)

**原文标题**: [HackerOne](https://hackerone.com/ibb?type=team)

该页面提示用户需要启用浏览器中的 JavaScript 功能才能正常使用 HackerOne 平台。

- 🔧 启用浏览器 JavaScript 以使用 HackerOne
- 🌐 刷新页面后功能将恢复正常

---

### [可执行文件 - 优雅的库打包工具](https://tsdown.dev/options/exe)

**原文标题**: [Executable - The Elegant Bundler for Libraries](https://tsdown.dev/options/exe)

tsdown 的 exe 选项可将 TypeScript/JavaScript 代码打包为独立可执行文件，无需安装 Node.js 即可运行。该功能目前处于实验阶段，要求 Node.js 版本不低于 25.7.0，且不支持 Bun 或 Deno 环境。

- 🚀 **基本用法**：通过命令行 `tsdown src/cli.ts --exe` 或配置文件启用 exe 选项，启用后默认禁用声明文件生成和代码分割，仅支持单入口点。
- ⚙️ **高级配置**：可通过对象形式自定义输出文件名（如 `fileName: 'my-tool'`）并传递 seaConfig 选项（如禁用实验警告、启用代码缓存等）以精细控制打包行为。
- 🌍 **跨平台构建**：安装 `@tsdown/exe` 包后，通过 targets 选项可指定多平台目标（如 Linux x64、macOS ARM64），自动下载对应 Node.js 二进制文件并生成带平台后缀的可执行文件。
- ⚠️ **注意事项**：跨平台构建时需禁用 useCodeCache 和 useSnapshot 以避免兼容性问题；targets 设置会覆盖 seaConfig.executable 选项；macOS 自动进行临时签名，Windows 自动添加 .exe 后缀。
- 📦 **缓存机制**：下载的 Node.js 二进制文件会缓存于系统目录（如 macOS 的 `~/Library/Caches/tsdown/node/`），后续构建直接复用以提升效率。

---

### [tsdown - 优雅的库打包工具](https://tsdown.dev/)

**原文标题**: [tsdown - The Elegant Bundler for Libraries](https://tsdown.dev/)

基于 Oxc 和 Rolldown 技术构建，该工具能够极速生成声明文件，性能卓越。

- 🚀 构建与生成声明文件的速度极快
- ⚡ 由 Oxc 和 Rolldown 提供强大动力支持
- 💨 性能表现令人惊叹

---

### [单可执行应用程序 | Node.js v25.9.0 文档](https://nodejs.org/api/single-executable-applications.html)

**原文标题**: [Single executable applications | Node.js v25.9.0 Documentation](https://nodejs.org/api/single-executable-applications.html)

Node.js 单可执行应用程序功能允许将脚本和资源打包进 Node.js 二进制文件，生成独立的可执行文件，无需目标系统安装 Node.js。该功能支持 CommonJS 和 ES 模块，可通过 `--build-sea` 标志或外部工具（如 postject）创建，并提供了管理内嵌资源、配置启动参数和优化性能（如快照和代码缓存）的 API。

- 📦 **生成单可执行文件**：使用 `--build-sea` 标志和 JSON 配置文件，可将脚本、资源打包并注入 Node.js 二进制文件，生成独立应用。
- 🗂️ **资源管理**：通过配置文件的 `assets` 字段嵌入静态资源（如图片、文本），并在运行时使用 `sea.getAsset()` 等 API 进行访问。
- ⚡ **性能优化**：支持启动快照（`useSnapshot`）和 V8 代码缓存（`useCodeCache`），以加速应用启动，但需注意平台兼容性和使用限制。
- 🛠️ **执行参数配置**：可通过 `execArgv` 预设 Node.js 运行时参数，并利用 `execArgvExtension` 控制环境变量或命令行参数的扩展方式。
- 📝 **模块与 API 支持**：内嵌主脚本可使用 CommonJS 或 ES 模块格式，但文件系统模块加载受限；提供 `sea.isSea()` 等 API 用于检测环境和资源操作。
- 🔧 **创建流程与平台**：生成过程包括准备 Blob 和注入二进制两步；官方支持 Windows、macOS 和主流 Linux 平台，其他平台可通过社区工具实现。

---

### [构建一个基于 QuickJS 的运行时环境 — Andrew Healey](https://healeycodes.com/building-a-runtime-with-quickjs)

**原文标题**: [Building a Runtime with QuickJS — Andrew Healey](https://healeycodes.com/building-a-runtime-with-quickjs)

本文介绍了作者基于 QuickJS 引擎构建一个轻量级 JavaScript 运行时的过程，该运行时包含 console.log、process.uptime()、setTimeout/clearTimeout、同步与异步文件读取等功能，并实现了事件循环和线程池机制。

- 🚀 **JavaScript 引擎与运行时的区别**：引擎（如 V8）负责执行代码，而运行时（如 Node.js）提供完整的运行环境，包括额外 API、事件循环和平台特性。
- 🔧 **自定义运行时构建**：作者从零开始创建运行时，通过 QuickJS 的 API 初始化引擎、上下文，并逐步添加全局对象和宿主函数。
- 📝 **实现 console.log**：通过 C 函数将 JavaScript 参数转换为字符串并输出到标准输出，展示了宿主与引擎的交互方式。
- ⏱️ **添加 process.uptime()**：利用单调时钟记录进程启动时间，通过运行时状态存储和管理宿主数据。
- ⏰ **实现 setTimeout/clearTimeout**：使用排序链表管理定时器，支持回调函数的调度和取消，并处理 JavaScript 值的引用计数。
- 🔄 **构建事件循环**：通过轮询定时器和异步任务，使用 select() 监听唤醒管道，确保回调按顺序执行并处理 Promise 微任务。
- 📂 **同步文件读取**：实现 fs.readFileSync，直接在主线程阻塞读取文件内容并返回 JavaScript 字符串。
- 🧵 **异步文件读取与线程池**：通过工作线程池处理异步 I/O，使用互斥锁和条件变量协调任务队列，并通过管道通知主线程任务完成。
- ⚡ **性能对比**：自定义运行时在启动速度上优于 Node.js，文件读取性能接近，展示了轻量级运行时的潜力。

---

### [GitHub - audiojs/web-audio-api: Web 音频 API 的便携式实现 · GitHub](https://github.com/audiojs/web-audio-api)

**原文标题**: [GitHub - audiojs/web-audio-api: Portable implementation of Web audio API · GitHub](https://github.com/audiojs/web-audio-api)

这是一个用于 Node.js 的便携式 Web Audio API 实现，它允许在服务器端、命令行或 CI 环境中进行音频处理、合成和渲染，无需浏览器环境。

- 🎯 **便携式 API 实现** - 在 Node.js 中实现了完整的 Web Audio API 规范，无需原生依赖。
- 🧪 **全面测试与兼容** - 通过 100% WPT 一致性测试，并支持 Tone.js 等流行音频库。
- 🖥️ **多环境运行** - 支持服务器端音频生成、命令行脚本、CI 环境渲染和离线音频处理。
- 🔊 **内置输出支持** - 通过 `audio-speaker` 提供内置扬声器输出，也支持将 PCM 数据管道传输到外部工具。
- ⚙️ **Node.js 扩展功能** - 提供超出规范的便捷功能，如通过回调注册 AudioWorklet、直接输出到可写流等。
- 📦 **易于集成** - 可通过 npm 安装，并可作为 polyfill 使用，使浏览器音频代码能在 Node.js 中运行。
- 🚀 **高性能架构** - 采用基于拉取的音频图架构，大多数场景下渲染速度快于实时，并计划支持 WASM 内核以加速重型 DSP 任务。
- 🛠️ **丰富示例** - 包含大量示例，涵盖测试信号、音频错觉、合成技术、生成式音乐和 API 演示。

---

### [Web Audio API - Web API | MDN](https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API)

**原文标题**: [Web Audio API - Web APIs | MDN](https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API)

Web Audio API 是一个用于在网页上控制音频的强大系统，支持音频源选择、效果添加、可视化、空间音效等功能，自 2021 年 4 月起广泛兼容各浏览器。

- 🎵 **音频处理基础**：在音频上下文中通过模块化音频节点构建处理图，支持多种音频源和动态效果。
- 🔗 **节点连接与流程**：从音频源（如振荡器、文件或流）出发，经效果节点（如增益、滤波）处理，最终输出到扬声器或耳机。
- ⏱️ **高精度时序控制**：支持低延迟操作，适用于鼓机、音序器等需要精准时序的应用。
- 🌐 **音频空间化**：基于源 - 听者模型实现声像控制和距离衰减，适合 3D 音频场景。
- 👥 **面向开发者与音乐人**：既可用于网站氛围音效或表单反馈，也能构建高级交互式乐器，提供从入门到进阶的教程。
- 🛠️ **丰富接口分类**：涵盖音频图定义、音源、效果滤镜、输出目标、数据分析、声道处理、空间化、JavaScript 音频处理等九大类接口。
- 📚 **学习资源齐全**：包含概念指南、基础与高级教程、示例代码及兼容性说明，帮助用户深入掌握 API。
- ⚠️ **注意过时特性**：已弃用`ScriptProcessorNode`（性能较差），推荐使用`AudioWorklet`在独立线程处理音频。
- 🔗 **扩展与社区**：提供`Tone.js`、`howler.js`等第三方库，并关联 Web 媒体技术指南，方便进一步探索。

---

### [Tone.js](https://tonejs.github.io/)

**原文标题**: [Tone.js](https://tonejs.github.io/)

Tone.js 是一个用于在浏览器中创建交互式音乐的 Web Audio 框架，其架构设计旨在让音乐人和音频开发者都能轻松上手。它提供了类似数字音频工作站的高级功能，如全局传输控制、预置合成器与效果器，同时也包含高性能的底层模块，支持用户自定义合成器、效果器和复杂控制信号。

- 🎵 Tone.js 是一个基于 Web Audio 的浏览器端音乐创作框架，兼顾音乐人友好与开发者灵活
- 📦 支持通过 npm 安装或直接引入 CDN 脚本，快速集成到项目中
- 🎹 提供基础合成器 Tone.Synth，支持音符触发（triggerAttack/triggerRelease）与时间调度
- ⏱️ 抽象化音频时间系统，支持秒数、音符时值（如 "4n"）等多种时间格式
- ▶️ 必须通过用户交互触发 Tone.start() 才能启动音频上下文，遵循浏览器自动播放策略
- 🔁 内置传输控制器（Transport）和循环事件（Tone.Loop），可实现复杂音乐时序编排
- 🎛️ 支持单复音合成器（如 FMSynth/AMSynth）及通过 PolySynth 实现复音合成
- 🔊 支持音频采样播放（Tone.Player）与多采样乐器（Tone.Sampler）
- 🎚️ 提供失真、滤波、延迟等效果器，支持灵活的信号路由与并行处理
- 📶 几乎所有参数都支持音频率信号控制，可实现自动化曲线与精准调度
- ⚙️ 自动创建兼容性优化的 AudioContext，也可自定义音频上下文
- 🧪 拥有完整的测试套件与近 100% 代码覆盖率，开发分支通过 npm @next 发布
- 🌐 性能基于原生 Web Audio 节点，兼容桌面与移动端，并附有性能优化建议

---

### [web-audio-api/examples 位于主分支 · audiojs/web-audio-api · GitHub](https://github.com/audiojs/web-audio-api/tree/master/examples)

**原文标题**: [web-audio-api/examples at master · audiojs/web-audio-api · GitHub](https://github.com/audiojs/web-audio-api/tree/master/examples)

这是一个名为“web-audio-api”的 GitHub 仓库，其中包含一系列使用 Web Audio API 的音频处理示例代码。

- 🎵 包含多种音频合成与处理示例，如加法合成、FM 合成和噪声生成
- 📁 示例文件涵盖从基础音调到高级空间音频的广泛主题
- 🔧 提供实际代码演示，包括节拍器、序列器和音频工作线程等应用
- 🧪 包含特殊效果示例，如双耳节拍、缺失基频和谢泼德音调
- 📊 涉及音频分析与处理技术，如 FFT 和缓冲区渲染

---

### [GitHub - tronghieuit/tiny-tts: 仅含 100 万参数的最小英语 TTS 模型 · GitHub](https://github.com/tronghieuit/tiny-tts)

**原文标题**: [GitHub - tronghieuit/tiny-tts: The Smallest English TTS Model with only 1M parameters · GitHub](https://github.com/tronghieuit/tiny-tts)

TinyTTS 是一个超轻量级的英语文本转语音模型，仅包含约 160 万参数，ONNX 模型大小约 3.4 MB，支持端到端合成，在 CPU 上即可实现实时语音生成。

- 🚀 **超轻量设计** – 仅约 160 万参数，ONNX 模型大小约 3.4 MB，适合边缘设备和嵌入式系统运行。
- ⚡ **高效推理** – 在 CPU 上通过 ONNX 运行时合成速度可达实时约 53 倍，GPU 上预计可达约 325 倍。
- 🔊 **高质量音频** – 支持 44.1 kHz 采样率，输出语音自然清晰，且为端到端模型无需单独声码器。
- 🐍 **多语言支持** – 提供 Python（PyPI）和 Node.js（npm）两种安装方式，均包含完整的 G2P 流程。
- 📊 **性能领先** – 在相同 CPU 环境下对比其他 TTS 引擎，TinyTTS 在参数大小和推理速度上表现最佳。
- 🔧 **灵活使用** – 支持通过 CLI、Python API 和 Node.js API 进行调用，并可调整语速、说话人等参数。
- 📚 **开源项目** – 代码托管于 GitHub，采用 Apache 2.0 许可证，包含训练代码、预训练模型和详细文档。

---

### [使用 tiny-tts 的文本转语音（Node.js ESM 示例）· GitHub](https://gist.github.com/peterc/2cdb2ba30476858b5d2a9a041ddf884c)

**原文标题**: [Text-to-speech with tiny-tts (Node.js ESM example) · GitHub](https://gist.github.com/peterc/2cdb2ba30476858b5d2a9a041ddf884c)

这是一个关于使用 Node.js 的 tiny-tts 库进行文本转语音的代码示例，展示了如何通过 ES 模块导入并生成语音文件。

- 🗣️ 导入 tiny-tts 库并创建实例
- 🔊 调用 speak 方法将文本转换为语音并保存为 WAV 文件
- 🧹 使用 dispose 方法清理资源
- 📁 代码以 ES 模块形式编写，文件扩展名为.mjs
- ⏱️ 示例创建于 2026 年 4 月 9 日，位于 GitHub Gist 平台

---

### [微型 TTS 演示 - 由 backtracking 创建的 Hugging Face 空间](https://huggingface.co/spaces/backtracking/tiny-tts-demo)

**原文标题**: [Tiny Tts Demo - a Hugging Face Space by backtracking](https://huggingface.co/spaces/backtracking/tiny-tts-demo)

清爽感是一种令人愉悦的体验，通常与清新、洁净和活力相关，能带来身心舒畅的感觉。

- 🌊 带来清新与洁净的感受
- 💧 常用于描述水、空气或食物的品质
- 🌿 引发活力与精神振奋
- 😌 促进身心放松与舒适
- 🍃 多与自然元素和简单生活方式关联

---

### [TimescaleDB — 顶尖时序数据库 | 泰格数据](https://www.tigerdata.com/timescaledb?utm_source=cooperpress&utm_medium=referral&utm_campaign=node-weekly-newsletter)

**原文标题**: [TimescaleDB — The #1 Time-Series Database | Tiger Data](https://www.tigerdata.com/timescaledb?utm_source=cooperpress&utm_medium=referral&utm_campaign=node-weekly-newsletter)

TimescaleDB 是一个基于 Postgres 构建的开源时序数据库，专为处理传感器、链上和客户数据而设计，提供实时分析、高效压缩和自动管理功能，适用于初创公司和企业。

- 🚀 高性能时序处理：通过自动分区的超表实现快速数据摄入和可预测查询，支持按时间或 ID 分区
- 💾 智能混合存储：结合行存储（写入快）和列存储（查询快），数据老化时自动转换
- 📉 高效数据压缩：压缩率高达 95%，保持多年历史数据在线并加速分析查询
- 🔄 增量物化视图：持续聚合支持即时仪表板，包含最新变更的实时模式
- ⚙️ 自动化管理：内置作业调度器、可配置保留策略，完整审计列存储和聚合刷新
- 📊 丰富时序函数：约 200 个原生 SQL 函数简化高级时序分析，支持时间加权平均和插值
- ☁️ 企业级云平台：提供弹性云服务，兼容 PostgreSQL，拥有超过 12,000 名开发者社区
- 🌐 行业应用广泛：已成功应用于加密货币、能源遥测、石油天然气等多个领域
- 🤝 强大社区支持：GitHub 获 22K+ 星标，Slack 有 12,000+ 成员，提供 Helm 图表快速部署

---

### [标记文档](https://marked.js.org/)

**原文标题**: [Marked Documentation](https://marked.js.org/)

Marked 是一个高性能、轻量级的 Markdown 编译器，支持多种 Markdown 规范，可在命令行、浏览器和 Node.js 环境中使用，但需注意其输出未经消毒，可能存在安全风险。

- 🚀 **高性能设计**：Marked 为速度而构建，采用低层级的 Markdown 编译方式，避免长时间阻塞或缓存。
- 📦 **轻量且功能全面**：在保持轻量的同时，支持所有主流 Markdown 风格和规范的功能。
- 🌐 **多环境支持**：提供命令行界面（CLI），并可在客户端或服务器端的 JavaScript 项目中运行。
- ⚠️ **安全警告**：Marked 不会对输出的 HTML 进行消毒，处理潜在不安全字符串时需使用如 DOMPurify 等工具过滤 XSS 攻击。
- 🔧 **灵活配置**：支持通过配置文件自定义选项，并允许使用扩展来增强功能。
- 📊 **规范兼容性**：积极支持 Markdown 1.0（100%）、CommonMark 0.31（98%）和 GitHub Flavored Markdown 0.29（97%）等规范。
- 🛠️ **广泛应用**：被多个工具如 zero-md、TeXMe 和 Homebrewery 等采用，用于快速 Markdown 转换和内容渲染。
- 🔒 **安全响应**：项目重视安全性，鼓励通过邮件报告潜在问题，并承诺在 48 小时内初步评估，两周内应用补丁。

---

### [标记演示](https://marked.js.org/demo/)

**原文标题**: [Marked Demo](https://marked.js.org/demo/)

该工具是一个用于演示和测试 Markdown 语法的在线平台，提供实时预览和多种辅助功能。

- 🌐 **Markdown 演示**：展示 CommonMark 和 Daring Fireball 两种主流 Markdown 规范的解析效果
- ⚙️ **交互功能**：包含语法高亮、HTML 源码查看、词法分析数据显示等调试选项
- 🔧 **技术要求**：需要启用 JavaScript 才能正常使用所有功能
- 📍 **版本管理**：支持查看当前使用的解析器版本（示例显示为 master 分支）
- ⚡ **性能监控**：实时显示服务器响应时间统计

---

### [GitHub - markedjs/marked：一款Markdown解析器与编译器，专为速度打造。· GitHub](https://github.com/markedjs/marked)

**原文标题**: [GitHub - markedjs/marked: A markdown parser and compiler. Built for speed. · GitHub](https://github.com/markedjs/marked)

Marked 是一个快速、轻量级的 Markdown 解析器和编译器，支持多种 Markdown 规范，可在浏览器、服务器或命令行中运行，但输出需自行进行 HTML 消毒以确保安全。

- ⚡ 高性能解析器，无缓存或长时间阻塞
- ⚖️ 轻量级且支持多种 Markdown 规范和功能
- 🌐 跨平台运行，兼容浏览器、服务器和命令行界面
- 🚨 输出 HTML 需额外消毒，建议使用 DOMPurify 等库
- 📚 提供详细文档和演示页面，自身文档也由 Marked 渲染
- 📦 支持通过 npm 安装，提供 CLI 和浏览器两种使用方式

---

### [grammY](https://grammy.dev/)

**原文标题**: [grammY](https://grammy.dev/)

grammY 框架让创建 Telegram 机器人变得异常简单，其直观的设计让用户能迅速上手。

- 🤖 使用简便：grammY 框架让创建 Telegram 机器人变得简单直观，即使新手也能快速掌握
- 🚀 上手迅速：框架设计清晰，用户无需复杂学习即可开始构建机器人
- 💡 直观体验：操作逻辑符合常见开发习惯，降低学习门槛

---

### [Telegram Bot API](https://core.telegram.org/bots/api#april-3-2026)

**原文标题**: [Telegram Bot API](https://core.telegram.org/bots/api#april-3-2026)

Telegram Bot API 是一个基于 HTTP 的接口，供开发者创建和管理 Telegram 机器人。它支持多种消息类型、文件传输、内联模式、支付、贴纸、游戏等功能，并可通过 Webhook 或轮询方式接收更新。机器人可以发送文本、媒体、位置、投票等内容，管理聊天成员、设置命令、处理支付，并支持高级功能如业务账户管理、礼物赠送和故事发布。

- 🤖 **机器人管理**：支持创建、配置和管理机器人，包括设置命令、名称、描述和菜单按钮。
- 📡 **更新接收**：提供 `getUpdates` 轮询和 Webhook 两种方式接收消息和事件更新。
- 📨 **消息发送**：可发送文本、照片、音频、视频、文档、贴纸、位置、联系人、投票等多种类型消息。
- 🎮 **内联模式**：支持内联查询，允许用户在聊天中直接与机器人交互并发送富媒体结果。
- 💰 **支付功能**：集成支付系统，支持发票创建、支付处理和 Telegram Stars 余额管理。
- 🎁 **礼物系统**：允许机器人发送礼物和 Telegram Premium 订阅，并管理业务账户的礼物设置。
- 📊 **聊天管理**：提供管理聊天成员、权限、邀请链接、置顶消息、论坛话题等功能。
- 🏷️ **贴纸管理**：支持创建、编辑和管理贴纸集，包括自定义表情符号。
- 🎲 **游戏功能**：允许发送 HTML5 游戏，并管理游戏分数和排行榜。
- 🔐 **业务账户**：支持连接和管理业务账户，包括消息处理、个人资料编辑和故事发布。
- 🔄 **文件传输**：支持通过文件 ID、URL 或多部分表单上传文件，最大可达 50MB。
- 🌐 **本地服务器**：可运行本地 Bot API 服务器以获得更高文件大小限制和自定义 Webhook 设置。

---

### [GitHub - grammyjs/grammY：Telegram 机器人框架。· GitHub](https://github.com/grammyjs/grammY)

**原文标题**: [GitHub - grammyjs/grammY: The Telegram Bot Framework. · GitHub](https://github.com/grammyjs/grammY)

grammY 是一个用于创建 Telegram 机器人的框架，适用于初学者和大型项目，具有易用性、强大功能、最新特性、优秀文档、高效性能和丰富的插件生态系统。

- 🤖 适用于 TypeScript/JavaScript，支持 Node.js 和 Deno 运行环境
- 📚 提供详细文档和 API 参考，便于开发者快速上手
- 🔌 拥有活跃的插件生态系统和友好的社区聊天支持
- 🚀 高效且易于扩展，适合各种规模的机器人项目
- 🌐 支持 Web 框架和数据库的无缝集成
- 📦 提供 JavaScript 捆绑包，兼容浏览器和 Cloudflare Workers
- 👥 拥有多语言社区，包括俄语聊天频道
- ✨ 项目遵循 all-contributors 规范，欢迎各种形式的贡献

---

### [GitHub - lirantal/tokenu：一个类似Unix du 的命令行工具，用于统计文件和目录的令牌使用情况 · GitHub](https://github.com/lirantal/tokenu/)

**原文标题**: [GitHub - lirantal/tokenu: a unix-like du command line tool to count token usage per files and directories · GitHub](https://github.com/lirantal/tokenu/)

tokenu 是一个类似 Unix du 命令的 CLI 工具，用于统计文件和目录的令牌使用量。

- 🚀 **快速启动**：无需安装，可直接通过 npx 运行或全局安装使用
- 📊 **功能丰富**：支持递归统计、人类可读格式、深度限制、JSON 输出等多种选项
- 🔧 **灵活配置**：可指定编码方式（如 o200k_base、cl100k_base）和模型名称（如 gpt-4o）
- 📁 **智能过滤**：支持通配符排除特定文件模式，可显示所有文件或仅目录统计
- 🔄 **实用示例**：提供多种使用场景示例，包括目录统计、汇总显示和 JSON 格式输出
- 👥 **开源协作**：项目遵循 Apache-2.0 许可证，欢迎贡献并提供了详细的贡献指南
- 📈 **项目状态**：当前获得 5 星标，主要使用 TypeScript 开发，由 Liran Tal 维护

---

### [发布 v2.0.0 · sindresorhus/ky · GitHub](https://github.com/sindresorhus/ky/releases/tag/v2.0.0)

**原文标题**: [Release v2.0.0 · sindresorhus/ky · GitHub](https://github.com/sindresorhus/ky/releases/tag/v2.0.0)

Ky 是一个基于 Fetch API 的 HTTP 客户端库，最新发布了 v2.0.0 版本，包含多项重大变更、新增功能和修复。

- 🚨 **重大变更**：要求 Node.js 22 版本，统一了钩子函数的签名，将 `prefixUrl` 重命名为 `prefix`，并允许输入 URL 包含前导斜杠。
- 🆕 **新增功能**：引入了 `totalTimeout` 选项以设置所有重试的总超时时间，新增 `baseUrl` 选项用于标准 URL 解析，并添加了 `init` 钩子。
- 🐛 **修复与改进**：修复了 `beforeRequest` 钩子在返回 `Request` 对象时被跳过的问题，改进了错误处理，使 `beforeError` 钩子能接收所有错误类型。
- 🔄 **行为调整**：`searchParams` 现在会与输入 URL 中的现有查询参数合并，而不是替换它们；`.json()` 方法在响应体为空或状态码为 204 时会抛出错误。
- 📦 **错误处理优化**：`HTTPError` 现在包含 `data` 属性，其中预解析了响应体，解决了资源泄漏问题，并使错误详情可同步获取。
- 📝 **迁移指南**：提供了从 v1 升级到 v2 的详细指南，包括钩子签名调整、`prefix` 重命名、错误处理更新等关键步骤。

---

### [发布 v20.0.0 · raineorshine/npm-check-updates · GitHub](https://github.com/raineorshine/npm-check-updates/releases/tag/v20.0.0)

**原文标题**: [Release v20.0.0 · raineorshine/npm-check-updates · GitHub](https://github.com/raineorshine/npm-check-updates/releases/tag/v20.0.0)

npm-check-updates 发布了 v20.0.0 版本，主要引入了自动冷却功能，并包含多项依赖更新和安全修复。

- 🚀 **自动冷却功能**：现在会根据 npm、yarn 或 pnpm 的配置自动应用冷却选项，排除未达到最小发布年龄的更新。
- 🔧 **依赖更新**：升级了 strip-ansi、lodash、@typescript-eslint/eslint-plugin 等多个依赖包。
- 🛡️ **安全修复**：解决了代码扫描警报中的字符串转义问题，并修复了其他潜在漏洞。
- 👋 **新贡献者**：欢迎 @onemen 和 @Copilot 首次贡献代码。
- 📈 **社区反应**：获得了 4 个点赞、1 个欢呼和 2 个爱心等积极反馈。

---

### [ESLint v10.2.0 发布 - ESLint - 可插拔的 JavaScript 代码检查工具](https://eslint.org/blog/2026/04/eslint-v10.2.0-released/)

**原文标题**: [ESLint v10.2.0 released - ESLint - Pluggable JavaScript Linter](https://eslint.org/blog/2026/04/eslint-v10.2.0-released/)

ESLint v10.2.0 是一个次要版本更新，引入了语言感知规则支持和 Temporal 全局对象识别，同时修复了若干错误并更新了文档。

- 🚀 新增语言感知规则支持，通过 `meta.languages` 属性允许规则作者声明支持的语言
- ⏳ 识别 Temporal 为内置全局对象，相关规则如 `no-undef` 和 `no-obj-calls` 已相应更新
- 🐛 修复了若干错误，包括更新了首方依赖项
- 📚 文档进行了多项更新，包括配置对象中新增 `language` 字段说明
- 🔧 包含多项内部优化和测试更新，如重构代码、更新依赖项和添加单元测试

---

### [发布 v7.0.0 · vadimdemedes/ink · GitHub](https://github.com/vadimdemedes/ink/releases/tag/v7.0.0)

**原文标题**: [Release v7.0.0 · vadimdemedes/ink · GitHub](https://github.com/vadimdemedes/ink/releases/tag/v7.0.0)

Ink 7.0.0 版本发布，这是一个重大更新，引入了多项新功能、改进和破坏性变更，主要针对 Node.js 22 和 React 19.2+ 的兼容性进行了升级。

- 🚨 **破坏性变更**：要求 Node.js 22 和 React 19.2+，并修复了 Backspace 键和 Escape 键的按键识别问题。
- 🆕 **新增功能**：引入了多个新 Hook，如 `usePaste`、`useWindowSize`、`useBoxMetrics` 和 `useAnimation`，增强了交互和布局能力。
- ⚙️ **渲染选项**：为 `render()` 新增了 `alternateScreen` 和 `interactive` 选项，提升终端应用的灵活性和用户体验。
- 📦 **组件增强**：为 `<Box>` 和 `<Text>` 组件添加了新的布局和样式属性，如边框背景色、硬换行和最大尺寸限制。
- 🐛 **问题修复**：解决了增量渲染、按键处理崩溃、CJK 文本截断和宽字符分割等多个已知问题。
- 📖 **迁移指南**：提供了详细的代码示例，帮助开发者从旧版本平滑迁移到新版本。

---

### [GitHub - jshttp/content-disposition: 创建与解析 HTTP Content-Disposition 头部 · GitHub](https://github.com/jshttp/content-disposition)

**原文标题**: [GitHub - jshttp/content-disposition: Create and parse HTTP Content-Disposition header · GitHub](https://github.com/jshttp/content-disposition)

这是一个用于创建和解析 HTTP Content-Disposition 头部的 Node.js 库，支持设置文件下载时的文件名和类型，并处理 Unicode 和 ISO-8859-1 编码的兼容性问题。

- 📦 提供创建和解析 Content-Disposition 头部的功能，便于控制文件下载行为
- ⚙️ 支持设置文件名和选项，如回退机制和处置类型（默认为附件）
- 🔤 自动处理 Unicode 文件名编码，确保跨客户端兼容性
- 📄 包含完整 API 文档、使用示例和测试方法
- 🔗 遵循相关 HTTP 标准（RFC 2616、5987、6266），代码开源且采用 MIT 许可

---

### [GitHub - alfateam/orange-orm：适用于Node和TypeScript的终极ORM · GitHub](https://github.com/alfateam/orange-orm)

**原文标题**: [GitHub - alfateam/orange-orm: The ultimate ORM for Node and Typescript · GitHub](https://github.com/alfateam/orange-orm)

Orange ORM 是一个面向 Node.js、Bun 和 Deno 的终极对象关系映射器，提供与多种流行数据库的无缝集成。它支持 TypeScript 和 JavaScript（包括 CommonJS 和 ECMAScript），具有丰富的查询模型、Active Record 模式、无需代码生成、可在浏览器中安全使用等关键特性，并支持包括 Postgres、MySQL、SQLite、MS SQL 等在内的多种数据库和运行时。

- 🚀 **核心特性**：提供强大的查询模型、Active Record 模式、无需代码生成、完整的 TypeScript/JavaScript 支持，并可在浏览器中安全使用。
- 🗄️ **数据库支持**：兼容 Postgres、MySQL、SQLite、MS SQL、MariaDB、Oracle、SAP ASE、Cloudflare D1 等多种数据库，支持 Node、Deno、Bun、Cloudflare 和 Web 运行时。
- 🔌 **连接与适配**：提供各种数据库的连接方式，包括 SQLite、MySQL、PostgreSQL 等，并支持通过 Express 或 Hono 插件在浏览器中安全使用。
- 📊 **数据操作**：支持插入、更新、删除、查询等完整的数据操作，包括事务处理、并发控制（乐观锁、覆盖、跳过冲突）和批量操作。
- 🛡️ **安全与过滤**：提供行级安全、基础过滤器、拦截器等功能，确保数据访问的安全性和隔离性，支持复杂的查询过滤和关系过滤。
- 🔧 **高级功能**：支持复合主键、列鉴别器、公式鉴别器、自定义验证、默认值、枚举、JSON 序列化排除敏感数据、日志记录和原始 SQL 查询。
- 📈 **聚合与统计**：支持计数、求和、最小值、最大值、平均值等聚合操作，可跨行或按行进行数据统计。
- 🚫 **非目标领域**：明确不处理数据库迁移、NoSQL 数据库或 GraphQL 集成，专注于关系型数据库的 ORM 解决方案。

---

### [GitHub - axios/axios: 基于 Promise 的浏览器和 Node.js HTTP 客户端 · GitHub](https://github.com/axios/axios)

**原文标题**: [GitHub - axios/axios: Promise based HTTP client for the browser and node.js · GitHub](https://github.com/axios/axios)

Axios 是一个基于 Promise 的 HTTP 客户端，适用于浏览器和 Node.js 环境，提供丰富的功能如拦截器、请求取消、自动 JSON 处理等，并支持现代 JavaScript 特性。

- 🌐 **跨平台支持**：可在浏览器和 Node.js 中发起 HTTP 请求，兼容主流浏览器。
- 🔧 **功能丰富**：支持拦截器、请求取消、自动数据转换、XSRF 防护等高级特性。
- 📦 **安装灵活**：可通过 npm、yarn、CDN 等多种方式安装，并支持 ES6 模块和 CommonJS。
- ⚙️ **配置灵活**：允许全局配置、创建自定义实例，并支持请求和响应的深度定制。
- 🛡️ **错误处理**：提供详细的错误分类和处理机制，便于调试和异常管理。
- 🔄 **数据格式支持**：自动处理 JSON、FormData 和 URL 编码数据，简化开发流程。
- 🚀 **现代特性**：支持 HTTP/2、Fetch 适配器、进度捕获和速率限制等新功能。
- 📚 **社区活跃**：拥有完善的文档、TypeScript 支持和活跃的社区贡献。

---

### [GitHub - weyoss/redis-smq: 一个用于 Node.js 的简单高性能 Redis 消息队列。· GitHub](https://github.com/weyoss/redis-smq)

**原文标题**: [GitHub - weyoss/redis-smq: A simple high-performance Redis message queue for Node.js. · GitHub](https://github.com/weyoss/redis-smq)

RedisSMQ 是一个基于 Redis 的高性能 Node.js 消息队列系统，设计简洁且易于扩展，支持多种队列类型、灵活的路由、实时事件处理以及丰富的管理功能。

- 📬 **可靠的消息传递**：支持消息重试，确保消息可靠送达。
- 📊 **多种队列类型**：提供 FIFO、LIFO 和优先级队列，满足不同场景需求。
- 🔀 **灵活的路由机制**：支持直接、主题和扇出交换，以及直接队列发布。
- 👥 **发布/订阅与点对点模型**：内置消费者组，支持多种消息传递模式。
- 🚦 **队列级速率限制**：可对单个队列设置速率限制，控制消息处理速度。
- ⏰ **内置调度器**：支持延迟消息、CRON 任务和重复任务调度。
- 🔒 **队列状态管理**：提供暂停、停止、恢复和审计功能，便于队列运维。
- ⏱️ **消息生存时间与消费超时**：可设置消息 TTL 和消费超时，避免消息堆积。
- 🚀 **高性能设计**：基于原子 Lua 脚本实现，支持高吞吐量处理。
- 📦 **批量确认与取消确认**：批量操作减少 99% 的 Redis 调用，提升效率。
- 🧵 **工作线程支持**：为 CPU 密集型任务提供工作线程处理能力。
- 🔄 **多队列生产与消费**：支持多队列操作和复用连接，优化资源使用。
- 📡 **事件总线**：提供实时内部事件通知，便于系统监控与集成。
- 🌐 **REST API 与 Web UI**：内置 OpenAPI 和 Swagger 文档，提供 Web 管理界面。
- 🎯 **进程级 API**：支持单次初始化、工厂方法和统一关闭，简化集成。
- 🔄 **双模式支持**：同时支持回调函数和 Promise 接口，编码更灵活。
- 📦 **模块兼容性**：支持 ESM 和 CJS 模块系统，适应不同项目结构。
- 📖 **TypeScript 优先**：提供完整的 TypeScript 类型定义和丰富文档。

---

### [GitHub - jens-maus/node-ical: 功能丰富的 Node.js iCalendar/ICS (RFC 5545) 解析器 · GitHub](https://github.com/jens-maus/node-ical)

**原文标题**: [GitHub - jens-maus/node-ical: Feature-rich iCalendar/ICS (RFC 5545) parser for Node.js · GitHub](https://github.com/jens-maus/node-ical)

node-ical 是一个功能丰富的 Node.js iCalendar/ICS 解析库，支持同步和异步 API，提供强大的重复规则扩展、时区感知日期处理以及异常日期和重复覆盖功能。

- 📦 **功能丰富的解析器**：支持 RFC 5545 标准的 iCalendar/ICS 文件解析，包含重复规则（RRULE）扩展、时区处理、异常日期（EXDATE）和重复覆盖（RECURRENCE-ID）。
- 🔄 **灵活的 API**：提供同步（sync）、异步（async）和自动检测（autodetect）三种 API 模式，支持从字符串、本地文件和远程 URL 解析日历数据。
- 🛠️ **易于安装与使用**：通过 npm 安装，提供清晰的代码示例，支持现代 JavaScript 特性如 async/await 和回调函数。
- 🌐 **时区与重复处理**：正确处理时区感知的日期，支持复杂时区场景和夏令时转换，确保重复事件的准确性。
- 📅 **异常与覆盖管理**：通过双键访问模式处理异常日期和重复覆盖，既保持向后兼容性，又符合 RFC 5545 标准。
- ⚙️ **扩展与工具函数**：提供 `expandRecurringEvent()` 函数扩展重复事件，支持日期范围筛选、包含覆盖和排除异常日期等选项。
- 📊 **类型与元数据支持**：包含完整的 TypeScript 类型定义，支持访问日历级元数据（如日历名称），并保留原始时区信息。
- 🔧 **底层实现**：内置 Windows/IANA 时区映射，通过生成的 `windowsZones.json` 文件确保时区解析的准确性和兼容性。

---

### [发布 · nodejs/undici · GitHub](https://github.com/nodejs/undici/releases)

**原文标题**: [Releases · nodejs/undici · GitHub](https://github.com/nodejs/undici/releases)

这是一个关于 Node.js 官方 HTTP 客户端库 Undici 在 GitHub 上的发布页面，主要展示了最近的版本更新记录。

- 🚀 **v8.0.2 发布**：修复了 WebSocket 在 H2 CONNECT 不可用时的降级问题，并重新启用了共享内置 CI 测试。
- 🔧 **v8.0.1 更新**：移除了遗留处理程序包装器，默认启用 HTTP/2，修复了缓存和 Blob 支持等问题。
- 🎉 **v8.0.0 重大版本**：包含多项破坏性变更，如移除旧版处理程序、默认启用 HTTP/2 等，标志着主要版本升级。
- 🐛 **v7.24.7 维护版本**：修复了类型定义、IPv6 测试和多值请求头处理等问题，并有新贡献者加入。
- 📚 **v7.24.6 改进**：增强了 WebSocket 对 H2 的支持，改进了代理环境变量处理和缓存授权验证。
- ⚙️ **v7.24.5 优化**：专注于表单数据测试和缓存响应处理，新增了贡献者。
- 🔍 **早期版本修复**：包括 v7.24.4 至 v6.24.1 的一系列小版本更新，主要修复路径逻辑、H2 错误和依赖问题。

---

### [GitHub - pnpm/pnpm：快速、节省磁盘空间的包管理器 · GitHub](https://github.com/pnpm/pnpm)

**原文标题**: [GitHub - pnpm/pnpm: Fast, disk space efficient package manager · GitHub](https://github.com/pnpm/pnpm)

pnpm 是一个快速且节省磁盘空间的包管理器，通过内容寻址存储和硬链接技术优化依赖安装，适用于单仓库和各类项目环境。

- 🚀 **快速高效**：安装速度比 npm 和 Yarn 快达 2 倍，适用于依赖众多的项目
- 💾 **节省存储**：采用内容寻址存储，相同依赖文件只保存一份，通过硬链接减少磁盘占用
- 📦 **严格依赖**：每个包只能访问其 package.json 中明确声明的依赖，避免隐式依赖问题
- 🔒 **确定性安装**：使用 pnpm-lock.yaml 锁文件确保安装结果的一致性
- 🌍 **跨平台支持**：完美兼容 Windows、Linux 和 macOS 操作系统
- 🏢 **单仓库友好**：特别适合大型单仓库项目，已被微软等团队用于生产环境
- 📚 **成熟稳定**：自 2016 年起被各种规模的团队广泛使用，经过实战检验
- ⚙️ **额外功能**：内置 Node.js 版本管理功能（pnpm env use），提供完整的包管理解决方案

---

### [将产品事件路由至 HubSpot、Salesforce、Slack 等平台 | Meshes](https://meshes.io/go/start?utm_source=node_weekly&utm_medium=referral&utm_campaign=cls_20260409)

**原文标题**: [Route Product Events to HubSpot, Salesforce, Slack & More | Meshes](https://meshes.io/go/start?utm_source=node_weekly&utm_medium=referral&utm_campaign=cls_20260409)

Meshes 是一个简化产品事件集成管理的平台，通过单一 API 调用将用户活动数据自动路由至多个第三方工具（如 HubSpot、Salesforce、Slack 等），无需为每个集成编写和维护代码。平台提供预置连接器、自动重试机制和灵活扩展的定价方案，帮助 SaaS 企业高效处理客户数据同步。

- 🚀 **单一 API 集成**：只需一次 API 调用，即可将产品事件自动分发至 HubSpot、Salesforce、Slack 等多个工具，无需为每个目标编写独立集成代码。
- 🔄 **自动重试与容错**：内置指数退避重试机制，确保事件可靠送达，开发者无需手动处理失败逻辑。
- 🌐 **多路同步分发**：一个事件可同时触发多个操作（如用户注册时更新 CRM、发送邮件并通知 Slack），实现高效数据流转。
- ⚙️ **即用型连接器**：提供 HubSpot、Salesforce 等预配置集成模块，几分钟即可完成设置，替代数百行自定义代码。
- 💰 **透明分级定价**：提供免费开发版（100 事件/月）到企业定制套餐，无时间限制，支持按需升级或取消。

---

### [申请 Gauntlet AI - 精英 AI 工程研究员计划](https://gauntletai.com/apply?utm_source=newsletter&utm_medium=paid&utm_campaign=node_weekly&utm_content=april_9)

**原文标题**: [Apply to Gauntlet AI - Elite AI Engineering Fellowship Program](https://gauntletai.com/apply?utm_source=newsletter&utm_medium=paid&utm_campaign=node_weekly&utm_content=april_9)

这是一个为期十周的强化 AI 工程训练营，旨在通过高强度、全时投入的实践项目，将参与者从 AI 爱好者转变为能构建生产级 AI 系统的专业人才。项目全程免费，由招聘合作伙伴承担费用，并提供前沿模型访问和实时招聘机会。

- 🚀 **高强度执行**：十周全时沉浸式学习，无捷径，通过每周交付项目强制提升 AI 工程能力。
- 🏢 **混合式学习**：前 3 周远程建立基础，后 7 周在奥斯汀线下集中，通过近距离协作与压力环境重塑工作方式。
- 💼 **就业直通**：招聘方实时观察学员项目表现，毕业生起薪达 20 万至 95 万美元，确保获得高薪 AI 工程职位。
- 🛠️ **前沿技术栈**：涵盖 AI 优先开发、RAG、智能体系统、多模态 AI、强化学习等，每周项目复杂度递增。
- 📅 **结构化课程**：分两阶段，从基础工作流到企业级系统构建，最终完成可部署的 AI 系统项目。
- 🎯 **严格录取**：面向有生产级软件开发经验的工程师，分“Gauntlet Prime”（企业方向）和“Gauntlet for America”（政府方向）两种路径。
- ⏳ **滚动招生**：多个季度班次开放申请，强调尽早行动，席位先到先得。

---

### [JavaScript 必知要点（2026 版）—— Frontend Masters 博客](https://frontendmasters.com/blog/what-to-know-in-javascript-2026-edition/)

**原文标题**: [What To Know in JavaScript (2026 Edition) – Frontend Masters Blog](https://frontendmasters.com/blog/what-to-know-in-javascript-2026-edition/)

本文概述了 JavaScript 在 2026 年的关键发展，涵盖语言新特性、框架生态、运行时、构建工具及行业趋势。

- 🆕 ECMAScript 2025 引入了迭代器助手、集合方法、正则表达式转义、Promise.try() 和导入属性等新特性，提升开发效率和性能。
- 📅 ECMAScript 2026 预计将带来 Temporal API（改进日期时间处理）、显式资源管理（using 关键字）、Array.fromAsync 和错误检查增强等功能。
- ⚛️ React 19 重点包括服务器组件、React 编译器和服务器动作，而 Vue 和 Svelte 分别聚焦性能优化（如 Vapor 模式）和细粒度响应式（Runes API）。
- 🖥️ JavaScript 运行时中，Node.js 原生支持 TypeScript，Bun 以速度见长，Deno 强调安全性，三者竞争推动生态进步。
- 🛠️ 构建工具方面，Vite 成为主流，Turbopack 在 Next.js 中提升打包速度，webpack 计划简化配置，TypeScript v7 将带来显著性能提升。
- 🤖 AI 在编程中广泛应用，测试工具如 Vitest 和 Playwright 流行，元框架（如 Next.js、Astro）持续演进，但 npm 安全事件频发需警惕。
- 🧠 学习核心技能和架构思维比追逐工具更重要，Frontend Masters 等平台提供系统学习路径。

---

### [Reddit - 请等待验证](https://www.reddit.com/r/node/comments/1sapgun/psa_npm_package_using_postinstall_to_inject/)

**原文标题**: [Reddit - Please wait for verification](https://www.reddit.com/r/node/comments/1sapgun/psa_npm_package_using_postinstall_to_inject/)

本文介绍了人工智能在医疗领域的应用现状与前景，重点探讨了其在疾病诊断、药物研发和个性化治疗方面的突破性进展，同时简要提及了相关的伦理挑战。

- 🏥 AI 辅助诊断系统能通过分析医学影像快速识别病灶，提升早期癌症等疾病的检出率
- 🔬 机器学习加速新药研发流程，大幅缩短化合物筛选与临床试验周期
- 📊 基于患者数据的个性化治疗方案正成为慢性病管理的新趋势
- ⚖️ 医疗 AI 面临数据隐私、算法透明度及责任界定等伦理监管问题

---

### [NPM 忽略脚本最佳实践：作为恶意软件包的安全缓解措施](https://www.nodejs-security.com/blog/npm-ignore-scripts-best-practices-as-security-mitigation-for-malicious-packages)

**原文标题**: [NPM Ignore Scripts Best Practices as Security Mitigation for Malicious Packages](https://www.nodejs-security.com/blog/npm-ignore-scripts-best-practices-as-security-mitigation-for-malicious-packages)

npm 包管理器允许第三方依赖在安装过程中执行任意命令，这带来了供应链安全风险，恶意包可能通过 postinstall 等生命周期脚本窃取敏感信息或破坏系统。为缓解此风险，建议默认启用 ignore-scripts 配置以阻止脚本执行，仅在必要时为受信任的包临时禁用。

- 🛡️ npm 包的生命周期脚本（如 postinstall）允许依赖包在安装时执行任意命令，成为恶意包攻击的常见途径
- ⚠️ 恶意 postinstall 脚本曾导致真实安全事件，如 eslint-scope 和 crossenv 包窃取用户凭据与环境变量
- 🚫 使用`npm install --ignore-scripts`或在.npmrc 中设置`ignore-scripts=true`可全局禁用脚本执行
- ⚖️ 启用 ignore-scripts 可能影响依赖原生编译的包（如 bcrypt），建议默认启用并仅对受信任包例外放行
- 📊 研究表明仅约 2.2% 的 npm 包使用安装脚本，启用 ignore-scripts 对大多数项目无影响
- 🔍 可通过`@lavamoat/preinstall-always-fail`测试项目是否已正确配置脚本禁用
- 🏗️ 在 CI/CD 流水线中强制启用 ignore-scripts，并使用 npq 等工具自动检测带脚本的包

---

### [缓解供应链攻击 | pnpm](https://pnpm.io/supply-chain-security)

**原文标题**: [Mitigating supply chain attacks | pnpm](https://pnpm.io/supply-chain-security)

本文介绍了如何通过 pnpm 工具来缓解供应链攻击的风险，包括禁用依赖中的高风险脚本、限制非标准依赖来源、延迟依赖更新、实施信任策略以及使用锁文件等措施，以增强项目安全性。

- 🛡️ 禁用高风险后安装脚本：pnpm v10 默认阻止依赖中的`postinstall`脚本自动执行，建议仅通过`allowBuilds`明确允许受信任的依赖运行构建脚本，避免安装恶意版本时自动执行有害代码。
- 🌐 阻止非常规传递依赖：通过设置`blockExoticSubdeps`为`true`，确保所有传递依赖都来自可信的注册源（如 npm），防止通过 git 仓库或直接压缩包 URL 引入不安全依赖。
- ⏳ 延迟依赖更新：利用`minimumReleaseAge`设置（例如 1440 分钟即 24 小时），在新版本发布后等待一段时间再安装，以利用恶意软件通常被快速检测的窗口期，降低安装受损包的风险。
- 🔒 实施信任策略：使用`trustPolicy`设置（如`no-downgrade`）防止安装信任等级降低的包版本，并结合`trustPolicyExclude`和`trustPolicyIgnoreAfter`灵活管理例外情况，确保供应链可信度。
- 📦 使用锁文件：始终通过锁文件（如`pnpm-lock.yaml`）锁定依赖版本，并将其提交到代码仓库，避免意外更新引入不安全依赖，保持依赖树的一致性。

---

### [JSHeroes 2026 | 社区组织的 JS 大会](https://jsheroes.io/)

**原文标题**: [JSHeroes 2026 | Community Organized JS Conference](https://jsheroes.io/)

JSHeroes 2026 是一场在罗马尼亚克卢日 - 纳波卡举办的为期两天的社区组织 JavaScript 与前端技术非营利会议，旨在探讨未来技术趋势、工具与实践，并关注开发者成长与行业人文关怀。

- 🧭 **Phil Hawksworth**：Deno 开发者关系负责人，将回顾 JavaScript 30 年历程并展望未来。
- 🔍 **Misha Korolev**：开发者体验工程师，分享通过逆向工程 JavaScript 提升调试与理解能力的技巧。
- 🛠️ **Daniel Roe**：Nuxt 团队负责人，探讨如何通过逆向设计提升开发者体验与 API 可维护性。
- 🧹 **Dominik Dorfmeister**：Sentry 前端工程师，介绍使用 Knip 工具检测并移除前端死代码的实践。
- ♿ **Craig Abbott**：TetraLogical 首席无障碍专家，讨论 AI 在无障碍领域的应用与局限性。
- 🎨 **Cassondra Roberts**：设计系统架构顾问，解析 Web 组件样式化的挑战与解决方案。
- 🚀 **Cyd Stumpel**：创意开发者，探讨如何用现代 CSS 替代 JavaScript 实现动画与过渡效果。
- ⚡ **Ryan Townsend**：Cloudflare 首席产品经理，分享利用 Web 平台特性实现超越 React 的极速页面导航。
- 📊 **Faris Aziz**：Smallpdf 高级软件工程师，讲解在恶劣网络条件下优化数据获取与用户体验的策略。
- 🧠 **Siddharth Dayalwal**：Storyblok 开发者社区专家，分析现代 Web 系统复杂性导致的认知负荷与团队倦怠。
- 🔬 **Richard Gross**：MaibornWolff 软件考古负责人，介绍通过法证技术可视化前端代码质量与架构。
- 🤹 **Zbyszek Tenerowicz**：meet.js 社区成员，分享 25 年来探索 JavaScript 奇特用法的经验与乐趣。
- 🌐 **Suz Hinton**：独立开发者，探讨前端开发中的数字保存与赛博朋克主题。
- ⚙️ **Bogdan Zaharia**：Hootsuite TypeScript 开发者，介绍通过“托管副作用”管理代码复杂性的函数式编程概念。
- 🏨 **会议场地**：克卢日 - 纳波卡 Grand Hotel Italia 五星级酒店，提供无障碍设施与多样化餐饮选择。
- ❤️ **社区精神**：由志愿者团队组织，秉承开源透明原则，旨在促进知识分享与社区互助。
- 👥 **组织团队**：包括内容策划、运营管理、视觉设计、活动协调等多领域志愿者共同协作。
- 🔮 **未来展望**：议题涵盖工程架构、工具框架、AI 协作、技能发展等，全面关注行业演进与人文价值。

---

### [移动铁路前端脱离 Next.js](https://blog.railway.com/p/moving-railways-frontend-off-nextjs)

**原文标题**: [Moving Railway's Frontend Off Next.js](https://blog.railway.com/p/moving-railways-frontend-off-nextjs)

Railway 已将其前端从 Next.js 迁移至 Vite + TanStack Router，以提升开发效率和构建速度，同时保持零停机部署。

- 🚀 **构建速度大幅提升**：前端构建时间从超过 10 分钟缩短至不到 2 分钟，显著加快迭代速度。
- 🔧 **框架更贴合实际需求**：Next.js 的服务器优先模式与 Railway 高度客户端驱动的应用不匹配，TanStack Start 提供了明确的客户端优先开发体验。
- 🛠️ **路由和布局优化**：TanStack Router 提供类型安全的路由和一流的路由布局，解决了 Next.js Pages Router 中布局共享的繁琐问题。
- ⚡ **开发体验改善**：Vite 带来即时热模块替换和近乎零启动时间的开发循环，提升开发效率。
- 🌐 **边缘缓存与性能优化**：通过 Fastly 实现边缘缓存和图像优化，动态页面按需使用增量静态再生，提升加载速度和用户体验。
- 📦 **简化依赖和代码**：迁移过程中用原生浏览器 API 替代 Next.js 特定功能，减少了依赖并让代码更清晰。
- 🔄 **无缝迁移与部署**：通过两个拉取请求完成迁移，无停机时间，Railway 的基础设施支持平滑部署和预览。

---

### [GitHub - dmop/puru: 一个适用于 JavaScript 的线程池，采用 Go 风格的并发原语。可在 Node.js 和 Bun 上运行。· GitHub](https://github.com/dmop/puru)

**原文标题**: [GitHub - dmop/puru: A thread pool for JavaScript with Go-style concurrency primitives. Works on Node.js and Bun. · GitHub](https://github.com/dmop/puru)

puru 是一个用于 JavaScript 的 Go 风格并发库，它通过零依赖的线程池实现 CPU 密集型或 I/O 密集型任务的异步执行，无需单独的 worker 文件或繁琐的配置。

- 🚀 **无依赖的并发库**：提供 Go 风格的并发原语，如通道、WaitGroup、ErrGroup 和 select，无需额外依赖。
- 🧵 **简化多线程编程**：通过 `spawn()` 和 `task()` 函数轻松在专用线程中执行任务，无需手动管理 worker 线程或消息传递。
- ⚡ **显著性能提升**：在 CPU 密集型任务（如素数计算）中可实现高达 4.4 倍的加速，异步任务处理速度提升 73 倍。
- 🔧 **灵活的并发模式**：支持专用线程处理 CPU 密集型任务，以及共享事件循环处理异步 I/O 任务。
- 📦 **内置协调工具**：提供通道、互斥锁、定时器等同步机制，适用于生产者 - 消费者管道和并行批处理场景。
- 🚫 **使用限制**：`spawn()` 函数不能捕获外部变量，通道值必须可结构化克隆，任务参数需可 JSON 序列化。
- 🌐 **跨运行时支持**：完全支持 Node.js 和 Bun，Deno 支持计划中。
- 📚 **丰富的文档和示例**：包含 API 参考、性能基准、生产用例和 AI 助手指南，便于快速上手和集成。

---

