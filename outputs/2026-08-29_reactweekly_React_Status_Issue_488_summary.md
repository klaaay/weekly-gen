### [](https://lovable.dev/blog/how-we-migrated-lovable-dev-away-from-nextjs)

**原文标题**: [How we migrated lovable.dev away from Next.js and turned it into another Lovable app | Lovable](https://lovable.dev/blog/how-we-migrated-lovable-dev-away-from-nextjs)

overview summary  
- 🚀 lovable.dev 从 Next.js 迁移到 TanStack Start，并改为由 Lovable 平台自身托管，成为其 6000 多万个应用之一。  
- 🐶 核心动机是“吃自家狗粮”：通过亲身体验用户痛点、推动单应用大规模扩展，并把最佳实践回馈给构建代理。  
- 🧭 迁移策略采用双框架并行、按路线分组逐步切换，避免了“大爆炸”式重写，并借助 AI 辅助大幅提升效率。  
- 📉 迁移后中位 TTFB 降低 49%，构建时间从 12+ 分钟降至 6–9 分钟，但长尾延迟需额外优化。  
- 🤖 AI 在代码迁移、审查自动化和规划调度中发挥了关键作用，使单人即可完成原本需要多团队协作的迁移。  
- 🔮 未来计划支持导入和编辑任意现有软件（包括 Next.js 应用），进一步拓展 Lovable 的能力边界。  

- 🏠 原有 Next.js 应用托管在 Vercel，表现良好，但团队决定迁移到自家平台以加深产品反馈闭环。  
- 📈 目标之一是解决“单应用千万级访问”的独特挑战，区别于平台上大量中小流量应用的常规场景。  
- ⚙️ Lovable 应用基于 TanStack Start 构建，每个应用运行在 Cloudflare workerd 的 V8 isolate 中，入口 worker 动态加载并分发请求。  
- 🧩 并行运行两个框架：代理 worker 按路线和用户决定由哪个框架响应，内部导航与跨框架硬导航体验差异明显。  
- 🗂️ 将路线按用户旅程分组迁移，每组用功能开关控制灰度比例，并利用 View Transitions API 平滑硬导航体验。  
- 🔒 通过“框架粘性”保证用户在同一路线组内始终使用首次命中的框架，并以统一路由注册表作为代理和两端框架的单一事实源。  
- 🧪 通过内部搜索参数实现确定性功能开关，让端到端测试不受随机灰度影响。  
- 📦 共享代码层目标实现：最终 90–95% 代码与框架无关，Next.js 专属代码仅占 3%，用 lint 规则强制隔离。  
- 🔌 适配器模式实现接口式依赖注入，共享代码通过 `@platform/router` 等别名导入，无需显式 DI 容器。  
- ✂️ 提前替换 next/font、next/image、认证和 i18n 方案，缩小框架依赖面，降低迁移风险并带来额外性能收益。  
- 🤖 AI 迁移流程：先沉淀可复用的 agent 技能，再提升规划抽象层级，用可量化指标驱动批量 PR 栈，最后引入审查自动化防止回归。  
- 🚦 流量切换按路线组逐步灰度：内部测试 → 全公司测试 → 1% 到 100%，并限制同时只进行一个外部灰度，整个过程约两个月。  
- 💥 曾发生 11 分钟线上事故：内存超限导致 isolate 被频繁杀死，错误率飙升至 50%；根因是无关的静态 JSON 数据压垮了内存临界状态。  
- 🧠 修复内存问题：避免模块级解析大 JSON、精简列表 API 字段、用空桩替换服务端不需要的客户端代码，显著降低 worker 内存占用。  
- 💻 TanStack Start 相比 Next.js：本地开发启动更快（10s/1.5GB vs 70s/8GB），抽象更少更直观，agent 出错的概率更低。  
- ⚠️ 但 TanStack Start 在生产构建上需要较多底层配置（17 个自定义构建插件），不像 Next.js 那样开箱即用。  
- 🏆 主要收益是 dogfooding 和文化变革：Lovable 员工现在可以用自家产品直接编辑 lovable.dev，实现“人人都是构建者”。  
- 🔭 下一步：利用沙箱能力支持导入并编辑任意现有软件，包括 Next.js 应用，进一步扩大 Lovable 的适用范围。

---

### [](https://www.tigerdata.com/go/trial?utm_source=content-syndication&utm_medium=referral&utm_campaign=react-status-newsletter)

**原文标题**: [Postgres for time-series workloads at any scale. | Tiger Data](https://www.tigerdata.com/go/trial?utm_source=content-syndication&utm_medium=referral&utm_campaign=react-status-newsletter)

Tiger Data 提供基于 Postgres 的时序数据云服务，强调海量规模、弹性扩展、企业级安全与高可用，并支持丰富的生态集成与快速部署。

- 📊 支持极致规模：单服务可处理每天 3 万亿指标、3 PB 数据、1 千万亿数据点。
- 🎁 提供 $1000 试用额度（30 天有效），无需信用卡，仅限新用户。
- ⚙️ 轻松扩展：读写分离，副本集群最多 10 节点，并支持 SSD/S3 分层存储，兼顾性能与成本。
- 💸 不为闲置容量付费：计算与存储分离，可独立伸缩，按需优化成本与性能。
- 🛡️ 高可用保障：多可用区集群、自动故障转移、时间点恢复及跨区域备份。
- 🔐 企业级合规：通过 SOC 2、HIPAA、GDPR 认证，支持加密、SSO、RBAC 与审计日志。
- 📈 深度可观测性：提供查询下钻和仪表盘，可向 CloudWatch、Datadog、Prometheus 发送指标。
- 🚀 快速启动：几分钟内完成数据库部署，支持 SQL、CLI、Terraform、Cursor 或 Claude Code 管理。
- 🔌 生态集成：可与主流云平台及更广泛的 Postgres 生态系统无缝对接。
- 🤝 企业级支持：提供合同化 SLA、区域数据隔离、7×24 小时专家支持及企业级响应保障。

---

### [我们如何在 React、Vue 和 Svelte 中构建快速数据网格 | SVAR 博客](https://svar.dev/blog/building-data-grid-in-react-vue-svelte/)

**原文标题**: [How We Built a Fast Data Grid in React, Vue, and Svelte | SVAR Blog](https://svar.dev/blog/building-data-grid-in-react-vue-svelte/)

本文基于SVAR团队在React、Svelte和Vue中实现同一高性能数据网格组件的经验，指出性能瓶颈主要来自DOM渲染等框架无关因素，而非框架本身；同时分享了虚拟化、记忆化、数据流等通用优化手段，并给出了务实的实践建议。

- 🧩 核心发现：高性能数据网格的昂贵部分几乎与框架无关，框架间的真实差异远小于“框架大战”所暗示的。
- 🏗️ 架构设计：将组件拆分为框架无关的引擎核心+每种框架的薄集成层，使跨框架维护变得现实。
- 📜 虚拟化为基线：只渲染可视区域的行列，用隐藏占位元素模拟完整数据；三个框架均无内置支持，全靠DOM工程实现。
- 📏 初始尺寸难题：通过先渲染空容器并挂载ResizeObserver解决，等待首个非零尺寸后再渲染数据。
- ⚛️ React的useLayoutEffect：可在浏览器绘制前测量并更新，但实践中仍需ResizeObserver兜底，因为布局常依赖外部资源。
- 🌍 SSR冲突：虚拟化与SSR天然矛盾，标记为client-only组件即可解决hydration错误，代价可接受。
- 🔁 派生状态与记忆化：React的useMemo、Svelte的$derived、Vue的computed在虚拟化数学计算中几乎可逐行翻译；React需手写依赖数组，其他自动追踪。
- 🔄 执行模型差异：React每次渲染重跑整个函数体，Svelte/Vue仅执行一次setup；前者显式但风险高，后者默认安全但可能忘记响应式。
- 📦 单一store三适配器：用同一个框架无关响应式store，分别通过writables、subscribe helper和hooks接入；React需额外计数器hook处理原地数组变更。
- 📊 数据更新：React中通过树冒泡更新在网格规模下效率低，直接订阅store能跳过整树重算；Svelte/Vue原生可限制子树，但统一store更易维护。
- 📈 性能数据：虚拟化时从1000行增至100000行仅增加约30ms；渲染全部行时耗时增长一个数量级，但三框架差距仍在15%以内，证明DOM主导一切。
- ✅ 实践建议：优先限制DOM规模（虚拟化、简化标记），再策略性记忆化重计算，并认真设计数据流（外部store或状态模块）。
- ⚠️ 归因提醒：框架限制真实但稀少，实现错误（缺失虚拟化、未优化的重计算、状态提升过高）才是常见拖慢应用的根源。

---

### [](https://nextjs.org/blog/august-2026-security-release)

**原文标题**: [August 2026 Security Release | Next.js](https://nextjs.org/blog/august-2026-security-release)

概述：Next.js 发布紧急安全更新，修复两个关键严重程度的漏洞，涉及 AVIF 图像优化导致的远程代码执行，以及 Windows 服务器上的未认证远程代码执行。建议用户立即升级到指定版本。

- 🔴 严重漏洞：AVIF 图像优化 API 存在未认证远程代码执行风险（GHSA-2xp9-vwfh-vxw4 / GHSA-g89c-p67h-r497），源于底层 libheif 库缺陷，已禁用 AVIF 优化直至上游修复。
- 🪟 严重漏洞：Windows 托管服务器上 Pages Router 与 App Router 组合可能导致未认证远程代码执行（CVE-2026-75604 / GHSA-p293-qw3h-jr36），Linux 和 macOS 不受影响，且无已知变通方案。
- ⚙️ 补丁版本：已发布 v16.3.3（Active LTS）和 v15.5.24（Maintenance LTS），请立即更新依赖（npm install next@15.5.24 或 next@16.3.3）。
- 🛡️ 安全计划：Vercel 开源漏洞奖励计划持续招募研究者，安全相关问题可联系 security@vercel.com。
- 📅 发布说明：原本计划上周公布，因发现新的上游依赖漏洞而提前至今日发布。

---

### [](https://github.com/react/react/pull/37290)

**原文标题**: [[flags] Enable enableParallelTransitions by acdlite · Pull Request #37290 · react/react · GitHub](https://github.com/react/react/pull/37290)

该 PR 是 React 核心团队对 `enableParallelTransitions` 功能标志的默认值进行翻转，将其在 OSS 和 canary 构建中正式启用，并同步到所有硬编码 fork（包括 React Native），同时保持 www 仍由 GK 控制。该改动已在 Meta 生产环境验证，并计划推广到 Vercel 应用以进入 React 19.3，若出现问题可快速回滚。

- 🔀 反转 #35709，将 `enableParallelTransitions` 标志从 `false` 改为 `true`，默认开启该功能。
- 🚩 在 OSS/canary 默认构建及所有硬编码 fork（包括 RN fork）中启用，并保持测试渲染器同步。
- 🌐 www 版本继续由 GK（gatekeeper）驱动，`www.js` 和 `www-dynamic.js` 文件未做更改。
- ✅ 该标志已在 Meta 生产环境运行，被认为足够安全；下一步计划部署到 Vercel 应用，以争取进入 React 19.3，并可快速回滚。
- 📦 包体积变化极小（如 `react-dom-client.production.js` 增加约 0.03%），无显著影响。
- 🔗 已获得审查者批准并合并到 main 分支（提交 `eb8feb7`），247 个检查全部通过，随后多个机器人自动同步到相关分支（如 Next.js 等）。

---

### [](https://github.com/react/react/pull/35392)

**原文标题**: [[flags] Add `enableParallelTransitions` by rickhanlonii · Pull Request #35392 · react/react · GitHub](https://github.com/react/react/pull/35392)

本 PR 为 React 新增 `enableParallelTransitions` 特性标志，目的是减少过渡（Transition）通道被过度纠缠（entangle）的情况，让彼此独立的过渡可以并行提交；目前属于早期研究，先在 Meta 内部试验评估影响，最终已合并到 React 主分支。

- 🚩 新增 `enableParallelTransitions` 特性标志，并已合并进 React 主分支。
- 🔗 动机：目前 React 有时会在不必要的情况下纠缠过渡通道，导致独立的过渡被迫绑定在一起提交。
- 🧪 示例效果：两个独立的 Counter 组件在开启该标志后，可各自独立完成提交，不再互相阻塞。
- ⚠️ 并非彻底取消纠缠：同一更新队列上的过渡仍然会保持纠缠，只减少不必要的关联。
- 🔬 属于早期实验：尚未进入 experimental 频道，需在 Meta 内部验证破坏性与实际收益。
- 📦 合并前补充了相关测试，并处理了手势（Gesture）提交与回退纠缠等后续问题（如 #35486、#35487）。
- ✅ 已通过 Code Review（acdlite 批准），合并后原分支已删除。

---

### [使用TanStack Router实现可靠的查询预取](https://tkdodo.eu/blog/reliable-query-prefetching-with-tanstack-router)

**原文标题**: [Reliable Query Prefetching with TanStack Router](https://tkdodo.eu/blog/reliable-query-prefetching-with-tanstack-router)

overview summary
本文探討在 TanStack Router 中搭配 TanStack Query 進行資料預取的可靠做法，重點在於解決「路由 loader 與元件內查詢重複且容易不同步」的問題。作者先指出常見的 fetch waterfall 與雙重請求風險，再提出透過 loaderDeps、共用 queryOptions，並將 queryOptions 放入 Route Context 來徹底消除重複與不一致，確保元件與 loader 永遠使用同一份查詢設定。

- ⚠️ **問題根源**：路由 loader 與元件各自定義資料請求，兩處必須 100% 同步，但元件拆到獨立檔案後很容易漏改 loader，且缺少錯誤提示。
- 🔄 **錯誤後果**：當元件新增參數（如 `asOf`）而 loader 未同步，會先預取舊資料，再觸發一次新查詢，造成不必要的等待與 waterfall。
- 🧩 **初步修正**：使用 `loaderDeps`，明確宣告哪些 query params 會影響 loader 的資料載入，讓 loader 能感知 `asOf` 等欄位。
- 🎯 **根本解決**：將 `queryOptions` 放進 Route Context，透過新的 `context` 函式建立共用查詢選項，loader 與元件都從 context 取得同一份選項。
- 📦 **Context 優勢**：元件不再直接依賴 params 或 deps，只訂閱 `useRouteContext`；避免 drift，也容易發現未使用的預取。
- 🧬 **繼承特性**：Root route 可預取全域資料（例如用戶資訊），子路由與元件也能透過 context 繼承使用同一批 queryOptions。
- ⚡ **效能細節**：context 函式只在 params 或 loaderDeps 改變時執行，因此無關的 search 參數變更不會造成不必要的 re-render。
- ✅ **總結**：此模式是確保元件消費的資料與 loader 預取一致的最佳、可擴展做法，能有效避免重複請求與不同步問題。

---

### [](https://nextjs.org/blog/building-app-like-experiences-with-nextjs-16-3)

**原文标题**: [Building App-like Experiences with Next.js 16.3 | Next.js](https://nextjs.org/blog/building-app-like-experiences-with-nextjs-16-3)

overview summary  
Next.js 16.3 推出了“即时导航”能力，结合 Cache Components 与 Partial Prefetching，让应用既保留 Server Components 的优势，又具备单页应用般的响应式体验。本文通过多个演示应用展示了这些功能如何协同工作，涵盖缓存、预取、交互、更新、离线支持、流式渲染、乐观更新、客户端数据获取及视图过渡动画等关键模式。

- ⚡ 即时导航：通过 Cache Components 提供可立即显示的 UI 外壳，Partial Prefetching 在点击前预取可见链接，让页面切换如 SPA 般快速。
- 🔄 跨导航缓存：使用 `'use cache'` 标记数据可跨页面复用，配合 `cacheLife` 控制新鲜度，`cacheTag` 便于后续失效，回访时可跳过加载状态。
- 🔗 URL 级预取：对需要解析参数或搜索参数的链接添加 `prefetch={true}`，可在点击前获取完整 URL 对应的内容，让详情页或产品页直接就绪。
- 🖱️ 客户端交互：用 `'use client'` 将交互组件隔离，通过 Context Provider 在共享布局中保持状态同步，其余部分仍由服务端渲染。
- 🏷️ 变更后重新验证：在 Server Action 中调用 `updateTag` 使相关缓存标签过期，结合 Partial Prefetching 可让新内容在导航前提前到位。
- 📡 连接中断处理：实验性离线重试功能让失败的软导航、RSC 请求或 Action 保持挂起并在重连后自动恢复，同时 `useOffline` 可显示重连提示。
- 🎢 Suspense 流式渲染：通过嵌套 Suspense 边界控制内容揭示顺序，避免布局跳动，同时保持各区域的并行加载。
- ⚡ 乐观更新：在 `useTransition` 中使用 `useOptimistic` 立即反映用户操作，失败时回滚到确认值，并显示错误提示。
- 🧩 复杂应用组合：服务端组件负责鉴权与数据，客户端 Provider 管理交互状态，结合 `useActionState` 与 `useOptimistic` 处理连续变更。
- 📥 客户端数据获取：使用 SWR 或 TanStack Query 完成按需请求、轮询、去重与聚焦重验证，并通过预加载 + Hydration 避免客户端瀑布流。
- ✨ View Transitions 动画：支持流式内容的淡入（Suspense reveals）、列表变化的位置移动（Morphs）以及前进/后退的页面滑动过渡。
- 🧪 演示应用与社区：提供 Next Beats、Drop、Flow、Huddle 四个开源示例，包含 Playwright 端到端测试，可通过 GitHub Discussions、Issues 和 Discord 参与反馈。

---

### [使用React Native和GPT-Realtime构建3D AI助手 - Margelo](https://margelo.com/blog/building-a-3d-ai-avatar-in-react-native)

**原文标题**: [Building a 3D AI assistant using React Native and GPT-Realtime - Margelo](https://margelo.com/blog/building-a-3d-ai-avatar-in-react-native)

本文介绍了如何用 React Native 与 OpenAI 的 gpt-realtime 构建一个名为 AvatarAssist 的 3D AI 助手——一只能够实时对话、做出口型同步并通过工具调用在真实日历中安排事件的 3D 松鼠。文章涵盖了 Filament 渲染、动画与相机控制、实时语音流、嘴部骨骼驱动、日历工具调用、启动优化，以及端侧与云端模型的实际性能对比。

- 🐿️ 项目目标：构建类似 Talking Tom 的 3D 松鼠助手 AvatarAssist，支持实时语音对话和日程安排。
- 🎨 3D 渲染：使用 react-native-filament 加载 .glb 模型，通过 FilamentView、useModel 和 ModelRenderer 在 React Native 中渲染。
- 🔄 动画控制：在 UI 线程的渲染回调中按帧选择 idle/wave 动画，通过 shared value 触发，无需 React 重渲染。
- 📷 相机系统：使用 35mm 镜头投影，支持拖动旋转和重力感应倾斜视角，背景会随手机姿态轻微晃动。
- 🌲 场景背景：森林背景是循环视频，使用 react-native-video 播放，并用 ffmpeg 交叉淡化实现无缝循环。
- 🌑 假阴影：由于场景没有地面，用一张 PNG 椭圆作为模型脚下的阴影，并跟随模型整体移动。
- 🗣️ 语音方案：跳过传统 TTS，直接通过 WebSocket 连接 gpt-realtime，模型自行输出音频，首个词延迟约 574ms。
- 🔊 音频播放：使用 react-native-audio-api 以 24kHz PCM 播放流式音频，通过 promise chain 保证音频块顺序不乱。
- 👄 口型同步：用 RMS 音量驱动下颌、耳朵和眉毛骨骼，加入噪声门限与不对称攻击/释放平滑，让嘴型更像真实说话。
- 📅 工具调用：声明 add_calendar_event 工具，模型生成工具调用后通过原生 EventKit 写入日历，再让模型继续回应。
- ⏰ 时间处理：在指令中注入当前本地时间和 ISO 8601 示例，避免模型将“明天 9 点”误解为 UTC 时间。
- 🚀 启动优化：用 gltf-transform 删除不需要的动画减小模型体积；使用原生 patch 的 BootSplash.HideOnDraw，在首帧有模型时才隐藏启动屏。
- ⚖️ 端侧 vs 云端：实测云端 gpt-realtime 首词 574ms，而最佳端侧模型为 6,130ms，端侧 CPU 占用高达 238%，工具调用错误也更多。
- 🧪 性能测试提示：不要在模拟器上基准测试端侧模型，真机比模拟器慢约 59%。
- ✨ 附加 UI：包含 iOS 26 液体玻璃按钮、SF Symbols 的 Android 回退、键盘避让动画和原生底部表单字幕。
- 📱 最终表现：在 iPhone 16 和 Galaxy S22 上均保持 60fps 流畅运行，源码已开源供开发者参考。

---

### [](https://margelo.github.io/react-native-filament/)

**原文标题**: [React Native Filament Documentation | React Native Filament Documentation](https://margelo.github.io/react-native-filament/)

React Native Filament 是一个专为 React Native 设计的 3D 图形渲染库，通过 React 组件简化 3D 内容的集成，并利用原生 GPU 加速能力，同时针对移动端进行了优化，包体增量极小。

- 📱 使用 React 组件即可轻松渲染 3D 图形，无需深入图形学细节
- ⚡️ 原生 GPU 加速渲染：iOS 上使用 Metal，Android 上使用 OpenGL/Vulkan
- 💪 专为移动端打造，原生依赖仅增加约 4MB 的应用下载体积

---

### [](https://sigh.dev/posts/making-react-testing-library-faster/)

**原文标题**: [Making React Testing Library Tests 43% Faster • sigh.dev](https://sigh.dev/posts/making-react-testing-library-faster/)

本文记录了作者在 Sentry HackWeek 期间，通过优化 jsdom 等底层库，使 React Testing Library 测试在不改动测试代码的前提下提速 43% 的过程。核心改动包括标签索引共享、选择器快速路径修复和事件路径优化，并借助 AI 工具 Codex 在真实测试中验证性能提升。

- ⚡ 核心成果：在真实 Sentry 测试文件上，三项底层改动使 jsdom 30 版本测试时间从 17.18s 降至 9.77s，比当前 jsdom 26 设置快 21%，整体提速 43%。
- 🔧 优化原则：测试代码完全不变，不把 getByRole 换成 getByTestId，也不替换 userEvent，只让底层库更快。
- 🤖 AI 辅助过程：使用 Codex 定位热点，但需避开微基准陷阱、不拆分测试文件、不改写测试或 hack React 运行时；最终通过快速 A/B 测试和上游维护者反馈反复收敛。
- 🏷️ 优化一（标签索引）：jsdom 读取 input.labels 时不再让每个控件独立扫描整棵 DOM，而是构建共享索引；读取 100 个控件的标签从 60.52ms 降到 0.67ms，约快 91 倍。
- ⚙️ 优化二（选择器快速路径）：修复 DOMSelector 中 jsdom 内部对象与 document wrapper 用 === 比较恒为 false 的问题，使 matcher 基准耗时减少 89%，getByRole('button') 基准减少 42%。
- 🖱️ 优化三（事件路径）：事件派发时避免在每个祖先节点重复搜索 event.target，并跳过无监听器的节点；事件吞吐量提升 12%–36%，对 userEvent 和 fireEvent 密集测试尤其有益。
- 🧪 适用场景：改进效果最明显的是大表单、大量使用带可访问名称的 getByRole、深层 DOM 树、频繁交互事件以及 matches() 调用多的测试。
- 📦 发布状态：标签缓存和事件路径改动已合并到 jsdom 但尚未发布，DOMSelector 快速路径修复仍处于开放状态。

---

### [](https://aurorascharff.no/posts/coordinating-optimistic-updates-in-nextjs/)

**原文标题**: [Coordinating Optimistic Updates in Next.js | Aurora Scharff](https://aurorascharff.no/posts/coordinating-optimistic-updates-in-nextjs/)

overview summary
- 🚀 本文介紹如何在 Next.js 中協調重疊的樂觀更新，結合 `useActionState` 與 `useOptimistic`，讓介面即時反應，同時依序儲存伺服器變更。
- 📚 以 Huddle 的頻道側欄為例，透過 `useActionState` 排隊儲存版面變更，並用 `useOptimistic` 即時顯示拖曳與編輯效果。
- 🔄 若儲存失敗，會顯示錯誤提示並回滾到最後一次成功的伺服器狀態，無需反向計算變更。
- 📅 Flow 的日曆事件看板把相同模式擴展到整個元件樹，用 Context Provider 共享待處理變更與儲存佇列。
- 🧩 Provider 保留「變更清單」而非事件本身，各看板透過 `useOptimisticEvents` 套用變更，確保月/週視圖同步。
- ❌ 失敗的事件寫入會顯示 toast，並讓事件返回伺服器已確認的位置。
- 📡 當資料會自動變化（如訊息輪詢）時，才需要引入 TanStack Query 或 SWR 等用戶端資料庫；單純互動變更則不需。
- ✅ 此模式讓 Server Components 繼續掌管資料，僅在用戶端加入協調互動的狀態，值得嘗試。

---

### [](https://oxc.rs/blog/2026-08-18-react-compiler-support)

**原文标题**: [React Compiler Support | The JavaScript Oxidation Compiler](https://oxc.rs/blog/2026-08-18-react-compiler-support)

Oxc 项目宣布在 Oxlint 和 Oxc Transform 中正式支持 React Compiler：Oxlint 新增 22 条由编译器验证逻辑驱动的规则，`oxc-transform-react` 提供自动记忆化，初步基准显示比 Babel 快 10 倍以上，并已集成至 Vite 插件。

- 🎉 Oxlint 集成 React Compiler 的 22 条规则，用于捕获违反 React 规则的问题（如不可变性、依赖项等）。
- 📦 新增 `oxc-transform-react` 包，在 Oxc Transform 中实现自动记忆化，初步基准比 Babel 快 10 倍以上。
- ⚡ Vite 集成已可用：`@vitejs/plugin-react` v6.1.0 支持 `compiler: true` 选项，且保持工具链中立。
- 🛠 快速开始：在 `.oxlintrc.json` 中启用 `react` 插件并将 `correctness` 设为 `error`，即可获得推荐规则。
- 📋 规则类别与上游 ESLint 预设对齐，部分规则（如 `config`、`gating`、`fbt`）暂未实现。
- 🔄 背景说明：React Compiler 由 Babel 移植到 Rust，Oxc 通过 vendor 方式直接操作自身 AST，减少转换开销。
- 🚀 性能改进：Oxc 版比原始 Rust 移植版快约 2 倍，并降低内存分配；编译约 100 ms 的文件现在仅需约 10 ms。
- ✅ 一致性：与最新实验版 `babel-plugin-react-compiler` 输出对齐，并在超过 10 万个源文件上验证。
- 🔍 诊断增强：Oxlint 显示紧凑代码帧、相关源码位置、帮助消息和文档链接，便于修复。
- 📉 二进制体积：从最初集成导致的 8.66 MiB 降至 3.97 MiB，且 React Compiler 作为可选包不增加默认体积。
- 🗺 源映射已修复，完整支持 React Compiler、TypeScript、JSX 与 React Fast Refresh 的组合场景。
- 🔮 未来工作：继续完善 TODO、修复上游 Babel 实现中的 bug，并欢迎社区报告问题与贡献。
- 🙏 致谢 React Compiler 团队（尤其 Joseph Savona）和 Lauren Tan 的帮助。

---

### [](https://waku.gg/blog/waku-v1-rc)

**原文标题**: [Waku 1.0 (RC) — Waku](https://waku.gg/blog/waku-v1-rc)

Waku 1.0 候选版正式发布，这是一个以 React 服务器组件为核心的极简 React 框架。公共 API 已固定，不稳定 API 已明确标识，团队呼吁社区提供最终反馈，以推动 v1 正式版尽快落地。

- 🚀 Waku 1.0 RC 发布，公共 API 稳定，所有不稳定 API 已显式标记，这是反馈影响 v1 的最后机会
- 🧭 引入类型安全导航：导航 API 支持按路由模式传入类型化目标，参数自动检查，重命名或遗漏参数会直接编译报错
- ⚡ 即时导航：缓存路由静态外壳，`<Link>` 可预热路由，`unstable_instant` 支持立即渲染已缓存外壳并流式加载动态内容
- 🔧 其他改进：修复重定向、404、哈希目标和版本偏差问题；请求处理更严格，增加 CSRF 来源检查和可配置请求体限制；支持外部 HTTP/HTTPS 重定向
- 💥 破坏性变更：请求上下文改为仅限请求且位于 router 中，旧的 `unstable_getContext()` 移除，改用 `unstable_getRequest()` 等新 API；中间件不再可读写 Waku 上下文，需通过 `createInterceptor` 在渲染作用域内执行代码

---

### [](https://trysound.github.io/rifm/)

**原文标题**: [Rifm — React input format and mask](https://trysound.github.io/rifm/)

Rifm 是一个 React 输入格式化与掩码库，专注于在格式化过程中精确保留光标位置；它体积极小、零依赖、开源，通过统一的 `useRifm` API 支持数字、日期、电话、文本大小写等多种输入场景。

- 🎯 光标感知：Rifm 会追踪已接受的字符，并精确恢复格式化后的光标位置。
- 🔌 输入无关：可搭配原生 input、设计系统或第三方文本组件，仅需供应 `value` 和 `onChange`。
- 🪶 轻量无依赖：压缩后约 1kb，0 依赖，MIT 开源协议。
- ⚙️ 通用 API：数字、日期、电话掩码、大小写规则等场景均使用同一套小型 API。
- 🚀 快速上手：通过 `useRifm` 配置 `value`、`onChange`、`format`、`accept` 等参数即可；示例涵盖金额、电话、日期掩码和文本强制大写。

---

### [](https://github.com/TanStack/query/pull/10658)

**原文标题**: [feat(query-core): add simplified query methods by DogPawHat · Pull Request #10658 · TanStack/query · GitHub](https://github.com/TanStack/query/pull/10658)

overview summary  
该 PR 为 TanStack Query 的 query-core 新增了简化的命令式查询方法 `query()` 与 `infiniteQuery()`，用以替代旧的 `fetchQuery`、`fetchInfiniteQuery` 等 API；新方法支持 `select`、`enabled`、`skipToken` 与静态 `staleTime` 场景，对旧方法标记弃用，并补充了大量运行时与类型推断测试，最终已合并至主分支。

- 🎯 新增 `QueryClient.query()` 与 `infiniteQuery()`，作为 `fetchQuery` / `fetchInfiniteQuery` 的简化替代方案。  
- ⚙️ 新方法支持 `select`、`enabled`、`queryFn === skipToken`，并在无法返回缓存数据时抛出明确错误。  
- 🚫 当 `enabled: false` 或 `skipToken` 且无可用缓存数据时，会拒绝执行并报错。  
- 🧪 扩展了 query-core 及 React、Solid、Svelte、Preact、Angular、Lit 等框架包的运行时与 TypeScript 类型测试。  
- 📦 为旧方法 `fetchQuery`、`prefetchQuery`、`ensureQueryData` 添加了弃用标记与迁移提示。  
- 🧹 修复了静态 `staleTime`、缓存读取、禁用查询及 `skipToken` 场景下的行为一致性问题。  
- 🔀 合并过程中经 CodeRabbit 多次审查，调整了泛型参数顺序并修复了 `infiniteQuery` 返回类型等兼容性问题。  
- 📄 文档、各框架适配器更新及 Vue 代理 QueryClient 的改动计划在后续独立 PR 中跟进。  
- ✅ PR 最终通过 9 项检查，并于 2026 年 8 月 17 日合并至 TanStack Query 主分支。

---

### [@tkdodo.eu](https://bsky.app/profile/tkdodo.eu/post/3mtoxwkypvs2n)

**原文标题**: [@tkdodo.eu on Bluesky](https://bsky.app/profile/tkdodo.eu/post/3mtoxwkypvs2n)

TanStack Query v5.102.0 发布，这是 v5 系列以来规模最大的一次更新，主要包含缺陷修复、性能优化和一项新特性。发布者特别提到此次投入了整整一周的时间进行开源开发，并附上了详细的发布说明链接。

- 🎉 正式发布 TanStack Query v5.102.0，被视为 v5 以来最重要的版本更新
- ⏳ 发布者罕见地投入一整周时间专注于开源开发，而非通常的高频小幅迭代
- 🐞 包含 27 项 Bug 修复，覆盖多个稳定性问题
- ⚡ 包含 4 项性能改进，提升运行效率
- 🔥 新增 1 项特性：统一命令式查询方法（Unified Imperative Query Methods）
- 📎 发布说明见 GitHub 链接：release-2026-08-22-1856
- 📅 发布时间为 2026 年 8 月 22 日

---

### [](https://ionic.io/blog/announcing-ionic-framework-9)

**原文标题**: [Announcing Ionic Framework 9 - Ionic Blog](https://ionic.io/blog/announcing-ionic-framework-9)

overview summary
Ionic Framework 9 正式發布，帶來多項社群期待已久的更新，包括更好的路由支援、更廣的 Angular 相容性，以及更順暢的升級工具。此次版本重點涵蓋 React Router 6、Vue Router 5、Angular 18–22 支援、zoneless 變更偵測、Stencil 輸出目標更新、Select 豐富內容、字型圖示支援，並推出自動化遷移工具。未來則朝向 Modular Ionic 架構邁進。

- 🚀 發布 Ionic Framework 9，回應社群對路由、Angular 相容性與簡易升級的需求。
- 🔀 支援 React Router 6，並重構視圖保留與清理機制，修復滑動返回等問題，為 React Router 7 做好準備。
- 🧭 支援 Vue Router 5，升級門檻低；注意 `next()` 已棄用，最低 Vue 版本為 3.5。
- 🅰️ 支援 Angular 18 至 22，並預設使用 zoneless 變更偵測；非同步回呼需明確通知 Angular（如 signal 或 `markForCheck()`）。
- ⚙️ Angular 22 預設 OnPush 元件、需 TypeScript 6.0 與較新 Node；`@ionic/angular/standalone` 改為 `@ionic/angular`，遷移工具會自動處理。
- 🧩 Stencil 輸出目標全面更新，React 與 Angular 進到 1.x，增加測試覆蓋；React 輸出目標要求 React 18 以上。
- 🎨 `ion-select-option` 支援豐富內容，可在四種 Select 介面中使用 start/end 插槽、圖片、頭像、圖示及描述文字。
- 🔤 `ion-icon` 新增字型圖示支援（如 Bootstrap Icons、Font Awesome 等），也可使用 slotted SVG；大小改用 `font-size` 控制。
- 🛠️ 推出 `npx @ionic/migrate` 遷移工具，自動處理多項破壞性變更，支援 `--dry-run` 與 `--check`，並保護 Git 工作區。
- 🔮 未來規劃 Modular Ionic（2027 Q2），將外觀與行為分離，提供更高自訂彈性；v9 先交付當前開發者所需功能。

---

### [更新到 v9 | Ionic Framework](https://ionicframework.com/docs/updating/9-0)

**原文标题**: [Updating to v9 | Ionic Framework](https://ionicframework.com/docs/updating/9-0)

本文是 Ionic 8 升级至 9 的完整指南，涵盖自动迁移工具、各前端框架（Angular、React、Vue）的版本要求与破坏性变更，以及核心组件行为调整。升级前需先确保已处于最新版 Ionic 8，并建议使用官方迁移工具自动处理安全变更。

- 🛠️ 自动迁移：先升级到 Ionic 8 最新版并提交代码，执行 `npx @ionic/migrate` 可自动修复安全变更，并列出剩余需手动处理项；支持 `--dry-run`、`--check`、`--experimental` 等选项，且单次运行后不会重复执行。
- ⚡ Angular：Ionic 9 支持 Angular 18–22（不再支持 16/17）；Angular 21+ 默认启用 zoneless，需通过信号或 `markForCheck()` 触发更新；Angular 22 默认使用 OnPush，`ng update` 可帮助迁移。
- 🔧 Angular 其他：更新 `@ionic/angular`、server 和 toolkit 包；移除 CSS 导入的 `~` 前缀；组件导入路径调整；`IonicModule` 弃用，建议改用 `provideIonicAngular()`；TypeScript 需设置 `moduleResolution: "bundler"`。
- ⚛️ React：Ionic 9 支持 React 18+ 和 React Router v6；`useIonModal`/`useIonPopover` 现在对 `componentProps` 做类型检查；路由 API 全面升级（用 `element` 替代 `component`/`render`，用 `Navigate` 替代 `Redirect`，使用 `useNavigate`/`useParams` 等），移除 `IonRedirect` 和自定义 history。
- 🟩 Vue：支持 Vue 3.5+ 和 Vue Router 5；Vue Router v5 无运行时破坏，但导航守卫中的 `next()` 已弃用，应改为返回 `false`/`true` 或路由对象；`@ionic/vue-router` 不再支持 v4。
- 🌐 核心与浏览器：浏览器支持列表更新（Chrome ≥89、Safari ≥16 等）；Capacitor 必须升级到 7+，否则 `isPlatform('capacitor')` 等会误判为 web。
- 🖼️ `ion-img` 组件弃用，改用原生 `<img>` 并添加 `loading="lazy"` 与 `decoding="async"`；同时改用标准 DOM 事件（`load`、`error`），样式直接写在 `img` 上。
- ⌨️ `ion-input` 和 `ion-searchbar` 的 `autocorrect` 属性改为布尔值（默认 `false`），`autocorrect="off"` 反而会启用自动更正；相关内部 DOM 结构已重构，需更新 CSS 选择器。
- 🎛️ 移除 `ion-picker-legacy` 及 `pickerController`、`useIonPicker` 和相关类型；改用 `ion-picker`，并放在 `ion-modal` 中呈现。
- 📱 `ion-modal` 的 `handleBehavior` 默认值改为 `"cycle"`；`ion-nav` 不再与 `ion-router` 集成，路由导航应改用 `ion-router-outlet`；`ion-router-outlet` 新增 `swipeGesture` 属性控制返回手势。
- 🔄 `ion-select` 的 `ionChange` 仅在选中值真正变化时触发；action-sheet 界面不再设置 `selected` 角色；同时调整了内部 shadow DOM 结构，`part` 名称和位置有变化。
- 📐 `ion-textarea` 内部结构重构（`.textarea-control` 等），Material Design 模式最小高度调整为 72px，若需保持原高度应使用自定义类覆盖。

---

### [](https://github.com/rjsf-team/react-jsonschema-form)

**原文标题**: [GitHub - rjsf-team/react-jsonschema-form: A React component for building Web forms from JSON Schema. · GitHub](https://github.com/rjsf-team/react-jsonschema-form)

overview summary
react-jsonschema-form 是一个基于 React 的库，能够利用 JSON Schema 以声明方式构建和定制 Web 表单。它支持多种 UI 主题、多个验证器库，并提供文档、在线演示和贡献指南。

- ⚛️ 使用 React 组件，通过 JSON Schema 声明式生成 Web 表单
- 🎨 支持多种 UI 主题：Ant Design、Bootstrap、Chakra UI、Mantine、Material UI 等
- ✅ 提供多个 API 及验证器库（如 ajv8、cfworker），便于集成和校验
- 📖 提供官方文档（Docusaurus 驱动）和在线 Playground 供试用
- 👥 拥有活跃的社区：15.9k Star、2.3k Fork，代码贡献和讨论丰富
- 📦 项目采用 monorepo 结构，包含 packages、docs、testing 等目录
- 🔒 采用 Apache-2.0 许可证，并提供行为准则、贡献指南和安全策略

---

### [](https://github.com/mui/material-ui/releases/tag/v9.4.0)

**原文标题**: [Release v9.4.0 · mui/material-ui · GitHub](https://github.com/mui/material-ui/releases/tag/v9.4.0)

MUI v9.4.0 版本于 8 月 28 日发布，由 19 位贡献者合作完成。本版带来了多项无障碍改进、新主题配置、组件修复、文档完善与测试基础设施升级。

- ♿️ 新增 `theme.focusVisible`，可在各组件中统一启用键盘聚焦环的视觉样式。
- 💡 `Tooltip` 现在支持直接配合禁用按钮触发，无需额外包装元素。
- 🔘 修复 `ButtonGroup` 在触摸设备上出现的粘性悬停边框问题。
- 🌐 完成繁体中文（Traditional Chinese）本地化翻译。
- 📑 `Pagination` 在首/末/上一页/下一页按钮禁用时会自动管理焦点。
- 📏 `MenuList` 在调整滚动条时保留自定义列表内边距。
- 🛠️ 修复 `resolveProps` 对函数型 `slotProps` 的合并逻辑，并以 `clip-path` 替换已废弃的 `clip` 属性。
- 🧩 `@mui/styled-engine-sc` 修复了通过 `styled` 扩展组件时的类型问题。
- 📖 文档改进：修复外链、为表格增加行标题与正确的屏幕阅读器行数、`Tabs` 面板可聚焦、移除隐藏轮播中的可聚焦链接等。
- 🧪 测试基础设施改进：自动化 CSS 相关的 WCAG 标准检查、改用 CSS Font Loading API、使用 Vitest 全局 `expect` 等。
- 🤝 全部贡献者有 19 位，包括 brijeshb42、petr-kratochvil、silviuaavram 等。

---

### [React Summit US – 美国最大的 React 大会](https://reactsummit.us/?utm_source=partner&utm_medium=reactstatus)

**原文标题**: [React Summit US – The Biggest React Conference in the US](https://reactsummit.us/?utm_source=partner&utm_medium=reactstatus)

美国最大规模 React 大会，采用线上线下混合形式，汇聚全球开发者分享 React、AI 与全栈工程的最新实践。大会设双轨、多场工作坊、主题演讲及社交活动，并提供多种门票方案。

- 📅 时间与地点：2026年11月17日（纽约现场）及11月20日（远程日）；现场位于新泽西州自由科学中心，拥有西半球最大天文馆。
- 🏆 大会规模：美国最大 React 会议，设 Base Camp 与 Summit 双轨道，邀请 50+ 位演讲者，预计吸引全球 10K+ 开发者，现场参与约 800 人。
- 🎟️ 门票特色：常规票 $990，组合票可同时解锁 React Summit、JSNation US 与 AI Coding Summit；另有远程票、含酒店套票及 Multipass 订阅方案。
- 🧠 核心主题：深度聚焦 AI 辅助编码、AI 工程、全栈开发与架构、技术领导力成长等热门方向。
- 🎤 重磅讲者：包括 Kent C. Dodds（《The Last Software Engineer》）、David Khourshid（XState 创始人）、Mark Erikson（Redux 维护者）等众多行业专家。
- 🛠️ 工作坊与训练：提供免费及专业工作坊，覆盖 React 架构、Next.js + Claude Code、TypeScript、Firebase 等实战内容。
- 🌟 独家体验：可在天文馆听演讲、乘渡轮欣赏曼哈顿景观，并参与美国最大 React 主题派对。
- 💻 远程参与：远端观众可观看高清直播、参与互动环节、接入技术讨论室，并获取录播回放。
- 📢 赞助与社区：大会由 GitNation 主办，并得到多家企业合作伙伴支持，公开招募赞助商与志愿者。

---

### [介绍聊天代理 | 更新日志](https://trigger.dev/changelog/chat-agent?utm_source=fnf&utm_medium=newsletter&utm_campaign=august&utm_term=react-weekly&utm_content=chat-agent-launch)

**原文标题**: [Introducing chat agent | Changelog](https://trigger.dev/changelog/chat-agent?utm_source=fnf&utm_medium=newsletter&utm_campaign=august&utm_term=react-weekly&utm_content=chat-agent-launch)

Trigger.dev 正式推出 chat.agent，用于构建持久化、无超时的 AI 聊天体验。它将每个对话绑定到一台有状态的真实 Linux 机器上，随消息启动、空闲时休眠、恢复后续跑，并内置追踪、指标与可观测性。该功能已在实际生产中大规模运行，支持 AI SDK，且完全开源。

- 💬 每个对话拥有独立的有状态机器，可跨刷新和崩溃持续流式响应，无需手动管理状态。
- 🖥️ 后端是真正的 Linux 机器，可自由安装依赖、运行 CLI、使用 ffmpeg 或 headless 浏览器，并支持从 micro 到更高规格的 CPU/内存配置。
- ⏳ 单轮任务无超时，内存与变量跨轮保留；即使机器崩溃，也会从持久化会话中恢复对话。
- ⚡ 可选 Head Start 机制：首轮 LLM 调用在自建热服务器上并行启动，显著降低首 token 延迟，同时保持持久性。
- 💤 等待免费：agent 可暂停等待人工审批，期间不消耗计算费用，回复后原地恢复。
- 📊 内置 tracing 和 AI metrics 仪表板，按模型、任务、成本、token、延迟和 finish reason 统计，并支持 TRQL 查询。
- 🔧 完全兼容 AI SDK：服务端使用 streamText，客户端使用 useChat，只需将 transport 指向 chat.agent，无需中间 API 路由。
- 🧠 支持记忆快照，不要求确定性代码；Date.now()、Math.random()、fetch 都能正常使用。
- 📜 内置 compaction 与 prompt caching，可自动摘要过长历史并降低长对话成本。
- 🔐 提示词可版本化、在仪表板中覆盖，并追踪每次生成所用的版本。
- 🤖 除浏览器外，还可通过 AgentChat 从任务/脚本/其他 agent 驱动对话，并支持 MCP server 接入 Claude Code 或 Cursor。
- 🧪 支持在单元测试中驱动真实对话进行测试，且可复用 Trigger.dev 的队列、调度、批处理和任务编排能力。
- 🆓 项目为 Apache 2.0 开源，可按运行时长付费，暂停期间不收费。

---

### [红迪网](https://www.reddit.com/r/nextjs/comments/1vrq0tp/were_the_nextjs_team_ask_us_anything/)

**原文标题**: [Reddit](https://www.reddit.com/r/nextjs/comments/1vrq0tp/were_the_nextjs_team_ask_us_anything/)

您似乎没有提供需要总结的文本内容。请将文章或段落粘贴发送给我，我会按照您的要求，用中文生成概述和带表情符号的要点列表。

---

### [](https://www.reddit.com/r/nextjs/comments/1vrq0tp/comment/p4feoa5/)

**原文标题**: [Reddit](https://www.reddit.com/r/nextjs/comments/1vrq0tp/comment/p4feoa5/)

您没有提供需要总结的文本内容，请发送文章或段落，我会按照模板为您生成中文要点总结。

---

### [红迪](https://www.reddit.com/r/nextjs/comments/1vrq0tp/comment/p4fu9st/)

**原文标题**: [Reddit](https://www.reddit.com/r/nextjs/comments/1vrq0tp/comment/p4fu9st/)

您未提供需要总结的文本内容，因此无法生成概述和要点。请补充文章内容后，我将按模板为您总结。

---

### [红迪](https://www.reddit.com/r/nextjs/comments/1vrq0tp/comment/p4f7pqj/)

**原文标题**: [Reddit](https://www.reddit.com/r/nextjs/comments/1vrq0tp/comment/p4f7pqj/)

您没有提供需要总结的文本内容。请发送文章或段落，我会按照要求用中文生成 overview summary 和带表情符号的要点列表。

---

### [](https://www.reddit.com/r/nextjs/comments/1vrq0tp/comment/p4fqlki/)

**原文标题**: [Reddit](https://www.reddit.com/r/nextjs/comments/1vrq0tp/comment/p4fqlki/)

请提供需要总结的文本内容，我将按照模板为您生成中文要点列表。由于您尚未提供文章，我无法生成概述和要点。请直接粘贴文本，我会立即处理。

---

### [红迪](https://www.reddit.com/r/nextjs/comments/1vrq0tp/comment/p4fl9ah/)

**原文标题**: [Reddit](https://www.reddit.com/r/nextjs/comments/1vrq0tp/comment/p4fl9ah/)

您尚未提供需要总结的文本内容。请发送文章或段落，我将按照模板为您生成：

概述总结（无标题）
- 📌 要点一
- 🔑 要点二
- 💡 要点三

请提供内容后，我会立即为您处理。

---

### [](https://www.reddit.com/r/IAmA/comments/3wyb3m/we_are_the_team_working_on_react_native_ask_us/)

**原文标题**: [Reddit](https://www.reddit.com/r/IAmA/comments/3wyb3m/we_are_the_team_working_on_react_native_ask_us/)

您好！您似乎没有附上需要总结的文本内容。请提供要总结的文章或文本，我会按照您的模板（overview summary + Emoji 要点列表）用中文为您整理。

---

