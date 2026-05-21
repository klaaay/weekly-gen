### [细致 AI - 无需编写测试的自动化前端测试](https://www.meticulous.ai/?utm_source=thisweekinreact&utm_medium=newsletter&utm_campaign=26q2&utm_content=1st)

**原文标题**: [Meticulous AI - Automated Frontend Testing Without Writing Tests](https://www.meticulous.ai/?utm_source=thisweekinreact&utm_medium=newsletter&utm_campaign=26q2&utm_content=1st)

Meticulous 是一款无需开发者编写代码即可实现自动化、全面且确定性测试的工具，专为复杂代码库设计，能大幅提升代码发布速度。

- 🚀 **零开发者工作**：自动录制开发中的交互，生成覆盖所有代码分支和用户流程的测试套件，无需手动编写或维护测试。
- 🔍 **全面且确定性**：基于 Chromium 的确定性调度引擎，消除测试不稳定性，支持快速并行测试（1000+ 屏幕在 120 秒内完成）。
- 🛡️ **无副作用测试**：通过模拟后端响应（保存并重放原始记录），避免数据变化导致的误报，无需特殊测试账户或模拟数据。
- 🔄 **自动演进**：测试套件随应用自动更新，新增功能或边缘案例时自动添加测试，过时测试自动移除，保持始终最新。
- ⚡ **极速迭代**：大幅提升无回归代码的发布速度，支持与现有测试套件互补或完全替代。
- 🔧 **集成简便**：支持 NextJS、React、Vue、Angular 等主流框架，只需添加脚本标签即可在开发、预发布和预览环境中使用。
- 🏢 **企业级信任**：已被 Dropbox、Notion 等超过 100 家组织采用，工程师反馈“无法想象没有它的工作方式”。

---

### [Meticulous AI - 无需编写测试的自动化前端测试](https://www.meticulous.ai/?utm_source=thisweekinreact&utm_medium=newsletter&utm_campaign=26q2&utm_content=1st#:~:text=Once%20we%20started%20using%20Meticulous%2C%20we%20couldn%27t%20imagine%20working%20without%20it.)

**原文标题**: [Meticulous AI - Automated Frontend Testing Without Writing Tests](https://www.meticulous.ai/?utm_source=thisweekinreact&utm_medium=newsletter&utm_campaign=26q2&utm_content=1st#:~:text=Once%20we%20started%20using%20Meticulous%2C%20we%20couldn%27t%20imagine%20working%20without%20it.)

Meticulous 是一款无需开发者编写代码即可实现全面、确定性测试的工具，能自动生成并维护测试套件，帮助团队快速、可靠地交付代码。

- 🚀 **零开发工作量**：只需添加脚本标签，即可自动记录用户交互并生成覆盖所有代码分支的端到端测试。
- 🧪 **自动化与全面性**：AI 引擎持续演化测试套件，覆盖每个用户流程和边缘情况，无需手动编写或维护测试。
- ⚡ **闪电般快速**：测试在计算集群上高度并行化，数千个屏幕的测试可在 120 秒内完成。
- 🔒 **消除假阳性**：通过模拟后端响应，避免因数据变化导致的误报，无需特殊测试账户或模拟数据。
- 🛡️ **从底层消除不稳定测试**：基于 Chromium 的确定性调度引擎，从根本上杜绝测试不稳定问题。
- 🔄 **与现有测试套件兼容**：可作为补充或完全替代现有测试，自动适应应用演变。
- 🏢 **受大型企业信赖**：被 Dropbox、Notion 等组织采用，工程师反馈“无法想象没有它的工作”。
- 🛠️ **简单集成**：支持 NextJS、React、Vue、Angular 等主流框架，几分钟内即可完成设置。

---

### [不断挖掘的蠕虫：TeamPCP 在最新一波攻击中瞄准 @antv | Wiz 博客](https://www.wiz.io/blog/mini-shai-hulud-teampcp-hits-antv-supply-chain)

**原文标题**: [The Worm That Keeps on Digging: TeamPCP Hits @antv in Latest Wave | Wiz Blog](https://www.wiz.io/blog/mini-shai-hulud-teampcp-hits-antv-supply-chain)

Wiz 研究团队发现 TeamPCP 组织在 2026 年 5 月 19 日发动了一场针对开源生态系统的多组件供应链攻击，波及 NPM 包（如@antv 命名空间）、GitHub Actions 和 VSCode 扩展，旨在窃取凭证、建立持久化访问。

- 🐛 **攻击范围广泛**：恶意代码注入 NPM 包（如@antv/*系列）、GitHub Actions（如 actions-cool/issues-helper）和 VSCode 扩展（nrwl.angular-console v18.95.0），影响开发者工具链。
- 🔑 **凭证窃取**：恶意软件收集 GitHub 令牌、SSH 密钥、云凭证、浏览器存储的秘密等敏感信息，并通过攻击者创建的 GitHub 仓库外传。
- 🕳️ **持久化后门**：在`~/.local/share/kitty/cat.py`安装 Python 后门，定期轮询 GitHub 寻找含`firedalazer`字符串的签名命令，执行远程代码。
- 🕵️ **归因于 TeamPCP**：基于基础设施、恶意软件功能和操作模式的重叠，Wiz 以中等置信度将此次攻击归因于已知威胁组织 TeamPCP。
- 🛡️ **安全建议**：建议组织立即调查开发者工作站和 CI/CD 环境，轮换暴露的凭证，检查持久化机制（如`cat.py`文件），并加强供应链防御（如依赖白名单、SBOM 生成）。

---

### [我们对 TanStack npm 供应链攻击的回应 | OpenAI](https://openai.com/index/our-response-to-the-tanstack-npm-supply-chain-attack/)

**原文标题**: [Our response to the TanStack npm supply chain attack | OpenAI](https://openai.com/index/our-response-to-the-tanstack-npm-supply-chain-attack/)

概述总结  
OpenAI 针对 TanStack npm 供应链攻击事件作出回应，确认未影响用户数据或生产系统，但两名员工设备受影响，导致部分内部代码库凭据泄露。作为预防措施，OpenAI 正在轮换代码签名证书，要求 macOS 用户在 2026 年 6 月 12 日前更新应用，以确保安全。

- 🔒 未发现用户数据或生产系统受损，也没有证据表明软件被篡改  
- 🛡️ 两名员工设备受影响，仅有限凭据从内部代码库泄露，已立即隔离并轮换凭据  
- 🖥️ 影响 macOS、iOS、Windows 签名证书，但仅 macOS 用户需在 6 月 12 日前更新应用  
- 📅 6 月 12 日后旧版 macOS 应用将无法使用，需从官方渠道更新  
- 🚫 已阻止新应用公证，未发现恶意软件使用 OpenAI 证书签名  
- 🔧 加速部署安全控制措施，包括 CI/CD 凭据强化和包管理器配置更新  
- 🌐 此事件反映供应链攻击趋势，OpenAI 正加强第三方组件完整性验证

---

### [Grafana Labs 安全更新：关于 TanStack npm 供应链勒索软件事件的最新情况 | Grafana Labs](https://grafana.com/blog/grafana-labs-security-update-latest-on-tanstack-npm-supply-chain-ransomware-incident/)

**原文标题**: [Grafana Labs security update: Latest on TanStack npm supply chain ransomware incident | Grafana Labs](https://grafana.com/blog/grafana-labs-security-update-latest-on-tanstack-npm-supply-chain-ransomware-incident/)

概述总结
Grafana Labs 于 2026 年 5 月 16 日确认遭受网络犯罪团伙针对性攻击，攻击者通过 TanStack npm 供应链攻击获取了 GitHub 仓库访问权限并下载了代码库，但未影响生产系统或 Grafana Cloud 平台。公司决定不支付赎金，已启动缓解措施并通知联邦执法部门。

- 🔒 攻击范围仅限于 GitHub 环境，未影响客户生产系统或 Grafana Cloud 平台
- 📂 下载内容包括源代码及内部运营信息（如业务联系人姓名和电子邮件地址）
- ✅ 代码库被下载但未被篡改，客户和开源用户无需采取行动
- 🚨 攻击源于 TanStack npm 供应链攻击（Mini Shai-Hulud 活动），于 5 月 11 日被检测到
- 🔑 因遗漏的 GitHub 工作流令牌导致攻击者获得访问权限
- 💰 公司决定不支付赎金，符合 FBI 的正式立场
- 🛡️ 已采取的缓解措施包括轮换自动化令牌、加强监控、审计提交记录及强化 GitHub 安全
- 👮 已通知联邦执法部门并保持对话
- 📋 调查仍在进行中，完成后将发布事件后报告
- 🔧 正在实施额外安全措施以保护 CI/CD 管道

---

### [仓库被 Shai-Hulud 的`.claude/settings.json`和`.vscode/tasks.json`文件入侵 · Issue #1186 · aidenybai/million · GitHub](https://github.com/aidenybai/million/issues/1186)

**原文标题**: [Repository Compromised with Shai-Hulud `.claude/settings.json` and `.vscode/tasks.json` files · Issue #1186 · aidenybai/million · GitHub](https://github.com/aidenybai/million/issues/1186)

概述摘要
该仓库因恶意文件注入而受到安全威胁，涉及 Shai-Hulud 恶意软件。

- 🚨 仓库默认分支中发现恶意 `.vscode/tasks.json` 和 `.claude/settings.json` 文件
- 🦠 这两个文件均会执行 Shai-Hulud 恶意软件
- 🔗 载荷通过被攻陷的 `actions-cool/issues-helper` 可重用操作注入
- 📎 引用来源：StepSecurity 博客关于 GitHub 操作被攻陷的详细报告
- ⚠️ 该问题导致 CI/CD 凭证可能被窃取

---

### [受损的 Nx Console 版本 18.95.0 · 安全公告 · nrwl/nx-console · GitHub](https://github.com/nrwl/nx-console/security/advisories/GHSA-c9j4-9m59-847w)

**原文标题**: [Compromised Nx Console version 18.95.0  · Advisory · nrwl/nx-console · GitHub](https://github.com/nrwl/nx-console/security/advisories/GHSA-c9j4-9m59-847w)

概述总结  
Nx Console 18.95.0 版本被恶意篡改并短暂发布，攻击者通过窃取的 GitHub 凭据注入恶意代码，窃取用户凭证并建立持久化后门。用户需立即更新至 18.100.0 版本并清理系统。

- 🔴 **事件概述**：Nx Console 18.95.0 被恶意篡改，在 Visual Studio Marketplace 和 OpenVSX 上短暂发布（分别约 18 分钟和 36 分钟），随后被下架。
- 🕒 **时间线**：攻击于 12:30 UTC 开始，12:47 UTC 被维护者下架；OpenVSX 上从 12:33 UTC 持续至 13:09 UTC。
- 🔍 **入侵指标**：检查是否安装 18.95.0 版本，以及是否存在特定文件（如 `cat.py`、`kitty-monitor.plist`）或运行中的恶意进程（如 `python cat.py` 或 `__DAEMONIZED=1`）。
- 🛠️ **修复措施**：立即更新至 18.100.0 或更高版本；终止所有 `__DAEMONIZED` 和 `cat.py` 进程；删除持久化文件（macOS 需先卸载 LaunchAgent）；轮换所有可访问的凭证（令牌、密钥、SSH 密钥）并审计访问日志。
- 🎯 **目标凭证**：恶意载荷从 Vault、npm、AWS、GitHub、1Password、文件系统等来源窃取凭证，并通过 HTTPS、GitHub API 和 DNS 外传。
- 🔗 **根本原因**：一名开发者因 Tanstack 供应链攻击泄露了 GitHub 凭据（通过 GitHub CLI），攻击者得以以贡献者身份运行工作流。
- 🛡️ **后续行动**：强化发布流程，要求两名管理员手动批准 Nx Console 的发布，以防止类似事件。
- 📊 **影响范围**：微软和 OpenVSX 报告下载量分别为 28 和 41，但内部分析显示约 6000 次扩展激活（仅限 VSCode），影响可能更大。

---

### [PlanetScale - 全球最快、最具可扩展性的 Vitess 和 Postgres 云托管服务](https://planetscale.com/?utm_source=newsletter&utm_medium=email&utm_campaign=2026_q1_react_weekly)

**原文标题**: [PlanetScale - the worldâs fastest and most scalable cloud hosting for Vitess and Postgres](https://planetscale.com/?utm_source=newsletter&utm_medium=email&utm_campaign=2026_q1_react_weekly)

PlanetScale 提供全球最快且最具可扩展性的云数据库服务，支持 Vitess/MySQL 和 Postgres，以超高性能、高可用性和低成本著称。

- ⚡ **极致性能**：采用 NVMe 驱动器实现无限 IOPS，延迟远低于 Amazon Aurora 和 GCP Cloud SQL，Metal 方案被基准测试为云端最快的 Postgres。
- 🚀 **超强可扩展性**：Vitess 通过水平分片实现无共享架构，支持跨数千节点分布数据，最初由 YouTube 开发，现用于 Slack、GitHub 等大型平台。
- 🛡️ **高可用性**：单区域部署 SLA 达 99.99%，多区域达 99.999%，支持自动故障转移、在线架构变更和零数据丢失回滚。
- 💰 **成本优化**：约 85% 的工作负载比 RDS MySQL 和 Aurora 更便宜，Metal 提供最佳性价比，支持预留实例和 Savings Plans。
- 🔒 **企业级安全**：符合 SOC 1/2、PCI DSS 4.0 和 HIPAA 标准，提供合规报告和信任中心。
- 🔧 **丰富功能**：分支与部署请求实现零停机架构变更，支持向量数据、数据库洞察、显式分片工作流、全局边缘网络和多种集成。
- 🌐 **灵活部署**：支持自带云（PlanetScale Managed）、AWS/GCP 市场，提供 Postgres 和 Vitess 两种引擎选项。

---

### [摇滚与反应节 2026 – 科技、数据摇滚、美食与派对，奥斯陆洛克菲勒](https://reactnorway.com/?utm_medium=social&utm_source=ThisWeekReact)

**原文标题**: [Rock & React Festival 2026 – Tech, Datarock, Food & Party at Rockefeller, Oslo](https://reactnorway.com/?utm_medium=social&utm_source=ThisWeekReact)

这是一场在奥斯陆摇滚圣地 Rockefeller 举办的 React 技术盛会，融合了前沿的前端技术与摇滚音乐，提供全天候的演讲、交流与现场演出。

- 🤘 **活动定位**：React Norway 2026 是一场“代码遇见和弦”的全栈前端大会，于 2026 年 6 月 5 日在奥斯陆传奇音乐场馆 Rockefeller 举行，强调真实、热烈与独特体验。
- 🎤 **豪华演讲阵容**：汇聚来自 Amazon、Sentry、Pinterest、Vercel、Hugging Face 等公司的行业领袖，分享 React 安全、TanStack Start、AI 集成、前端可观测性、异步设计等前沿话题。
- 📅 **紧凑日程安排**：从早上 8 点签到到晚上 7 点屋顶烧烤及摇滚音乐会，全天包含 12 场主题演讲、咖啡交流、午餐及社交环节，内容密集且互动性强。
- 🎟️ **多种门票选择**：提供“摇滚与 React”全票（5990 克朗）、仅音乐会票（450 克朗）及免费线上直播票，满足不同参与需求。
- 🏆 **创意竞赛环节**：参与者可录制乐器独奏并上传社交媒体参与抽奖，有机会赢取酒店住宿加节日门票，增加互动趣味性。
- 🏨 **住宿与地点**：推荐 Comfort Hotel Xpress Youngstorget，距离场馆仅几步之遥，参会者可享 15% 折扣（2026 年 6 月 3-6 日有效）。
- 📜 **丰富历史传承**：自 2019 年首次举办以来，React Norway 已从海边小规模活动发展为奥斯陆大型技术盛会，2025 年曾吸引 350 人参与。

---

### [TanStack 中的 React 服务端组件 – Frontend Masters 博客](https://frontendmasters.com/blog/react-server-components-in-tanstack/)

**原文标题**: [React Server Components in TanStack – Frontend Masters Blog](https://frontendmasters.com/blog/react-server-components-in-tanstack/)

本文介绍了 TanStack Start 中 React Server Components (RSC) 的实现，强调其与 Next.js 的不同之处，并展示了如何通过 RSC 减少客户端包体积、提升性能。

- 🖥️ **RSC 仅在服务器运行**：服务器组件（RSC）只运行在服务器，不发送代码到客户端，仅传输渲染后的标记，避免暴露敏感数据。
- ❌ **RSC 不是数据加载或 SSR 替代品**：TanStack Start 已有简洁的数据加载和服务器端渲染功能，RSC 专注于减少客户端包体积。
- 🎯 **RSC 适用场景**：适合大型、昂贵且客户端交互少的组件树，如包含大量条件导入和渲染的内容，可显著节省 JavaScript 大小。
- 📦 **性能对比**：非 RSC 版本发送 308KB JavaScript，RSC 版本降至 203KB，节省约 105KB。
- 🔧 **显式 API**：通过 `renderServerComponent` 和 `createCompositeComponent` 等工具，明确声明哪些内容作为 RSC 渲染，支持传递客户端组件作为 props。
- 🔄 **支持交互内容**：RSC 可接收客户端组件作为 props（如 `HeaderContent`），并在服务器端加载数据后渲染，通过 Suspense 实现流式加载。
- ⚠️ **谨慎使用**：RSC 不是万能方案，仅在组件树庞大或依赖重时才有显著收益，需根据项目需求选择。

---

### [结构共享、selectAtom 以及你的 jotai 原子为何过度重新渲染 | Peter Piekarczyk](https://www.peterp.me/articles/jotai-structural-sharing-vs-selectatom/)

**原文标题**: [Structural sharing, selectAtom, and why your jotai atoms re-render too much | Peter Piekarczyk](https://www.peterp.me/articles/jotai-structural-sharing-vs-selectatom/)

### 概述总结
Jotai 中原子值比较使用 `Object.is`，当派生原子每次返回新对象时会导致不必要的重渲染。解决方案包括：分解为原始值原子、使用 `selectAtom` 进行读取端去重，或在写入端实现结构共享（structural sharing）。

- 📊 **核心机制**：Jotai 使用 `Object.is` 比较原子值，新对象引用每次不同会触发所有订阅者重渲染
- 🚫 **常见陷阱**：派生原子中构造新对象（如对象字面量、数组方法）会导致 44 倍以上的不必要重渲染
- 🔧 **selectAtom 适用场景**：用于无法分解的投影（如 `.filter/.map` 列表操作）或需要保持身份稳定的聚合对象
- ✅ **更优方案**：优先将复杂对象分解为多个原始值原子（如 `countAtom`、`totalAtom`），利用 `Object.is` 免费去重
- 🛠️ **结构共享**：在写入端使用 `replaceEqualDeep` 保持未变子树的引用稳定性，适用于列表原子和 WebSocket 数据源
- 📋 **列表处理三选一**：简单列表无共享、列表 + 结构共享、ID 数组+atomFamily 规范化存储
- ⚡ **jotai-tanstack-query 最佳实践**：永远不要直接使用 `useAtomValue(rawQueryAtom)`，应派生所需字段原子

---

### [React2Shell 的故事 | Lachlan Davidson | 博客](https://lachlan.nz/blog/the-react2shell-story/)

**原文标题**: [The React2Shell Story | Lachlan Davidson | Blog](https://lachlan.nz/blog/the-react2shell-story/)

概述总结  
- 🐛 2025 年 11 月，研究人员发现并报告了 React 的严重远程代码执行漏洞“React2Shell”，影响数百万网站  
- 🚀 漏洞源于 React Server Components 的“Flight”协议，允许攻击者通过原型链访问和调用任意函数  
- 🔍 发现过程从研究 Flight 协议开始，逐步发现其缺乏安全检查，可滥用 thenable 和 Chunk 对象  
- 💡 最终利用 Chunk.prototype.then 和 Webpack 模块加载实现 RCE，PoC 只需安装 Next.js 即可复现  
- 🛡️ Meta 在 3 天内修复漏洞并发布 CVE-2025-55182，团队协作高效  
- 📡 后续扫描发现大量高危目标，包括 AI 公司和加密货币平台，凸显 Next.js 的广泛影响

---

### [飞行协议让你的拒绝服务攻击成了我的问题 | 萨沙·贝克尔](https://saschb2b.com/blog/flight-protocol-dos)

**原文标题**: [The Flight Protocol Made Your DoS My Problem | Sascha Becker](https://saschb2b.com/blog/flight-protocol-dos)

2026 年 5 月 6 日，React 和 Next.js 修复了 12 个漏洞，其中 CVE-2026-23870 是一个严重级别的拒绝服务漏洞，只需一个精心构造的 HTTP 请求就能耗尽 Node 进程 CPU。该漏洞揭示了 React Server Components 框架边界实际上一直是网络边界这一事实。

- 📝 **Flight 协议本质**：Flight 是 React 用于序列化服务器组件树的线格式协议，支持流式传输和引用去重。Server Actions 直接构建于其上，将函数调用暴露为 HTTP 端点。
- 🚨 **漏洞核心**：CVE-2026-23870 影响多个 react-server-dom-*包，其反序列化器缺乏结构约束验证，恶意负载可导致 CPU 耗尽。修复版本为 19.0.6、19.1.7 和 19.2.6。
- 🔍 **检查是否受影响**：运行`pnpm why react-server-dom-webpack`或`npm audit`检查版本。若低于修复版本则受影响，即使未直接使用 Server Actions（RSC 缓存和导航路由也会触发）。
- ⚠️ **紧急措施**：立即升级 Next.js 或直接依赖的 react-server-dom-*包。该攻击无需认证，单次请求即可触发，无优雅降级模式。
- 🧠 **框架边界即网络边界**：RSC 将服务器/客户端边界包装为渲染优化，但运行时实为序列化边界。每个 Server Action 都是未认证的 RPC 端点，前端开发者因框架抽象而忽略了威胁模型。
- 🔍 **为何被忽视**：协议早期缺乏文档、错误表面在调用点不可见、框架默认将解析视为性能而非安全。三者叠加使漏洞变得不可避免。
- 🛡️ **防御措施**：
  1. **将 Server Actions 视为 RPC 端点**：使用 Zod 等库进行显式参数验证。
  2. **限制解析器**：在反向代理层设置请求体大小上限。
  3. **保持 WAF 规则更新**：Cloudflare 已有通用规则覆盖此漏洞。
  4. **不信任缓存的 RSC 负载**：缓存同样跨越信任边界。
  5. **阅读协议一次**：花 20 分钟了解 Flight 格式，改变对安全的理解。
- 🔄 **模式背后的模式**：每一代“框架魔法”都在普通 API 内部埋下隐式协议。当框架将网络边界溶解为开发者易用性时，威胁模型仍需有人负责。

---

### [Certificates.dev 免费周末 | 免费获取 React 开发者认证培训 - Certificates.dev](https://certificates.dev/react/free-weekend?friend=TWIR)

**原文标题**: [Certificates.dev Free Weekend | Free access to React Developer Certification Training - Certificates.dev](https://certificates.dev/react/free-weekend?friend=TWIR)

以下是对所提供内容的概述摘要：

- 🎓 提供 React 中级认证备考训练的免费 48 小时访问权限，时间为 6 月 20 日至 21 日
- 📚 包含 9 个章节、13 个动手编码挑战、12 个测验和一次模拟考试
- 🏢 认证来自 680 多家公司，由行业领袖（如 Aurora Scharff、Cory House 等）共同创建
- 🧠 结构化学习：涵盖 JavaScript 基础、JSX、组件、事件处理、状态管理、高级 Hooks 和导航
- 🛠️ 动手项目：构建增量电影评分应用，练习 CRUD 操作、React Router 和 TypeScript 集成
- 🚫 不包括正式考试，考试券需单独购买（当前有黑五早鸟优惠，60% 折扣加送初级认证和 AI 课程）
- 💬 邀请用户投票选择其他框架/技术的认证需求

---

### [命运 1.0 | 命运](https://fate.technology/posts/fate-1.0)

**原文标题**: [fate 1.0 | fate](https://fate.technology/posts/fate-1.0)

fate 1.0 正式发布，这是一个专为 Async React 设计的数据框架，通过视图组合、归一化缓存和实时订阅等特性，简化数据获取和状态管理。

- 🚀 **核心特性**：fate 1.0 结合视图组合、归一化缓存、数据掩码和 Async React 功能，支持生产环境使用。
- 🔄 **实时视图**：新增 `useLiveView` 和 `useLiveListView` 钩子，通过 SSE 实现零配置的实时数据更新。
- 🛠️ **Drizzle 支持**：新增对 Drizzle 的原生 HTTP 传输支持，不再强制依赖 tRPC，降低集成门槛。
- ⚡ **Vite 插件**：用 Vite 插件替代手动代码生成，自动处理类型同步，提升开发效率。
- 🧹 **垃圾回收**：受 Relay 启发，引入缓存垃圾回收机制，自动释放未使用数据，优化内存管理。
- 🐛 **修复与优化**：改进了乐观更新排序、请求生命周期、列表缓存范围和大列表性能。
- 🏗️ **脚手架工具**：通过 `create-fate` 快速启动项目，支持 Drizzle、Prisma 等模板。
- 🌐 **Void 集成**：与 VoidZero 的 Void Router 结合，成为首个专为 Async React 设计的元框架。

---

### [发布 2026-05-20 10:04 · TanStack/router · GitHub](https://github.com/TanStack/router/releases/tag/release-2026-05-20-1004)

**原文标题**: [Release Release 2026-05-20 10:04 · TanStack/router · GitHub](https://github.com/TanStack/router/releases/tag/release-2026-05-20-1004)

TanStack Router 发布 2026-05-20 版本，包含多项新功能和修复，涉及多个包更新。

- 🚀 **新功能：延迟水合** (#7362) — 由 @schiller-manuel 实现，提升加载性能
- 🔧 **路由核心：参数优先级选项** (#7411) — 由 @Sheraff 添加，优化路由匹配算法
- 🐛 **修复路由不匹配警告和 HMR 路由索引** (#7422) — 由 @schiller-manuel 修复
- 🛠️ **路由插件：检测类型化根路由上下文** (#7420) — 支持 HMR 改进
- 🔄 **路由核心：在初始客户端路由匹配前水合** (#7416) — 优化客户端加载流程
- 📦 **依赖更新** — 包括 express、webpack-dev-server、zod、chokidar 等
- 📋 **包版本更新** — 涉及 @tanstack/react-router、@tanstack/react-start 等 20 多个包
- 👥 **贡献者** — Sheraff 和 schiller-manuel

---

### [延迟水合 | TanStack Start React 文档](https://tanstack.com/start/latest/docs/framework/react/guide/deferred-hydration)

**原文标题**: [Deferred Hydration | TanStack Start React Docs](https://tanstack.com/start/latest/docs/framework/react/guide/deferred-hydration)

TanStack Start 的延迟水合功能允许开发者标记页面部分内容为“暂不交互”，以优化初始加载性能，同时保留服务器端渲染的 HTML。

- 🧩 **核心机制**：通过 `<Hydrate>` 组件和策略（如 `visible()`、`idle()`）控制页面特定区域何时从静态 HTML 变为可交互，默认还会将子组件拆分为独立代码块以延迟加载。
- ⏳ **三大决策**：`when`（决定水合时机）、`split`（是否代码拆分）、`prefetch`（是否预加载），可灵活组合以平衡性能与用户体验。
- 🎯 **适用场景**：适合首屏非必需的 SSR 内容，如折叠区评论、地图、图表等；不适合导航、搜索框、购物车等需即时交互的元素。
- 🔄 **与 Astro 对比**：Astro 从静态出发，选择哪些部分“活过来”；TanStack Start 从全交互出发，选择哪些部分“可以等”，两者底层机制不同。
- ⚛️ **与 React 选择性水合对比**：React 控制水合顺序，但所有边界最终都会水合；延迟水合则决定边界是否水合，可完全避免某些区域的水合。
- 🧠 **嵌套边界**：父边界必须先水合，子边界才能水合；交互意图可触发祖先链的提前水合。
- 🛠️ **策略参考**：支持 `load()`、`idle()`、`visible()`、`media()`、`interaction()`、`condition()`、`never()` 等多种策略，可配置超时、边距、事件等参数。
- 📦 **编译限制**：`Hydrate` 必须直接使用静态导入的组件，子组件需直接放在内部，避免函数作为子组件、Hook 调用或 `this`/`super` 捕获等模式，否则无法正确拆分。

---

### [CSS 样式 | TanStack 开始 React 文档](https://tanstack.com/start/latest/docs/framework/react/guide/css-styling#inline-route-css-in-production)

**原文标题**: [CSS Styling | TanStack Start React Docs](https://tanstack.com/start/latest/docs/framework/react/guide/css-styling#inline-route-css-in-production)

TanStack Start 支援多種 CSS 模式，並提供 SSR 感知的資源發現功能，幫助開發者根據需求選擇合適的樣式導入方式。

- 📄 **`?url` 明確樣式表連結**：用於需要將樣式表 URL 放入路由 `head()` 的情況，由開發者自行渲染 `<link>` 標籤，支援動態 Early Hints。
- 🌍 **副作用導入全局 CSS**：使用 `import './global.css'` 將全局樣式附加到路由區塊，可從 Start 清單中發現，支援靜態 Early Hints 和 CSS 內聯。
- 🎨 **CSS Modules 作用域樣式**：導入 `import styles from './card.module.css'` 獲得作用域類名，同樣從路由區塊圖中發現，支援靜態 Early Hints 和 CSS 內聯。
- ⏱️ **CSS 發現時機**：副作用導入和 CSS Modules 在建置時發現，`?url` 則在路由 `head()` 執行時才被發現，影響 Early Hints 階段。
- ⚡ **生產環境 CSS 內聯**：啟用 `server.build.inlineCss` 可將路由 CSS 嵌入 HTML，減少首次渲染的阻塞請求，但會增加 HTML 大小。
- 🔧 **運行時控制內聯**：可在伺服器進入點按請求控制 CSS 內聯行為，例如根據請求頭 `x-inline-css` 動態調整。
- 🔗 **URL 重新基準**：內聯 CSS 時，相對路徑的 `url()` 和 `@import` 會自動重新基準為絕對路徑，支援 `transformAssets` 選項進行運行時 URL 重寫。
- ⚖️ **權衡考量**：CSS 內聯適合小型路由 CSS，但會增加 HTML 大小、失去獨立快取能力，且需處理 CSP 策略。

---

### [中间件 | TanStack Start React 文档](https://tanstack.com/start/latest/docs/framework/react/guide/middleware#csrf-middleware)

**原文标题**: [Middleware | TanStack Start React Docs](https://tanstack.com/start/latest/docs/framework/react/guide/middleware#csrf-middleware)

TanStack Start 的中间件系统允许开发者自定义服务器路由和服务器函数的行为，支持认证、日志、错误处理等多种功能。

- 🔗 **中间件类型**：分为请求中间件（处理所有服务器请求）和服务器函数中间件（专门处理服务器函数，支持输入验证和客户端逻辑）。
- 🧩 **可组合性**：中间件可以依赖其他中间件形成链式执行，通过调用 `next()` 函数推进链。
- 📋 **请求中间件**：通过 `.server()` 方法定义服务器端逻辑，可用于服务器路由的所有方法或特定方法。
- 🛠️ **服务器函数中间件**：支持 `.client()`（客户端逻辑）、`.inputValidator()`（输入验证）和 `.server()`（服务器端逻辑）方法。
- 🔄 **上下文管理**：通过 `next({ context: ... })` 在中间件间传递数据，客户端上下文需通过 `sendContext` 显式发送到服务器。
- 🌐 **全局中间件**：在 `src/start.ts` 中配置，可应用于所有请求或所有服务器函数，并包含 CSRF 保护。
- ⚡ **执行顺序**：按依赖顺序执行，全局中间件优先，然后依次执行链中的中间件。
- 📡 **请求/响应修改**：支持自定义头部、自定义 fetch 实现（客户端），以及读取/修改服务器响应。
- 🧪 **中间件工厂**：通过函数创建参数化的中间件（如授权中间件），实现复用和动态行为。
- 🌳 **环境优化**：服务器端代码在客户端构建时会被 tree-shaking 移除，提升性能。

---

### [别再等待 JSON：用单一模式流式输出结构化数据 | TanStack 博客](https://tanstack.com/blog/streaming-structured-output)

**原文标题**: [Stop Waiting on JSON: Stream Structured Output with One Schema | TanStack Blog](https://tanstack.com/blog/streaming-structured-output)

TanStack AI 的 `useChat` 现在支持通过 `outputSchema` 直接获取类型化的流式结构化输出，无需手动处理 JSON 解析。

- 🚀 **告别样板代码**：不再需要手动累加字符串、调用 `parsePartialJSON` 或进行类型转换，`useChat({ outputSchema })` 直接返回类型安全的 `partial` 和 `final` 对象。
- 🧩 **单一 schema，两端共享**：在服务器端定义 Zod schema，客户端传入相同 schema，即可获得 `DeepPartial<Person>` 的实时更新和完整的 `Person` 结果。
- ⚙️ **底层全面升级**：`StructuredOutputStream<T>` 使用正确的联合类型，自定义事件（如 `ApprovalRequestedEvent`）也获得类型标记，并支持逐块调试日志。
- 🌐 **框架与提供商全覆盖**：支持 React、Vue、Solid、Svelte，以及 OpenAI、OpenRouter、Grok 等主流提供商，结构化摘要也可端到端流式传输。
- 🎯 **设计哲学：不新增 Hook**：将 `outputSchema` 集成到现有 `useChat` 中，只需添加一个 prop 即可升级，避免引入额外 Hook 带来的文档和用户困惑。

---

### [发布 v9.3.0 · reduxjs/react-redux · GitHub](https://github.com/reduxjs/react-redux/releases/tag/v9.3.0)

**原文标题**: [Release v9.3.0 · reduxjs/react-redux · GitHub](https://github.com/reduxjs/react-redux/releases/tag/v9.3.0)

概述总结
- 🎉 React-Redux v9.3.0 正式发布，核心变化是标记 `connect` API 为弃用，但功能不变，鼓励用户迁移到现代 Hooks。
- 🔄 `connect` 被标记为 `@deprecated`，仅 IDE 显示删除线，无运行时错误或行为变化，同时提供无弃用标记的 `legacy_connect` 别名。
- 📚 此举旨在引导用户从 `connect` 迁移至 `useSelector`/`useDispatch` Hooks，以简化代码并提升性能。
- 🔒 修复了可信发布（Trusted Publishing）问题，重新启用了发布来源验证标志。
- 🛠️ 主要变更由 @markerikson 在 PR #2269 中完成，完整变更日志涵盖 v9.2.0 至 v9.3.0 的更新。

---

### [发布 v2.12.0 · reduxjs/redux-toolkit · GitHub](https://github.com/reduxjs/redux-toolkit/releases/tag/v2.12.0)

**原文标题**: [Release v2.12.0 · reduxjs/redux-toolkit · GitHub](https://github.com/reduxjs/redux-toolkit/releases/tag/v2.12.0)

Redux Toolkit v2.12.0 发布，新增技能文件、TypeScript 改进和多项修复。

- 🎉 新增 RTK 使用技能文件（基于 TanStack Intent），涵盖现代 RTK 使用、迁移、客户端/服务端状态管理和副作用处理
- 🔧 导出 RTK Query 钩子选项类型，方便开发者直接复用，无需再用 `Parameters` 提取
- 🛠️ 修复无限查询中 `isSuccess` 状态标志在切换缓存条目时的错误，避免 UI 闪烁
- ⏱️ 为 `autoBatch` 增强器的 `requestAnimationFrame` 添加 100ms 超时回退，解决后台标签页中 UI 不更新问题
- 🏷️ 内部 `IgnorePaths` 类型重命名为 `IgnoredPaths`，增强一致性
- 📦 改用 TS 5.4+ 内置的 `NoInfer` 工具类型
- 🔄 允许基于接口的类型守卫用于监听器中间件匹配器

---

### [v1.5.0 · 基础用户界面](https://base-ui.com/react/overview/releases/v1-5-0)

**原文标题**: [v1.5.0 · Base UI](https://base-ui.com/react/overview/releases/v1-5-0)

v1.5.0 版本更新概要  
- 🚀 通过交互拆分提升挂载性能，关闭弹窗挂载性能提升高达 50%，卸载性能提升高达 85%  
- 📄 为虚拟箭头使用本地文档  
- 🖥️ 修复 macOS Safari 和 Firefox 在按 Esc 关闭弹窗时最小化全屏的问题  
- 🔧 移除不必要的记忆化处理  
- 🔒 在 useStableCallback() 中不再使用 Math.random()  
- 🔙 修复引用断开时的焦点返回问题  
- 🎯 如果焦点已移入弹窗内，不再抢夺初始焦点  
- ⚠️ 警告对话框：修复默认值处理  
- 🔍 自动完成：修复原生 FormData 对弹窗输入的支持  
- ☑️ 复选框：按 Enter 时提交关联表单  
- 📋 组合框：暴露清除可见性状态，修复弹窗输入表单提交，保留关闭查询，修复 RTL 行为，忽略只读或禁用时的隐藏输入变化  
- 🖼️ 对话框：考虑受控的 open 属性进行状态检测  
- 📐 抽屉：在<Drawer.Viewport>中转发 style 属性  
- 📝 字段：避免在验证中使用 flushSync  
- 📑 表单：避免在验证中使用 flushSync  
- 🍔 菜单：修复子菜单指针事件范围，支持<Menu.GroupLabel>，考虑受控 open 属性  
- 🧭 导航菜单：修复 RTL 行为，修复 keepMounted 内容尺寸  
- 🔢 数字字段：允许键盘输入波斯数字，在步进交互时同步粘贴输入  
- 🔑 OTP 字段：重大变更：重命名 sanitizeValue() 为 normalizeValue() 并允许与验证组合，避免 flushSync，支持 Ctrl 和 Cmd 快捷键，触发 onValueComplete() 完成粘贴，修复垂直箭头导航，忽略只读或禁用时的隐藏输入变化，防止锁定隐藏自动填充验证，修复 RTL 箭头导航  
- 💬 弹出框：修复 RTL 行为，关闭时保留活动触发器，考虑受控 open 属性  
- 🃏 预览卡片：考虑受控 open 属性，集成内联定位  
- 📜 滚动区域：修复 RTL 行为  
- 📌 选择：清除过期项文本引用，添加 data-popup-side 到触发器，允许无高亮鼠标选择，忽略只读或禁用时的隐藏输入变化，修复嵌套选择需要额外点击关闭父级的问题  
- 📂 标签页：触发自动标签选择的 onValueChange()  
- 🍞 提示框：重用 getElementTransform() 并移除本地实现，修复释放时的卡住拖动状态，移除记忆化选择器  
- 💡 工具提示：考虑受控 open 属性，修复嵌套工具提示触发时的闪烁问题

---

### [发布版本 v7.76.0 · react-hook-form/react-hook-form · GitHub](https://github.com/react-hook-form/react-hook-form/releases/tag/v7.76.0)

**原文标题**: [Release Version v7.76.0 · react-hook-form/react-hook-form · GitHub](https://github.com/react-hook-form/react-hook-form/releases/tag/v7.76.0)

react-hook-form v7.76.0 版本发布，包含多项错误修复和功能改进。

- 🪭 修复 `isDirty` 与 `dirtyFields` 状态同步问题（#13141, #13370）
- 🐞 修复 `isValidating` 在未订阅 `validatingFields` 时的响应性问题（#13440）
- 🛺 修正测试描述中的重复单词拼写错误（#13439）
- 🐞 修复表单级验证时的错误状态问题（#13436, #13437）
- 🐞 修复 `append({ obj: null })` 在 `remove()` 后被 `defaultValues` 静默替换的问题（#13429, #13435）
- 🐞 修复因重复提交错误焦点导致的原生验证提示抑制问题（#13432）
- 🐞 修复 `setValues` 更新未传播到已挂载的 Controller 字段（#13431）
- 🐞 修复条件挂载的 Controller 字段在使用 `shouldUnregister` 时重置值的问题
- 🐞 修复 `useFieldArray` 的 `remove` 在使用 `values` 属性时留下空对象的问题（#13422）
- 🐞 修复嵌套 `setValue` 更新时未通知所有匹配字段数组根节点的问题（#13260, #13420）
- 🐞 修复 `trigger()` 中嵌套解析器字段数组错误的保留问题（#13104, #13419）
- 🐞 修复 `useFieldArray` 与 `watch` 同时使用时 `formState.defaultValues` 的保留问题（#13413）
- 📝 更新 `IsNever`、`register` 和 `getFieldState` 的 JSDoc 文档（#13410, #13411）
- 🐞 恢复 `Watch` 对 TypeScript 4 的兼容性（#13409）

---

### [发布 v21.0.0 · facebook/relay · GitHub](https://github.com/facebook/relay/releases/tag/v21.0.0)

**原文标题**: [Release v21.0.0 · facebook/relay · GitHub](https://github.com/facebook/relay/releases/tag/v21.0.0)

Relay v21.0.0 版本发布，带来 TypeScript 原生支持、现代化 Flow 类型生成、新错误处理能力和实验性 React 服务器组件支持，包含多项重大变更。

- 🎉 **TypeScript 原生支持**：`relay-runtime` 和 `react-relay` 现在直接包含 `.d.ts` 类型定义，不再需要 DefinitelyTyped 的 `@types/relay-runtime`。
- 🔄 **Flow 用户需注意**：生成的类型现在使用现代 Flow 语法，包括 `(expr as Type)` 转换、`ReadonlyArray`、`unknown` 和 `NonNullable`，升级后需重新运行 Relay 编译器。
- ❌ **`@live_query` 已移除**：该指令被移除，请迁移到 `@client_polling(interval: ...)` 或 `@live`。
- 🛠️ **Relay Resolvers 新语法**：`enable_legacy_verbose_resolver_syntax` 标志已移除，改用 `@relayField` 和 `@relayType` 标签，编译器可自动迁移。
- 🔒 **`@oneOf` 输入类型更严格**：现在生成更严格的判别联合类型，只允许一次设置一个属性，可通过 `oneOfType: "relaxed"` 选择退出。
- ✨ **新功能**：`@catch` 扩展支持 `@connection` 和客户端边缘字段；`@alias` 现在支持片段定义；新增实验性编译器 CLI 工具。
- 🧪 **React 服务器组件（实验性）**：新增 `react-relay/rsc_EXPERIMENTAL` 入口点，提供 `serverFetchQuery`、`serverReadFragment`、`serverPreloadQuery` 和 `useQueryFromServer` API。
- 🐛 **重要错误修复**：修复大型模式崩溃、`@raw_response_type` 准确性、冲突的 `@match` 字段、监视模式稳定性等问题。
- ⚠️ **重大变更**：包括移除 `@live_query`、`@OneOf` 输入类型更严格、移除旧版解析器语法、`mixed` 改为 `unknown`、`$NonMaybeType` 改为 `NonNullable` 等。
- 📚 **文档改进**：修复多处文档错误，更新解析器文档，升级 Docusaurus v3，并添加了术语表定义。

---

### [Storybook 10.4](https://storybook.js.org/blog/storybook-10-4/)

**原文标题**: [Storybook 10.4](https://storybook.js.org/blog/storybook-10-4/)

Storybook 10.4 版本发布，重点支持 AI 代理自动配置、代码变更审查、快速分享和框架扩展。

- 🤖 **自动配置**：AI 代理可自动分析项目结构、生成配置、模拟数据和测试，大幅降低组件开发的前期设置成本。
- 🔍 **变更检测**：新增侧边栏过滤器，可快速定位新增、修改或受代码变更影响的故事，简化 UI 审查流程。
- 🤝 **快速分享**：一键发布 Storybook 到云端，无需提交代码或等待 CI，即可让团队成员查看开发中的组件。
- 🌴 **TanStack React 框架**：与 TanStack 核心团队合作，提供零配置支持，包括类型安全路由和服务器函数。
- 📱 **React Native 隔离**：新增独立应用入口点，通过环境变量切换，实现 Storybook 与移动应用代码的彻底分离。
- ⚡ **React 组件元数据（实验性）**：基于 Volar 和 TypeScript 语言服务器，提供更快、更高质量的组件元数据，用于 AI 代理上下文。
- 🚀 **升级指南**：新用户可通过 `npm create storybook@latest` 创建项目，现有用户使用 `npx storybook@latest upgrade` 自动迁移。

---

### [GitHub - millionco/react-doctor: 你的代理编写了糟糕的 React 代码，这个工具能捕获它 · GitHub](https://github.com/millionco/react-doctor)

**原文标题**: [GitHub - millionco/react-doctor: Your agent writes bad React. This catches it · GitHub](https://github.com/millionco/react-doctor)

React Doctor 是一个用于检测 React 代码质量的开源工具，提供健康评分和可操作的诊断建议。

- 🩺 **一键扫描**：运行 `npx react-doctor@latest` 即可扫描代码库，输出 0-100 的健康评分（75+ 优秀，50-74 需改进，<50 严重），并列出状态、性能、架构、安全和可访问性等方面的问题。
- 🤖 **智能适配**：支持 Next.js、Vite 和 React Native，规则会根据框架和 React 版本自动切换。还能为 50+ 种编码代理（如 Claude Code、Cursor）安装最佳实践规则文件。
- 🚦 **CI/CD 集成**：提供 GitHub Actions 复合操作，可自动在 PR 中发布粘性评论或注释，支持基于诊断或分数阈值的门控机制，灵活配置失败模式。
- ⚙️ **灵活配置**：通过 `react-doctor.config.json` 或 `package.json` 的 `reactDoctor` 键进行配置，支持忽略规则、文件、覆盖特定规则，以及按表面（CLI、PR 评论、分数、CI 失败）精细控制诊断显示。
- 📊 **评分机制**：健康分数 = 100 - (唯一错误规则数 × 1.5) - (唯一警告规则数 × 0.75)，基于唯一规则触发次数而非总实例数，分数可能随新规则添加而下降。
- 🔍 **高级功能**：支持差异扫描（仅扫描变更文件）、暂存区扫描、JSON 输出、内联抑制注释、`--explain` 诊断规则触发原因，以及可选的 ESLint 插件集成。
- 📈 **排行榜**：公开扫描顶级 React 代码库的排名，如 executor（96 分）、nodejs.org（86 分）等，社区可贡献。

---

### [更新日志.md](https://raw.githubusercontent.com/remix-run/react-router/main/CHANGELOG.md)

**原文标题**: [CHANGELOG.md](https://raw.githubusercontent.com/remix-run/react-router/main/CHANGELOG.md)

React Router v7.15.1 发布，主要引入新的 `unstable_useRouterState()` 钩子，以整合多个现有钩子的功能，并修复了若干问题。

- 🆕 新增 `unstable_useRouterState()` 钩子（不稳定），可统一访问活动与待定路由状态，未来将取代 `useLocation()`、`useParams()` 等多个钩子
- 🔧 优化 `useFetchers` 的记忆化，确保返回稳定引用，仅当 fetchers 变化时更新
- 🛠 改进 fetcher Maps 的不可变操作，避免因未提交的更新导致 React 渲染延迟和闪烁
- 🐛 修复 `serverLoader()` 在客户端导航中断水合时返回陈旧 SSR 数据的问题
- 🐛 修复 SPA 模式下 `RouterProvider` 的 `onError` 回调未对同步初始加载器错误生效的问题
- 🧹 内部重构，通过共享工具统一突变请求检测逻辑
- 🐛 修复 `@react-router/dev` 中 `basename` 与 `app` 目录名冲突的问题（当 Vite `base` 也匹配时）
- ⚠️ 更新不稳定特性说明，强调 `unstable_useRouterState()` 仅适用于数据/框架/RSC 模式，否则会抛出错误

---

### [为什么 React 开发者正从 Next.js 转向 TanStack - YouTube](https://www.youtube.com/watch?v=6moPS3AAbe4)

**原文标题**: [Why React Developers Are Leaving Next.js for TanStack - YouTube](https://www.youtube.com/watch?v=6moPS3AAbe4)

概述：YouTube 平台的相關資訊與政策說明
- 📰 新聞中心：提供 YouTube 的最新消息與公告
- ©️ 版權：說明內容版權相關規範
- 📞 聯絡我們：提供用戶聯繫管道
- 🎨 創作者：支援內容創作者的工具與資源
- 📢 刊登廣告：廣告刊登選項與合作方式
- 👨‍💻 開發人員：API 與開發者相關資訊
- 📜 條款：使用條款與服務協議
- 🔒 私隱：隱私權保護政策說明
- 🛡️ 政策及安全：平台安全與內容政策
- ⚙️ YouTube 的運作方式：平台功能與運作機制
- 🧪 測試新功能：新功能測試與反饋
- ©️ 2026 Google LLC：版權所有歸 Google 公司

---

### [一个 PR 就劫持了 NPM 注册表... - YouTube](https://www.youtube.com/watch?v=gwTQLZSIlsU)

**原文标题**: [A single PR just hijacked the NPM registry... - YouTube](https://www.youtube.com/watch?v=gwTQLZSIlsU)

本頁面為 YouTube 平台相關資訊的總覽，涵蓋版權、政策、聯絡方式及平台運作等核心項目。

- 📰 新聞中心：提供 YouTube 最新消息與官方公告
- ©️ 版權：說明內容使用與版權保護相關規範
- 📞 聯絡我們：提供用戶與創作者聯繫 YouTube 的管道
- 🎬 創作者：針對內容創作者提供的資源與支援
- 📢 刊登廣告：介紹在 YouTube 上投放廣告的選項
- 👨‍💻 開發人員：提供 API 與技術整合資訊給開發者
- 📜 條款：列出使用 YouTube 服務需遵守的條款
- 🔒 私隱：說明用戶資料收集與使用的隱私政策
- 🛡️ 政策及安全：規範內容審查與平台安全準則
- ⚙️ YouTube 的運作方式：解釋平台推薦與內容管理機制
- 🧪 測試新功能：說明 YouTube 如何測試與推出新功能
- 🏢 © 2026 Google LLC：標示版權歸屬與法律責任

---

### [使用 Remotion 进行程序化与基于技能的视频创作 - Syntax #1005](https://syntax.fm/show/1005/programatic-and-skill-based-video-creation-with-remotion)

**原文标题**: [Programatic and Skill based Video Creation with Remotion - Syntax #1005](https://syntax.fm/show/1005/programatic-and-skill-based-video-creation-with-remotion)

本集 Syntax 播客邀请 Remotion 创始人 Jonny Burger，探讨程序化视频创作的爆发、AI 影响及新工具 Media Bunny。

- 🎬 Remotion 安装量从 12.5 万飙升至每日 80 万，展现程序化视频的爆炸式增长
- 💰 通过 Remotion Pro 实现可持续盈利，探索视频创作领域的商业变现策略
- 🤖 AI 正在重塑视频创作流程，但人类创意与自动化需平衡
- 🖥️ HTML-in-Canvas 新 Chrome 规范将彻底改变视频编辑工作流
- 📊 用户群体涵盖开发者、营销人员等，用例从社交媒体到企业宣传片
- ⚡ 技术挑战包括渲染性能优化、CSS 动画支持及跨平台兼容性
- 🐇 推出 Media Bunny 工具，简化视频资产管理流程
- 🎨 运动图形工作流正从传统软件向代码化、可编程方向演进
- 🔮 未来方向：社区反馈驱动产品迭代，探索 AI 辅助视频生成新边界

---

### [调试 Next.js 最佳实践：日志与追踪 | Sentry](https://sentry.io/resources/nextjs-may-workshop/?utm_source=thisweekinreact&utm_medium=paid-community&utm_campaign=nextjs-fy27q2-nextjsworkshop&utm_content=newsletter-secondary-nextjs-workshop-register)

**原文标题**: [Debugging Next.js Best Practices: Logs and Tracing | Sentry](https://sentry.io/resources/nextjs-may-workshop/?utm_source=thisweekinreact&utm_medium=paid-community&utm_campaign=nextjs-fy27q2-nextjsworkshop&utm_content=newsletter-secondary-nextjs-workshop-register)

### 概述总结
本内容介绍了关于 Next.js 调试的实践研讨会，重点涵盖日志记录、分布式追踪及错误监控，旨在帮助开发者高效定位生产环境中的问题。

- 🛠️ **研讨会核心内容**：涵盖高上下文日志编写、查询与告警设置，以及跨客户端和 Node 运行时的分布式追踪，帮助捕获认证、支付等场景的静默失败。
- 🔗 **日志与追踪关联**：强调将日志与追踪连接，提供完整上下文，避免切换工具。
- 📚 **入门资源推荐**：提供 Sentry for Next.js 的实践课程，以及关于 AI 代理、MCP 服务器监控和日志优化的额外阅读材料。

---

### [7 款最佳移动应用会话回放工具](https://posthog.com/blog/best-mobile-app-session-replay-tools?utm_source=twir&utm_campaign=may20)

**原文标题**: [7 best session replay tools for mobile apps](https://posthog.com/blog/best-mobile-app-session-replay-tools?utm_source=twir&utm_campaign=may20)

本文介绍了七款最佳移动端会话回放工具，并对比了它们的功能、价格和适用场景。

- 📱 **PostHog**：一体化开发者平台，提供会话回放、产品分析、A/B 测试等功能，免费层慷慨，适合初创和成长型团队。
- 🔍 **LogRocket**：专注于问题修复，支持 Redux 状态捕获和 AI 分析，适合 React Native 团队。
- 🧠 **UXCam**：专为移动应用设计，提供深度用户行为洞察，但定价不透明。
- 🆓 **Microsoft Clarity**：完全免费，适合仅需基础会话回放的用户，但缺少调试日志。
- 🎮 **Smartlook**：支持最广泛的移动 SDK（包括 Unity、Unreal Engine），适合游戏开发者。
- 📊 **FullStory**：企业级行为分析平台，提供自动捕获和 AI 摘要，但高级功能需付费。
- 🏢 **Contentsquare**：面向大型企业，提供区域热力图和影响量化，但成本高、复杂度高。

---

### [隔离棕地中 Expo SDK 55 的更新](https://www.callstack.com/blog/unlocking-expo-updates-in-an-isolated-brownfield-architecture-with-sdk-55)

**原文标题**: [Expo Updates in Isolated Brownfield with SDK 55](https://www.callstack.com/blog/unlocking-expo-updates-in-an-isolated-brownfield-architecture-with-sdk-55)

本指南介紹如何在隔離的棕地架構中使用 Expo SDK 55 啟用 Expo Updates，實現 OTA 更新。

- 🚀 **專案初始化**：使用 SDK 55 創建新 Expo 應用 (`npx create-expo-app@latest --template default@sdk-55`)，並確保棕地整合與 `expo-updates` 已配置完成。
- 📱 **iOS 整合步驟**：執行 `npx brownfield package:ios` 生成 XCFrameworks，然後在原生 iOS 應用中執行，即可啟用 Updates 支援。
- 🤖 **Android 暫行方案**：需先套用臨時補丁，再執行 `npx brownfield package:android` 生成 AAR，並透過 `publish:android` 發佈至 MavenLocal，最後在原生 Android 應用中驗證。
- 🧪 **測試 OTA 更新**：修改 UI（如將 "Welcome to Expo" 改為 "Welcome to Expo 55"），使用 `eas update` 發佈至 staging 頻道，重啟應用兩次後即可看到更新生效。
- ⚠️ **注意事項**：Android 補丁需在官方支援後移除；SDK 54 不正式支援此功能，但可透過特定補丁啟用；更多工具與文件可參考 React Native Brownfield GitHub。

---

### [Expo Go 中项目加载行为的变更 - Expo 更新日志](https://expo.dev/changelog/expo-go-loading-changes-may-2026)

**原文标题**: [Changes to project loading behavior in Expo Go - Expo Changelog](https://expo.dev/changelog/expo-go-loading-changes-may-2026)

概述摘要  
- 🔒 Expo Go 加载 EAS Update 更新时，仅限项目所有者或所属组织成员访问，自 2026 年 5 月 12 日起生效  
- 📦 Hermes 字节码包（HBC）仅在 Expo Go 的 EAS Update 中支持，自托管更新需提供纯 JavaScript 包，适用于 SDK 54、55、56 的最新版本  
- 🚀 推荐使用官方商店测试渠道（如 Google Play 内部测试、TestFlight）或 EAS Build 内部分发  
- 🛠 也可通过开发构建与 EAS Update 结合进行团队审阅分发

---

### [Nitro 模块中的 .box() 到底是干什么的？ | Peter Piekarczyk](https://www.peterp.me/articles/wtf-does-box-do-in-nitro-modules/)

**原文标题**: [WTF does .box() do in Nitro Modules? | Peter Piekarczyk](https://www.peterp.me/articles/wtf-does-box-do-in-nitro-modules/)

以下是您提供的文章摘要：

Nitro Modules 中的 `.box()` 方法用于在不同 JavaScript 运行时（如主线程和工作线程）之间安全传递 HybridObject。

- 📦 **核心问题**：Nitro 的 HybridObject 使用 JSI 的 `setNativeState` 将 C++ 对象附加到 JS 对象，但此状态绑定在特定运行时上，无法直接跨运行时使用。
- 🔄 **box() 的作用**：将 HybridObject 包装成更简单的 `jsi::HostObject`，该对象不依赖特定运行时，可被工作线程序列化器识别和传递。
- 🔓 **unbox() 的作用**：在目标运行时中，将 `HostObject` 还原为完整的 HybridObject，重新调用 `setNativeState` 创建新的 JS 包装器，但共享同一个 C++ 实例（通过 `shared_ptr`）。
- 🛠️ **工作线程限制**：工作线程有独立的 JS 引擎，不支持 `instanceof`、`Blob`、`FormData` 等，因此需要 `buildNitroRequestPure` 等纯函数来避免依赖主运行时特性。
- ⏳ **历史背景**：`setNativeState` 在 JSC 上直到 2023 年底才支持，Nitro 于 2024 年 9 月添加 `box/unbox` 以解决工作线程兼容性问题。
- 🎯 **当前状态**：尽管现代 `react-native-worklets` 支持自动序列化，但 `nitro-fetch` 等库仍手动使用 `box/unbox`，以确保与任何工作线程运行时兼容，避免依赖特定序列化器。
- 🧠 **关键洞察**：`HostObject` 是跨运行时的“护照”，而 `shared_ptr` 是实际共享的 C++ 对象，从未被复制。

---

### [无论何种情况，快速构建：Expo 如何优化速度（以及你如何也能做到）](https://expo.dev/blog/build-fast-no-matter-what-how-expo-is-optimizing-for-speed)

**原文标题**: [Build fast, no matter what: how Expo is optimizing for speed (and how you can, too)](https://expo.dev/blog/build-fast-no-matter-what-how-expo-is-optimizing-for-speed)

本文探讨了人工智能在医疗领域的应用现状与未来潜力，重点分析了诊断、治疗和患者管理方面的创新，同时指出了数据隐私和伦理挑战。

- 🩺 **诊断辅助**：AI 通过分析医学影像（如 X 光、MRI）提高疾病检测准确率，尤其在癌症早期筛查中表现突出。
- 💊 **个性化治疗**：基于患者基因和病史数据，AI 可推荐定制化药物方案，优化治疗效果并减少副作用。
- 🤖 **手术机器人**：AI 驱动的机器人辅助微创手术，提升操作精度，降低术后并发症风险。
- 📊 **患者管理**：AI 通过可穿戴设备实时监测健康指标，预测病情恶化，支持远程医疗和慢性病管理。
- 🔒 **数据隐私**：医疗数据共享面临泄露风险，需加强加密技术和法规保护，确保患者信息安全性。
- ⚖️ **伦理挑战**：AI 决策的透明性和责任归属问题亟待解决，需建立公平、可解释的医疗 AI 框架。

---

### [使用 TurboModule 替代构建更安全的 React Native 插件系统](https://www.callstack.com/blog/using-turbomodule-substitution-to-build-safer-react-native-plugin-systems)

**原文标题**: [Using TurboModule Substitution to Build Safer React Native Plugin Systems](https://www.callstack.com/blog/using-turbomodule-substitution-to-build-safer-react-native-plugin-systems)

本文介绍了在 React Native 沙箱系统中，通过 TurboModule 替换机制安全地管理共享资源（如文件系统、存储）的方法，实现了沙箱与宿主的数据隔离。

- 🔒 **核心问题**：沙箱中的代码需要访问共享资源（如文件系统、摄像头），但直接访问会带来数据泄露或覆盖风险。之前的 `allowedTurboModules` 白名单只能全盘允许或阻止，缺乏细粒度控制。
- 🔄 **解决方案**：引入 `turboModuleSubstitutions` 属性，允许宿主为每个沙箱声明模块替换。当沙箱请求原生模块时，运行时自动将其解析为沙箱安全的替代模块，例如将 `FileAccess` 替换为 `SandboxedFileAccess`。
- 🧩 **关键设计**：替换模块自动被列入白名单；运行时更改配置会触发沙箱完全重建；沙箱代码无需修改，替换在原生模块解析层透明完成。
- 🛠️ **沙箱感知协议**：通过 `SandboxAwareModule` 接口，替换模块能获取沙箱上下文（如 origin），从而为每个沙箱创建隔离的存储目录（如 `Sandboxes/<origin>/Documents`），并拒绝访问目录外的路径。
- 📂 **实际示例**：在文件系统实验中，关闭替换时沙箱与宿主共享数据；开启替换后，沙箱只能操作自己的隔离目录，实现完全透明的数据隔离。
- 💡 **其他应用场景**：该机制可扩展至分析（按沙箱标记事件）、网络（限制域名/速率限制）、密钥链（隔离凭证）、日志（自动添加沙箱前缀）等，提供通用安全方案。
- 🚀 **结论**：TurboModule 替换（v0.6.0 起）让沙箱宿主从“全有或全无”的权限控制，升级为提供限定、安全的原生功能，实现真正的沙箱内原生能力隔离。

---

### [GitHub - tmikov/hermes-node: Hermes JS 引擎的 Node.js 内置模块兼容层 · GitHub](https://github.com/tmikov/hermes-node)

**原文标题**: [GitHub - tmikov/hermes-node: Node.js built-in module compatibility layer for the Hermes JS engine · GitHub](https://github.com/tmikov/hermes-node)

hermes-node 是一个基于 Hermes 引擎、提供 Node.js 兼容性的 JavaScript 和 TypeScript 运行时，以单一二进制文件形式发布。

- 🚀 **直接运行 TypeScript**：无需单独编译步骤，Hermes 在解析时自动剥离类型注解，支持 `.ts` 文件直接执行
- 🐞 **内置调试器**：通过 `--inspect` 启动 Chrome DevTools 协议，自带 DevTools 前端 UI，支持断点、步进、控制台等功能
- 📦 **Node.js API 兼容**：复用 Node.js v24.13.0 的 JavaScript 库，支持 `fs`、`net`、`http`、`child_process` 等核心模块
- ⚠️ **启动速度较慢**：用户脚本每次运行都需重新编译，Hermes 的 AOT 优化在冷启动时成本较高，内置模块已预编译
- 🔒 **非 V8 引擎**：Hermes 是字节码解释器（带小型 arm64 JIT），适合快速启动和小内存场景，不适合长时间运行的非类型化 JavaScript
- 🧩 **Node-API 原生插件支持**：支持加载 `.node` 文件，但基于 V8 C++ API 的旧插件不兼容
- 🛠️ **命令行工具**：支持 `-e` 执行代码、REPL、`--node-version` 覆盖版本号、`--inspect-brk` 和 `--inspect-open` 调试选项
- 📋 **当前状态**：早期实验性项目，许多功能不完整，不适合生产环境；未来计划包括字节码缓存、AOT 预编译、`crypto` 和 `tls` 绑定
- 📜 **开源许可**：MIT 许可证，依赖 Hermes、libuv、c-ares 等第三方库

---

### [GitHub - daehyeonmun2021/react-native-skia-lab: 由 Daehyeon Mun 构建的精美 react-native-skia 演示](https://github.com/daehyeonmun2021/react-native-skia-lab)

**原文标题**: [GitHub - daehyeonmun2021/react-native-skia-lab: Beautiful react-native-skia demo built by Daehyeon Mun · GitHub](https://github.com/daehyeonmun2021/react-native-skia-lab)

daehyeonmun2021/react-native-skia-lab 是一个由 Daehyeon Mun 创建的开源项目，包含多个基于 React Native Skia 构建的精美演示，涵盖绘画、着色器、像素、手势、物理和多边形等交互效果，灵感来自 Jongmin Kim 的作品。

- 🎨 绘画演示：展示创意绘画功能
- ✨ 着色器效果：包含动态着色器示例
- 🔲 像素处理：演示像素级操作
- 👆 手势交互：实现触摸手势响应
- ⚡ 物理模拟：包含物理引擎效果
- 🔷 多边形示例：展示多边形图形处理
- 🛠️ 设置运行：通过 yarn 安装依赖，运行 yarn prebuild 准备环境，再使用 yarn android 或 yarn ios 启动应用
- ⭐ 社区数据：获得 160 颗星、14 个分叉和 2 个关注者
- 📝 技术栈：主要使用 TypeScript（98.2%）和 JavaScript（1.8%）

---

### [Meta Quest 着陆，工作室场景登场：ViroReact 2.55.0 新特性 | 作者：Oliver Edis | 2026 年 5 月 | ReactVision 更新](https://updates.reactvision.xyz/meta-quest-lands-studio-scenes-drop-in-whats-new-in-viroreact-2-55-0-a8876564047a?gi=e7e97c4ee9b1)

**原文标题**: [Meta Quest Lands, Studio Scenes Drop In: What’s New in ViroReact 2.55.0 | by Oliver Edis | May, 2026 | ReactVision Updates](https://updates.reactvision.xyz/meta-quest-lands-studio-scenes-drop-in-whats-new-in-viroreact-2-55-0-a8876564047a?gi=e7e97c4ee9b1)

ViroReact 2.55.0 正式发布，实现跨平台 AR/VR 开发，并整合 Studio 无代码编辑器，一套代码可同时部署到手机 AR 和 Meta Quest VR。

- 🚀 **跨平台 XR 导航器**：新增 `ViroXRSceneNavigator`，自动识别设备类型，AR 手机或 VR 头显一键切换，现有应用只需一行代码迁移。
- 🎮 **原生 VR 支持**：新增 `ViroVRSceneNavigator`，完整支持 Meta Quest 系列，保留物理、光照、阴影、动画等全部渲染管线。
- 🎨 **Studio 场景集成**：`StudioSceneNavigator` 让无代码设计的 XR 场景直接嵌入 ViroReact 应用，支持 UUID 指定场景，AR/VR 自动兼容。
- 📱 **一次开发多平台**：React Native 编写代码，Studio 设计场景，同时发布到手机 AR 和 Quest VR，无需重写。
- 🛠️ **新工具与修复**：新增 `useAnySourceHover` 和 `useAnySourcePressed` 钩子处理 VR 多指针输入，`isQuest` 和 `hasOpenXRSupport` 运行时导出，修复 Android 图像标记和 iOS 渲染问题。
- 🔄 **兼容性无破坏**：无破坏性变更，现有应用无需修改代码，Quest 支持通过 Expo 插件可选启用，兼容 React Native 0.83 和 Expo 54/55。
- 🎯 **未来路线图**：visionOS 和 Android XR 是下一步目标，持续扩展平台支持。

---

### [发布 v1.2.0 · callstackincubator/react-native-harness · GitHub](https://github.com/callstackincubator/react-native-harness/releases/tag/v1.2.0)

**原文标题**: [Release v1.2.0 · callstackincubator/react-native-harness · GitHub](https://github.com/callstackincubator/react-native-harness/releases/tag/v1.2.0)

此版本为 React Native Harness v1.2.0，主要聚焦于功能增强、架构优化和问题修复。

- 🐛 修复了 Harness 运行时中`expect.soft`的处理问题
- 🔐 新增权限自动化支持
- 🗂️ 为 iOS 模拟器 XCTest 工件添加了 Harness 管理的缓存
- 🔧 将 Harness 技能迁移至 CLI 中
- 📱 允许通过 UUID 查找 iOS 设备
- 🛠️ 避免将物理设备误判为模拟器
- ♻️ 简化了 Harness 架构以支持更安全的演进
- 📊 将客户端日志通过 Jest 结果控制台输出
- 🏗️ 支持将 xctest 构建作为外部命令执行
- 🧪 强化了应用监控命令的接口
- 🔄 更新操作以兼容 Node.js 24
- 🌐 在浏览器配置中暴露`ignoreDefaultArgs`参数
- 🧹 简化了 lefthook 钩子
- 🏅 新增原生 iOS 代码覆盖率支持
- 🌍 修复了 Web 上不覆盖原生 Event/EventTarget 的问题

---

### [发布 v56.0.0 · jamsch/expo-speech-recognition · GitHub](https://github.com/jamsch/expo-speech-recognition/releases/tag/v56.0.0)

**原文标题**: [Release v56.0.0 · jamsch/expo-speech-recognition · GitHub](https://github.com/jamsch/expo-speech-recognition/releases/tag/v56.0.0)

概述摘要  
- 🎉 expo-speech-recognition 发布 v56.0.0 预发布版本  
- 📅 该版本于 5 月 17 日 发布，包含 1 次提交  
- 🔄 版本号与 Expo SDK 同步，从 SDK 56 开始，库版本将跟随 Expo 版本号  
- 📱 最低 iOS 版本从 13.4 提升至 16.4  
- ✅ 支持 Expo SDK 56，未来 SDK 57 发布时对应安装 57.0.0  
- ❤️ 获得 2 个用户的心形表情反应

---

### [发布 v0.3.0 · software-mansion-labs/typegpu-confetti · GitHub](https://github.com/software-mansion-labs/typegpu-confetti/releases/tag/v0.3.0)

**原文标题**: [Release v0.3.0 · software-mansion-labs/typegpu-confetti · GitHub](https://github.com/software-mansion-labs/typegpu-confetti/releases/tag/v0.3.0)

typegpu-confetti v0.3.0 发布，主要进行了内部重构，使用 @typegpu/react 提升稳定性，无新功能。

- 🚀 版本号从 v0.2.x 升至 v0.3.0，属于次要版本更新
- 🔧 核心变更：使用 @typegpu/react 重写底层架构，带来更高稳定性
- 🛠️ 重构统一 Confetti 组件（PR #31）
- 📝 重命名 slots 和 accessors（PR #32）
- ⬆️ 更新至 TypeGPU 0.11.4（PR #33）
- 🧹 简化内部逻辑（PR #34）
- 👤 贡献者：iwoplaza 完成所有修改
- 📦 包含 2 个资源文件，获得 1 个火箭表情反应

---

### [发布 1.3.0 版本 · margelo/react-native-nitro-fetch · GitHub](https://github.com/margelo/react-native-nitro-fetch/releases/tag/v1.3.0)

**原文标题**: [Release Release 1.3.0 · margelo/react-native-nitro-fetch · GitHub](https://github.com/margelo/react-native-nitro-fetch/releases/tag/v1.3.0)

概述总结
- 🐛 修复：移除 nitroFetch 中的 box/unbox 操作（#95）
- 🐛 修复：Webpack 上的 textDecoder 警告（#92）
- 🐛 修复：arrayBuffer() 和 bytes() 中二进制响应体丢失/损坏的问题（#98）
- ⚡ 性能优化：文本解码器采用三级分发 + simdutf NEON + O3/LTO 优化（#97）
- 🎉 新贡献者：@fedpre 和 @ronickg 首次贡献
- 📦 发布 v1.3.0 版本，包含多项修复与性能改进

---

### [发布 v0.15.0 · callstackincubator/agent-device · GitHub](https://github.com/callstackincubator/agent-device/releases/tag/v0.15.0)

**原文标题**: [Release v0.15.0 · callstackincubator/agent-device · GitHub](https://github.com/callstackincubator/agent-device/releases/tag/v0.15.0)

该版本主要进行了架构重构、稳定性改进和性能优化，同时新增了截图无稳定化标志等功能。

- 🔧 重构命令架构和请求处理链，提升代码可维护性
- 🐛 修复多个稳定性问题，包括 Android 文本输入、iOS 超时和快照处理
- ⚡ 优化性能，如 macOS 设备快速解析和 iOS 回放加速
- 📸 新增截图无稳定化标志功能
- 📚 更新文档，包括 RN 设备稳定性和 React DevTools 分析指南
- 🧹 移除过时的生命周期命令
- 👥 欢迎新贡献者 spilist 和 demchenkoalex

---

### [发布 · gre/react-native-view-shot · GitHub](https://github.com/gre/react-native-view-shot/releases)

**原文标题**: [Releases · gre/react-native-view-shot · GitHub](https://github.com/gre/react-native-view-shot/releases)

gre/react-native-view-shot 是一个用于 React Native 的截图库，支持 iOS、Android、Web 和 Windows 平台，最新版本为 v5.1.0，主要更新包括对新架构的支持和跨平台修复。

- 📱 **iOS 17 兼容**：迁移至 UIGraphicsImageRenderer，修复弃用 API，并新增 XCTest 测试。
- 🤖 **Android 修复**：snapshotContentContainer 正确捕获屏幕外内容，扩展 JUnit 测试覆盖。
- 🪟 **Windows 支持**：在 RNW 0.76.17 上运行示例，包含完整演示套件和原生模块修复。
- 🧪 **新测试**：新增样式过滤器重现屏幕和 ScrollView 捕获演示，所有 Detox 端到端测试集成到 CI。
- 🔧 **v5.0.1 补丁**：修复 Android 直接捕获 GL/SurfaceView/TextureView 时的崩溃问题。
- 🚀 **v5.0.0 主要版本**：支持新架构（Fabric + TurboModules），迁移至 TypeScript，最低 React Native 版本要求 0.76.0。
- 🌐 **Web 改进**：修复 captureRef 崩溃、启用 CORS 图像处理、JPG 格式和 releaseCapture 问题。
- 📋 **示例应用**：重启包含 11 个测试屏幕，新增 Expo 示例和 Detox + Playwright 端到端覆盖。

---

### [发布 v1.10.0 · callstackincubator/rozenite · GitHub](https://github.com/callstackincubator/rozenite/releases/tag/v1.10.0)

**原文标题**: [Release v1.10.0 · callstackincubator/rozenite · GitHub](https://github.com/callstackincubator/rozenite/releases/tag/v1.10.0)

这是一个开源项目 Rozenite 的 v1.10.0 版本发布说明，主要包含多项功能增强和错误修复。

- 🔧 修复：将 GitHub Actions 固定到特定 SHA 以提升安全性
- 📊 功能：性能监控插件扩展数据覆盖范围，并实现 1 毫秒精度的时间显示
- 🗂️ 功能：存储插件为二进制条目添加十六进制优先的用户界面
- 🌐 功能：网络活动插件新增请求发起者详情、图片预览、二进制十六进制查看器、HTML/XML 响应渲染器，以及高级请求过滤器
- 🖥️ 功能：Vite 插件改进开发主机预设、流程和文档
- 🚀 优化：虚拟化大型代码块以提升性能，并避免 Metro 可选依赖覆盖问题
- 🎉 新贡献者：@draggie 首次参与贡献

---

### [回顾重绘与 TypeGPU - YouTube](https://www.youtube.com/watch?v=aP8GSJ7oTuc)

**原文标题**: [Debriefing Redraw & TypeGPU - YouTube](https://www.youtube.com/watch?v=aP8GSJ7oTuc)

本頁面為 YouTube 平台相關資訊的總覽，包含版權、政策、聯絡方式與開發者資源等。

- 📰 新聞中心：提供 YouTube 最新消息與官方公告
- ©️ 版權：說明內容使用規範與版權保護機制
- 📞 聯絡我們：提供用戶與創作者聯繫 YouTube 的管道
- 🎬 創作者：針對內容創作者提供的資源與支援
- 📢 刊登廣告：說明在 YouTube 上投放廣告的選項
- 👨‍💻 開發人員：提供 API 與技術整合的開發者資源
- 📜 條款：規範用戶使用服務的條款與條件
- 🔒 私隱：說明個人資料收集與使用的隱私政策
- 🛡️ 政策及安全：涵蓋社群規範與安全使用指引
- ⚙️ YouTube 的運作方式：解釋平台的推薦系統與內容管理
- 🧪 測試新功能：介紹平台正在測試的新功能與實驗
- 🏢 © 2026 Google LLC：版權歸屬與法律責任聲明

---

### [Expo SDK 56 全部新特性 - YouTube](https://www.youtube.com/watch?v=ywvywq0AGPM)

**原文标题**: [Everything new in Expo SDK 56 - YouTube](https://www.youtube.com/watch?v=ywvywq0AGPM)

本頁面列出了 YouTube 平台的核心資訊與政策，涵蓋版權、條款、隱私及創作者相關內容，並標明 Google 版權所有。

- 📰 **新聞中心**：提供 YouTube 官方新聞與公告。
- ©️ **版權**：說明內容版權相關規範與權利。
- 📞 **聯絡我們**：提供使用者聯繫 YouTube 的管道。
- 🎥 **創作者**：針對內容創作者提供的資源與支援。
- 📢 **刊登廣告**：說明廣告主如何在 YouTube 投放廣告。
- 👨‍💻 **開發人員**：提供 API 與技術開發相關資訊。
- 📜 **條款**：列出使用 YouTube 服務的條款與條件。
- 🔒 **私隱**：說明使用者資料的收集與使用方式。
- 🛡️ **政策及安全**：涵蓋社群規範與安全措施。
- ⚙️ **YouTube 的運作方式**：解釋平台推薦與內容管理機制。
- 🧪 **測試新功能**：介紹 YouTube 正在測試的新功能。
- 🏢 **© 2026 Google LLC**：版權歸屬與法律聲明。

---

### [使用 React Native Skia 构建高性能 UI | React Native Live | 第 11 集 - YouTube](https://www.youtube.com/watch?v=GChgKhfuzYA)

**原文标题**: [Building High-Performance UI with React Native Skia | React Native Live | Ep 11 - YouTube](https://www.youtube.com/watch?v=GChgKhfuzYA)

本頁面概述了 YouTube 平台相關的各項基本資訊、政策與聯絡方式。

- 📰 **新聞中心**：提供 YouTube 官方新聞與公告。
- ©️ **版權**：說明內容創作者的版權相關規範。
- 📞 **聯絡我們**：提供用戶與 YouTube 聯繫的管道。
- 🎥 **創作者**：針對內容創作者提供的資源與支援。
- 📢 **刊登廣告**：說明在 YouTube 上投放廣告的方式。
- 👨‍💻 **開發人員**：提供給開發者的 API 與技術文件。
- 📜 **條款**：列出使用 YouTube 服務的條款與條件。
- 🔒 **私隱**：說明用戶資料的收集與使用方式。
- 🛡️ **政策及安全**：涵蓋平台的安全政策與社群規範。
- ⚙️ **YouTube 的運作方式**：解釋平台推薦與內容審核機制。
- 🧪 **測試新功能**：介紹 YouTube 正在測試的新功能。
- ©️ **© 2026 Google LLC**：版權所有，歸 Google LLC 所有。

---

### [React Native Radio - RNR 353 - 在 AI 时代构建 React Native 应用](https://infinite.red/react-native-radio/rnr-353-building-react-native-apps-in-the-ai-era)

**原文标题**: [React Native Radio - RNR 353 - Building React Native Apps in the AI Era](https://infinite.red/react-native-radio/rnr-353-building-react-native-apps-in-the-ai-era)

### 概述摘要
本集讨论了在 AI 时代使用 React Native 构建应用的实践，包括 AI 工具（如 Claude、Cursor、Expo Agent）的应用、React Native 的持续相关性，以及开发者如何适应 AI 驱动的开发流程。

- 🤖 **AI 工具应用**：开发者主要使用 Claude 和 Cursor 等工具加速 React Native 开发，但 AI 在处理视觉反馈和复杂技术问题（如时区 bug）时仍显不足。
- 📱 **React Native 仍具优势**：实验表明，即使使用 AI，React Native 在构建跨平台应用时仍比单独开发 Android 和 iOS 更快、更一致，且支持空中更新和 JavaScript 开发者资源。
- 🔄 **进化而非革命**：AI 在移动开发中需逐步适应，例如通过 Maestro 测试和视觉反馈循环提升效果，但完全依赖 AI 仍有挑战。
- 🧪 **个人实验**：Mazen 正用 AI 构建一个应用，强调逐步迭代和手动审查，发现 AI 会忽略预存错误，需持续改进心态。
- 🌐 **社区与未来**：鼓励开发者分享 AI 辅助构建 React Native 应用的经验，并期待更集成的 IDE（如 Expo Agent）来统一开发、测试和设计流程。

---

### [GitHub - tc39/proposal-explicit-resource-management: ECMAScript 显式资源管理](https://github.com/tc39/proposal-explicit-resource-management)

**原文标题**: [GitHub - tc39/proposal-explicit-resource-management: ECMAScript Explicit Resource Management · GitHub](https://github.com/tc39/proposal-explicit-resource-management)

ECMAScript 显式资源管理提案（TC39 第三阶段）旨在通过引入 `using` 和 `await using` 声明，简化资源（如文件句柄、流、锁等）的获取与释放模式，并新增 `DisposableStack`、`AsyncDisposableStack` 容器及 `SuppressedError` 错误类型，以解决现有资源管理中的不一致性和常见陷阱。

- 📦 **核心语法**：引入 `using`（同步）和 `await using`（异步）声明，用于块级作用域内资源的自动释放，支持多个资源以逆序释放。
- 🧩 **容器对象**：新增 `DisposableStack` 和 `AsyncDisposableStack`，可聚合多个可释放资源，支持 `use`、`adopt`、`defer` 和 `move` 方法，便于复杂资源管理。
- ⚠️ **错误处理**：引入 `SuppressedError` 错误子类，用于捕获并报告资源释放过程中发生的多个异常，避免异常被静默吞没。
- 🔄 **迭代器集成**：为 `%IteratorPrototype%` 和 `%AsyncIteratorPrototype%` 添加 `@@dispose` 和 `@@asyncDispose` 方法，使迭代器支持自动清理。
- 🛠️ **内置适配**：建议为 DOM API（如 `AudioContext`、`WebSocket`）和 Node.js API（如 `fs.promises.FileHandle`）添加 `@@dispose`/`@@asyncDispose` 支持，但非强制。
- 🚀 **状态与进展**：提案已进入 TC39 第三阶段，同步部分已获批准，异步部分仍在审查中，需满足 Test262 测试和双实现等条件才能进入第四阶段。

---

### [[RFC] 使安装脚本成为可选加入 由 JamieMagee 提交 · 拉取请求 #868 · npm/rfcs · GitHub](https://github.com/npm/rfcs/pull/868)

**原文标题**: [[RFC] Make install scripts opt-in by JamieMagee · Pull Request #868 · npm/rfcs · GitHub](https://github.com/npm/rfcs/pull/868)

该 RFC 提议将 npm 的安装脚本（如 preinstall、install、postinstall）默认设为禁止，改为用户主动选择允许。

- 🔒 默认禁止安装脚本：npm 将默认阻止依赖项的安装脚本执行，用户需通过`package.json`中的`allowScripts`字段或新的 CLI 命令（`npm approve-scripts`、`npm deny-scripts`）来明确允许特定包的脚本。
- 🚨 安全动机：近期多起供应链攻击（如 Shai-Hulud 蠕虫、chalk 等包被注入恶意代码、Axios 被植入 RAT）均利用了自动执行的安装脚本，该 RFC 旨在通过默认禁止来消除此类攻击面。
- 🔧 分阶段实施：第一阶段仅发出警告，不阻止脚本；第二阶段将正式阻止未批准的脚本。同时提供`--dangerously-allow-all-scripts`等逃生舱口。
- 💬 社区讨论焦点：包括允许列表应放在`package.json`还是`.npmrc`（公开 vs 私有）、是否应基于脚本内容哈希而非仅包名来批准、以及如何避免用户“全部允许”的滥用行为。
- 🏢 兼容性考量：保留安装脚本功能是为了支持少量仍需此特性的合法包（如原生模块`canvas`、`sharp`、`sqlite3`），但通过精确的逐包允许列表来限制风险。

---

### [Jarred-Sumner 用 Rust 重写 Bun · 拉取请求 #30412 · oven-sh/bun · GitHub](https://github.com/oven-sh/bun/pull/30412)

**原文标题**: [Rewrite Bun in Rust by Jarred-Sumner · Pull Request #30412 · oven-sh/bun · GitHub](https://github.com/oven-sh/bun/pull/30412)

Bun 项目已成功用 Rust 重写，合并了 6755 个提交，通过了所有测试，并修复了内存泄漏和测试不稳定问题。

- 🚀 二进制体积缩小 3-8 MB，性能持平或更快
- 🐛 修复了多个内存泄漏和不稳定的测试
- 🛠️ 引入编译器辅助工具，可捕捉和预防内存错误
- 📐 架构和数据结构基本保持不变，仍使用少量第三方库
- ⚡ 未使用异步 Rust
- 🧪 在所有平台上通过了 Bun 原有的测试套件
- 🔄 可通过 `bun upgrade --canary` 试用
- 📝 后续还需进行优化和清理工作

---

### [声明式部分更新 | 博客 | Chrome 开发者](https://developer.chrome.com/blog/declarative-partial-updates)

**原文标题**: [Declarative partial updates  |  Blog  |  Chrome for Developers](https://developer.chrome.com/blog/declarative-partial-updates)

Chrome 团队推出“声明式局部更新”API，旨在打破 HTML 顺序加载的限制，通过两种新方式提升 Web 应用的性能和开发体验。

- 📜 **无序流式更新**：利用 `<template for>` 和 `<?marker>` 处理指令，允许 HTML 内容在文档中任意位置插入或替换，无需等待整个页面加载完毕。
- ⚡ **新 HTML 插入与流式 API**：提供 `setHTML`、`streamHTML` 等一致命名的静态和流式方法，支持动态注入 HTML，并内置安全消毒选项。
- 🎯 **主要用例**：支持岛屿架构、按需流式加载内容（如数据库查询结果）、优化页面加载顺序（如延迟加载大型菜单）。
- 🔒 **安全与限制**：`<template for>` 仅能在同一父元素内更新；新 API 默认启用消毒，`Unsafe` 版本需显式允许脚本执行。
- 🛠️ **兼容与未来**：Chrome 148 起可通过实验标志测试，并提供 polyfill；未来可能支持客户端包含、批量更新和版本控制。

---

### [QUIC 和 HTTP/3 终于登陆 Node.js | James M Snell](https://www.jasnell.me/posts/quic-comes-to-node)

**原文标题**: [QUIC and HTTP/3 Come To Node.js (finally) | James M Snell](https://www.jasnell.me/posts/quic-comes-to-node)

Node.js 终于原生支持 QUIC 和 HTTP/3 协议，目前处于实验阶段。

- 🚀 **QUIC 是什么**：基于 UDP 的传输协议，集成 TLS 1.3 加密，支持多路复用流、快速连接建立、连接迁移和内置流控。
- 🌐 **HTTP/3 是什么**：基于 QUIC 的 HTTP 版本，继承 QUIC 所有特性，使用 `node:quic` 模块默认 ALPN 为 `'h3'` 时获得 HTTP/3 会话。
- ⚙️ **为什么原生支持**：直接绑定 UDP 到事件循环、共享 TLS 基础设施、避免 JS/C++ 边界开销，基于 ngtcp2、nghttp3、OpenSSL 和 libuv。
- 🔧 **如何使用**：需要从源码构建并添加 `--experimental-quic` 标志，模块通过 `node:quic` 导入，仅支持 `node:` 协议。
- 📦 **核心对象**：`QuicEndpoint`（绑定 UDP 端口）、`QuicSession`（代表 QUIC 连接）、`QuicStream`（流式数据传输）、`QuicError`（错误处理）。
- 📝 **简单示例**：提供了回声服务器和客户端代码，使用 `listen()` 和 `connect()` 函数，支持 TLS 配置、流处理、优雅关闭和 `Symbol.asyncDispose` 自动清理。
- ⚠️ **实验性警告**：API 可能变化，功能未完全实现（如 HTTP/3 服务器推送），性能待优化，需在 GitHub 提交反馈。
- 🔮 **未来计划**：后续文章将深入端点生命周期、流传输、HTTP/3 集成、0-RTT、数据报和可观测性等高级主题。

---

### [发布 pnpm 11.2 · pnpm/pnpm · GitHub](https://github.com/pnpm/pnpm/releases/tag/v11.2.0)

**原文标题**: [Release pnpm 11.2 · pnpm/pnpm · GitHub](https://github.com/pnpm/pnpm/releases/tag/v11.2.0)

pnpm v11.2.0 发布，包含多项新功能和错误修复。

- 🚀 实验性功能：将 Rust 版的 pnpm（`@pnpm/pacquet`）加入 `configDependencies`，可让 pacquet 二进制文件接管 `pnpm install` 的物化阶段，pnpm 仍负责依赖解析。
- 🔧 `configDependencies` 现在支持解析和安装一层 `optionalDependencies`，并应用平台过滤，实现类似 esbuild/swc 的平台特定二进制包模式。
- 🔑 实现了 `pnpm login --scope <scope>` 标志，可自动写入 `@<scope>:registry=<registry>` 映射，使后续安装路由到指定仓库。
- 📊 `pnpm outdated` 和 `pnpm update --interactive` 现在会报告 Node.js、Deno 和 Bun 运行时依赖。
- 🐛 修复了 `cafile=<relative-path>` 在 `.npmrc` 中从错误目录读取的问题，现在路径会基于声明它的 `.npmrc` 目录解析。
- 🛠 修复了 `config.registry` 在 `.npmrc` 设置 `registry` 时被追加尾部斜杠的问题。
- 🧩 修复了全局 add/update 对 `minimumReleaseAge` 策略违规的处理错误。
- 🔧 修复了 `injectWorkspacePackages: true` 在锁文件被修剪时的两个崩溃问题。
- 🔄 修复了 `pnpm login` 和 `pnpm logout` 忽略 `pnpm-workspace.yaml` 中 `registries.default` 的问题。
- ⏱ 修复了 `minimumReleaseAge` 的截止时间包容性问题，避免不必要的全元数据重取。
- 📦 修复了发布包时未遵循 `publishConfig.access` 的问题。

---

### [pnpm/pacquet 主分支 · pnpm/pnpm · GitHub](https://github.com/pnpm/pnpm/tree/main/pacquet)

**原文标题**: [pnpm/pacquet at main · pnpm/pnpm · GitHub](https://github.com/pnpm/pnpm/tree/main/pacquet)

概述摘要
- ⚠️ pacquet 目前处于积极开发阶段，尚未准备好投入生产使用。
- 🔄 pacquet 是 pnpm 官方用 Rust 重写的 CLI 工具，完全复制 pnpm 的行为、标志、默认值、错误码、文件格式和目录布局。
- 🗺️ 项目分为两个阶段：第一阶段（当前重点）替换 pnpm 的获取和链接功能，预计使 pnpm 速度提升至少两倍；第二阶段将接管依赖解析。
- 📊 提供基准测试功能，详情见 CONTRIBUTING.md 文件。

---

### [发布 v4.15.0 · yarnpkg/berry · GitHub](https://github.com/yarnpkg/berry/releases/tag/%40yarnpkg%2Fcli%2F4.15.0)

**原文标题**: [Release v4.15.0 · yarnpkg/berry · GitHub](https://github.com/yarnpkg/berry/releases/tag/%40yarnpkg%2Fcli%2F4.15.0)

Yarnpkg/berry 发布了 v4.15.0 版本，包含多项修复、性能优化和新功能，并迎来了多位新贡献者。

- 🚀 修复 Next.JS 端到端测试问题
- ⚡ 优化插件性能：跨工作区缓存安装状态
- 🛠️ 正确支持 Unicode 路径的补丁处理
- 🔐 支持在 CircleCI 上使用 OIDC 发布
- 🧹 忽略旧的 YARN_IGNORE_SCRIPTS 环境变量
- ❌ 拒绝含有首尾空格的依赖名，避免重复安装
- ⚙️ 使 pnpm 安装并发数可配置
- 🧩 停止在 Node 26.1.0+ 中使用 EDABF 解决方案
- 🕐 默认启用 npmMinimalAgeGate: 1d 设置
- 👥 新增 7 位贡献者，包括首次贡献者

---

### [Node.js — Node.js 26.2.0（当前版本）](https://nodejs.org/en/blog/release/v26.2.0)

**原文标题**: [Node.js — Node.js 26.2.0 (Current)](https://nodejs.org/en/blog/release/v26.2.0)

Node.js 26.2.0 版本发布，带来多项功能增强和修复。

- 📝 `stream.compose` 标记为稳定功能
- 🕐 `fs` 模块新增 `Temporal.Instant` 支持到 `Stats` 和 `BigIntStats`
- 📡 `http` 模块新增 `writeInformation` 方法，可发送任意 1xx 状态码
- 🔐 `crypto` 模块多项增强：支持 ML-DSA/ML-KEM、ChaCha20-Poly1305、AES-KW，并改进安全性
- 🛠️ 更新多个依赖：undici 8.3.0、corepack 0.35.0、sqlite 3.53.1、simdjson 4.6.4 等
- 📚 文档改进：包括流迭代、HTTP2、构建指南等更新
- 🧪 测试修复：减少测试不稳定性和超时问题
- 🏃 测试运行器：新增标签选项和标签名称过滤功能
- 🔄 QUIC 实现：完成内部实现，支持 `--allow-net` 权限
- 🐛 修复：模块同步钩子、REPL 历史去重、SQLite 备份等问题

---

### [Webpack 5.107 | webpack](https://webpack.js.org/blog/2026-05-19-webpack-5-107/)

**原文标题**: [Webpack 5.107 | webpack](https://webpack.js.org/blog/2026-05-19-webpack-5-107/)

Webpack 5.107 发布，引入实验性 HTML 模块和 TypeScript 支持，以及多项 CSS 和 JavaScript 改进。

- 🧪 **实验性 HTML 模块**：通过 `experiments.html` 标志启用，允许从 JavaScript 导入 HTML 文件，并自动解析其中的 `<img src>`、`<link href>`、`<style>` 和 `<script src>` 引用，替代了 `html-loader` 的功能。
- 🆕 **实验性 TypeScript 支持**：通过 `experiments.typescript` 标志启用，利用 Node.js 内置的类型擦除功能直接编译 `.ts` 文件，无需 `ts-loader` 或 `swc-loader`，但仅支持可擦除的 TypeScript 语法。
- 🎨 **CSS 改进**：包括 CSS 模块的作用域提升、纯模式检查、`@value` 在 `@import` 和 `url()` 中的使用、`exportsConvention` 支持多别名，以及新增 `linkInsert` 和 `orderModules` 钩子。
- 📦 **JavaScript 和 ESM 优化**：新增 `anonymousDefaultExportName` 选项控制匿名默认导出的命名行为，保留外部依赖的 `defer` 和 `source` 阶段关键字，并支持 `#__NO_SIDE_EFFECTS__` 注释以优化 tree shaking。
- 🔧 **解析器更新**：在默认条件名称中添加了 `module-sync`，以对齐 Node.js 的同步加载 ESM 支持。
- 🐛 **错误修复**：修复了自 5.106 版本以来的多个问题，详情请查看更新日志。

---

