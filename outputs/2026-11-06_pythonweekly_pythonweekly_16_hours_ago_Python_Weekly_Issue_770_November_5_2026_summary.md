### [赫利奥波利斯中心——2026 年 Python 性能分析现状](https://p403n1x87.github.io/the-state-of-python-profiling-in-2026.html?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-770-november-5-2026)

**原文标题**: [The Hub of Heliopolis - The State of Python Profiling in 2026](https://p403n1x87.github.io/the-state-of-python-profiling-in-2026.html?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-770-november-5-2026)

2026 年 Python 性能剖析生态发生显著变化：CPython 3.15 将采样剖析器 Tachyon 纳入标准库，3.14 的远程调试与 asyncio 可检查能力增强了进程外工具，free-threading 逐步进入生产，编码代理也开始直接读取和分析 profile。文章比较 Tachyon、py-spy、Scalene 与 Austin，重点介绍 Austin 4.1 在采样率、原生栈、asyncio 任务剖析和代理辅助分析上的进展，并指出不同工具的适用边界。

- 🧭 四款工具都是采样剖析器：Tachyon、py-spy、Austin 在进程外工作，Scalene 在进程内运行；采样通常比追踪开销更低、时间归因更接近真实运行，但无法精确统计调用次数。
- ⚡ 采样率直接决定统计准确性：误差大致随样本数按 1/√n 下降；Austin 默认每线程每秒 10,000 个样本，Tachyon 默认 1 kHz 但可提高，高采样率更利于短运行和短生命周期函数。
- 🏛️ 关键背景：CPython 3.14 通过 PEP 768 支持远程调试并暴露 asyncio 任务图，3.15 内置采样剖析器；free-threaded 构建走向部署，编码代理成为 profile 的新读者。
- 🐍 Tachyon 是 CPython 3.15 的 `profiling.sampling`：支持 run、attach、dump、墙钟/CPU/GIL/异常采样、async-aware 模式、实时 top 视图、火焰图、pstats、Gecko、JSONL 等格式。
- ⏳ Tachyon 的主要限制是仅支持 Python 3.15 及以上，且剖析器与目标需同小版本、同构建类型；`--native` 只插入 `<native>` 占位帧，不展开原生栈。
- 🕰️ Tachyon 的进程外采样思路与 py-spy、pyflame、Austin 一脉相承，许多功能 Austin 更早提供；文章认为 PEP 799 未充分致谢这些外部工具的历史贡献。
- 🦀 py-spy 是成熟的主流选择：Rust 编写，提供 record/top/dump，输出 SVG、Speedscope、Chrome trace，支持子进程、GIL 过滤和部分平台的原生栈展开。
- 🧵 py-spy 0.4.2 已支持 Python 3.14，但尚不支持 free-threaded 构建，也没有任务感知的 asyncio 模式，协程只显示为事件循环线程上的普通帧。
- 📊 Scalene 是进程内全能型工具：提供行级 CPU 拆分、内存分配/泄漏/复制量、NVIDIA 与 Apple GPU 时间、async await 墙钟、混合栈和 AI 优化建议；典型开销 10–20%，但不能附加到已运行进程。
- ⚠️ Scalene 的多线程 Python/native 时间拆分存在已知争议，GPU 时间在 NVIDIA 上需 root 启用 per-process accounting；否则只能显示整卡利用率并给出警告。
- 🚀 Austin 是纯 C 的进程外帧栈采样器：读取解释器内存，将原始样本写入 MOJO 二进制，分析后置；支持 CPython 3.10–3.15、free-threaded、Linux/macOS/Windows 及多种架构。
- ⏱️ Austin 4.1 通过重复栈检测和输出缓冲提升采样率：墙钟模式最高从 121k 提升到 166k samples/s（+37%），CPU 模式从 34k 提升到 37k（+9%）；收益取决于栈重复频率。
- 🧬 Austin 原生模式用 `-n/--native` 交织 Python 与原生栈，可观察 NumPy、Cython、PyO3/Rust 扩展及纯原生线程；支持 Linux x86_64/aarch64、macOS、Windows x86_64，但采样时会短暂暂停线程，生产环境应慎用。
- 🔁 Austin 在 CPython 3.14+ 支持 asyncio 任务级剖析：跟踪任务图、协程链和 await 关系，把样本归属到具体任务并跟踪任务生命周期；VS Code 的 Task Trace 可展示每个任务的时间线。
- 🤖 Austin 4.1 降低使用门槛：VS Code MCP server 与 `austin-python` 查询 API/`austin-query` 让编码代理自动剖析、查询热函数/调用栈/async 任务/GC；MCP 动作工具还可引导用户阅读火焰图。
- 📦 Austin 4.1 其他改进包括首日支持 Python 3.15 与 free-threaded、线程显示 `threading` 名称、更好处理容器并记录工作目录、虚拟环境和 `PYTHONPATH`；free-threading 下内存模式准确性受限。
- ⚠️ Austin 的短板是内存模式测量 RSS 变化而非分配行为，不适合逐行分配分析或泄漏排查；它也没有自带行级 GUI，Linux/macOS 附加进程需要提权。
- ✅ 选择建议：3.15 上快速上手用 Tachyon；内存/GPU/行级细节用 Scalene；老版本或生产附加用 py-spy/Austin；asyncio 任务级用 Austin，Tachyon 提供任务感知栈，Scalene 可看慢 await 行；原生扩展尤其 macOS 用 Austin native；代理分析或教学用 Austin MCP/`austin-query`。
- 🔮 未来趋势是标准库剖析器抬高基线、远程调试让外部工具更可靠，并重点改进 free-threading 与 asyncio 并发支持，以及通过代理执行或代理教学让剖析更易用。

---

### [Django 中的规模化缓存：来自生产环境的经验 | Johnny Metz](https://johnnymetz.com/posts/caching-at-scale-in-django/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-770-november-5-2026)

**原文标题**: [Caching at Scale in Django: Lessons from Production | Johnny Metz](https://johnnymetz.com/posts/caching-at-scale-in-django/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-770-november-5-2026)

本文回顾了一个多租户 Django API 在两年流量增长约 20 倍后，如何通过更主动、更精细的缓存策略，把数据库压力转移到 Redis：采用“全局基础数据 + 按用户组装”的两层缓存、长 TTL 配合精确失效、限制失效影响范围，并为 Redis 故障和身份查询做好预案。最终在三个月推广期内，流量上涨约 40%，平均延迟下降约 40%，数据库查询量和 Web CPU 均减半。

- 🎯 缓存的核心价值是“减少工作量”，而不是单纯增加数据库容量；应优先缓存高频、高总耗时的查询和接口响应。
- 📊 优化顺序应按数据库总耗时排序，而不是只看单次查询延迟；高并发的小查询往往比偶发慢查询更耗数据库资源。
- 🧱 采用两层缓存：按用户缓存可见文档 ID 和权限查询结果，全局缓存每篇文档的基础数据，再在组装时合并。
- 🔐 全局共享的基础数据不能依赖请求者身份；应存储 owner、编辑组等原始字段，在组装时计算 `can_edit`，避免首个用户“决定”所有人的缓存内容。
- ⏳ 使用长 TTL（如 7 天）并依赖写入时的精确失效，而不是短 TTL；短 TTL 会在高峰期造成集中回源，也无法满足写入后立即可见。
- ✅ 用 Django signals 立即失效，并通过测试、`assertNumQueries`、Hypothesis 状态机验证缓存与未缓存结果一致，防止跨用户泄漏和失效遗漏。
- 🧩 失效要放在 `transaction.on_commit` 后执行，重建缓存应读主库，缓存基础数据保持扁平化，避免嵌套模型扩大失效链路。
- 💥 控制失效爆炸半径：只清除真正变化的键，优先使用全局键；面向全量用户的 fleet-wide 变更可依赖短 TTL 和管理员清缓存。
- 🪪 缓存身份查找：使用 Django `cached_db` session backend，并在用户停用或凭证撤销时失效，减少每个认证请求的数据库读取。
- 🛡️ 为 Redis 故障做预案：使用 `django-redis` 的忽略异常和日志配置实现 fail open，设置短连接/读取超时，避免 Redis 宕机直接导致 500。
- 📈 像监控数据库一样监控 Redis：关注延迟、流量、错误、饱和度、命中率和被驱逐键，并设置足够早的告警阈值。
- 📉 结果：推广期流量增长约 40%，平均延迟下降约 40%，数据库 QPS 和 Web CPU 均减半；当前峰值约 1,100 RPS，曾达 2,300 RPS，Postgres 约 0.3 查询/请求，Redis 命中率约 97%。
- ⏰ 如果预见到流量增长，应提前、系统地实施缓存，而不是等数据库被迫成为瓶颈后再补救。

---

### [spark vs hadoop vs duckdb vs polars - YouTube](https://www.youtube.com/watch?v=6_I3c1udTzo&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-770-november-5-2026)

**原文标题**: [spark vs hadoop vs duckdb vs polars - YouTube](https://www.youtube.com/watch?v=6_I3c1udTzo&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-770-november-5-2026)

该内容为 YouTube 页脚导航与版权信息，集中列出平台介绍、联系入口、创作者与开发者资源、政策条款及版权声明。

- 🏢 包含“关于”“新闻”“联系我们”等平台介绍与联系入口。
- 👥 提供创作者、广告合作、开发者相关链接。
- 📜 列出条款、隐私、政策与安全、YouTube 运作方式等说明。
- 🧪 提到“测试新功能”入口。
- ©️ 版权声明为 © 2026 Google LLC。

---

### [pyinfra – simple infrastructure automation in Python - death and gravity](https://death.andgravity.com/pyinfra?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-770-november-5-2026)

**原文标题**: [pyinfra – simple infrastructure automation in Python - death and gravity](https://death.andgravity.com/pyinfra?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-770-november-5-2026)

本文介绍了基础设施自动化工具 pyinfra：它用 Python 代码把服务器配置转换为通过 SSH 并行执行的 shell 命令，并现场演示如何先在本机虚拟机、再在两台远程服务器上部署静态落地页和 Python Web 应用。作者强调 pyinfra 声明式、幂等、无 YAML、易复用，适合自托管、家庭服务器和云无关的服务器配置，但生态和内置模块少于 Ansible，且不用于云资源编排。

- 🛠️ pyinfra 是类似 Ansible 的基础设施自动化工具，但部署文件是 Python 代码，不是 YAML，支持 for/if、代码补全、类型检查和导入库。
- ⚡ 核心特性是声明式和幂等：描述服务器目标状态，已满足时不会重复执行；在大规模场景下通常比 Ansible 更快。
- 🖥️ 演示目标：用同一套思路部署两个网站——静态落地页和 Python Web 应用，先在本地虚拟机作为 beta，再部署到两台生产服务器。
- 🧩 两个核心概念：Operations 用于改变服务器状态并确保目标状态；Facts 用于读取目标主机信息，从而控制操作分支。
- 📦 示例通过 apt 更新缓存、安装 nginx、禁用默认站点并重载服务，还使用 `_if` 避免不必要的服务重载。
- 🗂️ Inventory 是 Python 文件，可定义主机分组和主机数据；部署可按主机数据条件化包含任务，例如仅在存在 `home_domain` 时部署主页。
- 🔁 静态站点使用 `files.sync` 同步文件，并通过可复用的 packaged deploy 配置 nginx 站点；Jinja 模板支持基础模板和站点模板继承，`--diff` 可预览渲染结果。
- 🔐 Web 应用使用 Flask + Gunicorn + nginx Unix socket，部署中创建用户/组、虚拟环境、systemd 服务和 nginx 配置；密钥不硬编码，而是通过自定义 secrets 模块按 stage 读取。
- 🌐 HTTPS 通过自定义 Certbot operation 和 fact 实现：检查证书是否存在，不存在则申请证书；beta 因域名不可解析无法测试，最终在生产环境启用 HTTPS。
- ❓ 问答部分说明：可在交互式 Python shell 中使用但有样板代码；pyinfra 不适合云资源 provisioning，应使用 Terraform 等工具；可通过云 SDK 或 Terraform connector 生成动态 inventory。
- ⚠️ 局限包括：无内置 pull 模式、全自动流水线需额外工作、多人同时部署需谨慎；但结构化部署和 Python API 仍能覆盖较多场景。

---

### [我们起飞了 🚀：用 Python 构建 Gemini 服务器 | 右键检查](https://www.willmunn.xyz/gemini/python/2026/10/16/we-have-lift-off.html?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-770-november-5-2026)

**原文标题**: [We have lift off 🚀: building a gemini server in python | right click inspect](https://www.willmunn.xyz/gemini/python/2026/10/16/we-have-lift-off.html?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-770-november-5-2026)

文章介绍了作者在发现 Gemini 协议后，用 Python 从零实现一个极简 Gemini 服务器的过程：从 TCP 套接字、TLS 加密、用户输入与客户端证书，到异步优化和树莓派部署，最终上线了一个基础 TODO 应用。

- 🚀 Gemini 被视为“回归初代原则”的极简 Web 替代方案，强调独立创作者、无机器人/追踪器/商业化干扰。
- 🌐 Gemini 中的网站叫 capsule，网络空间叫 geminispace，文档格式为 gemtext，客户端有 Lagrange 等。
- 🔌 服务端先监听 TCP 1965 端口，使用 IPv4、TCP、`SO_REUSEADDR`，并绑定 `0.0.0.0`。
- 🧪 可用 `nc` 或 `telnet` 测试 TCP 服务；有效 Gemini 请求是绝对 URL，且不超过 1024 字节。
- 📨 响应需包含状态码和 MIME 类型，如 `20 text/gemini` 表示成功，`51` 表示未找到；示例包含 `/hello`、`/goodbye` 路由。
- 🔐 Gemini 强制使用 TLS，但常用自签名证书与 TOFU（首次使用即信任）模式，类似 SSH 的 known hosts。
- 💬 用户输入通过状态码 `10` 触发单字段提示，输入内容作为查询字符串返回同一 URI，比 HTML 表单简单得多。
- 🪪 客户端证书通过状态码 `60` 请求，形成 mTLS；证书 SHA256 指纹可作为用户唯一标识，Common Name 可作为友好名称。
- ⚠️ Python 标准库 `ssl` 难以灵活处理未知 CA 的客户端证书，因此作者改用 `pyOpenSSL`，并设置 `set_verify` 与 session id context。
- ⚡ 同步单线程服务器性能有限，作者讨论多线程、多进程与 `asyncio`，认为 I/O 密集型服务更适合异步并发。
- 🍓 部署使用旧款树莓派 3B、Raspberry Pi OS Lite、systemd、scp/ssh，并在路由器上开放 TCP 1965 端口。
- ✅ 最终成果是一个基础 TODO 应用，可通过 `gemini://todo.willmunn.xyz` 访问，源码发布在 Codeberg。

---

### [手腕上的 Python | 博客](https://tildeweb.nl/~michiel/python-on-my-wrist.html?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-770-november-5-2026)

**原文标题**: [
            
    Python on my wrist

        | Blog](https://tildeweb.nl/~michiel/python-on-my-wrist.html?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-770-november-5-2026)

overview summary
- 🐍 文章讲述作者用 MicroPython 复活廉价开源智能手表 PineTime 的 wasp-os，并将其移植到主线 MicroPython。
- ⌚ PineTime 是 Pine64 推出的约 25 美元开源可编程手表，不是 Apple Watch；它有彩色屏、蓝牙、计步和心率，但 CPU 与内存极小。
- 🧠 硬件为 64 MHz ARM Cortex-M4、64 KB RAM、512 KB 固件 flash 和 4 MB 外部 flash；蓝牙栈与 MicroPython 占用后，应用仅约 12 KB RAM。
- 🛠 作者 2023 年购买该表，原厂 InfiniTime 用 C++；他偏好 wasp-os，但项目曾休眠、基于 2019 年 MicroPython 且难以构建。
- 🔧 他修复构建流程并用 uv 管理工具链；蓝牙刷机改用 bleak，约 3.5 分钟而非 8 分钟以上，失败时会显示原因。
- 💾 外部 flash 改用真实 4 KB 块，去掉常驻缓冲区，启动空闲 RAM 从 7.1 KB 提升到 12.4 KB。
- 🛡 加入看门狗自动重置、修复振动马达持续震动、改进触摸抬起与设置滑动条、启动时解除 I2C 总线卡死，并让时钟从构建日期开始。
- 🐍 wasp-os 首次运行于主线 MicroPython；作者提交的 frozen native code、PWM 分配修复和 ADC 采样时间选项三个上游 PR 均已合并，目标 MicroPython 1.30。
- 🕰 新增两个表盘：荷兰语周钟（如 ma 26 okt 2026）和 8-bit 风格时钟，后者显示 ISO 日期、Unix 时间戳、步数与电量。
- 🚀 Pine64 正在开发 PineTime Pro，规格包括 410×502 AMOLED、GPS、双核 Cortex-M33 和数字表冠，但尚无发布日期。
- 📦 代码位于作者 wasp-os fork 的 pinetime-upstream-micropython 分支；更新称作者已成为 wasp-os 新维护者，Pine64 也将赠送 PineTime Pro。

---

### [基于 NFL 体测数据的 Sklearn 线性回归（分步详解）](https://my-space.io/blog/sklearn-linear-regression/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-770-november-5-2026)

**原文标题**: [Sklearn Linear Regression on NFL Combine Data (Step by Step)](https://my-space.io/blog/sklearn-linear-regression/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-770-november-5-2026)

这篇教程以 NFL Combine 数据为例，分 12 步演示 scikit-learn 线性回归从数据加载、清洗、特征工程、训练测试拆分、Pipeline、交叉验证到新秀预测的完整流程；最终“体重 + 身高 + 位置”模型在未见数据上达到 R²=0.809，并有意复现数据泄漏与错误缩放两个课堂错误，强调基线比较和防泄漏。

- 📈 核心方法：`LinearRegression().fit(X, y)` 训练、`predict()` 预测；模型用最小二乘拟合直线或平面，并可读取 `coef_` 与 `intercept_`。
- 🏈 任务与数据：用 nflverse 的 NFL Combine CSV 预测 40 码冲刺时间；原始数据 8,968 行×18 列，清洗缺失值并去掉 K/P/LS 后剩 7,826 名球员。
- 🧹 预处理：把 `6-4` 这类身高转成英寸，将 21 个位置标签归并为 8 组；2000–2025 的 7,637 人用于训练/测试，2026 届 189 人留作外部验证。
- 🧮 体重单变量模型：斜率约 0.00581 秒/磅；测试集 R²=0.747、MAE=0.117 秒、RMSE=0.153 秒。
- 🎯 基线对比：`DummyRegressor` 直接猜平均值，R²≈0、RMSE=0.304 秒，说明体重模型确实学到了信息。
- 📏 加入身高：R² 仅从 0.747 升到 0.748；身高与体重相关性达 0.72，体重入模后身高贡献很小。
- 🧩 加入位置：用 `OneHotEncoder`、`StandardScaler`、`ColumnTransformer` 和 `Pipeline`，R² 提升到 0.809，MAE=0.103 秒、RMSE=0.133 秒。
- 🔁 交叉验证：5 折 R² 在 0.802–0.809 之间，均值 0.806、标准差 0.003，说明单次测试分数较稳定。
- 📌 系数解读：标准化后，每多 45.9 磅约慢 0.229 秒；同体重同位置下每高 2.7 英寸快 0.035 秒；OL 比 DB 慢 0.225 秒，QB 慢 0.209 秒。
- 🆕 新秀预测：在全部 2000–2025 数据上重训后预测 2026 届，R²=0.753、MAE=0.114 秒、RMSE=0.142 秒。
- 🚨 错误复现一：把 `40 / forty` 作为输入造成数据泄漏，测试 R² 高达 0.996，看似完美，实际只是让模型反算除法。
- 🚨 错误复现二：只缩放测试集、不缩放训练集，导致 R²=-21.613，预测几乎都落在截距约 3.35 秒附近。
- ✅ 关键经验：先跑基线模型；用 Pipeline 把缩放和编码放进模型以防泄漏；分组检查残差；R² 异常高要警惕泄漏；需要 p 值可用 statsmodels，拟合曲线可加入 `PolynomialFeatures`。

---

### [用 Python 打造你自己的 Jarvis（实时语音助手）- YouTube](https://www.youtube.com/watch?v=hhym040zsBI&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-770-november-5-2026)

**原文标题**: [Build Your Own Jarvis in Python (Real-Time Voice Assistant) - YouTube](https://www.youtube.com/watch?v=hhym040zsBI&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-770-november-5-2026)

这是 YouTube 网站页脚信息，主要包含平台相关导航链接、政策条款、功能说明以及版权声明。

- 🏢 提供“关于”“新闻”“版权”“联系我们”等平台基本信息入口。
- 👥 包含“创作者”“广告”“开发者”等面向不同用户群体的链接。
- 📜 列出“条款”“隐私”“政策与安全”等法律与政策相关内容。
- ⚙️ 提供“YouTube 运作方式”和“测试新功能”等功能说明入口。
- ©️ 页面底部标注版权归属：© 2026 Google LLC。

---

### [Python 中不必要的语法 - Python Morsels](https://www.pythonmorsels.com/unnecessary-syntax/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-770-november-5-2026)

**原文标题**: [Unnecessary syntax in Python - Python Morsels](https://www.pythonmorsels.com/unnecessary-syntax/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-770-november-5-2026)

概览：文章主张判断 Python 代码中“非严格必需”的语法是否保留时，应以可读性和意图表达为准；只要能让代码更清晰、更少歧义，就不必机械删除。显式写法往往比隐式写法更易理解。

- 🧭 核心原则：不必要的语法不一定无用；若它能提升可读性，就应保留。
- 🐍 Python 代码不仅给解释器执行，更是写给人阅读和理解的。
- ↩️ `return None` 虽可省略，但显式写出能说明“有意返回 None”，也符合 PEP 8 的一致性建议。
- 🔀 `if/else` 中若两个分支同等重要，保留 `else` 可避免让其中一个分支看起来像“例外情况”。
- 🧪 `try/except/else` 中的 `else` 可强调两条同等重要的路径，即使技术上能省略。
- 🏷️ 关键字参数如 `enumerate(items, start=1)`、`open(filename, mode="wt")` 能提升可读性，让参数含义一目了然。
- 📄 显式指定默认值如 `mode="rt"` 有时能表达意图，尤其同时读写文件或为与二进制模式区分时。
- 🔑 遍历字典时调用 `.keys()` 并非必需，但显式写出可让“遍历键”的意图更清楚。
- ➕ 显式字符串拼接 `+` 可避免隐式拼接带来的潜在 bug，也让拼接行为更明显。
- ✅ 尾随逗号不是必需，但便于重排元素、减少 git diff，提升维护性。
- 🏷️ 命名良好的中间变量即使“多余”，也能把复杂条件解释清楚，通常不损效率。
- 🧩 括号、换行和空白有时非严格必需，但能改善复杂推导式、元组和长表达式的可读性。
- 🧠 最终建议：删除“非必需语法”前先权衡可读性；正如《Zen of Python》所说，“显式优于隐式”。

---

### [迁移到 Python 3.15 | mathspp](https://mathspp.com/blog/migrating-to-python-315?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-770-november-5-2026)

**原文标题**: [Migrating to Python 3.15 | mathspp](https://mathspp.com/blog/migrating-to-python-315?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-770-november-5-2026)

文章介绍迁移到 Python 3.15 时需关注的三类特性：向后兼容的新特性、仅限 3.15+ 的不兼容特性，以及因 Python 3.10 终止支持而现已 100% 可用的 Python 3.11 特性，并给出采用建议与后续行动。

- 🧭 Python 3.15 发布后，3.10 正式 EOL，3.13 进入仅安全更新阶段；若项目需兼容旧版本，可主张最低支持 3.11+。
- ✅ 向后兼容特性可立即使用：显式惰性导入通过 `__lazy_modules__` 列表实现，旧版本会忽略该列表。
- 🧠 类型提示改进可通过 `typing_extensions` 或字符串类型提示在旧版本中使用，并配合最新静态类型检查器。
- 📊 新采样分析器 Tachyon 可用于同版本程序分析；脚本可直接运行，长运行服务可让其附加到进程获取瓶颈线索。
- 🔌 发布 C 扩展的项目可使用新 `abi3t` 有限 C API，兼容 free-threaded 构建并减少未来 wheel 维护。
- 🧱 新内置 `frozendict` 不向后兼容；建议将字典类参数类型提示默认改为 `collections.abc.Mapping`，需要可变时用 `MutableMapping`。
- ⚠️ 3.15 主要不兼容特性包括：内置 `frozendict`、内置 `sentinel`、完整惰性导入、线程安全迭代器、`json`/`asyncio` 等标准库新工具、`profiling` 模块、推导式内解包、启动配置文件等。
- 🚀 使用建议：CLI/Web 服务等入口点考虑默认惰性导入；默认优先 `frozendict` 而非 `dict`；用 `sentinel` 表示特殊默认值或单例；线程代码可探索线程安全迭代器。
- 📦 `frozendict` 与 `json.load` 的新 `object_hook` 参数配合，可将 JSON 数据加载为不可变对象。
- 🎉 现已 100% 支持的 3.11 特性包括：异常组与 `except*`、标准库 `tomllib`、可变泛型与类型变量元组、`Self`、`LiteralString`、`TypedDict` 必选/非必选项。
- 🔧 下一步：可自由升级的项目应尝试 Python 3.15 新特性；否则考虑将最低支持版本提高到 3.11 或 3.13，并寻找可用新特性的场景。

---

### [GitHub - NVIDIA/auto-ontology：Auto Ontology 是一个 Python 框架，用于在数据之上构建基于图的语义推理层。它支持确定性查询生成、更好的上下文检索，并为](https://github.com/NVIDIA/auto-ontology?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-770-november-5-2026)

**原文标题**: [GitHub - NVIDIA/auto-ontology: Auto Ontology is a Python framework for building semantic, graph-based reasoning layers over data. It enables deterministic query generation, better context retrieval, and more explainable AI for LLM and agent workflows. · GitHub](https://github.com/NVIDIA/auto-ontology?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-770-november-5-2026)

NVIDIA Auto Ontology 是一个开源的 Python 框架，用于在数据之上构建基于语义图谱的推理层。它从企业元数据生成并整合本体，为 LLM 与 agent 工作流提供可信的业务语义、确定性查询生成、上下文检索、查询校验和结果溯源，并通过 MCP、CLI 与 API 对外提供能力。

- 🎯 核心目标是解决 agent 分析可靠性问题：不仅要快速查数，还要知道数据在哪里、含义是什么、是否可用、如何使用、来源何处以及哪些内容相似。
- 🧩 提供五项核心能力：Discover 生成或连接本体与知识图谱；Ground 统一指标、实体和关系定义；Validate 用认证定义与血缘校验查询；Expose 通过 MCP、CLI、API 暴露上下文；Learn 将认证修正和使用反馈回本体。
- 🏗️ 主要组件包括 Next.js 前端与 API 网关（3000）、FastAPI 后端（3001）、摄取 worker（3002）、MCP 服务（3003）、Postgres + pgvector（5432），以及可选的 HashiCorp Vault。
- 🤖 使用 NVIDIA NIM 模型角色：REASONING 负责构建本体、生成 SQL 与解释；NON_REASONING 处理意图、实体抽取、候选选择和 SQL 修复；EMBED 做向量检索；RERANK 做候选排序。
- 🚀 快速开始基于 Docker Compose 和 Wide World Importers 示例数据库，需要 uv 与 NVIDIA API key；启动后在 UI 开启语义编译即可用自然语言提问。
- 🔍 示例中，问题会被解析到本体术语并沿关系生成多表 SQL，返回答案、SQL 与执行步骤；当数据无法回答时，check_answerable 会报告覆盖不足并请求澄清。
- 🔌 集成方式包括 MCP 只读工具（如 search_terms、check_answerable、ask_question）、REST API 的 SSE 流式响应，以及安装、管理、查询三类 agent skills。
- 🗄️ 支持 PostgreSQL、MySQL、Databricks、Snowflake、ClickHouse、Trino、Apache Kyuubi、HeavyDB、DuckDB、SQLite 十种数据源。
- 🔮 配置 KUMO_RFM_API_KEY 后可将预测类问题路由至 KumoRFM；由于会向托管服务上传连接表数据，启用前需完成数据合规评估。
- 🔄 兼容 Apache Ossie 语义模型交换标准，支持通过 UI 或 API 导入导出 Ossie YAML。
- 📜 采用 Apache-2.0 许可证；项目当前不接受外部 pull request，但欢迎 issue、集成请求，安全漏洞应按 SECURITY.md 报告。
- ⭐ 仓库约有 8k stars、646 forks、42 watchers 和 1366 次提交。

---

### [GitHub - blitzcrieg1/agentmetry: Open-source security for AI coding agents: record, detect and block at the tool boundary, with a verifiable audit trail in the SIEM you already run. · GitHub](https://github.com/blitzcrieg1/agentmetry?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-770-november-5-2026)

**原文标题**: [GitHub - blitzcrieg1/agentmetry: Open-source security for AI coding agents: record, detect and block at the tool boundary, with a verifiable audit trail in the SIEM you already run. · GitHub](https://github.com/blitzcrieg1/agentmetry?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-770-november-5-2026)

Agentmetry 是一个面向 AI 编码代理的开源安全工具。它在工具调用边界记录代理行为，检测风险序列，可按策略在运行前阻止调用，并生成可验证的审计链，转发到现有 SIEM。当前为公开 alpha，API 和 hook payload 仍可能变化。

- 🛡️ **定位**：面向安全工程师和开发者，记录“哪个代理、哪个会话、哪次调用、顺序如何”；它是传感器，不是中央控制台。
- 🚀 **快速开始**：需要 Python 3.11+，可执行 `pip install agentmetry`；提供 `demo`、`doctor`、`benchmark`、`scan`、`dashboard` 等命令。
- 🧪 **演示与自检**：`demo` 通过真实摄取路径回放攻击会话，并演示篡改后 `verify` 失败、重哈希后通过；`doctor` 检查安装；`benchmark` 用检测语料评分规则。
- 🔍 **预运行扫描**：`scan` 检查 MCP 配置、skills、规则、`AGENTS.md`/`CLAUDE.md` 中的拼写仿冒包、提示注入、凭据访问、外泄和工具遮蔽等风险，但不启动服务器或拉取包。
- 🤖 **支持面**：Claude Code、Cursor、Codex、Qwen/Kimi/Qoder/CodeBuddy、GitHub Copilot CLI/VS Code 代理模式、Antigravity，以及 MCP stdio 代理；其他代理可通过摄取 API 记录。
- 💻 **平台**：Windows 和 Linux 在 CI 中测试；macOS 全套测试在 CI 中运行但非必需检查，且尚无 Mac 上真实代理 hook 验证。
- 🧭 **检测能力**：包含 14 条已发布序列规则和 1 条实验规则；例如 `credential-exfil` 匹配“凭据访问后网络外泄”，顺序反转不触发。
- 🏷️ **威胁映射**：对可识别工具调用打 MITRE ATT&CK 标签；对特定场景输出 MITRE ATLAS 标签，如间接提示注入、凭据收集、工具外泄、破坏和 MCP 供应链 rug pull。
- 📦 **事件与导出**：规范事件 schema 1.2.0，默认对参数做 SHA-256 哈希且不存秘密值；支持文件 JSONL、Webhook、CloudEvents、Elastic ECS、Splunk HEC、Google SecOps UDM、Microsoft Sentinel 等。
- 🧾 **证据与防篡改**：使用哈希链 JSONL；`verify` 检查链，`anchor` 记录检查点，`prove` 提供单事件包含证明，`export` 生成证据包或合规摘要；本地 anchor 需外部保存副本才能防全链重写。
- ❤️ **可见性**：`start` 每 300 秒发送心跳并列出已挂钩代理；SIEM 可告警“记录器沉默”或 `action.outcome: degraded`，后者表示记录器运行但某代理未被记录。
- 📊 **验证数据**：benchmark 共 57 个案例（26 攻击、31 良性），26 次预期触发全部检出，0 漏报、0 误报，覆盖 13 条规则；2108 个测试，Linux 行覆盖率 82.13%，CI 低于 78% 失败。
- 🚫 **边界**：不是沙箱、不是 CASB、不是控制台；hook 需合作，缺失事件不等于没发生；默认检测记录，DLP/工具策略设为 `block` 才可在运行前拒绝；审批多为推断；哈希链不证明“谁写的”。
- 🔐 **安全模型**：trail 默认留在本机；可设 `AGENTMETRY_HASH_KEY` 使用 HMAC-SHA256；除健康检查外 API 需 token；`AGENTMETRY_AUTH_DISABLED=1` 仅用于开发且 `doctor` 会标记。
- 📄 **许可与维护**：Apache-2.0，Copyright 2026 blitzcrieg1；由 Ioannis L. 维护；支持通过 SIEM 做舰队级问题排查，但本包不提供中央强制执行和集中分诊。

---

### [GitHub - MotleyAI/slayer：面向 AI 智能体与人类的可嵌入、富有表现力的语义层 · GitHub](https://github.com/MotleyAI/slayer?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-770-november-5-2026)

**原文标题**: [GitHub - MotleyAI/slayer: An embeddable, expressive semantic layer for AI agents and humans · GitHub](https://github.com/MotleyAI/slayer?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-770-november-5-2026)

SLayer 是 MotleyAI 开源的可嵌入、表达力强的语义层，面向 AI 代理和人类用户，在数据仓库之上提供受治理的共享数据与指标访问，帮助代理可靠地回答分析问题，并处理只读数据库连接、SQL 转换、常用数据变换和行级安全等复杂工作。

- 📊 项目定位：SLayer 可作为独立工具使用，也可作为 Python 库嵌入应用，用于构建分析型 MCP 服务器、API 或进行语义化数据库查询。
- 🔍 核心差异：不同于传统 BI 语义层需预定义每个指标及聚合方式，SLayer 允许定义一次字段后使用 `sum(revenue)`、`avg(revenue)`、比率、时间偏移和多阶段查询等表达式灵活查询。
- 🤖 面向代理流程：聚焦“搜索 → 检查 → 查询”的代理式分析流程，提供 `search` 工具和用于关联业务上下文的内存存储。
- 🔌 多种访问方式：支持 MCP、REST API、CLI、Python、Flight SQL 和基于 Postgres 的 SQL API。
- 🗄️ 数据生态：支持大多数流行数据库，并提供 dbt、Cube 和 Ossie 配置导入器，可配合现有数据栈使用。
- 🚀 快速开始：推荐使用 `uv tool install 'motley-slayer[all]'` 安装；可通过内置 Jaffle Shop 演示数据快速接入 Claude MCP，也可配置自己的数据源。
- 🔐 使用统计：`slayer` 命令最多每天发送一次匿名聚合使用统计，不包含查询、名称、数据或凭据；可通过 `SLAYER_USAGE_REPORTING=off`、`DO_NOT_TRACK=1` 或命令关闭。
- 📈 仓库概况：GitHub 仓库约 335 星、45 个 fork，采用 MIT 许可证，提交历史约 3,648 次。

---

### [请确认您不是机器人！](https://git.andros.dev/andros/tyrtulia?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-770-november-5-2026)

**原文标题**: [Making sure you're not a bot!](https://git.andros.dev/andros/tyrtulia?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-770-november-5-2026)

该内容是一个由 Anubis 提供的反机器人验证页面，要求浏览器启用 JavaScript 并完成计算任务（Proof of Work）以证明其为真实客户端；如果脚本加载失败，用户需要刷新页面，而部分隐私插件可能会阻止验证。

- 🤖 页面用于阻止机器人和恶意请求，作用类似 CAPTCHA。
- 🧮 浏览器需完成 Proof of Work 计算任务，通常几秒内完成并授予访问权限。
- 🔄 如果 Anubis 的 JavaScript 加载失败，可能是服务器过载，需要重新加载页面。
- ⚠️ 验证依赖现代 JavaScript 功能，JShelter 等插件需对该域名禁用。
- 🚫 必须启用 JavaScript 才能通过挑战，无 JavaScript 方案仍在开发中。
- 🛡️ 该网站由 Anubis（Techaro 出品）保护，当前版本为 v1.28.2。

---

### [GitHub - swarfte/django-ninja-expose · GitHub](https://github.com/swarfte/django-ninja-expose?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-770-november-5-2026)

**原文标题**: [GitHub - swarfte/django-ninja-expose · GitHub](https://github.com/swarfte/django-ninja-expose?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-770-november-5-2026)

django-ninja-expose 是一个基于 Django 与 django-ninja 的轻量库：给 Django 模型加上 `@expose()` 后，即可自动生成带过滤、分页、OpenAPI 文档、认证与对象级授权配置的 REST CRUD API。

- 🚀 核心用法：在 Django 模型上使用 `@expose()`，再通过 `NinjaAPI()` 与 `mount(api)` 挂载，即可生成 `/api/Task` 等端点。
- 🔗 自动路由：为模型生成 `GET/POST /api/<Model>` 以及 `GET/PUT/PATCH/DELETE/HEAD /api/<Model>/{pk}`。
- 🔍 查询能力：支持 Django 原生过滤（如 `?title__icontains=x&completed=false`）、Ninja 默认分页（`limit/offset`）和 OpenAPI 文档。
- 🧩 `@expose` 参数：`path`、`methods`、`fields`、`query`、`auth`、`queryset` 可控制路径、允许方法、暴露字段、可过滤字段、认证与查询集；`None` 表示自动，`[]` 表示禁用，列表表示显式限制。
- 🛡️ 认证机制：库本身不实现认证，`auth` 可继承 API 认证（`INHERIT`）、设为 `None` 公开、传入 Ninja/Django 认证对象或可调用对象，也可传列表。
- 👤 对象级授权：`queryset` 是 `(request, qs) -> qs` 的可调用对象，作为每次操作的起始查询集；列表/过滤/分页仅见授权数据，越权访问返回 `404`，POST 越权创建会回滚并返回 `403`。
- ⚠️ 安全警告：`@expose()` 默认暴露模型数据与 CRUD 操作；使用 `INHERIT` 时需确保 `NinjaAPI(auth=...)` 已配置，生产环境应限制 `methods`、`fields` 和 `query`。
- 📌 其他限制：外键与多对多字段以主键表示；过滤仅允许白名单字段，关系遍历会被拒绝并返回 `400`；写入会执行 Django `full_clean()`，不可编辑字段不可写。
- 📦 仓库信息：Apache-2.0 许可证，约 4 个 Star、0 个 Fork、8 次提交；README 提供完整 CRUD、Python 调用和安全配置示例。

---

### [GitHub - anthonyGosme/speedrunner: Makes aws, az, gcloud, ansible, eslint, rubocop, composer and hundreds of other Python, Ruby, PHP and Node CLIs start several times faster: each stays loaded in a daemon that forks it on every call. A checks script: 24.0 s → 5.3 s, same output. No per-tool config, one binary, Linux and macOS. · GitHub](https://github.com/anthonyGosme/speedrunner?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-770-november-5-2026)

**原文标题**: [GitHub - anthonyGosme/speedrunner: Makes aws, az, gcloud, ansible, eslint, rubocop, composer and hundreds of other Python, Ruby, PHP and Node CLIs start several times faster: each stays loaded in a daemon that forks it on every call. A checks script: 24.0 s → 5.3 s, same output. No per-tool config, one binary, Linux and macOS. · GitHub](https://github.com/anthonyGosme/speedrunner?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-770-november-5-2026)

speedrunner 是一个开源命令行加速工具：它让 Python、Ruby、PHP、Node 编写的 CLI 在守护进程中预加载，并在每次调用时 fork，从而显著减少解释器启动和加载代码的开销，且无需逐工具配置。

- 🚀 可将 aws、az、gcloud、ansible、eslint、rubocop、composer 等数百个 CLI 的启动速度提升数倍，同时保持输出与原生运行一致。
- ⏱️ 示例检查脚本从 24.0 秒降至 5.3 秒，约 4.5 倍；首次运行因守护进程冷启动约 3 倍。
- 📊 基准测试覆盖 96 个命令，输出全部与原生一致；几何平均加速 5.5 倍，中位数 4.8 倍，74 个命令达到 3 倍以上。
- ✍️ 编辑器保存场景：eslint 328→43 ms，mypy 213→50 ms；pre-commit 提交从 1.11 秒降至 0.31 秒。
- 🧰 使用方式包括 `srr aws s3 ls`、`speedrunner exec ./script.sh`、`eval "$(speedrunner activate)"`，以及 `init zsh/bash` 预热守护进程。
- 📦 安装支持安装脚本、Homebrew、Debian/Ubuntu APT 仓库和 Arch AUR；安装脚本会校验 SHA-256，并提供签名构建溯源。
- 🖥️ 支持 Linux x86_64/aarch64 与 macOS 11+（Intel/Apple Silicon）；Windows 暂不支持。
- ⚙️ PHP 工具需 FFI 扩展，Node 工具需 Node 22.15+，Node 支持仍属实验性；单线程 V8 可能拖慢计算密集型工具。
- 🧠 每个工具一个守护进程，典型内存 28–40 MB，Node 约 60 MB，最大可到 200 MB；闲置 4 小时后自动退出。
- ⚠️ 当命令自身工作或网络耗时占主导、工具加载时启动线程（如 vite）、或为原生二进制时，加速有限或不适用；无法忠实服务时会回退到原生运行。
- 🪪 项目采用 Apache-2.0 或 MIT 双许可证。

---

### [GitHub - colloq-edu/colloq：用于共同教授 Python、数据科学和机器学习的自托管课堂。学生只需提供姓名即可从浏览器加入 · GitHub](https://github.com/colloq-edu/colloq?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-770-november-5-2026)

**原文标题**: [GitHub - colloq-edu/colloq: Self-hosted classroom for teaching Python, data science and ML together. Students join from a browser with just a name · GitHub](https://github.com/colloq-edu/colloq?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-770-november-5-2026)

Colloq 是一个可自托管的实时课堂平台，面向 Python、数据科学与机器学习教学。教师分享一个链接，学生只需输入姓名即可在浏览器加入同一个实时 Notebook，无需账号、安装或环境配置；项目采用 MIT 许可，目前处于 1.0 之前阶段。

- 🎓 **核心定位**：一个链接、一个实时 Notebook、整个课堂共享同一份代码、文件与运行环境。
- 🔗 **学生体验**：浏览器即用，无需安装；同一链接可随时回到课堂。
- 🧑‍🏫 **三种课堂模式**：Standard 共同编辑与运行；Lecture 教师授课并可用 iPad/手写笔演示 PDF；Council 学生各自作答，教师审阅并展示答案。
- 🔒 **规则与权限**：预设模式加单元格锁定，服务器强制执行编辑、运行、提问、文件访问等权限。
- 🤖 **AI Oracle**：课堂共享问答线程，支持 Ask 解释/建议修改，Act 调用工具读写文件、运行代码；兼容 OpenAI 接口与本地模型。
- 📁 **课堂协作**：共享文件与终端、实时输出、Notebook 版本历史、活动日志、`.ipynb` 导入导出。
- 📚 **教学扩展**：课程/班级页面、Python 环境、GPU 环境、课堂结束后只读保存并可恢复。
- 🧪 **竞赛与比赛**：Competitions 支持 Notebook 提交与指标评分；Contests 支持算法题、测试点、ICPC/IOI 榜单。
- ⚙️ **快速开始**：`pip install colloq` 后运行 `colloq start`；需要 Docker，部分平台需 Node.js 22+。
- 🌐 **分享课堂**：`colloq start --share` 可生成临时公网链接；也支持自有 relay、命名隧道与直接 HTTPS。
- ☸️ **生产部署**：支持自有 Kubernetes Helm Chart、单台 Linux VM、单节点 k3s 预览，以及 Vast.ai GPU 镜像。
- 🛡️ **安全边界**：隔离主要发生在班级之间；每个教室的 Python 运行在独立容器中，可访问互联网但默认阻断本地网络。
- ⚠️ **安全注意**：Docker 路径下服务器控制 Docker daemon，不等同于虚拟机隔离；需按运行时边界评估不可信负载。
- 📦 **版本与许可**：版本以根 `package.json` 为准，使用 release-please 发布；MIT 许可，主要由单人维护。
- 🚫 **不是 LMS**：不提供课程进度跟踪、自动评分、SSO 或视频会议，适合搭配现有会议工具用于实时教学。

---

### [Django 安全版本发布：6.1.3、6.0.10 和 5.2.19 | 博客 | Django](https://www.djangoproject.com/weblog/2026/nov/03/security-releases/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-770-november-5-2026)

**原文标题**: [Django security releases issued: 6.1.3, 6.0.10, and 5.2.19 | Weblog | Django](https://www.djangoproject.com/weblog/2026/nov/03/security-releases/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-770-november-5-2026)

Django 团队于 2026 年 11 月 3 日发布 Django 6.1.3、6.0.10 和 5.2.19 安全版本，修复多个安全漏洞，并建议所有用户尽快升级。受影响分支包括 main、6.1、6.0 和 5.2，相关补丁已应用至这些分支。

- 🔐 **发布版本**：Django 6.1.3、6.0.10、5.2.19 为安全更新版本，由 Jacob Walls 发布。
- 💾 **CVE-2026-108147（低危）**：`MultiPartParser` 处理 `Content-Transfer-Encoding: base64` 上传时可能将内容全部缓冲到内存，绕过 `FILE_UPLOAD_MAX_MEMORY_SIZE`，导致内存耗尽。
- 📝 **CVE-2026-111211（低危）**：`GeometryField` 及其组件直接记录未转义的无效几何表单值，可能通过控制字符引发日志注入或伪造。
- 🌐 **CVE-2026-111362（中危）**：GeoJSON 几何的 `crs` 成员可触发 SSRF；GDAL 会解析外部 URL，用户输入在验证、保存或查询路径中可能发起网络请求或读取文件。现在空间字段查询、`GeometryField` 和 `GEOSGeometry` 会拒绝外部 CRS 引用，可信数据加载工具仍可接受。
- 🗄️ **CVE-2026-113593（低危）**：`UpdateCacheMiddleware` 和 `cache_page()` 对“缺少 Vary 头”和“Vary 头为空值”的请求生成相同缓存键，可能泄露私有数据；现已按 RFC 9111 区分缺失与空值，旧缓存将不再匹配并会重新缓存。
- 🔑 **CVE-2026-113733（低危）**：仅拥有查看权限的管理员在自定义用户模型场景下可能看到完整密码哈希；涉及非 `AUTH_USER_MODEL` 或通过多表继承获得 `password` 字段的情况。
- 🧭 **CVE-2026-114582（低危）**：`SpatialReference` 字符串输入可经 GDAL 解析 URL 或读取文件，导致 SSRF；影响 `transform()`、`srs`/`srid` setter 等。修复后 GDAL 3.9+ 禁用网络和文件访问，所有版本拒绝 `DICT:`/`ESRI:` 引用，建议优先使用整数 SRID，并注意 `gis.W001` 检查警告。
- 🛠️ **修复与发布**：补丁已进入 main、6.1、6.0、5.2 分支，并发布对应 tarball 与校验和。
- 📧 **安全报告**：潜在安全问题应私信 `security@djangoproject.com`，不要通过 Trac 或 Django Forum 报告。

---

### [ClePy November Meetup - OpenDroneMap, Tue, Nov 10, 2026, 6:00 PM   | Meetup](https://www.meetup.com/cleveland-area-python-interest-group/events/317106926/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-770-november-5-2026)

**原文标题**: [ClePy November Meetup - OpenDroneMap, Tue, Nov 10, 2026, 6:00 PM   | Meetup](https://www.meetup.com/cleveland-area-python-interest-group/events/317106926/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-770-november-5-2026)

本次 ClePy 十一月聚会以 OpenDroneMap 为主题，将于 11 月 10 日周二 18:00–20:00 EST 在克利夫兰 Happy Dog 地下室举行，包含社交、演讲和清理环节，重点介绍开源无人机影像处理平台 ODM 的安装、使用与贡献方式。

- 📅 时间：11 月 10 日（周二）18:00–20:00 EST
- 📍 地点：Happy Dog（Underdog 地下室），5801 Detroit Ave, Cleveland, OH
- 👥 主办：Cleveland Area Python User Group（CLEpy），主持人 Eddie C. 和 Anurag S.
- 🗓️ 议程：18:00–18:30 社交、布置与公告；18:30–19:30 演讲；19:30–20:00 社交与清理
- 🎤 演讲：India Johnson 分享“OpenDroneMap: A Community-focused Solution to Making Drone Data Usable”
- 🛰️ ODM 是开源平台，可将无人机原始影像处理为 2D 正射影像/高程模型和 3D 点云/纹理网格
- 🌳 应用场景包括场地规划、树冠分析、水文和作物分析等
- 💻 代码托管于 GitHub，主项目与 WebUI 主要以 Python 编写，欢迎贡献
- 🧪 现场将用无人机测试数据演示 ODM 安装与使用，并介绍参与贡献的方式
- 🔔 若已 RSVP“参加”但无法到场，请更新回复，便于统计人数并让候补者参加
- 🗣️ 想演讲可在 Meetup 或 Cleveland Tech Slack 的 #clepy 频道联系
- 🙌 赞助：Python Software Foundation；Happy Dog 提供场地和设备

---

### [Python 3.15 有哪些新特性，2026 年 11 月 12 日星期四 下午 6:30 | Meetup](https://www.meetup.com/madison-python/events/317147553/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-770-november-5-2026)

**原文标题**: [What's New in Python 3.15, Thu, Nov 12, 2026, 6:30 PM   | Meetup](https://www.meetup.com/madison-python/events/317147553/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-770-november-5-2026)

这是一场由 MadPy 主办、Ed R. 主持的线下技术分享活动，主题为“Python 3.15 新特性”，将介绍该新版 Python 的重要更新，包括性能优化、类型系统新功能、惰性导入等，并由 Workday 首席机器学习工程师 Josh Karpel 主讲。

- 📅 活动时间：11 月 12 日（周四）18:30–20:30 CST
- 📍 活动地点：Madison Public Library - Central，201 W Mifflin St, Madison, WI
- 🐍 主题内容：快速概览 Python 3.15 的新特性与重要变化
- ⚙️ 重点包括：内置采样分析器、底层性能改进、垃圾回收器相关变更、类型系统新功能、惰性导入等
- 🎙️ 主讲人：Josh Karpel，Workday 首席机器学习工程师，负责设计并开发连接 ML 预测与外部世界的系统
- 🎓 主讲背景：拥有 UW-Madison 物理学博士学位，曾在 Morgridge Institute 担任博士后研究员，通过 Center for High Throughput Computing 支持大规模科研计算
- 🏷️ 相关主题：Madison 本地活动、数据科学、Python、开源、软件开发、科学计算

---

### [AI 系统如何泄露其构建所依据的数据，2026](https://www.meetup.com/charlottesvilledatascience/events/317269604/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-770-november-5-2026)

**原文标题**: [How AI Systems Leak the Data They're Built On, Wed, Nov 11, 2026, 6:00 PM   | Meetup](https://www.meetup.com/charlottesvilledatascience/events/317269604/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-770-november-5-2026)

本次活动聚焦已部署的 AI 系统如何在实际中泄露其训练或检索数据、遭受攻击，由 AI 安全专家 Hunter Moore 主讲，结合真实案例讲解攻击方式、防御有效性及数据科学团队可立即采取的措施。

- 🗓️ 活动时间：11 月 11 日周三 18:00–20:00 EST，线下举行。
- 📍 地点：Vault Virginia，300 E Main St，Charlottesville, VA。
- 🏢 主办方：Charlottesville Data Science（PyData Group）；赞助方：NumFOCUS。
- 🎙️ 主讲人：Hunter Moore，Charlottesville AI 安全初创公司 Hardshell 联合创始人兼 CTO。
- 🔐 核心主题：AI 系统如何泄露其构建数据，包括间接提示注入、系统提示词提取、通过渲染输出进行数据外泄，以及诱导模型泄露敏感数据的隐私攻击。
- 🧠 RAG 风险：检索增强生成让语言模型可指向组织文档，但也使每份文档都可能成为潜在指令。
- 📚 真实案例：隐藏网页文本劫持 Bing Chat、Air Canada 因其聊天机器人答复被判承担责任等。
- 🛡️ 防御讨论：哪些防御有效、哪些在自适应攻击者面前失效，以及数据科学团队可立即采取的行动。
- 👨‍🎓 背景要求：无需安全背景；熟悉 LLM 与 RAG 会有帮助。
- 🎓 讲者资历：Hunter Moore 拥有 UVA 系统工程博士，曾为美国国防部提供 5 年以上 AI 安全建议，并为美国空军、USASOC 和 UVA 授课。
- 🔄 活动通知：组织方正在将活动日历迁移至 Luma，后续规划和沟通将通过 Luma 进行，Meetup 仍会继续交叉发布活动。

---

