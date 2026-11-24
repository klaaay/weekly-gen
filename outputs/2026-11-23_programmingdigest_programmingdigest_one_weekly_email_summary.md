# [Git beyond the basics](https://programmingdigest.net/newsletters/2414-git-beyond-the-basics)

### [Git 进阶：工作树、Cherry-Pick 与签名提交 | Larvitz Blog](https://hofstede.it/git-beyond-the-basics-worktrees-cherry-picks-and-signed-commits/)

总结失败：模型未返回符合格式的摘要。

### [Airbnb 搜索 API - SerpApi](https://serpapi.com/airbnb-search-api?utm_source=programmingdigest&utm_campaign=airbnb)

SerpApi 的 Airbnb Search API 发布说明显示，该接口可从 Airbnb 搜索结果抓取房源，支持按目的地或地图范围检索，结合日期、住客、价格、房型、设施、无障碍、房东语言和预订选项筛选，并通过 Airbnb 域名与货币本地化结果。返回数据覆盖评分、徽章、含折扣及税费明细的价格、房型床位、照片和 GPS 等结构化信息，同时提供分页、JSON/HTML/Markdown 输出以及缓存、异步等 SerpApi 参数；文档标注 API 可用性为 99.944%。

- 🚀 **API 上线**：SerpApi 提供 Airbnb Search API，端点 `https://serpapi.com/search?engine=airbnb`，用于抓取 Airbnb 搜索结果中的住宿房源；每个房源返回名称与类型、评分与评论数、徽章、住宿价格及明细和折扣、房间与床位、照片、GPS 坐标等数据。
- 🧩 **双入口检索**：使用 `q` 按城市、地区、街区、地址或地标检索，或用 `map_bounds` 按地图范围检索；两者至少设置一个。`map_bounds` 格式为 `north,east,south,west` 的 4 个逗号分隔数字，仅返回边界内房源，可单独使用或与 `q` 组合。
- 🌐 **本地化与货币**：`airbnb_domain` 决定结果语言、地区与默认货币，默认 `airbnb.com`；`currency` 可覆盖价格货币。例如 `airbnb.co.uk` 为英式英语和 GBP，`fr.airbnb.ca` 为法语（加拿大）和 CAD，`airbnb.fr` 为 EUR；欧盟和英国等地区还会返回 `host_type`，价格明细会列出税费。
- 🗓️ **日期与住客**：`check_in_date` 和 `check_out_date` 需成对使用，格式为 `YYYY-MM-DD`，退房日期须晚于入住日期；`adults`、`children`、`infants`、`pets` 用于限定可接待的住客数，设置 `pets` 后仅显示允许宠物的房源。未设置日期时，Airbnb 通常按 5 晚推荐日期并返回每个结果的入住/退房日期及对应价格。
- 🎯 **高级筛选**：支持 `room_type`（`entire_home`、`private_room`，酒店用 `property_types=hotel`）、含所有费用的 `min_price`/`max_price`、最小 `bedrooms`/`beds`/`bathrooms`，以及逗号分隔的 `property_types`、`amenities`、`accessibility_features`、`host_languages`；`instant_book`、`self_check_in`、`guest_favorite`、`luxe` 为布尔选项。未设置日期时，价格筛选按 5 晚住宿计算。
- 📦 **分页与状态**：`page` 用于获取指定页，默认第 1 页；Airbnb 每页最多返回 18 条结果，最多 15 页。`serpapi_pagination` 提供 `current`、`previous`、`next` 和 `other_pages` 链接；JSON 响应的 `search_metadata.status` 会经历 `Processing` 到 `Success` 或 `Error`，失败时 `error` 包含错误信息。
- 💻 **输出格式**：`output` 支持 `json`（默认）、`html`、`md`；`md` 面向 LLM 和 AI Agent，使用表格、Markdown 链接和 YAML frontmatter，也可通过 `/search.md` 或请求头 `Accept: text/markdown` 获取。`json_restrictor` 可限制输出字段以减小载荷；HTML 结果不含完整响应，仅有文本，并可通过 `search_metadata.prettify_html_file` 查看美化版。
- ⚙️ **缓存与异步**：`no_cache` 可强制跳过缓存，缓存仅在查询和全部参数完全一致时命中，1 小时后过期，缓存搜索免费且不计入月度搜索。`async` 异步提交搜索后需通过 Searches Archive API 取结果；`no_cache` 与 `async` 不能同用，`async` 不适用于启用 Ludicrous Speed 的账户；`zero_trace` 仅企业版可用，启用后跳过在服务器存储搜索参数、文件和元数据。
- 📊 **结果结构**：`organic_results` 每项包含 `position`、`listing_id`、`title`、`name`、`description`、`link`、`rating`、`reviews`、`is_new_listing`、`badges`、`price`、`extracted_price`、`old_price`、`price_qualifier`、`price_breakdown`、`price_disclaimers`、`check_in_date`、`check_out_date`、`details`、`bedrooms`、`beds`、`bathrooms`、`host_type`、`highlights`、`free_cancellation`、`gps_coordinates`、`thumbnail` 和 `images`；价格明细可包含折扣、税费和折后总价。
- ✅ **示例覆盖**：文档给出 Austin, TX 的 `q` 搜索、日期与住客、组合筛选（整套房、2+ 卧室、泳池、WiFi、Guest favorite、4 位住客、总价不超过 $3,000）、Downtown Austin 的 `map_bounds`、`airbnb.fr` 与 `airbnb.co.uk` 本地化以及 `page=2` 分页示例；示例价格分别按 4 晚或 5 晚住宿显示，并展示折扣和税费明细。

