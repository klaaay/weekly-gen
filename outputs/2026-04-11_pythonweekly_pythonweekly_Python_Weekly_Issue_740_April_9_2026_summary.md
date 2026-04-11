### [您能主办2027年欧洲Django大会吗？诚邀组织者 | 博客 | Django](https://www.djangoproject.com/weblog/2026/apr/07/could-you-host-djangocon-europe-2027-call-for-orga/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-740-april-9-2026)

**原文标题**: [Could you host DjangoCon Europe 2027? Call for organizers | Weblog | Django](https://www.djangoproject.com/weblog/2026/apr/07/could-you-host-djangocon-europe-2027-call-for-orga/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-740-april-9-2026)

DjangoCon Europe 2027 正在公开征集主办团队，欢迎有兴趣的个人或团体提交申请，主办方将提供全面的支持与指导，包括联系往届组织者和协助预算规划等，申请截止日期为2026年6月1日。

- 🗓️ **申请时间线**：主办方需在2026年6月1日前提交详细提案，初步意向可提前提交以获取协助。
- 🏛️ **主办资格**：欢迎欧洲任何城市申请，无论是否有过往经验，重点是热情、组织能力和团队合作。
- 🤝 **支持体系**：DSF活动支持工作组将提供全程帮助，包括预算规划、法律实体建议和往届经验分享。
- 📋 **提案内容**：需包含组织团队、法律实体、举办日期、场地详情、交通住宿、预算票价等基本信息。
- 🌍 **举办日期**：2027年会议需避开主要社区活动（如PyCon US、EuroPython）和重大节假日，建议在1月初至4月底或6月初至6月底之间举行。
- 💰 **资金与资源**：DSF可能提供高达6000美元的资助，并有社交媒体、行为准则等工作组提供额外支持。
- 📧 **申请步骤**：先提交意向表，随后与支持组沟通完善提案，最终提交完整方案。

---

### [编码智能体的构成要素 - Sebastian Raschka博士著](https://magazine.sebastianraschka.com/p/components-of-a-coding-agent?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-740-april-9-2026)

**原文标题**: [Components of A Coding Agent - by Sebastian Raschka, PhD](https://magazine.sebastianraschka.com/p/components-of-a-coding-agent?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-740-april-9-2026)

本文概述了编码代理（coding agent）的核心设计，重点解析了其六大组件如何通过工具、记忆和仓库上下文等系统层增强大语言模型在实际编码任务中的表现。

- 🏗️ **编码代理与工具框架**：编码代理（如Claude Code、Codex CLI）是在大语言模型外包裹的一层“代理框架”（agent harness），通过整合仓库上下文、工具调用和记忆管理等系统能力，显著提升模型在编码任务中的实用性和效率。
- 🔄 **三层架构关系**：大语言模型是核心的下一代词元生成引擎；推理模型是在此基础上优化、能输出中间推理步骤的增强版引擎；而代理则是在模型之上构建的控制循环，负责决策、工具调用和环境交互。
- 🛠️ **六大核心组件**：
  1. **实时仓库上下文**：代理在开始工作前会主动收集Git仓库状态、项目文档等“稳定事实”作为工作区摘要，确保模型不是从零开始，而是基于具体项目环境进行操作。
  2. **提示构建与缓存复用**：系统将指令、工具描述和工作区摘要等稳定内容构建为“稳定提示前缀”并缓存，避免每次交互都重新生成，从而提升效率并降低计算开销。
  3. **结构化工具访问与使用**：代理通过预定义的工具列表（如读取文件、运行命令）进行结构化操作，框架会验证工具参数、检查路径权限并在必要时请求用户批准，在提升安全性的同时确保可靠性。
  4. **上下文膨胀管理**：针对多轮对话中容易积累的冗长文件内容、工具输出和日志，代理采用剪裁、去重和摘要等策略压缩历史记录，优先保留近期相关信息，以维持提示上下文的清晰与相关。
  5. **结构化会话记忆**：代理将状态分为两层：完整的会话转录（存储所有历史记录，支持会话恢复）和精简的工作记忆（提炼当前任务的关键信息），分别用于长期存储和即时任务连续性。
  6. **有界子代理委托**：主代理可以将子任务（如查找符号定义、分析测试失败原因）委托给子代理并行处理。子代理会继承必要的上下文，但其操作范围（如只读权限、递归深度）受到约束，以防止任务失控或资源冲突。

---

### [异步Python的秘密确定性 | DBOS](https://www.dbos.dev/blog/async-python-is-secretly-deterministic?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-740-april-9-2026)

**原文标题**: [Async Python is Secretly Deterministic | DBOS](https://www.dbos.dev/blog/async-python-is-secretly-deterministic?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-740-april-9-2026)

在Python持久化执行库中添加异步支持时，我们面临一个核心挑战：持久化工作流必须具有确定性，以实现基于重放的恢复。异步Python工作流因并发执行多个步骤而难以保证确定性，但通过深入理解事件循环的FIFO调度机制，我们利用`@Step()`装饰器在步骤首次await前分配确定性ID，从而兼顾并发性能与可靠重放。

- 🔄 **并发与确定性的矛盾**：异步工作流通过`asyncio.gather`并发执行步骤以提升性能，但步骤执行顺序的不确定性阻碍了故障恢复时的重放。
- ⚙️ **事件循环调度原理**：异步Python基于单线程事件循环，任务按FIFO顺序调度，仅在通过await主动交出控制权时切换，这为预测执行顺序提供了基础。
- 🏷️ **确定性ID分配方案**：在`@Step()`装饰器中，于步骤首次await操作前从工作流上下文分配递增的步骤ID，确保即使并发任务也能按初始调度顺序获得唯一标识。
- 🧠 **单线程模型优势**：虽然单线程限制并行性，但任务仅通过await显式切换，使得执行逻辑更易推理，为编写并发安全代码提供了便利。
- 🛠️ **DBOS实践应用**：该方案已应用于DBOS持久化工作流库，通过结合事件循环特性与装饰器拦截，实现了高性能并发与可靠恢复的平衡。

---

### [用50行Python实现去中心化人工智能——我是特拉斯克](https://iamtrask.github.io/2026/04/07/decentralized-ai-in-50-lines/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-740-april-9-2026)

**原文标题**: [Decentralized AI in 50 Lines of Python - i am trask](https://iamtrask.github.io/2026/04/07/decentralized-ai-in-50-lines/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-740-april-9-2026)

本文介绍了如何用约50行Python代码构建一个点对点（P2P）的本地AI助手，通过WhatsApp接收消息，并基于本地数据与发送者特定的上下文文件夹进行个性化回复，同时保护隐私。这是“从零开始构建去中心化AI”系列的基础教程。

- 🧠 **核心概念**：构建一个本地运行的AI助手，使用Ollama运行开源语言模型，通过文件夹管理上下文数据，实现个性化回复。
- 🔧 **技术实现**：使用Python脚本处理消息，结合Node.js和Ollama搭建本地环境，通过文件夹结构区分公共和私人上下文。
- 📁 **数据管理**：利用`OMBox`文件夹存储上下文文件，通过读取文件夹内容动态构建AI的“大脑”，支持灵活扩展。
- 🛡️ **隐私保护**：为不同联系人创建独立文件夹，仅共享特定上下文，避免敏感信息泄露，即使面临提示注入攻击。
- 📱 **集成通信**：通过JavaScript桥接器连接WhatsApp，实现消息的自动收发，仅处理以“om”开头的消息。
- 🌐 **去中心化理念**：强调用户自主控制数据和模型，通过通用协议（如自然语言）实现跨平台互操作性，降低对单一平台的依赖。
- 🔮 **未来展望**：探讨去中心化AI在多方通信、治理模型和扩展性方面的潜力，以及如何应对上下文窗口限制等挑战。

---

### [TorchTPU：在谷歌规模上原生运行PyTorch于TPU平台](https://developers.googleblog.com/torchtpu-running-pytorch-natively-on-tpus-at-google-scale/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-740-april-9-2026)

**原文标题**: [
            
            TorchTPU: Running PyTorch Natively on TPUs at Google Scale
            
            
            - Google Developers Blog
            
        ](https://developers.googleblog.com/torchtpu-running-pytorch-natively-on-tpus-at-google-scale/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-740-april-9-2026)

Google推出TorchTPU，使PyTorch能够原生高效运行在TPU硬件上，旨在为开发者提供易用、可移植且高性能的AI开发体验，以支持大规模分布式AI模型训练。

- 🚀 **推出TorchTPU**：实现PyTorch在TPU上的原生高效运行，支持大规模AI模型训练。
- 🎯 **核心设计原则**：注重易用性、可移植性和高性能，开发者只需更改初始化设置即可迁移现有PyTorch代码。
- 🔧 **三种Eager执行模式**：提供调试、严格和融合模式，融合模式可自动优化操作，提升性能50%至100%以上。
- 🧩 **静态编译集成**：通过torch.compile和XLA后端实现全图编译，生成高度优化的TPU二进制文件。
- 🌐 **分布式训练支持**：兼容DDP、FSDPv2和DTensor等PyTorch分布式API，并支持MPMD执行模式。
- ⚙️ **硬件感知优化**：提供指导帮助开发者调整模型以充分利用TPU硬件特性，如优化注意力头维度。
- 📅 **2026年路线图**：包括公开GitHub仓库、动态形状支持、自定义内核扩展以及与vLLM等生态工具的深度集成。

---

### [使用Django在数据库中强制执行业务逻辑 | Lincoln Loop](https://lincolnloop.com/blog/enforce-business-logic-in-the-database-with-django/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-740-april-9-2026)

**原文标题**: [Enforce Business Logic in the Database with Django | Lincoln Loop](https://lincolnloop.com/blog/enforce-business-logic-in-the-database-with-django/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-740-april-9-2026)

在Django项目中，数据库是数据真实性的核心来源，因此确保其数据符合业务逻辑至关重要。通过数据库层面的约束、事务和锁机制，可以有效保障数据一致性和完整性，同时减少应用代码中的冗余检查。

- 🔄 使用事务（`transaction.atomic`）确保相关数据库操作要么全部成功，要么全部回滚，例如创建用户时同步创建用户档案。
- ⚠️ 注意默认的`ATOMIC_REQUESTS`设置可能在高流量场景下引发性能问题，建议结合`on_commit`处理耗时操作。
- 🔍 在并发环境下，“不可重复读”可能导致数据异常，如库存扣减出现负值。
- 🔒 通过`select_for_update`锁定数据库行，防止并发修改，确保业务规则（如库存检查）在事务间得到严格执行。
- 📏 利用Django的约束类（如`CheckConstraint`、`UniqueConstraint`）在数据库层强制实施业务规则，例如字段取值范围、互斥关系或条件唯一性。
- 🧹 约束能自动集成到模型验证中，替代繁琐的自定义`clean()`方法，提升代码简洁性与数据可靠性。
- ⏱️ 尽量缩短持有锁的事务时间，避免阻塞其他操作，优化系统性能。

---

### [梯度提升参数](https://statmills.com/2026-04-06-gradient_boosted_splines/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-740-april-9-2026)

**原文标题**: [Gradient Boosting Parameters](https://statmills.com/2026-04-06-gradient_boosted_splines/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-740-april-9-2026)

本文介绍了如何将梯度提升机（GBM）的原理应用于预测模型参数，而不仅仅是单一目标值，从而扩展GBM在平滑样条、生存分析和概率模型等复杂场景中的应用。通过具体案例——使用GBM学习自行车共享数据中每日骑行量随时间变化的样条函数系数，作者演示了如何将传统GBM优化过程转化为多参数优化，并利用Jax自动计算梯度，结合决策树迭代拟合，最终生成平滑的预测曲线。这一方法不仅提供了更灵活的建模工具，也深化了对梯度提升机制的理解。

- 🚀 扩展GBM应用：利用梯度提升原理预测模型参数（如样条系数），适用于平滑样条、生存分析等复杂模型。
- 📊 案例背景：使用纽约Citi Bike四年每小时骑行数据，包含日期、温度、降水等特征，目标是学习每日24小时骑行量的样条函数系数。
- 🔄 优化过程：将GBM的梯度下降步骤转化为多参数优化，通过计算损失函数对系数的梯度，用决策树预测梯度并更新参数。
- ⚙️ 技术实现：使用Jax自动计算梯度，结合Scikit-Learn的决策树进行迭代拟合，初始系数设为平坦线，逐步优化至生成平滑曲线。
- 🌳 树分裂逻辑：通过评估特征值（如星期几）对骑行量形状的影响，选择最佳分裂点，实现基于损失函数的监督聚类。
- 📉 效果对比：相比传统GBM直接预测每小时骑行量，梯度提升样条模型能一次性学习整体曲线形状，更清晰捕捉工作日与周末的差异。
- 🔍 模型输出：最终模型为每个观测日预测一组样条系数，应用于基函数后生成24小时平滑预测曲线，损失值显著降低。
- 💡 核心价值：该方法将GBM的扩展性与灵活参数化结合，只需定义损失函数和参数预测方式，即可适配多种模型类型。

---

### [Django表格、筛选与使用Htmx导出 | Fundor333](https://fundor333.com/post/2026/django-table-filter-export-with-htmx/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-740-april-9-2026)

**原文标题**: [Django Table, Filter and Export With Htmx | Fundor333](https://fundor333.com/post/2026/django-table-filter-export-with-htmx/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-740-april-9-2026)

本文介绍如何在Django项目中结合使用Htmx、Django-table2和Django-filters，实现数据表格展示、筛选和导出功能，并提供可复用的通用视图与模板代码。

- 🛠️ 通过整合ExportMixin、SingleTableMixin和FilterView创建通用视图，支持表格渲染、数据筛选及多格式导出（CSV、XLS等）。
- 📄 设计通用模板，利用条件判断动态控制筛选器和导出按钮的显示，提升代码复用性。
- 🔗 结合Htmx实现动态内容加载，示例中通过URL参数隐藏筛选器并保留导出功能。
- 📦 依赖Django-table2、django-filter和tablib等库，简化开发流程。
- 🔄 作者将代码重构为模块化组件，便于在不同项目中共享和导入。

---

### [Qdrant：Python中RAG的理想向量存储库 - YouTube](https://www.youtube.com/watch?v=DWP_-jMTNH0&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-740-april-9-2026)

**原文标题**: [Qdrant: Perfect Vector Store For RAG in Python - YouTube](https://www.youtube.com/watch?v=DWP_-jMTNH0&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-740-april-9-2026)

该文本为YouTube网站页脚链接列表，概述了其提供的各类信息与功能入口。

- ℹ️ 关于平台的基本信息与公司介绍
- 📰 新闻稿与媒体相关资源
- ©️ 版权政策与知识产权说明
- 📞 用户联系与反馈渠道
- 🧑‍🎨 创作者服务与支持内容
- 📢 广告合作与营销解决方案
- 👨‍💻 开发者工具与API资源
- 📜 服务条款与使用协议
- 🔒 隐私保护与数据政策
- ⚙️ 平台安全与内容规范
- 🔧 YouTube功能运作机制说明
- 🧪 新功能测试与体验计划
- ®️ 谷歌公司版权声明（至2026年）

---

### [如何实际运用Python的heapq解决第K大问题 | LoopPass博客](https://looppass.mindmeld360.com/blog/python-heapq-kth-largest/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-740-april-9-2026)

**原文标题**: [How to Actually use Python's heapq for Kth Largest Problems | LoopPass Blog](https://looppass.mindmeld360.com/blog/python-heapq-kth-largest/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-740-april-9-2026)

本文介绍了如何利用Python的heapq模块高效解决寻找第K大元素的问题，重点讲解了使用大小为K的最小堆策略，而非传统的最大堆方法。

- 🐍 使用Python的heapq模块时，需注意它仅支持最小堆，直接使用heapify_max()可能导致错误
- 🔄 通过数值取负可以模拟最大堆，但处理海量数据时内存效率低下
- 🎯 高效策略是维护一个大小为K的最小堆，仅保留当前最大的K个元素
- 📊 遍历数据时，若新元素大于堆顶，则替换堆顶元素，保持堆的大小始终为K
- 💡 该方法空间复杂度为O(K)，时间复杂度为O(N log K)，特别适合处理数据流场景
- 🧠 面试中展示此方法能体现对时间空间复杂度的深刻理解和实际问题解决能力

---

### [用Python学习无人机编程 – 教程 - YouTube](https://www.youtube.com/watch?v=k-yDYgc8AmU&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-740-april-9-2026)

**原文标题**: [Learn Drone Programming with Python – Tutorial - YouTube](https://www.youtube.com/watch?v=k-yDYgc8AmU&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-740-april-9-2026)

该内容为YouTube平台的政策与功能说明页面，主要介绍平台相关条款、开发者资源及用户权益信息。

- 📄 关于平台的基本信息与介绍
- 📢 媒体联系与新闻发布相关渠道
- ©️ 版权保护政策与侵权处理方式
- 📞 用户联系与反馈途径
- 👥 内容创作者支持与资源
- 📈 广告合作与商业推广机会
- 💻 开发者工具与API接口资源
- 📜 服务条款与使用协议
- 🔒 隐私保护政策与数据安全
- ⚙️ 平台运行机制与功能说明
- 🧪 新功能测试与体验计划
- ™️ 商标所有权与法律声明（截至2026年）

---

### [我用一个工具取代了Kafka、Redis和RabbitMQ，这是我的心得。](https://scalebites.substack.com/p/i-replaced-kafka-redis-and-rabbitmq?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-740-april-9-2026)

**原文标题**: [I Replaced Kafka, Redis, and RabbitMQ With One Tool. Here’s What I Learned.](https://scalebites.substack.com/p/i-replaced-kafka-redis-and-rabbitmq?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-740-april-9-2026)

本文介绍了作者使用NATS替代Kafka、Redis和RabbitMQ的经验，深入探讨了NATS的核心概念、JetStream持久化层、关键特性及其与Kafka的对比，并指出了NATS的优势与当前局限。

- 🚀 **NATS核心**：提供基于主题的发布/订阅模型，支持请求/回复、队列组等模式，所有功能构建于单一二进制文件之上。
- 📡 **主题与通配符**：使用点分隔的命名空间，支持`*`和`>`通配符进行灵活订阅，命名约定遵循“从通用到具体”的原则。
- 🔄 **请求/回复模式**：通过临时收件箱主题实现轻量级RPC，支持散射-收集模式，无响应时立即返回错误。
- 👥 **队列组**：实现消息在多个订阅者间的负载均衡，每个消息仅由一个工作节点处理，支持与普通订阅共存。
- 💾 **JetStream持久化**：为NATS添加持久化日志层，提供多种保留策略（如基于限制、基于兴趣、工作队列）。
- ⏳ **消息确认系统**：支持每条消息独立确认（Ack）、否定确认（Nak）、进行中标记（InProgress）和终止（Term），与Kafka的偏移量提交机制不同。
- 📊 **消费者类型**：推荐使用拉取消费者，支持Fetch、FetchNoWait和Consume三种消费方式，其中Consume在客户端内部隐藏了拉取循环。
- 🛡️ **死信队列**：通过MaxDeliver、Term和咨询主题组合实现，消息在达到最大投递次数或被终止后转入死信流。
- 🔒 **原子批量发布**（NATS 2.12+）：支持跨多个主题的原子性发布，确保所有消息全部提交或全部不提交。
- 📈 **扩展与排序**：无分区概念，通过增加工作节点横向扩展；默认不保证跨工作节点的按键排序，需通过特定模式或库实现。
- 🔄 **连接恢复**：客户端自动重连，JetStream消费者断线重连后可从服务器端游标恢复，无消息丢失。
- ⏸️ **消费者暂停**（NATS 2.11+）：可临时暂停消息投递至指定时间，用于维护、调试等场景。
- 🗃️ **数据存储**：提供KV存储和对象存储，均基于JetStream构建，分别适用于配置、状态管理和大型文件存储。
- ⚖️ **与Kafka对比**：NATS简化了分区规划和再平衡，但缺少Kafka的原子性读写事务和严格的按分区排序保证。
- 🏛️ **治理状态**：项目目前由CNCF托管，采用Apache 2.0许可证，由Synadia主导开发，结构稳定。

---

### [GitHub - tirth8205/code-review-graph：Claude代码的本地知识图谱。为您的代码库构建持久化地图，让Claude仅读取关键内容——代码审查时令牌数减少6.8倍，日常编码任务中最多减少49倍。· GitHub](https://github.com/tirth8205/code-review-graph?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-740-april-9-2026)

**原文标题**: [GitHub - tirth8205/code-review-graph: Local knowledge graph for Claude Code. Builds a persistent map of your codebase so Claude reads only what matters — 6.8× fewer tokens on reviews and up to 49× on daily coding tasks. · GitHub](https://github.com/tirth8205/code-review-graph?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-740-april-9-2026)

code-review-graph 是一个用于优化AI代码助手代码审查过程的工具，它通过构建代码知识图谱来减少令牌消耗，仅提供变更影响范围内的必要上下文。

- 🚀 **核心功能**：通过Tree-sitter解析代码构建AST图谱，增量追踪变更，为AI助手提供精准上下文，避免全量读取代码库。
- 📊 **性能优势**：平均减少8.2倍令牌使用，对大型单体仓库尤其有效，增量更新可在2秒内完成。
- 🌐 **语言支持**：支持19种编程语言及Jupyter笔记本，具备函数、类、导入、调用点、继承和测试检测的完整解析能力。
- 🔍 **智能分析**：提供爆炸半径分析，精确追踪变更影响的所有调用者、依赖项和测试，确保100%的召回率。
- 🛠️ **集成便捷**：通过MCP协议自动配置主流AI编码平台（如Claude Code、Cursor），支持命令行和交互式可视化。
- 📈 **评估指标**：包含完整的性能基准测试，涵盖令牌效率、影响准确性和构建性能，提供量化数据支持。
- ⚙️ **可扩展性**：提供22种MCP工具和5种工作流模板，支持语义搜索、社区检测、架构概述和重构工具等高级功能。

---

### [GitHub - Arthur-Ficial/apfel：命令行中的苹果智能。通过FoundationModels框架实现设备端LLM。无需API密钥、无需云端、无依赖。· GitHub](https://github.com/Arthur-Ficial/apfel?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-740-april-9-2026)

**原文标题**: [GitHub - Arthur-Ficial/apfel: Apple Intelligence from the command line. On-device LLM via FoundationModels framework. No API keys, no cloud, no dependencies. · GitHub](https://github.com/Arthur-Ficial/apfel?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-740-april-9-2026)

apfel 是一个开源命令行工具，让用户能够在本地 macOS 上直接调用 Apple Silicon 设备内置的 Apple Intelligence 大语言模型，无需 API 密钥、云端服务或订阅费用。

- 🍎 **核心功能**：作为 Apple FoundationModels 框架的封装，提供 CLI、HTTP 服务器和交互式聊天界面，实现完全在设备上的推理。
- 🖥️ **系统要求**：需 macOS 26 Tahoe 或更高版本、Apple Silicon 芯片（M1+），并已启用 Apple Intelligence 功能。
- 📦 **安装方式**：支持通过 Homebrew 一键安装或从源代码构建，安装后可通过 `apfel --model-info` 验证模型可用性。
- 🔧 **主要模式**：包括单次提示、流式输出、交互式聊天和兼容 OpenAI API 的本地服务器（默认端口 11434）。
- 📁 **文件处理**：支持通过 `-f` 参数附加多个文件内容到提示中，方便进行代码分析、文档对比等任务。
- 🛠️ **工具调用**：集成 MCP 工具服务器支持，可连接本地或远程工具（如计算器），实现自动化的函数调用。
- ⚙️ **高级配置**：提供温度、种子、最大令牌数等参数调整，以及多种上下文管理策略（如滑动窗口、总结压缩）。
- 🚀 **实用演示**：包含自然语言转 Shell 命令、复杂管道生成、系统状态叙述等示例脚本，展示实际应用场景。
- 🔒 **安全特性**：服务器模式支持令牌认证、CORS 配置和并发限制，并提供详细的权限管理选项。
- 📊 **性能信息**：模型上下文窗口为 4096 令牌，推理速度适中，完全在设备端运行，无网络延迟。

---

### [GitHub - KaiPereira/Overglade-Badges: 新加坡Overglade游戏开发马拉松的NFC黑客松徽章项目 · GitHub](https://github.com/KaiPereira/Overglade-Badges?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-740-april-9-2026)

**原文标题**: [GitHub - KaiPereira/Overglade-Badges: NFC hackathon badges for the Overglade game jam in Singapore! · GitHub](https://github.com/KaiPereira/Overglade-Badges?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-740-april-9-2026)

这是一个为新加坡Overglade游戏开发黑客松设计的零功耗徽章项目，基于RP2040芯片，具备被动NFC和电子墨水屏驱动功能。

- 🎨 **徽章设计**：采用对称的PCB艺术设计，配备20个GPIO引脚和4MB闪存
- ⚡ **零功耗特性**：核心功能无需电源，通过电子墨水屏保持显示
- 📱 **NFC功能**：支持被动/主动NFC模式，可自定义交互内容
- 🔧 **简易编程**：通过USB-C连接，使用Thonny上传Micropython固件
- 🖼️ **显示定制**：可替换位图图像和修改config.json配置文件
- 🏭 **生产制造**：建议通过JLC进行批量生产，单板成本约5美元
- 🤝 **社区贡献**：由HackClub高中生活动团队共同开发，感谢多位开发者参与

---

### [GitHub - ssrajadh/sentrysearch：使用Gemini Embedding 2或Qwen3-VL实现视频语义搜索。· GitHub](https://github.com/ssrajadh/sentrysearch?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-740-april-9-2026)

**原文标题**: [GitHub - ssrajadh/sentrysearch: Semantic search over videos using Gemini Embedding 2 or Qwen3-VL. · GitHub](https://github.com/ssrajadh/sentrysearch?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-740-april-9-2026)

SentrySearch 是一个基于语义的视频搜索工具，支持通过自然语言描述搜索视频片段，并自动剪辑匹配的内容。它提供云端（Gemini API）和本地（Qwen3-VL 模型）两种后端，适用于特斯拉行车记录仪等多种视频源，具备预处理、静帧跳过等优化功能，以提升搜索效率并控制成本。

- 🎥 **视频语义搜索** – 通过自然语言描述（如“红色卡车闯红灯”）直接搜索视频内容，无需文字转录或帧标注。
- ⚙️ **双后端支持** – 默认使用 Gemini API 进行云端嵌入，也支持本地 Qwen3-VL 模型以实现离线、私密搜索。
- 📦 **智能视频处理** – 自动将视频分割为重叠片段，进行降分辨率、降帧率等预处理，显著提升处理速度。
- 💾 **向量存储与匹配** – 使用 ChromaDB 存储视频片段的向量嵌入，通过向量相似度匹配返回最相关的结果。
- ✂️ **自动剪辑输出** – 搜索后自动从原始视频中裁剪出最佳匹配片段，并可选择保存多个结果。
- 🚗 **特斯拉元数据叠加** – 支持在剪辑片段上叠加速度、位置、时间等行车数据（需特定固件版本）。
- ⚡ **本地模型优化** – 通过量化、帧采样、维度截断等技术，在有限硬件上实现高效的本地推理。
- 💰 **成本控制机制** – 提供静帧跳过、调整片段时长/重叠等选项，帮助减少 Gemini API 的使用成本。
- 🛠️ **便捷管理功能** – 提供索引统计、文件移除、重置等命令，便于管理视频库和搜索数据。
- 📄 **广泛格式兼容** – 支持 .mp4 和 .mov 格式，不仅限于特斯拉，适用于各类视频素材。

---

### [GitHub - Netflix/void-model · GitHub](https://github.com/Netflix/void-model?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-740-april-9-2026)

**原文标题**: [GitHub - Netflix/void-model · GitHub](https://github.com/Netflix/void-model?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-740-april-9-2026)

Netflix开源的VOID项目是一个视频对象与交互删除系统，能够从视频中移除指定物体及其引发的所有交互效果，包括阴影、反射等次要效果以及物体掉落等物理交互。该系统基于CogVideoX构建，通过交互感知的掩码条件进行视频修复微调。

- 🎬 **项目概述**：VOID通过两阶段模型实现视频中物体及其交互效果的智能移除，确保移除后场景的自然连贯。
- 🛠️ **核心功能**：不仅能移除主要物体，还能同步处理其引发的物理交互（如被持物体掉落），使用四值掩码（quadmask）精确标记不同区域。
- 📦 **模型架构**：包含基础修复模型（Pass 1）和时序优化模型（Pass 2），支持单独或串联使用以提升时序一致性。
- 🚀 **快速开始**：提供Jupyter Notebook示例，需40GB+显存的GPU支持，可快速体验模型效果。
- ⚙️ **环境配置**：需安装依赖包、配置Gemini API密钥、单独安装SAM2，并下载预训练模型文件。
- 📁 **数据格式**：输入需包含原视频、四值掩码视频和背景描述JSON文件，描述移除物体后的场景状态。
- 🎭 **掩码生成流程**：通过GUI选择移除点，结合SAM2分割和VLM（Gemini）分析自动生成交互感知的四值掩码。
- 🖥️ **推理流程**：支持单次基础推理（Pass 1）和增强时序一致性的二次优化推理（Pass 2），可批量处理视频。
- ✏️ **手动优化**：提供GUI编辑器供用户手动修正自动生成的掩码，支持网格切换、画笔工具和帧间复制功能。
- 🏋️ **训练数据生成**：提供HUMOTO和Kubric两套数据生成流程，模拟物体移除前后的物理变化以构建训练数据。
- 🔧 **模型训练**：支持两阶段训练，分别优化基础修复能力和时序一致性，需多GPU环境运行。
- 🌐 **社区应用**：已推出Gradient交互演示，鼓励社区基于VOID进行二次开发和项目拓展。
- 📄 **引用信息**：项目相关论文已发布在arXiv，提供了标准的学术引用格式。

---

### [GitHub - JuliusBrussee/caveman: 🪨 能用少量词何必多费口舌 — 模仿原始人说话，Claude代码技能削减65%的令牌使用 · GitHub](https://github.com/JuliusBrussee/caveman?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-740-april-9-2026)

**原文标题**: [GitHub - JuliusBrussee/caveman: 🪨 why use many token when few token do trick — Claude Code skill that cuts 65% of tokens by talking like caveman · GitHub](https://github.com/JuliusBrussee/caveman?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-740-april-9-2026)

Caveman 是一个用于多种 AI 编程助手（如 Claude Code、Cursor 等）的技能/插件，通过模仿“穴居人”式的极简表达风格，在保持技术准确性的前提下，大幅减少 AI 输出的令牌（token）使用量，从而提升响应速度、可读性并降低成本。

- 🪨 **核心功能**：通过让 AI 使用省略填充词、使用短句和片语的“穴居人”说话风格，平均可减少约 65%-75% 的输出令牌，同时保持 100% 的技术准确性。
- ⚙️ **多级别模式**：提供“精简”、“完整”、“极致”和“文言文”四种压缩级别，用户可根据需求选择不同的简洁程度。
- 🤖 **广泛兼容**：支持 Claude Code、Codex、Gemini CLI、Cursor、Windsurf、Cline、GitHub Copilot 等超过 40 种 AI 代理和编辑器。
- 🛠️ **实用工具**：内置 `caveman-commit`（生成简洁提交信息）、`caveman-review`（单行代码审查）和 `caveman-compress`（压缩输入文件令牌）等增强技能。
- 📊 **效果验证**：提供基准测试和评估框架，证明其在多种编程任务中能显著减少令牌，部分场景节省高达 87%，且研究指出简洁约束有时能提升模型准确性。
- 🚀 **一键安装**：为不同平台和代理提供简单的安装命令（如 `npx skills add`），并可配置为会话自动启动。
- 📈 **核心优势**：提升响应速度、增强答案可读性、降低使用成本，并将每次代码审查变为有趣的体验。

---

### [GitHub - arman-bd/guppylm：一款约900万参数的LLM，说话像条小鱼。· GitHub](https://github.com/arman-bd/guppylm?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-740-april-9-2026)

**原文标题**: [GitHub - arman-bd/guppylm: A ~9M parameter LLM that talks like a small fish. · GitHub](https://github.com/arman-bd/guppylm?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-740-april-9-2026)

GuppyLM是一个约900万参数的小型语言模型，模拟一条名为Guppy的小鱼进行对话，专注于展示从零开始训练语言模型的完整流程，无需复杂资源。

- 🐟 项目核心为训练一个仅9M参数、模仿小鱼说话的轻量级语言模型，旨在通过简单流程揭示语言模型工作原理
- 🧪 采用极简Transformer架构（6层、384隐藏维度），使用合成生成的6万条对话数据，在单GPU上约5分钟完成训练
- 🌐 提供多种使用方式：浏览器WebAssembly本地运行、Colab在线体验、本地安装对话，以及完整训练代码
- 📚 项目结构清晰，包含数据生成、分词器训练、模型架构、训练循环和推理部署的全套工具
- 🎯 设计选择注重教学性：使用合成数据确保角色一致性、单轮对话避免上下文限制、简化架构降低理解门槛
- 📄 采用MIT开源协议，所有代码和预训练模型均已公开，包含详细文档和快速入门指南

---

### [GitHub - HKUDS/OpenHarness: OpenHarness：内置个人助手Ohmo的开源代理框架 · GitHub](https://github.com/HKUDS/OpenHarness?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-740-april-9-2026)

**原文标题**: [GitHub - HKUDS/OpenHarness: OpenHarness: Open Agent Harness with a built-in personal agent, Ohmo! · GitHub](https://github.com/HKUDS/OpenHarness?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-740-april-9-2026)

OpenHarness 是一个开源的 AI 代理基础设施框架，提供工具调用、技能、记忆和多代理协调等核心功能。其上层应用 ohmo 是一个基于此框架构建的个人 AI 代理，可在飞书、Slack 等聊天工具中运行，并自主执行编码、测试等任务。项目支持多种 LLM 提供商，强调安全性、可扩展性和社区驱动。

- 🧠 **核心架构**：提供完整的代理“马具”（Harness）基础设施，包括代理循环、工具集、技能系统、权限控制等 10 个子系统。
- 🛠️ **丰富工具**：内置 40 多种工具，涵盖文件操作、Shell、搜索、网络请求、MCP 协议集成及后台任务管理等。
- 📚 **技能与插件**：支持按需加载的 Markdown 技能文件，并与 Claude 官方技能及插件生态兼容，可扩展性强。
- 🛡️ **安全治理**：提供多级权限模式（默认、自动、计划模式）、路径级规则和命令黑名单，确保操作安全。
- 🤝 **多代理协调**：支持创建子代理、团队注册、任务管理，为多代理协作提供基础。
- 🚀 **快速启动**：通过一键安装脚本或 pip 安装，使用 `oh setup` 交互式向导配置提供商，即可运行。
- 🔌 **多提供商兼容**：原生支持 Claude、OpenAI、Copilot、Moonshot/Kimi 等多种 API，并可管理自定义兼容端点。
- 🧑‍💼 **个人代理 ohmo**：作为开箱即用的应用，可在聊天工具中部署，利用用户现有的 Claude Code 或 Codex 订阅运行。
- 🧪 **易于扩展**：允许开发者轻松添加自定义工具、技能和插件，框架代码结构清晰。
- 🌍 **社区与开源**：作为社区驱动的研究项目，欢迎在工具、技能、提供商支持等多方面贡献，采用 MIT 许可证。

---

### [GitHub - imbue-ai/mngr：用于管理编码代理的命令行界面 · GitHub](https://github.com/imbue-ai/mngr?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-740-april-9-2026)

**原文标题**: [GitHub - imbue-ai/mngr: CLI for managing coding agents · GitHub](https://github.com/imbue-ai/mngr?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-740-april-9-2026)

mngr 是一个类 Unix 工具，用于管理和运行 AI 编码代理，支持在本地、远程主机、容器等多种环境中并行部署和操作代理，其设计理念类似于“git for agents”，强调简单、快速、成本透明、安全和可组合性。

- 🛠️ **核心功能**：提供创建、销毁、列表、连接、消息传递、快照、克隆等命令，用于管理运行在 SSH、git 和 tmux 基础上的 AI 代理进程。
- 🌐 **灵活部署**：支持代理在本地、Docker 容器、Modal 云服务等多种提供商环境中运行，并可跨主机共享以节省成本。
- ⚡ **高效快速**：代理启动时间通常在 2 秒内，且具备空闲自动关闭机制，仅按实际使用的推理和计算资源付费。
- 🔒 **安全可控**：默认使用 SSH 密钥隔离，可限制网络访问，提供容器级控制，确保隐私和操作安全。
- 🔄 **可组合与可观测**：支持代理状态快照与分支、直接执行命令、持续数据同步，并提供消息记录和程序化交互能力。
- 📦 **易于使用与扩展**：通过简单命令即可操作，内置帮助问答功能，并可通过插件系统扩展代理类型、提供商后端和生命周期钩子。

---

### [GitHub - Obelus-Labs-LLC/WeThePeople：公民透明度平台，追踪八大行业企业对国会的影响。整合30多个政府API，追踪1000多个实体。开源项目。· GitHub](https://github.com/Obelus-Labs-LLC/WeThePeople?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-740-april-9-2026)

**原文标题**: [GitHub - Obelus-Labs-LLC/WeThePeople: Civic transparency platform tracking corporate influence on Congress across 8 sectors. 30+ government APIs, 1000+ tracked entities. Open source. · GitHub](https://github.com/Obelus-Labs-LLC/WeThePeople?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-740-april-9-2026)

WeThePeople 是一个开源公民透明度平台，追踪企业如何游说国会、赢得政府合同、面临执法行动、与立法者同步交易股票以及向政客捐款。它整合了40多个政府API，覆盖政治、金融、健康、科技、能源、交通、国防、化工和农业等9大领域及全美50个州，追踪537名政客和1000多家公司，每个数据点均链接回权威公共来源。

- 🏛️ **平台核心**：实时追踪游说与影响力，涵盖国会交易、资金流动、执法行动、游说备案和政府合同，覆盖9大领域的1000多个实体。
- 🔍 **研究工具**：提供15种深度研究工具，包括专利探索器、药物查询、临床试验、内幕交易、FDA召回搜索、有毒物质排放清单、外国游说追踪等。
- 📰 **数据新闻**：通过20种检测模式生成AI驱动的数据调查，涵盖《股票法》违规、委员会股票冲突、执法豁免等主题，并设有验证流程。
- 📱 **移动应用**：正在开发中，通过Expo支持iOS和Android，涵盖所有9大领域、国会交易、邮政编码查询、故事、异常检测等功能。
- 🌐 **关键功能**：包括交互式影响力网络图、国会交易追踪器、支出地图、资金流向桑基图、声明验证管道、AI聊天代理和异常检测等。
- 🏗️ **系统架构**：后端采用FastAPI + SQLite，前端使用React 19 + Vite + TypeScript，移动端基于Expo SDK 54 + React Native，基础设施部署在Hetzner Cloud和Vercel。
- 📊 **数据来源**：全部来自40多个官方政府API和开源数据集，如Congress.gov、SEC EDGAR、House Clerk Disclosures等，确保数据公开透明。
- 🚀 **快速入门**：提供详细的后端、前端和移动端启动指南，支持通过API端点进行数据查询和交互。
- 🤝 **贡献与支持**：欢迎贡献，特别是在新数据源集成、州级数据丰富化和测试方面；项目为开源，鼓励赞助、加星标和分享以支持发展。
- ⚖️ **许可证**：采用GNU Affero通用公共许可证v3.0，确保修改后的网络服务版本开源，但部分专有组件（如检测引擎）在私有仓库中维护。

---

### [GitHub - cuneytozseker/TinyProgrammer: 桌面上的微型程序员，竭尽全力。 · GitHub](https://github.com/cuneytozseker/TinyProgrammer?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-740-april-9-2026)

**原文标题**: [GitHub - cuneytozseker/TinyProgrammer: Tiny programmer sitting on your desk and trying its best. · GitHub](https://github.com/cuneytozseker/TinyProgrammer?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-740-april-9-2026)

TinyProgrammer 是一个基于树莓派和大型语言模型的自包含设备，能够自主编写、运行并观察小型 Python 程序。它模拟人类打字速度编写代码，具备错误修正功能，拥有情绪系统，并配备复古 Mac IDE 风格的显示界面。设备在休息时会访问共享公告板 TinyBBS，下班后则启动星空屏幕保护程序。

- 🖥️ **设备概述** – 基于树莓派的自编程设备，通过 LLM 自动生成并运行 Python 程序，具备情绪与交互功能。
- 🔄 **工作循环** – 遵循“思考→编写→审查→运行→观察→归档→反思”的无限循环，偶尔进行 BBS 社交休息。
- 🎮 **显示与界面** – 采用复古 Mac IDE 风格界面，支持多种显示屏配置，并内置星空屏幕保护程序。
- ⚙️ **硬件要求** – 兼容树莓派（如 Pi 4B 或 Pi Zero 2 W）及 HDMI/SPI 显示屏，需网络连接和 OpenRouter API 密钥。
- 📦 **安装方式** – 提供一键脚本快速安装，也支持手动分步安装或通过 Docker 在桌面环境无头运行。
- 🌐 **功能特性** – 包含情绪系统、BBS 社交互动、学习日志记录、Web 控制面板，以及可配置的程序类型与模型选择。
- 💰 **运行成本** – 默认设置下每日 API 成本约 0.15 美元，可通过调整运行时长与模型选择进一步降低。
- 📄 **开源许可** – 硬件设计采用 CERN-OHL-S 许可，软件部分使用 GPL-3.0 许可，支持克隆与二次开发。

---

### [GitHub - adamchainz/profiling-explorer: 基于表格的Python性能分析数据（pstats文件）探索工具。](https://github.com/adamchainz/profiling-explorer?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-740-april-9-2026)

**原文标题**: [GitHub - adamchainz/profiling-explorer: Table-based exploration tool for Python profiling data (pstats files). · GitHub](https://github.com/adamchainz/profiling-explorer?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-740-april-9-2026)

profiling-explorer 是一个用于探索 Python 性能分析数据（pstats 文件）的基于表格的交互式工具，支持通过本地网页界面查看和排序分析结果。

- 🐍 **支持 Python 3.10 至 3.14**，兼容 `cProfile` 和 Python 3.15+ 的 `profiling.sampling` 生成的分析文件
- 📦 **通过 pip 安装**：使用 `python -m pip install profiling-explorer` 即可安装
- 📊 **生成分析文件**：例如通过 `python -m cProfile -o example.pstats example.py` 命令生成
- 🌐 **启动网页界面**：运行 `profiling-explorer example.pstats` 在浏览器中打开交互式报告
- 🔍 **交互功能丰富**：支持按调用次数、内部时间、累计时间排序，可通过搜索框过滤文件名或函数名
- 🔗 **快速导航**：可查看函数的调用者与被调用者，并复制代码位置信息
- ⚙️ **可选参数**：支持自定义端口（`--port`）和开发模式（`--dev`）运行
- 📄 **开源项目**：采用 MIT 许可证，代码托管在 GitHub，包含测试和文档

---

### [GitHub - edumucelli/docking: 一款轻量级、功能丰富的Linux停靠栏，使用Python配合GTK 3和Cairo编写 · GitHub](https://github.com/edumucelli/docking?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-740-april-9-2026)

**原文标题**: [GitHub - edumucelli/docking: A lightweight, feature-rich dock for Linux written in Python with GTK 3 and Cairo · GitHub](https://github.com/edumucelli/docking?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-740-april-9-2026)

Docking 是一个使用 Python、GTK 3 和 Cairo 编写的轻量级、功能丰富的 Linux 程序坞，灵感来源于 Plank 和 Cairo-Dock，并具有可扩展的小程序系统。

- 🚀 **快速启动器**：支持运行状态指示器和窗口预览交互。
- 🎨 **高度可定制**：提供多种主题、透明度、图标大小、菜单选项和工具提示控制。
- 📍 **灵活布局**：支持多位置、多显示器、自动隐藏和拖放组织。
- 📁 **原生文件支持**：可固定文件和文件夹，支持左键点击文件夹堆栈。
- 🔌 **可扩展小程序**：内置 38 个小程序，涵盖系统状态、生产力、媒体和工具。
- 🖥️ **桌面环境集成**：兼容 MATE、Xfce、KDE、Cinnamon、GNOME 等。
- 🌐 **多语言支持**：包含 74 种语言环境，并支持英语回退。
- 📦 **多种安装方式**：提供 AppImage、Debian .deb、RPM、Flatpak、Snap、Arch 和 Nix 包。
- ⚙️ **丰富配置**：可通过 JSON 配置文件或右键菜单调整图标大小、缩放、位置、隐藏模式等。
- 🔧 **开发者友好**：支持自定义主题和小程序开发，提供完整的测试和构建工具链。

---

### [GitHub - WeianMao/triattention: TriAttention — 基于三角KV缓存压缩的高效长序列推理。支持在内存受限的GPU上本地部署OpenClaw。](https://github.com/WeianMao/triattention?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-740-april-9-2026)

**原文标题**: [GitHub - WeianMao/triattention: TriAttention — Efficient long reasoning with trigonometric KV cache compression. Enables OpenClaw local deployment on memory-constrained GPUs. · GitHub](https://github.com/WeianMao/triattention?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-740-april-9-2026)

TriAttention 是一个通过三角频率域压缩技术，显著减少 KV 缓存内存占用并提升长文本推理吞吐量的项目，支持多种模型和部署方式。

- 🚀 **核心优势**：在 AIME25 长推理任务上，实现 2.5 倍吞吐量提升和 10.7 倍 KV 内存压缩，且精度无损。
- 🔧 **工作原理**：利用预 RoPE 的 Q/K 向量围绕固定中心分布的特性，通过三角级数进行距离偏好建模，无需代表性查询选择即可实现精准的 KV 缓存压缩。
- 💻 **快速部署**：提供 vLLM 集成，支持 OpenAI 兼容的 API，可轻松与 OpenClaw 等工具结合，在本地受限 GPU（如 24GB RTX 4090）上部署。
- 📊 **性能结果**：在 Qwen3-8B 等模型上，于 AIME24、AIME25 和 MATH-500 等基准测试中均展现出接近全注意力的准确率，同时大幅提升推理速度。
- 🛠️ **灵活配置**：支持通过环境变量调整 KV 缓存预算、压缩触发间隔、保护策略等，并提供了预计算的频率统计文件，便于快速使用。
- 🌐 **生态扩展**：拥有社区实现的 ggml（支持 AMD GPU）、MLX（支持 Apple Silicon）等端口，并计划集成 SGLang、Ollama 等更多平台。
- 📚 **开源资源**：项目在 Apache-2.0 许可证下开源，包含完整的安装指南、复现命令、校准教程和详细的结果分析文档。

---

### [GitHub - yassi/dj-signals-panel：显示已注册的Django信号与接收器，揭示触发内容及位置。· GitHub](https://github.com/yassi/dj-signals-panel?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-740-april-9-2026)

**原文标题**: [GitHub - yassi/dj-signals-panel: Display registered Django signals and receivers, showing what fires and where. · GitHub](https://github.com/yassi/dj-signals-panel?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-740-april-9-2026)

这是一个用于Django的第三方面板工具，可在Django管理后台中直观展示项目中所有已注册的信号及其接收器，帮助开发者监控和调试信号系统。

- 🔍 **信号发现** - 自动发现项目及已安装应用中的所有Django信号
- 📋 **接收器检查** - 列出每个信号的所有连接接收器，包括函数名、模块、文件位置等信息
- 👁️ **源码查看** - 可在管理后台内联查看语法高亮的接收器源代码（需配置开启）
- 🔎 **搜索过滤** - 支持按名称、模块或应用搜索信号，并提供应用筛选下拉菜单
- 📊 **统计摘要** - 显示信号总数、接收器总数及无接收器信号数量概览
- 🌓 **深色模式** - 支持Django管理后台的深色/浅色模式切换
- 🚀 **无需迁移** - 纯只读功能，无需数据库变更
- 📦 **轻松集成** - 通过pip安装并添加至INSTALLED_APPS即可使用
- 🎛️ **控制室兼容** - 可无缝集成到Django Control Room统一仪表板中
- ⚙️ **灵活配置** - 支持通过DJ_SIGNALS_PANEL_SETTINGS自定义显示选项

---

### [Visual Studio Code 中的 Python - 2026年3月发布 - Microsoft Python 开发者博客](https://devblogs.microsoft.com/python/python-in-visual-studio-code-march-2026-release/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-740-april-9-2026)

**原文标题**: [Python in Visual Studio Code - March 2026 Release - Microsoft for Python Developers Blog](https://devblogs.microsoft.com/python/python-in-visual-studio-code-march-2026-release/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-740-april-9-2026)

Visual Studio Code 的 Python 扩展于 2026 年 3 月发布更新，引入了两项主要新功能：支持在已安装的包中搜索符号，以及一项实验性的、基于 Rust 的并行索引器以提升性能。此外，Python 环境扩展也进行了一些错误修复和集成改进。

- 🔍 **搜索已安装包中的符号**：Pylance 现在可以在工作区符号搜索中，包含当前虚拟环境中已安装包内的函数和类定义，便于快速探索第三方库。
- ⚙️ **按需启用与深度控制**：此功能默认关闭，需在设置中手动启用。用户还可通过设置控制对每个包的索引深度，以平衡功能与性能。
- 🚀 **实验性并行索引器**：新增基于 Rust 的并行索引器（实验性功能），据称在大型项目上平均快 10 倍，能提供更快的代码补全和更灵敏的 IntelliSense 体验。
- 🐛 **环境扩展的修复与集成**：修复了环境选择优先级和通知弹窗等问题，并在检测到 Pixi 环境时推荐社区扩展，优化了环境管理器的优先级顺序。
- 📢 **鼓励用户反馈**：团队邀请用户尝试新功能，并通过 GitHub 提交使用体验和问题报告，以帮助改进和稳定实验性功能。

---

### [Django安全版本发布：6.0.4、5.2.13与4.2.30 | 博客 | Django](https://www.djangoproject.com/weblog/2026/apr/07/security-releases/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-740-april-9-2026)

**原文标题**: [Django security releases issued: 6.0.4, 5.2.13, and 4.2.30 | Weblog | Django](https://www.djangoproject.com/weblog/2026/apr/07/security-releases/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-740-april-9-2026)

Django团队发布了安全更新版本6.0.4、5.2.13和4.2.30，修复了多个安全漏洞，并提醒用户尽快升级。Django 4.2版本已结束扩展支持，建议用户升级至5.2或更高版本。

- 🔒 **CVE-2026-3902**：ASGI请求中通过下划线/连字符混淆进行头部欺骗，严重性为“低”。
- 🛡️ **CVE-2026-4277**：GenericInlineModelAdmin中权限滥用问题，严重性为“低”。
- ⚠️ **CVE-2026-4292**：ModelAdmin.list_editable中权限滥用问题，严重性为“低”。
- 🚨 **CVE-2026-33033**：MultiPartParser中通过base64编码文件上传可能导致的拒绝服务漏洞，严重性为“中等”。
- 📈 **CVE-2026-33034**：ASGI请求中通过内存上传限制绕过可能导致的拒绝服务漏洞，严重性为“低”。
- 🔄 **受影响版本**：Django主分支、6.0、5.2和4.2版本均已应用修复补丁。
- 📥 **发布版本**：用户可下载Django 6.0.4、5.2.13和4.2.30进行升级。
- 📧 **安全报告**：安全问题请通过security@djangoproject.com私下报告。

---

### [使用Python构建您的首个智能代理，2026年4月16日周四下午6点 | 线下交流会](https://www.meetup.com/pydatachi/events/314105999/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-740-april-9-2026)

**原文标题**: [Build Your First Agent With Python, Thu, Apr 16, 2026, 6:00 PM   | Meetup](https://www.meetup.com/pydatachi/events/314105999/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-740-april-9-2026)

本次PyData芝加哥举办的混合式活动，是一场面向初学者的Python智能体构建实践工作坊，参与者将无需AI经验或本地安装，在云端创建具备文档问答、实时搜索等功能的AI聊天机器人。

- 🐍 工作坊主题为“用Python构建你的第一个智能体”，由Gus Cavanaugh主讲，聚焦使用Python、Streamlit、Claude AI和RAG技术开发生产就绪的AI聊天机器人
- 🕒 活动时间为4月16日周四晚6点至8点（CDT），采取线上线下混合形式，线上通过Zoom参与，线下地点在芝加哥LaSalle街200号1100室
- 🎯 参与者将完成具备文档上传问答、向量检索、网络搜索集成、Streamlit网页界面及云端部署的完整项目，获得可直接用于作品集的代码
- 🍕 赞助商AlphaSense提供场地、披萨和饮料，线下参与者需在4月15日前登记姓名并携带身份证件入场
- 🌐 AlphaSense作为市场情报平台，通过AI技术为全球6000多家企业客户提供决策支持，2024年收购Tegus后进一步扩展了服务能力

---

### [智能体AI，2026年4月16日，周四，下午5:30 | 聚会](https://www.meetup.com/pydataireland/events/313742990/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-740-april-9-2026)

**原文标题**: [Agentic AI, Thu, Apr 16, 2026, 5:30 PM   | Meetup](https://www.meetup.com/pydataireland/events/313742990/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-740-april-9-2026)

本次PyData爱尔兰聚会聚焦于代理式人工智能，由QuantumBlack（麦肯锡旗下AI公司）联合举办，包含两场主题演讲和社交环节。

- 🗓️ **活动信息**：聚会于4月16日17:30-20:30在都柏林Ranelagh举行，由Sukanya M.主持，NumFOCUS赞助
- 🛠️ **演讲一**：Jitendra Gundaniya分享《使用Kedro Builder构建代理式GenAI流水线》，演示如何通过可视化工具降低开发门槛
- 🤖 **演讲要点**：介绍llm_context_node应用、可视化构建GenAI流水线的方法，以及代码与可视化工具的分工场景
- 🔗 **演讲二**：Dmitry Sorokin探讨《让AI代理管理ML与数据流水线》，讲解通过MCP服务器将传统工作流与AI代理结合的技术方案
- 🌉 **技术融合**：展示如何让AI代理（如LangGraph、Claude Code）程序化调度确定性生产流水线，实现灵活性与稳定性的结合
- 🧠 **核心主题**：活动涵盖人工智能、机器学习、数据科学等开源技术，强调可复现计算在科技领域的应用价值

---

### [PyDataMCR 四月聚会，2026年4月16日星期四，下午6:00 | 见面会](https://www.meetup.com/pydata-manchester/events/314124036/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-740-april-9-2026)

**原文标题**: [PyDataMCR April , Thu, Apr 16, 2026, 6:00 PM   | Meetup](https://www.meetup.com/pydata-manchester/events/314124036/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-740-april-9-2026)

PyData曼彻斯特四月活动将于4月16日18:00至20:30在AutoTrader Circle Square举行，由Shaun H.和Anja S.主持，包含两场专业演讲，并设有社交环节。

- 🗓️ **活动详情**：4月16日18:00-20:30在曼彻斯特AutoTrader Circle Square举行，限50人，提供餐饮
- 👥 **主持与赞助**：由Shaun H.和Anja S.主持，获NumFOCUS、AutoTrader、Kraken和Horsefly Analytics赞助支持
- 🎤 **演讲主题1**：Shannen Riley分享数据治理与质量的重要性，强调从洞察到问责的实践
- 🤖 **演讲主题2**：Faith Sodipe探讨利用AI/ML构建自愈部署管道，提升系统可靠性与团队效率
- 🤝 **社交与准则**：活动后设有社交环节，需遵守NumFOCUS专业行为准则，场地具备无障碍设施

---

### [AI网络应用防火墙，2026年4月16日周四，下午6:00 | 聚会](https://www.meetup.com/python-stlouis/events/314009468/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-740-april-9-2026)

**原文标题**: [AI Web Application Firewall, Thu, Apr 16, 2026, 6:00 PM   | Meetup](https://www.meetup.com/python-stlouis/events/314009468/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-740-april-9-2026)

本次讲座介绍AIWAF（AI Web应用防火墙），这是一种为Django、Flask和FastAPI等框架设计的中间件安全系统，可直接集成到应用层进行实时行为分析与防护。

- 🛡️ AIWAF是一种中间件级安全系统，专为Django、Flask和FastAPI等框架设计，可直接集成到应用层
- 🔍 通过实时分析请求行为检测异常和恶意模式，而非依赖静态规则
- 🧠 结合特征提取、自适应学习和异常检测技术，智能决策是否允许或阻止流量
- ⚡ 包含基于Rust的高性能请求验证加速器
- 🗓️ 活动于4月16日18:00-20:00在圣路易斯TechArtista CWE举行，包含交流、主题演讲和告别环节
- 🤝 由PySTL组织，Manning Publications赞助，并与Python软件基金会等社区伙伴合作
- 🐍 相关主题涵盖人工智能、Python开发及软件工程等领域

---

### [PyData 诺里奇 - 四月聚会，2026年4月15日星期三，下午5:45 | Meetup](https://www.meetup.com/pydata-norwich/events/313947490/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-740-april-9-2026)

**原文标题**: [PyData Norwich - April Meetup, Wed, Apr 15, 2026, 5:45 PM   | Meetup](https://www.meetup.com/pydata-norwich/events/313947490/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-740-april-9-2026)

PyData Norwich四月聚会将于4月15日举行，由Chris J.主持，地点在诺里奇的Artlist。活动聚焦数据创业想法分享与讨论，适合对数据产品开发感兴趣的人士参与，提供免费餐饮和会后社交环节。

- 🗓️ 活动于4月15日17:45-19:45在诺里奇Artlist举行，遵循NumFOCUS行为准则  
- 🐉 主讲人Yogi将分享数据创业提案，征集技术反馈与商业见解  
- 🧠 形式为开放式讨论，欢迎各经验层次的Python/数据从业者参与交流  
- 🍕 现场提供免费披萨饮料，会后可前往Coach and Horses酒吧继续交流  
- 📍 地点需按4号门铃进入，演讲18:00开始，19:00起为酒吧社交时间

---

