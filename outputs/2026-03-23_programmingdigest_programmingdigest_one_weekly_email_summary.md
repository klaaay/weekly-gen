### [保修失效若再生 - 斯科特·沃纳 - 近零](https://nearzero.software/p/warranty-void-if-regenerated)

**原文标题**: [Warranty Void If Regenerated - by Scott Werner - Near Zero](https://nearzero.software/p/warranty-void-if-regenerated)

在软件生成时代，软件机械师汤姆·哈特曼为农民诊断和修复由AI生成的工具问题，揭示了技术变革下专业知识与人性需求的碰撞。

- 🚜 汤姆从农机技师转型为软件机械师，反映了后转型经济中职业的演变，硬件与软件的界限逐渐模糊，领域知识成为核心价值。
- 🥬 客户玛格丽特的收割工具因上游天气模型更新而错误推荐提前收割，导致经济损失，突显了规范未预见外部数据变化的常见问题。
- 🍝 年轻奶农伊桑的多个工具因随意再生而数据格式冲突，造成定价错误，暴露了缺乏系统架构管理的“意大利面式”集成风险。
- 💡 汤姆提出“软件编舞师”解决方案，强调管理工具间关系的价值远高于工具本身，类比集装箱与物流系统的关系。
- 🌱 老年农场主卡罗尔的孙子为其灌溉系统添加了优化工具，但工具无法编码她三十年的土地经验，汤姆通过物理开关让她保持控制权。
- 🔧 汤姆的工作融合了技术诊断与人性理解，如通过咖啡机比喻说明规范优化的困难，并常用物理开关满足客户的心理控制需求。
- 📊 软件维护的悖论在于客户宁愿为故障修复付费，却抗拒更便宜的预防性服务，反映了人类应对紧急情况而非脆弱性的心理倾向。
- 🌾 汤姆的日常案例体现了后转型经济的核心矛盾：AI擅长通用优化，但难以捕捉具体情境中的隐性知识，而机械师在两者间搭建桥梁。

---

### [编码时实时无障碍测试 | 借助AI实现WCAG合规 | BrowserStack](https://www.browserstack.com/accessibility-testing/accessibility-devtools?utm_source=newsletter&utm_medium=PR&utm_platform=&utm_content=product-updates&utm_campaign=PR-A11y-Devtools&utm_term=programming-digest)

**原文标题**: [Real-time accessibility testing while coding | WCAG conformance with AI | BrowserStack](https://www.browserstack.com/accessibility-testing/accessibility-devtools?utm_source=newsletter&utm_medium=PR&utm_platform=&utm_content=product-updates&utm_campaign=PR-A11y-Devtools&utm_term=programming-digest)

BrowserStack Accessibility DevTools 是一款帮助开发者在编码时实时检测和修复网页可访问性问题的工具，通过集成到 IDE 或终端，利用 Spectra™ 规则引擎和 AI 辅助建议，确保代码在提交前符合 WCAG 标准，并支持 CI/CD 集成。

- 🛠️ **实时检测**：在 IDE 或终端中实时扫描代码，即时提示可访问性违规问题
- 🤖 **AI 辅助修复**：提供上下文感知的修复建议，直接在开发流程中指导问题解决
- 🔌 **广泛集成**：支持 VS Code、IntelliJ、WebStorm 等多种主流 IDE 和开发环境
- 🚫 **提交前拦截**：支持扫描目录或文件，防止不符合可访问性标准的代码提交到仓库或 CI/CD 流水线
- 🌐 **渲染代码测试**：通过 BrowserStack MCP 对渲染后的代码进行自动化扫描，检测可访问性问题
- 📊 **平台化测试**：提供可访问性报告、辅助分析和自动化审计，支持定时测试，无需自建测试框架

---

### [获取失败](https://lemire.me/blog/2026/03/18/how-many-branches-can-your-cpu-predict/)

**原文标题**: [Failed to retrieve](https://lemire.me/blog/2026/03/18/how-many-branches-can-your-cpu-predict/)

无法总结：获取内容失败，状态码 202。

---

### [PostgreSQL索引简介 :: 解释与分析](https://dlt.github.io/blog/posts/introduction-to-postgresql-indexes/)

**原文标题**: [Introduction to PostgreSQL Indexes :: explain, analyze
](https://dlt.github.io/blog/posts/introduction-to-postgresql-indexes/)

本文介绍了Postgres索引的基础知识、工作原理、不同类型及其适用场景，帮助开发者理解索引如何提升查询性能，并权衡其带来的存储与维护成本。

- 📚 索引是数据库对象，旨在通过减少磁盘读取来加速数据访问，但仅当查询匹配索引列且返回数据量较小时有效
- 💾 数据以无序的“元组”形式存储在堆文件中，索引通过树结构将键值映射到对应的行位置（ctid）
- ⚡ 索引通过直接定位目标行而非全表扫描来大幅提升查询速度，例如将查询时间从265毫秒降至0.077毫秒
- 🛠️ 使用索引需考虑成本：额外磁盘空间、写操作开销、查询规划器复杂度增加及内存占用
- 🌳 B树是最常用的索引类型，支持快速查找、排序和连接操作，适用于大多数场景
- 🔗 多列索引需注意列顺序，PostgreSQL 18引入的“跳过扫描”优化允许非最左列查询使用复合索引
- 🎯 部分索引通过条件表达式仅索引特定行，适用于数据分布不均或仅需部分数据的场景
- 📊 覆盖索引允许“仅索引扫描”，避免访问堆表，提升只查询索引列时的性能
- 🧮 表达式索引可基于函数或表达式结果创建，适用于常对转换后数据进行查询的场景
- 🔑 哈希索引适用于等值查询且数据唯一性高的场景，比B树更紧凑快速，但不支持排序或多列
- 📦 BRIN索引针对大型有序数据（如时间序列）优化，通过存储数据块范围摘要减少索引大小
- 🔍 GIN索引适用于复合数据（如文本、数组、JSON）的搜索，支持多种数据类型策略
- 🌐 GiST和SP-GiST是索引框架，用于自定义数据类型（如几何、网络地址、全文搜索）的索引实现

---

### [SFQ：简单、无状态、随机公平性 - 马克的博客](https://brooker.co.za/blog/2026/02/25/sfq.html)

**原文标题**: [SFQ: Simple, Stateless, Stochastic Fairness - Marc's Blog](https://brooker.co.za/blog/2026/02/25/sfq.html)

本文介绍了Marc Brooker的个人背景及其对随机公平排队（SFQ）算法的探讨，该算法通过哈希映射和周期性扰动，以固定数量的队列有效隔离分布式系统中的“嘈杂邻居”问题，并提出了结合洗牌分片和最佳选择策略的优化方案。

- 👨💻 Marc Brooker是AWS工程师，专注于数据库、无服务器技术，并拥有广泛的个人兴趣
- 📄 随机公平排队（SFQ）源自Paul E. McKenney的论文，用于在分布式系统中实现随机隔离工作负载
- 🔄 相比传统公平排队（每客户一个队列），SFQ使用固定数量的队列并通过哈希分配客户，降低复杂度
- 🎲 通过周期性扰动哈希函数，避免客户因长期“坏运气”与嘈杂邻居持续冲突，提升服务公平性
- 🧩 结合洗牌分片和最佳选择策略，可进一步优化隔离效果，保持低复杂度同时增强系统稳定性

---

### [空中交通管制：IBM 9020系统](https://computer.rip/2026-01-17-air-traffic-control-9020.html)

**原文标题**: [air traffic control: the IBM 9020](https://computer.rip/2026-01-17-air-traffic-control-9020.html)

本文概述了IBM 9020计算机系统在美国空中交通管制（ATC）发展中的关键作用。该系统起源于20世纪50年代的SAGE防空系统，后经SATIN项目改造用于民用ATC，最终在1960年代末成为国家空域系统（NAS）航路阶段A的核心。IBM 9020采用多系统架构，集成了多个S/360计算机，具备高可靠性和实时处理能力，支持雷达数据处理、飞行计划管理和控制器交互等功能。尽管该系统于1980年代被更现代的HOST系统取代，但其在ATC自动化历程中留下了重要印记。

- 🛫 SAGE系统最初为军用防空设计，后被联邦航空局（FAA）尝试改造用于民用ATC，但项目因预算和技术问题中止。
- 💡 1960年代，FAA推动国家空域系统（NAS）自动化，IBM 9020作为航路阶段A的核心计算机系统，于1967年首次在杰克逊维尔安装。
- 🔧 IBM 9020采用多系统架构，集成多个S/360计算机，通过共享内存和冗余设计实现高可靠性和实时处理能力。
- 🖥️ 系统支持雷达数据处理、飞行计划管理、控制器控制台交互等功能，并与Raytheon显示系统协同工作。
- ⚙️ 控制程序（Control Program）和操作错误分析程序（OEAP）负责任务调度、错误处理和系统配置，确保稳定运行。
- 📡 9020系统与雷达站、控制器工作站、航空公司终端等外部设备通过低速通信线路连接，实现全自动化ATC操作。
- 🔄 1980年代，9020被基于IBM 3083的HOST系统取代，但部分显示子系统持续服务至1990年代，并在英国等地留有历史遗产。

---

### [获取失败](https://cacm.acm.org/research/a-decade-of-docker-containers/)

**原文标题**: [Failed to retrieve](https://cacm.acm.org/research/a-decade-of-docker-containers/)

无法总结：获取内容失败，状态码 403。

---