### [软件职位头衔的族谱 – zwischenzugs.com](https://zwischenzugs.com/2026/11/03/a-family-tree-of-software-job-titles/)

Ian Miell（在 Claude 协助下）发布了一张从 1940 年代至今的软件职位职称家族树，收录 104 个职称，按开发、分析架构与领导、运维与基础设施、网络与安全、数据与 AI、质量与测试、支持与客户七大家族分列，并以五年为行、实线与虚线箭头展示职称的衍生和影响关系；站点支持按家族或单个职称查看历史，作者借此说明职称如何分化、合并、复用并反复包装 DevOps、SRE 与平台工程之争，同时提醒图中日期是常见化估计而非首次记录。

- 🚀 **发布家族树**：发布 104 个软件职称的交互式家族树，覆盖 1940 年代至约 2025 年，按七个家族分列，用户可点击家族筛选或点击职称查看历史、背景和关联。
- 🧩 **组织规则**：时间从上到下以五年为行，实线箭头表示职称由父级演化而来，虚线表示影响或常见职业迁移，粗体标记地标性职称。
- 🛠️ **数据与实现**：全项目由一个 Graphviz 文件和一个 JSON 描述文件构成，每个职称在 `.dot` 文件中占一行，用 `dot -Tsvg job_title_family_tree.dot -o job_title_family_tree.svg` 渲染；新增职称需在所属家族列加节点、在五年行加入口并补父级箭头。
- ⚠️ **日期口径**：图中日期大致表示职称变得常见的时期，不是首次有记录的使用时间，且为作者最佳估计而非有来源引证；如 SRE 于 2003 年在 Google 出现、DevOps 于 2009 年被提出、Data Scientist 于 2008 年出现较确定，不少标注为 c. 且带不确定性。
- 📚 **编码起源**：1947 年 Goldstine 与 von Neumann 的《Planning and Coding of Problems》把使用计算机分为数学家规划问题、编码员翻译为机器指令，编码曾被视为较低地位的文书工作且多由女性承担；后来编码成为困难且有创造性的部分，编码员并入程序员，早期 ENIAC 程序员部分来自陆军人工计算员。
- 🔄 **拆合循环**：Webmaster 约 1993 年常由一人负责写 HTML、运行服务器、回复邮件和维持站点，至 2000 年代中期消失并拆给 Web 开发者、系统管理员、编辑和设计者；Web 开发约 2005 年分为前端和后端，约 2008 年又以 full-stack 合并。
- ⚡ **短命职称**：Prompt engineer 在 2023 年因高薪职位受关注，随着模型改进该技能并入其他岗位，在树上很快被 AI engineer 吸收；Scrum master 需求在 2010 年代见顶后被许多组织并入工程管理或交付角色；最新为约 2025 年的 AI Agent / Context Engineer，是否独立仍待观察。
- 🔍 **名称复用**：Systems Engineer 在 1960 年代 IBM 指售前角色，与客户设计并启用安装，在 1990 年代受 Microsoft MCSE 认证影响指更资深、偏设计的系统管理员，同名但不同分支；Configuration management 从 1960 年代美国国防追踪硬件变更，到 1970 年代软件版本控制，再到后来 Puppet 和 Chef 等工具名称。
- 💡 **新瓶旧酒**：Forward deployed engineer 是 2025 年热门职称，OpenAI、Anthropic 和许多 AI 初创用其帮助客户落地 AI；Palantir 约 2010 年起即以嵌入客户现场、按客户问题构建所需功能的软件工程师为核心，类似 IBM 1960 年代售前售后设计安装的系统工程师。
- 🧭 **DevOps 争论**：Ben Treynor Sloss 将 SRE 定义为“what happens when you ask a software engineer to design an operations team”；DevOps 原意是开发与运维协作文化，约 2011 年 DevOps Engineer 成为职称，多指做自动化的人；树上 SRE 与 DevOps 箭头双向，平台工程以二者为父级并在 2022 年前后被称为 DevOps 的继任者，Dev/Ops 分工仍未解决。

