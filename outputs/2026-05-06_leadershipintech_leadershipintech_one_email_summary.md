### [少测多学：用更少、更高质量的指标捕捉关键信息](https://discord.com/blog/measure-less-to-learn-more-using-fewer-higher-quality-metrics-to-capture-what-matters)

**原文标题**: [Measure Less to Learn More: Using Fewer, Higher-quality Metrics to Capture What Matters](https://discord.com/blog/measure-less-to-learn-more-using-fewer-higher-quality-metrics-to-capture-what-matters)

Discord 團隊發現，過多的實驗指標會因多重比較問題導致假陽性增加或真實效果被掩蓋。透過減少指標數量並使用高品質、非重複的指標，能顯著提升實驗的檢驗能力。

- 📉 **指標過多的問題**：當實驗包含100個指標時，即使設定5%的顯著性門檻，平均也會有5個指標因隨機波動而顯示顯著，導致假陽性。
- ⚖️ **多重比較校正的取捨**：使用 Benjamini-Hochberg 校正可控制假陽性率，但會使真實效果更難被檢測到（降低召回率）。
- 🧪 **模擬驗證**：透過5萬次模擬實驗證明，指標數量越多，校正越嚴格，召回率越低；減少指標能同時改善假陽性率和召回率。
- 🔗 **識別冗餘指標**：利用相關性分析和主成分分析（PCA）發現，許多指標（如參與度相關）高度相關，可合併或刪除而不損失重要信號。
- ✂️ **精簡成果**：將預設指標從約50個削減至約15個，成功將檢測中等大小真實效果的能力提升了約45%。
- 🧠 **未來方向**：計畫採用經驗貝葉斯方法設定更準確的先驗機率、自動化冗餘檢測，以及進一步整合為綜合評估指標（OEC），以持續優化實驗效率。

---

### [从云原生到AI原生 | re:cinq](https://re-cinq.com/ai-native?utm_source=leadership-in-tech&utm_medium=newsletter&utm_campaign=book-ai-native-free&utm_term=2026-05-04&utm_content=default)

**原文标题**: [From Cloud Native to AI Native | re:cinq](https://re-cinq.com/ai-native?utm_source=leadership-in-tech&utm_medium=newsletter&utm_campaign=book-ai-native-free&utm_term=2026-05-04&utm_content=default)

本内容介绍了一本免费电子书《从云原生到AI原生》，旨在帮助技术领导者理解并完成从云原生到AI原生的范式转变，并提供了一套实用框架和模式。

- 📚 **免费获取完整版书籍**：限时免费下载原价26.99美元的422页完整版电子书，非摘要或节选，亚马逊畅销书排名第一，评分4.8。
- ❌ **常见错误做法**：许多组织将AI视为工具升级而非范式转变，在遗留系统上简单叠加AI，导致战略惰性。
- 🧩 **五大核心挑战**：AI工具不成熟、缺乏最佳实践、AI技能缺口大、开发框架过时、以及“时间反转”（AI生成代码快，人类验证成瓶颈）。
- 🗺️ **创新浪潮与六种运营模式**：书中提供创新浪潮模型（瀑布→云原生→AI原生）和六种运营模式（开拓、启动、扩展、优化、创新、退出），指导组织转型。
- 🃏 **119个模式语言**：包含“战略惰性”、“盲从采用”、“增量伪装”、“时间反转”等119个命名模式、陷阱和反模式，为团队提供共享词汇。
- 🤖 **AI原生范式核心**：AI作为系统内在核心而非附加功能，涵盖模型中心架构、自主进化系统等，强调人类聚焦意图、伦理和验证。
- 📖 **真实案例与配套工具**：包含成功转型组织的详细案例研究，并提供实体/数字“模式卡片”和“AI原生评估”工具，支持团队实践。
- 👥 **作者背景**：由re:cinq公司CEO Pini Reznik和CTO Michael Müller合著，两人均有丰富的云原生转型实战经验。
- 📘 **前作延续**：本书是2019年O'Reilly出版的《云原生转型》的续作，帮助已实现云原生的组织迎接AI原生浪潮。

---

### [管理一个并非由你选择的团队](https://newsletter.manager.dev/p/managing-a-team-that-didn-t-choose-you)

**原文标题**: [Managing a team that didn't choose you](https://newsletter.manager.dev/p/managing-a-team-that-didn-t-choose-you)

### 概述总结
一位工程经理在接管非自己组建的团队后，分享了6个月的真实反思，强调适应团队需求比遵循预设计划更重要。

- 📋 **初始计划失败**：原计划前6-8周专注技术学习，但发现团队刚经历重组、缺乏管理，急需支持，因此立即转向人员管理。
- 👥 **团队优先**：团队由资深工程师组成，技术能力已很强，最需要的是建立团队凝聚力和流程，而非技术指导。
- 🚨 **过度推动问题**：为追求早期成功，在首个冲刺中强制加班，导致团队压力过大，直到资深工程师提醒才调整节奏。
- 🔧 **忽视支持工作**：前两个月专注于交付，忽略了21张积压的工单，后来通过“修复冲刺”和亲自参与支持工作解决。
- 🔄 **持续适应**：团队经历重组和个人休假后，计划再次失效，证明唯一有效的是不断观察、调整和倾听反馈。
- 💡 **核心教训**：不要害怕打破“前30天只学习”的规则，根据团队实际需求灵活行动，并接受变化是常态。

---

### [如何进行一对一沟通 | 本·巴尔特](https://ben.balter.com/2026/04/27/one-on-one-playbook/)

**原文标题**: [How to one-on-one | Ben Balter](https://ben.balter.com/2026/04/27/one-on-one-playbook/)

以下是根据您提供的文章内容整理的摘要：

一对一会议应避免用于状态更新，而应专注于职业发展、指导、反馈和人际连接，并像对待重要事务一样保护会议时间。

- 📋 **核心内容**：一对一会议应聚焦于职业成长、辅导、反馈、人际连接和澄清问题，而非状态更新或信息传递。
- 📝 **准备方法**：使用共享议程提前添加议题并附上背景，优先处理重要事项，确保会议无法被轻易取消。
- 🗣️ **会议执行**：从人性化问候开始，多提问少给答案，灵活跟随议程，为未说出口的话题留出空间，并明确下一步行动。
- 🔗 **跳级会议**：定期与上级的上级进行跳级一对一，有助于建立关系、获取组织视角和提升职业可见度。
- ❌ **避免的反模式**：避免无准备的“幽灵会议”、频繁取消、管理者独白或报告单向汇报。
- ✅ **真正考验**：优秀的一对一会议体现了领导能力，包括共享议程、记录结果和异步准备，是分布式团队成功的关键。

---

### [在团队中建立影响力 - 罗曼·尼古拉耶夫](https://highimpactengineering.substack.com/p/building-influence-within-the-team)

**原文标题**: [Building Influence Within the Team - by Roman Nikolaev](https://highimpactengineering.substack.com/p/building-influence-within-the-team)

### 概述总结
团队影响力并非来自自我牺牲或空洞鼓励，而是通过推动切实的积极变革、以身作则、庆祝小进步，并避免成为“传声筒”或言行不一的管理者来逐步建立。

- 📉 **失败案例**：一位新经理试图通过独自承担最烦人的测试任务来建立影响力，但忽略了团队缺乏所有权和内部冲突的根本问题，最终导致士气更低落，自己也不得不放弃管理职位。
- ✅ **建立影响力的方法**：影响力通过“以身作则”和“寻找第二玩家”来放大。管理者应持续展示期望的行为，并与团队中的正式或非正式领导者合作，共同推动改变。
- 🎉 **庆祝小进步**：从零到一的微小变革值得庆祝。完成一个改进后，一定要在团队中公开认可，这既能提升士气，也能巩固管理者的影响力。
- ❌ **破坏影响力的行为**：两大忌是“软弱”和“不一致”。软弱指没有自己的观点，只做上级的传声筒；不一致指言行不一，不兑现承诺，这会迅速摧毁信任。
- 💡 **管理的本质**：所有管理都是变革管理。真正的领导力在于驱动团队变得更好、更有成就感，而非忙于执行具体任务（如写代码）。管理职责永远优先于个人贡献。

---

### [克劳德调度与接口的力量](https://www.oneusefulthing.org/p/claude-dispatch-and-the-power-of)

**原文标题**: [Claude Dispatch and the Power of Interfaces](https://www.oneusefulthing.org/p/claude-dispatch-and-the-power-of)

以下是您提供的文章摘要：

AI的能力远超大多数人的认知，但聊天界面限制了其发挥，导致用户认知负荷过重。未来，更专业的界面、个人代理和按需生成的界面将改变这一现状。

- 🧠 **聊天界面造成认知负担**：研究表明，使用聊天机器人处理复杂任务时，用户需承受“精神税”，尤其对经验不足者影响更大，因为AI会输出冗长文本并主动提供无关信息。
- 💻 **专业界面（如编程工具）**：Claude Code等编程代理功能强大，但专为程序员设计，界面复杂（如1980年代风格），不适合99%的非开发知识工作者。
- 🔧 **面向非开发者的实验性界面**：Google的Stitch（自然语言生成应用）、Pomelli（自动生成营销活动）和NotebookLM（多源信息研究）展示了未来方向，但仍未达到编程工具的变革性水平。
- 📱 **个人代理（如OpenClaw与Claude Dispatch）**：OpenClaw通过WhatsApp等熟悉应用实现AI代理，但存在安全风险；Claude Dispatch则让用户通过手机远程控制桌面AI，执行复杂任务（如更新PPT图表），虽不完美但显著节省时间。
- 🎨 **按需生成界面**：最新AI系统（如Claude）能动态生成交互式可视化或自定义应用，无需预先设计固定界面，未来AI将主动适应人类需求，而非相反。

---

### [实用AI软件咨询](https://testdouble.com/solutions/pragmatic-ai?utm_medium=newsletter-ads&utm_source=leadership-in-tech&utm_campaign=pragmatic-ai&utm_content=dread-ai-office-hours)

**原文标题**: [Pragmatic AI Software Consultancy](https://testdouble.com/solutions/pragmatic-ai?utm_medium=newsletter-ads&utm_source=leadership-in-tech&utm_campaign=pragmatic-ai&utm_content=dread-ai-office-hours)

以下是您提供的文本的摘要：

概述总结
该内容介绍了Test Double公司提供的三种AI服务：AI Proof Sprint、AI Traction Sprint和加速遗留系统现代化。这些服务旨在帮助团队快速验证AI应用、提升工程团队的AI能力，以及利用AI加速遗留系统的改造。服务以固定价格$25,000提供两周的嵌入式咨询，强调从业务问题出发，与团队协作，并交付可复用的成果。

- 🚀 **AI Proof Sprint**：两周内帮助团队识别最高影响力的AI应用领域，并构建可运行的示例，包括基线评估、实时证明和90天路径规划，价格为$25,000。
- 📈 **AI Traction Sprint**：针对软件工程团队，通过嵌入方式衡量并缩小团队在AI使用上的差距，提供能力基线、机会地图和实时证明，价格为$25,000。
- 🔧 **加速遗留系统现代化**：结合AI工具与技术专长，加速遗留系统的分析、升级和测试，包括代码分析、Rails升级和自动化测试设计。
- 🤖 **技术与技巧**：支持多种AI模型、工具和技术，如代理编码、上下文工程、数据工程，以及自定义代理和提示工程，适应团队现有流程。
- 💡 **核心价值**：强调务实AI方法，专注于业务目标，避免为AI而AI，确保质量与安全，从策略到执行提供全面支持。

---

### [西方忘记了如何建造，现在又忘记了代码。](https://techtrenches.dev/p/the-west-forgot-how-to-make-things)

**原文标题**: [The West Forgot How to Build. Now It's Forgetting Code](https://techtrenches.dev/p/the-west-forgot-how-to-make-things)

### 概述总结
西方在制造业和国防领域因长期优化成本、忽视知识传承而失去生产能力，如今软件行业正重蹈覆辙，用AI替代人类工程师可能导致隐性知识断层，未来将面临同样的危机。

- 🚀 **国防工业的惨痛教训**：雷神公司为重启“毒刺”导弹生产，不得不请回70多岁退休工程师，从40年前纸质图纸重新学习，交付周期长达四年。
- 📉 **欧洲弹药承诺落空**：欧盟承诺一年内提供100万枚炮弹，但实际产能仅23万枚/年，最终延迟9个月才达标，暴露了供应链单一依赖和长期投资不足。
- 🏭 **“整合或死亡”的后遗症**：1993年五角大楼推动国防承包商从51家合并为5家，导致弹药供应链单点故障频发，如弹壳制造商位于地震带上，且无法应对危机时的产能激增。
- 🧪 **知识消失的典型案例**：美国核武器材料“雾堤”因停产20年，原工人退休或去世后，政府耗费6900万美元仍无法复制，甚至发现原工艺依赖未知杂质——隐性知识彻底丢失。
- 💻 **软件行业正在重演历史**：AI工具让开发者效率提升（实际研究显示反而慢19%），但企业减少招聘初级工程师，导致新人缺乏调试和纠错经验，形成“AI中介能力”而非真才实学。
- ⏳ **重建时间无法压缩**：国防领域恢复产能需3-10年，软件工程师培养同样需要5-10年才能成为系统级专家，而AI无法替代隐性知识和危机判断力。
- 🔍 **招聘数据揭示危机**：作者团队最近一次招聘中，2253名候选人仅4人被录用（转化率0.18%），说明兼具技术能力和AI纠错判断力的人才极度稀缺。
- 📋 **文档无法替代经验**：团队虽已建立详尽文档，但若未来工程师缺乏基础能力，这些文档将无人能解读——正如“雾堤”案例中，原始工人自己都未完全理解工艺。

---

### [GitHub Copilot 将转向基于使用量的计费 - GitHub 博客](https://github.blog/news-insights/company-news/github-copilot-is-moving-to-usage-based-billing/)

**原文标题**: [GitHub Copilot is moving to usage-based billing - The GitHub Blog](https://github.blog/news-insights/company-news/github-copilot-is-moving-to-usage-based-billing/)

### 概述总结
GitHub Copilot 将于2026年6月1日起，从高级请求计费模式转为基于使用量的账单模式，引入“GitHub AI Credits”概念，按Token消耗计费。

- 🔄 **计费模式变更**：自2026年6月1日起，所有Copilot计划将采用基于使用量的账单，用GitHub AI Credits取代高级请求单位（PRUs），按输入、输出和缓存Token消耗计费。
- 💡 **原因解析**：Copilot已从编辑器助手演变为代理平台，使用最新模型进行长时间多步骤编码，导致推理成本激增。旧模式无法持续，新计费方式能更好对齐实际使用，确保服务可靠性和可持续性。
- 📅 **关键时间点**：2026年6月1日正式生效。个人用户（月付）自动迁移；年付用户保持原计划至到期，之后转为免费版或升级月付。企业用户自动获得6-8月促销额度（Business $30/月，Enterprise $70/月）。
- 💰 **价格不变**：基础计划价格未变：Pro $10/月，Pro+ $39/月，Business $19/用户/月，Enterprise $39/用户/月。代码补全和Next Edit建议仍免费。
- 🚫 **功能调整**：不再提供降级回退体验。代码审查将额外消耗GitHub Actions分钟数。
- 🔧 **新工具与控制**：企业用户可设置预算控制（企业、成本中心、用户级别），并支持组织内额度池化，避免浪费。个人用户可通过账单概览页面预览预估成本。
- 📊 **促销与过渡支持**：现有企业客户在6-8月自动获得额外月度AI Credits，帮助平稳过渡。个人年付用户若提前转为月付，可获得按比例计算的信用额度。

---

### [荷兰央行选择Lidl作为欧洲云服务提供商 - Techzine Global](https://www.techzine.eu/news/infrastructure/140634/dutch-central-bank-chooses-lidl-for-european-cloud/)

**原文标题**: [Dutch central bank chooses Lidl for European Cloud - Techzine Global](https://www.techzine.eu/news/infrastructure/140634/dutch-central-bank-chooses-lidl-for-european-cloud/)

荷兰央行选择Lidl旗下欧洲云服务，以减少对美国云服务商的依赖。

- 🏦 荷兰央行（DNB）明日将与Lidl母公司施瓦茨集团的IT部门签署大合同，转向欧洲云服务
- 🌍 此举旨在降低对美国云服务商的依赖，应对地缘政治风险（如特朗普切断ICC邮件账户事件）
- ⚠️ DNB承认欧洲云平台“不如美国云成熟”，但认为这是必要权衡
- 🇪🇺 施瓦茨数字通过Stackit平台提供主权云，数据受欧洲法律保护，不受美国《云法案》约束
- 💰 施瓦茨数字近期投资110亿欧元在吕伯瑙建设大型数据中心
- 🚂 已有Lidl、考夫兰、德国铁路等大型组织使用该云服务
- 📉 荷兰央行和AFM去年警告金融部门过度依赖美国IT服务商
- 🔄 类似迁移案例：石勒苏益格-荷尔斯泰因州政府从微软迁移至开源环境遇到困难

---

### [获取失败](https://www.bloomberg.com/news/articles/2026-04-27/microsoft-to-stop-sharing-revenue-with-main-ai-partner-openai)

**原文标题**: [Failed to retrieve](https://www.bloomberg.com/news/articles/2026-04-27/microsoft-to-stop-sharing-revenue-with-main-ai-partner-openai)

无法总结：获取内容失败，状态码 403。

---

### [新款10GbE USB适配器更凉爽、更小巧、更便宜 - Jeff Geerling](https://www.jeffgeerling.com/blog/2026/new-10-gbe-usb-adapters-cooler-smaller-cheaper/)

**原文标题**: [New 10 GbE USB adapters are cooler, smaller, cheaper - Jeff Geerling](https://www.jeffgeerling.com/blog/2026/new-10-gbe-usb-adapters-cooler-smaller-cheaper/)

### 概述总结
新型 RTL8159 芯片的 10 GbE USB 适配器比 Thunderbolt 适配器更小巧、凉爽且价格更低，但实际速度取决于电脑的 USB 端口规格。

- 📏 **更小巧的设计**：新型 10G USB 适配器体积远小于传统的 Thunderbolt 适配器，携带更方便。
- 💰 **价格更低**：WisdPi 的 10G 适配器售价 80 美元，比 Thunderbolt 适配器便宜一半以上。
- 🔥 **散热更好**：运行温度仅 42.5°C，不像 Thunderbolt 适配器那样烫手，功耗约 0.86 瓦。
- ⚡ **速度受端口限制**：仅在使用 USB 3.2 Gen 2x2（20 Gbps）端口时才能达到满速 10 Gbps，否则只有 6-7 Gbps。
- 🖥️ **兼容性差异**：Mac 即插即用，但 Windows 需安装驱动；Mac 速度稳定但略低，Windows 速度波动大。
- 🏷️ **USB 命名混乱**：Windows 将所有 USB 3.x 显示为“3.0”，难以判断端口实际速度，建议查阅规格表。
- 💡 **性价比建议**：若不需要满速 10 Gbps，2.5G 或 5G 适配器（如 WisdPi 5G 售价 30 美元）性价比更高。
- 🛒 **更多选择**：AliExpress 上有多种替代品，或可选购 PCI Express 卡版本绕过 USB 限制。

---

### [复制失败 — CVE-2026-31431](https://copy.fail/)

**原文标题**: [Copy Fail — CVE-2026-31431](https://copy.fail/)

概述总结
- ❌ CVE-2026-31431（Copy Fail）是一个影响所有2017年后Linux发行版的内核漏洞，无需竞争条件即可实现100%可靠的本地提权。
- 🔓 漏洞利用仅需732字节Python脚本，通过authencesn逻辑缺陷、AF_ALG和splice()链式调用，实现4字节页缓存写入。
- 🎯 已验证影响Ubuntu 24.04、Amazon Linux 2023、RHEL 10.1、SUSE 16等主流发行版，其他发行版同样受影响。
- 🛡️ 高风险场景包括多租户Linux主机、Kubernetes容器集群、CI运行器、云SaaS平台等，低风险场景为单用户工作站。
- 📥 PoC已发布，可验证系统安全性，但需在授权环境下使用。
- 🔧 缓解措施：优先更新内核至包含修复补丁的版本；补丁前可通过禁用algif_aead模块防御。
- ⏳ 披露时间线：2026年3月23日报告，4月29日公开披露。
- 🧠 漏洞由Xint Code通过AI扫描发现，其工具可在约一小时内审计Linux crypto/子系统。

---

### [GitHub RCE漏洞：CVE-2026-3854深度解析 | Wiz博客](https://www.wiz.io/blog/github-rce-vulnerability-cve-2026-3854)

**原文标题**: [GitHub RCE Vulnerability: CVE-2026-3854 Breakdown | Wiz Blog](https://www.wiz.io/blog/github-rce-vulnerability-cve-2026-3854)

概述总结
Wiz研究团队在GitHub内部git基础设施中发现了一个严重漏洞（CVE-2026-3854），允许任何认证用户通过一次git push命令在GitHub.com和GitHub Enterprise Server上实现远程代码执行。该漏洞利用内部协议中的字段注入，影响数百万仓库，GitHub在6小时内修复了在线服务，但88%的GHES实例仍存在风险。

- 🔍 **漏洞发现**：Wiz研究团队通过AI增强的反向工程工具（IDA MCP）发现CVE-2026-3854，这是首个利用AI在闭源二进制文件中发现的严重漏洞。
- ⚡ **利用方式**：任何认证用户只需使用标准git客户端执行`git push -o`命令，通过注入分号到X-Stat头字段，即可覆盖安全配置并执行任意命令。
- 🏢 **影响范围**：在GitHub.com上，攻击者可访问共享存储节点上的数百万公共和私有仓库；在GHES上，可完全控制服务器，访问所有仓库和内部机密。
- 🛡️ **修复措施**：GitHub在报告后6小时内修复了GitHub.com，并发布了GHES补丁（版本3.19.3及更高），但88%的GHES实例仍易受攻击。
- 🔗 **攻击链**：通过注入三个字段（rails_env、custom_hooks_dir、repo_pre_receive_hooks）绕过沙箱、重定向钩子目录并执行路径遍历，最终实现RCE。
- 🌐 **跨租户风险**：在GitHub.com上，由于共享基础设施，攻击者可能读取其他组织和用户的仓库内容，但研究仅用自有账户验证了权限。
- ⏰ **披露时间线**：2026年3月4日发现并报告，3月10日分配CVE并发布补丁，4月28日公开披露。
- 💡 **安全建议**：GHES管理员应立即升级到3.19.3或更高版本，Wiz客户可使用预构建查询识别易受攻击实例。

---

### [fast16 | 神秘影子经纪人参考揭示震网前5年的高精度软件破坏 | SentinelOne](https://www.sentinelone.com/labs/fast16-mystery-shadowbrokers-reference-reveals-high-precision-software-sabotage-5-years-before-stuxnet/)

**原文标题**: [fast16 | Mystery ShadowBrokers Reference Reveals High-Precision Software Sabotage 5 Years Before Stuxnet | SentinelOne](https://www.sentinelone.com/labs/fast16-mystery-shadowbrokers-reference-reveals-high-precision-software-sabotage-5-years-before-stuxnet/)

SentinelLABS 发现了一个名为 fast16 的高级持续性威胁 (APT) 框架，其核心组件可追溯至 2005 年，比臭名昭著的 Stuxnet 蠕虫还要早五年。该框架通过一个内核级驱动程序，利用嵌入式 Lua 虚拟机，对高精度计算软件进行内存补丁，以实现精确的软件破坏。其名称 "fast16" 出现在 NSA 的 ShadowBrokers 泄露文件中，表明其与国家背景的关联。该攻击框架是已知最早针对物理世界进行网络破坏的案例之一。

- 🔍 **历史性发现**：fast16 框架的核心组件编译于 2005 年，比 Stuxnet 早五年，是已知最早利用嵌入式 Lua 虚拟机进行模块化设计的国家级恶意软件框架。
- 🎯 **精确破坏目标**：其内核驱动 `fast16.sys` 专门针对使用 Intel C/C++ 编译器编译的 `.EXE` 文件，通过内存补丁注入浮点运算指令，以微小但系统性的错误破坏物理模拟、结构工程等高精度计算结果。
- 🧬 **模块化架构**：载体模块 `svcmgmt.exe` 内嵌 Lua 5.0 虚拟机，通过加密的 Lua 字节码实现配置、传播、内核驱动部署等逻辑，具备极高的适应性和可重用性。
- 🕸️ **蠕虫式传播**：该框架具备自我复制能力，通过 Windows 服务控制和文件共享 API 在网络中传播，旨在使整个设施内的计算都产生一致的错误结果，从而掩盖破坏行为。
- 🕳️ **NSA 关联**：其名称 "fast16" 出现在 ShadowBrokers 泄露的 NSA "Territorial Dispute" 工具清单中，作为避免内部冲突的排除标记，证实了其与国家行为体的关联。
- 🧩 **疑似攻击目标**：通过模式匹配，研究人员发现其补丁目标极有可能指向 LS-DYNA（用于核武器模拟）、PKPM（中国建筑结构设计软件）和 MOHID（水动力模型）等高精度工程与科学计算软件。
- 🛡️ **高度隐蔽性**：该样本在 VirusTotal 上近十年几乎零检出，其代码中包含反分析机制，例如检查安全软件注册表键值，并在启动时禁用 Windows 预取功能。
- ⚙️ **Unix 血统**：代码中残留的 SCCS/RCS 版本控制标记表明其开发者可能来自长期使用 Unix 环境的高安全背景团队，进一步佐证其国家级工具的出身。

---

### [如何做到直接且具有策略性——赵越](https://news.theuncommonexecutive.com/p/how-to-be-direct-and-strategic)

**原文标题**: [How To Be Direct And Strategic  - by Yue Zhao](https://news.theuncommonexecutive.com/p/how-to-be-direct-and-strategic)

以下是根据您提供的文章内容整理的摘要：

直截了当且具有策略性的沟通方式，需要将直接与未经筛选区分开来。策略性沟通者会花时间管理沟通的时机和方式，并准备好如何让对方接受信息。

- 🎯 不要将策略性沟通误解为不真实或操纵；它本质上是基于同理心和关怀，考虑对方的背景和感受。
- 🧠 在关键对话前，思考三个问题：对方已有的信念、对话可能引发的情绪、以及需要先说什么来打开话题。
- 💡 直接意味着快速切入核心问题，但策略性沟通能避免触发防御心理，让对话更有效。
- 🚫 避免三种常见陷阱：认为好想法应自动被接受、不愿说对方想听的话、以及将策略性沟通视为操纵。
- ✅ 策略性沟通不是欺骗，而是沟通卓越的最佳实践，能让你的真实和正直更闪耀。
- 📈 通过调整沟通方式（如先询问对方看法再引入反馈），可以改变对话结果，即使事实不变。

---

