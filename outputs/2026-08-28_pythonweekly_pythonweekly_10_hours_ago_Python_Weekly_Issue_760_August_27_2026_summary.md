### [](https://yassa9.github.io/osint/gralhix-004/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-760-august-27-2026)

**原文标题**: [gralhix #004](https://yassa9.github.io/osint/gralhix-004/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-760-august-27-2026)

本文描述作者用数学与编程方法而非 Google Lens 解决 Gralhix #004 地理定位挑战：通过分析照片中三个岛屿的几何关系构建“指纹”，结合全球海岸线数据、CUDA GPU 并行计算及多种地理空间过滤，最终定位到密克罗尼西亚的 Oan 岛，并回答度假村名称、坐标与拍摄朝向。

- 🖼️ 挑战内容：给出一张度假村岛屿照片，需回答度假村名称、岛屿坐标、相机拍摄朝向；作者选择用数学和程序化方式求解。
- 📄 元数据检查：使用 exiftool 查看图片，仅得到 WebP 格式与尺寸，无地理位置等可用信息。
- 📐 构建几何指纹：通过点击 GUI 标记照片中三个陆地块（P0 主岛、P1 右侧岛、P2 左前带山岛屿），计算三角形角度与距离比，并允许 ±20% 容差。
- 🌍 全球候选数据：使用 OpenStreetMap 的 land-polygons-split-4326 全球陆地多边形数据（882MB）作为搜索空间。
- 🔍 热带纬度过滤：仅保留纬度 -30° 到 30° 之间的陆块，剩余 141,131 个多边形。
- 🏝️ 局部密度过滤：若某点 5km 内邻域中心点超过 10 个，则视为拥挤群岛或海岸，剔除后剩 51,576 个候选。
- 🗺️ 聚类筛选：要求 20km 范围内至少有 3 个点组成簇，得到 23,500 个潜在簇。
- 🔢 生成三元组：对每个簇内点进行组合，簇内点数上限 60，并按面积分层抽样，共产生 80,690,777 个候选三角形。
- ⚡ GPU 并行匹配：每个三角形分配一个 CUDA 线程，在 RTX 3050 上耗时 204ms；按面积选出最小岛 P0，用叉积符号判断 P1/P2 方向，匹配角度与距离比后，158,784 个三角形通过。
- 🧹 去重处理：同一物理三角形可能被多个簇重复计算，去重后剩 8,915 个唯一组合。
- 📏 开放矩形检查：在 P0→P1 边、P2 反侧构建矩形，若矩形内出现其他陆地则剔除，剩 948 个候选。
- 🪸 珊瑚礁形状检查：P0 的 Polsby-Popper 紧凑度需 ≥0.5，且 1.5km 内至少有一个小于 0.05km² 的微型沙洲，剩 213 个。
- 🥚 椭圆形状检查：P0 最小外接矩形长宽比需在 1.05~2.2 之间，填充率不低于 0.589（理想椭圆填充率 π/4 的 75%），剩 137 个。
- 🌿 NDVI 植被检查：通过公共 STAC API 获取 Sentinel-2 影像，计算 NDVI ≥ 0.6，确认主岛有茂密植被而非裸沙，剩 66 个。
- ⛰️ 高程与山体检查：P0 海拔需 ≤50m，且相机朝向 ±50°、2~20km 扇形范围内存在 100~500m 的高地，最终剩 26 个候选。
- 🗺️ 人工目视确认：生成包含国家名和 Google Maps 链接的 HTML 报告，逐一排查后锁定密克罗尼西亚的 Oan 岛。
- 📍 最终答案：度假村名称为 Oan；岛屿坐标为 7°21′48.4″N, 151°45′20.7″E（7.363444, 151.755750）；拍摄朝向为西北（NW），方位角约 324.97°。
- 📜 数据与许可：使用 OpenStreetMap（ODbL）、Copernicus DEM GLO-30、Sentinel-2 Earth Search、Natural Earth 等公开数据，并注明相应许可协议。

---

### [](https://nathancooper.io/blog/2026-08-10-ipython-is-all-you-need?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-760-august-27-2026)

**原文标题**: [Nathan Cooper - IPython is All You Need](https://nathancooper.io/blog/2026-08-10-ipython-is-all-you-need?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-760-august-27-2026)

本文介绍如何将 IPython 打造成一个功能强大且智能的终端 shell：通过扩展免去 `!` 前缀执行 bash 命令、在终端内显示图片，并集成 AI 助手使其能结合会话历史回答问题、安全地执行代码。

- 🐚 作者坚持用 IPython 完全替代传统 shell，并认为这是更高效的“唯一活法”。
- ⚡ 使用 `%rehashx` 魔法，让 `PATH` 中的命令自动获得 IPython 别名，从而无需 `!` 即可运行 bash 命令。
- 🖼️ 借助 Kitty Terminal Graphics Protocol 和 `ipythonng` 扩展，终端可直接渲染 matplotlib 图像和富文本输出。
- 🤖 集成 FastLLM 打造智能 IPython shell，AI 能读取 `In`/`Out` 及 `history_manager` 记录的代码、输出、图像和异常作为上下文。
- ✨ 通过自定义输入转换器，支持 `:query` 快捷指令向 AI 提问，AI 甚至能看到 `!` 命令的伪终端输出。
- 🛡️ 使用 `safecmd` 和 `safepyrun` 提供安全执行能力，通过 allowlist 阻止 `rm -fr /` 等危险操作，并封装成 AI 可调用的工具。
- 📦 文章最后推荐 `ipyai` 库，将这些能力封装成完整的智能 IPython shell 方案。

---

### [](https://huggingface.co/blog/train-multi-vector-encoder?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-760-august-27-2026)

**原文标题**: [Training and Finetuning Multi-Vector Embedding Models with Sentence Transformers](https://huggingface.co/blog/train-multi-vector-encoder?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-760-august-27-2026)

本文介绍了如何使用 Sentence Transformers 库对多向量（ColBERT 风格）嵌入模型进行训练与微调，涵盖模型选择、数据准备、损失函数、训练参数、评估方法与索引优化，并展示了在医学检索数据集上微调后的模型显著超越通用检索模型的效果。

- 📌 多向量模型为每个 token 生成一个向量，通过 MaxSim 逐 token 匹配打分，比单向量模型保留更细粒度信息，检索更强但索引更大。
- 🎯 微调能显著提升特定领域检索性能；许多公开模型截断长文档（如 180–512 token），在平均 941 token 的医学段落上可损失高达 0.24 NDCG@10。
- 🧠 模型起点选择很关键：无监督检查点（如 mLateOn-unsupervised）比已监督微调完成的检查点更适合领域自适应，从头构建时可在强骨干上新增随机投影层。
- 📂 训练数据可使用 Hugging Face Hub 数据集或本地 CSV/JSON 等，格式需与损失函数匹配；最简单的是（查询，相关段落）配对数据。
- ⚖️ 常用损失为 CachedMultiVectorMultipleNegativesRankingLoss，通过 GradCache 在有限显存下实现大批量对比学习，且不损失质量。
- ⚙️ 训练参数中，提示词需显式映射到训练列，建议取消长度截断以匹配推理，学习率 1e-4 在实验中效果最佳。
- 📊 评估使用 MultiVectorInformationRetrievalEvaluator，需加入干扰段落避免评估饱和；微调模型在 20 万段落语料上 NDCG@10 达 0.9139，领先最强零样本模型 0.062。
- 🏆 微调模型在 rank-1 准确率 84.9%，远超最强零样本多向量模型（75.8%），且训练仅需单张 RTX 3090 上 14.5 小时。
- 🗂️ 支持多数据集联合训练，可通过 MultiDatasetBatchSamplers 控制采样策略，并可对不同数据集使用不同损失函数与回调（W&B、TensorBoard、CodeCarbon）。
- 💾 索引优化：词元池化可将向量数减半仅损失 0.0033 NDCG@10；配合 1-bit PLAID 量化与剪枝，索引从 45 GB 降至 1.45 GB，同时仍高于 8B 稠密模型的精度。

---

### [](https://www.better-simple.com/django/2026/08/19/nifty-feature-counting-on-multiple-columns/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-760-august-27-2026)

**原文标题**: [
    
      Nifty Django Feature: Counting on Multiple Columns · Better Simple
    
  ](https://www.better-simple.com/django/2026/08/19/nifty-feature-counting-on-multiple-columns/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-760-august-27-2026)

本文章介紹了 Django ORM 中一個實用的擴充功能：如何透過自訂 `Subquery` 來對多個欄位進行計數，解決 `Count` 只能針對單一欄位計數的限制，並展示 Django expression 系統的靈活性。

- 🐕 問題情境：想計算每位獸醫看過多少「寵物-獸醫」唯一配對，但 `Count` 只能對單一欄位計數，無法直接統計多欄位組合。
- ❌ 現有方式不足：分別對 `appointment` 或 `vet` 計數會得到 4 與 2，無法得到唯一配對數 3。
- 🛠️ 自訂 `CountSubquery`：繼承 `Subquery`，設定 `template` 為 `(SELECT COUNT(*) FROM (%(subquery)s) _count)`，並以 `IntegerField` 作為輸出型別。
- ✨ 實作方式：內層查詢利用 `values('pet', 'vet').distinct()` 產生唯一配對，外層 `COUNT(*)` 計算列數，成功得到 `count_pairs = 3`。
- 🔧 重點價值：Django expression 系統允許透過 `template` 靈活控制 SQL 渲染，讓開發者不需撰寫原始 SQL 即可擴充 ORM 功能。
- 📚 延伸資源：官方文件提供 `Func()`、自訂 Aggregate、`Subquery()` 與自訂 Query Expression 等進階指引，方便進一步學習。

---

### [](https://www.youtube.com/watch?v=cAtKtvmds1o&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-760-august-27-2026)

**原文标题**: [How I Set Up Python for Machine Learning With AI - YouTube](https://www.youtube.com/watch?v=cAtKtvmds1o&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-760-august-27-2026)

overview summary
- 📋 提供網站簡介與新聞中心資訊
- ©️ 說明版權與聯絡方式
- 🎨 面向創作者與廣告刊登服務
- 🛠️ 提供開發人員資源與條款
- 🔒 涵蓋私隱、政策與安全規範
- ▶️ 解釋YouTube運作方式與新功能測試
- 🗓️ 標示© 2026 Google LLC版權所有

---

### [](https://blog.jupyter.org/jupytergis-0-16-new-visualization-capabilities-collaborative-story-maps-and-more-03e6b78bacc0?gi=a55cbf12cc54&utm_campaign=python-weekly-issue-760-august-27-2026&utm_medium=newsletter&utm_source=www.pythonweekly.com)

**原文标题**: [Medium](https://blog.jupyter.org/jupytergis-0-16-new-visualization-capabilities-collaborative-story-maps-and-more-03e6b78bacc0?gi=a55cbf12cc54&utm_campaign=python-weekly-issue-760-august-27-2026&utm_medium=newsletter&utm_source=www.pythonweekly.com)

JupyterGIS 0.16 版本发布，重点强化地理空间可视化、协同编辑能力，新增 Story Maps 重新设计、openEO 图层支持、Xarray 懒加载、更灵活的符号模型、GeoZarr/GeoPackage 格式、R API 及多项协作改进。

- 🗺️ 发布 JupyterGIS 0.16，带来全新的可视化与协作地理空间工作流。
- 📖 Story Maps 全面改版：通过滚动式分段组合 Markdown 与地图状态，让地图随叙事改变位置、图层与样式。
- ✏️ Story Map 编辑器大幅升级：支持多人实时协同编辑、Markdown 即时预览和整篇 Story Map 预览模式，更适合长文内容。
- 🛰️ 新增 openEO 图层支持：可将远程处理流程直接显示为地图图层，采用基于瓦片的懒加载，无需下载完整数据集。
- 🧩 内置图形化 openEO 流程编辑器：支持拖拽节点、连接后端、直接编辑 JSON，也便于 LLM 辅助生成流程。
- 📦 集成 jupyter-tiler：可直接在 JupyterGIS 中懒加载可视化 Xarray 数据集，支持超大数据的流畅浏览。
- 🎨 引入受 Grammar of Graphics 启发的新符号模型：灵活组合颜色、大小、透明度等属性，制作更丰富的专题地图。
- 🗃️ 新增 GeoZarr 与 GeoPackage 格式支持，提升云原生多维数据与现有 GIS 软件的互操作性。
- 🤝 矢量图层支持协作编辑：多人可同时创建、移动、修改要素，并实时同步变更。
- 🇷 发布新的 R API（r-jupytergis）：R 用户可通过 GISDocument 使用与 Python 相同的交互式地图和协作基础设施。
- 🐛 包含大量 Bug 修复与性能优化，并持续完善用户界面和 Python API。
- 🚀 获得欧洲空间局（ESA）与法国国家空间研究中心（CNES）资助，并由 QuantStack 及多位贡献者共同完成。

---

### [获取失败](https://machinelearningmastery.com/learn-vectorized-thinking-in-python-through-examples/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-760-august-27-2026)

**原文标题**: [Failed to retrieve](https://machinelearningmastery.com/learn-vectorized-thinking-in-python-through-examples/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-760-august-27-2026)

无法总结：获取内容失败，状态码 403。

---

### [](https://alexzhang13.github.io/blog/2026/spec-ptc/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-760-august-27-2026)

**原文标题**: [
  
  
    
      Speculative Programmatic Tool Calling | Alex L. Zhang
    
  
](https://alexzhang13.github.io/blog/2026/spec-ptc/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-760-august-27-2026)

sPTC（推测式程序化工具调用）是一种针对代码型代理（如 RLM）的优化技术，在代码流式生成过程中提前推测并异步启动工具调用，从而与主生成过程重叠，减少高延迟工具和阻塞式 REPL 调用带来的等待时间，实测可带来约 1–1.2 倍的速度提升。

- 🧠 核心动机：作者认为代码 REPL 是唯一需要的“工具”，因此有必要在生成代码时重叠工具调用与代码生成/执行。
- ⚙️ 核心机制：受 CPU 推测执行和 LLM 推测解码启发，在模型仍在生成 token 时，从部分 REPL 代码中解析并预启动工具调用，缓存结果供真实调用使用。
- ⏱️ 两大提速点：一是将已生成的工具调用与 token 流式传输重叠；二是充当简单 JIT 编译器，把彼此独立但写为阻塞的调用并行化。
- 📊 实验效果：在 OOLONG 数据集、Qwen3-30B-A3B 模型上，RLM 速度提升约 1–1.2 倍，具体收益取决于工具延迟、生成 token 数和引擎负载。
- 🔧 实现方式：通过装饰器标记可推测工具，在解析时异步调用并注册 promise，实际执行时若命中缓存则直接复用结果。
- 🌑 影子 REPL：维护一个深拷贝的 shadow REPL 来安全执行部分代码，并将外部库或 `open` 等有副作用函数标记为不安全，避免推测污染真实状态。
- ✅ 可推测情况：字面量输入、纯函数依赖、可安全计算的变量依赖均可推测；条件未知或有副作用依赖的调用会被阻止。
- 📈 开销与风险：运行时开销可忽略，但过度推测可能堵塞工具服务队列，需要控制推测力度。
- 📚 相关研究：对比 Conveyor、Speculative Interaction Agents 和 AsyncFC，sPTC 因程序本身运行时间未知，有更多重叠空间。
- 🚀 未来方向：希望发展更聪明的 JIT 编译技巧，并推广到多语言、多框架；当前代码已开源在 GitHub。

---

### [面向LLM的强化学习：完全指南](https://cameronrwolfe.substack.com/p/llm-rl?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-760-august-27-2026)

**原文标题**: [Reinforcement Learning for LLMs: The Complete Guide](https://cameronrwolfe.substack.com/p/llm-rl?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-760-august-27-2026)

overview summary
本文全面梳理了大型语言模型（LLM）强化学习（RL）的完整知识体系，从RL基本概念出发，逐步讲解策略梯度算法的演进（VPG、REINFORCE、PPO、GRPO及其改进变体），并深入探讨在线/离线RL、持续学习、rubric奖励、RL缩放定律和Agentic RL等前沿研究主题，为理解现代LLM RL训练提供了清晰的框架与关键洞察。

- 📘 RL基础框架：智能体在环境中通过策略采取动作、获得奖励并更新状态；轨迹由状态、动作、奖励序列组成，目标是最大化期望累积回报（可带折扣因子）。
- 🧠 核心函数与估计：价值函数V(s)、动作价值函数Q(s,a)和优势函数A(s,a)=Q(s,a)-V(s)；实际中常通过蒙特卡洛采样、critic网络等方式估计这些量。
- 🎯 LLM中的RL建模：策略即LLM本身，初始状态为提示，状态为提示+已生成token；动作可视为单个token（MDP）或整个补全（bandit），奖励可分为结果奖励（outcome）和过程奖励（process）。
- ⚖️ 奖励来源与正则化：RLHF使用偏好奖励模型，RLVR使用规则/确定性验证器（如数学答案匹配、代码测试）；KL散度用于限制策略偏离参考模型，常见k1和k3估计器。
- 🔄 重要性采样：用于修正行为策略与目标策略分布不匹配，如PPO中的重要性比率；截断或裁剪可降低方差、提升稳定性。
- 📈 Vanilla Policy Gradient (VPG)：基础策略梯度，通过增大高回报动作的概率、降低低回报动作概率来优化；几乎所有后续算法都沿用其“log概率梯度×学习信号”的结构。
- 🔁 REINFORCE：VPG的蒙特卡洛实现，使用基线（如批次平均奖励）降低方差；RLOO等变体通过同提示多个补全构造留一基线，进一步改进。
- 🏗️ PPO（近端策略优化）：引入critic估计优势函数，通过重要性比率+裁剪限制策略更新幅度，支持多轮更新，并常配合GAE进行优势估计；训练需维护策略、参考策略、critic和奖励模型，开销较大。
- 🪶 GRPO（组相对策略优化）：去除critic，通过每个提示采样一组补全，用组内奖励均值/标准差计算优势，显著降低内存和计算开销；采用PPO式裁剪并保留KL惩罚。
- 🛠️ GRPO的改进变体：GSPO使用序列级重要性比率；DAPO提出解耦裁剪、动态采样与token级损失聚合；Dr. GRPO修正长度偏差和难度偏差；TIS纠正训练与推理引擎分布不匹配；CISPO使用停梯度裁剪权重，确保稀有“分叉”token贡献梯度。
- 🔄 在线与离线RL：在线RL（PPO、GRPO）持续生成on-policy数据，通常性能更优；离线方法（如DPO）训练固定数据集，但可通过半在线刷新数据部分恢复性能。
- 🧠 持续学习与RL：在线RL对灾难性遗忘更鲁棒，因训练数据来自模型自身，分布偏移小；SFT则容易遗忘旧任务。
- 📋 基于rubric的奖励：对于非可验证的开放任务，可构建提示特定的质量标准清单，由LLM judge逐项评分并聚合为奖励，降低reward hacking风险。
- 📉 RL缩放定律：RL性能随计算量扩展确实存在一定规律，但比预训练更“杂乱”，依赖于模型、数据和训练方案；可通过增大batch、数据复用、增加rollout计算等方式扩展。
- 🤖 Agentic RL：涉及多轮生成与环境交互，需要模块化工具接口、掩码环境token、过程奖励、异步基础设施和规模化环境编排，是快速演进的前沿领域。
- 🏁 总结与展望：从VPG到GRPO及其变体，核心是降低方差、稳定更新、提升效率；RL仍围绕数据、奖励、缩放、持续学习、长程推理和智能体等开放问题不断演进。

---

### [](https://www.youtube.com/playlist?list=PLd3Y9yzyC5Uo&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-760-august-27-2026)

**原文标题**: [EuroPython 2026 - YouTube](https://www.youtube.com/playlist?list=PLd3Y9yzyC5Uo&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-760-august-27-2026)

overview summary  
- 📺 頁面為 YouTube 的標準頁腳資訊，包含新聞中心、版權、聯絡方式、創作者資源與開發人員選項。  
- 🔒 提供條款、私隱政策、安全政策及 YouTube 運作方式的說明，並包含測試新功能的入口。  
- 📅 標示為 EuroPython 2026 的相關內容，版權歸 Google LLC 所有，年份為 2026。

---

### [](https://www.caktusgroup.com/blog/2026/08/21/fuzzy-string-matching-django-postgresql/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-760-august-27-2026)

**原文标题**: [Fuzzy String Matching in Django and PostgreSQL | Caktus Group](https://www.caktusgroup.com/blog/2026/08/21/fuzzy-string-matching-django-postgresql/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-760-august-27-2026)

通過 Django ORM 在 PostgreSQL 中進行模糊字串匹配，本文介紹 Soundex、Daitch-Mokotoff、Levenshtein 與 Trigrams 等工具、使用範例及對應索引。

- 🔧 前置需求：啟用 `fuzzystrmatch` 與 `pg_trgm` 擴充，且需先建立擴充再建立索引。
- 📇 Soundex：以自訂 `Func` 包裝 `soundex()`，產生 4 字元語音碼，適合英文發音匹配，例如 Smith/Smyth。
- 🌍 Daitch-Mokotoff：包裝 `daitch_mokotoff()` 回傳語音碼陣列，用 `__overlap` 匹配，對德語、斯拉夫語等更佳。
- ✂️ Levenshtein：使用 `levenshtein_less_equal()` 計算編輯距離，需注意大小寫，且無法用索引預先加速。
- 🔤 Trigrams：Django 內建 `TrigramSimilarity` / `TrigramDistance`，可做相似度排名與最近鄰居搜尋。
- 🗂️ 索引建議：Soundex 用 B-tree、Daitch-Mokotoff 用 GIN、Trigram 用 GiST，前綴搜尋則用 `text_pattern_ops`。
- ⚠️ 重要提醒：功能索引必須與查詢表達式完全一致，否則 PostgreSQL 不會使用索引，可能導致全表掃描。

---

### [](https://www.youtube.com/playlist?list=PLKZM1caSP1-I&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-760-august-27-2026)

**原文标题**: [PyData & PyCon Yerevan 2026 - YouTube](https://www.youtube.com/playlist?list=PLKZM1caSP1-I&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-760-august-27-2026)

overview summary  
這是 YouTube 頁面底部資訊與 PyData & PyCon Yerevan 2026 活動內容的混合呈現，涵蓋平台基本連結、版權資訊及年度會議宣傳。

- 📰 提供新聞中心、版權聲明及聯絡方式等基本網站資訊  
- 👥 列出創作者、廣告刊登及開發人員相關入口  
- ⚖️ 包含條款、私隱政策及安全政策說明  
- 🔧 說明 YouTube 的運作方式與測試新功能機制  
- 📅 宣傳 PyData & PyCon Yerevan 2026 活動  
- ©️ 標示 © 2026 Google LLC 版權所有

---

### [](https://github.com/MadsLorentzen/ai-job-search?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-760-august-27-2026)

**原文标题**: [GitHub - MadsLorentzen/ai-job-search: The job search that runs on your machine. AI job application framework built on Claude Code: evaluate postings, tailor CVs, write cover letters, prep interviews. Fork it and own it. · GitHub](https://github.com/MadsLorentzen/ai-job-search?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-760-august-27-2026)

这是一个基于 Claude Code 的 AI 求职应用框架，由作者在失业后亲自构建并成功用它拿下 AI 工程师职位。它把职位评估、简历定制、求职信撰写和面试准备整合为可在本机运行的工作流，并强调 PDF/ATS 验证、双代理评审、可扩展的本地化门户集成与安全设计。项目以 MIT 协议开源，与 Anthropic 无官方关联，也不存在任何加密货币或付费赞助。

- 🤖 **核心定位**：AI 求职框架，跑在自己的机器上，基于 Claude Code，可 fork 后自定义个人画像。
- 🎯 **实战验证**：作者用该框架投出 69 份申请、获得 20 次首面，最终签约成为 AI 工程师。
- ⚙️ **主流程**：`/setup` 建立个人画像，`/scrape` 搜索职位，`/apply <url>` 评估匹配度并生成定制 CV 和求职信。
- 📄 **PDF 验证循环**：每次申请都会编译并视觉检查 PDF，确保 CV 恰好 2 页、求职信 1 页且无排版问题。
- 🔍 **ATS 文本层校验**：用 `pdftotext` 检查 PDF 提取出的文本，确认联系方式、阅读顺序和关键词覆盖，绝不虚构技能。
- ✂️ **智能裁剪**：CV 超页时按相关性、唯一性和求职信依赖度评分，优先删除低价值行而非机械按时间截断。
- 👥 **双代理评审**：起草代理生成内容后，由第二个代理研究公司并批评草案，再修订输出，减少泛泛而谈。
- 🖥️ **常用扩展命令**：`/rank` 批量评分、`/interview` 面试准备、`/outcome` 记录结果、`/gmail-sync` 自动识别邮件状态、`/notion-sync` 同步 Notion、`/html-report` 生成离线仪表板、`/upskill` 技能差距分析。
- 🔌 **可扩展设计**：支持 `/add-portal` 生成新求职门户技能、`/add-template` 注册自定义 CV/求职信模板，评估标准也可自由改写。
- 🌍 **市场适配**：自带丹麦门户 CLI，但模式适用于任何国家；另有 LinkedIn 和 freehire.me 的通用搜索技能。
- 🔒 **安全机制**：职位发布被视为不可信输入，不遵循其内嵌指令；从外部 fork 复制技能前需阅读全部代码并离线跑测试。
- 👤 **隐私提醒**：GitHub 不允许公开仓库的私有 fork，个人求职应使用私有仓库并以上游为 remote，避免个人资料泄露。
- 📊 **数据可视化**：可通过 `/html-report` 生成自包含的 HTML 仪表板，统计申请状态、渠道、漏斗等，完全离线可看。
- 📚 **环境要求**：需要 Claude Code、Python 3.10+、Bun、支持 `lualatex`/`xelatex` 的 LaTeX 发行版；`pypdf` 和 Poppler 为可选依赖。
- 💡 **提升效果的关键**：个人画像越详细，输出越精准；除显式目标搜索外，还能通过分析完整经历发现潜在职业路径。
- 🆓 **开源与合规**：MIT 许可，无关联加密货币、代币或付费赞助；作者通过 Ko-fi 接受捐赠，并欢迎社区贡献。

---

### [](https://github.com/debpalash/VoiceStudio?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-760-august-27-2026)

**原文标题**: [GitHub - debpalash/VoiceStudio: VoiceStudio is the open-source, fully-local ElevenLabs alternative — voice cloning, voice design, video dubbing, dictation, transcription & audiobook creation in 646 languages. · GitHub](https://github.com/debpalash/VoiceStudio?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-760-august-27-2026)

VoiceStudio 是一个本地优先的开源语音工具，前身为 OmniVoice-Studio，专注于语音克隆、视频配音、听写和长篇音频生成。它支持 16 种 TTS 引擎、11 种 ASR 引擎，覆盖 646 种语言，可在 macOS、Windows 和 Linux 上运行，核心功能无需账户或网络，强调数据隐私与本地控制。

- 🎙️ 支持 16 种 TTS 引擎、11 种 ASR 引擎，语言目录达 646 种，适配 macOS、Windows、Linux。
- 🔒 本地优先设计，核心工作流无需账户、API 密钥、订阅或用量计量；数据默认保存在本机。
- 🧬 功能齐全：语音克隆、语音设计、视频配音、故事与有声书、听写小部件、声音分离、说话人分离等。
- ⚡ 提供批处理队列、模型目录、GPU 自动检测（CUDA/MPS/ROCm/CPU）和远程模型下载。
- 🖥️ 架构基于 Tauri v2 桌面壳、React 前端和 FastAPI 后端，通过 localhost:3900 通信。
- 🌐 兼容 OpenAI 音频 API，支持 TTS、转写和流式转写端点，可轻松集成到现有应用。
- 🤖 提供 MCP 服务器和 Agent 技能（如 Claude Code、Codex），可通过 npx 快速安装。
- 📦 系统要求：最低 8GB RAM、10GB 磁盘，推荐 16GB+ RAM、20GB+ SSD；GPU 可选，推荐 8GB+ VRAM。
- 🧩 引擎可替换：如默认 VoiceStudio 引擎支持 600+ 语言，其他引擎如 CosyVoice、GPT-SoVITS 等各有特色。
- 📄 支持从 EPUB/PDF 导入制作有声书，并能导出 .m4b 格式。
- 🔑 许可证为 AGPL-3.0，允许商业使用生成的音频；修改后作为网络服务需提供源码。
- 🧹 数据隐私严格：默认无分析，即使用户同意也只发送不含文本/音频的元数据。
- 📚 文档完善，包含安装指南、故障排查、性能调优、API 参考和卸载说明。
- 💬 社区支持：GitHub Issues、Discord、贡献指南，以及 Ko-fi/PayPal 捐赠渠道。

---

### [](https://github.com/Tencent/AI-Infra-Guard?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-760-august-27-2026)

**原文标题**: [GitHub - Tencent/AI-Infra-Guard: A full-stack AI Red Teaming platform securing AI ecosystems via Agent Scan, Skills Scan, MCP scan, AI Infra scan and LLM jailbreak evaluation. · GitHub](https://github.com/Tencent/AI-Infra-Guard?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-760-august-27-2026)

概述：腾讯朱雀实验室开源的 AI 红队平台 A.I.G（AI-Infra-Guard）的 README 文档，该平台集成了多维度 AI 安全扫描和评估能力，支持 Docker 快速部署、API 集成和智能体调用，并提供丰富的社区与学术资源。

- 🚀 平台定位：A.I.G 是一个面向企业和个人的 AI 红队测试平台，由腾讯朱雀实验室开发，主打全面、智能、易用的 AI 安全风险自检。
- 🛡️ 核心功能：集成 Agent Scan、MCP Server 与 Agent Skills 扫描、AI 基础设施漏洞扫描、越狱评估、API 中继检查器等多种安全能力。
- 🔍 漏洞覆盖：可精准识别 100+ AI 框架组件，覆盖 2000+ 已知 CVE，支持 Ollama、vLLM、ComfyUI、n8n 等主流框架。
- 📊 扫描性能：在 SkillTrustBench 评估中，Claude Opus 4.6 取得 F1 0.9848 最高分，多款主流 LLM 表现出色。
- 🐳 快速部署：支持 Docker Compose 一键启动，提供一键安装脚本，也可从源码构建；要求 4GB RAM 和 10GB 磁盘空间。
- ⚡ CLI 工具：提供 aig-skill-scan 独立命令行工具，可通过 pip 安装并集成到企业 CI/CD 流程。
- 🌐 在线版本：提供 Pro 在线版（需邀请码），优先开放给贡献者，网址为 aigsec.ai。
- 🔌 API 集成：提供完整 REST API 和 Swagger 文档，支持任务创建、扫描管理等操作，方便二次开发。
- 🤖 智能体友好：支持从 OpenClaw 聊天中调用 aig-scanner 技能，实现安全扫描的无缝嵌入。
- 📚 研究与学术：相关成果发表于 Black Hat Europe 等会议，已有 19 篇学术论文引用该平台。
- 💬 社区参与：通过 GitHub Issues、Discussions、微信群和 Discord 等渠道交流，欢迎提交插件、指纹和规则。
- 📄 开源许可：采用 Apache 2.0 协议，要求保留原始 LICENSE/NOTICE，并明确标注使用了腾讯朱雀实验室的 AI-Infra-Guard。

---

### [](https://github.com/sunnypatell/basalt?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-760-august-27-2026)

**原文标题**: [GitHub - sunnypatell/basalt: World's first hazard checker for NVIDIA Blackwell (sm_120), with an assembler and scheduler matched against their own compiler byte for byte. The check they never shipped. · GitHub](https://github.com/sunnypatell/basalt?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-760-august-27-2026)

basalt 是专为 NVIDIA 消费级 Blackwell GPU（sm_120）设计的世界上首个 hazard checker，并附带汇编器与调度器。它主要解决 NVIDIA GPU 指令中 21 位调度控制字不被硬件检查、可能导致静默数据错误的问题；所有组件均以 NVIDIA 官方 ptxas 输出为基准，并通过真实硬件验证。

- ⚠️ NVIDIA GPU 指令包含 21 位调度控制字（stall、scoreboard、reuse），但硬件完全不检查；若 stall 过短，指令会静默读取旧寄存器值，产生错误结果而不崩溃。
- 🔍 basalt 是第一个能对外部生成的 cubin 文件直接检查其调度控制位安全性的工具，补上了 NVIDIA 从未提供的验证环节。
- 🛠️ 项目包含汇编器、hazard 检查器、审计工具与调度器，全部以 ptxas 的精确字节输出为基准，要求与厂商完全一致。
- ✅ 审计了 NVIDIA 官方库（cuBLAS、cuSOLVER、cuSPARSE、NPP 等）中的 2,473 个 sm_120 cubins，全部 0 错误；对 233 个故意缩短 stall 的破坏性内核也 0 漏报。
- 📊 调度器从零计算所有控制位后，439 个可比较的内核在 GPU 上与厂商调度输出字节完全一致，且平均 issue cycles 仅比厂商慢 1.05 倍。
- 🔬 项目采用干净室方法，不含任何 NVIDIA 源代码或头文件，仅通过外部驱动 ptxas/nvdisasm 并测量行为来构建指令数据库。
- 🖥️ 支持所有消费级 Blackwell GPU（RTX 50 系列及 RTX PRO 工作站卡），计算能力均为 sm_120；数据中心 B100/B200 因编码不同不在支持范围。
- ⏱️ 大部分功能无需 GPU 即可运行（仅需 ptxas 和 nvdisasm 作为子进程）；GPU 仅用于三个场景：延迟测量、调度器回环验证和故障注入验证。
- 📏 延迟模型基于一张 RTX 5070 Ti 实测，通过三种独立方法交叉验证，并与已发表研究结果一致；测量中发现并修正了多个此前假设错误的值。
- 📦 开源项目，采用 Apache-2.0 许可证，提供 Python 包和命令行工具，可直接安装使用或作为库集成。

---

### [](https://github.com/petergyang/fuck-cancer/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-760-august-27-2026)

**原文标题**: [GitHub - petergyang/fuck-cancer: Create and update a practical brief to help patients and caregivers advocate for themselves. · GitHub](https://github.com/petergyang/fuck-cancer/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-760-august-27-2026)

这个开源项目提供了一个名为“Fuck Cancer”的技能，旨在帮助癌症患者和护理者通过生成简明、基于证据的简报来更好地为自己辩护。它解决了患者面临信息过载和医疗术语混乱的问题，提供了清晰的行动步骤和知识整理，并支持通过可信医学来源进行研究和更新。

- 💡 **项目动机**：作者在分享母亲的故事后，收到许多照顾癌症亲人的反馈，发现患者和护理者最需要的是三个问题的答案：下一步该做什么、已知道什么、如何为自己倡导。
- 📋 **核心功能**：创建包含5个部分的简报——患者信息、下一步行动、已知信息、医学术语解释、护理日志，方便电话沟通和就医时快速参考。
- 🔍 **信息来源**：基于用户提供的文档和可信医学来源，如NCI的PDQ摘要、ClinicalTrials.gov API等，确保内容有据可依。
- ⚙️ **安装方式**：最简单的方式是将安装指令粘贴到ChatGPT、Claude Code等工具中，也可通过`npx skills add petergyang/fuck-cancer --skill fuck-cancer --global --yes`命令全局安装。
- ✍️ **使用方法**：支持多种场景，如“我父亲刚确诊”开始脑力倾泻、上传报告请求解读、查找附近临床试验、或更新简报加入新的生物标志物报告。
- 🏥 **可信来源范围**：包括NCI的PDQ摘要、国家监管机构（FDA、Health Canada等）、ASCO/ESMO等官方指南、ClinicalTrials.gov API、NCI癌症词典、PubMed同行评审研究，以及学术癌症中心的官方页面。
- ⚠️ **免责声明**：该技能仅支持决策，不提供诊断、不选择治疗方案、不判定试验资格，也不替代患者的医疗团队。
- 📂 **仓库内容**：包含SKILL.md（完整工作流程）、search_trials.py（ClinicalTrials.gov搜索脚本）、eval.md（评估标准）、test_search_trials.py（测试脚本）和openai.yaml（元数据）。支持本地Markdown模式和Google Doc模式，后者需连接Google Drive。

---

### [](https://github.com/ai-dynamo/aiperf?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-760-august-27-2026)

**原文标题**: [GitHub - ai-dynamo/aiperf: AIPerf is a comprehensive benchmarking tool that measures the performance of generative AI models served by your preferred inference solution. · GitHub](https://github.com/ai-dynamo/aiperf?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-760-august-27-2026)

AIPerf 是一个用于评估生成式 AI 模型推理性能的综合基准测试工具，提供命令行指标显示与详细报告。

- 🚀 快速启动：通过 Docker 运行 Ollama 服务器，并使用 `aiperf profile` 命令进行基准测试。
- 📊 输出详尽的性能指标，包括 TTFT、请求延迟、吞吐量等，并支持 CSV/JSON 报告导出。
- ⚙️ 采用多进程架构（10个服务，ZMQ 通信），支持实时仪表盘、进度条及无头模式。
- 🔄 支持多种基准测试模式：并发、请求率、请求率+最大并发、trace 重放等。
- 🔌 插件系统可扩展端点、数据集、传输和指标，并支持 ShareGPT 等公共数据集。
- 🎯 兼容 OpenAI 及 NIM 的多种 API（聊天、补全、嵌入、音频、图像等）。
- 📚 提供大量教程和文档，涵盖负载控制、数据集、端点类型、监控分析等主题。
- ⚠️ 已知问题包括输出长度约束、高并发端口耗尽、配置错误导致挂起等。

---

### [](https://github.com/dblift/dblift?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-760-august-27-2026)

**原文标题**: [GitHub - dblift/dblift: Database changes deserve the same safety as application code. · GitHub](https://github.com/dblift/dblift?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-760-august-27-2026)

DBLift 是一款 Python 原生的数据库迁移工具，类似 Flyway 但无需 JVM，让数据库变更也能像应用代码一样经过测试、CI 和审查。它支持 SQL 与 Python 迁移脚本，提供 CLI 和 SDK，并集成常见 Python 框架。

- 🐍 核心定位：Python 团队专用的 Flyway 风格原始 SQL 迁移工具，无 JVM 依赖，执行前可精确预览 SQL。
- 📦 安装方式：通过 pip 安装，如 `dblift[postgresql]`，另附 `pytest-dblift` 用于测试快速开始。
- 🚀 快速上手：创建 `dblift.yaml` 配置数据库连接，编写 `V1_0_0__create_users_table.sql` 迁移文件，运行 `dblift migrate` 即完成应用。
- 📄 迁移类型：支持版本化迁移（V）、可重复迁移（R）、撤销迁移（U），迁移脚本可用 SQL 或 Python（暴露 `migrate(context)` 函数）。
- ⚙️ 常用命令：`info` 查看状态、`migrate` 应用迁移、`validate` 校验、`undo` 回滚、`baseline` 基线化、`--dry-run --show-sql` 预览 SQL。
- 🔌 框架集成：提供 Django 管理命令、FastAPI 生命周期守卫、Flask 工厂集成及 OpenTelemetry 追踪可选支持。
- 🗄️ 数据库支持：涵盖 PostgreSQL、MySQL、SQL Server、Oracle、SQLite、Cosmos DB、MongoDB 等多种数据库，各有对应 driver extra。
- 📝 配置优先级：命令行 flag > 环境变量 > `dblift.yaml` > 数据库 URL 内嵌值，支持多迁移目录与递归/标签控制。
- ✅ 最佳实践：建议先 dry-run 预览、保持版本号规范、每个迁移可撤销、迁移小型化、测试后上线、不使用已应用的迁移文件。
- 🔬 高级功能：支持 `repair` 修复历史、`import-flyway` 从 Flyway 导入、CI/CD 无系统依赖；Pro 版额外提供静态 SQL 分析与 schema drift 检测。
- ❓ 故障处理：提供常见问题解答，如连接失败、乱码编码、迁移顺序异常、误操作回滚，并可通过 `dblift clean` 重置（慎用）。
- 📜 许可协议：Apache 2.0 开源协议，核心功能免费，Pro 功能需付费订阅。

---

### [](https://github.com/lordx64/pentestkit?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-760-august-27-2026)

**原文标题**: [GitHub - lordx64/pentestkit: Autonomous multi-agent pentest framework — plans, exploits, verifies (proof-required), CVSS-scores and writes client-ready reports. 104/104 (100%) on the XBOW validation benchmarks, powered by Kimi K3. · GitHub](https://github.com/lordx64/pentestkit?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-760-august-27-2026)

pentestkit 是一个基于 Claude Agent SDK 构建的多智能体渗透测试框架。它由一个编排器驱动多个专家代理，执行真实的渗透测试，通过实际利用来验证每个发现，使用 CVSS v3.1 评分，并生成客户就绪的报告。所有出站流量都经过范围保护网关，共享知识库持续积累。该框架在 XBOW 基准测试上取得了 104/104（100%）的满分成绩，所有角色均由 Kimi K3 模型驱动。

- 🕵️ 多智能体架构：编排器负责任务规划，范围代理并行进行漏洞挖掘，验证器强制要求实际利用作为证据，评分器分配 CVSS v3.1 分数，报告器生成最终报告。
- 🏆 基准测试表现：在 XBOW 104 项 Dockerized CTF Web 挑战中达到 100% 通过率（首次 90/104，修复提升后全部解决），精确匹配 flag 抓取评分。
- 📈 流水线设计：包含编排器、范围代理、验证器、CVSS 评分器和报告器五个阶段，验证器是地面真值门禁，可复现发现才被保留。
- 🛡️ 内置安全与控制：范围守卫、授权确认、完整审计日志、最小权限工具分配、每代理请求预算和全局速率限制。
- 📦 安装要求：需要 Python 3.14、Node.js 18+、Docker（含 compose/buildx 插件）、make、git、claude CLI，以及 Kimi API 密钥。
- 🚀 使用方式：提供 `pentest.py` 命令，支持列出作用域、测试范围守卫（`check`）、运行完整项目（`run`）和启动统一控制台（`console`）。
- 📊 基准测试运行：支持一键克隆 XBOW 挑战目标、按难度或指定挑战运行，并自动生成分数图和统计摘要。
- 🤖 模型配置：默认所有角色使用 kimi-k3（通过 Moonshot Anthropic 兼容端点），可在 YAML 中按角色覆盖为其他模型（如 claude-*）。
- 📁 输出产物：每次运行生成 report.md（最终报告）、context.json（知识库/审计日志）、run_summary.md（代理调用/成本）和 evidence/（可重放的 HTTP 请求记录）。
- 🧩 可扩展性：支持添加新的 ScopeDef（作用域模块）、@tool（工具）和 pipeline 阶段，并提供了清晰的目录布局和扩展指南。

---

### [](https://github.com/vinvomero/fastaddress?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-760-august-27-2026)

**原文标题**: [GitHub - vinvomero/fastaddress: fastaddress runs the usaddress CRF model in Rust with the same Python API. 11.3x faster single-core (89,653 vs 7,941 addr/sec) with identical output across 20,738 real county addresses. Confidence scores built-in. Prebuilt wheels, no C toolchain. · GitHub](https://github.com/vinvomero/fastaddress?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-760-august-27-2026)

fastaddress 是一个基于 Rust 的快速美国地址解析库，兼容 usaddress 的 Python API，性能提升显著且输出完全一致，并内置置信度评分，提供预编译安装包。

- 🚀 单核每秒解析 89,653 个地址，比 usaddress 快 11.3 倍；8 线程可达 360,035 个/秒。
- ✅ 在 20,738 个真实县级地址的对比测试中，与 usaddress 输出零分歧。
- 📦 可通过 `pip install fastaddress` 安装，提供 Linux/macOS/Windows 预编译 wheel，无需 Rust 工具链。
- 🧩 API 兼容 `parse()`、`tag()`、`tag_mapping` 等，另有原生 `tag_native()` 避免部分错误，并支持置信度评分。
- ⚠️ 已知差异：`tag()` 返回普通 dict 而非 OrderedDict；非 ASCII 输入的大小写和数字分类可能不同。
- 🧪 实验模型：默认模型为 DataMade 原版未修改；重新训练的模型在最终评估中反而更差，因此未发布。
- 📊 仓库提供可复现的基准脚本（如 `run_speed.py`），若与 README 数字冲突，以基准输出为准。
- 📁 主要目录：`crates/`（Rust 核心）、`benchmark/`（基准与对比）、`training/`（实验训练）、`model/`（模型来源与许可）。

---

### [](https://github.com/kjgpta/vectorsmith?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-760-august-27-2026)

**原文标题**: [GitHub - kjgpta/vectorsmith: Your vector database, as typed tools. Write a tools.yaml, then load_tools in Python or serve over MCP. · GitHub](https://github.com/kjgpta/vectorsmith?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-760-august-27-2026)

VectorSmith 是一个开源工具，旨在将向量数据库封装为 AI 代理可用的类型化工具。用户通过编写 tools.yaml 定义工具契约，编译后即可在 Python 中直接调用，或通过 MCP 协议提供给 Claude、Codex、Cursor 等客户端。它内置租户隔离、密钥管理、安全认证，并支持多种向量数据库，解决了代理访问私有数据时常见的“底层管理工具暴露”“手写 schema 繁琐”“租户过滤不可控”等痛点。

- 📝 只需编写 tools.yaml，即可编译出类型化、租户隔离的工具，支持 Python 导入或 MCP 服务两种消费方式。
- 🔧 解决典型痛点：避免供应商 MCP 暴露底层管理操作，免去手写 JSON schema，隐藏 tenant 过滤器。
- 🛡️ 凭据与租户安全：API 密钥仅在 connections 中配置，模型看不到 URL、密钥和强制附加的 tenant 过滤条件。
- 🐍 Python 集成丰富：支持 LangChain、LangGraph、OpenAI Agents、Anthropic 等框架，通过 `load_tools()` 一键加载。
- 🤖 MCP 客户端兼容：可为 Claude Desktop、Claude Code、Codex、Cursor 甚至 claude.ai 提供标准 MCP 服务。
- 🌐 生产级 HTTP 服务：支持 Streamable HTTP MCP、JWT/OAuth/API Key 认证、Kubernetes 部署与健康检查。
- 📦 多后端适配：内置 Qdrant、pgvector、Chroma、Pinecone、Weaviate、Milvus 六种向量存储，并支持混合检索。
- 🔍 工具类型多样：支持 search、lookup、count、scroll、pipeline 等类型，可声明参数、枚举、过滤器和输出字段。
- ⚙️ 命令行工具完善：提供 init、validate、test、serve、introspect、drafts、approve、auth、migrate 等实用命令。
- 📚 文档与示例齐全：包含完整 YAML 参考、集成指南、企业级安全（RBAC、审计、限流）和可观测性（OTLP、指标、日志）配置。

---

### [](https://www.meetup.com/python-glasgow/events/316258588/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-760-august-27-2026)

**原文标题**: [Building an AI Travel Agent That Actually Remembers You, Wed, Sep 2, 2026, 6:30 PM   | Meetup](https://www.meetup.com/python-glasgow/events/316258588/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-760-august-27-2026)

本次活动是关于构建一个具有记忆功能的AI旅行代理的Python技术分享会，由Python Glasgow主办，采用线上线下混合形式。演讲将深入探讨AI记忆系统的设计，包括短期与长期记忆、写入策略、语义搜索及冲突处理，并通过实际构建一个苏格兰旅行代理来演示。

- 🧠 主题：构建“真正记住你”的AI旅行代理，揭示LLM本身无记忆，记忆需额外系统实现  
- 📅 时间：9月2日（周三）18:30–21:30 BST，混合活动（现场+在线）  
- 📍 地点：The Gamer Club，153 Bath Lane，Glasgow；线上链接仅对报名者可见  
- 👥 组织者：David C. 与 Arron，Python Glasgow社区  
- 🔧 核心内容：用Python构建旅行代理，演示短期与长期记忆、记忆写入策略、语义搜索（如“讨厌早班机”）、时间冲突处理（3月信息覆盖1月）  
- 🕵️ 实战环节：规划行程后查看记忆存储内容，区分“用户明确告知”与“模型推断”，并修复推断错误  
- 🎯 目标受众：Python/AI开发者、LLM实践者、AI新手及对话系统产品工程师；无需AI经验  
- 🏟️ 场地特色：地下科技聚会场所，含主机休息室、街机、厨房/酒吧、PC、投影仪和千兆网络；允许自带酒水，提供免费茶/咖啡  
- 📺 直播：将在YouTube上同步直播（链接见活动页）  
- 📬 联系：organisers@python.scot；可通过Matrix加入Python Glasgow社区聊天

---

### [](https://www.meetup.com/pydata-st-louis/events/316080355/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-760-august-27-2026)

**原文标题**: [The AI Security Paradox: Asymmetric Threats and the Future of Defense, Mon, Aug 31, 2026, 5:00 PM   | Meetup](https://www.meetup.com/pydata-st-louis/events/316080355/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-760-august-27-2026)

overview summary
本次线上活动由PyData St. Louis主办，聚焦AI引发的安全悖论：AI加速漏洞产生，同时赋予攻击者更强的攻击能力，并探讨如何构建下一代防御体系。

- 🎯 核心悖论：AI让开发者更快写代码，也导致更多易受攻击的软件进入生产，安全并未自动改善。
- ⚔️ 攻击者优势：AI赋予攻击者无限耐心和速度，可自动化侦察并快速生成漏洞利用。
- 🐃 “受伤的水牛”效应：遗留代码库与AI驱动攻击路径，使攻击者在短期内占据上风。
- 💸 “Token税”谬误：仅购买现成安全令牌无法解决危机，必须进行深度架构集成。
- 🛡️ 下一代防御系统：结合业务逻辑理解与定制AI（如RAG、知识图谱、自主自愈代理），将被动安全转为自动化、上下文感知的管道。
- 👤 演讲者：Ammar Alim（Adobe产品安全工程负责人）讲解如何重新平衡AI带来的安全方程。
- 📚 相关主题：涉及深度学习、数据工程、数据可视化、开源Python和科学计算。

---

