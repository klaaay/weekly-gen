### [](https://ratfactor.com/cards/git-commit-size)

**原文标题**: [How big is a Git commit? - ratfactor](https://ratfactor.com/cards/git-commit-size)

Git 提交的大小并不固定，取决于文件内容的可压缩性和仓库结构。作者通过多个实验测量了不同场景下 `.git` 目录的增量大小，发现小提交有数 KB 的开销，而大文件提交由于压缩效率高，实际存储量远小于原始文件。

- 📊 Git 对象以 zlib 压缩存储，提交大小取决于内容可压缩性；之后还会打包为 packfiles 以进一步消除冗余。
- 🗂️ 空仓库 `.git` 约 64.8KB；首次提交 250 个微小文件（5 目录×50 文件）后增加约 47.6KB。
- ✏️ 在含 50 个文件的目录中修改 3 字节内容，单次提交增加约 17.1KB；单文件仓库仅增加约 8.7KB。
- 📦 提交 580KB 二进制文件，增加约 297.9KB；提交 16.4MB 源代码文件，仅增加约 1.6MB。
- 🔍 单文件变更会产生 4 个新对象：commit、两个 tree 对象和一个 blob 对象。
- 💡 小提交有几千字节固定开销，大提交压缩后仅占原始文件的 10%–50%，整体非常高效。

---

### [](https://www.jolli.ai/memory?utm_source=newsletter&utm_medium=post&utm_campaign=pd-nw-lp-1&utm_term=jolli+memory)

**原文标题**: [Jolli Memory – Knowledge that remembers your code and context](https://www.jolli.ai/memory?utm_source=newsletter&utm_medium=post&utm_campaign=pd-nw-lp-1&utm_term=jolli+memory)

Jolli Memory 是一款本地优先的 AI 编码记忆层，自动捕获每次提交背后的推理、备选方案和上下文，让所有编码代理跨会话复用这些记忆，从而减少重复解释、节省 token 并加快开发速度。

- 🔒 本地优先、默认私有：记忆只存于本机，云端同步或团队共享均需主动选择开启。
- 🧠 捕获“为什么”：记录每次提交选择的方案、被拒绝的替代方案、遇到的障碍，以及使用的工具和代理。
- 🔄 无痛复用：任何代理都能召回精确的推理和上下文，无需重新解释代码库，可无缝恢复会话或交接分支。
- ⚡ 性能与成本优化：通过提供精确上下文而非文件转储，可减少 50% 的 token 消耗，并让代理响应速度翻倍。
- 🛠️ 广泛集成：支持 28+ 工具（如 Claude Code、Cursor、Gemini CLI、Codex、GitHub Copilot）及主流 Git 托管平台（GitHub、GitLab、Bitbucket 等）。
- 📚 构建活知识库：记忆按提交和分支自动汇总，可生成 Wiki、规格文档、团队站会摘要、风险与差距报告。
- 👥 个人与团队均适用：个人开发者可加速调试和 PR 审查；团队管理者可跟踪 token/成本、发现风险和合规问题，快速完成 RCA。
- 🔗 与现有方案不同：对比手工维护的 claude.md 更自动且不过时；与代码审查工具互补；它优化上下文层，而非模型推理层，且与模型无关。
- 🚀 快速上手：macOS/Linux 一行 curl 命令安装，无需注册即可开始捕获记忆，已有 4k+ 下载量。

---

### [](https://lukasniessen.medium.com/harness-engineering-deep-dive-where-the-term-came-from-and-how-to-actually-build-one-a955bcdf5cce)

**原文标题**: [Medium](https://lukasniessen.medium.com/harness-engineering-deep-dive-where-the-term-came-from-and-how-to-actually-build-one-a955bcdf5cce)

此文章深入探讨了“harness engineering”（护栏工程）这一概念，主张“Agent = Model + Harness”，并指出在真实生产环境中，真正起决定性作用的是围绕模型构建的整套系统，而非模型本身。文章回顾了术语的起源与演进，拆解了 harness 的分类与核心组件（传感器、账本、完成验证、工具网关、预算等），并讨论了商业架构层面的启示与常见误区。

- 🧠 核心公式：Agent = Model + Harness。模型是租来的、会被替换；harness 是你拥有的代码。失败时应改变环境让失败结构上不可能，而非等待更好的模型。
- 📜 术语渊源：来自测试 harness、评估 harness（如 lm-evaluation-harness）和强化学习环境；2026 年初正式成为学科，源自多篇关键文章与 OpenAI 工程报告。
- 📈 演进脉络：从 prompt engineering（优化一条消息）→ context engineering（优化上下文窗口）→ harness engineering（优化一次多步运行），是层层嵌套而非彼此取代。
- 🗂️ 核心分类：内层 harness（厂商 SDK）与外层 harness（自建指令/MCP/钩子/评估等）；引导型 vs 传感型；计算型 vs 推理型。其中计算型传感器（如测试套件）最强，指令文件最弱。
- 🔧 传感器是转换器而非管道：将 pytest 原始输出转成“一行摘要 + 有限细节 + 建议下一步”，并预读取代码窗口，避免模型浪费一轮去读文件。
- 📒 账本是真相：状态不存于消息历史，而存于可持久化的 ledger 文档，每轮重新渲染；完整轨迹另行存储用于审计，账本只保留影响下一步决策的字段。
- ✅ 完成必须验证：模型不能自认完成；将“尝试完成”注册为工具，由机器检查退出标准（测试、类型检查、范围约束、无密钥等），通过才允许结束。
- ⛓️ 缩小行动空间：与其在 AGENTS.md 里写“先跑迁移”，不如让工具自动执行迁移或让应用启动时强制报错；用 schema 约束调用参数，使错误用法无法表达。
- 💰 预算与停滞检测：除了步骤/令牌/时间预算，还需检测“工作空间和账本哈希连续 N 步不变”的停滞；预算检查在模型调用前、计费在消耗处、停滞检测在每步末尾。
- 🛡️ 工具网关分级：按读/写/外发/变更分权限层级；授权必须基于参数（例如 tenant_id），避免 confused deputy；审批分支应明确“不要重试或找变通”。
- 📼 轨迹是调试单元：保存可重放的完整轨迹（上下文、模型输出、工具结果、状态变化），用于回答“哪个传感器没拦住”“上下文是否在压缩时丢失”等问题。
- 💼 商业与架构启示：模型对比必须固定 harness；护城河是自建外层 harness（存于自己仓库）；AI 就绪度取决于工程基础（类型系统、快速测试等），而不是提示词技巧。
- 💸 成本主要由 harness 决定：劣质传感器和累积式账本会浪费大量 token；高质量 harness 可降低 10–50 倍 token 消耗；平台团队与领域团队按“环/工具/预算”与“领域指南/传感器”拆分职责。
- ⚠️ 常见错误清单：用更长指令文件代替传感器、直接管道输出工具结果、让模型自认完成、状态只存于对话历史、只计数步骤不检测停滞、不固定 harness 比较模型、把外层 harness 建在厂商 UI 里、暴露所有工具、忽略轨迹存储等。

---

### [LLM 如何理解你的意思——无需数学学位 – Zarar 的博客](https://zarar.dev/how-ai-figures-out-what-you-mean-no-math-required/)

**原文标题**: [How LLMs Figure Out What You Mean - No Math Degree Required – Zarar's blog](https://zarar.dev/how-ai-figures-out-what-you-mean-no-math-required/)

概述：这篇文章用“Do lions roar?”这个简单句子，通俗易懂地解释了大型语言模型（LLM）如何理解词语之间的关系。从把单词变成数字（向量）开始，再到用向量的方向比喻含义，用点积计算相似度，最后通过 softmax 转换为注意力权重，整个过程不涉及复杂数学，帮助你建立清晰的直觉。

- 🔢 首先，每个单词会被转换为一个“token id”（数字），然后再变成一个向量（一串数字），因为单个数字无法承载含义。  
- 📏 向量的维度越多，能存储的意义就越丰富；真实模型中通常有数百或数千个维度。  
- 🎯 理解关系的关键是比较不同单词向量之间的“距离”或“方向”：方向相同表示相关，相反表示对立，直角表示无关。  
- 🛒 用“点积”（dot product）来量化两个向量的相似程度：分数高则相似，接近零则无关，负分则相反；可以用两人推购物车的比喻来理解。  
- 🍕 原始分数需要转化为相对权重：每个单词像拥有一整块披萨或 1 美元，将“注意力”分配给其他词——越相关的词分到的份额越大，这就是 softmax 机制。  
- ❓ 例句中的问号也是一个 token，与普通单词一样被处理，具有自己的含义，只是文章中为了方便才省略了它。  
- 🧠 初始向量是随机生成的，模型通过阅读海量文本并反复调整数字（反向传播），才最终让相似的词指向相近的方向。

---

### [认识爱丽丝。爱丽丝没有耐心。- 马克的博客](https://brooker.co.za/blog/2026/06/19/waiting.html)

**原文标题**: [Meet Alice. Alice is impatient. - Marc's Blog](https://brooker.co.za/blog/2026/06/19/waiting.html)

本文討論了「檢查悖論」（inspection paradox）如何造成服務端指標與使用者實際體驗之間的巨大落差，並解釋為什麼尾部延遲與長恢復時間才是影響使用者感受的關鍵。

- 📊 服務端統計的是「每個事件」的平均時間（如 MTTR、平均請求時間），但使用者是「每秒鐘」在體驗；越長的事件會被越多次取樣，因此使用者感受到的均值會偏向長尾。
- ⚖️ 數學上，使用者感知的平均值為 E[X²]/(2E[X])，等同於 ½(E[X] + Var(X)/E[X])；變異數越大，感知值與傳統平均值差異就越驚人。
- 🧪 用中位數與 p99 配合對數常態分佈模擬：若中位恢復時間 30 分鐘、p99 為 10 小時，服務端 MTTR 約 1 小時，但使用者感受到的平均恢復時間卻接近 6 小時。
- 💻 程式模擬顯示，在單一故障期間，以 Poisson 過程到達的客戶端會多次取樣，且每次取樣權重與「剩餘故障時間」成正比，重現了 t-weighted 效應。
- 🎯 尾部延遲與長恢復時間極其重要；超時重試可能部分隱藏服務延遲，但對恢復時間完全無法隱藏，長尾巴直接主宰使用者體驗。
- 🚫 作者不喜歡截尾均值（trimmed means），因為它丟棄了右尾的關鍵資訊，而右尾正是決定使用者感受的部分；這也與 Little’s Law 和容量規劃有關。
- 📈 真實系統的恢復時間常呈重尾分佈，變異數遠大於平均值；短故障已有成熟解法，長故障卻難以克服，導致使用者看到的情況比服務端指標嚴重得多。
- 📝 文中選用對數常態分佈只是為了計算方便，並非認為它最適合描述延遲或恢復時間；作者主張應使用非參數方法來分析真實資料。

---

### [](https://lyra.horse/blog/2026/06/reddit-spam-internals/)

**原文标题**: [A peek into Reddit's anti-spam internals Ʊ lyra's epic blog](https://lyra.horse/blog/2026/06/reddit-spam-internals/)

overview summary
这篇文章讲述了作者在 2021 年因 Reddit 的漏洞意外看到内部反垃圾邮件移除原因的经历，并据此结合公开源码、截图和官方资料，深度分析了 Reddit 反垃圾系统的运作机制，包括域名封禁、spammit、屏蔽用户、shadowban、spamurai 以及相关的工程架构与安全启示。

- 🔍 作者因 Reddit 内部错误，短暂看到了原本不可见的移除原因，并截图为证，随后这些信息被用于逆向分析。
- 🛡️ Reddit 由众多个 subreddit 组成，版主可移除内容，但“Auto”和“Reddit”移除代表管理员或自动反垃圾系统介入。
- 🧩 通过分析旧版开源代码，发现移除操作会在 `banner` 字段中记录原因，但通常只有管理员可见，普通用户只会看到“Auto”。
- 🚫 域名移除是最早的一类，包含类似“le sexxxxy sex spam”的趣味原因，还曾针对 Tumblr 等站点批量封禁。
- 📊 spammit 会给帖子打上“xx% spammy”的百分比评分，但误杀率高，很多正常 Imgur 图片也被标记为 70% 以上。
- 👤 被封禁用户的帖子会显示“banned user”或“banall performed”，通常是管理员针对明显垃圾账号的清除操作。
- 🌑 shadowban 移除记录会显示“shadowban applied on [日期]”，被屏蔽用户本人不知情，仍能发帖但他人不可见。
- 🤖 spamurai 是现役的主要反垃圾系统，包含 echelon 关键词过滤、基于账号年龄/行为/评分的规则，以及详细的移除信息转储。
- 📡 spamurai 信息中包含大量数据：帖子 ID、Perspective 垃圾分数、账号年龄、ISP、邮箱域名、浏览器 UA、TLS 指纹、语言、来源页等。
- 🔑 作者确认 spamurai 使用 Google Perspective API，并通过自己调用 API 重现了完全相同的分数，证明该系统可被绕过。
- 🧪 Perspective 的 SPAM 分数对微小改动极敏感，例如加两个字母就能从 86% 降到 1%，且忽略大小写、数字甚至西里尔字母。
- 🕵️ 部分移除基于 URL 被打开后抓取页面内容，例如匹配 Google Analytics ID，作者测试时导致账号被立即封禁。
- 🧾 还观察到一些神秘移除原因，如链接到内部 PM 的移除、奇怪的“Janitor russian girls chat”，以及因网站涉及人肉内容而封禁整个域名的例子。
- 🏗️ Reddit 反垃圾技术栈包括 REV1/REV2、Snooron，以及 Lua 规则引擎；spamurai 与旧版 REV1 相关，新系统还可能使用 OCR、Hive、Google Vision 等。
- 💡 作者选择在 2026 年公开这些信息，因为 Perspective API 即将停用，且 LLM 已彻底改变垃圾信息攻防的格局，旧系统的细节不再危险。

---