### [Slack 迁移至蜂窝架构 | Engineering at Slack](https://slack.engineering/slacks-migration-to-a-cellular-architecture/)

Slack 介绍其关键用户面服务在约 1.5 年内从单体架构迁移到蜂窝（cellular）架构的实践：2021-06-30 的可用区网络故障暴露出跨 AZ 依赖和 gray failure 问题，促使团队把 AZ 视为可排空的 cell，通过 siloing 让服务只在本 AZ 内通信，并利用 Envoy/xDS 在边缘按 AZ 重分配流量，从而把故障限制在单个 AZ 内并支持快速、渐进、无用户可见错误的排空。

- 🐛 **事故背景**：2021-06-30 PDT，Slack 主要托管的 us-east-1 中一个可用区连接其他可用区的网络链路间歇故障；12:33 自动移除后恢复，17:22 再次故障，17:31 永久移除。尽管最终恢复，用户仍在此期间看到错误。
- 🧠 **灰故障判断**：一次 Slack API 请求可能扇出数百个 RPC，不同组件对故障 AZ 的可用性视图不一致，形成 gray failure；服务前端需先记录失败才能排除后端，而 Vitess 等强一致数据存储要求单一主分片可写，增加了自动补救难度。
- 🎯 **AZ 排空目标**：设计目标包括在 5 分钟内尽量移除一个 AZ 的流量、排空不得造成用户可见错误以支持事故中实验式缓解、支持 1% 粒度增量排空和回填，且排空机制不能依赖待排空 AZ 内的资源。
- 🧩 **siloing 机制**：服务只接收本 AZ 流量，并只向上游本 AZ 服务发送请求，使每个服务在逻辑上变成每 AZ 一套；把用户请求从某 AZ 的前端导走后，该 AZ 内服务因无新工作自然静默，故障被限制在单个 AZ 内。
- ⚙️ **Envoy/xDS 实现**：Slack 使用边缘 Envoy 和自研 Rotor xDS 控制面，通过 weighted clusters 与 RTDS 动态权重重配 us-east-1 的每 AZ 目标集群；某 AZ 权重置零后，Envoy 继续处理在途请求，但把所有新请求分配到其他 AZ。
- ✅ **排空特性**：控制面传播约数秒，Envoy 立即应用新权重；排空平滑，不丢弃负载均衡层查询；权重提供 1% 粒度；边缘负载均衡器位于其他区域，控制面区域复制并可抵御单 AZ 故障。
- ⚠️ **实现约束**：Slack 服务混用 Hack、Go、Java、C++，服务发现涵盖 Envoy xDS API、Consul API 和 DNS；DNS 缺少 AZ 和部分排空抽象，Vitess 等开源系统改代码面临内部 fork 或上游合并成本，因此未采用逐客户端改代码的朴素方案。
- 📈 **效果与后续**：文中按 AZ 的带宽/QPS 图显示，逐步把一个 AZ 的流量排到另外两个 AZ 时出现明显拐点，体现低传播时延和高粒度；后续文章将详述内部服务 siloing、无法 siloing 的服务及 Slack 运维和构建方式的变化。

### [一个由25小时的一天引发的 Chromium Bug | In Pursuit of Simplicity](https://ramsayleung.github.io/en/post/2026/the_chromium_bug_caused_by_25_hour_day/)

Chromium 同步服务的设备统计调度器把“下一个本地午夜”实现为在 `last_recorded_at` 上加固定 24 小时再取 `LocalMidnight()`；在夏令时回拨产生 25 小时的那天，这个目标时间会早于当前时间，导致任务立即重复调度。Chromium 已用增加 4 小时容差的方式打补丁，说明处理本地时间时不能假设一天恒为 24 小时。

