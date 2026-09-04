### [获取失败](https://sendercircle.com/r.php?id=3613)

**原文标题**: [Failed to retrieve](https://sendercircle.com/r.php?id=3613)

无法总结：获取内容失败，状态码 202。

---

### [](https://github.com/tata1mg/catalyst-core)

**原文标题**: [GitHub - tata1mg/catalyst-core · GitHub](https://github.com/tata1mg/catalyst-core)

Catalyst 是一个用于构建高性能 Web 应用及 Android/iOS 通用应用的 React 框架。该 GitHub 仓库提供了框架核心、脚手架 CLI、文档和测试应用，并说明了快速启动、环境要求与贡献方式。页面还展示了仓库的 MIT 许可证和星标/fork 等状态。

- ⚛️ Catalyst 基于 React，支持服务端渲染、路由级数据获取、应用壳、样式约定及原生 WebView 打包。
- 🚀 快速开始：执行 `npx create-catalyst-app@latest` 创建项目，运行 `npm run start` 后访问 http://localhost:3005。
- 📚 文档见 catalyst.1mg.com，可参考“Getting Started”“First Catalyst App”“Universal App Setup”等。
- 📦 主要包：`catalyst-core`（框架）与 `create-catalyst-app`（脚手架 CLI）。
- 🖥️ 环境要求：Node.js 20.4.0+；macOS 或 Linux 用于本地开发。
- 🗂️ 仓库是 monorepo，包含 `packages/catalyst-core`、`packages/create-catalyst-app`、`apps/catalyst-core-test` 和 `docs`。
- 🤝 贡献：先运行 `npm run setup`，然后使用 `npm run core:build`、`npm run core:test`、`npm run cca:test`、`npm run docs:build` 等命令。
- ⭐ 仓库当前有 87 stars、24 forks，采用 MIT 许可证。

---

### [点阵](https://dotmatrix.zzzzshawn.cloud/)

**原文标题**: [Dot Matrix](https://dotmatrix.zzzzshawn.cloud/)

这是一个基于 React、TypeScript、Tailwind CSS 与 shadcn 构建的开源加载动画集合，提供 55+ 种点阵式 loader。用户可通过一条 npx 命令快速安装，复制代码并自由定制，适合直接集成到各类 Web 应用中，且有在线演示与展示页面供参考。

- 🧩 提供 55+ 种免费开源的加载动画，覆盖点阵、螺旋、轨道、脉冲等多种视觉风格
- ⚛️ 基于 React、TypeScript、Tailwind CSS 和 shadcn 开发，技术栈现代，易于集成
- 📦 支持通过 npx 命令一键安装，如 `npx shadcn@latest add @dotmatrix/dotm-square-3`
- ✂️ 安装后可复制代码，自由修改样式与逻辑，灵活适配不同应用场景
- 🎨 包含如 Neon Drift、Pulse Ladder、Core Spiral、Twin Orbit 等大量命名动画组件
- 🚀 提供 Playground 演示环境与 Showcase 展示页面，便于预览和挑选
- 🛠️ 提供完整的使用文档，涵盖手动安装配置等说明，降低上手门槛

---

### [](https://warper.tech/)

**原文标题**: [Warper - Ultra-Fast React Virtualization Library | WASM-Powered | 10M+ Rows at 120 FPS](https://warper.tech/)

Warper 是一款基于 Rust 和 WebAssembly 构建的 React 虚拟化库，主打超高性能滚动渲染，在超过 1000 万条项目时仍可保持 120 FPS。它在极小的 gzip 体积（约 8.7KB）内实现了 O(1) 查找、零 GC 压力、GPU 加速等特性，并提供 v7.2 新功能、多种交互示例、性能对比及简单的安装方式，采用 MIT 许可开源。

- 🚀 Warper 自称“最快的 React 虚拟化库”，由 Rust + WebAssembly 驱动，支持 10M+ 条目下流畅滚动。
- 🎯 关键指标：120+ FPS、10M+ 条目、O(1) 查找、gzip 后约 8.7KB、初始渲染 <10ms、内存占用少 40%。
- ⚡ v7.2 引入零分配热路径，使用 TypedArrays（Int32Array/Float64Array）替代常规数组，降低 GC 压力。
- 🔄 用 O(1) 环形缓冲区替代数组 push/shift，用于帧时间计算，提升滚动稳定性。
- 📦 通用打包器支持：Vite、Webpack、Rollup、esbuild、Parcel、Next.js 开箱即用。
- 🧠 核心技术包括 WASM 引擎、Fenwick 树 O(log n) 可变行高、CSS transform3d 与 contain: strict 的 GPU 加速渲染。
- 📱 示例全部支持响应式，并带有面向移动端的触摸惯性；同时支持 Context7 MCP 以配合 AI 辅助。
- 🏆 对比基准：120 FPS（Warper）> react-window 90、tanstack-virtual 80、react-virtualized 70。
- 🆚 特色对比：Warper 独有 WebAssembly、O(1) 固定高度、O(log n) 可变高度、零拷贝数组和自适应 overscan；竞品多数不支持。
- 🎮 提供 6 个可交互演示：10M 行压力测试、数据表、电子表格网格、聊天界面（可变高度/动态）、文件资源管理器（树视图）。
- 💻 安装命令：npm install @itsmeadarsh/warper；开源 MIT 许可，已被 Vercel、Stripe、Linear、Notion、Figma 等团队采用。

---

### [SVAR React 日历 | 事件日历组件](https://svar.dev/react/calendar/?utm_source=web_tools_weekly&utm_medium=email/)

**原文标题**: [SVAR React Calendar | Event Calendar Component](https://svar.dev/react/calendar/?utm_source=web_tools_weekly&utm_medium=email/)

概述：SVAR React Calendar 是一款专为 React 应用设计的交互式事件日历组件，支持快速构建调度器，并提供灵活视图、拖拽编辑与重复事件等功能，同时提供免费版与专业版。

- 📅 发布全新 React 事件日历组件，专为 React 应用打造
- ⚡ 几分钟内即可构建功能强大的调度器，上手简易
- 🔄 支持灵活视图切换与拖拽式事件编辑，操作直观
- 🔁 内置重复事件功能，满足周期性日程管理需求
- 💰 提供免费版与专业版（PRO Edition）两种选择
- 🚀 已提供“快速开始”与“在线演示”入口，方便体验
- 🧩 除 React 外，其他平台版本也已同步推出

---

### [](https://formengine.io/)

**原文标题**: [FormEngine - Free Open Source React Form Builder | Drag & Drop JSON Forms](https://formengine.io/)

overview summary
- 🧩 FormEngine Core 是一个免费开源的 React 表单库，通过 JSON 驱动动态渲染表单，支持最小化代码构建复杂表单。
- ⚛️ 提供三大部分：Core 表单渲染库、Components 现成 UI 组件库，以及 Designer 拖拽式表单构建器（商业授权）。
- 📜 采用 MIT 许可证，允许自由使用、修改和商用嵌入，无供应商锁定。
- 🧠 内置表单验证、动作（提交/重置/外部调用）、多语言本地化、动态 CSS 与响应式布局，开箱即用。
- 🧩 支持轻松集成自定义组件，只需指定名称、类型和 props，也能以 JSON 方式定义完整表单结构、逻辑和样式。
- 🚀 与 Next.js、Remix 等现代 React 框架无缝配合，并支持 TypeScript 类型定义与 IDE 智能提示。
- 📦 组件库包含 40 多种常用 UI 组件（如输入框、日期选择器、上传器、向导、标签选择器等），全部免费且 MIT 授权。
- 🎛️ FormBuilder 提供条件逻辑功能，可让字段根据用户输入动态显示、隐藏或禁用，适合构建交互式表单。
- 🏢 已被 Bosch、Philips、Dell、Novartis 等全球企业用于生产环境，项目活跃维护，社区支持良好。
- 💬 获得用户好评，认为文档清晰、集成简单、定制灵活，能显著提升表单开发效率。

---

### [microcharts — 适用于 React 的词级图表。迷你趋势图与微图表。](https://microcharts.dev/)

**原文标题**: [microcharts â Word-sized charts for React. Tiny sparklines & micro charts.](https://microcharts.dev/)

overview summary  
- 📦 這是一套針對句子、表格、KPI 卡片等小場景設計的微型圖表庫，提供 106 種圖表類型，體積極小且不需依賴其他套件。  
- 🪶 圖表中位數僅 5.3 kB，最大不超過 7 kB；多數可於 200px 內清楚呈現。  
- ⚛️ 使用方式很簡單：傳入資料陣列即可，React 為唯一 peer dependency。  
- 📊 圖表皆遵循一致 API，domain、color、title 等屬性在不同圖表間語義相同。  
- ♿ 內建無障礙支援：單一 Tab 停留、方向鍵讀值、自動產生 alt text，不以顏色單獨傳遞資訊。  
- 🎨 主題系統可從一個主色自動衍生色盲安全色與深色模式，並保留正負語意色彩。  
- 🛠 也提供 chart fence／MCP 等 AI 輔助設定，讓模型直接產生圖表元件。  
- 🚫 刻意排除圓餅圖、指針儀表、小提琴圖、華夫餅圖等不適合小尺寸的類型，並提供替代方案。  
- 📏 若需要座標軸、圖例與豐富 tooltip，建議改用 Recharts 等完整圖表工具庫。  
- 🧩 原生支援異常資料（NaN、空陣列等），確保模型回應中斷時仍能渲染出合理內容。  
- 🖨 靜態圖表可在 Server Component 中輸出，客戶端不需要任何 JavaScript。  
- 📱 內含七個範例應用，涵蓋全部 106 種圖表，展示產品分析、交易終端、健康年曆、印刷雜誌等不同風格與主題。

---

### [](https://www.mapcn.dev/)

**原文标题**: [mapcn - Beautiful maps made simple](https://www.mapcn.dev/)

overview summary  
- 🗺️ 提供基于 MapLibre 和 Tailwind CSS 的 React 地图组件，强调美观、易用与可定制性。  
- ⚡ 支持快速开始、组件浏览，并附有适用于 AI 智能体的提示词复制功能。  
- 📈 展示活跃用户数据（3,544 人，+12.5%），并示例跑步路径指标（距离、时长、卡路里）。  
- 🌆 内置多个城市选择（纽约、伦敦、东京、悉尼），方便地图切换与展示。  
- 🧩 定位为免费开源项目，提供产品文档、组件库、区块资源及社区支持。  
- 🎨 基于 MapLibre GL、shadcn/ui 与 Tailwind CSS 构建，并保留版权信息。

---

### [](https://github.com/roman01la/blender-react)

**原文标题**: [GitHub - roman01la/blender-react: A Blender addon that lets you create and manage 3D scenes using React components · GitHub](https://github.com/roman01la/blender-react)

Blender React 是一个在 Blender 中运行的开源插件，它将 React 组件映射为 3D 场景对象，借助 QuickJS 引擎、自定义 reconciler，并以 ClojureScript/UIx 与 shadow-cljs 作为开发栈，让用户用声明式语法创建和管理 Blender 场景。

- 🧩 核心能力：用 React/JSX 等声明式语法创建 3D 场景，完整支持 Hooks、状态、副作用与组件组合。
- 🔗 父子关系：嵌套组件会构建 Blender 对象层级，移动父对象时子对象跟随变换。
- 🎨 材质与几何节点：支持 PBR 材质，并通过 Blender 几何节点（60 余种）实现程序化建模。
- ⚡ 动画：支持 requestAnimationFrame 和 setInterval 驱动实时动态场景。
- 🔄 热重载：无需重启 Blender 即能重新加载场景与脚本。
- 📦 安装要求：需 Blender 3.0+、Node.js 18+ 和 Java，通过 addons 目录克隆、npm install、构建后启用插件。
- 🌐 支持组件：涵盖网格图元（立方体、球体、猴头等）、灯光（点光、太阳光、聚光、面光）、相机、材质和空对象等类型。
- 🔌 节点连接：几何节点支持自动链式连接、节点作为 prop 传入指定 socket，以及显式 connect 三种连接方式。
- 📂 开发结构：主要包含 src/app/core.cljs、reconciler.js、quickjs_runtime.py、__init__.py 等文件，Python/Blender 桥接 QuickJS。
- 🛠️ 调试方式：从终端启动 Blender，可在 JS 中使用 print() 或 console.log() 输出调试信息。
- 📄 许可证：项目采用 ISC 许可证发布。

---

### [适用于现代文档应用的开源 UI 工具包 - Extend UI](https://www.extend.ai/ui)

**原文标题**: [Open source UI kit for modern document apps - Extend UI](https://www.extend.ai/ui)

这是一个开源的 React UI 工具包，专为现代文档应用场景打造，提供 PDF、DOCX、XLSX、CSV 等多种文档组件的开箱即用能力，并集成了边界框引用、文件上传、电子签名等进阶功能，可灵活嵌入用户端流程、AI 代理或内部工具中。

- 📦 面向现代文档应用的开源 React UI 组件库
- 📄 提供 PDF 查看器，支持文档展示与交互
- 📊 提供 XLSX 查看器，方便表格数据浏览
- 🔗 兼容 DOCX、CSV 等多格式文档查看能力
- 🔖 支持边界框引用（bounding box citations）功能
- ✍️ 内置电子签名功能，满足签署流程需求
- 📂 包含文件上传与文件系统组件，便于文档管理
- 🧩 提供 Schema Builder 组件，辅助数据结构搭建
- 🚀 可快速集成到用户流程、AI 代理或内部工具中

---

### [智能体行为](https://www.agentbehavior.dev/)

**原文标题**: [Agent behavior](https://www.agentbehavior.dev/)

Agent behavior 是一套标准格式，用于以 Markdown 文件形式描述 AI 代理在重复交互中的预期行为；文件存放在代码仓库的 `.agents/behaviors/<行为名>/BEHAVIOR.md`，供审查 traces、设计 evals、对齐 prompts 和团队沟通使用。文本同时给出了成本敏感操作、生产环境变更、事实声明等示例，并说明了创建流程、使用场景、格式规范、验证方法以及与其他工件的关系。

- 📂 每个行为规范是一个 Markdown 文件，包含 YAML frontmatter（name、description 等）和自由格式正文，目录名必须与 name 字段一致。
- ✍️ 快速入门：先创建 BEHAVIOR.md，然后在正文里描述行为何时适用、应收集什么证据、如何让成本/环境等权衡可见以及要避免什么。
- 💰 示例行为“cost-sensitive-actions”：要求不得静默花钱，应评估或估算成本、信用和基础设施影响，在越过有意义阈值前先报成本并征求同意。
- ⚙️ 示例行为“production-environment-changes”：涉及生产系统、数据或用户状态的变更前需确认，明确环境和影响范围，环境不明时先询问。
- 📝 示例行为“factual-claims-in-copy”：发布前核实具体事实、数字和产品声明，无法核实的内容应标记为未验证，而不是当作事实。
- 🔍 推荐行为维度包括 Intent、Evidence、Decision、Execution、Recovery 和 Failure modes，可按需组合、改名或省略。
- 🚀 使用场景包括审查代理轨迹、设计 eval 用例、在 trace 显示行为缺失时修订 prompts 或工具，以及向队友传达预期行为。
- 🧭 何时新增行为：行为频繁出现、影响正确性/信任/安全/成本/体验、体现代理定位、默认模糊、跨多个上下文、有助于解释失败。
- 🔗 Behavior spec 与系统提示、技能、工具文档、evals、traces 各有分工：spec 制定标准，其他工件负责实现和测试该标准。
- ⚖️ 与 AGENTS.md 的关键区别：AGENTS.md 指导代理“如何做”，偏运行时实现；BEHAVIOR.md 定义“什么是良好行为”，面向审查/评估，变更随行为标准而非实现变化。
- 🧱 结构验证要求目录、BEHAVIOR.md、YAML frontmatter 字段（name/description 等）合法；高质量 spec 应清楚区分行为、适用场景、期望行为和不当行为。
- 📁 可选目录 references/ 可存放理由文档、示例 traces、背景资料等，帮助审查者和 eval 作者理解行为。

---

### [](https://paseo.sh/)

**原文标题**: [Paseo – Run Claude Code, Codex, Copilot, OpenCode from anywhere](https://paseo.sh/)

Paseo 是一款备受好评的开源 AI 编程代理编排工具，强调跨平台、自由选择、远程访问与高度自动化，让用户能灵活管理多种 coding agent。

- 🏆 开发者盛赞其为“最被低估的编排器”，开源且支持全平台，移动端体验特别出色。
- 🔄 可无缝互换 Claude Code、Codex、OpenCode、Pi、Cursor 等 34+ 工具，并沿用你自己的订阅、技能与配置。
- 📱 提供桌面应用、移动/Web 客户端，也能在家用服务器或云端远程运行，随时随地掌控代理进度。
- 🔐 借助端到端加密中继、Tailscale/自建隧道等方式，可安全地在外部网络连接工作区，且代码不会离开本机。
- ⚙️ 支持内置自动化：通过 MCP、CLI、TypeScript SDK，可将 GitHub 上待办 issues 自动分发给多个 worktree agents。
- 🧩 拥有插件系统，可扩展服务端能力和客户端组件；项目基于 Apache 2.0，允许自由 Fork 定制。
- 🗣️ 语音功能默认本地优先处理，也可按需配置云端语音服务提升识别与合成效果。
- 🆓 完全免费开源；各代理仍在本地以官方方式运行，不提取令牌或绕过服务条款。
- 📌 常见问答覆盖：无需桌面应用也能用、不依赖 Git、支持外部网络连接，并明确说明不会导致封号。
- ❤️ 用户称其“今年用过最好的软件”，能大幅提升生产力，同时实现“完全从手机工作”的流畅体验。
- 🎯 核心理念是“可选性与自由”——不锁定任何生态，既可自托管，也鼓励赞助以支持持续开发。

---

### [](https://github.com/luongnv89/asm)

**原文标题**: [GitHub - luongnv89/asm: The universal skill manager for AI coding agents. · GitHub](https://github.com/luongnv89/asm)

overview summary
- ⚙️ asm（agent-skill-manager）是一个面向 AI 代理与自动化的可脚本化 CLI，用于在 Claude Code、Codex、Cursor、Windsurf、Copilot 等 19 种工具之间安装、搜索、审计与管理技能，支持 `--json`/`--yes` 并附带可选 TUI。
- 🧩 它解决的关键痛点：技能目录分散、没有统一库存清单、技能描述常驻提示造成 token 开销、手动安装有安全风险、输出不易被代理解析等。
- 📊 目前收录 4,672 个技能，来自 58 个仓库；MIT 许可，无需账户、无遥测。
- 🗂️ 核心功能包括跨工具库存清单、本地标签、一键安装、重复/语义重叠审计、token 与驻留审计、安全扫描、创作发布流程、bundle 批量安装和本地 library 管理。
- 📥 安装方式：`npm install -g agent-skill-manager`，或通过 curl 脚本安装；要求 Node.js 22+，直接运行 `asm` 可进入 TUI。
- 🖥️ 常用命令示例：`asm list --json` 查看所有技能，`asm install github:anthropics/skills` 安装技能，`asm search "code review" --json` 搜索，`asm audit --yes` 自动清理重复技能。
- 🧠 注意力预算：`asm stats --tokens` 会区分 resident（每轮消息都消耗 token 的描述）与 body（仅在技能触发时加载）成本；`asm audit residency` 会建议将不值得驻留的技能降级。
- 📄 `asm get <skill>` 可将技能正文直接输出到 stdout，实现“按需读取”而不安装、不常驻，适合代理管道使用，并支持 `--json` 输出来源、token 与安全结果。
- 🔒 安全性：安装前会扫描 shell 执行、网络访问、凭据暴露等风险，校验 SKILL.md frontmatter，registry 安装会固定 commit；`asm audit security` 可做额外审查。
- 🧪 技能开发生命周期：`asm init` 脚手架、`asm link` 符号链接实时开发、`asm eval` 质量评分、`asm publish` 发布到 ASM Registry。
- 📚 支持从 GitHub 仓库或 ASM Registry 安装，也能处理子目录、私有仓库（SSH）与 Vercel skills；官方及社区集合（如 anthropics/skills、everything-claude-code 等）有超过 2,800 个技能可搜索安装。
- 🎛️ 19 个 provider 默认全部启用，可通过 config 文件关闭或添加自定义路径；TUI 提供键盘导航、筛选、配置与审计入口。

---

### [获取失败](https://sendercircle.com/r.php?id=3614)

**原文标题**: [Failed to retrieve](https://sendercircle.com/r.php?id=3614)

无法总结：获取内容失败，状态码 202。

---

### [](https://github.com/composio-community/awesome-claude-plugins)

**原文标题**: [GitHub - composio-community/awesome-claude-plugins: A curated list of Plugins that let you extend Claude Code with custom commands, agents, hooks, and MCP servers through the plugin system. · GitHub](https://github.com/composio-community/awesome-claude-plugins)

该仓库（composio-community/awesome-claude-plugins）是一个精选的 Claude Code 插件列表，收录了覆盖集成、前端、Git、测试、后端、DevOps、文档、安全与生产力等场景的生产级插件，并提供标准目录结构、使用方法和贡献指南。

- 🔌 插件机制：Claude Code 插件通过自定义斜杠命令、专用 agent、hooks 和 skills 扩展功能，并可在项目与团队间复用。
- 📬 核心亮点 connect-apps：让 Claude 连接 Gmail、Slack、GitHub、Notion 等 1000+ 应用，执行发邮件、建 issue、发消息等真实操作。
- 🎨 前端与设计类：包含 frontend-design、artifacts-builder、theme-factory、senior-frontend 等，强调避免“AI 味”的高质量 UI 与组件开发。
- 🌿 Git 与版本控制类：提供 commit、create-pr、pr-review、changelog-generator、ship 等自动化流程，覆盖提交到发布。
- ✅ 代码质量与测试类：包括 code-review、test-writer-fixer、debugger、bug-fix、AgentLint 等，辅助审查、测试与排错。
- 🏗️ 后端与架构类：backend-architect 提供架构与 API 设计，mcp-builder 指导构建 MCP server，另有 maestro-orchestrate 支持多 agent 编排。
- ⚡ DevOps 与性能类：包含 perf、audit-project、aws-cost-saver、MyVibe（即时部署）、Manifest（成本观测）等效率与运维工具。
- 🔒 文档与安全类：覆盖文档生成、安全最佳实践、OWASP/LLM Top 10 扫描，以及带可验证审计签名的 asqav 插件。
- 🧠 开发者生产力类：包含 CCHub 桌面管理、skill-bus、context-mode（节省上下文）、codebase-graph、backlog 任务管理等。
- ✨ 扩展与趣味类：claude-familiar 增强陪伴个性和交互，nano-banana 支持 Gemini 图像生成，taisly-agent-kit 可发布短视频到主流平台。
- 🚀 快速开始：克隆仓库后使用 `claude --plugin-dir <插件目录>` 即可加载，也可通过多个 `--plugin-dir` 同时启用多个插件。
- 📂 插件标准结构：插件包含 `.claude-plugin/plugin.json`，并可选含 skills、commands、agents、hooks 等目录；项目采用 MIT 许可证，欢迎提交 PR 贡献。

---

### [](https://github.com/DietrichGebert/ponytail)

**原文标题**: [GitHub - DietrichGebert/ponytail: Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote. · GitHub](https://github.com/DietrichGebert/ponytail)

这是 DietrichGebert/Ponytail 项目的 GitHub 介绍摘要：它是一套面向 AI 编码代理的规则/插件/技能，把“最懒也最资深开发者”的思维注入 AI，使其只编写真正必要的最小代码；真实基准显示可显著减少代码量、成本与耗时，同时保持安全，并支持多种主流 AI 工具。

- 🐴 核心理念：让 AI 像“长马尾、少说话、五十行换一行”的资深工程师——最佳代码是根本不需要写的代码，重点避免过度工程化。
- 📉 实测效果：在真实 Claude Code 会话中（编辑 FastAPI+React 仓库、完成 12 个功能任务），相比无技能基线：代码量平均减少约 54%（最高 94%），token 减少 22%，成本降低 20%，耗时减少 27%，安全性保持 100%。
- ✅ 对比优势：与 caveman 提示和“YAGNI + one-liners”提示相比，只有 ponytail 能在代码量、token、成本、时间和安全这五项上同时取得正收益并保持 100% 安全。
- 🪜 决策机制：先理解问题并阅读受影响的代码，再依次判断：是否真正需要（YAGNI）？仓库里是否已有？标准库能否实现？原生平台是否支持？已装依赖能否做到？一行能否搞定？最后才写最小可行实现。
- 🧯 安全底线：“懒但绝不疏忽”——验证、错误处理、安全性和无障碍相关代码绝不能被删减；代码小是因为“恰好必要”，而不是单纯追求字面最少 token。
- 🔌 平台覆盖：支持 Claude Code、Codex、GitHub Copilot CLI、OpenCode、Gemini CLI/Antigravity、Devin、Grok Build、OpenClaw、Hermes、Qoder 等插件安装；Cursor、Windsurf、Cline、Kiro 等可复制规则文件使用。
- 🎛️ 模式与命令：默认 full 模式；可用 `/ponytail lite|full|ultra|off` 调整强度，并提供 `/ponytail-review`（审查 diff）、`/ponytail-audit`（审计仓库）、`/ponytail-debt`、`/ponytail-gain`、`/ponytail-help` 等命令。
- ⚙️ 配置与许可：无需配置文件，也可通过 `PONYTAIL_DEFAULT_MODE` 或 `config.json` 设置默认级别；支持向子代理注入规则并可用正则限定范围；项目采用 MIT 许可证。

---

### [](https://github.com/XiaomiMiMo/MiMo-Code)

**原文标题**: [GitHub - XiaomiMiMo/MiMo-Code: MiMo Code: Where Models and Agents Co-Evolve · GitHub](https://github.com/XiaomiMiMo/MiMo-Code)

overview summary
MiMoCode 是小米推出的终端原生 AI 编码助手，支持连接主流 LLM API，具备多代理协作、持久记忆、智能上下文管理、工作流、内置技能等功能，并可通过“Dream & Distill”自我进化。

- 🚀 **终端 AI 编码助手**：MiMoCode 可读写代码、执行命令、管理 Git，并利用持久记忆系统跨会话保持项目深度理解，同时持续自我改进。
- 🧩 **多代理模式**：内置 build（默认全权限）、plan（只读分析）、compose（规范驱动开发）三种主要代理，可按 Tab 切换，并支持按需创建子代理并行工作。
- 🧠 **持久记忆系统**：基于 SQLite FTS5，保存项目记忆（MEMORY.md）、会话检查点、草稿笔记和任务进度；会话恢复时自动注入记忆，无需重新学习上下文。
- ⚙️ **智能上下文管理**：支持自动检查点、上下文重建、预算化注入，并可通过 `/context-limit` 为模型设置更早的压缩点以控制成本或适配实际可用窗口。
- 🎯 **目标与停止条件**：`/goal` 命令设定会话停止条件，由独立裁判模型评估是否真正满足，避免自主工作过早“乐观停止”。
- 📋 **Compose 模式**：推荐在 build 代理上使用 `/compose-next` 技能，执行从规格到交付的完整开发流程；也保留传统 compose 代理（含 14 个内置技能）供较弱模型使用。
- 🔄 **确定性工作流**：内置 compose、deep-research、fact-check、research-experiment 四种 JavaScript 工作流，可在沙箱中编排多代理执行固定阶段、并行化与有限重试，无需用户交互。
- 🛠️ **丰富内置技能**：包括 arxiv、claude-code、codex、文档/表格/PPT/PDF 处理、前端设计、深度研究、技能创建等；可被项目级或个人技能目录中的同名技能覆盖。
- 🎤 **语音输入**：支持实时流式语音（TenVAD + MiMo ASR），暂停自动分段转文字；也支持通过 OpenRouter 或自定义 OpenAI 兼容提供商路由语音控制。
- ✨ **自我进化机制**：`/dream` 从会话痕迹中提炼持久知识并清理过期条目；`/distill` 发现重复手动流程并打包为可复用技能、子代理或命令。
- 📦 **多平台安装**：支持 macOS/Linux 一行脚本、Windows PowerShell、npm 全局安装；首次启动引导配置 Xiaomi MiMo、Codex、Claude Code 或任意 OpenAI 兼容自定义提供商。
- ⚠️ **权限与安全性**：默认对项目外目录读写触发确认；可通过配置显式允许 `/tmp` 或使用 `--dangerously-skip-permissions` 自动批准（仅适用于可信环境，存有风险）。
- 🧪 **技术背景**：MiMoCode 基于 OpenCode 分支，保留多提供商、TUI、LSP、MCP、插件等核心能力，并新增记忆、上下文管理、子代理编排等增强。
- 📚 **配置灵活**：使用 JSON/JSONC 配置文件，支持项目级与全局级设置，带 JSON Schema 自动补全；数据与状态目录遵循 XDG，可用 `MIMOCODE_HOME` 覆盖。

---

### [](https://github.com/code-yeongyu/oh-my-openagent)

**原文标题**: [GitHub - code-yeongyu/oh-my-openagent: omo/lazycodex: The coding agent for tokenmaxxers;the one and only agent harness for complex codebases. For your Codex, for your OpenCode · GitHub](https://github.com/code-yeongyu/oh-my-openagent)

oh-my-openagent（简称 OmO）是一个开源的多智能体编程协调工具，旨在将 OpenCode、Codex CLI 等宿主环境与多种前沿 AI 模型结合，通过自动化编排完成复杂编码任务。它提供三种版本：面向 OpenCode 的 Ultimate 版、面向 Codex CLI 的 Light 版，以及独立的 Senpi 测试版。项目强调“集成而非锁定”，内置众多优化工具，并因高效的开发体验在 GitHub 上获得 68.6k 星标。

- 🧩 **统一多模型编排**：一套工具同时驱动 Claude、GPT、Kimi、GLM 等模型，根据任务类别自动匹配最佳模型，而不是绑定单一 AI 提供商。
- 🚀 **一键 ultrawork**：输入 `ultrawork`/`ulw` 即可激活全部智能体并行协作，自动持续工作直到任务彻底完成。
- 🏗️ **三种安装版本**：Ultimate（OpenCode 插件，`bunx oh-my-openagent install`）、Light（Codex CLI 插件，`npx lazycodex-ai install`）、Senpi（独立测试版，`npm i -g omo-ai@beta`）。
- 🤖 **学科智能体团队**：Sisyphus 作为主协调者，配合 Hephaestus（自主执行）、Prometheus（规划）、Oracle（调试）等专职智能体，组成完整的虚拟开发团队。
- 👥 **Team Mode 团队模式**：可选功能，由主智能体带领最多 8 个并行成员，支持 tmux 实时可视化，内置 `hyperplan`（敌意评审）和 `security-research`（安全审计）技能。
- ✂️ **Hashline 安全编辑**：通过哈希锚定的 `LINE#ID` 引用文件内容，文件变更后自动拒绝过时编辑，大幅减少模型“找不到行”或“错改”的问题。
- 🛠️ **集成 IDE 级工具**：内置 LSP（跳转、重命名、诊断）、AST-grep（25 种语言模式搜索）、Tmux（持久终端）和多个 MCP 服务（Exa、Context7、Grep.app）。
- 🔌 **兼容 Claude Code 生态**：现有 hooks、命令、技能、MCP 和插件均可直接复用，降低切换成本。
- 📄 **规则与上下文自动注入**：自动加载 `AGENTS.md` 与 `.omo/rules/**`，并支持 `/init-deep` 生成层级化项目文档。
- ⚙️ **高度可配置但有默认值**：支持 JSONC 配置、54+ 生命周期 hooks、模型回退、文件提示、会话恢复及实验性功能。
- 🔒 **遥测默认开启**：以匿名、每日一次的方式收集 DAU/WAU/MAU，可通过环境变量或配置文件完全关闭。
- 💡 **项目理念与社区**：由作者个人 2.4 万美元 token 消耗实验驱动，旨在“偷取最佳实践并集成”，无厂商隶属；欢迎 PR，并有 DISCORD 社区。
- ⚠️ **命名注意**：npm 上的 `omo` 属于无关作者的不同包，必须使用 `omo-ai@beta` 安装独立版；旧命令 `oh-my-opencode` 仍可用但推荐使用新名。

---

### [](https://github.com/openai/openai-apps-sdk-examples)

**原文标题**: [GitHub - openai/openai-apps-sdk-examples: Example apps for the Apps SDK · GitHub](https://github.com/openai/openai-apps-sdk-examples)

该仓库是 OpenAI 的 Apps SDK 示例合集，展示了如何结合 MCP（模型上下文协议）服务器，将可交互 UI 组件作为工具集成到 ChatGPT 中。示例覆盖多种服务器语言（Node/Python）与场景，并附带完整的本地构建、运行和测试流程，可作为开发 ChatGPT 应用的起点。

- 🧩 仓库包含多个示例 UI 组件和对应 MCP 服务器，用于构建和演示 ChatGPT 应用。
- 🔌 MCP 通过标准化协议将模型与外部工具、数据和 UI 连接起来，可同步返回结构化内容与界面元数据。
- 🛠️ 一个最小化 Apps SDK 集成需实现三件事：列出工具、调用工具、返回可内联渲染的 widget。
- 📁 目录结构包括 `src/`（组件源码）、`assets/`（构建产物）及各语言的 MCP 示例服务器，如 Pizzaz、Kitchen sink、购物车、太阳系、认证服务器等。
- 🍕 Pizzaz 示例展示列表、轮播、地图视图及带结账流程的店铺界面；Kitchen sink 示例演示完整的 `window.openai` API 的能力。
- 🛒 购物车示例特别展示 `_meta["widgetSessionId"]` 如何在多轮工具调用间同步 `widgetState`，保持模型与 widget 状态一致。
- ⚙️ 环境要求：Node.js 18+、pnpm、Python 3.10+；通过 `pnpm install` 和 `pnpm run build` 安装依赖并构建组件。
- 🖥️ 构建后执行 `pnpm run serve` 在本地 `localhost:4444` 提供静态资源；可用 `pnpm run dev` 进行组件开发迭代。
- 🚀 每个 MCP 服务器都有独立启动命令（如 `pnpm start` 或 `uvicorn`），Python 服务器可以共用同一个虚拟环境。
- 🧪 在 ChatGPT 中测试需开启开发者模式，在 Settings > Connectors 中添加应用；可使用 ngrok 将本地 MCP 服务器暴露为公网 URL。
- 🌐 使用隧道时需设置 `MCP_ALLOWED_HOSTS` 和 `MCP_ALLOWED_ORIGINS` 环境变量，以通过 Python MCP SDK 的 DNS 重绑定保护。
- 📦 部署服务器时需配置 `BASE_URL` 和 `API_BASE_URL`，用于生成可访问的 HTML 和 API 地址。
- 📄 项目基于 MIT 许可证开源，欢迎提交 issue 或 PR 贡献改进。

---

### [Meco：排名第一的](https://meco.app?utm_campaign=3nux)

**原文标题**: [Meco: The #1 newsletter reader | Declutter your inbox](https://meco.app?utm_campaign=3nux)

Meco 是一款专为阅读新闻通讯设计的聚合工具，它能把订阅内容从邮箱中解放出来，整合到一个更专注的阅读空间，并借助 AI 与整理功能帮助用户高效获取、管理知识与资讯，同时兼容多平台并可随时还原到邮箱。

- 📮 新闻通讯与收件箱分离：Meco 将新闻通讯移至专属阅读空间，摆脱收件箱噪音与混乱，快速实现收件箱的整洁。
- 🔗 快速连接已有邮箱：支持关联 Gmail、Outlook，可一键导入现有新闻通讯订阅，并将其设置为自动跳过邮箱，随时可以恢复。
- ✉️ 专属 Meco 邮箱：无需 Gmail 或 Outlook 也能使用，Meco 会提供专属邮箱地址，用于订阅各类新闻通讯。
- 🧭 智能筛选与分组：通过过滤器和分组功能，把最重要、最相关内容优先呈现，彻底告别信息过载。
- 🎧 AI 音频简报：每天生成 5–10 分钟个性化音频播客，帮助你利用通勤或碎片时间快速掌握新闻通讯要点。
- 💡 AI 文本摘要与每周回顾：可一键生成新闻通讯摘要，并定期汇总未读内容中的热门观点，避免错过关键信息。
- 📌 知识与标注工具：支持书签、高亮、标签及笔记，方便将阅读中获得的灵感系统化保存和分类。
- ✂️ 轻松管理订阅：提供一键退订入口，随时移除不再需要的订阅，让订阅列表更贴合个人需求。
- 📱 多平台离线阅读：适用于 iOS、Android 和 Web，并支持离线阅读，适合通勤或旅行场景。
- 🔒 隐私保护与商业模式：Meco 不存储或处理用户邮件数据，不投放广告也不出售数据，以付费订阅作为收入来源，可随时安全解除邮箱关联。

---

### [](https://github.com/BCsabaEngine/svelteesp32)

**原文标题**: [GitHub - BCsabaEngine/svelteesp32: Pack any Svelte, React, Angular, or Vue app into a single C++ header. Serve it straight from ESP32/ESP8266 flash — gzip compressed, ETag cached, OTA-ready. · GitHub](https://github.com/BCsabaEngine/svelteesp32)

该工具可将任意 Web 前端（Svelte/React/Angular/Vue）构建成一个 C++ 头文件，嵌入 ESP32/ESP8266 固件，直接通过 Flash 伺服页面；它省去 SPIFFS/LittleFS 分区上传与复杂 OTA，并用单二进制、自动 gzip、ETag 缓存等机制简化 IoT Web UI 部署。

- 🎯 核心定位：将前端构建产物打包成单个 `svelteesp32.h`，在固件中一行调用即可伺服整个 Web 应用。
- 🔄 解决痛点：取代传统文件系统方案，不需要分区表、独立上传或运行时压缩，适合单二进制 OTA 与 CI/CD。
- ⚡ 自动优化：构建时自动 gzip（大于 1KB 且压缩率 >15% 才启用），支持 duplicate 检测与跳过已压缩文件。
- 🧠 智能缓存：内置 SHA256 截断的 RFC 9110 兼容 ETag，返回 304 响应，大幅降低带宽占用。
- 🖥️ 四引擎可选：支持 PsychicHttpServer V2、ESPAsyncWebServer、Arduino WebServer、原生 ESP-IDF。
- 🚀 快速开始：安装 `svelteesp32` 后执行 `npx svelteesp32 -e psychic -s ./dist -o ./esp32/svelteesp32.h`，再在代码中 `initSvelteStaticFiles(...)`。
- 👩‍💻 开发工作流：日常用 Vite dev server + ESP32 REST API 做内循环，发布时才生成 header 并编译进固件。
- 🧩 Vite 插件：`svelteESP32()` 可挂到构建管线，在每次 `vite build` 后自动生成 header，不干扰 dev server。
- 📁 缓存控制：支持 `--cachetimehtml` / `--cachetimeassets` 区分 HTML 与内容哈希 JS/CSS，实现 no-cache 或一年缓存策略。
- 📦 生成内容：header 含文件清单、ETag 表、gzip 字节数组、URI 路由，并提供编译期宏与运行时文件元数据。
- 📥 HEAD 支持：psychic/async 引擎原生支持 HEAD；webserver/ESP-IDF 需自行添加类似处理。
- 🧩 SPA 与多前端：支持 `--spa` catch-all 路由和 `--basepath` 前缀（如 `/admin`、`/app`），可管理多个 web 应用。
- 📊 CI 工具：`--analyze` 输出各文件大小并检查预算，超限即 exit 1；`--manifest` 写出 JSON 清单，便于持续集成。
- 📝 配置文件：`.svelteesp32rc.json` 可保存所有选项，支持 npm 变量插值和多环境（如 `.prod.json`）。
- 🔌 集成示例：涵盖 Arduino IDE、PlatformIO 预构建、ESP-IDF CMake，可自动在 `pio run` 或 CMake 构建前生成 header。
- ⚙️ 编译期校验：用 `#if SVELTEESP32_COUNT != 5` 等宏检测前端是否失效或文件数是否符合预期。
- 📋 运行时钩子：可通过弱函数 `SVELTEESP32_onFileServed(path,status)` 记录请求与缓存命中统计。
- 🔐 注意事项：极限老浏览器可设 `--etag=never --cachetime=0`；RC 文件中输出路径必须为相对路径。

---

### [](https://github.com/webpro-nl/unbash)

**原文标题**: [GitHub - webpro-nl/unbash: Fast 0-deps bash parser written in TypeScript · GitHub](https://github.com/webpro-nl/unbash)

unbash 是一个用 TypeScript 编写的零依赖 Bash 解析器，可将 Bash 源码解析为带源码位置的类型化 AST，支持广泛语法、容错式部分解析、结构化词元展开，并提供打印器、基准测试和同类工具对比。

- 📦 **安装与定位**：通过 `npm install unbash` 安装，适合解析用户粘贴的命令、完整脚本或嵌入他处格式中的 shell 源码，返回类型化且带 `[pos,end)` 位置信息的 AST。
- 🛡️ **主要用途**：用于命令/重定向/替换分类、权限提示和审计；静态盘点包脚本/CI/任务运行器中的可执行文件与文件引用；单独转换 `curl` 等命令；生成诊断、结构化预览及进行源码范围编辑。
- 🧩 **语法覆盖**：支持命令、控制流、管道、重定向、赋值、复合语句、参数与词展开、进程/嵌套替换、heredoc/herestring、coproc、extglob 等；嵌入参数数组索引和算术表达式中的嵌套命令仍保持结构化。
- ⚠️ **容错与边界**：对畸形或不完整输入会返回尽力而为的局部 AST 并收集定位错误；它不执行代码、不做 shell 展开、不提供沙箱，也不判断命令是否安全。
- 🔍 **Word parts 特性**：`Word.parts` 是惰性 getter 且非自有可枚举属性，`Object.keys`、对象展开和 `structuredClone` 都看不到它；可直接读取或用 `JSON.stringify` 序列化。
- 📌 **位置与嵌套错误**：位置基于 UTF-16 码元，根脚本和部分嵌套替换可直接切片源文本；每个嵌套脚本都有独立 `errors`，完整遍历时需逐个检查。
- 🖨️ **打印器支持**：提供基础风格化 `unbash/printer`，可把 AST 打印为脚本，但不保留空白和注释（shebang 除外）。
- ⚖️ **同类对比**：相比 tree-sitter-bash，提供可执行语法 AST 而非 CST，且零依赖、无需 WASM/原生模块；相比 sh-syntax，无需 WASM 加载且 AST 更 JSON 友好；相比 bash-parser，支持更多现代 Bash 结构和错误恢复。
- 🚀 **性能与体积**：基准测试中解析速度大幅领先同类（如 970KiB 大文件约 112.4 MB/s，快于 tree-sitter-bash 等的约 8–15 MB/s）；打包后约 80KB minified、19KB gzip。
- 🔗 **资源与许可**：项目以 ISC 许可开源，提供在线 playground：`unbash.statichost.page` 和 `ast-explorer.dev`。

---

### [](https://github.com/lumirlumir/npm-eslint-markdown)

**原文标题**: [GitHub - lumirlumir/npm-eslint-markdown: Lint your Markdown with ESLint. Additional rules for use with `@eslint/markdown`.🛠️ · GitHub](https://github.com/lumirlumir/npm-eslint-markdown)

overview summary
该仓库是一个名为 eslint-markdown 的开源项目，提供 ESLint 插件，用于对 Markdown 文件进行代码检查，并补充了与 @eslint/markdown 配合使用的额外规则。

- ⭐ 项目欢迎用户为其在 GitHub 上点赞支持，以帮助改进和维护。
- 🛠️ 核心功能是使用 ESLint 检查 Markdown，并提供与 @eslint/markdown 配套的附加规则。
- 📄 已提供官方文档，涵盖安装、配置、迁移指南及规则说明。
- 🔄 该插件不包含与 ESLint 内置 Markdown 规则重叠的规则，建议与 @eslint/markdown 搭配使用。
- 📜 仓库包含行为准则、变更日志、版本控制和安全政策等标准项目文件。
- 🏷️ 项目采用 MIT 许可证，主要面向 CommonMark、GFM 等 Markdown 格式。
- 📦 仓库结构包括 packages/eslint-markdown、scripts、website 等目录，并配置了多种开发工具。

---

### [GitHub - stagas/tsbro：用于浏览器的 TypeScript · GitHub](https://github.com/stagas/tsbro)

**原文标题**: [GitHub - stagas/tsbro: TypeScript for the Browser · GitHub](https://github.com/stagas/tsbro)

tsbro 是一个让 TypeScript 直接在浏览器中运行的开源工具，主打“无需工具链、无需构建步骤”，适合快速写 demo 或概念验证。它通过同步 XHR 获取 TS/TSX 代码，用 SWC（WASM 版本）转译为 JavaScript，再借助自带的 ESM 到 CJS 转换器，最终通过 eval 执行。下面概述其核心要点。

- 🚀 **核心定位**：tsbro 让 TypeScript 在浏览器里原生可用，省去打包器与构建步骤，目标是解决浏览器对 TypeScript 支持不足的问题。
- 🔧 **工作原理**：同步 XHR 抓取 TS 代码 → SWC（WASM）转译成 JS → 自定义 ESM 转 CJS 转换 → eval 执行，从而绕过浏览器的原生 import 系统。
- 📥 **安装与引入**：通过 importmap 引入 `https://unpkg.com/tsbro`，可同时映射 `preact` 等远程依赖。
- ✍️ **用法示例**：先用模块脚本 `import { register } from 'tsbro'` 并调用 `register({ jsx: 'preact' })` 设置 JSX pragma；再在 `<script type="text/tsx">` 中直接编写 TSX 并导入本地文件（如 `./App.tsx`），也支持 `src` 属性引入外部文件。
- 📦 **远程包支持**：因为绕过了标准导入机制，可以直接通过 importmap 使用 npm 远程包（如 preact），无需先下载或构建。
- ⚠️ **类型缺失问题**：不安装 npm 包时 TypeScript 无法找到模块类型；解决办法是创建环境声明文件 `env.d.ts`，内容为 `declare module '*'`。
- 🐛 **已知缺陷**：由于代码经过转译与 eval，堆栈跟踪没有文件名且行号混乱，目前尚无解决方案。
- ⚙️ **推荐配置**：建议的 `tsconfig.json` 包含 `"jsx": "preserve"`、`"noEmit": true` 和 `"allowImportingTsExtensions": true` 等选项。
- 📄 **其他信息**：项目基于 MIT 许可证，在 GitHub 上已获 71 星，另有姊妹项目 tssw 可关注。

---

### [获取失败](https://recs.page/web-tools-weekly?ref_code=a082baf699&lc=link_campaign_0286c16e2f8b&email=<<subscriber@example.com>>)

**原文标题**: [Failed to retrieve](https://recs.page/web-tools-weekly?ref_code=a082baf699&lc=link_campaign_0286c16e2f8b&email=<<subscriber@example.com>>)

无法总结：获取内容失败，状态码 403。

---

### [简介 | pnpm](https://pnpm.io/pnpr/)

**原文标题**: [Introduction | pnpm](https://pnpm.io/pnpr/)

概述：pnpr 是一个用 Rust 编写的、兼容 pnpm 的 npm 注册表服务器，可托管私有包并代理上游注册表，同时提供认证与访问控制，旨在替代或补充 Verdaccio 等工具。其核心设计是每个包名唯一解析到一个注册表源，从根本上防止依赖混淆攻击。目前处于实验阶段。

- 🔬 实验性项目：pnpr 仍在积极开发中，行为、配置与 API 可能随版本变化。
- 🦀 技术基础：用 Rust 实现，原生支持 npm 注册表协议，兼容 pnpm、npm、yarn 等客户端。
- 📦 核心功能：既可作为私有注册表托管组织内部包，也能作为缓存代理镜像 npmjs.org 等上游源。
- 🔑 凭证网关：服务端持有上游令牌，通过自身认证分发给团队，客户端无需接触敏感凭据。
- ⚡ 安装加速器：可在服务端解析依赖图，为 pnpm 直接生成可用锁文件，提升安装速度。
- 🧩 与 pnpm 的关系：pnpr 是独立服务器产品，但特意与 pnpm CLI 协同设计，可让 pnpm 卸载解析任务。
- 🛡️ 安全设计：每个注册表源明确声明其服务的包名，路由将包名唯一映射到单个源，杜绝跨源回退，从结构上消除依赖混淆攻击。
- 📜 许可限制：采用 PolyForm Shield License 1.0.0，属“源代码可用”而非开源；允许运行、修改和自托管，但禁止提供与其竞争的产品。这是 pnpm monorepo 中唯一非 MIT 许可的部分。

---

### [](https://github.com/moumen-soliman/crust)

**原文标题**: [GitHub - moumen-soliman/crust: The production-build diff for Next.js. Compare two App Router builds, understand what changed and why, and decide what can ship. · GitHub](https://github.com/moumen-soliman/crust)

crust 是一个面向 Next.js 生产构建的开源 diff 工具，通过比较同仓库的两个 App Router 构建快照，帮助开发者发现路由、缓存、静态壳和客户端字节的变化，并定位根因，最终给出“是否可以发布”的判断。当前处于 pre-alpha，适合 Next.js 15/16 + App Router 项目。

- 🔍 核心功能：对比两个生产构建（例如 main vs feature），输出决策（BLOCK/REVIEW/CLEAR/CANNOT DECIDE），而不是简单列出路由变化。
- 📉 变更聚焦：可捕获“某路由不再静态”“缓存读失效”“组件离开静态壳”“首载 JS 增长”等回归，并给出最可能的修复动作。
- 🧩 原因去重与爆炸半径：同一包、客户端边界或调用点若影响多条路由，会合并展示，而不是重复刷屏。
- 📦 快速开始：需要先完成 next build，再通过 `npx @moumensoliman/crust init` 初始化；npm 包名为 @moumensoliman/crust，且要求 Next.js 15/16、App Router、Node 20+。
- ⚙️ 命令设计：支持 analyze / diff / ci / report / mcp / ask 等；`diff --build` 能在临时 git worktree 中构建两个 ref，无需切分支或干净工作区。
- 🛡️ 可当合并门禁：crust ci 会按基线或 .perf/budgets.json 约束进行阻断，例如渲染模式降级、未缓存读取、静态壳消失等；预算文件可设置默认首载字节上限、最大增长比例等。
- 🔬 证据归因：结合构建产物与源代码，给每条结论标注 verified/inferred/unknown；要追踪客户端字节到模块/包，则需开启 productionBrowserSourceMaps，否则只报“不可用”。
- 💾 快照机制：每次分析将快照存到 .perf/，并通过 orphan perf-history 分支同步；路由按页面文件身份而非 URL 匹配，支持 URL 重构后仍可比较。
- 🤖 Agent/LLM 集成：提供 read-only MCP 工具，供 Claude 等编码代理查询快照，直接回答“为什么 /dashboard 不再是静态”等问题；crust 本身不带模型或密钥。
- 📊 与 Next.js Bundle Analyzer 的区别：Bundle Analyzer 擅长单次构建的模块图，crust 则比较两次构建的渲染模式、缓存决策、静态壳组成、配置与 JS 变化，并回答“什么变了、为什么、影响谁”。
- 🚫 非目标提醒：不是运行时 APM/错误追踪，不出综合评分，只支持 Next.js App Router（Pages Router 会提示），不是托管服务，也不会修改打包过程。

---

### [包](https://pack.sh/)

**原文标题**: [pack](https://pack.sh/)

pack 是一个自托管应用部署工具，通过一条命令即可将应用构建为单文件可执行程序，并部署到自有服务器，提供持久 HTTPS 链接。它省去构建管道和容器配置，支持多种运行环境，并通过闲置休眠与自动恢复来节省资源。

- 🚀 只需运行 `pack` 命令，即可完成部署并获取持久的 HTTPS 网址。
- 🖥️ 支持 Linux/macOS 及 Windows 的本地安装，也提供服务器端一键安装脚本。
- 📦 将项目构建为单文件可执行程序，部署过程无需额外服务器更新或构建流水线。
- 🔒 每次部署生成持久且不可变的实例，并自动处理端口分配（`process.env.PORT`）。
- 😴 非活跃部署会自动休眠，在收到请求时自动恢复；旧部署超过 30 天无活动则被删除。
- 🌍 支持静态 HTML、Node.js (20.6.0+)、Bun、Deno、Go、Zig、Rust、C/C++ 等。
- ⚖️ 相比 Vercel 等托管平台，它让你在自有 VPS 上获得相似的部署体验；相比 Dokku 等平台，它更轻量，无需 Docker/容器构建。

---

### [联系 Web Tools Weekly](https://webtoolsweekly.com/contact?opt=classifieds)

**原文标题**: [Contact Web Tools Weekly](https://webtoolsweekly.com/contact?opt=classifieds)

概述摘要：这是 Web Tools Weekly 的广告联系页面，说明广告咨询方式、可选的广告方案，以及非广告类询问的替代联系渠道。用户需填写包含姓名、邮箱、广告 URL 及所选计划的表单。

- 📢 如需广告合作，可先查看“Advertising Plans”页面了解选项，并通过发送消息询问当前档期。
- 📝 所有广告咨询必须使用下方表单，填写姓名、邮箱、广告链接、意向计划及备注。
- 🎯 可选广告方案包括：顶部广告 + 顶部文字链接、付费产品评测、中部图片广告、文字链接组合、分类列表、广告互换。
- ✉️ 关于新闻通讯的一般问题或提交工具，请勿使用此表单，而应通过 X 私信、Bluesky 聊天或订阅后回复邮件联系。
- ⚠️ 此表单仅用于广告咨询，其他提问或工具提交将被引导至替代渠道。

---

### [](https://boxes.dev/)

**原文标题**: [boxes.dev](https://boxes.dev/)

您未提供需要总结的文章内容。请发送文本，我将按以下格式为您生成中文要点：

overview summary  
- 📌 待收到内容后，我会提取关键信息并添加合适表情符号。

---

### [学习 Visual Studio Code](https://lazarpress.gumroad.com/l/learnvscode)

**原文标题**: [Learn Visual Studio Code](https://lazarpress.gumroad.com/l/learnvscode)

overview summary  
目前您尚未提供需要摘要的文章內容，因此無法產出條列式重點。請先貼上文字，我將依照指定格式整理。  

- 📩 請提供文章或段落內容，以便進行後續摘要。  
- ✍️ 收到內容後，會使用「-」符號搭配表情符號，列出簡潔重點。  
- 🔍 摘要將涵蓋關鍵資訊與核心觀點，幫助快速掌握全文。

---

### [](https://www.latticegrid.dev/)

**原文标题**: [JavaScript Data Grid, Licensed Per Domain | Lattice Grid](https://www.latticegrid.dev/)

overview summary  
该文介绍 Lattice Grid v1.23.0：一款按域名授权而非按开发者授权的 JavaScript 数据表格，无需框架即可运行，支持海量行、虚拟列、服务端及流式数据，并内置编辑、类型解析、诊断、图表、演示模式等功能。

- 🧩 纯 JavaScript 数据表格，无框架依赖，可用同一套代码运行于 React、Vue、Svelte、Angular 或纯 HTML 页面。  
- 💰 按域名授权（每个域名 1000 美元），不限制开发者人数；支持通配符域名授权，本地开发、CI、预览分支免费但带水印。  
- ⚡ 支持百万行、虚拟列、服务端与流式数据源；仅需一个样式表和一个脚本即可开始使用。  
- ✏️ 内置丰富编辑功能：单元格内联编辑、拖拽填充、Excel 粘贴、批量编辑、校验、统一撤销栈、整行编辑及 22 种编辑器。  
- 🔢 列类型化：数字、货币、单位、时长、IPv4、日期、JSON 等；按解析后的值排序、筛选、汇总，而非按显示文本。  
- 🛡️ 错误诊断不静默失败：错误设置会明确指出问题，同时保留安全默认值继续渲染。  
- 📊 内置分析能力：35 种图表、统计值（中位数、百分位数）、以及跟踪数据变化的“影子列”。  
- 🖥️ 面向日常使用者：演示模式、保存视图、单元格评论、四套主题、Excel 导出、全键盘操作。  
- 🔒 支持列脱敏、屏幕共享前保护敏感数据、标注、全屏模式，便于展示与协作。  
- 📦 所有功能免费构建，无功能限制；按部署域名收费，支持无限开发者、承包商与构建代理。

---

### [Mathify —](https://mathify.dev/)

**原文标题**: [Mathify — AI Math Animation Maker for Education & Content Teams](https://mathify.dev/)

Mathify 是一款面向严肃制作场景的 AI 数学动画工具，可将文字提示直接转化为可用于课程、教学、营销与产品内容的数学动画，并支持 API 集成与交互式 3D 探索。

- 🎬 将一句话提示生成完整数学动画，适用于课程、频道、课堂与内容流水线。
- 📊 内置示例涵盖正弦波、抛体运动、指数增长、切线斜率、贝叶斯定理等经典主题。
- 🏫 教育公司可将课程概念与脚本批量转化为可复用动画，用于课程库与辅导讲解。
- 📣 内容与营销团队无需专业动画团队即可制作 YouTube 与短视频数学视觉。
- 🔧 开发者可通过 API 编程生成动画，接入教育应用、代理与自动化工作流。
- 🔬 教师、研究者与工程师能快速制作清晰的数学/物理/工程可视化解释。
- 🧊 在支持的场景中，生成的动画可转化为可在浏览器中旋转、缩放与检视的真实 3D 交互对象。
- ⚙️ 工作流三步完成：描述想法→生成并渲染动画→下载或通过 API 继续处理。
- 🚀 端到端系统覆盖从提示到渲染输出全流程，团队直接使用成品而非维护动画管线。

- 主要服务对象：教育公司、内容营销团队、开发者与产品团队、以及专家型用户。

---

### [获取失败](https://recs.page/web-tools-weekly?ref_code=fde5b5c207&lc=link_campaign_d8b9780aafe8&email=<<subscriber@example.com>>)

**原文标题**: [Failed to retrieve](https://recs.page/web-tools-weekly?ref_code=fde5b5c207&lc=link_campaign_d8b9780aafe8&email=<<subscriber@example.com>>)

无法总结：获取内容失败，状态码 403。

---

### [](https://opaquer.net/)

**原文标题**: [Opaquer .NET Obfuscator Source Code Protector](https://opaquer.net/)

Opaquer 是一款专业的 .NET 混淆器，旨在保护 .NET 程序集免受逆向工程、篡改和知识产权盗用。它支持从 .NET Framework 1.0 到 .NET 10 的广泛版本，提供字符串加密、控制流混淆、命令行批量处理等功能，并被视为 Skater .NET Obfuscator 的现代继任者。产品提供免费 Basic 版以及 Pro/Enterprise 付费版，满足不同开发团队的防护需求。

- 🛡️ 专业混淆防护：有效阻止黑客攻击、代码篡改和未经授权的逆向工程，保护软件安全。
- 🔑 广泛版本兼容：支持 .NET 10 以及 .NET 1.0 至 4.8 全系列，可混淆任意 .NET DLL/EXE。
- 🔐 字符串加密保护：对程序集中的字符串值进行加密，防止敏感逻辑被轻易反编译获取。
- 🚫 阻止去混淆工具：内置反逆向机制，防止常见 DEOBFUSCATION 工具的分析与破解。
- ⚙️ 命令行与批处理：可在 GUI 中配置程序集后，通过命令行批量处理，适合自动化构建和定时更新。
- 📜 继任 Skater 技术：作为 Skater .NET Obfuscator 的下一代产品，继承了成熟可靠的混淆基因。
- 💻 环境依赖要求：需安装 Visual Studio 2010 或更高版本（推荐 2026），并需 .NET 10 环境；处理旧框架程序集时还需对应 Framework。
- 💰 版本与价格方案：Basic 免费（基础功能）；Pro 售价 $189.99；Enterprise 售价 $489.99，均为终身授权，含高强度的控制流混淆、团队部署及无联网构建支持。

---

### [获取失败](https://dirstarter.com/)

**原文标题**: [Failed to retrieve](https://dirstarter.com/)

无法总结：获取内容失败，状态码 403。

---

### [](https://x.com/darrenjr/status/2085214022568124763)

**原文标题**: [darren on X: "the terminal is NOT the right interface for coding with agents 

can we please all agree on this" / X](https://x.com/darrenjr/status/2085214022568124763)

该帖作者认为，终端并不是与 AI 代理协作编程的理想界面，并呼吁大家就此达成共识。该言论在社交媒体上引发广泛关注。

- 💻 明确指出“终端不是与代理进行编码的正确界面”
- 🤖 暗示当前开发工具需要适配 AI 代理时代的新交互方式
- 🗣️ 公开呼吁：“我们能不能都同意这一点？”
- 📈 该帖引发热议，获得约 49.8 万次浏览和大量互动

---

### [路易斯·拉扎里斯（@LouisLazaris）/ X](https://x.com/LouisLazaris)

**原文标题**: [Louis Lazaris (@LouisLazaris) / X](https://x.com/LouisLazaris)

这是一位名为 Louis Lazaris 的推特/X 用户个人资料摘要，涵盖其账号简介、常用链接及社交数据，展示了一位科技内容创作者兼通讯创始人的线上形象。

- 👤 账号 @LouisLazaris，共发布 5,248 条帖子，关注 717 人，拥有 5,452 位粉丝。
- 😄 个人简介自称“Chairman of the Bored”，带有自嘲式幽默。
- 📬 创办了两份科技新闻通讯：webtoolsweekly.com 和 techproductivity.co。
- 🔗 另运营个人网站 impressivewebs.com，并在 bio.link/louislazaris 聚合各站链接。
- 📅 账号于 2009 年 5 月加入推特。
- 📍 所在地以“Torontocisco, Canadafornia”的玩笑方式混合标注多伦多、加拿大与加州。
- 🗂️ 页面设有帖子、回复、转推、媒体等分类内容区域。

---

### [](https://bsky.app/profile/louislazaris.com)

**原文标题**: [@louislazaris.com on Bluesky](https://bsky.app/profile/louislazaris.com)

overview summary  
这是一位前端开发者和资讯策展人在 Bluesky 上的个人资料简介，列出了其专业身份、相关网站及兴趣爱好。

- 👨‍💻 主要身份是前端开发者和资讯策展人，个人网站为 louislazaris.com
- ⚙️ 维护 Web Tools Weekly（webtoolsweekly.com），专注分享前端开发工具与资讯
- 💼 运营 Tech Productivity（techproductivity.co），关注技术效率提升
- 💻 开设 VSCode.email（vscode.email），提供与 VS Code 相关的邮件内容
- 🎸 在 YouTube 上开设频道 @tunejotter，面向吉他爱好者分享内容
- ⚠️ 该 Bluesky 页面为高度交互式 Web 应用，必须启用 JavaScript 才能正常使用；平台相关详情见 bsky.social 与 atproto.com

---

### [向 Web Tools Weekly 投稿工具](https://webtoolsweekly.com/submit)

**原文标题**: [Submit a Tool to Web Tools Weekly](https://webtoolsweekly.com/submit)

该内容说明如何向作者推荐前端开发工具，并列出可提交的类型与联系方式。

- ✉️ 可通过 X（@LouisLazaris）或 Bluesky（@LouisLazaris.com）私信提交工具
- 🧩 可提交库、框架、插件、脚本、Web/桌面/移动应用、API/服务及编辑器/IDE 等
- ❌ 不接受文章或教程投稿
- 📋 生产力相关工具需投递至其另一通讯《Tech Productivity》

---

### [获取失败](https://codepen.io/jcoulterdesign/pen/NOMeEb)

**原文标题**: [Failed to retrieve](https://codepen.io/jcoulterdesign/pen/NOMeEb)

无法总结：获取内容失败，状态码 403。

---

### [](https://webtoolsweekly.com/)

**原文标题**: [Web Tools Weekly | A Weekly Newsletter for Front-end Developers](https://webtoolsweekly.com/)

Web Tools Weekly 是一份面向 Web 开发者的每周邮件通讯，目前有超过 1.5 万名订阅者；页面重点展示了订阅方式、隐私声明，以及大量读者好评，强调其内容实用、值得长期订阅。

- 📧 每周发送一封邮件，目前已有 15,537 位订阅者。
- 🔒 订阅即表示同意相关条款与隐私政策，并说明会通过 EmailOctopus 进行数据存储与追踪。
- 🛡️ 网站受 reCAPTCHA 保护，并适用 Google 隐私政策与服务条款。
- ⭐ 读者普遍认为该通讯“内容优质”“值得推荐”，是了解新工具和库的好渠道。
- 💡 多位订阅者特别提到其中的 JS 技巧很有价值，能带来自身想不到的思路。
- 📬 有读者表示已连续订阅多年，每周必读，是“最好的技术通讯之一”。
- 👍 众多读者自发推荐，称其帮助自己发现了大量实用且常用的开发工具。

---

