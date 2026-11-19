### [自动化调试与 AI 根本原因分析 | Sentry](https://sentry.io/resources/automated-debugging/?utm_source=thisweekinreact&utm_medium=paid-community&utm_campaign=automateddebugging-fy27q4-evergreen&utm_content=newsletter-first-sponsor-resource-hub-learnmore)

**原文标题**: [Automated Debugging & AI Root Cause Analysis | Sentry](https://sentry.io/resources/automated-debugging/?utm_source=thisweekinreact&utm_medium=paid-community&utm_campaign=automateddebugging-fy27q4-evergreen&utm_content=newsletter-first-sponsor-resource-hub-learnmore)

Sentry 的自动化调试方案将生产环境 Bug 的检测、根因分析和修复生成串成 AI 代理闭环：Seer 利用堆栈跟踪、源码映射、提交历史、会话回放等上下文快速定位问题并生成修复 PR，并通过 MCP 与 Claude Code、Cursor 等自有代理集成，让工程师从重复调试转向审核与合并。

- 🐞 **自动化调试**：自动完成检测、诊断和修复，减少手工复现、追踪与打补丁。
- 🔍 **检测**：在 PR 发布前或生产上线后捕获 Bug，结合 AI 错误检测与监控获取完整上下文。
- 🧠 **诊断**：Seer 自动进行根因分析，从错误症状追溯到具体代码行，把原本约一小时的本地复现缩短到秒级。
- 🛠️ **修复**：自动生成补丁并创建 PR，还能根据 CI 与评审反馈持续迭代，直到修复合并。
- 📊 **生产上下文**：错误、追踪、会话回放、日志、指标、堆栈跟踪、source maps、提交历史等提升修复准确性。
- 🔗 **MCP 集成**：可连接 Claude Code、Cursor、Windsurf 或任意 MCP 兼容代理，让自有代理查询生产问题并提交修复。
- 🤖 **Seer 能力**：Seer Autofix 负责根因分析与创建 PR；Seer Agent 支持用自然语言查询应用并采取行动。
- 🧩 **工具链联动**：支持 GitHub、GitLab、Bitbucket、Azure DevOps，并可联动 Slack、Linear、Jira、PagerDuty。
- 🔁 **端到端流程**：Sentry 捕获问题后触发自动化流程，代理获取 RCA、生成修复并标记工程师审核，实现“审核并合并”；团队可控制自主程度，人工审核每个 PR 或让代理夜间自动分诊。
- 🚀 **成效与资源**：Bolt 将 MTTD 降低 99%，Supabase 每周崩溃减少 60 倍，Anthropic 600+ 工程师使用；平台提供 54 篇教程、案例与食谱。
- ✅ **上手方式**：在任意付费 Sentry 计划中添加 Seer，连接仓库并开启即可开始自动发现和修复 Bug。

---

### [使用 Seer 构建自动化调试工作流 | Sentry](https://sentry.io/cookbook/self-healing-workflow-seer/?utm_source=thisweekinreact&utm_medium=paid-community&utm_campaign=automateddebugging-fy27q4-cookbook&utm_content=newsletter-first-sponsor-self-healing-seer-trysentry)

**原文标题**: [Build an automated debugging workflow with Seer | Sentry](https://sentry.io/cookbook/self-healing-workflow-seer/?utm_source=thisweekinreact&utm_medium=paid-community&utm_campaign=automateddebugging-fy27q4-cookbook&utm_content=newsletter-first-sponsor-self-healing-seer-trysentry)

Sentry 与 Seer 可组成自动化调试闭环：应用向 Sentry 发送包含堆栈、追踪、日志、指标和回放的丰富上下文，Seer 连接代码库后分析根因、生成修复并创建 PR，或把结构化分析交给 Claude Code、Cursor、GitHub Copilot 等编码代理执行；自动化程度可配置，但最终仍由人工审查和合并。

- 🎯 核心目标：Sentry 捕获问题，Seer 定位根因，并以 Pull Request 或第三方编码代理交付修复。
- ⏱️ 教程约需 20–30 分钟、4 个步骤、难度中等；需安装 Sentry SDK、启用 Seer、拥有 Sentry 项目管理员权限及 GitHub/GitLab 源码库。
- 🧩 第 1 步：确保应用发送丰富上下文，包括堆栈跟踪与面包屑、Tracing 与 Spans、日志、应用指标和 Session Replays。
- 🔗 第 2 步：在 Integrations 中连接 GitHub 或 GitLab，配置 Code Mapping，并在 Seer Settings 选择编码代理和自动化步骤。
- 🔍 第 3 步：可在 Sentry Issues 中点击 Start Analysis 触发根因分析，也可通过 Slack 中的 Seer Agent 调查、分配和解决 issue。
- 🤖 第 4 步：Seer 可自动生成修复并创建 PR，也可将根因与解决方案作为结构化提示交给 Claude Code、Cursor、GitHub Copilot 等代理执行。
- ⚙️ 自动化可设置停止点：仅根因、仅解决方案、PR 草稿，或交给编码代理；即使最自动化，Seer 也不会自行合并代码。
- 🧪 自动 Issue Fix 的触发条件包括至少 10 个事件、近 14 天内出现且具备足够可修复性评分；建议先调整阈值再启用全自动。
- 💡 最佳实践：提供尽量多上下文；先用“Stop after Solution”建立信任；将 Seer 生成的 PR 当作人类 PR 一样审查和测试。
- ⚠️ 常见坑：跳过代码映射、在噪声较多的项目上直接全自动、期待每个问题都能生成可合并 PR、只发送裸异常而缺少追踪和日志。
- 🧭 Sentry MCP Server 免费且只读取已有 Sentry 数据，不消耗事件配额；Seer 使用另行计费，适合处理 Seer 无法看到的私有服务或 monorepo 代码。
- ✅ 最终效果：Sentry 捕获问题、Seer 解释根因、修复以 PR 落地，实现从发现问题到生成修复的自动化工作流。

---

### [推出 UI SDK · UI SDK](https://ui-sdk.dev/docs/core/changelog/introducing-ui-sdk)

**原文标题**: [Introducing UI SDK · UI SDK](https://ui-sdk.dev/docs/core/changelog/introducing-ui-sdk)

overview summary
UI SDK 于 2026 年 11 月 12 日发布，是一个面向组件构建与智能体使用的 TypeScript UI 行为库，提供可组合的键盘导航、焦点、选择、弹层、拖放和 ARIA 等基础能力，并配有跨框架组件库与 Agent 交互支持，目前处于 beta。

- 📅 发布日期：2026 年 11 月 12 日，正式推出 UI SDK。
- 🧩 产品定位：TypeScript UI 行为库，提供组件库底层行为模块，样式由使用者自行提供。
- ⌨️ 核心能力：包含 roving focus、typeahead、popup、焦点管理、选择、拖放及 ARIA 属性等 50+ 行为。
- 🛠️ 组合构建：开发者或 Agent 可组合这些行为来构建自定义组件，例如分享弹层。
- 🖥️ 跨框架组件库：基于相同行为提供 React、Vue、Svelte、Solid 和 Web Components 的 50+ 现成组件。
- 🤖 Agent 友好：提供 createAgent，让 Agent 在权限控制下读取页面并执行点击、输入、选择等操作。
- 🌐 WebMCP 支持：通过 registerTools 让浏览器内置 Agent 读取组件并调用其操作。
- 🚀 上手方式：可复制 setup prompt 让 Agent 自动配置 UI SDK，并查阅组件构建与行为组合文档。
- 🧪 当前状态：UI SDK 处于 beta，部分 API 可能变化，鼓励在 GitHub 上反馈。
- 🙏 致谢来源：借鉴 Radix、Base UI、React Aria、shadcn/ui、Nuxt UI、Geist 及 WAI-ARIA Authoring Practices。

---

### [GitHub - Pagepro/nexity: Nexity is an open source system for starting and growing AI-native websites on Next.js + Sanity. · GitHub](https://github.com/Pagepro/nexity)

**原文标题**: [GitHub - Pagepro/nexity: Nexity is an open source system for starting and growing AI-native websites on Next.js + Sanity. · GitHub](https://github.com/Pagepro/nexity)

Nexity 是一个基于 Next.js + Sanity 的开源 AI 原生网站搭建与增长系统，面向“每次网站变更都需开发者参与”的团队：它为编码代理提供设计系统、区块和 Sanity schema，让市场团队可用 AI 创建新区块，并由开发者在发布前审核。仓库包含基础模板、演示站点、代理层和营销技能插件。

- 🧭 **定位**：开源 AI 原生网站系统，基于 Next.js + Sanity，支持营销与开发协作，代理生成/修改内容，开发者审核后上线。
- 🚀 **快速开始**：需 Node.js 22.12+、pnpm 12.15、Sanity 账号；使用 `npm create sanity@latest -- --template Pagepro/nexity/base`，再运行 `pnpm dev`；站点在 `localhost:3000`，Studio 在 `/admin`。
- 🧱 **仓库结构**：`base/` 为无品牌基础模板；`theme-meridian/` 为完整演示站点；`.agents/` 为代理层；`plugins/nexity-marketing-skills` 为营销技能。
- 🛠 **技术栈**：Next.js 16.4 App Router/Turbopack、React 19.3、Sanity Studio 6.20、Tailwind CSS 4.3 + shadcn/ui、TypeScript 7.0、Zod 4.6、Oxlint/Oxfmt、c15t、Resend。
- 🧩 **页面构建**：约二十多个预设区块，包括 hero、功能网格、bento、分栏、统计、定价、对比表、推荐语、FAQ、联系表单、CTA、列表等，并支持可见性、明暗主题、分隔线和锚点 ID。
- 📚 **内容类型**：页面、博客、案例研究、播客、作者/推荐语/集成库、共享区块、全局区块、页头页脚和站点设置。
- ✍️ **编辑体验**：同域 `/admin` Studio、点击编辑可视化预览、实时草稿预览、发布时标签化重验证、区块画廊。
- 🔁 **SEO 与发布**：CMS 管理重定向/重写（发布后约 2 分钟生效）、页面 SEO 字段、分享图生成、XML 站点地图、`robots.txt` 开关、JSON-LD、发布前 GROQ 检查。
- 🤖 **AI 友好**：提供 `llms.txt`，任意页面 URL 加 `.md` 可获取 Markdown；代理层统一 `AGENTS.md`（如何构建）、`DESIGN.md`（外观）、`BRAND.md`（品牌表达）。
- 🧠 **代理层**：技能覆盖项目初始化、创建区块、修复链接、生成 alt 文本、Sanity 审计；只读 reviewer/auditor 检查样式、schema、GROQ、链接、图片与交付；支持 Claude Code、Codex、Cursor。
- 📈 **营销技能**：面向任意站点/CMS 的只读审计与内容技能，包括品牌套件、站点矛盾、博客质量、内链等，可通过 Claude Code 插件或 `npx skills` 安装。
- ⚠️ **已知限制**：单语言站点；newsletter 表单仅为 UI；CMS 重定向非即时；部分技能需浏览器、Python/Pillow/ImageMagick 或带写权限的 Sanity token；`product-mock` 仅限 Meridian；seed 会覆盖同 ID 文档，需使用新数据集。
- 📄 **许可与支持**：MIT 许可；文档位于各 starter 的 `docs/`，问题提交 GitHub Issues，贡献需参考 `CONTRIBUTING.md`、行为准则和安全政策。

---

### [HTML 优先的 React：结果摘要](https://html-first-react.pages.dev/summary/)

**原文标题**: [HTML-first React: results summary](https://html-first-react.pages.dev/summary/)

HTML-first React 通过新增 `enableFlightHTMLFirst` 标志，让静态内容不再重复进入 Flight 载荷，从而减少下载体积并提升服务端吞吐；该功能需要框架额外传入 `htmlFirst: true` 才会生效，目前属于实验性实现，已提供 Next.js 与 Waku 补丁和演示。

- 📉 **体积显著下降**：41 个测试页的 gzip 下载减少 42.8%，内联 Flight 减少 78.7%，原始 HTML 减少 50.2%，brotli 减少 40.3%。
- 🚀 **吞吐提升明显**：1000 行表格页在 Waku 上提升 3.18×，在 Next.js 16.4 上提升 2.79×；TTFB 约为基线的 0.45× 和 0.40×。
- 🧩 **核心机制**：Flight 用小型 stub 替代静态宿主标记，浏览器水合时采用 HTML 中已有的 DOM；SSR 所需真实内容通过内部注册表传递。
- 🔁 **仅限 HTML SSR 渲染**：框架必须在生成 HTML 的 Flight 渲染中传入 `htmlFirst: true`；导航、刷新、Server Action 响应仍返回完整载荷。
- 🚫 **不 stub 的内容**：Client Components、非 `children` props、表单、输入、图片、SVG、head 元素以及孤立 void 元素如 `<hr>` 不会被 stub。
- 🧠 **浏览器行为**：水合时采用服务端 DOM；未 SSR 的内容以“late rows”到达并在挂载时渲染；Back 导航从 HTML 快照恢复；后续完整载荷若 DOM 相同则保留 stub，变化则原地 patch。
- 🛠️ **Next.js 补丁**：约 165 行，通过 `experimental.htmlFirstFlight: true` 开启；覆盖动态页、PPR、预渲染页、Cache Components 和 `onMissingHTML` 恢复。
- ✅ **正确性验证**：Next.js 52 个端到端套件在 Turbopack 生产模式下 871 项测试全部通过；41 个 Chromium 页面在 DOM、交互、客户端导航和错误检查中全部通过。
- 🔍 **Reconciler 检查**：新增约 40 行、受标志控制的 `instanceMatchesStaticElement`；没有它时表格页首次刷新需 46 ms 并重建 1,044 个节点，有它时 19 ms 且 DOM 不变，接近基线 18 ms。
- 💾 **内存权衡**：使用 HTML 快照比基线更省内存；离开表格页后保留 75 个 DOM 节点和 4.21 MB JS 堆，基线为 256 个节点和 4.35 MB；保留 adopted 节点会留下约 14,000 个分离节点。
- ⚠️ **限制与注意事项**：节省幅度取决于静态标记比例，中位页面仅节省 7.3%；框架仍应实现 `onMissingHTML`；部分 preload 链接可能与基线不同；Firefox/WebKit 未在最终提交上复测。
- 🧪 **可试用**：提供 Next.js 与 Waku  starter，需 Node 22，使用预构建实验包，通过 `npm run build` 和 `npm start` 运行；实验构建不适合生产。

---

### [我们如何利用 AI 让 Next.js 更安全 | Next.js](https://nextjs.org/blog/how-were-using-ai-to-make-nextjs-more-secure)

**原文标题**: [How we're using AI to make Next.js more secure | Next.js](https://nextjs.org/blog/how-were-using-ai-to-make-nextjs-more-secure)

Next.js 团队说明近年安全公告数量上升（2024 年 6 个、2025 年 14 个、2026 年截至目前 51 个）主要因为 AI 让旧代码中的边缘漏洞更容易被发现和利用；团队正通过漏洞赏金、AI 安全机器人、外部审计、每月安全发布、PR 对抗性审查、架构硬化与依赖替换来修复旧问题并预防新问题，同时改进开发者升级体验，让应用更容易保持安全版本。

- 📈 **公告增多不等于更不安全**：2026 年发现的漏洞中，70% 位于至少一年前的代码，43% 位于三年以上的代码，说明 AI 正在帮助挖出长期潜伏的问题。
- 🖼️ **上游依赖也是风险来源**：部分严重漏洞来自图像优化等第三方库，而非 Next.js 自身代码。
- 💰 **漏洞赏金计划**：鼓励研究者在私下报告漏洞，而不是自行利用，许多公告源自赏金报告。
- 🤖 **内部安全机器人**：使用 Eve 开发机器人，协助发现漏洞、分类报告、构建复现、评估严重性并检查修复是否完整。
- 🔍 **外部安全审计**：聘请 Trail of Bits 对 Next.js 进行人工审计，发现其他渠道遗漏的问题。
- 🗓️ **每月安全发布**：建立可预测的安全发布计划，提前公布时间，方便用户和托管商准备升级与防护。
- 🛡️ **PR 对抗性安全审查**：Vercel Agent 的 Security Review 在每个 PR 上以攻击者视角尝试利用改动，已拦截通过代码审查和 CI 但仍存在风险的 PR。
- 🧱 **硬化服务边界**：通过 Adapters 明确定义托管平台与 Next.js 的契约，减少代理、CDN、运行时等层之间的绕过风险。
- 🔄 **替换脆弱依赖**：优先采用内存安全编解码器等更现代方案，并用 AI 加速集成与沙箱迭代。
- ⬆️ **简化安全升级**：从 Next.js 16.4 起，`next dev` 和 `next build` 会提示已知漏洞；DevTools 提供 Vulnerability Insight；`npx next@canary upgrade --agent` 可检查公告并交由编码代理完成安全升级。
- 🚀 **未来展望**：团队将继续调查报告、强化 PR 审查并降低升级门槛，对 Next.js 安全的未来保持乐观。

---

### [Remix v3：快速页面，精简生态](https://marmelab.com/blog/2026/11/12/remix-v3-fast-pages-thin-ecosystem.html)

**原文标题**: [Remix v3: Fast Pages, Thin Ecosystem](https://marmelab.com/blog/2026/11/12/remix-v3-fast-pages-thin-ecosystem.html)

文章记录了 Marmelab 用 Remix v3 与 TanStack Start 分别构建同一房地产演示站 Keyhaven，并由 Claude Code 辅助开发，重点比较服务端组件/岛屿架构、表单、测试、性能与生态，最终认为 Remix v3 适合小型独立项目，而多数项目仍推荐 TanStack Start。

- 🧱 Remix v3 不再依赖 React，以单一 `remix` 包提供路由、组件模型、资产服务器和测试运行器，无外部依赖。
- 🏠 测试项目 Keyhaven 是巴黎、里昂、尼斯、戛纳的高端房产站，含搜索、筛选、房源详情和管理后台；Supabase 作后端，RLS 为信任边界，两框架共享 `domain` 包中的 Zod 模型、校验和数据访问。
- 🤖 开发使用 Claude Code，配合 Context7 读取最新文档、Ponytail 追求最短 diff、框架自带 skill、规则集和 agent team。
- 🎨 Remix v3 没有 Vite 和插件系统，Tailwind 需并跑 CLI 并手动接入资产服务器，多一个进程；TanStack Start 用 Vite 一行插件即可。
- 🏝️ Remix 组件默认只在服务端渲染且不发送 JS，只有 `clientEntry` 标记的 island 才水合；props 必须可序列化，island 不共享组件树，状态通过 `domain` store 同步。
- 🔁 Remix 组件是 setup 函数返回 render 函数，状态在闭包中，只有调用 `handle.update()` 才重渲染；忘记调用会导致 UI 陈旧且无报错，代理倾向少用客户端状态。
- 📝 Remix 表单为纯 HTML、无客户端状态，服务端用同一 Zod schema 校验，每个错误一次往返；因共享 schema 需 `Object.fromEntries()` 转换 `FormData`，专用项目可用 `f.object()` 直接校验。
- 🧪 Remix 测试用 CSS 选择器（`$`/`$$`）和 `act`，API 接近 Vitest 但为独立 runner，浏览器测试需从仓库根运行；TanStack 用 Vitest browser mode + Testing Library 角色查询，更易读。
- ⚡ 性能：FCP 基本相同（约 1.44–1.48s）；Remix LCP 约 1.52–1.54s，比 TanStack 的 1.80s 快 0.26–0.28s；Remix TBT 近 0ms，TanStack 44–60ms；Remix 发送 132KB JS，TanStack 为 490KB。
- ⚠️ Lighthouse 默认模拟节流曾显示 2.5× 差距，但 DevTools 真实节流下消失；性能不应成为框架选择依据，测性能应使用 DevTools throttling。
- ✅ 结论：Claude Code 对 Remix v3 开箱可用，四个功能不到一天完成，评审只发现一个真实错误；最大短板是生态与工具集成，如 Vite 插件和 Vitest，UI 库缺失可由代理快速写组件缓解，`@remix-run/ui` 或可补位。
- 🧭 Marmelab 多数项目仍推荐 TanStack Start（团队熟悉 React）；Remix v3 适合依赖少的小型独立项目，大型项目因缺少自动响应式和良好生态集成暂不推荐。

---

### [看不见的形状](https://sorenblank.com/craft/the-invisible-shape)

**原文标题**: [The Invisible Shape](https://sorenblank.com/craft/the-invisible-shape)

本文围绕上下文菜单中的子菜单交互展开，解释了一个常被忽视却影响体验的“隐形安全区”问题：当用户从父菜单项斜向移动到子菜单时，系统如何判断用户意图并避免子菜单误关闭。文章从菜单历史、人机交互原理讲到多种现代实现方案，并讨论了无障碍与未来浏览器原生支持的可能性。

- 🖥️ 上下文菜单无处不在，但包含大量选项的菜单需要靠子菜单分层折叠；核心难题是鼠标斜向移动时容易滑出父项，导致子菜单瞬间关闭。
- 🕰️ 1976 年 Xerox Alto 的 Smalltalk-76 首次实现弹出式上下文菜单，Dan Ingalls 的 BitBlt 技术让菜单能快速覆盖和消失；1979 年 Steve Jobs 参观 Xerox PARC 后推动了 GUI 普及。
- 🍎 1984 年初代 Mac 没有子菜单，直到 1987 年 Mac II 和 Mac SE 才出现，子菜单的交互问题也由此开始。
- 📐 问题本质与 Steering law 有关：从父项横向移动到子菜单，就像穿过一条又长又窄的隧道，而人手通常走弧线而非直线，因此容易滑出；Tog 提出用“<”形缓冲区作为隐形安全区。
- ⏱️ 固定超时方案并不理想：对动作慢的用户太快，对动作快的用户又太慢；微软曾让子菜单在滑出后保留约半秒，也被 Tog 批评为“恰好相反”。
- 🎨 Hakim El Hattab 使用动态曲线 SVG 桥接父项与子菜单，路径更贴近光标自然轨迹，从而减少误触。
- 🔺 “安全三角形”用不可见区域连接光标与子菜单边角；但若用真实 DOM 实现，需要随鼠标频繁重绘，快速甩动可能跟不上，还会遮挡下方菜单项。
- 🛒 Amazon 的无延迟方案用纯数学判断光标是否位于三角形内；其专利 US9733783B1 实际使用三个三角形加一个小圆，参数来自大量用户移动数据。
- 🧠 Base UI 通过光标速度预测用户意图，每次 mousemove 都检查是否朝子菜单移动、是否太慢或停止；React Aria 更重视可访问性，会放宽角度、连续两次错误才关闭，并跳过触控和手写笔场景。
- ♿ 速度检查对运动障碍用户可能不友好，因此需要更宽容的策略；macOS 的安全三角形只保护进入子菜单的方向，返回父菜单时并不会保留。
- 🌐 目前各 UI 库各自实现类似机制；Open UI 正在讨论让浏览器原生处理悬停延迟和安全区域，未来开发者可能不再需要重复实现。

---

### [当一次导入变成 Zip 炸弹：Next.js 中的打包回归——Sergey Patrakeev](https://bra31k.dev/en/blog/bundle-size-regressions/)

**原文标题**: [When an import becomes a zip bomb: bundle regressions in Next.js — Sergey Patrakeev](https://bra31k.dev/en/blog/bundle-size-regressions/)

overview summary
本文讲述 Next.js 项目如何应对隐蔽的包体积回归：一次仅新增 7 KiB 代码的 PR 却让页面首屏包体增加 153 KiB，团队因此开发并开源 route-bundle-size，通过预算、压缩测量与 merge-base 对比在 CI 中阻止体积膨胀，并分享了误报、barrel import、AI 辅助修复和优化验证等经验。

- 💣 一次 PR 中新增代码仅 7 KiB，却使页面首屏包体增加 153 KiB；人工评审未发现，体积检查成功拦截。
- 🧰 官方工具难以直接用于 CI：Next.js 移除了 First Load JS 和 manifests，@next/bundle-analyzer 仅支持 webpack，next experimental-analyze 主要面向人工分析。
- 🔍 团队从构建产物中发现未文档化的 route-bundle-stats.json，并实现 measure 与 diff 命令，支持压缩体积、预算和报告比较。
- ⚠️ 初版以 preview 对比 main 产生大量误报：约一半失败为 false positives；与 main 同步的分支失败率 5.7%，落后 20+ commits 的分支达 43%。
- 🌿 改为 merge-base 流程：获取当前构建产物，获取 merge-base 产物（缓存或重建），再比较并更新 summary，减少分支未同步导致的误报。
- 🧩 典型案例：AI/agent 通过 barrel 导出新模块，与 style 页面重构合并后把 engine 代码拉入样式页；最终修复 4 处导入并将模块拆到独立 slice。
- 🛡️ 若无体积守卫，应用整体可能增长约 200 KiB；检查让问题在上线前暴露，避免长期留在生产环境。
- 🎉 体积监控也验证优化成果：删除旧 UI 的 220 个文件、19,354 行代码后，/projects 首载 JS 降低 26%，22 条路由变轻。
- 🧭 route-bundle-size 说明“发生了什么”，Next.js 官方 analyzer/next analyze 说明“为什么”；可附加官方报告，并用 next-bundle-optimizer 辅助修复。
- 🚀 工具已开源为 route-bundle-size（npm/GitHub），支持 per-route budgets；需注意 Next.js 产物格式未文档化，目前主要关注 first-load JS。

---

### [fate 2.0 有什么新变化？ | fate](https://fate.technology/posts/whats-new-in-fate-2.0)

**原文标题**: [What's new in fate 2.0? | fate](https://fate.technology/posts/whats-new-in-fate-2.0)

fate 2.0 已发布，从面向 Async React 的现代数据客户端扩展为同时支持 GraphQL、本地状态与离线数据的完整数据层，并在 Athena Crisis 生产环境中替代 Relay 与 TinyBase，带来更少代码、更好性能和更快交互。

- 🚀 新增完整 GraphQL 支持，包括流式与延迟数据加载，并可通过 Vite 插件生成 TypeScript 类型。
- 🖼️ 新增 Vue 支持，vue-fate 提供 views、requests、mutations、实时更新与 Suspense 集成。
- 🗂️ 可管理客户端状态：扩展服务端类型、构建纯客户端应用、执行客户端 mutation，并用 IndexedDB 持久化。
- 🧮 引入 memo 派生字段，跨视图共享计算结果，依赖变化时自动更新，避免重复计算。
- 📴 离线 mutation 会先保存到设备，联网后重试；支持等待本地持久化、原子写入和数据迁移。
- ⚡ 支持 SSR 缓存水合：服务端加载的数据可通过 dehydrate/hydrate 传给浏览器复用。
- 🧩 新增视图参数、条件选择、字段别名、viewFor 按结果类型组合视图，以及列表读取、刷新、取消和超时等能力。
- 🔁 Mutation 支持显式列表插入、移除与定向失效，失败时可回滚。
- ☁️ 默认通过 Void 部署到 Cloudflare，vp create fate 可快速创建项目并选择 UI、后端、i18n 或纯客户端应用。
- 📈 性能与可靠性提升：请求处理时间约减少 35%，内存占用约减少 45%，并修复并发 mutation、陈旧响应、分页、实时更新、鉴权与错误恢复等问题。
- 🧱 与 Void、Astryx 组成首个完整 Async React 技术栈，让搜索等交互保持流畅、可中断，减少手写 useEffect 协调。
- 🛠️ 可通过 vp create fate 或 pnpm create fate 试用，并反馈问题。

---

### [GitHub -](https://github.com/declarative-dragging/dragology)

**原文标题**: [GitHub - declarative-dragging/dragology: Declarative dragging for SVG on the web · GitHub](https://github.com/declarative-dragging/dragology)

Dragology 是一个用于在 Web 上为 SVG 构建高质量、新颖拖放界面的声明式拖拽库，采用模型驱动与可组合的拖拽理念；仓库提供安装方式、示例、演示和开发说明，但尚未准备正式文档。

- 📦 可通过 `npm install dragology` 安装，也可使用其他包管理器。
- 🧠 核心概念包括模型驱动拖拽与可组合拖拽，建议先从 Declarative Dragging 主页及相关视频/PDF 了解。
- 🧪 `examples/consumer` 是 Vite 项目中导入和使用 Dragology 的自包含示例。
- 🎮 仓库包含大量演示，可在线上体验，并在 `src/demos` 查看实现方式。
- 🤖 `docs/AGENTS.md` 由 LLM 编写，面向使用该库的 LLM，作为正式文档缺失时的替代资源。
- 🛠️ 开发本仓库需克隆后运行 `pnpm install` 和 `pnpm run dev`，再打开本地 Vite 开发服务器。
- 📄 根目录 `AGENTS.md` 提供仓库开发流程指引。
- ⭐ 仓库数据：759 stars、30 forks、4 watchers、1,072 commits。
- 🏷️ 主题标签包括 direct-manipulation、drag-and-drop、react、svg、typescript。
- ⚖️ 采用 MIT 许可证。

---

### [发布 10.0.0 · bvaughn/react-virtualized · GitHub](https://github.com/bvaughn/react-virtualized/releases/tag/10.0.0)

**原文标题**: [Release 10.0.0 · bvaughn/react-virtualized · GitHub](https://github.com/bvaughn/react-virtualized/releases/tag/10.0.0)

react-virtualized 10.0.0 是一次大规模现代化升级：源码改用 TypeScript，所有组件重写为带 hooks 的函数组件，并要求 React 18+。此次版本包含多项破坏性 API 变更，同时修复了 9.x 架构下长期存在的问题。

- 🔧 **现代化重构**：全面迁移至 TypeScript，组件改为函数组件 + hooks，并使用 `memo` 包装；要求 `react` / `react-dom` 为 `^18.0.0 || ^19.0.0`。
- 📦 **导入方式变更**：移除深路径导入和 UMD 构建，统一从包根导入，例如 `import { List } from 'react-virtualized'`；支持 tree-shaking，提供 ESM 与 CJS 入口。
- 🧩 **AutoSizer 移除**：改用 `react-virtualized-auto-sizer` 2.x，通过 `renderProp` 或 `ChildComponent` 使用；宽高在测量前为 `undefined`。
- 🔁 **滚动控制改为 ref API**：移除 `scrollToIndex`、`scrollToRow`、`scrollTop` 等受控滚动 props，改用 `*ImperativeAPI` ref 方法，如 `scrollToRow({ index, align })`、`scrollToCell()`、`scrollToPosition()`。
- 🧭 **初始滚动位置**：新增 `initialScrollTop` / `initialScrollLeft`，支持首次挂载及服务端渲染时设置初始滚动位置。
- 🪟 **WindowScroller 移除**：改用 `scrollElement="window"` 或传入可滚动元素；组件自动测量位置，移除 `autoHeight`、`autoWidth`、`scrollTop`、`scrollLeft`、`isScrolling` 等 props。
- 🎯 **ScrollSync / ArrowKeyStepper 变更**：子组件通过 `registerChild` ref 回调连接，不再依赖受控滚动 props。
- 🗑️ **Collection 移除**：`Collection` 及其相关样式被删除，且没有直接替代方案。
- 🧱 **Table Column 变更**：不再支持 `Column` 子类，改用包装组件；`Table` 会把 `defaultColumnProps` 应用于任意子元素。
- 📐 **CellMeasurer 要求可测量节点**：子元素必须是 DOM 元素或能转发 `ref` 的组件，否则使用 `registerChild`；无可测量节点时会记录 DEV 警告。
- 🧾 **类型增强**：为各组件 props、命令式句柄和渲染参数新增 TypeScript 类型，如 `GridProps`、`ListProps`、`TableProps`、`ColumnProps`、`*ImperativeAPI` 等。
- 🐛 **关键修复**：修复 React 19 下 `Table` 崩溃、`Grid` 在 StrictMode/并发渲染中的问题，以及 `Masonry`、`MultiGrid`、`InfiniteLoader`、`CellMeasurerCache` 性能与测量相关问题；窗口滚动场景下的 `scrollToRow` 等方法也已修复。
- 🧹 **依赖精简**：移除 `react-lifecycles-compat`、`prop-types`、`@babel/runtime`、`loose-envify`；样式仍可通过 `react-virtualized/styles.css` 引入。
- 📚 **文档更新**：新增文档站点与在线示例：`https://react-virtualized-docs.vercel.app/`。

---

### [发布 · bvaughn/react-resizable-panels · GitHub](https://github.com/bvaughn/react-resizable-panels/releases)

**原文标题**: [Releases · bvaughn/react-resizable-panels · GitHub](https://github.com/bvaughn/react-resizable-panels/releases)

该页面汇总了 `bvaughn/react-resizable-panels` 从 4.18.1 到 4.24.1 的发布说明，核心围绕 `Workspace` 标签页与面板布局能力增强、拖拽/浮动窗口支持、可访问性组件、性能优化以及多项缺陷修复。

- 🧩 4.24.1：修复打开 popover（如 `<div popover>`）后 `Separator` 仍可被拖动的问题，包括渲染在 `Group` 内的 popover。
- 🪟 4.24.0：`Workspace` 移动标签时，在支持 `moveBefore` 的浏览器中不再重载 iframe、暂停媒体或让焦点元素失焦；点击已展开的可折叠/浮动标签组的当前标签可折叠，禁用状态下行为调整，边缘拖放目标可加入折叠标签组。
- 🛡️ 4.23.0：新增 `onBeforeModelChange` 可拦截用户操作；新增 `resizeSplit`、`dragSourceInfo`、`addTab` 的 `target/size` 等能力；`classNames/styles` 支持函数；新增 `lazyTabContent`；`hiddenTabBehavior` 扩展到不可见标签。
- 🖱️ 4.22.0：新增 `startExternalDrag`、`acceptExternalDrop`、`useTabListOverflow`、`usePopoutWindows`；支持复制标签/标签组；弃用 `onTearOff`，建议用弹出窗口按钮替代。
- 🧾 4.22.1：`Workspace` 标签内表单控件不再触发选择/拖拽标签，可用 `data-tab-ignore` 自定义排除；修复 `preserve-pixel-size` 面板和 Grid 轨道在约束变化、折叠恢复时尺寸异常。
- 🧰 4.21.0：新增 `TabsetCollapseButton` 与 `TabsetMaximizeButton`，带 ARIA 状态；关闭按钮、拖拽手柄和新按钮的 `children/className/style/title` 支持函数；修复分数像素漂移。
- 🪟 4.20.0：`Workspace` 支持浮动标签组，可通过 `floatTab`、`floatTabset` 创建，`collapseTabset` 折叠，`moveTabset` 停靠；支持拖到工作区边缘生成侧边栏/底部面板；注意 `TabDropTarget` 新增 `{ edge }` 变体。
- ⚡ 4.19.1：提升缩放和拖拽性能，无 `onResize` 的 `Panel` 不再被观察；生产构建移除开发警告；有 `dragGroup` 时 `disableDrop` 仅在拖放目标变化时调用。
- 🔗 4.19.0：新增 `onTearOff` 支持拖出窗口；新增 `dragGroup` 支持跨 `Workspace`/窗口/应用副本拖拽标签；修复空工作区拖放指示器，支持指示器动画；警告拖放指示器不再是 tab panels 子元素。
- ↔️ 4.18.1：修复标签列表被压缩到 0px 后剩余空间不更新；修复 RTL 布局下的拖拽插入、方向键移动和左右边缘拖放行为。

---

### [发布 v3.1.0 · staylor/react-helmet-async · GitHub](https://github.com/staylor/react-helmet-async/releases/tag/v3.1.0)

**原文标题**: [Release v3.1.0 · staylor/react-helmet-async · GitHub](https://github.com/staylor/react-helmet-async/releases/tag/v3.1.0)

本次为 react-helmet-async v3.1.0 发布，重点修复 package.json 导出遗漏，恢复 React 19 下 `<Helmet>` 实例合并行为，并改进属性处理、错误提示、事件处理和构建兼容性，同时移除 `invariant` 与 `shallowequal` 依赖。

- 📦 新增 `react-helmet-async/package.json` 导出，修复 3.0.0 中 `exports` 映射遗漏的问题。
- ⚛️ React 19 下恢复挂载后 `<Helmet>` 实例合并：最内层 `<title>` 生效，并使用最近的 `titleTemplate` 和 `defaultTitle`；多个 `<Helmet>` 设置的同一标签只渲染一次，取最内层内容。
- 🖥️ 服务端渲染仍输出每个 `<Helmet>` 的标签；水合时 React 只复用首个服务端渲染的 `<title>`，第二个会保留在 `<head>` 中。
- 🔤 启用 `prioritizeSeoTags` 时，`<meta charset>` 从 `helmet.meta` 移到 `helmet.priority` 开头，以满足浏览器仅识别文档前 1024 字节内 charset 声明的限制。
- 🧾 无效子元素或缺少 `<HelmetProvider>` 时抛出的错误改为普通 `Error`，名称不再是 `Invariant Violation`。
- 🗑️ 移除 `invariant` 和 `shallowequal` 依赖。
- 🛠️ 修复 React 16–18 下缺少 `<HelmetProvider>` 或 `helmetData` 时抛出 `TypeError` 的问题，改为更明确的错误提示。
- 🏷️ 修复 React 16–18 下 `meta`、`link`、`script`、`style`、`noscript` 中使用 React 属性名（如 `itemProp`、`charSet`、`httpEquiv`）时条目被丢弃的问题，并转换为对应 HTML 属性名。
- 🧩 修复多个 fragment 或 fragment 与同类型标签相邻时，fragment 内 `<link>`、`<meta>`、`<noscript>`、`<script>`、`<style>` 被丢弃的问题。
- 🎛️ React 16–18 下函数型 props（如 `onLoad`）改为事件处理器，不再作为包含函数源码的属性写入，`toString()` 也会省略它们；处理器接收原生 `Event`。
- 🧱 `lib/index.js` 和 `lib/index.esm.js` 编译为 ES2018，兼容 webpack 4 及 Create React App 3/4。
- ⏱️ React 16–18 默认 `defer` 开启时，后台标签页中的变更约 1 秒内生效，而不是等标签页重新显示。
- 🔗 仅包含 `target` 属性的 `<base>` 不再被丢弃。

---

### [React Flow 13 - xyflow](https://xyflow.com/blog/react-flow-13-major-release)

**原文标题**: [React Flow 13 - xyflow](https://xyflow.com/blog/react-flow-13-major-release)

React Flow 13 于 2026 年 11 月 16 日发布，距上一个主要版本已有两年。此版本以升级 Zustand 5 来适配 Vite 8 与现代构建为起点，最终扩展为一次重要的性能与开发体验更新；同时，React Flow 的 npm 月下载量从 2024 年的 100 万增长到预计 6000 万，团队还扩展了 Strudel Flow 与 Pro 内容。

- 🚀 React Flow 13 正式发布，重点带来性能改进和开发者体验提升，并提供迁移指南。
- 📈 生态增长显著：月下载量预计达 6000 万，约占 React 下载量的 6–8%；案例包括 Google Stitch、Figma Weave 和 Supabase 的 database.build。
- 🎵 团队推出 Strudel Flow：基于 Strudel 实时编码语言的音乐创作与表演平台，最新版支持社区 patch 投稿。
- 💎 Pro 内容扩展并全部上线 reactflow.dev，新增自由手绘、基于 libavoid 的复杂边路由、AI 工作流构建器模板，并欢迎邮件反馈内容建议。
- ⚙️ 新版本的主要动机是升级 Zustand 5，以解决 Vite 8 和现代构建问题，并在社区 PR 基础上发展为大型流程图性能更新。
- 🧩 状态管理优化：拆分单一 store，改用针对 options、nodes、edges、selections、connections 的专用 hooks；新增 useNode/useEdge 精准订阅，减少不必要重渲染，并构建 xybench 基准工具。
- 🛠️ 开发体验改进：不再发布 UMD，转向 ESM；要求 React 18+，可利用 React Compiler；包内含 src/ 与 source maps，支持编辑器跳转到源码定义。
- 👪 父子节点与分组更易用：父节点不再必须排在子节点之前；useReactFlow 新增 changeParentNode，自动更新父节点边界以包含新子节点。
- 🎨 样式与主题增强：自动检测深色/浅色模式，样式支持分层控制，并导出 xy-theme.css，可通过 @xyflow/react/xy-theme.css 引入。
- 🔗 后续生态动态：官方提供迁移指南与 Pro 订阅支持开发；相关公告包括 Vue Flow 加入 xyflow 并发布 Vue Flow 2、Strudel Flow 2，以及预告将有新内容发布。

---

### [React 剖析 — 3D React 组件检查器](https://react-anatomy.com/)

**原文标题**: [React Anatomy â 3D React component inspector](https://react-anatomy.com/)

React Anatomy 是一款浏览器扩展，为开发者工具新增 Anatomy 面板，把当前页面与 React 实际渲染的组件对应起来；它支持将页面拆分为 3D 图层、查看真实组件树并读取 props，帮助理解、排查和解释页面结构。

- 🧩 通过 DevTools 的 Anatomy 面板连接页面与 React 渲染结果，可拆分 3D 图层、查看组件树和 props。
- 🖱️ 提供交互式示例，无需安装扩展即可体验，也可在文档中查看截图和操作指引。
- 🔌 可从 Chrome Web Store 安装到 Chrome，并兼容 Brave、Edge；Firefox 可通过 Add-ons 安装。
- ✍️ 工具源于作者过去用 Excalidraw 手动画结构图：耗时且基于代码阅读，而非 React 实际渲染。
- 🏗️ 图层来自屏幕上的可见内容，组件名称与嵌套关系来自 React 本身，从运行中的页面生成结构图。
- 🧭 适用场景包括：理解陌生布局、学习 React 组合与数据传递、排查异常、在 PR 中说明改动、阅读 AI 生成代码。
- 🔍 它只展示结构，不做评价；是检查器而非代码审查器，结构是否合理仍由用户判断。
- 🌳 展示当前 React 渲染的组件树，不是 import 依赖图；未出现在屏幕上的组件不显示，渲染多次的组件会出现多次并带各自 props。
- 📐 3D 视图从页面形状出发，自动深度区分可见区域；输出相同的包裹组件共享平面，捕获的组件仍保留在树中。
- ⚙️ 无需修改包或代码即可检查运行中的 React 应用，检查在浏览器内完成。
- ⚠️ 依赖 React 私有内部机制，兼容性和视觉保真度可能变化；文档会说明当前能查看的内容。
- 📚 提供心理模型、捕获限制与兼容性、常见问题等文档资源，帮助理解页面与组件树的连接。

---

### [A2UI 1.0：构建令人愉悦、快速、可靠的智能体体验 - Google 开发者博客](https://developers.googleblog.com/a2ui-10-build-delightful-fast-reliable-agentic-experiences/)

**原文标题**: [
            
            A2UI 1.0: Build delightful, fast, reliable, agentic experiences
            
            
            - Google Developers Blog
            
        ](https://developers.googleblog.com/a2ui-10-build-delightful-fast-reliable-agentic-experiences/)

A2UI 1.0 是 Google A2UI 团队发布的生成式 UI 开放协议首个稳定版，让 AI 智能体以可交互界面（如表单、图表、卡片）回应，而不再只输出大段文本；应用使用自身原生组件安全、低延迟地渲染，并可通过开源渲染器与智能体 SDK 接入。

- 🚀 **正式发布 1.0**：这是首个稳定版本，支持 Web、Android、iOS 渲染器及 Python、TypeScript、Dart 智能体 SDK。
- 🧩 **核心机制**：智能体描述要展示的内容，应用接收 A2UI 消息后用原生组件渲染，兼顾低延迟、高信任与原生体验。
- 🎨 **个性化与品牌一致**：UI 可按用户需求即时生成，并只使用开发者注册的设计系统和组件。
- 🛡️ **生产级能力**：支持 A2UI Express 或“系统一”决策模型选择组件；服务端绑定数据与子组件，敏感值不进入模型，并支持边生成边流式呈现。
- 🔄 **1.0 新特性**：新增双向函数调用、可访问性支持与扩展元数据；渲染器覆盖 React、Angular、Lit、Flutter、SwiftUI，Jetpack Compose 暂为 0.9.1。
- 🌐 **MCP Apps 集成**：A2UI 屏幕可出现在支持 MCP Apps 的 AI 助手中，如 Claude 和 Gemini。
- 🏢 **企业采用**：Atlassian 将 A2UI 用于 Jira 智能体交互卡片；Alation 用其渲染指标卡、图表和 SQL 透明信息；ByteDance 为 Lynx 发布渲染器；Bloomberg 等公司也在构建。
- 🧪 **应用示例**：同一智能体输出可跨手机和笔记本原生呈现，例如整合日历、餐厅订位与打车价格的晚餐安排视图；Gemini Notebook 用卡片询问并确认幻灯片选项。
- 🔮 **后续计划**：Jetpack Compose 1.0 支持即将推出，Gemini Enterprise 将升级至 1.0，路线图还包括跨平台设计系统原语和决策模型官方 SDK 支持。
- 🛠️ **上手方式**：可在 a2ui.org 阅读文档与快速开始，使用 CopilotKit 的 A2UI Playground 体验，并在 GitHub 提交问题与讨论。

---

### [变更日志.md | React Router](https://reactrouter.com/changelog#v851)

**原文标题**: [CHANGELOG.md  | React Router](https://reactrouter.com/changelog#v851)

该页面是 React Router 的完整变更日志索引，汇总了从 v7.0.0 到当前最新 v8.5.2 的发布说明，涵盖版本升级、破坏性变更、新功能、实验性 API、安全修复和补丁更新；当前稳定版为 8.5.2，main 分支尚未发布。

- 📄 页面列出 React Router 自 v7.0.0 起的全部发布记录，并提供 8.5.2、7.18.6、6.30.6、v4/5.x、v3.x 等版本文档入口。
- 🚀 v8 是重大版本：最低要求 Node 22.22.0+、React 19.2.7+、Vite 7+，发布为 ESM-only，并将 tsconfig target/lib 更新到 ES2022。
- 🧩 v8 将多个 v7 future flags 行为设为默认，包括 middleware、passThroughRequests、trailing slash aware data requests、Vite Environment API、splitRouteModules 等。
- 🗑️ v8 移除 react-router-dom，DOM 相关 API 需改从 react-router/dom 导入；同时移除 meta 的旧 data 字段，改用 loaderData。
- 🛠️ v8.5.2 主要是修复：导航元数据一致性、HEAD 请求资源泄漏、Suspense hydration、basename 下表单提交、href/generatePath 校验、redirect 的 302 状态污染等。
- 🆕 v8.5.0 弃用 React Router 自带 view transition API，推荐 React 19.3+ 的 <ViewTransition>；新增 unstable API-only 模式、自定义 fetch 和应用控制路由发现。
- ⚡ v8.4.0 通过更细粒度内部 context 减少无关路由组件重渲染，并实验性引入基于 @remix-run/route-pattern 的高效路由匹配。
- 🌐 v8.2.0 为非 Node 运行时提供 Web Streams 默认 server entry；Node 应用可通过 unstable_enableNodeReadableStream 实验性启用 Web Streams 默认入口。
- 🤖 v8.1.0 让 create-react-router 默认集成官方 Agent Skill，并增强 instrumentation 结果，提供 URL、路由 pattern、params、statusCode 等可观测元数据。
- 🔐 多个版本包含安全公告与修复，例如 v7.12.0 修复 CSRF、开放重定向 XSS、ScrollRestoration SSR XSS；v7.9.0 修复 JSON-LD XSS；v7.5.2、v7.4.1 等修复缓存污染与 Host 头问题。
- 🧪 v7 后期重点包括：稳定 middleware/context、优化路由匹配、type-safe href、route.lazy 对象 API、RSC unstable 支持、loaderData 命名统一、SPA fallback 与预渲染增强。
- 📦 v7.0.0 将 react-router-dom、@remix-run/router、@remix-run/server-runtime 等合并进 react-router，移除 json、defer 等旧 API，要求 Node 20+/React 18+，并默认启用 v7 future flags。
- 🧭 文档同时列出 Framework、Data、Declarative 三种模式，以及 API 参考、教程、升级指南、How-Tos 和社区资源。

---

### [以编程方式、](https://www.remotion.dev/blog/make-videos-programmatically-interactively-and-agentically)

**原文标题**: [Make videos programmatically, interactively and agentically | Remotion | Make videos programmatically](https://www.remotion.dev/blog/make-videos-programmatically-interactively-and-agentically)

2026年Remotion的工作方式已发生变化：Agent Skills成为默认的视频制作方式，Remotion Studio也全面交互化，支持直接选择、拖拽、修剪、裁剪和编辑内容，从而帮助用户更高效地快速迭代视频。

- 🗓️ 文章发布于2026年11月11日，作者是Remotion首席黑客Jonny Burger。
- 🤖 Remotion新增Agent Skills，并已成为使用Remotion制作视频的默认方式。
- 🎬 Remotion Studio实现全面交互，可选中、拖拽、修剪、裁剪和编辑内容。
- ⚡ 新工作流让视频制作更高效，也支持更快速地迭代。
- ▶️ 官方还发布了视频，展示当前最先进的Remotion视频制作与快速迭代方式。

---

### [最快的应用](https://www.thefastest.app/?utm_source=this_week_in_react&utm_medium=email&utm_campaign=launch)

**原文标题**: [The Fastest App](https://www.thefastest.app/?utm_source=this_week_in_react&utm_medium=email&utm_campaign=launch)

该内容来自 Callstack 的移动应用启动指标公开排行榜，基于真实设备测量应用启动速度，并按启动性能与资源占用排名；榜单列出 21 款应用的版本、平均 LCP、FCP、CPU 和 RAM。

- 📱 排名第一的 ShadowLens v1.3.0：LCP 与 FCP 均为 544 ms，CPU 27.8%，RAM 272 MB。
- 🧠 第二名 Mentrick v6.0.0：LCP 736 ms、FCP 369 ms、CPU 12.9%、RAM 218 MB。
- 👻 第三名 Snapchat：LCP 743 ms、FCP 473 ms、CPU 60.6%、RAM 489 MB。
- ▶️ 第四名 YouTube：LCP 783 ms、FCP 678 ms、CPU 21.5%、RAM 344 MB。
- 🛳️ 第五名 Royal Caribbean International：LCP 992 ms、FCP 653 ms、CPU 27.3%、RAM 457 MB。
- 🏠 第六名 Airbnb：LCP 1205 ms、FCP 608 ms、CPU 71.3%、RAM 517 MB。
- 💬 第八名 Discord：LCP 1414 ms、FCP 997 ms、CPU 49.7%、RAM 476 MB。
- 🗺️ 第十二名 Google Maps：LCP 1900 ms、FCP 493 ms、CPU 53.8%、RAM 478 MB。
- 📦 第十五名 Amazon Shopping：LCP 1975 ms、FCP 1477 ms、CPU 146.3%、RAM 826 MB。
- 🍔 第十九名 Uber Eats：LCP 2636 ms、FCP 1122 ms、CPU 142.5%、RAM 649 MB。
- 🚚 第二十名 Bolt Food：LCP 6470 ms、FCP 2028 ms、CPU 86.6%、RAM 538 MB。
- 👗 第二十一名 Zalando：LCP 7139 ms、FCP 2845 ms、CPU 104.1%、RAM 837 MB。
- ⚠️ 资源占用突出项：Expensify RAM 达 1004 MB；Odjazdowy Kraków CPU 达 168.4%；Yazio CPU 达 112.0%。

---

### [推出 Expo Simulators：专为智能体打造的云模拟器](https://expo.dev/blog/introducing-expo-simulators-cloud-simulators-built-for-agents)

**原文标题**: [Introducing Expo Simulators: cloud simulators built for agents](https://expo.dev/blog/introducing-expo-simulators-cloud-simulators-built-for-agents)

您尚未提供需要总结的文章内容，因此目前无法提取关键要点。
- 📭 未检测到正文内容，请粘贴文章后我将按要求生成中文要点摘要。

---

### [精确构建](https://exact.appdrop.app/)

**原文标题**: [exact build](https://exact.appdrop.app/)

您尚未提供需要总结的文章正文，因此暂时无法生成内容摘要。
- 📄 当前消息中“Use the following content:”后没有附带任何文本内容。
- ✍️ 请粘贴或发送文章正文，我将据此提取关键信息并生成摘要。
- ✅ 收到内容后，我会按要求输出中文概述，并使用“-”符号和合适表情符号列出要点。

---

### [无](https://appdrop.app/)

**原文标题**: [None](https://appdrop.app/)

目前未收到需要总结的文章正文，无法生成内容摘要。
- 📄 请提供文章内容后再进行总结
- ✍️ 我会提炼关键信息并整理为简洁要点
- ✅ 输出将使用“-”符号并搭配合适表情符号

---

### [在删除你的 AGENTS.md 之前，请先阅读这篇文章——作者：Jina Yoon](https://newsletter.posthog.com/p/your-agentsmd-is-holding-you-back?utm_source=twir&utm_campaign=nov18)

**原文标题**: [Read this before deleting your AGENTS.md - by Jina Yoon](https://newsletter.posthog.com/p/your-agentsmd-is-holding-you-back?utm_source=twir&utm_campaign=nov18)

文章指出，上下文工程正从“不断补充信息”转向“主动做减法”，避免过多规则和提示反而拖累 AI 智能体。作者建议定期删除或重写 AGENTS.md / CLAUDE.md，并通过人工审查、评估测试和智能体反馈三种方式，让上下文保持精简、准确和可维护。

- 🧠 模型能力提升后，过去必需的上下文可能变成负担；Anthropic 曾移除 Claude Code 系统提示的 80%，Claude Code 创作者也建议每六个月删除 CLAUDE.md 以保持前沿。
- 🩺 先运行 `/doctor` 做基础健康检查：删除冗余提示、发现损坏配置、清理未使用插件、优化懒加载，并估算可节省的 token。
- 👀 `/doctor` 不能判断内容是否正确，仍需人工逐行检查 AGENTS.md；如果说不清某条规则能防止什么失败，就删除它。
- ⚠️ 文章举例：团队暂停 merge queue 后忘记更新 AGENTS.md，导致智能体在 21 小时内给出错误合并指令，说明上下文必须随外部状态同步维护。
- 🧪 把上下文当作代码来测试：每次智能体出错，就记录触发错误的提示到 `failures.md`，修改 AGENTS.md 后重跑这些提示作为回归测试。
- 🔁 PostHog 用约 40 个示例应用运行 Wizard，再由 `pr-evaluator` 评估生成的 PR，从中发现如“跳过安装 PostHog”等问题。
- 💬 直接让智能体反馈上下文缺口：在提示中询问哪些信息本可避免工具失败、错误编辑和无效轮次，并将反馈聚类、验证后用于改进上下文系统。

---

### [RFC: Node-API addons in React Native by kraenhansen · Pull Request #1030 · react-native-community/discussions-and-proposals · GitHub](https://github.com/react-native-community/discussions-and-proposals/pull/1030)

**原文标题**: [RFC: Node-API addons in React Native by kraenhansen · Pull Request #1030 · react-native-community/discussions-and-proposals · GitHub](https://github.com/react-native-community/discussions-and-proposals/pull/1030)

该 RFC 提议让 React Native 应用通过 Hermes 自带的 Node-API 实现加载 Node-API 原生插件，并明确 React Native 作为 Hermes 的 Node-API 宿主，增加 `dlopen` 支持，同时由 Hermes 提供供插件链接的 `node-api` 库。目前该提案仍处于开放讨论阶段。

- 📌 **提案编号**：react-native-community/discussions-and-proposals 仓库中的 RFC #1030，当前状态为 Open。
- 👤 **发起人**：kraenhansen，计划将 4 个提交合并到 `main` 分支。
- 🧩 **核心目标**：允许 React Native 应用加载 Node-API addons，并复用 Hermes 自身的 Node-API 实现。
- 🏗️ **实现方式**：React Native 充当 Hermes 的 Node-API host，并在 `react-native/node-api` 中加入 `dlopen`。
- 📦 **Hermes 侧支持**：Hermes 提供 `node-api` 库，供 Node-API 插件链接使用。
- 🔗 **相关草案**：React Native 侧实现为 react/react-native#59894；Hermes 侧涉及 meta/hermes#1074 和 meta/hermes#2307。
- ⚠️ **已知问题**：`hermes_napi_load_module` 无法像 Node 的 `process.dlopen` 那样接收调用方的 `exports` 对象。
- 🔄 **提交进展**：后续提交补充了“无 Node-API 时如何构建”“将 Node-API 设为可选启用”以及“CI 是否应测试 Node-API”等内容。
- 🧪 **当前状态**：尚无 reviewer、assignee、label 或 milestone，仍处于早期讨论与草案阶段。

---

### [你好，Graphite：WebGPU](https://wcandillon.dev/article/hello-graphite-webgpu)

**原文标题**: [Hello, Graphite: WebGPU](https://wcandillon.dev/article/hello-graphite-webgpu)

本文是 React Native Skia 3.0 发布文章的第二部分，重点介绍基于 WebGPU 和 Dawn 的统一 GPU 运行时：Skia Graphite 与 Three.js、TensorFlow.js 等共享同一 GPU 设备，实现 2D、3D、视频、摄像头、Lottie 和原生视图内容之间的高效互操作，减少纹理拷贝与 CPU 回读。

- 🚀 React Native Skia 3.0 将 Skia 作为 WebGPU 运行时之上的库之一，并与 React Native WebGPU 自动共享同一个 Dawn 实例。
- 🔗 新增 GPU 资源共享 API：可通过 `importDevice(Skia.getNativeDevice())` 获取 `GPUDevice`，并在 Skia 图像、表面与 WebGPU 纹理之间互相封装。
- 🎨 Skia 与 Three.js 可双向集成：Three.js 场景可作为 Skia 图像绘制，Skia 图像也可作为 Three.js 纹理，无需 CPU 回读。
- 🎥 视频和摄像头帧通过 `device.importExternalTexture()` 导入，支持零拷贝、YUV 和同步 fence，替代 v2 中较脆弱的 Native Buffer API。
- 🧵 React Native WebGPU 暴露共享纹理内存与 fence API，可导入 `IOSurface`、`AHardwareBuffer` 和平台 fence，用于原生缓冲区读写与同步。
- 📷 React Native Vision Camera 与 React Native Skia Video 已迁移到 WebGPU 层，摄像头帧可直接供 TensorFlow.js 等模型处理。
- ✨ Lottie 动画可与任意 Skia、WebGPU 内容合成并自定义属性，模板中的图片可直接替换为视频或实时摄像头画面。
- 📱 原生视图快照从 Skia 的 `makeImageFromView()` 移至 WebGPU 的 `queue.drawElementImageToTexture()`；iOS 和 Android 13+ 可 GPU 直接绘制，旧版 Android 回退 CPU。
- 🧩 目标是打造统一 GPU 运行时，同时通过共享纹理内存和 fence 保留对原生平台能力的控制。
- 🙌 文章致谢社区生态及 Google 对 Dawn 和 Skia 的开源维护。

---

### [2026 年 React Native 表单验证：附示例的分步教程 | Formisch](https://formisch.dev/blog/react-native-form-validation/)

**原文标题**: [React Native Form Validation in 2026: Step-by-Step Tutorial with Example | Formisch](https://formisch.dev/blog/react-native-form-validation/)

本文是一篇 React Native 表单验证教程，演示如何使用 Formisch 和 Valibot 构建包含邮箱、密码和确认密码的注册表单，并覆盖规则定义、错误展示、提交处理、服务端错误及验证时机设置。

- 📱 React Native 不提供内置表单验证，需要自行实现或借助表单库。
- 📦 教程使用 `@formisch/react-native` 1.2.0 与 `valibot` 1.5.0，仅需安装这两个包。
- 📝 用 Valibot schema 定义邮箱非空与格式、密码非空且至少 8 位、确认密码非空等规则，错误信息会直接展示给用户。
- 🔐 密码一致性通过 `v.partialCheck` 比较两个密码，并用 `v.forward` 将错误定位到确认密码输入框。
- 🧩 用 `useForm` 创建表单，将每个 `TextInput` 包在 `Field` 中，传入 `of`、`path`、`field.props` 和 `field.input` 完成绑定。
- ⚠️ 通过 `field.errors` 在对应输入框下方显示错误；默认首次提交后才显示错误，之后随输入重新校验。
- 🚀 用 `handleSubmit` 包装提交函数并绑定到按钮 `onPress`，`isSubmitting` 可用于禁用按钮、防止重复提交。
- 🌐 服务端错误（如邮箱已被占用）可在提交函数中抛出 `Error`，Formisch 会将其放入 `signUpForm.errors` 并展示。
- ⏱️ `validate` 和 `revalidate` 控制校验时机，可选 `initial`、`touch`、`input`、`change`、`blur`、`submit`；注册页推荐 `blur` + `input`，并结合 `isTouched` 或 `isSubmitted` 控制错误显示。
- 🔄 可从 Formik、React Hook Form、TanStack Form 逐步迁移；Formisch 目前仅支持 Valibot，Zod 支持计划中。
- 💻 文末提供可直接复制的单文件完整示例代码。

---

### [从 React Native 到 Swift 与 Kotlin：Gobi 为期 11 周的迁移](https://swmansion.com/blog/react-native-to-native-migration-gobi/)

**原文标题**: [React Native to Swift & Kotlin: Gobi's 11-Week Migration](https://swmansion.com/blog/react-native-to-native-migration-gobi/)

Gobi 是一款集互动地图、实时推荐、酒店预订和 AI 聊天（Ask Gobi）于一体的社交发现应用。团队最初为优化核心交互性能，最终用约 11 周将应用从 React Native 渐进迁移到 Swift 和 Kotlin，并在迁移期间持续发布新功能、保持用户体验可用。

- 📱 Gobi 将地图探索、好友推荐、住宿预订和 AI 助手整合在同一应用内。
- 🧩 迁移始于性能瓶颈：先用原生代码处理 bottom sheet 的手势与运动，并开源 React Native Bottom Sheet。
- 🗺️ 地图从 RN Mapbox 换为自研原生模块，把相机驱动的 marker 更新移到原生端，仅在数据变化时传快照，实现 120 FPS。
- 🏗️ 团队决定整体渐进迁移：先定义导航契约，确保 iOS 和 Android 对地图上下文、相机位置、marker、sheet 栈等行为保持一致。
- 📦 建立原生宿主和工程基础，接管 Xcode/Gradle、Expo 模块与生命周期，并用 Turbo/Fabric 适配器兼容旧 React Native 调用。
- 🏝️ 未迁移功能作为 React islands 运行在原生应用中，共享按需启动的 JS runtime，使功能可逐个替换且不阻塞产品迭代。
- 🤖 使用 AI coding agents 执行小任务：开发者负责架构、依赖协调、检查点与代码审查，共享文件设单一负责人以避免冲突。
- 🧪 Ask Gobi 等大功能先记录现有行为、后端数据与测试标准，再分阶段迁移；双端用相同录制事件序列验证流式回复、重连和会话恢复。
- 👁️ 借助 Argent 和 ImageMagick 做截图视觉对比与交互检查，覆盖滚动、键盘、sheet 手势和导航一致性。
- ⏱️ 从引入原生宿主到移除 React Native runtime 约 11 周；最终删除 Hermes、Metro、JS 入口和 Expo runtime 依赖，应用完全原生。
- ✅ 结论：并非所有应用都需要全量迁移；当高要求功能已依赖原生且协调成本超过共享收益时才值得，并需清晰策略与检查以避免过渡期故障。

---

### [React Native OTA 更新：2026 年完整指南](https://bitrise.io/guides/react-native-ota-updates-complete-guide?utm_campaign=cp_guide_the-complete-guide-to-react-native-ota-updates_all_2026-11-09&utm_source=This%20Week%20in%20React%20Native&utm_medium=newsletter-november-18)

**原文标题**: [React Native OTA updates: the complete guide for 2026](https://bitrise.io/guides/react-native-ota-updates-complete-guide?utm_campaign=cp_guide_the-complete-guide-to-react-native-ota-updates_all_2026-11-09&utm_source=This%20Week%20in%20React%20Native&utm_medium=newsletter-november-18)

Bitrise 发布的《React Native OTA 更新：2026 完整指南》聚焦如何在不经过应用商店的情况下更新 React Native 应用的 JavaScript，以分钟级修复和回滚应对商店审核波动，同时说明合规、工具选择和安全发布策略。

- 📱 OTA 更新可绕过应用商店，仅更新应用 JavaScript，实现分钟级修复与全员回滚。
- ⏱️ 商店审核仍不可预测：截至 10 月中旬的 12 周内，Apple 小版本更新平均审核 14 小时；每周平均处理 37.8 万次提交。
- 🚫 2025 年 Apple 拒绝近 80 万次现有应用更新，被拒后需重新排队，进一步延长等待。
- ⚠️ OTA 虽快，但粗心更新可能同时导致所有用户崩溃，因此需要安全发布与风险控制。
- 🧭 指南覆盖 OTA 定义与商店政策、团队适用性与范围、工具选择与部署时长、快速且安全发布的方法。
- 👥 由 Bitrise 的 Oliver Falvai（Staff Engineer）与 Akos Birmacher（Product Manager）撰写，基于其 OTA 服务经验。
- 📅 文章发布日期与最后更新均为 2026 年 11 月 11 日。

---

### [React Native 底部弹层 1.0.0](https://swmansion.com/changelog/react-native-bottom-sheet-1-0-0/)

**原文标题**: [React Native Bottom Sheet 1.0.0](https://swmansion.com/changelog/react-native-bottom-sheet-1-0-0/)

React Native Bottom Sheet 发布 1.0.0 重大版本，重点包括统一关闭请求、修改 `settleDuration` 单位、重命名 `nativeOverlay`，并调整默认关闭行为和迁移方式。

- 🚀 1.0.0 于 2026 年 11 月 13 日发布，属于重大版本更新。
- 🔁 `ModalBottomSheet` 的 `nativeOverlay` 重命名为 `windowOverlay`，行为保持不变。
- ⏱️ `settleDuration` 改为毫秒单位，默认值为 `450`；低于 `10` 会触发开发警告，提示可能仍使用秒值。
- 🧩 统一 `ModalBottomSheet` 关闭请求：遮罩点击、读屏关闭、Android 返回键、Android/Web 的 Escape 都会调用 `onCloseRequest`（如已提供）。
- 📱 iOS 也支持 `onCloseRequest`，包括遮罩点击、遮罩上的 Dismiss 按钮和 VoiceOver 退出手势。
- ⚙️ 默认关闭行为变更：无处理器时会吸附到关闭档位并通过 `onIndexChange` 上报；Android 返回键和 Escape 在关闭动画期间仍被消耗；Web 仅最上层模态接收 Escape。
- 📐 档位 `insets` 新增 `start` 和 `end`，遵循布局方向并覆盖对应的左/右 inset；Web 使用文档方向，同时修复 RTL 下 `surfaceStyle` 圆角。
- 🎨 `scrimColor` 扩展为任意 `ColorValue`，支持 `PlatformColor` 和 `DynamicColorIOS`。
- 🛠️ 更新 `wrapNativeView` 类型以隐藏内部原生属性；`Animated.createAnimatedComponent` 仍可使用，并新增 `BottomSheetProviderProps` 类型导出。
- 📦 将 `react-dom` 和 `react-native-web` 声明为可选 peer dependencies。
- 🔄 迁移要点：重命名 `nativeOverlay`；将显式 `settleDuration` 值乘以 1000；在 `onCloseRequest` 中设置 `index` 到关闭档位以关闭；若需 Android 返回键或 Escape 不关闭，添加空处理器或将关闭档位标记为 `programmatic`；必要时将 `wrapNativeView` 参数类型改为 `ComponentType<any>`。

---

### [Release @react-navigation/core@7.25.0 · react-navigation/react-navigation · GitHub](https://github.com/react-navigation/react-navigation/releases/tag/%40react-navigation%2Fcore%407.25.0)

**原文标题**: [Release @react-navigation/core@7.25.0 · react-navigation/react-navigation · GitHub](https://github.com/react-navigation/react-navigation/releases/tag/%40react-navigation%2Fcore%407.25.0)

本次内容为 react-navigation 仓库中 `@react-navigation/core@7.25.0` 的版本发布说明，涵盖版本发布时间、问题修复、功能更新及贡献者信息。

- 📦 最新版本为 `@react-navigation/core@7.25.0`
- 🗓️ 该版本于 2026-11-15 发布，由 `satya164` 发布，自该版本以来主分支已有 923 次提交
- 🐛 修复了链接配置中嵌套路由类型未保留的问题，关闭 #12736、#12385、#10876
- ✨ 新增导出 `GenericNavigation` 类型，供 `useNavigation` 使用，关闭 #11893
- 👤 贡献者为 `satya164`
- 🔒 该发布为 Immutable，仅发布标题和说明可修改

---

### [发布 @react-navigation/bottom-tabs@7.22.0 · react-navigation/react-navigation · GitHub](https://github.com/react-navigation/react-navigation/releases/tag/%40react-navigation%2Fbottom-tabs%407.22.0)

**原文标题**: [Release @react-navigation/bottom-tabs@7.22.0 · react-navigation/react-navigation · GitHub](https://github.com/react-navigation/react-navigation/releases/tag/%40react-navigation%2Fbottom-tabs%407.22.0)

`@react-navigation/bottom-tabs` 发布 7.22.0 版本，由 satya164 于 2026-11-15 发布，包含两项 Bug 修复和一项新功能。  
- 🚀 新版本号为 `@react-navigation/bottom-tabs@7.22.0`，发布提交为 `77fad70`。  
- 🐛 修复 Web 端 Material Tab 项焦点环被裁剪的问题，关闭 #12594。  
- 🧩 修复 Tabs 中导航辅助函数类型不正确的问题，关闭 #10979。  
- ✨ 新增底部标签页的 `tabBarTransparent` 选项。  
- 👤 本次发布贡献者为 satya164，并附有 3 个资源文件。

---

### [Release 0.9.0 · DorianMazur/react-native-screen-choreography · GitHub](https://github.com/DorianMazur/react-native-screen-choreography/releases/tag/v0.9.0)

**原文标题**: [Release 0.9.0 · DorianMazur/react-native-screen-choreography · GitHub](https://github.com/DorianMazur/react-native-screen-choreography/releases/tag/v0.9.0)

v0.9.0 是 react-native-screen-choreography 的最新版本，于 11 月 16 日发布，包含 5 个提交，主要优化共享转场配置、Reduce Motion 兼容、导航组件重渲染以及跨页面共享元素匹配。

- 🚀 版本发布：DorianMazur/react-native-screen-choreography 发布 v0.9.0，为最新版本，16 日 09:26 发布，含 5 个提交合并至 main。
- 🧩 简化共享转场：通过 stack layout helpers、可按压共享元素及继承源 group 的 targets 简化设置。
- ♿ 支持 Reduce Motion：当减少动态效果跳过打开动画时，仍允许 tray pushes。
- ⚡ 减少重渲染：过渡会话更新时，避免调用导航钩子的组件重新渲染。
- 🔗 跨页面配对：将 tab 屏幕上的共享元素与根 stack 详情屏幕上的目标元素配对。
- ⏱️ 性能优化：跳过空闲共享元素的 presentation clock 更新。
- 📦 变更记录：提供 v0.8.6...v0.9.0 完整变更日志及 2 个 assets。

---

### [发布 v1.2.0 · software-mansion/enriched-markdown · GitHub](https://github.com/software-mansion/enriched-markdown/releases/tag/v1.2.0)

**原文标题**: [Release v1.2.0 · software-mansion/enriched-markdown · GitHub](https://github.com/software-mansion/enriched-markdown/releases/tag/v1.2.0)

enriched-markdown v1.2.0 已发布，这是 software-mansion 仓库的最新版本，围绕 Android、iOS、Web 的 Markdown 渲染与编辑能力带来大量新功能、修复、重构、测试和文档更新，重点覆盖代码块、链接、LaTeX、流式渲染、输入与无障碍体验。

- 🚀 发布信息：v1.2.0 于 11 月 12 日由 maksg 发布，页面显示 15 个提交，完整变更对比为 v1.1.1...v1.2.0。
- 🤖 Android 功能：支持自定义剧透遮罩、LaTeX 数学渲染插件、Material 3 Markdown 样式、代码块可选语法高亮/横向滚动/语言标题与复制按钮、最后块边距，以及通过 composable scope 提供插件。
- 🍎 iOS 功能：新增 tree-sitter 围栏代码块高亮、带标题和复制按钮的可滚动代码块面板、链接长按菜单、按 URL 模式设置链接样式、markdownBottomMarginEnabled，并让文本在内容处结束。
- 🔗 链接与交互：新增原生链接药丸及可选图标着色，输入 StyleState 暴露链接目标，支持 onTextPress、onLinksChange、onSelectionCopy 等回调，并可在文档中报告链接。
- 🌊 流式渲染：引入可替换块与代码块块槽、共享流式过滤器、iOS/Android 宿主块槽放置、流式块槽渐入、C++ Markdown 修复模块，并隐藏流式前缀末尾的半写语法。
- 🧩 渲染扩展：EnrichedMarkdownText 支持 renderers、resolveImageSource、代码块渲染器，并可在分段 Markdown 视图中托管 React 块渲染器。
- ♿ 数学与无障碍：通过共享 C++ 引擎用英文朗读 LaTeX 公式；Web 端新增 EnrichedMarkdownTextInput，并支持逐段 RTL 与双向文本方向。
- 🛠️ 修复与性能：大量修复 iOS/Android/Web 的列表、表格、图片、输入、剪贴板、代码块布局、RTL、测量缓存、首帧渲染等问题，并进行性能优化。
- ⚠️ 破坏性变更：Android 端 LaTeX 数学仅通过 LatexMathPlugin 启用，Span 注册改为 TextViewAwareSpan 并根据布局定位高亮。
- 🧪 工程与社区：新增 iOS XCTest、内存基准、Android 插件测试，上线 Docusaurus 文档站，并迎来 13 位新贡献者。

---

### [发布 v0.33.0 · software-mansion/argent · GitHub](https://github.com/software-mansion/argent/releases/tag/v0.33.0)

**原文标题**: [Release v0.33.0 · software-mansion/argent · GitHub](https://github.com/software-mansion/argent/releases/tag/v0.33.0)

该版本为 Argent v0.33.0，于 11 月 12 日发布，包含自上一版本以来的 30 次提交。更新重点集中在 React Profiler 修复、E2E 测试增强、设备工具与调试器改进、macOS 原生应用支持，以及 MCP 和工具服务优化。

- 🚀 发布 v0.33.0：包含 30 次提交，并新增两位贡献者。
- 🧪 React Profiler 修复：按 logicalDeviceId 查找会话，修正 Strict Mode 渲染计数，统计所有提交中的渲染次数，并支持从 Xcode 27 的 tagged-backtrace 读取 CPU 栈。
- 🧰 MCP 与工具服务优化：精简 Argent 规则、技能和工具描述；向代理隐藏五个工具；将 list-devices 渲染为简短文本；在 iOS 模拟器 describe 中显示禁用、选中和 VoiceOver 提示。
- ✅ E2E 测试增强：通过 requires 块控制 E2E 测试，并在测试文件头写入格式版本。
- 🛠️ 设备与调试修复：合并 10 项设备工具修复；为 Apple TV 提供可用的等待原语；旧版调试器连接到应用运行时而非 Reanimated；CLI 在工具报告失败时以 1 退出。
- 📦 初始化修复：当固定源无法访问时，安装已随附的技能。
- 🍎 macOS 支持：macOS 原生应用功能默认开启；在非 macOS 环境拒绝读取 Mac 应用；解释 SwiftUI 控件搜索未命中的原因。
- 🤖 Android DevTools：辅助工具升级至 0.4.0，停止抑制无障碍服务。
- 🐛 其他修复：Chromium 表单提交发送 Enter 文本；Flow 拒绝非数字 snapshot maxMismatch；describe 输出树帧时去除空格；推进 argent-private 子模块。

---

### [发布 Release 2.1.0 · kuatsu/react-native-boost · GitHub](https://github.com/kuatsu/react-native-boost/releases/tag/v2.1.0)

**原文标题**: [Release Release 2.1.0 · kuatsu/react-native-boost · GitHub](https://github.com/kuatsu/react-native-boost/releases/tag/v2.1.0)

该页面为 kuatsu/react-native-boost 的 v2.1.0 发布说明，主要内容是新增对 React Native 0.89 的支持，以及修复 Metro 兼容性问题。

- 📦 发布版本：v2.1.0，属于 Latest 最新版本，对应的提交为 cb84c23。
- 📅 发布时间：11 月 13 日 14:20，由 github-actions 发布。
- ✨ 新功能：新增对 React Native 0.89 的支持。
- 🐛 Bug 修复：Metro 现在支持 0.83 及更高版本。
- 📎 发布附件：共包含 2 个 Assets。
- 👍 用户反馈：获得 1 个点赞反应。

---

### [Release Release 0.10.0 · appandflow/react-native-ease · GitHub](https://github.com/appandflow/react-native-ease/releases/tag/v0.10.0)

**原文标题**: [Release Release 0.10.0 · appandflow/react-native-ease · GitHub](https://github.com/appandflow/react-native-ease/releases/tag/v0.10.0)

该页面是 appandflow/react-native-ease 仓库的 v0.10.0 发布说明，属于最新版本；本次更新主要新增 iOS 的 Swift Package Manager 支持，并修复了落地页按钮尺寸与左对齐布局问题。

- 📦 最新版本为 v0.10.0，由 floco-af 于 11 月 13 日发布，提交为 edbbccd。
- 🍎 新增 iOS 对 Swift Package Manager 的支持（#74）。
- 🐛 修复落地页按钮过大的问题，并恢复左对齐布局（#71）。
- 📊 仓库导航显示当前有 3 个 Issue 和 2 个 Pull Request。
- 👍 该发布获得 3 个点赞反应。
- 📁 发布页面包含 2 个资源文件。

---

### [React Native 交易图表](https://kirill3333.github.io/react-native-trading-charts/)

**原文标题**: [React Native Trading Charts](https://kirill3333.github.io/react-native-trading-charts/)

采用原生 GPU 渲染方案，通过共享 C++ 引擎统一处理图表数据与几何信息；当图表发生变化时，iOS 端使用 Metal、Android 端使用 OpenGL ES 3 绘制帧。

- 🧩 共享 C++ 引擎负责图表数据与几何处理
- 🍎 iOS 使用 Metal 进行原生 GPU 渲染
- 🤖 Android 使用 OpenGL ES 3 进行原生 GPU 渲染
- 🔄 图表变化时触发帧绘制

---

### [GitHub - backtickjs/backtick：用于完全由服务器驱动的 React Native 应用的工具链。 · GitHub](https://github.com/backtickjs/backtick)

**原文标题**: [GitHub - backtickjs/backtick: A toolchain for fully server-driven React Native apps. · GitHub](https://github.com/backtickjs/backtick)

Backtick 是一个面向 React Native 的全服务端驱动工具链：在服务器端用 React 编写每个屏幕的布局、数据与行为，更新随服务器部署生效，无需等待应用商店发版。

- 🚀 快速开始：运行 `npx create-backtick-app@latest` 创建 Expo 应用和 Backtick 服务器；`npm start` 后扫码预览，编辑 `server/Home.tsx` 即可修改屏幕；支持 React、Solid 模板和 Bun 运行时。
- 🧩 屏幕可由服务端组件、客户端组件或二者混合构成；客户端脚本用 `cs`…`` 内联编写，`$name` 拼接值在服务端与客户端之间传递，并进行双向类型检查。
- ⚙️ 工作方式：客户端脚本在构建时编译；每次请求运行服务端组件，并将所需脚本与数据打包成一个 JavaScript 文件；数据以数据形式写入，不作为代码执行。
- 📱 客户端执行：Web 通过 `script` 标签和 import map 加载；React Native 应用拉取 bundle 并用已有 RN 运行，因此服务器部署即发布。
- 📦 核心包：`create-backtick-app`、`@backtickjs/core`（`cs` 标签与跨端类型）、`@backtickjs/bundler`（按请求运行与打包）、`@backtickjs/hono`、`@backtickjs/expo`，以及 React/Solid JSX、Node/Bun/tsc 插件等。
- 🛠️ 编辑器支持：VS Code 扩展可将脚本高亮为 TSX、着色拼接并类型检查；`backtick-tsc` 支持命令行与 CI；Prettier 插件可在保存时格式化脚本。
- 👤 作者：Jean-François Bisson，曾在 Meta 构建移动基础设施，现全职开发 Backtick；可通过 `jf@backtickjs.com` 或 LinkedIn 联系。
- 📄 项目采用 MIT 许可证；仓库约 32 stars、2 forks、2 watching，提交历史约 1,965 commits。

---

### [GitHub - magrinj/expo-screen-time: The Screen Time API for React Native and Expo: block apps, run schedules, draw custom shields and render usage reports on iOS and Android, from one TypeScript API. · GitHub](https://github.com/magrinj/expo-screen-time)

**原文标题**: [GitHub - magrinj/expo-screen-time: The Screen Time API for React Native and Expo: block apps, run schedules, draw custom shields and render usage reports on iOS and Android, from one TypeScript API. · GitHub](https://github.com/magrinj/expo-screen-time)

expo-screen-time 是面向 React Native 与 Expo 的屏幕使用时间 API，用一套 TypeScript 接口在 iOS 和 Android 上实现应用拦截、时间表、自定义屏蔽页和使用报告，适合专注、数字健康及家长控制类应用。

- 📱 **统一 API**：覆盖 iOS 与 Android，提供应用拦截、日程、屏蔽页、使用报告等能力。
- 🍎 **iOS 原生封装**：基于 Apple Screen Time API（FamilyControls、ManagedSettings、DeviceActivity），配置插件自动生成所需扩展，无需手动改 Xcode。
- 🤖 **Android 自带引擎**：Android 没有系统级 Screen Time API，模块通过前台服务实现自己的执行引擎。
- 🔐 **一站式权限**：一次调用返回用户需完成的授权步骤，包括 iOS Family Controls 提示和 Android 设置开关。
- 🚫 **应用拦截**：支持用户通过原生选择器选择应用，并按黑名单或白名单模式拦截。
- ⏰ **时间表与阈值**：支持时间窗口和用量阈值，应用关闭后仍持续执行，并向 JS 回传事件。
- 🛡️ **自定义屏蔽页**：可定制屏蔽界面及关闭、延后、解锁、打开应用等按钮。
- ⏳ **临时解锁**：支持“赚取时间”式临时解锁，到期后自动重新锁定。
- 📊 **使用报告**：用 JSX 编写报告模板并原生渲染，使用数据不会进入 JavaScript。
- 🏷️ **Token 标签**：通过不透明句柄展示应用名称和图标，JS 无需获知用户具体选择。
- 🌐 **域名与商店限制**：iOS 支持屏蔽网页域名，并可限制安装或删除应用；Android 暂未支持类别和网页域名。
- ⚠️ **平台差异**：iOS 由系统强制执行，Android 用户可从设置关闭，模块提供 `getEnforcementGaps()` 报告执行缺口。
- ⚙️ **环境要求**：Expo SDK 54+、iOS 16+、Android 7+，必须使用开发构建，不能运行在 Expo Go；iOS 需 Family Controls 能力。
- 📦 **安装配置**：使用 `npx expo install expo-screen-time`，在 `app.json` 添加插件，再执行 `npx expo prebuild --clean` 和平台运行命令。
- 📚 **文档与示例**：提供完整文档、配置说明、API 参考、故障排查及覆盖全部功能的示例应用。
- 👥 **作者与许可**：由 Jérémy Magrin 和 Armand Petit 开发，二人属于 useffect.sh；项目采用 MIT 许可证。

---

### [发布 v2.6.0 · callstackincubator/rozenite · GitHub](https://github.com/callstackincubator/rozenite/releases/tag/v2.6.0)

**原文标题**: [Release v2.6.0 · callstackincubator/rozenite · GitHub](https://github.com/callstackincubator/rozenite/releases/tag/v2.6.0)

概述总结
- 🚀 Rozenite 发布 v2.6.0，为最新版本，发布于 11 月 11 日 23:05；自该版本发布以来，main 分支有 4 次提交。
- 🛠️ 修复 network-activity-plugin：将 Nitro 时间戳与系统实际时间对齐（#561）。
- 🔐 新增 storage-plugin：加入 react-native-keychain 适配器（#563）。
- 📚 更新文档：在插件目录中加入 rozenite-timeline-plugin（#569）。
- ⬆️ 将 playground 升级至 Expo SDK 58（#570）。
- 🧩 修复 CLI：基于当前 Rozenite 2.x 包生成插件（#571）。
- 📐 修复 UI：可调整大小的数据表格可填满容器（#567）。
- 🧭 修复 react-navigation-plugin：支持 Expo Router 58（#578）。
- 👋 新增贡献者：@lorenc-tomasz、@alexprigi、@R0ixy、@lukewalczak。
- 🔗 完整变更日志为 v2.5.0...v2.6.0；贡献者包括 lorenc-tomasz、V3RON 等 5 人，发布附有 3 个资源。

---

### [发布 v0.22.0 · wcandillon/react-native-webgpu · GitHub](https://github.com/wcandillon/react-native-webgpu/releases/tag/v0.22.0)

**原文标题**: [Release v0.22.0 · wcandillon/react-native-webgpu · GitHub](https://github.com/wcandillon/react-native-webgpu/releases/tag/v0.22.0)

v0.22.0 是 react-native-webgpu 的最新版本，由 github-actions 于 2026-11-17 发布，包含 3 次提交；本次更新主要修复 macOS 上的 WebGPU 问题，并改进 Android 上的 Dawn 下载方式。

- 🚀 发布版本：v0.22.0，标记为 Latest，发布于 17 Nov 10:39
- 📦 提交信息：自该版本发布以来，main 分支共有 3 次提交
- 🍏 修复 macOS：在 macOS 上编译并关闭 WebGPU（#629）
- 🎨 修复渲染：主线程为 CAMetalLayer 标记色彩空间，并处理仅挂载时生效的 Canvas 属性（#626），关闭 #4474
- 🤖 Android 功能：从 binaries release 下载 Dawn（#628）

---

### [发布 8.36.0 · getsentry/sentry-react-native · GitHub](https://github.com/getsentry/sentry-react-native/releases/tag/8.36.0)

**原文标题**: [Release 8.36.0 · getsentry/sentry-react-native · GitHub](https://github.com/getsentry/sentry-react-native/releases/tag/8.36.0)

sentry-react-native 8.36.0 是最新发布版本，由 sentry-release-bot 于 11 月 17 日 09:26 发布，提交为 ad67db4，主要包含 Android 回放修复、调试符号化回退处理以及 Cocoa SDK 依赖升级。

- 🛠️ 修复：当排除 `sentry-android-replay` 且设置了回放采样率时，仍会启动原生 Android SDK（#7035）。
- 🔁 内部调整：当 React Native 内置的 `symbolicateStackTrace` 不可用时，回退到 Sentry Metro 中间件 `/__sentry/symbolicate` 进行本地调试符号化（#7031）。
- 📦 依赖更新：Cocoa SDK 从 v9.34.0 升级到 v9.35.0（#7045）。
- 🏷️ 发布信息：8.36.0 标记为 Latest，页面包含 changelog、diff 和 4 个资源。

---

### [发布 v0.8.0 · callstackincubator/simlock · GitHub](https://github.com/callstackincubator/simlock/releases/tag/v0.8.0)

**原文标题**: [Release v0.8.0 · callstackincubator/simlock · GitHub](https://github.com/callstackincubator/simlock/releases/tag/v0.8.0)

callstackincubator/simlock 发布 v0.8.0（最新版，11 月 17 日发布），自 v0.7.0 以来包含 40 个提交，主要贡献者为 V3RON 和 dependabot。本次更新主要集中在设备注册与租赁、网关准入控制、可折叠模拟器支持、iOS/Android 设备与镜像处理、屏幕流共享与关键帧、E2E 测试发布，以及依赖升级和文档/ADR 提案。

- 🚀 **版本信息**：v0.8.0 为最新版本，17 Nov 09:13 发布，自 v0.7.0 起有 40 个提交，贡献者包括 V3RON 与 dependabot。
- 🛠️ **核心与守护进程修复**：测试调度器按生产方式存储失败；`nuke --delete-devices` 可销毁未认领的 provisioning 设备并删除隔离虚拟设备；relay 在响应后释放目标 Request。
- 🔐 **网关与租赁**：新增 admission command 对新请求进行排序或拒绝，租赁请求元数据可传入 admission command；已结束的 lease id 会返回 `LEASE_ENDED`，生成的 lease id 在 worker 重启上报前返回 `WORKER_UNREACHABLE`。
- 📱 **设备注册与发现**：drivers 可列出 USB 上的手机（无论是否注册）；worker 可在 `devices.autoEnroll` 下自动注册插入的手机；手机硬件序列号保存在记录中且一机一记录；Android 支持 `android.networkDevices` 网络手机。
- 🪟 **可折叠模拟器**：可折叠模拟器的流会显示当前使用面板并在折叠时切换；iOS 点击会落到正在使用的面板上。
- 🍎 **iOS 改进**：模拟器克隆/创建等待 `ios.simulator.createTimeoutMs`，延迟副本会被删除；`ios.*.bootTimeoutMs` 为 `simctl boot` 前统一截止时间；seed 从未启动的临时模拟器复制后删除；租赁模拟器首次启动前替换 lineage UDID。
- 🤖 **Android 改进**：worker 优先尝试默认镜像标签，失败则回退；doctor 在没有已安装镜像匹配默认标签时告警；catalog 会命名默认镜像标签并由网关排序。
- 🎥 **屏幕采集与流媒体**：同一设备在 worker 上的多个观看者共享一次采集，经网关的观看者共享一个 relay；iOS 与 Android 流至少每 5 秒发送一个关键帧（Android 通过 scrcpy reset video）。
- 🧪 **E2E 与工程化**：仓库构建、检查和发布 `@simlock/e2e`，支持选项检查；设备提供方支持租赁、安装、续租和释放，并新增 CI 运行测试页面；拆分所有超过 1,000 行的文件为主题文件。
- 📦 **依赖升级**：升级 npm minor/patch 依赖组，`pixelmatch` 从 7.1.0 升至 8.0.0。
- 📚 **文档与 ADR**：新增/提出多项 ADR，包括 worker 注册插入手机、可折叠模拟器流、仓库 workspace 统一发布、Android 默认镜像标签回退、每设备共享采集与 5 秒关键帧、iOS 克隆命名与网络手机等。

---

### [Release Release v1.14.0 · uni-stack/uniwind · GitHub](https://github.com/uni-stack/uniwind/releases/tag/v1.14.0)

**原文标题**: [Release Release v1.14.0 · uni-stack/uniwind · GitHub](https://github.com/uni-stack/uniwind/releases/tag/v1.14.0)

uniwind 发布 v1.14.0，重点新增系统颜色回退与原生文本换行能力，同时修复半径别名、主题色解析等问题，并包含多项原生端性能优化与测试补充。

- 🚀 新增 `platform-color()`，支持系统颜色并提供回退方案
- 📱 原生端支持将 `line-break` 和 `word-break` 类传递给 `Text` 属性
- 🐛 修复 bundler 中 start-end/end-start 圆角别名的 top/bottom 输出问题
- 🎨 修复原生端作用域主题下 `light-dark` 的解析问题
- 🧩 修复原生颜色函数中变量通道的解析问题
- ⚡ 优化 CSS 变量值归一化的记忆化处理
- 🧹 移除原生样式记录中未使用的 `index` 和 `className`
- 🗃️ 缓存使用 `data-[…]` 变体的原生样式
- 🧪 增加原生端文本装饰样式、颜色及 `mix-blend-mode` 测试
- 👏 新增贡献者 `@JaydeepAgravat` 和 `@Wadiou`
- 🔗 完整变更对比：`v1.13.2...v1.14.0`

---

### [v10.4.0 版本发布 · margelo/react-native-nitro-sqlite · GitHub](https://github.com/margelo/react-native-nitro-sqlite/releases/tag/v10.4.0)

**原文标题**: [Release v10.4.0 · margelo/react-native-nitro-sqlite · GitHub](https://github.com/margelo/react-native-nitro-sqlite/releases/tag/v10.4.0)

NitroSQLite 10.4.0 已发布，整理了自 v10.3.1 以来的依赖升级、新功能、问题修复和构建流程改进。

- 🚀 发布 v10.4.0 最新版本，发布日期为 2026-11-17。
- 📦 依赖升级：Chai 6.3.0、React Native 0.88.1、TypeORM 1.1.2。
- ✨ 新增已提交行变更的变更监听器。
- 🧩 新增 Expo 配置插件，并添加使用该插件的 Expo 示例。
- 🍎 iOS 支持从 Podfile.properties.json 读取 SQLite 设置。
- 🐛 Android 修复未应用所有 nitroSqliteFlags 定义的问题。
- 🖥️ macOS 声明最低部署目标为 10.15。
- ⏳ 修复异步结果后到达的行批次等待逻辑。
- 🏗️ 开发依赖升级：@react-native-harness CLI 和 Android 平台至 1.7.0，支持 better-sqlite3 13。
- 📱 示例项目改进：在无 watchman 的 Metro 构建中保留 Drizzle fixtures。

---

### [GitHub - expo/explore：用于跨平台、设备和状态捕获并探索应用屏幕的实验性工具 · GitHub](https://github.com/expo/explore)

**原文标题**: [GitHub - expo/explore: Experimental tool for capturing and exploring the screens of your app across platforms, devices, and states · GitHub](https://github.com/expo/explore)

Expo Explore 是一个实验性 MIT 工具，可自动截图并探索应用在不同平台、设备和状态下的屏幕，将屏幕与点击跳转关系连接成地图；它能在 PR 中生成前后视觉对比审查，也支持在本地模拟器或 Expo Simulators 上探索任意 iOS/Android 构建。

- 🗺️ 核心能力：为应用每个屏幕截图，并用点击路径连接成可视化地图，支持查看新增、删除、修改的屏幕。
- 🔍 PR 审查：在 PR 中捕获变更屏幕的修改前/后截图，标出变化区域，并自动评论报告链接。
- ⚙️ 使用要求：审查变更需 Expo SDK 57+、Expo Router 57+ 或 React Navigation 6+、Expo 账号及对应构建配置；探索构建需模拟器构建和 Claude Code/Codex 登录。
- 🚀 快速开始：可用 `npx @expo/explore capture` 审查本机变更，或 `npx @expo/explore explore:binary ./app.apk` 探索已有构建。
- 🧭 两种路径：审查变更依赖 Expo Services 构建并在 Expo Simulators/本地模拟器捕获；探索构建无需源码和配置，逐屏点击生成报告。
- 🤖 导航方式：支持模型代理自动导航，也可用 `--replay steps.json` 按固定步骤重放，保证不同运行/设备到达相同屏幕。
- 🎛️ 设备控制：默认使用 agent-device，也可配置 Argent；支持 iOS、Android、多设备 targets、折叠屏姿态等。
- 🔐 登录与状态：支持 `{{secret:NAME}}` 注入测试密码并自动脱敏；不点击删除、支付、退出、发送或离开应用的按钮。
- 🧪 CI 集成：通过 GitHub Actions 在 PR 上自动审查，也可比较任意两个 commit/tag；可选 EAS Hosting 托管预览报告。
- 🎯 配置能力：可设置 `platforms` 或 `targets`，为不同平台/设备指定 bundleId、easProfile、device、pose 等。
- 📊 报告与 API：报告有 Viewer 界面，也提供 Markdown 索引、`/llms.txt` 和 `/api/v1` JSON API，便于浏览器、脚本和 AI 代理读取。
- ⚠️ 安全与限制：审查会在本机运行两个 commit 的代码；fork PR 不审查；报告/基线保留 30 天；Android 捕获使用少于 iOS。
- 📦 维护与许可：用 `npx @expo/explore@latest setup --workflows` 更新工作流，项目采用 MIT 许可证。

---

### [GitHub - ccheever/llp：链接式文学编程 · GitHub](https://github.com/ccheever/llp)

**原文标题**: [GitHub - ccheever/llp: Linked Literate Programming · GitHub](https://github.com/ccheever/llp)

overview summary
LLP（Linked Literate Programming）是一个面向 AI 时代代码库的基础设施：人类用 Markdown 记录设计决策、原则与权衡，AI 负责编写代码和大部分审查工作。它通过代码中的 `@ref` 指针连接版本化的 LLP 文档，让 AI 能理解“为什么这样设计”，并用 `ref-check` 与一组技能维持代码和文档同步演进。

- 🧠 **核心理念**：人类留在 Markdown 中做决策，AI 处理代码与多数审查，避免 AI 因缺失背景而“简化”掉关键设计意图。
- 🔗 **引用机制**：代码通过 `@ref LLP NNNN#anchor` 指向具体文档章节，也支持关系标注、路径引用和 URL 引用。
- 📚 **解决隐式知识**：把决策、原则和约束写入仓库内、像代码一样版本化的 Markdown 文档，减少 Slack、Docs 和资深工程师脑中的隐性知识流失。
- ✅ **校验与维护**：`ref-check` 是无依赖单文件检查器，适合 CI；`llp-maintain` 用于处理代码漂移、引用修复、文档过时等需要判断的问题。
- 🛠️ **七个技能**：覆盖 `llp-orient`、`llp-create`、`llp-review`、`llp-adopt`、`llp-maintain`、`llp-super-refine`、`llp-ship`，每个技能以 `SKILL.md` 定义契约。
- 🚀 **快速开始**：创建 `llp/` 目录及根文档，在代码中添加 `@ref` 注释，再运行 `./ref-check` 验证引用与元数据。
- 📦 **安装与更新**：推荐通过 `/llp-adopt` 管理技能安装，从 tagged release 复制并写入 receipt，便于后续更新且不覆盖本地修改；也支持手动克隆复制。
- 📖 **核心文档**：`LLP 0000` 是根规范，`LLP 0001` 是采用指南，`LLP 0005` 讲审查流程，`LLP 0008` 讲技能设计，`LLP 0011` 讲 v2 的 `current/` 与 `foundation/` 结构。
- ⚖️ **许可**：项目采用 MIT License。

---

### [发布 0.13.0 版本 · callstackincubator/ai · GitHub](https://github.com/callstackincubator/ai/releases/tag/v0.13.0)

**原文标题**: [Release Release 0.13.0 · callstackincubator/ai · GitHub](https://github.com/callstackincubator/ai/releases/tag/v0.13.0)

本次 v0.13.0 发布将所有 provider 升级至 AI SDK 7，新增 iOS 27 Apple Intelligence API，并推出三个新包；同时包含功能增强、破坏性变更以及包替换与弃用说明。

- 🚀 由 grabbou 于 11 月 11 日发布 v0.13.0，标注为最新版本，版本日期为 2026-11-11。
- 📦 新增 `@react-native-ai/core-ai`，可在 iOS 27 上运行 Apple Core AI 模型包，支持语言、视觉、图像/视频生成、转录、嵌入、分割和原始模型调用。
- 🤖 新增 `@react-native-ai/android`，通过 ML Kit GenAI 运行 Gemini Nano，支持生成、流式输出、图像、工具调用、转录和嵌入。
- 🧰 新增 `@react-native-ai/utils`，提供 `wrapLanguageModelWithHistory`，帮助长对话保持在模型上下文范围内。
- 🍎 `@react-native-ai/apple` 新增 Private Cloud Compute、图像提示、Image Playground、Vision 工具、推理级别、token 用量、必选工具调用、实时转录和 Expo 配置插件等。
- 🦙 `@react-native-ai/llama` 新增推理、结构化输出、多模态输入和 `countTokens`，并修复真机测试中发现的崩溃问题。
- 🛠️ `@react-native-ai/dev-tools` 支持 AI SDK 7 遥测。
- ⚠️ 所有 provider 均要求 AI SDK 7（`ai@7`），仍在使用 AI SDK 6 的用户不应升级。
- 🔁 `@react-native-ai/llama` 要求 `llama.rn` 0.13.0-rc.8 或更高版本；`@react-native-ai/apple` 中 `isAvailable()` 改为 `getModelInfo()`，`AppleEmbeddings.getInfo()` 也改为 `getModelInfo()`。
- 📡 开发工具需通过 `registerTelemetry(...)` 注册一次 tracer，而不再在每次调用时传入 `experimental_telemetry: { tracer }`。
- 🗑️ `@react-native-ai/adk` 被 `@react-native-ai/android` 取代；`@react-native-ai/mlc` 不再维护，建议改用 `@react-native-ai/llama`。
- 📝 每个包都新增了 `CHANGELOG.md`，可查看完整变更列表。

---

### [获取失败](https://www.youtube.com/watch?v=fnvx2_ItPLM)

**原文标题**: [Failed to retrieve](https://www.youtube.com/watch?v=fnvx2_ItPLM)

无法总结：获取内容失败，状态码 429。

---

### [React Native Radio - RNR 377 - 无障碍与动画](https://infinite.red/react-native-radio/rnr-377)

**原文标题**: [React Native Radio - RNR 377 - A11y and Animations ](https://infinite.red/react-native-radio/rnr-377)

本期播客聚焦 React Native 动画的可访问性：在不削弱动画价值的前提下，让减少动态、屏幕阅读器、手势、轮播和 Toast 等交互更可访问；嘉宾提出“替换而非剥离”的思路和四问上线清单，并讨论 AI 的辅助作用与局限。

- 🎙️ 节目由 Mazen 和 Robin 对话 Shopify 的 Britta Evans-Fenton，主题是 React Native 动画与无障碍设计。
- 🌀 减少动态（Reduced Motion）不只服务前庭障碍用户，也能帮助孕吐、脑震荡、ADHD、癫痫等群体；必要动画如加载指示仍应保留。
- 📱 屏幕阅读器导航有技巧：双指下滑读全屏、拖动探索、利用屏幕边缘和底部标签；隐藏元素仍可能被读到。
- ⚠️ 常见问题包括突然出现/消失的按钮、仅靠红绿色传达状态、滑动删除/编辑等手势、轮播，以及自动消失的 Toast。
- ✅ 解决方案包括提供 accessibility actions、使用语义图标、用可关闭的 banner 替代 Toast，并确保状态变化能被屏幕阅读器感知。
- 🔁 Britta 提倡“Swap, don’t strip”：用交叉淡入等更温和动画替换缩放/3D 动画，而不是简单全部移除。
- 📋 四问清单：会动吗→处理减少动态；出现/消失/状态变化吗→让屏幕阅读器感知；需要手势吗→提供无障碍操作；会自动消失吗→重新考虑设计。
- 🤖 AI 可辅助审计和修复无障碍问题，但常把可访问性当“可选”，还容易过度添加 accessibilityLabel，导致与可见文本脱节；人工测试仍关键。
- 🧭 生态建议：在教程、文档和工作坊中更多纳入可访问性，让开发者和 AI 都更常看到并默认考虑它。

---

### [Node.js 的绿色线程 | James M Snell](https://www.jasnell.me/posts/green-threads-in-node)

**原文标题**: [Green threads for Node.js | James M Snell](https://www.jasnell.me/posts/green-threads-in-node)

Node.js PR #67288 于 2026 年 11 月 16 日引入实验性 `node:green_threads` 模块，让绿色线程由运行时调度，并在共享 OS 线程池上运行独立 V8 isolate；其定位介于 `worker_threads` 与 `vm` context 之间。该模块目前是 Stability 1.0（早期开发）原型，已获落地批准，但能否保留取决于实际价值。它适合大量小型、隔离、多租户或插件型代码，但不提供 Node.js API，并存在调度、调试和隔离边界等限制。

- 🧵 **模块状态**：`node:green_threads` 是实验性原型，属于 Stability 1.0 早期开发阶段；每个绿色线程拥有独立 V8 isolate、堆和垃圾回收器，但不占用独立 OS 线程、事件循环或 Node.js 环境。
- ⚙️ **运行机制**：消息、定时器回调和求值都作为任务运行；同一绿色线程的任务按顺序执行，但可被调度到不同池线程。进程共享一个 OS 线程池，默认最多 8 个线程，可通过 `NODE_GREEN_THREADS_POOL_SIZE` 调整，支持同时存在数千个绿色线程。
- 🧩 **能力边界**：绿色线程只有 ECMAScript 内建对象和少量全局能力，如 `postMessage()`、`onmessage`、定时器、`queueMicrotask()`、`console`、`EventTarget`、`AbortController`、`MessageChannel` 和受限 `BroadcastChannel`；没有 `require()`、`process`、文件系统或网络。
- 🔄 **与宿主通信**：支持结构化克隆和可转移 `ArrayBuffer`；`MessagePort` 与 `node:worker_threads` 兼容；宿主可传入 `env` 对象，其函数在绿色线程中表现为返回 Promise 的存根；模块源码可由宿主以 bundle 或 `resolve()`/`load()` 钩子提供。
- 🧮 **资源限制与预热**：支持 `maxTaskCpuTimeMs`、`maxCpuTimeMs` 和 `maxMemoryMb`，超限会停止绿色线程并触发 `error` 事件，不影响进程其他部分；`setWarmPoolSize()` 可预热 isolate，显著加快启动。
- 🆚 **与 worker / vm 对比**：worker 是独立 OS 线程上的完整 Node.js 环境，可阻塞、可用全部 API；`vm` context 是现有 isolate 内的独立全局对象，成本低但共享堆和 GC，且不是安全机制，只能限制同步超时、不能限制内存。绿色线程位于两者之间：有独立堆和 isolate，成本低到可大量创建，但无 Node.js API，并内置 CPU/内存限制。
- 📊 **基准表现**：启动 1000 个空闲实例时，worker 约 6.2 MB/实例、约 950 个/秒；绿色线程约 1.4 MB、约 3700 个/秒；预热池约 83,000 个/秒；`vm` context 约 0.25 MB。消息速度略慢于 worker；相同并行度下 CPU 密集任务性能接近；1000 租户场景中绿色线程约 195,000 req/s 且只用 8 个 OS 线程，worker 方案约 160,000 req/s 但需 1000 个 OS 线程。
- 🛡️ **故障隔离**：绿色线程遇到死循环可在约 51 ms 后被 CPU 限制停止，其他请求最慢约 3 ms；内存超限由 `maxMemoryMb` 停止，其他租户继续服务。`vm` 池的 `timeout` 只让请求失败且租户保留状态，但同一 worker 上其他租户会等待；微任务死循环需 `microtaskMode`，堆耗尽则可能拖垮整个 worker。
- 🎯 **适用场景**：适合大量小型、多数空闲且需相互隔离的代码单元，如多租户处理器、用户自定义函数、webhook；插件/扩展系统；用户脚本、规则和转换；以及可用预热池优化启动时间的场景。需要 Node.js API、npm 包、阻塞代码或少量长生命周期实例时，worker 更合适；代码可信或可接受一个坏租户拖垮整个 worker 时，`vm` 更便宜。
- ⚠️ **主要限制**：无 Node.js API，连 `URL`、`TextEncoder`、`structuredClone()`、`fetch()` 当前也缺失；`Atomics.wait()` 会抛错，`SharedArrayBuffer` 自旋可能占满池线程；无抢占，长任务会占住池线程；无调试器/DevTools 集成；内存和创建成本高于 `vm`，消息略慢于 worker；并行计算受池大小限制；极少数 V8 循环忽略终止请求时，线程会在 1 秒后被放弃，并可能最终导致进程中止。
- 🧪 **试用方式**：代码尚未进入正式发布，需要构建 PR 分支并使用 `--experimental-green-threads` 运行；分支内文档覆盖完整 API。落地后需决定是否保留及补充哪些 API，作者呼吁有相关用例或无适用场景的开发者试用并在 PR 上反馈。

---

### [RFC: Package Variants (formerly Package Distributions) by darcyclarke · Pull Request #928 · npm/rfcs · GitHub](https://github.com/npm/rfcs/pull/928)

**原文标题**: [RFC: Package Variants (formerly Package Distributions) by darcyclarke · Pull Request #928 · npm/rfcs · GitHub](https://github.com/npm/rfcs/pull/928)

该 RFC PR #928 提议在 npm 中引入“包变体（Package Variants）”机制：同一个包可以针对不同环境提供完整替代包，并通过 `variants` 字段来选择；当前 PR 仍处于开放状态，核心争议在于是否应改用 `optionalDependencies`、依赖如何处理，以及发布原子性。

- 📦 **PR 状态**：npm/rfcs #928 由 darcyclarke 发起，计划将 8 个提交合并到 `npm:main`，目前仍为 Open，尚未合并；ruyadorno 有推送权限并协助迭代。
- 🔁 **取代旧提案**：该 PR 取代 #519；因作者已无 npm/rfcs 写权限，改从个人 fork 推送同一分支的修订稿。
- 🏷️ **更名与字段**：将“Package Distributions”更名为“Package Variants”，并引入 `variants` 字段。
- 🧩 **变体定义**：变体是针对某一环境的完整替代包，拥有普通 tarball、完整性校验及可选的 provenance；它不是 overlay、patch 或 sidecar。
- ⚙️ **安装行为**：变体单独安装，并占据父包在依赖树中的位置；客户端不安装变体自身的 `dependencies`、`optionalDependencies`、`peerDependencies`，运行时依赖需打包进 tarball。
- 🔍 **解析一致性**：`require`、`import`、类型声明及包命令均应解析到被选中的变体。
- 🚀 **动机**：esbuild、swc、biome、oxc、rolldown、bun、pnpm 等原生二进制包目前靠“每平台一个包 + optionalDependencies + 脚本/运行时 shim”分发；脚本只是发布时 `bin` 指向问题的权宜，安装器已知平台，应直接链接对应文件。
- ⚠️ **optionalDependencies 局限**：锁文件可能遗漏其他平台包并被重写；可选包可全部缺失；运行时仍需 try/catch 查找；每平台还需单独包名和发布。
- 🧵 **讨论分歧**：zkochan 质疑维护多个包、provenance 和未作用域包名成本，建议一个版本多个 tarball（需 registry 支持、原子发布），或直接用 optionalDependencies 并自动链接所选包的 bin；ljharb 强调安装脚本是 npm 最大安全攻击面，并询问变体间入口/元数据差异。
- 🧪 **审阅状态**：zkochan 请求修改，ljharb 留下评论；合并至少需 1 个批准，共有 5 位参与者。

---

### [CSS 和 HTML 已内置 | webpack](https://webpack.js.org/blog/2026-11-16-css-and-html-are-built-in/)

**原文标题**: [CSS and HTML Are Built In | webpack](https://webpack.js.org/blog/2026-11-16-css-and-html-are-built-in/)

自 webpack 5.109.0 起，CSS 与 HTML 已内置支持，无需额外插件或复杂配置；你可以直接导入样式表，或以 HTML 页面作为入口，由 webpack 处理依赖、资源与输出。现有项目仍可兼容，并提供 codemod 辅助迁移。

- 🎨 **CSS 零配置**：直接 `import "./styles.css"` 即可，webpack 自动解析 `@import` 和 `url()`，并将 `*.module.css` 作用域化为 CSS Modules。
- 📦 **按 chunk 提取 CSS**：默认会为每个 chunk 提取 `.css` 文件；生产模式下（5.110.0+）自动压缩，并结合 `browserslist` 自动添加厂商前缀。
- 📄 **HTML 作为入口**：可将 `./src/index.html` 设为入口，webpack 会打包页面引用的脚本、样式和图片，并重写 URL。
- 🔗 **生成 HTML 页面**：若项目以 JavaScript 为入口，设置 `output.html: true` 可自动生成页面并关联脚本与样式表。
- 🧹 **可移除旧插件**：`css-loader`、`style-loader`、`mini-css-extract-plugin`、`css-minimizer-webpack-plugin`、`html-loader`、`html-webpack-plugin`、`html-minimizer-webpack-plugin` 等已被内置能力替代。
- 🛠️ **预处理器继续可用**：Sass、Less、PostCSS、Tailwind 等保留对应 loader，去掉其后的 CSS loader，并设置 `type: "css/auto"` 即可接入内置 CSS 管线。
- 🔁 **兼容现有项目**：已有 `css-loader` 和 `html-loader` 配置仍可工作；webpack 会检测相关规则并默认关闭对应内置支持，便于逐步迁移。
- 🚚 **迁移工具**：CSS 可运行 `@webpack/css-plugins-to-native-css` codemod；HTML 可运行 `@webpack/html-plugins-to-native-html` codemod（5.112.0+）。
- 🆕 **新项目默认启用**：通过 `npx create-webpack-app` 创建的新项目已直接使用内置 CSS 与 HTML 支持。

---

### [修复一个 WebKit 缺陷，看看 Promise 是否由火车轨道构成](https://alistair.sh/thenables)

**原文标题**: [Fixing a WebKit bug to see if promises are made of train tracks](https://alistair.sh/thenables)

文章讲述作者修复 WebKit 中一个 Promise 相关的规范符合性 bug：在 Bun 与 Safari 中，`await` 一个被篡改 `constructor`、且 `Symbol.species` getter 抛错的 Promise 时，程序会永久挂起；根因是 JavaScriptCore 的快速路径先读取 species、后创建 resolve/reject 函数，导致抛错时无法拒绝 Promise。修复仅需调整顺序并增加少量代码。

- 🐛 Bun 1.3.14 与 Safari 26 会打印 `before` 后挂起，而 Node.js 会按规范抛错退出。
- 🔧 根因是 JavaScriptCore 对真实 Promise 的快速路径先做 `SpeciesConstructor` 查找，再创建 resolve/reject；getter 抛错时没有 reject 函数可用，异常逃逸且 Promise 永远 pending。
- ✅ 修复 WebKit/WebKit#68749 仅 +16 行：先创建 resolving functions，再调用 `then()`；若调用抛错，就用已有的 reject 拒绝 Promise。
- 📜 规范中 `resolve(value)` 会先读取 `value.then`：不是函数则 fulfil；getter 抛错则 reject；是函数则把 resolve/reject 传给 `then()`，进行 thenable 同化。
- ⚠️ “resolved” 不是 Promise 状态；Promise 可以已锁定结果但仍处于 pending，只有 fulfilled/rejected 才是 settled。
- 🔍 `Promise.prototype.then` 会读取 `this.constructor[Symbol.species]` 来创建新 Promise，因此普通属性读取中的 getter 可以抛错，规范会把该错误放到 rejected track。
- 🚂 Promise 形似成功/失败双轨的铁路，但失败轨可由引擎写入任意错误，因此 TypeScript 的 `Promise<T>` 无法标注拒绝类型 `E`。
- 📌 结论：这是一个由步骤顺序错误导致的 bug；修复后 Bun 1.4 与 Safari 27 的行为与 Node.js 一致。

---

### [你的 JS 错误在骗你](https://blog.gaborkoos.com/posts/2026-11-12-Your-JS-Error-Is-Lying-to-You/)

**原文标题**: [Your JS Error Is Lying to You](https://blog.gaborkoos.com/posts/2026-11-12-Your-JS-Error-Is-Lying-to-You/)

overview summary
- 🧩 文章指出：JavaScript 中的 `Error` 对象并不像它看起来那样可靠，日志、堆栈、序列化和跨边界传输都会丢失关键信息。
- 🚫 `JSON.stringify(err)` 常得到 `{}`，因为 `message`、`cause` 默认不可枚举；`catch` 捕获到的值也可能根本不是 `Error`。
- 🧵 堆栈不是语言规范的一部分：V8 在错误创建时记录，默认只保留 10 帧，且 `stack` 可被代码覆盖或改写。
- 🔗 包装错误时必须传入 `{ cause }`，否则原始失败会丢失；读取 `cause` 链时还要防止循环和过深遍历。
- 🌳 一个错误可能代表多个失败：`AggregateError` 保存多个 `errors`，`SuppressedError` 保存清理错误与被替换错误，整体可能是树或图而非单链。
- 🌐 不同运行时在堆栈格式、深度、额外属性、错误消息等方面不一致，不能把某个引擎的行为当作标准。
- 📦 序列化会改变证据：JSON、对象复制、`structuredClone`、`postMessage`、worker threads、IPC 都只保留部分信息，无法完整还原原错误对象。
- 🚪 跨 HTTP 边界不应暴露堆栈和内部路径；应按 RFC 9457 返回小型 problem document，把完整错误留在服务端日志中。
- 🪵 日志器可能隐藏失败：Pino 和 Winston 的结果取决于错误传入的键、位置、序列化器和配置；错误字段还可能导致敏感信息泄露。
- ✅ 实践建议：包装时始终传 `cause`，重试/恢复逻辑基于稳定的错误码，并使用受控的提取函数遍历 `cause`、`errors`、`error/suppressed`，限制深度、成员数和白名单字段。
- 🧠 最终结论：`Error`、堆栈、日志记录、序列化对象和 API 错误响应只是失败的不同表示形式，彼此不可互换，也没有一种机制能保留完整诊断状态。

---

### [Solid 2.0 - 长期持有 | Solid](https://www.solidjs.com/blog/solid-2-0-the-long-hold/)

**原文标题**: [Solid 2.0 - The Long Hold | Solid](https://www.solidjs.com/blog/solid-2-0-the-long-hold/)

Solid 2.0 在五年开发后正式稳定发布，核心围绕异步响应式图、服务端函数、面向 AI Agent 的诊断能力与更小的 API 展开，同时回顾了发布历程与生态定位。

- 🚀 **正式稳定**：Solid 2.0 在首个提交五年后、1.0 发布五年后达到稳定版，继续坚持细粒度响应式与信号（Signals）方向。
- ⚡ **异步进入响应式图**：计算可返回 Promise 或异步迭代器，下游自动理解加载与竞态状态，并自动回滚推测状态，减少手写竞态、取消与加载逻辑。
- 🖥️ **服务端函数回归核心**：支持基于 Request/Response 的高能力 RPC，也支持 Server-Sent Events 持久连接；示例中可用 `live` 服务端函数流式获取股价。
- 🤖 **为 Agent 编写而设计**：开发构建会在错误发生时报告稳定错误码、源码位置与修复建议，并提供 Agent 修复指南；还可检测瀑布流、效果循环、过宽/过窄依赖图等问题。
- 🔍 **可观测性增强**：诊断能力延伸至生产构建，整合新的开发工具、Chrome Performance Tracks 与 Sentry 插件；实验性支持 ReactiveScript 和 TSRX。
- 🧩 **一个框架服务所有场景**：核心提供 Request/Response、可观测性等原语，支持任意路由与缓存方案；退役 SolidStart 元框架，减少重复实现，并强化与 TanStack Query/Router 等生态集成。
- 🪶 **更少即更多**：移除 `createResource`、`batch`、`startTransition`、`on`、`produce`、`createComputed`、`createMutable` 等 API，降低学习与维护成本，以“构造上安全”减少边界问题。
- 🛠️ **发布历程**：2024 年末启动实际工作，2025 年 2 月公布路线图，3 月 Beta、8 月 RC；14 周内发布 23 个 RC，合并 971 个 PR、关闭 753 个 issue，以“一周无普通应用回归、无崩溃或挂起”为稳定标准。
- 🙏 **社区与生态致谢**：感谢社区测试、贡献者与 Sentry、Netlify、Google Chrome、JetBrains、Anomaly、Cursor、Code Rabbit、Anthropic、Tembo 等赞助方；可通过 `npm create solid@latest` 开始使用。
- ⏳ **“The Long Hold”含义**：它是 Solid 2.0 的诊断警告，当已显示 `isPending` 且距离上次输入已过足够时间时触发；Holds 是 2.0 异步工作的核心概念，也承认这一能力历时较久才落地。

---

### [Faster type-aware linting with tsrs | The JavaScript Oxidation Compiler](https://oxc.rs/blog/2026-11-17-faster-type-aware-linting-with-tsrs)

**原文标题**: [Faster type-aware linting with tsrs | The JavaScript Oxidation Compiler](https://oxc.rs/blog/2026-11-17-faster-type-aware-linting-with-tsrs)

Oxlint 新增 tsrs 作为 tsgolint 的替代后端，用于类型感知 lint；tsrs 是 TypeScript 的 Rust 移植版，由 Cloudflare 与 VoidZero 于 10 月发布，已在 Cloudflare、Owner.com 和 OpenAI 等团队使用。其目标是让 Oxlint 成为对开发者和 agent 都更好的 linter，通过更快的反馈和更低的内存占用，提升编辑器、CI 与 agent 工作流的效率。

- 🚀 性能提升：tsrs 相比 tsgolint v7.0.2007 最高快 5 倍、内存约降 70%；相比 typescript-eslint 最高快 98 倍、峰值内存最高降 82%。
- 🧠 一体化分析：在 Oxlint 内将类型检查与类型感知 lint 合并为一次 TypeScript 分析，避免重复工作，最大提速 7 倍、内存最高降 75%；相比单独运行 typescript-eslint 与 tsc，最高快 122 倍、峰值内存最高降 82%。
- ⚙️ Fast mode 默认启用：自适应 checker 数量、分组相关工作、启用额外缓存与内存优化。
- ✅ 兼容性：实现 tsgolint v7.0.2007 的全部 61 条规则，力求保持相同配置、诊断、修复和建议，可作为现有 Oxlint 类型感知 lint 的直接替代。
- 🛠️ 使用方式：Vite+ 用户升级到 v1.7.0+ 后运行 vp check 或 vp lint；直接使用 Oxlint 可升级 Oxlint 与 tsrs，执行 pnpm i -D oxlint tsrs 和 pnpx oxlint --type-aware。
- 🔍 类型检查诊断：添加 --type-check 可在 lint 结果之外获取类型检查诊断；若已通过 options.typeAware 启用类型感知 lint，可继续使用原命令。
- 🤖 试用建议：提供 agent 任务模板，让编码 agent 按项目包管理器安装 tsrs、保留 lint 规则，并记录诊断、耗时与峰值内存以对比切换效果。
- 💬 反馈：鼓励在项目中试用并报告输出、修复、运行时或内存差异，加入 Oxc Discord 获取更新。
- 🔮 后续：继续提升兼容性与稳定性，跟进上游 TypeScript/tsgolint，探索更深集成和优化，让全面检查快到可在每次变更后运行。
- 🙏 致谢：感谢 Max Schwenk 创建 tsrs、TypeScript 团队的支持协作以及所有贡献者。

---

### [博客 | pnpm](https://pnpm.io/blog?type=releases)

**原文标题**: [Blog | pnpm](https://pnpm.io/blog?type=releases)

2026年11月 pnpm 12.x 与 11.28.x 密集更新，重点覆盖安全修复、全局配置、离线安装、依赖解析、锁文件格式及 pnpr 兼容性改进。

- 🔐 12.22.0 和 11.28.13 修复安全漏洞：默认或作用域注册表变更后，`pnpm install` 可能跳过对新注册表的 `minimumReleaseAge` 与 `trustPolicy` 检查；11.28.13 还修复 `pnpm audit` 丢弃字符串 ID 通告、离线安装 `minimumReleaseAge` 失败及 peer/注入包解析问题。
- ⚙️ 12.22.0 在全局 `config.yaml` 中新增 `globalPackagesConfig`，新增 `pnpm why --ranges`，并让 `pnpm list --recursive` 按依赖顺序列出工作区项目。
- 📦 12.21.0 支持 `pnpm store add` 为离线安装准备 tarball 和 git 依赖；重复安装保留 peer 依赖选择，并修复 `lockfile.format: v13`、`nodeLinker: hoisted`、`pnpm deploy` 等失败；pnpr 拒绝设置时改为本地解析。
- 🧩 11.28.12 修复大量 peer 依赖、`pnpm deploy`、frozen-lockfile、`nodeLinker: hoisted` 问题；含安全修复：注册表 URL 中的 `${VAR}` 占位符会使命令失败，避免请求发往其他注册表；内置 `node-gyp` 不再携带被安全扫描器标记的 undici，远程解析需 pnpr 0.1.0-alpha.20+。
- 🗂️ 12.20.0 在实验性 v13 锁文件中记录本地目录依赖的 specifier，修复 hoisted、peer、overrides 问题；移除 `node-gyp` 中被标记的 undici；远程解析和共享构建缓存需 pnpr 0.1.0-alpha.20+。
- 💰 12.19.0 新增 `pnpm fund`、`projectScopedOptionalPeers` 和实验性 JSON 锁文件；`loaded` node linker 可处理需构建的包；离线安装错误不再打印注册表凭据；检查所有工作区项目的 `engines` 和平台字段。
- 🧱 12.18.0 支持在 pnpr 注册表上打包、发布、安装平台变体包，新增 agent skills 逐项批准和 `pnpm store add` 离线安装；重复安装及 `verifyDepsBeforeRun` 不再读取未变更工作区项目的 `package.json`。
- 🔧 11.28.11 修复 `excludeLinksFromLockfile` 冻结安装、工作区 `pnpm link`、`pnpm deploy` 悬空符号链接、`verifyDepsBeforeRun` 不必要安装等问题。
- 🧭 12.17.0 新增 `pnpm peers check --global`、`overrides` 的依赖组选择器/通配符，以及 `pnpm outdated`/`update` 对 runtime、包管理器、Cargo、Python 的更新支持；修复 Docker 镜像文件权限和本地依赖变更漏检。
- 🧹 11.28.10 阻止 `pnpm store prune` 在 `cacheDir` 指向父目录时删除其他 store；修复全局命令加载 hoisted 依赖及重复安装漏检本地依赖变更。

---

### [GitHub - pithings/unkernel：一个真正的 Linux 内核，已编译为 WebAssembly。它能在不到一秒内启动到 shell。· GitHub](https://github.com/pithings/unkernel)

**原文标题**: [GitHub - pithings/unkernel: A real Linux kernel, compiled to WebAssembly. It boots to a shell in less than a second. · GitHub](https://github.com/pithings/unkernel)

unkernel 是一个将真实 Linux 内核（基于 Linux 7.x）编译为 WebAssembly 的开源项目，仅用户态程序通过 JIT 模拟运行未修改的 riscv64 二进制，因此能在浏览器或 Node 中不到一秒启动完整的 Alpine Linux 环境，兼具接近原生的性能与真实内核语义。项目在 GitHub 上已获约 459 星标、26 次复刻，采用 GPL-2.0 与 MIT 双许可。

- 🐧 **核心理念**：内核（系统调用、调度器、内存管理、ext4、TCP/IP）是编译后的 wasm 代码而非模拟，只有用户程序通过 kwemu（Zig 编写的 riscv64 CPU）加 JIT 模拟运行，Alpine/Ubuntu 官方二进制可直接运行。
- ⚡ **启动与性能**：内核约 70ms 到达 `/init`，约 0.3 秒出现 Alpine 提示符，页面下载约 10MB；`getppid` 约 170ns，fork+exit+wait 约 60µs（甚至快于原生），JIT 下紧密循环 2.5ns/次，https 下载可达 30MB/s，纯计算仍明显落后原生。
- 🧠 **真实内核能力**：具备真正的 MMU（`arch/wasm` 与 Sv39 页表），支持 fork、mmap、写时复制、线程与信号；支持 ext4、overlayfs、tmpfs、loop、FUSE、9p；自带 TCP/IP 栈与 DHCP/DNS；支持 cgroups、命名空间、userfaultfd、TUN，足以让 systemd 在 Ubuntu 24.04 上启动到 `multi-user.target`。
- 🖥️ **设备与图形**：提供帧缓冲 `/dev/fb0`、evdev 键鼠触摸、ALSA 与 `/dev/dsp` 声音、`AF_VSOCK` 以及与宿主共享内存的准虚拟驱动（kwblk、kwnet、kwfb、kwinput、kwsnd、kwvsock、kwshm）。
- 🌐 **浏览器体验**：打开 unkernel.dev 即可获得带 shell、包管理器、持久磁盘、网络和音画的 Linux；支持 URL 参数如 `?mem=512`、`?net=0`、`?wisp=`、`?jit=0`、`?data=0`、`?worker=1`、`?smp=2`；Chrome/Edge 137+、Firefox 153+、Safari 27+ 可用，依赖 JSPI。
- 💻 **命令行工具**：`npx unkernel` 即可启动，支持 `--disk`、`--data`、`--display --sound`、`--mem`、`--no-net`、`--mount .:/work`、`--forward 8000:80`、`--timeout` 与脚本化输入，并有明确的退出码约定（0 关机、124 超时、253 内核 panic 等）。
- 🧰 **JavaScript SDK**：零依赖 TypeScript SDK（MIT 许可）可在 Node 与浏览器中嵌入，提供 `createKernel`、`exec`、`spawn`（pty 或管道）、`vm.connect`、`vm.fetch`、vsock 字节流、`MemoryFs`/`nodeFs` 宿主目录挂载、零拷贝共享内存、帧缓冲与音视频接口。
- 🚧 **已知限制**：发布版仅单 CPU（SMP 为实验性且不可挂起）、无 IPv6、UDP 仅限 DHCP/DNS、无入站网络连接、无 ptrace 寄存器集（strace/gdb 不可用）、无 seccomp，JIT 将原子指令与系统指令交给解释器，内核 wasm trap 会终止会话。
- 🛠️ **构建与许可**：需 Linux、Zig 0.16、Node 24、clang 21+，首次构建约 12 分钟、占用 5GiB 磁盘；内核为 GPL-2.0-or-later，JS SDK 与网页为 MIT，npm 包整体为 MIT AND GPL-2.0-only；由 Pooya Parsa（pi0）制作，Vercel 赞助。

---

### [发布 v6.0.0 · sindresorhus/type-fest · GitHub](https://github.com/sindresorhus/type-fest/releases/tag/v6.0.0)

**原文标题**: [Release v6.0.0 · sindresorhus/type-fest · GitHub](https://github.com/sindresorhus/type-fest/releases/tag/v6.0.0)

type-fest v6.0.0 是一次重大发布，新增 120 个类型并解决全部开放 issue，同时包含大量性能与正确性修复；但也带来多项破坏性变更，需要按迁移指南升级 TypeScript/Node 和 tsconfig，并调整类型用法。

- 🚨 环境要求：需 TypeScript 6、Node.js 22，并在 tsconfig 开启 `exactOptionalPropertyTypes: true`；`strict` 默认开启且不可设为 false。
- 🗑️ 移除废弃类型：`IfAny`/`IfNever`/`IfUnknown`/`IfNull`/`IfEmptyObject` 改用 `If<Is*, ...>`；`ReadonlyTuple` 改用 `Readonly<TupleOf<...>>`。
- 🔤 大小写转换默认值变化：默认按标点拆分，`CamelCase`/`PascalCase` 不再按数字拆分并保留前导下划线；例如 `KebabCase<'div.card::after'>` 变为 `'div-card-after'`，可用旧选项恢复。
- 🧩 深度类型默认递归数组：`PartialDeep`、`PartialOnUndefinedDeep` 默认 `recurseIntoArrays: true`，数组/元组元素也会变可选；可传 false 保持旧行为。
- 📅 `ReadonlyDeep` 会把 `Date` 转为无 `set*` 方法的 `ReadonlyDate`；`WritableDeep` 可还原，或用 `keep` 选项保留 Date。
- ✅ 谓词结果调整：输入 `never` 时多数谓词返回 `false` 而非 `never`；`IsNull`/`IsUndefined` 对 `any`/`never` 返回 `false`。
- 🧮 数值/字面量类型更严格：`FixedLengthArray` 非字面量长度返回 `never`；`Finite`/`NonNegative` 对宽 `number` 返回 `never`；`NonNegative`/`Negative` 拒绝 `Infinity`。
- 🔁 多项结果修正：`Entries`/`Entry` 按键值配对；`ValueOf` 读取所有联合成员；`Get` 对缺失键返回 `undefined`；`LiteralToPrimitiveDeep` 保留元组。
- 🆕 新增 120 个类型：覆盖数组操作、字符串/大小写、JSON、对象路径、函数重载/柯里化、Map/Set、路由参数、严格事件目标等，如 `ArrayChunk`、`ArrayZip`、`JsonPointer`、`ParsePath`、`Curry`、`Pipe`、`StrictEventTarget`。
- ⚡ 改进：深度类型新增 `keep`，条件类型新增 `strict`，`Paths` 增加选项；数值比较支持 `bigint`；`Get`/`PickDeep`/`Set*Deep` 等类型检查性能提升。
- 🛠️ 修复：修正 `Jsonify`、`Exact`、`PickDeep`、`OmitDeep`、`Merge`、`Join`、`Replace`、数组切片/拼接、大小写转换、深度类型和数字键一致性等问题。
- 📦 配置类型更新：`PackageJson` 增加 `gypfile`、`libc` 等；`TsConfigJson` 移除 TS 5.5/6.0 淘汰项并增加新 lib 值。
- 🧭 迁移要点：按新默认值调整大小写转换、`Split`/`StringToArray` 选项名、`PartialDeep` 数组递归、`ReadonlyDeep<Date>` 和谓词分支判断。

---

