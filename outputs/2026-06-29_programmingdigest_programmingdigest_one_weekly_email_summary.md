### [p99 0 毫秒* 自动补全 2.4 亿个域名 - Ruurtjan Pul](https://ruurtjan.com/articles/p99-0ms-autocomplete-for-240-million-domain-names)

**原文标题**: [p99 0 ms* autocomplete for 240 million domain names - Ruurtjan Pul](https://ruurtjan.com/articles/p99-0ms-autocomplete-for-240-million-domain-names)

### 概述总结
本文介绍了如何为 240 百万个域名实现 p99 延迟为 0 毫秒的自动补全功能，通过客户端预取、缓存和优化 API 响应时间，使 99% 的按键操作在用户释放按键前完成渲染。

- 🔍 **核心目标**：实现按键释放前完成自动补全渲染，p99 延迟为 0 毫秒，即 99% 的按键操作无感知延迟。
- ⚡ **技术方案**：客户端在按键按下时预取当前字符及下一字符的建议，按键释放时渲染结果，利用按键间隔时间作为 API 响应预算。
- 🕒 **时间预算**：通过测量 100 个域名的快速输入，p99 时间预算为 121 毫秒，即 API 需在此时间内返回结果。
- 🗂️ **数据结构**：头部使用内存中的字符前缀树（trie）存储前 8 个建议，尾部使用 SSD 支持的内存映射块索引处理 240 百万域名，两者查找复杂度均为 O(1)。
- 📊 **性能测试**：API 在 1.6k req/s下p99延迟为15毫秒，网络延迟是主要瓶颈，端到端延迟（含Cloudflare）在预算内。
- 🌍 **地理限制**：单一欧洲服务器导致美国等远距离流量延迟超预算（100-200 毫秒），需多服务器和地理负载均衡才能完全实现 p99 0 毫秒。
- 💡 **优化权衡**：CDN 缓存和 Nielsen 的 0.1 秒“即时”阈值可缓解延迟，但未完全达标；作者认为该功能过于小众，暂不商业化，但欢迎用户反馈。

---

### [AURI 开发者版 | AI 原生应用安全平台 | Endor Labs](https://www.endorlabs.com/platform/developer?utm_source=programming-digest&utm_medium=newsletter&utm_campaign=auri-for-developers)

**原文标题**: [AURI for Developers | AI-Native AppSec Platform | Endor La](https://www.endorlabs.com/platform/developer?utm_source=programming-digest&utm_medium=newsletter&utm_campaign=auri-for-developers)

Endor Labs 推出 AURI for Developers，一个免费的开发者安全工具，能直接在 AI 编码工作流中修复漏洞、检测密钥和阻止恶意依赖。

- 🔒 **免费且本地化**：无需注册或信用卡，所有扫描在本地运行，代码绝不离开机器。
- ⚡ **快速集成**：支持 Cursor、VS Code、Claude Code 等主流 IDE，配置后 60 秒内即可开始扫描。
- 🛡️ **四合一扫描**：涵盖 SAST（代码漏洞）、SCA（依赖漏洞）、密钥检测和恶意包检测。
- 🤖 **MCP 服务器支持**：通过 MCP 协议与 AI 编码助手实时交互，在编写代码时即时发现并修复安全问题。
- 📦 **开源依赖安全**：可扫描所有 OSS 依赖，识别关键漏洞、恶意包（如 event-stream）并提供修复建议。
- 🧩 **Skills 插件**：一键安装后，可对代码、密钥、开源依赖和容器镜像进行全栈安全审查。
- 👥 **团队与企业版**：免费版适合个人，付费版提供集中策略、报告、团队管理和 SIEM 集成。
- 📚 **丰富资源**：提供安全代码提示库、恶意软件拦截指南和上下文工程指南，帮助开发者编写更安全的代码。

---

### [YAGNI 的成本从未关乎——肯特·贝克](https://newsletter.kentbeck.com/p/the-cost-yagni-was-never-about)

**原文标题**: [The Cost YAGNI Was Never About - by Kent Beck](https://newsletter.kentbeck.com/p/the-cost-yagni-was-never-about)

以下是对文章内容的总结：

YAGNI（You Aren't Gonna Need It）并非关于节省编写代码的精力，而是关于避免过早构建“推测性结构”所带来的两种隐性成本。

- 🎯 **核心误解澄清**：YAGNI 不是懒惰或拒绝设计的借口，而是关于“时机”的深思熟虑。过早构建结构与过晚构建结构同样危险。
- 💸 **第一笔账单：放弃期权价值**：提前构建结构是基于猜测的承诺。即使猜对了，也浪费了“等待信息到来后再构建正确结构”的期权价值。等待不是懒惰，而是持有资产。
- ⏳ **第二笔账单：净现值（NPV）损失**：提前投入成本，推迟获得回报，导致资金的时间价值损失。即使预测完全正确，这种时间差依然会造成损失。
- 🤖 **AI 时代依然有效**：YAGNI 并非关于“打字成本”。即使 AI 可以免费、即时生成推测性代码，上述两笔账单依然存在，且由于代码更难以理解，风险反而更大。
- 🧠 **核心原则**：在真正需要的时候再构建。不是因为代码昂贵，而是因为未使用的期权和未花费的资金更有价值。

---

### [延迟的 AWS 管道故事：一个看似简单的 AWS API 调用如何…… | 作者：Vladimir Romashov | Booking.com 工程部 | 2026 年 5 月 | Medium](https://medium.com/booking-com-development/a-story-of-delayed-aws-pipelines-382e4a1fede6)

**原文标题**: [A Story of Delayed AWS Pipelines. How a seemingly simple AWS API call can… | by Vladimir Romashov | Booking.com Engineering | May, 2026 | Medium](https://medium.com/booking-com-development/a-story-of-delayed-aws-pipelines-382e4a1fede6)

一个看似简单的 AWS API 调用如何悄然拖慢 CI/CD 流水线的故事

- 🔍 问题发现：团队 CI/CD 日志中出现长达 15 分钟的`aws_organizations_organization`数据读取延迟，约 1/10 的 Terraform 流水线受影响
- ⚙️ 根本原因：Terraform 的`aws_organizations_organization`数据源不仅调用`DescribeOrganization`，还额外调用`ListAccounts`和`ListRoots`两个分页 API
- 🚦 共享配额瓶颈：这些 API 的速率限制（1 请求/秒，突发 2 请求）按整个 AWS 组织共享，而非按账户独立计算
- 📊 放大效应：不同团队的流水线同时调用时，会快速耗尽共享令牌桶，导致排队延迟，即使 IAM 拒绝的调用也会触发重试
- 🔧 修复方案：向 Terraform AWS Provider 提交 PR，使`ListAccounts`和`ListRoots`调用变为可选，从 v6.29.0 版本开始生效
- 💡 临时缓解措施：在等待上游修复期间，引入中央缓存机制，避免重复 API 调用，累计节省数小时流水线时间
- 🔮 未来展望：AWS 已确认计划为 Organizations API 推出自动配额管理功能，但目前尚未覆盖
- 🎯 经验教训：看似简单的工具可能隐藏复杂交互，共享基础设施的成本只有在规模化时才会显现

---

### [LLM 实际工作原理 | 0xkato](https://www.0xkato.xyz/how-llms-actually-work/)

**原文标题**: [How LLMs Actually Work | 0xkato](https://www.0xkato.xyz/how-llms-actually-work/)

本文深入浅出地解析了现代基于 Transformer 的大语言模型（LLM）的核心工作原理，涵盖了从文本输入到输出预测的完整流程，并解释了关键组件如注意力机制、前馈网络和残差流的作用。

- 🔤 **分词与嵌入**：文本先被转换为整数 ID（分词），再通过嵌入矩阵映射为具有语义含义的向量，语义相近的词在向量空间中位置相近。
- 📍 **位置编码**：通过旋转位置编码（RoPE）等方法，为每个词注入位置信息，让模型理解词序，避免“lost in the middle”问题。
- 👁️ **注意力机制**：每个词通过查询、键、值（QKV）向量与其他词交互，计算注意力权重，实现信息共享，并采用因果掩码确保从左到右生成。
- 🧠 **多头注意力**：并行运行多个注意力头，每个头学习不同的关系（如语法、指代），并通过分组查询注意力（GQA）优化内存效率。
- ⚙️ **前馈网络**：每个词独立经过扩展、非线性变换和压缩，存储大量事实和语义知识，部分模型采用混合专家（MoE）架构提升效率。
- 🌊 **残差流与层归一化**：残差连接让信息逐层累积，避免梯度消失；层归一化（如 RMSNorm）稳定数值，使深层网络可训练。
- 🎯 **下一个词预测**：模型输出每个可能词的分数（logits），通过 softmax 转为概率，结合温度等解码策略生成文本，并可用推测解码加速。
- 🏗️ **架构与权重**：现代 LLM 共享 Transformer 骨架，差异在于训练数据、配置（层数、头数等）和后训练（指令微调、安全控制），权重是学习到的核心参数。

---

### [一个 CVE 争议 | daniel.haxx.se](https://daniel.haxx.se/blog/2026/06/24/a-cve-dispute/)

**原文标题**: [a CVE dispute | daniel.haxx.se](https://daniel.haxx.se/blog/2026/06/24/a-cve-dispute/)

本摘要讨论了 cURL 项目作为 CNA（CVE 编号授权机构）处理安全漏洞的过程，以及一起关于是否应为特定问题分配 CVE 的争议。

- 🔒 **CNA 角色与流程**：cURL 项目自成为 CNA 后，自主管理 CVE 编号，简化了漏洞处理流程，仅通过 API 调用即可快速分配 CVE。
- 📊 **漏洞评估标准**：项目团队根据漏洞的严重性（从 LOW 到 CRITICAL）进行分级，但强调用户实际受影响程度可能不同。
- ⚠️ **低于 LOW 的严重性**：对于极低风险的问题（如需要极端条件才能触发），项目选择不分配 CVE，以避免给全球数十亿安装实例带来不必要的安全更新成本。
- 🛡️ **争议案例**：2026 年 2 月，报告者要求为“主机名带前导点”的 bug 分配 CVE，但项目认为该问题需要极苛刻条件（如非法 DNS 名、本地攻击者等），风险低于 LOW，因此拒绝。
- 📝 **MITRE 介入与裁决**：MITRE 多次要求解释后，于 6 月 24 日最终裁定支持 cURL 项目的决定，认为该问题不构成安全漏洞，不分配 CVE。
- 🔧 **修复措施**：项目已于 2025 年 12 月修复该 bug 并添加单元测试，但坚持不将其视为安全漏洞。

---

### [停止使用常规提交 - Sumner Evans](https://sumnerevans.com/posts/software-engineering/stop-using-conventional-commits/)

**原文标题**: [Stop Using Conventional Commits - Sumner Evans](https://sumnerevans.com/posts/software-engineering/stop-using-conventional-commits/)

以下是对文章《停止使用 Conventional Commits》的总结：

概述总结：文章批评 Conventional Commits 标准，认为它优先关注错误的方面（提交类型），而忽略了真正重要的范围（变更领域），并指出其承诺的自动生成变更日志、版本号提升等好处在实际中难以实现，最后推荐使用范围前缀的提交格式。

- 📛 **优先顺序错误**：Conventional Commits 将提交类型（如 fix、feat）放在首位，而范围（scope）设为可选，这完全颠倒了优先级。实际上，范围才是开发者、调试者和事故响应者最关心的信息。
- 🚫 **类型冗余且限制性强**：提交描述通常已隐含变更类型，额外添加类型浪费空间，且可能限制表达（如一个提交同时包含修复、重构和新功能）。
- 💔 **承诺未兑现**：自动生成变更日志对用户无益，因为用户关心功能变化，而开发者关注范围变化；自动版本号提升常因回滚、意外破坏等问题不准确；触发构建流程可能被绕过，且不适用于恶意提交。
- 🧩 **难以应用**：项目需自定义类型，但常默认使用 commitlint 的预设，不适合特定项目；在需要工单号的企业环境中，范围字段被占用，失去元数据价值。
- ✅ **更好的替代方案**：推荐使用范围前缀提交格式（如 Linux、FreeBSD、Go 等成功项目采用的方式），例如“子系统：描述”或“包名：描述”，并推广 scopedcommits.com 网站。
- ⚠️ **AI 传播反模式**：Conventional Commits 在开源项目中流行，导致 AI 默认使用它生成提交信息，进一步传播了不良实践。

---

