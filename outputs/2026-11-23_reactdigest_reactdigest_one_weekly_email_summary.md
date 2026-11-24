# [React server components, without a framework?](https://reactdigest.net/newsletters/2415-react-server-components-without-a-framework)

### [React Digest：电子邮件通讯](https://reactdigest.net/)

React Digest 是面向 React 开发者的每周精选技术周刊，通过人工筛选文章并附简短摘要，帮助前端工程师节省寻找有价值内容的时间，并持续跟进 React 生态变化。页面显示其读者已超过 21,562 名前端软件工程师，内容由 Bonobo Press 运营，版权年份覆盖 2013-2026。

- 📚 **周刊定位**：面向 React 开发者提供每周一封邮件，精选文章并附简短摘要，强调节省筛选内容的时间并每周学习新知识。
- 📈 **读者规模**：页面称已有超过 21,562 名前端软件工程师订阅，读者来自前端工程群体。
- 💬 **读者反馈**：展示的反馈提到文章质量高、有助于跟上 React 持续演进，并特别提到关于 React Concurrent Mode 的文章有收获。
- 🏢 **运营信息**：页面底部标注由 Bonobo Press 运营，版权范围为 2013-2026，并提供 Newsletters、Privacy、Advertise 等入口。

### [React Server Components，不用框架？](https://timtech.blog/articles/react-server-components-rsc-no-framework/)

在 React Server & Client Actions 于 2023 年 10 月 23 日进入 Canary、Next.js 14 于 10 月 26 日宣布 Server Actions 稳定后，作者以 2020 年的 Create React App React Notes App 为样本，尝试不借助框架、仅用 React Canary 与 `react-server-dom-webpack` 等实验 API 迁移到 React Server Components，记录 Flight 序列化、流式渲染、Suspense、use()、路由和表单处理的实际做法与限制，并据此评估自建或迁移 RSC 框架的成本。

- 🗓️ **发布时间线**：React Server & Client Actions 于 2023 年 10 月 23 日公告，Canary 从 `18.3.0-canary-546178f91-20231005` 起提供；Next.js 14 于 2023 年 10 月 26 日宣布 Server Actions 稳定，生态当时主要由 Next.js 采用，Remix 有类似的 Actions。
- 🧩 **RSC 模型**：Server Components 只在服务端运行、不进入客户端 bundle、不会 hydration，不能用 `useState`、`useEffect`、`Context.Provider` 等客户端 API，也不能被 Client Components 直接导入或渲染；它们可向 Client Components 传可序列化 props，包括 Promise，但不能传函数和类。Client Components 是传统可运行在客户端的组件，Shared Components 则按父上下文成为 Server 或 Client Component。
- 🚀 **无框架实验**：作者把 2020 年用 Create React App 做的 React Notes App 迁移为 RSC playground，依赖 Node v18.8.1、npm v9.8.1、Fastify、Webpack、Babel、a-route，并将 `react` 与 `react-dom` 固定到同一 Canary 版本 `18.3.0-canary-8039e6d0b-20231026`。目标是学习 RSC，而非给出最优实现。
- 🛠️ **Flight 工具链**：实验使用 `react-server-dom-webpack/plugin` 根据 `'use client'` 生成客户端 chunk 和 `react-client-manifest.json`，用 `node-register` 在 Node 运行时创建 client/server 引用与代理，用 `react-server-dom-webpack/server#renderToPipeableStream` 把 Server Components 树渲染为 React Flight 格式并流式输出，再用 client 的 `createFromReadableStream` 或 `createFromFetch` 消费。这些 API 完全未文档化，属于实验性绑定。
- 📦 **非典型 SSR**：由于无框架时难以把 Flight 输出高效转成 HTML，作者将 `App` 的 Flight 字符串用 `await finished(flightStream)` 收集后注入 HTML 模板的 `<script id='react-flight' type='react/flight'>`，客户端读取后通过 `new Response(flightResponseText).body` 构造 `ReadableStream`，交给 `createFromReadableStream` 得到 Thenable，再由根组件的 `use()` 渲染。该方案不是真正 HTML SSR，首屏仍需 JavaScript，且会增加 TTFB，只适合学习或特定 SSG 变体。
- 🔄 **瀑布与 Suspense**：Server Component 中用 `async/await` 获取数据会流式输出，但父组件的 await 会阻塞子组件渲染，子组件再 await 会形成 waterfall；把 Promise 下移到消费组件可略好。用 `<Suspense fallback='Loading ...'>` 包裹后，await 会推迟该组件渲染，先发送 fallback chunk，Promise 解析后再发送组件输出 chunk。
- 🧠 **use() 行为**：`use()` 实验 hook 可读取 Promise；若 Thenable 为 pending 或 rejected 会 suspend 组件渲染，fulfilled 后返回结果并恢复渲染，组件会被重放，日志中 `before the use()` 会打印两次。它与 `async/await` 一样可配合 Suspense，产生相同 RSC Payload 和浏览器输出。
- 🔗 **跨边界 Promise**：Server Component 可把 pending Promise 作为 prop 传给 Client Component；Client Component 不能是 async，因此用 `use(itemsPromise)` 消费。Flight 输出会包含对客户端模块的引用和 Promise 引用，一秒钟后再发送 Promise 的解析值，文章称这是最值得继续探索的部分。
- 🧭 **路由限制**：原 Notes App 的自定义路由基于 React Context 与 a-route，仅客户端可用，不兼容 RSC。实验把 routes 定义在 `routes.js`，服务端用于首屏匹配、客户端用于导航，并把 location 等路由 props 传给 `App`；所有路由都是 Client Components，只有根布局及部分子组件是 Server Components。作者建议路由匹配逻辑放在 React 外，路由组件最好统一为全客户端或全服务端。
- ⚠️ **表单与 Actions**：该设置不支持 Server Actions，且出于路由限制和防止公开 demo 被滥用，笔记创建、编辑、删除都在客户端处理。作者试了 React Client Actions，把 async 函数传给 `<form action={...}>` 和 `<button formAction={...}>`；但 `useFormStatus` 只能用于 `<form>` 内部，而按钮在 form 外，因此无法使用，作者希望支持传入 formId。
- 🛡️ **安全机制**：`server-only` 与 `client-only` 包通过 `package.json` 条件导出中的 `react-server` 条件，在错误环境抛出带说明的错误或注入空模块，防止服务端代码被客户端导入；React Taint APIs 的 `experimental_taintUniqueValue` 与 `experimental_taintObjectReference` 可标记不得从服务端传给客户端的值，处理 secrets 时应与 server-only 配合。
- 🏢 **框架建议**：作者不建议产品或平台团队在当前阶段自建 RSC 框架，因为共享构建块不足且文档缺乏，框架会各自实现甚至互不兼容；建议个人和开源贡献者实验。现有全栈 React 框架迁移到 RSC 可简化 code-splitting、内建服务端数据获取、改进 SSR streaming、渐进增强和减小 bundle，但需要数月到数年的研究、逆向、迁移和文档工作，因此建议再等一等。

