### [在Facebook上推出视频通话 - 作者：苏飞](https://molochinations.substack.com/p/shipping-video-calling-on-facebook)

**原文标题**: [Shipping Video Calling on Facebook - by Philip Su](https://molochinations.substack.com/p/shipping-video-calling-on-facebook)

overview summary
- 🚀 文章回顾了作者16年前在Facebook西雅图办公室参与开发首个视频通话功能的经历，从初创小团队到发布后的高压冲刺，既有技术挑战也有温暖回忆。

- 🏢 作者是Facebook西雅图办公室第二名工程师，当时Facebook总共只有500名工程师，办公室仅四张桌子，音乐24小时循环播放。
- 👥 团队规模极小，作者一度是唯一全职开发者，后来加入了Thiago Hirai、Denise Noyes和Vijaye Raji等杰出同事。
- 🧠 产品评审直接与马克·扎克伯格进行，他曾故意提出“不接听直接连接”的极端建议，实为测试团队对“即时性”概念的探索边界。
- 📞 视频通话依赖Skype客户端二进制文件，但Skype技术表现糟糕，呼叫建立成功率仅82%，且对方竟没有相关数据。
- 🤔 Skype工程师对82%成功率难以置信，但作者索要他们自己的数据时，对方却称只有“用户满意度”指标，而这本身存在逻辑漏洞。
- 📉 通过视频通话日志，团队也发现了Facebook自身消息投递可靠性不足的问题，并以此推动改进底层基础设施。
- 🔔 早期版本视频通话的铃声是F-A-C-E四个音符，由一位未曾谋面的音频设计师巧妙构思。
- 📰 发布时作者作为核心成员接受“媒体培训”并参与记者沟通，这让他感到些许不自然。
- 🔥 发布后六周是作者职业生涯中最艰苦的时期，每天从早8点到午夜持续工作，靠垃圾食品维持，反而减重超过10磅。
- 👨‍👩‍👧‍👦 Facebook视频通话让作者第一次与父母通过视频交流，这让他深感科技拉近亲情的魔力。
- 🌍 十六年后，WebRTC已让视频通话成为标配，但当时一切都未成定数，这段“烈火洗礼”令他终身难忘。

---

### [](https://info.langchain.com/guide/the-agentic-operating-model/?utm_medium=paid-email&utm_source=programmingdigest&utm_campaign=q3-2026_agentic-operating-model_cv)

**原文标题**: [LangChain | The Agentic Operating Model](https://info.langchain.com/guide/the-agentic-operating-model/?utm_medium=paid-email&utm_source=programmingdigest&utm_campaign=q3-2026_agentic-operating-model_cv)

本指南介绍企业如何在生产中规模化运行AI代理，提出“代理化运营模式”（Agentic Operating Model），涵盖人员、流程与技术的协同，并给出从开发到持续改进的完整框架。

- 🤖 传统软件开发生命周期不适合代理系统，改用“代理开发生命周期”（ADLC），以评估驱动、持续循环迭代。  
- 👥 构建三类代理构建者角色：平台工程师、领域工程师与非技术主题专家，避免集中瓶颈、分散混乱和工程师单干等失败模式。  
- 🧪 生产级评估实践包括数据集构建、评估器选择，以及从追踪到修复的数日闭环，而非数季度。  
- 🛡️ 治理、FinOps 和安全通过具体执行点落地，对应不同风险等级与成本杠杆，而非仅停留在政策层面。  
- 🚗 案例：全球汽车制造商将代理部署时间从3个月缩短至1周；全球电信公司在数十个受监管实体中实现治理优先，无需重建平台。  
- 📥 下载指南可了解生产代理开发中人员、流程与技术同步推进的具体方式，并体验 LangSmith 的相关能力。  
- 📄 相关资源：ADLC 博客、Interrupt 2026 发布汇总、LangSmith Engine 介绍等。

---

### [](https://blog.florianherrengt.com/ai-removing-middle-class-software-engineering.html)

**原文标题**: [AI is removing the middle class of software engineering](https://blog.florianherrengt.com/ai-removing-middle-class-software-engineering.html)

2020年，你还能靠休假回来收拾烂摊子；到了2026年，AI让代码库在短短一个周末就能变得面目全非。25,000行的AI生成PR、没人真正理解的数据流、靠Claude对话充当设计文档——这一切都指向一个核心问题：AI极大加速了“产出”，却没有加速“理解”。作者认为，好工程师因此更有价值，而坏工程师则变成昂贵且危险的负债，并逐一回应了“坏工程师一直存在”“过程可以修复”“更多输出等于更高效”等常见辩护。

- 🧳 过去资深工程师度假回来收拾烂摊子；如今AI让烂摊子成为每个周一早晨的常态。
- 📈 AI移除了“速度限制”，让团队在数月内就积累起过去数年才能造成的技术债务。
- 🤖 工程师不再理解自己的代码，甚至把Claude对话链接当作架构决策的依据。
- 💥 大型AI生成的PR（+24506 / -3938）根本无法有效审查，每个人都仓促合并。
- 🎭 对不懂技术的人来说，AI生成的代码“看起来能用”，但没人知道系统为何失效。
- 💸 坏工程师可以用AI一天产出过去一年的代码量，把审查和修复成本转嫁给团队。
- 🏆 好工程师因AI变得更具生产力、更有价值；坏工程师则几乎变得不可雇佣。
- 🧠 编译器类比不成立：LLM是在替你做出架构和设计决策，而非简单翻译语义。
- 📊 PR数量、代码行数不是生产力指标，可能只是在消耗最稀缺的资深工程师时间。
- 👶 用AI来提升理解是正确的；用AI替代理解，会让资深开发者比勤奋的初级者更糟。
- 💡 作者是重度AI用户，但仍认为“理解系统”是无可替代的核心能力。
- 📉 技术债务并非都坏，关键是你是否意识到捷径；而无意识累积的债几乎无法偿还。
- 🔮 行业若减少初级开发者，将自毁未来；能维护大型系统的人只会更值钱。

---

### [](https://vitaut.net/posts/2026/yy-dtoa/)

**原文标题**: [The fastest double-to-string algorithm you’ve never heard of](https://vitaut.net/posts/2026/yy-dtoa/)

overview summary
- 🚀 本文介绍了一种名为“yy”的高性能浮点数转字符串算法，源自yyjson库，属于Schubfach家族，以极快的速度和仅需一次乘法为特点。
- ⚙️ yy的核心思想是寻找能“往返”转换回原浮点数的最短十进制表示，通过相交舍入区间与十进制网格，选择最粗的可用网格。
- 🔢 算法为每个二进制浮点数评估四个候选十进制值：相邻整数（d1、u1）和相邻10的倍数（d0、u0），优先输出更短的d0或u0。
- ✅ 三个谓词基于定点计算和半ulp带判断候选是否有效，并处理舍入到偶数；δ由预计算幂只需移位得到，无需额外乘法。
- 🔍 文章使用E4M3（8位浮点格式）进行可视化，逐步骤展示算法流程，并突出一个看似bug的边界情况：v=192时，由于p10表截断导致比较结果偏移。
- 🧮 该边界情况通过ηc=-1的阈值调整得到修正，使谓词正确触发并输出更短的“2e2”，而非错误的“19e1”。
- 🧪 文中提供了可交互的HTML探索器，让读者亲手验证不同编码下的输出变化，并强调这类算法虽无论文引用，但值得关注。

---

### [](https://fabiensanglard.net/quake_shareware_cd/index.html)

**原文标题**: [Quake Shareware, a CD-ROM just a little too full](https://fabiensanglard.net/quake_shareware_cd/index.html)

在90年代中期，CD-ROM大容量为游戏带来了新的分发可能。id Software在Quake共享版光盘中加密了完整游戏目录，让玩家通过电话付费解锁。然而，这套基于“隐匿安全”的机制在39天内即被黑客破解，且解锁系统本身还存在多处Bug和疏漏，最终沦为一次失败的反盗版实验。

- 💿 Quake共享版CD于1996年8月30日发售，售价$9.95，内含完整游戏加密版，需拨打1-800-ID-GAMES付费解锁。
- 📦 id Software本想利用CD剩余空间绕过零售商，但加密的游戏库很快被黑客组织GNOMON在39天后用QCRACK.EXE破解。
- 🔐 解锁流程看似可靠：程序生成动态CHALLENGE，用户致电获得SERIAL，且SERIAL不可重用。
- 💡 致命缺陷在于SERIAL只是“付款证明”，FLOW.EXE本地就能自行计算并校验SERIAL，整个保护仅靠代码混淆。
- 🔢 破解者逆向出算法：CHALLENGE拆分游戏ID和偏移量，经SKU.17、DOC文件及查表运算，最终生成SERIAL。
- 🐛 Final Doom因SKU.17中“Final”大小写错误，导致付费玩家反而无法解锁，盗版用户体验更佳。
- 📂 光盘内还残留明文SKU.TXT、临时文件及编辑备份，加密数据库格式也未做有效混淆。
- ⏳ 整体设计充满赶工痕迹，正如作者所言：这不是恶意，而是时间压力下的愚蠢与疏漏。

---

### [](https://tech.instacart.com/how-instacart-built-a-modern-search-infrastructure-on-postgres-c528fa601d54?gi=4bcf8cd2315d)

**原文标题**: [Medium](https://tech.instacart.com/how-instacart-built-a-modern-search-infrastructure-on-postgres-c528fa601d54?gi=4bcf8cd2315d)

overview summary
本文介绍了Instacart如何将搜索基础设施从Elasticsearch迁移到Postgres，并最终通过pgvector在单一Postgres引擎中实现全文检索与语义检索的混合召回。文章详细阐述了原有双检索栈的痛点、系统演进过程、pgvector的选型与调优，以及上线后带来的实际收益。

- 🔍 搜索是Instacart用户的主要入口，面对数十亿商品，需要兼具速度与相关性。
- ⚠️ 原有架构中，Postgres负责全文检索、FAISS负责语义检索，导致过度抓取、难以控制精度与召回、运维负担重。
- 🎯 核心目标：结合关键词匹配与语义理解，提升相关性；降低延迟；统一并简化检索栈。
- 📈 面临极端规模挑战：每日数百万查询、数十亿次写入（价格/库存实时变动）、复杂个性化偏好。
- 🔄 演进路径：Elasticsearch全文搜索 → Postgres全文搜索 → 引入FAISS语义搜索 → 使用pgvector实现混合搜索。
- ✅ 迁移至Postgres全文搜索：采用规范化数据模型，写入负载降低10倍；支持ML特征存储；计算靠近存储，性能翻倍。
- 🧠 FAISS语义搜索曾提升质量，但存在无法动态过滤、双系统数据一致性差、开发运维成本高等问题。
- 🗄️ 选择pgvector：由于已在Postgres上运行全文搜索，pgvector可统一两种检索机制，减少数据重复与维护成本。
- 🧪 通过离线原型集群模拟生产流量，验证pgvector满足吞吐与延迟要求，且召回率优于FAISS。
- ⚙️ 索引与参数调优：按零售商特征构建混合索引，调整并行worker数量，嵌入列改为内联存储，避免TOAST开销。
- 📊 线上A/B测试显示，零结果搜索减少了6%，显著提升用户完成购物率与平台收入。
- 🏷️ 属性过滤优势：利用单一数据存储可执行实时库存预过滤，未来将探索品牌、类别等更多属性过滤。
- 🏁 总结：pgvector混合检索架构统一了召回机制，提升搜索质量，降低运维复杂度，为后续优化奠定坚实基础。

---

### [压缩即预测 | ngrok 博客](https://ngrok.com/blog/compression-is-prediction)

**原文标题**: [Compression is prediction | ngrok blog](https://ngrok.com/blog/compression-is-prediction)

压缩本质上是预测：文章从基础压缩原理出发，讲解熵编码、概率模型与上下文建模，最终论证大语言模型（LLM）与压缩算法在数学上殊途同归——都是通过预测符号概率来最小化比特数。

- 📦 压缩依赖数据冗余：游程编码等变换可将重复字符序列大幅缩减，例如“A9B4C2D1A3D9”把28字符压到12字符。
- 🧩 现代压缩工具由变换、模型和熵编码器组成：模型提供符号概率，熵编码器将概率转换为最终比特流。
- 🔢 算术编码可将整段数据编码为单一数值：符号概率越高，最终范围越窄，所需比特越少；例如“ABABAAC”从56位压到约10位。
- ⚖️ 熵是压缩的理论下限：用 −log₂(概率) 计算每个符号所需比特数，平均后即为熵；概率分布越偏斜，熵越低，压缩率越高。
- 🌳 哈夫曼编码用决策树分配码字，高频符号获得短码，但受限于整数比特；算术编码则更接近熵极限。
- 🧠 上下文建模大幅提升预测能力：例如字母U在英文中概率约0.028，但跟在Q后概率升至0.999，比特数从5.158降至0.001。
- 🔍 高阶模型（如order-1）通过前一个符号动态调整概率，可将“TO BE OR NOT TO BE”的压缩输出从47位降至21位。
- 🤖 LLM本质上是超强预测器：基于上下文为下一个token分配概率，压缩时直接编码真实token，而非采样生成。
- 🏆 优秀模型压缩效果显著：对狄更斯名句，order-1模型压缩到原大小24%，GPT-2仅需10%。
- 🚫 实际应用受资源限制：LLM体积巨大、计算昂贵，不适合压缩HTTP响应等轻量任务；传统gzip/Brotli开销极小。
- 🔄 压缩与语言建模是同一枚硬币：熵编码器已是成熟技术，关键在模型质量；LLM训练优化的交叉熵正是压缩中的熵指标——压缩即预测，LLM即压缩器。

---

