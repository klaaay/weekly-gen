### [设置亚马逊设备构建工具MCP | 设计与开发Vega应用](https://developer.amazon.com/docs/vega/0.22/mcp-server.html?sc_category=&sc_channel=3P&sc_publisher=TWR&sc_campaign=ACQ_VG&sc_country=US&sc_detail=SLORBER-3_VG_GEN)

**原文标题**: [Set Up Amazon Devices Builder Tools MCP | Design and Develop Vega Apps ](https://developer.amazon.com/docs/vega/0.22/mcp-server.html?sc_category=&sc_channel=3P&sc_publisher=TWR&sc_campaign=ACQ_VG&sc_country=US&sc_detail=SLORBER-3_VG_GEN)

本文档介绍了 Amazon Devices Builder Tools MCP 服务器，这是一个独立的 npm 包，可为 AI 编码代理提供 Vega 专用元数据、工具和功能，帮助开发者更高效地构建、调试和优化应用。

- 🛠️ **MCP 服务器概述**：Amazon Devices Builder Tools MCP 是一个独立的 npm 包，为 AI 代理提供 Vega 专用元数据、工具和功能，支持性能分析、崩溃调试、项目设置和 Amazon 功能集成。
- 🔒 **隐私保护**：该 MCP 不收集、传输或存储任何机密信息（如代码、查询或项目文件），仅向 Amazon 发送文档搜索查询以获取相关文档。
- 📋 **安装前提**：需要 Node.js（兼容 npm）和 Vega SDK v0.22 或更高版本，并通过 `npx` 命令安装和初始化项目上下文。
- ⚙️ **配置与使用**：运行 `npx @amazon-devices/amazon-devices-buildertools-mcp@latest --init-context` 进行交互式安装，支持选择 AI 代理和安装目录。
- 🔄 **版本更新**：该工具原名 `@amazon-devices/vega-devtools-mcp`，用户需删除旧版本并安装新版本以获取最新功能。
- 📊 **匿名遥测**：Amazon 收集匿名遥测数据（如功能使用模式、错误率、性能指标）以改进工具，但不会收集个人身份信息或机密数据。
- 🔍 **故障排除**：如遇问题，可参考“Troubleshoot Amazon Devices Builder Tools MCP”文档获取帮助。

---

### [Next.js 2026年5月安全更新 - Vercel](https://vercel.com/changelog/next-js-may-2026-security-release)

**原文标题**: [Next.js May 2026 security release - Vercel](https://vercel.com/changelog/next-js-may-2026-security-release)

Next.js 发布了协调安全更新，修复了13个安全公告，涉及拒绝服务、中间件与代理绕过、服务端请求伪造、缓存投毒和跨站脚本攻击。其中一个公告涉及上游React服务端组件漏洞（CVE-2026-23870）。所有受影响用户应立即升级到补丁版本。

- 🛡️ **中间件与代理绕过**：影响依赖middleware.js或proxy.js进行授权的应用，包括通过App Router段预取URL、动态路由参数注入等方式绕过授权，以及中间件重定向缓存投毒。
- 💥 **拒绝服务**：影响使用服务端函数、部分预渲染缓存组件或图片优化API的应用，包括React服务端组件DoS（CVE-2026-23870）、连接耗尽DoS及图片优化API DoS。
- 🌐 **服务端请求伪造**：影响处理WebSocket升级请求的应用，存在SSRF风险。
- 🧊 **缓存投毒**：影响在React服务端组件响应前有缓存层的应用，包括RSC响应缓存投毒和缓存破坏碰撞。
- 🕸️ **跨站脚本攻击**：影响App Router中使用CSP nonce或beforeInteractive脚本处理不可信输入的应用，存在XSS风险。
- 🔧 **修复版本**：Next.js需升级到15.5.18或16.2.6；React的react-server-dom-*包需升级到19.0.6、19.1.7或19.2.6。仅补丁可完全缓解，WAF无法可靠拦截。

---

### [事后分析：TanStack npm 供应链安全事件 | TanStack 博客](https://tanstack.com/blog/npm-supply-chain-compromise-postmortem)

**原文标题**: [Postmortem: TanStack npm supply-chain compromise | TanStack Blog](https://tanstack.com/blog/npm-supply-chain-compromise-postmortem)

2026年5月11日，TanStack的npm供应链遭到攻击，攻击者利用GitHub Actions的多个漏洞，在42个包中发布了84个恶意版本，窃取凭证并自我传播。

- 🚨 **攻击概述**：攻击者通过结合`pull_request_target`漏洞、GitHub Actions缓存投毒和OIDC令牌内存提取，在42个`@tanstack/*` npm包中发布了84个恶意版本，无需窃取npm令牌即可发布。
- 🎯 **影响范围**：受影响包包括`@tanstack/history`等42个包，而`@tanstack/query*`、`@tanstack/table*`等家族确认安全。恶意代码在npm安装时执行，窃取AWS、GCP、Kubernetes、npm、GitHub和SSH凭证。
- ⏱️ **攻击时间线**：2026年5月10日攻击者创建恶意fork，5月11日通过PR触发缓存投毒，随后在19:20-19:26 UTC利用OIDC令牌发布恶意版本。外部研究人员在20分钟内发现并报告。
- 🔍 **根因分析**：三个漏洞链式利用：`pull_request_target`允许fork代码执行、缓存投毒跨越信任边界污染生产工作流、OIDC令牌从运行器内存中提取。每个漏洞单独不足，但组合后实现完全攻击。
- 🛡️ **检测与响应**：外部研究人员`ashishkurmi`（StepSecurity）在20分钟内报告，团队立即响应：移除团队权限、清除缓存、弃用所有受影响版本、发布安全公告。IOC包括`router_init.js`文件和Session网络外泄。
- 📚 **经验教训**：需加强内部监控、审计`pull_request_target`工作流、固定第三方操作版本、改进npm发布策略（如短生命周期令牌或来源验证）。幸运的是，攻击者代码导致测试失败，使攻击更易被发现。

---

### [迷你沙胡鲁德再次出击：TanStack及更多npm包遭入侵 | Wiz博客](https://www.wiz.io/blog/mini-shai-hulud-strikes-again-tanstack-more-npm-packages-compromised)

**原文标题**: [Mini Shai-Hulud Strikes Again: TanStack + more npm Packages Compromised | Wiz Blog](https://www.wiz.io/blog/mini-shai-hulud-strikes-again-tanstack-more-npm-packages-compromised)

2026年5月11日，TeamPCP发动了一场针对npm和PyPi生态系统的协同供应链攻击，通过利用GitHub Actions漏洞和多重C2通道，大规模投放凭证窃取型蠕虫恶意软件，影响范围包括TanStack、UiPath、Mistral AI等多个知名软件包。

- 🔍 **攻击手法**：攻击者利用GitHub Actions的`pull_request_target`工作流漏洞，通过恶意PR窃取OIDC令牌，无需npm凭证即可发布恶意包版本。
- 🧪 **感染载体**：恶意npm包通过`optionalDependencies`指向恶意Git提交和嵌入约2.3MB的`router_init.js`文件传播；PyPi包则通过下载执行`transformers.pyz`模块化窃密器。
- 🐛 **恶意行为**：植入的恶意软件是凭证窃取器和自传播蠕虫，窃取CI/CD令牌、云凭证、Kubernetes服务账户、Vault令牌等，并利用窃取的令牌发布更多恶意包。
- 📡 **三重C2架构**：通过域名仿冒（`git-tanstack.com`）、去中心化Session信使网络和GitHub API死信仓库三种冗余通道外泄窃取的数据。
- ⚠️ **破坏性机制**：在开发者机器上安装持久化守护进程`gh-token-monitor`，一旦检测到令牌被撤销，会执行`rm -rf ~/`命令删除用户主目录；24小时后自动退出。
- 🇷🇺 **规避检测**：恶意软件会检查系统语言是否为俄语，若是则终止运行且不泄露数据；PyPi变种还会检查以色列或伊朗时区/语言，有概率播放mp3并执行删除操作。
- 🐍 **Python变种新特点**：首次针对密码管理器（1Password、Bitwarden）进行窃取，仅在Linux上执行，且会检查CPU核心数（少于4个则退出）。
- 🛡️ **应急措施**：安全团队应立即检查锁文件和CI日志中的受影响版本，查找并移除`gh-token-monitor`守护进程，在移除前不要撤销GitHub令牌，轮换所有受影响凭证，并阻止C2基础设施。

---

### [npm 泄露事件后强化 TanStack | TanStack 博客](https://tanstack.com/blog/incident-followup)

**原文标题**: [Hardening TanStack After the npm Compromise | TanStack Blog](https://tanstack.com/blog/incident-followup)

以下是根据您提供的文章内容生成的摘要：

TanStack 团队在 npm 遭受攻击后，采取了多项安全加固措施，以防止类似事件再次发生。

- 📦 **攻击概述**：14 个包被恶意重新发布到 npm，攻击者利用 CI 缓存投毒，在发布流程中窃取短期令牌，而非直接窃取长期令牌。
- 🔍 **攻击路径**：攻击者通过一个被关闭的 PR 触发工作流，利用 `pull_request_target` 事件获得缓存写入权限，从而在后续合法发布中注入恶意代码。
- 🛡️ **已实施措施**：禁用 pnpm 缓存、移除所有 GitHub Actions 缓存、将操作固定到提交 SHA、强制非 SMS 双因素认证、移除 `pull_request_target` 使用、升级到 pnpm 11。
- 🔧 **计划中的改进**：添加 zizmor 静态分析、对 `.github` 文件夹设置 CODEOWNERS、用更保守的 `actions/cache/restore` 替换 pnpm 缓存。
- 🤔 **PR 政策讨论**：考虑限制外部贡献者直接提交 PR，改为邀请制，以降低 CI 被恶意利用的风险，但尚未最终决定。
- 💡 **核心教训**：CI 安全是之前被忽视的薄弱环节，仅依赖 OIDC、2FA 等工具不足，需主动审查工作流模式，平台也应改进缓存隔离等设计。

---

### [GitHub - lirantal/npm安全最佳实践：npm包管理器安全最佳实践合集 · GitHub](https://github.com/lirantal/npm-security-best-practices)

**原文标题**: [GitHub - lirantal/npm-security-best-practices: Collection of npm package manager Security Best Practices · GitHub](https://github.com/lirantal/npm-security-best-practices)

该文档提供了全面的npm安全最佳实践指南，涵盖从开发者本地环境到包维护的各个层面。

- 🔒 **禁用安装后脚本**：通过配置`ignore-scripts`或使用pnpm/Bun的内置策略，阻止恶意包在安装时执行任意代码。
- 🚫 **阻止Git依赖**：使用npm的`allow-git none`或pnpm的`blockExoticSubdeps`，防止绕过注册表安全扫描的代码引入。
- ⏳ **安装冷却期**：设置`min-release-age`（如3天），避免安装刚发布可能含恶意代码的新版本。
- 🛡️ **强化包安装工具**：使用`npq`或Socket Firewall（`sfw`）在安装前审计包的健康信号和恶意行为。
- 🔐 **防止锁文件注入**：通过`lockfile-lint`验证锁文件来源，确保包来自受信任的注册表。
- ✅ **使用确定性安装**：用`npm ci`替代`npm install`，确保严格遵循锁文件，避免版本不一致。
- 📋 **避免盲目升级**：使用交互式工具（如`npm-check-updates --interactive`）或自动化PR（Dependabot/Snyk）进行受控升级。
- 🖥️ **硬化npx执行**：预安装包到工作区并使用`--offline`模式，防止npx在无锁文件情况下下载执行恶意代码。
- 🔑 **不存储明文密钥**：使用1Password或Infisical等密钥管理工具，通过引用代替`.env`文件中的明文密钥。
- 🐳 **使用开发容器**：通过Dev Containers隔离项目环境，限制恶意包的攻击范围。
- 🔐 **启用2FA**：为npm账户启用双因素认证，防止账户劫持和恶意发布。
- 📜 **发布时附带来源证明**：使用`npm publish --provenance`生成可验证的构建来源信息。
- 🔗 **使用OIDC发布**：通过OpenID Connect消除长期令牌风险，自动生成来源证明。
- 🌿 **减少依赖树**：利用现代JavaScript原生功能替代外部库，降低攻击面。
- 📊 **咨询安全数据库**：在采用新包前，通过Snyk安全数据库检查其维护、流行度和安全评分。
- ⚠️ **不轻信npmjs.org**：检查实际tarball内容，因为网站显示的代码可能与安装的代码不一致。
- 🎯 **防止依赖混淆攻击**：使用作用域包名（`@yourorg/package`）并配置私有注册表路由，避免公共注册表同名包被安装。

---

### [伟大的公司诞生于黑客马拉松 - 伊恩·瓦纳加斯](https://newsletter.posthog.com/p/great-companies-are-built-in-hackathons)

**原文标题**: [Great companies are built in hackathons - by Ian Vanagas](https://newsletter.posthog.com/p/great-companies-are-built-in-hackathons)

### 概述总结
优秀公司诞生于黑客马拉松，本文分享了如何成功举办黑客马拉松的实用方法，强调创新、全员参与和持续迭代。

- 🚀 **黑客马拉松是创新引擎**：必须与日常工作完全分离，专注于全新想法，禁止讨论路线图上的项目，确保100%投入。
- 👥 **面向全员开放**：非技术人员也能借助AI工具参与，跨职能团队能打破部门壁垒，提升文化效益和创新成果。
- 🎤 **演示环节不可少**：强制演示能推动项目落地，但评判和奖品可省略，避免人为动机干扰真实创新。
- 📦 **优秀项目应持续迭代**：黑客马拉松后给予团队弹性时间完成收尾，推动项目从原型走向生产，如PostHog的Logs产品。
- 🎯 **打造传统**：将黑客马拉松变为年度传统，建立创意分享渠道（如Slack频道），鼓励全年积累灵感，形成文化基石。

---

### [React 项目规划 — 坦纳·林斯利](https://tannerlinsley.com/posts/projecting-react)

**原文标题**: [Projecting React â Tanner Linsley](https://tannerlinsley.com/posts/projecting-react)

### 概述总结
Tanner Linsley 在 TanStack Start 项目中，因 React 体积过大（~60 KB gzip）而探索使用 Preact 替代，但发现其与 React 19 不兼容。受 Kyle Mathews 关于“代码作为物化视图”的启发，他利用 AI 代理创建了一个针对 TanStack Start 需求优化的 React 投影（projection），名为 `@tanstack/redact`。该投影将 React 核心缩小至 7-9 KB gzip，通过可切换功能模块实现灵活定制，并在实际网站（tannerlinsley.com 和 tanstack.com）上验证了性能提升（如 JS 负载减少 33%，渲染速度提升 2 倍）。Linsley 强调这是实验性项目，不打算广泛推广，并认为未来 Web 开发将更趋向于“发行版”和“混音”模式。

- 🚀 **React 体积问题**：React 通过 Vite 打包后约 60 KB gzip，是 TanStack 工具链中最大的部分，促使寻找更轻量替代方案。
- 🔄 **Preact 兼容性失败**：`preact/compat` 与 React 19 的 `use()` 语义、服务器操作、门户等存在差异，导致需要大量补丁，最终放弃。
- 💡 **代码作为物化视图**：受 Kyle Mathews 启发，将 React 公共 API 视为“基表”，代码是“投影”，AI 可低成本生成不同投影。
- 🛠️ **@tanstack/redact 投影**：核心仅 7.08 KB gzip（`nano` 预设），支持 8 个可切换功能（如门户、上下文、Suspense 等），通过 Vite 插件实现零运行时分支。
- 📊 **性能提升**：相比 React 19，`full` 预设缩小 80-85%，客户端导航速度提升 2.24 倍，SSR 速度提升约 3 倍，JS 负载减少 33%。
- 🌐 **实际验证**：tannerlinsley.com 和 tanstack.com 已运行在投影上，LCP 和 FCP 显著改善，仅 RSC 重页面 LCP 有轻微回归（仍处于“良好”范围）。
- 🤖 **AI 辅助开发**：一天内完成投影构建，后续通过生产环境 bug 修复（如协调顺序、效果清理时机、受控输入等）完善。
- 🔒 **非营销定位**：不打算推广，避免社区成本；仅用于个人项目，不纳入 TanStack Start 核心依赖。
- 🌍 **未来趋势**：类比 Linux 发行版和音乐混音，认为 Web 开发将出现更多针对特定需求的库投影，成本下降使“默认使用上游”不再绝对。

---

### [龙湖](https://longho.dev/posts/rsc-server-functions-are-not-an-api-boundary/)

**原文标题**: [Long Ho](https://longho.dev/posts/rsc-server-functions-are-not-an-api-boundary/)

这篇报道主要讨论了人工智能在医疗领域的应用进展，特别是AI辅助诊断系统如何提高疾病检测的准确性和效率，同时强调了数据隐私和算法偏见等挑战。

- 🩺 **AI诊断系统提升效率**：AI在影像诊断中表现优异，能快速识别早期病变，如肺癌和乳腺癌，减少医生漏诊风险。
- 📊 **数据隐私保护是关键**：医疗AI依赖大量患者数据，但需严格遵循隐私法规，防止敏感信息泄露。
- ⚖️ **算法偏见需警惕**：训练数据若缺乏多样性，可能导致AI对特定人群的诊断准确率下降，需持续优化模型公平性。
- 🚀 **临床应用加速落地**：多家医院已试点AI辅助决策系统，帮助医生制定个性化治疗方案，缩短诊断时间。
- 🔬 **跨学科合作推动创新**：医学专家与工程师协作开发更精准的AI工具，未来可能覆盖更多疾病领域。

---

### [在React Router中理清对话框——编程不易——](https://programmingarehard.com/2026/05/06/react-router-dialogs.html/)

**原文标题**: [Untangling dialogs in React Router — ProgrammingAreHard — ](https://programmingarehard.com/2026/05/06/react-router-dialogs.html/)

以下是对该文章的总结概述：

本文介绍了如何在 React Router 7 中优雅地实现模态对话框，避免使用 `useEffect`，通过路由分离、视图过渡和会话存储等模式，使代码更清晰、可维护。

- 🚀 **初始方案问题**：直接在组件内使用 `<Dialog>` 会导致状态管理复杂，需要多个 `useState`、`useFetcher` 和 `useEffect` 来同步数据加载、错误处理和对话框关闭，代码混乱。
- 🧩 **路由分离方案**：将对话框拆分为独立路由（如 `models.install.tsx` 和 `models.uninstall.$name.tsx`），每个路由只负责单一功能，代码更清晰。
- 🔗 **优化导航性能**：使用 `unstable_defaultShouldRevalidate={false}` 避免不必要的数据重新验证，`preventScrollReset` 保持滚动位置，提升用户体验。
- 🎯 **错误与成功反馈**：通过 `actionData` 在对话框内显示错误信息；使用 Cookie 会话存储（`session.flash`）实现成功提示（如 toast），无需 `useEffect`。
- 🎬 **退出动画**：利用浏览器视图过渡（View Transitions）为对话框添加平滑的关闭动画，通过 CSS 定义 `::view-transition-old` 和 `::view-transition-new` 实现。
- ⚠️ **错误处理权衡**：若对话框频繁返回错误，视图过渡可能导致抖动。此时需使用 `useEffect` 监听成功状态再触发导航，这是可接受的折衷。
- ✅ **最终成果**：每个对话框作为独立路由，代码反映应用逻辑；视图过渡解决动画问题；会话存储处理反馈；整体模式简洁、可维护。

---

### [动画容器边界](https://www.userinterface.wiki/animating-container-bounds)

**原文标题**: [Animating Container Bounds](https://www.userinterface.wiki/animating-container-bounds)

本文介绍了如何使用 Motion 库实现容器边界平滑动画，解决宽度和高度无法直接动画的问题。

- 📏 **核心问题**：浏览器无法在固定值和“内容自适应”尺寸之间插值，导致容器宽度/高度变化时直接跳跃。
- 🛠️ **解决方案**：通过 `ResizeObserver` 构建 `useMeasure` 钩子，实时测量内部元素尺寸，并传递给 Motion 的 `animate` 属性。
- 🎯 **实现技巧**：使用内外两层 div——外层用 Motion 控制动画，内层挂载 `ref` 进行测量，避免动画与测量在同一元素上形成循环。
- 🔄 **宽度动画示例**：按钮标签切换时，测量内部包裹层的宽度，动画化外层按钮，实现平滑伸缩（需检查 `bounds.width > 0` 避免初始从 0 动画）。
- 📐 **高度动画示例**：可展开内容（如手风琴、FAQ）中，测量内部内容高度，动画化外层容器，支持动态增删内容。
- ⚠️ **注意事项**：初始渲染时尺寸为 0，需用条件判断避免动画；动画与测量分离；可添加小延迟提升自然感；避免过度使用此模式。

---

### [React 应用中的安全性 - Certificates.dev](https://certificates.dev/blog/security-in-react-applications)

**原文标题**: [Security in React Applications - Certificates.dev](https://certificates.dev/blog/security-in-react-applications)

本篇文章介绍了React应用中的关键安全实践，涵盖XSS防护、安全认证、服务端验证和内容安全策略。

- 🛡️ **React内置XSS防护**：React默认转义JSX中的特殊字符，防止脚本注入，但`dangerouslySetInnerHTML`会绕过此保护，需谨慎使用。
- 🧹 **使用DOMPurify清理HTML**：当必须渲染用户提供的HTML时，使用DOMPurify库移除危险标签和属性，确保安全。
- 🔒 **安全存储令牌**：避免将认证令牌存储在`localStorage`或`sessionStorage`中，改用`HttpOnly`、`Secure`和`SameSite=Strict`属性的Cookie，防止XSS窃取。
- 🛑 **CSRF防护**：在状态变更请求中包含CSRF令牌，配合`SameSite=Strict`属性，防止跨站请求伪造攻击。
- ✅ **服务端输入验证**：使用Zod库在服务端验证用户输入，并始终使用参数化查询防止SQL注入，客户端的验证仅用于用户体验。
- 🚧 **内容安全策略（CSP）**：通过HTTP头配置CSP，限制资源加载来源，并使用nonce允许必要的内联脚本，增加深度防御层。
- 📋 **测试与总结**：先用`Content-Security-Policy-Report-Only`测试策略，再强制执行；综合使用上述措施构建安全React应用。

---

### [从React到原生Web的nanotags迁移：节省了100 KB——火星编年史，邪恶火星人团队博客](https://evilmartians.com/chronicles/from-react-to-native-web-with-nanotags-a-migration-that-saved-100kb)

**原文标题**: [From React to native web with nanotags: a migration that saved 100 KB—Martian Chronicles, Evil Martians’ team blog](https://evilmartians.com/chronicles/from-react-to-native-web-with-nanotags-a-migration-that-saved-100kb)

### 概述总结
- 📉 通过从 React 迁移到原生 Web Components，成功减少 100 KB JavaScript 体积，且功能未受影响。
- 🚀 营销网站本质上是静态的，使用 React 等 SPA 框架会带来不必要的运行时开销。
- 🧩 Astro 框架默认零 JavaScript，但引入交互时容易依赖 React，导致体积膨胀。
- 🔧 作者开发了 nanotags 库，简化 Web Components 编写，提供类型安全、响应式属性和自动清理。
- 🎯 迁移后，组件系统总大小约 3 KB，远低于 React 的 62.8 KB（gzip）。
- ♿ 无障碍性未退化，通过 W3C ARIA 指南和 LLM 辅助实现，部分交互甚至有所改进。
- 🧩 nanotags 核心库仅 2.5 KB，支持按需导入，避免不必要的代码。
- 🌐 使用平台原生 API（Custom Elements、DOM、CSS），减少对第三方框架的依赖。
- 📚 文档和示例已公开，支持 AI 辅助开发。

---

### [探索HTML在Canvas中的提案 | Codrops](https://tympanus.net/codrops/2026/05/13/exploring-the-html-in-canvas-proposal/)

**原文标题**: [Exploring the HTML-in-Canvas Proposal | Codrops](https://tympanus.net/codrops/2026/05/13/exploring-the-html-in-canvas-proposal/)

本文探讨了HTML-in-Canvas提案，该提案允许在Canvas中渲染真实HTML内容，保留布局、可访问性和CSS样式等DOM优势，并通过实验性API和示例展示了其潜在应用。

- 🎨 提案核心：通过`layoutsubtree`属性、`drawElementImage()`方法和`paint`事件，实现Canvas内HTML的渲染与交互，目前需在Chromium浏览器中启用实验性标志。
- 🖼️ 基础应用：将HTML内容渲染为Canvas纹理后，可应用于后处理效果（如流体、雨滴、像素化），同时保持SEO和可访问性。
- ✨ 小交互：实现微妙UI效果（如输入框消失动画），无需隐藏Canvas技巧，直接渲染HTML元素，提升用户体验。
- 🔄 页面过渡：利用Canvas实现内容区域或页面间的过渡效果（如卷页、登录揭示），简化复杂动画开发。
- 🖥️ 3D场景UI：在Three.js等3D框架中，通过HTMLTexture和InteractionManager，将HTML内容嵌入3D对象（如电脑屏幕），支持原生事件处理，替代传统纹理或uikit方案。
- ⚠️ 当前限制：提案处于早期阶段，受安全限制（如跨域、脚本执行），但比现有替代方案（html2canvas、SVG foreignObject）更灵活，后者存在CSS支持不完整或可访问性缺失问题。
- 🌟 未来展望：若提案成熟，将模糊DOM与Canvas的界限，推动游戏、交互体验和WebXR应用的UI开发，实现统一渲染管线。

---

### [GitHub - svar-widgets/react-gantt: 高性能React甘特图，支持TypeScript和灵活的时间线配置。](https://github.com/svar-widgets/react-gantt)

**原文标题**: [GitHub - svar-widgets/react-gantt: High-performance React Gantt chart with TypeScript support and flexible timeline configuration. · GitHub](https://github.com/svar-widgets/react-gantt)

SVAR React Gantt 是一个高性能、可定制的 React 甘特图组件，支持 TypeScript、React 19 和灵活的时间线配置。

- 🎯 **核心功能丰富**：支持交互式拖放、任务依赖、进度可视化、子任务层级、可配置时间刻度（小时/天/周/冲刺/阶段）、网格列自定义、排序、过滤、工具栏、上下文菜单、缩放、热键和本地化。
- 🚀 **PRO 版增强**：提供工作日历、自动排程、关键路径、松弛可视化、汇总、基线、拆分任务、撤销/重做、导出为 PNG/PDF/Excel/MS Project 等高级功能。
- 🛠️ **使用简便**：通过 `@svar-ui/react-gantt` 包导入，只需提供任务数据（含 ID、文本、开始/结束时间、进度等）即可快速集成。
- ⚡ **高性能**：专为处理数千个任务而设计，演示中支持 10k 任务的高效渲染。
- ⭐ **社区支持**：鼓励用户给项目加星，通过 Issues 或社区论坛获取帮助，遵循 MIT 许可证开源。

---

### [Waku 1.0（测试版）— Waku](https://waku.gg/blog/waku-v1-beta)

**原文标题**: [Waku 1.0 (beta) — Waku](https://waku.gg/blog/waku-v1-beta)

Waku 1.0-beta 版本发布，聚焦兼容性与生产就绪，引入版本偏差处理、Vite 8 与 Rolldown 打包器，并优化了路由与开发体验。

- 🎉 发布 Waku 1.0-beta，这是一个基于 React 服务器组件的轻量框架，适合静态为主的网站（如营销页、博客、文档）
- 🔄 引入版本偏差处理：重新部署后，旧版客户端可恢复正常，避免崩溃
- ⚡ 升级至 Vite 8，集成 Rolldown 打包器，提升构建性能
- 🛠️ 新增浏览器开发者工具中服务器组件的性能追踪
- 🔒 支持内容安全策略（CSP），增强安全性
- 🧩 路由器更灵活：支持片段路由、带前缀的片段、尾部斜杠处理、布局片段属性
- 🖥️ 支持 Node 26
- 💬 邀请用户继续测试，并提供 GitHub Discussions 和 Discord 反馈渠道

---

### [Jotai v2.20.0 与存储构建模块](https://newsletter.daishikato.com/p/jotai-v2-20-0-and-the-store-building-blocks)

**原文标题**: [Jotai v2.20.0 and the Store Building Blocks](https://newsletter.daishikato.com/p/jotai-v2-20-0-and-the-store-building-blocks)

Jotai v2.20.0 发布，重点优化了存储构建块的性能，并回顾了从 v2.12.0 以来的改进历程。

- 📦 引入存储构建块概念：在 v2.12.0 中，Jotai 通过暴露内部机制，允许生态库在创建新存储时进行自定义，而非事后扩展。
- 🔧 逐步完善 API：经过 v2.15.0 等版本的迭代，构建块的 API 变得既灵活又安全，降低了误用风险。
- ⚡ 修复性能回归：针对 WeakMap 导致的性能问题，团队将参数传递方式改为直接传参，虽不够完美但更符合设计模型。
- 🚀 展望 Jotai v3：v2.20.0 已发布，作者表示已准备好着手开发下一个大版本。

---

### [发布 v6.1.0 · remarkablemark/html-react-parser · GitHub](https://github.com/remarkablemark/html-react-parser/releases/tag/v6.1.0)

**原文标题**: [Release v6.1.0 · remarkablemark/html-react-parser · GitHub](https://github.com/remarkablemark/html-react-parser/releases/tag/v6.1.0)

概述总结
- 📦 **v6.1.0 版本发布**：最新版本于2026年5月5日发布，由github-actions自动发布。
- 🔒 **安全增强**：新增CSP（内容安全策略）支持，通过`trustedTypePolicy`选项实现。
- 👤 **贡献者**：本次更新由@remdex贡献代码（提交ID: 0fd3aa0）。
- ✅ **已验证签名**：提交使用GitHub签名验证，GPG密钥ID为B5690EEEBB952194。
- ⚠️ **页面加载问题**：页面提示加载错误，建议重新加载。

---

### [别再冻结你的React应用了，试试这个背景技巧 - YouTube](https://www.youtube.com/watch?v=mOncu3xCllw)

**原文标题**: [STOP freezing your React apps, use this Background Trick instead - YouTube](https://www.youtube.com/watch?v=mOncu3xCllw)

本頁面列出了 YouTube 平台相關的各項資訊與政策連結。
- 📰 **新聞中心**：提供 YouTube 的最新消息與公告。
- ©️ **版權**：說明平台上的版權規範與相關權益。
- 📞 **聯絡我們**：提供用戶與 YouTube 團隊聯繫的管道。
- 🎨 **創作者**：針對內容創作者提供的資源與支援。
- 📢 **刊登廣告**：說明在 YouTube 上投放廣告的相關資訊。
- 👨‍💻 **開發人員**：提供給開發者的技術文件與工具。
- 📜 **條款**：列出使用 YouTube 服務時需遵守的條款。
- 🔒 **私隱**：說明 YouTube 如何收集與使用用戶資料。
- 🛡️ **政策及安全**：涵蓋平台的安全政策與內容規範。
- ⚙️ **YouTube 的運作方式**：解釋平台的推薦系統與運作機制。
- 🧪 **測試新功能**：介紹 YouTube 正在測試的新功能。
- ©️ **© 2026 Google LLC**：顯示版權歸屬於 Google 公司。

---

### [五分钟深度解析：React 服务端组件 - YouTube](https://www.youtube.com/watch?v=5QM7XjbqDug)

**原文标题**: [Five Minute Deep Dive: React Server Components - YouTube](https://www.youtube.com/watch?v=5QM7XjbqDug)

YouTube 相關資訊與政策總覽
- 📰 新聞中心：提供官方新聞與公告
- ©️ 版權：說明內容使用與保護規則
- 📞 聯絡我們：提供用戶聯繫管道
- 🎨 創作者：支援內容創作者的資源
- 📢 刊登廣告：廣告投放與合作資訊
- 👨‍💻 開發人員：技術開發相關指引
- 📜 條款：使用條款與規範
- 🔒 私隱：個人資料保護政策
- 🛡️ 政策及安全：平台安全與內容政策
- ⚙️ YouTube 的運作方式：平台運作機制說明
- 🧪 測試新功能：新功能測試資訊
- ©️ 2026 Google LLC：版權歸屬聲明

---

### [我黑了一个TanStack Start应用... - YouTube](https://www.youtube.com/watch?v=XSmpScSiPhw)

**原文标题**: [I hacked a TanStack Start app... - YouTube](https://www.youtube.com/watch?v=XSmpScSiPhw)

本頁面列出了 YouTube 平台相關的資訊與政策連結，涵蓋公司資訊、法律條款及功能說明。

- 📰 新聞中心：提供 YouTube 官方新聞與公告
- ©️ 版權：說明版權相關規範與申訴機制
- 📞 聯絡我們：提供用戶與創作者聯繫 YouTube 的方式
- 🎬 創作者：針對內容創作者提供的資源與指南
- 📢 刊登廣告：說明廣告投放選項與合作方式
- 👨‍💻 開發人員：提供 API 及技術開發文件
- ⚖️ 條款：列出使用 YouTube 的服務條款
- 🔒 私隱：說明用戶資料收集與使用政策
- 🛡️ 政策及安全：涵蓋社群規範與安全措施
- ⚙️ YouTube 的運作方式：解釋平台推薦與審核機制
- 🧪 測試新功能：介紹正在測試中的新功能
- 📅 © 2026 Google LLC：版權歸屬與年份標示

---

### [TanHacked - 语法 #1004](https://syntax.fm/show/1004/tanhacked)

**原文标题**: [TanHacked - Syntax #1004](https://syntax.fm/show/1004/tanhacked)

本集讨论了名为“Mini Shai-Hulud”的供应链攻击，该攻击通过GitHub Actions缓存投毒，入侵了TanStack等流行npm包，并利用Claude Code钩子和VS Code任务自我传播、窃取凭证。主持人还介绍了开发者如何通过pnpm安全默认设置、开发容器等策略进行防御。

- 🐛 攻击概述：一种名为“Mini Shai-Hulud”的供应链攻击，通过GitHub Actions缓存投毒，入侵了TanStack等流行npm包，形成自我传播的蠕虫。
- 🔑 攻击机制：利用GitHub Actions缓存漏洞，注入恶意代码，窃取凭证，并通过Claude Code钩子和VS Code任务持续传播。
- 🛡️ 防御措施：推荐使用pnpm的安全默认设置（如阻止异类子依赖）、开发容器（Dev Containers）以及“死机开关”（Dead Man’s Switch）等实用策略。
- 📦 包管理器角色：强调包管理器在安全中的关键作用，如pnpm的“Block Exotic Subdeps”功能可防止恶意依赖。
- 💡 实用建议：主持人Scott分享了自己的安全审查经验，并鼓励开发者采用开发容器隔离环境，降低风险。

---

### [细致AI - 无需编写测试的自动化前端测试](https://www.meticulous.ai/?utm_source=thisweekinreact&utm_medium=newsletter&utm_campaign=26q2&utm_content=2nd)

**原文标题**: [Meticulous AI - Automated Frontend Testing Without Writing Tests](https://www.meticulous.ai/?utm_source=thisweekinreact&utm_medium=newsletter&utm_campaign=26q2&utm_content=2nd)

该平台提供零开发工作量的自动化、穷尽式测试方案，通过记录用户交互并利用AI生成全面测试套件，确保代码变更无回归缺陷。

- 🤖 **零开发工作量**：只需添加脚本标签，即可自动记录开发、预发布环境中的用户交互，无需编写或维护测试代码。
- 🔍 **穷尽式测试覆盖**：AI引擎根据代码分支执行情况，生成覆盖所有用户流程和边缘案例的视觉端到端测试套件。
- ⚡ **即时回归检测**：提交PR时自动模拟后端响应，在合并前预测变更对用户工作流的影响，无假阳性且无需特殊测试账户。
- 🛠️ **自动演化测试**：测试套件随应用更新自动增删，确保始终与最新功能匹配，开发者无需干预。
- 🚫 **零脆性测试**：基于Chromium确定性调度引擎构建，彻底消除测试脆性，执行速度极快，适用于复杂应用。
- 🏢 **企业级信任**：已获Dropbox、Notion等超100家组织采用，开发者反馈“无法想象没有它”。
- 🔄 **灵活集成**：可补充或替代现有测试套件，支持NextJS、React、Vue、Angular等主流框架，测试结果在120秒内返回。

---

### [测试前端——Palantir百万行TypeScript的经验教训](https://www.meticulous.ai/blog/lessons-from-a-decade?utm_source=thisweekinreact&utm_campaign=26q2&utm_content=2nd)

**原文标题**: [Testing Frontend — Lessons from over a million lines of TypeScript at Palantir](https://www.meticulous.ai/blog/lessons-from-a-decade?utm_source=thisweekinreact&utm_campaign=26q2&utm_content=2nd)

概述总结  
- 🧪 **测试策略的核心**：正确的前端测试能成倍提升工程速度，但多数手动测试反而拖慢团队，关键在于降低测试维护成本。  
- 📦 **单元测试要选对“最小切面”**：测试应覆盖足够复杂的逻辑单元，沿稳定API边界划分，避免测试内部实现细节，减少因重构导致的频繁更新。  
- 🚫 **避免过度依赖组件测试**：如Enzyme测试，因UI频繁变动而脆弱，建议将复杂逻辑抽离为独立函数测试，降低维护负担。  
- 🔗 **利用稳定API构建可扩展的集成测试**：识别应用中变化少的API，设计测试框架使新增测试只需添加数据文件，实现“一次编写，永不维护”。  
- 🎯 **手动测试的优先级**：优先测试复杂逻辑的单元测试，辅以少量集成测试和端到端冒烟测试，避免追求100%覆盖率。  
- 🔄 **自动化测试的未来**：通过记录开发者的日常操作流（如本地预览），自动生成并维护接近100%代码覆盖的视觉快照测试，消除手动维护成本。

---

### [重绘](https://wcandillon.github.io/redraw/)

**原文标题**: [Redraw](https://wcandillon.github.io/redraw/)

本页面介绍了 Renderful 的矢量图形渲染功能，强调通过 GPU 编译的 TypeScript 函数实现动态、几何感知的描边和颜色控制，以及基于矢量的柔和效果和物理渲染。

- 🖌️ **动态描边**：描边宽度和颜色由 TypeScript 函数控制，在 GPU 上编译执行，可根据路径几何信息实现动态、几何感知的描边效果。
- 🎨 **路径颜色插值**：颜色同样由 TypeScript 函数控制，支持沿路径插值十一色调色板，实现几何感知的填充和描边颜色。
- 🌫️ **矢量羽化**：基于矢量几何计算软距离模糊，无需光栅化或后期处理，可在单一着色器中合成羽化图层，如毛玻璃效果。
- ✨ **扁平 UI 元素**：通过路径几何生成动态高光和反射，实现扁平 UI 元素的丰富视觉效果。
- 💡 **物理渲染**：将光照、菲涅尔效应和 GGX 高光引入 2D 路径，使描边和形状呈现陶瓷、金属或玻璃等材质效果，无需离开矢量管线。
- 📚 **资源与文档**：提供文档和示例，支持在编辑器中直接打开和探索。

---

### [《一起画》- YouTube](https://www.youtube.com/watch?v=nGLCmY7tdz4)

**原文标题**: [Drawn Together - YouTube](https://www.youtube.com/watch?v=nGLCmY7tdz4)

本頁面為 YouTube 平台的資訊與政策總覽，涵蓋版權、聯絡方式、創作者支援、廣告、條款、私隱及安全等核心內容，並標示版權歸屬 Google。

- 📰 新聞中心：提供 YouTube 官方新聞與公告
- ©️ 版權：說明版權相關政策與規範
- 📞 聯絡我們：提供使用者聯繫 YouTube 的管道
- 🎬 創作者：為內容創作者提供資源與支援
- 📢 刊登廣告：介紹廣告刊登選項與合作方式
- 👨‍💻 開發人員：提供開發者相關工具與 API 資訊
- 📜 條款：列出使用 YouTube 的服務條款
- 🔒 私隱：說明隱私權保護政策
- 🛡️ 政策及安全：涵蓋平台安全與使用規範
- ⚙️ YouTube 的運作方式：解釋平台功能與運作機制
- 🧪 測試新功能：介紹正在測試的新功能
- ©️ 2026 Google LLC：標示版權歸屬與年份

---

### [TypeGPU – 类型安全的WebGPU工具包](https://docs.swmansion.com/TypeGPU/)

**原文标题**: [TypeGPU – Type-safe WebGPU toolkit](https://docs.swmansion.com/TypeGPU/)

TypeGPU 是一个增强 WebGPU API 的 TypeScript 库，以类型安全、声明式方式管理资源，支持 GPU 渲染与计算。

- 🚀 类型安全声明式：通过 TypeScript 类型系统，以声明式方式管理 WebGPU 资源，提升代码可靠性。
- 🔢 轻松编解码：利用 typed-binary 技术，无需手动处理字节，简化 GPU 程序数据读写。
- 🧩 组合数据类型：轻松描述结构体、数组等复杂数据类型，TypeScript 自动验证输入输出数据。
- 📱 支持 React Native：基于 react-native-wgpu 库，可在 React Native 上运行。
- 📋 路线图清晰：逐步实现数据结构与缓冲区（v0.1）、绑定组（v0.2）、链接器（v0.3）、函数（v0.6）、管线及命令式代码，追求端到端类型安全。
- 💬 社区参与：通过 GitHub Discussions 和 Discord 服务器参与开发讨论。
- 🎯 立即尝试：开始使用 TypeGPU，重塑 GPU 渲染与计算体验。

---

### [使用Sentry追踪优化React Native结账性能 | Sentry](https://sentry.io/cookbook/track-checkout-performance-react-native/?utm_source=thisweekinreact&utm_medium=paid-community&utm_campaign=&utm_content=newsletter-rn-link-rn-checkout-learnmore)

**原文标题**: [Fix Checkout Performance in React Native with Sentry Tracing | Sentry](https://sentry.io/cookbook/track-checkout-performance-react-native/?utm_source=thisweekinreact&utm_medium=paid-community&utm_campaign=&utm_content=newsletter-rn-link-rn-checkout-learnmore)

本指南介紹如何在 React Native 應用程式中，使用 Sentry 追蹤結帳流程的效能，並找出並修復緩慢的 HTTP 請求，同時設定警示與儀表板以監控效能回歸。

- 📱 **啟用追蹤與傳播目標**：在 React Native 中初始化 Sentry SDK，設定 `tracesSampleRate` 大於零，並將 `tracePropagationTargets` 包含 Python 後端 URL，以建立分散式追蹤。
- ⏱️ **記錄完整顯示時間**：使用 `Sentry.TimeToFullDisplay` 元件，並傳入布林值來標記結帳畫面內容（如產品）是否已完全載入，以追蹤完整顯示時間 (TTFD)。
- 🛠️ **建立自訂區段**：使用 `Sentry.startSpan` 包裝關鍵操作（如目錄載入與結帳流程），並傳入屬性（如購物車項目數與總額），以便後續在 Trace Explorer 中搜尋與過濾。
- 📊 **檢視行動洞察**：在 Sentry 的 Mobile Insights 中，查看平均顯示時間、冷啟動時間與交易持續時間，並在 Mobile Vitals 畫面中檢視各畫面的 TTID、TTFD 與載入次數。
- 🔍 **深入分析緩慢交易**：從交易清單中篩選出最慢的交易，點擊進入交易摘要，瀑布圖會顯示所有操作（如 HTTP 請求、UI 載入與自訂區段），找出耗時最長的瓶頸。
- 🧩 **使用 Trace Explorer 探索區段**：在 Trace Explorer 中搜尋導航區段（如 `span.op:navigation`），點擊特定追蹤以查看完整瀑布圖，並可依屬性分組、比較 P50 與 P95 持續時間。
- 🚀 **修復後端端點並驗證**：針對緩慢的後端請求進行最佳化（如快取、查詢最佳化或減少負載），重新部署後重複結帳流程，並在 Trace Explorer 中比較新舊持續時間，使用 Visualize 標籤繪製平均區段持續時間圖表。
- 🔔 **設定結帳緩慢警示**：在 Trace Explorer 中，使用結帳區段篩選條件後，點擊「Save As」並選擇「Alert」，設定臨界值（如平均區段持續時間超過 1 秒），並配置通知動作（如電子郵件或 Slack）。
- 📈 **新增儀表板小工具**：前往 Dashboards，新增小工具，設定資料集為 Spans、Y 軸為 `avg(span.duration)`，並加入 `span.op:checkout.process` 篩選條件，命名後儲存，以監控結帳處理時間。

---

### [RSD 变得安静了——我们能做些什么？· facebook/react-strict-dom · 讨论 #471 · GitHub](https://github.com/facebook/react-strict-dom/discussions/471#discussioncomment-16896278)

**原文标题**: [RSD has gone quiet — what can we do about it? · facebook/react-strict-dom · Discussion #471 · GitHub](https://github.com/facebook/react-strict-dom/discussions/471#discussioncomment-16896278)

React Strict DOM 项目社区讨论其停滞状态及未来方向。

- 🚧 项目已停滞约6个月，上次发布是2025年10月的0.0.54版本，PR和问题积压未处理。
- 🎯 核心愿景受认可：基于Web标准编写跨平台组件，但缺少SVG支持、StyleX依赖更新、TypeScript类型、虚拟化模式及无障碍等关键功能。
- 💬 社区成员表达担忧：包括企业设计系统团队、130kLOC应用迁移者等，希望得到Meta或维护者的明确更新。
- 👤 主要维护者@necolas已离开Meta，导致项目进展缓慢；Meta内部RSD仍用于Quest等产品，但非优先项目。
- 🛠️ 社区提议分叉项目或贡献代码；维护者@martinbooth确认项目未废弃，将加强PR审查，但SVG因性能问题暂不添加。
- 📋 社区列出待办事项：升级StyleX依赖、处理虚拟化、无障碍问题、合并react-strict-animated及babel codemod等。
- 🏛️ 讨论将RSD移交至React Foundation的可能性，但需Meta内部评估。

---

### [React Native 的 Pressable 比 Gesture Handler 挂载更快 | Peter Piekarczyk](https://www.peterp.me/articles/react-native-pressable-faster-than-gesture-handler/)

**原文标题**: [React Native's Pressable mounts faster than Gesture Handler's | Peter Piekarczyk](https://www.peterp.me/articles/react-native-pressable-faster-than-gesture-handler/)

### 概述总结
React Native的`Pressable`组件在挂载速度上明显快于Gesture Handler的替代方案，特别是在同时挂载大量可点击元素时。测试显示，使用原生`Pressable`（无论是否配合Reanimated动画）比使用Gesture Handler的组件快约325毫秒。性能瓶颈主要来自Gesture Handler为每个实例注册原生手势处理器的开销，而非动画工作集本身。

- 📊 **性能差距显著**：原生`Pressable`（V3/V4）的平均挂载时间约455毫秒，而Gesture Handler方案（V1/V2）约770毫秒，差距达325毫秒。
- ⚙️ **瓶颈在Gesture Handler**：性能差异源于Gesture Handler为每个实例注册原生手势处理器，100个元素同时挂载时延迟累积明显。
- 🚀 **CSS动画方案最优**：使用Reanimated 4的CSS过渡API（V4）在保持流畅动画的同时，挂载速度与无动画的原生`Pressable`（V3）几乎相同（差异仅2.5毫秒）。
- 🔧 **实际迁移效果**：将100个可点击元素的挂载时间从778毫秒降至453毫秒，且动画效果完全一致。
- 💡 **关键洞察**：大量可点击元素同时挂载时的性能问题，根源通常不在动画逻辑，而在于手势处理器的注册开销。

---

### [React.Activity 的隐性成本 | Peter Piekarczyk](https://www.peterp.me/articles/hidden-cost-of-react-activity/)

**原文标题**: [The hidden cost of React.Activity | Peter Piekarczyk](https://www.peterp.me/articles/hidden-cost-of-react-activity/)

### 概述总结
React.Activity 在隐藏子树时保留状态但销毁副作用，重新显示时重建所有 Effect，这可能导致性能开销，尤其在 Effect 密集的 React Native 应用中。

- 🎭 **Activity 的真实行为**：隐藏时保留状态但销毁 Effects，重新显示时重建 Effects，并非简单的“保持挂载但不可见”
- ⚡ **React Native 的特殊挑战**：移动端代码天然包含大量 Effect（订阅、监听、测量、分析等），重新显示时触发副作用重建风暴
- 🔄 **useEffect + setState 的乘数效应**：同步 setState 在 Effect 中强制额外渲染，复杂屏幕中多个组件同时执行时性能问题放大
- 📦 **生态系统的隐藏成本**：TanStack Query、Jotai 等库依赖 Effect 进行订阅/观察，Activity 隐藏/显示会触发大量重建工作
- 🏗️ **密集屏幕问题**：嵌套设计系统组件（设置页、结账流程等）的屏幕，每个组件可能包含查询、存储、测量、分析等 Effect
- ⚠️ **危险组合**：大量嵌套组件 + 多个 Effect + 重复订阅 + Effect 驱动本地状态 = Activity 可能将工作从初始挂载转移到用户交互路径
- ✅ **适用场景**：表单、小详情面板、标签内容等子树小、Effect 轻量、用户很快返回的场景
- 🔍 **审计建议**：使用 Activity 前检查子树中的 Effect 模式，特别是立即调用 setState 的 Effect、挂载时逻辑、重复订阅和测量
- 💡 **核心洞察**：Activity 保留状态但测试 Effect 卫生，重新显示时若感觉像重挂载风暴，那确实就是

---

### [遇见Argent：用于控制、调试和分析iOS应用的智能工具包 | Software Mansion](https://swmansion.com/blog/argent-agentic-toolkit-to-control-debug-and-profile-ios-applications/)

**原文标题**: [Meet Argent: Agentic Toolkit to Control, Debug and Profile iOS applications | Software Mansion](https://swmansion.com/blog/argent-agentic-toolkit-to-control-debug-and-profile-ios-applications/)

### 概述总结
Argent 是一款为 iOS 模拟器提供直接访问权限的代理工具包，使 AI 编码代理能自主运行、检查、调试和性能分析 iOS 及 React Native 应用，形成闭环工作流。

- 🤖 **自主控制模拟器**：代理可启动模拟器、启动应用、执行点击、滑动、旋转等 UI 交互，并返回优化截图，支持链式操作以节省令牌。
- 🔍 **深度诊断能力**：代理能检查 React 组件树、评估运行中 JavaScript、读取控制台日志、拦截 HTTP 流量，具备类似 React DevTools 的可见性。
- ⚡ **性能瓶颈定位**：同时记录 React 和原生 iOS 性能分析，交叉关联结果，检测 UI 挂起、渲染级联和内存泄漏，单次捕获可多次查询。
- 🛠️ **实际应用案例**：在银行项目中减少 50% 重渲染，在金融科技中降低 30% 平均渲染时间和 22% 会话时间，在开源库中捕捉回归问题。
- 🚀 **独特优势**：直接与模拟器通信（非 XCUITest），速度快；提供全套诊断工具，代理可在单会话中复现、诊断并修复问题。
- 💻 **安装与使用**：免费开源，通过 `npx @swmansion/argent init` 一分钟安装，支持 Claude Code、Cursor 等主流编码代理，无需额外 API 密钥。

---

### [错误](https://shift.infinite.red/beyond-60-fps-building-a-real-time-can-bus-dashboard-with-nitro-modules-and-skia-d0f564f8d239)

**原文标题**: [Error](https://shift.infinite.red/beyond-60-fps-building-a-real-time-can-bus-dashboard-with-nitro-modules-and-skia-d0f564f8d239)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='shift.infinite.red', port=443): Max retries exceeded with url: /beyond-60-fps-building-a-real-time-can-bus-dashboard-with-nitro-modules-and-skia-d0f564f8d239 (Caused by SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1000)')))

---

### [获取失败](https://medium.com/doctolib/expo-without-eas-scaling-the-react-native-developer-experience-of-an-app-with-90m-users-2694ea841805)

**原文标题**: [Failed to retrieve](https://medium.com/doctolib/expo-without-eas-scaling-the-react-native-developer-experience-of-an-app-with-90m-users-2694ea841805)

无法总结：获取内容失败，状态码 403。

---

### [Expo SDK 56 测试版现已可用 - Expo 更新日志](https://expo.dev/changelog/sdk-56-beta)

**原文标题**: [Expo SDK 56 Beta is now available - Expo Changelog](https://expo.dev/changelog/sdk-56-beta)

SDK 56 测试版现已开始，为期约两周，包含多项重大更新和性能改进。

- 🎉 SDK 56 测试版开始，持续约两周，开发者可测试新版本并报告回归问题。
- 🚀 Expo UI 现已稳定，包含通用组件、稳定原生 API 和社区组件替代品，支持跨平台开发。
- ⚡ 预编译 XCFrameworks 加速 iOS 构建，默认启用，可通过环境变量选择退出。
- 🛠️ 内联模块功能允许在项目内直接定义 Expo 模块，简化原生代码实验。
- 📦 `create-expo-module` 重写，支持新技能、平台添加子命令和模块化模板。
- 🔧 运行时性能提升：Kotlin 编译器插件使 Android 冷启动快约 40%，新 JSI 层减少 iOS 调用开销。
- 📱 React Native 0.85.2 和 React 19.2.3，默认使用 Hermes V1，新动画后端，支持 HTTPS 开发服务器。
- 📂 `expo-file-system` 新增下载进度、任务式上传/下载、文件选择多选和文件系统事件监听功能。
- 📊 状态栏和导航栏 API 统一，新增 `<NavigationBar>` 组件和配置插件。
- 📋 新版日历、通讯录和媒体库 API 稳定，采用面向对象设计，支持精细数据获取。
- 📱 iOS 小组件和实时活动稳定，无需预渲染，支持完整环境访问。
- 🤖 AI 友好项目脚手架，包含代理指南和 Expo Skills，支持类型安全配置插件。
- ⚙️ Expo CLI 性能改进：更快的打包器启动、原生 Node.js 监视器、TypeScript 6 支持和 Hermes v1 转换。
- 🧭 Expo Router 不再依赖 React Navigation，新增工具栏、原生堆栈 v5 和 Web 流式 SSR 支持。
- 🏗️ Brownfield 支持多应用隔离、自定义 Turbo 模块和 iOS 预构建。
- 🔧 其他更新：`expo-audio` 新增音频流钩子，`expo-haptics` 支持 Safari 触觉，`expo-sqlite` 支持原生 ArrayBuffer 等。
- 📈 工具版本提升：Xcode 26.4、iOS/tvOS 16.4、macOS 13.4、TypeScript 6.0.3。
- ⚠️ 弃用：`@expo/vector-icons` 替换为 `@react-native-vector-icons/*`，旧版日历、通讯录和媒体库 API 弃用。
- 🔄 重大变更：`expo/fetch` 作为默认 `globalThis.fetch`，`copy()` 和 `move()` 变为异步，`@expo/dom-webview` 成为默认 WebView。
- 📋 如何测试：使用 `npx expo install expo@next --fix` 升级，构建原生应用，并报告问题。

---

### [GitHub - oblador/react-native-swc: ⚡️ 基于SWC的Metro转换器与压缩器](https://github.com/oblador/react-native-swc)

**原文标题**: [GitHub - oblador/react-native-swc: ⚡️ SWC-powered transformer & minifier for Metro · GitHub](https://github.com/oblador/react-native-swc)

这是一个基于SWC的React Native Metro打包器加速工具，用Rust替代Babel实现更快的编译体验。

- 🚀 **高性能替代方案**：作为Metro的Babel转换器替代品，转换速度提升约8倍，整体打包速度提升约3倍
- 🔋 **节能高效**：CPU利用率降低15倍，更省电
- 🔧 **功能完整**：支持HMR、内联require、Platform.select()、常量折叠、delta bundles等Metro核心特性
- 🔤 **多语言支持**：原生支持Flow、TypeScript、ESM、CJS、JSX
- 🧵 **Reanimated支持**：通过自定义SWC插件支持Worklet/Reanimated，无需Babel
- 🔌 **插件生态**：支持SWC插件和process.env内联
- ⚛️ **Expo集成**：提供Expo配置插件，实现无缝集成
- 📦 **安装简单**：通过yarn安装@react-native-swc/core，Reanimated用户额外安装worklets-plugin
- ⚠️ **注意事项**：不支持自定义Babel插件，TypeScript需兼容isolatedModules，Flow自动检测

---

### [使用React Native SDK改进Expo应用的调试 | Sentry博客](https://blog.sentry.io/debugging-expo-react-native-sdk/)

**原文标题**: [Improved debugging for Expo apps with the React Native SDK | Sentry Blog](https://blog.sentry.io/debugging-expo-react-native-sdk/)

本文介绍了 Sentry React Native SDK 针对 Expo 应用的最新调试与性能改进，帮助开发者更高效地监控和排查问题。

- 📱 **自动 OTA 更新上下文**：每个事件自动附带 OTA 更新信息（如频道、版本、更新 ID），无需额外配置，方便按更新渠道过滤问题。
- 🚨 **紧急启动检测**：当 OTA 更新失败回退到内置包时，自动发送警告事件，支持设置告警，及时知晓更新管道问题。
- 🔧 **EAS 构建钩子**：通过简单脚本配置，将构建失败（或成功）事件直接发送到 Sentry，无需手动查看构建日志。
- ⚡ **Expo Router 预取性能**：包装路由后，自动记录预取路由的性能跨度，帮助识别预取慢或无效的路由。
- 📋 **Expo 常量与环境上下文**：自动附带运行环境元数据（如 Expo Go、独立应用、SDK 版本等），完善事件信息。
- 🖼️ **图片与资源加载检测**：自动为 `expo-image` 和 `expo-asset` 的加载操作添加性能跨度，零额外开销。
- 🚀 **快速上手**：OTA 更新和常量上下文默认启用；构建钩子和性能检测仅需少量代码配置，需升级到 SDK 8.10 版本。

---

### [GitHub - mathnotes-app/mobile-ink：生产级React Native墨水引擎，支持原生Skia/Metal绘图与连续画布原语。](https://github.com/mathnotes-app/mobile-ink)

**原文标题**: [GitHub - mathnotes-app/mobile-ink: Production-grade React Native ink engine with native Skia/Metal drawing and continuous canvas primitives. · GitHub](https://github.com/mathnotes-app/mobile-ink)

这是一个由 MathNotes 团队开源的 React Native 高性能手写绘图引擎，专为移动端笔记应用打造，提供原生 Skia/Metal 渲染与连续画布支持。

- 📱 **生产级原生引擎**：采用 iOS 原生 Skia/Metal 渲染，支持 Apple Pencil 低延迟输入，已在 MathNotes 应用中投入生产使用。
- 🎨 **丰富绘图工具**：内置钢笔、荧光笔、蜡笔、书法笔、橡皮擦、选区及形状识别等工具集，满足笔记创作需求。
- 📄 **连续笔记本画布**：提供固定原生引擎池的无限滚动画布，支持动量滚动、捏合缩放及脏页序列化，模拟真实笔记本体验。
- 🚀 **React Native 集成**：专为 React Native 设计，提供 `InfiniteInkCanvas` 等高级组件，需配合 Expo 开发客户端或预构建使用。
- 🛠 **开源社区驱动**：项目旨在成为社区共享的高质量绘图引擎，欢迎初学者提问、提交修复或改进文档，共同完善生态。
- 📋 **序列化与导出**：支持 JSON 笔记本载荷序列化，提供原生页面加载、保存及导出辅助工具，便于数据持久化。
- 🗺 **未来路线图**：近期重点包括完善文档、优化选区变换性能、修复边界缩放问题，并完成 Android 平台功能对齐。

---

### [发布 1.2.0 版本 · margelo/react-native-nitro-fetch · GitHub](https://github.com/margelo/react-native-nitro-fetch/releases/tag/v1.2.0)

**原文标题**: [Release Release 1.2.0 · margelo/react-native-nitro-fetch · GitHub](https://github.com/margelo/react-native-nitro-fetch/releases/tag/v1.2.0)

react-native-nitro-fetch 发布了 v1.2.0 版本，主要新增原生预加载功能和 Web 存根，并修复了 Android 上的同步问题。

- 🚀 **新增原生预加载功能**：由 @riteshshukla04 在 #89 中实现，提升数据加载效率。
- 🔧 **修复 Android 同步问题**：@oferRounds 在 #73 中修复了 Cronet 和 token-refresh 请求与 CookieManager 的同步。
- 🌐 **新增 Web 存根**：@riteshshukla04 在 #90 中添加了 Web 存根，便于测试或开发。
- 👥 **贡献者**：版本由 oferRounds 和 riteshshukla04 共同贡献。
- 📅 **发布日期**：2024年5月7日，基于 v1.1.2 的完整变更日志。

---

### [发布 v0.6.0 · JoaoPauloCMarra/react-native-nitro-markdown · GitHub](https://github.com/JoaoPauloCMarra/react-native-nitro-markdown/releases/tag/v0.6.0)

**原文标题**: [Release v0.6.0 · JoaoPauloCMarra/react-native-nitro-markdown · GitHub](https://github.com/JoaoPauloCMarra/react-native-nitro-markdown/releases/tag/v0.6.0)

概述摘要  
- 📦 发布 react-native-nitro-markdown v0.6.0，集成 RaTeX 作为数学渲染器，并强化原生稳定性。  
- 🔧 将数学渲染从 MathJax/SVG 替换为 RaTeX，解决 issue #45，提升速度与简洁性。  
- 🛠 修复 iOS 构建失败（issue #40），调整 CocoaPods 路径配置以兼容 Expo 55/56。  
- 🧹 统一 iOS/Android 的 MarkdownSession 缓冲区限制为 10MB，增强跨平台一致性。  
- 🗑 清理冗余原生源文件，避免打包错误。  
- ⚙ 优化示例应用：添加共享 UI 组件、更新基准测试标签、调整间距。  
- 📈 更新文档与依赖，移除过时类型定义，对齐 Nitro 模块版本至 0.35.6。

---

### [发布 v0.13.0 · callstackincubator/rock · GitHub](https://github.com/callstackincubator/rock/releases/tag/v0.13.0)

**原文标题**: [Release v0.13.0 · callstackincubator/rock · GitHub](https://github.com/callstackincubator/rock/releases/tag/v0.13.0)

Rock 项目发布 v0.13.0 版本，包含多项新功能、错误修复和文档更新。

- 🚀 新增功能：过滤 xcodebuild 错误以提高可读性
- 💡 新增功能：添加 `--local` 标志提示以跳过缓存
- 🧪 新增功能：实验性支持 CNG 和 Expo 配置插件
- ⚙️ 新增功能：使用 plugin-metro 的 metro 配置，并使配置可选
- 🐛 错误修复：修复 brownfield-ios 中基于 sourceDir 的输出目录设置
- 📱 新增功能：为 `run:ios` 和 `run:android` 命令添加 `--host` 标志支持
- 🛠️ 错误修复：修复 Ruby 3.4.0 上新应用的 iOS 构建问题
- 📚 文档更新：更新过时的链接
- 🔍 新增功能：添加检查 ELF 对齐的命令
- 🔑 新增功能：如果可用，使用 GitHub CLI 进行身份验证，而不是 GITHUB_TOKEN
- 🎨 新增功能：为配置插件添加 Expo 图标支持
- 👥 新贡献者：JakubKorytko、SzaszkowMaksim、lukas-preply 首次贡献

---

### [发布 4.25.0 · software-mansion/react-native-screens · GitHub](https://github.com/software-mansion/react-native-screens/releases/tag/4.25.0)

**原文标题**: [Release 4.25.0 · software-mansion/react-native-screens · GitHub](https://github.com/software-mansion/react-native-screens/releases/tag/4.25.0)

react-native-screens 发布 4.25.0 版本，重点更新了 Tabs API，移除了对旧架构的支持，并新增多项功能与修复。

- 🎉 **Tabs API 稳定版发布**：移除 `freezeContents` 和 `placeholder` 属性，新增 `selectedIcon` 支持，并添加原生 RTL 支持。
- 🛠️ **移除旧架构支持**：不再兼容旧版 React Native 架构，需升级到新架构。
- 🌙 **深色模式支持**：iOS 和 Android 的 Tabs 组件现在支持 `colorScheme` 属性，可适配深色模式。
- 📱 **Android 增强**：新增状态驱动外观、IME 内边距配置、以及 Stack v5 的 header 支持。
- 🐛 **Bug 修复**：修复了多个问题，包括模态框状态更新、返回按钮显示、内存泄漏等。
- 🧹 **代码清理与重构**：移除了大量旧架构相关代码，重构了 Tabs 组件和示例应用结构。
- 🔄 **事件与 API 更新**：`onTabChange` 重命名为 `onTabSelected`，新增 `preventNativeSelection` 支持。
- 🤝 **新贡献者**：欢迎 `ahmedawaad1804`、`l2hyunwoo`、`DavidDuarte22` 等 6 位新贡献者。

---

### [发布 v1.9.0 · callstackincubator/rozenite · GitHub](https://github.com/callstackincubator/rozenite/releases/tag/v1.9.0)

**原文标题**: [Release v1.9.0 · callstackincubator/rozenite · GitHub](https://github.com/callstackincubator/rozenite/releases/tag/v1.9.0)

这是一个关于Rozenite v1.9.0版本发布的摘要，包含主要变更和贡献者信息。

- 🚀 **版本发布**: Rozenite v1.9.0 已发布，包含多项修复和新功能。
- 🐛 **修复Vite插件**: 修复了Vite插件中声明引用的规范化问题。
- 🌐 **修复网络活动插件**: 支持RFC 6839 JSON响应格式。
- 🗑️ **弃用MMKV插件**: 建议使用storage-plugin替代mmkv-plugin。
- 📦 **隔离React Native Nitro Fetch**: 将react-native-nitro-fetch分离到独立的bundle块中。
- 🛠️ **SQLite插件增强**: 导出SQL和桥接辅助函数，支持自定义适配器。
- 🆕 **新增RHF插件**: 实现了新的RHF插件。
- 💾 **存储插件功能**: 添加了存储级别的JSON导入/导出功能。
- 💻 **Vite插件改进**: 改进了开发主机消息检查器。
- 👥 **新贡献者**: burczu 首次贡献于#261。

---

### [React Native Radio - RNR 352 - 与Daniel Williams一起使用Storybook](https://infinite.red/react-native-radio/rnr-352-storybook-with-daniel-williams)

**原文标题**: [React Native Radio - RNR 352 - Storybook with Daniel Williams](https://infinite.red/react-native-radio/rnr-352-storybook-with-daniel-williams)

本集RNR 352邀请Daniel Williams讨论Storybook 10的新特性、AI集成及React Native开发趋势。

- 🚀 **Storybook 10核心更新**：捆绑包体积减少30%，移除CommonJS支持，采用ESM，提升性能并简化React Native集成。
- 🧩 **CSF Next语法**：推出更类型安全的Story语法（CSF Factories），React Native支持尚在PR中，预计版本11全面支持。
- 🤖 **MCP服务器（10.3版本）**：支持AI代理工作流，可远程控制Storybook、获取组件文档和状态，结合Figma MCP实现设计系统自动化。
- 📱 **React Native视觉回归测试**：Chromatic正在开发官方解决方案，当前可通过Maestro、Detox等工具结合Storybook远程控制实现截图测试。
- 🔧 **Repack集成**：Daniel Williams接管Repack（React Native微前端打包器），并开发Storybook插件，优化模块联邦和团队协作。
- 🎨 **设计系统协作**：Storybook用于展示组件状态和文档，支持与Figma变量联动，未来可通过AI工具（如Claude）自动生成组件。
- 🏢 **多Storybook架构**：推荐为设计系统和应用屏幕分别创建Storybook，或使用Storybook Connect功能合并，适应不同团队需求。
- 🌟 **社区与资源**：Daniel Williams在葡萄牙波尔图创办React Native OPO社区，定期举办线下活动；可通过Twitter（@Danny__W）关注最新动态。

---

### [05.md](https://raw.githubusercontent.com/tc39/agendas/main/2026/05.md)

**原文标题**: [05.md](https://raw.githubusercontent.com/tc39/agendas/main/2026/05.md)

本次会议为 Ecma TC39 第114次会议，将于2026年5月19日至21日在荷兰阿姆斯特丹的JetBrains举行。会议议程涵盖多项提案的推进、讨论和状态更新，涉及ECMAScript语言规范的多个方面。

- 📅 会议时间：2026年5月19日至21日，每天10:00至17:00（最后一天至16:00），地点为阿姆斯特丹。
- 📋 议程规则：提案需在截止日期前添加，并附上支持材料，否则可能无法推进。
- 🚀 提案推进：多个提案寻求阶段推进，包括Joint Iteration（至阶段4）、Decorators（至阶段2.7）、Iterator Join（至阶段3）等。
- 🔄 状态更新：Temporal、Explicit Resource Management、AsyncContext等提案将进行进展汇报。
- 🆕 新提案：Amount、Stable Formatting、Default Behaviours等提案寻求阶段0或阶段1的反馈。
- ⏰ 时间约束：部分演讲者有特定时间偏好，如Guy Bedford仅下午3点后可用，Eemeli Aro希望某些演讲按顺序安排。
- 🛠️ 工具与讨论：将讨论规范导航工具、正则表达式提案影响、欧盟CRA法规等议题。
- 📜 其他事项：包括会议开场、秘书报告、编辑报告、任务组报告、行为准则更新等。

---

### [宣布 Rolldown 1.0 | VoidZero](https://voidzero.dev/posts/announcing-rolldown-1-0)

**原文标题**: [Announcing Rolldown 1.0 | VoidZero](https://voidzero.dev/posts/announcing-rolldown-1-0)

Rolldown 1.0 稳定版发布，这是一个基于 Rust 的高性能 JavaScript 打包工具，速度比 Rollup 快 10-30 倍，兼容 Rollup 插件 API，并具备独特功能，现已作为 Vite 8 的默认打包器。

- 🚀 **性能卓越**：Rolldown 基于 Rust 和 Oxc 构建，速度与 esbuild 相当，比 Rollup 快 10-30 倍，Ramp 等公司已实现 57% 的构建时间缩减。
- 🔌 **Rollup 插件兼容**：支持 Rollup 插件 API，大多数 Vite 插件可直接在 Vite 8 中使用，并通过钩子过滤器和内置插件提升性能。
- 🧩 **独特打包功能**：提供更激进的死代码消除、细粒度代码分割（如 webpack 风格的分块规则），以及更小的默认输出包。
- 🛠️ **使用方式灵活**：可独立使用（通过 npm 安装 rolldown），也可通过 Vite 8 的 `build.rolldownOptions` 配置，无需代码更改即可从 RC 升级。
- 📅 **开发历程**：从 2024 年 4 月首次公开到 2026 年 5 月 1.0 稳定版，历经两年，包括 Vite 8 集成和广泛测试。
- 🔮 **未来计划**：包括 Vite 全捆绑模式（提升开发启动速度 3 倍）和惰性桶优化（仅编译实际使用的模块）。
- 🙌 **社区贡献**：感谢约 200 名贡献者和早期采用者，欢迎参与文档、插件兼容性测试和 GitHub 上的“好初试问题”。

---

### [Node.js — Node.js 26.1.0（当前版本）](https://nodejs.org/en/blog/release/v26.1.0)

**原文标题**: [Node.js — Node.js 26.1.0 (Current)](https://nodejs.org/en/blog/release/v26.1.0)

Node.js 26.1.0 版本发布，包含实验性 FFI 模块、多项新功能及大量改进。

- 🧪 新增实验性 `node:ffi` 模块，支持从 JavaScript 加载动态库和调用原生符号，需 `--experimental-ffi` 标志
- 📦 `buffer` 模块新增 `end` 参数，增强字符串搜索功能
- 🔐 `crypto` 模块新增 `randomUUIDv7()` 方法，并支持 `crypto.diffieHellman()` 接受密钥数据
- 🐛 `debugger` 新增编辑时运行时表达式探测功能
- 📁 `fs` 模块为 `fs.stat()` 添加 `signal` 选项，并暴露 `statfs` 的 `frsize` 字段
- 🌐 `http` 模块为 `IncomingMessage` 添加 `req.signal`，并强化 `ClientRequest` 选项合并
- ⚙️ `process` 模块在 `execve(2)` 失败时抛出错误而非中止进程
- 🧪 `test_runner` 支持测试顺序随机化、模拟定时器及 `AbortSignal.timeout`
- 🎨 `util` 模块支持使用十六进制颜色代码为文本着色
- 🔧 多项依赖更新，包括 OpenSSL 3.5.6、npm 11.13.0、V8 14.6.202.34 等

---

### [Meta: 原生支持 ES 模块 · 问题 #9430 · jestjs/jest · GitHub](https://github.com/jestjs/jest/issues/9430#issuecomment-4400281169)

**原文标题**: [Meta: Native support for ES Modules · Issue #9430 · jestjs/jest · GitHub](https://github.com/jestjs/jest/issues/9430#issuecomment-4400281169)

该议题概述了Jest对ES模块（ESM）原生支持的实现计划与当前状态。

- 📌 核心目标：在Jest中实现ESM原生支持，利用Node.js的`vm` API（需`--experimental-vm-modules`标志）
- 🔧 模块上下文：需在`vm.Context`中运行ESM，需在模块构建时访问上下文（已提交PR #9428）
- 🌐 全局变量：`expect`、`test`等全局变量保持不变，但`jest`全局属性需移至`import.meta`或通过`@jest/globals`导入
- 🚫 `jest.mock`限制：静态导入不支持`jest.mock`，仅动态导入可工作；可能需将`import`转换为`import()`并配合顶层`await`
- 🔗 模块链接：通过自定义`linker`实现模块转换和模拟（支持`__mocks__`目录），无需loader API
- 📂 文件检测：通过`package.json`的`type`字段或文件扩展名判断ESM/CJS模式
- ⚙️ 配置支持：`jest.config.mjs`需通过`import()`异步加载，可能需在Jest 25中实现异步配置解析
- 🧪 代码覆盖率：不受影响，仍可通过Babel转换源码和V8覆盖率收集
- 🚀 性能优化：ESM中`extraGlobals`选项不再适用，需解决全局变量访问性能问题（已提交Node.js issue）
- 📦 其他功能：支持`import.meta`、`package exports`、JSON/WASM模块、`module.createRequire`等

---

### [Bun v1.3.14 | Bun 博客](https://bun.com/blog/bun-v1.3.14)

**原文标题**: [Bun v1.3.14 | Bun Blog](https://bun.com/blog/bun-v1.3.14)

## 概述

Bun 发布了重大更新，包含内置图像处理 API、HTTP/3 支持、性能大幅提升和大量 Bug 修复。

- 🖼️ **内置图像处理** - Bun.Image 支持 JPEG、PNG、WebP 等格式，无需安装原生模块，性能比 sharp 快 1.2-70 倍
- 🚀 **HTTP/3 (QUIC) 支持** - Bun.serve 新增实验性 HTTP/3，性能比 HTTPS/1.1 快 2.7 倍，静态路由达 509,135 req/s
- ⚡ **实验性 HTTP/2 和 HTTP/3 客户端** - fetch() 支持多路复用连接，共享 TLS 握手，支持协议选择
- 📂 **全局虚拟存储** - bun install 新增 globalStore 选项，安装速度提升 7 倍，消除所有 clonefileat 调用
- 🔍 **重写 fs.watch()** - 支持递归监控新目录，修复 macOS 双线程问题，Linux 上删除重建文件正确触发事件
- 🛡️ **--no-orphans 模式** - 父进程死亡时自动退出，并递归终止所有子进程，支持 Linux 和 macOS
- 🔄 **process.execve() 支持** - 实现 Node.js v24 API，替换当前进程映像
- 🖥️ **Windows ConPTY 支持** - Bun.Terminal 和 Bun.spawn 现在在 Windows 上通过 ConPTY API 工作
- 📉 **内存优化** - 共享 SSL_CTX 缓存，MongoDB/Mongoose 内存使用大幅降低，RSS 从 1GB 降至 168MB
- 🎯 **JavaScriptCore 升级** - 565 个上游提交，异步函数、JSON.parse、数组操作等性能提升
- 📦 **bun publish 改进** - 自动发送 README 元数据到注册表
- 🗄️ **SQLite 升级至 3.53.0** - 新增浮点精度控制和解析器深度限制
- 🔧 **跨语言 LTO** - Zig↔C++ 全链接时优化，HTTP 吞吐量提升 3.5%
- ⚙️ **ESM 加载加速** - 修复解析器性能问题，模块加载速度提升约 12%
- 🧹 **减少 GC 开销** - 消除 63 种内置对象的冗余重新扫描
- 📏 **二进制体积缩小** - Windows 减少 17-18MB，Linux 减少 6-9MB
- 🔐 **TLS 系统证书改进** - tls.getCACertificates('system') 无需 --use-system-ca，修复 macOS 卡顿问题
- 🐛 **大量 Bug 修复** - 修复内存泄漏、崩溃、安全漏洞等数百个问题，涵盖 Node.js 兼容性、Bun API、Web API、Worker、定时器等
- 🧪 **bun test 改进** - 修复隔离测试崩溃、测试表数组 GC 问题等
- 🛠️ **Bun Shell 修复** - 修复 70 多个 Bug，包括 cd 挂起、路径过长崩溃等
- 🏗️ **Windows 修复** - 修复命名管道崩溃、路径规范化溢出、子进程清理崩溃等

---

### [发布 v11.14.0 · npm/cli · GitHub](https://github.com/npm/cli/releases/tag/v11.14.0)

**原文标题**: [Release v11.14.0 · npm/cli · GitHub](https://github.com/npm/cli/releases/tag/v11.14.0)

npm CLI v11.14.0 版本发布，包含新功能、错误修复及依赖更新。

- 🎉 新增 `allow-directory`、`allow-file` 和 `allow-remote` 功能（#9288）
- 🐛 修复 SBOM 中每个节点的 dependsOn/relationships 重复问题（#9318）
- 📦 更新依赖：socks@10.1.1、ip-address@10.1.1、cidr-regex@5.0.5
- 🧹 开发依赖更新及添加 cli-triage 团队作为代码所有者（#9320）
- 🛠️ 工作空间更新：@npmcli/arborist@9.5.0、@npmcli/config@10.9.0 等
- 👥 贡献者：wraithgar、owlstronaut、mikaelkristiansson

---

### [发布 v1.60.0 · microsoft/playwright · GitHub](https://github.com/microsoft/playwright/releases/tag/v1.60.0)

**原文标题**: [Release v1.60.0 · microsoft/playwright · GitHub](https://github.com/microsoft/playwright/releases/tag/v1.60.0)

Playwright v1.60.0 版本发布，带来了多项新功能和改进。

- 🌐 HAR 录制功能：通过 `tracing.startHar()` 和 `tracing.stopHar()` 提供一流的 HAR 录制 API，支持 `await using` 语法自动完成录制。
- 🪝 新增 `locator.drop()` API：模拟外部拖放文件或剪贴板数据到元素上，支持跨浏览器测试上传区域。
- 🎯 Aria 快照增强：`expect(page).toMatchAriaSnapshot()` 现在支持在 Page 上使用，新增 `boxes` 选项可附加元素边界框信息。
- 🛑 新增 `test.abort()`：允许在测试中从 fixture、钩子或路由处理器中立即中止测试并附带消息。
- 🔧 新 API：包括 `browser.on('context')` 事件、`browserContext` 页面生命周期事件镜像、`getByRole()` 的 `description` 选项、`toHaveCSS()` 的 `pseudo` 选项等。
- 🛠️ 其他改进：HTML 报告器支持直接打开 `.zip` 文件、Trace Viewer 新增 JSON 格式化切换、测试运行器新增 `{testFileBaseName}` 令牌等。
- ⚠️ 破坏性变更：移除了长期弃用的 API，如 `Locator.ariaRef()`、`handle` 选项、`logger` 选项和 `videosPath` 选项。
- 🌐 浏览器版本：Chromium 148.0.7778.96、Firefox 150.0.2、WebKit 26.4，并测试了 Google Chrome 147 和 Microsoft Edge 147。

---

### [pnpm 11.1 | pnpm](https://pnpm.io/blog/releases/11.1)

**原文标题**: [pnpm 11.1 | pnpm](https://pnpm.io/blog/releases/11.1)

### 概述总结
pnpm 11.1 版本新增了 `pnpm audit signatures`、`pnpm bugs` 和 `pnpm owner` 等命令，支持从任意命名注册表安装包（包括内置的 GitHub Packages npm 注册表别名），并允许在 CI 中跳过运行时安装，同时修复了多个问题。

- 🔍 **新增 `pnpm audit signatures` 命令**：验证已安装包的 ECDSA 注册表签名，支持作用域注册表，跳过未发布签名密钥的注册表。
- 🏷️ **支持命名注册表（含内置 `gh:` 别名）**：可通过 `gh:` 前缀从 GitHub Packages npm 注册表安装包，并支持在 `pnpm-workspace.yaml` 中配置额外别名或覆盖内置别名。
- 📋 **`pnpm sbom` 新增 `--sbom-spec-version` 标志**：可选择 CycloneDX 规范版本（1.5、1.6 或 1.7，默认 1.7），仅适用于 `--sbom-format cyclonedx`。
- ⏭️ **新增 `--no-runtime` 标志用于 CI 矩阵**：跳过安装运行时条目（如 Node.js），不修改锁文件，适用于外部预置运行时的 CI 环境。
- 🐛 **新增 `pnpm bugs` 命令**：在浏览器中打开包的 bug 跟踪器 URL，支持无参数（读取当前项目）或指定包名。
- 👥 **新增 `pnpm owner` 命令**：管理注册表上的包所有者，支持列出、添加和删除操作。
- 📝 **`pnpm view` 输出增强**：现在显示“published X ago by Y”信息，便于与 `minimumReleaseAge` 比较。
- 🔧 **`pnpm publish` 修复代理问题**：在基于 Web 的身份验证流程中，现在正确使用 HTTP/HTTPS 代理（包括环境变量）。
- 📦 **`pnpm add -g` 行为变更**：默认将每个空格分隔的包安装到独立目录，逗号分隔的包则捆绑安装。
- 🛠️ **`pnpm runtime set` 修复工作区根目录错误**：在多包工作区根目录中设置运行时不再触发 `ADDING_TO_ROOT` 错误。
- 🚀 **修复 `pnpm --version` 挂起问题**：版本打印后不再因工作池未关闭而挂起。

---

### [Tailwind CSS v4.3：滚动条、新颜色等 - Tailwind CSS](https://tailwindcss.com/blog/tailwindcss-v4-3)

**原文标题**: [Tailwind CSS v4.3: Scrollbars, new colors, and more - Tailwind CSS](https://tailwindcss.com/blog/tailwindcss-v4-3)

Tailwind CSS v4.3 和 v4.2 版本发布了大量新功能和改进，包括新调色板、性能优化和实用工具。

- 🎨 **新增四种中性调色板**：v4.2 引入了 mauve、olive、mist 和 taupe 调色板，为设计提供更多中性色调选择。
- ⚡ **Webpack 专属插件**：v4.2 的 `@tailwindcss/webpack` 插件使构建速度提升 2 倍以上，特别适合 Next.js 等框架。
- 📐 **逻辑属性工具**：新增 padding、margin、inset 等逻辑属性工具，支持不同书写模式和方向。
- 🔤 **字体特性控制**：`font-features-*` 工具允许直接控制 OpenType 字体特性，无需自定义 CSS。
- 📜 **滚动条样式工具**：v4.3 新增 `scrollbar-*` 工具，可控制滚动条宽度、颜色和槽位。
- 📦 **容器大小查询**：`@container-size` 工具支持基于块大小的容器查询。
- 🔍 **缩放工具**：`zoom-*` 工具支持 CSS zoom 属性，可缩放元素。
- 🖥️ **制表符宽度控制**：`tab-*` 工具可控制制表符渲染宽度，适用于代码展示。
- 🔗 **增强的 @variant 支持**：支持堆叠和复合变体，在 CSS 中更灵活地应用样式。
- 🛠️ **功能工具默认值**：`--default()` 参数允许工具在无值时使用默认值，提升 API 一致性。

---

### [Astro 6.3 | Astro](https://astro.build/blog/astro-630/)

**原文标题**: [Astro 6.3 | Astro](https://astro.build/blog/astro-630/)

Astro 6.3 发布，带来实验性高级路由、外部图片重定向支持及SVG处理安全改进。

- 🚀 实验性高级路由：允许开发者完全控制请求管道，可组合独立处理器、集成Hono等框架，自定义执行顺序。
- 🔄 外部图片URL重定向支持：Astro现在可追踪最多10次重定向，并验证每个URL是否在允许列表中，否则抛出错误。
- 🛡️ SVG图片处理默认禁用：为安全考虑，Sharp图片服务不再默认处理SVG，需手动启用`dangerouslyProcessSVG`选项。
- 🔧 其他改进：新增`AstroCookies.consume()`方法，用于标记已消费的cookie并返回Set-Cookie头值。
- 📦 升级方式：推荐使用`@astrojs/upgrade` CLI工具，或通过npm/pnpm/yarn手动升级到最新版本。
- 👥 社区贡献：列出核心团队及34位社区贡献者，并推广新Astro周边商品。

---

