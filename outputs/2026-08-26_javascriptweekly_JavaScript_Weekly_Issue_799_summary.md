### [Bun 1.4 | Bun 博客](https://bun.com/blog/bun-v1.4)

**原文标题**: [Bun 1.4 | Bun Blog](https://bun.com/blog/bun-v1.4)

overview summary：Bun 1.4 是一次重大发布，重点提升了 Node.js 兼容性（新增 1,517 个测试通过）、大幅优化的性能（CPU、内存、启动速度）、从 Zig 到 Rust 的重写，并带来大量新内置 API、包管理器改进、测试工具增强及安全加固。

- 📊 **Node.js 兼容性大幅提升**：新增 1,517 个测试，`node:events`、`node:sqlite` 达 100%，`node:quic` 达 99%，修复了超 2,900 个问题。
- ⚡ **显著性能优化**：空闲 CPU 使用率降低 5 倍，内存使用量最高减少 35%，Linux 启动速度提升 50%，二进制体积缩小 17%。
- 🦀 **核心从 Zig 重写为 Rust**：这是首个基于 Rust 的版本，为未来架构演进奠定基础。
- 🖼️ **新增多个内置 API**：`Bun.Image`（图像处理）、`Bun.WebView`（无头浏览器）、`Bun.markdown`、`Bun.cron()`、`Bun.Terminal`（PTY），无需额外依赖。
- 🚀 **CLI 新命令**：支持 `bun run --parallel`、`bun test --parallel`、`bun audit fix`、`bun dedupe`、`bun prune`，提升开发效率。
- 📦 **流处理性能卓越**：原生 `ReadableStream` 等实现，压缩/解压与管道吞吐大幅超越 Node.js、Deno，并改进背压控制与 `Response.clone()` 内存效率。
- 🔍 **更强的可观测性**：新增 `--cpu-prof`、`--heap-prof` 及 Markdown 报告（`--cpu-prof-md`、`--heap-prof-md`、`--metafile-md`），便于分析性能。
- 🔒 **全面安全加固**：多项 TLS 证书校验、请求解析、tarball 提取等安全修复，建议所有用户升级。
- 🖥️ **扩展平台支持**：新增官方 FreeBSD、Windows ARM64 构建，以及实验性 Android 构建。
- 🧪 **测试工具增强**：`--parallel`、`--isolate`、`--shard`、`--timings`、`--changed`、`--retry` 等，且兼容 `jest.useFakeTimers()`。
- 🏗️ **构建工具改进**：内置 React Compiler（约 20 倍加速）、barrel 导入优化、TC39 装饰器支持、`--asset` 嵌入文件等。
- 🧩 **生态兼容性提升**：Playwright、Next.js 16、vitest、OpenTelemetry、Datadog 等工具均可在 Bun 上正常运行。
- 🔧 **包管理器优化**：`bun install` 速度大幅领先，全局虚拟存储使安装快 7 倍，并新增 `bun pm diff`、`bun pm licenses` 等命令。

---

### [](https://bun.com/blog/bun-in-rust)

**原文标题**: [Rewriting Bun in Rust | Bun Blog](https://bun.com/blog/bun-in-rust)

Bun 的创作者 Jarred Sumner 详细记录了如何借助 Anthropic 的 Claude 模型，在 11 天内将 Bun 运行时从 53 万行 Zig 代码重写为 Rust。原 Zig 版本因手动内存管理与 JS 垃圾回收混用而饱受内存泄漏和崩溃困扰；重写后，Rust 的借用检查器与 Drop 机制从语言层面杜绝了这类问题，并带来更低的 memory 占用、缩小约 20% 的二进制体积和 2%-5% 的性能提升。整个过程采用"1 个实现者 + 2 个对抗性评审"的 AI 工作流，并行运行 64 个 Claude，花费约 16.5 万美元 API 成本，完成了人工需 3 名工程师全职一年的工作量。

- 🚀 Bun 最初以 Zig 编写，源自 esbuild 转译器的逐行移植，现已月下载超 2200 万次，并被 Claude Code、Vercel 等广泛采用
- 🐛 Zig 的手动内存管理与 JS 引擎的垃圾回收混用，导致大量 use-after-free、double-free 和内存泄漏等稳定性问题
- 🔍 原有的 ASAN、模糊测试、泄漏测试等缓解手段只能事后发现问题，无法系统性预防
- ⚙️ Rust 因编译期强制检查借用与 Drop 自动清理，成为替代 Zig 的理想选择，优于依赖代码评审执行风格指南的 C++
- 🤖 作者用 Claude 的 pre-release 模型（Fable 5）执行机械式 Zig→Rust 移植，而非人工逐行重写
- 👥 采用"1 个实现者 + 2 个对抗性评审"的动态工作流，评审者只看 diff 并假设代码有错，成功在合并前捕获多个隐蔽 bug
- 📋 前期通过 PORTING.md（移植指南）和 LIFETIMES.tsv（生命周期表）确立规范，并先试移植 3 个文件验证可行性
- ⚡ 峰值时 64 个 Claude 并行工作，11 天产生 6,502 个提交，最快每分钟写入约 1,300 行代码
- 🔧 约 16,000 个编译错误被当作工作队列，按 crate 分发给 64 个 Claude 并行修复，并解决了循环依赖问题
- ✅ 6 个平台（Linux/macOS/Windows 的 x64 与 arm64）全部通过 Bun 完整测试套件（约 6 万测试、138 万断言）后合并
- 💰 总成本约 16.5 万美元 API 费用（59 亿输入 token、6.9 亿输出 token），人工估算需 3 名工程师全职一年
- 🐞 移植引入 19 个已知回归，如 debug_assert! 宏在 release 构建中吞掉副作用、Rust 保留边界检查导致 panic、comptime 格式化字符串语义差异等，均已被修复
- 📉 v1.4.0 修复了 128 个在 v1.3.14 可复现的 bug，并消除了所有可检测的内存泄漏（Bun.build 重复 2000 次的内存从 6.7GB 降至 609MB）
- 💾 二进制体积在 Linux 与 Windows 上缩小约 20%（Linux 从 88MB 降至 70MB），得益于减少 comptime 使用、ICU 优化与 ICF 链接优化
- ⚡ 性能提升 2%-5%：HTTP 吞吐（Bun.serve +4.8%、node:http +4.5%）、next build +4.5%、tsc +4.7%
- 🏭 Prisma Compute 与 Claude Code v2.1.181 已采用 Rust 版 Bun，启动速度提升 10%，且未出现原有内存问题
- 🔮 未来将持续减少 unsafe 代码（当前约 4%，78% 为单行 C/C++ 互操作），并借助 Miri、LeakSanitizer 和 24/7 覆盖引导模糊测试进一步提升稳定性

---

### [](https://www.youtube.com/watch?v=i38DgEuaJwM)

**原文标题**: [Bun v1.4 - YouTube](https://www.youtube.com/watch?v=i38DgEuaJwM)

YouTube 頁面提供網站導覽連結，涵蓋公司資訊、使用者支援、創作與廣告服務、法律條款及隱私安全等核心區域。

- ℹ️ 提供簡介與新聞中心，讓使用者了解 YouTube 最新動態
- 📞 提供版權申訴、聯絡方式及創作者支援管道
- 📢 說明刊登廣告與開發人員相關服務
- ⚖️ 列出條款、私隱及政策與安全規範
- 🔧 說明 YouTube 運作方式與測試新功能機制
- ©️ 顯示版權年份為 2026 Google LLC

---

### [Webflow 开发者平台](https://developers.webflow.com/?utm_source=cooperpress-newsletter&utm_medium=email&utm_campaign=fy27-cooperpress-newslettter&utm_content=javascript-weekly)

**原文标题**: [Webflow Developer Platform](https://developers.webflow.com/?utm_source=cooperpress-newsletter&utm_medium=email&utm_campaign=fy27-cooperpress-newslettter&utm_content=javascript-weekly)

Webflow 开发者平台为开发者提供了完整的工具链与基础设施，涵盖 API、CLI、MCP 2.0、代码组件、云部署、应用市场与集成。平台配套丰富的文档、博客、社区和客户成功案例，支持从开发、扩展到部署的全流程，并可通过 MCP 兼容客户端实现 AI 驱动的站点与内容管理。

- 🚀 **开发者工具链**：提供 REST API、SDKs、CLI、DevLink 和代码组件，支持从命令行到视觉画布的多样化开发方式。
- 🤖 **MCP 2.0 支持**：可通过 Claude、Cursor、Postman 等 MCP 客户端管理 CMS 内容、更新站点设置并触发部署。
- ☁️ **Webflow Cloud**：部署全栈 Web 应用，内置存储能力，统一站点与应用的工作区。
- 🔌 **应用与集成**：Marketplace 应用（如 HubSpot、Zapier、PayPal）及自定义集成（REST API、Webhooks、OAuth）轻松扩展工作流。
- 📚 **文档与指南**：覆盖快速入门、认证、CMS API、站点管理、自定义代码、Webhooks 等核心文档资源。
- 📰 **开发者资源**：技术博客、MCP 相关文章、每月开发者新闻通讯，持续提供产品更新与最佳实践。
- 👥 **社区与支持**：GitHub 开源项目、Reddit、Discord、Webflow 社区、Beta 测试以及大学课程和 YouTube 教程。
- 📈 **客户成果展示**：案例显示成本节省达 10 倍、开发工单减少 67%、流量同比增长 1170% 等显著成效。

---

### [面向程序员的音乐理论](https://runjs.app/blog/music-theory-for-programmers)

**原文标题**: [Music theory for programmers](https://runjs.app/blog/music-theory-for-programmers)

该文本是 RunJS 网站的导航菜单，列出了用户可以访问的主要页面入口，帮助用户快速找到所需功能。

- 🧭 展示 RunJS 的顶部导航栏，方便用户浏览网站各板块
- 💰 包含“定价”入口，可查看产品价格方案
- 📚 设有“文档”链接，提供使用说明和开发资料
- ✍️ 提供“博客”栏目，用于发布更新和文章
- 📬 给出“联系”方式，便于用户沟通反馈
- ⬇️ 配有“下载”按钮，用于获取软件安装包

---

### [未找到标题](https://www.solidjs.com/blog/solid-2-0-rc-the-big-reveal)

**原文标题**: [No title found](https://www.solidjs.com/blog/solid-2-0-rc-the-big-reveal)

您尚未提供需要总结的文章内容，请重新发送文本，我会按照模板生成中文概述和要点。

---

### [](https://nextjs.org/blog/building-app-like-experiences-with-nextjs-16-3)

**原文标题**: [Building App-like Experiences with Next.js 16.3 | Next.js](https://nextjs.org/blog/building-app-like-experiences-with-nextjs-16-3)

Next.js 16.3 通过 Instant Navigations（由 Cache Components 和 Partial Prefetching 驱动）实现了类 SPA 的即时响应体验，同时保留 Server Components 的收益。文章结合四个演示应用（音乐播放器 Next Beats、社交源 Drop、日历 Flow、团队聊天 Huddle）展示了核心功能：路由缓存与预取、URL 级预取、客户端交互、变更后缓存失效、断网重试、Suspense 流式渲染、乐观更新、复杂应用组合、客户端数据获取、View Transitions 动画，并提供了开源示例与测试工具。

- ⚡ Instant Navigations 通过 Cache Components 提供立即可显示的 UI 外壳，搭配 Partial Prefetching 在点击前预取可见 Link，使页面切换如 SPA 般即时，但仍由服务端渲染。
- 🗂️ 使用 `'use cache'` 标记数据读取，结合 `cacheLife` 和 `cacheTag` 实现跨导航缓存复用与按标签失效，浏览器也会缓存访问过的路由负载，加快重访速度。
- 🔗 为特定 `<Link>` 设置 `prefetch={true}` 可提前解析 `params`、`searchParams` 或完整 URL，使依赖 URL 的 `'use cache'` 数据也能在点击前就绪，但需权衡额外请求。
- 🖱️ Client Components 作为交互孤岛，通过 `'use client'` 标记，配合 Context Provider 在共享布局中维持播放器状态等跨路由交互，同时不把整个应用移入浏览器。
- 🔄 在 Server Action 中调用 `updateTag` 使缓存标签失效，配合 Partial Prefetching 可在导航前获取最新数据，实现变更后跨页面即时同步。
- 📡 实验性 `useOffline` 与 `experimental.useOffline` 配置支持断网时软导航、RSC 请求和 Server Action 自动重试，同时仍可渲染已预取的 App Shell，但生产环境不建议启用。
- 🎢 通过嵌套 Suspense 边界控制内容流式揭示顺序，避免布局偏移（CLS），嵌套边界按从上到下稳定呈现，且不阻塞并行数据加载。
- ⚙️ 使用 `useTransition` 与 `useOptimistic` 在 Server Action 进行中即时渲染乐观值，失败时自动回滚并显示错误提示，如收藏按钮的即时响应。
- 🧩 复杂应用可组合 Server Components 负责数据授权与渲染、Client Provider 管理交互状态，配合 `useActionState` 排序连续变更，`useOptimistic` 保持待处理状态可见。
- 📊 客户端数据获取库（SWR/React Query）可用于轮询、聚焦重验证、去重和请求协调；初始数据由 Server Component 预载并通过 SWRConfig/HydrationBoundary 传递，避免瀑布流。
- 🎬 React 的 `<ViewTransition>` 可动画化 Suspense 揭示（fade）、列表变更（morph）和路由切换（方向滑动），通过 `transitionTypes` 和 CSS view-transition 类定义导航方向动画。
- 📦 提供四个开源演示应用（Next Beats、Drop、Flow、Huddle）及 Playwright 端到端测试，`instant()` 帮助将断言限定在预取 UI 上，方便探索和验证功能。

---

### [Node.js — Node.js Interactive 2026 活动回顾](https://nodejs.org/en/blog/events/nodejs-interactive-2026)

**原文标题**: [Node.js — Node.js Interactive 2026: A Recap](https://nodejs.org/en/blog/events/nodejs-interactive-2026)

2026 年 8 月 12–13 日，Node.js Interactive 重返亚特兰大，与 RenderATL 及 Atlanta Tech Week 同期举行。会议传递的核心信息是：Node.js 的未来不仅取决于 API 扩展，更依赖开源维护者、跨运行时标准、平台安全实践，以及文档与测试等基础设施。

- 🧑💻 开源基础设施仍由人驱动：OpenJS 基金会执行董事 Robin Bender Ginn 指出，Node.js、Express 等项目依赖小团队维护者，他们属于“缺失的中间层”，需要可持续的支持与认可。
- 🤝 生态协作依赖标准共识：Joe Sepi 讲解了 W3C、Ecma、OpenJS 等治理机构的分工；WinterCG 已转为 Ecma TC55（WinterTC），目标是定义服务器端 JavaScript 的最小通用 API，提升运行时互操作性。
- 🔐 供应链安全本质是身份安全：Shai-Hulud 与 Axios 维护者账户入侵事件均表明，攻击者通过攻陷人类身份获得合法发布权限；需采用可信发布、短时凭证、防钓鱼认证、依赖冷却等防御手段。
- 🤖 AI 是安全双刃剑：它让社工攻击和低质量漏洞报告更廉价（如 curl 结束金钱赏金），也能辅助防御（如 AI 驱动系统识别 OpenSSL 的 12 个漏洞，其中一些存在超 25 年）。
- 📦 可重现性需要超越版本号：Darcy Clarke 探讨了 SemVer 构建元数据作为向后兼容扩展点的潜力，并提出了开放规范 semver.xyz；语义化版本本身并不覆盖完整范围语法。
- 🏗️ AI 时代更需要平台思维：Fastly 的 Bekah Suttner Cheek 强调，快速 CI、有效测试、安全回滚、健康代码模式等护栏在开发提速时更加重要，平台应让安全操作成为默认路径。
- 🔋 Node.js 开箱能力显著增强：内置 TypeScript 类型剥离、node:test、.env 加载、fetch、watch 模式、node:sqlite 和权限模型等；从 27.x 起改为每年一次主版本发布，以减轻维护压力。
- 🌐 QUIC/HTTP/3 仍在推进：James Snell 介绍了 node:quic 的实验状态（需专用二进制和 --experimental-quic），未来或让 fetch 等网络栈受益，并计划提出统一 HTTP 服务器 API。
- 📚 文档与测试是基础设施：新 doc-kit 管线统一生成网页、man 页、JSON、搜索索引和 llms.txt，并重新设计 API 文档；@harperfast/integration-testing 则支持并行、真实的集成测试。
- 🎯 AI 改变工作流但不改变责任：多位讲者强调开发者仍须对系统负责，需关注输入、上下文、护栏、评估；MCP 与规范驱动开发提升可靠性，同时要警惕 AI 生成代码带来的性能回归，善用 INP、TTFB 等指标。
- 🎓 Code & Learn 收官：与会者与核心维护者结对，学习贡献流程并提交补丁，会议鼓励更多人通过贡献指南参与开源，延续社区协作精神。

---

### [TanStack AI 进入 RC 阶段 | TanStack 博客](https://tanstack.com/blog/tanstack-ai-rc)

**原文标题**: [TanStack AI Enters the RC Phase | TanStack Blog](https://tanstack.com/blog/tanstack-ai-rc)

overview summary
TanStack AI 正式进入 RC 阶段，经过一年的发展，从简单的 chat() 方法成长为支持多提供商、多模态、沙箱代理和可靠持久化的完整 AI 框架。其核心优势在于灵活的中间件架构、类型安全、传输层无锁定以及一致的 API 设计。团队正邀请社区参与测试，为稳定的 v1 版本做准备。

- 🎉 TanStack AI 进入发布候选阶段，提供商从 4 个增至 24 个，并采纳 AG-UI 协议，兼容多种编程语言与框架。
- 🧩 中间件系统是架构核心，可实现聊天持久化、沙箱代理、记忆、遥测、耐久性等功能，扩展性极强。
- ⚡ 提供懒工具调用（降低 token 成本）和高级中断场景（支持修改参数、多重中断），全程保持类型安全。
- 🔀 传输层灵活无锁定：支持 SSE、WebSockets、HTTP 流、Cap'n Web 及自定义适配器，客户端也可自定义连接适配器。
- 📐 API 设计注重一致性与最小化，图像、视频、音频生成及转录等媒体 API 几乎相同，学会一次即可复用。
- 🛡️ 类型安全为核心，提供大量编译时检查，如不支持的模型选项、缺少必填属性、不兼容的工具等都能提前报错。
- 💬 chat() 方法功能强大：支持持久化、耐久性、沙箱代理（如 Codex）、遥测、结构化输出、代码模式及 MCP。
- 🖼️ 媒体生成 API 是一等公民，支持实时音频、TTS、图像、视频、音乐生成与转录，覆盖 100+ 模型，可流式或一次性生成。
- 🧠 支持 embeddings、reranking（如 Cohere、OpenRouter）及主流厂商的代理记忆，为 RAG 和个性化对话提供基础。
- 📦 沙箱与代理框架提供商无关，可接入 Codex、Claude Code、Grok 等 20+ ACP 代理，也可构建自定义编码代理并持久化到 SQLite。
- 🔌 MCP 支持类型安全：内置 CLI 为远程 MCP 服务器生成类型，支持连接池和生命周期策略（关闭、保留或复用连接）。
- 💾 持久化设计出色：实现存储并通过对符合性测试后，约 20 行代码即可完成对话持久化，耐久性适配器可恢复中断的流。
- 👥 团队三人引以为傲：Jack 赞赏 API 的简洁与灵活性；Tom 强调类型安全与核心设计的优雅；Alem 则骄傲于架构的快速实现。
- 🚀 未来计划包括代理工作流与编排（并行代理、定时任务、复杂流程）、更多提供商支持，并欢迎社区贡献。
- 🙏 感谢合作伙伴（如 OpenRouter）和社区反馈，邀请大家测试 RC 版本，稳定版 v1 即将到来，旨在构建真正开源、无商业附加条件的 AI 框架。

---

### [](https://blog.master.dev/react-compiler-linting-just-got-a-rust-native-speedup-in-oxlint/)

**原文标题**: [React Compiler Linting Just Got a Rust-Native Speedup in Oxlint – Master.dev Blog](https://blog.master.dev/react-compiler-linting-just-got-a-rust-native-speedup-in-oxlint/)

Oxlint 现已为 React Compiler 提供 Rust 原生 lint 支持，大幅提升了检查速度，并发布 22 条由 React Compiler 驱动的规则；作者还分享了配置建议、性能对比，以及 Vite 构建环节的进展。

- 🚀 React Compiler 的 Rust 重写版本已发布，并成为官方标准实现。
- ⚛️ 作者长期使用 React Compiler，配合 `useEffectEvent` 与“You Might Not Need An Effect”实践，彻底摆脱手动 `useCallback`/`useMemo`。
- 🔧 作者已全面迁移到 Vite v8（Rolldown）与 oxc 生态：Rollup→Rolldown、ESLint→Oxlint、Prettier→oxfmt、Jest→Vitest。
- 🐢 之前 React Compiler lint 插件需经 Babel + Compiler 核心，导致 lint 任务耗时增加 3 倍以上。
- ⚠️ 作者强调：启用全部 React Compiler 规则是使用它的前提；否则 bailout 可能造成性能明显回退。
- 📉 他们曾因一次 bailout 导致首页动画占位符出现视觉故障。
- ⚡ Oxlint v1.70.0 在 Rust 中原生实现了 `react/react-compiler` 规则，不再需要 Babel 管线。
- ⏱️ 切换原生规则后，lint 从约 29.2s 降至 9.1s（3.2×），若不运行 JS 插件 perfectionist，则仅约 2.6s（11×）。
- 🎉 Oxlint v1.79.0 正式发布 22 条 React Compiler 驱动规则，用于捕获违反 Rules of React 的代码。
- 📋 推荐配置：开启 `correctness` 类别（覆盖 12 条），再显式启用其余 10 条规则。
- 🧩 Oxlint 规则是 `eslint-plugin-react-hooks` v7 规则的一个子集，但不含 `config`、`gating`、`fbt`、`memoized-effect-dependencies`。
- 🛠️ 构建侧进展：oxc 曾合并原生 transform 但因二进制增大 17% 而回滚；现推出实验性的 `oxc-transform-react`，速度约为原 Rust 移植版的 2 倍，并支持 source map。
- 🧪 作者已用 `oxc-transform-react` 自制 Vite 插件替代 `@rolldown/plugin-babel`，并在生产环境使用。
- 📦 采用 Oxlint 非常容易：安装 `oxlint` 即可，可用 `npx @oxlint/migrate` 从 ESLint 迁移，也可与 ESLint 并行运行。
- 💡 常见坑：在组件内重新赋值 props 会导致 React Compiler bailout；建议启用 `eslint/no-param-reassign` 并用重命名代替赋值。
- 🔒 作者始终将所有 React Compiler 规则设为 error，并总结：“React Compiler 不在 lint 所有 bailout 的情况下使用是不安全的。”
- 🎓 文末还推广了 React 学习课程（Master.dev 订阅可享 20% 折扣）。

---

### [](https://github.com/electron/electron/releases/tag/v44.0.0)

**原文标题**: [Release electron v44.0.0 · electron/electron · GitHub](https://github.com/electron/electron/releases/tag/v44.0.0)

Electron v44.0.0 正式发布，主要带来 Chromium 152、Node 24.18.1 与 V8 15.2 的升级，同时包含多项破坏性变更、新功能、问题修复及性能优化。

- 🚀 **核心升级**：Chromium 152.0.7977.54、Node v24.18.1、V8 15.2。
- ⚠️ **破坏性变更**：移除 Linux Unity 桌面支持；macOS 12 及以下不再受支持；停止发布 32 位构建（Windows ia32 / Linux armv7l）；ANGLE 改为静态链接，不再分发 libEGL/libGLESv2；clipboard 模块不再暴露给渲染进程；移除 macOS 12 相关的登录项旧字段等。
- ✨ **新增功能**：主进程新增 `net.WebSocket`（WHATWG 兼容）；支持 `select-client-certificate` 事件；新增跨平台窗口状态保存/恢复 API；Linux 无边框窗口默认改为圆角并支持系统主题标题栏图标；新增 `webFrameMain.printToPDF()`、`webContents` 缩放模式控制、macOS 通知移除等能力。
- 🛠️ **重要修复**：修复大量崩溃问题（如 DevTools 关闭、D-Bus 断开、ASAR 循环链接、进程退出时 TLS 相关崩溃等）；修复 DevTools 网络面板、`nativeImage` 颜色空间、Linux 无边框窗口尺寸与缩放、ASAR 内文件下载、沙箱预加载脚本缓存等问题。
- ⚡ **性能优化**：启用 ThinLTO 优化；通过嵌入式 Node.js 启动快照加快主进程启动；沙箱渲染器冷启动时间减少约 35%；Linux 发行版体积减少约 37 MB；优化 IPC、事件派发及预加载脚本加载等。
- 🔄 **其他变更**：更新 macOS Squirrel.Mac 自动更新后端；移植上游 Chromium/V8 修复；新增多项文档更新。

---

### [](https://waku.gg/blog/waku-v1-rc)

**原文标题**: [Waku 1.0 (RC) — Waku](https://waku.gg/blog/waku-v1-rc)

Waku 1.0 候选版（RC）正式发布，这是一个以 React 服务端组件为核心的最小化 React 框架，目前公共 API 已固定，并明确标记了所有不稳定 API。团队呼吁用户在最终版 v1 落地前提供反馈，同时本次更新带来了类型安全导航、即时导航、多项修复及破坏性变更。

- 🚀 发布 Waku 1.0-RC，公共 API 已稳定，所有不稳定 API 被明确标记，并开放最终反馈渠道（GitHub 讨论与 Discord）。
- 🧭 导航 API 全面支持类型安全：根据路由模式自动补全和校验参数，重命名路由或遗漏 slug 会在编译期报错，而非运行时 404。
- ⚡ 新增即时导航功能：缓存路由静态外壳，`<Link>` 可预加载，实验性 `unstable_instant` 能立即渲染外壳并流式加载动态部分。
- 🔧 其他改进：修复重定向、404、哈希目标与版本偏差问题，增加了 CSRF 源检查、服务端操作请求验证和可配置请求体限制。
- 🔀 `unstable_redirect` 现支持外部 http/https URL，可重定向到其他网站。
- 🧩 破坏性变更：请求上下文改为仅请求可用且位于路由器中，`unstable_getContext()` 和 `unstable_getContextData()` 已从 `waku/server` 移除，改用 `waku/router/server` 的新 API，并需自备 AsyncLocalStorage 处理上下文数据。
- 🛠️ 破坏性变更：Hono 中间件无法再读写 Waku 上下文，需通过 `createInterceptor` 注册处理器拦截器来运行渲染作用域内的代码（如注入每请求数据或 CSP nonce）。

---

### [](https://svelte.dev/blog/sveltekit-3-release-candidate)

**原文标题**: [The SvelteKit 3 Release Candidate is here](https://svelte.dev/blog/sveltekit-3-release-candidate)

SvelteKit 3 已进入候选发布阶段，主要清理代码并引入若干破坏性更新，为未来发展奠基。现有项目可通过迁移工具自动升级，新项目可直接创建。核心变化包括配置迁移至 Vite、别名调整、TypeScript 简化、Service Worker 重构、环境变量增强、错误处理改进以及基于 Vite 8 的性能提升，同时远程函数仍处于实验阶段。

- 🚀 SvelteKit 3 发布候选版，若无重大问题将很快稳定，不再有破坏性变更
- 🔄 使用 `npx sv@next migrate sveltekit-3` 自动迁移旧应用，新应用用 `npx sv@next create`
- ⚙️ 配置文件从 `svelte.config.js` 改为 `vite.config.ts`，集中管理
- 📁 `$lib` 别名改为 `#lib`，需按 Node 子路径导入规则带扩展名（如 `#lib/foo.ts`）
- 🔧 TypeScript 配置简化为扩展 `$app/tsconfig`，并需显式指定 `include`/`exclude`
- 👷 Service Worker 改用 `$app/env`、`$app/manifest` 等模块，不再是特殊 `$service-worker`
- 🔐 环境变量支持显式声明、类型安全、构建时/启动时解析，并可用 Standard Schema 验证
- 🛡️ 错误处理基于 Svelte 5 错误边界，所有错误（含 `error(...)`）都经过 `handleError`，且堆栈跟踪支持 sourcemap
- 🧭 浅路由改用 `goto` 的 `shallow: true` 选项，并支持 `persistState` 保留页面状态
- ⚡ 必须使用 Vite 8，受益于 Rolldown 构建加速和 Environment API，但不支持 FetchableDevEnvironment
- 🔮 远程函数作为实验性功能亮相，未来将改进客户端 - 服务器通信方式
- 📣 团队期待社区反馈和 bug 报告，以完善最终版本

---

### [](https://reactnative.dev/blog/2026/08/11/react-native-0.87)

**原文标题**: [React Native 0.87 - Strict TypeScript API, Metro Update, Swift Package Manager, AGP 9 Support · React Native](https://reactnative.dev/blog/2026/08/11/react-native-0.87)

React Native 0.87 正式发布，主要亮点包括：默认启用 Strict TypeScript API、Metro 性能大幅提升、实验性 Swift Package Manager 支持，以及对 Android Gradle Plugin 9 的支持。此版本同时提高了最低工具链要求，并引入多项破坏性变更与弃用调整，社区贡献者共 74 人，包含 265 个提交。

- 🚀 **Strict TypeScript API 成为默认**：类型由源码直接生成，更准确可靠；深度导入 `react-native/Libraries/*` 变为类型错误，可通过 `customConditions` 临时退回到 0.88。
- ⚡ **Metro 更新至 0.87**：源码映射生成快 2 倍，内存占用减半；稳定支持 TypeScript/ESM 配置文件，移除 `.es6` 和 YAML 配置支持。
- 🧪 **实验性 Swift Package Manager 支持**：可替代 CocoaPods，仅需 Xcode；使用 `npx react-native spm --deintegrate` 集成，但库需含 `Package.swift`，且暂不建议生产使用。
- 🤖 **支持 Android Gradle Plugin 9**：推荐在 `gradle.properties` 中设置 `android.builtInKotlin=false` 和 `android.newDsl=false` 以兼容现有构建。
- 🔧 **最低工具链要求提高**：Node.js ≥ 22.13，Kotlin 2.0+，compileSdk 最低 34（buildTools 已升至 37）。
- 🗑️ **移除多项 API**：包括 `InteractionManager`（改用 `requestIdleCallback`）、`Modal` 的 `animated` prop、`StatusBar` 部分 props、`useTurboModules` 标志等。
- 📦 **头文件引用变更**：原生代码中裸 include 需添加命名空间，例如 `#import <RCTAppDelegate.h>` 改为 `#import <React/RCTAppDelegate.h>`。
- ⏳ **弃用若干 API**：`InitializeCore`、`ImageBackground`、`NativeMethods`、`DrawerLayoutAndroid` 等均被标记为弃用，并给出替代方案。
- 🛠️ **工具链与包调整**：`@react-native/core-cli-utils` 不再发布，`rn-get-polyfills` 移除，需使用 `@react-native/js-polyfills`，并停止对独立 `react-devtools` WebSocket 连接的支持。
- 📈 **升级与支持**：0.87 为最新稳定版，0.84.x 停止支持；可使用 Upgrade Helper 或 `npx @react-native-community/cli@latest init` 创建新项目，Expo 用户可通过 `expo@canary` 获取。

---

### [](https://eslint.org/blog/2026/08/eslint-v10.9.0-released/)

**原文标题**: [ESLint v10.9.0 released - ESLint - Pluggable JavaScript Linter](https://eslint.org/blog/2026/08/eslint-v10.9.0-released/)

ESLint v10.9.0 是 ESLint 的次要版本升级，新增若干功能并修复多个缺陷，重点为 `no-unmodified-loop-condition` 规则新增 `checkConditionalExpressions` 选项。
- 🎉 发布 ESLint v10.9.0，带来新特性与多项修复
- ✨ 新增 `checkConditionalExpressions` 选项：启用后，循环中的三元表达式各分支会独立检查变量是否被修改
- 🐛 修复 `no-loss-of-precision` 在数值下溢时的处理问题
- 🔧 修复 `no-var` 自动修复在函数提升或 catch 参数遮蔽变量时可能产生不安全代码的问题
- 🛠️ 修复 `prefer-template` 自动修复错误生成带标签模板调用的问题
- 📝 文档更新：统一配置文件写法、更新架构文档、修复外部链接等
- 🔄 维护：更新依赖、GitHub Actions 及生态插件

---

### [](https://eslint.org/blog/2026/08/eslint-v10.9.1-released/)

**原文标题**: [ESLint v10.9.1 released - ESLint - Pluggable JavaScript Linter](https://eslint.org/blog/2026/08/eslint-v10.9.1-released/)

概述：ESLint v10.9.1 是补丁版本，主要修复了上一版本中 `no-loss-of-precision` 规则的误报问题，并更新了文档和生态插件。

- 🔧 修复 `no-loss-of-precision` 规则对尾随小数点的误报问题（#21251）
- 📄 为已停止维护的包版本补充弃用步骤说明（#21248）
- 🤖 更新生态系统插件依赖（#21249）
- 👥 发布人为 Milos Djermanovic，归属 ESLint TSC 成员
- 📅 发布于 2026 年 8 月 24 日，属于补丁版本升级

---

### [发布 v1.20.0 · axios/axios · GitHub](https://github.com/axios/axios/releases/tag/v1.20.0)

**原文标题**: [Release v1.20.0 · axios/axios · GitHub](https://github.com/axios/axios/releases/tag/v1.20.0)

axios v1.20.0 正式发布，重点强化了运行时选项的安全性，新增了 RFC 9110 状态码别名，修复了多个 Node.js 与 XHR 环境下的可靠性问题，同时更新了依赖、文档和赞助信息，并迎来了多位新贡献者。

- 🚀 发布概述：v1.20.0 主要聚焦运行时选项硬化、状态码别名补充、Node.js 和 XHR 可靠性修复，以及项目工具与文档的全面刷新。
- ⚠️ 破坏性变更：新增 ContentTooLarge (413) 和 UnprocessableContent (422) 状态命名，同时保留 PayloadTooLarge 和 UnprocessableEntity 作为向后兼容的弃用别名。
- 🔒 安全修复：加固运行时配置读取，抵御共享与外部原型污染，并规范化不安全的拦截器替换对象；同时明确 Fetch redirect、HTTP/2 DNS 与代理、CIDR 的 NO_PROXY 匹配、畸形 data URI 拒绝等行为。
- 🐛 拦截器生命周期：修剪被弹出的拦截器，防止处理器数组无限增长，同时保持迭代语义不变，并在公共 handlers 字段为空时确保操作安全。
- 🛡️ 错误处理修复：阻止自定义 Error.prepareStackTrace 返回非字符串值而覆盖原始请求错误；将无效 DNS 查找和 httpVersion 失败统一标准化为 AxiosError.ERR_BAD_OPTION_VALUE，并修正 timeoutErrorMessage 的合并策略。
- 🌐 XHR 可靠性提升：导航取消的请求现在以 ECONNABORTED 拒绝，而非错误解析为 status 0；成功下载也会在 loadend 事件分发时刷新最后一次进度回调。
- 🧠 内存与核心修复：移除了每个 socket 错误监听器对请求上下文的保留，避免 keep-alive socket 长时间固定已完成响应数据；同时防止 method-header 桶泄漏到传出请求头。
- 🔧 维护与文档更新：升级了 fast-uri、postcss、js-yaml、mocha 等多项依赖，补充缺失的 fs 导入示例，新增本地化全局搜索，并更新赞助链接与数据。
- 🌟 新贡献者：感谢 @yens1、@Sasireddy001、@ari-token-security 等 9 位新贡献者的帮助，完整变更见 v1.19.0...v1.20.0。

---

### [](https://pnpm.io/blog/releases/11.23)

**原文标题**: [pnpm 11.23 | pnpm](https://pnpm.io/blog/releases/11.23)

pnpm 11.23 版本发布，重点改进了 registries 配置结构，新增 virtualStoreType 选项，解决 ESM 下幽灵依赖解析问题，优化 pnpm config 输出，并包含多项修复与性能改进。

- 📦 `registries` 设置改为按 URL 声明一次，包含 `serverType`、`scopes`、`prefix` 等字段，支持 Artifactory 等私有仓库无需在锁文件中写入 tarball URL；旧格式仍兼容。
- 🔀 新增逐注册表的 `time` 字段支持，`resolutionMode: time-based` 仅对需要完整元数据的注册表获取大文档。
- 🗂️ 新增 `virtualStoreType` 设置（`global` 或 `project`），替代 `enableGlobalVirtualStore`，默认仍为 `project`。
- 🔧 全局虚拟存储下，ESM 导入的幽灵依赖现在可通过注入 `NODE_OPTIONS` 的 resolve hook 解析，无需插件；`extendNodePath: false` 可退出。
- 📋 `pnpm config get/list` 现在显示 pnpm 实际生效的设置，如合并后的 `registries`、`update`/`audit` 有效区段、完整 `catalogs` 等。
- ⚠️ 全局配置中不被当前版本识别的 key 会警告，并提示建议的正确名称；项目级 `pnpm-workspace.yaml` 中的未知 key 也不再静默忽略。
- 🔌 `importPackage` pnpmfile 钩子已弃用，未来将移除，并会降低安装并行度。
- 📁 读取已安装树时改用项目自身配置，不再依赖 `.modules.yaml` 中记录的旧注册表信息。
- 🔒 存储文件重新哈希时报告结果，耗时超过 1 秒或文件数超 1000 时显示具体原因。
- 🌐 pnpr 协议请求携带注册表声明结构，支持按 scope 路由到正确服务器；允许非白名单注册表在拉取时才校验，并传递更多客户端配置。
- 🩹 `pnpm audit` 会验证补丁版本是否存在，修正不存在的范围，`--fix` 不再写入无效覆盖；`--json` 中 `patched_versions` 为 `null` 表示无修复。
- 🧊 冻结安装不再重写 `packageManagerDependencies`，若锁文件与固定版本不匹配则报错，防止绕过 CI。
- 📌 `pnpm init` 写入 Corepack 接受的精确 pnpm 版本到 `packageManager` 字段。
- 🎯 `pnpm update <name>@<version>` 现在只更新指定包，不触碰其他依赖；间接依赖更新会明确报错。
- 🔗 非 npmjs 注册表的 tarball URL 若包含 `%2f` 编码，不再尝试重建，保留在锁文件中原样请求。
- ⏱️ `trustPolicy: no-downgrade` 在注册表缺失 `time` 字段且 `minimumReleaseAgeIgnoreMissingTime` 启用时不再报错，会跳过并警告。
- 📝 `pnpm add --allow-build` 合并现有 `allowBuilds` 而非覆盖；`approve-builds` 清理旧弃用字段。
- ⚙️ 多项修复：deploy 排除依赖组不再写入锁文件；overrides 不再写入元数据缓存；通配符排除规则修复；Windows 更新清理陈旧 ps1 文件；git 依赖保留 specifier；global update 不再误 404；runtime 匹配多平台架构；workspace 范围依赖安装更快；`pnpm set-script` 等命令修复。

---

### [](https://infrequently.org/2026/08/notes-on-performance-remediation-strategies/)

**原文标题**: [The Wicked Reason Removing Code Beats Better Scheduling - Infrequently Noted](https://infrequently.org/2026/08/notes-on-performance-remediation-strategies/)

这篇文章反驳了“调度资源比删除代码更容易优化性能”的观点，主张在大多数团队中，删除代码远比优化调度更持久、更可控。作者从组织协作、管理认知和技术风险等角度论证，调度优化容易造成系统脆弱、团队内耗甚至恶性循环，而控制代码体积才是改善性能的可靠根基。最后给出了务实的分步建议。

- 🧹 作者认为，删除代码与调度优化都需要深入理解页面行为，因此“调度更简单”的说法并不成立，两者基础成本相当。
- ⚠️ 重新排序资源的后果更难预测，被推迟的字节仍会占用主线程，可能给首屏带来隐性延迟，并产生难以排查的 INP 卡顿。
- 🔀 跨团队维护精心构造的加载顺序，需要极强的回归预防纪律，实际运营难度高于直接删除代码。
- 👥 调度优化会加剧协作复杂度，依据“布鲁克斯法则”，沟通成本最终会主导页面质量与团队交付形态。
- 📱 许多团队误判用户网络和设备条件（如“人人都有 5G”），基于错误假设的调度方案难以持久，而删除代码对用户群体变化更具韧性。
- 🎯 过度依赖调度会导致“用例过拟合”，使产品在面对多元用户与功能竞争时失去敏捷性，应优先考虑删代码和拆分体验。
- 🧑‍💼 从管理者视角看，依赖调度的系统显得脆弱且消耗资源；相同精力投入删代码，反而给团队更多余地和长期灵活性。
- 🕸️“预加载/延迟加载”在大型组织中极易引发团队间的恶性竞争，导致公共资源被挤占，核心体验被不断削弱。
- 📉 低管理成熟度的组织缺乏代码体积预算，误信“调度能救场”，最终陷入“越优化越臃肿”的恶性循环。
- ✂️ 一个“不讲道理但有效”的纠正方式是：清除所有预加载/延迟加载系统，暴露真实体积，强制削减，并立下“我们不做这种事”的规矩。
- 🍽️ 调度优化只能当作“特殊场合的菜”，仅适用于已具备严格体积预算、回归预防和发布门禁的成熟团队（至少达到成熟度四级）。
- 📚 删除代码能帮助团队理解系统组件间的交互，为未来真正有效的调度优化打下基础；体积缩小后，调度测试也更容易执行。
- 🛠️ 通用建议：尽可能削减发给客户的代码，包括“不干净”的代码；把工作移到服务器；只有当删减进入边际收益递减时，才考虑重排工作。
- 🧭 管理层面应推动关键用户旅程的明确化，并认真讨论“边缘用户”是谁——这类共识本身就能产生价值。
- ✅ 结论：从“糟糕”到“还行”的性能提升，本质是管理与文化问题；大多数团队应集中精力删代码，而非迷信调度。

---

### [](https://blog.gaborkoos.com/posts/2026-08-14-Your-Modules-Are-Lying-to-You/)

**原文标题**: [Your Modules Are Lying to You](https://blog.gaborkoos.com/posts/2026-08-14-Your-Modules-Are-Lying-to-You/)

概述：文章揭示 ESM 与 CommonJS 模块系统在绑定、执行顺序、循环依赖、跨模块加载及包发布中的深层差异，帮助开发者理解为何看似相同的导入代码行为不同，并给出实用调试与发布建议。

- 🔗 ESM 具名导入是“活绑定”，引用导出模块的变量本身，因此导入值会随导出方更新而变；CommonJS 解构则复制当前值，不会同步后续修改。
- ⚠️ ESM 导入的绑定对导入方只读，但导出对象内部属性仍可被修改；CommonJS 通过`module.exports`返回普通对象，解构复制属性，保留对象引用才能看到变更。
- ⏳ ESM 静态导入会先构建依赖图并按依赖顺序执行，即使导入语句写在后面也会先运行；CommonJS 的`require()`按代码执行顺序同步加载。
- 🧠 CommonJS 模块会缓存，多次`require()`返回同一实例；ESM 也有自己的模块缓存，但 URL 查询参数或片段变化会导致同一文件被当作不同模块加载。
- 🔄 ESM 在评估前就建立所有绑定，循环依赖中早期读取可能触发“未初始化”错误；CommonJS 允许循环中读取部分构建的导出对象，且替换`module.exports`会与已缓存引用脱节。
- 🔁 ESM 使用动态`import()`可以实现条件和延迟加载，并从 CommonJS 异步加载 ESM；Node.js 新版本也允许`require()`同步加载无顶层`await`的 ESM 图。
- 🌉 ESM 导入 CommonJS 时，默认导出对应`module.exports`，具名导出是静态检测的“快照”，不会跟踪运行时属性变化；CommonJS 加载 ESM 时通常得到命名空间对象，需要访问`.default`。
- 🧩`__esModule`是打包器/转译器的互操作约定，不是原生 ESM 特性；不同工具生成的默认导出包装可能不同，导致开发与生产行为不一致。
- 📦发布双格式包时，需用`"exports"`条件映射分别指向 ESM 和 CommonJS 入口，并注意`"type"`字段与文件扩展名（`.mjs`/`.cjs`）的决定性作用。
- ⚡分离的`"import"`和`"require"`目标会产生两个独立模块实例，导致类、状态、配置等“双重包”问题；应尽量共享底层实现或将状态外置。
- 🧪实际测试应针对打包后的 tarball 安装到干净项目，分别运行 ESM 和 CommonJS smoke tests，验证公共入口和子路径，而不是只测试源码路径。
- 🛠️调试模块异常时，先确认文件格式、入口解析、返回形状、局部变量持有的是绑定/对象/复制值、评估是否完成、循环依赖、模块身份，并移除转译器干扰。

---

### [在投资于技术和技术人员的地方工作。| 富达职业](https://jobs.fidelity.com/en/life-at-fidelity/our-stories/tech-careers/fidelity-tech-strategy-empowers-associates/?utm_source=javascript&utm_medium=paidsocial&utm_campaign=jobssocial&utm_content=awn-tech-nl2-s)

**原文标题**: [Work where they invest in technology and technologists. | Fidelity Careers](https://jobs.fidelity.com/en/life-at-fidelity/our-stories/tech-careers/fidelity-tech-strategy-empowers-associates/?utm_source=javascript&utm_medium=paidsocial&utm_campaign=jobssocial&utm_content=awn-tech-nl2-s)

富达投资聚焦于技术栈与员工培训，旨在通过实用且高质量的技术赋能员工和客户。本文介绍了富达的科技战略、新技术采用流程，以及技术员工的成长机会与支持。

- 💼 富达大力投资战略技术，打造安全可靠的产品与服务，助力员工和客户共同发展。
- 🎓 技术员工可获得专门时间、充足资源和动手实践机会，持续提升自身技能。
- 🔍 团队紧密关注科技与金融科技趋势，确定新技术的最佳应用场景。
- 🧪 通过真实场景测试技术，并制定清晰路线图，将新技术无缝整合到工作流程中。
- 🔄 持续评估技术的质量与适用性，以满足不断变化的客户需求和业务目标。
- 🤝 提供教练、导师和社交机会，帮助技术员工相互连接、共同成长。
- 📈 员工反馈表示，富达提供大量成长机会，实际接触技术比课程学习更有价值。
- 📬 欢迎加入富达人才网络，获取最新职位信息与求职建议，开启技术职业生涯。

---

### [](https://blog.cloudflare.com/cloudflare-blog-uses-emdash/)

**原文标题**: [The Cloudflare Blog â Brought to you by EmDash | Cloudflare Blog](https://blog.cloudflare.com/cloudflare-blog-uses-emdash/)

Cloudflare 博客近期完成了一次大规模迁移，从原有 CMS 切换到专为 Astro 和 Cloudflare 设计的 EmDash 平台。本次迁移不仅是技术栈升级，还结合了前端重新设计、多层缓存架构和渐进式发布策略，显著提升了性能与稳定性，并为 AI 代理提供了 MCP 支持。

- 🚀 作为“客户零号”，Cloudflare 内部率先使用 EmDash，通过实际场景验证了平台可用性，并推动其修复调度发布等关键缺口。
- 📊 使用 k6 执行 Ramp、Breakpoint、Burst 三类性能测试，确保平台能应对 75 RPS 常态及超过 5,000 RPS 的突发流量。
- 🧱 采用 Cloudflare Worker + Workers Cache + KV 对象缓存 + Hyperdrive/PlanetScale 的多层缓存架构，提升缓存命中率并降低数据库压力。
- 🎨 前端基于 Kumo 设计系统重新设计，加入原生明暗模式、修正订阅表单位置，并新增“本页目录”与“在线讨论”侧边栏。
- 🛡️ 通过代理 Worker 和版本 Cookie 实现渐进式流量切换，从 1% 逐步至 100%，确保零停机且可随时回退旧版。
- ⚡ 迁移后 p95 延迟显著降低且曲线平稳，在 850 RPS 下依然保持低错误率，Lighthouse 分数明显提升。
- 🤖 发布 Cloudflare Blog 的 MCP 服务器，支持搜索、列表、获取文章等工具；EmDash 自身也提供 MCP，且不额外收费。
- 🧪 Agents Week 期间新平台经受住考验：9 天发布 28 篇文章、近 300 万浏览量，并成功吸收 28,000 RPS 的 DDoS 攻击。
- ✨ Cloudflare 团队对 EmDash 的反馈响应表示高度认可，并推荐读者尝试即将推出 v1 的 EmDash。

---

### [EmDash 内容管理系统](https://www.emdashcms.com/)

**原文标题**: [EmDash CMS](https://www.emdashcms.com/)

EmDash 是一个基于 Astro 构建的开源全栈 CMS，定位为 WordPress 的精神续作，主打 TypeScript 全栈体验、安全插件沙箱、AI 代理友好和现代化内容管理。

- 🚀 EmDash 已正式发布，是一个面向 Astro 的开源、全栈、支持 AI 代理的 CMS，提供在线试玩和文档。
- 🔐 插件不再有安全噩梦：所有插件都在隔离沙箱中运行，并遵循最小权限原则。
- ⚡ 深度集成 Astro，支持服务端渲染页面、内容加载器、图像组件和 JSON 结构化内容。
- 🧩 继承 WordPress 的优点，但管理面板更快、架构更现代，且无插件安全隐患。
- 📝 可在后台创建专属内容类型，支持草稿、修订、定时发布、全文搜索、分类、菜单和实时预览。
- 🤖 为 AI 代理而生：通过完善的 API 和 MCP 服务器，让人类与代理协同构建和编辑网站。
- 🧰 支持插件扩展：可添加自定义块类型、管理页面、钩子、存储适配器等。
- 💬 获得 WordPress 联合创始人 Matt Mullenweg、Yoast 创始人 Joost de Valk 等行业大咖的高度认可。
- ❓ 常见问题回答：EmDash 是 Cloudflare 团队基于 Astro 构建的开源 CMS；无需 AI 也能使用，但内置 MCP 服务器可轻松接入 Claude、OpenCode 等工具。
- 🛠️ 快速上手：可直接打开 Playground，或运行 `npm create emdash` 在本地创建新项目。
- 💬 支持渠道：可通过 Discord 交流、GitHub 提交 Issue，官方文档覆盖安装、架构和完整 API 参考。

---

### [](https://www.youtube.com/watch?v=cywK3XYYJ2o)

**原文标题**: [Creator of TypeScript: 10x Faster Typescript, Why AI Won't Replace SWEs | Anders Hejlsberg - YouTube](https://www.youtube.com/watch?v=cywK3XYYJ2o)

overview summary
這是 YouTube 網站頁尾的導覽連結清單，提供關於版權、聯絡方式、創作者支援、廣告、法律條款與平台運作等基本資訊。

- 📰 包含新聞中心與版權資訊入口
- 📧 提供聯絡我們與創作者相關連結
- 📢 設有刊登廣告與開發人員選項
- ⚖️ 列明條款、私隱及政策安全規範
- 🔍 說明 YouTube 的運作方式與新功能測試
- ©️ 標示 2026 Google LLC 版權所有

---

### [在 TypeScript 对象中隐藏内部状态 ✦ Carlos Menezes](https://www.carlos-menezes.com/posts/hiding-properties-typescript)

**原文标题**: [Hiding internal state in TypeScript objects ✦ Carlos Menezes](https://www.carlos-menezes.com/posts/hiding-properties-typescript)

本文介绍了在 TypeScript 对象中隐藏内部状态的技巧：通过模块内不导出的 `unique symbol` 作为属性键，让内部状态难以被外部直接访问，同时避免出现在常规字符串化操作中。该方法虽不能提供绝对隐私，但能有效阻止意外访问。

- 🤔 将内部上下文直接作为对象属性会暴露实现细节，而下划线前缀只是表达意图，无法真正限制外部读写。
- 🔑 使用 `unique symbol` 定义属性键，并将该符号保留在模块内部，外部代码因无法引用同一符号而难以访问该属性。
- 👀 符号键属性不会出现在 `Object.keys` 或 `JSON.stringify` 中，使对象的公共表面保持简洁。
- 🔄 模块内的函数仍可通过符号引用访问内部状态，例如 `createChildLogger` 能够读取并合并父 logger 的 context。
- ⚠️ 这种方案并非绝对安全，属性仍可通过 `Reflect.ownKeys` 或 `Object.getOwnPropertySymbols` 被发现；它更适合防止意外访问，而非抵御恶意代码。

---

### [](https://tkdodo.eu/blog/reliable-query-prefetching-with-tanstack-router)

**原文标题**: [Reliable Query Prefetching with TanStack Router](https://tkdodo.eu/blog/reliable-query-prefetching-with-tanstack-router)

本篇文章探讨了 TanStack Router 中可靠查询预取的实现路径，聚焦 route loader 与组件间数据获取逻辑重复且易失同步的痛点，并给出了通过 `loaderDeps` 与 Route Context 共享 `queryOptions` 的完整解决方案。

- 🎯 组件不应自行发起数据获取，而应尽早交由 route loader 触发，否则会延迟加载时机并容易产生 fetch waterfall。
- ⚠️ 核心痛点：route loader 与组件中的查询逻辑需要双重维护，且必须 100% 同步，但实际开发中会因组件拆分和需求迭代而逐渐脱节。
- 🔍 两处不一致时没有任何编译期或运行期错误提示，是一种隐蔽且极易引入的 bug。
- 🐛 示例说明：Dashboard 新增可选 `asOf` 查询参数后，若 loader 未同步更新，会先预取"今天"数据，组件再按 `asOf` 重新请求并二次挂起，导致多余请求和 waterfall。
- 🧩 方案一：通过 `loaderDeps` 显式声明影响数据加载的查询参数，让 loader 在相关 search 参数变化时也能正确重新预取。
- 🔗 方案二（治本）：利用新的 `context` 函数（仅在 loader 运行时执行）创建 `queryOptions` 并放入 Route Context，loader 与组件都从 context 获取同一份 options，从根源杜绝重复与失同步。
- 📦 Context 继承优势：父路由预取的 `queryOptions`（如用户数据）会被所有子路由组件共享复用，进一步减少重复代码。
- ⚡ 订阅性能保障：`context` 仅在 `params` 或 `loaderDeps` 变化时重新执行，无关的 search 参数变化不会触发订阅组件不必要的重渲染。

---

### [](https://bhugo.dev/blog/compile-time-crimes/1/)

**原文标题**: [I Patched the TypeScript Compiler to Add Up Nine Numbers Â· Hugo Vilela](https://bhugo.dev/blog/compile-time-crimes/1/)

本文介紹作者如何將函數式編程熱情帶入 TypeScript，透過在型別系統中實作演算法來解 HackerRank 題目，甚至為了突破遞迴限制而直接修改 TypeScript 編譯器。

- 🧩 作者決心把 Haskell 的函數式編程樂趣帶進 TypeScript，嘗試只用型別系統解競爭程式設計題目。
- 📥 題目是「加總所有奇數」，例如 `3 + 5 + 7 + 1 = 16`，需要在型別層級完成判斷與加法。
- 🔢 由於型別系統沒有數字，採用 Peano 數（`Zero` 與 `Succ<N>`）來表示自然數，並實作 `ToNumber`、`ToPeano`、`Add`、`IsOdd` 等型別工具。
- 🧮 接著用型別映射將輸入陣列轉成 Peano 數、過濾奇數、加總，最終得到 `Result = 16`。
- ⚠️ 當輸入規模變大時，Peano 數的 O(N) 遞迴深度讓 TypeScript 報出「Type instantiation is excessively deep」錯誤。
- ⛏️ 作者直接修改 TypeScript 編譯器，加入 `--noRecursionLimits`（移除遞迴限制）和 `--printType`（印出型別結果）兩個 CLI 旗標。
- ⚡ 另外實作更高效的「數字字串」表示法，讓複雜度降到 O(log₁₀N)，執行時間從 2.35 秒降到 0.57 秒，約快 4 倍。
- 📦 所有程式碼已公開在 `TypescriptCompetitiveProgramming` repo，並預告未來可能挑戰更瘋狂的編譯期 Turing Machine 或圖形遍歷。

---

### [](https://daverupert.com/2026/08/microlighter/)

**原文标题**: [Introducing Microlighter - daverupert.com](https://daverupert.com/2026/08/microlighter/)

作者介绍了自己开发的一个极简客户端语法高亮器 MicroLighter，它基于 CSS Custom Highlights API，具备零依赖、体积小、按需加载语言等特性，并将额外功能拆分到 Web Component 中，方便集成和自定义。

- 🚀 开发了 MicroLighter，一个约 2kb 的轻量级语法高亮器，利用 CSS Custom Highlights API，通过 `::highlight()` 直接标记 token，不注入 span，避免 DOM 操作。
- ⚙️ 零依赖，基于 Textmate 语法规则，可支持几乎所有编程语言；语言语法按需动态加载，只加载实际用到的部分，减小打包体积。
- 🎨 将 Textmate 的分类简化成更人性化的 token 类别，如 comment、function、type 等；并利用 `light-dark()` 函数把明暗主题合并成一个文件，便于维护。
- 🧩 核心库只负责“推断语言 + 高亮”，其他功能如行号、复制按钮等通过 `<micro-lighter>` 自定义元素实现，利用 ShadowDOM 隔离样式和逻辑。
- 📦 提供多种使用方式：可直接用脚本标签引入、按需动态 `import()`、使用 ESM 版本调用 `highlightAll()`，或直接使用自定义元素，且支持扩展自定义类。
- 🛠️ 用户可以自定义主题，通过 `--syntax-*` CSS 变量配置背景、前景及各 token 颜色，并用 `::highlight()` 伪元素应用样式，示例结构清晰易懂。

---

### [](https://developer.mozilla.org/en-US/docs/Web/API/CSS_Custom_Highlight_API)

**原文标题**: [CSS Custom Highlight API - Web APIs | MDN](https://developer.mozilla.org/en-US/docs/Web/API/CSS_Custom_Highlight_API)

CSS Custom Highlight API 是一种用于在网页上为任意文本范围添加样式的新机制，结合 JavaScript 创建 Range 对象与 CSS 进行样式定义，无需改动 DOM 结构。该 API 扩展了 ::selection 等伪元素，并提供了 Highlight 与 HighlightRegistry 接口，让开发者能灵活实现搜索高亮、协作文本编辑等效果。

- 🔍 概述：该 API 通过 JavaScript 创建 Range 范围，再用 CSS 的 ::highlight() 伪元素进行样式设置。
- 🧩 核心概念：支持任意 Range 对象，并涵盖 ::selection、::spelling-error 等类似场景，但不受浏览器内置范围限制。
- 📝 四步用法：创建 Range → 创建 Highlight → 通过 CSS.highlights 注册 → 使用 ::highlight() 设置样式。
- 🎯 Range 创建：用 new Range() 和 setStart / setEnd 精确定位文本范围。
- 💡 Highlight 对象：可聚合多个 Range，支持按用户或场景创建多个高亮并分别定制样式。
- 📚 注册机制：HighlightRegistry 是类似 Map 的对象，用 CSS.highlights.set() 注册，支持 delete 和 clear。
- 🎨 样式设置：通过 ::highlight(user-1-highlight) 等伪元素应用背景色、文字颜色等样式。
- ♿ 无障碍注意：高亮本身无语义，需用 type 属性或结合 <mark> 等方式提供辅助信息。
- 🖥️ 接口：主要包含 Highlight 和 HighlightRegistry，浏览器兼容性自 2025 年 6 月起全面支持。
- 🔧 示例：完整展示了搜索框输入时用 TreeWalker 找出匹配文本并动态高亮的过程。

---

### [MicroL](https://davatron5000.github.io/microlighter/)

**原文标题**: [MicroLighter - A zero-dep syntax highlighter](https://davatron5000.github.io/microlighter/)

overview summary：MicroLighter 是一個輕量級、高速的程式碼語法高亮工具，支援 TextMate 文法，具備依需求延遲載入語言模組、自動高亮、與自訂元素擴充等功能，並涵蓋多種程式語言與設定格式。
- ⚡ 主打輕量與極速：程式碼高亮非常迅速，且支援 gzip 壓縮，檔案僅約 2.05 kb。
- 📦 安裝簡易：透過 npm 安裝，匯入主題後，標記 `language-*` class 即可使用，並支援 `highlightAll()` 自動高亮。
- 🚀 自動執行模式：引入 minified 的 auto-runner 即可在頁面載入時自動高亮，亦可監聽 `syntax-highlight` 事件重新整理。
- 🧩 自訂元素擴充：可導入 `micro-lighter` 元素，透過屬性設定語言、複製按鈕與行號顯示。
- 🗂️ 語言模組延遲載入：每種語言語法獨立模組，只在頁面實際使用時才載入，有效節省資源。
- 🌐 支援多種語言與格式：涵蓋 Web（HTML、CSS、JavaScript、TypeScript 等）、系統（C、C++、Rust、Go）、應用（Java、C#、Swift）、腳本（Python、Ruby、Bash）、資料與設定（JSON、TOML、SQL、Markdown、Dockerfile）等多種常見語法。
- 🎨 相容 TextMate 文法：使用與 VS Code 相同的文法規則，高亮表現專業且一致。
- 🧪 提供線上 Playground：可即時預覽各種語言的高亮效果。

---

### [TermDOM | 使用 HTML、CSS 和 DOM 构建终端应用](https://termdom.org/)

**原文标题**: [TermDOM | Build terminal apps with HTML, CSS and the DOM](https://termdom.org/)

TermDOM 是一个 JavaScript/TypeScript 库，它把浏览器标准的 HTML、CSS 和 DOM 渲染到终端里，让开发者可以用原生前端技术或主流框架直接编写 TUI 和交互式 CLI，无需学习自定义控件 API，并自动处理布局、样式、事件与重绘。

- 🖥️ **真实 DOM 渲染**：实现符合规范的 DOM 与 CSSOM，节点变更后自动重绘，无需手动调用渲染函数。
- 🎨 **完整 CSS 支持**：支持样式表与内联样式，经级联计算后转换为 ANSI 转义序列，包括颜色、粗体、斜体、下划线等。
- 📐 **浏览器级布局**：内置 flexbox、grid、表格、盒模型等算法，以字符单元格为长度单位（1px/1ch 代表一格），支持文本换行与终端尺寸自适应。
- ⌨️ **原生事件系统**：解码 stdin 的转义序列并派发 DOM 事件（keydown、click、paste 等），支持 Tab 焦点移动和 :focus 样式。
- 🧩 **前端生态兼容**：浏览器库无需修改即可运行，前端框架只需少量配置即可使用；示例展示了直接使用 Prism 做语法高亮。
- 📊 **示例丰富**：提供 Solitaire、柱状图、表单、Flexbox 布局、代码高亮等演示，展示从静态界面到动态交互的能力。
- 🔄 **实时动态更新**：通过标准 DOM API（如 innerHTML、style 修改）即可驱动终端画面更新，适合动画、实时数据等场景。
- 📦 **快速上手**：通过 `npm install @b9g/termdom` 安装，支持入门指南、在线 playground 和 GitHub 源码，并提供浏览器特性兼容性表。

---

### [](https://github.com/vadimdemedes/ink)

**原文标题**: [GitHub - vadimdemedes/ink: 🌈 React for interactive command-line apps · GitHub](https://github.com/vadimdemedes/ink)

overview summary
Ink 是一个基于 React 的 CLI 渲染库，允许开发者用组件化方式构建命令行界面，支持 Flexbox 布局和 React 全部特性。

- 🖥️ Ink 将 React 组件渲染为终端输出，支持 Flexbox 布局（基于 Yoga）。
- ⚛️ 安装方式：`npm install ink react`，需配置 Babel 以支持 JSX。
- 🚀 快速创建项目：`npx create-ink-app` 支持 JavaScript 和 TypeScript。
- 🧱 核心组件包括 <Text>（文本样式）、<Box>（布局容器）、<Newline>、<Spacer>、<Static>、<Transform>。
- 🎨 <Text> 支持颜色、背景色、粗体、斜体、下划线、删除线等样式，以及文本换行/截断。
- 📐 <Box> 提供尺寸、内边距、外边距、间隙、Flexbox 布局、定位、边框、背景色等丰富样式属性。
- 📌 <Static> 用于永久渲染静态内容（如已完成任务列表），<Transform> 可转换子组件输出字符串。
- ⌨️ Hooks 包括 useInput、usePaste、useApp、useStdin/useStdout/useStderr、useBoxMetrics、useWindowSize、useFocus、useFocusManager、useCursor、useAnimation 等。
- 🔄 Ink 应用生命周期由 Node.js 事件循环驱动，可通过 Ctrl+C、exit() 或 unmount() 退出。
- 🧪 支持使用 ink-testing-library 进行组件测试，并可集成 React Devtools 调试。
- ♿ 提供屏幕阅读器支持（ARIA 属性及 INK_SCREEN_READER 环境变量）。
- 🗂️ API 包含 render()、renderToString()，实例方法有 rerender、unmount、waitUntilExit、clear、measureElement 等。
- 🧩 社区拥有大量实用组件（如 text-input、spinner、select-input、table 等）和钩子，方便扩展。
- 📚 提供丰富示例（如计数器、表单、路由、Suspense、焦点管理等）供学习参考。
- 🤝 由社区维护，支持 MIT 许可证，欢迎贡献（需人工验证 AI 生成代码）。

---

### [发布 TermDOM 0.1.5 · bikeshaving/termdom · GitHub](https://github.com/bikeshaving/termdom/releases/tag/v0.1.5)

**原文标题**: [Release TermDOM 0.1.5 · bikeshaving/termdom · GitHub](https://github.com/bikeshaving/termdom/releases/tag/v0.1.5)

TermDOM 0.1.5 是一个重要版本，新增了 CSS Grid、元素滚动、剪贴板、焦点导航、IME 组合等多项能力，并大幅优化了初始渲染性能，同时通过大量 WPT 测试验证了规范一致性。

- 🎯 新增 CSS Grid 支持，包括轨道尺寸、放置、对齐及简写解析。
- 📜 实现元素滚动，支持溢出裁剪、scrollTop/scrollLeft 限制和滚动事件链。
- 📋 添加剪贴板事件与 DataTransfer，基于用户激活门控。
- ⌨️ 支持 Selection.modify() 的字符、单词、行粒度。
- 🔍 顺序焦点导航遵循 HTML 作用域模型，含 delegatesFocus 和负 tabindex 行为。
- 🚫 实现 user-select: none/text 的选择禁用与恢复。
- 📐 增加 aspect-ratio 支持。
- 🎨 将 CSS 系统颜色映射到终端调色板。
- 📂 为 `<details>` 添加用户代理影子树。
- 🔢 数字输入按数字方式编辑，支持过滤、箭头步进和 valueAsNumber 系列。
- 🔀 新增 Node.moveBefore 原子移动原语。
- 📡 新增多个事件接口，如 MessageEvent、DragEvent、StorageEvent 等。
- 📍 暴露几何与命中测试 API，如 elementsFromPoint、checkVisibility 等。
- 🈶 支持 IME 组合输入，终端透传按键并整体交付。
- ✨ 变更：`<kbd>` 改为加粗下划线，:focus 系列阴影感知，isTrusted 真实反映来源。
- 🚀 性能修复：widget 重绘导致初始渲染从 43 秒降至 374 毫秒。
- 🐛 修复焦点、全屏、requestAnimationFrame、grid-template-areas 等缺陷。
- ✅ WPT DOM 套件：95,064 个子测试通过，1,389 个失败，详情见相关文档。

---

### [GitHub - paradedb/drizzle-paradedb：用于 ParadeDB 的 Drizzle 官方扩展 · GitHub](https://github.com/paradedb/drizzle-paradedb)

**原文标题**: [GitHub - paradedb/drizzle-paradedb: Official extension to Drizzle for use with ParadeDB · GitHub](https://github.com/paradedb/drizzle-paradedb)

overview summary
- 📦 这是 ParadeDB 官方为 Drizzle ORM 提供的集成扩展，基于 pg_search 扩展，可管理索引并支持完整查询 API。
- 🔍 覆盖全文搜索与基于 pgvector 的向量搜索，满足混合检索需求。
- 🚀 兼容性要求：Node 22.12+、Drizzle 1.0+、ParadeDB 0.25.0+、PostgreSQL 15+（向量搜索需 pgvector）。
- 📚 提供多种示例：快速开始、向量搜索、分面搜索、混合搜索（RRF）、RAG、自动补全、更多类似内容。
- 🛠️ 项目包含完整的贡献指南、开发环境配置、测试与代码规范工具。
- 📄 采用 MIT 许可证，支持通过 GitHub Issues、Slack、Discussions 获取社区帮助，也可联系商业支持。

---

### [](https://formisch.dev/blog/formisch-v1/)

**原文标题**: [Formisch v1 is here | Formisch](https://formisch.dev/blog/formisch-v1/)

overview summary
Formisch v1 正式发布，这是一个基于 schema 的框架无关表单库，现已稳定可用于生产环境。文章介绍了其设计理念、新增框架支持、迁移指南、面向 AI 代理的文档，以及未来规划。

- 🎉 Formisch v1 已稳定，支持生产环境，采用语义化版本控制，破坏性变更仅随主版本发布。
- 🧩 框架无关：基于 schema 定义表单，类型与验证由 schema 驱动，UI 层可自由构建，支持八种框架。
- 📦 新增 Angular 支持，通过 injectForm/injectField 及指令绑定，schema 驱动类型与验证。
- 📱 新增 React Native 支持，首个无 DOM 环境，核心逻辑与 DOM 解耦，通过原生组件 refs 实现焦点路径。
- 🧭 六个框架共提供 15 份迁移指南，覆盖 TanStack Form、Formik、React Hook Form、VeeValidate、FormKit、Superforms 等，Preact 和 Qwik 暂缺。
- 🤖 文档以 Markdown 形式提供，并配有 MCP 服务器，方便 AI 代理读取和检索，且可按框架限定范围。
- 🔮 未来计划：支持 meta-framework 实现前后端表单贯通、通过 Standard Schema 支持更多 schema 库（如 Zod）。
- 🚀 快速体验：提供在线 playground，安装对应框架包与 Valibot 即可使用。
- 🙏 感谢所有 RC 测试者、文档/代码贡献者及赞助商，项目保持免费开源。

---

### [](https://valibot.dev/)

**原文标题**: [Valibot: The modular and type safe schema library](https://valibot.dev/)

Valibot 是一个注重 bundle 体积、类型安全和开发者体验的开源 TypeScript schema 库，可运行时验证未知数据，并支持通过模块化设计大幅减小打包体积。

- 🔒 完全类型安全：在 TypeScript 中享受静态类型推断与类型安全带来的好处
- 📦 极小的 bundle 体积：模块化 API 设计使其初始体积小于 700 字节
- ✅ 验证万物：支持从原始值到复杂对象的几乎所有 TypeScript 类型
- 🧪 100% 测试覆盖：源代码开源且全面测试，覆盖率高达 100%
- 🧰 内置辅助工具：已包含重要的验证和转换辅助函数
- 👨‍💻 出色的开发者体验：API 简洁、可读且经过精心设计
- 💰 免费且开源：采用 MIT 许可证，依靠合作伙伴和赞助商资助项目
- 🔍 核心功能：用 schema 描述结构化数据，可在运行时执行以保证未知数据的类型安全（区别于 TypeScript 类型只在编译期生效）
- ✂️ 模块化设计大幅减少体积：通过 tree shaking 和代码分割，只打包实际使用的代码
- ⚔️ 与 Zod 的对比：功能相似，但模块化设计可将体积比 Zod 减少高达 95%，特别适合客户端表单验证和无服务器环境

---

### [](https://stryker-mutator.io/)

**原文标题**: [Stryker Mutator](https://stryker-mutator.io/)

overview summary  
Stryker 是一款支持多种语言的变异测试工具，具备丰富的突变类型、高效执行和灵活集成的特点，并可通过智能报告提升测试有效性。

- 🧬 支持超过 30 种变异操作，可全面验证测试用例的有效性。  
- ⚡ 利用代码分析与并行测试进程，大幅提升变异测试速度。  
- 🔌 与主流测试运行器无缝兼容，可自由选择偏好的测试框架。  
- 🌍 开源免费，由 GitHub 社区持续维护，遵循自由软件理念。  
- 🗣️ 多语言支持，覆盖 JavaScript、TypeScript、C# 和 Scala。  
- 📊 借助智能报告快速定位存活变异体，针对性改进测试质量。

---

### [](https://stryker-mutator.io/docs/mutation-testing-elements/supported-mutators/)

**原文标题**: [Supported mutators | Stryker Mutator](https://stryker-mutator.io/docs/mutation-testing-elements/supported-mutators/)

本頁介紹 Stryker 系列工具支援的各種變異算子（Mutators），並以表格列出在不同框架（StrykerJS、Stryker.NET、Stryker4s）中的支援情況，以及各算子的原始碼與變異後範例。

- ➕ 算術運算子：支援加減乘除互換、餘數轉乘法；StrykerJS 與 Stryker.NET 支援，Stryker4s 不支援。
- 📦 陣列宣告：可移除陣列建構子或陣列字面值的全部項目（如 `new Array(1,2,3)` → `new Array()`）。
- 📝 賦值表達式：將 `+=`、`-=`、`*=`、`/=` 等複合賦值運算子互換；部分僅限特定框架。
- 🧱 區塊陳述式：`BlockRemoval` 會清空所有區塊內容，例如函數體變成空 `{}`。
- 🔘 布林字面值：將 `true` 與 `false` 互相替換，或移除 `!` 運算子。
- ✅ Checked 陳述式：僅 Stryker.NET 支援，可移除 `checked` 關鍵字。
- 🔀 條件表達式：將比較條件改為 `true`／`false`（如 `i < 10` → `false`），或用於三元表達式。
- ⚖️ 相等運算子：改變邊界與否定比較（如 `<` ↔ `<=`、`==` ↔ `!=`、`===` ↔ `!==`）。
- 🔗 邏輯運算子：互換 `&&`、`||` 以及 `??` 的變異。
- 🧪 方法表達式：因語言而異；JS、.NET、Scala 各有不同的方法替換（如 `trim()` ↔ `trimEnd()`、`First()` ↔ `Last()`、`filter()` ↔ `filterNot()`）。
- 🎯 物件字面值：僅 StrykerJS 支援，移除物件屬性（`{ foo: 'bar' }` → `{}`）。
- 🔍 可選鏈：僅 StrykerJS 支援，將 `?.` 移除為必需存取（如 `foo?.bar` → `foo.bar`）。
- 🧩 正規表達式：透過武器級工具產生 Level 1 變異，如移除錨點、字元類取反、量詞移除、Lookahead 替換等。
- 🔤 字串字面值：將非空字串變為空字串，或將空字串填入固定文字；插值字串也會被清空。
- ➖ 一元運算子：互換正負號（`+a` ↔ `-a`）。
- 🔄 更新運算子：將前置／後置遞增與遞減互換（`a++` ↔ `a--`）。

---

### [入门 | Stryker Mutator](https://stryker-mutator.io/docs/stryker-js/getting-started/)

**原文标题**: [Getting started | Stryker Mutator](https://stryker-mutator.io/docs/stryker-js/getting-started/)

overview summary  
- 🚀 StrykerJS 是一个用于 JavaScript 项目的变异测试工具，通过引入变异来检查测试套件的有效性。  
- 📦 使用 npm 安装并初始化：先进入项目目录，运行 `npm init stryker@latest` 并按提示配置。  
- ⚙️ 初始化完成后，检查生成的 `stryker.config.mjs` 配置文件以调整选项。  
- 🧪 运行 `npx stryker run` 执行变异测试；若遇问题，可用 `--logLevel trace` 开启详细日志。  
- 📚 更多配置细节可查阅官方配置文档，问题反馈可通过 GitHub Issues 或 Slack 联系。

---

### [](https://ionic.io/blog/announcing-ionic-framework-9)

**原文标题**: [Announcing Ionic Framework 9 - Ionic Blog](https://ionic.io/blog/announcing-ionic-framework-9)

Ionic Framework 9 正式发布，重点回应社区对路由支持、Angular 兼容性和升级体验的诉求，带来多项新功能与迁移工具，并预告未来 Modular Ionic 方向。

- 🚀 新增 React Router v6 支持：重写集成逻辑，不再依赖其内部实现，修复滑动返回等问题，为 v7 铺路。
- 🛤️ 支持 Vue Router v5：多数 v4 用户可无缝升级，注意 `next()` 已弃用，最低 Vue 版本升至 3.5。
- 🔄 兼容 Angular 18–22：默认采用 zoneless 变更检测，异步回调需显式通知；Angular 22 默认 OnPush，导入路径调整。
- 🧩 更新 Stencil 输出目标：React/Angular 输出目标升至 1.x，增强类型检查与测试覆盖；React 输出目标要求 React 18+。
- 📋 Select 支持富文本：`ion-select-option` 可在四种界面中使用图片、头像、图标、徽章和描述文字。
- 🔤 ion-icon 新增字体图标支持：搭配 SVG 使用，支持 color、size 和 RTL，推荐用 font-size 控制大小。
- 🛠️ 提供迁移工具 `npx @ionic/migrate`：自动修复多项 v9 破坏性变更，支持 `--dry-run` 和 `--check`。
- 🔮 预告 Modular Ionic：计划于 2027 年 Q2 推出，将外观与行为解耦以提升自定义灵活性。

---

### [更新到 v](https://ionicframework.com/docs/updating/9-0)

**原文标题**: [Updating to v9 | Ionic Framework](https://ionicframework.com/docs/updating/9-0)

overview summary
- 🚀 **自动化迁移工具**：运行 `npx @ionic/migrate` 可扫描应用、自动应用安全迁移，并输出仍需手动处理的清单；支持 `--dry-run`、`--force`、`--experimental` 等选项。
- 🔄 **Angular 升级**：Ionic 9 支持 Angular 18–22；需更新到最新版本，注意 Angular 21+ 默认 zoneless 无 Zone.js，Angular 22 默认 OnPush 策略。
- ⚛️ **React 升级**：Ionic 9 支持 React 18+ 与 React Router 6；`useIonModal`/`useIonPopover` 现在对 `componentProps` 做类型检查。
- 🟢 **Vue 升级**：Ionic 9 支持 Vue 3.5+ 与 Vue Router 5；`next()` 导航守卫已弃用，改用返回值模式。
- 🧩 **组件导入路径变化**：懒加载组件从 `@ionic/angular/lazy` 导入，独立组件改从 `@ionic/angular` 导入；`IonicModule` 弃用，改用 `provideIonicAngular()`。
- 📱 **Capacitor 要求**：Ionic 9 官方支持 Capacitor 7+，不再回退到 Capacitor 2 的 `isNative` 标志检测原生平台。
- 🖼️ **ion-img 弃用**：改用原生 `<img>` 标签，添加 `loading="lazy"` 和 `decoding="async"`；事件需改用标准 DOM 事件。
- 🔤 **Input/Searchbar 属性变更**：`autocorrect` 改为 boolean 类型，`"off"` 字符串会意外启用，需移除属性或使用属性绑定。
- 🎰 **Legacy Picker 移除**：`ion-picker-legacy` 和 `pickerController` 已删除，改用 `ion-picker` 并放入 `ion-modal` 中展示。
- 📐 **Modal 默认行为变化**：`handleBehavior` 默认值从 `"none"` 改为 `"cycle"`，需要旧行为的应用需显式设置 `handleBehavior="none"`。
- 🧭 **Nav 路由集成移除**：`ion-nav` 不再与 `ion-router` 集成，URL 路由改用 `ion-router-outlet`。
- 👆 **Router Outlet 新增 swipeGesture**：`swipeBackEnabled` 配置改为仅初始化时读取，动态切换需使用 `swipeGesture` 属性。
- 📋 **Select 行为变更**：`ionChange` 仅在值真正改变时触发；`action-sheet` 界面不再分配 `selected` 角色。
- 📝 **Textarea 结构调整**：内部 DOM 重组，`.textarea-wrapper-inner` 移除，新增 `.textarea-control`；md 模式最小高度改为 72px。
- 🌐 **浏览器支持更新**：最低版本为 Chrome 89、Safari 16、iOS 16 等，需更新 `browserslist` 配置。
- 📦 **包导出字段**：`@ionic/core` 新增 `exports` 字段，需使用支持的子路径，如 `@ionic/core/components`、`@ionic/core/loader`。

---

### [Papa](https://www.papaparse.com/)

**原文标题**: [Papa Parse - Powerful CSV Parser for JavaScript](https://www.papaparse.com/)

overview summary
Papa Parse 5 是一款高性能、支持多线程的浏览器端 CSV 解析库，主打速度、隐私和稳健性，可处理超大文件，并提供丰富的解析与转换功能。

- 🚀 号称目前最快的浏览器 JavaScript CSV 解析器，支持多线程，能处理 GB 级大文件而不崩溃
- 🔒 在浏览器本地解析文件，避免上传隐私问题，适合注重性能、隐私和正确性的场景
- 📊 支持 CSV→JSON 和 JSON→CSV 双向转换，自动检测分隔符，兼容本地与远程文件
- 🧵 通过 `worker: true` 启用多线程解析，避免页面卡顿，保持界面响应
- 🧠 设置 `header: true` 可自动识别表头，让数据按字段名而非索引访问
- 🔢 开启 `dynamicTyping: true` 会自动将数字/布尔值转换为对应类型，而非一律当字符串
- 💬 支持 `comments: "#"` 跳过注释行，应对包含注释的非常规 CSV 文件
- ⚠️ 对畸形 CSV 提供优雅的错误处理，并输出详细错误报告（如字段数量不匹配）
- 🔧 可选集成 jQuery（当 jQuery 存在时自动暴露为插件），但本身无依赖
- 📦 可通过 npm 或 bower 安装，并提供 minified 版本（Lil' Papa）和开发版（Fat Papa）
- 💡 支持流式解析（`step` 回调）逐行处理数据，避免将整个大文件载入内存

---

### [](https://github.com/maplibre/maplibre-gl-js)

**原文标题**: [GitHub - maplibre/maplibre-gl-js: MapLibre GL JS - Interactive vector tile maps in the browser · GitHub](https://github.com/maplibre/maplibre-gl-js)

MapLibre GL JS 是一个开源的浏览器端地图渲染库，源于 mapbox-gl-js 的分支，利用 GPU 加速矢量瓦片渲染，实现快速交互地图。它提供了快速上手方式、丰富文档、社区贡献渠道和赞助计划，并采用 3-Clause BSD 协议授权。

- 🗺️ 开源地图库：用于在网站或 webview 应用中发布交互式地图，通过 GPU 加速渲染矢量瓦片。
- 🔄 项目起源：因 Mapbox GL JS 于 2020 年转向非开源许可证而产生，初期作为 1.x 兼容替代品，后续持续演进。
- ⚡ 快速开始：在 HTML 中引入 CSS 和 JS 模块，通过配置容器、样式、中心点与缩放级别即可创建地图。
- 📖 文档与示例：提供完整官方文档、功能示例，并有 React 和 Angular 绑定及 awesome-maplibre 资源列表。
- 🤝 社区与贡献：可通过 OSMUS Slack 参与，阅读 CONTRIBUTING.md，鼓励加入以避免碎片化，遵循语义化版本。
- 💰 赞助支持：设有金、银等赞助等级，感谢定期捐赠者，详细信息见官方赞助计划。
- 🙏 致谢 Mapbox：承认其开源成就，但明确禁止未经授权回迁非 BSD-3 许可的代码。
- 🛠️ 技术特点：基于 TypeScript 和 WebGL2 构建，相关主题包括 Hacktoberfest 等。
- 📜 开源许可：基于 3-Clause BSD 许可证发布。
- ⭐ 项目规模：GitHub 上拥有 11.4k stars、1.2k forks 和 14,347 次提交。

---

### [](https://github.com/plotly/plotly.js)

**原文标题**: [GitHub - plotly/plotly.js: Open-source JavaScript charting library behind Plotly and Dash · GitHub](https://github.com/plotly/plotly.js)

Plotly.js 是一个开源的 JavaScript 数据可视化库，同时驱动 Python 和 R 的 plotly 模块，支持多种图表类型，可通过 npm、CDN 或自定义 bundle 加载，并提供官方文档、社区支持和 MIT 许可。

- 📊 Plotly.js 是独立 JavaScript 图表库，支持统计图、3D 图、科学图表、SVG 和地图、金融图表等
- 📦 可通过 npm 安装 `plotly.js-dist-min` 或 `plotly.js-dist`，支持 ES6 import 和 CommonJS require
- 🌐 可通过 script 标签加载 CDN 版本（如 `https://cdn.plot.ly/plotly-4.0.0.min.js`），也支持原生 ES6 module 导入
- ➗ 支持 MathJax v3/v4 渲染数学表达式，需单独加载脚本，用 `$...$` 包裹内容
- 🖥️ 可加载 `virtual-webgl` 脚本，以支持页面上多个 WebGL 图表
- 🧩 提供完整和部分官方 bundle，也可自定义 bundle 以优化文件大小
- 📚 官方文档位于 plotly.com/javascript，由 Jekyll 构建并托管于 GitHub Pages
- 🐛 Bug 和功能请求可通过 GitHub issues 提交，并有明确的贡献指南
- 👥 项目有活跃维护者和社区贡献者，包括 Alex C. Johnson、Emily Kellison-Linn 等
- 📄 代码和文档版权归 Plotly, Inc.，采用 MIT 许可证，遵循语义化版本管理
- 💬 社区支持可通过 Plotly 论坛和 Stack Overflow（标签 plotly.js）获取，也可关注 X 和 LinkedIn

---

### [](https://gtkx.dev/blog/gtkx-1-3)

**原文标题**: [GTKX 1.3: Introducing @gtkx/animated | GTKX](https://gtkx.dev/blog/gtkx-1-3)

GTKX 1.3 是一次重大更新，核心是推出 @gtkx/animated，将 React Spring 的动画引擎带到 GTK，并新增了 per-widget 的 style 属性、独立的 @gtkx/cairo 包，以及大幅增强的 registerClass。动画可直接写入 widget 属性或 CSS 样式，性能高效，同时带来了一些破坏性变更和升级注意事项。

- 🎉 发布 GTKX 1.3，重点引入 @gtkx/animated，让 React Spring 支持 GTK 目标，并配备新 style prop、@gtkx/cairo 包和更大的 registerClass。
- 🏷️ animated(Component) 让组件 props 接受 SpringValue 或 Interpolation，每帧通过 ref 直接写属性，不触发重渲染，动画开销极小。
- 🎯 动画值会自动适配目标属性：对整数属性截断、对范围超界值夹紧，非数字值（如 Gsk.Transform）原样传递。
- 📦 移动 widget 需借助容器机制（如 GtkFixedLayoutChild 的 transform），没有通用的 transform 简写。
- 🎨 style prop 可为每个 widget 独立编译 CSS 规则，支持 spring 驱动，颜色动画可通过 interpolation 实现。
- ⚛️ 大部分 React Spring API 可用，但 useScroll、useResize、useInView 因依赖 DOM 未导出。
- 🖥️ 动画帧由 GTK frame clock 驱动，窗口变化时自动切换驱动源，无窗口时使用 timer 兜底。
- ♿ 减少动态效果有两个设置：gtk-enable-animations 完全关闭动画，gtk-interface-reduced-motion 表示减少运动；useReducedMotion 相应处理。
- 🖌️ 新增 @gtkx/cairo 包，Cairo 对象成为真实类，构造函数会抛错；旧 @gtkx/gi/cairo 弃用但暂时保留。
- 🧩 registerClass 增加信号参数定义、类初始化钩子、抽象类、paramSpecOverride 等能力，GType 参数可接受注册类，GValue 参数可接受 JS 值。
- 🔧 多项正确性修复：参数校验、数组绑定、错误传播、所有权转移等不再泄漏或双释放。
- ⚠️ 升级有破坏性变更：移除不安全的 C 函数，on<SignalName> 方法现在会作为信号默认处理器，需重命名无关方法。
- 🚫 更多场景会直接抛错（如缺失参数、非法 flag、cairo 失败、无效 typeName 等）。
- 📉 部分 API 已弃用（Gdk.RGBA.create、Graphene 辅助函数等），将在 2.0 移除。
- 🌗 CSS 中的 prefers-color-scheme、prefers-contrast、prefers-reduced-motion 媒体查询现在真正生效。
- 🗺️ 未来计划包括 @gtkx/navigation（基于 Adwaita 和 React Navigation）和 @gtkx/forms，路线图可在 issue 中讨论调整。

---

### [](https://github.com/LuanRT/YouTube.js/releases/tag/v18.0.0)

**原文标题**: [Release v18.0.0 · LuanRT/YouTube.js · GitHub](https://github.com/LuanRT/YouTube.js/releases/tag/v18.0.0)

YouTube.js 发布 v18.0.0（2026-08-13），带来一项破坏性变更、多项新功能以及若干 bug 修复，涵盖解析器、客户端支持与内部逻辑改进。

- ⚠️ **破坏性变更**：Comments.ts 新增线程评论支持（#1194），并同时修复相关问题
- ✨ **新功能**：Author 新增 `collaborators` 属性，Playlist 新增 `getCollaborators()` 方法（#1203）
- ✨ **新功能**：LockupView 支持将 station 作为 `content_type`（#1229）
- ✨ **新功能**：解析器新增 `VideoDescriptionYouchatSectionView` 类，并修复相关解析警告
- ✨ **新功能**：解析器新增 `ThumbnailOverlayAvatarStackView` 类（#1200）
- ✨ **新功能**：新增 `TicketEvent` 和 `TicketShelf` 类（#1205）
- ✨ **新功能**：protos 新增 `ClipParams`（#1215）
- ✨ **新功能**：Session 新增 `VISIONOS` 客户端（#1213）
- 🐛 **Bug 修复**：CommentView 处理 mutations 时应对未定义 endpoint 的情况（#1208）
- 🐛 **Bug 修复**：HTTPClient 为 ANDROID_VR 客户端添加 User-Agent 头覆盖（#1184）
- 🐛 **Bug 修复**：Innertube#getHashtag 改用 URL-safe Base64（#1211）
- 🐛 **Bug 修复**：MusicResponsiveListItem 读取音乐时长时正确匹配时间戳（#1230）
- 🐛 **Bug 修复**：SubscriptionButton 修复 `subscription_type` 因拼写错误从未被设置的问题，并处理 `text`、`subscribed` 字段缺失的情况
- 🐛 **Bug 修复**：修复 VideoOwner 的一些解析问题
- 🎉 **社区反馈**：该发布获得 hooray 和 heart 等表情回应

---

### [](https://www.reddit.com/r/nextjs/comments/1vrq0tp/were_the_nextjs_team_ask_us_anything/)

**原文标题**: [Reddit](https://www.reddit.com/r/nextjs/comments/1vrq0tp/were_the_nextjs_team_ask_us_anything/)

您似乎没有附上需要总结的文本内容。请提供文章或段落，我将按照指定模板为您生成中文摘要。

---

### [获取失败](https://hacks.mozilla.org/2026/08/intent-to-ship-jpeg-xl/)

**原文标题**: [Failed to retrieve](https://hacks.mozilla.org/2026/08/intent-to-ship-jpeg-xl/)

无法总结：获取内容失败，状态码 403。

---

### [](https://github.com/gajus/css-in-js-arena)

**原文标题**: [GitHub - gajus/css-in-js-arena: Comparison of modern CSS-in-JS frameworks. · GitHub](https://github.com/gajus/css-in-js-arena)

overview summary
这是一个针对编译时 CSS 引擎的基准测试项目，通过完全相同的 React 应用对 Bamboo CSS、StyleX 和 Panda CSS 进行了多维度对比。总体而言，Bamboo 在大多数计分项中胜出，但排名会随着样式数量、文件数量和主题数量的变化而改变。

- 🏆 总体结果：Bamboo CSS 赢得 23/30 个计分项，Panda CSS 赢得 14/30 个，StyleX 赢得 9/30 个。
- 📦 网络传输：Bamboo 在大多数体积指标上最小，但 StyleX 在类名属性字节上更优。
- ⚡ 构建与开发：Panda 的冷启动和 HMR 响应最快，Bamboo 的生产构建时间最短。
- ✍️ 编写体验：Bamboo 和 Panda 支持类型化变体配方（cva），StyleX 需要更多手动组合。
- 🔧 正确性与维护：Bamboo 和 Panda 能在编译时捕获错误，StyleX 更容易将错误输出到生产环境。
- 📈 规模化表现：随着样式定义增加，StyleX 的边际成本呈线性上升，Panda 有固定开销，Bamboo 居中。
- 🗂️ 文件数量影响：Bamboo 在构建和冷启动上随文件数增长最快，Panda 最稳定。
- 🎨 主题机制：Bamboo 和 Panda 支持按需加载主题，StyleX 将全部主题打包进 CSS，导致体积膨胀。
- ⚖️ 结论限制：轴线权重不等，且配置仅代表一种场景，结果不直接推广到所有项目。

---

### [开始使用 Bamboo | Bamboo CSS](https://bamboocss.com/docs/overview/getting-started/)

**原文标题**: [Get started with Bamboo | Bamboo CSS](https://bamboocss.com/docs/overview/getting-started/)

Bamboo CSS 是一个构建时、类型安全、零运行的 CSS-in-JS 方案，源自 Panda CSS，通过 Vite 编译样式调用为全局共享原子类，并自动修剪未使用的样式，显著精简输出。

- ⚡ 构建时编译：样式调用被编译为全局共享的原子类，无运行时开销。
- 🎯 类型安全：由配置生成类型，编辑器自动补全，编译器严格校验。
- 🚫 失败快速：引用不存在的模式或令牌时直接构建失败，如 `ERR_BAMBOO_DEAD_IMPORT`。
- ✂️ 自动修剪：移除未使用的令牌、关键帧和重置规则；示例中样式表体积减少 36–78%。
- 🏭 生产验证：Contra 在生产环境使用超过 20,000 个 `css()` 调用点，并有 3,000+ 测试覆盖。
- 🌿 源自 Panda CSS：API 更小、输出更精简；`css`、`cva`、`sva`、`cx` 等兼容，迁移方便。
- 🧩 核心特性：现代 CSS 输出（`@layer`、自定义属性）、可预测组合、配方/变体、设计令牌多主题、`fallback` 值、视图转换、MCP 服务器。
- 📦 框架支持：适用于 Solid、Vite、Preact、Svelte、Astro、React Router、Qwik、Vue、Nuxt、Storybook。

---

### [拆分 git 提交](https://blog.gnoack.org/post/git-history-split)

**原文标题**: [Splitting a git commit](https://blog.gnoack.org/post/git-history-split)

通过一条新命令即可轻松拆分 git 提交，告别繁琐操作
- 🔧 使用 `git history split ${REF}` 命令，可逐块选择要放入第一个提交的内容
- 📝 命令会自动打开编辑器，分别填写第一个和第二个提交的说明
- ⏳ 过去拆分提交的旧方法非常繁琐，Stack Overflow 上的传统高赞回答步骤复杂
- 💡 第 20 个回答给出了正确做法，但仅获 2 票，远低于旧方法的 2656 票，好方法常被埋没

---

### [](https://github.blog/open-source/git/highlights-from-git-2-54/#h-rewrite-history-with-git-history)

**原文标题**: [Highlights from Git 2.54 - The GitHub Blog](https://github.blog/open-source/git/highlights-from-git-2-54/#h-rewrite-history-with-git-history)

Git 2.54 正式发布，汇集了 137 位贡献者（其中 66 位是新贡献者）的更新，本文涵盖 2.53 与 2.54 两个版本的亮点：包括新的实验性 `git history` 命令、基于配置的 hook 系统、几何 repacking 成为默认维护策略，以及 `add -p`、`replay`、`log -L`、HTTP 传输、`rebase`、`blame` 等多方面改进。

- 🧪 新增实验性 `git history` 命令，支持 `reword` 和 `split` 操作，无需触碰工作树/索引即可重写历史，甚至可在裸仓库使用，但不支持含合并提交的历史。
- ✂️ `git history split` 通过类似 `git add -p` 的交互界面选择 hunks，将提交拆分为父提交与保留剩余更改的原提交，并自动重写后代分支。
- ⚙️ 配置化 hooks 登场：可在 Git 配置中通过 `hook.<name>.event` 和 `hook.<name>.command` 定义 hooks，支持用户级、系统级与仓库级配置。
- 📋 同一事件可配置多个 hooks，`git hook list` 可查看配置来源；`hook.<name>.enabled=false` 可单独禁用，传统 `$GIT_DIR/hooks` 脚本仍有效且最后运行。
- 📦 `git maintenance run` 默认策略从 `gc` 改为几何 repacking，可增量合并 packfiles 提高效率，并保留 `maintenance.strategy = gc` 选项。
- 🎯 `git add -p` 增强：用 `J`/`K` 导航时会显示各 hunk 是否已处理，新增 `--no-auto-advance` 标志让文件间切换更可控。
- 🔄 `git replay` 持续成熟：默认执行原子引用更新，新增 `--revert` 模式，可丢弃空提交并支持重放到根提交。
- 🌐 HTTP 传输开始处理 429“Too Many Requests”响应，支持 `Retry-After`，新增 `http.retryAfter`、`http.maxRetries`、`http.maxRetryTime` 配置。
- 🔍 `git log -L` 改走标准 diff 管道，首次兼容 `-S`/`-G` pickaxe、`--word-diff`、`--color-moved` 等选项。
- 🧩 增量多包索引（MIDX）新增压缩能力，可合并较小层与关联位图，避免链层数无限增长。
- 📊 `git status` 新增 `status.compareBranches` 配置，可同时对比 upstream 和 push 远程，适应三角工作流。
- 🏷️ `git rebase` 新增 `--trailer` 选项，可简单批量向所有 rebased 提交追加 trailer（如 `Reviewed-by`）。
- 🔏 用已过期 GPG 密钥做的有效签名现在会被视为良好签名，不再以红色误导用户。
- ⚡ `git blame` 新增 `--diff-algorithm` 选项，可指定 histogram、patience、minimal 等 diff 算法。
- 🛠️ 对象数据库（ODB）内部重构为可插拔后端设计，为未来存储后端与更灵活配置打下基础。
- 📥 `git backfill` 支持修订范围与 pathspec 参数，如 `git backfill main~100..main -- '*.c'`，更适合大型部分克隆。
- 🌍 别名配置支持非 ASCII 字符，新增 `[alias "名称"] command = ...` 语法，传统 ASCII 别名仍兼容。
- 🎨 修复直方图 diff 算法在 compaction 阶段可能跨过 anchor 线的问题，输出更紧凑、更符合预期。

---

### [](https://github.com/hulkholden/n64js)

**原文标题**: [GitHub - hulkholden/n64js: An n64 emulator in JavaScript · GitHub](https://github.com/hulkholden/n64js)

n64js 是一个用 ES6 JavaScript 编写的 N64 模拟器，旨在展示现代浏览器性能，目前可运行大量 ROM，兼容性持续改善，并支持多种外设与存储方式。

- 🎮 核心定位：纯 ES6 JavaScript 实现的 N64 模拟器，多数 ROM 可全帧率运行，托管版本见 GitHub Pages。
- 💡 开发动机：作者有约 25 年 N64 模拟器经验，通过 JavaScript 移植挑战自我，并展示浏览器能力。
- 🛠️ 构建与运行：需安装 bun，使用 `bun run build --watch` 编译，本地服务器通过 `python3 -m http.server` 启动，也可直接引用源码版本。
- ✅ 兼容性：截至 2023-09-23，95% 的 n64-systemtest 测试通过；主要失败点包括 64 位内存访问、RDP（HLE 方式）及浮点精度边缘情况。
- ⚠️ 已知问题：周期计数不精准，可能导致 GoldenEye 在 LLE 音频下挂起；图形采用 HLE，多数 ROM 可玩但仍有大量图形缺陷。
- 🌐 浏览器支持：Chrome 表现最佳，Firefox 与 Safari 可运行但较慢，Edge 未测试。
- 🚀 性能表现：在 Apple M2 Max 上多数 ROM 全帧率，LLE 音频模拟是主要性能瓶颈。
- 🧩 实现状态：CPU（cop0/cop1、TLB、周期精度部分）、RSP、控制器（静态/可配置/Gamepad API）；图形 HLE 部分实现（GBI0 基本、GBI1/2 部分，LLE 未实现）；音频 LLE 已实现、HLE 未实现；保存支持 localStorage、导入导出、Mempack、Eeprom、SRAM、FlashRAM。
- 📜 项目历史：源自 1999 年开始的 Daedalus 模拟器，2012 年因打赌而开启 JavaScript 移植。
- 📊 仓库概况：MIT 许可，639 stars、84 forks、1,890 commits，持续维护中。

---

### [](https://hulkholden.github.io/n64js/)

**原文标题**: [n64js - An N64 Emulator in JavaScript](https://hulkholden.github.io/n64js/)

这是一个基于 Web 的 N64 模拟器，支持在浏览器中运行，已在多种现代浏览器上测试，但存在一些图形问题，并提供了详细的键盘控制和项目背景。

- 🎮 n64js 是一款 N64 模拟器，基于 Daedalus 项目，作者是 @HulkHolden
- 🖥️ 在 M2 MacBook Pro 上许多游戏接近全速运行，但存在不少图形问题
- 🌐 支持 Chrome（推荐）、Firefox 和 Safari，Edge 未测试；需要 WebGL，大部分现代 GPU 可用
- ⌨️ 提供完整的 N64 键盘映射，例如 Start 用 A，A 键用 S，B 键用 X，Z 键用 Z，方向键用 T/G/F/H 等
- 🔧 内置调试功能，包括 CPU、RSP、内存、Dynarec、DisplayList、纹理、时间线等详细信息
- 📚 项目起源于作者大学时期的 Daedalus，并由 DaedalusX 团队继续发展
- 🙏 特别感谢 Jan-Christoph Borchardt 对 QWERTZ 键盘映射的改进
- 📄 更多最新状态和已知问题请参阅 GitHub 仓库

---

