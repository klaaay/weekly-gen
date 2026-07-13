### [小编程技巧 · 威尔·凯勒赫](https://will-keleher.com/posts/small-programming-tricks-matter/)

**原文标题**: [
  
    Small Programming Tricks Â· will keleher
  
](https://will-keleher.com/posts/small-programming-tricks-matter/)

### 概述总结
本文强调了日常工作中微小但高价值的技术技巧对提升工程效率的重要性，并列举了多个实用示例。

- 💡 **命令行历史搜索增强**：通过安装 `fzf` 实现模糊搜索，或使用 `atuin` 将历史记录存入 SQLite 数据库，还可配置 `per-directory-history` 按目录搜索。
- 🔍 **SQL 无表查询**：使用 `SELECT` 无需 `FROM` 子句，便于测试函数或检查 `NULL` 比较行为（如 `SELECT TRUE <> NULL`）。
- ⚡ **数据库性能分析**：PostgreSQL 和 MySQL 支持 `EXPLAIN ANALYZE`，可实际运行查询并提供详细性能信息。
- 📝 **正则表达式词边界**：`\b` 断言可精准匹配单词开头或结尾，简化文本处理。
- 📊 **指标分布分析**：通过 `Math.log10` 对数值取对数后分桶，可快速了解字段值的分布情况。
- 🚀 **现代 JS 实用特性**：包括 `Array.flatMap`、`Object.entries` 和 `Promise.withResolvers`，提升代码简洁性。
- 🔗 **Node.js 连接复用**：创建 `https.Agent` 并传入 `fetch` 请求，可显著降低与外部资源的通信延迟。
- 🔎 **Git 代码搜索**：`git log -S pattern`（“git pickaxe”）可查找添加或删除特定字符串的提交，尤其适用于旧代码库。
- 🔄 **Git 快速切换分支**：`git checkout -` 可回到上一个 HEAD，类似 `cd -` 的便捷操作。
- 📂 **文件搜索替代方案**：使用 `**/*.md` 通配符替代 `find` 命令（需在 bash 中启用 `shopt -s globstar`）。
- 🛠️ **高效搜索工具**：推荐使用 `ripgrep (rg)` 替代 `grep`、`ack` 或 `ag`，速度更快。
- ⚙️ **Zsh 自动补全配置**：需手动启用 `compinit` 并添加 `FPATH` 路径，以激活高级自动补全功能。
- 🏢 **公司内部知识分享**：鼓励高级工程师每日分享一个技巧（如调试方法、工具使用、领域知识），避免信息过载并促进讨论。

---

### [Display.dev – 面向工件的中立工作空间](https://display.dev/?utm_source=programmingdigest&utm_medium=newsletter&utm_campaign=2026-07-13)

**原文标题**: [Display.dev – Agent-neutral workspace for artifacts](https://display.dev/?utm_source=programmingdigest&utm_medium=newsletter&utm_campaign=2026-07-13)

display.dev 是一个与代理无关的工作空间，能将任何 AI 代理生成的 HTML 或 Markdown 文件，一键发布为受公司 SSO 保护的永久链接，支持团队协作和迭代，且价格统一，无席位限制。

- 🔗 **统一发布平台**：任何代理（Claude Code、Codex、Cursor 等）生成的工件，都能通过一条命令发布为永久 URL，切换代理时链接、版本和评论不丢失。
- 🔒 **默认企业级认证**：工件默认仅限公司成员通过 Google 或 Microsoft SSO 访问，外部用户无法查看，确保隐私安全。
- 💬 **内联评论与迭代**：团队成员可直接在页面上留下内联评论，代理能通过 MCP 读取评论、更新内容并重新发布，使工件成为活文档。
- 👥 **无限查看者**：定价基于存储和功能，而非查看者数量，一个统一价格即可覆盖整个组织的所有人。
- 📊 **完整审计与版本控制**：记录谁在何时查看了工件，并保留版本历史，支持审计日志。
- 💰 **定价灵活**：提供免费版（10 个门控工件）、个人版（€15/月）、团队版（€49/月，含 SSO）和企业版（从 €499/月起），性价比远高于 Vercel、Cloudflare 等竞品。
- 🛠️ **易于集成**：支持 CLI、MCP 或 API 调用，无需额外账户或许可证，即可从任何代理发布。

---

### [Display.dev – 用于工件的代理中立工作空间](https://display.dev/)

**原文标题**: [Display.dev – Agent-neutral workspace for artifacts](https://display.dev/)

display.dev 是一个为 AI 代理生成的内容提供统一、永久且安全的分享平台。它支持从任何代理（如 Claude Code、Codex、Cursor）一键发布 HTML 或 Markdown 文件，并通过公司 SSO（Google/Microsoft）进行身份验证，无需观众额外注册或购买许可。该平台提供无限观众、内联评论、版本控制、审计日志等功能，且定价基于存储和功能，而非用户数量，旨在成为所有代理产出的中心枢纽。

- 🔗 **统一链接**：为每个代理生成的内容提供一个永久、私密的 URL，切换供应商时链接、版本和评论保持不变。
- 🔐 **公司认证**：通过 Google 或 Microsoft SSO 自动验证公司域名的用户，外部人员无法访问，确保隐私。
- 💬 **内联评论**：团队成员可在页面上直接评论，代理能通过 MCP 读取评论、更新内容并解决线程，使文档成为活文档。
- 🤖 **代理无关**：支持任何能输出 HTML 或 Markdown 的代理（CLI、MCP 或 API），无供应商锁定。
- 📊 **无限观众**：定价基于存储和功能，而非观众数量，从 1 人到 1000 人费用相同。
- 📝 **版本与审计**：记录每个版本和评论的代理及操作者信息，提供谁在何时查看了什么内容的审计日志。
- 💰 **灵活定价**：提供免费、个人（€15/月）、专业版（€49/月）和企业版（从 €499/月）计划，满足不同需求。
- 🏢 **企业故事**：Indigo Engineering 等团队使用后，避免了在 Slack 中混乱分享文件或截图的问题。
- 📹 **产品演示**：展示了从代理发布、团队评论到代理更新的完整循环，所有操作围绕一个 URL 进行。
- 🆚 **性价比**：与 Vercel、Cloudflare、GitBook 等方案相比，display.dev 在共享 HTML 工件时成本低 7-40 倍。
- 🚀 **快速上手**：无需账户即可通过粘贴命令或示例文件试用，15 秒内即可将文件转换为认证后的 URL。

---

### [分支避免编程](https://easylang.online/blog/branchless)

**原文标题**: [Branch‑Avoidant Programming](https://easylang.online/blog/branchless)

无法总结：未找到主要内容。

---

### [特里斯·谢利克](https://tris.sherliker.net/blog/obfuscated-self-evaluating-bash-script-by-cdn-akamai-being-supplied-to-consumers-via-retail-stores/)

**原文标题**: [Tris Sherliker](https://tris.sherliker.net/blog/obfuscated-self-evaluating-bash-script-by-cdn-akamai-being-supplied-to-consumers-via-retail-stores/)

### 概述总结
Akamai 与优衣库合作推出了一款印有混淆 bash 脚本的 T 恤，脚本解码后是一个显示"Peace for All"动画的复活节彩蛋。

- 🧥 **T 恤设计**：正面是心形图案，背面印有 base64 编码的 bash 脚本，需解码运行
- 🐣 **隐藏彩蛋**：脚本解码后生成一个正弦波动画，循环显示"♥PEACE♥FOR♥ALL♥"文字
- 💻 **技术细节**：脚本使用终端控制命令 (tput) 定位字符，通过正弦函数计算水平位置，并实现青色到橙色的渐变效果
- 🎨 **字体之谜**：最初被误认为是 Consolas 字体，后经 Hacker News 用户指正实际为 Roboto Mono
- 🌐 **设计理念**：浅米色代表早期互联网"米色盒子"电脑，心形象征互联网的善意用途，代码致敬 Linux 开源精神
- 🔍 **OCR 挑战**：因 base64 无纠错能力，需精确转录；对比了 Android 圈选搜索、Tesseract 和 Claude 三种 OCR 结果
- 📰 **媒体报道**：Akamai 曾发布新闻稿介绍该 T 恤设计，强调其代表"更安全、更互联的世界"愿景

---

### [虚拟内存：页表、TLB 与 Linux 内部机制](https://blog.codingconfessions.com/p/virtual-memory)

**原文标题**: [Virtual Memory: Page Tables, TLBs, and Linux Internals](https://blog.codingconfessions.com/p/virtual-memory)

这是一篇关于虚拟内存的深度指南，通过进程“Alloca”与“内核”的对话，全面讲解了虚拟内存的原理、实现及其对性能的影响。

- 📖 **虚拟内存基础与必要性**：虚拟内存为每个进程提供独立的地址空间，实现内存隔离与保护，防止进程间相互干扰，并让每个进程感觉拥有海量内存。
- 🗺️ **地址空间布局**：进程的虚拟地址空间被划分为代码段、数据段、BSS 段、堆、内存映射区和栈，每个区域有特定的权限（如只读、可执行）和增长方向。
- 🔄 **地址转换机制**：虚拟地址通过四级页表层次结构转换为物理地址，由 MMU 硬件执行。TLB（转译后备缓冲器）缓存最近使用的转换，避免每次都进行完整的页表遍历。
- 💡 **按需分页**：内核不会在分配内存时立即分配物理帧，而是在进程首次访问页面时通过“页错误”机制才分配，这称为惰性分配，能有效节省物理内存。
- 💾 **页面回收与交换**：当物理内存不足时，内核会回收最近未使用的页面。匿名页可能被换出到交换空间，而文件支持页则可直接丢弃并从磁盘重新读取。
- ✂️ **写时复制**：`fork()`创建子进程时，父子进程共享物理页面。只有当一方尝试写入时，内核才会复制该页面，这使得进程创建非常迅速。
- 📁 **内存映射文件**：`mmap()`系统调用将文件直接映射到进程地址空间，避免了`read()`/`write()`所需的从内核缓冲区到用户缓冲区的额外拷贝，提高了 I/O 效率。
- ⚡ **性能影响因素**：内存访问模式（顺序 vs. 随机）、页面大小、TLB 容量、NUMA 拓扑结构等都会显著影响数据密集型应用的性能。
- 🔍 **可观测性工具**：Linux 提供了多种工具来观察虚拟内存状态，如`/proc/<pid>/maps`、`smaps`、`vmstat`、`perf stat`和`numastat`，用于诊断内存相关性能问题。

---

### [给新毕业生的建议：在行业内抓住任何你能得到的工作——Jim Grey 谈软件管理](https://dev.jimgrey.net/2026/07/08/advice-to-new-grads-take-any-job-you-can-get-in-the-industry/)

**原文标题**: [Advice to new grads: take any job you can get in the industry – Jim Grey on software management](https://dev.jimgrey.net/2026/07/08/advice-to-new-grads-take-any-job-you-can-get-in-the-industry/)

概述总结  
- 🎓 对刚毕业的计算机或软件工程学生：若找不到理想编程工作，先接受行业内任何职位（如技术写作、客服、QA 等），进入公司比岗位完美更重要。  
- 🚪 进入公司后，通过解决实际问题（如逆向工程 API）和建立人际关系，能自然转向工程岗位。  
- 🤝 同事的信任和认可比简历项目更有价值，内部转岗或跳槽到更开放的公司是常见路径。  
- ⏳ 这条路需要耐心，但能让你在真实组织中积累声誉和机会。  
- 💡 例子：作者从技术写作到 QA 再到工程，Dan 从客服到 QA，都因“在场”和“解决问题”而获得晋升。  
- 🌟 核心建议：抓住任何进入软件公司的机会，从内部寻找发展路径。

---

### [CORS：它在保护什么？| 工程笔记](https://sanyamserver.online/posts/cors/)

**原文标题**: [CORS: What is it protecting? | Engineering Notes](https://sanyamserver.online/posts/cors/)

以下是您提供的文章摘要：

CORS 是浏览器实施的安全机制，用于控制跨源请求的响应读取权限，而非服务器安全措施。

- 🌐 **CORS 是浏览器安全机制**：浏览器根据 `Access-Control-Allow-Origin` 头决定是否允许 JavaScript 读取跨源响应，服务器本身不强制执行。
- 🔄 **实现方式**：浏览器在跨源请求中自动添加 `Origin` 头，服务器返回 `Access-Control-Allow-Origin` 头进行匹配，不匹配则浏览器丢弃响应。
- ⚡ **预检请求**：对于非简单请求（如 PUT、自定义头），浏览器先发送 `OPTIONS` 预检请求确认服务器允许，再发送实际请求。
- 🛡️ **CORS 保护场景**：防止恶意网站利用用户浏览器中的会话 cookie 读取其他网站的数据（如银行账户余额）。
- ❌ **CORS 不防御 CSRF**：CSRF 攻击利用用户会话执行写操作（如转账），CORS 只阻止读取响应，不阻止请求本身。
- 🔐 **CSRF 防御措施**：使用 `SameSite` cookie 属性、CSRF token 或服务器端检查 `Origin`/`Referer` 头来防止跨站请求伪造。
- 📌 **核心区别**：CORS 关注“能否读取响应”，CSRF 关注“是否应接受请求”，两者独立且需分别防护。

---