### [DatAInsights Composer | Progress Telerik](https://www.telerik.com/datainsights-composer?utm_medium=cpm&source=reactdigest&utm_campaign=dt_ww_datainsightscomposer_launch)

Progress 的 DatAInsights Composer 是面向 KendoReact 与 Telerik UI for Blazor 商业应用的 AI 数据可视化组件，允许用户通过自然语言基于经批准的业务数据生成图表、数据视图和洞察，同时由开发者和组织控制数据访问、权限与治理；它把自助式数据探索嵌入应用，并以自带 AI 基础设施和可视化复用降低开发支持成本。

- 🎯 **产品定位**：面向 KendoReact 和 Telerik UI for Blazor 商业应用，以组件形式嵌入，让用户在受控数据集上生成图表、数据视图和洞察，开发者保留访问、权限和治理控制。
- 💬 **自然语言生成**：用户输入自然语言提示即可基于获批业务数据生成交互式图表、表格数据视图，并通过 AI 过滤、聚合和后续追问继续细化结果。
- 🧩 **可视化复用**：生成的图表可存储在应用中，之后继续编辑、优化或复用，减少重复配置。
- 🔑 **自带 AI**：支持 bring-your-own-AI，可连接 Anthropic、Azure、OpenAI 等受支持的 AI 基础设施并管理 AI 访问；推荐模型为 `GPT-5.4 mini Model | OpenAI API`。
- 🛡️ **治理与安全**：应用和组织可定义可用数据集、字段、权限与可视化边界，数据访问仍由应用及组织治理和控制。
- 📦 **订阅范围**：该组件包含在 DevCraft 套装、Telerik UI for Blazor 和 KendoReact 中，并非免费独立产品；目前支持 Blazor 和 React。

### [什么是 React Fiber？React 底层工作原理详解](https://tej.as/blog/what-is-react-fiber)

React Fiber 是 React 16（2017 年 9 月）起使用的协调器，React 19 仍沿用；它把组件树转换成由 fiber 组成的可中断工作单元树，使 React 能在渲染途中暂停、处理更紧急的更新，并从原处恢复，同时用不可中断的提交阶段保证 DOM 不会出现半更新。文章基于 2026 年 9 月 React 主分支源码，拆解 fiber 对象、工作循环、双缓冲、lanes 优先级及其对业务代码的约束。

