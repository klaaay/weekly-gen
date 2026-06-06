### [面向开发者的AI工程 | 博客 | Luca Cavallin](https://www.lucavallin.com/blog/ai-engineering-for-developers?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-748-june-4-2026)

**原文标题**: [AI Engineering for Developers | Blog | Luca Cavallin](https://www.lucavallin.com/blog/ai-engineering-for-developers?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-748-june-4-2026)

### 概述总结
本文为有经验的软件工程师提供了AI工程领域的全面指南，涵盖从基础概念到生产部署的完整技术栈，强调系统思维而非模型本身。

### 关键要点
- 🎯 **AI工程核心转变**：产品不再是模型本身，而是围绕模型构建的系统；AI工程师是后端工程师的扩展，负责接地、评估和成本优化
- 🏗️ **三层技术栈**：应用层（提示词、RAG、代理）→ 模型开发层（微调）→ 基础设施层（GPU、向量数据库），大多数团队应聚焦第一层
- 🔧 **模型适配三步骤**：优先提示工程 → 其次RAG（检索增强生成）→ 最后微调，不要跳过步骤
- 📊 **评估体系**：混合使用程序化指标、LLM-as-judge、人工审查和A/B测试；建立评估流水线是首要任务
- 🧩 **RAG实战要点**：混合搜索（BM25+语义）加重排序是标准配置；注意分块策略和上下文窗口限制
- 🤖 **代理系统设计**：默认使用工作流（固定步骤），仅在需要运行时决策时使用代理；注意无限循环、上下文溢出和工具幻觉等故障模式
- 🔐 **安全防御**：三层防护（输入过滤、输出过滤、代理级约束），没有纯提示词能防御提示注入
- 💰 **成本管理**：使用模型路由（简单请求用便宜模型）、缓存（精确/语义/前缀）和预算控制；不要所有请求都用最贵的模型
- ☁️ **GCP部署路径**：优先Agent Engine → 需要自定义容器或GPU时用Cloud Run → 仅当遇到瓶颈时才用GKE
- 📈 **持续维护**：模型漂移、提示词腐烂、数据变化；需要持续的评估预算和监控，而非一次性开发

---

### [Django：介绍 django-integrity-policy - Adam Johnson](https://adamj.eu/tech/2026/05/31/introducing-django-integrity-policy/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-748-june-4-2026)

**原文标题**: [Django: introducing django-integrity-policy - Adam Johnson](https://adamj.eu/tech/2026/05/31/introducing-django-integrity-policy/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-748-june-4-2026)

Django 新套件 django-integrity-policy 介紹，用於設定 Integrity-Policy 安全標頭，確保所有腳本與樣式表都需有 integrity 屬性，防止供應鏈攻擊。

- 🔒 **新安全標頭支援**：Firefox 145 和 Chrome 138+ 支援 Integrity-Policy 標頭，要求頁面上的腳本與樣式表必須有 integrity 屬性，否則瀏覽器會封鎖載入。
- 🛡️ **防範供應鏈攻擊**：透過子資源完整性（SRI）機制，確保第三方 CDN 內容未被篡改，即使必須使用外部資源也能保障安全。
- ⚙️ **簡潔的設定方式**：套件提供 Django 中介軟體，只需在 MIDDLEWARE 加入並設定 INTEGRITY_POLICY，即可啟用強制 integrity 檢查。
- 📜 **適用所有資源**：Integrity-Policy 不區分第一方或第三方資源，所有腳本與樣式表都需添加 integrity 屬性，包括自託管檔案。
- 🧩 **搭配 django-sri**：使用 Jake Howard 的 django-sri 套件，透過模板標籤自動為靜態檔案產生帶有 integrity 屬性的 HTML 標籤。
- 🤖 **LLM 輔助開發**：作者僅用兩次提示給 Claude，從現有 django-permissions-policy 儲存庫改寫而成，節省數小時重複工作。
- 🌐 **未來發展**：WAICT 倡議將持續擴充 Integrity-Policy 功能，作者計劃跟進更新套件，並觀察是否適合納入 Django 核心。

---

### [使用Python和JavaScript进行网页抓取 – MERN全栈课程 - YouTube](https://www.youtube.com/watch?v=V1JmI5sUc5E&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-748-june-4-2026)

**原文标题**: [Web Scraping with Python & JavaScript – MERN Stack Full Course - YouTube](https://www.youtube.com/watch?v=V1JmI5sUc5E&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-748-june-4-2026)

本頁面為 YouTube 平台的相關資訊與政策總覽，涵蓋版權、聯絡方式、創作者支援及法律條款等核心內容。

- 📰 新聞中心：提供 YouTube 最新動態與官方消息
- ©️ 版權：說明內容使用與版權保護相關規範
- 📞 聯絡我們：提供用戶與平台聯繫的管道
- 🎬 創作者：支援內容創作者的資源與工具
- 📢 刊登廣告：介紹廣告投放與營利相關選項
- ⚖️ 條款：列出使用 YouTube 服務的條款與條件
- 🔒 私隱：說明用戶資料的收集與保護政策
- 🛡️ 政策及安全：規範內容審核與社群安全準則
- ⚙️ YouTube 的運作方式：解釋平台推薦與演算法機制
- 🧪 測試新功能：介紹實驗性功能與用戶測試
- 📅 © 2026 Google LLC：版權歸屬與法律免責聲明

---

### [在Python中打破循环导入而不损失类型安全性 - Orcaset | AI原生金融模型](https://www.orcaset.com/blog/breaking-circular-imports-in-python-without-losing-type-safety?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-748-june-4-2026)

**原文标题**: [Breaking Circular Imports in Python Without Losing Type Safety - Orcaset | AI-Native Financial Models](https://www.orcaset.com/blog/breaking-circular-imports-in-python-without-losing-type-safety?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-748-june-4-2026)

Orcaset 是一个用于构建财务报表模型的框架，通过将行项目定义为函数来处理循环依赖问题，并探讨了在保持类型安全的同时避免循环导入的多种方法。

- 🔄 Orcaset 的核心是将行项目建模为 `line_item(dates) -> value` 函数，直观地映射财务报表结构
- ⚡ 使用延迟执行的公式而非原始数值，以解决循环值依赖并跟踪执行路径
- 🧩 通过直接引用定义依赖关系，但跨文件时会导致循环导入错误
- 🛠️ 推荐使用局部导入（local import）打破循环，在函数体内延迟导入依赖，直到模块完全定义
- 📉 局部导入的缺点：隐藏模块依赖、增加每次函数调用的开销（但Python缓存机制和Orcaset的生成器缓存可忽略）
- 🔁 对于便捷构造函数中的依赖，可使用thunk（返回依赖的函数）替代直接引用
- ❌ 其他方案如上下文字典（缺乏类型安全和静态验证）和构建器模式（增加维护复杂性）各有缺陷
- 🏆 局部导入被视为“最不坏”的方案，具有依赖明确、类型安全、静态完整和简洁的优点

---

### [您的REST API需要Webhooks - YouTube](https://www.youtube.com/watch?v=yc-gp3PFHEI&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-748-june-4-2026)

**原文标题**: [Your REST API Needs Webhooks - YouTube](https://www.youtube.com/watch?v=yc-gp3PFHEI&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-748-june-4-2026)

本頁面列出了 YouTube 平台的核心資訊與政策，涵蓋法律、商業及功能層面，並標示版權年份。
- 📰 新聞中心：提供 YouTube 的最新消息與公告
- ©️ 版權：說明內容使用的版權規範與保護
- 📞 聯絡我們：提供用戶與平台聯繫的管道
- 🎨 創作者：支援內容創作者的工具與資源
- 📢 刊登廣告：介紹廣告投放與營利選項
- 👨‍💻 開發人員：提供 API 與技術開發文件
- 📜 條款：列出使用 YouTube 的服務條款
- 🔒 私隱：說明個人資料的收集與使用方式
- 🛡️ 政策及安全：規範內容與社群安全準則
- ⚙️ YouTube 的運作方式：解釋平台推薦與演算法機制
- 🧪 測試新功能：說明新功能的測試與反饋流程
- ©️ 2026 Google LLC：標示版權歸屬與年份

---

### [PyTorch 自定义操作 - 雷茂的日志](https://leimao.github.io/blog/PyTorch-Custom-Operation/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-748-june-4-2026)

**原文标题**: [PyTorch Custom Operation - Lei Mao's Log Book](https://leimao.github.io/blog/PyTorch-Custom-Operation/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-748-june-4-2026)

本文介绍了如何在 PyTorch 中实现 C++ 和 CUDA 自定义操作（函数与类），并将其用于模型导出（torch.export）和 AOTInductor 编译推理，以简单的恒等卷积为例。

- 🧩 **自定义函数**：通过 `TORCH_LIBRARY_IMPL` 宏注册 CPU 和 CUDA 实现，PyTorch 根据输入设备自动调度。
- 🏛️ **自定义类**：继承 `torch::CustomClassHolder`，通过 `TORCH_LIBRARY` 宏注册，支持参数持有和序列化。
- 🔧 **Python 集成**：加载共享库后，使用 `torch.ops` 和 `torch.classes` 调用自定义操作，并通过 `@register_fake_class` 和 `@torch.library.register_fake` 注册抽象版本以支持 `torch.export` 符号追踪。
- 📦 **模型导出与编译**：使用 `torch.export` 导出模型，再通过 `torch._inductor.aoti_compile_and_package` 编译为 `.pt2` 包，支持 Python 和纯 C++ 推理。
- 🚀 **C++ 推理**：通过 `dlopen` 加载自定义操作库，无需 pybind11 或 libpython，直接运行编译后的模型包。
- ✅ **验证**：恒等模型输出与输入逐位相同，通过 `torch.equal` 验证，支持 CPU 和 CUDA 设备。

---

### [服务器工作原理：TCP套接字实战入门](https://labs.iximiuz.com/tutorials/how-servers-work-tcp-sockets?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-748-june-4-2026)

**原文标题**: [How Servers Work: A Hands-On Introduction to TCP Sockets](https://labs.iximiuz.com/tutorials/how-servers-work-tcp-sockets?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-748-june-4-2026)

本教程通过动手实践，从零构建一个微型TCP服务器和客户端，深入讲解服务器如何工作、TCP套接字原理及网络编程模型。

- 📚 **核心概念**：TCP服务器是一个等待客户端连接、接收输入并返回输出的进程，使用TCP协议进行网络通信，将数据视为有序字节流
- 🔌 **套接字本质**：套接字是操作系统提供的进程间通信（IPC）抽象，允许两个进程通过网络或本地通信，类似现实中的电源插座
- 🧩 **数据传输机制**：TCP通过分块、数据包重组、连接管理和端口号实现可靠、有序、无差错的字节流传输
- 🖥️ **服务器端流程**：创建套接字→绑定地址和端口→监听连接→接受客户端→读写数据→关闭连接，服务器端有N+1个套接字（1个监听套接字+N个客户端套接字）
- 📡 **客户端流程**：创建套接字→连接到服务器→发送数据→关闭写端→接收响应→关闭连接
- ⚠️ **关键注意事项**：recv()和send()操作网络缓冲区，可能不会一次性传输所有数据；需使用sendall()确保完整发送，通过检测recv()返回0字节判断客户端发送完毕
- 🛠️ **实践代码**：提供了完整的Python TCP回显服务器和客户端示例代码，包括套接字创建、绑定、监听、接受连接、数据收发和关闭等核心操作

---

### [Django 6.1 新特性！获取模式、邮件发送器及更多功能 - YouTube](https://www.youtube.com/watch?v=ib9am_m2CnM&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-748-june-4-2026)

**原文标题**: [Django 6.1 New Features! Fetch Modes, Mailers and more... - YouTube](https://www.youtube.com/watch?v=ib9am_m2CnM&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-748-june-4-2026)

本頁面涵蓋 YouTube 平台的核心資訊與政策，包括版權、聯絡方式、創作者支援、廣告、條款及隱私等。

- 📰 **新聞中心**：提供 YouTube 官方新聞與公告。
- ©️ **版權**：說明版權相關規範與保護機制。
- 📞 **聯絡我們**：提供用戶與創作者聯繫 YouTube 的管道。
- 🎨 **創作者**：專為內容創作者提供的資源與支援。
- 📢 **刊登廣告**：介紹廣告投放選項與合作方式。
- 👨‍💻 **開發人員**：針對開發者的 API 與技術文件。
- 📜 **條款**：列出使用 YouTube 服務的條款與條件。
- 🔒 **私隱**：說明用戶資料的收集與使用方式。
- 🛡️ **政策及安全**：涵蓋社群規範與安全措施。
- ⚙️ **YouTube 的運作方式**：解釋平台推薦與演算法機制。
- 🧪 **測試新功能**：介紹 YouTube 正在測試的新功能。
- ©️ **© 2026 Google LLC**：版權聲明，歸 Google 所有。

---

### [模式尖叫者：未知寻址网络中的子网发现](https://ifritnoises.org/articles/pattern-screamer/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-748-june-4-2026)

**原文标题**: [Pattern Screamer: Subnet Discovery in Networks with Unknown Addressing](https://ifritnoises.org/articles/pattern-screamer/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-748-june-4-2026)

本篇文章介绍了一种名为“Pattern Screamer”的工具，用于在未知寻址的网络中进行子网发现，通过TTL追踪和启发式采样，高效地构建网络拓扑图，避免大规模扫描带来的负载和耗时问题。

- 🔍 **核心方法**：利用TTL追踪机制，发送探测包并收集ICMP超时响应，从而发现路由设备及其接口地址。
- 🧩 **启发式采样**：将大型地址空间（如10.0.0.0/8）分割为/24子网，仅探测每个子网中可能的网关地址（如.1和.254），大幅减少探测目标数量（如/16网络从65,536个地址降至512个）。
- 🌐 **多协议支持**：支持ICMP Echo、ICMP Timestamp、TCP SYN和UDP探测，提高对网络过滤的抵抗能力；其中TCP/443和UDP/123常用于绕过ACL限制。
- 📊 **效率验证**：在实验室测试中，对192.168.0.0/16网络进行探测，仅需约25-55秒发送约1,534个探测包，即可发现13个唯一跃点，显著优于传统扫描。
- 🗺️ **结果应用**：生成有向图展示路由结构，并输出潜在子网列表，为后续针对性扫描（如仅扫描发现的/24子网）提供基础，避免盲目扫描。
- ⚠️ **局限性**：依赖网关位置假设（.1或.254），多接口路由器可能显示为多个节点；在严格过滤或“默认拒绝”策略的网络中可能失效；防火墙可能通过修改TTL隐藏自身。

---

### [错误](https://blog.jupyter.org/a-users-journey-with-plugin-playground-from-first-idea-to-installable-jupyterlab-extension-697021dd6fb9?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-748-june-4-2026)

**原文标题**: [Error](https://blog.jupyter.org/a-users-journey-with-plugin-playground-from-first-idea-to-installable-jupyterlab-extension-697021dd6fb9?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-748-june-4-2026)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='blog.jupyter.org', port=443): Max retries exceeded with url: /a-users-journey-with-plugin-playground-from-first-idea-to-installable-jupyterlab-extension-697021dd6fb9?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-748-june-4-2026 (Caused by SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1010)')))

---

### [智能体强化学习：令牌输入，令牌输出的正确实现](https://qgallouedec-tito.hf.space/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-748-june-4-2026)

**原文标题**: [Agentic RL: Token-In, Token-Out Done Right](https://qgallouedec-tito.hf.space/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-748-june-4-2026)

### 概述总结
本文讨论了大语言模型强化学习训练中一个关键但容易被忽视的问题：当模型支持工具调用时，多轮对话的token处理不当会导致梯度信号失效。核心解决方案是遵循"Token-In, Token-Out"（TITO）原则，即永远不对已解码的token进行重新编码。

- 🔄 **单轮RL训练表现良好**：单轮强化学习训练中，模型生成token后直接计算奖励和梯度，过程清晰且收敛稳定
- ⚠️ **多轮工具调用引入问题**：当模型需要调用工具时，传统循环会解码token、解析工具调用、重新编码对话，导致token序列漂移
- 🔍 **Token-In, Token-Out原则**：核心规则是"永远不对已解码的token重新编码"，将模型生成的token直接存入缓冲区作为唯一真理来源
- 🛠️ **工具响应增量技巧**：通过比较有无工具消息的模板渲染结果，计算token增量并直接追加到缓冲区，避免重新编码
- ✅ **前缀保持性检查**：只需验证一个简单属性——追加工具结果后，渲染结果的前缀部分保持不变，绝大多数模型模板已满足此条件
- 📊 **18/19模型通过测试**：对Qwen、DeepSeek、Llama等主流模型测试，仅Qwen3需要一行代码修复即可满足前缀保持性
- 🚫 **历史重写与截断处理**：当模型编辑自身历史或达到长度限制时，TITO原则需要特殊处理，但比传统渲染器方案更简单可靠
- 💡 **正确训练原语**：只要持有token序列，无需重新实现聊天模板，仅需检查工具消息的前缀保持性并正确计算增量

---

### [GitHub - interviewstreet/hiring-agent: 用于评估和评分简历的AI代理。](https://github.com/interviewstreet/hiring-agent?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-748-june-4-2026)

**原文标题**: [GitHub - interviewstreet/hiring-agent: AI agent to evaluate and score resumes. · GitHub](https://github.com/interviewstreet/hiring-agent?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-748-june-4-2026)

Hiring Agent 是一个从简历PDF中提取结构化数据、结合GitHub信号进行公平、可解释评估的AI工具。

- 📄 **核心功能**：将简历PDF转换为Markdown，提取结构化JSON数据，结合GitHub信息进行客观评分
- 🏗️ **架构流程**：PDF提取→LLM分节解析→GitHub数据增强→严格评分→CSV输出
- 🔧 **技术栈**：Python 3.11+，支持Ollama（本地）或Google Gemini（云端）作为LLM后端
- 📁 **关键模块**：`pdf.py`处理PDF，`github.py`获取GitHub数据，`evaluator.py`执行评分，`score.py`协调全流程
- ⚙️ **配置灵活**：通过`.env`文件设置LLM提供商、模型和API密钥，支持开发模式（缓存+CSV导出）
- 🚀 **使用简单**：运行`python score.py /path/to/resume.pdf`即可获得完整评估报告
- 📊 **评分维度**：涵盖开源贡献、个人项目、生产经验和技术技能，包含加分和扣分机制
- 🤝 **开源贡献**：MIT许可证，鼓励贡献者保持提示声明式、跨提供商验证、添加单元测试

---

### [GitHub - nesquena/hermes-webui: Hermes WebUI：在网页或手机上使用Hermes Agent的最佳方式！· GitHub](https://github.com/nesquena/hermes-webui?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-748-june-4-2026)

**原文标题**: [GitHub - nesquena/hermes-webui: Hermes WebUI: The best way to use Hermes Agent from the web or from your phone! · GitHub](https://github.com/nesquena/hermes-webui?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-748-june-4-2026)

Hermes WebUI 是一个轻量级、深色主题的网页界面，用于与 Hermes Agent 交互，提供与命令行几乎一致的功能体验，并支持持久记忆、任务调度、多平台访问等高级特性。

- 🧠 **持久记忆与自我进化** — 代理能跨会话保留上下文、用户配置和技能，并自动从经验中学习与保存新技能，无需重复配置。
- 🗓️ **自托管任务调度** — 支持 cron 定时任务，在离线时执行并通过 Telegram、Discord、邮件等10+平台传递结果。
- 🌐 **多平台与多模型支持** — 同一代理可在终端、手机和网页使用，兼容 OpenAI、Anthropic、Google、DeepSeek 等多种模型提供商。
- 🖥️ **三面板布局与完整功能** — 左侧会话导航、中央聊天、右侧工作区文件浏览器，支持文件编辑、代码高亮、Mermaid 图表渲染、语音输入等。
- 🔒 **安全与认证** — 可选密码和 WebAuthn 通行密钥认证，支持 SSH 隧道和 Tailscale 远程访问，默认绑定本地地址。
- 🐳 **Docker 一键部署** — 提供单容器和多容器 Compose 文件，支持 amd64/arm64，自动处理 UID/GID 映射。
- 🎨 **主题与自定义** — 支持深色/浅色模式及多种皮肤（如 ares、mono、catppuccin 等），可即时切换并持久保存。
- 📱 **移动端响应式** — 手机端通过汉堡菜单和滑出面板保持完整功能，触摸目标最小44px。
- 🧩 **扩展与集成** — 支持管理员控制的 WebUI 扩展注入、CLI 会话桥接、工作区 Git 检测等高级功能。
- 👥 **活跃的开源社区** — 超过190位贡献者，持续迭代更新，提供详细的文档、测试套件和贡献指南。

---

### [GitHub - galilai-group/stable-worldmodel: 可复现世界模型研究与评估平台](https://github.com/galilai-group/stable-worldmodel?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-748-june-4-2026)

**原文标题**: [GitHub - galilai-group/stable-worldmodel: A platform for reproducible world model research and evaluation · GitHub](https://github.com/galilai-group/stable-worldmodel?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-748-june-4-2026)

stable-worldmodel 是一个专为可复现世界模型研究与评估设计的统一平台，提供数据收集、模型训练和模型预测控制评估的全流程支持，包含多种标准化环境和基准实现。

- 📦 提供统一接口，支持世界模型研究的三个核心阶段：数据收集、训练和模型预测控制评估
- 🚀 安装简便，支持 PyPI 安装和源码开发，并可选集成 LeRobot 数据集
- 🧪 快速入门示例清晰展示从数据采集到模型评估的完整流程
- 📊 支持多种数据格式（Lance、HDF5、视频、文件夹、LeRobot），其中 LanceDB 在本地和 S3 上均表现出最高吞吐量
- 🌍 集成丰富环境库，包括 DeepMind Control Suite、Gymnasium、Atari 等，并提供可控制的变化因子用于零样本泛化评估
- 🛠️ 内置多种求解器（CEM、iCEM、MPPI 等）和基线模型（DINO-WM、LeWM 等）
- 💻 提供命令行工具，无需编写代码即可检查、转换数据集和环境
- 📚 完整文档托管于 GitHub Pages，包含 API 参考和教程
- 📝 提供引用格式，便于学术使用

---

### [GitHub - boundless-large-model/boundless-world-model: 用于通用具身智能的高保真世界模型，如数据引擎和世界模拟器。](https://github.com/boundless-large-model/boundless-world-model?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-748-june-4-2026)

**原文标题**: [GitHub - boundless-large-model/boundless-world-model: High-fidelity world models for general embodied intelligence, such as data engines and world  simulators. · GitHub](https://github.com/boundless-large-model/boundless-world-model?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-748-june-4-2026)

Boundless-World-Model（BWM）是一个基于Wan2.2-TI2V-5B构建的高保真、低成本机器人操作视频世界模型，支持动作条件化生成，并具备物理一致性。

- 🌍 **项目概述**：BWM是一个物理一致、动作条件化的视频世界模型，用于机器人操作模拟，基于Wan2.2-TI2V-5B构建。
- 🚀 **最新进展**：已发布推理代码和模型定义（2026年5月），支持生成动作条件化的机器人操作视频。
- ✅ **待办事项**：待发布模型权重、训练代码和技术报告。
- 🧩 **场景1：组合空间重排**：成功处理多对象空间排序、堆叠稳定性和接触丰富的放置任务。
- 🚪 **场景2：铰链交互**：准确捕捉微波炉、笔记本电脑等铰链约束的开启动态和持久对象状态。
- 🕹️ **场景3：细粒度交互**：实现小接触区域、精确放置和状态改变交互（如开关、挂杯）。
- 🤝 **场景4：双臂协调**：模拟同步双臂运动、对象连续性和避免近距离碰撞。
- 📦 **场景5：长时程约束放置**：保持长时程场景连贯性，处理遮挡和稳定约束放置。
- 🎨 **分布外泛化**：能泛化到GPT-Image-2创建的初始场景和对象外观变化，保持动作条件化动态。
- 🛠️ **使用指南**：提供环境设置、模型权重下载和推理脚本，支持快速开始视频生成。
- 🏋️ **训练**：训练代码即将发布。
- 🙏 **致谢**：基于Wan2.2、DiffSynth-Studio、WorldArena等开源项目，感谢工程贡献者。
- 📜 **引用**：鼓励在研究中引用BWM，并给予星标支持。

---

### [GitHub - EverMind-AI/EverOS：跨智能体与平台的自我进化记忆](https://github.com/EverMind-AI/EverOS?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-748-june-4-2026)

**原文标题**: [GitHub - EverMind-AI/EverOS: Self-evolving memory across Agent and platform. · GitHub](https://github.com/EverMind-AI/EverOS?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-748-june-4-2026)

EverOS 是一个开源 Python 框架，为 AI 代理和聊天提供结构化、可检索、自演进的长期记忆，核心设计基于 Markdown 文件、轻量级存储和纯算法库。

- 🧠 **核心功能**：将对话、代理轨迹和文件转化为长期记忆，支持轻量本地部署，无需 MongoDB 等重型数据库。
- 📝 **Markdown 即真理源**：所有记忆以 `.md` 文件持久化，可编辑、搜索、版本控制，无黑盒数据库锁定。
- 🗄️ **三层轻量存储**：Markdown 文件（真理）+ SQLite（状态/队列）+ LanceDB（向量/BM25/标量）。
- ⚙️ **EverAlgo 算法库**：记忆提取算法解耦为独立库，本项目负责编排和持久化。
- 🏗️ **DDD 五层架构**：入口（CLI/HTTP API）→ 服务（用例编排）→ 领域（记忆提取/搜索）→ 基础设施（存储）→ 组件/核心，单向依赖。
- 🚀 **快速启动**：通过 `pip install everos` 安装，`everos init` 生成配置，支持 OpenAI 协议兼容端点。
- 🖼️ **多模态支持**：可选安装后支持图片、PDF、音频、Office 文档（需 LibreOffice）的摄取。
- 📂 **存储布局**：按应用/项目/用户/代理组织，记忆分为可见（episodes）和隐藏（facts/foresights）两类。
- 🔍 **混合检索**：BM25 + 向量（HNSW/IVF-PQ）+ 标量过滤，单查询在 LanceDB 中完成。
- 🔄 **级联索引同步**：编辑 `.md` 文件后，文件监视器触发增量同步，亚秒级完成。
- 🎯 **双轨记忆**：用户轨道（剧集/档案）+ 代理轨道（案例/技能）。
- ⚡ **异步优先**：完全基于 asyncio，单事件循环。
- 📚 **丰富用例**：包括记忆驱动游戏、AI 助手、浏览器代理、多代理编排等 20+ 实际应用。
- 🤝 **开源贡献**：Apache 2.0 许可，欢迎代码、文档、用例、集成等各类贡献。

---

### [GitHub - prathik-arun/考古学家 · GitHub](https://github.com/prathik-arun/archaeologist?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-748-june-4-2026)

**原文标题**: [GitHub - prathik-arun/archaeologist · GitHub](https://github.com/prathik-arun/archaeologist?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-748-june-4-2026)

该工具包提供五种代码库智能分析工具，帮助理解、清理和改进代码库。

- ☠️ **整体概述**：Archaeologist 是一个代码库智能工具包，包含五个工具，支持9种语言，已通过44个开源项目测试，零误报且置信度超过80%。
- 🗺️ **代码库图谱**：生成交互式浏览器地图，按文件夹分组、健康度着色，并显示真实调用关系，可保存为HTML文件共享。
- 💥 **变更影响分析**：分析文件变更的波及范围，包括所有调用者、导入者、测试覆盖率和0-100的风险评分，支持按文件或全局排名。
- 🧮 **复杂度评分**：对每个函数进行圈复杂度评分，按最差到最好排序，可设定最低分数阈值过滤，标签分为极复杂、复杂、中等和简单。
- 🔍 **重复代码检测**：查找代码库中的复制粘贴代码和近似相同的函数，包括同名、完全复制和85%以上相似度的函数体。
- 💀 **死代码查找**：结合调用图和Git历史识别未使用函数，支持自动删除、运行测试并创建PR，置信度评分基于调用图、Git年龄、作者数等信号。
- 🛡️ **安全清理流程**：自动清理在隔离分支上进行，不触及主分支，测试通过后自动创建PR，失败则删除分支，支持一键回滚。
- 🌐 **语言支持**：Python、Dart/Flutter、JavaScript、TypeScript已生产测试，Go、Java、Kotlin、Ruby、Rust、Swift处于Beta阶段。
- 📋 **要求与许可**：需要Python 3.11+和Git，可选GitHub令牌用于自动PR功能，采用MIT许可证。

---

### [GitHub - MordechaiHadad/rustgate: 一个基于Rust的、支持令牌感知的FastAPI速率限制器 · GitHub](https://github.com/MordechaiHadad/rustgate?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-748-june-4-2026)

**原文标题**: [GitHub - MordechaiHadad/rustgate: A rust powered token-aware rate limiter for FastAPI · GitHub](https://github.com/MordechaiHadad/rustgate?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-748-june-4-2026)

Rustgate 是一个基于 Rust 的 FastAPI 后端，利用 PyO3 扩展实现 AI token 感知的速率限制，并依赖 Redis 进行滑动窗口限流。

- 🔧 **架构**: 包含 Rust 绑定（bindings/）和 FastAPI 后端（backend/），通过 PyO3/maturin 实现 Python 与 Rust 交互
- 🚀 **快速启动**: 使用 `uv sync` 安装依赖并构建 Rust 扩展，`uv run uvicorn` 启动服务器
- ⚙️ **环境配置**: 通过 `RUSTGATE_REDIS_URL` 环境变量配置 Redis 连接，默认地址为 `redis://127.0.0.1:6379/0`
- 📡 **API 端点**: 提供 GET `/health` 健康检查，以及 POST `/models/auto`、`/models/gpt-5`、`/models/gpt-4` 等模型路由端点
- 🛡️ **速率限制**: 基于滑动窗口（10 分钟）和 IP 识别，总预算 5000 单位，gpt-4 每 token 1 单位，gpt-5 每 token 25 单位
- 🧮 **Token 计数**: 使用 tiktoken-rs 库，gpt-4 用 Cl100kBase 分词器，gpt-5 用 O200kBase 分词器，零 token 查询绕过限制
- 📊 **性能基准**: 负载测试显示 `/models/auto` 端点平均延迟 88.76ms，每秒处理 1128 请求；`/health` 端点平均延迟 66.90ms，每秒处理 1496 请求
- ❌ **模型支持**: 仅支持 gpt-4 和 gpt-5 系列，不支持 gpt-4o、gpt-4o-mini、gpt-5-mini 或 o3 等模型

---

### [GitHub - Vae-Scrooge/remote-cmd: 一个轻量级Python CLI+API，用于通过SSH管理服务器。支持添加主机、运行命令、传输文件、按标签分组目标——无需Ansible DSL。](https://github.com/Vae-Scrooge/remote-cmd?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-748-june-4-2026)

**原文标题**: [GitHub - Vae-Scrooge/remote-cmd: A lightweight Python CLI + API for managing servers over SSH. Add hosts, run commands, transfer files, target groups by tags — no Ansible DSL required. · GitHub](https://github.com/Vae-Scrooge/remote-cmd?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-748-june-4-2026)

Remote CMD 是一个轻量级的Python CLI和API工具，用于通过SSH管理服务器，支持添加主机、运行命令、传输文件以及按标签分组操作，无需Ansible DSL或复杂脚本。

- 🚀 **快速安装与使用**：通过 `pip install remote_cmd_manager` 一键安装，并可用 `remote-cmd host add` 和 `remote-cmd run` 等命令快速添加服务器并执行命令。
- 🖥️ **批量操作与标签分组**：支持 `batch-run` 命令按标签（如 `production`）跨多台服务器批量运行命令，例如检查磁盘空间或日志。
- 📁 **文件传输功能**：内置SFTP上传和下载功能，可轻松传输文件，如更新nginx配置。
- 🐍 **Python API集成**：提供SSHClient和HostManager等类，允许在自定义脚本中执行命令、传输文件和列出目录。
- 🔒 **多种认证方式**：支持密码、密钥文件和ssh-agent认证，确保连接安全。
- 📊 **主机管理CRUD**：支持创建、读取、更新和删除主机，并持久化到JSON或YAML文件。
- 🎯 **标签系统**：通过标签（如 `web`、`db`）过滤主机，实现精准操作。
- ✅ **类型安全与测试**：完整的类型注解和mypy严格检查，保证代码质量。
- 📚 **丰富文档**：提供API参考、快速入门教程、高级教程、开发指南和故障排除等文档。
- ⭐ **开源与贡献**：MIT许可证，欢迎贡献，鼓励GitHub上标星支持。

---

### [GitHub - Mergifyio/alembic-git-revisions: 基于Git提交历史自动链式管理Alembic迁移](https://github.com/Mergifyio/alembic-git-revisions?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-748-june-4-2026)

**原文标题**: [GitHub - Mergifyio/alembic-git-revisions: Automatic Alembic migration chaining based on git commit history · GitHub](https://github.com/Mergifyio/alembic-git-revisions?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-748-june-4-2026)

alembic-git-revisions 是一个开源工具，通过 Git 提交历史自动解决 Alembic 数据库迁移中的多分支冲突问题，避免手动修复。

- 🚀 **解决问题**：自动处理 Alembic 的“Multiple head revisions”错误，无需手动 rebase 或修改 down_revision
- 🔗 **工作原理**：基于 `git log` 确定迁移文件首次提交顺序，自动线性链接动态迁移，兼容已有静态迁移
- ⚙️ **安装与配置**：通过 `pip install` 安装，替换 Alembic 的 `script.py.mako` 模板，使用 `get_down_revision()` 自动生成链
- 🐳 **无 Git 环境支持**：在 Docker 或 CI 中，通过 `alembic-git-revisions` 命令预生成 `revision_chain.json` 文件，需完整 Git 历史
- 📂 **迁移类型**：支持动态（自动链）、静态（手动管理）和混合（链接动态迁移）三种分类
- 🛠️ **API 功能**：提供 `get_down_revision()`、`generate_chain_file()` 和 `build_chain()` 函数，支持缓存清除
- 📜 **许可证**：Apache-2.0 开源许可

---

### [Django 安全版本发布：6.0.6 和 5.2.15 | 博客 | Django](https://www.djangoproject.com/weblog/2026/jun/03/security-releases/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-748-june-4-2026)

**原文标题**: [Django security releases issued: 6.0.6 and 5.2.15 | Weblog | Django](https://www.djangoproject.com/weblog/2026/jun/03/security-releases/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-748-june-4-2026)

Django 发布了安全更新版本 6.0.6 和 5.2.15，修复了五个低严重性安全漏洞，建议所有用户尽快升级。

- 🔒 CVE-2026-6873: 修复了 `get_signed_cookie()` 中签名盐值命名空间冲突问题，防止不同 cookie 名称和盐值组合产生相同拼接结果导致的安全风险。
- 📧 CVE-2026-7666: 修复了 SMTP 后端中 `STARTTLS` 握手失败时可能以未加密方式发送电子邮件的漏洞，仅影响使用 `EMAIL_USE_TLS` 且 `fail_silently=True` 的情况。
- 🗄️ CVE-2026-8404: 修复了 `UpdateCacheMiddleware` 中因 `Cache-Control` 指令大小写敏感而错误缓存标记为私有的响应的问题。
- 🔑 CVE-2026-35193: 修复了 `UpdateCacheMiddleware` 中缺少 `Vary: Authorization` 导致带有 `Authorization` 头的响应被缓存的问题。
- 🚫 CVE-2026-48587: 修复了 `Vary` 头值中存在前导或尾随空格时缓存响应不正确的漏洞，特别是 `Vary: *` 带空格的情况。

---

### [GitHub Python 交流会，2026年6月10日星期三下午5:30 | Meetup](https://www.meetup.com/psppython/events/314760102/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-748-june-4-2026)

**原文标题**: [Python talk night at GitHub, Wed, Jun 10, 2026, 5:30 PM   | Meetup](https://www.meetup.com/psppython/events/314760102/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-748-june-4-2026)

本次Python讲座之夜由PuPPy主办，在GitHub Bellevue办公室举行，包含三场技术演讲和社交环节。

- 🐍 活动由Puget Sound Programming Python (PuPPy) 主办，在GitHub Bellevue办公室举行
- 📅 时间：6月10日周三，下午5:30-7:30 PDT，之后有After Party
- 🎤 演讲1：用Circuit Python和Django实现嵌入式设备与浏览器双向通信
- 🐕 闪电演讲：通过狗名数据揭示西雅图社区身份（使用NetworkX、Wikidata等）
- 🌾 演讲2：从农田到API的全栈数据科学，涉及Polars、GPyTorch、FastAPI等技术
- 🍕 赞助商提供食物，但活动本身不提供餐食
- 🚪 电梯6点后关闭，迟到可能无法入场
- 🅿️ 有付费停车场，建议使用公共交通

---

### [ChiPy 2026年6月__main__会议，2026年6月11日星期四下午6:00 | Meetup](https://www.meetup.com/_chipy_/events/315062701/)

**原文标题**: [ChiPy June 2026 __main__ Meeting, Thu, Jun 11, 2026, 6:00 PM   | Meetup](https://www.meetup.com/_chipy_/events/315062701/)

ChiPy 2026年6月主要会议将于6月11日在Expedia举办，内容包括网络安全讲座和社交活动。

- 📅 会议时间：2026年6月11日（周四）下午6点至8点，提供餐饮，讲座6:30开始
- 🏢 主办方：Expedia，地点在芝加哥500 W Madison St Suite 700
- 🛡️ 主题演讲：关于"Mini Shai Hulud"恶意软件，它从npm扩散到PyPI，窃取开发者凭证，适合新手
- 🆔 参会要求：需提供全名和邮箱用于安全验证，现场需在3楼领取二维码并扫描通过闸机和电梯
- 🔗 更多信息：chipy.org/meetings/1113/ 及 LinkedIn页面

---

### [通过张量网络实现高效神经网络，2026年6月8日（周一）下午5:30 | Meetup](https://www.meetup.com/pydata-st-louis/events/314762089/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-748-june-4-2026)

**原文标题**: [Efficient Neural Networks Through Tensor Networks, Mon, Jun 8, 2026, 5:30 PM   | Meetup](https://www.meetup.com/pydata-st-louis/events/314762089/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-748-june-4-2026)

本次活动介绍如何利用张量网络提升神经网络效率，并包含技术讲解与社区交流。

- 🧠 **张量网络基础**：讲解张量网络的概念及其重要性，源自物理学和科学计算。
- ⚖️ **现代AI挑战**：指出当前神经网络在规模、计算成本和内存方面的瓶颈。
- 🔗 **压缩技术**：介绍矩阵乘积态（MPS）和张量列车等分解方法，用于压缩信息。
- 📉 **参数优化**：展示张量网络如何在保持性能的同时减少神经网络参数。
- 💻 **Python实践**：提供实际示例和演示，便于初学者理解应用。
- 🔬 **应用领域**：涵盖机器学习、科学计算等场景，强调跨学科价值。
- 🍕 **活动安排**：5:30 PM开始披萨和社交，6:15 PM演讲，6:50 PM讨论与交流。
- 👥 **适合人群**：对数据科学、机器学习、高效AI或科学计算感兴趣的学生、专业人士及爱好者。

---

### [PyData 2026年6月11日聚会，2026年6月11日（周四）下午6:00 | Meetup](https://www.meetup.com/pydata-hamburg/events/314757285/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-748-june-4-2026)

**原文标题**: [PyData June 11th 2026 Meetup, Thu, Jun 11, 2026, 6:00 PM   | Meetup](https://www.meetup.com/pydata-hamburg/events/314757285/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-748-june-4-2026)

PyData 2026年6月11日聚会由Sanchit B.和Zeinab主持，在汉堡Accenture举办，包含两场精彩演讲和社交环节。

- 📅 活动时间：2026年6月11日（周四）18:00-21:00，地点在汉堡Accenture
- 🎤 第一场演讲：Sahra Klünder探讨“AI采用悖论”，指出企业失败常因缺乏数据访问、API和治理等基础条件，而非AI能力不足
- 💡 第二场演讲：Artur Galstyan分享从95%代码由AI编写到保持编程技能的转变，提出日常练习和决策树方法
- 🍕 活动安排：18:00开门，18:30简短介绍，之后有演讲、问答和社交茶歇
- 🔗 相关主题：机器学习、数据分析、Python数据科学和开源

---

### [PyData 特拉维夫 @ Melio，2026年6月14日（周日）下午6:00 | 聚会](https://www.meetup.com/pydata-tel-aviv/events/314608590/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-748-june-4-2026)

**原文标题**: [PyData Tel Aviv @ Melio, Sun, Jun 14, 2026, 6:00 PM   | Meetup](https://www.meetup.com/pydata-tel-aviv/events/314608590/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-748-june-4-2026)

PyData Tel Aviv 聚会将于 2026 年 6 月 14 日在 Melio 办公室举办，包含三场关于 AI 和机器学习的演讲，并提供社交与餐饮。

- 📅 活动时间与地点：2026 年 6 月 14 日（周日）18:00-21:00，于 Tel Aviv 的 Melio 办公室（Hagag Towers 北塔 32 层）举行，语言为希伯来语。
- 🍕 活动流程：18:00 开始签到与餐饮，18:30 欢迎致辞，随后进行三场主题演讲。
- 🤖 演讲一：Shon Mendelson 分享如何结合向量搜索与小型模型，实现 LLM 级别的判断速度，用于大规模实体匹配。
- 💡 演讲二：Dr. Adi Sarid 讲述市场研究机构从依赖 GenAI 到建立评估框架的历程，强调 AI 扩展中的挑战与经验。
- ⚙️ 演讲三：Michael Levinger 探讨通过缓存、模型路由、蒸馏等技术优化 LLM 系统的成本与性能，并对比 Gemini、Claude、GPT 等模型。
- 🚀 报名与交通：名额有限需提前 RSVP，建议使用公共交通，驾车可参考附近停车场列表。

---

