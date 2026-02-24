### [为智能代理未来构建 Next.js | Next.js](https://nextjs.org/blog/agentic-future)

**原文标题**: [Building Next.js for an agentic future | Next.js](https://nextjs.org/blog/agentic-future)

Next.js 团队在过去一年中致力于提升框架的 AI 智能体（agent）使用体验，通过实验和集成，认识到关键在于从智能体的视角出发，提供必要的可见性和上下文支持。

- 🧠 **核心理念转变**：将智能体视为 Next.js 的一等用户，从它们的需求出发设计功能，而非仅提供表面工具。
- 🐞 **解决可见性问题**：最初发现智能体无法感知浏览器中的运行时错误、客户端警告和渲染组件，因此改进了错误数据结构和日志转发机制。
- 🧪 **实验性浏览器内智能体**：开发了名为 Vector 的集成智能体，支持页面元素选择和源码查看，但因与通用编程工具功能重叠而最终停止开发。
- 🔗 **MCP 集成突破**：通过 Model Context Protocol（MCP）暴露 Next.js 内部状态（如路由、渲染片段、错误信息），使智能体能直接访问运行时的开发服务器数据。
- 📚 **知识库支持**：创建压缩文档索引（agents.md）和结构化工作流（Next.js skills），为智能体提供框架特定知识，减少幻觉（hallucination）。
- 🔄 **持续优化方向**：正在通过`npx @next/codemod`自动生成项目文档索引，并计划将智能体上下文支持直接集成到`next dev`中，实现零配置体验。

---

### [React 的 useTransition：你可能用错的钩子](https://www.nutrient.io/blog/react-usetransition-guide/)

**原文标题**: [React’s useTransition: The hook you’re probably using wrong](https://www.nutrient.io/blog/react-usetransition-guide/)

本文介绍了如何利用 AI 助手进行搜索、提问和获取代码示例，以提高开发效率和问题解决能力。

- 🔍 通过搜索功能快速查找所需信息
- 🤖 向 AI 助手提问以获得个性化解答
- 💻 获取实用的代码示例和解决方案
- 📚 浏览搜索结果以深入了解相关主题

---

### [GitHub - Blazity/next-migration-skills](https://github.com/Blazity/next-migration-skills)

**原文标题**: [GitHub - Blazity/next-migration-skills](https://github.com/Blazity/next-migration-skills)

这是一个用于将 Next.js 项目从 Pages Router 迁移到 App Router 的代理导向工具包，包含多个技能模块，旨在通过 AST 分析和转换工具自动化迁移过程。

- 🛠️ **核心工具包**：提供 AST 分析和转换工具（ts-morph），是所有其他技能的基础依赖
- 📊 **迁移评估**：分析代码库复杂性和迁移准备情况
- 📋 **迁移规划**：创建分阶段迁移计划
- 🔗 **依赖映射**：将旧依赖映射到 App Router 等效项
- 🛣️ **路由转换**：将 pages/路由转换为 app/路由结构
- ⚛️ **组件迁移**：迁移组件以实现 RSC 兼容性
- 📡 **数据层迁移**：迁移数据获取和 API 路由
- ✅ **验证测试**：在每个阶段后验证正确性

---

### [移除 Next.js 让我明白为何框架对 AI 依然至关重要](https://zenn.dev/smartvain/articles/coding-agent-kills-framework-nextjs-reverse-truth?locale=en)

**原文标题**: [Removing Next.js Taught Me Why Frameworks Are Still Essential Even for AI](https://zenn.dev/smartvain/articles/coding-agent-kills-framework-nextjs-reverse-truth?locale=en)

本文作者通过移除 Next.js 框架并尝试使用纯 HTML/JS 配合 AI 编码助手进行开发后，得出了一个反直觉的结论：在 AI 时代，框架不仅没有过时，反而因其能提供明确的开发规范而变得更为重要。框架的约定成为了人类与 AI 协作的“共同语言”，有效减少了认知偏差和代码不一致性，其核心价值从提供工具转变为定义协作协议。

- 🧪 作者实验性地将 Next.js 项目重写为纯 HTML/JS，初期 AI 能顺利生成代码，但在后续协作中出现了文件位置和代码结构不一致的问题。
- 🤔 网络上的“反框架派”认为 AI 降低了框架的学习成本，而“挺框架派”则强调框架能避免重复造轮子，但作者认为两者都未触及核心痛点。
- 🧠 作者发现，框架的约定（如文件结构）实质上是给 AI 的明确“指令集”。在没有框架时，AI 每次都需要自行判断代码组织方式，导致与开发者的预期产生偏差。
- 🔄 在 AI 时代，框架的价值发生了“反转”：其提供现成工具的价值在下降，但作为“统一团队（包括 AI）规范”的价值却在急剧上升。
- 🤝 框架约定成为了人类与 AI 协作的“共同协议”或“约束”，极大地稳定了 AI 的代码输出，替代了复杂的提示工程。
- 🏗️ 结论是：框架不会消亡，但其存在意义将从“为人类提供便利”转变为“为人机协作提供通用协议”。明确的规则在加入了容易“遗忘上下文”的 AI 成员后变得更为关键。

---

### [虚拟滚动处理数十亿行数据——来自 HighTable 的技术 | Hyperparam 博客](https://blog.hyperparam.app/hightable-scrolling-billions-of-rows/)

**原文标题**: [Virtual Scrolling for Billions of Rows — Techniques from HighTable | Hyperparam Blog](https://blog.hyperparam.app/hightable-scrolling-billions-of-rows/)

本文介绍了 HighTable 组件中用于在浏览器中处理数十亿行数据表格的垂直滚动技术，通过五种方法实现高性能和可访问性。

- 🧠 **惰性加载**：仅加载当前可见的单元格数据，避免一次性加载全部数据，显著减少内存占用。
- ✂️ **表格切片**：只渲染可见的行，而非整个表格，大幅减少 HTML 元素数量，提升渲染性能。
- ♾️ **无限像素**：通过设置画布最大高度并降低滚动条分辨率，突破浏览器对元素高度的限制，支持海量行数。
- 🎯 **像素级精确滚动**：结合全局和局部两种滚动模式，允许用户通过滚动条快速跳转，同时支持鼠标滚轮进行精细滚动。
- 🎹 **两步随机访问**：将垂直和水平滚动逻辑分离，支持通过键盘或程序跳转到任意单元格，确保导航的准确性和流畅性。

---

### [Next.js 甘特图教程 – SVAR React 甘特图 | SVAR 博客](https://svar.dev/blog/nextjs-gantt-chart-tutorial/)

**原文标题**: [Next.js Gantt Chart Tutorial â SVAR React Gantt | SVAR Blog](https://svar.dev/blog/nextjs-gantt-chart-tutorial/)

本教程介绍了如何在 Next.js 项目中集成 SVAR React Gantt 图表，涵盖从创建项目到解决常见集成问题的完整步骤。

- 🚀 **Next.js 与 SVAR Gantt 的集成优势**：Next.js 作为流行的 React 元框架，结合 SVAR Gantt 可快速构建交互式项目时间线，节省大量开发时间。
- ⚙️ **快速集成步骤**：通过创建 Next.js 应用、安装 SVAR Gantt 包、添加客户端组件和 CSS 样式，可在 20 分钟内实现基础功能。
- 🎨 **主题与样式配置**：使用 Willow 主题提供一致视觉风格，并通过 CSS 调整确保图表全高度显示。
- ⚠️ **处理水合警告**：可通过忽略警告或使用客户端渲染来避免 SSR 与客户端渲染间的属性不匹配问题。
- ✏️ **启用任务编辑功能**：通过集成 Editor 组件，用户可双击任务在侧面板中编辑详细信息，提升交互性。
- 📚 **后续学习方向**：教程后续将涵盖创建 API 路由、数据库持久化及服务器同步等进阶主题，以构建生产级调度模块。

---

### [我们如何将 INP 降低 100 毫秒以上：GTM 隔离、React 编译器与改进的遥测技术 - DEV 社区](https://dev.to/subito/how-we-reduced-inp-by-100ms-gtm-isolation-react-compiler-and-better-telemetry-315g)

**原文标题**: [How We Reduced INP by 100ms+: GTM Isolation, React Compiler, and Better Telemetry - DEV Community](https://dev.to/subito/how-we-reduced-inp-by-100ms-gtm-isolation-react-compiler-and-better-telemetry-315g)

Subito 团队通过隔离第三方脚本、启用 React 编译器及改进监控，成功将关键页面的 INP 指标降低超过 100 毫秒，并提升了核心业务转化率。

- 🎯 **识别瓶颈**：通过 A/B 测试隔离 Google 标签管理器（GTM）和广告脚本（ADV），发现 GTM 是广告详情页 INP 超标的主因。
- 🔍 **精准优化**：与营销团队协作，采用二分法定位并移除了拖慢性能的 TikTok 跟踪脚本，使 INP 从 208 毫秒降至 170 毫秒。
- 📊 **增强监控**：集成 Grafana Faro 和 web-vitals 库，实现 INP 问题脚本和 DOM 元素的精准溯源。
- ⚡ **编译器助力**：升级至 Next.js 16 并启用 React 编译器，列表页 INP 从 345 毫秒显著下降至 271 毫秒。
- 📈 **业务提升**：优化后四周内，“广告浏览/访问”比率同比上升 5.3%，证实性能改进直接促进用户转化。
- 🤝 **协作优先**：强调通过跨团队沟通解决根本问题，避免不可持续的技术“取巧”方案。
- 🚀 **未来规划**：建立自动化告警机制，设定性能预算（如 GTM/ADV 各限 50 毫秒），将核心 Web 指标视为业务标准持续优化。

---

### [介绍 Geist Pixel - Vercel](https://vercel.com/blog/introducing-geist-pixel)

**原文标题**: [Introducing Geist Pixel - Vercel](https://vercel.com/blog/introducing-geist-pixel)

Geist 字体家族新增 Geist Pixel 系列，这是一款基于像素网格设计的位图风格字体，延续了 Geist Sans 和 Geist Mono 的系统化设计理念，注重功能性、可扩展性和现代产品适配性。

- 🧱 **系统化扩展**：Geist Pixel 并非装饰字体，而是包含五种独立变体（方形、网格、圆形、三角形、线条）的功能性字体系统，专为真实产品场景设计。
- 🔍 **网格化精密设计**：每个字形基于统一像素网格构建，兼顾怀旧感与现代感，通过手动优化确保小尺寸清晰度与大尺寸表现力。
- ⚙️ **开发友好集成**：提供 npm 安装包和 CSS 变量，支持与现有 Geist 字体混合使用，垂直度量标准保持一致，避免布局冲突。
- 🌐 **多场景适用性**：专为网页与现代产品设计，适用于横幅、仪表板、实验性布局等 UI 场景，支持 32 种语言和 7 种样式集。
- 🚀 **内部验证与未来规划**：已在 Vercel 内部产品探索中应用，同时 Geist Serif 字体已在开发中，延续系统化设计思路。

---

### [GitHub - vercel-labs/portless：用稳定的、命名的.localhost URL 替代端口号。为人类与智能体设计。](https://github.com/vercel-labs/portless)

**原文标题**: [GitHub - vercel-labs/portless: Replace port numbers with stable, named .localhost URLs. For humans and agents.](https://github.com/vercel-labs/portless)

Portless 是一个开发工具，用于将本地开发服务器从传统的端口号访问（如 `localhost:3000`）替换为稳定的、命名的 `.localhost` 域名（如 `myapp.localhost:1355`），旨在解决端口冲突、记忆困难等问题，并为人类和 AI 代理提供可靠的访问地址。

- 🚀 **核心功能**：通过一个运行在 1355 端口的代理，将形如 `<应用名>.localhost:1355` 的请求转发到对应的本地开发服务器。
- ⚙️ **快速上手**：全局安装后，使用 `portless <应用名> <启动命令>` 即可运行应用并通过专属域名访问。
- 🧩 **解决痛点**：消除端口冲突、避免记忆端口号、防止浏览器历史混淆、解决跨端口 Cookie/localStorage 问题，并帮助 AI 代理准确找到服务。
- 🔧 **灵活配置**：支持子域名、可集成到 `package.json` 脚本中，并能自动为应用分配随机端口（4000-4999）。
- 🔒 **HTTPS/HTTP2支持**：可一键启用 HTTPS 和 HTTP2，自动生成并信任证书，以提升开发服务器加载速度。
- 📜 **丰富命令**：提供代理控制（启动/停止）、查看活动路由、信任证书等多种命令。
- 🛠️ **开发友好**：项目本身是使用 Turborepo 的 pnpm monorepo，便于贡献和构建。

---

### [GitHub - ipikuka/next-mdx-remote-client：一个用于`Next.js`应用的`@mdx-js/mdx`封装器，用于加载MDX内容。它是`next-mdx-remote`的一个分支。](https://github.com/ipikuka/next-mdx-remote-client)

**原文标题**: [GitHub - ipikuka/next-mdx-remote-client: A wrapper of `@mdx-js/mdx` for `Next.js` applications in order to load MDX content. It is a fork of `next-mdx-remote`.](https://github.com/ipikuka/next-mdx-remote-client)

next-mdx-remote-client 是一个用于 Next.js 应用的 MDX 内容加载库，它是 next-mdx-remote 的一个分支，支持 MDX 版本 3，并为 Next.js 的 App Router 和 Pages Router 提供了专门的功能。

- 🚀 **支持 MDX 版本 3**：完全兼容最新的 MDX 特性。
- 🔧 **双路由支持**：为 App Router 和 Pages Router 提供独立的组件和函数。
- 🛡️ **内置错误处理**：在编译和渲染过程中提供内部错误处理机制。
- 📦 **导入/导出语句支持**：允许在 MDX 中使用 import 和 export 语句（App Router 支持导入，Pages Router 仅支持导出）。
- 📄 **轻松获取 Frontmatter**：提供 `getFrontmatter` 实用工具，无需编译即可提取元数据。
- 📑 **简易目录生成**：通过 `vfileDataIntoScope` 选项，可将插件数据（如目录）传递到作用域中。
- 🧩 **组件与类型导出**：导出 `@mdx-js/mdx` 的组件和类型，减少额外依赖。
- ⚠️ **安全考虑**：强调 MDX 的安全风险，建议对不受信任的内容进行清理，并提供了禁用 ESM 块的选项。
- 📚 **丰富的插件生态**：作者贡献了多个 Remark、Rehype 和 Recma 插件，以增强 MDX 处理能力。
- 📦 **安装灵活**：支持 React 18 和 React 19，可通过 npm 或 yarn 安装。

---

### [发布 7.4.0 版本 · prisma/prisma · GitHub](https://github.com/prisma/prisma/releases/tag/7.4.0)

**原文标题**: [Release 7.4.0 · prisma/prisma · GitHub](https://github.com/prisma/prisma/releases/tag/7.4.0)

Prisma 发布了 7.4.0 稳定版本，引入了查询缓存层以提升性能，并新增了对部分索引（筛选索引）的支持，同时修复了多个社区贡献的 bug。

- 🚀 **查询缓存层**：通过缓存查询计划减少重复编译，提升高并发下的应用吞吐量。
- 📊 **部分索引支持**：允许为特定条件创建索引，减小索引大小并优化查询性能，支持 PostgreSQL、SQLite、SQL Server 和 CockroachDB。
- 🐛 **Bug 修复**：包括修复 PostgreSQL 迁移中 `CREATE INDEX CONCURRENTLY` 的使用问题、MySQL 和 CockroachDB 的 BigInt 精度丢失、非 ASCII 数据库名称连接失败等。
- 💼 **企业支持**：提供企业级支持计划，涵盖架构集成、性能调优、安全合规等专业服务。
- 🌟 **社区贡献**：多个修复来自社区贡献，体现了活跃的开发者协作。

---

### [终端用户的下一个对象存储界面 | Tigris 对象存储](https://www.tigrisdata.com/blog/tigris-cli/)

**原文标题**: [A terminal user's next interface to object storage | Tigris Object Storage](https://www.tigrisdata.com/blog/tigris-cli/)

Tigris 发布了一款全新的命令行界面工具，专为终端用户设计，让开发者能够直接从 shell 管理对象存储，遵循 UNIX 哲学，提供直观且易于使用的命令。

- 🚀 **全新 Tigris CLI 发布**：专为终端用户打造，可通过 `npm install -g @tigrisdata/cli` 安装，支持跨平台使用。
- 🔄 **直观的命令模式**：采用 `tigris DOMAIN OPERATION <ARGUMENT>` 结构，如 `tigris cp` 支持本地与远程存储间的文件复制。
- 🛠️ **设计过程与规范驱动**：通过 RFC 流程和 `specs.yaml` 规范文件生成 CLI 代码，确保设计一致性和可维护性。
- 📊 **与 AWS S3 命令对比**：提供更简洁的语法，例如 `tigris ls` 对应 `aws s3 ls`，降低学习成本。
- ❓ **常见问题解答**：CLI 免费且开源，支持 Windows/macOS/Linux，兼容 S3 API，并设计为 AI 助手可理解。
- 📦 **核心功能示例**：`tigris cp` 命令支持 `t3://` URL 协议，实现文件上传、下载及桶间操作，行为类似 UNIX `cp`。
- 🌐 **社区与反馈**：鼓励用户通过 GitHub、Discord 等渠道提供反馈，以优化工具设计。

---

### [AGENTS.md 在我们的代理评估中表现优于技能 - Vercel](https://vercel.com/blog/agents-md-outperforms-skills-in-our-agent-evals)

**原文标题**: [AGENTS.md outperforms skills in our agent evals - Vercel](https://vercel.com/blog/agents-md-outperforms-skills-in-our-agent-evals)

我们原本期望通过技能（skills）来教授 AI 编程助手框架知识，但测试发现，将压缩的文档索引直接嵌入 AGENTS.md 文件实现了 100% 的通过率，而技能方法即使在明确指令下最高也只有 79%。被动上下文之所以优于按需检索，主要因为消除了代理的决策点、确保信息始终可用，并避免了顺序问题。

- 🧠 **技能未被可靠触发**：在 56% 的测试案例中，代理从未调用技能，导致表现与无文档时相同。
- 📝 **明确指令提升有限**：添加使用技能的指令后，通过率提升至 79%，但效果受措辞影响大，显得脆弱。
- 🏆 **AGENTS.md 表现卓越**：嵌入压缩文档索引的方法在测试中达到 100% 通过率，全面优于技能方法。
- 🔍 **消除决策点优势**：被动上下文让代理无需决定是否查阅文档，信息始终可用，避免了检索顺序问题。
- 📦 **高效压缩处理**：文档索引被压缩 80% 至 8KB，通过管道分隔结构指向外部文件，既节省上下文又保持效果。
- 🛠️ **实际应用简便**：通过`npx @next/codemod@canary agents-md`命令可自动为 Next.js 项目设置 AGENTS.md。
- ⚖️ **技能仍有特定价值**：技能适用于垂直的、用户明确触发的操作，如版本升级或迁移任务。
- 🧪 **测试与设计建议**：应针对训练数据中未包含的 API 构建评估，并设计便于代理检索的文档结构。

---

### [获取失败](https://atlas9.dev/blog/soft-delete.html)

**原文标题**: [Failed to retrieve](https://atlas9.dev/blog/soft-delete.html)

无法总结：获取内容失败，状态码 206。

---

### [如何为网站挑选合适图标的技巧 - Stéphanie Walter（用户体验研究员兼设计师）](https://stephaniewalter.design/blog/tips-on-how-to-pick-the-right-icons-for-your-website-with-icons8/)

**原文标题**: [Tips on How to Pick the Right Icons for Your Website by Stéphanie Walter - UX Researcher & Designer.](https://stephaniewalter.design/blog/tips-on-how-to-pick-the-right-icons-for-your-website-with-icons8/)

选择适合网站的图标需考虑其意义、文化相关性、风格一致性和使用场景，以确保专业且易于理解。

- 🎯 **明确图标目的**：选择与主题相关的图标，通过同义词工具或图标库（如 TheNounProject）寻找最佳视觉表达。
- 🌍 **注意文化差异**：图标含义可能因文化而异，复杂概念应搭配文字标签，并添加无障碍替代文本。
- 🎨 **保持风格统一**：避免混合不同风格的图标（如填充与线框、单色与多色），确保线条粗细、尺寸和视觉样式一致。
- 📐 **适应显示环境**：根据背景和尺寸选择图标样式，小尺寸宜用简洁形状，深色背景适合单色图标。
- 🔍 **使用同一图标集**：优先从同一图标库（如 Icons8）选取图标，利用其风格筛选功能确保一致性。
- 🎨 **统一配色方案**：若使用多色图标，需调整颜色以匹配品牌调色板，许多高级工具支持直接重新着色。
- 🏆 **参与资源活动**：文章提供赢取 Icons8 三个月许可的机会，需分享文章链接并评论参与。

---

### [客户端与服务器端通用的 React 组件 - Kiril Peyanski](https://gitnation.com/contents/react-components-for-both-the-client-and-the-server)

**原文标题**: [React Components for both the Client & the Server by Kiril Peyanski](https://gitnation.com/contents/react-components-for-both-the-client-and-the-server)

这篇演讲探讨了如何构建同时适用于客户端和服务器的 React 组件，通过分离关注点来兼顾交互性与性能优化。

- 🧩 **混合组件架构**：演讲介绍了构建跨越客户端和服务器的混合组件，旨在保持清晰的职责分离，同时提供交互性和性能。
- 🚀 **性能优势**：服务器组件通过减少捆绑包大小和优化数据获取来提升性能，并能直接访问文件系统和数据库。
- 🔄 **组合模式应用**：通过组合模式，服务器组件可以渲染客户端组件，但反之则不行，这有助于有效整合两者。
- 🛠️ **代码复用策略**：通过创建可在客户端和服务器上运行的“不可知”部分，并视需要包装客户端特定逻辑，来最小化代码重复。
- 📦 **服务器端代码保留**：将如语法高亮等大型库保留在服务器端，可以减少客户端捆绑包大小，从而提升性能。
- 🔧 **交互性添加方法**：通过使用“use client”指令包装服务器组件，添加客户端组件来处理交互逻辑和事件。
- 🌳 **渲染树优化**：保持渲染树不可知，提取客户端部分，使服务器组件能深入渲染树，同时不干扰整体结构。

---