- 🧩 **Fiber 对象**：每个组件或宿主元素对应一个普通 JavaScript 对象，保存 tag、key、type、stateNode、pendingProps、memoizedProps、memoizedState、updateQueue、flags、subtreeFlags、lanes 和 alternate，并用 return、child、sibling、index 指针把树连接起来；return 表示工作完成后返回的父节点，相当于把调用栈重建为数据。
- 🔄 **可中断工作循环**：同步更新使用 workLoopSync，并发更新使用 workLoopConcurrentByScheduler，两者唯一区别是后者在每次 performUnitOfWork 前检查 !shouldYield()；当前源码默认约 5 毫秒让出主线程，workInProgress 作为模块级变量使 React 回来时从停下的 fiber 继续。
- 🧭 **渲染与提交两阶段**：render 阶段调用组件、对比新旧 fiber，可暂停、重启或丢弃；commit 阶段不可中断，依次执行 commitBeforeMutationEffects、commitMutationEffects、commitLayoutEffects，再运行 useEffect 的被动效果，因此 DOM 变更一次性完成。
- 🎨 **双缓冲树**：React 同时维护 current 树（屏幕上的树）和 work-in-progress 树，每个 fiber 的 alternate 指向另一棵树中的对应节点；新树完成后以 root.current = finishedWork 交换，旧 current 成为下一次渲染的复用空间，半成品可安全丢弃。
- ⚡ **Lanes 优先级**：每个更新分配一个 lane，即 31 位数字中的一位；fiber 的 lanes 可同时保存多个待处理优先级并用位掩码快速检查。SyncLane 用于点击或按键等离散事件，InputContinuousLane 用于拖动或滚动，DefaultLane 用于普通更新，transition lanes 用于 startTransition，IdleLane 用于可等待工作。
- 🛠️ **向下与向上遍历**：performUnitOfWork 调用 beginWork 渲染组件并返回第一个子节点；没有子节点时 completeUnitOfWork 调用 completeWork 完成该 fiber，准备 DOM 变更并把 flags 冒泡到父节点的 subtreeFlags，然后转向 sibling 或 return 向上，使无变化子树可被跳过。
- 📦 **元素与 fiber 的生命周期**：JSX 生成的是 React element，只描述本次渲染想要的屏幕，渲染后即被丢弃；React 19 用 Symbol.for("react.transitional.element") 标记元素。fiber 则跨渲染保留组件实例的类型、props、state、effects 和优先级，是 React 记住现有屏幕的载体。
- 💡 **对业务代码的约束**：render 阶段可能执行组件后丢弃结果再执行，因此组件渲染必须纯粹；副作用应放在 effect 中，在提交后运行；列表项需要稳定 key，让 React 按 type 和 key 匹配新旧 fiber 并保留状态；慢更新用 useTransition 或 useDeferredValue 标记为 transition。
- 🔮 **实验性调度与未来**：源码中存在默认关闭的 enableThrottledScheduling 标志，若启用会在 transition 期间改为每 25 毫秒让出一次，避免动画使渲染得不到机会执行；文章明确表示不确定它是否发布，也不确定 React Compiler 全面记忆化后这些内部规则会以何种程度继续显现。

### [本地视觉回归测试 | Mainmatter](https://mainmatter.com/blog/2026/11/03/local-visual-regression-testing/)

文章讨论如何用 Playwright 的本地视觉对比能力配合 Docker 标准化环境，为 AI 编码代理建立更紧的视觉回归反馈闭环：代理可在本地运行截图测试、读取期望/实际/差异图并按需求判断是否更新快照，从而减少对 Percy、Chromatic 等 PR 后服务的依赖和成本；同时强调跨平台一致性、快照更新风险、Git 历史膨胀与方案适用性等限制。

