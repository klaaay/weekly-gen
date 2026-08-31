### [](https://cursor.com/blog/git-at-any-scale)

**原文标题**: [Git at any scale · Cursor](https://cursor.com/blog/git-at-any-scale)

Git 在大规模托管时的核心挑战源于其分布式设计：packfile 既是存储格式也是网络传输格式，导致水平扩展和一致性保障极其困难。文章回顾 GitHub 的 Spokes 架构及其 3PC 共识局限，并介绍 Cursor 基于 S3 写前日志（WAL）构建的 Continuity 系统，它实现了线性一致性、无限副本扩展和低成本运维，最终落成为 Origin 平台。

- 📦 Git 的 packfile 基础设计让服务端存储与传输都受制于二进制大文件，难以直接扩展。
- 🧠 由于 Git 对象图（DAG）需要逐步随机访问，基于键值存储的对象级分布方案在实践中不可行。
- 🗄️ GitHub 早期尝试分布式文件系统（NFS、DRBD 等）失败，因为 packfile 的随机读取模式在网络文件系统上性能极差。
- 🔁 Spokes 采用应用层复制：每个仓库存多份于 NVMe，用 3PC 共识同步推送，保证强一致性。
- ⚖️ Spokes 的 3PC 受最慢副本拖累，副本越多推送吞吐越差，且大规模小仓库场景下资源浪费严重。
- 🐾 Spokes 运维繁重：仓库“像宠物而非牲畜”，需要路由表、持续校验和快速修复，否则可用性受损。
- 💡 Continuity 的核心是 S3 上的写前日志（WAL）：推送先持久化再确认，所有推送线性化。
- 🗳️ 通过 S3 原子 CAS 操作同步 WAL，无需选举主节点；任意服务器都可安全接收推送。
- 📡 副本通过 UDP gossip 和 ETag 条件 GET 快速对齐，读取始终与 S3 真相一致。
- 🏷️ 本地仓库只是“热缓存”，可随时从 WAL 重新物化，空闲副本也会被自动回收。
- 🗜️ 压缩（repack）只由主节点执行，副本直接从 S3 下载压缩结果，用带宽换 CPU。
- 🚀 扩展性测试：S3 Standard 可支撑约 120 pushes/s，S3 Express One Zone 超过 300 pushes/s，读取随副本数线性扩展。
- 🔍 WAL 作为唯一真相源，提供完整推送历史与审计能力，发生 Git 故障时可精确定位并回滚。
- 🏢 与 Azure DevOps 的关系型数据库方案相比，Continuity 避免外部数据库运维，更强调数据一致性。
- ⭐ Origin 是 Cursor 基于上述经验推出的 Git 托管平台，目标是平稳迁移到更可靠、更高效、可无限扩展的基础设施。

---

### [](https://momentic.ai/mo?utm_medium=influencer&utm_campaign=plug-pilot&utm_source=newsletter&utm_content=ad&utm_term=programmingdigest)

**原文标题**: [Mo the AI QA, by Momentic | Get Onboarded](https://momentic.ai/mo?utm_medium=influencer&utm_campaign=plug-pilot&utm_source=newsletter&utm_content=ad&utm_term=programmingdigest)

overview summary  
Mo 是一款面向工程团队的 AI QA 工具，可针对 Web、iOS 和 Android 应用自动执行 bug 搜索。用户只需提供目标与访问入口，Mo 就能并行探索真实用户流程，生成带录屏、复现步骤和推理的 bug 报告，并支持与 coding agent 集成，大幅减少手动测试负担。

- 🤖 Mo 是 AI QA 工具，能对 Web、iOS、Android 应用进行自动 bug bash，无需编写或维护测试脚本
- 🎯 使用方式简单：给 Mo 一个 URL 或应用构建，并描述关注点，它会自动探索并找出值得修复的问题
- 📹 每个 bug 都会附带录屏、复现步骤和 Mo 的推理过程，便于开发和修复
- ⚡ 可在单次 bug bash 中运行数十个代理（最高记录 116 个同时探索），覆盖多个浏览器或移动模拟器
- 🔄 支持多种场景：bug bash、dogfood 会话、探索性测试、回归检查、设备/浏览器矩阵测试
- 🧪 发现的 bug 会先由独立的 reproducer 代理在干净环境中验证，减少误报，未复现的问题不会进入报告
- 🧠 Mo 会学习产品的术语、规则和已知流程，当用户标记“按预期工作”时，会生成知识条目，避免重复报告同样行为
- 🔗 与 coding agent 无缝协作：agent 通过 MCP 服务器读取 bug 报告并直接修复，无需二次描述问题
- 📦 可将已覆盖的流程转化为 Momentic 测试：用 YAML 文件编写纯英文步骤，由 CLI 在 CI 中运行，守护每次 merge
- 💼 特别适合编码 agent 合并代码速度快、但缺少专职 QA 团队的工程组织
- 📊 实测案例：某 Fortune 1000 公司在 staging 上运行一次 bug bash，一个下午发现 27 个 bug，相当于节省 2 天手动 QA 工作量
- 🌐 支持 hosted browsers、iOS simulators、Android emulators，并可为多目标同时启动多个会话
- 💬 定价仍在设计阶段，将在正式接入前与首批团队沟通确认

---

### [](https://maurycyz.com/projects/bad_jpeg/)

**原文标题**: [Regressive JPEGs: (Maurycy's blog) ](https://maurycyz.com/projects/bad_jpeg/)

JPEG 渐进式编码通过多个扫描（scan）分阶段传输图像数据，可先显示低分辨率预览再逐步细化。本文还探讨了利用扫描拼接实现“单图动画”的技巧及其限制。

- 📷 渐进式 JPEG 可将数据分为多个扫描，先保存低频 DCT 分量，下载时先显示模糊预览而非截断图像。
- 🧩 每个扫描带独立头部，包含长度、颜色通道、Huffman 表索引、DCT 频率范围及精度等信息。
- 🎨 图像使用 YCbCr 色彩空间：亮度（Y）单独保存，色度（Cb/Cr）可降低分辨率或精度而不易察觉。
- 📊 典型渐进文件包含 10 个扫描：先 DC 系数粗预览，再逐级补充 AC 系数，最后补全高精度数据。
- ⚖️ 色度数据以半分辨率存储，因此完整色度信息仅占亮度一半，可优先传输。
- 🔁 通过拼接多个同尺寸 JPEG（滤除 SOI/SOF/EOI 标记），可在慢网络中展示多帧切换效果。
- 🚫 多数解码器限制扫描数量（如 Chrome 约 90 次），防止“zip 炸弹”式滥用，故难以做长动画。
- 🛠 解决方法是仅使用 DC-only 扫描：每个帧只含一个 DC 扫描（0-0 频段，全精度），即可被广泛支持。
- 📁 用 `jpegtran -scans frame.scans out.jpg in.jpg` 可生成合法的纯 DC 渐进图，无特殊要求。
- 🎭 由此可实现将视频“打包”进单张 JPEG、无 CSS/JS 的交互页面，或利用部分渲染做趣味玩法。
- 💡 这种技术无实际用途，因为无法包含时间信息，播放速度完全依赖网络延迟，但仍有极大恶搞潜力。

---

### [](https://blog.cloudflare.com/dns-cache-memory-optimization-1111/)

**原文标题**: [How we saved 100 terabytes of memory by optimizing 1.1.1.1âs DNS cache | Cloudflare Blog](https://blog.cloudflare.com/dns-cache-memory-optimization-1111/)

overview summary
- 🧠 文章介绍Cloudflare通过五项内存优化技术，将其DNS缓存平台Big Pineapple的每条缓存条目内存占用降低56%，节省约100 TB内存，同时提升性能。
- 💾 使用`Box<[T]>`和`Box<str>`替代`Vec<T>`和`String`，去掉容量字段并消除多余堆空间，每条节省64字节，总计超15 TB。
- 📋 将answer、authority、additional三个独立列表合并为单一列表加偏移量，用u16偏移替代指针和长度，每条节省28字节。
- 👤 对大多数与查询域名相同的记录所有者不再存储，改为读取时从缓存键推断，避免堆分配；仅当所有者不同时才存储完整名称。
- 📦 优化Rust枚举大小：将TXT、NAPTR、SVCB等大型RecordData变体装箱到堆上，使A/AAAA等常见记录从144字节降至24字节，每条A记录节省120字节。
- 🔗 进一步将记录数据以原始字节形式存储为带长度前缀的缓冲区，消除枚举开销和独立堆分配，提升缓存局部性，并减少序列化工作。
- ⚡ 性能显著提升：缓存插入吞吐量提高43%，查找延迟降低19%；生产环境中p99内存从9.3 GB降至5.3 GB（降43%），p90从6.5 GB降至3.8 GB。
- 📊 基准测试显示，每条条目从953字节降至420字节，分配从1.1 KB降至461字节；释放的内存计划用于增加缓存容量，提升命中率并减少上游查询。

---

### [](https://bernsteinbear.com/blog/zkp/)

**原文标题**: [A quick look at zero-knowledge proofs | Max Bernstein](https://bernsteinbear.com/blog/zkp/)

overview summary
本文以3-着色图为例，深入浅出地介绍了零知识证明（ZKP）的核心概念、交互式协议、Python实现步骤、重复轮次的概率分析，以及如何扩展到数独等NP完全问题；作者强调该内容与加密货币无关，并提供了网络演示和开放源码。

- 🧩 零知识证明允许证明者在不泄露实际解的情况下，向验证者证明自己拥有某个NP完全问题的有效解。
- 🎨 经典示例是3-着色图：证明者知道合法的3色分配，但不愿透露具体颜色，只需让验证者相信该分配存在。
- 📜 协议源自Goldreich、Micali和Widgerson的论文，核心是每轮随机置换颜色，并用带nonce的哈希“锁箱”提交所有颜色。
- 🔑 验证者随机选择一条边，要求打开两端节点的锁箱，检查哈希匹配、颜色合法且两端颜色不同；若不符合则拒绝。
- 🔁 协议需重复m²轮（m为边数），使欺骗概率上限为(1-1/m)^(m²)；例如1000条边时，4600轮后欺骗率约1%，10000轮后约0.0045%。
- 💻 实现中需注意：不能直接用hash(color)，必须加入nonce避免相同颜色产生相同哈希；推荐使用secrets或hmac生成安全随机数。
- 🌐 作者提供了基于网络的服务端（prover）和客户端（verifier）演示，并开放API文档，支持读者自行构建客户端。
- 🧩 同一思路可应用于数独：洗牌数字代替颜色，揭示行、列、盒代替边，即可证明完成数独而不泄露解法。
- 🔄 任何NP完全问题都能通过多项式时间归约转化为3-着色，从而构建零知识证明；但实际归约可能产生巨大图，如大整数分解。
- 🚫 作者明确表示对加密货币场景不感兴趣，更享受图论、计算理论与网络编程结合的乐趣。

---

### [](https://addyo.substack.com/p/agentic-code-quality)

**原文标题**: [Agentic Code Quality - by Addy Osmani - Elevate](https://addyo.substack.com/p/agentic-code-quality)

在 AI 智能体大规模编写代码的时代，传统人工审查已无法扩展，代码质量取决于你在智能体周围设置的约束与质量门。通过自动化检查、背压机制和有选择地投入人类注意力，才能在高速交付中守住质量底线。

- 🤖 智能体生成的代码量远超人工可读范围，质量必须依赖环境、工具和约束来把关，而非逐行人工审查。
- 🧪 质量门形式多样，包括单元测试、属性测试、验收测试、变异测试，以及圈复杂度等可读性指标，决定提案能否被接受。
- ⚠️ 智能体在信息缺失或任务模糊时可能失败，环境需要提供可信反馈、低损害失败模式和渐进式成功路径。
- 🛡️ 信任必须靠约束与验证来赢得，不能盲目接受智能体的意图或输出，正确性始终需要检查。
- 👁️ 人类注意力是稀缺资源，应聚焦于最需要判断力的复杂问题，只在自动化护栏失效时介入。
- 📊 软件质量不是单一指标，而是正确性、可维护性、性能、安全、效率、可理解性等多维信号的集合。
- 🔁 背压应贯穿整个流水线，从编译器、测试、安全策略到 CI 部署，而不是到最后才做一次终审。
- ⚖️ 当变更量超过验证容量时，可扩展验证系统、降低生成速率或调整质量条，也可在低风险处放宽约束以提升吞吐。
- 🎯 在关键处施加强约束，在无关处放松，平衡创新与质量，并始终保持人类对最终决策的责任。

---

### [](https://blog.florianherrengt.com/ai-removing-middle-class-software-engineering.html)

**原文标题**: [AI is removing the middle class of software engineering](https://blog.florianherrengt.com/ai-removing-middle-class-software-engineering.html)

overview summary
- 🚀 AI让代码产出速度飙升，但理解与评审速度没变，导致团队以惊人速度积累技术债。
- 🧩大型AI生成的PR（如两万行改动）无人真正理解，设计决策可能藏在冗长的AI聊天记录里。
- 💸弱工程文化的团队在AI加速下更快崩溃，坏工程师的破坏力从“慢速车祸”变成“高速撞击”。
- 🛠️修复坏决策极难（比如数据库迁移），同时新坏代码持续合并，形成恶性循环。
- 💰AI拉大工程师薪资差距：优秀者更值钱，糟糕者几乎不可雇用，判断力成为稀缺核心能力。
- ⚖️反驳常见观点：过程、测试无法完全阻挡AI垃圾；批评AI不等于反AI；高产出可能是偷走他人时间。
- 🧠用AI替代理解是致命错误，应把AI当作构建理解的工具，而非逃避思考的借口。
- 🔮行业未来：维护复杂系统仍需人类架构能力，减少初级岗位会破坏长远发展。

---

