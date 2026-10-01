### [](https://claude.dev/blog/how-we-made-claude-ai-faster/)

**原文标题**: [How we made claude.ai 3x faster in two weeks / claude.dev Blog](https://claude.dev/blog/how-we-made-claude-ai-faster/)

Anthropic 工程团队在 2026 年 8 月的两周冲刺中，通过 Slack 中的人类与 Claude 协作、确定性实验室基准和 CI 棘轮，将 claude.ai 与桌面应用核心体验提升约 3 倍，合并 3000+ 变更且无客户影响事故。

- 🚀 四大旅程占 95% 用户活动：启动应用、开始对话、加载对话、发送消息；13 项 p75 测量平均提速 3.1 倍。
- ⚡ 具体结果：claude.ai 网页冷加载 3.1s→0.55s，Claude Code 新会话 0.8s→0.3s，Cowork 云会话 2.6s→0.73s；每天节省数万用户小时。
- 🤝 使用 Claude Tag（beta，约 Opus 5.5），在一个 Slack 频道中监控部署、完善遥测、维护仪表盘、主动修复并提议项目；人类设定目标、取舍并批准变更。
- 📊 用 Datadog MCP 分析，识别最高影响旅程，建立客户端/服务端可比的端到端基线；启动约 20 个项目并由 Claude 估算毫秒收益，第 3 天完成 12/13 目标。
- 🧱 早期优化包括：把静态 composer 烤进 HTML、预编译 V8 code cache、保持 composer 挂载、悬停预取会话、将侧栏重渲染减少 90%。
- 🔬 核心经验：能被测量就能被优化；用 Valgrind + node --predictable 测指令数，用 React commits、V8 调用数、布局/样式重算、DOM 变更等确定性指标做实验室基准。
- 🛡️ 每个基准必须证明与 wall-clock 相关，否则丢弃；有效指标进入 CI 作为只能下降的棘轮。
- 📉 示例：消息树组装消除重复 message ID 解析，指令 -48%、墙钟 -78%；状态行扫描器加首字符检查，指令 -31%、墙钟 -44%。
- 🔁 工作循环：开线程→追踪并建基准→提交 PR→带 flag 部署→读真实用户数据→成功则下调棘轮，失败则关 flag 迭代→继续找下一处；同时运行 150+ 线程。
- 🐛 发现并修复：侧栏抖动（31% 网页加载在可用后移动）、composer 输入路径 6900 hooks/900 store 订阅、:root:has() 每次 DOM 变更加 24ms、每天 50 万隐藏 reload、IndexedDB 重复克隆，以及 em dash 触发 UTF-16 使代码高亮变慢（1.0s→0.35s）。
- 🚦 护栏：自动审查 + 人工批准、测试先行、短生命周期 feature flags；近 200 个 flag 超过一半已清理；静态 composer 有 jsdom、14 视口 1px、按键、0.1px 字段偏移等测试；高风险变更按员工→1%→全量推进。
- 🎛️ 人类 steering 分三部分：Ambition 鼓励更大胆、Taste 由人类 owner 判断体验取舍、Direction 保持线程窄并聚焦排序/合并/止损。
- 🖥️ 8.33ms 帧预算：用 headless Chrome DevTools begin-frame 实现确定性 120Hz，逐帧优化流式渲染，约 60 个 PR；长回复主线程阻塞 750ms→200ms、CPU 约 1/3、120fps，流式流畅度约 4 倍。
- 📌 后续：claude.ai 和桌面应用目前约快 3 倍，棘轮防止回退；p95、其他旅程和超长对话仍有空间，并向上游 Electron、Chromium、Node.js 贡献。

---

### [](https://www.meticulous.ai/?utm_source=jsweekly&utm_medium=newsletter&utm_campaign=26q3&utm_content=primary)

**原文标题**: [Meticulous AI - Automated Frontend Testing Without Writing Tests](https://www.meticulous.ai/?utm_source=jsweekly&utm_medium=newsletter&utm_campaign=26q3&utm_content=primary)

Meticulous 是一款面向复杂代码库的自动化、穷尽式、确定性端到端测试工具。它通过记录应用交互，由 AI 生成持续演进的视觉测试套件，在合并 PR 前展示改动对用户工作流的影响，几乎无需开发者编写或维护测试，并致力于从底层消除 flaky tests。已有 100 多家组织使用，包括 Dropbox、Notion、Engine 等，集成方式简单，支持主流前端框架。

- ⚙️ 核心主张：自动化、穷尽、确定性验证，零开发者投入，让代码交付速度跟上智能体编写代码的速度，专为全球最复杂代码库构建。
- 🏢 已被 100 多家组织信任采用，用户包括 Dropbox、Notion、Engine 等；反馈称无需再在合并后调试，零维护、无 flaky，开发者很快接受。
- 🧩 工作方式第 1 步：在本地开发、staging 和预览 URL 环境添加脚本标签以记录会话，也可选择记录生产会话来增加覆盖。
- 🤖 第 2 步：AI 引擎跟踪每次交互执行的代码分支，生成持续演进的视觉端到端测试套件，覆盖每行代码、每个用户流程和每个边界情况。
- 🔀 第 3 步：打开拉取请求即可在合并前看到改动跨用户工作流的影响；默认保存并回放后端响应，实现无副作用测试，避免数据变化导致误报，也无需特殊测试账号或模拟数据。
- 🧪 无需再编写、修复或维护测试：测试随应用演进而自动更新，新功能或边界情况出现时自动加测，过时测试自动移除，测试套件始终保持最新完整。
- 🚀 快速迭代：显著提升交付可靠且无回归代码的速度，让团队以更高速度安全发布。
- 🧯 从 Chromium 底层构建，采用确定性调度引擎，从根本上消除 flaky；同时测试执行速度极快，适用于最复杂的应用。
- 🧱 可与现有测试套件配合使用，也可完全替代；测试在大规模计算集群上高度并行化，能在 120 秒内测试数千个屏幕并得到结果。
- 🔌 集成与安全：通过添加 Meticulous recorder 脚本标签即可开始，支持 NextJS、React、Vue、Angular、Nuxt、SvelteKit 等；同时提供集成、安全与文档支持。

---

### [宣布 Vite+ 1.0 | VoidZero](https://voidzero.dev/posts/announcing-vite-plus-1-0)

**原文标题**: [Announcing Vite+ 1.0 | VoidZero](https://voidzero.dev/posts/announcing-vite-plus-1-0)

Vite+ 1.0 正式发布，这是由 Vite、Vitest、Rolldown 和 Oxc 背后的团队打造的统一 Web 开发工具链。它采用 MIT 开源许可，接近每周两百万下载量，通过单条命令 vp 统一管理 Node.js 运行时、包管理器和前端工具链。Vite+ 并非框架、包管理器，也不是 Vite 的替代品，而是一个框架无关的整合方案，将已有工具组合成经过测试的单一技术栈，配以单一配置文件和一致的命令集，支持从 React 应用到大型 monorepo 的各类项目。

- 🚀 **核心定位**：Vite+ 为 Web 开发提供单一入口，将现有工具整合为统一技术栈，拥有单一配置文件与一致的命令体系，且项目本身无需使用 Vite 也能采用。
- 🛠️ **九大命令覆盖本地开发周期**：包括 vp create（脚手架）、vp install（依赖安装）、vp dev（开发服务器）、vp check（格式化/检查/类型检查）、vp test（测试）、vp build（生产构建）、vp pack（库构建与独立二进制）、vp run（带缓存的 monorepo 任务运行器）、vp env（Node.js 版本管理），全部由根目录的 vite.config.ts 统一配置。
- ⚡ **性能大幅提升**：底层工具以 Rust 编写，Oxlint 比 ESLint 快 50 至 100 倍，Oxfmt 比 Prettier 快最高 30 倍，Vite 8 借助 Rolldown 显著加快构建速度。
- 📦 **告别工具链维护**：单个 vite-plus 依赖可替代 vite、vitest、eslint、prettier、tsup、turbo 等一整套依赖及其插件配置，升级只需一次版本号变更且作为整体经过测试。
- 🔄 **跨仓库一致体验**：内置 vp 命令在任何项目中含义相同，项目自定义脚本通过 vpr 运行，方便新成员和 AI 代理上手。
- ⏩ **CI 更高效**：vp run 记录任务实际使用的文件、参数与环境变量，未变更任务可即时重放缓存；setup-vp 将 Node 环境、包管理器与依赖缓存步骤合并为单一操作。
- 🔓 **无锁定风险**：可继续使用喜爱的 Vite 插件和包管理器，vp run 的缓存同样适用于任意脚本。
- 🆕 **Beta 以来的更新**：新增 GitLab CI/CD 的 setup-vp、支持 tsup 迁移、提供 Homebrew 和 Docker 镜像、新增 vp toolchain、vp env doctor、vp hooks 与 vp staged 命令；Vitest 5 稳定，Vite 8.1 发布实验性 Bundled Dev Mode，Oxc 获得原生 React Compiler 支持。
- 🌍 **采用情况**：接近两百万周下载量，超过 2600 个公开仓库依赖 vite-plus；用户包括 Tiptap、Dify、vinext、BlockNote、Inkline、npmx、hono 等，其中 Tiptap 已用 Vite+ 替换其原有的 Vite、Vitest、tsup 和 Oxc 组合。
- 📥 **快速开始**：macOS/Linux 使用 curl -fsSL https://vite.plus | bash，Windows 使用 PowerShell 脚本安装；随后运行 vp create 新建项目，或用 vp migrate 迁移现有项目（迁移前会展示计划，生产项目建议先阅读迁移指南，也可使用迁移提示词配合编码代理）。
- 🔮 **未来规划**：远程缓存、更深入的 monorepo 诊断、vp release 和 vp docs 等功能将在后续版本中推出。
- 🙌 **社区共建**：Vite+ 由国际核心团队与社区共同开发，半数核心成员来自社区，感谢众多贡献者的审核、修复与功能提交。

---

### [迁移到 Vite+ | 面向 Web 的统一工具链](https://viteplus.dev/guide/migrate)

**原文标题**: [Migrate to Vite+ | The Unified Toolchain for the Web](https://viteplus.dev/guide/migrate)

`vp migrate` 是将现有项目迁移到 Vite+ 的迁移命令，可统一整合 Vite、Vitest、Oxlint、Oxfmt、ESLint、Prettier、tsdown 和 tsup 等分散工具配置到 Vite+ 默认体系，涵盖依赖更新、导入重写、配置合并、脚本调整、提交钩子设置以及 agent/editor 配置文件生成等完整流程，但迁移后大多数项目仍需进一步手动调整。

- 🚀 **基本用法**：`vp migrate` 迁移当前目录，`vp migrate <path>` 迁移指定目录，`vp migrate --no-interactive` 无提示运行；monorepo 必须在工作区根目录运行，无法单独迁移某个成员。
- ⚙️ **核心选项**：`--agent <name>` / `--no-agent` 控制 agent 指令写入，`--editor <name>` / `--no-editor` 控制编辑器配置，`--hooks` / `--no-hooks` 控制预提交钩子，`--no-interactive` 跳过交互提示。
- 📋 **迁移流程**：更新依赖、重写导入、将工具专属配置合并进 `vite.config.ts`、更新脚本至 Vite+ 命令面、可选设置提交钩子与 agent/editor 配置，最后格式化项目。
- ✅ **迁移前准备**：未使用 Vite+ 的项目应先升级到 Vite 8+ 和 Vitest 4.1+，并理解现有 lint、格式化和测试设置，保留原始 lockfile。
- 🔍 **迁移后验证**：依次运行 `vp install`、`vp check`、`vp test`、`vp build`（库项目用 `vp pack`），并运行浏览器、覆盖率和基准测试套件。
- ⬆️ **0.3 升 1.0**：1.0 包含 Vitest 5 破坏性变更、tsdown 0.23 升级；可用全局 CLI 或 `pnpm dlx` / `npx --package=vite-plus@1.0.0 vp migrate --no-interactive`，Node 需满足 `^22.18.0 || ^24.11.0 || >=26.0.0`。
- 🧪 **Vitest 迁移**：`vite-plus` 重新导出 `vitest@5.0.1` 于 `vite-plus/test*`，node 模式无需单独安装 vitest；Playwright/WebDriverIO 需额外 provider，导入路径改为 `vite-plus/test*`；`declare module 'vitest'` 类型增强**不**重写，需保持指向上游模块。
- 📦 **tsdown 迁移**：更新 `pack` 块与 `tsdown.config.*` 至 tsdown 0.23，自动插入 `deps.resolveDepSubpath: true` 和 `attw.profile: 'strict'` 兼容设置；`tsdown.config.ts` 选项应移入 `vite.config.ts` 的 `pack` 块并删除原文件。
- 🪝 **lint-staged 与 Git 钩子**：Vite+ 用 `vite.config.ts` 中的 `staged` 块替代 lint-staged；Husky、lefthook、simple-git-hooks、yorkie **不会**自动转换，仅显示警告，需手动迁移至 `staged` 块并更新生命周期脚本运行 `vp config`。
- 🛠️ **钩子命令**：用 `vp hooks status` 验证调度器是否激活，`vp hooks disable` 在当前克隆中关闭，`.vite-hooks/pre-commit` 运行 `vp staged`。

---

### [](https://github.com/tc39/agendas/blob/main/2026/09.md)

**原文标题**: [agendas/2026/09.md at main · tc39/agendas · GitHub](https://github.com/tc39/agendas/blob/main/2026/09.md)

overview summary
TC39 第116次会议议程已发布，会议将于 2026 年 9 月 29 日至 10 月 1 日在日本东京由 Sony 主办，采用 JST 时区，预计总议程容量约 15 小时。文件列出关键截止日期、议程规则、各阶段提案、需共识 PR、项目/任务组报告以及日程限制。

- 📅 会议：第116次 Ecma TC39 会议，2026-09-29 至 10-01，10:00 开始，最后一天 16:00 结束（Asia/Tokyo），地点东京，Sony 主办。
- ⏰ 截止：提案推进资格截止 9 月 19 日 10:00 JST；日程约束截止 9 月 26 日；会前一个月里程碑为 8 月 29 日。
- 📏 议程规则：不寻求推进的提案可随时加入；Stage 0/1 需截止前标注；Stage 2/2.7/3/4 及规范性变更需附支持材料；Stage 4 必须链接规范 PR；提案按 Stage 降序、timebox 升序、插入日期排序。
- 🔑 议程标记：❄️ 硬日程约束、🔒 日程约束、⌛️ 迟交/推进优先、🔁 上次议程续议。
- 🧾 开场行政：开幕、点名、行为准则、IPR、通信工具、GitHub Delegate 团队提醒、速记与法律声明、招募记录员、通过议程与上次纪要、下次会议主办。
- 📊 报告：秘书报告；Eemeli Aro 加入 ECMA-402 编辑；ECMA262/402/404/Test262 状态更新；TG3 安全、TG4 Source Maps、TG5 编程语言标准化实验；CoC 委员会更新。
- ⚖️ Web 兼容/需共识 PR：DataView 分离缓冲区行为、RevalidateAtomicAccess、尾调用优化设为规范性可选、非法输入 RangeError vs TypeError、WeakRef KeptAlive 语义、TG2 编号系统/weekInfo firstDay/typed array toLocaleString。
- 🗂️ 短时讨论：AI 辅助技术政策更新寻求共识；结构化 TC39 数据状态更新。
- 🧩 Stage 3：Iterator Join、Iterator Includes、Iterator Chunking、Dynamic Code Brand Checks 冲刺 Stage 4；禁止向不可扩展对象添加新私有字段。
- 🔄 Stage 2.7：ESM Phase Imports 的模块源标识与非单射源导入规范性 PR；Thenable Curtailment 冲刺 Stage 3。
- 🧪 Stage 2：Intl Sequence Units、Intl Unit Protocol、Amount 更新；export defer 与 JSON.parse Options 冲刺 Stage 2.7；Async iterators 全提案与开放问题（120 分钟）；Include default in export*；Bigint from exponential；Private declarations；Composites。
- 🌱 Stage 1/0：Pulling in AbortController 冲刺 Stage 1 或类似阶段。
- 🗣️ 长时/开放式讨论：重做 Cover 与 Supplemental Grammars；议程截止问题；AI 政策中的模糊性、期望与允许使用；缺少 champion 的 Stage 2 提案；缺少 Stage 2.7 审阅者的提案。
- 🧷 其他事项：timebox 溢出、其他业务、感谢主办方、休会。
- 🚧 日程约束：Kevin Gibbons 偏好不晚于 15:00 JST 发言；Nicolò Ribaudo 希望 Include default in export* 先于 export defer，并强烈偏好 15:00 后；Guy Bedford 仅最后一天 10:00-12:00 JST 可发言；Matthew Gaudet 仅第一天之后 10:00-12:00 JST 可发言。

---

### [](https://github.com/tc39/proposal-iterator-chunking/)

**原文标题**: [GitHub - tc39/proposal-iterator-chunking: a proposal to add a method to iterators for producing an iterator of its subsequences · GitHub](https://github.com/tc39/proposal-iterator-chunking/)

这是一个 TC39 Stage 3 提案，旨在为迭代器增加按可配置大小消费为重叠或非重叠子序列的方法，方便一次处理多个值。

- 🧩 仓库为 tc39/proposal-iterator-chunking，当前 Stage 3，进一步推进依赖至少 2 个已发布实现。
- 📜 规范地址为 https://tc39.es/proposal-iterator-chunking/，并已有 2024 至 2025 年多次委员会展示。
- ⚙️ 核心能力之一是 `chunks(n)`：产生非重叠子序列，如 `[0,1]`、`[2,3]`，最后一个块可能不足。
- 🪟 另一核心能力是 `windows(n)`：产生重叠滑动窗口，如 `[0,1]`、`[1,2]`、`[2,3]`。
- 🎯 动机：某些算法需要同时查看相邻元素，或按批次消费流式数据。
- 📄 `chunks` 用例包括分页、日历/网格布局、批处理与流处理、矩阵运算、格式化/编码、分桶。
- 📈 `windows` 用例包括运行/连续计算如平均值、上下文敏感算法如成对比较、轮播及无限循环。
- 🌍 多语言已有先例：C++、Clojure、Elm、Haskell、Java、Kotlin、.NET、PHP、Python、Ruby、Rust、Scala、Swift 等。
- 📦 JS 生态已有 Lodash/Underscore、Ramda、extra-iterable、iter-tools、itertools-ts、wu、iter-ops 等库，但行为存在差异。
- 🧪 仓库包含 `src`、`test`、`demo`、`spec.emu`、`run-test262.mjs` 等，配有规范、测试和演示。
- 🤝 仓库还包含行为准则、贡献指南、安全策略等文件，便于社区参与。

---

### [](https://github.com/tc39/proposal-iterator-join)

**原文标题**: [GitHub - tc39/proposal-iterator-join: JS proposal for a means to concatenate the contents of an iterator into a string · GitHub](https://github.com/tc39/proposal-iterator-join)

该仓库是 TC39 的 Iterator Join 提案，目标是为 JavaScript 增加将迭代器内容拼接成字符串的能力，目前处于 Stage 3，已有规范与 test262 测试，准备进入实现阶段。

- 📌 **提案名称**：Iterator Join，为 JavaScript 添加把迭代器内容连接为字符串的方法。
- 🧑‍💻 **作者与推进者**：Kevin Gibbons。
- 🚦 **当前状态**：TC39 Stage 3，已有规范与 test262 测试，可供引擎实现。
- 🎯 **核心动机**：将字符串列表合并为单个字符串非常常见；数组可直接 `.join(sep)`，但其他可迭代对象缺少简便方法。
- ⚠️ **现有替代方案问题**：`Iterator.from(it).reduce((a, b) => a + sep + b)` 会分配中间字符串且空迭代器会出错；`Array.from(it).join(sep)` 需要先转换为数组，成本较高。
- 🛠️ **提案方案**：添加 `Iterator.prototype.join`，行为类似 `Array.prototype.join`，但作用于迭代器接收者。
- 🔗 **背景来源**：该需求曾在早期 iterator helpers 提案和 Discourse 讨论中出现。
- 📁 **仓库文件**：包含 `README.md`、`spec.html`、`polyfill.js`、`run-test262.mjs`、`package.json`、`LICENSE`、GitHub workflows 等。
- 📊 **仓库数据**：15 stars、7 watchers、2 forks、1 issue、0 pull requests。
- 📜 **许可与规范**：MIT license，并提供行为准则、贡献指南与安全政策；项目主页为 `tc39.es/proposal-iterator-join/`。

---

### [GitHub - tc39/proposal-iterator-includes：用于迭代器的 Array.prototype.includes · GitHub](https://github.com/tc39/proposal-iterator-includes)

**原文标题**: [GitHub - tc39/proposal-iterator-includes: Array.prototype.includes but for iterators · GitHub](https://github.com/tc39/proposal-iterator-includes)

该仓库是 TC39 的提案 `proposal-iterator-includes`，目标是为迭代器增加 `includes` 方法，用于判断迭代器是否会产出指定值，功能类似 `Array.prototype.includes`。目前提案处于 Stage 3，后续推进依赖至少 2 个已发布的实际实现。

- 📌 提案状态：Stage 3，需 2 个或更多正式实现才能继续推进。
- 🎯 核心目标：让开发者能直接询问迭代器是否产出某个值，类似数组的 `includes`。
- 🧠 动机：虽然可以用 `some` 加自定义比较器，但不够直接简洁，也容易在多种比较方式间做无谓选择。
- ⚖️ 比较操作：最终选择 SameValueZero，以匹配 `Array.prototype.includes` 的行为。
- 🧮 第二参数：包含 `fromIndex`，但迭代器已有 `drop`，所以并非必需；不支持负偏移，这与数组方法不同但符合迭代器语境。
- ✅ 最终方案：在 `Iterator.prototype` 上新增 `includes` 方法。
- 💻 示例：`gen().includes(1)` 返回 `true`，`gen().includes(2)` 返回 `false`，`gen().drop(1).includes(3)` 返回 `true`。
- 📦 仓库信息：公开仓库，约 13 stars、3 forks、1 issue、13 commits；规范地址为 `tc39.es/proposal-iterator-includes`。

---

### [](https://developer.chrome.com/release-notes/154#javascript)

**原文标题**: [Chrome 154  |  Release notes  |  Chrome for Developers](https://developer.chrome.com/release-notes/154#javascript)

Chrome 154 稳定版定于 2026 年 9 月 22 日发布，适用于 Android、ChromeOS、Linux、macOS 和 Windows。本次更新涵盖 CSS/UI、JavaScript、网络与连接、隐私与安全、隔离 Web 应用（IWA）及源试验。

- 🗓️ 稳定版发布日期为 2026 年 9 月 22 日；除非另有说明，变更适用于各平台 Chrome 154 稳定版。
- 🎨 `scroll-marker-group` 新增 `links`（默认）与 `tabs` 模式，分别按导航列表和标签页方式处理焦点与无障碍语义。
- ✍️ `text-decoration-inset` 可控制下划线、上划线和删除线的内缩或外扩，支持 `auto`、长度和百分比值。
- 🧵 CSS Typed OM 的 `CSSStyleValue` 层级暴露到 Worker 上下文，与规范和其他浏览器引擎保持一致。
- 🔤 `FontFace.width` 属性与 `@font-face` 的 `font-width` 描述符成为 `stretch` / `font-stretch` 的别名。
- 🪟 Popover 和 Dialog 的轻触关闭改用 `click` 事件，避免触摸滚动或右键误关闭。
- 📐 站点可选择让 `<iframe>` 响应式调整大小，按嵌入文档的布局溢出尺寸设置，减少子文档滚动。
- 🔁 JavaScript 实现 TC39 的 `Iterator.prototype.includes()`，用于检查迭代器是否产出指定值。
- 🔌 `WebSocket` 构造函数支持第二个选项对象 `WebSocketInit`，可传 `protocols`，并为未来选项扩展预留。
- 🏠 WebSocket 支持 `targetAddressSpace` 选项，可将公共主机名连接视为 `local` 或 `loopback`，与 Fetch 一致。
- ⛔ Fetch API 会将 `AbortController` 的中止原因转发到 `Response` 及其 `ReadableStream`，而不仅是 `fetch` Promise。
- 🛡️ Background Fetch 强制执行 CORS，与常规 `fetch()` 一样受安全策略检查，防止绕过。
- 🌐 Background Fetch 受本地网络访问（LNA）限制，需 Service Worker 来源具备相应权限；企业可用现有 LNA 策略管理。
- 🔒 默认启用“HTTP 前询问”，用户连接不安全 `http` 站点时会收到提示；管理员可用 `HttpsOnlyMode` 控制。
- 💳 Secure Payment Confirmation 的 `locale` 字段若无语言标签匹配对话框语言，会返回 `NotSupportedError`；未设置或为空则跳过验证。
- 🪟 隔离 Web 应用（IWA）在 ChromeOS 白名单中可使用 Window Shape API 定义自定义窗口形状，需无框显示模式与 `window-management` 权限。
- 🧪 源试验：Private Verification Tokens（PVT）可在常规浏览中签发、在隐私模式中兑换，用于减少 CAPTCHA 等摩擦。

---

### [](https://x.com/jarredsumner/status/2104739495895781679)

**原文标题**: [Jarred Sumner on X: "An early preview of experimental Bun + JSC with ahead-of-time compilation

For Claude Code's CLI: 24% faster startup, 48% lower memory, 46% lower CPU, and nearly 2x larger binary size" / X](https://x.com/jarredsumner/status/2104739495895781679)

Jarred Sumner 在 X 上公布实验性 Bun + JSC 提前编译（AOT）的早期预览，并展示其对 Claude Code CLI 的性能影响。

- 🧪 发布内容：实验性 Bun + JSC 提前编译（ahead-of-time compilation）预览
- ⚡ Claude Code CLI 启动速度提升 24%
- 🧠 内存占用降低 48%
- 🔋 CPU 占用降低 46%
- 📦 二进制体积几乎增大到原来的 2 倍
- 📅 发布于 2026 年 9 月 29 日凌晨 1:06
- 📊 帖子约 7.2 万次浏览，65 条回复、59 次转发、1.1K 点赞、169 次收藏

---

### [介绍 cf：适用于整个 Cloudflare API 的智能体 CLI | Cloudflare 博客](https://blog.cloudflare.com/cloudflare-cf-cli-launch/)

**原文标题**: [Introducing cf: the agentic CLI for the entire Cloudflare API | Cloudflare Blog](https://blog.cloudflare.com/cloudflare-cf-cli-launch/)

Cloudflare 推出全新 CLI：cf，定位为面向 AI 代理的 agentic CLI，目标是让代理访问整个 Cloudflare API。Wrangler 中代理使用量已从去年个位数升至 48%，但其仅覆盖约 280 个操作；借助 Forge 从 OpenAPI schema 生成，cf 覆盖 3000+ 操作。cf 默认 JSON 输出，支持自然语言命令搜索、TypeScript 配置 cloudflare.config.ts、Vite 默认开发体验，并提供迁移工具；Wrangler 将在 cf 正式版后继续维护 18 个月。

- 🚀 Cloudflare 发布 cf：面向整个 Cloudflare API 的 agentic CLI，已开放全球公测。
- 📈 代理对 Wrangler 的使用激增：2026 年 3 月占四分之一，上周达 48%；代理每天使用更多不同命令。
- 🤖 目标：让代理用单一工具完成设置 Worker、部署、监控、用 Access 保护、购买域名、加 WAF 等。
- 🔄 从 Wrangler 约 280 个操作扩展到 Cloudflare API 的 3000+ 操作；Forge 从 OpenAPI schema 生成 CLI 命令。
- 🔍 内置 cf cli search：代理可用自然语言查找合适命令，避免上下文膨胀；首次运行 --help 会提示该功能。
- 🧾 默认输出 JSON：方便代理过滤结果、节省 token；人类可用格式化输出，复杂操作可用表单式输入。
- ⚙️ 新配置格式 cloudflare.config.ts：TypeScript 类型检查，便于人和代理编辑；支持 bindings 与 triggers 辅助函数。
- 🧩 配置可程序化生成环境，减少重复；Worker 配置可通过 cf migrate 迁移。
- 🛠️ 默认基于 Vite：提供最佳本地开发服务器、HMR、Rolldown 构建、插件生态，并与 Vitest 集成。
- 🔁 迁移策略：cf migrate 可自动转换；依赖 esbuild、Rust 或 Python 的 Worker 暂时委托 Wrangler。
- 📦 安装与使用：npm i -g cf；cf init 新建项目；cf deploy 部署；静态站点无需配置文件即可部署。
- 🕒 Wrangler 最终大版本将引导使用 cf；公测结束后继续维护 18 个月。
- 🌐 cf 开源，问题可提交到 GitHub 仓库。

---

### [获取失败](https://blog.angular.dev/an-update-on-angulars-typescript-7-powered-compiler-9619a35e2b0a)

**原文标题**: [Failed to retrieve](https://blog.angular.dev/an-update-on-angulars-typescript-7-powered-compiler-9619a35e2b0a)

无法总结：获取内容失败，状态码 403。

---

### [发布 v3.0.0 · mswjs/msw · GitHub](https://github.com/mswjs/msw/releases/tag/v3.0.0)

**原文标题**: [Release v3.0.0 · mswjs/msw · GitHub](https://github.com/mswjs/msw/releases/tag/v3.0.0)

MSW（mswjs/msw，约 18.2k Star）发布 v3.0.0，这是一次重大版本更新，包含破坏性变更、新功能和错误修复，核心变化包括仅支持 ESM、提高 Node.js/TypeScript 最低版本，并重构 GraphQL、WebSocket 和工具入口等 API。

- 🚨 v3.0.0 已发布（2026-09-28），由 kettanaito 发布，包含 1 个提交。
- 📦 仅支持 ESM；最低 Node.js 提升到 v22，弃用 v18/v20。
- 🧩 msw/native 移除，改用 @msw/react-native；最低 TypeScript 要求 5.9，弃用 5.1/5.2。
- ⏳ worker.stop() 现在返回 Promise；关键在途场景需要 await。
- 🔗 GraphQL 从 msw/graphql 导出，并成为可选 peer dependency；GraphQLLinkHandlers 重命名为 GraphQLLink。
- 🔄 移除 handleRequest()，改用 defineNetwork()。
- 🍪 Node.js 不再管理 cookies，改为环境默认；request.headers.get('cookie') 返回 null，应使用 cookies 解析参数；不再 patch setTimeout。
- 📡 WebSocket connection 生命周期事件改名为 websocket:connection；onUnhandledRequest 改名为 onUnhandledFrame。
- 🚫 其他破坏性变更：file:// 请求和经 fetch() 的 HTTP-to-WebSocket upgrade 在 Node.js 中抛错；bypass() 移除 Content-Length。
- ✨ 新特性：支持 Node.js v24/v26、TypeScript v6/v7、GraphQL v17、GraphQL subscriptions，以及页面导航和表单提交拦截。
- 🧰 新增 msw/utils 入口，可按需导入 delay/passthrough；新增 Vite 插件、WebSocket Extension API 和 websocket:error 事件。
- 🔌 支持在 passthrough 场景修改拦截请求头；从 path-to-regexp 迁移到 @msw/url；移除 graphql、path-to-regexp、picocolors、statuses、strict-event-emitter 等依赖。
- 🐛 修复 beforeunload 导致 worker 注销、Vitest 浏览器模式 + Firefox 间歇失败、worker.stop() 前在途请求错误 passthrough、localStorage cookie 配额超限及 Node.js 网络拦截等问题。
- 👥 贡献者：Andarist 和 kettanaito。

---

### [](https://blog.cloudflare.com/vinext-nextjs-on-vite/)

**原文标题**: [Next.js applications, powered by Vite: introducing Vinext 1.0 | Cloudflare Blog](https://blog.cloudflare.com/vinext-nextjs-on-vite/)

Cloudflare 发布 Vinext 1.0，这是一个基于 Vite、兼容 Next.js 的框架，目标是让任何 Next.js 应用（Pages Router 或 App Router）都能可移植并部署到任意 Web 平台。Vinext 最初源于 2026 年 2 月一次 AI 驱动的实验，如今已用于客户生产环境；1.0 重点提升兼容性、稳定性、缓存行为，并加入迁移、缓存预热和持续自动化维护能力。

- 🚀 Vinext 1.0 正式发布：从实验项目毕业，成为可用于生产的高流量动态应用框架。
- 🌍 跨平台部署：支持把 Next.js 应用迁移到 Cloudflare Workers 免费计划、Netlify、AWS Lambda 等平台。
- 🧭 双路由支持：同时支持 App Router、Pages Router 及混合应用，覆盖 RSC、Server Actions、API 路由、路由处理器、中间件和客户端导航。
- ✅ 兼容性超 99%：核心客户关注功能的测试兼容性超过 99%（不含缓存组件），并通过社区反馈和 nightly Next.js E2E 测试持续验证。
- 🧱 完整页面生命周期：支持服务端渲染、构建时预渲染、静态导出、页面级 ISR，以及按路径或标签进行后台/按需重新验证。
- 💾 统一缓存能力：App/Pages Router 与运行时共享缓存函数，并支持 Cloudflare Workers Cache。
- 🔍 可观测性：提供 Next.js 兼容 tracing，兼容 OpenTelemetry/Sentry，并集成 Cloudflare Workers Observability。
- 📦 生态兼容：实现 `next/*` 公共接口，支持认证、MDX、图片优化、字体、metadata、环境变量等常见模式。
- ⚙️ Workers 一等支持：服务端代码可在 workerd 运行时开发与生产运行，直接访问图片优化、Hyperdrive 等 bindings。
- 🚚 迁移简单：运行 `npx vinext check` 和 `npx vinext init` 即可检查兼容性并生成 Vite/部署配置，同时保留原项目结构。
- 🔥 缓存预热：把构建时预渲染从构建机器转移到 Cloudflare 网络，提前为高流量页面填充缓存；部署时先发布到 0% 流量，预热后再安全提升。
- 🧪 有限支持 `use cache`：对驱动 Cache Components 的 `use cache` 指令支持有限，因为多数团队未将其视为迁移前提。
- 🤖 持续自动化维护：每日审查 Next.js canary 变更、夜间重跑兼容矩阵，代理可定位差异、复现、移植测试并提出修复。
- 🛠️ 立即试用：新建应用用 `npm create vinext-app@latest my-app`；迁移用 `npx vinext check && npx vinext init`；部署用 `npx @vinext/cloudflare deploy --warm-cache`；文档见 vinext.dev，开源地址为 github.com/cloudflare/vinext。

---

### [](https://github.com/mermaid-js/mermaid/releases/tag/mermaid%4012.0.0)

**原文标题**: [Release mermaid@12.0.0 · mermaid-js/mermaid · GitHub](https://github.com/mermaid-js/mermaid/releases/tag/mermaid%4012.0.0)

Mermaid 12.0.0 是一次破坏性大版本：默认布局改为 ELK，默认主题/外观改为 redux-color / neo，新增 UML 用例图，并要求 ES2024、Safari 17.4+、Node 22.12+；若要保留旧渲染，需显式设置 `layout: 'dagre'`、`theme: 'default'`、`look: 'classic'`。

- 💥 破坏性升级：要求 ES2024、Safari 17.4+、Node.js 22.12+，旧浏览器可能需要 polyfill 或转译。
- 🧩 ELK 成为内置默认布局引擎：流程图、状态图、类图、ER、需求、用例等未指定 `layout` 时会从 dagre 切换到 ELK；可显式用 `layout: 'dagre'` 恢复。
- 🎨 新默认外观：`redux-color` / `neo` 取代 `default` / `classic`，未配置的图会重新布局和配色。
- 🆕 新增 UML 用例图：支持角色、用例、系统边界、关系、构造型、备注、JSON 表、类/样式、无障碍元数据和业务变体。
- ⚙️ 布局配置增强：支持 `elk.stress`、`elk.force`、`elk.mrtree`、`elk.sporeOverlap`、`elk.box`、`elk.rectpacking` 等变体；容器可用 `@{ algorithm: … }` 指定自己的 ELK 算法。
- 🧹 移除 `defaultRenderer`：流程图、类图、状态图的该选项失效，改用顶层 `layout: 'dagre' / 'elk'`；旧 legacy 渲染器 ID 移除。
- 📦 构建变化：ESM 中 ELK 按需加载；IIFE 内联后约增大 500 kB gzip；tiny 构建不含 ELK，会回退到 dagre。
- 🧭 配置粒度增强：`theme`、`look`、`layout` 可按图类型设置；优先级为 front matter/directive、`initialize()`、图类型默认、全局默认。
- 🌈 主题增强：`redux-color` / `redux-dark-color` 支持类框、流程图子图、复合状态、泳道、用例图等按项、按容器或按角色轮换配色。
- 🐛 关键修复：块图渐变边框、C4 边界端点、ELK 箭头日志、子图边框/标题留白、复合状态循环起始点、手绘填充和线跨避让等。
- 📐 图形与标签修复：多边形边连接偏移半像素、stadium 标签不再挤成圆形、`</br>` 识别为换行、Circle/Delay/Display 节点按标签高度调整尺寸。
- 🧪 性能与维护：深度缩进解析性能从约 1.4 秒降至约 30 毫秒；移除部分内部布局导出；更新 `@mermaid-js/parser@2.0.0`。
- ✅ 兼容旧外观：初始化时设置 `mermaid.initialize({ layout: 'dagre', theme: 'default', look: 'classic' })`，或在前言中按图设置。

---

### [用例图 (12.0.0+) | Mermaid](https://mermaid.ai/open-source/syntax/usecase.html)

**原文标题**: [Use case diagrams (12.0.0+) | Mermaid](https://mermaid.ai/open-source/syntax/usecase.html)

Mermaid 12.0.0+ 的用例图用于展示参与者与系统用例的交互；本文覆盖语法、默认渲染、元素类型、边界、关系、注释、JSON 表、样式、颜色、配置、无障碍与 PlantUML 迁移。

- 🧩 以 `usecase-beta` 开头；UML 中写作 use case，Mermaid 的关键 token 是 `usecase-beta`，每条语句必须独占物理行。
- 🧭 用 `direction TD`、`TB`、`BT`、`LR` 或 `RL` 选择布局方向。
- 🎨 默认使用 `redux-color` 主题、`neo` 外观和 ELK 布局；可通过 front matter 或 `mermaid.initialize()` 覆盖，`layout` 是顶层选项。
- 🆔 Actor 与用例标识符匹配 `[A-Za-z0-9_]+`，可数字开头且图内全局共享；裸 actor 用标识符作标签。
- 👤 Actor 支持普通 stick、`hollow`、`awesome`、`icon`；图标需先注册 icon pack，失败时显示 unknown-icon fallback；metadata 仅接受 `type`、`icon`、`business`。
- 💼 `business: true` 只适用于普通/空心 actor 或椭圆用例；矩形用例、awesome actor、icon actor 不能是 business 元素。
- 🏷️ 构造型用 `<<...>>`，放在 metadata 后、`:::` 类后缀前，保留大小写并显示在主标签上方，但不自动创建 CSS 类或选择器。
- 🔤 标签支持括号/方括号内未引号文本、单行普通字符串、Mermaid Markdown 字符串；未引号文本按字面、单行、去首尾空格，保留字符需引号或实体码。
- 💬 Markdown 字符串外层双引号、内层反引号，可含物理换行；普通字符串不处理 Markdown 或反斜杠转义。
- 📝 每条语句占一行，但 Markdown 字符串、多行 metadata、JSON、无障碍描述和边界块例外；`%%` 是整行注释，`//`、`#` 不是注释，`;` 不是分隔符。
- 📦 `systemBoundary` 用 `systemBoundary <id><title>@{...}:::<classes>` 分组 actor/用例；默认 `rect`，`type: package` 显示包标签；边界仅一层，内容只允许 actor/用例声明、空行和 `%%` 注释。
- 🔗 支持 7 种实线关联，保留标记方向与类型；可加标签，含 `include`/`extend` 的标签仍是普通关联；JSON 节点只能连接点、反向点或无标记实线关联。
- 📐 `include`、`extend`、泛化需显式操作符；include/extend 端点必须是用例，泛化需两个 actor 或两个 use case。
- 🆔 显式边 ID 写在 `@` 前并紧邻操作符，可被 `class`、`style`、metadata 引用；匿名边不能按 ID 样式；`animate`/`animation` 控制动画，额外短横线增加最小布局长度。
- 🗒️ 注释附着单个 actor/用例，目标可后声明；注释是普通节点，布局会随方向移动，不能指向 JSON 节点、边界、边或其他注释。
- 📊 顶层 JSON 声明生成表格，标题为标识符，正文必须是严格 JSON 对象；属性按源顺序，数组按索引，嵌套用 `address.city` 路径；数组/标量不能作根。
- 🎛️ 样式支持 `classDef`、`class`、`style` 和 `:::`；CSS 声明用逗号分隔 `property:value`，字面逗号用 `\,`，分号被拒绝；优先级为主题变量 → default 类 → 命名类 → 直接 style。
- 🖌️ Actor metadata 是有类型的，不是样式 map；`fillColor`、`strokeColor`、`strokeWidth` 等会报错，应改用 `classDef`、`class` 或 `style`。
- 🌈 颜色按元素种类而非声明顺序；主题变量覆盖 actor、用例、边界、include/extend 的填充与描边；include 与 extend 使用不同色相；系统边界按出现顺序使用主题调色板编号。
- 🔄 `colorScheme: rotate` 让 actor 和用例也逐元素取分类调色板颜色，actor 先编号、用例后编号；会牺牲稳定性，插入元素会移动后续同类颜色；仅颜色主题有调色板，`classDef`/`style` 可覆盖。
- ⚙️ 常用配置键包括 `actorFontSize` 14、`usecaseFontSize` 12、`nodeSpacing` 50、`rankSpacing` 50、`diagramPadding` 20、`colorScheme` 默认 `role`、`useMaxWidth` true 等。
- ♿ 用 `accTitle`/`accDescr` 提供可访问标题与描述；`accDescr` 支持单行或块；渲染元素含语义可访问名称，包含变体、业务角色、构造型和关系类型。
- 🔁 从 PlantUML 迁移：一行一语句；未声明端点变椭圆用例；actor 必须显式声明；`include`/`extend` 语义用 `..> : include` / `..> : extend`；不支持分隔符、别名、`skinparam`、`<style>`、`allowmixing`、link hints、独立 package/rectangle、`newpage` 等。
- ⚠️ `A("Line1\nLine2")` 会保留反斜杠和 `n` 字面量，`A("Paren \( x")` 也保留反斜杠；真实换行需用 Markdown 字符串物理换行或实体码如 `#40;`、`#41;`。

---

### [发布 pnpm 12.8 · pnpm/pnpm · GitHub](https://github.com/pnpm/pnpm/releases/tag/v12.8.0)

**原文标题**: [Release pnpm 12.8 · pnpm/pnpm · GitHub](https://github.com/pnpm/pnpm/releases/tag/v12.8.0)

pnpm 12.8.0 发布，重点改进发布安全、工作区并发安装、命令行配置、锁文件与补丁一致性、依赖解析、缓存存储以及 Windows 使用体验。

- 🚀 pnpm 12.8.0 发布，核心变化覆盖安装、解析、锁文件、工作区、缓存、发布、配置和跨平台支持。
- ⚠️ `pnpm pack` / `pnpm publish` 会警告打包了未列入 `files` 的 `.env` 或 `.env.*`，但 `.env.example` 等模板除外。
- 🤫 `pnpm pack` 支持 `--silent`、`--reporter=silent`、`--loglevel=silent` 隐藏 tarball 内容；配合 `--json` 仍保留脚本与 JSON 输出。
- ⚙️ 所有设置都可通过 `--config.<name>=<value>` 传入，并优先于 pnpmfile 的 `updateConfig`，避免设置被忽略后重写锁文件。
- 🧵 `sharedWorkspaceLockfile: false` 时工作区项目可并发安装，最高按 `workspaceConcurrency` 执行，并共享元数据、锁文件校验和存储缓存。
- 🛡️ 通过 pnpr 服务器安装会记录 pnpmfile 校验和，`--frozen-lockfile` 对 pnpmfile 变更更严格，并处理 `publishConfig.directory` 不一致。
- 🔁 离线安装会优先选择 store 中已有 tarball 的最新匹配版本；旧版镜像缓存布局会给出更明确错误与修复提示。
- 📦 修复 git 依赖、`file:` 依赖、`npm:` alias、peer 依赖解析等问题，减少错误版本、重复解析和构建失败。
- 🧹 `nodeLinker: hoisted` 下会清理孤立目录、恢复被删除的 `node_modules`，并改善并发安装与共享依赖链接。
- 🔒 `--frozen-lockfile` 支持 detached HEAD 下的 `gitBranchLockfile`，并更严格检查缺失 importer、缺失快照和 CI 过期锁文件。
- 🧩 修复 injected workspace 依赖、`publishConfig.directory`、`linkDirectory` 等场景，避免符号链接误删、注入副本不同步和构建目录问题。
- 🗂️ 工作区发现会跳过点开头目录；`pnpm import` 会保留 workspace 内 `yarn.lock` 的版本锁定。
- 💾 Store 文件权限遵循 umask，并保留 owner/group/mode；修复硬链接存储文件时尽量保留 inode，提升共享存储修复效率。
- 🧪 Side-effects 缓存会恢复构建脚本创建的符号链接；全局虚拟存储与 side-effects 缓存按 Node.js 运行时版本隔离构建产物。
- 🩹 `patchedDependencies` 校验更严格：修复 patch hash 不一致、frozen-lockfile 报错、hoisted 重复打补丁、补丁文件缺失等问题。
- ➕ `pnpm add <dir>` 对 peer 依赖发出警告；`--save-types` 不再添加已废弃 `@types` 包；`package.json5` 更新保持 JSON5 风格。
- 🏃 `pnpm run` / `pnpm exec` 不再自动安装当旧 `pnpm` 字段包含覆盖配置；过滤运行只安装选中项目，并改进 Ctrl+C、后台输出和脚本退出码处理。
- 🧰 脚本环境改进：`scriptShell` / `shellEmulator` 协同、Git Bash、`npm_config_node_gyp`、`npm_command` 和 `node_modules/.bin` 解析等。
- 📤 发布/打包/部署增强：`files` 包含被排除目录、prune 排除目录、publish 等待至少 5 分钟、deploy 复制工作区依赖而不硬链。
- 🔧 配置与认证改进：`PNPM_CONFIG_WORKSPACE_DIR`、`_password` base64 校验、`proxy=false` 覆盖代理变量、配置依赖插件 pnpmfile 钩子生效。
- 🌍 全局包与运行时：`pnpm update --global` 迁移 pnpm 10 全局包；信号透传；arm64 musl 兼容；`pnpm env remove --global` 清理 Node.js。
- 🪟 Windows 修复：Ctrl+C 不再卡终端；`pnpm run` 参数原样传递；无需 VC++ Redistributable；`.cmd` shims 处理 `%`、非 ASCII、Cygwin 等。
- 🔍 检查与输出：`pnpm audit`、`pnpm licenses list`、`pnpm root` 更准确；错误信息更具体，并减少无意义的策略放宽建议。
- 🙌 本次更新以稳定性、安全性、跨平台和 monorepo 体验为主，建议升级后重点关注锁文件、补丁和配置迁移。

---

### [发布 22.2.0 · angular/angular · GitHub](https://github.com/angular/angular/releases/tag/v22.2.0)

**原文标题**: [Release 22.2.0 · angular/angular · GitHub](https://github.com/angular/angular/releases/tag/v22.2.0)

Angular 发布了 v22.2.0 最新版本，由 thePunderWoman 于 9 月 23 日 17:53 发布，自上一版本以来包含合并到 main 的 186 个提交；本次更新覆盖 compiler、compiler-cli、core、forms、language-service 和 router 等关键模块。

- 🚀 发布 v22.2.0，标记为 Latest，并包含 186 个提交。
- 🔒 该版本为不可变发布，仅发布标题和说明可修改。
- 🧩 compiler：允许模板访问私有属性；父选择器包含 ::ng-deep 时不封装嵌套选择器；对嵌套 CSS 规则进行作用域化。
- 🛠️ compiler-cli：新增 strictUnclaimedEventNames 选项以捕获拼写错误的输出绑定；限定 keyed defer 块的类型检查；跨多个块去重延迟导入。
- ⚙️ core：新增 ErrorBoundary 编程式 API 和指令测试工具；支持从视图或内容查询读取 Injector；支持 WebMCP 工具声明中的注解；修复列表重排时嵌套视图离开动画取消；支持 animate.enter 和 animate.leave 的函数与信号绑定；更新 FakeNavigation 以符合 WHATWG HTML 规范。
- 📝 forms：允许信号表单中的永久隐藏字段；为 WebMCP 隐式信号表单硬编码 readOnlyHint 和 untrustedContentHint。
- 🧠 language-service：新增对 @boundary 块的支持（#70463）。
- 🧭 router：新增 containsTree 公共 API；允许抛出 RedirectCommand 触发重定向；公开 router 资源；稳定自动清理注入器功能；仅根据资源加载状态判断阻塞状态；暴露 ActivatedRoute 资源的 reload 方法；回滚时保持冻结状态直至资源加载完成；将 router_resource 模块级符号标记为无副作用。
- 📦 发布包含 3 个资源文件；社区反应包括 👍4、🎉5、❤️23、🚀2，共 28 人反应。

---

### [版本发布 | Tiny](https://tinybase.org/guides/releases/#v10-0)

**原文标题**: [Releases | TinyBase](https://tinybase.org/guides/releases/#v10-0)

TinyBase 发布日志按时间倒序记录了各主要版本的新功能与改进，从 v1.1 一路演进至 v10.0，涵盖持久化、同步、UI 组件、查询引擎、Schema 系统与 AI 集成等方向。

- 🗄️ **v10.0 新增 TinyJoinPersister**：可在浏览器中通过 TinyJoin 这一 Worker 优先的关系型数据库保存和加载 Store，支持 JSON 与表格模式。
- 🏢 **v10.0 新增 MsSqlPersister**：绑定 SQL Server、Azure SQL Database 与 Azure SQL Managed Instance，采用 rowversion 列轮询实现自动加载。
- ⚠️ **v10.0 破坏性变更**：移除 CR-SQLite、sqlite3、ElectricSQL 三个 Persister，并提升 libSQL 客户端要求至 v0.18。
- 📚 **v10.0 完善 Agent Skill**：官方 `build-with-tinybase` 技能随 npm 包发布，新增 Persister／Synchronizer 生命周期与 Cloudflare Durable Object 参考资料。
- ♿ **v10.0 无障碍增强**：文档站点支持全程键盘导航、跳过内容链接与屏幕阅读器友好的主题切换。
- 🧩 **v9.7 新增 node:sqlite Persister**：无需第三方依赖，支持 JSON 与表格模式；同时弃用 sqlite3 与 electric-sql 持久化器。
- 🔌 **v9.6 一次新增多个 Persister**：覆盖 pg、Supabase、better-sqlite3 与 Capacitor SQLite，并让 IndexedDB 支持 MergeableStore，同时统一 SQL 占位符风格。
- 🧱 **v9.5 Schema 增强**：支持 enum 枚举与 type 联合数组，并修正一批 `/with-schemas` 类型声明。
- 🛡️ **v9.4 可靠性加固**：新增 `selectAll` 查询，多路复用 WebSocket 限制通道数并清理碎片与订阅。
- 🌐 **v9.3 单连接多路复用**：多个 MergeableStore 可共享一条 WebSocket，通过 channel Id 区分逻辑路径；同时修复事务回滚与任意 Id 安全性。
- 🤖 **v9.2 面向 AI 优化**：发布 `llms.txt`、`llms-full.txt`、Context7 索引与官方 Agent 技能，并让脚手架输出 AGENTS.md。
- 🔢 **v9.1 必填 Schema 字段与自定义排序**：可标记 required 而不需要默认值，`getSortedRowIds` 等支持自定义排序器。
- 📊 **v8.5 React 图表组件**：新增 `ui-react-dom-charts`，包含 LineChart、BarChart 与可组合的 CartesianChart。
- 🎨 **v8.3–v8.4 补齐 Solid 支持**：先加入 `ui-solid` 响应式原语，再补上 DOM 组件与 Inspector，并支持以查询结果作为查询来源。
- 🧵 **v8.1–v8.2 引入 Svelte 支持**：新增基于 runes 的 `ui-svelte` 模块，随后补齐 Svelte 的 DOM 组件与 Inspector。
- 🧬 **v8.0 对象与数组类型 + Middleware**：Cell／Value 可直接存放对象与数组，Middleware 允许在写入前校验、转换或拒绝数据。
- ⚙️ **v7.x 系列**：v7.0 支持 null 类型，v7.1 引入 Schematizers，v7.2 加入参数化查询，v7.3 提供 useState 风格的状态钩子。
- 🧳 **v6.x 系列**：覆盖 OPFS、React Native MMKV／SQLite、Durable Object SQL 存储、Bun SQLite、子集持久化与 omni 模块等。
- 🔄 **v5.0 里程碑**：引入 MergeableStore（CRDT）与 Synchronizer 框架，支持 WebSocket、BroadcastChannel 与本地同步。
- 🗃️ **v4.0 数据库持久化起点**：提供 SQLite3、SQLite WASM、CR-SQLite、Yjs 与 Automerge 等 Persister，并持续扩展至 IndexedDB、PartyKit、LibSQL、PowerSync 等。
- 🧮 **v2.0 查询引擎**：引入 TinyQL 查询、排序与分页；v3.0 增加键值存储；v3.1 带来基于 Schema 的类型系统。

---

### [QUnit 3.0 升级指南 | QUnit](https://qunitjs.com/upgrade-guide-3.x/)

**原文标题**: [QUnit 3.0 Upgrade Guide | QUnit](https://qunitjs.com/upgrade-guide-3.x/)

若测试在 QUnit 2.24 或更高版本上通过且没有警告，通常即可无改动升级到 QUnit 3。QUnit 3.0 主要移除废弃方法并将警告升级为错误；重大版本未引入显著新功能，相关能力已在 QUnit 2.x 中逐步加入。

- 🚀 升级条件：QUnit 2.24 上测试通过且无警告，可无改动升级到 QUnit 3。
- 🧭 发布理念：重大版本不主打新功能，QUnit 3 相关特性已在 QUnit 2.x 系列中逐步出现。
- 🎨 新默认主题：更快、更可访问，并改进错误报告。
- ✅ 新增断言：assert.step、assert.timeout、assert.rejects、assert.true、assert.false、assert.propContains、assert.closeTo。
- 🧪 测试生成：QUnit.test.each() 可通过数据提供器生成测试用例。
- ⏭️ 条件跳过：QUnit.test.if() 可在条件为假时自动跳过测试。
- 📊 性能分析：QUnit.reporters.perf 可在浏览器 DevTools 中查找并分析慢测试。
- ⚠️ 警告升级为错误：错误模块中的 beforeEach、异步模块作用域、runEnd 后意外测试等。
- ⏱️ 默认超时：QUnit 3 默认测试超时为 3 秒，可用 config.testTimeout 调整。
- 🔢 assert.expect 变更：QUnit 3 不再将 assert.step() 计入断言数，可移除 assert.expect 或启用 countStepsAsOne。
- 🗑️ 移除 QUnit.load()：通常可直接删除，无需替代方案。
- 🗑️ 移除 QUnit.onError() 与 QUnit.onUnhandledRejection()：改用 QUnit.onUncaughtException()。
- 🧱 移除旧版标记支持：改用 `<div id="qunit"></div>`。
- 🖥️ 运行环境变更：移除 Node.js 10-16 支持，CLI 需 Node.js 18+；移除 PhantomJS。
- 📦 分发变更：不再发布到 Bower；qunit.js 不再通过 AMD 导出 API，但应用与测试仍可用 AMD/RequireJS。
- 📚 延伸阅读：可查看“The Road to QUnit 3”和 QUnit 3.0.0 完整变更日志。

---

### [前端的大统一架构 - DEV 社区](https://dev.to/playfulprogramming/the-grand-unifying-architecture-of-frontend-bhk)

**原文标题**: [The Grand Unifying Architecture of Frontend - DEV Community](https://dev.to/playfulprogramming/the-grand-unifying-architecture-of-frontend-bhk)

前端架构长期围绕“状态归谁”反复摇摆，作者认为可统一为三种核心职责：客户端导航、服务器内容、客户端可交互性；所有框架只是在这三层之间分配不同权重。Solid 2.0 尝试用统一的异步响应式模型覆盖从 HTMX 到 SPA、LiveView、RSC、同步引擎的完整谱系。

- 🧭 历史主线：前端演进一直在服务器与客户端之间争夺状态归属，从 ASP.NET 到 HTMX/React 仍未停止。
- 🧩 三大职责：导航归浏览器/客户端，内容归服务器，affordances（本地 UI、乐观更新）归客户端。
- 🔁 统一分层：架构遵循客户端→服务器→客户端；写入通过导航/动作上行，读取由服务器单向下发，这种不对称带来可组合性。
- 📊 谱系定位：HTMX、LiveView、DataStar、Astro、Next.js RSC、React SPA+JSON、Zero 同步引擎，都是三层职责的不同配比。
- 🧭 Solid 2.0 导航：路由不拥有渲染树；编译器认领 `a[href]` 与 `form[action]`，拦截并渐进增强，无客户端组件也能参与导航。
- 📡 内容传输：`use server` 函数配合 Seroval 跨边界序列化 Promise、异步迭代器等；服务器响应式图可继续推送更新。
- 🧬 Server Components：服务器组件可流式返回并做细粒度原地更新，客户端无需携带组件代码；传输可换成 SSE/socket，变为长期 live 组件。
- 🛡️ 安全规则：服务器 live 图必须是持久状态的可重推投影，不能成为真相源；重连不依赖会话或事件回放。
- ⚡ Affordances：Solid 2.0 把异步原生接入响应式图；乐观更新是一等原语，作为覆盖层最终结算或回滚，不会超出事务。
- 💧 单次 hydration：只 hydrate 一次；服务器内容按调用地址存储，网络不能直接写 DOM，避免陈旧预加载或响应覆盖。
- 🧰 可遍历谱系：从无客户端组件的服务器组件应用，到 SPA+JSON，再到持久 `use server` 加乐观层，都能用同一套模式表达。
- 🎯 结论：浏览器负责导航与 affordances，服务器负责内容；传输和响应窗口可配置。所有框架只是网格坐标，差异在效率与人体工程，而非表达力。

---

### [未找到标题](https://www.solidjs.com/blog/solid-2-0-rc-the-big-reveal)

**原文标题**: [No title found](https://www.solidjs.com/blog/solid-2-0-rc-the-big-reveal)

未提供可总结的正文内容，因此暂时无法提取关键信息；请发送或粘贴需要总结的文章。

- 📄 当前输入为空，缺少待总结的文本内容。
- ✍️ 请补充文章或段落，我将据此生成中文总结。
- ✅ 收到内容后，我会按“概述 + 表情符号要点”的格式提炼核心信息。

---

### [](https://jobs.fidelity.com/en/technology-careers/?utm_source=javascript&utm_medium=paidsocial&utm_campaign=jobssocial&utm_content=awn-tech-nl3-s)

**原文标题**: [Technology careers at Fidelity | Fidelity Careers](https://jobs.fidelity.com/en/technology-careers/?utm_source=javascript&utm_medium=paidsocial&utm_campaign=jobssocial&utm_content=awn-tech-nl3-s)

Fidelity 技术职业页面介绍其技术团队如何以创新推动金融未来，兼具初创公司心态与财富500强基础，并列出招聘岗位、核心技能、学习支持和求职入口。

- 🚀 加入 Fidelity 技术团队，参与有影响力的创新，共同打造明日金融科技。
- 🏢 兼具初创思维与财富500强根基，持续投资创新并兑现数字未来承诺。
- 📊 强调技术人才规模、员工承担新角色或扩展职责，以及美国专利成果。
- 🎥 员工分享：全栈工程师 Monica 认为，Fidelity 最棒的是人与人之间的互动。
- 💼 技术岗位频繁更新；若无合适职位，可加入人才网络并订阅职位提醒。
- 📌 精选岗位包括 Leap 系统分析师、测试软件工程总监、Leap 软件工程师，地点涉及 Westlake, TX、Merrimack, NH、Durham, NC 等，多为现场办公。
- 🛠️ 招聘技能涵盖软件工程、全栈工程、云工程、数据可视化、人工智能与机器学习、架构、系统工程和系统分析。
- 📚 每周提供专门学习时间，可通过在线课程、职业辅导、导师影子学习等方式保持技能更新。
- 🔎 可按技能和地点搜索职位，找到适合自己的技术角色。
- 🧭 更多信息包括技术职业详情、福利、播客，以及加密货币职业与招聘领域。

---

### [](https://adventures.nodeland.dev/archive/optimizing-objects-with-null-prototypes/)

**原文标题**: [Optimizing objects with null prototypes](https://adventures.nodeland.dev/archive/optimizing-objects-with-null-prototypes/)

在 V8 中用 `{ __proto__: null }` 创建的对象会永久停留在字典模式，性能很差；作者通过改用类或 `Object.setPrototypeOf` 来创建无原型对象，使 Node 核心中的 WebStreams 吞吐量翻倍。

- 🐢 **问题根源**：任何在创建时带 `__proto__: null` 的对象字面量都会进入 V8 的字典模式，属性存在哈希表里而非隐藏类背后，字面量构建耗时约 500–1500ns（普通字面量仅约 30ns），且此后所有属性访问都是字典查找，永远不会命中快速内联缓存。
- 🔒 **无法自愈**：即使对象被大量读取（如 10 万次），它也永远不会回到快速模式；唯一的例外是当它被用作其他对象的原型时，V8 会将其优化为快速模式。
- ⚡ **三种快速替代方案**：① 让类的 prototype 指向 null 原型（适用于按实例的状态记录）；② 先创建普通字面量再用 `Object.setPrototypeOf(obj, null)` 设为 null 原型；③ 当读取的都是自有属性时，直接用普通字面量（自有属性会遮蔽 `Object.prototype`）。
- 📊 **第一轮修复（Round 16）**：将 WebStreams 中四个每流的状态记录从 null 原型字面量改为类实例，pipe-to 吞吐量提升 +105–112%，WritableStream 创建快 +204%，ReadableStream +138%，TransformStream +134%。
- 📊 **第二轮修复（Round 19）**：`writablestream.js` 中的两个模块级哨兵 `kNilRequest` 和 `kNilPendingAbortRequest` 曾是 null 原型字面量，因从未被用作原型而终生停留在字典模式；改用普通字面量后再置空原型后，pipe-to 提升 +12.3% 至 +14.9%，带转换的 pipe-through +6.8%，写入器驱动写入 +6.5% 至 +17.6%。
- 🎯 **核心结论**：null 原型对象只在热路径上创建或被频繁读取时才影响性能（包括被热路径反复读取的长生命周期共享常量）；一次性传给 `Object.defineProperty` 的描述符等无碍。不必删除所有 `__proto__: null`，只需针对每秒运行百万次的路径上的那些。
- 🧪 **可复现性**：文章附带了使用 `node --allow-natives-syntax` 和 `%HasFastProperties` 检测对象模式的完整探针脚本，可自行验证整张对照表，以及检查真实 Node 构建中哨兵对象的属性模式。
- 💡 **最大启示**：最便宜的优化有时不在于之后对对象做什么，而在于你如何创建它。

---

### [](https://flaviocopes.com/node-builtins/)

**原文标题**: [Node.js built-ins that replaced npm packages](https://flaviocopes.com/node-builtins/)

Node.js 内置模块正在逐步取代常见 npm 包，文章详细列举了 12 个替代方案及其在 Node 24 中的稳定性状态和使用局限

- 📦 **node:sqlite 取代 better-sqlite3**：Node 22.5 起内置 SQLite 驱动，同步 API，无需编译原生插件；但缺少 `db.transaction()` 自动事务封装，需手动写 BEGIN/COMMIT/ROLLBACK
- 🧪 **node:test + node:assert 取代 Jest 和 Mocha**：零配置测试运行器，`node --test` 即可；但覆盖率、模块 Mock 和监听模式仍为实验性，重度 Mock 场景建议保留 Jest
- 🌐 **全局 fetch() 取代 axios 和 node-fetch**：基于 undici，浏览器同款 API；但不会因 404/500 抛错，无拦截器和自动重试，代理需加 `--use-env-proxy` 标志
- 👀 **node --watch 取代 nodemon**：内置文件监听重启，`--watch-preserve-output` 可保留终端输出；但默认只监听导入的模块，`--watch-path` 仅支持 macOS 和 Windows
- 🔐 **--env-file 和 process.loadEnvFile() 取代 dotenv**：原生读取 .env 文件，支持引号、多行和注释；但不支持变量展开，--env-file 遇文件缺失会报错
- ⚙️ **util.parseArgs() 取代 yargs、commander 和 minimist**：轻量命令行参数解析；但仅支持 string 和 boolean 类型，无 --help 生成和子命令，正式 CLI 仍推荐 commander
- 🎨 **util.styleText() 取代 chalk**：内置终端着色，尊重 NO_COLOR 和 FORCE_COLOR；但输出非终端时自动去除颜色码，无链式 API
- 📂 **fs.glob() 取代 glob**：Node 22 引入、24 稳定，支持 brace 展开和 exclude 选项；但 promise 版返回异步迭代器而非数组，选项远少于 glob 包
- 🔌 **WebSocket 全局取代客户端 ws**：浏览器同款 WebSocket 类，事件 API 一致；但仅限客户端，服务端仍需安装 ws
- 🆔 **crypto.randomUUID() 取代 uuid**：无需导入，直接调用生成 v4 UUID；但仅支持 v4，缺少 v7 时间有序 ID 及 validate/parse 等工具函数
- 🗑️ **fs.rm() 和 fs.mkdir() recursive 取代 rimraf 和 mkdirp**：递归创建和删除目录，`force: true` 相当于 `rm -rf`；但 rm() 只接受单个路径，不支持 glob 模式
- 📘 **TypeScript 类型剥离取代 ts-node 和 tsx**：Node 24.12 稳定，直接运行 .ts 文件无需安装配置；但不做类型检查，enum、namespace 等需要生成 JS 的语法会报错，.tsx 不支持

**核心要点**：每个内置模块只覆盖常见场景，旧包在特定场景下仍有价值。移除依赖前需确认部署环境的 Node 版本，并在 engines 字段中固定版本。

---

### [](https://shukla.io/blog/2026-09/pun.html)

**原文标题**: [The Greatest Pun: JavaScript’s ${{ }} tagged template
literal](https://shukla.io/blog/2026-09/pun.html)

文章从莎士比亚的语言双关出发，延伸到 JavaScript 的标签模板字面量，展示自然语言与编程语言共享“语法”时，同一字符串如何产生两种解析。作者认为自己发现的最伟大双关是 `${{ url }}`：读者眼中像 `{{ url }}` 模板，JavaScript 却将其解析为对象简写的求值结果，使 `prompt` 标签函数能为 Helicone 生成结构化提示词标注。

- 🎭 莎士比亚擅长双关，如《第十二夜》中 “Better a witty fool than a foolish wit.”，通过 fool/foolish、witty/wit 的词性翻转改变含义。
- 🕯️ 双关也能借上下文超越语法，如《奥赛罗》中 “Put out the light, and then put out the light.”，第一句指熄灭蜡烛，第二句隐喻杀死苔丝狄蒙娜。
- 📖 牛津词典将双关定义为利用一词多义、联想或同音异义制造幽默效果的文字游戏；作者则强调幽默因人而异。
- 💻 作者认为自然语言和编程语言共有“语法”，于是把双关延伸到代码；JavaScript 的 tagged template literal 支持强大的字符串处理。
- 🧹 标签函数如 `dedent` 会接收模板字面量的文本片段和 `${...}` 求值结果，因此能去除多余缩进或任意处理内容。
- 🧩 多数模板语言采用“文本加变量洞”的形式，`{{ }}` 常见于 Mustache、Handlebars、Jinja2、Django、Liquid、Angular 和 Vue。
- ✨ 作者定义 `prompt` 标签函数，让它看起来接受 `{{ }}` 模板；示例中的 `${{ url }}`、`${{ notes }}`、`${{ time }}` 会转成 Helicone 可分析的 `<prompt id="...">` 标注。
- 🧠 巧妙之处在于 JavaScript 的巧合：`${...}` 会求值，而 `{ url }` 等价于 `{ url: url }`，所以 `${{ url }}` 在 JS 中是 `${ {url} }`，在读者眼中却像 `{{ url }}`。
- 🤝 作者与 Helicone 的 Justin 于 2024 年合作，将这个内部想法推进到 SDK 官方支持，双方均有 PR；作者自认这个双关好笑且值得骄傲。
- 🔁 文章核心可概括为 “A pun is one string with two parses.”：同一字符串可被自然语言和编程语言分别解析，形成跨语法的双关。

---

### [通过发布更多 CSS 来提升网站性能 - GitHub 博客](https://github.blog/engineering/architecture-optimization/improving-site-performance-by-shipping-more-css/)

**原文标题**: [Improving site performance by shipping more CSS - The GitHub Blog](https://github.blog/engineering/architecture-optimization/improving-site-performance-by-shipping-more-css/)

overview summary
- 🧭 GitHub 将整个平台从 CSS-in-JS 迁移到 CSS Modules，以提升性能、可维护性和规模化样式交付能力。
- 🧱 Primer 设计系统是迁移起点；2023 年组件数量激增，导致首屏加载变慢、SSR 性能下降、样式更新失控。
- 🎯 选择 CSS Modules：支持原生 CSS、类名默认局部化、无客户端或服务端运行时，样式随 HTML 作为 CSS 样式表发送。
- 🚩 采用渐进迁移：新增 CSS Modules 文件、用 feature flag 切换新旧样式、视觉回归验证，并逐步向团队、员工和所有用户发布。
- 📉 到 2024 年 12 月，Primer 全部组件完成迁移；SSR 时间减少 55%，组件初始化时间减少 25%。
- 🔁 随后 GitHub 主站继续迁移，最大障碍是 `sx` prop：类型支持好，但运行时成本高且难以扩展。
- 🧩 为保持兼容，创建 `@primer/styled-react` 包装组件，让仍使用 `sx` 的代码继续消费新组件。
- 📦 按包迁移：将 `sx` 转为 CSS Modules，替换 `@primer/styled-react` 导入为 `@primer/react`，预生产测试后部署。
- 🤖 2025 年 4 月开始约 7,760 个 `sx`；8 名工程师 6 个月迁移 6,419 个，部分页面 SSR 提升 1%–22%。
- 🚀 2026 年 4 月借助 Copilot coding agents，2 名工程师 3 周内将剩余 895 个 `sx` 降为 0。
- 🎨 之后还需解耦主题：GitHub 有 7 套主题及高对比模式，原本依赖 `styled-components` 的 JavaScript 工具与用法。
- ✅ 到 2026 年 6 月，GitHub 100% 使用 CSS Modules，移除 `sx`、`styled-components`、`styled-system`，并在不破坏 GitHub 的情况下完成性能提升。

---

### [](https://github.com/ai/size-limit)

**原文标题**: [GitHub - ai/size-limit: Calculate the real cost to run your JS app or lib to keep good performance. Show error in pull request if the cost exceeds the limit. · GitHub](https://github.com/ai/size-limit)

Size Limit 是用于 JavaScript 的性能预算工具，在 CI 中检查每次提交，计算 JS 对最终用户的真实成本，并在超出限制时报错。它支持 ES 模块和 tree-shaking，提供 CLI、插件与预设，可检查文件大小或浏览器下载/执行时间，并能集成 GitHub Actions 在 PR 中评论或拒绝超限变更。

- 📏 在 CI 中检查每次提交，计算 JS 真实成本，超出限制时抛错。
- 🌳 支持 ES 模块和 tree-shaking，可测试 tree-shaking 后的体积。
- 🔌 可接入 GitHub Actions、Circle CI 等 CI 系统，防止 PR 引入庞大依赖。
- 🧩 模块化设计，适合大型 JS 应用和小型 npm 库等不同使用场景。
- ⏱️ 可计算浏览器下载和执行时间，比字节大小更准确，并可配置网络速度、延迟等。
- 📦 计算范围包含所有依赖和 polyfills。
- 💬 配合 GitHub Action，会在 PR 讨论中评论 bundle 大小变化。
- 🔍 使用 `--why` 和 Statoscope 分析体积来源，展示内部依赖的真实成本。
- 🛠️ 由 Evil Martians 构建，面向开发者工具、AI 和网络安全等初创项目。
- 👥 使用者包括 MobX、Material-UI、Ant Design、Autoprefixer、PostCSS、Browserslist、EmojiMart、nanoid、React Focus Lock、Logux，部分项目体积减少 20%–90%。
- ⚙️ 组成包括 CLI 工具、3 个插件（file、webpack、time）和 3 个预设（app、big-lib、small-lib）。
- 🔧 CLI 从 `package.json` 查找插件并加载配置；webpack 插件打包并比较 bundle 大小；time 插件用 headless Chrome 和低端 Android 节流测量编译与执行时间。
- 📱 适用场景：JS 应用、时间限制、大库（>10 kB）、小库（<10 kB）。
- 🚦 提供 GitHub Action，可根据 Size Limit 输出评论并拒绝 PR。
- 🧾 配置支持 `package.json`、`.size-limit.json`、`.size-limit.js/cjs/ts`，包含 `path`、`import`、`limit`、`name`、`message`、`entry`、`gzip`、`brotli`、`ignore` 等选项。
- 🧩 官方插件含 file、webpack、webpack-why、webpack-css、esbuild、esbuild-why、rolldown、rolldown-why、time；预设含 app、big-lib、small-lib；支持第三方 `size-limit-*` 插件。
- 🧪 CLI 支持 `--limit`、`--config`、`--ignore-missing`；`--why` 可生成分析报告；还提供 JS API。

---

### [](https://www.tigerdata.com/go/trial?utm_source=content-syndication&utm_medium=referral&utm_campaign=javascript-weekly-newsletter)

**原文标题**: [Postgres for time-series workloads at any scale. | Tiger Data](https://www.tigerdata.com/go/trial?utm_source=content-syndication&utm_medium=referral&utm_campaign=javascript-weekly-newsletter)

Tiger Data 提供面向时间序列工作负载的 Postgres 服务，支持任意规模；单个 Tiger Cloud 服务可承载每天 3 万亿指标、3 PB 数据与 1 千万亿数据点，并提供新用户 $1000 信用额度及企业级能力。

- 📨 提供 Contact us 和 get started 入口，便于咨询与快速开始。
- 🐘 面向任意规模的时间序列工作负载，基于 Postgres。
- 📈 单个 Tiger Cloud 服务真实规模：每天 3 万亿指标、3 PB 数据、1 千万亿数据点。
- 💳 注册可获 $1000 信用额度，30 天有效，无需信用卡，仅限新账户。
- 🏭 受数千家 IoT 公司信任。
- ⚡ 轻松扩展：读写分离，最多 10 节点副本集，分层 SSD/S3 实现低成本、近乎无限存储。
- 💸 不为空闲容量付费：计算与存储分离，可独立扩展，降低成本并优化性能。
- 🛡️ 高可用：多可用区集群、自动故障转移、时间点恢复和跨区域备份。
- 🔐 企业级合规：SOC 2、HIPAA、GDPR，始终加密，支持 SSO、RBAC 和审计日志。
- 🔍 深度可观测性：查询下钻与仪表板，指标可发送至 CloudWatch、Datadog、Prometheus。
- 🚀 快速启动：几分钟内配置数据库，可用 SQL、CLI、Terraform、Cursor 或 Claude Code 管理。
- 🔌 集成：支持首选云提供商和更广泛的 Postgres 生态。
- 🏢 企业就绪：合同 SLA、区域数据隔离和企业级合规认证。
- ☎️ 24/7 支持：全球 Postgres 专家，保证企业响应时间。
- 📄 页脚包含隐私偏好、法律、隐私、站点地图；2026 Timescale, Inc. d/b/a Tiger Data 版权所有。

---

### [EmDash 1.0：稳定的内容管理系统，配备安全插件注册表 | Cloud](https://blog.cloudflare.com/emdash-cms-plugin-registry/)

**原文标题**: [EmDash 1.0: the stable CMS with a secure plugin registry | Cloudflare Blog](https://blog.cloudflare.com/emdash-cms-plugin-registry/)

EmDash 1.0 已正式发布：它是一个稳定、免费、开源的 Astro CMS，最初被误以为是愚人节玩笑；它将 Astro 开发、EmDash 管理后台和 AI 代理（API/CLI/MCP）结合，面向真实生产站点、代理机构和托管平台。

- 🎉 EmDash 1.0 带来生产验证的编辑、媒体、本地化、迁移和部署工作流，为不依赖 WordPress 的建站提供稳定选择。
- 🧱 开发者用 Astro 构建，编辑在 EmDash 后台管理内容，代理可通过 API、CLI 或内置 MCP 服务器操作。
- 🔐 去中心化插件注册表基于 AT Protocol，发布者用 Atmosphere 身份保留包和发布历史，不把身份与分发交给单一市场。
- ✅ 注册表通过签名 Merkle Search Trees 和包含证明验证发布记录，并检查校验和、包名、版本、权限和构建来源。
- 🧪 插件采用沙箱模型：每个插件在隔离运行时中仅获得其声明并经管理员批准的能力，默认无法访问站点内容、媒体、用户、密钥、环境、文件系统或网络。
- 🆚 与 WordPress 插件同 PHP 进程运行不同，EmDash 在 Cloudflare 上通过 Worker Loader 运行为 Dynamic Worker，在 Node.js 上通过独立 workerd 进程隔离运行。
- 🌍 项目完全免费开源，采用 MIT 许可证；已有 175+ 贡献者、1,800+ 提交，并翻译成 25 种语言。
- 👏 实习生 Noah Pham 成为 EmDash 第二维护者，贡献 80+ 变更，负责媒体库、内容编辑器和后台等核心部分。
- 🚀 Cloudflare Blog 已迁移到 EmDash，支撑每周数百万页面浏览、最高 5,000 RPS 合法流量和 DDoS 攻击压力。
- ⚡ 迁移催生了 KV 对象缓存、Hyperdrive 数据库适配器和 Workers Cache 兼容等功能，并已向所有用户开放。
- 🛍️ 生态正在成长：Lexington Themes 提供 44 个 Astro 主题，Urumi 开发首个电商插件，Empress 构建多品牌多站点平台。
- 🏗️ 平台可用 Workers for Platforms 将每个客户站点作为 Worker 运行，并用 EmDash 作为内容层，支持自有后台、API/CLI 或代理界面。
- 🤖 EmDash Build alpha 开源发布：AI 建站器从提示生成 EmDash 站点、内容模型和页面，使用 Cloudflare Sandbox、Agents SDK 和 Artifacts 验证与追踪更改。
- 🧭 开始使用：`npm create emdash@latest`，或通过 Cloudflare Dashboard；可加入 800+ 人的 Discord 社区参与代码、翻译、文档、测试、设计等。
- 📚 插件开发有分步文档，注册表相关服务（聚合器、标签器、Astro 实时内容加载器）也已开源。

---

### [](https://github.com/dolanmiu/docx/releases/tag/9.8.0)

**原文标题**: [Release 9.8.0 · dolanmiu/docx · GitHub](https://github.com/dolanmiu/docx/releases/tag/9.8.0)

docx 9.8.0 是一次重大版本更新，新增原生 Word 图表、形状、水印和更丰富的数学功能，并为各功能提供独立入口以按需打包；同时引入主题支持、增强 patchDocument，并用 Open XML SDK 校验所有示例文档，修复多项问题并迎来五位新贡献者。

- 🚀 **版本发布**：dolanmiu/docx 发布 9.8.0，包含 33 个提交；仓库约 5.9k Star、613 Fork、118 Issues。
- 📊 **原生图表**：支持 Word 原生图表而非图片，可在 Word 中通过“编辑数据”用 Excel 修改；涵盖柱状、条形、折线、面积、饼图、圆环、复合饼图、雷达、散点、气泡、股价和组合图等。
- 🧩 **图表补丁**：图表可用于模板；patchDocument 可用 ChartRun 替换占位符，ChartDataPatch 可为已样式化图表更新数据并保留外观。
- 🟦 **形状功能**：支持 Word 预设形状、SVG 自定义路径、分组、连接线和 ShapeCanvasRun 自动布局，适合流程图、组织图和泳道图。
- ➗ **数学增强**：新增矩阵、cases、带编号对齐公式、任意字符括号；原有 docx 数学导入继续可用。
- 💧 **水印**：支持文字或图片水印置于每页背景，Word 的“设计 > 水印”菜单可识别。
- 🎨 **主题系统**：每个文档都有主题，可设置颜色和字体；文本、下划线、边框、底纹、形状和页面背景均可使用主题色，并随 Word 主题切换联动变化。
- 🩹 **模板主题**：patchDocument 可从模板自身主题解析主题色。
- ✅ **CI 校验**：所有示例文档均通过 Open XML SDK 验证器检查，并修复发现的问题。
- 🙌 **新贡献者**：@slmnsh 增加图片裁剪，@theunal 实现水印，@holm 增加 ImageRun run 属性，@omartuhintvs 和 @fushanbobfan 修复表格与 patcher。
- 🏷️ **按需入口**：charts、shapes、watermarks、math 各有入口，如 docx/charts、docx/shapes 等，打包时只包含导入模块。
- 🔧 **其他修复**：包括书签 ID 分配、表格百分比宽度、样式定义隐式 ListParagraph、重复占位符倒序 patch、textbox 图片写入、仅在文档有批注时写入 comments part 等。

---

### [](https://docx.js.org/)

**原文标题**: [docx - Generate .docx documents with JavaScript](https://docx.js.org/)

暂无可总结的内容，因为您未提供需要摘要的文本。
- 📄 请粘贴文章或文本内容。
- 🧾 收到后我会生成中文概述和要点列表。
- ✨ 每条要点将使用“-”符号，并配一个合适的表情符号。

---

### [GitHub -](https://github.com/katspaugh/wavesurfer.js)

**原文标题**: [GitHub - katspaugh/wavesurfer.js: Audio waveform player · GitHub](https://github.com/katspaugh/wavesurfer.js)

wavesurfer.js 是一个由 katspaugh 维护的开源 Web 音频波形渲染与播放库，采用 BSD-3-Clause 许可证，当前约 10.4k Star、1.8k Fork、2,153 次提交；它基于现代 Web 技术提供交互式音频体验，并附带插件、响应式 API、Shadow DOM 样式能力以及开发测试指引。

- 🎧 核心功能：在 Web 应用中渲染交互式音频波形并播放音频。
- ⭐ 仓库概况：公开仓库，10.4k stars、1.8k forks、12 issues、1 pull request、2,153 commits，BSD-3-Clause 许可。
- 📦 快速开始：支持 `npm install --save wavesurfer.js`，或通过 unpkg 的 UMD script 标签引入全局 `WaveSurfer`。
- 🛠️ 基本用法：调用 `WaveSurfer.create({ container, waveColor, progressColor, url })` 创建实例。
- 🧩 官方插件：Regions、Timeline、Minimap、Envelope、Record、Spectrogram、Hover，可添加区域、时间轴、缩略图、包络、录音、频谱和悬停功能。
- 🪟 长音频频谱：Spectrogram 支持 `rendering: 'windowed'`，仅渲染可见时间范围并淘汰屏外片段，替代已弃用的 WindowedSpectrogramPlugin。
- ⚡ 响应式 API：`getState()` 返回只读 Signal，覆盖 `currentTime`、`isPlaying`、`volume`、`muted`、`loadPhase`、`scrollPosition` 等；`getRenderer().getVisibleRange()` 提供可见范围。
- 🔌 插件开发：可用 `WaveSurfer.definePlugin(name, (ctx, options) => api)` 替代 BasePlugin 子类化，`ctx.scope` 资源在 `destroy()` 时自动清理。
- 🎨 CSS 样式：v7 渲染在 Shadow DOM 中，可用 `::part()` 选择器定制 cursor、region 等元素。
- ❓ FAQ：CORS 需音频源允许跨域；大文件建议预解码 peaks；流媒体需预解码 peaks 和 duration；VBR 可能波形不匹配，可转 CBR 或使用 Web Audio shim。
- 🔊 音频处理边界：主要作为播放器和波形可视化，不封装 Web Audio 效果，但可导出 audio element 接入 Web Audio 图。
- 🧪 开发测试：`yarn` 安装依赖，`yarn start` 在 localhost:9090 实时开发；测试基于 Cypress，先 `yarn build` 再 `yarn cypress`。
- 💬 反馈支持：问题或建议可发布到 Discussion forum，官方欢迎贡献与反馈。

---

### [GitHub - sindresorhus/pretty-bytes：将字节转换为人类可读的字符串：1337 → 1.34 kB · GitHub](https://github.com/sindresorhus/pretty-bytes)

**原文标题**: [GitHub - sindresorhus/pretty-bytes: Convert bytes to a human readable string: 1337 → 1.34 kB · GitHub](https://github.com/sindresorhus/pretty-bytes)

pretty-bytes 是一个由 sindresorhus 维护的 JavaScript 包，用于把字节数转换成人类可读的字符串，例如 1337 → 1.34 kB，适合展示文件大小、进度条和表格等场景，采用 base-10 单位（kB 而非 KiB）。

- 📦 仓库概况：作者为 sindresorhus，MIT 许可证，约 1.3k stars、94 forks、97 commits，当前 Issues 与 Pull Requests 均为 0。
- ⚙️ 安装方式：使用 `npm install pretty-bytes` 安装。
- 🚀 基本用法：`import prettyBytes from 'pretty-bytes'; prettyBytes(1337); //=> '1.34 kB'`。
- 🔢 数字类型：接受 `number | bigint`；超大或极小值有特殊输出规则，普通数字约保留 16 位有效数字，约 `1e17` 字节以上尾数可能不精确。
- 🧮 舍入规则：使用 `Number#toPrecision`，在精确中点时方向取决于浮点数存储方式，例如 `1005` 舍入为 `1 kB`，`1125` 舍入为 `1.13 kB`。
- 🧩 选项 `bits`：设为 `true` 时以 bit 而非 byte 格式化，例如 `1337` → `1.34 kbit`。
- ➕ 选项 `signed`：设为 `true` 时正数显示加号，零差异时前置空格以便对齐，例如 `+42 B`。
- 💾 选项 `binary`：使用二进制前缀，例如 `1024` → `1 KiB`，适合内存量展示，但不建议用于文件大小。
- 🌍 选项 `locale`：支持系统或 BCP 47 语言标签，例如德语 `de` → `1,34 kB`；仅本地化数字和小数分隔符，单位不本地化。
- 🎛️ 小数位选项：`minimumFractionDigits` 与 `maximumFractionDigits` 可控制小数位，需为 0 到 100 的整数；指定时会截断而非四舍五入。
- 📏 格式选项：`space` 默认 true 控制数字与单位间空格；`nonBreakingSpace` 使用不换行空格；`fixedWidth` 可右对齐填充固定宽度，适合表格和进度条。
- ❓ FAQ：使用 `kB` 而不是 `KB`，因为 `k` 是标准 SI 千前缀。
- 🔗 相关项目：包含 `pretty-bytes-cli` 命令行工具，以及把毫秒转为可读字符串的 `pretty-ms`。

---

### [GitHub - postalsys/postal-mime：适用于浏览器和无服务器环境的电子邮件解析](https://github.com/postalsys/postal-mime)

**原文标题**: [GitHub - postalsys/postal-mime: Email parser for browser and serverless environments · GitHub](https://github.com/postalsys/postal-mime)

postal-mime 是一个零依赖、TypeScript 编写的 RFC822 邮件解析库，适用于浏览器、Node.js、Web Workers 和无服务器环境；它可将原始邮件解析为包含头部、收件人、正文、附件等信息的结构化 Email 对象，并提供类型声明、安全限制和工具函数。

- 📧 postal-mime 是用于 Node.js、浏览器、Web Workers 和 serverless（如 Cloudflare Email Workers）的邮件解析库，接收 RFC822 原始邮件并输出结构化对象。
- 🏢 由 EmailEngine 团队开发；EmailEngine 是自托管邮件网关，提供 IMAP/SMTP REST API，并通过 webhooks 通知账户变化。
- 🧩 主要特性：浏览器与 Node.js 兼容、TypeScript 编写、ESM/CommonJS 双包、零依赖、符合 RFC 2822/5322、处理复杂 MIME 与附件、内置安全限制。
- 📦 安装：`npm install postal-mime`；需要 Node.js 20+，或现代浏览器/Deno/Bun/Cloudflare Workers，并支持 TextDecoder、Blob、ReadableStream。
- 🔄 v4 变化：TypeScript 重写；按名称导入和解析输出不变；浏览器深导入路径改为 `dist/esm/postal-mime.js`；Node.js 20+；Attachment.disposition、流输入、addressParser `_depth` 和 CommonJS 类型有调整。
- 🌐 使用方式：浏览器可用打包器或直接导入 ESM；Node.js 直接 import；CommonJS 用 `require()`；Cloudflare Email Workers 解析 `message.raw`。
- 🧠 TypeScript 支持：源码生成类型，通过 exports 映射解析，无需 @types；提供 Email、Address、Mailbox、AddressGroup、Header、HeaderLine、Attachment、PostalMimeOptions、RawEmail 等类型。
- ⚙️ 核心 API：`PostalMime.parse(email, options) -> Promise<Email>`；email 可为 string、ArrayBuffer、Uint8Array、ArrayBufferView、Blob 或 ReadableStream。
- 🧾 解析选项：`rfc822Attachments`、`forceRfc822Attachments`、`attachmentEncoding`（base64/utf8/arraybuffer）、`maxNestingDepth`、`maxHeadersSize`、`maxRfc822NestingDepth`。
- 🛡️ 安全限制：防止深层嵌套、超大头部和失控嵌套；限制只限深度不限广度，不可信输入仍应先按大小限制。
- ⚠️ 扫描提醒：不要忽略附件 `rfc822DepthExceeded`；超出限制的嵌套内容可能藏在原始字节中，需重新解析附件 content 并限制次数。
- 📨 返回 Email：headers/headerLines、from/sender、to/cc/bcc/replyTo、subject、messageId/inReplyTo/references、date、html、text、attachments。
- 📎 附件字段：filename、mimeType、disposition、related、contentId、description、method、rfc822DepthExceeded、content、encoding；日历部分规范化为 UTF-8/LF。
- 🧰 工具函数：`addressParser()` 解析地址并支持 flatten；`decodeWords()` 解码 MIME encoded-words。
- 🏗️ 开发构建：源码在 `src/` TypeScript；构建生成 `dist/esm/` 与 `dist/cjs/` 及类型声明、source maps；提供 test、lint、format 脚本。
- 📜 许可证为 MIT No Attribution；仓库现有 550 stars、45 forks、226 commits、0 issues 和 0 pull requests。

---

### [首页 | Typia](https://typia.io/)

**原文标题**: [Home | Typia](https://typia.io/)

typia 是一个能将纯 TypeScript 类型转化为极速运行时验证器、JSON 序列化器和 LLM 模式（schema）的库，实现零 schema 开销。

- ⚡ **AOT 编译魔法**：编译时分析 TypeScript 类型的 AST 并生成专用优化验证代码，无需运行时解析 schema
- 🚀 **超快验证**：`typia.validate<T>()` 比 class-validator 快 20,000 倍，支持复杂联合类型、递归结构和详细错误报告
- 📦 **JSON 序列化**：`typia.json.stringify<T>()` 比 class-transformer 快 200 倍，还支持生成 OpenAPI 所需的 JSON schema
- 🤖 **AI 函数调用集成**：`typia.llm.application<App>()` 将 LLM 准确率从 6.75% 提升至 100%（qwen3-coder-next 测试），提供 schema 生成、宽松 JSON 解析、类型强制转换和验证反馈
- 🔧 **Protocol Buffers**：`typia.protobuf.encode<T>()` 是 TypeScript 中唯一支持完整 Protobuf 规范的库，无需 .proto 文件
- 🎲 **随机生成器**：`typia.random<T>()` 可生成完美符合 TypeScript 类型约束的模拟数据
- ✨ **AOT 优势**：告别独立 schema 对象、运行时开销和类型漂移，纯 TypeScript 类型即唯一真实来源
- 🧩 **完整类型支持**：全面支持联合、交叉、递归、模板字面量和标签类型

---

### [](https://expo.dev/ai?utm_campaign=agentic-development&utm_source=React%20Status&utm_medium=newsletter&utm_term=Agentic%20Development&utm_content=expo.dev/ai)

**原文标题**: [AI integration hub — Expo](https://expo.dev/ai?utm_campaign=agentic-development&utm_source=React%20Status&utm_medium=newsletter&utm_term=Agentic%20Development&utm_content=expo.dev/ai)

Expo 正将自己定位为移动端 AI 基础设施：AI 提高开发下限，Expo 提高交付上限；让 Claude、Codex、Cursor 等更会写移动代码，同时由 Expo 完成 AI 难以独立完成的部分——构建、提交、更新与监控。

- 🤖 **Expo MCP**：让 AI 代理真正操作项目，可启动构建、运行工作流、检查提交、回复商店评论；已进入 Anthropic MCP 目录，支持免费计划，并可在 Claude、Codex、Cursor、VS Code 甚至手机上使用。
- ☁️ **Simulators 早期访问**：按需启动安全的云端模拟器，代理可安装构建、驱动应用、验证结果，并把会话录制发到 PR 作为证明，支持并行运行。
- 🧩 **Expo Skills**：由 Expo 工程师构建和维护，帮助开发者打造现代、美观、生产级移动应用。
- 📱 **技能覆盖广泛**：包括原生 UI、数据获取、EAS Hosting、开发客户端、Tailwind、DOM 组件、工作流、应用商店提交、SDK 升级、Observe、模拟器、Brownfield 集成和设计系统等。
- 🔌 **Claude Code Connector**：把 AI 代理编程直接带入 React Native 工作流，可通过自然语言在 IDE 中实时发布、调试和迭代 Expo 应用。
- 🚀 **Expo Launch Beta**：无需配置或前置知识，几分钟内把应用发布到应用商店。
- 🛠️ **EAS 服务体系**：涵盖 Workflows、Build、Submit、Update、Hosting、Observe 等，支持从构建到发布、更新和监控的完整流程。
- 💬 **开发者反馈积极**：用户用 Claude Code、Cursor 与 Expo 快速升级 SDK、构建个人应用、迁移部署，有用户称从未做过移动应用也能在数小时内完成。
- 🎥 **学习资源**：视频介绍 2026 年用 AI 构建真实移动应用的三大核心工具：Skills、MCP 和 Planning。
- ✅ **行动入口**：鼓励开发者“Start building with AI”并设置自己的代理，AI 工具已能直接对接 Expo 生态。

---

### [](https://fingerprint.com/products/ai-agent-detection/?utm_source=JSWeekly09292026)

**原文标题**: [Detect AI Agents with 100% Accuracy | Fingerprint](https://fingerprint.com/products/ai-agent-detection/?utm_source=JSWeekly09292026)

该方案超越传统机器人检测，专注于识别和区分 AI 智能体与恶意自动化流量，通过加密签名验证可信 AI 代理，并结合智能信号实现更智能的流量处理与欺诈防御。

- 🤖 不只检测机器人，还要识别 AI agents，并区分网站上的自动化流量类型。
- 🔐 通过签名代理生态，以 100% 准确率检测已授权的 AI agents。
- ✅ 每个 AI agent 由其提供商进行加密签名，提供可靠、明确且防篡改的身份信号。
- ⚙️ 可按 Allow、Enrich、Throttle、Block 精细处理不同 agentic traffic，同时阻止欺诈、抓取和滥用。
- 🛡️ 区分可信代理与恶意机器人，防止身份冒充和 AI 驱动的欺诈。
- 📈 支持安全扩展自动化项目，让可信 AI agents 执行数据检索和多步骤工作流。
- 🚫 防御 AI 欺诈，缓解虚假账户创建、自动提交、刷量、促销滥用等威胁。
- 🕵️ 检测并威慑高级机器人攻击，识别可疑威胁模式、活动和未授权访问。
- 🧰 提供开发者工具：AI Agent 检测、反检测浏览器检测、住宅代理检测、虚拟机检测、高活跃设备检测。
- 💬 Fingerprint MCP Server 可连接 ChatGPT 或 Claude，用自然语言分析流量、发现模式并调查可疑自动化活动。
- 📊 客户案例：ClickValue 借助该方案识别 AI agent 流量并接入 GA4，获得原本容易遗漏的流量可见性。
- 🚀 可在不到 10 分钟内向工作区添加 AI Agent Detection，支持自助、企业方案及联系销售。

---

### [调查问卷与](https://surveyjs.io/?utm_source=jsweekly&utm_medium=email)

**原文标题**: [Survey and Form Management Software - SurveyJS](https://surveyjs.io/?utm_source=jsweekly&utm_medium=email)

SurveyJS 是一套用于客户端调查与表单管理的 JavaScript 库，可让企业将动态表单、拖拽式表单构建、数据看板和 PDF 导出直接集成到自己的 Web 应用中，从而跳过数月定制开发，并通过自托管实现完整的数据所有权与合规控制。

- 🧱 核心目标：在应用内构建调查和表单，减少自定义开发，确保数据完全自有。
- 📝 Form Library：MIT 许可的 UI 组件，解析 SurveyJS JSON 并即时渲染交互式动态表单，用于收集响应并发送到自有数据库。
- 🛠️ Survey Creator：白标拖拽式表单构建器，自动生成描述结构、布局、样式和行为的 JSON schema，可深度定制以匹配应用设计。
- 📊 Dashboard：读取 JSON schema，识别数据类型，用交互式图表和表格展示调查结果，并支持表格视图、分页和筛选。
- 📄 PDF Generator：根据表单 JSON 将 Web 表单渲染为可编辑或预填 PDF，便于导出、打印和分发。
- 🔗 后端集成：可与任意后端技术栈配合，连接自有 REST API，并自动化客户端表单与存储层之间的数据传输。
- 🧬 JSON 驱动：每个表单由 JSON schema 定义结构、问题、逻辑和布局，可由后端按用户角色、流程状态或外部数据动态生成和修改。
- 🔐 数据所有权：客户端表单管理，不将数据存储或传输到外部服务；存储位置、加密方式和访问权限均由自己决定。
- ✅ 合规支持：有助于满足 GDPR、HIPAA 等法规及内部安全标准，相比传统 SaaS 更透明、可审计。
- 📦 前端框架：提供 React、Angular、Vue3 和原生 JavaScript 的 npm 包，可直接集成到现有代码库。
- 🏢 行业场景：适用于保险、医疗、市场研究、教育、人力资源、电商、客户体验、非营利、银行等领域。
- 🧾 许可模式：Survey Creator、PDF Generator、Dashboard 等采用一次性开发者许可证；维护订阅首年包含，之后可续订。
- ♾️ 使用限制：不限制管理员、受访者、表单数量、月提交量、文件上传和功能使用；数据存于自有数据库。
- 🖥️ 职责边界：SurveyJS 只专注前端 UI，不提供后端、数据存储和用户管理；审批流等逻辑需在自己的服务器实现。
- 👨💻 许可证管理：许可证可分配给团队成员或外包开发者，获得开发者状态和帮助台权限；密钥可在账户 License Manager 查看。
- ⭐ 用户反馈：用户普遍称赞其灵活性、易用性、复杂条件逻辑、前端框架支持和响应迅速的技术支持。
- 🚀 上手方式：可查看 All-in-One Demo、产品文档、实时演示、定价计划并立即开始。

---

### [](https://dittytoy.net/ditty/2dd99fc839)

**原文标题**: [A-ha Take On Me by espeset | Dittytoy](https://dittytoy.net/ditty/2dd99fc839)

这是 a-ha《Take On Me》的 Dittytoy 音乐代码移植：作者将 Shadertoy 声音着色器版重制为浏览器可运行、可分享和导出的完整合成歌曲，并以 CC BY-NC-SA 4.0 授权。

- 🎶 项目内容是 a-ha《Take On Me》的 Shadertoy 版本 Dittytoy 移植。
- 👤 由 espeset（Tonny Espeset）创建，标注日期为 2026/09/25。
- ⚖️ 采用 CC BY-NC-SA 4.0，允许使用乐器与歌曲，但需保留署名和原链接。
- 🎚️ 代码以 60 BPM 运行，并为各乐器设置独立混音音量。
- 🥁 自定义合成器包含鼓、DX7 贝斯、钟声、orbit pluck、Juno、pad、FM 键盘等。
- 🗜️ 乐谱用 LZ 压缩数据存储，处理 tick 转秒、音符门限、间隙与淡出。
- 🎤 人声由 5 ms 记录驱动 72 个谐波和 12 个噪声带，含主唱、伴唱、合唱与修复路由。
- 🎹 编曲包含 Juno 铃/低拨弦、多种 pad、弦乐合奏、bridge strings/plucks、伴唱八度。
- 🖥️ 页面支持编译播放、Remix、分享、iframe 嵌入和 MP3 导出设置。
- 💬 页面提供登录评论、互动计数，并保留代码中的 credits 与 Shadertoy 链接。

---

### [迪蒂玩具](https://dittytoy.net/)

**原文标题**: [Dittytoy](https://dittytoy.net/)

这是一个基于代码的网页音乐创作平台，用户可以在浏览器中编写、编译并聆听音乐，主打零配置、极简语法、开源学习与分享，并展示社区的最新、精选和热门作品。

- 🎹 核心理念是“写代码、编译、聆听”，打造面向网页的代码驱动音乐游乐场。
- 🌐 零配置：完全在浏览器中通过 Web Audio 运行，无需安装、无依赖，打开即可开始编程。
- 🎛️ 表达性语法：受 Sonic Pi 启发的极简 API，可用简单循环构建合成器、滤波器和复节奏。
- 🔗 学习与分享：每个作品都是开源项目，可通过单个链接分享，也能从他人创作中学习。
- 🆕 最新贡献包括 Exp_2、Exp_1、Uplifting Trance Classic、Für Elise | Not-so-piano、a-ha Take On Me 等。
- ⭐ 精选作品包括 Richeh adapting to change、Flute + Fauré's Pavane、-- --- .-. ... .、Cosmic Drone、THX 等。
- ❤️ 最受欢迎作品包括 Oxygene4.js、DT303、Karplus synth with reverb、93' Ditty Jungle、Rainy Night、Vocoder Puccini 等。
- 📚 页面支持浏览全部作品、精选作品和最多人喜爱作品，并带有分页导航，方便探索社区内容。

---

### [](https://github.blog/open-source/git/highlights-from-git-2-56/)

**原文标题**: [Highlights from Git 2.56 - The GitHub Blog](https://github.blog/open-source/git/highlights-from-git-2-56/)

Git 2.56.0 已发布，汇集 104+ 位贡献者（其中 39 位新贡献者）的更新。此次亮点包括更安全的冲突暂存、merge-base 查找提前停止、面向服务器的 path-walk repack 改进，以及 `git history drop`、`git refs`、批量删除分支、bisect/replay 等工具增强；同时修复多处性能缩放问题。

- 🛡️ `git add --resolved`：只暂存索引中的未合并路径，先检查冲突标记；发现标记则全部不暂存，可加 pathspec，且不能与 `-u`/`-A` 组合。
- ⏱️ merge-base 查找优化：一侧独占提交耗尽后即停止，仍返回所有 merge base；monorepo 从 0.68 秒降至 0.01 秒，Linux 内核案例从 167,441 步/0.29 秒降至 3,887 步/0.01 秒。
- 📦 path-walk repack 更适合服务器：更优 delta 使 Fluent UI pack 从 558.5 MB 降至 164.4 MB（约小 71%）；现兼容 reachability bitmaps 与 delta islands，但不默认启用。
- 🧪 `git history drop <commit>`：实验性删除指定提交并把后代重放到其父提交；保护无关本地修改，遇冲突/覆盖则中止，不支持含 merge commit 或删除 root/merge commit。
- 🌿 `git refs` 工具箱：新增 `create/update/delete/rename` 低层引用操作，update/delete 可用 old value 做 CAS；`rename` 不处理 `git branch -m` 的分支配置调整。
- 🧹 `git branch --delete-merged` 批量清理：可匹配 upstream 和本地分支名，支持 `--dry-run`；只删除 tips 可从匹配 upstream 到达的分支，跳过 worktree/缺失 upstream/模糊 push，`deleteMerged=false` 可保护。
- 🔍 `git bisect run --reset-when-found[=<where>]`：查找回归后自动重置；默认 `original` 回到开始前，`found` 保留 culprit，不能与 `--no-checkout` 同用。
- 🧭 `git replay --linearize`：实验性线性化 merge 拓扑并丢弃 merge commit，类似 `git rebase --no-rebase-merges` 但不使用工作树；不能与 `--contained` 或多分支重放组合。
- 🚀 命令行纠错建议：`git push origin/main` 会建议 `git push origin main`；`git branch --set-upstream-to origin main` 会建议 `=origin/main`，且会先检查修正是否合理。
- 🧽 partial clone blob 清理：`git repack -a --filter=blob:limit=1m --drop-filtered` 可删除大且可恢复 blob，之后按需从 promisor remote 重新获取；手动清理，仅支持 `blob:limit`，拒绝不安全情况。
- 🧵 `git log --follow` 更可靠：为每个 parent 单独记录路径，使非线性历史/subtree merge 中的跟踪不受遍历顺序影响。
- 🌳 `git log --graph` 视觉根缩进：多根图中不相关提交不再看起来连到 root；默认启用，可用 `--no-graph-indent` 或 `log.graphIndent` 调整。
- ⚙️ 性能修复：reftable 写入避免冗余重载，packfile 加载去除 O(N²)，37,815 packs 场景从 4.5 秒改善；tombstone 测试约 13 秒降至 0.2 秒；Chromium 50 万 index 的 `git diff` 从约 8 分钟降至 0.07 秒。
- 📚 更多变更可查看 Git 2.56 release notes 和 Git 仓库。

---

### [](https://tannerlinsley.com/posts/projecting-react)

**原文标题**: [Projecting React â Tanner Linsley](https://tannerlinsley.com/posts/projecting-react)

overview summary
文章讲述 Tanner Linsley 用 AI 将 React 公共 API“投影”为 TanStack Start 专用运行时 @tanstack/redact：它体积极小、渲染路径更简单，同时保留 RSC、SSR、Suspense 等实际需要的能力。作者认为代码正从不可变产物变成可按需再生成的“物化视图”，因此未来会出现更多像 Linux 发行版或歌曲 remix 一样的个人化投影；但他不打算把它营销成“替代 React”，只在自己的项目和 tanstack.com 上验证。

- ⚛️ 动机：React 客户端 gzip 约 60KB，是 TanStack 栈中最大且无法移除的部分；Preact/compat 与 React 19 漂移，已不是真正 drop-in。
- 🧠 核心隐喻：代码是“物化视图”，React 公共 API 是 base table，React 仓库只是面向通用场景的一种投影；AI 可生成面向特定消费者的新投影。
- 🌐 背景：Cloudflare 的 vinext 用 AI 一周、约 1100 美元重实现 Next.js API，引发“slop-fork”争议；作者认为商业动机会让它成为产品，而自己的实验没有市场份额目的。
- 🧩 产物：@tanstack/redact，为 TanStack Start 定制的 React 投影；最小核心约 7.08KB gzip，full 预设约 9.39KB gzip。
- 🗜️ 特性开关：portal、context、suspense、memo、forwardRef、lazy、classComponents、hydration 可关闭；Vite 插件用 stub 替换，未用代码不进入模块图。
- 🚫 舍弃：并发渲染、时间切片、lane 调度器、React DevTools、Flight 客户端反序列化；useTransition/useDeferredValue 同步化，startTransition 即 fn()。
- ✅ RSC 可用：Flight 序列化仍使用真实 react-server-dom；tanstack.com 的 RSC 博客与文档渲染无功能回归。
- ⏱️ 构建：一天提示词/塑形完成几乎完整 React surface 并通过测试；后续是在真实流量中发现并修复生产 bug。
- 🐛 生产 bug：子节点插入需反向遍历、useEffect 清理时机、延迟 hydration、受控输入 nativeEvent、SSR 流式缓冲等，修复后 700/700 测试通过。
- 📉 体积：相对 React 19.2.3，客户端运行时约小 80–85%；full 约 11.47KB，nano 约 9.92KB。
- ⚡ 性能：client-nav 34.9→78.1 Hz（2.24×），SSR 约 48→168 Hz（约 3×），stable-list 45.5→37.3ms（1.22×）。
- 📊 站点：tannerlinsley.com 已上线投影，Lighthouse 100，FCP -18%，LCP -12%，JS -33%；tanstack.com 性能持平，FCP 改善，客户端 JS 减约 980KB（-4.7%）。
- ⚠️ 已知回归：tanstack.com 的 RSC 重页面 LCP +8% 到 +43%，但仍在 Core Web Vitals “Good” 范围，修复路径明确。
- 📦 不推广：仅发布 npm 供自用/好奇者，不进入 TanStack Start、不是任何 TanStack 包依赖；避免“替代 React”带来的社区成本。
- 🧬 类比：像 Linux 发行版或歌曲 remix，内核/原曲不变，投影按用户形状重新组合；未来会有更多个人化投影。
- 🧭 结论：上游默认仍是多数场景正确选择，但对强观点项目，拥有自己投影的成本已从数月降到数天，“默认使用上游”不再是自动答案。

---

### [](https://github.com/TanStack/redact)

**原文标题**: [GitHub - TanStack/redact: An alternative logical projection of React with 100% API compliancy but simpler implementation resulting in smaller bundle size and better performance. · GitHub](https://github.com/TanStack/redact)

TanStack Redact 是一个 React 兼容的小型运行时，采用同步渲染；用一个 Vite 插件替换 React、DOM、服务器、调度器和 JSX 入口，同时保持应用导入不变。它追求 React API 与日常行为兼容，但不实现并发调度；0.1.0 默认配置下 gzip 体积比 React 19.3.0 小约 66.3%，部分基准更快，但在 Suspense、水合、被动效果等场景更慢，并有明确兼容边界。

- 🚀 快速开始：`pnpm add @tanstack/redact`，在 Vite 配置中加入 `redact()`；继续从 `react` 和 `react-dom/client` 导入。
- 📦 体积：默认 Vite 配置 gzip 23,311 B，比 React 19.3.0 的 69,162 B 小 66.3%；启用原生动画为 28,159 B，小 59.3%。
- 🧩 独立入口：DOM client 默认 20,139 B，原生动画 24,991 B，`nano` 12,466 B，React API 2,764 B，Server 8,964 B；入口有重叠，不可相加。
- ⚡ 性能亮点：稀疏状态更新 -71.9%、混合深度更新 -59.1%、键控列表反转 -30.3%、context 穿透 memo -29.1%、深层 prop 更新 -22.4%。
- 🐢 性能短板：挂载/卸载 +7.5%、reducer 批量 +7.9%、浏览器端字符串 SSR +10.4%、水合 +21.4%、被动效果 +27.0%、Suspense 重试 +124.8%。
- 🖥️ 服务端渲染：完全就绪可读流 -49.4%，带 hooks/context 的字符串 SSR -30.5%，干净文本 SSR -6.9%，转义文本无明显差异。
- 🖱️ 交互与内存：2,400 行夹具中点击到提交中位数 1.2/1.3 ms，React 为 1.5/1.6 ms；挂载后保留 JS 堆 762.5 KiB，React 为 666.4 KiB；最终卸载后额外 DOM 节点均为 0。
- 🧱 核心兼容：支持 JSX、hooks、context、refs、memo、lazy、portals、错误边界、现代类生命周期；旧版类生命周期为 no-op。
- ⏳ 并发行为：无优先级调度；`useTransition`/`startTransition` 同步执行，`useDeferredValue` 返回输入，pending 始终为 false。
- 🧪 表单与动作：受控输入、重置默认、事件处理、水合期间编辑保留有共享 React 测试；`useActionState`、`useOptimistic`、`useFormStatus` 基本为空操作或空闲。
- 🪟 Suspense/水合：支持 fallback、保留主 DOM、重试、流式边界和事件重放；但没有并发优先级调度。
- 🧠 缓存与调试：`cache` 返回原函数，`cacheSignal` 返回 `null`，`unstable_useCacheRefresh` 为客户端 no-op；`StrictMode`/`Profiler` 不双调或分析，`useDebugValue` 为 no-op；DevTools/Fast Refresh 未实现。
- 🧬 RSC/Flight：RSC 环境保留上游 React，由 `@vitejs/plugin-rsc` 负责 Server Component 序列化，Redact 不重实现。
- 🎛️ 特性开关：`redact()` 默认 full preset，除原生动画外全部可选特性开启；可禁用 hydration、classComponents 等；`nano` 默认关闭所有可选特性，可按需覆盖。
- ✅ 验证：`pnpm test:ci` 通过 1,569 个测试、类型检查、构建包验证器和 19 个 size budget；91 个普通套件跳过不算通过；Chrome 门禁执行 1,266 个用例，7 个声明排除。
- 🌐 真实应用：tanstack.com 预览通过 503 个测试、5 个本地 Worker 路由等，生产升级待审查；tannerlinsley.com 已生产升级，10 页预渲染、8 个实时路由通过，移动端 header 溢出仍存在。
- 🚢 发布流程：用 `pnpm changeset` 提交发布说明；合并到 main 后 Release workflow 创建/更新版本 PR，检查通过后发布到 npm latest 并创建 GitHub release；使用 npm 可信发布。
- 🛠️ 开发命令：`pnpm install`、`pnpm test:ci`、`pnpm size`、`pnpm --filter ssr-demo dev`。
- ⭐ 仓库信息：325 stars、8 forks、2 watchers、1 issue、3 PR、69 commits；定位为 React 的替代逻辑投影，追求 100% API 兼容，但实现更简单、体积更小、性能更好。

---

### [](https://smarmelling.com/posts/the-accidental-history-of-3000-8080-and-other-port-numbers.html)

**原文标题**: [<smarmelling> — The accidental history of 3000, 8080, and other port numbers](https://smarmelling.com/posts/the-accidental-history-of-3000-8080-and-other-port-numbers.html)

文章从“端口已被占用”出发，追溯 3000、8080、5173、6379、31337/1337 等常见端口的历史，发现许多默认值并非严格标准，而是早期选择、惯例与“谢林点”式共识的结果。

- 🔌 端口共有 65,536 个，其中 1–1023 为系统端口，1024–49151 为注册/用户端口；理论上选择很多，但开发默认端口高度集中。
- 🛤️ 3000：Ruby on Rails 在 2004 年早期推广，可能 DHH 个人偏好；Palantir 2002、IANA 2001 已有使用，起源不明；Node.js、Next.js、React 和训练营进一步普及。
- 🌐 8080：HTTP 备选端口，源于 80+80；CERN HTTPD 1998 推荐 8001/8080 作非特权测试端口；Debian 1997、IANA http-alt、Tomcat 与 Jenkins 使其流行；8000/8888 是同思路变体。
- ⚡ 5173：Vite 默认端口，源自文字游戏 51=VI、73=TE，拼成 VITE；虽不如 3000 流行，但很有梗。
- 🍝 6379：Redis 默认端口，手机键盘对应 “Merz”，指意大利模特 Alessia Merz；在 Redis 创始人 Salvatore Sanfilippo 及其朋友语境中意为“愚蠢/无意义”。
- 💀 31337/1337：leet speak 的 elite/leet，与黑客文化绑定；也吸引恶意软件，如 ShadyShell 后门木马。
- 🤝 端口选择像“谢林点”：很多默认端口缺乏清晰传承链，可能只是某人先选，后来者理性地沿用以免出错，最终形成共识。
- 🧠 因此追溯端口历史常会中断；作者建议下次启动服务时选更有纪念意义的端口，如 7373（端口界的 Chuck Norris）或 27182（项目以 e 开头）。
- 📝 文末提示信息可能有误/不全，并邀请订阅 Substack/RSS、评论需启用 JavaScript。

---

