### [GitHub - lirantal/pypi-security-best-practices: PyPI 注册表包管理器安全最佳实践集锦，涵盖 uv 与 pip · GitHub](https://github.com/lirantal/pypi-security-best-practices?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-741-april-16-2026)

**原文标题**: [GitHub - lirantal/pypi-security-best-practices: Collection of PyPI registry package manager Security Best Practices featuring uv and pip · GitHub](https://github.com/lirantal/pypi-security-best-practices?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-741-april-16-2026)

本文档提供了全面的 PyPI 安全最佳实践指南，旨在帮助开发者和管理员防范供应链攻击、保护 Python 包的使用和发布安全。内容涵盖包管理器配置、依赖管理、漏洞扫描、CI/CD 安全及维护者安全措施等多个方面。

- 🛡️ **优先二进制安装**：配置包管理器优先使用预编译的 wheel 包，避免安装源码包（sdist）时执行潜在的恶意代码。
- ⏳ **安装冷却期**：为新发布的包设置冷却期（如 3-7 天），以降低安装到刚发布即被发现的恶意版本的风险。
- 🔐 **依赖锁定与哈希验证**：使用锁文件（如`uv.lock`）并启用哈希验证，确保安装的包内容未被篡改。
- 🔄 **确定性安装**：在生产环境和 CI/CD 中使用冻结的锁文件安装，确保每次安装的依赖版本完全一致。
- 🚫 **防止依赖混淆**：在使用私有仓库时，配置包管理器（如 uv 的“首次匹配”策略）确保内部包优先于公共 PyPI 解析。
- 🔍 **漏洞扫描**：集成`pip-audit`或`uv-secure`等工具到 CI/CD 中，持续扫描依赖中的已知安全漏洞。
- 🛡️ **安装加固工具**：使用如 Socket Firewall (`sfw`) 等工具，在安装前实时拦截被标记为恶意的包。
- 🔑 **避免明文密钥**：不使用`.env`文件存储明文密钥，改用 1Password、Infisical 等密钥管理工具动态注入。
- 📦 **开发容器隔离**：使用开发容器（Dev Containers）进行本地开发，将包安装和执行限制在沙箱环境中，降低主机风险。
- ✅ **启用双因素认证**：为 PyPI、GitHub 等所有相关账户启用双因素认证（2FA），优先使用物理安全密钥。
- 🔗 **可信发布**：使用基于 OIDC 的可信发布（Trusted Publishing）替代长期有效的 API 令牌，消除令牌泄露风险。
- 📜 **包来源证明**：发布时启用包来源证明（Attestations），为包提供可验证的构建来源和完整性证明。
- 🛠️ **CI/CD管道安全**：固定 GitHub Actions 到提交 SHA、使用最小权限、审计工作流（如用`zizmor`）、手动批准发布流程。
- 🌳 **减少依赖树**：设计包时尽量减少外部依赖，优先使用 Python 标准库，以降低攻击面和维护负担。
- 📋 **生成 SBOM**：在构建时生成软件物料清单（SBOM），便于在出现漏洞或攻击时快速评估影响。
- 📊 **查询漏洞数据库**：在采用新包前，通过 Snyk、OSV 等数据库检查其安全状况、维护状态和社区健康度。
- 🔎 **验证已发布包内容**：不要仅依赖 PyPI 页面或 GitHub 源码，应下载并检查实际发布的包内容，优先选择带有来源证明的包。

---

### [Python 中的状态模式——我喜欢这样的实现方式 - YouTube](https://www.youtube.com/watch?v=OeirQdzYdnc&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-741-april-16-2026)

**原文标题**: [The State Pattern in Python - I Like How This Turned Out - YouTube](https://www.youtube.com/watch?v=OeirQdzYdnc&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-741-april-16-2026)

该文本为 YouTube 网站底部的通用信息与链接列表，概述了平台的功能、政策与公司信息。

- 📄 关于平台的基本信息与公司介绍
- 📰 新闻与媒体相关资源
- ©️ 版权声明与知识产权
- 📞 联系与反馈渠道
- 🧑‍🎨 内容创作者相关资源
- 💼 广告与商业合作
- 👨‍💻 开发者工具与资源
- 📜 服务条款与使用协议
- 🔒 隐私政策与数据保护
- ⚙️ 平台运作机制说明
- 🧪 新功能测试与更新
- 🏢 谷歌母公司及年份信息

---

### [追踪 Python 中 Celery 任务失败的方法 | AppSignal 博客](https://blog.appsignal.com/2026/04/09/tracking-celery-task-failures-in-python.html?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-741-april-16-2026)

**原文标题**: [Tracking Celery Task Failures in Python | AppSignal Blog](https://blog.appsignal.com/2026/04/09/tracking-celery-task-failures-in-python.html?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-741-april-16-2026)

本文介绍了在 Python 中使用 Celery 处理后台任务时，任务失败可能被默认设置隐藏的问题，并展示了如何通过 AppSignal 监控工具来有效追踪和调试这些失败。

- 🐇 Celery 是 Python 中处理后台任务的主流工具，但默认设置可能导致任务失败被重试机制掩盖，难以从日志中及时发现。
- 📉 Celery 内置重试机制，任务失败时可能自动重试多次才成功，使系统表面正常但实际存在隐藏错误。
- 📜 默认情况下，Celery 将错误信息输出到工作进程日志中，缺乏集中监控界面，在分布式系统中难以排查。
- 🔍 AppSignal 能自动监控 Celery 任务，捕获每次执行的异常、重试次数和性能指标，提供结构化错误展示。
- 📊 通过 AppSignal 仪表盘，可以直观查看任务失败分组、异常追踪、任务上下文和运行环境等详细信息。
- ⚠️ 需警惕的任务异常模式包括：重试风暴、单个任务拖慢整个队列、外部依赖故障等。
- 🚨 有效的警报应关注错误率突增、新异常类型出现、任务执行时间异常等高价值信号。
- 💳 示例中，支付任务因特定银行卡类型失败，通过 AppSignal 快速定位到 Stripe API 验证问题。
- 🛠️ 使用 AppSignal 等可观测性平台，能帮助团队实时发现任务失败，提升分布式系统的调试效率。

---

### [Python 类型检查器对比：速度与内存占用 | Pyrefly](https://pyrefly.org/blog/speed-and-memory-comparison/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-741-april-16-2026)

**原文标题**: [Python Type Checker Comparison: Speed and Memory Usage | Pyrefly](https://pyrefly.org/blog/speed-and-memory-comparison/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-741-april-16-2026)

本文比较了 Pyrefly、Ty、Pyright 和 Mypy 四种 Python 类型检查器在速度和内存使用上的性能表现，基于对 53 个流行开源包的测试。结果显示，新一代基于 Rust 的检查器（Pyrefly 和 Ty）在速度和内存效率上显著优于传统工具（Pyright 和 Mypy），尤其在大规模项目中优势明显。

- 🚀 **性能大幅领先**：Pyrefly 和 Ty 在大多数测试包中比 Pyright 和 Mypy 快 10-50 倍，内存占用也更低。
- ⚙️ **架构影响性能**：Pyrefly 和 Ty 采用 Rust 编写，相比 Python（Mypy）和 TypeScript（Pyright）的实现有天然速度优势；两者内部架构差异也影响了内存管理效率。
- 📦 **包类型影响显著**：科学计算包（如 scipy、pandas）因包含大量重载和联合类型，对检查器挑战最大，性能差异也最明显。
- 🔍 **功能与速度的权衡**：Pyrefly 默认启用返回类型推断等高级功能以提升类型安全，但通过限制联合类型宽度等机制平衡性能成本。
- 📊 **测试与方法**：性能数据来自每日自动运行的基准测试，涵盖 53 个包，在 GitHub Actions 和本地 M4 MacBook 上执行，确保结果可重现。
- 🛠️ **持续优化中**：Pyrefly 近期通过改进实现了速度翻倍和内存占用下降，开发团队认为仍有进一步优化空间。
- 🤖 **快速检查的重要性**：在 AI 辅助编程时代，快速的类型检查能提升开发效率，尤其对于大型代码库和持续集成环境。
- 📈 **如何选择检查器**：除性能外，还需考虑类型规范符合度、推断能力、IDE 支持及社区生态等因素；所有基于 Rust 的新检查器都能提供高速体验。

---

### [错误](https://www.youtube.com/watch?v=yyX0QoUzoE4&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-741-april-16-2026)

**原文标题**: [Error](https://www.youtube.com/watch?v=yyX0QoUzoE4&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-741-april-16-2026)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='www.youtube.com', port=443): Max retries exceeded with url: /watch?v=yyX0QoUzoE4&utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-741-april-16-2026 (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [我们为何还未成为紫外线？](https://aleyan.com/blog/2026-why-arent-we-uv-yet/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-741-april-16-2026)

**原文标题**: [Why aren't we uv yet?](https://aleyan.com/blog/2026-why-arent-we-uv-yet/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-741-april-16-2026)

自 2024 年发布以来，uv 作为 Python 项目管理工具迅速受到开发者青睐，尤其在速度、Python 版本管理和虚拟环境方面表现突出。尽管在 Stack Overflow 2025 年调查中被评为最受“赞赏”的工具，但在实际代码库中的使用率仍显著低于传统的 pip 和 requirements.txt，这主要受限于历史项目遗留和 AI 编码代理的推荐偏好。

- 🚀 **uv 在 2025 年后新项目中的使用率达 30%-43%**，显示其在新生代开发者中快速普及，但整体占比仍低于 pip。
- 🤖 **AI 编码代理普遍推荐 pip**，因训练数据中 pip 指令占主导，导致自动生成的代码仍多依赖 requirements.txt。
- 📊 **实际开发者使用率可能高于仓库数据**，因开发者常跨项目工作，且 uv 在工具链中更易集成。
- 🔧 **非典型 requirements.txt 用途常见**，如仅用于测试或子项目，反映部分使用可能由 AI 代理无意生成。
- 💡 **建议按项目类型优化工具推荐**：库作者可同时提供 uv 和 pip 指令；应用作者应优先推荐 uv 以简化环境配置；脚本作者可采用 PEP 723 内联依赖替代 requirements.txt。

---

### [错误](https://github.com/GetBindu/Bindu?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-741-april-16-2026)

**原文标题**: [Error](https://github.com/GetBindu/Bindu?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-741-april-16-2026)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='github.com', port=443): Max retries exceeded with url: /GetBindu/Bindu?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-741-april-16-2026 (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [错误](https://github.com/Tracer-Cloud/opensre?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-741-april-16-2026)

**原文标题**: [Error](https://github.com/Tracer-Cloud/opensre?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-741-april-16-2026)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='github.com', port=443): Max retries exceeded with url: /Tracer-Cloud/opensre?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-741-april-16-2026 (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [错误](https://github.com/docglow/docglow?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-741-april-16-2026)

**原文标题**: [Error](https://github.com/docglow/docglow?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-741-april-16-2026)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='github.com', port=443): Max retries exceeded with url: /docglow/docglow?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-741-april-16-2026 (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [错误](https://github.com/HKUDS/Vibe-Trading?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-741-april-16-2026)

**原文标题**: [Error](https://github.com/HKUDS/Vibe-Trading?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-741-april-16-2026)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='github.com', port=443): Max retries exceeded with url: /HKUDS/Vibe-Trading?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-741-april-16-2026 (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [错误](https://github.com/aallan/vera?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-741-april-16-2026)

**原文标题**: [Error](https://github.com/aallan/vera?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-741-april-16-2026)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='github.com', port=443): Max retries exceeded with url: /aallan/vera?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-741-april-16-2026 (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [GitHub - dropseed/plain：用于构建应用的Python Web 框架。· GitHub](https://github.com/dropseed/plain?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-741-april-16-2026)

**原文标题**: [GitHub - dropseed/plain: The Python web framework for building apps. · GitHub](https://github.com/dropseed/plain?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-741-april-16-2026)

Plain 是一个基于 Python 的 Web 应用框架，最初从 Django 分支而来，经过多年实际使用重塑而成，专为 AI 代理时代设计。

- 🐍 采用显式、类型化且可预测的代码风格，同时适合人类和 AI 代理使用
- 🛠️ 提供完整的开箱即用技术栈，包括 Postgres 数据库、Jinja2 模板、htmx 和 Tailwind CSS
- 📊 内置可观测性功能，包含 OpenTelemetry 追踪、请求观察器和慢查询检测
- 🤖 为 AI 代理提供专门工具，包括规则文件、按需文档和端到端工作流技能
- 📦 包含 30 个一体化官方包，涵盖认证、API、后台任务、前端开发等各个方面
- 🚀 支持快速启动项目，可通过 AI 代理或 uv 工具直接创建应用
- 🔧 强调开发体验，提供调试工具栏、远程 Shell、安全扫描等开发工具

---

### [错误](https://github.com/hugohe3/ppt-master?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-741-april-16-2026)

**原文标题**: [Error](https://github.com/hugohe3/ppt-master?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-741-april-16-2026)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='github.com', port=443): Max retries exceeded with url: /hugohe3/ppt-master?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-741-april-16-2026 (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [GitHub - nedbat/linklint：一个用于减少过度链接的Sphinx扩展 · GitHub](https://github.com/nedbat/linklint?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-741-april-16-2026)

**原文标题**: [GitHub - nedbat/linklint: A Sphinx extension to reduce excessive linking · GitHub](https://github.com/nedbat/linklint?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-741-april-16-2026)

Linklint 是一个 Sphinx 扩展和命令行工具，用于检测并移除文档中多余的引用链接，以提升文档的可读性。

- 🔗 **功能概述**：作为 Sphinx 扩展或命令行工具，可检查并移除文档中不必要的引用链接，如指向自身或段落内重复的链接。
- 🛠️ **检查类型**：支持两种检查——"self"（移除指向自身章节的链接）和"paradup"（移除同一段落内重复的链接，仅保留第一个为链接）。
- 📂 **集成方式**：通过将`linklint.ext`添加到 Sphinx 配置文件的扩展列表中，可在构建过程中自动处理多余链接，无需修改源文件。
- ⚙️ **命令行使用**：支持通过`linklint`命令对.rst 文件进行静态检查，并提供`--fix`选项直接修复问题（例如将`:func:`foo``改为`:func:`!foo``）。
- 📈 **版本更新**：最新版本 v0.4.1 兼容 Sphinx 8.x 和 9.x，修复了早期版本中错误移除显式引用（如`:ref:`、`:doc:`）的问题，并优化了类与方法的关联处理。
- 📊 **应用效果**：在 CPython 文档中已成功移除了 3612 个多余链接，显著提升了文档的简洁性。

---

### [阿姆斯特丹 AgentCamp 2026，2026 年 4 月 23 日星期四，下午 6:00 | 聚会](https://www.meetup.com/pyladiesams/events/313950343/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-741-april-16-2026)

**原文标题**: [AgentCamp Amsterdam 2026, Thu, Apr 23, 2026, 6:00 PM   | Meetup](https://www.meetup.com/pyladiesams/events/313950343/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-741-april-16-2026)

AgentCamp Amsterdam 2026 是一场面向 AI 爱好者和开发者的全球性活动，旨在通过研讨会和主题演讲促进 AI 知识的学习与分享。

- 🎤 **主题演讲**：探讨 AI 代理的未来发展，涵盖从研究到实际应用的历程、自动化框架及可靠性工程技术。
- 🍕 **研讨会一**：学习使用 Microsoft Foundry 和 MCP 构建披萨订购代理，包括系统提示、工具调用和外部服务集成。
- 🔍 **研讨会二**：从零开始掌握语义搜索和多代理 AI，利用 DocumentDB、OpenAI 和 LangGraph 构建 RAG 聊天机器人。
- 🎧 **研讨会三**：创建 AI 驱动的播客制作团队，学习部署本地 AI 模型并构建完整的播客生产流程。
- ⏰ **活动安排**：活动于 18:00 开始，包含主题演讲、90 分钟研讨会选择及闭幕致辞。
- 🌐 **资源与联系**：提供 GitHub 代码库、YouTube 直播链接，并欢迎通过邮件或 Slack 频道参与社区交流。

---

### [PyData 三城会 #42，2026 年 4 月 22 日星期三，下午 6:00 | 聚会](https://www.meetup.com/pydata-trojmiasto/events/314161432/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-741-april-16-2026)

**原文标题**: [PyData Trójmiasto #42, Wed, Apr 22, 2026, 6:00 PM   | Meetup](https://www.meetup.com/pydata-trojmiasto/events/314161432/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-741-april-16-2026)

PyData Trójmiasto 第 42 次会议即将举行，聚焦人工智能的自我改进与批判性反思，包含两场主题演讲及交流环节。

- 🗓️ **活动详情**：第 42 届 PyData 三城会议，4 月 22 日 18:00-20:00 于格丁尼亚 Tensor Z 大楼举行，需提前注册并携带身份证件。
- 🧠 **主题演讲一**：Dawid Moczadło 分享“用 AI 改进 AI”，探讨如何通过评估、实验和反馈循环持续优化智能体系统，强调快速迭代与内部工具的重要性。
- ⚠️ **主题演讲二**：Tomasz Dołbniak 带来“antiLLM——你的 AI 助手正让你变笨”，基于研究数据批判 AI 对批判性思维、就业市场及环境的潜在负面影响。
- 🤝 **交流环节**：会议包含开场介绍、演讲后的社交网络环节，并提供免费街边停车位。
- 🏢 **赞助与支持**：活动由 NumFOCUS 赞助，遵循 PyData 许可协议，面向对人工智能、深度学习及 Python 技术感兴趣的专业人士。

---

### [Claude 代码入门：演示与讲解，2026 年 4 月 21 日周二晚 7 点 | 线下交流会](https://www.meetup.com/rochester-python-meetup/events/312840184/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-741-april-16-2026)

**原文标题**: [Intro to Claude Code, a Demonstration and Explanation , Tue, Apr 21, 2026, 7:00 PM   | Meetup](https://www.meetup.com/rochester-python-meetup/events/312840184/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-741-april-16-2026)

本次罗切斯特 Python 聚会将介绍 Claude Code 工具，通过现场演示展示其在实际开发中的应用，包括代码重构、测试生成和故障排查，并讨论其适用场景与局限性。

- 🗓️ 活动于 4 月 21 日 19:00-21:00（美国东部时间）举行，每月第三个周二持续至 2026 年 7 月 8 日
- 🏛️ 线下地点为罗切斯特大学 Wegmans Hall 1201 室，提供停车指引与路线图
- 💻 线上通过 Zoom 同步进行，会议号与密码已明确列出
- 🛠️ 主题聚焦 Anthropic 开发的命令行工具 Claude Code，涵盖其功能、配置与工作流集成
- 🔍 现场演示包含脚本重构为包、从零生成 pytest 套件、根据追踪信息调试等实际案例
- ⚖️ 将客观分析该工具的优缺点及适用边界
- 📍 活动由罗切斯特 Python 社区组织，支持线上线下混合参与模式

---

### [PyLadies 旧金山分会 @ WorkOS，2026 年 4 月 23 日星期四下午 5:30 | 聚会](https://www.meetup.com/pyladiessf/events/313916889/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-741-april-16-2026)

**原文标题**: [PyLadies San Francisco @ WorkOS, Thu, Apr 23, 2026, 5:30 PM   | Meetup](https://www.meetup.com/pyladiessf/events/313916889/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-741-april-16-2026)

旧金山 PyLadies 小组将于 4 月 23 日在 WorkOS 举办一场技术交流活动，内容包括披萨聚餐、Python 技术分享与社交网络。

- 🗓️ **活动时间**：4 月 23 日下午 5:30 至 8:30（太平洋时间）
- 📍 **活动地点**：旧金山 WorkOS（需通过 Luma 注册获取具体地址）
- 👩‍💻 **主办方**：Alla B.与旧金山 PyLadies 小组
- 🔗 **注册方式**：需通过 Luma 平台完成注册（链接：https://luma.com/z9px4nbg）
- 🍕 **活动特色**：提供披萨餐饮，由 WorkOS 赞助支持
- 🎤 **核心演讲**：Viviana Márquez 将分享《如何通过 Python 快速为 AI 收集数据》，涵盖人类数据在 LLM 生命周期中的作用及实操演示
- ⚡ **附加环节**：包含闪电演讲、社区公告与自由交流时段
- 👥 **参与群体**：适合 Python 初学者、技术开发人员及对 AI 数据收集感兴趣的女性科技从业者

---

### [错误](https://www.meetup.com/pydata-southampton/events/314185040/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-741-april-16-2026)

**原文标题**: [Error](https://www.meetup.com/pydata-southampton/events/314185040/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-741-april-16-2026)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='www.meetup.com', port=443): Max retries exceeded with url: /pydata-southampton/events/314185040/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-741-april-16-2026 (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [Vertex AI 入门指南：使用 Google Gemini 构建你的首个 AI 应用，2026 年 4 月 26 日周日，上午 9:00 | Meetup 活动](https://www.meetup.com/pydata-omr/events/314031353/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-741-april-16-2026)

**原文标题**: [Getting Started with Vertex AI: Build Your First AI App with Google Gemini, Sun, Apr 26, 2026, 9:00 AM   | Meetup](https://www.meetup.com/pydata-omr/events/314031353/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-741-april-16-2026)

本次网络研讨会面向初学者，介绍如何使用 Google Vertex AI 平台和 Gemini 模型构建 AI 应用，无需编程经验。

- 🎯 **学习内容**：涵盖生成式 AI 基础、Vertex AI 平台介绍、Google Gemini 模型概览、平台实时演示以及如何开始构建 AI 应用。
- 👥 **适合人群**：学生、初学者、有抱负的开发者以及对 AI 工具和职业感兴趣的任何人士。
- 🌐 **相关主题**：涉及 Google Cloud、大数据、数据科学、Python 和开源技术。
- 🤝 **活动支持**：由 NumFOCUS 赞助，致力于推广开源科学代码。

---

### [错误](https://www.meetup.com/pydata-milton-keynes/events/314008314/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-741-april-16-2026)

**原文标题**: [Error](https://www.meetup.com/pydata-milton-keynes/events/314008314/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-741-april-16-2026)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='www.meetup.com', port=443): Max retries exceeded with url: /pydata-milton-keynes/events/314008314/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-741-april-16-2026 (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

