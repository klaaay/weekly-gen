### [Node周刊第619期：2026年4月9日](https://nodeweekly.com/issues/619)

**原文标题**: [Node Weekly Issue 619: April 9, 2026](https://nodeweekly.com/issues/619)

Node Weekly 第619期（2026年4月9日）主要报道了Node.js生态中的安全事件、工具更新、技术文章及行业动态，涵盖供应链攻击分析、新工具发布、会议信息等。

- ⚠️ **Axios供应链攻击事件分析**：Axios团队详细复盘了近期因恶意依赖导致的供应链攻击，涉及精心策划的社会工程手段，同时提醒npm包维护者警惕类似攻击。
- 🗣️ **Node.js安全漏洞赏金计划暂停**：由于互联网漏洞赏金计划（IBB）因AI辅助环境调整而暂停资助，Node.js项目的安全漏洞赏金计划随之暂停，但仍可提交漏洞报告（无奖金）。
- 🛠️ **工具更新与发布**：包括tsdown支持生成Node单可执行文件、web-audio-api在Node中实现完整Web Audio API、TinyTTS提供轻量级文本转语音、以及Axios、ESLint、Ink等流行库的重大版本更新。
- 📅 **技术会议与活动**：免费虚拟会议POSETTE: An Event for Postgres 2026将于6月16-18日举行；JSHeroes会议将于5月14-15日在罗马尼亚回归。
- 🔍 **生态动态与文章**：Google提出JavaScript高级IR（JSIR）；Microsoft终止Azure SDK对Node 20.x的支持；开发者分享从Next.js迁移至Vite和TanStack Router的经验；新工具tokenu用于统计代码令牌数量。
- 📢 **安全提醒与最佳实践**：社会工程攻击持续针对Node.js核心维护者；建议忽略npm包的postinstall脚本以降低风险（pnpm v10+已默认禁用）。

---

### [事后分析：axios npm 供应链安全事件 · Issue #10636 · axios/axios · GitHub](https://github.com/axios/axios/issues/10636)

**原文标题**: [Post Mortem: axios npm supply chain compromise · Issue #10636 · axios/axios · GitHub](https://github.com/axios/axios/issues/10636)

2026年3月31日，axios的两个恶意版本（1.14.1和0.30.4）通过被入侵的维护者账户发布到npm仓库，其中注入了包含远程访问木马的依赖包plain-crypto-js@4.2.1，影响macOS、Windows和Linux系统。恶意版本在约3小时后被移除，受影响用户需立即检查并采取补救措施，包括降级版本、删除恶意依赖、轮换所有密钥凭证等。项目团队已启动全面安全加固，包括重置设备凭证、采用不可变发布流程等，以防止类似事件再次发生。

- 🚨 **事件概述**：2026年3月31日，axios的1.14.1和0.30.4两个恶意版本通过被入侵的维护者npm账户发布，持续约3小时。
- 🦠 **攻击方式**：恶意版本注入依赖`plain-crypto-js@4.2.1`，在macOS、Windows和Linux系统上安装远程访问木马。
- 🔍 **影响检测**：用户需检查lockfile中是否包含恶意版本或依赖，并排查网络连接记录中是否有异常域名或IP。
- 🛡️ **补救措施**：立即降级至安全版本（如axios@1.14.0）、删除恶意依赖、轮换受影响机器上的所有密钥凭证。
- 🕵️ **攻击溯源**：攻击者通过针对性的社会工程学和远程访问木马入侵维护者个人电脑，获取npm账户权限后发布恶意包。
- 📅 **时间线**：攻击始于约两周前的社会工程活动，恶意包在3月31日00:21 UTC发布，社区在约一小时后发现并报告，03:15 UTC被移除。
- 🔧 **安全改进**：项目将重置所有设备凭证、采用不可变发布设置、实施OIDC流程发布，并全面升级安全实践。
- 👥 **致谢与响应**：感谢社区成员和npm安全团队的快速响应，恶意版本已从npm移除，事件得到初步解决。

---

### [axios在npm上遭入侵——恶意版本投放远程访问木马——StepSecurity](https://www.stepsecurity.io/blog/axios-compromised-on-npm-malicious-versions-drop-remote-access-trojan)

**原文标题**: [axios Compromised on npm - Malicious Versions Drop Remote Access Trojan - StepSecurity](https://www.stepsecurity.io/blog/axios-compromised-on-npm-malicious-versions-drop-remote-access-trojan)

2026年3月30日，StepSecurity发现npm上发布的两个恶意axios版本（1.14.1和0.30.4），这些版本通过被劫持的维护者账户发布，注入了一个隐藏依赖`plain-crypto-js@4.2.1`，其`postinstall`脚本会部署一个跨平台远程访问木马（RAT）。攻击具有高度预谋和隐蔽性，旨在窃取凭证并建立持久访问。

- 🚨 **恶意版本发布**：攻击者通过劫持的axios维护者账户发布了恶意版本`axios@1.14.1`和`axios@0.30.4`，注入了一个从未在源码中使用的依赖`plain-crypto-js@4.2.1`。
- 🕵️ **隐蔽依赖与RAT投放**：恶意依赖的唯一目的是执行`postinstall`脚本，该脚本作为跨平台RAT投放器，针对macOS、Windows和Linux系统，从C2服务器获取并执行第二阶段有效载荷。
- 🧹 **自我销毁与反取证**：恶意软件执行后会删除自身，并用一个干净的`package.json`存根替换，报告版本为4.2.0，以逃避检测，使得事后检查`node_modules`难以发现异常。
- ⏱️ **精心策划的攻击时间线**：攻击提前约18小时准备，恶意依赖先以干净版本发布建立历史，39分钟内先后发布两个恶意axios版本以最大化覆盖，恶意版本在npm上存活约2-3小时后被撤销。
- 🔍 **攻击检测与响应**：StepSecurity的AI Package Analyst和Harden-Runner检测到了此次攻击，并通过异常网络连接（如对`sfrclak.com:8000`的调用）发现了恶意行为。攻击被负责任地披露给项目维护者，npm随后对恶意包实施了安全保留。
- 🛡️ **影响与应对措施**：如果安装了受影响版本，应假设系统已遭入侵。建议检查代码库、CI/CD流水线和开发机器，移除恶意包，降级到安全版本（如`axios@1.14.0`），并立即轮换所有可能暴露的凭证。

---

### [Axios供应链攻击采用了个性化定向社交工程手段](https://simonwillison.net/2026/Apr/3/supply-chain-social-engineering/)

**原文标题**: [The Axios supply chain attack used individually targeted social engineering](https://simonwillison.net/2026/Apr/3/supply-chain-social-engineering/)

Axios团队发布了对供应链攻击的详细事后分析，该攻击通过针对其维护者的高度定制化社交工程手段，成功植入恶意依赖包。

- 🎭 攻击者伪装成某公司创始人，克隆其形象与公司信息，通过Slack工作区建立联系
- 🛡️ 精心构建的Slack环境包含仿冒团队频道、LinkedIn动态等，甚至伪造其他开源维护者资料
- 📅 通过Microsoft Teams安排会议，制造多人参与的假象以增强可信度
- ⚠️ 会议中提示系统更新，诱导安装实为远程访问木马（RAT）的恶意软件
- 🔐 RAT窃取开发者凭证后，攻击者利用权限发布包含恶意代码的软件包
- ⏱️ 作者指出此类利用时间压力的攻击手法极具欺骗性，开源维护者需提高警惕

---

### [攻击者正瞄准高影响力Node.js维护者展开C...](https://socket.dev/blog/attackers-hunting-high-impact-nodejs-maintainers)

**原文标题**: [Attackers Are Hunting High-Impact Node.js Maintainers in a C...](https://socket.dev/blog/attackers-hunting-high-impact-nodejs-maintainers)

Socket CEO Feross Aboukhadijeh 分析了朝鲜如何劫持 Axios 库的事件，并探讨了这对软件供应链安全的未来影响。

- 🕵️ 朝鲜黑客通过接管维护者账户，在 Axios 库中植入恶意代码
- 🔗 攻击利用了软件供应链的依赖关系，影响广泛的下游项目
- 🛡️ 事件凸显了开源软件维护和依赖安全审查的脆弱性
- 📈 需要更严格的供应链安全措施和自动化监控工具来预防类似攻击
- 🌐 这一事件促使开发者社区重新评估对第三方依赖的信任模型

---

### [日程安排 | POSETTE：2026年Postgres大会 - POSETTE](https://posetteconf.com/2026/schedule/)

**原文标题**: [Schedule | POSETTE: An Event for Postgres 2026 - POSETTE](https://posetteconf.com/2026/schedule/)

POSETTE: An Event for Postgres 2026 是一场由微软Postgres团队主办的线上技术会议，聚焦于PostgreSQL数据库的最新发展、性能优化、云集成、AI应用及生态系统工具。会议包含多个主题演讲和技术分享，涵盖从核心功能到前沿趋势的广泛内容。

- 🗓️ 会议于6月10日、17日和18日进行多场直播，涵盖主题演讲、技术深度分享及总结环节。
- 🎤 主题演讲包括微软对Postgres的投入、Postgres 19新特性前瞻，以及Postgres作为“全能数据库”的崛起。
- ⚙️ 技术专题涉及性能调优（如random_page_cost、VACUUM增强）、新功能（如JSON处理、约束改进、逻辑解码）及扩展工具（如Apache AGE、pg_lake）。
- ☁️ 多个议题聚焦Azure云服务，包括Azure Database for PostgreSQL的性能提升、迁移策略及HorizonDB应对突发负载的解决方案。
- 🤖 AI与Postgres的结合是亮点，涵盖MCP协议、AI辅助调优、生产级RAG应用及智能体数据检索。
- 🔧 开发与运维主题包括分区表管理、大表维护、安全实践、测试覆盖（pgcov）及贡献指南。
- 📊 会议还探讨了Postgres在数据分析、图计算、事件驱动架构和逻辑复制方面的演进与应用。
- 💬 参会者可通过Discord等平台加入社区交流，会议内容由微软Postgres团队及其合作伙伴提供支持。

---

### [你不能取消一个JavaScript Promise（除了有时你可以） - Inngest博客](https://www.inngest.com/blog/hanging-promises-for-control-flow)

**原文标题**: [You can't cancel a JavaScript promise (except sometimes you can) - Inngest Blog](https://www.inngest.com/blog/hanging-promises-for-control-flow)

JavaScript Promise 本身没有内置的取消机制，但可以通过返回一个永不解析的 Promise 来中断异步函数的执行，同时允许垃圾回收器清理挂起的函数状态，从而实现类似中断的效果。

- 🚫 JavaScript Promise 没有原生的 `.cancel()` 方法，因为取消任意代码可能留下资源脏状态，需要协作清理
- 🛑 通过返回永不解析的 Promise 并等待它，可以让函数在 `await` 处停止，无需抛出异常或特殊处理
- ⚙️ 这种技术适用于需要精确中断异步函数的场景，例如在服务器less环境中处理硬超时和工作流步骤
- ⚠️ 使用抛出错误中断的方法容易被 `try/catch` 捕获并吞没，破坏控制流
- 🔄 生成器（Generators）天生支持中断，但语法不够直观，且难以处理并发操作
- 🔧 通过永不解析的 Promise 配合步骤状态记忆化，可以实现工作流的分步执行和恢复
- 🧠 利用事件循环的微任务和宏任务机制，确保函数在中断前能推进到新步骤
- 🗑️ 未解析的 Promise 在函数调用栈不可达时会被垃圾回收，不会造成内存泄漏
- 📦 该模式已应用于 Inngest TypeScript SDK，用于在服务器less环境中可靠地中断和恢复工作流

---

### [[RFC] JSIR：面向JavaScript的高级中间表示 - MLIR - LLVM讨论论坛](https://discourse.llvm.org/t/rfc-jsir-a-high-level-ir-for-javascript/90456)

**原文标题**: [[RFC] JSIR: A High-Level IR for JavaScript - MLIR - LLVM Discussion Forums](https://discourse.llvm.org/t/rfc-jsir-a-high-level-ir-for-javascript/90456)

JSIR 是一种基于 MLIR 框架的高层 JavaScript 中间表示，旨在填补 JavaScript 工具链中缺乏公开、稳定 IR 的空白。它通过保留 AST 的全部信息，支持源代码与 IR 之间的高保真双向转换，并利用 MLIR 区域表示控制流结构，同时提供数据流分析能力。JSIR 已在 Google 内部用于代码分析和转换任务，如反编译和反混淆，并已开源。

- 🎯 **填补 IR 空白**：JavaScript 社区已有大量 AST 工具（如 Babel、ESLint），但缺乏公开的 IR 工具，JSIR 旨在解决这一问题。
- 🔄 **高保真双向转换**：JSIR 设计支持源代码 ↔ AST ↔ JSIR 的无损往返转换，内部测试显示转换成功率超过 99.9%。
- 🏗️ **基于 MLIR 构建**：利用 MLIR 的区域机制表示控制流结构（如 if、while 语句），并通过包装 MLIR 数据流分析 API 提供更易用的分析框架。
- 🛠️ **实际应用场景**：在 Google 内部用于 Hermes 字节码反编译、JavaScript 反混淆等任务，并结合 Gemini LLM 提升效果。
- 🌐 **开源与社区贡献**：JSIR 已开源，并希望与 MLIR 社区合作，探索上游集成、改进数据流分析 API 等方向。
- 🔍 **设计亮点**：区分左值与右值表示，通过后序遍历 AST 生成 IR，并保持与 ESTree 标准的高度映射一致性。
- 📈 **未来展望**：计划进一步整合 MLIR 内置功能（如符号表）、贡献区域数据流分析改进，并评估上游至 MLIR 的可行性。

---

### [GitHub - google/jsir：下一代JavaScript分析工具集 · GitHub](https://github.com/google/jsir)

**原文标题**: [GitHub - google/jsir: Next-generation JavaScript analysis tooling · GitHub](https://github.com/google/jsir)

JSIR 是一个基于 MLIR 的下一代 JavaScript 分析工具，其核心是一个高级中间表示，支持数据流分析和无损转换回源代码，适用于源代码到源代码的转换。它在 Google 被用于反编译和反混淆等场景，并通过结合 Gemini LLM 提升反混淆能力。项目提供了 Docker 和本地构建方式，便于快速开始使用。

- 🛠️ **核心设计**：基于 MLIR 的高级中间表示，兼顾高级别源代码转换和低级别数据流分析需求。
- 🔄 **主要用途**：在 Google 内部用于 JavaScript 反编译（如 Hermes 字节码）和反混淆，支持源代码到源代码的转换。
- 📄 **技术亮点**：通过 MLIR 区域精确建模控制流结构，平衡高级 AST 转换与数据流分析（如污点分析、常量传播）。
- 🐳 **快速开始**：推荐使用 Docker 构建和运行，也可通过 Bazel 在本地安装构建工具并编译项目。
- 🧪 **测试与运行**：提供完整的测试套件和 `jsir_gen` 工具，可将 JavaScript 文件转换为 JSHIR 进行进一步分析。
- 🔗 **相关资源**：包括 LLVM 开发者会议演讲和结合 LLM 的反混淆研究论文，项目声明为非官方 Google 产品。

---

### [Azure SDK for JavaScript 中 Node.js 20.x 支持终止公告 - Azure SDK 博客](https://devblogs.microsoft.com/azure-sdk/announcing-the-end-of-support-for-node-js-20-x-in-the-azure-sdk-for-javascript/)

**原文标题**: [Announcing the end of support for Node.js 20.x in the Azure SDK for JavaScript - Azure SDK Blog](https://devblogs.microsoft.com/azure-sdk/announcing-the-end-of-support-for-node-js-20-x-in-the-azure-sdk-for-javascript/)

Azure SDK for JavaScript 将于2026年7月9日起停止支持 Node.js 20.x，建议用户升级至活跃的 Node.js LTS 版本以确保安全性和功能更新。

- 🚨 **停止支持时间**：2026年7月9日起，Azure SDK for JavaScript 将不再支持 Node.js 20.x（该版本于2026年4月30日终止生命周期）。
- 🔄 **升级建议**：用户应升级至活跃的 Node.js 长期支持（LTS）版本，以继续获得安全更新和最新功能。
- ⚠️ **影响说明**：从该日期起，SDK 将设置 Node.js 22.x 为最低支持版本；使用 Node.js 20.x 安装新版 SDK 会触发警告，若启用严格引擎模式则会导致安装错误。
- 📜 **政策依据**：此举遵循 Node.js 的发布周期和 Azure SDK 支持政策，对终止生命周期的版本停止支持无需更新 SDK 主版本号。
- 💡 **后续操作**：用户可暂时使用旧版 SDK 配合 Node.js 20.x，但强烈建议尽快升级 Node.js 版本以保障安全。

---

### [npm可信发布现已支持CircleCI - GitHub更新日志](https://github.blog/changelog/2026-04-06-npm-trusted-publishing-now-supports-circleci/)

**原文标题**: [npm trusted publishing now supports CircleCI - GitHub Changelog](https://github.blog/changelog/2026-04-06-npm-trusted-publishing-now-supports-circleci/)

npm 现已支持 CircleCI 作为可信发布的 OIDC 提供商，进一步扩展了 CI/CD 管道的安全认证能力，同时推出了备受期待的网站深色模式。

- 🔐 npm 可信发布新增支持 CircleCI，与 GitHub Actions 和 GitLab CI/CD 并列，维护者可通过 CI/CD 管道直接认证，无需存储凭据
- 🌐 可信发布现已覆盖大多数主流 CI 提供商，配置可通过 npm 官网或 `npm trust` CLI 命令完成
- 🌙 npmjs.com 网站正式推出深色模式，该功能借助 GitHub Copilot agent 模式高效开发，极大减少了工程时间
- 🛡️ npm 团队持续聚焦于强化供应链安全，并提升维护者对软件包发布的控制权
- 💬 用户可通过社区讨论提供反馈或咨询问题

---

### [npmx：人民驱动的软件包索引 | Igalia](https://www.igalia.com/chats/npmxyz)

**原文标题**: [npmx : The PeopleâPowered Package Index | Igalia](https://www.igalia.com/chats/npmxyz)

npmx是一个由社区驱动的开源项目，旨在为npm包注册表提供一个更现代化、功能更丰富的网站界面，以替代npmjs.com。它强调用户体验、社区协作和开源精神，通过集成社交功能、包管理工具和生态系统数据，帮助开发者更高效地发现和管理包。

- 🚀 **项目起源**：Daniel Roe因对npmjs.com的不满，在社区反馈的推动下，与Matias Capeletto等人共同发起，迅速吸引了大量贡献者。
- 👥 **社区驱动**：通过私密启动、邀请制社区和精心维护的友好环境，项目在短时间内获得了超过100位贡献者和数千次提交。
- 🌐 **功能特色**：提供暗色模式、包管理界面优化、安装大小和漏洞提示，并与e18e项目集成，帮助清理过时包。
- 🔗 **社交集成**：基于AT Proto协议实现去中心化社交功能，允许用户“点赞”包，未来计划扩展项目组织和信任网络。
- 💡 **开源理念**：强调团队协作优于“10倍开发者”，注重迭代开发和社区参与，推动开源可持续发展。
- 💰 **资金与未来**：项目计划通过基金会模式寻求可持续资金，支持核心贡献者，并探索数据主权和开源货币化新途径。
- 🌱 **健康维护**：倡导开源开发者休假文化，关注项目长期健康与社区福祉。

---

### [npmx - npm 注册表的包浏览器](https://npmx.dev/)

**原文标题**: [npmx - Package Browser for the npm Registry](https://npmx.dev/)

npmx 是一款专为 npm 注册表设计的快速现代浏览器，旨在提升包搜索与开发体验。

- 🔍 **即时搜索功能**：提供快速开关的即时搜索选项，优化查找 npm 包的效率
- 🛠️ **技术兼容广泛**：支持 Nuxt、Vue、React、Svelte 等多种主流前端框架和工具
- 📅 **持续更新维护**：最新版本 v0.8.1 于 2026 年 4 月发布，保持技术前沿性
- 🤝 **开源社区参与**：鼓励开发者通过 GitHub 贡献代码，共同构建理想的 npm 体验
- 💬 **活跃社区交流**：提供 Discord 社区平台，方便用户交流讨论和分享想法
- 📢 **信息同步渠道**：通过 Bluesky 社交平台持续发布项目最新动态和更新信息

---