- 🧩 **时间背景**：夏令时通过调整本地时间相对 UTC 的偏移实现：春季拨快形成 23 小时日，秋季拨回形成 25 小时日；温哥华和西雅图常用 PST（UTC-8）与 PDT（UTC-7）。
- 🌐 **现实差异**：不列颠哥伦比亚自 2026-03-02 起永久使用夏令时并放弃回拨，而安大略和华盛顿州继续切换，导致相距约 200 公里的温哥华和西雅图出现 1 小时时差。
- 🐛 **错误假设**：`components/sync/service/device_statistics_scheduler.cc` 的 `ComputeEarliestAllowedTimeToRun()` 用 `last_recorded_at + base::Days(1)` 表示“加一天”，即固定 86400 秒，再调用 `.LocalMidnight()`；本地日历日并不总是 24 小时。
- ⚡ **触发过程**：回拨日示例中 `last_recorded_at = 2025-11-01 00:30 PDT`，加 24 小时后变为 `2025-11-01 23:30 PST`，取本地午夜得到 `2025-11-01 00:00 PST`，早于当前时间，`Run()` 便立即执行并重新调度。
- 🔄 **重复调度**：执行后 `last_recorded_at = now` 仍处于回拨日 00:00~01:00 窗口，重新计算的 `LocalMidnight()` 仍是同一天 00:00，仍早于 now，于是再次立即触发，形成连续执行和调度。
- 🛠️ **修复方案**：Chromium 补丁在取午夜前加入 `base::Hours(4)` 容差，代码为 `(last_recorded_at.LocalMidnight() + base::Days(1) + base::Hours(4)).LocalMidnight()`；注释称用于覆盖 25 小时的回拨日，但这是容差式规避而非按本地日历精确计算，作者也质疑是否真正修好。

### [The Watchmaker：在数据库中构建机械表 · Trevor Dwyer](https://sqlartist.github.io/posts/the-watchmaker-building-a-mechanical-watch-in-a-database/)

作者用数据库空间几何从零建模并运行机械表：先在 SQL Server 2025 的 2D 空间能力中完成擒纵、轮系、发条和分轮四部分，后因 `geometry` 缺少旋转、仿射变换和真正 3D 能力迁移到 PostgreSQL 18 + PostGIS 3.6，构建 26 mm、34 个零件的 3D 机芯，自动检查干涉与拆解顺序，并计算一分钟 300 拍、30,901 帧。文章既展示数据库做几何物理仿真的边界，也对比了两个数据库空间能力的明显差距。

- 🎯 **建模路线**：把每个零件表示为多边形，用 `STIntersects` 反复检查重叠，将可运动位置存成表，运行时只做表搜索；数据库负责物理，Python 只渲染，另用独立 Python 镜像做双重校验。
- ⚙️ **SQL Server 擒纵**：SQL Server 2025 对约 97,000 个重叠问题计算约 6 秒，得到真实擒纵：每拍进 12°、回退 -0.2°、冲量约 10°，这些数字由齿形涌现而非代码写死。
- 🧩 **轮系与齿形**：轮系平均传动比为 8、7.5、10；标准外摆线齿在单齿内速度波动约 1%，直边齿波动 ±32%，并使 8 叶擒纵小齿轮卡死。
- 🛠️ **发条与单向机构**：棘轮和棘爪由形状天然实现单向，每转 36 次咔哒，松手回滑 10.9°；遍历发条长度后最佳填充 49.6% 发条盒，输出 6.36 圈、约 51 小时。
- 📈 **分轮精度**：分轮使时针转 1 圈时分钟转 12.0 圈，中心偏差 4.4 × 10⁻¹⁶ mm，SQL 中同样没有写死 12:1。
- ⚠️ **SQL Server 短板**：`geometry` 无旋转、平移、缩放或仿射变换，作者用 WKT 字符串重写实现 `fn_Affine`，旋转一个齿轮仍需 160 ms；无真正 3D 实体、挤出、3D 相交和 3D 旋转，保存动画耗时 20 秒，轮系动画 64 秒。
- 🔄 **迁移 PostGIS**：因 SQL Server 无法计算 3D 旋转与拆解，迁移到 PostgreSQL 18 + PostGIS 3.6；`ST_Rotate` 一行完成旋转，同样齿轮转 100 次 SQL Server 需 21 秒、PostGIS 低于 3 毫秒。
- 📦 **3D 机芯构建**：机芯直径 26 mm、表冠在 3 点；34 个零件、107 个片段、90,836 个三角形在 1 秒内构建，每个实体水密，体积与面积乘厚度吻合到 12 位小数。
- 🔍 **干涉检查**：数据库检查所有零件对；首次发现 4 处微小重叠，原因是圆被离散为多边形，孔 48 边、轴 32 边，角点穿出千分之几毫米，放大孔后通过。
- 🧭 **拆解顺序**：每轮找出可直线取出的零件，形成拆解轮次并转为爆炸视图；轮次越大越靠近主夹板，three.js 页面直接绘制 PostGIS 生成的三角形。
- ⚡ **一分钟运行**：运行一分钟即 300 拍、30,901 帧，全部由 PostgreSQL 计算；秒针完成一圈由齿形允许，SQL 未写 60；游丝按每 10° 摆角预生成 23 个形状。
- 🧪 **网格验证**：将擒纵网格细化 2 倍和 4 倍后，一分钟内解锁、冲量、跌落、锁定时刻均未移动，擒纵轮仍精确转 10 圈；修复了用 15 个网格步而非 1.5° 作限幅导致的减速 bug。
- 🛠️ **PostGIS 限制**：SFCGAL 精确 3D 太慢，一个 160 个角的柱体体积耗时 20 秒、两齿轮重叠测试一分钟未完成，故未使用；TIN 仍需以文本构造，部分 3D 重叠可退化为 2D 加高度判断。
- 📊 **能力对比**：同机测试中 PostGIS 在旋转等操作上远快于 SQL Server；作者认为 SQL Server `geometry` 自 2012 后缺重大空间新功能，2025 的向量、JSON、正则更新未覆盖空间类型。
- 🔮 **后续计划**：下一步是补全上链机构：上链轮和表冠轮齿侧向突出，属于真正 3D，将继续使用 PostgreSQL。