- 🎯 **本地闭环**：文章针对 AI 代理参与前端开发后视觉回归风险上升、Percy/Chromatic 需提交 PR 后等待 diff 且成本随截图量增长的问题，提出用本地视觉回归测试把反馈缩到类似单元测试的粒度。
- 🧩 **Playwright 截图**：使用 `@playwright/test` 的 `expect(page).toHaveScreenshot()`；首次运行会生成并保存 PNG 基线，失败时在 `test-results` 输出 expected、actual 和 diff 图，确认变更后用 `npx playwright test --update-snapshots` 更新快照。
- 🐛 **意外变更示例**：示例让 Claude 只把强调色改成 Svelte 橙色 `#ff3e00`，测试报告 6216 个像素不同、比例 0.01；查看 diff 发现它还误删了“Pixel Perfect”标题周围的 glitch 效果，说明视觉测试能捕获未请求的改动。
- ⚙️ **Docker 标准化**：为消除 macOS、Linux、Windows 截图差异，使用官方 Playwright 镜像构建 `Dockerfile.visual-tests`，在 `docker-compose.yml` 中固定 `linux/amd64` 和 `PLAYWRIGHT_VERSION: 1.62.0`，并通过脚本校验镜像与项目内 Playwright 版本一致，避免重复下载浏览器。
- 🌐 **跨平台差异**：文章展示同一页面在容器中生成 `homepage-1-linux.png` 后与 macOS 截图不同，原因是 CSS 使用了 `-apple-system`、`SF Mono` 等 macOS 系统字体，而 Linux 缺失这些字体；Docker 让本地与 GitHub Actions 使用同一 Linux 运行环境。
- 📈 **成本压力**：Actual Budget 每次 CI 约 440 张截图，PR 从约 70 增至约 140，其中约 40% 带 `[AI]` 标签，AI PR 提交中位数为 4 次而人类为 2 次，截图量约增至 2.5–3 倍；估算 Chromatic 从约 $490 涨到约 $1600，TurboSnap 下约 $180 到 $400，Percy 从约 $3300 涨到约 $8300，而 Playwright CI 分钟成本约从 $19 到 $47。
- 🧠 **代理技能**：建议在 `./.agents/skills/visual-regression` 添加技能，提示代理在视觉变更时运行 `pnpm test:visual`，检查失败测试及 expected、actual、diff 图，只有确认改动完全符合用户请求时才运行 `pnpm test:visual:update`，并警告更新快照是破坏性操作；可用专用 subagent 避免上下文污染。
- ⚠️ **适用边界**：文章强调这是可选方案而非通用答案：视觉回归本身难做，质量不足会增加维护成本；提交截图会让 Git 历史快速膨胀，可考虑把基线放 S3、测试前下载并在测试后上传更新，但该示例仓库尚未公开。

### [声明式拖拽](https://declarative-dragging.github.io/)

论文《Declarative Dragging》提出一种声明式拖拽范式：开发者不再手写几何计算、视觉反馈和动画，而是指定元素可被拖向哪些未来模型状态，系统再据此合成拖放交互。作者实现了面向 Web SVG 界面的 `Dragology` 库，并将该方法用于数学探索、并行表示、编程环境重构和游戏等场景；该论文获 UIST 2026 最佳论文奖。

- 🚀 **最佳论文发布**：《Declarative Dragging》由 Joshua Horowitz、Andrew Blinn 和 Jeffrey Heer 撰写，获 UIST 2026 最佳论文奖，论文共 16 页，文章编号为 168。
- 🧩 **核心机制**：`D2` 是模型驱动的：界面作者只需说明拖动某元素应到达哪些未来模型状态；引擎会推测性渲染这些状态为视图树，提取被拖元素在各渲染中的位置，并据此合成拖放交互，无需作者处理几何、反馈和动画细节。
- 🛠️ **可组合设计**：`D2` 支持组合：简单的模型驱动拖放行为可组合成更复杂的行为，修饰器可叠加浮动、吸附和过渡等特性，以扩大表达范围和可定制性。
- 📦 **Dragology 实现**：`D2` 被实现为 `Dragology` 库，面向 Web 上的 SVG 界面；演示包括 algebra、twisted trees、bézier curve、braid、card piles、face、trominoes 和 sprouting tree 等交互作品。
- 🔄 **并行表示**：论文发表后，作者展示了适合并行表示的交互：在 permutation lab 中，同一系统的多个表示可联动更新，甚至在拖拽过程中也能实时反映各表示之间的关系。
- 🎯 **应用拓展**：Andrew 正将声明式拖拽引入现有应用，包括 Hazel 编程环境，使重构操作变得可触摸和可发现；他还重启数学游戏项目，将其适配到游戏手柄并从 2D 画布扩展到 3D 世界。

### [恰到好处的光照：实时全局光照探索 - The Blog of Maxime Heckel](https://blog.maximeheckel.com/posts/lighting-that-feels-just-right/)

Maxime Heckel 在文章中记录了自己为实时渲染近似全局光照而做的技术探索：从基于屏幕空间的 GI 出发，转向更稳定的探针式 GI，再叠加时间累积、反射和大气散射天空光，最终在浏览器中实现包含颜色溢出、离屏光照、动态天空和反射的间接照明效果，同时坦率讨论了性能、精度和实现边界。

