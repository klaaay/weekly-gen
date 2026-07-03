### [使用本地编码代理 - Sebastian Raschka博士](https://magazine.sebastianraschka.com/p/using-local-coding-agents?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-752-july-2-2026)

**原文标题**: [Using Local Coding Agents - by Sebastian Raschka, PhD](https://magazine.sebastianraschka.com/p/using-local-coding-agents?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-752-july-2-2026)

本教程详细介绍了如何使用开源工具和开放权重模型搭建本地编码代理，作为Claude Code和Codex订阅的替代方案。文章涵盖了从模型选择、性能评估到代理框架安装和使用的完整流程，并比较了Qwen-Code、Codex和Claude Code三种主流框架的表现。

- 🖥️ **本地化优势**：本地设置透明、可审计、免费运行（仅需硬件和电费），完全可控且可自定义，适合隐私敏感任务（如处理收据）和离线场景。
- ⚙️ **核心组件**：本地编码代理由LLM（提供推理和代码生成）和编码框架（提供操作环境，如读写文件、运行命令）组成，两者协同工作。
- 🧠 **模型推荐**：Qwen3.6 35B-A3B是目前同类最佳模型，约22GB下载大小，需30-40GB RAM，在Mac Mini M4和DGX Spark上运行流畅；North Mini Code 1.0是优秀替代品。
- 📊 **性能评估**：本地模型生成速度达20-30 tok/sec即合理，与GPT 5.5“高推理”模式相当；Qwen3.6在概念调试和安全审查任务中表现良好，但工具调用判断仍需改进。
- 🔧 **Qwen-Code设置**：通过Ollama服务本地模型，选择“自定义提供商”和“OpenAI兼容”选项，配置本地端点（http://127.0.0.1:11434/v1）即可连接，支持思考模式。
- 🔍 **安全审计**：使用前需审计代理代码，关注数据外泄、文件权限和提示注入风险；Qwen-Code可禁用遥测和自动更新以增强隐私。
- 📈 **框架对比**：在小型基准测试中，Qwen3.6在Codex上表现优于其原生Qwen-Code框架；Claude Code令牌消耗最高（主要来自输入令牌），Codex最低。
- 🌐 **远程部署**：可通过SSH隧道将Mac连接到DGX Spark等远程机器，实现模型远程运行而代理本地使用。
- 🎯 **结论**：本地代理的核心在于理解模型服务层、代理框架、权限模型和评估方法；Qwen3.6等30-35B MoE模型已足够胜任多数任务，且速度与GPT 5.5相当。

---

### [使用Micro-DDP扩展你的AI模型 – 教程 – YouTube](https://www.youtube.com/watch?v=7q4D6_3syuE&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-752-july-2-2026)

**原文标题**: [Scaling Your AI Models with Micro-DDP – Tutorial - YouTube](https://www.youtube.com/watch?v=7q4D6_3syuE&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-752-july-2-2026)

YouTube 的相關資訊與政策總覽
- 📰 新聞中心：提供官方新聞與最新動態
- ©️ 版權：保護原創內容與智慧財產權
- 📞 聯絡我們：提供用戶與創作者聯繫管道
- 🎬 創作者：支援內容創作者的資源與工具
- 💰 刊登廣告：廣告合作與收益機會
- 👨‍💻 開發人員：API 與技術開發相關資訊
- 📜 條款：使用規範與服務條款
- 🔒 私隱：用戶資料保護與隱私政策
- 🛡️ 政策及安全：平台安全與內容審查準則
- ⚙️ YouTube 的運作方式：解釋平台功能與機制
- 🧪 測試新功能：新功能測試與用戶體驗改進
- 🏢 © 2026 Google LLC：版權歸屬與法律聲明

---

### [Go deh!：稀疏范围](https://paddy3118.blogspot.com/2026/06/sparse-ranges.html?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-752-july-2-2026)

**原文标题**: [Go deh!: Sparse Ranges](https://paddy3118.blogspot.com/2026/06/sparse-ranges.html?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-752-july-2-2026)

本文介紹了作者從Python Discuss論壇的一個想法出發，實現了一個名為 `sparse_range` 的輕量級、無狀態的稀疏整數範圍生成器，並通過埃拉托色尼篩法進行了壓力測試，驗證了其可靠性。

- 💡 **靈感來源**：Python Discuss論壇上關於「從範圍中排除子範圍」的需求，啟發了作者開發一個乾淨、高效的抽象解決方案。
- ⚙️ **核心架構**：`sparse_range` 基於 `S_in`（允許範圍）和 `S_ex`（排除範圍）兩組範圍集合，並使用 `RangePointer` 來動態對齊迭代方向，實現無狀態的數值跳躍。
- 🔄 **方向對齊**：為了支援正向和反向迭代，內部所有子範圍的游標方向必須與外部循環一致，否則會通過數學反轉公式進行重新計算。
- 🧪 **測試驗證**：通過5個測試案例（包括正向、反向、大跨步、越界和空輸入邊界情況），所有測試均順利通過。
- 🏛️ **壓力測試：埃拉托色尼篩法**：作者將 `sparse_range` 應用於純聲明式的埃拉托色尼篩法，使用多達13個並發排除範圍，成功生成了200以內的46個質數，並通過了正向和反向遍歷驗證。
- 🧠 **AI輔助開發**：作者使用Gemini AI協助實現演算法細節和測試程式碼，但核心設計和除錯由作者主導。

---

### [构建我自己的自托管dbt云 | Daan | 2026年6月 | Medium](https://medium.com/@diedericks.dan/building-my-own-self-hosted-dbt-cloud-d3b737ae885c?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-752-july-2-2026)

**原文标题**: [Building My Own Self-Hosted dbt Cloud | by Daan | Jun, 2026 | Medium](https://medium.com/@diedericks.dan/building-my-own-self-hosted-dbt-cloud-d3b737ae885c?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-752-july-2-2026)

本文介绍了作者如何利用React、FastAPI、dbt Core和Prefect自行搭建一个自托管的dbt Cloud替代方案，旨在为不熟悉命令行的开发者提供类似云端的体验。

- 💡 **项目起源**：作者从dbt Core开源版出发，思考能否为不擅长CLI的开发者打造一个类似dbt Cloud的图形化体验。
- 🎯 **核心目标**：构建一个前端界面，模拟dbt Cloud的关键功能，包括项目概览、作业管理、运行历史、模型探索、环境管理和开发工具。
- 🛠️ **技术栈**：前端使用React + Tailwind + Shadcn，后端采用FastAPI，并通过Prefect实现编排功能。
- 🔒 **安全改进**：通过白名单机制限制dbt命令（如run、test、build等），防止命令注入风险。
- 🚀 **开发突破**：使用Monaco Editor实现浏览器内代码编辑器，并集成Git版本控制和终端访问。
- 📊 **数据展示**：解析schema.yml、dbt_project.yml和profiles.yml文件，呈现模型探索、环境配置和项目概览页面。
- 🔗 **Prefect集成**：通过Prefect的OpenAPI接口实现作业编排，替代了脆弱的CLI解析方式，提升了架构清晰度。
- 📋 **当前功能**：已实现开发环境、模型探索、项目概览、运行历史、作业管理和环境配置等核心模块。
- 🔮 **未来计划**：添加CI/CD功能，通过GitHub Actions自动触发验证流程，并实现分支与环境关联。
- 🧪 **最终测试**：作者计划在实际dbt项目中测试该平台，记录每次回退到传统工具的原因，并持续优化以提升实用性。

---

### [无锁线程Python：过去、现在与未来 [LWN.net]](https://lwn.net/Articles/1078367/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-752-july-2-2026)

**原文标题**: [Free-threaded Python: past, present, and future [LWN.net]](https://lwn.net/Articles/1078367/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-752-july-2-2026)

PyCon US 2026上，CPython核心开发者Thomas Wouters详细介绍了Python自由线程（free-threaded）版本的动机、历史、现状和未来展望。自由线程移除了全局解释器锁（GIL），允许多线程并行执行，是Python近年来的重大变化。

- 🧵 **动机与挑战**：GIL移除旨在提升多线程性能，但Python中所有对象都是共享可变数据，导致线程安全复杂；GIL保护了对象引用计数，但移除后需解决原子操作、内存模型等问题。
- 📜 **历史演进**：从1996年Greg Stein的补丁到2015年Larry Hastings的Gilectomy项目，再到Sam Gross基于PEP 703的No-GIL分支，最终形成当前自由线程方案。
- 🔧 **技术实现**：采用对象拥有者线程、延迟引用计数、推测性引用计数、静止状态回收、细粒度锁、mimalloc内存分配器等，确保单线程性能损失控制在0-10%。
- 🚀 **当前状态**：Python 3.13实验性支持，3.14成为正式特性，3.15将提供统一稳定ABI；超过50%的顶级PyPI包已支持自由线程。
- 🛠️ **扩展适配**：C扩展需保护全局变量、使用临界区、声明自由线程支持；普通Python代码通常无需修改，但需注意多线程bug。
- 🔮 **未来预测**：自由线程可能成为默认Python版本（3.16至3.20之间），GIL版本最终将完全移除（预计下个十年）。

---

### [将后量子密码学引入Python - Trail of Bits博客](https://blog.trailofbits.com/2026/06/30/shipping-post-quantum-cryptography-to-python/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-752-july-2-2026)

**原文标题**: [Shipping post-quantum cryptography to Python - The Trail of Bits Blog](https://blog.trailofbits.com/2026/06/30/shipping-post-quantum-cryptography-to-python/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-752-july-2-2026)

概述总结
Python生态现已通过pyca/cryptography库支持后量子密码学，包括ML-KEM和ML-DSA标准算法，为应对量子计算机威胁做好准备。

- 🔐 后量子密码学现可通过`pip install cryptography>=48`轻松获取，支持ML-KEM密钥封装和ML-DSA数字签名。
- 📊 后量子算法在保持相同安全强度的同时，公钥和签名大小比经典算法大1-2个数量级，例如ML-DSA-65签名达3309字节。
- 🚀 ML-DSA作为量子安全签名方案，API与现有非对称原语类似，支持生成、签名和验证操作。
- 🔑 ML-KEM采用密钥封装机制而非Diffie-Hellman交换，通过封装/解封装方式建立共享密钥。
- ⏳ SLH-DSA（基于哈希的签名标准）仍在开发中，提供保守的量子安全后备方案。
- 🔄 协议集成是迁移关键，需要将后量子算法整合到Certbot、Ansible等实际工具中。
- 🏛️ 美国白宫已下令联邦系统在2030年前完成后量子密钥建立迁移，2031年前完成数字签名迁移。
- 💡 后量子密码学的主要优势不仅是量子抵抗，还包括其他安全特性。

---

### [Python：在WeakKeyDictionary中为对象存储额外数据 - Adam Johnson](https://adamj.eu/tech/2026/06/27/python-weak-key-dict-pattern/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-752-july-2-2026)

**原文标题**: [Python: store extra data for objects in a WeakKeyDictionary - Adam Johnson](https://adamj.eu/tech/2026/06/27/python-weak-key-dict-pattern/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-752-july-2-2026)

### 概述摘要
本文介绍了使用 `WeakKeyDictionary` 为 Python 对象存储额外数据的方法，避免了直接属性存储的缺点，并解释了其优势与适用条件。

- 📦 **问题背景**：需要为对象（如 `ast.Module`）关联额外数据，但直接属性存储存在限制（如不支持任意属性、命名冲突、干扰 `vars()` 等）。
- 🔑 **解决方案**：使用 `WeakKeyDictionary` 以对象为键存储数据，利用弱引用在对象不再被引用时自动清理条目，保持 O(1) 查找性能。
- ✅ **对象要求**：对象必须可哈希（默认满足）且可弱引用（大多数用户类默认支持，内置类型如 `int`、`str` 等不支持，但可通过在 `__slots__` 中添加 `__weakref__` 实现）。
- ⚠️ **与 `functools.cache` 对比**：`functools.cache` 使用强引用，会阻止对象被垃圾回收，导致内存泄漏；而 `WeakKeyDictionary` 自动释放未引用对象的内存。
- 🛠️ **实现示例**：通过 `try-except` 模式检查缓存，若不存在则计算并存储结果，确保高效且安全地管理额外数据。

---

### [我是如何为专业AI开发设置Python环境的 - YouTube](https://www.youtube.com/watch?v=PHICGGjN5Pc&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-752-july-2-2026)

**原文标题**: [How I Set Up Python for Professional AI Development - YouTube](https://www.youtube.com/watch?v=PHICGGjN5Pc&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-752-july-2-2026)

本頁面列出YouTube平台的各項基本資訊與政策指引。

- 📰 新聞中心：提供YouTube最新消息與公告
- ©️ 版權：說明內容版權相關規範
- 📞 聯絡我們：提供用戶聯繫管道
- 🎨 創作者：為內容創作者提供支援與資源
- 📢 刊登廣告：介紹廣告刊登選項與服務
- 💻 開發人員：提供API與開發工具資訊
- 📜 條款：列出服務使用條款
- 🔒 私隱：說明隱私權保護政策
- 🛡️ 政策及安全：涵蓋平台安全與內容政策
- ⚙️ YouTube 的運作方式：解釋平台運作機制
- 🧪 測試新功能：介紹正在測試的新功能
- © 2026 Google LLC：版權所有歸Google公司

---

### [我们如何使用DSPy将Dash聊天中的AI评估转化为更好的回复 - Dropbox](https://dropbox.tech/machine-learning/how-we-turned-ai-evaluations-into-better-responses-in-dash-chat?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-752-july-2-2026)

**原文标题**: [How we used DSPy to turn AI evaluations into better responses in Dash chat - Dropbox](https://dropbox.tech/machine-learning/how-we-turned-ai-evaluations-into-better-responses-in-dash-chat?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-752-july-2-2026)

概述摘要  
Dropbox 团队利用DSPy框架优化AI聊天代理Dash的评估与性能，通过人工标注校准评估模型，再使用优化后的评估器改进代理提示词，最终显著减少不完整回答并降低token消耗。

- 🧠 **评估复杂性**：代理评估需覆盖多步骤过程（意图理解、工具使用、上下文选择等），不能仅关注最终回答。
- 📊 **人工校准**：使用人工标注的示例（含评分、推理笔记和失败代码）来校准LLM评估器，确保其与人类判断一致。
- 🔄 **DSPy优化循环**：通过DSPy的GEPA和MIPROv2算法自动优化评估器提示词，再基于优化后的评估器改进代理提示词，形成反馈闭环。
- ⚡ **性能提升**：优化后不完整回答减少26%，遗漏关键方面减少13%，同时token使用量下降5.4%，回答长度缩短9.8%。
- 🛡️ **安全护栏**：对提示词编辑设置自动检查（结构、完整性、缓存行为等），确保优化过程安全可控。
- 🚀 **未来方向**：代理优化将转向持续机器学习工作流（重放数据、运行优化、验证改进），强调强评估信号与人工审查结合。

---

### [带注释的PyTorch训练循环——idlemachines](https://idlemachines.co.uk/essays/pytorch-training-loop?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-752-july-2-2026)

**原文标题**: [The annotated PyTorch training loop — idlemachines](https://idlemachines.co.uk/essays/pytorch-training-loop?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-752-july-2-2026)

## 概述总结
本文深入解析了PyTorch训练循环中每一行代码的作用，以及错误放置代码会导致什么问题，涵盖了数据加载、模型构建、前向/反向传播、梯度裁剪、权重更新、学习率调度、验证和GPU优化等完整流程。

- 📊 **数据管道**：Dataset和DataLoader负责数据加载与批处理，`num_workers`并行预取，`pin_memory`加速GPU传输，`drop_last`避免小批量影响BatchNorm
- 🎲 **可重复性**：设置多种随机种子（torch、numpy、random），关闭cuDNN非确定性算法，确保实验结果可复现
- 🏗️ **模型构建**：`nn.Module`需调用`super().__init__()`注册子模块，`.to(device)`必须在构建优化器之前执行
- 🔄 **训练模式**：`model.train()`启用Dropout和BatchNorm训练行为，省略该调用不会报错但会改变学习动态
- 🧹 **梯度清零**：`optimizer.zero_grad()`必须在每个批次前调用，否则梯度会累积，`set_to_none=True`可略微提升性能
- 📈 **前向传播**：动态构建计算图，激活值保留在内存中用于反向传播，`torch.no_grad()`可禁用图构建节省内存
- 🎯 **损失计算**：`CrossEntropyLoss`内部结合LogSoftmax和NLLLoss，使用log-sum-exp技巧保证数值稳定性
- 🔙 **反向传播**：`loss.backward()`遍历计算图填充参数梯度，`retain_graph=True`允许多次反向传播
- ✂️ **梯度裁剪**：必须在`backward()`之后、`step()`之前调用，全局L2范数裁剪保留梯度方向
- ⚡ **权重更新**：`optimizer.step()`读取`.grad`并应用更新规则（如Adam的动量估计和偏差校正）
- 📉 **学习率调度**：`scheduler.step()`每个epoch调用一次（非批次循环内），余弦退火结合线性预热是标准做法
- ✅ **验证模式**：`model.eval()`和`torch.no_grad()`需同时使用，前者改变层行为，后者禁用图构建
- 💾 **检查点保存**：保存模型、优化器、调度器状态和验证损失，仅在验证损失改善时保存最佳模型
- 🚀 **GPU优化**：使用混合精度（bfloat16无需GradScaler）、`non_blocking=True`异步传输、`torch.compile`融合内核操作

---

### [Python网格布尔运算库比较与基准测试 — 2026 · Polydera](https://polydera.com/algorithms/python-mesh-boolean-libraries-2026?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-752-july-2-2026)

**原文标题**: [Python Mesh Boolean Library Comparison and Benchmarks — 2026 · Polydera](https://polydera.com/algorithms/python-mesh-boolean-libraries-2026?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-752-july-2-2026)

本文对三种可pip安装的Python网格布尔运算库（trueform、MeshLib、Manifold）在Thingi10K数据集上进行了性能基准测试，测试规模为每个操作数20万至150万多边形。结果显示trueform在所有测试中速度最快。

- 🚀 **trueform最快**：中位数18毫秒，比MeshLib快4.9倍，比Manifold快6.9倍（几何均值），在全部1000对测试中均领先。
- 🔧 **库对比**：trueform 0.9.8、MeshLib 3.1、Manifold 3.5均通过pip安装，使用默认线程数，从NumPy数组输入到输出。
- ✅ **结果一致性**：三个库在所有测试对上生成的实体体积一致（浮点容差内），trueform和Manifold在1000对上均有效，MeshLib在999对上有效。
- 📊 **测试协议**：每次测试构建新对象，计时包括原生对象构建和布尔运算，取5次最佳结果，排除文件I/O。
- 🖥️ **环境**：Apple M4 Max、macOS、CPython 3.13，所有库均提供原生arm64构建。
- ⏱️ **性能分布**：trueform的中位数时间集中在18毫秒附近，而MeshLib和Manifold的分布更分散，尾部更长。
- 📚 **扩展信息**：trueform的Python绑定性能略低于原生C++（15.7毫秒中位数），完整八库对比（含CGAL等）及N元缩放测试可参考行业基准。

---

### [我为什么写PEP 832——虚拟环境发现](https://snarky.ca/why-i-wrote-pep-832-virtual-environment-discovery/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-752-july-2-2026)

**原文标题**: [Why I wrote PEP 832 -- virtual environment discovery](https://snarky.ca/why-i-wrote-pep-832-virtual-environment-discovery/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-752-july-2-2026)

### 概述总结
文章解释了为什么需要PEP 832（虚拟环境发现），主要解决编辑器（如VS Code）无法自动识别项目使用的虚拟环境和工作流工具的问题，并提出了标准化解决方案。

- 📝 **核心问题**：编辑器无法自动知道项目使用哪种工作流工具（如Hatch、Poetry、uv）以及虚拟环境的位置，导致无法正确运行代码或分析依赖。
- 🔍 **首次打开项目**：当用户首次打开项目时，编辑器无法推断用户偏好的工具（如pyproject.toml中的tool表），且硬编码工具列表无法覆盖自定义工具（如my-tool）。
- 🗺️ **环境发现困难**：工具可能将环境存储在项目本地或全局位置，且某些工具（如virtualenvwrapper、conda）允许环境跨项目共享，导致编辑器难以匹配正确的环境（尤其当用户有700+环境时）。
- 💡 **解决方案**：提出两个标准化方法——1）`.python-envs`文件记录环境路径（最后一行作为默认）；2）`pyproject.toml`中的`[workflow]`表指定工作流工具，通过JSON-RPC协议（WSP）与编辑器通信。
- 🎯 **设计目标**：降低用户配置负担，隐藏环境复杂性，使VS Code能作为工作流工具的用户（而非对等方），并避免编辑器特定的硬编码方案（如Hatch扩展）。
- 🌍 **通用性**：方案不限于VS Code，其他编辑器或AI代理也可复用，避免重复开发（如每个工具为不同编辑器定制扩展）。

---

### [GitHub - safishamsi/graphify: AI编码助手技能（Claude Code、Codex、OpenCode、Cursor、Gemini CLI等）。将任何代码文件夹、SQL模式、R脚本、Shell脚本、文档、论文、图像或视频转换为可查询的知识图谱。应用代码+数据库模式+基础设施整合于一个图谱中。· GitHub](https://github.com/safishamsi/graphify?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-752-july-2-2026)

**原文标题**: [GitHub - safishamsi/graphify: AI coding assistant skill (Claude Code, Codex, OpenCode, Cursor, Gemini CLI, and more). Turn any folder of code, SQL schemas, R scripts, shell scripts, docs, papers, images, or videos into a queryable knowledge graph. App code + database schema + infrastructure in one graph. · GitHub](https://github.com/safishamsi/graphify?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-752-july-2-2026)

Graphify 是一个 AI 编码助手技能，能将整个项目（代码、文档、图片、视频等）映射成一个可查询的知识图谱，支持多种主流 AI 编码平台。

- 🧠 **一键生成知识图谱**：在 AI 助手中输入 `/graphify .`，即可将整个项目映射为包含代码、文档、PDF、图片、视频的知识图谱，支持查询、过滤和搜索。
- 🔧 **广泛平台兼容**：支持 Claude Code、Codex、Cursor、Gemini CLI、GitHub Copilot CLI 等 30+ 种 AI 编码助手和 IDE。
- 📦 **简单安装与使用**：通过 `uv tool install graphifyy` 安装，运行 `graphify install` 注册技能，即可在 AI 助手中使用 `/graphify` 命令。
- 🌐 **多语言与文件支持**：支持 36 种编程语言（通过 tree-sitter 本地解析）、文档、Office 文件、PDF、图片、视频/音频等，代码提取完全离线。
- 📊 **丰富的输出格式**：生成交互式 HTML 图、Markdown 报告、JSON 数据、Mermaid 调用流程图、SVG、GraphML、Obsidian 仓库等。
- 🔍 **强大查询功能**：支持自然语言查询、路径查找、节点解释、社区检测、PR 影响分析等，可通过 MCP 服务器或 HTTP 服务共享。
- 🔄 **团队协作与版本控制**：`graphify-out/` 可提交到 Git，支持自动合并冲突、Git 钩子自动重建、增量更新。
- 🛡️ **隐私优先**：代码本地处理不离开机器，视频/音频本地转录，无遥测、无使用追踪、无分析。
- 🧩 **可扩展与可定制**：支持多种 LLM 后端（OpenAI、Claude、Gemini、Ollama 等），提供 PDF、Office、视频等可选扩展包。

---

### [GitHub - LukasNiessen/ArchUnitPython: ArchUnitPython是一个架构测试库。在您的Python应用中指定并确保架构规则。易于设置和管道集成。](https://github.com/LukasNiessen/ArchUnitPython?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-752-july-2-2026)

**原文标题**: [GitHub - LukasNiessen/ArchUnitPython: ArchUnitPython is an architecture testing library. Specify and ensure architecture rules in your Python app. Easy setup and pipeline integration. · GitHub](https://github.com/LukasNiessen/ArchUnitPython?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-752-july-2-2026)

ArchUnitPython 是一個用於 Python 專案的架構測試庫，可強制執行依賴方向、檢測循環依賴、實施編碼標準，並與 pytest 等測試框架無縫整合。

- ⚡ **快速入門**：只需 `pip install archunitpython`，即可在現有測試套件中添加架構規則測試，並自動在 CI 中執行。
- 🐹 **多種使用案例**：支援分層架構、整潔架構/六邊形架構、微服務/模組化架構的依賴規則驗證。
- 🐣 **豐富功能**：包括循環依賴檢測、層級依賴規則、命名約定檢查、代碼度量（如 LCOM 內聚性）、自定義規則和 PlantUML 圖表驗證。
- 📊 **依賴圖報告**：可生成 DOT、Mermaid、D2、CSV、JSON、HTML 等多種格式的依賴圖報告，並支援多種圖表探索選項。
- 🔎 **靈活的模式匹配**：支援 glob 字串模式和正則表達式，可針對檔案名、路徑或資料夾進行匹配。
- 📢 **資訊豐富的錯誤訊息**：測試失敗時會提供詳細的檔案路徑和違規說明，方便除錯。
- 🦊 **社群與貢獻**：歡迎貢獻，使用 Conventional Commits，並透過 GitHub Issues 和 Discussions 進行交流。

---

### [GitHub - diabloidyobane/DriverScope: 自动化BYOVD驱动程序分析：导入扫描、IOCTL分发提取、Speakeasy仿真 · GitHub](https://github.com/diabloidyobane/DriverScope?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-752-july-2-2026)

**原文标题**: [GitHub - diabloidyobane/DriverScope: Automated BYOVD driver analysis: import scanning, IOCTL dispatch extraction, Speakeasy emulation · GitHub](https://github.com/diabloidyobane/DriverScope?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-752-july-2-2026)

DriverScope 是一个自动化 BYOVD（自带易受攻击驱动）狩猎工具，用于扫描 Windows 内核驱动中的危险导入、提取 IOCTL 调度接口，并与已知数据库交叉比对，发现零日漏洞候选。

- 🛠️ **核心功能**：扫描系统驱动，提取 IOCTL 代码，通过 Speakeasy 模拟驱动入口，并生成零日狩猎报告
- 🔍 **检测能力**：识别 18 种内核原语，包括物理内存映射、跨进程附加、进程查找、MSR 访问等危险导入
- 📊 **实时演示**：在 Windows 11 上扫描 463 个驱动，发现 423 个标记项，并展示 IOCTL 提取结果
- 🌐 **批量供应商抓取**：支持 55 个供应商（覆盖 10 个地区），使用 Playwright 爬取驱动下载门户，构建本地语料库
- 🤖 **Claude 辅助分析**：通过 Claude API 对扫描结果进行批量分类，提供每个 IOCTL 的原始类型和风险判定
- 🧩 **完整管道**：从采集、扫描、富化、聚类到差异分析，生成 Markdown 和 HTML 报告，结果持久化到 SQLite
- 🔬 **参考实现**：提供三个 PoC 和 C++ 封装头文件，演示 KslD.sys、WinNotify.sys 和 RTCore64.sys 的利用原语
- 📚 **丰富文档**：包含安装指南、子命令说明、使用示例、安全警告和披露建议，支持社区贡献

---

### [GitHub - MaxandreOgeret/collider：Collider 为 Meson 的原生 wrap 生态系统带来现代包管理。](https://github.com/MaxandreOgeret/collider?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-752-july-2-2026)

**原文标题**: [GitHub - MaxandreOgeret/collider: Collider brings modern package management to Meson's native wrap ecosystem. · GitHub](https://github.com/MaxandreOgeret/collider?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-752-july-2-2026)

Collider 是一个为 Meson 构建系统提供现代包管理功能的扩展工具，它增强了依赖解析、锁文件支持和私有仓库发布能力。

- 📦 **自动依赖解析**：自动解析 Meson wrap 项目的依赖，简化手动维护 wrap 文件的工作。
- 🔒 **可复现构建锁文件**：通过 `collider lock` 生成锁文件，确保构建环境的一致性和可复现性。
- 🌐 **私有仓库支持**：允许团队托管与 WrapDB 兼容的私有包仓库，并发布自定义包。
- 💾 **离线依赖缓存**：支持离线依赖缓存，方便在没有网络的环境下进行构建。
- 🚀 **快速上手**：通过 `collider init`、`collider repo add` 等命令，快速集成到现有 Meson 项目中。
- 📚 **全面文档**：提供详细的用户指南、配置说明和 CLI 参考，帮助用户轻松上手。
- 🛠️ **兼容性**：与 WrapDB 完全兼容，支持 Python 3.10+ 和 Meson 1.8.5+。
- 🏷️ **开源许可**：采用 Apache-2.0 许可证，社区友好且可自由使用。

---

### [GitHub - rajtilakjee/kivo：一款轻量级桌面提词器。](https://github.com/rajtilakjee/kivo?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-752-july-2-2026)

**原文标题**: [GitHub - rajtilakjee/kivo: A lightweight desktop teleprompter. · GitHub](https://github.com/rajtilakjee/kivo?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-752-july-2-2026)

Kivo 是一款基于 PySide6 构建的轻量级桌面提词器，提供始终置顶的透明阅读覆盖层，适用于脚本、演示和视频录制。

- 🚀 **轻量级桌面提词器**：采用 PySide6 构建，提供简洁、始终置顶的透明阅读覆盖层，适用于脚本、AI生成内容、演示和视频录制。
- 🎨 **现代UI与核心功能**：无边框圆角半透明界面，支持拖拽窗口、打开 .txt 文件并自动重载，以及平滑的提词器式自动滚动。
- ⌨️ **键盘快捷键支持**：包含 Esc 关闭、空格暂停/恢复滚动、上下箭头调节滚动速度等快捷键，提升操作效率。
- 📦 **简易安装与构建**：通过克隆仓库、安装依赖即可运行，并支持使用 PyInstaller 打包为独立可执行文件。
- 🗺️ **未来路线图**：计划添加设置窗口、全局热键、记住上次文件、字体自定义、可调透明度、滚动速度预设、镜像模式、多主题等功能。
- 🛠️ **技术栈与许可**：基于 Python 3 和 PySide6 开发，采用 MIT 许可证开源，并包含行为准则和贡献指南。

---

