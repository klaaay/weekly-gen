### [JavaScript 周刊第 739 期：2025 年 6 月 6 日](https://javascriptweekly.com/issues/739)

**原文标题**: [JavaScript Weekly Issue 739: June 6, 2025](https://javascriptweekly.com/issues/739)

概述总结  
本期内容涵盖 JavaScript 生态的最新动态，包括工具更新、提案进展、教程资源及赞助商推广。  

- ✈️ 编辑 Peter Cooper 因行程变更推出精简版通讯，承诺下周恢复完整版。  
- ⚡ Rolldown-Vite 发布：基于 Rust 的快速 JavaScript 打包工具，可显著减少构建时间。  
- 📜 TC39 会议进展：Array.fromAsync、Error.isError 等提案进入 Stage 4。  
- 🤖 CodeRabbit 推出免费 IDE 内 AI 代码审查工具，支持 VS Code 等平台。  
- 🌐 WebStatus.dev 更新：增强数据查询与浏览器兼容性追踪功能。  
- 🔧 简讯：React Native 冻结旧架构代码、SQLite-JS 扩展发布、State of CSS 2025 调查启动。  
- 🚀 版本发布：Babel 8 Beta、ESLint v9.28.0、AngularFire 20.0 等。  
- 📖 文章推荐：JavaScript 开发者 Go 语言入门指南、document.currentScript 实用技巧等。  
- ▶️ Svelte Summit 2025 演讲视频上线，Rich Harris 主题演讲为重点。  
- 🛠️ 工具更新：php-node（Node.js 运行 PHP）、Storybook 9（增强 UI 组件测试）。  
- 🏖️ Beachpatrol CLI 工具：通过 Playwright 实现浏览器自动化控制。

---

### [宣布 Rolldown-Vite | 归零](https://voidzero.dev/posts/announcing-rolldown-vite)

**原文标题**: [Announcing Rolldown-Vite | VoidZero](https://voidzero.dev/posts/announcing-rolldown-vite)

Rolldown-Vite 是一个基于 Rust 的新一代打包工具，旨在提升 Vite 的性能，现已达到与当前 Vite 版本的功能对等，可作为直接替代方案使用。早期测试显示，生产构建时间减少了 3 倍至 16 倍，内存使用量降低了高达 100 倍。未来，Rolldown 将成为 Vite 的默认打包工具。

- 🚀 **性能提升**：Rolldown-Vite 作为 Vite 的替代方案，可显著减少构建时间和内存使用。  
- 🔧 **简单替换**：通过修改 `package.json` 中的别名或覆盖依赖，即可轻松切换到 Rolldown-Vite。  
- ⚙️ **兼容性优先**：已通过 Vite 生态系统的兼容性测试，但部分高级用例可能存在兼容性问题。  
- 🛠️ **插件支持**：插件作者可立即测试其插件，部分插件可能需要调整以兼容或优化性能。  
- 📊 **实际效果**：早期用户报告构建时间大幅减少，如 GitLab 从 2.5 分钟降至 40 秒，内存使用减少 100 倍。  
- 🔮 **未来计划**：包括开发全捆绑模式的开发服务器，进一步优化性能，并分三个阶段将 Rolldown 整合到 Vite 中。  
- 📢 **鼓励尝试**：欢迎用户试用并提供反馈，以帮助改进 Rolldown-Vite。

---

### [卷下](https://rolldown.rs/)

**原文标题**: [Rolldown](https://rolldown.rs/)

Rolldown 能够高效处理数以万计的模块，表现出色且稳定。

- 🚀 高效处理 - 轻松应对数以万计的模块  
- 💪 稳定性能 - 运行流畅无压力  
- 🔧 模块支持 - 大规模模块管理能力突出

---

### [Vite | 下一代前端构建工具](https://vite.dev/)

**原文标题**: [Vite | Next Generation Frontend Tooling](https://vite.dev/)

Vite 是一个现代化的前端构建工具，提供快速、高效的开发体验。  

- 🚀 **快速开发** - Vite 提供极速的冷启动和热模块替换（HMR）。  
- 📂 **多语言支持** - 文档支持多种语言，包括中文、英文、日语等。  
- 🔧 **配置灵活** - 提供详细的配置指南和插件系统，方便定制。  
- 🌐 **社区资源** - 拥有活跃的社区，包括 Discord、Mastodon 等交流平台。  
- 📚 **版本文档** - 提供多个版本的文档，包括 Vite 2、3、4 和 5。  
- 🛠 **扩展功能** - 支持插件和 Awesome Vite 资源库，增强开发能力。  
- 📅 **持续更新** - 通过博客、发布日志和贡献指南保持项目活跃。

---

### [TC39 推进 Array.fromAsync、Error.isError 及显式资源管理等提案](https://socket.dev/blog/tc39-advances-9-proposals)

**原文标题**: [TC39 Advances Array.fromAsync, Error.isError, and Explicit R...](https://socket.dev/blog/tc39-advances-9-proposals)

Socket 现已支持 pylock.toml 文件，实现安全、可复现的 Python 构建，并与 PEP 751 新标准全面对齐。

- 🔒 Socket 新增对 pylock.toml 的支持  
- 🐍 提升 Python 构建的安全性和可复现性  
- 🔍 提供高级扫描功能  
- 📜 完全符合 PEP 751 新标准  
- 🚀 由 Trevor Norris 于 2025 年 6 月 5 日发布

---

### [WebStatus.dev：更多数据、更深洞察，更清晰迈向 Baseline 之路 | 博客 | web.dev](https://web.dev/blog/web-platform-dashboard-evolution?hl=en)

**原文标题**: [WebStatus.dev: Now with more data, deeper insights, and a clearer path to Baseline  |  Blog  |  web.dev](https://web.dev/blog/web-platform-dashboard-evolution?hl=en)

WebStatus.dev 平台进行了重大升级，新增了移动浏览器数据、更强大的筛选功能，并整合了社区需求，以更全面地追踪网页平台的互操作性和功能进展。

- 🌐 平台功能覆盖大幅扩展，现追踪超过 1000 项网页功能，接近全面覆盖。
- 📊 新增了自 2020 年以来 Chrome 功能的采用时间线数据，展示功能使用趋势。
- 📱 整合了移动浏览器数据，帮助识别尚未达到 Baseline 标准的功能。
- 🔍 强化了排序和筛选功能，支持保存和分享自定义查询视图。
- 🗣️ 整合了 State of CSS 和 State of HTML 调查中社区最需求的十大功能列表。
- 📈 新增平台级统计数据，展示主要浏览器支持的互操作性功能从 2020 年的 400 项增长到近 700 项。
- 🔎 新增“仅缺一款浏览器支持”功能视图，帮助预测即将实现的互操作性功能。
- 🚀 提供更丰富的发现工具和趋势洞察，成为前端开发者更不可或缺的资源。

---

### [网络平台状态](https://webstatus.dev)

**原文标题**: [Web Platform Status](https://webstatus.dev)

好的，请提供需要总结的文本内容，我会按照您要求的格式生成概述和带表情符号的要点列表。  

示例格式：  

这里是文章的概述总结，简明扼要地概括全文核心内容。  
- 🌟 第一个关键点，用简短的语言描述。  
- 📊 第二个关键点，涉及数据或重要细节。  
- 🔍 第三个关键点，可能是分析或深入观察。  

请提供您的文本内容，我会立即为您处理！

---

### [❄️ 冻结传统架构 · reactwg/react-native-new-architecture · 讨论 #290 · GitHub](https://github.com/reactwg/react-native-new-architecture/discussions/290)

**原文标题**: [❄️ Freezing the Legacy Architecture · reactwg/react-native-new-architecture · Discussion #290 · GitHub](https://github.com/reactwg/react-native-new-architecture/discussions/290)

React Native 团队宣布自 2025 年 6 月 2 日起冻结旧架构代码库，停止接受相关 PR 和新功能开发，全面转向新架构。  

- 🚀 **冻结旧架构**：自 6 月 2 日起，停止对旧架构的开发和 PR 合并，仅接受安全修复和严重问题修复。  
- 🔧 **开发重点转移**：所有新功能和修复将仅针对新架构，旧架构不再获得更新。  
- ⚠️ **测试调整**：发布新版本时不再测试旧架构，旧架构的稳定性将无法保证。  
- 📢 **迁移建议**：库维护者和应用开发者应尽快迁移至新架构，避免未来兼容性问题。  
- 🔄 **互操作层暂时保留**：目前仍可使用互操作层，但未来会被移除，建议提前迁移。  
- 📅 **时间节点**：React Native 0.81 起，新项目默认使用新架构，旧架构需自行承担风险。  
- 📹 **更多信息**：可参考 App.js Conf 2025 的相关演讲视频。

---

### [关于新架构·React Native](https://reactnative.dev/architecture/landing-page)

**原文标题**: [About the New Architecture · React Native](https://reactnative.dev/architecture/landing-page)

React Native 团队自 2018 年起重新设计了核心架构，以提升开发体验，新架构已在 Meta 的生产环境中验证，并逐步成为开源生态的默认选项。

- 🏗️ 新架构自 React Native 0.68 起支持实验性启用，持续优化后计划作为默认配置  
- 🔄 改造动机：旧架构存在底层设计限制，阻碍了高性能、精细化用户体验的实现  
- ⚡ 同步布局效果：新架构支持同步测量视图尺寸，避免视觉跳跃（如工具提示定位场景）  
- 🌐 并发渲染支持：兼容 React 18 特性（如 Suspense、Transitions），实现自动批处理减少渲染  
- 🚀 JSI 取代异步桥接：直接内存访问提升原生/JS 交互性能（如实时相机帧处理库 VisionCamera）  
- ⚠️ 启用提示：需代码适配新特性才能发挥优势，数据序列化可能非所有应用的性能瓶颈  
- 🔧 默认启用：0.76 版本起新项目自动启用，发现问题可通过模板提交 issue  
- ↩️ 回退选项：通过 gradle.properties(Android) 或 Podfile(iOS) 配置可关闭新架构

---

### [GitHub - sqliteai/sqlite-js: 用 JavaScript 创建自定义 SQLite 函数。直接在 JavaScript 中扩展数据库，支持标量、聚合、窗口函数和排序规则。](https://github.com/sqliteai/sqlite-js)

**原文标题**: [GitHub - sqliteai/sqlite-js: Create custom SQLite functions in JavaScript. Extend your database with scalars, aggregates, window functions, and collations directly in JavaScript.](https://github.com/sqliteai/sqlite-js)

SQLite-JS 是一个强大的扩展，允许在 SQLite 中使用 JavaScript 创建自定义函数、聚合函数、窗口函数和排序规则，从而直接在数据库中进行灵活的数据操作。

- 🚀 **功能概述**：SQLite-JS 支持标量函数、聚合函数、窗口函数和排序规则，扩展了 SQLite 的功能。
- 📥 **安装**：提供预编译的二进制文件，支持 Linux、macOS、Windows、Android 和 iOS 平台。
- 🔧 **标量函数**：处理单行数据并返回单个值，适用于数据转换和计算。
- 📊 **聚合函数**：处理多行数据并返回聚合结果，如计算中位数。
- 🖼️ **窗口函数**：访问多行数据而不折叠为单行，如计算移动平均值。
- 🔠 **排序规则**：定义自定义文本排序规则，如不区分大小写的自然排序。
- 🔄 **同步功能**：与 sqlite-sync 结合使用时，自定义函数可在 SQLite Cloud 集群中自动同步。
- 📜 **JavaScript 评估**：直接在 SQLite 查询中执行 JavaScript 代码。
- 🛠️ **示例**：包括字符串操作、统计聚合和自定义窗口函数等实用示例。
- 🔄 **更新函数**：需要通过新的数据库连接来更新已定义的函数。
- 🏗️ **从源码构建**：提供 Makefile 支持多平台构建。
- 📜 **许可证**：项目采用 MIT 许可证。

---

### [CSS 2025 现状](https://survey.devographics.com/en-US/survey/state-of-css/2025)

**原文标题**: [State of CSS 2025](https://survey.devographics.com/en-US/survey/state-of-css/2025)

概述总结  
该文章主要讨论了 2025 年 CSS 调查的背景、目的、参与方式以及相关常见问题，同时呼吁开发者参与调查以帮助社区和浏览器厂商更好地了解 CSS 技术的采用情况。  

- 🐌 作者希望 2025 年 CSS 的发展节奏放缓，以便社区有时间巩固现有功能并解决浏览器兼容性问题。  
- 📊 2025 年的 CSS 调查将帮助了解哪些新功能已被广泛采用，哪些仍待探索。  
- ⏳ 完成调查大约需要 15-20 分钟，参与者可以是任何使用 CSS 的人（职业、学习或兴趣）。  
- 🎯 调查目标是追踪新功能和库的演变，帮助开发者决定学习重点。  
- 🌍 调查数据将公开，供开发者和浏览器厂商参考以优化技术路线图。  
- 📅 调查时间为 2025 年 6 月 1 日至 7 月 1 日，结果将在结束后不久发布。  
- 👥 调查由 Devographics 团队及全球贡献者、翻译志愿者共同组织。  
- 🔍 调查设计过程开放，涉及浏览器厂商和开发者社区的反馈。  
- 🌐 提供多语言版本，并欢迎更多人参与翻译工作。

---

### [Babel 8 测试版发布 · Babel](https://babel.dev/blog/2025/05/30/babel-8-beta)

**原文标题**: [Announcing Babel 8 Beta · Babel](https://babel.dev/blog/2025/05/30/babel-8-beta)

Babel 8 Beta 版本正式发布，标志着经过近两年的开发，所有计划中的破坏性变更已完成，并清理了大量技术债务。团队呼吁用户在实际项目中测试该版本以发现问题。

- 🎉 Babel 8 Beta 发布：完成所有破坏性变更，大幅减少技术债务  
- 🧪 需实际项目测试：团队自 Alpha 阶段已内部使用，但需更多用户反馈  
- 📚 升级资源完备：提供用户迁移指南、API 开发者指南及临时文档网站  
- ⚡ ESM 专属包：Babel 8 仅支持 ESM，借助 Node.js 20 的 `require(esm)` 实现  
- 🔍 详细变更记录：GitHub 可查看各 Alpha 版本的完整更新日志  
- 🚧 后续计划：与主流项目协作适配、分离 Babel 7/8 代码分支、修复已知问题  
- 🐞 呼吁参与：鼓励用户测试并提交 GitHub Issue 反馈问题

---

### [ESLint v9.28.0 发布 - ESLint - 可插拔的 JavaScript 代码检查工具](https://eslint.org/blog/2025/05/eslint-v9.28.0-released/)

**原文标题**: [ESLint v9.28.0 released - ESLint - Pluggable JavaScript Linter](https://eslint.org/blog/2025/05/eslint-v9.28.0-released/)

ESLint v9.28.0 是一个小版本升级，引入了新功能和错误修复，包括对 TypeScript 语法支持的增强和新的 CLI 选项。

- 🚀 新增 CLI 选项 `--pass-on-unpruned-suppressions`，允许忽略未使用的抑制规则，不影响退出代码。  
- 📜 增强了对 TypeScript 语法的支持，更新了五个核心规则：`func-style`、`no-magic-numbers`、`no-shadow`、`no-use-before-define` 和 `prefer-arrow-callback`。  
- 🛠️ 修复了多个错误，包括全局变量处理和规则误报问题。  
- 📚 更新了文档，包括配置数组的嵌套说明和插件文档的补充。  
- 🔧 进行了多项内部改进和依赖项更新，如升级 `@eslint/js` 和 `globals` 版本。  
- 👥 由多位贡献者共同完成，包括 Francesco Trotta 和 Nitin Kumar 等。

---

### [GitHub - angular/angularfire: Angular + Firebase = ❤️](https://github.com/angular/angularfire)

**原文标题**: [GitHub - angular/angularfire: Angular + Firebase = ❤️](https://github.com/angular/angularfire)

AngularFire 是一个为 Angular 开发者设计的库，旨在简化 Firebase JS SDK 的使用，提供更符合 Angular 习惯的开发体验。它支持依赖注入、RxJS 观察者模式、懒加载等功能，并提供了丰富的 Firebase 产品集成。

- 🔥 Angular + Firebase 结合，提供更自然的开发体验  
- 🛠️ 支持依赖注入、Zone.js 封装、RxJS 观察者模式  
- 📦 懒加载 Firebase 功能，减少应用加载时间  
- 🚀 提供部署工具，一键部署到 Firebase Hosting  
- 📊 集成 Google Analytics，支持 Angular Router  
- 🔒 提供路由守卫，支持 Firebase 认证检查  
- 📚 包含丰富的文档、示例应用和社区支持资源  
- 🔄 支持多种 Firebase 产品（如 Firestore、Auth、Functions 等）  
- ⚠️ 目前为开发者预览版，可能存在变动

---

### [宣布 Angular v20 发布。过去几年… | 作者：Minko Gechev | 2025 年 5 月 | Angular 博客](https://blog.angular.dev/announcing-angular-v20-b5c9c06cf301?gi=397b18bde016)

**原文标题**: [Announcing Angular v20. The past couple of years have been… | by Minko Gechev | May, 2025 | Angular Blog](https://blog.angular.dev/announcing-angular-v20-b5c9c06cf301?gi=397b18bde016)

Angular v20 正式发布，带来多项稳定性提升、开发者体验优化及实验性功能探索。

- 🚀 **核心功能稳定化**：`effect`、`linkedSignal`、`toSignal` 等 API 晋升为稳定版，增量水合与路由级渲染模式配置同步稳定。
- 🔧 **开发者工具增强**：Angular DevTools 深度整合 Chrome 性能面板，新增组件实例化追踪与错误监听功能。
- 💡 **响应式编程升级**：Signal 相关 API（`signal`、`computed` 等）全面稳定，YouTube 实测输入延迟降低 35%。
- 🌐 **无 Zone 开发预览**：提供 SSR 错误处理方案，移除 `zone.js` 依赖，可通过 CLI 直接创建无 Zone 项目。
- ⚡ **实验性资源 API**：新增 `resource` 和 `httpResource`，支持基于 Signal 的异步状态管理与 HTTP 请求。
- 📊 **模板语法扩展**：支持指数运算符 `**`、`in` 操作符及未标记模板字面量，类型检查覆盖宿主绑定。
- 🧩 **样式指南革新**：简化命名规则，默认禁用文件后缀，迁移 `@HostBinding` 至 `host` 元数据。
- 🤖 **AI 开发支持**：推出 `llms.txt` 引导 LLM 生成现代 Angular 代码，发布 AI 应用构建指南。
- 🐠 **社区共创吉祥物**：启动官方吉祥物投票，提供棱角生物、深海鮟鱇鱼等候选方案。
- ⚠️ **弃用结构指令**：`*ngIf`、`*ngFor` 和 `*ngSwitch` 进入弃用周期，建议迁移至内置控制流语法。
- 🔍 **测试工具实验**：集成 Vitest 支持，提供节点环境与浏览器测试方案。
- 🙌 **致谢贡献者**：225 位社区成员提交代码，新增表单标记脏值、路由异步重定向等实用功能。

---

### [Vitest 3.2 正式发布！ | Vitest](https://vitest.dev/blog/vitest-3-2.html)

**原文标题**: [Vitest 3.2 is out! | Vitest](https://vitest.dev/blog/vitest-3-2.html)

Vitest 3.2 版本发布，主要改进了浏览器模式和 TypeScript 支持，引入新方法和配置选项，同时弃用部分旧功能。

- 🚨 **弃用 `workspace` 配置**：推荐使用 `projects` 替代，简化全局配置并避免与其他工具冲突。未来版本将完全移除该功能。  
- 📝 **新增注释 API**：支持为测试添加自定义注释和附件，并在多种报告器中显示。  
- 🔧 **作用域夹具**：`test.extend` 新增 `scope` 选项（`file` 或 `worker`），优化夹具生命周期管理。  
- 🎨 **自定义项目名称颜色**：通过 `projects` 配置可为不同项目设置标签颜色。  
- 🌐 **自定义浏览器定位器 API**：通过 `locators.extend` 扩展定位器逻辑，增强测试灵活性。  
- 🧹 **显式资源管理**：支持 `using` 语法自动恢复模拟函数，简化 `vi.spyOn` 和 `vi.fn` 的清理。  
- ⏱️ **测试信号 API**：提供 `AbortSignal` 以响应超时或中断，例如终止 `fetch` 请求。  
- 📊 **V8 AST 感知覆盖率映射**：使用 `ast-v8-to-istanbul` 提升性能，未来将作为默认选项。  
- 🔍 **文件监听触发模式**：通过 `watchTriggerPatterns` 配置特定文件变更时重新运行相关测试。  
- 🧩 **统一匹配器类型**：新增 `Matchers` 类型，集中扩展自定义匹配器的类型支持。  
- ⏩ **测试组顺序控制**：`sequence.groupOrder` 支持按组顺序运行多项目测试，优化执行流程。  

详细变更请参考 [Vitest 3.2 更新日志](https://github.com/vitest-dev/vitest/releases/tag/v3.2.0)。

---

### [Astro 5.9 | Astro](https://astro.build/blog/astro-590/)

**原文标题**: [Astro 5.9 | Astro](https://astro.build/blog/astro-590/)

Astro 5.9 版本带来了多项实验性功能和安全增强，包括内容安全策略（CSP）支持、Markdown 渲染优化以及适配器日志控制等。

- 🔒 **实验性内容安全策略（CSP）支持**：新增对 CSP 的实验性支持，帮助防止跨站脚本攻击（XSS），适用于所有渲染模式（静态页面、动态页面和单页应用）。  
- 📝 **在内容加载器中渲染 Markdown**：新增 `renderMarkdown` 辅助函数，允许在自定义加载器中直接渲染 Markdown 内容，并保持与项目配置的一致性。  
- 🖼️ **禁用实验性响应式图片的默认样式**：新增 `image.experimentalDefaultStyles` 配置选项，可禁用默认样式，便于与 Tailwind 4 等工具集成。  
- 📢 **允许适配器抑制功能支持日志**：适配器现在可以通过 `suppress` 选项控制日志输出，避免重复或冲突的提示信息。  
- 🔄 **升级指南**：推荐使用 `@astrojs/upgrade` CLI 工具或手动运行包管理器的升级命令（如 `npm install astro@latest`）进行版本更新。  
- 🌟 **社区贡献**：感谢核心团队及众多社区开发者的代码和文档贡献，共同推动了 Astro 5.9 的发布。  

（注：原文中部分技术配置细节和示例代码已简化，完整内容可参考官方文档。）

---

### [宣布 Ionic 8.6 版本发布 - Ionic 博客](https://ionic.io/blog/announcing-ionic-8-6)

**原文标题**: [Announcing Ionic 8.6 - Ionic Blog](https://ionic.io/blog/announcing-ionic-8-6)

Ionic 8.6 版本发布，带来全新输入验证码组件、日期时间功能增强、iOS 18 触觉反馈支持以及 Stencil 编译器更新，同时修复多项关键问题并优化性能。

- 🆕 **新增 OTP 输入组件**：提供现代化且无障碍的一次性密码输入支持，适用于验证码、安全 PIN 等场景，支持智能输入处理和灵活样式配置。  
- 📅 **日期时间组件增强**：新增`showAdjacentDays`属性，显示相邻月份日期，提升边界日期选择的便捷性。  
- 📱 **iOS 18 触觉反馈**：为`ion-toggle`组件添加触觉反馈，提升开关操作的交互体验。  
- 🔧 **Stencil 编译器升级**：从 v4.20 更新至 v4.33，修复 SSR 作用域样式、Shadow DOM 渲染等问题，并优化性能与可访问性。  
- 🛠️ **关键问题修复**：包括按钮/输入框无障碍属性更新、复选框 VoiceOver 兼容、日期时间 24 小时格式支持等，覆盖多个核心组件。  
- 🌟 **社区贡献致谢**：特别感谢开发者对 Datetime、Modal 等组件的代码贡献。  
- 🚀 **后续计划**：探索 React Router 最新版本支持，筹备下一主要版本更新，并欢迎实习生加入开发。

---

### [发布 6.9.0 版本 · prisma/prisma · GitHub](https://github.com/prisma/prisma/releases/tag/6.9.0)

**原文标题**: [Release 6.9.0 · prisma/prisma · GitHub](https://github.com/prisma/prisma/releases/tag/6.9.0)

Prisma 发布了 6.9.0 稳定版本，引入了多项新功能和改进，包括无 Rust 引擎的 Prisma ORM 预览版、本地 Prisma Postgres 的增强、多 ORM 支持、自动备份与恢复、VS Code 扩展的新管理界面以及新增的旧金山区域支持。

- 🎉 Prisma 6.9.0 稳定版发布，包含多项新功能和改进。
- 🚀 无 Rust 引擎的 Prisma ORM 进入预览阶段，支持 PostgreSQL 和 SQLite，提升无服务器和边缘环境体验。
- 📊 本地 Prisma Postgres 功能增强，支持数据库持久化和多实例同时运行。
- 🔗 新增多 ORM 支持，允许通过标准 PostgreSQL 连接字符串连接 Prisma Postgres。
- 💾 自动化备份与恢复功能升级，支持通过 UI 恢复任意历史备份。
- 🛠️ VS Code 扩展新增数据库管理界面，支持创建、删除远程实例和查看本地实例。
- 🌍 新增旧金山（us-west-1）区域，扩展 Prisma Postgres 的全球可用性。

---

### [Go 语言 JavaScript 开发者指南](https://prateeksurana.me/blog/guide-to-go-for-javascript-developers/)

**原文标题**: [A JavaScript Developer's Guide to Go](https://prateeksurana.me/blog/guide-to-go-for-javascript-developers/)

overview summary
- 作者是一名有五年经验的 JavaScript 开发者，过去一年转向使用 Go 进行服务器端开发，并注意到两种语言在语法、基础概念、实践和运行时环境上的差异。
- Go 最近因微软宣布将 TypeScript 编译器移植到 Go 而受到 JavaScript 社区的关注，新编译器速度预计比当前版本快 10 倍。
- 本文旨在为对 Go 感兴趣的 JavaScript 开发者提供入门指南，涵盖 Go 的基础概念，并与 JavaScript/TypeScript 进行对比，同时分享一些适应过程中的注意事项。

- 🚀 **语言对比**：Go 是编译型语言，需要先编译成机器码再执行，而 JavaScript 是解释型语言，直接执行。
- 📦 **包管理**：Go 程序由包组成，每个程序从 main 包开始执行，包通过首字母大写来导出成员，类似于 JavaScript 的模块系统。
- 🏗️ **变量与类型**：Go 是静态类型语言，变量类型在编译时确定，而 JavaScript 是动态类型语言。
- 🧩 **结构体与类型**：Go 使用结构体（struct）来组织数据，与 JavaScript 的对象类似，但 Go 的结构体是具体的数据类型，而非形状定义。
- 🔢 **零值**：Go 中的变量在声明时会自动初始化为其类型的零值，而 JavaScript 中未初始化的变量值为`undefined`。
- 🎯 **指针**：Go 支持指针，允许直接操作内存地址，而 JavaScript 中除原始类型外都是引用传递。
- 🔄 **函数**：Go 的函数支持多返回值，常用于错误处理，而 JavaScript 使用`try-catch`处理异常。
- 📊 **数组与切片**：Go 的数组长度固定，切片则是动态大小的，与 JavaScript 的数组不同。
- 🗺️ **映射（Map）**：Go 的映射与 JavaScript 的`Map`类似，但访问不存在的键会返回零值，而非`undefined`。
- 🔍 **比较操作**：Go 中大多数类型按值比较，而 JavaScript 中对象和数组按引用比较。
- 🛠️ **方法与接口**：Go 通过方法接收器为类型添加方法，接口通过方法集隐式实现，与 TypeScript 的接口和类实现不同。
- ❌ **错误处理**：Go 显式处理错误，通常作为函数的最后一个返回值，而 JavaScript 使用`try-catch`。
- ⚡ **并发**：Go 通过 goroutine 实现真正的并发，而 JavaScript 通过事件循环实现非阻塞 I/O。
- ✨ **格式化与 Linting**：Go 自带官方格式化工具`gofmt`，社区提供多种 lint 工具如`golangci-lint`。

- 🌟 **总结**：本文为 JavaScript 开发者提供了 Go 的基础知识对比，帮助理解两种语言的核心差异和 Go 的优势，特别是在并发和错误处理方面。

---

### [Go 编程语言](https://go.dev/)

**原文标题**: [The Go Programming Language](https://go.dev/)

Go 是一种由 Google 支持的开源编程语言，适合构建简单、安全且可扩展的系统。它具有易学性、内置并发功能和强大的标准库，同时拥有庞大的合作伙伴、社区和工具生态系统。

- 🚀 **简单易学**：Go 语言设计简洁，适合团队快速上手开发。  
- 🔒 **安全可靠**：内置并发支持和健壮的标准库，确保代码高效且安全。  
- 🌍 **广泛应用**：适用于云服务、网络服务、命令行工具、Web 开发及 DevOps 等多个领域。  
- 📦 **丰富生态**：拥有大量第三方库和工具，支持主流云平台（如 Google Cloud、AWS、Azure）。  
- ⚡ **高效性能**：编译速度快，内存占用低，适合微服务和容器化部署。  
- 💡 **开发者友好**：内置测试、性能分析和文档工具，提升开发效率。  
- 🏢 **企业认可**：Capital One、PayPal、American Express 等企业通过 Go 优化性能并简化部署。  
- 📚 **学习资源丰富**：提供教程、在线课程、书籍及云实践实验室，支持自学和团队培训。  

示例代码：  
```go
package main  
import "fmt"  
func main() {  
  fmt.Println("Hello, 世界")  
}  
```  
（输出：`Hello, 世界`）  

企业评价：  
- Capital One：“一个月内全员掌握 Go，其并发处理和开发效率令人印象深刻。”  
- PayPal：“Go 代码减少 10% CPU 占用，且更易维护。”  
- American Express：“开发者不愿再切换回其他语言。”  

用途扩展：  
- ☁️ **云服务**：支持快速构建云原生应用。  
- 🖥️ **CLI 工具**：利用标准库和开源包创建高效命令行程序。  
- 🌐 **Web 开发**：高性能内存管理助力可扩展应用。  
- 🔧 **DevOps/SRE**：快速构建和格式化特性提升运维效率。  

学习路径：  
- 提供免费下载（Windows/macOS/Linux）、在线教程、书籍及定制化企业培训（如 Ardan Labs）。

---

### [Go 语言周刊](https://golangweekly.com/)

**原文标题**: [Golang Weekly](https://golangweekly.com/)

每周关注 Go 编程语言的动态，提供最新资讯和资源  

- 📬 每周发布一期，订阅用户达 39089 人  
- 📰 已发布 556 期，支持 RSS 订阅  
- 🆓 提供最新一期免费试读  
- 🏢 由 Cooperpress 出版，注重隐私和反垃圾政策  
- 🎨 Go 吉祥物由 Renee French 设计，采用 CC 3.0 署名许可

---

### [`document.currentScript` 比我想象的更有用 | Alex MacArthur](https://macarthur.me/posts/current-script/)

**原文标题**: [`document.currentScript` is more useful than I thought. | Alex MacArthur](https://macarthur.me/posts/current-script/)

`document.currentScript` 是一个有用的 JavaScript API，能够获取当前正在执行的脚本元素，适用于传递配置属性和其他用途。  

- 🚀 **发现实用 API**：`document.currentScript` 可以获取当前执行的 `<script>` 元素，适用于动态配置传递。  
- 🏷️ **访问 DOM 属性**：通过该 API 可以读取脚本元素的属性，如 `dataset` 或 `defer`。  
- 🚫 **模块限制**：在 `<script type="module">` 中，`document.currentScript` 返回 `null`，无法使用。  
- ⏳ **异步代码问题**：异步代码（如 `setTimeout`）中访问该属性也会返回 `null`。  
- 🔧 **配置传递方案**：利用 `dataset` 在 `<script>` 标签中传递配置，避免全局变量污染。  
- 📦 **CMS 与静态网站适用**：适用于无法直接修改脚本内容的场景（如 Markdown 或 CMS）。  
- 🛠️ **其他用途**：可用于脚本加载验证（如强制异步加载）或实现“行为局部性”模式。  
- 🤔 **未来改进**：模块脚本中缺乏类似功能，标准社区正在讨论解决方案。

---

### [Svelte 峰会 2025 春季 - YouTube](https://www.youtube.com/playlist?list=PL8bMgX1kyZThKy_B41FQHk_xsHMQouV1Z#sveltesociety2025)

**原文标题**: [Svelte Summit Spring 2025 - YouTube](https://www.youtube.com/playlist?list=PL8bMgX1kyZThKy_B41FQHk_xsHMQouV1Z#sveltesociety2025)

该内容为 YouTube 网站底部的导航链接列表，涵盖了关于平台、法律条款、创作者支持及公司信息等多个方面。

- 📢 Press - 媒体相关  
- ©️ Copyright - 版权信息  
- 📞 Contact us - 联系我们  
- 🎨 Creators - 创作者相关  
- 💼 Advertise - 广告合作  
- 💻 Developers - 开发者资源  
- 📜 Terms - 使用条款  
- 🔒 Privacy - 隐私政策  
- ⚖️ Policy & Safety - 政策与安全  
- 🔧 How YouTube works - 平台运作机制  
- 🧪 Test new features - 测试新功能  
- ™ © 2025 Google LLC - 版权归属声明

---

### [Svelte • 为所有人打造的网页开发](https://svelte.dev/)

**原文标题**: [Svelte • Web development for the rest of us](https://svelte.dev/)

Svelte 是一个通过编译器让你能用熟悉的 HTML、CSS 和 JavaScript 编写极其简洁组件的 UI 框架，在浏览器中实现高效运行。

- 🎨 优雅简洁：Svelte 以轻量、优雅和时尚著称，让开发更高效。  
- 💻 开发者喜爱：开发者普遍认为 Svelte 是最令人兴奋的框架之一。  
- 🌍 广泛使用：被多家知名公司采用，社区活跃且遍布全球。  
- 🤝 社区支持：通过 Svelte Society 和 Discord 服务器提供友好的交流平台。  
- 🏢 企业支持：由 Vercel 等公司及众多捐赠者支持，维护团队强大且稳定。  
- 📜 开源免费：基于 MIT 许可证，永久免费且开放源代码。

---

### [将 Svelte 峰会带给整个社区](https://svelte.dev/blog/svelte-summit-videos)

**原文标题**: [Bringing Svelte Summit to the whole community](https://svelte.dev/blog/svelte-summit-videos)

Svelte 团队宣布将赞助并免费发布 Svelte Summit 巴塞罗那站的演讲视频，以便更广泛地分享社区成果，视频将于本周末开始陆续发布。

- 🎉 Svelte Summit 巴塞罗那站成功举办，充满活力与创意的社区庆祝活动  
- 💻 为无法亲临现场的观众提供了虚拟门票和高质量直播  
- 🙏 感谢 Svelte Society、Mainmatter 及购票者的支持使活动成真  
- 🆓 Svelte 团队决定赞助并免费公开演讲视频，惠及更广泛受众  
- 💰 资金来源于社区通过 opencollective.com/svelte 的慷慨捐助  
- 📺 订阅 Svelte Society YouTube 账号，第一时间获取视频发布通知

---

### [Svelte 的承诺，Rich Harris — 2025 春季 Svelte 峰会 - YouTube](https://www.youtube.com/watch?v=1dATE70wlHc)

**原文标题**: [What Svelte Promises, Rich Harris — Svelte Summit Spring 2025 - YouTube](https://www.youtube.com/watch?v=1dATE70wlHc)

YouTube 平台相关信息概览  

- 📢 关于我们 - 介绍 YouTube 的基本信息和背景  
- 🗞️ 新闻动态 - 提供 YouTube 相关的最新新闻和公告  
- ©️ 版权信息 - 说明 YouTube 的版权政策和相关内容  
- 📩 联系我们 - 提供与 YouTube 团队联系的途径  
- 🎨 创作者信息 - 介绍平台上的内容创作者相关资源和支持  
- 💼 广告合作 - 提供广告投放和商业合作的详细信息  
- 💻 开发者资源 - 提供 API 和开发者工具的相关信息  
- 📜 服务条款 - 列出用户使用平台需遵守的条款和条件  
- 🔒 隐私政策 - 说明用户数据的保护和使用政策  
- ⚖️ 政策与安全 - 介绍平台的内容政策和安全措施  
- 🔧 工作原理 - 解释 YouTube 平台的运作机制  
- 🆕 测试新功能 - 介绍正在测试中的新功能和特性  
- © 2025 Google LLC - 版权归属和年份声明

---

### [Svelte 最新动态：2025 年 6 月更新](https://svelte.dev/blog/whats-new-in-svelte-june-2025)

**原文标题**: [What’s new in Svelte: June 2025](https://svelte.dev/blog/whats-new-in-svelte-june-2025)

Svelte 在 2025 年 6 月迎来多项重要更新，包括新功能 Attachments、代码片段泛型支持、XHTML 兼容性改进等，同时社区涌现了大量基于 Svelte 构建的应用和工具。

- 🎯 **Attachments 发布**：作为 Actions 的升级版，提供更灵活的 API，支持通过`fromAction`工具将现有 Actions 转换为 Attachments（PR #1500，Svelte 5.29.0）。  
- ✨ **代码片段泛型支持**：提升类型提示能力（Svelte 5.30.0）。  
- 🔧 **开发工具增强**：Svelte 扩展支持保存时自动补全导入（language-tools@109.6.0）。  
- 🏗️ **类构造函数状态字段**：允许在类构造函数中声明状态字段（Svelte 5.31.0）。  
- 🌐 **XHTML 与 CSP 兼容**：新增`fragments`选项提升安全性（Svelte 5.33.0）。  
- 🚀 **客户端代码优化**：SSR 禁用时允许在通用页面顶层运行客户端代码（kit@2.21.0）。  

**社区亮点**：  
- 🎮 **应用展示**：包括游戏引擎 Whimsy、Markdown 编辑器 Kraa、AI 工具 Shovel AI 等创新项目。  
- 📚 **学习资源**：Svelte Summit 视频上线，Joy of Code 的 Attachments 教程，以及 SvelteBench 性能测试工具更新。  
- 🛠️ **工具库更新**：Bits UI v2 支持 Attachments，Svelte Flow 1.0 发布，新增密码保护、图像优化等实用工具。  

更多细节可查看[Svelte](https://github.com/sveltejs/svelte/blob/master/CHANGELOG.md)和[SvelteKit](https://github.com/sveltejs/kit/blob/master/CHANGELOG.md)的更新日志。

---

### [使用可选链编写更可靠的 JavaScript - Matt Smith](https://allthingssmitty.com/2025/06/02/write-more-reliable-javascript-with-optional-chaining/)

**原文标题**: [
    Write more reliable JavaScript with optional chaining - Matt Smith
  ](https://allthingssmitty.com/2025/06/02/write-more-reliable-javascript-with-optional-chaining/)

JavaScript 的可选链（?.）是一种强大特性，能有效避免访问嵌套属性时的常见错误，提升代码的可靠性和简洁性。  

- 🚨 **常见问题**：访问深层嵌套属性时，若中间值为`undefined`或`null`，会抛出`TypeError`错误。  
- 🛠️ **解决方案**：使用可选链（`?.`）安全访问属性，如`user?.profile?.avatar`，遇到`null`或`undefined`时直接返回`undefined`。  
- 📌 **典型场景**：  
  - 🌐 **API 数据**：`response?.data?.user?.name`避免中间缺失导致的错误。  
  - 🖥️ **DOM 操作**：`document.querySelector("#myInput")?.value`安全获取元素值。  
  - ⚙️ **方法调用**：`user?.sendMessage?.("Hello!")`确保方法存在再调用。  
- 🔄 **对比逻辑 AND（&&）**：可选链更简洁且仅针对`null/undefined`，而`&&`检查所有假值。  
- ⚠️ **注意事项**：  
  - 仅对`?.`前的`null/undefined`短路，其他假值（如`0`）会继续执行。  
  - 过度使用可能掩盖数据结构问题。  
  - 部分写法如`user?.profile.avatar`仍需完整链式保护。  
- ➕ **搭配空值合并（??）**：`user?.profile?.avatar ?? "default.png"`提供默认值。  
- 🌍 **浏览器支持**：现代浏览器均支持，IE 需通过 Babel 等工具转换。  
- 💡 **优势总结**：减少冗余代码，增强可读性，降低运行时错误风险。

---

### [RSC 中的导入机制解析——过度反应篇](https://overreacted.io/how-imports-work-in-rsc/)

**原文标题**: [How Imports Work in RSC — overreacted](https://overreacted.io/how-imports-work-in-rsc/)

React Server Components（RSC）是一种编程范式，允许开发者将客户端/服务器应用表达为跨越两个环境的单一程序。以下是关键点总结：

- 🚀 RSC 扩展了模块系统（`import`和`export`），通过新语义控制前端/后端代码分割。
- 🔍 `'use client'`和`'use server'`指令标记了两种环境的分割点，并定义了它们如何与模块系统交互。
- 📦 JavaScript 模块系统确保每个模块是单例，无论被导入多少次，代码只执行一次。
- 🔗 传统前后端代码共享时，模块系统独立运行，可能导致意外引入不兼容代码（如后端专属 API 泄露到前端）。
- 🛡️ 使用`server-only`和`client-only`标记模块，可防止代码被错误导入到不支持的环境，触发构建失败。
- 🔄 RSC 通过`'use client'`和`'use server'`指令，允许跨环境引用模块而不实际导入代码，实现数据传递。
- 🌐 RSC 应用可视为跨越两台计算机的单一程序，具有独立的模块系统、安全机制和通信通道。

---

### [rxliuli - 个人网站](https://rxliuli.com/blog/intercepting-network-requests-in-chrome-extensions/)

**原文标题**: [rxliuli - Personal Website](https://rxliuli.com/blog/intercepting-network-requests-in-chrome-extensions/)

概述  
本文介绍了在 Chrome 扩展中拦截网络请求（XHR/fetch）的实现方法，作者通过自定义中间件方案解决了现有库（如 mswjs 和 xhook）的局限性，并分享了设计思路与核心代码逻辑。

- 🚀 **动机**  
  - 开发 Chrome 扩展时需批量屏蔽 Twitter 垃圾用户，需拦截 XHR 请求获取动态生成的认证头信息。  
  - 现有库（如 mswjs 需 Service Worker、xhook 仅支持 XHR 且已停更）无法满足需求，决定自主实现。

- 🎨 **设计目标**  
  - 支持拦截/修改 fetch/XHR 请求、代理请求 URL、调用原始请求并修改响应、处理 SSE 流响应。  
  - API 设计参考 hono 框架的洋葱模型中间件模式，确保简洁易用。

- ⚙️ **Fetch 拦截实现**  
  - 覆写`globalThis.fetch`，通过中间件链处理请求/响应，保留原始 fetch 调用逻辑。  
  - 示例代码展示了中间件执行顺序（洋葱模型）及如何修改请求上下文。

- 🔄 **XHR 拦截实现**  
  - 覆写`XMLHttpRequest`类，记录`open/send`参数，延迟执行原始方法至`send`阶段。  
  - 需处理事件监听器绑定及响应修改，但当前实现为简化版（未完全覆盖所有事件/头信息）。

- 📦 **成果发布**  
  - 完整工具已封装为 npm 包`@rxliuli/vista`，支持项目中直接使用。  
  - 提供 GitHub 仓库链接（文中未展示具体地址）。

- 📌 **关键点总结**  
  - 优先考虑需求场景（如动态头信息获取），而非深入第三方 API 逆向分析。  
  - 洋葱模型中间件设计提升灵活性与可维护性。  
  - XHR 拦截复杂度高于 fetch，需注意方法覆写时机与事件监听管理。

---

### [高效单代码库的构成要素](https://blog.swgillespie.me/posts/monorepo-ingredients/)

**原文标题**: [The Ingredients of a Productive Monorepo](https://blog.swgillespie.me/posts/monorepo-ingredients/)

以下是按照您提供的模板总结的博客内容：

一个高效的单体代码库（monorepo）需要精心设计的工具链和明确的组织目标，以应对规模增长带来的挑战。

- 🏗️ **明确目标**：选择 monorepo 应基于一致性、组织协作和共享工具，而非盲目模仿大公司的成功案例。  
- ⚖️ **黄金法则**：所有操作必须保持 O(change) 而非 O(repo) 的复杂度，确保性能随代码库增长仍可接受。  
- 🔧 **版本控制挑战**：Git 在大型 monorepo 中性能受限，需考虑稀疏检出（sparse checkout）或虚拟文件系统等优化方案。  
- 🛠️ **构建系统**：优先使用语言原生工具（如 Cargo、Go build），避免过早引入多语言支持；关键需求是高效构建和精准识别变更影响目标。  
- 🧪 **测试策略**：需自动重试失败测试、仅运行必要测试，并通过隔离不稳定测试减少 CI 噪音。  
- 🔄 **持续集成**：结合变更范围触发定向任务，权衡吞吐量、正确性和延迟（如合并队列批处理或概率性任务选择）。  
- 🚀 **持续交付陷阱**：代码原子提交≠原子部署，需强制验证服务合约变更，避免破坏性部署。  
- 💡 **长期投入**：Monorepo 能强化工程文化，但需持续优化工具链以应对规模问题。  

（注：原文中的技术术语链接和脚注未在摘要中保留，重点保留了核心观点和 actionable 建议。）

---

### [无缝融合 PHP 与 Node.js](https://blog.platformatic.dev/seamlessly-blend-php-with-nodejs)

**原文标题**: [Seamlessly Blend PHP with Node.js](https://blog.platformatic.dev/seamlessly-blend-php-with-nodejs)

概述总结  
Platformatic 发布了全新的 Node.js 模块 `@platformatic/php-node`，该模块允许在 Node.js 环境中无缝嵌入 PHP，实现两种语言的高效结合。通过 Rust 和 Node.js 的多线程工作池，php-node 提供了高性能的 PHP 请求处理能力，适用于多种场景，如迁移遗留 PHP 应用、构建混合应用等。此外，文章还展示了如何在 Watt 服务器中运行 WordPress，并结合 Next.js 构建现代化的前端应用。

- 🚀 **发布新模块**：`@platformatic/php-node` 是一个革命性的 Node.js 模块，允许在 Node.js 中直接嵌入 PHP，实现两种语言的无缝结合。  
- 🔧 **技术原理**：基于 Rust 和 `napi.rs`，php-node 通过多线程工作池处理 PHP 请求，提升性能并简化开发流程。  
- 🌐 **核心功能**：支持多线程处理、低延迟请求响应，并提供统一的开发环境，减少认知负担。  
- 🏗️ **应用场景**：适用于迁移遗留 PHP 应用、构建混合应用以及创建高性能的 Web 服务。  
- 📦 **快速上手**：通过 `npm install @platformatic/php-node` 安装模块，详细文档可在 GitHub 仓库查看。  
- 🛠️ **示例演示**：展示了如何在 Watt 服务器中运行 PHP，并成功部署 WordPress。  
- 🔗 **混合开发**：结合 Next.js 和 WordPress，实现内容管理与前端展示的分离，提升性能和灵活性。  
- 📺 **更多资源**：提供了完整的演示视频和 GitHub 仓库链接，方便开发者进一步探索。  
- 📩 **社区支持**：欢迎开发者通过 `hello@platformatic.dev` 反馈问题或建议。

---

### [为您的 SaaS 添加 Clerk Billing 订阅服务](https://clerk.com/blog/add-subscriptions-to-your-saas-with-clerk-billing?utm_source=cooper-press&utm_medium=newsletter&utm_campaign=billing-guide&utm_content=06-06-25&dub_id=uVnqYxmGqzuWZrfe)

**原文标题**: [Add subscriptions to your SaaS with Clerk Billing](https://clerk.com/blog/add-subscriptions-to-your-saas-with-clerk-billing?utm_source=cooper-press&utm_medium=newsletter&utm_campaign=billing-guide&utm_content=06-06-25&dub_id=uVnqYxmGqzuWZrfe)

Clerk Billing 是一项新功能，旨在简化 SaaS 应用的订阅管理，帮助开发者快速实现付费功能，无需从头构建复杂的计费系统。

- 💡 **Clerk Billing 简介**：Clerk 的新功能，集成订阅管理到现有身份验证系统中，通过仪表板轻松定义订阅计划和功能。
- 🛠️ **工作原理**：在 Clerk 仪表板中创建计划和功能，使用 `<PricingTable />` 组件展示计划，用户可通过模态窗口输入支付信息。
- 🔒 **权限验证**：使用 `has()` 助手函数检查用户是否有权访问特定功能或计划，轻松保护高级功能。
- 🔄 **订阅管理**：用户可通过 `<UserProfile />` 组件管理订阅，管理员可在仪表板中查看和取消订阅。
- 🚀 **实际应用**：在 Quillmate 写作平台中，通过 Clerk Billing 实现了 AI 助手功能的付费订阅，保护前后端代码。
- ⚡ **快速集成**：无需自定义计费逻辑，Clerk 处理用户界面和授权逻辑，与 Stripe 集成处理支付。
- 📈 **灵活定价**：支持月费和年费计划，可配置折扣，功能可跨计划共享，构建分层定价结构。

---

### [故事书 9](https://storybook.js.org/blog/storybook-9/)

**原文标题**: [Storybook 9](https://storybook.js.org/blog/storybook-9/)

Storybook 9 是一个专注于组件测试的高效工具，通过与最新测试工具（如 Vitest 和 Playwright）合作，提供了全面的 UI 测试解决方案。  

- 🚀 **Storybook 9 发布**：专注于组件测试，提供更高效的测试工具链。  
- ⚡ **Vitest 集成**：最快的测试运行器，支持一键运行所有测试。  
- 🌐 **Playwright 支持**：提供高保真的浏览器测试体验。  
- ▶️ **交互测试**：模拟用户行为，验证组件功能。  
- ♿ **无障碍测试**：检测并修复 WCAG 违规问题。  
- 👁️ **视觉测试**：精确到像素的 UI 检查，防止视觉错误。  
- 🛡️ **测试覆盖率报告**：直观展示代码测试情况。  
- 🚥 **测试小部件**：一键运行全面的测试套件。  
- 🪶 **体积减小 48%**：更轻量级的安装，依赖更少。  
- ✍️ **故事生成**：自动生成和编辑组件故事。  
- � **标签组织**：通过标签分类和过滤故事。  
- 🌐 **故事全局变量**：支持按故事设置主题、视口等上下文。  
- 🏗️ **框架升级**：支持 Svelte 5、Next.js、React Native 等。  
- 📱 **React Native 改进**：支持 Web 和移动端并行开发。  
- 📅 **未来计划**：进一步优化体积、模块模拟和类型安全。  

Storybook 9 通过全面的测试功能和核心升级，帮助开发者更高效地构建和维护高质量的 UI 组件。

---

### [GitHub - sebastiancarlos/beachpatrol: �️ 一款替代并自动化日常网页浏览的 CLI 工具](https://github.com/sebastiancarlos/beachpatrol)

**原文标题**: [GitHub - sebastiancarlos/beachpatrol: 🏝️ A CLI tool to replace and automate your daily web browser.](https://github.com/sebastiancarlos/beachpatrol)

Beachpatrol 是一个 CLI 工具，旨在替代并自动化日常网页浏览操作，通过 Playwright 脚本控制浏览器，支持 Chromium 和 Firefox，提供自动化任务执行和浏览器扩展集成。

- 🏝️ **项目简介**：Beachpatrol 是一个命令行工具，用于替代和自动化日常网页浏览，支持 Chromium 和 Firefox。
- 🛠️ **功能特点**：通过 Playwright 脚本控制浏览器，支持多配置文件、隐身模式和后台运行。
- 📂 **安装步骤**：克隆仓库、安装依赖、运行 `make` 安装可执行文件。
- 🚀 **使用示例**：启动浏览器后，可通过 `beachmsg` 命令运行自动化脚本，支持自定义脚本和浏览器扩展。
- 🔍 **技术细节**：使用 Playwright 和 stealth 插件隐藏自动化痕迹，支持 Linux 和 macOS（Windows 支持开发中）。
- ❓ **常见问题**：解释了为什么选择 Playwright 和 JavaScript，以及与其他工具（如 Selenium 和 bookmarklets）的比较。
- ⚠️ **已知问题**：下载文件名显示为 UUID，Firefox 用户可能遇到 Cloudflare 误报和 Google 验证码问题。
- 📜 **许可证**：MIT 许可证，欢迎贡献。
- 🔄 **项目状态**：Alpha 阶段，API 可能变动，浏览器扩展尚未公开发布。

---

### [GitHub - wooorm/starry-night: 类似 GitHub 的语法高亮](https://github.com/wooorm/starry-night)

**原文标题**: [GitHub - wooorm/starry-night: Syntax highlighting, like GitHub](https://github.com/wooorm/starry-night)

starry-night 是一个开源的语法高亮工具，类似于 GitHub 使用的 PrettyLights 项目。它支持 600 多种语法，使用 TextMate 语法规则，适用于多种编辑器（如 SublimeText、Atom、VS Code 等）。该项目适合需要高质量语法高亮的场景，尤其是在浏览器或 Node.js 环境中。

- 🌟 开源语法高亮工具，支持 600+ 种语法
- 📦 使用 TextMate 语法规则，适用于多种编辑器
- 🚀 适合高质量语法高亮需求，支持浏览器和 Node.js
- 📝 生成 AST，适用于虚拟 DOM 框架（如 React、Preact）
- 🎨 提供多种主题，支持自动切换暗黑模式
- 🔧 支持自定义语法规则和扩展
- 📊 包含常见语法（如 JavaScript、Python、HTML）和更多小众语法
- 🔗 兼容 Node.js 16+ 和现代浏览器
- 🛡️ 安全性高，所有语法规则均为宽松许可证
- 🔄 可与 unified、remark、rehype 等工具集成

---

### [获取失败](https://javascriptweekly.com/link/170175/web)

**原文标题**: [Failed to retrieve](https://javascriptweekly.com/link/170175/web)

无法总结：获取内容失败，状态码 404。

---