- 🧩 **从直接光到间接光**：文章以 Blinn-Phong 的 max(dot(normal, lightDirection), 0.0) 只能表达直接光为起点，指出真实光照会在表面反弹，产生阴影区补光、白墙反光和彩色表面染色等间接光效果，目标是用较低成本近似全局光照。
- 💻 **屏幕空间 GI**：首个实现用 TSL 的 mrt 捕获 output、normal 和 albedo，从 depth 重建世界坐标，在每个可见表面法线半球内做 cosine-weighted 采样，每像素每帧追踪 8 条射线，以深度比较和 0.2 容差判定命中并读取颜色；结果有颜色溢出但噪声明显。
- 🔄 **时间累积**：通过 render target 保存历史，ping-pong 读写纹理并按 1/(count+1) 递推平均，历史窗口上限 128 帧；用 frameIndex 和 blue noise 变化采样方向，低射线数下获得更平滑结果，但相机移动需重置或重投影。
- ⚠️ **SSGI 局限**：全分辨率计算成本随像素增长，时间累积在相机移动时产生拖影或需重置，屏幕空间无法计算离屏物体，反射也受可见性限制，例如反射墙中缺失物体背面。
- 🧭 **探针式 GI**：改用世界空间探针：在 PROBE_MIN/PROBE_MAX 包围盒内按 grid 和 probeSpacing 布点，用 compute shader 为每个探针生成 6 个方向 lobe 并存入 2D atlas，向场景几何追踪射线，收集自发光、太阳漫反射和遮挡信息；相比 SSGI 可在相机移动时保留光照并纳入离屏发光体，但间接光更柔和、精度较低，网格越密越能捕捉细节但更新和存储成本更高。
- 🎯 **探针查询**：渲染时重建可见表面世界坐标，在最近探针的 3×3×3 邻域内按距离权重混合，权重在 d<0.5 时为 0.75-d²，否则为 0.5×(1.5-d)²；跳过遮挡探针，并按法线轴向采样对应 lobe，再乘以 albedo。
- ⚡ **滞回更新**：为灯移动后避免从零累积，引入 hysteresis：示例 0.95 时历史占 95%、新测量占 5%，stableFrames 在光照稳定时增加历史权重，光照变化时重置 stableFrames 但不清空 atlas；仍有突变光照下的 ghosting，适合近乎静态或缓慢变化光源。
- 🎨 **反射与材质**：增加 roughness 和 metalness render target；反射从可见点沿 reflect(-v,n) 追踪，命中后叠加 emission、太阳直接光和探针间接光，并用 Schlick Fresnel 的 f0=mix(0.04, albedo, metalness) 与 (1-roughness)² 的 mirrorWeight 控制强度；当前只做单次反射，非递归，粗糙度只是淡出镜面项而非 GGX 模糊。
- 🌐 **天空光**：用独立 compute shader 将大气散射预计算为天空纹理，探针射线未命中几何时用 sampleSky(direction) 补入天空光，反射未命中时也采样天空；太阳移动时天空颜色参与间接照明，带来自然染色和更柔和阴影。
- 🛠️ **演示与边界**：浏览器 demo 使用 traceWorld 对球和盒求交，复杂几何需 BVH 或三角形网格；作者称实现非生产级，建议参考 Three.js 的探针 GI，并提及 Radiance Cascade 作为后续方向。

### [我们如何将 Next.js 内存从约 5GB 降到约 1GB：一个 react-query 定时器让每个 SSR 请求无法释放 · rohitpotato](https://rohitpotato.xyz/thoughts/ssr-requests-still-alive)

Zepto 的 Next.js SSR 服务每个 Pod 常驻约 4.8 GiB 内存，强制 GC 后几乎不下降，这看起来像内存泄漏，但真正的根源是 react-query v3：它在服务端渲染时，由每个 `Query` 的构造函数立即启动一个 2–5 分钟的 `setTimeout` 缓存过期定时器，而 SSR 期间 `useEffect` 不执行，查询无人订阅，定时器会一直运行到超时且毫无用处；同时 Node 会把当前请求的 AsyncLocalStorage store 复制到每个 timer 上，而该 store 引用了请求、响应、响应缓冲和 OpenTelemetry span，由于待触发的 timer 是 GC root，每个已完成的请求都被固定住数分钟。修复方式是在服务端 `QueryCache.build` 中强制 `cacheTime: Infinity`（`isValidTimeout` 会排除 Infinity，因此不会创建定时器），生产环境单 Pod 内存随即从约 4.8 GiB 降到约 1.2 GiB 并保持平稳。

