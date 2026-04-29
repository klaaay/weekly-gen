### [JavaScript 周刊第 783 期：2026 年 4 月 28 日](https://javascriptweekly.com/issues/783)

**原文标题**: [JavaScript Weekly Issue 783: April 28, 2026](https://javascriptweekly.com/issues/783)

以下是您提供的JavaScript周刊内容的概述摘要：

- 📬 **pnpm 11.0发布**：默认设置`minimumReleaseAge`为一天，引入SQLite存储索引以加速安装，支持原生包发布和`pack-app`，并提供迁移指南。
- 🤖 **Meticulous AI测试工具**：自动创建E2E UI测试套件，提供全面覆盖，无需开发者额外努力，被Notion、Dropbox等公司使用。
- ⚡ **TypeScript 7.0 Beta**：Go语言重写，编译速度快10倍，接近生产就绪，但稳定API需等到v7.1。
- 📰 **Node.js v26.0发布**：默认启用Temporal API，基于V8 14.6升级。
- 🛠️ **Rspack 2.0发布**：基于Rust的快速打包器，性能比v1.7快10%，改进静态分析，添加实验性RSC支持。
- 🌐 **Nuxt UI 4.7**：Vue UI库新增Listbox和Prompt组件，共125+组件。
- 📖 **JavaScript新特性文章**：涵盖ES2025和ES2026的迭代器助手、`Promise.try`、`Map.getOrInsert`、`using`、Temporal等。
- 🎬 **TSRX语言扩展**：Svelte维护者创建，改进JSX，支持控制流、作用域样式，编译到React、Preact等。
- 📊 **Lightweight Charts 5.2**：专为金融数据优化的图表库，支持圆蜡烛图、箱线图等。
- 🍋 **Fresh 2.3框架**：Deno全栈框架，默认零JavaScript，支持View Transitions API和WebSocket。
- 🎵 **Chip Player JS**：在线播放器，收录30万+MIDI、追踪器、chiptune和游戏音乐文件。
- 📊 **Datatype字体**：OpenType变量字体，无需JS即可将文本表达式渲染为内联图表。

---

### [pnpm 11.0 | pnpm](https://pnpm.io/blog/releases/11.0)

**原文标题**: [pnpm 11.0 | pnpm](https://pnpm.io/blog/releases/11.0)

pnpm 11.0 版本发布，带来了多项重大更新，包括更强的安全默认设置、原生发布流程、SQLite 存储索引以及隔离的全局安装。该版本要求 Node.js 22 或更高版本，并全面转向纯 ESM 模块。

- 🔒 **安全默认设置加强**：`minimumReleaseAge` 默认设为 1440 分钟（1天），`blockExoticSubdeps` 默认启用，新增 `allowBuilds` 替代旧的构建依赖设置。
- 🗄️ **SQLite 存储索引**：引入 store v11，使用 SQLite 数据库替代 JSON 文件，减少系统调用并提升安装速度。
- 📦 **原生发布流程**：`pnpm publish`、`login`、`logout` 等命令不再依赖 npm CLI，改为原生实现。
- 🌍 **隔离的全局安装**：每个 `pnpm add -g` 拥有独立目录和锁文件，避免全局包相互干扰。
- ⚙️ **配置分离**：`.npmrc` 仅用于认证和注册表设置，pnpm 特定配置移至 `pnpm-workspace.yaml` 或 `config.yaml`。
- 🚀 **性能优化**：使用 `undici` 替代 `node-fetch`，预分配内存下载，直接写入 CAS 文件，减少重命名系统调用。
- 🛠️ **新命令与改进**：新增 `pnpm ci`、`pnpm clean`、`pnpm sbom`、`pnpm peers check` 等命令，并支持 ESM 格式的 pnpmfile。
- 🧹 **移除旧功能**：删除了 `pnpm server`、`useNodeVersion`、`hooks.fetchers` 等多项设置和命令。

---

### [动机 | pnpm](https://pnpm.io/motivation)

**原文标题**: [Motivation | pnpm](https://pnpm.io/motivation)

### 概述总结
pnpm通过内容可寻址存储、三阶段安装流程和符号链接机制，显著节省磁盘空间、提升安装速度，并创建非扁平化的node_modules结构。

- 💾 **节省磁盘空间**：依赖存储在单一内容可寻址存储中，相同版本的依赖跨项目共享，仅存储差异文件（如更新时只添加修改的文件），通过硬链接避免重复占用空间。
- ⚡ **提升安装速度**：三阶段安装流程（依赖解析、目录结构计算、链接依赖）比传统npm的解析-获取-写入方式更高效，大幅缩短安装时间。
- 🔗 **创建非扁平node_modules**：默认使用符号链接仅将直接依赖添加到node_modules根目录，避免代码访问未声明的依赖；同时支持通过`nodeLinker: hoisted`设置回退到传统扁平结构。

---

### [pnpm pack-app | pnpm](https://pnpm.io/11.x/cli/pack-app)

**原文标题**: [pnpm pack-app | pnpm](https://pnpm.io/11.x/cli/pack-app)

以下是 pnpm `pack-app` 命令的摘要：

pnpm `pack-app` 是一个实验性命令，用于将 CommonJS 入口文件打包成独立可执行文件，支持多平台构建，基于 Node.js 单可执行应用 API。

- 🧪 实验性功能：`pack-app` 在 v11.0.0 中添加，其标志、配置和输出布局可能在未来版本中更改。
- 📦 打包输出：每个目标平台生成可执行文件，默认输出到 `dist-app/<target>/`；Windows 输出带 `.exe` 后缀，macOS 输出自动进行临时签名。
- ⚙️ 系统要求：主机需运行 Node.js v25.5+ 以执行 SEA 注入；若版本不匹配，pnpm 会自动下载匹配的构建器。
- 🖥️ 支持目标：格式为 `<os>-<arch>[-<libc>]`，包括 `linux-x64`、`darwin-arm64`、`win32-x64` 等，`-musl` 仅适用于 Linux 目标。
- 📝 配置选项：可通过 CLI 或 `package.json` 中的 `pnpm.app` 设置，包括 `--entry`、`--target`、`--runtime`、`--output-dir` 和 `--output-name`。
- 🔧 示例：`pnpm pack-app --entry dist/index.cjs --target linux-x64 --target win32-x64` 可同时为 Linux 和 Windows 构建。
- 📂 配置示例：在 `package.json` 中设置 `pnpm.app` 可简化命令，CLI 标志会覆盖配置文件中的设置。

---

### [从 v10 迁移到 v11 | pnpm](https://pnpm.io/11.x/migration)

**原文标题**: [Migrating from v10 to v11 | pnpm](https://pnpm.io/11.x/migration)

这是 pnpm 11.x 版本的未发布文档。  
- 📄 从 v10 迁移到 v11 引入了多项配置读取和设置的破坏性变更，大部分可通过 codemod 自动处理，其余需手动调整。  
- 🔧 运行 codemod：使用 `pnx codemod run pnpm-v10-to-v11` 或全局安装 codemod 后执行，自动完成以下操作：  
  - 将 `package.json#pnpm` 中的设置移至 `pnpm-workspace.yaml`。  
  - 拆分 `.npmrc`，仅保留认证和注册表设置，其余移至 `pnpm-workspace.yaml`。  
  - 合并构建依赖设置为 `allowBuilds` 映射。  
  - 替换包管理器严格性设置为 `pmOnFail`。  
  - 重命名 `allowNonAppliedPatches` 和 `auditConfig.ignoreCves`。  
  - 将 `useNodeVersion` 转换为 `devEngines.runtime` 条目。  
  - 更新 `package.json` 中的 `packageManager` 版本。  
- ⚠️ 手动跟进事项：  
  - 将 CVE ID 转换为 GHSA ID（如 `auditConfig.ignoreGhsas`）。  
  - `ignorePatchFailures` 已移除，失败补丁会抛出错误。  
  - `executionEnv.nodeVersion` 需改用 `devEngines.runtime`。  
  - `npm_config_*` 环境变量需重命名为 `pnpm_config_*`。  
  - `pnpm link <pkg-name>` 不再解析全局存储，需使用路径。  
  - `pnpm install -g` 不再支持，改用 `pnpm add -g <pkg>`。  
  - `pnpm server` 已移除且无替代。  
  - 脚本名称可能覆盖内置命令，使用 `pnpm pm <name>` 强制运行内置命令。

---

### [GitHub - pnpm/pacquet：用 Rust 重写的官方 pnpm](https://github.com/pnpm/pacquet)

**原文标题**: [GitHub - pnpm/pacquet: The official pnpm rewrite in Rust · GitHub](https://github.com/pnpm/pacquet)

pnpm 的 Rust 重写版本 pacquet 正在积极开发中，旨在提升性能并逐步替代原 TypeScript 实现。

- ⚠️ 项目处于活跃开发阶段，尚未准备好用于生产环境
- 🔄 是 pnpm CLI 从 TypeScript 到 Rust 的精确移植，行为、标志、默认值等完全一致
- 📋 分两阶段实施：第一阶段替换获取和链接，第二阶段接管依赖解析
- 🚀 第一阶段预计使 pnpm 速度提升至少两倍
- 📊 包含基准测试、贡献指南和开发设置文档
- 🏗️ 仓库包含 394 次提交，拥有 980 颗星和 31 个复刻
- 💻 代码主要使用 Rust（98.7%）编写，采用 Apache-2.0 和 MIT 双许可证

---

### [黎明](https://aube.en.dev/)

**原文标题**: [aube](https://aube.en.dev/)

### 概述
Aube 是一款极速的 Node.js 包管理器，兼容现有锁文件，大幅提升安装速度并节省磁盘空间。

- 🚀 **速度领先**：Aube 比 pnpm 快 9.2 倍，比 Bun 快 2.7 倍（热安装基准测试）。
- 💾 **节省磁盘**：使用全局内容寻址存储，项目间共享依赖文件，比 npm 少用 90% 磁盘空间。
- 🔒 **兼容锁文件**：可直接读写 `yarn.lock`、`pnpm-lock.yaml` 或 `package-lock.json`，无需团队迁移。
- ⚡ **智能脚本运行**：`aubr test` 自动检测依赖变化并安装，重复运行时跳过安装步骤。
- 🛡️ **安全默认设置**：默认阻止信任降级、新版本有 24 小时冷却期、构建脚本需批准，并支持 `paranoid: true` 强化安全。

---

### [首页 | 准备工作](https://mise.en.dev/)

**原文标题**: [Home | mise-en-place](https://mise.en.dev/)

概述摘要：本文档介绍了 mise 工具的核心功能模块，包括版本管理、开发工具、环境配置和任务执行，并提供了界面外观设置选项。

- 🔍 搜索功能：支持快速查找内容
- 🗺️ 主导航：提供主菜单导航入口
- 🔄 版本管理：mise-versions 模块用于管理软件版本
- 🛠️ 开发工具：集成开发者常用工具链
- 🌐 环境配置：管理项目运行环境设置
- 📋 任务执行：支持自动化任务定义与运行
- 📅 版本标识：当前版本为 v2026.4.25
- 🎨 外观设置：允许自定义界面显示风格

---

### [基准测试 | aube](https://aube.en.dev/benchmarks.html)

**原文标题**: [Benchmarks | aube](https://aube.en.dev/benchmarks.html)

该基准测试对比了不同包管理器在多种场景下的安装速度，结果显示 aube 在多数情况下性能最优。

- ⚡ **aube 性能领先**：在热缓存的新安装中，aube（270ms）比 bun（724ms）快约 2.7 倍，比 npm（10.18s）快约 38 倍。
- 📦 **冷缓存安装对比**：aube（3.10s）在冷启动时仍表现良好，仅次于 bun（2.07s），远超其他工具。
- 🛠️ **CI 环境优化**：禁用全局虚拟存储后，aube 在热缓存 CI 安装（588ms）和冷缓存 CI 安装（2.85s）中均保持领先。
- 🚀 **增量操作高效**：添加依赖时 aube（328ms）比 bun（716ms）快 2 倍以上，比 pnpm（3.16s）快近 10 倍。
- 🔄 **开发循环加速**：在已安装依赖后执行测试命令，aube（9ms）几乎瞬间完成，bun（36ms）次之。
- ⚙️ **技术优势**：aube 采用与 pnpm 相同的全局内容寻址存储和隔离符号链接布局，但使用原生多线程语言编写，安装管道更快。
- 📊 **可复现基准**：所有测试使用相同的中等规模真实项目（约 1400 个包），通过 hyperfine 在受控条件下测量，并提供了完整的复现脚本。

---

### [Meticulous AI - 无需编写测试的自动化前端测试](https://www.meticulous.ai/?utm_source=jsweekly&utm_medium=referral&utm_campaign=26q2&utm_content=primary)

**原文标题**: [Meticulous AI - Automated Frontend Testing Without Writing Tests](https://www.meticulous.ai/?utm_source=jsweekly&utm_medium=referral&utm_campaign=26q2&utm_content=primary)

Meticulous AI 是一款自动化、全面且确定性的测试工具，旨在帮助开发团队以更快的速度交付代码，无需手动编写或维护测试用例。

- 🤖 **AI驱动自动化测试**：Meticulous 的 AI 引擎能自动生成并持续更新测试套件，覆盖应用的每一行代码、每个用户流程和边缘情况。
- 📹 **无侵入式会话录制**：通过在本地开发、预发布等环境添加脚本标签，自动记录用户交互，无需额外配置。
- 🔍 **PR影响预览**：提交拉取请求时，可提前看到代码变更对所有用户工作流的影响，避免合并后出现问题。
- 🚫 **零维护与零误报**：测试自动随应用演进，并基于 Chromium 级确定性调度引擎，彻底消除测试不稳定（flakes）问题。
- ⚡ **闪电般速度**：测试在计算集群上高度并行化，可在120秒内完成数千个屏幕的测试。
- 🛠️ **广泛框架支持**：支持 NextJS、React、Vue、Angular、Nuxt、SvelteKit 等主流框架，集成简单。
- 🏢 **企业级信任**：已被 Dropbox、Notion 等超过100家组织采用，获得工程师高度评价。
- 🔒 **安全与合规**：提供安全文档和隐私政策，确保测试过程安全可靠。

---

### [宣布 TypeScript 7.0 Beta 版 - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-7-0-beta/)

**原文标题**: [Announcing TypeScript 7.0 Beta - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-7-0-beta/)

TypeScript 7.0 Beta 正式发布，基于 Go 语言重写，性能大幅提升，并引入了并行化处理、新默认配置和编辑器增强等重大更新。

- 🚀 TypeScript 7.0 基于 Go 语言重写，速度比 6.0 快约 10 倍，且与 6.0 类型检查逻辑完全一致。
- ⚙️ 可通过 `npm install -D @typescript/native-preview@beta` 安装，使用 `tsgo` 命令运行，并支持 VS Code 扩展预览。
- 🔄 支持与 TypeScript 6.0 并行运行，提供 `@typescript/typescript6` 兼容包以避免冲突。
- 🧵 引入并行化处理，通过 `--checkers` 和 `--builders` 标志控制类型检查与项目构建的并行度。
- 🛠️ 新增 `--singleThreaded` 标志，用于调试或资源受限环境。
- 📋 采用 TypeScript 6.0 的默认配置，如 `strict: true`、`module: esnext` 等，并废弃了 `es5`、`amd` 等旧选项。
- 🗂️ `rootDir` 默认改为 `./`，`types` 默认改为 `[]`，需手动配置以保持旧行为。
- 📜 JavaScript 支持全面重写，与 `.ts` 文件分析更一致，废弃了 `@enum`、`@class` 等旧 JSDoc 模式。
- ✨ 编辑器体验大幅提升，支持自动导入、悬停提示、内联提示等，但仍有一些功能待完善。
- 🗓️ 计划在两个月内发布稳定版，当前 Beta 版已高度稳定，建议在真实项目中测试反馈。

---

### [宣布 TypeScript 6.0](https://devblogs.microsoft.com/typescript/announcing-typescript-6-0/)

**原文标题**: [Announcing TypeScript 6.0 - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-6-0/)

TypeScript 6.0 正式发布，这是连接 TypeScript 5.9 和即将到来的原生 Go 语言重写版本 7.0 的桥梁版本，带来了一系列新特性、性能改进和重要的弃用变更。

- 🚀 TypeScript 6.0 是通往 7.0 的桥梁，7.0 基于 Go 重写，性能大幅提升，且已接近完成，可试用预览版。
- 🎯 改进了类型推断：不再将未使用 `this` 的函数视为上下文敏感，使得方法语法下的泛型调用推断更准确。
- 🔗 支持 Node.js 的 `#/` 子路径导入，简化了包内模块别名的写法。
- ⚙️ 允许 `--moduleResolution bundler` 与 `--module commonjs` 组合使用，为迁移提供更平滑的路径。
- 🧩 新增 `--stableTypeOrdering` 标志，使 6.0 的类型排序与 7.0 一致，帮助诊断迁移中的差异。
- 📅 新增 `es2025` 目标与库支持，包含 `RegExp.escape` 等新 API。
- ⏳ 为 `Temporal` API 和 `Map`/`WeakMap` 的 `getOrInsert` 方法提供了内置类型定义。
- 🌐 DOM 库现在默认包含 `dom.iterable` 和 `dom.asynciterable`，无需额外配置。
- ⚠️ 大量默认值变更（如 `strict` 默认开启）和弃用项（如 `es5` 目标、`moduleResolution node`、`baseUrl`、`outFile` 等），需注意迁移。

---

### [宣布 TypeScript 7.0 Beta 版 - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-7-0-beta/#updates-since-5.x-and-new-behaviors-from-6.0)

**原文标题**: [Announcing TypeScript 7.0 Beta - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-7-0-beta/#updates-since-5.x-and-new-behaviors-from-6.0)

TypeScript 7.0 Beta 发布，基于 Go 重写，性能大幅提升，并带来并行化构建、新默认配置等重大更新。

- 🚀 **性能飞跃**：TypeScript 7.0 基于 Go 重写，利用原生速度和并行处理，速度比 6.0 快约 10 倍。
- ✅ **高度兼容**：与 6.0 类型检查逻辑结构一致，经过大规模测试，可直接用于日常开发。
- 📦 **安装与使用**：通过 `npm install -D @typescript/native-preview@beta` 安装，使用 `tsgo` 命令，并提供了 VS Code 扩展。
- 🔄 **并行化控制**：新增 `--checkers` 和 `--builders` 标志，可分别控制类型检查和项目构建的并行度，并支持 `--singleThreaded` 单线程模式。
- ⚙️ **6.0 新默认配置**：默认启用 `strict`、`module: esnext`、`noUncheckedSideEffectImports` 等，并移除对 `es5`、`amd` 等旧特性的支持。
- 📝 **JavaScript 支持重写**：JSDoc 分析更严格，弃用了 `@enum`、`@class` 等非标准模式，与 `.ts` 文件分析更一致。
- 🛠️ **编辑器体验增强**：VS Code 扩展支持自动导入、悬停提示、内联提示、代码镜头等，性能同样大幅提升。
- 🗺️ **未来规划**：计划两个月内发布稳定版，后续将完善 `--watch` 模式、声明文件发射、稳定 API 等。

---

### [宣布 TypeScript 7.0 Beta 版 - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-7-0-beta/#javascript-differences)

**原文标题**: [Announcing TypeScript 7.0 Beta - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-7-0-beta/#javascript-differences)

TypeScript 7.0 Beta 正式发布，基于Go重写，速度提升约10倍，并带来全新并行化架构和编辑器体验。

- 🚀 核心架构迁移：TypeScript 7.0 将代码库从 TypeScript 移植到 Go，利用原生代码速度和共享内存并行，编译速度比 6.0 快约 10 倍。
- 🧪 高度稳定与兼容：新代码库是系统化移植而非重写，类型检查逻辑与 6.0 结构一致，已通过大规模测试并在多家公司生产环境中验证。
- 📦 安装与试用：可通过 npm 安装 `@typescript/native-preview@beta`，使用 `tsgo` 命令；VS Code 提供 `TypeScript Native Preview` 扩展。
- 🔄 并行化控制：新增 `--checkers` 和 `--builders` 标志，分别控制类型检查器和项目构建的并行数量，并支持 `--singleThreaded` 单线程模式。
- ⚙️ 6.0 默认配置继承：7.0 采用 6.0 新默认值（如 `strict: true`、`module: esnext` 等），并废弃了 `es5`、`downlevelIteration` 等旧特性。
- 🛠️ JavaScript 支持重构：统一 JS 文件分析逻辑，废弃了 `@enum`、`@class` 等特殊 JSDoc 语法，要求使用更严格的 TypeScript 风格。
- 🖥️ 编辑器体验提升：VS Code 扩展支持自动导入、可展开悬停、内联提示、代码镜头等功能，性能与命令行一致。
- 📅 未来计划：即将推出更高效的 `--watch` 模式、稳定 API（7.1+），预计两个月内发布正式版，RC 版将提前几周推出。

---

### [RafaelGSS 提交的 2026-04-28，版本 26.0.0（当前版）· 拉取请求 #62526 · nodejs/node · GitHub](https://github.com/nodejs/node/pull/62526)

**原文标题**: [2026-04-28, Version 26.0.0 (Current) by RafaelGSS · Pull Request #62526 · nodejs/node · GitHub](https://github.com/nodejs/node/pull/62526)

Node.js 26.0.0 版本正式发布，带来了多项重大更新和破坏性变更，包括默认启用 Temporal API、V8 引擎升级至 14.6、Undici 更新至 8.0，以及多项弃用和移除。

- 🎉 **Temporal API 默认启用**：全新的现代日期/时间 API，提供比传统 `Date` 对象更强大、更丰富的功能。
- 🚀 **V8 引擎升级至 14.6**：带来 `Map.getOrInsert()`、`Iterator.concat()` 等新特性，性能与功能全面提升。
- ⚡ **Undici 更新至 8.0.2**：Node.js 的 HTTP 客户端实现获得新功能和改进。
- 🗑️ **多项 API 弃用与移除**：包括 `writeHeader()`、`_stream_*` 模块、`module.register()` 等被移除或运行时弃用。
- 🔧 **构建系统变更**：GCC 要求提升至 13.2，放弃对 Python 3.9 的支持，目标平台调整为 Power 9。
- 🛡️ **安全修复**：修复了数组索引哈希碰撞漏洞 (CVE-2026-21717)。
- 🐧 **平台支持调整**：放弃对 p8 和 z13 的支持，更新 Windows SDK 版本至 11。
- 📦 **依赖更新**：ICU 更新至 78.3，libuv 更新至 1.52.1，并包含多项 V8 补丁。
- ⏳ **LTS 计划**：Node.js 26 将在 10 月进入长期支持 (LTS) 阶段，目前为“Current”版本。

---

### [GitHub 可用性更新 - GitHub 博客](https://github.blog/news-insights/company-news/an-update-on-github-availability/)

**原文标题**: [An update on GitHub availability - The GitHub Blog](https://github.blog/news-insights/company-news/an-update-on-github-availability/)

GitHub 近期因两次服务中断事件而发布更新，承诺提升可用性和可靠性，并分享了具体改进措施和未来计划。

- 📉 两次服务中断：4月23日合并队列问题导致658个仓库受影响，4月27日搜索子系统因攻击过载，部分UI无结果，均无数据丢失
- 🚀 容量扩展计划：2025年10月起执行10倍容量提升，2026年2月因AI开发激增需扩展至30倍规模
- ⚙️ 短期修复：解决Webhooks迁移、用户会话缓存重设计、认证流程优化等瓶颈，并利用Azure迁移增加计算资源
- 🔒 服务隔离：优先隔离Git和Actions等关键服务，减少单点故障，降低影响范围
- ☁️ 多云策略：加速从自建数据中心迁移至公共云，并启动多云路径以提升弹性和低延迟
- 🏗️ 大型仓库优化：针对大型单体仓库增长，优化Git系统、拉取请求体验和合并队列操作
- 📢 透明度提升：更新状态页显示可用性数据，承诺报告大小事件，改进事件分类和用户报告机制
- 💡 长期承诺：优先可用性，再容量，后新功能，减少不必要工作、改善缓存、隔离服务，并移除单点故障

---

### [GitHub 可用性更新 - GitHub 博客](https://github.blog/news-insights/company-news/an-update-on-github-availability/#h-recent-incidents)

**原文标题**: [An update on GitHub availability - The GitHub Blog](https://github.blog/news-insights/company-news/an-update-on-github-availability/#h-recent-incidents)

GitHub 近期发生两起服务中断事件，团队正全力提升可靠性和容量，以应对因AI开发工作流激增带来的30倍规模增长需求。

- 📉 **服务中断致歉**：对4月23日合并队列故障和4月27日搜索相关事件表示歉意，已影响658个仓库和2092个PR，但无数据丢失。
- 🚀 **容量扩展计划**：2025年10月起执行10倍容量提升计划，2026年2月因代理开发工作流加速，目标调整为30倍当前规模。
- ⚙️ **短期优化措施**：解决Webhooks迁移、用户会话缓存重设计等瓶颈，利用Azure迁移增加计算资源。
- 🔒 **关键服务隔离**：优先隔离Git和Actions等核心服务，减少单点故障，将性能敏感代码从Ruby迁移至Go。
- ☁️ **多云架构推进**：加速从自建数据中心迁移至公有云，并启动多云路径以提升弹性和低延迟。
- 📊 **大规模仓库优化**：重点应对大型单体仓库增长，优化合并队列操作，支持每日数千PR的高效处理。
- 🛠️ **4月23日故障详情**：合并队列使用squash合并时产生错误提交，影响658个仓库，已修复流程防止复发。
- 🔍 **4月27日搜索故障**：Elasticsearch集群因疑似僵尸网络攻击过载，导致UI搜索功能失效，正在完成根因分析。
- 📢 **透明度提升**：更新状态页面显示可用性数据，承诺大小事件均通报，并改进事件分类和用户报告渠道。
- 💡 **长期承诺**：优先保障可用性、容量和可靠性，减少隐藏耦合，确保系统在压力下优雅降级。

---

### [NodeConf EU | Node.js](https://www.nodeconf.eu/)

**原文标题**: [NodeConf EU | Node.js](https://www.nodeconf.eu/)

NodeConf EU 是一个汇聚技术社区的 Node.js 会议，将于 9 月 29 日至 30 日在意大利博洛尼亚举行，目前门票已开售，并开放演讲提案征集（CFP）。

- 🎟️ 门票现已开售，可立即购买参会资格
- 📅 会议时间为 9 月 29 日至 30 日，地点在意大利博洛尼亚
- 🎤 开放演讲提案征集（CFP），鼓励社区参与
- 🏆 设有铂金、金、银等各级赞助商，包括 T 恤和咖啡休息赞助
- 🤝 社区赞助商支持，促进技术交流与协作

---

### [NodeConf EU 2026](https://docs.google.com/forms/d/e/1FAIpQLSdhxLUxB5kW8NU5Dv6PM7vvQqKLcKed45AXvsXPGN8tIkzfkg/viewform)

**原文标题**: [NodeConf EU 2026](https://docs.google.com/forms/d/e/1FAIpQLSdhxLUxB5kW8NU5Dv6PM7vvQqKLcKed45AXvsXPGN8tIkzfkg/viewform)

NodeConf EU 2026 回歸，本次在義大利波隆那舉行，並開放講者投稿。

- 🇮🇹 NodeConf EU 2026 將於9月29日至30日在義大利波隆那舉行，帶來濃厚的義大利風情。
- 🎤 活動為期兩天，預計有24位講者，涵蓋Node.js核心、實際應用與生態系統等主題。
- 📝 歡迎對Node.js充滿熱情的人投稿，分享故事、願景或想法。
- 📧 投稿需提供電子郵件、提案標題、描述、講者姓名、簡介及社交媒體等資訊。
- ✅ 提交時需同意個人資料與活動主辦方共享，並確認是否需旅行補助及公司贊助意願。

---

### [Rspack 2.0 发布公告](https://rspack.rs/blog/announcing-2-0)

**原文标题**: [Announcing Rspack 2.0 - Rspack](https://rspack.rs/blog/announcing-2-0)

Rspack 2.0 正式发布，带来了性能提升、输出优化、ESM 支持改进以及多项新功能，同时保持与 webpack 生态的兼容性。

- 🚀 **性能大幅提升**：相比 1.7 版本整体性能提升约 10%，相比 1.0 版本提升高达 100%，并优化了持久缓存和内存使用。
- 📦 **依赖大幅减少**：`@rspack/dev-server` 依赖从 192 个减至 1 个，`@rspack/cli` 实现零依赖，安装体积减少 90% 以上。
- 🌿 **静态分析增强**：改进 tree shaking 支持 CommonJS `require` 解构、属性访问及动态 `import()` 结果的内联分析。
- 🧹 **编译器注解支持**：支持 `#__NO_SIDE_EFFECTS__` 标记无副作用函数，以及通过 `pureFunctions` 手动声明纯函数。
- 🔗 **Module Federation 摇树优化**：支持共享依赖的导出级别摇树，减少共享包体积。
- 📜 **纯 ESM 包发布**：核心包（如 `@rspack/core`、`@rspack/cli`）转为纯 ESM 包，移除 CommonJS 构建。
- 🆕 **新功能**：包括 React Server Components 实验性支持、`#/` 子路径别名导入、简化 target 和 swc-loader 配置、CSS 导入控制、哈希模块 ID 及改进代码分割。

---

### [宣布 Rspack 2.0 发布 - Rspack](https://rspack.rs/blog/announcing-2-0#better-tree-shaking)

**原文标题**: [Announcing Rspack 2.0 - Rspack](https://rspack.rs/blog/announcing-2-0#better-tree-shaking)

Rspack 2.0 正式发布，带来性能提升、输出优化、ESM 支持增强及多项新功能，并逐步向现代化 JavaScript 开发演进。

- 🚀 **性能大幅提升**：相比 1.7 版本，整体性能提升约 10%，带缓存的生产构建速度提升近 50%，HMR 速度也更快。
- 📦 **依赖大幅精简**：`@rspack/dev-server` 依赖从 192 个降至 1 个，`@rspack/cli` 实现零依赖，安装体积减少超 90%。
- ✂️ **输出优化增强**：改进静态分析，支持 CommonJS 解构、属性访问的 Tree Shaking，并新增编译器注解和 Module Federation 的 Tree Shaking 支持。
- 🌐 **ESM 全面支持**：核心包转为纯 ESM 发布，支持 `import.meta`、`import defer`，并新增 `modern-module` 库构建模式，输出更纯净。
- 🆕 **新功能亮点**：实验性支持 React Server Components，支持 `#/` 子路径别名导入，简化 `target` 和 `swc-loader` 配置，CSS 导入可精细控制，并新增 `hashed` 模块 ID 和强制代码分割阈值。
- 🔮 **未来规划**：将持续优化输出质量、增强对编码代理的支持，并深化 Rstack 工具链的协作，如集成 typescript-go。

---

### [Rspack 2.0 发布公告 - Rspack](https://rspack.rs/blog/announcing-2-0#rsc-support)

**原文标题**: [Announcing Rspack 2.0 - Rspack](https://rspack.rs/blog/announcing-2-0#rsc-support)

Rspack 2.0 正式发布，带来性能提升、输出优化和新功能，同时保持与 webpack 生态的兼容性。

- 🚀 **性能大幅提升**：相比 1.7 版本整体性能提升约 10%，相比 1.0 版本提升高达 100%；启用持久缓存后构建性能再提升约 50%，内存使用降低超过 20%。
- 📦 **依赖大幅减少**：`@rspack/dev-server` 依赖从 192 个降至 1 个，安装体积减少 90% 以上；`@rspack/cli` 实现零依赖。
- 🔍 **静态分析增强**：支持 CommonJS `require` 解构、属性访问和动态 `import()` 的导出级 Tree Shaking，以及编译器注解 `#__NO_SIDE_EFFECTS__`。
- 🌐 **ESM 支持改进**：核心包转为纯 ESM 包；支持 `import.meta` 属性保留、`import defer` 延迟加载，以及优化库构建的 `modern-module` 输出类型。
- 🧩 **新功能亮点**：实验性支持 React Server Components（RSC）；支持 `#/` 子路径别名导入；简化目标配置和 `swc-loader` 配置；CSS 导入控制；哈希模块 ID；改进代码分割。
- 🔗 **生态兼容与扩展**：继续兼容 webpack 生态，并已获得 Angular、Next.js、Nuxt、Storybook 等众多框架和工具的支持。

---

### [Rsbuild 2.0 发布公告 - Rsbuild](https://rsbuild.rs/blog/v2-0)

**原文标题**: [Announcing Rsbuild 2.0 - Rsbuild](https://rsbuild.rs/blog/v2-0)

Rsbuild 2.0 正式发布，这是一个由 Rspack 驱动的现代构建工具，带来了更快的构建速度、新功能和更好的开发体验。该版本经过三个月的验证和打磨，生态中的 Rslib、Rstest、Rspress 等工具均已稳定升级。

- 🚀 **核心升级**：基于 Rspack 2.0，带来更快构建和新的输出优化能力。
- ⚛️ **React 服务端组件 (RSC) 支持**：通过 `rsbuild-plugin-rsc` 插件，利用 Environments API 统一管理客户端和服务端环境。
- 💬 **开发服务器与客户端通信**：新增 `hot.send` 和 `import.meta.webpackHot.on` API，复用现有 HMR 通道，无需额外 WebSocket 连接。
- 🛠️ **扩展内置服务器**：新增 `server.setup` 选项，可在开发或预览服务器启动时运行初始化逻辑，如注册中间件。
- 📝 **自定义日志支持**：通过 `customLogger` 选项，可为每个 Rsbuild 实例定义不同的日志级别、前缀或日志系统。
- 🧩 **更易用的代码分割**：引入与 Rspack `splitChunks` 行为一致的新配置，并提供 `preset` 预设（如 `per-package`）。
- 📦 **更轻量**：默认依赖从 13 个减少到 4 个，安装体积减少约 2 MB（core-js 等改为按需安装）。
- 🔒 **默认更安全**：`server.host` 默认值从 `0.0.0.0` 改为 `localhost`，避免开发服务器意外暴露。
- 🔄 **代理中间件升级**：`http-proxy-middleware` 升级至 v4，支持 HTTP/2 代理，修复安全漏洞。
- 🧹 **纯 ESM 包**：`@rsbuild/core` 发布为纯 ESM 包，减少安装体积约 500 KB。
- 🖥️ **Node.js 支持更新**：最低支持 Node.js 20.19+ 或 22.12+，不再支持已 EOL 的 Node.js 18。
- 🌐 **更新默认目标**：Web 输出目标浏览器更新为更现代的版本（如 Chrome 107+），Node.js 输出目标提升至 Node.js 20。
- 📄 **ESM Node.js 输出**：Node.js 输出默认生成未压缩的 ES 模块，便于调试。
- 🏷️ **装饰器版本更新**：默认装饰器版本从 `2022-03` 更新为 `2023-11`，与 Babel 8 默认行为一致。
- 🙏 **致谢**：感谢所有社区贡献者，包括 @chenjiahan、@hardfist 等众多开发者。

---

### [直观的Vue UI库 - Nuxt UI](https://ui.nuxt.com/)

**原文标题**: [The Intuitive Vue UI Library - Nuxt UI](https://ui.nuxt.com/)

### 概述总结
一个基于 Vue 的 UI 组件库，包含 125+ 个可访问、Tailwind CSS 驱动的组件，支持 Nuxt 和普通 Vue 应用，提供灵活的设计系统、运行时配置和主题定制。

- 🎨 **Tailwind CSS 样式**：默认美观，可覆盖任意样式。
- ♿ **Reka UI 无障碍**：开箱即用的无障碍支持。
- 🔒 **TypeScript 类型安全**：所有组件支持自动补全和类型安全。
- 📦 **125+ 组件**：包含手风琴、按钮、日历、卡片、轮播等丰富组件。
- 🌐 **国际化 (i18n)**：支持 50+ 种语言和双向布局 (LTR/RTL)。
- 🌓 **明暗模式**：组件支持深色模式，集成 `@nuxtjs/color-mode`。
- 🖌️ **CSS 优先设计系统**：通过 `@theme` 指令定义字体、颜色和断点，可移植且易维护。
- 🎯 **语义化颜色系统**：7 种语义颜色别名（主色、次要、成功、信息等），描述颜色用途。
- ⚙️ **运行时颜色配置**：通过 AppConfig 动态更改颜色和图标，无需重新构建应用。
- 🔧 **组件定制**：使用 Tailwind Variants API 支持插槽、变体和复合变体，全局或单独覆盖样式。
- 🚀 **生产级模板**：响应式、SEO 优化、可立即部署的模板，支持 Nuxt 和 Vue。
- 👥 **社区支持**：1.3M+ 月下载量、6.5K+ GitHub 星标、300+ 贡献者，开源社区活跃。

---

### [发布 v4.7.0 · nuxt/ui · GitHub](https://github.com/nuxt/ui/releases/tag/v4.7.0)

**原文标题**: [Release v4.7.0 · nuxt/ui · GitHub](https://github.com/nuxt/ui/releases/tag/v4.7.0)

Nuxt UI v4.7.0 版本发布，带来了新组件、功能增强和错误修复。

- 📋 新增 Listbox 组件：一个可选择的列表组件，内置搜索、虚拟化和丰富的渲染功能，适合需要始终可见列表的场景。
- 🤖 新增 ProsePrompt 组件：用于在文档中显示预构建的 AI 提示，支持一键复制和直接集成到 Cursor 或 Windsurf IDE。
- 🌍 自动链接本地化：Link 组件现在自动与 @nuxtjs/i18n 集成，内部链接会根据当前语言环境自动本地化，并扩展到所有接受 to 属性的组件。
- 🚀 功能增强：AuthForm 添加分隔符插槽；Card 添加标题和描述属性；CommandPalette 添加组标签插槽和搜索延迟属性；EditorSuggestionMenu 暴露建议匹配选项；Table 支持虚拟化模式下的粘性页眉/页脚；Textarea 暴露自动调整大小方法。
- 🐛 错误修复：修复了 Accordion/Tabs 的键值问题、Avatar 的备用样式、ChatMessage 的类型保留、ChatMessages 的滚动和布局问题、FieldGroup 的上下文泄漏、InputDate/InputTime 的段宽度、Link 的单根渲染、Modal/Slideover 的空包装器、PricingTable 的 RTL 支持等多项问题。
- 👋 新贡献者：感谢 faizkhairi、Archetipo95、nimonian、mrkaashee、tratteo、Ken-vdE、claylevering 和 ChronicStone 的首次贡献。

---

### [Vue 列表框组件 - Nuxt UI](https://ui.nuxt.com/docs/components/listbox)

**原文标题**: [Vue Listbox Component - Nuxt UI](https://ui.nuxt.com/docs/components/listbox)

Listbox 是一个可搜索、支持虚拟化、可多选的项目列表组件，通过 `v-model` 控制选中值，并支持丰富的自定义渲染。

- 📋 **基本用法**：使用 `v-model` 或 `default-value` 控制选中项，通过 `items` 属性传入项目数组。
- 🔍 **搜索过滤**：设置 `filter` 属性可启用搜索输入框，支持自定义占位符和图标。
- ✅ **多选模式**：添加 `multiple` 属性允许选择多个项目，`v-model` 绑定为数组。
- 🎨 **自定义图标**：通过 `selected-icon` 属性更改选中项的图标，默认是 `i-lucide-check`。
- 📏 **尺寸调整**：使用 `size` 属性（xs/sm/md/lg/xl）调整组件大小。
- ⏳ **加载状态**：设置 `loading` 属性显示加载指示器，可自定义加载图标。
- 🚫 **禁用状态**：设置 `disabled` 属性阻止用户交互。
- 🧩 **项目类型**：项目支持 `label`、`separator` 类型，可分组显示。
- 🖼️ **丰富内容**：项目内可嵌入图标、头像（avatar）、徽章（chip）和描述文本。
- 🔑 **值键绑定**：通过 `value-key` 属性绑定对象的特定属性作为值，而非整个对象。
- ⚡ **虚拟化**：启用 `virtualize` 属性优化大型列表性能。
- 🔄 **传输列表**：可组合两个 Listbox 组件实现穿梭框（transfer list）模式。
- 🛠️ **自定义过滤**：`ignore-filter` 禁用内置搜索，配合 `v-model:search-term` 实现自定义过滤逻辑。
- 📂 **过滤字段**：使用 `filter-fields` 指定搜索的字段（如 label、email）。

---

### [提示 - Nuxt UI](https://ui.nuxt.com/docs/typography/prompt)

**原文标题**: [Prompt - Nuxt UI](https://ui.nuxt.com/docs/typography/prompt)

本文档介绍了 Nuxt UI 中的 `prompt` 组件，用于展示可一键复制或集成到 IDE 的 AI 提示。

- 📝 **组件概述**：`prompt` 组件可显示预构建的 AI 提示，支持一键复制到剪贴板或直接在 IDE（如 Cursor、Windsurf）中打开。
- 🎯 **基本用法**：通过 `description` 属性设置可见标签，默认插槽包含要复制的提示文本。示例：`Build a dashboard layout with Nuxt UI.`
- 🖼️ **图标支持**：使用 `icon` 属性可在描述旁显示图标，例如 `i-lucide-file-pen-line`。
- ⚙️ **操作按钮**：`actions` 属性控制显示哪些按钮（默认 `["copy"]`），可选 `copy`、`cursor` 和 `windsurf`，支持组合使用。
- 🛠️ **API 配置**：提供 `description`、`icon`、`actions` 等 Props，以及 `default` 插槽，支持通过 `ui` 属性自定义样式。
- 🎨 **主题定制**：可在 `app.config.ts` 或 `vite.config.ts` 中配置 `prose.prompt.slots` 来修改根元素、图标、内容、描述和操作区域的样式类。
- 📋 **其他相关组件**：文档还提及 `Kbd`（键盘快捷键）、`Steps`（步骤指南）等组件，用于增强提示的交互和展示。

---

### [Lingui 6.0 发布公告 | Lingui](https://lingui.dev/blog/2026/04/22/announcing-lingui-6.0)

**原文标题**: [Announcing Lingui 6.0 | Lingui](https://lingui.dev/blog/2026/04/22/announcing-lingui-6.0)

Lingui 6.0 发布，专注于技术改进和现代化，包括 ESM-only 分发、更小的包体积、更强的 TypeScript 支持，以及多项新功能和性能优化。

- 🚀 **核心升级**：转向 ESM-only 分发，要求 Node.js v22.19+，简化代码库并减少维护复杂性。
- 📦 **包体积大幅缩减**：`@lingui/core`、`@lingui/react` 和 `@lingui/cli` 组合安装从 62 MB 降至 35 MB（减少 44%），依赖包从 146 个减至 104 个。
- 🧩 **JSX 占位符命名**：新增 `macro.jsxPlaceholderAttribute` 和 `macro.jsxPlaceholderDefaults` 配置，使占位符名称语义化，提升翻译上下文清晰度。
- ⚡ **CLI 多线程支持**：所有 CLI 命令（extract、compile 等）支持多线程，默认使用 CPU 核心数减 1（最多 8 个），可通过 `--workers` 配置。
- 🛠️ **Vue 提取器增强**：支持 Vue 3 Reactivity Transform，通过 `createVueExtractor()` 工厂函数启用 `reactivityTransform` 选项。
- 🖥️ **Vite 插件改进**：支持 Vite 8，新增 `linguiTransformerBabelPreset` 简化 Rolldown 和 Babel 集成。
- 🔒 **更强的类型安全**：收紧 TypeScript 类型，统一 `undefined` 而非 `null`，优化提取消息与加载目录的类型分离。
- 🤖 **AI 时代集成**：提供 `llms.txt` 文档、Context7 MCP 集成和 Lingui Skills Agent Skills，助力 AI 工具正确实现国际化。
- 🆕 **新示例项目**：新增 React Webpack Po-Gettext 示例，展示复数处理、动态加载编译目录等功能。
- 📈 **社区增长**：自 5.0 以来 GitHub 星标增长 24%，下载量大幅提升，`eslint-plugin-lingui` 月下载量增长 639%。

---

### [发布 4.2.0 · huggingface/transformers.js · GitHub](https://github.com/huggingface/transformers.js/releases/tag/4.2.0)

**原文标题**: [Release 4.2.0 · huggingface/transformers.js · GitHub](https://github.com/huggingface/transformers.js/releases/tag/4.2.0)

Transformers.js v4.2 版本发布，新增工具调用、简化内部结构及隐私过滤功能。

- 🚀 为文本生成管道添加工具调用支持 (#1655)
- 🔧 使用 inputMetadata API 简化内部实现 (#1657)
- 🛡️ 新增 OpenAI 隐私过滤模型支持 (#1658)

---

### [发布 Electron v41.3.0 · electron/electron · GitHub](https://github.com/electron/electron/releases/tag/v41.3.0)

**原文标题**: [Release electron v41.3.0 · electron/electron · GitHub](https://github.com/electron/electron/releases/tag/v41.3.0)

electron v41.3.0 版本发布，修复了多个问题并更新了 Node.js。

- 🐛 修复 `webContents.printToPDF` 在 `pageRanges` 无效导致后续调用全部拒绝的问题
- 🪟 修复 Windows 上隐藏 `WebContentsView` 内 `app-region: drag` 仍拖动父窗口的问题
- 🍎 修复 macOS 更新因其他应用阻塞系统更新循环而无法应用的问题
- 🔧 修复禁用 `enable_pdf` 时构建失败的问题
- 🖼️ 修复 Windows 无框透明窗口在 `setResizable(false)` 后 `setResizable(true)` 失去透明度的问题
- ⬆️ 更新 Node.js 至 v24.15.0

---

### [发布 v2.7.0 · ether/etherpad · GitHub](https://github.com/ether/etherpad/releases/tag/v2.7.0)

**原文标题**: [Release v2.7.0 · ether/etherpad · GitHub](https://github.com/ether/etherpad/releases/tag/v2.7.0)

Etherpad v2.7.0 版本发布，包含重大变更、多项增强、修复及安全改进。

- 🔄 重大变更：用 LibreOffice 替换 Abiword 进行文档导入/导出，需更新 settings.json 配置。
- 🕐 时间滑块增强：新增行号显示和播放速度调节，方便回放历史记录。
- 👤 创建者控制：创建者可为 pad 设置默认配置，增强初始控制。
- 🍪 Cookie 配置：支持通过前缀配置 Cookie 名称，避免同域名下冲突。
- 🔌 插件钩子：新增 aceRegisterLineAttributes 钩子，支持插件保留自定义行属性。
- 🚀 简化安装：提供一键安装脚本，快速部署 Etherpad。
- 🐳 Docker 支持：镜像发布至 GitHub Container Registry，并修复多项构建问题。
- 📦 npm 安全：迁移至 OIDC 可信发布，增强供应链安全。
- 🛠️ 数据库修复：重新捆绑数据库驱动，修复 Postgres/MySQL 连接问题。
- 🔄 同步改进：重连后立即刷新待处理变更集，并警告未接受编辑。
- 🧹 会话清理：定期清理过期会话，修复竞态条件。
- 🔒 错误信息：默认清理并去重返回客户端的错误信息，防止内部泄露。
- 📏 消息大小：提升 socket.io 消息大小至 10 MB，支持大粘贴。
- 📝 列表修复：修复编号列表缩进、顺序保留、属性保持等多项问题。
- 🎨 格式保留：复制粘贴后保留加粗等格式，修复死键输入问题。
- 🌐 API 修复：修复 POST API 超时、appendText 属性、createDiffHTML 错误等。
- ♿ 无障碍改进：修复键盘陷阱、增强屏幕阅读器支持、添加 aria-live 公告。
- 🔄 RTL 修复：rtl=false 参数正确禁用从右到左模式。
- 📚 语言排序：语言下拉菜单按本地名称字母排序。
- ⬇️ PageDown 修复：正确前进一整页行数。
- 🔧 模块兼容：修复 ESM/CJS 互操作问题，添加 setter 和回归测试。
- 🏷️ 重命名：多处“etherpad-lite”改为“etherpad”。
- 🔒 安全更新：固定 33 个传递依赖版本，限制 GITHUB_TOKEN 权限。

---

### [JavaScript 中真正的新特性（以及接下来会有什么）—— Neciu Dan](https://neciudan.dev/whats-new-in-javascript)

**原文标题**: [What's actually new in JavaScript (and what's coming next) — Neciu Dan](https://neciudan.dev/whats-new-in-javascript)

以下是您提供的文章摘要，包含概述和要点列表：

ES2025已正式发布，ES2026候选版也已获批，JavaScript语言迎来多项实用新特性，包括迭代器辅助方法、Set操作方法、Promise.try、RegExp.escape等。同时，Temporal、using关键字和import defer等备受期待的功能虽未进入ES2026，但已在浏览器和Node中实现，可提前使用。文章还介绍了如何让AI编码助手使用这些新API。

- 📜 **ES2025核心新特性**：迭代器辅助方法（.map、.filter、.take等）让流式数据处理更高效；Set新增union、intersection等非变异操作方法；JSON模块支持原生导入；Promise.try统一处理同步/异步函数；RegExp.escape安全转义用户输入；Float16Array节省内存。
- 🔜 **ES2026即将落地**：Math.sumPrecise解决浮点数求和精度问题；Uint8Array原生支持base64和hex编码；Error.isError跨领域可靠检测错误；Iterator.concat连接多个迭代器；Map.getOrInsert简化缓存和计数；Array.fromAsync收集异步可迭代对象；JSON.parse支持源文本恢复。
- 🚀 **未进入ES2026但已可用**：Temporal（ES2027）彻底替代Date；using关键字自动管理资源清理；import defer延迟模块执行，优化启动性能。
- 🤖 **AI编码助手适配**：建议在系统提示中添加现代JavaScript偏好规则，引导AI优先使用新API（如Temporal替代moment.js、Map.getOrInsert替代手动检查），避免生成过时代码。

---

### [调试Next.JS最佳实践：日志与追踪 | Sentry](https://sentry.io/resources/nextjs-may-workshop/?utm_source=javascriptweekly&utm_medium=paid-community&utm_campaign=nextjs-fy27q1-nextjsworkshop&utm_content=newsletter-sponsored-link-register)

**原文标题**: [Debugging Next.JS Best Practices: Logs and Tracing | Sentry](https://sentry.io/resources/nextjs-may-workshop/?utm_source=javascriptweekly&utm_medium=paid-community&utm_campaign=nextjs-fy27q1-nextjsworkshop&utm_content=newsletter-sponsored-link-register)

概述摘要  
本资源介绍了关于Next.js调试最佳实践的研讨会，重点涵盖日志记录、分布式追踪和错误监控，旨在解决生产环境中调试困难的问题。

- 🔧 研讨会涵盖编写高上下文日志，记录失败原因、影响用户及具体细节  
- 🔍 学习如何查询和设置日志告警，捕获认证、支付、Webhook及第三方API调用中的静默失败  
- 🌐 深入探讨跨客户端和Node运行时的分布式追踪技术  
- 🔗 连接日志与追踪，无需切换工具即可获取完整上下文  
- 📘 提供额外资源，如Sentry与Next.js集成实践、AI代理构建及日志优化文章

---

### [调试Next.JS最佳实践：日志与追踪 | Sentry](https://sentry.io/resources/nextjs-may-workshop/?utm_source=javascriptweekly&utm_medium=paid-community&utm_campaign=nextjs-fy27q1-nextjsworkshop&utm_content=newsletter-sponsored-link-register%20)

**原文标题**: [Debugging Next.JS Best Practices: Logs and Tracing | Sentry](https://sentry.io/resources/nextjs-may-workshop/?utm_source=javascriptweekly&utm_medium=paid-community&utm_campaign=nextjs-fy27q1-nextjsworkshop&utm_content=newsletter-sponsored-link-register%20)

### 概述摘要
本内容介绍了关于调试Next.js应用的最佳实践研讨会，重点涵盖日志记录、追踪和错误监控，帮助开发者高效定位生产环境中的问题。

- 🔧 **研讨会主题**：涵盖Next.js调试最佳实践，包括日志记录、追踪和错误监控。
- 📝 **高上下文日志**：学习编写详细日志，不仅记录失败，还包含谁、什么和为什么。
- 🔍 **日志查询与告警**：针对身份验证、支付、Webhook和第三方API的静默失败进行查询和告警。
- 🌐 **分布式追踪**：深入探讨跨客户端和Node运行时的分布式追踪。
- 🔗 **日志与追踪连接**：将日志与追踪关联，无需切换工具即可获得完整上下文。
- 📚 **入门资源**：提供Sentry与Next.js集成的手动实践课程，帮助快速上手。
- 📖 **额外阅读**：包含关于Next.js日志记录和AI代理监控的更多资源。

---

### [在Chrome DevTools中调试WASM - Eli Bendersky的网站](https://eli.thegreenplace.net/2026/debugging-wasm-in-chrome-devtools/)

**原文标题**: [Debugging WASM in Chrome DevTools - Eli Bendersky's website](https://eli.thegreenplace.net/2026/debugging-wasm-in-chrome-devtools/)

## 概述总结
本文介绍了如何在Chrome DevTools中调试WebAssembly（WASM）代码，包括设置调试环境、使用断点、处理异常等实用技巧。

- 🛠️ **环境搭建**：使用`watgo`将WAT文件编译为WASM，并通过本地HTTP服务器（如`static-server`）加载`browser-loader.html`文件。
- 🔍 **调试入口**：在Chrome DevTools的“Sources”面板中，通过“Page”视图找到WASM条目，可查看反编译的WAT代码。
- ⏸️ **断点设置**：点击代码左侧的地址列即可设置断点，刷新页面后程序会停在断点处，支持单步执行、查看局部变量和调用栈。
- ⚠️ **异常调试**：勾选“Pause on exceptions”复选框后，调试器会自动停在异常指令处（如`ref.cast`失败），并在“Scope”面板显示变量的实际类型。
- 📌 **实用案例**：通过修改示例代码（如错误地假设变量类型），演示如何快速定位`ref.cast`异常来源。
- 💡 **调试器 vs printf**：在WASM中，调试器优于printf的原因包括：WASM的字符串处理复杂、gc类型对主机不透明、异常调试时调试器能直接定位问题点。

---

### [使用 .NET Native AOT 编写 Node.js 插件 - .NET 博客](https://devblogs.microsoft.com/dotnet/writing-nodejs-addons-with-dotnet-native-aot/)

**原文标题**: [Writing Node.js addons with .NET Native AOT - .NET Blog](https://devblogs.microsoft.com/dotnet/writing-nodejs-addons-with-dotnet-native-aot/)

本文介绍了如何使用 .NET Native AOT 构建 Node.js 原生插件，以简化 C# Dev Kit 的工程流程，并提供了从项目配置到实际调用的完整示例。

- 🚀 **背景与动机**：C# Dev Kit 团队原本用 C++ 和 node-gyp 构建原生插件，但需要安装旧版 Python，增加了开发者和 CI 的复杂度。团队已有 .NET SDK，因此转向 C# 和 Native AOT 来简化工具链。
- 🧩 **Node.js 原生插件原理**：Node.js 原生插件是共享库（.dll/.so/.dylib），通过 N-API（稳定 C API）与 Node.js 交互。Native AOT 可生成符合 N-API 要求的共享库，无需关心底层语言。
- ⚙️ **项目配置与入口点**：项目文件设置 `<PublishAot>true</PublishAot>` 和 `<AllowUnsafeBlocks>true</AllowUnsafeBlocks>`。通过 `[UnmanagedCallersOnly]` 导出 `napi_register_module_v1` 函数，注册 C# 函数到 JavaScript 的 exports 对象。
- 🔗 **N-API 调用与字符串处理**：使用 `[LibraryImport]` 声明 P/Invoke 方法，通过 `NativeLibrary.SetDllImportResolver` 将 "node" 库解析到宿主进程。字符串转换利用 `Span<T>`、`stackalloc` 和 `ArrayPool` 避免堆分配，实现高效 UTF-8 互转。
- 🖥️ **实际函数实现**：以读取 Windows 注册表为例，`ReadStringValue` 函数通过 `GetStringArg` 获取参数，使用 `Microsoft.Win32.Registry` API，返回字符串或 `undefined`。异常被捕获并转换为 JavaScript Error。
- 📦 **TypeScript 调用**：`dotnet publish` 生成平台特定共享库，重命名为 `.node` 文件。TypeScript 中通过 `require()` 加载，并定义类型安全接口，直接调用原生函数。
- 🔄 **现有库对比**：`node-api-dotnet` 提供更高级的框架，但本文的薄封装方式对少量函数更轻量，无额外依赖。
- ✅ **收益与展望**：简化了开发者体验（无需 Python），CI 更简单，性能与 C++ 相当。未来可探索将 .NET 逻辑直接加载到 Node.js 进程，减少进程间通信开销。
- 💡 **开发经验**：团队利用 GitHub Copilot 快速实现原型，降低了学习 N-API 的门槛，展示了 AI 工具在探索新方案中的价值。

---

### [GitHub - peterc/webassembly-simplest-demo: 一个将C语言编译为WebAssembly并运行的简单示例 · GitHub](https://github.com/peterc/webassembly-simplest-demo)

**原文标题**: [GitHub - peterc/webassembly-simplest-demo: A simple example of compiling C to WebAssembly and running it · GitHub](https://github.com/peterc/webassembly-simplest-demo)

该仓库演示了如何用最简方式将C语言编译为WebAssembly，并分别在Node.js和浏览器中运行。

- 📦 项目核心：用clang将C代码编译为.wasm文件，无需Emscripten或打包工具
- 🔧 环境要求：需安装支持wasm32目标的clang和LLVM链接器lld
- 🍎 macOS配置：需通过Homebrew安装llvm和lld（系统自带clang不支持wasm32）
- 🐧 Linux配置：直接安装clang和lld包即可
- 📝 C代码示例：提供斐波那契数列函数(fib.c)，通过循环计算第n项
- ⚙️ 编译命令：使用Makefile或直接运行clang命令，需指定wasm32目标并导出符号
- 🖥️ Node.js运行：通过node node.js执行，同样支持Bun
- 🌐 浏览器运行：需启动HTTP服务器（如python3 -m http.server），通过WebAssembly.instantiateStreaming加载
- 🚀 进阶提示：复杂场景建议参考Surma的详细教程
- ⭐ 项目状态：23个星标，2个关注，0个分支，使用Makefile/HTML/JavaScript/C语言

---

### [将Cypress升级到TypeScript v6 | 通过更好的软件创造更美好的世界](https://glebbahmutov.com/blog/upgrade-cypress-to-typescript-v6/)

**原文标题**: [Upgrade Cypress To TypeScript v6 | Better world by better software](https://glebbahmutov.com/blog/upgrade-cypress-to-typescript-v6/)

概述：Cypress v15.14 支持 TypeScript v6，这是升级到更快的 TypeScript v7（Go 实现）的最后一步。本文提供了将项目迁移到 TypeScript v6 的简明步骤和注意事项。

- 🔧 将 `moduleResolution` 从 `"node"` 改为 `"bundler"`，让 Cypress 使用 Webpack 打包转译后的代码
- 🎯 移除 `"target"` 选项，因为它默认为当前 ES 标准（es2025）
- 🧹 移除 `allowSyntheticDefaultImports: true`，因为它已默认启用
- ⚠️ 如果规格文件中使用了路径别名（如 `@support/*`），则必须保留 `baseUrl` 选项，并指向当前 `tsconfig.json` 文件夹
- 🛑 添加 `"ignoreDeprecations": "6.0"` 选项以避免弃用警告
- 📂 路径别名中的所有相对路径均相对于 `tsconfig.json` 文件

---

### [TSRX](https://tsrx.dev/)

**原文标题**: [TSRX](https://tsrx.dev/)

TSRX 是一种用于构建声明式 UI 的 TypeScript 语言扩展，旨在提升代码可读性和开发效率。

- 📝 **核心概念**：TSRX 是 JSX 的精神继承者，将结构、样式和控制流整合在模板中，作为一等语法存在，而非通过表达式插槽实现。
- 🔧 **框架无关**：支持编译到 React、Preact、Ripple、Solid 和 Vue 等多种框架，且与现有 JS/TS/TSX 代码库兼容。
- 🎯 **代码共置**：UI 结构、控制流和样式位于同一文件，减少三元表达式和渲染辅助函数，便于重构和团队协作。
- 🤖 **AI 友好**：显式的 UI 结构为编辑器、编译器和代码生成工具提供更好的工作表面，语言模型能更高效处理集中信息。
- ⚡ **人体工学优化**：自动处理框架的棘手部分，如条件性调用 React hooks、Solid props 解构保持响应性、局部变量紧邻 JSX 使用。
- 🛠️ **工具集成**：提供语言服务器（诊断、导航、补全）、Prettier 和 ESLint 插件，支持 VS Code、Zed、Neovim 等编辑器。
- 🔄 **智能编译**：通过 AST 解析和框架特定插件生成高效输出，包括作用域 CSS，新目标可添加为独立插件。
- 🚀 **开发状态**：处于活跃 alpha 阶段，欢迎在 issue tracker 上反馈意见。

---

### [瑞波TS](https://www.ripple-ts.com/)

**原文标题**: [Ripple TS](https://www.ripple-ts.com/)

Ripple 是一个融合 React、Solid 和 Svelte 优点的 TypeScript UI 框架，提供高性能、响应式状态管理和丰富的开发工具支持。

- ⚡ **响应式状态管理**：内置 `track()` 和 `&[]` 语法实现懒解构，自动追踪依赖变化
- 🧩 **组件化架构**：支持 props 和 children 的干净可复用组件设计
- 📝 **模板语法增强**：在熟悉模板基础上添加 Ripple 特有的语法优化
- 🚀 **极致性能**：细粒度渲染，在性能、包体积和内存使用上均达行业领先水平
- 🔷 **完整 TypeScript 支持**：全面集成类型检查功能
- 💻 **VSCode 集成**：提供诊断和智能感知的丰富编辑器支持
- 🔀 **原生控制流**：模板中直接支持 `if`、`for` 和 `try` 等控制语句
- 🎨 **作用域样式**：通过 `<style>` 元素实现组件级 CSS 隔离
- ✨ **Prettier 支持**：为 `.tsrx` 模块提供完整的代码格式化支持
- 🛡️ **ESLint 支持**：为 `.tsrx` 模块提供完整的代码检查集成

---

### [轻量级图表™库 — TradingView](https://www.tradingview.com/lightweight-charts/)

**原文标题**: [Lightweight Charts™ library — TradingView](https://www.tradingview.com/lightweight-charts/)

Lightweight Charts™ 是一个轻量级、功能丰富的开源图表库，仅35KB，专为金融数据可视化设计，支持实时更新、高度定制和跨设备交互。

- 📦 超轻量级：仅35KB，基于HTML5 Canvas技术，体积比标准GIF还小
- 🔄 实时更新：无需刷新页面即可显示最新数据流
- 🌐 开源免费：由TradingView维护，托管于GitHub，采用Apache 2.0许可
- ⚡ 高性能：能处理海量数据，即使数千根K线也能保持响应
- 👨‍💻 开发者友好：文档完善，集成简单，灵活直观
- 🎨 完全样式控制：支持预设和自定义主题，适配UI风格
- 📱 交互响应式：桌面和移动设备均可无缝适配
- ♿ 无障碍设计：符合主流无障碍标准，确保所有用户可访问
- 💹 金融核心：被超过4万公司和1亿交易者信赖，支持蜡烛图、线图、柱状图等多种图表类型
- 🔌 插件扩展：支持自定义图表类型、指标和插件（如波段指示器、价格提醒）
- 🤝 合作伙伴生态：被交易所、银行、媒体等顶级金融科技公司采用

---

### [轻量级图表 - 圆角蜡烛系列示例](https://tradingview.github.io/lightweight-charts/plugin-examples/plugins/rounded-candles-series/example/)

**原文标题**: [Lightweight Charts - Rounded Candles Series Example](https://tradingview.github.io/lightweight-charts/plugin-examples/plugins/rounded-candles-series/example/)

本系列蜡烛在较大尺寸时，烛体边角采用圆角设计，兼具美观与实用性。

- 🕯️ 圆角设计：大尺寸蜡烛的边角经过圆角处理，减少尖锐感，提升视觉柔和度。
- 📏 尺寸影响：圆角效果仅在蜡烛达到一定尺寸时显现，小尺寸保持常规形状。
- 🎨 系列特点：该系列注重细节与造型，圆角设计成为其标志性元素。

---

### [轻量级图表 - 箱线图系列插件示例](https://tradingview.github.io/lightweight-charts/plugin-examples/plugins/box-whisker-series/example/)

**原文标题**: [Lightweight Charts - Box Whisker Series Plugin Example](https://tradingview.github.io/lightweight-charts/plugin-examples/plugins/box-whisker-series/example/)

箱线图是一种常用于统计学的图表，用于直观展示数据集的分布和离散程度。它通过箱体表示四分位距，箱内线条显示中位数，触须延伸表示最小值和最大值，异常值则以点状显示在触须上下。

- 📊 箱体代表四分位距，涵盖数据中间50%的分布范围
- 📏 箱内线条标记中位数，反映数据的中心趋势
- 📈 触须从箱体延伸，显示数据的最小值和最大值
- 🔵 异常值以点状表示，位于触须上下方，突出离群数据

---

### [轻量级图表 - 双范围直方图系列插件示例](https://tradingview.github.io/lightweight-charts/plugin-examples/plugins/dual-range-histogram-series/example/)

**原文标题**: [Lightweight Charts - DualRangeHistogram Series Plugin Example](https://tradingview.github.io/lightweight-charts/plugin-examples/plugins/dual-range-histogram-series/example/)

此图表为双范围直方图，一种用于展示每个时间点正负值范围的柱状可视化工具。

- 📊 每组包含两正两负柱：浅色柱表示总范围，深色柱表示子集或相关成分
- 🔼 正柱向上延伸，代表上升指标（如涨幅）的总值与部分值
- 🔽 负柱向下延伸，代表下降指标（如回撤）的总值与部分值
- ✅ 深色柱值必须始终小于或等于对应的浅色柱值
- 💹 适用于金融分析、绩效回测等需要对比正负方向幅度与构成的场景

---

### [GitHub - tradingview/lightweight-charts: 使用HTML5 Canvas构建的高性能金融图表](https://github.com/tradingview/lightweight-charts)

**原文标题**: [GitHub - tradingview/lightweight-charts: Performant financial charts built with HTML5 canvas · GitHub](https://github.com/tradingview/lightweight-charts)

TradingView Lightweight Charts™ 是一个高效、轻量的金融图表库，专为在网页上快速展示交互式金融数据而设计，支持自定义插件和多种安装方式。

- 📊 核心特性：提供快速、轻量的金融HTML5图表，可替代静态图片图表，提升网页性能。
- 🚀 安装方式：支持通过npm安装（`npm install lightweight-charts`）或CDN引入（unpkg），并提供最新master版本安装选项。
- 🛠️ 使用示例：通过`createChart`和`LineSeries` API快速创建折线图，并设置时间序列数据。
- 🔌 扩展性：支持自定义插件，提供交互式示例和详细文档，方便开发者扩展功能。
- 📦 构建变体：提供ES模块和IIFE格式，包含生产版和开发版，以及独立版（含依赖）。
- 📜 许可证：基于Apache 2.0许可证，需注明TradingView为创作者，并可在图表中使用`attributionLogo`选项满足链接要求。
- 🌟 社区资源：拥有15.4k星标和2.4k分支，提供“awesome-tradingview”项目列表和相关社区项目。

---

### [Clerk CLI](https://clerk.com/cli?utm_source=cooper_press&utm_medium=newsletter&utm_campaign=cli&utm_content=04-28-26&dub_id=iDWOAe25FIGZWBTj)

**原文标题**: [Clerk CLI](https://clerk.com/cli?utm_source=cooper_press&utm_medium=newsletter&utm_campaign=cli&utm_content=04-28-26&dub_id=iDWOAe25FIGZWBTj)

概述总结
- 🤖 让AI代理通过Clerk CLI完全掌控认证设置，无需离开终端或复制粘贴API密钥
- ⚡ 仅需三个命令即可完成认证配置：`clerk init`自动检测框架并添加文件，`clerk config`通过代码管理设置，`clerk deploy`（即将推出）安全验证变更并同步生产环境
- 🛠️ 支持多种安装方式（npm/bun/pnpm/yarn/Homebrew/curl），开发者与AI代理共享统一命令行工具
- 🚀 从提示到生产：代理可自动处理认证设置、租户注册、组织配置，最终完成生产环境交接
- 🔒 专为使用AI快速安全开发的团队设计，确保认证变更可审查、可同步、可部署

---

### [GitHub - nanostores/nanostores：一个极小的（286字节）状态管理器，支持React/RN/Preact/Vue/Svelte，拥有众多可树摇的原子化存储](https://github.com/nanostores/nanostores)

**原文标题**: [GitHub - nanostores/nanostores: A tiny (286 bytes) state manager for React/RN/Preact/Vue/Svelte with many atomic tree-shakable stores · GitHub](https://github.com/nanostores/nanostores)

Nano Stores 是一个超轻量级的状态管理库，支持多种前端框架，通过原子化存储和直接操作实现高性能和可维护性。

- 📦 **极致轻量**：压缩后仅 294-831 字节，零依赖，使用 Size Limit 控制体积。
- ⚡ **高性能**：原子化和派生存储设计，避免不必要的组件重渲染。
- 🌳 **可摇树优化**：只打包组件实际使用的存储代码。
- 🧩 **框架无关**：支持 React、Vue、Svelte、Solid、Lit、Angular 等主流框架及原生 JS。
- 💡 **智能存储**：提供原子、映射、计算、异步、持久化、路由等多种存储类型。
- 🔄 **懒加载机制**：存储有挂载和禁用两种状态，仅在 UI 中使用时占用资源。
- 🛠️ **开发工具**：提供浏览器控制台日志和 Vue Devtools 插件。
- 📝 **TypeScript 友好**：完整类型支持，便于类型安全开发。
- 🧪 **测试便利**：提供 `keepMount`、`cleanStores`、`allTasks` 等测试工具。
- 🎯 **最佳实践**：倡导将逻辑从组件迁移到存储，分离变更与响应，减少 `get()` 使用。

---

### [GitHub - metafloor/bwip-js: 纯JavaScript条形码生成器 · GitHub](https://github.com/metafloor/bwip-js)

**原文标题**: [GitHub - metafloor/bwip-js: Barcode Writer in Pure JavaScript · GitHub](https://github.com/metafloor/bwip-js)

bwip-js 是一个将条形码生成功能移植到纯 JavaScript 的库，支持超过 100 种条形码类型，可在浏览器、Node.js、React Native 等平台生成 PNG、Canvas 或 SVG 格式的条形码图像。

- 📦 **多平台支持**：提供浏览器、Node.js、React Native、Electron 和命令行界面，并针对各平台有专用包（如 @bwip-js/node）
- 🎯 **丰富的条形码类型**：支持 Code128、QR Code、Data Matrix、EAN-13 等 100 多种标准条形码，涵盖线性、二维和复合符号
- 🖼️ **多种输出格式**：支持生成 PNG 图像（toBuffer）、Canvas 渲染（toCanvas）、SVG 矢量图（toSVG）和 React Native 的 Data URL
- ⚙️ **灵活的配置选项**：提供缩放、旋转、填充、背景色等参数，并兼容 BWIPP 的宽度、高度等高级设置
- 🌐 **在线服务**：包含在线条形码生成器和 API，可通过 URL 参数直接生成条形码图像
- 📚 **详细文档与示例**：提供完整的 API 参考、示例代码（包括 React、Electron、自定义字体）和演示 HTML 应用
- 🔄 **版本兼容性**：当前版本 4.10.1（2026-04-22），支持 Node.js 6.0+ 和主流浏览器
- 🛠️ **模块化设计**：支持 ES6 模块导入和 tree-shaking，可单独导入特定编码器以减小打包体积

---

### [bwip-js - JavaScript条码生成器](https://bwip-js.metafloor.com/demo/demo.html)

**原文标题**: [bwip-js - JavaScript Barcode Generator](https://bwip-js.metafloor.com/demo/demo.html)

此工具是一个纯JavaScript编写的条形码生成器，支持多种输出格式和自定义选项。

- 🔲 支持Canvas和SVG两种渲染方式
- 📏 可调整X/Y轴缩放比例
- 🔄 支持图像旋转（正常/右/左）
- 🎨 提供反转颜色功能
- 💾 可保存为PNG或JPEG格式
- 🔗 支持条形码跳转链接设置
- 🏷️ 可自定义条形码文本和替代文本
- 📐 支持多种条形码类型选择

---

### [Fresh 2.3：默认零JS、视图过渡与Temporal支持 | Deno](https://deno.com/blog/fresh-2.3)

**原文标题**: [Fresh 2.3: Zero JS by default, View Transitions, and Temporal support | Deno](https://deno.com/blog/fresh-2.3)

Fresh 2.3 发布，带来零 JavaScript 默认、视图过渡、WebSocket 支持等多项更新

- 🚀 **零 JavaScript 默认**：页面不再自动注入 JavaScript，仅当使用岛屿或局部组件时才会加载，静态页面升级后直接零 JS
- 🎨 **视图过渡支持**：通过 `f-view-transition` 属性启用，配合 CSS 自定义动画，不支持的浏览器自动降级
- 🔌 **WebSocket 原生支持**：提供 `app.ws()` 和 `ctx.upgrade()` 两种方式，支持托管模式和裸模式
- ⚡ **Vite 集成改进**：CJS 转 ESM 由 Vite 处理，移除 Babel 转换，兼容 Radix UI 等包，缓存破坏参数优化
- 🔒 **安全中间件**：新增 CSP nonce 注入（替换 'unsafe-inline'）和 IP 过滤中间件（支持 CIDR）
- 📊 **OpenTelemetry 追踪**：自动注入 W3C traceparent meta 标签，连接浏览器和服务器端追踪
- 📅 **Temporal API 支持**：所有八种 Temporal 类型可作为岛屿属性传递
- 📁 **多静态目录**：`staticDir` 支持数组，同名文件按优先级处理
- 🔄 **表单加载指示器**：支持表单提交时的加载状态，可针对不同按钮独立设置
- 🌐 **反向代理支持**：`trustProxy` 选项使 `ctx.url` 反映真实客户端 URL
- 🛠️ **其他改进**：`deno create` 支持、预编译中间件链、Windows 路径规范化、多项 bug 修复

---

### [Fresh - 简洁、易用、高效的Web框架。](https://fresh.deno.dev/)

**原文标题**: [Fresh - The simple, approachable, productive web framework.](https://fresh.deno.dev/)

概述摘要  
- 🍳 点击食谱即可将HTML内容流式加载到当前位置

---

### [GitHub - Vanilagy/mediabunny：纯TypeScript媒体工具包，用于在浏览器中直接读取、写入和转换视频与音频文件。](https://github.com/Vanilagy/mediabunny)

**原文标题**: [GitHub - Vanilagy/mediabunny: Pure TypeScript media toolkit for reading, writing, and converting video and audio files, directly in the browser. · GitHub](https://github.com/Vanilagy/mediabunny)

Mediabunny 是一个纯 TypeScript 编写的 JavaScript 媒体工具库，用于在浏览器中高效读写和转换音视频文件，零依赖且支持树摇优化。

- 🎥 支持 MP4、WebM、HLS 等 25+ 音视频编解码格式的读写与编码解码
- ⚡ 利用 WebCodecs API 实现硬件加速，微秒级精度操作
- 🔄 提供易用的转换 API，支持转码、裁剪、旋转、重采样等
- 📦 零依赖、树摇优化，最小打包仅 5KB gzipped
- 🌐 跨平台兼容浏览器和 Node.js 环境
- 🛠️ 支持内存高效流式处理任意大小文件
- 📖 提供完整文档、示例和 API 参考
- 💰 采用 MPL-2.0 开源许可，商用友好，但修改需公开源码

---

### [GitHub - mcollina/hyperid: 超快速唯一ID生成器，适用于Node.js和浏览器](https://github.com/mcollina/hyperid)

**原文标题**: [GitHub - mcollina/hyperid: Uber-fast unique id generation, for Node.js and the browser · GitHub](https://github.com/mcollina/hyperid)

hyperid 是一个为 Node.js 和浏览器设计的超快速唯一 ID 生成库，性能极高，支持多种配置选项。

- 🚀 性能极佳：基准测试显示，hyperid 的生成速度远超其他方案，最高可达每秒 9900 万次操作，在 Apple M4 Max 和 Node.js v24.13.0 上测试。
- 🔧 灵活配置：支持固定长度、URL 安全（RFC4648）、自定义起始计数器和最大整数限制等选项，满足不同需求。
- 🆔 唯一 ID 生成：通过 `instance()` 函数生成 ID，内部使用 UUID 和计数器组合，确保唯一性。
- 🔍 解码功能：提供 `hyperid.decode()` 方法，可将生成的 ID 解码为 UUID 和计数器两部分，便于调试和分析。
- 📦 轻量安装：通过 `npm i hyperid` 即可安装，使用简单，示例代码清晰。
- 📜 开源许可：基于 MIT 许可证，代码托管在 GitHub，拥有 740 颗星和 37 个复刻，社区活跃。

---

### [Svelte 积木](https://bricks.janosh.dev/)

**原文标题**: [Svelte Bricks](https://bricks.janosh.dev/)

这是一个基于 Svelte 的瀑布流布局组件演示页面，支持 SSR 和 CSS 容器查询，并提供了多种排序与列平衡选项。

- 🧱 **Svelte Bricks 组件**：支持 SSR 的瀑布流布局组件，利用 CSS 容器查询实现自动列平衡。
- 🔄 **多种排序模式**：提供 order（默认）、balanced（平衡）、balanced-stable、row-first、column-sequential、column-balanced 六种排序方式。
- 🎛️ **可调参数**：可设置项目数量（nItems=30）、最小列宽（minColWidth=330px）、最大列宽（maxColWidth=500px）和间距（gap=20px）。
- 📐 **动态尺寸与样式**：每个卡片高度随机（102-297px），使用渐变色背景，并显示当前瀑布流容器的宽高。
- 🃏 **交互功能**：支持卡片翻转（Sliding card flip?）的交互效果。

---

### [GitHub - focus-trap/focus-trap: 在DOM节点内捕获焦点。](https://github.com/focus-trap/focus-trap)

**原文标题**: [GitHub - focus-trap/focus-trap: Trap focus within a DOM node. · GitHub](https://github.com/focus-trap/focus-trap)

focus-trap 是一个轻量级的 JavaScript 库，用于将焦点限制在指定的 DOM 节点内，常用于构建无障碍模态框等组件。

- 🎯 **核心功能**：激活后，Tab/Shift+Tab 键只能在陷阱内的可聚焦元素间循环，外部点击被阻止，Escape 键可退出陷阱。
- 🔄 **生命周期管理**：提供 `activate()`、`deactivate()`、`pause()` 和 `unpause()` 方法，支持暂停/恢复陷阱行为而不完全停用。
- ⚙️ **丰富配置选项**：支持自定义初始焦点、回退焦点、外部点击行为、Escape 键行为、焦点返回逻辑等。
- 🌐 **跨框架兼容**：提供 ESM、CJS 和 UMD 格式，并可通过 `focus-trap-react` 等封装库在 React 中使用。
- 🧩 **多容器支持**：允许指定多个容器元素，焦点会在这些容器间循环。
- 🛡️ **无障碍增强**：支持 `inert` 或 `aria-hidden` 属性隔离子树，防止屏幕阅读器访问陷阱外内容。
- 🚫 **浏览器限制**：Safari 需用户启用“Tab 键高亮”功能；不再支持 IE。
- 📦 **依赖说明**：依赖 `tabbable` 库，UMD 版本需手动引入该依赖。
- ⚠️ **注意事项**：JSDom 环境需配置 `tabbableOptions.displayCheck: 'none'`；Shadow DOM 中避免使用选择器字符串。
- 🧪 **测试建议**：推荐使用 Cypress 等完整浏览器环境进行测试。

---

### [焦点陷阱演示](https://focus-trap.github.io/focus-trap/)

**原文标题**: [focus-trap demo](https://focus-trap.github.io/focus-trap/)

该页面展示了 focus-trap 库的多种交互演示，用于在网页中创建焦点陷阱，确保用户焦点被限制在特定区域内。

- 🎯 **默认行为演示**：激活后区域变粉，可通过按钮或 Escape 键退出陷阱
- 🌀 **动画对话框**：陷阱激活/关闭时带有淡入淡出动画，并显示状态提示
- 🎬 **动画触发器**：激活按钮会淡出，支持 `returnFocus` 选项控制焦点返回行为
- 🔧 **可配置 Escape 行为**：Escape 键行为可通过函数动态控制，支持条件性退出
- ❌ **Escape 键取消**：演示如何从陷阱内的子元素取消 Escape 键的默认行为
- 🎯 **初始焦点与无 Escape**：支持指定初始焦点元素，或设为 `false` 跳过初始聚焦
- 🧩 **棘手的初始焦点**：当焦点元素隐藏时，使用 `fallbackFocus` 聚焦容器
- 🔄 **初始焦点选择器与回退**：当初始焦点节点不存在时，自动回退到容器聚焦
- 📦 **初始聚焦容器**：首次聚焦在容器元素，Tab 键不会返回容器
- 🕵️ **隐藏宝藏**：焦点节点初始隐藏，激活后显示，支持 Escape 退出
- 🪆 **嵌套陷阱**：支持在陷阱内再嵌套另一个陷阱
- 👥 **同级陷阱**：多个同级陷阱，取消一个后焦点返回前一个
- ⌨️ **输入激活**：输入内容变化自动激活陷阱，不改变输入框选择
- ⏳ **延迟聚焦**：焦点放置有延迟，避免触发事件重复激活
- ⚡ **无延迟聚焦**：焦点无延迟，事件会触发陷阱关闭
- 🌳 **隔离子树**：使用 `inert` 或 `aria-hidden` 隐藏陷阱外内容
- 📻 **单选组**：陷阱内含单选组，箭头键切换选项，Tab 键只聚焦选中项
- 🖼️ **iframe 支持**：陷阱内可包含 iframe，支持 Tab 键进出
- 🔲 **在 iframe 内工作**：陷阱在 iframe 内执行，需提供 iframe 文档
- 🌑 **Shadow DOM 激活元素**：激活按钮在 Shadow DOM 内，取消后焦点返回
- 🏠 **在 Shadow DOM 内**：陷阱实例化在开放 Shadow DOM 内
- 🌓 **含 Shadow DOM 的陷阱**：陷阱包含开放和封闭 Shadow DOM 内的可聚焦元素
- 🔓 **allowOutsideClick 选项**：允许点击陷阱外特定按钮控制陷阱
- 👆 **clickOutsideDeactivates 选项**：点击陷阱外任意位置自动关闭
- 🎯 **setReturnFocus 选项**：自定义取消后焦点返回的元素
- 🔄 **setReturnFocus 函数**：动态指定取消后焦点目标
- 📦 **多元素陷阱**：焦点保持在多个元素边界内
- 🗑️ **多元素带删除**：动态更新可聚焦节点，确保至少一个容器有可聚焦节点
- ❌ **多元素全删除**：删除所有节点后，焦点回退到指定按钮
- 🎪 **多陷阱多元素**：多个陷阱各有多个元素，点击外部按钮允许
- ⏸️ **多陷阱手动暂停**：暂停前一个陷阱，取消当前陷阱不会自动恢复
- ➖ **负 tabindex**：陷阱内含可聚焦但不可 Tab 的元素
- 🔚 **负 tabindex 最后**：负 tabindex 元素在最后位置
- ➕ **正 tabindex**：支持正 tabindex 元素，但有限制
- 🌐 **开放 Web 组件**：陷阱包含开放 Web 组件内的元素
- 📚 **全局陷阱栈**：使用 window 访问陷阱栈，支持多版本库
- ⌨️ **自定义键盘导航**：使用 `j` 和 `k` 键替代 Tab 键导航
- 🚫 **与 inert 元素协作**：陷阱忽略 `inert` 属性的按钮
- 🔄 **DOM 元素移除时保持焦点**：移除当前焦点元素后，焦点仍留在陷阱内

---

### [CheerpJ 4.3 - 在浏览器中运行未经修改的Java应用程序](https://labs.leaningtech.com/blog/cheerpj-4.3)

**原文标题**: [CheerpJ 4.3 - Run unmodified Java applications in the browser](https://labs.leaningtech.com/blog/cheerpj-4.3)

CheerpJ 4.3 发布，专注于稳定性和用户体验，支持在浏览器中运行未经修改的 Java 应用，无需本地安装 Java。

- 🚀 CheerpJ 4.3 发布，支持 Java 8、11 和 17，计划支持 Java 21，提供基于 WebAssembly 的完整 JVM 和 OpenJDK 运行时。
- 🔄 通过 Library Mode 和原生方法支持，实现 Java 与 JavaScript 的深度互操作，可直接从 JavaScript 调用 Java 方法。
- 🖥️ 可运行未修改的 Java 应用（如复杂 Swing 应用）到浏览器，并支持开发新 Java 网页应用，例如 JavaFiddle 在线游乐场。
- 📁 虚拟文件系统改进：支持从 Java 窗口直接上传文件到 /files/，并新增 /files/downloads/ 目录自动下载文件到本地。
- 📱 改进移动端支持：添加长按手势模拟鼠标悬停，优化触摸事件处理，使 Java UI 组件在手机和平板上更流畅。
- 🎮 演示：Browsercraft 运行未修改的 Minecraft 客户端.jar，展示 CheerpJ 的强大能力。
- 🔮 未来计划：CheerpJ 5.0 将全面支持现代 Java，使 Java 成为 Web 的一等语言。
- 💼 许可：对 FOSS 项目、个人和单人公司免费；企业和教育机构有优惠许可选项。
- 💬 社区支持：提供详细文档和活跃的 Discord 社区，供开发者交流和使用。

---

### [GitHub - scopewu/qrcode.vue: 一款同时支持 Vue 2 和 Vue 3 的二维码生成组件。](https://github.com/scopewu/qrcode.vue)

**原文标题**: [GitHub - scopewu/qrcode.vue: A Vue component to generate qrcode. Supports both Vue 2 and Vue 3. 一款同时支援 Vue 2 和 Vue 3 的二维码组件。 · GitHub](https://github.com/scopewu/qrcode.vue)

这是一个用于生成二维码的 Vue 组件库，同时支持 Vue 2 和 Vue 3，提供丰富的自定义选项。

- 📦 **安装便捷**：通过 npm 或 yarn 安装 `qrcode.vue`，支持 CommonJS、ES 模块和 UMD 格式。
- 🖼️ **多种渲染方式**：支持 `canvas` 和 `svg` 两种渲染模式，其中 `svg` 模式可兼容 SSR。
- 🎨 **高度自定义**：可设置二维码大小、边距、纠错等级、前景/背景颜色、圆角半径等。
- 🖌️ **渐变与图片支持**：支持线性或径向渐变填充，并可嵌入图片 logo，支持镂空效果。
- 🚀 **Vue 3 增强**：3.5+ 版本导出独立 `QrcodeCanvas` 和 `QrcodeSvg` 组件，并优化 TypeScript 类型支持。
- 📜 **开源许可**：基于 MIT 许可证开源，拥有 814 颗星和 90 个 fork，社区活跃。

---

### [STRICH | 网页应用条形码扫描](https://strich.io/?ref=js-weekly)

**原文标题**: [STRICH | Barcode Scanning for Web Apps](https://strich.io/?ref=js-weekly)

STRICH 是一款基於 JavaScript/WASM 的網頁條碼掃描庫，支援即時掃描 1D/2D 條碼，無需原生應用或後端，提供簡單透明的定價與開發者友好的體驗。

- 📦 **核心功能**：STRICH 是一個 JavaScript 庫，可在瀏覽器中實現即時 1D/2D 條碼掃描，支援 Code 128、QR Code、Data Matrix 等多種格式。
- 💰 **定價透明**：提供 Basic（$99/月，10k 次掃描）、Professional（$249/月，100k 次掃描）與 Enterprise（自定義）方案，無需預付大額費用，可隨時取消，附帶 30 天免費試用。
- 🛠️ **開發者友好**：零依賴，相容所有主流框架（Angular、Vue、React 等），提供詳細文檔與 TypeScript 綁定，支援 NPM 或 CDN 安裝。
- 📱 **跨平台相容**：可在 Android 和 iOS 的主流瀏覽器上運行，利用 WebAssembly 與 WebGL 技術實現高效掃描。
- 🎯 **掃描能力強**：支援讀取模糊、破損、光線不均或反色的條碼，內建掃描 UI（含對準框、閃光燈、點擊對焦等），並提供一鍵彈出掃描器。
- 🏢 **企業級功能**：定期更新維護，支援白標籤自訂品牌、離線授權檢查（無數據離開設備），且為瑞士 GS1 解決方案合作夥伴。
- 🌐 **網頁應用優勢**：無需應用商店審核，透過連結或 QR 碼分發，降低開發成本（單一代碼庫），並支援 PWA 實現離線操作與推送通知。
- 👍 **客戶好評**：眾多用戶稱讚其穩定可靠、整合簡單、效能優於免費替代方案（如 ZXing-JS 與 Quagga），且技術支援回應迅速。

---

### [命令代码](https://commandcode.ai/?utm_source=newsletter&utm_medium=referral&utm_campaign=classified_april&utm_id=cooper_press)

**原文标题**: [Command Code](https://commandcode.ai/?utm_source=newsletter&utm_medium=referral&utm_campaign=classified_april&utm_id=cooper_press)

Command Code 是一款能持续学习开发者编码偏好的 AI 编程代理，通过其独特的 taste-1 模型大幅提升开发效率。

- 🚀 **核心功能**：Command Code 是首个能持续学习开发者编码品味的 AI 编程代理，可完成全栈项目、功能开发、Bug 修复、测试编写和代码重构。
- 🧠 **taste-1 模型**：采用元神经符号 AI 与持续强化学习，能从每次接受、拒绝和编辑中学习，自动构建项目级技能（taste）。
- ⚡ **效率提升**：编码速度提升 10 倍，代码审查加快 2 倍，Bug 减少 5 倍。
- 🛠️ **多种模式**：支持交互式 CLI、无头模式（-p, --yolo）和后台沙盒模式。
- 📚 **完整工作流**：提供 /skills 技能、/review 审查、文件操作、shell 命令、grep 搜索和扩展思考等全栈开发工具。
- 🔧 **可扩展性**：支持自定义 /agents 代理、/memory 持久记忆、/skills 技能、/commands 命令、MCP 服务器和插件。
- 👥 **团队协作**：支持 /share 会话共享、npx taste push/pull 跨项目和团队协作。
- 💡 **解决问题**：解决传统 AI 编码工具不学习用户偏好、需要反复修正的痛点，让 AI 代码真正符合开发者的编码风格。
- 🎯 **实际效果**：开发者反馈一周后减少 80% 的修正，无需重复说明偏好，代码更符合项目架构。

---

### [芯片播放器JS](https://chiptune.app/)

**原文标题**: [Chip Player JS](https://chiptune.app/)

概述摘要  
- 🖥️ 此应用需要启用JavaScript才能正常运行。

---

### [Chip Player JS - 任天堂SNES/时空之轮](https://chiptune.app/browse/Nintendo%20SNES/Chrono%20Trigger/)

**原文标题**: [Chip Player JS - Nintendo SNES/Chrono Trigger](https://chiptune.app/browse/Nintendo%20SNES/Chrono%20Trigger/)

概述摘要  
- 🔒 该应用需要启用JavaScript才能正常运行。

---

### [数据类型——将文本转化为图表的可变字体](https://franktisellano.github.io/datatype/)

**原文标题**: [Datatype — variable font that turns text into charts](https://franktisellano.github.io/datatype/)

概述摘要
Datatype是一款将文本表达式转换为内联图表的可变字体，无需JavaScript或图像即可生成条形图、折线图或饼图。

- 📊 **条形图**：通过`{b:值1,值2,...}`语法生成，支持最多20个0-100的数值，高度按百分比显示。
- 📈 **折线图**：使用`{l:值1,值2,...}`语法创建，最多20个数据点，展示趋势变化。
- 🥧 **饼图**：用`{p:值}`语法表示，单个0-100数值控制填充百分比。
- 🔧 **可变轴控制**：提供“宽度”和“重量”两个轴，可实时调整图表密度和粗细。
- 📏 **多尺寸适应**：从14px到64px均可清晰渲染，适合不同场景。
- 🌐 **上下文集成**：图表可嵌入文本、表格或仪表盘，与周围字体风格匹配（如衬线、无衬线、等宽字体）。
- 💻 **使用方式**：通过CSS加载字体，在HTML中直接输入图表表达式即可，无需额外库。
- 📂 **开源许可**：基于SIL开放字体许可证，支持下载和GitHub集成。

---

### [您的网站准备好迎接AI代理了吗？](https://isitagentready.com/)

**原文标题**: [Is Your Site Agent-Ready?](https://isitagentready.com/)

### 概述总结
该网站提供AI代理就绪性扫描工具，从5个类别（可发现性、内容可访问性、机器人访问控制、协议发现、商业支持）检查网站是否符合新兴标准，并给出优化建议。

- 🔍 **扫描工具**：输入网站URL即可检查其对AI代理的兼容性，支持自定义扫描范围。
- 📋 **五大检查类别**：包括可发现性（robots.txt、站点地图）、内容可访问性（Markdown协商）、机器人控制（AI规则）、协议发现（MCP、OAuth等）及商业支持（x402等）。
- 🚀 **快速优化建议**：优先完善robots.txt（含AI规则和站点地图指令），并确保首页暴露有用的发现头或元数据。
- 📚 **学习资源**：可参考Cloudflare Agents文档，学习如何构建和部署能与网站交互的AI代理。
- ⚙️ **代码集成**：提供可直接复制到编码助手（如Cursor、Claude Code）中的指令，帮助提升网站代理就绪性。

---

### [GitHub - cloudflare/skills: 用于教授代理如何基于Cloudflare构建的技能。· GitHub](https://github.com/cloudflare/skills)

**原文标题**: [GitHub - cloudflare/skills: Skills for teaching agents how to build on Cloudflare. · GitHub](https://github.com/cloudflare/skills)

Cloudflare Skills 是一个为 AI 代理提供构建 Cloudflare 应用能力的技能集合，支持多种代理工具和平台。

- ⭐ 该项目在 GitHub 上获得 1.3k 星标，拥有 112 个复刻，社区活跃度高
- 🔧 支持 Claude Code、Cursor、OpenCode、OpenAI Codex 和 Pi 等多种 AI 代理工具
- 📦 提供多种安装方式：插件市场、Cursor 市场、npx skills CLI 以及手动克隆复制
- 🎯 包含命令和技能两种类型：命令需显式调用，技能根据对话上下文自动加载
- 🛠️ 核心命令包括 `/cloudflare:build-agent` 和 `/cloudflare:build-mcp`，用于构建 AI 代理和 MCP 服务器
- 📚 提供 7 个实用技能：cloudflare、agents-sdk、durable-objects、sandbox-sdk、wrangler、web-perf、building-mcp-server-on-cloudflare 等
- 🌐 内置 5 个 MCP 服务器：cloudflare-api、cloudflare-docs、cloudflare-bindings、cloudflare-builds、cloudflare-observability
- 📖 提供完整文档资源：Cloudflare Agents 文档、MCP 指南、Agents SDK 仓库和入门模板
- 🔒 项目采用 Apache-2.0 许可证，并包含行为准则、贡献指南和安全政策

---

### [优秀工程师如何在大公司写出糟糕的代码](https://www.seangoedecke.com/bad-code-at-big-companies/)

**原文标题**: [How good engineers write bad code at big companies](https://www.seangoedecke.com/bad-code-at-big-companies/)

### 概述总结
大型科技公司中，优秀工程师写出糟糕代码的现象源于系统性因素，而非个人能力问题。核心原因是工程师频繁轮岗、被迫在不熟悉的代码库中工作，而公司为追求灵活性和快速响应，主动牺牲了代码质量和长期专精。

- 🏢 **新手主导代码变更**：大型公司中，大部分代码变更由入职不到半年的“新手”完成，他们需要同时适应公司、代码库甚至编程语言。
- 🔄 **频繁轮岗与重组**：工程师平均任期仅1-2年，且内部重组频繁，导致难以积累对特定系统的长期专精，而代码库寿命却长达十年以上。
- 👴 **老手资源有限**：资深工程师虽能通过深度审查减少错误，但公司不正式保留其专精，且他们自身工作超载，无法全面覆盖所有变更。
- ⏳ **时间压力与妥协**：工程师在多重截止日期下工作，只能采用“临时方案”修复问题，这些方案经粗略审查后上线，成为未来被诟病的“糟糕代码”。
- ⚖️ **公司主动权衡**：公司明知轮岗会降低代码质量，仍选择牺牲专精以换取快速部署人才到优先项目（如AI领域），这是有意的战略取舍。
- 🛠️ **工程师无力改变**：个人无法对抗系统动态，只能尽力成为“老手”来拦截最差方案，但可能因逆流而行面临绩效压力。
- 🧩 **纯工程与杂工程**：纯工程（如开发语言）追求完美，而杂工程（如维护旧系统）需在陌生环境中快速交付，糟糕代码不可避免。
- 🔍 **根源在于不熟悉**：即使工程师能力翻倍，在不熟悉的代码库中仍会犯错，因此责任应归于公司系统而非个人。

---

### [盯着墙壁提升专注力与效率 | 亚历克斯·塞利莫夫](https://www.alexselimov.com/posts/men_who_stare_at_walls/)

**原文标题**: [Staring at walls to improve focus and productivity | Alex Selimov](https://www.alexselimov.com/posts/men_who_stare_at_walls/)

### 概述总结
通过“盯墙”休息法，在信息过载时代恢复专注力与生产力，尽管执行困难但效果显著。

- 📉 **信息过载问题**：现代人日均接收约87GB信息（基于2008年数据增长推算），导致大脑疲劳和“脑雾”循环。
- ☕ **恶性循环**：睡眠不足→过量咖啡因→依赖媒体分散注意力→熬夜→重复循环，难以打破。
- 🧘 **盯墙法核心**：当感到精神疲劳时，停止屏幕娱乐，静坐5-10分钟凝视墙壁（放松焦点、用周边视觉、放空思维）。
- 😓 **执行挑战**：保持“什么都不想”极难，类似锻炼时的抗拒感，但坚持后能显著恢复专注。
- ✅ **效果与计划**：结合副交感神经激活和思维放空，有效提升生产力；作者将持续实践并分享更多策略。

---

