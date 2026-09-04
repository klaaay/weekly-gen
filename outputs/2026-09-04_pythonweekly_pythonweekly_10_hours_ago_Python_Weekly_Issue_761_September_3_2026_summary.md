### [2026 年](https://lp.jetbrains.com/django-developer-survey-2026/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-761-september-3-2026)

**原文标题**: [Django Developers Survey 2026 Results](https://lp.jetbrains.com/django-developer-survey-2026/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-761-september-3-2026)

这份报告是 2026 年 Django 开发者调查的第五次年度总结，由 Django 软件基金会与 PyCharm 合作完成，收集了全球约 3500 名开发者的反馈。

- 📊 调查规模与方法：2026 年 5 月至 7 月通过官方 Django 渠道收集，过滤后共 3,468 份有效回复，排除了年龄、异常回答等不可靠数据。
- 🎯 Django 主要用途：75% 用于工作，69% 用于个人项目，22% 用于教育；服务器渲染模板（72%）仍是最常见模式，但 API-only 和 SPA 后端也占相当比例。
- 🗓️ 版本使用趋势：43% 使用 6.0 版本，44% 使用 5.x；46% 的开发者跟随每个稳定版本升级，35% 只升级 LTS 版本。
- 🗄️ 数据库选择：PostgreSQL 以 79% 居首，SQLite 46%，MySQL 26%；GeoDjango 中 PostGIS 最常用（23%）。
- 🛠️ 开发工作流：75% 通过命令行动手创建项目；最流行的代码工具为 Ruff（43%）；环境管理以 venv（63%）和 uv（43%）为主；测试首选 pytest（45%）。
- 📡 API 与前端：API 构建以 Django REST Framework（73%）占绝对优势，Django Ninja 为 17%；前端 CSS 常用 Bootstrap（45%）和 Tailwind（39%）；JavaScript 框架中 React（38%）和 htmx（34%）领先。
- ⚡ 现代 Django 特性：57% 使用类型提示；33% 使用异步功能（其中 WebSockets 占 61%、async views 占 58%）；最常用 type checker 是内置（40%）和 Mypy（32%）。
- ☁️ 部署与运维：54% 主要部署为单体应用；44% 自托管/VPS，36% 使用主流云服务商；51% 使用 GitHub Actions；静态文件多由 nginx/Apache 直接服务（50%）。
- 🤖 AI 使用情况：58% 每天使用 AI；常用工具包括 Claude Code（35%）、ChatGPT（33%）和 GitHub Copilot（23%）；主要用于写代码（74%）、规划研究（69%）和调试（66%）。
- 🌐 社区与贡献：最受欢迎第三方包为 Django REST framework、allauth、Debug Toolbar、Ninja、Celery；58% 从未贡献过开源，主要障碍是不知如何开始（43%）和时间不足（42%）。
- 👥 人口统计：56% 为全职员工，83% 是开发者/工程师；33% 具有 11 年以上编程经验；27% 年龄在 21–29 岁；男性占 89%；欧洲（37%）和亚洲（24%）为主要地区。

---

### [你以为这是优秀的 OOP…其实不然 - YouTube](https://www.youtube.com/watch?v=RqcEK7sWesQ&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-761-september-3-2026)

**原文标题**: [You Think This Is Good OOP… It’s Not - YouTube](https://www.youtube.com/watch?v=RqcEK7sWesQ&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-761-september-3-2026)

overview summary  
该内容为 YouTube 网站页脚信息，涵盖简介、新闻、版权、联系方式、创作者支持、广告、开发者资源、条款隐私、政策安全及平台运作说明。

- 📰 提供新闻中心与公司简介入口  
- ©️ 明确版权归属及联络方式  
- 🎬 面向创作者与广告主提供支持  
- 👨‍💻 为开发者与广告合作方设置专区  
- 🔒 展示条款、隐私、政策与安全说明  
- ⚙️ 介绍 YouTube 运作方式及新功能测试  
- 📅 版权声明为 © 2026 Google LLC

---

### [](https://grahamdumpleton.me/posts/2026/09/unit-testing-with-wrapture/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-761-september-3-2026)

**原文标题**: [Unit testing with wrapture - Graham Dumpleton](https://grahamdumpleton.me/posts/2026/09/unit-testing-with-wrapture/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-761-september-3-2026)

本文對比 wrapture 與 unittest.mock 在單元測試中的差異，重點展示 wrapture 透過包裝真實程式碼而非替換，在自呼叫、嚴格簽名校驗、修改真實呼叫、錯誤路徑斷言及測試程式碼結構上的優勢，同時說明 mock 仍適用的場景。

- 🔄 核心理念：wrapture 是「包裝」而非「替換」真實程式碼，與 unittest.mock 的替代式打樁有根本差異。
- ⚙️ 在簡單打樁上兩者相似，但 wrapture 預設嚴格校驗簽名，能捕獲 mock 會放過的錯誤呼叫（如多餘關鍵字參數）。
- 🕵️ 對物件內部自呼叫（如 place() → _take_payment()），mock 無法觀測或被替換掉；wrapture 能記錄真實呼叫層級。
- ✨ wrapture 可執行真實方法同時改寫參數/回傳值，mock 無法做到「只改一處」。
- 🛡️ 錯誤路徑測試：用 wrapture 可注入 Ledger 失敗，斷言退款使用了真實 charge ID、通知未發送，並可驗證事件順序。
- 📊 斷言失敗訊息會展示「filtered from」真實事件，便於診斷過窄過濾。
- 📝 測試程式碼形態：binding 可在模組層級宣告而不生效，直到 with 區塊或 timeline 使用；有裝飾器形式將期望寫在頂部。
- ♻️ fixtures 可配合 binding 使用，允許同一測試中途切換行為（如失敗回復）。
- 🧪 可選 pytest 外掛能偵測洩漏的 binding 並附加呼叫樹到失敗報告。
- 👍 unittest.mock 仍適用：當需要動態產生不存在屬性/鏈式呼叫的 MagicMock 時，mock 是合適的工具。
- 📚 下一篇文章將深入 timeline/tape，用資源洩漏範例說明。

---

### [](https://www.pythonmorsels.com/when-to-use-notimplemented/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-761-september-3-2026)

**原文标题**: [When to use NotImplemented - Python Morsels](https://www.pythonmorsels.com/when-to-use-notimplemented/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-761-september-3-2026)

overview summary
本文介紹 Python 中 NotImplemented 的用途與重要性：當雙下劃線方法（dunder method）無法處理某個物件時，應回傳 NotImplemented，讓 Python 有機會嘗試右側物件的反向方法，以維持運算的一致性與正確性。

- 🔍 `NotImplemented` 是 Python 的特殊值，表示「我不知道如何處理這個操作」
- 🐍 整數與浮點數的 `==`、`+` 等運算之所以能成功，是因為其中一方會回傳 `NotImplemented`，讓 Python 轉而呼叫另一方的反向方法
- 🔄 執行 `a + b` 時，Python 先嘗試 `a.__add__(b)`；若得到 `NotImplemented`，再嘗試 `b.__radd__(a)`
- 🧱 自訂類別時，若 `__eq__`、`__add__` 等方法收到無法處理的型別，應回傳 `NotImplemented` 而非直接回傳 `False`
- ❓ 回傳 `NotImplemented` 與回傳 `False` 的差異：若回傳 `False`，可能導致「物件 A 等於 B，但 B 不等於 A」的不一致情況
- 🛡️ 使用 `isinstance` 進行型別檢查是少數需要強型別檢查的情境，因為要明確判斷「是否能與此物件進行操作」
- ✅ 若雙方都回傳 `NotImplemented`，Python 在相等比較時會回傳 `False`，在其他操作（如 `+`、`<`）時會拋出 `TypeError`
- 📌 正確做法：在自訂的 dunder method 中，若物件無法處理另一個物件，請回傳 `NotImplemented`，以確保 Python 能正確委派給其他物件

---

### [Avi Chawla 在 X 上：“https://t](https://x.com/_avichawla/status/2093265776266637739?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-761-september-3-2026)

**原文标题**: [Avi Chawla on X: "https://t.co/sLoULsUfEt" / X](https://x.com/_avichawla/status/2093265776266637739?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-761-september-3-2026)

本文梳理了 LLM 推理中最常被混为一谈的四类缓存层：KV Cache、Prefix Caching、Prompt Caching 与 Semantic Caching，并额外提到精确匹配响应缓存。文章逐一解释它们各自存储什么、如何决策命中与失效、有哪些代价与风险，以及在生产环境中让缓存失效的常见原因和应对方式。

- 🧠 KV Cache 在预填充阶段为每个 token 的每一层保存 K/V 向量，解码时只需做矩阵向量乘，避免整段序列重复计算；但解码因此受 HBM 带宽限制，每一步都要搬移整份缓存。
- 📈 KV Cache 随生成 token 数线性增长；70B 模型在 128K 上下文下约需 40GB（BF16），几乎等于一个 4-bit 量化模型的体积。
- 🔧 减小 KV 缓存的手段包括 GQA 共享 KV 头、DeepSeek 的 MLA 隐向量压缩，以及 KV 量化；但量化会引入额外开销，短上下文里不一定更快。
- ♻️ KV Cache 默认随请求结束释放；手动在多次 `generate` 之间复用 `past_key_values` 可实现多轮免重算，但前提是后续 prompt 必须与上一轮 token 序列严格前缀一致。
- 🔗 Prefix Caching 是服务端在请求结束后保留 KV block，用“父块哈希 + 当前块 token”的链式哈希做前缀匹配，只有完整 block 被索引，末尾不足 block 会被重算。
- 🔍 vLLM 的调度器会按序匹配 block 直到第一个 miss；命中块增加引用计数防止被驱逐，miss 部分则重新 prefill。
- 🧂 Prefix Caching 可通过 per-tenant salt 隔离不同客户：相同文本在不同租户间不会共享同一份物理缓存，但会牺牲内存和命中率。
- ⚠️ Prefix Caching 只节省 prefill，不缩短 decode；在高度独特的 prompt 流量下，哈希计算等开销甚至可能造成已测得的吞吐回退。
- 📚 RAG 场景常因检索文档顺序改变而完全无法命中缓存；LMCache/CacheBlend 可以在任意位置复用 chunk 缓存，只重算恢复交叉注意力所需的小部分 token，TTFT 提升约 2–3 倍。
- 💰 Prompt Caching 是托管模型把服务端 prefix reuse 变成计费项：Anthropic 写入约 1.25x 基础输入价、读取约 0.1x，OpenAI 也有类似倍数；缓存写入位置由 `cache_control` 决定。
- 📏 托管缓存有最短可缓存长度、向后查找限制（例如 Anthropic 最多 20 个 block）等规则；如果两个 usage counter 都为 0，说明本次请求低于可缓存长度或被完全绕过。
- 🎯 Semantic Caching 用 embedding 相似度匹配整个输入，命中时直接返回旧回复，因此能同时跳过输入和输出 token，但每次请求都要付出一次 embedding 往返。
- ⚠️ Semantic Caching 的相似度并不代表答案正确：改写、加一个否定、换一个数值可能获得几乎相同的分数，却需要完全不同的答案；固定阈值无法根治这种风险，生产上还需额外的答案校验。
- 🧾 第五种缓存是 byte 完全相同的精确匹配响应缓存：没有假阳性，也能省往返 token；应先用请求日志测量“字节级重复率”，再决定是否引入 embedding。
- 🛠️ 生产建议一：把时间戳、request id、用户名等可变内容放到 prompt 后部，稳定内容放前面，并用 `cache_control` 标记在边界上；任何前缀改动都会使后续所有 block 失效。
- 🛠️ 生产建议二：注意工具 schema 的排序、provider 侧渲染设置（web search、citations、thinking、tool_choice 等）；A/B 测试不同的 reasoning 配置会把缓存分成两份。
- 🛠️ 生产建议三：不要重写或摘要历史前缀；原地截断工具输出可保持前缀一致；换用不同模型/配置也会让整段累积历史按冷前缀计费。
- 🔍 判断两个 prompt 是否可复用时，应直接比较 token ID 而不是渲染文本；常见陷阱包括 BOS token、尾部换行、聊天模板默认系统消息，以及工具输出重新序列化带来的差异。

---

### [](https://blog.veitheller.de/numpy.html?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-761-september-3-2026)

**原文标题**: [Tracing np.add, all the way down | Veit's Blog](https://blog.veitheller.de/numpy.html?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-761-september-3-2026)

本文深入剖析了 `np.add(a, b)` 从 Python 层调用到最终 SIMD 内核执行的完整内部流程，展示了 NumPy 2.5.2 中 ufunc 的架构、历史演变与优化机制。核心要点如下：

- 🧭 路线图：`np.add(a, b)` 依次经历参数解析、`__array_ufunc__` 覆盖检查、类型提升与分发、迭代策略选择，最后进入实际内层循环。
- 📦 `np.add` 是 `numpy.ufunc` 实例，内部封装了 22 个类型签名对应的内层循环；本文关注的是 `dd->d`（double→double）路径。
- 🔀 执行前会先询问参数是否实现 `__array_ufunc__`，Dask、CuPy 等第三方库借此接管运算，这是协议分流的“逃生舱”。
- 🧮 类型分发有缓存：首次遇到某类型组合才完整解析，后续调用仅做哈希查找，大幅提升重复调用性能。
- 🏗 现代 `ArrayMethod` 层包裹了数十年历史的“legacy”内层循环接口，`generic_wrapped_legacy_loop` 适配器依然在每日无数运算中扮演核心角色。
- ⚡ 快速路径与迭代器：形状匹配且连续/一维时走“trivial loop”直接调用内层循环；否则使用 `NpyIter` 处理广播、缓冲、重叠检测等复杂情况。
- 🧵 GIL 管理与告警：非对象循环会按阈值释放 GIL；浮点溢出告警并非循环内检查，而是依赖循环后的 CPU 状态标志。
- ⏱ 性能差异实例：连续数组与跨步数组的加法耗时差达 2.6 倍，部分因内存带宽，部分因 SIMD 分支仅在连续/标量布局下才能启用。
- 📝 内层循环由模板生成：`loops_arithm_fp.dispatch.c.src` 通过模板展开为 `DOUBLE_add` 等函数，包含标量回退与可移植 SIMD 专门化。
- 🗂 构建时通过 `generate_umath.py` 生成 C 代码和函数表；`dispatch=` 标记使同一循环按 CPU 特性多次编译，导入时再按运行时检测选择最适版本。
- 💎 代码历史分层清晰：旧式 `types` 表和函数指针仍是基石，新协议与 SIMD 调度逐层叠加而未淘汰旧结构——这正是“遗产”的价值所在。
- 🔧 持续演进：主分支已针对自由线程 Python 重构了旧式循环查找，将扫描从每次调用改为注册时一次并缓存，反映 NumPy 不断适应新时代。

---

### [](https://www.youtube.com/watch?v=c9AnqCeyxbI&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-761-september-3-2026)

**原文标题**: [Building AI Agents in Pure Python - Beginner Course - YouTube](https://www.youtube.com/watch?v=c9AnqCeyxbI&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-761-september-3-2026)

该内容為 YouTube 頁面底部的導覽與法律資訊清單，涵蓋公司資訊、使用者支援、合作選項、政策條款及版權聲明等標準連結。

- 📄 提供「簡介」與「新聞中心」連結，供使用者了解 YouTube 公司資訊與最新動態  
- ⚖️ 包含「版權」、「條款」、「私隱」及「政策及安全」等法律與規範頁面  
- 📞 設有「聯絡我們」管道，方便使用者與平台溝通  
- 🎬 針對「創作者」提供相關資源與支援  
- 📢 開放「刊登廣告」選項，協助企業與品牌進行曝光  
- 💻 設有「開發人員」專區，提供技術文件與 API 等工具  
- 🔍 說明「YouTube 的運作方式」，並開放「測試新功能」的參與機會  
- ©️ 標示版權年份為 2026 年，屬於 Google LLC

---

### [](https://www.youtube.com/watch?v=AFYNEGtsjKI&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-761-september-3-2026)

**原文标题**: [Django API Overview - DRF, django-ninja, django-bolt and django-modern-rest - YouTube](https://www.youtube.com/watch?v=AFYNEGtsjKI&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-761-september-3-2026)

概述：此內容為 YouTube 頁面底部的標準導覽與法律資訊區塊，列出平台相關連結、政策說明及版權年份。

- 📄 提供平台簡介、新聞中心與聯絡方式
- ⚖️ 涵蓋版權、條款、私隱及政策安全資訊
- 👥 設有創作者與廣告刊登相關連結
- 🛠️ 包含開發人員資源及 YouTube 運作方式說明
- 🧪 開放測試新功能與體驗
- 📅 保留所有權利，© 2026 Google LLC

---

### [](https://www.better-simple.com/django/2026/09/02/nifty-feature-use-index-for-custom-migrations/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-761-september-3-2026)

**原文标题**: [
    
      Nifty Django Feature: Use Index for Custom Migration Operations · Better Simple
    
  ](https://www.better-simple.com/django/2026/09/02/nifty-feature-use-index-for-custom-migrations/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-761-september-3-2026)

该文章介绍了 Django 中一个相当 hacky 但有趣的功能：通过继承 `models.Index` 来自定义数据库迁移操作，使开发者能在模型层直接控制表格的 SQL 变更。

- 🤯 这是一个非常 hacky 的功能，作者坦言“可能不应该这样做”，但仍值得探讨。
- 🧩 通过继承 `models.Index` 并重写 `create_sql` 和 `remove_sql` 方法，可以生成任意自定义 SQL。
- 📦 将自定义类放在模型的 `Meta.indexes` 列表中，`makemigrations` 会自动生成对应的迁移文件。
- 🛠️ 生成的 SQL 可以是任何操作，例如修改表格注释、设置触发器或整表级改造。
- 🎯 实际案例：在 `django-security-label` 项目中，通过此机制为 PostgreSQL Anonymizer 配置匿名化规则。
- 👩‍💻 这种方案让匿名化规则成为模型定义的一部分，迁移系统能自动管理字段变动，减少开发者负担。
- 💡 虽然 hacky，但它启发了我们如何扩展 Django，让数据库层的自定义操作更贴近模型逻辑。

---

### [](https://blog.jetbrains.com/pycharm/2026/08/fine-tuning-sota-object-detection-models-on-real-world-datasets/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-761-september-3-2026)

**原文标题**: [Fine-Tuning SOTA Object Detection Models on Real-World Datasets - The JetBrains Blog](https://blog.jetbrains.com/pycharm/2026/08/fine-tuning-sota-object-detection-models-on-real-world-datasets/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-761-september-3-2026)

本文介绍了在 PyCharm 中微调三种 SOTA 目标检测模型（YOLO12、YOLO26、RF-DETR）的完整流程，涵盖 COCO 基线验证、零样本测试、三个特殊数据集（电缆损伤、骨折 X 光、汽水瓶）的微调与评估，并展示了 PyCharm 如何通过隔离环境管理多模型工作流。

- 🔬 为何微调：预训练模型基于 COCO（80 类日常场景），真实应用（骨折、工业缺陷等）既超出类别范围又存在巨大视觉分布差异，直接部署几乎无效。
- 🧠 模型选择：实验涵盖 YOLO12、YOLO26（两种尺寸）和 RF-DETR（Nano/Base），并在 COCO val2017 上复现基线，验证准确性与延迟。
- 📊 零样本结果：未微调的模型在三个目标数据集上 mAP50-95 几乎为 0，证明“预训练 ≠ 可部署”，即使 SOTA 模型也无法识别未见过类别。
- 🛠️ 环境配置：利用 PyCharm + uv 创建三个隔离 Python 环境，分别对应不同 YOLO 版本及 RF-DETR，解决依赖冲突，并支持远程 GPU 解释器。
- 📥 数据获取：通过 Roboflow API 下载 RF100-VL 中三个数据集（cable-damage、bone-fracture、soda-bottles），格式为 YOLOv8。
- ⚙️ 微调参数：每个模型在单张 A100 GPU 上训练 10 个 epoch，使用 Ultralytics 或 RF-DETR 自带的高层训练 API。
- 🏆 微调后结果：汽水瓶任务最易（mAP50 0.91–0.97）；电缆损伤检测易但精确定位难（mAP50-95 仅 0.37–0.45）；骨折 X 光仍困难（最佳 RF-DETR Base 仅 0.447 mAP50）。
- 📈 综合表现：RF-DETR Base 在三个数据集上最稳定，DETR 架构跨域迁移更强；YOLO26 延迟最优但骨折任务表现差。
- 🖼️ 可视化验证：预测框叠加显示汽水瓶标注紧实准确，电缆损伤框偏大或遗漏，骨折检测不足一半且模型间分歧大。
- 💡 核心结论：没有普适“最佳”检测器，需综合任务、时延、许可及预训练数据相似性；微调 10 epoch 足以适应部分场景，但对大域迁移（如 X 光）需更多数据或领域预训练。
- 🧩 PyCharm 价值：单项目管理多环境，内置终端、Python Packages 工具窗口及远程开发支持，简化了复杂依赖与 GPU 训练流程。

---

### [](https://github.com/SenteLabsAI/OpenExecutive?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-761-september-3-2026)

**原文标题**: [GitHub - SenteLabsAI/OpenExecutive: AI-powered virtual executive team — a single coherent executive persona backed by 8 specialist Claude agents (FastAPI + Next.js). · GitHub](https://github.com/SenteLabsAI/OpenExecutive?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-761-september-3-2026)

OpenExecutive 是一个开源的 AI 虚拟高管团队系统，由 SenteLabsAI 发布。它把 8 个专业领域代理（战略、财务、人力、法务、运营、营销、产品、董事会沟通）凝聚为一个统一的高管助手，结合内置 MBA 知识与企业上传文档提供 RAG 问答，同时具备跨会话记忆、主动调度和多种工作消息平台集成。该项目基于 FastAPI + ChromaDB + Next.js，可通过 Anthropic 或本地模型运行，并提供了完整的部署、评测与扩展机制。

- 🏢 项目定位：OpenExecutive 作为公司的“虚拟高管团队”，以统一、连贯的高管风格对外回复，用户不会感知背后的多代理架构。
- 🧠 八大专业代理：涵盖 CSO、CFO、CHRO、法务、COO、CMO、CPO 和董事会沟通，各代理从 ChromaDB 检索相关上下文后，再由执行编排器合成回复。
- 📚 双层知识检索：内置 MBA 级 Markdown 知识 + 上传的公司文档分库存储；RAG 上下文注入用户消息，而非缓存系统提示。
- 💾 情景记忆：每次回复后由轻量模型提取关键决策与行动项并存入 SQLite，下一次会话自动携带 <past_decisions> 区块实现跨会话记忆。
- ⏰ 调度器：内置任务运行器通过 UPDATE … RETURNING 认领到期任务以防重复触发，因此 API 必须保持单实例运行。
- ⚙️ 技术栈：Python 3.11 + FastAPI + uv，ChromaDB 向量库，SQLite 记忆库，Next.js 15 Web UI；默认模型为 Claude Sonnet 4.6，深推理任务使用 Opus 4.7。
- 🚀 快速开始：克隆仓库后配置 .env 的 ANTHROPIC_API_KEY，运行 make dev；首次启动会下载约 90MB 嵌入模型，需等待几分钟。
- 💬 多渠道集成：支持 Web UI、Slack、Email、Telegram、Google Chat、Discord（DM/提及/斜杠命令）及 CLI，可共用同一数据库。
- 📄 文档上传：可通过 UI/CLI/API 上传融资路演、财务模型、战略文档，系统会在相关问答中自动引用。
- ☁️ 生产部署：基于 Fly.io 部署，dev 与 qa 两套环境各自独立；API 使用持久卷，UI 无状态；必须保证单机运行，不能覆盖 max_machines_running=1。
- 🔐 访问控制：UI 由 Google 登录 + 邮箱白名单保护，API 通过共享请求头验证；渠道用户需在 /people 界面配置。
- 🔧 配置灵活：通过环境变量可切换 Anthropic、OpenRouter 或本地 OpenAI 兼容服务（Ollama、LM Studio、vLLM、llama.cpp），也支持混合路由。
- 🧩 可扩展性：新增专家代理需继承 BaseAgent、注册到 router、补充领域别名和内置知识文档，并添加至少 2 个 eval 场景。
- 📊 评估体系：evals/ 包含 29 个跨 8 领域的场景，由 Claude Opus 4.7 作为裁判评分，CI 门槛要求均分 ≥3.5/5。
- 🔒 隐私与合规：公司配置与上传文档均被 gitignore，数据只保存在本地或自己的云存储中，发送给 Anthropic 的 API 数据不会被用于训练；项目采用 Apache 2.0 许可证。

---

### [](https://github.com/securo-finance/securo?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-761-september-3-2026)

**原文标题**: [GitHub - securo-finance/securo: Open-source personal finance manager. Self-hosted, privacy-first. · GitHub](https://github.com/securo-finance/securo?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-761-september-3-2026)

Securo 是一个开源、可自托管的个人财务管理工具，强调隐私与数据主权，支持多账户、交易管理、预算、银行同步、多币种、多用户及可选 AI 助手等功能，并采用 AGPL-3.0 许可。

- 🚀 快速开始：Linux/macOS 可用一行脚本安装，Windows 需 Docker Desktop，然后访问 localhost:3000 创建账户即可使用。
- 💰 核心功能：多账户余额管理、交易搜索/筛选/CSV 导出、OFX/QIF/CAMT/CSV 文件导入、自动分类规则、循环交易与预算、储蓄目标、资产追踪、净值和收支报表。
- 🏦 银行同步：支持 Pluggy（巴西）、Enable Banking（欧洲 PSD2）、SimpleFIN（美国及国际），可按需在 .env 中配置并自动注册。
- 🔐 登录与安全：支持 TOTP 双因素认证、OIDC（如 Authentik/Pocket ID）单点登录，并可完全禁用本地认证以强制 SSO。
- 🗝️ Passkeys：默认启用生物识别/安全密钥登录，但仅限 localhost 或 HTTPS 域名；IP 地址和纯 HTTP 不可用。
- 💱 汇率转换：可配置 Open Exchange Rates 密钥自动获取汇率，无密钥时跨币种按 1:1 并显示警告。
- 🤖 可选 AI 代理：支持 OpenAI/Anthropic/Ollama 等，通过 MCP 工具访问数据，提供 RAG 知识库与全局聊天面板，默认关闭零成本。
- 🧩 技术栈：后端 FastAPI + SQLAlchemy + Celery，前端 React + TypeScript，数据库 PostgreSQL，队列 Redis，支持 Docker Compose 部署。
- 🛠️ 开发与贡献：提供 pytest 测试、mise 工具链支持、AI 辅助编码合规指南，并鼓励提交 issue 或预约交流。
- 📜 许可证：AGPL-3.0，允许自由使用/修改/分发，但任何修改（含 SaaS 服务）也必须以同样许可证开源。

---

### [](https://github.com/pollen-robotics/microduck_rl?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-761-september-3-2026)

**原文标题**: [GitHub - pollen-robotics/microduck_rl: RL training environments for Microduck (mjlab) · GitHub](https://github.com/pollen-robotics/microduck_rl?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-761-september-3-2026)

Microduck RL 是面向约 800g 双足机器人 Microduck 的强化学习训练环境，基于 mjlab（MuJoCo Warp）和 PPO，用于训练后部署到真实机器人。

- 🤖 项目定位：提供 RL 训练环境，策略在 50 Hz 训练、导出 ONNX，并通过 microduck 运行时部署到真实机器人
- ⚙️ 快速开始：需要 CUDA GPU 和 uv；`uv run train Mjlab-Velocity-Flat-MicroDuck --env.scene.num-envs 4096` 约 1-2 小时即可训练出可用的行走策略，也支持从检查点恢复，无 GPU 可用 `--hf-jobs` 远程运行
- 🗂️ 多种任务：涵盖平地/粗糙地形行走、站立恢复、坐站、地面拾取、踢球、前滚翻、轮滑、斜坡滑行、原地旋转等，所有策略共享 61 维观测契约，运行时可以热切换
- 🦾 执行器仿真：采用 BAM M6 XL330 执行器模型，包含电压控制、反电动势、负载相关摩擦以及域随机化（电池电压、电压跌落、命令延迟、摩擦幅度），是缩小 sim2real 差距的关键
- 🔧 机器人模型：提供从 Onshape 导出的多种 MJCF 模型，如行走专用、地面接触、滚轮、全碰撞和带 Backlash 变体等，场景文件便于快速查看和推理
- 📂 项目结构清晰：源码按 `robot/`、`actuator/`、`tasks/` 组织，包含训练 CLI、HF Jobs 提交脚本和每个任务族的独立配置模块
- 📐 观测空间约定：61 维 actor 观测 = 48 维本体感觉 + 命令（twist 3 维、head_pose 4 维、body_pose 6 维）；未使用的命令槽会零填充，确保不同策略可无缝切换
- ⚡ Backlash 变体：每个主任务提供带 ±1° 齿轮间隙的模型，通过无驱动的 `passive_*_backlash` 关节建模，观测/动作维度不变，导出 ONNX 时无需改动
- 📤 策略发布：`uv run publish` 将策略上传到 Hugging Face Hub，支持 episodic、perpetual（gait 或 held pose）等类型，自动验证 ONNX 输入输出形状、NaN/常量输出，并生成带有观测归一化器的部署文件
- 📋 测试与许可：提供 CPU-only 的回归测试，锁定关节索引映射、奖励符号和 NaN 防护；代码采用 Apache-2.0 许可，3D 模型采用 CC BY-SA-NC 许可

---

### [](https://github.com/perixtar/Tech-OA-Interview-Questions?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-761-september-3-2026)

**原文标题**: [GitHub - perixtar/Tech-OA-Interview-Questions: Daily updated list of Tech Company OAs and Interview Problems. Save your time from finding them all over the internet. · GitHub](https://github.com/perixtar/Tech-OA-Interview-Questions?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-761-september-3-2026)

该仓库是每日更新的科技公司在线测评（OA）与面试问题合集，聚合来自互联网的题目信息，旨在节省求职者的搜索时间，并配套多种公司标签与相关资源。

- 📅 每日更新科技公司的在线测评（OA）与面试题目
- ⭐ 获得 4.8k 星标、334 个 fork 和 245 个 watcher，社区关注度较高
- 🔧 包含 689 个提交，维护活跃，并配置了贡献指南
- 🏢 聚焦 Amazon 等科技公司，覆盖实习、全职及面试准备场景
- 🔗 提供 FastPrep 问题列表等外部资源，以及 formats、scripts、assets 等目录
- 🧩 主要主题包括 amazon、interview-preparation、online-assessments、university 等
- 🤝 开源项目支持社区贡献，鼓励开发者共同补充题目与答案

---

### [](https://github.com/yashmulgaonkar/FlightScnr_Pi?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-761-september-3-2026)

**原文标题**: [GitHub - yashmulgaonkar/FlightScnr_Pi: Desktop flight and marine radar: a real-time aircraft and marine vessel tracker powered by a Raspberry Pi and 4" round screen. · GitHub](https://github.com/yashmulgaonkar/FlightScnr_Pi?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-761-september-3-2026)

FlightScnr Pi 是一个基于树莓派的桌面飞行/海上雷达项目，采用 4 英寸圆形触控屏，提供暗色雷达界面、手势导航、实时航班与船只追踪，并通过本地 Web 门户完成所有配置，日常使用无需 SSH。

- 🛰️ 实时追踪飞机（可选船只），支持 FR24、adsb.fi、本地 dump1090/readsb 等数据源，并可叠加天气、地震、野火等图层。
- 📱 720×720 圆形触摸屏，滑动切换雷达主页、航班详情、追踪航班路线、Follow/Live 地图和时钟/天气等屏幕。
- 🗺️ 十种底图样式（CARTO、OSM、Stadia、Esri、FAA VFR 等），支持标签、按高度着色、降水、机场叠层等效果。
- 🔊 支持 LiveATC 音频输出到 USB/蓝牙音箱，可在设备或门户选择机场和频道；HUD 可显示时间、天气和 AQI，并带各项音频控制。
- 🖼️ 航班详情可显示飞机照片（planespotters/Wikimedia），还可选 AIS 船只显示及船舶照片。
- 🛠️ 本地 Web 门户（http://<hostname>.local）管理全部设置、数据源和系统更新，支持 OTA“立即更新”“今晚稍后”等选项。
- 📥 安装快捷：刷入 Raspberry Pi OS 后运行 `sudo bash install-pi.sh`，自动切换 X11（支持捏合缩放）、启用风扇、禁用 Wi-Fi 省电并开启蓝牙。
- 📚 完整文档见项目 Wiki，涵盖硬件组装、软件配置、故障排除和更新方法。
- 👥 社区通过 Discord 提供帮助，欢迎提交 PR；较大改动建议先开 issue 讨论。
- ⚖️ 固件与文档采用 CC BY-NC-SA 4.0 许可；3D 打印外壳文件在 MakerWorld 上另行许可，请阅读对应模型页条款。

---

### [](https://github.com/ashuttl/linecast?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-761-september-3-2026)

**原文标题**: [GitHub - ashuttl/linecast: Weather, tides, the sun, the moon, and maps, in your terminal. The Old Farmer's Almanac meets Minitel. · GitHub](https://github.com/ashuttl/linecast?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-761-september-3-2026)

linecast 是一个在终端中展示天气、潮汐、太阳、月亮与地图的工具套件，纯 Python 构建、跨平台，使用公开数据且无需账号或 API 密钥。

- 🖥️ 提供六个实时、鼠标友好的命令行应用：weather、sunshine、moon、tides、radar、maps，并支持快捷键与滚轮/拖拽交互。
- 🐍 纯 Python 实现，除 Windows 上需要 tzdata 与 truststore 外无依赖；需 Python 3.10+，且无需任何 API 密钥或账户。
- 📦 安装方式多样：Homebrew、uv、pipx、pip、AUR、nixpkgs，甚至可用 curl 一行脚本临时运行。
- 🌤️ weather 显示当前天气、逐小时温度、7 天预报、空气质量、与常年对比，以及覆盖 45 国的官方预警。
- ☀️ sunshine 模拟 Apple Watch 太阳表盘，展示太阳运行弧线、天空颜色、昼长与月相；也支持整年视图并呈现极昼/极夜现象。
- 🌙 moon 按本地视角绘制月相、升降时间与月历；支持中、日、韩、泰、夏威夷、伊斯兰、希伯来等传统历法。
- 🌊 tides 为多日潮汐曲线，标出高/低潮及当前水位；数据来自 NOAA、加拿大水文局、昆士兰、香港天文台等国家服务或全球潮汐模型。
- 🛰️ radar 可播放全球雷达或卫星云图动画，叠加温度、风场与美国预警多边形，并支持多种自定义配色主题。
- 🗺️ maps 提供街道、地形与可旋转地球视图；内置地点搜索、路线导航、实时昼夜边界与云层动画。
- 🗣️ 界面支持 18 种语言，可通过 --lang 或环境变量设置；月历传统年份可手动指定或跟随语言。
- ⚙️ 设置保存在 ~/.config/linecast/config.json；位置、单位、时钟、语言、颜色、主题等均可通过命令行参数或环境变量覆盖。
- 🎨 自动从终端主题取色，也可强制 truecolor、256 色、16 色或无色模式；图标支持 Nerd Font、emoji 与纯 Unicode。
- 🧾 支持一次性静态输出，并提供 --json 与 --oneline，方便脚本和状态栏集成。
- ⌨️ 提供 linecast link 短命令与 bash/zsh/fish/nushell 自动补全，提升日常使用效率。
- 🩺 linecast doctor 可检查终端信息、配置来源与各数据源连通性；--debug 会输出所有回退路径，便于排障。
- 🗃️ 数据源采用开放服务：Open-Meteo、NOAA、LibreWXR、OpenFreeMap/OpenStreetMap、NASA 月球纹理等。
- 📜 项目以 MIT 许可开源，配有架构文档、测试与 lint，欢迎贡献者提交 Pull Request。

---

### [](https://github.com/experientiallabs/experiential?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-761-september-3-2026)

**原文标题**: [GitHub - experientiallabs/experiential: An open source model gateway that provides one control plane across closed, open-source, local, and custom models. · GitHub](https://github.com/experientiallabs/experiential?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-761-september-3-2026)

Experiential 是一个开源的 agent 工作流网关与路由器，它通过统一的 OpenAI 兼容 API 连接托管、BYOK 和本地模型，并提供权限、预算控制以及基于真实流量优化模型的能力。

- 🌐 开源网关：通过单一 OpenAI 兼容 API 接入托管、自带密钥（BYOK）和本地模型，作为 agent 工作流的统一入口。
- 🎛️ 精细化控制：决定哪些用户和 agent 可使用哪些模型、用在哪些场景，并限定预算上限。
- ⚡ 快速启动：`pip install experiential` 后运行 `exp`，由向导完成提供商、模型和预算配置，再通过 curl 调用即可。
- ☁️ 托管替代方案：提供托管平台（platform.experientiallabs.ai），同时兼容 OpenAI 与 Anthropic Messages API。
- 🐍 Python 集成：`exp.load_router("my-project")` 可将路由器作为标准 OpenAI 客户端在本地使用。
- 📊 流量驱动优化：先采集 OTel trace 或使用公共数据集，再用 `exp build` 构建项目，结合 `exp optimize` 微调模型。
- 🔒 遥测默认开启：PostHog 匿名聚合遥测，不涉及提示、追踪、凭据或原始内容，也可用命令禁用。
- 🛠️ 开发与测试：使用 `uv sync --extra dev` + ruff + ty check + pytest 进行开发验证，规范见 AGENTS.md。

---

### [](https://github.com/microsoft/AutoSaddler?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-761-september-3-2026)

**原文标题**: [GitHub - microsoft/AutoSaddler · GitHub](https://github.com/microsoft/AutoSaddler?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-761-september-3-2026)

AutoSaddler 是微软发布的一个开源工具，用于自动化优化 LLM 智能体（agent）的“马具”（harness）系统。它通过诊断智能体执行轨迹，对提示词、工具和中间件进行结构化更新，并筛选出具有泛化能力的改进方案，从而显著提升智能体在多个基准上的表现。以下是该项目的核心要点总结：

- 🛠️ **核心功能**：自动优化 LLM-agent harness，涵盖提示词、工具定义与实现、中间件钩子及智能体循环逻辑的全面搜索与改进。
- 📈 **显著效果**：在 GAIA2（53.0→62.0）、SWE-Bench Pro（37.3→46.9）和 Terminal-Bench 2.0（40.0→50.0）上分别实现 +9.0、+9.6、+10.0 个百分点（pp）的 Pass@1 提升。
- 🔍 **深度诊断机制**：不只做浅层反思，而是深入调试执行轨迹与 harness 代码库，定位失败根本原因。
- 🧩 **结构化干预**：通过明确的补丁分类法与分阶段 Capability-to-Steering 调度，精准作用于提示词、工具和中间件，而非无约束地直接编辑。
- 🌿 **泛化感知选择**：基于“演化 DAG”（EvoDAG）进行反思与候选合成，保留具有广泛价值的经验，确保更新超越单次动机轨迹的验证。
- 🗄️ **持久化执行**：支持仅追加事件记录、不可变来源追踪、可恢复状态和内容寻址候选，保证运行的耐用性与可复现性。
- 📋 **版本体系**：V2 为当前主推的持久化插件化实现；V1 为论文实验所用的旧版研究实现，仅用于复现。
- 📦 **安装与启动**：要求 Python 3.12–3.14、uv 与 Git，通过条件命令 `uv sync --extra dev` 安装，并用 V2 本地模板配置快速运行无凭据的确定性测试。
- ⚙️ **配置策略**：所有 V2 配置以 `schema_version` 开头，通过场景插件适配具体的 harness/基准，并声明 scenario、optimization、provider、storage 四类所有权区域。
- 🚀 **运行模式**：采用“诊断 - 补丁 / 反思 / 演化”三类会话，将优化视为离线小批量学习；候选更新在训练样本上验证，并在开发集上设关卡，预算耗尽后返回最佳候选。
- 🔌 **可扩展架构**：内置 fake 与 Meta-ARE（GAIA2 冒烟测试）示例；未来将支持 OpenClaw、Codex 与 Terminal-Bench；外部插件可通过 `autosaddler.scenarios` 入口点注册。
- ⏯️ **恢复与分支**：运行中断后可安全重试，非终态检查点可带新 run ID 分叉；但同一 run ID 不可并发执行，且要求输入字节级一致。
- 🔒 **安全与合规**：配置严格失败关闭；分享运行前需检查会话/评估记录中的敏感数据；遵循 Microsoft 开源行为准则与 MIT 许可证。

---

### [](https://github.com/neo4j-labs/neocarta?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-761-september-3-2026)

**原文标题**: [GitHub - neo4j-labs/neocarta: Library built for generating semantic layer graphs for query routing, query generation and data discovery · GitHub](https://github.com/neo4j-labs/neocarta?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-761-september-3-2026)

Neocarta 是一个由 Neo4j Labs 支持的开源库，目标是在 Neo4j 中构建语义层，并通过 MCP 服务器向 AI 代理提供数据组织结构、业务含义和存储位置的结构化信息，从而提升 Text2Query、查询路由和数据发现的可靠性。其核心流程包括摄取（Ingest）、服务（Serve）和使用（Use），并支持多种数据源连接器、嵌入生成、CLI 与 MCP 工具。

- 📚 Neocarta 是端到端语义层库，统一将模式元数据、业务术语、指标和查询历史存入 Neo4j，原始数据仍保留在源系统中
- ⚡ 快速开始三步曲：摄取源 schema 到语义图、通过 MCP 服务器暴露工具、让代理检索表与外键后生成并执行 SQL
- 🔌 提供多类连接器：BigQuery Schema/Logs、Dataplex、OSI、CSV、Query Logs，均基于 extract/transform/load 组件
- 🏗️ 统一元数据图模型：Database → Schema → Table → Column → Value，Column 间以 REFERENCES 表示外键
- 🧩 可选嵌入生成：支持 LiteLLM 多提供商或 OpenAI 直连，为表、列、术语等开启语义/向量搜索
- 🖥️ Neocarta CLI（[cli] 附加包）提供摄取命令（如 neocarta bigquery schema）和镜像 MCP 的查询工具
- 🤖 MCP 服务器（neocarta-mcp）提供 list_schemas、混合搜索、业务术语桥接等工具，可接入 Claude Desktop
- 📊 完整 Text2SQL Agent 示例（LangGraph + 双 MCP）可将自然语言问题转为 BigQuery SQL 并返回结果
- 🚀 性能加速器 neo4j-rust-ext 可将批量加载吞吐量提升 60–90%（需 Python ≥3.11）
- 📁 附带 ecommerce（4 表）和 acme（33 表）示例数据集，并可通过 make 命令一键构建和运行
- 🔧 采用 uv 管理依赖，支持按需分组安装；提供 connector contract 和 Claude Code skill 便于添加新连接器

---

### [](https://www.meetup.com/sfpython/events/316322896/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-761-september-3-2026)

**原文标题**: [Ducks and Data -  Sept SF Python at Sentry, Wed, Sep 9, 2026, 6:30 PM   | Meetup](https://www.meetup.com/sfpython/events/316322896/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-761-september-3-2026)

Ducks and Data - 九月旧金山 Python 聚会（Sentry 主办场）是面向 Python 开发者的线下交流活动，时间为 9 月 9 日晚间，地点在旧金山 Sentry 办公室，核心是两场关于数据生成与数据分析的演讲，并设有社交与 Q&A 环节。

- 🐍 SF Python 志愿者组织举办此次活动，旨在促进湾区 Python 社区发展；主持人为 Phebe 和 James。
- 📅 活动于 9 月 9 日（周三）18:30–20:30（PDT）举行，地点为 45 Fremont Street 的 Sentry 办公室。
- 🎤 第一场演讲：Saiteja Jonnalagadda 主讲“使用 Python 生成真实合成数据”，解决真实数据的隐私与访问问题，涵盖统计方法到生成模型，并验证数据有效性与隐私泄露风险。
- 👨‍🔬 Saiteja 是 CVS Health 高级云工程师，有合成医疗数据研究背景，也是 IEEE 会员和 AI 会议审稿人。
- 📊 第二场演讲：Bev Turnbaugh 主讲“利用 Python 进行数据分析”，展示如何从公共等任意数据源摄取数据，让分析水平更进一步。
- 🦆 重点介绍 MotherDuck 的 Flights 功能，即以 Python 程序按 Python 风格灵活操控数据。
- 💼 Bev 长期从事 ETL、数据库与金融数据应用开发，曾参与分布式内存 RDBMS 团队，现为客户提供数据难题支持。
- 📝 议程包括：18:30 社交、19:00 开场及致谢、19:10 演讲与问答 + 休息、20:30 结束并深入交流。
- 💰 活动由 Sentry 赞助，理念为“代码出错，更快修复”。
- 🔗 报名需通过指定 ti.to 链接完成，并欢迎通过 bit.ly/bapyacfp 提交 5/15/25 分钟演讲提案。

---

### [ClePy 九月聚会 - 日志、Postgres 与 Python，2026 年 9 月 8 日 星期二 下午 6:00 | Meetup](https://www.meetup.com/cleveland-area-python-interest-group/events/316359502/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-761-september-3-2026)

**原文标题**: [ClePy September Meetup - Logging, Postgres, and Python, Tue, Sep 8, 2026, 6:00 PM   | Meetup](https://www.meetup.com/cleveland-area-python-interest-group/events/316359502/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-761-september-3-2026)

ClePy 九月线下聚会以“日志、Postgres 与 Python”为主题，由 Cleveland Area Python 用户组在 Happy Dog 举办，包含一场聚焦 Python 日志系统与 PostgreSQL 集成的技术演讲。

- 📅 活动时间：9 月 8 日（周二）下午 6:00–8:00（美东时间）
- 📍 活动地点：Happy Dog（Underdog 地下室），地址为 5801 Detroit Ave, Cleveland, OH
- 👥 主办与主持：Cleveland Area Python User Group（CLEpy），由 Anurag S.和 Eddie C.主持
- 📋 活动流程：6:00–6:30 社交与设备调试、公告；6:30–7:30 演讲；7:30–8:00 社交与清理
- 🎤 演讲主题：Matt Wilson 主讲的“When Logs Become Data: Building a PostgreSQL Logging Handler in Python”
- 🧠 技术要点：通过 logtopg 案例，讲解如何自定义 Python logging handler，将日志存储到 PostgreSQL 并可用 SQL 查询；涵盖 Python logging 基础、数据库 schema 与索引设计、利用 ltree 扩展处理 logger 层级，以及写入失败和日志性能的权衡
- ✅ RSVP 提醒：若已报名但无法到场，请及时取消报名，以便候补者参加
- 📣 演讲征集：如有意向演讲，可在 Meetup 或 Cleveland Tech Slack 的#clepy 频道联系主办方
- 🏆 赞助支持：Python Software Foundation 和 Happy Dog 为本次活动提供支持

---

### [以 Agentic AI 加速企业现代化：走进 AWS Transform，2026 年 9 月 9 日（周三）下午 5:30 | Meetup](https://www.meetup.com/pydata-st-louis/events/316295374/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-761-september-3-2026)

**原文标题**: [Accelerating Enterprise Modernization with Agentic AI: Inside AWS Transform, Wed, Sep 9, 2026, 5:30 PM   | Meetup](https://www.meetup.com/pydata-st-louis/events/316295374/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-761-september-3-2026)

企业遗留系统现代化成本高、周期长，传统手动改造难以应对。AWS Transform 作为首个面向企业现代化改造的代理式 AI 服务，通过能推理、规划与执行的智能代理，帮助分析遗留负载、分解单体架构、跨语言转换代码，并持续修复技术债务。PyData St. Louis 主办本次活动，由 Saurabh Sharma 进行分享。

- 🏦 许多企业仍在运行大型机、.NET 单体应用和复杂数据库，这些遗留代码难以进行模块化变更。
- ⏳ 传统现代化改造通常需要 18 个月以上的人工投入，且精通旧系统的工程师越来越少。
- 🤖 Agentic AI 区别于基于规则的迁移工具，它能对代码转换进行推理、规划和自适应执行。
- 🔄 实际转换模式包括：大型机迁移到云原生、.NET 现代化，以及自定义代码/API/框架转换（涉及 Python）。
- ♻️“持续现代化”理念将技术债修复从一次性项目变成长期自动化、始终在线的能力。
- 🎤 活动包含现场演示和讲解，之后预留 30 分钟用于问答、讨论和社区交流，并提供披萨。
- 👥 适合软件工程师、数据从业者及技术领导，也适合关注 LLM 在生产代码中真实应用的人群。
- 📍 活动由 PyData St. Louis 主办，该社区属于 NumFOCUS 教育项目，当地还涵盖深度学习、数据可视化、Python 机器学习等主题。

---

