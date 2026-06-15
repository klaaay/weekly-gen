### [React 摘要：电子邮件通讯](https://reactdigest.net/)

**原文标题**: [React Digest: Email Newsletter](https://reactdigest.net/)

概述摘要
- 📬 每周一封精心策划的邮件，专为 React 开发者设计
- 👥 已有超过 22,393 名前端软件工程师订阅
- 📝 精选文章并附简短摘要，节省寻找优质内容的时间
- 🎓 每周都能学到新知识
- 💬 读者反馈：文章实用、紧跟技术演进、并发模式内容受益匪浅
- 🏢 订阅者来自各大前端工程师团队
- 📅 覆盖 2013-2026 年，提供新闻通讯、隐私及广告选项

---

### [TanStack Query 入门指南 — Neciu Dan](https://neciudan.dev/a-gentle-introduction-to-tanstack-query)

**原文标题**: [A gentle introduction to TanStack Query — Neciu Dan](https://neciudan.dev/a-gentle-introduction-to-tanstack-query)

以下是您提供的文章摘要：

本文是 TanStack Query 的全面入门指南，从基础概念到高级用法，涵盖了数据获取、缓存、状态管理及规模化最佳实践。

- 📚 **核心问题**：原生 React 数据获取存在状态管理分散、竞态条件及组件卸载后数据丢失等问题。
- 🎣 **抽象层**：TanStack Query 通过`useQuery`提供统一的数据获取、加载和错误状态管理，并利用`queryKey`实现跨组件缓存共享。
- ⚙️ **关键配置**：包括`retry`（重试与指数退避）、`signal`（请求取消）、`enabled`/`skipToken`（条件查询）及`staleTime`（数据新鲜度控制）。
- 🏗️ **规模化实践**：推荐使用`queryOptions`替代自定义 Hook 包装，按领域分组查询，并利用 Orval 从 OpenAPI 模式自动生成代码。
- 🔄 **高级场景**：使用`useQueries`处理动态并行查询，`useInfiniteQuery`实现“加载更多”，并通过乐观更新与批量失效避免 UI 闪烁。
- 📖 **延伸资源**：建议查阅官方文档和 TkDodo 的博客，并强调 TanStack Query 应成为每个 React/RN/Solid/Svelte 项目的标配。

---

### [React 网格大比拼：KendoReact vs. MUI vs. AG Grid](https://www.telerik.com/blogs/great-react-grid-off-kendoreact-vs-mui-vs-ag-grid?utm_medium=cpm&utm_source=reactdigest&utm_campaign=dt_kendo-ui-react_grid_comparison)

**原文标题**: [
	The Great React Grid-Off: KendoReact vs. MUI vs. AG Grid
](https://www.telerik.com/blogs/great-react-grid-off-kendoreact-vs-mui-vs-ag-grid?utm_medium=cpm&utm_source=reactdigest&utm_campaign=dt_kendo-ui-react_grid_comparison)

本文对 KendoReact、MUI 和 AG Grid 三款 React 数据网格进行了性能基准测试，重点比较了它们在不同数据集大小和功能场景下的渲染与虚拟化性能。

- 📊 **测试概述**：针对基本网格、分页、行虚拟化和行列双轴虚拟化四种场景，测试了从 100 行到 100 万行、10 到 100 列的数据集，使用 Selenium 和 Faker.js 进行自动化重复测试。
- 🏆 **基本网格（≤5k 行）**：MUI 表现最快，例如 5,000x20 网格中 MUI 耗时 10.4 秒，优于 KendoReact 的 14.7 秒和 AG Grid 的 16.5 秒。
- 📄 **分页网格**：启用分页后，KendoReact 在所有数据集大小上均领先，例如 5,000x20 网格中仅需 0.38 秒，而 MUI 为 0.46 秒，AG Grid 为 0.50 秒。
- 🚀 **行虚拟化**：KendoReact 优势显著，在 100 万行 x 10 列测试中仅用 0.83 秒，远快于 MUI 的 5.6 秒和 AG Grid 的 6 秒。
- 🔄 **行列双轴虚拟化**：小数据集（10,000x100）中 MUI 略快（0.49 秒），但大数据集（100,000x100）中 KendoReact 胜出（0.62 秒），且扩展性更佳。
- 🎯 **选择建议**：若处理小数据集且无需虚拟化，MUI 合适；若需处理大型或增长数据集、注重虚拟化性能，KendoReact 是更优选择，其性能差距随数据量增大而扩大。

---

### [在 Next.js 中构建活跃的导航链接组件 | Aurora Scharff](https://aurorascharff.no/posts/building-an-active-navlink-component-in-nextjs/)

**原文标题**: [Building an Active NavLink Component in Next.js | Aurora Scharff](https://aurorascharff.no/posts/building-an-active-navlink-component-in-nextjs/)

本篇文章详细介绍了如何在 Next.js App Router 中构建一个可复用的、功能完善的 `NavLink` 组件，涵盖了从基础实现到高级特性（如渲染属性、待定状态、前缀匹配、无障碍、TypeScript、防闪烁及缓存组件支持）的全过程。

- 🔗 **核心实现**：基于 `usePathname()` 构建 `NavLink`，通过比较当前路径与链接 `href` 来确定激活状态，并包裹 `next/link` 以保持客户端导航能力。
- 🎨 **灵活样式**：采用渲染属性模式，允许 `className` 和 `children` 接收函数，从而根据 `isActive` 和 `isPending` 动态返回样式或内容，支持 `clsx` 等工具。
- ⏳ **待定状态**：利用 `useLinkStatus` 在链接内部获取导航加载状态，并通过 `children` 渲染属性暴露 `isPending`，用于显示加载指示器。
- 🧭 **前缀匹配**：默认支持前缀匹配（如 `/search` 匹配 `/search?q=react`），并通过 `exact` 属性提供精确匹配选项，特别处理根路径 `/` 始终精确匹配。
- ♿ **无障碍支持**：自动为激活链接添加 `aria-current="page"` 属性，既提升辅助技术体验，也便于通过 CSS 或 Tailwind 的 `aria-` 变体进行样式设计。
- 🛡️ **TypeScript 支持**：通过泛型和类型定义，确保 `href` 支持静态类型链接（`typedRoutes`），并为 `className` 和 `children` 的渲染属性提供完整的类型检查。
- ⚡ **防闪烁**：通过内联脚本在 HTML 解析阶段读取 `location.pathname` 并设置 `aria-current`，避免因客户端水合延迟导致的激活样式闪烁。
- 🧩 **缓存组件支持**：通过将 `Suspense` 边界移至组件内部，确保在 `cacheComponents` 模式下，静态链接的激活状态延迟不会导致布局偏移，同时为异步链接提供稳定的骨架屏。
- 🔄 **替代方案**：提供基于 `useSelectedLayoutSegments()` 的版本，比较路由段而非完整路径，天然避免重写导致的 hydration 问题，但需注意路由组的影响。
- ⚠️ **注意事项**：使用 `usePathname()` 时需警惕重写（rewrites）导致的 hydration 不匹配，可通过延迟读取路径名或内联脚本解决；渲染属性函数不可序列化，无法直接用于服务端组件。

---

### [指挥家重写：他们为提速所做的改动](https://performance.dev/the-conductor-rewrite)

**原文标题**: [The Conductor Rewrite:
What They Changed to Make It Fast](https://performance.dev/the-conductor-rewrite)

### 概述总结
Conductor 团队通过全面重写，将应用性能提升了 2 倍，核心优化包括从 React Router 迁移到 TanStack Router、采用虚拟化列表、将运行时从 Node 切换到 Bun，以及将检查点操作移出关键路径。

- 🚀 **架构基础**：采用本地优先架构（SQLite 作为数据源）和 Tauri 框架，消除网络延迟，实现快速冷启动
- 🔧 **性能瓶颈定位**：通过模拟 Tauri 桥接层，在 Chrome 中使用 React DevTools Profiler 精准定位渲染问题
- ⚡ **路由优化**：从 React Router 迁移到@tanstack/react-router，利用稳定引用减少不必要的组件重渲染
- 💬 **聊天性能提升**：使用 react-virtuoso 实现虚拟化列表，配合 React.memo 确保仅重渲染正在流式输出的消息
- 🖥️ **进程管理**：空闲代理进程自动关闭，通过`--resume`标志安全恢复，有效管理内存
- 🧩 **运行时切换**：从 Node 切换到 Bun，减少 150MB 包体积并提升进程启动速度
- ⏱️ **关键路径优化**：将检查点操作移至后台执行，确保用户按下回车后立即获得首个 token 响应
- 🛠️ **技术栈选择**：深度采用现代 React 生态（TanStack Query/Router、Zustand、Tiptap），而非手动优化
- 🎯 **产品理念**：团队自身重度使用产品，通过"自食其果"的方式发现并解决每个性能痛点

---

### [性能不是技术问题 - 舒丁](https://shud.in/thoughts/performance-is-not-a-technical-problem)

**原文标题**: [Performance Is Not a Technical Problem - Shu Ding](https://shud.in/thoughts/performance-is-not-a-technical-problem)

### 概述总结
性能问题并非技术缺陷，而是系统熵增的必然结果。通过分析 400 个性能优化 PR，发现相同错误反复出现，根源在于人类认知局限和系统设计缺陷。

- 🧠 **认知约束**：工程师无法在本地修改时掌握全局上下文，代码库增长远超个人记忆容量
- 🔍 **抽象幻觉**：看似干净的抽象隐藏真实成本（如全局事件监听器、缓存失效、隐式瀑布流）
- ⚠️ **系统失效**：类型安全、lint 工具、代码审查都无法阻止性能退化，因为问题本质是系统性的
- 🌱 **熵增定律**：性能如同花园，必须持续维护。等待"变慢"再修复是被动反应
- 🛠️ **系统解法**：需要能实时参考全局架构的智能系统，在编码时即时教学和约束
- 📚 **知识蒸馏**：将每个错误转化为可查询、可执行的结构化规则，让系统记住人类遗忘的细节
- 🚀 **早期验证**：团队已通过智能代理发现人工审查遗漏的关键性能问题

---

### [React 服务器组件如何与打包器集成 | reactjs maxxing](https://reactjs-maxxing.vercel.app/blog/how-react-server-component-integrate-with-bundler)

**原文标题**: [How React Server Components Integrate with Bundler | reactjs maxxing](https://reactjs-maxxing.vercel.app/blog/how-react-server-component-integrate-with-bundler)

本文介绍了 React 服务端组件（RSC）如何与打包器协同工作，在构建时将应用拆分为服务端和客户端两部分。

- 📦 **Flight 协议**：RSC 使用自定义的 Flight 协议生成流式数据，而非 JSON，以支持异步边界和延迟解析的服务端计算。
- 🔄 **双构建目标**：同一代码库需针对服务端和客户端两种运行时分别构建，使用不同的 React 入口点（服务端用`react-server`条件，客户端用标准 React）。
- 🧩 **服务端构建**：遇到客户端组件（如`Counter`）时，打包器将其替换为存根（stub），仅注册组件引用，不包含实际实现。
- 🖥️ **客户端构建**：客户端组件在浏览器端正常编译，使用 hooks 和浏览器 API，并生成清单将 Flight 流中的引用（如`$L1`）映射到实际模块。
- ⚡ **关键集成**：`react-server-dom-webpack`包负责将 Flight 协议与 webpack 连接，提供服务端渲染和客户端解析功能。
- 📋 **清单作用**：生成的清单作为内部胶水，将服务端引用转换为浏览器可加载的实际文件，实现组件按需加载。

---

### [CSS 网格轨道字段指南](https://gridlanes.webkit.org/)

**原文标题**: [The Field Guide to CSS Grid Lanes](https://gridlanes.webkit.org/)

本页面介绍了 CSS Grid Lanes，一种纯 CSS 实现瀑布流布局的简单方法，无需 JavaScript。

- 📸 提供多种演示：照片、食谱、报纸、菜单、时间线、图板等
- 🧱 核心概念：通过`display: grid-lanes`和`grid-template-columns/rows`实现自动排列
- 📐 支持多种轨道定义：`fr`单位、固定长度、百分比、`auto`、`min-content`、`max-content`、`fit-content()`、`minmax()`
- 🔄 自动填充与适应：`repeat(auto-fit, minmax(120px, 1fr))`实现响应式列数
- 🎯 放置控制：`flow-tolerance`调整排序灵敏度，`span`跨列，`grid-column`固定位置
- ♿ 无障碍：视觉顺序变化但 DOM 顺序不变，键盘和屏幕阅读器遵循源码顺序
- 🛡️ 渐进增强：使用`@supports`为不支持的浏览器提供回退布局
- 📱 方向切换：通过媒体查询切换`grid-template-columns`和`grid-template-rows`实现瀑布流与砖块布局
- 📚 深入资源：WWDC 演讲、webkit.org 文档、开发者工具指南
- 🏗️ 团队背景：由 WebKit 和 Safari 团队开发，经 CSS 工作组多年设计验证

---

### [一夜之间，构建 HTML 优先网站让我们的用户翻倍](https://mohkohn.co.uk/writing/html-first/)

**原文标题**: [How building an HTML-first site doubled our users overnight](https://mohkohn.co.uk/writing/html-first/)

该文章讲述了如何通过构建 HTML 优先的网站，使一家公用事业公司的用户数量在一夜之间翻倍。

- 📈 用户数量翻倍：采用 HTML 优先的 Astro 框架后，完成表单的用户数量立即翻倍，甚至分析工具都无法追踪到这些新用户的来源。
- 🛠️ 解决历史问题：此前两次昂贵的尝试（包括 React 应用）均失败，React 应用因加载缓慢、不兼容和无法访问等问题上线仅 3 天就被撤回。
- 🌐 公共服务的核心原则：网站必须能在任何设备、弱网络环境下工作，且表单数据永不丢失，尤其要支持老旧浏览器（如 PSP 浏览器）。
- 💡 技术实现：每个表单步骤独立页面，提交后数据存储后端；使用 HTML Web 组件（validation-enhancer）实现轻量级表单验证（<1KB），并渐进增强。
- 🔄 失败回退机制：验证失败时依次回退到浏览器原生验证、后端 API 验证，确保用户体验不中断。
- 📱 真实案例：有用户在一个月后继续完成之前中断的表单，验证了后端会话保存数据的可靠性。
- ⚠️ 行业反思：不应因“工作量更大”而放弃包容性设计；应构建能在 PSP+3G 环境下运行的网站，以确保长期可用性。

---

### [Patrick - CSS 布局中缺少什么](https://patrickbrosset.com/articles/2026-05-20-whats-missing-in-css-layout/)

**原文标题**: [Patrick  - What's missing in CSS layout](https://patrickbrosset.com/articles/2026-05-20-whats-missing-in-css-layout/)

### 概述总结
本文探讨了 CSS 布局中开发者面临的主要痛点与缺失功能，基于 2025 年 CSS 现状调查及社交媒体反馈，重点分析了 Grid 和 Flexbox 的使用困难，并提出了 12 项亟待补充的布局特性。

- 📚 **Grid 学习门槛高**：语法复杂（如`grid-template-*`）、心智模型难理解（隐式/显式网格）、属性命名不一致（`justify-*` vs `align-*`），需频繁查文档。
- 🛠️ **Grid 实际使用繁琐**：常见布局（全高滚动区、仪表盘）仍需复杂代码；与 Flexbox 选择困难；无法自然换行、缺乏行列选择器（如`:nth-column`），且动画支持差。
- 🔄 **Flexbox 方向与对齐混乱**：`flex-direction`与主轴/交叉轴关系难内化，`justify-*`/`align-*`依赖方向，导致频繁试错。
- 📏 **Flexbox 尺寸行为不可预测**：`flex-grow`/`shrink`/`basis`交互难推理，项目意外收缩（需`min-width:0`），固定与弹性尺寸混合效果不佳。
- 🔗 **Flexbox 换行控制缺失**：无法检测换行事件或为每行单独设置样式，导致孤项、行间距不均等问题。
- 🚨 **溢出与换行检测（12 次提及）**：CSS 无法感知内容溢出或换行，需 JS 实现自适应布局（如折叠导航项、显示"+3"徽章）。
- 📰 **CSS Regions（5 次提及）**：缺乏文本跨容器流动功能（类似 InDesign 链接文本框），影响杂志式多栏布局。
- 🔲 **CSS Exclusions（5 次提及）**：无法实现元素四周文字环绕、非矩形文本包裹（如`clip-path`形状），印刷级排版受限。
- 🧩 **元素重排独立于 DOM（5 次提及）**：无法在不修改 DOM 或复制标记的情况下改变元素视觉位置，影响响应式重排（如目录侧边栏/顶部切换）。
- 📐 **内容感知网格尺寸（3 次提及）**：网格项无法根据内容自动跨列或吸附列边缘，需 JS 计算跨度。
- 📄 **页面/列浮动（2 次提及）**：缺乏将元素浮动到列/页面顶部或底部的基本印刷布局功能。
- 🎯 **锚点定位扩展（2 次提及）**：尚不支持相对于光标、选中文本或行首/尾定位。
- 🧩 **Shadow DOM 样式控制（2 次提及）**：新 CSS 特性未考虑影子 DOM 边界，缺乏`:has-slotted`等选择器。
- ✏️ **文本自适应缩放（2 次提及）**：无原生方法使文本自动填充容器宽度（需 JS hack）。
- 📏 **Flex 行级控制（2 次提及）**：无法为 Flex 容器中每行单独设置对齐或样式。
- 🕳️ **网格间隙与空单元格样式（2 次提及）**：无法直接样式化网格间隙或空单元格，需额外包装元素。
- 💡 **其他单次提及功能**：包括瀑布流布局、图标内联附着、软换行指示、小数对齐列、圆形/极坐标布局、曲线文本、流程图箭头、网格/非线性变换、安全区域感知扩展、粘性表格列、虚拟键盘视口处理、边框偏移、可编辑上下文菜单等。
- 🏆 **首要改进建议**：溢出与换行检测最具潜力，可大幅减少 JS 依赖，解锁更多响应式设计可能性。

---

### [不必要的异步的隐忧 - 马特·史密斯](https://allthingssmitty.com/2026/06/08/the-quiet-problem-with-unnecessary-async/)

**原文标题**: [
    The quiet problem with unnecessary async - Matt Smith
  ](https://allthingssmitty.com/2026/06/08/the-quiet-problem-with-unnecessary-async/)

### 概述总结
文章讨论了 JavaScript 中不必要的`async`关键字如何悄然增加代码复杂性，强调`async`应仅用于真正的异步边界，而非未来的假设需求。

- 📉 **`async`改变函数契约**：即使没有`await`，`async`函数也会返回 Promise，迫使所有调用者变为异步，导致复杂性向外传播。
- 🔍 **函数签名失去信息价值**：当所有函数都标记为`async`时，签名无法区分真正的 I/O 操作与同步数据，增加代码理解难度。
- 🚫 **“未来可能需要”的陷阱**：为假设的未来异步需求提前添加`async`，会让当前代码付出不必要的认知成本，如测试和调用链的异步化。
- 🧠 **认知开销大于性能影响**：现代 JS 引擎处理 Promise 高效，但`async`会破坏同步控制流，增加调试和阅读的心理负担。
- 🏗️ **异步边界是架构决策**：在流式 SSR、React Server Components 等现代前端系统中，`async`影响渲染、组合和错误处理，应谨慎对待。
- ✅ **保持 API 诚实**：函数应反映当前行为，而非未来可能。同步函数保持同步，直到真正的异步需求出现再引入`async`。

---

### [为什么我们不用 Service Workers？—— Neciu Dan](https://neciudan.dev/why-are-we-not-using-service-workers)

**原文标题**: [Why are we not using Service Workers? — Neciu Dan](https://neciudan.dev/why-are-we-not-using-service-workers)

以下是您提供的文章的概述和要点总结：

Service Workers 是一项被低估的技术，能带来显著的性能提升、离线支持和部署稳定性，但因其复杂的生命周期和缓存管理而未被广泛采用。文章通过 Slack、Mux 和作者自身的案例，展示了其实际应用价值。

- 📉 **现状：未被充分利用**：尽管自 2018 年起所有主流浏览器都支持 Service Workers，但大多数中小型公司并未使用，主要原因是认为不需要、过去遇到困难或害怕缓存问题。
- 🚀 **Slack 案例：启动性能提升 50%**：通过 Service Worker 缓存资产和 Redux 状态，实现“热启动”，使应用在无网络请求时即可显示界面，同时通过版本化缓存桶和定时重新注册，确保新旧版本资产一致。
- 🎥 **Mux 案例：代理重写视频流**：利用 Service Worker 拦截并修改 HLS 视频清单，强制最低分辨率不低于 720p，解决了慢网速下视频模糊的问题，且代码可无缝部署到边缘运行时。
- 🛠️ **作者案例：解决部署导致的懒加载路由 404**：通过 Service Worker 缓存旧版本资产，并轮询 `version.json` 实现平滑更新，避免用户因部署后旧 chunk 被删除而遇到错误或无限刷新。
- ⚠️ **采用障碍：生命周期复杂与缓存恐惧**：Service Worker 的安装、激活、等待阶段容易导致混淆，且错误的缓存策略可能导致用户长期使用旧版本，修复困难。
- 💡 **关键见解：离线不是唯一用途**：Service Worker 的核心价值在于作为网络代理，可用于性能优化、部署策略和请求重写，离线支持只是附带优势。
- 🔧 **简化工具：Workbox**：Google 的 Workbox 模块化库能简化 Service Worker 的路由、缓存和预缓存开发，降低使用门槛。

---

### [Linear 为何如此快速？技术解析](https://performance.dev/how-is-linear-so-fast-a-technical-breakdown)

**原文标题**: [How's Linear so fast? A technical breakdown](https://performance.dev/how-is-linear-so-fast-a-technical-breakdown)

Linear 的速度源于从底层架构到前端交互的数百个精心决策，核心是将浏览器作为数据库、网络请求后台化、并极致优化首屏加载与动画性能。

- 🚀 **浏览器即数据库**：UI 直接从浏览器 IndexedDB 读取，本地先应用变更，再异步同步到服务器，彻底消除网络等待。
- ⚡ **首屏瞬间加载**：通过极致代码分割（21MB 拆成数百个按需加载的块）、预加载模块、Service Worker 缓存，以及内联关键 CSS/JS，让首屏几乎无需等待。
- 🔄 **乐观更新与后台同步**：所有操作（如修改 issue）立即更新本地 MobX 状态，再异步推送服务器，用户从不见加载状态，失败才回滚。
- 🧩 **细粒度响应式更新**：每个属性都是独立 MobX observable，变更仅重绘依赖该字段的组件，50 个 issue 更新只触发 50 个单元格重渲染。
- ⌨️ **键盘优先设计**：所有操作都有快捷键，⌘K 全局命令面板搜索本地数据，无需网络请求，设计上缩短操作路径。
- 🎨 **GPU 动画与短时长**：仅动画 composited 属性（transform/opacity），时长低于 100ms（如 0.12s），避免布局触发，保持流畅。
- 🛠️ **简单技术栈**：React + MobX + TypeScript + Postgres，无复杂框架，坚持客户端渲染，降低复杂度与心智负担。
- 🔐 **先渲染后认证**：假设用户已登录，直接显示本地数据，后台验证会话，失败才重定向，避免加载状态。

---

### [编程文摘：邮件通讯](https://programmingdigest.net/?utm_source=web-archive&utm_campaign=react)

**原文标题**: [Programming Digest: Email Newsletter](https://programmingdigest.net/?utm_source=web-archive&utm_campaign=react)

概述摘要  
- 📧 每周为软件工程师精心策划的编程文摘通讯  
- 👥 已有超过 21,783 名软件工程师订阅，每周一封邮件  
- 📚 精选文章并附简短摘要，节省寻找优质内容的时间  
- 🧠 每周学习新知识，持续提升技能  
- 💬 读者反馈：内容切中需求（如 API 设计），每期都有收获  
- 🏢 读者来自各大科技公司（如 Google、Apple 等）  
- 📅 2013-2026 年运营，提供隐私保护和广告服务

---

### [科技领导力：电子邮件通讯](https://leadershipintech.com/?utm_source=web-archive&utm_campaign=react)

**原文标题**: [Leadership in Tech: Email Newsletter](https://leadershipintech.com/?utm_source=web-archive&utm_campaign=react)

以下是对所提供内容的总结：

本通讯专为 CTO、工程经理及资深工程师设计，旨在提升领导力。每周一和周四发送，精选文章并附简短摘要，帮助读者节省时间并学习新知识。已有 28,973 名工程领导者订阅，并获得高度评价。

- 📧 每周两次推送：每周一和周四发送一封邮件，内容精选自手选文章。
- 🎯 目标读者：面向 CTO、工程经理及资深工程师，聚焦领导力提升。
- ⏱️ 节省时间：提供文章摘要，避免读者自行筛选有价值内容。
- 📚 持续学习：每周带来新知识，覆盖架构、会议、规划及沟通等主题。
- 💬 读者好评：读者称赞其在领导力文章、沟通及授权等技能方面的独到见解。
- 🌍 广泛影响：被来自多家科技公司的领导者阅读，覆盖全球。

---

### [C# 摘要：电子邮件通讯](https://csharpdigest.net/?utm_source=web-archive&utm_campaign=react)

**原文标题**: [C# Digest: Email Newsletter](https://csharpdigest.net/?utm_source=web-archive&utm_campaign=react)

本内容介绍了一封专为.NET 开发者设计的每周精选邮件通讯，旨在节省阅读时间并提升技能。

- 📧 每周一封精心策划的邮件，面向超过20,784名C#工程师
- 📝 提供精选文章及简短摘要，节省寻找优质内容的时间
- 🎯 帮助读者每周学到新知识，并能在工作中实际应用
- 💬 读者反馈：已使用多个技巧，如 LINQ、标准功能标志和操作结果模式
- 🌐 读者来自全球各地，包括多家知名公司
- 📅 通讯由 Bonobo Press 自 2013 年持续运营，提供隐私保护和广告服务

---

### [让开发者保持最新动态 – Bonobo Press](https://bonobopress.com/)

**原文标题**: [Keeping developers up to date â Bonobo Press](https://bonobopress.com/)

概述摘要
- 📰 Bonobo Press 自 2013 年起发布软件新闻通讯，服务超过 80,000 名开发者及 IT 专业人士。
- ✉️ 提供针对软件开发者、技术主管和 CTO 的简洁新闻通讯，深受技术人士喜爱。
- 📢 提供广告服务，帮助触达软件工程师、团队领导及 IT 决策者等专业受众。
- 📞 如有疑问、建议或广告需求，可通过官网联系。

---

### [过往通讯：第 1 页](https://reactdigest.net/newsletters)

**原文标题**: [Past Newsletters: Page 1](https://reactdigest.net/newsletters)

以下是对 React Digest 内容的总结：

React Digest 涵盖了 TanStack Query、Linear 性能优化、React 19 新特性、安全漏洞、可访问性、性能优化等多方面内容，提供了前端开发的最新趋势和实践技巧。

- 🚀 TanStack Query 简化了竞态条件、缓存和后台重新获取，几乎零配置
- ⚡ Linear 通过浏览器存储和后台同步实现即时 UI，无加载指示器
- 🧩 React Server Components 允许每个组件独立获取数据，取代传统 prop drilling
- 🔒 发现 React Flight 协议存在严重 RCE 漏洞，影响默认 Next.js 应用
- 🛠️ React 19 的 useTransition 和 useActionState 简化了异步代码，自动处理状态和错误
- 📉 86% 的前端项目存在内存泄漏，主要是定时器和事件清理缺失
- 🎨 MDN 从 React SPA 转向服务器端 HTML 和 Lit Web 组件，构建时间从 2 分钟降至 2 秒
- 🔄 React Fiber 将渲染拆分为约 5ms 的块，优先处理紧急更新如点击
- 📚 可访问性常见错误包括缺失语义、焦点中断和动态更新无声
- 🧪 use() 钩子打破常规，在渲染时读取 promise，与 Suspense 配合，消除 useEffect 数据获取反模式

---

### [隐私](https://reactdigest.net/privacy)

**原文标题**: [Privacy](https://reactdigest.net/privacy)

概述摘要
本隐私政策详细说明了 React Digest 如何收集、使用和保护您的个人信息，包括电子邮件地址的收集目的、儿童隐私保护、数据访问与删除请求，以及反垃圾邮件政策。

- 🔒 隐私承诺：我们高度重视您的隐私，仅在明确目的下收集和使用个人信息，并采取安全措施防止数据丢失或未经授权访问。
- 📧 信息收集：我们仅收集您的电子邮件地址，用于发送新闻通讯，不用于其他目的。
- 🚸 儿童保护：我们遵守 COPPA，不会故意收集 13 岁以下儿童的信息，网站也不针对该年龄段用户。
- 📋 数据访问：根据英国《数据保护法》，您可发送邮件至[email protected]请求获取我们存储的您的所有信息。
- 🗑️ 数据删除：如需删除数据，请发送邮件至[email protected]并提供必要信息。
- 🚫 反垃圾邮件：我们坚决反对垃圾邮件，您可随时通过邮件中的取消订阅链接退订。
- 📅 版权信息：© 2013-2026 Bonobo Press，涵盖新闻通讯、隐私和广告相关内容。

---

### [媒体资料包 – 倭黑猩猩出版社](https://bonobopress.com/media-kit/)

**原文标题**: [Media Kit â Bonobo Press](https://bonobopress.com/media-kit/)

Bonobo Press 提供面向程序员和技术人员的新闻通讯广告服务，帮助合作伙伴精准触达目标受众，提升参与度和转化率。

- 📊 **高参与度受众**：新闻通讯的参与度是行业基准的两倍以上，通过严格的列表清理实践优先吸引活跃读者。
- 👥 **精准目标群体**：覆盖 CTO、工程经理、软件工程师等技术决策者，主要来自欧洲（35-48%）和美国（30-35%），就职于 Google、Amazon 等知名公司。
- 💰 **多样化定价选项**：Leadership in Tech 每期$2,235（预计点击 365-585 次），Programming Digest $985，C# Digest $1,220，React Digest $1,375，并提供二级展示位置。
- 🚀 **高打开率和点击率**：各新闻通讯的独特打开率在 50-58% 之间，有机点击率（CTR）从 11% 到 22% 不等，确保广告效果。
- 📝 **纯文本广告格式**：采用文本形式以最大化参与度，要求提供链接、标题（<100 字符）和描述（<400 字符），截止日期为发布前 4 天。
- 🤝 **简单订购流程**：包括产品介绍、排期安排、发票支付锁定、素材交付、广告上线和性能报告，建议提前几周联系。
- 🏆 **成功合作伙伴**：涵盖 Okta、Gitlab、Datadog、MongoDB、Pluralsight 等知名品牌，许多合作伙伴重复预订广告位。

---

