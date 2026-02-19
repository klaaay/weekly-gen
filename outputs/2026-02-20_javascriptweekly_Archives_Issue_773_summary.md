### [JavaScript 周刊第 773 期：2026 年 2 月 17 日](https://javascriptweekly.com/issues/773)

**原文标题**: [JavaScript Weekly Issue 773: February 17, 2026](https://javascriptweekly.com/issues/773)

本期通讯聚焦 JavaScript 和 Web 开发领域的最新动态，涵盖新工具发布、技术更新及行业趋势。

- 🚀 TanStack 推出跨平台热键库 Hotkeys，支持多步骤序列和用户快捷键录制，目前处于 Alpha 阶段，主要关注 React 适配。
- 🤖 Meticulous AI 提供自动化 E2E UI 测试解决方案，帮助 Notion、Dropbox 等公司实现高覆盖率测试，无需人工编写。
- 🔧 TypeScript 6.0 Beta 发布，为过渡到 Go 驱动的 TypeScript 7 做准备，包含多项破坏性变更和配置清理。
- 📊 State of React 调查结果公布，同时 Google 展示 WebMCP 预览，旨在为 AI 代理提供标准化网站能力接口。
- 🛠️ 多个工具更新：Biome 2.4 增强 CSS 和 GraphQL 支持，React Native 0.84 默认启用 Hermes V1 引擎，Node.js 发布新版本。
- 📖 技术文章涵盖 CodeMirror 扩展、Node.js HTTP 请求优化、虚拟滚动实现及反对 JS 重型架构的性能讨论。
- ⚡ 新工具包括 Electrobun 桌面应用框架、Console Ninja 调试工具、网络模拟库 fetch-network-simulator 及轻量级页面头库 Peek。
- 🎨 社区动态：DPaint.JS 图像编辑器更新，almostnode 项目将 Node.js 带入浏览器，CSS 使用报告揭示现代网站样式规模。

---

### [TanStack 热键](https://tanstack.com/hotkeys/latest)

**原文标题**: [TanStack Hotkeys](https://tanstack.com/hotkeys/latest)

TanStack Hotkeys 是一个用于处理键盘快捷键的 TypeScript 库，提供类型安全、跨平台支持，并包含序列检测、按键状态跟踪和快捷键录制等功能。

- 🎯 **类型安全与跨平台** – 通过类型安全的 Hotkey 字符串定义快捷键，跨平台 Mod 修饰符自动适配 macOS 的 Cmd 和其他系统的 Ctrl。
- ⚙️ **智能默认设置** – 内置合理的默认行为，如自动阻止默认事件和事件冒泡，智能忽略输入框焦点，并支持按元素或引用范围限定快捷键。
- 🔄 **快捷键序列与录制** – 支持多步骤键盘序列（如 Vim 风格命令），并提供内置录制功能，允许用户自定义快捷键。
- 🛠️ **功能丰富** – 提供按键保持检测、冲突警告、显示格式化工具、轻量级且支持 Tree-Shaking 等完整键盘交互工具集。
- 👥 **维护与合作伙伴** – 由 Kevin Van Cott 等维护者主导，并开放合作伙伴计划，共同推动库的发展。

---

### [TanStack | 面向 Web 开发者的高质量开源软件](https://tanstack.com/)

**原文标题**: [TanStack | High Quality Open-Source Software for Web Developers](https://tanstack.com/)

TanStack 是一个为 Web 开发者提供高质量开源软件的工具集合，专注于构建无头、类型安全且功能强大的 Web 应用工具，涵盖路由、状态管理、数据可视化、表格等多个领域，并以其框架无关、生产就绪的特性受到广泛信任和使用。

- 🧩 **核心库与框架**：提供 TanStack Start（全栈框架）、Router（类型安全路由）、Query（异步状态管理）和 Store（响应式数据存储）等核心工具，支持 React、Vue、Solid 等多种框架。
- 🛠️ **UI 与用户体验**：包括 Table（高性能表格）、Form（类型安全表单）、Hotkeys（键盘快捷键管理）和 Virtual（列表虚拟化）等库，帮助开发者构建高效且可控的界面。
- ⚡ **性能优化工具**：提供 Pacer（防抖、节流等性能优化工具）和 Virtual（大规模列表渲染优化），确保应用流畅运行。
- 🔧 **开发与工具链**：包含 Devtools（统一开发工具面板）、Config（包发布配置工具）和 CLI（命令行与 AI 工具包），提升开发效率与协作。
- 🤖 **AI 与数据管理**：推出 TanStack AI（多供应商 AI SDK 统一接口）和 DB（客户端优先的响应式数据存储），专注于现代数据流与智能集成。
- 🌐 **社区与生态**：拥有活跃的社区支持（如 Discord）、详细文档、博客教程和赞助计划，并强调开源、无供应商锁定的原则。

---

### [概述 | TanStack 热键文档](https://tanstack.com/hotkeys/latest/docs/overview)

**原文标题**: [Overview | TanStack Hotkeys Docs](https://tanstack.com/hotkeys/latest/docs/overview)

TanStack Hotkeys 是一个类型安全、框架无关的键盘快捷键处理库，提供全面的工具集，支持热键注册、按键状态跟踪、自定义快捷键录制和多键序列处理，具备一流的 TypeScript 支持和跨平台兼容性。

- 🎯 **类型安全的热键字符串**：支持完整自动补全，如 `Control+A`，也可使用原始对象注册热键。
- 🌍 **跨平台兼容性**：`Mod` 键在 macOS 上解析为 `Meta`（Cmd），在 Windows/Linux 上解析为 `Control`。
- ⌨️ **热键注册与管理**：通过集中的 `HotkeyManager` 实现按目标监听、冲突检测和自动输入过滤。
- 🔢 **多键序列支持**：支持 Vim 风格序列（如 `['G', 'G']`），可配置超时时间。
- ⏺️ **热键录制功能**：为设置界面提供交互式捕获，支持便携的 `Mod` 格式转换。
- 📊 **按键状态跟踪**：提供实时按键状态钩子，如 `useHeldKeys`、`useKeyHold`。
- 🖥️ **显示格式化**：支持平台感知的格式化（如 Mac 显示 `⌘⇧S`，Windows 显示 `Ctrl+Shift+S`）。
- ⚛️ **框架适配**：提供 React 钩子，如 `useHotkey`、`useHotkeySequence` 等。
- 🛠️ **开发者工具**：实时查看已注册热键、按下的按键等状态。

---

### [精密 AI——无需编写测试的自动化前端测试](https://www.meticulous.ai?utm_source=jsweekly&utm_medium=referral&utm_campaign=26q1&utm_content=primary)

**原文标题**: [Meticulous AI - Automated Frontend Testing Without Writing Tests](https://www.meticulous.ai?utm_source=jsweekly&utm_medium=referral&utm_campaign=26q1&utm_content=primary)

Meticulous AI 是一款创新的自动化测试工具，通过记录用户与应用交互生成并维护测试套件，无需手动编写或维护测试，帮助开发团队高效、无缺陷地交付代码。

- 🚀 无需编写或维护测试：通过记录用户交互自动生成覆盖所有代码分支、用户流程和边缘情况的测试套件。
- 🔄 测试自动演进：随着应用更新，测试套件自动添加新测试并淘汰过时测试，保持测试的时效性和完整性。
- ⚡ 闪电般快速执行：利用并行计算技术，能在 120 秒内完成数千个屏幕的测试。
- 🛡️ 消除测试波动：基于 Chromium 构建的确定性调度引擎，从根本上消除测试的不稳定性。
- 🔗 易于集成：支持多种前端框架（如 React、Vue、Angular 等），只需添加脚本标签即可快速设置。
- 📈 提升开发效率：被 Dropbox、Notion 等超过 100 家组织信任，帮助团队加速迭代并确保代码质量。

---

### [TypeScript 6.0 Beta 版本发布](https://devblogs.microsoft.com/typescript/announcing-typescript-6-0-beta/)

**原文标题**: [Announcing TypeScript 6.0 Beta - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-6-0-beta/)

TypeScript 6.0 Beta 版本发布，这是基于当前 JavaScript 代码库的最后一次主要更新，旨在为使用 Go 重写的 TypeScript 7.0 原生版本铺平道路。此版本引入了多项新特性、改进以及为适应现代 JavaScript 生态而进行的重大破坏性变更和弃用。

- 🚀 **无 `this` 函数的上下文敏感性降低**：对于未使用 `this` 的函数，TypeScript 6.0 在类型推断时不再将其视为上下文敏感函数，从而解决了之前方法语法中可能出现的类型推断问题。
- 📁 **支持以 `#/` 开头的子路径导入**：现在 TypeScript 支持 Node.js 中允许的以 `#/` 为前缀的子路径导入映射，简化了项目内部的模块引用路径。
- 🔧 **`--moduleResolution bundler` 可与 `--module commonjs` 组合使用**：这为许多项目提供了从旧版 `node` 模块解析策略升级的合适路径。
- 🧩 **新增 `--stableTypeOrdering` 标志**：此标志使 TypeScript 6.0 的类型排序行为与 7.0 保持一致，旨在帮助诊断两个版本间的差异，但可能会带来性能开销。
- 🎯 **新增 `es2025` 作为 `target` 和 `lib` 选项**：虽然 ES2025 未引入新语法，但增加了新的内置 API 类型，并将一些声明从 `esnext` 移至 `es2025`。
- ⏳ **内置 `Temporal` API 类型**：为已进入 Stage 3 的 Temporal 日期时间提案提供了内置类型支持，可通过 `esnext` 等 lib 配置使用。
- 🗺️ **新增 Map/WeakMap 的 `getOrInsert` 等方法类型**：为 ECMAScript 新增的 "upsert" 方法提供了类型支持，简化了常见的检查 - 设置模式。
- 🛡️ **新增 `RegExp.escape` 类型**：为用于转义正则表达式特殊字符的新标准方法提供了类型支持。
- 🌐 **`dom` lib 现在包含 `dom.iterable` 和 `dom.asynciterable`**：简化了配置，现在只需指定 `dom` 即可使用 DOM 集合的迭代方法。
- ⚠️ **多项破坏性变更与弃用**：包括默认启用 `strict` 模式、`module` 默认值改为 `esnext`、弃用 `target: es5`、`--moduleResolution node`、`--baseUrl`、`--outFile` 等，旨在推动项目向现代开发实践和 TypeScript 7.0 过渡。

---

### [TypeScript 7 进展 - 2025 年 12 月 - TypeScript](https://devblogs.microsoft.com/typescript/progress-on-typescript-7-december-2025/)

**原文标题**: [Progress on TypeScript 7 - December 2025 - TypeScript](https://devblogs.microsoft.com/typescript/progress-on-typescript-7-december-2025/)

TypeScript 7.0（代号“Corsa”）的开发进展顺利，已进入稳定可用的阶段。该版本通过将编译器与语言服务重写为原生代码，显著提升了性能、内存使用效率与并行处理能力。目前，其语言服务已在 VS Code 扩展中提供预览，支持代码补全、跳转定义、重命名等核心功能，且编译器类型检查已接近完成，与 TypeScript 6.0 高度兼容。团队宣布 TypeScript 6.0 将是最后一个基于 JavaScript 代码库的版本，后续将全力投入 7.0 的开发，以尽快实现全面迁移。

- 🚀 **性能大幅提升**：原生代码重写带来近 10 倍编译速度提升，支持多线程并行构建，内存占用更低。
- 🔧 **编辑器支持完善**：VS Code 扩展已提供稳定的语言服务预览，包含自动导入、重命名、查找引用等关键功能。
- ✅ **类型检查高度兼容**：TypeScript 7.0 与 6.0 在错误检测上基本一致，现有项目可安全用于类型验证。
- ⚠️ **注意变更与限制**：默认启用`--strict`、移除部分已弃用配置（如`--target es5`），且 JavaScript/JSDoc 检查更严格，可能导致更多错误。
- 🔄 **构建与增量编译**：支持`--incremental`、项目引用和`--build`模式，大幅提升大型项目构建效率。
- 📅 **版本规划明确**：TypeScript 6.0 为最终 JavaScript 版本，后续仅提供安全补丁；7.0 将作为主要发展方向。
- 🐛 **问题反馈与迁移**：团队鼓励开发者试用预览版并报告问题，但语言服务相关旧问题需在新版本中重新验证提交。
- ⏳ **待完成功能**：JavaScript 发射管道（尤其针对旧版目标）、`--watch`模式优化及完整 API 支持仍在开发中。

---

### [TypeScript 6.0 Beta 版本发布](https://devblogs.microsoft.com/typescript/announcing-typescript-6-0-beta/#breaking-changes-and-deprecations-in-typescript-6.0)

**原文标题**: [Announcing TypeScript 6.0 Beta - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-6-0-beta/#breaking-changes-and-deprecations-in-typescript-6.0)

TypeScript 6.0 Beta 版本发布，这是基于当前 JavaScript 代码库的最后一个主要版本，旨在为使用 Go 重写的 TypeScript 7.0 原生版本铺平道路。此版本引入了多项新特性、改进以及为未来版本对齐所做的调整，同时包含大量破坏性变更和弃用项，以反映现代 JavaScript 生态系统的演进。

- 🚀 **TypeScript 6.0 是当前代码库的最终版本**，作为 5.9 与 7.0 之间的桥梁，主要变化旨在为采用 7.0 做准备。
- 🔧 **改进 `this` 无关函数的上下文敏感性推断**：若函数未使用 `this`，则不再视为上下文敏感，提升了类型推断的优先级和准确性。
- 📁 **支持以 `#/` 开头的子路径导入**：Node.js 20+ 支持，现可在 `--moduleResolution` 设为 `node20`、`nodenext` 或 `bundler` 时使用。
- ⚙️ **允许 `--moduleResolution bundler` 与 `--module commonjs` 组合**：为许多项目提供了合适的升级路径。
- 🆔 **新增 `--stableTypeOrdering` 标志**：使 6.0 的类型排序行为与 7.0 一致，帮助迁移，但可能降低性能。
- 🎯 **新增 `es2025` 作为 `target` 和 `lib` 选项**：包含新的内置 API 类型（如 `RegExp.escape`），并将部分声明从 `esnext` 移至 `es2025`。
- ⏳ **内置 Temporal API 类型**：提案已进入 Stage 3，可通过 `--target esnext` 或 `"lib": ["esnext"]` 使用。
- 🗺️ **新增 Map/WeakMap 的 `getOrInsert` 与 `getOrInsertComputed` 方法类型**：简化“存在则获取，否则插入”模式。
- 🛡️ **新增 `RegExp.escape` 函数类型**：用于转义正则表达式特殊字符，包含在 `es2025` 库中。
- 🌐 **`dom` 库现在包含 `dom.iterable` 和 `dom.asynciterable`**：简化配置，现代浏览器均支持这些功能。
- ⚠️ **多项破坏性变更与弃用**：包括默认启用 `strict`、`module` 默认改为 `esnext`、弃用 `target: es5`、`--moduleResolution node`、`--baseUrl`、`--outFile` 等，需调整配置以适应现代开发实践。
- 🚫 **命令指定文件时若存在 `tsconfig.json` 将报错**：新增 `--ignoreConfig` 标志以忽略配置。
- 🔮 **为 TypeScript 7.0 做准备**：6.0 中的弃用项在 7.0 将完全移除，建议尽快处理警告。

---

### [React 2025 现状](https://2025.stateofreact.com/en-US)

**原文标题**: [State of React 2025](https://2025.stateofreact.com/en-US)

React 在 2024 年继续展现出强大的生命力，不仅未被快速变化的网络开发环境淘汰，反而持续进化，甚至有时引领趋势。随着生成式 AI 依赖现有代码库生成新代码，React 可能进一步巩固其地位，成为首个“永久框架”。虽然今年调查参与度因时间较晚而有所下降，但仍提供了有价值的见解，揭示了生态系统的未来走向。

- 🚀 React 持续进化，适应并引领网络开发趋势
- 🤖 生成式 AI 可能使 React 成为“永久框架”
- 📊 2024 年调查参与度下降，但仍提供关键洞察
- 🔍 调查独立进行，与 Meta、Vercel 等无关
- 📧 可订阅以获取下次调查通知
- 🌍 感谢全球志愿者提供多语言翻译支持
- 🤝 合作伙伴包括 Google Chrome 团队等多家技术公司

---

### [WebMCP 现已开放早期预览  | 博客  |  Chrome 开发者](https://developer.chrome.com/blog/webmcp-epp)

**原文标题**: [WebMCP is available for early preview  |  Blog  |  Chrome for Developers](https://developer.chrome.com/blog/webmcp-epp)

WebMCP 是一项旨在帮助网站与 AI 智能体进行结构化交互的新标准，通过提供声明式和命令式 API，使网站能够更可靠、高效地支持智能体执行任务，如客户支持、电商购物和旅行预订等。

- 🚀 **WebMCP 提供早期预览**：开发者可通过早期预览计划获取文档和演示，探索如何让网站支持 AI 智能体交互。
- 🛠️ **结构化交互提升效率**：通过声明式 API（基于 HTML 表单）和命令式 API（基于 JavaScript），使智能体能更快速、精准地执行操作，如填写工单或完成购物流程。
- 🌐 **赋能智能体应用场景**：支持客户支持、电商购物和旅行预订等复杂任务，帮助智能体自动处理技术细节、筛选商品或预订航班。
- 🔗 **加入预览计划**：参与早期预览可及时了解 API 更新，获取示例代码，并推动智能体与网站交互的标准化发展。

---

### [Biome v2.4——嵌入式代码片段、HTML 可访问性与更优框架支持 | Biome](https://biomejs.dev/blog/biome-v2-4/)

**原文标题**: [Biome v2.4—Embedded Snippets, HTML Accessibility, and Better Framework Support | Biome](https://biomejs.dev/blog/biome-v2-4/)

Biome v2.4 作为今年的首个次要版本发布，带来了多项重要新特性与改进，包括对 JavaScript 中内嵌 CSS 和 GraphQL 代码片段的格式化与检查、编辑器内联配置、HTML 可访问性规则、规则性能分析器，以及对 Vue、Svelte 和 Astro 等 HTML 类语言的增强支持。此外，还引入了新的辅助操作、提升的规则、格式化器选项、CLI 增强功能，并改进了配置文件的发现机制。

- 🧩 **内嵌代码片段支持**：实验性功能，可自动格式化和检查 JavaScript 文件内（如 styled-components、GraphQL 查询）的 CSS 和 GraphQL 模板字面量。
- ⚙️ **编辑器内联配置**：编辑器可向 Biome 语言服务器注入配置，该配置会与项目配置合并并优先生效，便于临时调整规则（如关闭 `noConsole`）。
- 🌐 **HTML 类语言增强**：显著改进了 Vue 和 Svelte 的解析能力，减少了 `noUnusedVariables` 等规则的误报，并支持解析 Vue SFC 中的 CSS 模块语法（如 `:slotted`）。
- ♿ **HTML 可访问性规则**：新增 15 条专注于可访问性的 lint 规则，如 `useAltText`、`useHtmlLang`，助力构建更易访问的 Web 应用。
- ⏱️ **规则性能分析器**：`lint` 和 `check` 命令新增 `--profile-rules` 标志，可分析各 lint 规则、辅助操作和 GritQL 插件的执行时间，帮助定位性能瓶颈。
- 📁 **配置文件发现改进**：现在支持加载 `.biome.json` 等隐藏配置文件，并会尝试从各操作系统特定的配置目录（如 `~/.config/biome`）加载配置。
- 🛠️ **新的辅助操作与规则增强**：新增了如“移除重复 CSS 类”和“排序接口成员”等辅助操作；为 `useSortedKeys`、`useHookAtTopLevel` 等规则增加了新的配置选项，提升了灵活性和准确性。
- 🆕 **新增 `types` 规则域**：引入新的 `types` lint 域，专门管理需要类型推断引擎的规则，允许通过 `--only` 和 `--skip` 标志更精细地控制类型相关检查。
- 🚀 **规则升级**：将 24 条 nursery 规则提升至稳定的 `correctness`、`suspicious`、`complexity` 和 `style` 组别，使其可用于生产环境。
- ✨ **格式化器更新**：新增 `trailingNewline` 选项以控制文件末尾换行符；支持在文件顶部使用 `biome-ignore-all format` 注释来全局禁用格式化；修复代码时自动应用格式化。
- 🖥️ **CLI 功能增强**：`check` 和 `ci` 命令的 `--skip` 和 `--only` 标志现在支持规则、操作、组和域；支持使用多个报告器并将输出保存至文件；新增 SARIF 格式报告器。
- 🔧 **其他改进**：包括 GritQL 新增 JSON 语言支持、LSP 进度报告、支持 Cursor 编辑器配置文件、CSS 解析器支持 `@function` 规则及自动检测 CSS Modules 等。

---

### [React Native 0.84 - 默认启用 Hermes V1 · React Native](https://reactnative.dev/blog/2026/02/11/react-native-0.84)

**原文标题**: [React Native 0.84 - Hermes V1 by Default · React Native](https://reactnative.dev/blog/2026/02/11/react-native-0.84)

React Native 0.84 版本发布，默认启用 Hermes V1 引擎，带来显著性能提升，同时继续移除旧架构代码，并默认使用预编译的 iOS 二进制文件以加快构建速度。

- 🚀 Hermes V1 现为默认 JavaScript 引擎，自动提升应用执行速度并降低内存使用，无需迁移配置
- ⚡ iOS 默认启用预编译二进制文件，大幅减少干净构建时的编译时间
- 🗑️ 继续移除 iOS 和 Android 的旧架构组件，iOS 构建默认不再包含旧架构代码，减少应用体积
- 📦 最低要求 Node.js 22.11 版本，以支持现代 JavaScript 特性
- 🛠️ 同步 React 19.2.3，支持 ESLint v9 扁平配置，并新增图像格式和键盘事件等平台功能
- ♿ 改进可访问性，如交互式文本自动获得链接角色，修复 Android 回收视图的状态问题
- 🔗 增强 URL API，添加标准属性和方法，更接近 Web 标准
- ⚠️ 包含一些破坏性变更，如 iOS 图像观察者 API 调整，Android 移除 BridgeDevSupportManager 等
- 📢 弃用 XHRInterceptor 等网络拦截 API，推荐使用 Chrome DevTools Protocol
- 🙏 感谢 95 位贡献者的 650 多次提交，特别鸣谢几位关键贡献者
- 🔄 提供升级指南，可通过 React Native Upgrade Helper 或新 AI 技能辅助升级，新项目可使用最新 CLI 初始化

---

### [Node.js — Node.js 25.6.1（当前版本）](https://nodejs.org/en/blog/release/v25.6.1)

**原文标题**: [Node.js — Node.js 25.6.1 (Current)](https://nodejs.org/en/blog/release/v25.6.1)

Node.js 25.6.1（Current）版本发布，包含多项依赖更新、性能优化、错误修复及文档改进，并提供了各平台的安装包和二进制文件下载链接。

- 🛠️ **依赖更新**：将 cjs-module-lexer 替换为 merve，并升级 npm 至 11.9.0，同时更新了多个核心依赖如 undici、minimatch 等。
- 🐛 **错误修复**：解决了 Windows 上 DNS SRV 查询的 ECONNREFUSED 问题，修复了模块加载、网络连接及测试中的多个缺陷。
- 📚 **文档完善**：更新了安全警告、弃用说明及工具安装指南，并修正了多处文档错误和链接。
- ⚡ **性能优化**：通过内存分配改进、SIMD 加速和代码重构，提升了 HTTP 头部解析、SQLite 操作及字符串处理的效率。
- 🔧 **工具与测试增强**：更新了构建工具链，优化了测试框架，并统一了快照测试模式，提升了开发体验和测试稳定性。
- 📦 **多平台支持**：提供了 Windows、macOS、Linux 等多种操作系统的安装包和二进制文件，确保广泛兼容性。

---

### [Node.js — Node.js 24.13.1（长期支持版）](https://nodejs.org/en/blog/release/v24.13.1)

**原文标题**: [Node.js — Node.js 24.13.1 (LTS)](https://nodejs.org/en/blog/release/v24.13.1)

Node.js 24.13.1（LTS）版本发布，代号“Krypton”，包含多项功能更新、依赖升级、错误修复和性能改进，并新增了三位协作者。

- 🐍 构建系统新增对 Python 3.14 的支持。
- 📊 CLI 中将 `--heapsnapshot-near-heap-limit` 和 `--build-snapshot` 相关选项标记为稳定功能。
- 🔐 加密模块更新根证书至 NSS 3.119，并将 `crypto.hash` 标记为稳定。
- 👥 新增 Aviv Keller、Gürgün Dayıoğlu 和 Renegade334 三位项目协作者。
- 🌐 URL 模块更新 ada 解析器至 v3.4.2，支持 Unicode 17。
- ⚡ V8 引擎中将 `v8.queryObjects()` 方法标记为稳定。
- 🔄 多项依赖升级，包括 OpenSSL 至 3.5.5、npm 至 11.8.0、SQLite 至 3.51.2 等。
- 🛠️ 包含大量错误修复、性能优化、文档更新和测试改进。
- 🚨 修复了两个安全漏洞（CVE-2025-59465 和 CVE-2026-21637）。

---

### [sql.js](https://sql.js.org/)

**原文标题**: [sql.js](https://sql.js.org/)

本文介绍了人工智能在医疗领域的应用现状与前景，重点探讨了其在疾病诊断、治疗方案优化及医疗管理效率提升方面的作用，并简要提及了相关的伦理挑战。

- 🤖 AI 辅助诊断系统能通过分析医学影像快速识别病灶，提高早期疾病检出率
- 💊 基于机器学习的个性化治疗方案可整合患者数据，提升用药精准性与疗效
- 📊 智能医疗管理系统自动化处理病历与排程，显著减轻医护人员行政负担
- ⚖️ 数据隐私与算法透明度等伦理问题仍需在技术推广中同步完善规范

---

### [CodeMirror 实验 | 博客 | aziis98](https://aziis98.com/blog/codemirror-review-tool/)

**原文标题**: [Experiments with CodeMirror | Blog | aziis98](https://aziis98.com/blog/codemirror-review-tool/)

本文探讨了为复杂 Web 应用构建一个具备代码审查功能的文本编辑器，作者选择使用 CodeMirror 6 的合并扩展来实现这一目标。

- 🧑‍💻 作者在开发复杂 Web 应用时，需要一个支持语法高亮、多光标等功能的代码编辑器，而不仅仅是简单的文本域。
- ⚖️ 对比了 Monaco 和 CodeMirror 6，作者认为 Monaco 虽然功能强大但过于笨重且不易定制，而 CodeMirror 6 更模块化和可定制。
- 🔍 随着 LLM 的兴起，作者认为具备代码审查模式的编辑器越来越重要，允许用户查看并接受或拒绝文档的更改。
- 📝 文章详细介绍了 CodeMirror 6 的基本概念，包括状态、视图、扩展和 Facets，并解释了其函数式核心架构。
- 🛠️ 通过使用`@codemirror/merge`扩展，作者展示了如何构建一个统一的合并视图来显示文档差异。
- 🎯 实现了审查模式逻辑，包括通过用户事件监听接受/拒绝操作，并使用 Compartments 动态启用或禁用差异视图。
- 🔧 提供了一个完整的代码示例，展示了如何将审查模式集成到编辑器中，并支持通过查找替换工具触发审查。
- 🚀 作者展望了未来的实验方向，包括自定义装饰、Lezer 解析器集成以及 LSP 在浏览器中的 WASM 编译。

---

### [CodeMirror](https://codemirror.net/)

**原文标题**: [CodeMirror](https://codemirror.net/)

CodeMirror 是一款用于网页的代码编辑器组件，支持丰富的编辑功能与扩展接口，适用于多种编程语言，并具备良好的可访问性和跨平台兼容性。

- 🌐 **网页代码编辑器组件**：可在网站中实现支持多种编辑功能的文本输入字段。
- ♿ **无障碍支持**：兼容屏幕阅读器和纯键盘操作，提升可访问性。
- 📱 **移动端适配**：利用平台原生选择与编辑功能，优化手机端体验。
- 🔤 **双向文本**：支持从左到右和从右到左文字的混合排版。
- 🎨 **语法高亮**：根据语法结构进行颜色标记，提升代码可读性。
- 🔢 **行号显示**：在代码旁显示行号或其他信息的边栏。
- 💡 **自动补全**：提供基于语言的代码补全提示。
- 📂 **代码折叠**：可临时隐藏文档部分内容。
- 🔍 **搜索替换**：支持编辑器内搜索、正则表达式搜索及替换功能。
- 🌳 **完整解析**：生成详细语法树，支持多种语言集成。
- 🔌 **扩展接口**：提供稳健的 API 用于实现高级编辑器扩展。
- 🧩 **模块化设计**：多数功能基于通用公共 API 构建，便于定制。
- ⚡ **高效性能**：即使处理大型文档或长文本行也能保持响应速度。
- 🧱 **括号自动闭合**：输入时自动插入匹配的括号。
- ⚠️ **代码检查**：在编辑器中显示错误和警告信息。
- 🎭 **灵活样式**：支持混合字体样式、大小，并可在内容中添加小组件。
- 🎨 **主题定制**：可导入或创建自定义视觉编辑器样式。
- 👥 **协同编辑**：允许多用户同时编辑同一文档。
- ↩️ **撤销历史**：支持撤销与重做，兼容协同编辑。
- 🖱️ **多选区编辑**：可同时选择并编辑文档中的多个范围。
- 🌍 **国际化**：支持自定义显示或播报给用户的文本。
- 📜 **开源许可**：采用 MIT 许可，代码托管于 GitHub，欢迎贡献。
- 🌐 **浏览器兼容**：支持 Internet Explorer 11 及以上（需部分 polyfill）。
- 💬 **社区支持**：可通过论坛讨论、问题追踪器报告漏洞，并遵守行为准则。
- 📚 **语言支持**：提供多种语言的完整解析包，包括 JavaScript、Python、HTML 等，另有社区维护的语言包资源。
- 💖 **赞助支持**：由 Holmusk、Amplenote 等企业资助维护与开发。

---

### [如何在 Node.js 中发起 HTTP 请求](https://nodejsdesignpatterns.com/blog/nodejs-http-request/)

**原文标题**: [How to make an HTTP request in Node.js](https://nodejsdesignpatterns.com/blog/nodejs-http-request/)

本文全面介绍了在 Node.js 中进行 HTTP 请求的现代方法，重点推荐使用 Node.js 18+ 内置的 `fetch()` API。文章涵盖了从基础请求到高级场景（如流式传输、并发请求、错误重试、文件上传和测试模拟）的详细指南，并对比了 `fetch()` 与传统的 `http/https` 模块及外部库的适用场景。

- 🚀 **首选内置 fetch API**：Node.js 18+ 内置了 `fetch()` 函数，无需安装额外依赖即可进行 HTTP 请求，语法与浏览器端一致。
- ⚠️ **正确处理错误与超时**：`fetch()` 仅在网络错误时拒绝 Promise，需手动检查 `response.ok` 处理 HTTP 错误码；使用 `AbortSignal.timeout()` 设置超时，避免请求无限挂起。
- 📤 **支持多种请求与认证**：示例展示了如何进行 GET、POST（含 JSON 请求体）请求，以及如何通过请求头添加认证信息（如 Bearer Token）和内容协商（Accept 头）。
- 🌊 **流式传输大文件**：可通过流式处理请求体和响应体来高效处理大文件上传与下载，避免内存溢出，并支持 `multipart/form-data` 格式。
- 🔁 **实现请求重试与并发控制**：提供了自动重试失败请求的辅助函数（支持指数退避），并介绍了使用 `Promise.all` 进行并发请求及限制并发数的模式。
- 🔧 **安全构建 URL 与查询参数**：推荐使用 `URL` 和 `URLSearchParams` API 安全地构建带查询参数的 URL，避免手动拼接字符串的安全风险。
- 🧪 **使用 MockAgent 进行单元测试**：可通过安装 `undici` 包并使用其 `MockAgent` 来模拟 HTTP 请求，方便编写不依赖真实网络的单元测试。
- ⚡ **性能考量与替代方案**：虽然 `fetch()` 适用于大多数场景，但在超高吞吐量需求下，直接使用 `undici.request()` 或 `http/https` 模块可能获得更高性能。
- 📚 **总结与选择建议**：文章总结了不同方法（`fetch()`、`undici.request()`、`http/https` 模块）的适用场景和 Node.js 版本要求，并回答了关于是否需要 `axios` 等外部库的常见问题。

---

### [TimescaleDB：PostgreSQL 时序数据库 | 虎数 | 虎数](https://www.tigerdata.com/timescaledb?utm_source=cooperpress&utm_medium=referral&utm_campaign=javascript-weekly-newsletter)

**原文标题**: [TimescaleDB: PostgreSQL Time-Series DB | Tiger Data | Tiger Data](https://www.tigerdata.com/timescaledb?utm_source=cooperpress&utm_medium=referral&utm_campaign=javascript-weekly-newsletter)

TimescaleDB 是基于 PostgreSQL 构建的时序数据库，提供自动分区、行列混合存储、高达 95% 的压缩率、增量物化视图、自动化数据管理和专用时序函数等功能，适用于物联网、金融科技和实时分析等场景。其托管云服务 Tiger Cloud 提供数据分层、统一数据架构、弹性扩展和高可用性等优势，同时支持自托管部署。

- 🗂️ **自动分区**：通过超表实现按时间或 ID 自动分区，支持快速数据摄取和大规模查询优化。
- 💾 **行列混合存储**：结合行存储和列存储优势，在降低成本的同时提升分析查询性能。
- 📉 **高效压缩**：采用列式编码技术，压缩率高达 95%，支持在压缩数据上直接过滤和聚合。
- 🔄 **增量物化视图**：通过连续聚合实现增量刷新，支持实时数据更新和分层计算。
- 🤖 **自动化数据管理**：内置任务调度器，支持列存储、保留策略和聚合刷新的自动化配置。
- ⏱️ **专用时序函数**：提供约 200 种超函数，简化高级时序分析，支持统计汇总和时间加权计算。
- 🌐 **托管云服务优势**：Tiger Cloud 提供数据分层、统一架构、弹性扩展、高可用性和安全合规等生产级功能。
- 🏢 **自托管灵活性**：支持在任意 PostgreSQL 环境部署，包含核心功能但需自行管理高可用和扩展特性。

---

### [虚拟滚动处理数十亿行数据——HighTable 的技术方案](https://rednegra.net/blog/20260212-virtual-scroll/)

**原文标题**: [Virtual Scrolling for Billions of Rows — Techniques from HighTable](https://rednegra.net/blog/20260212-virtual-scroll/)

本文介绍了 React 组件 HighTable 中用于处理数十亿行数据垂直滚动的五种关键技术，这些技术结合了懒加载、表格切片、无限像素、像素级精确滚动和两步随机访问，以实现高性能和可访问性。

- 🚀 **懒加载技术**：仅加载当前可见的单元格数据，避免一次性加载全部数据，显著减少内存占用。
- ✂️ **表格切片技术**：只渲染可见的行，而非整个表格，大幅减少 HTML 元素数量，提升渲染性能。
- 🌌 **无限像素技术**：通过设置画布最大高度并降低滚动条分辨率，突破浏览器对元素高度的限制，支持海量行数。
- 🎯 **像素级精确滚动**：结合全局和局部滚动模式，允许用户通过滚动条快速跳转或通过鼠标滚轮精细浏览，确保每个像素都可访问。
- 🎮 **两步随机访问技术**：分离垂直和水平滚动逻辑，支持通过键盘或程序跳转到任意单元格，并保持流畅的导航体验。

---

### [GitHub - hyparam/hightable: 一个用于 React 的动态窗口化滚动表格组件](https://github.com/hyparam/hightable)

**原文标题**: [GitHub - hyparam/hightable: A dynamic windowed scrolling table component for react](https://github.com/hyparam/hightable)

HighTable 是一个用于 React 的虚拟化表格组件，旨在高效显示大型数据集，通过仅渲染可视区域内的行来实现流畅滚动和高性能。

- 📊 **虚拟化滚动**：仅渲染可见行，优化大型数据集的性能。
- 🔄 **异步数据加载**：支持滚动时按需获取数据，适用于任意大小的数据集。
- 🔍 **列排序**：提供可选的列数据排序功能。
- 📏 **列调整大小**：允许调整列宽以适应可用空间并支持自动调整。
- ✅ **行选择**：支持使用 Shift+ 点击进行多行选择。
- 🖱️ **事件处理**：支持单元格的双击事件。
- ⏳ **加载占位符**：每个单元格显示动画加载指示器。
- 📦 **易于集成**：通过 npm 安装，提供详细的 DataFrame 数据模型定义和丰富的配置属性。
- 🛠️ **实用工具**：包含将数组转换为 DataFrame 的辅助函数，以及用于 Node.js 环境的数据框工具。
- 🎨 **样式定制**：包含基础 CSS 样式，并支持通过 CSS 自定义外观。

---

### [JS 密集型方法与长期性能目标不兼容。](https://sgom.es/posts/2026-02-13-js-heavy-approaches-are-not-compatible-with-long-term-performance-goals/)

**原文标题**: [JS-heavy approaches are not compatible with long-term performance goals](https://sgom.es/posts/2026-02-13-js-heavy-approaches-are-not-compatible-with-long-term-performance-goals/)

本文基于作者在 Web 性能优化领域的实践经验，指出过度依赖 JavaScript（尤其是 React 等框架）的前端开发方式通常难以满足长期性能目标，并提倡更多采用服务端为中心的架构。

- 🚫 **JS 密集型方案与长期性能目标不兼容**：大量 JS 代码会增加加载与执行开销，导致应用启动慢且难以维持性能
- 📦 **依赖包成本高昂且易膨胀**：npm 包常引入冗余代码，且版本更新可能无声增加体积（如 moment 增长 10%、react-dom v18→v19 增加 33%）
- ⚠️ **框架易导致性能陷阱**：React 等框架常默认鼓励低效模式（如全局状态滥用、同步导入、缺乏代码分割），使优化比犯错更困难
- 🧩 **性能优化脆弱且难持久**：单一错误导入或低效组件即可破坏既有优化，依赖开发人员持续警惕的体系十分脆弱
- 🔍 **性能调试工具不完善**：React 等框架的自带工具与浏览器开发者工具割裂，增加调试复杂度，且缺乏关键信息（如聚合耗时视图）
- 🛡️ **缓解措施成本高昂**：需实施代码分割、包体积监控、性能测试等系列措施，但效果有限且维护负担重
- ⚖️ **React 生态的稳定性问题**：版本升级常导致大规模重写（如 Hooks、并发模式、测试库弃用），长期项目面临持续代码迭代压力
- 🌐 **性能影响用户体验与包容性**：未优化的 JS 应用会排除低端设备用户，造成操作延迟与数据流量浪费
- 🖥️ **服务端方案为更优替代**：将计算移至服务器可利用更强硬件、更易监控调试，且减少对用户设备资源的占用
- 🧱 **服务端架构的多样化实践**：包括全页面导航、Turbolinks 局部替换、HTMX 增强等，能以更少 JS 实现良好交互体验
- 🔄 **呼吁行业转变开发范式**：应停止盲目采用 JS 框架，根据实际需求评估服务端方案，将性能与用户体验纳入技术选型核心考量

---

### [TypeScript 泛型趣味探索 – Frontend Masters 博客](https://frontendmasters.com/blog/fun-with-typescript-generics/)

**原文标题**: [Fun with TypeScript Generics – Frontend Masters Blog](https://frontendmasters.com/blog/fun-with-typescript-generics/)

本文深入探讨了 TypeScript 泛型的高级应用，通过一个具体的案例——为 TanStack Start 中的查询函数实现类型安全的`refetchedQueryOptions`辅助函数，展示了如何结合泛型、条件类型和函数重载来解决复杂的类型问题。

- 🧩 **泛型基础**：泛型允许函数接受类型参数，增强代码的类型安全性和复用性，例如实现类型安全的数组过滤函数。
- 🔄 **条件类型**：通过条件类型可以基于类型关系动态生成新类型，例如判断类型是否为数组或提取函数参数类型。
- 🛠️ **实际案例**：文章以实现`refetchedQueryOptions`函数为例，逐步解决服务器函数参数与返回值的类型推断问题。
- ⚙️ **函数重载**：利用 TypeScript 的函数重载特性，根据服务器函数是否接受参数来定义不同的函数签名，确保类型正确。
- 🎯 **类型工具**：构建了`ServerFnArgs`、`ServerFnHasArgs`等辅助类型，结合泛型约束和条件类型实现精确的类型控制。
- 📚 **学习价值**：尽管案例较为小众，但涉及的泛型、条件类型和函数重载等技术在 TypeScript 高级开发中广泛应用。

---

### [构建坚不可摧的 React 组件 - 舒丁](https://shud.in/thoughts/build-bulletproof-react-components)

**原文标题**: [Building Bulletproof React Components - Shu Ding](https://shud.in/thoughts/build-bulletproof-react-components)

构建健壮的 React 组件需要超越常规场景，确保在服务器渲染、并发渲染、异步子组件等多种复杂环境下仍能稳定运行。关键在于使组件具备适应性，以应对未来可能出现的各种挑战。

- 🛡️ **服务器端渲染安全**：避免在服务器端直接调用浏览器 API（如 localStorage），应将其移至 useEffect 中执行，防止构建时崩溃。
- 💧 **水合过程安全**：通过内联脚本在浏览器绘制前同步设置初始状态，避免因客户端水合后状态更新导致的界面闪烁。
- 🔢 **多实例安全**：使用 useId 生成唯一标识符，确保同一组件多个实例间不会因 ID 冲突而相互干扰。
- ⚡ **并发渲染安全**：利用 React.cache 对服务器组件中的异步请求进行去重，避免同一请求在并发渲染中被重复执行。
- 🧩 **组合安全**：使用 Context 而非 cloneElement 传递数据，确保与服务器组件、懒加载等现代 React 特性兼容。
- 🪟 **门户安全**：通过 ownerDocument.defaultView 获取正确的窗口上下文，使全局事件监听在 iframe 或 portal 中也能正常工作。
- 🎭 **过渡动画安全**：使用 startTransition 包裹状态更新，确保在视图过渡中能够触发平滑的动画效果。
- 🎨 **活动状态安全**：通过动态修改 style 标签的 media 属性，控制全局样式在组件隐藏时不被意外应用。
- 🔒 **数据防泄漏安全**：使用 taintUniqueValue 标记敏感数据，防止其被意外序列化并发送到客户端。
- 🔮 **未来兼容安全**：优先使用 useState 而非 useMemo 来保证数据的语义化持久性，避免因 React 内部优化导致缓存失效。

---

### [SWR](https://swr.vercel.app/)

**原文标题**: [SWR](https://swr.vercel.app/)

SWR 是一个专为 React 设计的现代数据获取库，通过简洁的 API 提供缓存、重新验证和请求去重功能，帮助开发者构建快速、一致且实时更新的用户界面。

- 🚀 **快速数据获取**：通过 `useSWR` 钩子轻松获取数据，自动管理请求、缓存和响应状态
- 🔄 **智能重新验证**：支持焦点重连、网络恢复、轮询等多种方式保持数据新鲜
- 🛡️ **错误处理与重试**：内置智能错误重试机制，增强应用稳定性
- 💾 **本地状态管理**：支持乐观更新，提升用户体验
- 📱 **React 原生集成**：完美支持 Suspense、SSR/SSG，提供完整的 TypeScript 类型
- 🔌 **数据源无关**：兼容 REST、GraphQL 及自定义获取器，灵活适配各种后端
- 📊 **高级功能**：提供分页、滚动位置恢复、实时订阅等生产级功能
- ⚡ **轻量高效**：极简 API 设计，保持应用性能优异

---

### [Rolldown 工作原理：利用位集逻辑实现高性能代码分割 | Atriiy](https://www.atriiy.dev/blog/rolldown-high-performance-code-splitting)

**原文标题**: [How Rolldown Works: High-Performance Code Splitting with Bitset Logic | Atriiy](https://www.atriiy.dev/blog/rolldown-high-performance-code-splitting)

Rolldown 是一款高性能 JavaScript 打包工具，Vite 计划将其作为未来的默认打包器。其打包过程分为模块扫描、符号链接和最终代码生成三个阶段。本文重点解析代码生成阶段的核心分块算法，该算法通过位集逻辑高效处理模块可达性，并结合手动与自动分块策略，最终通过结构优化生成精简的打包输出。

- 🧩 **位集指纹记录模块可达性**：为每个入口点分配唯一比特位，通过广度优先搜索标记每个模块的可达入口，形成位集指纹，用于后续分块决策。
- 🛠️ **优先处理手动分块规则**：根据用户配置的匹配组（如正则表达式）优先将特定模块及其依赖树分配到指定分块，确保开发者意图优先于自动算法。
- 🤖 **基于位集的自动分块**：对剩余模块，根据其位集指纹将属于相同入口集合的模块自动分组到共享分块，利用位操作高效处理模块分配。
- 🔄 **结构优化减少冗余**：合并可安全嵌入的共享模块到现有分块，并移除因模块移出而变空的“门面”入口分块，减少文件数量和 HTTP 请求。
- 🌐 **后处理优化输出**：在分块级别合并相同的外部命名空间导入，排序模块和执行顺序，并对纯再导出链优化生成简洁的入口级外部模块导入。

---

### [获取失败](https://javascriptweekly.com/link/180809/web)

**原文标题**: [Failed to retrieve](https://javascriptweekly.com/link/180809/web)

无法总结：获取内容失败，状态码 403。

---

### [Electrobun v1 - 黑板博客](https://blackboard.sh/blog/electrobun-v1/)

**原文标题**: [Electrobun v1 - Blackboard Blog](https://blackboard.sh/blog/electrobun-v1/)

Electrobun v1 是一个使用 TypeScript 构建超快速、轻量且跨平台桌面应用的框架，由开发者 Yoav 历时两年打造，现已稳定发布，支持 macOS、Windows 和 Ubuntu 平台，提供完整的开发工具链和自动更新功能。

- 🚀 开发动机：源于作者早期使用 Visual Basic 6 和 Adobe AIR 的桌面应用开发经验，以及对现代 Electron 等框架开发体验的不满，促使他创建更高效的替代方案。
- 🔧 技术演进：最初仅支持 macOS，后扩展至跨平台，利用 Zig、C++ 等技术优化，并集成 Bun 提升性能，支持自动安装包生成和差分更新。
- 🌐 核心功能：提供跨平台窗口控制、菜单、快捷键、Webview 分区等完整功能，特别是改进的 `<electrobun-webview>` 解决了 Electron 中 Webview 的遗留问题。
- 📈 应用现状：已成功用于重写 co(lab) 项目，框架稳定，社区活跃，支持开发者构建复杂桌面应用，未来将持续发展。

---

### [使用 JavaScript、HTML 和 CSS 构建轻量级跨平台桌面应用 | Neutralinojs](https://neutralino.js.org/)

**原文标题**: [Build lightweight cross-platform desktop apps with JavaScript, HTML, and CSS | Neutralinojs](https://neutralino.js.org/)

Neutralinojs 是一个轻量级的跨平台应用开发框架，它通过 JavaScript API 提供操作系统级别的功能访问，无需额外依赖即可在多种平台上运行。

- 🛠️ 提供原生 API，支持文件操作、命令执行和原生对话框等系统级功能
- 📦 零依赖且便携，无需编译器即可跨平台开发应用
- 🌍 支持 Linux、Windows、macOS、Web 和 Chrome 等多平台运行
- ⚡ 应用体积小，未压缩约 2MB，压缩后约 0.5MB，资源占用低
- 🔧 提供简单灵活的开发接口，包含便携式自动更新器和 CLI 工具
- 🔌 兼容任意前后端框架，支持热模块替换和进程间通信扩展

---

### [Bun — 一个快速的全能 JavaScript 运行时](https://bun.sh/)

**原文标题**: [Bun — A fast all-in-one JavaScript runtime](https://bun.sh/)

Bun v1.3.9 是一个快速、可逐步采用的 JavaScript 全栈工具包，包含运行时、打包器、测试运行器和包管理器，并强调与 Node.js 的完全兼容性。

- 🚀 Bun 是一个快速的 JavaScript 全栈工具包，支持 TypeScript 和 JSX
- 🔧 可单独使用工具（如 bun test 或 bun install）或整体采用
- 🎯 旨在实现 100% Node.js 兼容性
- 📦 在打包 10,000 个 React 组件时，速度超过 Rolldown、esbuild 等工具
- 🌐 Express.js 性能测试中，每秒处理请求数显著高于 Deno 和 Node.js
- ⚡ WebSocket 服务器消息发送速率远超 Deno 和 Node.js
- 🗃️ 大数据表查询性能优于 Node.js 和 Deno

---

### [Electrobun 文档 - 构建超快速、轻量级、跨平台的桌面应用](https://blackboard.sh/electrobun/docs/)

**原文标题**: [Electrobun Documentation - Build ultra fast, tiny, cross-platform desktop apps](https://blackboard.sh/electrobun/docs/)

Electrobun 是一个基于 TypeScript 的超快、超小、跨平台桌面应用开发框架，结合原生绑定与 Bun 运行时，提供极致的性能和原生体验。

- 🚀 极速轻量：应用启动时间低于 50ms，打包大小仅 14MB，更新包仅 14KB
- 🔧 技术架构：使用 C++、ObjC 和 Zig 编写原生绑定，以 Bun 作为后端运行时和打包工具
- 🌐 渲染引擎：默认采用系统原生 Webview 渲染，可选 CEF（Chromium Embedded Framework）
- 📦 更新机制：基于 bsdiff 的自定义差分更新系统，大幅减少更新包体积
- 💻 跨平台支持：全面兼容 macOS、Windows 和 Linux 操作系统
- 🛠️ 开发体验：提供完整的 API 体系，包括窗口管理、系统托盘、上下文菜单、应用菜单等原生功能
- 📚 学习资源：包含快速入门指南、架构解析、打包分发教程和高级开发指南
- 🤝 社区支持：拥有活跃的 GitHub 仓库和 Discord 社区，助力开发者快速上手

---

### [GitHub - blackboardsh/electrobun：使用TypeScript构建超快速、小巧且跨平台的桌面应用程序。](https://github.com/blackboardsh/electrobun)

**原文标题**: [GitHub - blackboardsh/electrobun: Build ultra fast, tiny, and cross-platform desktop apps with Typescript.](https://github.com/blackboardsh/electrobun)

Electrobun 是一个用于构建超快速、轻量且跨平台桌面应用的 TypeScript 框架，它集成了 bun 运行时和 zig 原生绑定，提供从开发到分发的完整解决方案。

- 🚀 使用 TypeScript 开发主进程和 Webview，无需额外配置
- 🔗 通过类型化 RPC 实现主进程与 Webview 进程间的快速通信
- 📦 应用体积极小（约 12MB），支持增量更新（最小 14KB）
- 🛠️ 提供一体化工作流，快速开始开发与分发
- 🌍 官方支持 macOS 14+、Windows 11+ 和 Ubuntu 22.04+
- 📖 包含详细文档、模板和社区资源（Discord、GitHub）
- 🔧 开发环境设置简单，支持从源码构建和调试

---

### [音频 TTS - 使用克隆声音生成音频的 Electrobun 应用 - YouTube](https://www.youtube.com/watch?v=Z4dNK1d6l6E)

**原文标题**: [Audio TTS - Electrobun App that generates Audio with your cloned voice. - YouTube](https://www.youtube.com/watch?v=Z4dNK1d6l6E)

该内容为 YouTube 网站底部的通用导航链接列表，展示了平台的主要信息与功能入口。

- 🏠 **平台信息** - 包含版权声明、联系方式和运营公司信息
- 📜 **规则与安全** - 列出使用条款、隐私政策及平台安全相关指南
- 🛠️ **功能与服务** - 提供创作者支持、广告投放和开发者资源入口
- 🔍 **探索与更新** - 设有平台运作说明和新功能测试通道

---

### [代码旁实时显示控制台日志输出](https://console-ninja.com/?utm_source=cooperpress&utm_medium=javascriptweekly&utm_content=javascriptweekly)

**原文标题**: [Console log output right next to your code](https://console-ninja.com/?utm_source=cooperpress&utm_medium=javascriptweekly&utm_content=javascriptweekly)

本文介绍了人工智能在医疗领域的应用现状与前景，重点探讨了其在疾病诊断、治疗方案优化及医疗管理效率提升方面的作用，同时简要提及了相关的技术挑战和伦理考量。

- 🤖 AI 辅助诊断系统通过分析医学影像提升疾病检测准确率
- 💊 机器学习算法帮助个性化制定治疗方案，改善患者预后
- ⚡ 智能管理系统优化医院工作流程，减少行政负担
- 🧠 自然语言处理技术加速医疗文献分析与临床决策支持
- 🛡️ 数据隐私保护与算法透明度成为应用推广的关键挑战
- 🌐 远程医疗与可穿戴设备结合实现持续健康监测

---

### [GitHub - thisiskps/fetch-network-simulator: 获取网络模拟器](https://github.com/thisiskps/fetch-network-simulator)

**原文标题**: [GitHub - thisiskps/fetch-network-simulator: fetch-network-simulator](https://github.com/thisiskps/fetch-network-simulator)

fetch-network-simulator 是一个用于前端开发的网络行为模拟工具，它通过拦截全局 fetch 函数，在浏览器中模拟真实世界的不稳定网络条件，帮助开发者在开发阶段测试应用在不良网络环境下的表现。

- 🌐 **拦截全局 fetch** – 在 JavaScript 层模拟 HTTP 请求/响应行为，不模拟底层网络协议。
- 🧪 **模拟多种网络状况** – 包括延迟、丢包、自动重试、响应乱序、并发限制和带宽限制。
- 🛠️ **提升 UI 韧性测试** – 帮助暴露在理想网络中难以发现的 UI 缺陷和竞态条件。
- 📦 **易于集成** – 通过 npm 安装，需在应用入口点初始化，支持开发环境按需启用。
- 🔍 **内置调试模式** – 提供结构化的请求生命周期日志，便于观察规则应用和请求流程。
- 🧩 **可扩展规则引擎** – 采用确定性规则执行管道，支持开发者自定义规则。
- 🚧 **持续开发中** – 计划支持请求取消模拟、响应乱序等更多特性，并提供可视化控制界面。

---

### [Peek - 智能标题演示](https://adesignl.github.io/Peek/)

**原文标题**: [Peek - Smart Header Demo](https://adesignl.github.io/Peek/)

Peek 是一个轻量级 JavaScript 库，用于实现智能的页面头部行为：向下滚动时隐藏，向上滚动时显示，以优化屏幕空间使用。

- 🪶 **轻量无依赖**：纯 JavaScript 实现，体积小巧，无额外依赖。
- 🎯 **智能滚动检测**：通过容差设置区分有意滚动和微小移动，避免误触。
- ⚡ **高性能流畅**：采用 requestAnimationFrame 和被动事件监听器，确保滚动顺滑。
- 🎨 **高度可定制**：支持自定义偏移量、容差及 CSS 类，轻松适配设计需求。
- 📱 **适用场景广泛**：特别适合移动网站、内容平台、电商页面和落地页，提升用户体验。
- 🚀 **快速集成**：只需简单添加 HTML 结构、CSS 样式并初始化 JavaScript 即可使用。
- 🔓 **开源免费**：代码托管于 GitHub，支持下载、贡献和问题反馈。

---

### [GitHub - adesignl/Peek：轻量级“头部空间风格”滚动意图库，向下滚动时隐藏网站头部，向上滚动时显示](https://github.com/adesignl/Peek)

**原文标题**: [GitHub - adesignl/Peek: Light Weight "Headroom Style" scroll intent library that hides the site header on scroll down and shows on scroll up](https://github.com/adesignl/Peek)

Peek 是一个轻量级的 JavaScript 库，用于实现智能的滚动意图检测，能够在用户向下滚动时隐藏网站头部，向上滚动时显示，从而提升浏览体验。

- 🚀 **轻量高效**：无依赖，体积小巧，采用现代 JavaScript 实践优化性能。
- 🧠 **智能滚动检测**：通过算法区分有意滚动与微小移动，避免抖动。
- ⚙️ **易于集成与定制**：支持自定义滚动阈值、延迟和 CSS 类，适配各类网站和框架。
- 📄 **丰富的文档与示例**：提供详细配置选项、API 方法和多种使用案例。
- 🔧 **良好的浏览器兼容性**：支持所有现代浏览器，并采用被动事件监听器提升滚动性能。

---

### [rari：基于 Rust 运行时的 React 服务器组件](https://rari.build/)

**原文标题**: [rari: React Server Components on a Rust Runtime](https://rari.build/)

本文介绍了人工智能在医疗领域的应用现状与前景，重点探讨了其在疾病诊断、治疗方案优化及医疗管理效率提升方面的作用，并简要提及了相关的伦理挑战。

- 🏥 AI 辅助诊断系统能通过分析医学影像快速识别病灶，提升早期疾病检出率
- 💊 基于机器学习的个性化治疗方案可结合患者数据优化用药与治疗路径
- 📊 智能医疗管理平台能自动化处理病历、预约及药物配送，减轻医护负担
- ⚖️ 数据隐私与算法透明度等伦理问题仍需在技术发展中同步完善规范

---

### [入门指南 / rari 文档](https://rari.build/docs/getting-started)

**原文标题**: [Getting Started / rari Docs](https://rari.build/docs/getting-started)

本文介绍了人工智能在医疗领域的应用现状与前景，重点探讨了其在疾病诊断、药物研发和个性化治疗方面的突破性进展，同时简要提及了相关的伦理挑战。

- 🤖 AI 辅助诊断系统能通过分析医学影像快速识别病灶，提升早期癌症等疾病的检出率
- 🔬 机器学习加速了新药研发流程，大幅缩短化合物筛选与临床试验设计周期
- 🧬 基于患者基因组数据的 AI 模型可为慢性病和肿瘤提供个性化治疗方案
- ⚖️ 医疗 AI 面临数据隐私、算法透明度及责任认定等伦理监管问题

---

### [Broad Infinite List by suhaotian - 适用于 React、Vue 3 和 React Native 的双向无限列表](https://suhaotian.github.io/broad-infinite-list/)

**原文标题**: [Broad Infinite List by suhaotian  - The bidirectional infinite list for React, Vue 3 and React Native](https://suhaotian.github.io/broad-infinite-list/)

该内容展示了一个项目频道中的实时消息记录，主要围绕服务器状态检查和最新部署的确认请求。

- 🔄 频道成员反复请求检查最新部署情况
- 🖥️ 多次重复进行服务器状态检查
- ⏰ 所有消息均在同一时间（12:15）发送
- 📊 消息记录从#9950 持续到#9999，显示高频沟通
- 👥 表明团队正在密切关注系统运行状态

---

### [GitHub - perspective-dev/perspective：一款数据可视化与分析组件，尤其适用于大规模及/或流式数据集。](https://github.com/perspective-dev/perspective)

**原文标题**: [GitHub - perspective-dev/perspective: A data visualization and analytics component, especially well-suited for large and/or streaming datasets.](https://github.com/perspective-dev/perspective)

Perspective 是一个用于大规模和/或流式数据集的交互式分析与数据可视化组件，支持 WebAssembly、Python 和 Rust 高性能查询引擎，可构建可配置的报告、仪表板、笔记本和应用程序。

- 📊 提供框架无关的 UI 自定义元素，支持浏览器内（通过 WebAssembly）或远程（通过 WebSocket）连接数据模型，包含数据网格和 10 多种图表类型
- 🔌 具备可插拔引擎的数据模型 API，可将视图配置转换为原生查询，支持连接外部数据源如 DuckDB
- ⚡ 内置基于 C++ 开发的快速、内存高效的流式数据模型，支持 WebAssembly、Python 和 Rust，并兼容 Apache Arrow 读写/流式处理
- 📓 集成 JupyterLab 小部件和 Python 客户端库，支持在笔记本中进行交互式数据分析
- 🌐 提供全面的多语言 API 支持，包括 JavaScript（浏览器/Node.js）、Python 和 Rust，并附带丰富示例项目
- 🏢 项目隶属于 OpenJS 基金会，采用 Apache-2.0 开源协议，拥有活跃的社区贡献和版本发布

---

### [支持 React、Vue、Angular 及原生 TypeScript 的零依赖布局管理器 | Dockview](https://dockview.dev/)

**原文标题**: [A zero dependency layout manager supporting React, Vue, Angular, and vanilla TypeScript | Dockview](https://dockview.dev/)

功能齐全的布局管理器，提供无依赖的布局管理和停靠控件，支持序列化布局和自定义主题，可选择多种控件类型，具备丰富的功能控制、浮动和弹出组、拖放操作，代码质量高且支持 React 或原生 TypeScript。

- 🚀 无依赖布局管理，提供完整的停靠控件解决方案
- 💾 支持序列化布局，可通过 API 或序列化方法添加/移除面板
- 🎨 可自定义主题，通过 CSS 属性或特定类实现简单或深度定制
- 🛠️ 提供多种控件选择：分屏视图、网格视图、可折叠面板或完整停靠方案
- ⚙️ 丰富的功能控制，支持自定义标题图标和标签页渲染
- 🌐 内置浮动组和弹出窗口组，提供编程控制 API
- 🖱️ 支持拖放操作，可调整布局并与外部拖放事件交互
- 📦 零依赖，代码简洁高效
- 🔍 代码质量透明，通过 Sonarcloud 分析，高测试覆盖率，源码可查
- ⚛️ 支持 ReactJS 组件和原生 TypeScript

---

### [GitHub - nmrugg/stockfish.js：适用于网页浏览器的Stockfish国际象棋引擎](https://github.com/nmrugg/stockfish.js)

**原文标题**: [GitHub - nmrugg/stockfish.js: The Stockfish chess engine for web browsers](https://github.com/nmrugg/stockfish.js)

Stockfish.js 是 Stockfish 国际象棋引擎的 WebAssembly 实现，专为浏览器环境设计，提供多种版本以适应不同性能与兼容性需求。

- 🚀 **多线程引擎**：最强版本，需浏览器支持 CORS 头部，文件较大（>100MB）。
- 🔧 **单线程引擎**：无需 CORS 支持，但无法使用多线程，适用于无 CORS 环境。
- 📱 **精简多线程引擎**：体积小（约 7MB），性能稍弱，推荐用于支持 CORS 的移动浏览器。
- 📲 **精简单线程引擎**：体积小且无需 CORS，适用于移动浏览器。
- ⚙️ **ASM-JS 引擎**：兼容所有 JavaScript 浏览器，性能较弱，仅作为备选方案。
- 🌐 **兼容性**：WASM 版本支持现代浏览器及 Node.js，ASM-JS 版本几乎全平台兼容。
- 📦 **安装与使用**：可通过 npm 安装，支持浏览器 Web Workers 及 Node.js 命令行或模块调用。
- 🛠️ **编译与开发**：需安装 emscripten 3.1.7，使用 build.js 脚本编译，提供示例代码供参考。
- 👏 **致谢与许可**：感谢 Chess.com 等赞助方，项目基于 GPLv3 开源协议发布。

---

### [GitHub - ohmjs/ohm：一个用于构建解析器、解释器、编译器等的库与语言。](https://github.com/ohmjs/ohm)

**原文标题**: [GitHub - ohmjs/ohm: A library and language for building parsers, interpreters, compilers, etc.](https://github.com/ohmjs/ohm)

Ohm 是一个用于构建解析器、解释器和编译器的工具包，包含库和领域特定语言，基于解析表达式语法（PEG），支持左递归规则和面向对象的语法扩展。

- 🧩 **核心功能**：提供库和语言来构建解析器、解释器、编译器，基于解析表达式语法（PEG）。
- 🔗 **技术特性**：完全支持左递归规则，允许自然定义左结合运算符；支持面向对象的语法扩展。
- 🧠 **设计优势**：语义动作模块化，实现语法与语义分离，提升可读性和可扩展性。
- 🛠️ **开发工具**：提供在线编辑器和可视化工具，支持即时反馈和交互式解析过程可视化。
- 🌐 **应用案例**：已用于 Seymour 课堂编程环境、Shadama 粒子模拟语言、turtle.audio 音乐生成工具等。
- 🚀 **入门方式**：可通过在线编辑器体验，或通过 npm、yarn 等安装库，支持浏览器和 Node.js 环境。
- 📚 **学习资源**：包含教程、示例和文档，社区支持通过 Discord、GitHub 讨论区和邮件列表提供。
- 🐛 **调试支持**：提供文本追踪和图形可视化工具，帮助调试语法。
- 🤝 **开源贡献**：鼓励贡献，提供贡献指南和文档，项目采用 MIT 许可证。

---

### [JSNation——2026 年主要 JavaScript 大会](https://jsnation.com/?utm_source=partner&utm_medium=jsweekly)

**原文标题**: [JSNation – the main JavaScript conference of 2026](https://jsnation.com/?utm_source=partner&utm_medium=jsweekly)

JSNation 是一个为期两天的 JavaScript 全栈技术大会，将于 2026 年 6 月 11 日（阿姆斯特丹线下 + 线上）和 6 月 15 日（线上）举行。大会汇聚了 50 多位演讲者，预计有 1500 名现场参与者和 1 万名线上参与者，旨在探讨 Web 开发的最新趋势、分享前沿技术，并连接全球 JavaScript 开发者社区。

- 🗓️ **活动时间与形式**：2026 年 6 月 11 日（阿姆斯特丹线下 + 线上）和 6 月 15 日（线上）。
- 🎤 **演讲者与规模**：超过 50 位演讲者，预计 1500 名现场参与者和 1 万名线上参与者。
- 🚀 **核心主题**：聚焦全栈工程、AI 辅助编程、AI 工程、向高级工程师/技术主管成长等深度专题。
- 🌐 **活动亮点**：包含主题演讲、研讨会、城市导览、全球最大的 JS 派对、开源奖项和丰富的社交机会。
- 🎟️ **票务选项**：提供线下 + 线上混合票、纯线上票以及与 React Summit 的联票等多种选择，并有团队折扣和奖学金计划。
- 🏆 **社区贡献**：设立 JS 开源奖项，表彰有影响力的开源项目，并为技术领域的弱势群体提供 100 个奖学金名额。

---

### [STRICH | 适用于网页应用的条形码扫描](https://strich.io/?ref=js-weekly)

**原文标题**: [STRICH | Barcode Scanning for Web Apps](https://strich.io/?ref=js-weekly)

STRICH 是一个用于网页应用的 JavaScript 条码扫描库，支持实时 1D/2D 条码识别，无需原生应用或后端支持。

- 📦 通过 npm 安装，提供 30 天免费试用，采用透明定价模式，无设备限制
- 🛠️ 专为开发者设计，零依赖，兼容主流框架，提供详细文档和 TypeScript 支持
- 📱 支持多种 1D 和 2D 条码类型，内置扫描 UI 和弹窗扫描器，可处理复杂条码（如褪色、低光、反色）
- 🌐 基于现代 Web 技术（WebAssembly、WebGL），跨浏览器和设备兼容，支持离线操作
- 💼 提供企业级功能，包括白标定制、安全合规、GS1 认证，以及基础版到企业级的灵活定价
- ⭐ 获多家客户好评，强调易集成、高精度、可靠支持和成本效益

---

### [DPaint JS](https://dpaint.app/)

**原文标题**: [DPaint JS](https://dpaint.app/)

本文介绍了人工智能在医疗领域的应用现状与前景，重点探讨了其在疾病诊断、治疗方案优化及医疗管理效率提升方面的作用，并简要提及了相关的伦理挑战。

- 🏥 AI 辅助诊断系统能通过分析医学影像快速识别病灶，提升早期疾病检出率
- 💊 基于机器学习的个性化治疗方案可结合患者数据优化用药与治疗路径
- 📊 智能医疗管理平台能自动化处理病历、预约及药物配送，减轻医护负担
- ⚖️ 数据隐私与算法透明度等伦理问题仍需在技术发展中同步完善规范

---

### [未找到标题](https://dpaint.app/docs/#history)

**原文标题**: [No title found](https://dpaint.app/docs/#history)

DPaint.js 是一款基于浏览器的像素艺术编辑器，提供丰富的绘图工具和功能，适合创建复古风格的图形。

- 🎨 提供多种绘图工具，包括画笔、填充和形状工具
- 🖼️ 支持图层和蒙版功能，便于复杂图形编辑
- 🌈 包含颜色循环功能，用于创建动态像素艺术效果
- 💾 支持特定文件格式，方便保存和分享作品
- ⌨️ 提供键盘快捷键，提升操作效率
- 🔗 可通过 URL 参数自定义编辑器设置
- ❓ 设有常见问题解答部分，帮助用户解决问题
- 📜 包含历史记录和许可证信息，确保透明使用
- 📞 提供联系方式，便于用户反馈和获取支持

---

### [almostnode — 浏览器中的 Node.js](https://almostnode.dev/)

**原文标题**: [almostnode — Node.js in your browser](https://almostnode.dev/)

Next.js 应用路由器通过文件系统路由在浏览器中完全客户端运行，无需服务器即可实现动态路由和页面渲染。

- 🗂️ 文件系统路由：基于文件结构自动生成路由，简化配置
- 🌐 纯客户端运行：应用完全在浏览器中执行，无需后端服务器支持
- ⚡ 动态渲染：支持客户端动态路由和页面渲染，提升交互体验
- 📁 应用路由器：使用 App Router 架构组织页面和布局，提高开发效率

---

### [CSS 选择器 - 2026 年版 - 项目华莱士](https://www.projectwallace.com/the-css-selection/2026)

**原文标题**: [The CSS Selection - 2026 Edition - Project Wallace](https://www.projectwallace.com/the-css-selection/2026)

本文基于对超过 10 万个网站 CSS 使用情况的分析，总结了 2026 年 CSS 在实际应用中的状态，涵盖了从文件大小、代码行数到具体特性采用率的多个维度。

- 📊 **CSS 文件大小**：中位数网站 CSS 文件大小为 309 kB，最大达 52.5 MB，但多数网站通过压缩控制传输体积。
- 📏 **代码行数与复杂度**：中位数网站的 CSS 源代码行数约 10,677 行，复杂度中位数为 33,188，显示大多数网站 CSS 规模可控。
- 🖼️ **嵌入内容与注释**：约半数网站嵌入少量内容（中位数 2.23 kB），注释内容普遍较少，但存在个别极端案例。
- 🎛️ **At 规则使用**：`@media`（93%）、`@font-face`（86%）和`@keyframes`（84%）采用率最高，而`@supports`（45%）和`@layer`（2.7%）等较新特性采用率较低。
- 🎨 **选择器与伪类**：`:hover`、`:where`和`:focus`是最常用的伪类，`:has`的采用率已达 41%，显示新选择器快速普及。
- ⚠️ **!important 与自定义属性**：中位数网站使用 154 条`!important`声明，自定义属性在约半数网站中得到应用，但采用深度不一。
- 🛠️ **浏览器兼容与前缀**：仍有一定比例的网站使用属性浏览器 hack（如`*property`占 18.75%）和供应商前缀，但前缀属性占比普遍较低。
- 🎨 **颜色与字体**：十六进制颜色格式最常用，OKLCH 等新格式采用率仍低；中位数网站使用约 12 种独特字体家族和 47 种独特字体大小。
- 📐 **单位使用**：`px`、`em`和`s`是最常用的 CSS 单位，视口和容器单位开始被采用但占比不高。
- 🔍 **分析局限与展望**：当前分析在值比较和关联性上存在局限，未来计划使用无头浏览器等方法进行更深入和动态的分析。

---

### [Three.js 地震模拟](https://mrdoob.github.io/three-quake/)

**原文标题**: [Three.js Quake](https://mrdoob.github.io/three-quake/)

本文介绍了人工智能在医疗领域的应用现状与前景，重点探讨了其在疾病诊断、药物研发和个性化治疗方面的突破性进展，同时简要提及了相关的伦理挑战。

- 🤖 AI 辅助诊断系统能通过分析医学影像快速识别病灶，提升早期癌症等疾病的检出率
- 🔬 机器学习加速了新药研发流程，大幅缩短化合物筛选与临床试验设计周期
- 🧬 基于患者基因组数据的 AI 模型可为慢性病和肿瘤提供个性化治疗方案
- ⚖️ 医疗 AI 面临数据隐私、算法透明度及责任认定等伦理监管问题

---

### [Three.js 下降](https://mrdoob.github.io/three-descent/)

**原文标题**: [Three.js Descent](https://mrdoob.github.io/three-descent/)

本文介绍了人工智能在医疗领域的应用现状与前景，重点探讨了其在疾病诊断、治疗方案优化及医疗管理效率提升方面的作用，同时简要提及了相关的技术挑战和伦理考量。

- 🤖 AI 辅助诊断系统能通过分析医学影像快速识别病灶，提高早期疾病检出率
- 💊 基于机器学习的个性化治疗方案可结合患者数据优化用药与治疗路径
- ⚡ 智能医疗管理平台自动化处理行政流程，显著减轻医护人员行政负担
- 🧬 基因组学与 AI 结合助力精准医疗发展，实现遗传病风险预测
- 🛡️ 数据隐私保护与算法透明度是目前医疗 AI 面临的主要伦理挑战
- 🌐 远程医疗与可穿戴设备集成正推动慢性病智能监测体系的建立

---

### [GitHub - mrdoob/three-descent: 将《Descent》移植至 Three.js 的工作进行中版本。](https://github.com/mrdoob/three-descent)

**原文标题**: [GitHub - mrdoob/three-descent: A WIP port of Descent to Three.js.](https://github.com/mrdoob/three-descent)

这是一个使用 Three.js 对经典游戏《Descent》进行移植的未完成项目，允许在浏览器中体验该游戏。

- 🎮 **项目性质**：基于 Three.js 对《Descent》游戏的非官方移植，目前仍在开发中
- 🌐 **在线体验**：可通过特定网址直接在线游玩演示版本
- 📁 **资源包含**：项目内已包含共享版（第一章节）的游戏资源文件
- 🔄 **完整游戏**：如需体验完整内容，需自行替换为正版游戏文件
- ⚖️ **许可协议**：项目代码采用 MIT 开源许可证
- 👥 **开发贡献**：由 mrdoob 主导移植，并获得了 Claude 的协助
- ⭐ **社区关注**：在 GitHub 上获得 63 个星标和 3 个分支，显示出一定的开发者兴趣

---

### [用小型集群构建 SQLite | Kian Kyars](https://kiankyars.github.io/machine_learning/2026/02/12/sqlite.html)

**原文标题**: [building sqlite with a small swarm | Kian Kyars](https://kiankyars.github.io/machine_learning/2026/02/12/sqlite.html)

该实验利用 Claude、Codex 和 Gemini 三种 AI 代理协作，在 Rust 中构建了一个模拟 SQLite 架构的数据库引擎。项目通过严格的协调机制（如 Git、锁文件和测试）实现并行开发，最终产出约 1.9 万行代码，支持 SQL 子集并通过 64 项基础查询测试，但存在未优化代码和并发缺失等问题，核心目标是探索多智能体协同的工程方法。

- 🧠 实验通过 Claude、Codex、Gemini 三种 AI 代理并行开发，在 Rust 中构建了模拟 SQLite 架构的数据库引擎
- 📊 项目产出约 1.9 万行代码，支持 SQL 子集并通过 64 项基础查询测试，但未通过完整 SQLite 测试套件
- 🔧 采用分布式系统思维协调开发，通过 Git、锁文件、测试和模块化设计管理多代理协作
- ⚠️ 代码存在性能问题（如线性扫描空闲列表、缓冲区冗余克隆）且缺乏并发支持
- 📈 实验发现严格任务边界、共享状态文档和快速测试反馈是提升多代理效率的关键因素
- 🔄 项目尝试使用"合并代理"消除代码重复，但因执行中断未能在开发过程中实际应用
- 📉 54.5% 的提交为协调操作（如锁管理），凸显多代理并行开发的协调开销
- 🔮 未来需改进使用量监控、代理贡献度追踪和错误处理机制

---

### [为智能体引入 Markdown](https://blog.cloudflare.com/markdown-for-agents/)

**原文标题**: [Introducing Markdown for Agents](https://blog.cloudflare.com/markdown-for-agents/)

随着在线内容发现方式从传统搜索引擎转向需要结构化数据的 AI 代理，Cloudflare 推出“Markdown for Agents”功能，使网站能自动将 HTML 实时转换为 Markdown 格式，以优化 AI 处理效率并降低计算成本。

- 📈 **在线流量来源转变**：AI 爬虫和代理正取代传统搜索引擎，成为主要流量来源，需要为它们提供结构化数据。
- 📝 **Markdown 的高效性**：相比 HTML，Markdown 能减少约 80% 的令牌使用量，成为 AI 处理的理想格式。
- 🔄 **实时自动转换**：Cloudflare 网络支持通过内容协商头，在请求时自动将 HTML 转换为 Markdown，简化 AI 流程。
- 🛠️ **多种使用方式**：支持通过 cURL、Workers 等工具请求 Markdown 内容，并提供令牌数估计等实用信息。
- 🚦 **内容信号策略**：转换后的响应包含内容使用策略标头，明确允许 AI 训练、搜索和输入等用途。
- 📊 **流量追踪与分析**：Cloudflare Radar 新增内容类型洞察功能，可追踪 AI 代理消费 Markdown 内容的情况。
- 🆓 **免费 Beta 开放**：该功能已在 Pro、Business 和 Enterprise 计划中免费提供，可通过仪表板快速启用。

---

