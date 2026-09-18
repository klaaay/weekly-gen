### [快速扩展在线存储，为超过 10 亿 ChatGPT 用户提供服务 | OpenAI](https://openai.com/index/scaling-storage-one-billion-users-part-one/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-763-september-17-2026)

**原文标题**: [Rapidly scaling online storage to serve over 1 billion ChatGPT users | OpenAI](https://openai.com/index/scaling-storage-one-billion-users-part-one/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-763-september-17-2026)

OpenAI 的 Habitat 在线存储平台为 ChatGPT、API、Codex 等产品提供快速可靠的数据访问，并经历从 Python 客户端库到独立服务，再到 Rust 重写的演进。它当前支撑 7000 万 + 请求/秒、10 亿 + 周用户和 500PB+ 数据，以应对连续三年超 10 倍增长；文章还分享了 Python 尾延迟、连接池、下游洪泛和受限 API 等关键工程取舍。

- 🏗️ Habitat 是 OpenAI 的在线存储平台，让产品无需关心底层数据库、缓存、路由、授权、加密和序列化等细节。
- 📊 规模已超过 7000 万请求/秒、10 亿 + 周用户、500PB+ 数据，覆盖近 40 个地理区域。
- 🧩 2023 年 DevDay 首次推出时，Habitat 只是连接 Azure Cosmos DB 的 Python 客户端库。
- 🔄 到 2025 年中，客户端库因跨数十个服务协调部署而变得脆弱，Habitat 被拆分为独立服务。
- 🎛️ 服务化带来部署、可观测性和平台增强的单一控制点，也能集中执行安全、审计和存储访问控制。
- 🐍 团队短期继续使用 Python，将其视为战略技术债，优先稳定平台并解锁产品开发。
- ⏱️ Python 服务的核心挑战是 asyncio 调度延迟：CPU 重任务会让已就绪响应等待，推高尾延迟。
- 📈 团队实时监控事件循环延迟，限制每进程并发数，并大量横向扩展 Python 工作进程。
- ⚙️ Statsig 功能标志配置的每分钟无抖动 JSON 解析曾造成停顿，后通过更小配置、更长刷新间隔和 jitter 缓解。
- 🔁 连接池 LIFO 复用导致 metastable failure，让慢服务器接收更多流量；改为 FIFO 后打破反馈循环，现主要依赖 Istio/Envoy。
- 🌊 大量 Python 进程容易向下游造成连接洪泛；Envoy 负责 HTTP/2 多路复用、连接池、限流和断路器。
- 🧱 Habitat 有意提供受限 NoSQL API，围绕预定义对象和边，避免任意 SQL、无界查询和不可预测 fanout。
- 🔎 复杂查询通过 CDC 同步到 Rockset 离线二级视图，从而隔离在线存储与分析/搜索负载。
- 🦀 2026 年 Q2，2 名工程师借助 Codex 和 GPT-5.5 将服务重写为 Rust；Rust 已处理 95% 生产请求，CPU 效率提升 6 倍、内存效率提升 15 倍。
- 📚 后续文章将介绍多租户可靠性、分层读性能优化，以及 Azure Cosmos DB 存储层的扩展。

---

### [熊猫应该灭绝 • 埃迪的博客](https://eddie.codes/posts/pandas-should-go-extinct/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-763-september-17-2026)

**原文标题**: [Pandas Should Go Extinct • Eddie's Blog](https://eddie.codes/posts/pandas-should-go-extinct/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-763-september-17-2026)

概述摘要
文章认为 Pandas 的低效会迫使用户过早采用复杂的分布式系统，而 Polars 和 DuckDB 能用单机高性能填补 Pandas 与真正大数据之间的空白，并在速度、内存和开发体验上显著胜出。

- 🐼 作者主张应淘汰的是 Python 的 Pandas DataFrame 库，而不是熊猫；Pandas 的性能问题会推动用户过早使用 Spark、Databricks、Snowflake、Dask 等复杂系统。
- 📈 典型采用路径：从 Excel 转向 Pandas，在数十 GB 时遇到内存、速度或 API 问题，然后被建议转向“大数据”分布式工具。
- 📊 数据规模真相：引用 Amazon Redshift 分析，94.68% 的表小于 100GB，86.9% 的查询处理不超过 80GB，多数人面对的是“中等数据”问题。
- 🕳️ 关键缺口：Pandas 瓶颈与真正需要分布式系统的约 100GB 门槛之间存在空白，Polars 和 DuckDB 正好可以填补。
- ⚡ Polars：Rust 编写，API 类似 Pandas，但采用惰性求值、查询优化、流式分块和多线程，像数据库一样构建优化执行计划。
- 🦆 DuckDB：面向分析的嵌入式内存数据库，类似“分析版 SQLite”，提供 SQL 接口，可直接查询 CSV、Parquet 和内存中的 Python 对象。
- 🏁 1 Billion Row Challenge 结果：Pandas 中位耗时 4 分 28 秒、内存 38.12GB；Polars 5.04 秒、18.02GB；DuckDB 5.19 秒、1.93GB。
- 💻 本地开发性能：同一笔记本上 Pandas 耗时 12 分 15 秒，Polars 39 秒，DuckDB 47 秒；DuckDB 内存占用约 547MB。
- 🧵 免费收益：自动多线程、内存高效与流式处理、惰性求值、谓词下推，以及必要时智能溢写磁盘。
- 🏹 Apache Arrow：Polars 和 DuckDB 原生支持 Arrow，Pandas 2.0 起也支持；可在框架间近乎零拷贝迁移，但 Pandas 默认不是 Arrow-backed。
- 🚕 NYC 出租车案例：处理约 3GB Parquet 数据，纯 DuckDB 21.70 秒、216.76MB；纯 Pandas 41.88 秒、14.52GB；混合方案性能仍较差。
- 🧐 作者承认局限：基准测试不完美、切换成本可能存在、Pandas 也在改进；但 DuckDB/Polars API 更清晰，DuckDB 的 SQL 技能可迁移性强。
- 🧭 Polars 与 DuckDB 选择：取决于工作负载、经验和偏好；数据工程师常爱 SQL，软件工程师常爱 Polars，最好都试一试。
- 🚫 最终建议：不要仅因 Pandas 性能差就盲目采用分布式系统；多数人长期并不需要，性能如今更易获得，应多比较再决定。

---

### [](https://www.youtube.com/watch?v=fjF8EKnxKCU&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-763-september-17-2026)

**原文标题**: [Agents Without Code: Skills, YAML, and Filesystems Replaced Python — Philipp Schmid, Google DeepMind - YouTube](https://www.youtube.com/watch?v=fjF8EKnxKCU&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-763-september-17-2026)

這是 YouTube 網站的頁尾與導覽資訊，涵蓋平台介紹、新聞、版權、聯絡方式、創作者與開發者資源、廣告刊登、法律條款、私隱與安全政策，以及功能測試和 Google 版權聲明。

- ℹ️ 簡介
- 📰 新聞中心
- ©️ 版權
- 📮 聯絡我們
- 🎬 創作者
- 📣 刊登廣告
- 👨‍💻 開發人員
- 📜 條款
- 🔐 私隱
- 🛡️ 政策及安全
- ⚙️ YouTube 的運作方式
- 🧪 測試新功能
- 🏢 © 2026 Google LLC

---

### [](https://baldino.dev/blog/there-are-only-twelve-4x4-sudokus/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-763-september-17-2026)

**原文标题**: [There are only twelve 4x4 sudokus - and a cool trick for finding minimal subsets | baldino.dev](https://baldino.dev/blog/there-are-only-twelve-4x4-sudokus/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-763-september-17-2026)

本文探讨 4x4 数独到底有多少种解和有效谜题：空盘共有 288 个有效解，若把数字仅看作可置换符号，则只有 12 种结构上不同的解；最小有效谜题共有 85632 个，按数字置换等价后为 3568 个，并介绍了一种用位掩码判断最小子集的巧妙方法。

- 🧩 4x4 数独是 4×4 网格，按行、列和 2×2 宫填入 1 到 4，每个数字在每行、每列、每宫恰好出现一次。
- 🔢 若把空盘的所有有效填法都算作解，暴力程序得到总数为 288 个。
- 🎲 数字本身没有意义，任何数字置换都视为同一结构；因为有 4! = 24 种置换，所以 288 / 24 = 12 种结构上不同的解。
- 🧠 通过固定第一行为 1 2 3 4，可以一一对应所有结构，程序也验证了确实只有 12 个不同解。
- 🐍 文章用 Python 深度优先搜索暴力枚举所有解，代码很慢但足以处理 4x4 这种小规模。
- 🧮 有效数独谜题要求部分填写后只有唯一解，并且是“最小”的：去掉任意一个给定数字后解就不再唯一。
- 📊 统计得到最小 4x4 谜题共有 85632 个；若把数字置换等价的谜题合并，则只有 3568 个。
- 💡 寻找最小子集时可用位掩码表示子集，子集关系判断为 `bitmask(P) & bitmask(Q) == bitmask(Q)`；由于迭代顺序，只需检查已见过的谜题即可保证最小性。
- 🚫 同样方法无法扩展到 9x9，因为复杂度约为 `O(2^{N^2 · N!})`，计算量远超宇宙年龄。
- 📄 趣味结论：全部 4x4 谜题按 4cm 大小打印约 2247 页，按置换等价后约 102 页；每天一页，全部做完约 7 年，等价版约 102 天。
- ❓ 开放问题包括：为什么不同解对应的最小谜题数量不同，以及能否更优雅地解释 12 = 3×2×2 的结构。
- 🔗 文中还提供了代码仓库、CSV、ASCII/Unicode 格式的全部解与谜题资源。

---

### [Python 3.15 即将改变 Python 🤯 - YouTube](https://www.youtube.com/watch?v=rxaDxyPUoSY&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-763-september-17-2026)

**原文标题**: [Python 3.15 Is About to Change Python 🤯 - YouTube](https://www.youtube.com/watch?v=rxaDxyPUoSY&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-763-september-17-2026)

此內容為 YouTube 網站頁尾的導覽與法律資訊，涵蓋平台介紹、聯絡與創作者資源、廣告與開發者入口、條款與私隱安全，以及功能測試和 2026 年版權聲明。

- 🏢 提供簡介與新聞中心等基本資訊。
- ©️ 包含版權、條款、私隱、政策及安全等法律內容。
- 📞 設有聯絡我們與創作者相關入口。
- 📢 涵蓋刊登廣告與開發人員資源。
- ⚙️ 說明 YouTube 的運作方式與測試新功能。
- © 2026 Google LLC：頁尾顯示 Google 版權標示。

---

### [](https://hugovk.dev/blog/2026/soft-deprecating-re.match/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-763-september-17-2026)

**原文标题**: [Soft-deprecating re.match() · Hugo van Kemenade](https://hugovk.dev/blog/2026/soft-deprecating-re.match/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-763-september-17-2026)

overview summary
本文说明 Python 3.15 将 `re.match()` 软弃用，并新增语义更明确的 `re.prefixmatch()`；核心原因是 `re.match()` 只在字符串开头匹配，容易与 `re.search()`、`re.fullmatch()` 混淆。

- 🐍 Python 3.15 新增 `re.prefixmatch()`，作为 `re.match()` 的别名，明确表示“仅从字符串开头匹配”。
- ⚠️ `re.match()` 是“半锚定”：只在开头匹配，不要求匹配到结尾；例如 `re.match("pi", "pie")` 成功，但 `re.match("pi", "api")` 失败。
- 🔎 `re.search()` 可在任意位置匹配；`re.fullmatch()` 要求整个字符串完全匹配。
- 🧹 `re.match()` 被软弃用：不建议新代码使用，但不会移除、不会发警告，仍会保留文档和测试。
- 🧭 新代码若只想锚定开头，应优先用 `re.prefixmatch()`；否则按需求用 `re.search()` 或 `re.fullmatch()`。
- 🕰️ 为兼容旧版 Python 的代码仍可继续使用 `re.match()`；软弃用不等于硬弃用或未来移除。
- 📊 对比：`re.search()` 无始/尾锚定，1.5 加入；`re.match()` 仅始锚定，1.5 加入；`re.prefixmatch()` 仅始锚定，3.15 加入；`re.fullmatch()` 始尾都锚定，3.4 加入。
- ⚡ 不用特殊字符的写法通常稍快：如 `re.search("pi", s)` 对比 `re.search("^pi", s)` 或 `re.search(r"\Api", s)`。
- 🛠️ 可用 Ruff 的 `TID251` 禁止项目中使用 `re.match()`，并提示改用 `re.fullmatch()` 或 `re.search()`。
- 📚 相关建议：Python 正则中可用 `\A...\z`，而不是 `^...$`；作者 Hugo van Kemenade，发布于 2026-09-10。

---

### [Finch 遇见 MLIR | Quansight Labs](https://labs.quansight.org/blog/finch_meets_mlir?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-763-september-17-2026)

**原文标题**: [Finch meets MLIR | Quansight Labs](https://labs.quansight.org/blog/finch_meets_mlir?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-763-september-17-2026)

本文记录了作者在 finch-tensor 实习期间，为编译器新增 MLIR 后端，并打通 scipy.sparse 与 Finch 张量格式的过程。内容涵盖 MLIR 方言、Finch Assembly IR 的 lowering、缓冲区与控制流实现难点、辅助函数 scansearch、基准测试结果以及未来 GPU 与并行化方向。

- 🧑💻 作者 Yu Sheng Aow 在 Quansight 实习，导师为 Mateusz Sokół，实习项目是为 finch-tensor 实现全新 MLIR 后端。
- 🎯 finch-tensor 原本只支持 CPU，已有 C 与 Numba 后端；MLIR 后端有望扩展到 GPU、SIMD 等更多硬件架构。
- 🧩 MLIR 通过 dialect 表达不同抽象层，文中涉及 arith、memref、scf、llvm、builtin、func 等方言。
- ⚙️ 项目验证 Finch Assembly IR 能否 lowering 到 MLIR，重点测试 Dense MatMul、SpMM 与 SDDMM 三类 kernel。
- 🔍 arith 方言有严格类型检查，float、unsigned int、signed int 使用不同操作，常需用 arith.index_cast 做类型转换。
- 📝 MLIR 采用 SSA 形式，每个值只能赋值一次且不可变，链式运算必须拆成多个新 SSA 值。
- 🧱 缓冲区处理复杂：Finch 缓冲区是嵌套层级的一维内存块，lowering 时需转为 LLVM struct，再 cast 成 memref 读写。
- 🔁 scf 控制流是最大难点之一，scf.if、scf.for、scf.while 都需要处理循环携带变量、作用域字典与新 SSA 生成。
- 🔎 scansearch 是 Finch 的 gallop 协议辅助函数，用于稀疏坐标跳跃匹配；当前硬编码为 memref<?xindex>，i32 索引需转换，已提 issue。
- 🔗 作者还实现了 scipy.sparse 与 finch-tensor 的桥接，asarray 支持 to_scipy 与 from_scipy，并通过模式匹配支持 COO、CSR 等格式。
- 📊 基准测试显示：SDDMM 中 MLIR/Numba 远快于 SciPy，MLIR 多数情况下优于 Numba；Hadamard 与 SpMV 中 SciPy 更好，SpGEMM/SpGEMM2 中 finch-tensor 更优。
- 🚀 未来计划包括 GPU 执行、更多 linalg 方言、scf.parallel 并行化、多线程、稀疏输出分配以及 scansearch 类型变体。
- ✅ 总体而言，MLIR 后端为 finch-tensor 带来更强硬件适配与优化潜力，作者也通过多个 PR 和 issue 留下重要贡献。

---

### [](https://adamj.eu/tech/2026/09/16/django-change-password-url/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-763-september-17-2026)

**原文标题**: [Django: serve the change password well-known URL - Adam Johnson](https://adamj.eu/tech/2026/09/16/django-change-password-url/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-763-september-17-2026)

这篇指南说明如何让 Django 站点支持密码管理器自动发现修改密码页面：添加 `/.well-known/change-password` 重定向到实际改密页，避免暴露管理员等私有页面，并用另一个特殊 well-known URL 检测服务器状态码是否正常，最后通过测试和 `autocomplete` 属性保证安全与可用性。

- 🔐 密码管理器发现密码泄露或复用时，会提示用户改密，但各网站改密 URL 不同。
- 🌐 Web 规范使用保留的 `/.well-known/` 命名空间（RFC 8615），其中 `/.well-known/change-password` 应重定向到真实改密页。
- 🧩 支持的密码管理器包括 Apple iCloud Keychain（Safari 2019）、Google Password Manager（Chrome 86/2020）和 1Password。
- ⚙️ Django 中可在根 URLconf 添加 `RedirectView.as_view(pattern_name="password_change")`，路径为 `.well-known/change-password`，无尾斜杠且无需 `name`。
- 🔁 若使用 `django.contrib.auth.urls`，`password_change` 指向内置 `PasswordChangeView`；若用 django-allauth 可换成 `account_change_password`。
- 🧪 可用 `runserver` 访问 `http://localhost:8000/.well-known/change-password` 测试；部署后应在 HTTPS 生产域名再测，也可用 Chrome 密码检查工具验证。
- 🚫 该功能只用于公共用户的改密页，不要重定向到 Django admin 或其他私有页面，否则会暴露隐藏 URL。
- 🛡️ 第二个保留 URL 是 `/.well-known/resource-that-should-not-exist-whose-status-code-should-not-be-200`，用于检测服务器是否错误地对所有请求返回 200。
- ✅ Django 默认对未匹配 URL 返回 404，通常无需额外实现；但 catch-all 路由可能破坏它，因此应加测试。
- 📝 测试可用 `SimpleTestCase`：断言 change-password 返回 302 且 Location 正确，并用 `resolve` 校验真实视图；另一个测试断言特殊资源 URL 返回 404。
- 🔤 改密表单应设置 `autocomplete="current-password"` 和 `autocomplete="new-password"`；Django 3.0+ 内置 `PasswordChangeForm` 已包含，自定义表单最好继承它或手动设置。
- 🎯 总结：只需添加一个 URL 条目，密码管理器就能把用户引导到改密页，降低泄露密码风险。

---

### [](https://www.bentasker.co.uk/posts/blog/general/playing-with-an-eink-badge.html?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-763-september-17-2026)

**原文标题**: [Playing with a Badgeware Badger | www.bentasker.co.uk](https://www.bentasker.co.uk/posts/blog/general/playing-with-an-eink-badge.html?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-763-september-17-2026)

作者为了缓解倦怠、重拾技术热情，入手 Badgeware Badger 电子墨水名牌并记录从连接到定制、排错的完整过程。Badger 基于 2.7 英寸电子墨水屏和 Raspberry Pi RP2350，运行 MicroPython；作者通过 USB 大容量存储模式修改应用、添加 fediverse 社交图标与头像，并解决字号、图片颜色与对比度问题，最终成功显示，还计划开发 GitHub 宕机检测和 Home Assistant 垃圾桶提醒等 WiFi 应用。

- 🧪 作者为摆脱倦怠、重新激发技术兴趣，开始寻找可折腾的小硬件项目。
- 🏷️ Badgeware Badger 是一款 2.7 英寸电子墨水名牌，搭载 Raspberry Pi RP2350，并预装 MicroPython。
- 🔌 连接电脑时插入 USB，双击 Reset 按钮即可进入 USB 大容量存储模式；但可用空间很小，约 12MB。
- 📁 根目录包含 `apps`、`assets`、`main.py` 和 `secrets.py`；`secrets.py` 用于配置 WiFi、地区与时区。
- 🚀 `main.py` 是入口文件，默认启动 `/system/apps/menu`，HOME 按钮可退出到启动器，菜单本身也被实现为一个应用。
- 🧩 `apps` 目录中有 `badge`、`clock`、`hydrate`、`mass_storage`、`menu`、`the_compendium` 等应用，菜单会扫描目录并读取 `icon.png`。
- 👤 `badge` 应用在 `__init__.py` 中硬编码头像、姓名、职位和社交账号，且预置了大量社交网络图标，包括 Mastodon。
- 🌐 作者尝试添加 fediverse 图标，使用 fedigram，并设置自己的头像、姓名和 Mastodon 账号。
- 🔤 社交账号文字过长：作者改用更小的像素字体 `rom_font.corset`，因为原有像素字体无法缩小。
- 🖼️ 图片不显示：问题涉及色彩空间、位深、透明度和对比度；最终通过 ImageMagick 转为 8-bit、PNG32、合适尺寸，并用 `-fill '#464646' -colorize 100` 加深颜色修复。
- ✅ 修复后，头像、fediverse 图标和社交信息都能正常显示在 Badger 上。
- 🔮 未来计划利用 WiFi 支持，制作“GitHub 是否宕机”应用，并与 Home Assistant 集成做垃圾桶日提醒。
- 💡 作者认为这次深入排错正符合购买 Badge 的初衷：在“跟魔法盒子说话”的时代重新训练大脑解决问题。

---

### [FastHTML - 用纯 Python 构建 Web 应用！ - YouTube](https://www.youtube.com/watch?v=Ck0w7zqshjU&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-763-september-17-2026)

**原文标题**: [FastHTML - Build Web Apps in Pure Python! - YouTube](https://www.youtube.com/watch?v=Ck0w7zqshjU&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-763-september-17-2026)

這是 YouTube 頁面底部的導覽與法律資訊清單，涵蓋平台介紹、聯絡方式、創作者與商業資源、法律條款、私隱與安全政策、平台運作說明及測試功能，並標示 2026 Google LLC 版權聲明。

- ℹ️ 基本資訊：簡介、新聞中心
- ⚖️ 法律與政策：版權、條款、私隱、政策及安全
- 📞 聯絡與支援：聯絡我們
- 🎬 創作者與商業：創作者、刊登廣告
- 👨‍💻 開發資源：開發人員
- ⚙️ 平台運作與更新：YouTube 的運作方式、測試新功能
- ©️ 版權歸屬：© 2026 Google LLC

---

### [漫漫长路的最后一英里：浏览器中更快的 NumPy | Notebook.link](https://notebook.link/blog/the-last-mile-faster-numpy/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-763-september-17-2026)

**原文标题**: [The last mile of a long road: faster NumPy in the browser | Notebook.link](https://notebook.link/blog/the-last-mile-faster-numpy/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-763-september-17-2026)

Emscripten-forge 现已让浏览器中的 NumPy 链接 WebAssembly 版 OpenBLAS，显著加速矩阵乘法与线性代数；OpenBLAS 0.3.34 进入主渠道，0.3.35 实验包和可选 Relaxed SIMD 进一步提升，并推动 Fortran 与科学计算栈在 WebAssembly 上成熟。

- 🧱 Emscripten-forge 是面向 WebAssembly 的语言无关 conda 发行版，重建编译器、运行时和共享库，支持 Python、R、C++、OCaml、Lua 等。
- 🐍 此前浏览器中的 NumPy 没有加速 BLAS，`np.matmul`、`@`、`np.linalg` 回退到普通 C 循环，缺乏缓存与 SIMD 优化。
- ⚡ 现在 Emscripten-forge 的 NumPy 2.5.3 链接 OpenBLAS 0.3.34，并启用 WASM SIMD；在 `n=1024` 方阵 `np.matmul` 上相对无 BLAS 提升约 30.92×（float32）和 14.90×（float64）。
- 🧮 OpenBLAS 提供 BLAS Level 1/2/3 与 LAPACK；`np.matmul` 等由 GEMM 主导，`np.linalg` 多数最终调用 LAPACK。
- 🛠️ 将 Fortran 带到 wasm32 是关键：借助 Flang/LLVM 补丁及 Ian Thomas 对 OpenBLAS 的 Emscripten 适配，解决 WebAssembly 更严格调用约定等问题。
- 📦 打包模型类似“WebAssembly 的 conda-forge”：OpenBLAS 是独立 conda 包，NumPy 运行时动态链接 `libopenblas`，升级 OpenBLAS 无需重建 NumPy，也可惠及 SciPy、scikit-learn、xtensor-blas 等。
- 📈 OpenBLAS 0.3.34 对矩阵乘积增益最大；部分 `np.linalg` 提升 1.08–1.65×；`A @ x` 与向量 `np.dot` 因缺少快速列主序 GEMV 仍接近 1×。
- 🚀 OpenBLAS 0.3.35（实验，SIMD128）增加 WASM SIMD 内核：`n=1024` 的 `np.matmul` 比 0.3.34 再提升 1.79×（float32）和 1.41×（float64），`A @ x` 从约 4 GFLOPS 提升到 23.1 GFLOPS（float32）。
- 🧬 可选 Relaxed SIMD 构建可利用 FMA：在 Chromium 153 上，`n=1024` 的 `np.matmul` 比便携 0.3.35 再提升 1.17×（float32）和 1.43×（float64）；Chrome ≥114、Firefox ≥146 支持，Safari 需开启 JavaScriptCore 标志。
- 🏁 从无 BLAS 到 0.3.35 + Relaxed SIMD 的端到端 `np.matmul`，在 `n=1024` 达到约 64.89×（float32）和 30.07×（float64）提升。
- 💻 使用方式：主渠道安装 `numpy` 即拉取 OpenBLAS 0.3.34；OpenBLAS 0.3.35 位于 `emscripten-forge-4x-experimental`，可选 `simd128` 或 `relaxed_simd` 构建，后者可移植性较差。
- 🌍 结论：改进已上游到 OpenBLAS 并作为可分发 conda 包发布，其他 WebAssembly Python 栈（如 Pyodide）采用相同构建与 Fortran 工具链后也可受益。

---

### [错误](https://ankit-rana.com/logs/49-jitter-synchronised-clients/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-763-september-17-2026)

**原文标题**: [Error](https://ankit-rana.com/logs/49-jitter-synchronised-clients/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-763-september-17-2026)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='ankit-rana.com', port=443): Read timed out. (read timeout=30)

---

### [](https://github.com/petergyang/no-ai-slop?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-763-september-17-2026)

**原文标题**: [GitHub - petergyang/no-ai-slop: Removes 20+ patterns of AI slop from any piece of writing. · GitHub](https://github.com/petergyang/no-ai-slop?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-763-september-17-2026)

这是一个名为 No AI Slop 的开源项目，旨在帮助写作者从文本中清除 20 多种“AI 味”模式，同时保留个人声音和风格。

- 🤖 **项目定位**：GitHub 仓库 petergyang/no-ai-slop，获得 10.4k 星标和 726 次复刻，采用 MIT 许可证
- ✍️ **核心问题**：AI 让写作变得千篇一律，编辑时还会抹掉个人词汇、节奏、幽默和不完美之处
- 🛠️ **安装方式**：可粘贴指令到 ChatGPT、Claude Code、Codex 等工具全局安装，或用 npx 命令安装
- ✂️ **编辑写作**：输入 /no-ai-slop 加文本，即可移除 AI 味模式、保留个人声音并列出修改内容
- 🔍 **检测功能**：可检测文本中的 AI 味模式，逐条引用而不断言是否由 AI 生成
- 🎭 **趣味生成**：可用该技能生成最尴尬的 AI 味文本作为讽刺练习
- 📋 **检测模式**：涵盖二元对比、清嗓子开场、伪洞察铺垫、冒号揭示、戏剧性碎片、肤浅分析、重要性吹捧、模糊归因、同义词循环、伪深刻结尾等 20 多种
- 📐 **基础检查**：还会检查开门见山、主动语态、句子通顺度、具体细节优先于抽象表达
- 📁 **文件构成**：包含 SKILL.md 编辑规则、eval.md 检查项、plugin.json 插件元数据和 build_plugin.py 构建脚本
- 🔌 **插件支持**：已作为插件在 ChatGPT 中可用
- 🔗 **延伸资源**：作者提供 Behind the Craft 个人 AI 系统、YouTube 频道和 newsletter 等实用教程

---

### [](https://github.com/cayu-dev/cayu?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-763-september-17-2026)

**原文标题**: [GitHub - cayu-dev/cayu: Cayu is the runtime for long-horizon agents that need explicit environments, durable sessions, controlled tools, secrets boundaries, evals, and replay · GitHub](https://github.com/cayu-dev/cayu?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-763-september-17-2026)

Cayu 是一个用 Python 构建和运行 AI 代理的生产级代理运行时，提供对代理完整执行生命周期的控制，包括上下文组装、模型与工具调用、状态持久化、权限治理、故障恢复以及行为观测与评估。

- 🏗️ **核心定位**：Cayu 是面向长时间跨度、高影响任务的代理运行时，应用可直接组合其运行时原语，无需额外的工作流引擎，同时保留对 UI、认证、领域逻辑和业务工作流的控制权
- 🔬 **诞生背景**：从支撑数千个业务应用构建与部署的代理软件工厂生产环境中提炼而来，团队曾使用 Claude Agent SDK、Mastra、LangGraph 等框架，但生产质量需要对循环本身及周边能力有更深的控制
- ⚠️ **解决的生产痛点**：进程在副作用后、状态记录前崩溃；模型请求了权限错误的工具；运行中途需人工输入或审批；上下文膨胀导致提供商拒绝请求；重试/分叉/子代理丢失成本与因果归因；评估只看最终文本而忽略运行时轨迹
- 🧩 **核心原语对照**：长期任务→持久会话/转录/事件/恢复/分叉；安全副作用→类型化工具/效果声明/策略/审批/幂等键；人工交互→用户输入检查点/审批解决；上下文压力→Token 计数/投影/压缩；成本控制→用量事件/运行限制/预算；执行边界→环境/工作区/运行器/工件/保险库/出站
- 🚀 **快速开始**：`pip install cayu pytest && cayu new myagent`，脚手架无凭证依赖，包含仅组合的 `app.py`、`build_app()` 工厂、单模型代理、完整的提示词/工具/策略/环境等目录、密封的运行时测试与输出评估
- 💻 **编码代理预设**：`cayu new mycoder --preset coding` 提供带文件与 Git 工具、持久知识、后台评审委托和人工输入的编码入门模板，可选 Docker 执行与远程 Git/GitHub 交付能力
- 🧠 **心智模型**：`AgentSpec` 定义身份与模型配置；`Environment` 定义可触碰资源；`Session` 记录持久执行与血缘；`Tool` 是应用拥有的显式注册能力；`Task` 是可选的持久后台工作单元；`Workflow` 是围绕代理步骤的确定性编排
- 🛡️ **执行面选择**：原生 Python 工具运行于可信应用进程；进程隔离宿主工具提供硬墙钟时限；运行器支持的操作由选定运行器提供隔离保证；MCP 工具独立集成边界；虚拟出站可让真实凭证不进入工作负载
- 📦 **可选功能扩展**：`cayu[server]`（FastAPI 控制面）、`cayu[postgres]`、`cayu[aws]`（Bedrock）、`cayu[vertex]`、`cayu[e2b]`、`cayu[microsandbox]`、`cayu[egress]`、`cayu[otel]` 等，`cayu[all]` 不包含浏览器验证工具
- 🔌 **提供商灵活性**：内置 OpenAI、Anthropic、OpenAI 兼容 HTTP 及实验性 OpenAI 订阅适配器，重点关注 OpenAI、Anthropic、OpenRouter、Google、Bedrock 和 Vertex，支持通过 `cayu auth openai login` 使用 ChatGPT 订阅进行本地开发
- ☁️ **Cayu Cloud 部署**：云命令与 `cayu` 包一同发布，目前仅限邀请，登录使用 WorkOS 设备授权，`cayu cloud deploy` 将本地目录打包为不可变源包上传，无需 GitHub 或干净工作树
- 🖥️ **控制面开放可替换**：支持捆绑的编译仪表盘、弹出 React/TypeScript 源码进行自定义，或基于版本化控制面 API 提供完全自定义 UI，`cayu dashboard eject` 仅使用包数据无网络请求
- 🔒 **生产边界明确**：原生工具是可信宿主进程代码，`ToolPolicy` 不是操作系统隔离边界；本地运行器无沙箱隔离；SQLite 适合单写入者，多进程用 PostgreSQL；FastAPI 控制面需显式访问策略，面向多用户产品需独立客户授权边界
- 📚 **文档与示例**：提供快速参考（`cayu guide authoring#cayu-map`）、运行时契约、评估指南、成本优化等，示例涵盖领域工具、本地环境、服务器、云 PR 审查、业务审批、虚拟出站 GitHub CLI 及高级运行时策略
- 📄 **许可证**：采用 Apache License 2.0，安全漏洞请按 `SECURITY.md` 私下报告

---

### [](https://github.com/moio9/NFS-Online-Server?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-763-september-17-2026)

**原文标题**: [GitHub - moio9/NFS-Online-Server: NFS MW, UG2 and Carbon online server emulator. · GitHub](https://github.com/moio9/NFS-Online-Server?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-763-september-17-2026)

这是一个面向《极品飞车：地下狂飙 2》《极品飞车：最高通缉（2005）》和《极品飞车：碳化》的非官方社区联机服务器项目，同时提供 Windows x86 客户端插件；服务器用 Python 编写，客户端 ASI 插件由 Zig 源码构建，不包含原版游戏文件。

- 🎮 为《Need for Speed: Underground 2》《Most Wanted (2005)》《Carbon》提供非官方在线服务器和客户端插件。
- 🐍 服务器基于 Linux、Python 3.10+ 和 sqlite3，使用单一 TOML 配置文件。
- 🧱 三个 ASI 客户端从 Zig 源码构建，需要 Linux x86-64 或 Termux、Zig 0.16.0、Python 3 和 file。
- 🚀 快速开始流程包括克隆仓库、运行 check、configure、create-account，然后用 start.sh 启动。
- 🛠️ 常用命令包括 status、stop、start、kick、dlc、stats，可用 `--help` 查看完整命令列表。
- 🌐 公共服务器地址为 `brake.go.ro`；部署前需修改 `PUBLIC_HOST`。
- 🔐 Messenger IPC 和独立 DLC 监听默认绑定回环地址，除非置于受保护的反向代理之后。
- 🔌 默认端口覆盖 Messenger、U2、Most Wanted、Carbon 的 TCP/UDP 服务；只应开放实际运行游戏所需的端口。
- 🧩 构建产物为 `net_u2.asi`、`net_mw.asi`、`net_carbon.asi`，需与对应 INI 放入游戏的 ASI/插件目录。
- ⚠️ 不要与修改同一游戏代码的旧插件同时加载。
- 🗺️ 路线图包括错误修复、协议工作、排行支持、配置选项、文档和整体优化，详见 `TODO.md`。
- ✅ 测试使用 unittest；发布前还需运行 `tools/check_public_tree.py` 和 `nfs_online.py check`。
- 📜 原项目代码采用 AGPL-3.0-or-later 许可；EA 及相关名称是 Electronic Arts 的商标，本项目为非官方项目。
- 💰 支持方式包括 Monero、Bitcoin、Ethereum 和 PayPal。
- ⭐ 仓库当前约有 35 stars、6 forks，主要目录包括 server、clients、config、data、tests、tools 等。

---

### [](https://github.com/timgordontg/engrim?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-763-september-17-2026)

**原文标题**: [GitHub - timgordontg/engrim: The Universal Cross-Model Episodic Memory Standard. Local-first, project-scoped SQLite engine for Google Antigravity, Claude Code, Cursor, Codex CLI, and OpenCode. Zero cloud lock-in. · GitHub](https://github.com/timgordontg/engrim?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-763-september-17-2026)

Engrim 是面向 AI 编码代理的通用跨模型、跨代理情景记忆标准，以本地优先、项目级 SQLite 数据库（~/.engrim/memory.db）保存架构决策、事实、反馈、状态等，让开发者在 Google Antigravity、Claude Code、Cursor、Codex CLI、OpenCode、Windsurf 之间自由切换而不丢失项目上下文。

- 🧠 核心价值：用约 4,000 字符（<1,000 token，<1% 上下文）的高精度记忆包，替代每轮重放 15 万 + token 原始对话，缓解注意力稀释与 token 膨胀。
- 🔄 Continue-as-Clear：可随时 `/clear`，下一次会话从 `memory.db` 恢复决策、活跃状态和 `[▶ RESUME HERE]` 指针，实现零上下文丢失。
- 🗄️ 架构：包含适配器与生命周期钩子、健康诊断、来源追踪、混合检索；存储使用 SQLite WAL、FTS5 全文搜索、model2vec 静态向量嵌入和 flight recorder 日志。
- 🤝 多代理支持：通过 hooks、MCP stdio、插件等集成 Antigravity、Claude Code、Cursor/Windsurf、Codex CLI、OpenCode；`engrim setup` 可自动检测并配置。
- 🩺 诊断与自愈：`engrim doctor`、`--fix`、`--json` 可检查数据库完整性、语义召回、各代理钩子，并提供跨 OS/路径迁移的便携 PATH 回退。
- 🧩 MCP 工具：`engrim_recall` 混合检索、`engrim_add` 写入持久记忆、`engrim_context` 获取启动记忆包、`engrim_review` 清理前检查未捕获决策。
- 🛠️ CLI 覆盖：`add`、`recall`、`context`、`doctor`、`hook`、`setup`、`serve`、`review`、`prune`、`list`、`project(s)`、`supersede`、`retire`、`sync`、`merge`、`backup` 等完整工作流。
- 🧪 实证：在 5 万行算法交易系统上连续测试 105 个会话，15.3 万 token 工作压缩到 <1,000 token，重载上下文成本降低 99%+，186 个单元测试零回归。
- 🏷️ 来源追踪：每条记忆记录 `origin_agent`（antigravity、claude-code、cursor、opencode、cli、user），并在 `engrim context/list` 中显示；旧库通过 `ALTER TABLE` 非破坏性迁移。
- 🔐 隐私安全：100% 本地离线，无遥测、云同步或追踪；CPU-only model2vec，SQLite 文件使用 POSIX 0600，`*.db` 默认 gitignore。
- 🆚 对比优势：相比 gbrain 更轻量本地、无需云或守护进程；相比 OpenCode/Codex 内置存储仅限单工具 transcript，Engrim 是跨工具情景记忆层；相比个人伴侣工具，专注软件工程决策与约束。
- 🏢 开源与商业：MIT 开源版面向个人开发者与本地代理；企业版面向团队/CI/CD，提供 In-VPC 状态收集、多租户语义搜索、密钥/PII 清理、Merkle 合规账本等。
- 👤 项目信息：作者 Tim Gordon（@timgordontg），网站 engrim.dev，GitHub `github.com/timgordontg/engrim`，MIT © 2026；仓库约 276 stars、15 forks、82 commits。

---

### [](https://github.com/SnailSploit/Claude-Red?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-763-september-17-2026)

**原文标题**: [GitHub - SnailSploit/Claude-Red: claude-red is a curated library of offensive security skills designed for the Claude skills system. Each skill is a structured SKILL.md file that primes Claude with expert-level methodology for a specific attack surface — from SQLi to shellcode, EDR evasion to exploit development. · GitHub](https://github.com/SnailSploit/Claude-Red?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-763-september-17-2026)

Claude-Red 是 SnailSploit 维护的开源进攻性安全技能库，面向 Claude Skills 系统。每个技能都是结构化 SKILL.md，按需加载，让 Claude 针对特定攻击面呈现专家级红队方法论；适用于授权红队、漏洞赏金、安全研究、CTF、操作员培训与攻击面探索。

- 🧠 核心理念：给 Claude 正确技能，它就从聊天机器人变成操作员；技能包含技术、工具、边缘情况与升级路径。
- ⚡ 自动触发：根据对话关键词加载匹配技能，未使用技能不占上下文；例如提到 SQL 注入会加载 offensive-sqli。
- 🚀 快速安装：克隆到 ~/.claude/skills/claude-red；支持稀疏检出单类、Claude Code 管道、Claude.ai 手动粘贴及 install.sh 交互安装。
- 🗂️ 分类规模：覆盖 23+ 类别，目标约 130 个技能；当前含 Web、认证、AD、无线、云、移动、IoT、红队基础设施等。
- 🕸️ Web 应用 16 项：SQLi、XSS、SSRF、SSTI、XXE、IDOR、文件上传、RCE、反序列化、竞态、请求走私、GraphQL、WAF 绕过、业务逻辑等。
- 🔐 认证与身份：JWT 攻击（alg:none、密钥混淆、爆破）、OAuth/OIDC 滥用（重定向 URI、令牌泄露、PKCE 绕过）。
- 🏢 Active Directory：Kerberoast、ASREProast、ACL 滥用、ADCS ESC1-15、委派、混合 AAD 攻击方法论。
- 📡 无线 14 项：802.11、WPA2-PSK、WPA3-SAE、802.1X/EAP、WPS、邪恶双胞胎、KRACK/FragAttacks、BLE、经典蓝牙、Zigbee/Thread/Matter、Z-Wave、LoRaWAN/Sub-GHz。
- ☁️ 云与移动/IoT：多云提权、IMDS 滥用、跨账号跳板；Android/iOS Frida、证书固定绕过；硬件、固件、RTOS、ICS/OT、MQTT/CoAP。
- 🛡️ 基础设施与红队 7 项：初始访问、EDR 规避、shellcode、Windows 缓解与边界绕过、高级红队全杀伤链。
- 💥 漏洞利用开发 6 项：栈/堆破坏、ROP、缓解绕过、崩溃分析、TOCTOU；模糊测试 4 项：libFuzzer、AFL++、覆盖率引导、漏洞分类。
- 🔎 其他领域：侦察/OSINT、API 安全、容器逃逸与 K8s 攻击、CI/CD 流水线与密钥、密码学/TLS、Linux/Windows 提权、横向移动/持久化/数据外泄。
- 🕵️ 更多类别：反取证、C2 框架、供应链攻击/依赖混淆、钓鱼与社工、网络层攻击、AI 安全（提示注入、越狱、RAG 投毒）、快速检查与专业报告。
- 🗺️ 路线图：9 个阶段；无线、文档/工具、新类别、深度重写已完成；AD/Windows、云身份、IoT、Web 基础/高级等计划中。
- 🤝 开源信息：MIT 许可，欢迎贡献；作者 Kai Aizen（SnailSploit），原始清单来自 Sahar Shlichov；约 6k stars、775 forks、43 watchers、34 commits。

---

### [](https://github.com/jordan-gibbs/hyperresearch?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-763-september-17-2026)

**原文标题**: [GitHub - jordan-gibbs/hyperresearch: Agent-driven research knowledge base. Agents collect, search, and synthesize web research into a persistent, searchable wiki. · GitHub](https://github.com/jordan-gibbs/hyperresearch?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-763-september-17-2026)

Hyperresearch 是一个将 Claude Code 变成深度研究代理的开源项目，通过可扩展的 16 步流水线，从单一提示生成带完整来源溯源、引用核查和对抗式审计的研究报告，并把所有读过的来源沉淀为可搜索、可复用的知识库。

- 🧠 **定位**：把 Claude Code 变成深度研究代理，号称在 DeepResearch-Bench RACE 榜单领先，但为内部基准、第三方验证待定。
- ⚙️ **流程**：16 步流水线覆盖查询分解、宽度扫描、矛盾图、深度调查、三重草稿、合成、四路批评、补丁、引用核查、润色与可读性审计。
- 🎚️ **规模分层**：light 约 30–40 分钟；full 约 1.5–2.5 小时；dissertation 约 4–8 小时，产出 25K–80K 词、300–450 个来源。
- 🔧 **配置齿轮**：premier/full 等 profile 可调来源目标、深度预算、草稿数、每代理模型等，并按项目持久化。
- 🗣️ **报告模式**：register、domain_notes、inference_depth 等杠杆决定报告语气、领域策略和推理深度。
- 🔍 **学术检索**：`hpr scholar search` 一次查询 OpenAlex、Crossref、CORE、DOAB、ClinicalTrials.gov、SEC EDGAR、FRED 等并去重。
- ✅ **引用验证**：逐条检查引用与句子绑定；幻觉引文、未披露撤稿、引文不支持句子都会阻止发布。
- 🧾 **来源独立性**：聚类联合发布和转载副本，避免同一新闻稿的多个副本被当作多个独立证据。
- 🛡️ **对抗审计**：四名批评者并行攻击草稿；补丁器被工具锁定为 Read+Edit，只能做外科式修改，不能重写报告。
- 📚 **开放获取**：通过 Unpaywall、Europe PMC、CORE 寻找合法 OA 全文；若正文来自替代来源或“救援”来源，会明确披露。
- 🗃️ **持久保险库**：来源以 Markdown+SQLite 保存，支持全文/语义搜索、图谱、去重、生命周期管理和未来会话复用。
- 💾 **运行管理**：每次运行有隔离工作区与 manifest，支持断点续跑、预算上限、状态报告和发布前验证。
- 🧩 **子代理体系**：fetcher、source-analyst、loci/depth-investigator、critics、draft-orchestrator、synthesizer、patcher、cite-checker 等可配置。
- 🔐 **安全边界**：网页正文放入 `<untrusted-source>` 围栏并按数据处理，防止提示注入，URL 也会校验。
- 🌐 **网页提供方**：支持 builtin、crawl4ai、exa、tavily、parallel、serply；可登录抓取，受阻请求进入浏览器升级队列。
- 🧱 **结构强制**：原始提示为教条、locus 覆盖、补丁专属修改、引用原文必须存在于 vault、撤稿阻断发布等均有 lint/验证约束。
- 📦 **安装使用**：`pip install hyperresearch && hyperresearch install`，在 Claude Code 中用 `/hyperresearch`；支持 Python 3.11–3.13，MIT 许可。
- ⚠️ **限制**：不替代来源判断，无法绕过未登录付费墙，依赖 Anthropic 模型，lint 只抓结构性问题，事实准确性仍需人工负责。

---

### [](https://github.com/IMvision12/ZeroModels?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-763-september-17-2026)

**原文标题**: [GitHub - IMvision12/ZeroModels: ZeroModels: Open-source Keras 3 collection of pretrained models across Vision, LLM, VLM, Depth, Speech, and more · GitHub](https://github.com/IMvision12/ZeroModels?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-763-september-17-2026)

ZeroModels 是 IMvision12 开发的开源 Keras 3 预训练模型集合，将 timm、transformers、diffusers 等来源的 PyTorch 权重转换为 Keras，覆盖文本、视觉、多模态、音频等广泛任务，并提供安装说明、详细文档、模型清单、许可证与引用信息。

- 📦 **安装方式**：可通过 PyPI 安装 `pip install -U zeromodels`，也可从 GitHub 源码安装。
- 📚 **文档完善**：提供官网文档和 `docs/` 源码，涵盖架构说明、用法示例、预训练权重与真实模型输出；分类骨干模型共享同一文档页。
- 📝 **文本模型**：包含文本编码器与掩码语言模型，如 BERT、ModernBERT、ELECTRA、RoBERTa、XLM-RoBERTa、DeBERTa 系列、T5、BART。
- 🤖 **文本大模型**：支持 Qwen、GPT、Llama、Mistral、Mixtral、DeepSeek、Gemma、MiniMax、GLM 等系列，多数权重来自 `transformers`，部分为 gated。
- 👁️ **视觉骨干**：覆盖 BEiT、CaiT、ConvNeXt、DeiT、DenseNet、EfficientNet、Inception、LeViT、MaxViT、MobileNet、MobileViT、PVT、RegNet、ResNet、Swin、VGG、ViT、Xception 等。
- 🎯 **视觉任务**：包括目标检测、分割、特征提取和单目深度估计；检测有 DETR、RT-DETR、RF-DETR、OWL-ViT、Grounding DINO 等，分割有 DeepLabV3、MaskFormer、OneFormer、SAM 系列、SegFormer 等。
- 🖼️ **多模态模型**：包含视觉语言编码器如 CLIP、MetaCLIP 2、SigLIP、SigLIP2、TIPSv2，多模态 LLM 如 Qwen-VL、InternVL3、Gemma、Mistral、DeepSeek-VL、Janus-Pro、GLM-4V/4.5V、Kimi 等。
- 🎨 **文生图扩散**：支持 Stable Diffusion 1.x、2.x、XL、3、3.5 等版本，权重来自 `diffusers`。
- 🔊 **音频模型**：包含语音识别模型 Whisper、Speech2Text、Moonshine、Granite Speech 5，以及语音 LLM Granite Speech、Granite Speech Plus。
- ⚖️ **许可证与来源**：ZeroModels 代码采用 Apache 2.0；转换权重保留上游许可证，例如 Stable Diffusion 为 OpenRAIL-M，SDXL-Turbo 为非商业许可。
- 🙏 **致谢与引用**：项目基于 Keras、Transformers、timm、Diffusers，并提供 BibTeX 引用；GitHub 页面显示约 34 stars、2 forks。

---

### [](https://github.com/hermes-labs-ai/lintlang?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-763-september-17-2026)

**原文标题**: [GitHub - hermes-labs-ai/lintlang: Static analysis for AI agent configs, tool descriptions, and system prompts — catches vague tool descriptions, missing stop conditions, and schema gaps before they reach runtime. Zero-LLM, deterministic checks, built for CI. · GitHub](https://github.com/hermes-labs-ai/lintlang?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-763-september-17-2026)

LintLang 是 Hermes Labs 维护、Apache-2.0 许可的静态分析工具，用于在运行时之前检查 AI agent 的自然语言指令、工具描述、系统提示和配置，以零 LLM、确定性、本地方式发现歧义、缺失限制与冲突指令。

- 🧰 核心用途：静态分析 AI agent 配置、工具描述与系统提示，运行前捕获模糊工具、缺失停止条件、无界重试、schema 与描述不一致等问题。
- 🔒 零 LLM 与本地确定性：默认检查不调用 LLM、API、遥测或网络；安装后每次扫描离线、可复现，适合 CI。
- ⚙️ 快速开始：需要 Python 3.10+；可用 `python -m pip install lintlang`、`uvx lintlang scan AGENTS.md` 或 `pipx install lintlang`。
- 🧪 示例扫描：对 `samples/bad_tool_descriptions.yaml` 报告 `FAIL — 1 CRITICAL, 2 HIGH, 7 MEDIUM, 3 LOW`，包括 H1.1 无描述、H1.2 描述过短、H1.6 工具间无区分。
- 🚦 CI 闸门：默认只报告 findings 并退出 0；`--fail-on fail` 阻止 HIGH/CRITICAL，`--fail-on review` 阻止 MEDIUM 及以上；无法扫描的输入始终非零。
- ✅ 判定含义：PASS 表示所选检查后无 MEDIUM+；REVIEW 表示仍有 MEDIUM；FAIL 表示有 HIGH/CRITICAL；ERROR 表示请求输入无法检查。
- 🔁 基线管理：`--write-baseline` 与 `--baseline` 可记录已审阅存量，同时阻止新增 MEDIUM+ 发现，无需禁用整条规则。
- 🧩 CI 与集成：提供 GitHub Action、SARIF/JSON、pre-commit、MegaLinter `AI_LINTLANG`、Claude Code 插件、Gemini CLI 扩展，以及 Hermes Agent `pre_verify` 钩子。
- 📂 可检查输入：JSON/YAML 顶层 agent 字段（`system_prompt`、`instructions`、`tools`、`functions`、`messages` 等）、`.txt`/`.md`/`.prompt` 文件，以及 Python AST 中的提示字符串和阈值。
- 🔍 检测范围：H1-H7 覆盖工具清晰度、执行边界、schema-描述对齐、上下文边界、指令具体性、输出契约、消息角色结构；Python 管道问题为 P1/P2。
- ⚖️ H1.6 工具差异：逐对比较工具描述，报告 mutual/domination，属 MEDIUM；不触发 `--fail-on fail`，受有限英语同义词表限制，无发现不等于不存在。
- 🧭 定位边界：介于语法/schema 验证与运行时评估之间，用于编写和 PR 审查；不证明指令正确、不观察工具选择、不证明运行时失败、不认证安全，也不替代运行时评估与人工审查。
- 📜 项目信息：Apache-2.0 许可，由 Hermes Labs 维护；列于 MegaLinter 外部插件目录、awesome 列表、Software Heritage 和 Research Software Directory；相关技术说明 DOI 为 `10.5281/zenodo.21817243`。
- 🧠 同实验室工具：zer0dex、little-canary、fidelis、quick-gate-js/quick-gate-python 等，面向 agent 记忆、提示注入检测和 CI 质量门。

---

### [](https://github.com/anuj0456/OpenArch?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-763-september-17-2026)

**原文标题**: [GitHub - anuj0456/OpenArch: PyTorch implementations of modern open-source LLM architectures (Llama, Qwen, DeepSeek, Gemma, GPT-OSS, Kimi, and more) — written from scratch for readability and learning, based on Sebastian Raschka's LLM Architecture Gallery. · GitHub](https://github.com/anuj0456/OpenArch?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-763-september-17-2026)

OpenArch 是由 anuj0456 维护的公开 GitHub 项目，目标是用 PyTorch 从零实现现代开源 LLM 架构，强调可读性与学习，而非与 transformers 等生产库竞争。它参考 Sebastian Raschka 的 LLM Architecture Gallery，覆盖文本、多模态和图像模型，并欢迎社区贡献。

- 📊 仓库数据：387 stars、32 forks、3 watchers、104 commits，1 个 issue。
- 🧭 核心理念：每个架构一个可读的 model.py，显式展示 attention、normalization、MoE 路由、位置编码等关键设计。
- 🎯 目标范围：对应 LLM Architecture Gallery 中的 72 个架构，用 ✅ 表示可前向运行，🚧 表示建设中。
- 📚 已实现文本模型：GPT-2 XL、Llama 2/3、OLMo 2、DeepSeek R1、Gemma 3、Mistral 3、Llama 4 Maverick、Qwen 3、Kimi K2、GLM 4.5、GPT-OSS 等。
- 🧪 开发中模型：Grok-2.5、Qwen3 多模态、Dall-e 等。
- 🔍 架构差异关注：MHA/GQA/MQA/MLA、滑动窗口、线性/DeltaNet 混合、RMSNorm/QK-Norm、RoPE/NoPE/YaRN、稠密/稀疏 MoE、MTP 等。
- 📁 仓库结构：text/ 与 multimodal/ 按模型分文件夹，各含 model.py 和 README.md。
- 🤝 贡献方向：实现缺失模型、补充架构文档、添加前向权重测试、修复 bug/重构；大工作先开 issue，优先可读性。
- 🙏 参考与致谢：主要来自 Sebastian Raschka 的 Gallery/对比系列/LLMs From Scratch，以及 Machine Learning Mastery。
- ⚠️ 免责声明：仅供学习，非官方实现；生产使用建议选择官方实现或 transformers。
- 📜 许可证：README 写 Apache License 2.0，仓库页面显示 MIT license，具体各模型遵循原模型许可。

---

### [](https://github.com/reconurge/flowsint?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-763-september-17-2026)

**原文标题**: [GitHub - reconurge/flowsint: A modern platform for visual, flexible, and extensible graph-based investigations. For cybersecurity analysts and investigators. · GitHub](https://github.com/reconurge/flowsint?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-763-september-17-2026)

Flowsint 是 reconurge 维护的开源 OSINT 图谱调查工具，面向合法、透明、可验证的调查场景，通过可视化图谱与自动富化器探索域名、IP、组织、人物、邮箱、电话、加密钱包等实体关系。

- 🛡️ 强调道德与合法使用，适用于网络安全研究、记者/OSINT 调查、执法/反欺诈、组织威胁情报等合规场景。
- 🚫 禁止用于未授权入侵、监控、骚扰、人肉、政治操纵、虚假信息或侵犯隐私。
- ⭐ GitHub 项目约 8.8k stars、1.1k forks，采用 Apache-2.0 许可，仍处早期开发并欢迎社区贡献。
- 🐳 快速安装需 Docker；Linux/macOS 可运行 `make prod`，Windows 可用 `docker compose -f docker-compose.prod.yml up -d`，无需本地构建。
- 🔐 首次访问 `http://localhost:5173/register` 创建账户，无默认凭据；数据保存在本机，适合重视隐私的 OSINT 调查。
- 🌐 团队/服务器部署时，前端提供 UI 并内部代理 API，只需暴露 5173 端口，客户端访问 `http://<server-ip>:5173`。
- ⚙️ 暴露到网络前需修改 `.env` 中的 `AUTH_SECRET`、`MASTER_VAULT_KEY_V1`、`NEO4J_PASSWORD`，并在 `nginx.conf` 的 Host 白名单加入服务器域名/IP。
- 🔒 建议在 5173 前加反向代理启用 HTTPS，并将应用端口绑定为 `127.0.0.1:5173:8080`。
- 🏷️ 可通过 `FLOWSINT_VERSION` 固定版本，默认拉取 `latest` 镜像。
- 🧠 核心能力是图谱化侦察与 OSINT，用自动富化器扩展实体关系和数据。
- 🌍 富化器覆盖域名、网站、IP、ASN、CIDR、组织、社交媒体、加密货币、邮箱、电话、个人与 N8n 集成。
- 🧱 项目模块化：`flowsint-core`、`flowsint-types`、`flowsint-enrichers`、`flowsint-api`、`flowsint-app`，依赖关系逐级向下。
- 💻 开发环境可运行 `make dev` 或 `docker compose -f docker-compose.dev.yml up -d --build`，应用位于 `localhost:5173`；各模块用 `uv run pytest` 测试。
- 📚 贡献需遵循模块结构、使用 `uv` 管理依赖、为新功能写测试、更新文档，并参考 `CONTRIBUTING.md`。

---

### [](https://github.com/arnegiacomo/fugleramme?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-763-september-17-2026)

**原文标题**: [GitHub - arnegiacomo/fugleramme: E-ink bird frame for Raspberry Pi - real-time bird detection by audio, fully local AI, rendered as real, hand-cut 1800s bird illustrations. · GitHub](https://github.com/arnegiacomo/fugleramme?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-763-september-17-2026)

Fugleramme 是 arnegiacomo 开发的 Raspberry Pi 电子墨水鸟框项目：通过本地 AI 实时听音识别鸟类，再把真实手工剪裁的 1800 年代公共领域鸟类插图绘制到电子墨水屏或网页 kiosk 上。项目仍处早期开发，已有约 2.9k stars、71 forks，在线实例运行于挪威卑尔根厨房窗前。

- 🐦 核心机制：BirdNET-Go 用麦克风监听并分类鸟声，Fugleramme 轮询其 API，匹配物种插图，并且只在鸟种变化时重绘。
- 🖼️ 显示方式：支持 Inky Impression 13.3" e-ink 面板和网页 kiosk；没有电子墨水屏也可仅用网页或 HDMI 显示。
- ⚙️ 管理与集成：提供 admin 页面配置显示内容、自动更新等；也可连接同机或网络内已有的 BirdNET-Go。
- 🧰 推荐硬件：Raspberry Pi 5、Inky Impression 13.3"（Spectra 6）、麦克风和 A4 相框。
- 🎨 艺术资源：800+ 手工剪裁、400+ 物种，来自真实公共领域自然史图版；非 AI 生成，部分经 AI 修饰，按体重排布，大鸟居中。
- 🌍 物种覆盖：目前北欧、不列颠和中欧最佳，欧洲与北美覆盖正在扩展；无检测时显示空栖木。
- 🚀 本地开发：uv sync 后可用 fake detector 在 :8090 模拟 BirdNET-Go，并在 :8080 热重载启动服务。
- 📦 安装部署：树莓派可用 install.sh 安装为 systemd 服务；支持 Docker，kiosk 在 :8080，admin 在 :8080/admin，数据存于 /data。
- 🐳 容器运行：提供 docker run 和 docker compose 示例，可在带 USB 麦克风的 Linux 机器上连同 BirdNET-Go 一起启动。
- 🤝 贡献方式：欢迎修复、文档和鸟类艺术作品；bug 报告、FAQ/Discussions、PR 均有对应渠道。
- 📜 许可证：代码为 MIT；BirdNET-Go 为 CC BY-NC-SA 4.0 非商业；图像、字体、数据等有各自许可与来源说明。
- 🔗 灵感与相似项目：受 WWF 海报、AvianVisitors、BirdNET-Go 启发；相似项目包括 inky-bird-frame、HABirdDashboard、featherframe、birdframe 等，但不共享代码或艺术。

---

### [](https://github.com/ifixai-ai/iFixAi?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-763-september-17-2026)

**原文标题**: [GitHub - ifixai-ai/iFixAi: Independent Auditing of AI Agents. Run by human or the agent itself, to answer the most crucial question in the AI Agent Economy. Is the agent doing what is supposed to do? With iFixAi you can have this answer in less than 120 seconds. · GitHub](https://github.com/ifixai-ai/iFixAi?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-763-september-17-2026)

iFixAi 是一个面向 AI 智能体的开源独立审计工具（Apache 2.0），旨在回答 AI 代理经济中最关键的问题——智能体是否真正按业务目标和组织结构履行职责。它结合了 AI 红队测试与运营保障，能在 120 秒内给出 A–F 等级评分，弥补现有评估工具只关注技术指标而忽视业务一致性的不足。

- 🎯 核心定位：独立审计 AI 智能体，在问题爆发前发现其错误与盲区，兼顾对抗深度与保障纪律。
- 🚀 快速上手：一条 `ifixai run` 端到端完成，向导式设置选择系统、评判者和测试套件，执行 32 项检查，输出 A–F 等级与评分卡。
- 🛠️ 三种运行方式：CLI 向导（`ifixai setup` 后零参数运行）、CLI 显式标志（完全可脚本化，适合 CI）、插件或技能（在 Claude Code、Codex 等代理内以自然语言驱动）。
- 🔌 插件与技能：Claude Code/Codex 可一次性原生安装自动配置插件；其他代理可用 `uvx ifixai install` 生成 `/ifixai-skill` 斜杠命令。
- 🧪 测试对象：支持任意提供商或你的智能体真实端点，可将已部署的智能体作为黑盒（`--provider http --endpoint ... --grounding sut`）进行评测。
- ⚖️ 双角色评分：SUT（被评对象）与 Judge（评判者）需来自不同厂商的两个密钥，才能获得“可引用”的成绩；否则需加 `--eval-mode self` 仅作冒烟测试。
- 🧑⚖️ 推荐评判配置：单评判用 Sonnet（约 $12–18）；更经济的双评判用 Gemini 2.5 Pro + GPT-5.4-mini（约 $10–14），跨厂商增强稳健性。
- 📦 测试套件：smoke（3 项）、strategic（8 项）、core（32 项评分卡）、extended（28 项前沿风险）、all（60 项，默认）。
- 🏛️ 五大核心支柱：伪造（Fabrication）、操纵（Manipulation，权重 0.35）、欺骗（Deception）、不可预测性（Unpredictability）、不透明性（Opacity，各 0.15），加权平均得出 A–F 等级（A ≥ 0.90，F < 0.60）。
- ⚠️ 强制最低要求：B01 需 100%、B08 需 95%、P01 需 100%，任一未达标则总分上限为 60%。
- 💎 高级类别：20 个高级类别（如破坏、颠覆、隐瞒、系统性风险等）共 28 项检查，免费预览但不影响等级，保证不同能力智能体评分可比。
- 📊 评分配置可复用：`ifixai setup` 生成 `ifixai.yaml`，存储密钥环境变量名而非密钥本身，默认被 git 忽略。
- 🔐 遥测透明：仅发送匿名安装 ID、版本、操作系统、界面类型与时间戳，不发送代码、发现、评分、提示词、路径或 IP，CI 中自动关闭，可随时退出。
- 🌍 开源许可：Apache 2.0，免费开放，欢迎 Issue 与 PR；文档涵盖入门、测试、CLI、Python API、评分与方法论。
- 📈 社区热度：15.3k 星标、1.3k 分支、361 位关注者，覆盖 agent-evaluation、ai-governance、owasp-llm 等主题标签。

---

### [](https://github.com/dbt-labs/dbt-charts?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-763-september-17-2026)

**原文标题**: [GitHub - dbt-labs/dbt-charts · GitHub](https://github.com/dbt-labs/dbt-charts?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-763-september-17-2026)

dbt Charts 是 dbt Labs 推出的开源工具，用声明式 YAML 语法包裹 SQL，把看板定义编译成多种格式的交互式仪表盘与报表，旨在解决"氛围编程"产生的仪表盘难以审计的问题。

- 📊 **核心定位**：SQL 负责定义"看什么数据"，dbt Charts 用简洁的 YAML 声明"怎么展示"，包名为 dbt-charts，命令行工具为 dct。
- 🎯 **解决问题**：随意生成的仪表盘会堆积大量构件、框架与数据转换，导致审计困难；YAML 语法让智能体易写、人类易审。
- 🚀 **快速体验**：无需安装即可在 play.dbtcharts.com 试用，或查阅官方文档。
- 🐍 **环境要求**：当前为 Beta 阶段（pre-1.0），需 Python 3.10–3.13，可通过 `uv tool install dbt-charts` 或 pip 安装。
- 🔌 **仓库连接**：通过 dbt 适配器连接数据仓库，支持 BigQuery、Snowflake、Redshift、Databricks、PostgreSQL、Spark、Trino 等，DuckDB 内置。
- 🛠️ **CLI 功能**：dct 提供 validate（校验）、serve（实时预览）、render（导出 HTML/PDF/PNG/SVG/JSON）、query、search、impact、docs、examples 等命令。
- 🤖 **智能体支持**：内置技能与本地 MCP 服务器，`dct skills intro` 是智能体入门入口，可安装到 Cursor、VS Code、Claude Desktop 等。
- 🧩 **VS Code 扩展**：提供 YAML/SQL/Jinja 语法高亮、schema 自动补全、实时诊断与随存随渲染的预览。
- 🔗 **与 dbt 协作**：charts/ 可独立存在；放入 dbt 项目后可用 `ref()` 查询模型、复用 dbt profile，`dct impact` 可追溯列变更影响的看板。
- 📦 **支持范围**：本地源支持 CSV、Parquet、JSON、DuckDB；16 种核心图表类型、13 种语义图表类型、5 种内置主题。
- ✅ **校验与 CI**：错误信息含代码、文件行号、修复建议与文档指引；`dct init ci` 生成无需仓库凭证的 GitHub Actions 工作流。
- 🔄 **迁移机制**：旧语法仍可解析并在内存中迁移，`dct migrate` 可将文件重写为最新语法。
- ⚙️ **技术栈**：Pydantic（校验）、Jinja2（模板）、Vega-Lite + vl-convert（图表）、FastAPI（预览服务器）。
- 📄 **许可与贡献**：Apache 2.0 许可；仓库为私有上游的只读镜像，欢迎提交 Issue，但不接受 PR。

---

### [媒介](https://blog.jupyter.org/jupyterhub-6-0-df28f06ea3ed?gi=d68f8295941e&utm_campaign=python-weekly-issue-763-september-17-2026&utm_medium=newsletter&utm_source=www.pythonweekly.com)

**原文标题**: [Medium](https://blog.jupyter.org/jupyterhub-6-0-df28f06ea3ed?gi=d68f8295941e&utm_campaign=python-weekly-issue-763-september-17-2026&utm_medium=newsletter&utm_source=www.pythonweekly.com)

JupyterHub 是一套为教育和研究提供标准化、易用计算环境的工具集。JupyterHub 6.0 已发布，这是一次重要更新，破坏性变更预计很少，仅影响少数部署；但包含小型数据库架构升级，升级前请务必备份数据库。主要亮点包括命名服务器规则更严格、Python 3.10 与数据库升级、指标系统更新、内部通信改用 aiohttp、API 权限控制更细粒度等。

- 🚀 JupyterHub 6.0 发布：为教育和研究提供标准化、用户友好的计算环境。
- ⚠️ 升级注意：包含小型数据库架构升级，升级前必须备份数据库；破坏性变更预计很少，影响部署不多。
- 🏷️ 命名服务器规则更严格：名称规则收紧，并新增限制更少的“显示名称”字段；这可能是对用户影响最大的变更。
- 🐍 环境要求：JupyterHub 6.0 需要 Python 3.10，并伴随数据库架构升级。
- 📊 指标更新：移除旧 StatsD 指标，转向更常用的 Prometheus 指标；为 Spawner/spawn hook 作者引入 SpawnException，以便在指标中更细粒度地区分 spawn 失败中的错误与拒绝。
- 🔗 内部通信变化：内部 HTTP 请求改用 aiohttp；大型部署可能需要调优，因为内部 HTTP 请求常是扩展瓶颈；单节点部署可使用 Unix socket 进行内部通信。
- 🔐 API 权限更细粒度：新增用于操作单个服务器的 API 端点，提供更灵活的权限定义方式，如 start:servers 范围和 extra_user_scopes。
- 🛠️ 其他改进：包含大量其他改进与错误修复，详情见升级文档和变更日志。
- 🙏 致谢贡献者：文章列出了参与讨论、代码、文档和审查的众多贡献者。

---

### [](https://www.meetup.com/pydataireland/events/316266703/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-763-september-17-2026)

**原文标题**: [Generative Computing: An Evening with IBM Research, Thu, Sep 24, 2026, 5:30 PM   | Meetup](https://www.meetup.com/pydataireland/events/316266703/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-763-september-17-2026)

本次活动是 PyData Ireland 主办的“Generative Computing: An Evening with IBM Research”，将于 9 月 24 日周四 17:30–21:00 IST 在都柏林 Trinity College Dublin Business School 举行，聚焦生成式计算、Mellea，以及如何像调用函数一样调用模型来编写程序。

- 🗓️ 时间与地点：9 月 24 日周四 17:30–21:00 IST，Trinity College Dublin Business School，182 Pearse St, Dublin 2, D02 F6N2。
- 👩‍💻 主办与支持：Sukanya M. / PyData Ireland 主办，IBM Research 合作，NumFOCUS 赞助。
- 🧪 活动定位：Open Source Science Dublin 聚会，连接前沿科研、开源技术、AI 与云原生基础设施。
- 🍕 活动预期：技术深度探讨、跨学科交流和披萨。
- 💡 核心主题：Generative Computing——把模型调用当作一等程序元素，具备类型、可组合、可验证、可治理。
- ⚠️ 现状问题：LLM 调用常是临时提示词粘进应用代码，脆弱、难测试、难审计。
- 🐍 实践工具：开源 Python 库 Mellea，用于构建可预测的生成式程序。
- 🔧 FactReasoner：IBM 概率长文本事实性评估器，迁移到 Mellea 后获得可靠性和速度提升。
- 🧩 Mellea Skills Compiler：把自然语言技能规范编译为受治理、可认证的生成流水线。
- 🎤 Talk 1：Rahul Nair 介绍 Mellea 核心抽象——指令、需求、采样策略、验证器，并现场编码。
- 🎤 Talk 2：Radu Marinescu 讲解 FactReasoner 如何将生成文本拆为原子声明并对证据推理，以及移植经验。
- 🎤 Talk 3：Elizabeth M. Daly 展示 Skills Compiler 端到端示例，讨论 LLM 技能“认证”与可审计生产部署。
- 🏷️ 相关主题：人工智能、计算机编程、开源、软件开发。

---

### [](https://www.meetup.com/pydatahelsinki/events/316164476/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-763-september-17-2026)

**原文标题**: [PyData Helsinki at Reaktor, Tue, Sep 22, 2026, 5:30 PM   | Meetup](https://www.meetup.com/pydatahelsinki/events/316164476/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-763-september-17-2026)

PyData Helsinki 将于 9 月 22 日（星期二）17:30–20:30 EEST 在赫尔辛基 Reaktor 举行，由 Jouni S. 等 4 人主持，NumFOCUS 赞助。活动包含四场演讲，涵盖自制超 8 胶片扫描仪、生存模型直觉理解、强化学习玩 Pokémon TCG，以及闪电演讲“如何学习 AI？”，并关联 AI、机器学习、数据科学和 Python 等主题。

- 🗓️ 时间：9 月 22 日星期二，17:30–20:30 EEST
- 📍 地点：Reaktor，Yliopistonkatu 4，Helsinki
- 👥 主办：Jouni S. 和另外 3 人，PyData Helsinki
- 🎤 演讲：Jussi Pakkanen——在家搭建超 8 胶片扫描仪
- 📊 演讲：Alban King——生存模型的直观理解
- 🤖 演讲：Aji Samudra——用强化学习训练智能体玩 Pokémon TCG
- ⚡ 闪电演讲：Sajal Choudhary——如何学习 AI？
- 🤝 赞助：NumFOCUS，推动科学技术的可访问与可复现计算
- 🏷️ 相关主题：Helsinki 活动、人工智能、机器学习、数据科学、Python
- 🔗 更多详情见活动页面

---

### [](https://www.meetup.com/pythonsd/events/312775789/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-763-september-17-2026)

**原文标题**: [SDPy Monthly Meetup, Thu, Sep 24, 2026, 7:00 PM   | Meetup](https://www.meetup.com/pythonsd/events/312775789/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-763-september-17-2026)

本次为 San Diego Python 用户组（SDPy）月度聚会，由 David F. 和 Diane C. 主办，9 月 24 日周四 19:00–21:00 PDT 在 Qualcomm Building Q 举行，并同步 YouTube 直播；Qualcomm 提供场地，Cloudflare 提供披萨。活动包含 5–7 分钟闪电演讲，以及 Python 类和 AI 数据主题分享。

- 📅 时间：9 月 24 日周四，19:00–21:00 PDT
- 📍 地点：Qualcomm Building Q，6455 Lusk Blvd, San Diego, CA
- 🎙️ 主办：San Diego Python Users Group，David F. 和 Diane C.
- 🏢 赞助：Qualcomm 提供场地；Cloudflare 提供披萨；Ansir Innovation Center 曾承办聚会
- 💻 参与：线下举行，并会在 YouTube 频道直播
- 🚪 入场：穿过咖啡厅入口，前往建筑后方的大型阶梯会议厅；门可能上锁，说明来参加 San Diego Python，安保会协助
- 🗣️ 议程：5–7 分钟闪电演讲；想演讲可在 sandiegopython.org/present/ 报名
- 🐍 演讲 1：Trey Hunner《Everything You Don't Need to Know About Classes in Python》（25 分钟，PyBeach 预览）
- 🤖 演讲 2：Jaskirat Singh Nandhra《Why Your AI Agent Is Only as Good as Your Data》
- 📢 公告：欢迎提交反馈以改进 San Diego Python；活动遵守行为准则
- 🔎 其他：可举报活动，查看相关 San Diego 活动与更多推荐

---

### [](https://www.meetup.com/pydata-southampton/events/316271029/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-763-september-17-2026)

**原文标题**: [PyData Southampton - 26th Meetup, Tue, Sep 22, 2026, 7:00 PM   | Meetup](https://www.meetup.com/pydata-southampton/events/316271029/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-763-september-17-2026)

PyData Southampton 第 26 次聚会将于 9 月 22 日星期二 19:00–21:00 BST 在 Network Eagle Lab 举行，场地已变更。活动由 Sam M. 等 5 人主办，包含两场主演讲、闪电演讲、茶歇和会后交流，需提前 RSVP 并遵守入场与行为准则。

- 🗓️ 时间：9 月 22 日星期二，19:00–21:00 BST；18:30 开门。
- 📍 地点：Network Eagle Lab，Portland Terrace, Southampton, SO14 7SJ，注意场地已更换。
- 👥 主办：PyData Southampton，Sam M. 和其他 4 人。
- 🎤 主演讲 1：Hugh Evans 分享用 Python 和网络爬虫从 Meetup 数据绘制 PyData 社区地图，涉及地理编码、Folium 地图制作，并呼吁支持本地 PyData 小组。
- 🤖 主演讲 2：Damian Bemben 介绍“City Dreams”装置，结合语音识别、3D 捕捉和生成式 AI，让公众描绘并生成理想中的南安普顿城市愿景。
- ⚡ 闪电演讲：两场，讲者与主题待定（TBA）。
- 🪪 入场要求：建筑安保要求有效带照片身份证件；Meetup 资料必须使用名/首名和姓氏，否则无法列入宾客名单。
- ✅ RSVP：状态为“You're going”即可入场，无需额外确认；如不能参加请尽快取消，以便把名额让给候补者。
- 📜 行为准则：活动遵循 NumFOCUS Code of Conduct，参加前请熟悉；有问题可联系组织者。
- ☕ 茶歇与交流：主办方提供茶和咖啡；21:00 后可能前往附近酒吧继续交流。
- 🔗 关注渠道：Bluesky/Instagram/Threads 可关注 @pydatasoton，也可在 LinkedIn 获取更新和预告。
- 🏢 赞助：NumFOCUS 推广开放代码促进科学；Southampton City Council 提供 Network Eagle Lab 场地。
- 🧠 相关主题：机器学习、大数据、数据科学、Python、统计计算。

---

### [](https://www.meetup.com/python-spokane/events/316344742/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-763-september-17-2026)

**原文标题**: [🚀 Build Your First API with Python!, Tue, Sep 22, 2026, 5:30 PM   | Meetup](https://www.meetup.com/python-spokane/events/316344742/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-763-september-17-2026)

这是一场由 Spokane Python 用户组与 David 主办的线下实践工作坊，主题是“用 Python 构建你的第一个 API”，面向初学者和有经验开发者，涵盖 API 基础、CRUD、认证授权、OpenAPI/Swagger 文档，以及 FastAPI、Django、Flask 框架对比。

- 🗓️ 时间：9 月 22 日（周二）下午 5:30–7:30 PDT
- 📍 地点：IntelliTect，1720 W 4th Ave Unit B，Spokane, WA
- 🐍 主题：用 Python 框架把 Python 代码变成可用的 Web API
- 🔄 内容：讲解 CRUD 基础——创建、读取、更新、删除
- 🔐 内容：API 如何识别用户并控制访问权限
- 📖 内容：OpenAPI 与 Swagger 交互式文档，可在浏览器中探索和测试接口
- ⚡ 框架：介绍 FastAPI、Django、Flask 的不同 API 构建方式及各自优势
- 🌱 适合人群：初学者友好，无需 API 或 Web 开发经验；有经验者也欢迎参与
- 💻 参与方式：可带笔记本跟做，也可只观看、提问和学习
- 🤝 赞助支持：IntelliTect 提供场地和零食，Python Software Foundation 赞助 Meetup 订阅
- 💬 活动前可加入 Event chat，与其他参会者交流

---

### [](https://www.meetup.com/pydata-manchester/events/316512300/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-763-september-17-2026)

**原文标题**: [PyDataMCR September , Thu, Sep 24, 2026, 6:00 PM   | Meetup](https://www.meetup.com/pydata-manchester/events/316512300/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-763-september-17-2026)

PyDataMCR 九月活动由 PyData Manchester 主办，Shaun H. 等三人主持，将于 9 月 24 日周四 18:00–20:00 BST 在曼彻斯特 AutoTrader Circle Square 举行，包含两场数据与 AI 主题演讲、餐饮和会后社交。

- 📅 时间地点：9 月 24 日周四 18:00–20:00 BST，AutoTrader Circle Square，No. 3 Circle Square, M1 7BL，曼彻斯特。
- 🎙️ 主办主持：PyData Manchester，主持人为 Shaun H. 和另外两位。
- 🧠 演讲一：Lucy Stafford-Hughes 分享《Empathy Data in LLM's - Part II》。
- 🔍 核心内容：探讨用锚定和身份容器建立 LLM 稳定交互模式，以减少幻觉并提升响应上下文与准确性。
- 🤖 模型观察：对比两种 AI 模型，结合 Anthropic 关于 Claude 情绪概念与情绪向量的最新研究，讨论人机协作与未来涌现行为。
- 👩‍💼 讲者背景：Lucy 是顾问、作家和 AI 研究者，专长包括复杂业务系统、敏捷工作方式和人机交互。
- 📊 演讲二：Josh Hayes 分享《The meaning of lift - understanding marketing effectiveness》。
- 💬 核心观点：数据科学不只是回答问题，更要理解问题，并帮助利益相关者澄清细微不同的需求、建立衡量语言。
- 📈 营销案例：讨论广告支出、归因建模，以及如何衡量和沟通营销活动影响。
- 👨‍🔬 讲者背景：Josh 是 Autotrader 高级数据科学家，天体物理学博士，拥有近 10 年学术界与业界经验，曾在 Natwest 和 Autotrader 领导团队。
- 🍕 场地餐饮：Autotrader 提供场地和餐饮，容量限 50 人；会后将前往当地场所社交。
- 📜 活动规范：PyDataMCR 是严格的专业活动，遵循 NumFOCUS 行为准则。
- ♿ 无障碍：场地和厕所均无障碍。
- 🤝 赞助支持：NumFOCUS、AutoTrader、Kraken、Horsefly Analytics。
- 💬 活动聊天：可加入活动聊天，在活动开始前与其他参会者交流。

---

### [](https://www.meetup.com/pydata-leeds/events/315680259/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-763-september-17-2026)

**原文标题**: [PyData Leeds: Leeds Digital Festival '26, Tue, Sep 22, 2026, 5:30 PM   | Meetup](https://www.meetup.com/pydata-leeds/events/315680259/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-763-september-17-2026)

PyData Leeds 将第四次参加 Leeds Digital Festival，于 2026 年 9 月 22 日晚在 Leeds 举行，面向数据与软件工程爱好者，包含社交、演讲、投票和问答，重点讨论云与本地模型之间的取舍。

- 📅 活动：PyData Leeds 第四次参与 Leeds Digital Festival。
- 🗓️ 日期：2026 年 9 月 22 日（星期二），17:30–20:00 BST。
- 📍 地点：Hippo Digital Event Space（Brew Society 后方），26 Aire Street, Leeds, LS1 4HT。
- 👥 主办：由 Edward H. 与 Adam E. 主持，PyData Leeds 组织。
- 🤝 目的：连接数据与软件工程爱好者，进行社交、学习和交流，融入 Leeds 科技生态与数字文化节。
- 🗣️ 议程：17:30 到达、社交与茶点；18:10 欢迎与破冰；18:30 活动与演讲；20:00 收尾与饮品。
- 🎤 演讲：Lee Crossley 分享“The Cloud won't die. It's monopoly on intelligence might”。
- 🧠 核心观点：不要默认使用云；将每个任务路由到能通过验收测试的最小模型，考虑信任边界，有证据支持时再用云。
- 🧪 案例：Overshow 内 4-bit Gemma 重打包、128 GB M5 Max 上运行 27B Qwen，以及消耗超 1400 万 tokens 仍引入 4 个回归的 agentic 实验。
- 🗳️ 互动：包含快速投票、现场投票，并尽量留 10 分钟问答讨论。
- 📜 规范：严格专业活动，遵守 NumFOCUS 行为准则；可通过 Meetup 关注社区。
- 🏷️ 相关主题：Leeds/GB 活动、大数据、新技术、专业社交、Python。

---

### [](https://www.meetup.com/pydata-lisbon/events/316579913/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-763-september-17-2026)

**原文标题**: [19th PyData Lisbon Meetup: Special on AI Infrastructure, Tue, Sep 22, 2026, 6:00 PM   | Meetup](https://www.meetup.com/pydata-lisbon/events/316579913/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-763-september-17-2026)

第 19 届 PyData Lisbon Meetup 将推出“AI 基础设施”特别场，并作为 Lisbon AI Week 的一部分举行。活动包含专题讨论、演讲、披萨饮料与社交，适合关注 LLM 部署、推理优化与自托管模型的开发者参加。

- 📅 时间：9 月 22 日（周二）18:00–22:00 WEST
- 📍 地点：IDEA Spaces - Saldanha，Av. Defensores de Chaves 4, 1000-117 Lisboa, Portugal
- 🎯 主题：AI Infrastructure，聚焦 AI 基础设施与 LLM 技术栈
- 🧑‍💻 主办与主持：PyData Lisbon，主持人 Telmo F.
- 💬 专题讨论：“The LLM Stack: Inference, Accelerators, Open Models and Beyond”
- 👥 讨论嘉宾：Miguel Silva（AWS）、Samuel Arcadinho（Zendesk）、Bojan Jakimovski（Loka）、Sara Zanzottera（BGBx）
- 🎙️ 讨论主持：Tiago Mota（DareData）
- 🗣️ 第二场演讲：“Getting Started with Self-Hosted LLMs”，由 Miguel Silva（AWS）主讲
- 🕕 日程：18:00–18:30 入场；18:30–19:30 专题讨论；19:30–19:45 休息；19:45–20:30 演讲；20:30 起社交、披萨与饮料
- 🤝 赞助与支持：NumFOCUS、Idea Spaces（场地）、Loka（组织）、jungle.ai
- 🏷️ 相关主题：机器学习、大数据、计算机编程

---

### [](https://www.meetup.com/pydata_seattle/events/316322058/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-763-september-17-2026)

**原文标题**: [Building Production-Ready AI: Agentic Systems, RAG & Responsible AI, Thu, Sep 24, 2026, 5:30 PM   | Meetup](https://www.meetup.com/pydata_seattle/events/316322058/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-763-september-17-2026)

本次活动由 PyData Seattle 与 Microsoft Reactor 联合举办，聚焦如何构建可靠、负责任且可投入生产的 AI 系统。内容涵盖负责任 AI 采用、生产级智能体 AI、RAG 管线、多步骤智能体工作流、评估策略与常见失败模式，并邀请 Google 与 Microsoft 专家分享真实落地经验。

- 🗓️ 活动主题：构建生产就绪的 AI：智能体系统、RAG 与负责任 AI。
- 🏢 主办方：PyData Seattle 与 Microsoft Reactor，线上活动。
- 🎯 核心目标：帮助工程团队超越模型能力，设计可扩展、可信且实用的 AI 系统。
- 🧭 Ramachandra Nalam（Google 高级数据工程师）：分享 AI 在真实系统中的最佳实践与局限，包括可靠性、隐私、透明度与人工监督。
- 🧰 他将提供实用框架，帮助在采用 AI 时做出明智且负责任的决策。
- 🤖 Anamika Kumari（Microsoft 高级 AI/ML 工程师）：讲解如何架构和部署生产级智能体 AI 系统。
- 🔍 重点技术：RAG 管线、多步骤智能体工作流、检索设计、智能体编排与评估策略。
- ⚠️ 她也会分析从原型走向生产时的常见失败模式。
- 📈 实战经验：曾交付基于 RAG 的 Copilot，并扩展至每月 9 万活跃用户。
- 👥 适合人群：软件工程师、数据科学家、ML/AI 工程师、研究人员及对实用 AI 系统感兴趣者。
- 🧩 相关主题：机器学习、云计算、计算机编程、开源与软件开发。
- 💡 活动价值：提供从实验到负责任生产落地的可操作见解。

---

