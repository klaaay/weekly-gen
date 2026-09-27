### [](https://github.blog/engineering/user-experience/rendering-huge-pull-requests-in-the-github-copilot-app/)

**原文标题**: [Rendering huge pull requests in the GitHub Copilot app - The GitHub Blog](https://github.blog/engineering/user-experience/rendering-huge-pull-requests-in-the-github-copilot-app/)

overview summary
- 🚀 GitHub Copilot 应用重建 PR diff 界面，让百万行变更、数百条评论的超大 PR 也能流畅打开和滚动。
- 🧩 核心难题：代码行高可预知，虚拟化容易；评论高度依赖 markdown 换行、展开区、回复框、图片加载等渲染时信息，破坏“绘制前高度已知”契约，导致滚动跳动。
- 🧱 解决方案：拆分两种几何。代码几何精确、前缀和、永不因评论重建；动态块几何按稳定键与文件/行/侧锚定，估算后测量，并记录内容指纹和宽度分桶。
- ⏱️ 测量调度：采用空闲和停止滚动后触发的批量测量，仅覆盖视口约 2400px 内；屏幕内块优先读真实高度；离屏块最多一次渲染；观察器默认只标记，不直接写高度。
- 📌 滚动锚定：按身份而非像素锚定，应用高度差后恢复用户正在看的位置；区分用户滚动与程序滚动，避免与指针或滚轮惯性对抗。
- 🔄 数据管道：结构先于内容流式到达；评论线程提前解析；语法高亮离开主线程并按需运行；缓存最近几个 diff，兼顾内存与返回速度。
- 🛠️ 调试方法：内建结构化探针和性能预算 E2E 测试；自动运行 change → measure → improve 循环；无头探针加桌面应用 autopilot 无人值守复现，用健康信号定位问题。
- ✅ 结果：百万行 diff 与 400+ 行内评论像普通 PR 一样打开、滚动；评论完整渲染不裁剪；展开区域只推动下方代码；返回时保持原位置。
- 🎯 结论：代码审查不是固定尺寸文档，而是会变形的对话；界面必须从一开始就为动态内容设计，而不是事后修补。

---

### [GitHub Copilot 应用 · GitHub](https://github.com/features/ai/github-app)

**原文标题**: [GitHub Copilot app · GitHub](https://github.com/features/ai/github-app)

GitHub Copilot 桌面应用是唯一原生构建于 GitHub 之上的代理驱动开发桌面体验，支持 macOS、Windows 和 Linux，适用于任何 Copilot 套餐或自带密钥。从 issue 到合并，一切在一个应用内完成，并提供免费至每月 100 美元的多档定价方案。

- 🖥️ GitHub Copilot 桌面应用是唯一原生构建于 GitHub 的 agent 驱动开发桌面体验，支持 macOS、Windows、Linux
- 🔑 适用于任何 Copilot 套餐，也可自带密钥（BYOK）
- 🚀 可从 issue、提示词或进行中的 PR 直接启动会话，每个会话拥有独立工作区与分支文件隔离空间
- 📥 集中式收件箱统一管理多个并行会话，工作流全程可见
- ✅ 内置验证循环：可检查差异、通过应用内浏览器预览、运行终端检查并直接合并 PR
- 🔁 自动化工作流可将技能与提示词转化为可定期运行的重复性任务
- 🎨 内置开源设计技能 Impeccable，提供 23 条设计命令（如 /critique、/typeset、/layout、/polish）
- 🧠 一次性传授设计系统上下文后，agent 可记住你的设计规范；在设置 Experimental 标签页中开启即可
- 🔧 支持通过 MCP 服务器、插件和技能扩展 agent，减少配置时间
- 🔗 每个会话原生连接代码、PR、issue 与搜索，无需手动配置即可获得深度上下文
- 💰 定价分为 Free（$0）、Pro（$10/月）、Pro+（$39/月）、Max（$100/月）
- 🆓 Free 版含每月 2,000 次补全、Copilot CLI 与桌面应用，无需信用卡，学生可免费使用
- ⭐ Pro 版含 Cloud agent、代码审查、无限代码补全、第三方 agent（Claude Code、Codex）、模型选择及每月 $15 额度
- 💎 Pro+ 版含高级模型（含 Opus）、审计日志、4 倍以上使用量及每月 $70 额度
- 🏆 Max 版含新模型优先访问、2.9 倍以上使用量及每月 $200 额度，性价比最优
- 💬 用户可通过下载应用、分享反馈、查阅文档、探索仓库与阅读更新日志参与共建

---

### [AI 代码审查 | CodeRabbit | 免费试用](https://www.coderabbit.ai/?utm_source=newsletter&utm_medium=email&utm_campaign=creator_program&utm_term=cooperpress&utm_content=ad-cooperpress-003&ref=cooperpress&dub_id=RsosTiT2E8ATLNtr)

**原文标题**: [AI Code Reviews | CodeRabbit | Try for Free.](https://www.coderabbit.ai/?utm_source=newsletter&utm_medium=email&utm_campaign=creator_program&utm_term=cooperpress&utm_content=ad-cooperpress-003&ref=cooperpress&dub_id=RsosTiT2E8ATLNtr)

CodeRabbitAI 机器人于 2 分钟前评审指出：数据更新后必须使缓存失效，否则 Redis 中会残留旧的 project key，并建议用封装函数同时完成更新与缓存清理。  
- 🤖 coderabbitai 机器人在 2 分钟前进行了代码评审  
- ⚠️ 核心问题是变更后未使缓存失效  
- 📝 数据库记录虽已更新，但 Redis 中仍保留过期的 project key  
- 🔁 建议将 `await db.project.update(input)` 替换为 `await updateProjectAndInvalidate(input)`  
- ✅ 新函数应同时完成项目更新和缓存失效，避免读取到旧数据

---

### [](https://github.com/TanStack/redact)

**原文标题**: [GitHub - TanStack/redact: An alternative logical projection of React with 100% API compliancy but simpler implementation resulting in smaller bundle size and better performance. · GitHub](https://github.com/TanStack/redact)

Redact 是 TanStack 推出的 React 兼容运行时，通过一个 Vite 插件替换 React、React DOM、服务端、调度器和 JSX 入口，同时保持应用中的 React 导入不变。它追求 React API 与日常行为兼容，但以同步渲染替代并发调度，因此包体更小、部分场景更快，也存在明确的兼容性与性能取舍。

- ⚛️ **核心定位**：Redact 是“React，但被精简”的运行时，目标是保留 React API 和常见行为，不引入新的组件模型。
- 🧩 **接入方式**：安装 `@tanstack/redact`，在 `vite.config.ts` 中使用 `redact()` 插件，客户端与 SSR 构建由插件处理。
- 🔁 **导入不变**：仍可从 `react`、`react-dom/client` 等入口导入 `useState`、`Suspense`、`createRoot`、`hydrateRoot`。
- 🧪 **版本基准**：0.1.0 对比 React 19.3.0，基准记录于 2026 年 9 月 11 日。
- 📦 **包体优势**：默认 Vite 配置下 gzip 为 23,311 字节，比 React 的 69,162 字节小 66.3%；启用原生动画后为 28,159 字节，小 59.3%。
- 🧮 **独立入口体积**：DOM 客户端默认 20,139 字节，原生动画版 24,991 字节，`nano` 预设 12,466 字节，React API 入口 2,764 字节，服务端入口 8,964 字节。
- ⚡ **浏览器性能**：稀疏状态更新快 71.9%，混合深度更新快 59.1%，键控列表反转快 30.3%，上下文穿透 memo 快 29.1%。
- 🐢 **性能取舍**：挂载/卸载慢 7.5%，reducer 批量慢 7.9%，浏览器字符串 SSR 慢 10.4%，水合慢 21.4%，被动副作用慢 27%，Suspense 重试慢 124.8%。
- 🖥️ **服务端渲染**：完全就绪可读流快 49.4%，带 hooks/context 的字符串 SSR 快 30.5%，干净文本 SSR 快 6.9%，转义文本无明显差异。
- 🖱️ **交互与内存**：2,400 行场景中，点击到提交 DOM 的中位数/p95 为 1.2/1.3ms，React 为 1.5/1.6ms；挂载后保留 JS 堆为 762.5 KiB，React 为 666.4 KiB；最终卸载后额外 DOM 节点均为 0。
- 🧱 **核心渲染兼容**：支持 JSX、hooks、context、refs、memo、lazy、portals、错误边界和现代类生命周期；旧式类生命周期为空操作。
- 📝 **DOM 与表单**：受控输入、重置默认值、事件处理、水合期间保留编辑等通过共享 React 测试。
- ⏳ **Suspense 与水合**：支持 fallback、保留主 DOM、重试、流式边界和事件回放，但没有优先级调度。
- 👻 **Activity**：隐藏时保留 DOM/状态，断开 effects、refs 和订阅；插入型 effects 保持连接；隐藏工作是同步的。
- 🔗 **Fragment refs**：提供稳定 DOM 实例，支持事件、焦点、几何、观察器、滚动及 portal/可见性跟踪。
- 🚦 **Transitions**：`useTransition`/`startTransition` 同步执行，pending 始终为 false；`useDeferredValue` 原样返回输入，无时间切片或可中断渲染。
- 🧾 **表单与乐观更新**：`useActionState` 返回初始状态、空操作 dispatch 和 false；`useOptimistic`、`useFormStatus` 无乐观覆盖，setter 为空操作，状态保持 idle。
- 🎬 **视图过渡与动画**：`ViewTransition` 保留状态，`addTransitionType` 默认不播放动画；原生快照/样式/回调为实验性可选功能。
- 🌐 **浏览器专属与资源 API**：支持 `browser()`、`onBrowserBailout`、preload/preinit/preconnect/DNS hints，以及声明式 styles/scripts 和流式样式表覆盖。
- 🧰 **SSR 与缓存**：支持 `renderToString`、`renderToStaticMarkup`、可读/可管道流；未实现完整 Fizz prerender/resume；`cache` 返回函数，`cacheSignal` 返回 null，客户端/DOM 服务端渲染不缓存。
- 🧠 **React Compiler 与 RSC**：实现并别名了 `react/compiler-runtime` memo-cache 入口；Server Components/Flight 继续使用上游 React，不由 Redact 重实现。
- 🐞 **调试**：`StrictMode`/`Profiler` 只渲染 children，不双重调用或分析；`useDebugValue` 为空操作；未实现 React DevTools 与 Fast Refresh 内部机制。
- 🚩 **功能开关**：`redact()` 使用 full 预设，默认启用所有可选功能但关闭原生动画；`nano` 预设默认关闭全部可选功能；可单独关闭 hydration、classComponents、context、suspense 等。
- 🧪 **验证情况**：`pnpm test:ci` 通过 1,569 个测试、类型检查、构建包验证器和 19 个源/产物体积预算；91 个跳过不算通过；Chrome 门禁执行 1,266 个用例，仍有 7 项声明排除。
- 🚀 **真实应用验证**：`tanstack.com` 生产构建、503 个测试、5 个本地 Worker 路由及移动端检查通过；`tannerlinsley.com` 已生产升级，10 页预渲染，8 条实时路由和浏览器交互通过。
- 📤 **发布流程**：使用 changeset 提交发布说明，合并到 main 后 Release workflow 创建/更新版本 PR，通过后测试、构建、发布到 npm `latest` 并创建 GitHub release。
- 🔐 **发布安全**：使用 npm trusted publishing，无需存储 npm token，也不需要本地发布或手动改版本。
- 🛠️ **开发命令**：`pnpm install`、`pnpm test:ci`、`pnpm size`、`pnpm --filter ssr-demo dev` 可用于安装、测试/检查、体积测量和 SSR 演示。

---

### [](https://tannerlinsley.com/posts/projecting-react)

**原文标题**: [Projecting React â Tanner Linsley](https://tannerlinsley.com/posts/projecting-react)

Tanner Linsley 为 TanStack Start 构建了一个名为 @tanstack/redact 的 React 投影（projection），将 React 客户端运行时从约 60KB gzip 缩减至 7-9KB，并已在其个人网站和 tanstack.com 上实际运行。

- 🎯 **核心动机**：React 作为 TanStack Start 中无法移除的最小依赖却体积最大（客户端约 60KB gzip），而其余 TanStack 工具链加起来都远小于此，这种不平衡促使作者寻找替代方案
- 🔄 **Preact 尝试失败**：preact/compat 与 React 19 已严重脱节，在 use() 语义、Server Actions、portals、错误边界和 hydration 边界上不断需要补丁，最终放弃
- 💡 **“代码即物化视图”理念**：受 Kyle Mathews 启发，作者认为代码只是思想的一种投影；当重新生成代码的成本大幅降低时，思想成为基础表，代码成为可选投影之一
- 🧩 **技术架构**：最小核心（约 7.08KB gzip）包含 fiber 协调器、标准 hook 集合、JSX 运行时等；之上有八个可切换功能（portal、context、suspense、memo、forwardRef、lazy、classComponents、hydration），通过 Vite 插件在构建时替换以实现 tree-shaking
- 📦 **两种预设**：`full`（9.39KB，完整 React 替代，可选择移除不需要的功能）和 `nano`（7.08KB，最小核心，按需添加功能）
- ✅ **RSC 支持**：投影使用真实的 react-server-dom 进行 Flight 序列化，tanstack.com 的 RSC 博客和文档渲染器在此方案下无功能退化
- ⚡ **性能提升**：客户端导航渲染频率提升 2.24 倍，SSR 请求循环提升约 3 倍，稳定列表重渲染在真实 Chrome 中比 React 快约 18%
- 📊 **实际数据**：tannerlinsley.com 上 JS 传输量减少 33%（144KB → 96.5KB），FCP 降低 18%，LCP 降低 12%；tanstack.com 上客户端 JS 减少约 980KB
- ⚠️ **已知回归**：RSC 密集型页面的 LCP 增加 8%-43%（因 use(pendingPromise) + 延迟恢复路径），但仍符合 Core Web Vitals “良好”标准
- 🐛 **生产环境发现的 bug**：协调顺序需反向迭代、useEffect 清理时机、延迟 hydration 的 Suspense 守卫、受控输入的 nativeEvent 别名、SSR 流式输出缓冲等，均为真实 React bug 形态
- 🚫 **不进行市场推广**：作者认为营销一个“替代 React”会带来社区成本，该项目仅发布在 npm 上供自己和好奇者使用，不进入 TanStack Start，不作为任何 TanStack 包的依赖
- 🌐 **类比 Linux 发行版**：如同内核与各种发行版的关系，未来 Web 开发将更多呈现“发行版与混音”形态，人们会为自身需求量身定制依赖库的投影
- 🔮 **核心建议**：默认使用上游库通常正确，但当重新生成代码的成本下降两个数量级后，“直接使用默认”不再是自动答案；应关注自身消费者的实际形态，避免运送不再需要的通用化代码

---

### [](https://github.com/TanStack/redact#compatibility)

**原文标题**: [GitHub - TanStack/redact: An alternative logical projection of React with 100% API compliancy but simpler implementation resulting in smaller bundle size and better performance. · GitHub](https://github.com/TanStack/redact#compatibility)

概述摘要
Redact 是 TanStack 推出的一个轻量级 React 兼容运行时，采用同步渲染，通过单个 Vite 插件替代 React、DOM、服务端、调度器和 JSX 入口点，应用导入保持不变，目标是在不引入并发调度的前提下还原 React 的 API 与日常行为。

- 🎯 定位：提供 React 的 API 与常见行为，但不采用并发调度，与 React 19.3.0 对比并附有兼容性表说明有意差异
- ⚙️ 快速上手：安装 `@tanstack/redact`，在 vite.config.ts 中启用 `redact()` 插件，代码仍从 `react` 与 `react-dom/client` 导入
- 📦 体积优势：默认配置 gzip 后 23,311 字节，比 React 19.3.0 小 66.3%；启用原生动画为 28,159 字节，小 59.3%
- 🧩 独立入口：DOM client 默认 20,139 字节、nano 预设 12,466 字节，React API 入口 2,764 字节，服务端入口 8,964 字节（体积重叠不可相加）
- 🚀 浏览器性能：稀疏状态更新快 71.9%，混合深度更新快 59.1%，键控列表反转快 30.3%，深层属性更新快 22.4%
- ⚠️ 性能短板：Suspense 重试慢 124.8%（每轮约多 0.15ms），Hydration 慢 21.4%，被动副作用慢 27.0%
- 🖥️ 服务端渲染：完全就绪的可读流快 49.4%，带 hooks/context 的字符串 SSR 快 30.5%，转义文本无差异
- 💾 内存与交互：点击处理到提交中位数 1.2/1.3ms（React 为 1.5/1.6ms），挂载保留堆 762.5 KiB 略高于 React 的 666.4 KiB
- 🧱 核心能力：支持 JSX、hooks（含 use、useEffectEvent、useId、useSyncExternalStore）、context、refs、memo、lazy、portals、错误边界
- 🔒 兼容性说明：Transition 同步执行、useActionState 不运行 action、useOptimistic 为空操作、StrictMode/Profiler 不做双调用
- 🌐 特性开关：默认 full 预设，可用 `nano` 预设并按需开启 context、viewTransitions 等，禁用项会移除对应行为
- 🧪 验证情况：`pnpm test:ci` 通过 1,569 个测试、类型检查、构建包校验和 19 项体积预算；Chrome 门禁通过 1,266 个用例
- 🌍 真实应用：tanstack.com 生产构建 503 项测试通过，tannerlinsley.com 已生产升级，10 个页面预渲染全部通过
- 📤 发布流程：使用 changeset 提交发布说明，Release 工作流自动开版本 PR、测试构建并发布到 npm（可信发布，无需 token）
- 🛠️ 开发命令：`pnpm install`、`pnpm test:ci`、`pnpm size`、`pnpm --filter ssr-demo dev`

---

### [](https://azukiazusa.dev/blog/what-is-tanstack-redact/)

**原文标题**: [React 互換の軽量ランタイム TanStack Redact とは](https://azukiazusa.dev/blog/what-is-tanstack-redact/)

TanStack Redact 是一个 React 兼容的轻量级运行时，通过 Vite 插件在构建时把 `react`、`react-dom/client` 等导入替换为自身实现，保留 JSX 与 Hooks 写法，但采用同步渲染并省略并发调度，因此部分 API 行为与 React 不同，换来更小的包体积。

- 🧩 **定位**：以 React 公开 API 为起点，按 TanStack Start 所需范围实现，不同于 Preact 的 `preact/compat` 兼容层路线。
- ⚙️ **Vite 集成**：安装 `@tanstack/redact` 并添加 `redact()` 插件；使用 Vite 内置 JSX 转换时需设置 `esbuild.jsx: 'automatic'`；RSC 环境不替换导入，仍使用 React。
- 🧠 **React 设计核心**：通过纯组件与 concurrent rendering 控制渲染优先级，让输入等更新优先于重列表渲染。
- ⏱️ **Redact 的选择**：采用同步渲染，不实现 lane 优先级、`workInProgress`、`shouldYield`、中断与恢复等并发调度机制。
- 🔁 **API 差异**：`startTransition`、`useDeferredValue` 仍存在，但不提供 React 式优先级控制；`useDeferredValue` 直接返回传入值。
- 🧵 **进一步简化**：DOM 事件主要用 `addEventListener` 并补 `nativeEvent` 等兼容，不完整复现合成事件；可通过 feature flags / `nano` 预设禁用功能并在构建时剔除。
- 📦 **示例对比**：同一商品列表在 React 中 `startTransition` 可保持输入响应；在 Redact 中输入与列表更新同优先级，输入会延迟。
- 📉 **体积收益**：production build gzip 体积 React 约 69,714 bytes，Redact `full` 预设约 20,112 bytes。
- ✅ **结论**：Redact 适合需要 React 写法兼容、可接受同步渲染语义差异并追求更小包体的场景；`nano` 可进一步减小体积，但会改变部分功能行为。

---

### [](https://nextjs.org/blog/upcoming-nextjs-security-release-september-2026)

**原文标题**: [Upcoming Next.js September Security Release | Next.js](https://nextjs.org/blog/upcoming-nextjs-security-release-september-2026)

Next.js 计划于 2026 年 9 月 30 日发布安全更新，提前通知以便团队规划升级；本次将修复 9 个漏洞，并发布 16.3.7 和 15.5.27 版本及完整安全公告。

- 📅 发布日期为 2026 年 9 月 30 日，通知发布于 9 月 23 日
- 🛡️ 将修复 9 个漏洞：1 个严重、2 个高危、5 个中危、1 个低危
- 📦 计划发布 16.3.7 和 15.5.27 两个版本
- 📝 完整公告将包含影响、受影响版本和升级说明
- ⬆️ 建议在补丁发布后升级到已修复版本
- 🐛 通过 Vercel 开源漏洞赏金计划与安全研究人员合作
- 📧 相关问题可发送至 security@vercel.com

---

### [Vercel 漏洞赏金计划现已公开 - Vercel](https://vercel.com/blog/the-vercel-bug-bounty-program-is-now-publicly-available)

**原文标题**: [The Vercel Bug Bounty Program is now publicly available - Vercel](https://vercel.com/blog/the-vercel-bug-bounty-program-is-now-publicly-available)

Vercel 将私人漏洞赏金计划与开源漏洞赏金计划合并为一个公开的 Vercel bug bounty 计划，继续通过 HackerOne 运行，并已优化流程与工具以应对 AI 时代报告数量激增。
- 🧑💻 2022 年启动 HackerOne 私人 bug bounty，并与 HackerOne VIP 计划合作完善流程、目标和范围。
- 💰 曾推出 100 万美元 React2Shell 挑战、100 万美元 Vercel Sandbox 挑战和 OSS bug bounty 计划。
- 🔗 现在将私人和 OSS 赏金计划合并为统一的公开 Vercel bug bounty 计划。
- 🤖 AI 改变了漏洞赏金生态，报告数量激增且真假混杂；Vercel 仍相信公开报告能带来真实价值。
- 🛠️ 安全工程团队简化流程并构建工具，以过滤噪音、加速修复，改进分诊到验证修复的每一步。
- 🌐 覆盖 Vercel 平台所有产品及开源项目，完整范围见 HackerOne Scope 页面。
- 📬 统一计划简化提交；OSS 新发现应提交主项目，旧 OSS 提交无需转移且仍会审核。
- 🧭 研究者可通过 HackerOne 参与，提交清晰复现步骤，团队承诺快速响应和透明沟通。
- 🙌 感谢负责任报告的研究者，尤其是私人计划贡献者；他们为公开计划奠定基础，原有安排不变。
- 💼 Vercel 正在招聘安全团队，欢迎申请加入。
- ✍️ 贡献者：Eric Dodds。

---

### [发布 v9.4.0-alpha.0 · reduxjs/react-redux · GitHub](https://github.com/reduxjs/react-redux/releases/tag/v9.4.0-alpha.0)

**原文标题**: [Release v9.4.0-alpha.0 · reduxjs/react-redux · GitHub](https://github.com/reduxjs/react-redux/releases/tag/v9.4.0-alpha.0)

React-Redux 发布 v9.4.0-alpha.0 预发布版，新增可选 `useSignalSelector` 与 `SignalProvider`，通过路径追踪和信号机制只重跑依赖实际变化的 selector，面向大型应用性能优化；这是早期 alpha，邀请社区试用反馈。

- 🚀 新增 opt-in `useSignalSelector` hook 和 `SignalProvider` 组件，仅重跑状态依赖实际变化的 selector。
- 📦 新增 `react-redux/signals` 入口，可将 `Provider`/`useSelector` 整体别名替换，也支持按组件逐步采用。
- 🧩 `SignalProvider` 可替代 `Provider`，`useSignalSelector` 与 `useSelector` 签名/选项一致，并通过现有测试；`connect`、`useDispatch`、`useStore`、Reselect/weakMapMemoize、SSR 等保持兼容。
- ⚙️ 内部基于 `alien-signals` 传播算法，使用路径键控信号图和两层依赖跟踪，信号按需创建，内存随挂载组件而非状态树增长。
- 📈 基准测试对 9.3.0：16 个场景中 13 个总脚本时间改善，`dispatch()` 内耗时降低 49–88%，多数渲染次数相近或更优。
- 🧪 示例：`derived-selectors` 脚本时间 -87%、dispatch 时间 -70%、平均 dispatch 1.47→0.44ms、渲染 347→30。
- ⚠️ 成本：被追踪 selector 求值约慢 3–4 倍，每次 dispatch 增加状态树 diff，小应用挂载略慢，单组件读数千顶层键时脚本 +36%。
- 📦 包体积：opt-in 后约增加 22.7kB min / 7.2kB min+gzip（总计 32.9kB / 10.9kB），包含 `alien-signals`；标准 `Provider`/`useSelector` 用户不受影响且可 tree-shake。
- 🚫 约束：状态必须是普通不可变对象/数组；`Map`/`Set`/`Date`/类实例仅按引用跟踪；selector 不可变异状态，开发模式会抛 `TypeError`。
- 🪄 selector 接收代理，返回对象自动解包；`useSignalSelector(state => state)` 永不更新；数组迭代只追踪一层深。
- 📚 文档重构：Hooks API 拆分为 `useSelector`、`useDispatch`、`useStore` 等独立页，并新增 `SignalProvider`、`useSignalSelector`、`unwrap` 页面。
- 💬 可通过 `npm/yarn/pnpm add react-redux@alpha` 安装试用；官方希望获得性能、selector 行为边缘情况和 bundle size 反馈。

---

### [](https://shopify.engineering/helix)

**原文标题**: [Helix: The internal tool powering our Shopify app's native migration (2026) - Shopify](https://shopify.engineering/helix)

Shopify 开发了内部工具 Helix，用 LLM 将移动应用从 React Native 迁移到原生 Swift/Kotlin。它不追求一次性生成完美代码，而是通过小型检查点与严格质量门，让每次尝试在行为、视觉和代码质量都被证明前无法前进，从而实现可靠收敛。  

- 📱 Shopify 正把移动应用迁回原生 Swift/Kotlin；Shop 已在 12 周内完成，Shopify App 有 300+ 屏幕。  
- 🧰 Helix 为 LLM 提供工具、技能和护栏，并要求遵循一套高度明确、文档化的原生架构。  
- 🔁 它不指望首次输出正确，而是把迁移拆成有序检查点，逐步学习并自动化更多任务。  
- 🧭 流程：工程师指定屏幕，Helix 读取 React Native 代码并提出检查点序列，工程师几分钟内审核批准。  
- ✅ 每个检查点必须通过行为测试、与参考应用视觉对比、两轮对抗代码审查，并获得工程师批准后才能提交。  
- 🧠 每次审查反馈都会被记住，使后续检查点更自主，迁移越往后越少人工监督。  
- 🪜 检查点刻意小且递增：先屏幕骨架，再小区域，后续逐步扩大；小上下文让“参考代码本身就是规格”。  
- 🧪 子代理从参考代码生成用户视角集成测试，覆盖边缘案例，定义什么才算“已证明”。  
- ⚙️ 门 1 行为：CLI 暴露与 App 相同状态和动作，通过行为测试验证，无需模拟器，迭代更快。  
- 🖼️ 门 2 UI：GPT 编排器在相同状态截图，Gemini 充当完美主义设计审查者，列出差异、严重性和位置；可修复差异默认阻塞。  
- 🛡️ 门 3 对抗审查：两个上下文隔离的 reviewer 按文档架构检查代码，所有发现必须修复，直到双方批准。  
- 👩‍💻 门 4 工程师闭环：工程师查看代码和运行应用，反馈既让代理修复并重跑门，也存入记忆改进后续。  
- 🤖 可选自主模式：可连续完成多个检查点或跳过批准，整夜运行；质量门不放松，多屏幕可并行迁移。  
- 📦 自主运行后交付一系列已提交检查点及证据，如归档 UI 审查、通过测试和审查者结论，而非一个巨大 diff。  
- 🧩 方法不限于迁移：新功能、架构迁移和重构都可使用；纯逻辑变更可跳过 UI 门。  
- 🎯 核心经验：停止优化完美首次尝试，转向可靠收敛；允许尝试出错，但未证明不能发布。

---

### [](https://shopify.engineering/back-to-native)

**原文标题**: [Native is now the future of mobile at Shopify (2026) - Shopify](https://shopify.engineering/back-to-native)

概述总结  
Shopify 宣布将移动端技术栈从 React Native 转向原生 Swift 与 Kotlin。核心原因是 LLM/编码智能体大幅降低了双平台实现、测试、审查和一致性维护成本，使原生开发重新具备优势。迁移将采用 greenfield 重建，Shop 已上线，Shopify 主应用等将随后迁移，并配套 Helix 与 CLI 工具确保质量、防止 AI 生成不可维护代码。

- 📱 Shopify 决定把移动应用从 React Native 迁回原生 Swift 和 Kotlin。
- 🕰️ 2020 年全面押注 React Native 曾很成功：一次构建、跨栈贡献、减少功能对齐成本。
- 🤖 2025 年后 LLM/编码智能体显著进步，改变了“同一功能要构建两次”的核心假设。
- 🔁 智能体可用 iOS 版本作参考实现 Android，反之亦然，并通过共享规格、测试和审查降低双平台维护成本。
- 🧭 原生优势仍在：更贴近平台能力、第一方工具，减少框架和依赖层。
- 📦 开源库安排：React Native Skia 赞助至 2026 年底并由 William Candillon 分叉更名；FlashList 继续修关键兼容问题并寻找长期维护方；Restyle 2026 年底后归档。
- 🚀 迁移策略选择 greenfield 重建而非渐进式 brownfield，因 AI 辅助可更快、无历史约束地重写。
- 🛍️ Shop 应用首个完成迁移：AI 辅助下 12 周从 PoC 到发布原生版；Shopify 主应用（300+ 屏幕）也在迁移，今年晚些发布。
- 🧪 Helix 系统逐步重建：按检查点推进，需测试、视觉比对、两名对抗性代码审查和人工批准，避免生成不可维护的“AI slop”。
- ⚡ 为解决模拟器反馈慢，架构将业务逻辑与 UI 解耦，支持桌面无头运行，并通过 CLI 让智能体毫秒级检查状态、导航和操作；需要时远程驱动模拟器做 E2E。
- 🎯 目标：用 AI 迁移所有移动应用，但不降低性能、稳定性、无障碍和产品质量标准；以产品速度、应用质量和智能体自主完成度衡量成功。
- 🙏 文章致谢 Meta、William Candillon、Software Mansion、Shopify 工程师和 React Native 社区。

---

### [Props 不是设计系统](https://vitonsky.net/blog/2026/09/18/design-system/)

**原文标题**: [Props Are Not a Design System](https://vitonsky.net/blog/2026/09/18/design-system/)

概述：文章批评把样式作为 props、内联样式或大量 Tailwind 类在调用处传入的做法，认为这会导致视觉不一致、缺乏语义且难以维护；正确做法是把样式定义为可复用的命名单元——变体（variants）与修饰符（modifiers），并借此自然形成设计系统。

- 🎯 大多数 UI 套件允许传入任意样式（radius、size、color、Tailwind 类），看似灵活，实则让每次组件调用都变成一次性样式决策。
- 🧱 无论是 style 属性、style props 还是工具类，本质都是“内联”：在调用点决定样式，而非命名一次并复用。
- ⚠️ 内联带来根本问题：难以保证视觉一致性、代码没有语义、没有系统支撑、维护困难且易错。
- 🏷️ 解决方案是用 variant（变体）：以语义名称完整描述组件的视觉细节，包括几何、颜色、排版，不依赖外部样式补充。
- 🔧 需要变化时用 modifier（修饰符），如 size="xl"；修饰符是组件 API 的一部分，不是绕过变体的逃生口。
- 🧩 若经常同时使用多个修饰符，说明应将其组合提升为新的 variant，如 fancy-primary。
- 🛠️ 该原则跨技术栈通用：BEM/CSS、CSS Modules/Mantine、Chakra UI theme 都可用 variants + modifiers 实现。
- 📦 坚持这一纪律会自然形成设计系统：代码从零散样式决策变成可观察、可维护、可扩展的系统。
- 📚 文末还推荐了关于 BEM、UI 套件模块化、TypeScript 价值、接口意义与 UX 细节的延伸阅读。

---

### [](https://tannerlinsley.com/posts/ai-open-source-and-the-long-road-to-tanstack-charts)

**原文标题**: [AI, Open Source, and the Long Road to TanStack Charts â Tanner Linsley](https://tannerlinsley.com/posts/ai-open-source-and-the-long-road-to-tanstack-charts)

Tanner Linsley 在 2026 年 9 月 24 日的一次 Twitter Space 中，回顾了自己从 Chart.js、react-charts 到用 AI 构建 TanStack Charts 的历程，并讨论 AI 对编程身份、开源维护、代码审查和 TanStack 未来路线的影响。核心观点是：AI 让他更享受把想法变成产品，但开源库仍承载人类多年经验，判断力和人工审查依然关键。

- 🏃 作者跑步时开 Twitter Space，约 71 分钟；因音频问题一度听不到别人，Kevin 帮忙救场，文章是编辑回顾，附完整录音与时间戳转录。
- 🤖 他曾把身份与写代码速度绑定，对 AI 感到不安；但现在更享受把想法快速变成可用产品，不必手动实现每个细节。
- ⚠️ AI 也让低质量 issue/PR 更容易产生；问题不在工具本身，而在使用者的判断力，像“50 英尺光剑”能做事也能搞出大乱子。
- 📊 图表兴趣始于 Nozzle 的营销/SEO 数据探索；他用过 D3，参与 Chart.js 维护，并与 Everett 一起工作，还做了 Chart.js 2.0 的动画/补间。
- ⚛️ React 的声明式思路促使他构建 react-charts：React 负责渲染，D3 负责计算/布局，追求“给数据就出图”的自动体验。
- 🧩 “自动”背后隐藏大量细节：边距、标签、旋转文本、几何与布局决策；后来他想要组合图表类型、不同数据和布局的更大自由。
- 📚 他研究 D3 源码、Grammar of Graphics 和其他图表库；Observable Plot 对他影响很大，用了约三年并积累了许多包装层。
- 🚀 用 AI 构建 TanStack Charts 时，他已有多年 API、数据模型、渲染和痛点经验；几小时做出首个版本，不到一周得到实验性 alpha，且未手写代码。
- 🏗️ Charts 架构包括 scene graph 和响应式；类型安全必须从一开始考虑。后续投入文档、API 参考、迁移指南、测试和优化。
- 🧪 早期迁移反馈积极：更灵活、更小 bundle、更快；让 agent 讲解架构时，他认出 react-charts 中的旧模式与后来经验结合。
- 💸 他承认 token/资金影响产出，但旧流程也有成本；react-charts 花了一年多，他愿花钱换回实现时间，专注 API 与用户体验，而不是整夜处理图表几何。
- 🧠 他不会因此用 AI 重写所有 TanStack 库；Router、Start、Table、Form 的类型等仍复杂。Charts 恰好适合 AI，也归功于 D3、Grammar of Graphics、Observable Plot、Chart.js、Everett、Nick 等前人工作。
- 🔑 开源库承载多年教训，不应让每个 agent 从零重学 SVG 和数学；在 Codex 项目中，他知道该指向 TanStack DB 处理缓存/实时、TanStack Virtual 处理虚拟化，识别问题与选对库仍关键。
- 🎮 问答涉及 Three.js、Hotkeys、代码审查和自动化：Three.js 是基础工具，TanStack explore 页有小游戏；Kevin 谈 Pacer/Hotkeys，并提醒 agent 可能给 Hotkeys 包多余代码。
- 🔍 代码审查依项目而定：开源库仍以人工审查为主，安全敏感区域额外审查，发布/CI 严格控制；tanstack.com 可更快更松，但数据库迁移等需谨慎。
- 🤝 他仍深度参与流程，愿意让 agent 持续检查网站、发现问题并帮助修复，但不希望自动化系统决定下一步做什么而自己只批准范围。
- ✅ Charts 重度依赖测试、集成/浏览器测试和 bundle 预算；他批准功能、描述 API，要求 agent 实现且不破坏行为/不增大 bundle，并解释为何需要更多代码。
- 📅 TanStack 正推进生态稳定，包括计划中的 Start 1.0 发布，但未公布日期；其他库也在迈向下一阶段。
- 🎯 结尾：他仍能决定做什么、深入思考怎么工作，并看到想法对他人有用；这是他不想放弃的软件开发部分，现在能做更多。

---

### [](https://github.com/seek-oss/playroom)

**原文标题**: [GitHub - seek-oss/playroom: Design with JSX, powered by your own component library. · GitHub](https://github.com/seek-oss/playroom)

Playroom 是 seek-oss 开源的设计环境，基于 JSX 与自有组件库，让开发者在真实代码中同时面向多主题、多屏幕尺寸进行设计、原型和验证，并可构建为独立 bundle 随设计系统文档部署。

- 🧩 核心用途：创建零安装、面向代码的设计环境，支持快速 mock-up、交互原型，并评估设计系统灵活性。
- 🔗 分享与迭代：可复制 URL 分享作品，并在最终媒介中持续迭代设计。
- 🖼️ 演示案例：Braid、Cubes、Mesh、Mística、Shopify Polaris、Agriculture 等设计系统。
- ⚙️ 快速开始：安装 `playroom` 为开发依赖，添加 `playroom:start` / `playroom:build` 脚本，并创建 `playroom.config.js`。
- 🛠️ 主要配置：支持 `components`、`outputPath`、`themes`、`widths`、`snippets`、`frameComponent`、`scope`、`port`、`openBrowser`、`iframeSandbox` 等；默认端口 9000、自动打开浏览器，iframe 至少需 `allow-scripts`。
- 🧱 组件与片段：`components` 需导出对象或命名导出；`snippets` 可预定义代码片段，支持可选的 `group` 和 `description`。
- 🪄 自定义扩展：`frameComponent` 可包裹主题或 Provider，并接收 `theme`、`themeName`、`frameSettings`、`children`；`scope` 通过 `useScope` Hook 暴露额外变量。
- 🎨 主题与样式：`themes` 支持多主题同时渲染；`style jsx` 中的 CSS 会借助 Prettier 格式化。
- 🧪 帧设置：`frameSettings` 提供每帧独立的布尔开关，仅存内存、刷新重置、不持久化，也不进入分享 URL。
- 🧾 TypeScript 与 ESM：检测 `tsconfig.json` 后用 `react-docgen-typescript` 增强自动补全，可配置 `typeScriptFiles` 和 `reactDocgenTypescriptConfig`；支持 `.js`、`.mjs`、`.cjs` 配置。
- 📚 集成与支持：可配合 `storybook-addon-playroom`，面向最新稳定版主流浏览器；采用 MIT 许可。
- 👩‍💻 贡献方式：使用 `pnpm start` 开发，`pnpm test` 跑单元测试，`cypress` / `cypress:dev` 跑端到端测试。
- 📈 仓库状态：约 4.6k stars、187 forks、326 commits、26 issues、11 pull requests。

---

### [方块 • 游戏室](https://cubes.trampoline.cx/)

**原文标题**: [Cubes • Playroom](https://cubes.trampoline.cx/)

未检测到需要总结的正文内容，因此暂时无法生成文章摘要。
- 📭 你提供的“以下内容”为空，没有可提取的关键信息。
- 📝 请把需要总结的文章或文本粘贴过来。
- ✅ 收到内容后，我会用中文给出概述，并用“-”加 emoji 列出要点。

---

### [](https://www.pdfcn.dev/)

**原文标题**: [pdfcn - Beautiful PDFs, made simple](https://www.pdfcn.dev/)

这是一个面向 React 的 PDF 生成与主题构建方案，主打美观、简单、可定制；它基于 Takumi 和 Forme，通过 shadcn 分发，并提供模板、组件、预览与 CLI 安装流程。

- 🎨 新增主题构建器，让 PDF 制作更美观、更简单。
- ⚛️ 为 React 提供即用且可定制的 PDF 组件。
- 🧱 底层基于 Takumi 与 Forme，并通过 shadcn 分发。
- 📦 支持 bun、npm、pnpm、yarn 等包管理器。
- 🚀 可通过 `pnpm dlx shadcn add @pdfcn/forme/alert` 添加组件。
- 🧭 提供 Get Started、Browse Components，以及为 agent 复制提示词。
- 📄 可选择基础模板：Documents 下的 Corporate invoice、Financial report、Minimal invoice。
- 🔍 界面支持 Preview / Code 切换，并展示所用组件数量。
- 🧩 示例 `corporate-invoice.tsx` 使用 Takumi 和 Forme。
- 🏗️ 包含 6 个组件：Page header、Key-value、Table、Section、Text、Page footer。
- 🏷️ Page header 是带品牌感的文档页眉，包含 logo、公司信息和文档标题。
- 💻 可通过 `pnpm dlx shadcn@latest add @pdfcn/takumi/page-header` 添加 Page header。

---

### [](https://loading.dev/)

**原文标题**: [loading.dev](https://loading.dev/)

这是一个面向 React 的轻量级加载动画库，主打让加载效果更美观，并提供丰富的加载指示器组件。

- ⚛️ 专为 React 设计，定位为轻量级、美观的加载指示器库。
- 📦 可通过 npm 安装：`npm install loading-dev`。
- ✨ 内置 27 种加载指示器：Arc、Atom、Blocks、Bouncing dots、Cascade、Circular dots、Classic、Classic v2、Clock、Comet、Dual、Eclipse、Flip、Gather、Leap、Linear dots、Loading、Morph、Orbit、Pulse、Ring、Ripple、Slide、Snake、Swirl、Trace、Wave。
- 💚 由 Jakub Krehel 和 Paul Faivret 用心制作。

---

### [](https://loading.dev/spinners/wave)

**原文标题**: [loading.dev › Wave](https://loading.dev/spinners/wave)

Wave 是 loading-dev 提供的加载动画组件，由五根上下起伏的波浪柱组成，支持尺寸、颜色、速度、播放状态和原点等配置，并可通过自定义类名扩展。

- 🌊 基础用法：从 `loading-dev` 导入 `Wave`，通过 `size` 控制尺寸，例如 `<Wave size={48} />`。
- 📏 `size`：设置像素尺寸，默认值为 20，可组合 16、24、40 等不同大小。
- 🎨 `color`：默认继承父级 `currentColor`，可接受任意有效 CSS 颜色，例如 `#f97316`。
- 🛠️ `className`：用于自定义样式或库未提供的微调，例如 `opacity-40`。
- ⏱️ `duration`：设置动画时长/速度，单位 ms；值越大越慢，越小越快。
- ⏯️ `playState`：可暂停或恢复动画，并暴露 spinner 状态，例如 `"paused"`。
- ⚖️ `origin`：控制生长原点；`center` 从中间缩放，`bottom` 保持底部固定从基线上升，默认 `center`。
- 🎛️ 演示控件包括 Small、Medium、Large、Center、Bottom、Color、Speed 900ms、Opacity 100% 和 Reset。

---

### [发布 Reanimated -](https://github.com/software-mansion/react-native-reanimated/releases/tag/4.7.0)

**原文标题**: [Release Reanimated - 4.7.0 · software-mansion/react-native-reanimated · GitHub](https://github.com/software-mansion/react-native-reanimated/releases/tag/4.7.0)

Reanimated 4.7.0 发布，默认启用新布局动画引擎，修复多项共享元素过渡问题，新增 `backgroundImage` 动画与更多 Android CSS 平台过渡支持，支持 React Native 0.86–0.88，并包含若干破坏性变更。

- 🚀 版本 4.7.0 已发布，由 pawicao 于 9 月 18 日发布，提交为 d36edbc。
- 🧩 新布局动画引擎成为默认；如遇回归可启用 `USE_LEGACY_LAYOUT_ANIMATIONS_PROXY`，但旧引擎不支持共享元素过渡，不能与 `ENABLE_SHARED_ELEMENT_TRANSITIONS` 同时启用。
- 🔗 共享元素过渡仍为实验性，需启用 `ENABLE_SHARED_ELEMENT_TRANSITIONS`；本版修复 Android 手势、颜色恢复、百分比位移、边界阻挡触摸等多项问题。
- 🎨 `useAnimatedStyle` 现支持 `backgroundImage`，可用对象或 CSS 字符串传入线性/径向渐变，并在 UI 线程处理。
- 📱 开启 `ANDROID_CSS_PLATFORM_TRANSITIONS` 后，`backgroundColor`、`borderColor`、数字 `borderRadius`、`shadowColor`（Android 9+）的 CSS 过渡改走 Android 平台路径；该标志实验且默认关闭。
- 🧪 支持 React Native 0.86–0.88，搭配 Worklets 0.13.x；以 0.88.0-rc.1 测试；不再支持 RN 0.83、0.84、0.85。
- ⚠️ 破坏性变更：新布局动画引擎默认；mutables 始终使用 Synchronizable，移除 `USE_SYNCHRONIZABLE_FOR_MUTABLES`；`AnimatedRefOnUI` 变为 Shareable 并用 `.value` 读取；`AnimatedRefOnJS` 更名为 `AnimatedRefOnRN`；未挂载 ref 的 `measure` 返回 `null` 并警告。
- 🛠️ 其他修复包括 sticky header 冻结、CSS 解析/过渡、Jest 支持、Windows JS fallback、SPM、日志自定义回调等。
- 👥 新增多名贡献者，完整变更范围为 4.6.0…4.7.0，共 16 位其他贡献者，发布获得 11 个 ❤️ 和 5 个 🚀。

---

### [发布 v14.0.0](https://github.com/gridstack/gridstack.js/releases/tag/v14.0.0)

**原文标题**: [Release v14.0.0 · gridstack/gridstack.js · GitHub](https://github.com/gridstack/gridstack.js/releases/tag/v14.0.0)

gridstack.js 发布 v14.0.0，重点是用新的 `mode` 选项取代旧 `float:boolean`，并新增 `cellHeight:'fill'`；同时集中修复拖拽、调整大小、触摸以及 React/Vue 渲染等问题。

- 🚀 版本：v14.0.0 为最新发布，提交 `3f0469d` 经 GitHub 验证签名（GPG key ID: B5690EEEBB952194）
- 📊 项目公开数据：约 9.1k Star、1.4k Fork、28 个 Issue、1 个 PR
- 🔄 重大变更：新增 `mode?: 'top' | 'float' | 'list' | 'compact'`，取代旧 `float:boolean`（#754、#2866）
- 📋 `list` 模式：项目按行优先顺序连续重排，像可排序列表；拖拽、调整大小、增删会重排其他项，拖放到另一项时会占据其位置（见 `list.html` 演示）
- 📏 新增 `cellHeight:'fill'`：让行均分容器高度，填满固定尺寸网格（#2583、#787；见 `cell-height.html` 演示）
- 🧲 侧边栏拖入项现在会触发 `dragstart`/`drag`/`dragstop` 事件（#2627、#2761）
- 🛡️ 修复：在 change 事件中调用 `update()` 导致崩溃的问题（#3012、#3179）
- 🖱️ 修复：调整大小时不再显示其他组件的 resize 手柄（#3226）
- 🌑 修复：可在打开的 Shadow DOM 中查找拖拽手柄（#3148；见 `title_drag.html`）
- 👆 修复：组件在触摸中途销毁时释放全局触摸锁（#3188）
- 📐 修复：API `update()` 现在像拖拽一样遵循 `maxRow`（#2953）
- ⚛️ 修复：React/Vue 中渲染有组件但无 id 的拖入项（#2976）
- 🔘 修复：允许从 button/input 手柄内部的嵌套元素开始拖拽（#2703）
- 🔄 修复：React/Vue 在交互式拖拽/调整大小后重新渲染项内容（#2974）

---

### [发布 v9.8.0 · pmndrs/react-three-fiber · GitHub](https://github.com/pmndrs/react-three-fiber/releases/tag/v9.8.0)

**原文标题**: [Release v9.8.0 · pmndrs/react-three-fiber · GitHub](https://github.com/pmndrs/react-three-fiber/releases/tag/v9.8.0)

react-three-fiber v9.8.0 于 9 月 22 日发布，核心是兼容 React 19.3.0，并修复同步配置根节点、Strict Mode 画布及重挂载期间根节点被拆除等长期问题。

- 🚀 主要亮点：R3F 现已兼容 React 19.3.0，虽未完全支持所有新 API，但不再与最新 React 冲突。
- ⚙️ React roots 改为同步配置；若渲染器需要异步（如 WebGPURenderer），则再按需门控，避免不同步问题。
- 🛡️ Strict Mode 不再导致 canvas 出现问题，这与此前加入的异步支持相关。
- 🔗 修复损坏链接（#3872，@dor-rondel）。
- ⚛️ 新增 React 19.3 支持（#3916，@cades）。
- 🧹 修复 core：卸载宽限期内重新挂载的 root 不再被拆除（#3869，@abernier）。
- 🧩 core：同步配置与渲染 roots（#3925，@krispya）。
- 👏 新贡献者：@dor-rondel 和 @cades；完整变更见 v9.7.0...v9.8.0。

---

### [React 柏林 2026 会议](https://reactday.berlin/?utm_source=partner&utm_medium=reactstatus)

**原文标题**: [React Conference in Berlin 2026](https://reactday.berlin/?utm_source=partner&utm_medium=reactstatus)

overview summary  
React Day Berlin 2026 是第 7 届柏林 React 大会，主题为 “Build apps, not walls”，聚焦 AI 与 React 开发，于 2026 年 12 月 4 日和 7 日以柏林线下+线上形式举行，预计 800 人到场、5K 人远程参与，汇聚 40+ 讲者与培训师。

- 📅 日期与形式：2026 年 12 月 4 日（柏林线下+远程）与 12 月 7 日（远程日）。
- 🌍 地点：柏林 KOSMOS，Karl-Marx-Allee 131A，并同步线上直播。
- 👥 规模：800 名现场开发者、5K 名远程参与者、40+ 讲者与培训师。
- 🤖 主题重点：AI 集成、系统设计、全栈工程、可靠性、长期可维护性。
- 💻 覆盖技术：Claude Code、Next.js 16 + React Compiler、OpenAI Codex、Vercel AI SDK、Cursor、React Server Components + Server Functions、TanStack、Storybook & Playwright、shadcn/ui、MCP。
- 🗓️ 12 月 4 日：柏林线下与远程混合日，现场 9am CET 开始，远程按多时区接入。
- 🗓️ 12 月 7 日：远程日，双轨道直播，并提供跨时区讲者 Q&A。
- 🛠️ 工作坊：10+ 免费远程与 Pro 工作坊，涵盖 Modern React Architecture、MCP App、Claude Code、Next.js + Claude Code 等。
- 📚 Deep Dives：全栈开发与架构、晋升 Senior/TechLead、AI 辅助编码、AI 工程。
- 🎤 讲者亮点：Kitze、Nicola Corti、David Khourshid、Tejas Kumar、Fadila Fidina、Maurice de Beijer、Brad Westfall、Misha Kazakov、Dennis Nerush 等。
- 🎙️ 主持与委员会：Kim Ngan Le Dang、Nathaniel Okenwa、Johannes Goslar 主持；Robin Pokorny、Bogdan Plieshka、Michele Bonazza、Daniel Rios Pavia 等参与程序委员会。
- 🎟️ 票务：Hybrid 常规 €545；React Day Berlin + AI Coding Summit €645；远程早鸟 €90；远程+AI €150；Multipass €17/月，团队 €13/月。
- 📍 场地特色：KOSMOS 是 1960 年代太空时代剧院，位于 Friedrichshain 创意街区。
- 🌱 社区与包容：提供 100 个多样性奖学金，申请截止 10 月 2 日 23:59 CEST；分享徽章可赢取免费票。
- ⚠️ 其他：React Day Berlin 将跳过 2025，推荐关注 React Advanced 2025；活动由 GitNation 主办，FocusReactive 等赞助。

---

### [](https://jobs.fidelity.com/en/technology-careers/?utm_source=javascript&utm_medium=paidsocial&utm_campaign=jobssocial&utm_content=awn-tech-sl3-txt)

**原文标题**: [Technology careers at Fidelity | Fidelity Careers](https://jobs.fidelity.com/en/technology-careers/?utm_source=javascript&utm_medium=paidsocial&utm_campaign=jobssocial&utm_content=awn-tech-sl3-txt)

概述摘要
- 🚀 富达科技职业以“重塑金融未来”为使命，推动有影响力的创新，并邀请人才加入以开启职业生涯。
- 🏢 公司兼具初创企业心态与财富500强基础，持续投资创新并兑现数字化未来承诺。
- 📈 页面以数据模块强调技术人才规模、2023年员工承担新/扩展职责比例及美国专利成果。
- 🧑💻 技术工作文化强调人与人的互动；全栈工程师 Monica 称这是富达最棒的地方。
- 📌 近期技术职位包括高级网络修复分析师、高级大型机工程师（COBOL、Java、Azure/AWS）、高级系统工程师，地点为北卡罗来纳州达勒姆，现场办公，发布于9月25日。
- 🛠️ 招聘技能涵盖软件工程、全栈工程、云工程、数据可视化、AI/机器学习、架构、系统工程师和系统分析等。
- 📚 富达技术员工每周有专门学习时间，可通过在线课程、职业辅导、导师影子等方式更新技能。
- 🔍 求职者可搜索职位、加入人才网络、订阅职位提醒，并进一步了解技术职业与加密货币职业机会。

---

### [动物岛UI](https://guokaigdg.github.io/animal-island-ui/)

**原文标题**: [Animal Island UI](https://guokaigdg.github.io/animal-island-ui/)

overview summary
- ⚠️ 你尚未提供需要总结的正文内容。
- 📥 请粘贴文章或文本，我会立即提炼关键信息。
- 🧾 输出将使用“-”符号列表，并为每条搭配合适的 emoji。
- 🈶 最终摘要会使用中文，并包含概览与核心要点。

---

### [](https://github.com/github/dmca/blob/master/2026/09/2026-09-03-nintendo.md)

**原文标题**: [dmca/2026/09/2026-09-03-nintendo.md at master · github/dmca · GitHub](https://github.com/github/dmca/blob/master/2026/09/2026-09-03-nintendo.md)

该文档是 GitHub DMCA 公共仓库中公开的一份删除通知：任天堂美国公司指控仓库 `guokaigdg/animal-island-ui` 未经授权使用《动物森友会》受版权和商标保护的角色、图像及近似官方 logo 的设计，并要求删除该仓库及其全部 fork。因受影响仓库网络超过 100 个，GitHub 最终对 377 个仓库（含父仓库）执行处理。

- 📄 文件位于 GitHub `dmca` 公共仓库的 `2026/09/2026-09-03-nintendo.md`，属于公开的 DMCA 通知记录。
- ⚖️ 任天堂美国公司委托律师发送通知，指控目标仓库侵犯其《动物森友会》相关版权与商标。
- 🎮 侵权内容据称包括：仓库主页展示《动物森友会》角色、图像及模仿官方 logo 的设计；UI 组件库中包含多份未经授权的角色和图像副本。
- 🚫 通知要求 GitHub 立即移除或禁用 `https://github.com/guokaigdg/animal-island-ui/` 及其所有 fork。
- 🍴 发函时该仓库有 318 个 fork；由于受影响网络超过 100 个仓库，且发函方认为多数 fork 与父仓库侵权程度相同，GitHub 对全部 377 个仓库（含父仓库）进行了处理。
- 📧 因 GitHub 在线表单不支持同时提交版权与商标侵权投诉，发函方改用电子邮件提交。
- 🧾 法律依据包括美国《版权法》17 USC § 501 和《兰哈姆法》15 USC § 1125。
- 📎 通知附有 Exhibit A（相关美国版权登记列表）和 Exhibit B（任天堂受保护的《动物森友会》logo 设计示例）。
- ✅ 发函人声明已阅读 GitHub DMCA 指南，善意认为使用未经授权，已考虑合理使用，并愿受伪证罪处罚确认信息准确且获授权代理任天堂。
- 🛡️ GitHub 在禁用内容前联系了受影响仓库所有者，给予修改机会，并说明可提交 DMCA 反通知。

---

### [动物岛用户界面](https://guokaigdg.github.io/animal-island-ui/#/skill)

**原文标题**: [Animal Island UI](https://guokaigdg.github.io/animal-island-ui/#/skill)

目前没有收到需要总结的正文内容，因此无法生成文章摘要。
- 📭 “Use the following content:”之后为空，未检测到可总结文本。
- 📝 请粘贴文章或提供原文，我会提炼核心信息。
- 📌 摘要将包含开头概览与带 emoji 的“-”要点列表。
- 🌐 我会用中文回复并保持简洁。

---

