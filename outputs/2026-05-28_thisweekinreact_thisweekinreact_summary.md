### [Meticulous AI - 无需编写测试的自动化前端测试](https://www.meticulous.ai/?utm_source=thisweekinreact&utm_medium=newsletter&utm_campaign=26q2&utm_content=1st)

**原文标题**: [Meticulous AI - Automated Frontend Testing Without Writing Tests](https://www.meticulous.ai/?utm_source=thisweekinreact&utm_medium=newsletter&utm_campaign=26q2&utm_content=1st)

Meticulous 是一个自动化、详尽且确定性的测试工具，旨在帮助开发者以极快的速度交付无缺陷代码，无需手动编写或维护测试。

- 🧪 **零开发者工作量**：只需添加脚本标签，Meticulous 会自动记录开发、暂存和预览环境中的用户交互，生成并维护测试套件。
- 🤖 **AI 驱动测试生成**：通过追踪代码分支执行，AI 引擎持续生成覆盖所有用户流程和边缘情况的视觉端到端测试。
- 🔍 **拉取请求即验证**：在合并前，Meticulous 会模拟后端响应，展示代码变更对用户工作流的影响，避免假阳性。
- ⚡ **闪电般快速测试**：测试在计算集群上高度并行化，可同时测试数千个屏幕，结果在 120 秒内返回。
- ❌ **彻底消除不稳定测试**：基于 Chromium 构建的确定性调度引擎，从根源上杜绝测试不稳定，并支持高速执行。
- 🔄 **自动演化测试套件**：测试随应用自动更新，新增功能或边缘案例时自动添加测试，过时测试自动移除，无需人工干预。
- 🏢 **企业级信赖**：被 Dropbox、Notion 等超过 100 家组织使用，工程师反馈“立即爱上，合并后无需调试，零维护”。
- 🔌 **广泛集成**：支持 NextJS、React、Vue、Angular、Nuxt、SvelteKit 等主流框架，可补充或替代现有测试套件。

---

### [Meticulous AI - 无需编写测试的自动化前端测试](https://www.meticulous.ai/?utm_source=thisweekinreact&utm_medium=newsletter&utm_campaign=26q2&utm_content=1st#:~:text=Once%20we%20started%20using%20Meticulous%2C%20we%20couldn%27t%20imagine%20working%20without%20it.)

**原文标题**: [Meticulous AI - Automated Frontend Testing Without Writing Tests](https://www.meticulous.ai/?utm_source=thisweekinreact&utm_medium=newsletter&utm_campaign=26q2&utm_content=1st#:~:text=Once%20we%20started%20using%20Meticulous%2C%20we%20couldn%27t%20imagine%20working%20without%20it.)

该平台提供零开发工作量的自动化、穷举且确定性测试工具，专为复杂代码库设计，可大幅提升代码发布速度。

- 🚀 **零开发工作量**：无需编写、修复或维护测试用例，测试套件随应用自动演化
- 🔍 **穷举验证**：AI 引擎追踪每次交互的代码分支，生成覆盖所有用户流程和边缘情况的视觉端到端测试
- ⚡ **极速测试**：测试在计算集群上高度并行化，1000+ 屏幕测试可在 120 秒内完成
- 🛡️ **零假阳性**：通过模拟后端响应（保存并重放原始记录），避免因数据变化导致的误报
- 🤖 **确定性调度引擎**：基于 Chromium 底层构建，彻底消除测试不稳定问题
- 🔗 **无缝集成**：支持 NextJS、React、Vue 等主流框架，只需添加录制脚本标签即可开始
- 📊 **兼容现有测试**：可补充或完全替代现有测试套件
- 💬 **行业验证**：被 Dropbox、Notion 等 100+ 组织采用，工程师反馈“无法想象没有它的工作”

---

### [逐一修复 JavaScript 可观测性库 | Sentry 博客](https://blog.sentry.io/fixing-javascript-observability/?utm_source=thisweekinreact&utm_medium=paid-community&utm_campaign=observability-fy27q2-evergreen&utm_content=newsletter-react-link-javascript-blog-learnmore)

**原文标题**: [Fixing JavaScript observability, one library at a time | Sentry Blog](https://blog.sentry.io/fixing-javascript-observability/?utm_source=thisweekinreact&utm_medium=paid-community&utm_campaign=observability-fy27q2-evergreen&utm_content=newsletter-react-link-javascript-blog-learnmore)

### 概述总结
JavaScript 可观测性正从脆弱的猴子补丁转向基于运行时内建 `TracingChannel` 的标准化方案，Sentry 正主导推动跨生态系统的库级采纳。

- 🐒 **猴子补丁的局限性**：现有 APM 工具依赖拦截 `require/import`，导致 ESM 兼容性差、无法在非 Node 运行时工作、与打包器冲突，且存在初始化顺序问题。
- 🛠️ **TracingChannel 方案**：利用 Node 内建 `diagnostics_channel` API，库只需发布结构化事件，APM 工具即可订阅，无需补丁，零开销，跨运行时兼容。
- 🤝 **生态共识与行动缺失**：社区普遍认可 TracingChannel 是未来，但缺乏推动库采纳的实际行动，Sentry 主动承担起主导工作。
- 🤖 **AI 辅助规模化**：使用 Claude Code 自动化研究、实现和跟踪，将单人多年的工作量转化为每日产出，同时保持人类主导架构决策与维护者沟通。
- ✅ **进展与里程碑**：已合并 10 个库（如 mysql2、node-redis、ioredis、unjs 生态），44 个目标库中 22 个尚未启动，关键 PR 针对 Express、PostgreSQL 等核心库。
- 🏢 **对 Sentry 的意义**：彻底解决 ESM 破坏、初始化顺序、运行时锁定和打包器冲突问题，简化插桩代码，惠及所有 APM 工具。
- 🔄 **飞轮效应启动**：库采纳后，社区自发构建纯 `diagnostics_channel` 订阅者（如 mysql2-otel-instrumentation），验证了方案的可持续性。
- 🗺️ **下一步计划**：推动 MongoDB、Prisma、Hono 等 20+ 库，设计共享映射器注册表以减少 APM 工具重复工作，最终实现库原生发射事件、社区维护映射器、APM 工具专注于数据分析的愿景。

---

### [React 服务端组件的组件架构 | Aurora Scharff](https://aurorascharff.no/posts/component-architecture-for-react-server-components/)

**原文标题**: [Component Architecture for React Server Components | Aurora Scharff](https://aurorascharff.no/posts/component-architecture-for-react-server-components/)

### 概述总结

本文探讨了从传统的客户端数据获取模式（如 `useEffect` 和 React Query）过渡到 React 服务端组件（RSC）的架构演进，重点阐述了如何通过 RSC 实现组件自包含、服务端数据获取和流畅的加载体验。

- 🚀 **服务端数据获取的优势**：服务端数据获取比客户端更快，因为它无需等待 JS 下载和执行，且能与渲染并行进行，减少了网络往返。
- 🔗 **传统模式的局限**：`useEffect` 和 React Query 虽能实现组件本地数据获取，但会导致“爆米花 UI”（内容随机弹出），且所有获取都在客户端进行。路由级加载器（如 Remix/Next.js Pages Router）虽将获取移至服务端，但会使组件与路由数据耦合，难以复用。
- 💡 **RSC 的核心价值**：RSC 允许每个组件在服务端异步获取自身数据，无需通过 props 传递，实现了真正的组件自包含和可复用性。`cache()` 函数可避免重复请求。
- 🧩 **构建加载体验**：通过 `Suspense` 边界和骨架屏，可以设计页面的加载顺序，避免布局偏移。骨架屏应与对应组件放在同一文件中，保持同步。
- 🛠️ **实际构建示例**：在 Next.js 中，通过 `Suspense` 包裹异步组件，并利用 `.then()` 处理 `params` Promise，保持页面同步。客户端交互（如点赞）通过 Server Function 和 `useOptimistic` 实现即时反馈。
- 📁 **代码组织**：采用按功能分组的文件夹结构（如 `features/post/`），组件仅接受最小 props（如 ID），便于复用和重构。
- 🎨 **错误处理与动画**：结合 `ErrorBoundary` 和 `ViewTransition`，为每个区域提供独立的错误处理和流畅的动画过渡。
- ⚡ **未来展望**：Next.js 16 的 `cacheComponents` 和 Partial Prerendering 将进一步提升性能，静态部分可即时渲染，动态部分流式加载。

---

### [TanStack 路由器和查询](https://tkdodo.eu/blog/tan-stack-router-and-query)

**原文标题**: [TanStack Router and Query](https://tkdodo.eu/blog/tan-stack-router-and-query)

TanStack Router 和 TanStack Query 的整合指南，探討如何結合兩者優勢進行數據管理。

- 🔗 **路由器緩存 vs 查詢緩存**：路由器緩存適用於路由專屬數據，但全局數據需用 TanStack Query 的全局查詢緩存，通過唯一 `queryKey` 跨路由共享。
- 🚀 **在加載器中使用查詢**：在路由加載器中調用 `queryClient.ensureQueryData` 或 `prefetchQuery` 可提前啟動數據獲取，確保組件渲染時數據已就緒，避免瀑布請求。
- ⚙️ **配置要點**：需將 `QueryClient` 添加到路由器上下文，並設置 `defaultPreloadStaleTime: 0` 關閉路由器內建緩存，避免緩存衝突。
- 🧩 **選擇 useSuspenseQuery 或 useQuery**：`useSuspenseQuery` 與路由器的 Suspense 邊界完美整合，適合阻塞數據；`useQuery` 用於非阻塞數據，可顯示內聯骨架加載器。
- ⏳ **加載器中的 await 決策**：不 `await` 加載器中的查詢，可將阻塞/非阻塞決策交給組件；`useSuspenseQuery` 自動處理阻塞，`useQuery` 處理延遲數據。
- 🌐 **SSR 支援**：使用 TanStack Start 時，`setupRouterSsrQueryIntegration` 自動將服務器數據流式傳輸到客戶端緩存；`useSuspenseQuery` 支援流式 SSR，無需額外 `await`。
- 🛑 **避免使用 useLoaderData**：查詢需通過 `useQuery` 或 `useSuspenseQuery` 創建觀察者，否則無法自動重新獲取、無效化後不更新，且可能被垃圾回收。
- 🎯 **將加載器視為事件處理器**：加載器僅用於觸發數據預取，不返回數據；組件始終依賴 `use(Suspense)Query`，確保查詢活躍並獲得完整功能。

---

### [从延迟到即时：现代化 GitHub Issues 导航性能 - GitHub 博客](https://github.blog/engineering/architecture-optimization/from-latency-to-instant-modernizing-github-issues-navigation-performance/)

**原文标题**: [From latency to instant: Modernizing GitHub Issues navigation performance - The GitHub Blog](https://github.blog/engineering/architecture-optimization/from-latency-to-instant-modernizing-github-issues-navigation-performance/)

GitHub Issues 团队通过客户端缓存、智能预取和服务工作线程，将页面导航延迟从秒级降至毫秒级，实现了近乎即时的用户体验。

- 🚀 **核心策略**：采用“陈旧时重新验证”（stale-while-revalidate）模式，优先从本地缓存渲染页面，再异步与服务器同步数据，大幅降低用户感知延迟。
- 💾 **IndexedDB 缓存**：将高频访问的 Issue 数据持久化到浏览器 IndexedDB 中，使约 22% 的 React 导航达到“即时”（<200ms）水平，缓存命中率约 33%。
- 🔥 **预加热机制**：在用户点击前，智能预取高概率访问的 Issue 数据，但仅当缓存中不存在时才发起网络请求，将缓存命中率提升至约 96%，70% 的 React 导航实现即时响应。
- ⚡ **服务工作线程**：拦截硬导航请求，利用缓存数据跳过服务器端渲染（SSR），显著加速 Turbo 导航和硬导航，尤其对 Turbo 路径效果显著。
- 📊 **性能提升**：HPC（最高优先级内容）指标全面改善，P10 从 600ms 降至 70ms，P25 从 800ms 降至 120ms，P50 从 1200ms 降至 700ms，中位数体验进入“快速”区间。
- 🎯 **权衡与未来**：接受约 4.7% 的数据陈旧率以换取速度，未来将优化冷启动路径，通过后端重写和边缘交付进一步减少 JavaScript 加载和客户端渲染瓶颈。

---

### [Linear 为何如此之快？技术解析](https://performance.dev/how-is-linear-so-fast-a-technical-breakdown)

**原文标题**: [How's Linear so fast? A technical breakdown](https://performance.dev/how-is-linear-so-fast-a-technical-breakdown)

### 概述总结
Linear 通过将数据库置于浏览器、本地优先同步、激进代码拆分和键盘优先设计，实现了毫秒级的响应速度，其核心是消除网络延迟对用户体验的影响。

- 🚀 **浏览器即数据库**：UI 直接从 IndexedDB 读取数据，本地修改后异步同步到服务器，彻底消除网络等待。
- ⚡ **即时首屏加载**：通过模块预加载、Service Worker 缓存、内联关键 CSS/JS 和字体优化，实现秒级启动。
- 🔄 **同步引擎三支柱**：本地数据立即可用、乐观更新无需等待网络、细粒度响应式更新（仅重绘变更的单元格）。
- 🎯 **键盘优先设计**：所有操作支持快捷键，全局命令面板（⌘K）基于本地内存搜索，无需网络请求。
- 🖌️ **克制动画**：仅对 GPU 加速属性（transform/opacity）进行动画，持续时间控制在 100ms 内，避免布局抖动。
- 🧩 **极简技术栈**：React + MobX + TypeScript + Postgres，无 SSR/边缘数据库等复杂架构，专注客户端渲染优化。
- 🔐 **乐观认证**：假设用户已登录，直接渲染本地数据，后台异步验证会话有效性。
- 📦 **极致代码拆分**：每个 npm 包独立分块，按需加载，支持离线使用。

---

### [一个核心，六个框架，零运行时抽象 | Formisch](https://formisch.dev/blog/one-core-six-frameworks/)

**原文标题**: [One core, six frameworks, zero runtime abstraction | Formisch](https://formisch.dev/blog/one-core-six-frameworks/)

### 概览总结
Formisch 是一个基于模式优先的表单库，支持 SolidJS、React、Vue、Svelte、Preact 和 Qwik 六大框架。其核心设计理念是“零运行时抽象”，通过在构建时替换框架原生响应式原语，实现框架原生集成、树摇优化和类型安全，无需运行时适配层。

- 🎯 **核心设计**：库仅依赖 `createSignal`、`batch`、`untrack` 和 `createId` 四个函数，在构建时根据目标框架动态替换实现，无运行时检测或适配器开销。
- 🔧 **构建时替换**：通过 Rolldown 插件，根据框架目标将 `framework/index.ts` 重定向到对应的 `index.{framework}.ts`，生成自包含的捆绑包。
- ⚡ **原生响应式集成**：在 Solid 中使用真实信号，Vue 中使用 `shallowRef`，Svelte 中使用 `$state`，Preact/Qwik 使用原生信号，React 使用轻量级 pub/sub（约100行），实现框架调度器原生追踪。
- 📦 **极致树摇优化**：每个表单操作（如 `setInput`、`validate`、`reset`）独立模块化，未使用的操作不会打包，核心保持最小体积。
- ✅ **单一类型源**：基于 Valibot 模式定义，自动推断路径、输入和输出的 TypeScript 类型，无需额外声明，确保类型一致性。
- 🌍 **跨框架共享**：核心代码（递归存储构建器、验证编排、方法集）在所有框架间共享，改进和修复惠及所有社区。
- 🚀 **零运行时抽象成本**：无需运行时适配层，无额外捆绑包体积，无调度/批处理冲突，实现框架原生性能。
- 🛠️ **快速上手**：提供浏览器内 playground，各框架独立指南，开源在 GitHub 上，支持社区贡献。

---

### [Skybridge：面向 MCP 应用与 MCP 服务器的全栈 React 框架 | Claude & ChatGPT](https://www.skybridge.tech/?utm_source=Third+Party&utm_medium=react+newsletter&utm_campaign=Skybridge+V1)

**原文标题**: [Skybridge, the full-stack React framework for MCP apps and MCP servers | Claude & ChatGPT](https://www.skybridge.tech/?utm_source=Third+Party&utm_medium=react+newsletter&utm_campaign=Skybridge+V1)

在过去的 24 小时内，我从模板仓库出发，为合作伙伴构建了三个生产级演示。Skybridge 模板的结构设计非常出色，与 Claude Opus 和 Codex 结合使用极为便捷。

- 🚀 从模板仓库到三个生产级演示，仅用 24 小时完成
- 🎨 Skybridge 模板结构设计优美，易于使用
- 🤖 与 Claude Opus 和 Codex 无缝集成，提升开发效率
- 💼 直接为合作伙伴生成可用的演示产品

---

### [Spiceflow — Spiceflow](https://getspiceflow.com/)

**原文标题**: [Spiceflow — Spiceflow](https://getspiceflow.com/)

Spiceflow 是一个类型安全的 API 框架和全栈 React RSC 框架，适用于 Node.js、Bun 和 Cloudflare Workers，以极致的简洁性和类型安全为核心。

- 🚀 **全栈 React 框架**: 支持 React Server Components (RSC)、服务端操作、布局和自动客户端代码分割。
- 🌍 **多运行时兼容**: 同一套代码可在 Node.js、Bun 和 Cloudflare Workers 上运行。
- ✅ **类型安全验证**: 通过 Zod 提供基于 schema 的类型安全请求和响应验证。
- 🔗 **类型安全客户端**: 提供类型安全的 `fetch` 客户端，可完全推断路径参数、查询、请求体和响应类型。
- 📄 **自动 OpenAPI 生成**: 基于路由定义自动生成 OpenAPI 3.1 规范文档。
- 🧠 **模型上下文协议 (MCP)**: 内置 MCP 插件，可将 API 路由作为工具和资源暴露给 AI 语言模型。
- 📡 **流式支持**: 支持通过 Server-Sent Events (SSE) 进行异步生成器流式传输。
- 🧩 **模块化设计**: 通过 `.use()` 方法挂载子应用，实现模块化设计。
- 📊 **内置 OpenTelemetry**: 内置 OpenTelemetry 追踪，零开销时自动禁用。
- 🛡️ **安全特性**: 提供认证、授权、输入验证、数据隔离等安全指南。
- 🧪 **测试支持**: 通过 `app.handle()` 直接测试，无需浏览器或构建步骤，反馈迅速。
- ⚡ **高性能**: 使用 Web 标准 `Request` 和 `Response`，架构简洁，性能优异。

---

### [Holocron — 开源文档站点生成器 — Holocron](https://holocron.so/)

**原文标题**: [Holocron — Open Source Documentation Site Generator — Holocron](https://holocron.so/)

Holocron 是一个开源的文档站点生成器，作为 Vite 插件运行，是 Mintlify 的替代品，支持本地构建和自托管。

- 📚 **Mintlify 兼容**：使用相同的 `docs.json` 配置、MDX 组件和 frontmatter 字段，迁移仅需约 2 分钟。
- ⚡ **快速上手**：通过 CLI 命令 `npx -y @holocron.so/cli create` 即可创建项目，或手动安装依赖并配置 `vite.config.ts`。
- 🛠️ **核心功能**：支持 OpenAPI 参考文档、Orama 搜索、深色模式、AI 导出（`/llms.txt`、`/docs.zip`、`.md` 路由）。
- 🚀 **部署灵活**：可部署到 Node.js、Cloudflare Workers 或 Holocron 托管服务，构建输出为标准 Node.js 服务器。
- 💰 **免费开源**：采用 MIT 许可证，无托管费用，支持本地 `vite build` 和标准 CI 流程。
- 📁 **项目结构**：包含 `index.mdx` 页面、`docs.json` 配置、`vite.config.ts` 和 `public/` 静态资源目录。
- 🔗 **AI 可读**：自动生成 `.md` 路由、`/llms.txt` 索引和 `/docs.zip` 下载，方便 AI 代理抓取内容。

---

### [GitHub - AndrewPrifer/liquid-dom: 液态玻璃网页效果 · GitHub](https://github.com/AndrewPrifer/liquid-dom)

**原文标题**: [GitHub - AndrewPrifer/liquid-dom: Liquid Glass for the Web · GitHub](https://github.com/AndrewPrifer/liquid-dom)

Liquid DOM 是一个用于 Web 液体玻璃渲染的 monorepo 项目，提供从底层渲染引擎到高层 React 绑定的完整工具链。

- 🧊 核心包 @liquid-dom/core 提供基于 DOM 的场景图、WebGPU 渲染器和玻璃效果类
- ⚛️ @liquid-dom/react 为 React 19 提供声明式布局和玻璃 API 绑定
- 🎨 @liquid-dom/three 支持在 Three.js WebGPU 渲染器上叠加液体玻璃层
- 🔗 @liquid-dom/r3f 集成 React Three Fiber，实现 React 驱动的 3D 玻璃 UI
- 📐 @liquid-dom/layout 提供独立于渲染器的 SwiftUI 风格布局引擎
- 🚀 安装灵活，可根据集成目标选择对应包（如 pnpm add @liquid-dom/core）
- 🖥️ 需要 WebGPU 支持，DOM 内容渲染需启用 Chrome 实验性 Canvas Draw Element 标志
- ⭐ 项目获得 1.9k 星标，主要使用 TypeScript 开发（占 95.6%）

---

### [TanStack Virtual 大幅提速，并终于支持 iOS | TanStack 博客](https://tanstack.com/blog/tanstack-virtual-perf-and-ios)

**原文标题**: [TanStack Virtual just got a lot faster, and finally handles iOS | TanStack Blog](https://tanstack.com/blog/tanstack-virtual-perf-and-ios)

以下是根据您提供的文章内容整理的摘要：

TanStack Virtual 发布了重大性能更新，修复了 iOS Safari 滚动问题，并引入了快照功能以改善滚动恢复体验。

- 🚀 **性能大幅提升**：冷挂载 10 万项列表从 6.1 毫秒降至 4.5 毫秒（React），`resizeItem` 风暴从 1.9 秒降至 1.3 毫秒，提升高达 1382 倍。
- 🐛 **修复尴尬 Bug**：修复了 `resizeItem` 中每次操作都克隆整个 Map 的问题（50 万次浪费操作），改用版本计数器后性能显著改善。
- 🧠 **优化对象分配**：对单通道列表改用 `Float64Array` 存储起始和大小，仅按需构造 `VirtualItem` 对象，减少内存分配，提升 50 万项列表性能（从 14 毫秒降至 2.7 毫秒）。
- 📱 **iOS Safari 滚动修复**：新增 iOS 专用代码路径，在触摸滚动期间延迟 `scrollTop` 写入，避免动量滚动中断，解决多年来的“滚动突然停止”问题。
- 🔄 **消除向后滚动卡顿**：根据滚动方向调整 `scrollTop` 写入，向后滚动时跳过调整，默认解决动态高度列表的“向上滚动时项目跳动”问题。
- 📸 **新增快照方法**：`takeSnapshot()` 返回当前测量项的快照，结合 `scrollOffset` 可实现精确的滚动恢复（如路由导航后）。
- 📊 **性能数据对比**：各项指标显著改善，包括 `setOptions` 渲染时间（从 14.4 毫秒降至 1.3 毫秒）和 `scrollToIndex` 精度（从 1 像素降至 0 像素）。
- 📦 **包体积微小增加**：约增加 900 字节 gzip，总大小约 6.1 kB，所有 91 个单元测试通过。
- 🔮 **未来计划**：将独立发布反向无限滚动（聊天场景）和 Fenwick 树内存重写（百万级列表），并已建立跨库基准测试套件。

---

### [聊天界面是列表，直到它们不再是 | TanStack 博客](https://tanstack.com/blog/tanstack-virtual-chat)

**原文标题**: [Chat UIs Are Lists Until They Aren't | TanStack Blog](https://tanstack.com/blog/tanstack-virtual-chat)

TanStack Virtual 新增了聊天 UI 专用的反向无限滚动功能，使虚拟列表能原生支持聊天场景的特殊需求。

- 🎯 **末端锚定**：`anchorTo: 'end'` 让列表末端成为稳定参考点，预加载旧消息时自动保持当前可见项位置不变
- 📌 **智能跟随**：`followOnAppend: true` 实现“仅在底部时自动跟随新消息，滚动历史时不跳转”的规则
- 📏 **可配置阈值**：`scrollEndThreshold: 80` 可调节“接近底部”的判断距离，并支持平滑滚动
- ⚡ **流式支持**：自动处理令牌流式输出时消息动态增长，保持末端锚定不漂移
- 🛠️ **实用 API**：提供 `isAtEnd()`、`getDistanceFromEnd()`、`scrollToEnd()` 等方法，方便构建“跳至最新”按钮
- 🔑 **稳定键要求**：需使用唯一 ID 作为 `getItemKey`，确保预加载后索引变化时仍能正确追踪消息
- 🧩 **无 UI 约束**：仍保持无头设计，不提供气泡、头像等 UI 组件，只处理滚动物理逻辑

---

### [2026 年 5 月 - 注册表包含与验证 - shadcn/ui](https://ui.shadcn.com/docs/changelog/2026-05-registry-include)

**原文标题**: [May 2026 - Registry Include and Validate - shadcn/ui](https://ui.shadcn.com/docs/changelog/2026-05-registry-include)

该文档介绍了 shadcn/ui 组件库的注册表系统及其相关功能。

- 📋 **概述**：文档涵盖组件列表、安装指南、主题配置、CLI 工具、注册表系统及表单集成等核心内容。
- 🧩 **组件库**：包含从 Accordion 到 Typography 的 60+ 个 UI 组件，如按钮、对话框、数据表格等。
- 🚀 **注册表更新**：2026 年 5 月新增 `include` 功能支持多文件组合注册表，以及 `shadcn registry validate` 命令用于发布前验证。
- 🔧 **注册表构建**：通过 `shadcn build` 将分散的 `registry.json` 文件合并为扁平化结构，保留原始文件路径。
- ✅ **验证功能**：`shadcn registry validate` 可检查根注册表、包含文件、项目模式、重复名称及本地文件路径等错误。
- 📂 **动态加载**：`shadcn/registry` 包提供 `loadRegistry` 和 `loadRegistryItem` 函数，支持动态注册表路由。
- 🌐 **部署支持**：文档推荐使用 Vercel 部署应用，并提及已被 OpenAI、Sonos、Adobe 等公司采用。

---

### [发布 ultracite@7.8.0 · haydenbleasel/ultracite · GitHub](https://github.com/haydenbleasel/ultracite/releases/tag/ultracite%407.8.0)

**原文标题**: [Release ultracite@7.8.0 · haydenbleasel/ultracite · GitHub](https://github.com/haydenbleasel/ultracite/releases/tag/ultracite%407.8.0)

概述摘要  
- 🌟 ultracite 7.8.0 版本发布，包含多项更新和修复。  
- 🆕 新增专为 TanStack 框架设计的预设，支持 Biome、ESLint 和 Oxlint 工具。  
- 🔄 现有用户需注意：TanStack Query 规则从 react 预设移至 tanstack 预设，需手动切换。  
- 🛠️ 修复 CLI 对 .biome.json 和 .biome.jsonc 配置文件的识别问题。  
- 🔒 增强 Husky 钩子安全性，防止文件名被误解析为 Git 选项。  
- 🐛 修复 Oxlint 配置中 ignorePatterns 未生效的问题，现已在根级别设置。  
- 📦 新增多项 Oxlint 规则支持，涵盖核心、React 和 Vitest 预设。  
- 🚫 添加文件写入保护，拒绝符号链接和项目根目录外的文件操作。  
- ✅ 验证包管理器名称，防止不安全值被用于钩子命令。

---

### [Apollo Client 4.2 新特性 - Apollo GraphQL 博客](https://www.apollographql.com/blog/whats-new-in-apollo-client-4-2)

**原文标题**: [What's New in Apollo Client 4.2 - Apollo GraphQL Blog](https://www.apollographql.com/blog/whats-new-in-apollo-client-4-2)

Apollo Client 4.2 发布，带来类型安全默认选项和事件驱动重新获取两大新功能。

- 🎯 **类型安全默认选项**：通过 TypeScript 模块增强声明默认选项，使运行时行为与类型匹配，避免因默认选项与类型不一致导致的崩溃风险。
- 🔄 **事件驱动重新获取**：引入 `RefetchEventManager`，支持窗口聚焦、网络重连等事件自动重新获取查询，并可自定义事件源和查询重获行为。
- 🚫 **泛型参数弃用**：为支持类型安全默认选项，推荐使用 `TypedDocumentNode` 替代泛型参数，以充分利用新特性。
- ⚙️ **灵活配置**：查询可通过 `refetchOn` 选项选择退出特定事件的重获，`RefetchEventManager` 支持扩展自定义事件和处理逻辑。

---

### [介绍上下文指令 | Lingui](https://lingui.dev/blog/2026/05/22/lingui-context-directives)

**原文标题**: [Introducing Context Directives | Lingui](https://lingui.dev/blog/2026/05/22/lingui-context-directives)

Lingui 引入 `lingui-set` 和 `lingui-reset` 指令，简化翻译上下文的批量声明，提升翻译质量与开发效率。

- 📝 **解决上下文重复问题**：新指令允许在代码块中一次性声明 `context`、`comment` 和 `idPrefix`，避免在每个宏调用中重复编写。
- 🌍 **上下文提升翻译准确性**：同一字符串在不同场景（如“保存”在设置页、支付表单）可能有不同译法，上下文帮助翻译者避免猜测，减少质量隐患。
- ⚙️ **指令支持合并与覆盖**：`lingui-set` 可累积设置，显式宏属性优先级更高；`lingui-reset` 清除所有上下文，空字符串可单独移除某参数。
- 🧩 **兼容 React/JSX 宏**：指令同样适用于 `<Trans>` 等 JSX 宏，通过注释即可批量应用上下文。
- 🏷️ **ID 前缀命名空间**：`idPrefix` 参数配合 `idPrefixLeader` 配置，可自动为以特定字符开头的 ID 添加前缀，实现灵活分组。
- 🚀 **新功能已可用**：`lingui-set` 和 `lingui-reset` 在最新 Lingui 版本中提供，欢迎通过 GitHub Discussions 反馈。

---

### [GitHub - nkzw-tech/fbtee: JavaScript 与 React 国际化框架。](https://github.com/nkzw-tech/fbtee)

**原文标题**: [GitHub - nkzw-tech/fbtee: The JavaScript & React Internationalization Framework. · GitHub](https://github.com/nkzw-tech/fbtee)

fbtee 是一个专为 JavaScript 和 React 构建的国际化框架，支持内联翻译、高效编译和现代工具链集成。

- 🌐 **内联翻译提升开发体验**：将翻译直接嵌入代码中，无需管理翻译键或使用 `t()` 函数，通过编译器自动提取字符串。
- 🚀 **经过生产验证**：基于 Facebook 的 fbt，拥有超过十年的生产使用经验，服务数十亿用户，并在 Athena Crisis 中持续运行。
- ⚡ **优化性能的 IR 编译**：将翻译编译为中间表示（IR）以提取字符串，并优化运行时输出，提升性能。
- 🛠️ **轻松集成多种工具**：快速与 Babel、SWC、Vite、Next.js 和 Expo 集成，支持 Node 22+ 和 React 19+。
- 📝 **丰富的字符串编写方式**：支持 `<fbt>`、`fbt()` 和 `fbs()` 编写字符串，并包含动态内容、复数、列表、枚举和代词等高级功能。
- 🔄 **完整的翻译工作流**：通过 `fbtee collect`、`fbtee prepare-translations` 和 `fbtee translate` 命令提取、准备和编译翻译文件。
- 🤖 **支持编码代理翻译**：利用 `prepare-translations` 标记新条目，代理可自动翻译并移除状态，保持代码整洁。
- 📦 **可选的 ESLint 插件**：安装 `@nkzw/eslint-plugin-fbtee` 以强制执行翻译包装规则，支持推荐和严格配置。
- 🔄 **从 fbt 迁移支持**：兼容核心编程模型，只需替换包和导入，并调整编译器命令即可完成迁移。

---

### [Fumapress 简介](https://press.fumadocs.dev/blog/introducing-fumapress)

**原文标题**: [Introducing Fumapress](https://press.fumadocs.dev/blog/introducing-fumapress)

### 概述总结
Fumapress 是一个基于 React.js 的内容站点生成器，旨在解决传统静态站点生成器在处理动态内容（如 CMS、评论、AI 聊天）时的局限性。它通过固定框架、自动路由、插件系统和高度灵活性，提供更优的开发体验，同时保留 Fumadocs 的模块化与可组合性。

- 🚀 **解决动态内容痛点**：传统静态生成器假设“静态文件=静态页面”，但实际站点常需集成 CMS、评论、AI 聊天等动态功能，Fumapress 专门为此优化。
- 🧩 **插件系统简化功能添加**：通过插件（如 flexsearch、llms、takumi）轻松扩展功能，无需手动管理路由或组件，实现“无脑”配置。
- ⚙️ **固定 React 框架与自动路由**：基于 Next.js 等固定框架，自动处理路由配置，降低决策成本，减少样板代码。
- 🔄 **继承 Fumadocs 的模块化设计**：复用 Fumadocs 的 UI、内容和创作系统，支持无缝集成自定义 CMS、搜索方案等，保持高度灵活性。
- 📄 **类型安全配置**：使用`press.config.tsx`文件，通过`defineConfig`和插件链式调用（如`.usePlugins()`），确保配置类型安全且可组合。
- 🎯 **最小抽象与最大灵活性**：相比 Fumadocs 的框架无关性，Fumapress 通过固定框架和插件系统，在牺牲少量灵活性的前提下，极大提升开发体验（DX）。

---

### [TanStack 的延迟水合是否具有革命性？ - YouTube](https://www.youtube.com/watch?v=_PB9rHndhU8)

**原文标题**: [Is TanStack Starts Deferred Hydration Revolutionary? - YouTube](https://www.youtube.com/watch?v=_PB9rHndhU8)

本頁面概述了 YouTube 平台的各項基本資訊與政策。

- 📰 新聞中心：提供 YouTube 最新消息與公告
- ©️ 版權：說明內容版權相關規範與保護機制
- 📞 聯絡我們：提供用戶與平台聯繫的管道
- 🎨 創作者：專為內容創作者提供的資源與支援
- 💰 刊登廣告：說明廣告合作與收益模式
- 👨‍💻 開發人員：提供 API 與技術整合資訊
- 📜 條款：用戶需遵守的使用條款與協議
- 🔒 私隱：個人資料保護與隱私政策說明
- 🛡️ 政策及安全：平台內容審核與安全規範
- ⚙️ YouTube 的運作方式：解釋平台推薦與運作機制
- 🧪 測試新功能：介紹平台正在測試的新功能
- 🏢 © 2026 Google LLC：版權歸屬與法律聲明

---

### [我测试了 Next.js Dev MCP（省得你亲自试） - YouTube](https://www.youtube.com/watch?v=OODK3KGUjDA)

**原文标题**: [I Tested Next.js Dev MCP (So You Don't Have To) - YouTube](https://www.youtube.com/watch?v=OODK3KGUjDA)

本頁面列出了 YouTube 平台相關的主要連結與政策資訊，包括版權、聯絡方式、創作者資源、廣告、條款及隱私等。

- 📰 新聞中心：提供 YouTube 官方新聞與公告
- ©️ 版權：說明版權相關規範與申訴機制
- 📞 聯絡我們：提供使用者與平台聯繫的管道
- 🎬 創作者：為內容創作者提供的資源與支援
- 📢 刊登廣告：介紹在 YouTube 上投放廣告的選項
- 📜 條款：列出使用 YouTube 服務的相關條款
- 🔒 私隱：說明使用者資料的收集與保護政策
- 🛡️ 政策及安全：規範平台使用行為與安全準則
- ⚙️ YouTube 的運作方式：解釋平台功能與推薦機制
- 🧪 測試新功能：介紹 YouTube 正在測試的新功能
- ©️ 2026 Google LLC：版權歸屬與年份標示

---

### [React 基础、AI 代理与框架的未来——与 Seth Webster 对话 - YouTube](https://www.youtube.com/watch?v=LZa3GIpX4l4)

**原文标题**: [React Foundation, AI Agents, and the Future of Frameworks w/ Seth Webster - YouTube](https://www.youtube.com/watch?v=LZa3GIpX4l4)

本頁面列出了 YouTube 平台相關的資訊與政策連結，包括版權、聯絡方式、創作者支援、廣告、條款、私隱及安全等核心內容。
- 📰 新聞中心：提供 YouTube 官方新聞與公告
- ©️ 版權：說明版權相關規範與權利
- 📞 聯絡我們：提供用戶聯絡 YouTube 的管道
- 🎬 創作者：為內容創作者提供資源與指引
- 📢 刊登廣告：介紹廣告刊登選項與政策
- 👨‍💻 開發人員：提供 API 與開發者工具
- 📜 條款：列出使用 YouTube 的服務條款
- 🔒 私隱：說明用戶資料保護與私隱政策
- 🛡️ 政策及安全：涵蓋社群規範與安全措施
- ⚙️ YouTube 的運作方式：解釋平台功能與演算法
- 🧪 測試新功能：介紹正在測試中的新功能
- ©️ 2026 Google LLC：版權歸屬聲明

---

### [TanStack Query 大规模应用实践：与 Dominik Dorfmeister (TkDodo) 对话 | 开源、Knip、Sentry 设计系统 - YouTube](https://www.youtube.com/watch?v=anz2xw4FY9c)

**原文标题**: [TanStack Query at Scale with Dominik Dorfmeister (TkDodo) | Open Source, Knip, Sentry Design System - YouTube](https://www.youtube.com/watch?v=anz2xw4FY9c)

本頁面列出了 YouTube 平台的相關資訊與政策連結，包括版權、聯絡方式、開發者條款及隱私政策等。
- 📰 新聞中心：提供 YouTube 的最新消息與公告
- ©️ 版權：說明內容使用與版權相關的規範
- 📞 聯絡我們：提供與 YouTube 團隊聯繫的管道
- 🎬 創作者：為內容創作者提供的資源與指南
- 📢 刊登廣告：介紹在 YouTube 上投放廣告的選項
- 👨‍💻 開發人員：提供 API 及技術開發相關資訊
- 📜 條款：列出使用 YouTube 服務的條款與條件
- 🔒 私隱：說明用戶資料的收集與使用方式
- 🛡️ 政策及安全：涵蓋社群規範與安全措施
- ⚙️ YouTube 的運作方式：解釋平台功能與運作機制
- 🧪 測試新功能：介紹 YouTube 正在測試的新功能
- ©️ 2026 Google LLC：版權歸屬與法律聲明

---

### [Agent Conf 2026 | 华沙 | 智能体开发](https://www.agent.sh/?utm_campaign=agent_conf&utm_source=twir&utm_medium=email&utm_content=cfp)

**原文标题**: [Agent Conf 2026 | Warsaw | Agentic Development](https://www.agent.sh/?utm_campaign=agent_conf&utm_source=twir&utm_medium=email&utm_content=cfp)

以下是对所提供内容的概述和要点总结：

本次会议聚焦于代理开发（Agentic Development）领域的范式转变，从人类驱动代码转向自主系统。会议将于 2026 年 9 月 17-18 日在波兰华沙举行，现正开放论文征集和门票购买。

- 📢 **论文征集已开放**：欢迎提交演讲提案，参与这一前沿技术盛会。
- 🎫 **门票购买中**：立即购票，锁定席位，参与华沙的代理开发大会。
- 🤖 **主题聚焦“代理开发”**：探讨从人类编码到自主系统的转变，塑造未来。
- 🧠 **四大核心主题**：涵盖 Vibe Coding、代理工程基础、多代理系统编排以及实际案例研究。
- 🌍 **主办方与社区**：由 Callstack 等组织主办，汇聚了 nader_dabit、Kent_C_Dodds 等行业领袖。
- 🏛️ **会议背景与使命**：延续 React Universe Conf 的成功经验，为代理时代打造专注、实践性的工程师会议。
- 📊 **过往成就**：10 年组织顶级 React Native 活动经验，服务 2 万 + 与会者，邀请 100+ 行业演讲者，与 30+ 合作伙伴合作。
- 🤝 **合作伙伴机会**：诚邀合作伙伴共同塑造代理开发的未来，联系 GUTEK@CALLSTACK.COM 获取合作资料。
- 📅 **关键日期与地点**：2026 年 9 月 17-18 日，波兰华沙。

---

### [Agent Conf 2026：演讲者征集 @ Sessionize.com](https://sessionize.com/agent-conf-2026/)

**原文标题**: [Agent Conf 2026: Call for Speakers @ Sessionize.com](https://sessionize.com/agent-conf-2026/)

Agent Conf 2026 是一个专注于自主 AI 代理开发的实践型会议，将于 2026 年 9 月 17 日至 18 日在波兰华沙举行，由 Callstack 组织，预计吸引 500 多名工程师参与。

- 🗓️ **会议时间**：2026 年 9 月 17 日至 18 日，为期两天
- 📍 **地点**：波兰华沙，线上线下同步进行
- 🎯 **主题**：聚焦自主 AI 系统开发，涵盖代理设计、提示技术、编排及 AI 驱动工作流
- 👥 **目标受众**：正在或希望掌握 AI 代理构建的工程师
- 📢 **演讲征集**：开放中，截止日期为 2026 年 6 月 20 日，优先原创内容（20 分钟演讲）
- ✨ **演讲主题**：包括新思路、实验方法、代理架构、高级提示、多代理系统、工具框架及生产案例
- 🏆 **演讲者福利**：全额会议门票、最高 1200 欧元差旅补助、3 晚酒店住宿及专属晚宴邀请
- ⏰ **关键日期**：征集开始于 2026 年 5 月 7 日，通知截止于 2026 年 6 月 30 日
- 🔗 **提交方式**：通过 Sessionize 登录（支持 Facebook、Google 等账号）

---

### [Expo SDK 56 - Expo 更新日志](https://expo.dev/changelog/sdk-56)

**原文标题**: [Expo SDK 56 - Expo Changelog](https://expo.dev/changelog/sdk-56)

Expo SDK 56 正式发布，带来多项重大更新和性能提升。

- 🚀 **核心升级**：基于 React Native 0.85 和 React 19.2，默认启用 Hermes v1 引擎，带来更快的启动速度和性能。
- 🎨 **Expo UI 稳定版**：Jetpack Compose (Android) 和 SwiftUI (iOS) API 现已稳定，并作为新项目默认模板，提供通用组件、稳定原生 API 和社区库替代方案。
- ⚡ **构建速度提升**：iOS 预编译 XCFrameworks 可减少约 16% 的构建时间；Android 预编译头文件实验性功能可带来高达 2.81 倍的 CMake 编译加速。
- 🛠️ **模块开发简化**：支持内联模块，可在项目内直接编写原生代码；新增类型生成工具和 revamped `create-expo-module`，提升开发体验。
- 📱 **运行时性能优化**：Android 使用 Kotlin 编译器插件替代反射，冷启动速度提升约 40%；iOS 采用新的 JSI 层，减少原生模块调用开销。
- 🔄 **文件系统增强**：`expo-file-system` 新增任务式上传/下载、进度报告、多文件选择等功能，并实验性支持文件系统事件监听。
- 🗺️ **Expo Router 独立**：不再依赖 React Navigation，引入新的原生堆栈 (Stack v5) 和工具栏支持，并支持 Web 流式 SSR。
- 🏗️ **EAS 服务升级**：EAS Build 提供构建时间统计，预编译热门社区库；预告即将推出性能监控服务 EAS Observe。
- 🧩 **其他重要更新**：新的 Calendar、Contacts、MediaLibrary API 稳定；iOS Widgets 稳定；类型安全配置插件；AI 友好的项目脚手架；Convex 集成等。

---

### [Expo UI 现已稳定：通过单一导入实现 SwiftUI 和 Jetpack Compose](https://expo.dev/blog/expo-ui-stable-sdk-56)

**原文标题**: [Expo UI is now stable: SwiftUI and Jetpack Compose from a single import](https://expo.dev/blog/expo-ui-stable-sdk-56)

概述：本文探讨了人工智能在医疗领域的应用，重点分析了其提升诊断效率、个性化治疗方案及数据隐私挑战等方面的关键影响。

- 🏥 人工智能通过分析医学影像（如 X 光、CT 扫描）辅助医生更快速准确地诊断疾病，减少误诊率。
- 💊 基于患者基因和病史数据，AI 可定制个性化治疗计划，优化药物剂量和疗效预测。
- 🔒 医疗数据共享引发隐私担忧，需加强加密技术和法规保护患者信息安全。
- 📈 AI 系统持续学习新病例，提升对罕见病的识别能力，但依赖高质量训练数据。
- 🤖 自动化流程（如病历整理、预约管理）减轻医护人员负担，提高医院运营效率。

---

### [Expo UI 中的 Worklet 集成：同步控制 SwiftUI 和 Compose 状态](https://expo.dev/blog/worklet-integration-in-expo-ui-synchronously-controlling-swiftui-and-compose-state)

**原文标题**: [Worklet integration in Expo UI: synchronously controlling SwiftUI and Compose state](https://expo.dev/blog/worklet-integration-in-expo-ui-synchronously-controlling-swiftui-and-compose-state)

概述：本文讨论了人工智能在医疗领域的应用，包括诊断辅助、药物研发和个性化治疗，同时强调了数据隐私和伦理挑战。  
- 🩺 人工智能可辅助医生进行疾病诊断，提高准确率和效率。  
- 💊 在药物研发中，AI 加速分子筛选和临床试验设计，缩短研发周期。  
- 🧬 个性化治疗通过分析患者数据，制定定制化医疗方案。  
- 🔒 数据隐私问题需严格保护，防止患者信息泄露。  
- ⚖️ 伦理挑战包括算法偏见和责任归属，需制定明确规范。

---

### [Expo SDK 56 新特性：Expo UI、内联 Swift/Kotlin 模块及更快的构建 - YouTube](https://www.youtube.com/watch?v=MKqGbv-Tssg)

**原文标题**: [What's New in Expo SDK 56: Expo UI, Inline Swift/Kotlin Modules, and Faster Builds - YouTube](https://www.youtube.com/watch?v=MKqGbv-Tssg)

本頁面為 YouTube 平台的相關資訊與政策總覽，涵蓋版權、聯絡方式、創作者資源、廣告、開發者條款、隱私與安全等核心內容，並標示版權歸屬 Google。

- 📰 新聞中心：提供 YouTube 官方新聞與公告
- ©️ 版權：說明版權相關規範與申訴機制
- 📞 聯絡我們：提供用戶與創作者的聯繫管道
- 🎬 創作者：為內容創作者提供資源與支援
- 📢 刊登廣告：介紹廣告合作與投放選項
- 👨‍💻 開發人員：提供 API 與開發工具資訊
- 📜 條款：列出使用 YouTube 的服務條款
- 🔒 私隱：說明個人資料處理與隱私保護政策
- 🛡️ 政策及安全：規範平台使用安全與內容政策
- ⚙️ YouTube 的運作方式：解釋平台推薦與審核機制
- 🧪 測試新功能：介紹 YouTube 正在測試的新功能
- ©️ 2026 Google LLC：標示版權歸屬於 Google 公司

---

### [4,063 个错误未经人工处理即关闭——PostHog 的经验教训](https://posthog.com/blog/agents-closed-4063-errors?utm_source=twir&utm_campaign=may27)

**原文标题**: [4,063 errors closed without a human opening PostHog – here's what we learned - PostHog](https://posthog.com/blog/agents-closed-4063-errors?utm_source=twir&utm_campaign=may27)

以下是您提供的文章摘要：

4,063 个错误在无人打开 PostHog UI 的情况下被 AI 代理关闭——以下是我们的经验总结

- 🤖 AI 代理在错误积压中执行三种不同任务：修复（4,063 个）、抑制（1,751 个）和路由（310 个），无需人工打开 UI。
- 🛠️ 更小、更精准的工具更有效：将单一端点拆分为三个独立工具后，批量处理流程显著更顺畅。
- 🔍 分类并非单一动作：修复、抑制和路由是三种不同的工作，需要不同的提示和成功标准。
- 📊 错误是起点而非终点：代理会深入事件、用户、功能标志和会话记录，跨产品调查而不中断上下文。
- 💡 搜索行为揭示意外发现：约一半搜索按业务表面（如结账、计费）组织，而非仅按错误类型，表明业务表面过滤需求强烈。
- ⏱️ 批量工作是真正节省时间的关键：如“抑制过去 90 天内所有第三方噪音变体”或“将所有 iOS 崩溃路由到移动团队”，一句话即可完成。
- 🎯 代理处理最佳的错误类型：前端噪音、网络/认证错误、业务领域错误和平台特定崩溃，各有针对性提示。

---

### [特性：重构服务器渲染 API - satya164 · 拉取请求 #13118 · react-navigation/react-navigation · GitHub](https://github.com/react-navigation/react-navigation/pull/13118)

**原文标题**: [feat: rework server rendering API by satya164 · Pull Request #13118 · react-navigation/react-navigation · GitHub](https://github.com/react-navigation/react-navigation/pull/13118)

此 PR 重构了 React Navigation 的服务器端渲染（SSR）API，以支持 React 19 的流式渲染。

- 🔄 将 SSR 相关 API 移至专用入口 `@react-navigation/native/server`
- 📦 引入新的 `ServerContainer` 组件，接受 `URL` 类型的 `location` 属性
- 🚀 使用 `renderToPipeableStream` 实现流式渲染，替代旧版 SSR 方式
- 🧹 移除旧的 `useCurrentRender` hook 和 `CurrentRenderContext`，简化 SSR 逻辑
- 🌐 更新 web linking，在 SSR 环境下避免创建浏览器历史记录
- 🧪 迁移 SSR 测试和示例服务器至流式渲染，并增加 E2E 测试覆盖
- ⏳ 当前版本暂不暴露标题、数据加载等功能，后续将通过静态配置实现

---

### [采用 React Native 0.82 DOM 节点 API，由 yaminyassin 提交 · 拉取请求 #475 · facebook/react-strict-dom · GitHub](https://github.com/facebook/react-strict-dom/pull/475)

**原文标题**: [Adopt React Native 0.82 DOM Node APIs by yaminyassin · Pull Request #475 · facebook/react-strict-dom · GitHub](https://github.com/facebook/react-strict-dom/pull/475)

此 Pull Request 将 react-strict-dom 升级以采用 React Native 0.82 的原生 DOM 节点 API，并使用原型委托替代代理来提升性能。

- 🚀 将 react-native 依赖提升至 >=0.82.0，并采用 RN 0.82 稳定的 DOM 节点 API
- 🛠️ 使用 `Object.create(node)` 原型委托替代 Proxy，解决 Hermes 无法内联 Proxy 陷阱的性能问题
- 📏 保留对 `nodeName`、`getBoundingClientRect`、`<img>.complete` 和输入选择 API 的 polyfill
- 🔄 通过原型链实现 `ownerDocument`、`getRootNode`、`parentNode` 等属性直接转发至 RN 节点
- 🆔 使用 WeakMap 保持节点身份缓存，确保同一 RN 节点始终返回相同的包装引用
- 🧪 新增 10 个原生引用测试，覆盖大写 nodeName、缩放、DOM 节点 API 透传等场景
- 📦 原生包体积减少约 363 字节（压缩后 69 字节），Web 构建保持不变
- ⚠️ 已知问题：`memoizedStrictRefs` 仅以 `node` 为键，未考虑 `viewportScale` 变化

---

### [RFC：为内置组件引用添加专用实例类型（JS API 稳定化） —— 由 huntie 提交 · 拉取请求 #1003 · react-native-community/discussions-and-proposals · GitHub](https://github.com/react-native-community/discussions-and-proposals/pull/1003)

**原文标题**: [RFC: Add dedicated Instance types for built-in component refs (JS API stabilization) by huntie · Pull Request #1003 · react-native-community/discussions-and-proposals · GitHub](https://github.com/react-native-community/discussions-and-proposals/pull/1003)

此 RFC 提案为 React Native 内置组件引入专用的*Instance 类型导出（如 ViewInstance、TextInputInstance），以提供规范化的 ref 类型定义方式。

- 📝 提案核心：为每个内置组件创建专用的*Instance 类型导出，作为 ref 类型的标准写法
- 🎯 解决痛点：填补了手写 TypeScript 类型中类声明隐藏的 API 空白，提供从`useRef<View>`到`useRef<ViewInstance>`的简洁迁移路径
- 🔧 影响范围：涉及所有 React Native 内置组件，是严格 TypeScript API 中用户迁移摩擦最大的变更
- ✅ 当前状态：已准备好审核，等待三位审核人批准合并
- 🔗 关联工作：已关闭相关兼容性修复 PR，并有对应的实现 PR 正在推进

---

### [React Native 键盘理解指南（第一部分）](https://blog.margelo.com/deep-dive-in-keyboard-handling)

**原文标题**: [The Go-To Guide for Understanding Keyboards in React Native (Part 1)](https://blog.margelo.com/deep-dive-in-keyboard-handling)

以下是您提供的文章摘要：

React Native 中键盘处理的核心挑战在于 iOS 和 Android 平台底层机制的差异，以及 Android 15 强制边缘到边缘显示带来的破坏性变化。文章深入剖析了这些差异，并提供了从基础组件到高级库的实用解决方案。

- 📱 **平台差异是根源**：iOS 提供“调度式”键盘动画（告知起始、结束和时长），而 Android（现代版）提供“逐帧”插值事件。任何忽略此不对称性的处理都会在其中一个平台上表现不佳。
- 🚨 **Android 15 强制改变规则**：从 Android 15 起，边缘到边缘显示被强制启用，系统不再自动调整窗口大小。依赖旧有 `adjustResize` 模式的代码（包括 React Native 自带的 `KeyboardAvoidingView`）会结构性失效。
- 🧩 **内置组件有局限**：React Native 的 `KeyboardAvoidingView` 基于 iOS 的调度合约构建，在 iOS 上表现流畅，但在 Android 上因缺乏逐帧信息、`LayoutAnimation` 不可靠及版本碎片化问题，表现不佳。
- ✨ **`react-native-keyboard-controller` 库提供统一方案**：该库通过将两个平台的生产模型映射到一个单一动画值上，提供了行为一致的 `KeyboardAvoidingView`，通常只需一行代码迁移即可修复跨平台键盘问题。
- 📜 **可滚动表单用 `KeyboardAwareScrollView`**：对于多输入框的长表单，该组件不仅追踪键盘，还追踪当前聚焦的输入框及其光标位置，确保输入始终可见，解决了 `KeyboardAvoidingView` 无法处理的场景。
- 📌 **固定元素用 `KeyboardStickyView`**：对于需要跟随键盘移动的页脚、按钮或工具栏，此组件仅通过平移元素来实现，避免了 `KeyboardAvoidingView` 重新调整整个布局带来的性能开销和副作用。

---

### [在 React Native 发布版本中分析 React 组件](https://www.callstack.com/blog/profile-react-components-in-react-native-release-builds)

**原文标题**: [Profile React Components in React Native Release Builds](https://www.callstack.com/blog/profile-react-components-in-react-native-release-builds)

概述摘要  
- 📱 **新库发布**：Callstack 推出@callstack/inspector 库，允许在 React Native 发布构建中分析组件性能。  
- 🚀 **核心优势**：无需原生代码更改，即可在接近生产环境（发布构建）中分析性能，避免调试代码干扰。  
- 🛠️ **设置步骤**：通过 Expo 应用示例演示，包括安装依赖、配置 Metro、创建自定义入口文件。  
- ⚙️ **运行与调试**：使用`npx inspector start`启动分析器，需在发布模式下运行应用（如`npx expo run:ios --configuration Release`）。  
- 📊 **扩展功能**：支持 React.Profiler 的 onRender 回调，可收集性能指标并本地记录或上传至分析服务。  
- 🌟 **开源贡献**：项目开源，欢迎在 GitHub 上查看文档并 Star。

---

### [一个适用于 Web 和原生应用的 React——Nicolas Gallagher 的笔记](https://nicolasgallagher.com/one-react-for-web-and-native/)

**原文标题**: [One React for Web and Native – Notes by Nicolas Gallagher](https://nicolasgallagher.com/one-react-for-web-and-native/)

### 概述总结
React Strict DOM 旨在通过统一 Web 和原生平台的 API，解决 React 生态系统的碎片化问题，实现跨平台代码共享，同时保持原生级体验。

- 🚀 **统一愿景**：React Strict DOM 通过标准化 Web API，让开发者能用一套代码同时构建 Web 和原生应用，消除“Web 或原生”的初始选择困境。
- ⚙️ **核心机制**：提供 `html` 和 `css` 模块，在 Web 上渲染标准 HTML/CSS，在原生平台映射为原生视图，并自动填充缺失功能（如 CSS 自定义属性、媒体查询）。
- 🧩 **解决碎片化**：React DOM 和 React Native 的割裂导致重复工作、学习成本高且阻碍 AI 应用。统一后可复用现有 Web 代码，降低迁移成本。
- 🏆 **生产验证**：Meta 的 VR 应用（60% 代码与 Web 共享）和 Zalando 的成功案例证明，该方法能实现高效开发与原生品质。
- 🔧 **技术基础**：React Native 新架构（JSI）支持同步布局、事件循环一致性及 Web API 原生实现，使 DOM 模拟成为可能。
- 📦 **迁移路径**：通过 Babel 自动代码转换（codemods），可逐步将现有 Web 或 React Native 代码迁移至 React Strict DOM，并保留平台特定“逃生舱”机制。
- 💡 **未来价值**：标准化 Web API 能降低 AI 编码复杂性，并确保技术栈长期稳定，符合行业发展趋势。

---

### [获取失败](https://www.npmjs.com/package/@nativescript/react-native)

**原文标题**: [Failed to retrieve](https://www.npmjs.com/package/@nativescript/react-native)

无法总结：获取内容失败，状态码 403。

---

### [宣布 lynx-ui - Lynx](https://lynxjs.org/next/blog/lynx-ui)

**原文标题**: [Announcing lynx-ui - Lynx](https://lynxjs.org/next/blog/lynx-ui)

## 概述总结
lynx-ui 正式公开发布，这是一个基于原生渲染、无样式组件库，结合 Web 开发速度与原生体验的开源 UI 框架。

- 🎉 **lynx-ui 正式发布**：自去年 12 月在 React Advanced London 预览后，经过数月打磨，现已全面可用。
- ⚡ **原生基础 + Web 速度**：基于内置元素和 XElement 实现原生渲染，同时提供 Web 风格的前端堆栈，兼顾性能与开发效率。
- 🧩 **可组合的原语组件**：组件为无样式原语，通过独立部分（如 PopoverRoot、PopoverTrigger）组合，支持自定义主题和设计系统。
- 🎨 **LUNA 设计语言**：参考设计语言，以 Lynx 渐变色调为基础，使用感性词汇（如 ambient、faint）描述表面质感。
- 🖱️ **可编程交互**：利用 Lynx 双线程模型和主线程脚本，实现逐帧响应的手势交互，如 Swiper 组件。
- 🎬 **Motion 动画支持**：适配 Web 动画库 Motion，通过 @lynx-js/motion 实现弹簧驱动动画，如 Sheet 组件。
- 📱 **多平台可用**：支持 iOS、Android 和 HarmonyOS，未来将扩展至 Web 和桌面端。
- 🚀 **立即使用**：可通过 Lynx Explorer 预览组件，或直接安装 @lynx-js/lynx-ui-* 包集成到项目中。

---

### [发布 Reanimated - 4.4.0 · software-mansion/react-native-reanimated · GitHub](https://github.com/software-mansion/react-native-reanimated/releases/tag/4.4.0)

**原文标题**: [Release Reanimated - 4.4.0 · software-mansion/react-native-reanimated · GitHub](https://github.com/software-mansion/react-native-reanimated/releases/tag/4.4.0)

React Native Reanimated 4.4.0 版本发布，带来了多项重要更新和修复。

- 🚀 引入 iOS CSS Core Animation 引擎，动画直接在 Core Animation 层运行，提升性能
- ⚙️ 集成新的动画后端，优化阴影树更新流程
- ⏱️ 新增 `useTimestamp` 钩子，提供每帧时间戳共享值，支持暂停和恢复
- 📱 Android 端使用预编译头文件，大幅减少 C++ 编译时间
- 🐛 修复弹簧动画抖动、动画取消竞态条件、CSS 过渡属性回退等问题
- ✨ 新增对 `placeholderTextColor`、`shadowColor`、`outlineColor` 等同步属性的支持
- 🔧 移除 JSC 运行时支持、旧版 CDP 调试器设置，清理冗余代码
- 📚 更新文档，添加 Expo SDK 55/56 版本支持
- 🎉 欢迎 5 位新贡献者加入

---

### [发布 Worklets - 0.9.1 · software-mansion/react-native-reanimated · GitHub](https://github.com/software-mansion/react-native-reanimated/releases/tag/worklets-0.9.1)

**原文标题**: [Release Worklets - 0.9.1 · software-mansion/react-native-reanimated · GitHub](https://github.com/software-mansion/react-native-reanimated/releases/tag/worklets-0.9.1)

react-native-reanimated 的 Worklets 库发布了 0.9.1 版本，主要带来了跨运行时 Promise 支持、统一的 Shareable 托管、以及多项开发者体验改进和错误修复。

- 🚀 **跨运行时 Promise 支持**：`runOnRuntimeAsync` 等返回 Promise 的函数现在可在所有运行时（Bundle 模式）使用，并优化了 C++ 中 JavaScript 回调的内存管理，减少内存占用并提升稳定性。
- 🔗 **统一的 Shareable 托管**：Shareable 现在可以在任何运行时上托管，不再仅限于 UI 运行时。
- 🛠️ **开发者体验改进**：将本地函数传递给 `scheduleOnRN` 不再导致应用崩溃，而是抛出可操作的 JavaScript 错误；在 Worklets 中抛出的错误会附加异步堆栈跟踪（可通过 `ENABLE_CROSS_RUNTIME_STACK_TRACES` 静态特性标志选择退出）；Bundle 模式下的控制台实现现在在 Worklet 运行时与 RN 运行时上打印对象的方式完全相同。
- 🐛 **其他修复与改进**：包括可序列化正则表达式、尊重 Worklets 中的相对引用、简化的 Bundle 模式设置、原生 ArrayBuffer 序列化支持、原生 Error 序列化、更好的错误消息、从 Java 迁移到 Kotlin、修复死锁和内存泄漏、以及多项代码清理和文档更新。
- 👥 **新贡献者**：多位新贡献者首次参与，包括 @tshmieldev、@avibega23、@mobinni 等。

---

### [GitHub - react-navigation/standard-navigation：导航库的标准导航API · GitHub](https://github.com/react-navigation/standard-navigation)

**原文标题**: [GitHub - react-navigation/standard-navigation: Standard navigation API for navigation libraries · GitHub](https://github.com/react-navigation/standard-navigation)

该仓库提供了一个标准导航 API，用于创建可与 React Navigation 和 Expo Router 等导航库协同工作的导航器。

- 📦 核心包仅包含最小化辅助工具和类型定义，实际集成由各导航库实现
- 🧩 通过`createStandardNavigator`函数创建导航器，支持三个泛型参数：NavigatorOptions、NavigatorEventMap 和 NavigatorProps
- 🗺️ 导航器回调函数接收 state（路由状态）、descriptors（路由描述器）、actions（导航动作）和 emitter（事件发射器）等属性
- 🔗 返回包含`type: 'standard'`、`version: 1`和`NavigatorContent`组件的对象，供 React Navigation 和 Expo Router 等库使用
- 🎯 state 对象包含当前焦点路由索引和路由数组，每个路由有 key、name、params 和 href 属性
- 📋 descriptors 对象映射路由 key 到包含 options 和 render 函数的描述器
- ⚡ actions 提供 navigate 和 back 方法，emitter 支持自定义事件发射（如 tabPress）并允许阻止默认行为
- 🌐 支持 Web 导航的 href 属性，事件系统包含 canPreventDefault 和 defaultPrevented 机制

---

### [发布 v2.5.0 · module-federation/core · GitHub](https://github.com/module-federation/core/releases/tag/v2.5.0)

**原文标题**: [Release Release v2.5.0 · module-federation/core · GitHub](https://github.com/module-federation/core/releases/tag/v2.5.0)

module-federation 核心库发布了 v2.5.0 版本，主要新增了可观测性插件、开发工具集成、Metro 支持改进以及多项错误修复。

- 🎉 新增可观测性插件，支持完整模块加载生命周期追踪
- 🔧 MF DevTools 集成可观测性功能
- 🚇 Metro 新增插件并迁移示例至 Rock 架构
- 🔍 运行时支持 getInstance 查找回调
- 📦 Metro 支持清单哈希用于原生缓存
- 🐞 修复 Metro 缺失变更集和 DTS 插件 URL 问题
- 🔄 优化 Metro 示例应用 Ruby 版本至 3.4.9
- 🔐 Metro 核心添加 SHA-256 哈希及可选缓存层集成
- 🛠️ 重构 DevTools 代理逻辑并清理工作流操作

---

### [发布 v0.6.0 · software-mansion-labs/react-native-enriched-markdown · GitHub](https://github.com/software-mansion-labs/react-native-enriched-markdown/releases/tag/0.6.0)

**原文标题**: [Release v0.6.0 · software-mansion-labs/react-native-enriched-markdown · GitHub](https://github.com/software-mansion-labs/react-native-enriched-markdown/releases/tag/0.6.0)

此版本为 react-native-enriched-markdown 库的 v0.6.0 发布，包含多项新功能、错误修复、重构和文档改进。

- ✨ **新增功能**：支持自定义选中颜色、GFM 流式渲染表格和块级数学、上下标、提及功能，以及创建测试平台和 Storybook。
- 🐛 **修复与改进**：修复了 Android 上背景在引用块中显示、iOS 上删除混合选区崩溃、Web 上数学公式嵌套问题，以及多个平台上的动画和渲染错误。
- 🔧 **重构**：集中化了选中颜色应用、样式注入和事件处理逻辑，并重构了渲染器基类和异步渲染协调器。
- 📚 **文档与杂项**：更新了 API 参考、兼容性表格，添加了 E2E 测试和 Maestro 测试框架，并升级了示例应用中的 React Native 版本。
- 🆕 **新贡献者**：欢迎 xindixu、istarkov、mgmx-io、radoslawrolka、rhnmht30 和 bobbyg603 的首次贡献。

---

### [发布 · gronxb/hot-updater · GitHub](https://github.com/gronxb/hot-updater/releases)

**原文标题**: [Releases · gronxb/hot-updater · GitHub](https://github.com/gronxb/hot-updater/releases)

hot-updater v0.32.0 版本发布，引入了内容寻址存储、Android 原生配置优化和 Cloudflare R2 存储改进，同时 v0.31.0 版本带来了包差异更新功能，大幅减小 OTA 更新体积。

- 📦 **内容寻址存储**：通过内容哈希去重，部署时只上传真正变更的资源，减少重复上传，提升部署效率并降低成本
- 🤖 **Android 原生配置迁移**：将配置值写入 `AndroidManifest.xml` 元数据，避免因本地化导致的渠道识别错误，保持向后兼容
- ☁️ **Cloudflare R2 存储改进**：改用 S3 兼容 API 进行部署，解决大包体上传慢的问题，需创建新的 R2 凭证
- 🔍 **Expo Fingerprint 可选依赖**：改为可选依赖，避免 Expo Doctor 警告，需手动安装 `@expo/fingerprint`
- 📉 **包差异更新**：v0.31.0 引入，仅下载变更文件，Hermes 补丁平均缩小 97.2%，大幅减少 OTA 更新体积
- 🛠️ **CLI 命令增强**：新增 `hot-updater doctor` 检查基础设施、`hot-updater rollback` 回滚、`hot-updater bundle promote` 提升版本，以及 `HotUpdater.init` 简化初始化
- 🎯 **目标群体发布**：v0.30.0 稳定目标群体功能，支持针对特定组进行发布，修复了原有 1-100% 发布的问题

---

### [Maestro CLI 2.6.0：推出 Maestro Viewer](https://maestro.dev/blog/maestro-cli-v2-6-0)

**原文标题**: [Maestro CLI 2.6.0: introducing Maestro Viewer](https://maestro.dev/blog/maestro-cli-v2-6-0)

Maestro CLI 2.6.0 发布，重点推出 Maestro Viewer，让 AI 编码代理拥有移动设备，同时带来多项性能优化和修复。

- 📱 **Maestro Viewer**：在 AI 编码代理中嵌入 iOS 模拟器、Android 模拟器或物理设备，实时显示命令执行过程，支持直接与设备交互。
- ⚡ **并行 iOS 模拟器执行**：新增设备会话跟踪、跨进程文件锁定和端口检查，支持多模拟器同时运行测试。
- ❌ **移除内置 Studio**：CLI 中捆绑的 Web 版 Maestro Studio 已移除，推荐使用 Maestro Viewer 或桌面版 Studio。
- 🔧 **移除 Rhino JS 引擎**：完全替换为 GraalJS，用于执行`evalScript`和`runScript`。
- 📝 **更好的 YAML 解析错误**：错误信息精确到行和列，输出格式更清晰。
- 🧹 **更简洁的路径显示**：步骤描述和错误信息使用相对路径，CLI 和 Cloud 输出格式一致。
- 📁 **iOS XCTest 日志集成**：测试失败时，XCTest 日志自动打包到 Maestro 调试输出目录。
- 📊 **`maestro hierarchy`输出纯 JSON**：移除混合可读标题，可直接管道到`jq`或脚本处理。
- 🚀 **截图取消更快**：按 Ctrl+C 时不再延迟清理。
- ⚙️ **跳过冗余设备读取**：只读命令（如`assertVisible`）后不再重新读取 UI 层次，提升含大量断言的流程速度。
- 📈 **HTML 报告增强**：包含 Cloud 运行链接和应用二进制 ID，便于审计。
- 🏷️ **JUnit XML 改进**：新增`file`属性，`id`和`classname`可配置，支持 CI 工具分组过滤。
- 🤖 **MCP `cheat_sheet`无需 Cloud 认证**：返回命令文档的工具不再要求登录。
- 🖼️ **MCP `take_screenshot`自动缩小**：避免 LLM 图像令牌限制，减少浪费。
- 🐛 **修复`assertScreenshot`匹配百分比**：错误消息中的百分比与配置阈值使用相同标准。
- 🔧 **修复 Android WebView 层次为空**：`devtools`模式下 WebView 元素可正常识别和点击。
- 💡 **更友好的错误提示**：无效超时和空环境变量值给出明确解释，而非通用堆栈跟踪。
- ⏳ **弃用`--android-api-level`和`--ios-version`**：建议改用`--device-os`，v2.6.0 会发出弃用警告。

---

### [发布 v0.9.0 · software-mansion/react-native-executorch · GitHub](https://github.com/software-mansion/react-native-executorch/releases/tag/v0.9.0)

**原文标题**: [Release v0.9.0 · software-mansion/react-native-executorch · GitHub](https://github.com/software-mansion/react-native-executorch/releases/tag/v0.9.0)

React Native ExecuTorch v0.9.0 版本发布，带来了语音、视觉和自然语言处理方面的多项改进和新功能。

- 🔒 语音识别性能提升高达 10 倍，并新增 VAD（语音活动检测）集成
- 🌍 文本转语音支持多语言，包括波兰语、西班牙语、意大利语、法语和印地语
- 🎤 新增 VAD 流式 API，支持连续语音活动检测
- 🛡️ 自然语言处理新增 OpenAI 隐私过滤器 API，可本地检测私人信息
- 📝 支持多语言文本嵌入生成
- 🤖 新增 Qwen 3.5 模型支持
- 👁️ 计算机视觉新增姿态估计 API，基于 YOLO 26
- 🖼️ FastSAM 支持点、框或文本提示驱动的分割掩码
- ⚙️ ExecuTorch 运行时升级至 v1.2.0
- 📦 新增类型化模型注册表，便于后端/精度选择
- 🔧 扩展分词器支持，包括 unigram 和 word-level
- 📱 Android 支持 32 位/不兼容 ABI 的优雅降级
- 🚨 破坏性变更：TextToImage 返回文件 URI 而非 base64，多语言 TTS API 重构等

---

### [发布 8.12.0 · getsentry/sentry-react-native · GitHub](https://github.com/getsentry/sentry-react-native/releases/tag/8.12.0)

**原文标题**: [Release 8.12.0 · getsentry/sentry-react-native · GitHub](https://github.com/getsentry/sentry-react-native/releases/tag/8.12.0)

sentry-react-native 8.12.0 版本发布，主要新增多实例协调、触摸面包屑标签自动注入等功能，并修复了多项问题。

- 🎉 **多实例协调**：新增 `ready` 属性，支持多个 `<TimeToFullDisplay>` 实例协调，仅当所有实例报告 `ready === true` 时记录 TTID/TTFD
- 🏷️ **触摸面包屑标签**：从触摸组件的子文本内容提取标签，并支持在构建时自动注入 `sentry-label`
- 🔧 **自定义文本组件**：新增 `textComponentNames` 选项，用于 `annotateReactComponents` 配置
- 📱 **Expo Router 集成**：新增 `expoRouterIntegration()` 并支持自动注册
- 🎥 **Android 会话回放**：实验性暴露 `captureSurfaceViews` 选项
- 🐛 **问题修复**：修复重复 HTTP 面包屑、iOS 新架构重复 JS 错误报告、Android 布尔选项忽略、Metro 配置崩溃等问题
- ⬆️ **依赖更新**：升级 JavaScript SDK 至 v10.53.1、CLI 至 v3.4.2、Android SDK 至 v8.42.0 等

---

### [发布 v1.7.0 · uni-stack/uniwind · GitHub](https://github.com/uni-stack/uniwind/releases/tag/v1.7.0)

**原文标题**: [Release Release v1.7.0 · uni-stack/uniwind · GitHub](https://github.com/uni-stack/uniwind/releases/tag/v1.7.0)

概述：UniWind v1.7.0 版本发布，包含错误修复、重构和杂项改进。

- 🐛 修复：不再解析 `flex: 1` 的问题（由 @Brentlok 在 #543 中修复）
- 🔨 重构：主要打包器重构（由 @Brentlok 在 #523 中完成）
- 🏠 杂项：静默 SSR 的 CSS 变量警告（由 @Brentlok 在 #539 中处理）
- 🚀 获得 2 个火箭表情反应（来自 SpasiboKojima 和 karume-lab）

---

### [介绍 Apex：一款专为 React Native 打造的快速专用模型](https://www.callstack.com/blog/introducing-apex-a-fast-specialized-model-for-react-native)

**原文标题**: [Introducing Apex: A Fast, Specialized Model for React Native](https://www.callstack.com/blog/introducing-apex-a-fast-specialized-model-for-react-native)

Callstack 发布了 Apex，一个专为 React Native 开发优化的 AI 编码模型，旨在提供更快、更精准的框架特定支持，并已开始内测。

- 🚀 **Apex 发布**：Callstack 宣布推出 Apex，这是专为 React Native 编码工作训练的模型，能提供更快、更精准的框架特定答案，并降低推理成本。
- 💡 **专业化趋势**：AI 编码市场正转向可持续计算，小型优化模型（如 Cursor 和 Windsurf）在特定领域能显著改善成本与性能比，React Native 开发因此受益。
- 🎯 **构建原因**：React Native 开发涉及多平台约束，通用模型常忽略框架细节；Apex 旨在原生理解这些细微差别，减少工具调用和提示构建的需求。
- ✅ **当前能力**：Apex 并非替代所有前沿模型，而是专注于 React Native 领域，通过 React Native Evals 评估，在特定领域提供显著更优的性能与成本比。
- 🛠️ **训练方法**：基于 Gemma 4 模型，使用监督微调（SFT）和组相对策略优化（GRPO），训练数据精心挑选自近期 GitHub 仓库和 React Native 生态系统。
- ⚡ **速度与运行**：速度源于模型架构和专用集群（4-8 块 NVIDIA RTX PRO 6000 GPU），生成速度达 2000-4000+ tokens/秒，且因模型内嵌更多知识，减少了搜索和工具调用时间。
- 🔒 **托管与安全**：通过 Vast.ai 安全云托管，使用已验证的数据中心提供商，兼顾成本灵活性和企业级安全要求。
- 📅 **未来计划**：目前仅对选定团队开放私密测试，以优化体验和收集反馈，待法律和运营事宜完成后将作为更广泛的公共服务推出。

---

### [GitHub - margelo/react-native-skills: 最佳 React Native 代理技能。忘掉 10 倍，这是 100 倍。](https://github.com/margelo/react-native-skills)

**原文标题**: [GitHub - margelo/react-native-skills: The best react-native Agent Skills. Forget 10x, this is 100x. · GitHub](https://github.com/margelo/react-native-skills)

margelo/react-native-skills 是一个宣称能极大提升开发效率的 React Native 代理技能库，通过简单的安装命令即可添加多种技能。

- ⭐ 项目获得 106 颗星，受到社区关注
- 🔧 提供“最佳”React Native 代理技能，号称效率提升 100 倍
- 📦 安装简单：运行 `npx skills add margelo/react-native-skills` 后交互式选择技能
- 📁 仓库包含 skills 文件夹、.gitignore 和 README 文件，共 17 次提交
- 🚫 无正式发布版本或包，处于早期开发阶段
- 👀 有 2 个观察者和 3 个分支，社区参与度有限

---

### [App.js Conf 2026 - YouTube](https://www.youtube.com/playlist?list=PLSk21zn8fFZCE_TlHUVnTVMm7mNl_fzxl)

**原文标题**: [App.js Conf 2026 - YouTube](https://www.youtube.com/playlist?list=PLSk21zn8fFZCE_TlHUVnTVMm7mNl_fzxl)

本頁面為 YouTube 平台的綜合資訊頁，涵蓋了版權、聯絡方式、政策條款及平台運作等核心內容。
- 📰 新聞中心：提供 YouTube 官方新聞與最新動態
- ©️ 版權：說明內容版權相關規範與權利保護
- 📞 聯絡我們：提供用戶與平台聯繫的管道
- 🎨 創作者：專為內容創作者提供的資源與支援
- 📢 刊登廣告：介紹廣告投放選項與合作機會
- 👨‍💻 開發人員：提供 API 與技術開發相關資訊
- 📜 條款：列出使用 YouTube 服務的條款與條件
- 🔒 私隱：說明個人資料收集與使用政策
- 🛡️ 政策及安全：涵蓋平台安全規範與社群準則
- ⚙️ YouTube 的運作方式：解釋平台功能與內容推薦機制
- 🧪 測試新功能：介紹正在測試中的新功能與實驗
- ©️ 2026 Google LLC：版權歸屬與法律聲明

---

### [@tc39.es 在 Bluesky 上](https://bsky.app/profile/tc39.es/post/3mmhlitpxrq2a)

**原文标题**: [@tc39.es on Bluesky](https://bsky.app/profile/tc39.es/post/3mmhlitpxrq2a)

本週 TC39 第 114 次會議推進多項 ECMAScript 提案，涵蓋原子操作、迭代器、國際化及正則表達式等領域。

- 🎉 Atomics.pause 進入第 4 階段，提供原子操作暫停功能
- 🔗 Joint iteration 進入第 4 階段，實現聯合迭代
- ⚠️ Error stack accessor 進入第 3 階段，標準化錯誤堆疊訪問
- 🔢 Intl: Keep Trailing Zeros 進入第 3 階段，保留數字尾隨零
- 📦 Iterator Chunking 進入第 3 階段，支援迭代器分塊處理
- ✅ Iterator Includes 進入第 3 階段，檢查迭代器是否包含元素
- ➕ Iterator Join 進入第 3 階段，連接迭代器元素
- 🔤 RegExp Buffer Boundaries 進入第 3 階段，新增正則表達式邊界匹配
- 💰 Amount 進入第 2 階段，處理金額相關功能
- 🌐 Intl Sequence Units 進入第 2 階段，支援序列單位國際化

---

### [特性：`allowScripts` 可选安装脚本策略的第一阶段 —— JamieMagee · 拉取请求 #9360 · npm/cli · GitHub](https://github.com/npm/cli/pull/9360)

**原文标题**: [feat: Phase 1 of `allowScripts` opt-in install-script policy by JamieMagee · Pull Request #9360 · npm/cli · GitHub](https://github.com/npm/cli/pull/9360)

npm 引入 `allowScripts` 策略，让依赖安装脚本变为可选加入，第一阶段仅提供警告，不实际阻止脚本运行。

- 📦 新增 `package.json` 中的 `allowScripts` 字段，用于管理依赖安装脚本的审查状态
- ⚙️ 添加三个新配置项：`allow-scripts`、`strict-script-builds` 和 `dangerously-allow-all-scripts`，后两个为预留项
- ✅ 引入 `npm approve-scripts` 和 `npm deny-scripts` 命令，支持不对称锁定规则（批准可锁定版本，拒绝仅限名称）
- ⚠️ 在 `npm install`、`ci`、`update` 和 `rebuild` 后显示建议性警告，列出未审查的安装脚本包
- 🔍 身份匹配器支持注册表、Git、文件和远程 tarball，注册表身份从锁文件的 `resolved` URL 派生
- 🏷️ 别名匹配底层注册包而非别名名称，确保安全性
- 🚫 捆绑依赖的安装脚本标记为未审查，且在第一阶段无法被列入白名单
- ⚡ 非根工作区声明自己的 `allowScripts` 时会发出警告
- 🔮 实际阻止脚本运行推迟到第二阶段，届时将基于匹配器控制构建集

---

### [GitHub - WICG/persistent-iframes · GitHub](https://github.com/WICG/persistent-iframes)

**原文标题**: [GitHub - WICG/persistent-iframes · GitHub](https://github.com/WICG/persistent-iframes)

### 概述摘要
该提案旨在通过`persist`属性和匹配的`id`，允许跨源 iframe 在父页面的同源导航中存活，从而解决硬导航导致 iframe 状态丢失的问题，减少 MPA 与 SPA 架构间的性能差距。

- 🛠️ **问题核心**：硬导航会销毁所有子 iframe，导致复杂状态（如聊天、媒体播放器）丢失，影响 MPA 架构性能。
- 💡 **解决方案**：通过`persist`属性和匹配`id`，使 iframe 在同源导航后保留并重新附加到新文档。
- 🔒 **安全限制**：仅限同源导航，跨源导航时 iframe 立即终止。
- ⏳ **渲染时机**：iframe 需在首屏渲染前匹配并重新附加，开发者可通过`<link rel=expect>`延迟渲染。
- ❓ **未决问题**：是否限制为跨源或进程隔离的 iframe 以简化规范？能否扩展到跨源导航？
- 📊 **项目状态**：WICG 仓库，3 星，4 关注，0 分叉，1 贡献者（Yoav Weiss）。

---

### [CSS 与 JavaScript • Josh W. Comeau](https://www.joshwcomeau.com/animation/css-vs-javascript/)

**原文标题**: [CSS vs. JavaScript • Josh W. Comeau](https://www.joshwcomeau.com/animation/css-vs-javascript/)

本文探讨了 CSS 与 JavaScript 动画的性能差异，并提供了选择合适工具的建议。

- 🎯 **CSS 动画优于 JS 循环**：CSS 关键帧动画运行在独立线程，不受主线程阻塞影响；而基于`requestAnimationFrame`的 JS 动画会因主线程繁忙而卡顿。
- ⚡ **现代动画库的差异**：Motion 库利用 Web Animations API（WAAPI）实现类似 CSS 的独立线程运行，避免卡顿；GSAP 则仍受主线程限制，且可能因帧延迟导致动画不同步。
- 📦 **库的下载成本可接受**：虽然 Motion（48kB）和 GSAP（27kB）需下载解析，但除非需要即时页面动画，否则对用户体验影响不大。
- 🔧 **优先选择 CSS 原生方案**：现代 CSS 已支持 View Transitions、`linear()`和 Animation Timeline 等强大功能，多数场景无需 JS 库。
- 💡 **区分两类动画库**：第一类（如 Motion、GSAP）扩展动画能力（如 SVG 变形），值得使用；第二类仅封装 CSS 基础功能，不推荐。
- 🎓 **课程推广**：作者推出《Whimsical Animations》课程，教授现代 CSS、JS、SVG 和 Canvas 动画设计，目前春季促销可省$150。

---

### [npm 的分阶段发布与新的安装时控制 - GitHub 更新日志](https://github.blog/changelog/2026-05-22-staged-publishing-and-new-install-time-controls-for-npm/)

**原文标题**: [Staged publishing and new install-time controls for npm - GitHub Changelog](https://github.blog/changelog/2026-05-22-staged-publishing-and-new-install-time-controls-for-npm/)

npm 推出分阶段发布与新的安装源控制功能，强化供应链安全。

- 📦 **分阶段发布正式可用**：npm 11.15.0 及以上版本支持分阶段发布，将包上传到暂存队列，需维护者通过 2FA 批准后才能安装，增强发布安全性。
- 🔒 **推荐搭配可信发布使用**：建议将分阶段发布与 OIDC 可信发布结合，可限制 CI 工作流仅允许 `npm stage publish`，提升自动化流程的安全性。
- 🛠️ **新增安装源控制标志**：在 `--allow-git` 基础上，新增 `--allow-file`、`--allow-remote` 和 `--allow-directory` 标志，可分别控制本地文件、远程 URL 和本地目录的安装来源。
- ⚙️ **灵活配置与未来默认值变更**：每个标志可设为 `all` 或 `none`，并支持在 `.npmrc` 或 `package.json` 中配置。未来 npm CLI v12 中 `--allow-git` 默认值将改为 `none`。
- 💬 **社区反馈与讨论**：欢迎在 GitHub 社区讨论中分享使用体验和问题。

---

### [pnpm 11.3 | pnpm](https://pnpm.io/blog/releases/11.3)

**原文标题**: [pnpm 11.3 | pnpm](https://pnpm.io/blog/releases/11.3)

pnpm 11.3 版本发布，新增了 npm 的分阶段发布功能、信任锁文件设置以及多个原生命令实现，并优化了内存使用和修复了多个问题。

- 📦 新增 `pnpm stage` 命令，支持 npm 的分阶段发布工作流，包括发布、列表、查看、批准、拒绝和下载子命令
- 🔒 新增 `trustLockfile` 设置，可跳过锁文件中 `minimumReleaseAge` 和 `trustPolicy` 的验证，默认关闭
- 🧠 优化了 `minimumReleaseAge` 和 `trustPolicy` 验证的内存占用，仅缓存必要字段，避免大型工作区内存溢出
- 🛠️ 原生实现了 `pnpm pkg`、`pnpm repo` 和 `pnpm set-script` 命令，不再依赖 npm
- 🏷️ 为 `pnpm pack` 和 `pnpm publish` 新增 `--skip-manifest-obfuscation` 标志，保留原始 `packageManager` 字段和生命周期脚本
- 🐛 修复 `pnpm dlx` 在缺失 `package.json` 时失败的问题，现在会回退到无作用域包名
- 🔄 修复 `pnpm dedupe` 和 `pnpm install` 在处理具有传递性对等依赖的包时锁文件非确定性问题
- ✅ 修复 `pnpm add <github-shorthand>` 被静默忽略的问题
- 🧹 修复 `pnpm add --config` 在 `pnpm-lock.env.yaml` 中留下孤立条目的问题

---

### [Deno 2.8](https://deno.com/blog/v2.8)

**原文标题**: [Deno 2.8 | Deno](https://deno.com/blog/v2.8)

Deno 2.8 发布，这是迄今为止最大的次要版本，带来了大量新功能、性能提升和 Node.js 兼容性改进。

- 🚀 **新子命令**：新增 `deno audit fix`（自动修复漏洞）、`deno bump-version`（自动更新版本号）、`deno ci`（可重现的 CI 安装）、`deno pack`（打包为 npm tarball）、`deno transpile`（仅转译 TypeScript）、`deno why`（解释依赖来源）。
- 📦 **默认 npm 前缀**：`deno add` 和 `deno install` 现在默认将无前缀名称视为 npm 包，无需再手动添加 `npm:` 前缀。
- ⚡ **性能飞跃**：冷 npm 安装速度提升 3.66 倍，`node:http` 吞吐量提升 2.21 倍，`node:buffer` base64 编码速度提升 3.07 倍，`node:crypto` scrypt 速度提升 2.12 倍。
- 🧩 **Node.js 兼容性**：Node.js 官方测试套件通过率从 42% 提升至 76.4%，远超 Bun 的 40.6%。新增 `lib.node` 默认类型支持。
- 🕸️ **网络调试**：Chrome DevTools 现在可以检查 Deno 的网络流量，包括 `fetch()`、`node:http` 和 WebSocket 请求。
- 🔥 **CPU 性能分析**：内置 CPU 分析器，支持生成 `.cpuprofile` 文件、交互式 SVG 火焰图和 Markdown 报告。
- 🗂️ **包管理工作空间**：支持 `catalog:` 协议统一管理依赖版本，支持跨平台 npm 安装 (`--os` 和 `--arch` 标志)，新增 `--prod` 标志跳过开发依赖，支持 `nodeModulesLinker: "hoisted"` 提升的 `node_modules` 布局。
- ⏳ **import defer**：支持 TC39 `import defer` 提案，延迟模块评估以优化启动时间。
- 📜 **TypeScript 6.0.3**：内置 TypeScript 编译器更新至 6.0.3。
- 🧪 **测试与覆盖率**：测试 sanitizers 默认关闭，新增 per-test 超时，覆盖率报告新增函数覆盖率。
- 🌐 **Web API**：新增 `OffscreenCanvas` 和几何接口（`DOMPoint`、`DOMRect` 等），改进 `structuredClone` 和可转移对象支持。
- 🛠️ **任务运行器**：并行任务输出带颜色编码的任务名前缀，支持 `set -e` 和 `:` 命令。
- 📉 **增量更新**：`deno upgrade` 现在下载二进制差异，典型补丁级升级下载量减少 87-93%。
- 🔗 **模块加载器钩子**：实现 Node.js 的 `module.registerHooks()` API，允许自定义模块加载行为。
- ⏰ **setTimeout/setInterval**：现在返回 Node.js 的 `Timeout` 对象，而非数字，提升性能并简化模型。
- 🎨 **其他改进**：支持 `NODE_EXTRA_CA_CERTS` 环境变量，`deno compile` 新增 `include`/`exclude` 字段，`deno doc` 支持渲染 npm 包，`--watch` 重启发送 `SIGTERM` 信号。

---

### [Node.js — Node.js 24.16.0（长期支持版）](https://nodejs.org/en/blog/release/v24.16.0)

**原文标题**: [Node.js — Node.js 24.16.0 (LTS)](https://nodejs.org/en/blog/release/v24.16.0)

Node.js 24.16.0 (LTS) 版本发布，代号“Krypton”，包含多项新功能、安全修复和依赖更新。

- 🔒 **加密模块增强**：新增 `randomUUIDv7()` 方法，支持 Ed25519 上下文参数，并修复密钥类型验证问题
- 🐛 **调试器升级**：`node inspect` 新增免编辑运行时表达式探测功能
- 📁 **文件系统改进**：`fs.stat()` 支持信号选项，`statfs` 暴露 `frsize` 字段
- 🌐 **HTTP 模块强化**：`ClientRequest` 选项合并更安全，`IncomingMessage` 新增 `req.signal` 属性
- 🔄 **流处理优化**：`duplexPair` 支持销毁传播，修复嵌套 compose 错误传播问题
- 🧪 **测试运行器更新**：支持测试顺序随机化、mock 超时 API 对齐、`AbortSignal.timeout` 支持
- 🎨 **工具函数增强**：`util` 模块支持十六进制颜色文本着色
- 🔧 **QUIC 协议改进**：多项修复与功能增强，包括 ALPN 协商、SNI 支持
- 📦 **依赖更新**：V8、npm、OpenSSL、libuv、sqlite 等核心库升级
- 🛠 **构建与工具优化**：修复编译警告，改进 CI 流程和依赖管理

---

### [Firefox 151 开发者发布说明（稳定版） - Mozilla | MDN](https://developer.mozilla.org/en-US/docs/Mozilla/Firefox/Releases/151)

**原文标题**: [Firefox 151 release notes for developers (Stable) - Mozilla | MDN](https://developer.mozilla.org/en-US/docs/Mozilla/Firefox/Releases/151)

以下是 Firefox 151 开发者版本的更新摘要：

Firefox 151 为开发者带来了多项新功能，包括对 Shadow DOM、CSS 容器查询、文档画中画 API 和 Web 串行 API 的支持，并修复了多个 WebDriver 和扩展开发相关的问题。

- 🧩 **HTML 模板增强**：`<template>` 元素新增 `shadowrootslotassignment` 属性，支持声明式定义 Shadow DOM 的插槽分配行为。
- 🎨 **CSS 容器查询升级**：`@container` 规则现支持 `style()` 查询，可检查容器是否包含特定 CSS 声明或自定义属性。
- 📌 **定位锚点优化**：`position-anchor` 属性新增 `normal` 默认值，与 `position-area` 属性联动更新。
- 🖼️ **文档画中画 API**：桌面平台支持始终置顶窗口，可显示任意 HTML 内容（如视频会议、股票行情）。
- 🎨 **Canvas 语言设置**：`CanvasRenderingContext2D.lang` 属性支持设置画布上下文语言，尤其适用于离屏画布。
- 🔒 **全屏键盘锁定**：`Element.requestFullscreen()` 新增 `keyboardLock` 选项，可阻止 Esc 键退出全屏并拦截浏览器快捷键。
- 📡 **Web 串行 API**：桌面平台支持串行通信，可控制微控制器（如 ESP 设备、3D 打印机），需安装站点权限插件。
- 🧪 **WebDriver 改进**：新增 `browser.setClientWindowState` 命令，支持窗口状态切换；修复网络事件 cookie 属性和重定向超时问题。
- 🔧 **扩展开发修复**：`webRequest.onErrorOccurred` 事件错误信息更稳定；`tabs.group()` 和 `tabs.move()` 正确处理分屏标签。
- 🚀 **实验性功能**：包括 `@container style()` 范围语法、`field-sizing` 属性、滚动驱动动画时间线范围值等，默认禁用。

---

