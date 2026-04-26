### [Node 周刊第 621 期：2026 年 4 月 23 日](https://nodeweekly.com/issues/621)

**原文标题**: [Node Weekly Issue 621: April 23, 2026](https://nodeweekly.com/issues/621)

Node Weekly 第621期主要介绍了Node.js生态中的新工具、性能改进和开发技巧。

- 🎥 Playwright新增了`page.screencast` API，支持更灵活的视频录制和视觉注释功能
- 📦 aube：一个新的Node.js包管理器，注重性能和安全性，由mise开发者打造
- 🏗️ 微软展示了用.NET Native AOT编写Node.js原生插件的新方法
- ⚡ TypeScript 7.0 Beta发布，Go语言重写后性能提升约10倍
- 🗺️ 开发者用Node.js和Turf.js构建了10KB大小的动态六边形世界地图
- 🛠️ Optique 1.0发布：类型安全的组合式CLI解析器，支持配置文件和man页面生成
- 📚 DocMD：从Markdown生成生产就绪文档的零配置站点生成器
- 🗄️ rocksdb-js：Facebook RocksDB键值存储的新版Node.js绑定
- 🐰 Bun v1.3.13：内存使用减少5%，测试功能更智能
- 🔧 多个工具更新：pnpm v11支持、node-mssql 12.5、MongoDB驱动v7.2.0等

---

### [黎明](https://aube.en.dev/)

**原文标题**: [aube](https://aube.en.dev/)

概述总结
Aube 是一款快速、高效的 Node.js 包管理器，兼容现有锁文件，提供全局存储以节省磁盘空间，并默认启用安全策略。

- 🚀 **极速性能**：比 pnpm 快 7.3 倍，比 Bun 快 3 倍，最高可达 22 倍于 pnpm，是速度最快的 Node.js 包管理器。
- 🔗 **锁文件兼容**：可直接读写 `yarn.lock`、`pnpm-lock.yaml` 或 `package-lock.json`，无需团队迁移。
- 💾 **节省磁盘**：使用全局内容寻址存储，项目间共享包文件，比 npm 少用 90% 磁盘空间。
- ⚡ **智能运行**：`aube run test` 在依赖变更时自动安装，重复运行则跳过，提升效率。
- 🔒 **安全默认**：默认启用最低发布年龄、阻止外来依赖和构建脚本审批，确保安装安全。

---

### [首页 | 准备工作](https://mise.en.dev/)

**原文标题**: [Home | mise-en-place](https://mise.en.dev/)

本工具提供多版本管理、开发工具、环境配置、任务执行及外观设置等核心功能，帮助用户高效完成开发工作。

- 🔍 搜索功能：快速定位所需资源或配置
- 🗂️ 主导航栏：清晰划分功能模块，便于操作
- 🔄 多版本管理（mise-versions）：支持软件版本切换与控制
- 🛠️ 开发工具（Dev Tools）：集成常用开发辅助工具
- 🌐 环境配置（Environments）：管理项目运行环境参数
- 📋 任务执行（Tasks）：自动化运行预设任务流程
- 🎨 外观设置（Appearance）：自定义界面主题与显示风格

---

### [基准测试 | aube](https://aube.en.dev/benchmarks.html)

**原文标题**: [Benchmarks | aube](https://aube.en.dev/benchmarks.html)

该基准测试对比了 aube、bun、pnpm、npm 和 yarn 在多种场景下的安装性能，重点关注缓存状态对速度的影响。

- 🚀 **aube 在 warm cache 场景下表现最快**：CI 安装仅需 139ms，远快于 bun（416ms）和 pnpm（1.01s）
- ❄️ **cold cache 时 bun 反超**：aube 需 1.12s，而 bun 仅 935ms，成为最慢场景下的速度冠军
- ⚡ **开发者循环中 aube 优势巨大**：`npm install && npm run test` 仅需 21ms，比 yarn（351ms）快 16 倍
- ➕ **添加依赖时 aube 依然领先**：耗时 209ms，是 bun（414ms）的一半，npm（2.89s）的十分之一
- 🧠 **速度源于底层语言差异**：aube 使用原生多线程语言重写安装管道，而非 JavaScript，但保留与 pnpm 相同的内容寻址存储和符号链接布局
- 🔬 **测试方法严谨**：使用 hyperfine 在约 1400 个真实包的中等规模项目上端到端测量，区分 warm/cold 缓存状态
- 📊 **结果可复现**：通过 `mise run bench:bump` 命令可本地复现，使用 500mbit 限速的本地注册表确保跨机器可比性

---

### [配置 | aube](https://aube.en.dev/package-manager/configuration.html)

**原文标题**: [Configuration | aube](https://aube.en.dev/package-manager/configuration.html)

### 配置概览

aube 支持从 `.npmrc`、用户 `.npmrc`、`aube-workspace.yaml`、环境变量和 CLI 标志读取配置，并兼容 pnpm 生态。现有 `pnpm-workspace.yaml` 文件可作为迁移输入。

- 🔗 **链接器**：默认 `nodeLinker=isolated`，将传递依赖限制在声明它们的包内。
- 📦 **包导入**：`packageImportMethod=auto`，根据文件系统支持自动选择引用链接、硬链接或复制。
- 🕒 **新版本发布**：`minimumReleaseAge=1440`（24小时），避免安装刚发布的版本。
- 🚫 **外来传递依赖**：`blockExoticSubdeps=true`，默认阻止传递的 git 和 tarball 依赖。
- 🛠️ **依赖脚本**：需要批准才能运行，构建脚本默认跳过。
- 🔄 **脚本前自动安装**：`aube run`、`aube test`、`aube exec` 会先修复过时的安装。
- ⚙️ **配置来源**：支持 `.npmrc`、工作区 YAML、环境变量和 CLI 标志，CLI 标志优先级最高。
- 🔍 **配置检查**：使用 `aube config` 命令查看、设置或列出配置。
- 📝 **package.json 命名空间**：支持 `pnpm.*` 和 `aube.*`，两者合并时遵循特定优先级规则（映射键冲突时 `aube.*` 优先，列表键合并，顶层 npm 标准键最高优先）。

---

### [为Cursor、Claude和Copilot编写更好的提示词 | 前端大师](https://frontendmasters.com/courses/prompt-engineering/?utm_source=email&utm_medium=nodeweekly&utm_content=promptengineering)

**原文标题**: [Write Better Prompts for Cursor, Claude & Copilot | Frontend Masters](https://frontendmasters.com/courses/prompt-engineering/?utm_source=email&utm_medium=nodeweekly&utm_content=promptengineering)

本课程系统讲解了如何通过提示工程提升AI编程工具（如Claude、ChatGPT、Copilot、Cursor）的代码质量，涵盖从基础到高级的提示技巧，并强调未来适应性。

- 📚 **课程概述**：由Sabrina Goldfarb主讲，时长3小时43分钟，适合有技术基础的“氛围编程者”，通过纯提示构建一个提示管理应用。
- 🤖 **核心提示技巧**：涵盖标准提示、零样本、单样本和少样本提示，强调提示质量直接影响输出质量。
- 🌡️ **控制参数**：介绍温度（0-2）和Top P参数，用于调整LLM输出的确定性与随机性。
- 🧠 **上下文管理**：解释令牌和上下文窗口的重要性，提示中上下文放置（开头和结尾）比中间更有效。
- 🔧 **高级技术**：包括结构化输出、链式思维提示、情感提示、分隔符和角色设定，提升复杂任务的准确性。
- 🚀 **未来适应性**：建议记录提示使用情况，测试不同模型，并调整技巧以适应模型演变。
- ⭐ **用户评价**：4.6星好评，学员认为课程实用性强，显著提升AI编程体验和效率。

---

### [使用 .NET Native AOT 编写 Node.js 插件 - .NET 博客](https://devblogs.microsoft.com/dotnet/writing-nodejs-addons-with-dotnet-native-aot/)

**原文标题**: [Writing Node.js addons with .NET Native AOT - .NET Blog](https://devblogs.microsoft.com/dotnet/writing-nodejs-addons-with-dotnet-native-aot/)

本文介绍了如何使用 .NET Native AOT 构建 Node.js 原生插件，以简化开发工具链并提升性能。

- 🚀 使用 .NET Native AOT 替代 C++ 和 node-gyp，简化了 C# Dev Kit 的构建流程，无需再安装旧版 Python。
- 🔧 通过 N-API 实现跨语言互操作，只需导出 `napi_register_module_v1` 入口点，即可让 Node.js 加载 .NET 编译的共享库。
- 📦 项目配置简洁，仅需 `<PublishAot>true</PublishAot>` 和 `<AllowUnsafeBlocks>true</AllowUnsafeBlocks>`，即可生成原生共享库。
- 🧩 使用 `[UnmanagedCallersOnly]` 导出 C# 方法，并通过 `[LibraryImport]` 调用 N-API 函数，实现字符串等数据的编组。
- ⚡ 字符串处理采用 `Span<T>`、`stackalloc` 和 `ArrayPool` 优化性能，避免不必要的堆分配。
- 🛠️ 示例展示了读取 Windows 注册表的功能，通过 C# 的 `Microsoft.Win32.Registry` API 实现，并暴露给 JavaScript 调用。
- 💻 跨平台支持：生成的 `.dll`、`.so` 或 `.dylib` 文件可在 Windows、Linux 和 macOS 上使用。
- 📚 对于复杂场景，可考虑使用 `node-api-dotnet` 等高级库，但本文的轻量封装更适合简单需求。
- 🎯 实际收益包括简化开发者环境（无需 Python）、简化 CI 流程，以及性能与 C++ 实现相当。
- 🔮 未来可探索将 .NET 逻辑直接托管在 Node.js 进程中，减少进程间通信开销。
- 🤖 GitHub Copilot 帮助团队快速验证概念，降低了学习 N-API 的门槛。

---

### [NodeConf EU | Node.js](https://www.nodeconf.eu/)

**原文标题**: [NodeConf EU | Node.js](https://www.nodeconf.eu/)

NodeConf EU 是一场于9月29日至30日在意大利博洛尼亚举办的Node.js技术会议，旨在汇聚技术社区，目前门票已开售，并开放演讲提案征集。会议由多家赞助商支持，包括白金、金、T恤、咖啡休息、银、支持及社区赞助商。

- 🎟️ 门票已开售，并开放演讲提案征集（CFP）
- 📅 会议时间：9月29日至30日，地点：意大利博洛尼亚
- 🤝 旨在汇聚Node.js技术社区，促进交流
- 🏆 赞助商层级：白金、金、T恤、咖啡休息、银、支持及社区赞助商

---

### [NodeConf EU 2026](https://docs.google.com/forms/d/e/1FAIpQLSdhxLUxB5kW8NU5Dv6PM7vvQqKLcKed45AXvsXPGN8tIkzfkg/viewform)

**原文标题**: [NodeConf EU 2026](https://docs.google.com/forms/d/e/1FAIpQLSdhxLUxB5kW8NU5Dv6PM7vvQqKLcKed45AXvsXPGN8tIkzfkg/viewform)

NodeConf EU 2026 將於義大利波隆那舉行，現正徵求演講者與贊助商。

- 🇮🇹 NodeConf EU 2026 將於義大利波隆那舉辦，帶來濃厚的義大利風情
- 📅 活動日期為 9 月 29 日至 30 日，為期兩天
- 🎤 預計有 24 位演講者，涵蓋 Node.js 核心、實際應用、創新想法及生態系統整合
- ✉️ 徵求演講提案，需提交主題、描述、講者資訊及同意資料分享
- ✈️ 提供有限且不保證的差旅補助申請選項
- 🏢 詢問公司或雇主是否對贊助感興趣

---

### [加载器：通过arcanis实现包映射 · 拉取请求 #62239 · nodejs/node · GitHub](https://github.com/nodejs/node/pull/62239)

**原文标题**: [loader: implement package maps by arcanis · Pull Request #62239 · nodejs/node · GitHub](https://github.com/nodejs/node/pull/62239)

Node.js 新增 `--experimental-package-map` 标志，允许使用静态 JSON 文件替代 `node_modules` 目录进行包解析，以解决传统解析算法的已知问题。

- 📦 **新功能**：引入 `--experimental-package-map=<path>` 标志，通过 `package-map.json` 文件声明包及其依赖关系，实现静态包解析。
- 🚫 **解决幻影依赖**：包只能导入其显式声明的依赖，防止意外访问提升的传递依赖。
- 🔗 **修复对等依赖问题**：在 monorepo 中，不同版本的对等依赖（如 React@18 和 React@19）可正确解析，避免提升导致的错误。
- ⚡ **减少 I/O 操作**：静态映射避免文件系统遍历，提升解析速度，尤其在多 Git 仓库场景中效果显著。
- 🔄 **兼容性设计**：包管理器可同时生成 `node_modules` 和 `package-map.json`，支持逐步采用，不兼容工具仍可回退到传统解析。
- 📝 **与导入映射的区别**：包映射专为 Node.js 运行时设计，支持 `exports` 和 `imports` 字段，与 Web 标准的导入映射语义不同。
- 🛠️ **包管理器集成**：Yarn、pnpm 等工具可自动生成包映射文件，通过 `NODE_OPTIONS` 注入标志，实现无缝集成。
- ❓ **严格模式讨论**：当前实现严格拒绝未声明依赖，社区讨论是否增加 `--experimental-strict-package-maps` 标志以允许回退。
- 🗂️ **扁平结构**：所有包（包括不同版本）在 `packages` 字段中以独立 ID 存储，支持复杂依赖图（如 Git 源、捆绑依赖）。
- 🔒 **路径冲突处理**：若两个包映射到同一路径，当前会抛出错误，后续计划通过包 ID 区分模块实例以支持对等依赖。

---

### [宣布 TypeScript 7.0 Beta 版 - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-7-0-beta/)

**原文标题**: [Announcing TypeScript 7.0 Beta - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-7-0-beta/)

TypeScript 7.0 Beta 已发布，基于Go语言重写，性能提升约10倍，兼容6.0语法，提供并行化编译和编辑器支持。

- 🚀 TypeScript 7.0 Beta 发布，基于Go语言完全重写，性能比6.0提升约10倍
- ⚡ 支持并行化解析、类型检查和输出，可通过 `--checkers` 和 `--builders` 控制并行度
- 🔄 与TypeScript 6.0完全兼容，可并排运行，提供 `tsgo` 命令和 `@typescript/native-preview` 包
- 🛠️ 编辑器体验提升，VS Code扩展支持自动导入、悬浮提示、内联提示等功能
- 📦 默认配置变更：`strict` 默认开启，`module` 默认 `esnext`，`target` 默认最新ECMAScript版本
- ❌ 废弃功能移除：不再支持 `target: es5`、`downlevelIteration`、`moduleResolution: node` 等
- 📝 JavaScript支持改进：更一致的类型分析，移除部分旧有JSDoc模式
- 🧪 已在微软内部及多家公司（如Bloomberg、Google、Figma等）大规模测试，稳定性高
- 🗓️ 计划在未来两个月内发布稳定版，RC版本将提前几周推出

---

### [宣布 TypeScript 6.0 - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-6-0/)

**原文标题**: [Announcing TypeScript 6.0 - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-6-0/)

TypeScript 6.0 正式发布，作为连接 5.9 和 7.0 的桥梁，引入了新功能、性能改进和大量弃用项，为过渡到基于 Go 的原生编译器（TypeScript 7.0）做准备。

- 🚀 **TypeScript 7.0 桥梁版本**：6.0 是最后一个基于 JavaScript 代码库的版本，旨在为即将到来的、用 Go 编写的原生编译器（7.0）铺平道路。
- 🎯 **减少对 `this` 的上下文敏感性**：未使用 `this` 的函数不再被视为上下文敏感，从而改善了泛型调用中的类型推断，解决了方法语法与箭头函数之间的不一致问题。
- 🆕 **支持 `#/` 子路径导入**：现在支持 Node.js 中以 `#/` 开头的子路径导入，简化了内部模块别名，无需额外路径段。
- 🔗 **`--moduleResolution bundler` 与 `--module commonjs` 组合**：允许将 bundler 模块解析与 commonjs 模块输出结合使用，为许多项目提供了更合适的升级路径。
- 🧩 **新增 `--stableTypeOrdering` 标志**：使 6.0 的类型排序行为与 7.0 保持一致，有助于诊断迁移过程中的差异，但会降低检查速度。
- 📅 **支持 `es2025` 目标与库**：添加了 `es2025` 作为 `target` 和 `lib` 选项，包含新的内置 API 类型（如 `RegExp.escape`）并移动了部分声明。
- ⏳ **新增 `Temporal` API 类型**：为已进入 Stage 4 的 Temporal 提案提供了内置类型，可通过 `--target esnext` 使用。
- 🗺️ **新增 Map `upsert` 方法类型**：为 `Map` 和 `WeakMap` 新增的 `getOrInsert` 和 `getOrInsertComputed` 方法提供了类型支持。
- 🔒 **`RegExp.escape` 方法**：新增了 `RegExp.escape` 方法，用于安全地转义正则表达式中的特殊字符，可在 `es2025` 库中使用。
- 🌐 **DOM 库合并迭代器**：`dom.iterable` 和 `dom.asynciterable` 的内容已合并到 `dom` 库中，简化了配置。
- ⚠️ **重大更改与弃用项**：引入了多项弃用和默认值更改，包括 `strict` 默认为 `true`、`module` 默认为 `esnext`、`target` 默认为当前 ES 版本、`types` 默认为 `[]`、弃用 `es5` 目标、`moduleResolution node`、`baseUrl`、`outFile`、`module` 语法用于命名空间等。
- 🛠️ **准备迁移至 7.0**：强烈建议用户在升级到 6.0 后处理弃用警告，并尝试 7.0 的原生预览版，以便平稳过渡。

---

### [宣布 TypeScript 7.0 Beta 版本 - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-7-0-beta/#updates-since-5.x-and-new-behaviors-from-6.0)

**原文标题**: [Announcing TypeScript 7.0 Beta - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-7-0-beta/#updates-since-5.x-and-new-behaviors-from-6.0)

TypeScript 7.0 Beta 发布，基于 Go 重写，速度提升约 10 倍，并带来并行化构建、编辑器优化及多项配置变更。

- 🚀 **性能飞跃**：将代码库从 TypeScript 移植到 Go，利用原生速度和共享内存并行，速度比 6.0 快约 10 倍。
- 🧪 **高度稳定**：经过十年积累的测试套件验证，已在微软内外多个百万行级代码库中使用，可立即用于日常工作和 CI 流程。
- 📦 **安装与试用**：通过 `npm install -D @typescript/native-preview@beta` 安装，使用 `tsgo` 命令；VS Code 扩展提供编辑器支持。
- 🔄 **并行化控制**：引入 `--checkers`（默认 4 个类型检查工作线程）和 `--builders`（并行项目构建）标志，支持单线程模式 `--singleThreaded`。
- ⚙️ **配置变更**：默认启用 `strict`、`module: esnext`、`noUncheckedSideEffectImports` 等；废弃 `target: es5`、`moduleResolution: node` 等，并转为硬错误。
- 📝 **JavaScript 支持调整**：统一 JS 分析逻辑，不再支持 `@enum`、`@class` 等特定模式，需使用 `@typedef` 和 `class` 声明。
- 🖥️ **编辑器体验增强**：VS Code 扩展支持自动导入、悬停提示、内联提示、代码镜头等，性能与命令行一致。
- 🗓️ **未来计划**：预计两个月内发布稳定版，后续将推出 `--watch` 优化、稳定 API（7.1+）及更多编辑器功能。

---

### [宣布 TypeScript 7.0 Beta 版本 - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-7-0-beta/#javascript-differences)

**原文标题**: [Announcing TypeScript 7.0 Beta - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-7-0-beta/#javascript-differences)

TypeScript 7.0 Beta 发布，带来基于 Go 语言重写的编译器，性能提升约 10 倍，同时保持与 6.0 版本的高度兼容性。

- 🚀 核心性能提升：TypeScript 7.0 将代码库从 TypeScript 移植到 Go，利用原生代码速度和共享内存并行，速度比 6.0 快约 10 倍。
- ✅ 高兼容性与稳定性：新代码库从现有实现方法性移植，类型检查逻辑与 6.0 结构相同，经过大规模测试和多公司验证，可直接用于日常开发。
- 🔧 安装与使用：通过 npm 安装 `@typescript/native-preview@beta`，使用 `tsgo` 命令；VS Code 有专用扩展支持。
- 📦 并行化控制：新增 `--checkers` 和 `--builders` 标志，可分别控制类型检查和项目构建的并行度；`--singleThreaded` 标志用于单线程模式。
- 🔄 与 6.0 共存：提供 `@typescript/typescript6` 包，通过 npm 别名实现 `tsc`（7.0）和 `tsc6`（6.0）并行运行，便于过渡。
- ⚙️ 默认配置变更：`strict` 默认启用，`module` 默认为 `esnext`，`rootDir` 默认为 `./`，`types` 默认为 `[]` 等，需注意调整。
- 🚫 废弃功能硬错误：`target: es5`、`downlevelIteration`、`moduleResolution: node` 等不再支持，需迁移到新选项。
- 📝 JavaScript 支持改进：重新设计 JS 文件分析，更一致地处理类型，废弃 `@enum`、`@class` 等特殊模式。
- 🖥️ 编辑器体验提升：VS Code 扩展支持自动导入、悬浮提示、内联提示、代码镜头等，性能与命令行一致。
- 📅 未来计划：未来几周内改进 `--watch` 和声明文件生成，7.1 版本提供稳定 API，预计两个月内发布正式版。

---

### [每个AI代理所需的四层生产堆栈](https://orkes.io/webinars/the-4-layer-production-stack-every-ai-agent-needs?utm_campaign=Node%20weekly&utm_source=Newsletter&utm_medium=referral)

**原文标题**: [The 4-Layer Production Stack Every AI Agent Needs](https://orkes.io/webinars/the-4-layer-production-stack-every-ai-agent-needs?utm_campaign=Node%20weekly&utm_source=Newsletter&utm_medium=referral)

概述摘要  
Orkes 推出“AI 代理所需的四层生产堆栈”网络研讨会，聚焦从原型到企业级部署的架构蓝图，强调代理在生产环境中稳定运行的关键基础设施。

- 🎯 **核心问题**：多数企业代理在演示中表现优异，但生产环境易崩溃，问题常出在底层基础设施而非模型本身。
- 🧱 **四层架构**：包括耐久性（故障恢复）、协调（多代理协作）、安全控制（人工审核与合规）、可观测性（全流程追踪与审计）。
- ⚙️ **关键工具**：开源项目 Agentspan，能将代理定义编译为持久化工作流，支持自动重试、状态恢复与人工审批。
- 🎓 **适用对象**：面向工程领导者，适合初学至企业级部署，无需先验知识，时长约40分钟。
- 📅 **活动详情**：2025年4月30日（周四）举办，分美国中部时间上午11点与下午6点两场，由Orkes产品经理与解决方案架构师主讲。
- 🖥️ **现场演示**：展示代理在进程被终止后恢复状态，以及多代理协作的实际集成案例。
- 🚀 **立即行动**：注册后可免费试用Orkes Conductor开发者版与Orkes Assistant，提前构建工作流。

---

### [仅用10KB呈现动态六边形世界地图 | Calibre 博客](https://calibreapp.com/blog/building-our-beloved-hex-map)

**原文标题**: [Delivering a dynamic hexagonal world map in just 10kb | Calibre Blog](https://calibreapp.com/blog/building-our-beloved-hex-map)

### 概述总结
本文介绍了Calibre团队如何在10kb内构建一个动态六边形世界地图，用于可视化真实用户会话性能数据，重点阐述了设计目标、技术实现和优化过程。

- 🌍 **六边形地图概述**：动态地图由2164个六边形组成，每个代表一个国家，颜色根据用户体验评级（UX Rating）显示性能状态。
- 🎯 **设计目标**：要求加载快、轻量、低画质艺术感、跨浏览器兼容、支持明暗主题。
- 🔍 **研究与灵感**：受体素几何、选举地图和抽象地理可视化启发，选择六边形地图实现简洁视觉。
- 🛠️ **技术实现**：使用Node.js管道处理10米精度的地理数据，通过Turf简化路径，采用等距投影和点内多边形检测生成SVG。
- 📦 **优化成果**：最终SVG仅144kb，经GZip压缩至10kb，利用SVG `<symbol>` 和 `<use>` 避免重复渲染，无客户端地图数据加载。
- 🌗 **主题与样式**：通过CSS `light-dark` 实现明暗主题，动态分配评级颜色，并添加径向背景光效。
- ❌ **未包含细节**：美国地图边缘包裹、塔斯马尼亚岛因太小未显示，地图在准确性和细节上有所取舍，但满足核心需求。

---

### [TypeScript高级地理空间工具包 | Turf.js](https://turfjs.org/)

**原文标题**: [Advanced geospatial toolkit for Typescript | Turf.js](https://turfjs.org/)

Turf 是一个模块化、轻量级的 JavaScript 地理空间分析库，专注于处理 GeoJSON 数据，具有易用、快速和无需服务器端处理的特点。

- 🧩 模块化设计：由小型独立模块组成，用户可按需选用所需功能
- 🌍 专注 GeoJSON：所有函数均围绕 GeoJSON 数据格式设计，简单易懂
- ⚡ 快速高效：采用最新算法，无需将数据发送至服务器即可完成分析
- 🚀 基于 React 驱动：与 React 生态兼容，提升前端开发体验

---

### [每个人都应该从npmx借鉴的功能 | Andrew Nesbitt](https://nesbitt.io/2026/04/16/features-everyone-should-steal-from-npmx.html)

**原文标题**: [Features everyone should steal from npmx | Andrew Nesbitt](https://nesbitt.io/2026/04/16/features-everyone-should-steal-from-npmx.html)

npmx 为包注册表网站提供了大量值得借鉴的功能，以下是对其核心亮点的总结：

- 📦 **显示传递安装大小**：展示包及其所有依赖的实际磁盘占用，而非仅单个压缩包大小，比 crates.io 和 PyPI 更实用。
- 🔒 **安装脚本披露**：在包页面展示 preinstall、install、postinstall 脚本及其可能拉取的 npx 包，并链接到代码浏览器，提升供应链安全。
- 🌳 **过时与脆弱依赖树**：提供可展开的依赖树，每个节点标注与最新版的差距及是否出现在 OSV 中，递归到传递依赖，类似 Google 的 deps.dev。
- 🔢 **版本范围解析**：显示 semver 范围（如 ^1.0.0）当前解析的具体版本，省去 CLI 查询步骤。
- 🔄 **模块替换建议**：对出现在 e18e 模块替换数据集中的包，给出原生 API 或更轻量替代方案的提示，并附 MDN 链接。
- 🏷️ **模块格式与类型徽章**：显示 ESM/CJS/双格式、TypeScript 类型是否捆绑、Node 引擎范围，类似 crates.io 的 MSRV 字段。
- 🌐 **多平台仓库统计**：从 GitHub、GitLab、Bitbucket 等十个平台获取星标和分支数，而非仅限 GitHub。
- 🔗 **跨注册表可用性**：标记同时存在于 JSR 的包，可用于依赖混淆检查。
- 📊 **并排包比较**：最多十个包可加载到对比视图，以表格和散点图展示各项指标，直观区分流行但沉重与小众但轻量的选项。
- 📝 **版本差异比较**：在浏览器中逐文件比较任意两个发布版本，类似 Hex 的 diff.hex.pm。
- 📈 **发布时间线带大小注释**：每个版本在时间线上标记安装大小显著变化点，便于发现意外打包测试文件的情况。
- 📉 **按版本下载分布**：将周下载量按主/次版本线分解，显示生态系统版本迁移情况，类似 RubyGems 但以分布图呈现。
- ⌨️ **命令面板**：⌘K 打开全局操作面板，包页面上输入 semver 范围可过滤版本列表。
- 🌍 **国际化**：支持超过三十种语言，包括 RTL 语言，类似 PyPI 的 Warehouse。
- ♿ **无障碍设计**：图表和视频附有长文本 aria-label 和 figcaption，命令面板支持屏幕阅读器，并有专门的无障碍声明。
- 🎮 **沙盒链接提取**：从 README 中提取 StackBlitz、CodeSandbox 等沙盒链接，方便直接试用。
- 🤖 **Agent 技能检测**：列出包含 Agent Skills 清单的包及其工具兼容性，适合检测非代码负载。
- 🐦 **基于 AT Protocol 的社交功能**：包“喜欢”和评论使用 atproto 记录，而非私有数据库，并运行自有 PDS 以保持控制。
- 🔑 **本地 CLI 管理连接器**：通过本地 npm CLI 代理包名认领等管理操作，避免 npmx 持有凭证。
- 🌙 **深色模式与自定义调色板**：已被 npmjs.com 复制，但 pkg.go.dev、crates.io 和 PyPI 早已支持。

---

### [npmx - npm注册表的包浏览器](https://npmx.dev/)

**原文标题**: [npmx - Package Browser for the npm Registry](https://npmx.dev/)

概述摘要
- 🔍 快速现代化的npm注册表浏览器，支持即时搜索功能
- 📅 最新版本v0.9.0，构建于2026年4月14日
- 🛠️ 支持多种主流框架和工具：Nuxt、Vue、React、Svelte、Vite、Next.js、Astro、TypeScript、Angular等
- 🤝 鼓励社区参与：在GitHub上贡献代码
- 💬 提供Discord社区，用于聊天、提问和分享想法
- 🐦 可通过Bluesky关注最新动态

---

### [光学](https://optique.dev/)

**原文标题**: [Optique](https://optique.dev/)

概述摘要  
组合式解析器通过小型函数构建，利用`merge()`合并选项组，`or()`处理备选方案，支持跨命令共享解析组件并保留类型信息，体现了解析器组合子的优势。

- 🧩 通过小型函数构建解析器，支持`merge()`合并选项组和`or()`处理备选方案  
- 🔗 解析器组件可跨命令共享，同时保留完整的类型信息  
- ⚙️ 解析器组合子设计模式，提供灵活且可复用的解析逻辑

---

### [optique/CHANGES.md 位于主分支 · dahlia/optique · GitHub](https://github.com/dahlia/optique/blob/main/CHANGES.md#version-100)

**原文标题**: [optique/CHANGES.md at main · dahlia/optique · GitHub](https://github.com/dahlia/optique/blob/main/CHANGES.md#version-100)

该页面是 **optique** 项目在 GitHub 上的 `CHANGES.md` 文件视图，记录了项目的变更日志。

- 📄 文件包含 6434 行代码，体积约 286 KB，内容为项目的版本更新历史。
- 🔧 页面提供代码查看、编辑、复制原始文件及下载等操作选项。
- 👁️ 项目当前有 646 个 Star、7 个 Fork，并开放了 Issues、Pull Requests 和 Discussions 功能。
- 🔒 用户需登录才能修改通知设置，但可匿名浏览文件内容。

---

### [从五个可选字段到判别联合：使用Optique 1.0进行命令行解析](https://hackers.pub/@hongminhee/2026/optique-10-discriminated-unions-for-cli)

**原文标题**: [From five optional fields to a discriminated union: CLI parsing with Optique 1.0](https://hackers.pub/@hongminhee/2026/optique-10-discriminated-unions-for-cli)

### 概述摘要
Optique 1.0 是一个 TypeScript CLI 解析库，通过可组合的解析器（如 `or()`、`object()`）和判别联合类型，将互斥选项、必需选项、多来源值（argv、环境变量、配置文件、提示）的约束编码到类型系统中，从而消除运行时检查与类型知识之间的差距。

- 🛠️ **类型安全的约束**：使用 `or()` 和 `object()` 构建解析器，自动生成判别联合类型，确保互斥选项（如 token、basic auth、OAuth）在类型层面被正确区分，无需手动类型断言。
- 🔄 **多来源值统一处理**：通过 `bindEnv()`、`bindConfig()`、`prompt()` 包装器，从命令行、环境变量、配置文件、交互式提示中获取值，并自动按优先级（CLI > env > config > prompt）解析，类型保持不变。
- ✅ **约束不泄露**：`Parser.validateValue()` 方法确保来自环境变量、配置文件或默认值的值也会经过 CLI 解析器的约束验证（如端口范围 `1024-65535`），防止绕过。
- 📦 **与 Commander.js/Yargs 对比**：Commander.js 的 `.conflicts()` 和 Yargs 的 `.implies()` 仅作用于运行时，不反映到类型；Optique 将约束编码到类型中，编译器能直接捕获错误（如 `parsed.username` 在 token 分支中报错）。
- ⚠️ **适用场景**：适合具有复杂结构（互斥组、必需选项、多来源值、子命令）的 CLI；简单 CLI（如四个标志）应使用 Commander.js 以降低开销。
- 📚 **1.0 稳定性**：API 已稳定（env、config、prompt 包），文档位于 optique.dev，支持 Node.js 和 Bun，但生态较小。

---

### [几秒钟内从Markdown构建生产就绪的文档——docmd](https://docmd.io/)

**原文标题**: [
        Build production-ready docs from Markdown in seconds
         — docmd
        
      ](https://docmd.io/)

### 概述

docmd 是一款零配置的文档引擎，可将 Markdown 快速转换为生产级文档网站，注重 AI 就绪、SEO 优化和极速性能。

- 📄 **一键生成**：通过 `npm i @docmd/core` 安装，无需 React 或配置文件，即可将 Markdown 转为静态 HTML 和 SPA。
- 🎨 **复杂布局**：支持 Markdown 原生容器语法，实现标注、卡片、标签页等复杂布局，无需 HTML。
- 🌗 **主题与搜索**：内置明暗主题，提供零 API 密钥的离线模糊搜索，100% 隐私。
- 🔌 **插件生态**：默认包含搜索、SEO、站点地图、分析、LLM 上下文和 Mermaid 图表六大核心插件，可选 PWA、评论、数学公式等扩展。
- 📚 **版本管理**：原生支持多版本文档切换（如 v0.7.0、v0.6.0、v0.5.0）。
- 🤖 **AI 就绪**：自动生成 `llms.txt` 和 `llms-full.txt`，为 AI 代理提供语义化上下文信号。
- ⚡ **极致性能**：客户端 JS 小于 20KB，零重新加载导航，Lighthouse 评分 100，SPA 过渡延迟接近 0ms。
- 🌐 **国际化**：支持多语言（中、英、日等），具备本地化 URL、搜索和 UI 字符串。
- 🚀 **一键部署**：生成针对 Docker、Nginx 和 Caddy 的配置，开箱即用。
- 📝 **变更日志**：提供美观的时间线组件，用于发布说明和版本更新。

---

### [docmd 文档：从 Markdown 零配置生成文档](https://docs.docmd.io/)

**原文标题**: [
      docmd docs: zero-config docs from Markdown
    ](https://docs.docmd.io/)

## 概述
docmd 是一个将 Markdown 文件一键转换为生产级文档网站的工具，具备静态 HTML、SPA 速度、AI 就绪等特性，无需配置文件或样板代码。

- 🚀 **即时启动**：只需 `npx @docmd` 一个命令，即可从 `docs/` 文件夹生成完整文档网站，包含导航、搜索、SEO 和站点地图
- 🤖 **AI 优化**：自动生成 `llms.txt` 和 `llms-full.txt` 文件，让文档默认对大型语言模型友好
- 🔍 **内置搜索**：基于 MiniSearch 的客户端全文搜索，支持多版本和多语言环境，零配置即可使用
- 🎨 **主题引擎**：支持切换内置主题或自定义主题，兼容亮色、暗色和系统偏好模式
- 🌍 **原生国际化**：提供一流的多语言支持，包括语言优先 URL、按语言搜索和翻译后的 UI 字符串
- 📦 **扩展 Markdown**：通过丰富的容器语法（如标注、标签页、卡片、网格、折叠区等）超越静态文本
- 💻 **交互沙盒**：使用 Live Preview API 在页面中嵌入可编辑的实时代码预览窗口
- 💬 **内联协作**：在开发模式下选中文本可打开 Threads，与文档团队直接留言讨论

---

### [发布 docmd@0.7.2 🚀（Docker、NGINX 和 Caddy 自动部署）· docmd-io/docmd · GitHub](https://github.com/docmd-io/docmd/releases/tag/0.7.2)

**原文标题**: [Release docmd@0.7.2 🚀 (Auto-Deploy for Docker, NGINX & Caddy) · docmd-io/docmd · GitHub](https://github.com/docmd-io/docmd/releases/tag/0.7.2)

以下是您提供的文本内容的概述和要点总结：

概述总结  
- 🚀 **docmd 0.7.2 发布**：新增 `docmd deploy` 命令，可一键生成 Docker、Nginx 和 Caddy 的生产级部署配置。  
- ⚙️ **智能配置感知**：部署命令自动读取 `docmd.config.js`，提取项目标题、输出目录、站点 URL 和 SPA 模式，生成个性化文件。  
- 🐳 **Docker 支持**：生成多阶段构建的 Dockerfile，包含 `package.json` 层缓存和版本锁定的 `@docmd/core`。  
- 🌐 **Nginx 模板**：包含安全头、GZIP 压缩和不可变资产缓存，并自动配置 `server_name`。  
- 🛡️ **Caddy 模板**：支持自动 HTTPS、安全头、SPA 路由和静态资产缓存。  
- 🔄 **始终同步**：每次运行 `docmd deploy` 都会重新生成部署文件，确保与最新配置一致。  
- 🧩 **稳定性增强**：内部验证引擎重构为 7 个逻辑支柱，新增动态完整性引擎，可即时捕获版本不匹配问题。  
- 🌍 **全球生态扩展**：核心引擎新增德语、西班牙语、日语和法语的原生 UI 翻译，文档站点已完全翻译为德语。  
- 📝 **完整变更日志**：包括新命令、配置感知脚手架、统一配置标签、SEO 插件改进、错误修复（如 CLI 参数解析、Caddy 配置语法等）。  
- ⬆️ **升级方式**：运行 `npm install -g @docmd/core` 即可更新。

---

### [博客 | Node.js 的新 RocksDB 绑定](https://www.harper.fast/resources/new-rocksdb-binding-for-node-js)

**原文标题**: [Blog  | New RocksDB Binding for Node.js](https://www.harper.fast/resources/new-rocksdb-binding-for-node-js)

Harper 发布了 rocksdb-js，一个为 Node.js 打造的现代 RocksDB 绑定，支持完整事务、惰性范围查询和 TypeScript API，专为 Harper 5.0 及高并发写入场景设计。

- 🚀 **全新绑定**：从零构建的 C++ 绑定，直接使用 Node-API，避免旧抽象层开销，提供完整事务、惰性迭代器和内置事务日志。
- 🛠️ **事务支持**：支持乐观和悲观事务，实现原子性提交和真实隔离级别，适合高并发下的复杂多记录更新。
- 📚 **惰性范围查询**：返回可迭代对象，按需从磁盘读取记录，内存使用与处理数据量成正比，避免加载不必要的数据。
- ⚡ **预编译二进制**：提供 macOS、Linux、Windows 等多平台预构建二进制文件，安装仅需约 12 秒，大幅提升开发体验。
- 📝 **内置事务日志**：集成事务日志系统，支持变更追踪、事件溯源和复制，为 Harper 的节点同步和实时消息提供基础。
- 🔓 **开源与社区**：采用 Apache 2.0 许可，鼓励社区贡献，包括测试、基准测试、自定义存储和平台测试，以完善功能和覆盖更多场景。

---

### [GitHub - facebook/rocksdb：一个提供可嵌入、持久化键值存储的库，适用于快速存储。](https://github.com/facebook/rocksdb)

**原文标题**: [GitHub - facebook/rocksdb: A library that provides an embeddable, persistent key-value store for fast storage. · GitHub](https://github.com/facebook/rocksdb)

RocksDB 是由 Facebook 数据库工程团队开发维护的持久化键值存储库，专为闪存和 RAM 存储优化，基于 LevelDB 构建，采用 LSM 树设计，支持灵活的读写放大与空间放大权衡。

- 📦 提供嵌入式、持久化键值存储库，适合快速存储服务器，尤其适用于闪存驱动器
- 🔄 采用日志结构合并数据库（LSM）设计，可在写放大、读放大和空间放大之间灵活权衡
- 🧵 支持多线程压缩，特别适合存储数 TB 级别的单数据库数据
- 📂 公共接口位于 `include/` 目录，内部 API 可能随时更改
- 🌐 提供示例代码（examples 目录）和 GitHub Wiki 文档
- 💬 欢迎通过 Facebook RocksDB 开发者群组和 Google Groups 邮件列表讨论
- ⚖️ 采用双重许可证：GPLv2 和 Apache 2.0，用户可自行选择
- ⭐ 拥有 31.6k 星标、6.8k 分支、981 关注者，社区活跃
- 🛠️ 主要编程语言为 C++（84%），另有 Java、Starlark、C、Python 等
- 📦 已发布 213 个版本，最新为 v11.0.4（2026年4月7日）

---

### [GitHub - HarperFast/rocksdb-js: 用于Node.js的RocksDB绑定](https://github.com/HarperFast/rocksdb-js)

**原文标题**: [GitHub - HarperFast/rocksdb-js: RocksDB binding for Node.js · GitHub](https://github.com/HarperFast/rocksdb-js)

rocksdb-js 是一个 Node.js 的 RocksDB 绑定库，提供高性能的键值存储操作，支持事务、范围查询、统计、事件和自定义存储等功能。

- 📦 **核心功能**：支持乐观和悲观事务、混合同步/异步数据检索、范围查询返回可迭代对象（支持懒加载）
- 🔧 **数据库操作**：提供 `open`、`close`、`clear`、`destroy`、`drop`、`flush` 等方法，支持同步和异步版本
- 🔑 **数据操作**：支持 `get`、`put`、`remove`、`getRange`、`getKeys` 等操作，键值支持高效二进制编码
- 🔄 **事务系统**：支持同步和异步事务，自动提交或回滚，可配置重试逻辑和快照控制
- 📊 **统计与监控**：可启用 RocksDB 内部统计（ticker 和 histogram），提供 `getStats`、`getStat` 方法
- 🔒 **独占锁**：提供 `tryLock`、`unlock`、`withLock` 等线程安全锁机制
- 📝 **事务日志**：支持自定义事务日志记录、查询、清理，日志文件可解析
- 🎯 **事件系统**：提供类似 EventEmitter 的异步事件通知，支持 `addListener`、`notify`、`once` 等
- 🛠 **自定义存储**：可扩展 `Store` 类，覆盖默认数据库交互方法（如编码、获取、写入）
- 🌐 **跨平台支持**：支持 Linux、macOS、Windows 上的 Node.js 和 Bun 运行环境
- ⚙️ **开发工具**：提供调试构建、测试覆盖、环境变量配置（如 RocksDB 版本、C 运行时选择）

---

### [Bun v1.3.13 | Bun 博客](https://bun.com/blog/bun-v1.3.13)

**原文标题**: [Bun v1.3.13 | Bun Blog](https://bun.com/blog/bun-v1.3.13)

## 概述总结

Bun 最新版本带来了大量性能优化和新功能，包括测试工具增强、安装过程优化、内存使用减少、JavaScript 引擎升级等多项改进。

- 🚀 **测试工具大幅增强** - 新增 `--isolate`（每文件独立环境）和 `--parallel`（多进程并行）标志，以及 `--shard`（CI 分片）和 `--changed`（仅运行变更文件）功能，显著提升大型测试套件速度
- 📦 **安装过程优化** - `bun install` 现在流式解压 tarball 到磁盘（内存减少 17 倍），隔离链接器使 peer-heavy monorepo 安装从 20.5 秒降至 2.4 秒
- 💾 **内存使用显著降低** - 运行时内存减少 5%，源映射内存使用降低最多 8 倍（从 20 B/映射到 2.4 B/映射），mimalloc 升级到 v3 并实现 libpas scavenger
- ⚡ **JavaScriptCore 引擎升级** - 合并 1316 个上游提交，带来数组长度内联缓存、字符串方法 JIT 优化、SIMD 加速等多项性能改进
- 🔐 **加密功能扩展** - 新增 SHA3 系列哈希算法支持、X25519 `deriveBits` 支持，以及 BoringSSL 更新带来的后量子算法（ML-KEM/ML-DSA）
- 🌐 **网络功能增强** - `Bun.serve()` 支持 Range 请求（206 Partial Content）、WebSocket 客户端支持 Unix 域套接字、文件流式传输改进
- 📈 **压缩性能大幅提升** - zlib 升级到 zlib-ng 2.3.3，gzip 压缩速度提升最多 5.5 倍，支持 AVX-512/AVX2/NEON/SVE 等 SIMD 加速
- 🛠️ **大量 Bug 修复** - 修复 Worker 生命周期崩溃、Node.js 兼容性问题、内存泄漏、Windows 平台问题、CSS 解析器回归等数十个问题
- 🔧 **开发者体验改进** - `bunx claude` 现在可作为 `bunx @anthropic-ai/claude-code` 的简写，独立 HTML 构建正确内联 JS 导入的文件加载器资源

---

### [Bun v1.3.13 | Bun 博客](https://bun.com/blog/bun-v1.3.13#bun-s-runtime-uses-5-less-memory)

**原文标题**: [Bun v1.3.13 | Bun Blog](https://bun.com/blog/bun-v1.3.13#bun-s-runtime-uses-5-less-memory)

## Bun 新版本功能概览

- 🚀 **测试性能大幅提升** — 新增 `--isolate` 和 `--parallel` 标志，支持文件隔离和并行测试，大幅加速大型测试套件
- 📊 **CI 分片测试** — `--shard=M/N` 支持跨 CI 任务拆分测试文件，与 Jest/Vitest 语法兼容
- 🔍 **智能变更测试** — `--changed` 标志仅运行受 git 变更影响的测试文件，支持与 `--watch` 组合使用
- 📦 **安装优化** — `bun install` 流式解压 tarball，内存减少 17 倍；隔离链接器使大型 monorepo 安装从 20.5s 降至 2.4s
- 💾 **内存效率提升** — 源映射内存减少 8 倍（2.4 bytes/映射）；运行时内存使用降低 5%
- ⚡ **JavaScriptCore 引擎升级** — 合并 1316 个上游提交，带来数组长度内联缓存、SIMD 加速字符串比较等性能改进
- 🌐 **HTTP 服务增强** — 支持 Range 请求（206 部分内容）、文件流式传输（SSL/Windows）、WebSocket Unix 套接字连接
- 🔐 **加密功能扩展** — 支持 SHA3 哈希算法、X25519 密钥派生、ML-KEM/ML-DSA 后量子算法
- 🗜️ **压缩性能飞跃** — zlib-ng 升级使 gzip 压缩速度提升高达 5.5 倍
- 🐛 **大量 Bug 修复** — 修复 Worker 崩溃、HTTP/2 兼容性、文件描述符泄漏、内存泄漏等 50+ 问题

---

### [GitHub - pnpm/action-setup: 安装 pnpm 包管理器 · GitHub](https://github.com/pnpm/action-setup)

**原文标题**: [GitHub - pnpm/action-setup: Install pnpm package manager · GitHub](https://github.com/pnpm/action-setup)

pnpm/action-setup 是一个 GitHub Action，用于在 CI/CD 工作流中安装 pnpm 包管理器，支持版本选择、自动安装依赖和缓存优化。

- ⚠️ **v2 版本已失效**：v2 在新版 Node.js 上停止工作，建议升级到最新版本以修复问题。
- 🔧 **核心输入参数**：支持 `version`（指定 pnpm 版本，可选）、`dest`（存储路径）、`run_install`（自动运行 `pnpm install`）、`cache`（缓存 pnpm 存储目录）等。
- 📦 **安装方式灵活**：可通过 `package.json` 的 `packageManager` 字段自动获取版本，或直接指定版本号（如 `10`、`10.9.8`、`latest`）。
- 🚀 **依赖安装选项**：`run_install` 支持递归安装、指定工作目录、添加额外参数（如 `--strict-peer-dependencies`），并可执行多个安装命令。
- 💾 **缓存加速**：设置 `cache: true` 可缓存 pnpm 存储目录，基于 `pnpm-lock.yaml` 的哈希值作为缓存键，减少安装时间。
- 🔗 **输出路径**：提供 `dest`（扩展后的目标路径）和 `bin_dest`（pnpm/pnpx 命令位置）两个输出。
- ⚡ **独立模式**：设置 `standalone: true` 可安装 `@pnpm/exe`（含 Node.js 的捆绑包），用于兼容不匹配的 Node.js 和 pnpm 版本。
- 📝 **注意事项**：此 Action 不安装 Node.js，需配合 `actions/setup-node` 使用；无需手动运行 `pnpm store prune`，后处理会自动清理。
- 🏷️ **开源与社区**：MIT 许可证，拥有 1.2k Star、189 Fork、29 个发布版本，主要语言为 TypeScript（88.5%）。

---

### [发布 pnpm 11 RC 0 · pnpm/pnpm · GitHub](https://github.com/pnpm/pnpm/releases/tag/v11.0.0-rc.0)

**原文标题**: [Release pnpm 11 RC 0 · pnpm/pnpm · GitHub](https://github.com/pnpm/pnpm/releases/tag/v11.0.0-rc.0)

pnpm v11.0.0-rc.0 是一个重大版本更新，引入了多项破坏性变更和新功能，旨在提升性能、安全性和用户体验。

- 🚀 **核心要求升级**：要求 Node.js 22+，放弃对 Node 18-21 的支持；pnpm 自身转为纯 ESM；独立 exe 版本需要 glibc 2.27 以上。
- 🛡️ **供应链安全默认开启**：`minimumReleaseAge` 默认设为 1 天（新发布包 24 小时内不可解析），`blockExoticSubdeps` 默认启用。
- ⚙️ **构建依赖配置简化**：用 `allowBuilds` 替代了旧的 `onlyBuiltDependencies`、`neverBuiltDependencies` 等多项设置。
- 🗂️ **全局安装隔离化**：`pnpm add -g` 现在每个包拥有独立的 `package.json`、`node_modules` 和锁文件，并使用全局虚拟存储。
- 🗄️ **新的 SQLite 存储索引**：存储版本升至 v11，使用 SQLite 数据库替代 JSON 文件，减少系统调用并加速安装。
- 🎯 **原生发布流程**：`pnpm publish`、`login`、`logout`、`view`、`deprecate`、`unpublish`、`dist-tag` 和 `version` 不再依赖 npm CLI。
- 📝 **配置迁移**：`.npmrc` 仅用于认证和注册表设置，其他配置需移至 `pnpm-workspace.yaml` 或全局 `config.yaml`；环境变量使用 `pnpm_config_*` 前缀。
- ✨ **新增命令**：`pnpm ci`、`pnpm sbom`、`pnpm clean`、`pnpm peers check`、`pnpm runtime set`，以及短别名 `pn` 和 `pnx`。
- 📦 **ESM pnpmfile 支持**：`.pnpmfile.mjs` 优先级高于 `.pnpmfile.cjs`。
- 🔧 **安全修复新方式**：`pnpm audit --fix=update` 通过更新锁文件中的包来修复漏洞，而非添加覆盖。
- ⚡ **性能大幅提升**：使用 undici 实现 Happy Eyeballs、直接写入 CAS、跳过暂存目录、预分配 tarball 下载、NDJSON 元数据缓存等优化。
- ❌ **移除旧命令和 npm 回退**：不再回退到 npm CLI，移除 `pnpm server` 命令，以及 `useNodeVersion` 等字段支持。
- 🔄 **锁文件格式简化**：`patchedDependencies` 格式从 `Record<string, { path, hash }>` 简化为 `Record<string, string>`。

---

### [GitHub - tediousjs/node-mssql: Node.js 的 Microsoft SQL Server 客户端](https://github.com/tediousjs/node-mssql)

**原文标题**: [GitHub - tediousjs/node-mssql: Microsoft SQL Server client for Node.js · GitHub](https://github.com/tediousjs/node-mssql)

node-mssql 是一个用于 Node.js 的 Microsoft SQL Server 客户端库，支持多种 TDS 驱动程序和丰富的数据库操作功能。

- 📦 **支持多种驱动程序**：默认使用 Tedious（纯 JavaScript，跨平台），可选 MSNodeSQLv8（Windows/Linux/macOS 64 位）
- 🚀 **多种连接方式**：支持连接字符串、配置对象和 Windows 身份验证，并提供连接池管理
- 🔧 **丰富的查询操作**：支持 Async/Await、Promises、回调、流式查询和 ES6 模板字面量
- 🛡️ **内置安全防护**：自动参数化查询防止 SQL 注入，支持连接验证和错误处理
- 📊 **高级功能支持**：包括事务、预编译语句、批量插入、表值参数 (TVP) 和 JSON 解析
- 🌍 **地理空间数据支持**：内置 Geography 和 Geometry 数据类型解析器
- 🔍 **诊断与监控**：通过 diagnostics_channel 发布遥测数据，支持 OpenTelemetry 集成
- 📚 **详尽文档**：提供从入门到高级的完整示例，包括版本迁移指南

---

### [GitHub - privatenumber/type-flag: ⛳️ 用于Node.js的类型化命令行参数解析器](https://github.com/privatenumber/type-flag)

**原文标题**: [GitHub - privatenumber/type-flag: ⛳️ Typed command-line arguments parser for Node.js · GitHub](https://github.com/privatenumber/type-flag)

type-flag 是一个强类型的命令行参数解析库，体积小巧（最大1.4 kB），无依赖且支持摇树优化，适合 Node.js 项目使用。

- 🚀 **快速安装与使用**：通过 `npm i type-flag` 安装，支持 `typeFlag()` 和 `getFlag()` 两种解析方式，示例中可轻松解析 `--name John --age 20` 等参数。
- 🔧 **灵活定义标志**：支持字符串、数字、布尔等默认类型，以及数组类型（如 `[String]`），可通过对象语法设置别名、默认值，并自动将 kebab-case 映射为 camelCase。
- 🎯 **高级特性**：包括未知标志解析、标志值分隔符（`=`、`:`、`.`）、参数收集（`_` 属性）、布尔取反（`--no-` 前缀）、标志计数（如 `-vvv`）等。
- 📦 **API 与配置**：`typeFlag()` 接受标志模式、argv 数组和选项（如 `ignore` 回调、`booleanNegation`），`getFlag()` 提供更简洁的单标志解析。
- 💡 **实用示例**：支持自定义类型（如枚举 `size`）、可选值标志、点嵌套标志（如 `--env.TOKEN=123`），并内置 AI 编码助手技能。

---

### [发布 v7.2.0 · mongodb/node-mongodb-native · GitHub](https://github.com/mongodb/node-mongodb-native/releases/tag/v7.2.0)

**原文标题**: [Release v7.2.0 · mongodb/node-mongodb-native · GitHub](https://github.com/mongodb/node-mongodb-native/releases/tag/v7.2.0)

概述摘要  
MongoDB Node.js 驱动程序 v7.2.0 发布，新增智能工作负载管理、运行时兼容性改进和 ChangeStream 增强功能。  

- ⚙️ 支持 MongoDB 智能工作负载管理，新增 `maxAdaptiveRetries` 和 `enableOverloadRetargeting` 选项，优化高负载下的连接建立和重试机制。  
- 🧩 运行时兼容性改进：用标准 `Uint8Array` 替代 Node.js 的 `Buffer`，用 Web Crypto API 替代 Node.js 的 `crypto`，减少非 Node.js 运行时的补丁需求。  
- 🧪 实验性支持依赖注入：新增 `runtimeAdapters` 选项，允许注入核心 Node.js 模块（如 `os`），提升在受限环境中的兼容性。  
- ☀️ ChangeStream 新增 `bufferedCount()` 方法，可返回本地缓冲文档数量，无需调用异步方法即可检查数据。  
- 🔄 重试循环引入指数退避和抖动机制，提升高负载下的稳定性。  
- 📦 其他改进：限制副本集服务器降级仅针对过载错误，使令牌桶在客户端反压中可选，并最终确定反压实现。

---

### [发布 9.5.0 · Automattic/mongoose · GitHub](https://github.com/Automattic/mongoose/releases/tag/9.5.0)

**原文标题**: [Release 9.5.0 · Automattic/mongoose · GitHub](https://github.com/Automattic/mongoose/releases/tag/9.5.0)

Mongoose 9.5.0 版本发布，包含多项新功能、错误修复和性能优化。

- 🎉 新增 debug 输出的 `timestamp` 选项 (#16216)
- 🔧 新增 `cloneUpdate` 选项以显式禁用更新克隆 (#16230, #16202)
- 🔍 扩展 `defaults` 查询选项至 `find()` 方法 (#16226)
- 🚀 优化更新克隆逻辑，避免不必要克隆以更好支持 `__proto__` (#16230, #16202)
- 🛠️ 修复将含有 `$set()` 方法的文档误判为对象的问题 (#16230)
- 🔄 修复查询助手向鉴别器传递默认选项 (#16227, #16226)
- 📄 修复乐观并发下嵌套路径的包含与排除处理 (#16177, #16054)
- ❌ 在 `insertOne()` 中若文档非对象则抛出 `ObjectParameterError` (#16221)
- 🗣️ 修复 `CastError` 消息在 `setModel()` 后保留原因 (#16167, #White-Devil2839)
- ⚡ 移除 `findOneAndUpdate()` 中的不必要克隆以提升性能 (#16230)
- 🔄 使用 kareem 3.3.0 版本 (#16229)
- 🧪 改用 TSTyche 断言 (#16222)

---

### [pg-boss 文档](https://timgit.github.io/pg-boss/)

**原文标题**: [pg-boss Docs](https://timgit.github.io/pg-boss/)

概述摘要：  
本文探讨了人工智能在医疗领域的应用，重点介绍了诊断辅助、药物研发和患者监测三大方面，并强调了数据隐私和伦理挑战的重要性。  

- 🩺 诊断辅助：AI通过分析医学影像（如X光片、CT扫描）提高疾病检测的准确性和效率。  
- 💊 药物研发：机器学习加速候选药物筛选和临床试验设计，缩短新药上市周期。  
- 📊 患者监测：可穿戴设备与AI结合，实时追踪生命体征并预警潜在健康风险。  
- 🔒 数据隐私：医疗数据共享需严格加密，防止泄露患者敏感信息。  
- ⚖️ 伦理挑战：算法偏见和决策透明度问题需通过监管框架解决。

---

### [GitHub - XeroAPI/xero-node: 基于XeroAPI/Xero-OpenAPI生成的Xero Node SDK，用于OAuth 2.0](https://github.com/XeroAPI/xero-node)

**原文标题**: [GitHub - XeroAPI/xero-node: Xero Node SDK for OAuth 2.0 generated from XeroAPI/Xero-OpenAPI · GitHub](https://github.com/XeroAPI/xero-node)

xero-node 是 Xero 官方推出的 Node.js SDK，支援 OAuth 2.0 認證，讓開發者能輕鬆整合 Xero 的會計、資產、薪資等多種 API，並提供完整的文件與範例應用。

- 📘 **完整 API 支援**：涵蓋 Accounting、Assets、Bankfeeds、Files、Projects 及多國 Payroll API。
- 🔐 **OAuth 2.0 認證**：支援授權碼流程與客戶端憑證流程，並內建 JWT 驗證與 CSRF 防護。
- ⚙️ **簡易安裝與設定**：透過 npm 安裝，只需提供 client ID、secret、redirect URI 與 scopes 即可初始化。
- 🧩 **多種認證模式**：支援標準 OAuth 2.0、Custom Connections（M2M）及 App Store 訂閱管理。
- 📦 **Token 管理**：提供 refreshToken、setTokenSet 等方法，方便儲存與更新存取權杖。
- 🧪 **豐富範例應用**：包含 starter-app、full-app、custom-connections-starter 等，快速上手。
- 🛠️ **實用輔助方法**：如 buildConsentUrl、apiCallback、disconnect、formatMsDate 等，簡化開發流程。
- 🔍 **查詢與過濾**：支援 where、order、page 等參數，並建議使用 undefined 而非 null 避免查詢錯誤。
- 🤝 **社群貢獻**：遵循 MIT 授權，歡迎提交 PR 與 issue，並採用 Contributor Covenant 行為準則。

---

### [小型企业会计软件 | Xero 香港](https://www.xero.com/hk/)

**原文标题**: [Accounting Software for Small Businesses | Xero HK](https://www.xero.com/hk/)

Xero 是一款专为小型企业和个体经营者设计的会计软件，帮助用户专注于业务增长，并利用AI助手JAX提升效率。

- 📊 Xero会计软件专为小型企业和个体经营者设计，支持账单支付、费用报销等功能
- 🤖 新增AI财务助手JAX，可自动处理日常任务、提供实时业务洞察
- 💰 提供三种定价方案：Starter（$5.80/月）、Standard（$10/月）、Premium（$15/月），均有3个月折扣
- 🏢 支持多种业务类型：自雇人士、建筑行业、零售业等
- 🔗 可与多种应用集成，扩展功能
- 👥 为会计师和簿记员提供专业支持
- 🆓 提供30天免费试用，无需信用卡，可随时取消

---

### [GitHub - sindresorhus/np: 更好的 `npm publish` 工具 · GitHub](https://github.com/sindresorhus/np)

**原文标题**: [GitHub - sindresorhus/np: A better `npm publish` · GitHub](https://github.com/sindresorhus/np)

`np` 是一个改进的 `npm publish` 工具，提供交互式发布流程和多项安全校验。

- 🚀 提供交互式 UI，引导用户完成版本发布
- ✅ 确保从正确的发布分支（main/master）发布，工作目录干净且无未拉取变更
- 🔄 重新安装依赖，确保项目与最新依赖树兼容
- 🧪 运行测试，并支持自定义测试脚本（`--test-script`）
- 📦 自动更新 `package.json` 版本号并创建 Git 标签
- 🛡️ 防止意外将预发布版本发布到 `latest` 标签
- 🔙 发布失败时自动回滚到之前状态
- 📤 将提交和标签推送到 GitHub/GitLab
- 🔐 支持双因素认证（2FA）和新仓库启用 2FA
- 📝 发布后自动打开 GitHub Release 草稿（支持自动生成 Release Notes）
- 🔍 提供 `dry-run` 模式，预览执行任务但不实际发布
- 🌐 支持 npm 9+、Yarn、pnpm 8+ 和 Bun
- ⚙️ 支持全局和本地配置（`.np-config.js`、`package.json` 等）
- 🚫 不支持 Monorepo 和 CI 环境（设计为本地交互工具）
- 📌 支持私有包、作用域包、自定义注册表和 gh-pages 发布
- 🧹 发布前清理 `node_modules` 并检查未发布的新文件
- 🔧 提供 `--any-branch`、`--yolo`、`--no-tests` 等灵活选项

---

### [Flox 面向开发者 | 一条命令，零摩擦](https://flox.dev/developers/?utm_source=newsletter&utm_medium=fnf&utm_campaign=2026q1_tofu_awa_influ_devs_floxhub_gl_node&utm_content=landing_page)

**原文标题**: [Flox for Developers | One Command, Zero Friction](https://flox.dev/developers/?utm_source=newsletter&utm_medium=fnf&utm_campaign=2026q1_tofu_awa_influ_devs_floxhub_gl_node&utm_content=landing_page)

概述总结
Flox 是一个面向开发者的多语言开发环境管理工具，旨在消除环境配置的繁琐，让开发者从零开始快速投入生产。它通过简单的命令实现环境初始化、依赖安装、激活和共享，支持个人设置、团队协作、全栈开发、微服务调试和生产部署等场景，并可与 CI/CD 管道集成。

- 🚀 快速上手：通过 `flox init` 和 `flox activate` 命令，几分钟内即可创建并激活包含所需工具（如 vim、git、Node、Python、Postgres）的开发环境，无需手动配置。
- 👥 团队协作：新人激活公司基线环境后，运行 `flox activate` 即可无缝获得所有项目依赖，实现零摩擦入职和代码贡献。
- 🛠️ 全栈开发：一个 Flox 环境可同时支持 React 前端、Python API 和 Postgres，避免版本冲突，轻松切换项目。
- 🔍 微服务调试：使用 Flox 环境在本地复现生产环境（如认证和支付服务），快速定位并修复问题。
- 📦 生产部署：CI/CD 使用与开发相同的 Flox 环境，确保测试和部署一致性，消除“在我机器上能跑”的问题。
- 🔄 发布编排：从开发环境构建包并发布到 FloxHub，生产环境可直接消费并部署到 Kubernetes，实现版本控制和回滚。
- ⚙️ 工作原理：通过 `flox init` 创建环境清单，`flox install` 安装依赖（支持 190,000+ 包），`flox activate` 激活环境，并可通过 Git 或 FloxHub 共享给团队。
- 💡 常见问题：Flox 与 Docker 不同，无需学习 Nix，支持迁移现有项目，包缺失可扩展，兼容 CI/CD 管道，且免费使用。

---

### [Gauntlet AI - 学习生产级AI技能](https://apply.gauntletai.com/register/champions?utm_source=Third%20Party&utm_campaign=Node%20Weekly&utm_medium=referral&utm_content=)

**原文标题**: [Gauntlet AI - Learn Production AI Skills](https://apply.gauntletai.com/register/champions?utm_source=Third%20Party&utm_campaign=Node%20Weekly&utm_medium=referral&utm_content=)

概述摘要：本文探讨了人工智能在医疗诊断中的应用，强调其提升效率与准确性，同时指出数据隐私和伦理挑战。

- 🏥 人工智能通过分析医学影像和病历，辅助医生快速识别疾病，如癌症早期检测。
- 📊 机器学习算法处理海量医疗数据，优化诊断流程，减少人为误差。
- 🔒 数据隐私问题突出，需加强患者信息保护，防止敏感数据泄露。
- ⚖️ 伦理争议包括算法偏见和责任归属，需制定透明监管框架。
- 🌍 全球医疗系统逐步整合AI技术，但发展中国家面临资源和技术差距。

---

### [GitHub - Agent-Field/agentfield: 像API和微服务一样构建、运行和扩展AI代理——从第一天起就具备可观测、可审计和身份感知能力。](https://github.com/Agent-Field/agentfield)

**原文标题**: [GitHub - Agent-Field/agentfield: Build, run and scale AI agents like API and microservices - observable,auditable and identity-aware from day one. · GitHub](https://github.com/Agent-Field/agentfield)

AgentField 是一个开源 AI 后端控制平面，能将 AI 代理像 API 一样构建、部署和扩展，具备可观测性、身份认证和审计追踪能力。

- 🚀 **核心功能**：将 Python、Go 或 TypeScript 编写的代理逻辑自动转为 REST 端点，支持结构化 AI 输出、跨代理调用、异步执行和人类审批。
- 🔒 **身份与治理**：每个代理拥有 W3C 去中心化标识符（DID）和 Ed25519 密钥，执行生成防篡改的可验证凭证，支持基于标签的访问策略。
- 📊 **可观测性**：自动生成工作流 DAG 图、Prometheus 指标、结构化日志和执行时间线，支持健康检查和关联 ID 追踪。
- 🔧 **部署与运维**：支持金丝雀部署、A/B 测试、蓝绿部署，提供 Docker Compose 和 Kubernetes 就绪的部署方案，控制平面为无状态 Go 服务。
- 🧠 **AI 与 LLM 集成**：支持 100+ LLM（通过 LiteLLM），提供结构化输出（Pydantic/Zod）、多模态输入、流式响应和多轮编码代理（Claude Code、Codex 等）。
- 🌐 **代理网格与发现**：支持按标签发现代理、跨代理调用带追踪、自动上下文传播，以及并行执行和自动注册。
- 💾 **分布式内存**：内置键值存储和向量搜索，支持全局、代理、会话和运行四种作用域，无需额外 Redis 依赖。
- 👥 **人类参与**：支持持久化暂停/恢复、审批工作流 UI、可配置超时和自动升级，崩溃安全且状态持久。
- 🛠️ **开发者体验**：提供 CLI 脚手架（`af init`）、本地仪表盘（`af server`）、热重载（`af dev`），以及 Python、Go、TypeScript SDK。
- 📚 **适用场景**：适合构建生产级代理系统（如理赔处理、研究引擎、合规审查），而非简单聊天机器人或早期工作流。

---

### [AgentField — AI 后端](https://agentfield.ai/?utm_source=node&utm_medium=referral&utm_campaign=node-0604&utm_id=node-060424-home-cta&utm_content=home-cta)

**原文标题**: [AgentField — The AI Backend](https://agentfield.ai/?utm_source=node&utm_medium=referral&utm_campaign=node-0604&utm_id=node-060424-home-cta&utm_content=home-cta)

概述摘要：本文探讨了人工智能在医疗领域的应用现状与未来潜力，重点分析了诊断辅助、药物研发和个性化治疗等关键方向。

- 🩺 人工智能通过分析医学影像数据，显著提高了疾病诊断的准确性和效率，尤其在癌症早期筛查中表现突出。
- 💊 在药物研发方面，AI加速了候选化合物的筛选过程，缩短了新药上市周期，降低了研发成本。
- 🧬 基于患者基因组和健康数据的个性化治疗方案，借助AI算法实现了更精准的疾病管理。
- ⚠️ 数据隐私、算法偏见以及监管标准不统一，仍是AI医疗落地的主要挑战。
- 🌐 未来，AI有望与可穿戴设备结合，实现实时健康监测和远程医疗，进一步改善医疗可及性。

---

### [发布 v1.59.0 · microsoft/playwright · GitHub](https://github.com/microsoft/playwright/releases/tag/v1.59.0)

**原文标题**: [Release v1.59.0 · microsoft/playwright · GitHub](https://github.com/microsoft/playwright/releases/tag/v1.59.0)

Playwright v1.59.0 版本发布，带来了多项新功能和改进。

- 🎬 **Screencast 录制**：新增 `page.screencast` API，支持视频录制、动作注释、视觉叠加、实时帧捕获和智能体视频凭证。
- 🔗 **浏览器互操作性**：新增 `browser.bind()` API，允许将已启动的浏览器绑定，供 `playwright-cli`、`@playwright/mcp` 等客户端连接。
- 📊 **可观测性**：`playwright-cli show` 命令可打开仪表盘，列出所有绑定的浏览器及其状态，并支持交互操作。
- 🐛 **CLI 调试器**：智能体可通过 `npx playwright test --debug=cli` 附加并调试测试，适用于自动化修复工作流。
- 📋 **CLI 追踪分析**：智能体可运行 `npx playwright trace` 探索 Playwright 追踪，理解失败或不稳定的测试。
- ♻️ **`await using` 语法**：许多 API 返回异步可释放对象，支持自动清理。
- 🔍 **快照与定位器**：新增 `page.ariaSnapshot()`、`locator.normalize()` 和 `page.pickLocator()` 等方法。
- 🛠️ **其他改进**：UI 模式支持仅显示受源更改影响的测试；HTML 报告器显示同一工作者的运行列表；新增 `retain-on-failure-and-retries` 追踪模式。
- ⚠️ **已知问题**：`navigator.platform` 模拟可能导致 Ctrl 或 Meta 分发错误，需设置环境变量 `PLAYWRIGHT_NO_UA_PLATFORM='1'`。
- ⚠️ **重大变更**：移除了 macOS 14 对 WebKit 的支持；移除了 `@playwright/experimental-ct-svelte` 包。

---

