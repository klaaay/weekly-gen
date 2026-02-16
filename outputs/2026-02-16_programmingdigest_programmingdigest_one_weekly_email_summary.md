### [我的 AI 采用之旅——米切尔·哈希莫托](https://mitchellh.com/writing/my-ai-adoption-journey)

**原文标题**: [My AI Adoption Journey – Mitchell Hashimoto](https://mitchellh.com/writing/my-ai-adoption-journey)

作者分享了自己从对 AI 持怀疑态度到有效利用 AI 工具的个人历程，强调通过具体实践和策略调整来逐步实现效率提升，而非盲目追随炒作。

- 🚫 **放弃聊天机器人**：停止通过聊天界面进行编码工作，因其效率低下且结果不可靠，转而使用具备文件读取、程序执行等能力的智能体（Agent）。
- 🔁 **复制自身工作**：强制自己用智能体重现手动完成的任务，通过实践发现最佳使用方式，如拆分任务、让智能体验证自身工作，并明确其擅长与不擅长的领域。
- ⏰ **每日结束前启动智能体**：在每天最后 30 分钟启动智能体进行深度研究、探索模糊想法或处理 GitHub 任务，利用自己效率较低的时间段取得进展。
- 🏀 **外包确定性任务**：将智能体擅长且能可靠完成的任务（如解决特定类型的问题）委托给其在后台处理，同时自己专注于其他深度工作，并关闭通知以避免分心。
- 🔧 **设计控制工具**：通过改进提示（如更新 AGENTS.md 文件）或编写脚本工具，让智能体能够自我验证和纠正错误，防止重复犯错，提升其首次成功率。
- 🔄 **保持智能体持续运行**：努力让智能体始终在后台执行有益任务，结合使用速度较慢但质量更高的模型，平衡手动工作与自动化辅助，目前仍在逐步提高这一比例。

---

### [了解你工作方式的 AI 代码审查](https://getunblocked.com/code-review/?utm_source=programmingdigest&utm_medium=email&utm_campaign=codereview&utm_content=260216_primary)

**原文标题**: [AI Code Review That Knows How You Work](https://getunblocked.com/code-review/?utm_source=programmingdigest&utm_medium=email&utm_campaign=codereview&utm_content=260216_primary)

Unblocked 是一款 AI 代码审查工具，通过整合团队的代码库、历史决策、文档和沟通记录，提供基于上下文的精准审查，减少无关反馈，专注于逻辑错误和关键问题。

- 🧠 基于团队记忆：参考 Slack 讨论、过往 PR 和文档决策，而非通用最佳实践，避免提出无关的风格建议
- 🏗️ 系统感知：理解系统架构和约束，标记与现有模式冲突的问题（如同步/异步调用不匹配）
- 🔍 CI 故障分析：自动分析构建失败日志，在 PR 中提供具体修复建议（如协议缓冲区字段冲突）
- 💬 交互式功能：支持 PR 内聊天提问、请求示例或测试，并生成包含相关背景的 PR 摘要
- 🔗 知识图谱构建：连接代码库、对话、文档和规划系统，构建动态知识地图，依据团队真实标准进行审查
- 🔒 企业级安全：具备 SOC 2 Type II 合规、权限感知和细粒度访问控制，支持私有仓库
- ⚙️ 快速集成：支持主流编程语言，10 分钟内完成设置，提供 21 天免费试用

---

### [无需嵌入的语义搜索](https://softwaredoug.com/blog/2026/01/08/semantic-search-without-embeddings.html)

**原文标题**: [Semantic Search Without Embeddings](https://softwaredoug.com/blog/2026/01/08/semantic-search-without-embeddings.html)

本文探讨了语义搜索的多种实现方式，指出向量搜索并非唯一方案，并介绍了基于分类体系的替代方法及其在现代技术下的新优势。

- 🔍 语义搜索的核心在于将查询和内容映射到共享表示空间，并通过相似度函数进行匹配，但传统方法常忽略匹配标准的重要性。
- 🧠 向量嵌入是当前语义搜索的默认方案，通过训练数据学习表示，但存在新项目冷启动和缺乏精确匹配能力的问题。
- 🌳 分类体系（如管理词汇表或分类法）提供了另一种语义搜索路径，通过层级结构映射查询和内容，并天然支持匹配判断。
- ⚙️ 利用分层标记化技术，可在传统 BM25 索引中实现分类体系的相似度评分，使搜索结果按相关性层级排序。
- 🤖 大语言模型（LLMs）显著简化了分类体系的构建与管理，能够辅助自动分类、增强标注，并提升语义搜索的实用性。
- 🛠️ 实际应用中可结合多种方法（如关键词匹配、向量搜索和分类体系）构建混合搜索系统，以平衡精度与覆盖范围。
- 🚀 建议从简单的分类结构开始，逐步迭代细化，并注意分类体系与用户实际语言和需求的对应关系。

---

### [完美代码审查：如何在提升质量的同时减轻认知负担——丹尼尔·巴斯特里奇](https://bastrich.tech/perfect-code-review/)

**原文标题**: [The PERFECT Code Review: How to Reduce Cognitive Load While Improving Quality â Daniil Bastrich](https://bastrich.tech/perfect-code-review/)

本文概述了构建高效代码审查流程的 PERFECT 原则，旨在降低认知负荷并提升代码质量。通过明确审查目的、处理边界情况、确保可靠性、遵循设计形式、验证测试证据、提升代码清晰度及管理主观偏好，使审查过程结构化、清晰且一致。

- 🎯 **目的**：代码必须解决既定任务，这是首要且不可妥协的要求。审查者需先理解任务目标，再验证代码实现是否符合预期。
- 🚧 **边界情况**：识别并处理业务与技术上的边界情况，如异常输入、边界值、空值等，能显著减少生产环境中的错误。
- 🔒 **可靠性**：确保代码无性能与安全问题，避免引入明显瓶颈或安全漏洞，这对商业或关键项目尤为重要。
- 🏗️ **形式**：代码应符合设计原则（如高内聚低耦合），提升可读性与可维护性，减少长期维护成本。
- ✅ **证据**：测试与持续集成流程必须通过，确保代码处于可部署状态，测试覆盖应遵循约定且避免仅为测试而写的特殊逻辑。
- 📖 **清晰度**：代码应清晰传达意图，通过命名、结构等约定提升可读性，便于他人理解与维护。
- 👅 **品味**：个人偏好不应阻碍变更，缺乏依据的主观意见可被忽略，但有价值的建议可转化为团队共识。

---

### [获取失败](https://lemire.me/blog/2026/02/08/the-cost-of-a-function-call/)

**原文标题**: [Failed to retrieve](https://lemire.me/blog/2026/02/08/the-cost-of-a-function-call/)

无法总结：获取内容失败，状态码 520。

---

### [游戏中的道路艺术](https://sandboxspirit.com/blog/art-of-roads-in-games/)

**原文标题**: [Art of Roads in Games](https://sandboxspirit.com/blog/art-of-roads-in-games/)

本文探讨了游戏中道路设计的艺术与技术挑战，从玩家对道路美学的着迷出发，分析了现有游戏道路系统的局限，并提出了基于真实工程原理的改进方案。

- 🛣️ 作者从小时候玩《模拟城市 2000》开始就对道路设计着迷，认为道路是城市建造类游戏的基石
- 🎮 回顾了《模拟城市 4》《模拟城市 2013》《都市：天际线》等游戏在道路设计上的演进，指出即使有模组加持，仍存在不自然之处
- 📐 揭示了游戏常用贝塞尔曲线生成道路的缺陷：偏移时无法保持平行，导致急弯处几何失真
- ⭕ 提出圆形弧线作为替代方案，因其偏移后仍保持平行，且计算复杂度远低于贝塞尔曲线
- 🚗 进一步引入回旋曲线（clothoid），它能实现曲率平滑变化，更符合高速行驶的工程需求，但数学实现复杂
- 🔧 作者因好奇心和现有教程的不足，决定自己开发更真实的道路系统，并预告将分享技术细节

---

### [获取失败](https://ricomariani.medium.com/software-performance-engineering-the-ideas-i-keep-coming-back-to-6f421b6a9505)

**原文标题**: [Failed to retrieve](https://ricomariani.medium.com/software-performance-engineering-the-ideas-i-keep-coming-back-to-6f421b6a9505)

无法总结：获取内容失败，状态码 403。

---

