### [](https://hatchet.run/blog/postgres-survival-guide)

**原文标题**: [Hatchet · The startup's Postgres survival guide](https://hatchet.run/blog/postgres-survival-guide)

作为初创团队在生产环境中运行 Postgres 的实战指南，本文基于作者两年多的运维经验，从基础到进阶梳理了一系列避免数据库“翻车”的建议，内容涵盖 Schema 设计、查询优化、索引策略、迁移、连接管理、查询计划器、autovacuum、批量写入、数据/索引膨胀、分区以及大表数据迁移等关键话题。

- 📐 Schema 设计是最难事后调整的部分，应结合读写场景迭代建表；优先使用 identity 列或 UUID 主键、timestamptz，低容量表可用外键级联删除，但高容量时要谨慎。
- 🔍 读查询的核心是让 Postgres“快速找单行”，而不是全表顺序扫描；索引查找约为 log(n)，不到 20k 行的小表全表扫描往往也很快。
- 🔗 编写 JOIN 时，ON 子句要像 WHERE 一样重视；尽量用主键/索引列作为连接条件，避免无索引连接拖慢性能。
- 🗂️ 大表列表查询可用复合索引优化；将 ORDER BY 的列放在索引最后，并尽量与排序方向对齐。
- ✍️ 写入事务要短，避免在事务中途调用外部服务，只锁定必要的行；创建索引请用 CREATE INDEX CONCURRENTLY，防止锁表阻塞写入。
- 🔄 迁移要保持增量、尽量在事务内执行，参考 expand and contract；需要注意 ALTER TABLE 以及新 check constraint 可能锁表，必要时使用 NOT VALID。
- 🔌 数据库连接要长生命周期并复用，避免连接风暴；可引入 pgbouncer，或使用应用内连接池（如 Go 的 pgxpool）。
- 🧠 查询计划器是“漏水的抽象”，依赖统计信息；应利用 ANALYZE/autovacuum 更新统计，并用 EXPLAIN ANALYZE + explain.dalibo.com 可视化排查慢查询。
- 🤷 在统计信息正常时，Postgres 仍可能倾向 seq scan，因为索引扫描有额外开销；可接受该计划，或考虑重构查询、分区表，而不是疯狂加索引。
- ⚡ 高吞吐写入推荐批量插入/隐式事务（如 pgx SendBatch），文章实测能将吞吐提升约 10 倍。
- 🧹 autovacuum 在高写入场景下默认配置可能跟不上，需要监控运行超过 1 小时的 autovacuum 并及时调优，避免事务 ID 回卷引发长时间停机。
- 💥 除了死元组，表和索引膨胀同样危险；可通过调优 autovacuum、pg_repack、REINDEX INDEX CONCURRENTLY 处理，尽量避免 VACUUM FULL。
- 🔒 FOR UPDATE SKIP LOCKED 适合在 Postgres 中实现队列或租约，可以在并发弹任务时跳过已被锁定的行。
- 🍰 Postgres 内置分区非常适合时间序列数据：可独立 autovacuum、秒级删除旧分区，但要注意查询计划中的分区裁剪开销。
- 🚚 大表迁移到新表时，不要用单个长期事务；可借助触发器、批量回填和主键唯一约束来同步新写入并避免重复数据。

---

### [](https://nango.dev/blog/lessons-from-operating-api-auth-for-900-apis?utm_source=programming_digest&utm_medium=newsletter&utm_campaign=brand_awareness_2026_08&utm_content=auth_lessons_900_apis&utm_source_platform=bonobopress)

**原文标题**: [What we learned operating auth for 900+ APIs | Nango Blog](https://nango.dev/blog/lessons-from-operating-api-auth-for-900-apis?utm_source=programming_digest&utm_medium=newsletter&utm_campaign=brand_awareness_2026_08&utm_content=auth_lessons_900_apis&utm_source_platform=bonobopress)

overview summary
2025 年 5 月 Nango 因一个 if 条件 bug 导致数百连接令牌永久失效，随后在支持 900 多 API 的过程中总结出 OAuth 提供者之间存在大量非标准化行为。文章提炼了四条关键教训，并向 API 开发方提出十条改进建议。

- 🔄 令牌轮换使普通 bug 不可逆：刷新令牌一旦被替换，旧令牌可能立即失效，若未及时持久化新令牌，用户必须重新授权；Nango 因此采用先保存刷新令牌再继续其他逻辑的策略。
- 🔁 不同提供者的轮换规则差异巨大：Airtable 可能因重试旧令牌而撤销整个授权，Salesforce/Slack 启用轮换后同样严格，Xero 则提供 30 分钟宽限期。
- ⏳ 无法可靠预知访问令牌过期时间：RFC 6749 允许 expires_in 可选，Zendesk 默认不返回，Salesforce 需额外调用 introspection 接口，导致静默失效。
- 🪙 刷新令牌的生命周期同样不一致：NetSuite 7 天过期，Google 无限期但有诸多条件如测试状态、闲置超 6 个月或超 100 个令牌，Nango 用 cron 主动刷新来规避。
- 📄 认证失败并不总是显示为失败：Zoho CRM 返回 HTTP 200 但错误在 body，Workday 等只返回空数据，LastPass 等需在纯文本中搜索“Authorization Error”，Nango 为 276 个提供者声明了认证检查端点。
- 🚨 提供者会对 API 认证做破坏性变更：Figma 通过邮件通知 auth header 变更，Shopify 悄悄改变 offline token 有效期；这些变更无可靠 feed，Nango 约 16% 配置提交是修复。
- 🧩 有时必须绕开提供者：Salesforce Data Cloud 拿不到测试凭证就构建 mock server，LastPass 全 API 只有一个 URL 需特殊代理支持，Asana 错误通过社区 forum 才找到解决办法。
- 🧾 给 API 提供者的十条建议：始终返回 expires_in、给被轮换的旧 token 一个有界宽限期、用具体错误码替代 invalid_grant、把 auth 变更当作破坏性 API 变更、文档化撤销触发条件、提供无销售门槛的测试方式、保持 auth 文档公开准确、不要让 200 表示有错误、在规范模糊处遵循常规行为、让 REST 成为事实来源。
- 🔍 核心结论：OAuth 只是标准，提供者并不互通；生产环境中会出现未文档化的差异，客户端需要防御性设计与逐提供者适配。

---

### [](https://deepsystemstuff.com/how-oracles-secret-column-sorting-technique-became-public-after-its-patent-expired-making-sorting-5x-faster/)

**原文标题**: [What is Orasort? understanding Oracle’s Sorting Aglorithm In Simple Terms – deepsystemstuff.com](https://deepsystemstuff.com/how-oracles-secret-column-sorting-technique-became-public-after-its-patent-expired-making-sorting-5x-faster/)

Orasort 是 Oracle 发明的排序算法，其专利已于 2024 年到期并进入公共领域。该算法通过利用 CPU 寄存器一次比较 8 字节数据，将传统逐字符排序的速度提升约 5 倍。目前开源数据库与云服务商正受益于此，本文用通俗语言解释了其原理、优势及高层处理流程。

- 🔍 Orasort 是 Oracle 的排序算法，由 Mark Callaghan 取得专利；2024 年专利期满，现已公有化。  
- 🐢 传统排序逐字符（1 字节）比较，如“Apple”vs“Amazon”需比对到第二个字符，长字符串更耗 CPU。  
- ⚡ Orasort 将字符串中每 8 字节提取为 64 位整数，利用 CPU 寄存器批量比较，减少 CPU 周期，速度提高 5 倍。  
- 🌍 开源数据库（如 MySQL、PostgreSQL）已开始整合 Orasort，云服务因 CPU 使用降低而节省运营成本。  
- 🗂️ 高层过程：先抽取待排字段的键和 ID 到 RAM 排序区；海量数据时分区落盘、逐批处理。  
- ✍️ 排序结果采用异步、分阶段写回磁盘，完成后在磁盘上做最终合并，避免一次性写入压力。

---

### [](https://docs.pixeldrain.com/posts/2024-03-07_network_optimizations/)

**原文标题**: [Fornax's Guide To Ridiculously Fast Ethernet â¢ Pixeldrain Documentation](https://docs.pixeldrain.com/posts/2024-03-07_network_optimizations/)

overview summary
- 📚 本文是 Pixeldrain 站长分享的将服务器网络速度优化至 100 GbE 的实战指南，内容涵盖内核参数、网卡设置、BIOS 配置、软件架构等全方位技术要点。
- ⚙️ 系统内核参数（sysctls）是性能基础，推荐使用 BBR 拥塞控制算法、配合 fq 队列规则，并启用 `net.ipv4.tcp_shrink_window` 防止 TCP 缓冲区无限增长，从而大幅降低内存占用并提升吞吐。
- 📏 TCP 收发缓冲区大小需根据带宽延迟积（BDP）计算，为了跑满 100G 高延迟链路，需要将 `tcp_wmem`/`tcp_rmem` 最大值设为 1 GiB，同时将 `tcp_mem` 三个阈值设置为内存页数的 40%、50%、60%。
- 🖧 网卡选择上，作者推荐 Mellanox ConnectX-5/6，不推荐安装闭源驱动，建议使用内核自带驱动并升级固件。
- 🛠 使用 ethtool 优化网卡：将 combined 通道数设为 CPU 核心数（多 CPU 平台仅用单 CPU），增大 rx/tx 环形缓冲区至 8192，关闭自适应中断并设置合理的中断合并值（约 100µs，帧数 8192）。
- 💾 ethtool 设置需通过 systemd .link 单元或脚本持久化，否则重启后失效。
- 🔩 BIOS 中应设置 NUMA nodes per socket 为 NPS1、禁用 L3 cache 作为 NUMA domain；核心数超过 128 时关闭 SMT；最关键是关闭 IOMMU 或使用 passthrough 模式，否则网卡性能会被严重拖垮甚至系统崩溃。
- 🔄 反向代理会带来多次内核/用户空间拷贝，严重限制 100G 吞吐，因此 Pixeldrain 直接用 Go 内置 HTTP 服务器，并利用 SO_REUSEPORT 实现零停机升级。
- 🚀 HTTP/2 与 BBR 配合能显著提升加载速度；HTTP/3（QUIC）目前吞吐远不如 HTTP/2，因此作者仍推荐 HTTP/2。
- 🐧 操作系统建议使用精简的 Debian，并升级到至少 6.5 内核（最好更新），因为新内核在 TCP 性能和网络栈优化上持续大幅改进（如 6.8、6.19 等版本）。

---

### [](https://www.righto.com/2026/08/spacelab-core-memory.html)

**原文标题**: [Cores in space: The core memory module from a 1980 Spacelab computer](https://www.righto.com/2026/08/spacelab-core-memory.html)

Spacelab 是欧洲为航天飞机货舱设计的可重复使用实验室，其 1980 年计算机采用法国 Mitra 125 MS 小型机，而非标准航天飞机电脑；该机配备的是 128KB 磁芯内存而不是硅内存。文章详细拆解了这块磁芯存储模块，解释其工作原理（磁滞、重合电流寻址、感测线、破坏性读出等）、独特 2½D 架构、板级布线细节、历史背景及磁芯内存在航空航天领域“长寿”的原因。

- 🚀 Spacelab 实验室由欧洲建造，使用三台法国 Mitra 125 MS 计算机，分别负责管理、实验和备份；存储使用磁芯内存而非半导体内存。
- 💾 该计算机容量为 128KB，采用铁氧体磁环存储每位数据，内存堆栈约占机箱三分之一，由 7 块电路板构成并可通过侧板滑出散热。
- ⚙️ 磁芯核心原理：利用磁滞特性，X/Y 驱动线各通半电流，在交叉处选中一个磁芯；感测线读取时若磁芯为 1 则产生感应电流，读后需重写。
- 🧮 为解决驱动线数量问题，使用二极管矩阵配合“顶部/底部”驱动选择线，同时用禁止线（或 2½D 架构）实现逐位写入。
- 📐 Spacelab 内存采用 2½D 架构：取消禁止线，每个位配独立 X 驱动；U 型垂直环和相位反转技术将垂直驱动数量减半。
- 🔬 核心板构造：每板有 1024 条 Y 线、288 条 X 线，共 294,912 个锂铁氧体磁芯，每个约 0.8mm；感测线采用双绞和交叉“蝶形”布局抑制噪声。
- 🛠️ 板卡拆解显示：每块核心板背面有 18 个双通道感测放大器芯片、二极管阵列芯片，以及大量用于矩阵选择的 PCB 走线和通孔。
- ⏳ 历史对比：磁芯内存曾是主流，Whirlwind 最初手绕一板需 40 小时，IBM 后来自动化使成本每两年降半；到 1980 年已非常先进和致密。
- 🛰️ 磁芯内存在航天领域比半导体更耐用：断电不丢失数据且抗辐射；1991 年航天飞机换用半导体 AP-101S 后，需电池备份和纠错码应对辐射翻转。
- 📌 文章还提及“core dump”一词源自磁芯，并附有详细引脚注释、电路图和参考文献；作者计划继续研究该 Spacelab 计算机。

---

### [切换前的对等](https://alexocallaghan.com/parity-before-cutover)

**原文标题**: [Parity before cutover](https://alexocallaghan.com/parity-before-cutover)

这篇文章讨论了一个典型的“重写迁移”陷阱：服务长期存在 Python 2 旧系统与 Python 3 新版分支，目标虽然清晰，但一次性大切换的做法让风险不断累积。作者提出先“倒退一步”——让新代码先跑在旧基础设施上，实现同代码后再迁移基础设施，从而把复杂迁移拆解为可逐步发布的小变更。

- 🔁 长期存在的“v2”重写语言会让风险累积：热修复需同步两套代码，行为差异则成为未来故障源。
- ⏳ 大爆炸式切换把所有风险集中到单一时间点，也延迟了反馈，错失尽早发现问题的机会。
- ⏪ 作者主张先“倒退”：把新版本代码放回旧 on-prem 环境，让旧环境与云环境运行同一份代码。
- 🐍 面对旧系统最高只支持 Python 3.6、新版要求 3.7 的问题，选择降级到 3.6，并保留按环境选择运行配置，而不是堆砌临时方案。
- 📦 降级表面是负进度，却让一套代码能同时部署到旧主机和 Kubernetes，使后续迁移路径大大简化。
- 🔍 在代码一致后，每次发布同时推向两个环境，行为差异立刻暴露，多年累积的分歧被逐步清偿。
- 🌩️ 真正切换到云端时，代码保持不变，问题只会来自基础设施；这次 cutover 因此变得“无聊”而安全。
- 📊 用表格展示了逐步序列：代码/基础设施/Python 版本每次只动一个变量，而不是全部同时改变。
- ✅ 迁移完成后，被卡住多年的 Python 升级成了普通例行发布——旧系统限制消失，且只需升级一套代码。
- 🧭 核心启示：长期未合并的分支或等待他人迁移的“v2”，通常说明步子太大；应寻找可立即发布的中间状态，哪怕看起来像倒退。真正的难点从来不是终点，而是可一步步释放的路径。

---

### [任意规模的 Git · Cursor](https://cursor.com/blog/git-at-any-scale)

**原文标题**: [Git at any scale · Cursor](https://cursor.com/blog/git-at-any-scale)

Git 托管的规模化之所以极难，源于 Git 本身是分布式仓库、依赖 packfile 进行存储和网络传输，而 packfile 的随机读模式与图遍历让复制和扩展都非常棘手。文章先回顾 GitHub 早期尝试文件系统复制失败的教训，再介绍成功又被验证有瓶颈的 Spokes 方案；最后引出 Cursor 团队构建的新系统 Continuity——它以 S3 中的预写日志（WAL）为唯一事实源，把磁盘上的仓库视为可重建缓存，从而在保持线性一致的条件下实现高度弹性和水平扩展。该文也是为 Cursor 的 Git 托管产品 Origin 做技术铺垫。

- 😵 Git 的分布式设计本身构成了托管痛点：所有仓库副本对等，服务器端并没有天然的中心化地位，packfile 同时决定本地存储和网络传输。
- 🧠 用分布式键值存储按对象拆散 Git 并不可行：Git 的 DAG 必须逐步遍历，每个指针依赖前一个对象，远程往返会拖垮一切操作。
- 🏢 GitHub 曾试过 NFS、GFS、DRBD 等文件系统复制方案，全因 packfile 随机读与网络化文件系统语义不匹配而失败。
- 🔩 Spokes 的正确判断：不修改 Git、不碰文件系统，而是把完整仓库复制到本地 NVMe，并在 packfile 层面做应用级复制。
- 🗳️ Spokes 使用三阶段提交（3PC）保证多个副本全量一致：push 时同步参考事务，push 被多数节点确认后才生效，读取可路由到任意副本。
- 📉 Spokes 的根本瓶颈是 3PC：任何副本变慢都会拖低推送吞吐，增加副本数会恶化推送性能；小型闲置仓库也要维持三份副本，造成浪费。
- 🐾 Spokes 运维困难：磁盘仓库就是事实源，每个副本都需要持续校验、跟踪和修复，仓库像宠物一样靠人工关注，路由表数据库还带来额外单点。
- 📜 Continuity 改为 WAL-first：每次 push 先持久化为 S3 对象，写入成功后才确认；参考事务提交后再把指向 WAL 的指针写入索引，推送因此线性化。
- 🗃️ Continuity 没有路由表，磁盘只是缓存：通过 rendezvous hashing 找到预期节点，缺仓库时可直接从 WAL 物化；任一台主机都能当 primary，靠 S3 原子 CAS 处理并发冲突。
- 📡 副本一致性很轻量：每个副本用 S3 条件 GET 校验自己的 ETag，304 就直接服务，200 就先追赶 WAL；gossip 用 UDP 丢了也无所谓。
- 🧹 压缩开销被集中到 primary：只有 primary 做几何压缩，副本从 S3 下载压缩后的 pack，以带宽换 CPU，避免多副本同时重打包引发的故障。
- ⚡ 扩展与吞吐：读取可随副本数线性扩展，压测支持 100 个副本；S3 Standard 能支撑约 120 push/s，S3 Express One Zone 可超过 300 push/s。
- 🔍 WAL 即历史：每次推送和重打包都被记录，可回放、可回滚、可审计，不依赖任何外部数据库，也不需要像 Azure DevOps 那样运行并维护 SQL Server。
- 🚀 Origin 是这套设计的商业化落地，目标是为企业提供更可靠、更高性能、迁移更平滑的 Git 托管服务。

---

