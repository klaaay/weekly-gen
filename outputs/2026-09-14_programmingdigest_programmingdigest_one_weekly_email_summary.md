### [如何命名事物 | Koleman Nix](https://kolemannix.com/blog/how-to-name-things/)

**原文标题**: [How to name things | Koleman Nix](https://kolemannix.com/blog/how-to-name-things/)

命名是软件工程与知识工作的核心技能：清晰的语言几乎总意味着清晰的思考，而每次命名都是在与同事、未来的自己以及语言模型沟通。文章主张按事物本质而非即时需求来命名，把命名视为一种智力共情；坏名字往往暴露出模糊概念，甚至牵出真实缺陷。

- 🧠 命名是基础能力：清晰语言体现清晰思考，含糊命名通常意味着内部理解不清。
- 💬 每次命名都是沟通：变量、函数、字段、API、页面、数据库表和产品名都在传递语义。
- 🤖 LLM 依赖代码库清晰度：术语被“slop-fried”后模型表现会退化；减少、澄清、打磨术语就是控制系统复杂度。
- 🔍 DRY 是语义压缩而非位相同：相同值不一定是同一事实，应抽象事实，而非偶然相等的数字。
- ⚖️ 警惕“一致性”崇拜：Clean Code、OOP、FP 等像带承诺的产品，诱人用规则逃避深入思考。
- 🧩 要一致的是命名过程：综合考虑类型、用途、本质、对称性（如 src/dst）和读者，而非死守“缩写/长名”规则。
- ❤️ 命名是智力共情：不要按“我为什么需要它”命名；如 to-pixels 本质只是浮点转整数，像素叙事应放在调用处。
- 🗓️ 时间字段要看语义：created_at 常是默认，但 uploaded_at/issued_at 取决于行代表真实世界对象还是软件合成对象。
- 📦 名称问题常是模型问题：如 fallbackConfig 是否为 Option[Map] 取决于缺失语义，名称与数据形状应一起审视。
- 🗺️ 坏名会隐藏通用性：mergeTargetValuesIntoSourceTemplate 其实只是 Map 合并，应使用 template ++ values 等惯用法。
- 🧵 坏名常牵出真 bug：documentDate 同时表示文件日期、记录日期和到达日期，导致陈旧规则判断错误，改名还需迁移与回填。
- ✅ 好命名反向检验设计：设计未定型时难以命名是正常信号；好名字自然涌现则是高质量信号。
- 🎯 结论：命名要深思熟虑、整体权衡、按本质而非需求、像在乎一样对待。

---

### [](https://www.revel.io/careers?utm_source=newsletter&utm_medium=cpc&utm_campaign=programming_digest&utm_id=revel_careers)

**原文标题**: [Careers – Revel](https://www.revel.io/careers?utm_source=newsletter&utm_medium=cpc&utm_campaign=programming_digest&utm_id=revel_careers)

Revel 的招聘页面强调硬件推动世界，而 Revel 致力于推动硬件前进。团队由高水平人才组成，文化强调协作、快速交付、持续挑战与高成长，同时展示员工证言、职位筛选、客户案例和全面福利。

- 🚀 使命：硬件推动世界，Revel 推动硬件向前。
- 👥 员工证言：团队水平极高，资深者可共事顶尖人才，初级者能快速成长。
- 🤝 协作文化：销售与工程紧密合作，倾听客户并快速交付。
- 🧠 FDE 视角：在前沿硬件团队成功所依赖的基础软件中拥有前排席位。
- 📈 挑战升级：难题不断变大，标准持续提高，个人也随之成长。
- 🏆 规模化后不变：节奏、雄心和团队水准始终如一。
- 🧩 开放职位：可按部门、地点、雇佣类型筛选；页面显示 0 个开放职位，并处于加载状态。
- 💡 号召：若想让工作在物理世界产生影响，这里就是建造之地。
- 📊 案例研究：Orbital Operations 以创业速度测试火箭发动机（2026 年 8 月）。
- ⚡ 案例研究：Impulse Space 使用 Revel 实现测试与建造同速（2026 年 6 月）。
- 🛠️ 案例研究：Astro Mechanica 借助 Revel 加速发动机测试（2026 年 3 月）。
- 🩺 福利：医疗、牙科、视力保险；401k；全员股权；公司付费人寿保险。
- 👶 福利：带薪产假/陪产假；每周五天提供午餐；全职员工无限带薪休假。

---

### [](https://www.benjoffe.com/fast-time-of-day)

**原文标题**: [A faster way to convert a timestamp â Hour, Min, Sec](https://www.benjoffe.com/fast-time-of-day)

overview summary
本文介绍 Ben Joffe 对“将一天内秒级时间戳 [0..86399] 转换为时、分、秒”的深度优化：通过重排计算打破依赖链，并结合定点数、高/低位乘法与 base-64 技巧，把延迟从传统库的约 16 个 CPU 周期降到最低约 5 个周期，且结果高度依赖平台、编译器和 SIMD 支持。

- 🎯 核心目标：把每日时间戳 [0..86399] 快速拆成 Hour、Minute、Second，传统日期库通常较慢且存在很长的串行依赖链。
- 🐌 传统做法：先算小时、余数，再算分钟、秒，步骤间强依赖；另一种“三组件独立计算”可打破部分依赖，但操作数更多。
- 🔗 关键突破 V1：把“总分钟”和“小时”放到最前面并行计算，再并行计算“秒”和“分钟”，从而显著缩短依赖链。
- 🧮 V1 特点：数学简单、可读性好，不依赖复杂位技巧；部分平台上约比传统方法快，是后续优化的结构基础。
- ⚙️ V2 固定点高/低位：用乘法高位直接得到商，结合 Lemire 风格的高/低位余数思路，通常只需四次乘法，具备低延迟和高吞吐。
- 🧙 V3 Base-64 技巧：利用恒等式把 base-60 时钟转成 base-64，使用 `% 64` 或 `& 63`，总延迟可低至 5 个周期，但整体操作更多，吞吐可能不如 V2。
- 📊 基准结果：在 Apple M4 Pro、AMD Ryzen 9 9950X3D、Raspberry Pi Zero 等平台测试；V2/V3 通常优于传统方法和 Neri 2020 方案，但具体最佳取决于目标与编译器。
- 🧭 选择建议：要可读性选 V1；要吞吐与近最低延迟选 V2；要最低延迟且能接受“黑魔法”选 V3；SIMD 场景需按 x86 AVX-512 或 ARM Neon 选择。
- ⏱️ 亚秒扩展：同样思路可用于毫秒、厘秒、纳秒等时间戳拆分；毫秒场景可通过并行计算秒、分、时和毫秒字段降低延迟。
- 🌶️ 闰秒处理：给出无分支处理方案，以及利用定点数学“误差对齐”的闰秒 hack；适用于 Unix 时间且可兼容未来闰秒变化。
- 📱 ARM Neon SIMD：Neon 上可用小乘数、小移位避免 64 位扩展，以提升 SIMD 吞吐；x86 与 ARM 的最佳 SIMD 版本不同。
- ⚠️ 实践提醒：尽量使用无符号整数，有符号除法/取模更慢；编译器并不总能自动完成这些优化。
- 🔮 后续内容：作者还将发布复活节日期算法、地图投影等文章；测试与基准代码在 `fast-world-calendars` 仓库。

---

### [](https://yusufaytas.com/good-apis-age-slowly)

**原文标题**: [Good APIs Age Slowly | Yusuf Aytas](https://yusufaytas.com/good-apis-age-slowly)

概述总结  
好 API 的价值不在第一眼优雅，而在能否经受时间和真实使用的考验：边界清晰、契约稳定、少暴露、少隐藏假设，让其他团队敢依赖，并降低长期维护成本。

- 🕰️ 好 API 会缓慢变老：时间比代码评审中的优雅更能检验设计，真实需求、实现变更和意外用法才是试金石。
- 🧪 第一版常被高估：早期系统简单、作者与用户想法一致，任何设计都显得合理；一旦外部依赖字段、顺序或行为，内部实现就变成事实契约。
- 🚧 多数问题源于边界：必须尽早区分公共契约与私有实现；只要暴露了字段或状态，消费者就可能依赖它，之后移除极其痛苦。
- 🔒 保守暴露更安全：宁可先少暴露，后续再添加；删除已被依赖的内容会带来迁移、沟通和团队政治成本。
- 🧩 便利有代价：看似易用的 API 常隐藏调用顺序、用户类型、时序等假设；无聊但诚实的 API 往往更长寿，因为边界和状态更清晰。
- 🖥️ API 不是前端：不要围绕当前页面结构设计 API；屏幕不是领域模型，应围绕系统稳定概念建模，否则 API 会随产品迭代快速老化。
- 🔄 版本控制不能救烂设计：版本化必要，但不能消除耦合、过度聪明和用例特定带来的迁移、重测与兼容成本。
- 🎁 输出要谨慎：输入可略宽松，返回要严格克制；额外数据或行为一旦被看到就会被依赖，好 API 的关键是小心它“放出”什么。

---

### [](https://tidydesign.substack.com/p/a-coding-agent-is-six-functions-in)

**原文标题**: [A coding agent is six functions in a trenchcoat](https://tidydesign.substack.com/p/a-coding-agent-is-six-functions-in)

编码代理本质上是“六个函数穿着同一件风衣”：它通过一组特定工具，让 LLM 像人类一样探索、编辑代码库。Hadley Wickham 以 R 和 ellmer 为例，展示最小编码代理如何搭建，并说明安全限制与精确编辑工具为何重要。

- 🛠️ Claude Code、Cursor、Codex 等编码代理自 2025 年 11 月起深刻改变了软件开发实践。
- 🧩 代理 = 工具（函数）+ harness；编码代理的关键是提供适合代码库读写的专用工具。
- 📖 六类核心工具：读文件、写文件、编辑文件、列出文件、搜索、运行命令。
- 🧪 用 R 的 ellmer 可构建最小代理；仅需 read_file、write_file、run_command 三个工具即可运作。
- 🐚 运行命令是“万能逃生卡”，能执行 ls、grep、Rscript、git 等，但也很危险。
- ⚠️ 通用 shell 跨平台差异大、输出嘈杂，且难以判断某条命令是否安全。
- 🔐 专用 list/search 工具更容易加防护，例如用 safe_path() 限制路径不超出项目目录。
- 🙈 list.files() 默认跳过点文件，可避免读取 .Renviron、.Rhistory 和 .git/ 等敏感内容。
- ✏️ edit_file 支持只替换精确文本片段，避免重写整个文件，更快、更便宜、更安全且失败更明显。
- 🧠 真实编码代理通常还包含复杂系统提示；文章后续将深入讨论通用工具的安全防护。

---

### [](https://danluu.com/agentic-testing/)

**原文标题**: [How well do agents use test/verification techniques?](https://danluu.com/agentic-testing/)

overview summary
- 🧪 文章测试：给编码代理不同测试技术、测试库、形式化方法和技能提示，能否提升 Zstd 实现正确性。
- 📊 方法：在 Rust 中测试 26 种提示条件与 4 个技能，每种约 80 次运行；另用 IMAP RFC 等任务验证。
- 🎯 预注册预测大多命中：TDD 会差、形式化方法不会超常、Make no mistakes 无实质提升、多数测试技能不会超常。
- 🏁 总体结果：几乎没有条件显著优于默认；Default 无额外指令表现高于平均。
- 🧰 xhigh 下，模糊测试和性质测试相关条件平均略好于形式化方法；medium 下结果更混杂。
- 🧑‍💻 核心发现：代理通常不会有效使用被指定的技术或库，只是把普通测试套进新框架。
- 🧱 形式化方法：Verus、Alloy、Lean 4、Spin、TLA+、SMT、ACL2、Kani 等大多只做抽象、空洞或无关证明，很少验证实际易错代码。
- ✅ 代理在 xhigh 往往能让自己写的测试通过，但测试本身质量差，甚至把错误行为编码进测试。
- 🔁 TDD 表现差：测试更多、迭代更强，但更常写无关难例的测试，IMAP 上也同样不佳。
- 🐞 Differential、mutation、metamorphic、Insta、rstest 等条件基本未被按本意有效使用，收益很小。
- 🎲 Fuzzing 偶尔有效：只有少数结构化随机输入真正找到 bug；大量随机输入落入无效路径。
- 📉 技能总体不佳：Hegel 技能更差且成本更高；ECC 技能表面尚可但多因未被真正读取；Trail of Bits 技能也弱。
- ✍️ 作者自写简单技能得分最高，但未实现预期的独立上下文复核，说明方向可能有用但仍需迭代。
- 🧭 代理能找到高风险区域，但随后仍不会针对这些区域设计有效测试；人类引导和结构仍关键。
- 💸 成本与努力：低 effort 更差；审计增加成本且收益不稳定；Make no mistakes 与默认无显著差异。
- 🏭 作者疑问：AI 实验室为何不大力用 RL 环境训练代理学会测试，尤其测试质量对编码代理采用很重要。
- 🧪 结论：截至 2026 年 9 月，公开代理若无测试专家指导，测试与验证能力普遍薄弱，可能拖累软件质量。

---

### [](https://www.cloudways.com/en/prepathon.php?utm_source=ProgrammingDigest&utm_medium=newsletter&utm_campaign=Prepathon&utm_content=Community)

**原文标题**: [Prepathon 2026 | Build, Ship & Scale at Velocity](https://www.cloudways.com/en/prepathon.php?utm_source=ProgrammingDigest&utm_medium=newsletter&utm_campaign=Prepathon&utm_content=Community)

Prepathon 2026 是 2026 年 9 月 22–23 日举办的免费线上大会，聚焦 AI 时代的构建、交付与扩展，面向开发者、代理机构、店主和 SMB；两天包含专家演讲、实操活动和线下城市场次，免费注册但名额有限。
- 🗓️ 时间与形式：2026 年 9 月 22–23 日，免费线上活动，需注册且名额有限。
- 📍 线下场次：墨西哥城和卡拉奇在 9 月 25 日、班加罗尔在 9 月 26 日举行，提供实操、社交和现场活动。
- 🚀 核心主题：“The Future Is Here. Build. Ship. Scale at Velocity.”强调更快、AI 辅助，并突破传统网站边界。
- 👥 目标受众：开发者、代理机构主、店主、SMB；帮助各类在线建设者获得领先优势。
- 📈 活动规模：1500+ 参会者、8+ 直播场次、20+ 专家演讲者、100% 免费参与。
- 🧠 第一天重点：Deploy with Velocity 主题演讲、AI 代码归属、AI/真人成交、API 与推理成本、Prompt 到生产的 JavaScript 应用、WordPress 与现代技术栈、AI 对 WordPress 开发者的影响。
- 🛠️ 第一天活动：Human or AI? Who Gets the Sale? 与 Prompt -> Code -> Production Challenge。
- 💡 第二天重点：WordPress 只是起点、代理机构下一步机会、AI 成为下一批客户、WooCommerce 准备、AI 工具与代理交付、创始人个人品牌增长、停止只卖网站。
- 🎯 第二天活动/讨论：Would You Buy From This Store?、AI Can Build It, Can Your Agency Deliver It?、Ship It or Scrap It?。
- 🌟 演讲嘉宾：Katie Keith、Jason Swenk、Nicole Osborne、Valentin Radu、Miriam Schwab、Mike Szyszka、Suhaib Zaheer、Brent Weaver、Ajay Koshti、Ali Ahmed Khan 等。
- 🤝 行业支持：页面显示由 Cloudways Ltd. 提供支持，并设有合作伙伴与行业嘉宾阵容。
- 🔗 行动号召：免费注册，有限名额，活动标签为 #Prepathon。
- ✅ 核心卖点：两天专家演讲、现场演示和动手活动，帮助参与者更快构建、更聪明交付、更有信心扩展。

---

### [](https://hatchet.run/blog/postgres-survival-guide)

**原文标题**: [Hatchet · The startup's Postgres survival guide](https://hatchet.run/blog/postgres-survival-guide)

面向初创公司的 Postgres 生产生存指南，来自 Hatchet 联合创始人 Alexander Belanger，基于两年生产实战，覆盖 schema、查询、写入、迁移、连接管理、查询规划器、autovacuum、分区与高级技巧，核心目标是防止数据库在高负载下崩溃。

- 🧭 本文由内部文档整理而成，面向有 SQL 基础者；ORM 用户可能需突破抽象层写原生 SQL，如 sqlc 或 Prisma TypedSQL。
- 🧱 Schema 最难事后修改：应迭代设计，关注读写频率、常用过滤列和更新列；主键用 identity/UUID，时间用 timestamptz，低流量表可谨慎用外键级联。
- 🔍 读查询心智模型：数据库要么通过索引、唯一约束或主键快速定位单行，要么 seq scan 全表；小表 seq scan 通常几乎无感。
- 🔗 内连接尽量用主键，ON 条件应像 WHERE 一样使用索引，否则可能反映 schema 或规范化问题。
- 📈 列表查询常需复合索引：如 `(organization_id, created_at DESC)`，ORDER BY 列放索引最后并对齐顺序，以兼顾过滤与排序。
- ✍️ 写查询要短事务、避免事务中调用外部服务、只锁必要行；大表建索引务必用 `CREATE INDEX CONCURRENTLY`，避免阻塞写入。
- 🔄 迁移应尽量增量、可回滚并放在事务中；警惕 `ALTER TABLE` 阻塞写，check constraint 可用 `NOT VALID`，进阶采用 expand/contract。
- 🔌 连接昂贵且应长寿命，避免连接风暴；推荐外部 pgbouncer，或应用内连接池如 Go 的 pgxpool。
- 🧠 查询规划器是“漏抽象”，依赖表统计；ANALYZE/autovacuum 越及时，计划越准；按主键和索引查询更稳定。
- 📊 调试慢查询用 `EXPLAIN ANALYZE`（生产慎用）或 `EXPLAIN`，可结合 explain.dalibo.com 可视化，对比估算与实际行数。
- 🐢 有时 seq scan 是合理选择：索引扫描有堆表查找开销；若无法重构查询，可接受或考虑分区。
- 🚀 高吞吐写入用批处理减少往返和锁开销，`pgx SendBatch` 等可约 10 倍提升吞吐。
- 🧹 默认 autovacuum 可能撑不住高写入，导致死元组、表/索引膨胀，甚至 transaction id wraparound 大宕机；需监控 `pg_stat_activity` 并调优。
- 🧊 表膨胀可用 pg_repack 或 PG19 `REPACK CONCURRENTLY`，索引膨胀用 `REINDEX INDEX CONCURRENTLY`；`VACUUM FULL` 慎用。
- 🧩 高级技巧：`FOR UPDATE SKIP LOCKED` 可实现单查询队列和租约分发；分区适合时间序列、独立 autovacuum 和快速删旧数据，但未剪枝时可能有读开销。
- 📦 大表数据迁移避免长事务：用触发器加批量回填，主键唯一约束防重复，并让新写入同步到新表。
- ✅ 结尾邀请社区分享更多 Postgres 扩展与生产经验。

---

