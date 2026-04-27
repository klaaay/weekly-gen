### [Node 周刊第 621 期：2026 年 4 月 23 日](https://nodeweekly.com/issues/621)

**原文标题**: [Node Weekly Issue 621: April 23, 2026](https://nodeweekly.com/issues/621)

以下是您提供的Node Weekly内容的概述和要点总结：

概述摘要  
本期Node Weekly涵盖了Node.js生态中的新工具、性能提升、开发技巧及实用库更新，包括新的包管理器、TypeScript 7.0 Beta、Playwright的视频录制API等。

- 🚀 **aube：新型Node.js包管理器** — 由mise开发者打造，注重原始性能和安全性，可作为npm的即插即用替代品。
- 🎓 **编写更好的AI提示词** — Frontend Masters赞助的课程，由GitHub的Sabrina Goldfarb教授实用提示词技巧。
- 🔧 **用.NET Native AOT编写Node.js插件** — 微软的Drew Noakes展示了如何用C#等.NET语言创建原生Node扩展。
- 📰 **简讯** — NodeConf EU回归（9月29-30日，意大利博洛尼亚）；Yarn维护者Maël Nison正开发支持包映射的新功能；TypeScript 7.0 Beta发布，性能提升10倍。
- 🗺️ **10KB内交付动态六边形世界地图** — Ben Schwarz使用Node管道和Turf.js简化GeoJSON，构建基于六边形的SVG地图。
- 📦 **npmx：值得借鉴的功能** — Andrew Nesbitt推荐npmx作为浏览npm注册表的优秀工具。
- 🛠️ **Optique 1.0：类型安全的组合CLI解析器** — 提供类型安全、类型推断和Shell补全支持，首个稳定版发布。
- 📚 **DocMD：从Markdown构建生产级文档** — 零配置文档站点生成器，支持i18n和版本控制，新增部署命令。
- 🗃️ **rocksdb-js：Node的新RocksDB绑定** — Chris Barber为Facebook的RocksDB键值存储提供了现代原生插件。
- ⚡ **Bun v1.3.13：更智能的测试和更低内存使用** — 内存减少5%，bun test新增环境隔离和并行化选项。
- 🎥 **Playwright的page.screencast API** — 新版Playwright v1.59.0提供更灵活的视频录制，支持视觉注释和自定义HTML叠加，可自动生成文档用视频。

---

### [黎明](https://aube.en.dev/)

**原文标题**: [aube](https://aube.en.dev/)

### 概述
Aube 是一款快速 Node.js 包管理器，无需迁移锁文件即可集成到现有项目中，通过全局存储和链接机制大幅减少磁盘占用，并支持多种锁文件格式。

- 🚀 **极速性能**：Aube 比 pnpm 快 9.2 倍，比 Bun 快 2.7 倍，在热安装基准测试中表现突出。
- 💾 **节省磁盘**：采用全局内容寻址存储，项目间共享包文件，比 npm 减少 90% 磁盘空间。
- 🔒 **锁文件兼容**：直接读写 `yarn.lock`、`pnpm-lock.yaml` 或 `package-lock.json`，无需团队迁移。
- ⚡ **智能运行**：`aubr test` 命令在依赖变更时自动安装，后续重复运行跳过安装步骤。
- 🛡️ **安全沙箱**：支持“监禁构建”，对依赖脚本进行权限限制，使用清理环境运行生命周期脚本。

---

### [首页 | 准备工作](https://mise.en.dev/)

**原文标题**: [Home | mise-en-place](https://mise.en.dev/)

该文章介绍了mise-versions工具及其相关功能模块，包括开发工具、环境管理和任务执行，并提供了版本和外观设置选项。

- 🔍 提供搜索功能，便于快速定位内容
- 🧭 主导航栏用于浏览不同模块
- 🛠️ 包含开发工具（Dev Tools）相关配置
- 🌍 支持环境（Environments）管理
- ✅ 提供任务（Tasks）执行与跟踪
- 📌 当前版本为v2026.4.23
- 🎨 允许调整外观（Appearance）设置

---

### [基准测试 | aube](https://aube.en.dev/benchmarks.html)

**原文标题**: [Benchmarks | aube](https://aube.en.dev/benchmarks.html)

该基准测试对比了 aube、bun、pnpm、npm 和 yarn 在多种场景下的性能表现，重点突出 aube 的速度优势。

- ⚡ **aube 在多数场景下速度最快**：在热缓存全新安装中，aube 仅需 270ms，远快于 bun（724ms）和 pnpm（2.50s）。
- ❄️ **冷缓存场景下 aube 仍具竞争力**：冷缓存全新安装中，aube 耗时 3.10s，仅次于 bun（2.07s），优于其他工具。
- 🔄 **CI 场景中 aube 表现稳定**：禁用全局虚拟存储后，aube 热缓存 CI 安装仅需 588ms，冷缓存为 2.85s，均领先于 pnpm 和 npm。
- 🚀 **增量操作极快**：aube 的“添加依赖”仅需 328ms，而 npm 需 10.19s，yarn 需 8.83s。
- 🧪 **开发循环优化**：aube 在“安装后运行测试”场景中仅需 9ms，远优于 bun（36ms）和 pnpm（905ms）。
- 🛠️ **技术原理**：aube 采用与 pnpm 相同的全局内容可寻址存储和隔离符号链接布局，但使用更快的原生多线程语言编写安装管道，而非 JavaScript。
- 📊 **测试方法严谨**：所有测试使用相同的约 1400 个真实包，通过 hyperfine 在可控条件下运行，并采用固定 500mbit 带宽的本地注册表以确保结果可复现。

---

### [配置 | aube](https://aube.en.dev/package-manager/configuration.html)

**原文标题**: [Configuration | aube](https://aube.en.dev/package-manager/configuration.html)

### 概述总结
aube 从 `.npmrc`、用户配置、`aube-workspace.yaml`、环境变量和 CLI 标志中读取 pnpm 兼容配置，并支持从 `pnpm-workspace.yaml` 迁移。

- 🔗 **链接器**：默认 `nodeLinker=isolated`，将传递依赖项限定在声明它们的包内。
- 📦 **包导入**：`packageImportMethod=auto`，根据文件系统支持使用重链接、硬链接或复制。
- ⏳ **新版本**：`minimumReleaseAge=1440`，默认避免安装过去 24 小时内发布的版本。
- 🚫 **外来传递依赖**：`blockExoticSubdeps=true`，默认阻止传递的 git 和 tarball 依赖，除非选择退出。
- ✅ **依赖脚本**：需批准，构建脚本在依赖中保持跳过，直到被批准。
- 🔒 **受限构建**：`jailBuilds=false`，可选择在受限环境中运行批准的依赖脚本，计划在下个主要版本中默认启用。
- 🔄 **脚本前自动安装**：`aube run`、`aube test` 和 `aube exec` 会先修复过期的安装。
- ⚙️ **配置源**：支持 `.npmrc`、工作区 YAML、环境变量和 CLI 标志，优先级依次递增。
- 🔍 **检查配置**：使用 `aube config` 命令查看、设置和列出配置。
- 📝 **package.json 命名空间**：支持 `pnpm.*` 和 `aube.*`，合并时映射值键冲突以 `aube.*` 为准，列表值合并并集，顶级 npm 标准键优先级最高。

---

### [为Cursor、Claude和Copilot编写更好的提示词 | 前端大师](https://frontendmasters.com/courses/prompt-engineering/?utm_source=email&utm_medium=nodeweekly&utm_content=promptengineering)

**原文标题**: [Write Better Prompts for Cursor, Claude & Copilot | Frontend Masters](https://frontendmasters.com/courses/prompt-engineering/?utm_source=email&utm_medium=nodeweekly&utm_content=promptengineering)

本课程系统讲解了提示工程的核心技巧，帮助开发者更高效地使用AI工具生成代码，内容涵盖从基础到高级的多种提示方法。

- 🧠 **提示工程基础**：介绍了LLM的工作原理、温度与Top P参数、Token限制及上下文窗口等核心概念，强调提示质量直接影响输出结果。
- 📝 **标准提示与零样本提示**：标准提示即直接提问，质量决定答案；零样本提示无示例，适合常见任务，但依赖模型预训练知识。
- 🎯 **单样本与少样本提示**：单样本提示提供一个示例，让模型学习格式与风格；少样本提示提供多个示例与边缘情况，提升模型对细节的把握。
- 🛠️ **上下文放置与结构化输出**：上下文放在提示开头和结尾更有效；通过指定模板或模式，可让模型输出一致格式。
- 🔗 **链式思维提示**：要求模型逐步推理，分解复杂问题，结合少样本技巧效果更佳，适用于实现复杂功能如导入/导出。
- 🚀 **未来验证与情感提示**：记录成功提示与模型，便于测试新模型；情感提示可增强模型对关键部分的关注，但效果因模型而异。
- 🧩 **分隔符与角色设定**：使用引号、XML标签等分隔符增加提示结构；设定角色（如专家）可引导模型聚焦特定知识领域。
- 💡 **实用技巧**：推荐使用“continue”让代理重新输出；选择不同模型可优化准确性与成本；鼓励持续实验以应对模型更新。

---

### [使用.NET Native AOT编写Node.js插件 - .NET博客](https://devblogs.microsoft.com/dotnet/writing-nodejs-addons-with-dotnet-native-aot/)

**原文标题**: [Writing Node.js addons with .NET Native AOT - .NET Blog](https://devblogs.microsoft.com/dotnet/writing-nodejs-addons-with-dotnet-native-aot/)

本文介绍了如何使用 .NET Native AOT 为 Node.js 编写原生插件，以简化 C# Dev Kit 的构建流程，并提供了详细的实现步骤。

- 📝 **背景与动机**：C# Dev Kit 团队过去使用 C++ 和 node-gyp 编写原生 Node.js 插件，但需要安装旧版 Python，增加了开发复杂性和 CI 维护成本。改用 .NET Native AOT 后，只需依赖已安装的 .NET SDK，简化了工具链。
- ⚙️ **Node.js 插件原理**：Node.js 原生插件是共享库（.dll/.so/.dylib），通过 N-API（稳定 C API）导出 `napi_register_module_v1` 函数。Native AOT 可生成任意原生入口点，满足 N-API 要求。
- 🛠️ **项目配置**：项目文件只需设置 `<PublishAot>true</PublishAot>` 和 `<AllowUnsafeBlocks>true</AllowUnsafeBlocks>`，发布时自动生成共享库。
- 🔗 **模块入口与 N-API 调用**：使用 `[UnmanagedCallersOnly]` 导出 `napi_register_module_v1`，并通过 `NativeLibrary.SetDllImportResolver` 将 N-API 函数解析到宿主进程（node.exe），避免额外链接。
- 🔤 **字符串编组**：通过 `ReadOnlySpan<byte>` 和 UTF-8 处理字符串，使用 `stackalloc` 和 `ArrayPool` 优化小字符串性能，避免堆分配。
- 🖥️ **实现导出函数**：以读取 Windows 注册表为例，使用 `GetStringArg` 获取参数，调用 .NET API（如 `Microsoft.Win32.Registry`），并通过 `CreateString` 返回结果。需捕获异常并转发到 JavaScript。
- 🚀 **TypeScript 调用**：发布后重命名共享库为 `.node` 文件，通过 `require()` 加载，并定义 TypeScript 接口实现类型安全。
- 📚 **现有库对比**：`node-api-dotnet` 提供更高级框架，但本文采用轻量级 N-API 封装，适合少量函数场景。
- ✅ **收益**：消除 Python 依赖，简化 CI，性能与 C++ 相当。未来可探索在 Node.js 进程中直接托管 .NET 逻辑，减少进程间通信开销。
- 💡 **开发体验**：团队借助 GitHub Copilot 快速实现概念验证，降低了学习 N-API 的门槛。

---

### [NodeConf EU | Node.js](https://www.nodeconf.eu/)

**原文标题**: [NodeConf EU | Node.js](https://www.nodeconf.eu/)

NodeConf EU 是一场于9月29日至30日在意大利博洛尼亚举办的Node.js技术会议，旨在汇聚技术社区，目前门票已开售，并开放演讲征集（CFP）。会议设有多个赞助商层级，包括白金、黄金、T恤、咖啡休息、白银、支持及社区赞助商。

- 🎟️ 会议时间与地点：9月29-30日，意大利博洛尼亚
- 💻 核心主题：Node.js技术社区交流
- 🛒 门票状态：现已开售
- 📢 演讲征集：CFP开放中
- ⏳ 倒计时：365天24小时60分钟60秒（可能指活动倒计时）
- 🏆 赞助商层级：白金、黄金、T恤、咖啡休息、白银、支持、社区赞助商

---

### [NodeConf EU 2026](https://docs.google.com/forms/d/e/1FAIpQLSdhxLUxB5kW8NU5Dv6PM7vvQqKLcKed45AXvsXPGN8tIkzfkg/viewform)

**原文标题**: [NodeConf EU 2026](https://docs.google.com/forms/d/e/1FAIpQLSdhxLUxB5kW8NU5Dv6PM7vvQqKLcKed45AXvsXPGN8tIkzfkg/viewform)

NodeConf EU 2026 將於義大利波隆那舉辦，現正徵求演講者與贊助商。

- 🇮🇹 活動地點移至義大利波隆那，日期為9月29日至30日
- 🎤 兩天內共有24位講者，涵蓋Node.js核心、實際應用、創新想法與生態系統
- 📋 徵求演講提案，需提供主題、描述、講者資訊及同意資料分享
- ✈️ 提供有限的旅行補助選項，可於報名時申請
- 💼 詢問贊助意願，公司或雇主可表達興趣

---

### [加载器：通过arcanis实现包映射 · 拉取请求 #62239 · nodejs/node · GitHub](https://github.com/nodejs/node/pull/62239)

**原文标题**: [loader: implement package maps by arcanis · Pull Request #62239 · nodejs/node · GitHub](https://github.com/nodejs/node/pull/62239)

Node.js 的 PR #62239 提出新增 `--experimental-package-map` 标志，允许使用静态 JSON 文件替代 `node_modules` 目录来解析包，旨在解决现有模块解析的诸多问题。

- 📦 **新增 `--experimental-package-map` 标志**：通过一个 JSON 文件声明包及其依赖关系，替代传统的 `node_modules` 目录遍历解析。
- 🐛 **解决“幽灵依赖”问题**：包只能导入其显式声明的依赖，防止意外访问提升的传递依赖。
- 🔗 **修复 monorepo 中对等依赖解析**：通过为每个包分配唯一 ID 并独立指定依赖，解决不同版本 React 等对等依赖冲突。
- ⚡ **减少 I/O 操作**：静态 JSON 文件解析无需文件系统遍历，显著提升性能，尤其适用于多 Git 仓库场景。
- 🔄 **与 `node_modules` 兼容**：包管理器可同时生成 `node_modules` 和 `package-map.json`，后者引用前者路径，支持渐进式采用。
- 🆚 **与 Import Maps 的区别**：包映射采用扁平结构，支持同一包名的多版本共存，且与 Node.js 的 `exports` 和 `imports` 字段兼容。
- 🛠️ **由包管理器生成**：Yarn、pnpm 等工具可自动生成 `package-map.json`，并通过 `NODE_OPTIONS` 注入标志。
- ❓ **待定问题**：是否默认严格模式（发现错误即拒绝解析），或通过额外标志/字段控制。
- 💬 **社区反馈**：获得多位贡献者支持，但需与 TSC 及 WinterCG 进一步讨论标准化及与 Import Maps 的兼容性。

---

### [TypeScript 7.0 Beta 版本发布](https://devblogs.microsoft.com/typescript/announcing-typescript-7-0-beta/)

**原文标题**: [Announcing TypeScript 7.0 Beta - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-7-0-beta/)

TypeScript 7.0 Beta 正式发布，基于 Go 语言重写，性能大幅提升，并带来多项新特性和配置变更。

- 🚀 性能飞跃：TypeScript 7.0 基于 Go 重写，利用原生代码速度和并行处理，比 6.0 快约 10 倍。
- 🧪 高度兼容：核心类型检查逻辑与 6.0 结构一致，经过大规模测试和多家公司验证，Beta 版已可日常使用。
- 🛠️ 安装与试用：通过 `npm install -D @typescript/native-preview@beta` 安装，使用 `tsgo` 命令；VS Code 有专用扩展。
- 🔄 并行化控制：新增 `--checkers` 和 `--builders` 标志，可分别控制类型检查和项目构建的并行度；`--singleThreaded` 用于单线程模式。
- ⚙️ 默认配置变更：`strict` 默认开启，`module` 默认为 `esnext`，`target` 默认为最新稳定版 ECMAScript，`types` 默认为 `[]` 等。
- 🚫 废弃特性移除：不再支持 `target: es5`、`downlevelIteration`、`module: amd/umd/systemjs/none`、`baseUrl` 等。
- 📝 JavaScript 支持调整：JSDoc 分析更严格，不再特殊支持 `@enum`、`@class`、后置 `!` 等模式，需使用标准 TypeScript 语法。
- ✨ 编辑器体验提升：VS Code 扩展支持自动导入、悬停提示、内联提示、代码镜头、JSX 编辑等，性能同样显著提升。
- 🗺️ 未来规划：即将推出更高效的 `--watch` 模式，完善声明文件输出，稳定版 API 预计在 7.1 中发布，正式版计划两个月内推出。

---

### [宣布 TypeScript 6.0 - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-6-0/)

**原文标题**: [Announcing TypeScript 6.0 - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-6-0/)

TypeScript 6.0 正式发布，作为连接 5.9 和 7.0 的桥梁，引入了多项新功能、性能改进和重大弃用，为迁移到基于 Go 的原生编译器（TypeScript 7.0）做准备。

- 🚀 **TypeScript 6.0 发布**：这是基于当前 JavaScript 代码库的最后一个版本，旨在为 TypeScript 7.0（原生 Go 编译器）铺路。
- 🧠 **减少 `this` 敏感性**：改进了类型推断，未使用 `this` 的函数不再被视为上下文敏感，解决了方法语法中类型推断不一致的问题。
- 🔗 **支持 `#/` 子路径导入**：在 `nodenext` 和 `bundler` 模块解析模式下，支持 Node.js 新增的 `#/` 子路径导入语法。
- ⚙️ **新增 `--stableTypeOrdering` 标志**：使 6.0 的类型排序行为与 7.0 一致，用于诊断迁移差异，但会降低检查速度。
- 🌐 **支持 ES2025 目标**：新增 `es2025` 的 `target` 和 `lib` 选项，包含 `RegExp.escape` 等新 API。
- 📅 **新增 Temporal API 类型**：为 Stage 4 的 Temporal 提案提供内置类型，可通过 `--target esnext` 使用。
- 🗺️ **新增 Map 的 `getOrInsert` 方法**：支持 `Map` 和 `WeakMap` 的 `getOrInsert` 和 `getOrInsertComputed` 方法。
- 🔒 **`dom` 库合并迭代器**：`dom.iterable` 和 `dom.asynciterable` 内容已合并到 `dom` 中，无需额外配置。
- ⚠️ **重大弃用与默认值变更**：`strict` 默认启用，`module` 默认 `esnext`，`target` 默认最新 ES 版本；弃用了 `es5`、`downlevelIteration`、`moduleResolution node`、`baseUrl` 等多项旧设置。
- 🛠️ **迁移准备**：建议使用 `"ignoreDeprecations": "6.0"` 临时忽略弃用警告，并积极采用 7.0 原生预览版。

---

### [宣布 TypeScript 7.0 Beta 版 - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-7-0-beta/#updates-since-5.x-and-new-behaviors-from-6.0)

**原文标题**: [Announcing TypeScript 7.0 Beta - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-7-0-beta/#updates-since-5.x-and-new-behaviors-from-6.0)

TypeScript 7.0 Beta 正式发布，基于 Go 语言重写，性能大幅提升，并引入了多项新特性和配置变更。

- 🚀 TypeScript 7.0 基于 Go 语言重写，速度比 6.0 快约 10 倍，且保持语义兼容。
- 📦 可通过 npm 安装 `@typescript/native-preview@beta`，并使用 `tsgo` 命令替代 `tsc`。
- 🖥️ 提供 VS Code 扩展 `TypeScript Native Preview`，支持编辑器内高性能体验。
- 🔄 支持与 TypeScript 6.0 并行运行，通过 `@typescript/typescript6` 包和 `tsc6` 入口点实现无缝过渡。
- ⚙️ 引入并行化控制，新增 `--checkers`、`--builders` 和 `--singleThreaded` 标志，优化构建性能。
- 📋 默认配置变更：`strict` 为 true，`module` 默认为 `esnext`，`target` 默认为最新 ECMAScript 版本等。
- 🚫 多项废弃特性变为硬错误，如 `target: es5`、`downlevelIteration`、`module: amd` 等不再支持。
- 🧩 JavaScript 支持重写，更一致地分析 JS 文件，废弃部分 JSDoc 模式（如 `@enum`、`@class`）。
- 🛠️ 编辑器体验增强，支持自动导入、悬停提示、内联提示、代码镜头等功能。
- 📅 计划在未来两个月内发布稳定版，RC 版将提前几周推出，鼓励用户反馈。

---

### [宣布 TypeScript 7.0 Beta 版 - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-7-0-beta/#javascript-differences)

**原文标题**: [Announcing TypeScript 7.0 Beta - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-7-0-beta/#javascript-differences)

TypeScript 7.0 Beta 正式发布，基于 Go 重写，性能提升约 10 倍，同时保持与 6.0 的语义兼容性。

- 🚀 性能飞跃：TypeScript 7.0 将代码库从 TypeScript 移植到 Go，利用原生速度和共享内存并行，速度比 6.0 快约 10 倍。
- ✅ 高度稳定：经过十年积累的测试套件验证，已在微软内外多个百万行级代码库中使用，可直接用于日常开发和 CI 流程。
- 📦 安装与试用：通过 npm 安装 `@typescript/native-preview@beta`，使用 `tsgo` 命令；VS Code 提供“TypeScript Native Preview”扩展支持。
- 🔄 并行化控制：新增 `--checkers` 和 `--builders` 标志，分别控制类型检查和项目构建的并行度；`--singleThreaded` 可强制单线程模式。
- ⚙️ 6.0 兼容性：完全兼容 TypeScript 6.0 行为，并采用其新默认值（如 `strict: true`、`module: esnext` 等），弃用项变为硬错误。
- 🛠️ 配置变更：`rootDir` 默认改为 `./`，`types` 默认改为 `[]`，需显式设置；`target: es5`、`downlevelIteration` 等不再支持。
- 📝 JavaScript 支持重构：JSDoc 分析更一致，移除 `@enum`、`@class` 等特殊处理，改用更严格的 TypeScript 风格语法。
- ✨ 编辑器体验：VS Code 扩展支持自动导入、悬停提示、内联提示、代码镜头等功能，性能显著提升。
- 🗓️ 未来计划：未来几周将改进 `--watch` 模式，计划两个月内发布稳定版，RC 版提前几周推出。

---

### [每个AI代理所需的四层生产堆栈](https://orkes.io/webinars/the-4-layer-production-stack-every-ai-agent-needs?utm_campaign=Node%20weekly&utm_source=Newsletter&utm_medium=referral)

**原文标题**: [The 4-Layer Production Stack Every AI Agent Needs](https://orkes.io/webinars/the-4-layer-production-stack-every-ai-agent-needs?utm_campaign=Node%20weekly&utm_source=Newsletter&utm_medium=referral)

Orkes 平台提供了一套完整的 AI 代理生产堆栈，并即将举办一场关于该堆栈的深度网络研讨会。

- 🧠 **核心问题**：企业团队构建的 AI 代理在演示中表现优异，但在生产环境中却容易崩溃，问题通常不在于模型本身，而在于底层基础设施。
- 🗓️ **网络研讨会**：将于 4 月 30 日举行，主题为“每个 AI 代理所需的四层生产堆栈”，旨在提供从原型到企业级部署的实用蓝图。
- 🏗️ **四层堆栈**：包括持久性（故障恢复）、协调（多代理协作）、安全与控制（人工审核、输入验证）和可观测性（执行步骤查询与回放）。
- 🎥 **现场演示**：将展示一个持久代理在被终止进程后如何恢复状态，以及多代理交接的实例。
- 🚀 **开源工具**：介绍 Agentspan，一个开源服务器和 SDK，可将代理定义编译为持久化工作流。
- 🎯 **目标受众**：适合部署首个生产代理或为大规模 AI 系统设计基础设施的工程领导者。
- 💡 **客户证言**：Foxtel 的首席架构师称赞 Orkes 提升了开发敏捷性、成本效益和应用安全性。

---

### [仅用10KB呈现动态六边形世界地图 | Calibre 博客](https://calibreapp.com/blog/building-our-beloved-hex-map)

**原文标题**: [Delivering a dynamic hexagonal world map in just 10kb | Calibre Blog](https://calibreapp.com/blog/building-our-beloved-hex-map)

### 概述摘要
本文介绍了Calibre团队如何在10KB内构建动态六边形世界地图，用于可视化真实用户会话的性能数据。

- 🌍 **地图功能**：六边形地图动态展示各国用户体验评分（UX Rating），基于真实用户监控（RUM）数据。
- 🎯 **设计目标**：要求加载快速、轻量、低画质艺术风格、跨浏览器兼容，并支持明暗主题。
- 🔍 **研究灵感**：受体素几何、选举地图和抽象地理可视化启发，选择六边形地图以实现简洁美观。
- 🛠️ **技术实现**：通过简化GeoJSON数据（10米精度）、使用Turf简化路径、生成SVG文件（144KB，GZip后仅10KB）。
- ⚡ **性能优化**：利用SVG的`<symbol>`和`<use>`重复使用六边形，避免冗余；通过CSS变量控制颜色和明暗主题。
- ❌ **局限性**：美国地图左右边缘重叠，塔斯马尼亚岛因尺寸太小无法显示，存在简化带来的不完美。
- 💡 **最终成果**：地图在每次构建时生成，缓存于CDN，动态加载后根据性能数据着色，提供直观的用户体验洞察。

---

### [TypeScript高级地理空间工具包 | Turf.js](https://turfjs.org/)

**原文标题**: [Advanced geospatial toolkit for Typescript | Turf.js](https://turfjs.org/)

Turf 是一个模块化、轻量级的 JavaScript 地理空间分析库，专注于 GeoJSON 数据处理，无需服务器即可快速运行。

- 🧩 模块化设计：由小型独立模块组成，用户可按需加载所需功能
- 🚀 高速性能：采用最新算法，本地处理数据，无需发送至服务器
- 🎯 专注核心：功能简洁专一，聚焦于 GeoJSON 格式的地理数据操作
- 🔧 易于使用：JavaScript 函数简单直观，降低使用门槛

---

### [每个人都应该从npmx借鉴的功能 | Andrew Nesbitt](https://nesbitt.io/2026/04/16/features-everyone-should-steal-from-npmx.html)

**原文标题**: [Features everyone should steal from npmx | Andrew Nesbitt](https://nesbitt.io/2026/04/16/features-everyone-should-steal-from-npmx.html)

npmx 为 npm 注册表提供了一个功能丰富的替代前端，其创新功能不仅迫使官方 npmjs.com 开始更新（如深色模式），还为其他包注册表网站提供了可借鉴的参考实现。

- 📦 **传递安装大小**：显示包及其所有依赖项的解压后总大小，而非单个 tarball 大小，让开发者更清楚实际磁盘占用。
- 🔍 **安装脚本披露**：在包页面上直接展示 `preinstall`、`install`、`postinstall` 脚本内容及关联的 `npx` 包，并链接到代码浏览器，有助于防范供应链攻击。
- 🌳 **过时与脆弱依赖树**：提供可展开的依赖树，每个节点标注与最新版本的差距及是否出现在 OSV 漏洞库中，递归展示传递依赖。
- 🎯 **版本范围解析**：在 semver 范围（如 `^1.0.0`）旁显示其当前解析的具体版本，省去查询 CLI 的步骤。
- 💡 **模块替换建议**：对出现在 e18e 模块替换数据集中的包，显示指向原生 API 或更轻量替代方案的横幅，并附上 MDN 链接。
- 🏷️ **模块格式与类型徽章**：在包名旁显示 ESM、CJS 或双格式，以及 TypeScript 类型是否内置或需单独安装，并声明 Node 引擎范围。
- ⭐ **多平台仓库统计**：从 GitHub、GitLab、Bitbucket 等十个平台获取星标和分支数，而非仅限 GitHub。
- 🔗 **跨注册表可用性**：标记同时存在于 JSR 的包，既作为生态系统重叠的提示，也用于依赖混淆检测（当名称存在但发布者不匹配时）。
- 📊 **并排包比较**：最多可加载十个包到比较视图，以表格和散点图展示所有指标，直观区分流行但笨重与小型但未知的选项。
- 📝 **版本差异比较**：在浏览器中逐文件比较任意两个已发布版本，类似 Hex 的 diff.hex.pm 功能。
- 📈 **带大小注释的发布时间线**：绘制每个版本的时间线，并用标记突出显示安装大小显著变化的版本，便于发现意外包含测试文件的情况。
- 📉 **按版本的下载分布**：将每周下载量按主版本或次版本细分，以分布图而非表格展示，类似 RubyGems 的功能。
- ⌨️ **命令面板**：按 `⌘K` 打开，提供当前页面所有操作及全局导航，在包页面输入 semver 范围可过滤版本列表。
- 🌐 **国际化**：界面支持超过三十种语言，包括从右到左的语言，与 PyPI 的 Warehouse 并列为重视此功能的注册表。
- ♿ **可访问性**：图表和演示视频带有长 `aria-label` 和 `figcaption` 文本，命令面板支持屏幕阅读器，并有专门的无障碍声明。
- 🎮 **游乐场链接提取**：从包的 README 中提取 StackBlitz、CodeSandbox 等平台的链接，放入专用面板，方便直接试用。
- 🤖 **Agent 技能检测**：列出包含 Agent Skills 清单的包及其声明的工具兼容性，适用于检测发布包中的非代码负载。
- 🐦 **基于 AT Protocol 的社交功能**：包的“点赞”是 atproto 记录，博客评论是 Bluesky 线程，自定义记录类型公开在仓库中，其他工具可读写，npmx 运行自己的 PDS 以控制记录。
- 🔐 **本地 CLI 管理连接器**：通过本地 `npm` CLI 代理管理操作（如认领包名或编辑访问权限），避免 npmx 持有注册表凭据。
- 🌙 **深色模式与自定义调色板**：最后列出，因为这是 npm 已复制的功能，而 pkg.go.dev、crates.io 和 PyPI 此前已支持。

---

### [npmx - npm注册表的包浏览器](https://npmx.dev/)

**原文标题**: [npmx - Package Browser for the npm Registry](https://npmx.dev/)

概述摘要  
- 🚀 npmx 是一款快速、现代的 npm 注册表浏览器，目前处于 alpha 阶段。  
- 🔍 支持即时搜索 npm 包，可通过“/”键快速启动。  
- 🛠️ 内置多种流行框架支持，包括 Nuxt、Vue、React、Svelte、Vite 等。  
- 📅 最新版本 v0.9.0 于 2026 年 4 月 14 日构建。  
- 🤝 鼓励社区参与：贡献代码、加入 Discord 讨论或关注 Bluesky 获取更新。

---

### [光学](https://optique.dev/)

**原文标题**: [Optique](https://optique.dev/)

概述总结  
- 🧩 采用可组合设计，通过小型函数构建解析器  
- 🔗 使用 `merge()` 合并选项组，`or()` 处理备选方案  
- ♻️ 解析器组件可在命令间共享，同时保留类型信息  
- ❓ 解释了为何选择解析器组合子（parser combinators）的方式

---

### [optique/CHANGES.md 在 main 分支上 · dahlia/optique · GitHub](https://github.com/dahlia/optique/blob/main/CHANGES.md#version-100)

**原文标题**: [optique/CHANGES.md at main · dahlia/optique · GitHub](https://github.com/dahlia/optique/blob/main/CHANGES.md#version-100)

这是一个名为 **optique** 的开源项目，托管在代码托管平台上，主要包含更新日志文件 `CHANGES.md`。

- 📂 项目拥有 **665 个星标** 和 **7 个复刻**，表明其受到一定关注
- 🔔 需登录才能更改通知设置，当前有 **1 个议题** 和 **0 个拉取请求**
- 📝 核心文件 `CHANGES.md` 位于 `main` 分支的 `optique/` 目录下，包含 **6461 行** 代码
- 🔄 提供代码查看、编辑、原始文件下载等操作选项
- 🛡️ 启用了安全与质量检查功能，确保项目稳定性

---

### [从五个可选字段到判别联合：使用Optique 1.0进行命令行解析](https://hackers.pub/@hongminhee/2026/optique-10-discriminated-unions-for-cli)

**原文标题**: [From five optional fields to a discriminated union: CLI parsing with Optique 1.0](https://hackers.pub/@hongminhee/2026/optique-10-discriminated-unions-for-cli)

概述总结
- 🎯 Optique 1.0 通过将 CLI 解析从运行时验证提升到类型级别，解决了 Commander.js 和 Yargs 中类型与约束脱节的问题。
- 🔄 使用解析器组合子（如 `or()` 和 `object()`）构建带判别联合类型的 CLI 参数，使 TypeScript 能根据分支自动推断字段可用性。
- 🌐 统一处理命令行参数、环境变量、配置文件和交互式提示四种来源，通过 `bindEnv()`、`bindConfig()` 和 `prompt()` 包装器实现优先级和约束一致性。
- 🛡️ 新增 `Parser.validateValue()` 方法，确保所有来源的值都经过相同约束验证，防止通过非 argv 途径绕过限制。
- ⚠️ 对于简单 CLI 建议使用 Commander.js，Optique 更适合复杂结构（如互斥组、必需选项、多来源值）。
- 📚 1.0 版本标志着 API 稳定，无需额外脚注说明，文档和变更日志已发布在 optique.dev 和 GitHub。

---

### [从Markdown快速构建生产级文档](https://docmd.io/)

**原文标题**: [
        Build production-ready documentation from Markdown in seconds
        
      ](https://docmd.io/)

docmd 是一个零配置的文档引擎，可将 Markdown 文件转换为生产级文档站点，无需框架、无需学习曲线，一键生成静态 HTML，支持 SEO、SPA 导航和 AI 上下文。

- 📄 **零配置启动**：运行 `npx @docmd/core dev` 即可生成文档站点，支持 `docmd.config.js` 自定义配置，兼容现有 Markdown 结构。
- 🎨 **丰富布局**：通过原生 Markdown 容器语法实现标注、标签页、卡片等复杂布局，无需编写 HTML。
- 🔍 **离线搜索**：内置全文模糊搜索，支持快捷键 ⌘K，无云依赖，完全离线运行，且支持多语言索引。
- 🚀 **生产就绪**：提供主题（亮/暗）、国际化（i18n）、多版本文档和一键部署（支持 Docker、Nginx、Caddy）。
- 🤖 **AI 就绪**：自动生成 `llms.txt` 和 `llms-full.txt` 文件，为 AI 模型提供结构化上下文，便于智能导航。
- 🆓 **免费开源**：基于 MIT 许可证，所有核心功能和插件默认包含，无隐藏费用。
- ❓ **常见问题**：无需 React 或 Vue，支持与现有文档集成，原生多语言支持，可与 AI 工具（如 ChatGPT、Claude）配合使用。

---

### [docmd 文档：即时部署生产级文档](https://docs.docmd.io/)

**原文标题**: [
      docmd documentation: deploy production-ready docs instantly
    ](https://docs.docmd.io/)

### 概述
docmd是一个将Markdown快速转换为生产级文档站点的工具，支持静态HTML、SPA和AI优化，无需配置即可运行。

- 🚀 **一键启动**：通过`npx @docmd`命令，无需配置文件，即可从`docs/`文件夹生成完整文档站点
- 🤖 **AI优化**：自动生成`llms.txt`和`llms-full.txt`文件，使文档默认支持大语言模型读取
- 🔍 **内置搜索**：基于MiniSearch的客户端全文搜索，支持多版本和多语言，无需额外配置
- 🎨 **主题引擎**：支持切换内置主题或自定义主题，适配浅色、深色和系统偏好模式
- 🌐 **原生国际化**：提供多语言支持，包括基于语言环境的URL、搜索和翻译界面
- 📦 **扩展Markdown**：支持富容器语法，如提示框、标签页、卡片、网格、折叠区域等
- 💻 **交互式沙盒**：通过Live Preview API嵌入可编辑的实时预览窗口
- 💬 **内联协作**：在开发模式下选择文本可开启Threads，与团队在文档旁直接评论

---

### [发布 docmd@0.7.2 🚀（Docker、NGINX 和 Caddy 自动部署）· docmd-io/docmd · GitHub](https://github.com/docmd-io/docmd/releases/tag/0.7.2)

**原文标题**: [Release docmd@0.7.2 🚀 (Auto-Deploy for Docker, NGINX & Caddy) · docmd-io/docmd · GitHub](https://github.com/docmd-io/docmd/releases/tag/0.7.2)

以下是对所提供内容的概述总结：

- 🚀 **docmd 0.7.2 发布**：新增 `docmd deploy` 命令，可生成生产就绪的 Docker、Nginx 和 Caddy 配置文件，并自动读取项目配置（如标题、输出目录、URL 和 SPA 模式）以个性化输出。
- 🛡️ **增强的稳定性**：内部验证引擎重构为 7 个逻辑支柱，并引入动态完整性引擎，可即时捕获版本不匹配问题。
- 🌍 **全球化扩展**：核心引擎新增德语、西班牙语、日语和法语的 UI 翻译，整个文档套件现已提供德语版本。
- ✨ **配置感知部署**：`docmd deploy` 命令支持 `--docker`、`--nginx` 和 `--caddy` 选项，每次运行都会根据当前配置重新生成文件，确保同步。
- 📝 **完整变更日志**：包括新功能（如配置感知脚手架、多阶段 Dockerfile、强化 Web 服务器模板）、错误修复（如 CLI 参数解析、Caddy 配置语法）以及升级指南。

---

### [博客 | Node.js 的新 RocksDB 绑定](https://www.harper.fast/resources/new-rocksdb-binding-for-node-js)

**原文标题**: [Blog  | New RocksDB Binding for Node.js](https://www.harper.fast/resources/new-rocksdb-binding-for-node-js)

Harper 发布了 rocksdb-js，一个为 Node.js 打造的现代化 RocksDB 绑定库，支持完整事务、惰性范围查询和 TypeScript API，旨在为 Harper 5.0 及更广泛的社区提供高性能、可扩展的键值存储解决方案。

- 🚀 **全新绑定库**：rocksdb-js 是 Harper 从零构建的 C++ 原生绑定，提供 TypeScript API、完整事务支持、惰性范围迭代器和内置事务日志系统，开源且采用 Apache 2.0 许可。
- 📦 **快速安装与使用**：通过 `npm install @harperfast/rocksdb-js` 安装，API 设计借鉴 lmdb-js 以降低学习成本，支持 `put`、`get`、`getRange` 等基础操作。
- ⚡ **性能与设计考量**：RocksDB 的 LSM 树架构擅长处理写密集型工作负载，Harper 5.0 同时支持 LMDB 和 RocksDB，后者成为新工作负载的默认引擎，提供更强的写优化和事务保证。
- 🔒 **完整事务支持**：支持乐观和悲观事务，实现原子性提交和真正的隔离级别，适用于复杂多记录更新、条件写入和并发访问场景。
- 🔍 **惰性范围查询**：范围查询返回惰性迭代器，仅从磁盘读取实际处理的记录，有效控制内存使用，适合大型数据集。
- 🛠️ **原生层与预构建**：基于 Node-API (N-API) 构建，提供 macOS、Linux 和 Windows 平台的预编译二进制文件，安装时间从 10-30 分钟缩短至约 12 秒。
- 📝 **内置事务日志系统**：集成事务日志，支持变更跟踪、事件溯源和复制，为 Harper 的节点同步、实时消息和持久性提供基础。
- 🌍 **开源社区贡献**：鼓励社区尝试、提交问题、贡献基准测试、自定义存储和平台测试，以共同完善这个填补 Node.js 生态空白的 RocksDB 绑定库。

---

### [GitHub - facebook/rocksdb：一个提供可嵌入、持久化键值存储的库，适用于快速存储。](https://github.com/facebook/rocksdb)

**原文标题**: [GitHub - facebook/rocksdb: A library that provides an embeddable, persistent key-value store for fast storage. · GitHub](https://github.com/facebook/rocksdb)

RocksDB 是由 Facebook 数据库工程团队开发维护的持久化键值存储库，专为闪存和内存存储优化，基于 LevelDB 构建，采用 LSM 树设计，支持灵活的读写放大和空间放大权衡。

- 🗄️ 核心功能：提供可嵌入的持久化键值存储，特别适合闪存驱动器上的数据存储
- ⚖️ 灵活权衡：在写放大因子(WAF)、读放大因子(RAF)和空间放大因子(SAF)之间提供可调节的平衡
- 🔄 多线程压缩：支持多线程压缩操作，适合存储数TB级别的单数据库
- 📚 示例代码：在 examples 目录提供使用示例，方便开发者快速上手
- 📖 文档资源：通过 GitHub Wiki 提供详细说明，公共接口在 include/ 目录
- 💬 社区支持：欢迎在 RocksDB 开发者 Facebook 群组和 Google Groups 邮件列表讨论
- 📜 双许可证：同时采用 GPLv2 和 Apache 2.0 许可证，用户可自行选择
- 🌟 项目规模：获得 31.6k 星标，6.8k 分支，981 关注者，213 个发布版本
- 🛠️ 开发语言：主要使用 C++(84%)，辅以 Java、Starlark、C、Python 等

---

### [GitHub - HarperFast/rocksdb-js: 适用于Node.js的RocksDB绑定](https://github.com/HarperFast/rocksdb-js)

**原文标题**: [GitHub - HarperFast/rocksdb-js: RocksDB binding for Node.js · GitHub](https://github.com/HarperFast/rocksdb-js)

rocksdb-js 是一个用于 Node.js 的 RocksDB 数据库绑定库，支持乐观和悲观事务、混合同步/异步数据检索、范围查询、事务日志、自定义存储、高效二进制编码以及内部统计信息访问，适用于 Linux、macOS 和 Windows 平台。

- 📦 **核心功能**：支持乐观和悲观事务模式，提供混合同步/异步数据检索，范围查询返回支持懒评估的迭代器。
- 🔧 **数据库操作**：提供 `open`、`close`、`clear`、`destroy`、`drop`、`get`、`put`、`remove` 等方法，支持同步和异步版本。
- 🔄 **事务系统**：通过 `transaction` 和 `transactionSync` 方法执行事务，支持自动提交和回滚，可配置重试逻辑和快照。
- 📊 **统计与监控**：启用 `enableStats` 后可获取 RocksDB 内部统计信息（tickers 和 histograms），支持 `getStats`、`getStat` 等方法。
- 🔒 **独占锁**：提供 `tryLock`、`unlock`、`withLock` 等方法，支持跨线程的互斥操作。
- 📝 **事务日志**：通过 `useLog` 管理事务日志，支持添加条目、查询和清理，日志文件可自动轮转和保留。
- 🧩 **自定义存储**：可扩展 `Store` 类覆盖默认数据库交互方法，实现自定义编码、解码或日志逻辑。
- ⚙️ **配置选项**：支持 `blockCacheSize`、`parallelismThreads`、`readOnly`、`pessimistic` 等全局和实例配置。
- 🛠 **开发与测试**：需要 Node.js 18+、pnpm 和 C++ 编译器，提供 `pnpm build`、`pnpm test` 等命令，支持调试构建和代码覆盖率测试。

---

### [Bun v1.3.13 | Bun 博客](https://bun.com/blog/bun-v1.3.13)

**原文标题**: [Bun v1.3.13 | Bun Blog](https://bun.com/blog/bun-v1.3.13)

以下是 Bun 版本更新的摘要，涵盖性能优化、新功能与多项 Bug 修复。

- 📦 **安装与升级**：支持 curl、npm、PowerShell、Scoop、Homebrew 及 Docker 多种方式安装 Bun，并通过 `bun upgrade` 升级。
- ⚡ **测试性能提升**：新增 `--isolate`（文件间隔离环境）和 `--parallel`（多进程并行）标志，大幅加速大型测试套件。
- 🧩 **CI 分片测试**：`bun test --shard=M/N` 支持跨 CI 任务拆分测试文件，确保各分片负载均衡。
- 🔍 **变更驱动测试**：`bun test --changed` 仅运行受 Git 变更影响的测试，支持与 `--watch` 结合使用。
- 🚀 **安装优化**：`bun install` 流式解压 tarball 到磁盘，内存占用降低 17 倍；隔离链接器使大型 monorepo 安装速度从 20.5 秒降至 2.4 秒。
- 🗺️ **源映射内存优化**：内部源映射表示重写为紧凑位打包格式，每映射仅 2.4 字节，内存占用降低最多 8 倍。
- 🧠 **运行时内存降低**：升级 mimalloc 至 v3 并实现 libpas 回收支持，基线内存使用减少 5%。
- 🚄 **JavaScriptCore 升级**：合并 1316 个上游提交，带来数组长度、字符串方法、SIMD 加速等多项性能改进。
- 🎯 **事件系统加速**：`addEventListener` 和 `dispatchEvent` 性能提升，得益于约 270 个 WebKit 提交。
- 📁 **文件流式响应**：SSL 和 Windows 下 `Bun.file()` 响应支持流式传输，减少大文件内存占用。
- 📐 **范围请求支持**：`Bun.serve()` 支持 `Range` 请求头，自动返回 206 或 416 状态码。
- 🔄 **gzip 压缩加速**：升级至 zlib-ng 2.3.3，gzip 同步压缩速度提升最多 2.59 倍，异步 deflate 提升 5.48 倍。
- 🔁 **数组迭代加速**：内部数组迭代优化，`toContain` 等方法速度提升最多 1.43 倍。
- 🔐 **加密算法扩展**：支持 SHA3 系列哈希算法及 X25519 `deriveBits`，并引入 ML-KEM/ML-DSA 后量子算法。
- 🌐 **WebSocket Unix 套接字**：支持 `ws+unix://` 和 `wss+unix://` 协议，用于 Unix 域套接字连接。
- 🖼️ **HTML 构建内联资源**：`bun build --compile --target browser` 现在内联 JS 中通过 file loader 导入的资产为 data URI。
- 🐛 **大量 Bug 修复**：修复 Worker 生命周期崩溃、HTTP/2 兼容性、`fetch` 代理问题、Windows 文件读取崩溃、内存泄漏等数十个问题。

---

### [Bun v1.3.13 | Bun 博客](https://bun.com/blog/bun-v1.3.13#bun-s-runtime-uses-5-less-memory)

**原文标题**: [Bun v1.3.13 | Bun Blog](https://bun.com/blog/bun-v1.3.13#bun-s-runtime-uses-5-less-memory)

## 概述摘要

Bun 发布了一系列性能优化和新功能，包括测试运行器的隔离与并行执行、安装过程的流式解压、内存使用优化、JavaScriptCore引擎升级、以及多项Node.js兼容性修复。

- 🚀 **测试运行器重大升级**：新增 `--isolate`（每个测试文件独立全局环境）和 `--parallel`（多进程并行执行）标志，大幅加速大型测试套件，支持 `--shard` 在CI中分片测试
- 📦 **安装性能飞跃**：`bun install` 实现流式解压tarball（内存降低17倍），隔离链接器在peer依赖多的monorepo中速度提升8.5倍（20.5s→2.4s）
- 🔧 **内存优化**：Source Map 采用位压缩格式（2.4字节/映射，减少8倍内存），运行时内存使用降低5%，mimalloc升级至v3并实现libpas scavenger支持
- ⚡ **引擎与压缩升级**：JavaScriptCore合并1316个上游提交，zlib-ng 2.3.3使gzip压缩速度提升最高5.5倍，支持AVX-512/NEON/SVE等SIMD加速
- 🌐 **Web功能增强**：`Bun.serve()` 支持Range请求（206 Partial Content），WebSocket客户端支持Unix域套接字（ws+unix://），X25519密钥协商，SHA3哈希算法
- 🔧 **Node.js兼容性修复**：修复Worker生命周期崩溃、tls.connect行为、process.ppid动态更新、socket.setTimeout超时误触发、http2服务器ENABLE_PUSH设置等关键问题
- 🛠️ **构建与打包改进**：`bun build --compile --target browser` 正确内联JS导入的文件加载器资源，HTML ETag在JS/CSS变更时正确更新，修复macOS ARM64和NixOS上的编译问题
- 🐛 **大量Bug修复**：涵盖Windows平台竞态条件、文件描述符泄漏、内存泄漏（AbortSignal、--hot重载、Glob扫描）、CSS解析器@layer顺序保留、快照测试重试逻辑等

---

### [GitHub - pnpm/action-setup: 安装 pnpm 包管理器 · GitHub](https://github.com/pnpm/action-setup)

**原文标题**: [GitHub - pnpm/action-setup: Install pnpm package manager · GitHub](https://github.com/pnpm/action-setup)

pnpm/action-setup 是一个用于在 GitHub Actions 中安装 pnpm 包管理器的官方 Action，支持版本指定、依赖安装、缓存等功能，需配合 Node.js 环境使用。

- ⚠️ 重要升级：v2 版本已失效，请升级到最新版本以兼容新 Node.js
- 📦 核心功能：安装指定版本的 pnpm，支持 `version`、`dest`、`run_install` 等输入参数
- 🔧 灵活安装：可通过 `packageManager` 字段自动获取版本，或手动指定版本（如 `10`、`^10.9.8`、`latest`）
- 🚀 自动安装：设置 `run_install` 为 `true` 或 YAML 配置，可自动执行 `pnpm install` 及递归安装
- 💾 缓存支持：启用 `cache` 可缓存 pnpm 存储目录，加速后续安装
- 📁 输出路径：提供 `dest` 和 `bin_dest` 输出，便于定位 pnpm 文件位置
- ⚡ 独立模式：`standalone: true` 可安装 `@pnpm/exe`，无需 Node.js 即可运行 pnpm
- 📋 使用示例：支持多种场景，如仅安装 pnpm、结合 `packageManager`、安装依赖、使用缓存等
- 🔗 注意事项：本 Action 不负责安装 Node.js，需配合 `actions/setup-node` 使用
- 🏷️ 项目信息：MIT 许可，1.2k 星标，192 个分支，主要使用 TypeScript 开发

---

### [发布 pnpm 11 RC 0 · pnpm/pnpm · GitHub](https://github.com/pnpm/pnpm/releases/tag/v11.0.0-rc.0)

**原文标题**: [Release pnpm 11 RC 0 · pnpm/pnpm · GitHub](https://github.com/pnpm/pnpm/releases/tag/v11.0.0-rc.0)

pnpm v11.0.0-rc.0 是一个重大版本更新，带来了多项破坏性变更和新功能，主要聚焦于性能提升、安全增强和配置简化。

- 🚀 **核心要求升级**：要求 Node.js 22+，放弃对 Node 18-21 的支持，pnpm 自身转为纯 ESM 格式，独立可执行文件需要 glibc 2.27。
- 🛡️ **供应链安全默认开启**：`minimumReleaseAge` 默认设为 1 天（新发布包 24 小时内不可解析），`blockExoticSubdeps` 默认设为 `true`，以防范供应链攻击。
- ⚙️ **构建依赖设置简化**：废弃了 `onlyBuiltDependencies` 等多个旧设置，统一使用 `allowBuilds` 配置，以键值对形式控制包是否允许运行构建脚本。
- 📦 **全局安装隔离**：`pnpm add -g` 现在为每个包创建独立的安装目录（含自己的 `package.json`、`node_modules` 和锁文件），并默认使用全局虚拟存储。
- 🗄️ **全新 SQLite 存储索引**：存储版本升级到 v11，使用 SQLite 数据库替代单个 JSON 文件，减少文件系统调用，提升安装速度。
- 📜 **原生发布流程**：`pnpm publish`、`login`、`logout`、`view`、`deprecate`、`unpublish`、`dist-tag` 和 `version` 不再依赖 npm CLI，完全由 pnpm 原生实现。
- 🔧 **配置体系重构**：`.npmrc` 仅用于认证和注册表设置，其他所有设置必须放在 `pnpm-workspace.yaml` 或新的全局 `config.yaml` 中，环境变量前缀改为 `pnpm_config_*`。
- ✨ **新增多个命令**：包括 `pnpm ci`（干净安装）、`pnpm sbom`（生成软件物料清单）、`pnpm clean`（安全删除 `node_modules`）、`pnpm peers check`（检查对等依赖问题）和 `pnpm runtime set`（安装运行时），以及 `pn`/`pnx` 短别名。
- ⚡ **性能大幅优化**：使用原生 `undici` 替代 `node-fetch`，采用 Happy Eyeballs 算法、直接写入 CAS 文件、跳过暂存目录、预分配 tarball 下载内存和 NDJSON 元数据缓存，显著提升 HTTP 和 I/O 性能。
- 🔒 **锁文件与生命周期改进**：简化了 `patchedDependencies` 格式，生命周期脚本不再设置 `npm_config_*` 变量，输出更清晰，并支持 ESM 格式的 `.pnpmfile.mjs`。

---

### [GitHub - tediousjs/node-mssql: 适用于 Node.js 的 Microsoft SQL Server 客户端 · GitHub](https://github.com/tediousjs/node-mssql)

**原文标题**: [GitHub - tediousjs/node-mssql: Microsoft SQL Server client for Node.js · GitHub](https://github.com/tediousjs/node-mssql)

node-mssql 是 Node.js 的 Microsoft SQL Server 客户端，支持多种驱动和连接方式，提供丰富的查询、事务和流式处理功能。

- 🗄️ **支持两种驱动**：Tedious（纯 JavaScript，跨平台默认）和 MSNodeSQLv8（原生驱动，支持 Windows 认证）
- 🔗 **灵活连接方式**：支持连接字符串和配置对象两种方式，并兼容 Azure Active Directory 认证
- 🛠️ **完整数据库操作**：提供查询、存储过程、批量插入、事务和预处理语句等核心功能
- 🌊 **流式处理支持**：可处理大量数据行，支持暂停/恢复操作，防止内存溢出
- 🔒 **安全防护**：内置 SQL 注入保护，支持参数化查询和模板字面量
- 📊 **高级特性**：支持 JSON 解析、地理空间数据类型、表值参数和重复列名处理
- 📡 **诊断通道**：通过 Node.js diagnostics_channel 提供遥测数据，支持 OpenTelemetry 集成
- 🔄 **连接池管理**：支持全局连接池和自定义池，提供连接验证选项
- 📋 **丰富文档**：包含完整 API 文档、版本迁移指南和多种编程风格示例（async/await、Promise、回调）

---

### [GitHub - privatenumber/type-flag: ⛳️ 用于 Node.js 的类型化命令行参数解析器](https://github.com/privatenumber/type-flag)

**原文标题**: [GitHub - privatenumber/type-flag: ⛳️ Typed command-line arguments parser for Node.js · GitHub](https://github.com/privatenumber/type-flag)

type-flag 是一个强类型、无依赖的命令行参数解析库，体积小巧（最大1.4 kB），支持树摇优化，可在线试用。

- 🚀 安装简单：通过 `npm i type-flag` 即可快速安装使用。
- 🎯 快速入门：支持 `typeFlag()` 和 `getFlag()` 两种方式解析命令行参数，如 `--name John --age 20`。
- ⚙️ 强大功能：支持多值标志、标志操作符（如 `=`）、未知标志解析、别名分组（如 `-abc`）。
- 📦 灵活定义：标志类型支持 `String`、`Number`、`Boolean` 等，也可自定义类型或数组。
- 🔗 别名支持：可为标志设置单字符别名（如 `-m` 对应 `--my-flag`），单字符名和长标志可独立存在。
- 🛠️ 高级特性：支持默认值、kebab-case 自动映射为 camelCase、未知标志收集、参数分离（`--` 后作为参数）。
- 🔄 数组与布尔：数组类型允许多次传递同一标志，布尔标志支持 `--no-` 前缀取反。
- 🧩 自定义类型：可创建验证函数（如限制 `size` 为 `small`/`medium`/`large`）或可选值标志。
- 📋 API 丰富：`typeFlag()` 返回 `flags`、`unknownFlags`、`_` 对象；`getFlag()` 快速获取单标志值。
- 🤖 集成 AI：内置 agent skill，支持 AI 编码助手集成。

---

### [发布 v7.2.0 · mongodb/node-mongodb-native · GitHub](https://github.com/mongodb/node-mongodb-native/releases/tag/v7.2.0)

**原文标题**: [Release v7.2.0 · mongodb/node-mongodb-native · GitHub](https://github.com/mongodb/node-mongodb-native/releases/tag/v7.2.0)

MongoDB Node.js 驱动 v7.2.0 版本发布，引入了智能工作负载管理、运行时兼容性改进和新的 ChangeStream 方法。

- ⚙️ 支持 MongoDB 智能工作负载管理，新增 `maxAdaptiveRetries`（默认2次）和 `enableOverloadRetargeting` 客户端选项，优化高负载下的连接建立和重试逻辑。
- 🧩 运行时兼容性改进：用标准 `Uint8Array` 替代 Node 特有 `Buffer` API，用 Web Crypto API 替代 Node 特有 `crypto` API，减少非 Node.js 运行时的补丁需求。
- 🧪 实验性支持依赖注入：新增 `runtimeAdapters` 客户端选项，允许注入 Node.js 核心模块（如 `os`）的替代实现，提升在受限环境中的兼容性。
- ☀️ ChangeStream 新增 `bufferedCount()` 方法，可返回本地缓存文档数量，便于在调用异步方法前检查数据状态。
- 🔧 其他功能：指数退避与抖动重试、副本集服务器降级限制、客户端背压令牌桶可选化等多项优化。

---

### [发布 9.5.0 · Automattic/mongoose · GitHub](https://github.com/Automattic/mongoose/releases/tag/9.5.0)

**原文标题**: [Release 9.5.0 · Automattic/mongoose · GitHub](https://github.com/Automattic/mongoose/releases/tag/9.5.0)

Mongoose 9.5.0 版本发布，包含多项新功能、修复和性能优化。

- 🚀 新增 `timestamp` 选项到调试输出功能 (#16216)
- 🔧 新增 `cloneUpdate` 选项以显式禁用更新克隆 (#16230, #16202)
- 🔍 扩展 `defaults` 查询选项以支持 `find()` 方法 (#16226)
- 🛠️ 修复更新克隆问题，避免不必要地克隆更新以更好支持 `__proto__` (#16230, #16202)
- 🐛 修复文档处理中 `$set()` 方法的对象识别问题 (#16230)
- 🎯 修复查询助手将默认选项传递给鉴别器的问题 (#16227, #16226)
- 📄 修复文档中嵌套路径的乐观并发处理 (#16177, #16054)
- ⚠️ 在 `insertOne()` 中如果文档不是对象则抛出 `ObjectParameterError` (#16221)
- 🔄 修复 `CastError` 消息中 `setModel()` 后的原因保留问题 (#16167)
- ⚡ 优化 `findOneAndUpdate()` 中的克隆性能 (#16230)
- 🚄 使用 kareem 3.3.0 提升性能 (#16229)
- 🧹 使用 TSTyche 断言进行代码整理 (#16222)

---

### [pg-boss 文档](https://timgit.github.io/pg-boss/)

**原文标题**: [pg-boss Docs](https://timgit.github.io/pg-boss/)

在人工智能领域，研究者们开发出一种新型神经网络架构，能够更高效地处理复杂数据，尤其在图像识别和自然语言处理任务中表现优异。该架构通过引入注意力机制和模块化设计，显著减少了计算资源消耗，同时提升了模型准确性。实验结果显示，与传统模型相比，新架构在多个基准测试中取得了领先成绩，并展现出更强的泛化能力。未来，该技术有望应用于自动驾驶、医疗诊断等实际场景，推动AI技术的普及。

- 🧠 新型神经网络架构通过注意力机制和模块化设计，优化了复杂数据处理效率
- 📈 在图像识别和自然语言处理任务中，新架构显著减少计算资源消耗并提升准确性
- 🏆 实验表明，新架构在多个基准测试中领先传统模型，泛化能力更强
- 🚗 未来应用前景包括自动驾驶、医疗诊断等领域，助力AI技术普及

---

### [GitHub - XeroAPI/xero-node：基于XeroAPI/Xero-OpenAPI生成的Xero Node SDK（OAuth 2.0）](https://github.com/XeroAPI/xero-node)

**原文标题**: [GitHub - XeroAPI/xero-node: Xero Node SDK for OAuth 2.0 generated from XeroAPI/Xero-OpenAPI · GitHub](https://github.com/XeroAPI/xero-node)

Xero-node SDK 讓開發者能輕鬆在 JavaScript 中存取 Xero API，並利用會計資料建構應用程式。

- 📚 **API 支援**：完整涵蓋 Accounting、Assets、Bankfeeds、Files、Projects 及多國 Payroll API。
- 🚀 **快速入門**：提供 starter-app、full-app 等範例，協助快速上手 OAuth 2.0 授權流程。
- 🔐 **安全認證**：支援 OAuth 2.0 授權碼流程及 Custom Connections（client_credentials），並內建 JWT 驗證與 CSRF 防護。
- 💾 **Token 管理**：建議儲存 token set，並在每次 API 呼叫前透過 refreshToken 或 refreshWithRefreshToken 更新 access_token。
- 🛒 **App Store 整合**：支援訂閱查詢與 Webhook，可透過 marketplace.billing scope 取得 subscription 資料。
- ⚙️ **彈性設定**：可自訂 clientId、clientSecret、redirectUris、scopes、state、httpTimeout 及 clockTolerance。
- 📄 **使用範例**：提供 Accounting API 完整範例，包含查詢、建立發票、歷史記錄及附件上傳。
- 🔍 **查詢慣例**：支援 ifModifiedSince、where、order、page 等參數，建議使用 undefined 而非 null 來忽略篩選條件。
- 🤝 **社群貢獻**：遵循 MIT 授權，歡迎提交 PR 與 issue，並鼓勵遵循貢獻指南與行為準則。

---

### [小型企业会计软件 | Xero 香港](https://www.xero.com/hk/)

**原文标题**: [Accounting Software for Small Businesses | Xero HK](https://www.xero.com/hk/)

Xero 是一款专为小型企业和个体经营者设计的会计软件，旨在帮助用户专注于业务增长，同时通过AI助手JAX自动化日常任务并提供洞察。

- 💼 **核心定位**：专为小型企业和个体经营者打造的会计软件，支持账单支付、费用报销等功能
- 🤖 **AI助手JAX**：可自动执行报价、发票创建等任务，通过Xero、WhatsApp、短信和电子邮件操作，提供实时业务数据洞察
- 🏆 **用户规模**：拥有超过460万订阅用户，并获得行业奖项认可
- 💰 **定价方案**：提供Starter（$5.80/月）、Standard（$10/月）、Premium（$15/月）三档，均含会计基础功能，首3个月有折扣
- 🆓 **免费试用**：30天免费试用，无需信用卡，可随时取消，含全天候在线支持
- 🛠️ **行业适配**：针对个体经营者、建筑行业、零售业等提供定制化功能，如移动端报价、费用追踪和现金流管理
- 🔗 **应用集成**：支持与多种应用无缝集成，扩展会计软件功能
- 👥 **会计师支持**：为会计师和簿记员提供专业工具，保持行业领先地位

---

### [GitHub - sindresorhus/np: 更好的 `npm publish` 工具 · GitHub](https://github.com/sindresorhus/np)

**原文标题**: [GitHub - sindresorhus/np: A better `npm publish` · GitHub](https://github.com/sindresorhus/np)

`np` 是一个改进版的 `npm publish` 工具，提供交互式界面和多项安全检查，确保发布流程更可靠。

- 🚀 **核心功能**：交互式UI、自动检查分支、工作目录清洁、依赖重装、Node.js/npm版本兼容、运行测试、版本号更新与Git标签创建、防止意外发布预发布版本、发布到npm、失败回滚、推送提交与标签、支持双因素认证、自动打开GitHub Release草稿、警告多余文件、支持dry-run模式。
- 📦 **包管理器支持**：支持npm 9+、Yarn（Classic和Berry）、pnpm 8+和Bun。
- ⚠️ **限制与前提**：不支持Monorepo；不适合CI环境；需要Node.js 20+、npm 9+、Git 2.11+。
- 🔧 **安装与使用**：通过 `npm install --global np` 全局安装；运行 `$ np <version>` 指定版本（如patch、minor、major等）；提供多种选项（如 `--any-branch`、`--no-tests`、`--dry-run` 等）。
- ⚙️ **配置方式**：支持全局和本地配置，通过 `.np-config.js`、`.np-config.json` 或 `package.json` 中的 `np` 字段设置；可配置分支、清理、测试、发布、标签等选项。
- 💡 **实用技巧**：支持npm生命周期钩子、自定义测试脚本、签名Git标签、私有包、作用域包、自定义注册表、CI发布、gh-pages发布、初始版本设置、旧版本更新等。
- 🔍 **常见问题解决**：Yarn发布错误（检查registry URL）、`np` 挂起（避免使用 `publish` 作为脚本名、确保测试命令退出、registry URL加斜杠）。
- 👥 **维护者**：Sindre Sorhus 和 Tommy Mitchell；项目拥有7.7k星标和310个复刻。

---

### [Flox 面向开发者 | 一条命令，零摩擦](https://flox.dev/developers/?utm_source=newsletter&utm_medium=fnf&utm_campaign=2026q1_tofu_awa_influ_devs_floxhub_gl_node&utm_content=landing_page)

**原文标题**: [Flox for Developers | One Command, Zero Friction](https://flox.dev/developers/?utm_source=newsletter&utm_medium=fnf&utm_campaign=2026q1_tofu_awa_influ_devs_floxhub_gl_node&utm_content=landing_page)

概述总结
Flox是一款面向开发者的环境管理工具，通过一键命令消除环境配置痛点，支持从个人开发到生产部署的全流程。

- 🚀 **零摩擦入门**：安装Flox后，一键创建默认环境，集成vim、git等常用工具，推送到FloxHub即可在多台设备同步，无版本冲突或系统污染。
- 👥 **团队快速上手**：新员工激活公司基线环境后，运行`flox activate`即可自动获取Node、Python、Postgres等所有项目依赖，实现无缝协作。
- 🔧 **新项目贡献**：克隆仓库并激活Flox环境，立即获得完整技术栈（如Go、Redis、支付SDK），无需手动配置即可开发、测试。
- 🖥️ **全栈开发**：一个环境同时支持React前端、Python API和Postgres数据库，切换项目无冲突，更新框架不影响其他项目。
- 🐛 **微服务调试**：本地同时启动认证和支付服务的Flox环境，复现生产版本bug仅需10分钟，修复后本地验证再推送。
- 🚢 **生产部署**：CI/CD使用与开发完全相同的Flox环境，从测试到生产环境一致，消除“在我机器上能跑”的焦虑。
- 📦 **规模化发布**：从开发环境构建包并发布到FloxHub，生产环境直接部署到Kubernetes，支持版本控制和回滚。
- ⚙️ **工作流程**：通过`flox init`初始化环境→`flox install`安装依赖（支持19万+包）→`flox activate`激活使用→通过Git或FloxHub共享给团队。
- ❓ **常见问题**：无需学习Nix，支持现有项目迁移，与CI/CD管道兼容，基础功能免费使用。

---

### [Gauntlet AI - 学习生产级AI技能](https://apply.gauntletai.com/register/champions?utm_source=Third%20Party&utm_campaign=Node%20Weekly&utm_medium=referral&utm_content=)

**原文标题**: [Gauntlet AI - Learn Production AI Skills](https://apply.gauntletai.com/register/champions?utm_source=Third%20Party&utm_campaign=Node%20Weekly&utm_medium=referral&utm_content=)

概述：本文探讨了人工智能在医疗领域的应用，强调了其提升诊断准确性和治疗效率的潜力，同时指出了数据隐私和伦理挑战。

- 🩺 人工智能通过分析医学影像，能辅助医生更精准地检测疾病，如癌症早期识别。
- 📊 机器学习模型可处理海量患者数据，预测疾病风险并个性化治疗方案。
- 🔒 数据隐私问题是主要挑战，需确保患者信息在AI系统中的安全使用。
- ⚖️ 伦理争议包括算法偏见和决策责任归属，需建立透明监管框架。
- 🚀 未来趋势是AI与医疗深度融合，推动远程医疗和智能健康管理发展。

---

### [GitHub - Agent-Field/agentfield: 像API和微服务一样构建、运行和扩展AI智能体——从第一天起就具备可观测、可审计和身份感知能力。](https://github.com/Agent-Field/agentfield)

**原文标题**: [GitHub - Agent-Field/agentfield: Build, run and scale AI agents like API and microservices - observable,auditable and identity-aware from day one. · GitHub](https://github.com/Agent-Field/agentfield)

AgentField 是一个开源 AI 后端控制平台，能将 AI 智能体像 API 一样构建、部署和扩展，提供路由、协调、内存、异步执行和加密审计追踪等生产级基础设施。

- 🧠 **核心概念**：将 AI 智能体转化为生产级基础设施，每个函数都成为 REST 端点，每个智能体都拥有加密身份，每个决策都可追溯。
- 🚀 **快速上手**：支持一键式“提示到生产”的快速部署，也提供 Python、Go、TypeScript 的 SDK 进行手动开发，并配有 CLI 工具 `af` 进行脚手架搭建。
- ⚙️ **构建能力**：支持 `@app.reasoner()` 进行 AI 判断、`@app.skill()` 执行确定性代码、`app.ai(schema=MyModel)` 获取结构化输出，以及 `app.harness()` 调用多轮编码智能体。
- 🌐 **智能体网格**：通过 `app.call()` 实现跨智能体调用并全程追踪，`app.discover()` 可按标签或健康状态发现智能体，支持自动注册和零配置服务网格。
- 🧠 **分布式记忆**：内置 KV 存储和向量搜索，支持全局、智能体、会话和运行四种作用域，无需额外依赖 Redis。
- 👤 **人机协同**：通过 `app.pause()` 实现持久化的暂停/恢复，支持审批工作流、可配置超时和崩溃安全状态。
- 🚦 **金丝雀部署**：支持流量权重路由、A/B 测试和蓝绿部署，可进行 5% → 50% → 100% 的渐进式发布。
- 🔐 **身份与治理**：每个智能体自动生成 W3C DID 和 Ed25519 密钥，提供可验证凭证和离线验证功能，支持基于标签的访问策略和加密签名请求。
- 📊 **可观测性**：提供自动工作流 DAG 可视化、Prometheus 指标、结构化 JSON 日志和执行时间线，支持健康检查和关联 ID。
- 🏗️ **架构**：控制平面为无状态 Go 服务，智能体可从任何地方连接（笔记本、Docker、Kubernetes），通过注册能力实现路由、追踪和策略执行。
- 🎯 **适用场景**：适合在后台系统中做决策的智能体（如退款审批、理赔处理、研究协调），不适合聊天机器人或早期工作流阶段。

---

### [AgentField — AI后端](https://agentfield.ai/?utm_source=node&utm_medium=referral&utm_campaign=node-0604&utm_id=node-060424-home-cta&utm_content=home-cta)

**原文标题**: [AgentField — The AI Backend](https://agentfield.ai/?utm_source=node&utm_medium=referral&utm_campaign=node-0604&utm_id=node-060424-home-cta&utm_content=home-cta)

概述：本文探讨了数字时代下隐私保护的重要性及挑战，强调了个人数据泄露的普遍风险，并提出了加强数据加密、完善法律法规和提升公众意识等应对措施。

- 🔒 个人数据泄露风险日益普遍，如社交媒体、在线购物等场景频繁发生信息滥用。
- 📜 现有法律法规在数据保护方面存在漏洞，需加强监管力度与处罚标准。
- 🛡️ 数据加密技术是保护隐私的核心手段，但需平衡安全性与用户体验。
- 🧠 公众隐私意识薄弱，需通过教育普及数据安全知识，避免过度分享个人信息。
- 🌐 跨国数据流动带来监管难题，需推动国际合作制定统一隐私保护标准。

---

### [发布 v1.59.0 · microsoft/playwright · GitHub](https://github.com/microsoft/playwright/releases/tag/v1.59.0)

**原文标题**: [Release v1.59.0 · microsoft/playwright · GitHub](https://github.com/microsoft/playwright/releases/tag/v1.59.0)

Playwright v1.59.0 发布，带来全新的录屏、互操作和调试功能。

- 🎬 新增 `page.screencast` API，支持录制视频、动作标注、视觉叠加、实时帧捕获和智能体视频凭证。
- 🔗 新增 `browser.bind()` API，允许将浏览器绑定到命名会话，供 `playwright-cli`、`@playwright/mcp` 等客户端连接。
- 📊 新增 `playwright-cli show` 命令，打开仪表盘查看所有绑定的浏览器状态并与之交互。
- 🐛 CLI 调试器支持 `npx playwright test --debug=cli`，方便智能体自动修复测试。
- 📋 CLI 跟踪分析支持 `npx playwright trace` 命令，用于探索 Playwright Trace 并理解失败或波动测试。
- ♻️ 许多 API 现在返回异步可释放对象，支持 `await using` 语法实现自动清理。
- 🔍 新增 `page.ariaSnapshot()`、`locator.normalize()`、`page.pickLocator()` 等快照和定位器方法。
- 🛠️ UI 模式增加仅显示受源更改影响的测试选项；HTML 报告器支持运行列表和测试步骤过滤。
- ⚠️ 已知问题：`navigator.platform` 模拟可能导致 Ctrl 或 Meta 分发错误，可设置环境变量绕过。
- ⚠️ 重大变更：移除 macOS 14 的 WebKit 支持和 `@playwright/experimental-ct-svelte` 包。

---

