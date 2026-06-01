### [面向开发者的 AI 工程 | 博客 | Luca Cavallin](https://www.lucavall.in/blog/ai-engineering-for-developers)

**原文标题**: [AI Engineering for Developers | Blog | Luca Cavallin](https://www.lucavall.in/blog/ai-engineering-for-developers)

## 概述总结
本文为有经验的软件工程师提供了 AI 工程实践的全面指南，涵盖从基础概念到生产部署的完整技术栈，强调系统思维而非单纯依赖模型。

- 🧠 **核心转变**：AI 工程的核心是围绕模型构建系统，而非模型本身。输出具有概率性，需构建容错、评估和监控体系。
- 🏗️ **技术栈三层**：应用层（提示词/RAG/智能体）→ 模型开发层（微调/蒸馏）→ 基础设施层（GPU/向量数据库）。大多数团队应聚焦应用层。
- 🛠️ **优化三步骤**：默认顺序为提示词工程 → RAG → 微调。不要跳过步骤，多数问题可通过前两者解决。
- 📊 **评估体系**：构建包含程序化指标、LLM 裁判、人工审查和 A/B 测试的多层次评估管道。评估数据集的构建比评估工具更重要。
- 🔄 **RAG 架构**：混合搜索（BM25+ 稠密检索）+ 重排序是最佳实践。注意分块策略、元数据过滤和查询转换等高级技术。
- 🤖 **智能体模式**：优先使用确定性工作流，仅在需要运行时决策时使用智能体。注意循环限制、确认门和工具幂等性。
- 🔒 **安全防御**：采用多层防护（输入/输出/智能体级别），无纯提示词可防御提示注入，需架构性防御。
- ☁️ **GCP 部署**：推荐顺序为 Agent Engine → Cloud Run → GKE。Vertex AI 平台提供模型花园、智能体运行时和记忆银行等托管服务。
- 💰 **成本控制**：建立成本模型、请求标签、智能路由和缓存机制。模型路由（廉价模型处理简单请求）是最大成本杠杆。
- 📈 **持续维护**：模型漂移、提示词腐化和数据变化需要持续监控。将评估管道集成到 CI/CD 中，每次变更都需验证。

---

### [面向开发者的电子签名 API – BoldSign 提供快速安全的解决方案](https://boldsign.com/esignature-api/?utm_campaign=boldsign_june2026&utm_medium=newsletter_ad&utm_source=programming_digest)

**原文标题**: [eSignature API for Developers – Fast & Secure by BoldSign](https://boldsign.com/esignature-api/?utm_campaign=boldsign_june2026&utm_medium=newsletter_ad&utm_source=programming_digest)

该 API 专为开发者打造，提供强大的电子签名集成能力，支持多语言 SDK、高安全合规和灵活定价。

- 🔧 **开发者友好**：提供 cURL、C#、Java、PHP、Python、Node.js 等多种语言的 SDK 和代码示例，简化集成流程
- 🏆 **行业认可**：获 Postman 2025 开发者选择奖，被全球 5 万 + 企业信赖
- ⚡ **快速部署**：仅需几行代码即可嵌入电子签名工作流，几分钟内开始发送合同
- 🛡️ **安全合规**：符合 SOC 2、GDPR、HIPAA、PCI DSS 标准，采用 AES-256 加密，签名具法律效力
- 🎨 **自定义体验**：支持品牌定制、嵌入签名、身份验证、实时文档更新等高级功能
- 📊 **开发者仪表盘**：提供实时洞察、详细报告和沙箱环境，便于测试与监控
- 💰 **透明定价**：企业版每月$30 起，每封文档$0.75，按用量付费
- 🌐 **全球覆盖**：24 年行业经验，服务 120+ 国家，99.999% 正常运行时间保障
- 📚 **丰富资源**：提供交互式演示、Postman 集合、API 参考文档和 SDK，加速集成
- ❓ **常见问题**：支持免费沙箱测试、批量发送（通过模板 + 循环调用）、代发签名请求等功能

---

### [Lambda 网络背后的隐形工程 | 分布式一切](https://www.allthingsdistributed.com/2026/04/the-invisible-engineering-behind-lambdas-network.html)

**原文标题**: [The invisible engineering behind Lambdaâs network | All Things Distributed](https://www.allthingsdistributed.com/2026/04/the-invisible-engineering-behind-lambdas-network.html)

### 概述总结
AWS Lambda 网络团队通过近十年的隐形工程优化，大幅提升了 VPC 冷启动性能、网络密度和效率，实现了从 200 到 4000 个快照网络每工作节点的扩展，并将 CPU 使用率降低 1%。

- 🔧 **网络拓扑优化**：通过 eBPF 替代 Geneve 隧道创建，将延迟从 150 毫秒降至 200 微秒，消除了 VPC 冷启动瓶颈。
- 🚀 **SnapStart 支持**：重新设计网络拓扑，从按需创建转为工作节点初始化时预创建 4000 个网络，消除了运行时的 CPU 消耗。
- ⚡ **NAT 性能提升**：用 eBPF 无状态包处理替代 iptables 有状态 NAT，将 NAT 设置延迟降低 100 倍。
- 📉 **iptables 规则简化**：将根命名空间从 125,000+ 条规则减少至 144 条静态规则，消除了不同网络槽位间的性能差异。
- 🔒 **RTNL 锁优化**：通过重新排序操作（先池化命名空间、批量附加 eBPF 程序），解决了内核锁竞争导致的网络创建延迟。
- 🔄 **统一拓扑架构**：合并传统和快照网络拓扑，支持所有工作负载，容量提升 20 倍。
- 🛠️ **跨团队复用**：将网络堆栈封装为服务，供 Aurora DSQL 等团队直接使用，节省数月工程时间。
- ⏳ **持续改进**：团队以“隐形工程”为荣，持续优化底层系统，使 Lambda 函数启动更快、运行更高效。

---

### [Stripe 的选择性测试执行：面向 5000 万行 Ruby 单体仓库的快速 CI | Stripe Dot Dev 博客](https://stripe.dev/blog/selective-test-execution-at-stripe-fast-ci-for-a-50m-line-ruby-monorepo)

**原文标题**: [Selective Test Execution at Stripe: Fast CI for a 50M-line Ruby monorepo | Stripe Dot Dev Blog](https://stripe.dev/blog/selective-test-execution-at-stripe-fast-ci-for-a-50m-line-ruby-monorepo)

Stripe 在拥有 5000 万行 Ruby 单体仓库中实现了选择性测试执行，大幅提升 CI 速度。

- ⚡ 选择性测试执行：仅运行受代码变更影响的测试，而非全部测试，显著缩短 CI 时间。
- 🏢 应对大型单体仓库：针对 5000 万行 Ruby 代码的复杂项目，解决传统全量测试耗时长的问题。
- 🛠 技术实现：通过分析代码依赖关系，智能识别并只执行相关测试用例。
- 📈 提升开发效率：加快反馈循环，让开发者能更快验证代码变更，提高生产力。
- 🔗 相关实践：与 Stripe 其他优化工具（如 rubyfmt 自动格式化）共同提升工程效率。

---

### [随叫随到教会了我一切——姚越](https://yaoyue.org/blog/2026-oncall/)

**原文标题**: [Being oncall taught me everything - Yao Yue](https://yaoyue.org/blog/2026-oncall/)

### 概述总结
值班经历不仅塑造了技术能力，更教会了工程师如何应对现实中的复杂系统与人际协作。

- 🚨 **值班的核心价值**：通过处理高吞吐量分布式缓存（如 Twitter Cache）的故障，深刻理解了系统在真实环境中的脆弱性与韧性
- ⚡ **技术关键教训**：速度不如可预测性重要；尾部延迟比平均值更关键；简洁架构在危机中价值凸显；运营卓越需设计阶段就考虑可观测性、自动化与默认值
- 🤝 **人际协作启示**：主动承认错误赢得信任；跨团队协作（如内核工程师、上游服务团队）是解决复杂故障的关键；高压环境催生深厚战友情谊
- 🔍 **对软件工程的反思**：不参与部署、监控和调试的工程师无法真正理解软件；生产环境中的失败是理解系统本质的必经之路
- 💡 **个人成长感悟**：值班带来的肾上腺素与责任感让专注力提升，与优秀团队共同解决问题的成就感无可替代

---

### [关于索引你不知道的事](https://jon.chrt.dev/2026/04/15/things-you-didnt-know-about-indexes.html)

**原文标题**: [Things you didn't know about indexes](https://jon.chrt.dev/2026/04/15/things-you-didnt-know-about-indexes.html)

### 概述摘要
本文深入探讨了数据库索引的实用知识，涵盖基础概念、成本、常见陷阱及高级索引类型，强调合理使用索引对性能的关键影响。

- 📚 **索引基础**：数据库索引类似教科书索引，通过排序结构（如 B-tree）实现快速查找，避免全表扫描。
- ⚖️ **索引成本**：索引加速读取但拖慢写入（需同步更新），占用存储和内存，并增加查询规划时间。
- ❌ **常见陷阱**：复合索引需注意列顺序（如`(type_1, type_2)`无法优化`type_2`单独查询）；函数包裹列（如`lower(name)`）会使索引失效；隐式类型转换也有同样问题。
- 🔍 **避免方法**：使用`EXPLAIN`或`EXPLAIN ANALYZE`检查查询计划，确保出现`Index Scan`而非`Seq Scan`。
- 🛠️ **高级索引**：
  - **函数索引**：对表达式（如`lower(name)`）建索引，解决函数查询问题。
  - **部分索引**：仅索引满足条件的行（如`WHERE is_legendary = true`），节省空间和写入成本。
  - **覆盖索引**：通过`INCLUDE`附加列，实现仅索引扫描（`Index Only Scan`），避免回表查询。
- 💡 **实用建议**：不要猜测，通过测量和工具优化索引；部分索引适用于高频查询的特定值场景。

---

### [Google IDE 发展史 | Laurent Le Brun 的博客](https://laurent.le-brun.eu/blog/a-history-of-ides-at-google)

**原文标题**: [A History of IDEs at Google | Laurent Le Brun's blog](https://laurent.le-brun.eu/blog/a-history-of-ides-at-google)

Google 的 IDE 发展历程展示了从碎片化到统一工具的演变，最终通过云端 IDE 和 VSCode 前端整合了大部分开发工作。

- 📜 **碎片化时代**：2011 年，Google 工程师可自由选择 IDE，导致工具碎片化，Jeff Dean 认为统一编辑器会引发不满。
- 🔧 **工具重复投入**：不同 IDE 需重复实现 Bazel、Starlark、代码格式化等集成，虽通过 20% 时间和同行奖励缓解，但效率低下。
- ☁️ **Cider 云端 IDE 诞生**：约 2013 年，基于 Web 的编辑器 Cider 出现，最初用于技术写作，后通过语言服务器协议支持代码补全，并利用后端索引整个代码库。
- 🚀 **转向 VSCode 前端**：2020 年，Cider 团队决定采用 VSCode 作为前端，继承成熟编辑器和扩展生态，减少重复开发。
- 📈 **统一 IDE 成效**：到 2023 年，80% 的 Google 主代码库开发在 Cider V 上完成，统一的平台促进了内部扩展开发（约 100 个）和 AI 功能集成（如代码审查注释解析、智能粘贴）。
- 💡 **标准工具的价值**：统一 IDE 虽成本高昂，但通过集中资源提升了整体生产力，并支持了 AI 等创新功能的快速部署。

---