- 🐛 **问题现象**：Pod 内存稳定在约 5 GB，GC 正常运行但内存回收不下来，强制 GC 后堆也几乎不动；在生产构建下做快照对比发现，每处理约 1 个请求就多保留约 1 MB 内存，336 个请求对应 336 个仍存活的 `ServerResponse`，以及它们的 socket 和约一千个 OpenTelemetry span。
- 🔍 **排查方法**：不要在 `next dev` 里分析内存，因为 webpack、HMR 和 source map 会掩盖问题；应使用生产构建并从 inspector 启动，通过 Chrome DevTools Protocol 先连续两次 `HeapProfiler.collectGarbage` 再拍快照，并把 `addHeapSnapshotChunk` 分块直接写入磁盘（快照太大，无法用 `join('')` 放进单个字符串）。
- 🧭 **保留路径分析**：因为增长分散在约一百万个字符串、约 1.6 万个 `ArrayBuffer` 和数十万普通对象上，支配树（dominator tree）无济于事——最大对象仅约 2 MB 且是 Next 自带的有界 fetch-cache LRU。改为从 GC roots 做 BFS 求最短保留路径、跳过 weak 边，才暴露出所有 `ServerResponse` 都被同一个 `timerListMap[300000]` 下的 `Timeout` 引用。
- 🧩 **根因机制**：react-query v3 的 `Query` 构造函数会立即调用 `scheduleGc()`，即 `setTimeout(() => this.optionalRemove(), cacheTime)`，默认 5 分钟；浏览器里组件订阅会取消定时器，但 v3 在 `useEffect` 中订阅，SSR 期间 effect 不执行，查询创建后无人订阅，定时器跑满全程，而它要清理的 `QueryClient` 在渲染结束时就已被丢弃。
- 🔗 **内存被长时间占用**：Node 会把当前 AsyncLocalStorage store 复制到新建的 `setTimeout`、promise、socket 操作上（`kResourceStore`），以保证回调里 `getStore()` 可用；Next.js 每个请求都在 ALS 中渲染（`cookies()`、`headers()`、`after()` 依赖它），该 store 引用 req/res 等全部相关对象，而待触发的 timer 是 GC root，于是一个请求级的 `useQuery` 就能让整个请求存活 2–5 分钟。
- 🛠️ **修复方案**：服务端使用 `ServerQueryCache extends QueryCache` 覆写 `build()`，为每个 query 注入 `cacheTime: Infinity`；`isValidTimeout` 要求值不是 `Infinity`，因此定时器根本不会创建。安全性来自三点：服务端 `QueryClient` 本就按请求创建并在渲染后丢弃，所以「永不淘汰」等于「活到请求结束」；react-query 取 `Math.max(this.cacheTime, options.cacheTime)`，hook 传入的 1/2/3/5 分钟无法覆盖 Infinity；浏览器端仍走默认缓存，行为不变。
- 🧪 **回归防护**：新增一个在构建服务端查询时监视 `setTimeout` 的测试，旧代码下失败、修复后通过，防止此问题悄悄回归。
- ⚠️ **升级的局限**：react-query v4/v5 只是把服务端的 `cacheTime`/`gcTime` 默认值改为 `Infinity`；任何显式传入有限值的 query 在 SSR 时仍会启动真实定时器，后果相同。该问题记录于 TanStack/query#11320，截至 2026 年 11 月提议的修复尚未合并，`main` 上的 `scheduleGc()` 对有限 `gcTime` 依旧启动定时器，所以即使上 v5，自定义 `gcTime` 的 hook 仍需这道防护。
- 📈 **修复效果**：本地堆在预热、+280 请求和持续负载下分别为 70/75/84 MB 并保持平稳，增长仅来自 JIT 编译代码；2、3、5 分钟定时器列表从约 900 个应用定时器降为零，GC 后保留的响应缓冲从 373 MB 降到 7 MB；生产平均每 Pod 内存从约 4.8 GiB 降至约 1.2 GiB，并在随后数日保持平稳。
- 🎯 **扩缩容副作用**：该服务同时按 CPU 和内存自动扩缩容，内存原先总是先越过阈值，实际上在主导副本数；泄漏修掉后只剩 CPU 能触发扩容，而 Node 服务很少把 CPU 推到阈值，导致副本数缩减、单 Pod 流量上升、延迟变高。最终把 CPU 作为真正的扩容信号，内存阈值只作安全网保留；修完内存问题后应观察数天的副本数与延迟。
- 💡 **通用经验**：请求期间创建的任何 `setTimeout`（以及长期 pending 的 promise）都会把请求上下文固定到触发为止，与回调是否使用上下文无关；面向浏览器编写的库常因缓存淘汰、轮询、防抖、重试而制造这类定时器。「GC 不释放」等价于「还有引用」，先 diff 两份快照找出增长的是什么，再从 GC roots 沿保留路径找出为什么；没有单个大对象时不要依赖支配树；测量务必在强制 GC 之后进行。

