### [程序员如何分配时间 | 或许在跳舞](https://probablydance.com/2026/02/10/how-programmers-spend-their-time/)

**原文标题**: [How Programmers Spend Their Time | Probably Dance](https://probablydance.com/2026/02/10/how-programmers-spend-their-time/)

本文作者分享了一次修复代码 bug 的经历：一个仅需 10 秒的代码修改，却耗费了超过 10 小时的时间。整个过程涉及多个步骤，包括调试、使用工具、构建环境、版本问题等，揭示了程序员在实际工作中大量时间消耗在非编码任务上，如应对系统层级、构建工具、依赖管理和版本控制等挑战。

- 🐛 同事遇到一个 cudnn attention 随机崩溃的 bug，初步排查无果，怀疑是已有 bug 被触发。
- ⏳ 花费数小时尝试复现 bug，但进展缓慢，因为 bug 难以稳定重现。
- 🛠️ 尝试使用 compute sanitizer 工具，但遇到测试环境沙箱限制，浪费约 1 小时解决运行问题。
- 🔍 在测试框架外运行 compute sanitizer，快速发现内存问题，但需关闭 pytorch 缓存分配器才能暴露。
- 🧩 尝试修复张量填充不一致的问题，花费 10 分钟，但 bug 依然存在，随后发现另一处需填充的张量。
- 🐞 检查 flash-attention 代码，发现一个明显的释放后使用 bug，但修复需自行构建 wheel 包验证。
- 💻 在家用电脑尝试构建 flash-attention，遇到构建系统问题、CUDA 版本冲突和编译缓慢，耗时约 2 小时。
- 🔧 第二天发现系统包冲突，花费 45 分钟修复驱动和 CUDA 环境，重新构建。
- 🤦 构建成功后无法复现 bug，发现 GPU 仅支持 flash-attention 2，而 bug 存在于 flash-attention 3。
- 🖥️ 在工作电脑上尝试构建，遇到编译器版本、CUDA 和 Python 兼容性问题，甚至编译器崩溃，最终耗时 1 小时解决。
- 🔄 构建后导入出错，发现编译器版本不兼容，切换后重新编译。
- 📁 意识到一直在编译 flash-attention 2，实际 bug 在“hopper”子目录的版本 3 中，重新构建。
- 🧪 复现 bug 失败，发现相关功能在最新版本中被硬编码禁用，bug 实际上被缓存分配器掩盖。
- ✍️ 撰写博客时注意到功能已恢复，重新构建并成功复现 bug，最终修复并提交 pull request。
- ⏱️ 整个修复过程耗时超 10 小时，突显了程序员大量时间花在环境配置、构建系统和版本管理上，而非实际编码。

---

### [构建与购买认证方案——FusionAuth](https://fusionauth.io/buildvsbuy?utm_campaign=38862912-NL-2026-02-Programming_Digest&utm_source=Programming_Digest&utm_medium=Newsletter)

**原文标题**: [Build vs Buy Authentication - FusionAuth](https://fusionauth.io/buildvsbuy?utm_campaign=38862912-NL-2026-02-Programming_Digest&utm_source=Programming_Digest&utm_medium=Newsletter)

FusionAuth 是一款企业级客户身份和访问管理（CIAM）平台，提供高度可定制、安全的认证与授权解决方案，支持自托管或云端部署，旨在帮助组织在控制成本的同时快速实现生产就绪的身份验证。

- 🏆 **行业认可**：被 G2 报告评为 2026 年 CIAM 领域的势头领导者。
- 🔐 **全面功能**：提供多因素认证、单点登录、无密码登录、社交登录、高级威胁检测、API 优先架构等丰富身份管理功能。
- ☁️ **部署灵活**：支持自托管或在 FusionAuth Cloud 上托管，确保数据主权和完全控制。
- 💰 **成本效益**：通过总拥有成本计算器显示，相比自建或传统 SaaS 方案，FusionAuth 在三年内可节省大量费用。
- ⚙️ **高度可定制**：允许完全自定义登录界面、业务流程，并支持与现有系统深度集成。
- 🛡️ **安全合规**：已获得 SOC 2、ISO 27001、GDPR、HIPAA 等多项合规认证，提供企业级安全保障。
- 🚀 **快速集成**：提供多语言 SDK、详细文档和快速入门指南，帮助开发团队在几天内完成生产级集成。
- 📊 **成功案例**：服务于金融科技、低代码平台、旅游等多个行业，处理千万级用户并实现显著的成本节约与性能提升。

---

### [238. 软件之死？不。](https://hardcoresoftware.learningbyshipping.com/p/238-death-of-software-nah)

**原文标题**: [238. Death of Software. Nah.](https://hardcoresoftware.learningbyshipping.com/p/238-death-of-software-nah)

AI 不会终结软件，而是改变软件的内容与开发者，但软件需求将大幅增长。文章通过回顾个人电脑、零售和媒体三大领域的转型历史，说明技术变革往往带来扩张而非取代，新工具和领域经验将变得更加重要，同时创新与淘汰并存，但整体发展需要时间和耐心。

- 💻 个人电脑的普及并未消灭大型机，反而推动了数据中心和云计算的发展，命令行界面至今仍是基础
- 🛒 在线零售并未摧毁实体零售，而是催生了全渠道模式，亚马逊和沃尔玛以不同方式主导市场
- 📺 媒体行业历经多次“消亡”预言，却通过流媒体、用户生成内容等形式爆发式增长，内容总量远超以往
- 🚀 AI 将推动软件数量激增，因为它能解决尚未满足的广泛需求，从个人工具到企业系统
- 🔧 AI 软件将向上整合到产品栈中，就像软件融入银行、旅游等行业，催生新旧公司的变革
- 🛠️ AI 将创造实现新功能的新工具，改善工作、协作和交通等众多尚未数字化的领域
- 🧠 领域经验变得至关重要，因为各行业将变得更加复杂，客户和从业者都需要更高技能
- ⏳ 转型周期远长于预期，需要耐心；部分公司会被淘汰，但整体行业将扩大并多样化

---

### [未找到标题](https://postgreslocksexplained.com/)

**原文标题**: [No title found](https://postgreslocksexplained.com/)

该网站由一位专注于 Postgres 管理与可观测性的客户可靠性工程师创建，旨在提供关于 Postgres 锁机制的全面学习资源，包括概念解释、监控工具、故障排查及实际案例，以帮助他人更高效地理解和应对锁相关问题。

- 🧠 解释锁的基本概念，通过动画使内容更易理解
- 🛠️ 演示表锁操作，提供实际运行示例
- 📊 展示交互式锁阻塞图，说明 SQL 操作间的互锁关系
- 🔍 指导如何识别和解决常见的锁问题
- 📈 评测常用监控工具并分享自制解决方案
- 📝 计划补充更多主题，如概念详解、工具评测和故障排查

---

### [迈克尔·阿布拉什如何将《雷神之锤》帧率翻倍](https://fabiensanglard.net/quake_asm_optimizations/index.html)

**原文标题**: [How Michael Abrash doubled Quake framerate](https://fabiensanglard.net/quake_asm_optimizations/index.html)

本文通过实验验证了 Michael Abrash 的手写汇编优化确实使《雷神之锤》的帧率翻倍，并深入分析了关键优化函数及其实现原理。

- 🎮 实验证实，关闭汇编优化后游戏帧率从 42.2fps 降至 22.7fps，性能确实减半。
- 🔍 关键优化集中在底层绘制函数，其中 D_DrawSpans8 贡献最大（提升 12.6fps），其次是 R_DrawSurfaceBlock8_mip*（4.2fps）和 D_Polyset*（2.2fps）。
- ⚙️ TransformVector 函数通过并行计算三个点积、利用 Pentium FPU 流水线和延迟隐藏，避免了 VC6 编译器生成的代码中的停顿。
- 🔄 R_DrawSurfaceBlock8_mipX 采用自修改代码、循环展开和避免分支预测，将光照与纹理合并循环优化至每纹理 2.25 周期。
- 🧩 D_DrawSpans8 通过重叠 FDIV 除法与整数像素绘制、使用跳转表避免分支预测，以及巧妙的无符号比较实现边界裁剪，极大提升了渲染效率。
- 📚 这些优化体现了 Abrash 对 Pentium 架构的深刻理解，尤其是在整数与浮点流水线并行执行方面的极致追求。

---

### [获取失败](https://lukasniessen.medium.com/how-to-make-architecture-decisions-rfcs-adrs-and-getting-everyone-aligned-ab82e5384d2f)

**原文标题**: [Failed to retrieve](https://lukasniessen.medium.com/how-to-make-architecture-decisions-rfcs-adrs-and-getting-everyone-aligned-ab82e5384d2f)

无法总结：获取内容失败，状态码 403。

---

### [未找到标题](https://www.vpdae.com/redirect/kjn7znz7k07snaptplkn1rtekys)

**原文标题**: [No title found](https://www.vpdae.com/redirect/kjn7znz7k07snaptplkn1rtekys)

无法总结：未找到主要内容。

---

### [我的 AI 应用之旅——米切尔·哈希莫托](https://mitchellh.com/writing/my-ai-adoption-journey)

**原文标题**: [My AI Adoption Journey – Mitchell Hashimoto](https://mitchellh.com/writing/my-ai-adoption-journey)

作者分享了自己从对 AI 持怀疑态度到有效将其融入软件开发工作流的个人历程，强调通过具体步骤和实践找到实用价值，而非盲目追随炒作。

- 🚫 **放弃聊天机器人**：停止通过聊天界面进行实质性编码工作，因其在复杂项目中效率低下，结果不可靠。
- 🔄 **复制自身工作**：强制自己用智能体重新完成已手动完成的任务，以此学习如何有效分解任务、验证工作，并理解智能体的能力边界。
- ⏰ **安排下班前智能体**：在每日最后 30 分钟启动智能体，处理深度研究、探索性想法或问题分类等任务，利用非工作时间取得进展。
- 🏀 **外包“扣篮”任务**：将高成功率的确定性任务委托给智能体在后台处理，同时自己专注于其他创造性或复杂工作，并避免通知干扰。
- 🔧 **设计“约束框架”**：通过改进提示词或编写工具，系统化地防止智能体重复犯错，并使其能自我验证，提升首次成功率。
- ♻️ **保持智能体持续运行**：以始终有一个智能体在后台运行为目标，将其视为持续的辅助，但仅在存在有价值任务时才启用，避免为用而用。

---

