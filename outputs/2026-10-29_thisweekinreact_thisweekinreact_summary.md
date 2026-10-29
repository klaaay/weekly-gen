### [CodeRabbit 分诊 | 确定拉取请求优先级](https://www.coderabbit.ai/triage?utm_source=newsletter&utm_medium=email&utm_campaign=creator_program&utm_term=twir&utm_content=ad-twir-007&ref=twir&dub_id=4CHCTLcHmppXyJDf)

**原文标题**: [CodeRabbit Triage | Prioritize pull requests](https://www.coderabbit.ai/triage?utm_source=newsletter&utm_medium=email&utm_campaign=creator_program&utm_term=twir&utm_content=ad-twir-007&ref=twir&dub_id=4CHCTLcHmppXyJDf)

overview summary
本文介绍 CodeRabbit Triage：面对 PR 数量激增、来源多样、优先级不清和队列混乱，它通过看板视图、价值/风险/评审成本排序、重叠与过时提示、评审者建议和过滤器，把 PR 队列转化为优先级列表，帮助团队先处理高价值与高风险变更。

- 📈 PR 正越来越多地由开发者、AI 代理和监控系统直接产生，规划被绕过，队列更易积压、重叠和陈旧。
- 🗂️ Triage 用 Kanban 视图展示 PR 及排序原因，并提供 Following、Requires Action、All PRs、Safe to close、Projects 等视图。
- 🎯 排序综合考虑业务价值、风险、评审工作量、近期人工活动和 PR 间关系，优先展示重要功能、关键修复和高风险变更。
- ⚠️ 通过风险信号指导评审深度，重点标记敏感系统、生产凭据、跨租户权限、外部攻击面等高危 PR。
- 🔁 识别重叠和过时 PR，减少无效评审，把人工注意力留给真正需要判断的工作。
- 👥 根据代码所有权、贡献和评审历史建议评审者，并可直接发起审查请求。
- 🔍 支持按仓库、作者、评审者、优先级、风险、安全风险、工作流和变更类型过滤，并保存团队关注视图。
- 🧩 与现有 CodeRabbit 评审流程兼容，为已有 PR 增加队列级上下文，而不是替代原有评审。
- ☁️ 当前公测面向 GitHub Cloud 组织并按组织启用；定制优先级、数据合规、费用和席位需联系团队确认。
- 🔐 示例队列包含大量 P0/P1 安全与修复任务，如认证凭据泄露、GitLab 运行时凭据、Azure MFA 重新认证、反向隧道探针等，建议尽早审查。
- 🚀 最终目标是把 PR 噪音转化为价值：更快交付重要变更，并让团队先处理最值得关注的 PR。

---

### [推出 TanStack Redact | TanStack 博客](https://tanstack.com/blog/introducing-tanstack-redact)

**原文标题**: [Introducing TanStack Redact | TanStack Blog](https://tanstack.com/blog/introducing-tanstack-redact)

TanStack 发布 Redact 0.2.0：它是浏览器端更小的 React/React DOM 替代实现，可在不改应用代码的情况下减少客户端 JavaScript，并已提供 TanStack Start、Vite、Vinext 和 Next.js 的稳定集成。

- 🚀 Redact 实现应用渲染与更新 UI 所需的 React API，只需加入构建配置，现有 React 导入、组件、Hooks 和依赖即可在浏览器中使用 Redact。
- 🧩 在 Vinext 和 Next.js 中，React 继续负责服务端渲染与 Server Components，框架仍管理路由、缓存和 Server Action 传输；Redact 接管水合与客户端渲染。
- ⚡ Redact 采用同步渲染，不包含 React 的时间切片或可中断渲染；Suspense 过渡、待处理表单和乐观状态已覆盖，但重渲染仍可能延迟输入。
- 📦 默认构建体积节省：TanStack Start 从 109.3 KB 降至 62.3 KB，节省 43.0%；Vite 从 68.3 KB 降至 20.1 KB，节省 70.5%；Vinext 从 138.1 KB 降至 98.8 KB，节省 28.5%；Next.js 从 175.6 KB 降至 139.9 KB，节省 20.4%。
- 🔧 关闭未使用的可选功能后，Start 可降至 59.8 KB，纯客户端 Vite 应用可降至 12.6 KB。
- 📊 Vinext 基准测试六轮结果显示，应用从 154.9 KB 降至 115.5 KB，减少 39.4 KB；生产构建时间基本不变，开发启动略快，但该测试未衡量浏览器渲染或水合速度。
- 🛠️ 0.2.0 的关键在于扩大兼容性覆盖并修复失败场景，同时保持两个运行时包在原有体积限制内。
- 💡 作者仍看好 React，也期待 Solid 和 Octane 的发展；Redact 的价值在于让现有应用以更小实现继续维护和构建。
- 🧪 官方邀请开发者用 TanStack Start、Vite、Vinext 或 Next.js 试用 0.2.0，测量实际变化并反馈兼容性问题。

---

### [我们刚刚向开源维护者捐赠了一百万美元 | Sentry 博客](https://blog.sentry.io/another-year-another-1-000-000-to-open-source-maintainers/)

**原文标题**: [We just gave a million dollars to Open Source maintainers | Sentry Blog](https://blog.sentry.io/another-year-another-1-000-000-to-open-source-maintainers/)

Sentry 宣布今年向开源维护者捐赠 100 万美元，预算从 75 万美元提升至 100 万美元，并通过 Open Source Pledge、thanks.dev、ecosyste.ms Funds、开源基金会及 Syntax 团队赞助等方式分配，强调使用开源的公司应回馈维护者，尤其在 AI 时代开源基础设施需求持续增长的背景下。

- 💰 Sentry 将开源回馈预算从 75 万美元增加到 100 万美元，认为使用开源软件的公司应支持其建设者和维护者。
- 🤝 Open Source Pledge 迎来两周年，目前 37 家成员公司已向开源维护者和基金会累计支付 8,421,535 美元。
- 🤖 AI/LLM 栈同样依赖开源；Sentry 继续支持 NumFOCUS，该非营利组织资助当今 AI 开发所使用的科学计算开源工具。
- 📈 Python Software Foundation 曾表示其 AWS 支出同比增长约 69%，反映 AI 应用、包安装和 CI 运行对开源基础设施带来更高需求。
- 🧾 Sentry 向 thanks.dev 支付 49.5 万美元，用于向数百名其依赖包的维护者分配赞助，并提供持续更新的接收者表格。
- 📦 Sentry 通过 ecosyste.ms Funds 向 Python、Django、Ruby、Rust、JS 和 Go 生态中的全球关键包捐赠 10 万美元。
- 🔍 Sentry 与 Software Stewardship Lab 合作，识别并资助传统依赖分析容易遗漏的“幻影依赖”维护者。
- 🏛️ 基金会赞助包括：Python Software Foundation 6 万美元、PHP Foundation 4.5 万美元、Ruby Central 4 万美元、Django Software Foundation 4 万美元、Packagist 3.5 万美元、Open Source Initiative 3 万美元、Rust Foundation 1.5 万美元、Geomys 1.5 万美元、OpenJS Foundation 1 万美元、NumFOCUS 1 万美元、Alpine Linux 5,000 美元。
- 🎙️ Syntax 团队另用 10 万美元赞助项目和维护者，包括 FFmpeg、Jellyfin、OBS、pnpm、biomejs、Caddy、TanStack、Three.js 维护者等。
- 🙌 文章最后感谢所有开源维护者，并呼吁更多公司加入 Open Source Pledge、使用 thanks.dev 等方式回馈开源生态。

---

### [即将发布的 Next](https://nextjs.org/blog/upcoming-nextjs-security-release-november-2026)

**原文标题**: [Upcoming Next.js November Security Release | Next.js](https://nextjs.org/blog/upcoming-nextjs-security-release-november-2026)

Next.js 计划于 2026 年 11 月 3 日（周二）发布安全更新，提前通知团队安排升级；此次将修复 7 个中危漏洞，并同步公布完整安全公告与升级指引。

- 🗓️ 安全版本计划于 2026 年 11 月 3 日发布。
- 🛡️ 将修复 Next.js 中的 7 个中危漏洞。
- 📄 发布时将同步提供完整安全公告，包含影响、受影响版本和升级说明。
- ⬆️ 建议在补丁版本发布后尽快升级。
- 🤝 通过 Vercel 开源漏洞赏金计划与安全研究人员合作，保障 Next.js 等开源框架安全。
- 📧 有关安全计划或漏洞管理的问题，可联系 security@vercel.com。

---

### [](https://building.owner.com/project-speed)

**原文标题**: [Project Speed Â· Building @Owner](https://building.owner.com/project-speed)

Owner 通过“Project Speed”重构面向本地餐厅的建站基础设施，以提升网站速度、转化率和销售额；核心是用 Astro 技术栈 Apollo 替换 Next.js 技术栈 Mercury，在边缘缓存页面，仅在需要交互的区域使用 React。上线后，菜单页 p75 LCP 从 5.4 秒降至 0.7 秒，单店月收入提升 4% 以上，并节省基础设施成本。

- 🚀 背景：大型连锁餐厅投入巨资打造高速、高转化网站，本地餐厅难以竞争；Owner 已服务 1 万多家餐厅网站，有足够流量测试优化并推广成功方案。
- 🐢 旧栈 Mercury 慢：页面渲染需往返后端 Olympus，缓存层层叠加但每次部署都会清空；还加载过多位置和菜单数据，并受 Google Tag Manager、Facebook Pixel 等第三方脚本拖累。
- ⚡ 新栈 Apollo 选择 Astro：默认输出纯标记，客户端 JS 按需加载；支持 islands、预渲染与按需页面混合，并深度集成 Cloudflare。
- 🏝️ 架构：页面在服务器渲染为 HTML 并缓存，菜单、购物车等交互部分作为 React islands 水合；营销页几乎不需要客户端 JS。
- 🌐 边缘与缓存：运行在 Cloudflare Workers 边缘网络；请求经网关 Worker、Workers Cache、R2 HTML 存储，缓存未命中再回退 Astro 渲染；采用 stale-while-revalidate 和后台刷新。
- 📨 数据更新：Olympus 数据变化时主动调用 Apollo 的重新验证接口，后台重渲染受影响页面，而不是轮询；响应头标记来源和耗时，便于追踪。
- 🛠️ 优化细节：内联 CSS 和小于 150KB 的资源、启用链接预取、在边缘完成品牌域名查找（省约 50ms）、Pluto 在边缘处理图片、启用 HTTP 103 Early Hints。
- ⚠️ 挑战：功能开关组合会放大缓存变体，因此按用户分桶做实验；缓存键包含品牌和功能开关哈希；登录相关页面不走共享缓存；还修复了服务端 React 重复副本问题。
- 🧪 发布：Apollo 与 Mercury 以 50/50 实验并行，用 PostHog 衡量，并用 Sphinx 浏览器扩展强制切换；按 8、800、4800、全量分阶段上线，保留 kill switch；2026 年 1 月 26 日 Apollo 承载 100% 流量，2 月 9 日公开发布。
- 📈 结果：菜单页 p75 LCP 5.4s→0.7s（约快 87%）；首页到菜单点击率 +23%；单店收入 +4%；基础设施每月省 8000–10000 美元；移动 Lighthouse 44→99，桌面 98→100；购物车转化约 +10%，El Vaquero +33%。
- 🔮 后续：Apollo 成为默认建站方式，Restaurant Grader 等前端也按类似方式重建；Owner 希望帮助本地商家成功，AI 正加速平台改进。

---

### [设计系统应默认快速 | Den Odell](https://denodell.com/blog/design-systems-should-be-fast-by-default)

**原文标题**: [
      Design Systems Should Be Fast by Default | Den Odell
    ](https://denodell.com/blog/design-systems-should-be-fast-by-default)

文章主张设计系统应像重视可访问性一样重视性能，因为组件一旦变慢，所有使用它的应用都会被拖累；作者实测了10个主流开源设计系统在“249项国家下拉框”和“一次性选中100个复选框”场景下的表现，通过性能剖析定位慢因，并提出修复建议、性能预算测试和“默认快”的工程实践。

- 🎯 设计系统是应用的基础层；浏览器主线程负责执行 JavaScript、响应事件和绘制屏幕，底层组件越省时，留给应用的空间越多。
- ♿ 性能应与可访问性并列成为设计系统团队的优先事项；组件应在接近真实的大量数据下测试，并防止性能随版本悄悄退化。
- 📊 作者测试了10个设计系统，覆盖 React、Lit、FAST、Stencil 和 SAP 自研框架，使用生产构建、Chrome v155、M1 Pro、CPU 4倍限速，并取三次测试中位数。
- 🧪 只有 Spectrum Web Components 有明显自动组件性能测试；Fluent 有基准但未见自动运行；Ant Design、Material UI、Fluent 只检查包体积，无法反映交互响应速度。
- ⏱️ 打开含249个国家的下拉框：Fluent 61ms、Carbon 63ms 最快；Material UI 208ms、React Spectrum 227ms、Ionic 1266ms 最慢。
- ☑️ 一次选中100个复选框：Fluent 29ms、Carbon 41ms 最快；Mantine 227ms、React Spectrum 298ms、Ant Design 421ms 最慢；整体 UI 阻塞时间相对较短。
- 🧩 框架不是决定性因素：同为 Lit 的 Carbon、Web Awesome、Spectrum Web Components 差异明显；Ionic 下拉框最慢，但复选框并非最慢。
- 🐌 Ionic 慢因：`ion-radio-group` 不使用 shadow DOM，Stencil 的 `experimentalSlotFixes` / `appendChildSlotFix` 在添加每个选项时多次遍历已有选项，导致越加越慢；建议改用 shadow DOM 或优化 Stencil 只检查变化的 slot。
- 🖥️ Material UI 国家下拉框一次性渲染约250个元素；Ant Design 只渲染可见项并随滚动补充，即虚拟化，因此更快；虚拟化需兼顾键盘导航和屏幕阅读器。
- 🎨 UI5 下拉框打开时要一次性为隐藏 popover 中约1500个元素计算样式；React Spectrum 虽使用虚拟化但仍慢，因 React Aria 逐个 `checkVisibility` 并读写布局，造成 layout thrashing；建议批量读取和写入。
- ✅ Ant Design 复选框慢主要因100个动画同时计算样式和绘制；关闭动画后耗时降至不到三分之一；建议仅在直接选择时动画，或用 opacity 合成层动画。
- 🧪 建议用 Playwright 写性能测试：测量主线程 `TaskDuration`、Long Animation Frames 和最长无响应时间，并设置性能预算，例如总耗时低于300ms、长帧低于100ms。
- 📈 更稳健的测试是比较250项与125项下拉框的耗时比；若全量耗时远超半量两倍则失败，可发现“每加一项越来越慢”的问题，Ionic 在此失败。
- 🚀 将快行为设为默认：列表超预算自动虚拟化、复选框仅在直接选择时动画；文档标明组件测试过的数据量上限。
- 🔍 用真实页面上的 DevTools 性能剖析决定优化优先级；发布说明给出优化前后指标，让应用团队感知收益。
- 📚 文章配套 GitHub 仓库和 GitHub Actions 工作流；作者新书《Fast by Default》进一步讲解性能预算与每次 PR 检查。

---

### [](https://sarthakmishra.com/blog/optimizing-tanstack-start)

**原文标题**: [Optimizing the sh*t out of TanStack Start - Sarthak](https://sarthakmishra.com/blog/optimizing-tanstack-start)

本文记录作者将个人站点迁移到 TanStack Start 后，通过审计生产构建、减少不必要下载、优化字体、图片与 JavaScript/CSS，将移动端主页 Lighthouse 性能从 73 提升到 100，并讨论哪些优化真正有效、哪些收益难以归因，以及如何用预算和浏览器测试防止性能回退。

- 📉 优化前移动主页性能为 73，LCP 5.2 秒；优化后达到 100，LCP 1.7 秒，FCP 1.2 秒，TBT 0 毫秒，CLS 0.001，Speed Index 1.2 秒。
- 🔍 应先审计生产构建并多次运行取中位数，确认 LCP 元素后再修改；开发模式包含访客不会收到的额外工作。
- 🧱 检查首屏 HTML 响应：作者主页文档约 110 毫秒返回且已包含正文，延迟主要来自周边资源，应使用服务端 loader 或预渲染而不是客户端 Effect。
- 📦 最大收益来自“不加载”：每页曾加载含 117 张图片元数据的全站图片清单，约 35 KiB 压缩；改为按路由收集所需图片数据。
- 🪟 对话框和关闭功能应懒加载：搜索、移动菜单、图片放大等在首次打开时才下载，主页初始 gzip JavaScript 从 196.1 KiB 降至 174.4 KiB。
- 🔤 字体需两层优化：使用 WOFF2 子集并移除未用样式/轴，减少 preload；再用匹配度量的 fallback 字体避免布局偏移，作者曾测得 CLS 约 0.21。
- 🖼️ LCP 图片应在初始 HTML 中可发现、eager、高优先级，并设置正确 `sizes`；CSS 隐藏的图片仍会下载，隐藏导航图和视频海报应延迟加载。
- ⏳ 非关键 JavaScript 可延后到页面加载后、空闲时或首次交互；但延后不等于减少，仍需清理空闲动画和不必要循环。
- 🧪 Critical CSS 与延迟 hydration 可减少阻塞 CSS，但最终分数收益无法确认，且维护成本高，可能引入暗色模式、字体变量、表单选择器和滚动恢复问题。
- 🤖 作者用 Claude Code 与 Codex 分工发现图片清单、字体、CSS、Early Hints 和回滚问题，但最终保留哪些优化仍由作者判断。
- 📏 应建立性能预算和浏览器测试：限制阻塞 CSS、总 CSS、初始 JS、module preloads 和共享内容索引大小，并测试水合前内容、字体稳定、隐藏资源、焦点返回和早期滚动。
- 🚧 主页之外仍有优化空间：两篇图片较多的文章分别得分 89 和 88，LCP 均为 3.5 秒，下一步应优化这些页面的 LCP 图片。

---

### [修复 React 中的水合不匹配错误和 UI 闪烁问题](https://www.gmoniava.com/blog/hydration-mismatch-errors-and-how-to-fix-them)

**原文标题**: [Fixing a Hydration Mismatch Error and UI Flicker in React](https://www.gmoniava.com/blog/hydration-mismatch-errors-and-how-to-fix-them)

overview summary
本文解析 React/Next.js 服务端渲染中的水合不匹配错误，并结合侧边栏状态、主题切换和移动端遮罩案例，说明如何通过内联脚本在水合前同步本地状态、让 React 初始渲染与服务端/更新后的 DOM 一致，从而同时避免报错和 UI 闪烁，并比较相关替代方案。

- ⚛️ 水合是客户端接管服务端预渲染 HTML 并使其可交互的过程；客户端组件会先发送 HTML，之后下载并执行 JavaScript。
- 🧩 React 水合主要分两步：在内存中重新渲染并比对服务端 HTML，然后为 HTML 绑定事件监听器等交互能力。
- ⚠️ 当服务端输出的 HTML 与客户端首次渲染结果不一致时，就会发生水合不匹配错误，常见原因是依赖仅客户端可用的信息，如 localStorage。
- 🚫 常见修复是组件挂载前返回 `null`，用 `useEffect` 在客户端设置 `isClient`；可避免不匹配，但会让该组件及其子组件退出 SSR，不利于 SEO 或大范围布局内容。
- 🩹 `suppressHydrationWarning` 只能压制警告，不能修复底层差异，且仅作用一层，应作为逃生舱谨慎使用。
- 📦 案例中侧边栏开关存于 localStorage；在 `useState` 初始化函数中读取会导致 SSR 与首次客户端渲染不一致，也存在初始化函数纯度问题。
- 🔄 改用 `useEffect` 读取 localStorage 可避免水合错误，但会造成侧边栏从关闭到打开的短暂闪烁。
- 🧠 最终方案是在水合前运行内联脚本：读取 localStorage、直接切换侧边栏相关 class，并把状态存到 `window._INITIAL_SIDEBAR_STATE_`，供 React 初始状态读取并保持首次渲染一致。
- 🎨 主题切换使用 `useIsClient()`/`next-themes`，挂载前不渲染小组件是可接受取舍；`next-themes` 注入脚本可能引发不匹配，因此在 `<html>` 上用 `suppressHydrationWarning`。
- 📱 移动端遮罩始终存在于 HTML，通过 `group` 与 `hidden group-[.left-0]:block` 等 CSS 类跟随侧边栏的 `left-0` 状态显示，避免条件渲染导致水合不匹配。
- 🆕 React 19.3 的 `use(browser())` 可跳过客户端组件的服务端渲染并保留最近的 `<Suspense>` fallback；它是替代方案，但用在布局中同样会让布局及子内容不被 SSR。

---

### [](https://formisch.dev/blog/ai-writes-forms-hand-it-a-library/)

**原文标题**: [AI Writes Forms Pretty Well; Here's Why We'd Still Hand It a Library | Formisch](https://formisch.dev/blog/ai-writes-forms-hand-it-a-library/)

概述总结：AI 已经能高质量地生成表单代码，但文章认为仍应让 AI 基于表单库开发，因为表单库已经解决了异步校验竞态、状态同步、可访问性、类型安全和维护一致性等大量隐性难题，能让 AI 少重复造轮子，把精力放在业务逻辑上。

- 🧠 AI 很擅长写表单：能理解需求、覆盖常见场景、主动处理无障碍属性，并实现防重复提交、去除空格和网络错误处理。
- ⚠️ 但 AI 生成代码仍会漏掉异步竞态：用户名检查结果可能覆盖新输入，提交时可能发送点击瞬间的旧值，且提交后不会自动聚焦到第一个错误字段。
- 🐛 这类问题并非个例：Formisch 曾修复校验竞态、重置后旧结果回写等 bug；React Hook Form、React Final Form 等表单库也遇到过类似问题。
- 🧩 使用表单库后，同样的表单无需手写 latestCheck 计数器或焦点逻辑：库会丢弃过期校验结果、在输入已变化时取消旧提交，并自动聚焦首个错误字段。
- 🔄 表单库减少手动状态同步：isSubmitting、isValidating、isDirty、errors 等状态由库维护，开发者只需读取，不必维护五到七份本地状态。
- 📐 表单库提供统一模式：登录页、设置页等都能复用 useForm、Form、Field 等模式，团队和 AI 更容易读写一致代码。
- 🛡️ TypeScript 能从 schema 推断字段路径：像 emial 这样的拼写错误会被类型检查发现，AI 也能据此自动修复。
- 🎯 对用户更友好：支持配置 blur 时校验、input 时重新校验，并在提交出错时聚焦第一个错误字段。
- 📦 Formisch 以 headless、模块化、signals 为基础：保留完整标记控制权，按需引入方法，字段级重渲染，包体约 2.5 kB，并支持 FieldArray 稳定 ID。
- 🚀 结论是：AI 不依赖表单库也能写表单，但交给它一个成熟表单库，能让它从已被验证的基础设施出发，减少维护成本，更专注于应用特有逻辑。

---

### [TanStack AI 1.0：依然是你的 AI，依然按你的方式来 | TanStack 博客](https://tanstack.com/blog/tanstack-ai-1-0)

**原文标题**: [TanStack AI 1.0: Still Your AI, Still Your Way | TanStack Blog](https://tanstack.com/blog/tanstack-ai-1-0)

TanStack AI 正式发布 1.0：核心 API 稳定并可用于生产，延续“无锁定”承诺，同时推出实验性的 Agent Harness。自 alpha 以来，它已成长为覆盖聊天、工具、媒体、MCP、持久化、沙箱与代理的工具箱，拥有 23 个提供商适配器、广泛 UI 框架支持和 140+ 贡献者。

- 🚀 **1.0 定位**：核心 API 稳定、适合生产，且没有引入新概念；0.x 中弃用的 API 已移除，替代方案此前已发布。
- 🔄 **升级要求**：所有稳定的 `@tanstack/ai*` 包需一起升级到 1.0；实验性 harness 包仍保持 0.x。
- 📈 **成长数据**：提供商适配器从 4 个增至 23 个，另含 `openaiCompatible`；UI 覆盖 React、Vue、Solid、Svelte、Preact、Angular、Octane、Remix 与原生 JS；沙箱提供商达 11 个。
- 🧩 **RC 后新增**：子代理、`decide()`、Agent Skills、上下文压缩、计算机使用、统一 `reasoning`、自动提示缓存、重试、自带密钥与 OAuth 登录、MCP 服务端/WebMCP 等。
- 🛠️ **测试与开发**：新增无头聊天 UI 工厂、`fakeText()` 无网络测试、编码助手 Agent Skills，以及更多适配器、框架和沙箱支持。
- 📚 **文档重写**：所有手写文档针对 1.0 重写，页面以问题和可运行设置开头，高级细节后置，适配器页面统一结构。
- ⬆️ **迁移要点**：运行 codemod；`body` 改为 `forwardedProps`，`conversationId` 改为 `threadId`；`threadId` 在浏览器和服务端均必填；移除 `ai-react-ui`、`ai-solid-ui`、`ai-vue-ui`；工具审批改用 `interrupts.resolveInterrupt()`；流结束使用 `RUN_FINISHED` 而非 `data: [DONE]`。
- 🤖 **Agent Harness**：新增 `@tanstack/ai-harness`，支持持久会话、重启后可恢复的等待、类型化代理、插件、多用户访问规则与后台工作。
- 🧑‍💻 **构建编码代理**：通过文件工具、权限、快照、待办、压缩、用量和项目指令等插件，配合 `runCli` 快速搭建终端编码代理。
- 🌐 **多端运行**：同一 harness 可运行于终端、脚本/CI、Web 应用（`useChat` + `createHarnessHandler`）、编辑器 ACP，以及 Claude Code/Cursor 的 MCP。
- 🧪 **实验性说明**：harness 及相关入口仍为 0.x/实验性 API，可能在次版本中变化，与稳定的 1.0 核心分离。
- 🙌 **社区与伙伴**：3 名维护者、143 位贡献者；OpenRouter 等合作伙伴持续支持。
- 🔭 **下一步**：打磨核心体验、帮助团队交付各类 AI 功能，并推动 harness 稳定、增加提供商与沙箱、跟进模型实验室更新。

---

### [更新日志 | Motion](https://motion.dev/changelog)

**原文标题**: [Changelog | Motion](https://motion.dev/changelog)

Motion 生态发布说明汇总了 Motion、Motion UI、AI Kit 和 Motion Studio 共 968 个版本，近期更新重点集中在动画性能与包体积优化、布局/拖拽/重排动画修复、Gallery 2D/3D 交互增强，以及 Studio 动效工具和 AI 辅助能力。

- 📦 发布范围覆盖 Motion、Motion UI、AI Kit、Motion Studio，并提供按补丁、次版本、主版本筛选及 RSS。
- 🧩 Motion 14.6.0 新增 Reorder 键盘抓取移动排序、processFrame 手动处理帧循环、stepFrames 同步推进测试时间，并修复 layoutId 跳变、拖拽动画和树摇优化等问题。
- 🎯 Motion 14.5.0 引入 scopeMotion/useScopeMotion，用于限定动画和手势作用域、设置默认过渡、匹配媒体查询及简化清理。
- 🖱️ Motion 14.4.0 将 drag 拖拽手势加入 JavaScript API；14.2.0 支持 x、y、scaleX 等硬件加速独立变换。
- 🎞️ Motion 14.3.0 增强 stagger 的 grid、edges、random 选项，支持 scaleZ，并修复 matrix3d、useSpring 和 SVG MotionValue 相关问题。
- 🖼️ Motion UI 4.1.0 优化 Gallery：切换 grid 时从中心淡入、详情条支持 stagger from、关闭时按波浪式收拢，并修复分页和布局切换的飞行动画问题。
- 🚀 Motion UI 4.0.0 是主版本更新，加入列表与详情视图的 2D/3D Gallery 动画，要求 motion@^14.1.0，改进树摇，并将 animateLayout 移至 motion。
- 🧪 Motion 14.0.0 移除部分内部 API 以改善跨版本兼容；13.5.0 支持负 bounce 的过阻尼弹簧，并显著缩小 useSpring 和 m 组件体积。
- ⚡ 多个版本持续优化性能：scroll/useScroll 更小更快、更多 offset 硬件加速、spring 重定向提速、animate 启动与逐帧开销降低。
- 🛠️ Motion Studio 2.0.0 首次发布；2.1.0 增加 Ultramotion 免费额度及撤销/重做；2.2.0 增加减少动态效果模式。
- 🤖 AI Kit 提供 Performance Doctor，可按 S-F 评估源码动画性能并给出修复建议；Motion+ 还包含 Carousel、Ticker、Cursor、AnimateNumber、splitText、510+ 示例、110+ 教程及私有 Discord。

---

### [useScopeMotion | React 中的作用域动画与手势 | Motion for React](https://motion.dev/docs/react-use-scope-motion)

**原文标题**: [useScopeMotion | Scoped animations and gestures in React | Motion for React](https://motion.dev/docs/react-use-scope-motion)

useScopeMotion 是 Motion for React 的 Hook，用于把 animate、inView、hover、drag 等 JavaScript 动画、手势和滚动监听限定在组件 ref 元素和/或媒体查询范围内，并在组件卸载时自动清理。

- 🎯 通过 ref 创建作用域，选择器只在 ref 元素内解析，例如 `"li"` 仅选中该列表中的 `li`。
- 📦 从 `"motion/react"` 导入 `useScopeMotion` 及 `animate`、`inView`、`drag` 等函数。
- ⚙️ 接收 ref 与 setup 函数；setup 在组件挂载后、浏览器绘制前运行。
- 🧹 作用域自动收集 `animate`、`scroll`、`inView`、`hover`、`press`、`drag`、`resize`、`delay` 及其回调中启动的动画。
- 🗑️ 组件卸载时取消作用域：停止动画、移除手势/滚动/视口监听，并恢复被 animate 或拖拽元素的 `style`。
- ↩️ setup 可返回自定义清理函数，用于作用域未收集的工作，如 `window` 事件监听。
- 🔁 默认只运行一次；通过 `deps` 在依赖变化时取消当前作用域并重新运行 setup。
- 🧩 `ref`、`transition`、`matchMedia` 仅在作用域创建时读取；若 ref 元素延迟挂载，需添加相应依赖。
- 🖱️ 返回当前 scope 的 ref，可在事件处理器中用 `scope.current?.run` 或 `bind` 启动受作用域管理的动画。
- 🎛️ 选项包括 `deps`、`transition`（作用域内 animate 默认过渡）和 `matchMedia`（按媒体查询运行 setup）。

---

### [Vinext 1.4：减少服务器工作量、加快水合、更轻量的预取 | Vinext 博客](https://vinext.dev/blog/vinext-1-4)

**原文标题**: [Vinext 1.4: less server work, faster hydration, and lighter prefetching | Vinext blog](https://vinext.dev/blog/vinext-1-4)

Vinext 1.4 是一次以性能为核心的更新：在 Hacker News 基准应用上，服务端 CPU 比 1.3 下降 43% 并略优于 Next.js，浏览器脚本时间下降 26%，Lighthouse 移动端得分从 81 升到 88；同时预取体积大幅缩减、HTML 与 RSC 缓存改为同步填充与再生成，并附带一批正确性与开发体验修复。

- 🚀 **升级方式**：执行 `npm install vinext@1.4.0 @vinext/cloudflare@1.3.0 @cloudflare/workers-response-store@1.1.4`；若 Response Store 以独立 Worker（默认 service-binding 模式）运行，也需一并部署，因为本次修复了重叠刷新的处理问题，`vinext init` 创建的项目自带 `deploy:response-store` 脚本。
- 📉 **服务端性能**：Hacker News 故事页（约 1500 条评论、每请求渲染）单请求 CPU 从 54.4ms 降至 31.1ms，略低于 Next.js 的 33.7ms；吞吐提升 40%（22.9/s vs 21.3/s），中位响应时间下降 28%，峰值内存下降 10%。
- 🧵 **减少管道开销**：流式响应不再被 SSR 入口、页面生命周期、tracing、缓存和 `after()` 层层包裹各自的 `TransformStream`，改为直接读取并合并；RSC 流同样处理，并移除了对每个字节重写 React 样式表提示的逻辑（React 19.3 已正确发送）。
- 🧩 **Node 渲染优化**：在 Node 上用 React 的 Node 构建而非 edge 构建渲染 HTML，内嵌 RSC payload 保持 UTF-8 字节而非反复解码转义编码；`<Link>` 在 SSR 期间跳过十余个无意义的 hook。
- 🐛 **内存泄漏修复**：社区发现 Node 服务器会把每个 App Router route handler 请求留在内存中，50 万次请求后堆增长到 1.18GB，现在稳定在约 10MB。
- 📐 **布局每请求只跑一次**：原先预跑一遍布局以捕获 `redirect()`/`notFound()` 并区分静态/动态，导致静态布局每请求执行两次；现在由渲染本身处理 `redirect/notFound/forbidden/unauthorized`，重布局应用客户端导航 CPU 指令降 14%、整页加载降 8%，且客户端可跳过已有布局（仅限不缓存的响应）。
- ⚡ **水合更快**：启动所需 chunk 携带 V8 显式编译提示，Chrome 136+ 在下载时后台线程编译，650 个客户端组件的页面水合从 104ms 降到 87ms；启动脚本改为低优先级加载，App Router 浏览器入口不再为每个客户端组件保留 loader，入口文件名也更稳定、利于跨部署缓存。
- 📊 **浏览器指标**：脚本时间 193ms→143ms（Next.js 150ms），主线程工作 706ms→609ms，LCP 712ms→628ms，客户端导航脚本时间 182.4ms→146.5ms；Lighthouse FCP 3.31s→2.11s，TBT 110ms→56ms，得分 88。
- 🪶 **预取更轻**：不再为视口内每个链接完整渲染动态页面，只预取路由及其 loading 状态；大型内容站原型打开一页的预取量从 3.9MB 降到 10.7kB（约 364 倍更少），与 Next.js 行为对齐。
- 🗂️ **HTML 与 RSC 缓存同步**：两者仍分开存储，但现在一起填充与再生成——RSC 未命中时直接用已有 payload 渲染 HTML，不再重跑服务端组件；Workers Cache 无法存无人请求的响应，故后台补取，代价是每次未命中/刷新多一个请求。
- 🌐 **跨主机共享缓存**：Workers Response Store 与 Workers Cache 的键不再包含 host，同一应用在多个域名下共用一份缓存（与 KV 缓存一致）；读取 host 的渲染属于动态、不会被缓存，Pages Router 的 `getServerSideProps`/`getInitialProps` 仍需 `CDN-Cache-Control` 显式选择加入。
- 🏗️ **大型内容站基准**：FCP 2.54s→1.67s、Lighthouse 84、脚本时间 191ms、JS 下载 382kB（比 Next.js 少 39%）、峰值内存不到 Next.js 一半；但仍落后 Next.js 的 1.21s 首绘与低约 27% 的 CPU，原因包括 15 个小样式表（Vite 每 chunk 一文件）拖慢首绘，以及在 workerd 上仍用 edge 构建、RSC payload 更大（297kB vs 204kB）。
- 🧪 **TanStack Redact 实验**：构建期用更小运行时替换 React DOM，JS 下载减少 25%，首页脚本 51ms→14ms；但 1500 条评论页水合几乎翻倍（143ms→264ms），TBT 56ms→666ms，Lighthouse 从 88 掉到 70，原因是生产环境仍逐元素做 prop 与 HTML 属性比对。
- 🔧 **其他修复**：`vinext start`/`deploy`/`typegen` 及自定义服务器正确设置 `NODE_ENV=production`（此前 `vinext start` 跑的是开发版 React）；`next/dynamic` chunk 加载失败会进入最近的 `error.tsx` 而非永久"Loading..."；`revalidateTag(tag, profile)` 支持 stale 直到 profile 过期；布局 `notFound()` 返回 404 而非 500；GTM/GA4 能记录每次客户端导航；生产服务器会记录渲染错误；新增 `--vite-config` 与 `--ignore-wrangler-config` 选项。
- 🙌 **致谢**：感谢 @exKAZUu、@gengjiawen、@Godsenal、@Gourav224、@hakarrr、@williamrogersdev 等贡献者，以及 1.3.1 贡献者和众多 bug 报告者；完整变更见 vinext 1.4.0、@vinext/cloudflare 1.3.0、@cloudflare/workers-response-store 1.1.4 的发布说明。

---

### [](https://tanstack.com/blog/tanstack-db-1.0-rc1-going-all-in-on-oracles)

**原文标题**: [TanStack DB 1.0 RC1: Going All In on Oracles | TanStack Blog](https://tanstack.com/blog/tanstack-db-1.0-rc1-going-all-in-on-oracles)

TanStack DB 1.0 RC1 已发布，标志这个响应式客户端数据框架经过约一年半开发后进入稳定、生产可用阶段；文章重点讲述团队如何借助“oracles”和编码代理大规模硬化核心、发现边界 Bug，并加速软件成熟。

- 🚀 **发布定位**：TanStack DB 1.0 RC1 API 稳定、生产就绪；升级现有应用需参考迁移指南，处理包更新与破坏性变更。
- 🧩 **功能进展**：自 0.6 起加入服务端渲染、TanStack Start 深度集成、Neon Realtime 与 Convex 适配器、Preact 支持，并修复大量 Bug、提升性能、减小体积。
- 💡 **核心价值**：把后端数据变成类型化集合，组件可查询联表、过滤后的实时结果；乐观编辑即时显示并与服务器协调，且可从现有 REST/TanStack Query 增量采用。
- 📈 **采用情况**：核心包周下载超百万，过去一年约增长 10 倍；Prisma Studio、Unkey、Skylight 等团队已在使用。
- 🧪 **从单元测试到 Oracle**：用属性测试生成大量输入，再以独立模型计算期望结果；对同一变更历史比较 DB 实际输出与模型，验证完整行为规则。
- 🐞 **硬化 1.0**：Oracle 让代理持续发现新 Bug 和未定义行为；仓库增加约 42 万行测试，现有 211 个 oracle 测试文件覆盖 15 个包。
- 🤖 **为代理打造可玩环境**：Oracle 把设计决策变成可执行、可反馈的约束；代理触发失败后可读取模型、反例和设计理由，再修正实现。
- 🧭 **Oracle 设计方法**：明确单一承诺、独立计算答案、选择观察点、生成有意义序列、主动试图骗过 oracle，并在分歧时先诊断实现、模型或规则。
- 🏗️ **Cranes 与可演化性**：Oracle 被比作“起重机”，让代理在保留设计知识的前提下大胆重构；关键不是一次生成正确，而是积累可复用的验证工具。
- ⏱️ **Superhistory**：代理与 oracle 压缩经验获取时间，把原本数年的成熟过程压缩到数月；写代码更便宜，但设计判断更密集、更重要。
- 🔮 **未来方向**：DB 可为代理提供 SKILLs、可执行模型和验证工具；还在探索把普通 server functions 编译成客户端集合/action 与服务端 API 的实验性方案。
- ✅ **行动号召**：在要求较高的应用中试用 1.0 RC，并向团队反馈。

---

### [发布版本 7.91.0 · react-hook-form/react-hook-form · GitHub](https://github.com/react-hook-form/react-hook-form/releases/tag/v7.91.0)

**原文标题**: [Release Version 7.91.0 · react-hook-form/react-hook-form · GitHub](https://github.com/react-hook-form/react-hook-form/releases/tag/v7.91.0)

react-hook-form 发布 v7.91.0，重点修复 useFieldArray、验证与表单状态同步问题，并包含性能优化、测试补充、依赖升级和社区致谢。

- 🚀 发布 v7.91.0 最新版本，自上一版本以来包含 11 个提交。
- 🐞 重点修复 useFieldArray：setValue/setValues 不更新行、卸载时未正确注销、字段重索引错误、reset 后丢失验证规则、数组变化后验证结果过期、onBlur 模式提交后验证异常等。
- ✅ 修复验证与状态同步：reset/unregister 后异步验证过期、Controller 使用过期 DOM 值、isValid/isSubmitting 更新异常、空验证消息被误判为错误、延迟验证错误未在 blur 时刷新。
- 🧩 修复表单与字段行为：<Form /> 对 JSON、URL 编码、multipart、纯文本提交的处理；useWatch 默认值；select 选项丢失；useForm 保留已移除选项或禁用状态；渐进式 required；maxLength 为 0 的校验。
- 🧠 修复对象与值处理：null 原型对象、稀疏数组、constructor 键、setValue 处理 null 原型对象，以及 NaN/无效日期验证结果。
- ⚡ 性能优化：getValues() 避免不必要的复制，减少 <Form /> 的重复渲染。
- 🧹 重构与文档：简化 multipart Content-Type 处理、改进内部类型、清理 memo 组件 displayName、修复 JSDoc 示例。
- 🧪 测试与依赖：补充禁用字段数组操作及 useFieldArray/reset/验证/表单状态回归测试；升级 joi、browserslist、follow-redirects、vite 等依赖。
- ❤️ 感谢 19 位贡献者及 Pennylane 团队的特别支持。

---

### [发布 2.5.0 · bvaughn/react-window · GitHub](https://github.com/bvaughn/react-window/releases/tag/2.5.0)

**原文标题**: [Release 2.5.0 · bvaughn/react-window · GitHub](https://github.com/bvaughn/react-window/releases/tag/2.5.0)

react-window 2.5.0 已由 bvaughn 于 10 月 22 日发布，包含 12 次提交；本次更新重点新增滚动元素支持、无头虚拟化与滚动状态 Hook，并改进滚动定位及补充文档。

- 🚀 为 `List` 和 `Grid` 新增 `scrollElement` 属性，支持列表/网格随页面或指定滚动祖先元素一起滚动，并仅渲染可视区域内的行。
- 🧩 新增 `useVirtualizer` Hook，用于渲染自定义/无头虚拟化内容（如语义化 `<table>`），返回渲染项、偏移与尺寸、总尺寸、可视范围及 `scrollToIndex` 方法。
- 👀 新增 `useIsScrolling` Hook，用于跟踪列表、网格或滚动元素是否正在滚动，支持在滚动时渲染简化内容。
- 📐 `scrollToRow`、`scrollToColumn`、`scrollToCell` 及 `useVirtualizer` 的 `scrollToIndex` 会遵循被滚动元素的 CSS `scroll-padding`，类似浏览器 `scrollIntoView`。
- 📚 文档站点新增“scrolling with the page”“useVirtualizer”“useIsScrolling”和“infinite loading”页面。

---

### [发布 4.15.0 · bvaughn/react-resizable-panels · GitHub](https://github.com/bvaughn/react-resizable-panels/releases/tag/4.15.0)

**原文标题**: [Release 4.15.0 · bvaughn/react-resizable-panels · GitHub](https://github.com/bvaughn/react-resizable-panels/releases/tag/4.15.0)

本次发布为 react-resizable-panels 4.15.0，新增父级组件访问 Hook，并优化面板缩放、折叠、展开及拖拽交互行为。

- 🆕 新增 `useParentGroup`、`useParentPanel` 和 `useParentGrid` Hook，组件可直接访问最近的 `Group`、`Panel` 或 `Grid` 及其命令式 API，无需逐层传递 ref；在匹配组件外返回 `null`。
- 🧩 在 `Cell` 内，`useParentGroup` 会返回 `Grid` 外最近的 `Group`。
- ↔️ `Panel` 和 `GridTrack` 的命令式 `resize()`、`collapse()`、`expand()` 以及双击分隔条重置尺寸，现在会从被调整面板两侧最近且可吸收空间的面板中获取或分配空间。
- ⚖️ 优先选择不会折叠或展开其他面板的调整方式，避免此前可能无效果或意外影响其他面板的问题。
- 📏 `expand()` 仍会恢复面板最近尺寸；若恢复会导致其他面板折叠，则改为扩展到可容纳的最大尺寸，前提是不小于其 `minSize`。
- 🖱️ 修复在没有 `Separator` 的面板边界拖拽后释放指针时，误触发指针下方元素点击的问题。
- 🔢 本次发布包含 5 个提交，涉及 #775 和 #774。

---

### [GitHub - module-federation/tanstack：TanStack Start 的模块联邦插件 · GitHub](https://github.com/module-federation/tanstack)

**原文标题**: [GitHub - module-federation/tanstack: Module Federation plugin for Tanstack Start · GitHub](https://github.com/module-federation/tanstack)

该仓库提供 `@module-federation/tanstack`，用于在 TanStack Start 中集成 Module Federation，支持 Vite 与 Rsbuild（底层使用 Rspack），覆盖浏览器端联邦、SSR 联邦、运行时辅助工具，并提供完整示例与端到端测试。项目采用 MIT 许可证，当前约 20 stars、2 forks。

- 🧩 核心功能：为 TanStack Start 提供 Module Federation 插件，帮助主机与远程应用共享模块并协同构建。
- 📦 安装方式：安装 `@module-federation/tanstack` 与 `@tanstack/react-start`，再按打包器选择安装 Vite 或 Rsbuild 适配器；两者为可选 peer 依赖，避免无关适配器被解析。
- ⚙️ 配置顺序：联邦包装插件必须放在 `tanstackStart()` 之前，以便规范化 TanStack 的客户端与 SSR 入口。
- 🔧 Vite 适配：默认 `remoteEntry.js`、`manifest: true`、`hostInitInjectLocation: "entry"`；React/ReactDOM 为单例，声明 remotes 时对主机 eager 共享；不要设置全局 Module Federation `target`。
- 🏗️ Rsbuild 适配：通过 `/rsbuild` 导入，输出兼容 script 的浏览器产物，manifest 可被 Vite/Rsbuild 主机消费；共享 React 单例，远程默认 `publicPath: "auto"`，主机建议 `shareStrategy: "loaded-first"`。
- 🖥️ SSR 支持：Rsbuild SSR 联邦需显式开启 `server: true`，远程生成 `remoteEntry.ssr.cjs` 并在 manifest 中公布；主机可从异步 Node CommonJS 服务端构建加载远程。
- 🧰 运行时工具：`lazyRemote` 可在远程加载失败后重试；`getRemoteStylesheets` 可从远程 manifest 读取样式表并注入服务端响应的 `<head>`。
- ✅ 兼容矩阵：Vite↔Vite 浏览器与 SSR 均支持；Vite↔Rsbuild 支持浏览器联邦，SSR 需远程开启 `server: true`；Rsbuild↔Vite 的 SSR 需主机开启；Rsbuild↔Rsbuild 的 SSR 需双方开启。
- 📌 版本要求：Node 22.18+、24.11+、26+，TanStack Start 1.167.43+；Vite 适配器要求 Vite 8 与 `@module-federation/vite` 1.23.3+；仓库使用 pnpm 12。
- 🧪 示例与测试：工作区包含 6 个 TanStack Start 应用；`pnpm test` 会构建并两次运行应用，用无头 Chromium 验证 SSR 标记、样式注入、水合、交互、共享 React 上下文、控制台错误、manifest 可达性及远程离线回退恢复。

---

### [在 Next.js 中借助](https://nextjs.org/blog/ship-less-javascript-with-ai)

**原文标题**: [Ship less JavaScript in Next.js with your AI agent | Next.js](https://nextjs.org/blog/ship-less-javascript-with-ai)

Next.js 16.4 为 AI 代理提供 bundle 分析与优化能力，借助 Turbopack 的模块图定位意外的导入关系，并通过 `next-bundle-optimizer` 技能自动提出或应用优化建议；Vercel 已在 v0 和 vercel.com 上减少近 2MB 压缩 JavaScript。同时，面向开发者的 Bundle Analyzer 新增路由概览、快照对比和关键渲染路径过滤等功能。

- 🔧 Next.js 16.4 引入面向 AI 代理的 bundle 优化技能 `next-bundle-optimizer`，依赖 Turbopack 的详细模块图。
- 📉 Vercel 使用该技能审计 v0 和 vercel.com，累计减少近 2MB 压缩 JavaScript，多个关键页面节省数百 KB。
- 🧠 代理可重建模块与 chunk 图，识别大型关联模块组，分析导入链，并用最小割找到可延迟加载的导入边界。
- 🛠️ 技能可发现并修复：逻辑可迁移到 React Server Components、大型依赖重复版本、tree shaking 未生效导致的无用代码等问题。
- ⚙️ 使用流程：安装技能后运行 `/next-bundle-optimizer` 获取报告；运行 `/next-bundle-optimizer fix` 应用修改、重新分析并对比快照。
- 📊 人类可用的 Bundle Analyzer 新增路由摘要首页和表格视图，便于按大小排序查找最大贡献模块。
- 🧭 分析器会自动保存快照，支持对比不同构建，衡量优化影响或排查 bundle 增长。
- 🔍 新增关键渲染路径高亮与异步依赖过滤，帮助聚焦首屏同步加载的代码。
- 💬 官方邀请开发者在自己的应用中试用，并通过 GitHub Discussion 等渠道反馈。

---

### [Codemagic Patch | 面向 React Native 的自托管 OTA 更新](https://patch.codemagic.io/?utm_source=rn-weekly&utm_medium=newsletter)

**原文标题**: [Codemagic Patch | Self-hosted OTA updates for React Native](https://patch.codemagic.io/?utm_source=rn-weekly&utm_medium=newsletter)

Patch 是面向 React Native 的自托管 OTA 更新方案，主打快速部署、低成本与完整更新控制。它通过一行命令和 Docker Compose 简化安装，并利用 CDN、指纹校验、二进制差分、发布指标与权限管理，帮助团队安全管理大规模应用更新。

- 🚀 自托管 OTA：为 React Native 提供空中更新，安装与架构高效，可支持数百万用户。
- ⏱️ 快速部署：一条命令启动安装向导，自动配置 OAuth、CDN 缓存规则和 TLS，并通过 Docker Compose 启动服务，约 20 分钟完成。
- 🛡️ 兼容性保护：通过指纹校验检查目标原生二进制，阻止不兼容版本发布。
- 📦 差量更新：设备只下载发生变化的小型二进制差异包，不依赖稳定高速的移动网络。
- 📊 发布管理：支持灰度发布、安装监控、版本推广以及回滚控制，指标展示在仪表盘中。
- 🌐 CDN 扩展：设备向 CDN 发起检查和下载请求，避免服务器因用户量增长而过载。
- ⚖️ 对比优势：相较其他自托管 OTA，Patch 在吞吐、停机风险、指纹校验、差分包、安装时机、发布指标、仪表盘、RBAC 权限和支持许可等方面更完整。
- 🏢 团队经验：由 Codemagic 打造，拥有 10 年以上移动 CI/CD 经验，已向生产应用交付数十亿次 OTA 更新。

---

### [本地快速入门 | Codemagic Patch](https://patch.codemagic.io/docs)

**原文标题**: [Local quickstart | Codemagic Patch](https://patch.codemagic.io/docs)

本文介绍 Codemagic Patch 的本地评估栈快速上手流程：它可在本机运行真实的服务端、Worker、Postgres、Silo 和仪表盘，并用一键本地登录替代正式认证，适合在配置域名或 OAuth 前完整评估服务。文档同时覆盖 React Native 与 Capacitor，并说明如何连接自有应用、运行 OTA 更新演示、查看仪表盘以及清理环境。

- 🧭 文档支持 React Native 和 Capacitor，可通过侧边栏选择器切换；本地评估栈会运行真实服务，但仅用于评估，不适合生产部署。
- 💻 前置要求包括 macOS、Linux 或 Windows 上的 WSL 2，Node.js 20.19+ 或 22.12+，git、curl，以及 Docker 和 Compose v2。
- 📱 如需运行设备演示，还需 iOS Simulator（macOS、Xcode、CocoaPods 或指定 Bundler）和/或 Android 模拟器（Android SDK、Java、adb），以及 Node.js ≥ 22.20 和通过 Corepack 使用 Yarn。
- 🚀 安装 CLI：`npm install -g @codemagic/patch-cli`，然后运行 `cmpatch selfhost local-eval` 启动本地栈；首次运行需数分钟构建镜像，重复运行是安全的。
- 🌐 启动后可访问仪表盘 `http://localhost:8080`，使用预填的 `local-admin@example.com` 一键登录；API 为 `http://localhost:3000`，产物下载地址为 `http://localhost:9100/codemagic-patch`。
- 🧪 本地栈会预置 `demo-app-ios`、`demo-app-android` 以及示例数据，方便在发布前查看有数据的仪表盘。
- 📊 使用 `cmpatch selfhost local-eval status` 可查看服务状态、Silo 控制台、预置 API Token 和示例发布命令。
- 🧱 也可从仓库克隆后运行 `./scripts/local-eval/up.sh`；该方式同样需要 Node.js ≥ 22.20、Yarn，并会全局安装 `cmpatch`。
- ⚠️ 本地评估栈禁用认证且所有端口仅绑定 localhost；如需自有域名部署，应参考正式 Install 指南。
- 🔌 连接自有 React Native 应用时，配置 `CodemagicPatchApiUrl=http://localhost:3000`、`CodemagicPatchDownloadBaseUrl=http://localhost:9100/codemagic-patch`，并从 `cmpatch deployment list` 获取部署密钥。
- 🛠️ 在项目根目录运行 `cmpatch init --server-url http://localhost:3000` 可创建各平台应用并关联项目；不要复用 `demo-app-*`，除非只需要内置演示。
- 📶 Android 模拟器或 USB 设备需执行 `adb reverse tcp:3000 tcp:3000` 和 `adb reverse tcp:9100 tcp:9100`；设备或 adb 重启后需重新转发。
- 🚨 Android Release 构建默认阻止明文 HTTP；仅本地评估时可在 `AndroidManifest.xml` 的 `<application>` 中添加 `android:usesCleartextTraffic="true"`，上架前必须移除。
- 📦 Capacitor 需安装 `@codemagic/capacitor-patch-cli` 和 `@codemagic/capacitor-patch`，在本地栈为各平台创建应用并复制 Staging 部署密钥，再在 `capacitor.config.ts` 中分别配置 iOS/Android 的 `deploymentKey`、`apiUrl` 和 `downloadBaseUrl`。
- 🔁 Capacitor 配置后运行 `npx cap sync`；Android 同样需要 `adb reverse` 转发端口，并注意明文 HTTP 限制。
- 🎬 可选运行 `cmpatch demo` 进行设备演示：CLI 会检查依赖、登录本地栈、构建并启动 Release 应用，展示错误后发布 JavaScript 修复并验证 OTA 更新自动生效。
- 🖥️ 可在 `http://localhost:8080` 浏览 Example Data；示例发布不可下载，若运行了演示可查看对应 demo 应用的 staging 部署。
- 🧹 使用 `cmpatch selfhost local-eval down` 停止栈并保留数据；添加 `--delete-data` 可删除数据库和已存储的 Bundle。
- 🔑 预置 API Token `cm_pat_local-dev-token-change-me-00000001` 仅用于本地脚本，不可用于生产。
- ➡️ 后续可继续阅读 Native setup、验证测试发布、从 Expo Updates/CodePush/Appflow 迁移，以及使用自有域名正式部署。

---

### [](https://devblogs.microsoft.com/react-native/react-native-windows-v0-85-is-here/)

**原文标题**: [🚀 React Native Windows v0.85 is here React Native](https://devblogs.microsoft.com/react-native/react-native-windows-v0-85-is-here/)

React Native Windows v0.85 于 2026 年 10 月 21 日发布，基于 React Native 0.85.3，全面完成向新架构的迁移，并更新 Windows 构建工具链，同时带来组件能力增强、触摸/文本/无障碍/渲染修复和性能优化。

- 🚀 **版本发布**：React Native Windows 0.85.0 基于 React Native 0.85.3。
- 🏗️ **仅支持新架构**：旧架构已被移除，仍使用旧架构的应用需先迁移到 Fabric 才能升级到 0.85；新项目已默认使用新架构。
- 🛠️ **工具链更新**：要求 Visual Studio 2026、.NET 10、Windows App SDK 1.8（Microsoft.WindowsAppSDK 1.8.260508005），升级前需更新构建环境。
- 🪟 **组件能力增强**：Modal 支持 hideTitleBar 和 hideBorder；View 支持 outline 样式；Win32 应用可通过 ReactNativeWin32App 访问 ReactNativeWindow。
- ⚡ **TurboModule 与提示**：TurboModules 可选择提前初始化；Tooltip 可在键盘聚焦时显示，且同一时间仅显示一个。
- 🧩 **可靠性修复**：修复 TextInput 缩放、Unicode 文本长度、多行 TextInput 崩溃、触摸/ScrollView 高 DPI 点击、键盘滚动漂移、指针捕获丢失等问题。
- 🎨 **渲染与无障碍**：修复圆角边框、Image 源变更更新、非活动 Modal 标题栏对比度，以及 accessibilityState.selected 变化时的 UI Automation 选择事件。
- 🐛 **运行时与 WebSocket**：修复关闭时获取运行时崩溃、调用器收到空运行时的竞态、WebSocket binaryType 处理；移除旧版 WinRTWebSocketResource 和 JSBigStringResourceDll 实现。
- 📈 **性能与 CLI**：文本渲染性能提升；run-windows 支持在自定义端口启动 Metro；模板配置更一致。
- 🖼️ **Gallery 应用**：React Native Gallery 2.1.10.0 基于 RNW 0.85.0，可用于体验新功能和组件改进。
- 📦 **发布信息**：提交范围覆盖 2026 年 4 月 1 日至 10 月 19 日，可通过 GitHub Release 和完整变更日志查看详情。

---

### [关于 | Expo 桌面](https://expo-desktop-docs.vercel.app/)

**原文标题**: [About | Expo Desktop](https://expo-desktop-docs.vercel.app/)

Expo Desktop 是一个为 Expo 应用提供 macOS 和 Windows 支持的独立项目；它通过 CLI 和配套库，帮助开发者创建并运行多平台应用。

- 🖥️ 为 Expo 应用增加 macOS 与 Windows 的“尽力而为”支持，并非 Expo 官方背书或维护。
- 👤 该项目由 Jamie Birch 独立开发。
- 🧰 项目包含 `expo-desktop` CLI，以及 `expo-desktop-config-plugins` 等支持库。
- 📱💻 可创建并运行面向 iOS、Android、Web、macOS、Windows 的应用。
- 🚀 快速开始需先满足前置条件，再执行 `npx expo-desktop@latest create-app` 创建应用。
- 📁 进入项目目录后执行 `node --run prebuild`，生成 Xcode、Gradle 和 MSBuild 工程。
- ▶️ 使用 `node --run ios/android/web/macos/windows` 运行对应目标平台。

---

### [](https://legend.so/spark/)

**原文标题**: [Legend Spark · Legend](https://legend.so/spark/)

Legend Spark 是一个实验性、暂不可用于生产环境的 React Native 桌面框架，旨在让 React Native 应用在 Mac 上拥有原生窗口、菜单、对话框和文件能力；你可以先使用预构建 Runner 和 Fast Refresh 开发，再打包为独立的 `.app`。

- 🧪 实验性项目：当前版本为 Spark 0.0.1，明确标注“not for production”。
- 🖥️ 面向桌面：为 React Native 应用提供真实的 macOS 窗口、菜单、对话框和文件系统能力。
- 📦 单一包集成：从 `@legendapp/spark` 导入 Windows、Menus、Shortcuts、Files/Dialogs、Settings、Updates 等模块。
- 🪟 窗口能力：支持命名窗口、显示器、几何布局、关闭守卫和 macOS 原生窗口外观。
- 📋 菜单与快捷键：支持应用菜单栏、上下文菜单、托盘菜单、Dock 菜单及本地/全局快捷键。
- 📁 文件与设置：提供打开/保存面板、原子写入、流、文件监听、废纸篓、JSON 设置、Legend State 持久化和安全存储。
- 🚀 三种运行方式：预构建 Spark Runner、自定义开发构建、独立 `.app` 发布构建。
- ⚡ 开发体验：预构建 Runner 无需 Xcode，支持 Fast Refresh；需要额外原生模块时再构建自定义开发版。
- 🧱 原生架构：界面是 React Native 视图，JavaScript 运行在 Hermes 中，不使用浏览器内核；Node 仅用于工具链且不会打包进应用。
- 🧩 Expo 工作流：Expo Desktop 生成原生宿主，Expo CLI 负责 Metro、日志和重载；Spark 增加桌面 API 与运行时选择。
- ✅ 当前状态：主要目标为 macOS 14+ Apple Silicon；Intel Mac 构建和 Windows 开发仍需原生验证。
- 🔐 发布说明：Spark 0.0.1 首次启动会下载匹配的 macOS Apple Silicon Runner；签名分发需使用自己的应用和凭据测试。

---

### [](https://posthog.com/blog/self-driving-loops?utm_source=twir&utm_campaign=oct28)

**原文标题**: [6-7 loops we use every day to make PostHog self-driving](https://posthog.com/blog/self-driving-loops?utm_source=twir&utm_campaign=oct28)

PostHog 自驱团队分享了 6–7 个日常运行的自动化闭环，用“发现信号—分诊归因—生成报告—创建 PR—人工审核—验证修复”的方式，让 AI 代理承担重复性排查与实现工作，同时保留人类对最终发布的控制。作者认为好闭环应能主动发现问题、清理繁琐工作，并让人随时介入。

- 🔁 **MCP 代理反馈闭环**：代理或用户通过 `agent-feedback` 提交结构化反馈，scout 将负面/受阻反馈聚类、路由负责人、用 `mcp_tool_call` 错误率佐证，并生成报告；任务可自动开 PR，scout 还会回查修复是否真正生效。
- ⚡ **反馈到修复很快**：示例中 `missing_tool` 反馈提交约 5 分钟后生成报告，8 分钟后开出 PR #90832，最终当天进入生产。
- 💬 **Slack 团队 bug 报告闭环**：scout 监视 #team-self-driving 中的 bug、想法和客户反馈，按线程聚合、过滤闲聊并放入自驱收件箱；示例“Task not found”问题最终由 PR #88912 修复并于 9 月 4 日合并。
- 📝 **Issue → 报告 → PR 闭环**：人类写清 GitHub issue/spec，scout 定期扫描范围是否清晰、是否有阻塞或重复工作；就绪后进入实现。示例技能重命名 issue #94896 促成 PR #95499，新增重命名对话框和 `skill-rename` MCP 工具并保留版本与归属。
- 🚨 **异常告警 → 调查 → 修复闭环**：告警监控关键指标并推送到 Slack，团队可追问并引导修复；示例 MCP 错误率升至约 9.9%，定位到 `scout-project-profile-get` 的权限格式不兼容，PR #95623 当天合并。
- 👁️ **Replay Vision 观察闭环**：通过会话回放自动生成结构化观察，发现用户真实卡点；示例“Desktop onboarding friction”监控发现 provider 错误处理缺口，PR #93181 改进重试与错误提示并于 9 月 2 日合并。
- 🧾 **自检查/自验证日志闭环**：定时 scout 扫描运行时日志，判断重复行是重试循环还是多次失败，并检查是否已有修复；示例 Hogland 元数据标签过长问题由 PR #92909 修复。
- 📌 **证据累积与修复验证**：PR 审核期间，scout 会把后续发现追加到同一报告，避免重复调查；合并后继续观察日志，确认失败停止后才关闭问题。
- 📊 **自验证已成常态**：过去一个月约十分之一的 scout 运行包含自验证环节，说明“检查旧发现是否真的修好”已成为常规工作。
- 🛠️ **人类仍在环中**：作者主要参与写 spec、审查报告与 PR、拉合适的人评审、决定是否合并；检测、分诊、去重和根因排查多由闭环先行完成。

---

### [](https://github.com/ccheever/exact2)

**原文标题**: [GitHub - ccheever/exact2: Exact, restarted: rules and scope before code. · GitHub](https://github.com/ccheever/exact2)

Exact2 是一个面向 AI 代理与跨平台交付的应用运行时：用声明式 Contract 描述界面，用 TypeScript/Rust 编写数据逻辑，同一份应用可运行于 Web、macOS、iOS 和 Linux，并强调无 WebView/JS 桥、快速启动和平台原生表现。

- 🧩 **核心理念**：Contract 负责视图、状态和动作，TypeScript/Rust 负责数据源；编译器把界面变成紧凑 plan，Web 端用约 20 KB 运行时驱动真实 DOM，原生端由 Rust runner、Taffy 布局内核和 AppKit/UIKit/GPU 绘制执行。
- 🤖 **Agent 原生**：提供 tree、screenshot、tap、type、state、layout、logs、clock、prefer、perf 十种操作，同一脚本可驱动 Web、macOS、iOS 和 Linux；测试是操作脚本，时钟由代理控制，减少等待和时序抖动。
- ⚡ **速度优先**：目标包括冷启动到首帧 100 ms p50、开发重启 100 ms p50、首像素前不执行应用 JavaScript、单行改动重建 30 秒、完整阻塞检查 65 秒。
- 🎨 **写 Web、交付平台**：布局和命名遵循 CSS；未声明的控件、颜色、字体、动效、手势和可访问性交给平台原生实现；浏览器是布局与表现的对齐基准，必要偏差需声明理由。
- ⚙️ **工作原理**：Contract 经语法、类型、分析和 lowering 四阶段编译；plan 在构建时烘焙常量数据；runner 是 plan 的虚拟机；数据源在单一 seam 后运行，TS 在原生端用 Hermes、Web 用浏览器引擎，Rust 可原生运行或热替换。
- 🚀 **快速开始**：安装 Rust、Bun、Chrome、Xcode 和 Hermes；运行 `bun scripts/exact.mjs setup`；用 `bun host/web/dev.mjs` 跑 Web 开发循环，用 `build.mjs` 跑 macOS/iOS，用 `scripts/agent.mjs` 驱动和测试，用 `exact new` 创建独立应用。
- ✅ **Contract 示例**：Todo 应用展示 shape、component、state、resource、mutation、action、view 和 `app.test.contract`；视图不直接改数据，而是通过命名、类型化的 mutation 调用数据源，测试可在不同宿主上原样运行。
- 📱 **示例应用**：Caltrain 是定义 v1 的真实应用，覆盖 Rust 数据、路由、Canvas 和 GPU；Shelf 展示“少声明、多原生”的风格；Weatherlight、Fieldnotes、Recorder、Markdown、Conduit 等覆盖网络、SQLite、媒体、编辑器和基准测试。
- 📊 **性能基准**：在 RealWorld/Conduit 对比中，Exact Web 运行时约 26 KB，React SSR 为 81 KB；Exact 在 React 完成 hydration 前约 300 ms 已可交互。
- 🧪 **当前状态**：四个宿主已可运行真实应用，布局、文本、绘制、动效、虚拟列表、控件、媒体、数据、原生模块、SSR、交付和代理测试均有覆盖；Windows 初步但未完成，Android 早期，暂无 JSX/React 层，TS 尚不能导入 npm 包运行时代码，生产代码热更新未实现，Linux 编辑和部分分词能力受限。
- 🗂️ **仓库结构**：核心包括 `kernel/`、`contract/`、`plan/`、`runner/`、`motion/`、`host/`、`js/`、`data/`、`gpu/`、`canvas/`、`apps/`、`scripts/`、`llp/`、`rules/` 和 `vendor/taffy/`。
- 🛠️ **开发规则**：先读 `rules/RULES.md`、`rules/DEFERRED.md` 和 `AGENTS.md`；六项阻塞检查总计约 65 秒；强调运行验证、删除而非废弃、设计写入 LLP；项目为 MIT 许可。
- 📌 **版本状态**：Exact 处于 pre-1.0，每日变化，无 API 稳定性、向后兼容或迁移指南；`exact2` 是早期项目的重建版；Snapback4 适配器使用已发布的 0.4.33 及匹配的不可变 Rust 源码修订。

---

### [你好，Graphite：性能](https://wcandillon.dev/article/hello-graphite-performance)

**原文标题**: [Hello, Graphite: Performance](https://wcandillon.dev/article/hello-graphite-performance)

React Native Skia 3.0 已发布，核心变化是渲染后端从 OpenGL 为中心的 Ganesh 迁移到 Skia Graphite，并默认启用多线程渲染。新架构把录制与提交放到独立线程池中，显著减轻 UI 线程压力，提升稳定性、帧率和多画布并行能力；同时为 WebGPU 生态集成和后续性能优化打下基础。

- 🚀 **版本升级**：React Native Skia 3.0 使用 Skia Graphite 栅格化后端，面向现代 GPU API，支持默认多线程。
- 📦 **包名变化**：v3 起以 `react-native-skia` 发布；v2 仍在维护，也已使用新包名。
- ⚠️ **v2 的瓶颈**：Ganesh 将 GPU 上下文绑定到 UI 线程，导致资源跨线程处理复杂、稳定性风险高，并占用宝贵帧预算。
- 🧵 **Graphite 架构**：通过线程池在专用线程录制绘制命令并提交 GPU，React Native Skia 自动完成，减少线程规则和出错概率。
- 🛡️ **稳定性提升**：图像可跨线程无拷贝绘制；命令会校验，GPU 设备丢失可上报并恢复，被拒绝的录制会记录日志。
- 📈 **UI 线程释放**：重画布不再拖累整个应用，React Native 动画在画布旁边仍可保持显示刷新率。
- 🎨 **多画布并行**：多个画布可利用线程池并行渲染；Pixel 8 上双画布吞吐约为单画布的 1.25 倍，iPhone 14 Pro 约为 1.7 倍，但画布过多会受核心数限制。
- ⏱️ **Android 帧调度改善**：Graphite 的先录制后提交模型让呈现时机不再依赖绘制耗时，TextureView 画布在 Pixel 8 上从 58.7 fps 提升到 115.9 fps。
- 💾 **管线与着色器优化**：Graphite 使用更少、更通用的管线，可后台预编译；借助 Dawn/WebGPU 可将编译结果持久化到磁盘，后续启动跳过大部分编译工作，导航过渡中加载 Skia 绘图早期实验帧率约翻倍。
- 🔜 **后续方向**：WebGPU 集成将连接 Three.js、TensorFlow.js 等生态，共享 GPU 设备与资源；Dawn 还带来 YUV 纹理和 GPU fence 等视频/相机能力，第二部分将展开。

---

### [在 react-native-screens 中引入 ScrollViewMarker](https://swmansion.com/blog/introducing-scroll-view-marker-in-react-native-screens/)

**原文标题**: [Introducing ScrollViewMarker in react-native-screens](https://swmansion.com/blog/introducing-scroll-view-marker-in-react-native-screens/)

overview summary  
本文介绍 react-native-screens 新增的 ScrollViewMarker 组件，用于显式告知原生导航 UI 哪个滚动视图是屏幕内容滚动视图，从而修复因 React Native 视图扁平化和复杂层级导致标签栏不最小化、导航栏样式异常、Android Stack 头部闪烁等静默问题。

- 📌 原生导航栏和标签栏需要知道内容滚动视图才能响应滚动，但 UIKit、Android Material 和 react-native-screens 各自依赖不同的启发式查找。
- 🧩 React Native 的视图扁平化会让同一布局有时正常、有时静默失效，例如加个背景色就可能让列表不再是第一个原生子视图，导致 Liquid Glass 标签栏不再最小化。
- ✅ ScrollViewMarker 用声明式包裹滚动视图，替代“猜测第一个可滚动子视图”的脆弱做法，并与最近的 Stack 或 Tabs 屏幕集成。
- 📱 iOS 上标记后 UIKit 直接监听该列表，导航栏和标签栏能正确切换外观，iOS 26+ 标签栏可最小化，并可在列表处设置 scrollEdgeEffects。
- 🤖 Android 上标记解决 Stack 小头部 liftOnScroll 的闪烁问题，让头部在内容滚动时正确变色并保持状态。
- ⚠️ 使用时应直接包裹可滚动组件，只接受单个子元素；标记本身按普通视图布局，需要给它 flex: 1，每屏建议只用一个。
- 🔗 FlatList、SectionList 可直接包裹；LegendList 可同样包裹；FlashList 需通过 renderScrollComponent 配合标记传入。
- 🔢 ScrollViewMarker 是 5.0.0-alpha 的新功能；4.x 不适用，仍建议保持首子级或使用 collapsable={false}。
- 🧠 原理上标记会向上注册到最近的 Stack 或 Tabs 屏幕，嵌套容器逐级传递；启发式仅作为最后回退。
- 🎯 该组件让滚动视图识别从“依赖层级运气”变成显式声明，减少静默故障和开发者对原生层级的额外知识负担。

---

### [一个基于 Expo 的 3 万行 Rust GPU 引擎，以及 12 万次无广告安装](https://expo.dev/blog/doodraw-rust-gpu-engine-expo-config-plugin-100k-installs)

**原文标题**: [A 30,000-line Rust GPU engine on Expo, and 120,000 installs without ads](https://expo.dev/blog/doodraw-rust-gpu-engine-expo-config-plugin-100k-installs)

尚未收到需要总结的文章内容，因此暂时无法生成具体要点。
- 📄 请在“Use the following content:”后粘贴完整文章正文
- 🔍 收到内容后，我会用中文提供概览摘要与带表情符号的要点列表
- ✅ 要点将使用“-”符号，并突出关键信息与核心结论

---

### [使用 Expo 支持 iPhone Duo：开发者指南](https://expo.dev/blog/supporting-iphone-duo)

**原文标题**: [Supporting iPhone Duo with Expo: a developer guide](https://expo.dev/blog/supporting-iphone-duo)

未收到可供总结的正文内容，因此暂时无法提炼文章要点。请提供需要总结的文本，我将按“概述总结 + 表情符号要点列表”的格式用中文输出。

- 📄 当前输入中缺少文章正文
- ✍️ 请粘贴或发送需要总结的内容
- 🧾 收到后将提炼关键信息并生成简洁要点
- ✅ 输出将使用“-”符号和合适的表情符号

---

### [React Native 的内部工作原理 | Code with Beto](https://codewithbeto.dev/blog/how-react-native-works-under-the-hood)

**原文标题**: [How React Native Works Under the Hood | Code with Beto](https://codewithbeto.dev/blog/how-react-native-works-under-the-hood)

文章以“粉色圆形”为例，从 JSX 一路追踪到屏幕上的原生视图，再通过点击变色展示更新链路，系统解释 React Native 在 Fabric 架构下如何由 Metro、Hermes、JSI、Shadow Tree、Yoga 和 UI 线程协作，把 JavaScript 描述转换为真实 iOS/Android 视图，并说明开发热更新与生产更新的原生边界。

- 🧩 Metro 从入口解析依赖、转换 JSX/TypeScript，并将模块打包成 JavaScript bundle；JSX 会被转换为 `jsx()` 函数调用。
- ⚙️ Hermes 是 React Native 默认 JavaScript 引擎；发布构建时会把 bundle 预编译为字节码，安装后的应用可直接在设备上执行。
- 🔗 JSI 是 JavaScript 与 C++ 之间的接口，不是单独线程或布局引擎；Fabric 通过 JSI 与 C++ 渲染核心通信。
- 🌳 Fabric 将 React 元素转换为 C++ 的 Shadow Tree，记录宿主组件的属性、子节点和布局信息；自定义组件本身不会生成独立原生视图。
- 📐 Yoga 根据 Flexbox 样式和可用空间计算尺寸与位置，例如 200×200 的圆在 393×852 空间中定位为 `x=96.5, y=326`。
- 📱 挂载阶段在 UI 主线程创建、配置并插入原生视图；iOS 使用 UIKit，React Native 通过 Objective-C++ 调用，并不会为每个组件生成 Swift 文件。
- 🪶 视图扁平化可省略仅用于布局的包装 `View`，减少原生层级；但 `testID`、无障碍行为或 `collapsable={false}` 等可能阻止扁平化。
- 🔁 点击更新时，React 根据组件身份进行调和，Fabric 计算最小原生变更；结构共享可复用未变化分支，但应用性能仍需关注 JS 开销、大图和频繁更新。
- 🔥 Fast Refresh 在开发时更新相关 JavaScript 并重新渲染，兼容的函数组件编辑可保留状态；原生代码变更仍需要重新构建。
- 📦 生产环境更新如 EAS Update 只能下发与已安装原生运行时兼容的 JS 和资源；新增原生库需要新的原生构建，并需遵守应用商店规则。

---

### [Maestro MCP 服务器 | Maestro 文档](https://docs.maestro.dev/get-started/maestro-mcp?utm_source=this-week-in-react)

**原文标题**: [Maestro MCP Server | Maestro Docs](https://docs.maestro.dev/get-started/maestro-mcp?utm_source=this-week-in-react)

Maestro MCP Server 通过 Model Context Protocol 将 Maestro 的移动端与 Web UI 测试能力接入编码代理，使代理能够编写、运行并调试端到端测试；文档涵盖安装配置、Viewer 使用、更新方式及可用 MCP 工具。

- 🧭 Maestro 实现 MCP，可集成 Claude Code、Claude Desktop、Cursor、GitHub Copilot、Codex、Gemini、Windsurf、JetBrains AI Assistant 等编码代理。
- 🛠️ 安装前需准备 Maestro CLI，以及支持 MCP 的编码代理；不同代理需通过对应配置文件或交互命令添加 Maestro MCP。
- 🔁 配置完成后需重启编码代理，使其连接 MCP，并可针对真实移动模拟器、仿真器或设备检查工作。
- 🖥️ Maestro MCP 内置 Maestro Viewer，可将 iOS 模拟器、Android 模拟器或物理设备嵌入编码代理或浏览器，实时显示命令并支持完整交互。
- 👁️ 通过 `open_maestro_viewer` MCP 工具可打开 Viewer，只需让代理执行“open the maestro viewer”。
- ⬆️ Maestro MCP 随 Maestro CLI 打包，升级 CLI 后需在编码代理中重新加载或重启以连接新版本。
- 🧰 核心工具包括 `list_devices`、`inspect_screen`、`take_screenshot`、`run`、`cheat_sheet`，用于设备发现、界面检查、截图、执行流程和查询语法。
- ☁️ 云工具包括 `list_cloud_devices`、`run_on_cloud`、`get_cloud_run_status`，可列出云设备、提交流程并轮询运行状态。
- 🔐 使用 Maestro Cloud 相关工具需要认证，可运行 `maestro login`，或在非交互环境中设置 `MAESTRO_CLOUD_API_KEY`。
- 📡 MCP 是连接大语言模型与外部数据源、工具和服务的开放标准，采用客户端—服务器架构，并通过 stdio、HTTP/SSE 或 WebSocket 上的 JSON-RPC 2.0 通信。

---

### [](https://github.com/jpudysz/react-native-unistyles/releases/tag/v3.6.0)

**原文标题**: [Release Release v3.6.0 · jpudysz/react-native-unistyles · GitHub](https://github.com/jpudysz/react-native-unistyles/releases/tag/v3.6.0)

react-native-unistyles v3.6.0 是迈向 4.0 的次要版本，重点包括实验性零配置 Metro 集成、性能优化、Reanimated 主题切换修复、useVariants 内存泄漏修复，以及 iOS、Android、Web 和 React Compiler 兼容性改进。

- 🚇 新增实验性 `react-native-unistyles/metro` 零配置集成，可替代 Babel 插件；第三方组件也能跟随主题变化，但 Babel 插件仍是默认方案，Re.Pack、Vite、Next.js 等继续使用 Babel 插件。
- ⚡ 无 unistyle 的 View 不再被关联，普通视图性能提升：900 个视图在 iOS Release 下，重渲染中位耗时从 13.0ms 降至 6.4ms，卸载从 5.0ms 降至 1.3ms。
- 🎨 Reanimated CSS transitions 在主题切换后会动画到新主题颜色，并修复嵌套 `Text`、`Animated.Text` 变体样式等未完全切换主题的问题。
- 🧊 `Suspense` fallback、react-freeze 冻结或隐藏 `<Activity>` 中的视图，在主题变化或重新显示时能正确展示新主题。
- 🧠 修复 `styles.useVariants()` 在动态函数 StyleSheet 下的内存泄漏，堆内存现保持平稳。
- 🍏 iOS：StyleSheet 渐变在 React Native 0.83+ 跟随主题变化；自适应主题下支持 `Appearance.setColorScheme`。
- 🤖 Android：修复 `FlatList` 翻转 `horizontal` 时的渲染错误，以及翻回后注册表泄漏问题。
- 🌐 Web：修复 `createUnistylesElement` 包裹组件上 Reanimated `useAnimatedStyle` 失效，以及断点媒体查询在小数视口宽度下的间隙问题。
- ⚛️ React Compiler：调用 `styles.useVariants()` 的组件现在可正常编译。
- 🧪 内部改进：未知类组件 ref 现在解析为第一个原生视图，而不是抛出错误；同时感谢本次发布的多位贡献者。

---

### [发布 v11.0.0 · ammarahm-ed/react-native-actions-sheet · GitHub](https://github.com/ammarahm-ed/react-native-actions-sheet/releases/tag/v11.0.0)

**原文标题**: [Release v11.0.0 · ammarahm-ed/react-native-actions-sheet · GitHub](https://github.com/ammarahm-ed/react-native-actions-sheet/releases/tag/v11.0.0)

本次发布为 react-native-actions-sheet v11.0.0，核心是将手势与动画迁移到 UI 线程，显著提升 sheet 的响应、滚动可靠性与交互体验，同时新增多项 API、可访问性改进和问题修复；该版本要求 React Native 新架构。

- 🚀 v11.0.0 重大发布：手势引擎完全重写并默认在 UI 线程运行，JS 线程繁忙时不再导致 sheet 卡顿。
- 🖐️ 拖拽、滚动与拖拽交接、打开/关闭/吸附动画默认通过 worklet 在 UI 线程执行。
- ⚡ 新增基于速度的吸附：快速滑动会根据释放速度进入下一吸附点或关闭，而不仅依赖拖拽距离。
- 📜 同一 sheet 内的多个可滚动区域现在可独立并同时处理。
- 🧩 新增 `useSheetScrollable`、`SheetGestureBlocker`、`useSheetGestureRegion`、`useSheetPosition`、`onChangeWorklet`、`dimBackdropOnDrag` 等 API。
- 🎨 重设计 `drawUnderStatusBar`：顶部圆角变平，sheet 平滑填充状态栏后方；拖拽关闭时背景默认渐隐。
- ♿ 可访问性增强：sheet 对屏幕阅读器呈模态化，支持 VoiceOver/TalkBack 退出手势，吸附点下抓手可调，并新增 `accessibilityLabels`。
- 🍎 iOS 上 `onClose` 与 `SheetManager` Promise 会在原生 Modal 关闭后解析，便于安全弹出 alert、分享面板、图片选择器或跳转模态页面。
- 🧪 提供官方 Jest mock：`react-native-actions-sheet/jest/mock`。
- 🛠️ 修复 Android 底部随机多余空白、iOS 每次输入时 resize、嵌套 sheet 有时未全部关闭、Web 废弃属性警告等问题。
- ⚠️ 迁移要求：v11 需要 React Native 新架构；`react-native-worklets` 改为 peer dependency；不再依赖 `react-native-linear-gradient`；可通过 `legacyGestures` 回退旧手势引擎。
- 📚 新增文档网站，并包含大量其他修复与改进。

---

### [发布 · callstack/react-native-bottom-tabs · GitHub](https://github.com/callstack/react-native-bottom-tabs/releases)

**原文标题**: [Releases · callstack/react-native-bottom-tabs · GitHub](https://github.com/callstack/react-native-bottom-tabs/releases)

该页面汇总了 callstack/react-native-bottom-tabs 仓库的发布记录，最新版本为 1.5.0，重点覆盖 iOS 27/Android 构建兼容、Expo 模板改进、导航包同步发布以及 React Native 0.87 支持。

- 🚀 最新 1.5.0 新增 iOS 27+ 的 prominent 标签角色，修复 iOS 27 标签切换或最小化后选中 tint 残留，并支持 iOS Swift Package Manager。
- 🤖 1.5.0 修复 Android AGP 9 内置 Kotlin 构建问题，移除不兼容的 kotlin-kapt，切换标签时应用按路由 activeTintColor，并支持 React Native 0.87。
- 🍎 1.5.0 还修复了 iOS 27 SDK 下使用 search 角色时标签标题、选中图标和无障碍标签偏移的问题。
- 📦 @bottom-tabs/react-navigation 1.5.0 同步发布；Expo 模板 1.1.4 改进 Android 图标与颜色、改用开发构建、迁移到 React Native Testing Library 并补充 lint/typecheck。
- 🎨 1.4.0 增加图标渲染模式以保留原始颜色，并在 iOS Liquid Glass 悬停时显示聚焦图标；Android 暴露测试 ID，修复 Xcode <26 编译问题。
- 🧭 1.3.1 修复 react-navigation 中 CommonActions.navigate 的弃用对象参数；Expo 模板 1.1.2 对齐 Expo SDK 54 依赖以修复安装。
- 🧪 1.3.0 引入 experimental_bakedTintColors 应对 iOS 26 Liquid Glass tint，并修复 iOS 27 切换后页面不渲染、phantom tab switch、tabBarHidden、tvOS 编译和过渡平滑等问题。
- 🗂️ 发布由 github-actions 自动生成，页面列出多个版本及标签，涵盖 1.3.0 至 1.5.0 的主要特性与修复。

---

### [发布 v1.20.0 · software-mansion/radon-ide · GitHub](https://github.com/software-mansion/radon-ide/releases/tag/v1.20.0)

**原文标题**: [Release v1.20.0 · software-mansion/radon-ide · GitHub](https://github.com/software-mansion/radon-ide/releases/tag/v1.20.0)

Radon IDE v1.20.0 是一次功能与稳定性更新，重点加入 iPhone Duo 折叠屏模拟器支持，并适配 React Native 0.88 与 Expo SDK 58，同时修复大量 Expo Go、模拟器、视图层级和构建相关问题。

- 📱 新增 iPhone Duo 折叠屏模拟器支持（Xcode 27.1）：可用底部栏按钮折叠/展开，按住 ⌥ 选择任意铰链角度，所有工具支持双屏。
- 🧩 支持 React Native 0.88、Expo SDK 58，包括 expo-router 58。
- ⚠️ 对未使用 UIScene 生命周期、将在 iOS 27 崩溃的应用，启动前会警告并链接 Expo 迁移指南。
- 🖥️ View Hierarchy 会在设备旋转或应用重载后自动刷新；大变更时可能暂停自动更新，可用 Refresh 手动刷新。
- 🤖 设备预览可跟随 Argent AI 代理的旋转操作；卡在启动中的模拟器会自动重启；Android 模拟器启动不再抢占编辑器焦点。
- 🐞 修复 Expo Go + React Native 0.87 在 iOS 启动卡死、CPU profile 无法解析源文件、Expo Go iOS 方向检测滞后等问题。
- 📱 修复 Expo Go 56/57 在 Android 上无法调试却无限等待的问题，现会说明原因并建议使用 expo-dev-client。
- 🖱️ 修复旋转设备上鼠标滚轮方向错误、iOS 27 上 View Hierarchy 选择器误选 UIKit 浮动栏、切换 Radon 版本后 iOS 模拟器启动崩溃等问题。
- 🛠️ 修复构建错误被“Expo Prebuild skipped”提示遮挡、带 app.json 的裸 React Native 项目被误判为 Expo Go、Android 模拟器首次启动超时或中断后无法启动等问题。
- 🚀 其他改进：删除或切换启动中设备最长耗时一分钟的问题已修复；iOS 跳过 Expo 开发菜单引导页，与 Android 保持一致。

---

### [发布 create-react-native-library@0.64.0 · callstack/react-native-builder-bob · GitHub](https://github.com/callstack/react-native-builder-bob/releases/tag/create-react-native-library%400.64.0)

**原文标题**: [Release create-react-native-library@0.64.0 · callstack/react-native-builder-bob · GitHub](https://github.com/callstack/react-native-builder-bob/releases/tag/create-react-native-library%400.64.0)

本次发布为 create-react-native-library 0.64.0（2026-10-22），主要升级 Node.js 与 React Native/Expo 支持，正式启用 C++ 模板，并集中修复示例应用生成、包名处理、Nitro、Codegen、Android 构建及 Turborepo 等问题。

- ⚠️ 破坏性变更：Node.js 版本要求提升为 `^22.22.2 || ^24.15.0 || >= 26.0.0`。
- 🚀 更新 React Native 至 0.88.0，Expo SDK 至 58。
- 🧱 C++ 模板不再处于实验阶段，无需 `includesGeneratedCode: true`，支持 React Native 0.88+ 与 Expo SDK 58+。
- 📦 生成项目默认使用 Yarn 4.18.1。
- 🐛 保留示例应用的忽略规则，如 `.xcode.env` 和 `*.xcworkspace/`。
- 🐛 避免生成示例应用时使用过期的 Community CLI 缓存。
- 🐛 使 ESLint/Jest 添加的 `@react-native/*` 包版本与示例应用的 React Native 版本匹配。
- 🐛 修复 `react-native-test-app` 示例在 React Native 需要更高 React 版本时的生成问题。
- 🐛 拒绝作用域或 `react-native-` 前缀后以数字开头的包名，并修复连续/尾部分隔符包名的原生类名生成。
- 🐛 当描述、作者或仓库 URL 含引号时，仍能生成有效的 `package.json`。
- 🐛 修复 podspec 的 `source` 指向、作用域包名的 Expo slug 生成等问题。
- 🐛 完善本地 Nitro 库设置，添加 `react-native-nitro-modules`、`nitrogen`，并提示运行 `nitrogen`。
- 🐛 仅在使用 Codegen 时为本地库添加 `codegenConfig`，并修复 Nitro 视图配置加载与 `color` 属性类型。
- 🐛 Android C++ 模板支持 CMake 4，Turborepo 会在相关原生文件变化时重建原生代码。
- 🐛 对暂存的 `.jsx` 和 `.tsx` 文件运行 pre-commit 类型检查，并避免 npm 响应慢时使用过期回退版本。
- 👥 贡献者：satya164、dcavalcante、RezoanurRahman。

---

### [Keyframer Inspector：面向所有平台的动效调试器](https://keyframer.dev/inspector)

**原文标题**: [Keyframer Inspector: a motion debugger for every platform](https://keyframer.dev/inspector)

Keyframer Inspector 是一款免费的跨平台动画调试工具，通过开源 SDK 与桌面应用，将模拟器或真机上的每个动画关联到启动它的代码行；支持慢放、逐帧、曲线调参并回写源码，还可让编码代理和 CI 检查动效质量。

- 🧭 **核心能力**：添加开源 SDK 并打开桌面应用后，模拟器或手机上的每个动画都会显示对应代码行，便于定位、调试和优化。
- ⏱️ **慢放与逐帧**：支持 1x、0.5x、0.25x、0.1x 速度，暂停和逐帧步进；即使慢放录制，仍报告真实速度时序。
- 🎛️ **曲线调参与回写**：以值/速度随时间展示动画，显示过冲、稳定时间、峰值速度和丢帧；可拖拽结束值、时长、过冲峰值或稳定线，预览后“Apply to code”写回源码。
- 🔗 **动画链调试**：可在同一区块内调试 `withDelay`、`withTiming`、`withSpring` 等完整链条，并保留上一次运行轨迹作对比。
- 📱 **多平台支持**：React Native（Reanimated、Expo 或 bare）、Flutter（隐式动画、Hero、Web）、iOS（UIKit、SwiftUI 可选追踪）、Android（Views、Compose 可选）以及 macOS、Windows、Linux 桌面端。
- 🐞 **问题诊断**：Problems 标签按丢帧成本排序问题，指出位置并给出框架相关修复建议，包括忽略“减少动态效果”、隐藏/后台动画、同一值多写入者、动画中断跳变及渲染成本提示。
- 🤖 **代理与 CI 检查**：模拟器代理驱动应用、Inspector 测量动效；每个行为一个可读检查文件，`keyframer-inspect ci` 可在多个模拟器/仿真器上约束 PR，支持 `settle < 400ms`、`overshoot < 5%`、无丢帧等预期。
- 📤 **CI 输出**：支持文本、JSON、GitHub annotations 和 JUnit 输出；流程可来自 agent-device 脚本、Maestro、Argent 或普通步骤。
- 💻 **桌面下载**：macOS 提供 Apple silicon 与 Intel 版本，已签名并公证；Windows 提供 NSIS 安装包；Linux 提供 AppImage 和 `.deb`。
- 💰 **价格**：调试器免费且 SDK 开源；生产监控即将推出，按每月会话数计费：1k 免费，50k 为 $5/月或 $50/年，200k 为 $15/月或 $150/年，500k 为 $29/月或 $290/年，1M 为 $49/月或 $490/年，3M 为 $119/月或 $1190/年，超过 3M 需联系。

---

### [发布 v3.7.0 · LegendApp/legend-list · GitHub](https://github.com/LegendApp/legend-list/releases/tag/v3.7.0)

**原文标题**: [Release v3.7.0 · LegendApp/legend-list · GitHub](https://github.com/LegendApp/legend-list/releases/tag/v3.7.0)

本次 LegendApp/legend-list v3.7.0 发布重点修复滚动 ref 方法的 Promise 行为，新增 cancelScroll、scrollToKey、anchorVisibleContent 等 API，并完善自动跟随末尾、RTL、键盘、动画与性能等边界场景；同时引入若干类型必填项，自定义实现或 mock 需同步更新。

- 🛠️ 修复 scrollToIndex、scrollToOffset、scrollToItem、scrollToKey、scrollToEnd、scrollIndexIntoView、scrollItemIntoView：Promise 在滚动落定、被用户输入中断、取消/替换、无法到达目标（目标移除、数据集替换、卸载）时解析，不再提前或永不解析。
- 🆕 新增 ref 方法：cancelScroll 停止排队和活动滚动；scrollToKey 按稳定 key 跨 prepend 导航；anchorVisibleContent 捕获并保持可见内容锚点，可传 { key } 选择条目，或 { hold:false } 仅生成快照。
- 🧩 类型变更：LegendListRef / LegendListState / SectionListRef 等新增必填成员（cancelScroll、scrollToKey、anchorVisibleContent、distanceFromEnd、isFollowingEnd 等），实现或 mock 这些类型时必须补齐；dataKey 为可选。
- 🎯 scrollIndexIntoView 新增 viewportMargin: { start, end }，并支持 itemOffset / itemLength 与 scrollItemIntoView 一起显示条目内区域，适用于垂直和水平列表。
- 📊 getState() 暴露 distanceFromEnd、isFollowingEnd、dataKey，getState().listen 接受 isFollowingEnd；distanceFromEnd 不是 listen key，需按需读取。
- 🔚 maintainScrollAtEnd.on.dataAppend 仅跟随保持原有 item key 顺序的追加；暂停时保留结束意图，isFollowingEnd 持续报告该意图。
- 👆 onUserScroll 仅对真实用户手势触发（原生拖拽及惯性、Web 触摸/滚轮、滚动键、滚动条、iOS 状态栏点击），不因库或 ref 滚动触发，仍为 experimental。
- ♿ 修复屏幕阅读器滚动、iOS 状态栏点击、原生滚动/Reanimated 滚动等场景对 end following 和 onUserScroll 的影响；必要时在 JS 线程先调用 cancelScroll。
- 🧭 修复触摸板惯性取消滚动命令、RTL 横向偏移、scrollToOffset 达到 contentContainerStyle 最小尺寸、getFixedItemSize/extraData 变更等边界问题。
- 📏 修复 end 阈值重复计算 trailing content 和键盘 inset，重新检查 onStartReached / onEndReached，使分页回调可在布局变化时触发。
- 🎞️ 修复动画列表滚动时 itemLayoutAnimation、短列表增长、footer/视口变化、延迟测量、拖拽到惯性交接等场景的 end following 对齐。
- ⌨️ 修复 scrollMessageToEnd({ closeKeyboard:true }) 与键盘关闭的联动，避免回退或重复关闭，并处理冻结状态残留。
- 🚀 性能优化：启用 recycleItems 时优先复用离屏热行，跳过未变化追加前缀的 key 提取。

---

### [发布 rnsec v1.4.0 - 18 条新规则、CI 集成和更少误报 · adnxy/rnsec · GitHub](https://github.com/adnxy/rnsec/releases/tag/v1.4.0)

**原文标题**: [Release rnsec v1.4.0 - 18 new rules, CI integrations and fewer false positives · adnxy/rnsec · GitHub](https://github.com/adnxy/rnsec/releases/tag/v1.4.0)

rnsec 1.4.0 于 2026 年 10 月 23 日发布，安全规则从 87 条增至 105 条，新增 18 条规则，并增强 CI 集成、减少误报；升级后可能出现此前被隐藏的新发现，建议用基线管理存量问题。

- 🚀 新增 18 条安全规则，覆盖凭据泄露、加密/TLS/认证、存储与注入、Android/iOS 配置、WebView 与供应链等场景。
- 🧩 支持通过 `rnsec scan --sarif rnsec.sarif` 将结果上传至 GitHub Code Scanning。
- 📌 新增基线机制：`--write-baseline` 记录当前发现，`--baseline` 仅对新增问题失败。
- 🎚️ 支持配置失败阈值：`--fail-on high|medium|low|none`，默认仅 HIGH 导致退出码 1。
- ⚙️ 支持 `severityOverrides` 调整规则严重性，`// rnsec-ignore: RULE_ID reason` 忽略单条发现。
- 🔍 发现项带有 `confidence`，可用 `--min-confidence medium` 仅显示更确定的问题。
- 🧹 降低误报：`__DEV__` 仅作用于受保护代码，设计上公开的密钥降为 LOW，同行重复项合并，多条规则匹配更严格。
- ⚠️ 升级注意：可能新增 HIGH 发现；`.gitignore` 默认生效，可用 `--no-gitignore` 扫描被忽略文件。
- 🧾 `--json` 标准输出为纯 JSON，提示信息移至 stderr，管道输出不再被截断在 8 KB。
- 🔧 修复 `ASYNCSTORAGE_SENSITIVE_KEY`、`--changed-files` 与 `--path` 配合、非 git 目录检查提示等问题。
- 📦 安装方式：`npm install -g rnsec@1.4.0`；要求 Node.js 20 或更新版本。
- 🧭 已知缺口：暂不含 typosquat 检测与 CodePush 代码签名检查；Expo 配置规则仅读取 `app.config.js|ts` 中的字面量值。

---

### [发布 8.32.0 · getsentry/sentry-react-native · GitHub](https://github.com/getsentry/sentry-react-native/releases/tag/8.32.0)

**原文标题**: [Release 8.32.0 · getsentry/sentry-react-native · GitHub](https://github.com/getsentry/sentry-react-native/releases/tag/8.32.0)

sentry-react-native 8.32.0 于 10 月 22 日发布，主要新增 React Native 与 WebView 的链路追踪连接能力，并修复 Expo、HTTP 计时、Windows 原生打包及 iOS 性能相关问题，同时更新依赖版本。

- 🔗 新增 `sentryWebViewProps`，支持通过 `allowedHosts` 将 React Native traces 与内嵌 WebView 连接。
- 🛠️ 修复 Expo 插件在 iOS 使用 Swift Package Manager 时无法正确找到 `ios/.xcode.env` 的问题。
- ⏱️ 修复 React Native 0.83 以下及检测到 `expo/fetch` 时 HTTP timing listeners 泄漏，并正确遵循 `enableHTTPTimings` 选项。
- 🪟 修复 Windows 构建的原生包因包含 `@sentry/browser` feedback 模块和仅服务端 `@sentry/core` 模块而导致启动失败的问题，尤其是 `includeWebFeedback: false` 场景。
- ⚡ 默认不再用 `turboModuleContextIntegration` 包装 SDK 自身的 `RNSentry` 模块，避免每次调用多次写入 native scope、增加 iOS CPU 开销；如需恢复可添加 `{ name: 'RNSentry' }`。
- 📊 为 `_experiments.profilingOptions` 在 `trace` 和 `manual` 生命周期中启动/停止 native UI profiler，并导出 `Sentry.profiler`。
- 🧩 设置 `profilingOptions` 时默认添加 `uiProfilingIntegration`；若设置 `defaultIntegrations: false`，需手动加入 `Sentry.uiProfilingIntegration()`。
- 📦 将 Cocoa SDK 从 v9.30.2 升级至 v9.31.0，CLI 从 v3.8.0 升级至 v3.8.1。

---

### [推出 @expo/agent-cli：专为智能体设计的 CLI](https://expo.dev/blog/introducing-expo-agent-cli)

**原文标题**: [Introducing @expo/agent-cli: the CLI designed for agents](https://expo.dev/blog/introducing-expo-agent-cli)

目前没有收到可总结的正文内容，因此无法生成文章要点。
- 📄 请提供需要总结的文章或文本内容。
- ✍️ 收到内容后，我会按要求整理成简洁的中文要点列表。
- 📌 输出将包含概述总结，并使用“-”符号和合适的表情符号逐条呈现。

---

### [发布 v0.30.0 · software-mansion/argent · GitHub](https://github.com/software-mansion/argent/releases/tag/v0.30.0)

**原文标题**: [Release v0.30.0 · software-mansion/argent · GitHub](https://github.com/software-mansion/argent/releases/tag/v0.30.0)

Argent v0.30.0 已发布，自 v0.29.0 起包含 27 次提交，主要聚焦 CLI、调试器、安装器、E2E 流程、Android 设备支持与依赖更新，并新增网络请求抓包和 Android 模拟器折叠支持。

- 🚀 发布 v0.30.0，包含 27 个提交，并有 2 位新贡献者加入
- 🖥️ CI 优化：macOS 任务改用 GitHub 更大的 xlarge runner
- 🛠️ CLI 修复：拒绝空参数值，并让 server status/stop/logs 正确响应 `--help`
- 🐞 调试器修复：旧版 Metro attach 时避免构建 source-map
- 📦 工具与技能修复：符号链接 tar 上传目标、Chromium 路由到 `argent-device-interact`
- 🧪 测试与 E2E 改进：Metro 仅停止本次启动的进程，修复 `discover-tools.sh` 并检查所有 shell 脚本
- 🔁 破坏性重构：Argent flows 重命名为 Argent e2e，旧 flow 名称保留为别名
- 📱 Android 改进：支持模拟器折叠、容忍缺失 keyguard 行、慢速关闭后解锁，并在 devtools helper 空闲关闭后重连
- 🌐 网络能力增强：在 React Native 中捕获 XMLHttpRequest 与 axios 流量
- 🧹 维护更新：升级多组 npm 与 GitHub Actions 依赖，移除卸载时 `.kiro/skills` 链接，并忽略 `.claude/` 的 ESLint 配置

---

### [](https://github.com/callstack/agent-device/releases)

**原文标题**: [Releases · callstack/agent-device · GitHub](https://github.com/callstack/agent-device/releases)

overview summary  
该页面是 callstack/agent-device 的 GitHub Releases 发布记录，集中展示 v0.21.24 至 v0.21.33 的版本更新。整体以高频小版本迭代为主，重点覆盖 iOS、Android、macOS 设备自动化能力、快照与交互可靠性、性能优化、测试与 CI 工程化、发布流程和文档重构，并迎来多位新贡献者。

- 🚀 最新版本为 v0.21.33，主要包含 iOS 返回回退、快照桥接、折叠屏模拟器旋转、Android Compose 角色发布及原生重复代码检测等改动。
- 🍎 iOS 相关更新密集，涉及快照捕获、键盘与输入、手势合成、iPad Simulator AX 桥接、XCTest 稳定性及错误原因上报。
- 🤖 Android 持续增强设备与交互支持，包括 Compose 可点击父节点、Fire OS/Android TV 识别、硬件静音/休眠/唤醒/媒体按键及快照性能。
- 🖥️ macOS 能力扩展明显，如将每个原生 macOS 应用视为独立设备、按应用路径打开、SwiftUI 表单滚动和 AX 快照修复。
- ⚡ 多个版本聚焦性能与稳定性，包括缩短快照耗时、优化辅助器捕获、减少冗余等待、修复键盘/焦点/长按/选择器边界问题。
- 🧪 测试与质量门禁持续强化，增加覆盖率、CRAP 指标、变异测试、重复代码检测、快照桥接测试和跨平台烟雾测试。
- 📦 发布与 CI 流程多次调整，包括 npm trusted publishing、每日 nightly、发布保护校验、CI 任务合并及依赖安全告警清理。
- 👥 社区贡献活跃，v0.21.24 至 v0.21.33 期间多位新贡献者首次提交，涉及 iOS、Android、proxy、macOS 和 release 等方向。
- 📚 文档与工程结构同步演进，新增能力矩阵、集成指南、Maestro 流程文档，并推进 daemon、contracts、test-kit 等模块化重构。

---

### [发布 v0.11.0 · software-mansion/react-native-executorch · GitHub](https://github.com/software-mansion/react-native-executorch/releases/tag/v0.11.0)

**原文标题**: [Release v0.11.0 · software-mansion/react-native-executorch · GitHub](https://github.com/software-mansion/react-native-executorch/releases/tag/v0.11.0)

React Native ExecuTorch v0.11.0 已发布，重点升级 LLM 的模块化 TypeScript 运行器与采样能力，新增深度估计、图像修复、向量检索和语音支持，并通过 Vulkan 与 XNNPACK int8 优化移动端性能；同时包含实验性 API 与部分模型变体的破坏性变更。

- 🚀 **版本发布**：v0.11.0 于 10 月 27 日发布，包含 5 个提交，并整合 v0.10.1–v0.10.7 的全部修复。
- 🧠 **LLM 能力增强**：LLM 生成改为模块化 TypeScript 运行器，覆盖文本、多模态和 Gemma，并采用基于 llama.cpp 的完整采样器，支持约束解码与细粒度生成控制。
- 📏 **LLM 模型更新**：重新导出上下文窗口最高 16k tokens 的 LLM，新增 `enable_thinking` 聊天模板选项和 MiniCPM5-2B。
- 👁️ **计算机视觉扩展**：新增 Depth Anything V2/V3、ZipDepth 深度估计，MI-GAN 图像修复，MediaPipe Face Mesh 关键点；Core ML 分割模型可返回索引图。
- 🔎 **检索功能新增**：新增 `createVectorStore` 内存向量存储，支持 top-k 余弦/点积查询与元数据过滤；新增 ColBERT 晚期交互嵌入、LFM2.5-ColBERT-350M 和 `maxSim` 辅助函数。
- 🗣️ **语音支持**：Kokoro 新增中文支持和词级时间戳。
- ⚡ **性能与模型优化**：Android 上 Vulkan 成为风格迁移、YOLO26、RF-DETR、FastSAM、BlazeFace 和 SDXS 的默认后端；Whisper、YOLO26 等多个模型支持 XNNPACK int8，Core ML 文本嵌入器以 int8 提供服务。
- 📊 **基准测试**：为每个注册表变体提供按设备划分的延迟和内存基准数据。
- ⚠️ **破坏性变更**：`@experimental` LLM runner API 已变更，但聊天和生成 API 不变；移除 15 个未量化 XNNPACK LLM 变体，并弃用 66 个有更快量化替代版本的未量化变体，计划在 v1.0.0 移除。

---

### [Node.js — 2026年10月21日星期三安全版本发布](https://nodejs.org/en/blog/vulnerability/october-2026-security-releases)

**原文标题**: [Node.js — Wednesday, October 21, 2026 Security Releases](https://nodejs.org/en/blog/vulnerability/october-2026-security-releases)

Node.js 项目于 2026 年 10 月 21 日发布 26.x、24.x、22.x 的安全版本，修复多项高危与中低危漏洞，最高严重级别为 HIGH，涉及 DNS、TLS 证书校验、Brotli 解码、HTTP 连接复用、crypto、ZIP 与权限模型等，并更新多个依赖；建议尽快升级至 v26.12.1、v24.22.1、v22.23.4。

- 🗓️ 安全版本计划于 2026 年 10 月 21 日或之后不久发布，覆盖 26.x、24.x、22.x 版本线。
- ⬆️ 对应修复版本为 Node.js v26.12.1、v24.22.1、v22.23.4。
- 🚨 三个版本线修复的最高严重级别均为 HIGH。
- 📦 本次更新包含 c-ares、ca-cert、OpenSSL、SQLite、Undici 等依赖更新，以修复公开漏洞。
- 🌐 CVE-2026-105482（高危）：`dns.resolve*()` 与 `dns.reverse()` 会截断含 NUL 字符的主机名，可能绕过域名白名单校验。
- 🔐 CVE-2026-105483（高危）：TLS 主机名校验未识别全角数字 IP，可能导致证书主机名绕过，影响 26.x、24.x。
- 🔢 CVE-2026-106069（高危）：前导零 IPv4 地址在 TLS 校验与系统解析器之间规范化不一致，可能用错误 IP 的证书通过认证。
- 💥 CVE-2026-111497（高危）：内置 Brotli 解码器存在越界写入，恶意压缩数据可能导致崩溃、内存泄露或远程代码执行。
- 🔁 CVE-2026-105481（中危）：HTTP Agent 复用 keep-alive socket 时，可能把请求发送前已到达的响应当作新请求的合法响应。
- 🧾 CVE-2026-106072（中危）：非规范 IPv4 主机名可仅凭 DNS SAN 证书认证 IP 端点，绕过 IP SAN 要求。
- 🎲 CVE-2026-106074（中危）：`crypto.randomUUID()`、`randomUUIDv7()`、`randomInt()` 的熵缓存可能写入用户态启动快照和 SEA，导致多个进程重复相同随机值。
- 🗜️ CVE-2026-106070（低危）：`zlib.ZipFile` 在 ZIP 头校验失败后可能返回攻击者控制的前缀字节，影响 26.x。
- 📁 CVE-2026-106071（低危）：Permission Model 通配符 radix 查找可能过度授权，例如 `--allow-fs-read=/etc/passwd.*` 也可能允许读取 `/etc/passwd`，影响 26.x。
- 🚫 CVE-2026-106073（低危）：`fs.realpathSync()` 缺少必要读权限检查，可绕过 Permission Model 枚举受限目录外路径。
- ⚠️ 已结束生命周期（EOL）的版本在安全发布时始终受影响，应使用受支持的最新版本。
- 🤝 超过 Maintenance LTS 阶段的版本可通过 OpenJS Ecosystem Sustainability Program 合作伙伴获得商业支持。
- 📬 可通过 Node.js 安全政策、SECURITY.md 流程及 nodejs-sec 邮件列表获取漏洞报告和更新信息。

---

### [](https://nolanlawson.com/2026/10/28/the-ai-cost-of-javascript-frameworks/)

**原文标题**: [The AI cost of JavaScript frameworks | Read the Tea Leaves](https://nolanlawson.com/2026/10/28/the-ai-cost-of-javascript-frameworks/)

本文作者 Nolan Lawson 让 AI 代理用多种 JavaScript 框架/元框架构建同一款 Pokémon 应用，并以多次运行的中位数衡量构建成本、耗时、token、Lighthouse 性能/可访问性、JS 体积、TBT、LCP 和代码行数。文章的核心主张是：在 AI 编程时代，选择框架仍应基于证据而不是“感觉流”；结果显示轻量 MPA 方案通常在成本与性能上占优，但实验本身存在随机性和偏向 SPAs 等局限。

- 🧪 **实验设计**：使用 PokéAPI 构建一个小而完整的 Pokémon 应用，要求代理使用指定框架的最新版本，并通过规范一致性测试防止作弊；每个框架取 3–5 次运行的中位数。
- 💰 **构建成本**：Hono+htmx（$2.67）、Astro（$2.76）、Nuxt（$2.82）最便宜；SvelteKit（$4.28）、Gracile+Lit（$4.65）、Angular（$4.97）最贵。
- ⏱️ **时间与 token**：Astro 约 8.2 分钟、Hono+htmx 约 8.6 分钟、Nuxt 约 9.0 分钟较快；Angular 约 17.2 分钟最慢，token 消耗也最高之一。
- 📉 **Angular 异常**：Angular 有 2 次未能构建可运行应用，最终只取 3 次迭代；其成本高也与代码量较大相关。
- 📊 **Lighthouse 结果**：性能、可访问性和 CLS 分数几乎饱和，各框架差异不大；Angular 性能 98、Accessibility 100，Astro/Hono+htmx/Nuxt 等多为 100/100。
- 📦 **JS 体积差异明显**：Astro 为 0 KiB、Vanilla 7 KiB、Gracile+Lit 8 KiB、Hono+htmx 18 KiB；Next.js 142 KiB、TanStack Start 118 KiB、React Router 115 KiB 较重。
- 🧱 **运行性能**：TBT 上 Astro、Gracile+Lit、Hono+htmx、SvelteKit、Vanilla 接近 0 ms；Next.js 约 71 ms、Angular 约 103 ms。
- 🖼️ **LCP 偏向 MPA**：Astro 约 810 ms、Gracile+Lit 约 956 ms、Hono+htmx 约 978 ms 表现好；Next.js 约 2090 ms、TanStack Start 约 2028 ms 较慢，SPA 普遍受罚。
- 🧮 **可维护性**：以代码行数衡量，Hono+htmx 约 1370 行、Nuxt 约 1415 行、Astro 约 1461 行较少；Angular 约 2009 行最多，Hono+htmx 约用 Angular 70% 的代码实现类似功能。
- ⚠️ **重要局限**：LLM 和 Lighthouse 都有随机性；应用样本单一、只看首页；Lighthouse/Core Web Vitals 对 SPA 不利；MCP/skills 使用不一致，作者甚至怀疑当前 MCP/skills 可能弊大于利。
- 🧭 **结论**：作者并非要“封杀”某框架，而是鼓励开发者在 vibe coding 时代重新审视技术栈选择；基准已开源，欢迎他人复现、改进或提出反例。

---

### [](https://nodejs.org/en/blog/release/v26.13.0)

**原文标题**: [Node.js — Node.js 26.13.0 (LTS)](https://nodejs.org/en/blog/release/v26.13.0)

Node.js 26.13.0 于 2026 年 10 月 28 日发布，代号为 “Lithium”，标志着 Node.js 26.x 正式进入长期支持（LTS）阶段。本次发布主要更新了 LTS 元数据，并未包含相对 26.12.1 的功能变更，同时提供了多平台安装包、二进制文件、源码及校验信息。

- 🚀 Node.js 26.13.0 发布，版本代号为 “Lithium”，属于 LTS 版本。
- 📅 发布日期为 2026 年 10 月 28 日，由 Richard Lau 发布。
- 🛠️ 该版本将 26.x 转入长期支持阶段，并将持续获得更新至 2029 年 4 月底。
- 📝 相比 Node.js 26.12.1 没有进一步代码变更，仅更新了 `process.release` 等 LTS 元数据。
- ⚠️ 从 Node.js 24、22 或更早的 LTS 版本升级时需注意：自 Node.js 25 起，Linux 官方二进制文件链接了 `libatomic`，部分 Linux 发行版可能需要单独安装。
- 💻 提供 Windows 64 位/ARM64、macOS Intel/Apple Silicon、Linux 多架构、AIX 等平台的安装包或二进制文件，以及源代码和文档。
- 🔐 发布文件包含 SHASUMS 校验值和 PGP 签名，可用于验证下载文件的完整性与来源。

---

### [Bun v1.4.4 | Bun 博客](https://bun.com/blog/bun-v1.4.4)

**原文标题**: [Bun v1.4.4 | Bun Blog](https://bun.com/blog/bun-v1.4.4)

概述摘要：Bun v1.4.4 是一次覆盖工具链、包管理器、数据库、WebSocket、运行时和兼容性修复的大型更新，重点包括内置极速格式化器 `bun fmt`、`bun check` 与 `bun install` 的显著提速，以及 `Bun.SQL`、`ws` 兼容层和 JavaScriptCore 升级。

- 🚀 Bun v1.4.4 发布，核心亮点是新增内置格式化器 `bun fmt`，兼容 Prettier/oxfmt 配置，并支持 JS、TS、CSS、HTML、Vue、Svelte、Markdown、YAML、TOML 等多种语言。
- ⚡ `bun fmt` 性能极强：在 Prettier 仓库中约 60ms 完成检查，而 Prettier 约 17 秒，官方称快约 286 倍；对 oxfmt 项目也快 3x 到 6x。
- 🧹 `bun fmt` 支持 `--check`、`--staged`、`--changed`、`--init`、`--doctor`，并内置导入排序、Tailwind、`package.json` 和 Svelte 插件能力。
- ✅ `bun check` 在大型项目上快 1.4x 到 7.8x，`bun check -b` 在多项目 monorepo 中最高快约 15x，并降低内存占用。
- 📦 `bun install` 可迁移 Yarn Berry `yarn.lock` 到 `bun.lock`，保留 workspace、alias、resolution、git/tarball/file 依赖和 patch 依赖。
- 🔁 安装请求支持指数退避重试，尊重 `Retry-After`，并重试 429/408；还新增 `bun pm fetch`、缓存打包/解包/清理、递归发布和 `packageExtensions`。
- 🧩 依赖解析更接近 pnpm：peer dependency 会选择满足范围的版本，Linux 安装会按 libc 跳过不匹配的原生包，并新增 `link:` 路径支持。
- 🛠️ 包管理命令更严格：支持 npm/Yarn/pnpm 常见 flag 映射，拒绝未知 flag，新增 `--env-file`、`bunx --cwd`、`bunx --trust` 等。
- 🗄️ `Bun.SQL` 与 `bun:sqlite` 大幅重构：查询 CPU 最多降低 48%，新增 PostgreSQL `query.cancel()`、`COPY` 流、列名转换、数组参数、`sql.json()`、连接复用和 SQLite 自定义函数/更新钩子。
- 🔌 `ws` 在 Bun 中更接近 npm 包行为：通过 `ws` 8.22.0 测试更多用例，支持 `createWebSocketStream()`、agent、handshakeTimeout、maxPayload、压缩和 Node.js 风格事件。
- 🌐 WebSocket 关闭语义更符合浏览器/Node.js：失败连接先触发 `error` 再以 1006 `close`，并新增 `ws.pause()`/`resume()`、`websocket.error` 接收 socket、`proxy.tls` 独立配置。
- ⚙️ 运行时升级 JavaScriptCore，包含 1,013 个 WebKit 提交；`toLocaleString()` 等场景最高快 54x，`Bun.Glob` 新增 extglob 和 brace range。
- 📈 性能改进还包括 `Headers` 迭代最高快 2.8x、内存响应体流式读取最高快 2.6x、`Bun.JSON5.parse()`、`Bun.Glob.match()`、哈希和加密相关 API 提速。
- 🖥️ 开发服务器错误覆盖层重新设计，支持错误分组、滚动、浅色主题，并减少重复构建错误展示。
- 🔐 该版本包含 TLS、WebSocket、数据库客户端和包管理器的安全修复，同时大量修复 Node.js 兼容性、`bun test` 覆盖率、打包器、Shell、Windows 和 TypeScript 类型问题。

---

### [GitHub - swc-project/swc-next：](https://github.com/swc-project/swc-next)

**原文标题**: [GitHub - swc-project/swc-next: A new Rust-based platform for the Web · GitHub](https://github.com/swc-project/swc-next)

SWC Next 是一个用 Rust 编写的快速 JavaScript/TypeScript 工具链，也是对 SWC 的从零重写；它采用扁平的、基于 ESTree 的 AST，重点提升性能与可扩展性。

- 🚀 性能表现：在原生解析器基准中最高比 SWC 快 3 倍，在 JavaScript API 基准中最高快 10 倍。
- 🧩 JavaScript 扩展性：支持 Rust 与 JavaScript 之间快速往返 AST，从而可用 JavaScript 编写插件。
- ✅ 正确性保障：针对 Test262、TypeScript 和 Babel 进行测试，并补充额外单元测试。
- ⚠️ Rust API 状态：仍处于非常早期阶段，生产环境建议继续使用 SWC 的 Rust API。
- 📦 JavaScript API：通过 `@swc-next/core` 使用，安装命令为 `npm install @swc-next/core`，示例中用 `parseSync` 解析、用 `printSync` 打印代码。
- 🗺️ 路线图：项目在独立仓库开发并发布独立包，逐步对齐 SWC 能力，长期目标是成为 SWC 下一主版本并合并回 SWC 仓库。
- 🏗️ 架构设计：采用“扁平化 AST”设计；当前 Rust AST API 存在已知健全性问题，节点 ID 和类型句柄未绑定所属 `Ast`，跨 AST 使用可能导致未定义行为。
- 🔄 兼容性：计划支持部分 `.swcrc` 选项，但 Rust/JavaScript API 不与 SWC 兼容，配置兼容尚未实现。
- 🙏 致谢与许可：借鉴 Yuku、Zig/rowan、Oxc、esbuild 等项目；自有代码采用 Apache-2.0 许可，第三方代码和数据保留上游许可。
- 📊 仓库概况：该项目公开仓库约有 61 stars、5 forks、3 watchers、105 issues、17 PR 和 812 commits。

---

### [Reylo — 将 .sql 文件导入 TypeScript，完全类型化](https://reylo.dev/)

**原文标题**: [Reylo — Import .sql files into TypeScript, fully typed](https://reylo.dev/)

Reylo 让 TypeScript 可以直接导入 `.sql` 文件，并从正在运行的开发数据库中获得完整的参数、列、可空性、行数与 JSON 结构类型推断；核心依赖 TypeScript 7.1 的 content mappers，无需 codegen 或 watcher。

- 🧩 通过 TypeScript 7.1 content mappers 导入 `.sql`，类型检查器会调用 Reylo 返回模块类型。
- 🎯 类型来自实时开发数据库：数据库只 prepare 查询而不执行，Reylo 读取 catalog 获取参数与结果类型。
- 🗄️ 支持 Postgres、MySQL、SQLite，并覆盖 Neon、PGlite、PlanetScale、Cloudflare D1、Turso、libSQL 等环境。
- 🔌 不自带数据库驱动，可配合 `pg`、`postgres.js`、`mysql2`、`better-sqlite3`、Drizzle 等使用。
- ⚙️ 安装需要 TypeScript 7.1 beta、Node 24+，以及 `reylo` 和对应数据库的 `@reylosql/*` 包。
- 📦 在 `tsconfig.json` 中为 `.sql`、`.reylo.yaml`、`.reylo.yml` 配置 content mapper。
- ✅ 使用 `tsc --noEmit --runExternalCode` 进行类型检查；Next.js 需先运行 `next typegen`。
- 🚀 运行时通过 preload 或插件加载 `.sql`，支持 Node、Bun、Vite、Next.js、esbuild、webpack、Rspack、Jest、Cloudflare Workers。
- 🔧 `.reylo.yaml` 可配置 `direct_url`、`.env` 文件、`strict_params` 和 `sqlcommenter`。
- 🧠 可推断参数类型、列类型、NULL 可空性、唯一键基数、聚合、子查询、`returning`、枚举和嵌套 JSON。
- 🛡️ 查询由数据库校验，列名拼错等错误会定位到 `.sql` 文件的行列，并同时暴露给 `tsc` 和编辑器。
- 🧾 支持 JSON Schema 类型推断与运行时校验，包括嵌套对象、数组、`oneOf` 判别联合。
- 🧮 类型映射统一：64 位整数为 `bigint`，decimal 为精确字符串，日期时间为 UTC ISO 字符串，不使用 `Date`。
- 🧰 主要 API 包括 `.run(db, params)`、`.try()`、`.trySync()`、`.runSync()`、`.with(db)`，以及 `.sql`、`.raw`、`.source`。
- 🧭 编辑器需使用 TypeScript 7 扩展并指向项目内 TypeScript；悬停可看类型、SQL 和文件注释。
- 📈 可通过 Node tracing channel `reylo:query` 为查询添加可观测性。
- 🤖 提供 agent skill：`npx skills add colinhacks/reylo --skill using-reylo`，便于编码代理编写查询。
- ⚠️ 限制：类型检查和构建需要实时数据库；Reylo 不执行迁移；`.reylo/` 是缓存且不应提交。

---

### [GitHub - colinhacks/motherload：从 TypeScript 导入数据文件，完全类型化](https://github.com/colinhacks/motherload)

**原文标题**: [GitHub - colinhacks/motherload: Import data files from TypeScript, fully typed. Powered by TypeScript 7.1 content mappers. · GitHub](https://github.com/colinhacks/motherload)

Motherload 是 colinhacks 开发的 TypeScript 数据文件加载器，利用 TypeScript 7.1 的 content mappers 将多种数据文件导入为完全静态类型的模块，并原生集成 `tsc`；文件在构建时解析，bundle 中只保留数据而不包含解析器。

- 📦 支持 TOML、YAML/YML、JSONC、JSON5、CSV、TSV、Markdown、纯文本和 `.env`，提供统一 content mapper，也可按需单独使用。
- ⚙️ 需要 TypeScript 7.1 beta 或更高版本，以及 Node 24+、Bun 或 nub；通过 npm 安装 `motherload` 和 `typescript@beta`。
- 🧩 在 `tsconfig.json` 的 `contentMappers` 中声明 Motherload 及其扩展名，并使用 `tsc --noEmit --runExternalCode` 进行类型检查。
- 🚀 运行时集成：Node 使用 `--import motherload/register`；Bun/nub 配置 preload；Vite、Vitest、Rollup、Rolldown、esbuild、webpack、Rspack、Next.js、Jest 均有对应插件或加载器。
- 🧠 默认导出按 `as const` 推导类型；TOML 的字面量、YAML 多文档、JSONC 注释与尾逗号、JSON5 等均可获得精确静态类型。
- 📊 CSV/TSV 由表头定义列名，所有值按字符串处理，导入结果为带只读字段的数组类型。
- 📝 Markdown 默认导出正文与 frontmatter，并支持分别命名导出；`.txt` 直接导出字符串。
- 🔐 导入 `.env` 会把变量写入 `process.env` 并类型化为 `string`；已有环境变量优先；bundle 不包含 `.env` 值，运行时需用 `--env-file` 提供。
- ❌ 无效数据会在编译期报类型错误并定位到行列；缺失文件会导致类型检查或构建失败，可用 `strict: false` 放宽副作用导入检查。
- 🛠️ VS Code/Cursor 需安装 TypeScript 7 扩展并指向项目内的 TypeScript；Zed 需额外配置。

---

### [博客 | pnpm](https://pnpm.io/blog?type=releases)

**原文标题**: [Blog | pnpm](https://pnpm.io/blog?type=releases)

本文汇总了 pnpm 在 2026 年 10 月 10 日至 10 月 27 日期间发布的多个版本更新，主要涉及安装与打包问题修复、安全漏洞修补，以及新增环境文件、OIDC 认证、远程缓存、配置依赖管理等能力。

- 🛠️ 12.16.1（2026-10-27）：修复在安装 Cargo crate 的工作区中，冷存储导致 `pnpm install` 挂起的问题；修复 `pnpm pack` 仍打包被 `files` 按名称排除的文件的问题。
- 🔐 12.16.0（2026-10-27）：新增全局 `--env-file` 参数，支持符号链接的 `pnpm-lock.yaml` 和 `pnpm setup --no-modify-path`；修复 zstd 解压与签名相关的两个安全问题。
- ⚠️ 11.28.9（2026-10-27）：修复 registry 响应内容编码过多时的崩溃（GHSA-xjj6-f33q-929c）；按容器 CPU 配额设置安装 worker 池大小；重复执行 `pnpm install` 可应用更多设置变更。
- 📌 11.28.8（2026-10-22）：该版本未提供具体更新说明。
- 🧩 12.15.0（2026-10-21）：支持 `pnpm-workspace.yaml` 通过 `include` 委派设置及配置依赖；新增 `lockfile.integrityTarget: tar` 与 tar-registry 支持；接受 zstd 压缩的 registry 响应；在 `pnpm deploy` 和 `pnpm install` 中遵循 `SOURCE_DATE_EPOCH`；拒绝包名不一致的 registry 元数据；加速工作区安装与 macOS 文件链接。
- ⚙️ 12.14.0（2026-10-15）：新增 `sideEffectsCache.exclude` 设置；`pnpm install` 不再等待每日更新检查；输出读取端退出时不再导致 pnpm 核心转储中止。
- 🛡️ 11.28.6（2026-10-15）：`pnpm publish` 不再向非签发目标 registry 发送 CI 身份令牌；修复安装时丢弃同时声明为 optional peer 的依赖；重新接受空的 `httpProxy` 和 `httpsProxy` 设置。
- 🧰 12.13.0（2026-10-13）：新增 `pnpm profile` 和 `pnpm token` 命令；新增 `storeIndexFormat: files`，用于网络文件系统共享存储；提升 Python 依赖解析速度。
- 🔑 12.12.1（2026-10-11）：`pnpm dist-tag` 支持 OIDC 认证，新增 `tool:` 协议；`pnpm publish` 使用 `NPM_ID_TOKEN` 前会检查其签发 registry。
- 🚀 12.12.0（2026-10-10）：通过远程缓存共享任务结果与依赖构建；新增 `addMissingPeerTypes` 设置；支持 `pnpm add --config` 和 `pnpm update` 管理配置依赖；修复 `dangerouslyAllowAllBuilds` 执行被 `allowBuilds` 拒绝的包构建脚本的问题。

---

### [Biome v2.6——支持新语言、JavaScript 插件、更好的 Tailwind 集成以及 biome inspect 命令 | Biome](https://biomejs.dev/blog/biome-v2-6/)

**原文标题**: [Biome v2.6—Support for new languages, JavaScript plugins, better Tailwind integration and the biome inspect command | Biome](https://biomejs.dev/blog/biome-v2-6/)

Biome v2.6 是一次覆盖新语言支持、插件生态、Tailwind 集成、调试工具和底层架构的重要更新：新增 Markdown、SCSS、YAML 支持，推出 JavaScript 插件开发者预览，强化 Tailwind v4 类名排序与相关规则，并带来 `biome inspect`、Stylelint 迁移、59 条规则转正及基于 salsa 的新架构。

- 📝 新增 Markdown 支持：解析器 100% 符合 CommonMark，格式化器约 92% 兼容 Prettier，默认支持 GFM 任务列表、表格和短链接，可配置 frontmatter 及 HTML/代码块嵌入的格式化与分析。
- 🎨 新增 SCSS 支持：官方测试套件兼容性超过 90%，格式化开箱即用，现有 CSS lint 规则可作用于 SCSS；涉及循环、mixin 等结构的部分规则仍有局限。
- 📦 新增 YAML 支持：解析器 100% 通过官方测试套件，格式化器 100% 兼容 Prettier；当前仅有一条 YAML lint 规则，后续将增加 GitHub Workflows 等规则。
- 🔌 JavaScript 插件开发者预览：可编写自定义 lint 规则，支持 `.js`/`.ts` 文件，基于 CST 和错误恢复解析；插件可接入 Rust 基础设施，底层使用 boa 运行时。
- 📦 插件分发升级：可通过 npm 包和 `biome-manifest.json` 同时分发配置、GritQL/JavaScript 插件与规则预设；新增 `resolutionKind`，便于按共享配置目录解析插件。
- 🌬️ Tailwind 集成增强：`useTailwindSortedClasses` 采用 Tailwind v4 排序语义并读取设计系统样式表，新增 `noTailwindRawColors`、`noTailwindRestyledComponents`、`useTailwindStaticClassStrings` 等规则。
- 🧭 Tailwind 类名检测统一：JSX、TSX、HTML、Vue、Svelte、Astro 采用一致检测方式，可通过 `tailwind` 配置 `mergeFunctions`、`variantFunctions`、`attributes`。
- 🔍 新增 `biome inspect` 命令：`inspect config` 可解析 `extends`、`overrides`、monorepo 配置并支持点号访问；`inspect plugins` 列出插件规则；`inspect file` 展示 CST、IR、语义模型等调试信息。
- 🔁 配置与迁移：支持递归继承配置和插件，最多 10 层；新增 `biome migrate stylelint --write`，可迁移 JSON/JavaScript 格式的 Stylelint 配置及忽略规则。
- ✅ 规则与安装：59 条 nursery 规则转正，覆盖 correctness、suspicious、security、performance、complexity、style 等组；新增独立安装脚本，支持 Linux/macOS/Windows。
- ⚙️ 新架构与类型推断：采用 salsa 实现按需增量计算、缓存与取消机制，提升 CLI/LSP 响应；重写类型推断引擎，新增 `--profile-type-inference` 性能分析。
- 🤝 社区参与：可通过测试预览版、翻译文档、加入 Discord、贡献代码/规则/LSP/编辑器扩展，或通过 Open Collective/GitHub Sponsors 资助项目。

---

### [面向开发者的 Firefox 159 发行说明（稳定版） - Mozilla | MDN](https://developer.mozilla.org/en-US/docs/Mozilla/Firefox/Releases/159)

**原文标题**: [Firefox 159 release notes for developers (Stable) - Mozilla | MDN](https://developer.mozilla.org/en-US/docs/Mozilla/Firefox/Releases/159)

Firefox 159 于 2026 年 10 月 27 日发布，主要面向开发者更新了 CSS 滚动驱动动画、WebGL 扩展、DOM 作用域自定义元素注册表、HTML Sanitizer API 行为及 WebDriver 一致性等功能；HTML 与 JavaScript 无重大变化。

- 🎞️ CSS 滚动驱动动画默认启用，可基于滚动时间线而非文档时间线驱动属性动画。
- 🧱 移除旧版 masonry 布局语法，包括 `masonry` 值和 `masonry-auto-flow` 属性，改由 grid lanes 布局替代。
- 🧼 HTML Sanitizer API 相关方法在解析标记时即移除不需要的元素和属性，相邻文本会合并为单个文本节点。
- 🎮 WebGL 新增 `EXT_clip_control` 扩展，可调整裁剪空间到窗口坐标的映射，并支持 0 到 1 深度范围以提升深度精度。
- 🪞 WebGL 新增 `EXT_texture_mirror_clamp_to_edge` 扩展，支持镜像钳制到边缘的纹理环绕模式。
- 🧬 WebGL 2 在支持 16 位归一化格式的设备上默认启用 `EXT_texture_norm16`，提升高程图、医学图像等数据精度。
- 🧩 DOM 支持作用域自定义元素注册表，使 Shadow Tree 可拥有独立 `CustomElementRegistry`，避免组件元素名冲突。
- ⚙️ WebDriver 推荐首选项改为默认值，避免非正常关闭后残留在 `prefs.js`。
- 🚫 移除 `--remote-allow-system-access` 命令行参数，改用环境变量 `MOZ_REMOTE_ALLOW_SYSTEM_ACCESS=1` 开启系统访问。
- 🐛 修复超时后内部轮询持续运行至关闭导致的内存泄漏，可能影响 WebDriver BiDi 的 `browsingContext.traverseHistory` 等命令。
- 🧪 WebDriver BiDi 实现 `emulation.setMediaFeaturesOverride`，目前仅支持覆盖 `prefers-color-scheme`。
- 📄 为 Firefox 特有的 WebDriver BiDi 扩展新增机器可读 CDDL 文件。
- 🧰 实验性功能：CSS 数值工厂函数（如 `CSS.px()`）可在 workers 和 paint worklets 中使用，需相关首选项启用。
- 🔗 实验性功能：`MathMLAnchorElement` 新增 `download`、`ping`、`rel`、`relList` 和 `referrerPolicy` 属性。

---

### [博客 | WebKit](https://webkit.org/blog/)

**原文标题**: [  Blog | WebKit](https://webkit.org/blog/)

该页面汇总了 WebKit 与 Safari 的最新动态，涵盖 Safari 27.x 功能更新、多个 Safari Technology Preview 版本发布、隐私防跟踪进展、Interop 2027 提案征集，以及 Top-Level Await 修复等内容，并显示文章列表共有 53 页。

- 🚀 Safari 27.2 已发布，改进了 Customizable Select，重命名了 Grid Lanes 属性，并带来 20 项修复，涉及无障碍、媒体、CSS 等。
- 📱 Safari 27.1 随 iPhone Duo 推出。
- 🧪 Safari Technology Preview 250–255 均已发布，可在 macOS Golden Gate 和 macOS Tahoe 下载。
- 🛡️ Apple 与 WebKit 推出了针对“身份解析基础设施”的阻止措施，延续其长期网络跟踪防护。
- 📜 Safari 27.0 的发布说明篇幅创下该版本系列新高。
- 🧩 Safari 27 为顶层 await 增加了完整规范符合性，修复了 Safari 中的 Top-Level Await。
- 💡 WebKit 正在征集 Interop 2027 提案。
- 📄 文章列表当前为第 1 页，共 53 页，并提供下一页导航。

---

### [发布 remix v3.1.0 · remix-run/remix · GitHub](https://github.com/remix-run/remix/releases/tag/remix%403.1.0)

**原文标题**: [Release remix v3.1.0 · remix-run/remix · GitHub](https://github.com/remix-run/remix/releases/tag/remix%403.1.0)

Remix 3.1.0 已发布，重点提升服务端渲染性能与内存效率，并带来更灵活的组件混入、frame 重载/预取、焦点控制、S3 流式上传及面向未来的流式表单解析 API，同时修复 HMR 缓存问题并更新依赖。

- 🚀 发布 `remix@3.1.0`，包含 16 个提交，主要围绕性能、开发体验和流式处理。
- ⚡ `remix/component` 服务端渲染约快 2 倍且更省内存；48 商品列表 `renderToString()` 从 513µs 降至 244µs，持续负载下内存从 793MiB 降至 527MiB。
- 🧩 新增 `createMixin(setup, { ssr: false })`，可让 mixin 跳过服务端 setup/render，同时保留浏览器行为和 hydration；默认仍开启 SSR。
- 🔄 新增 `frame.reload({ src, method, encType, body })`，可重载其他来源或提交数据并渲染响应，且不改变浏览器历史。
- ⏱️ 支持 `data-rmx-prefetch="intent"`、`"viewport"` 和命令式 `prefetch()` 预取 frame HTML/资源，并尊重 Save-Data、跳过慢速连接。
- 🎯 可通过 `resetFocus: 'manual'` 或 `data-rmx-reset-focus="manual"` 关闭拦截导航时的自动焦点重置；滚动/焦点控制支持 Navigation API 的 `"after-transition"` 与 `"manual"`。
- 📦 `remix/file-storage/s3` 的 `storage.set()` 改为 S3 分片流式上传，大文件无需全部载入内存，并新增 `partSize` 选项。
- 🌊 新增 `remix/multipart-parser/future`、`remix/form-data-parser/future`、`remix/middleware/form-data/future`，流式解析上传；100MiB 上传解析从 68ms 降至 37ms，峰值内存增量从 396MiB 降至 29MiB；未来 API 尚不稳定，官方鼓励反馈。
- 🧾 `remix/*` 入口现在保留底层包默认导出，如 `remix/assert` 的可调用断言助手和 `remix/headers` 的 `SuperHeaders`；并新增对应 `package.json` exports。
- 🛠️ 修复 HMR 后客户端入口的缓存破坏 URL，补充 `unsafeHTML()` 错误提示，并升级多项 `@remix-run/*` 依赖。

---

