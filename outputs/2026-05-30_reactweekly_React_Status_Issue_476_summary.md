### [TanStack 路由器和查询](https://tkdodo.eu/blog/tan-stack-router-and-query)

**原文标题**: [TanStack Router and Query](https://tkdodo.eu/blog/tan-stack-router-and-query)

TanStack Router 與 TanStack Query 的整合指南

- 🔄 **路由緩存 vs 查詢緩存**：路由緩存僅限於特定路由，而查詢緩存是全局共享的，適合跨路由數據（如用戶資料）
- ⚡ **在路由加載器中使用查詢**：通過 `queryClient.ensureQueryData` 或 `prefetchQuery` 在加載器中啟動查詢，確保數據在組件渲染前就已開始獲取
- 🛠️ **必要配置**：將 QueryClient 添加到路由上下文中，並設置 `defaultPreloadStaleTime: 0` 以關閉路由內建緩存，避免衝突
- 🧩 **使用 useSuspenseQuery**：與路由的 Suspense 和 Error Boundaries 完美整合，讓組件只處理正常情況，並支援流式 SSR
- ⏳ **加載器中是否 await**：不 await 時，可在組件中靈活選擇 `useSuspenseQuery`（阻塞）或 `useQuery`（非阻塞），避免瀑布效應
- 🌐 **SSR 支援**：TanStack Start 提供 `setupRouterSsrQueryIntegration`，自動將服務端數據脫水並流式傳輸到客戶端緩存
- 🚫 **避免使用 useLoaderData**：查詢需要 Query Observers 來觸發自動重新獲取、失效和垃圾回收，應始終使用 `use(Suspense)Query`
- 🎯 **將加載器視為事件處理器**：僅用於預先啟動數據獲取，不返回數據，組件仍能獨立運作，可逐步引入作為性能優化

---

### [TanStack Router 之美](https://tkdodo.eu/blog/the-beauty-of-tan-stack-router)

**原文标题**: [The Beauty of TanStack Router](https://tkdodo.eu/blog/the-beauty-of-tan-stack-router)

TanStack Router 是一款以类型安全、开发者体验和细粒度性能优化为核心的前端路由方案，它通过深度集成 TypeScript、文件路由和验证机制，解决了传统路由器的诸多痛点。

- 🎯 **类型安全路由**：路由参数、链接和搜索参数完全类型化，无需手动断言，错误信息清晰，重构更自信。
- 🔗 **类型化链接与参数**：`<Link>` 组件和 `useParams` 钩子基于路由定义自动推导类型，无效路径或参数会直接报错。
- 🔍 **搜索参数验证**：内置标准 schema 验证（如 arktype），自动解析/序列化，支持嵌套对象和数组，默认使用结构共享避免不必要渲染。
- ⚡ **细粒度订阅**：通过选择器（selectors）只订阅状态变化的部分，避免全局重渲染，提升性能，类似 TanStack Query 或 Zustand 的机制。
- 📁 **文件路由与代码路由**：支持文件系统路由（自动代码分割）和代码路由，两者最终统一为代码路由，兼顾灵活性和开发速度。
- 🧩 **集成 Suspense**：每个路由默认包裹 `<Suspense>` 和 `<ErrorBoundary>`，可直接使用 `useSuspenseQuery`，简化数据加载和错误处理。
- 🚀 **React 过渡支持**：导航使用 `startTransition`，但通过 `useSyncExternalStore` 实现细粒度订阅，未来期待并发存储改进。
- 💡 **其他亮点**：包括路由上下文、嵌套路由、查询集成、搜索中间件、monorepo 支持以及可选的 SSR 层 TanStack Start，全面提升开发效率。

---

### [Meticulous AI - 无需编写测试的自动化前端测试](https://www.meticulous.ai/?utm_source=reactstatus&utm_medium=newsletter&utm_campaign=26q2&utm_content=primary)

**原文标题**: [Meticulous AI - Automated Frontend Testing Without Writing Tests](https://www.meticulous.ai/?utm_source=reactstatus&utm_medium=newsletter&utm_campaign=26q2&utm_content=primary)

该平台提供自动化、全面且确定性的代码测试解决方案，无需开发者手动编写或维护测试用例，能显著提升开发效率并消除测试中的不稳定因素。

- 🧪 **零开发者工作量**：系统自动监控开发交互，生成覆盖所有代码路径的测试套件，无需手动编写或修复测试。
- 🤖 **AI 驱动持续进化**：AI 引擎根据代码变更自动更新测试用例，确保测试套件始终与应用程序同步。
- ⚡ **极速回归测试**：通过并行计算集群，可在 120 秒内完成数千个屏幕的测试，并支持与 CI 集成。
- 🚫 **彻底消除测试不稳定**：基于 Chromium 的确定性调度引擎从底层消除测试中的随机失败（flakes）。
- 🔒 **安全无副作用**：测试通过模拟后端响应（录制回放）避免数据污染，无需特殊测试账户或模拟数据。
- 🛠️ **广泛框架支持**：兼容 NextJS、React、Vue、Angular 等主流前端框架，提供简单脚本集成。
- 🏢 **企业级验证**：已被 Dropbox、Notion 等超 100 家组织采用，开发者反馈“无法想象没有它的工作方式”。

---

### [JSX.lol - 真的有人喜欢 React 吗？](https://jsx.lol/)

**原文标题**: [JSX.lol - Does anybody actually like React?](https://jsx.lol/)

### 概述总结
React 被广泛批评为过度复杂、性能低下且不适合大多数项目，其生态系统存在技术债务、供应商锁定和安全隐患，而更简单的原生 Web 技术或替代框架往往更优。

- 🚫 React 常被错误地当作万能工具，导致项目过度复杂和性能问题
- 🐌 JS 重型项目（如 React）会随时间变慢，维护成本高且漏洞多
- 🔓 React Server Components 曾出现 CVSS 10.0 的严重安全漏洞
- 🔄 水合模式（hydration）导致服务器和客户端重复执行 JS，效率低下
- 📱 React 的移动策略可能导致平台锁定，而 Web 提供更开放的替代方案
- 🤯 React API 设计混乱，文档不明确，正确用法争议不断
- 🧠 默认选择 React 而非根据需求选工具，扼杀了前端创新
- ⏳ React 技术栈变化过快，开发者难以长期维护旧项目
- 💸 React 生态系统臃肿，技术债务深重，但依然被盲目选择
- 🧩 React 社区存在质量危机，但行业会议未公开讨论
- 🔗 Next.js 在 Vercel 外几乎不可用，存在供应商锁定问题
- 👨‍💻 真正精通 React 的开发者稀缺且昂贵，资深工程师因复杂性流失
- 🌐 原生 HTML 渐进增强比 React 更快、更可靠、更易用
- ⚠️ Vercel 处理 Next.js 安全漏洞的方式被批评为不尊重社区
- 🚫 许多开发者建议完全停止使用 React，因其弊大于利
- 📉 “胖客户端”时代正在衰退，React 等框架可能过时
- 🛠️ 框架主义（frameworkism）让人误以为更多工具能解决问题，实则不然
- 🕰️ React 不擅长现代 UI 功能（如 autofocus、dialog），且学习成本高
- 💀 React 被形容为“臃肿的虚假承诺尸体”，向后兼容性差
- 🗑️ 构建计数器组件只需删除 node_modules，讽刺 React 的复杂性
- 🔄 React 只是技术历史中又一个被高估的框架（如 Flash、Angular）
- 🎭 React 的狂热支持者、冗长文档和自大态度令人反感
- 🛡️ 工程领导者应拒绝 React 重写，避免“又一个 JS 灾难”
- 🌱 新开发者可考虑避开 React，以提升长期职业前景
- ⚡ 从 React 迁移到原生 DOM API 后，速度和交互性立即提升
- 🐢 React 19 曾几乎让互联网更慢，因社区反对才暂缓变更
- 🏎️ Microsoft Edge 从 React 转向 Web Components 后，低端硬件性能大幅提升
- 💼 React 被批评为“劳动力套利”工具，对大多数组织而言不如替代方案
- 🚀 团队在 3 周内将 React 应用重写为 Svelte，效果显著
- 📉 React 正受到越来越多批评，建议项目决策时谨慎
- 😠 用户抱怨 React 导致糟糕的用户体验，而非开发者体验
- 🧹 移除 React 被视为“让弱点离开代码库”，强调 Web 基础的重要性
- 🤔 开发者质疑为何任何界面更新都要用 React，且前后端不应混为一谈
- 🧐 React 的复杂性和所有权问题让新开发者望而却步
- 🔄 团队在 2023 年放弃 React，转向更匹配客户需求的技术栈
- 😤 即使资深开发者，对 React 也感到“越来越恼火”
- ⏰ React 发布周期过长（1.5 年无更新），引发不满
- 🎭 React Server Components 对客户端问题毫无改善，不适合大多数场景
- 🏃 Liveview 在两天内解决了 React SPA 的性能问题，并成功替换
- 🚫 明确建议“不要使用 React”，认为它本就不该被用在多数项目中
- 📡 Signals 比 React Hooks 更易用、更高效
- 🚢 React Server Components 不适合快速交付产品
- 🤷 开发者质疑 React 的发展方向是否正确
- 📚 社区呼吁改善 JS 使用方式、推广渐进增强并化解 React 争议
- 📖 存在一份历史参考，记录了多年来对 React 的各种批评

---

### [获取失败](https://news.ycombinator.com/item?id=48274077)

**原文标题**: [Failed to retrieve](https://news.ycombinator.com/item?id=48274077)

无法总结：获取内容失败，状态码 429。

---

### [react-router/CHANGELOG.md 在 main 分支 · remix-run/react-router · GitHub](https://github.com/remix-run/react-router/blob/main/CHANGELOG.md#v7160)

**原文标题**: [react-router/CHANGELOG.md at main · remix-run/react-router · GitHub](https://github.com/remix-run/react-router/blob/main/CHANGELOG.md#v7160)

概述总结
- 🌟 React Router 是一个公开的 GitHub 仓库，拥有 56.4k 星标和 10.9k 分支，代码活跃且社区关注度高。
- 📂 仓库包含 Issues（93 个）、Pull requests（37 个）、Discussions 和 Actions 等丰富功能，支持协作开发。
- 🔒 需要登录才能更改通知设置，强调用户身份验证的重要性。
- 📄 主要文件为 CHANGELOG.md，包含 4762 行代码和 294KB 内容，详细记录了版本变更历史。
- 🛠️ 提供代码浏览、编辑、原始文件下载和 blame 功能，便于追踪修改和贡献。
- 🔄 当前分支为 main，支持展开文件树和查看最新提交历史。

---

### [未来标志 | React Router](https://reactrouter.com/upgrading/future#futurev8_trailingslashawaredatarequests)

**原文标题**: [Future Flags  | React Router](https://reactrouter.com/upgrading/future#futurev8_trailingslashawaredatarequests)

React Router 未来标志升级指南概述

- 📋 建议逐步采用每个未来标志并分别提交，避免一次性全部更改
- 🔄 首先升级到最新的 v7.x 版本以获取所有未来标志：`npm install react-router@7 @react-router/{dev,node,etc.}@7`
- 🛡️ `future.v8_middleware`：启用中间件功能，允许在请求处理前后运行代码，需更新使用 `context` 参数的代码
- ⚡ `future.v8_splitRouteModules`：将客户端路由导出拆分为独立代码块，提升加载性能，无需更改代码
- 🏗️ `future.v8_viteEnvironmentApi`：支持 Vite 6+ 的环境 API，无需代码更改（除非有自定义 Vite 配置）
- 🔍 `future.v8_passThroughRequests`：传递原始 HTTP 请求，减少服务器开销，需使用新的 `url` 参数替代 `request.url`
- 🔗 `future.v8_trailingSlashAwareDataRequests`：保留尾部斜杠语义，避免 URL 歧义，需更新自定义匹配逻辑
- ⚠️ 不稳定标志仅供测试使用，不建议用于生产环境

---

### [无产者们！尚未读到祂降临的迫近，"他重复道。](https://www.readwriterachel.com/presentations/2026/05/21/react-60fps-slides.html)

**原文标题**: [Proles! Without having read to the imminence of His Coming," he repeated.](https://www.readwriterachel.com/presentations/2026/05/21/react-60fps-slides.html)

概述总结
- 📖 文章片段来自《1984》，描述了温斯顿与茱莉亚的互动，以及极权社会中压抑的氛围。
- 👤 温斯顿在回忆中感到恐惧与讽刺，提到“他的来临”等宗教隐喻，暗示对希望的扭曲。
- 🚫 文中出现“冒名顶替”和“租房间不易”等细节，反映社会控制与个人自由的缺失。
- 😢 茱莉亚以“别这样”抗议，温斯顿则因自杀冲动而痛苦，凸显心理压迫。
- 🐷 提到“猪面警察”和“党囚犯”，强化了奥威尔对极权统治的批判。
- 📝 包含“三十到四十组”等指令，展现集体化与个人身份的抹杀。

---

### [TanStack 的延迟水合是否具有革命性？ - YouTube](https://www.youtube.com/watch?v=_PB9rHndhU8)

**原文标题**: [Is TanStack Starts Deferred Hydration Revolutionary? - YouTube](https://www.youtube.com/watch?v=_PB9rHndhU8)

本頁面列出了 YouTube 平台的相關資訊與政策，包括版權、聯絡方式、開發者條款及隱私安全等核心內容。
- 📰 新聞中心：提供官方新聞與公告
- ©️ 版權：說明內容使用與保護規則
- 📞 聯絡我們：提供用戶與創作者聯繫管道
- 🎨 創作者：支援內容製作者的資源與工具
- 📢 刊登廣告：廣告投放與合作資訊
- 💻 開發人員：API 與技術開發文件
- 📋 條款：使用條款與服務協議
- 🔒 私隱：隱私權政策說明
- 🛡️ 政策及安全：平台安全與內容規範
- ⚙️ YouTube 的運作方式：平台機制與演算法說明
- 🧪 測試新功能：新功能測試與反饋
- 🏢 © 2026 Google LLC：版權歸屬與法律聲明

---

### [延迟水合 | TanStack Start React 文档](https://tanstack.com/start/latest/docs/framework/react/guide/deferred-hydration)

**原文标题**: [Deferred Hydration | TanStack Start React Docs](https://tanstack.com/start/latest/docs/framework/react/guide/deferred-hydration)

TanStack Start 的延遲水合功能允許開發者將頁面部分內容標記為「暫不互動」，以優化初始載入效能。

- 🚀 **延遲水合機制**：透過 `<Hydrate>` 元件與策略（如 `visible()`、`idle()`）控制子樹何時從靜態 HTML 轉為可互動狀態，預設會將子元件拆分為獨立 JS 區塊。
- 🎯 **適用場景**：適合折疊內容、地圖/圖表等豐富元件、需用戶觸發的面板，但不適合導航、搜尋框、購物車按鈕等需立即互動的 UI。
- ⚡ **三大決策**：`when`（決定水合時機）、`split`（是否拆分程式碼）、`prefetch`（是否提前載入），可精細控制效能與用戶體驗。
- 🧩 **策略多樣**：支援 `visible()`（進入視口）、`idle()`（空閒時）、`interaction()`（用戶互動）、`never()`（永不水合）等，並可組合使用。
- 🔄 **巢狀邊界**：父邊界先水合，子邊界才能水合；互動策略可穿透未解析的祖先鏈，但 `never()` 會阻止後代水合。
- 🛠️ **實用食譜**：如折疊內容延遲水合、閒暇預載子區塊、用戶意圖觸發冷元件、無拆分僅延遲水合、靜態 SSR 保留等。
- ⚠️ **限制與注意**：編譯器拆分需直接使用 `<Hydrate>` 標籤，避免鉤子呼叫或 `this` 捕獲在 JSX 內；`fallback` 僅用於客戶端掛載場景。

---

### [Expo UI 现已稳定：从单一导入实现 SwiftUI 和 Jetpack Compose](https://expo.dev/blog/expo-ui-stable-sdk-56?utm_source=react-status&utm_medium=email&utm_campaign=sdk-56)

**原文标题**: [Expo UI is now stable: SwiftUI and Jetpack Compose from a single import](https://expo.dev/blog/expo-ui-stable-sdk-56?utm_source=react-status&utm_medium=email&utm_campaign=sdk-56)

概述：本文探讨了人工智能在医疗诊断中的最新应用，强调其提升准确性和效率的潜力，同时指出数据隐私和算法偏见等挑战。

- 🩺 人工智能通过分析医学影像（如 X 光片和 CT 扫描），提高了疾病检测的准确率，尤其在早期癌症诊断中表现突出。  
- 📊 机器学习模型能快速处理大量患者数据，辅助医生制定个性化治疗方案，减少误诊风险。  
- 🔒 数据隐私问题成为主要障碍，医疗数据的敏感性和法规要求（如 HIPAA）需严格保护患者信息。  
- ⚖️ 算法偏见可能导致诊断结果不公，尤其对少数族裔或低收入群体，需通过多样化训练数据来缓解。  
- 💡 未来方向包括整合自然语言处理技术，优化电子健康记录分析，以及加强人机协作以提升医疗服务质量。

---

### [我为何从 Next.js 和 RSC 回归到普通 SPA 与独立后端 - DEV 社区](https://dev.to/devrayat000/why-i-walked-back-from-nextjs-and-rsc-to-a-plain-spa-and-a-separate-backend-3ibo)

**原文标题**: [Why I Walked Back from Next.js and RSC to a Plain SPA and a Separate Backend - DEV Community](https://dev.to/devrayat000/why-i-walked-back-from-nextjs-and-rsc-to-a-plain-spa-and-a-separate-backend-3ibo)

以下是对文章内容的总结：

作者从 Next.js 和 React Server Components（RSC）的忠实用户，经过一系列安全事件和架构反思，最终回归到传统的单页应用（SPA）加独立后端架构。

- 🔄 作者经历了从 Next.js Pages Router（清晰、可理解）到 App Router/RSC（心智模型破碎、缓存问题、安全漏洞）的完整循环
- 🚨 一系列严重安全漏洞（包括 CVSS 10.0 的 RSC 漏洞和中间件授权绕过）暴露了全栈框架的深层攻击面
- 🧠 核心问题在于 RSC 的序列化边界：函数、类实例、错误堆栈等无法干净地跨网络传输，且序列化本身成为安全风险点
- 🛡️ 安全最佳实践：中间件只能用于用户体验，真正的安全边界必须由后端在每个请求上强制执行
- 📦 当前技术栈：前端使用 React Router 框架模式+Vite（SPA 模式，无 SSR），后端使用 Hono（或 Go/Python），通过纯 HTTP 通信
- ✅ 新架构优势：代码可读性高、无序列化开销、前端攻击面极小、安全策略可见、后端语言自由选择、故障影响范围小
- ⚠️ 作者强调并非否定 Next.js 或 TanStack，而是针对自己的认证型产品场景，更简单的架构更合适

---

### [TanStack Start 身份验证：2026 年开发者指南 — WorkOS](https://workos.com/blog/tanstack-start-authentication-guide)

**原文标题**: [TanStack Start authentication: A developer's guide for 2026 — WorkOS](https://workos.com/blog/tanstack-start-authentication-guide)

### 概述
TanStack Start 的身份验证模型围绕一个核心原则构建：**服务器函数是安全边界，而非路由**。本文从零开始，详细介绍了如何利用服务器函数、`beforeLoad`、会话和中间件构建完整的身份验证系统，并强调了“双重防护”模式的重要性。

- 🔐 **核心原则**：每个 `createServerFn` 都是一个独立的 HTTP 端点，可直接被调用。`beforeLoad` 守卫仅保护页面体验，无法阻止对服务器函数的直接访问。因此，身份验证必须在每个处理敏感数据的服务器函数内部强制执行。
- 🛡️ **双重防护模式**：保护操作需要两层防护。第一层是路由守卫（`beforeLoad`），用于重定向未认证用户；第二层是服务器函数守卫（中间件），用于保护数据和操作，防止端点被直接调用。
- ⚙️ **核心构建块**：TanStack Start 提供了四个关键原语：服务器函数（安全边界）、`beforeLoad`（路由守卫）、中间件（可组合的身份验证逻辑）和会话（通过 `vinxi/http` 管理 cookie）。
- 🧩 **类型安全上下文**：TanStack Router 的类型系统允许 `beforeLoad` 返回的数据自动更新路由上下文，并在整个路由树中提供类型安全的用户信息，在编译时捕获身份验证错误。
- 🚀 **实现方法**：文章介绍了三种方法：1）使用会话 cookie 的服务器函数（完全控制）；2）使用 Better Auth 或 Auth.js 等库；3）使用 WorkOS 等托管身份验证提供商，后者提供专门的 SDK 和中间件集成，尤其适合需要企业级功能（如 SSO、SCIM）的 B2B 应用。
- ⚠️ **关键安全考量**：必须始终在服务器函数内部强制执行身份验证，并使用 `inputValidator` 进行输入验证。需防范用户枚举攻击，使用恒定时间比较，并设置安全的 cookie 属性（`httpOnly`、`secure`、`sameSite`）。
- 📋 **生产环境清单**：提供了一份详细清单，涵盖了安全实践（如密码哈希、速率限制、日志记录）和部署注意事项（如生成强会话密钥、测试端点、配置反向代理）。
- ⏳ **构建 vs 购买**：自行构建 MVP 需要 1-3 天，生产就绪版本需要 4-8 周，企业级版本需要 3-6 个月以上。托管提供商可将集成时间压缩至几小时，并将安全维护负担转移出去。

---

### [在 React 中构建预测文本输入 - Matt Huggins](https://matthuggins.com/blog/posts/building-a-predictive-text-input-in-react)

**原文标题**: [Building a Predictive Text Input in React - Matt Huggins](https://matthuggins.com/blog/posts/building-a-predictive-text-input-in-react)

### 概述总结

本文详细介绍了如何在 React 中使用`contentEditable`构建一个内联预测文本输入组件，该组件能够像 IDE 一样在用户输入时显示灰色预测文本，并通过 Tab 或方向键快速接受预测，从而提升用户输入流畅度。

- 🧠 **核心思路**：使用`contentEditable`属性在`div`元素上实现富文本编辑，通过插入灰色`<span>`显示预测文本，并利用`Tab`或`→`键接受预测。
- ⚙️ **组件结构**：定义`PredictiveTextInput`组件，包含`keywords`、`onChange`、`placeholder`和`value`等属性，通过`ref`和`isUpdatingRef`防止 DOM 反馈循环。
- 📍 **光标追踪**：使用`Selection`和`Range` API 获取光标位置，并通过克隆 DOM 并移除预测`<span>`来计算纯净文本长度。
- 🔍 **当前词识别**：通过正则表达式查找光标前最后一个完整单词，并检查光标是否位于词尾，避免在词中显示预测。
- 🔗 **关键词匹配**：将用户输入的单词与关键词列表进行不区分大小写的前缀匹配，返回未输入的部分作为预测文本。
- 🧹 **预测管理**：在插入新预测前移除旧预测，插入后立即将光标定位在预测文本之前，确保用户未“输入”的文本不被选中。
- ⌨️ **键盘交互**：按`Tab`或`→`接受预测（将`<span>`替换为文本节点），按`Enter`阻止换行，按`Backspace`或普通字符键移除预测。
- 🔄 **选择变化处理**：监听`selectionchange`事件，防抖后更新预测，确保光标移动时预测正确显示或移除。
- 🎯 **光标设置**：提供`setCursorPosition`函数，通过遍历文本节点并创建折叠范围，将光标定位到指定位置。
- 🔗 **外部值同步**：当`value`属性变化时，更新 DOM 内容并尝试恢复光标位置，使用`setTimeout(0)`确保 DOM 稳定后再操作。
- 💡 **关键要点**：`contentEditable`需要直接 DOM 操作，预测应在词尾显示，使用`Tab`/`→`接受，通过`ref`和标志位管理反馈，并防抖处理选择变化事件。

---

### [react-data-table-component：10 行代码实现表格功能](https://reactdatatable.com/)

**原文标题**: [react-data-table-component: Working table in 10 lines](https://reactdatatable.com/)

react-data-table-component v8.0 是一个开箱即用的 React 数据表格库，无需额外配置和样式工作，支持排序、分页、行选择等多种功能。

- 📦 零依赖：无需 peer deps，支持 React 18+，安装即可使用
- 🎨 内置 5 种主题：默认、Material、Rounded、Catppuccin、AG Grid，均支持暗黑模式，也可自定义
- 🔄 排序与分页：支持客户端和服务端排序，可配置或自定义分页组件
- ✅ 行选择：多选复选框，支持全选、跨页持久化，通过 ref 控制
- ▶️ 可展开行：渲染任意组件到展开面板，单属性控制动画开合
- 🔍 列过滤：每列支持文本、数字、选择过滤，可对接服务端搜索
- 📊 列分组：跨列标题，适用于财务和分析表格
- ↔️ 可调整列宽：拖动调整，宽度可序列化保存
- 🖥️ SSR 与 Next.js 支持：兼容 Next.js App Router、Remix、Astro，无 useLayoutEffect 警告
- ⚡ 低学习成本：相比 TanStack Table 和 AG Grid Community，设置更简单，无需额外样式工作
- 💰 免费使用：2018 年起持续维护，支持赞助

---

### [pip-it-up — 现代文档画中画工具包](https://pip-it-up.vercel.app/)

**原文标题**: [pip-it-up — Modern Document Picture-in-Picture Toolkit](https://pip-it-up.vercel.app/)

这是一个用于将任何 UI 组件弹出为画中画窗口的库，支持零配置、自动调整大小和框架无关的核心。

- 🖼️ **核心功能**：通过`PipWrapper`和`PipTrigger`组件，轻松将任意 UI 组件弹出为浮动画中画窗口，保留内容和光标状态。
- 🔄 **实时样式同步**：使用`MutationObserver`实时同步样式、主题和 CSS-in-JS 变更，确保弹出窗口样式一致。
- 🎮 **多种 DOM 策略**：支持移动、克隆和传送门三种模式，移动模式保留状态，传送门保持组件树完整。
- 📏 **自动调整与响应式**：窗口自动适应内容大小，支持`isInsidePip`属性实现响应式画中画布局。
- ⌨️ **键盘转发**：Cmd+S、Cmd+K 等快捷键在画中画窗口中正常工作，提升编辑体验。
- 🌐 **优雅降级**：Firefox 和 Safari 回退到新标签页或自定义处理程序（如模态框），兼容性良好。
- 🛡️ **SSR 安全**：无缝支持 Next.js、Remix 和 Vite，无 hydration 不匹配问题。
- 🔗 **解耦触发器**：通过命名注册表，任何触发器可连接任意包装器，无需共享上下文。
- 📝 **TypeScript 优先**：提供泛型类型钩子、完整 IntelliSense，无需类型转换。
- 🧩 **编辑器支持**：与 Tiptap、Monaco、CodeMirror 等编辑器完美集成，保留状态和撤销历史。
- 📊 **浏览器支持**：基于文档画中画 API，Chrome/Edge 116+ 完全支持，Firefox/Safari 回退，需 HTTPS 和用户手势。
- 🚀 **路线图**：计划支持视频/Canvas 画中画、Vue/Svelte/Angular 绑定，以及 v1.0 稳定版发布。

---

### [游乐场](https://pip-it-up-playground.vercel.app/)

**原文标题**: [playground](https://pip-it-up-playground.vercel.app/)

概述摘要：本文探讨了人工智能在医疗诊断中的应用，强调其提升效率与准确性的潜力，同时指出数据隐私和算法偏见等挑战。

- 🤖 人工智能通过分析医学影像（如 X 光片和 CT 扫描）辅助医生更快、更准确地识别疾病。
- 📊 机器学习模型可处理大量患者数据，预测疾病风险，支持个性化治疗方案。
- 🔒 数据隐私问题突出，需严格保护患者信息，防止未经授权的访问或滥用。
- ⚖️ 算法偏见可能导致诊断不公，需确保训练数据多样且代表不同人群。
- 💡 尽管有挑战，AI 在医疗中的持续发展有望改善全球医疗资源分配和诊断效率。

---

### [React 中的“剧透”动画剧透](https://spoiled.vercel.app/)

**原文标题**: [`spoiled` animated spoilers in React](https://spoiled.vercel.app/)

概述摘要  
- 🧠 文章核心围绕人工智能在医疗诊断中的应用，强调其提升准确性与效率的潜力。  
- 📊 通过分析大量医学影像数据，AI 能辅助识别早期病变，如肿瘤或视网膜疾病。  
- ⚕️ 实际案例显示，AI 系统在皮肤癌和肺部结节检测中表现优于部分人类专家。  
- 🔒 数据隐私与算法偏见仍是主要挑战，需加强监管与伦理审查。  
- 🌍 未来趋势包括跨机构数据共享与联邦学习，以促进模型泛化能力。

---

### [GitHub - Agent-Field/agentfield: 像 API 和微服务一样构建、运行和扩展 AI 智能体——从第一天起就具备可观测、可审计和身份感知能力。](https://github.com/Agent-Field/agentfield)

**原文标题**: [GitHub - Agent-Field/agentfield: Build, run and scale AI agents like API and microservices - observable,auditable and identity-aware from day one. · GitHub](https://github.com/Agent-Field/agentfield)

AgentField 是一个开源 AI 后端控制平面，能将 AI 智能体像 API 一样构建、部署和扩展，具备可观测性、可审计性和身份感知能力。

- 🚀 **核心能力**：将 Python、Go 或 TypeScript 编写的智能体逻辑转化为生产级 REST API，支持路由、协调、内存、异步执行和加密审计。
- ⚙️ **关键功能**：提供 `app.ai()`（结构化 LLM 调用）、`app.pause()`（人工审批暂停）、`app.call()`（跨智能体路由）和 `app.run()`（自动暴露 REST 端点）。
- 🧠 **智能体网格**：支持智能体发现（按标签、健康状态）、跨智能体调用（带追踪）、并行执行和自动注册。
- 🛡️ **治理与安全**：每个智能体拥有 W3C DID 加密身份，提供可验证凭证（VC）、基于标签的策略执行和防篡改审计追踪。
- 📊 **可观测性**：自动生成工作流 DAG 图、Prometheus 指标、结构化日志、执行时间线和健康检查。
- 🔄 **部署与版本**：支持金丝雀部署、A/B 测试、蓝绿部署、流量权重路由和智能体生命周期管理。
- 💾 **分布式内存**：内置键值存储、向量搜索（语义）、四种作用域（全局/智能体/会话/运行）和无 Redis 依赖。
- 🤖 **多步编码代理**：通过 `app.harness()` 调度 Claude Code、Codex 等工具，支持成本上限、轮次限制和输出恢复。
- 🛠️ **开发者体验**：CLI 脚手架（`af init`）、本地仪表盘（`af server`）、热重载、MCP 服务器集成和 Docker/K8s 就绪。
- 🏗️ **架构**：控制平面为无状态 Go 服务，智能体可连接自任何环境，通过 WebSocket 注册和通信。

---

### [发布 Reanimated - 4.4.0 · software-mansion/react-native-reanimated · GitHub](https://github.com/software-mansion/react-native-reanimated/releases/tag/4.4.0)

**原文标题**: [Release Reanimated - 4.4.0 · software-mansion/react-native-reanimated · GitHub](https://github.com/software-mansion/react-native-reanimated/releases/tag/4.4.0)

React Native Reanimated 4.4.0 版本发布，带来了多项重要更新和新功能。

- 🚀 **iOS CSS Core Animation 引擎**：新增基于 Core Animation 的 CSS 动画引擎，直接在 iOS 图层上运行动画，绕过 JS 驱动更新循环，需通过 `IOS_CSS_CORE_ANIMATION` 特性标志启用。
- ⚙️ **动画后端集成**：引入新的动画后端，优化阴影树更新流程，提升动画性能。
- ⏱️ **新的 useTimestamp 钩子**：提供 `useTimestamp` 钩子，返回每帧更新的共享值，并支持通过 `isActive` 标志暂停和恢复。
- 📱 **Android 预编译头**：Android 原生构建使用预编译头 `ReanimatedPCH.h`，显著减少 C++ 编译时间。
- 🐛 **修复与优化**：修复弹簧动画抖动、动画取消竞态条件、CSS 过渡属性回退等问题，并优化同步属性逻辑。
- ✨ **新增同步属性支持**：新增对 `placeholderTextColor`、`shadowColor`、`shadowOffset`、`outlineColor` 等属性的支持。
- 🧹 **代码清理与重构**：移除不再使用的代码和旧功能，如 JSC 运行时支持、`useInterpolateConfig` 函数等。
- 📚 **文档更新**：更新特性标志、布局动画、同步属性等文档，并添加 Expo SDK 55 和 56 版本支持。
- 🤝 **新贡献者**：欢迎 `PiotrWszolek`、`pranko17`、`edkimmel`、`ashfurrow`、`elliottkember` 首次贡献。

---

### [发布 3.0.0 · software-mansion/react-native-gesture-handler · GitHub](https://github.com/software-mansion/react-native-gesture-handler/releases/tag/v3.0.0)

**原文标题**: [Release 3.0.0 · software-mansion/react-native-gesture-handler · GitHub](https://github.com/software-mansion/react-native-gesture-handler/releases/tag/v3.0.0)

React Native Gesture Handler 3.0.0 稳定版发布，针对新架构重建，引入基于 Hook 的新 API、新的 Touchable 组件以及与 Reanimated 的深度集成。

- 🎉 发布 React Native Gesture Handler 3.0.0 稳定版，针对新架构重建
- 🆕 引入基于 Hook 的新 API，简化手势处理
- 🖱️ 新增 Touchable 组件，替代旧版按钮组件
- 🔄 深度集成 Reanimated，提升动画性能
- 🛠️ 移除对旧架构和 Paper 的支持
- 🧹 清理和重构代码，包括移除废弃组件和优化类型定义
- 🌐 改进 Web 平台支持，修复手势和事件对齐问题
- 📱 修复 iOS 和 Android 上的多个手势处理 Bug
- 📚 更新文档，添加迁移指南和兼容性表格
- 🤝 新增多位贡献者，包括 AndreasHogstrom、YevheniiKotyrlo 等

---

### [GitHub - pierpo/react-archer: 🏹 在 React 元素之间绘制箭头 🖋](https://github.com/pierpo/react-archer)

**原文标题**: [GitHub - pierpo/react-archer: 🏹 Draw arrows between React elements 🖋 · GitHub](https://github.com/pierpo/react-archer)

react-archer 是一个用于在 React 元素之间绘制箭头的库，支持自定义样式和锚点，安装简单并提供丰富的 API 配置。

- 🏹 核心功能：在 React DOM 元素之间绘制箭头，支持曲线、角度或直线样式
- 📦 安装方式：通过 `npm install react-archer` 或 `yarn add react-archer` 快速安装
- 🎨 自定义箭头：可配置颜色、宽度、虚线、端点形状（箭头或圆形）及标签
- 🔗 锚点选项：支持 top、bottom、left、right、middle 五种锚点定位
- 🛠 容器组件：`ArcherContainer` 提供全局样式控制，如 `strokeColor`、`strokeWidth` 等
- 🧩 元素组件：`ArcherElement` 通过 `id` 和 `relations` 定义箭头关系
- 🔄 刷新方法：通过 `ref` 调用 `refreshScreen` 手动重绘箭头，解决渲染问题
- 📐 高级功能：支持 `order` 控制箭头层级，`domAttributes` 实现交互（如悬停）
- ⚠️ 注意事项：`middle` 锚点效果不佳，箭头曲线和标记可能有偏移
- 🌟 项目状态：1.3k 星标，40 个版本，MIT 许可证，主要使用 TypeScript 开发

---

### [react-spring](https://www.react-spring.dev/)

**原文标题**: [react-spring](https://www.react-spring.dev/)

React Spring 是一个为 React 应用提供流畅自然动画的库，通过弹簧物理模拟替代传统时间曲线动画，让界面交互更生动。它支持多种平台，性能优异，且无需频繁重新渲染。

- 🚀 **轻松上手**：通过 `npm i @react-spring/web` 安装，即可用弹簧动画提升 UI 交互体验。
- 🌱 **弹簧原理**：摒弃固定时长和曲线，模拟真实世界物理运动，实现连续、流畅的交互效果。
- 🎯 **多平台支持**：覆盖 web、native、three、konva、zdog 五种目标，灵活适配不同场景。
- ⚡ **避免重渲染**：使用命令式 API 运行动画，无需更新状态，减少 React 渲染开销。
- 🛠️ **生产就绪**：支持 SSR、TypeScript 编写，可压缩至 15.2kb（核心包），轻量高效。
- 💬 **社区好评**：被 Remix 联合创始人、CodeSandbox 创建者等开发者盛赞，认为它简单、强大且性能卓越。
- 🌐 **生态扩展**：与 react-three-fiber、zustand 等工具集成，提供更丰富的开发能力。

---

