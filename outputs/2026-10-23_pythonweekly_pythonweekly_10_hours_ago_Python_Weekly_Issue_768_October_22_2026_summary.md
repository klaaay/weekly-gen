### [LiteLLM 再次遭劫持：恶意 1.107.0 Wheel 包窃取凭据并加载远程代码 - JFrog 安全研究](https://research.jfrog.com/post/litellm-hijacked-again/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-768-october-22-2026)

**原文标题**: [LiteLLM Hijacked Again: Malicious 1.107.0 Wheels Steal Credentials and Load Remote Code - JFrog Security Research](https://research.jfrog.com/post/litellm-hijacked-again/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-768-october-22-2026)

JFrog 安全研究团队在 LiteLLM 1.107.0 的 PyPI wheel 中发现恶意代码。这是 LiteLLM 在 2026 年第二次被劫持。恶意 wheel 是合法项目的功能副本，但额外加入了三个 Python 启动文件，可在不导入 `litellm` 的情况下窃取大量凭据，并建立每小时执行的远程代码通道。LiteLLM 称事件已控制，PyPI 和 Docker Hub 已移除受影响制品。

- 🧨 受影响范围：1.107.0 的全部 7 个平台 wheel 均含 `cook.pth`、`cook.py`、`sitecustomize.py`；官方 Docker 镜像及曾指向 1.107.0 的 `latest`、`main-latest`、`main-stable` 标签也应视为暴露。
- 🕵️ 供应链差异：源码分发包不含三个恶意文件，但 `pyproject.toml` 多了 `data = "cook"`；wheel 的 ZIP 时间戳和元数据与正常构建一致，提示注入发生在构建或制品阶段，具体根因仍未知。
- 🚀 启动即触发：`cook.pth` 会执行 `import cook`，`sitecustomize.py` 会启动分离加载器；受影响环境中的普通 Python 或 `pip` 启动也可能再次触发。
- 🔐 凭据窃取器 `privcollect`：收集 SSH/GPG/TLS 私钥、浏览器数据、云凭据、Kubernetes/Docker 密钥、CI/CD 与 IaC 密钥、包管理器凭据、AI 开发工具令牌、环境变量及 `/proc` 环境、云元数据。
- 🗄️ LiteLLM 专属风险：通过 `DATABASE_URL` 读取 `LiteLLM_CredentialsTable` 和 `LiteLLM_ProxyModelTable`，可一次性泄露多家上游 AI 提供商凭据。
- 📡 外传方式：数据用 AES-256-CBC 加密，RSA-4096 封装密钥，经明文 HTTP 发往 `www[.]litellm[.]dev/healthcheck`，带固定 `X-Token`；该域名是 `litellm.ai` 的仿冒域名。
- ⏱️ 远程加载器：`sitecustomize.py` 每小时从 GitHub raw 的 `letters9813/pythonclient-test/main/domain.txt` 获取 C2 域名，再下载并 `exec` `/codepy`，无完整性校验，等同任意代码执行。
- 🪟 Windows 差异：`sitecustomize.py` 因依赖 `os.fork()` 失败，但 `cook.pth` 仍会加载 `cook.py`，因此 Windows 安装仍会遭凭据窃取。
- 📭 观察时 `domain.txt` 为空，远程加载器暂休眠，但可随时重新激活；本地 `cook.py` 窃取器不受影响，仍会运行。
- 🧾 安全启示：只审查源码、Git tag 或 sdist 会漏掉 wheel 中的启动钩子；应验证实际安装 wheel 的 `RECORD` 内容和启动文件。
- 🧹 处置建议：避免所有 1.107.0 wheel；不要在受影响环境先运行 `pip`；先移除 `cook.pth`、`cook.py`、`sitecustomize.py`、`__pycache__` 编译文件、`/tmp` 锁与标记，终止相关分离进程。
- 🔁 凭据与取证：隔离主机/容器，轮换所有可达凭据（浏览器、SSH/GPG、云、K8s、CI/CD、AI 开发令牌、`DATABASE_URL`、LiteLLM 密钥等），调查 `/codepy` 执行，封禁相关域名并从可信制品重建。
- 🧬 关联与检测：本次与 2026 年 3 月 TeamPCP 事件使用不同载荷和基础设施，应分开处置；JFrog Xray/Curation 以 `XRAY-955589` 检测，社区跟踪 LiteLLM issue #47826。

---

### [](https://www.youtube.com/watch?v=EnEVtmbr-uM&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-768-october-22-2026)

**原文标题**: [Hamza Remmal – Bridging between Scala & Python with GraalVM #ScalaDays - YouTube](https://www.youtube.com/watch?v=EnEVtmbr-uM&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-768-october-22-2026)

本内容为 YouTube 网站页脚信息，主要列出平台相关入口、政策链接及版权声明。

- 📄 提供“关于”“新闻”“版权”“联系我们”等基础信息入口
- 👥 包含创作者、广告合作、开发者相关链接
- 📜 列出条款、隐私、政策与安全、YouTube 工作原理等政策说明
- 🧪 提供“测试新功能”入口
- ©️ 版权声明为 © 2026 Google LLC

---

### [Python 的二进制 wheel 与供应链攻击 | Artem Golubin](https://rushter.com/blog/python-binary-wheels/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-768-october-22-2026)

**原文标题**: [Python's binary wheels and supply chain attacks | Artem Golubin ](https://rushter.com/blog/python-binary-wheels/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-768-october-22-2026)

Python 的预编译 wheel 提升了安装效率，但源码与二进制可不一致、二进制又难以审计，使其成为 Python 供应链安全的薄弱点；作者预计此类攻击会增多，并建议从源码编译依赖、避免安装最新版本。

- 🚀 Python 包之所以快，常因核心用 C/C++/Rust 编译，Python 只作胶水；PyPI 的预编译 wheel 让用户免于自行编译。
- 📦 `pip install` 会优先使用 wheel；每个发行版需按 Python 版本、平台和架构提供不同 wheel，作者称其包最多发布 90 个 wheel。
- 🧩 没有 wheel 时，用户必须本地编译，需要正确的编译器和系统依赖，安装难度明显增加。
- ⚠️ wheel 的关键风险是：攻击者可同时发布干净源码和恶意二进制；目前无法确保二进制由同一源码编译，二进制证明也非强制。
- 🕵️ 恶意 Python 包几乎每日上传，多为 typo-squatting，合法包也可能被入侵；扫描器通常用 AST、沙箱和 LLM 分析源码。
- 🔍 二进制自动分析更困难，未知恶意软件需逆向；攻击者可植入延迟触发的小后门，数周不被发现，并针对安全软件较少的 Linux 等平台。
- 🛡️ 当前对二进制分析关注不足，多数初创公司只分析源码；作者认为这类供应链攻击会变得普遍。
- 🔧 作者认为目前唯一可行方案是从源码编译所有 Python 依赖，并避免安装最新版本。

---

### [如何在 PyTorch 的反向传播中运行图灵完备的恶意软件 | 向量空间的元素](https://elonlit.com/scrivings/how-to-run-turing-complete-malware-in-pytorchs-backward-pass/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-768-october-22-2026)

**原文标题**: [How to Run Turing-Complete Malware in PyTorch's Backward Pass | Elements of a Vector Space](https://elonlit.com/scrivings/how-to-run-turing-complete-malware-in-pytorchs-backward-pass/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-768-october-22-2026)

文章指出，攻击者可利用 IEEE 754 浮点舍入与 PyTorch 自动微分符号计算之间的不一致，构造一个前向值为 0.0、反向梯度却非零的损失项；从而在正常训练循环的 `backward()` 与 `optimizer.step()` 中执行任意计算，甚至运行图灵完备程序，并可将其伪装成普通正则项或预编译 CUDA 扩展。

- 🧨 核心结论：可在任意 PyTorch 网络的反向传播中运行图灵完备程序；损失和训练指标可始终显示为 `0.0`。
- 🎯 威胁模型：攻击者只需发布名为 `UltraLoss` 的正则器，不必修改基础 checkpoint、模型架构、数据集或优化器；`aux_loss` 每轮报告 `0.000000`，但反向传播会执行载荷。
- 🧮 将 SGD 变成状态机：令 `F(θ)` 为下一状态，目标梯度为 `v = θ - F(θ)`；当学习率为 1 时，SGD 更新得到 `θ_next = θ - v = F(θ)`。
- 🔬 浮点陷阱：函数 `h(u) = (2^30 + u) - 2^30` 在前向 `float32` 中因 ULP 舍入返回 `0.0`，但 Autograd 将加减法符号微分为 `1`；`bfloat16` 可用更小常数实现。
- 🕵️ 隐蔽的“detach”：`u - h(u)` 前向传值、反向梯度为 0，用纯加减法阻断梯度，避免代码中出现显眼 `.detach()`。
- 🚪 乘积门控：损失 `L = Σ(v - h(v)) * h(θ)` 前向为 0；反向乘积规则保存 `A = v`、`B = 0`，使 `θ.grad = v`，`step()` 后权重变为 `F(θ)`。
- 🧬 概念验证：可在参数张量中运行 Conway 生命游戏，零损失推进脉冲星、振荡器和滑翔机；在 CNN 上训练 MNIST 时，1024 个权重完成 2345 代生命游戏且无错误，测试精度 98.80%，基线 98.84%。
- 🥷 隐藏手法：将元胞自动机包装成“流形曲率正则”或卷积加 `clamp`；把关键常量放入 JSON 伪装成超参数；或编译进 CUDA `.so`，Python 仅保留薄包装。
- ⚙️ 扩展能力：可适配 Adam、Minsky 双计数器机器或多训练步时钟；大模型中未使用词表行、MoE 未选专家可作隔离暂存区，并在第 N 代把后门写入活跃投影层或分类头。
- 🛡️ 绕过防御：训练从官方哈希验证的 checkpoint 开始，静态扫描看不到训练过程中组装的载荷；程序完全在 GPU 张量内核中执行，不触网络、文件系统或子进程，容器沙箱难以发现。
- 🧩 编译器两难：`torch.compile`、XLA、Triton 若代数化简 `u - ((C + u) - C)` 可消除漏洞，但会破坏 Kahan 求和、`TwoSum` 等浮点误差补偿；若不化简，该漏洞将长期存在。
- ⚠️ 安全建议：应把未使用参数视为受保护虚拟机；ML 安全团队需重新审视浮点语义、自动微分和编译器优化边界。

---

### [7 个让你的代码变得更糟的 Python 特性 - YouTube](https://www.youtube.com/watch?v=RHCyTWaRZSk&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-768-october-22-2026)

**原文标题**: [7 Python Features That Make Your Code Worse - YouTube](https://www.youtube.com/watch?v=RHCyTWaRZSk&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-768-october-22-2026)

该文本是 YouTube 页面底部的导航与版权信息，涵盖平台介绍、合作联系、法律条款、功能说明及 Google LLC 的版权声明。

- ℹ️ 提供“关于”“新闻”等平台介绍与媒体入口。
- 📬 包含“联系我们”“创作者”“广告”“开发者”等合作与支持链接。
- ⚖️ 列出“条款”“隐私”“政策与安全”等法律相关信息。
- 🛠️ 说明“YouTube 运作方式”，并提供“测试新功能”入口。
- ©️ 版权归属标注为 © 2026 Google LLC。

---

### [如何像 Jev 一样构建决策模型 | Antonello Fratepietro](https://www.fratepietro.com/2026/how-to-build-a-decision-model-like-jev/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-768-october-22-2026)

**原文标题**: [How to Build a Decision Model Like Jev | Antonello Fratepietro](https://www.fratepietro.com/2026/how-to-build-a-decision-model-like-jev/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-768-october-22-2026)

本文介绍如何构建类似 Jev 的决策模型：不再让 LLM 逐 token 生成文本，而是把模型调用拆成一次 prefill 前向计算，直接输出已知选项上的概率分布；同时说明 Hugging Face `transformers serve` 的零样本 `/v1/systemone` 快速路径、预留选项 token 与 `<readout>` 头的训练方法、概率校准、树批处理，以及通过黑盒探测推断 Jev 的底层架构与训练策略，最后给出四种决策模型选型方案。

- 🧠 **Prefill 与 Decode 分离**：Prefill 并行读取提示且受算力限制；Decode 逐 token 输出并反复读取权重，受显存带宽限制，因此文本生成成本高。
- 🎯 **多数软件决策不需要生成文本**：工单路由、风险工具调用审核、事件评分、看涨概率等任务，真正需要的是对固定结果集的概率分布。
- 📦 **Jev 的 typed contract**：`/v1/systemone` 接收一个 `state` 和一组命名 `questions`，支持 `choice`（最多 255 个选项）、`noul`（是/否概率）、`score`（2–10 级有序评分）。
- ⚡ **零输出 token**：模型只做一次 prefill，不生成任何输出 token，直接返回每个选项的概率。
- 🛠️ **Hugging Face 快速路径**：`transformers serve` 已原生支持 `/v1/systemone`，可将 250+ 开放 LLM/VLM 架构变成 logit-scoring 决策模型，并支持最多 4 张 base64 图片输入。
- ⚠️ **零样本字母评分有三重限制**：只能覆盖 26 个字母、预训练先验污染概率、选项槽位存在位置偏差。
- 🔤 **预留选项 token 与 `<readout>` 头**：加入 `<opt_0>…<opt_254>`、`<yes>/<no>`、`<lvl_1>…<lvl_10>` 等专用 token，在选项描述之后放置选项 token，并用字母 embedding 热启动。
- 🔀 **训练时打乱选项顺序**：消除位置偏差，迫使 `<readout>` 按内容而非槽位分配概率；`score` 还可加入 RPS 距离惩罚。
- 🌡️ **概率校准至关重要**：用温度缩放分别校准 `choice`、`noul`、`score`；温度应针对生产评分规则调优，而不是只看对数似然。
- 📊 **校准陷阱**： pooled ECE 会掩盖任务与上下文长度差异；one-hot 标签会放大不确定性任务中的多数答案；量化后必须重新验证校准。
- 🌳 **树批处理降低多问题延迟**：把 state 与所有问题分支打包成一个序列，配合块对角树注意力掩码和按分支重置 RoPE 位置 ID，避免前缀缓存的主机端开销与调度竞争。
- 🔍 **黑盒探测揭示 Jev 特征**：身份探测、对齐先验、PopQA 稀有事实错误指纹均指向 Qwen 3.5 35B-A3B 规模底座；单次 prefill 在 MMLU-Pro、代码数学、单位换算上显著超过非思考版 Qwen。
- 🧪 **合成数据与程序验证训练**：TypeSafe 使用“程序在环”的合成任务与软概率目标，不需要 PPO rollout；RLCD 本质是对程序验证标签做交叉熵训练。
- ✂️ **词表手术**：Jev 词表约 145,072 token，由 Qwen 3.5 与 GPT-4o/gpt-oss 拼接并裁剪而来；保留共同 token、删除大量 Qwen 独有 token、加入 GPT-4o 复合 token，并用 Fast Vocabulary Transfer 初始化。
- 💰 **非拉丁语言存在 token 税**：裁剪后中文约 1.7 倍 token，俄语/希腊语/阿拉伯语/日语约 2 倍，泰语约 4 倍，API 按输入 token 计费会放大成本。
- 🧭 **四种选型**：小型本地双向编码器适合低延迟边缘场景；`transformers serve` 适合零样本原型与多模态；托管 Jev 适合长文档与宽问题批次；4B–12B 微调因果决策模型适合 VPC 内高并发生产。

---

### [Apache Iceberg 表面之下 - YouTube](https://www.youtube.com/watch?v=9Fz5noobWcE&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-768-october-22-2026)

**原文标题**: [apache iceberg beneath the surface - YouTube](https://www.youtube.com/watch?v=9Fz5noobWcE&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-768-october-22-2026)

该文本是 YouTube 网站页脚信息，汇总了平台导航链接、法律与政策说明、创作者及开发者资源、联系方式，以及 Google 的版权声明。

- ℹ️ 包含“关于”“新闻”“联系我们”等平台介绍与联系入口。
- 🎬 提供“创作者”“广告”“开发者”等面向内容创作与商业合作的链接。
- 📜 列出“版权”“条款”“隐私”“政策与安全”等法律与政策信息。
- ⚙️ 包含“YouTube 的工作原理”和“测试新功能”等说明与功能入口。
- ©️ 页脚注明版权归属：© 2026 Google LLC。

---

### [](https://pytorch.org/blog/introducing-torchtpu/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-768-october-22-2026)

**原文标题**: [Introducing TorchTPU - PyTorch](https://pytorch.org/blog/introducing-torchtpu/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-768-october-22-2026)

TorchTPU 是 Google 与 Meta 合作开源的 PyTorch 原生 TPU 后端，目标是让现有 PyTorch 工作负载仅需将 `.to("cuda")` 改为 `.to("tpu")` 即可在 TPU 上运行，并在推理与训练上提供有竞争力的性能；它基于 XLA/StableHLO/PjRT，支持 eager、`torch.compile`、分布式、Pallas/Helion 自定义内核和三级编译缓存，已在 Hugging Face 模型、vLLM/SGLang 推理、TorchTitan 训练及 TorchRec 推荐系统中验证。

- 🎯 定位与原则：TorchTPU 于 2025 年中在 Google 启动，与 Meta PyTorch 团队合作，强调“PyTorch 公民”、用户易用性和提升 TPU 编程栈水平，避免运行时依赖 JAX。
- 🧱 底层架构：TPU 由 TensorCore/MXU、SparseCore、HBM、ICI 和 DCN 组成；通过 StableHLO/Mosaic 进入 XLA 编译器栈，PjRT 负责编译、启动和数据拷贝。
- ⚙️ 执行模式：支持 Strict eager、Debug 同步模式和新颖的 DeferAndFuse 混合模式；后者可融合多个 Aten 算子，比 Strict eager 快 50% 以上并降低峰值 HBM。
- 🧠 编译能力：以 Torch Dynamo 为前端注册 `backend="tpu"`，将 FX 图整体编译为 StableHLO；提供 tier-1/2/3 编译缓存，分别支持进程内、同机跨进程和跨主机复用。
- 🧊 动态形状：通过 XLA Bounded Dynamism 支持有界动态形状，按最大上界分配缓冲并只编译一次，减少因 batch/seq 变化触发的重编译。
- 👁️ 视图与流：通过视图分解、视图反转和延迟算子支持 PyTorch 可变视图语义；实现 Stream API，可将流固定到 SparseCore，并用 DMA 引擎协调异步数据传输。
- 🌐 分布式：在 Process Group API 层实现 TPU collectives，支持 DTensor、FSDPv2、SimpleFSDP、FairScale 等；采用一进程一设备模型，提供 `tpu_dist` 后端和 `topology_aware_mesh()` 优化物理拓扑映射。
- 🧩 自定义内核：支持 Pallas 内核、Tokamax 高性能 TPU 内核库和实验性 Helion DSL；还支持通过 Pallas 编写直接走 ICI RDMA 的分布式通信内核。
- 📚 生态兼容：已集成 Hugging Face Transformers v5、Diffusers、Kernels，以及 vLLM、SGLang、TorchTitan、Ray、TorchRec 等框架。
- ✅ 模型验证：自动化测试覆盖 4,917 个 Hugging Face 模型、500+ 架构族；Tier 1 无崩溃通过率 98%，Tier 2 相对 GPU 数值一致性 97%，有界动态形状在 839 个模型中 834 个数值正确。
- 🚀 纯 PyTorch 性能：Muse Glimmer 30B 仅用标准 PyTorch 模块和算子，在单 TPUv7 上推理达约 25.7k TPS/59% MFU（seq 5,120）；4 芯片训练达约 5.6k TPS/TPU、38% MFU。
- 📈 POD 级训练：Qwen3 MoE 235B 在 TorchTitan 上扩展至 1 个 TPU v7 POD，8,192 芯片时仍约 2,104 TPS/TensorCore、27.1% MFU，呈弱 scaling，MFU 基本持平。
- 💵 LLM 推理：SemiAnalysis InferenceX 中 vLLM-TorchTPU 在 8K/1K 场景实现每百万 token 2.01 美分；AgentX 上 Qwen 3.5 达 0.83 美分并取得 Pareto 前沿领先。
- 🧪 微调与训练框架：TorchTitan 上 FLUX.1-dev 通过 DeferAndFuse、SimpleFSDP、Pallas SplashAttention、`torch.compile` 等优化，步时从 11.49s 降至 2.78s，约 3.80× 加速；Llama 3 405B 在 1,024 芯片上达 500 tokens/sec/chip、50%+ MFU。
- 🗂️ 推荐系统：TorchRec 原生 TPU 后端在 32 芯片 TPU v7x 上跑 DLRM v2，达到与 JAX 基线一致的 18.3ms 步时，并实现 In-Place Optimizer Fusion 以消除梯度内存开销。
- 🛣️ 未来路线：未来 6–12 个月聚焦生产硬化、FP8/FP4 量化、SymInt/有界动态形状完善、POD 级训练与 RL、vLLM/SGLang 服务优化、新架构支持、通信优化和规模化诊断工具。

---

### [Django：使用 norwegianblue 检查版本支持 - Adam Johnson](https://adamj.eu/tech/2026/10/16/django-norwegianblue/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-768-october-22-2026)

**原文标题**: [Django: check version support with norwegianblue - Adam Johnson](https://adamj.eu/tech/2026/10/16/django-norwegianblue/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-768-october-22-2026)

norwegianblue 是一个查询软件支持周期与 EOL 日期的命令行工具，数据来自社区维护的 endoflife.date，适合 Django 开发者检查 Django、Python、PostgreSQL 等相关组件的版本支持情况。
- 🧩 Django 项目常涉及 Django、Python、数据库、缓存等多个发布周期，使用不受支持的版本会错过安全与缺陷修复。
- 🦜 norwegianblue 由 Python 发布经理 Hugo van Kemenade 开发，名称源自《蒙提·派森的飞行马戏团》的“死鹦鹉”桥段。
- ⚙️ 工具提供 `norwegianblue` 和更短的别名 `eol`，推荐使用 `eol`；可用 `uv tool install norwegianblue`、pip 或 pipx 全局安装。
- 📋 直接运行 `eol` 可列出已知产品名；运行 `eol django` 可查看 Django 各功能版本的发布、最新补丁、主流支持结束、EOL 和支持的 Python 版本范围。
- 🚦 输出使用颜色编码：红色表示日期已过，黄色表示未来六个月内到期，绿色表示更晚；版本周期名称按 EOL 日期着色，便于快速识别不支持版本。
- 🐍 示例显示 Django 6.1、6.0、5.2 仍受支持，其中 6.0 已进入仅安全修复阶段；Django 5.0 和 5.1 已 EOL，应尽快升级。
- 🐘 可检查 Python 与 PostgreSQL：Python 3.10 已 EOL；PostgreSQL 14 下月 EOL 并以黄色警示，Django 通常也会在 PostgreSQL EOL 前后停止支持旧版本。
- 🗄️ endoflife.date 覆盖数百种产品，包括 MariaDB、MySQL、SQLite、Oracle、SQL Server、云托管数据库、Redis、Valkey、Memcached、Elasticsearch、Ubuntu、Debian、Nginx、Node.js 和 Wagtail 等。
- 💾 norwegianblue 会缓存当天数据，重复运行较快；还支持 Markdown、reStructuredText、JSON 等输出格式，便于写入文档或脚本检查。
- 🙏 文章最后感谢 Hugo van Kemenade 制作工具，以及 endoflife.date 贡献者维护数据。

---

### [如何在 Django 网站上改进技术 SEO | Code With Stein](https://codewithstein.com/improve-technical-seo-django/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-768-october-22-2026)

**原文标题**: [How to improve technical SEO on a Django website | Code With Stein](https://codewithstein.com/improve-technical-seo-django/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-768-october-22-2026)

Django 默认的服务端渲染对 SEO 有良好基础，但标题描述、规范 URL、站点地图、爬虫指令、状态码和性能等仍需手动配置。本文按页面头部、URL 规范、抓取与索引、状态码、性能与验证的顺序，给出可落地的技术 SEO 清单。

- 🏷️ 为重要页面设置独立 title 和 meta description，并在 Django admin 中可编辑，避免全站共用同一标题。
- 🔗 添加自引用 canonical URL，基于 Django 路由生成，避免查询参数或域名变体造成重复内容。
- 🌐 统一域名、HTTPS 和末尾斜杠规则，旧域名或 HTTP 请求应永久重定向到规范版本。
- 🔒 在 Nginx 等反向代理后正确配置 `SECURE_PROXY_SSL_HEADER`，确保 Django 知道原始请求是 HTTPS。
- 🗺️ 使用 Django sitemap 框架生成 `/sitemap.xml`，只包含已发布内容，并提供准确的 `lastmod`。
- 🤖 提供简洁的 `robots.txt`，禁止抓取后台并声明 sitemap 地址；注意它控制抓取而非索引。
- 🚫 对内部搜索页、临时页等不应出现在搜索结果中的页面使用 `noindex, follow`，且不要同时在 robots.txt 中阻止抓取。
- ❌ 不存在的页面应返回真实 HTTP 404，可使用自定义 404 模板但不要返回 200。
- ↪️ URL 变更时使用永久重定向 301，避免有外链或已被收录的旧 URL 直接变成 404。
- 🔍 谨慎处理筛选和查询参数，明确哪些版本可索引，避免大量参数组合成为意外落地页。
- 📊 在内容匹配的页面添加 JSON-LD 结构化数据，并确保其准确描述页面可见内容。
- 🧭 通过普通 `<a href>` 内链、分类页和相关文章让重要页面可被正常爬取，避免依赖 JavaScript 点击导航。
- ⚡ 优化数据库查询，使用 `select_related()`、`prefetch_related()` 和缓存减少慢查询与重复渲染。
- 🖼️ 优化图片尺寸，设置 width/height，首屏大图慎用懒加载，下方图片可使用 `loading="lazy"`。
- 🚀 生产环境让 Nginx/CDN 处理静态资源，并控制 CSS/JavaScript 体积，关注 Core Web Vitals。
- ✅ 部署后用 `curl -I` 检查实际响应和生成源码，并通过 Google Search Console 提交 sitemap、检查索引与 canonical。

---

### [将 uv 和 ty 结合在一起](https://astral.sh/blog/uv-ty-integration?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-768-october-22-2026)

**原文标题**: [Bringing uv and ty together](https://astral.sh/blog/uv-ty-integration?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-768-october-22-2026)

Astral 于 2026 年 10 月 13 日发布 uv 与 ty 的实验性集成预览，通过共享项目环境与代码理解，为 PEP 723 Python 脚本提供一等支持，并推出统一的 `uv check` 命令，向集成化 Astral 工具链迈出一步。

- 🔗 uv 负责理解项目环境与依赖，ty 负责理解代码；二者结合可提供单独工具难以实现的能力。
- 🐍 基于 PEP 723 内联元数据，ty 可在命令行和编辑器中发现脚本，并调用 uv 为每个脚本准备独立环境进行类型检查。
- 🧠 编辑器集成启用后，ty 会在后台自动调用 uv 准备脚本环境，并提供补全、悬停信息和跳转到定义等功能。
- ✅ 新增 `uv check` 统一诊断入口：自动准备环境、安装依赖并用 ty 检查项目，支持单包、工作区和 PEP 723 脚本。
- 📦 `uv check` 支持 `--package`、`--all-packages` 和 `--script`；并自动使用 lockfile 中记录的 ty 版本，方便开发者与 CI 保持一致。
- 🪝 ty 的 pre-commit hook 底层也使用 `uv check`，自动根据项目依赖声明为 ty 设置环境。
- ⚙️ 集成依赖 uv workspace metadata；因自动安装依赖可能执行第三方代码，PEP 723 脚本的自动环境设置目前需显式启用。
- 🧪 可通过 VS Code 设置 `ty.experimental.useUv` 为 `on`，或使用 `TY_UV=scripts ty check` 试用；`uv check` 会自动启用集成，无需额外配置。
- 📌 需要 uv 0.12.3+ 和 ty 0.0.76+；未来计划支持 Ruff、检测未使用依赖等新检查，并继续推进 ty 稳定版。

---

### [用Python构建多模态AI应用（初学者项目）- YouTube](https://www.youtube.com/watch?v=aypkvuGFq5Y&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-768-october-22-2026)

**原文标题**: [Build a Multimodal AI App in Python (Beginner Project) - YouTube](https://www.youtube.com/watch?v=aypkvuGFq5Y&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-768-october-22-2026)

这是 YouTube 网站底部的导航与法律信息区域，汇总了平台介绍、政策条款、创作者与开发者等入口，并标注 Google LLC 的版权信息。

- ℹ️ 包含“关于、新闻、版权、联系我们”等基础信息入口。
- 👥 提供创作者、广告合作与开发者相关链接。
- 📜 列出条款、隐私、政策与安全等法律与合规页面。
- ⚙️ 包含“YouTube 的工作原理”和“测试新功能”入口。
- ©️ 版权声明为 © 2026 Google LLC。

---

### [django-lifecycle - Django 模型的钩子（Signals 的替代方案） - YouTube](https://www.youtube.com/watch?v=sNdopNFOEB8&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-768-october-22-2026)

**原文标题**: [django-lifecycle - hooks for Django models (Signals alternative) - YouTube](https://www.youtube.com/watch?v=sNdopNFOEB8&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-768-october-22-2026)

该内容为 YouTube 页面底部的导航与版权信息，涵盖公司介绍、新闻、版权、联系方式、创作者与广告服务、开发者资源、法律条款、隐私与安全政策、YouTube 运作方式、新功能测试以及 Google LLC 的版权声明。

- 🏢 提供“关于”“新闻”“联系我们”等公司与沟通入口。
- ©️ 包含版权、条款、隐私及政策与安全相关链接。
- 👥 面向创作者、广告主和开发者提供相应服务入口。
- ⚙️ 说明 YouTube 的运作方式，并提供新功能测试入口。
- 📄 页面底部标注“© 2026 Google LLC”版权信息。

---

### [获取失败](https://lemire.me/blog/2026/10/17/decoding-base64-in-python-at-10-gigabytes-per-second/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-768-october-22-2026)

**原文标题**: [Failed to retrieve](https://lemire.me/blog/2026/10/17/decoding-base64-in-python-at-10-gigabytes-per-second/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-768-october-22-2026)

无法总结：获取内容失败，状态码 403。

---

### [推出 TorchNeuron：AWS Trainium 的原生 PyTorch 后端 - PyTorch](https://pytorch.org/blog/introducing-torchneuron-native-pytorch-backend-for-aws-trainium/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-768-october-22-2026)

**原文标题**: [Introducing TorchNeuron: Native PyTorch backend for AWS Trainium - PyTorch](https://pytorch.org/blog/introducing-torchneuron-native-pytorch-backend-for-aws-trainium/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-768-october-22-2026)

AWS 发布 TorchNeuron，一个面向 AWS Trainium 的开源原生 PyTorch 后端，目标是让现有 PyTorch 模型代码、库和工具几乎无需修改即可在 Trainium 上训练与推理。它基于 PyTorch 社区的 PrivateUse1 设备后端和 torch.accelerator 等扩展点构建，支持 eager、torch.compile、NKI 自定义内核和性能分析，并计划于 2026 年 10 月 20 日以 Apache 2.0 开源、公测形式发布。

- 🚀 **核心发布**：TorchNeuron 是 Trainium 的原生 PyTorch 后端，模型代码、常用库和工具可直接运行在 Trainium 上。
- 🧩 **官方扩展机制**：基于 PyTorch 的 PrivateUse1 自定义设备后端和 torch.accelerator API，将 Trainium 注册为标准 PyTorch 设备。
- 🖥️ **设备切换简单**：使用 `.to('neuron')` 即可把模型放到 Trainium；编译模式可通过 `torch.compiler.set_default_backend("neuron")` 或 `backend="neuron"` 启用。
- ⚡ **两种执行模式**：支持 eager 执行用于研究和调试，并提供实验性的 adaptive eager 模式提升性能；`torch.compile` 用于生产级高性能模型。
- 🔥 **Trainium2/3 支持**：TorchNeuron 支持 Trainium2 和 Trainium3，并原生支持 FlexAttention。
- 🧠 **NKI 自定义内核**：通过 Neuron Kernel Interface 编写和注册自定义算子，同时提供开源 NKI-lib，包含 FlashAttention、MoE blockwise 等优化算子。
- 📊 **性能分析**：集成 `torch.profiler` 和 NeuronConfig，可通过 Neuron Explorer 查看框架、运行时和设备执行轨迹，并支持 Parquet 输出和按设备耗时排序定位热点。
- 🔢 **算子与数据类型**：覆盖文本、多模态、视觉语言、图像/视频生成、状态空间模型和世界模型等场景；支持 BF16、FP32、FP16、整数和布尔类型及 autocast 混合精度。
- 🧪 **FP8/TorchAO**：TorchAO 和 FP8 目前处于私有 Beta，计划在下一版本正式可用。
- 🌐 **分布式能力**：支持 DDP、FSDP2、SimpleFSDP、张量并行、流水线并行及 FSDP2+TP、ZeRO 等组合；支持 DTensor、DeviceMesh、集合通信和 P2P API。
- 🔗 **通信原生优化**：集合通信在节点内使用 Trainium 专用 collective cores，节点间使用 EFA，无需修改 PyTorch API。
- 🧵 **流与事件**：原生支持 torch streams 和 events，`torch_neuronx.Stream/Event` 映射到 Trainium 硬件队列，并保持 PyTorch 流语义。
- 🏢 **客户与生态**：Cartesia 用于语音 AI，Deepgram 报告 Trainium 每美元处理输入音频秒数比现有 GPU 基线高约 60%，Hugging Face 将 Trainium 作为 Transformers/Diffusers 的原生后端。
- 🤝 **合作伙伴**：Anyscale、Decart、Kernelize、Loka、Luminal、Makora、Modular、Nota AI、Radix、Wafer、Yasp 等正在共建 Trainium 生态。
- 🧰 **框架兼容**：TorchTitan 已支持 Trainium，`torchtitan-neuron` 提供 NKI 内核、调优配置和 Neuron Explorer 集成；Hugging Face Transformers v5 支持 `device_map="neuron"`。
- 🧪 **测试覆盖**：对 10 万个 Hugging Face 模型进行广泛扫描，覆盖约 99.9% 实际使用量；同时运行 PyTorch 上游 ATen、Dynamo、分布式和 profiler 测试套件。
- 📉 **测试差距**：2026 年 8 月约 15.4 万个测试结果，约 6.9 万个跳过；其中约 3.9 万个为 Neuron 主动跳过，主要涉及暂未原生支持的算子、CUDA 专用测试和首版不支持的特定功能。
- 📦 **获取方式**：2026 年 10 月 20 日起可通过 AWS Neuron pip 源执行 `pip install torch-neuronx` 安装公测版。
- 🔗 **开源资源**：代码将发布于 `github.com/aws-neuron/torch-neuronx`，并配套 Trainium、Neuron SDK 和 Neuron 文档资源。
- 🎤 **PyTorch Conference**：将在北美 PyTorch Conference 上开源 TorchNeuron、发布 pip 包，并举办技术深入分享和现场演示。

---

### [Django ORM、迁移与 makemigrations 综合教程](https://my-space.io/blog/django-orm-migrations/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-768-october-22-2026)

**原文标题**: [Comprehensive Tutorial on Django ORM, Migrations and makemigrations](https://my-space.io/blog/django-orm-migrations/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-768-october-22-2026)

本文以搭建一个 SQLite 咖啡与茶叶商店为例，系统讲解 Django ORM、`makemigrations` 与 `migrate` 的工作机制，并演示查询、必填字段回填、迁移回滚、团队协作冲突处理，以及用 Django 6.1 的 fetch modes 解决 N+1 查询问题。

- 🧠 Django ORM 用 Python 模型类映射数据库表：类对应表、字段对应列、对象对应行；Django 自动生成 SQL，可用 `print(queryset.query)` 或 `sqlmigrate` 查看。
- 🔁 `makemigrations` 只比较模型与已有迁移文件并生成迁移脚本，不修改数据库；`migrate` 才执行脚本并把执行记录写入 `django_migrations`。
- 🛠️ 标准流程是：修改 `models.py` → 运行 `makemigrations` → 检查并提交迁移文件 → 运行 `migrate`；`showmigrations` 查看状态，`migrate --plan` 预演操作。
- 🔍 ORM 查询支持 `filter()`、`get()`、`values_list()`、`Q()`、`F()`、`annotate()` 等；QuerySet 惰性执行，`count()` 只发 COUNT 查询，`related_name` 可反向访问关联对象。
- 🧱 给已有数据表添加必填字段要分三步：先加 `null=True` 字段，再用 `RunPython` 数据迁移回填，最后改为必填/唯一；数据迁移应用 `apps.get_model()` 获取历史模型，并提供反向函数。
- ↩️ 回滚用 `migrate shop 0002` 指定目标迁移，或用 `migrate shop zero` 撤销整个应用；`RunPython` 无反向函数会报 `IrreversibleError`，可用 `RunPython.noop` 或自定义反向函数。
- 👥 团队迁移不同步常见于拉代码后忘记 `migrate`、切分支未撤销本分支迁移、两分支生成同编号迁移；前者执行 `migrate`，切分支前先 unapply，同编号用 `makemigrations --merge`。
- 🌿 `migrate --check` 和 `makemigrations --check` 适合部署或 CI：前者检查未应用迁移，后者检查模型改动未生成迁移，也能发现迁移冲突。
- ⚡ N+1 问题指循环访问关联对象时每行多一次查询；`select_related()` 用 JOIN 一次查完，Django 6.1 的 `FETCH_PEERS` 可按需用两次查询批量加载关联对象，`FETCH_RAISE` 可阻止隐式查询。
- 🧪 可用 `CaptureQueriesContext` 或 `assertNumQueries` 固定页面查询数，防止模板改动重新引入 N+1。
- 🚨 常见错误：`no such table/column` 多为未 `migrate`；非空字段报错需回填或设置默认值；`UNIQUE constraint failed` 多因一次性默认值重复；`Conflicting migrations` 用 `--merge`；`migrate --fake` 应谨慎使用。
- ✅ 迁移清单：模型变更后生成并检查迁移、迁移文件与模型一起提交、每次 pull 后 `migrate`、切分支前撤销迁移、CI 跑 `makemigrations --check`、循环访问关联对象时使用 `select_related()` 或 `FETCH_PEERS`。

---

### [](https://github.com/lightseekorg/tokenspeed?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-768-october-22-2026)

**原文标题**: [GitHub - lightseekorg/tokenspeed: TokenSpeed is a speed-of-light LLM inference engine. · GitHub](https://github.com/lightseekorg/tokenspeed?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-768-october-22-2026)

TokenSpeed 是 LightSeek 基金会开源的“光速级”LLM 推理引擎，面向 Agentic 工作负载，目标是兼具 TensorRT-LLM 级性能与 vLLM 级易用性，并已成为 PyTorch 生态项目。

- 🚀 **定位明确**：专为生产级 Agentic 工作负载打造，追求极致推理性能。
- 🧠 **架构创新**：首次分离控制面与执行面；控制面用 C++ 有限状态机，借助类型系统在编译期保障请求生命周期与 KV Cache 资源安全；执行面用 Python 提升迭代效率。
- 🧩 **内核模块化**：内核作为一等子系统，提供可移植公共 API、集中注册表与选择机制，并支持异构加速器插件；包含 Blackwell 上最快的 MLA 实现之一。
- ⚡ **低开销入口**：采用 SMG 集成的 AsyncLLM，降低 CPU 侧请求处理开销。
- 🏛️ **中立开源**：由非营利 LightSeek Foundation 支持，获 NVIDIA、AMD 等厂商硬件与工程支持，避免商业公司主导。
- 📈 **社区热度**：约 2.8k stars、367 forks、17 watchers、1978 commits，另有 9 个 issue、134 个 PR，采用 MIT 许可证。
- 🏎️ **性能亮点**：Qwen3.8-Flash-Next 在 GB300 上达 685 tokens/s/用户；Qwen3.5-397B-A17B 在 Agentic 负载达 580 TPS；Kimi K3 在 AMD MI355X 上持续优化。
- 🆕 **生态进展**：2026 年新闻覆盖 EAGLE-4 训练与服务、Reflection Beam 501B MoE 在 GB200 上 NVFP4 服务、TokenSpeed MLA 2 面向 Vera Rubin、Qwen3.8 2.4T 规模 Day 0 支持等。
- 📊 **对比与文档**：提供与 TensorRT-LLM 在 Agentic 工作负载（Kimi K2.5、B200）上的 Pareto 曲线对比，并有文档索引、快速开始、模型配方、服务参数、并行化指南等资料。
- 📚 **工程完备**：仓库包含贡献指南、安全政策、治理文件与引用信息，便于部署、研究和二次开发。

---

### [GitHub - llm-d/llm-d：在 Kubernetes 上使用现代加速器实现最先进的推理性能 · GitHub](https://github.com/llm-d/llm-d?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-768-october-22-2026)

**原文标题**: [GitHub - llm-d/llm-d: State of the art inference performance with modern accelerators on Kubernetes · GitHub](https://github.com/llm-d/llm-d?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-768-october-22-2026)

llm-d 是面向 Kubernetes 的高性能分布式 LLM 推理服务栈，旨在帮助用户在多种加速器和基础设施上快速达到 SOTA 推理性能。项目已加入 CNCF 沙箱，由 Red Hat、Google Cloud、IBM Research、CoreWeave 和 NVIDIA 共同创立，围绕智能路由、KV 缓存管理、大模型服务、运维与批处理提供生产级能力。

- 🎯 项目定位：为 Kubernetes 上的生产部署提供高性能分布式推理，兼容 vLLM、SGLang 等模型服务器，支持主流开源大模型与多种硬件加速器。
- 🏛️ 社区背景：CNCF 沙箱项目，由 Red Hat、Google Cloud、IBM Research、CoreWeave、NVIDIA 创立，并获得 AMD、Cisco、Hugging Face、Intel、Lambda、Mistral AI、UC Berkeley、University of Chicago 等支持。
- 🧠 智能路由：通过前缀缓存感知和负载感知均衡提升性能，并探索基于预测延迟的调度以降低延迟、提高吞吐。
- 🗂️ KV 缓存管理：支持向 CPU/磁盘分层卸载，并对 KV 缓存状态进行全局索引，提升多轮请求的有效工作集。
- 🧱 大模型服务：利用 prefill/decode 分离和宽专家并行优化 DeepSeek-R1、GPT-OSS 等超大模型。
- ⚙️ 运维与批处理：提供多租户智能流控、SLO 感知自动扩缩容，以及 OpenAI 兼容 Batch API 和异步处理。
- 📈 性能亮点：前缀缓存感知路由实现 3 倍输出吞吐和 2 倍更快 TTFT；预测延迟调度降低 40% TTFT/ITL；P/D 分离最高提升 70% tokens/sec；分层 KV 卸载在 250 并发下提升 13.9 倍吞吐。
- 🚀 版本动态：v0.7 带来优化基线稳定化、kustomize 优先迁移指南、扩展夜间 CI、预测延迟调度 GA、实验性批处理网关和文档重构；v0.5/v0.4 也包含多项性能与功能更新。
- 🧭 上手资源：提供 Quickstart、Optimized Baseline、well-lit path 指南、Helm charts、可复现基准 Prism 和加速器文档。
- 🤝 参与贡献：遵循 CNCF 行为准则，提供贡献指南、SIG、Slack、Google Group、双周例会等协作渠道，项目采用 Apache-2.0 许可。

---

### [](https://github.com/deepseek-ai/DeepInfer?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-768-october-22-2026)

**原文标题**: [GitHub - deepseek-ai/DeepInfer: DeepInfer: High-performance, large-scale inference framework for DeepSeek models · GitHub](https://github.com/deepseek-ai/DeepInfer?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-768-october-22-2026)

DeepInfer 是 DeepSeek 开源的高性能、大规模推理框架，用于支撑其生产级服务；本次开源主要提供离线推理能力与规模化部署所需的核心特性。

- 🚀 仓库当前约有 19.9k Stars、2.1k Forks，采用 Apache-2.0 许可证。
- 🧠 支持的模型为 DeepSeek-V4.1-Flash。
- ⚙️ 核心能力包括优化算子、模型与采样器运行时、Attention DP 和均衡 CP、MoE EP+EPLB、异步调度、批不变推理、确定性采样、结构化输出等。
- 🔥 优化算子涵盖 FlashMLA、DeepGEMM、DeepEP、TileKernels、DeepSelect 及自定义 TileLang 算子。
- 🧩 DSpark 与置信度调度验证可加速解码；通过 `DEEPINFER_ENABLE_MTP_VARLEN=1` 启用，`DEEPINFER_USE_NEXTN_DECODE` 控制最大草稿长度，默认 5。
- 🪟 Decoder SWA 有界重放可减少预填充工作量；默认 V4.1 设置使用 `DEEPINFER_YOCO_PREFILL_TRUNCATION_MODE=compact` 和 `DEEPINFER_YOCO_PREFILL_KEEP_TOKENS=140`。
- 🔒 批不变推理通过 `DEEPINFER_BATCH_INVARIANT=1` 启用；确定性采样需同时设置 `DEEPINFER_BATCH_INVARIANT=1`、`DEEPINFER_ENABLE_MTP_VARLEN=0` 并传入固定 `seq_seed`，两者仅限 NVIDIA。
- 📐 结构化输出支持正则、JSON Schema、EBNF 语法约束，通过 `SamplingParams` 的 `so_args` 配置。
- 🖥️ 支持 NVIDIA SM100 GPU 和华为昇腾 950 NPU；环境要求 Linux、GCC>=13、Python 3.12、CUDA 13 或 CANN 9.2。
- 🏗️ 可从源码构建，设置 `DEEPINFER_ACCELERATOR=nvidia` 后运行 `./build.sh`，并通过 `examples/offline_inference.py` 进行离线推理。
- ⚠️ 完整推理服务还需要 KV Cache 系统、VE/Prefill/Decode 分离以及数据并行副本负载均衡，这些未包含在本次发布中。
- 🙏 项目最初主要基于 vLLM 构建，并受到 SGLang 和 TensorRT-LLM 启发。

---

### [GitHub - dbiswas55/vlmhub：一个轻量级、配置驱动的框架，用于在本地和云端后端统一进行视觉语言模型推理，基于 LiteLLM 和 Transformers 构建。 · GitHub](https://github.com/dbiswas55/vlmhub?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-768-october-22-2026)

**原文标题**: [GitHub - dbiswas55/vlmhub: A lightweight, config-driven framework for unified vision-language model inference across local and cloud backends, built on LiteLLM and Transformers. · GitHub](https://github.com/dbiswas55/vlmhub?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-768-october-22-2026)

vlmhub 是一个轻量、配置驱动的统一视觉语言模型推理框架，基于 LiteLLM 与 Transformers，让同一套代码在本地和云端后端运行交错文本与图像的多模态提示。

- 🧩 统一接口：通过 `Model.generate()` 处理 `TextBlock` 与 `ImageBlock`，无需为不同模型或后端重写推理代码。
- 🖼️ 多模态交错提示：文本和图像可按任意顺序混合，后端自动按需编码；API 后端使用 base64 data URI，Transformers 使用 PIL。
- 🗂️ 模型注册表：`models.json` 集中管理模型、托管设置和生成默认值，并支持为模型设置短名称映射真实 model id。
- 🖥️ 多后端支持：覆盖 Ollama、MLX-VLM、vLLM、HuggingFace Transformers、Gemini/Vertex AI、OpenAI、Anthropic 和 OpenRouter。
- ⚙️ 硬件感知 Transformers：支持可选 4-bit 量化加载和 `fallback_dtype`，适配 V100 等缺少原生 bfloat16 的 GPU。
- 🚀 安装方式灵活：可克隆仓库运行测试，也可作为子模块安装到自有项目；纯本地 Ollama 或 vLLM 环境无需云 API 密钥。
- 🧪 示例与测试：`tests/` 提供 VQA、图像描述、客户端端到端检查和 LLM judge 脚本，兼作冒烟测试与使用示例。
- 🎛️ 生成参数管理：参数按 defaults、hosting、model 层级解析，并支持单次调用覆盖；`None` 值不会发送给提供商。
- 🔌 易于扩展：多数新供应商只需在 `models.json` 中添加 LiteLLM 前缀托管；全新后端可继承 `BaseBackend` 并注册。
- 📦 本地模型管理：`local_models.py` 可列出、下载和删除 HuggingFace 缓存及 Ollama 模型；项目采用 MIT 许可证。

---

### [GitHub - chio-labs/sqlbuild：具备自定义编译时检查、端到端测试和安全重命名的 SQL 转换框架，可保留表历史记录。 · GitHub](https://github.com/chio-labs/sqlbuild?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-768-october-22-2026)

**原文标题**: [GitHub - chio-labs/sqlbuild: SQL transformation framework with custom compile-time checks, end-to-end testing and safe renames that keep your table history. · GitHub](https://github.com/chio-labs/sqlbuild?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-768-october-22-2026)

SQLBuild 是 chio-labs 推出的开源 SQL 转换框架，采用 Apache 2.0 许可，面向 SQL/Python 数据管道，强调在编译期发现问题、端到端测试以及安全重构，并将状态保存在用户自己的数据仓库中，无外部状态数据库、清单文件或付费版本。

- 🛠️ 提供编译期检查：解析引用、验证 SQL、推断列类型、检查 contracts、计算列血缘，全部离线完成。
- 📏 支持将团队规范写成内置或自定义 Python 规则，把评审意见转化为编译错误。
- 🧪 支持跨模型测试、宏/UDF/表函数测试、端到端场景测试，以及审计和数据 diff。
- 🔁 `sqb rename` / `sqb mv` 可更新所有引用，并迁移现有表而非重建，旧名称通过兼容视图继续可用。
- ⏱️ 通过 `replay_on_change` 可选择模型 SQL 变更后的重放范围，从仅新数据到全量重建。
- 📦 支持声明作用域，把宏、枚举和常量放在使用它们的模型附近，并用 `sqb scope` 预览移动影响。
- 🧹 内置 janitor 可在删除前归档过期表，降低清理风险。
- 📝 Recall 记录每次命令的语句、SQL、审计结果和精确输出，支持用 SQL 查询历史与实时状态。
- 🐍 Python loaders、任务、资产和检查可与 SQL 模型运行在同一图中。
- 🚀 快速开始：`pip install sqlbuild`，再用 `sqb playground waffle-shop` 在本地 DuckDB 体验，无需仓库凭据。
- 🗄️ Snowflake、DuckDB、MotherDuck、PostgreSQL 已支持；BigQuery、Databricks、SQL Server 处于 Beta。
- 🌟 项目免费且独立，无商业版或保留功能；GitHub 上约有 47 stars、2 forks，欢迎贡献。

---

### [](https://github.com/nautilusbits/retrokit?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-768-october-22-2026)

**原文标题**: [GitHub - nautilusbits/retrokit: Headless-Ghidra toolkit for reverse engineering 32-bit DOS and Win32 games (1993-2010): own LE/LX loader, Watcom calling conventions, library signatures, MCP server · GitHub](https://github.com/nautilusbits/retrokit?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-768-october-22-2026)

retro-kit 是面向 1993–2010 年 32 位 DOS/Win32 游戏的 headless Ghidra 逆向工具包，提供自研 LE/LX 加载器、Watcom 调用约定支持、库签名识别和 MCP 服务器，可将分析结果导出为可检索工作区，并支持命名回写与再导出。

- 🎯 主要用途：反编译 DOS LE/LX 与 Win32 PE 游戏，覆盖 DOS/4GW、DOS/32A、PMODE/W、CauseWay、DOS/4G bind、OS/2 LX、VxD 等格式。
- 🧩 核心能力：自带 LE/LX loader、Watcom 调用约定与编译器规格，支持函数、调用图、字符串、指针表、导入等索引。
- 📦 输出工作区：生成一个包含全部函数的大 `.c` 文件，以及 `functions.csv`、`calls.txt`、`strings.txt`、`fixups.txt`、`imports.txt` 等便于 grep 和分工的索引。
- 🛠️ 安装要求：需要 Ghidra 12.x、JDK 21+、Python 3.10+；可用 `pipx install` 安装，并用 `retrokit doctor` 检查环境。
- ⚙️ 常用命令：`info` 识别格式/扩展器/编译器/调用约定，`analyze` 跑完整流水线，`show` 查看函数，`tables` 查看指针与字符串表，`names` 应用命名，`reexport` 重新导出。
- 🤖 AI 代理支持：`retrokit mcp GAME_analysis` 提供 stdio MCP 服务器，可查询函数、反编译代码、调用图、交叉引用、字符串、指针表、反汇编、字节和库信息。
- 📚 库识别：`retrokit libs` 可从字符串、导入和数据文件识别约 20 个时代库，如 Miles/AIL、HMI SOS、DIGPAK、Smacker、Bink、FMOD、BASS、DirectX、zlib、libjpeg、libpng、PKWARE DCL、Lua 等。
- 🧭 LE/LX 流水线：按 fixup 目标创建函数，保留 switch 跳转表，修正错误的“无返回”标记，定义短字符串与字符串字面量，依据 `ADD ESP,n` 推断参数数量并自底向上恢复原型。
- 🪟 PE 流水线：使用 Ghidra PE loader 与自动分析，按指针表目标和填充区继续发现函数，执行字符串、参数和原型恢复，并支持 MSVC RTTI 类与 Rich header 编译器版本识别。
- 🧰 其他工具：`classes`、`libs`、`convert`、`sigs match|build|learn`、`entries`、`modules`、`strings`、`match`、`le`、`rnc`、`flic` 等命令覆盖类恢复、格式转换、签名匹配、字符串清单和资源处理。
- 🧪 测试方式：用 Open Watcom 构建小型合成程序，校验 loader、运行分析，并按 linker map 对函数地址、参数数量、调用参数、字符串字面量和反编译噪声评分。
- 📝 贡献要求：欢迎 issue/PR，但不要附带游戏文件或反编译游戏代码；应描述二进制格式、扩展器、编译器和问题，并尽量用 Open Watcom 小程序复现。
- 🧑‍💻 开发与许可：项目在维护者指导下大量使用 Claude Code 开发，提交中标注 Claude 为共同作者；采用 Apache 2.0 许可，不含游戏文件或反编译游戏代码，仅限用于自有软件。

---

### [](https://github.com/pacewisdomhq/TutorLoom?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-768-october-22-2026)

**原文标题**: [GitHub - pacewisdomhq/TutorLoom: Self-hosted, multi-tenant learning management system (LMS) for training institutes and teams: course builder, trainer and student portals, progress tracking. Django + React. Apache-2.0. · GitHub](https://github.com/pacewisdomhq/TutorLoom?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-768-october-22-2026)

TutorLoom 是一个免费、自托管、多租户的学习管理系统，面向培训机构和团队，提供课程构建、讲师与学生门户、学习进度跟踪，并支持 Web、Android 和 iOS。项目采用 Django + React + Flutter 技术栈，以 Apache-2.0 许可证开源。

- 🏢 **多租户架构**：一次部署可服务多个组织，所有查询按组织隔离，确保数据仅对所属成员可见。
- 🧱 **结构化课程构建**：课程按层级、章节和步骤组织，支持视频、文档、任务、测验、先修条件和顺序解锁。
- 👥 **批次与批量导入**：可将学习者分组到限时批次中，并通过 CSV/Excel 批量邀请讲师和学生。
- ✅ **评分与反馈**：讲师可在统一队列中审核提交，按分数和文字反馈批准或拒绝，并导出进度到 Excel。
- 🗺️ **学习路线图**：学生可在 Web 或移动端按步骤学习，跟踪完成情况，并获得积分和等级。
- 🔌 **API 优先**：提供带 JWT 认证的 REST API，以及 OpenAPI 3、Swagger UI 和 ReDoc 文档，支持 Web、移动端和自定义集成。
- 👤 **角色与门户**：包括机构管理员、讲师、学生；企业版还提供超级管理员和外部候选人等角色，一个账号可拥有多个角色并切换门户。
- 📦 **社区版与企业版**：社区版免费开源且可自托管；企业版增加 Google/Microsoft 登录、AI 编程题、课程导入导出、评估、超级管理员控制台、排行榜、徽章等高级模块。
- 🧰 **技术栈**：后端使用 Python 3.13、Django 6、Django REST Framework、Celery、PostgreSQL、Redis；前端使用 React 19、TypeScript、Vite、Tailwind CSS 4；移动端使用 Flutter。
- 🚀 **快速启动**：推荐使用 Docker Compose 启动 Postgres、Redis、Django API、Celery Worker 和 Web 前端；默认前端地址为 `http://localhost:5173`，API 文档为 `http://localhost:8010/api/docs/`。
- ⚙️ **配置与部署**：通过环境变量或 `.env` 配置数据库、Redis、邮件、S3 等；生产环境应使用 Gunicorn、设置 `DEBUG=False`、强 `SECRET_KEY`、明确允许主机和 CSRF 来源，并单独部署前端静态构建。
- 🧪 **测试支持**：后端使用 pytest、pytest-django 和覆盖率工具；前端使用 Vitest 与 ESLint；移动端使用 `flutter test`。
- 🧭 **路线图**：计划包括主数据管理、培训周期模板、系统设置、跨组织报表、通知广播、AI 辅导与反馈、SCORM/xAPI、防作弊、合规追踪、白标、SSO/SCIM、多语言等。
- 🤝 **开源协作**：欢迎社区贡献，需遵循贡献指南和行为准则，保持查询按组织隔离，随模型变更提交迁移，并确保测试通过。
- 📄 **许可证与维护**：基于 Apache License 2.0 开源，由 Pace Wisdom Solutions 构建和维护。

---

### [使用 Python 进行空间分析 🌎 + 闪电演讲 ⚡️，2026年10月27日星期二下午6:30 | Meetup](https://www.meetup.com/pydatanyc/events/316912352/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-768-october-22-2026)

**原文标题**: [Spatial Analytics with Python 🌎 + Lightning Talks ⚡️, Tue, Oct 27, 2026, 6:30 PM   | Meetup](https://www.meetup.com/pydatanyc/events/316912352/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-768-october-22-2026)

本次活动由 PyData NYC 与 Rinchen L. 等主办，聚焦 Python 地理空间数据分析，包含 xarray-spatial 主题演讲、社区闪电演讲和社交环节，适合 GIS 从业者、数据科学家、Python 开发者及初学者参加。

- 🌎 活动主题：Spatial Analytics with Python + Lightning Talks，探索 Python 地理空间数据科学。
- 🗓️ 时间：10 月 27 日（周二）18:30–20:30 EDT；18:00 开门，19:00 停止入场。
- 📍 地点：纽约 CUNY Graduate Center，365 5th Ave, New York, NY 10016。
- 🎤 主讲人：Brendan Collins，Makepath 创始人兼 CTO、Xarray-Spatial 创建者。
- 🧭 主题演讲：介绍开源库 xarray-spatial 的可扩展栅格分析，以及 CPU/GPU 加速能力。
- 🗺️ 内容涵盖：将空间数据带入 Xarray、地形/水文/邻近分析等算法、分区统计与多边形化。
- ⚡ 社区环节：包含一轮社区闪电演讲，并讨论开源贡献、代码质量与 AI 辅助开发等经验。
- 🤝 社交机会：与数据爱好者、Python 开发者、研究者和社区领袖交流合作。
- 🍕 餐饮与设备：Makepath 赞助披萨和饮料；建议携带笔记本电脑跟随演示。
- 🪪 报名要求：使用政府签发的正式姓名注册，并携带政府签发的照片身份证件签到。
- 👶 参与门槛：活动面向所有水平，欢迎新人和初学者；所有 NumFOCUS 相关活动均遵循行为准则。

---

### [PyData 诺里奇](https://www.meetup.com/pydata-norwich/events/316977289/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-768-october-22-2026)

**原文标题**: [PyData Norwich - October Meetup, Mon, Oct 26, 2026, 6:00 PM   | Meetup](https://www.meetup.com/pydata-norwich/events/316977289/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-768-october-22-2026)

本次活动是 PyData Norwich 十月聚会，由 Chris J. 与 PyData Norwich 主办，聚焦 Python 与数据科学交流。活动形式轻松，适合各水平参与者，包含演讲、问答、免费披萨饮料，并在会后前往酒吧继续交流。

- 📅 时间：10 月 26 日星期一，18:00–20:00 GMT
- 📍 地点：Artlist，27 St Giles St, Norwich NR2 1JN，按 4 号门铃
- 🎤 演讲：Ruben Galvao（Artlist）带来《A Deep Seek into LLM Architecture》
- 🧠 内容：从单个神经元逐步讲到现代大语言模型架构、网络学习方式、模型扩展，以及 DeepSeek 等最新进展
- 🍕 安排：18:00 开门并提供免费披萨和饮料，18:15 开始演讲
- 🍻 会后：19:15 起可前往 Coach and Horses Pub（NR1 1BA）继续交流
- 🤝 氛围：非正式活动，欢迎所有技能水平者参与提问与讨论
- 📜 规范：活动遵循 NumFOCUS 行为准则

---

### [](https://www.meetup.com/pydata-warsaw/events/316948141/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-768-october-22-2026)

**原文标题**: [PyData Warsaw #35 - Piotr Szwed & Mikołaj Roszczyk, Tue, Oct 27, 2026, 6:00 PM   | Meetup](https://www.meetup.com/pydata-warsaw/events/316948141/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-768-october-22-2026)

PyData Warsaw #35 将于10月27日（周二）18:00–20:00 CET 在华沙 ING Hubs Poland 举行，由 Mikołaj R. 与 Rafał M. 主持，ING 赞助场地。活动包含两场演讲，分别聚焦企业多智能体 AI 平台参考架构与多源信息融合方法选择，并设有会前交流聊天。

- 📅 活动时间为10月27日周二18:00–20:00 CET，特别提醒是周二而非周三。
- 📍 地点为 ING Hubs Poland，地址：ul. Pańska 97, Warszawa。
- 🎙️ 18:00 由 Piotr Szwed 主讲“Autonomous Enterprise: Reference Architecture for Multi-Agent AI Platforms”。
- 🧩 该演讲介绍开放、模块化的企业多智能体平台参考架构，提供可加速 AI Agent 部署的生产级蓝图，并强调成本透明与自主行动可审计。
- 🚀 对技术团队提供工程路线图，对 IT 领导层提供安全扩展 AI、将实验转化为合规资产并明确 ROI 的策略。
- 👤 Piotr Szwed 拥有20多年 Cloud Native、SRE、DevOps、平台工程与 Agentic Engineering 经验，是 CNCF 成员和社区组织者，关注可扩展 AI 平台与 Agentic 生态。
- 🕕 18:45 由 Mikołaj Roszczyk 主讲“Choosing the right method for Multi-Source Information Fusion”。
- 🧠 该演讲讨论基于多异构数据源的自主决策，介绍投票方法、贝叶斯推断、Dempster-Shafer 证据理论等多源信息融合方法，并展示用于评估的原创框架。
- 👤 Mikołaj Roszczyk 是 PyData Warsaw 组织者、Intel AI Software Engineer，也是华沙理工大学计算机科学研究学者。
- 🏢 活动由 ING 提供场地并赞助；页面另列 Continuum Analytics 为创始赞助、Centrum Innowacji PW 等支持信息。
- 💬 参会者可在活动开始前加入活动聊天，与其他参会者连接交流。

---

### [PyData 三城 #46，2026年10月28日星期三下午6:00 | Meetup](https://www.meetup.com/pydata-trojmiasto/events/316944967/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-768-october-22-2026)

**原文标题**: [PyData Trójmiasto #46, Wed, Oct 28, 2026, 6:00 PM   | Meetup](https://www.meetup.com/pydata-trojmiasto/events/316944967/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-768-october-22-2026)

PyData Trójmiasto 第46期活动将于10月28日（周三）18:00–20:00（CET）在格丁尼亚 Nordea Tensor Z（Łużycka 8b）举行，围绕 Databricks 平台与企业级 AI 展开两场演讲，并设有披萨与交流环节。

- 📅 **活动信息**：由 Łukasz G. 和 Adrian B. 主办，地点为格丁尼亚 Tensor Z 大楼，活动页面提供聊天区供参会者提前交流。
- 🎟️ **报名与入场**：需用完整姓名注册，入场时携带身份证件；RSVP 截止活动前一天18:00。
- 🅿️ **停车与联系**：楼旁街道有免费停车位；紧急沟通可联系 kontakt@pydata-trojmiasto.pl。
- 🗓️ **议程安排**：18:00–18:05 入场，18:05–18:10 PyData 简介，18:10–18:55 第一场演讲，19:00–19:45 第二场演讲，19:45 披萨与社交。
- 🚀 **演讲一**：Łukasz Wybieralski 讲“One Platform to Rule Them All”，聚焦 Databricks 常见架构、治理与成本控制陷阱，并基于7个真实项目给出最佳实践。
- 🛠️ **现场演示**：将使用 Cursor 与 Databricks MCP Server 快速搭建可运行的数据平台，帮助听众形成平台全景图、避坑清单和更高效的工作流。
- 👨💻 **讲者一**：Łukasz Wybieralski 是 Dateonic 的 CTO，长期关注业务与技术结合，目前专注 Databricks 和客户数据平台建设。
- 🤖 **演讲二**：Rafał Korszuń 讲“AI in the Enterprise: From harness to governance”，讨论企业 AI 在成本、安全、合规方面与初创公司的差异。
- 🧭 **企业 AI 要点**：强调模型外围的 harness、内部 AI 工具市场、模型与任务匹配、代码图谱/CPU embeddings/Spec-Driven Development，以及“治理内置”的 human-in-the-loop、硬性停止和 AI Act。
- 👨🔬 **讲者二**：Rafał Korszuń 有20多年软件经验，任职 JIT Team，创办 Kleder，帮助企业把 AI 落到生产环境，并在 Twitch 分享编程知识。
- 🍕 **赞助与主题**：NumFOCUS/PyData license 为赞助方，Dateonic 团队赞助本场披萨；相关主题包括 AI、深度学习、机器学习、大数据与 Python。

---

### [相关性与因果性：为什么重要？，2026年10月28日星期三下午6:00 | Meetup](https://www.meetup.com/pydata-bradford/events/316888579/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-768-october-22-2026)

**原文标题**: [Correlation vs Causation: Why Does It Matter?, Wed, Oct 28, 2026, 6:00 PM   | Meetup](https://www.meetup.com/pydata-bradford/events/316888579/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-768-october-22-2026)

本次线上活动由 PyData Bradford 主办，Elizabeth O. 与 pydatabradford 组织，Joshua Amayo 主讲，聚焦“相关性与因果性”的区别，以及这一区别对数据驱动商业决策的重要性。

- 📅 活动主题：Correlation vs Causation: Why Does It Matter?，探讨“相关不等于因果”。
- 🎙️ 主讲与主办：Joshua Amayo 主讲；PyData Bradford 主办，Elizabeth O. 和 pydatabradford 组织。
- 💻 活动形式：线上活动，参会者可加入活动聊天并与其他参会者交流。
- 🧠 核心内容：讲解相关性与因果性的区别，以及仅基于相关性的分析在解决商业问题时的局限。
- 🛠️ 方法应用：介绍因果分析技术及其在商业场景中的应用。
- 📈 决策价值：培养因果分析能力，有助于提出更好的问题并做出更明智的决策。
- 👥 适合人群：数据从业者，以及希望理解数据如何影响商业决策的人。

---

### [](https://www.meetup.com/pydata-calgary/events/317077367/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-768-october-22-2026)

**原文标题**: [2026-10 Call me Ahab: Webscraping tooling, approaches and dataset obsession, Wed, Oct 28, 2026, 5:30 PM   | Meetup](https://www.meetup.com/pydata-calgary/events/317077367/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-768-october-22-2026)

本次活动是 PyData Calgary 主办的线下技术分享，主题为“Call me Ahab: Webscraping tooling, approaches and dataset obsession”，聚焦网络爬虫的工具、架构、规模化挑战与数据集执念；活动于 2026 年 10 月 28 日 17:30–19:30（MDT）在卡尔加里 Platform Calgary 举行，由 NumFocus 赞助。

- 🐋 演讲主题：网络爬虫并非单一技术或单一目的，而是覆盖多种工具、方法与动机的广阔领域。
- ⚙️ 案例跨度：从每分钟轮询 API 的爬虫，到持续运行多年、维护完整镜像的爬虫集群。
- 💰 核心权衡：无边界的数据需求会带来时间、精力、资金与风险等无边界成本。
- 🧭 内容重点：涵盖爬虫库与架构选择、Agentic 与机器学习工具的适用场景，以及规模化陷阱。
- 📉 现实挑战：互联网提供的机会很广，但抓取难度逐年上升，需要更系统的策略。
- 🎤 讲者背景：Michael Moores 是顾问与网络安全教育者，曾任高级解决方案工程师，经历横跨风险、网络安全、产品与数据领域。
- 🍕 活动安排：17:30 披萨与交流，18:00 演讲与讨论，19:30 结束。
- 📍 地点与主办：Platform Calgary East Annex；PyData Calgary 主办，Graham D. 等人组织，NumFocus 赞助。

---

