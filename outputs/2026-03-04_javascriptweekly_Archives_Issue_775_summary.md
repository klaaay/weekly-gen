### [JavaScript 周刊第 775 期：2026 年 3 月 3 日](https://javascriptweekly.com/issues/775)

**原文标题**: [JavaScript Weekly Issue 775: March 3, 2026](https://javascriptweekly.com/issues/775)

本期 JavaScript 周刊涵盖了多个重要更新与工具发布：Bun v1.3.10 带来 REPL 重写和浏览器编译功能，React 基金会正式成立，Node.js 发布周期将调整，以及 Deno、Expo 等工具的新版本发布。同时探讨了 WebAssembly、Streams API 等技术议题，并推荐了多项开发工具和资源。

- 🚀 **Bun v1.3.10 发布**：REPL 完全重写，新增浏览器编译选项，全面支持 ES 装饰器，事件循环和导入优化提速  
- 🤖 **Meticulous AI 自动化测试**：为 Notion、Dropbox 等公司自动生成端到端 UI 测试，实现零开发投入的全面覆盖  
- 🗺️ **外部导入映射支持**：Lea Verou 提出解决方案，JSPM 4.0 已实现该功能  
- ⚛️ **React 基金会正式启动**：由 Meta 等八家创始成员组成，接管 React、React Native 和 JSX 的所有权  
- 📅 **Node.js 发布周期变更**：计划改为每年一次主要发布，所有版本均为 LTS，取消奇偶版本区分  
- 🦕 **Deno 2.7 发布**：稳定 Temporal API 支持，新增 Windows on ARM 和 package.json 覆盖功能  
- 🌐 **WebAssembly 改进倡议**：Ryan Hunt 倡导通过组件模型让 WASM 直接绑定浏览器 API，提升开发体验  
- 🔄 **Streams API 优化提案**：James M Snell 针对现有标准的可用性和性能问题提出替代方案  
- 🛠️ **开发工具更新**：包括 Expo SDK 55、Shiki 4.0、AdonisJS v7 等多项工具发布  
- 🎨 **前端技术资源**：涵盖 ViteLand、Astro 月度总结，Angular 漏洞修复，以及 React Native VR 开发等内容

---

### [Bun v1.3.10 | Bun 博客](https://bun.com/blog/bun-v1.3.10)

**原文标题**: [Bun v1.3.10 | Bun Blog](https://bun.com/blog/bun-v1.3.10)

Bun 1.3.1 版本发布，带来了全新的原生 REPL、支持编译为独立 HTML 文件、完全支持 TC39 标准装饰器、多项性能优化（包括更快的 structuredClone、Buffer.slice 和 path.parse）、Windows ARM64 原生支持、捆绑器新增 Barrel 导入优化、事件循环与 TLS 保活改进、JavaScriptCore 引擎升级，并修复了大量错误。

- 🚀 **全新原生 REPL**：用 Zig 重写，启动迅速，支持语法高亮、多行输入、Tab 补全、持久历史记录和 Emacs 键绑定等丰富功能。
- 🌐 **编译为独立 HTML**：`bun build --compile --target=browser` 可将所有 JS、CSS 和资源内联到单个 HTML 文件中，无需服务器即可运行。
- 🎨 **支持 TC39 标准装饰器**：完全支持 Stage 3 装饰器规范，包括 `accessor` 关键字、装饰器元数据和正确的求值顺序。
- ⚡ **多项性能大幅提升**：`structuredClone` 对数组克隆快达 25 倍，`Buffer.slice()` 快约 1.8 倍，`path.parse()` 快 2.2-7 倍，字符串与正则操作也显著加速。
- 🖥️ **Windows ARM64 原生支持**：可在 ARM64 Windows 设备上安装运行，并支持交叉编译为目标平台的可执行文件。
- 📦 **捆绑器 Barrel 导入优化**：自动检测并仅解析实际使用的子模块，使类似 `antd` 的库构建速度提升高达 2 倍。
- 🔧 **事件循环与 TLS 改进**：macOS/Linux 事件循环更快；自定义 TLS 配置（如 mTLS）现在支持连接保活，减少握手开销。
- 🔄 **升级与安装**：提供 `curl`、`npm`、`PowerShell`、`Scoop`、`Homebrew` 和 `Docker` 多种安装方式，并通过 `bun upgrade` 轻松升级。
- 🐛 **大量错误修复**：修复了 `Bun.spawn()` 与 Python MCP 服务器的兼容性、Node.js 兼容性问题、内存泄漏、崩溃问题以及 `bun install`、`bun test` 和 Bun Shell 中的多个缺陷。
- 📜 **根证书更新**：更新了捆绑的根证书列表，移除了四个不受信任的 CommScope 根证书。
- 🧪 **测试功能增强**：`bun test` 新增 `--retry` 标志，支持全局重试失败测试，并改进了 JUnit XML 报告输出。
- 🛠️ **API 与工具改进**：`Bun.generateHeapSnapshot("v8")` 支持返回 `ArrayBuffer`；`Bun.build()` 输出对象和堆大小减少；修复了 HTTP 头注入等安全问题。

---

### [GitHub - tc39/proposal-decorators: ES6 类的装饰器提案 · GitHub](https://github.com/tc39/proposal-decorators)

**原文标题**: [GitHub - tc39/proposal-decorators: Decorators for ES6 classes · GitHub](https://github.com/tc39/proposal-decorators)

该提案旨在为 JavaScript 类引入装饰器语法，允许开发者通过装饰器扩展类的功能，同时保持代码的简洁性和可维护性。装饰器可用于类、类字段、方法和访问器，提供替换、访问和初始化能力，并引入新的自动访问器概念。

- 🎯 **装饰器功能**：装饰器是函数，可在类定义期间应用于类、类元素等，用于替换、访问或初始化被装饰的值，增强类的功能而不改变其外部行为。
- 🔄 **设计目标**：提案强调装饰器应易于使用和编写，避免混淆和非局部效应，确保装饰后的值保持原有语义，提升静态分析能力。
- 📚 **应用范围**：装饰器可应用于类、类字段（公共、私有、静态）、类方法、类访问器，并引入类自动访问器（使用`accessor`关键字），支持更灵活的元编程。
- 🛠️ **装饰器执行步骤**：装饰器评估分为三步：装饰器表达式与计算属性名交错评估；装饰器在类定义期间调用；所有装饰器调用后统一应用，确保过程不可观察。
- 📝 **API 设计**：装饰器接收被装饰的值和上下文对象，上下文包含类型、名称、访问方法等信息，支持通过`addInitializer`添加初始化逻辑。
- 🌟 **自动访问器**：新引入的类自动访问器通过`accessor`关键字定义，默认提供 getter 和 setter，装饰器可包装这些访问器以拦截属性访问。
- ⚙️ **初始化器**：通过`addInitializer`方法，装饰器可关联初始化函数，在类或类元素定义后运行额外代码，例如注册 Web 组件或绑定方法。
- 🔗 **访问与元数据**：装饰器可通过上下文中的`access`对象访问被装饰值，支持依赖注入等高级模式，利用元数据侧信道实现值注入。
- 📈 **标准化进展**：提案已进入 Stage 3，完成规范文本编写，并在 Babel 等工具中实现实验性支持，正收集开发者反馈以进一步推进。
- ❓ **常见问题解答**：提案与 Babel 遗留装饰器、TypeScript 实验性装饰器等版本对比，解释设计差异、优化能力和静态分析优势，强调对生态系统的影响。

---

### [精密 AI - 无需编写测试的自动化前端测试](https://www.meticulous.ai?utm_source=jsweekly&utm_medium=referral&utm_campaign=26q1&utm_content=primary)

**原文标题**: [Meticulous AI - Automated Frontend Testing Without Writing Tests](https://www.meticulous.ai?utm_source=jsweekly&utm_medium=referral&utm_campaign=26q1&utm_content=primary)

Meticulous AI 是一款创新的自动化测试工具，通过记录用户与应用的交互来生成并维护测试套件，无需手动编写或维护测试代码，从而帮助开发团队高效、可靠地发布无回归错误的代码。

- 🚀 **无需编写测试**：通过记录开发、预演和生产环境中的用户交互，自动生成覆盖所有代码分支和用户流程的测试。
- 🤖 **AI 驱动测试生成**：AI 引擎持续生成和更新测试套件，覆盖应用的每个角落，包括边缘情况。
- 🔄 **自动测试维护**：测试随应用演进自动更新，移除过时测试，确保测试套件始终最新且完整。
- ⚡ **闪电般测试速度**：通过并行计算集群，能在 120 秒内测试数千个页面，大幅提升测试效率。
- 🛡️ **无干扰测试环境**：默认模拟后端响应，避免因数据变化导致的误报，无需设置测试账户或模拟数据。
- 🌐 **广泛框架支持**：支持 NextJS、React、Vue、Angular、Nuxt、SvelteKit 等多种前端框架，集成简便。
- 📈 **提升开发效率**：被 Dropbox、Notion 等超过 100 家组织信任，帮助团队快速迭代并保证代码质量。

---

### [外部导入映射，今日上线！ • Lea Verou](https://lea.verou.me/blog/2026/external-import-maps-today/)

**原文标题**: [
		External import maps, today! • Lea Verou](https://lea.verou.me/blog/2026/external-import-maps-today/)

本文介绍了通过动态注入脚本实现外部导入映射（import map）的方法，从而解决了 Web 依赖管理的核心限制。该方法利用 DOM 操作在页面中插入内联导入映射，无需依赖 HTML 生成或外部导入映射文件，且兼容主流浏览器版本。

- 🚀 动态注入导入映射：通过经典脚本创建并插入`<script type="importmap">`元素，实现外部导入映射的模拟，无需紧密耦合的构建流程。
- 🌐 广泛浏览器兼容：该方法在 Chrome 89、Safari 16.4+ 和 Firefox 108+ 等支持导入映射的浏览器中均可使用。
- 🔗 相对 URL 处理：注入的导入映射需将相对 URL 转换为绝对 URL，以避免跨页面路径问题，代码仅增加约 5 行。
- ⚠️ 错误处理增强：脚本需确保使用经典脚本（非模块）并检查`document.currentScript`，防止在模块脚本中运行失败。
- 🛠️ 现有工具应用：JSPM v4 已采用相同技术，验证了该方法的实用性。
- 📜 平台集成愿景：作者认为当前仅通过 HTML 提供导入映射是一种临时方案，未来需在平台层面深化集成，如通过 HTTP 头或同步 API 支持。
- 🔮 未来工具展望：作者正开发基于此技术的依赖管理工具，旨在实现无构建过程的端到端依赖管理。

---

### [网络依赖关系已断裂。我们能修复吗？• 莉亚·维罗](https://lea.verou.me/blog/2026/web-deps/)

**原文标题**: [
		Web dependencies are broken. Can we fix them? • Lea Verou](https://lea.verou.me/blog/2026/web-deps/)

Web 平台当前缺乏原生的依赖管理机制，导致开发者不得不依赖打包工具等第三方方案，这增加了开发复杂度，尤其对新手造成障碍。文章探讨了现有无打包方案的问题，并呼吁改进标准以提供更优雅的依赖管理方案。

- 🚫 **无打包方案的普遍缺陷**：当前所有无打包使用依赖的方法（如直接引用 node_modules、使用公共 CDN 等）都存在安全、性能或维护性问题，无法提供健康生态所需的体验。
- 🔗 **导入映射的局限性**：虽然导入映射（import maps）允许浏览器解析说明符，但其依赖 HTML、缺乏组合性且管理繁琐，并未真正解决依赖管理的根本问题。
- 📦 **打包工具成为无奈之选**：由于平台原生支持的缺失，打包工具已成为处理依赖的事实标准，但这将基础功能外包，导致工具链复杂化和学习曲线陡峭。
- 🌍 **对 Web 架构的负面影响**：依赖管理的缺失迫使平台设计围绕打包工具进行，影响了如组件资源引用等基础功能的自然实现，甚至导致标准库膨胀。
- 🛠️ **改进方向与呼吁**：文章建议通过外部导入映射、服务器透明解析说明符等方案改进标准，并强调依赖管理应作为平台基础功能，呼吁社区共同推动解决这一根本问题。

---

### [JSPM - JSPM 4.0 版本发布](https://jspm.org/jspm-4.0-release#import-map-package-management)

**原文标题**: [JSPM - JSPM 4.0 Release](https://jspm.org/jspm-4.0-release#import-map-package-management)

JSPM 4.0 发布，采用基于标准的约定优于配置工作流，专注于原生 ES 模块和导入映射，简化开发流程并减少工具依赖。

- 🚀 **标准优先工作流**：基于原生 ES 模块和导入映射，无需自定义加载器，减少配置和构建步骤
- 📦 **导入映射包管理**：将导入映射视为包管理产物，通过`importmap.js`脚本注入，支持浏览器原生语义
- 📄 **package.json 作为清单**：依赖和入口点由`package.json`的`name`和`exports`字段定义，JSPM 自动处理映射
- 🔥 **热重载服务器**：`jspm serve`提供零配置开发环境，支持 TypeScript 类型剥离和即时热模块重载
- 🏗️ **生产构建**：`jspm build`遵循相同的运行时语义，无需额外配置，优化包大小
- 🎯 **未来方向**：专注于在线沙盒和无 CDN 本地工作流，强调标准优先和安全性
- 📚 **下一步**：鼓励尝试新版本，提供入门指南、CLI 文档和在线导入映射生成器

---

### [React 基金会：Linux 基金会托管下的 React 新家园](https://react.dev/blog/2026/02/24/the-react-foundation)

**原文标题**: [The React Foundation: A New Home for React Hosted by the Linux Foundation – React](https://react.dev/blog/2026/02/24/the-react-foundation)

React Foundation 正式成立，由 Linux Foundation 托管，标志着 React、React Native 及相关项目从 Meta 独立出来，转为由新基金会所有，旨在推动生态系统的持续发展。

- 🏛️ React Foundation 正式启动，由 Linux Foundation 托管，React、React Native 和 JSX 等项目不再属于 Meta，转为基金会所有。
- 🤝 八家铂金创始成员包括 Amazon、Callstack、Expo、Huawei、Meta、Microsoft、Software Mansion 和 Vercel，Huawei 为新加入成员。
- 🧑‍💼 基金会由各成员代表组成的董事会管理，Seth Webster 担任执行董事，技术治理保持独立，暂设临时领导委员会制定技术方向。
- 📅 未来几个月将完成技术治理结构、基础设施转移，并规划支持生态系统的项目和下一届 React Conf。
- 🙏 感谢所有贡献者和开发者，React Foundation 的成立源于社区支持，期待共同构建未来。

---

### [错误](https://javascriptweekly.com/link/181405/web)

**原文标题**: [Error](https://javascriptweekly.com/link/181405/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='nodejs-org-git-fork-ulisesgascon-release-announcement-openjs.vercel.app', port=443): Max retries exceeded with url: /en/blog/announcements/evolving-the-nodejs-release-schedule (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1000)')))

---

### [Svelte 2026 年 3 月更新亮点](https://svelte.dev/blog/whats-new-in-svelte-march-2026)

**原文标题**: [What’s new in Svelte: March 2026](https://svelte.dev/blog/whats-new-in-svelte-march-2026)

Svelte 在 2026 年 3 月迎来了一系列更新，涵盖核心库、SvelteKit 及工具链，同时社区生态持续繁荣，Svelte 在 State of JS 2025 调查中保持积极评价领先地位。

- 🆕 Svelte 核心新增多项功能：`createContext` 支持编程式组件实例化、`{@html}` 表达式兼容 `TrustedHTML`、HTML 标签内允许注释、错误边界现支持服务端。
- 🛠️ SvelteKit 更新包括：`hydratable` 脚本适配 CSP 策略、导航回调新增滚动位置信息、支持 Vite 8、`match` 函数可映射路径至路由 ID 与参数。
- ⚠️ Netlify 适配器有重大变更：`platform.context` 升级为现代 Netlify Functions 格式，并支持通过 `netlify.toml` 配置重定向。
- 🚀 Svelte CLI 新增官方插件 `better-auth`，用于身份验证功能集成。
- 🌟 社区展示丰富：涵盖知识库、地图工具、音乐生成器、AI 吉他平台、自托管音乐流媒体、简历分析工具、战术游戏等多样化 Svelte 应用。
- 📚 学习资源更新：包括开发者经验分享、播客节目及新增的 Laravel + Svelte 官方入门套件。
- 🧩 工具与组件库涌现：如智能骨架加载器、全栈电商平台、状态路由框架、动画图标库、拖拽库、开发调试工具等。

---

### [ViteLand 二月 2026 回顾：新动态一览 | VoidZero](https://voidzero.dev/posts/whats-new-feb-2026)

**原文标题**: [What’s New in ViteLand: February 2026 Recap | VoidZero](https://voidzero.dev/posts/whats-new-feb-2026)

ViteLand 2026 年 2 月更新回顾了 Vite+ 生态系统中各项目的进展，包括 Oxfmt 进入 Beta 阶段、Vite 8 Beta 引入开发者工具、Vitest 新增测试钩子、Rolldown 性能优化、Oxc 速度提升以及社区动态和即将举行的活动。

- 🚀 Oxfmt 进入 Beta 阶段，实现与 Prettier 完全兼容，运行速度提升高达 36 倍，并已获多家知名团队采用。
- 🔧 Vite 8 Beta 实验性开发者工具上线，支持模块图检查、转换时间线分析和 HMR 调试，并推出插件注册表。
- 🧪 Vitest 4.1 Beta 引入`aroundEach`和`aroundAll`钩子，后续版本将添加慢速测试过滤功能。
- ⚡ Rolldown 通过优化文件路径处理提升 9.6% 性能，文档新增死代码消除详解，tsdown 实验性支持 Node.js 单可执行文件打包。
- 🏎️ Oxc 通过标识符哈希预计算使语义分析提速 4-6%，Oxlint 增加类型感知规则并支持配置选项。
- 📅 即将举办的活动包括 Vue.js Amsterdam、Laravel Live Japan 2026 和 enterJS 2026，将有 VoidZero 团队成员分享。
- 🌐 社区动态涵盖 Vinext（基于 Vite 8 的 Next.js）、Astro 基于 Oxc 开发 Rust 编译器、Nest.js 迁移至 Vitest 等多项进展。

---

### [Astro 2026 年 2 月更新亮点 | Astro](https://astro.build/blog/whats-new-february-2026/)

**原文标题**: [What’s new in Astro - February 2026 | Astro](https://astro.build/blog/whats-new-february-2026/)

2026 年 2 月，Astro 生态系统迎来多项更新：采用率显著提升，在多项开发者调查中表现优异；发布了 Astro 5.18 和 6.0-beta.17 版本；众多知名企业及创新项目采用 Astro 构建网站；社区贡献了大量工具、主题和内容资源，展示了 Astro 的广泛应用与活跃生态。

- 📈 **采用率增长**：Astro 在 HTTP Archive 中的移动端和桌面端采用率分别提升 11.8% 和 14.6%，并在 2025 年 State of JS 调查中多项指标蝉联榜首。
- 🚀 **版本更新**：Astro 5.18 新增请求体大小配置选项，6.0-beta.17 发布并提供升级指南草案，方便开发者提前体验。
- 🌐 **知名采用者**：包括 Aftonbladet、MrBeast/Salesforce、Pokémon 等大型企业及项目已使用 Astro 构建网站。
- 🎨 **创意网站展示**：社区涌现出众多风格独特、视觉出色的网站案例，如 Ingrid Hartman 个人网站、Aptos Network 官网等，展现 Astro 的多样化应用。
- 🛠️ **工具与集成**：社区发布了大量新工具，如字体优化、缓存管理、SEO 增强等集成，助力开发效率提升。
- 🧩 **主题与模板**：新增多款主题，涵盖博客、电商、文档等类型，为项目快速启动提供丰富选择。
- 📚 **社区内容**：包括技术文章、迁移案例、视频教程等资源，涵盖性能优化、部署实践等热门话题。
- 🌟 **Starlight 应用**：多家项目采用 Starlight 构建文档站点，展示了其在文档领域的适用性。

---

### [获取失败](https://javascriptweekly.com/link/181409/web)

**原文标题**: [Failed to retrieve](https://javascriptweekly.com/link/181409/web)

无法总结：获取内容失败，状态码 403。

---

### [导航 API - 更优导航方式，现已基线新可用 | 博客 | web.dev](https://web.dev/blog/baseline-navigation-api?hl=en)

**原文标题**: [Navigation API - a better way to navigate, is now Baseline Newly Available  |  Blog  |  web.dev](https://web.dev/blog/baseline-navigation-api?hl=en)

单页应用（SPA）的导航长期以来依赖不完善的 History API，存在诸多限制。新的 Navigation API 现已全面可用，它通过统一的事件处理机制，简化了客户端路由，支持程序化导航、表单提交、滚动控制和视图过渡，为现代 Web 应用提供了更强大、可靠的导航解决方案。

- 🚀 Navigation API 已全面可用，解决了 History API 在单页应用导航中的长期痛点
- 🔗 通过统一的 `navigate` 事件集中处理所有导航类型，包括链接点击、表单提交和前进/后退按钮
- ⚙️ 自动处理 URL 更新、历史记录和可访问性，无需手动调用 `pushState` 或监听 `popstate`
- 📝 支持拦截表单提交并直接访问 `formData`，无需额外处理页面重载
- 🖱️ 提供手动控制滚动恢复时机的能力，确保内容加载后再调整滚动位置
- 🎬 与 View Transitions API 无缝集成，可实现流畅的页面过渡动画
- 🛠️ 简化了路由器的构建，减少了边缘情况处理，提高了开发效率和用户体验

---

### [Deno 2.7：Temporal API、Windows ARM 与 npm 覆盖功能 | Deno](https://deno.com/blog/v2.7)

**原文标题**: [Deno 2.7: Temporal API, Windows ARM, and npm overrides | Deno](https://deno.com/blog/v2.7)

Deno 2.7 版本发布，带来了多项重要更新，包括 Temporal API 的稳定化、Windows ARM 原生支持、npm overrides 功能增强，以及大量 Node.js 兼容性改进和开发者体验优化。

- 🗓️ **Temporal API 稳定化**：移除了 `--unstable-temporal` 标志，现在可直接使用，提供了更强大的日期时间处理能力。
- 💻 **Windows ARM 原生支持**：为 ARM 架构的 Windows 设备（如 Surface Pro X）提供官方构建版本，无需 x86 模拟，性能更优。
- 📦 **package.json overrides 支持**：允许在依赖树中精确控制特定包的版本，便于修复安全漏洞或强制兼容性。
- 🔧 **新增子进程 API**：引入了 `Deno.spawn()`、`Deno.spawnAndWait()` 等简化函数（目前标记为不稳定），使子进程操作更便捷。
- 🔄 **Node.js 兼容性大幅提升**：修复了 `node:worker_threads`、`node:child_process`、`node:zlib` 等模块的数十个问题，增强了与现有 Node.js 生态的互操作性。
- 🌐 **API 新增与改进**：包括 `navigator.platform` 支持、Brotli 压缩流、非阻塞文件锁 `FsFile.tryLock()`、SHA3 加密算法以及 GIF/WebP 图像解码等。
- 🛠️ **包管理器功能增强**：新增 `deno create` 脚手架命令、`deno install --compile` 编译独立可执行文件、`--save-exact` 精确版本锁定，以及 `jsr:` 协议在 `package.json` 中的直接支持。
- ⚡ **开发者体验优化**：包括 `deno compile --self-extracting` 自解压二进制、`deno task` 支持 `pipefail` 等 shell 配置、`deno check --check-js` 对纯 JavaScript 项目的类型检查，以及调试工具对 Web Workers 的全面支持。
- 🔒 **安全与维护增强**：新增 `deno audit --ignore` 忽略特定 CVE、`deno upgrade` 支持校验和验证、`SSLKEYLOGFILE` 环境变量支持 TLS 会话密钥记录，以及 OpenTelemetry 对 `Deno.cron` 的自动集成。
- 🚀 **性能与底层更新**：升级至 V8 14.5 引擎，带来性能提升和新 JavaScript 特性，同时修复了大量错误并优化了运行时行为。

---

### [Expo SDK 55 - 更新日志](https://expo.dev/changelog/sdk-55)

**原文标题**: [Expo SDK 55 - Expo Changelog](https://expo.dev/changelog/sdk-55)

Expo SDK 55 正式发布，包含 React Native 0.83 和 React 19.2，并引入了多项重要更新，包括新的项目模板、Hermes v1 支持、AI 工具增强、Brownfield 应用改进、Expo Router 功能扩展以及多个模块的稳定与实验性功能。

- 🚀 **SDK 55 发布**：包含 React Native 0.83 和 React 19.2，SDK 56 计划于第二季度发布。
- 📱 **过渡期安排**：Expo Go 和应用商店项目暂时保持 SDK 54，建议迁移至开发构建。
- 🎨 **新项目模板**：采用原生标签 API、更新设计和 /src 文件夹结构，提升开发体验。
- 🏗️ **弃用旧架构**：SDK 55 起不再支持旧架构，相关配置已移除。
- ⚡ **Hermes v1 支持**：提供性能改进和现代 JavaScript 功能支持，但需从源码构建。
- 📦 **字节码差分更新**：通过 Hermes 字节码差分优化，减少更新下载大小和带宽使用。
- 🤖 **AI 工具扩展**：Expo MCP 支持 CLI 操作和 EAS 查询，新增官方 AI 技能库。
- 🔗 **Brownfield 应用改进**：新增 `expo-brownfield` 包，支持集成和隔离两种开发模式。
- 🧭 **Expo Router 增强**：新增颜色 API、Apple 缩放过渡、工具栏 API 等原生功能。
- 🎭 **Expo UI 更新**：Jetpack Compose 和 SwiftUI 组件大幅改进，更贴近原生开发体验。
- 📦 **包版本统一**：所有 Expo SDK 包版本与 SDK 主版本号对齐，便于兼容性管理。
- 🛠️ **模块与工具更新**：包括 Expo Modules Core 功能增强、CLI 改进、实验性小部件支持等。
- 📢 **模块亮点**：多个模块如 `expo-blur`、`expo-sharing`、`expo-audio` 等新增稳定或实验性功能。
- ⚠️ **弃用与破坏性变更**：移除旧配置、更新工具链、调整 API，需注意升级影响。
- 🔧 **升级指南**：提供依赖升级、问题检查和构建更新步骤，支持通过 AI 技能辅助升级。
- 👏 **致谢贡献者**：感谢团队和外部贡献者的辛勤工作与测试支持。

---

### [尸鬼](https://shiki.style/)

**原文标题**: [Shiki](https://shiki.style/)

准确美观的文本编辑器，采用与 VS Code 相同的语法引擎，随 VS Code 同步优化提升。

- 🌈 采用与 VS Code 相同的语法引擎，确保代码高亮和语法分析的准确性
- 🎨 界面美观，提供优质的视觉体验
- 🔄 与 VS Code 同步优化，持续改进功能与性能

---

### [发布 21.2.0 · angular/angular · GitHub](https://github.com/angular/angular/releases/tag/v21.2.0)

**原文标题**: [Release 21.2.0 · angular/angular · GitHub](https://github.com/angular/angular/releases/tag/v21.2.0)

Angular 框架发布了 21.2.0 版本，包含多项核心功能增强、编译器优化、表单改进、语言服务更新及路由器功能扩展。

- 🚀 编译器新增 `instanceof` 操作符支持与 switch 块详尽检查，优化视图调用
- 🔧 核心模块引入 `ChangeDetectionStrategy.Eager` 别名，支持 TypeScript 6 及嵌套动画
- 📝 表单系统增强，新增 `SignalFormControl`、解析错误处理及提交选项配置
- 💬 语言服务与服务器提供内联样式补全、折叠范围及 JSON 架构支持
- 🛣️ 路由器更新 `canMatch` 参数与 `IsActiveMatchOptions` API，使匹配选项可选
- 🐛 修复了动态组件在无区域模式下的动画元素重复等问题

---

### [发布 v1.35.0 · Vanilagy/mediabunny · GitHub](https://github.com/Vanilagy/mediabunny/releases/tag/v1.35.0)

**原文标题**: [Release v1.35.0 · Vanilagy/mediabunny · GitHub](https://github.com/Vanilagy/mediabunny/releases/tag/v1.35.0)

该版本 v1.35.0 主要增加了对非正方形像素视频帧（SAR 非 1:1）的读写支持，并引入了新的视频相关字段和工具类型。

- 🎥 新增对 ISOBMFF、Matroska 和 MPEG-TS 格式中非正方形像素视频帧的读写支持
- 📐 为 VideoSample 添加 pixelAspectRatio、squarePixelWidth、squarePixelHeight 和 visibleRect 字段
- 🔧 为 InputVideoTrack 新增 pixelAspectRatio、squarePixelWidth 和 squarePixelHeight 字段
- 🛠️ 引入 Rational 和 Rectangle 两种新的实用工具类型
- 🐛 修复了 VideoSample 构造函数中部分参数缺少运行时验证的问题

---

### [发布 Neo.mjs v12.0.0 版本说明 · neomjs/neo · GitHub](https://github.com/neomjs/neo/releases/tag/12.0.0)

**原文标题**: [Release Neo.mjs v12.0.0 Release Notes · neomjs/neo · GitHub](https://github.com/neomjs/neo/releases/tag/12.0.0)

Neo.mjs v12.0.0 是一次重大的架构革新，专注于极致性能与多线程优化。它通过全新的旗舰应用 DevIndex 展示了处理 5 万条实时更新记录的能力，核心改进包括引擎级流式处理、虚拟字段和五线程网格架构，同时保持了 API 的完全向后兼容。

- 🚀 **重大架构革新**：v12.0.0 是一次彻底的核心引擎重写，引入了“零开销”更新，专注于对象持久性和极致性能，无需迁移现有代码。
- 🏆 **旗舰应用 DevIndex**：构建了一个实时排名 5 万 GitHub 开发者的“胖客户端”应用，整个数据集在内存中处理，实现零延迟排序和过滤，无需后端服务器。
- ⚙️ **核心性能技术**：实现了**引擎级流式处理**（JSONL 代理）、**虚拟字段**（零内存开销）和**软水合**，以绕过对象实例化，大幅提升数据处理效率。
- 🧵 **五线程网格架构**：将网格工作负载拆分到五个独立线程（应用、VDom、数据、Canvas、主线程），实现了 O(1) 滚动性能和恒定的内存使用，通过严格的 DOM 池实现零 DOM 变异。
- 🛡️ **对抗垃圾回收**：在整个引擎的热路径中进行了全面的内存分配审计，消除了隐藏的分配，例如用 `slice()` 替换数组展开运算符，以减轻 V8 垃圾回收压力。
- 🔗 **动态工作者架构**：实现了按需启动工作者协议，高级组件（如 Sparkline）可以自主启动所需的 Canvas Worker，实现零配置。
- 🌐 **通用应用引擎**：证明了 Neo.mjs 核心架构同样适用于 Node.js 后端，DevIndex 的数据工厂后端就是基于此构建的微服务管道。
- 📚 **丰富文档与案例**：为 DevIndex 项目添加了 26 篇详细指南，涵盖从伦理宣言到前后端架构的方方面面，并分享了四个具体的工程“战争故事”来剖析性能优化过程。
- 📦 **大量问题修复与增强**：此次版本共解决了 402 个工单，涵盖了网格、数据层、核心引擎、性能优化以及测试基础设施的各个方面，所有更改均在一个原子提交中交付。

---

### [获取失败](https://javascriptweekly.com/link/181416/web)

**原文标题**: [Failed to retrieve](https://javascriptweekly.com/link/181416/web)

无法总结：获取内容失败，状态码 403。

---

### [引言 - WebAssembly 组件模型](https://component-model.bytecodealliance.org/)

**原文标题**: [Introduction - The WebAssembly Component Model](https://component-model.bytecodealliance.org/)

WebAssembly 组件模型是一种用于构建可互操作的 WebAssembly 库、应用和环境的广泛架构，旨在通过组合现有功能实现新功能。组件在平台（如浏览器、独立运行时或操作系统）上运行，平台为组件提供与外界交互的 API（如 WASI 标准），同时组件为平台扩展功能。

- 🧩 WebAssembly 组件模型通过组合现有功能构建可互操作的应用，运行于多种平台
- 🌍 平台为组件提供外部交互 API（如 WASI 标准），组件为平台扩展新功能
- 📅 WASI 0.2.0 为稳定版本，提供标准接口定义，未来版本将持续演进
- 🔧 文档面向组件用户（开发者），运行时开发者可参考规范实现支持
- 🤝 可通过 GitHub 反馈问题或参与内容贡献

---

### [我们值得为 JavaScript 拥有一个更好的流式 API。](https://blog.cloudflare.com/a-better-web-streams-api/)

**原文标题**: [We deserve a better streams API for JavaScript](https://blog.cloudflare.com/a-better-web-streams-api/)

本文探讨了当前 Web Streams API 存在的根本性可用性和性能问题，并提出了一种基于 JavaScript 语言原语（特别是异步迭代器）的替代方案。该方案通过简化设计、采用拉取式转换、明确背压策略和批处理块等原则，显著提升了性能，在多个运行时中实现了 2 倍到 120 倍的性能提升。

- 🚀 **性能瓶颈**：Web Streams API 设计复杂，包含大量 Promise 创建和内部状态管理，导致高开销，尤其在处理高频小数据块时性能下降显著。
- 🔒 **锁机制问题**：手动锁管理（如`getReader()`和`releaseLock()`）容易出错，忘记释放锁会导致流永久锁定，增加调试难度。
- 🧩 **BYOB 复杂性**：BYOB（自带缓冲区）读取 API 复杂且使用率低，增加了实现和使用的负担，而实际优化效果有限。
- ⚖️ **背压机制缺陷**：背压信号（如`desiredSize`）仅为建议性，缺乏强制执行力，容易导致内存无限制增长，尤其在`tee()`和`TransformStream`中问题突出。
- 🔄 **转换流问题**：`TransformStream`采用推送模型，可能在没有消费者时仍进行数据处理，导致不必要的计算和缓冲，背压传递存在漏洞。
- 🗑️ **GC 压力**：在服务器端渲染等场景中，大量小数据块处理导致频繁的 Promise 和对象分配，引发垃圾回收压力，影响吞吐量和延迟。
- 🛠️ **优化负担**：各运行时为实现可接受性能，不得不采用非标准内部优化，导致行为不一致和可移植性问题，增加实现和维护复杂度。
- 🔗 **替代方案优势**：新方案基于异步迭代器，简化了流的创建和消费，采用拉取式转换、明确背压策略和批处理块，性能显著提升，且更符合现代 JavaScript 开发模式。
- 📊 **性能对比**：基准测试显示，新方案在多种场景下（如小数据块处理、链式转换）相比 Web Streams 有数倍到数十倍的性能提升，尤其在浏览器和服务器运行时中表现一致。
- 🔮 **未来展望**：作者旨在通过此方案引发讨论，探索更简单、高效且符合语言发展的流 API 设计，并提供了参考实现供社区试用和反馈。

---

### [CLI 安装程序 – AuthKit – WorkOS 文档](https://workos.com/docs/authkit/cli-installer?utm_source=cpjavascript&utm_medium=referral&utm_campaign=q12026)

**原文标题**: [CLI Installer – AuthKit – WorkOS Docs](https://workos.com/docs/authkit/cli-installer?utm_source=cpjavascript&utm_medium=referral&utm_campaign=q12026)

WorkOS CLI 安装工具能自动检测项目框架并快速集成 AuthKit 身份验证功能，实现约两分钟内从零到完整配置。

- 🛠️ **自动集成流程**：通过单一命令自动完成框架检测、SDK 安装、路由创建、环境变量配置和构建验证
- 🌐 **多框架支持**：兼容 Next.js、React、SvelteKit、Node.js/Express 等主流开发框架
- 🔒 **安全配置**：自动设置 OAuth 回调 URI、CORS 来源和仪表板配置
- 🤖 **智能分析**：AI 代理会分析项目结构并生成适配代码，保留现有中间件配置
- ⚙️ **灵活选项**：支持自定义重定向 URI、跳过验证等命令行参数
- 🐛 **故障排查**：提供调试模式、差异查看和诊断工具解决安装问题

---

### [JavaScript DRM 的幻象：HotAudio 版权保护的三轮拆解](https://www.therantydev.com/javascript-drms-are-stupid)

**原文标题**: [
      The Illusion of JavaScript DRM: A Three-Round Demolition of HotAudio's Copy Protection

    ](https://www.therantydev.com/javascript-drms-are-stupid)

本文探讨了 JavaScript DRM 的固有缺陷，以 HotAudio 平台为例，详细分析了其基于 JavaScript 的 DRM 系统如何被逐步破解，并论证了在客户端环境中实现真正有效 DRM 的不可能性。

- 🔓 JavaScript DRM 本质上是“用户空间”的，代码对用户完全可见且可修改，无法提供真正的保护。
- 🛡️ 真正的 DRM 依赖于硬件可信执行环境（TEE），如 Widevine，但这需要商业授权和原生集成，小型平台无法实现。
- 🎯 攻击的核心在于“PCM 边界”：无论前端加密多复杂，音频数据最终必须在 JavaScript 中解密才能交给浏览器解码，这个解密瞬间是可拦截的。
- 🕵️ 第一轮破解通过全局变量暴露和篡改`nozzle.js`脚本，直接拦截`appendBuffer`方法捕获解密后的音频数据。
- 🔧 开发者随后通过移除全局变量、添加哈希验证和`toString()`反篡改检查进行防御。
- 🤥 第二轮破解使用`mockToString`函数让被钩子函数伪装成原生代码，并通过钩住`HTMLMediaElement.prototype.play`等方法，无论播放器实例如何隐藏都能捕获。
- 🚫 开发者尝试使用 iframe、Shadow DOM 和`srcObject`进行隔离。
- ⚙️ 第三轮破解通过钩住`HTMLMediaElement.prototype`的`src`/`srcObject`属性描述符、`MediaSource.prototype.addSourceBuffer`以及使用捕获阶段事件监听器，实现了几乎无死角的拦截。
- ⚡ 自动化脚本通过静音、16 倍速播放和自适应缓冲监控来快速获取完整音频数据。
- 📜 最终使用`spoof`函数完美伪造原生函数的`toString`输出，以通过更严格的完整性检查。
- 🤔 作者认为，对于小型 NSFW 音频平台，JavaScript DRM 已是其能力范围内最复杂的“摩擦”机制，但将其称为“DRM”会误导用户对其安全性的期望。
- 💭 文章质疑 DRM 对 ASMR 创作者的真正价值，并指出其无法阻止有动机的攻击者，但理解开发者保护内容收入的初衷。
- ⚠️ 所有操作均在客户端浏览器内完成，未干扰服务器基础设施。

---

### [加密媒体扩展 - 维基百科](https://en.wikipedia.org/wiki/Encrypted_Media_Extensions)

**原文标题**: [Encrypted Media Extensions - Wikipedia](https://en.wikipedia.org/wiki/Encrypted_Media_Extensions)

加密媒体扩展（EME）是 W3C 制定的一项规范，旨在为网页浏览器与实现数字版权管理（DRM）的内容解密模块（CDM）软件之间建立通信通道。它允许 HTML 视频播放受 DRM 保护的流媒体内容，无需依赖 Adobe Flash 或 Microsoft Silverlight 等第三方插件。EME 基于媒体源扩展（MSE），支持自适应比特率流媒体（如 MPEG-DASH），但因其依赖专有、封闭的解密组件并涉及许可费用，引发了开源社区和隐私倡导者的广泛争议。

- 🔐 EME 是 W3C 规范，用于浏览器与 DRM 解密模块之间的通信，实现 HTML5 视频播放加密内容  
- 🌐 旨在替代 Flash 等插件，支持流媒体服务（如 Netflix）的 DRM 保护内容播放  
- ⚙️ 基于媒体源扩展（MSE），可结合 MPEG-DASH 等技术实现自适应比特率流媒体  
- 🚫 因依赖专有解密组件、许可费用和隐私问题，遭到电子前沿基金会等组织的强烈反对  
- 🌍 主流浏览器（Chrome、Firefox、Safari、Edge 等）均已支持 EME，但实现方式各异  
- 🔧 常用内容解密模块（CDM）包括 Widevine、PlayReady、FairPlay 等，部分需付费授权  
- 🛡️ 批评焦点包括对开源浏览器的限制、互操作性不足、隐私风险及 DMCA 法律隐患  
- 📉 2020 年后，独立开源浏览器面临 CDM 授权壁垒，加剧了生态封闭性担忧

---

### [我们如何在一周内用 AI 重建 Next.js](https://blog.cloudflare.com/vinext/)

**原文标题**: [How we rebuilt Next.js with AI in one week](https://blog.cloudflare.com/vinext/)

上周，一位工程师与 AI 模型在一周内从零重建了最流行的前端框架 Next.js，推出了基于 Vite 的替代品 vinext。它可一键部署至 Cloudflare Workers，生产构建速度提升高达 4 倍，客户端包体积缩小 57%，且已有客户在生产环境中使用。整个项目仅消耗约 1100 美元的 AI 令牌成本。

- 🚀 **快速构建** – vinext 基于 Vite 开发，生产构建速度比 Next.js 快 4 倍，客户端包体积减少 57%
- 🔄 **无缝迁移** – 直接替换 Next.js，兼容现有 app/、pages/和 next.config.js 配置
- ☁️ **一键部署** – 支持单命令部署到 Cloudflare Workers，自动生成配置并处理全流程
- ⚡ **性能优势** – 利用 Vite 架构和 Rolldown（Rust 打包工具），在编译和打包速度上具有结构优势
- 🧩 **平台兼容** – 基于 Vite 环境 API，可在多平台运行，95% 代码与 Cloudflare 无关
- 🔧 **缓存灵活** – 内置 Cloudflare KV 缓存处理器，支持 ISR，并可插拔替换为 R2 等其他后端
- 🧪 **实验特性** – 推出流量感知预渲染（TPR），根据实际访问量智能预渲染页面，避免资源浪费
- 🤖 **AI 驱动开发** – 项目几乎全部由 AI 编写，通过 1700+ 单元测试和 380+ 端到端测试保障质量
- 📦 **生态友好** – 开源项目，欢迎其他平台贡献，已验证可在 Vercel 等平台运行
- ⚠️ **实验阶段** – 目前仍为实验性项目，尚未经过大规模流量测试，生产使用需谨慎

---

### [GitHub - cloudflare/vinext：重新实现Next.js API 界面的 Vite 插件——随处部署 · GitHub](https://github.com/cloudflare/vinext)

**原文标题**: [GitHub - cloudflare/vinext: Vite plugin that reimplements the Next.js API surface — deploy anywhere · GitHub](https://github.com/cloudflare/vinext)

vinext 是一个基于 Vite 的实验性插件，旨在重新实现 Next.js 的 API 接口，使现有的 Next.js 应用能够在 Vite 工具链上运行，并支持部署到包括 Cloudflare Workers 在内的多种平台。

- 🚀 **快速迁移**：提供 `vinext init` 命令自动化迁移现有 Next.js 项目，支持 App Router 和 Pages Router，兼容约 94% 的 Next.js 16 API。
- 🌐 **多平台部署**：原生支持 Cloudflare Workers（通过 `vinext deploy`），也可通过 Nitro 插件部署到 Vercel、Netlify、AWS 等其他平台。
- ⚡ **Vite 驱动**：基于 Vite 构建，具备快速的 HMR 和现代构建工具链，利用 `@vitejs/plugin-rsc` 实现 React Server Components 支持。
- 🧪 **实验性质**：项目主要由 AI 生成代码，尚未经过全面人工审查，可能存在缺陷，建议谨慎用于生产环境。
- 🔧 **灵活配置**：支持自定义 Vite 配置，可集成 Cloudflare Workers 绑定（如 D1、R2、KV）并通过 `cloudflare:workers` 直接访问。
- 📊 **测试覆盖**：包含超过 1,700 项 Vitest 测试和 380 项 Playwright E2E 测试，确保核心功能稳定性。
- ⚠️ **已知限制**：暂不支持 Vercel 特定功能、AMP 及完整的图片优化（本地图片依赖运行时处理），Google Fonts 仅通过 CDN 加载。

---

### [GitHub - cloudflare/vinext：重新实现Next.js API 界面的 Vite 插件——随处部署 · GitHub](https://github.com/cloudflare/vinext#whats-not-supported-and-wont-be)

**原文标题**: [GitHub - cloudflare/vinext: Vite plugin that reimplements the Next.js API surface — deploy anywhere · GitHub](https://github.com/cloudflare/vinext#whats-not-supported-and-wont-be)

vinext 是一个基于 Vite 的实验性插件，旨在重新实现 Next.js 的 API 接口，使现有的 Next.js 应用能够在 Vite 工具链上运行，并支持部署到包括 Cloudflare Workers 在内的多种平台。

- 🚀 **快速迁移**：提供 `vinext init` 命令和 AI 助手技能，可自动化迁移现有 Next.js 项目，支持渐进式采用。
- 🌐 **多平台部署**：原生支持 Cloudflare Workers（含一键部署和绑定访问），并通过 Nitro 插件兼容 Vercel、Netlify、AWS 等其他平台。
- ⚙️ **API 兼容性**：覆盖约 94% 的 Next.js 16 API，包括 Pages Router、App Router、RSC、服务器操作、中间件和缓存等功能。
- 🔧 **配置灵活**：自动加载 Next.js 风格的配置文件（如 `next.config.js` 和 `.env` 文件），支持自定义 Vite 配置。
- 🧪 **实验性质**：项目主要由 AI 生成代码，尚未经过全面人工审查，存在已知限制（如图像优化和字体自托管功能不完整）。
- 📊 **性能基准**：在构建速度和客户端包大小上相比 Next.js 有优势，但生产环境性能取决于具体部署平台。
- 🛠️ **开发与测试**：包含完整的测试套件（Vitest 和 Playwright），并提供多个线上示例应用供参考。
- ⚠️ **注意事项**：明确不支持 Vercel 专有功能、AMP 等特性，且不追求与未公开行为的完全一致。

---

### [利用 Val Town 带我去看电影](https://www.raymondcamden.com/2026/03/01/using-val-town-to-get-me-to-the-movies)

**原文标题**: [Using Val Town to Get Me to the Movies](https://www.raymondcamden.com/2026/03/01/using-val-town-to-get-me-to-the-movies)

作者利用 The Movie Database API 和 Val Town 构建了一个工具，用于定期获取即将上映的电影信息，并通过电子邮件发送提醒，以帮助自己和妻子更频繁地去电影院观影。

- 🎬 为解决忘记新片上映的问题，作者使用 TMDB 的 Upcoming Movies API 获取电影数据，并构建了一个展示页面。
- 💻 初始版本通过 JavaScript 和 HTML 创建了一个电影信息展示页面，包含电影标题、简介、海报和上映日期。
- 🔄 在 Val Town 中创建定时任务，每周日中午自动获取电影数据并生成 HTML 内容，通过电子邮件发送给自己。
- 📧 利用 Val Town 的免费邮件功能实现提醒，代码中导入电影数据函数并格式化邮件内容。
- 🛠️ 项目代码公开在 Val Town 上，方便查看和复用，同时作者提供了支持其创作的途径。

---

### [瓦尔镇](https://www.val.town/)

**原文标题**: [Val Town](https://www.val.town/)

Val Town 是一个面向开发者的无服务器平台，允许用户快速编写、部署和运行 TypeScript 代码，用于构建小型应用、API、AI 代理、定时任务等，无需管理基础设施。

- 🚀 **快速部署**：支持即时部署 TypeScript 代码，无需配置服务器或运维
- 🔧 **多功能用途**：可用于构建 Web 应用、API、AI 代理、定时任务、Slack 机器人等
- 💡 **简化开发**：提供代码智能提示、版本控制、CLI 工具和 AI 编程助手
- 🆓 **免费起步**：提供免费入门方案，适合个人和小团队快速验证想法
- 🤝 **团队协作**：受多个技术团队推崇，用于快速搭建销售演示 API、自动化营销流程等
- ⏰ **定时任务**：支持一键调度函数执行，适合自动化工作流
- 🌐 **模板丰富**：提供多种入门模板，如邮件订阅表单、用户信息丰富等
- 🔌 **集成便捷**：可轻松与 Clay、Attio、Slack 等第三方服务集成

---

### [粘性网格滚动：构建滚动驱动的动画网格 | Codrops](https://tympanus.net/codrops/2026/03/02/sticky-grid-scroll-building-a-scroll-driven-animated-grid/)

**原文标题**: [Sticky Grid Scroll: Building a Scroll-Driven Animated Grid | Codrops](https://tympanus.net/codrops/2026/03/02/sticky-grid-scroll-building-a-scroll-driven-animated-grid/)

本文介绍如何构建一个滚动驱动的粘性网格动画，通过 GSAP、ScrollTrigger 和 Lenis 实现视觉元素的渐进式展开，强调节奏、间距和结构化的动画设计。

- 🎨 动画设计理念：以滚动为驱动，在固定场景中逐步展开网格动画，注重节奏与结构而非堆叠效果
- 🛠️ 技术栈：基于 GSAP 实现精确动画，ScrollTrigger 绑定滚动事件，Lenis 提供平滑滚动体验
- 📐 结构设计：采用粘性布局，包含固定场景区、12 图网格和主时间轴三个核心部分
- 📊 滚动映射：将滚动进度划分为四个阶段（0-45% 网格进入、45-90% 展开、90-95% 内容聚焦、95-100% 稳定）
- 🏗️ HTML 结构：简洁分层设计，分离文本内容与画廊区域，便于独立控制动画
- 🎯 CSS 策略：使用流体 rem 系统实现响应式缩放，通过 425vh 高度创造动画时间空间
- ⚙️ JavaScript 架构：封装为 StickyGridScroll 类，模块化处理元素获取、状态初始化、列分组和动画编排
- 📈 时间轴编排：主时间轴协调网格显示、缩放和内容切换，子时间轴处理列级动画
- 🔄 交互逻辑：滚动方向触发内容显隐，动态计算元素位置保持视觉平衡
- 🚀 扩展性：系统设计支持节奏调整、布局替换和动画阶段重组，保持逻辑一致性

---

### [粘性网格滚动 | Codrops](https://tympanus.net/Tutorials/StickyGridScroll/)

**原文标题**: [Sticky Grid Scroll | Codrops](https://tympanus.net/Tutorials/StickyGridScroll/)

一个关于滚动驱动布局的实验，通过粘性网格实现图片在滚动时渐进展示的动态效果。

- 📐 结构化滚动驱动图像网格
- 🧩 粘性布局中渐进展开的动效
- 🎓 附带详细教程说明

---

### [从 instanceof 到 Error.isError：JavaScript 中更安全的错误检查方法 - Matt Smith](https://allthingssmitty.com/2026/02/23/from-instanceof-to-error-iserror-safer-error-checking-in-javascript/)

**原文标题**: [
    From instanceof to Error.isError: safer error checking in JavaScript - Matt Smith
  ](https://allthingssmitty.com/2026/02/23/from-instanceof-to-error-iserror-safer-error-checking-in-javascript/)

JavaScript 开发者长期以来依赖 `instanceof` 进行错误检查，但在跨领域（如 iframe、Worker）时可能静默失败，导致错误被错误处理或日志系统忽略。新引入的 `Error.isError()` 方法提供了跨领域安全的错误检查，能准确识别真实错误对象，包括自定义错误类，且不会抛出异常。建议在涉及跨边界处理的代码中使用，并通过特性检测优雅降级以兼容旧环境。

- 🚨 `instanceof Error` 在跨领域（如 iframe、Worker）时可能静默失败，导致错误被错误处理
- 🌐 JavaScript 领域（realms）拥有独立的全局对象和内置构造函数，使跨领域错误检查不可靠
- 🛡️ `Error.isError()` 提供跨领域安全的错误检查，准确识别真实错误对象且永不抛出
- ✅ 适用于 `Error`、`TypeError` 及正确继承的自定义错误类，跨领域返回 `true`
- 🚫 拒绝仅继承 `Error.prototype` 的非错误对象，浏览器中亦将 `DOMException` 视为错误
- 🔧 建议在全局错误处理、日志、测试框架、SSR 等跨边界场景中优先使用
- 📦 可通过特性检测包装函数渐进采用，现代环境（Chrome 134+、Node.js 24.3+）已支持

---

### [服务器端 JavaScript 中代理 fetch 请求 - Human Who Codes](https://humanwhocodes.com/blog/2026/03/proxying-fetch-requests-server-side-javascript/)

**原文标题**: [Proxying fetch requests in server-side JavaScript - Human Who Codes](https://humanwhocodes.com/blog/2026/03/proxying-fetch-requests-server-side-javascript/)

本文介绍了如何在 Node.js、Deno、Bun 和 Cloudflare Workers 等服务器端 JavaScript 运行时中代理 fetch() 请求，以实现流量监控、性能优化等目的。

- 🌐 代理 fetch 请求可用于记录流量、修改头部、缓存内容或隐藏 IP 地址，是服务器开发的常见需求
- 📦 Node.js 需通过安装 undici 包并使用 ProxyAgent 类来设置代理，示例代码展示了具体配置方法
- 🦕 Deno 通过 createHttpClient() 方法创建代理客户端，支持 HTTP/HTTPS 代理，使用后需记得关闭客户端
- 🐰 Bun 原生支持 proxy 属性配置代理，实现方式最为简洁直接
- ⚡ Cloudflare Workers 需借助 Docker 容器和专用工具包@humanwhocodes/proxy-fetch-server 来实现代理功能
- 🔧 不同运行时对代理的支持程度各异，Deno 和 Bun 提供直接 API，而 Node.js 和 Cloudflare Workers 需要额外配置
- 🛠️ 掌握这些代理技术有助于构建更安全、可靠且高效的服务器端应用

---

### [为何我选择 Electron 而非原生开发（并且我还会再次选择）- Syntax #983](https://syntax.fm/show/983/why-i-chose-electron-over-native-and-i-d-do-it-again)

**原文标题**: [Why I Chose Electron Over Native (And Iâd Do It Again) - Syntax #983](https://syntax.fm/show/983/why-i-chose-electron-over-native-and-i-d-do-it-again)

在 Syntax 播客第 983 集中，Wes 和 Scott 讨论了开发 v_framer（一款自定义多源视频录制应用）的过程，并解释了为何选择 Electron 而非 Tauri 或原生 API。他们深入探讨了技术选型、应用功能、商业化及发布挑战。

- 🎙️ 播客主题围绕开发 v_framer 应用，重点讨论为何 Electron 在桌面应用开发中胜出
- 🛠️ 应用需求包括多源录制、防崩溃、自动更新和自定义功能（如键盘快捷键与 FPS 锁定）
- 🔄 比较了 Tauri、WKWebView 和 Electron，最终因 Electron 的稳定性和清晰录制效果而选择它
- 📦 技术实现涉及 MKV 与 WebM 格式选择、浏览器捕获与原生 API 的权衡
- 🚀 发布流程涵盖 Mac 应用公证、证书管理及使用 CI/CD 实现自动更新
- 💰 商业化方面采用一次性购买、试用模式，并自托管 Keygen 进行许可证管理
- 📊 通过 Google Sheets 建立等待列表，以灵活方式收集用户需求
- 🎯 总结强调 Electron 在快速迭代和跨平台发布中的优势，适合需要高效开发桌面应用的场景

---

### [React Native 登陆 Meta Quest · React Native](https://reactnative.dev/blog/2026/02/24/react-native-comes-to-meta-quest)

**原文标题**: [React Native Comes to Meta Quest · React Native](https://reactnative.dev/blog/2026/02/24/react-native-comes-to-meta-quest)

React Native 现已正式支持 Meta Quest 设备，使开发者能够利用熟悉的工具和模式构建 VR 应用。Meta Quest 运行基于 Android 的 Meta Horizon OS，因此现有的 Android 工具链和开发流程基本适用。开发者可通过 Expo Go 快速开始开发，并通过开发构建访问原生功能。平台需进行特定配置，并注意设计时需考虑 VR 的交互与显示特点。

- 🚀 **React Native 扩展至 Meta Quest**：在 React Conf 2025 上宣布官方支持，延续其跨平台愿景，使开发者能利用现有知识构建 VR 应用。
- 🛠️ **开发流程与移动端相似**：Meta Quest 基于 Android，因此现有 Android 开发工具、构建系统和调试工作流只需最小调整即可使用。
- 📱 **通过 Expo Go 快速开始**：在头显上安装 Expo Go 后，扫描 QR 码即可运行标准 Expo 项目，支持实时重载和快速迭代。
- ⚙️ **开发构建与原生功能**：当需要访问原生模块或深度平台集成时，可使用标准的 Expo 开发构建工作流在 Quest 设备上直接运行。
- 🔧 **平台特定配置**：需通过 `expo-horizon-core` 插件进行项目配置，包括设置 Horizon App ID、默认面板大小和支持的设备列表等。
- 📚 **库兼容性注意事项**：大多数 React Native 库可用，但需避免依赖移动端特有硬件、触摸输入或 Google 移动服务；Expo 为部分功能提供替代方案。
- 🎨 **VR 设计与用户体验考量**：设计需考虑头戴显示器的特点，如更大的点击目标、可读性强的排版，并支持控制器、手部追踪等多种输入方式。
- 🔗 **资源与参考**：提供参考项目、官方文档、电子书、文章和播客等资源，帮助开发者深入学习和开始构建。

---

### [微型 JavaScript 运行时 | txiki.js](https://txikijs.org/)

**原文标题**: [The tiny JavaScript runtime | txiki.js](https://txikijs.org/)

一个轻量且功能强大的 JavaScript 运行时环境。

- 🚀 小巧而强大
- ⚙️ 专为现代 JavaScript 设计
- 📚 快速上手使用

---

### [冬季 TC](https://wintertc.org/)

**原文标题**: [WinterTC](https://wintertc.org/)

WinterTC 是 Ecma 国际技术委员会，专注于推动服务器端 JavaScript 运行时之间的 API 互操作性，特别是与 Web 共享的 API，通过标准化“最小公共 API”并与 Web 标准组织合作，以促进服务器端与 Web 环境的一致性。

- 🌐 致力于服务器端 JavaScript 运行时的 API 互操作性
- 🔗 标准化与 Web 共享的“最小公共 API”
- 🤝 与 WHATWG、W3C 等 Web 标准组织协作
- 📜 发布新的互操作性服务器端 API 标准
- 👥 参与方包括 Bloomberg 等组织

---

### [GitHub - saghul/txiki.js：一个微型的JavaScript运行时环境 · GitHub](https://github.com/saghul/txiki.js)

**原文标题**: [GitHub - saghul/txiki.js: A tiny JavaScript runtime · GitHub](https://github.com/saghul/txiki.js)

txiki.js 是一个小巧而强大的 JavaScript 运行时，基于 QuickJS-ng 引擎和 libuv 平台层构建，支持现代 ECMAScript 标准，并兼容 WinterTC 规范。

- 🚀 **快速开始**：通过 Git 克隆仓库并编译即可运行 REPL 环境
- 🌐 **Web 平台 API**：支持 fetch、WebSocket、Console、setTimeout、Crypto 及 Web Workers 等
- 🔌 **网络与 I/O**：提供 TCP、UDP、Unix 套接字、HTTP 服务器（含 WebSocket）及文件 I/O 功能
- ⚙️ **系统功能**：支持子进程管理、信号处理和独立可执行文件编译（tjs compile）
- 📚 **标准库扩展**：包含 tjs:sqlite、tjs:ffi、tjs:path、tjs:hashing 等模块
- 📖 **完整文档**：详细文档可通过 txikijs.org 获取
- 💻 **跨平台支持**：兼容 GNU/Linux、macOS、Windows 及其他 Unix 系统
- ❤️ **开源项目**：基于 MIT 许可证，由 saghul 及贡献者共同维护

---

### [numpy-ts - numpy-ts](https://numpyts.dev/)

**原文标题**: [numpy-ts - numpy-ts](https://numpyts.dev/)

numpy-ts 是一个为 TypeScript 和 JavaScript 设计的完整 NumPy 实现，提供与 Python NumPy 高度一致的 API，具备类型安全、可树摇优化和跨运行时支持等特点。

- 🧩 **高 API 覆盖率** – 实现了 476 个 NumPy 函数中的 94%，涵盖算术、线性代数、随机分布等广泛功能。
- 🛡️ **类型安全** – 所有函数、数据类型和数组操作均提供完整的 TypeScript 类型定义，可在编译时捕获错误。
- 🌳 **可树摇优化** – 支持按需导入，打包工具会自动移除未使用代码，保持生产构建体积小巧。
- ✅ **NumPy 验证** – 通过超过 6000 项测试直接对比 NumPy 输出，确保结果一致性。
- 📦 **零依赖** – 纯 TypeScript 实现，无需原生模块或 WebAssembly，可在任何 JavaScript 环境中运行。
- 🌐 **跨运行时支持** – 兼容 Node.js、Bun、Deno 及所有现代浏览器，适用于服务器和客户端场景。
- 🔄 **易于迁移** – API 设计尽可能贴近 NumPy，大部分代码可直接转换，并提供详细的迁移指南。

---

### [NumPy](https://numpy.org/)

**原文标题**: [NumPy](https://numpy.org/)

NumPy 是 Python 科学计算的基础包，提供强大的 N 维数组和数值计算工具，支持广泛的硬件平台和科学领域，拥有活跃的开源社区和丰富的生态系统。

- 🚀 最新版本 NumPy 2.4.0 已于 2025 年 12 月发布
- 🔢 核心功能包括 N 维数组、向量化计算、广播机制和数学函数库
- 🌍 采用 BSD 开源协议，在 GitHub 上公开开发和维护
- 🔌 支持 GPU 计算、分布式处理和稀疏数组等硬件与库的互操作
- ⚡ 底层采用优化的 C 代码实现，兼具 Python 灵活性和编译语言速度
- 📚 高级语法设计使得不同背景的程序员都能轻松使用
- 🧪 提供浏览器交互式环境，可直接在线尝试代码示例
- 🔬 广泛应用于量子计算、统计学、信号处理、天文学等数十个科学领域
- 🏗️ 为 Dask、CuPy、PyTorch 等专业数组库提供 API 基础
- 📊 构成 Pandas、scikit-learn 等数据科学生态系统的核心组件
- 🖼️ 支持 Matplotlib、Seaborn 等可视化库处理大规模数据
- 🌌 曾应用于黑洞成像、引力波探测等重大科学发现案例

---

### [游乐场 - numpy-ts](https://numpyts.dev/v1.0.x/playground)

**原文标题**: [Playground - numpy-ts](https://numpyts.dev/v1.0.x/playground)

numpy-ts 是一个允许在浏览器中直接编写和运行代码的在线平台，无需安装即可使用其全部功能。

- 🌐 **浏览器内运行**：代码直接在浏览器中执行，通过 CDN 加载 numpy-ts 库，无需本地安装。
- 📦 **预加载功能**：`np` 对象已预先包含所有 numpy-ts 函数，开箱即用。
- 🖥️ **即时输出**：使用 `console.log()` 打印结果，或通过最后表达式返回值查看输出。
- 🔗 **集成资源**：提供 Playground、指南、API 参考和示例，方便学习和实践。
- 🤖 **AI 辅助**：平台由 AI 技术支持，响应可能包含自动生成的内容。

---

### [TimescaleDB：PostgreSQL 时序数据库 | 虎数 | 虎数](https://www.tigerdata.com/timescaledb?utm_source=cooperpress&utm_medium=referral&utm_campaign=javascript-weekly-newsletter)

**原文标题**: [TimescaleDB: PostgreSQL Time-Series DB | Tiger Data | Tiger Data](https://www.tigerdata.com/timescaledb?utm_source=cooperpress&utm_medium=referral&utm_campaign=javascript-weekly-newsletter)

TimescaleDB 是基于 PostgreSQL 构建的时序数据库，提供自动分区、行列混合存储、高达 95% 的压缩率、增量物化视图等核心功能，适用于物联网、加密货币和实时分析等场景。其托管云服务 Tiger Cloud 提供数据分层、统一数据架构、弹性扩展和高可用性等优势，同时提供开源自托管选项。

- 🗄️ 自动分区：通过超表实现按时间或 ID 自动分区，支持快速数据摄取和大规模查询优化
- 💾 混合存储：结合行存储和列存储，在降低成本的同时提升分析查询性能
- 📦 高效压缩：采用列式编码技术，压缩率高达 95%，支持在压缩数据上直接过滤和聚合
- 🔄 增量视图：通过连续聚合实现增量刷新的数据汇总，支持实时模式包含最新变更
- 🤖 自动化管理：内置任务调度器，提供列存储、保留策略和聚合刷新的可配置策略
- ⏱️ 时序函数：提供约 200 个原生 SQL 超函数，简化高级时序分析
- 🌐 云端优势：Tiger Cloud 提供数据分层、统一架构、弹性扩展、高可用性和安全合规等托管服务
- 🏠 自托管选项：支持在任何 PostgreSQL 环境安装，包含核心功能但需自行管理部分高级特性
- 🛠️ 专业支持：提供 24/7 专家帮助和技术指导，涵盖从原型到生产的全周期支持

---

### [Yoopta 编辑器 | 适用于 React 的无头富文本编辑器](https://yoopta.dev/)

**原文标题**: [Yoopta Editor | Headless Rich Text Editor for React](https://yoopta.dev/)

Yoopta 是一款免费开源的富文本编辑器框架，专为构建类似 Notion 的编辑器或自定义 CMS 应用而设计，提供丰富的插件和现代化功能，让开发者能够快速创建高性能的编辑体验。

- 📦 **免费开源**：基于 MIT 许可证，提供完整功能，无付费层级，支持商业项目
- 🧩 **插件丰富**：内置 20+ 插件，涵盖段落、标题、列表、表格、代码块、媒体嵌入等多样内容模块
- 🎨 **主题预设**：提供浅色/深色主题及 Shadcn UI 等预设，支持自定义主题
- 🖱️ **交互便捷**：支持拖拽排序、多块选择、键盘快捷键和 Markdown 快捷输入
- 📱 **多端适配**：响应式设计，移动端友好，支持触控操作
- 🔧 **高度可定制**：提供完整的程序化 API（编辑器、块、元素、插件命令等），支持创建自定义插件
- 📤 **灵活导出**：可导出为 HTML、Markdown、纯文本及邮件兼容的 HTML 格式
- ⚡ **性能优异**：基于 TypeScript 开发，类型安全，支持大型文档流畅编辑，提供撤销/重做功能
- 🚀 **未来功能**：即将推出实时协作、AI 内联编辑、插件市场、MDX 导入导出等增强特性
- 🤝 **社区支持**：拥有活跃的 Discord 社区和 GitHub 讨论区，由贡献者和赞助者共同维护

---

### [互动游乐场 | Yoopta 编辑器](https://yoopta.dev/playground)

**原文标题**: [Interactive Playground | Yoopta Editor](https://yoopta.dev/playground)

Yoopta 是一个现代化的富文本编辑器框架，提供 Beta 版本、示例、文档和交互式 Playground v6（测试版）等功能，帮助开发者快速上手和集成。

- 🚀 提供交互式 Playground v6（测试版）的实时演示和源代码
- 📚 包含详细文档和示例，支持快速入门
- ⭐ 鼓励用户星标仓库，获取更多更新和支持
- ⏱️ 宣称可在几分钟内开始使用，强调易用性和效率

---

### [AdonisJS v7 现已发布](https://adonisjs.com/blog/v7)

**原文标题**: [
      AdonisJS v7 is here
    ](https://adonisjs.com/blog/v7)

AdonisJS v7 是一次增量升级，带来了全面的类型安全、改进的开发者体验和新的功能模块，同时保持了与 v6 的最小化破坏性变更。

- 🚀 **现代化基础**：要求 Node.js 24+，更新了 Vite、ESLint 和 TypeScript 等工具链，并替换了 `dotenv` 等依赖为原生 API。
- 📦 **全新的启动套件**：提供 Hypermedia、API、React 和 Vue 四种功能齐全的套件，均内置 Lucid、Auth 及完整的登录/注册流程。
- 🔄 **简化的开发流程**：自动生成控制器、事件和策略的 Barrel 文件，并自动为路由命名，减少了样板代码。
- 🛡️ **端到端类型安全**：核心特性，通过代码生成实现了从路由定义、URL 构建、数据序列化到前端组件 Props 的全面类型检查。
- 🔗 **类型安全的 URL 构建与组件**：新的 `urlFor` 助手及 `<Link>`、`<Form>` 组件在前后端均提供类型安全的路径生成。
- 📤 **Transformer 数据层**：引入 Transformer 作为专门的序列化层，定义了 API 响应的类型化契约，并自动生成前端可用的数据类型。
- 🖥️ **类型安全的 Inertia 集成**：`inertia.render` 现在能根据页面组件自动生成的类型映射，确保传递正确的 Props。
- 🌐 **类型安全的 API 客户端**：通过 Tuyau 为独立前端应用提供完全类型化的 API 调用体验。
- 🛠️ **开发者体验增强**：包括环境变量文件读取、密钥类型保护、多重速率限制、智能迁移生成、简化的 Auth 设置、Vite HMR 端口自动分配等。
- 🔐 **全新的加密模块**：支持多驱动、密钥轮换和确定性加密，便于数据库查询。
- 📊 **可观测性**：推出 `@adonisjs/otel` 包，集成 OpenTelemetry 进行应用追踪。
- 🗃️ **Lucid ORM 改进**：引入“迁移优先”的 Schema 类生成，模型无需重复定义列信息。
- ⚙️ **增强的 Codemods**：为包作者和工具提供了更多自动化代码修改能力。
- 📝 **内容与 Markdown**：新增 `edge-markdown` 包用于在 Edge 模板中渲染 MDC，以及 `@adonisjs/content` 包用于管理类型化的静态内容集合。
- 🐛 **全新的错误页面**：重写了 Youch 错误页面，体积更小，兼容性更好。
- ⚡ **平台原生 Response 支持**：控制器现在可以直接返回原生的 `Response` 对象。
- 🔒 **安全加固**：修复了文件上传路径遍历、Lucid 批量赋值等安全漏洞。
- ❤️ **致谢与未来**：感谢核心团队、赞助者和社区。未来将专注于队列、工作流、调度器和 AI SDK 等功能的开发。

---

### [AdonisJS - 全功能 TypeScript 框架](https://adonisjs.com/)

**原文标题**: [
      AdonisJS - The batteries-included TypeScript framework
    ](https://adonisjs.com/)

AdonisJS 是一个功能齐全的 TypeScript 框架，集成了身份验证、ORM、验证、邮件、队列、缓存和测试等核心功能，旨在帮助团队快速构建产品，而无需组装多个框架。

- 🚀 **一体化 Node.js 框架**：内置身份验证、ORM、验证、邮件、队列、缓存和测试，所有功能协同工作。
- 📝 **优雅的代码体验**：结合表达性 API、清晰约定和完整的 TypeScript 支持，常见任务保持简单而不失强大。
- 🔧 **强大的开发工具**：提供漂亮的错误页面、CLI、安全原语、Vite 集成和端到端类型安全，工具链无缝高效。
- 📦 **官方包支持**：从缓存到速率限制、健康检查，常见需求都有官方包解决，无需寻找第三方包。
- 🏗️ **灵活的 MVC 架构**：提供完整的 MVC 架构，但视图层灵活，可与 React、Vue、服务器渲染模板或纯 API 搭配使用。
- 🌍 **活跃的社区与支持**：拥有超过十年的稳定发展，活跃的 Discord 社区、全面文档和合作伙伴支持，确保框架持续成长。

---

### [错误](https://javascriptweekly.com/link/181439/web)

**原文标题**: [Error](https://javascriptweekly.com/link/181439/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='lokeshdhakar.com', port=443): Max retries exceeded with url: /projects/color-thief/ (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1000)')))

---

### [GitHub - lokesh/color-thief: 仅用 JavaScript 从图像中提取色彩调色板。支持浏览器和 Node 环境。· GitHub](https://github.com/lokesh/color-thief)

**原文标题**: [GitHub - lokesh/color-thief: Grab the color palette from an image using just Javascript.  Works in the browser and in Node. · GitHub](https://github.com/lokesh/color-thief)

Color Thief 是一个用于从图像中提取主色调和调色板的 JavaScript 库，支持浏览器和 Node.js 环境，提供同步和异步 API，并包含丰富的颜色处理功能。

- 🎨 支持浏览器与 Node.js，提供同步/异步 API，可提取主色、调色板及语义化色板
- 🔄 支持实时提取，可监听视频、画布或图片元素的变化并动态更新调色板
- ⚙️ 提供多种配置选项，如颜色数量、采样质量、色彩空间（RGB/OKLCH）及 Web Worker 支持
- 🧩 颜色对象功能丰富，支持 HEX、RGB、HSL、OKLCH 等多种格式转换及 WCAG 对比度计算
- 📦 安装简便，可通过 npm 或 CDN 直接引入，且无运行时依赖
- 🔧 包含完整的开发工具链，支持构建、测试及发布流程
- 📄 项目采用 MIT 许可证开源，由 Lokesh Dhakar 维护

---

### [Angular 图表演示](https://valor-software.com/ng2-charts)

**原文标题**: [Angular Charts Demo](https://valor-software.com/ng2-charts)

ng2-charts 是一个为 Angular 应用设计的 Chart.js 指令库，用于集成图表功能。

- 📊 提供 Angular 指令，简化 Chart.js 在 Angular 项目中的使用
- 🔧 支持多种图表类型，如折线图、柱状图、饼图等
- ⚙️ 易于配置和自定义，与 Angular 的数据绑定和生命周期无缝集成
- 🚀 帮助开发者快速在 Angular 应用中实现交互式数据可视化

---

### [GitHub - nemanjamalesija/vue-superselect：专为Vue 3 打造的无头、无障碍、TypeScript 优先的选择/组合框组件 · GitHub](https://github.com/nemanjamalesija/vue-superselect)

**原文标题**: [GitHub - nemanjamalesija/vue-superselect: Headless, accessible, TypeScript-first select/combobox for Vue 3 · GitHub](https://github.com/nemanjamalesija/vue-superselect)

这是一个用于 Vue 3 的无样式、可访问、TypeScript 优先的选择/组合框组件库，提供两种 API 模式：复合组件或可组合函数。

- 🎨 **无样式设计**：不提供内置 CSS，完全通过插槽控制渲染样式
- ♿ **完全可访问**：遵循 WAI-ARIA 组合框模式，支持键盘导航和屏幕阅读器
- 📦 **TypeScript 优先**：严格模式，完整的泛型推断，类型化的 Props 和插槽
- 🔧 **双 API 模式**：支持复合组件或 `useSelect()` 可组合函数进行完整 DOM 控制
- ⚡ **功能丰富**：支持单选/多选、内置过滤、智能定位、树摇优化等
- 🎯 **现代浏览器支持**：支持 Chrome、Firefox、Safari、Edge 等现代浏览器
- 📄 **MIT 许可证**：开源项目，包含完整的文档和贡献指南

---

### [React-PDF](https://projects.wojtekmaj.pl/react-pdf/)

**原文标题**: [React-PDF](https://projects.wojtekmaj.pl/react-pdf/)

本文介绍了人工智能在医疗领域的应用现状与前景，重点探讨了其在疾病诊断、治疗方案优化及医疗管理效率提升方面的作用，并简要提及了相关的技术挑战和伦理考量。

- 🏥 AI 辅助诊断系统能通过分析医学影像快速识别病灶，提高早期疾病检出率
- 💊 基于机器学习的个性化治疗方案可结合患者数据优化用药与治疗路径
- 📊 智能医疗管理平台能整合临床数据，减少行政负担并辅助资源配置决策
- ⚙️ 深度学习技术需应对数据质量、算法透明度及跨机构数据共享等挑战
- ⚖️ 人工智能应用需建立伦理规范以确保患者隐私和算法公平性

---

### [发布 v10.4.0 · wojtekmaj/react-pdf · GitHub](https://github.com/wojtekmaj/react-pdf/releases/tag/v10.4.0)

**原文标题**: [Release v10.4.0 · wojtekmaj/react-pdf · GitHub](https://github.com/wojtekmaj/react-pdf/releases/tag/v10.4.0)

react-pdf 库发布了 v10.4.0 版本，新增了 Page 组件的 pageColors 属性，允许自定义 PDF 渲染的背景色和前景色，以提升可访问性。

- 🆕 新增 Page 组件的 pageColors 属性，支持自定义 PDF 渲染颜色
- 🎨 可通过 background 和 foreground 选项覆盖默认颜色设置
- ♿ 该功能有助于实现可访问性增强，例如高对比度主题
- 🔧 示例代码展示如何将背景设为黑色、前景设为红色
- 📦 版本由维护者 wojtekmaj 于 2 月 21 日发布，包含 10 次提交

---

### [发布 2.0.0 版本 · bfirsh/jsnes · GitHub](https://github.com/bfirsh/jsnes/releases/tag/v2.0.0)

**原文标题**: [Release 2.0.0 · bfirsh/jsnes · GitHub](https://github.com/bfirsh/jsnes/releases/tag/v2.0.0)

JSNES 2.0 是一次重大更新，专注于提升硬件模拟精度、易用性和性能，包括新的浏览器嵌入类、游戏兼容性增强、作弊码支持及多项硬件准确性改进。

- 🎮 新增 `jsnes.Browser` 类，简化网页嵌入，自动处理渲染、音频、输入和错误处理
- 🔧 硬件模拟精度大幅提升，通过多项测试套件验证，修复了 NMI 时序、PPU 同步等核心问题
- 🕹️ 支持六款新游戏映射器（Mapper 9、71、79、118、119、240），扩展游戏兼容性
- 🎯 新增 Game Genie 作弊码支持，允许运行时动态添加和移除代码
- ⚡ 性能优化，采用类型化数组和快速内存访问路径，提升运行速度约 24%
- 🔊 使用 AudioWorklet 替代已弃用的 ScriptProcessorNode，改善音频时序和延迟
- 🔄 新增连发按钮支持，模拟 NES Advantage 控制器的自动连发功能
- 🐛 修复多个错误，包括无效操作码导致的无限循环和映射器状态泄漏问题

---

### [JSNES：一款基于 JavaScript 的 NES 模拟器](https://jsnes.org/)

**原文标题**: [JSNES: A JavaScript NES emulator](https://jsnes.org/)

本文介绍了人工智能在医疗领域的应用现状与前景，重点探讨了其在疾病诊断、药物研发和个性化治疗方面的突破性进展，同时提及了相关的伦理挑战和未来发展趋势。

- 🤖 AI 辅助诊断系统能通过分析医学影像显著提升早期疾病检出率
- 💊 机器学习加速新药研发流程，缩短化合物筛选与临床试验周期
- 🧬 基于基因数据的 AI 模型为患者提供定制化治疗方案
- ⚖️ 医疗 AI 面临数据隐私、算法透明性及责任界定等伦理监管问题
- 🌐 跨机构医疗数据共享与边缘计算技术正推动行业协同发展

---

### [GitHub - Milkdown/milkdown: 🍼 插件驱动的所见即所得 Markdown 编辑器框架。· GitHub](https://github.com/Milkdown/milkdown)

**原文标题**: [GitHub - Milkdown/milkdown: 🍼 Plugin driven WYSIWYG  markdown editor framework. · GitHub](https://github.com/Milkdown/milkdown)

Milkdown 是一个插件驱动的所见即所得 Markdown 编辑器框架，基于 ProseMirror 和 Remark 构建，灵感来源于 Typora。

- 🍼 插件驱动的所见即所得 Markdown 编辑器框架，基于 ProseMirror 和 Remark 构建
- 🌐 提供官方文档网站，设计由 Meo 和 Mirone 完成，采用 Theme Nord 和 Material Design 风格
- 📋 项目规划可通过 Milkdown TODO 页面和里程碑追踪
- 👥 拥有 Discord 社区，欢迎贡献者参与，遵循贡献指南
- 💖 接受赞助以支持项目维护，特别感谢设计师 @Meo
- 📄 采用 MIT 许可证，代码仓库包含丰富的开发配置和文档
- ⭐ 在 GitHub 上获得 11.1k 星标，497 个复刻，由 70 多位贡献者共同开发

---

### [GitHub - peggyjs/peggy: Peggy：适用于 JavaScript 的解析器生成器 · GitHub](https://github.com/peggyjs/peggy)

**原文标题**: [GitHub - peggyjs/peggy: Peggy: Parser generator for JavaScript · GitHub](https://github.com/peggyjs/peggy)

Peggy 是一个用于 JavaScript 的解析器生成器，它能够生成具有出色错误报告功能的快速解析器，适用于处理复杂数据或计算机语言，并能轻松构建转换器、解释器、编译器及其他工具。

- 🚀 **简单易用的语法** – 提供简洁而富有表现力的语法规则，便于定义解析逻辑。
- 🔗 **词法与句法分析结合** – 将词法分析和语法分析无缝集成，简化解析流程。
- 🛡️ **优秀的错误报告** – 生成的解析器默认具备详细的错误提示，便于调试。
- 📚 **基于解析表达文法** – 采用 PEG 形式，比传统的 LL(k) 和 LR(k) 解析器更强大灵活。
- 🌐 **多平台使用** – 可在浏览器、命令行或通过 JavaScript API 调用，适应不同开发环境。
- 🗺️ **支持源映射** – 便于在生成的代码中追踪原始语法位置，提升开发体验。
- 📖 **完善的文档** – 提供在线版本和完整文档，方便快速入门和深入使用。
- 🔄 **PEG.js 的继承者** – 作为 PEG.js 的后继项目，保持 API 兼容性，升级迁移简单。
- 👥 **活跃的社区维护** – 由开源社区共同维护，欢迎贡献代码，拥有讨论区和问题跟踪系统。

---

### [npmx - npm 注册表的包浏览器](https://npmx.dev/)

**原文标题**: [npmx - Package Browser for the npm Registry](https://npmx.dev/)

npmx 是一个专为 npm 注册表设计的快速现代浏览器，提供即时搜索功能，支持多种前端框架，并鼓励社区参与贡献。

- 🔍 **即时搜索功能**：用户可开启或关闭快速搜索 npm 包的功能
- ⚙️ **技术支持**：兼容 Nuxt、Vue、React、Svelte 等主流前端框架和工具
- 🛠️ **社区参与**：开源项目，欢迎通过 GitHub 贡献代码以改进 npm 体验
- 💬 **交流平台**：提供 Discord 社区供用户聊天、提问和分享想法
- 📢 **信息更新**：可通过 Bluesky 关注项目最新动态和版本发布

---

### [发布 npmx：一款快速、现代的 npm 注册表浏览器](https://npmx.dev/blog/alpha-release)

**原文标题**: [Announcing npmx: a fast, modern browser for the npm registry](https://npmx.dev/blog/alpha-release)

npmx 是一个为 npm 注册表设计的快速、现代浏览器，旨在通过提供详尽的包信息（如下载量、依赖状态和安装大小）和社交功能，提升开发者查找、评估和管理 npm 包的效率与体验。该项目自构想之初便依托社区力量快速发展，现已在 alpha 阶段提供多语言支持、深色模式及一键演示环境等丰富功能，并邀请更多用户参与测试与贡献。

- 🚀 **快速启动**：npmx 致力于提升 npm 包浏览与管理的速度与便捷性，提供安装大小、模块格式等关键数据，帮助开发者高效决策。
- 🌍 **社区驱动**：项目自 Daniel Roe 发起后迅速获得全球开发者响应，两周内收获超 1000 个议题与 PR，形成活跃且多元的协作社区。
- 🔍 **功能丰富**：支持包搜索、代码查看、下载统计、过时依赖警告、JSR 交叉引用等，并集成 StackBlitz 等演示环境，覆盖 19 种语言。
- 🤝 **开放共建**：强调无障碍性、国际化与公开协作，鼓励包括新手在内的所有开发者参与，提供详细的贡献指南以降低参与门槛。
- 📢 **持续进化**：目前处于 alpha 阶段，积极寻求用户反馈以迭代产品，未来计划基于社区输入推进至 beta 版本，优化 JavaScript 生态工具体验。

---

### [在 npmx 中寻找无障碍优先文化 - Piccalilli](https://piccalil.li/blog/finding-an-accessibility-first-culture-in-npmx/)

**原文标题**: [
  Finding an accessibility-first culture in npmx - Piccalilli
](https://piccalil.li/blog/finding-an-accessibility-first-culture-in-npmx/)

作者在寻找重视无障碍设计的文化环境时，意外在 npmx 社区中发现了这种氛围，并分享了其体验与建议。

- 🏠 作者曾感到孤独，作为团队中唯一关注无障碍设计的人，经常需要反复解释基础问题，渴望一个无障碍优先的社区环境。
- 🤝 在 npmx 社区中，作者惊喜地发现了专门的无障碍频道、自动化测试，以及一群积极避免常见错误的开发者，重新激发了学习热情。
- 📚 社区重视无障碍讨论，专家会被邀请参与相关问题的评审，使作者重新感受到专业环境中的支持与重视。
- 🛠️ 文章建议通过编写文档、使用检查工具、将无障碍纳入设计与测试阶段，以及认真对待专家意见来构建无障碍优先的文化。
- 💡 强调保持谦逊，从错误中学习，并以包容为最终目标，真正倾听被排除在外的用户的声音。

---

### [npmx.dev：在朋友们的帮助下 | johnnyreilly](https://johnnyreilly.com/npmx-with-a-little-help-from-my-friends)

**原文标题**: [npmx.dev: with a little help from my friends | johnnyreilly](https://johnnyreilly.com/npmx-with-a-little-help-from-my-friends)

npmx.dev 是一个由社区驱动、重新设计的 npm 网站，旨在改善用户体验并积极开发新功能。作者 John Reilly 分享了他作为贡献者的经历，强调该项目的开放性和友好社区氛围。

- 🚀 npmx.dev 是 npmjs.com 的重新设计版本，由社区积极开发，旨在提供更好的用户体验
- 🤝 项目社区非常欢迎贡献，无论贡献大小，都鼓励参与
- 🔍 作者通过发现并修复 npm API 速率限制导致的显示问题，成功提交了第一个 PR
- 🤖 项目允许使用 AI 工具辅助贡献，但强调贡献者需理解代码并用自己语言沟通
- 💻 即使不熟悉 Vue/Nuxt 框架，作者也能通过学习和尝试成功参与开发
- 🌟 npmx.dev 采用更高效的数据查询方式，减少了依赖 npm 官方 API 的限制

---

### [VoidZero 与 npmx：携手共建更优工具 | VoidZero](https://voidzero.dev/posts/npmx-alpha)

**原文标题**: [VoidZero and npmx: Building Better Tools Together | VoidZero](https://voidzero.dev/posts/npmx-alpha)

VoidZero 与 npmx 项目通过共享使命和工具链合作，共同提升 JavaScript 开发效率，npmx 作为 npm 注册表的现代浏览器，利用 VoidZero 工具实现快速开发，并通过真实反馈优化工具性能，体现了开源生态的良性互动。

- 🚀 npmx.dev 进入 alpha 阶段：作为 npm 注册表的快速现代浏览器，专注于帮助开发者更高效地选择和评估包
- 🎯 共享使命：VoidZero 旨在提升 JavaScript 开发效率，npmx 通过展示包大小、性能建议等细节支持这一目标
- 🔧 工具链集成：npmx 使用 VoidZero 全套工具，包括 Vite、Vitest、Rolldown、oxlint 和 oxfmt，并预览 Vite+ 统一工具链
- 🔄 反馈循环：npmx 团队在实际使用中发现问题并提供基准测试，帮助 VoidZero 优化工具性能，例如将 Vite+ 命令开销降低近三倍
- 🤝 开源合作：VoidZero 赞助 npmx 项目，双方通过真实场景推动工具进步，共同促进 JavaScript 生态系统健康发展

---

### [良性循环 - 丹尼尔·罗](https://roe.dev/blog/virtuous-circle)

**原文标题**: [The virtuous circle - Daniel Roe](https://roe.dev/blog/virtuous-circle)

良性循环是开发者工具中最强大的模式，而“10 倍效率开发者”的神话使其难以被察觉。

- 🧠 “10 倍效率开发者”的概念源于 1968 年的一项研究，但过度关注个人能力可能误导团队协作的真正价值。
- 🤝 研究表明，在复杂任务中团队表现优于个人，迭代和并行协作往往比一次性设计产生更好结果。
- 🔄 npmx 项目的启动展示了良性循环的力量：使用者即贡献者，改善工具体验的同时吸引更多共建者。
- 🌱 项目由社区驱动，不受企业议程或资金限制，通过集体迭代持续优化 npm 注册表的使用体验。
- 🚀 成功的关键在于构建“10 倍效率团队”，而非依赖个别开发者，欢迎所有感受到 npm 使用痛点的贡献者参与。

---

### [npmx，汇聚社区的力量 | patak](https://patak.cat/npmx/converging-communities.html)

**原文标题**: [npmx, converging communities | patak](https://patak.cat/npmx/converging-communities.html)

npmx 项目在过去一个月中从一个想法发展为功能完整的 npm 注册表现代浏览器，凝聚了来自 Vite、Vitest 等开源社区的开发者。社区在合作中重燃希望，共同应对开源可持续性挑战，并计划通过资金筹集、跨社区协作和线下活动构建长期可持续的开源生态。

- 🚀 npmx 在一个月内从概念发展为成熟的 npm 注册表浏览器，汇聚了 Vite、Vitest 等社区的力量
- 🌱 开源社区在合作中重燃希望，但面临可持续性和开发者倦怠的挑战
- 🤝 通过 Mastodon、Bluesky 等开放网络工具，社区不断扩展跨领域协作
- 💡 项目启动时已有 200 多名贡献者，并围绕 alpha 版本发布了 20 篇互联博客文章
- 🌍 社区计划推动开源可持续性，包括资金筹集、核心团队全职化及跨项目协作
- ❤️ 作者从抑郁中恢复，强调社区支持的重要性，并宣布将全职投入 npmx 及开源事业
- 📢 邀请更多人通过 build.npmx.dev 加入，共同构建长期可持续的开源未来

---

### [我们是洛库图斯 | 洛库图斯](https://locutus.io/)

**原文标题**: [We are Locutus | Locutus](https://locutus.io/)

Locutus 是一个自 2008 年运行的开源项目，提供了 565 个 TypeScript 实现的标准库函数，这些函数源自 15 种编程语言。它允许开发者通过 npm 单独安装并使用这些函数，同时通过 tree-shake 移除未使用的代码。项目强调函数行为的移植，而非语言特定的结构或数据，适合学习和特定功能复用，但不作为 TypeScript 的完整标准库替代。社区驱动，采用 MIT 许可证，鼓励贡献与改进。

- 🧩 项目包含 565 个 TypeScript 实现的标准库函数，覆盖 15 种编程语言如 C、Python、Rust 等
- 📦 支持通过 npm 单独安装函数，并利用 tree-shake 优化代码体积
- ⚙️ 移植重点为函数语义，使用 JavaScript 原生值，避免语言特定结构或扩展内置对象
- 🌱 社区驱动项目，遵循“麦当劳理论”，鼓励迭代改进和贡献
- 📄 采用 MIT 许可证，允许自由使用于商业或个人项目

---

### [React Native 2025 现状](https://results.stateofreactnative.com/en-US/)

**原文标题**: [State of React Native 2025](https://results.stateofreactnative.com/en-US/)

2025 年 React Native 社区调查结果显示，新架构采用率已达 80%，生态系统持续成熟，显著改善了调试等常见痛点，调查不仅为开发者提供前沿资源，还通过追踪采用情况和社区反馈引导生态发展方向。

- 📊 新架构采用率达 80%，为众多库开启新可能
- 🛠️ 生态系统持续成熟，显著改善调试等痛点
- 📈 调查成为社区重要资源，帮助开发者掌握最新工具与最佳实践
- 🧭 通过追踪采用情况和社区反馈，引导生态系统未来发展方向
- 📧 鼓励订阅以获取未来调查结果，保持信息同步

---

### [TypeScript 5.x 至 6.0 迁移指南 · GitHub](https://gist.github.com/privatenumber/3d2e80da28f84ee30b77d53e1693378f)

**原文标题**: [TypeScript 5.x to 6.0 Migration Guide · GitHub](https://gist.github.com/privatenumber/3d2e80da28f84ee30b77d53e1693378f)

TypeScript 6.0 是一个过渡版本，为即将到来的 TypeScript 7.0（基于 Go 的重写版本）做准备。它引入了新的默认配置、多项废弃选项以及一些新功能，旨在与现代生态系统对齐并提升性能。大多数项目需要更新 `tsconfig.json` 以适配新的默认值，并移除已废弃的选项。

- 📄 **默认配置变更**：`strict` 现在默认为 `true`，`target` 默认为 `es2025`，`types` 默认为空数组（不再自动包含 `@types`），`rootDir` 默认为 `tsconfig.json` 所在目录。
- 🗑️ **废弃选项**：包括 `target: es3/es5`、`downlevelIteration`、`baseUrl`、`moduleResolution: node10/classic`、`module: amd/umd/system/none`、`outFile` 等，这些将在 TypeScript 7.0 中被移除。
- 🛠️ **迁移工具**：可使用 `ts5to6` 工具自动处理 `baseUrl` 移除和 `rootDir` 推断等破坏性变更。
- 🚨 **临时解决方案**：可通过设置 `"ignoreDeprecations": "6.0"` 暂时屏蔽废弃警告，但此选项在 TypeScript 7.0 中无效。
- ✨ **新功能**：包括对 `#/` 子路径导入的支持、`es2025` 目标库、Temporal API 类型、`Map.getOrInsert` 方法以及 `RegExp.escape` 等。
- ⚠️ **行为变更**：`esModuleInterop` 和 `allowSyntheticDefaultImports` 现在始终为 `true`，非 ESM 输出文件会无条件添加 `"use strict"`，且模块解析默认值已更改。
- 📅 **发布时间线**：TypeScript 6.0 最终版计划于 2026 年 3 月 17 日发布，之后将很快推出 TypeScript 7.0。

---

### [p5.js 网页编辑器](https://editor.p5js.org/isohedral/full/vJa5RiZWs)

**原文标题**: [p5.js Web Editor](https://editor.p5js.org/isohedral/full/vJa5RiZWs)

本文介绍了人工智能在医疗领域的应用现状与前景，重点探讨了其在疾病诊断、药物研发和个性化治疗方面的突破性进展，同时简要提及了相关的伦理挑战。

- 🤖 AI 辅助诊断系统能通过分析医学影像快速识别病灶，提升早期癌症等疾病的检出率
- 🔬 机器学习加速新药研发流程，大幅缩短化合物筛选与临床试验周期
- 🧬 基于患者基因组数据的 AI 模型可为个体提供定制化治疗方案
- ⚖️ 医疗 AI 面临数据隐私、算法透明度及责任认定等伦理监管问题

---

### [xkcd：依赖关系](https://xkcd.com/2347/)

**原文标题**: [xkcd: Dependency](https://xkcd.com/2347/)

XKCD 是一个每周一、三、五更新的网络漫画，内容涵盖浪漫、讽刺、数学和语言，提供多种订阅方式并推荐了其他漫画作品，同时以幽默方式列出了浏览要求。

- 🌐 网站提供漫画存档、订阅功能（RSS/Atom/邮件）和社交媒体链接
- 📅 漫画每周更新三次，主题多元且充满幽默与知识性
- 🔗 页面包含永久链接、图片直连和详细版权说明（CC 协议）
- 📚 作者推荐了十余部同类网络漫画作品清单
- ⚙️ 以戏谑口吻列出“最佳浏览要求”（如 Netscape 浏览器、船用模式等）

---

### [p5.js](https://p5js.org/)

**原文标题**: [p5.js](https://p5js.org/)

p5.js 是一个创意编程库，提供丰富的学习资源、社区作品展示和支持途径。

- 📚 提供 p5.js 库参考文档和示例学习资源
- 🎨 展示社区创作作品，如地理数据编织、生成植物等视觉艺术
- 👥 设有活跃的社区平台供用户交流与分享
- 💝 接受捐赠以支持项目发展
- 📥 提供库文件下载服务

---

### [Drizzle ORM - 下一代 TypeScript ORM。](https://orm.drizzle.team/)

**原文标题**: [Drizzle ORM - next gen TypeScript ORM.](https://orm.drizzle.team/)

Drizzle ORM 是一款轻量、高性能的 TypeScript/JavaScript ORM，专注于开发者体验与类型安全，支持多种数据库和运行时，并提供丰富的工具链和持续迭代的更新。

- 🚀 **高性能与轻量**：强调不拖慢开发速度，提供接近原生 SQL 的性能，并在多种数据库和服务器环境中表现优异。
- 🔌 **多数据库支持**：兼容 PostgreSQL、MySQL、SQLite、MSSQL、CockroachDB 等主流数据库，并针对云平台（如 Vercel、Supabase、Neon）提供专门驱动。
- 🛠️ **完整工具链**：包含 Drizzle Kit（迁移管理）、Drizzle Studio（数据库可视化操作）、Drizzle Seed（数据填充）等工具，支持从开发到部署的全流程。
- 📦 **持续迭代与更新**：定期发布新版本，增加功能（如行级安全、缓存层、新方言支持）并修复大量错误，保持项目活跃度。
- 🌐 **社区驱动与赞助**：拥有活跃的开发者社区和赞助体系，提供免费开源版本，并通过云合作伙伴和赞助支持项目发展。
- 🎯 **开发者友好**：提供类型安全的查询构建器、简洁的 API 设计、丰富的教程和文档，并支持现代前端与全栈框架集成。

---

### [Drizzle 加入 PlanetScale —— PlanetScale](https://planetscale.com/blog/drizzle-joins-planetscale)

**原文标题**: [Drizzle joins PlanetScale â PlanetScale](https://planetscale.com/blog/drizzle-joins-planetscale)

PlanetScale 宣布 Drizzle 团队加入，共同致力于提升 JavaScript 和 TypeScript 的数据库工具性能与开发者体验，同时保持 Drizzle 作为独立开源项目的地位。

- 🚀 Drizzle 团队加入 PlanetScale，专注于优化 JavaScript 和 TypeScript 的数据库工具性能与开发者体验
- 🔧 Drizzle ORM 因卓越性能和开发者体验成为默认选择，与 PlanetScale 理念高度契合
- 🌍 Drizzle 将继续作为独立开源项目运营，保持自身路线图和目标不变
- 💪 PlanetScale 将支持 Drizzle 团队专注于核心工作，推动项目持续发展
- 👏 PlanetScale 团队感谢 Drizzle 对社区的贡献，欢迎成为同事

---

### [小趣语言](https://taylor.town/scrapscript-000)

**原文标题**: [Lil' Fun Langs](https://taylor.town/scrapscript-000)

本文介绍了一系列小型编程语言实现，涵盖从极简的 Lambda 演算解释器到功能相对完整的编译器，重点关注 ML 风格（函数式、静态类型）语言。这些项目以代码简洁、教育性强或概念创新为特点，展示了类型系统、编译技术及语言设计的核心思想。

- 🤖 **Hirrolot's CoC**：约 70 行 OCaml 代码实现完整的构造演算，支持依赖类型和双向类型检查，展示了依赖类型系统的极简实现。
- 🤖 **Harrop MiniML**：约 100 行 OCaml 代码，利用 LLVM 生成原生代码，支持整数运算和递归函数，但缺乏高阶函数和闭包。
- 🤖 **Algorithm W**：约 300 行 Haskell 代码，是 Hindley-Milner 类型推断算法的经典教学实现。
- 🤖 **tomprimozic/type-systems**：多个 OCaml 实现（约 300-600 行），涵盖算法 W、行多态和 HMF 等类型系统变体。
- 🤖 **lambda-calculus-hs**：一系列 Haskell 单文件实现（200-900 行），从简单类型演算逐步扩展到双向类型检查、系统 T 等。
- 🤖 **THIH**：429 行 Haskell 代码，完整实现了 Haskell 98 的类型系统规范，包括类型类和模式匹配类型。
- 🤖 **Simple-sub**：约 500 行 Scala 代码，实现了 MLsub 的代数子类型系统，支持并集和交集类型。
- 🤖 **PLZoo poly**：约 400-600 行 OCaml 代码，实现惰性函数式语言，支持参数多态和 HM 类型推断。
- 🤖 **EYG**：约 500 行 Gleam 代码，使用行类型推断和代数效应，支持 JSON AST 存储和无语法错误的结构化编辑。
- 🤖 **Pico-ml**：TypeScript 实现的 OCaml 子集，编译到 WebAssembly，适合浏览器端 ML 编译学习。
- 🤖 **TinyML**：不到 700 行 Standard ML 代码，包含完整的词法分析、解析、解释器和 HM 类型推断。
- 🤖 **Eff**：约 1-2 千行 OCaml 代码，是代数效应处理器的原始实现，影响了后续众多效应系统。
- 🤖 **Frank**：约 1-2 千行 Haskell 代码，提出“函数即效应处理器”概念，支持多处理器抽象。
- 🤖 **Grace**：约 1-3 千行 Haskell 代码，作为“可复刻”的 DSL 骨架，支持双向类型检查和行多态。
- 🤖 **Hackett**：约 1-3 千行 Racket 代码，通过“类型系统即宏”技术实现 Haskell 风格语言。
- 🤖 **Scrapscript**：约 1-3 千行 Python 代码，实现基于内容寻址的纯函数语言，可编译为 C/WASM/Cosmo。
- 🤖 **MinCaml**：约 2000 行 OCaml 代码，生成 x86/SPARC/PPC 原生代码，支持闭包、尾调用优化和寄存器分配。
- 🤖 **Ben Lynn**：约 2000 行 Haskell+C 代码，通过组合子逻辑自举实现接近 Haskell 98 的编译器。
- 🤖 **1ML**：约 3-5 千行 OCaml 代码，统一 ML 的核心与模块层，模块为一等公民。
- 🤖 **mlml**：约 3-5 千行 OCaml 代码，自托管编译到 x86-64 原生代码，支持模式匹配和代数数据类型。
- 🤖 **Dhall**：约 4 千行 Haskell 代码，基于构造演算的完全配置语言，保证归约终止。
- 🤖 **Ante**：约 5-10 千行 Rust 代码，结合 HM 类型推断、代数效应和所有权系统，使用 Cranelift 生成代码。
- 🤖 **Tao**：约 5-10 千行 Rust 代码，支持泛型、类型类、代数效应和完全性检查，编译到字节码。
- 🤖 **Austral**：约 5-10 千行 OCaml 代码，系统语言，强调线性类型和能力安全，编译到 C。
- 🤖 **AQaml**：约 5-8 千行 OCaml 代码，自托管编译到 x86-64，支持记录、变体和垃圾回收。
- 🤖 **Borgo**：约 5-10 千行 Rust 代码，为 Go 生态添加 ML 特性，编译到 Go 源代码。
- 🤖 **polytt**：约 5-10 千行 OCaml 代码，实验性多项式函子类型理论实现，支持依赖类型。
- 🤖 **Newt**：约 7 千行自托管代码，依赖类型语言，编译到 JavaScript，支持类型类和擦除。
- 🤖 **HaMLet**：约 1-1.5 万行 SML 代码，完整实现 Standard ML 97，包括模块系统。
- 🤖 **SOSML**：约 1-1.5 万行 TypeScript 代码，浏览器端 SML 实现，支持 HM 类型推断和异常。
- 🤖 **MicroHs**：约 1.5-3 万行 Haskell/C 代码，近乎完整的 Haskell 2010 编译器，可从 C 自举。

---