### [编程文摘：电子邮件通讯](https://programmingdigest.net/?utm_source=web-archive&utm_campaign=react)

提供的正文是 Programming Digest 的订阅介绍页，并非具体技术文章：该通讯面向软件工程师，每周人工精选文章并附简短摘要，宣称已有超过 20,139 名订阅者，强调帮助读者节省筛选内容的时间并持续学习，同时展示读者正面反馈。

- 📚 **周刊定位**：Programming Digest 是面向软件工程师的每周精选通讯，强调人工挑选文章并附简短摘要。
- 📈 **订阅规模**：页面显示已有超过 20,139 名软件工程师订阅该每周邮件。
- ✅ **订阅价值**：主打帮助读者节省寻找优质内容的时间，并每周学习新内容。
- 💬 **读者反馈**：页面引用读者评价，称其内容涉及 API 设计、发现优质读物，并能从每期中有所收获。

### [科技领导力：电子邮件通讯](https://leadershipintech.com/?utm_source=web-archive&utm_campaign=react)

Leadership in Tech 是一份面向 CTO、工程经理和资深工程师的精选技术领导力周刊，目标是帮助读者成为更好的领导者；邮件每周一和周四发送，页面称已有超过 28,169 名工程领导者订阅，内容以人工挑选的文章和简短摘要为主，帮助读者节省筛选内容的时间并持续学习。

- 🎯 **目标读者**：面向 CTO、工程经理和资深工程师，聚焦技术领导力提升。
- 🗓️ **发送节奏**：每周一和周四发送邮件，页面称已有超过 28,169 名工程领导者订阅。
- 📚 **内容形式**：提供人工精选文章及简短摘要，强调节省寻找有价值内容的时间并便于每周学习。
- 💬 **读者反馈**：页面展示的反馈提到领导力建设文章、架构讨论、会议、规划和沟通，以及授权（delegation）等主题。

### [C# Digest：电子邮件通讯](https://csharpdigest.net/?utm_source=web-archive&utm_campaign=react)

C# Digest 是面向 .NET 开发者的每周精选邮件通讯，主打由人工筛选文章并附简短摘要，帮助读者节省寻找高质量内容的时间，并称已有超过 21,978 名 C# 工程师订阅。

- 📦 **订阅通讯**：以每周一封邮件的形式提供内容，面向 .NET 开发者，页面显示已有超过 21,978 名 C# 工程师订阅。
- 📚 **精选摘要**：每期由人工挑选文章并提供简短摘要，目标是减少筛选内容的时间，让读者每周学习新知识。
- 💬 **读者反馈**：读者提到曾在工作中使用通讯推荐的内容，并关注标准功能开关、LINQ、DiagnosticListener、Operation Result Pattern 等主题。
- 🔄 **实践影响**：有读者表示因 Operation Result Pattern 一文将其推荐给朋友和同事，并迁移了自己的 Azure Function。

### [让开发者随时掌握最新动态 – Bonobo Press](https://bonobopress.com/)

Bonobo Press 自 2013 年起面向软件开发者、IT 专业人士和技术人员发布软件技术通讯，目前覆盖超过 94,000 名读者，并提供面向技术细分人群的广告投放渠道。

- 🏢 **读者规模**：Bonobo Press 自 2013 年起持续发布软件通讯，读者超过 94,000 名，包括软件开发者、IT 专业人士和技术人员。
- 📚 **通讯定位**：通讯面向开发者、工程经理、技术负责人和 CTO，特点是内容干净、精炼并帮助读者节省时间。
- 📈 **广告触达**：广告服务可连接活跃的软件工程师、团队负责人、工程经理、CTO 和 IT 决策者，帮助产品和服务触达技术细分受众。
- 🔗 **订阅与资源**：用户可查看具体出版物并订阅，也可获取媒体资料包、联系团队或洽谈广告合作。

### [往期通讯：第 1 页](https://reactdigest.net/newsletters)

总结失败：模型未返回符合格式的摘要。

### [隐私](https://reactdigest.net/privacy)

React Digest 的隐私政策页面由 Bonobo Press 标注版权（2013-2026），说明其在邮件通讯场景下收集、使用和保护个人信息的规则：仅在收集前或收集时明确目的，按目的限定使用与保留，采取合理安全措施，并赋予用户访问和删除数据的渠道；同时声明遵守美国 COPPA、反对 SPAM，且邮箱仅用于新闻通讯并可随时退订。