### [五项正在改变我对软件工程中AI看法的研究](https://newsletter.getdx.com/p/five-studies-that-are-changing-how)

Brian Houck 汇总的五篇近期研究共同指向一个变化：AI 正在压缩写代码等上游工作，GitHub Copilot 等工具能显著提升编码与 PR 产出，但增益沿提交、PR、仓库到发布逐级衰减，瓶颈转向评审、集成、验证和理解；同时开发者体验出现分化，共享理解与意图记录不足会积累新的认知债和意图债，因此工具、指标与团队设计需要随瓶颈一起后移。

- 📊 **Copilot 剂量效应**：Heilman 等分析 16,223 名开发者 43 周数据，控制 Active Coding Time 并在同一工程师内部比较，发现 Copilot 使用最高的周比未使用周每小时编码时间完成 PR 多约 40%，呈剂量反应且极高使用后趋平；效果在大 PR（7+ 文件）最强，并通过 7 项稳健性与证伪测试。
- 🔄 **交付链路衰减**：Demirer 等基于 100,000+ GitHub 开发者估计，自动补全带来约 +40% 提交，交互式编码代理约 +140%，自主代理约 +180%；但收益从代码生成到仓库、发布逐级衰减，发布最多约 +30%。AI 与人力替代弹性约 0.25，表明二者仍主要是互补，评审、集成、验证和发布仍需大量人力。
- ⚠️ **生产力—体验悖论**：Vella 与 Blincoe 对 95 名专业工程师进行六个月纵向研究，两个时间点均有 84% 报告生产力改善；但至少一个 DevEx 维度变差的工程师占比从 14% 升至 27%，心流最易受损、认知负荷略有恶化、反馈循环改善。DevEx 与生产力的横截面相关强，但变化分数不相关，提示两者在 AI 工作流中可能脱钩。
- 🛠️ **22 类期望工具**：基于 860 名 Microsoft 开发者的调查，Choudhuri 等提出 22 个超越代码生成的 AI 工具方向，核心是“有界委托”：AI 可承担文档更新、边缘用例单测等装配工作，但不接管核心逻辑、架构和关键决策；由于 AI 加速编码带来更多评审、事故和文档压力，开发者更希望 AI 嵌入验证任务，并要求权限范围明确（禁止自动批准）、数据来源清晰、显式不确定性信号和最小权限访问。
- 🧠 **认知债与意图债**：Storey 认为技术债已不足以描述 AI 时代的软件健康：技术债存在于代码，AI 可通过重构、测试生成和自动评审缓解；认知债存在于人，源于团队共享理解补充不及侵蚀；意图债存在于制品，源于目标、约束和理由不清晰、未记录或被遗忘。三类债相互作用并复合，应把共享理解当作一等交付物。
- 🧭 **瓶颈转移**：综合五项研究，AI 确实提高代码生成和个体效率，但增益不能同等传递到已交付软件；瓶颈已转向评审、集成、验证和理解，而工具、指标与团队设计尚未跟随。作者的核心判断是：生成代码的速度快于建立安全理解、验证和交付系统的速度。
