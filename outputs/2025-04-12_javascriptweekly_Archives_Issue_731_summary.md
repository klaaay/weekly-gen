## [Read on the Web](https://javascriptweekly.com/issues/731)

**原文标题**: [JavaScript Weekly Issue 731: April 11, 2025](https://javascriptweekly.com/issues/731)

**中文标题**: 《JavaScript 周刊》第 731 期：2025 年 4 月 11 日

概述：本期内容涵盖 JavaScript 和前端开发的最新动态，包括 Google Firebase 的 AI 开发环境、JavaScript 新特性、Next.js 教程、Node.js 测试实践、以及多个工具和库的更新。此外，还包含一些实用的开发技巧和资源推荐。

- 🔥 **Google 推出 Firebase Studio**：基于 AI 的开发环境，类似 Cursor/v0，支持浏览器内应用构建。  
- 📜 **JavaScript 2025 新特性**：包括 iterator helpers、`structuredClone()`和集合操作等。  
- 🎓 **Next.js 教程 v4**：学习 React Server Components、Server Actions、动态路由等，并部署到 Vercel。  
- 🧪 **Node.js 测试最佳实践**：GitHub 上的详细指南，覆盖 50 多个测试技巧，如“测试钻石”和微服务测试。  
- ⚠️ **npm 令牌问题**：npm 注册表可能清空所有访问令牌，建议创建新令牌。  
- ☁️ **Cloudflare 更新**：支持 Next.js 部署到 Workers、Vite 插件 v1 发布，以及全栈一键部署功能。  
- 🚀 **RedwoodJS 未来展望**：React 框架的“下一个纪元”计划更新。  
- 🛠️ **工具发布**：TypeSpec 1.0-RC、pnpm 10.8、Prisma 6.6、React Native 0.79 等。  
- 📖 **文章与教程**：比较 Tauri 和 Electron、空值合并运算符（`??`）的使用、Clerk 与 Supabase 集成等。  
- 🔧 **代码与工具**：Next.js 15.3 支持 Turbopack 构建、Chrono 2.8 自然语言日期解析器、Wallaby 调试工具等。  
- 📢 **其他资源**：Git 20 周年访谈、PostScript 编程、CSS 模糊图片占位技术等。

---

## [Firebase Studio: Google's New Agentic AI-Powered Development Environment](https://firebase.studio/)

**原文标题**: [Firebase Studio](https://firebase.studio/)

**中文标题**: Firebase 工作室

Firebase Studio 是一个全栈 AI 工作空间，通过 AI 代理加速整个开发生命周期，支持后端、前端和移动应用的构建。

- 🚀 **快速开始**：从浏览器打开到构建只需几分钟，支持从 GitHub、GitLab 等导入现有仓库，或使用 App Prototyping 代理快速创建新应用。
- 🛠️ **灵活构建**：支持自然语言、草图工具、截图或模板创建应用，并可利用 Nix 自定义环境。
- 🆓 **免费预览**：预览期间提供 3 个免费工作空间，Google 开发者计划成员可享最多 30 个。
- 🤖 **AI 助力**：集成 Gemini，协助编码、调试、测试、重构等，支持选择不同模型，新 Gemini Code Assist 代理可帮助迁移和 AI 测试。
- 📱 **跨平台测试**：通过 Open VSX Registry 的扩展测试和优化 API 及后端，内置网页预览和 Android 模拟器。
- 🚀 **部署与监控**：一键发布到 Firebase App Hosting，支持 Firebase Hosting、Cloud Run 或自定义基础设施部署。
- 🔍� **持续创新**：Firebase 持续进化，支持生成式 AI 和新型构建方式，助力开发者更高效地开发应用。

---

## [Gemini 2.5 Pro](https://blog.google/technology/google-deepmind/gemini-model-thinking-updates-march-2025/)

**原文标题**: [Gemini 2.5: Our newest Gemini model with thinking](https://blog.google/technology/google-deepmind/gemini-model-thinking-updates-march-2025/)

**中文标题**: "Gemini 2.5：我们具备思考能力的最新 Gemini 模型"

Google DeepMind 发布了其最智能的 AI 模型 Gemini 2.5，具备强大的推理和编码能力，并在多个基准测试中领先。

- 🧠 Gemini 2.5 Pro Experimental 是目前最先进的 AI 模型，擅长处理复杂任务，在 LMArena 排行榜上领先。  
- 📊 该模型在数学、科学和编码基准测试中表现优异，如 GPQA 和 AIME 2025。  
- 💻 Gemini 2.5 在编码性能上有显著提升，擅长创建视觉吸引人的网页应用和代理代码应用。  
- 🔍 具备增强的推理能力，能够分析信息、结合上下文并做出明智决策。  
- 🌐 支持多模态输入（文本、音频、图像、视频等），并拥有 100 万 token 的上下文窗口（未来将扩展至 200 万）。  
- 🚀 开发者可通过 Google AI Studio 和 Gemini Advanced 体验 Gemini 2.5 Pro，Vertex AI 版本即将推出。  
- 📈 未来将进一步优化模型，并逐步推出定价方案，支持规模化生产使用。

---

## [Some Features Every JavaScript Developer Should Know in 2025](https://waspdev.com/articles/2025-04-06/features-that-every-js-developer-must-know-in-2025)

**原文标题**: [Some features that every JavaScript developer should know in 2025 | WaspDev](https://waspdev.com/articles/2025-04-06/features-that-every-js-developer-must-know-in-2025)

**中文标题**: "2025 年每位 JavaScript 开发者都应了解的一些特性 | WaspDev"

JavaScript 在 2025 年开发者应掌握的重要特性，涵盖迭代器助手、数组方法、Promise 优化、字符串处理、变量交换、深拷贝、标记模板、WeakMap/WeakSet 及集合操作等现代功能。

- 🔄 **迭代器助手**：通过`Iterator.prototype`方法（如`drop()`、`take()`、`filter()`等）实现高效链式操作，避免临时数组分配，提升大数组处理性能。  
- 📌 **数组 at() 方法**：支持负索引访问元素（如`arr.at(-1)`），简化末尾元素获取，替代`arr[arr.length-1]`的冗长写法。  
- 🤝 **Promise.withResolvers()**：简化 Promise 构造，直接解构出`promise`、`resolve`、`reject`，告别手动赋值冗余代码。  
- ✏️ **字符串替换回调**：`replace()`/`replaceAll()`支持回调函数，单次遍历完成复杂替换（如动态计数替换），提升效率。  
- 🔄 **变量交换**：使用解构赋值`[a, b] = [b, a]`替代临时变量，代码更简洁。  
- 🧩 **深拷贝 API**：优先用`structuredClone()`替代`JSON.stringify()`，正确处理`NaN`、循环引用等场景，避免数据丢失或异常。  
- 🏷️ **标记模板**：通过标签函数解析模板字符串（如自动 HTML 转义），灵活处理插值内容。  
- 🗑️ **WeakMap/WeakSet**：弱引用集合，键对象无引用时自动垃圾回收，适合无副作用的对象关联场景。  
- 🔗 **集合操作**：新增`difference()`、`intersection()`、`union()`等方法，支持集合间布尔运算（如差集、并集），简化逻辑处理。

---

## [Node.js Testing Best Practices](https://github.com/goldbergyoni/nodejs-testing-best-practices#readme)

**原文标题**: [GitHub - goldbergyoni/nodejs-testing-best-practices: Beyond the basics of Node.js testing. Including a super-comprehensive best practices list and an example app (April 2025)](https://github.com/goldbergyoni/nodejs-testing-best-practices#readme)

**中文标题**: GitHub - goldbergyoni/nodejs-testing-best-practices: Node.js 测试进阶指南。包含一份超级全面的最佳实践清单和示例应用（2025 年 4 月）

Node.js 测试最佳实践概述，涵盖从基础到高级的测试策略、工具和示例应用。

- 🚀 **50+ 最佳实践列表** - 提供如何以正确方式编写现代测试的详细指南。
- 📊 **示例应用** - 展示典型 Node.js 后端的高性能测试设置（40 个测试在 5 秒内完成，包括数据库）。
- 🎯 **高级主题** - 超越基础，涵盖数据库测试、外部服务交互测试、消息队列测试等热门话题。
- 🔍 **测试策略与工作流** - 包括应编写的测试类型、数据库和基础设施设置、Web 服务器配置等。
- 🛠 **测试解剖** - 组件测试的核心实践，如使用纯 HTTP 客户端、提供真实凭证、断言整个 HTTP 响应对象等。
- 🔗 **集成测试** - 测试与第三方组件的协作，包括使用 HTTP 拦截器隔离组件、模拟网络混乱等。
- 📊 **数据处理** - 测试应用数据和数据库的模式和实践，如每个测试应仅操作自己的记录、使用公共 API 断言新数据状态等。
- 📨 **消息队列测试** - 正确测试从队列开始或结束的流程，包括使用假 MQ、测试消息确认和批量处理等。
- 🤹 **模拟测试** - 区分好的模拟和坏的模拟，避免隐藏模拟，清理所有模拟等。
- 📚 **其他配方** - 包括 Nest.js、Fastify、Mocha 等更多用例和平台的具体示例。

---

## [speculation](https://github.com/orgs/community/discussions/156354)

**原文标题**: [NPM Private Package Installation is broken · community · Discussion #156354 · GitHub](https://github.com/orgs/community/discussions/156354)

**中文标题**: "NPM 私有包安装问题 · 社区 · 讨论 #156354 · GitHub"

GitHub 社区中关于 NPM 私有包安装问题的讨论，问题已通过设置.npmrc 文件解决，官方发布了事件报告确认问题已修复。

- 🔍 用户 xav-ie 报告 NPM 私有包安装失败问题，持续超过 30 分钟，队友也验证了此问题。
- 🛠️ 通过设置.npmrc 文件并包含特定内容解决了问题：`//registry.npmjs.org/:_authToken=${NPM_TOKEN}`。
- 📢 多位用户确认他们的访问令牌被删除，未收到任何通知邮件。
- ⏳ 问题发生在大约 9 小时前，CI 和用户管理账户的令牌也被清除。
- 🔄 用户可以通过重新创建新令牌来解除阻塞，确认此方法有效。
- 📜 官方维护者 ebndev 确认问题已解决，并发布了事件报告。
- 🔗 如果问题持续存在，用户可以在讨论中继续反馈。

---

## [the status update](https://status.npmjs.org/incidents/bndr0gf8nnsq?u=t144d04641jw)

**原文标题**: [npm Status - Issues publishing and installing packages](https://status.npmjs.org/incidents/bndr0gf8nnsq?u=t144d04641jw)

**中文标题**: npm 状态 - 发布和安装包的问题

npm 包发布与安装问题事件已解决，由数据库维护期间的内部 bug 引发，现恢复正常。

- 🔍 事件原因：常规数据库维护时出现内部 bug  
- ✅ 当前状态：问题已解决（2025 年 4 月 11 日 14:51 UTC 更新）  
- ⚠️ 影响范围：包安装和发布功能  
- 🛠️ 处理过程：  
  - 02:46 UTC：开始调查访问令牌问题，建议用户创建新令牌临时解决  
  - 05:37 UTC：确认问题并实施修复  
  - 08:32 UTC：持续修复旧访问令牌恢复功能  
  - 12:52 UTC：监控修复结果  
- 📩 订阅服务：支持邮件/SMS 通知（含全球多国号码选项）

---

## [deploy Next.js apps to Cloudflare Workers](https://blog.cloudflare.com/deploying-nextjs-apps-to-cloudflare-workers-with-the-opennext-adapter/)

**原文标题**: [Deploy your Next.js app to Cloudflare Workers with the Cloudflare adapter for OpenNext](https://blog.cloudflare.com/deploying-nextjs-apps-to-cloudflare-workers-with-the-opennext-adapter/)

**中文标题**: "使用 OpenNext 的 Cloudflare 适配器将 Next.js 应用部署到 Cloudflare Workers"

Cloudflare 推出了 1.0.0-beta 版本的@opennextjs/cloudflare 适配器，用于将 Next.js 应用部署到 Cloudflare Workers，取代了之前的 Next on Pages 方式。该适配器通过与 OpenNext 集成，支持更多 Next.js 功能，并计划在未来版本中进一步优化。

- 🚀 **适配器发布**：@opennextjs/cloudflare 1.0.0-beta 版本发布，支持 Next.js 应用部署到 Cloudflare Workers。  
- 🔧 **功能支持**：支持 Next.js 15 的大部分功能，包括缓存、部分预渲染（PPR）、中间件、App 和 Pages 路由等。  
- 🖼️ **图像优化**：集成 Cloudflare Images，优化图像交付。  
- 🛠️ **未来计划**：计划支持 Windows 开发、Edge 运行时和组合缓存（use cache）。  
- 📦 **生态系统改进**：Workers 的 Node.js 兼容性提升，Worker 大小限制增加。  
- 🚧 **开发与部署**：通过简单命令即可创建、开发和部署 Next.js 应用到 Workers。  
- 📢 **反馈与贡献**：鼓励用户通过 GitHub 和 Discord 提供反馈和贡献代码。  
- 🌐 **Cloudflare 使命**：致力于构建更好的互联网，提供网络安全、加速和零信任解决方案。

---

## ['deploy to Workers' button](https://blog.cloudflare.com/deploy-workers-applications-in-seconds/)

**原文标题**: [Skip the setup: deploy a Workers application in seconds](https://blog.cloudflare.com/deploy-workers-applications-in-seconds/)

**中文标题**: "跳过设置：数秒内部署 Workers 应用"

Cloudflare 推出“一键部署到 Cloudflare”按钮，简化 Workers 应用的部署流程，使开发者能快速分享和部署开源项目。

- 🚀 **一键部署功能**：在 Git 仓库 README 中添加按钮，其他开发者可快速部署项目。
- 🔄 **自动克隆仓库**：Cloudflare 自动克隆并创建新仓库，方便继续开发。
- ⚙️ **自动配置资源**：自动创建所需资源（如 Workers KV、D1 数据库、R2 存储桶）并绑定到 Worker。
- 🔧 **自动 CI/CD 配置**：通过 Workers Builds 实现生产分支的自动构建和部署。
- 🔍 **预览 URL 生成**：非生产分支的更改会生成预览 URL，并在 GitHub 拉取请求中显示。
- 📜 **简化部署流程**：省去传统部署中的复杂步骤（如克隆、安装、配置等），提升开发者体验。
- ☁️ **自托管简化**：与传统云服务相比，Cloudflare 提供无服务器、高可用性、自动扩展等优势，降低运维复杂度。
- 🌐 **应用场景广泛**：适用于从入门项目到全栈应用，包括 API 测试、AI 代理等复杂场景。
- 📌 **示例项目**：如 Fiberplane 的 API 测试工具和远程 MCP 服务器，展示一键部署的实际应用。
- 📚 **文档支持**：提供详细文档，指导如何为项目添加部署按钮并确保成功部署。
- 🛠️ **开发者资源**：新开发者可通过 Cloudflare 仪表板或公共 Git 仓库 URL 快速上手，关注开发者周获取最新功能。

---

## [v1 of their Cloudflare Vite plugin](https://blog.cloudflare.com/introducing-the-cloudflare-vite-plugin/)

**原文标题**: ["Just use Viteââ¦ with the Workers runtime](https://blog.cloudflare.com/introducing-the-cloudflare-vite-plugin/)

**中文标题**: “就用 Vite”…配合 Workers 运行时

Cloudflare 宣布推出 Vite 插件 1.0 版本，并正式支持 React Router v7，使开发者能够在 Cloudflare Workers 运行时环境中直接使用 Vite 进行开发。

- 🚀 **Vite 插件 1.0 发布**：Cloudflare Vite 插件 1.0 正式发布，支持 React Router v7。
- 🔧 **原生 Workers 运行时支持**：通过 Vite 6 的 Environment API，开发者可以在本地开发时使用 Cloudflare Workers 运行时（workerd），确保开发与生产环境行为一致。
- 🤝 **与 Vite 团队合作**：Cloudflare 与 Vite 团队紧密合作，共同设计了 Environment API，使 Vite 能够支持多种自定义运行时环境。
- 🌐 **SPA 开发优化**：Vite 已成为单页应用（SPA）开发的首选工具，支持 React、Vue、Svelte 等前端框架。
- 🛠️ **快速创建项目**：使用`create-cloudflare` CLI 可以快速创建配置了 Cloudflare Vite 插件的新项目。
- 🔄 **现有项目升级**：通过添加`@cloudflare/vite-plugin`依赖和配置`wrangler.jsonc`文件，现有 Vite 项目可以轻松升级以支持 Cloudflare Workers。
- 🔄 **无缝开发体验**：开发时，Vite 会跟踪代码变化并更新 Worker 环境，同时保留客户端状态。
- 📦 **构建与部署**：`vite build`和`vite preview`命令支持构建和预览，`wrangler deploy`可直接部署 Vite 构建的应用。
- 🔗 **React Router v7 支持**：Cloudflare Vite 插件提供对 React Router v7 的一流支持，开发者可以轻松创建、构建和部署 React Router 应用。
- ⚙️ **全栈框架支持**：Cloudflare 计划支持更多全栈框架，并欢迎框架贡献者参与合作。
- 🌍 **Workers 全面支持**：Cloudflare Vite 插件支持所有 Cloudflare 开发者平台功能，包括 KV、D1、Durable Objects 等。
- 📚 **文档与资源**：开发者可以参考 Cloudflare Vite 插件文档，了解更多使用细节。

---

## [deploy an entire frontend, backend, and database](https://javascriptweekly.com/link/167999/web)

**原文标题**: [Error](https://javascriptweekly.com/link/167999/web)

**中文标题**: 错误

无法总结：获取内容时出错 - HTTPSConnectionPool(host='javascriptweekly.com', port=443): Max retries exceeded with url: /link/167999/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

## [The RedwoodJS team has an update](https://community.redwoodjs.com/t/the-future-of-redwood-launches-today/7938)

**原文标题**: [The Future of Redwood Launches Today - Announcements - RedwoodJS Community](https://community.redwoodjs.com/t/the-future-of-redwood-launches-today/7938)

**中文标题**: "红木未来今日启航 - 公告 - RedwoodJS 社区"

RedwoodJS 社区宣布重大变革，创始人 David 转型全职 VC，项目由 Peter 接手并分拆为 Redwood GraphQL 和 Redwood SDK 两条发展路径，未来将聚焦个人软件革命。

- 🚀 David 宣布不再领导 Redwood 项目，转型为全职 VC，但仍愿与社区保持联系。  
- ❤️ 表达对 Redwood 社区和核心团队的感激，强调项目对个人和创业者的深远影响。  
- 🔄 解释项目未达“逃逸速度”的原因，包括 React Server Components（RSC）的技术挑战和团队士气问题。  
- 🛠️ Peter 回归并领导 Redwood，将其发展为独立公司，提出新愿景并推进 Redwood SDK。  
- 📢 宣布 Redwood 未来将分为 Redwood GraphQL 和 Redwood SDK 两条路径，后者旨在推动个人软件革命。  
- 📚 提供新项目文档和 Discord 链接，鼓励社区参与和反馈。  
- 🤝 社区成员对变革反应不一，有人兴奋期待，也有人表达失望和担忧。  
- 💬 David 回应质疑，强调现有用户可继续使用 Redwood，SDK 将是补充而非替代。  
- 🌟 多位社区成员感谢 David 和团队的贡献，并对 Redwood 的未来表示期待。

---

## [p5.js](https://p5js.org/)

**原文标题**: [p5.js](https://p5js.org/)

**中文标题**: "p5.js"

探索 p5.js 库的参考资源与创意社区实践

- 📚 **参考文档** - 提供 p5.js 库的官方学习参考  
- 🎨 **示例学习** - 通过实例掌握 p5.js 编程技巧  
- 🌐 **社区作品** - 展示 p5.js 社区的创意项目  
  - � **Geodata Weaving** - Kaspar Ravel 的地理数据编织艺术  
  - 🦠 **Slime Molds** - Patt Vira 的黏菌模拟视觉  
  - 🌵 **Generative Succulents** - newyellow 的生成式多肉植物  
  - 🔷 **Padrão Geométrico** - Guilherme Vieira 的几何图案设计  
  - 🏺 **Zen Pots** - newyellow 的禅意花盆生成  
  - 📺 **Glitch animation** - Karakure178 的故障风格动画  
- ❤️ **支持项目** - 捐赠以支持 p5.js 发展  
- ⬇️ **下载库** - 获取最新版 p5.js 库文件  

（注：原内容为 p5.js 官网的功能模块与社区作品展示，未包含具体技术细节或项目描述）

---

## [The release notes](https://github.com/processing/p5.js/releases/tag/v2.0.0-beta.2)

**原文标题**: [Release v2.0.0-beta.2 · processing/p5.js · GitHub](https://github.com/processing/p5.js/releases/tag/v2.0.0-beta.2)

**中文标题**: 发布 v2.0.0-beta.2 · processing/p5.js · GitHub

p5.js 2.0.0-beta.2 版本发布，包含多项新功能和改进，主要涉及异步加载、字体支持、WebGL 增强、曲线绘制优化等。

- 🚀 **异步加载** - 2.0 版本引入`async setup`替代`preload`函数，支持异步加载资源。  
- ✏️ **字体支持** - 新增通过 CSS 加载字体（如 Google Fonts），并支持可变字体权重调整。  
- 🎨 **WebGL 增强** - 新增`textToModel`将文本转为 3D 模型，支持自定义着色器属性和简单线条模式。  
- 🔄 **曲线绘制优化** - 重命名`curveVertex`为`splineVertex`，简化闭合曲线绘制，支持多种曲线类型混合。  
- 🌈 **色彩空间扩展** - 新增 RGBHDR、HWB、LAB 等色彩模式，支持广色域显示（需 HDR 屏幕）。  
- 🛠️ **修复与改进** - 修复了像素操作、WebGL 文本对齐、闭合样条等多项问题，并优化了性能。  
- 📦 **发布详情** - 版本号 v2.0.0-beta.2，包含 174 次提交，由多位贡献者共同完成。

---

## [JSHeroes conference](https://jsheroes.io/)

**原文标题**: [JSHeroes 2025 | Community Organized JS Conference](https://jsheroes.io/)

**中文标题**: JSHeroes 2025 | 社区组织的 JS 大会

2025 年 JSHeroes 大会将于 5 月 29 日至 30 日在罗马尼亚克卢日举行，这是一个由社区组织的非营利性活动，旨在汇聚全球 JavaScript 和 Web/前端爱好者，提供高质量内容、精彩社交和丰富乐趣。

- 🎉 **活动概述**：JSHeroes 2025 是第七届年度会议，为期两天，单轨道形式，强调学习、交流和开放精神。
- 🎤 **演讲嘉宾**：包括多位行业专家，涵盖从代码设计、安全、CSS 动画到 AI 和 LLM 等多个前沿话题。
- 📅 **日程安排**：第一天主题包括代码文档、表单验证、技术债务等；第二天聚焦 RPC 复兴、Express 框架、可访问性等。
- 🏛️ **地点**：克卢日的 Grand Hotel Italia，设施齐全，轮椅可通行。
- 💡 **主题**：2025 年主题是“弥合差距”，探讨技术债务、复杂性和新技术的平衡。
- 🤝 **组织团队**：由志愿者团队组织，强调透明度和开源精神，所有活动数据公开。
- 💰 **赞助**：活动得到金、银、铜三级赞助商支持，同时有媒体和活动合作伙伴。
- 🎨 **额外活动**：包括速写艺术、社交活动等，增强与会者互动体验。
- 🌍 **社区影响**：活动不仅关注技术，也注重人文方面，致力于为开发社区提供全面视角。

---

## [TypeSpec 1.0-RC](https://typespec.io/blog/2025-03-31-typespec-1-0-release/)

**原文标题**: [typespec.io](https://typespec.io/blog/2025-03-31-typespec-1-0-release/)

**中文标题**: "typespec.io"

TypeSpec 1.0-RC 发布，这是一个用于描述 API 合约的开源语言和工具，旨在加速 API 开发并简化长期维护。通过简洁易读的格式定义 API，自动生成多种规范、代码骨架和文档，保持 API 同步演进。

- 🚀 **TypeSpec 简介**：微软开源的语言和工具，用于描述 API 合约，支持生成 OpenAPI、JSON Schema、Protocol Buffers 等规范，以及多语言客户端库和服务端代码骨架。  
- 🔄 **API 优先开发**：通过单一源头生成所有必要产物，避免维护多个独立产物导致的同步问题。  
- 🌍 **生态系统**：提供 GitHub Issues、Discord 社区、文档等多渠道支持，欢迎社区贡献和反馈。  
- 🏢 **用户案例**：微软 Learn 团队和伦敦证券交易所等已采用 TypeSpec，简化 API 设计流程并提升协作效率。  
- 📦 **1.0-RC 内容**：包括稳定的编译器、核心库、IDE 支持和 OpenAPI/JSON Schema 生成器，以及预览功能如 Protocol Buffers 和多语言代码生成。  
- ⚠️ **预览功能限制**：代码生成目前支持有限的认证机制和 HTTP 功能，文档仍在完善中。  
- 🔧 **自定义生成器**：实验性框架支持创建自定义生成器，满足特定需求。  
- 📚 **快速入门**：提供安装指南、快速入门教程和社区支持，鼓励用户试用并反馈。  
- 📢 **反馈征集**：特别关注预览功能的用户体验，欢迎通过 GitHub 提交问题和建议。  
- 🙏 **致谢**：感谢社区成员的贡献，共同推动 TypeSpec 发展。

---

## [pnpm 10.8](https://github.com/pnpm/pnpm/releases/tag/v10.8.0)

**原文标题**: [Release pnpm 10.8 · pnpm/pnpm · GitHub](https://github.com/pnpm/pnpm/releases/tag/v10.8.0)

**中文标题**: 发布 pnpm 10.8 · pnpm/pnpm · GitHub

pnpm 10.8 版本发布，引入了新的实验性功能并修复了一些问题。

- 🆕 **实验性功能**：支持通过`.pnpmfile.cjs`中的`updateConfig`钩子更新配置设置。  
- ⚙️ **新命令**：`pnpm add`现在支持`--config`标志来安装新的配置依赖。  
- 🐛 **修复问题**：修复了`pnpm-workspace.yaml`中以`!/`开头的 glob 导致无限挂起的问题。  
- 🔄 **改进功能**：`pnpm audit --fix`和`pnpm link`现在会更新`pnpm-workspace.yaml`中的覆盖配置。  
- 📦 **发布信息**：版本 v10.8.0 由 zkochan 于 4 月 7 日发布，包含 2 次提交。  
- ❤️ **社区反应**：获得了 14 个❤️、2 个🚀和 1 个🎉的反应。

---

## [Prisma 6.6](https://www.prisma.io/blog/prisma-orm-6-6-0-esm-support-d1-migrations-and-prisma-mcp-server)

**原文标题**: [Prisma ORM 6.6.0: ESM Support, D1 Migrations & Prisma MCP Server](https://www.prisma.io/blog/prisma-orm-6-6-0-esm-support-d1-migrations-and-prisma-mcp-server)

**中文标题**: "Prisma ORM 6.6.0：ESM 支持、D1 迁移与 Prisma MCP 服务器"

Prisma ORM v6.6.0 发布，带来多项新功能，包括 ESM 支持、D1 和 Turso 迁移支持、MCP 服务器等，旨在提升开发体验和灵活性。

- 🚀 **Prisma ORM v6.6.0 发布**：包含 ESM 支持、Cloudflare D1 和 Turso 迁移支持、MCP 服务器等新功能。  
- 🔄 **ESM 支持（早期访问）**：新的`prisma-client`生成器支持 ESM 和 CommonJS，提供更灵活的项目配置。  
- 📂 **更灵活的生成器**：生成器不再将文件输出到`node_modules`，而是输出到指定路径，支持更多自定义选项。  
- 🤖 **MCP 服务器（预览版）**：允许通过 AI 工具管理 Prisma Postgres 数据库，支持创建实例、设计数据模型等操作。  
- ☁️ **Cloudflare D1 & Turso 迁移支持（早期访问）**：新增`prisma db push`、`prisma db pull`等命令，支持远程数据库模式变更。  
- 🛠️ **`prisma init`新增`--prompt`选项**：可快速生成 Prisma 模式并部署到 Prisma Postgres 实例。  
- 📅 **未来计划**：包括拆分生成文件、优化编辑器性能、移除 Accelerate 扩展需求等。  
- 📢 **反馈渠道**：开发者可通过 X 和 Discord 分享反馈，或查看 3 个月路线图了解未来更新。

---

## [React Native 0.79](https://reactnative.dev/blog/2025/04/08/react-native-0.79)

**原文标题**: [React Native 0.79 - Faster tooling and much more · React Native](https://reactnative.dev/blog/2025/04/08/react-native-0.79)

**中文标题**: "React Native 0.79 - 更快的工具链及其他改进 · React Native"

React Native 0.79 版本带来了多项性能改进和新功能，包括更快的工具链、Android 启动优化、iOS 原生模块注册改进等，同时移除了一些旧特性。

- 🚀 **Metro 工具链提速**：Metro 0.82 通过延迟哈希技术，使 `yarn start` 启动速度提升 3 倍以上，并稳定支持 `package.json` 的 `exports` 和 `imports` 字段解析。  
- 📦 **JSC 迁移至社区包**：JavaScriptCore (JSC) 引擎移至 `@react-native-community/javascriptcore`，未来将从 React Native 核心中移除，Hermes 用户不受影响。  
- 🍏 **iOS Swift 兼容的原生模块注册**：新增 `modulesProvider` 字段简化原生模块注册，支持纯 C++ 模块和 Swift `AppDelegate`。  
- ⚡ **Android 启动加速**：默认不再压缩 JS Bundle，减少启动时间（如 Discord TTI 提升 12%），可通过 `enableBundleCompression` 配置。  
- 🔧 **移除远程 JS 调试**：弃用 Chrome 远程调试，推荐使用 React Native DevTools 或 Expo DevTools 插件。  
- ♻️ **内部模块改用 `export` 语法**：约 46 个 API 更新为 ES 模块语法，建议从根路径导入（如 `import {ImageBackground} from 'react-native'`）。  
- ⚠️ **其他破坏性变更**：包括不支持无单位的阴影/滤镜值、修正 `hwb()` 语法、更新 `ExceptionsManager` 导出方式等。  
- 🙏 **致谢**：感谢 100 位贡献者的 944 次提交，特别提及 Marc Rousavy、Kudo Chien 等社区成员的关键贡献。  
- 🔄 **升级指南**：推荐使用 React Native Upgrade Helper 或通过 CLI 创建新项目（`npx @react-native-community/cli init`），Expo SDK 53 将默认支持此版本。

---

## [Bun 1.2.9](https://bun.sh/blog/bun-v1.2.9)

**原文标题**: [Bun v1.2.9 | Bun Blog](https://bun.sh/blog/bun-v1.2.9)

**中文标题**: "Bun v1.2.9 | Bun 博客"

Bun 1.2.9 版本发布，修复了 48 个错误（116 个👍），新增多项功能与优化。

- 🐛 **Bug 修复**：修复了 48 个问题，包括`node:http`、`AsyncLocalStorage`和`node:crypto`的回归问题。
- 🚀 **Bun.redis**：内置 Redis 客户端，性能比 ioredis 快 44.82%-85.39%。
- 📦 **Bun.S3Client**：新增`ListObjectsV2`支持，可列出 S3 存储桶中的对象。
- 🔧 **libuv 支持**：新增多个 libuv 互斥锁和计时函数，支持原生模块。
- 📂 **require.extensions**：完全支持`require.extensions`，提升与 Node.js 模块的兼容性。
- 🛠️ **性能优化**：优化了`Number.isFinite()`、数组方法及 NaN 处理，性能提升显著。
- 🔄 **WebKit 升级**：包含 WebKit 的更新。
- 🔌 **Fastify 修复**：修复了 Fastify WebSocket 注册问题。
- 🖥️ **Windows 网络共享修复**：修复了查询网络共享返回错误的问题。
- 📜 **Bun.spawn**：新增`maxBuffer`选项，限制子进程输出。
- 🔗 **符号链接支持**：新增`--preserve-symlinks`选项，支持保留符号链接。
- 🌐 **node:net.Server**：修复了`address()`方法在 localhost 上的返回结果。
- 🧹 **垃圾回收修复**：修复了`node:fs`中输入缓冲区过早回收的问题。
- 🙏 **贡献者**：感谢 13 位贡献者的贡献。

---

## [Tailwind CSS 4.1](https://tailwindcss.com/blog/tailwindcss-v4-1)

**原文标题**: [Tailwind CSS v4.1: Text shadows, masks, and tons more - Tailwind CSS](https://tailwindcss.com/blog/tailwindcss-v4-1)

**中文标题**: "Tailwind CSS v4.1：文字阴影、遮罩及更多新功能 - Tailwind CSS"

Tailwind CSS v4.1 版本发布，新增多项实用功能和改进，包括文本阴影、遮罩元素、浏览器兼容性优化等，提升开发体验和设计灵活性。

- 🌟 新增 `text-shadow-*` 工具类，支持文本阴影效果，包含五种预设尺寸和颜色调整功能。
- 🎭 引入 `mask-*` 工具类，支持使用图片和渐变遮罩元素，提供更灵活的遮罩 API。
- 🌐 改进对旧版浏览器的兼容性，优化颜色、阴影等功能的降级表现。
- 📏 新增 `overflow-wrap` 工具类，支持精细控制文本换行，防止长单词破坏布局。
- 🎨 支持彩色 `drop-shadow`，可为阴影添加颜色和透明度。
- 🖱️ 新增 `pointer-*` 和 `any-pointer-*` 变体，针对不同输入设备优化设计。
- 🔍 新增 `items-baseline-last` 工具类，支持将元素对齐到文本最后一行的基线。
- 🛡️ 引入 `safe` 对齐工具类，防止内容在容器过小时溢出。
- 🚫 新增 `@source not` 功能，支持忽略特定路径以加快构建速度。
- 📌 新增 `@source inline(…)` 功能，支持强制生成特定工具类。
- 🔄 新增多种变体，包括 `noscript`、`user-valid`、`inverted-colors` 等，扩展设计可能性。
- 📦 提供多种安装方式，支持通过 CLI、Vite 和 PostCSS 升级到最新版本。

---

## [CKEditor5 45](https://github.com/ckeditor/ckeditor5/releases/tag/v45.0.0)

**原文标题**: [Release v45.0.0 · ckeditor/ckeditor5 · GitHub](https://github.com/ckeditor/ckeditor5/releases/tag/v45.0.0)

**中文标题**: "发布 v45.0.0 · ckeditor/ckeditor5 · GitHub"

CKEditor 5 v45.0.0 版本发布，带来多项新功能和改进，包括邮件编辑增强、全屏模式和链接体验优化等。此外，还包含多项重大变更、错误修复和其他改进。

- 📧 **邮件编辑增强**：新增导出内联样式和邮件配置助手功能，改进邮件兼容性和布局表格支持。  
- 🖥️ **全屏模式**：新增经典和解耦编辑器的全屏编辑功能，提升写作体验。  
- 🔗 **链接体验优化**：重新设计链接用户界面，支持文档内书签链接和预定义链接列表。  
- 🛠️ **安装方法改进**：新增图标替换功能，支持通过包覆盖机制自定义图标。  
- ⚠️ **弃用旧安装方法**：预定义构建包已弃用，计划在 2025 年底前逐步淘汰自定义构建和 DLL 构建。  
- 🐞 **错误修复**：修复了多个问题，包括表格行为、HTML 支持和复杂邮件结构的处理。  
- 📦 **新包发布**：新增 `@ckeditor/ckeditor5-email`、`@ckeditor/ckeditor5-export-inline-styles` 等包。  
- 🔄 **重大变更**：涉及书签、链接和表格功能的重大变更，需特别注意更新指南。  
- 🌍 **多语言支持**：新增白俄罗斯语翻译支持。  
- ⬆️ **技术升级**：最低 Node.js 版本要求升级至 20.0.0，TypeScript 目标更新为 `es2022`。

---

## [Zod 4 Beta](https://v4.zod.dev/v4)

**原文标题**: [Introducing Zod 4 beta | Zod Docs](https://v4.zod.dev/v4)

**中文标题**: "Zod 4 测试版发布 | Zod 文档"

Zod 4 beta 版本发布，带来性能提升、新功能和架构改进。

- 🚀 **性能提升**：Zod 4 解析速度显著提升，字符串解析快 2.6 倍，数组解析快 3 倍，对象解析快 7 倍。
- 📦 **更小的体积**：核心包体积减少 57%，引入 `@zod/mini` 进一步减少 85% 体积。
- ⚡ **TypeScript 优化**：类型实例化减少 20 倍，解决泛型爆炸问题。
- 🆕 **新功能**：
  - 元数据支持 (`z.registry` 和 `z.meta`)
  - JSON Schema 转换 (`z.toJSONSchema`)
  - 新的 `z.interface()` API，支持精确可选属性和递归类型
  - 文件验证 (`z.file()`)
  - 国际化支持 (`z.config`)
  - 错误美化 (`z.prettifyError`)
  - 模板字面量类型 (`z.templateLiteral`)
  - 数字和布尔值格式增强
- 🔄 **简化错误定制**：统一 `error` 参数，取代多个旧 API。
- 🧩 **可扩展基础**：引入 `@zod/core` 作为共享核心，支持构建其他库。
- 📅 **Beta 测试**：预计持续 4-6 周，鼓励用户升级并提供反馈。

---

## [Comparing Tauri and Electron for Building Desktop Apps](https://gethopp.app/blog/tauri-vs-electron)

**原文标题**: [Tauri vs. Electron: performance, bundle size, and the real trade-offs](https://gethopp.app/blog/tauri-vs-electron)

**中文标题**: "Tauri 与 Electron 对比：性能、打包体积及实际权衡"

概述总结  
Tauri 和 Electron 是两种流行的跨平台应用开发框架，各有优缺点。Tauri 基于 Rust，使用系统原生 WebView，应用体积小且内存占用低；Electron 基于 Node.js 和 Chromium，功能成熟但资源消耗较大。Hopp 最终选择 Tauri，因其性能、轻量化和对 Rust 的支持更符合项目需求。  

- 🏗️ **架构差异**  
  - Electron：主进程为 Node.js，渲染进程为 Chromium 实例，需打包 Node.js 运行时。  
  - Tauri：主进程为 Rust 原生二进制，渲染进程使用系统 WebView（如 WebView2/WKWebView），无需额外运行时。  

- ⚖️ **性能对比**  
  - **内存占用**：Tauri（172MB）显著低于 Electron（409MB）。  
  - **应用体积**：Tauri（8.6MiB）远小于 Electron（244MiB）。  
  - **启动时间**：两者差异微小，可忽略。  

- 🛠️ **开发体验**  
  - Electron：基于 JavaScript，生态成熟，构建速度快。  
  - Tauri：需学习 Rust，初始构建慢（Rust 编译），但后续优化明显。  

- 🌐 **跨平台一致性**  
  - Tauri 依赖系统 WebView，可能面临浏览器引擎差异（如 Safari/Chrome 兼容性问题）。  
  - Electron 统一使用 Chromium，UI 一致性更好。  

- 🚀 **Hopp 选择 Tauri 的原因**  
  - **后端性能**：Rust 适合低延迟 WebRTC 视频流处理。  
  - **Sidecar 支持**：简化独立进程（如屏幕流）的生命周期管理。  
  - **功能迭代**：Tauri v2 提供了更新器等关键功能，符合项目需求。  

- 🔍 **结论**  
  - 无绝对优劣，需根据项目需求（性能、体积、团队技术栈）选择。  
  - Tauri 适合轻量化、高性能场景；Electron 适合快速开发且需要成熟生态的项目。

---

## [Electron](https://www.electronjs.org/)

**原文标题**: [Build cross-platform desktop apps with JavaScript, HTML, and CSS | Electron](https://www.electronjs.org/)

**中文标题**: "使用 JavaScript、HTML 和 CSS 构建跨平台桌面应用 | Electron"

Electron 是一个开源框架，允许开发者使用网页技术构建跨平台桌面应用，支持自动更新、原生界面交互和多种分发渠道，并集成了丰富的开发工具和第三方库。

- 🖥️ Electron 结合 Chromium 和 Node.js，让网页开发者能创建桌面应用  
- 🌍 跨平台兼容 macOS、Windows 和 Linux  
- 🔓 开源项目，由 OpenJS Foundation 和活跃社区维护  
- 🏆 被众多知名应用（如 VS Code、Slack、Figma）采用  
- 🛠️ 简化桌面开发，自动处理底层复杂部分  
- 🎨 支持原生 GUI 交互（窗口、菜单、通知等）  
- 🔄 通过 autoUpdater 模块实现自动软件更新  
- 📦 提供平台专属安装包生成工具（如 .dmg、.msi）  
- 🏬 支持主流应用商店分发（Mac App Store、Microsoft Store 等）  
- ⚠️ 内置崩溃报告功能（crashReporter 模块）  
- 🧩 可自由集成前端生态工具（React、Vue.js、TypeScript 等）  
- 🚀 提供 Electron Forge 工具链，简化应用构建和发布  
- ⚡ 支持直接通过 npm 安装稳定版/实验版  
- 🎛️ 提供 Electron Fiddle 工具快速实验 API  
- ❤️ 被 1Password、Discord、Notion 等数千款应用使用

---

## [Neutralinojs](https://neutralino.js.org/)

**原文标题**: [Build lightweight cross-platform desktop apps with JavaScript, HTML, and CSS | Neutralinojs](https://neutralino.js.org/)

**中文标题**: "使用 JavaScript、HTML 和 CSS 构建轻量级跨平台桌面应用 | Neutralinojs"

Neutralinojs 是一个轻量级、跨平台的应用程序开发框架，提供原生 API 支持、零依赖和灵活的开发选项。

- 🖥️ Neutralinojs 提供 JavaScript API，支持操作系统级功能（如文件操作、命令执行和原生对话框）。  
- 📦 零依赖且便携，无需额外依赖或编译器即可跨平台开发应用。  
- 🌍 支持 Linux、Windows、macOS、Web 和 Chrome，单一应用兼容多平台。  
- ⚡ 轻量高效，未压缩应用仅约 2MB，压缩后约 0.5MB，资源占用低。  
- 🛠️ 提供简单灵活的接口，避免复杂设置，支持便携式自动更新和 CLI。  
- 🔄 兼容任何前后端框架，支持 HMR 等特性，并可通过扩展 IPC 对接其他后端语言。

---

## [Tauri.](https://v2.tauri.app/)

**原文标题**: [Tauri 2.0 | Tauri](https://v2.tauri.app/)

**中文标题**: "Tauri 2.0 | Tauri"

Tauri 2.0 是一个用于创建小型、快速、安全且跨平台应用程序的工具，支持多种前端框架和操作系统，强调安全性和性能。

- 🚀 **快速开始**：提供多种安装方式（Bash、PowerShell、npm、Yarn 等）来创建 Tauri 项目。  
- 🔄 **前端独立**：支持任何前端框架，无需更改现有技术栈。  
- 🌍 **跨平台**：支持 Linux、macOS、Windows、Android 和 iOS，单一代码库即可构建多平台应用。  
- 📡 **进程间通信**：前端使用 JavaScript，应用逻辑使用 Rust，并可集成 Swift 和 Kotlin 进行深度系统集成。  
- 🔒 **高安全性**：安全性是 Tauri 团队的核心优先事项。  
- 📦 **极小体积**：利用操作系统原生 Web 渲染器，应用体积可小至 600KB。  
- 🦀 **基于 Rust**：以性能和安全性为核心，Rust 是下一代应用的理想语言。  
- © **版权信息**：2025 年 Tauri 贡献者，采用 CC-BY/MIT 许可。

---

## [Mastering Default Values with Nullish Coalescing (??)](https://allthingssmitty.com/2025/04/10/mastering-default-values-in-javascript-with-the-nullish-coalescing-operator/)

**原文标题**: [
    Mastering default values in JavaScript with the nullish coalescing (??) operator - Matt Smith
  ](https://allthingssmitty.com/2025/04/10/mastering-default-values-in-javascript-with-the-nullish-coalescing-operator/)

**中文标题**: "掌握 JavaScript 中的默认值：空值合并操作符 (??) 的使用 - Matt Smith"

JavaScript 中利用空值合并运算符（??）掌握默认值设置  

- 🎯 空值合并运算符（??）比传统的逻辑或（||）运算符更有效地处理默认值  
- 🔍 `||` 会将 `false`、`0`、`NaN`、`""`、`null` 和 `undefined` 视为假值，可能覆盖有效值（如 `0` 或空字符串）  
- ✅ `??` 仅当左侧为 `null` 或 `undefined` 时返回右侧默认值，保留其他假值（如 `0` 或 `false`）  
- 📊 示例对比：  
  - `0 || 5` 返回 `5`（因 `0` 被 `||` 视为假值）  
  - `0 ?? 5` 返回 `0`（因 `??` 不视 `0` 为无效）  
- ⚡ 使用 `??` 可避免意外覆盖，确保代码在处理数字或空字符串时更精准可靠  
- 👍 推荐场景：需保留明确假值（如 `0`/`false`），同时为 `null`/`undefined` 提供默认值

---

## [How Clerk Integrates with a Next.js Application Using Supabase](https://clerk.com/blog/how-clerk-integrates-nextjs-supabase?utm_source=cooper-press&utm_medium=newsletter&utm_campaign=supabase-nextjs&utm_content=04-11-25&dub_id=ka3gb8fzr5lr009d)

**原文标题**: [How Clerk integrates with a Next.js application using Supabase](https://clerk.com/blog/how-clerk-integrates-nextjs-supabase?utm_source=cooper-press&utm_medium=newsletter&utm_campaign=supabase-nextjs&utm_content=04-11-25&dub_id=ka3gb8fzr5lr009d)

**中文标题**: "Clerk 如何通过 Supabase 与 Next.js 应用集成"

本文介绍了如何在 Next.js 应用中集成 Supabase 和 Clerk，以提高安全性并减少开发时间。Supabase 允许客户端直接访问数据库，而无需通过后端代码，同时通过 Postgres 的行级安全（RLS）功能保护数据。Clerk 作为身份验证提供者，通过 JWKS 端点验证 JWT 令牌，确保与 Supabase 的安全集成。文章还通过一个实际应用 Quillmate 的示例，展示了如何配置和使用这些技术。

- 🚀 Supabase 允许客户端直接访问数据库，无需传统后端代码，同时通过 RLS 确保数据安全。
- 🔐 Clerk 通过 JWKS 端点验证 JWT 令牌，确保与 Supabase 的安全集成。
- 🔧 在 Supabase 中配置 Clerk 作为第三方身份验证提供者，确保 JWT 令牌包含正确的角色声明。
- 📝 使用 Clerk 的`getToken`函数获取 JWT 令牌，并在 Supabase 客户端中设置`accessToken`选项。
- 🛡️ 通过 RLS 策略，使用 Clerk 用户 ID 限制数据库访问，确保用户只能访问自己的数据。
- 📚 通过 Quillmate 示例展示了如何在实际应用中实现这些技术。

---

## [Accelerating Large-Scale Test Migration with LLMs](https://medium.com/airbnb-engineering/accelerating-large-scale-test-migration-with-llms-9565c208023b)

**原文标题**: [Accelerating Large-Scale Test Migration with LLMs | by Charles Covey-Brandt | The Airbnb Tech Blog | Mar, 2025 | Medium](https://medium.com/airbnb-engineering/accelerating-large-scale-test-migration-with-llms-9565c208023b)

**中文标题**: "利用 LLM 加速大规模测试迁移 | Charles Covey-Brandt | Airbnb 技术博客 | 2025 年 3 月 | Medium"

Airbnb 利用大型语言模型（LLM）在 6 周内完成了 3500 个 React 组件测试文件从 Enzyme 到 React Testing Library（RTL）的大规模迁移，远超手动预计的 1.5 年时间。  

- 🚀 **项目背景**：2020 年 Airbnb 开始采用 RTL 替代 Enzyme，但由于两者差异大，需自动化重构以保留测试意图和代码覆盖率。  
- 🤖 **技术方案**：通过 LLM 驱动的迁移管道，将迁移分解为并行化步骤，加入可配置的重试循环和动态提示。  
- 🔄 **重试机制**：通过多次重试和动态提示，成功迁移中低复杂度文件，大部分在 10 次尝试内完成。  
- 📚 **丰富上下文**：为复杂文件提供多达 10 万 token 的提示，包含相关文件、示例和迁移指南，显著提升成功率。  
- 📊 **系统优化**：通过“采样、调整、扫描”循环，4 天内将成功率从 75% 提升至 97%，剩余 3% 手动完成。  
- 💰 **成果显著**：总成本（包括 API 使用和 6 周工程时间）远低于手动迁移预估，同时保持了测试覆盖率和意图。  
- 🔮 **未来计划**：扩展 LLM 在代码转换中的应用，开发更复杂的迁移工具，提升开发者效率。

---

## [React Reconciliation: The Hidden Engine Behind Your Components](https://cekrem.github.io/posts/react-reconciliation-deep-dive/)

**原文标题**: [React Reconciliation: The Hidden Engine Behind Your Components · cekrem.github.io
](https://cekrem.github.io/posts/react-reconciliation-deep-dive/)

**中文标题**: "React 协调机制：组件背后的隐形引擎 · cekrem.github.io"

React 协调机制是 React 更新 DOM 以匹配组件树的核心算法，它使得声明式编程成为可能。理解这一机制有助于优化性能并设计更高效的组件结构。

- 🔄 **协调机制概述**：React 通过比较新旧元素树来确定如何高效更新 DOM，而非直接操作虚拟 DOM。
- 🧩 **组件标识与状态保留**：相同类型和位置的元素会保留状态，即使属性不同；不同类型则会导致重新挂载。
- 🌳 **元素树结构**：JSX 被转换为轻量级的 JavaScript 对象树，DOM 元素的类型是字符串，自定义组件的类型是函数引用。
- 🔍 **协调原则**：
  - **类型决定标识**：元素类型变化会触发子树重建。
  - **树中位置重要**：相同位置的相同类型组件仅更新属性，不同类型则替换。
  - **键覆盖位置比较**：`key` 属性可以显式控制组件标识，用于列表或状态保留。
- 🗝️ **键的妙用**：
  - 列表中使用 `key` 避免全量重新渲染。
  - 非列表场景中，`key` 可跨条件分支保留状态（如切换标签页时保持表单输入）。
- 🏗️ **组件设计与性能**：
  - 避免内联组件定义（导致函数引用变化）。
  - 使用组合模式隔离状态变化（如 `CounterButton` 独立于 `ExpensiveComponent`）。
  - 状态共置（State Colocation）：将状态限制在最小范围组件内，减少无关渲染。
- 🛠️ **优化实践**：
  - 拆分混合职责的组件（如分离商品配置与评论模块）。
  - 遵循单一职责、依赖倒置等清洁架构原则。
  - 优先通过结构调整而非 `React.memo` 强制优化。
- 📌 **调试建议**：从元素树和组件标识角度分析渲染问题，善用键控制更新行为。

---

## [Hiding Elements That Require JavaScript Without Using JavaScript](https://0xda.de/blog/2025/04/hiding-elements-that-require-javascript-without-javascript/)

**原文标题**: [
        
            Hiding elements that require JavaScript without JavaScript :: dade
        
    ](https://0xda.de/blog/2025/04/hiding-elements-that-require-javascript-without-javascript/)

**中文标题**: "无需 JavaScript 隐藏依赖 JavaScript 的元素 :: dade"

这篇文章讨论了如何在不使用 JavaScript 的情况下隐藏需要 JavaScript 的元素，并提供了几种解决方案。

- 🛠️ **问题背景**：网站需要在 JavaScript 禁用时隐藏依赖 JS 的元素，避免显示不完整的功能。
- 🔍 **初始方案**：通过 JavaScript 在`<html>`标签添加`js-enabled`类，但需要为每个元素编写双重 CSS 规则，显得繁琐。
- 📌 **改进方案**：利用`<noscript>`标签内联 CSS，直接隐藏特定元素（如`.theme-toggle`），但需手动维护列表。
- ⭐ **最佳方案**：创建通用类`d-js-required`，结合`<noscript>`统一隐藏所有依赖 JS 的元素，简化代码和维护。
- 🌟 **效果**：无需额外 JS，仅需单行 CSS 即可实现元素的条件显示，提升渐进增强的灵活性。  
- 🔗 **示例**：分享按钮的 SVG（JS 启用时显示）与纯链接（JS 禁用时显示）的实践案例。  

文章最后鼓励开发者探索渐进增强的创意解决方案，并附上页面分享功能（JS 启用可点击，禁用可复制链接）。

---

## [Debugging JavaScript Memory Leaks in Bun](https://bun.sh/blog/debugging-memory-leaks)

**原文标题**: [Debugging JavaScript Memory Leaks | Bun Blog](https://bun.sh/blog/debugging-memory-leaks)

**中文标题**: "调试 JavaScript 内存泄漏 | Bun 博客"

Bun 实现了 V8 堆快照 API，Chrome DevTools 支持比较堆快照以检测内存泄漏。内存泄漏的关键特征是内存使用量持续增长而不下降。文章提供了检测和减少内存使用的技巧，并列举了常见的内存泄漏来源。

- 🐞 内存泄漏的特征是内存使用量持续增长而不下降，即使工作负载保持不变。
- 📊 高内存使用量指应用消耗大量内存但在运行期间保持稳定。
- 📸 Bun 实现了 V8 的堆快照 API，可以生成.heapsnapshot 文件供 Chrome DevTools 分析。
- 🔍 Chrome DevTools 支持比较多个堆快照，帮助识别内存泄漏。
- 💾 示例代码展示了如何在 Express 应用中故意制造内存泄漏。
- 📈 使用 process.memoryUsage.rss() 测量内存使用量，RSS 是实际分配在 RAM 中的内存量。
- 🛠️ 减少内存使用的技巧：使用 Blob 替代流处理不可变数据，避免不必要的流操作，及时清空不再需要的引用。
- 🔄 常见内存泄漏来源：闭包保留大对象、未清理的 AbortSignal 和 AbortController、Function.prototype.bind() 保留对象、未移除的 EventEmitter 监听器。

---

## [Using Chrome's (Preview) Prompt API for Data Summarization](https://www.raymondcamden.com/2025/04/10/using-chromes-preview-prompt-api-for-data-summarization)

**原文标题**: [Using Chrome's (Preview) Prompt API for Data Summarization](https://www.raymondcamden.com/2025/04/10/using-chromes-preview-prompt-api-for-data-summarization)

**中文标题**: "利用 Chrome（预览版）Prompt API 实现数据摘要"

概述：作者介绍了使用 Chrome 的 Prompt API 进行数据摘要的演示，尽管 API 尚未正式发布且可能变动，但仍展示了其潜力。作者通过 Pirate Weather API 获取天气预报数据，并利用 Prompt API 生成简洁的天气摘要。

- 🚀 作者正在寻找开发者关系和倡导方面的职位，并提供了联系方式。  
- 🛠️ 尽管 Chrome 的 AI 功能 API 尚未稳定，作者仍分享了一个基于 Prompt API 的演示。  
- 📚 Prompt API 是一个通用问答工具，基于较小的 Gemini Nano 模型，适用于多种场景。  
- 🌦️ 演示使用 Pirate Weather API 获取天气预报数据，并提取关键信息（如高低温和天气概况）。  
- 🤖 通过 Prompt API 将原始数据转换为简洁的一周天气预报摘要。  
- ⚠️ 目前该功能需要注册才能使用，且代码示例较为简单。  
- 💡 作者鼓励读者测试并提供反馈，同时提供了支持其内容的途径。

---

## [How to Easily Reproduce a Flaky Test in Playwright](https://www.charpeni.com/blog/how-to-easily-reproduce-a-flaky-test-in-playwright)

**原文标题**: [How to Easily Reproduce a Flaky Test in Playwright | Nicolas Charpentier](https://www.charpeni.com/blog/how-to-easily-reproduce-a-flaky-test-in-playwright)

**中文标题**: "如何在 Playwright 中轻松复现不稳定的测试 | Nicolas Charpentier"

概述：本文介绍了如何利用 Playwright 工具复现不稳定的测试（flaky tests），并提供了一系列调试技巧，包括 CPU 节流、禁用重试、重复测试、压力测试等，帮助开发者更高效地定位和修复问题。

- 🚨 **问题背景**：本地测试通过但 CI 或他人机器上失败的 flaky tests，常与机器性能差异（如超时）相关。  
- 🔍 **复现方法**：通过 Playwright 的`CDPSession`模拟 CI 环境性能，使用`Emulation.setCPUThrottlingRate`节流 CPU（如 M1 Pro 设为 4-6 倍）。  
- ⚠️ **注意事项**：节流代码仅限本地调试，切勿提交到版本库。  
- 🔧 **调试技巧**：  
  - 🔄 **禁用重试**：`--retries 0`避免掩盖问题，或使用`--fail-on-flaky-tests`直接标记不稳定测试。  
  - 🔁 **重复测试**：`--repeat-each 10`多次运行以暴露偶发问题。  
  - 💻 **压力测试**：`--workers 10`增加并行 worker 数模拟高负载。  
  - ⏹️ **快速终止**：`-x`在首次失败时停止测试，节省时间。  
- 🛠️ **组合命令**：结合所有参数（如`--fail-on-flaky-tests --repeat-each 10 --workers 10 -x`）全面检测。  
- 💡 **额外提示**：测试完成时通过终端声音通知提醒开发者。

---

## [Securing a Vue App with OpenID Connect and the BFF Pattern](https://blog.duendesoftware.com/posts/20250409-secure-vue-app-with-openid-connect-bff-pattern/)

**原文标题**: [Secure a Vue app with OpenID Connect and the BFF pattern | Duende Software Blog](https://blog.duendesoftware.com/posts/20250409-secure-vue-app-with-openid-connect-bff-pattern/)

**中文标题**: "使用 OpenID Connect 和 BFF 模式保护 Vue 应用 | Duende Software 博客"

概述：本文介绍了如何使用 OpenID Connect 和 BFF（Backend for Frontend）模式来保护 Vue 应用程序的安全，详细讲解了 BFF 的基本架构、各组件职责以及前后端如何安全通信。

- 🛡️ 单页应用（SPA）如 Vue、React 等在用户体验创建中占主导地位，但安全选项有限。  
- 🔐 Duende 推荐使用 BFF 模式来维护高安全态势，保护用户和数据免受恶意攻击。  
- 🏗️ BFF 架构包括前端、后端和 BFF 代理，确保通信可信和安全。  
- 🔑 OAuth 2.x 和 OpenID Connect 是与此架构配套的安全标准。  
- ⚠️ 浏览器本地存储访问令牌存在安全风险，可能被恶意 JavaScript 利用。  
- 🛠️ BFF 代理作为可信中介，负责服务器端会话管理、用户认证、令牌管理等安全职责。  
- 🍪 使用 HTTPS 和基于 cookie 的会话进行前后端通信，增强安全性。  
- 📦 在 ASP.NET Core 中，通过 NuGet 包轻松集成 BFF 功能。  
- 🔄 前端通过 BFF 管理端点进行登录、注销和会话检查，简化安全操作。  
- 📡 安全调用 API 只需使用 fetch 并依赖 cookie 认证，无需复杂配置。  
- 🔒 后端使用 ASP.NET Core 的 JWT 认证和授权策略保护 API 端点。  
- 📚 更多 BFF 模式的详细信息和示例可参考 Duende 的官方文档。

---

## [The Case for Web Components with Lit](https://typescript.guru/the-case-for-web-components-with-lit/)

**原文标题**: [The Case for Web Components with Lit](https://typescript.guru/the-case-for-web-components-with-lit/)

**中文标题**: "使用 Lit 构建 Web 组件的理由"

Web Components 结合 Lit 提供了一种强大且面向未来的构建 UI 组件的方法。通过 TypeScript 集成，您可以在创建可重用元素的同时获得类型安全的所有好处，这些元素可以在任何地方工作。

- 🌐 **原生浏览器支持**：Web Components 利用内置的浏览器标准（自定义元素、Shadow DOM 和 HTML 模板），无需额外的库或框架即可渲染自定义元素。
- 🏝️ **强封装性**：Shadow DOM 确保每个组件的样式和 DOM 结构与其他部分隔离，避免样式冲突和布局问题。
- 🔄 **框架无关**：Web Components 符合浏览器 API，可以在 React、Angular 或纯 HTML 页面中使用，无需特殊包装器。
- 📈 **可扩展性和可维护性**：每个 UI 部分都被封装，便于大型项目的扩展和维护。
- ⚡ **Lit 的优势**：Lit 是一个轻量级库，简化了 Web Components 的构建，提供响应式属性、声明式模板、快速更新和 TypeScript 支持。
- 🛠️ **TypeScript 与 Lit 的完美结合**：Lit 的简洁性与 TypeScript 的静态类型相结合，提供类型安全属性、接口驱动开发和增强的 IDE 支持。
- 📦 **组件组合与插槽**：Lit 的强大功能之一是使用插槽组合组件，允许创建带有占位符的组件模板。
- 🔄 **状态管理与响应式控制器**：Lit 2.0 引入了响应式控制器，用于提取和重用状态逻辑。
- 🧪 **测试 Web Components**：Lit 组件易于测试，得益于其标准化的基础。
- 🚀 **性能优化**：Lit 已经针对性能进行了优化，但还可以通过高效属性更新、模板缓存和指令使用进一步优化。
- 🔗 **框架集成**：Web Components 的优势之一是它们的互操作性，可以与 React、Vue 等流行框架无缝集成。
- 🏗️ **实际应用场景**：Lit 和 Web Components 在设计系统和微前端架构中表现出色。
- 📝 **最佳实践**：使用强类型定义、类型化事件和泛型可重用组件，以获得最佳开发体验。

关键要点：
- **基于标准**：建立在浏览器标准上，而非框架约定。
- **TypeScript 友好**：一流的 TypeScript 支持，提供更好的工具支持。
- **高性能**：优化的渲染，开销最小。
- **可互操作**：可与任何框架或无框架一起使用。
- **可扩展**：非常适合设计系统和微前端。

---

## [Next.js 15.3: Now Including Turbopack Builds](https://nextjs.org/blog/next-15-3)

**原文标题**: [Next.js 15.3 | Next.js](https://nextjs.org/blog/next-15-3)

**中文标题**: "Next.js 15.3 | Next.js"

Next.js 15.3 引入了 Turbopack 构建工具、新的客户端监控和导航钩子等功能，提升了开发和生产构建的性能和灵活性。

- 🚀 **Turbopack 构建工具（Alpha）**：生产构建速度提升，支持多核性能扩展，4 核快 28%，16 核快 60%，30 核快 83%。  
- 🔧 **Rspack 社区支持（实验性）**：提供 Webpack 兼容的替代打包工具，测试通过率约 96%。  
- 📊 **客户端监控钩子**：通过 `instrumentation-client.js` 提前设置性能跟踪和错误监控。  
- 🔗 **导航钩子**：新增 `onNavigate` 和 `useLinkStatus`，支持路由控制和加载状态管理。  
- ⚡ **TypeScript 插件优化**：语言服务器性能提升约 60%，减少大型代码库的卡顿问题。  
- 📦 **其他改进**：包括 `new URL()` 支持、视口选项分离、Pinterest Rich Pins 支持等。  
- 🔄 **升级指南**：提供 CLI 或手动升级方式，建议非关键生产环境试用 Turbopack。  
- 🤝 **社区合作**：与 Rspack 团队合作，共享 SWC 和 Lightning CSS 等基础技术。  
- 📢 **反馈渠道**：鼓励通过 GitHub 讨论和问题提交反馈，助力稳定版发布。

---

## [Chrono 2.8: A Natural Language Date Parser](https://github.com/wanasit/chrono)

**原文标题**: [GitHub - wanasit/chrono: A natural language date parser in Javascript](https://github.com/wanasit/chrono)

**中文标题**: "GitHub - wanasit/chrono: 基于 JavaScript 的自然语言日期解析器"

Chrono 是一个用 JavaScript 编写的自然语言日期解析库，支持多种日期和时间格式的解析，适用于多种语言环境。

- 📅 **功能概述**：Chrono 可以解析多种自然语言日期格式，如“今天”、“明天”、“上周五”、“2013 年 8 月 17 日至 19 日”等。
- 🌍 **多语言支持**：默认支持英语（en）、日语（ja）、法语（fr）、荷兰语（nl）、俄语（ru）和乌克兰语（uk），部分支持德语（de）、葡萄牙语（pt）和繁体中文（zh.hant）。
- 📦 **安装**：通过 npm 安装 `chrono-node`，支持 Node.js 和浏览器环境。
- 🔄 **版本变化**：v2 版本仅默认解析国际英语，项目用 TypeScript 重写，代码结构更清晰。
- ⚙️ **使用方法**：通过 `chrono.parseDate` 或 `chrono.parse` 解析日期，支持参考日期和时区设置。
- ⏳ **解析选项**：支持 `forwardDate` 选项，可以设置未来日期；支持自定义时区映射。
- 📊 **解析结果**：返回包含日期组件（如年、月、日、小时等）的详细结果，支持严格模式和宽松模式。
- 🛠️ **自定义配置**：用户可以通过添加解析器（Parser）和优化器（Refiner）来自定义 Chrono 的行为。
- 📚 **开发指南**：项目使用 Jest 进行测试，贡献者可以通过克隆仓库、安装依赖并运行测试来参与开发。

---

## [Breakpoints and console.log Is the Past, Time Travel Is the Future](https://wallabyjs.com/?utm_source=cooperpress&utm_medium=javascriptweekly&utm_content=javascriptweekly)

**原文标题**: [Wallaby - Immediate JavaScript test feedback in your IDE as-you-type](https://wallabyjs.com/?utm_source=cooperpress&utm_medium=javascriptweekly&utm_content=javascriptweekly)

**中文标题**: "Wallaby - 在 IDE 中实时输入即得 JavaScript 测试反馈"

Wallaby.js 是一款实时运行 JavaScript 和 TypeScript 测试的工具，能够在代码编辑器中即时显示测试结果和代码覆盖率，大幅提升开发效率。

- 🚀 **即时反馈**：输入代码时立即运行测试，结果实时显示在代码旁边，减少上下文切换。
- ⚡ **极速运行**：仅运行受代码更改影响的最小测试集，速度远超传统测试工具。
- 🔓 **无锁定**：作为插件集成到现有测试框架和 IDE 中，无需依赖特定供应商或 API。
- 🛠️ **多工具支持**：支持 VS Code、React、Jest 等主流开发环境和测试工具。
- 🕰️ **时间旅行调试**：允许向前和向后调试代码，快速定位问题。
- 📊 **智能测试分析**：仅运行当前工作的测试文件，提高大型项目的测试效率。
- 📝 **内联运行时值**：在编辑器中直接查看 `console.log` 和变量值，支持快捷键操作。
- ❌ **内联错误报告**：错误信息直接显示在代码旁边，快速定位问题源。
- ✅ **内联代码覆盖率**：实时显示测试覆盖率，标记未覆盖的代码区域。
- 🌐 **测试资源管理器**：提供项目的测试和代码覆盖率全局视图，支持排序和过滤。
- 🔍 **运行时值探索器**：以树状视图查看和探索复杂的运行时对象。
- 📋 **交互式测试输出**：在编辑器的输出窗口中显示测试结果，包含错误、快照和日志。
- 📖 **测试故事**：以单一逻辑视图查看测试执行路径，便于调试和阅读代码。
- ⏱️ **测试性能分析**：记录和分析测试的 CPU 使用情况，优化性能。
- 🔄 **增强的差异和快照**：在编辑器中显示紧凑的差异对比，支持 Jest 快照更新。
- 💰 **效率提升**：据估算，使用基础功能即可提升 10.84% 的开发效率，年节省 2396 美元。
- 🌍 **广泛认可**：全球超过 10,000 家公司使用，包括多家财富 500 强企业，用户反馈极佳。

---

## [Communicate with Ableton Live via WebSockets](https://github.com/ricardomatias/ableton-live)

**原文标题**: [GitHub - ricardomatias/ableton-live: A library for communicating with Ableton Live via WebSockets, works both in NodeJS and in the Browser.](https://github.com/ricardomatias/ableton-live)

**中文标题**: GitHub - ricardomatias/ableton-live: 通过 WebSockets 与 Ableton Live 通信的库，支持 NodeJS 和浏览器环境。

一个用于通过 WebSockets 与 Ableton Live 通信的库，支持 NodeJS 和浏览器环境。

- 🎵 项目名称：Ableton Live  
- 🔗 项目链接：ricardomatias.net/ableton-live/  
- ⭐ 星星数：104  
- 🍴 复刻数：9  
- 📦 安装方式：通过 npm 安装 `npm install --save ableton-live`  
- 🎛️ 要求：Ableton Live 11 和 Max 4 Live  
- 🖥️ 支持环境：NodeJS 和 浏览器  
- 📄 文档：可在项目链接中找到详细文档  
- 🔄 开发提示：运行 `sudo lsof -i :send_port_number` 确保只有 Max 在使用端口  
- 🎶 相关主题：音乐、live、maxmsp、ableton、ableton-live、max4live  
- 📜 许可证：未明确提及，但项目公开可用

---

## [Ableton Live](https://www.ableton.com/)

**原文标题**: [Creative tools for music makers | Ableton](https://www.ableton.com/)

**中文标题**: 音乐创作者的创意工具 | Ableton

Ableton 最新动态：涵盖 Note 1.3 新功能、艺术家故事、教程及 Live 12.1 更新内容  

- 🎵 Note 1.3 新增功能：支持序列节拍、旋律与和弦创作  
- 📱 移动端更新：Move 应用新增采样翻转功能  
- 🎤 艺术家故事：Raffertie 从音乐学院到电子音乐的转型历程  
- 🌱 艺术家故事：TOKiMONSTA 的音乐风格新探索  
- 🎬 教程推荐：使用 Ableton Live 制作歌舞伎风格音乐  
- 🎧 Live 12.1 亮点：MIDI 工具包、鼓采样器新设备及 Push 控制器升级  
- � 更多内容：涵盖新闻、下载、视频及 Loop 资源

---

## [Spacetime 7.9](https://github.com/spencermountain/spacetime)

**原文标题**: [GitHub - spencermountain/spacetime: A lightweight javascript timezone library](https://github.com/spencermountain/spacetime)

**中文标题**: GitHub - spencermountain/spacetime: 一个轻量级的 JavaScript 时区库

Spacetime 是一个轻量级的 JavaScript 时区库，用于处理日期计算、时区转换和格式化。

- 🌍 支持远程时区计算，包括夏令时、闰年和半球差异  
- 📅 提供类似 Moment 的 API（但不可变）  
- 🚀 无依赖（不依赖 Intl API），大小约 40kb  
- 🔌 支持插件扩展功能  
- ⏳ 频繁更新以应对即将到来的夏令时变化  
- 📊 支持即将推出的 Temporal 标准  
- 📦 可通过 npm 或 CDN 安装  
- 📝 支持多种日期输入格式（如 epoch、数组、ISO 等）  
- 🔧 提供丰富的日期操作方法（如 add、subtract、startOf、endOf 等）  
- ⏱️ 支持时间比较和差异计算  
- 🌐 支持 IANA 时区代码和宽松时区名称（需插件）  
- 📊 提供灵活的日期格式化选项  
- ⚠️ 注意历史时区信息和国际日期线的限制  
- 🔧 支持自定义语言和周起始日配置  
- 🔗 相关推荐：luxon、date-fns、sugarjs/dates 等  

Spacetime 是一个功能强大且易于使用的库，适合处理复杂的日期和时区问题。

---

## [in SQL ISO format.](https://github.com/spencermountain/spacetime/issues/437)

**原文标题**: [Question: format('SQL') · Issue #437 · spencermountain/spacetime · GitHub](https://github.com/spencermountain/spacetime/issues/437)

**中文标题**: "问题：format('SQL') · 第 437 期 · spencermountain/spacetime · GitHub"

overview summary  
该内容是关于一个 GitHub 仓库中的问题讨论，用户询问是否可以在 SQL 中格式化 DateTime 为 ISO 格式的字符串，并希望库能提供便捷的方法。  

- 🚀 **仓库信息** - 仓库名为 spacetime，属于用户 spencermountain，有 4k 星标和 189 个分支。  
- 📝 **问题描述** - 用户 vanodevium 提出能否在 SQL 中将 DateTime 格式化为 ISO 格式的字符串（#437 号问题）。  
- 🔍 **功能需求** - 用户希望库能提供常量方法直接生成所需格式，避免手动编写。  
- 🏷️ **标签分类** - 问题被标记为“enhancement”（功能增强）和“yess”。  
- ❓ **开发状态** - 问题已关闭，暂无分配人员、项目或里程碑关联。  
- 🙏 **用户反馈** - 用户表达了对该库的赞赏，称其为“awesome library”。

---

## [Perspective 3.5](https://perspective.finos.org/)

**原文标题**: [Perspective | Perspective](https://perspective.finos.org/)

**中文标题**: "视角 | 视角"

Perspective 是一个交互式分析和数据可视化组件，特别适合处理大型和/或流式数据集，可用于创建用户可配置的报告、仪表板、笔记本和应用程序，并支持独立部署或与 Python/JupyterLab 结合使用。

- 🚀 高性能查询引擎：基于 C++ 编写，支持 WebAssembly 和 Python，兼容 Apache Arrow，内置高效列式表达式语言（ExprTK）。  
- 🖥️ 跨框架 UI：提供自定义元素（Custom Element），支持浏览器端 WebAssembly 或服务端 WebSocket（Python/Node）。  
- 📊 Jupyter 集成：作为 JupyterLab 组件和 Python 库，支持笔记本交互式分析及生产级 Voila 应用扩展。  
- 🌐 灵活部署：JavaScript 组件（如`<perspective-viewer>`）可无缝集成到任何 Web 框架，支持 API 或用户交互配置。  
- 🔄 数据混合：支持浏览器端与服务端（Python）数据混合，视图可交叉过滤、导出、堆叠及保存。  
- ⚡ 高效内存：依赖 WebAssembly 和 Apache Arrow 实现快速查询计算与低内存占用，适合处理超大规模数据集。  
- 🐍 Python 支持：`perspective-python`提供与 WebAssembly 版本相同的数据引擎，支持生产级虚拟化或 Jupyter 嵌入式组件。  
- 📉 动态加载：虚拟化组件仅渲染当前屏幕所需数据，支持极大数据集即时加载或通过 Arrow 流式传输。  
- 🔬 科研友好：`PerspectiveWidget`支持在 Jupyter 中交互式可视化 Pandas 和 Arrow 数据。

---

## [Embla Carousel 8.6](https://www.embla-carousel.com/)

**原文标题**: [A lightweight carousel library with fluid motion and great swipe precision | Embla Carousel](https://www.embla-carousel.com/)

**中文标题**: "轻量级轮播库，流畅动画与精准滑动 | Embla Carousel"

Embla Carousel 是一个轻量级的轮播库，具有流畅的动画效果和精准的滑动体验，支持高度扩展和自定义。

- 🎠 轻量级轮播库，提供流畅动画和精准滑动  
- 🔧 高度可扩展的 API 设计，灵活满足各种需求  
- 🧩 插件系统支持随时添加功能和自定义轮播效果  
- 🛠️ 轮播生成器可快速创建个性化轮播组件

---

## [simpleParallax.js 6.1](https://simpleparallax.com/)

**原文标题**: [simpleParallax.js - Easy Parallax Effect for React & JavaScript](https://simpleparallax.com/)

**中文标题**: "simpleParallax.js - 为 React 和 JavaScript 轻松实现视差效果"

simpleParallax.js 是一个轻量级的 JavaScript 和 React 库，用于为任何图像添加视差动画效果。它以简单易用和出色的视觉效果著称，支持直接应用于图像标签，无需背景图像。提供了多种配置选项和方向设置，适用于 React 和原生 JavaScript 项目。

- 🚀 **简单易用**：轻量级库，轻松为图像添加视差效果。  
- 🖼️ **支持任意图像**：直接应用于图像标签，无需背景图像。  
- ⚙️ **多种配置选项**：包括方向、缩放、延迟、过渡等参数。  
- 🔄 **方向设置**：支持上下左右及对角线方向的视差效果。  
- 📦 **安装简单**：通过 npm 或 yarn 安装，支持 React 和原生 JavaScript。  
- 🔧 **自定义设置**：可调整缩放比例、延迟时间、过渡效果等。  
- 📱 **响应式支持**：适用于不同设备和滚动容器。  
- ⭐ **开源支持**：鼓励在 GitHub 上给项目点赞支持。

---

## [Tesseract.js 6.0.1](https://github.com/naptha/tesseract.js)

**原文标题**: [GitHub - naptha/tesseract.js: Pure Javascript OCR for more than 100 Languages 📖🎉🖥](https://github.com/naptha/tesseract.js)

**中文标题**: "GitHub - naptha/tesseract.js: 纯 JavaScript OCR 支持 100 多种语言 📖🎉🖥"

Tesseract.js 是一个纯 JavaScript OCR 库，支持超过 100 种语言，可在浏览器和 Node.js 中使用，基于 WebAssembly 的 Tesseract OCR 引擎。

- 📖 **功能概述**：Tesseract.js 能够从图像中提取文本，支持多语言识别，适用于浏览器和 Node.js 环境。
- 🎉 **使用简单**：通过简单的 API 调用即可实现 OCR 功能，支持异步操作。
- 🖥 **跨平台**：支持浏览器（通过 CDN 或 webpack）和 Node.js（v14 及以上版本）。
- 🔧 **安装方式**：可通过 CDN、npm 或 yarn 安装，支持 ESM 和 CommonJS。
- 📜 **许可证**：Apache-2.0 许可证，开源且免费使用。
- 🌍 **多语言支持**：支持超过 100 种语言的文本识别。
- 🚀 **性能优化**：v5 和 v6 版本显著减少了文件大小和内存使用，提升了运行效率。
- ⚠️ **限制**：不支持 PDF 文件，也不修改 Tesseract 的核心识别模型。
- 📚 **文档丰富**：提供详细的文档、示例和社区项目参考。
- 🔄 **社区贡献**：欢迎社区贡献，提供开发指南和测试流程。
- 💡 **替代方案**：对于更复杂的需求，推荐使用 Scribe.js 库。

---

## [Meticulous automatically creates and maintains an E2E UI test suite with zero developer effort](https://www.meticulous.ai?utm_source=javascript_weekly&utm_campaign=april11th2025)

**原文标题**: [Meticulous](https://www.meticulous.ai?utm_source=javascript_weekly&utm_campaign=april11th2025)

**中文标题**: "一丝不苟"

Meticulous AI 提供了一种无需编写和维护测试的自动化测试解决方案，通过记录用户交互并生成覆盖所有边缘情况的测试套件，帮助开发者快速发现和修复问题。

- 🚀 **无需编写测试** - Meticulous AI 自动记录用户交互并生成测试套件，覆盖所有代码分支和边缘情况。  
- 🔍 **实时监控** - 在开发、预发布和生产环境中记录会话，确保全面覆盖。  
- ⚡ **快速反馈** - 在合并代码前查看 PR 对用户流程的影响，避免回归问题。  
- 🛠️ **零维护** - 测试套件随应用自动更新，无需手动修复或维护。  
- 🌐 **广泛兼容** - 支持多种前端框架（如 React、Vue、Angular 等），并可与其他测试工具结合使用。  
- ⏱️ **高效执行** - 通过并行化测试，可在 120 秒内完成数千次测试。  
- 💬 **用户认可** - 被 Dropbox、Lattice 等 100 多家组织信任，显著提升开发效率和代码质量。  
- 📥 **快速上手** - 只需添加脚本标签，几分钟即可集成到现有工作流中。

---

## [Frontend Focus](https://frontendfoc.us)

**原文标题**: [Frontend Focus](https://frontendfoc.us)

**中文标题**: "前端聚焦"

每周精选前端资讯，涵盖 HTML、CSS、WebGL、Canvas 及浏览器技术等。  

- 📰 每周一期，提供最佳前端新闻、文章和教程  
- ✉️ 订阅用户达 73085 人，已发布 687 期  
- 📡 支持通过 RSS 订阅获取更新  
- 🔍 可查看最新一期内容作为示例  
- 🏢 由 Cooperpress 出版，注重隐私和反垃圾邮件政策  
- 🔒 严格遵守 GDPR 政策，保护用户数据安全

---

## [GitHub's Taylor Blau caught up with Linus Torvalds](https://github.blog/open-source/git/git-turns-20-a-qa-with-linus-torvalds/)

**原文标题**: [Git turns 20: A Q&A with Linus Torvalds - The GitHub Blog](https://github.blog/open-source/git/git-turns-20-a-qa-with-linus-torvalds/)

**中文标题**: "Git 诞生 20 周年：与 Linus Torvalds 的问答 - GitHub 博客"

Git 诞生 20 周年：Linus Torvalds 访谈回顾  

- 🎉 Git 于 2005 年 4 月 7 日由 Linus Torvalds 创建，最初是为了替代 Linux 内核开发中无法继续使用的 BitKeeper。  
- ⚡ Git 的设计理念是分布式和高效，解决了当时版本控制系统（如 CVS）的性能和可扩展性问题。  
- 🛠️ Linus 在 10 天内完成了 Git 的初始版本，并在之后将其移交给社区维护，由 Junio Hamano 长期担任维护者。  
- 🔄 Git 的分布式特性使其成为协作开发的理想工具，后来催生了 GitHub 等平台。  
- 🤔 Linus 提到 Git 的成功出乎意料，尤其是它被广泛用于各种规模的项目，从大型开源项目到个人小项目。  
- 🚀 Git 的核心设计简单而强大，尽管早期用户认为它难以使用，但后来逐渐被广泛接受和喜爱。  
- 🔮 对于未来，Linus 认为 Git 的挑战主要来自用户的新需求和使用场景，但他对 Git 的持续成功充满信心。  
- 🙏 Linus 将 Git 的成功归功于社区，尤其是维护者 Junio Hamano 和其他贡献者的长期努力。

---

## [programming in PostScript](https://seriot.ch/projects/programming_in_postscript.html)

**原文标题**: [Programming in PostScript](https://seriot.ch/projects/programming_in_postscript.html)

**中文标题**: 《PostScript 编程》

PostScript 不仅是一种页面描述语言，还能用于编程和游戏开发，通过巧妙的方法可以将打印机变成游戏平台。

- 🎮 PostScript 是一种基于堆栈的语言，最初设计用于文档渲染，但也可以用于编写游戏。
- 📜 PostScript 的历史可以追溯到 20 世纪 70 年代的 Xerox PARC，Adobe 在 1984 年发布了第一个版本。
- 🖨️ PostScript 允许设备独立的高质量图形，但随着互联网的普及，PDF 逐渐取代了它。
- 🧩 PostScript 程序可以通过 GhostScript 解释器运行，GhostScript 还可以动态解释 PostScript 代码。
- 📚 PostScript 使用四个堆栈：操作数堆栈、字典堆栈、执行堆栈和图形状态堆栈。
- 🎨 PostScript 可以用于绘制图形，例如通过简单的算术和图形变换来绘制时钟。
- 🤖 PostScript 是图灵完备的，这意味着它可以执行与其他高级语言相同的计算任务。
- ♟️ 通过 PostScript 可以编写游戏，例如井字棋和国际象棋，甚至可以在打印机上运行。
- 🕹️ 桌面游戏如 Sokoban 和俄罗斯方块也可以通过 PostScript 实现，需要解决即时用户输入等问题。
- 🎵 PostScript 还可以用于动画和 3D 渲染，甚至可以通过 MIDI 消息添加音乐。
- 📝 通过 PostScript 可以读写文件，甚至可以在打印机文件系统中保存游戏进度。

---

## [Minimal CSS-only Blurry Image Placeholders](https://leanrada.com/notes/css-only-lqip/)

**原文标题**: [Minimal CSS-only blurry image placeholders](https://leanrada.com/notes/css-only-lqip/)

**中文标题**: "纯 CSS 实现的极简模糊图片占位符"

一种使用纯 CSS 生成模糊图像占位符（LQIP）的技术，仅需一个自定义属性即可实现，无需额外标记或 JavaScript。

- 🖼️ 仅需单个 CSS 自定义属性即可生成模糊图像占位符，例如：`<img src="…" style="--lqip:192900">`  
- ⚡ 优势：简洁、非侵入性，无需包装元素、长数据字符串或 JavaScript  
- ⚠️ 注意：依赖 CSS 图像的技术可能不被 RSS 阅读器或“阅读模式”客户端支持  
- 🔍 对比其他 LQIP 方案：包括低分辨率 WebP/JPEG、SVG 形状（SQIP）、BlurHash、渐进式 JPEG 等  
- 🎨 技术核心：将图像信息压缩为 20 位整数，通过 CSS 解码并渲染为 3×2 网格的灰度组件 + 基色  
- 🛠️ 实现细节：使用 Oklab 色彩空间编码基色（8 位），6 个灰度组件（各 2 位），通过 CSS 数学函数解包  
- 📊 限制：CSS 整数值范围有限（-999,999 至 999,999），仅支持约百万种配置  
- 🌈 渲染方法：用径向渐变模拟双线性插值，平滑拼接灰度组件，叠加基色生成最终效果  
- 🔄 替代方案尝试：曾探索四色混合、单色填充等，最终选择单基色 + 灰度的平衡方案  
- 🔮 未来优化：期待 CSS `attr()` Level 5 支持，进一步简化标记语法

---

## [default styles for H1 elements are changing](https://developer.mozilla.org/en-US/blog/h1-element-styles/)

**原文标题**: [Default styles for h1 elements are changing | MDN Blog](https://developer.mozilla.org/en-US/blog/h1-element-styles/)

**中文标题**: "h1 元素的默认样式即将改变 | MDN 博客"

浏览器默认样式对嵌套标题元素（如 `<h1>`）的更改即将生效，开发者需检查网站以避免意外显示问题及 Lighthouse 检测失败。

- 🚨 **默认样式变更**：浏览器将移除 `<h1>` 在 `<section>`、`<article>` 等嵌套结构中的自动降级样式（如字体大小和边距），统一为相同样式。  
- 📅 **时间线**：  
  - Firefox：2025 年 3 月 31 日起逐步推送，稳定版 Firefox 140 全面生效。  
  - Chrome：136 版本起显示废弃警告，影响 Lighthouse 评分。  
  - Safari：预计后续跟进。  
- ⚠️ **Lighthouse 警告**：新增规则 `H1UserAgentFontSizeInSection`，若未显式定义 `<h1>` 的 `font-size` 会触发警告。  
- 🛠️ **修复建议**：  
  - 显式设置 `<h1>` 的样式（如 `font-size: 2em; margin-block: 0.67em;`）。  
  - 使用 `:where(h1)` 避免特异性冲突。  
  - 避免依赖默认样式，改用 `<h2>`、`<h3>` 等明确层级标签。  
- 📚 **参考资源**：MDN 文档更新了相关说明，提供详细用法建议。  
- 🔍 **自查步骤**：通过 Lighthouse 和开发者工具检测废弃用法，更新 CSS 重置代码。

---

## [Docker has released a new extension for VS Code](https://www.docker.com/blog/docker-dx-extension-for-vs-code/)

**原文标题**: [New Docker Extension for Visual Studio Code | Docker](https://www.docker.com/blog/docker-dx-extension-for-vs-code/)

**中文标题**: "Visual Studio Code 的新 Docker 扩展 | Docker"

Docker 发布了新的 VS Code 扩展 Docker DX，旨在提升开发者在编辑 Docker 相关文件时的效率和体验。该扩展由 Docker 和 Microsoft 联合开发，提供了实时反馈、漏洞检查和文件导航等功能。

- 🚀 **Docker DX 扩展发布**：新的 VS Code 扩展，提供实时反馈和增强的 Docker 工具支持。  
- 🔍 **关键功能**：包括 Dockerfile 语法检查、镜像漏洞修复（实验性）、Bake 文件支持和 Compose 文件大纲导航。  
- 🛠️ **Dockerfile 优化**：通过 BuildKit 和 Buildx 提供构建警告和最佳实践建议，Docker Scout 提供漏洞检查。  
- 📂 **Bake 文件支持**：代码补全、变量导航和基于 Dockerfile 阶段的建议目标生成。  
- 🌐 **Compose 文件导航**：通过大纲视图快速浏览复杂的 Compose 文件。  
- 💻 **语言服务器支持**：Docker Language Server 基于 LSP，可在其他编辑器中提供相同的智能编辑体验。  
- 📢 **反馈与贡献**：鼓励用户提供反馈，并欢迎通过 GitHub 参与项目贡献。  
- 🔗 **相关资源**：提供扩展安装链接、反馈渠道和语言服务器项目信息。

---