- 🎯 **用途限定**：在收集个人信息前或收集时明确目的，仅用于指定目的及兼容目的，除非取得个人同意或法律要求。
- 📦 **收集范围**：就邮件通讯而言，仅收集电子邮箱地址用于发送邮件新闻通讯，不将邮箱用于其他目的。
- 🛡️ **安全保障**：以合法公平方式收集，并在适当情况下告知或取得同意；采取合理安全措施防止丢失、盗窃、未经授权访问、披露、复制、使用或修改。
- ✅ **用户权利**：依据英国《1998 年数据保护法》，用户可申请获取所存个人资料，但受某些法律限制；也可通过邮件申请删除数据。
- ⚠️ **儿童隐私**：遵守美国 COPPA，不有意收集或存储 13 岁以下儿童信息，网站也不面向或设计为吸引该年龄段儿童；如发现相关情况可立即联系。
- 💬 **反垃圾邮件**：邮箱仅用于新闻通讯，用户可随时点击邮件中的退订链接取消订阅；政策明确反对并不参与任何形式的 SPAM。
- 📝 **保留与准确性**：仅在实现目的所需期间保留个人信息，并确保数据与用途相关且在必要范围内准确、完整和最新；同时公开相关政策与实践信息。

### [媒体资料包 – Bonobo Press](https://bonobopress.com/media-kit/)

Bonobo Press 的媒体资料包（最后更新于 2026 年 10 月 19 日）介绍其面向开发者、工程管理者和技术领导者的四份技术周刊，并给出订户规模、打开率、点击率、赞助价格、广告格式与预订流程；核心卖点是高于行业基准两倍以上的互动率、严格的名单清理，以及以纯文本原生内容触达软件交付相关决策者和工程师。

- 🎯 **刊物矩阵**：Bonobo Press 运营 Leadership in Tech、Programming Digest、C# Digest、React Digest 四份技术周刊，分别覆盖技术管理者、软件工程师、C#/.NET 开发者和 React 前端开发者，强调互动率高于行业基准两倍以上，并通过严格名单清理优先保留活跃读者而非追求列表规模。
- 📊 **领导力版**：Leadership in Tech 面向工程经理、技术负责人、CTO 等决策者，每周一和周四发布，订户 29,158，独立打开率 51.47%，自然点击率 11.38%，单期赞助 $2,570，预计点击 365-585，CPC $4.39-$7.04，次级广告位 $1,799。
- 📈 **编程摘要**：Programming Digest 面向软件工程师、Web 与桌面应用开发者，每周发布，订户 21,149，独立打开率 45.57%，自然点击率 14.83%，单期赞助 $1,135，预计点击 273-493，CPC $2.3-$4.16，受众偏后端或全栈。
- ⚙️ **C# 周刊**：C# Digest 面向使用 C# 构建 Windows、.NET 原生桌面、Web 和移动应用的开发者，每周发布，订户 21,077，独立打开率 53.41%，自然点击率 21.63%，单期赞助 $1,345，预计点击 411-631，CPC $2.13-$3.27，受众更偏企业级和大型公司。
- 💻 **React 周刊**：React Digest 面向使用 React 构建交互式 Web 应用的前端开发者，每周发布，订户 22,463，独立打开率 49.86%，自然点击率 12.17%，单期赞助 $1,375，预计点击 180-400，CPC $3.44-$7.64，次级广告位 $962。
- 🌐 **受众分布**：四个刊物多数订户来自欧洲和美国：Leadership in Tech 与 Programming Digest 为欧洲 40%、美国 35%，C# Digest 为欧洲 48%、美国 32%，React Digest 为欧洲 35%、美国 30%。
- 📝 **广告格式**：Newsletter 为纯文本格式，广告嵌入正文；文案格式为链接地址 URL、标题（少于 100 字符最佳）、描述（少于 400 字符的一段），截稿为发布日前 4 天。
- 🗓️ **预订流程**：多数广告位提前 1-2 个月预订；时间敏感活动需在目标日期前至少 6-8 周联系；发票付款锁定排期，随后完成文案协作、上线和效果报告。
- 🔗 **合作伙伴**：近期合作伙伴覆盖访问管理、开发者工具、可观测性、安全、数据、客户互动、教育、项目管理和平台等类别，包括 Okta、GitLab、Datadog、MongoDB、Twilio、Pluralsight、O'Reilly、Retool、Webflow、PostHog 等，且常复购赞助。
