### [流体计算：我们如何构建无服务器服务器 - Vercel](https://vercel.com/blog/fluid-how-we-built-serverless-servers)

**原文标题**: [Fluid compute: How we built serverless servers - Vercel](https://vercel.com/blog/fluid-how-we-built-serverless-servers)

概述：Vercel 推出的 Fluid compute 技术和 Active CPU 定价模式通过优化资源利用、减少冷启动和降低成本，显著提升了无服务器计算的效率。该技术已支持每周超过 450 亿次请求，并为客户节省高达 95% 的成本。其核心是通过自定义传输协议和智能路由系统，实现请求的多路复用和资源的动态分配。

- 🚀 Fluid compute 技术通过更高效的资源利用和减少冷启动，显著降低成本，支持每周超过 450 亿次请求，节省高达 95% 的费用。
- 🔧 基于 React Server Components (RSC) 和 Next.js 的 App Router，Vercel 开发了支持 HTTP 流式传输的新传输协议。
- 🌐 通过自定义的 TCP 隧道协议，Vercel 实现了 Lambda 函数与基础设施之间的高效通信，支持流式响应和其他高级功能。
- 🔄 通过 compute-resolver 服务，Vercel 智能路由请求，提高 TCP 连接的复用率，优化资源利用。
- ⚙️ Rust 核心系统动态监控函数实例的资源使用情况，确保在不过载的情况下多路复用请求。
- 💡 Active CPU 定价模式根据实际使用的 CPU 时间和内存量计费，进一步降低了 I/O 密集型工作负载的成本。
- 📊 目前，超过 75% 的 Vercel 函数调用使用 Fluid compute，推荐新项目和现有项目启用以节省成本。

---

### [Next.js 迁移 - 更新日志 - LLM 网关](https://llmgateway.io/changelog/nextjs-migration?v=2)

**原文标题**: [Next.js migration - Changelog - LLM Gateway](https://llmgateway.io/changelog/nextjs-migration?v=2)

项目从 TanStack Start 迁移至 Next.js，性能与 SEO 显著提升，系统资源使用更高效。

- 🚀 **迁移至 Next.js**：从 TanStack Start（旧版 alpha）切换到 Next.js，效果显著。  
- 📈 **性能提升**：  
  - 性能评分从 85 升至 100  
  - SEO 评分从 80 升至 100  
  - 速度指数从 2.4 秒优化至 1.1 秒  
- 🧠 **迁移原因**：  
  - Next.js 提供开箱即用的 SEO 和性能优化  
  - 更简单的路由、布局和部署模型  
  - 支持边缘计算，兼容未来计划（中间件、流式处理等）  
  - CPU 和内存使用更稳定高效  
- 🔍 **变化对比**：  
  - 之前：CPU 和内存峰值高，渲染不一致，SEO 较低  
  - 现在：系统资源使用降低，渲染速度低于 1.2 秒，关键 Lighthouse 评分满分  
- 💡 **未来展望**：为更快功能交付、更低延迟和更流畅的开发体验奠定基础。

---

### [未找到标题](https://x.com/tannerlinsley/status/1950310182451630384)

**原文标题**: [No title found](https://x.com/tannerlinsley/status/1950310182451630384)

当前页面提示 JavaScript 未启用或浏览器不受支持，建议用户开启 JavaScript 或更换浏览器以继续使用 x.com，并提供相关帮助链接和隐私提示。

- 🚫 JavaScript 未启用或浏览器不受支持  
- 🔄 建议启用 JavaScript 或更换支持的浏览器  
- ℹ️ 提供帮助中心链接获取支持浏览器列表  
- 🔒 隐私相关扩展可能导致问题，建议禁用后重试  
- 📜 页面底部包含服务条款、隐私政策等法律链接

---

### [未找到标题](https://x.com/nextjs/status/1949935608735866957)

**原文标题**: [No title found](https://x.com/nextjs/status/1949935608735866957)

当前页面提示 JavaScript 未启用或浏览器不受支持，导致功能无法正常使用。

- 🚫 JavaScript 未启用：检测到浏览器中 JavaScript 被禁用，需启用以继续使用 x.com。  
- 🌐 浏览器支持：建议切换至受支持的浏览器，具体列表可参考帮助中心。  
- 🔧 扩展冲突：部分隐私相关扩展可能导致问题，建议禁用后重试。  
- 📜 相关链接：提供帮助中心、服务条款、隐私政策等文档入口。  
- 🔄 操作提示：页面鼓励用户再次尝试操作。  
- ©️ 版权信息：底部标注 2025 年 X 公司版权及广告信息等。

---

### [维梅特里克](https://vemetric.com/?utm_source=nextjsweekly&utm_medium=Referral&utm_campaign=newsletter)

**原文标题**: [Vemetric](https://vemetric.com/?utm_source=nextjsweekly&utm_medium=Referral&utm_campaign=newsletter)

Vemetric 是一款开源、隐私至上的网站与产品分析工具，专注于提供简洁易用的用户行为洞察，支持从首次访问到功能采纳的完整用户旅程追踪。

- 🌐 **开源与隐私优先**：Vemetric 以 GDPR 合规设计，默认无 Cookie 跟踪，数据存储在欧盟服务器，支持用户自主选择启用 Cookie。
- 📊 **核心功能**：提供实时看板、用户旅程分析、事件流监控、漏斗转化跟踪（支持多事件路径），并计划推出用户分群、营销活动分析等高级功能。
- 🔍 **多维度洞察**：包括热门页面、最佳引荐来源、用户地域分布等，支持匿名与登录行为合并分析，并配备交互式热力图（即将上线）。
- 💻 **便捷集成**：提供多平台 SDK 和脚本安装指南，支持快速接入项目，开发者体验友好。
- 🏷️ **灵活定价**：开放测试期间提供免费版（2,500 次事件/月）和专业版（10,000 次事件/月，无限项目），未来价格将随功能成熟度调整。
- ❓ **常见问题**：事件限额按组织统计，超限提醒升级；暂不支持自托管（社区版开发中），开源代码基于 AGPLv3 许可。
- 🚀 **未来规划**：持续增加自动化触发、营销活动深度分析等功能，鼓励用户反馈需求。

---

### [使用运行时密钥注入对 Next.js 进行仪表化 | Phase 博客](https://phase.dev/blog/instrumenting-nextjs-with-runtime-secret-injection/)

**原文标题**: [Instrumenting Next.js with runtime secret injection | Phase Blog](https://phase.dev/blog/instrumenting-nextjs-with-runtime-secret-injection/)

Next.js 14 引入了一个新特性 Instrumentation，允许在应用启动时运行自定义逻辑，并通过 instrumentation.ts/js 文件注入运行时密钥，提升安全性和可移植性。

- 🚀 **Instrumentation 功能**：Next.js 14 新增功能，通过根目录的 `instrumentation.ts/js` 文件在服务器启动时执行自定义逻辑（如日志或遥测服务）。  
- 🔐 **运行时密钥注入**：利用 `register()` API 从密钥管理服务（如 Phase、AWS Secrets Manager）动态获取密钥，避免密钥泄露到代码或构建产物中。  
- ⚠️ **.env 文件的缺陷**：传统 `.env` 文件易泄露、难管理，缺乏加密和访问控制，而密钥管理工具提供更安全的解决方案。  
- 📂 **实现步骤**：  
  - 创建 `instrumentation.ts` 文件，通过 API 获取密钥并存入 `globalThis` 全局对象。  
  - 在应用代码中通过 `globalThis.secrets` 访问密钥，或使用模块化缓存（如 `lib/runtime-env.ts`）避免污染全局作用域。  
- 🌐 **客户端密钥传递**：避免使用 `NEXT_PUBLIC_` 变量，改为通过 Server Component 向 Client Component 传递 props 或 Context 共享密钥。  
- 🔧 **优势**：密钥不进入版本控制或构建流程，支持动态更新，提升团队协作和安全性。  
- 📚 **扩展阅读**：Next.js Instrumentation 文档、Phase Node SDK 及密钥管理最佳实践。

---

### [捕获指标 - 网页性能专家 - 停止发布臃肿代码：Next.js 开发者的实用打包精简方案](https://www.catchmetrics.io/blog/stop-shipping-bloat-practical-bundle-diet-for-nextjs-developers)

**原文标题**: [Catch Metrics - the web performance experts - Stop Shipping Bloat: Practical Bundle Diet for Next.js Developers](https://www.catchmetrics.io/blog/stop-shipping-bloat-practical-bundle-diet-for-nextjs-developers)

Next.js 应用在加载过多 JavaScript 时性能会受影响，大体积的代码包会增加下载、解析和执行时间，延迟首次内容绘制（FCP）和可交互时间（TTI），同时也会推迟广告位和其他第三方脚本的加载。

- 📦 本文所有大小数据均指 Bundlephobia 报告的压缩后但未压缩的体积（数据验证于 2025 年 7 月）。虽然 gzip/brotli 可以减少传输字节，但浏览器仍需解析每个压缩后的字节，因此解析和执行成本与压缩后的大小相关。
- 🔄 用轻量级替代库替换大型库可以显著减小体积。例如，用 dayjs（7 kB）替代 moment（295 kB）可以减少 96% 的体积，且 API 相似，迁移简单。
- 🔍 在安装 npm 包之前使用 Bundlephobia 查看安装大小、压缩后大小、依赖树和导出表面，以便比较替代方案。
- 🤖 使用 LLM（大型语言模型）询问替代方案，可以获取更小的替代库、迁移到服务器端的建议以及迁移难度评估。
- 🚫 避免使用通配符导入（import *），这会阻碍 tree-shaking，增加运行时开销。应使用命名导入以优化打包体积。
- 🛠️ 使用 ESLint 的 import/no-namespace 规则来禁止通配符导入，并确保内部库在 package.json 中声明"sideEffects": false 以便打包工具可以删除未使用的文件。
- 📊 优化 Lodash 的使用：可以选择按方法导入、使用 lodash-es 并启用 tree-shaking、或通过 Babel/SWC 插件转换导入方式。需注意避免 CJS 和 ESM 混合使用导致的重复代码。
- ⚠️ 注意重复代码问题：遗留的 require('lodash') 或第三方依赖可能引入重复的 Lodash 代码，需通过工具如@next/bundle-analyzer 检测并修复。
- 📏 使用 Next.js 的配置别名功能来统一 Lodash 的导入路径，确保开发和生产环境一致。
- 🔎 检测和修复重复代码：使用 npm ls lodash 查看哪些包引入了 CJS Lodash，并通过 patch-package 或提交 PR 修复。
- 🚀 通过选择轻量库和优化导入策略，可以显著提升性能。现代 Web 应用尤其在移动设备上需要快速响应，优化代码包体积是关键。
- 📈 使用 Lighthouse、Web Vitals 或 Next.js 的构建大小分析工具测量改进效果，并持续迭代优化。最终结果将是一个更快、更响应的应用，充分发挥 Next.js 的潜力。

---

### [在 Vercel 上使用 Next.js 部署 Puppeteer](https://vercel.com/guides/deploying-puppeteer-with-nextjs-on-vercel)

**原文标题**: [Deploying Puppeteer with Next.js on Vercel](https://vercel.com/guides/deploying-puppeteer-with-nextjs-on-vercel)

本指南详细介绍了如何在 Vercel 上部署结合 Puppeteer 的 Next.js 应用，实现无头浏览器自动化功能，并通过生成网页截图作为示例演示关键步骤。

- 🛠️ **Puppeteer 简介**：Puppeteer 是一个强大的 Node.js 库，用于控制无头 Chrome 或 Chromium，适用于截图、生成 PDF 和网页抓取等任务。  
- ⚙️ **Vercel 适配**：在 Vercel 的服务器环境中运行 Puppeteer 需解决 250MB 的包大小限制，推荐使用轻量级组合：`puppeteer-core`（不包含浏览器）和`@sparticuz/chromium`（精简版 Chromium）。  
- 📂 **项目初始化**：通过`create-next-app`创建 Next.js 项目，并安装必要的依赖包，包括开发环境用的`puppeteer`和生产环境专用的轻量包。  
- 🌐 **示例 API 实现**：创建`/api/screenshot`路由，动态加载环境适配的 Puppeteer 包，接收 URL 参数并返回对应页面的 PNG 截图。  
- 🖥️ **前端交互界面**：构建简单页面，包含 URL 输入框和截图按钮，调用 API 并实时展示生成的截图或错误信息。  
- 🔧 **Vercel 配置**：修改`next.config.mjs`文件，声明不打包`@sparticuz/chromium`和`puppeteer-core`以兼容 Vercel 环境。  
- 🚀 **部署上线**：通过 Git 或 Vercel CLI 部署应用，即可在 Vercel 的无服务器架构中运行 Puppeteer 自动化任务。

---

### [[实验] <Link unstable_dynamicOnHover> 由 acdlite · Pull Request #77866 · vercel/next.js · GitHub](https://github.com/vercel/next.js/pull/77866)

**原文标题**: [[Experiment] <Link unstable_dynamicOnHover> by acdlite · Pull Request #77866 · vercel/next.js · GitHub](https://github.com/vercel/next.js/pull/77866)

Next.js 项目中关于 `<Link unstable_dynamicOnHover>` 实验性功能的合并提交摘要：

- 🚀 新增实验性功能：为 Link 组件添加 `unstable_dynamicOnHover` 选项，当设置为 true 时，鼠标悬停即触发动态预加载
- ⚡ 功能等效于在鼠标事件处理程序中将 prefetch prop 设为 true
- ⚠️ 注意：由于采用动态预加载，导航时目标页面数据可能存在轻微过时（与 prefetch={true} 语义相同）
- 🔧 技术实现：通过强制推送更新分支（3da3109 → 9eda36c）
- ✅ 代码审查：ztanner 审核通过，lubieowoce 待审核
- 🔒 状态：已合并到 canary 分支（提交 d0dbd3a），109 项检查通过后锁定讨论

该功能属于实验性 API，主要优化页面导航性能，但需注意数据新鲜度的潜在影响。

---

### [更优上传 - React 的简易文件上传方案](https://better-upload.com/)

**原文标题**: [Better Upload - Simple and easy file uploads for React](https://better-upload.com/)

概述：  
Better Upload 是一个简单易用的 React 文件上传工具，支持直接上传到任何 S3 兼容服务，并提供快速设置和美观的 UI 组件。  

- 🚀 **快速上手**：只需几分钟即可开始使用，直接将文件上传到 S3 存储桶。  
- 🎨 **美观设计**：使用 shadcn/ui 组件快速构建用户界面。  
- 🔒 **文件自主权**：文件直接上传到您的 S3 存储桶，确保完全控制。  
- 📂 **文件限制**：每次最多上传 4 个文件，每个文件最大 2MB，支持 JPEG、PNG、GIF 格式。  
- 💻 **客户端示例**：通过 `UploadDropzone` 组件轻松实现拖放上传功能。  
- ⚙️ **服务器配置**：支持 S3 客户端配置，包括存储桶名称、路由规则和文件类型限制。  
- 🔗 **开源支持**：提供 GitHub 链接，方便开发者查看和贡献代码。

---

### [AI SDK 5 - Vercel](https://vercel.com/blog/ai-sdk-5)

**原文标题**: [AI SDK 5 - Vercel](https://vercel.com/blog/ai-sdk-5)

AI SDK 5 发布，为 TypeScript 和 JavaScript 开发者提供了全面的类型安全聊天和代理循环控制功能，支持 React、Svelte、Vue 和 Angular 等主流框架。

- 🚀 **AI SDK 5 发布**：首个完全类型化且高度可定制的聊天集成框架，支持多种前端框架。
- 🔄 **代理循环控制**：新增 `stopWhen` 和 `prepareStep` 功能，提供更精细的执行流程控制。
- 🗣️ **语音生成与转录**：实验性支持语音生成和转录，统一了不同提供商的 API 接口。
- 🛠️ **工具改进**：包括动态工具、提供者执行工具和工具生命周期钩子，增强灵活性和类型安全。
- 📜 **V2 规范**：更新了所有规范，支持新的 API 功能和扩展机制。
- 🌍 **全局提供者**：简化模型引用，支持自定义全局提供者。
- 🔍 **原始响应访问**：提供对原始请求和响应数据的完全访问，便于调试和实现特定功能。
- 📚 **Zod 4 支持**：支持 Zod 4 和 Zod 3，增强输入和输出验证。
- 🔄 **迁移工具**：提供自动化迁移工具和详细的迁移指南，帮助开发者平滑升级。
- 🏗️ **模块化架构**：重新设计的 `useChat` 钩子支持灵活的传输、解耦的状态管理和框架无关的聊天体验。

---

### [停止重复渲染 — TanStack DB，专为 TanStack Query 设计的嵌入式客户端数据库 | TanStack 博客](https://tanstack.com/blog/tanstack-db-0.1-the-embedded-client-database-for-tanstack-query)

**原文标题**: [Stop Re-Rendering — TanStack DB, the Embedded Client Database for TanStack Query | TanStack Blog](https://tanstack.com/blog/tanstack-db-0.1-the-embedded-client-database-for-tanstack-query)

TanStack DB 是一个客户端数据库层，旨在解决 React 应用中因数据更新导致的性能问题。它通过差分数据流技术，仅更新发生变化的部分，从而大幅提升性能。  

- 🚀 **性能优化**：TanStack DB 使用差分数据流技术，仅重新计算变化的部分，例如在 M1 Pro 上更新 10 万条数据中的一行仅需 0.7 毫秒。  
- 🔄 **无缝集成**：与 TanStack Query 兼容，无需重写现有代码，可逐步采用。  
- ⚡ **实时查询**：支持声明式查询，仅推送变化的数据，响应时间低于 1 毫秒。  
- 🔄 **乐观更新**：自动处理乐观更新，并在错误时回滚，减少手动管理状态的复杂性。  
- 📊 **简化架构**：支持加载规范化数据集合，并在客户端进行高效连接，减少 API 调用和网络依赖。  
- 🔌 **后端灵活**：支持 REST、GraphQL、WebSocket 等多种数据源，并可适配同步引擎（如 Electric、Firebase）。  
- 🛠 **增量采用**：可以从单个集合开始使用，逐步扩展，无需大规模重构。  
- 🎯 **目标场景**：适合已使用 TanStack Query 但遇到性能瓶颈、需要实时协作功能或处理大规模数据集的团队。  
- 📚 **资源**：提供文档、快速入门指南和 Discord 支持，前 20 个团队可获得迁移指导。  

TanStack DB 旨在提供一种更高效、更简单的方式来管理客户端数据，同时保持与现有架构的兼容性。

---

### [邪恶图表 - 精美动态图表](https://evilcharts.com/)

**原文标题**: [Evil Charts - Beautiful & Animated Charts](https://evilcharts.com/)

Recharts 是首选图表库，EvilCharts 提供更多动画交互式图表样式，适合项目使用。  

- 📊 Recharts 是作者首选的图表库  
- 🎨 EvilCharts 提供多样化的图表风格（如动态条形图、面积图、雷达图等）  
- ⚡ 图表支持动画和交互功能  
- 📅 示例数据涵盖 2024 年 1 月至 2025 年 6 月的时间范围  
- 📈 包含多种图表类型：条形图、面积图、折线图、饼图、雷达图等  
- 📉 示例中展示了正负增长率（如±5.2%）对比  
- 💻 可通过 GitHub 获取资源并快速开始使用

---

### [Sevalla® - 云应用平台。数分钟部署应用。](https://sevalla.com/?utm_source=nextjsweekly&utm_medium=Referral&utm_campaign=newsletter)

**原文标题**: [SevallaÂ® - Cloud Application Platform. Deploy Apps in Minutes.](https://sevalla.com/?utm_source=nextjsweekly&utm_medium=Referral&utm_campaign=newsletter)

Sevalla 是一个简化应用部署和托管的 PaaS 平台，提供全栈解决方案，强调易用性、灵活性和无限制的资源使用，支持全球部署和高效协作。

- 🚀 **一站式部署**：Sevalla 支持应用、数据库及静态站点的快速部署，无需基础设施管理。  
- 🌐 **全球覆盖**：利用 25 个数据中心和 260+ 边缘节点，实现低延迟和高性能内容交付。  
- 🛠️ **全托管服务**：包括应用托管（GKE+Cloudflare）、对象存储、数据库托管及免费静态站点托管。  
- 🔓 **无限制资源**：提供无限用户、资源、流量、并行构建和数据库使用，按需付费。  
- 💡 **开发友好**：支持任意技术栈、Git/Docker 部署，免除 DevOps 负担，专注编码。  
- 🔄 **灵活协作**：基于角色的访问控制（RBAC），支持团队无缝协作。  
- ⚡ **高性能网络**：通过私有连接保障应用与数据库间流量的高速与安全。  
- 📌 **透明定价**：无计划限制或隐藏费用，仅按实际使用计费。

---

### [无用的 useCallback | TkDodo 的博客](https://tkdodo.eu/blog/the-useless-use-callback)

**原文标题**: [The Useless useCallback | TkDodo's blog](https://tkdodo.eu/blog/the-useless-use-callback)

overview summary  
本文探讨了在 React 中过度使用`useCallback`和`useMemo`的问题，指出许多情况下这些钩子并无实际作用，反而增加了代码复杂性和维护成本。作者通过实际案例分析了无效的 memoization 模式，并提出了替代方案如“最新引用模式”和未来的`useEffectEvent`。

- 🏔️ **memoization 的初衷**  
  使用`useCallback`或`useMemo`通常是为了性能优化或防止副作用频繁触发，确保引用稳定性。

- 🚫 **无效的 memoization 场景**  
  当未传递给`React.memo`组件或内置 React 元素（如`<button>`）时，memoization 毫无意义，反而增加内部开销。

- 🔄 **依赖传递问题**  
  将非原始类型 props 作为内部 hook 的依赖项（如`useEffect`）会导致 memoization 链断裂，最终所有优化失效。

- 💥 **实际案例的连锁反应**  
  以 Sentry 代码库中的`useHotkeys`为例，未 memoized 的`attachments.filter`导致下游所有 memoization（如`paginateItems`）失效。

- 🛠️ **替代方案**  
  - **最新引用模式**：通过`useRef`动态更新值，避免依赖数组问题。  
  - **未来方案**：React 的`useEffectEvent`将直接解决“获取最新值且保持引用稳定”的需求。

- 🧠 **核心观点**  
  盲目应用 memoization 会增加代码脆弱性，建议仅在明确需要时使用，或依赖编译器优化。

---

### [写代码从来不是瓶颈 - ordep.dev](https://ordep.dev/posts/writing-code-was-never-the-bottleneck)

**原文标题**: [Writing Code Was Never The Bottleneck - ordep.dev](https://ordep.dev/posts/writing-code-was-never-the-bottleneck)

软件开发的核心瓶颈并非编写代码，而是理解、协作与维护。  

- 🤖 **代码生成成本趋零**：LLM 大幅降低代码编写时间，但理解、测试和维护成本反而增加。  
- 🔍 **验证复杂度上升**：生成的代码可能包含陌生模式或隐藏缺陷，审查和集成压力加剧。  
- 📚 **理解仍是核心挑战**：代码易写难懂，推理行为、确保可维护性仍需大量人力投入。  
- 👥 **协作信任不可替代**：团队依赖共享上下文和代码审查，过快生成代码可能削弱质量保障。  
- ⚖️ **工具未改变本质**：LLM 加速原型设计，但清晰的设计思维和严谨的评审仍是关键瓶颈。

---

### [是时候让现代 CSS 终结单页应用了——乔诺·奥尔德森](https://www.jonoalderson.com/conjecture/its-time-for-modern-css-to-kill-the-spa/)

**原文标题**: [It's time for modern CSS to kill the SPA - Jono Alderson](https://www.jonoalderson.com/conjecture/its-time-for-modern-css-to-kill-the-spa/)

现代 CSS 技术（如视图过渡 API 和推测规则）已能实现 SPA 的流畅交互效果，而无需客户端路由和复杂 JS 框架。文章批判了 SPA 的过度使用，指出其带来的性能、SEO 和维护问题，并倡导回归多页面应用（MPA）结合现代 CSS 的轻量化方案。

- 🌐 **SPA 的过时假设**：认为“应用感”必须依赖 SPA 的观点已被现代 CSS 技术推翻。  
- ⚠️ **SPA 的虚假承诺**：实际常导致加载延迟、滚动错乱、布局偏移等问题，性能代价高昂。  
- 🛠️ **浏览器原生解决方案**：视图过渡 API 实现跨页面动画，推测规则预加载页面，无需 JS。  
- 📉 **性能对比**：MPA+ 现代 CSS 方案在 TTI、SEO、资源占用上全面优于 SPA 框架（如 Next.js）。  
- 🚀 **开发建议**：优先使用 HTML/CSS 原生特性，仅在必要时添加 JS，避免框架滥用。  
- ⚠️ **注意事项**：推测规则需谨慎使用，低效页面会放大性能问题；Firefox 对部分 API 支持仍不完善。  
- 🔄 **技术案例**：代码示例展示如何用 CSS 实现页面淡入淡出和元素共享动画。  
- 📢 **行业呼吁**：区分网站与真实应用场景，回归简洁、高效的 Web 开发模式。

---

### [Parcel 如何打包 React 服务器组件](https://devongovett.me/blog/parcel-rsc.html)

**原文标题**: [How Parcel bundles React Server Components](https://devongovett.me/blog/parcel-rsc.html)

Parcel v2.14.0 新增了对 React Server Components (RSCs) 的支持，本文深入探讨了 RSCs 如何与打包工具集成、指令如 "use client" 的内部工作原理、代码分割机制及其优化等内容。

- 🚀 **Parcel 支持 RSCs**：Parcel v2.14.0 新增了对 React Server Components 的支持，通过统一的模块图实现跨环境代码分割。
- 📦 **打包工具的作用**：将多个 JavaScript 模块合并为更少的文件，优化加载性能，减少 HTTP 请求数量。
- 🔄 **代码分割**：通过将公共依赖提取到共享包中，优化初始加载性能和浏览器缓存利用率。
- ⚡ **动态加载**：动态 `import()` 语法支持按需加载模块，但可能导致网络瀑布问题。
- 🌐 **React Server Components**：RSCs 通过服务器端渲染和预加载机制，解决了嵌套路由和数据加载的网络瀑布问题。
- 🔧 **环境与指令**：Parcel 使用环境标识模块运行位置，"use client" 指令将模块环境切换为 `react-client` 并创建客户端引用。
- 🧩 **客户端组件打包**：多个客户端组件会被打包到同一文件中，减少 HTTP 请求数量。
- 🔗 **条件渲染与预加载**：动态导入的 RSCs 会自动预加载相关资源，优化加载性能。
- 🎨 **CSS 资源处理**：Parcel 自动将 CSS 注入 JSX 树，并通过 `ReactDOM.preinit` 提前加载，避免样式闪烁。
- 🔮 **未来展望**：未来将探讨 Server Actions 和渐进式加载导入映射等更多内容。

---

