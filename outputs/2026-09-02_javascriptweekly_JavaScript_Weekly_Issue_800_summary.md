### [](https://yui.dev/blog/minesweeper-in-247-bytes)

**原文标题**: [The Depths of JavaScript: Minesweeper in 247 Bytes](https://yui.dev/blog/minesweeper-in-247-bytes)

本文介绍作者将经典扫雷游戏压缩到仅 247 个字符 JavaScript 的代码高尔夫过程，并详细拆解了各种压缩技巧、位运算妙用和最终实现原理。

- 🎮 用 247 个字符实现浏览器扫雷，具备随机 8×8 棋盘、左键开格、右键标旗、递归展开空白格和胜利检测。
- 🧩 代码从 658 字节逐步压缩，作者与 DNEK 合作降至 247 字节，且未移除任何主要功能。
- 🔧 利用 HTML 解析器自动闭合 `<p>` 和 `<a>` 的规则，省略所有关闭标签，节省大量字节。
- 🖱️ 使用单个 `onmouseup` 事件配合 `event.which` 区分左右键，通过 XOR 切换未打开/旗标状态，但牺牲了右键菜单阻止。
- 🗄️ 将函数 `b` 和 `m` 当作对象来存储可见棋盘与地雷状态，用 `??=` 在初始化时随机生成地雷并更新安全格计数。
- ⚡ 大量使用位运算（`^`、`|`、`~`）和类型强制转换，实现紧凑的边界检查、递归条件和邻地雷计数。
- 📐 用一维数组存储二维棋盘，借助隐藏列和越界返回 `undefined` 处理边缘，邻居偏移量写成 `[~9,..."1172711",~9]`。
- 🔄 递归打开空白格通过 `b(b[i=j]^1|e)` 实现，利用短路逻辑同时完成边界判断、旗标过滤和零雷扩展。
- 🏁 该版本被认为接近理论极限，但 Kolmogorov 复杂度不可计算，未来仍可能存在更小实现。
- ✨ 作者视代码为艺术，享受纯粹娱乐编程，并借此寻求支持与远程工作机会。

---

### [AI 代码审查 | CodeRabbit | 免费试用](https://www.coderabbit.ai/?utm_source=newsletter&utm_medium=email&utm_campaign=creator_program&utm_term=cooperpress&utm_content=ad-cooperpress-002&ref=cooperpress&dub_id=jfh8Z3stMsGQOlFK)

**原文标题**: [AI Code Reviews | CodeRabbit | Try for Free.](https://www.coderabbit.ai/?utm_source=newsletter&utm_medium=email&utm_campaign=creator_program&utm_term=cooperpress&utm_content=ad-cooperpress-002&ref=cooperpress&dub_id=jfh8Z3stMsGQOlFK)

该提交为团队邀请功能加入角色管理，新增邀请 API、邮件通知及管理员权限控制，涉及 10 个文件。

- 🔧 新增邀请 API 与邮件发送功能
- 📋 提供创建、列表、接受邀请的端点
- 🔑 支持邀请令牌生成
- 📧 发送邀请确认邮件
- 🔒 仅允许组织管理员（ADMIN）执行邀请操作
- 📁 修改权限检查、邀请服务与路由等核心文件

---

### [Remix 3 候选版本 | Remix](https://remix.run/blog/remix-3-release-candidate)

**原文标题**: [Remix 3 Release Candidate | Remix](https://remix.run/blog/remix-3-release-candidate)

overview summary
2026 年 8 月 31 日，Remix 3 发布首个候选版本（RC），距 Beta 预览已过去 4 个月。团队在此期间大幅扩展功能，涵盖数据库工作流、全栈 HMR、改进的资产服务、类型安全路由、扩展 UI 库及 SPA 支持等。官方强调 Remix 作为单一依赖的全栈框架，基于 Web 原语构建，对 AI 代理友好，并宣布将于 10 月 2 日的 Remix Jam 上正式发布。

- 🚀 发布 Remix 3 首个候选版，正式版定于 10 月 2 日 Remix Jam 推出
- 🗄️ CLI 内置完整数据库工作流：迁移、填充、状态检查、重置、回滚
- ⚡ 全栈热更新（HMR），服务器模块重载并就地更新兼容 UI 组件
- 📦 改进的未打包资源服务，支持 JS、CSS、图片、字体及 npm 包预加载
- 🧭 更安全、更快的路由匹配与 URL 生成，支持组合式路由和增强 TypeScript 推断
- 🧩 扩展 UI 库，新增标签页、开关、上下文菜单等组件
- 📱 SPA 支持，将路由器、中间件、控制器及请求 - 响应模型带入客户端渲染应用
- 🔧 新增 remix.json 配置数据库、资产、测试，并附带 remix doctor 及资产检查工具
- 🤖 强调对 AI 代理友好：基于 Web 原语、类型安全、将 UI 状态视为 JavaScript 作用域
- 📦 单个 remix 依赖即可构建全栈应用，减少 package.json 攻击面，且各组件可替换（如 Zod、Drizzle）
- 🧹 RC 阶段停止新增功能，专注修复 bug、安全审计、优化文档并收集反馈
- 🎯 官方示例：`npx remix@next new my-remix-app`可体验，并推荐查阅文档、官网源码及 Discord

---

### [](https://remix.run/)

**原文标题**: [Remix - The Fully-Stacked Web Framework](https://remix.run/)

Remix 是一个基于 Web 标准的全栈框架，将服务器运行时、路由、数据、认证、UI、资产编译等能力整合到一个统一的包里，强调更少的概念和更高的可理解性，适合现代 Web 应用开发。

- 🧩 一站式框架：一条命令 `npx remix@next new my-app` 即可获得从服务器到前端所需的完整工具链。
- ⚙️ 服务器与运行时：基于 Fetch 的 HTTP 服务器，支持跨现代 JavaScript 运行时的可移植 Web API。
- 🛣️ 路由与中间件：提供类型化路由、控制器、请求上下文和可组合中间件，统一模型。
- 🗄️ 数据与数据库：运行时校验，支持 SQLite、PostgreSQL、MySQL 的类型化关系数据。
- 🔐 认证与会话：内置认证、OAuth、Cookie、会话、存储适配器及安全中间件。
- 🎨 UI 与样式：服务端渲染、HTML-first Frames、可组合样式、可访问组件、表单和动画。
- 📦 资产与开发：TypeScript、JSX、CSS 按需编译，支持 HMR 和官方 CLI。
- 💾 文件与存储：流式上传、Web 标准 File API、本地存储和 S3 集成。
- 🧪 测试与生产：自带测试框架、日志、压缩、静态文件和生产服务器工具。
- 🧠 更小的心智模型：全栈贯穿标准 Web API，运行时优先，包可独立采用，模型一致。
- 🔄 重新思考最佳实践：状态用普通 JS 变量或对象管理，显式 `update()` 更新；支持 mixin、可见客户端边界、HTML over the wire、HTTP 即接口、按需编译和原生模块缓存。
- 🤖 对人机都友好：行为可透过普通代码追踪，默认层可替换，并有 Remix skills 辅助编码代理。
- 🚀 快速上手：提供逐步指南和 API 文档，也可订阅月度更新保持了解。

---

### [](https://pnpm.io/blog/releases/12.0)

**原文标题**: [pnpm 12.0 | pnpm](https://pnpm.io/blog/releases/12.0)

pnpm 12.0 是 pnpm 的 Rust 重写稳定版，并非迁移：命令、标志、设置和锁文件格式与 pnpm 11 兼容；本文介绍了安装方式、破坏性变更、新特性、关键修复与反馈渠道。

- 📦 安装需通过 `pnpm self-update next-12`，Homebrew、winget、Scoop 等暂未提供。
- 🔧 Git 依赖改为“仓库身份”解析，统一走主机 HTTPS URL，SSH 不再直接记录，可用 git config 重写。
- ⚠️ `pnpm-workspace.yaml` 中无法识别的设置现在会报错或警告，并给出最接近的拼写建议。
- 🔄 循环依赖图的锁文件生成已规范化，字节一致，peer 解析性能提升 2–3 倍、内存降低约 25%。
- 🔗 Linux 上 `packageImportMethod:auto` 优先硬链接（btrfs 更快），ext4 不变，macOS 保持 clone-first。
- 🛡️ `engineStrict` 改为按依赖边检查，即使整棵子树挂在 optionalDependencies 下，常规依赖不兼容也会失败。
- 🖥️ 项目感知的全局 bin：全局安装的 node/deno/bun 会跟随项目版本，由 `globalShims` 配置，并带信任提示。
- 📥 pnpm 现在可安装并调用其他包管理器（npm、Yarn Classic/Berry/6、Bun），用于 git 依赖、`pnx` 和 shim。
- 📝 新增注册表修订（registry revisions），允许替换已发布版本并记入锁文件，`pnpm update --patches` 可刷新。
- 🎯 `pnpm init` 改为固定最新发布版 pnpm，而不是当前运行版本；离线等情况回退旧行为。
- ✅ `pnpm stage approve` 支持批量审批 staged 包，整个批次只需单个 OTP，并按依赖顺序处理。
- 🧹 新增 `audit.ignorePrune`，让 `pnpm audit --fix` 清除已不再出现的忽略 GHSA 条目。
- 🚫 全局修改类命令在 sudo 下拒绝运行，返回 `ERR_PNPM_SUDO_NOT_SUPPORTED`。
- ☁️ 远程副作用缓存（PoC）通过 pnpr 共享构建产物，仅 Linux/glibc x64/arm64 支持恢复。
- 🛠️ 修复：兼容性数据库移除静态分析条目；无可用上级链接时 store 放入 `<project>/node_modules/.pnpm-store`；`filterLog` hook 已弃用。
- 📣 反馈：如遇问题请前往 GitHub 报告。

---

### [pnpm 12 有什么不同 | pnpm](https://pnpm.io/blog/whats-different-in-pnpm-12)

**原文标题**: [What's different in pnpm 12 | pnpm](https://pnpm.io/blog/whats-different-in-pnpm-12)

pnpm 12 是基于 Rust 的重写，不改变原有命令、标志、设置和锁文件格式，但有以下七项关键差异，其中一项移除的标志会导致直接报错。

- 🔧 全局安装的 node、deno、bun 现在会遵循当前项目固定的版本，无需单独版本管理器；由 globalShims 设置控制。
- 🔗 Git 依赖（GitHub/GitLab/Bitbucket）的 specifier 不再区分传输方式，统一通过主机规范 HTTPS URL 解析，锁文件不再记录 SSH URL；旧锁文件需用 pnpm update 重新解析。
- 📦 指定包管理器时直接安装真实工具（npm、Yarn Classic/Berry/6、Bun），而非同名 npm 包；全局包管理器在项目有固定版本时优先使用项目版本。
- 🔄 依赖循环的锁文件现在按包 ID 固定断点，锁文件仅由依赖图决定；重复安装或重排条目产生字节一致的锁文件，循环多的 workspace 性能提升。
- ⚡ Linux 上 packageImportMethod:auto 默认先尝试硬链接再 reflink，btrfs 上安装速度约提升一半；macOS 仍优先 clonefile。
- ⚠️ engineStrict 下，若常规依赖边指向不兼容包，即使整个子树挂在 optionalDependencies 下也会失败；可跳过但不可检查的规则不变。
- ❌ `pnpm install --resolution-only` 标志在 pnpm 12 中不存在，会直接报错；请改用 `pnpm peers check` 读取锁文件中的 peer 问题。

---

### [](https://github.com/microsoft/TypeScript/pull/63931)

**原文标题**: [Support import attributes on ambient modules by gabritto · Pull Request #63931 · microsoft/TypeScript · GitHub](https://github.com/microsoft/TypeScript/pull/63931)

该 PR（microsoft/TypeScript#63931）为模式（pattern）ambient module 声明加入 import attributes 支持，使 `declare module "*" with { type: "css" } { ... }` 能按导入属性的类型匹配模块，并已合并进 TypeScript 7.1。

- ✅ 新增语法：允许在模式 ambient module 上使用 `with { type: "css" }` 等属性声明。
- 🔍 匹配规则：导入声明的 attributes 类型需“可指派（assignable）”至 ambient module 声明的 attributes 类型，例如 `{ type: "sqlite", embed: "false" }` 可匹配 `{ type: "sqlite" }`。
- 🎯 最具体类型优先：若存在多个匹配模块，会选择 attributes 类型最具体（strict subtype）的声明。
- 📦 解析优先序：当导入带有非空 import attributes 时，会优先解析到 pattern ambient module，而非实体 `.d.*.ts` 文件；无 attributes 时维持原有行为。
- ⛓️ 类型限制：目前 attributes 类型只能是带字符串字面量类型的普通属性，避免 `"exact" | "approximate"` 这类模糊匹配。
- 🔀 合并行为：只有 attributes 类型完全相同的 pattern ambient module 才会合并；不同 attributes 使用 mangled symbol 名称区分。
- 🚫 模块扩充：带 attributes 的 pattern ambient module 暂不支持 module augmentation 套用。
- 📄 无实体文件不报错：解析到 pattern ambient module 时，即使磁盘上不存在对应文件（如 `./missing-file.css`）也不会报错。
- 🧩 其他变更：允许 type-level import 使用 import attributes；auto-import 暂不支持；`with {}` 等同于未指定 attributes。
- 🔮 未来工作：考虑在标准库中加入 `{ type: "css" }` 等声明，但目前因覆盖与兼容问题暂不加入。

---

### [Svelte 新动态：2026 年 9 月](https://svelte.dev/blog/whats-new-in-svelte-september-2026)

**原文标题**: [What’s new in Svelte: September 2026](https://svelte.dev/blog/whats-new-in-svelte-september-2026)

本月 Svelte 5.57 带来了 SvelteMap 新方法、表单与上下文相关的质量改进；SvelteKit 3 进入 RC 阶段并持续完善；sv CLI 新增迁移工具和 ai-tools；社区也涌现出大量新应用、组件库与学习资源。

- 🆕 Svelte 5.57：SvelteMap 新增 `getOrInsert` 和 `getOrInsertComputed` 方法，简化“读取或初始化”模式。
- 🔍 `createContext` 现在返回第三个 `has` 函数，可安全检查上下文是否已设置，避免触发 `get` 错误。
- 🔽 `<select>` 支持 `defaultValue` 属性，表单重置时可恢复为默认值。
- 🧾 `svelte/server` 新增 `RenderOutput`、`SyncRenderOutput`、`Csp`、`Sha256Source` 类型，便于服务端渲染输出与 CSP 类型标注。
- 🚀 SvelteKit 3 RC：跨页表单动作现在会在成功或失败时导航到动作页，更贴近原生表单行为（破坏性变更）。
- ⚙️ Adapter Vite 插件支持 `pre` / `post` 分组，并新增 `applyReroute` 助手，适配拆分式 serverless 部署。
- 🧪 路由现在会自动忽略文件名中含 `test`、`spec` 或 `stories` 的 `+` 前缀文件，避免测试文件变成路由。
- 📄 `+server.js` 支持导出 `QUERY` 方法处理器；`defineParams` 及相关类型移至 `@sveltejs/kit/params`。
- 🛠️ sv CLI：原 `mcp` 加装被更通用的 `ai-tools` 取代，可配置 Svelte 插件或按客户端选择 MCP 服务、技能等。
- 🔄 `sv migrate` 重构，新增 `sveltekit-3` 迁移任务：自动升级依赖、将 `$lib` 重写为 `#lib`，并输出无法自动迁移的改动清单。
- 🧭 新项目默认使用 `#lib`（Node 子路径导入）以匹配 SvelteKit 3；`svelte-check` 与 `svelte2tsx` 已适配新的扁平配置结构。
- 🌐 社区应用：EdenText（本地文档编辑器）、Kraa.io（极简发布平台）、Note by Note（音乐伴侣扩展）、Roomy（AT 协议群聊）、Taxing Wages（OECD 工资税计算器）等。
- 🎨 组件与工具：Svelte DataTables Components、SVAR Calendar/Kanban、MUKADE UI、Material Svelte、morphicons、Amicro SV、loadersz 等丰富设计资源。
- 📚 框架与开发工具：ogygia（SvelteKit SSR islands）、TanStack Table v9 Svelte 原生适配、Wait0（动态缓存）以及多篇技术文章和播客内容。

---

### [](https://astro.build/blog/whats-new-august-2026/)

**原文标题**: [What’s new in Astro - August 2026 | Astro](https://astro.build/blog/whats-new-august-2026/)

Astro 2026 年 8 月更新亮点：新项目管理员接任、Astro 7.2 正式发布、社区活动精彩纷呈，还有众多新站点、工具与主题亮相。

- 🤝 团队变动：Matthew Phillips 接任 Astro 项目管理员，前任 Fred 获得感谢。
- 🚀 Astro 7.2 发布：带来实验性增量静态构建、`astro preview` 后台模式、相对 logger 入口等新功能。
- 🏢 大型采用者：Evil Martians、Microsoft TypeSpec Azure、Microsoft Orleans 等知名公司正在使用 Astro。
- 🌐 趣味网站：Open Apps、Madeira 徒步路线、sandwich maxxing 等站点展示 Astro 的多样可能性。
- 🎨 视觉盛宴：Cosmic Canvas 收录了多个动画流畅、视觉效果惊艳的网站（如 Achim Loobes、Infinite Semantic）。
- 📅 社区活动：Vue Fes Japan、ViteConf 2026 有 Astro 成员参与；9 月 5 日 Astro Together 首次在德国威斯巴登举办。
- 🧪 开发体验：新增 GitHub 社区支持仓库和基于 Svelte 的 Astro Playground，方便快速测试组件。
- 🏆 黑客松：Webflow × CodeTV 联合挑战赛圆满结束，获奖网站已公布。
- 🤖 合作伙伴动态：ImageKit 推出 Astro 官方集成；CloudCannon 连通 Astro 多语言翻译工作流。
- 📚 社区文章精选：包括 Astro 维护者分享将 GitHub issue 清零的方法、Webflow 迁移案例、内容集合设计、构建提速 64.7% 等。
- 🛠️ 工具与集成涌现：新增行为模块、SEO 审计工具、Cookie 同意横幅、Starlight 插件等数十个社区项目。
- 🧩 主题模板丰富：Astro Palette、8-BitQuest、Develi、Scholarly 等大量新主题上线或更新至 v7。
- 🌍 站点展示：新增数十个 Astro 网站，覆盖商业、医疗、教育、娱乐、房产等多个领域。
- 📖 Starlight 文档：如 Astro LilyPond、WinUtil 文档等使用 Starlight 构建的实例被收录。

---

### [](https://play.astro.build/)

**原文标题**: [Astro Playground](https://play.astro.build/)

概述：您尚未提供需要总结的文本，无法生成摘要。
- 📝 请发送文章内容，我将按照模板为您提取要点并添加适合的表情符号。

---

### [发布 Rspack 2.2 - Rspack](https://rspack.rs/blog/announcing-2-2)

**原文标题**: [Announcing Rspack 2.2 - Rspack](https://rspack.rs/blog/announcing-2-2)

overview summary
Rspack 2.2 正式发布，带来了性能提升、HMR 优化、更短的模块 ID、新特性、更广泛平台支持及生态工具链的同步更新，同时提供了升级指南。

- ⚡ 性能优化超 30 项，生产构建时间约缩短 5%（1822ms→1725ms），CSS 解析提速约 3 倍，CopyRspackPlugin 复制大文件快 3-4 倍，Wasm 体积减少 1.1MB，SWC Wasm 插件加载时间大幅缩短。
- 🔄 改进 HMR：JS 热更新不再随样式表增大而显著变慢（原来最大约 385ms，现在约 5-6ms），并修复了 mini-css-extract-plugin 热更新时页面闪烁问题。
- 🆔 新增 compact-hashed 模块/块 ID 策略，在稳定哈希基础上选用最短前缀，相比 deterministic 可减少输出体积（真实项目 gzip 后减少约 0.87%）。
- ✨ import.meta 增强：新增 Rspack 专用变量（如 import.meta.rspackPublicPath），import.meta.glob 支持 caseSensitive 选项，可大小写不敏感匹配。
- 🌐 支持 Browserslist Baseline 查询（如 "baseline widely available" 或指定日期），便于按基线特性集锁定目标浏览器。
- 🖥️ 新增 Linux RISC-V 64、ppc64le、s390x 架构的原生预编译绑定，减少对 Wasm 回退的依赖。
- 📦 Rsbuild 2.2 同步发布：支持 import attributes 导入文本、Node.js 构建默认启用 chunk splitting（真实案例服务端输出减少 98%，内存减少 73%）、支持 Solid v2 RC（Rust 编译器快 20 倍以上）、新增 Octane 模板、动态端口、自定义压缩配置和自定义重启逻辑。
- 🧪 Rstest 新增 Module Federation 远程模块测试、Playwright E2E 测试支持，以及预打包测试环境（jsdom 测试时间减少 37.8%，happy-dom 减少 53%）。
- 🔍 Rslint 内置超 500 条规则并实现全部 @typescript-eslint 规则和预设，defineConfig 提供完整类型提示，内置常用全局变量，并新增与 ESLint v10 对齐的 JavaScript API。
- 📚 Rslib 0.23.2 支持 TypeScript 7 生成声明文件（快 5-10 倍），Rslib 1.0 RC 已发布，稳定版即将推出。
- 🤖 Rspress 获得 AFDocs 的 Agent 友好评分 100/100，支持 llms.txt、SSG-MD、text/markdown 等特性；Rstack 发布 Agent 插件，兼容 GitHub Copilot、Codex、Cursor。
- ⚠️ 升级注意：Rspack 2.2 升级 swc_core 至 77，SWC Wasm 插件需重建或升级至兼容版本；RSC 插件不再包装 Client References，改用 React preinit 加载 CSS，集成方需同步升级 react-server-dom-rspack 至 0.1.0。

---

### [Cypress 16：更快的测试，从 HTTP/2 支持开始](https://www.cypress.io/blog/cypress-16-faster-tests-starting-with-http2-support)

**原文标题**: [Cypress 16: faster tests, starting with HTTP/2 support](https://www.cypress.io/blog/cypress-16-faster-tests-starting-with-http2-support)

overview summary
Cypress 16 是一次以性能为核心的重大更新，默认启用 HTTP/2、加快输入与可见性检查、改进内存管理以减少长测试崩溃，同时移除 Cypress.env() 以增强安全性，并包含多项破坏性变更及迁移指南。

- 🚀 HTTP/2 支持：在 Chromium 浏览器中默认开启，请求并行加载，1,000 张图片从 3,896ms 降至 1,362ms；SSE 等流式功能变得可测试。
- ⌨️ 输入提速：`cy.type()` 的默认按键延迟改为 0ms，可全局或按命令恢复原值。
- 👀 可见性检查优化：新算法减少布局抖动，可用 `visibilityStrategy: 'legacy'` 回退旧行为。
- 🍪 减少 flake：`cy.getCookie()`、`cy.getCookies()` 等改为查询命令，自动重试直到断言通过。
- 🧠 内存管理默认开启：`manageBrowserMemory` 替代实验配置，在 Chromium 中自动触发 GC，防止渲染进程崩溃。
- 🛠️ 基础升级：Node.js 24、Electron 41、Chromium 146；组件测试支持 Vite 8、Angular 21/22。
- 🔒 安全强化：移除 `Cypress.env()`，改为异步 `cy.env()` 和同步 `Cypress.expose()`，避免敏感环境变量进入浏览器。
- ⚠️ 破坏性变更：Electron 弃用、移除 `cy.exec()` 和 `cy.end()`、限制 `viewportWidth`/`blockHosts` 运行时配置、CoffeeScript 及旧版框架不再支持。
- 📖 迁移指南：提供完整迁移步骤和 AI 助手 prompt，可自动检查 Node/框架版本、更新依赖并定位需修改的代码。
- ❓ 常见问题：包括 HTTP/2 对 `cy.intercept()` 传输细节的影响（如不报告 `httpVersion`、压缩头解码）、恢复旧打字/可见性行为的方法等。

---

### [](https://trilon.io/blog/nestjs-12-is-now-available)

**原文标题**: [NestJS v12 is Now Available - Trilon Consulting](https://trilon.io/blog/nestjs-12-is-now-available)

概述：NestJS 12 正式发布，这是该框架多年来最重要的一次平台更新，涵盖核心框架、CLI、默认工具链与文档，带来 ESM 优先支持、可选的 CJS/ESM 项目生成、Rspack 取代 webpack、Standard Schema 原生支持、结构化日志、可读错误码、可观测性 SDK 以及多项微服务和生态改进，同时发布全新官网与迁移指南。

- 🚀 核心包全面转向 ESM-first，但现有 CommonJS 项目可通过 `require(esm)` 无缝升级，无需强制迁移。
- 🔀 `nest upgrade` 新命令可自动更新依赖并保留原有模块格式；`nest new` 会让用户选择 CJS 或 ESM 项目。
- ⚡ 新 ESM 项目默认使用 Vitest 和 oxlint；CJS 项目继续使用 Jest 与 ESLint，`@nestjs/testing` 保持 runner 无关。
- 🧱 webpack 工作流在 CLI 中被弃用，Rspack 成为 monorepo 默认打包器；`tsc` 仍是标准项目的默认编译器。
- 🛠️ CLI 新增 `--emit-declarations`、`--no-type-check`、`--silent`、`--parallel` 等选项，并加入 `nest deploy` 命令。
- ✅ 路由参数装饰器（`@Body()`、`@Query()`、`@Param()`）支持 Standard Schema，可直接集成 Zod、Valibot、ArkType。
- 📦 `@nestjs/config` 的 `validationSchema` 现接受任意 Standard Schema 对象，Joi 仍可用但需升级至 v18+。
- 📝 `ConsoleLogger` 支持将对象作为结构化参数输出，JSON 模式下可嵌套 `params` 或通过 `flattenParams` 展开。
- 🏷️ `HttpExceptionOptions` 新增 `errorCode` 属性，可向 API 响应输出稳定的机器可读错误码。
- 🧭 路由冲突诊断新增 `routeConflictPolicy` 和 `routeResolutionStrategy`，可检测并处理路由遮蔽或重复问题。
- 👀 官方 `@nestjs/observe` SDK 通过 `instrument` 选项集成，自动采集请求、后台任务、错误、日志和分布式追踪。
- 📡 微服务更新：支持 NATS v3、Kafka 正则主题匹配、处理器前置钩子，以及 gRPC 专用异常过滤器。
- 🔌 GraphQL 默认使用 GraphiQL，移除 `subscriptions-transport-ws`，全面转向 `graphql-ws`。
- ⚙️ WebSocket 网关支持 request-scoped 模式和断开原因回调；Express 应用新增优雅关闭能力。
- 📅 NestJS 12 要求 Node.js v20.19+ 或 v22.12+，并伴随全新设计的官网和文档上线。
- 🔁 从 v11 迁移只需运行 `nest upgrade`；可选迁移到 ESM 需添加 `"type": "module"`、`nodenext` 模块解析和显式 `.js` 扩展名。
- 💡 ESM 迁移没有截止日期，CommonJS 项目会继续得到完整支持，可逐服务按需推进。

---

### [](https://github.com/vuejs/core/blob/minor/CHANGELOG.md#360-rc6-2026-08-28)

**原文标题**: [core/CHANGELOG.md at minor · vuejs/core · GitHub](https://github.com/vuejs/core/blob/minor/CHANGELOG.md#360-rc6-2026-08-28)

overview summary
Vue 3.6 核心变更日志，重点记录了 Vapor Mode（一种新的编译模式）的完整开发历程，从 alpha 到 RC 阶段，包含大量 bug 修复、性能优化、新特性以及关于 Vapor Mode 的详细说明（如启用方式、互操作限制、特性兼容性等）。

- 🚀 Vapor Mode 是 Vue 3.6 引入的新编译模式，旨在减小包体积并提升性能，性能与 Solid 和 Svelte 5 相当。
- 🔧 Vapor Mode 为 100% 可选功能，支持 `<script setup vapor>` 或 `<template vapor>` 标记，且仅支持组合式 API。
- ⚡ 纯 Vapor 应用使用 `createVaporApp()` 创建，可避免引入虚拟 DOM 运行时；与 VDOM 应用混用时需安装 `vaporInteropPlugin`。
- 🧩 Vapor 与 VDOM 组件可通过 interop 插件互相嵌套，但仅覆盖标准 props、事件和插槽，仍存在边缘问题，建议保持区域分离。
- 🚫 Vapor Mode 不支持 Options API、`app.config.globalProperties`、`getCurrentInstance()`（返回 null）、`@vue:xxx` 事件、`v-memo` 等。
- 🧪 自定义指令在 Vapor 中使用新接口：`VaporDirective` 接收 reactive getter 作为值，可通过 `watchEffect` 设置响应式副作用并返回清理函数。
- ⚠️ 在 Vapor 中直接调用 `slots.default()` 不是安全检查，会执行渲染逻辑并产生副作用，应避免用于判断插槽内容。
- 📅 版本更新从 3.6.0-alpha.1（2025-07-12）持续到 3.6.0-rc.6（2026-08-28），逐步完善了 Hydration、Transition、KeepAlive、Teleport、Suspense 等支持。
- 🔧 大量修复集中在 runtime-vapor、compiler-vapor、hydration 等方面，涵盖属性回退、插槽锚点、过渡组、异步组件、KeepAlive 缓存等细节。
- ⚡ 性能优化包括事件委托改为 opt-in（使用 `.delegate` 修饰符）、基于 alien-signals 重写 reactivity 核心、减少不必要的分配和副作用追踪等。
- 🎯 Vue 3.6 中 reactivity 系统基于 alien-signals 进行了重构，显著提升了性能和内存效率。
- 📌 3.6.0-rc.1 开始进入 RC 阶段，Vapor Mode 功能完整；rc.6 为最新版本，包含多个 Vapor 相关修复和性能优化。
- 📚 日志末尾附有旧版 changelog 链接（3.0.x 至 3.5.x），供追溯历史版本。

---

### [发布 v2.9.6 · denoland/deno · GitHub](https://github.com/denoland/deno/releases/tag/v2.9.6)

**原文标题**: [Release v2.9.6 · denoland/deno · GitHub](https://github.com/denoland/deno/releases/tag/v2.9.6)

Deno 发布 v2.9.6 版本，主要包含新增功能、多项修复与性能优化，涵盖桌面端、HTTP/网络、Node 兼容性、npm 集成及核心稳定性等方面。

- 🆕 新增功能：支持 `text/x-component` 压缩类型；桌面端新增剪贴板 API；菜单项支持选中状态、图标和工具提示。
- 🐛 桌面端修复：修复 macOS bundle 签名、应用名称含点号时的解析、错误对话框阻塞 JS 线程、Vite HMR 服务器运行在桌面运行时等问题；同时将 `deno.json` 中的版本和许可证信息传播到安装包。
- 🌐 HTTP/网络修复：将 HTTP/2 最大头列表大小提升至 256KB；修复代理传输权限检查、连接池重试逻辑、响应发送后请求体仍可读、多部分边界必填等多项问题。
- 🧩 Node 兼容性修复：修复 require 解析检查、Brotli 编码器操作校验、原始 HTTP 头校验、crypto 二进制密钥导出口令、TLS 客户端会话恢复、readv 短读及 `inspector.open` 权限等问题。
- 📦 npm 相关修复：修复 peer 依赖回退匹配、`--cached-only` 时缓存元数据使用、tar 路径校验、裸 npm 说明符解析，并移除 `arrayref` 依赖。
- 🛠️ 其他修复：涵盖权限检查中已解析 IP 的拒绝列表、Windows 进程参数 NUL 字符校验、发布流程对私有包和 JSR 包名验证、REPL 输入验证、glob 忽略规则解析及格式化时尊重 `.editorconfig` 等。
- ⚡ 性能优化：优化 op driver 的 future arena 按需增长、AsyncRefCell 无竞争借用快路径、SafeArrayIterator 索引式迭代、零拷贝快照反序列化、base64 编码/解码，以及 WebSocket 创建 future 的缩小等。

---

### [发布 v12.0.0 · mochajs/mocha · GitHub](https://github.com/mochajs/mocha/releases/tag/v12.0.0)

**原文标题**: [Release v12.0.0 · mochajs/mocha · GitHub](https://github.com/mochajs/mocha/releases/tag/v12.0.0)

Mocha.js 于 2026 年 8 月 31 日发布了 v12.0.0 版本，主要包含功能修复、文档更新和项目维护等改动。

- 🐛 修复了解析负数及带引号字符串时的问题
- 🔧 修复了重新生成进程时保留 FIFO 描述符的问题
- 📚 修正了文档中一些小的正确性问题
- 🔗 将文档链接从 wiki 更新为指向 mochajs.org
- 🧹 为 v12 稳定版配置了 Release Please 自动化发布流程

---

### [](https://www.electronjs.org/blog/electron-44-0)

**原文标题**: [Electron 44 | Electron](https://www.electronjs.org/blog/electron-44-0)

overview summary
- 🚀 Electron 44 正式发布，带来 Chromium 152、V8 15.2 与 Node v24.18.1 的核心升级。
- 📋 剪贴板模块重构为 W3C 标准，新增异步 API 与 ClipboardItem 类，渲染进程不再直接暴露该模块。
- 🪟 新增跨平台窗口状态持久化 API，可保存窗口位置、大小与显示模式。
- 🐧 Linux 集成显著改进：恢复徽标/进度条支持，新增透明度与系统主题图标。
- ⚠️ 多项破坏性变更：移除 macOS 12、Windows 32 位与 Linux 32 位 ARM 支持，ANGLE 静态链接等。

- 🎯 安装方式：`npm install electron@latest` 或从 releases 网站下载。
- 🔄 剪贴板 API 改为异步，新增 `ClipboardItem`，Linux 选区剪贴板通过 `clipboard.selection` 访问。
- 🔒 渲染进程不再直接使用 `clipboard`，需改用 `navigator.clipboard` 或经 preload 的 `contextBridge` 暴露。
- 💾 `windowStatePersistence` 选项可自动保存/恢复窗口状态，并支持 `clearPersistedState()` 清除。
- 📊 Linux 恢复 `app.setBadgeCount()` 和 `win.setProgressBar()`，无需 libunity，支持 LauncherEntry D-Bus。
- 🎨 Linux 无边框窗口支持系统主题标题栏图标，并新增 `win.setOpacity()`。
- ⚙️ 技术栈升级：Chromium 152.0.7977.54、Node v24.18.1、V8 15.2。
- ➕ 新增 `net.WebSocket`（主进程 WHATWG 兼容客户端）。
- 🔍 新增 `webContents.setZoomMode()` 等逐 WebContents 缩放控制。
- 🖨️ 新增 `webFrameMain.printToPDF()`，支持主进程打印单帧为 PDF。
- 🔢 macOS 14+ 菜单项支持 `badge` 属性显示徽标。
- ⚡ 启动时间与 IPC 性能优化，改进了 Linux 启动流程、PGO 配置与 Node 快照。
- 📦 Linux 发行包体积减少约 37 MB。
- 🧩 首个沙箱化 BrowserWindow 可预启动 renderer 进程，加速多窗口应用。
- 🗑️ 移除 macOS 12 (Monterey) 支持，需 macOS 13+。
- 🔐 `select-client-certificate` 事件中 `webContents` 可能为 null，需检查参数。
- 📚 ANGLE 改为全平台静态链接，不再附带 libEGL/libGLESv2 动态库。
- 🚫 `net.request` 拒绝非 navigate 模式的 frame 类型请求。
- 🐧 移除 Unity 桌面环境支持与 `app.isUnityRunning()`。
- 🖥️ 停止发布 Windows x86 与 Linux ARM (armv7l) 预构建二进制。
- ✂️ 剪贴板模块的 `readImage`、`writeHTML`、`availableFormats` 等辅助方法移除，需参考迁移指南。
- 🧹 移除 pre-macOS 13 登录项属性（如 `openAsHidden`）。
- ⏳ Electron 41.x.y 已停止支持，建议升级至新版本。
- 📌 未来将继续跟进 Chromium、Node、V8 的更新，详情见公开时间线与计划破坏性变更页面。

---

### [](https://nodejs.org/en/blog/release/v26.8.0)

**原文标题**: [Node.js — Node.js 26.8.0 (Current)](https://nodejs.org/en/blog/release/v26.8.0)

overview summary
Node.js 26.8.0 当前版本于 2026 年 8 月 26 日发布，带来多项新功能、性能优化与稳定性改进，涵盖加密、SQLite、网络、流处理、测试运行器等模块，并提供各平台安装包。

- 🔐 **加密增强**：更新根证书至 NSS 3.126，并支持 SIV 与 GCM-SIV 加密模式。
- 🧮 **直方图升级**：改进 histogram 实现，并新增统计假设检验功能。
- 🌐 **网络性能**：优化 `net.BlockList` 性能，提升处理效率。
- ✨ **REPL 改进**：新增基础语法高亮，提升交互体验。
- 🗄️ **SQLite 扩展**：新增 `StatementSync.prototype.close()` 与 `Symbol.dispose()` 支持，便于资源管理。
- 🧰 **工具增强**：`util` 新增非抛错 `MIMEType.parse`，简化解析流程。
- 📦 **Zlib 新特性**：引入 `ZipEntry`、`ZipFile` 和 `ZipBuffer`，增强压缩归档能力。
- ⚡ **性能优化**：多处改进包括缓冲读写、URL 解析、流处理和文件系统操作。
- 🧪 **测试与稳定性**：测试运行器增加点号报告器、标签过滤 DSL，并修复多项崩溃与边界问题。
- 🔧 **构建与工具链**：更新依赖（如 zlib、simdjson、undici），支持 Power 9/z14 及新增 PGO 脚本。
- 📥 **下载信息**：提供 Windows、macOS、Linux、AIX 等全平台安装包与校验和。

---

### [](https://nodejs.org/en/blog/release/v24.20.0)

**原文标题**: [Node.js — Node.js 24.20.0 (LTS)](https://nodejs.org/en/blog/release/v24.20.0)

Node.js 24.20.0（LTS，代号“Krypton”）于 2026 年 8 月 26 日正式发布。该版本带来了多项新特性、性能优化与依赖更新，重点包括异步作用域支持、权限系统增强、stream/iter 实现以及 WebAssembly JSPI 启用，并同步发布了各平台安装包与校验和。

- 📦 发布 Node.js v24.20.0 LTS，代号“Krypton”，属于长期维护版本
- ✨ async_hooks 为 AsyncLocalStorage 新增 `using` 作用域支持，简化异步上下文管理
- 📝 buffer 模块为 indexOf / lastIndexOf 等方法新增 `end` 参数，提升切片查询灵活性
- 🔐 权限系统新增 `permission.drop` API 和 `--permission-audit` 审计模式，便于动态权限控制与安全检查
- 📂 loader 实现 package maps，优化包导入映射解析
- 🌊 新增 `node:stream/iter` 实现，改善流迭代的性能与背压处理
- 🧪 test_runner 新增 `context.log()` 与 `test:log` 事件，并在 TestStream 事件中报告 `entryFile`
- ⚡ WebAssembly 启用 JSPI（JavaScript Promise Integration），支持更高效的异步 Wasm 互操作
- 🚀 QUIC 模块大量改进：支持 TLS 证书压缩、主机名验证、会话创建速率限制、流空闲超时等
- 🔄 依赖更新：npm 升至 11.19.0，根证书同步至 NSS 3.125，并更新 ngtcp2、nghttp3、zlib、sqlite 等
- 🐛 修复 crypto、http、stream、net、tls、sqlite、zlib 等模块的多个 bug 与崩溃问题
- 📚 文档与工程改进：新增合作者 MikeMcC399，调整 CI 与工具链，优化文档结构
- 💾 提供 Windows、macOS、Linux、AIX 等多平台安装包与二进制文件，并附 SHA256 校验和

---

### [](https://resend.com/blog/email-verification-api)

**原文标题**: [The Email Verification API · Resend](https://resend.com/blog/email-verification-api)

该文介绍了一种新的浏览器 API 提案——Email Verification API，它可在浏览器内直接验证用户邮箱所有权，省去跳转收件箱的步骤，从而提升体验并减少无效邮箱地址。文章说明了其工作原理、前端与服务器实现方式、当前支持状态以及应用价值。

- ✉️ 传统邮箱验证需打开收件箱找验证码或链接，新 API 让用户无需离开页面即可完成验证。
- 🔄 流程涉及用户、浏览器（客户端）、邮箱提供商（签发方）与服务器（验证方），通过隐藏 token 实现归属校验。
- 🔑 实现时需在表单中加入`type="email"`与`autocomplete="email"`，并添加带随机 nonce 的隐藏 token 输入。
- 🖥️ 服务器端可借助作者提供的 npm 包（`email-verification-api`）解析 DNS、校验签名，快速验证 token。
- 🧪 该 API 目前处于提案阶段，仅 Chrome（通过 origin trial）与 Gmail 支持，适合作为渐进增强功能提前试验。
- 🛡️ 验证邮箱能减少硬退信、防止冒用地址，同时保护发件人信誉，让订阅/注册流程更顺畅。
- 📌 若需在 API 不可用时，可参照其他邮箱验证 API（语法、MX 记录、SMTP 检查）作为备选方案。
- ⭐ 想跟进进展可给 GitHub 仓库加星，或关注 Chrome 开发者博客；试运行可查看作者提供的示例应用。

---

### [](https://lovable.dev/blog/how-we-migrated-lovable-dev-away-from-nextjs)

**原文标题**: [How we migrated lovable.dev away from Next.js and turned it into another Lovable app | Lovable](https://lovable.dev/blog/how-we-migrated-lovable-dev-away-from-nextjs)

lovable.dev 是一个月访问量超 4200 万、拥有近 400 条路由和 91 万行代码的复杂网站。团队将其从 Next.js 迁移到自家平台使用的 TanStack Start，通过双框架并行、AI 辅助代码迁移和分阶段流量切换，最终实现“用 Lovable 开发 Lovable”的完全自举，并获得了性能、工具链和自编辑能力等多重收益。

- 🏠 背景：lovable.dev 月独立访客超 4200 万，包含近 400 条路由、91 万 + 行非生成代码，支持 150+ 代理工具，甚至内置小型 IDE，现已作为普通应用托管在 Lovable 平台上，仅剩不到 200 行服务路径专属代码。
- 🐶 核心动机：最大原因是“dogfooding”——亲身体验用户痛点以缩短反馈循环；同时希望挑战单应用极致扩展，并将最佳实践反馈给 builder agent，让所有用户受益。
- 🧩 迁移策略：放弃“大爆炸式重写”，改为让 Next.js 和 TanStack Start 并行运行，由代理 worker 按路由和用户分发请求，实现逐路由渐进迁移。
- 🗂️ 分组与平滑切换：按用户旅程划分迁移组，组内通过 feature flag 控制百分比逐步放量；利用 CSS 的 View Transitions API 让硬导航不再闪白，体验更接近软导航。
- 🔗 代码共享架构：目标将 90–95% 代码沉淀为框架无关核心，通过 `#shared/` 别名、lint 规则禁止导入任一框架，并用“平台适配器”实现接口级依赖注入，最终 Next.js 专属代码仅占 3%。
- 🤖 AI 辅助迁移：从“agents 起草 PR、负责人审查”演变为“agents 自主完成并直接合入”，配合可量化指标、规划代理批量拆分任务、以及自动审查新代码的可移植性，最终仅一名开发者带领一群 agents 完成迁移，团队其他成员几乎无感知。
- 📊 流量切换：每个路由组按“内部测试→全公司→1%→100%”分阶段 A/B 放量，同一时间只允许一个外部 rollout 爬坡，整体约两个月完成，大部分时间仍在并行迁移代码。
- 💥 OOM 事故：因未提前测量内存占用且忽略早期 0.1% 错误率警告，静态 JSON 数据使 V8 isolate 超限，错误率 11 分钟内飙升至 50%；回滚远比定位根因快，教训是必须关注内存指标并果断回滚。
- 🔧 内存优化三板斧：不在模块层解析多 MB 静态 JSON（改为请求时解析，内存降低 2–12 倍）；剔除列表 API 中不需要的字段；在 server bundle 中替换客户端专属代码为空 stub，节省约 9MB bundle（≈18MB worker 内存）。
- ⚖️ TanStack Start 体验：本地开发启动快（10s vs 70s）且内存低（1.5GB vs 8GB+）；抽象更少、更直观，几乎没有 Next.js 中服务端组件/操作等令人困惑的概念。
- 🤖 Agent 友好度：TanStack Start 训练语料一致且新，agents 第一次就能给出正确方案；而 Next.js 因版本差异大、网上资料混乱，agents 常产生过时的误导性建议。
- 🔍 代价与配置：TanStack Start 在大型应用下需要大量底层 bundler 配置（当前 17 个自定义构建插件），而 Next.js 开箱即用；但 agents 擅长这类优化，只要识别需求后指派即可。
- 📈 最终收益：用户侧中位 TTFB 下降 49%（长尾经优化后较原始仍快 16%），Web Vitals 持平；生产构建从 12+ 分钟降至 6–9 分钟，且还有进一步优化空间。
- ✨ 自编辑能力：统一技术栈后，Lovable 团队可用 Lovable 直接编辑 lovable.dev 并实时预览，已成为非技术员工自助修改公司官网的主要方式，开发者也在日常使用。
- 🚀 未来计划：基于现有可运行任意代码的沙箱 VM，Lovable 计划支持用户导入并编辑任意现有软件，包括 Next.js 应用——尽管刚刚迁移离开它。

---

### [](https://svar.dev/blog/building-data-grid-in-react-vue-svelte/)

**原文标题**: [How We Built a Fast Data Grid in React, Vue, and Svelte | SVAR Blog](https://svar.dev/blog/building-data-grid-in-react-vue-svelte/)

overview summary
- 📊 本文分享 SVAR 团队在 React、Svelte 和 Vue 中构建高性能数据网格组件的经验，核心发现是：性能瓶颈几乎与框架无关，框架间真正差异比想象中更窄，文章不判定胜负。
- 🐌 直接渲染大量 DOM 节点（如 10,000 行）会让所有框架同样卡顿，浏览器 DOM 操作是最慢环节，JS 计算次之，框架自身开销占比极小。
- 🧩 通过“框架无关核心 + 薄集成层”架构，将数据、布局逻辑与框架解耦，便于维护和测试；虚拟化是性能基线，只渲染可视区域行/列。
- 📏 初始测量存在“先有鸡还是先有蛋”问题：用 ResizeObserver 等待容器尺寸；React 的 useLayoutEffect 可优化首帧，但实际仍需回退到 ResizeObserver。
- ♻️ 三个框架的派生状态机制（useMemo、$derived、computed）使用方式几乎一致，可逐行翻译；React 需手动写依赖数组，Svelte/Vue 自动追踪。
- 🔄 数据更新时，React 默认自顶向下的重算对网格不友好，需借助外部 store 直接订阅；Svelte/Vue 默认能限制子树更新，但统一用 store 更易维护。
- 🧪 性能数据：虚拟化下 10 万行仅比 1 千行多约 30ms；全量渲染时耗时增长一个数量级，三框架差距在 15% 以内，再次证明 DOM 量主导性能。
- 🛠️ 实用建议：优先虚拟化并简化 DOM；用记忆化保留重计算；重视数据流设计，用 store 替代树形冒泡；区分框架固有限制和实现失误。
- 🎯 结论：Svelte 和 Vue 默认稍好，React 也完全能做好，框架并非性能瓶颈，架构才是；相关技能可跨框架迁移。

---

### [](https://jfmengels.net/concurrent-linter-fixes/)

**原文标题**: [Problem with concurrent linter fixes](https://jfmengels.net/concurrent-linter-fixes/)

overview summary
- 🔍 文章讨论并发 linter 修复中的问题：多个自动修复同时应用时可能产生错误代码，即使每个修复单独正确。
- ⚠️ 示例中，一个修复将手动平均值计算替换为`average`函数，另一个修复删除未使用的`average`函数；同时应用导致“未知引用”错误。
- 🔄 ESLint 采用批量应用所有无冲突修复后重新分析的流程，而 elm-review 采用每次仅应用一个修复并重新分析的策略。
- ✅ elm-review 的方法虽然更慢，但能避免应用已过时的修复，确保最终代码总是有效的。
- 🤔 作者认为此问题在 ESLint 中不常见，但若未来更激进地自动删除或移动代码，将成为阻碍。
- 📝 作者的选择是每次修复后重新分析代码，虽然性能有代价，但在支持自定义规则时无法提前预测冲突。
- 🧩 文章强调，对于代码删除、重命名、移动等大幅修改的规则，并发修复可能导致严重问题，顺序修复更安全。

---

### [](https://yob.id.au/2026/09/01/major-version-bumps.html)

**原文标题**: [
    
      Bumping the major version of your Javascript library is user hostile · James Healy
    
  ](https://yob.id.au/2026/09/01/major-version-bumps.html)

本文批评了 JavaScript 库频繁升级主版本号给用户带来的沉重负担，呼吁维护者尽可能减少破坏性变更、延长主版本生命周期，并通过合理依赖策略帮助用户简化升级与安全维护。

- 📦 作者发现其 TypeScript monorepo 中竟同时使用 8 个版本的 glob、7 个版本的 minimatch 和 3 个版本的 brace-expansion，导致依赖碎片化严重。
- 🔒 这些多版本依赖在过去一年触发了数十个 GitHub 安全警报，多数虽不可利用，却消耗大量工程师时间进行排查与升级。
- ⚖️ 根本问题在于 Node 依赖系统允许同一包多版本共存，让破坏性变更看似“廉价”，但实际把升级成本转嫁给了所有下游用户。
- 🛑 呼吁维护者尽量少 bump 主版本号，即使语义化版本允许破坏性变更，也不意味着必须频繁使用，建议至少间隔 2-3 年。
- ➕ 优先采用增量式 API 扩展，用弃用代替删除，谨慎移除旧 Node 版本支持，避免无必要地更改 ESM 默认导出。
- 🌱 尽量减少运行时依赖和 peer 依赖，参考 npm 上约 47% 的流行包零依赖的做法；开发依赖则无碍用户。
- 📏 选择依赖时优先考虑主版本更新不频繁的库，并声明尽可能宽的版本范围（如`axios: ^1`），让用户能自由去重和修复漏洞。
- 🔀 可以同时依赖多个主版本（如`brace-expansion: ^2 || ^3 || ^4`），只要 API 兼容，就为包解析器提供更大灵活性。
- 🏆 表扬做得好的包：debug（4.x 自 2018）、semver（7.x 自 2019）、strip-ansi（仅 6/7）、axios（1.x 自 2022）。
- 📜 引用 semver.org 和 Mike Taylor 的观点：破坏性变更应谨慎评估成本收益，单纯提升主版本号并不能免除用户阅读文档、修改代码和验证的工作。

---

### [](https://uppy.io/blog/uppy-6.0/)

**原文标题**: [Uppy 6.0 : fewer packages, fewer moving parts, and a robust S3 Plugin | Uppy](https://uppy.io/blog/uppy-6.0/)

overview summary
Uppy 6.0 是一次以清理和简化为核心的版本更新，重点重写了 @uppy/aws-s3 插件，将多个子包合并进 @uppy/core 以消除依赖版本冲突，并改进了 Companion、Transloadit 等模块，同时加强了供应链安全，移除或废弃了部分旧功能。

- 🧹 核心重构：Uppy 6.0 主打“少包、少移动部件”，将 @uppy/utils、@uppy/store-default、@uppy/companion-client、@uppy/provider-views 四个包合并进 @uppy/core，解决重复版本导致的 bug。
- 🪣 S3 插件重写：@uppy/aws-s3 从零开始，弃用原先最多八个回调的配置方式，改为三种签名模式（getCredentials、signRequest、companionEndpoint），并支持 Cloudflare R2、MinIO、DigitalOcean Spaces 等 S3 兼容服务。
- 🧪 可靠性提升：S3 插件修复了重试、凭证过期、离线检测、暂停/恢复竞态等问题，并在 CI 中针对真实 MinIO 实例进行测试。
- 🎛️ Transloadit 状态暴露：插件将 assemblyStatus 和 lastAssemblyStatus 放入 state，允许开发者自定义进度 UI；golden-retriever 改用 IndexedDB 存储元数据，支持大 Assembly 恢复。
- 🔌 Companion 改进：OAuth token 改经 WebSocket 传输，不再依赖 window.opener；Companion 升级到 Express 5（需宿主应用同步升级），并改用 TypeScript 编写。
- 🔒 供应链加固：新依赖需发布满 7 天才可被解析，Dependabot 更新有冷却期，第三方 GitHub Action 固定到 commit SHA，安全更新可绕过冷却期。
- 🗑️ 弃用与移除：@uppy/instagram 因 Instagram API 停用而彻底移除；四个合并进 core 的包在 npm 上标记为 deprecated；provider CSS 路径迁移到 @uppy/core/provider-views/css/style.min.css。
- 🐛 其他变化：@uppy/tus 出错时不再中止请求，服务端状态和响应体可正确传递；@uppy/angular 支持 Angular 22，Dashboard 的“My Device”按钮尊重 fileManagerSelectionType，新增挪威博克马尔语等区域更新。
- 📦 版本影响：@uppy/core、@uppy/companion、@uppy/aws-s3、@uppy/tus、@uppy/components、uppy 六个包主版本号更新；使用 uppy meta 包或 CDN 的用户大多无需改动，完整迁移指南已提供。

---

### [Zod 4.5](https://zod.dev/blog/zod-4-5)

**原文标题**: [Zod 4.5](https://zod.dev/blog/zod-4-5)

Zod 4.5 正式发布，带来了性能大幅提升的 schema 预编译功能、多个实用新 API、显著的内存优化以及一系列破坏性修复。

- 🚀 **z.compile() 旗舰功能**：可将任意 Zod schema 预编译，解析速度提升约 3–9 倍，复杂 schema 收益更大；可通过 `import "zod/compile"` 自动编译所有 schema，也支持 CLI 标志和 preload 配置。
- 💳 **新增 z.creditCard() 格式**：验证 12–19 位数字，可选空格或连字符分隔，并通过 Luhn 校验和检查。
- 🧩 **新增 z.properties()**：作为 z.property() 的多属性版本，可同时检查 instanceof 对象的多个属性，如 `z.instanceof(Response).check(...z.properties({...}))`。
- 🗂️ **恢复 z.deepPartial()**：以函数形式回归，递归地将所有字段变为可选，返回值仍是 ZodObject，支持 `.shape` 和 `.extend()`。
- 🎯 **新增 .exactPartial()**：类似 `.partial()`，但使用 `z.exactOptional()`，显式传入 `undefined` 会被拒绝，匹配 TS 的 `exactOptionalPropertyTypes`。
- ⚡ **新增 z.validate() 快速验证**：直接返回布尔值，不构建 ZodError，无效输入时比 `.safeParse().success` 快最多 16 倍；另有 `z.validateAsync()` 支持异步 refinement。
- 🔄 **新增 z.input() / z.output()**：将 schema 投影到输入或输出侧，便于独立验证 codec 的两半；对不含 codec/pipe 的 schema 是 no-op。
- 📝 **新增 z.toZod\<T\>()**：根据静态类型（通常是手写或外部定义的）定义完全匹配的 Zod schema，返回值类型得到保留。
- 🔍 **新增 z.getDiscriminatedOption()**：按 discriminator 值提取联合成员，传入不存在的值会触发 TypeScript 错误。
- 🔁 **支持循环输入**：递归 schema 现在可以解析循环引用的数据；Zod Mini 需显式注册 memoizer。
- 🧠 **内存占用减少 9 倍**：通过将方法移到 prototype 并采用 memoization 模式，`z.string()` 的保留堆内存从 7.5kb 降至 784 字节。
- 🐢 **失败的解析更快**：`.safeParse()` 不再捕获堆栈跟踪，失败路径速度提升约 7.5 倍。
- 🔑 **z.object() 支持 Symbol 键**：shape 可声明 symbol 键，TS 类型会将其视为必需且校验值类型；未声明的 symbol 键仍被忽略。
- ⚠️ **破坏性修复一：datetime 必须包含秒**：`z.iso.datetime()` 不再接受 `2020-01-01T06:15Z` 这类分钟精度输入，RFC 3339 强制要求秒。
- ⚠️ **破坏性修复二：字符串长度按 Unicode 码点计算**：`.max()`/`.min()`/`.length()` 现在对 emoji 等星形字符正确计数。
- ⚠️ **破坏性修复三：record 键和交集行为对齐 TypeScript**：模式键 record 只约束匹配的键，不再误报对象自身键。
- ⚠️ **破坏性修复四：__proto__ 始终被剥离**：无论来自输入、schema 声明还是 transform，都会被移除；`.strict()` 会将其报告为 unrecognized_keys。
- ⚠️ **破坏性修复五：字符串格式更严格**：ipv6 直接校验字符集、ulid 首位限制 0-7、httpUrl 强制 RFC 1035 长度限制、emoji 正则消除指数级回溯。
- 🌐 **新增 8 种语言环境**：孟加拉语 (bn)、中库尔德语 (ckb)、印地语 (hi)、卡纳达语 (kn)、挪威尼诺斯克语 (nn)、巴西葡萄牙语 (pt-BR)、斯洛伐克语 (sk)、土库曼语 (tk)。

---

### [使用方法记忆化将 Zod 的内存占用减少一个数量级](https://zod.dev/blog/reducing-memory-footprint)

**原文标题**: [Reducing Zod's memory footprint by an order of magnitude with method memoization](https://zod.dev/blog/reducing-memory-footprint)

overview summary
Zod 4.5 通过“方法记忆化”模式大幅降低 schema 实例的内存占用，将 z.string() 的保留堆从 7.5kb 降至 784 字节，同时保持方法自动绑定的便利性，并规避了 V8 对象自身属性存储的阶梯式开销。

- 🧠 问题根源：Zod 默认将所有方法自动绑定为闭包，导致每个实例都持有大量独立函数，无法通过原型链共享方法，内存开销巨大。
- 💡 解决方案：采用“方法记忆化”——方法定义为原型上的 getter，首次访问时绑定到实例并缓存为自身属性，之后直接命中，未使用的方法永不实例化。
- 📊 显著成果：常见 schema（如 z.string()、z.number()）内存减少 2 到 10 倍，复杂对象和管道组合优化尤为明显（最高达 9.8 倍）。
- 🔧 V8 细节：旧版 z.string() 有 49 个自身属性，触发 V8 1616 字节的备份存储；新版仅保留 6 个急切属性，其余放在原型上，避免阶梯式内存膨胀。
- 📉 实例属性急剧减少：从 49 个降至 6 个自身属性，原型上则承载 86 个方法/getter，兼顾性能与灵活性。
- 🔬 测量方法：内存数字来自仓库中的 packages/bench/memory/schema-footprint.ts 基准测试，确保数据可复现。
- 🚀 升级建议：直接升级到 Zod 4.5（npm upgrade zod@latest）即可获得这些内存优化，无需改动业务代码。

---

### [](https://expo.dev/solutions/expo-for-react-web-devs?utm_campaign=33087804-React%20to%20Native&utm_source=email&utm_medium=email&utm_term=js-weekly)

**原文标题**: [Expo for React web devs](https://expo.dev/solutions/expo-for-react-web-devs?utm_campaign=33087804-React%20to%20Native&utm_source=email&utm_medium=email&utm_term=js-weekly)

overview summary
Expo 是一个基于 React Native 的框架，让熟悉 React 的网页开发者无需学习全新工具，即可直接构建 iOS 和 Android 原生应用。它强调复用 React 技能、真正的原生渲染、多平台支持，并通过 EAS Build、文件路由、原生 API 等工具简化移动开发流程，同时提供丰富的文档与教程。

- 🚀 Expo 是 Meta 推荐的 React Native 框架，适合有 React 经验的网页开发者快速转向移动应用开发。
- ♻️ 复用 React 技能：采用相同的组件模型，大部分代码使用 JavaScript/TypeScript，现有模式与库可直接沿用。
- 📱 真正的原生体验：组件映射到 iOS 和 Android 原生 UI 元素，而非 WebView，性能与质感更佳。
- 🌐 一套代码多平台：支持 iOS、Android 和 Web，通过 Expo Router 与 API Routes 共享导航和后端逻辑。
- 🧩 内置丰富库与工具：包含 100+ 维护良好的库、顶级开发工具，以及自动化移动开发中复杂环节的服务。
- 📂 文件式路由：Expo Router 采用类似 Next.js 的文件路由方式，对网页开发者非常友好。
- 📷 原生 API 化：相机、推送通知、文件系统等原生能力以 Hooks 和组件形式暴露，调用简单。
- 🏗️ 无需 Xcode 或 Android Studio：EAS Build 和 Submit 自动处理原生构建与上架的繁重工作。
- 🔓 开源且迭代快：开源模式与快速迭代周期融合了网页开发的最佳实践。
- 📚 提供丰富资源：包括 Expo Router 文档、EAS Hosting 文档及多个从 React 过渡到 React Native 的教程。
- 💬 社区高度认可：大量开发者表达对 Expo 的喜爱，称赞其更新方便、工具优秀、体验极佳。

---

### [](https://four.htmx.org/announcements/2026-08-28-htmx-4.0.0-is-released)

**原文标题**: [htmx 4.0.0 has been released! ~ htmx](https://four.htmx.org/announcements/2026-08-28-htmx-4.0.0-is-released)

htmx 4.0.0 正式发布，历经 8 个月开发，内部从 XMLHttpRequest 迁移到 fetch()，用户可见变化不大，但带来属性继承显式化、事件命名标准化、历史记录机制调整等主要改动，并新增 morph swaps 和 `<hx-partial>` 等特性，同时提供升级工具与扩展生态更新。

- 🚀 发布公告：htmx 4.0.0 历经 8 个月开发完成，内部迁移至 fetch()，用户视角与 2.x 几乎一致，但为未来 100 年 Web 服务打下基础。
- 🔧 主要变化 1：属性继承默认改为显式，需在属性名后添加 `:inherited` 后缀，这成为从 2.x 升级的最大负担。
- 🔧 主要变化 2：事件命名统一为 `htmx:phase:action[:sub-action]` 格式，并移除部分旧事件（如 `htmx:xhr:*`、`htmx:validation:*`）。
- 🔧 主要变化 3：历史记录不再默认使用 localStorage，改为返回时重新抓取页面，并新增 `hx-history-cache` 扩展实现本地缓存。
- 🧩 新特性 1：现成支持 morph swaps（基于 idiomorph 算法），可平滑完成 DOM 变形。
- 🧩 新特性 2：新增 `<hx-partial>` 标签，用于更清晰的局部页面更新，类似改进版 out-of-band swaps。
- 🔌 扩展生态：新增 `hx-preload`、`hx-download`、`hx-alpine-compat` 等扩展，并推出 `hx-live` 前端脚本方案和 `htmax.js` 打包版本。
- 📡 流式扩展：`hx-sse`、`hx-ws`、`hx-multipart` 分别支持 text/event-stream、WebSockets 和 multipart/mixed 流式传输。
- ⬆️ 升级工具：提供 `npx htmx.org@4.0.0 upgrade-check` 命令，可自动检测属性继承、旧事件名、移除属性等问题；同时提供 LLM 技能文件辅助迁移。
- 📦 安装说明：4.0.0 可通过 CDN 或包管理器获取，但 NPM 上 2.x 仍标记为 latest，4.0 为 next，直到 2027 年初网站才会默认引用 4.0。
- ♻️ 兼容性：htmx 2 将继续获得无限期支持，用户无需强制升级；开发团队感谢所有贡献者，并附上了“升级音乐”。

---

### [变形指南 ~ htmx](https://four.htmx.org/docs/morphing-swaps-guide)

**原文标题**: [Morphing Guide ~ htmx](https://four.htmx.org/docs/morphing-swaps-guide)

概述：本文介绍了 htmx 4 中集成的 DOM Morphing 技术，包括两种 morph swap 样式、Idiomorph 算法的工作原理、如何排除特定元素、输入值与焦点的处理，以及相关配置选项。

- 🧬 DOM Morphing 通过编辑旧 DOM 以匹配新内容，保留未变节点的身份，从而保持焦点、滚动位置和视频播放等状态不中断。
- 🔄 htmx 4 直接支持`innerMorph`和`outerMorph`两种交换策略，无需额外扩展，例如通过`hx-swap="innerMorph"`实现内容平滑更新。
- 🎯 `innerMorph`只变形目标元素的子节点，`outerMorph`则变形目标元素及其子节点，分别对应`innerHTML`与`outerHTML`。
- 🗺️ Idiomorph 算法利用`id`属性映射新旧内容，以最小移动次数重建结构；建议为重要元素添加`id`以获得稳定变形。
- 🚫 使用`hx-morph-skip`可完全冻结元素（属性和子节点都不动），`hx-morph-skip-children`则只变形属性但保留子节点。
- ⚙️ 可通过`htmx.config.morphSkip`和`htmx.config.morphSkipChildren`扩展全局跳过选择器，适用于第三方组件或 Web Components。
- ⌨️ Morph 交换自动保留当前聚焦输入框的值，防止服务器响应覆盖用户输入；未聚焦输入的值仅当`value`属性变化时才会被更新。
- 🔧 配置项`htmx.config.morphIgnore`（默认忽略`data-htmx-powered`）控制不处理的属性前缀；`htmx.config.morphScanLimit`（默认 10）控制位置匹配的查找深度。

---

### [](https://four.htmx.org/announcements/2026-08-28-htmx-4.0.0-is-released#hx-partial)

**原文标题**: [htmx 4.0.0 has been released! ~ htmx](https://four.htmx.org/announcements/2026-08-28-htmx-4.0.0-is-released#hx-partial)

overview summary
- 🎉 htmx 4.0.0 正式发布，历经 8 个月开发，团队基于 fetch() 重写内部机制，但用户视角与 2.x 差异较小。
- 🔄 三大主要变更：属性继承改为显式、事件命名标准化、历史记录不再默认使用 localStorage，内部从 XMLHttpRequest 迁移到 fetch()。
- 🧩 新增两大核心特性：内置 morph 交换（idiomorph）和 <hx-partial> 标签，同时扩展生态大幅更新。
- 🛠 提供命令行升级检查工具、LLM 技能文件，并发布 htmax.js 整合包，2.x 将继续长期支持。

- 📦 版本策略：2.x 仍为 NPM latest，4.0 标记为 next，避免强制升级依赖非版本化 CDN 的用户；官网默认使用 4.0。
- 🧬 属性继承：htmx 2 中默认继承，htmx 4 需显式添加 :inherited 后缀，例如 hx-confirm:inherited，这是主要升级负担。
- 🏷 事件命名：统一为 htmx:phase:action 格式，如 htmx:beforeRequest 改为 htmx:before:request，错误事件合并，移除 xhr 与 validation 事件。
- 🗄 历史记录：不再用 localStorage 缓存快照，后退时重新抓取页面；提供 hx-history-cache 扩展以恢复 sessionStorage 缓存。
- 🔀 Morph 交换：内置 idiomorph 算法，支持平滑的 DOM 变形替换，无需额外配置。
- 📦 <hx-partial> 标签：允许在响应中声明多个目标区域的替换，类似但更清晰于 out-of-band swaps。
- 🚀 新扩展：包括 hx-preload、hx-download、hx-alpine-compat、hx-history-cache，以及流式扩展 hx-sse、hx-ws、hx-multipart。
- 🧠 hx-live 脚本：团队自研的前端脚本方案，受 Alpine.js/jQuery/hyperscript 启发，支持 DOM 基础的反应式编程。
- 📜 升级工具：运行 npx htmx.org@4.0.0 upgrade-check 可扫描模板文件，标记需要 :inherited 的属性、旧事件名和已移除 API。
- 🤖 LLM 支持：提供 htmx-guidance、htmx-debugging、htmx-extension-authoring、htmx-upgrade-from-htmx2 等技能文件。
- 🎵 团队致谢与升级音乐：感谢多位贡献者，延续惯例发布升级音乐。

---

### [](https://four.htmx.org/docs/whats-new-in-htmx-4)

**原文标题**: [What's New in htmx 4 ~ htmx](https://four.htmx.org/docs/whats-new-in-htmx-4)

htmx 4 是一次大规模更新，以 fetch() 取代 XMLHttpRequest，引入显式继承、新的交换机制与属性，同时重命名或移除大量旧 API，并新增多项用于现代 Web 开发的核心扩展。  
- 🔄 **请求引擎全面更换**：所有请求改用原生 `fetch()`，无法回退；默认 60 秒超时（可设 `defaultTimeout=0` 取消）。  
- 🧬 **继承改为显式**：需要向下继承的属性须加 `:inherited`，如 `hx-confirm:inherited`；用 `:append` 可追加而非覆盖；可用 `implicitInheritance` 回退旧行为。  
- 📨 **错误响应也会交换**：4xx/5xx 响应默认参与 DOM 交换，仅 204/304 不交换；可用 `noSwap` 或 `hx-status` 按状态码定制。  
- 🧹 **hx-delete 不再携带表单数据**：需通过 `hx-include="closest form"` 手动包含。  
- 🗑️ **历史缓存机制移除**：不再用 localStorage 缓存页面，返回时重新抓取；可用 `history="reload"` 或 `history=false` 调整。  
- 🔃 **OOB 交换顺序反转**：主内容先交换，`hx-swap-oob` 与 `<hx-partial>` 在其后按文档顺序交换。  
- 🎯 **队列修饰符移除**：`hx-trigger` 上的 `queue:` 不再生效，改用 `hx-sync` 控制请求排队。  
- 📦 **扩展加载方式改变**：直接引入脚本即可，无需 `hx-ext`；可用 `<meta>` 限制可加载扩展，注册函数改为 `htmx.registerExtension()`。  
- ✏️ **属性重命名与移除**：`hx-disable`→`hx-ignore`，`hx-disabled-elt`→`hx-disable`；`hx-vars`、`hx-params`、`hx-prompt`、`hx-disinherit`、`hx-inherit`、`hx-request`、`hx-history` 均被移除或改为配置。  
- 🔉 **事件名统一新模式**：如 `htmx:beforeRequest`→`htmx:before:request`，多数错误事件合并为 `htmx:error`，HTTP 错误使用 `htmx:response:error`；XHR 相关事件全部移除。  
- ⚙️ **配置项大量重命名**：`defaultSwapStyle`→`defaultSwap`，`timeout`→`defaultTimeout`，`historyEnabled`→`history`，`globalViewTransitions`→`transitions`，`includeIndicatorStyles`→`includeIndicatorCSS` 等；许多旧配置被删除。  
- 📡 **请求/响应头调整**：`HX-Trigger` 改为 `HX-Source`（格式 `tagName#id`），`HX-Target` 格式变化；移除 `HX-Trigger-Name`、`HX-Prompt`；新增 `HX-Request-Type`、`Accept` 头。  
- 🗑️ **JS API 精简**：移除 `addClass`、`removeClass`、`toggleClass`、`closest`、`remove`、`off`、`location`、`defineExtension`、`logAll/logNone/logger` 等，推荐使用原生方法或新 API。  
- 🌟 **新增属性**：`hx-action`、`hx-method`、`hx-query`（QUERY 请求）、`hx-config`、`hx-ignore`、`hx-validate`。  
- 🎨 **hx-swap 大幅扩展**：支持 `innerMorph`/`outerMorph` 形态交换、`textContent`、`delete`，以及 `before`/`after`/`prepend`/`append` 别名；`show`/`scroll` 修饰符改为独立键（如 `show:top showTarget:#other`）。  
- 🧯 **状态码级交换**：通过 `hx-status:422`、`hx-status:5xx` 等为不同 HTTP 状态码指定独立 swap/target/select 策略。  
- 🧩 **新增 `<hx-partial>`**：可在一次响应中针对多个元素分别设置 `hx-target` 和 `hx-swap`，是多目标更新的更显式方案。  
- 🎞️ **View Transitions 支持**：默认关闭，需 `htmx.config.transitions = true` 启用。  
- ⚛️ **JSX 兼容**：可设置 `metaCharacter`（如 `"-"`）替代属性名中的冒号。  
- 🆕 **新增 JS 辅助方法**：`htmx.timeout()`；`hx-live` 扩展提供 `take`、`forEvent`、`nextFrame`、`q`、`debounce` 等。  
- 📝 **事件自动记录**：通过 `detail.error`/`detail.warn` 控制输出到 `console.error`/`warn`，其余事件在 `logAll` 时输出到 `console.log`。  
- 📊 **事件附带上下文**：所有事件提供统一的 `ctx` 对象，包含请求/响应信息。  
- 🧰 **新增配置键**：`extensions`、`mode`、`inlineScriptNonce`、`metaCharacter`、`morphIgnore`、`morphScanLimit`、`morphSkip` 等。  
- 🚀 **核心扩展扩充**：新增 `hx-multipart`、`hx-live`、`hx-targets`、`hx-ptag`、`hx-csp`、`hx-download`、`hx-prompt`、`hx-history-cache`，并重写 SSE/WebSocket 扩展，另附 `htmx-2-compat` 兼容扩展。

---

### [](https://sveltebits.xyz/)

**原文标题**: [Svelte Bits - Animated UI Components For Svelte](https://sveltebits.xyz/)

Svelte Bits 是一个专为创意开发者打造的开源 Svelte 5 动画组件库，提供 130+ 个可直接嵌入项目的背景、文字效果、动画与 UI 模式，支持 TypeScript 和 Tailwind，并兼容 AI 编程工具。

- 🧩 提供 130+ 个组件，涵盖背景、文字效果、动画与 UI 模式，免去从零构建的麻烦
- 📂 组件按四个清晰分类组织，方便快速定位，避免在无关内容中翻找
- ⚡ 基于 Svelte 5 + TypeScript + Tailwind 构建，类型安全且样式统一
- 🤖 兼容 Cursor、Copilot、v0 等 AI 工具，可描述需求后直接插入使用
- 🚀 快速安装：支持 jsrepo 与 shadcn，组件直接进入你的代码库
- 🎨 内置丰富示例，如 DotField、ColorBends、MagicRings、Soft Aurora 等
- 💎 每款组件都提供高度可定制参数，如颜色、速度、频率、噪点等
- 🌟 开源且永久免费，是 React Bits 的 Svelte 移植版本，正在快速增长
- 📈 欢迎在 GitHub 上 Star 关注项目进展

---

### [](https://reactbits.dev/)

**原文标题**: [React Bits - Animated UI Components For React](https://reactbits.dev/)

请先提供需要总结的文本内容，因为您消息中“Use the following content:”后面没有附上任何文章。收到文本后，我会按以下模板为您生成中文概述和要点：

- 以简短的 overview summary 开头（无标题）
- 每一条要点前加一个合适的 emoji，并用“-”开头
- 内容精炼，涵盖关键信息

---

### [现代 JavaScript 事件日历](https://schedule-x.dev/)

**原文标题**: [Modern JavaScript Event Calendar](https://schedule-x.dev/)

Schedule-X 是一个现代化的 JavaScript 事件日历组件，旨在帮助开发者快速集成日历功能，是 FullCalendar 的现代替代方案。它提供丰富的免费功能（如拖放、调整大小、暗色模式等），也有付费的 Premium 版本，包含资源视图、事件弹窗等高级能力，并配套 BuildCalendar 全栈解决方案。

- 🗓️ 提供开箱即用的现代化事件日历，支持多种技术栈，显著缩短开发周期
- ⚙️ 高度可定制，支持自定义视图、插件、每日时间边界等高级配置
- 🖱️ 支持经典拖放与拖拽边缘调整事件大小，操作流畅
- 🌙 内置明暗双主题，可通过调用方法一键切换，响应式适配桌面与移动端
- 🌍 原生支持多语言（i18n），降低国际化部署门槛
- 💎 Premium 版预置复杂功能：事件弹窗表单、快速创建、资源调度视图，安装仅需约 1 小时
- 🧩 拥有丰富插件生态，包括资源调度器、时间网格视图、侧边栏、绘制模式等
- 🚀 开发口碑良好，获赞灵活性高、易于集成，且支持 React、Vue、Angular 等主流框架
- 🔗 配套 BuildCalendar 提供全栈方案，包含数据库持久化、Google 日历双向同步
- 📦 提供 MCP 服务器与 Temporal API 集成，适合高级用户和 AI 场景化扩展

---

### [版本 v9.6.0 | M](https://mantine.dev/changelog/9-6-0/)

**原文标题**: [Version v9.6.0 | Mantine](https://mantine.dev/changelog/9-6-0/)

Mantine v9.6.0 于 2026 年 9 月 1 日发布，带来新组件、图表增强、通知与富文本编辑器升级，以及多项体验优化。

- 💖 新增 OpenCollective 赞助支持，所有资金用于改进 Mantine 组件和功能。
- 🖼️ 推出 @mantine/lightbox 包：全屏媒体灯箱，支持轮播、缩放、缩略图、视频与自定义幻灯片、键盘快捷键、本地化及 Store API。
- 🔔 Notifications 支持 renderNotification 自定义渲染，并新增 layout="stacked" 堆叠式通知布局。
- ⚡ 新增 ActionBar 组件：固定底部批量操作栏，适合表格多选场景，支持分割线、关闭按钮和自定义操作。
- 📝 RichTextEditor 新增表格控制（增删行列、合并/拆分单元格）、Details 折叠区块控件和 InvisibleCharacters 格式标记开关。
- 📊 图表库新增 GaugeChart（仪表图）、WaffleChart（百分比网格图）、MatrixChart（热力图）和 CandlestickChart（K 线图）。
- 📈 常用图表支持 referenceAreas 高亮区域与 referenceDots 标记点；AreaChart 新增 stream 流图；ScatterChart 新增右侧 Y 轴。
- 🪜 Stepper 新增 labelPosition="bottom"，可将步骤标签和描述显示在图标下方。
- 🧭 Cascader 在 hover 展开时新增 safeAreaPolygon，避免斜向移动时误切换列。
- 📅 YearView 新增 renderDay 自定义日期单元格，并支持 withWeekendDays 控制周末显示。
- 📋 ResourcesMonthView 新增 withEventResize，可拖拽事件边缘调整起止日期。
- ⏱️ 日程时间网格视图新增 eventDragInterval 和 eventResizeInterval，拖拽与缩放可独立按步长对齐。
- 📦 Dropzone 升级至 react-dropzone 20：maxFiles 超过限制时改为接受部分文件，并需 Node.js 22+。
- 🎨 其他更新：ColorInput 支持 fullWidth、FloatingWindow 新增大小调整回调、PasswordInput 可见性切换可聚焦、日程视图支持背景事件交互、use-scroll-spy 支持 ref 对象。

---

### [首页 | Cropper.js](https://fengyuanchen.github.io/cropperjs/)

**原文标题**: [Home | Cropper.js](https://fengyuanchen.github.io/cropperjs/)

该内容主要介绍一个可自定义的裁剪器（cropper），强调用户能够通过简单操作自由定制，满足个性化需求。

- ⚙️ 核心特性是可定制化，支持用户按需调整裁剪器功能。
- 🪄 强调操作轻松（easily），降低使用门槛，无需复杂配置。
- 🔲 专注于“创建属于自己的裁剪器”，突出个性化与自主性。

---

### [游乐场 | Cropper.js](https://fengyuanchen.github.io/cropperjs/playground.html)

**原文标题**: [Playground | Cropper.js](https://fengyuanchen.github.io/cropperjs/playground.html)

overview summary
该内容为 Vue.js 官方文档的导航界面，涵盖指南、API、示例、版本信息、迁移说明、贡献指南及多语言支持等核心入口。

- 📖 提供“指南”板块，包含从基础到进阶的完整学习路径
- 🔧 提供“API”参考，方便查阅全部接口定义
- 🎮 提供“示例”与“Hello World”快速上手演示
- 📦 标注当前版本 2.2.0，并附有更新日志（Changelog）
- 🔄 包含“迁移”指南，帮助用户从 1.x 平滑升级
- 🤝 提供“贡献”指引，鼓励开发者参与项目
- 🌐 支持中英文切换，并可调整外观主题

---

### [](https://github.com/paulmillr/noble-curves)

**原文标题**: [GitHub - paulmillr/noble-curves: Audited & minimal JS implementation of elliptic curve cryptography. · GitHub](https://github.com/paulmillr/noble-curves)

noble-curves 是一个经独立审计、极简且高性能的 JavaScript 椭圆曲线密码学库，提供多种曲线、签名方案与高级密码学协议，并注重安全性和可审计性。

- 🔒 经过 Trail of Bits、Cure53、Kudelski Security 等独立安全公司多次审计，安全性有保障。
- 🪶 极简设计：secp256k1 gzipped 仅 15KB，通过摇树优化排除未用代码；另有 5kb 的姊妹项目。
- 🏎 针对 JS 引擎手写优化，性能出色（如 ed25519 获取公钥约 137μs/op）。
- 🔍 通过跨库、Wycheproof 向量及模糊测试，确保实现正确性。
- ➰ 支持 Weierstrass 和 Edwards 曲线：secp256k1、p256/p384/p521、ed25519/ed448、brainpool、ristretto255、decaf448、bls12-381、bn254 等。
- ✍️ 提供 ECDSA、EdDSA、Schnorr、BLS 签名，以及 ECDH、hash-to-curve、OPRF、FROST 阈值签名、Poseidon 哈希和 FFT。
- 🔖 Ed25519/Ed448支持ZIP215共识友好验证，也支持严格RFC 8032/SBS非否认模式。
- 🥈 提供与原生 WebCrypto API 一致的包装器，方法异步且兼容多种运行时。
- 📦 安装简单：npm install @noble/curves 或 deno add jsr:@noble/curves；几乎零依赖。
- 🧩 模块化子导入（如'@noble/curves/secp256k1.js'）以保持应用体积小；代码可读性强，基于 TypeScript。
- 📜 遵循多项标准：RFC 6979、RFC 8032、BIP 340、RFC 7748、RFC 9380、RFC 9497、RFC 9591 等。
- ⚙️ 暴露内部 API：Point 数学、模运算、自定义曲线构建（weierstrass/edwards），便于扩展。
- 🛡️ 安全加固：固定运算序列、标量盲化、常数时间统计验证；但 JS/GC 环境难以保证绝对常数时间，高安全场景建议用低级语言。
- 🧹 内存注意事项：Uint8Array 可清零，但 bigint 和字符串不可变，秘密可能驻留内存；需用户权衡。
- 🔏 供应链安全：PGP 签名提交、透明 CI 发布、依赖极少且锁版本，降低攻击风险。
- 🎲 随机性依赖内置 crypto.getRandomValues（CSPRNG），不自行实现熵源。
- 🔄 v2 升级为 ESM-only，需使用.js 扩展；p256/p384/p521 移至 nist 模块，有破坏性更改（如签名输入改为未哈希消息、默认 Uint8Array 格式等）。
- 🧪 测试完善：npm test，包含慢速大标量测试和常数时间测试工具。

---

### [API](https://zuplo.com/?utm_source=react_status&utm_medium=newsletter&utm_campaign=cooper_press_unified_1q&utm_content=classified_listing)

**原文标题**: [The Unified Gateway for APIs, AI, and MCP - Zuplo](https://zuplo.com/?utm_source=react_status&utm_medium=newsletter&utm_campaign=cooper_press_unified_1q&utm_content=classified_listing)

Zuplo 是一个统一的 API 与 AI 网关，通过单一可编程策略引擎管理出站 LLM 调用和入站 AI 代理（MCP）流量，提供认证、限流、预算控制、审计及货币化能力，帮助企业快速部署并保障 AI 生态的安全性、可见性和成本效益。

- 🔀 统一网关：同时管理出站 LLM 调用与入站 AI 代理（MCP）流量，所有 API、LLM 和 MCP 调用集中在同一策略引擎上执行。
- ⚙️ 可编程策略引擎：认证、限流、预算、审计等策略一次编写，双向生效，支持用户、代理、API/MCP 和 LLM 四大表面。
- 🛡️ 安全与治理：自动拦截认证失败、超限、无效 schema 和提示注入等恶意流量，减少攻击面，保护后端系统。
- 💰 成本控制：动态限流吸收流量峰值，按团队设置硬性预算上限，防止异常代理导致开支失控。
- 👁️ 全量可见性：每个调用都归属到具体用户或客户端，实时仪表板展示工具调用、延迟和错误，并支持导出到 Datadog/SIEM。
- 🤖 代理生态支持：原生支持 Claude、Cursor、Codex、ChatGPT 等代理，结合 OAuth 2.1/PKCE 实现安全认证与工具级审计。
- 💵 内置货币化：计量、定价与账单功能直接集成 Stripe，支持按请求、令牌或自定义单位计费，快速实现 API 收入。
- 🚀 快速集成：只需替换 base URL 即可接入 LLM，通过 OpenAPI 扩展将现有 API 暴露为 MCP 工具，分钟级上线。
- 📈 客户验证：帮助 Blockdaemon 节省超 70% 成本、Finsolutia 数小时启动 MCP 服务器，并服务 10 亿 + 终端用户。

---

### [PDF 数据提取：将 PDF 转换为结构化 JSON](https://developer-api.foxit.com/developer-blogs/api-guides-tutorials/pdf-data-extraction-api-structured-json/?utm_source=draftdev&utm_medium=newsletter&utm_campaign=jsweekly_20260901)

**原文标题**: [PDF Data Extraction: Turn PDFs into Structured JSON](https://developer-api.foxit.com/developer-blogs/api-guides-tutorials/pdf-data-extraction-api-structured-json/?utm_source=draftdev&utm_medium=newsletter&utm_campaign=jsweekly_20260901)

概述：本文比较了六款 DocuSign API 替代方案（Dropbox Sign、Adobe Acrobat Sign、PandaDoc、SignNow、BoldSign、Foxit eSign），并从集成速度与长期维护的六个关键标准进行评估，帮助开发者节省调研时间。

- 📊 比较范围：涵盖六款主流电子签名 API，包括 Dropbox Sign、Adobe Acrobat Sign、PandaDoc、SignNow、BoldSign 和 Foxit eSign。
- ⚡ 核心标准：以集成速度与长期维护为两大核心维度，针对开发者实际需求进行筛选。
- 🔍 评估维度：从六个关键标准（如文档、SDK、API 稳定性等）系统化对比各方案优劣。
- 🕒 节省时间：该指南旨在避免开发者耗费数小时自行研究 API 替代品的细节差异。
- 🧩 适用场景：适合正在寻求 DocuSign 替代方案、注重开发效率与后期可维护性的技术团队。
- 📈 长期视角：不仅关注初始接入便捷性，更强调 API 在长期使用中的可靠性与维护成本。

---

### [](https://www.meticulous.ai/?utm_source=jsweekly&utm_medium=newsletter&utm_campaign=26q3&utm_content=classified)

**原文标题**: [Meticulous AI - Automated Frontend Testing Without Writing Tests](https://www.meticulous.ai/?utm_source=jsweekly&utm_medium=newsletter&utm_campaign=26q3&utm_content=classified)

Meticulous 是一个自动化测试平台，核心理念是“穷尽验证、零开发者精力”。它通过录制日常开发会话、用 AI 生成并持续演进覆盖整个应用的测试套件，让开发者在合并代码前即可发现回归问题，同时彻底告别手动编写、修复和维护测试的负担。平台基于 Chromium 的确定性调度引擎消除了 flaky 测试，并借助大规模并行计算实现极速反馈，已被包括 Dropbox、Notion 在内的 100 多家组织采用。

- 📹 自动录制交互：在本地开发、staging、preview 及可选生产环境添加脚本标签，记录真实用户会话作为测试基础。
- 🧠 AI 生成测试套件：引擎追踪每个交互对应的代码分支，自动编排覆盖用户流程与边缘情况的视觉端到端测试。
- 👀 合并前风险预览：打开 PR 即可查看变更对各类工作流的影响，通过保存并回放后端响应实现无副作用、零假阳性的测试。
- 🔄 测试持续演进：新功能或边界情况出现时自动添加测试，旧测试自动淘汰，套件始终完整最新且无需人工维护。
- 🚫 彻底消除 flaky：从 Chromium 层面构建的确定性调度引擎，保证测试稳定可靠，同时具备闪电般的执行速度。
- ⚡ 高速并行测试：测试在计算集群上高度并行化，数千个屏幕的验证可在 120 秒内完成。
- 🔌 框架集成广泛：支持 NextJS、React、Vue、Angular、Nuxt、SvelteKit 等主流技术栈，可补充或完全替代现有测试体系。
- 🏢 深受客户信赖：Dropbox、Notion 等公司工程领导者给予高度评价，认为它价值极高且开发人员上手即爱。

---

### [](https://addyo.substack.com/p/agentic-skill-decay)

**原文标题**: [Mastery Still Comes From Doing the Reps - by Addy Osmani](https://addyo.substack.com/p/agentic-skill-decay)

在 AI 代理时代，任务完成不再自动等同于技能成长，“代理技能衰减”成为新挑战。作者强调，开发者必须刻意保持学习：通过提问、反思、验证和积累实战“reps”来维持专业判断力，而不能只把 AI 当作快速产出的工具。验证是能力地板，想象力是价值天花板；专家知识反而变得更重要，同时应把经验教训编码进文档、测试和规则中，让代理和自己共同进步。

- 🤖 代理能快速完成任务，但也可能“短路”学习过程，让人错失建立直觉、理解原理的机会。
- 🧠 真正的专业能力来自深度领域知识与应用判断力，需要刻意练习决策、规格制定、引导 AI 和验证结果。
- 🔍 使用 AI 时，先形成假设、多问“为什么”、阅读 diff、预测可能失败点，并偶尔手动解决问题。
- 📉 研究发现，把 AI 当“代码售货机”的初级开发者学习效果较差（测验 50% vs 手动 67%）；主动请求解释和提问者表现更好。
- ✅ 任务完成不等于学到东西；没有错误就没有反思，须主动向 AI 索要关键总结，寻找学习契机。
- 🏗️ 验证是地板，想象力是天花板：你能想到创意，但仍需专家知识去判断输出是否正确、可维护、可扩展。
- 🔐 当代理接触生产数据时，需要身份认证与审计追踪，确保每个查询可追溯到具体代理与人类（如 Teleport 方案）。
- ⚡ 代理吞吐量远超个人注意力，必须谨慎选择把有限的时间、品味和判断力投入到哪里。
- 📈 专家知识回报在上升：AI 放大了有经验者的能力，但初学者仍需通过真实犯错积累“reps”来跨越 junior 阶段。
- 📝 将每次教训写入 markdown、测试、lint 规则等，避免会话结束即遗忘；形成“双循环”让代理和自己每天进步。
- 🌐 下一代工程师依然需要领域专业知识，因为代理的工作并不完美，你必须能识别“好”的标准并察觉隐性代价。

---

### [Lean 编程语言](https://lean-lang.org/)

**原文标题**: [Lean Programming Language](https://lean-lang.org/)

Lean 是一种开源编程语言和证明助手，用于编写正确、可维护且经形式化验证的代码。它通过小型可信内核确保绝对正确性，并提供了名为“Grind”的自动化证明工具，能高效处理模式匹配、case 分析和线性不等式求解等问题。文章展示了用 Lean 定义素数、证明素数无限等示例，并介绍了多个实际项目（如 AWS 的 Cedar、ArkLib、Mathlib、Fermat's Last Theorem 形式化等），以及各界专家对 Lean 的高度评价和近期进展。

- 💻 Lean 是开源编程语言兼证明助手，能够让代码和数学证明获得机器可验证的正确性。
- ⚙️“Grind”自动化工具可高效处理复杂模式匹配、分支分析以及线性不等式系统求解。
- ✅ 极简可信内核（trusted kernel）保证数学证明、软件与硬件验证的绝对正确。
- 🔢 提供素数（IsPrime）定义，并证明“每个大于 1 的数都有素因子”以及“素数无限”。
- ➗ 递归定义阶乘，并自动证明阶乘恒正、整除等关键性质。
- 🧰 通过元编程能力可扩展语言，添加专属数学记号和新的证明自动化策略。
- 🧮 Mathlib 是 Lean 的数学库，包含超过一百万行形式化数学内容，覆盖代数、分析、拓扑等。
- 🛡️ 工业级应用：AWS 使用 Lean 形式化验证 Cedar 授权语言，确保关键安全属性。
- 🔐 ArkLib 验证 SNARKs 的密码学安全证明，Veil 则用于分布式协议的多模态验证。
- 🔧 Aeneas 利用 Rust 的类型系统简化验证，并在 SymCrypt 生产密码算法中得到应用。
- 🚀 2026 年 OpenAI、Anthropic 等机构在 Lean 上取得突破，Quanta Books 出版《The Proof in the Code》。
- 🧑‍🏫 陶哲轩等专家高度评价 Lean 能支撑大规模协作，并助力 AI 加速数学形式化。
- 🤝 Lean FRO 获得 Alex Gerko 及 Amazon、Microsoft Research 等组织的资助与支持。

---

### [](https://gruhn.me/blog/2026-08-29/)

**原文标题**: [Lean explained with TypeScript](https://gruhn.me/blog/2026-08-29/)

overview summary  
该文章以 TypeScript 类型系统类比 Lean 证明语言，深入浅出地解释了“命题即类型、证明即值、验证器即类型检查器”的核心思想，并展示了如何用 TS 类型定义真假、与或、蕴含、否定、等价等逻辑概念，最后通过德摩根定律示例说明证明过程的机械性。

- ⚙️ Lean 是一种可让数学命题被自动验证的编程语言，证明过程极其正式、严谨，但也非常繁琐。
- 🤖 LLM 能快速生成大量代码，而 Lean 负责繁琐的验证，二者“天作之合”，也让 Lean 热度大增。
- 🧠 普通软件也能从 Lean 受益，例如保证错误状态不可达、事务满足 ACID、账户不能重复扣款等。
- 🔍 Lean 验证器本质上只是一个类型检查器：命题用类型表达，证明用值表达，类型检查通过即证明正确。
- 🟦 TypeScript 也能模拟基础证明，形式为 `const 命题名: 命题类型 = 证明值`，或借助泛型函数进行类型变量包装。
- ❌ 用 `never` 表示 `false`（空类型，无值可返回）；用带单一 dummy 值的类型表示 `true`，并可直接给出证明。
- 🔗 类型级 `And<P,Q>` 通过对象 `{left:P; right:Q}` 实现，`Or<P,Q>` 通过联合类型 `{left:P} | {right:Q}` 实现，语法与 `&&`、`||` 高度相似。
- 🧷 蕴含 `P => Q` 用箭头函数类型 `(p:P) => Q` 表示，证明就是写出一个接收 P 证明并返回 Q 证明的函数。
- 🦄 `false => false` 可以证明，就像“如果你给我独角兽，我还你独角兽”，但前提条件永远不会发生。
- 🎯 Modus Ponens（肯定前件）本质上就是函数应用：给定 `P` 和 `P=>Q`，即可调用函数得到 `Q`。
- ❗ 否定不能用条件类型简单定义，因为无法处理未具体化的类型变量；应定义为 `Not<P> = (p:P) => False`，即“P 蕴含假”。
- 🔄 等价 `Equiv<P,Q>` 要求两个方向的蕴含同时成立，可用来表达逻辑定律，如德摩根定律 `!(p||q) === (!p && !q)`。
- 📜 德摩根定律的完整证明非常冗长，足以让人体会到 Lean 证明的 tedious 程度，也展示了证明过程的机械性。
- 💡 核心结论：命题=类型，证明=值，验证器=类型检查器；传统纸笔证明常跳过“显然”步骤，而这种形式化证明则极其精确且机械化。

---

### [](https://webiterate.dev/google-removed-extensions-ublock-origin-108/)

**原文标题**: [Google Has Removed Manifest V2 Extensions From the Chrome Web Store, Including uBlock Origin](https://webiterate.dev/google-removed-extensions-ublock-origin-108/)

Google 已完成将所有 Manifest V2 扩展从 Chrome 网上应用店移除的里程碑，包括广受好评的 uBlock Origin。此举影响所有依赖 Chrome 网上应用店的 Chromium 浏览器，但 Brave 浏览器通过自建后端保留了四款 MV2 扩展。

- 🗑️ Google 移除了所有剩余 Manifest V2 扩展，uBlock Origin 等知名内容拦截器被下架。
- ⏳ 在 Chrome 138 或更早版本中已安装的 MV2 扩展仍可保留，但将无法接收更新，也无法在移除后重新安装。
- 🌐 由于 Chrome 网上应用店是 Chromium 浏览器的主要扩展市场，Brave 等非 Chrome 浏览器用户也无法继续获取这些 MV2 扩展。
- 🦁 Brave 团队决定在自建后端托管 AdGuard、uBlock Origin、uMatrix 和 NoScript，方便用户直接启用。
- 🔒 Google 宣称 Manifest V3 提供更强的安全性、隐私保护和性能控制，这是其推动迁移的主要原因。

---

### [](https://aws.amazon.com/blogs/compute/introducing-public-preview-runtimes-on-aws-lambda-starting-with-node-js-26-and-python-3-15/)

**原文标题**: [Introducing public preview runtimes on AWS Lambda, starting with Node.js 26 and Python 3.15 | AWS Compute Blog](https://aws.amazon.com/blogs/compute/introducing-public-preview-runtimes-on-aws-lambda-starting-with-node-js-26-and-python-3-15/)

AWS Lambda 推出公共预览运行时，首次支持 Node.js 26 与 Python 3.15。开发者可以在正式 GA 前试用即将发布的语言版本，并通过 GitHub 提供反馈。预览运行时使用与 GA 相同的运行时标识，覆盖所有 AWS 区域，但可能包含破坏性变更，不受 SLA 与技术支持保护，不建议用于生产。正式版预计在 2026 年 10 月上游稳定后约两个月内发布，届时函数将自动升级。

- 🚀 新预览机制：AWS Lambda 首次推出公共预览运行时，今天即可使用 Node.js 26 与 Python 3.15 创建或更新函数。
- 🎯 核心目的：让开发者在 GA 前试用预发布语言版本，从而在仍可进行破坏性变更时收集反馈并改进运行时。
- 🌍 可用范围：覆盖所有 AWS 商业区域、GovCloud (US) 和中国区域；运行时标识与未来 GA 版相同（如 nodejs26.x、python3.15）。
- 📦 预览内容：基于各语言最新上游预发布版本构建，目前为直接版本升级；同时提供托管运行时和基础容器镜像（标记为 26-preview / 3.15-preview）。
- ⚙️ 支持与节奏：补丁更新节奏与 GA 运行时一致，支持 Lambda 托管实例、durable functions 等全部现有功能。
- ⚠️ 风险提示：预览期间可能出现破坏性变更；不受 Lambda SLA 和 AWS 技术支持计划保护，强烈不建议用于生产环境；每次冷启动会向 CloudWatch Logs 写入警告。
- 📉 性能与费用：初始冷启动性能可能比 GA 运行时慢，团队会在预览期优化；按标准 Lambda 费率计费，无额外费用。
- 💬 反馈渠道：通过专属 GitHub issue（Node.js 26 / Python 3.15）提交反馈，不限于 bug，也欢迎新语言特性、编程模型改进建议。
- ⏳ 转正时间线：上游稳定版预计 2026 年 10 月发布；Lambda GA 目标在上游发布后两个月内，Node.js 需等到 Active LTS 后才 GA。
- 🔄 自动升级：运行时到达 GA 后，函数自动从预览升级，无需修改配置或代码；若已通过 Runtime Management Controls 固定到预览特定版本，需手动解除固定。
- 🛠️ 入门方式：支持控制台、AWS CLI、CloudFormation、SAM、CDK，使用标准 runtime 标识即可，CDK 可用自定义 Runtime 构造。

---

### [](https://www.matuzo.at/blog/2026/html-boilerplate)

**原文标题**: [My HTML boilerplate in 2026 - Manuel Matuzović](https://www.matuzo.at/blog/2026/html-boilerplate)

这篇文章是作者对五年前 HTML 样板的一次全面更新，逐行解释了 2026 年现代 HTML 文档的基础结构，涵盖必填标签、性能优化、SEO、社交分享、PWA 等，并给出了许多可选标签的实用建议。

- 📄 作者更新了五年前的 HTML boilerplate，反映了近年 HTML 标准的变化。
- 🔧 `<!DOCTYPE html>` 仍是兼容性必需，因为 HTML 已成为活标准。
- 🌍 `<html lang>` 定义页面自然语言，对可访问性和 SEO 非常重要。
- 🚫 `class="no-js"` 可为禁用 JS 的环境提供特定样式，JS 执行时会自动移除。
- 🔤 `<meta charset="UTF-8">` 必须尽早声明，避免字符显示错误。
- 📱 viewport meta 用于响应式设计，`initial-scale=1` 可能只在旧 iOS/Android 上有必要。
- 🔠 text-scale 是新的 meta 标签，让移动浏览器尊重系统字号，但可能破坏布局，使用时需充分测试。
- 🏷️ 页面`<title>`应唯一且具描述性，会影响浏览器标签、搜索结果和书签。
- ⏳ 渲染阻塞脚本放在 CSS 之前，非渲染阻塞脚本则使用`type="module"`以延迟执行、提升性能。
- 🖨️ 提供打印样式表（`media="print"`）可以改善打印体验，节省纸张和墨水。
- 🖼️ Favicon 推荐组合：ICO 兼容旧浏览器、SVG 支持缩放和暗黑模式、`apple-touch-icon`供 iOS 设备使用。
- 📲 Web manifest（`.webmanifest`）是 Android 设备和 PWA 所需的图标与配置来源。
- 🔗 `rel="canonical"` 可防止重复内容造成的 SEO 问题。
- 📄 可提供 Markdown 替代版本（`rel="alternate"`），方便 LLM 处理并降低 token 消耗。
- 🐘 `rel="me"` 用于 Mastodon 个人资料验证，`fediverse:creator` 可在 Mastodon 分享时自动添加作者归属。
- 📝 meta description 与 Open Graph 标签（`og:image`、`og:url`）分别控制搜索摘要和社交分享预览。
- 🎨 `theme-color` 可定制浏览器界面颜色，但新版 Safari 已改为使用 body 背景色。
- ⭐ 其他可选标签包括：`og:title`、`og:description`、`og:image:alt`、`og:type`、`og:locale`、`preload`、RSS、`author`、`viewport-fit=cover`、`interactive-widget=resizes-content`和`color-scheme`等。

---

