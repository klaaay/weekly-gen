### [JavaScript 周刊第 790 期：2026 年 6 月 16 日](https://javascriptweekly.com/issues/790)

**原文标题**: [JavaScript Weekly Issue 790: June 16, 2026](https://javascriptweekly.com/issues/790)

以下是您提供的 JavaScript Weekly 第 790 期内容的摘要：

JavaScript Weekly 第 790 期涵盖了 Flow 与 TypeScript 的差异、npm v12 的安装脚本变更、代码复杂性讨论，以及多项工具和库的更新。

- 📰 **Flow 与 TypeScript 的差异**：Flow 的默认设置更严格，拒绝 TypeScript 严格模式下接受的易崩溃模式，并增加了穷尽匹配表达式等特性。
- 🛑 **npm v12 默认停止运行安装脚本**：即将发布的 npm v12 将不再默认执行 `preinstall`/`install`/`postinstall` 脚本，除非用户明确允许。
- 🤖 **代码便宜，理解昂贵**：htmx 作者指出，虽然代码生成变得容易，但理解代码仍很昂贵，复杂性是主要敌人。
- ⚡ **TanStack 大幅减少类型检查工作**：通过使用 `tsc` 诊断，TanStack Table v9 将 TypeScript 类型检查工作量减少了 62-86%。
- 🛠️ **工具和库更新**：包括 Playwright 1.61、ESLint v10.5.0、TanStack AI Beta、eslint-plugin-unicorn 67.0、zod-compiler、billboard.js 4.0、Tabulator 6.5、React Native 0.86、Biome 2.5 等。
- 📖 **文章与视频**：涵盖 React 库与工具指南、Kindle 主页修改、numpy-ts 性能优化、HTML 优先站点案例、Astro 博客构建等。
- 🚀 **其他生态系统动态**：包括 MapKit JS 6 发布、LinkedIn 虚假招聘骗局警告、WASI 0.3 发布、以及通过 WebUSB 驱动老旧扫描仪的趣味项目。

---

### [2026 年 TypeScript 用户的 Flow：Flow 与 TypeScript 对比 | Flow](https://medium.com/flow-type/flow-for-typescript-users-in-2026-ad07ac0a2d92)

**原文标题**: [Flow for TypeScript users in 2026: Flow vs TypeScript comparison | Flow](https://medium.com/flow-type/flow-for-typescript-users-in-2026-ad07ac0a2d92)

### 概述总结
Flow 在 2026 年对 TypeScript 用户进行了三项重大改进：语法与 TypeScript 趋同、引入 TypeScript 缺少的特性、在差异处保持更安全的默认行为。

- 🔄 **语法趋同**：Flow 的语法已与 TypeScript 高度一致，支持`keyof`、`readonly`、`unknown`、条件类型等特性，TypeScript 用户可快速上手
- ✨ **独特功能**：Flow 提供 TypeScript 没有的`match`表达式（穷举模式匹配）和 React 原生支持（`component`/`hook`/`renders`语法）
- 🛡️ **安全默认值**：Flow 在差异处选择更安全的默认行为，能捕获 TypeScript 忽略的运行时错误
- ⚠️ **四大运行时崩溃**：TypeScript 无法检测但 Flow 能捕获的四种错误——方法绑定丢失、多余属性传递、可变数组协变问题、类型守卫体未验证
- 📚 **完整对比**：官方文档提供 20+ 个 Flow 与 TypeScript 的并排对比案例

---

### [Flow：JavaScript 的类型化方言 — JS 静态类型检查器 | Flow](https://flow.org/)

**原文标题**: [Flow: A Typed Dialect of JavaScript — JS Static Type Checker | Flow](https://flow.org/)

Flow 是一种类型化的 JavaScript 方言，目前语法与 TypeScript 相似，但更安全，并内置了 React 组件支持和模式匹配功能。

- 🎯 **熟悉语法**：支持 `keyof`、`readonly`、`unknown`、索引访问类型 `T[K]`、`extends` 泛型约束、条件类型、映射类型和类型守卫，与 TypeScript 高度兼容。
- ⚛️ **React 一等公民**：内置 `component` 和 `renders` 语法，Props 作为命名参数并支持默认值，组件渲染规则可在类型层面检查，避免运行时错误。
- 🧩 **模式匹配 `match`**：作为表达式或语句，提供安全的 `switch` 替代，无 fall-through，穷尽性检查，结构模式可解构匹配，遗漏 case 时会提示补充。
- 📦 **默认精确对象**：对象类型默认精确，能捕获多余属性，防止因额外字段导致的运行时崩溃（如 `toFixed` 调用失败）。
- 🛡️ **默认安全**：禁止提取未绑定方法（如 `counter.incr`），防止 `this` 丢失导致的运行时错误，比 TypeScript 更严格。

---

### [免费的 Claude Code 课程！| Frontend Masters](https://frontendmasters.com/courses/claude-code/?utm_source=email&utm_medium=javascriptweekly&utm_content=claudecooper)

**原文标题**: [Free Claude Code course! | Frontend Masters](https://frontendmasters.com/courses/claude-code/?utm_source=email&utm_medium=javascriptweekly&utm_content=claudecooper)

本课程提供关于 Claude Code 的高级代理技术，帮助开发者优化编码工作流，涵盖配置、权限管理、多代理系统及插件集成等内容。

- 🎓 免费课程，评分 4.6，由 Anthropic 的 Lydia Hallie 主讲，适合初学者和日常用户
- ⚙️ 使用 CLAUDE.md 文件、技能和钩子配置 Claude Code，自动化重复任务并提升代码质量
- 🔒 通过计划模式、拒绝模式及模型选择，灵活管理权限和成本控制
- 🤖 利用子代理和代理团队并行处理复杂工作流，保持上下文清晰并促进协作
- 🔌 通过插件、MCP 和 Agent SDK 扩展 Claude Code，连接外部工具和服务
- 📚 16 节课，约 1.9 小时，含测验和闪卡，完成后获结业证书
- 🧠 前提：需要提示工程知识和基础软件开发经验
- 🏆 课程内容涵盖：模型理解、工作流自动化、权限配置、多代理编排及系统集成

---

### [npm v12 即将到来的破坏性变更 - GitHub 更新日志](https://github.blog/changelog/2026-06-09-upcoming-breaking-changes-for-npm-v12/)

**原文标题**: [Upcoming breaking changes for npm v12 - GitHub Changelog](https://github.blog/changelog/2026-06-09-upcoming-breaking-changes-for-npm-v12/)

npm v12 将于 2026 年 7 月发布，引入安全相关的默认变更，影响`npm install`命令。当前 npm 11.16.0+ 版本可预览警告。

- 🔒 `allowScripts`默认关闭：`npm install`不再自动执行依赖中的`preinstall`、`install`、`postinstall`脚本（包括原生`node-gyp`构建），需通过`npm approve-scripts`显式允许信任的包，并提交更新后的`package.json`。
- 🌐 `--allow-git`默认`none`：`npm install`不再解析 Git 依赖（直接或间接），防止通过`.npmrc`覆盖 Git 可执行文件的安全风险。
- 📦 `--allow-remote`默认`none`：`npm install`不再解析远程 URL 依赖（如 https tarball），需显式允许。
- 🛠️ 准备步骤：升级到 npm 11.16.0+，运行正常安装并查看警告；使用`npm approve-scripts --allow-scripts-pending`识别脚本包，批准信任的包，提交更新。未批准的脚本将在升级后停止运行。

---

### [发布 v11.16.0 · npm/cli · GitHub](https://github.com/npm/cli/releases/tag/v11.16.0)

**原文标题**: [Release v11.16.0 · npm/cli · GitHub](https://github.com/npm/cli/releases/tag/v11.16.0)

npm CLI v11.16.0 版本发布，包含新功能、错误修复、文档更新和依赖升级。

- 🚀 新增 `publish --access=private` 别名，用于限制发布访问权限
- 🛡️ 引入 `allowScripts` 可选安装脚本策略的第一阶段，增强安全性
- 🐛 修复 `fullMetadata` 的拼写错误
- ⏸️ 修复配置中交互式编辑器启动时进度旋转器的暂停问题
- 📚 文档新增 `npm_old_version` 和 `npm_new_version` 环境变量说明
- 📦 更新多个依赖项，包括 undici、sigstore、lru-cache 等
- 🧹 清理开发依赖，并修复标志表默认值和类型值中的换行符问题
- 👥 感谢 claude、36degrees 等贡献者的参与

---

### [</> htmx ~ 代码更廉价](https://htmx.org/essays/code-is-cheap/)

**原文标题**: [</> htmx ~ Code is Cheap(er)](https://htmx.org/essays/code-is-cheap/)

### 概述总结
AI 使代码生成更便宜，但理解代码的成本上升，复杂性仍是核心挑战，需要培养“减法工程师”思维。

- 🤖 **代码成本下降**：AI 能快速生成大量质量尚可的代码，这是无法否认的现实。
- 🧠 **理解成本上升**：生成代码缺乏内在理解，阅读他人代码比编写更困难，尤其当 AI 产出速度远超人类理解能力时。
- ⚠️ **编译器 vs LLM 误区**：编译器确定性、保留源码、输出领域受限；而 LLM 非确定、不保留源码、输出泛化，两者不可类比。
- 🎬 **魔法学徒陷阱**：AI 像失控的扫帚，快速生成代码可能引发复杂度失控，唯有“巫师”（理解代码者）能掌控局面。
- 📈 **复杂性仍是天敌**：人类难以感知指数级增长，LLM 无惧复杂性却可能加速系统崩溃，需警惕代码膨胀。
- 🛠️ **减法工程师**：核心是“说不”——严格审查 AI 输出、移除冗余代码、简化系统层级，像雕塑家而非建造者。
- 🏗️ **系统设计仍需建设**：在组件组合层面保留“建造者”思维，但减法心态同样有用：消除不必要的系统边界和交互。
- 🌟 **核心矛盾**：代码变便宜，复杂性仍是顶级掠食者，需在 AI 时代保留编程艺术。

---

### [</> htmx - HTML 的高能工具](https://htmx.org/)

**原文标题**: [</> htmx - high power tools for html](https://htmx.org/)

htmx 是一个轻量级、无依赖的 HTML 扩展库，通过属性直接支持 AJAX、CSS 过渡、WebSocket 和 SSE，能大幅减少代码量（相比 React 减少 67%），并即将推出 v4 版本。

- 🚀 **核心特性**：在 HTML 中直接使用属性实现 AJAX、CSS 过渡、WebSocket 和 SSE，无需额外 JavaScript
- 📦 **轻量高效**：仅约 16KB（min.gz'd），无依赖，可扩展，代码量比 React 减少 67%
- 🔧 **突破限制**：允许任意 HTML 元素发起 HTTP 请求，支持多种事件和方法，可局部替换屏幕内容
- ⚡ **快速上手**：通过 CDN 引入后，使用`hx-post`和`hx-swap`等属性即可实现 AJAX 交互
- 📚 **资源支持**：有《Hypermedia Systems》书籍指导构建超媒体驱动应用，可通过 GitHub 赞助支持开发
- 🔄 **版本更新**：htmx v4 正在开发中（Beta 阶段），预计 2026 年夏季正式发布，2.x 已放弃 IE 支持

---

### [使用运行时设置 pnpm · 操作 · GitHub 市场 · GitHub](https://github.com/marketplace/actions/setup-pnpm-with-runtime)

**原文标题**: [Setup pnpm with runtime · Actions · GitHub Marketplace · GitHub](https://github.com/marketplace/actions/setup-pnpm-with-runtime)

该 GitHub Action 可在一个步骤中同时安装 pnpm 和 JavaScript 运行时（Node.js、Bun 或 Deno），简化了 CI 配置。

- 🚀 一键安装 pnpm 和运行时：无需单独使用 actions/setup-node、oven-sh/setup-bun 或 denoland/setup-deno。
- 📦 自动读取配置：若 package.json 中声明了 devEngines.runtime，则自动选择运行时和版本。
- ⚙️ 灵活输入：支持指定 pnpm 版本、运行时（如 node@22、bun@latest）、缓存 pnpm 存储、自定义 package.json 路径等。
- 🔄 自动运行 pnpm install：当存在 package.json 时自动执行，可通过 install: false 跳过。
- 🧩 矩阵测试支持：可轻松在多个 Node 版本上运行测试（如 20、22、24）。
- 🗂️ 缓存支持：启用缓存可加速后续工作流运行。
- 📤 输出信息：提供 dest、bin-dest、runtime-name、runtime-version 等输出，便于后续步骤使用。
- 🔧 工作原理：安装 @pnpm/exe 独立包，通过 pnpm runtime set 下载运行时到 PATH 中，并自动处理版本冲突。

---

### [compilecat - JavaScript 性能编译器](https://isaac-mason.github.io/compilecat/)

**原文标题**: [compilecat - javascript performance compiler](https://isaac-mason.github.io/compilecat/)

本篇文章介绍了 compilecat，一个专注于 JavaScript 性能的编译器项目，由 Isaac Mason 开发，托管在 GitHub 上，并鼓励用户通过 X 平台（Twitter）关注和赞助支持。

- 🐱 项目名称：compilecat，一个 JavaScript 性能编译器
- ⚡ 核心目标：提升 JavaScript 代码的执行性能
- 💻 开发平台：托管在 GitHub 上，便于协作和版本管理
- 🐦 社交联系：通过 X 平台（@isaac_mason_）关注开发者动态
- 💰 赞助支持：项目提供赞助选项，鼓励用户支持开发工作

---

### [GitHub - isaac-mason/compilecat: TypeScript 性能编译器 · GitHub](https://github.com/isaac-mason/compilecat)

**原文标题**: [GitHub - isaac-mason/compilecat: typescript performance compiler · GitHub](https://github.com/isaac-mason/compilecat)

compilecat 是一个 JavaScript/TypeScript 编译器插件，专注于通过注解驱动的热路径优化，支持函数内联、标量替换聚合（SROA）和循环展开。

- ⚠️ 该项目高度实验性，目前不提供稳定性保证，仅作探索用途
- 🔧 提供两种执行模式：`renderChunk`（整程序优化）和 `transform`（逐文件优化），适配 rollup、Vite 和 rolldown
- 📝 通过 `/* @inline */`、`/* @flatten */`、`/* @sroa */`、`/* @unroll */` 和 `/* @optimize */` 等块注释注解驱动优化
- 🚀 `@inline` 支持函数声明或调用点内联；`@flatten` 批量内联函数内所有调用；`@sroa` 将数组局部变量拆分为标量；`@unroll` 展开静态循环
- 🛠️ 优化管道包括类型擦除、内联、循环展开、标量替换、常量折叠、死代码消除等，部分源自 Google Closure Compiler
- 📦 通过 `npm install github:isaac-mason/compilecat` 安装，Vite 适配器需指定 `include` 范围以限制优化目标
- 📜 采用 MIT 许可证，优化部分基于 Apache 2.0 许可证的 Google Closure Compiler

---

### [GitHub - google/closure-compiler：一个JavaScript检查器和优化器。· GitHub](https://github.com/google/closure-compiler)

**原文标题**: [GitHub - google/closure-compiler: A JavaScript checker and optimizer. · GitHub](https://github.com/google/closure-compiler)

Google Closure Compiler 是一个将 JavaScript 代码优化为更高效版本的编译器，主要用于大型项目的代码压缩、错误检查和性能提升，但需遵循特定规则才能正确工作。

- 📦 **核心功能**：将 JavaScript 编译成更优的 JavaScript，通过删除死代码、重写和最小化来提升下载和运行速度。
- ⚠️ **重要限制**：仅`ADVANCED`模式受支持，其他模式已弃用；输入代码必须为编译器专门编写，否则可能产生损坏输出。
- 🔍 **优化前提**：作为“全局”优化器，需直接看到所有全局变量、导出变量和属性名的所有使用，否则会错误删除或重命名。
- 🚫 **属性访问规则**：不能混合使用点访问（`obj.prop`）和方括号访问（`obj[p]`），否则编译器可能无法正确识别属性。
- 🧩 **模块要求**：必须使用`goog.module()`和`goog.require()`声明模块，ES6 的`import/export`支持不活跃，CommonJS 支持可能在 2024 年移除。
- 🛠️ **支持用途**：大幅减小代码体积、检查错误、支持国际化、转译新特性、将应用拆分为按需加载的代码块。
- 📥 **安装方式**：通过 npm 或 yarn 全局安装`google-closure-compiler`，也可从 Maven 仓库下载预编译版本。
- 💻 **基本用法**：使用命令行如`google-closure-compiler --js file.js --js_output_file file.out.js`，或通过 NodeJS API 编程访问。
- 🏗️ **构建与测试**：需 Java 21+、NodeJS、Git 和 Bazelisk，运行`bazelisk build //:compiler_uberjar_deploy.jar`构建，`bazelisk test //:all`测试。
- 🤝 **贡献指南**：需签署 CLA，通过 GitHub 提交 Pull Request，并遵循代码规范和社区行为准则。
- 📜 **许可证**：基于 Apache 2.0 许可证，依赖包括 Rhino、Guava、JUnit 等，各有其许可证。

---

### [发布 @sveltejs/kit@3.0.0-next.4 · sveltejs/kit · GitHub](https://github.com/sveltejs/kit/releases/tag/%40sveltejs%2Fkit%403.0.0-next.4)

**原文标题**: [Release @sveltejs/kit@3.0.0-next.4 · sveltejs/kit · GitHub](https://github.com/sveltejs/kit/releases/tag/%40sveltejs%2Fkit%403.0.0-next.4)

这是一个关于 SvelteKit 预发布版本的更新摘要。

SvelteKit 发布了 3.0.0-next.4 预发布版本，主要包含一个重要的错误修复。

- 🚀 **版本发布**：发布了 `@sveltejs/kit@3.0.0-next.4` 预发布版本，基于 40 次提交。
- 🐛 **错误修复**：修复了当设置 `invalidateAll` 时，导航前未重置查询的问题（#16014）。
- ✅ **代码签名**：该提交已使用 GitHub 的验证签名进行签署，确保代码来源可信。
- 👥 **社区反馈**：该版本获得了 4 个火箭表情反应，来自 SymphonySimper 等用户。

---

### [获取失败](https://javascriptweekly.com/link/186578/web)

**原文标题**: [Failed to retrieve](https://javascriptweekly.com/link/186578/web)

无法总结：获取内容失败，状态码 429。

---

### [vite/packages/vite/CHANGELOG.md 在 v8.1.0-beta.0 版本 · vitejs/vite · GitHub](https://github.com/vitejs/vite/blob/v8.1.0-beta.0/packages/vite/CHANGELOG.md#810-beta0-2026-06-15)

**原文标题**: [vite/packages/vite/CHANGELOG.md at v8.1.0-beta.0 · vitejs/vite · GitHub](https://github.com/vitejs/vite/blob/v8.1.0-beta.0/packages/vite/CHANGELOG.md#810-beta0-2026-06-15)

Vite 是一个开源的前端构建工具，拥有 81.5k 的 Star 和 8.3k 的 Fork，当前版本为 v8.1.0-beta.0，其 CHANGELOG.md 文件包含 2147 行代码，记录了详细的版本更新历史。

- ⚡ Vite 是一个高性能的前端构建工具，广受开发者欢迎
- 🌟 在 GitHub 上拥有 81.5k 的 Star 和 8.3k 的 Fork，社区活跃
- 📝 当前版本为 v8.1.0-beta.0，处于测试阶段
- 📄 CHANGELOG.md 文件包含 2147 行，详细记录了版本变更历史
- 🔧 项目包含 503 个 Issues 和 219 个 Pull Requests，开发活跃
- 🛡️ 设有 19 个安全与质量相关的项目，注重代码质量

---

### [发布 astro@7.0.0-beta.4 · withastro/astro · GitHub](https://github.com/withastro/astro/releases/tag/astro@7.0.0-beta.4)

**原文标题**: [Release astro@7.0.0-beta.4 · withastro/astro · GitHub](https://github.com/withastro/astro/releases/tag/astro@7.0.0-beta.4)

概述摘要  
Astro 7.0.0-beta.4 版本发布，主要变更包括默认 Markdown 处理器切换为 Sätteri，并修复了安全配置相关的警告问题。

- 🚀 默认 Markdown 处理器改为 Sätteri，不再自动安装 @astrojs/markdown-remark  
- 🔧 如需使用 remark/rehype 管道，需手动安装 @astrojs/markdown-remark 并配置 processor  
- ⚠️ 废弃的 markdown.remarkPlugins 等选项仍可用，但需配合 @astrojs/markdown-remark  
- 🛡️ 修复 prerendered 页面中 security.allowedDomains 配置导致的 Astro.request.headers 错误警告  
- ✅ 内部 allowedDomains 头部验证现在跳过 prerendered 路由，避免误报

---

### [发布说明 | Playwright](https://playwright.dev/docs/release-notes#version-161)

**原文标题**: [Release notes | Playwright](https://playwright.dev/docs/release-notes#version-161)

Playwright 发布说明涵盖了从 v1.7 到 v1.61 的多个版本，引入了大量新功能、API 和测试工具改进，包括 WebAuthn 通行密钥、Web Storage API、屏幕录制、HAR 录制、Aria 快照、组件测试、UI 模式、Trace Viewer、测试代理和 CLI 调试等。

- 🔑 **v1.61 新增 WebAuthn 通行密钥支持**，允许测试注册和应答通行密钥，无需真实硬件密钥。
- 🗃️ **v1.61 引入 Web Storage API**，通过 `page.localStorage` 和 `page.sessionStorage` 读写页面存储。
- 🎬 **v1.59 引入 Screencast API**，支持视频录制、动作注释、视觉叠加和实时帧捕获。
- 🌐 **v1.60 在 Tracing 中集成 HAR 录制**，通过 `tracing.startHar()` / `stopHar()` 实现。
- 🎯 **v1.49 引入 Aria 快照断言** `expect(locator).toMatchAriaSnapshot()`，用于验证页面结构。
- 🧩 **v1.22 引入组件测试（预览）**，支持 React 和 Vue.js 组件在真实浏览器中测试。
- 🖥️ **v1.32 引入 UI 模式（预览）**，提供探索、运行和调试测试的图形界面。
- 📋 **v1.16 引入 CLI Trace Viewer**，用于分析测试追踪文件。
- 🤖 **v1.56 引入 Playwright 测试代理**，包括规划器、生成器和修复器，辅助 LLM 构建测试。
- 🐛 **v1.59 引入 CLI 调试器**，支持代理通过 `playwright-cli` 附加和调试测试。
- 🚀 **v1.12 正式发布 Playwright Test 测试运行器**，支持跨浏览器并行测试、上下文隔离和失败时自动捕获视频/截图。
- 🔗 **v1.59 新增 `browser.bind()` API**，使启动的浏览器可被 `playwright-cli` 和 `@playwright/mcp` 等客户端连接。
- 🛠️ **多个版本持续改进**，包括网络路由、WebSocket 路由、时钟 API、TLS 客户端证书、新断言方法、HAR 重放、角色选择器和定位器 API 等。

---

### [Web 存储 | Playwright](https://playwright.dev/docs/api/class-webstorage)

**原文标题**: [WebStorage | Playwright](https://playwright.dev/docs/api/class-webstorage)

WebStorage 提供一個非同步、跨瀏覽器一致的 API，用於存取頁面的 localStorage 或 sessionStorage，可透過 page.localStorage 和 page.sessionStorage 使用。

- 📦 **clear()**：移除儲存空間中的所有項目，無回傳值。
- 🔍 **getItem(name)**：根據名稱取得對應的值，若不存在則回傳 null。
- 📋 **items()**：回傳所有儲存項目，以名稱/值對的陣列形式呈現。
- ❌ **removeItem(name)**：移除指定名稱的項目，若項目不存在則不執行任何操作。
- ✏️ **setItem(name, value)**：設定指定名稱的值，若名稱已存在則覆蓋原有值。

---

### [ESLint v10.5.0 发布 - ESLint - 可插拔的 JavaScript 代码检查工具](https://eslint.org/blog/2026/06/eslint-v10.5.0-released/)

**原文标题**: [ESLint v10.5.0 released - ESLint - Pluggable JavaScript Linter](https://eslint.org/blog/2026/06/eslint-v10.5.0-released/)

ESLint v10.5.0 发布，这是一个次要版本升级，新增了一些功能并修复了多个错误。

- 🎯 五个核心规则现在高亮更小的代码范围，避免在编辑器中遮蔽其他问题
- 📏 `max-lines-per-function`、`max-nested-callbacks` 和 `max-statements` 规则仅高亮函数头部而非整个函数
- 🔍 `max-depth` 和 `no-with` 规则仅高亮第一个关键字
- 🐛 修复了 `max-depth` 和 `max-nested-callbacks` 规则中的计算错误，可能报告更多现有代码中的 lint 错误
- ✨ 新增功能：修正 `max-nested-callbacks` 的堆栈跟踪、在 `no-with` 的 with 关键字处报告违规、在函数头部报告 `max-lines-per-function` 和 `max-nested-callbacks` 违规、在 `max-depth` 的关键字处报告违规、修正 `max-depth` 对 else-if 链的处理、更新 `max-statements` 的错误位置到函数头部
- 📚 文档更新：更新 README、Node.js 先决条件增加 ICU 支持、阐明 parserOptions 对 languageOptions 的优先级
- 🛠 杂项：更新生态系统插件、重构代码、增强配置规则支持、添加单元测试、更新依赖

---

### [TanStack AI Beta：AI 工具界的瑞士军刀成长记 | TanStack 博客](https://tanstack.com/blog/tanstack-ai-beta)

**原文标题**: [TanStack AI Beta: The Switzerland of AI Tooling Grows Up | TanStack Blog](https://tanstack.com/blog/tanstack-ai-beta)

TanStack AI 正式发布 Beta 版本，提供框架和供应商无关的 AI 工具包，支持多模态、类型安全和可调试性。

- 🎉 **Beta 版本发布**：核心 API 已稳定，协议已文档化和版本化，测试基础设施强大，适合构建真实产品。
- 🧠 **统一的多模态 API**：支持文本、图像、视频、音频生成、实时语音聊天等，所有模态共享一致的接口和钩子（如 `useChat`、`useGenerateImage`）。
- 🔄 **供应商切换零成本**：仅需更改导入的适配器（如从 `openaiText` 改为 `anthropicText`），代码结构不变，实现真正的供应商无关。
- ✅ **逐模型类型安全**：每个模型和供应商的选项在类型层面严格区分，不兼容的工具会在编译时报错，避免生产环境静默失败。
- 🛠️ **生产级系统构建**：内置中间件、惰性工具发现、代码模式、MCP 支持及实验性编排功能，帮助管理日志、缓存、追踪等复杂性。
- 🌐 **TypeScript 优先与开放协议**：基于 AG-UI 协议，支持跨语言后端（如 Python、Rust），前端兼容 React、Vue、Svelte 等框架。
- 🔍 **可视化调试**：提供可插拔的调试日志和同构开发者工具，可逐层查看 LLM 行为、中间件输入输出及工具执行。
- 🧪 **严格测试保障**：在每次 PR 中运行 265 个确定性端到端测试，覆盖 10 个 LLM 提供商，确保稳定性和兼容性。
- 💡 **开源且无锁定**：无商业服务或平台迁移要求，保持开源精神，提供与 Vercel AI SDK 的诚实对比文档。

---

### [TanStack Table V9 中的 TypeScript 性能 | TanStack 博客](https://tanstack.com/blog/tanstack-table-v9-typescript-performance)

**原文标题**: [TypeScript Performance in TanStack Table V9 | TanStack Blog](https://tanstack.com/blog/tanstack-table-v9-typescript-performance)

TanStack Table V9 在保持功能强大的同时，大幅优化了 TypeScript 类型性能，从 Alpha 版本到 Beta 版本将类型实例化次数降低了 62-86%，显著提升了编辑器体验。

- 🚀 **性能飞跃**：核心包类型实例化从 Alpha 版的 1,230,007 次降至 Beta 版的 266,723 次，降幅达 78.3%，React 适配器也降低了 76.9%。
- 🧩 **模块化特性系统**：V9 将特性模块化，用户可按需选择功能，类型系统会基于所选特性自动组装，实现按需加载和更精准的类型推断。
- 📉 **消除性能瓶颈**：通过将 14 个条件分支的 UnionToIntersection 模式替换为命名的 FeatureMap 接口，大幅减少了编译器重复计算。
- 🔧 **内部类型优化**：将内部使用的 Table_Internal 类型从条件类型改为接口，避免了每次调用时的重展开，核心包实例化再降 40%。
- 🏷️ **方差注解**：为 166 个泛型参数添加 `in out` 注解，让编译器直接根据类型参数关联实例，避免了结构回退检查，React 适配器性能提升一倍。
- 🎯 **显式类型参数**：在适配器钩子中显式传递类型参数，消除类型推断步骤，为 Angular 和 Preact 适配器节省约 15% 的检查时间。
- 📊 **全框架受益**：所有框架适配器（Angular、Lit、Preact、React、Solid、Svelte、Vue）的类型性能均提升 62% 至 85% 以上。
- 💡 **作者建议**：对于库作者，应测量 Instantiations 指标、使用命名类型作为缓存点、用接口替代条件类型、并善用 `in out` 注解。

---

### [TanStack Table V9：表单化 | TanStack 博客](https://tanstack.com/blog/tanstack-table-v9-taking-form)

**原文标题**: [TanStack Table V9: Taking Form | TanStack Blog](https://tanstack.com/blog/tanstack-table-v9-taking-form)

TanStack Table V9 测试版发布，带来了多项重大改进，解决了 V8 版本中长期存在的问题，并引入了更现代的状态管理和扩展机制。

- 🎉 **V9 测试版正式发布**：经过多年开发，TanStack Table V9 终于进入 Beta 阶段，带来了全面的架构升级和性能优化。

- 🔧 **状态管理革新**：采用 TanStack Store 作为底层状态管理，支持原子（Atom）状态管理，更好地兼容 React Compiler，并提供更细粒度的订阅控制。

- ⚡ **渲染性能提升**：通过状态选择器（State Selector）和`table.Subscribe`组件，实现精确的组件级重新渲染，避免不必要的全局更新。

- 🧠 **内存优化**：针对大型虚拟化表格，通过共享原型、减少不必要的对象创建和优化行模型，显著降低内存占用。

- 📦 **树摇（Tree-shakable）特性**：采用插件式特性注册机制，用户可按需引入功能模块，有效控制包体积，同时保持 TypeScript 类型安全。

- 🔌 **自定义扩展能力**：提供清晰的特性扩展模型，允许开发者创建自定义特性，与内置特性使用相同的 API 体系。

- 🔄 **可复用表格代码**：引入`createTableHook`和`tableOptions`，支持一次性定义通用表格配置和组件，实现跨项目的代码复用。

- 🛠️ **全新开发者工具**：集成@tanstack/devtools 平台，提供专门的表格调试面板，支持状态检查和数据可视化，并区分开发/生产环境。

- 📚 **丰富的示例和迁移指南**：提供完整的 V8 到 V9 迁移指南，以及多个框架（React、Angular、Vue 等）的 Kitchen Sink 示例。

---

### [2026 年 React 库 - Robin Wieruch](https://www.robinwieruch.de/react-libraries/)

**原文标题**: [React Libraries for 2026 - Robin Wieruch](https://www.robinwieruch.de/react-libraries/)

以下是您提供的文章内容摘要：

React 生态系统在 2026 年已高度成熟，开发者可根据项目需求灵活选择库，从轻量级设置到全栈应用均有成熟方案。

- 🚀 **项目启动**：推荐 Vite 用于客户端渲染，Next.js 用于全栈应用，Astro 用于静态站点；TanStack Start 和 React Router v7 是新兴全栈选择。
- 📦 **包管理器**：npm 最普及，pnpm 以速度和磁盘效率成为强替代，Bun 作为一体化工具链增长迅速。
- 🗃️ **状态管理**：内置 useState/useReducer 处理局部状态，Zustand 是全局状态的事实标准；TanStack Query 专用于远程数据获取和缓存。
- 🔄 **数据获取**：客户端推荐 TanStack Query（REST/GraphQL），服务端优先使用 React Server Components；tRPC 提供端到端类型安全。
- 🧭 **路由**：React Router 最常用，TanStack Router 以 TypeScript 类型安全见长；框架自带路由（如 Next.js）可免额外配置。
- 🎨 **CSS 样式**：Tailwind CSS 成为行业标准（v4 版本），CSS Modules 用于封装，PandaCSS 和 vanilla-extract 是零运行时 CSS-in-JS 替代。
- 🧩 **UI 库**：shadcn/ui 是无头 UI 的事实标准，Mantine 和 Chakra UI v3 是全能型选择；趋势转向无样式、可组合的库。
- 🎞️ **动画**：Motion（原 Framer Motion）是标准选择，react-spring 适合物理动画，GSAP 用于复杂时间线动画。
- 📊 **可视化**：Recharts 是推荐图表库（shadcn/ui 图表的基础），D3 提供底层控制，Tremor 适合 SaaS 仪表盘。
- 📝 **表单**：React Hook Form 最流行，常与 zod 集成验证；TanStack Form 和 Conform 是新兴替代。
- 🔧 **代码结构**：ESLint + Prettier 是成熟方案，oxlint + oxfmt 是 Rust 驱动的更快替代，Biome v2 提供单二进制工具链。
- 🔐 **认证**：Better Auth 是自托管首选，Clerk 和 AuthKit 是付费方案，Supabase Auth 和 Firebase Auth 适合已有后端用户。
- 🖥️ **后端**：Next.js、Astro、React Router v7 和 TanStack Start 是全栈框架；Hono 是边缘运行时首选，Express v5 仍是经典选择。
- 🗄️ **数据库**：Drizzle ORM 已超越 Prisma 成为默认选择，Kysely 是轻量查询构建器；Supabase 和 Convex 是流行后端服务。
- 🌐 **托管**：Vercel 最适合 Next.js，Netlify 是竞争选择，Cloudflare 提供慷慨免费层；Coolify 是自托管开源 PaaS。
- 🧪 **测试**：Vitest + React Testing Library 用于单元/集成测试，Playwright 是端到端测试默认选择。
- 📅 **时间处理**：date-fns 和 Day.js 是主流，Temporal API 已进入 ES2026 标准，未来可原生替代。
- 📧 **邮件**：react-email 是标准邮件渲染库，Resend 是推荐邮件服务提供商。
- 📱 **移动开发**：Expo 已成为 React Native 的默认框架，Tamagui 提供跨平台统一组件。
- 🎮 **VR/AR**：react-three-fiber 是 Three.js 的 React 渲染器，@react-three/xr 提供 VR/AR 功能。
- 🛠️ **设计原型**：v0 by Vercel 是 AI 驱动组件生成默认工具，Figma 仍是设计协作标准。
- 📚 **组件文档**：Storybook 是通用选择，Ladle 提供更快的 React 专用替代。

---

### [编码代理测试运行器命令行界面](https://wallabyjs.com/whatsnew/cli.html?utm_source=cooperpress&utm_medium=javascriptweekly&utm_content=javascriptweekly)

**原文标题**: [Test Runner CLI for Coding Agents](https://wallabyjs.com/whatsnew/cli.html?utm_source=cooperpress&utm_medium=javascriptweekly&utm_content=javascriptweekly)

Wallaby CLI 为 AI 编码代理带来了运行时测试智能，可直接在命令行中运行测试并提供结果、覆盖率和运行时数据，无需编辑器或 MCP 服务器。

- 🧪 支持 Claude Code、Codex CLI、Copilot CLI 等多种 AI 编码代理，无需编辑器会话或 MCP 服务器即可运行测试
- ⚡ 兼容 Vitest、Jest 等测试框架，提供精确的结构化运行时数据，减少令牌消耗并加速反馈循环
- 🚀 通过`npx skills add`命令轻松集成，按需启动和停止，并可复用编辑器会话中的现有实例
- ✅ 帮助代理验证生成代码、提升测试质量和覆盖率，无需修改源文件即可调试失败测试
- 🔄 持续改进对隔离、沙盒和 CI 环境的支持，并计划连接编辑器扩展与 CLI 管理的 Wallaby 实例

---

### [React Native、Hermes 字节码与 Kindle 主页 | Rincon](https://sighery.com/posts/patching-kindle-homepage/)

**原文标题**: [React Native, Hermes bytecode, and the Kindle homepage | Rincon](https://sighery.com/posts/patching-kindle-homepage/)

Kindle 主頁使用 React Native 和 Hermes 字節碼，自 5.14.2 版本起取代了舊的 Java 實現，這使得逆向工程和修改變得更加困難。

- 📱 Kindle 主頁自 2022 年起使用 React Native 和 Hermes 字節碼，取代了舊的 Java 堆棧
- 🔧 Hermes 字節碼版本不兼容，Kindle 使用版本 84，需使用對應的 v0.11.0 版本進行構建
- 🛠️ hbctool 是修補 Hermes 字節碼的主要工具，支持反彙編和重新彙編，但已停止維護
- 📝 字節碼修補可通過修改字符串表或操作碼實現，字符串修補有限制，操作碼修補更靈活
- 🎯 KPP_Patch 工具可自動化修補 Kindle 主頁，移除廣告書架（如 Discover Books、Top Reads With Prime）
- 🔍 使用 screenControl 和 KIWI 功能可定位 UI 元素，找到對應的模板函數進行修補
- ⚠️ 部分卡片（如 Card 49 和 Card 18）需修補 render 函數，其他卡片可直接修補模板函數
- 📂 修補程式碼可通過函數名稱或 ID 定位，未來需改進函數查找方法以適應不同固件版本

---

### [GitHub - facebook/hermes: 一个为运行 React Native 而优化的 JavaScript 引擎。](https://github.com/facebook/hermes)

**原文标题**: [GitHub - facebook/hermes: A JavaScript engine optimized for running React Native. · GitHub](https://github.com/facebook/hermes)

Hermes 是一个专为 React Native 应用优化的 JavaScript 引擎，通过提前静态优化和紧凑字节码实现快速启动。

- 🚀 **核心优化**：专为 React Native 应用快速启动设计，采用提前静态优化和紧凑字节码技术
- 📱 **使用方式**：用户无需直接访问源码，只需按照官方指南启用 Hermes 即可在 React Native 项目中使用
- ⚠️ **版本匹配**：每个 Hermes 版本对应特定 React Native 版本，版本不匹配可能导致应用崩溃，需严格遵循版本发布
- 🔧 **构建指南**：提供 macOS/Linux 和 Windows 的详细构建步骤，依赖 cmake 和 Ninja 等工具
- 📚 **资源链接**：包含 Hermes 博客、构建文档、自定义构建集成指南等丰富资源
- 🤝 **社区贡献**：欢迎社区贡献，设有行为准则、贡献指南和安全政策
- 📄 **开源许可**：采用 MIT 许可证，代码主要语言为 JavaScript (52.8%) 和 C++ (36.5%)
- ⭐ **项目概况**：获得 11.1k 星标，804 个复刻，137 位关注者，最新版本 v0.13.0（2024 年 8 月发布）

---

### [使 numpy-ts 达到原生速度 — nico.codes](https://nico.codes/notes/numpyts-optimization/)

**原文标题**: [Making numpy-ts as fast as native — nico.codes](https://nico.codes/notes/numpyts-optimization/)

### 概述总结
numpy-ts 通过将数组数据所有权从 JavaScript 转移到 WASM 线性内存，实现了从比原生 NumPy 慢 15 倍到性能持平甚至略快的突破。

- 🚀 **初始阶段**：纯 TypeScript 实现比 NumPy 慢 15 倍，因为 JS 无法利用 SIMD、BLAS 等底层优化。
- 🧩 **WASM 优化**：将核心计算迁移到 Zig 编译的 WASM 模块，性能差距缩小至 2 倍，但仍有瓶颈。
- 🔄 **关键突破**：发现性能瓶颈并非 WASM 调用开销，而是每次操作都需要在 JS 和 WASM 内存间复制数据。
- 💾 **内存模型变革**：将 ndarray 数据存储在 WASM 线性内存中，JS 仅持有元数据，消除复制开销，性能达到原生 NumPy 的 1.11 倍。
- ⚖️ **权衡一：内存管理**：WASM 内存需手动管理，通过 FinalizationRegistry 和 Symbol.dispose 支持自动与确定性清理。
- 🔢 **权衡二：数据类型**：WASM 对 float16 等类型支持有限，需通过 uint16 存储并提升为 float32 计算。
- 📦 **权衡三：打包兼容**：为适应多运行环境，将 WASM 模块编码为 base64 内联到 TypeScript 文件中，确保可树摇和 ESM 兼容。
- 🧠 **核心教训**：原生性能的关键不在于计算位置，而在于数据驻留位置——数据应存在于内核运行的内存空间。

---

### [numpy-ts - 数值计算库](https://numpyts.dev)

**原文标题**: [numpy-ts - numpy-ts](https://numpyts.dev)

numpy-ts 是一个完整的 NumPy TypeScript 实现，提供与 Python NumPy 相同的 API，具有类型安全、零依赖和高效性能等特点。

- 📊 94% API 覆盖率：实现了 476 个 NumPy 函数，涵盖基础运算、FFT、线性代数和随机分布等
- ⚡ 比 NumPy 快 1.13 倍：在 7200 个基准测试中平均性能更优，18 个类别中有 12 个更快
- 🚫 零依赖：纯 TypeScript + WASM 实现，无原生模块或第三方包
- ✅ NumPy 验证：超过 20000 个测试直接对比 NumPy 输出，确保结果一致
- 🔒 类型安全：为每个函数、数据类型和数组操作提供完整 TypeScript 类型定义
- 🌳 可摇树优化：按需导入，构建工具自动消除未使用代码，减小生产包体积
- 🔄 无缝迁移：API 与 NumPy 高度一致，Python 代码可直接转换为 TypeScript
- 📚 丰富文档：提供快速入门、API 参考、示例和性能基准测试

---

### [一夜之间，构建 HTML 优先的网站让我们的用户翻倍](https://mohkohn.co.uk/writing/html-first/)

**原文标题**: [How building an HTML-first site doubled our users overnight](https://mohkohn.co.uk/writing/html-first/)

### 概述总结
一家公用事业公司通过采用 HTML 优先的架构，将表单完成率翻倍，并解决了用户流失和合规风险问题。

- 📈 **用户翻倍**：改用 HTML 优先的 Astro 框架后，表单完成用户数一夜之间翻倍，甚至让分析团队无法追踪来源。
- 🚫 **失败教训**：之前两次昂贵的尝试（包括 React 应用）因加载慢、可访问性差等问题失败，仅上线 3 天就被撤回。
- 🛠️ **核心方案**：采用 HTML 优先设计，每个表单步骤独立页面，提交后通过 API 验证并重定向，确保无 JavaScript 也能运行。
- 📱 **极端兼容**：要求表单能在老旧设备（如 PSP）和弱网络下工作，参考 GOV.UK 的轻量 HTML 设计理念。
- 🧩 **轻量验证**：自研`validation-enhancer` Web 组件（<1KB），利用浏览器原生验证，渐进增强用户体验，失败时自动回退。
- 💾 **数据安全**：每个会话分配唯一 ID，所有数据实时存储后端，用户可一个月后继续填写，不会丢失。
- ♿ **无障碍优先**：满足 WCAG AA 标准，确保辅助技术用户和旧浏览器用户也能正常使用。
- ⚠️ **行业反思**：作者强调不应抛弃旧用户，应构建能在任何设备上稳定运行的成熟应用，而非追逐短期技术潮流。

---

### [在 Astro 中轻松构建真实博客 | Zell Liew](https://zellwk.com/blog/real-astro-blog-made-easy/)

**原文标题**: [Building a Real Blog Easily in Astro | Zell Liew](https://zellwk.com/blog/real-astro-blog-made-easy/)

本文介紹了如何在 Astro 中建立一個功能完善的部落格，從基本架構到進階的用戶體驗與開發者體驗改進，並提供了一個簡化流程的函數。

- 📝 **基本部落格需求**：每篇文章需包含標題、永久連結（slug）、描述、標籤和發布日期，這些通常放在 frontmatter 中。
- 🔧 **靜態渲染設定**：將 Astro 的輸出設為 `static`，讓部落格頁面靜態化，可透過 CDN 加速載入。
- 🏗️ **建立基本部落格**：在 `pages/blog` 目錄下創建 `[slug].astro` 文件，使用 `getStaticPaths` 生成靜態頁面，並透過 `render` 提取內容。
- 🚀 **真實部落格需求**：增加發布日期於檔名、更新日期、摘要、過濾已發布文章、按時間倒序排序等功能，提升內容管理效率。
- 📅 **檔名含發布日期**：使用 `YYYY-MM-DD-slug.md` 格式，方便按時間查找，並需從檔名提取 slug 和日期。
- 🔄 **更新日期處理**：在 frontmatter 添加 `updateDate`，並在頁面顯示更新標記，同時需考慮排序時結合 `pubDate` 和 `updateDate`。
- ✂️ **建立摘要**：透過 `<!-- more -->` 註解自訂摘要位置，並在程式碼中提取其前內容，支援 Markdown 格式輸出。
- ✅ **過濾已發布文章**：根據 `pubDate` 是否早於或等於今天，或 `status` 設為 `published` 來過濾，排除草稿。
- 📊 **文章排序**：使用 `Array.sort()` 按 `pubDate` 或 `updateDate` 倒序排列，需先複製陣列避免變異。
- 🛠️ **簡化流程**：作者開發了 `processFiles` 函數，整合上述所有功能，只需一行程式碼即可套用，並支援客製化配置。

---

### [流式 HTML](https://olliewilliams.xyz/blog/streaming-html/)

**原文标题**: [Streaming HTML](https://olliewilliams.xyz/blog/streaming-html/)

### 概述总结
本文介绍了通过 `fetch()` API 获取 HTML 流、使用 `textStream()` 方法解码流数据，以及将 HTML 流式注入 DOM 的新方法。同时对比了安全与非安全方法，并提到了声明式部分更新和浏览器支持情况。

- 📡 **获取 HTML 流**：使用 `fetch()` 的 `response.textStream()` 方法（等效于 `response.body.pipeThrough(new TextDecoderStream())`）可获取字符串流，而非一次性返回全部文本。
- 🖥️ **流式注入 DOM**：新增 `streamHTML`、`streamAppendHTML` 等安全方法，以及对应的 `Unsafe` 版本（如 `streamHTMLUnsafe`），用于将 HTML 流式插入元素，支持替换、追加、前置等操作。
- 🔒 **安全与不安全方法**：安全方法（如 `streamHTML`）自动清理 HTML；不安全方法（如 `streamHTMLUnsafe`）不执行默认清理，但可选用消毒器，并支持声明式 Shadow DOM 和 `runScripts` 选项。
- 🧩 **声明式部分更新**：通过 `<template>` 元素和 `<?marker>` 处理指令，可将模板内容流式注入页面指定位置，实现部分更新。
- 🚀 **浏览器支持**：`textStream()` 和流式 DOM 方法目前仅在 Chrome Canary 中支持。

---

### [GitHub - sindresorhus/eslint-plugin-unicorn：超过200条强大的ESLint规则 · GitHub](https://github.com/sindresorhus/eslint-plugin-unicorn)

**原文标题**: [GitHub - sindresorhus/eslint-plugin-unicorn: More than 200 powerful ESLint rules · GitHub](https://github.com/sindresorhus/eslint-plugin-unicorn)

eslint-plugin-unicorn 是一个包含超过 200 条强大 ESLint 规则的插件，主要针对 JavaScript 和 TypeScript，部分规则也支持 CSS、HTML、JSON 和 Markdown。它需要 ESLint >=10.4、扁平配置和 ESM，并提供推荐配置和全量配置预设。

- 🦄 插件提供超过 200 条 ESLint 规则，覆盖 JavaScript 和 TypeScript，并支持 CSS、HTML、JSON 和 Markdown
- ⚙️ 需要 ESLint >=10.4、扁平配置和 ESM，安装命令为 `npm install --save-dev eslint eslint-plugin-unicorn`
- 📋 提供推荐配置（`recommended`）和全量配置（`all`）预设，方便快速集成
- 🔧 多数规则支持自动修复（`--fix`）或手动修复（编辑器建议），部分规则需要类型信息
- 🌟 规则涵盖多种类别，如数组方法、DOM 操作、错误处理、模块规范等，例如 `prefer-module`、`no-for-each`、`prefer-array-find`
- 🗑️ 已删除和废弃的规则有单独列表，确保维护清晰
- 👥 由 Sindre Sorhus 和 Fisker Cheung 维护，拥有 5.1k 星和 485 个分支

---

### [eslint-plugin-unicorn/docs/rules/comment-content.md 在主分支 · sindresorhus/eslint-plugin-unicorn · GitHub](https://github.com/sindresorhus/eslint-plugin-unicorn/blob/main/docs/rules/comment-content.md)

**原文标题**: [eslint-plugin-unicorn/docs/rules/comment-content.md at main · sindresorhus/eslint-plugin-unicorn · GitHub](https://github.com/sindresorhus/eslint-plugin-unicorn/blob/main/docs/rules/comment-content.md)

该规则旨在强制注释内容遵循更优的书写规范，如品牌名称、缩写和项目特定术语的正确大小写。

- 📝 规则概述：强制注释内容使用更优的替换，例如将 `nodejs` 改为 `Node.js`，或自定义项目偏好。
- 🚫 配置状态：在 `recommended` 和 `unopinionated` 配置中默认禁用，但可通过 `--fix` 自动修复。
- 🔧 替换机制：仅检查已知替换模式，每次只报告一个替换，并跳过代码片段、链接等非散文区域。
- ❌ 错误示例：`nodejs uses javascript.` → ✅ 正确示例：`Node.js uses JavaScript.`
- ⚙️ 选项 `checkUniformCase`：默认 `true`，可设为 `false` 以仅修正大小写混合的令牌（如 `Github` → `GitHub`），忽略全小写或全大写。
- 🛠️ 选项 `replacements`：允许自定义替换，键为正则表达式，默认区分大小写；可禁用特定模式（如 `false`）。
- 🔄 选项 `extendDefaultReplacements`：默认 `true`，设为 `false` 可完全覆盖默认替换列表。

---

### [eslint-plugin-unicorn/docs/rules/max-nested-calls.md 在 main 分支 · sindresorhus/eslint-plugin-unicorn · GitHub](https://github.com/sindresorhus/eslint-plugin-unicorn/blob/main/docs/rules/max-nested-calls.md)

**原文标题**: [eslint-plugin-unicorn/docs/rules/max-nested-calls.md at main · sindresorhus/eslint-plugin-unicorn · GitHub](https://github.com/sindresorhus/eslint-plugin-unicorn/blob/main/docs/rules/max-nested-calls.md)

该规则限制嵌套调用的深度，以提高代码可读性。默认最大嵌套深度为 3 层。

- 📝 限制嵌套调用深度，避免代码难以阅读
- 💡 建议将中间结果提取为命名变量，替代深层嵌套
- 🔄 忽略流畅接收者链（如 query().filter().map()）和 JSX 包装器
- ⚙️ 默认最大深度为 3 层，可通过 `max` 选项自定义（如设为 4）
- ✅ 推荐配置中启用，非意见性配置中禁用

---

### [eslint-plugin-unicorn/docs/rules/prefer-temporal.md 位于主分支 · sindresorhus/eslint-plugin-unicorn · GitHub](https://github.com/sindresorhus/eslint-plugin-unicorn/blob/main/docs/rules/prefer-temporal.md)

**原文标题**: [eslint-plugin-unicorn/docs/rules/prefer-temporal.md at main · sindresorhus/eslint-plugin-unicorn · GitHub](https://github.com/sindresorhus/eslint-plugin-unicorn/blob/main/docs/rules/prefer-temporal.md)

eslint-plugin-unicorn 的 prefer-temporal 规则推荐用 Temporal 替代 Date，修复了 Date 的零索引月份、可变性、时区缺失和跨平台解析不一致等问题。

- 📝 规则建议使用 Temporal 替代 Date，因为 Temporal 是 ECMAScript 2026 标准的一部分，提供不可变类型和精确解析
- 🚫 该规则在 recommended 和 unopinionated 配置中默认禁用
- 🔧 支持自动修复（--fix）和编辑器建议修复
- 🎯 Date.now() 自动修复为 Temporal.Now.instant().epochMilliseconds，返回相同的毫秒数
- ⚠️ new Date() 和 new Date(milliseconds) 有精确的 Temporal 等价建议，但字符串解析和日历部分仅报告不自动修复
- 🌐 Temporal 已到 Stage 4，在 Node.js 26 和现代浏览器中无需标记，旧环境可使用 @js-temporal/polyfill
- 📋 提供 checkDateNow、checkReferences 和 checkMethods 三个可选配置项，默认关闭
- 🛠️ checkMethods 需要类型信息支持，仅检测类型为 Date 的值，不包括子类或泛型约束

---

### [eslint-plugin-unicorn/docs/rules/prefer-https.md 在 main 分支 · sindresorhus/eslint-plugin-unicorn · GitHub](https://github.com/sindresorhus/eslint-plugin-unicorn/blob/main/docs/rules/prefer-https.md)

**原文标题**: [eslint-plugin-unicorn/docs/rules/prefer-https.md at main · sindresorhus/eslint-plugin-unicorn · GitHub](https://github.com/sindresorhus/eslint-plugin-unicorn/blob/main/docs/rules/prefer-https.md)

eslint-plugin-unicorn 的 `prefer-https` 规则旨在强制使用 HTTPS 替代 HTTP，以提升安全性。

- 🔒 规则默认在 `recommended` 配置中启用，在 `unopinionated` 配置中禁用，并支持 `--fix` 自动修复。
- 🌐 检查范围包括源代码中的字符串、模板字面量、JSX、注释，以及通过 ESLint 语言插件（如 `@eslint/css`、`@eslint/json` 等）处理的非 JavaScript 文件。
- 🚫 忽略没有公开顶级域名的 URL（如 `http://localhost`、`http://example`、`http://127.0.0.1`），以及已知的 XML 命名空间 URI（如 `http://www.w3.org/2000/svg`），以避免破坏解析。
- ❌ 错误示例：`const url = 'http://sindresorhus.com';`、注释中的 `http://` 链接、JSX 中的 `http://` 属性。
- ✅ 正确示例：`const url = 'https://sindresorhus.com';`、注释和 JSX 中使用 `https://`。

---

### [GitHub - gajus/zod-compiler: 在构建时将 Zod 模式编译为零开销的验证函数。支持 Vite、webpack、esbuild、Rollup 等](https://github.com/gajus/zod-compiler)

**原文标题**: [GitHub - gajus/zod-compiler: Compile Zod schemas into zero-overhead validation functions at build time. Works with Vite, webpack, esbuild, Rollup, etc · GitHub](https://github.com/gajus/zod-compiler)

zod-compiler 是一个在构建时编译 Zod 架构的工具，可将验证速度提升 2-75 倍，无需更改代码。

- ⚡ **性能飞跃**：通过构建时编译，将 Zod 架构转换为零开销的验证函数，性能提升 2-75 倍，嵌套对象和数组的增益最大。
- 🔧 **多种使用模式**：支持自动模式（零代码更改）、显式 `compile()` 包裹模式，以及 CLI 命令行模式，适应不同项目需求。
- 🛠 **广泛构建工具支持**：兼容 Vite、webpack、esbuild、Rollup、Rolldown、rspack、Bun、Farm 等主流构建工具。
- 🧩 **完整 API 保留**：编译后的架构保留原始 Zod 对象的完整 API（如 `.parse()`、`.safeParse()`、`.shape`、`instanceof`），与 tRPC、Hono、React Hook Form 等库无缝集成。
- 🚀 **双阶段验证架构**：生成“快速路径”（零分配的布尔表达式链）和“慢速路径”（错误收集验证），有效输入立即返回，无效输入才触发详细错误。
- 📦 **优化包体积**：通过共享运行时模块和结构去重，减少生成的验证器代码体积，同时保持高性能。
- 🔍 **架构诊断工具**：提供 `npx zod-compiler check` 命令，分析架构编译覆盖率、快速路径资格，并给出优化建议。
- 🧪 **全面编译支持**：完全编译大多数标准 Zod 类型（字符串、数字、对象、数组、联合等），对包含捕获变量的 `transform`/`refine` 等回调则回退到 Zod 运行时。
- ⚠️ **行为差异注意**：默认情况下，编译后的验证器在成功解析时返回输入值本身（而非重建），因此 `z.object()` 不会剥离未知键；可通过 `stripUnknownKeys` 选项启用剥离行为。
- 🏗 **架构提升**：自动将函数体内定义的 Zod 架构提升到模块作用域，避免每次调用时重复构建，显著提升性能。

---

### [适用于任意规模时间序列工作负载的 Postgres。| Tiger Data](https://www.tigerdata.com/go/trial?utm_source=content-syndication&utm_medium=referral&utm_campaign=javascript-weekly-newsletter)

**原文标题**: [Postgres for time-series workloads at any scale. | Tiger Data](https://www.tigerdata.com/go/trial?utm_source=content-syndication&utm_medium=referral&utm_campaign=javascript-weekly-newsletter)

Tiger Cloud 提供专为时间序列工作负载优化的 PostgreSQL 服务，支持大规模数据处理，并附带免费试用额度。

- 🚀 提供免费试用，新用户获 $1000 额度（30 天有效），无需信用卡
- 📊 支持每秒 3 万亿指标、3PB 数据、1 千万亿数据点的超大规模
- 🔄 读写分离架构，最多 10 节点副本集，SSD/S3 分层存储实现无限扩展
- 💰 计算与存储分离，独立扩缩容，避免为闲置容量付费
- 🛡️ 多可用区集群，自动故障转移、时间点恢复和跨区域备份
- 🔐 企业级安全：SOC 2、HIPAA、GDPR 合规，始终加密、SSO、RBAC 和审计日志
- 👁️ 深度可观测性：查询钻取和仪表盘，集成 CloudWatch、Datadog、Prometheus
- ⚡ 分钟级数据库部署，支持 SQL、CLI、Terraform、Cursor、Claude Code 管理
- 🔌 与主流云提供商及 PostgreSQL 生态系统无缝集成
- 🏢 企业级支持：SLA 保障、区域数据隔离、24/7 全球专家支持

---

### [billboard.js 4.0 发布：Canvas 渲染模式，整体基准测试速度提升 94.3%！ | 作者：Jae Sung Park | 2026 年 6 月 | Medium](https://netil.medium.com/billboard-js-4-0-release-canvas-rendering-mode-94-3-faster-overall-in-benchmark-894b18798ffe)

**原文标题**: [billboard.js 4.0 release: Canvas rendering mode, 94.3% faster overall in benchmark! | by Jae Sung Park | Jun, 2026 | Medium](https://netil.medium.com/billboard-js-4-0-release-canvas-rendering-mode-94-3-faster-overall-in-benchmark-894b18798ffe)

billboard.js 4.0 版本发布，主要带来 Canvas 渲染模式、性能大幅提升和更轻量的 ESM 模块支持。

- 🚀 **Canvas 渲染模式**：新增可选 Canvas 渲染，处理数万数据点时性能显著优于传统 SVG，支持多种图表类型和交互功能。
- ⚡ **性能提升 94.3%**：基准测试显示，Canvas 模式比 3.18 版本整体快 94.3%，SVG 路径也快了 47.4%。
- 🎨 **Canvas 主题选择器**：提供`canvas.theme.selectors`映射 SVG 选择器到 Canvas 绘制样式，方便迁移。
- 📦 **更小的 ESM 包**：分离可选 API（如 exportApi、flow 等）为独立模块，最小化条形图 ESM 包可减小约 19KB（压缩后 6.3KB）。
- 🔧 **ESM 迁移注意**：使用 chart.export() 等 API 时需导入并调用对应解析器，否则会报错。
- 📚 **文档更新**：提供详细发布说明、变更日志和模块导入指南，方便用户升级。

---

### [billboard.js - 示例](https://naver.github.io/billboard.js/demo/)

**原文标题**: [billboard.js - examples](https://naver.github.io/billboard.js/demo/)

以下是基于您提供的 billboard.js 页面内容的概述和要点总结：

📊 billboard.js 是一个支持多种图表类型的 JavaScript 图表库，提供丰富的示例和可编辑代码功能。

- 📚 **API 文档与 GitHub 链接**：提供详细的 API 文档和 GitHub 仓库，方便开发者查阅和贡献。
- 🎨 **多主题支持**：内置 default、datalab、dark、insight、graph、modern 等多种主题，可灵活切换。
- 🖼️ **渲染方式**：支持 SVG 和 Canvas 两种渲染模式，满足不同性能需求。
- 📋 **丰富的图表类型**：涵盖 Area、Bar、Bubble、Candlestick、Donut、Gauge、Line、Pie、Polar、Radar、Scatter、Spline、Treemap 等 17 种图表。
- 💻 **可编辑代码示例**：提供 JS/TS 代码示例，用户可直接编辑并运行，支持复制到剪贴板。
- 🔗 **ESM 导入示例**：提供 ESM 模块导入的使用示例链接，方便现代前端项目集成。

---

### [billboard.js - 示例](https://naver.github.io/billboard.js/demo/#Chart.DonutChart)

**原文标题**: [billboard.js - examples](https://naver.github.io/billboard.js/demo/#Chart.DonutChart)

overview summary  
billboard.js 是一个图表库，提供丰富的图表类型和交互功能，支持通过代码编辑实时尝试。

- 📊 支持多种图表类型：面积图、面积范围图、条形图、气泡图、烛台图、组合图、甜甜圈图、漏斗图、仪表图、折线图、饼图、极地图、雷达图、散点图、样条图、堆叠条形图、阶梯图、树图  
- 🎨 提供多种主题：默认、数据实验室、暗色、洞察、图形、现代  
- 🖼️ 支持渲染模式：SVG 和 Canvas  
- 🛠️ 提供代码编辑器：可实时编辑 JS/TS 代码并查看效果  
- 📋 示例代码可复制到剪贴板，方便使用  
- 🔗 提供 ESM 导入用法链接，便于模块化开发  
- 📁 左侧菜单列出所有示例，便于浏览

---

### [billboard.js - 示例](https://naver.github.io/billboard.js/demo/#Chart.FunnelChart)

**原文标题**: [billboard.js - examples](https://naver.github.io/billboard.js/demo/#Chart.FunnelChart)

以下是基于您提供内容的概述总结和要点：

billboard.js 是一款图表库，提供丰富的图表类型和示例代码，支持多种主题和渲染方式。

- 📊 支持多种图表类型：Area、Bar、Bubble、Candlestick、Combination、Donut、Funnel、Gauge、Line、Pie、Polar、Radar、Scatter、Spline、Stacked Bar、Step、Treemap 等
- 🎨 提供多种主题：default、datalab、dark、insight、graph、modern
- 🖼️ 支持 SVG 和 Canvas 两种渲染方式
- 💻 提供 JS 和 TS 示例代码，可直接编辑运行
- 📚 左侧菜单列出所有示例，方便探索
- 🔗 包含 API 文档和 GitHub 链接，便于深入学习
- 📋 支持复制代码到剪贴板，方便使用

---

### [billboard.js - 示例](https://naver.github.io/billboard.js/demo/#BarChartOptions.BarOverlap)

**原文标题**: [billboard.js - examples](https://naver.github.io/billboard.js/demo/#BarChartOptions.BarOverlap)

概述摘要  
- 📊 billboard.js 提供丰富的图表类型，包括面积图、条形图、气泡图、烛台图、组合图、甜甜圈图、漏斗图、仪表图、折线图、饼图、极地图、雷达图、散点图、样条图、堆叠条形图、阶梯图和树状图。  
- 🎨 支持多种主题（默认、数据实验室、暗色、洞察、图形、现代）和渲染方式（SVG 或 Canvas）。  
- 🛠️ 提供代码编辑器，用户可直接编辑示例代码（JS 或 TS）并实时查看效果。  
- 📋 左侧菜单列出所有示例，方便浏览和选择。  
- 🔗 提供 API 文档和 GitHub 链接，并附有 ESM 导入使用示例的参考链接。

---

### [billboard.js - 示例](https://naver.github.io/billboard.js/demo/#RadarChartOptions.RadarAxis)

**原文标题**: [billboard.js - examples](https://naver.github.io/billboard.js/demo/#RadarChartOptions.RadarAxis)

以下是 billboard.js 示例页面的内容总结：

📊 billboard.js 是一个图表库，提供丰富的图表类型和示例。

- 🎨 支持多种主题：default、datalab、dark、insight、graph、modern
- 🖼️ 渲染方式可选：SVG 或 Canvas
- 📋 图表类型包括：面积图、面积范围图、条形图、气泡图、蜡烛图、组合图、甜甜圈图、漏斗图、仪表图、折线图、饼图、极地图、雷达图、散点图、样条图、堆叠条形图、阶梯图、树状图
- 💻 提供可编辑的示例代码，支持 JS 和 TS 两种语言
- 📁 可通过左侧菜单浏览所有示例
- 🔗 提供 ESM 导入使用示例的链接
- 📋 支持复制代码到剪贴板

---

### [PolyCSS - 面向 DOM 的 CSS 3D 引擎](https://polycss.com/)

**原文标题**: [PolyCSS - CSS 3D Engine for the DOM](https://polycss.com/)

PolyCSS 是一种无需 WebGL 或 Canvas 即可在 DOM 中渲染带纹理 3D 网格的技术，每个多边形都是真实的 DOM 元素。

- 🎨 支持 OBJ、glTF、GLB 和 MagicaVoxel VOX 文件，包括 UV 纹理和材质颜色
- 🖥️ 兼容原生 JS、React 和 Vue，提供 npm 包和 CDN 使用方式
- 🔧 每个多边形成为独立 DOM 元素，可通过 CSS 定位、添加点击事件和动画
- 🏗️ 使用自定义元素（如 `<poly-camera>`、`<poly-scene>`、`<poly-mesh>`）构建 3D 场景
- 🚀 浏览器合成器处理 3D 分层，无需 Shadow DOM 或 WebGL 上下文
- 📦 支持包管理器安装（npm）和 CDN 脚本引入
- 🛠️ 提供 Hello World 示例，展示在 vanilla JS、React 和 Vue 中的基本用法

---

### [画廊 | PolyCSS](https://polycss.com/gallery/)

**原文标题**: [Gallery | PolyCSS](https://polycss.com/gallery/)

这是一个包含多个功能模块的导航页面，涵盖工具、资源、社区和娱乐功能。
- 🏠 首页：提供网站或应用的入口
- 🛠️ 使用指南：帮助用户了解如何操作
- 🔗 API 接口：提供程序化访问功能
- 📚 参考文档：包含详细的技术说明
- 🖼️ 画廊：展示图片或作品示例
- 🧱 构建工具：用于创建或定制内容
- ✨ 艺术字：生成装饰性文字效果
- 📺 电视功能：可能指媒体播放或直播
- 🐙 GitHub：代码托管与协作平台
- ⭐ 收藏功能：用于标记重要内容

---

### [构建器 | PolyCSS](https://polycss.com/builder/)

**原文标题**: [Builder | PolyCSS](https://polycss.com/builder/)

该页面是一个功能导航总览，提供了多种工具和资源入口。

- 🏠 首页：网站的主页入口
- 🛠️ 使用指南：介绍如何使用相关功能
- 🔌 API 接口：提供程序化调用接口
- 📚 参考文档：详细的参考资料
- 🖼️ 画廊：展示作品或模板示例
- 🧩 构建器：用于创建或自定义内容
- ✨ 艺术字：文字特效设计工具
- 📺 电视模式：大屏显示或演示功能
- 💻 GitHub：开源代码仓库链接
- ⭐ 收藏：用户标记的喜爱内容

---

### [Tabulator | JavaScript 表格与数据网格](https://www.tabulator.info/)

**原文标题**: [Tabulator | JavaScript Tables & Data Grids](https://www.tabulator.info/)

Tabulator 是一个功能丰富、易于使用的 JavaScript 表格库，支持交互式数据展示和编辑，兼容所有主流浏览器和前端框架。

- 📊 **简单易用**：只需几行 HTML 和 JavaScript 代码即可创建功能完整的表格
- 🌐 **跨浏览器支持**：兼容所有现代桌面和移动浏览器
- 🔗 **框架兼容**：作为纯 JavaScript 库，支持所有前端框架，并提供框架设置指南
- 🎯 **丰富功能**：包含过滤、排序、格式化、分组、Ajax 加载、编辑、回调等大量功能
- ⚡ **虚拟 DOM**：通过虚拟化 DOM 实现大数据集的快速渲染
- 🎨 **CSS 样式**：所有图形元素都分配了 CSS 类，支持完全自定义样式
- 📱 **响应式设计**：支持响应式布局、触摸友好和 RTL 文本方向
- 📋 **数据操作**：支持分页、行选择、数据下载（CSV/XLSX）、剪贴板操作
- 🔄 **高级特性**：历史记录、撤销/重做、列计算、输入验证、树形结构、多表连接
- 🗂️ **主题与本地化**：提供 5 个预打包主题，支持多语言本地化

---

### [GitHub - github/relative-time-element: 标准<time>元素的 Web 组件扩展。](https://github.com/github/relative-time-element)

**原文标题**: [GitHub - github/relative-time-element: Web component extensions to the standard <time> element. · GitHub](https://github.com/github/relative-time-element)

这是一个 GitHub 上的开源项目 `<relative-time>` 元素，它是一个 Web 组件，用于将时间戳格式化为本地化字符串或相对文本，并能在浏览器中自动更新。

- 📅 **核心功能**：将服务器缓存的日期时间，在浏览器端自动转换为用户本地时区和语言格式的相对或绝对时间文本。
- 🔄 **自动更新**：时间文本会根据当前时间自动刷新，例如显示“3 分钟前”或“20 天后”，超过阈值（默认 30 天）则显示完整日期。
- ⚙️ **丰富属性**：支持 `datetime`、`format`（datetime/relative/duration）、`tense`、`precision`、`threshold`、`time-zone` 等多种自定义配置。
- 🌐 **国际化支持**：利用 `Intl.DateTimeFormat` 和 `Intl.RelativeTimeFormat` API，自动适配用户浏览器语言和时区。
- 🧩 **易于集成**：可通过 npm 安装 `@github/relative-time-element`，支持原生 HTML 和 React 项目使用。
- 🎨 **样式定制**：通过 CSS `::part(root)` 伪元素可自定义内部文本样式。
- 🛡️ **降级友好**：若浏览器禁用 JavaScript，仍显示服务器提供的默认日期文本。
- 📦 **开源许可**：采用 MIT 许可证，拥有 4k Star、187 Fork，社区活跃。

---

### [发布 5.2.0 · fable-compiler/Fable · GitHub](https://github.com/fable-compiler/Fable/releases/tag/5.2.0)

**原文标题**: [Release 5.2.0 · fable-compiler/Fable · GitHub](https://github.com/fable-compiler/Fable/releases/tag/5.2.0)

Fable 编译器发布 5.2.0 版本，新增对 Erlang/BEAM 目标平台的支持，并修复了多个语言后端的错误。

- 🚀 新增功能：在独立编译器中支持 Erlang/BEAM 目标平台
- 🐞 修复错误：优化 BEAM 后端中数组字面量与进程字典的往返调用
- 🐞 修复错误：确保 BEAM 后端的 Emit $N 替换为单次从左到右传递
- 🐞 修复错误：在 JS/TS 后端的 jsOptions 中尝试设置非属性成员时抛出错误
- 🐞 修复错误：拒绝 .NET TryParse 不接受的 JS 宽松日期字符串
- 🐞 修复错误：使 Exception.ToString() 返回消息而非 "Exception"
- 🐞 修复错误：避免 Python 后端中联合类型字段名与 Union.name 冲突
- 🐞 修复错误：使 Python 后端中 [] 联合静态成员正常工作

---

### [寓言 · 你可以引以为傲的 JavaScript！](https://fable.io/)

**原文标题**: [Fable · JavaScript you can be proud of!](https://fable.io/)

这段代码定义了一个简单的扑克牌类型系统，并展示了模式匹配的用法。

- 🃏 定义了扑克牌的面值类型：Ace、King、Queen、Jack，以及用数字表示的其他牌
- ♠️ 定义了花色类型：Spades、Hearts、Diamonds、Clubs
- 🎴 通过组合面值和花色创建了 Card 类型，例如 aceOfHearts 和 tenOfSpades
- 🔍 使用 match 表达式对 card 进行模式匹配，根据不同组合输出对应信息
- ⚠️ 模式匹配不完整，编译器警告可能遗漏了某些情况，例如 (_,Spades) 未被覆盖

---

### [React Native 0.86 - 全屏显示与开发者工具改进，无破坏性变更 · React Native](https://reactnative.dev/blog/2026/06/11/react-native-0.86)

**原文标题**: [React Native 0.86 - Edge-to-Edge and DevTools Improvements, no breaking changes · React Native](https://reactnative.dev/blog/2026/06/11/react-native-0.86)

React Native 0.86 发布，带来 Android 15+ 全面边到边支持和 DevTools 改进，无破坏性变更。

- 🏠 React Native 仓库已迁移至 react 组织，所有链接自动重定向
- 📱 Android 15+ 边到边模式全面修复，包括 measureInWindow、KeyboardAvoidingView 等关键组件
- 🎨 DevTools 新增明暗模式模拟，可通过命令面板临时切换
- ✅ 无用户端破坏性变更，0.85 用户可直接升级
- ⚠️ 废弃 ViewUtil.getUIManagerType 和 AppRegistry 部分参数
- 🔧 修复 PerformanceObserver 默认阈值、Modal 样式转发、动画同步闪烁等问题
- 🛠️ 新增 JSI API 支持类型数组、数组扩展、错误创建等
- 📱 Android 修复 BackHandler、TextInput、Image 等多项问题
- 🌐 网络模块修复大响应 OOM、WebSocket Cookie 头、Blob 新架构支持
- 🙏 感谢 97 位贡献者的 596 个提交

---

### [Biome v2.5——500 条代码规范规则、插件代码修复及跨文件代码检查 | Biome](https://biomejs.dev/blog/biome-v2-5/)

**原文标题**: [Biome v2.5—500 Lint Rules, Plugin Code Fix, and Cross-File Linting | Biome](https://biomejs.dev/blog/biome-v2-5/)

Biome v2.5 版本发布，新增 500 条 lint 规则、插件代码修复功能及跨文件 lint 能力，并带来多项性能优化和新特性。

- 🎯 突破 500 条 lint 规则里程碑，新增跨语言 lint 规则（如 noUndeclaredClasses 和 noUnusedClasses），可分析 CSS 类在 HTML/JSX 文件中的使用情况
- 🔧 插件系统增强：支持按路径应用插件（includes 配置）和声明代码修复（=>符号），修复可标记为 safe 或 unsafe
- ✨ 新增 73 条稳定规则，涵盖正确性、可疑、风格、复杂度、性能、安全、无障碍等分组，部分规则更名
- 🖊️ 新增 delimiterSpacing 格式化选项，在分隔符（括号、方括号等）内添加空格，有助于阅读障碍者
- 👀 为 lint/format/check 命令添加--watch 监视模式，实时检测文件变化并输出诊断
- 🔍 LSP 支持“转到定义”功能，可解析 JS 变量/类型、JSX 组件、CSS 类等定义位置
- ⚙️ 新增 linter.rules.preset 选项（含 all 预设），废弃 recommended 选项，提供 biome migrate 迁移命令
- 🚀 性能提升约 13%，新增.svg 文件格式化/lint 支持、concise 简洁报告器、organizeImports 排序增强等
- 📦 新增 biome upgrade 升级命令，支持 Homebrew 和手动安装更新
- 🤝 欢迎社区贡献：翻译网站、加入 Discord、代码贡献（创建 lint 规则、构建解析器、改进 LSP）、财务支持

---

### [GitHub - jonschlinkert/get-value: 使用属性路径（`a.b.c`）从对象中获取嵌套值。](https://github.com/jonschlinkert/get-value)

**原文标题**: [GitHub - jonschlinkert/get-value: Use property paths (`a.b.c`) get a nested value from an object. · GitHub](https://github.com/jonschlinkert/get-value)

get-value 是一个用于从对象中获取嵌套值的 JavaScript 库，支持点号路径，即使键名包含点号也能正确处理。

- 📦 **安装简便**：通过 `npm install --save get-value` 即可安装，支持 ES 模块和 CommonJS 两种导入方式。
- 🔍 **核心功能**：使用 `a.b.c` 这样的属性路径，从对象中安全地获取深层嵌套的值。
- 🎯 **支持点号键名**：与其他库不同，即使键名本身包含点号（如 `'a.b'`），也能正确解析路径。
- 📊 **支持数组**：可以通过数字索引访问数组元素，例如 `e.1.f` 或 `a.b.0.c`。
- 🧩 **支持函数**：可以获取函数对象上的属性值，如 `foo.bar.baz`。
- ⚙️ **灵活选项**：提供 `default`（默认值）、`isValid`（验证函数）、`split`（自定义分割）、`separator`（分隔符）、`join`（自定义连接）和 `joinChar`（连接字符）等配置。
- 🚀 **性能优异**：在深度和根路径基准测试中，速度比其他库快 56-65%，浅层测试中仅次于 dot-prop。
- 📝 **版本更新**：v4.1.0 支持 Map 类对象，v4.0.0 重构为 TypeScript 并改进数组处理，v3.0.0 增强转义和选项功能。
- 🔗 **相关项目**：与 has-value、set-value、unset-value 等库协同使用，构成完整的对象操作工具集。

---

### [发布 v1.18.0 · axios/axios · GitHub](https://github.com/axios/axios/releases/tag/v1.18.0)

**原文标题**: [Release v1.18.0 · axios/axios · GitHub](https://github.com/axios/axios/releases/tag/v1.18.0)

Axios v1.18.0 版本发布，重点强化了安全性与稳定性，并修复了若干问题。

- 🔒 安全增强：新增 Node HTTP 适配器支持，跨域重定向时自动剥离敏感请求头（如 API 密钥），防止信息泄露；同时强化 URL 校验，拒绝缺少 "//" 的畸形 http/https 请求，并收紧原型污染防护、流大小限制等。
- 🐛 错误修复：引入 `transitional.validateStatusUndefinedResolves` 配置，允许将 `validateStatus: undefined` 视为未设置选项，而 `validateStatus: null` 仍表示接受所有状态码。
- 📚 文档更新：发布 v1.17.0 发布说明、修正更新日志错字、明确包更新 PR 策略，并在高级文档中标注 `proxy` 请求配置仅适用于 Node.js。
- 🔧 依赖升级：更新多个核心依赖，包括 `@babel/core`、`eslint`、`rollup`、`vitest` 等，提升开发工具链兼容性。
- 🌟 新贡献者：欢迎 @drori12、@eyupcanakman 和 @Adi-Beker 加入项目，共同改进 axios。

---

### [未找到标题](https://visx.airbnb.tech/)

**原文标题**: [No title found](https://visx.airbnb.tech/)

概述摘要  
- 📖 文章主要探讨了人工智能在医疗领域的应用现状与未来潜力，强调其能提升诊断准确性和效率。  
- 🩺 通过分析大量医疗数据，AI 可辅助医生识别疾病模式，尤其在影像诊断中表现突出。  
- ⚠️ 但 AI 应用仍面临数据隐私、算法偏见和监管挑战，需要谨慎推进。  
- 🔬 未来趋势包括个性化治疗方案开发，以及 AI 与可穿戴设备的结合，实现实时健康监测。  
- 🌍 全球合作与伦理规范制定是确保 AI 医疗安全、公平发展的关键。

---

### [STRICH | 网页应用的条码扫描](https://strich.io/?ref=js-weekly)

**原文标题**: [STRICH | Barcode Scanning for Web Apps](https://strich.io/?ref=js-weekly)

STRICH 是一个基于 JavaScript 的网页端条码扫描库，支持实时扫描 1D/2D 条码，无需原生应用或后端。

- 📱 **实时扫描**：直接在浏览器中扫描条码，支持 JavaScript/WASM，兼容所有主流框架。
- 💰 **透明定价**：无大额预付，可随时取消，提供 30 天免费试用。
- 🚀 **高性能**：用户反馈扫描速度极快，甚至在高端设备上条码未完全进入画面即被解码。
- 🌐 **Web 优势**：无需应用商店，通过链接或二维码分发，降低开发成本，避免应用疲劳。
- 🔍 **广泛兼容**：支持 Code 128、EAN、QR Code、Data Matrix 等多种条码类型。
- 🛠️ **高级图像处理**：可读取褪色、损坏、光照不均或反转的条码，优于 ZXing-JS 和 Quagga。
- 🏢 **企业级功能**：定期更新、技术支持、白标定制、离线操作，符合 GS1 标准。
- 💵 **定价方案**：BASIC（$99/月，10k 次扫描）、PROFESSIONAL（$249/月，100k 次扫描）、ENTERPRISE（按需报价）。
- ❓ **常见问题**：支持所有框架，超出扫描限制不会拒绝，提供免费更新和试用 Demo。

---

### [Meticulous AI - 无需编写测试的自动化前端测试](https://www.meticulous.ai/?utm_source=jsweekly&utm_medium=referral&utm_campaign=26q2&utm_content=classified)

**原文标题**: [Meticulous AI - Automated Frontend Testing Without Writing Tests](https://www.meticulous.ai/?utm_source=jsweekly&utm_medium=referral&utm_campaign=26q2&utm_content=classified)

Meticulous 是一款自动化、穷尽且确定性的测试工具，专为复杂代码库设计，让开发者无需手动编写或维护测试，即可高速交付可靠代码。

- 🚀 零开发者精力投入：自动生成并维护测试套件，覆盖所有用户流程和边缘情况，无需编写、修复或维护测试。
- 🎯 穷尽且确定性：从 Chromium 级别构建确定性调度引擎，消除所有不稳定测试，实现闪电般快速的测试执行。
- 🧪 自动化测试演进：测试随应用自动更新，新功能或边缘情况出现时自动添加测试，过时测试自动移除。
- 🔍 PR 影响预览：在合并前即可看到代码变更对用户工作流的影响，通过模拟后端响应避免假阳性。
- ⚡ 高速迭代：大规模并行测试，1000 个屏幕可在 120 秒内获得结果，大幅提升交付速度。
- 🔗 灵活集成：可与现有测试套件配合使用或完全替代，支持 NextJS、React、Vue、Angular 等主流框架。
- 🛡️ 安全可靠：受超过 100 个组织信任，包括 Dropbox 和 Notion 等知名企业，开发者反馈“无法想象没有它”。

---

### [文档生成 API：规模化自动化创建个性化文档 - 福昕](https://developer-api.foxit.com/developer-blogs/api-guides-tutorials/document-generation-api-automate-creation/?utm_source=draftdev&utm_medium=referral&utm_campaign=jsweekly_20260616)

**原文标题**: [Document Generation API: Automate Personalized Document Creation at Scale - Foxit](https://developer-api.foxit.com/developer-blogs/api-guides-tutorials/document-generation-api-automate-creation/?utm_source=draftdev&utm_medium=referral&utm_campaign=jsweekly_20260616)

本文档解释了文档生成的工作原理，重点介绍如何通过模板驱动 API 替代手动流程，并详细说明从 Word 模板和 JSON 数据到最终 PDF 的完整流水线。

- 📄 **文档生成定义**：文档生成是将数据与模板结合，自动创建结构化文档（如 PDF、Word）的过程，适用于合同、报告等高频场景。
- ⚙️ **模板驱动 API 核心**：通过 API 将 Word 模板与 JSON 数据动态合并，无需人工干预，实现大规模文档的快速生成。
- 🔄 **流水线步骤**：从 Word 模板（含占位符）和 JSON 数据输入开始，经解析、数据填充、格式渲染，最终输出 PDF 文件。
- 🚀 **优势**：消除手动复制粘贴错误，支持批量处理，显著提升效率，尤其适合企业级文档管理需求。

---

### [探索 MapKit JS 6：为现代 Web 开发者重建 | WebKit](https://webkit.org/blog/18027/discover-mapkit-js-6-rebuilt-for-todays-web-developer/)

**原文标题**: [  Discover MapKit JS 6: Rebuilt for Today’s Web Developer | WebKit](https://webkit.org/blog/18027/discover-mapkit-js-6-rebuilt-for-todays-web-developer/)

MapKit JS 6 针对现代网页开发者进行了重构，简化了集成流程，支持 npm 包加载、静态令牌和标准浏览器事件模型，让在网页中嵌入 Apple 地图更加便捷。

- 🗺️ **快速上手**：只需几行代码即可在网页中嵌入交互式 Apple 地图，支持自定义中心坐标和相机距离。
- 🔑 **简化令牌配置**：v6 支持静态域名绑定令牌，无需管理私钥或自签名，直接从 Apple Developer 网站生成。
- 📦 **NPM 包集成**：MapKit JS 加载器现以 npm 包形式提供，无缝融入现代构建流程，并自动支持 TypeScript。
- 🏷️ **PlaceAnnotation 增强**：新增 PlaceAnnotation 注解，基于 Place ID 自动获取地点标题、坐标和图标，支持 Promise 异步加载。
- 🖱️ **标准事件模型**：v6 采用浏览器标准 EventTarget 模型，通过 `addEventListener` 处理地图交互（如注解选择），实现双向绑定。
- 🎨 **按需加载库**：MapKit JS 将功能划分为多个库（如 map、services、annotations），仅加载所需部分以优化性能。
- 📱 **框架兼容性**：支持直接传递 DOM 元素给 UI 框架（如 React），通过 ref 轻松集成。
- 📚 **丰富资源**：提供详细文档、迁移指南和示例代码，并通过 Feedback Assistant 收集反馈。

---

### [约塞米蒂探险者](https://webkit.org/demos/yosemite/)

**原文标题**: [Yosemite Explorer](https://webkit.org/demos/yosemite/)

优胜美地国家公园概览：探索标志性峡谷、古老红杉和花岗岩峰，通过实时兴趣点规划游览。
- 🗺️ 公园地图提供卫星视图，覆盖加利福尼亚州优胜美地国家公园
- 🌲 探索标志性峡谷、古老红杉林和花岗岩山峰
- 📍 实时兴趣点功能帮助游客规划行程
- 🚗 支持导航至公园内各主要景点

---

### [LinkedIn 工作邀请中的后门 - Roman Imankulov](https://roman.pt/posts/linkedin-backdoor/)

**原文标题**: [A backdoor in a LinkedIn job offer - Roman Imankulov](https://roman.pt/posts/linkedin-backdoor/)

### 概述总结
一名 Python 开发者通过 LinkedIn 收到伪装成招聘测试的恶意代码仓库，其中隐藏了自动执行的后门程序，攻击者利用伪造身份和社交工程手段诱骗受害者运行恶意代码。

- 🔍 **发现后门**：开发者使用只读 AI 工具审查代码时，在伪装成测试脚本的文件中发现恶意 URL 拼接和远程代码执行逻辑
- ⚠️ **触发机制**：后门通过 npm 的`prepare`脚本在`npm install`时自动执行，无需手动运行测试文件
- 🕵️ **身份盗用**：GitHub 提交记录和 LinkedIn 招聘者身份均盗用真实人物（一名工程师和一名文化记者）
- 🛡️ **防御建议**：对陌生代码仓库保持警惕，使用沙箱环境审查代码，避免直接运行`npm install`
- 🤖 **技术启示**：使用只读 AI 工具审查代码比人工阅读更高效，能快速识别伪装成新手代码的恶意内容

---

### [字节码联盟 — WASI 0.3 发布](https://bytecodealliance.org/articles/WASI-0.3)

**原文标题**: [Bytecode Alliance — WASI 0.3 Launched](https://bytecodealliance.org/articles/WASI-0.3)

WASI 0.3 正式发布，将异步支持原生集成到 WebAssembly 组件模型中，大幅简化了接口并提升了性能。

- 🚀 **异步原生支持**：WASI 0.3 将异步操作纳入组件模型规范，由宿主运行时统一管理事件循环，取代了 WASI 0.2 中每个组件各自运行事件循环的碎片化方式。
- 📦 **核心抽象简化**：WASI 0.2 中的 `pollable`、`input-stream`、`output-stream` 等资源类型被组件模型的 `stream<T>`、`future<T>` 和 `async func` 替代，接口签名更简洁，且流状态问题（如提前停止读取无法区分关闭与错误）得到解决。
- 🌐 **语言绑定原生异步**：绑定生成器可生成符合语言习惯的异步绑定，例如 Rust 中 `async fn handle`、Go 中通过 goroutine 实现并发，无需手动处理回调或轮询。
- ⚡ **性能飞跃**：`wasi:http` 新增 `middleware` 世界，支持服务链式组合，微服务间通信可从毫秒级降至纳秒级（六数量级提升）。
- ✅ **稳定与生态就绪**：规范已通过 WASI 子组投票，Wasmtime 46 默认启用，Jco 即将发布默认支持版本，Rust、Go、JavaScript、Python 等语言工具链正在适配中。

---

### [performative-ui | AI 原生 React 组件](https://vorpus.github.io/performativeUI/)

**原文标题**: [performative-ui | AI-native React Components](https://vorpus.github.io/performativeUI/)

概述：本文探讨了人工智能在医疗领域的最新应用，包括诊断辅助、药物研发和个性化治疗，同时强调了数据隐私和伦理挑战。

- 🩺 人工智能通过分析医学影像（如 X 光片和 CT 扫描）辅助医生提高诊断准确率，尤其在早期癌症检测中表现突出。
- 💊 在药物研发方面，AI 加速了候选药物的筛选过程，通过模拟分子相互作用缩短了传统研发周期。
- 🧬 个性化治疗利用 AI 分析患者基因和病史数据，制定更精准的医疗方案，提升治疗效果。
- 🔒 数据隐私成为关键问题，医疗 AI 系统需确保患者信息的安全存储与合规使用，防止泄露风险。
- ⚖️ 伦理挑战包括算法偏见和决策透明度，需建立监管框架确保 AI 在医疗中的公平性和可解释性。

---

### [performative-ui | AI 原生 React 组件](https://vorpus.github.io/performativeUI/#/components/ascii-hero)

**原文标题**: [performative-ui | AI-native React Components](https://vorpus.github.io/performativeUI/#/components/ascii-hero)

概述摘要：本文探讨了人工智能在医疗领域的应用进展，强调了其在诊断、治疗和患者管理中的潜力，同时指出了数据隐私和伦理挑战。

- 🩺 人工智能通过分析医学影像，显著提高了疾病诊断的准确性和效率。
- 💊 在个性化治疗中，AI 能根据患者数据推荐最优药物方案，减少副作用。
- 📊 通过实时监测患者健康数据，AI 助力慢性病管理和早期预警。
- 🔒 数据隐私问题成为主要挑战，需加强安全措施以保护患者信息。
- ⚖️ 伦理争议包括算法偏见和决策透明度，需制定严格监管框架。

---

### [performative-ui | AI 原生 React 组件](https://vorpus.github.io/performativeUI/#/components/node-graph)

**原文标题**: [performative-ui | AI-native React Components](https://vorpus.github.io/performativeUI/#/components/node-graph)

概述总结  
- 📚 本文主要讨论了如何通过高效的学习方法提升知识吸收能力，强调主动学习与重复练习的重要性。  
- 🧠 提出“费曼技巧”，即用简单语言解释复杂概念，以检验理解深度。  
- ⏰ 建议采用“番茄工作法”，通过 25 分钟专注学习与 5 分钟休息的循环提高效率。  
- 🗂️ 强调知识结构化，使用思维导图或笔记整理信息，便于长期记忆。  
- 🔄 提倡定期复习与自我测试，利用间隔重复巩固学习成果。  
- 💡 指出学习环境与心态的影响，鼓励保持好奇心与积极反馈循环。

---

### [是的，我们扫描：背景故事与工作原理](https://yes-we-scan.app/details)

**原文标题**: [Yes We Scan: backstory and how it works](https://yes-we-scan.app/details)

概述总结
- 📟 介绍"yes-we-scan.app"：一款让旧 USB 扫描仪在现代浏览器中正常工作的网络应用
- 🖨️ 灵感来源：作者此前为旧 Canon 照片打印机开发了"printervention.app"，类似技术可应用于扫描仪
- ⚙️ 核心技术：使用 v86 在浏览器中模拟 x86 CPU 和完整机器，将机器码实时编译为 WebAssembly 模块
- 🖥️ 运行机制：在模拟机上运行 SANE（扫描仪访问工具）和 Alpine Linux，通过小型 C 程序连接浏览器与 SANE
- 🔄 数据处理：扫描数据在浏览器中直接写入<canvas>预览，或通过 Web Worker 压缩为 JPEG/PNG
- 🔗 USB 桥接：通过 USB/IP 协议、tcpip.js 和 WebUSB API，实现模拟机与物理扫描仪的 USB 通信
- 🗓️ 兼容性：已测试 Canon LiDE 100，理论上支持数百种型号（包括 Agfa、Epson、HP 等品牌）
- 🔒 开源状态：作者暂未开源代码，但鼓励用户尝试并反馈

---

### [printervention.app：背景故事与工作原理](https://printervention.app/details)

**原文标题**: [printervention.app: backstory and how it works](https://printervention.app/details)

### 概述总结
本文介绍了如何通过一个名为 printervention.app 的网页应用，让老旧 USB 打印机在现代电脑上重新工作，并详细说明了其技术实现原理和开发历程。

- 📸 **意外获得旧打印机**：作者从朋友那里得到一台佳能 SELPHY 照片打印机，发现它无法在 Mac 和 Windows 上使用，但在 Linux 上可以正常工作。
- 🐧 **Linux 共享打印方案**：通过 CUPS、Gutenprint 和 Avahi 在 Linux 上设置 AirPrint 共享，让全家人都能轻松打印照片。
- 💡 **从原生应用到网页应用**：最初尝试开发 Mac 原生应用，但最终选择使用 WebUSB 技术开发跨平台的网页应用，无需安装即可使用。
- 🖥️ **核心技术：浏览器内虚拟机**：利用 v86 在浏览器中模拟 x86 环境，运行 Alpine Linux 和 CUPS，通过 WebUSB 连接打印机。
- 🔄 **双向数据桥接**：通过 USB/IP 和 tcpip.js 实现浏览器与虚拟机之间的双向 USB 通信，让 CUPS 能实时监控打印机状态。
- 🛠️ **解决实际打印问题**：针对照片尺寸适配、HEIC 格式转换、EXIF 方向数据等问题进行了专门优化。
- 🌐 **未来展望**：该应用目前仅测试了少数照片打印机，但有望支持更多 Gutenprint 兼容的打印机型号，并计划增加更多 PPD 驱动包支持。

---

