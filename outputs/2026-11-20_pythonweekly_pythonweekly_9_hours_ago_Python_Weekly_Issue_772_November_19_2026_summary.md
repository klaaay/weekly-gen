### [PyCon 美国 2027 :: pretalx](https://pretalx.com/pycon-us-2027/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-772-november-19-2026)

**原文标题**: [
            
            PyCon US 2027 ::
            pretalx
        ](https://pretalx.com/pycon-us-2027/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-772-november-19-2026)

PyCon US 2027 已开放征稿，欢迎各类 Python 使用者投稿；会议将在加州长滩线下举行，并强调需新建投稿账号、提供差旅补助、重视安全与行为准则，征稿截止日期为 2026 年 12 月 19 日。

- 🐍 欢迎专业开发者、爱好者以及对 Python、编程和开源社区感兴趣的人投稿。
- 📍 所有讲者需在加州长滩的 Long Beach Convention and Entertainment Center 现场演讲。
- 🆕 PyCon US 2026 使用的 Pretalx 账号不会沿用，2027 投稿者需重新创建账号。
- ✈️ 将为讲者提供差旅补助，不应因费用问题而放弃投稿。
- 🛡️ 社区安全是首要任务，投稿前需阅读 PyCon US 2027 健康与安全指南。
- 📜 所有讲者都应阅读并遵守会议行为准则。
- 🗓️ Talks、Tutorials、Charlas 和 Poster 征稿开放至 2026 年 12 月 19 日。
- ✏️ 投稿者可编辑或查看提案，并提交提案。

---

### [是什么让 uv 变慢？ - 博客](https://blog.schuetze.link/what-makes-uv-slow/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-772-november-19-2026)

**原文标题**: [What makes uv slow? - Blog](https://blog.schuetze.link/what-makes-uv-slow/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-772-november-19-2026)

uv 的速度主要来自持续的性能剖析、复用成熟的 CPU 密集实现、缓存、并发和减少分配；它的“慢”通常来自外部构建工具、网络请求、CPU 密集操作、磁盘 I/O、同步代码、内存分配与复杂回溯等固有瓶颈。文章结合 Jupyter、Airflow、boto3、Home Assistant、Plotly 等真实基准，逐项解释 uv 在哪些场景会慢，以及做了哪些优化。

- 🧭 优化优先级大致是：先消除外部构建工具，再减少网络请求，再优化 CPU 密集代码、磁盘读写、单线程同步代码、分配/拷贝/系统调用；经典“大 O”优化较少。
- 📊 基准显示冷缓存与热缓存差异巨大：Airflow 冷缓存 `uv sync` 桌面约 54s、树莓派约 10.5min；Plotly 冷安装桌面 310ms、树莓派 2.3s、Windows 4.8s，热缓存分别降至 40ms、120ms、900ms。
- 📝 TOML 解析：`uv.lock` 用 TOML 便于审阅和生成良好 diff，但 Rust TOML 解析器较慢，Airflow 锁文件读取解析约 30ms；大型 workspace 还会重复解析成员 `pyproject.toml`。
- 🔮 预取：uv 根据 pubgrub 状态并行预取包/版本元数据和构建；batch prefetch 在 boto3 回溯场景把冷缓存解析从 40s 降到 2s，但热缓存下可能带来约 16% CPU 开销。
- 🧩 缺失 wheel 与动态元数据：没有静态元数据时需下载完整 sdist、建隔离 venv、解析构建依赖并执行 Python 钩子；wheel 安装中位约 240ms，sdist 中位约 13s，原生代码构建更慢。
- 🌐 Simple API 与索引协议：缺少 PEP 658 和 HTTP Range 时需下载整包，回溯 torch 可能重复下载数百 MB；每个版本依赖信息还常需额外网络往返；uv 用 msgpack、rkyv 等减少解析成本。
- 🔢 版本表示：版本创建、复制、比较极多；uv 用小版本类型（16 字节、可单指令比较/复制）和 `Arc` 包装大版本；去掉小版本使 boto3 热解析慢 2.1x，再去掉 `Arc` 慢 4.7x。
- 🏷️ Markers 与元数据：marker 用代数决策图规范化并 intern 节点；包名、extra、group 用短字符串优化；pubgrub 虚拟包 intern 为 32 位整数；Airflow 约 1k 个 intern 节点、368KB 直接分配。
- 🔐 哈希：校验 SHA-256 较慢；BLAKE3 在桌面 1GB 文件约快 4.7x、树莓派约 2.1x；但 SHA-256 是生态标准且索引普遍提供预计算值，uv 仍用它，主要影响 CPU 负载而非网络下载。
- 📦 虚拟环境：安装需遍历并复制/链接整棵包树；reflink 可避免重复大文件并保护缓存，但难自动判断最快方式；uv venv 仅约 84KB，Docker 中仍推荐使用 venv。
- 🗜️ 压缩：wheel 用 DEFLATE、sdist 用 gzip，通常比 zstd 文件更大、解压更慢；uv 用流式 zip/tar 边下载边解压，网络常是限速点，但 CPU 和下载体积仍重要。
- 🔁 回溯：pubgrub 负责复杂解析；uv 记录冲突涉及的包，在过度回溯时切换优先级并手动回溯；启发式较保守以保证确定性和低 churn；真实库热缓存解析最慢约 160ms。
- 🧵 并发：混合网络、磁盘、CPU 负载调度很难；uv 混用 tokio、`spawn_blocking`、rayon 和 Python 子进程池；并发限制为 1 时 Airflow 冷解析 16s 变 26s，Jupyter 200ms 变 762ms。
- 🐍 解释器发现：uv 需查询外部 Python 的版本、路径、ABI、libc 等信息，Python 3.14 约 30ms，约占 `uv pip install --no-cache tqdm` 的 25%；结果可缓存，未来 `build-details.json` 可改善。
- 📡 不可靠网络与批量刷新：CI 网络失败需重试、等待或续传下载；`uv pip install` 对 n 个包需 n 次重新验证，缺少批量刷新端点，受网络并行度限制。
- 🌿 Forking：不同平台或 Python 范围可能需要分叉解析；uv 在发现平台 marker 差异或版本不支持完整 Python 范围时 fork，按优先级串行处理并尽量复用先前版本和元数据。
- 🧱 类型布局与内存：Rust 标准类型常非最优；uv 用手动 `Box`、`Arc`、`Cow`、`SmallVec`、小字符串等减少分配，但需类型大小断言和 `Box::pin`；Airflow 热缓存 `uv run` 仍用 110MB、10.7GB 分配、880 万次分配。
- 🧹 释放内存：`Drop` 递归释放，大量 `Arc` 版本和解析结构带来原子引用计数开销；Airflow 解析约 1.4% 时间用于释放解析结构，部分与主线程并行。
- 🦀 Rust 库、胖 wheel 与系统 ABI：crate 生态性能关键；numpy/torch 胖 wheel 合并多微架构/GPU 代码，浪费空间且缺少变体选择；依赖系统库的包常无 wheel，安装慢且环境难配。
- 🐍 Python 解释器：python-build-standalone 提供最快 CPython 构建，可用 `uv python install`；Linux 上 glibc 通常快于 musl，因此不建议 musl 作为 Python Docker 基础镜像。
- 🛠️ 工具与测量：criterion/codspeed 做持续基准，samply/hyperfine/tracing 做剖析；walltime、CPU profile、span 各有局限，基准噪声、构建配置和机器环境都会影响数字。

---

### [No module named 'distutils', 'imp', 'cgi': the PyPI packages that still break](https://py-code.org/blog/removed-stdlib-modules-pypi/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-772-november-19-2026)

**原文标题**: [No module named 'distutils', 'imp', 'cgi': the PyPI packages that still break](https://py-code.org/blog/removed-stdlib-modules-pypi/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-772-november-19-2026)

文章基于 2026 年 11 月 13 日的数据，分析了 PyPI 上仍导入 Python 3.12 和 3.13 已移除标准库模块的项目，重点揭示了大量高下载量、长期未维护的包在导入时会失败，并讨论了废弃依赖带来的维护与安全风险。

- 🐍 Python 3.12 移除了 `distutils`、`imp`、`asyncore`、`asynchat`、`smtpd`；Python 3.13 又移除了 19 个 PEP 594 模块和 `lib2to3`，共 25 个模块。
- 📊 在索引的 354,763 个 PyPI 项目中，3,763 个项目导入了被移除模块，其中 1,623 个项目在自身代码中存在未加保护的导入，实际会失败。
- 📦 在下载量最高的 60,000 个项目中，852 个存在未加保护的导入；其中 544 个已两年没有发布新版本，但过去 30 天仍获得约 1.26 亿次下载。
- ⚠️ `nose` 和 `boto` 仍分别有约 180 万和 340 万月下载量，合计约 520 万；但 `import nose` 和 `import boto` 在 Python 3.12 及以后会失败，二者最后发布年份分别为 2015 和 2018。
- 🛠️ `distutils` 是被导入最多的移除模块：2,565 个项目导入，973 个未加保护；不过安装 `setuptools` 可临时恢复，长期应改用 `sysconfig`、`shutil.which`、`packaging` 等。
- 🧩 Python 3.13 移除的模块中，`cgi`、`imghdr`、`telnetlib` 影响较多项目；例如 `coreapi`、`htmlmin`、`pgpy` 等包在导入时会失败。
- 🎵 `pydub` 的导入保护并不充分：它先导入已移除的 `audioop`，再回退到不存在的 `pyaudioop`，因此 Python 3.13 下 `import pydub` 会报错；安装 `audioop-lts` 可修复。
- 🔍 检查依赖的最快方法是在不含 `setuptools` 的全新虚拟环境中用 Python 3.13 运行测试；也可用 py-code.org、`uvx py-code-org who-uses imp` 或 DuckDB 查询索引。
- 🚨 文章强调，导入已移除模块本身不等于不安全，但它是包无人维护的明显信号；AI 正加快漏洞发现与利用，废弃包既难以及时修复，也更容易被劫持或长期遗留漏洞。
- ✅ 对无法修改的依赖，可安装对应 PyPI 兼容包，如 `legacy-cgi`、`audioop-lts`、`zombie-imp`；更长期的方案是迁移到维护中的替代品，如用 `pytest` 替代 `nose`、用 `boto3` 替代 `boto`。

---

### [理解现代大语言模型中的位置嵌入](https://magazine.sebastianraschka.com/p/understanding-positional-embeddings?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-772-november-19-2026)

**原文标题**: [Understanding Positional Embeddings in Modern LLMs](https://magazine.sebastianraschka.com/p/understanding-positional-embeddings?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-772-november-19-2026)

overview summary
本文系统梳理现代大语言模型如何编码 token 位置信息：从 GPT-2 的可学习绝对位置嵌入、原始 Transformer 的固定正弦/余弦编码，到当前主流的 RoPE 相对位置方法，并给出频率公式与 PyTorch 实现。文章还讨论部分 RoPE、NoPE 层、学习式相对位置偏置等新变体，并基于 2025–2026 开源模型架构统计指出全层 RoPE 仍最常见但占比下降，部分 RoPE 与混合 NoPE 正在增多。

- 🧭 位置信息必要：词序改变语义；显式位置信号补充因果掩码只能提供隐式顺序、无法区分间隔大小的问题。
- 🧱 GPT-2 方法：训练可学习绝对位置嵌入表，与 token embedding 逐元素相加后进入首个 Transformer 块；上下文长度固定，扩展成本高。
- 🌊 原始 Transformer：使用固定正弦/余弦函数生成绝对位置编码，按特征对赋不同频率；固定偏移对应固定旋转，便于学习相对关系。
- 🔄 RoPE 核心：在注意力内用 token 位置旋转 query/key 向量，value 不旋转；QK 点积主要依赖相对偏移，因此同时平移两个位置可保持固定 Q/K 下的分数。
- 📐 RoPE 频率：每个头维度 d 有 d/2 对特征，常用 θ_i=b^{-2i/d}，原始 b=10000；实现有 split-half 与 interleaved 两种等价配对约定。
- 💻 实现要点：预计算 cos/sin 表并按位置、批次和头广播；仅对 Q、K 应用旋转，再算缩放点积、因果掩码、softmax 与 value 加权。
- 🧩 现代变体：部分 RoPE 只旋转每头部分维度（如 MiniMax-M3 的 64/128）以省内存；NoPE 在某些层省略显式位置编码（如 SmolLM3 每四层跳过 RoPE）。
- 🎯 学习式相对偏置：Inkling 等在 softmax 前按 query 隐状态和 key 距离加入可学习偏置，延续 T5 思路。
- 📊 趋势统计：2025–2026 架构库中“每层都用 RoPE”仍最常见但占比下降；部分 RoPE 在 RoPE 模型中渐成多数，RoPE/NoPE 混合与纯 NoPE 也在增加。
- 🔮 结论：RoPE 仍是主流位置编码方法，预计延续到 2027；未来可能看到更多 Inkling 式学习相对偏置设计。

---

### [函数式编程会让你成为更优秀的 Python 开发者 - YouTube](https://www.youtube.com/watch?v=bcdZlYPn3BA&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-772-november-19-2026)

**原文标题**: [Functional Programming Will Make You a Better Python Developer - YouTube](https://www.youtube.com/watch?v=bcdZlYPn3BA&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-772-november-19-2026)

该内容为 YouTube 页脚信息汇总，主要涵盖平台政策与安全、创作者与广告/开发者入口、版权与联系方式、公司主体信息，以及创作者推荐商品的销售免责声明。

- 📄 提供信息、新闻稿、版权、咨询及政策与安全等平台相关入口。
- 👤 面向创作者、广告主和开发者提供相应服务与资源链接。
- ⚖️ 列出使用条款、隐私政策、政策与安全、YouTube 运作原理及新功能测试说明。
- 🏢 公司信息显示为 © 2026 Google LLC，CEO 为 Sundar Pichai，并包含地址、免费电话、支持邮箱及托管方 Google LLC。
- 🚨 提供事业者信息与非法拍摄物举报入口。
- 🛒 创作者在 YouTube 上发布、标记或推荐的商品按卖家条款销售，YouTube 不销售这些商品且不承担责任。

---

### [对 PyPI 上上传的分发包进行更严格的检查 - Python 包索引博客](https://blog.pypi.org/posts/2026-11-18-stricter-checks-for-uploaded-sdists/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-772-november-19-2026)

**原文标题**: [Stricter checks for uploaded distributions on PyPI - The Python Package Index Blog](https://blog.pypi.org/posts/2026-11-18-stricter-checks-for-uploaded-sdists/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-772-november-19-2026)

PyPI 正在加强对上传分发包的归档格式检查，以减少 Python 打包生态中的解析差异风险；这些变化对普通下游用户没有破坏性影响，主要要求包维护者使用合规的构建后端生成 sdist 和 wheel。

- 📦 **背景**：Python 包主要有源码分发 sdist（`.tar.gz`）和构建分发 wheel（`.whl`），但 tar 与 ZIP 并非为包分发设计，宽松解析可能造成不同工具“看到”不同内容。
- 🛡️ **安全目标**：防止攻击者利用解析差异，让 PyPI、镜像、安全扫描器和安装器对同一分发包产生不一致理解，甚至安装恶意内容。
- 🚫 **新增拒绝规则**：PyPI 已开始拒绝使用“V7”风格 tar 归档的源码分发，以及包含可能被误读为 ZIP 控制结构的归档级注释的 wheel。
- 👥 **对下游用户**：没有破坏性影响；已通过 `pip install` 或 `uv add` 依赖的分发包会继续正常工作。
- 🔧 **对维护者**：绝大多数不受影响；若上传因归档格式被拒，应查阅 PyPI 归档文档，并使用 Python 构建后端，而不是手动用 `tar`、`zip` 打包。
- 📐 **格式要求**：sdist 必须是 POSIX pax 风格 tar；使用 GNU tar 时需加 `--format=pax`，并避免 sparse 成员和 pax 供应商扩展；wheel 必须是有效 ZIP；两者成员文件名都需 UTF-8 编码。
- 🚀 **后续计划**：PyPI 将继续与 Python 的 `zipfile`、`tarfile` 及打包标准对齐，寻找“最小干扰”的限制，近期将评估完全拒绝 GNU tar 和完全拒绝 ZIP 注释。

---

### [微软 agent-framework 在 PyPI 上两次遭入侵 | SafeDep](https://safedep.io/blog/microsoft-agent-framework-pypi-compromise?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-772-november-19-2026)

**原文标题**: [Microsoft agent-framework Compromised Twice on PyPI | SafeDep](https://safedep.io/blog/microsoft-agent-framework-pypi-compromise?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-772-november-19-2026)

概览摘要：微软官方 Python 元包 agent-framework 于 2026 年 11 月 17 日遭供应链攻击。恶意版本 1.26.1 和 1.26.2 通过 `.pth` 文件在每次 Python 启动时自动执行窃密程序，因此无需导入包；在 CI 中执行一次 `pip install` 就足以触发。该程序会窃取环境变量、凭据文件和其他进程环境，并主动申请 Azure DevOps、Azure 托管身份及 GitHub Actions OIDC 令牌，再将结果外传至 webhook.site。最后一个干净版本是 1.26.0。

- 🚨 1.26.1 于 20:35 发布，20:57 被标记；1.26.2 于 21:08 发布，21:12 被标记；两个版本均已被 PyPI 移除。
- 🧨 恶意版本只发布 wheel，不发布 sdist；1.26.1 通过 `agent_framework_meta.pth` 触发，1.26.2 改用 `af_runtime_diag.pth` 和 `af_runtime_diag.py`，并新增 GitHub Actions OIDC 窃取。
- 🕵️ 程序会窃取名称含 `TOKEN`、`SECRET`、`KEY`、`AZURE`、`AWS`、`GITHUB` 等 31 类关键词的环境变量、最多 60 个凭据文件，以及最多 300 个 `/proc/<pid>/environ` 中其他进程的密钥。
- 🎟️ 程序会主动请求 Azure DevOps 联邦令牌、Azure 托管身份令牌（Resource Manager、Key Vault、Storage、Graph 等）以及 GitHub Actions ID Token。
- 📡 数据会先经 zlib 压缩和 Base64 编码，再发送至 `hxxps://webhook[.]site/d381fd80-ec62-42ad-8f5c-d1b15103c9bb?t=telemetry`；两个版本共用该端点。
- 👤 PyPI 维护者账号 `vibiret` 于攻击当天注册，可发布 agent-framework 及五个关联项目；其中四个会随 1.26.0 安装。该账号疑似为上传者，但尚未获 PyPI 或 Microsoft 确认；项目月下载量约 19.2 万次。
- 📅 这是六个月内第二起微软 PyPI 包被植入恶意版本的事件；5 月 `durabletask` 1.4.1 至 1.4.3 也曾被入侵，但暂无证据表明两起事件有关联。
- ⏱️ 1.26.1 下架后，攻击者仍能发布 1.26.2，说明仅删除恶意版本并未切断其发布权限。
- 🔍 应检查锁文件与依赖文件中的 1.26.1、1.26.2；在镜像和 runner 上查找 `.pth` 与窃密文件哈希时，不要启动其 Python 环境。
- 🔐 安装过任一恶意版本的环境应视为所有可达密钥已泄露；应轮换密钥并审查 Azure 托管身份、联邦凭据及相关登录/活动日志，并注意轮换不能撤销已签发令牌。
- 📌 使用带哈希的完整依赖锁定，暂缓升级 agent-framework 及五个关联项目，直到 Microsoft 移除 `vibiret` 并确认发布干净。
- 🧾 关键 IoC 包括两个 wheel 的 SHA-256、两个 `.pth`、两个窃密脚本、webhook 地址、User-Agent `af-runtime-diagnostics/1` 与 `runtime-diagnostics/1`、环境变量 `_AF_TEL` 及账号 `vibiret`。

---

### [Laurence Tratt：为 yk 适配 CPython](https://tratt.net/laurie/blog/2026/adapting_cpython_for_yk.html?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-772-november-19-2026)

**原文标题**: [Laurence Tratt: Adapting CPython for yk](https://tratt.net/laurie/blog/2026/adapting_cpython_for_yk.html?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-772-november-19-2026)

overview summary
文章讲述作者将 yk（为 C 解释器自动添加元追踪 JIT 的工具）适配到 CPython，形成 ykcpython。适配约 3–4 天、约 450 行改动，在 AWFY 基准上多数项目快于 CPython，13 项中 8 项快于 CPython 实验 JIT；但作者强调 ykcpython 尚未生产可用，基准有限，真实程序效果可能差很多。

- 🐍 **目标与背景**：yk 旨在让现有 C 解释器在不牺牲兼容性的前提下获得 JIT 加速；此前 yklua 已比 PUC Lua 快约 2 倍，作者进一步验证大型解释器 CPython。
- ⚠️ **初步挑战**：CPython 的 quickening/特化会让 opcode 在通用与特化间切换，导致 trace 频繁失效；tier 1 方案性能很差。
- 🔁 **转向 tier 2**：改用 CPython 的 tier 2 解释器后适配更简单，仅约 80 行代码即可接入 YkLocation。
- 🚀 **关键优化：幂等加载**：用 yk_promote 和幂等函数暴露 opcode/code ID 常量，Mandelbrot 从 13.70s 降至 5.00s，约为 CPython 的 0.43 倍耗时。
- 🧭 **扩大 trace 覆盖**：DeltaBlue 因 trace 过长、原子指令未实现、executor 无 _JUMP_TO_TOP 等问题变慢；增加 trace 长度限制、outline 不宜内联函数、在 executor 首指令加 YkLocation 后提升 4.23 倍至 8.64s。
- 🔍 **更多 dispatch 优化**：对指令其他字段也做幂等加载，DeltaBlue 进一步降至 8.09s，接近 CPython 10% 以内。
- 📦 **选择性循环展开**：用 yk_unroll 标记 _PyFrame_Initialize、_PyFrame_ClearLocals 等小循环函数，JSON 从 11.52s 降至 10.85s。
- 🔗 **间接调用内联**：对 len/list_length、range 等间接调用使用 yk_promote 与 yk_indirect_inline，JSON 进一步降至 10.41s。
- 📊 **结果与局限**：ykcpython 在多数基准快于 CPython，8/13 快于实验 JIT，但仅测少量小基准，尚未生产可用。
- 🛠️ **结论**：大型复杂解释器也可较容易 ykify；yk 的通用修复会惠及所有 ykified 解释器，未来仍有大量性能空间。

---

### [funkycache：一个在 SQLite 中缓存函数的 Python 库 – alexwlchan](https://alexwlchan.net/2026/funkycache/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-772-november-19-2026)

**原文标题**: [funkycache: a Python library to cache functions in SQLite – alexwlchan](https://alexwlchan.net/2026/funkycache/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-772-november-19-2026)

funkycache 是一个基于 SQLite 的 Python 函数缓存库，旨在为静态站点生成器等确定性任务加速；作者总结了其设计动机、实现机制与使用方式，并说明缓存键、值序列化、失效依赖和生成器缓存等关键细节。

- 🧩 早期缓存只提供字符串存取，缺少函数级缓存逻辑，代码难测试且容易出错，因此作者开发了 funkycache。
- 🚀 使用方式类似 `functools.cache`：创建 `FunkyCache(storage="sqlite")` 实例后，用装饰器注册需要缓存的函数。
- 🔑 缓存键由函数完整参数生成：用 `inspect.signature` 统一位置参数、关键字参数和默认值，再 JSON 序列化并用 XXH64 哈希缩小键体积。
- 💾 缓存值通过函数返回类型和 Pydantic 进行 JSON 序列化与反序列化，便于调试；作者因已有 JSON 流程而避免使用 pickle。
- 🔄 支持自动失效：源文件变化会使对应函数缓存失效；也可声明依赖的文件、目录或静态值，如模板文件或库版本号。
- 🧠 对惰性生成器采取“物化为列表再缓存”的策略，并设置软内存预算，避免大型或无限生成器导致内存失控。
- 📁 文件变更追踪不内置于 funkycache，作者选择复用已有代码，以保持库小而专注。
- 🌐 项目灵感来自响应式编程和 DAG 式构建依赖：输入变化只触发相关任务，从而提升构建效率。
- ⚡ 使用热缓存构建作者网站约需半秒，其中不少时间花在遍历 Markdown 文件上。
- 📦 funkycache 已发布到 PyPI，源码也在作者网站上，代码量仅几百行且包含测试。

---

### [使用编排式 Pytest Worker 加速 CI | Close 的打造历程](https://making.close.com/posts/faster-ci-with-orchestrated-pytest-workers/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-772-november-19-2026)

**原文标题**: [Faster CI with Orchestrated Pytest Workers | The Making of Close](https://making.close.com/posts/faster-ci-with-orchestrated-pytest-workers/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-772-november-19-2026)

Close 后端约有 58,000 个集成测试，大多真实访问多个数据存储；文章回顾其 CI 从 Jenkins/nose 到 GitHub Actions/pytest 的演进，并说明如何通过集中式编排、动态分片和 Spot 实例把全量测试运行压缩到约 2.5 分钟。

- 🧪 测试规模：Close 主后端近 58,000 个集成测试，多为 API/服务级测试，避免 mock 并实际访问数据存储，CI 全量约 2.5 分钟。
- 🕰️ 演进路径：测试 CI 始于 2012 年的 Jenkins + nose，后迁移到 CircleCI、GitHub Actions，并切换到 pytest。
- 🚦 早期并行：多 CPU 的 pytest-xdist 不适合共享数据库场景；团队采用 pytest-split 做确定性分片，2014 年引入，并按主分支测试耗时做 bin packing。
- 🧱 遇到瓶颈：镜像拉取和数据存储启动约 1 分钟、应用需等待数据存储、全量 test collection 超过 1 分钟；即使 17 倍并行，最佳墙钟时间仍约 12 分钟。
- 💡 新架构：借鉴 currents.dev 的集中队列编排，orchestrator 只收集文件和分发任务、不运行数据存储；worker 只收集自己要跑的测试，并与后端启动并行。
- ☁️ Spot 实例：从 17 台按需 runner 变为 2 台按需 + 54 台 Spot，成本相近；保留 main 按需 runner 以保持可预测性。
- 🔌 通信方式：GitHub Actions runner 无法被外部寻址，团队用 Kubernetes operator 创建临时命名空间/Pod，worker 按运行标识查找并等待连接。
- 🔁 失败重跑：worker 等所有批次结束后由 orchestrator 判断结果；任一失败则全体失败，重跑 failed jobs 会启动正确数量的 worker，避免单 worker 跑全量。
- 🧰 细节优化：pytest 负责收集并输出 JSON 以避免配置漂移；批次按耗时降序分配；扩容自托管 runner 空闲数和节点池；用 OTel、ClickHouse、Grafana 聚合真实 CI 耗时。

---

### [如何在 Django 中查找并修复 N+1 查询 | Code With Stein](https://codewithstein.com/fix-n-plus-one-queries-django/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-772-november-19-2026)

**原文标题**: [How to find and fix N+1 queries in Django | Code With Stein](https://codewithstein.com/fix-n-plus-one-queries-django/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-772-november-19-2026)

本文说明 Django 中 N+1 查询的成因、定位与修复方法：用实际 SQL 找出重复查询，再通过 `select_related()` 和 `prefetch_related()` 减少不必要数据库访问，并用测试防止回归。

- 🔍 N+1 查询指先执行 1 次主查询，再为每条记录分别查询关联对象；示例中 20 篇文章可能产生 61 次查询。
- 🧩 关联访问常隐藏在模板、DRF 序列化器、模型属性或 `__str__()` 中，代码看似正常但会触发额外查询。
- 🛠️ 使用 Django Debug Toolbar 的 SQL 面板定位重复查询，也可在开发时查看 `connection.queries`。
- 🔗 对 `ForeignKey`、`OneToOneField` 等“单对单”关系使用 `select_related()`，通过 JOIN 随主查询一起加载。
- 📦 对多对多和反向外键关系使用 `prefetch_related()`，以额外批量查询加载关联对象并在 Python 中匹配。
- 🎛️ 需要过滤预取数据或控制结果属性时，使用 `Prefetch`，可指定自定义 queryset 和 `to_attr`。
- ⚠️ 不要在所有 queryset 上盲目添加优化方法；应遵循“先分析、修改、再测量”，避免用内存或复杂 SQL 换取表面上的低查询数。
- 🧪 用 `assertNumQueries()` 编写查询数测试，防止模板新增关联字段后 N+1 问题悄悄回归。
- 📈 查询数合理但页面仍慢时，可用 `QuerySet.explain()` 检查执行计划与索引使用情况。
- 🆕 Django 6.1 的 `FETCH_PEERS` 等 fetch modes 可帮助批量加载，但显式使用 `select_related()` 与 `prefetch_related()` 仍更可控。

---

### [zar-rs](https://brmmm3.github.io/posts/2026/11/15/zar-rs/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-772-november-19-2026)

**原文标题**: [zar-rs](https://brmmm3.github.io/posts/2026/11/15/zar-rs/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-772-november-19-2026)

ZAR 是一种由 Rust 实现的新归档格式，并提供原生 Python API。它主打并行 Zstandard 压缩、提交式版本历史、内容去重、随机访问与恢复校验，目标是在保持归档操作快速的同时管理文件随时间发生的变化；同一 Rust 核心还支持 CLI、桌面工具及多语言绑定。

- 🚀 **新格式而非包装器**：ZAR 不是 ZIP/TAR 的 Python 封装，而是面向快速并行压缩与历史管理的独立归档格式。
- ⚡ **性能突出**：在 Linux Core i7-10700、热缓存、未加密基准中，525 MiB 源码树压缩仅 0.86 秒，ZIP 为 11.01 秒，7z 为 24.91 秒。
- 📦 **压缩体积均衡**：同一测试中 ZAR 归档为 115.5 MiB，小于 ZIP 的 151.1 MiB，但大于 7z 的 81.1 MiB；若追求更小体积，7z 可能更合适。
- 🕘 **提交式更新**：每次更新可新增 commit 并保留旧版本，可检查或恢复历史，无需为每个版本保存完整归档。
- 🧬 **内容去重与随机访问**：支持单次创建/添加操作内的内容去重，并可按文件随机访问，不必解压整个归档。
- 🛡️ **校验与恢复**：提供分块校验和，可扫描损坏区域之外的数据；还支持历史恢复和归档检查。
- 🔐 **认证加密**：支持 AES-256-GCM 或 ChaCha20-Poly1305，可加密头部、数据或两者，并支持按提交使用不同密码。
- 🐍 **Python API 完整**：`pyzarlib` 支持创建、追加、列出、检查、提取、读取元数据、预览恢复等操作，接受 `pathlib.Path` 和字符串路径。
- 🧵 **并发友好**：Rust 长操作会释放 GIL，其他 Python 线程可继续工作；支持 Python 3.11+，并测试 CPython 3.11–3.15 及自由线程版本。
- 🗜️ **压缩可控**：Zstandard 压缩级别可选 -7 到 22，块大小 64 KiB 到 32 MiB，默认压缩级别为 3，也可自动选择块大小。
- 📥 **可导入常见归档**：`create_archive` 和 `add_archive` 可从 ZIP、7z、RAR、ISO、TAR、TAR.GZ、TGZ、GZ 导入条目并保留内部路径；加密输入等有限制。
- 🛠️ **多入口与多语言**：提供 `zarc` CLI、`zarg` 桌面应用、`zarmcp` 本地服务、`zcopy` 网络传输工具，以及 Rust、C/C++、Go、Java、C#、WASI 等绑定。
- 📥 **安装方式**：可通过 Maturin 从源码构建 Python 扩展，执行 `maturin develop --release` 后导入 `pyzarlib`；项目采用 MIT 或 Apache-2.0 许可。

---

### [获取失败](https://lemire.me/blog/2026/11/14/reading-json-at-277-gb-s-in-python/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-772-november-19-2026)

**原文标题**: [Failed to retrieve](https://lemire.me/blog/2026/11/14/reading-json-at-277-gb-s-in-python/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-772-november-19-2026)

无法总结：获取内容失败，状态码 520。

---

### [通过可视化学习 Python 数据结构和算法 - YouTube](https://www.youtube.com/watch?v=ybe6EGe_wjo&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-772-november-19-2026)

**原文标题**: [Learn Data Structures and Algorithms in Python with Visualizations - YouTube](https://www.youtube.com/watch?v=ybe6EGe_wjo&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-772-november-19-2026)

这是 YouTube 韩语页面底部的信息与法律声明，主要包含平台导航链接、公司信息、版权声明、联系方式及商品销售免责说明。

- 🔗 页面包含信息、新闻稿、版权、咨询、创作者、广告、开发者等导航链接。
- 📜 还列出服务条款、隐私政策、政策与安全、YouTube 运作原理及新功能测试等入口。
- ©️ 版权信息显示为 © 2026 Google LLC，并提及 Sundar Pichai。
- 🏢 公司地址为美国加州山景城 Amphitheatre Parkway 1600 号，邮编 94043。
- ☎️ 提供免费电话 0807-882-594 及支持邮箱 yt-support-solutions-kr@google.com。
- 🖥️ 说明网站托管方为 Google LLC，并列出事业者信息及非法拍摄物举报入口。
- 🛒 创作者在 YouTube 上发布、标记或推荐的商品按卖家条款销售，YouTube 不销售这些商品且不承担责任。

---

### [GitHub - google-research/paper-orchestra：PaperOrchestra 是一个用于自动化 AI 研究论文写作的多智能体框架。 · GitHub](https://github.com/google-research/paper-orchestra?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-772-november-19-2026)

**原文标题**: [GitHub - google-research/paper-orchestra: PaperOrchestra is a multi-agent framework for automated AI research paper writing. · GitHub](https://github.com/google-research/paper-orchestra?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-772-november-19-2026)

PaperOrchestra 是 Google Cloud AI Research 推出的多智能体框架，用于自动撰写 AI 研究论文。它可将想法、实验日志等未结构化的前置写作材料转化为符合会议模板、可直接投稿的 LaTeX 手稿，并覆盖大纲生成、文献综述、章节写作、内容润色与图表生成等流程。

- 🤖 **多智能体流水线**：协调 Outline、Literature Review、Section Writing、Content Refinement、Plotting 等专用智能体，实现端到端论文生成。
- 📚 **综合文献综述**：自动搜索、筛选并整合相关文献到手稿中。
- 📊 **可视化生成**：支持生成图表，并可加入概念示意图。
- 📝 **LaTeX 自动化**：产出符合目标会议模板、可直接投稿的 LaTeX 手稿。
- ⚙️ **环境安装**：依赖名为 `paper_orchestra` 的 Conda 环境，建议 Python 3.11，并通过 `requirements.txt` 安装依赖。
- 🔑 **API 配置**：需在项目根目录创建 `.env`，配置 Semantic Scholar、OpenAI、Vertex AI/Gemini 等密钥；可选配置 SMTP 用于邮件发送。
- 📂 **数据集说明**：论文生成所用数据集未包含在代码仓库中，后续将单独发布，并需放置于 `datasets/` 目录。
- 🚀 **使用方式**：可通过 `./paper_writing_cli.sh` 或 `python paper_writing_cli.py` 运行；需指定原始材料目录和 LaTeX 模板目录，可选输出目录、绘图开关及模型名称。
- 🖥️ **交互演示**：提供 Streamlit 交互式 Demo，使用说明见 `frontend/README.md`。
- 🗂️ **项目结构**：包含 `autoraters/` 自动评估、`methods/` 智能体与流水线核心逻辑、`templates/` 会议 LaTeX 模板、`utils/` API 与 PDF 等工具函数。
- 📈 **仓库数据**：约 5k stars、633 forks、14 个 issues、34 个 pull requests。
- 📄 **许可与声明**：采用 Apache-2.0 许可证；该项目不是 Google 官方支持的产品。

---

### [GitHub - elementalsouls/Claude-BugHunter: A Claude Code skill bundle for bug hunting and external red-team work - 82 skills, 15 slash commands, 681 disclosed-report patterns curated across 24 core vulnerability classes, plus enterprise identity + infrastructure attack matrices. · GitHub](https://github.com/elementalsouls/Claude-BugHunter?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-772-november-19-2026)

**原文标题**: [GitHub - elementalsouls/Claude-BugHunter: A Claude Code skill bundle for bug hunting and external red-team work - 82 skills, 15 slash commands, 681 disclosed-report patterns curated across 24 core vulnerability classes, plus enterprise identity + infrastructure attack matrices. · GitHub](https://github.com/elementalsouls/Claude-BugHunter?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-772-november-19-2026)

Claude-BugHunter 是面向 Claude Code 的即插即用技能包，专注漏洞赏金与外部红队工作，内置 83 个技能、15 个斜杠命令和来自 681 份公开报告的 24 类漏洞模式，并覆盖企业身份与基础设施攻击矩阵；支持插件或复制安装、按自然语言自动加载技能、多代理框架运行，但明确限定于授权的外部攻击面，不覆盖内部 AD、C2、后渗透、规避等方向。

- 🧰 仓库由 Sachin Sharma / ElementalSoul 维护，定位为 Claude Code 的漏洞赏金与外部红队技能包，已有约 12.5k Star、1.6k Fork。
- 🧠 能力分为四层：方法论与红队思维、58 个 Web/API 漏洞狩猎技能、企业平台攻击链、验证与报告交付。
- 📚 包含 83 个技能、15 个斜杠命令、681 个公开报告模式（其中 433 个可审计引用），覆盖 24 类核心漏洞。
- 🏢 企业攻击面覆盖 M365/Entra、Okta、vCenter、SSL VPN、SharePoint、云 IAM、APK 红队与供应链侦察等。
- ⚙️ 安装方式：推荐作为 Claude Code 插件安装，也可克隆后用脚本复制安装；插件用户可单独用 pipx 安装 cbh CLI。
- 🗣️ 使用方式：用自然语言描述测试目标，相关技能会自动加载；也提供 /hunt 脚手架和 cbh CLI 编排。
- 🧩 技能采用通用 SKILL.md 格式，可运行于 Claude Code、OpenCode、Codex CLI、Hermes Agent、Google AntiGravity 等多个代理框架。
- 🎯 范围限定为外部攻击面：Web/API、SaaS、GraphQL、OAuth、JWT、文件上传、IDOR、SSRF、RCE 链、云配置错误与外部红队初始访问。
- 🚫 明确不覆盖内部 AD 攻击、C2 框架、后渗透/持久化/横向移动、免杀规避、iOS/硬件/RF/ICS、二进制与内核利用。
- ✅ 强调仅用于自有或获书面授权的资产；含 7 问验证门、Bugcrowd 报告卫生与授权信号，并提示 Anthropic 网络防护及 CVP 计划。
- 📄 文档包含安装、使用、架构、CVE 覆盖、贡献与安全政策；许可证为代码 MIT、内容 CC BY 4.0。
- 🗺️ 路线图包括 HackerOne MCP、跨目标记忆层、行业技能、项目规则解析器、企业 VPN CVE 矩阵季度刷新等。

---

### [GitHub - NVIDIA/SkillEvaluator: Multi-tier framework for evaluating AI agent skills and plugins with quality gates, security scanning, harness compatibility checks, semantic overlap detection, synthetic evaluation dataset generation, and live agent evaluation that measures how skills affect agent behavior. Ships reusable CI templates that bring every check to any repository. · GitHub](https://github.com/NVIDIA/SkillEvaluator?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-772-november-19-2026)

**原文标题**: [GitHub - NVIDIA/SkillEvaluator: Multi-tier framework for evaluating AI agent skills and plugins with quality gates, security scanning, harness compatibility checks, semantic overlap detection, synthetic evaluation dataset generation, and live agent evaluation that measures how skills affect agent behavior. Ships reusable CI templates that bring every check to any repository. · GitHub](https://github.com/NVIDIA/SkillEvaluator?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-772-november-19-2026)

NVIDIA SkillEvaluator 是 NVIDIA 推出的开源多层级框架，用于评估和改进 AI agent 技能与插件，覆盖质量、安全、Harness 兼容性、语义重叠、合成评测数据集及真实 agent 行为影响，并提供可复用 CI 模板。

- ⚙️ **三层评估**：Tier 1 验证技能是否安全、格式正确且能被 agent 加载；Tier 2 用嵌入/对话模型检测重复与语义重叠；Tier 3 通过真实 agent 运行衡量技能带来的“skill lift”，三层可独立使用。
- 🛡️ **Tier 1 静态检查**：包含 500+ 静态规则与检测模式，覆盖质量、schema、版本、PII、许可证、Unicode、脚本 lint、Harness Check；安全与代码完整性使用 SkillSpector、Gitleaks、Bandit，Semgrep 可选。
- 🔌 **无需密钥的快速检查**：`skillevaluator quality-check` 可无 API key、扫描器、GPU 或 Docker 运行并输出 100 分制评分；`harness-check` 无需 API key 或 agent 运行即可判断 agent 是否会加载技能。
- 🚀 **安装与全流程**：Python 3.12–3.14 下 `pip install skillevaluator`；全三层 `validate` 需 NVIDIA Build key、扫描器配置和 Docker（Tier 3），可用 `--tiers 1,2` 或 `--tiers 1` 跳过后续层级。
- 🧪 **Tier 3 实时评测**：需要模型提供方、受支持的 agent 和运行中的沙箱（默认 Docker），用于生成/复用评测数据集并比较有技能与无技能的任务结果；`doctor` 可检查环境就绪情况。
- 🏗️ **CI 集成**：运行 `skillevaluator ci init` 可生成 GitHub/GitLab 配置；模板内置 11 项 CI 检查，支持可选 PR 评论与托管报告，无需编写维护评测代码。
- 📚 **生态与依赖**：属于 NVIDIA Verified Skills pipeline，使用 Harbor 驱动沙箱 agent 运行，并集成 pip-audit 等第三方工具；文档、论文、BibTeX 与性能面板齐全。
- 📄 **许可与支持**：Apache-2.0 许可；支持级别为 Experimental，社区支持、无 SLA 或 NVIDIA 企业支持；项目约有 4.1k stars、537 forks。

---

### [GitHub - Sibyl-Labs/Sibyl-Memory: Durable, file-based long-term memory for AI agents. Five-package plugin family: SDK, CLI, MCP server, Hermes adapter, and a LangGraph BaseStore. No vector database, no embeddings. · GitHub](https://github.com/Sibyl-Labs/Sibyl-Memory?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-772-november-19-2026)

**原文标题**: [GitHub - Sibyl-Labs/Sibyl-Memory: Durable, file-based long-term memory for AI agents. Five-package plugin family: SDK, CLI, MCP server, Hermes adapter, and a LangGraph BaseStore. No vector database, no embeddings. · GitHub](https://github.com/Sibyl-Labs/Sibyl-Memory?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-772-november-19-2026)

Sibyl-Memory 是面向 AI Agent 的持久化、基于文件的长期记忆基础设施，采用 SQLite + FTS5 与五层分层模式，无需向量数据库和嵌入模型；它以五个 PyPI 包组成插件家族，覆盖 SDK、CLI、MCP、Hermes 与 LangGraph，并强调本地优先、隐私保护与可基准复现。

- 🧠 **核心定位**：为 AI Agent 提供持久、文件化的长期记忆，数据保存在本机单个文件中，不依赖外部检索服务。
- 📦 **五包体系**：包括 `sibyl-memory-client`（SDK）、`sibyl-memory-cli`、`sibyl-memory-mcp`、`sibyl-memory-hermes` 和 `sibyl-memory-langgraph`。
- 🗂️ **五层架构**：HOT、WARM、COLD、REFERENCE、ARCHIVE 分别管理活跃状态、实体、事件日志、静态知识与归档，并通过唯一约束保证实体单一事实源。
- 🔒 **隐私设计**：记忆内容不离开本机；仅激活、账户心跳、容量检查和聚合操作计数等少量元数据会与服务器交互。
- 🔑 **账户要求**：使用记忆工具需激活账户并持有有效 entitlement；本地记忆始终可用 `sibyl memory` 读取，离线授权最长可用 14 天。
- 📈 **基准表现**：在 LongMemEval Oracle 上，Claude Opus 4.6 得分 95.6%，2026 年 4 月排名第 2；Claude Sonnet 4.5 得分 95.1%，并有外部复现约 95.2%。
- ⚙️ **安装与集成**：可通过 `pip install sibyl-memory-cli` 后运行 `sibyl init`；支持 Claude Code、Codex、Cursor、Continue 等 MCP 客户端及 Hermes、LangGraph。
- 💾 **保存与瘦身**：Save 机制记录决策、实体、会话状态、优先级与归档；Debloat 测量并裁剪 `CLAUDE.md`、`AGENTS.md`、`.cursorrules` 等指令文件，历史可移至旁边文件或 Sibyl Memory。
- 🆓 **免费与 Pro 差异**：免费版提供基础保存/瘦身流程与提醒；Pro 解锁自动保存、自动瘦身、技能提案、记忆 linter 及更高本地容量。
- 🖥️ **平台支持**：支持 Linux、macOS（Apple Silicon 与 Intel）及 Windows WSL2，不支持原生 Windows。
- ⚖️ **开源与托管**：代码为 MIT 许可，本地引擎可 fork；但账户、设备管理、计费、更新与托管功能依赖服务器端 entitlement。
- 🧹 **卸载注意**：应先运行 `sibyl skills uninstall` 移除 Claude Code hooks、技能 shim 与 Codex 配置，再卸载 PyPI 包。

---

### [GitHub - codepawl/creator-generalist: AI agent skills to be professional at 2D and 3D · GitHub](https://github.com/codepawl/creator-generalist?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-772-november-19-2026)

**原文标题**: [GitHub - codepawl/creator-generalist: AI agent skills to be professional at 2D and 3D · GitHub](https://github.com/codepawl/creator-generalist?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-772-november-19-2026)

这个仓库是 CodePawl 维护的开源项目 `creator-generalist`，提供面向 2D、3D 和游戏内容生产的 AI 代理技能包，目标是把代理变成 2D/3D 通才和一个小型游戏工作室。项目采用 MIT 许可，当前约 331 stars、30 forks，安装一次后可按需求自动加载相应技能。

- 🧩 **核心定位**：让 AI 代理具备 2D 动画、3D 建模、视觉开发、视频编辑、声音设计和游戏原型制作能力。
- 🚀 **使用方式**：无需手动点名技能，直接描述任务即可匹配技能；也可用 `/3dg`、`/2dg`、`/gameg` 启动对应工作流。
- 🎬 **3D 主技能**：支持切面短片、故事短片、世界/场景、角色、资产等模式，使用 Blender、Three.js 或 Crucible 构建。
- 🖋️ **2D 主技能**：面向 Vox 风格解说图，支持脚本、照片、地图、图表时间线、档案拼贴、设计风格帧和工具审计。
- 🎮 **游戏主技能**：支持可玩灰盒原型、完整小型原创游戏和现有游戏打磨，覆盖 Web、Godot、Unity、Unreal。
- 🧰 **配套技能**：包含角色建模、雕塑、绑定、动画、绘画、背景绘制、代码绘画、3D 软件操作、视频编辑、视频学习、声音设计等。
- 🧭 **生产流程**：两个通才技能遵循八步流程：简报、参考、脚本/节拍、准备与风格门禁、资产、构建与动画、声音、QA 与预览。
- ✅ **质量控制**：构建前会检查工具与资源，提供 WIP 演示、540p 预览和 A/B/C 风格帧；最终渲染前需用户确认。
- 🖼️ **真实感策略**：优先使用 CC0/CC BY 模型与纹理，强调真实资产、角色表演、灯光镜头、接触与滑步检查、渲染对比。
- 📦 **安装方式**：支持 Claude Code 插件市场、`npx skills add codepawl/creator-generalist`、或手动复制技能文件夹；全部功能需安装五个插件。
- ⚖️ **开源信息**：MIT 许可证，由越南独立 3D 工作室 CodePawl 制作，README 中的横幅和示例片段也由这些技能生成。

---

### [GitHub - seifheakal/blue-harness: Make your own app expensive to reverse. A build-time audit, harden and verify harness for native binaries and mobile apps, built to counter AI-assisted reverse engineering. · GitHub](https://github.com/seifheakal/blue-harness?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-772-november-19-2026)

**原文标题**: [GitHub - seifheakal/blue-harness: Make your own app expensive to reverse. A build-time audit, harden and verify harness for native binaries and mobile apps, built to counter AI-assisted reverse engineering. · GitHub](https://github.com/seifheakal/blue-harness?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-772-november-19-2026)

overview summary
blue-harness 是一个面向自有原生二进制与移动应用的构建时反逆向审计、加固与验证框架，旨在提高 AI 辅助逆向工程的成本，并证明每项防御确实生效。

- 🛡️ 核心流程是“审计→加固→证明”：扫描暴露面、施加对策、验证防御真实触发而非摆设。
- 📊 单次实测中，未保护构建不到 2 秒被破解；加固后同一小模型失败，消耗约 13 倍 token 和 120 倍耗时。
- 🧩 提供九类对策，包括反调试、字符串加密、反 Frida、代码完整性/服务端证明、核心转储抑制、分析面耗尽、蜜标等，每项均标注强度层级与已知绕过。
- 🖥️ 支持 Linux ELF、Windows PE、macOS/iOS Mach-O 的只读暴露审计，三种格式均有构建后加固路径。
- ⚙️ 提供 `make demo`、`make verify`、`make report`、`make harden` 等命令；CI 在每次推送重新验证防御，当前 362 项检查通过。
- 🧪 测量基于小型 4-bit 量化 7B 模型的 N=1 运行，属于下限；项目公开征集更大/前沿模型复测，可一键 `make slice-k-run`。
- 📱 尚未覆盖 Android JNI、iOS 应用内部等移动端深入场景；PE/Mach-O 构建时加固和 Windows/Mac 运行时验证仍在路线图中。
- 🚫 明确不是“不可破解”包装、不是秘密保险库、也不是攻击工具；仅限蓝队审计和加固自有或授权软件。
- 📜 采用 AGPL-3.0 开源，闭源产品/专有服务需商业许可；评估与测试免费。

---

### [GitHub - sigilco/pyscriptc：将带注解的 Python 编译为原生二进制文件。类型化子集，可选启用 CPython 回退。· GitHub](https://github.com/sigilco/pyscriptc?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-772-november-19-2026)

**原文标题**: [GitHub - sigilco/pyscriptc: Compile annotated Python to native binaries. Typed subset, opt-in CPython fallback. · GitHub](https://github.com/sigilco/pyscriptc?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-772-november-19-2026)

pyscriptc 是 sigilco 开发的一个实验性 Python 编译器，可将带类型注解的 Python 子集编译为原生二进制；遇到不支持代码时，它通过稳定的 PSxxxx 诊断指出具体行号，也支持按需回退到嵌入式 CPython。

- 🚀 **核心定位**：把带类型注解的 Python 编译为原生可执行文件，目标是兼容 CPython，但当前只支持 Python 子集、内置函数、标准库和部分 PyPI 包。
- 🧩 **编译机制**：先根据类型注解和类型提示进行类型检查，再把受支持代码降为机器码；超出子集时构建停止并给出 PSxxxx 诊断。
- 🔁 **CPython 回退**：使用 `--island` 或 `--fallback=cpython` 可让不支持代码运行在嵌入的 CPython 上，但需宿主机已安装 Python，且跨边界调用有编组开销。
- 🛠️ **快速上手**：`pyscriptc run hello.py` 可直接运行；`pyscriptc compile hello.py --emit bin -o hello` 可生成二进制。
- 📦 **安装方式**：支持 macOS/Linux 安装脚本、Windows PowerShell 脚本及 `uv tool install pyscriptc`；构建二进制需 PATH 中有 clang 或 zig。
- 💻 **平台支持**：Windows 上 pyscriptc 可运行但属实验性；暂不支持原生 Windows 编译，交叉编译到 Windows 也未经验证。
- ⚡ **性能表现**：基准测试中，相比 CPython 3.14.9，Kernels 快 23.9 倍、脚本快 22.2 倍、标准库调用快 14.4 倍，内存占用也显著更低。
- 📊 **兼容性跟踪**：逐模块、逐库支持状态由 nightly CI 更新到 compat site；PyPI 库状态分为“可编译为原生代码”和“在 CPython 岛上运行”两类。
- 🔒 **遥测与许可**：发布版默认发送匿名使用事件，可用 `PYSC_NO_TELEMETRY=1`、`DO_NOT_TRACK=1` 或命令关闭；项目采用 Apache-2.0 许可。
- ⭐ **项目状态**：仓库约 1,083 次提交、14 个 Star、0 个 Fork，仍处于实验阶段。

---

### [GitHub - solarian-dev/solarian：面向现代AI时代的机器人开发框架。 · GitHub](https://github.com/solarian-dev/solarian?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-772-november-19-2026)

**原文标题**: [GitHub - solarian-dev/solarian: Robot development framework for the modern era of AI. · GitHub](https://github.com/solarian-dev/solarian?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-772-november-19-2026)

Solarian 是面向 AI 机器人时代的开源 Python 框架，覆盖机器人构建、仿真、遥操作、训练与部署，强调模块化、UMI 技能复用，以及从硬件到 AI 控制的一体化开发体验。

- 🤖 统一 Python 技术栈：在同一框架内完成机器人构建、仿真、遥操作、训练和策略部署。
- 🧩 模块化机器人：机器人是 Python 类，由机械臂、夹爪、相机等可复用模块组成，每个模块包含传感器和执行器。
- 🎯 内置运动学：支持末端执行器控制与逆运动学求解，也支持关节控制与正运动学求解。
- 🧠 AI Agentic Controller：围绕视觉语言模型构建代理控制层，可接收聊天任务、规划并调用物理技能，同时用快速监控模型通过相机监督执行。
- 🖥️ 内置 MuJoCo 仿真：使用 `solarian run-robot --sim` 可在仿真中运行与真实硬件相同的机器人类和 YAML 配置。
- 🔌 插件化扩展：执行器、传感器、模块、技能等可作为插件安装，`solarian create-plugin` 可创建新插件。
- 📹 数据与训练闭环：按原生频率录制相机和信号、整理 episodes，并训练 diffusion、ACT 或 UMI 策略后回传机器人使用。
- ⚙️ 类型与配置：使用 Pydantic 模式绑定模块，使用 Hydra 组合式 YAML 并支持命令行覆盖。
- 📦 快速开始：`pip install solarian`，可选安装 `solarian[all]` 获取 AI、代理控制器和仿真扩展。
- 🛠️ 面向编码代理：提供 `create-project`、`create-plugin`、`docs list`、`agent install` 等 CLI，并生成 `AGENTS.md` 与代理技能。
- 🚀 示例 Arm1：展示 UMI 风格夹爪、腕部相机、技能工具绑定、键盘遥操作和代理可调用技能。
- 🌐 社区与许可：提供 Discord、文档、教程和插件目录；项目采用 Apache-2.0 许可，欢迎早期贡献。

---

### [GitHub - NodeX-AR/Pytml：Pytml 是一个 15KB 的轻量级 PyScript 替代方案——只需一个 script 标签即可在 HTML 中运行 Python。· GitHub](https://github.com/NodeX-AR/Pytml?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-772-november-19-2026)

**原文标题**: [GitHub - NodeX-AR/Pytml: Pytml is a 15KB lightweight PyScript alternative — run Python in HTML with one script tag. · GitHub](https://github.com/NodeX-AR/Pytml?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-772-november-19-2026)

Pytml 是一个约 15KB 的轻量级 PyScript 替代方案，基于 Pyodide，可通过单个 script 标签在浏览器中零配置运行 Python，并支持 DOM 交互、编号 UI 控件、包安装、本地文件运行和客户端隐私安全。

- 🪶 轻量零配置：仅约 15KB，只需引入一个 script 标签即可在 HTML 中运行 Python，无需服务器。
- 🐍 基于 Pyodide：Pytml 2.5 构建于 Pyodide 314.0.7，是官方 Pyodide 相关项目。
- 🧩 HTML 内嵌 Python：使用 `<py>` 或 `<pyN>` 块编写 Python，可与普通 HTML ID 和 DOM 元素交互。
- 🎛️ 编号 UI 语法：`<btnN>`、`<inputN>`、`<txtN>` 会转换为真实按钮或输入框，并保留 Python 缩进。
- 📦 包管理支持：通过 `micropip` 安装包，可使用 NumPy、pandas、Matplotlib 等科学计算库。
- 🧠 多程序与事件：`<py1>`、`<py2>` 等标识符用于区分程序；支持鼠标、触摸、键盘、滚动、手柄等事件。
- 💻 本地文件支持：内联 Python 可直接通过 `file://` 打开，无需 Python Web 服务器；外部 `.py` 文件受浏览器安全限制。
- 🔒 隐私与安全：客户端执行，默认使用 `textContent`，可防 XSS；渲染原始 HTML 时需用 `pytml.escape()` 清理不可信输入。
- 🛠️ 丰富辅助功能：提供 Canvas、音频、视频、剪贴板、存储、下载、全屏等能力。
- 📜 开源与资源：采用 Apache 2.0 许可，官网为 pytml.js.org，GitHub 仓库为 NodeX-AR/Pytml，欢迎 Star。

---

### [GitHub - Balanov/mcp-attest: Authorization conformance harness for MCP servers: test a live server against your own policy, as every identity, and produce evidence an auditor can verify. · GitHub](https://github.com/Balanov/mcp-attest?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-772-november-19-2026)

**原文标题**: [GitHub - Balanov/mcp-attest: Authorization conformance harness for MCP servers: test a live server against your own policy, as every identity, and produce evidence an auditor can verify. · GitHub](https://github.com/Balanov/mcp-attest?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-772-november-19-2026)

mcp-attest 是一个面向 MCP 服务器的授权一致性测试工具：它按策略以不同身份连接真实服务器、发送真实调用，并对比“策略期望的决策”与“服务器实际执行的决策”，生成可供审计验证的证据。

- 🔎 **核心定位**：测试“实际决策”而非工具描述；它不挡请求，只证明服务器是否按策略允许或拒绝。
- 🧪 **测试方式**：连接策略中的每个身份，自动生成“身份 × 工具”矩阵，从 schema 派生参数并发送真实调用。
- 🛡️ **规则覆盖**：包含 24 条实时规则，映射 OWASP MCP Security Testing Guide，涵盖授权、令牌、工具投毒、清单漂移、密钥泄露、失败关闭、注入、执行汇、schema、审批、错误信息等。
- 🔐 **OAuth 检查**：提供 12 项 OAuth 检查，覆盖必需令牌、签名、`alg:none`、过期、受众、签发者、scope、PKCE、redirect_uri、state、令牌透传等。
- 🧾 **证据输出**：记录请求、响应、身份、时间戳、期望/观察决策并脱敏，支持哈希链和 HMAC-SHA256 签名，可离线 `attest verify`。
- ⚙️ **CI 门禁**：退出码 0 表示干净、1 表示阻断性发现、2 表示输入错误；支持 `--json`、`--sarif`、`--strict` 和 GitHub Action。
- 📦 **零依赖**：基于 Python 3.10+ 标准库，自行实现 JSON-RPC，不引入 SDK；可用 `pipx`、`uvx` 或 `pip` 安装。
- 🧰 **主要命令**：`attest init/test/suite/verify/check/receipts/shadow/posture/rules`，覆盖策略生成、测试、套件导出验证、证据校验、OTLP trace 审计、收据链和公开服务器姿态测量。
- 📜 **策略文件**：定义 `clients`、工具 allow/deny、身份 headers/env、显式 `cases`、调用参数 `probes`，以及可选 `oauth` 配置；凭据用 `${VAR}` 引用。
- 🔄 **套件可移植**：`attest suite export/validate/run` 可导出跨工具执行的授权一致性套件，schema 已公开。
- 🚫 **明确边界**：不是网关/代理/执行点，不能阻断调用；不是扫描器、不是模型红队、不是 PKI、不是托管服务。
- ✅ **适用场景**：把“我们的 agent 策略已执行”从问卷表述变成第三方可验证的 CI 工件，适合 MCP 服务器授权合规与回归测试。

---

### [IndyPy - Django 与 FastAPI：下一步是什么？，2026 年 11](https://www.meetup.com/indypy/events/311855037/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-772-november-19-2026)

**原文标题**: [IndyPy - Django & FastAPI: What's Next?, Tue, Nov 24, 2026, 7:00 PM   | Meetup](https://www.meetup.com/indypy/events/311855037/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-772-november-19-2026)

IndyPy 将于 11 月 24 日举办“Django & FastAPI: What's Next?”混合活动，围绕 Django 社区发展与 Django/FastAPI 的实际选型展开两场分享，适合关注 Python Web 开发的人士线下或线上参加。

- 📅 活动时间：11 月 24 日（周二）晚 7:00–9:00 EST。
- 📍 活动形式：混合活动，线下地点为印第安纳波利斯 E-gineering Inc.，线上需注册获取 Zoom 链接。
- 🎤 核心主题：Django 开源社区的新变化，以及 Django 与 FastAPI 在真实项目中的取舍。
- 🧑‍💻 第一场分享：Tim Schilling 讲解“What's New in Contributing to Django?”，聚焦导师计划、冲刺活动、新功能流程与社区可持续性。
- ⚖️ 第二场分享：Calvin Hendryx-Parker 讲解“Batteries-Included vs. Speed: The Django/FastAPI Debate”，比较 Django 的“开箱即用”与 FastAPI 的轻量 API 优先设计。
- 🗓️ 议程安排：包含破冰交流、公告、两场演讲、抽奖及 Networking/自由讨论。
- 🎟️ 参与要求：欢迎嘉宾参加，但每位参与者需使用自己的 Meetup 账号分别 RSVP。
- 🤝 组织与赞助：由 IndyPy 主办，Six Feet Up、JetBrains、E-gineering 等提供赞助支持。

---

### [与 King 一起进行数据分析与可视化，2026 年 11 月 25 日星期三下午 5:30 | Meetup](https://www.meetup.com/pyladiesstockholm/events/317379149/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-772-november-19-2026)

**原文标题**: [Data analysis and visualisation with King, Wed, Nov 25, 2026, 5:30 PM   | Meetup](https://www.meetup.com/pyladiesstockholm/events/317379149/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-772-november-19-2026)

本次活动由 PyLadies Stockholm 与 King、Women@King 合办，围绕数据分析与可视化展开，邀请 King 的两位讲者分享真实工作中的实践经验；活动适合 Python 初学者和数据从业者参加，需通过 LUMA 页面申请且名额有限。

- 📊 主题：数据分析与可视化，重点介绍如何把原始数据转化为洞察和清晰、有意义的可视化。
- 🏢 主办与合作方：PyLadies Stockholm、King、Women@King。
- 🗓️ 时间：2026 年 11 月 25 日（周三），17:30 开门，18:00 开始，至 19:30 结束（CET）。
- 📍 地点：瑞典斯德哥尔摩 Malmskillnadsgatan 19。
- 🎤 内容：两位 King 讲者分享实战案例；具体讲者与演讲主题待公布。
- 🗒️ 议程：欢迎与 PyLadies 传统入门问答、第一场演讲、Fika 茶歇、第二场演讲、提问与交流。
- 👥 名额：最多 50 人；请通过 LUMA 页面申请，若计划有变请更新 RSVP。
- ☕ 其他：King 与 Women@King 提供场地和 Fika；无需先备知识，欢迎初学者和日常使用数据的从业者。
- 🤝 社区：PyLadies Stockholm 欢迎热爱或想学习 Python 的女性与非二元人群，以及所有支持其使命的人；请遵守行为准则。

---

### [VilniusPY #32, Wed, Nov 25, 2026, 6:00 PM   | Meetup](https://www.meetup.com/vilniuspy/events/317451556/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-772-november-19-2026)

**原文标题**: [VilniusPY #32, Wed, Nov 25, 2026, 6:00 PM   | Meetup](https://www.meetup.com/vilniuspy/events/317451556/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-772-november-19-2026)

VilniusPY #32 是由 Justinas K. 和 EPAM L. 主办的 Python 社区聚会，将于 11 月 25 日（周三）18:00–21:00 EET 在维尔纽斯 EPAM 举行，重点探讨 AI 驱动的软件开发、自主智能体工作流以及 AI 工具链的安全风险。

- 📅 时间安排：18:00 开门，18:30 正式开始演讲，活动持续至 21:00。
- 📍 活动地点：EPAM，Šeimyniškių g. 19B，维尔纽斯。
- 🎤 主演讲一：Markuss Davis Skrastins 分享“It's Not the Model, It's the User – From an AI Chat to Dark Factory”，探讨从 AI 聊天界面向自主智能体工作流的转变。
- 🔐 主演讲二：Alexandr Marmuzevich 分享“Nobody Clicked Anything”，讲解被劫持的 LiteLLM 如何通过 AI 智能体工具链引入安全漏洞。
- ⚡ 闪电演讲：Denis Filiakin 和 Adnan Rafiq 各进行 5 分钟分享。
- 🍕 现场提供小吃和饮品，建议提前 RSVP 以便主办方统计人数。
- 🪪 入场要求：需携带个人身份证件（身份证、护照或驾照）。
- 📸 活动期间可能拍照和录像，用于社区活动宣传与沟通。

---

### [PyData Helsinki at Sievo, Tue, Nov 24, 2026, 5:30 PM   | Meetup](https://www.meetup.com/pydatahelsinki/events/317117204/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-772-november-19-2026)

**原文标题**: [PyData Helsinki at Sievo, Tue, Nov 24, 2026, 5:30 PM   | Meetup](https://www.meetup.com/pydatahelsinki/events/317117204/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-772-november-19-2026)

PyData Helsinki 将在赫尔辛基 Sievo 举办线下聚会，由 Jouni S. 等 4 人主办，NumFOCUS 赞助。活动于 11 月 24 日星期二 17:30–20:30 EET 举行，包含多场数据科学演讲、问答竞赛、茶歇交流及会后 pub 讨论；需注意准时入场和无鞋政策。

- 📅 活动时间：11 月 24 日星期二 17:30–20:30 EET；报名截止同日 9:00。
- 📍 活动地点：Sievo，Elielinaukio 5 B, 00100 Helsinki, Finland。
- 👥 主办与赞助：Jouni S. 和另外 3 人主办，PyData Helsinki 组织，NumFOCUS 赞助。
- 🚪 入场提醒：17:30 开门，18:00 关门；之后有 30 分钟宽限期，再晚无法入场，只能去 pub 会合。
- 🗣️ 演讲安排：Chandreyee Roy（主题待定）、Quentin Salomé 讲疏散期间人口大规模移动建模、Seija Sirkiä 闪电演讲“平均值到底是什么？”、Kasper Paavolainen 讲算法优化。
- 🧠 互动环节：19:45 举行著名的 PyData Helsinki  quiz。
- 🍪 交流安排：19:20 茶歇、饮料和社交；20:45  networking；21:00 结束后转往附近 pub 继续讨论。
- 👟 场地规则：场地内有无鞋政策，可自带室内鞋或拖鞋。
- 🧭 到场指引：跟随 ELIELINAUKIO 5 标识，靠近 19 号轨道和 Arnold’s。
- 🏷️ 相关主题：人工智能、机器学习、数据科学、Python、赫尔辛基活动。

---

### [如何评估你的第一个 AI 智能体？PyData 索菲亚聚会 2026 年 11 月 24 日，星期二，2026 年 11 月 24 日，晚上](https://www.meetup.com/pydata-sofia/events/317338237/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-772-november-19-2026)

**原文标题**: [How to evaluate your first AI agent ? PyData Sofia Meetup 24 Nov 2026, Tue, Nov 24, 2026, 7:00 PM   | Meetup](https://www.meetup.com/pydata-sofia/events/317338237/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-772-november-19-2026)

本次活动是 PyData Sofia 于 2026 年 11 月 24 日举办的线下 Meetup，主题为“如何评估你的第一个 AI agent”。内容围绕使用 LangFuse 建立评估体系，量化 AI agent 的工具调用、性能与成本，帮助判断更换模型后的效果以及成本优化方向。活动要求强制报名，地点在索菲亚 SiteGround HQ，包含主题演讲、抽奖以及餐饮社交环节。

- 📅 时间：2026 年 11 月 24 日（周二）19:00–21:00 EET。
- 📍 地点：保加利亚索菲亚 SiteGround HQ，Olimpiyska 街 6 号；提供停车位和地图导航。
- 🎯 主题：如何评估第一个 AI agent，并把 LLM/agent 表现转化为可理解的量化指标。
- 🧰 方法：使用 LangFuse 创建评估集，观察工具调用是否正确，并衡量性能与成本。
- 🤖 关键问题：agent 是否调用正确工具；更换模型后性能是否保持或提升；是否需要更大模型或降低成本。
- 🎤 讲者：Zdravko，SiteGround AI Evaluation Engineer，负责 AI 系统性能评估框架与测试。
- 🗓️ 议程：19:00 开场；19:10 主题演讲；20:10 闭幕与 SiteGround 抽奖；20:15 餐饮社交。
- ⚠️ 报名：活动要求强制注册，感兴趣需提前报名。
- 🍽️ 其他：SiteGround 提供饮品和食物，并有抽奖礼品。

---

### [PyData 三联市 #47，2026 年 11](https://www.meetup.com/pydata-trojmiasto/events/317368740/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-772-november-19-2026)

**原文标题**: [PyData Trójmiasto #47, Tue, Nov 24, 2026, 6:00 PM   | Meetup](https://www.meetup.com/pydata-trojmiasto/events/317368740/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-772-november-19-2026)

PyData Trójmiasto 第 47 期活动将于 11 月 24 日 18:00–20:00 CET 在格丁尼亚的 Nordea Tensor Z 举办，由Łukasz G.和 Adrian B.主持，包含两场关于 AI 产品实践与 LLM 安全风险的演讲，并提供交流 networking 环节。

- 📅 **时间地点**：11 月 24 日 18:00–20:00 CET，Łużycka 8b, Gdynia，Tensor Z 大楼。
- 📝 **报名要求**：需用完整姓名注册，入场时携带身份证件；RSVP 截止活动前一天 18:00。
- 📧 **联系与停车**：紧急联系邮箱为 kontakt@pydata-trojmiasto.pl；大楼旁街道有免费停车位。
- 🗓️ **议程安排**：18:00 签到；18:05 PyData 简介；18:10–18:55 Patrycja Mielewczyk 演讲；19:00–19:45 Andrzej Gębski 演讲；19:45 TBA 与交流。
- 🚀 **演讲一**：Patrycja Mielewczyk 分享“先做原型，自信交付”，讲述 PM 如何结合设计能力，将 AI 目录功能从商户沟通推进到正式发布。
- 🧭 **演讲一要点**：从倾听客户与“North Star”原型出发，在不丢失愿景的前提下缩减范围，并将 AI 用于工单、文档、测试和发布，但关键决策仍由人负责。
- 🔐 **演讲二**：Andrzej Gębski 探讨“LLM 的暗面：为何我们假装 Shadow AI 不存在”，聚焦组织内未经 IT 批准的 AI 工具使用问题。
- ⚠️ **风险分析**：AI 采用绕过架构可能带来静默业务逻辑错误、数据外泄以及“slop”污染生产仓库等问题；传统防火墙阻断只是治标。
- 🛡️ **现场演示**：展示 Zero Trust Secure Access 架构，如何在飞行中拦截流量与 PII、阻止不合规提示，同时不破坏开发者生产力。
- 🎤 **讲者背景**：Patrycja 为 Commerce 产品经理，兼具产品设计背景；Andrzej 为 TrendAI 技术客户成功经理，专注企业 AI 工作负载网络安全。
- 🤝 **主办与赞助**：活动由 PyData Trojmiasto 主办，NumFOCUS 赞助，主题涵盖 AI、深度学习、机器学习、大数据与 Python。

---

### [PyData Warsaw #36 - Jawad Ali & Piotr Szwed, Tue, Nov 24, 2026, 6:00 PM   | Meetup](https://www.meetup.com/pydata-warsaw/events/317345820/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-772-november-19-2026)

**原文标题**: [PyData Warsaw #36 - Jawad Ali & Piotr Szwed, Tue, Nov 24, 2026, 6:00 PM   | Meetup](https://www.meetup.com/pydata-warsaw/events/317345820/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-772-november-19-2026)

PyData Warsaw #36 将于 11 月 24 日（周二）18:00–20:00 CET 在 ING Hubs Poland（华沙 Pańska 97）举行，由 Mikołaj R. 与 Rafał M. 主持；活动聚焦生产级 AI 智能体与多智能体企业平台参考架构，分享工程实践、架构模式与落地策略。

- 📅 **时间提醒**：11 月 24 日周二 18:00–20:00 CET，活动在周二而非周三。
- 📍 **地点与承办**：ING Hubs Poland，ul. Pańska 97, Warszawa；ING Hubs Poland 承办并赞助。
- 🎙️ **主持与主办**：由 Mikołaj R. 和 Rafał M. 主持，PyData Warsaw 主办。
- 🤖 **18:00 Jawad Ali**：主题为“Engineering Production-Ready AI Agents with LangGraph”，涵盖有状态工作流、工具调用、记忆管理、子智能体编排、可观测性与可维护性，以及从单智能体到多智能体系统的设计取舍。
- 👨‍💻 **讲者背景**：Jawad Ali 是 Bayer 华沙数字中心高级 AI/ML 工程师、牛津大学校友，拥有 6 年以上企业 AI 系统经验，专注 Agentic AI、RAG、MCP、LangGraph 等。
- 🏢 **18:45 Piotr Szwed**：主题为“Autonomous Enterprise: Reference Architecture for Multi-Agent AI Platforms”，介绍开放模块化企业多智能体平台参考架构、生产级蓝图、成本透明、可审计与 ROI。
- 🧭 **讲者背景**：Piotr Szwed 拥有 20 多年云原生、SRE、DevOps、平台工程经验，是 CNCF 成员与社区组织者，关注可扩展 AI 平台与 Agentic 生态。
- 🤝 **社区与赞助**：列出 Continuum Analytics（Founding）、Centrum Innowacji PW 等赞助/支持方；活动提供会前交流聊天。

---

### [Beyond the Prompt: Building Intelligent AI Agents for Real-World Applications, Tue, Nov 24, 2026, 5:00 PM   | Meetup](https://www.meetup.com/pydata-wolverhampton/events/317450049/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-772-november-19-2026)

**原文标题**: [Beyond the Prompt: Building Intelligent AI Agents for Real-World Applications, Tue, Nov 24, 2026, 5:00 PM   | Meetup](https://www.meetup.com/pydata-wolverhampton/events/317450049/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-772-november-19-2026)

本次活动是 PyData Wolverhampton 举办的免费线下聚会，主题聚焦如何从基础提示词应用迈向能推理、调用工具并解决真实问题的智能 AI Agent，包含专家演讲、问答和社交环节。

- 📅 活动时间：11 月 24 日（星期二）17:00–18:30 GMT；页面另标注为 17:00–19:00 及 2026 年，建议以报名页面最新信息为准。
- 📍 活动地点：英国伍尔弗汉普顿大学 City Campus 的 Alan Turing（MI）Building，房间 MI035。
- 🎤 主讲嘉宾：Dr. Praveen Chandramenon；主持人：Julius Odede 和 Anthonette Adanyin。
- 🤖 核心主题：超越简单提示词，理解智能 AI Agent 与传统 LLM 应用的区别。
- 🧠 技术内容：介绍智能 Agent 的关键组件、架构，以及工具、API 和数据源集成方式。
- 🌍 实践应用：探讨智能 Agent 在真实场景中的用途，以及从原型走向可靠产品需考虑的要点。
- 🗓️ 活动议程：欢迎介绍、主题演讲、问答讨论和自由交流。
- 👥 适合人群：数据分析师、数据科学家、AI/ML 工程师、软件开发者、学生、研究人员及 AI 爱好者。
- 🆓 参与方式：免费入场，但名额有限，需 RSVP 报名；活动遵循 PyData/NumFOCUS 行为准则，欢迎不同经验水平者参加。

---

### [Py](https://www.meetup.com/pydata-cornwall/events/317063147/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-772-november-19-2026)

**原文标题**: [PyData Cornwall - Meetup #5, Tue, Nov 24, 2026, 6:30 PM   | Meetup](https://www.meetup.com/pydata-cornwall/events/317063147/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-772-november-19-2026)

PyData Cornwall 第五次聚会将于 11 月 24 日（周二）在纽基 Flowmoco 举行，活动包括两场主题演讲、闪电演讲、披萨和社交交流，适合数据科学与 Python 社区成员参加。

- 📅 活动时间：11 月 24 日（周二）18:30–21:30 GMT；报名截止时间为当天 17:30。
- 📍 地点：英国纽基 Flowmoco，11 Trevena Terrace, Newquay TR7 1LJ；主办方为 Tun 等 3 人及 PyData Cornwall。
- 🍕 活动流程：18:30 开门并提供饮品，19:00 开始演讲，期间提供披萨，结束后可前往附近酒吧继续交流。
- 🎙️ 主题演讲 1：Savio Rozario 分享本地 LLM 推理的全栈优化，包括硬件、推理引擎、模型、网关、harness 与可观测性，并讨论本地运行与 API 的成本对比。
- 📊 主题演讲 2：Tariq Rashid 介绍图形语法（Grammar of Graphics），说明如何用概念框架让 Python 数据可视化代码更可预测、易写易读。
- ⚡ 闪电演讲：Ben Whorwood 与 Kevin Bath 分享会议见闻（上）；Fei Phoon 与 Tun Shwe 分享会议见闻（下）。
- 🙋 演讲征集：欢迎提交 30 分钟演讲或 5 分钟闪电演讲，首次演讲者也可参加；有问题可在 Discord 咨询。
- ✅ 报名提醒：如无法参加请更新 RSVP，以便估算餐饮；名额有限，有过敏或饮食要求请提前告知。
- 🧭 行为准则：活动遵循 PyData Code of Conduct；相关问题可联系组织者或 NumFOCUS 的 Leah Silen（+1 512-222-5449；leah@numfocus.org）。
- 🤝 社区与赞助：欢迎赞助披萨、饮品或承办未来活动；可加入 Discord、关注 LinkedIn 获取更新并参与交流。

---

### [PyData 2026 年 11 月 25 日聚会，2026 年 11 月 25 日星期三，下午 6:00 | Meetup](https://www.meetup.com/pydata-hamburg/events/317281931/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-772-november-19-2026)

**原文标题**: [PyData Nov 25th 2026 Meetup, Wed, Nov 25, 2026, 6:00 PM   | Meetup](https://www.meetup.com/pydata-hamburg/events/317281931/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-772-november-19-2026)

本次 PyData 汉堡聚会定于 2026 年 11 月 25 日（周三）18:00–21:00 CET，在德国汉堡 Große Bleichen 23-27 举行，由 Sanchit B. 和 Zeinab 主办；活动包含两场主题演讲、问答、交流及披萨。

- 📅 时间：2026 年 11 月 25 日 18:00–21:00 CET
- 📍 地点：Große Bleichen 23-27, 20354 Hamburg, Germany（汉堡）
- 🎙️ 主办：PyData Hamburg，主持人为 Sanchit B. 和 Zeinab
- 🗓️ 议程：18:00 入场；18:20 简短介绍；18:30–19:00 第一场演讲及问答；19:00–19:30 休息、交流与披萨；19:30–20:00 第二场演讲及问答；20:00–20:45 交流与披萨
- 👤 第一位讲者：Omar Bachet
- 🧩 第一场主题：Metadata as Infrastructure（将元数据作为基础设施）
- 💡 第一场要点：把元数据用于数据产品的发现、治理与运营，跨管道和领域团队采集并保持可信，连接访问管理、血缘、质量和变更通知等工作流
- 👤 第二位讲者：MeiJu Huang
- 🚀 第二场主题：From Code to C-Level: Strategic Business Communication for Engineers（从代码到 C 级管理层：工程师的战略性商业沟通）
- 💼 第二场要点：帮助工程师用战略、ROI 和业务目标表达技术价值，应对阻力并建立影响力，结合 Deloitte、OTTO 和健康科技创业经历
- 🧠 相关主题：机器学习、数据科学、Python、开源、NumPy
- 💬 活动聊天：报名参加后可加入，提前与其他参会者交流

---

### [PyData Prague #37 - Trust the Age of Juniors, Thu, Nov 26, 2026, 6:00 PM   | Meetup](https://www.meetup.com/pydata-prague/events/317314096/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-772-november-19-2026)

**原文标题**: [PyData Prague #37 - Trust the Age of Juniors, Thu, Nov 26, 2026, 6:00 PM   | Meetup](https://www.meetup.com/pydata-prague/events/317314096/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-772-november-19-2026)

第 37 届 PyData Prague 聚会以“Trust the Age of Juniors”为主题，将于 11 月 26 日（周四）18:00–21:00 CET 在布拉格 Flow Building 的 Apple 办公室举行。活动聚焦 Python 与数据社区、初级开发者友好、AI 时代的编程教学，以及如何用 AI 编写并交付可信代码。

- 📅 时间地点：11 月 26 日（周四）18:00–21:00 CET，Flow Building，Václavské nám. 47, Praha 1。
- 🎤 活动安排：Jan P. 和 Jakub U. 主办；18:00 开始社交，18:30 开始演讲，休息和会后可继续交流。
- 👩‍💻 社区目标：围绕 Python 和数据建设包容社区，欢迎不同技能与经验水平的人，包括初级开发者。
- ⚡ 闪电演讲：可提前联系主办方或在活动开始时报名，最多 5 分钟，主题需至少部分涉及 Python 和/或数据。
- 📢 议题一：Miroslav Brabenec（Everpure）讲“PyLadies 与 AI 时代的编程教学”，回顾 PyLadies 自 2014 年以来帮助女性进入科技、学习 Python，并探讨生成式 AI 改变软件开发后如何教初学者。
- 🤖 议题二：Atahan Aksoy（Apple）讲“交付可信代码：AI 编码实用指南”，介绍用 Claude 的日常工作流、端到端流程、自动化与 AI 自审，避免架构不匹配和质量下降。

---

