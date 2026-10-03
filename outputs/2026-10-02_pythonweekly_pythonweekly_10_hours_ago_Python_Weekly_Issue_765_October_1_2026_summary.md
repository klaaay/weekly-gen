### [MCP SDK OAuth 漏洞导致账户接管（内含 CVE 修复）](https://cycode.com/blog/mcp-python-sdk-oauth-account-takeover/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-765-october-1-2026)

**原文标题**: [MCP SDK OAuth Flaw Enabled Account Takeover (CVE Fix Inside)](https://cycode.com/blog/mcp-python-sdk-oauth-account-takeover/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-765-october-1-2026)

Cycode 发现 MCP Python SDK 的 OAuth 登录流存在账户接管漏洞：恶意 MCP 服务器可通过触发 fallback discovery 使 issuer 校验被跳过，进而控制登录配置，诱使 SDK 将 client secret、授权码和 PKCE code_verifier 发往攻击者，最终在真实身份提供商处换取有效令牌。问题影响多个 SDK 版本和三个认证提供者，官方已在 mcp 2.2.0 / 1.30.0 修复并发布协调披露。

- 🧩 MCP 是 Anthropic 提出的开放标准，用于连接 AI 助手与外部工具/数据源，现由 Linux Foundation 的 Agentic AI Foundation 维护。
- 🚨 核心风险是完整账户接管：攻击者拿到长期可复用的 client secret、有效授权码和 PKCE 证明密钥。
- 📦 受影响版本包括 MCP Python SDK 1.9.1–1.29.1 和 2.0.0–2.1.1（文章短述为 1.9.1–2.1.1），涉及 OAuthClientProvider、ClientCredentialsOAuthProvider、PrivateKeyJWTOAuthProvider。
- 📊 漏洞评级为 High / 7.5；交互式 OAuthClientProvider 为 6.5，无人值守提供者为 7.5。
- 🔍 正常 discovery 应先获得授权服务器 URL，再校验其 issuer 字段是否匹配，这是防止恶意服务器撒谎的关键控制。
- 🕳️ 攻击者让服务器对 discovery 返回 404，触发 fallback 路径；此时 auth_server_url 为 None，issuer 校验根本不会运行。
- 🎭 攻击者在 fallback 配置中把 issuer 伪造成真实登录提供商，使凭据绑定检查被“谎言”通过，真实凭据被保留并发送到攻击者控制的 token endpoint。
- 🔑 PKCE 本应让被盗授权码无法单独使用，但 code_verifier 会与授权码、client secret 一起被打包送给攻击者。
- ✅ 登录页仍是真实 Google/Okta/Azure AD 页面，用户会正常批准；异常只表现为 MCP 服务器像故障一样报错或挂起。
- 🚫 audience binding 也只在现代 discovery 路径生效；fallback 下授权码没有受众限制，攻击者可拿它到真实 IdP 兑换令牌。
- 🧪 三组测试证明：Attack 成功；Control 因 issuer 校验运行而阻止；Escape 通过 issuer 但被凭据绑定阻止，真实凭据不外泄。
- ⚠️ “需要用户交互”低估风险：注册表投毒、AI 代理 prompt injection、DNS 劫持或内部入侵都可让用户无意连接恶意服务器；机器对机器提供者甚至无需交互。
- 🧨 攻击者后续可用长期 client secret 申请新令牌、用刷新令牌维持访问，并借原客户端权限横向移动；授权服务器看到的是正常登录，常规监控难以发现。
- 🛠️ 修复方案：升级到 mcp 2.2.0（2.x）或 1.30.0（1.x）或更高；新版会预先确定预期登录提供商、拒绝不匹配配置并绑定存储凭据。
- 📝 升级后还应：为 ClientCredentialsOAuthProvider / PrivateKeyJWTOAuthProvider 传入 issuer=；清除旧版保存的 OAuth 注册；若可能暴露，轮换 client secret 并撤销令牌。
- 🧠 根本模式：安全检查只在特定数据存在时执行，而攻击者可控制该数据是否存在；未验证输入流入下一检查并主动“满足”它。

---

### [](https://aiengineeringfromscratch.com/index.html?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-765-october-1-2026)

**原文标题**: [AI Engineering from Scratch](https://aiengineeringfromscratch.com/index.html?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-765-october-1-2026)

overview summary
- 🧭 《AI Engineering from Scratch》是开源 MIT 课程，强调每节已发布课程、每个阶段、每个算法都先从原始数学构建，再导入框架。
- 👨‍💻 由 Rohit Ghumare 和贡献者维护，可在自己的机器上运行。
- 💻 终端学习：`npx skills add rohitg00/ai-engineering-from-scratch`，再用 `start-learning` 开始。
- 🤖 Claude、Cursor、Codex 或任意 SKILL.md agent 可成为导师：入学测验、个性化路径、终端交互式授课。
- 📐 覆盖从线性代数到自主 swarm；反向传播、分词器、注意力、智能体循环均手写实现。
- 🧪 每课固定循环：读问题、推导数学、写代码、跑测试、保留产物；无五分钟视频或复制粘贴部署。
- 🐍 支持 Python、TypeScript、Rust、Julia 四种语言，按概念选择最合适语言；免费开源，适合个人笔记本。
- 🧭 四条核心学习路径：构建与部署 AI 应用、软件工程基础、智能体辅助工程、产品判断与交付。
- 🧑‍🎓 推荐新手先走“AI 工程入门”：搭建环境、运行仓库、熟悉课程流程，再选方向。
- 🔌 专注路径包括 MCP 和 Agent Skills，涵盖构建、安全、验证、操作、打包与评估。
- 📚 课程含 20 个阶段、523 节课；进度仅存浏览器，可重置。
- 📖 书籍版六卷，EPUB/PDF 由相同课程编译，并附在每个 GitHub release。
- 🎓 认证备考：Claude 与 MCPA，5 条轨道、67 节认证课、505 道原创练习题；与 Anthropic 等无隶属关系，不发证书。
- ⭐ 全部内容在 GitHub，可克隆/分叉，无付费墙、无注册；每课有可运行代码。
- 🏢 被 Apple、Google、Meta、OpenAI、NVIDIA、IIT Bombay、University of Windsor 等工程师与学生阅读。

---

### [](https://www.philipzucker.com/proof_uf/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-765-october-1-2026)

**原文标题**: [A Lean Proof Printing Python Union Find | Hey There Buddo!](https://www.philipzucker.com/proof_uf/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-765-october-1-2026)

文章介绍一种用 Python 实现 union find、同时输出可被 Lean 检查的等式证明的方案。作者以“证明是搜索过程的痕迹”为核心思想，把 union find 的造集、查找、合并、路径压缩等操作记录成 Lean 证明项，并用 Lean 子进程验证；之后讨论如何扩展到 e-graph、congruence closure、proof-producing union find 及相关理论方向。

- 🔍 动机：e-graph 作为后端或硬件优化工具时，常需要可检查的证明证书；没有证书可能导致工具链不可用。
- 🧩 先处理更简单的 union find：它维护连通分量，两顶点连通的证明可表示为显式路径，生成树则是紧凑的路径存储方式。
- ⚠️ 普通 union find 的森林不等同于图上的生成树，因为 `union(a,b)` 实际连接的是 `find(a)` 与 `find(b)`，而非 `a-b`；可用重定根或双结构修正。
- 💡 核心原则是“证明作为搜索痕迹”：证明数据应包含在搜索或执行轨迹中，类似 UNSAT 的 DRAT 证明；union find 和 e-graph 都在操作等式，可流式输出 Lean。
- 🐍 基础 Python UF 用 `parents` 记录父节点，`find` 带路径压缩，`union` 合并根；证明版再加入 `log`、`memo` 和 `FatId=(PId, Id)`。
- 📜 证明版 UF：`memo` 映射外部名称到内部 id 与证明 id；`makeset` 生成 `let eN := name` 与 `Eq.refl`；`find` 路径压缩生成 `Eq.trans`；`union` 用 `Eq.symm`/`Eq.trans` 组合等式。
- ✅ Lean 检查：通过 `lake env lean --stdin` 运行生成的证明；示例可证明 `(a b c : Int) (pfab : a = b) (pfbc : b = c) : a = c`。
- 🧾 输出示例会生成多行 `let e0 := a ... let p9 := trans ...`，最后用 `exact trans ...` 通过检查；合并原因名称目前需手动传入，未来可由 e-graph 规则实例化。
- 🌐 扩展想法包括：全路径 union find、2-union find/字符串 Knuth-Bendix、带证明的 FatId、proof-producing congruence closure、memo/rebuild、无用证明剪枝与死代码消除。
- 🧮 与 e-graph 的联系：`memo` 表对应 `f(e1,e2)=e7` 等式；`rebuild` 是 memo 归一化，`cong` 与 `trans` 组合成证明；类似 microegg 的实现展示 `add_term`、`union`、`find`、`rebuild`、`ematch`、`rw`。
- 🧷 更多理论方向：群胚/拉回 union find、对象与态射、线性映射、thinnings/置换、多词项表示、范畴乘积等。
- 📚 相关参考包括 Nieuwenhuis & Oliveras 的 Proof Producing Congruence Closure、Z3 证明证书讨论、简化并验证的 proof-producing union-find、Rudi 的证明注解、Graham 的 Aufbau 等。

---

### [](https://fsdatalab.github.io/blog/introducing-quail/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-765-october-1-2026)

**原文标题**: [Building an Ultra-High Throughput AI-SQL Engine | Full Stack Data Lab](https://fsdatalab.github.io/blog/introducing-quail/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-765-october-1-2026)

Quail 是面向 AI-SQL 的查询感知推理层，联合优化 SQL 查询规划与开源权重模型推理，解决 AI-SQL 逐行、逐对调用 LLM 的高成本问题；在 29 个 QUAIL-B 查询上平均比调优 vLLM 快 1.84 倍，最高快 14.04 倍，并提供 GitHub 与在线演示。

- 💸 AI-SQL 让非结构化数据可用，但逐行过滤或逐对连接会产生数十万到数百万次 LLM 调用，成本极高。
- 🧩 关键思想：查询计划应控制 LLM 推理，而不是把大量相关模型调用当作独立请求发给通用推理引擎。
- 🏗️ Quail 包含前端、查询规划器和执行引擎：接收 Arrow 数据与 AI-SQL/Python 查询，用 SQLGlot 解析逻辑计划，再降为物理算子计划。
- 🛠️ 支持 AI 过滤/连接、投影和 LIMIT；兼容 Snowflake AI_FILTER 与 BigQuery AI.IF；可指定模型、GPU 数、selectivity、join anchor 等信息。
- 🚀 执行优化：KV 管理支持“rewind”、只保留后续可复用 KV、按文档长度驱逐；流式算子间传递批次，避免物化完整数据集。
- 🔬 推理优化：复用 vLLM 模型实现，但融合小算子、针对 join 共享 anchor KV 做分组注意力、只计算 TRUE/FALSE 输出头相关行。
- ⚡ 评估设置：Qwen3 4B FP8、BF16 KV、单张 H100，对比 stock vLLM 与 pipelined vLLM，指标为 KV regret、$/query、输入 tokens/秒。
- 🏆 QUAIL-B 共 29 个查询，覆盖 IMDB、医疗报告、事实核查、法律文档和软件 agent traces；scale 0.1 下 Quail 在 27/29 查询胜出，几何平均加速 1.84 倍。
- 🩺 BIO-4 案例：scale 1.0 下 Quail 29.26 分钟，vLLM 6.84 小时，快 14.04 倍；成本 $1.93 vs $27.03；KV 重算 1800 万 vs 5030 万 tokens。
- 🤖 AGENT-1 例外：vLLM 103.07 秒，Quail 239.12 秒，vLLM 快 2.32 倍，因为 vLLM 自动前缀缓存可跨行复用重叠前缀，而 Quail 尚不支持。
- 🧠 也支持 DiffusionGemma 26B-A4B FP8：在 IMDB-2 上匹配 Qwen3 32B 答案 88.89%，优于 Qwen3 4B 的 76.41%，运行时间 32.41 秒。
- 💰 示例：10 万条 IMDB 评论双过滤查询中，Quail 找到 16057 条，总成本约 $0.3675，远低于 GPT-5 nano 估算约 $1.75。
- 🗺️ 未来方向：更多 AI-SQL 算子/模型/硬件，KV 分层存储与自动前缀缓存/压缩，提升 MFU，训练规划/执行小模型，探索类 hash join 的 AI join，并用 AI agent 构建系统。
- 📦 Quail 采用 MIT 许可，由 Modal 赞助算力；团队邀请试用、反馈，并基于其构建 LLM judge、trace compaction、标注等数据工作流。

---

### [](https://www.youtube.com/watch?v=zH2Mg782XhA&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-765-october-1-2026)

**原文标题**: [Python Algorithmic Trading Course – Massive, SnapTrade & Alpaca Integrations - YouTube](https://www.youtube.com/watch?v=zH2Mg782XhA&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-765-october-1-2026)

这些是 YouTube 页脚中的常见导航链接与版权信息，涵盖平台介绍、创作者与开发者资源、法律政策、安全机制、功能测试及版权归属。

- 🏢 公司信息与联系：About、Press、Contact us
- 👥 资源与合作：Creators、Advertise、Developers
- 📜 法律与隐私：Copyright、Terms、Privacy、Policy & Safety
- ⚙️ 平台机制与测试：How YouTube works、Test new features
- ©️ 版权声明：© 2026 Google LLC

---

### [](https://adamj.eu/tech/2026/10/01/django-security-txt/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-765-october-1-2026)

**原文标题**: [Django: serve a security.txt file - Adam Johnson](https://adamj.eu/tech/2026/10/01/django-security-txt/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-765-october-1-2026)

本文介绍如何在 Django 中提供符合 RFC 9116 的 security.txt 文件，让安全研究者知道如何报告漏洞，并通过单元测试和系统检查确保文件长期有效。

- 🔐 security.txt 是 Web 标准，用于在 `/.well-known/security.txt` 提供安全联系信息，避免研究者只能猜测联系方式或放弃报告。
- 📄 文件由 `Field: value` 行和以 `#` 开头的注释组成；必需字段是 `Contact`（联系方式，可多条）和 `Expires`（过期时间，RFC 3339 格式，只出现一次，建议少于一年）。
- 🌐 每个域名或子域名都需单独提供 security.txt，并应通过 HTTPS 以 `text/plain; charset=utf-8` 提供。
- ⚙️ 在 Django 中可用 `FileResponse` 视图提供文件，并在根 URLconf 中添加到 `.well-known/security.txt` 路径。
- 🛡️ 视图使用 `@login_not_required`、`@require_safe`、`@cache_control(max_age=300, public=True)`，分别保证公开访问、仅允许 GET/HEAD、缓存 5 分钟。
- 🧪 单元测试应检查 200 状态、`content-type`、`cache-control`，解析并验证 `Contact` 与唯一的 `Expires`（含时区），并测试 HEAD 成功、POST 返回 405。
- 📥 因为 `FileResponse` 是流式响应，测试中需用 `getvalue()` 读取完整正文，而不是直接使用 `text` 属性。
- ⏳ `Expires` 会过期，因此需要定期更新；可编写自定义 Django system check 在临近过期、缺失或超过一年时提醒。
- 🚨 system check 在 `Expires` 缺失时返回错误；距过期不足 30 天或超过 365 天时返回警告，并在 `AppConfig.ready()` 中导入注册。
- ✅ 这样运行管理命令时会显示警告，提醒维护者及时更新 security.txt。

---

### [为什么你需要这个新的 Python 工具 - YouTube](https://www.youtube.com/watch?v=lFA-zuZRG4Q&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-765-october-1-2026)

**原文标题**: [Why You NEED This New Python Tool - YouTube](https://www.youtube.com/watch?v=lFA-zuZRG4Q&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-765-october-1-2026)

该内容为 YouTube/Google 页脚导航与版权信息，主要提供平台介绍、媒体联系、创作者与开发者资源、广告合作、法律条款、隐私安全政策、功能测试及版权归属等入口。

- ℹ️ 关于：平台介绍信息。
- 📰 新闻界：媒体与新闻资源入口。
- ©️ 版权：版权相关信息。
- 📬 联系我们：联系渠道入口。
- 🎬 创作者：面向内容创作者的资源。
- 📢 广告：广告合作与投放入口。
- 👨‍💻 开发者：开发者资源与工具入口。
- 📜 条款：服务条款信息。
- 🔒 隐私：隐私政策信息。
- 🛡️ 政策与安全：平台政策与安全说明。
- ⚙️ YouTube 运作方式：平台机制说明。
- 🧪 测试新功能：试用新功能入口。
- © 2026 Google LLC：版权归属于 Google LLC，年份为 2026。

---

### [](https://magazine.sebastianraschka.com/p/classifier-history-and-jev?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-765-october-1-2026)

**原文标题**: [Language Models for Text Classification: From Bag-of-Words to Jev](https://magazine.sebastianraschka.com/p/classifier-history-and-jev?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-765-october-1-2026)

overview summary
本文梳理文本分类从词袋、RNN/CNN、Transformer 到 Jev 的演进，并分析 Jev 作为通用、快速、廉价的分类 API 为何引发关注：它不是单一任务分类器，而是可跨任务即插即用，但仍依赖精心数据与校准训练，且已有 OpenAI Decision API 等竞品跟进。

- 🧺 词袋模型把不同长度文本转为固定词频向量，配合朴素贝叶斯、逻辑回归、XGBoost 等经典分类器，便宜且常作基线，但丢失词序；IMDb 逻辑回归约 89.9%。
- 🧠 词嵌入把单词或标记映射为稠密向量，早期 Word2Vec/GloVe 上下文无关，现代模型可在训练中学习嵌入。
- 🔁 RNN/LSTM/GRU 逐步读取序列并维护隐藏状态，能保留词序，但训练较难；IMDb LSTM 约 85.66%，ULMFiT 通过预训练+微调达 95.4%。
- 🧱 CNN 用卷积核扫描相邻词嵌入窗口，可并行计算，IMDb 文本 CNN 约 90.07%。
- 🤖 Transformer 分化为编码器 BERT/ModernBERT、解码器 GPT 和编码器-解码器 T5；BERT 类天然适合分类，ModernBERT 在 IMDb 微调后约 95%。
- ✍️ GPT 类模型可提示分类、替换分类头微调或文本到文本分类；GPT-2 124M 在 IMDb 约 92%，更大 LLM 可能更好。
- ⚡ Jev 由 TypeSafe AI 发布，专有、低成本、低延迟，目标是无需逐任务微调即可分类多种文本，并被形容为分类领域的“ChatGPT 时刻”。
- 🔌 Jev API 主要有 Choice、Noul、Score，分别适用于多分类、二分类/多标签概率、序数评分，并返回标签、概率与置信度。
- 📊 Jev 在 IMDb 25,000 条测试集上：Choice 准确率 96.47%，成本约 $0.6492，耗时约 22 分钟；Noul 准确率 96.20%，成本约 $0.6345，耗时约 23 分钟。
- 🎮 Jev 与 ModernBERT 精度相近，但无需为每个任务微调，还能实时玩 Tetris，体现通用与低延迟优势。
- 🧩 可在 BERT/GPT/T5 上加 Jev-like API：用单输出评分头对每个候选选项打分，再 softmax 得到概率，从而支持任意类别数。
- 🏗️ Jev 架构未公开，作者猜测可能类似小型 ModernBERT；数据据称 100% 合成但经过精心筛选；训练方法称 RLCD，即基于校准决策的强化学习。
- 🎯 相关校准方法包括温度缩放和 RLCR：奖励包含正确性与置信度惩罚 c-(q-c)^2，能显著降低预期校准误差，让概率更可靠。
- 👥 Jev 适合想省去微调、又比大 LLM 更便宜快速的场景；可用于邮件分类、垃圾过滤、Agent 预筛选提示注入、选择推理强度、评审与检索文件等。
- ⚠️ 大量 Jev 克隆多基于 ModernBERT/Qwen 快速 SFT，广任务表现难匹敌；GLiNER 相似但 Jev 更强；开源替代的真正驱动力包括隐私。
- 🆕 OpenAI 已在 DevDay 2026 发布类似 Decision API；其他替代品如 Contrastive Language Models、Laya 在 IMDb 或 Tetris 测试中表现明显不足。
- ✅ 结论：Jev 并非全新概念，但把通用分类器做成即插即用 API，抬高微调门槛；它不一定解锁新能力，却可能让 Agent 决策更便宜、更快。

---

### [](https://www.youtube.com/watch?v=M1RMHhHJeNU&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-765-october-1-2026)

**原文标题**: [FastAPI Middleware - writing custom middleware functions! - YouTube](https://www.youtube.com/watch?v=M1RMHhHJeNU&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-765-october-1-2026)

这是 YouTube 页脚中的导航与法律信息摘要，涵盖平台介绍、商务合作、开发者资源、政策条款、新功能测试以及版权声明。

- ℹ️ 关于（About）
- 📰 新闻（Press）
- ©️ 版权（Copyright）
- 📬 联系我们（Contact us）
- 🎬 创作者（Creators）
- 📈 广告（Advertise）
- 👨‍💻 开发者（Developers）
- 📜 条款（Terms）
- 🔒 隐私（Privacy）
- 🛡️ 政策与安全（Policy & Safety）
- ⚙️ YouTube 运作方式（How YouTube works）
- 🧪 测试新功能（Test new features）
- © 2026 Google LLC

---

### [](https://www.youtube.com/watch?v=P3kmo04DiEw&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-765-october-1-2026)

**原文标题**: [LangSmith Crash Course: LLMOps in Python - YouTube](https://www.youtube.com/watch?v=P3kmo04DiEw&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-765-october-1-2026)

这是 YouTube 页脚导航与法律版权信息，汇总了平台介绍、合作资源、政策条款及 Google LLC 版权声明。

- 🏢 包含关于、新闻、联系我们等基础信息入口
- ⚖️ 涵盖版权、条款、隐私、政策与安全等法律与安全链接
- 👥 提供创作者、广告商、开发者等合作与资源入口
- ▶️ 介绍 YouTube 运作方式，并提供测试新功能入口
- ©️ 显示 2026 Google LLC 版权归属

---

### [](https://github.com/ollaya-dev/ollaya?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-765-october-1-2026)

**原文标题**: [GitHub - ollaya-dev/ollaya: Run open decision models locally: pull and serve Laya, decider, NLI and GLiClass behind a TypeSafe-compatible API. Ollama for decision models. · GitHub](https://github.com/ollaya-dev/ollaya?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-765-october-1-2026)

Ollaya 是一个 Rust 实现的本地决策模型运行时与守护进程，定位为“决策模型版 Ollama”：它按名称拉取并服务开放决策模型，读取状态与类型化问题（choice、score、noul），在单次前向传播中毫秒级返回校准概率，不生成文本，并能以 TypeSafe/Jev 兼容接口接入现有客户端。

- 🧠 核心机制：输入状态（消息、邮件、工单、JSON）和类型化问题，输出校准概率；模型只做决策，不生成自然语言文本。
- 🚀 推荐模型：winnow:e4b 是推荐项，4B 类，在 typed decisions 上 0.722，RTX 4090 上 5 个问题约 89 ms；无 NVIDIA GPU 可先用 CPU 友好的 laya。
- 🔌 TypeSafe 兼容：提供 /v1/systemone、/v1/decisions 和 GET /v1/models，与 TypeSafe 线格式一致；设置 TYPESAFE_BASE_URL=http://localhost:11435 后官方 SDK 可直接使用。
- 🛠️ CLI 与守护进程：单个二进制，ollaya serve/run/pull/list/ps/show/rm/cp/stop/create 类似 Ollama；守护进程未运行 CLI 会自动启动。
- 🌐 原生 API：/api/decide 增加路由与耗时，/api/pull 流式输出 NDJSON，另有 /api/tags、/api/show、/api/ps 等接口。
- 🤖 面向 Agent：ollaya mcp 可服务 Claude Code、Claude Desktop、Cursor 等 MCP 客户端；ollaya-decisions skill 教代理何时以及如何使用模型。
- 🧭 路由与自定义：laya 自动检测语言和脚本，路由到 laya:en 或 laya:multilingual；Modelfile 可把问题集烘焙进自定义模型。
- ⚡ 性能与精度：CPU 使用 ONNX Runtime 和 fp32，NVIDIA GPU 使用 CUDA 和 fp16，GGUF 模型用 llama.cpp 运行于 CPU、CUDA、Apple Metal；fp32 导出在 2,383 个问题上与 PyTorch 参考 100% 一致。
- 📚 模型生态：包括 winnow、laya、decider、kev、decision、qwen3guard、nli、gliclass、von、clm、jevk5、nimble、jeb、jeeves、cygnet 等；权重来自作者 Hugging Face，Ollaya 只发布约 3 MB ONNX 图或使用作者 GGUF，不重新托管权重。
- 📊 评测结果：公开 benchmark 上 winnow:12b 得分 0.773、约 60 ms/题；Ollaya 上 Nimble 校准误差 0.022，而 Ollama 为 0.122；发布准确率、校准、速度和与作者代码的 parity 原始数据。
- 📦 安装：Linux/macOS 用 curl 安装脚本，Windows 用 PowerShell；检测到 NVIDIA GPU 时自动添加 CUDA runtime；还提供桌面应用和 Docker 镜像。
- 🗂️ 代码结构：crates/ollaya（CLI、daemon、runner）、ollaya-server、ollaya-api、ollaya-registry、ollaya-decision、ollaya-runner、ollaya-lang；convert/ 负责 ONNX 导出、parity 检查和打包。
- 🧪 开发：cargo test --workspace；cargo build --release -p ollaya --features cuda；convert 下用 uv sync 安装 Python 构建链。
- ⚖️ 许可与独立性：项目 Apache-2.0，各模型保留自身许可；llama.cpp 为 MIT；Ollaya 是独立项目，与 Ollama 或 TypeSafe 无关联或背书。

---

### [](https://github.com/derblub/django-upgrade-report?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-765-october-1-2026)

**原文标题**: [GitHub - derblub/django-upgrade-report: Which of your dependencies block a Django upgrade, and in which order to upgrade them. · GitHub](https://github.com/derblub/django-upgrade-report?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-765-october-1-2026)

overview summary
django-upgrade-report 是一款用于规划 Django 升级的 CLI 工具：它读取项目锁文件，向 PyPI 查询所有 Django 相关依赖声明的兼容信息，输出"哪些依赖阻塞升级、按什么顺序升级"的可执行计划，支持文本、Markdown、JSON 与 HTML 报告，可无缝接入 CI。

- 🎯 **核心目标**：在动手升级 Django 前，厘清 20~200 个依赖中哪些已就绪、哪些今天就能升、哪些必须与 Django 同步升级，免去人工翻阅每个 changelog。
- 🔢 **明确升级顺序**：区分"当前 Django 下即可独立升级"与"必须和 Django 一起升级"的包；并提示某版本是否还要求更高的 Django 补丁版或其他依赖的新版本。
- 📦 **最小升级步长**：为每个包指定"最早声明支持目标版本"的发行版，让每次改动小而易于评审，而非一味升到最新。
- 📖 **兼容现有依赖文件**：支持 uv.lock、poetry.lock、pdm.lock、Pipfile.lock、requirements*.txt、pyproject.toml 及已安装环境，并包含传递依赖。
- 🤔 **诚实对待不确定性**：缺少分类器只标为"需人工确认"而非"阻塞"；目标版本发布前写的上界不被当作承诺；两年无新版本或已标记停维护的包会被标注。
- 🐍 **识别项目 Python 版本**：从 --python、.python-version、requires-python 等推断，并按项目环境（CPython/Linux）而非本机环境评估环境标记。
- 🚦 **状态语义清晰**：Blocked（阻塞）、Upgrade first（先单独升）、Upgrade together with Django（与 Django 同升）、Check manually（人工确认）、Ready（就绪）。
- 🔁 **含"已被 Django 取代"提示**：对 South、django-jsonfield 等被 Django 内置功能替代的包给出说明，需有官方来源佐证。
- 🖥️ **多种使用方式**：uvx / pipx / pip 安装即可运行；支持 --target（auto/lts/latest/具体版本）、--from、--format、--output、--fail-on 等选项。
- 🔒 **隐私友好**：仅将来自 PyPI 的包名与版本发送给索引，git、本地路径和私有索引的包只列出不查询，URL 中的凭据会被移除。
- ⚙️ **CI 集成**：提供 GitHub Actions（写入 Job Summary、输出各状态计数、可配置 fail-on）和 GitLab CI 示例，退出码可区分"包需关注"与"工具无法运行"。
- 🧠 **判断依据**：以 PyPI 上的 `Framework :: Django :: X.Y` 分类器和 `Django` 依赖要求为准，分类器优先，兼顾上界与发布时间，未发布目标仅看分类器。
- 🔗 **与其他工具互补**：Dependabot/Renovate 负责逐个开 PR，django-upgrade 改写代码，本工具负责升级规划，三者配合使用。
- 📄 **开源信息**：MIT 许可，作者 Daniel Kurdoghlian（Pushing Pixels，维也纳），当前 7 星、1 次 fork。

---

### [](https://github.com/wbopan/tastebench?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-765-october-1-2026)

**原文标题**: [GitHub - wbopan/tastebench: Taste-Bench: measuring the long-horizon judgment of LLM agents at real decision forks · GitHub](https://github.com/wbopan/tastebench?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-765-october-1-2026)

Taste-Bench 是用于衡量 LLM 智能体“品味”的基准：在长时程任务的真实决策分叉点，给定任务、分叉前轨迹与两个候选下一步，模型需选出被隐藏后续轨迹证明正确的一步。错误选择往往当下看似合理，却会在后期消耗大量预算。该基准从软件工程与机器学习研究轨迹中挖掘出 502 道题，无需专家标注，最佳前沿模型正确率为 59.7%。

- 🎯 核心定义：Taste-Bench 测量 LLM 智能体在长时程任务决策分叉处选择更优方向的能力。
- 📦 题目规模：共 502 题，来自真实软件工程与机器学习研究轨迹，最佳模型 GPT-5.6 Sol 仅答对 59.7%。
- 🏆 排行榜：GPT-5.5 为 59.5%，Claude Opus 5 为 55.5%，Grok 4.5 为 54.6%；随机猜测按协议得 25，总选同一位置得 0。
- 🧪 计分规则：每题需在原选项顺序和反向顺序中都答对才算正确；未解析输出、请求错误均计为错误。
- 🧭 题目类型：分为“并行分叉”和“绕路分叉”，并行分叉用同一任务不同尝试的结果标注，绕路分叉用放弃方向与后续恢复作为候选。
- 🔍 质量控制：丢弃仅凭候选措辞即可判断的 trivial 题，以及读完整记录后仍与标签不一致的 undecidable 题；4,657 个分叉中保留 502 个。
- 📚 数据构成：工程 390 题含 266 绕路、124 并行，来自 SWE-bench 与 SWE-bench Pro；研究 112 题含 64 绕路、48 并行，来自 METR MALT 的 RE-Bench 与 HCAST。
- ⚖️ 评测协议：使用 paired_order_v1，模型看到任务、完整 prefix_text 和两个候选，只输出 `ANSWER: X`；每题按正反两种顺序各问一次，字母重新计算。
- 🚀 快速开始：克隆 `wbopan/tastebench`，执行 `uv sync`、`tb download`、设置 `TASTEBENCH_API_KEY`，再运行 `tb run` 与 `tb score`；全量评测为 1,004 次请求，约 8M 输入 token。
- 🔐 数据访问：数据集在 Hugging Face 上受门控以限制训练污染；代码采用 MIT 许可证，数据集文本采用 CC BY 4.0。
- 📄 论文信息：论文为《The Tasteful Agent: Measuring and Improving Taste in Long-Horizon Tasks》，arXiv:2609.25804，作者包括 Wenbo Pan 等。

---

### [](https://github.com/strands-agents/harness-sdk?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-765-october-1-2026)

**原文标题**: [GitHub - strands-agents/harness-sdk: Build an agent harness and control it end-to-end. Open-source SDK for production AI agents in Python & TypeScript - any model, any cloud. · GitHub](https://github.com/strands-agents/harness-sdk?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-765-october-1-2026)

Strands Agents 是一个开源 SDK，用模型驱动方式在 Python 和 TypeScript 中只需少量代码即可构建和运行生产级 AI 代理；本仓库是包含 harness、SDK、CLI、文档与治理材料的 monorepo。

- 🧩 核心定位：适合原本需要手写 agent loop 的场景，SDK 在自身进程运行，无需托管控制平面。
- 📦 仓库结构：包含 harness-py、harness-ts、strands-cli、strands-py、strands-ts、site、team、test-infra 等目录。
- ⚡ 快速开始：推荐使用 Strands harness，通过 `create_harness()` 或 `createHarness()` 获得带基准默认配置的完整代理。
- 🚀 安装方式：Python 可 `pip install strands-harness`，TypeScript 可 `npm install @strands-agents/harness`。
- 🧰 SDK 深入：Python 需 3.10+，安装 `strands-agents` 与 `strands-agents-tools`；TypeScript 需 Node.js 22+，安装 `@strands-agents/sdk`。
- 🔄 模型无关：一等支持 Amazon Bedrock、Anthropic、OpenAI、Gemini，并支持更多提供商和自定义模型。
- 🛡️ 生产控制：内置生命周期控制、token 预算、取消、停止原因、guardrails、steering，以及可拦截每步的 hooks。
- 🔌 内置能力：MCP、流式输出、多代理模式、结构化输出、记忆、会话、追踪和评估。
- 🧭 可观测性：agent loop 默认追踪每个决策，hooks 可记录、验证或重定向任一步骤。
- 👨‍💻 编码代理集成：提供 Strands skill，Claude Code 可通过 `.claude/skills/strands` 自动发现。
- 📚 文档与社区：文档位于 `site/`，发布在 strandsagents.com；Discord 可联系团队与用户。
- 🛠️ 开发方式：Python 用 hatch 测试与格式化，TypeScript 用 npm 构建与测试，文档站用 npm run dev。
- 📈 社区指标：约 8.6k stars、1.3k forks、2,845 次提交、541 个 issues、369 个 PR。
- 📜 许可证：项目采用 Apache License 2.0。

---

### [](https://github.com/firelex/jeff?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-765-october-1-2026)

**原文标题**: [GitHub - firelex/jeff: Millisecond decisions, any domain: a 0.8B open "System 1" model that picks between your options with calibrated probabilities. One base, swappable LoRA adapters, on your own hardware. · GitHub](https://github.com/firelex/jeff?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-765-october-1-2026)

overview summary
firelex/jeff 是一个 0.8B 开源“System 1”决策模型，用单次前向传播为文字选项返回校准概率，作为大模型前的快速分类器；配合可插拔 LoRA 适配器，可在毫秒级、低内存下实现特定任务高准确率。

- 🧠 **定位**：Jeff 不生成文本，只做快速、校准的多选/是/否/评分决策；强本地模型如 Qwen3.8-27B 只在其不确定时兜底。
- ⚡ **性能提升**：8 个适配器平均，27B 单独准确率 86.6% → Jeff+适配器 95.3%，耗时 8.1s → 0.25s（38×），错误 13.4% → 4.7%，内存仅 +1.96GB。
- 🧩 **九个 LoRA 适配器**：guard、triage、support-intents、tools、ground、nav、emotion、spam、legal-clauses；每个约 41MB，单任务表现突出，如 guard 98.4%、tools 97.9%、spam 98.4%。
- 📊 **任务示例**：邮件/客服代理五决策从 87.7% 提升到 95.7%，快 39×；ground 最接近 27B，但快 20×。
- 🚀 **使用方式**：用自然语言描述情况与选项，返回每个选项概率、选择与置信度；支持 choice（最多 254 项）、yes/no、score。
- 🛠️ **快速开始**：git clone、uv sync 安装，下载 Jeff-Qwen3.5-0.8B v1.2 与所需适配器，启动 jeff-serve；提供 Python/TypeScript 客户端，适配器可热切换、无需重启。
- 📏 **使用规则**：选项键用短描述词如 "refunds"，不要裸数字；固定内容在前、变化字段在后；独立问题可合并请求。
- 🧪 **训练与数据**：适配器用 LoRA，1 个 epoch，单 GPU 约 0.5–4 小时；数据经捷径检查与独立审查；发布权重、代码、测试/校准集，不发布训练数据。
- 🏁 **基准表现**：5 个公共基准 4599 题，Jeff-Qwen3.5-0.8B 总体 78.7%，2B 81.7%，Gemma4-E2B 81.6%；分类/接地强，推理密集任务较弱。
- 🖥️ **速度与体积**：RTX PRO 6000 上 0.8B 22ms、2B 24ms；M4 Max 28ms；CPU 463ms；九个适配器全载切换中位 30ms，GPU 内存 1.96GB。
- 🎮 **零样本游戏/象棋**：零样本可玩 Doom、Frogger、Pac-Man；象棋微调后解 55.8% 保留谜题，约 1000 Elo，无搜索，每步一次前向传播。
- ⚠️ **限制**：适配器绑定基座版本，v1.2 仅配 v1.2，v1.3 需重训；小模型不做多步推理；英文文本；Qwen 最多 254 选项，Gemma 仅 26。
- 📦 **版本与许可**：v1.2 为社区预览，v1.3 LTS 约 36 小时内发布；代码 MIT，权重 Apache 2.0；源自 AutoJev，与 TypeSafe/Jev 无关。

---

### [](https://github.com/ninjahawk/livenerf?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-765-october-1-2026)

**原文标题**: [GitHub - ninjahawk/livenerf: Benchmark for tracking model capability after release. · GitHub](https://github.com/ninjahawk/livenerf?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-765-october-1-2026)

livenerf 是一个长期、尽量确定性的基准测试，用于检测前沿模型在发布后是否悄悄变差，尤其回应 Anthropic 模型被“削弱”的传闻。它从 Claude Opus 5.5 发布后启动，每天运行 30 天，使用 Claude Max 订阅通过无头 Claude Code，冻结提示词、固定 CLI、精确评分器和原始日志，并用统计方法度量能力漂移。

- 🎯 目标：检测模型发布后是否出现真实能力漂移或静默降级，并区分变化与噪声。
- 📅 时间线：Opus 5.5 于 2026-09-22 发布；Day 1 为 2026-09-24，运行 30 天，前 10 天为基线；截至 2026-10-01 已收集 8/30 天。
- ⚙️ 运行方式：通过 headless Claude Code（`claude -p`）和 Claude Max 订阅运行，无需 API key；固定 CLI 版本 2.1.280，并关闭自动更新。
- 🔬 确定性设计：冻结系统提示词、固定 CLI、使用纯函数评分器、保存原始 `.eval` 日志，统计漂移基于数千个样本。
- 📊 统计框架：基于 UK AISI 的 Inspect，遵循 Anthropic 的《Adding Error Bars to Evals》，使用配对每题差异和聚类标准误。
- 🧩 面板筛选：从 2,336 道 GPQA Diamond、MMLU-Pro、竞赛数学和 AIME 题中筛出 78 道模型有时对、有时错的题。
- 🧮 检测能力：每日运行整个面板可检测约 7.5 个百分点/10 天窗口的准确率变化，成本约为每周计划额度的 3.6%。
- 🧪 验证结果：正对照显示低/中 effort 会显著减少输出 token 并降低准确率；A/A 检查验证误差棒可靠。
- 🚫 已知限制：无法区分 Opus 5 与 Opus 5.5 的同族模型替换；问题中有 8 个答案键疑似错误、30 个模糊题，但未删除，改用预注册敏感性分析。
- 🛡️ 安全分类器：有时会以 Opus 5 回答或拒绝生物/数学题；这些样本被拒绝并计数，相关题目排除。
- 📈 主要指标：配对每题分数差异对比基线；次要指标是每样本输出 token 数，可能先于准确率显示“思考变少”。
- 🔒 预注册规则：数据收集前公开 `PREREGISTRATION.md`；判定变化需两个连续 10 天窗口 99% 区间排除零、效应至少 3 点、且控制组不移动。
- 🧠 双组设计：主面板测量 Opus 5.5；对照组用 `claude-opus-5` 每天跑 GPQA 题，用于排除 harness 或平台变化。
- 🛠️ 使用流程：需要 Python 3.11+、`uv` 和已登录的 Claude Code；依次运行校准、设计、验证、提交并启动每日收集，支持 Linux/macOS/Windows。
- 📌 测量对象：Opus 5.5 通过 Claude Code 订阅服务，而非原始 API；发布周基线只是参考点，不假设降级机制。
- 🤝 贡献与披露：任务须可精确评分、位于 30–70% 区间且足够便宜；变更会创建新版本；PR 需披露 LLM 贡献，冻结面板题目保持私有。
- 📜 许可与引用：MIT 许可；独立项目，与 Anthropic 无关联；README 提供 BibTeX 引用格式。

---

### [](https://github.com/lemma-work/lemma-platform?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-765-october-1-2026)

**原文标题**: [GitHub - lemma-work/lemma-platform: The open-source workspace where humans and AI agents work as one team. · GitHub](https://github.com/lemma-work/lemma-platform?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-765-october-1-2026)

Lemma 是面向团队的开源多人、自我改进 AI harness：把模型周围的工具、记忆、状态、循环和边界统一到共享 pod 中，让人和 AI agent 在同一套记录与权限下协作，并可由现有编码代理直接构建、导入和验证。

- 🧩 核心定位：状态共享且带权限，多人和多 agent 可处理同一批记录，并在会话之间按计划、webhook、表事件持续运行。
- 🛠️ 构建方式：在 Claude Code、Codex、Cursor、OpenCode 或 Antigravity 中描述任务，它会生成应用、表、agents、workflows、权限文件，再通过同一 CLI 导入并验证。
- 🌐 使用入口：团队可通过 URL、Slack、Teams、Telegram、WhatsApp 或 email 使用；所有入口读写同一记录、工作流和权限。
- ☁️ 部署与模型：开源且可跑在笔记本、服务器或 Lemma Cloud；模型可用现有 Claude Code/Codex 订阅、Lemma 托管模型，或 OpenAI/Anthropic 兼容提供商。
- 🚀 快速开始：云端用 uv tool install lemma-terminal，选择 lemma-cloud，登录、安装 skills、创建带 starter 的 pod，再进入 lemma chat。
- 💻 本地安装：下载 Lemma Desktop 选 Local 并安装本地服务，再用 install.sh --cli-only 注册 local server；务必用 uv，不要用 pip，因为需要 Python 3.14，pip 可能静默安装旧版 0.6.2。
- 🧭 故障排查：local server 未找到说明 Desktop 本地设置未完成；provider 报错需配置 AI Providers；lemma doctor 可诊断版本偏差和重复安装。
- 🔐 权限示例：Priya 为 Owner 可批准任意退款；Marco 为 Member 只能处理自己的 jobs 且退款需路由；Classifier agent 仅只读 tickets。
- 🧱 Pod 原语：Tables、Files、Agents、Workflows、Functions、Permissions、Approvals、Connectors、Apps、Surfaces。
- 📚 关键原语：Files 是带权限和全文搜索的 Markdown 记忆；Workflows 可混合 agents、函数、决策、循环、等待和人工审批；Approvals 可暂停并路由给人后恢复。
- 🤖 Agent 与函数：Agents 是有角色、工具授权和表/文件/连接器访问范围的 LLM worker；Functions 是确定性代码，供 agent 作为工具调用。
- 📥 表面支持：Slack、Microsoft Teams、Telegram、WhatsApp、email 均支持 webhook 入口、身份解析和 agent 发起动作；Telegram long-polling 与 Slack Socket Mode 支持本地连接。
- ✉️ 邮件与个人助理：每个 pod agent 有独立地址，任何邮件客户端可写；Gmail/Outlook 是 connector 不是 surface；单人也可用 WhatsApp 作为前门、tables 作为记忆。
- 🧑💻 技能与 CLI：用 lemma skills install 把 Lemma 技能装入已有编码代理；CLI 可执行 pod init/import、apps deploy、table/record/agent/workflow/chat 等操作。
- 🔄 Agent Host：可把本地 Claude Code、Codex、OpenCode、Cursor 连接到 pod，从持久队列取任务、流式回传、在审批门暂停；多个 agent 共享状态、任务队列和运行历史。
- 🧰 SDK：提供 Python 和 TypeScript SDK，含 25+ React hooks，可让外部前端直接由 pod 提供表、agents、workflows 和权限。
- 📦 示例 Pod：Roundtable、Frontdesk、Panini、Smart Inbox、Sidekick、Lemma Design、Nachiketa、Drop、Meal、Lemma GTM，可在 lemma.work/templates 浏览安装。
- 📤 Pod 即文件：可 export/import/分享/重混；同一编码代理能修改、验证并重新导入。
- 🖥️ 桌面与服务器：macOS 14+ Apple silicon 提供签名在线包；无公开 Windows 安装器，Windows 11 23H2+ 构建仅作为 GitHub Actions 工作流产物；团队可用 Docker Compose 部署。
- 🔌 模型提供商：可在 Local Control Center → AI Providers 或 lemma-stack 配置；无 API key 可用 Ollama/LM Studio；服务端 agent 需 provider 验证后才可用。
- 🗂️ 仓库与开发：backend、frontend、harness 为 AGPLv3；stack、CLI、Python/TS SDK、skills、pod-bundle 为 Apache-2.0；开发命令包括 make init、make dev、make dev-public、make logs、make stop。
- ⚖️ 许可与数据：核心 AGPLv3、客户端工具 Apache-2.0，可获取商业许可；Lemma 名称和 logo 是商标；仓库约 475 stars、64 forks、13 个 PR、0 个 issue。

---

### [](https://github.com/connor-makowski/type_enforced?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-765-october-1-2026)

**原文标题**: [GitHub - connor-makowski/type_enforced: Fast runtime type enforcement for Python 3.11+ type annotations. Zero dependencies and uncompromising performance. · GitHub](https://github.com/connor-makowski/type_enforced?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-765-october-1-2026)

type_enforced 是 connor-makowski 开发的 Python 3.11+ 运行时类型强制执行库，目标是在运行时验证类型注解，兼顾完整验证与高性能采样验证，且零运行时依赖。
- 📦 公开 GitHub 项目，MIT 许可，主分支约 325 次提交，约 67 stars、6 forks。
- 🚀 核心定位：弥补 mypy/pyright 仅静态检查、运行时无保护的问题；相比 Pydantic 更轻更快，相比 Beartype 默认不牺牲完整性。
- 🧩 提供 Enforcer（完整验证）、FastEnforcer（O(1) 采样验证）、ModuleEnforcer/FastModuleEnforcer（模块级验证）。
- ⚡ 性能：FastEnforcer 采样验证最高约比 Beartype 快 15 倍；Enforcer 完整验证在标量上最高约比 Pydantic 快 40 倍，在较大数据结构上约快 20 倍。
- 📥 安装：pip install type_enforced 或 uv add type_enforced。
- 🧱 要求 Python 3.11+，零运行时依赖；可选 nanobind C++ 加速，无编译器时自动回退纯 Python，也可强制纯 Python。
- 🛠️ 用法：用 @type_enforced.Enforcer 或 @FastEnforcer 装饰函数、方法、类、dataclass；验证位置参数、关键字参数、默认值、返回值及 *args/**kwargs。
- 🔍 支持类型：标准内置类型、| 联合、嵌套泛型、Literal、Callable、Sized、Any、TypedDict、NewType、Self、NoReturn/Never、TypeGuard/TypeIs、TypeVar、ParamSpec、TypeVarTuple、PEP 695 等。
- 🧬 支持自定义类与子类继承；type[Animal] 用于验证类对象本身，而非实例。
- ✅ 值约束：Constraint 支持 gt、lt、ge、le、eq、ne、pattern、includes、excludes；GenericConstraint 支持自定义谓词。
- ⚙️ 关键配置：enabled、strict、clean_traceback、iterable_sample_pct、only_typed、submodules。
- 📊 采样模式：first、last、bookend、bookend_plus、log、0（随机 1 个）、百分比、100（全部）；Fast* 默认 first，Enforcer 默认 100。
- 🧼 clean_traceback 默认清理内部栈帧，便于定位用户代码；但 REPL/IPython/Jupyter 仍显示完整 traceback。
- 🏭 生产实践：多线程服务、Web 框架或集中错误处理场景建议设置 clean_traceback=False。
- 🚫 已知限制：暂不支持 Sized[int] 这类泛型参数化，需使用无内部类型参数的 Sized。
- 🧪 开发贡献：使用 uv 管理依赖，pytest 测试，nox 覆盖 Python 3.11–3.14（C++ 与纯 Python），并提供基准与格式化脚本。
- 📚 学术引用：JOSS 论文 DOI 10.21105/joss.08832；作者 Connor Makowski，2026。
- ⚖️ 许可证：MIT License。

---

### [](https://github.com/NandhaKishorM/laya?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-765-october-1-2026)

**原文标题**: [GitHub - NandhaKishorM/laya: Non-autoregressive System 1 decision engine. Typed choice, score and yes/no decisions over any text in a single forward pass, in 100+ languages, with a router that picks the right checkpoint per request. · GitHub](https://github.com/NandhaKishorM/laya?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-765-october-1-2026)

Laya 是一个多语言、非自回归的 System 1 决策引擎，能在单次前向传播中于 100 多种语言上给出类型化决策（33 毫秒），采用 RLCD 强化学习训练，并配有路由器为每个请求选择正确的检查点。

- ⚡ **核心能力**：在单次前向传播中对任意文本（文本、邮件、工单、JSON 文档）进行类型化决策，单问题约 33 毫秒，批处理时每问题 7.2 毫秒，无文本生成、无需解析、不会产生幻觉
- 🗂️ **三种检查点**：`laya`（英语，ModernBERT-large，421M 参数）、`laya-multilingual`（100+ 语言，mmBERT-base，322M 参数，速度翻倍）、`laya-typed-decisions`（类型化决策工作流）
- 🔀 **路由器机制**：自动检测文字与语言（<0.5 毫秒），按请求分派到最优检查点；支持 `preload=True` 预加载、`max_loaded` 控制内存驻留、`lang_guess` 覆盖检测
- 📦 **安装与部署**：`pip install laya`，需 Python 3.10+；支持可选组件（serve、mcp、langchain、llamaindex、crewai、onnx、fast）；提供 Docker、Nix/NixOS、HTTP 服务端、MCP 服务端
- 🎯 **决策原语**：`choice`（单选标签）、`score`（序数级别）、`noul`（是/否概率 P(true)）；每个答案均带校准置信度与概率分布
- 📈 **微调效果**：在类型化决策基准（2,000 项决策）上，微调后检查点准确率 0.766，远高于基础英语检查点的 0.362；微调是提升价值的关键，基础模型零样本接近随机
- 🧮 **评分与校准**：概率经严格适当评分规则（RLCD）训练，置信度具有统计意义；发货检查点存在过度自信，需在自有数据上重新拟合温度；平均 ECE 可从 0.466 降至 0.081
- 🛡️ **安全与弃权**：支持 `min_confidence` 弃权阈值，返回 `abstention` 状态（passed/abstained/unevaluated），便于构建自动路由与人工升级策略
- 🔗 **框架集成**：LangChain、LangGraph、LlamaIndex、CrewAI 官方集成；提供 `LayaRouter`、`LayaGuardrail`、`LayaDecision` 等组件；TypeScript SDK（laya-ts、laya-client）支持浏览器与 Node.js
- 📄 **长文档支持**：`predict_long` 通过重叠窗口扫描全文并聚合结果，`laya-multilingual` 可读取最多 8,192 个 token，避免静默截断
- ⚙️ **性能优化**：批处理 `predict_batch`、`sort_by_length` 按长度分组减少填充、TileLang GPU 快速路径、`warmup()` 预热、ONNX 导出，T4 上吞吐可达 103–332 问题/秒
- 🏆 **对比 Jev**：单问题延迟约快 7.8 倍，ECE 约优 3 倍，权重开源（Apache 2.0），自托管成本为零；但在 >20 个选项的高基数标签场景下 Jev 更优
- 🧪 **评估框架**：`laya-evals` 纯 Python 实现，可对接 CI 按切片质量门禁评分，支持基线对比与 ONNX 路径
- 🌐 **社区工具**：omp-laya-judge、laya-adk-toolkit（Google ADK）、laya-Ascend（华为 NPU）、laya-apple（MLX + 神经引擎）、stuntd 等
- ⚠️ **已知局限**：基础检查点零样本接近随机；`choice` 避免使用布尔词标签；否定语义不安全；`score` 为最弱原语；英语检查点在非拉丁文字上会崩溃（高置信度却错误）；`noul` 易跟随标签而非状态
- 📜 **许可与背景**：Apache 2.0，由 Convai Innovations 开发；仓库获 29.9k 星标、2.6k 分支，Hugging Face 模型为 `convaiinnovations/laya`

---

### [](https://github.com/TencentCloud/Octop?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-765-october-1-2026)

**原文标题**: [GitHub - TencentCloud/Octop: A smarter, self-hosted AI assistant — multi-user, multi-agent. · GitHub](https://github.com/TencentCloud/Octop?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-765-october-1-2026)

Octop 是腾讯云开源的自托管多用户、多智能体 AI 助手平台，单进程即可提供 Web 仪表盘、CLI、IM 渠道与定时任务，所有对话、工作区和凭证默认保存在本地 `~/.octop/`，强调隐私、可扩展与专家协作。

- 🚀 项目定位：开源、本地优先、自托管 AI 助手；GitHub 仓库为 TencentCloud/Octop，MIT 许可，约 6.2k stars、785 forks。
- 👥 多用户与专家：支持管理员与多用户隔离，每位用户可拥有多个专家，每个专家有独立工作区、模型、渠道与 cron。
- 🤝 专家共享：可发布专家、共享技能与子代理池，让团队复用成熟配置。
- 🎭 人格与团队：内置 16 种 MBTI 人格模板与测验；AgentTeams（Beta）可由协调者调度多个专家完成多步任务。
- 🔒 安全能力：JWT 多用户隔离、工具审批、Shell 命令护栏、PII 脱敏，数据尽量留在本地。
- 🔌 连接器生态：支持腾讯套件、OAuth、MCP 网关，并可接入飞书、钉钉、QQ、微信、Telegram、Discord、企业微信等 IM。
- 💾 工作区后端：专家文件可存本地磁盘、Docker 沙箱、PostgreSQL、COS/S3 等，与控制面数据库分离。
- 🧠 记忆与知识库：由 Octop Memory 提供可迁移记忆；知识库支持 RAG、文档语料管理与部署内共享。
- 🧩 插件系统：支持第三方插件安装与管理，内置插件可按需启用。
- ↔️ ACP 双向集成：既可作为 ACP 服务供 IDE/终端使用，也可将编码任务委派给 OpenCode、Claude Code、Codex 等外部代理。
- 💻 交互增强：提供终端 AI+、浏览器 AI+、远程桌面，用于命令执行、网页自动化、截图与 GUI 操作。
- 🖥️ 客户端形态：包含 Web 仪表盘、Windows/macOS/Linux 桌面客户端、FnOS NAS 包，以及 HTTP/SSE/WebSocket API。
- 🏠 自托管部署：`octop init` 初始化，`octop run` 启动；默认 SQLite，可选 PostgreSQL；Docker Compose 适合生产。
- 🧱 技术栈：Python 3.12+、FastAPI、uvicorn、Octop Harness/Gateway/Memory/Browser、React 18 + TypeScript + Vite + Ant Design、APScheduler。
- ⚙️ 快速开始：支持 macOS/Linux 一行安装、Windows PowerShell/cmd 安装、PyPI 安装与 Docker 部署；默认访问 `http://127.0.0.1:8088`。
- 📖 CLI 与配置：提供 `octop models`、`channel`、`cron`、`skills`、`plugin`、`backup`、`update`、`memory` 等命令，配置集中在 `~/.octop/`。
- 🗺️ 路线图：已交付共享资源池、专家共享、PC 客户端；进行中包括 AgentTeams Beta、移动客户端；计划包括浏览器/终端增强、自我进化、托管代理、插件市场等。
- 🤝 社区与贡献：欢迎 Fork、功能分支与 PR；提供 Discord、企业微信社群；贡献指南、安全策略与更新日志齐全。

---

### [](https://www.meetup.com/pydata-london-meetup/events/316770322/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-765-october-1-2026)

**原文标题**: [PyData London - 110th Meetup, Tue, Oct 6, 2026, 6:30 PM   | Meetup](https://www.meetup.com/pydata-london-meetup/events/316770322/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-765-october-1-2026)

本次 PyData London 第110次聚会将于10月6日（周二）18:30–21:00 BST 在伦敦大学伯贝克学院举行，聚焦生成式AI代理应用的生产化、缺失数据下的黑洞引力波推断以及Python提速等主题，并提供免费餐饮和会后交流。

- 📅 时间地点：10月6日周二18:30–21:00 BST，Birkbeck, University of London，Malet St, London WC1E 7HX，房间 MAL B33。
- 🏢 新场地提醒：活动换到伯贝克大学新场地；入场需携带有效带照片证件，18:30开门，建议早到签到。
- 🗣️ 组织者：由 Alexandra R. 和另外4人主办，Hugh E. 是 Super Organizer。
- 🤝 社区规范：活动遵循 NumFOCUS 行为准则，参会者需提前了解；有问题可联系组织者。
- ✅ RSVP：状态为“You're going”即可入场，无需出示确认；若不能参加请尽快取消 RSVP。
- 🍕 餐饮赞助：Man Group 提供免费食物和饮料；赞助方包括 NumFOCUS、Man Group & ArcticDB。
- 🤖 主演讲1：Sultan Al Awar 与 Ksenia Shishkanova 讲“From PoC to Production: Building Scalable Agentic Applications”，讨论从 PoC 到生产级代理系统的挑战与 AgentOps 实践。
- 🧪 主演讲1要点：涵盖工具执行、评估基线、提示回归、治理、可观测性、版本管理、供应商/模型锁定，以及 MLflow、LLM-as-a-Judge、黄金数据集、追踪监控、生产检查清单和参考架构。
- 🌌 主演讲2：Kavit Tolia 讲“Listening to black holes with missing data”，介绍用模拟推断和神经网络后验估计处理带缺失数据的引力波信号，并与传统 MCMC 比较。
- 📚 主演讲2启示：输入表示与模型同样重要；缺失数据的影响取决于缺失位置而非数量；后验接近真值仍可能错误；使用 PyCBC、sbi、emcee，无需物理背景。
- ⚡ 闪电演讲：Richard Hickling 分享“Making Python Faster”。
- 🍻 会后安排：19:00 开始演讲，21:00 后到附近酒吧继续交流（地点待定）；活动容量减少，请及时释放名额。
- 🏷️ 相关主题：大数据、商业智能、数据管理、Python、开源等。

---

### [](https://www.meetup.com/pydata-nl/events/316593765/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-765-october-1-2026)

**原文标题**: [Data from the Physical World, Thu, Oct 8, 2026, 6:00 PM   | Meetup](https://www.meetup.com/pydata-nl/events/316593765/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-765-october-1-2026)

这是 PyData Amsterdam 的下一场线下聚会 “Data from the Physical World”，聚焦真实物理世界中的数据与 AI 难题，联合 Monumental 和 Source.ag，带来温室收成预测与建筑工地机器人两场讲座，并安排晚餐、饮品和社交交流。活动需转到 Luma 订阅并报名。

- 🏷️ 活动名称：Data from the Physical World，由 PyData Amsterdam 主办，主持人 sarthak a.
- 📅 时间：10 月 8 日周四 18:00–21:00 CEST；18:00–18:30 签到与欢迎。
- 📍 地点：荷兰阿姆斯特丹 Plantage Middenlaan 62, 1018 DH。
- 🔄 重要变更：PyData Amsterdam 正在迁移到 Luma，请先在 Luma 订阅并报名：https://luma.com/pydataamsterdam 与 https://luma.com/6fuljd88。
- 🌱 讲座一 18:30–19:00：Sebastiaan Vermeulen（Source.ag 数据科学家）讲 “Data problems in the greenhouse”，解析温室收成预测为何困难：每季每作物约 40 个数据点、人工记录杂乱、普通 ML 会违背植物生长规律；Source 采用生物机理模型与机器学习混合方案。
- 🤖 讲座二 19:00–19:30：Josefine Quack（Monumental 前向部署机器人工程师）讲 “Robot Whispering on the Construction Site”，介绍建筑工地恶劣环境下的机器人系统、超 100 台机器人跨站点/国家同时运行、实时部署新功能与远程调试。
- 🍽️ 19:30–21:00：晚餐、饮料与交流；提供酒精和非酒精饮品及晚餐。
- 🎯 适合人群：数据科学家、软件工程师、Python 用户，以及任何对物理世界数据应用感兴趣的人。
- 🤝 赞助商：Adyen、The NextGen、Heineken、Rabobank，提供餐饮、饮品和场地等支持。
- 🏢 相关团队：Monumental 开发自主建筑机器人，已参与建造 100+ 房屋；Source.ag 为温室种植者提供 AI 决策，帮助用更少资源生产更多食物。

---

### [](https://www.meetup.com/charlottesvilledatascience/events/316599352/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-765-october-1-2026)

**原文标题**: [Accuracy Isn’t Everything: Good Models are Lurking Everywhere, Thu, Oct 8, 2026, 6:00 PM   | Meetup](https://www.meetup.com/charlottesvilledatascience/events/316599352/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-765-october-1-2026)

Charlottesville Data Science（PyData Group）将于 10 月 8 日周四 18:00–20:00 EDT 在 UVA 数据科学学院举办线下讲座“准确率不是一切：好模型无处不在”，由 Purdue 数学博士 Evzenie Coupkova 主讲，NumFOCUS 赞助，活动需通过 Luma RSVP。讲座不局限于寻找单一“最佳”模型，而是探索可能的模型全景，讨论机器学习模型“好”的含义，以及预测准确率与泛化、可解释性等特性之间的权衡。

- 📅 活动信息：10 月 8 日周四 18:00–20:00 EDT，地点为 School of Data Science，1919 Ivy Rd, Charlottesville, VA。
- 👥 主办与主持：Charlottesville Data Science（PyData Group），由 Patrick H. 等主持。
- 🎤 主讲人：Evzenie Coupkova，Purdue 数学博士，专长统计学习理论、机器学习与高维数据分析。
- 🎯 核心观点：数据科学家常只关注最高准确率模型，但应审视所有可能模型，理解“好模型”是否大量存在及其与数据集的关系。
- 📐 第一部分内容：从高斯混合上的线性模型入手，观察高/低准确率模型在参数空间中的位置，以及类别均值距离变化时“好模型”比例如何变化。
- 🧠 第二部分内容：研究随机初始化神经网络中“好”分类器的比例，并用 Sanjeev Arora 的矩阵方法衡量数据集复杂度，展示真实数据实验结果。
- ⚖️ 一般原则：若“好模型”很丰富，就可在不牺牲太多准确率的情况下提升泛化，并选择更可解释、稀疏或满足专家约束的模型，适合医疗、司法等高风险场景。
- 🔗 报名与赞助：活动日历已迁移至 Luma，需前往 Luma RSVP 并可选订阅；赞助方 NumFOCUS 致力于推动开放代码促进科学。
- 🗂️ 相关主题：深度学习、机器学习、机器学习可解释性、数据科学、预测分析。

---

