### [](https://refactoringenglish.com/excerpts/write-an-effective-design-doc/)

**原文标题**: [How to Write an Effective Software Design Document · Refactoring English](https://refactoringenglish.com/excerpts/write-an-effective-design-doc/)

Michael Lynch 结合在 Google、微软和自创公司的经验说明：优秀软件设计文档能在写代码前厘清关键决策、协调团队、避免昂贵返工；文章覆盖何时写、投入多少、应含哪些部分及如何评审。
- 🧠 设计文档的核心价值：迫使团队在错误实现前思考重要决策，并让队友与合作团队提前反馈。
- ✅ 适合写设计文档的信号：多人协作、超过 3 个月全职开发、生产运行多年、跨团队、需求模糊，或存在安全/法律等灾难风险；命中两项以上几乎都值得写。
- ⚖️ 投入没有统一标准：可由一页到 50 页，取决于目标、风险、截止日期与文化；有时正确投入甚至是零。
- 🎯 只记录“做错代价高”的决定：语言、存储等难改选择要写；像“加载更多”按钮这种易改细节不必写，更不必为它争论。
- 🧱 常见组件包括：标题、元数据、目标、背景、相关文档、目标/非目标、场景、图表、术语表、约束、SLO、监控告警、时间线、接口、依赖/基础设施、安全、隐私、法律、日志、开放/已解决问题和备选方案。
- 🏷️ 标题应简短、独特、易记；元数据写作者、创建日期、权威 URL、批准人和批准时间。
- 📝 目标用一句话说明项目目的；背景解释动机、问题、历史尝试，并确保读者无需外部解释也能理解第一页。
- 🎯 目标应描述用户、团队或公司层面的影响，而非内部实现；非目标明确划出范围之外。
- 🎬 场景用简短故事展示完成后的系统如何被使用；图表展示数据流、组件关系、依赖、下游和协议，并用易修改工具制作。
- 📚 术语表定义内部工具或不熟悉的术语；约束说明预算、客户、基础设施或依赖带来的限制。
- 📈 SLO 提供可衡量指标，如可用性、延迟、规模；监控/告警说明如何发现服务宕机、性能骤降和其他异常。
- 🗓️ 时间线拆分为里程碑，优先产出对利益相关者有价值的工件，例如先用假数据展示 UI。
- 🔌 接口部分描述 UI 草图、API/CLI 语义或文件格式；依赖/基础设施部分说明语言、运行环境、持久化存储及长期维护成本。
- 🔐 安全部分考虑威胁、攻击面、信任边界；隐私部分说明敏感数据、保留期、访问权限和保护措施。
- ⚖️ 法律部分关注金融/医疗等合规、合同限制和开源许可证；日志部分说明关键事件、级别、存储、保留、访问和敏感数据过滤。
- ❓ 开放问题记录未解决的设计缺陷、缺失信息或方案纠结，并写清问题、选项和下一步；解决后移入已解决问题并保留讨论。
- 🧪 备选方案简要说明强有力但被拒绝的选项及原因，主动回答“为什么不做 X”。
- 👥 完成文档后应推动评审，向团队和合作方收集能推进项目的有效反馈，而不是陷入争论。
- 📄 文章附有一个从零编写的真实示例设计文档（Little Moments），用于展示文中原则。

---

### [Context.dev：面向 AI 代理与 LLM 的网页](https://www.context.dev/?utm_source=bonobopress&utm_campaign=bonobopress&utm_term=bonobopress&ref=bonobopress&dub_id=6HtPyXr6Vb2FMLWY)

**原文标题**: [Context.dev: Web Scraping API for AI Agents & LLMs](https://www.context.dev/?utm_source=bonobopress&utm_campaign=bonobopress&utm_term=bonobopress&ref=bonobopress&dub_id=6HtPyXr6Vb2FMLWY)

Context.dev 是面向 AI 智能体与产品的网页数据基础设施，通过统一 API 提供网页抓取、爬取、结构化提取、品牌情报、Logo、图片、截图和分类等能力，帮助团队实时获取 Web 上下文、更新 RAG 知识、补全公司资料并识别交易信息。免费层含每月 1,000 API credits 和 10K Logo Link 请求，无需信用卡，并提供 TypeScript、Python、Ruby、Go、PHP SDK 及 AI agent 自动接入方案。

- 🕸️ 核心能力：Web Scraping API，支持 markdown、HTML、sitemap、搜索、整站爬取、图片与截图提取。
- 🧩 Extract：用 JSON Schema 从任意网站提取结构化数据，示例通过 TypeScript/Zod 提取定价层级。
- 🏢 Brand Data：获取公司 logo、颜色、字体、风格指南、描述、社交账号和地址等品牌资料。
- 🖼️ Logo Link：通过 CDN 用一行 `<img>` 标签嵌入任意公司 logo，无需 API 调用且不消耗 API credits。
- 🔎 其他 API：Pull Images、Classification（NAICS/SIC/交易识别）、产品提取、截图、Styleguide 等。
- 🤖 AI & agents：为 LLM 提供实时 Web Context，支撑生成式 AI、RAG 新鲜内容与网站变更监控。
- 🚀 产品场景：自动填充 onboarding、程序化主题、自动品牌套件、公司资料丰富、交易噪音解析。
- 📈 前后对比：从内部维护爬虫、多供应商拼接、数据冻结，转为按需实时拉取、统一 API、更快上线。
- 🧪 客户案例：Mintlify、SiteGPT、Sourcely、daily.dev、Propane、Architect、DocsBot、OpenTag、Squad、Tinfoil 等快速集成。
- 💬 用户反馈：10 分钟内完成集成、自服务 API key、提升试用激活率、支持零数据留存。
- 🛠️ 接入方式：控制台自助，或让 AI agent 根据 `auth.md` 和 `agent-quickstart` 自动注册并集成。
- 💰 定价：Developer $25/月、Pro $149/月、Scale $499/月；Enterprise 支持 >2M credits/月、自定义限速、SSO、SLA 等。
- 🎁 免费层：每月 1,000 API credits + 10K 一次性 Logo Link 请求，无需信用卡。
- 🔢 Credits：简单抓取 1 credit；品牌检索、风格指南、结构化提取、行业识别等 10 credits；Logo Link 单独计量。
- ⏱️ 限速：Free 30 次/分钟（工作邮箱）或 10 次/分钟（个人邮箱），Developer 60，Pro 300，Scale 700。
- ✅ 计费规则：失败请求不计费；付费计划有超额计费；年付省两个月；初创/非营利可申请 30% 折扣。
- 🧾 数据与支持：品牌数据默认缓存约 90 天；冷启动可能较慢，可用 Prefetch 或批处理；支持子域名；提供多语言 SDK。
- 🏁 总结：Context.dev 定位为 AI 产品与智能体的统一 Web 数据 API，可替代多供应商并加速功能交付。

---

### [](https://planetscale.com/blog/debugging-live-database-connections)

**原文标题**: [How one connection kills a database â PlanetScale](https://planetscale.com/blog/debugging-live-database-connections)

概述：文章用一个可复现的故障链说明，单个未关闭的数据库连接如何导致 PostgreSQL/MySQL 卡死：未提交事务持有锁，阻塞迁移，迁移又阻塞后续查询，最终造成停机；PlanetScale 新增 Dashboard 与 CLI 连接管理能力，可查看并终止阻塞连接，并建议设置事务空闲超时。

- 🎯 以 GitHub 面试题引出问题：数据库卡死常源于一个未提交事务，而不是复杂死锁。
- 🔒 MySQL 场景中，schema 变更需要排他锁，却被一个未提交会话阻塞，后续查询全部排队；Postgres 也能轻易复现。
- 🧪 复现方式：连接 A 执行 `BEGIN` 和 `SELECT` 后应用抛异常，事务未 `COMMIT`/`ROLLBACK`，连接保持打开。
- ⛔ 连接 B 执行 `ALTER TABLE` 需要 `ACCESS EXCLUSIVE` 锁，被连接 A 的 `ACCESS SHARE` 锁阻塞；连接 C、D、E 又排在 B 后面。
- 🚨 没有死锁，也不会自动超时，整个阻塞链会一直堆积，直到有人终止最顶部的连接。
- ⚠️ 默认 `idle_in_transaction_session_timeout` 被禁用会加剧问题；设置该值可让 Postgres 自动超时未关闭事务。
- 🛠️ PlanetScale 新增 Postgres/MySQL 连接查看与终止功能，即使连接耗尽，也能通过保留的管理连接排障。
- 📊 Dashboard 的 Connections 标签可查看 Process ID、State、Duration、Blocked Queries 等，便于定位阻塞者。
- 🔪 终止选项包括：Cancel query、Terminate transaction、Terminate connection；Vitess 提供取消查询或终止连接。
- 💻 CLI 可用 `pscale branch connections top <database> <branch>` 查看实时连接；用 `show --format json` 获取 JSON 和终止所需 ID。
- ✅ 结论：设置事务空闲超时，并迁移到 PlanetScale，可更轻松地管理连接、避免停机并快速解卡。

---

### [](https://jestoph.com/2026/09/04/jane-street-challenge.html)

**原文标题**: [On solving the Jane Street Reverse Engineering Challenge | jestoph’s tech blog](https://jestoph.com/2026/09/04/jane-street-challenge.html)

overview summary
作者用一个月时间解出 Jane Street 的 ASIC 逆向工程挑战：从 GDS/VCD 文件出发，识别 sky130 标准单元，重建电路，自制模拟器并用 z3 约束求解器反向求解，最终得到答案 (* TWO STARS *)。

- 🧩 挑战要求逆向一枚 ASIC，理解其功能并找出隐藏答案；分为热身题和正式题两阶段。
- 📁 作者用 Python 的 gdstk 读取 GDS，发现 27 个热身单元、sky130_fd_sc_hd__ 逻辑单元，并从 VCD 中提取出“TRY AGAIN”。
- 🛠️ 他一度自制电路模拟器、HDL 解析器、测试框架和 GDS 查看器，后来意识到偏离主线，转而使用现成工具。
- 📚 通过 sky130 文档和 SVG 标签，他把几何与引脚重叠关系映射成电路 I/O，并构建连接图。
- 🔗 热身题包含移位寄存器、加法器和 comparator496；需让输入之和为 496，最终成功模拟。
- ⚙️ 正式题有约 81 类、近 10k 个组件；他手动实现约 40 个新组件，并大幅优化电路提取速度。
- 🐞 他发现并报告了 Jane Street 电路中的一个疑似引脚连接 bug，获官方确认且不影响结果。
- 🔄 面对 120 位输入，他采用反向求解：从第 120 步期望输出反推前一步约束。
- 🧮 先用电子表格和手写 Verilog 验证思路，后用 z3 约束求解器处理数千条约束，确定约 24 根线需同时为高。
- 🏁 最终解出正确输入，电路输出 (* TWO STARS *)，并收到 Jane Street 的确认。
- 📊 其他输出包括：错误答案“TRY AGAIN”、全 0“EMPTY SKY”、全 1“BIG BANG”。
- 🚀 作者享受这次挑战，期待 Jane Street 未来新挑战，并欢迎交流项目或在悉尼约咖啡。

---

### [](https://seldo.com/posts/we-are-all-product-engineers-now/)

**原文标题**: [We are all Product Engineers now | Seldo.com](https://seldo.com/posts/we-are-all-product-engineers-now/)

AI 与自动化正让写代码的边际成本趋近于零，软件行业的重心将从“程序员”转向“产品工程师”：核心工作变成发现客户真正想要什么、精确定义“好”、设计愉悦体验，而 agents 负责大部分实现与运维。作者预测未来十年软件需求近乎无限、从业者可能更多，但几乎没人再以敲代码为主要工作；转型期会伴随初级岗位消失、培训断层和工匠式编程职业的衰落。

- 🤖 写代码成本已崩塌，AI agents 预计将吞噬整个软件开发生命周期：编码、审查、测试、修 bug、部署、监控与扩展。
- 📈 软件需求近乎无限：大量组织和小企业仍依赖糟糕软件、表格和群聊，说明好软件供给远未饱和。
- 🧩 成本拆解：编码已自动化；代码审查与维护很快被自动化；部署与扩展是下一波；最难替代的是决定“做什么”、定义“好”和做出愉悦体验。
- 🍞 产品发现无法机械完成：需求藏在具体客户脑中且不可转移，面包店和汽车零件厂需要不同软件，产品决策没有规模经济。
- 👶 初级开发者受冲击最大：他们原本负责按明确 ticket 写代码，而这正是 agents 最先擅长的；22—25 岁 AI 暴露岗位就业差距达 19%，大厂入门招聘比 2019 年降 65%。
- 🧪 Agent 能力快速提升：真实 bug 修复 benchmark 两年从约 50% 到约 95%，Claude Code 的 PR 84% 最终被合并，Google Big Sleep 发现 SQLite 等漏洞。
- ⚠️ 审查危机：GitHub PR 与提交激增，很多 agent PR 无人类审查，58% 的 agent PR 只由另一个 agent 审查；curl 因低质量报告关闭漏洞赏金。
- 🛠 运维与扩展尚未自动化，数据稀少，但作者认为逻辑上会是下一步。
- 🧑‍🍳 剩余核心是“产品感”：理解客户、把模糊愿望变成精确规格、验证做出来的东西是否真是对方想要的。
- 🏗 历史角色回归：系统分析师、产品经理和工程师可能合并为“产品工程师”；forward deployed engineer 等岗位九个月增长约 800%，平均总包约 24 万美元，高级超 60 万美元。
- 🎯 新岗位职责：与客户界定问题、理解业务、在既有系统中写生产代码、持续迭代；写代码只是最小部分。
- 🎓 培训管道缺失：Google APM 每年约 50 人/1.2 万申请者，大学和训练营不教需求分析与品味；市场会调节但太慢。
- 💔 编程手艺作为付费职业基本终结，是真实损失；热爱“问题变清晰”时刻的人可能适应，craft 会像木工一样作为爱好或利基存活。
- 🔮 十年预测：更多软件、更多人做软件，但几乎没人打字；我们都是产品工程师，不论是否喜欢。

---

### [](https://lalitm.com/post/git-history/)

**原文标题**: [The git history command deserves more attention - Lalit Maganti](https://lalitm.com/post/git-history/)

overview summary
- 🧭 文章主张 `git history` 这一实验性命令值得更多关注：它内置在 Git 中，无需额外安装，就能带来部分 `jj` 式工作流优势。
- 🧩 它包含三个子命令：`fixup`、`reword`、`split`，随 Git 2.54 和 2.55 版本加入。
- 🛠️ `git history fixup` 会把已暂存的修改折入旧提交，并自动变基所有包含该提交的本地分支；它比 `git rebase --update-refs` 更进一步，但不支持 merge commit。
- ✏️ `git history reword` 用于修改旧提交信息，并自动重建其上的提交和分支；它只改提交图，不触碰索引或工作区。
- ✂️ `git history split` 可交互地把一个提交拆成两个，类似 `git add -p`，但无需复杂的 `git rebase` 操作。
- 🔒 三个命令的共同关键特性是原子性：遇到可能产生冲突的操作会拒绝执行，避免让工作树处于半损坏状态。
- ⚖️ 它仍弱于 `jj`：`jj` 支持操作日志与轻松撤销、把工作副本建模为提交，并能携带冲突通过变基；`git history` 暂不做到这些。
- 🚪 文档暗示该限制未来可能解除，前提是 Git 学会处理“一等冲突”，作者对此持期待态度。
- 📰 文章发布于 2026 年 7 月 13 日，并在 Hacker News、lobste.rs 和 r/programming 上引发讨论。
- 💡 结论：`git history` 尚不能完全替代 `jj`，但已在日常 Git 中实现了许多吸引人的优点，是重要进步。

---

### [未找到标题](https://www.vpdae.com/redirect/xojc8fotobhlbnr4q89hvk97wwd)

**原文标题**: [No title found](https://www.vpdae.com/redirect/xojc8fotobhlbnr4q89hvk97wwd)

无法总结：未找到主要内容。

---

### [如何命名事物 | Koleman Nix](https://kolemannix.com/blog/how-to-name-things/)

**原文标题**: [How to name things | Koleman Nix](https://kolemannix.com/blog/how-to-name-things/)

命名是软件工程与知识工作的核心技能：清晰的语言通常意味着清晰的思考，而模糊的表达往往反映内在理解不足。文章强调，命名不是套用规则，而是理解事物本质、使用语境、对称关系与读者感受的沟通过程；在代码库中，名字是人类与语言模型进入语义世界的入口。

- 🧠 命名是软件工程和知识工作的基本能力；语言模糊往往说明思考也不清晰。
- 💬 每次命名都在沟通：变量、函数、字段、API、页面、数据库表/列、产品，甚至同时面向用户和代码的 URL 参数。
- 🤖 与 LLM 协作时尤其如此：新代码库初期效果常很好，后期变差往往是名称与术语被不断“插值”而失真，偏离最初意图。
- 🔁 要维持与模型协作的可持续性，必须持续减少、澄清、打磨术语；这等同于打磨系统本身的复杂度。
- 🧩 DRY 应理解为：一个事实只在一处表达，追求语义压缩而非位级相同；两个都等于 64 的常量若含义不同，就应分开。
- ⚠️ 不要把一致性本身当成美德；Clean Code、OO、FP 等可能变成带承诺的“产品”，诱使人把判断外包给规则，拒绝深入原语。
- ❓ 对可选值命名不要找机械规则；要像队友一样读代码并思考：它总是可选？缺失是错误？是回退？是覆盖？覆盖本就可选。
- 🧭 应保持一致的是命名过程：纳入类型、用法、本质、对称性等更多输入，让 src/dst 这类名字彼此呼应。
- ❤️ 好的命名是智力共情；按眼前需求命名则自私短视。比如 to-pixels 的本质只是四舍五入/实数转整数，像素叙事应留在调用点。
- 🗂️ created_at 是合理默认，但要看行代表什么：合成对象可用 created_at；真实世界文档可能更该叫 uploaded_at、issued_at。日期列作为一组要讲清一个故事。
- 🧱 值的形状也影响命名：fallbackConfig 若是稀疏覆盖表，Option[Map] 可能重复表达缺失；若 None 与空 map 处处等价，Option 就是噪音，应在边界折叠。
- 🏷️ 名字会掩盖一般性：mergeTargetValuesIntoSourceTemplate 本质是 template ++ values / map union；按需求命名会使它难以被发现和信任，用惯用操作即可消除问题。
- 🧵 代码库大部分文本都是名字，是人类和 LLM 的语义入口；别扭的名字常指向模糊概念或冲突语义，如 documentDate 可能指文档日期或到达日期，导致错误且难改。
- 🌱 命名也可反向检验设计：设计未成形时难命名很正常；若设计几乎定型仍无法命名，可能是警讯；精炼中自然出现好名字则是高质量信号。
- ✅ 结论：命名要深思熟虑、整体考虑、依本质而非眼前需求，并像真正在乎读者一样对待。

---

