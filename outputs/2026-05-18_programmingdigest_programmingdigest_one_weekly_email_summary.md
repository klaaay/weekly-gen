### [GPS 到底是怎么工作的？（互动探索）](https://perthirtysix.com/how-the-heck-does-gps-work)

**原文标题**: [How The Heck Does GPS Work? (An Interactive Exploration)](https://perthirtysix.com/how-the-heck-does-gps-work)

### 概述摘要
GPS 通过将时间转换为距离来定位，利用卫星信号、时钟校正和相对论效应实现精确导航。

- 🌍 **基本原理**：GPS 将时间转化为距离，1 纳秒信号延迟对应 0.3 米距离。
- 📡 **单卫星定位**：一颗卫星只能确定你位于地球表面的一个环上，无法给出精确位置。
- 🔗 **三卫星定位**：三颗卫星的环相交于唯一一点，通过三边测量法确定位置。
- ⏱️ **时钟问题**：手机时钟精度低，需第四颗卫星校正时钟误差，使所有球面交于一点。
- ⚛️ **相对论修正**：卫星时钟因速度和引力产生偏差，需硬件调整（每秒慢 0.00457 秒）以避免每日约 10 公里的定位误差。
- 🛰️ **实际应用**：现代 GPS 通常锁定 8-12 颗卫星，结合多系统（如 GLONASS、Galileo）和几何精度因子优化，减少城市中的多路径误差。

---

### [你的 CI/CD 需要拯救](https://www.jetbrains.com/teamcity/migrate-from-jenkins/?utm_source=newsletter_programming_digest&utm_medium=cpc&utm_campaign=TC-programming-digest-may26)

**原文标题**: [Your CI/CD needs rescue](https://www.jetbrains.com/teamcity/migrate-from-jenkins/?utm_source=newsletter_programming_digest&utm_medium=cpc&utm_campaign=TC-programming-digest-may26)

TeamCity 是一款持续集成和部署工具，提供免费试用版本，帮助团队自动化构建、测试和发布流程。

- 🛠️ 支持自动化构建与测试流程，提升开发效率
- 🚀 提供持续部署功能，简化软件发布过程
- 🆓 可免费试用，降低团队入门门槛
- 🔄 集成版本控制，支持多种代码仓库
- 📊 提供实时构建状态监控与报告

---

### [学习软件架构](https://matklad.github.io/2026/05/12/software-architecture.html)

**原文标题**: [Learning Software Architecture](https://matklad.github.io/2026/05/12/software-architecture.html)

### 概述总结
软件架构设计的最佳学习方式是通过实践，而非理论。核心挑战在于理解社会激励结构对软件架构的影响（康威定律），并学会在现实约束下适应或调整这些结构。个人成长需结合动手实践、关键资源（如边界演讲、测试方法）以及对组织动态的深刻理解。

- 📚 **实践出真知**：软件设计必须通过实际项目学习，理论课程和模拟项目（如大学设计课）效果有限，真实项目中的错误和领导经验才是关键。
- 🏛️ **康威定律的启示**：软件架构复制组织的社会结构，代码的重要性低于架构，而架构又低于社会问题。科研代码与工业代码的差异源于激励结构（如论文发表压力），而非技术知识。
- ⚖️ **适应激励结构**：要么抓住机会调整项目激励（如 TIGER_STYLE 的社会背景），要么接受无法改变的现实，在约束下做到最好。例如 rust-analyzer 通过分离核心与外围功能，吸引不同贡献者。
- 🔧 **具体实践策略**：rust-analyzer 通过稳定构建、秒级测试和`catch_unwind`隔离错误，降低贡献门槛；核心代码则严格把控质量，体现了对激励结构的主动适应。
- 📖 **关键学习资源**：推荐 Gary Bernhardt 的《边界》演讲（提供具体建议）、测试方法论（需批判传统教条）、Pieter Hintjens 的康威定律思考、Jamii 的十年编码反思（元认知），以及 Ted Kaminski 博客（系统化软件开发理论）。
- ⚠️ **不确定性警示**：适应激励结构时需注意未来不可预测，例如 rust-analyzer 原本作为实验项目，最终却成为长期维护的编译器，类似 uutils 从学习项目演变为 Ubuntu 核心工具。

---

### [关于渲染天空、日落与行星——马克西姆·赫克尔博客](https://blog.maximeheckel.com/posts/on-rendering-the-sky-sunsets-and-planets/)

**原文标题**: [On Rendering the Sky, Sunsets, and Planets - The Blog of Maxime Heckel](https://blog.maximeheckel.com/posts/on-rendering-the-sky-sunsets-and-planets/)

以下是您提供的文章内容的摘要：

本篇文章详细介绍了如何在浏览器中通过着色器实现逼真的天空渲染，涵盖大气散射、日落效果及行星大气层渲染，并探讨了基于查找表（LUT）的性能优化方法。

- 🌅 **核心目标**：通过着色器实时渲染出与真实照片媲美的天空效果，包括蓝色天空、日落色彩及行星大气层。
- 🔭 **基本原理**：利用光线步进（Raymarching）模拟光线在大气中的传播，计算透射率（Transmittance）和散射（Scattering）。
- 🎨 **关键散射模型**：瑞利散射（Rayleigh）决定蓝色天空；米氏散射（Mie）产生雾霾和太阳光晕；臭氧吸收（Ozone）为天空增添紫色调。
- 🌍 **行星大气渲染**：通过射线 - 球体相交检测，将天空着色器扩展为后处理特效，实现行星周围的大气层效果。
- 🌞 **动态光照**：引入光源步进（Light Marching）计算太阳光到达采样点的透射率，支持渲染日出、日落及日食效果。
- 🪐 **跨行星模拟**：通过调整常数（如行星半径、散射系数），可模拟火星等其他行星的大气特征。
- ⚡ **性能优化**：采用基于查找表（LUT）的方法，将昂贵的散射计算预存为纹理，大幅提升渲染效率。
- 🛠️ **实现细节**：包括世界空间坐标重建、对数深度缓冲处理、以及天空视图和空中透视 LUT 的生成与合成。

---

### [电子邮件太疯狂了](https://samkhawase.com/blog/email-is-crazy/)

**原文标题**: [Email is crazy](https://samkhawase.com/blog/email-is-crazy/)

### 概述总结
电子邮件系统虽然复杂且充满历史遗留问题，但每天仍能可靠地处理数十亿封邮件，其设计缺陷通过多层补丁式安全机制勉强维持运行。

- 📧 **邮件发送流程**：用户客户端仅负责提交邮件，随后由邮件传输代理（MTA）通过 DNS 的 MX 记录查找收件服务器，并使用 SMTP 协议传输。邮件本质上是异步队列系统，支持重试机制（指数退避最长 5 天）。
- 🔍 **安全漏洞**：SMTP 允许“信封地址”（MAIL FROM）与“邮件头地址”（From）不一致，这一设计源于早期学术网络的信任假设，成为钓鱼和垃圾邮件的根源。
- 🛡️ **三层安全补丁**：SPF（授权 IP 列表）、DKIM（加密签名）、DMARC（策略对齐）共同验证发件人身份，但三者配置复杂且存在缺陷（如 SPF 在转发时失败、DKIM 签名无过期时间）。
- 🚨 **过滤与防火墙**：邮件需通过 IP 信誉、域名互动、内容分析、病毒扫描、URL 拦截等多层过滤，但规则不透明，且新服务器需数周建立信誉。
- 🔒 **加密的妥协**：邮件使用“机会性 TLS”，若接收方不支持则回退为明文；加密仅保护传输层，服务器仍可读取内容，端到端加密（如 S/MIME）普及率低。
- 📬 **最终命运**：邮件可能被正常投递、静默移入垃圾箱（无通知），或被直接拒绝。RFC 5321 允许服务器接受后丢弃邮件，这是交易邮件发送者的噩梦。

---

### [如果 AI 写你的代码，为什么还要用 Python？ | 作者：Noah Mitchem | 2026 年 4 月 | Medium](https://medium.com/@NMitchem/if-ai-writes-your-code-why-use-python-bf8c4ba1a055)

**原文标题**: [If AI Writes Your Code, Why Use Python? | by Noah Mitchem | Apr, 2026 | Medium](https://medium.com/@NMitchem/if-ai-writes-your-code-why-use-python-bf8c4ba1a055)

### 概述总结
AI 的进步正在改变编程语言的选择逻辑：过去开发者因易用性和生态选择 Python/TypeScript，如今 AI 擅长编写 Rust、Go 等高性能语言，使得“难学但高效”的语言成为新趋势。这导致大量项目从 Python/JS 迁移到 Rust/Go，生态优势被削弱，AI 辅助开发成为常态。

- 🤖 **AI 擅长“难语言”**：Rust、Go 等强类型语言因编译器反馈循环紧密，AI 能自我纠错，生成质量优于 Python/JS。微软用 Go 重写 TypeScript 编译器，速度提升 10 倍。
- 🚀 **实际案例激增**：Anthropic 用 AI 编写 Rust 版 C 编译器（10 万行代码，成本$20K）；Rust 专家两周内用 AI 构建新语言；Ladybird 浏览器引擎从 C++ 移植到 Rust 仅用两周。
- 🔄 **生态优势被侵蚀**：Python/JS 的生态（如 PyPI、npm）逐渐被 Rust 底层库取代（如 Polars、uv）。AI 使“移植库”比“修复补丁”更高效（45 分钟完成跨语言移植）。
- ⚠️ **例外与局限**：PyTorch 仍主导 AI 研究；Zig、Haskell 等小众语言 AI 支持不足；部分场景（如无服务器）仍需轻量方案。
- 🏆 **永久性转变**：开发者角色从“写代码”转向“架构与审核”，语言选择标准从“人类易用”变为“AI 易用”。Rust 连续十年最受赞赏，AI 工具使团队无需掌握 Rust 即可交付高性能应用。

---

### [不良软件设计的症状 - 作者：Marcos F. Lobo 🗻🧭](https://newsletter.optimistengineer.com/p/symptoms-of-bad-software-design)

**原文标题**: [Symptoms of Bad Software Design - by Marcos F. Lobo 🗻🧭](https://newsletter.optimistengineer.com/p/symptoms-of-bad-software-design)

以下是您提供的文章内容摘要，使用指定模板整理为中文要点：

软件设计不良的四个信号：僵硬性、脆弱性、不动性和粘滞性，以及相应的解决方案。

- 🔒 **僵硬性**：系统难以修改，一个模块的变更会引发连锁反应。解决方案是使用策略模式解耦，遵循开闭原则，新增功能时不修改现有代码。
- 💥 **脆弱性**：修改一处代码导致多处意外故障，常因隐藏依赖或全局状态引起。解决方案是封装和接口隔离，让每个模块只访问所需部分。
- 🧱 **不动性**：代码难以复用，因与特定环境（如 UI、数据库）紧密耦合。解决方案是分层架构，将业务逻辑提取为纯对象，通过依赖反转分离实现细节。
- 🧈 **粘滞性**：系统促使开发者选择捷径而非正确方式，因正确路径耗时或环境低效。解决方案是自动化工具和基础设施优化，让“正确方式”变得轻松快捷。

---

