### [糟糕软件设计的症状 - 作者：Marcos F. Lobo 🗻🧭](https://newsletter.optimistengineer.com/p/symptoms-of-bad-software-design)

**原文标题**: [Symptoms of Bad Software Design - by Marcos F. Lobo 🗻🧭](https://newsletter.optimistengineer.com/p/symptoms-of-bad-software-design)

以下是关于不良软件设计症状的概述和要点总结：

软件设计中存在四种常见的不良信号：刚性、脆弱性、不动性和粘滞性，它们会导致系统难以维护和扩展，但可以通过设计模式、封装和自动化等方法解决。

- 🔒 刚性：系统难以修改，一处改动引发连锁反应。解决方案是使用策略模式解耦，遵循开闭原则。
- 💥 脆弱性：修改一处代码导致多处意外故障。解决方案是封装和接口隔离，避免全局状态和隐藏依赖。
- 🧱 不动性：代码难以复用，因与特定环境深度绑定。解决方案是分层架构，将业务逻辑与框架和数据库分离。
- 🐌 粘滞性：走捷径比遵循正确设计更容易。解决方案是自动化工具和优化开发环境，让正确做法更便捷。

---

### [获取失败](https://www.levelaccess.com/resources/webinar-closing-the-accessibility-resolution-gap/?utm_source=bonobopress&utm_medium=paid-media&utm_campaign=fy26q2-pm-programming-digest&utm_content=May11)

**原文标题**: [Failed to retrieve](https://www.levelaccess.com/resources/webinar-closing-the-accessibility-resolution-gap/?utm_source=bonobopress&utm_medium=paid-media&utm_campaign=fy26q2-pm-programming-digest&utm_content=May11)

无法总结：获取内容失败，状态码 403。

---

### [编写自己的文本编辑器，并日常使用它](https://blog.jsbarretto.com/post/text-editor)

**原文标题**: [Writing my own text editor, and daily-driving it](https://blog.jsbarretto.com/post/text-editor)

这篇博文讲述了作者为何以及如何从零开始编写自己的文本编辑器，并最终将其作为日常主力工具的经历。作者认为，对于有动力的工程师来说，编写自己的工具并非徒劳，反而能带来巨大的好处。

- 🏰 **不满现状，寻求完美工具**：作者对现有编辑器（如Howl、Helix等）的诸多方面感到不满，包括开发停滞、项目搜索缓慢、不支持SSH、缺少集成终端等，因此决心打造一款完全符合自己“指尖触感”的编辑器。
- 🚀 **从零开始，逐步迭代**：项目初期保持小范围，硬编码偏好，暂不追求极致性能或全面Unicode支持。通过“强制使用”（替代nano）、“记录所有问题”和“即时修复烦人bug”三个习惯，将项目从停滞状态推进到每周数小时的活跃开发。
- 🎯 **核心功能精雕细琢**：重点实现了出色的文件浏览器（基于“开头匹配”、“包含匹配”和“最近修改时间”的简单排序算法，效果惊人）、高性能正则引擎（通过AST优化、线程码VM、CPS转换等技术，高亮5万行Rust文件仅需<10毫秒）、以及高效的按需高亮缓存。
- 💡 **集成终端与渲染优化**：基于`alacritty_terminal`库轻松实现了终端模拟器缓冲区，并采用双缓冲屏幕渲染技术，仅发送变化的单元格，大幅提升远程连接下的性能。
- 🎉 **结论：乐趣与生产力双赢**：作者强烈推荐编写自己的工具，认为这能带来“量身定做”的契合感、深入学习通用技术（如正则、ANSI、UTF-8）、提升长期生产力，并且“过程非常有趣”，重新点燃了对编程的热爱。

---

### [Git的神奇文件 | Andrew Nesbitt](https://nesbitt.io/2026/02/05/git-magic-files.html)

**原文标题**: [Git’s Magic Files | Andrew Nesbitt](https://nesbitt.io/2026/02/05/git-magic-files.html)

本文介绍了 Git 仓库中多个特殊的“魔法文件”，它们随代码一起提交，用于控制 Git 行为，并建议工具开发者应尊重这些配置。

- 📄 **.gitignore**：定义 Git 应忽略追踪的文件模式，支持通配符、目录标记和否定规则，且仅在文件未追踪时生效。
- ⚙️ **.gitattributes**：配置文件的处理方式，如过滤器、差异驱动、行尾标准化和语言检测覆盖，支持 `text`、`binary` 等属性。
- 🔗 **.lfsconfig**：Git LFS 的配置，随仓库携带，用于设置 LFS 端点 URL 和传输选项，需与 `.gitattributes` 配合使用。
- 📦 **.gitmodules**：管理 Git 子模块，记录路径、URL 和分支，但子模块需手动初始化和更新。
- 🏷️ **.mailmap**：将作者姓名和邮箱映射为规范身份，用于 `git log` 和 `git blame` 的输出聚合。
- 🚫 **.git-blame-ignore-revs**：列出 `git blame` 应跳过的提交（如格式化变更），支持自动读取（GitHub/GitLab/Gitea）。
- ✏️ **.gitmessage**：提交消息模板，需手动配置 `commit.template`，常被 `commit-msg` 钩子替代。
- 🏢 **Forge 特定文件夹**：如 `.github/`、`.gitlab/` 等，存放 CI/CD、模板和 CODEOWNERS，部分平台有回退链。
- 🛠️ **其他约定**：包括 `.gitkeep`（占位空目录）、`.gitconfig`（建议配置）、`.gitsigners`（签名密钥）、`.gitreview`（Gerrit 集成）、`.gitlint`（提交消息检查）等。
- 🌐 **超越 Git**：类似模式出现在 `.editorconfig`（编辑器行为）、`.ruby-version`（语言版本）、`.dockerignore`（Docker 构建上下文）等文件中。
- 💡 **工具支持**：构建 Git 交互工具时应读取 `.gitignore`、`.gitattributes`、`.mailmap` 和 `.gitmodules`，并注意 Git 配置格式。

---

### [数据库并非为此而设计](https://arpitbhayani.me/blogs/defensive-databases/)

**原文标题**: [Databases Were Not Designed For This](https://arpitbhayani.me/blogs/defensive-databases/)

## 概述总结
传统数据库架构基于人类开发者的隐性契约，但AI代理系统从根本上违反了这些假设，需要重新设计数据库安全层。

- 🤖 **非确定性调用者**：AI代理生成的查询不可预测，需设置角色级语句超时（如5秒）和空闲事务超时（如10秒）
- 🚫 **非意图性写入**：代理可能自主执行错误写入，需强制使用软删除（含deleted_by字段）、追加式事件日志和幂等键约束
- ⏱ **连接时长剧增**：代理推理过程会长时间占用连接，需独立连接池（建议pool_timeout=3秒）配合PgBouncer事务池模式
- 🔇 **静默失败风险**：代理无法识别错误查询结果，需通过查询注释标记agent_id/task_id/step实现可观测性
- 🗄 **模式即LLM契约**：列名和注释直接影响代理生成SQL质量，需建立代理友好视图层并编写文档式注释
- 🔒 **最小权限原则**：按代理类型创建独立角色，仅授予必要权限（如agent_analytics只读），缩小故障影响范围
- 🛡 **防御性设计模式**：软删除、追加日志、幂等键、行级安全等传统最佳实践从“可选”升级为“承载关键业务”的基础设施

---

### [交互式解释MicroGPT | growingSWE](https://growingswe.com/blog/microgpt)

**原文标题**: [MicroGPT explained interactively | growingSWE](https://growingswe.com/blog/microgpt)

### 概述总结
本文通过可视化方式，逐步解释了Andrej Karpathy的200行MicroGPT代码如何从零训练一个字符级语言模型，涵盖数据准备、数学原理、模型架构和训练推理全过程。

- 📚 **数据集与任务**：模型在32,000个人名上训练，学习字符统计规律以生成新名字，如"karai"；每个名字被视为一个文档，核心任务是预测下一个字符。
- 🔢 **文本数字化**：使用简单分词器将26个字母映射为0-25的整数，并添加BOS（序列开始）标记；每个字符对应一个无意义的索引值。
- 🎯 **预测机制**：模型通过滑动窗口逐位置预测下一个token，每个位置生成输入-目标对；所有语言模型（包括ChatGPT）都采用这种训练方式。
- 📊 **概率转换**：模型输出27个原始logits，通过Softmax函数转换为概率分布；Softmax通过指数运算放大差异，使高logits获得更高概率。
- 📉 **损失函数**：使用交叉熵损失衡量预测错误程度，公式为 -log(p)；当模型对正确token的预测概率接近0时损失趋近无穷大，有效惩罚错误预测。
- 🔄 **反向传播**：通过计算图反向传播梯度，应用链式法则计算每个参数对损失的影响；梯度从损失开始逐层回传，多路径贡献的梯度会累加。
- 🧠 **嵌入表示**：每个token查找16维嵌入向量，并与位置嵌入相加；模型从零学习这些表示，训练后相似字符（如元音）的嵌入会趋近。
- 👁️ **注意力机制**：每个token生成Query、Key、Value向量，通过点积计算注意力权重；因果掩码确保每个位置只能看到过去信息，多头注意力并行捕捉不同模式。
- 🏗️ **完整架构**：模型依次经过嵌入、归一化、注意力、残差连接、MLP（两层全连接+ReLU）、最终投影；残差连接为梯度提供捷径，RMSNorm稳定训练。
- 🎓 **训练过程**：重复1000次，每次选取一个名字，前向传播计算每个位置的损失，反向传播计算梯度，使用Adam优化器更新参数；Adam维护动量和自适应学习率。
- ✨ **推理生成**：从BOS开始，前向传播获取概率，随机采样下一个token，重复直到生成BOS或达到最大长度；温度参数控制采样随机性，0.5左右为名字生成的最佳值。
- ⚡ **效率扩展**：MicroGPT包含完整算法，与ChatGPT的区别仅在于规模：万亿级token、子词分词、GPU张量、千亿参数、数百层、数千GPU训练数月。

---

### [20条软件工程法则 - 米兰·米兰诺维奇博士](https://newsletter.techworld-with-milan.com/p/the-20-software-engineering-laws)

**原文标题**: [The 20 Software Engineering Laws - by Dr Milan Milanović](https://newsletter.techworld-with-milan.com/p/the-20-software-engineering-laws)

以下是您提供的文章摘要，包含概述和要点列表。

软件工程定律揭示了项目失败、系统腐化和团队效率下降的根本原因，这些定律并非关于软件本身，而是关于人们在时间压力下协作的本质。

- 🧩 **高尔的定律**：复杂系统必须从简单系统逐步构建，试图一步到位往往导致失败。
- 🎯 **KISS原则**：保持简单，任何超出必要的东西都是负担，简单设计更易维护和调试。
- 🏢 **康威定律**：系统架构会镜像组织的沟通结构，改变架构前需先调整团队。
- 🔗 **海勒姆定律**：API的每个可观察行为都可能成为用户的依赖，维护向后兼容性代价高昂。
- ⚖️ **CAP定理**：分布式系统只能在一致性、可用性和分区容忍性中保证两项，需根据场景权衡。
- 📧 **扎温斯基定律**：程序会不断膨胀直到能读取邮件，功能蔓延是自然过程，需警惕。
- 👥 **布鲁克斯定律**：向已延期的项目增加人手只会让它更慢，因为沟通和培训成本增加。
- 📉 **林格曼效应**：团队规模越大，个人产出越低，小团队效率更高。
- 🔢 **普莱斯定律**：一半的工作由团队人数的平方根完成，少数核心贡献者至关重要。
- 🤔 **邓宁-克鲁格效应**：能力越低的人越容易高估自己，而专家往往低估自己。
- ⏳ **霍夫施塔特定律**：任务总是比你预期的时间更长，即使你已经考虑到这个定律。
- 📅 **帕金森定律**：工作会膨胀以填满可用的时间，设定明确的截止日期可提升效率。
- 📊 **古德哈特定律**：当一个指标成为目标时，它就不再是好的指标，会导致行为扭曲。
- 📏 **吉尔布定律**：任何需要量化的东西都能找到测量方法，有测量总比没有好。
- ⚡ **克努特优化原则**：过早优化是万恶之源，应先写出能工作的代码再优化。
- 🚀 **阿姆达尔定律**：并行加速受限于串行部分，找到瓶颈比盲目增加资源更重要。
- 💥 **墨菲定律**：任何可能出错的事情最终都会出错，需编写防御性代码并做好预案。
- 📨 **波斯特尔定律**：发送时要保守，接收时要宽容，但需在安全场景中谨慎使用。
- 🗑️ **斯特金定律**：90%的东西都是垃圾，识别并专注于那10%真正重要的项目。
- 💬 **坎宁安定律**：在网上获得正确答案最快的方式是发布错误答案，利用纠错机制。

---

