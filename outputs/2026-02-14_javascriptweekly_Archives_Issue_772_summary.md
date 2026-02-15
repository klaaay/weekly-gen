### [JavaScript 周刊第 772 期：2026 年 2 月 10 日](https://javascriptweekly.com/issues/772)

**原文标题**: [JavaScript Weekly Issue 772: February 10, 2026](https://javascriptweekly.com/issues/772)

本期 JavaScript 周刊主要介绍了 npmx 新包浏览器、State of JS 2025 调查结果、ESLint v10.0.0 发布等工具更新，以及关于 JavaScript 资源清理新特性、Vite 创始人访谈等技术内容，同时涵盖多个框架和库的最新发布与实用工具推荐。

- 📦 **npmx 新包浏览器**：提供流畅快速的 npm 包浏览体验，支持包比较功能。
- 📊 **State of JS 2025 调查结果**：汇总超过 1.2 万名开发者意见，涵盖框架选择、构建工具使用等主题。
- 🛠️ **ESLint v10.0.0 发布**：移除旧配置系统，改进配置查找算法，增强 JSX 范围分析。
- 🔄 **JavaScript 资源清理新特性**：介绍 Symbol.dispose 和 using 语法，简化资源管理。
- 🎙️ **Vite 创始人访谈**：Evan You 讨论 Vite 发展历程及 Rust 工具链的未来。
- 🤖 **AI 调试 React 的局限性**：实验显示 AI 在复杂调试场景中仍难以替代经验丰富的开发者。
- ⚡ **Bun v1.3.9 更新**：支持并行运行脚本、优化 Markdown 渲染和正则表达式性能。
- 📄 **技术文章精选**：涵盖 Next.js 调试、Angular 22 预期特性、Solid.js 最佳实践等内容。
- 🛠️ **开发工具推荐**：包括 Shovel.js 全栈框架、VerifyFetch 增强下载库、OTPAuth 双因素认证工具等。
- 📰 **行业动态**：Notion 等公司采用 Meticulous 进行前端测试，Heroku 进入维护模式引发迁移讨论。

---

### [npmx - npm 注册表的包浏览器](https://npmx.dev/)

**原文标题**: [npmx - Package Browser for the npm Registry](https://npmx.dev/)

npmx 是一个专为 npm 注册表设计的快速现代浏览器，旨在提升包管理和搜索体验。

- 🔍 **快速搜索 npm 包** – 提供高效的包搜索功能，支持多种前端框架和技术栈。
- 🛠️ **持续开发与贡献** – 项目处于 Canary 版本阶段，鼓励开发者参与贡献，共同改进 npm 使用体验。
- 🌐 **活跃社区互动** – 通过 Discord 社区进行交流、提问和分享想法，保持用户间的紧密联系。
- 📢 **及时获取更新** – 关注 Bluesky 等平台，获取项目最新动态和版本发布信息。

---

### [获取失败](https://javascriptweekly.com/link/180448/web)

**原文标题**: [Failed to retrieve](https://javascriptweekly.com/link/180448/web)

无法总结：获取内容失败，状态码 403。

---

### [axios - npmx](https://npmx.dev/package/axios)

**原文标题**: [axios - npmx](https://npmx.dev/package/axios)

Axios 是一个基于 Promise 的 HTTP 客户端，适用于浏览器和 Node.js 环境，提供简洁的 API 进行网络请求。

- 🌐 **跨平台支持**：可在浏览器和 Node.js 中发起 HTTP 请求。
- ⚡ **Promise 基础**：完全支持 Promise API，便于异步操作。
- 🔧 **拦截器功能**：允许在请求和响应前后添加自定义逻辑。
- 📦 **自动数据转换**：自动序列化 JSON 数据，支持 FormData 和 URL 编码格式。
- 🛡️ **请求取消**：内置机制支持取消请求，避免不必要的网络流量。
- 📄 **丰富配置**：提供灵活的请求配置选项，如超时、头部、代理等。
- 🔄 **实例创建**：可创建自定义实例，设置默认配置以适应不同场景。
- 🚀 **高级特性**：支持 HTTP/2、进度捕获、速率限制和 Fetch 适配器等现代功能。

---

### [比较 nitro 与 h3 - npmx](https://npmx.dev/compare?packages=nitro,h3)

**原文标题**: [Compare nitro vs h3 - npmx](https://npmx.dev/compare?packages=nitro,h3)

该工具用于并排比较 npm 软件包，帮助开发者根据性能、包大小、健康状况、兼容性及安全合规性等关键维度选择合适依赖。

- 📊 **性能与包大小** – 支持评估性能指标、安装大小、直接与总依赖数量
- 📈 **健康状况分析** – 提供每周下载量、点赞数、发布时间及是否弃用状态
- 🔧 **兼容性检查** – 涵盖引擎支持、TypeScript 类型和模块格式适配性
- 🛡️ **安全合规** – 检测许可证类型与已知漏洞，确保代码合规安全
- 🔍 **智能筛选** – 可通过多维度筛选器（如 Facets）快速缩小包选择范围

---

### [闭包、异步与面向对象：JavaScript 的难点解析 | 前端大师](https://frontendmasters.com/courses/javascript-hard-parts-v3/?utm_source=email&utm_medium=javascriptweekly&utm_content=jshardpartsv3)

**原文标题**: [Closure, Async, and OOP: The Hard Parts of JavaScript | Frontend Masters](https://frontendmasters.com/courses/javascript-hard-parts-v3/?utm_source=email&utm_medium=javascriptweekly&utm_content=jshardpartsv3)

本课程深入讲解 JavaScript 中的高阶函数、闭包、异步编程、面向对象编程和元编程等核心难点，帮助开发者建立扎实的思维模型，提升代码复用和复杂问题解决能力，适合希望深化 JavaScript 理解的中高级开发者。

- 🧠 掌握高阶函数与闭包，编写可复用函数，避免重复逻辑
- ⏳ 深入异步代码机制，理解 Promise、调用栈和事件循环
- 🏗️ 学习面向对象编程，掌握类、静态属性等现代 JavaScript 特性
- 🔧 探索类型强制转换与元编程，使用 Symbol 自定义类型行为
- 📚 包含 54 节课程、9.7 小时内容，提供结业证书
- 🧑🏫 由 Codesmith 创始人 Will Sentance 授课，融合十年教育经验
- 🎯 通过逐行代码跟踪、比喻教学和练习强化理解
- 📝 支持笔记、测验和闪卡功能，助力学习巩固
- 🌟 受到 50 万 + 开发者好评，被誉为重塑 JavaScript 思维的高质量课程

---

### [JavaScript 2025 现状](https://2025.stateofjs.com/en-US/)

**原文标题**: [State of JavaScript 2025](https://2025.stateofjs.com/en-US/)

2025 年 JavaScript 生态持续快速演进，为开发者带来新工具与挑战，反映了技术社区的活跃与创新。

- 🎮 类比游戏行业，强调 JavaScript 生态变化迅速，与八年未换代的游戏平台形成鲜明对比
- 📊 介绍 2025 年 State of JS 调查结果，总结年度技术趋势与创新
- 📧 提供订阅渠道，邀请读者参与未来调查
- 🤝 列出合作伙伴，包括 Google Chrome 团队及多家技术服务平台
- 🌍 展示多语言翻译贡献者，体现社区国际化协作
- 🔗 包含就业推荐、技能提升课程及开发工具等资源链接

---

### [JavaScript 2025 状态：特性](https://2025.stateofjs.com/en-US/features/#language_pain_points)

**原文标题**: [State of JavaScript 2025: Features](https://2025.stateofjs.com/en-US/features/#language_pain_points)

这份 JavaScript 社区调查报告揭示了开发者对语言特性、浏览器 API、痛点及未来提案的看法，同时反映了学习趋势和热门工具。

- 📊 **语法特性使用率**：空值合并运算符（Nullish Coalescing）以 10,717 票成为最常用语法特性，动态导入（Dynamic Import）和私有字段（Private Fields）紧随其后。
- 🔤 **字符串与数组特性**：`string.replaceAll()`和`array.toSorted()`分别是字符串和数组中最受欢迎的新方法。
- 🧩 **集合与对象特性**：多数开发者未使用新的 Set 方法（如`set.union()`），而`Object.groupBy()`是对象特性中使用最广泛的。
- ⚡ **异步与浏览器 API**：`Promise.allSettled()`和 WebSocket API 在各自类别中领先，显示异步处理和实时通信的重要性。
- 😫 **主要痛点**：缺乏静态类型（1,102 票）是 JavaScript 语言的最大痛点，浏览器兼容性（725 票）则是浏览器 API 的主要问题。
- 🚀 **期待的新提案**：Temporal（5,614 票）和装饰器（Decorators，3,672 票）是开发者最期待的 JavaScript 新特性。
- ❓ **缺失功能需求**：静态类型（6,177 票）和标准库（5,441 票）被广泛认为是 JavaScript 当前最需要补充的功能。
- 📈 **类型实现偏好**：多数开发者希望通过类型注解（5,380 票）在 JavaScript 中实现原生类型支持。
- 📚 **学习进度**：平均分 2.5（满分 5）表明大多数开发者难以跟上所有新特性，仅部分学习并尝试。
- 📖 **热门学习资源**：Svelte、Solid 和 Astro 是阅读列表中最受关注的工具，反映现代前端框架的学习趋势。

---

### [JavaScript 2025 现状：前端框架](https://2025.stateofjs.com/en-US/libraries/front-end-frameworks/)

**原文标题**: [State of JavaScript 2025: Front-end Frameworks](https://2025.stateofjs.com/en-US/libraries/front-end-frameworks/)

尽管 Solid 框架的使用率仅为 10%，但已连续五年获得最高满意度，其创建者 Ryan Carniato 推动了 signals 等概念的普及，并擅长解析前端框架的复杂原理。

- 🏆 **Solid 框架满意度领先**：尽管用户基数较小，但连续五年在满意度调查中名列前茅
- 🧠 **创新概念推动者**：创始人 Ryan Carniato 积极推广 signals 等前沿技术理念
- 📊 **开发者使用习惯稳定**：调查显示平均每位开发者仅使用 2.6 个框架，颠覆了频繁切换技术的刻板印象
- 😊 **整体满意度中等偏上**：前端框架满意度平均得分 3.7（满分 5），92% 受访者参与评价
- ⚡ **主要痛点集中**：React 相关问题、过度复杂性、性能优化成为开发者最常遇到的挑战
- 🌟 **年度技术推荐**：社区成员推荐 RSC Explorer 工具，帮助理解 React Server Components 的序列化机制
- 📈 **生态多样性丰富**：Astro、Ember、TanStack Start 等框架在特定场景中受到关注

---

### [JavaScript 2025 现状：构建工具](https://2025.stateofjs.com/en-US/libraries/build-tools/)

**原文标题**: [State of JavaScript 2025: Build Tools](https://2025.stateofjs.com/en-US/libraries/build-tools/)

Vite 团队开发的 Rust 打包工具 Rolldown 正成为构建工具生态的核心，社区调查显示开发者对构建工具的多样性和满意度存在不同看法，同时配置复杂性和性能是主要痛点。

- 🚀 Vite 团队开发的 Rolldown 是基于 Rust 的快速打包工具，已被 Vite 采用
- 📊 社区调查显示开发者平均使用 4.1 种构建工具，Vite 可能改变这一现状
- 😊 构建工具满意度平均为 3.6 分（满分 5 分），82% 受访者参与评价
- ⚠️ 主要痛点包括配置复杂（289 人提及）、性能问题（147 人提及）和文档缺乏
- 🎯 推荐资源包括 Vite 学习指南和 Web 性能优化课程

---

### [JavaScript 2025 使用现状](https://2025.stateofjs.com/en-US/usage/#ai_generated_code_balance)

**原文标题**: [State of JavaScript 2025: Usage](https://2025.stateofjs.com/en-US/usage/#ai_generated_code_balance)

这份调查报告揭示了 JavaScript 社区在 2025 年的使用趋势和开发者态度，涵盖了编程语言偏好、工具链、AI 辅助编程及行业应用等多个维度。

- 📈 使用 TypeScript 的开发者比例持续上升，平均 77% 的代码为 TypeScript，完全使用 TypeScript 的开发者可能很快成为多数
- 🔧 86% 的浏览器端 JavaScript 代码会经过构建步骤，主要优势包括静态类型支持、更好的开发体验和代码优化
- 🤖 AI 生成代码的比例从 20% 增至 29%，但完全依赖 AI 的开发者仍占极少数
- 🌐 前端开发仍是 JavaScript 最主要的应用场景，其次是后端开发和移动应用
- 🏢 开发者主要集中在编程与技术工具、咨询服务和电子商务零售等行业
- 🏗️ 单页面应用（SPA）是最流行的架构模式，服务器端渲染（SSR）和静态站点生成（SSG）也广泛使用
- 🧩 开发者面临的主要挑战包括代码架构、状态管理和依赖管理
- 😊 对 Web 技术和 JavaScript 的整体满意度平均为 3.8 分（满分 5 分），保持稳定

---

### [JavaScript 2025 现状：其他工具](https://2025.stateofjs.com/en-US/other-tools/#non_js_languages)

**原文标题**: [State of JavaScript 2025: Other Tools](https://2025.stateofjs.com/en-US/other-tools/#non_js_languages)

这份内容总结了 JavaScript 社区对各类工具、库和技术的使用情况调查结果，涵盖了多个类别中最受欢迎和增长最快的选项。

- 📈 **库类**：Zod 增长显著，日期管理库如 date-fns、Day.js 等广泛使用，而 Moment 虽仍有人用但呈下降趋势。
- 📊 **图形与动画**：Chart.js 今年跃居第一，Three.js 和 D3 紧随其后，Motion（原 Framer Motion）和 GSAP 也较受欢迎。
- 🛠️ **工具类**：ESLint 和 Prettier 几乎成为开发者标配，nvm、Babel 和新兴的 Biome 使用率也较高。
- 🖥️ **JavaScript 运行时**：Node.js 和浏览器环境占据主导，Bun 表现突出升至第三，Cloudflare Workers 增长明显。
- ☁️ **托管服务**：AWS 和 Vercel 是最常用的托管平台，GitHub Pages、Netlify 和 Cloudflare 也广泛使用。
- ⚡ **边缘/无服务器运行时**：AWS Lambda 和 Cloudflare Workers 领先，但“无使用”选项占比最高，反映该领域仍在普及中。
- ✏️ **文本编辑器**：VS Code 保持绝对优势，Cursor 凭借 AI 功能快速崛起，WebStorm 和 Vim 稳定在第二梯队。
- 🤖 **AI 工具**：ChatGPT 和 GitHub Copilot 最受欢迎，Claude 和 Google Gemini 紧随其后，Cursor 也进入前五。
- 📱 **移动与桌面框架**：React Native 领先，Electron 和 Expo 次之，Tauri 作为新兴框架值得关注。
- 📦 **Monorepo 工具**：pnpm 明显领先，Turborepo 和 Nx 竞争激烈，npm Workspaces 仍有不少用户。
- 🐍 **非 JavaScript 语言**：Python 和 PHP 最常用，Bash、Java 和 Go 也较受欢迎，Rust 和 Lua 呈现增长趋势。
- 💡 **期望功能**：开发者最希望 JavaScript/TypeScript 加入模式匹配、静态类型和管道操作符等功能。

---

### [ESLint v10.0.0 发布 - ESLint - 可插拔的 JavaScript 代码检查工具](https://eslint.org/blog/2026/02/eslint-v10.0.0-released/)

**原文标题**: [ESLint v10.0.0 released - ESLint - Pluggable JavaScript Linter](https://eslint.org/blog/2026/02/eslint-v10.0.0-released/)

ESLint v10.0.0 是一个主要版本发布，引入了新功能、修复了错误，并包含多项重大变更。用户需手动安装此版本，并注意 Node.js 支持版本已更新。配置系统已完全转向扁平配置，移除了对 eslintrc 的支持。此外，该版本改进了 JSX 引用追踪、RuleTester 的测试断言，并更新了推荐规则配置。

- 🚀 **重大版本发布**：ESLint v10.0.0 为主要版本，包含新功能、错误修复和重大变更，需手动安装并参考迁移指南。
- 🔧 **配置系统变更**：完全移除 eslintrc 配置系统，默认使用新的扁平配置查找算法，支持从被检测文件目录查找配置。
- ⚠️ **Node.js 支持更新**：不再支持 Node.js v20.19.0 以下版本、v21.x 和 v23.x，仅支持 v20.19.0、v22.13.0 及以上版本。
- 🛠️ **JSX 引用追踪**：现在正确追踪 JSX 元素的引用，避免 `no-unused-vars` 和 `no-undef` 规则中的误报问题。
- 📦 **RuleTester 增强**：新增断言选项（如 `requireMessage`、`requireLocation`），强化测试用例的验证，并改进失败测试的位置报告。
- 📝 **类型定义更新**：Espree 和 ESLint Scope 包现在包含内置类型定义，取代了之前的 Definitely Typed 包。
- 🔄 **规则与 API 变更**：更新了 `eslint:recommended` 配置，移除了已弃用的规则上下文方法和 `SourceCode` 方法，并引入了 `max-params` 规则的 `countThis` 选项。
- 🎨 **格式化器支持**：新增 `color` 属性到格式化器上下文，允许自定义格式化器根据命令行选项决定是否使用颜色输出。
- 📚 **文档与构建更新**：提供了详细的迁移指南，更新了文档，并进行了多项构建和维护相关的改进。

---

### [2026 年路线图 (2026-02-04) | webpack](https://webpack.js.org/blog/2026-04-02-roadmap-2026/)

**原文标题**: [Roadmap 2026 (2026-02-04) | webpack](https://webpack.js.org/blog/2026-04-02-roadmap-2026/)

webpack 2026 年路线图聚焦于提升开发体验、扩展跨运行时支持、优化性能与构建流程，并加强社区与项目可持续性。

- 🎯 **增强跨平台兼容性**：推出 universal 目标，使代码能在 Node.js、Deno、Bun 及 Web 等多运行时环境中无缝运行。
- 🛠️ **简化配置与依赖**：计划内置支持 CSS Modules、TypeScript 编译和 HTML 入口，减少对第三方插件和加载器的依赖。
- ⚡ **性能优化探索**：评估引入类似 Rspack 的惰性 Barrel 优化，以提升大型代码库的构建速度；并研究多线程 API 以利用多核系统。
- 📚 **改进文档与工具**：通过自动生成 API 文档确保准确性；整合开发中间件与 CLI 工具，提升维护性和用户体验。
- 🤝 **社区与可持续发展**：通过博客、会议加强社区互动；借助 GSoC 导师计划培养贡献者；并积极寻求捐赠与赞助以确保项目长期健康。
- 🚀 **为 webpack 6 铺路**：通过代码清理、测试覆盖和基准测试，为下一代版本打下坚实基础，同时探索资产最小化等新功能。

---

### [ViteLand 2026 年 1 月新动态回顾 | VoidZero](https://voidzero.dev/posts/whats-new-jan-2026)

**原文标题**: [What’s New in ViteLand: January 2026 Recap | VoidZero](https://voidzero.dev/posts/whats-new-jan-2026)

ViteLand 2026 年 1 月更新回顾了 VoidZero 旗下工具链的统一视觉设计、各项目的技术进展及社区动态。

- 🎨 **统一视觉设计**：VoidZero 为旗下所有项目（Vite、Vitest、Rolldown、Oxc）推出全新网站和标识，强化品牌一致性。
- 📈 **Vite 里程碑**：Vite 累计 npm 下载量突破 30 亿次，React Server Components 插件优化提升框架集成体验。
- 🧪 **Vitest 4.1 测试版**：引入测试标签筛选、构建器模式等新功能，支持脱离 Vite 环境运行测试。
- ⚡ **Rolldown 发布候选版**：新增惰性桶优化技术，编译效率提升 2 倍，模块数量减少 92%。
- 🔧 **Oxc 工具增强**：Oxlint 支持动态配置并新增规则，Oxfmt 实现与 Prettier 100% 兼容并集成 Tailwind CSS 排序。
- 🌍 **社区生态活跃**：Turborepo、Hugging Face 等知名项目迁移至 Oxc 工具链，JavaScript 新星榜单中多款工具上榜。
- 📅 **技术会议预告**：团队将在 CityJS 新加坡、Laravel Live 日本等国际会议分享工具链统一愿景。

---

### [Deno Deploy 现已全面开放 | Deno](https://deno.com/blog/deno-deploy-is-ga)

**原文标题**: [Deno Deploy is Generally Available | Deno](https://deno.com/blog/deno-deploy-is-ga)

Deno Deploy 现已全面开放，提供最简单的方式将任何 JavaScript 或 TypeScript 应用部署到网络，支持所有主流框架并自动检测构建流程，实现零配置持续部署和内置数据库管理，同时推出 Deno Sandbox 服务，通过微虚拟机安全执行代码，并提供免费套餐及多种付费方案。

- 🚀 **全面开放**：Deno Deploy 正式推出，支持一键部署 JavaScript/TypeScript 应用，无需适配器或复杂配置。
- 🛠️ **框架兼容**：自动识别并适配主流框架（如 Sveltekit、Next、Astro），优化框架特性使用。
- 🔄 **持续部署**：连接 GitHub 仓库即可实现零配置持续交付，包括实时预览、独立数据库环境和生产发布管理。
- 🗄️ **内置数据库**：支持 Deno KV 和 Postgres，可自动为每个拉取请求创建独立数据库，简化开发流程。
- 🌐 **本地隧道开发**：通过 `--tunnel` 标志实现本地开发与生产环境同步，支持共享环境变量和公开 URL。
- 📊 **自动可观测性**：默认捕获日志、追踪和指标，自动关联请求数据，便于调试和监控。
- 🧪 **安全沙盒**：推出 Deno Sandbox 服务，基于微虚拟机提供安全、快速的代码执行环境，支持即时部署。
- 💰 **灵活定价**：提供免费套餐（每月 100 万请求、100 GB 出口流量、15 CPU 小时）及多种专业和企业方案。

---

### [smnx/promethee：适用于JavaScript的UEFI绑定（概念验证）- Codeberg.org](https://codeberg.org/smnx/promethee)

**原文标题**: [smnx/promethee: UEFI Bindings for JavaScript (Proof of Concept) - Codeberg.org](https://codeberg.org/smnx/promethee)

本文介绍了人工智能在医疗领域的应用现状与前景，重点探讨了其在疾病诊断、治疗方案优化及医疗管理效率提升方面的作用，并简要提及了相关的技术挑战和伦理考量。

- 🤖 AI 辅助诊断系统能通过分析医学影像快速识别病灶，提高早期疾病检出率
- 💊 基于机器学习的个性化治疗方案可结合患者数据优化用药与治疗路径
- 📊 智能医疗管理平台整合临床数据，显著降低医院运营成本并减少人为失误
- ⚠️ 数据隐私保护与算法透明度仍是当前技术落地面临的主要伦理挑战
- 🔮 未来 AI 或将成为远程医疗和预防性医疗体系的核心支撑技术

---

### [Transformers.js v4 预览版：现已在 NPM 上发布！](https://huggingface.co/blog/transformersjs-v4)

**原文标题**: [Transformers.js v4 Preview: Now Available on NPM!](https://huggingface.co/blog/transformersjs-v4)

Transformers.js v4 预览版现已发布，带来 WebGPU 运行时、性能优化、代码库重构、新模型支持及独立分词库等重大更新。

- 🚀 **性能与运行时改进**：采用全新 C++ 编写的 WebGPU 运行时，支持浏览器、Node.js 等多种环境，实现离线运行与 4 倍速度提升。
- 🏗️ **代码库重构**：使用 PNPM 工作区改造为 monorepo，模块化类结构提升可维护性，示例项目移至独立仓库。
- 🎨 **开发体验优化**：统一 Prettier 代码格式化，迁移至 esbuild 构建系统使构建速度提升 10 倍、包体积减小 10%。
- 🤖 **新模型与架构**：新增 GPT-OSS、Mamba、MoE 等先进模型支持，全部兼容 WebGPU 硬件加速。
- 📦 **独立分词库**：推出轻量级@huggingface/tokenizers 库（仅 8.8kB），支持跨平台零依赖分词。
- 🔧 **其他改进**：增强类型系统与日志功能，支持超过 80 亿参数的大模型运行。

---

### [Bun v1.3.9 | Bun 博客](https://bun.sh/blog/bun-v1.3.9)

**原文标题**: [Bun v1.3.9 | Bun Blog](https://bun.sh/blog/bun-v1.3.9)

本文介绍了 Bun 的安装方法、升级方式、并行与顺序运行脚本功能，以及多项性能优化和错误修复。

- 🚀 **安装 Bun**：支持多种安装方式，包括 curl、npm、PowerShell、Scoop、Homebrew 和 Docker。
- 🔄 **升级 Bun**：使用`bun upgrade`命令可轻松升级 Bun 版本。
- ⚙️ **并行与顺序运行脚本**：新增`--parallel`和`--sequential`选项，支持并发或顺序运行 package.json 脚本，并带有前缀输出。
- 🔗 **HTTP/2连接升级**：修复了`net.Server`到`Http2SecureServer`的连接升级模式，适用于 HTTP/2 代理服务器。
- 🧪 **自动恢复模拟和监视**：`mock()`和`spyOn()`支持`Symbol.dispose`，使用`using`关键字可自动恢复模拟，无需手动清理。
- 🛡️ **NO_PROXY 支持**：修复了显式代理选项中`NO_PROXY`环境变量被忽略的问题，确保代理绕过规则生效。
- 📊 **CPU 性能分析**：新增`--cpu-prof-interval`标志，可配置 CPU 分析器的采样间隔，提高性能分析精度。
- 📦 **ESM 字节码支持**：`--compile`命令现在支持 ESM 格式的字节码，提升了编译灵活性。
- 🐛 **ARMv8.0 兼容性修复**：解决了在 ARMv8.0 aarch64 CPU 上的崩溃问题，确保在旧 ARM64 处理器上的稳定运行。
- ⚡ **Markdown 渲染加速**：`Bun.Markdown`通过 SIMD 加速扫描，提升 HTML 转义速度，渲染性能提高 3-15%。
- 🏷️ **React 渲染优化**：`Bun.markdown.react()`缓存常用 HTML 标签字符串，减少内存分配，提升渲染速度。
- 🚫 **AbortSignal 性能提升**：`AbortSignal.abort()`在没有监听器时跳过事件对象创建，性能提升约 6%。
- 🔍 **正则表达式优化**：JavaScriptCore 升级引入 SIMD 加速前缀搜索，大幅提升正则表达式匹配性能。
- 📏 **字符串和集合方法优化**：`String#startsWith`、`Set#size`、`Map#size`、`String#trim`等方法在 JIT 编译层得到优化，性能显著提升。
- 🐞 **错误修复**：包括 Node.js 兼容性改进、Bun API 修复、Web API 问题解决和 TypeScript 类型修正，提升了整体稳定性和开发体验。

---

### [GitHub - vadimdemedes/ink：🌈 用于交互式命令行应用的 React](https://github.com/vadimdemedes/ink)

**原文标题**: [GitHub - vadimdemedes/ink: 🌈 React for interactive command-line apps](https://github.com/vadimdemedes/ink)

Ink 是一个基于 React 的命令行界面（CLI）渲染器，允许开发者使用熟悉的 React 组件模型构建交互式命令行应用。它利用 Yoga 引擎实现终端中的 Flexbox 布局，支持大多数 CSS 样式属性，并提供了丰富的内置组件和钩子来管理输入、输出和焦点。

- 🚀 **核心功能**：使用 React 组件构建 CLI 应用，支持 Flexbox 布局和样式控制。
- 📦 **内置组件**：包括 `<Text>`、`<Box>`、`<Newline>`、`<Spacer>`、`<Static>` 和 `<Transform>` 等，用于处理文本、布局和静态内容。
- 🎮 **交互钩子**：提供 `useInput`、`useApp`、`useStdin`、`useStdout`、`useStderr`、`useFocus` 和 `useFocusManager` 等钩子，方便处理用户输入和焦点管理。
- 🛠️ **开发工具**：支持 React Devtools 集成，便于调试和检查组件树。
- ♿ **无障碍支持**：提供屏幕阅读器支持，可通过 ARIA 属性增强可访问性。
- 📚 **丰富生态**：拥有众多第三方组件和钩子库，如文本输入、选择器、进度条和图表等。
- 🧪 **测试友好**：可与 `ink-testing-library` 配合，轻松测试组件渲染结果。
- 🔧 **灵活配置**：支持自定义输出流、退出控制和渲染模式等选项。

---

### [Ember 6.10 版本发布](https://blog.emberjs.com/ember-released-6-10/)

**原文标题**: [Ember 6.10 Released](https://blog.emberjs.com/ember-released-6-10/)

Ember 6.10 版本发布，这是一个标准的小版本更新，主要聚焦于清理新生成应用的蓝图，包括更新废弃依赖、升级 WarpDrive 和 Glint 的使用，并移除不再需要的默认包。

- 🎉 Ember.js 6.10 未新增功能，但弃用了旧版 AMD 捆绑包，未来将不再发布包含这些捆绑包的 ember-source 包
- 🛠️ Ember CLI v6.10 减少了包弃用警告，更新了应用蓝图，默认使用 WarpDrive 包和 Glint 2，并移除了 tracked-built-ins 和 ember-auto-import
- 📦 依赖包全面更新，包括 broccoli 的新主版本，提升了 ember-cli 的现代性和稳定性
- 🚀 新应用默认直接使用现代 WarpDrive 包替代旧版 ember-data，目前仍以兼容模式运行
- 🔍 Glint 升级至 v2，基于 Volar.js 框架，提供更强大的模板类型检查支持
- 🧹 tracked-built-ins 功能已内置至 ember-source，不再作为独立插件默认安装
- 📤 移除 ember-auto-import，避免不必要的 webpack 依赖，简化项目结构

---

### [JavaScript 自我清理即将变得更加轻松 - Piccalilli](https://piccalil.li/blog/its-about-to-get-a-lot-easier-for-your-javascript-to-clean-up-after-itself/)

**原文标题**: [
  It’s about to get a lot easier for your JavaScript to clean up after itself - Piccalilli
](https://piccalil.li/blog/its-about-to-get-a-lot-easier-for-your-javascript-to-clean-up-after-itself/)

JavaScript 即将通过“显式资源管理”提案，让开发者能更轻松地管理资源清理，提升代码的整洁性和可预测性。

- 🧹 提案引入`using`关键字，声明块作用域变量，在变量离开作用域时自动调用`[Symbol.dispose]()`方法进行资源清理
- 🔗 标准化`[Symbol.dispose]()`方法，为各种资源（如文件、WebSocket 连接等）提供一致的清理接口
- 🗑️ 解释“隐式资源管理”，如 WeakSet 和 WeakMap 的弱引用机制，允许垃圾回收自动清理不再使用的对象
- ⏳ 强调垃圾回收的不可预测性，显式资源管理让开发者能主动控制清理时机
- 🛠️ 提案已进入标准第三阶段，主流浏览器（除 Safari 外）已实现，可用于实验环境
- 🎭 作者以“混乱木偶”自喻，但在 JavaScript 中追求秩序，凸显该提案对代码整洁性的重要性

---

### [Vite、Rust 与 JavaScript 工具的未来 | Better Stack 播客第 11 集 - YouTube](https://www.youtube.com/watch?v=LSGZtHafiM4)

**原文标题**: [Vite, Rust & The Future of JavaScript Tooling | Better Stack Podcast Ep. 11 - YouTube](https://www.youtube.com/watch?v=LSGZtHafiM4)

该页面为 YouTube 平台的政策与信息索引，列出了用户服务相关的核心条款、功能说明及联系渠道。

- 📄 关于平台的基本介绍与背景信息
- 📢 媒体与新闻发布相关内容
- ©️ 版权声明与知识产权保护条款
- 📞 用户联系与反馈渠道
- 🧑‍🎨 内容创作者相关资源与说明
- 📈 广告合作与商业推广信息
- 💻 开发者工具与技术文档
- ⚖️ 服务条款与使用协议
- 🔒 隐私政策与数据保护措施
- ⚙️ 平台政策与安全规范
- ▶️ YouTube 功能运作机制说明
- 🧪 新功能测试与更新公告
- ™️ 谷歌公司版权标识（截至 2026 年）

---

### [无错调试 Next.js：日志如何揭示生产环境中的 Bug | Sentry](https://blog.sentry.io/not-everything-that-breaks-is-an-error-a-logs-and-next-js-story/?utm_source=javascriptweekly&utm_medium=paid-community&utm_campaign=nextjs-fy27q1-nextjs&utm_content=newsletter-sponsored-link-learnmore)

**原文标题**: [Debugging Next.js without errors: how Logs revealed a production bug | Sentry](https://blog.sentry.io/not-everything-that-breaks-is-an-error-a-logs-and-next-js-story/?utm_source=javascriptweekly&utm_medium=paid-community&utm_campaign=nextjs-fy27q1-nextjs&utm_content=newsletter-sponsored-link-learnmore)

本文讲述了作者在开发一个 AI 驱动的 Next.js 应用时，如何通过日志而非仅依赖错误堆栈，成功诊断并解决了一个仅影响 Firefox 和 Safari 浏览器的生产环境 bug。

- 🔍 **错误堆栈仅显示“什么”出错，而日志能揭示“为什么”出错**：作者遇到一个 API 端点在生产环境中拒绝 Firefox 和 Safari 请求的问题，错误堆栈无法提供足够上下文。
- 🤖 **使用 Vercel 的`checkBotId`函数进行机器人防护**：为保护需要调用付费 AI 服务的 API 端点，作者引入了该功能以阻止恶意请求。
- 🐛 **一个仅影响特定浏览器的生产 Bug**：在 Chrome 上运行正常的请求，在 Firefox 和 Safari 上却返回“访问被拒绝”，且错误反复出现。
- 📝 **通过添加日志捕获关键上下文**：作者在`checkBotId`检查处添加了日志，记录检查结果和`User-Agent`请求头，以获取决策依据。
- 🔎 **利用 Sentry 日志的高基数属性定位根源**：通过筛选日志发现，失败的请求其`User-Agent`显示为`ai-sdk`而非浏览器本身，这导致被误判为机器人。
- 🔗 **利用追踪关联功能确认问题场景**：Sentry 的追踪功能确认了带有`ai-sdk`用户代理的请求确实来自 Firefox，从而锁定了问题。
- 🛠️ **通过防火墙规则快速解决问题**：在 Vercel 防火墙设置中添加规则，允许用户代理包含`ai-sdk`的请求绕过机器人检查，问题得以解决。
- 💡 **关于日志与调试的关键启示**：日志提供了错误堆栈无法提供的上下文；高基数属性便于灵活分析；追踪关联能呈现完整画面，三者结合是强大的调试工具。

---

### [AI 调试：能否替代经验丰富的开发者？](https://www.developerway.com/posts/debugging-with-ai)

**原文标题**: [Debugging with AI: Can It Replace an Experienced Developer?](https://www.developerway.com/posts/debugging-with-ai)

本文探讨了 AI 在调试 React/Next.js 应用中的实际能力，通过三个真实 bug 案例测试了 AI 的修复效果，并与人工调试过程进行对比，最终评估 AI 能否替代经验丰富的开发者。

- 🐛 **用户页面崩溃问题**：AI 成功修复了因 Zod 模式验证失败导致的页面错误，通过补充缺失字段数据解决了问题，准确识别了根本原因。
- 🔄 **双重加载器问题**：AI 提出了使用`useSuspenseQuery`的解决方案，虽然暂时有效但可能引发水合不匹配问题，未能正确识别根本原因且修复方案存在缺陷。
- 🚫 **奇怪的重定向错误**：AI 完全未能解决因服务器操作与 Suspense 边界冲突导致的钩子计数错误问题，所有尝试方案均无效且解释具有误导性。
- 🤖 **AI 调试能力评估**：AI 擅长处理模式化问题（如数据验证、常见运行时错误），但在需要深入理解系统行为、考虑未来影响或用户体验的复杂场景中表现不佳。
- 💡 **关键结论**：AI 可作为调试的辅助起点，但开发者必须亲自验证修复方案的正确性；核心技能在于知道何时停止依赖 AI 并开始自主思考。

---

### [将本地开发时间减少 83%：我们为何从 Next.js 迁移——Inngest 博客](https://www.inngest.com/blog/migrating-off-nextjs-tanstack-start)

**原文标题**: [Reducing local dev time by 83%: Why we migrated off Next.js - Inngest Blog](https://www.inngest.com/blog/migrating-off-nextjs-tanstack-start)

Inngest 团队为提高开发体验，将前端框架从 Next.js 迁移至 Tanstack Start，使本地开发页面加载时间从 10-12 秒缩短至 2-3 秒，效率提升显著。

- 🚀 **迁移动机**：Next.js 在本地开发中加载缓慢（10-12 秒），认知开销大，影响小团队效率。
- 🔄 **尝试优化**：升级 Next.js 并试用 Turbopack，但效果有限，仅减少几秒加载时间。
- ⚖️ **框架选型**：评估 Tanstack Start、Deno Fresh 和 React Router v7 后，选择 Tanstack Start，因其明确的路由配置和数据加载方式。
- 🩹 **迁移策略**：采用“快速切换”方式，先转换开发服务器路由（约一周），再处理更复杂的仪表板（数周）。
- ⏱️ **效果提升**：迁移后本地加载时间降至 2-3 秒，后续路由几乎瞬时加载，开发体验大幅改善。
- 🤖 **AI 辅助**：利用 AI 处理重复代码转换和调试，加速迁移过程，减少对日常开发的影响。
- 📚 **经验总结**：频繁构建检查、不依赖开发模式测试，大版本迁移需依赖全面测试而非代码审查。
- 🔗 **开源参考**：迁移代码已开源，供其他团队参考决策。

---

### [在 JavaScriptCore 中实现 Temporal 提案](https://blogs.igalia.com/compilers/2026/02/02/implementing-the-temporal-proposal-in-javascriptcore/)

**原文标题**: [Implementing the Temporal proposal in JavaScriptCore](https://blogs.igalia.com/compilers/2026/02/02/implementing-the-temporal-proposal-in-javascriptcore/)

过去一年，作者在 JavaScriptCore（JSC）中实现了 JavaScript 的 Temporal 提案，以改进日期和时间处理。初始时仅部分支持 Duration、PlainDate、PlainDateTime 和 Instant 类型，且许多测试未通过。现已完成 Duration 精度优化、新增日期类型（如 PlainMonthDay 和 ZonedDateTime），并实现了 relativeTo 参数支持。非 ISO8601 日历支持仍在进行中，测试覆盖大幅提升。所有工作已在 JSC 技术预览版中通过标志启用，预计提交更多代码以完成剩余功能。

- 🗓️ Temporal 提案在 JSC 中已实现 Duration、PlainDate 等基础类型，并优化了精度处理以支持大数值计算。
- 📅 新增了 PlainMonthDay 和 PlainYearMonth 等部分日期类型，以及带时区的 ZonedDateTime 类型。
- ⏱️ 实现了 relativeTo 参数，允许基于起始点转换时间单位（如年转天），解决日历差异问题。
- 🌍 非 ISO8601 日历支持仍在开发中，依赖 ICU 库和未来 Intl 提案。
- ✅ 通过大量测试（test262）提升覆盖率，当前非 intl402 测试全部通过，远优于原版本。
- 🚧 所有功能已在 JSC 技术预览版中通过--useTemporal=1 标志启用，代码以渐进方式提交，预计完成剩余类型和参数支持。

---

### [Angular 22 新特性展望 | MESCIUS](https://developer.mescius.com/blogs/what-to-expect-in-angular-22)

**原文标题**: [What to Expect in Angular 22 | MESCIUS](https://developer.mescius.com/blogs/what-to-expect-in-angular-22)

Angular v22 预计将巩固其信号驱动的响应式架构，提升开发体验，并优化与第三方工具（如 MESCIUS 产品）的集成，以支持更高效、可维护的企业级应用开发。

- 🚀 **信号驱动的响应式架构**：信号成为核心响应式原语，表单等子系统将基于信号实现细粒度更新，提升性能并与无 Zone 变更检测更好对齐。
- 🧩 **组件与模板优化**：引入无选择器组件和模板导入功能，简化组件使用、增强重构能力，并改善工具支持。
- ⚡ **默认变更检测策略**：计划将 OnPush 设为默认策略，鼓励显式性能优化，减少意外性能问题。
- 🛠️ **开发体验提升**：改进热模块替换（HMR）和语言服务，加速开发反馈循环，增强对信号和现代模板语法的支持。
- 🧪 **测试与工具现代化**：推动测试运行器和工具链的现代化，提升与 CI/CD 流程的集成效率。
- 🤖 **AI 工具集成**：通过 MCP 等工具增强 AI 辅助开发能力，提高代码生成和建议的准确性。
- 📊 **MESCIUS 产品集成**：Wijmo、SpreadJS 和 ActiveReportsJS 等 JavaScript 产品将受益于 Angular v22 的响应式改进，实现更高效的数据可视化、表格和报表功能集成。

---

### [Solid.js 最佳实践](https://www.brenelz.com/posts/solid-js-best-practices/)

**原文标题**: [Solid.js Best Practices](https://www.brenelz.com/posts/solid-js-best-practices/)

本文介绍了 Solid.js 框架的最佳实践，涵盖核心概念如信号传递、属性处理、响应式编程、控制流组件、副作用管理、数据派生、复杂状态管理以及 SolidStart 中的预加载和服务器数据交互策略，旨在帮助开发者更高效地利用 Solid 的响应式特性。

- 🚀 在 JSX 属性中传递信号时调用函数，确保组件不依赖信号类型，保持响应性
- 🧩 避免直接解构 props，以保留响应式 getter，或使用`splitProps`处理
- 🔄 使用函数包装器或`createMemo`使派生值在响应式作用域内更新
- 🎛️ 优先使用 Solid 控制流组件如`<Show>`和`<For>`，而非 JavaScript 条件或数组方法
- ⚠️ 谨慎使用`createEffect`，避免用于数据获取或状态同步，推荐`createResource`或派生值
- 📊 尽量派生值而非同步状态，利用 Solid 的依赖图优化更新
- 🗃️ 处理复杂对象时使用 store 而非 signal，实现细粒度响应式更新
- ⏱️ SolidStart 中预加载函数不等待，仅启动工作，让组件处理挂起和解析
- 🔍 使用 query/server 函数获取服务器数据，利用缓存和去重优化
- ✏️ 通过 actions 变更服务器数据，并自动重新验证相关查询

---

### [铁锹 | 铁锹简介](https://shovel.js.org/blog/introducing-shovel/)

**原文标题**: [Shovel | Introducing Shovel](https://shovel.js.org/blog/introducing-shovel/)

Shovel.js 是一个由 AI 辅助开发的开源全栈服务器框架与元框架，旨在让开发者能够像编写浏览器 Service Worker 一样构建和部署 Web 应用，并可在 Node、Bun 和 Cloudflare 等环境中运行。它通过实现浏览器标准 API（如 Cache、FileSystem）并提供配置化全局服务，结合创新的路由、中间件和资源处理机制，提供了一种简洁、标准化且高效的开发体验。

- 🚀 **项目起源**：作者因 Remix 框架放弃 React 而决定自行开发基于 Crank.js 的全栈框架，并借助 Claude Code 在三个月内完成了 Shovel.js。
- 🧩 **设计理念**：核心思想是“将服务器视为 Service Worker”，通过为服务器环境实现浏览器标准 API（如 Cache、FileSystem、CookieStore），创建统一的开发模型。
- 🔧 **核心功能**：提供 CLI 工具和库，支持开发与部署 Service Worker 式应用，替代 Express、Fastify、Vite 或 Next.js 等传统工具。
- 🛣️ **路由与中间件**：内置高性能路由器（基于基数树）和创新的中间件系统，利用生成器函数和 `yield` 操作符简化请求/响应生命周期管理。
- 🌐 **全局服务**：通过 `shovel.json` 配置化地提供缓存、数据库、文件系统、日志等全局服务（如 `self.caches`、`self.databases`），支持多后端（如 S3、Redis、Postgres）。
- 📦 **静态资源处理**：利用 ESBuild 和 import attributes 简化资源引用与打包，无需复杂加载器或文件路由，即可将本地文件路径转换为公共 URL。
- 🔄 **渲染模式统一**：SSR、SSG、SPA 等渲染模式仅通过代码执行时机区分，例如可利用 Service Worker 的 `install` 事件实现静态站点生成。
- 🤖 **AI 辅助开发**：项目全程借助 Claude Code 实现，AI 帮助完成了路由优化、标准 API 实现、配置 DSL 设计等关键任务。
- 🚧 **早期采用**：框架已发布，欢迎早期使用者尝试，作者计划持续扩展功能（如会话、WebSocket、管理界面），并追求“最大程度开箱即用”。

---

### [Service Worker API - Web API | MDN](https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API)

**原文标题**: [Service Worker API - Web APIs | MDN](https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API)

Service Worker API 是一种在浏览器后台运行的脚本，充当网络代理，用于创建离线体验、拦截网络请求、管理缓存，并支持推送通知和后台同步等功能。

- 🛠️ **代理服务器角色**：位于网页应用、浏览器和网络之间，可拦截和处理网络请求。
- 📡 **离线体验与缓存**：支持创建有效的离线应用，能更新服务器资源并缓存内容。
- 🔒 **安全运行环境**：仅适用于安全上下文（如 HTTPS），但本地开发时 `http://localhost` 也被允许。
- ⚙️ **事件驱动与异步**：在独立线程运行，无 DOM 访问权限，完全异步设计，依赖 Promise。
- 📝 **注册与生命周期**：通过 `register()` 方法注册，生命周期包括下载、安装和激活阶段。
- 🔄 **更新机制**：当发现新版本时，会在后台安装并等待旧版本页面关闭后激活。
- 🛡️ **功能控制与扩展**：可用于资源请求拦截、后台数据同步、推送消息响应等多样化场景。
- 🔗 **相关 API 接口**：包括 Cache、FetchEvent、ServiceWorkerRegistration 等，支持缓存管理和事件处理。

---

### [VerifyFetch - 流式完整性验证](https://verifyfetch.com/)

**原文标题**: [VerifyFetch - Streaming Integrity Verification](https://verifyfetch.com/)

VerifyFetch 是一个用于浏览器中大型文件流式完整性验证的 JavaScript 库，旨在解决原生 fetch 在验证大文件时需要完整缓冲导致高内存占用的问题，并提供可恢复下载、多 CDN 故障转移等高级功能，以防范供应链攻击。

- 🛡️ **解决原生 fetch 的痛点**：原生 `fetch({ integrity })` 验证大文件（如 4GB AI 模型）时需完整缓冲，占用大量内存，而 VerifyFetch 支持流式验证，仅需 2MB 内存即可处理任意大小文件。
- 🔄 **支持可恢复下载**：网络中断后可从断点（如 3.8GB/4GB）恢复下载，无需从头开始，并自动将进度持久化到 IndexedDB。
- ⚡ **快速失败的分块验证**：文件在传输过程中即可逐块验证，一旦检测到损坏立即停止，避免下载剩余无效数据。
- 🌐 **多 CDN 故障转移**：支持配置多个备用 URL，自动切换至首个验证通过的 CDN，提升可用性与安全性。
- 🔧 **多种集成方式**：提供简单 API、Service Worker 模式（单行代码保护所有 fetch 请求）和 CLI 工具，适应不同开发需求。
- 📦 **广泛的适用场景**：专为保护 WebAssembly 模块、大型 AI 模型、配置文件及其他关键二进制资产而设计，防止因 CDN 入侵或供应链攻击导致的恶意代码注入。
- 🛠️ **丰富的免费安全工具**：包括 Polyfill 扫描器（检测漏洞脚本）、SRI 生成器（生成哈希和密钥对）和在线 Playground，帮助开发者强化应用安全。
- 🚀 **快速入门**：通过 npm 安装后，可使用 CLI 生成文件哈希清单，并在代码中调用 `verifyFetch` 进行验证，还支持在 CI/CD 中强制执行清单检查。

---

### [GitHub - hamzaydia/verifyfetch：支持断点续传、验证下载的大型浏览器文件工具。在3.8GB处中断后，可从3.8GB处恢复下载。](https://github.com/hamzaydia/verifyfetch)

**原文标题**: [GitHub - hamzaydia/verifyfetch: Resumable, verified downloads for large browser files. Fail at 3.8GB, resume from 3.8GB.](https://github.com/hamzaydia/verifyfetch)

VerifyFetch 是一个用于浏览器中大型文件下载的 JavaScript 库，它通过流式验证、可恢复下载和分块哈希等技术，解决了传统下载方式在内存占用、完整性验证和网络中断恢复等方面的痛点。

- 🛡️ **核心功能**：提供带完整性验证的 `fetch` 替代方案，确保下载文件与预期哈希值匹配，防止 CDN 劫持或文件损坏。
- 💾 **内存优化**：通过流式处理和 WebAssembly 实现恒定内存占用（约 2MB），避免原生 `crypto.subtle.digest()` 需要缓冲整个文件（如 4GB 文件需 4GB+ RAM）导致浏览器崩溃的问题。
- 🔄 **可恢复下载**：支持从网络中断点（如 3.8GB/4GB）恢复下载，而非重新开始，利用 IndexedDB 存储已验证的分块和 HTTP Range 请求。
- ⚡ **快速失败**：通过分块验证，可在下载过程中即时检测到损坏（如第 5 个分块出错），而无需等待整个文件下载完成。
- 🌐 **多 CDN 容错**：支持配置多个源地址，在某个源失败时自动切换到备用源，提供“顺序”、“竞速”或“最快”等策略。
- 📊 **进度追踪**：提供下载进度回调，实时显示百分比、速度、剩余时间等信息。
- 🔧 **多种使用模式**：包括直接 API 调用、Service Worker 模式（零代码集成）和基于清单文件的自动哈希查找。
- 🤖 **AI 模型友好**：专为在浏览器中加载多 GB 的 AI 模型（如 WebLLM、Transformers.js、ONNX）设计，解决大文件下载和验证的难题。
- 🛠️ **配套工具**：提供 CLI 工具生成和验证哈希清单，支持分块哈希生成，并可集成到 CI/CD 流程中。
- ⚙️ **灵活 API**：提供 `verifyFetch`、`verifyFetchStream`、`verifyFetchResumable`、`createVerifyFetcher` 等多种函数，满足不同场景需求。
- 📝 **清单驱动**：支持 JSON 格式的清单文件，可集中管理文件的哈希值、分块信息及元数据。
- 🚫 **安全模型**：采用与浏览器 SRI 相同的信任模型，防止 CDN 攻击和中间人攻击，但需注意无法防范构建过程被入侵或恶意内部人员。
- ⚠️ **注意事项**：需要现代浏览器支持 `crypto.subtle`、`ReadableStream` 和 `IndexedDB`；WebAssembly 为可选，用于实现真正的流式验证，否则会回退到缓冲整个文件的 SubtleCrypto。

---

### [AI 代理文员技能](https://clerk.com/changelog/2026-01-29-clerk-skills?utm_source=cooper_press&utm_medium=newsletter&utm_campaign=skills&utm_content=02-10-26&dub_id=FKDaesWKu6v6oe5l)

**原文标题**: [Clerk Skills for AI Agents](https://clerk.com/changelog/2026-01-29-clerk-skills?utm_source=cooper_press&utm_medium=newsletter&utm_campaign=skills&utm_content=02-10-26&dub_id=FKDaesWKu6v6oe5l)

Clerk 推出可安装技能包，使 AI 编程助手获得关于 Clerk 身份验证的专门知识，帮助开发者快速集成认证功能。

- 🔧 通过单一命令安装所有技能：`npx skills add clerk/skills`
- 🧠 赋予 AI 助手专业身份验证知识，支持多种框架和自定义流程
- 💬 示例应用场景：添加 Next.js 应用认证、构建自定义登录表单、设置 B2B SaaS 组织架构
- 🤖 兼容主流 AI 编程助手：Claude Code、Cursor、Windsurf、GitHub Copilot 等
- 📚 详细技能列表和安装指南可查阅官方技能文档

---

### [GitHub - hectorm/otpauth：适用于Node.js、Deno、Bun及浏览器的一次性密码（HOTP/TOTP）库。](https://github.com/hectorm/otpauth)

**原文标题**: [GitHub - hectorm/otpauth: One Time Password (HOTP/TOTP) library for Node.js, Deno, Bun and browsers.](https://github.com/hectorm/otpauth)

这是一个用于生成和验证一次性密码（HOTP/TOTP）的 JavaScript 库，支持 Node.js、Deno、Bun 和浏览器环境，遵循 RFC 4226 和 RFC 6238 标准，常用于多因素身份验证系统。

- 🔐 支持 HOTP 和 TOTP 协议，适用于双因素身份验证
- 🌐 兼容多种运行环境：Node.js、Deno、Bun 和浏览器
- 📦 提供完整版、精简版和无依赖版三种构建版本
- 🔑 可生成安全随机密钥并支持自定义 HMAC 算法
- 🔄 包含令牌生成、验证、剩余时间计算等完整功能
- 🔗 支持 Google Authenticator 密钥 URI 格式的转换
- 📚 提供详细文档和在线演示应用
- ⚖️ 采用 MIT 开源许可证

---

### [GitHub - shaka-project/shaka-player: JavaScript 播放器库 / DASH 与 HLS 客户端 / MSE-EME 播放器](https://github.com/shaka-project/shaka-player)

**原文标题**: [GitHub - shaka-project/shaka-player: JavaScript player library / DASH & HLS client / MSE-EME player](https://github.com/shaka-project/shaka-player)

Shaka Player 是一个开源的 JavaScript 媒体播放库，支持 DASH 和 HLS 自适应流媒体格式，无需插件或 Flash，基于现代浏览器标准（MSE 和 EME）构建，并具备离线存储与播放、DRM 支持、广告插入和 VR 播放等功能。

- 🎬 **开源播放库**：基于 JavaScript，支持 DASH 和 HLS 自适应流媒体播放，无需插件。
- 🌐 **现代标准**：利用 MediaSource Extensions (MSE) 和 Encrypted Media Extensions (EME) 实现跨浏览器兼容。
- 📦 **离线功能**：通过 IndexedDB 支持媒体内容的离线存储和播放。
- 🔒 **DRM 支持**：兼容 Widevine、PlayReady、FairPlay 等多种数字版权管理方案。
- 🖥️ **多平台**：支持 Chrome、Firefox、Safari、Edge 等主流浏览器及智能电视、游戏机等设备。
- 📊 **格式广泛**：支持 MP4、WebM、MPEG-2 TS 等容器格式，以及 WebVTT、TTML 字幕和 CEA-608/708 字幕。
- 🔄 **高级特性**：包括内容转向、广告插入（IMA SDK、AWS MediaTailor）、VR 播放和低延迟流媒体。
- 🛠️ **可扩展性**：提供自定义清单解析器、文本显示插件和实验性功能（如 MOQT 流媒体格式）。
- 📚 **丰富资源**：包含演示、API 文档、教程和社区维护的框架集成（如 React、Vue、Angular）。
- 👥 **活跃社区**：由开源社区维护，拥有详细的贡献指南和持续更新。

---

### [Shaka 播放器演示](https://shaka-project.github.io/shaka-player/demo/)

**原文标题**: [Shaka Player Demo](https://shaka-project.github.io/shaka-player/demo/)

该项目提供了 jQuery 相关的资源链接、许可证信息、浏览器支持测试以及多种使用模式。

- 📚 文档与许可证：提供项目文档和 Apache 许可证信息
- 🔗 代码与分发：源代码托管于 GitHub，可通过 NPM 获取包，并支持 CDN 及多个托管库
- 🌐 兼容性测试：包含浏览器支持测试链接
- 🛠️ 使用模式：提供编译版（含发布和调试版本）及未编译版本供不同开发需求使用

---

### [GitHub - meriyah/meriyah：一个100%兼容、自托管的JavaScript解析器 - https://meriyah.github.io/meriyah](https://github.com/meriyah/meriyah)

**原文标题**: [GitHub - meriyah/meriyah: A 100% compliant, self-hosted javascript parser  - https://meriyah.github.io/meriyah](https://github.com/meriyah/meriyah)

Meriyah 是一个完全符合标准、自托管的 JavaScript 解析器，专注于高性能和稳定性，已用于生产环境。它支持最新的 ECMAScript 规范、部分 TC39 提案以及 JSX 语法，并生成兼容 ESTree 的抽象语法树。

- 🚀 **高性能与稳定性**：专为性能与稳定性设计，已在生产环境中使用。
- 📜 **标准兼容**：完全符合 ECMAScript® 2024 语言规范，并支持 Web 浏览器附加特性。
- ⚙️ **灵活配置**：提供多种解析选项，如脚本/模块模式、位置信息追踪和严格模式。
- 🔮 **实验性支持**：通过选项启用部分 TC39 第三阶段提案，如装饰器和 JSON 模块。
- 🧩 **JSX 支持**：可通过配置选项启用 JSX 语法解析。
- 🚫 **明确限制**：不支持 TypeScript 或 Flow 语法，正则表达式验证依赖运行时环境。
- 📦 **易于集成**：通过 npm 安装，API 简单易用，支持错误检测和注释提取。

---

### [梅里亚](https://meriyah.github.io/meriyah/)

**原文标题**: [Meriyah](https://meriyah.github.io/meriyah/)

本文介绍了人工智能在医疗领域的应用现状与前景，重点探讨了其在疾病诊断、药物研发和个性化治疗方面的突破性进展，同时简要提及了相关的伦理挑战。

- 🏥 AI 辅助诊断系统能通过分析医学影像快速识别病灶，提升早期癌症等疾病的检出率
- 🔬 机器学习加速了新药研发过程，大幅缩短化合物筛选与临床试验周期
- 📊 基于患者基因数据的人工智能模型可为慢性病患者提供个性化治疗方案
- ⚖️ 医疗 AI 面临数据隐私、算法透明度及责任认定等伦理监管问题

---

### [React Grab 1.0](https://www.react-grab.com/blog/1-0)

**原文标题**: [React Grab 1.0](https://www.react-grab.com/blog/1-0)

React Grab 1.0 正式发布，这是一个允许开发者直接从网站中选择上下文以加速编码代理工具的工具。

- 🚀 支持多种开发框架，包括 Next.js、Vite、Webpack 和 TanStack Start
- ⚡ 可将 Cursor、Claude Code、Copilot 等工具的运行速度提升高达 3 倍
- 📦 通过 `npx -y grab@latest init` 命令快速安装和初始化

---

### [React 代理抓取工具](https://www.react-grab.com/blog/agent)

**原文标题**: [React Grab for Agents](https://www.react-grab.com/blog/agent)

React Grab 现已升级为可直接与 AI 编程助手交互，在浏览器内完成代码编辑，无需切换应用或复制粘贴。

- 🚀 **功能升级**：从仅复制 React 上下文，变为可直接在页面内启动 Claude Code、Cursor 等助手并执行多任务编辑
- 🛠️ **核心不变**：仍免费开源，支持所有主流 AI 编程工具，保持“点击元素即获精确组件路径”的理念
- 💡 **诞生背景**：为解决 AI 助手在复杂代码库中定位 UI 组件效率低下的痛点，初版使任务速度平均提升约 3 倍
- 🔄 **工作流程**：按住 ⌘C 点击元素 → 输入修改指令 → 助手直接修改代码文件 → 页面自动刷新显示变更
- ⚙️ **技术原理**：通过 React fiber 树获取组件堆栈与源码位置，新增的“代理提供者”将上下文与指令转发至本地 CLI 执行
- 📦 **快速安装**：在项目根目录运行 `npx -y grab@latest init` 即可自动配置
- 🔮 **未来方向**：保持工具无关性，任何具备 CLI/API 的编程助手均可通过开发提供者适配集成

---

### [GitHub - downshift-js/downshift: 🏎 一套用于构建简单、灵活且符合 WAI-ARIA 标准的 React 自动完成、组合框或选择下拉组件的原语。](https://github.com/downshift-js/downshift)

**原文标题**: [GitHub - downshift-js/downshift: 🏎 A set of primitives to build simple, flexible, WAI-ARIA compliant React autocomplete, combobox or select dropdown components.](https://github.com/downshift-js/downshift)

Downshift 是一个用于构建简单、灵活且符合 WAI-ARIA 标准的 React 自动完成、组合框或选择下拉组件的原始工具集。

- 🏎 提供 React hooks（如 `useSelect`、`useCombobox`）和 `Downshift` 组件，支持创建可访问的 UI 组件
- 📚 遵循最新的 ARIA 1.2 设计模式，推荐使用 hooks 以获取更好的可访问性和维护性
- ⚙️ 采用渲染属性（render prop）模式，赋予开发者完整的 UI 控制权，同时通过属性获取器简化事件处理和状态管理
- 🔧 支持高级功能如状态管理、自定义事件处理、服务器端渲染（SSR）和 React Native 集成
- 🌍 包含丰富的示例和文档，涵盖从基础到高级的使用场景，并支持多语言和社区贡献
- 📦 通过 npm 安装，依赖 React，同时兼容 Preact，采用 MIT 许可证开源

---

### [GitHub - ocsigen/js_of_ocaml：从OCaml到JavaScript的编译器](https://github.com/ocsigen/js_of_ocaml)

**原文标题**: [GitHub - ocsigen/js_of_ocaml: Compiler from OCaml to Javascript.](https://github.com/ocsigen/js_of_ocaml)

Js_of_ocaml 是一个将 OCaml 字节码编译为 JavaScript 的编译器，允许在浏览器或 Node.js 等 JavaScript 环境中运行纯 OCaml 程序。它基于现有 OCaml 安装工作，无需重新编译库，并提供了大量浏览器 API 的绑定。生成的代码通常比 OCaml 字节码解释器运行更快，且维护相对容易。项目包含编译器、语法扩展、基础库等多个包，支持 Node.js 16 及以上版本和现代浏览器。

- 🛠️ **编译器功能**：将 OCaml 字节码转换为 JavaScript，支持在浏览器和 Node.js 中运行 OCaml 程序。
- 📦 **易于集成**：无需重编译 OCaml 库，通过 opam 安装即可使用，兼容现有 OCaml 环境。
- 🌐 **浏览器绑定**：提供广泛的浏览器 API 绑定，方便开发 Web 应用。
- ⚡ **性能优势**：生成的 JavaScript 代码运行速度通常快于 OCaml 字节码解释器。
- 📚 **多包组成**：包括编译器、语法扩展、基础库、Lwt 支持、TyXML 支持等多个独立包。
- 🔄 **数据表示差异**：整数为 32 位，浮点数不装箱，影响序列化、哈希等操作的结果。
- 🎯 **尾调用优化**：支持自递归函数和相互递归函数的优化，提升性能。
- 🖥️ **交互式环境**：提供基于 Web 的 OCaml 顶层环境（toplevel），支持代码高亮和缩进。

---

### [GitHub - TaTo30/vue-pdf: Vue 3 的 PDF 组件](https://github.com/TaTo30/vue-pdf)

**原文标题**: [GitHub - TaTo30/vue-pdf: PDF component for Vue 3](https://github.com/TaTo30/vue-pdf)

VuePDF 是一个用于 Vue 3 的客户端 PDF 渲染组件，基于 pdf.js 库开发，支持文本层、注释层、XFA 表单和注释编辑等高级功能，并提供了服务器端渲染和旧版浏览器兼容性解决方案。

- 📦 VuePDF 是一个基于 pdf.js 的 Vue 3 客户端 PDF 渲染组件
- 🛠️ 支持文本选择、注释交互、XFA 表单和注释编辑层等高级功能
- 📄 提供基础用法和最小化构建选项，可自定义 PDF 工作线程配置
- 🎨 需要导入 CSS 样式文件以确保文本层和注释层正确渲染
- 🌐 支持非拉丁字符显示，需配置 cmaps 目录
- 🔧 提供旧版浏览器兼容性解决方案和常见问题排查指南
- ⚙️ 支持服务器端渲染框架（如 Nuxt），需使用客户端指令包装
- 🐛 解决了扫描 JPEG PDF 空白页和 wasm 缺失等常见问题
- 📈 项目采用 MIT 许可证，欢迎贡献代码和文档改进

---

### [Lume，专为 Deno 打造的静态网站生成器 - Lume](https://lume.land/)

**原文标题**: [Lume, the static site generator for Deno - Lume](https://lume.land/)

本文介绍了为英国大选创建六边形地图（hexmap）的方法与过程，旨在通过视觉化方式更直观地展示选举结果。

- 🗺️ 六边形地图通过将每个选区表示为相同大小的六边形，避免了因选区面积差异造成的视觉误导，使选举结果对比更公平清晰。
- 🛠️ 制作过程结合了地理数据处理、选区匹配和手动调整，确保每个六边形位置既反映实际地理关系，又保持布局紧凑美观。
- 📊 该地图可用于突出显示选举关键变化，如选区翻转、政党优势区域，帮助读者快速把握整体政治格局。
- 🔍 项目强调了数据可视化在政治分析中的重要性，提供了开源工具与步骤，鼓励更多人参与类似的数据表达创新。

---

### [精密 AI - 无需编写测试的自动化前端测试](https://www.meticulous.ai?utm_source=jsweekly&utm_medium=referral&utm_campaign=26q1&utm_content=classified)

**原文标题**: [Meticulous AI - Automated Frontend Testing Without Writing Tests](https://www.meticulous.ai?utm_source=jsweekly&utm_medium=referral&utm_campaign=26q1&utm_content=classified)

Meticulous AI 是一款创新的自动化测试工具，通过记录用户与应用的交互来生成并维护测试套件，无需手动编写或维护测试代码，帮助开发团队高效、无差错地发布代码。

- 🚀 无需编写测试：通过记录开发、预演和生产环境中的用户交互，自动生成覆盖所有代码分支和边缘情况的测试
- 🔄 测试自动演进：随着应用更新，测试套件自动添加新测试并淘汰过时部分，保持测试的时效性和完整性
- ⚡ 高速并行测试：利用计算集群并行执行测试，可在 120 秒内完成数千个屏幕的测试
- 🛡️ 消除测试波动：基于 Chromium 构建的确定性调度引擎，从根本上消除测试的不稳定性，确保结果可靠
- 🔗 灵活集成：支持与现有测试套件结合使用或完全替代，提供与主流前端框架（如 React、Vue、Angular 等）的集成
- 📈 提升开发效率：被 Dropbox、Notion 等超过 100 家组织信任，显著加快代码发布速度，减少回归错误

---

### [STRICH | 适用于网页应用的条形码扫描](https://strich.io/?ref=js-weekly)

**原文标题**: [STRICH | Barcode Scanning for Web Apps](https://strich.io/?ref=js-weekly)

STRICH 是一款用于网页应用的 JavaScript 库，支持在浏览器中实时扫描一维和二维条码，无需原生应用或后端支持。

- 📦 通过 npm 安装，提供免费试用和演示应用
- 🚀 基于现代 Web 技术（WebAssembly/WebGL），兼容主流浏览器与框架
- 💰 提供透明定价，无设备限制，支持按月订阅或企业方案
- 🛠️ 内置扫描界面，支持离线操作、白标定制及多种条码类型
- 🌟 客户反馈积极，强调易集成、高准确度与优质支持
- 🌐 倡导网页应用优势：无需应用商店、易于分发、降低成本
- 🔧 持续更新维护，包含企业级功能与合规支持

---

### [半色调的渐变 - 马克西姆·赫克尔的博客](https://blog.maximeheckel.com/posts/shades-of-halftone/)

**原文标题**: [Shades of Halftone - The Blog of Maxime Heckel](https://blog.maximeheckel.com/posts/shades-of-halftone/)

本文深入探讨了半色调（halftone）效果的历史、原理及其在现代数字设计中的多样化实现方式，从基础的网格圆点到复杂的多通道 CMYK 模拟，展示了如何通过 GLSL 着色器创造丰富的视觉纹理和艺术风格。

- 🎨 **半色调的复兴与艺术应用**：半色调作为一种经典的点阵图案，最初用于有限墨色的印刷，现已成为跨媒体和网页设计的艺术工具，通过软件如 Paper、Efecto 等普及，赋予数字输出独特的纹理感。
- 🔍 **光学原理与实现基础**：半色调通过高频点阵模拟连续色调，利用人眼的空间分辨率限制，使大脑对图案进行空间平均，从而感知平滑渐变。其 GLSL 实现核心包括绘制圆形距离场和网格生成（使用`fract`函数）。
- ⚙️ **基础到高级的实现步骤**：从单一圆形的渲染出发，结合网格化和像素化纹理，通过调整点的大小（基于亮度值）和网格偏移，实现经典半色调效果，并引入抗锯齿（如`smoothstep`）优化显示。
- 🌈 **多通道与颜色混合**：探索 RGB 和 CMYK 多通道半色调，通过叠加不同颜色的网格层模拟物理印刷中的颜色混合。CMYK 版本需转换颜色空间并旋转各层以减少莫尔条纹（Moiré）干扰。
- 🌀 **突破网格的创新变体**：通过采样邻近单元格（3x3 内核）消除点阵的“裁剪”限制，实现点的溢出与融合，创造出液态（gooey）效果和动态位移（如跟随光标轨迹），增强有机感和交互性。
- 🚀 **性能与艺术扩展**：较大内核虽提升效果真实性但增加性能开销；半色调作为模块化着色器的基础，可扩展至实时绘画风格模拟（如点彩、水彩），展示了其持续的艺术与技术潜力。

---

### [引言 - React Three Fiber](https://r3f.docs.pmnd.rs/getting-started/introduction)

**原文标题**: [Introduction - React Three Fiber](https://r3f.docs.pmnd.rs/getting-started/introduction)

React-three-fiber 是一个用于 three.js 的 React 渲染器，允许开发者以声明式、组件化的方式构建 3D 场景，并充分利用 React 的状态管理和生态系统。

- 🎨 使用声明式 JSX 语法构建 three.js 场景，支持可复用、自包含的交互式组件
- ⚡ 无性能开销，组件在 React 外渲染，且借助 React 调度能力可处理大规模场景
- 🔄 与 three.js 完全兼容，新特性无需等待库更新即可直接使用
- 📦 提供丰富的生态系统，包括物理引擎、后期处理、VR/AR 等扩展库
- 🛠️ 支持 Web、React Native 及 TypeScript，示例包含交互式旋转立方体组件
- 🌐 要求具备 React 和 three.js 基础，推荐结合官方文档及社区资源学习

---

### [AI PaaS：用于部署、管理和扩展应用程序的平台](https://www.heroku.com/)

**原文标题**: [The AI PaaS for Deploying, Managing, and Scaling Apps](https://www.heroku.com/)

Heroku 是一个全托管云应用平台，专注于简化 AI 应用和智能体开发，让开发者无需管理底层基础设施，从而更专注于构建数据驱动的应用程序。

- 🚀 **简化 AI 开发**：提供托管推理和智能体服务，可快速接入领先 AI 模型，通过 Model Context Protocol（MCP）轻松扩展工具与 API 集成。
- 🗄️ **集成向量数据库**：Heroku Postgres 支持 pgvector，便于构建 RAG 应用或执行向量相似性搜索，实现嵌入数据与业务数据的统一存储查询。
- 🌐 **丰富生态系统**：拥有 150 多个第三方插件和 380 多个开源构建包，支持 Node.js、Ruby、Java、Python 等主流语言，并可灵活扩展其他语言。
- ⚙️ **强大功能集**：包括智能容器运行环境、全托管 PostgreSQL 数据库、Redis 键值存储、弹性扩展、团队协作、快速回滚、应用监控及持续交付等核心功能。
- 🔒 **安全合规**：平台定期接受审计，符合 PCI、HIPAA、ISO、SOC 等合规标准，提供 Heroku Shield 等高合规性解决方案。
- 🏢 **企业级支持**：提供私有空间、单点登录（SSO）、Heroku Connect 数据同步及企业级 SLA 支持，满足大型组织的安全和协作需求。
- 📈 **广泛适用性**：服务于开发者、CTO、初创公司至大型企业等各类用户，提供从原型验证到关键业务系统的全场景支持。

---

### [Heroku 最新动态](https://www.heroku.com/blog/an-update-on-heroku/)

**原文标题**: [An Update on Heroku](https://www.heroku.com/blog/an-update-on-heroku/)

Heroku 将转向以稳定性、安全性和可靠性为核心的维护模式，现有服务与价格保持不变，但不再为新客户提供企业合同，以集中资源发展企业级 AI 等长期价值领域。

- 🛠️ Heroku 进入维护模式，专注稳定性、安全与支持，而非新增功能
- 💳 现有及新个人客户（信用卡支付）的服务、价格与使用均无变化
- 📝 企业合同不再对新客户开放，现有合约继续履行并可续约
- 🎯 公司将资源集中于企业级 AI 等能创造长期价值的领域

---

### [Heroku 最新动态 | 黑客新闻](https://news.ycombinator.com/item?id=46913903)

**原文标题**: [An Update on Heroku | Hacker News](https://news.ycombinator.com/item?id=46913903)

Heroku 宣布将转向“持续工程模式”，重点维持现有服务质量和运营稳定，而非推出新功能。企业版合同将不再向新客户开放，但现有客户服务暂时不变。公司表示此举是为了更专注于企业级 AI 等新兴领域。

- 🛠️ **技术债务与扩展挑战**：前员工指出，Heroku 在 2011-2012 年因快速增长面临严重技术债务和扩展压力，尽管团队规模扩大，仍难以跟上需求。
- 🚀 **简单部署体验**：用户怀念 Heroku“git push”一键部署的极致简洁性，认为当前市场仍缺乏完全媲美的平台即服务（PaaS）产品。
- 📉 **收购后逐渐停滞**：Salesforce 于 2010 年收购 Heroku，初期给予资金支持，但随后创始人淡出、领导力缺失，产品创新逐渐停滞。
- 🔄 **市场竞争与替代方案**：用户讨论 Render、Fly.io、Railway 等替代平台，部分肯定其易用性，但也指出在功能或定价方面与 Heroku 存在差距。
- 💡 **工程文化与影响**：前员工赞扬 Heroku 早期的工程团队和创新文化，其设计理念（如“输入 - 过滤 - 输出”模式）对行业影响深远。
- 🏢 **企业决策与沟通模糊**：官方公告被批评为“企业废话”，模糊的表述引发用户对服务即将关闭的担忧和不满。

---

### [Remotion | 以编程方式制作视频](https://www.remotion.dev/)

**原文标题**: [Remotion | Make videos programmatically](https://www.remotion.dev/)

Remotion 是一个基于 React 的程序化视频创作平台，允许开发者通过代码创建、编辑和渲染动态视频，适用于多种应用场景并提供灵活的许可方案。

- 🎬 使用 React 技术栈编写代码来创建和参数化视频内容
- 🖥️ 提供 Remotion Studio、Player 和 Editor Starter 等工具支持动态编辑
- ⚙️ 支持本地、服务器或无服务器环境渲染 MP4 等多种格式视频
- 💼 提供免费许可（3 人以下团队）和公司许可（4 人以上团队）两种方案
- 🏢 企业版包含优先支持、定制条款和每月咨询会议等高级服务
- 🤝 拥有活跃社区，每月 90 万次安装、6000 多名 Discord 成员和 300 多名贡献者
- 🛠️ 可通过 Editor Starter 模板构建自定义视频编辑应用程序
- 📈 适用于音乐可视化、字幕生成、屏幕录制和年度回顾等多种用例

---

### [用 AI 创建动态图形——初学者简易教程 - YouTube](https://www.youtube.com/watch?v=5NRAOnKc3c8)

**原文标题**: [Create motion graphics with AI – Simple tutorial for beginners - YouTube](https://www.youtube.com/watch?v=5NRAOnKc3c8)

该页面为 YouTube 平台的官方信息与政策说明区域，涵盖服务条款、隐私政策及功能说明等内容。

- 📄 关于平台的基本信息与介绍
- 📢 新闻发布与媒体资源
- ©️ 版权政策与保护措施
- 📞 联系与反馈渠道
- 🧑‍🎨 创作者相关资源与支持
- 💼 广告合作与商业推广
- 👨‍💻 开发者工具与 API 资源
- ⚖️ 服务条款与使用协议
- 🔒 隐私政策与数据保护
- 🛡️ 平台安全与使用规范
- 🔄 功能更新与测试说明
- ℹ️ 平台运作机制介绍

---

### [Node.js v24.13.0 文档](https://nodejs-api-docs-tooling.vercel.app/)

**原文标题**: [| Node.js v24.13.0 Documentation](https://nodejs-api-docs-tooling.vercel.app/)

Node.js 文档提供了全面的 API 参考和指南，涵盖从核心模块到高级功能的广泛主题，旨在帮助开发者构建高效的服务器端和网络应用。

- 📚 **核心模块与 API** – 包括文件系统、网络、加密等基础功能
- 🔄 **异步与事件处理** – 支持异步操作、事件驱动和流处理
- 🌐 **网络与通信** – 提供 HTTP/HTTPS、TCP/UDP、DNS 等网络协议支持
- ⚙️ **系统与进程管理** – 涉及子进程、集群、性能钩子和系统交互
- 📦 **模块与包管理** – 支持 CommonJS 和 ES 模块，包含 TypeScript 集成
- 🛠️ **工具与调试** – 提供调试器、测试运行器、错误处理和诊断工具
- 🔐 **安全与加密** – 涵盖 TLS/SSL、Web Crypto API 和权限管理
- 🌍 **国际化与兼容性** – 支持国际化、URL 处理和 Web 标准 API

---

### [GitHub · 软件构建之地](https://github.com/nodejs/doc-kit/issues)

**原文标题**: [GitHub · Where software is built](https://github.com/nodejs/doc-kit/issues)

Node.js 官方文档工具 doc-kit 项目在 GitHub 上公开了其 2026 年路线图及一系列待处理的议题，涵盖功能增强、错误修复和迁移任务。

- 🗺️ **2026 年路线图**：概述了项目新一年的主要发展方向和目标。
- 🐛 **用户体验问题**：切换页面明暗模式时需滚动回顶部，已被确认为待修复的缺陷。
- 🔄 **Web 生成器迁移**：多项任务与此关键迁移工作相关，包括重构参数表和自动化 npm 发布流程。
- ⚙️ **功能开发**：计划实现记住用户的 ESM/CJS 选择、改进 JavaScript 与 Markdown 的混合解析等新功能。
- 🧪 **测试与质量**：强调了进行端到端测试和为元数据生成器添加测试的重要性，部分任务标记为适合新手参与。
- 📦 **模块化与分发**：旨在按类或章节对模块文件进行分块，并简化 DTS 使用者的体验。
- 🏷️ **界面与状态显示**：提议在标题右侧添加显著的活动状态指示器。

---

