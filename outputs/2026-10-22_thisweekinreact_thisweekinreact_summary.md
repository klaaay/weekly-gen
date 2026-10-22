### [GitHub - nobodywho-ooo/nobodywho：NobodyWho 是一个推理引擎，让你能在任何设备上本地高效运行大语言模型。· GitHub](https://github.com/nobodywho-ooo/nobodywho)

**原文标题**: [GitHub - nobodywho-ooo/nobodywho: NobodyWho is an inference engine that lets you run LLMs locally and efficiently on any device. · GitHub](https://github.com/nobodywho-ooo/nobodywho)

NobodyWho 是一个面向任意设备的本地 LLM 推理引擎，主打离线运行、跨平台绑定和高效端侧 AI 能力，支持文本、多模态、语音识别与合成，并基于 Rust、llama.cpp 与 ONNX Runtime 构建。

- 🚀 **核心定位**：可在本地高效运行大语言模型，无需 API Key 或隐藏费用，支持离线使用。
- 🧠 **主要功能**：支持任意聊天 LLM、类型安全的工具调用、多模态图像/音频输入、TTS、STT、语音活动检测，以及从 Hugging Face 或 URL 下载模型。
- 🧩 **跨平台绑定**：提供 Kotlin、Swift、React Native / Expo、Flutter、Python、Godot 等绑定，覆盖桌面、Android、iOS、macOS、visionOS、watchOS 等平台。
- ⚙️ **底层架构**：核心由 Rust 实现，文本推理依赖 llama.cpp，语音相关能力依赖 ONNX Runtime，并通过 Vulkan / Metal / CUDA / CPU 加速。
- 📱 **平台限制**：Godot 暂不支持 iOS 导出；Windows ARM64 暂不支持；暂无 Web 导出。
- 💾 **硬件要求**：推理优先使用 GPU，否则回退 CPU；可用内存建议约为模型文件的 2 倍，8 GB 可流畅运行约 2 GB 以下模型，16 GB 以上更适合更大模型。
- 📲 **移动端要求**：iOS 建议 iPhone 11 或更新、4 GB RAM 以上；Android 建议 Snapdragon 855 / Adreno 640 / 6 GB RAM 或更好。
- 🧾 **模型支持**：兼容 GGUF 格式模型，可使用 `hf:owner/repo:QUANT`、HTTPS URL 或本地路径；推荐用约 330 MB 的 Qwen3 0.6B 快速验证集成。
- ⚡ **快速开始**：Python 可通过 `pip install nobodywho` 使用；其他平台也提供对应包管理与示例代码。
- 🖥️ **本地服务器**：提供实验性的 OpenAI Chat Completions API 兼容服务器，默认监听 `http://127.0.0.1:8888`。
- 📚 **文档与社区**：官方文档位于 `docs.nobodywho.ooo`，并提供 Discord、Matrix、Issues、Discussions 等支持渠道。
- ⭐ **项目热度**：约 1.6k Stars、97 Forks、2,097 次提交，采用 EUPL-1.2 许可证。
- 📜 **许可证说明**：可用于专有和商业项目且免费，但若分发修改后的本仓库代码，需开源相应修改；不允许制作专有 Fork。

---

### [关于编写智能体技能，没人告诉你的那些事](https://newsletter.posthog.com/p/what-nobody-tells-you-about-writing?utm_source=twir&utm_campaign=oct21)

**原文标题**: [What nobody tells you about writing agent skills](https://newsletter.posthog.com/p/what-nobody-tells-you-about-writing?utm_source=twir&utm_campaign=oct21)

PostHog 团队总结编写 agent skills 的经验：agent 每次对话都会“失忆”，技能应写一次、按需加载，并保留 agent 自主解决问题的空间；同时要防止技能腐烂，只给高价值、重复且缺少上下文的流程建技能。

- 🧠 背景：PostHog 已发布 226 个内部技能、代码库有 187 个 SKILL.md，技能用于避免 agent 反复重新发现代码库与工作流。
- 🧭 渐进披露：好技能是“路由器”，名称和描述说明“何时用”，主文件再链接参考与脚本，避免上下文过载和选错技能。
- 🎯 技能不是纯代码：应精确目标、完成标准、约束和不可推导上下文；对步骤、失败处理、运行时细节保持模糊，避免过度规定。
- 🔗 防止腐烂：稳定结构手写，易变内容引用单一事实源（如 docs/URL）；从稳定基础重新生成，而不是不断打补丁。
- 🏭 可规模化：PostHog 用 context mill 做来源、组装、交付流水线，生成 120+ 个集成与使用技能。
- ❓ 多问少命令：问 agent “能帮什么/需要什么/上次运行如何改进”，利用它掌握的工具体系与失败信息提升技能。
- 🧹 不是一切都值得技能：优先重复、默认做不好、需模型外上下文、可自动运行的任务；先用 agent 试做，避免不必要的上下文与维护成本。
- 📝 实践提示：可让 agent 扫描过去 30 天工作，找出值得打包的重复手动流程并生成候选清单。

---

### [React 服务器组件中的未认证远程代码执行 · 安全公告 · react/react · GitHub](https://github.com/react/react/security/advisories/GHSA-xqc2-xf4c-x3h3)

**原文标题**: [Unauthenticated Remote Code Execution in React Server Components · Advisory · react/react · GitHub](https://github.com/react/react/security/advisories/GHSA-xqc2-xf4c-x3h3)

该安全公告披露 React Server Components 存在未认证远程代码执行漏洞（GHSA-xqc2-xf4c-x3h3），严重等级为 Critical，CVSS v4 评分为 9.5/10，建议受影响用户立即升级修复版本。

- 🚨 漏洞可导致远程代码执行，攻击者可通过构造恶意载荷利用支持 React Server Components 的框架。
- 📦 受影响 npm 包包括 `react-server-dom-webpack`、`react-server-dom-parcel`、`react-server-dom-turbopack`。
- 🔢 受影响版本为 19.0.0–19.0.8、19.1.0–19.1.9、19.2.0–19.2.8 和 19.3.0。
- ✅ 修复版本为 19.0.9、19.1.10、19.2.9 和 19.3.1，相关补丁已回移植。
- ⚠️ 该漏洞仅影响极少数场景：响应传输多个 typed arrays，且其中包含攻击者可控值。
- 🛡️ 如果应用 React 代码不使用服务器，或未使用支持 React Server Components 的框架、打包器或插件，则不受影响。
- 📅 公告发布于 2026 年 10 月 14 日，漏洞发现者致谢为 evolutionstorm。
- 🧾 当前无已知 CVE ID，也未分配 CWE；CVSS 指标显示攻击向量为网络、复杂度低、无需权限且无需用户交互。

---

### [Next.js 上游漏洞安全更新 | Next.js](https://nextjs.org/blog/nextjs-security-update-october-14-2026)

**原文标题**: [Next.js Security Update for Upstream Vulnerabilities | Next.js](https://nextjs.org/blog/nextjs-security-update-october-14-2026)

2026年10月14日，Next.js 发布安全更新，修复来自上游依赖的多个漏洞，涉及远程代码执行和拒绝服务风险。官方已在 v16.4.1（Active LTS）和 v15.5.28（Maintenance LTS）中提供修复，建议所有用户尽快升级依赖。

- 🚨 **严重漏洞一**：使用 App Router 与 Cache Components 时，若 `use cache` 函数返回多个 typed arrays，可能导致未认证远程代码执行；无已知缓解措施，应立即升级。
- 🖼️ **严重漏洞二**：Image Optimization API 处理 SVG 时，因上游库内存相关问题，在 glibc Linux 上可能导致远程代码执行；临时缓解措施是确保 Next.js 使用的 `sharp` 版本为 0.35.5 或更高。
- ⚙️ **高危漏洞三**：使用 App Router 且至少有一个 Server Action 的应用，可能遭精心构造请求导致 CPU 过度占用，进而引发拒绝服务；使用 Pages Router 或未使用 Server Actions 的应用不受影响。
- 📦 **修复版本**：升级到 Next.js v16.4.1 或 v15.5.28，以确保包管理器自动提供修复后的依赖版本。
- 🛡️ **安全计划**：Vercel 通过 Open Source Bug Bounty 与研究人员合作保障 Next.js 等开源框架安全；相关问题可联系 security@vercel.com。

---

### [React 基金会聚会：伦敦 · Luma](https://luma.com/g9q690i2)

**原文标题**: [React Foundation Meetup: London · Luma](https://luma.com/g9q690i2)

React Foundation 将在伦敦 Meta Kings Cross 举办 React & React Native 社区聚会，活动包括交流、披萨与饮品、三场技术分享及社交环节，适合新手和资深开发者参加，需提前注册，目前约 65 人报名。

- 🗓️ 活动名称：React Foundation Meetup: London，聚焦 React 与 React Native 社区交流。
- 📍 活动地点：Meta Kings Cross，地址为 11-22 Canal Reach, London N1C 4DB, UK。
- 🤝 主办与合作方：React Foundation、Expo、React Native London、Software Mansion、Callstack、Amazon Developer 等；合作伙伴还包括 Meta、Microsoft、Vercel、Huawei。
- 🍕 18:00 开门，18:00-18:45 提供披萨与饮品。
- 🎤 18:45 Tomasz Zawadzki（Software Mansion）分享 “What a Time to Be Alive!”
- 🎤 19:10 Szymon Chmal（Callstack）分享 “The React Native Software Factory”；19:10-19:20 休息。
- 🎤 19:20 Tomasz Sapeta（Expo）分享 “Expo Modules 2.0”。
- 🌐 19:40 开始 Networking 社交环节。
- 👥 已有 65 人报名参加，包括 Luke Howsam、Ayo Ahmed 等；需在活动页面注册加入。

---

### [](https://thisweekinreact.com/newsletter/300#react:~:text=React%20Foundation%20news)

**原文标题**: [This Week In React #300: Next.js, TanStack, React Foundation, Compiler, Ink, Streamdown, Shaders | Skia, Live Activities, Lucent, Voltra, Apex, Coinbase, Stim Desktop, Unistyles | TC39, e2e, Effect, Remix, h3, SvelteKit, TypeScript | This Week In React](https://thisweekinreact.com/newsletter/300#react:~:text=React%20Foundation%20news)

本期《This Week In React》迎来第300期，重点覆盖 Next.js 16.4 与 TanStack 多个 1.0 发布、React Foundation 最新动态，以及 React Native 生态的重大变化：Skia 3.0 发布，Shopify 与 Coinbase 相继宣布迁离 React Native；同时还有 e2e、Effect 4.0、Remix v3 等框架与工具更新。

- 🎉 第300期里程碑：感谢读者长期支持；本周重点包括 Next.js、TanStack 大版本、React Foundation 动态和移动端重大发布。
- ⚛️ Next.js 16.4：Cache Components 日趋成熟并推荐所有应用使用，create-next-app 默认启用，v17 将成为默认；新增 Partial Prefetching、ensureStatic、navigation() 预取控制及 Agent 辅助升级；React 19.3 带来稳定 View Transitions、Fragment Refs 和 browser() API。
- 📊 TanStack：Charts 1.0 正式稳定，主打小体积、快速更新、可组合和类型安全；Markdown + Highlight 1.0 提供轻量快速的 Markdown 渲染与语法高亮。
- 🏛️ React Foundation：Barbara Markiewicz 出任社区总监；11月10–12日将在伦敦举办 Contributors Summit，邀请制但生态贡献者可自荐；11月4–5日加纳 React Conf 被文中称为首个由基金会官方组织的 React 大会。
- 🔐 TanStack Start 安全更新：修复 CVE-2026-102989，涉及评分 9.3 的 XSS 漏洞。
- 📱 React Native Skia 3.0：基于 Skia Graphite 重构，支持默认多线程、与 WebGPU 对称、Three.js 零拷贝互操作、视频/摄像头 GPU 导入和 WebGPU Lottie；Android minSDK 提升至 26，且仅支持 Vulkan。
- 🚀 Shopify 与 Coinbase 相继宣布迁移离开 React Native；Shopify 仍将在年底前赞助 Skia；相关讨论聚焦新架构迁移不足、双端原生同步变易等趋势。
- 🧠 Callstack 推出 Apex：面向 React、React Native 和 Next.js 的代理式编码模型，现已正式可用。
- 🧪 测试与框架：e2e 推出自然语言与确定性 API 混合的代理式端到端测试框架；Effect 4.0 核心重建、无依赖、包体更小并获得长期支持。
- 🧰 其他发布：Remix v3 首个稳定版及 Remix Jam 2026；h3 2.0、SvelteKit 3.0、pnpm 12.9/12.10；TC39 第116次会议推进 Composites、Iterator 新方法、export defer 等；TypeScript 7.1 迭代计划支持 LSP 等。
- 📦 移动与前端工具更新：Ink 8.0、Streamdown 2.7、Stim Desktop 0.1、Unistyles 3.5.0、Voltra 2.4、Maestro CLI 2.11、Nitro Markdown 0.14 等，覆盖 CLI、AI Markdown 流、设备调试、主题与原生能力。

---

### [添加 <Link prefetch="navigation">（作者：acdlite](https://github.com/vercel/next.js/pull/99871)

**原文标题**: [Add <Link prefetch="navigation"> by acdlite · Pull Request #99871 · vercel/next.js · GitHub](https://github.com/vercel/next.js/pull/99871)

Next.js 仓库合并 PR #99871，新增 `<Link prefetch="navigation">`。该 PR 为 Link 的 `prefetch` 属性增加 `"shell"`、`"prefetch"`、`"navigation"` 三个选项；其中 `"navigation"` 可越过 `await navigation()` 边界，强制预取导航阶段内容，适合用户很可能点击的链接。命名与 v16.4 的 `await prefetch()`、`await navigation()` API 阶段对应。

- 🚀 PR #99871 已由 acdlite 合并到 canary，包含 6 个提交，120 项检查通过，lubieowoce 批准。
- 🧩 `prefetch="shell"` 等同于未设置 prefetch，`prefetch="prefetch"` 等同于 `prefetch={true}`。
- ⚡ 新增 `prefetch="navigation"`，可覆盖 `await navigation()` 对预取的限制，强制预取到导航阶段。
- 🖱️ 适用于高概率被点击的链接，以更高预取成本换取更完整的导航预取。
- 🗄️ 在 Partial Prefetching 下，路由器通过新的运行时预取请求填充缓存直到 navigation 阶段；非 Partial Prefetching 下行为等同 `prefetch={true}`。
- 🔧 配套改动包括命名预取 header 值、记录静态预取完成阶段、增加 `ShouldAttemptStaticNavigation` 提示，并让 `unstable_dynamicOnHover` 在 Partial Prefetching 路由上获得该预取。
- 🧪 改动包含测试与类型更新，标签为 tests、type: next。

---

### [](https://react.dev/reference/dev-tools/react-devtools-cdt-mcp)

**原文标题**: [React DevTools for agents – React](https://react.dev/reference/dev-tools/react-devtools-cdt-mcp)

该文档介绍实验性工具 `react-devtools-cdt-mcp`：它把 React DevTools 的组件树、Props、Hooks、Owner、源码位置和渲染耗时能力暴露给通过 Chrome DevTools MCP 操作浏览器的 AI 编码代理，帮助代理理解组件状态、来源与性能；它需在 React 初始化前导入，且仅建议用于开发环境。

- 🧪 该功能属于 React 实验特性，基于 Chrome DevTools MCP 的实验性第三方开发者工具 API，工具与输出可能随版本变化。
- 🧩 `react-devtools-cdt-mcp` 是运行在页面内的浏览器库，不是 MCP server，不需要加入 MCP 客户端配置；只需配置 Chrome DevTools MCP。
- 🤖 它为 AI 编码代理提供类似 React DevTools 的视图：组件树、Props、Hooks、Owner、源码位置和渲染时序。
- ⚙️ 安装方式为 `npm install --save-dev react-devtools-cdt-mcp`，并在应用入口文件最顶部、任何 `react-dom` 导入之前导入 `react-devtools-cdt-mcp/register`。
- 🚨 必须在 React 初始化前加载；它会像 DevTools 扩展一样让 React 报告每次 commit，可能拖慢应用，因此只应包含在开发构建中。
- 🛠️ 注册的 `react` 工具组包括组件树快照、按名称查找、按 uid 或 DOM 元素查询、父级与 Owner 栈、源码位置、性能分析开始/停止、trace 概览和 commit 报告。
- 🆔 组件使用类似 `"r5"` 的短 uid 标识，跨工具和重渲染保持稳定，但页面刷新后会失效，需要重新获取。
- 📦 每个工具返回可序列化的普通对象；失败时返回带 `error` 信息的对象；也可手动调用 `register(target?)` 安装 hook，并返回 `facade` 与 `unregister`。
- 🔍 排障要点：确认已启用第三方开发者工具且页面导入了 register；组件树为空通常是导入太晚；源码位置/Owner 栈为空通常是生产构建；浏览器外导入会报错，应仅在客户端代码中使用。

---

### [使用 Next.js 16.4 改善 v0 中的导航体验 | Next.js](https://nextjs.org/blog/improving-navigation-experience-in-v0-with-nextjs-16-4)

**原文标题**: [Improving navigation experience in v0 with Next.js 16.4 | Next.js](https://nextjs.org/blog/improving-navigation-experience-in-v0-with-nextjs-16-4)

Vercel 团队介绍了如何利用 Next.js 16.3/16.4 的 Partial Prefetching 与 `next-partial-prefetching-optimizer` Skill，将 v0 中模板、设置、项目等页面的导航体验改得更接近单页应用：点击前预取可复用内容，返回时复用缓存，同时通过 `instant()` 测试和成本指标控制预取范围。

- 🎯 背景：此前仅 `/chat` 实现 instant 导航，其他页面常出现加载骨架，返回已打开页面时也会重复加载。
- ⚡ Next.js 16.3 引入 Partial Prefetching；16.4 增加缓存内容加载时机控制，并提供用于优化预取内容的 Skill。
- ✅ `create-next-app` 默认启用 Cache Components 与 Partial Prefetching；v0 先全局启用，再逐步重构各路由。
- 🧪 使用 `@next/playwright` 的 `instant()` 锁定点击行为，断言点击前目标 UI 已可见且不再显示大范围骨架屏。
- 🔁 Skill 引导代理循环：选择导航与目标 UI → 写 `instant()` 测试 → 加断言并确认失败 → 用缓存和预取重构 → 重跑直至通过，测试留在 CI 防回归。
- 🧩 `/templates/[id]`：公开模板数据用 `'use cache: remote'` 缓存，配合 `cacheLife()`、`cacheTag()`/`revalidateTag()`，并对链接使用 `prefetch={true}`。
- 🖱️ 大网格优化：最初对所有卡片预取导致 `/templates/[id]` 预取请求增 2.9 倍；改为 hover、focus、touch 的“用户意图”触发，避免无谓预取。
- 🔐 `/settings`：个性化内容用 `'use cache: private'` 存浏览器，`scope` 纳入缓存键隔离账户/团队；Advanced 缓存 5 分钟，写操作后用 `updateTag()` 立即失效。
- 🧭 `/projects`：项目标题和 Production Deployment 提前预取；Recent Chats 用 `navigation()` 延迟到导航后加载，并缓存供返回复用。
- 📊 结果：整体日成本降 2.9%；共享 Runtime Cache 支出增至 4.3 倍、约每日增加 3.44 美元；请求服务相关成本降 14.4%；`instant()` 测试数量翻倍。
- 🛠️ 可安装 Skill：`npx skills add vercel/next.js --skill next-partial-prefetching-optimizer`；前提是已采用 Cache Components 与 Partial Prefetching。
- 💬 团队将全应用指标视为“重构后没有更贵”的确认，而非单纯节省，因为同期流量和部署变化也会影响数据。

---

### [构建一个人人可用的可筛选菜单 · Base UI](https://base-ui.com/blog/building-a-filterable-menu)

**原文标题**: [Building a filterable menu that works for everyone · Base UI](https://base-ui.com/blog/building-a-filterable-menu)

概述：本文介绍 Base UI 在实现可筛选菜单时，如何兼顾键盘、屏幕阅读器和子菜单交互。核心方案是采用 dialog、searchbox 与 menu 语义，而不是 combobox，并通过 `Menu.FilterProvider` 让整个菜单选择启用筛选行为，同时修复普通菜单中的若干无障碍问题。

- ⌨️ 添加输入框会影响整个菜单交互：按键既用于导航又用于编辑文本，焦点移动可能打断输入，屏幕阅读器对弹窗的预期也会变化。
- 🧭 未采用 combobox 或 `aria-autocomplete`：菜单项用于执行命令，并非填写值；并且菜单与输入框同时可见，不存在可展开、收起的建议弹窗。
- 🪟 采用 dialog 包含搜索框和菜单，触发器设置 `aria-haspopup="dialog"`，明确告知用户打开的是可探索的对话框上下文。
- 🔎 输入框使用 `role="searchbox"`，而没有使用 `type="search"`，以避免浏览器自带清除按钮，并允许应用自行加入 `Menu.Clear`。
- ⬇️ 键盘用户可从输入框按 ↓ 高亮匹配项，用方向键浏览，按 Enter 执行；从最后或第一项继续按方向键会回到输入框，并用 `data-highlighted` 显示状态。
- 🏠 Home/End 会根据上下文变化：输入为空且菜单项高亮时移动到首项或末项；焦点回到输入框时移动光标；有查询时始终移动光标。
- 📂 子菜单焦点处理会区分意图：键盘按 → 进入子菜单时立即聚焦其输入框；鼠标悬停仅预览，指针进入子菜单后才聚焦输入框。
- 🚪 菜单不困住焦点，Tab 可离开并关闭菜单；`Menu.Clear` 不进入 Tab 顺序，键盘和屏幕阅读器用户可直接删除输入文本。
- 🐞 同时修复普通 Menu 的无障碍问题：VoiceOver 重复播报、Shift+Tab 焦点丢失、iPhone VoiceOver 子菜单返回后未关闭、TalkBack 无法关闭子菜单等。
- 🧩 使用 `Menu.FilterProvider` 整体启用筛选：保留现有菜单部件和样式，触发器可在输入框挂载前声明 dialog，非筛选菜单不会加载额外筛选代码。

---

### [智能体时代的纯 UI | Matt Rothenberg](https://mattrothenberg.com/notes/pure-ui-agentic-era/)

**原文标题**: [Pure UI in the Agentic Era | Matt Rothenberg](https://mattrothenberg.com/notes/pure-ui-agentic-era/)

文章围绕“纯 UI”理念，讨论智能体大量编写前端代码后，如何确保 UI 变更覆盖所有关键状态：核心公式是 `ui = fn(state)`，但真实应用状态分散在 hooks、context、布局和功能开关中；智能体常只验证当前账号的状态就宣布完成，导致 Viewer 仍看到 Delete 按钮等问题。作者主张把与展示相关的状态显式提升到页面或视图边界，并用 Storybook、Playwright 和状态网格并列渲染组合，让评审者看清智能体到底检查了哪些状态。

- 🧮 纯 UI 的核心规则：UI 应尽可能成为应用状态的纯函数，即 `ui = fn(state)`；开发时应把界面看作某一时刻的数据快照，而不是直接修改 DOM 的事件处理器。
- 🧠 智能体写 UI 的风险：智能体可能只基于单一账号、单一角色验证页面，却以同样自信报告“完成”，未必考虑 Viewer、Free、逾期账单、功能开关等组合。
- 🧵 状态往往很分散：角色可能来自 `useSession()`，套餐来自全局 context，账单来自布局包装器，beta 开关来自全局 flag，单看组件无法知道页面可占据哪些状态。
- 🐞 典型案例：给函数表添加删除操作时，智能体只以 Owner 身份检查；结果 Viewer 页面标题显示“View only”，表格却仍出现 Delete 按钮。
- 🧪 测试只覆盖被选中的状态：若组件通过 hooks 读取状态，测试需逐个 mock；若展示状态是显式输入，则可直接渲染选定组合并断言。
- 📚 Storybook 与 Playwright 可配合 Pure UI：前者用于渲染选定组件状态，后者验证这些状态在真实应用中可达，但仍需人决定哪些角色、账单、开关和数据组合重要。
- 🧱 重构方向：把与展示相关的状态移到页面或视图边界，再作为参数传给子组件，使组件 API 成为“哪些输入会改变输出”的可工作清单。
- 🖼️ 用状态网格暴露遗漏：示例中 role、plan、billing、beta 各有两个值，可生成 16 个屏幕；并列渲染比设置 16 个账号更快，也更容易发现 Viewer 仍显示删除按钮的问题。
- 🔍 合并前追问智能体看到了什么：一个账号只是一条路径，不是整个屏幕；评审关键状态不能保证万无一失，但能提升发布信心，并在客户之前发现尴尬问题。

---

### [](https://reactrouter.com/changelog#v850)

**原文标题**: [CHANGELOG.md  | React Router](https://reactrouter.com/changelog#v850)

该文档是 React Router 的完整版本变更日志与文档导航，覆盖 v7.0.0 至最新 v8.5.0，集中说明各版本的新功能、修复、稳定性改进、破坏性变更及升级注意事项。

- 📚 发布说明集中管理：官方将 v7.0.0 以来的发布说明放在同一文件，便于搜索和查看完整内容；v6 及更早版本另有入口。
- 🧭 文档体系完整：包含 Framework/Data/Declarative 模式、API Reference、Tutorials、How-Tos、Explanations、Community 等章节。
- 🆕 v8.5.0 重点：弃用 React Router 自带视图过渡 API，推荐 React 19.3+ 的 `<ViewTransition>`，旧 API 将在 v9 移除。
- 🧪 v8.5.0 不稳定能力：新增 API-only 模式、`unstable_fetch` 自定义请求、应用控制路由发现，支持 CDN 静态 HTML 搭配运行时数据服务。
- ⚡ v8.4.0 改进：细化内部路由上下文以减少无关重渲染；Data Mode 可选更高效路由匹配，并新增参数校验能力。
- 🧵 v8.3.x 更新：改进不稳定 RSC 入口，支持客户端版本、子资源完整性、CSP nonce；修复路由、会话与流式响应相关问题。
- 🌐 v8.2.0 变化：非 Node 运行时默认使用 Web Streams 服务端入口；Node 应用可通过 flag 选择 `renderToReadableStream`。
- 🤖 v8.1.0 亮点：`create-react-router` 支持默认安装 Agent Skill；插桩结果增加 URL、路由 pattern、params、statusCode 等元数据。
- 🚨 v8.0.0 重大变更：最低 Node 22.22、React 19.2.7、Vite 7；改为 ESM-only；移除 `react-router-dom` 和 `meta` 的废弃 `data` 字段；多个 future flags 成为默认行为。
- 🛠️ v7 系列演进：逐步稳定 middleware/context、RSC、路由发现、类型安全 `href`、预渲染、SPA fallback、可观测性与视图过渡等能力。
- 🔐 安全与修复：多个版本包含 CSRF、XSS、开放重定向、会话文件并发写入、IPv6 Host 处理、流式响应崩溃等修复。

---

### [发布 v10.0.0-alpha.6：WebGPU 优先 · pmndrs/react-three-fiber · GitHub](https://github.com/pmndrs/react-three-fiber/releases/tag/v10.0.0-alpha.6)

**原文标题**: [Release v10.0.0-alpha.6: Going WebGPU First · pmndrs/react-three-fiber · GitHub](https://github.com/pmndrs/react-three-fiber/releases/tag/v10.0.0-alpha.6)

R3F v10.0.0-alpha.6 发布，这是 v10 目前最大的 alpha，核心变化是默认转向 WebGPU，并对渲染器、TSL hooks、多 Canvas、物理时间步、React 19 支持和 ESLint 迁移工具做了系统性升级。

- 🚀 v10.0.0-alpha.6 是迄今最大的 alpha，自 alpha 5 以来包含 200+ 提交，明确走“WebGPU 优先”路线。
- 🖥️ 默认渲染器改为 WebGPURenderer，可回退 WebGL2；使用自定义 GLSL 或旧 WebGL 库时，从 `@react-three/fiber/legacy` 导入 `Canvas`。
- 📦 核心不再直接导入 three，各渲染器独立打包，默认入口只加载 WebGPU，legacy 入口只加载 WebGL；`@react-three/fiber/webgpu` 已废弃。
- 🧠 类型随入口变化：默认入口的 hooks 按 WebGPURenderer 类型，legacy 按 WebGLRenderer 类型；同时支持双渲染器的库可用 `@react-three/fiber/extension`。
- 🧩 TSL hooks 移至新包 `@react-three/tsl`，包括 `useUniforms`、`useLocalNodes`、`useRenderPipeline` 等，并改进类型注册、依赖追踪和资源重建。
- 🎛️ 多 Canvas 共享渲染器简化为 `primary` 和 `share` 属性，`scheduler` 也成为 Canvas 属性。
- ⏱️ physics 阶段改为固定 1/60 秒时间步，保证不同刷新率下物理速度一致；可用 `state.overstep` 做插值。
- ⚛️ 更好支持 React 19 的 StrictMode、Fast Refresh 和 `<Activity>`，卸载立即清理，运行时设置不被重渲染覆盖，并适配高 DPI 屏幕。
- 🛠️ 多数材质属性变更不再需要手动 `needsUpdate`，如图片背景、`frameloop="demand"` 重绘等问题得到修复。
- 🧹 `state.gl` 保留为 `state.renderer` 的别名；`onUpdate` 被移除；`<Canvas shadows>`、`primaryCanvas`、`scheduler` 等 API 有迁移变更。
- 🧪 `@react-three/eslint-plugin` 升级到 1.0.0-alpha.6，规则从 2 条扩展到 20 条，并提供 v9 迁移配置和 `eslint --fix`。
- 🔬 CI 新增基于 Dawn 的真实 WebGPU 设备像素测试，不再只依赖 mock 或手工浏览器验证。
- ⚠️ 破坏性变更包括默认 WebGPU、TSL hooks 新包、shadows 配置方式、physics 固定步长、`useRenderPipeline` 卸载行为等。
- 📥 安装命令为 `npm install @react-three/fiber@alpha @react-three/tsl@alpha three@latest`，要求 three >= 0.185.0、React >= 19.0 < 19.4。

---

### [Hydrogen 2026-10 现已发布](https://hydrogen.shopify.dev/update/hydrogen-2026-10-now-available)

**原文标题**: [Hydrogen 2026-10 now available](https://hydrogen.shopify.dev/update/hydrogen-2026-10-now-available)

Hydrogen 2026-10 已正式发布，核心变化是从专用框架转型为可接入任意 JavaScript 框架的电商库，让开发者无需迁移平台即可把 Shopify 商务能力加入现有项目。

- 🚀 2026 年 10 月 14 日正式发布，开发者预览自 6 月以来已基于反馈发布七个版本。
- 🧩 最大亮点是“不再是大事”：Hydrogen 现在兼容任意 JavaScript 框架，可直接加入现有应用，无需重新搭建平台。
- 🛒 内置购物车、变体选择、本地货币价格、符合同意要求的分析、Shop Pay 和客户登录等电商能力。
- ⚛️ 提供 React Router 和 Next.js 起步模板，可部署到任何地方，包括仍免费的 Oxygen。
- 🤖 包含 20 项面向编码代理的 skills，可让代理搭建首页、集合、搜索、商品、购物车、账户页面并做冒烟测试。
- 🧪 可通过 `npx @shopify/hydrogen@latest setup` 在现有项目中试用，并让代理执行“Set up my store with Shopify”。
- 🔗 使用与 Liquid 主题相同的标准 storefront actions，应用、店铺 UI 和代理可共享同一购物车契约。
- 🌐 支持购物代理：在支持 WebMCP 的浏览器中，代理可搜索目录、更新购物车，并在买家确认后通过 `complete_checkout` 提交订单。
- 🔄 旧版 Hydrogen 店铺继续可用；准备迁移时可借助 migration skill 保留页面和路由，仅替换商务代码来源。
- 📦 入门方式包括本地运行 setup、从 Shopify 后台部署 React Router 模板到 Oxygen，或克隆 Vercel 维护的 Next.js 店铺模板 Vercel Shop。

---

### [2026年10月 - Trace、代码块和 AI 元素 - shadcn/ui](https://ui.shadcn.com/docs/changelog/2026-10-ai-elements)

**原文标题**: [October 2026 - Trace, Code Block and AI Elements - shadcn/ui](https://ui.shadcn.com/docs/changelog/2026-10-ai-elements)

本次更新发布了 Trace、Code Block 两个新组件，以及基于 shadcn/ui 组件构建的 AI Elements 智能体界面模式，进一步完善了聊天与智能体交互界面的组件体系。

- 🧩 Trace 用于展示智能体执行步骤，每条步骤包含图标、标题、描述与状态，支持展开、跳转、弹窗、嵌套，以及 running、error、pending 状态与 shimmer 效果。
- 💻 Code Block 用于展示代码、终端输出、日志与 diff，支持标题栏、操作按钮、行号、自动换行、差异与高亮行，并提供适合工具输出的小尺寸样式。
- 🎨 Trace 与 Code Block 已支持 Base UI、React Aria、Radix，并覆盖全部八种样式。
- 🧱 结合此前发布的聊天组件，可覆盖完整智能体界面，包括 Message Scroller、Message、Bubble、Trace、Code Block、Marker、Attachment、Questionnaire 等。
- 🤖 AI Elements 提供 21 种智能体界面模式，如 Chat、Prompt Input、Reasoning、Tool、Plan、Subagent 等，无需安装包，直接复制组合代码到项目即可。
- 📝 每个 AI Elements 页面都提供 Markdown 版本，便于让编码智能体直接读取并集成对应模式。
- 🔁 AI Elements 将取代并逐步弃用 AI SDK Elements，但已复制到项目中的旧组件仍可继续使用，无需立即迁移。
- 🛠️ 迁移时可通过各模式页面提供的迁移提示，让编码智能体基于 Trace、Code Block 等 shadcn/ui 组件重建包装层，且导出名称与 props 保持不变。
- 📚 官方文档还提供从 AI SDK Elements 迁移的对照说明，未重建的元素可通过提交 issue 获得支持。

---

### [博客 | Vinext](https://vinext.dev/blog)

**原文标题**: [Blog | Vinext](https://vinext.dev/blog)

Vinext 团队博客发布版本更新、深度解析与工程进展，核心项目是在 Vite 上重新实现 Next.js API 表面。近期四个版本持续聚焦性能优化、缓存机制、Cloudflare Workers 兼容性与开发体验。

- 📝 博客内容涵盖发布说明、技术深潜和工程更新，介绍 Vinext 在 Vite 上重建 Next.js API 表面的工作。
- 🚀 2026-10-20 Vinext 1.3：减少每页请求数、加快冷启动并推出 Worker Previews；支持按路由分组客户端组件、按路由 SSR 预加载、仅哈希构建产物名、使用 path-to-regexp 做 next.config 路由匹配，阅读约 9 分钟。
- 🛡️ 2026-10-14 Vinext 1.2：public/ 文件中间件可在 Workers 运行、缓存键更严格、生态兼容性更广；支持 Pages ISR 全文档再生和 next/dynamic 对齐，阅读约 6 分钟。
- ⚡ 2026-10-08 Vinext 1.1：提升构建与开发启动速度；在 Cloudflare 上为 revalidateTag 和 “use cache” 提供后台再验证、压缩 RSC 响应、减少客户端导航时的服务器工作，阅读约 3 分钟。
- ✅ 2026-09-28 Vinext 1.0：稳定 API 与缓存预热；缓存遵循 Next.js 规则、为 Cloudflare Workers 提供持久缓存、类型化 Cloudflare 配置，并支持 OpenTelemetry 追踪，阅读约 3 分钟。

---

### [宣布 Mutative 2.0：更快的更新和更安全的补丁 | Mutative](https://mutative.js.org/blog/releases/2.0/)

**原文标题**: [Announcing Mutative 2.0: Faster Updates and Safer Patches | Mutative](https://mutative.js.org/blog/releases/2.0/)

Mutative 2.0 保持 1.x 的 API，不重命名或删除函数与选项，但通过底层优化显著提升不可变更新性能，并修复补丁、集合、构建与类型等多处边界行为，因此作为大版本发布。

- 🚀 **核心机制不变**：仍以“可变写法”更新草稿，返回新状态；只复制被修改路径，未变部分与旧状态共享。
- ⚡ **性能大幅提升**：数组 `shift()`、`splice()`、`reverse()` 等改为原生移动；基准中几何平均比 Immer 11.1.18 快 3.6 倍，比 Mutative 1.3.0 快 4.3 倍。
- 🧩 **集合与快照更省工**：Set/Map 草稿减少代理操作；`current()` 更高效复制变更数组；`apply()` 借助原生数组方法加速。
- 🛠️ **补丁行为更可靠**：补丁顺序对齐 Immer，修复排序、Set 变更、`-0`、数组伸缩等场景下的回放问题，并保留 Set 中多个变更。
- 🔒 **`apply()` 更严格**：拒绝以 `__proto__` 结尾的路径，Set 项只能按索引读取，Map 键不做字符串转换；`mutable: true` 下替换根状态会抛错。
- 🧊 **自动冻结变化**：启用 `enableAutoFreeze` 后会冻结 Map/Set 实例本身；返回的新状态若含草稿会被搜索处理，`rawReturn()` 可跳过搜索。
- 📦 **构建更可预测**： bundler 与 Node.js 通过 `process.env.NODE_ENV` 选择开发/生产构建；目标语法升至 ES2018；生产错误使用编码提示。
- 🧪 **开发检查更多**：捕获草稿作 Map 键、非字符串路径键、大量未变更草稿搜索等问题；异步 recipe 类型改为 `Promise<State>`，`apply()` 支持 `enableAutoFreeze` 并返回 `Immutable<State>`。
- 📉 **存在权衡**：`create()` 单独约 7.9 kB，比 1.3.0 增 2.1 kB；自动冻结下大量字段类实例更新可能慢于 Immer，手写 reducer 多数仍更快。
- 🔄 **升级注意**：1.3.0 是最后 1.x 版本；需同时用开发/生产构建测试，定义 `NODE_ENV`，更新补丁快照、自动冻结、草稿生命周期、数组 getter 与类型检查相关代码。
- 🔁 **从 Immer 迁移**：主要重命名为 `produce()`→`create()`、`applyPatches()`→`apply()` 等；无插件体系；因默认不冻结，依赖冻结状态时需启用 `enableAutoFreeze: true`。

---

### [发布 v11.2.0 · immerjs/immer · GitHub](https://github.com/immerjs/immer/releases/tag/v11.2.0)

**原文标题**: [Release v11.2.0 · immerjs/immer · GitHub](https://github.com/immerjs/immer/releases/tag/v11.2.0)

Immer 发布 v11.2.0，主要新增了用来判断 draft 是否被修改的 `isModified` 工具函数。
- 📦 版本：v11.2.0，发布日期为 2026-10-20。
- 🧰 新功能：`utils` 模块新增 `isModified` 辅助函数，用于检查 draft 是否已被修改（#1328，b05ac6c）。
- 🔄 变更：该版本包含自上一版本以来合并到 `main` 的 11 个提交。
- ✅ 发布提交带有 GitHub 验证签名（GPG key ID：B5690EEEBB952194）。
- 📊 仓库页面显示当前有 29 个 Issues、17 个 Pull requests。

---

### [发布 2.4.0 · bvaughn/react-window · GitHub](https://github.com/bvaughn/react-window/releases/tag/2.4.0)

**原文标题**: [Release 2.4.0 · bvaughn/react-window · GitHub](https://github.com/bvaughn/react-window/releases/tag/2.4.0)

bvaughn/react-window 发布 2.4.0（10 月 18 日，5 个提交合入 main），本次更新主要聚焦服务端渲染改进与相关 Bug 修复。

- 🚀 **新增滚动偏移配置**：`List` 支持 `defaultScrollOffset`，`Grid` 支持 `defaultScrollLeft` / `defaultScrollTop`，用于设置初始滚动位置。
- 🖥️ **优化服务端渲染滚动行为**：服务端渲染 HTML 无法预滚动，因此从首行开始渲染；组件水合时应用默认偏移，除非浏览器已恢复滚动位置。
- 📦 **空数据场景处理**：列表或网格初始为空时，默认滚动偏移会在有行数据后应用。
- 📏 **动态行高预配置**：`useDynamicRowHeight` 新增 `initialRowHeights`，可在服务端渲染等场景提前提供已知或估算的行高。
- 📚 **文档更新**：文档站点新增“服务端渲染”页面。
- 🐞 **修复动态高度 SSR 定位问题**：服务端渲染的动态高度行在测量前改为按正常文档流显示，避免因估算高度导致重叠或间隙。
- ⚠️ **修复 React 18 警告**：解决 `List` 和 `Grid` 在服务端渲染时记录 `useLayoutEffect` 警告的问题。
- 🧰 **修复滚动条尺寸计算**：`getScrollbarSize` 在服务端渲染期间不再抛错，而是返回 `0`。

---

### [推出 Astryx RichText：适用于你的表单的富文本字段 · Astryx](https://astryx.atmeta.com/blog/introducing-astryx-richtext)

**原文标题**: [Introducing Astryx RichText: a rich text field for your forms · Astryx](https://astryx.atmeta.com/blog/introducing-astryx-richtext)

Astryx 正式发布稳定版富文本表单组件 @astryxdesign/richtext，它基于 Lexical 构建，由 Astryx 主题统一驱动样式，可无损地在 Markdown 与编辑器状态之间读写，并自带完整的无障碍支持，可与 Astryx Markdown 的渲染保持一致。

- 📦 **稳定发布**：@astryxdesign/richtext 已转为稳定包，自 v0.7.1 起与 @astryxdesign/core 同版本发布，并遵循相同的兼容策略；安装时需自行安装 Lexical 0.52 系列 peer 依赖，样式则以预构建 CSS 提供。
- 📋 **表单字段优先**：RichTextEditor 与 TextArea 一样是带标签的表单字段，支持标签、描述、必填或可选状态、状态提示、只读与禁用、字数限制，以及与其他表单一致的边框和聚焦环；RichTextView 用于以相同排版只读展示内容。
- 💾 **存储格式**：存储的是序列化为 JSON 的 Lexical 编辑器状态，可回传给 defaultValue 继续编辑，或传给 RichTextView 展示。
- 🔄 **无损 Markdown 互转**：markdownToEditorStateJSON 与 editorStateJSONToMarkdown 无需挂载编辑器即可双向转换，也可在服务端使用；未做修改时往返转换可得到完全相同的字节，改动一段后其余格式（列表标记、转义、空格、字符引用）原样保留。
- 🎨 **显示一致**：RichText 文档与 Astryx Markdown 渲染同一文档时，字号层级、块间距、行宽、列表标记和代码框完全一致，明暗主题及左右书写方向均支持，长代码行会自动换行。
- 🧰 **主题化工具栏**：RichTextEditorToolbar 由 Astryx 的 Toolbar、Selector、ToggleButton 和 Dialog 构成，包含撤销重做、段落与标题、列表与引用、粗体、斜体、下划线、删除线、行内代码和链接；空间不足时改为横向滚动，而非折叠菜单，图标可替换，并可通过 endContent 扩展自定义控件。
- 🔌 **基于 Lexical 可扩展**：可直接添加自定义节点、Markdown 转换器和 Lexical 插件；编辑器支持一个 Lexical 次版本（当前为 ^0.52.0），由应用安装 Lexical，而非由 RichText 内置；用 createMarkdownPlugin 编写的 Markdown 插件可通过 createRichTextExtension 复用到编辑器，如果插件会转换整个文档，则会以 RichTextExtensionError 拒绝。
- ♿ **无障碍开箱即用**：读屏软件会正确播报字段标签并说明其为多行文本框；工具栏可完全用键盘操作（方向键切换、Tab 缩进、Escape 再 Tab 移出并播报提示）；任务列表复选框也可用键盘勾选；按钮提示、链接对话框与播报文案均取自 Astryx 消息目录，便于本地化翻译。
- 🚀 **快速上手**：安装包与 Lexical peer 依赖后，可查阅 RichTextEditor 文档，或在已安装该包的项目中运行 npx @astryxdesign/cli component RichTextEditor，也可在 RichText playground 中体验全部功能。

---

### [c15t 3.0.0 发布说明](https://c15t.com/changelog/3.0.0)

**原文标题**: [c15t 3.0.0 release notes](https://c15t.com/changelog/3.0.0)

c15t v3 是 2026 年 10 月 8 日发布的重大版本，核心是从 React/Next.js 库重构为统一同意引擎：一套内核为 Next.js、TanStack Start、React、Nuxt、Vue、Astro、Svelte、SvelteKit 及纯 HTML 提供适配器，并通过同一套一致性测试；同时带来服务端渲染横幅、同意清单、策略规则、GPP/IAB 增强、新集成和重写的自托管后端。该版本包含破坏性变更，但会读取 v2 已存储的访客选择。

- 🚀 重大重构：v2 是 React 库加 Next.js 适配器，v3 是跨 8 个框架和脚本标签的统一同意引擎，策略行为在各框架中保持一致。
- 🧩 框架覆盖扩大：新增 TanStack Start、Nuxt、Vue、Astro、Svelte、SvelteKit 和 @c15t/browser（用于 WordPress、Shopify 等 CMS/纯 HTML 站点）。
- ⚡ 性能提升：服务端框架可在首屏 HTML 中直接渲染横幅；cookiebench 桌面端 c15t 横幅 27ms 可见，10 款工具中位数 471ms；移动端 240ms 对 2.71s。
- 🧾 同意清单（Consent Manifest）：后端新增 GET /manifest，可在构建时下载或运行时缓存；带 150ms 后端延迟的 Next.js 基准中 TTFB 从 157.6ms 降至 7.4ms。
- 🎨 浏览器负担降低：首屏 CSS 从 10.3KB 降至 8.8KB gzip；主题在服务端生成；对话框和可选模块按需加载；React 重渲染显著减少。
- 📜 策略规则升级：policy packs 改为 policy rules，提供 34 个预设（原 6 个），支持 notice 提示、按当前规则实时计算权限、GPC 实时读取而非存储为拒绝。
- 🎛️ 同意控制增强：支持非 IAB 的按供应商同意、ConsentGate 替代 Frame、floating/bar/widget/wall 横幅展示、A/B 实验、撤销时清理 cookie/存储、镜像其他 CMP 决策。
- 🌍 IAB TCF 与 GPP：支持 GPP 1.1 和 16 个美国州 section；将 IAB publisher restrictions 写入 TC string；IAB 横幅覆盖所有新框架，TCF 2.4 延续支持。
- 🔌 集成更新：@c15t/scripts 更名为 @c15t/integrations，37 个旧 helper 保留并新增 5 个，总计 42 个；新增 Cloudflare Zaraz、Klaviyo、Sentry、Vercel Speed Insights、OpenAI ChatGPT Ads pixel。
- 🗄️ 自托管后端重写：基于 Effect 4/Effect SQL，支持 PostgreSQL、MySQL、SQLite；提供 c15t self-host migrate 迁移 v2 数据库；MongoDB 无迁移路径。
- 🛠️ CLI 与开发工具：c15t setup 可脚手架各框架并支持 --plan 预览；--codex 面向编码代理；提供 codemods 迁移 v2 源码；DevTools 不再依赖 React。
- ⬆️ 升级与兼容：v3 可读取 v2 的 cookie/存储记录，访客选择保留；但客户端与后端需一起升级，v3 客户端无法读取 v2 后端 /init。
- ⚠️ 破坏性变更：全面 ESM、React 18+/Next.js 15+；ConsentManagerProvider→ConsentProvider；useConsentManager() 移除改为按字段 hooks；回调、主题/CSS、IAB 配置、导出路径、Node SDK 和后端配置均有变更，需使用 codemods 与升级指南。

---

### [](https://julesblom.com/react-trees)

**原文标题**: [React Trees Playground | JulesBlom.com](https://julesblom.com/react-trees)

Jules Blom 的 React Trees Playground 是一个可视化工具：粘贴 React 代码后，可用“父树—所有者树”记法阅读组件结构，理解输出落点与 props 来源。

- 🧩 支持粘贴 React 代码，并以视觉化方式查看父树和所有者树。
- 🌳 行表示父树，即输出落点；弧线表示所有者树，即 props 来源。
- 🖱️ 点击上下文提供者、错误边界等区域，可查看其覆盖的父树部分。
- 📦 底层 walker 和 renderer 已发布为 npm 包 `react-parent-owner-trees`，也能从运行中的 React 应用实时绘制。
- 🧪 页面仅静态绘制初始渲染：Hooks 返回初始值，effects 和数据获取不运行，未知导入会变成命名透传行。
- 📚 提供 context/memo、状态下移、内容提升、廉价 context、Suspense/lazy、reducer/context、错误边界、portal modal 等示例。
- 🏷️ 图例区分组件、宿主元素、结构 fiber、父结构、所有者边等标记。
- 🔍 特殊标记说明：`React.memo` 在圆盘比较 props，portal 输出到目标 DOM，lazy 表示懒加载，context 用区域、点和线表示消费范围与值。
- 🛡️ 支持 Suspense、错误边界、Profiler、Activity、ViewTransition 等结构，并说明其独占或包含范围。
- 🔗 提供分享和复制链接功能。

---

### [调查与表单管理软件 - SurveyJS](https://surveyjs.io/?utm_source=this-week-in-react&utm_medium=email)

**原文标题**: [Survey and Form Management Software - SurveyJS](https://surveyjs.io/?utm_source=this-week-in-react&utm_medium=email)

SurveyJS 是一套开源、可自托管的 JavaScript 客户端调查与表单管理组件，帮助开发者在自己的应用中构建动态表单、拖拽式表单设计器、数据看板和 PDF 表单导出功能，并确保调查数据完全存储在自有数据库中，避免依赖第三方 SaaS。

- 🧩 核心产品包括 Form Library、Survey Creator、Dashboard 和 PDF Generator，覆盖表单渲染、可视化创建、结果分析和 PDF 导出全流程。
- 📝 Form Library 是 MIT 许可的 UI 组件，可解析 SurveyJS JSON 并渲染动态交互表单，支持复杂题型、条件逻辑和校验。
- 🎛️ Survey Creator 是白标拖拽式表单构建器，可自动生成 JSON Schema，并支持主题编辑、分支逻辑、默认值和计算，无需写代码。
- 📊 Dashboard 可读取表单 JSON，实时展示调查结果，支持交互式图表、表格、分页和筛选。
- 📄 PDF Generator 可将 Web 表单按 JSON Schema 渲染为可编辑或预填答案的 PDF。
- 🔐 强调数据所有权与自托管：SurveyJS 只负责前端 UI，不存储、访问或追踪数据，后端存储、用户管理和审批流程需自行实现。
- ♾️ 无使用限制：不限制管理员、受访者、表单数量、提交量、文件上传或功能使用。
- ♿ 无障碍支持完善：Form Library 和 Survey Creator 符合 WCAG、Section 508 与 ARIA 标准，并支持键盘导航和屏幕阅读器。
- 🧱 支持自定义独立或复合题型，可扩展内置题型或集成 Angular、React、Vue 3 组件。
- 📴 支持离线数据采集，本地保存调查、主题和回答，联网后自动同步。
- 🎨 支持白标与主题定制，可适配 Bootstrap、Material UI、shadcn/ui 等设计系统。
- 🤖 可通过 API 集成 AI，实现自然语言生成表单、翻译和智能内容建议。
- 🏢 适用于保险、医疗、市场研究、教育、人力资源、电商、客户体验、非营利和银行等行业。
- 💳 商业组件采用一次性开发者许可，永久使用；含 12 个月免费维护与支持，之后可续订维护订阅。
- 🔑 许可证可分配给团队成员或外包开发者，被分配者可使用许可证并联系支持，但不能查看账单或管理团队。
- ⚠️ SurveyJS 不提供后端、数据库或用户认证方案，适合希望完全控制前端体验、后端逻辑和数据合规的组织。

---

### [React Native 0.88 - 基于 Web 的事件分发、可变字体、SceneDelegate，无破坏性变更 · React Native](https://reactnative.dev/blog/2026/10/19/react-native-0.88)

**原文标题**: [React Native 0.88 - Web-Based Event Dispatching, Variable Fonts, SceneDelegate, no breaking changes · React Native](https://reactnative.dev/blog/2026/10/19/react-native-0.88)

React Native 0.88 于 2026 年 10 月 19 日发布，核心变化包括默认启用基于 Web 标准的事件分发、支持可变字体、iOS 新增 SceneDelegate 生命周期，并升级 React 19.3.0 与 Metro 0.87。该版本没有用户可见的破坏性变更，是连续第三个无此类变更的版本，升级预计无需修改应用代码。

- 🚀 **发布概况**：React Native 0.88 正式发布，包含 568 个提交、91 位贡献者；0.85.x 进入不再支持状态。
- 🧩 **Web 事件分发**：默认通过 W3C EventTarget API 分发事件，支持捕获、冒泡、`stopPropagation()`、`preventDefault()`；Canary 提供 `addEventListener`、`removeEventListener`、`dispatchEvent` 命令式 API。
- ✅ **兼容性预期**：事件 prop 名称、合成事件对象、执行顺序、触摸响应系统等保持不变；直接事件如 `onLayout` 仍只在目标节点触发，错误仍同步到达 React 错误边界。
- 🅰️ **可变字体**：`fontVariationSettings` 在 Android/iOS 的 `<Text>` 和 `<TextInput>` 中可用，支持 CSS 字符串和对象两种写法。
- 📦 **Java TurboModules**：可直接接收和返回 `ArrayBuffer`，二进制数据无需再编码为字符串或数字数组；同步方法可借用 JS 内存，但仅在方法返回前有效。
- 🍎 **iOS SceneDelegate**：为满足 iOS 27 SDK 的 UIScene 生命周期要求，新增 SceneDelegate 入口并保留 AppDelegate 兼容；目前仅支持单场景，需迁移入口、转发 URL/用户活动回调并添加 `UIApplicationSceneManifest`。
- 🛠️ **Swift Package Manager**：SwiftPM 支持仍为实验性、可选启用；计划 0.89 默认使用并提供 CocoaPods 退出选项，后续版本再移除 CocoaPods。
- ⚠️ **弃用项**：`InitializeCore` 改用 `react-native/setup-env`；`experimental_background*` 改名；iOS `InputAccessoryView`、`ReactFragment.fabricEnabled`、`ReactImageManager` 的 `String?` 重载等被弃用。
- 🔧 **其他重要更新**：React 19.3.0、Metro 0.87.1 最低版本、Hermes 更新；背景样式属性稳定；RTL 文本默认右对齐；FileReader/Blob 更符合 Web 规范；修复 ScrollView、Image、Renderer 等问题。
- 📱 **平台与工具**：Android 默认 User-Agent 加入应用名和版本；iOS 支持资源目录图片；TypeScript 支持模块扩展；DevTools 默认支持应用截图，Canary 支持 WebSocket 检查。
- ⬆️ **升级方式**：建议使用 React Native Upgrade Helper 和升级文档；新项目可用 `npx @react-native-community/cli@latest init MyProject --version latest`；Expo 用户将在 Expo SDK 58 中获得 0.88。

---

### [EventTarget - Web API | MDN](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget)

**原文标题**: [EventTarget - Web APIs | MDN](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget)

EventTarget 是事件目标对象实现的接口，用于接收事件并注册监听器；元素、文档、窗口以及多种其他对象都可作为事件目标。

- 🎯 **核心作用**：实现该接口的对象可以接收事件，并可为其添加事件监听器。
- 🌐 **常见事件目标**：`Element` 及其子节点、`Document`、`Window` 是最常见的事件目标。
- 🔄 **其他事件目标**：`IDBRequest`、`AudioNode`、`AudioContext` 等对象也可以作为事件目标。
- 🧩 **事件处理器**：许多事件目标还支持通过 `onevent` 属性或特性注册事件处理器。
- 🛠️ **构造函数**：`EventTarget()` 用于创建新的 `EventTarget` 实例。
- 📌 **实例方法**：包括 `addEventListener()`、`removeEventListener()`、`dispatchEvent()` 和 `when()`。
- 👀 **when() 方法**：返回一个 `Observable` 对象，表示在该事件目标上触发的事件流。
- 🧵 **运行环境**：该功能可在 Web Workers 中使用。
- ✅ **兼容性**：属于 Baseline 广泛可用功能，自 2015 年 7 月起已在各浏览器中可用，但部分功能支持程度可能不同。
- 📚 **相关规范与参考**：规范为 DOM 标准中的 `interface-eventtarget`，另可参考事件索引、事件入门和 `Event` 接口。

---

### [Expo SDK 58 — Expo 更新日志](https://expo.dev/changelog/sdk-58)

**原文标题**: [Expo SDK 58 — Expo changelog](https://expo.dev/changelog/sdk-58)

Expo SDK 58 正式发布，面向 iOS 27 并升级至 React Native 0.88，重点增强 iPhone Duo/可调整窗口适配、Xcode 27 Device Hub、App Intents、Expo UI、Expo Router、Expo Modules 2.0 Beta 以及构建与调试性能。Expo Go 商店版将在数周内上线；现阶段建议使用开发构建体验 SDK 58，并重点关注弃用项与破坏性变更。

- 🚀 发布信息：SDK 58 支持 iOS 27、内置 React Native 0.88；新 Expo Go 仅支持 SDK 58，商店版数周内推出。
- 🍎 iOS 27 适配：采用 UIScene 场景生命周期，应用自动支持可调整尺寸；Expo 包不再依赖 UIScreen.main，并提供场景感知几何工具。
- 📱 iPhone Duo：支持折叠、分屏与铰链状态；推荐 Stack/NativeTabs、SafeAreaView、ArrangementView，并新增 expo-hinge。
- 🧰 Xcode 27 Device Hub：Expo CLI 可检测并启动 Device Hub；expo-device-hub 提供浏览器内模拟器/模拟器实时控制、监控与设置切换。
- 🗣️ App Intents（Alpha）：expo-app-intents 将应用操作与内容暴露给 Siri、Shortcuts、Spotlight 和 Apple Intelligence，支持 Spotlight 索引与屏幕内容识别。
- 🎨 Expo UI：列表虚拟化/回收、iOS NavigationStack/Toolbar 等导航组件、SwiftUI/Compose 组件与修饰符增强，并修复 RNHostView 测量与触摸问题。
- 📈 Expo Observe：生产环境监控启动/导航性能、JS 错误与原生崩溃；新增 errorHandlingEnabled 与 clientId，AppMetrics 弃用。
- 🤖 代理开发：Expo CLI 增加面向代理的实验性命令；@expo/agent-cli 提供 status、dev、smoke、skills:sync 等能力。
- 🧩 Android 小组件：expo-widgets 支持 Android 独立 Hermes 运行 JS bundle、交互与 Material Colors；iOS Live Activities 增强。
- 📦 Swift Package Manager：为 Expo 应用采用 SwiftPM 打基础；CocoaPods 仍是默认且受支持的路径。
- ⚡ 构建提速：expo-modules-core 提供 Android 预编译库，干净调试构建约从 80 秒降至 39 秒。
- 🧠 Expo Modules 2.0 Beta：用 Swift/Kotlin 注解暴露 API，iOS/Android 性能显著提升，同步调用比 DSL 快 2.5–5.6 倍。
- 🔍 指纹默认 balanced：版本号等常见变更不再触发不必要的原生重建。
- 🦀 实验性 Rust 转换器：Noxcturnal 基于 oxc/napi-rs，模块转换约快 3 倍，冷打包约快 2 倍。
- 🧭 Expo Router：数据加载器、SSR、中间件、Native Tabs、Toolbar 稳定；导航核心重构，默认 server output、Web 异步路由等变化需迁移。
- 🌐 开发服务器与隧道：代理/隧道连接更可靠；新 ws-tunnel 默认更快更稳，需登录 Expo 账户。
- 📱 React Native 0.88：带来 SwiftPM 工具、Text fontVariationSettings、TurboModules ArrayBuffer、DevTools 实验性能截图等。
- 🔗 集成与启动链接：PostHog 一条命令接入并关联 EAS 更新；开发构建与 Expo Go 统一 __expo_ 启动参数。
- 🛠️ 其他更新：相机文档扫描、文件哈希/预览、音频锁屏与 WAV 录制、图片 SVG 变量、SecureStore 确认、SQLite/Font/Notifications/Location 等改进。
- ⚠️ 升级注意：Strict TypeScript API、RN API 移除、iOS 场景生命周期、NODE_ENV、Android R8 默认开启、expo-router/文件系统/SQLite/通知等破坏性变更；按指南升级并重建开发构建。

---

### [推出 expo-app-intents：为 Expo 应用带来 Siri、快捷指令、Spotlight 和 Apple Intelligence — Expo 博客](https://expo.dev/blog/introducing-expo-app-intents)

**原文标题**: [Introducing expo-app-intents: Siri, Shortcuts, Spotlight, and Apple Intelligence for Expo apps â Expo blog](https://expo.dev/blog/introducing-expo-app-intents)

目前未提供可总结的文章正文，因此无法提炼关键信息。
- 📄 请粘贴需要总结的文章内容
- 🧾 我将按要求输出中文概览与带表情符号的要点列表
- ✅ 每条要点会使用“-”符号开头并突出核心信息

---

### [DeployPulse | 面向 React Native 的托管式 OTA 更新](https://deploypulse.io/)

**原文标题**: [DeployPulse | Hosted OTA Updates for React Native](https://deploypulse.io/)

DeployPulse 是面向 React Native 的托管 OTA 更新平台，兼容现有 CodePush 与 Expo Updates SDK，提供秒级发布、自动回滚、灰度发布、代码签名和 CI 集成，并按月活用户计费且各套餐均包含带宽。

- 🚀 兼容 `react-native-code-push` 和 `expo-updates`，同一账户可同时运行两种协议，无需修改代码。
- 🔁 从 CodePush 迁移只需将 `serverUrl` 指向 DeployPulse，SDK 与签名密钥保持不变。
- ⚡ 通过 `dpctl` CLI 发布更新，经全球边缘节点数秒触达设备，绕过应用商店审核。
- 🛡️ 支持设置错误率阈值，发布异常时自动回滚全部用户至上一稳定版本。
- 🎯 支持 semver 应用版本定向、按百分比灰度发布，以及 Production/Staging 多环境管理。
- 👆 可一键回滚、暂停发布，并将 Staging 中已验证版本晋升到 Production。
- 📊 实时跟踪下载、活跃安装和错误率，支持按国家细分与角色权限团队协作。
- 🔧 可从 GitHub Actions、GitLab CI、Jenkins、Bitrise、CircleCI 通过一条命令发布。
- 🔐 提供代码签名，用户自带密钥，发布时签名并由设备端验证防篡改。
- 📱 支持裸 React Native、Expo prebuild/CNG、EAS Build；不支持 Expo Go，EAS Update 由 DeployPulse 替代。
- 💰 按 MAU 而非席位计费，所有套餐含带宽、无限应用/部署/发布；免费版 10,000 MAU、100GB，付费从 $20/月起。
- 🧭 三步上手：安装 `dpctl`、连接应用、发布 OTA 更新。

---

### [](https://github.com/react-native-community/discussions-and-proposals/pull/1027)

**原文标题**: [RFC: API removal strategy in React Native by satya164 · Pull Request #1027 · react-native-community/discussions-and-proposals · GitHub](https://github.com/react-native-community/discussions-and-proposals/pull/1027)

这份 RFC 由 satya164 提交，编号 #1027，当前状态为 Open；其目的是讨论 React Native 核心中组件、模块等 API 的移除策略，以避免不同 bundler 配置和项目设置引发的问题。该 PR 包含 1 个提交，正在等待 huntie 审查，合并前至少需要 1 个批准。

- 📄 RFC 标题为“RFC: API removal strategy in React Native”，原题为“Add RFC for API removal strategy”
- 🎯 目标是制定从 React Native core 移除 components、modules 等内容的策略
- 🧩 主要动机是避免各种 bundler 配置和设置产生问题
- 🌿 分支 satya164:@satya164/removal-strategy 拟合并至 react-native-community:main
- 👀 cortinico 于 2026-10-21 请求 huntie 审查，目前仍在等待
- ✅ 合并要求至少 1 个 approving review
- 🏷️ 当前无 assignee、labels、projects 或 milestone
- 👥 页面显示 1 名参与者，PR 含 1 个 commit

---

### [GitHub - zoontek/react-native-edge-to-edge：在 React Native 中轻松启用边到边显示（原名 react-native-bars）。· GitHub](https://github.com/zoontek/react-native-edge-to-edge)

**原文标题**: [GitHub - zoontek/react-native-edge-to-edge: Effortlessly enable edge-to-edge display in React Native (formerly known as react-native-bars). · GitHub](https://github.com/zoontek/react-native-edge-to-edge)

该项目是一个用于在 React Native 中轻松启用 Android 边到边（edge-to-edge）显示的库，原名 react-native-bars，可让应用内容延伸到系统栏下方，并保持跨平台体验一致。不过该库现已弃用，官方建议改用 React Native 内置能力及新的导航栏控制库。

- ⚠️ 该库已弃用：React Native 0.86 及以上版本内置了许多边到边修复，建议在 `android/gradle.properties` 中设置 `edgeToEdgeEnabled=true`，导航栏样式控制改用 `@zoontek/react-native-navigation-bar`。
- 🎯 主要目标是让 Android 6 及以上应用内容无缝显示在系统栏下方，提升与 iOS 一致的体验，并支持沉浸式全屏模式。
- 🛠️ 安装方式为 `npm i -S react-native-edge-to-edge` 或 `yarn add`，同时需要将 Android `AppTheme` 的父主题替换为对应的 `Theme.EdgeToEdge` 系列主题。
- 📱 Expo 项目需在 `app.config.js`、`app.config.ts` 或 `app.json` 中配置插件，可设置 `parentTheme` 和 `enforceNavigationBarContrast`；这些配置不支持 Expo Go，需要使用开发构建。
- 🎨 默认采用 Android 15 风格：透明状态栏、透明手势导航栏、半透明按钮导航栏；如需完全透明，可设置 `enforceNavigationBarContrast: false`，但需自行管理导航栏样式。
- ⌨️ 启用边到边会影响 Android 键盘的 `adjustResize` 行为，推荐使用 `react-native-keyboard-controller`，也可考虑 `KeyboardAvoidingView`。
- 📐 安全区域管理建议使用 `react-native-safe-area-context`；使用内置 `Modal` 时需设置 `statusBarTranslucent` 和 `navigationBarTranslucent`，更推荐使用导航库的 Modal 方案。
- 🧩 提供 `SystemBars` 组件替代 `StatusBar`、`expo-status-bar` 和 `expo-navigation-bar`，支持 `style`、`hidden` 属性，以及 `pushStackEntry`、`popStackEntry`、`replaceStackEntry`、`setStyle`、`setHidden` 等 API。
- 🔍 排查问题时，应确保 `expo-router`、`react-native-screens`、`react-native-reanimated` 等相关生态库为最新版本，并将旧系统栏组件替换为 `SystemBars`。
- 🧑‍💻 第三方库作者如涉及边到边兼容问题，可参考 `react-native-is-edge-to-edge` 的 README 获取兼容性说明。
- 🐞 Android 15 模拟器上完全透明导航栏样式可能异常，但该问题通常不在真机出现。

---

### [OpenIAP 新增对 Amazon 的支持 - DEV 社区](https://dev.to/amazonappdev/openiap-adds-supports-for-amazon-33b)

**原文标题**: [OpenIAP adds supports for Amazon - DEV Community](https://dev.to/amazonappdev/openiap-adds-supports-for-amazon-33b)

OpenIAP 宣布获得 Amazon 赞助，并新增对 Amazon 设备应用内购买（IAP）流程的支持，覆盖 Fire OS 与 Vega OS。开发者可用统一 API 在 Expo、React Native、Flutter、KMP、.NET MAUI、Godot 等框架中接入 Amazon IAP，减少单独维护 Amazon 集成路径的成本。

- 🚀 Amazon 赞助 OpenIAP，OpenIAP 现支持 Fire OS 和 Vega OS 上的 IAP 流程与收据验证。
- 🧩 OpenIAP 提供统一标准 API，支持 Expo、React Native、Flutter、Kotlin Multiplatform、.NET MAUI、Godot。
- 📱 已使用 react-native-iap 或 expo-iap 的开发者可用相同 API 在 Amazon 设备上发布 IAP 流程，无需单独集成路径。
- 📺 Fire TV 全球销量超过 3 亿台，去年用户在设备上流媒体、游戏和直播观看时长超过 1000 亿小时，IAP 支付流程需求显著。
- 🔄 OpenIAP 将 Amazon Appstore 的消耗型商品、权益、订阅、购买更新和履约映射到与 Google Play、App Store 相同的 API 模型。
- ⚙️ Fire OS 以 Android Amazon flavor 实现，基于 Amazon Appstore SDK；可通过 Gradle 配置或框架对应配置选择 Amazon IAP 后端。
- 🛰️ Vega OS 是独立 Kepler 运行时目标，使用 manifest.toml、Kepler 依赖和 Amazon Kepler IAP 模块；Expo 与 React Native for Vega 可通过适配器接入。
- ✅ 验证与商品目录身份保持一致：使用相同 IAPKit Amazon 收据载荷，产品 ID 在 Amazon Developer Console、Amazon App Tester、应用代码和权益校验中保持一致。
- 📦 Fire OS 与 Vega OS 支持已在 OpenIAP RC.1 发布，当前稳定版本包括 react-native-iap 16.3.1、expo-iap 5.3.1、openiap-google-amazon 3.3.1。
- 🛠️ 建议从 OpenIAP 文档的 Amazon Store Setup 指南开始，并在发布前使用 Amazon App Tester 测试购买。
- 📚 帮助资源包括 OpenIAP 文档、GitHub、Amazon Appstore IAP 文档和 Amazon 开发者社区。
- 🧾 OpenIAP 继续独立运营，核心库保持 MIT 许可并免费使用；文章特别感谢首席维护者 Hyo Dev 及贡献者。

---

### [](https://expo.dev/blog/teamreach-ota-updates-relaunch)

**原文标题**: [Relaunching TeamReach: how OTA updates saved a 5,000,000-user cutover â Expo blog](https://expo.dev/blog/teamreach-ota-updates-relaunch)

未提供可总结的文章内容，因此无法提取关键信息或生成摘要。
- 📭 当前待总结文本为空
- 📝 请补充需要总结的文章正文
- ✅ 收到内容后将按模板输出中文要点摘要

---

### [Meta VR 布局 SDK：多窗口 React Native 应用](https://www.callstack.com/blog/multi-window-react-native-apps-with-the-meta-vr-layout-sdk)

**原文标题**: [Meta VR Layout SDK: Multi-Window React Native Apps](https://www.callstack.com/blog/multi-window-react-native-apps-with-the-meta-vr-layout-sdk)

overview summary  
本文介绍 Meta 在 Meta Connect 2026 发布的 Meta VR Layout SDK 及其 React Native 支持：开发者可将界面拆分到多个空间窗口中，同时保持同一个 React 树，让状态、props 和 context 在主面板与副面板之间自然共享，并需为系统无法分配独立窗口时设计 inline 或 drop 回退方案。

- 🧩 **核心变化**：过去第二面板常需单独 Android Activity 和独立 React root，状态难同步；现在副面板可作为 `SpatialWindow` 组件存在于同一 React 树中。
- 🪟 **使用方式**：用 `SpatialSceneProvider` 包裹空间相关应用区域，再用 `SpatialWindow` 包裹希望独立成面板的子树，由 Horizon OS 决定是否提升为空间窗口。
- 🔄 **状态共享**：主面板和副面板仍属于同一 React 树，父组件状态、props、context 和共享 store 可直接传递；示例中计数器在两侧同步更新。
- ⚠️ **回退机制**：`fallback="inline"` 会在原位置渲染内容，适合必需内容；`fallback="drop"` 在无独立面板时不渲染，适合提示等可省略内容。
- 📌 **放置状态**：`useSpatialWindowState` 可读取 `spatial`、`pending`、`inline`、`dropped` 四种 placement 状态，便于展示或处理窗口是否成功独立。
- 🧱 **关键限制**：需要系统 v207 或更高版本；当前 React Native 集成最多支持两个额外空间窗口；`SpatialWindow` 不能嵌套；窗口多于槽位时按 `priority` 分配。
- 🏷️ **窗口标识**：`label` 用于系统识别窗口并关联状态，建议在窗口生命周期内保持稳定；相同 label 的已挂载窗口共享同一 placement 状态。
- ⚙️ **环境配置**：需要 React Native 0.85+、React 18.2+，安装 `@metavr/layout-compat` 和 `@metavr/layout-window-compat`；支持 bare 项目及保留 Android 生成文件的 Expo 项目。
- 📐 **尺寸与定位**：`windowWidth`、`windowHeight` 必填；可用 `anchor`、`{ parent, child }` 和 `offset` 请求布局，但最终位置由 Horizon OS 根据可用空间决定。
- 🧪 **无头显测试**：可用 Meta Spatial Simulator 与 `metavr` CLI 检查窗口创建、槽位限制、fallback、尺寸和锚点；发布前仍建议在头显中验证深度、舒适度、性能和最终外观。
- 🚀 **实践建议**：为必需内容准备 inline 布局，对可省略内容使用 drop 回退；该 SDK 让 React Native 开发者能用熟悉的组件和状态模式构建多窗口 VR 界面。

---

### [使用 Appduct 为 AI QA 智能体控制应用测试条件](https://www.callstack.com/blog/give-qa-agents-the-controls-they-need-with-appduct)

**原文标题**: [Control App Test Conditions With Appduct for AI QA Agents](https://www.callstack.com/blog/give-qa-agents-the-controls-they-need-with-appduct)

Appduct 让 QA 智能体直接调用应用内由团队注册的工具，从而控制测试条件，例如调整应用时钟或触发底部弹窗，减少等待和重复 UI 操作，让智能体专注于验证目标行为。

- 🎯 核心问题：智能体检查定时提醒或底部弹窗时，往往要等待真实时间或重复界面操作才能进入目标测试条件。
- 🛠️ Appduct 允许团队把应用内函数注册为工具，并提供名称、描述和输入 schema；只有注册过的工具才能被智能体访问。
- 🔌 工具通过处理器执行具体逻辑，例如设置功能开关、推进测试时钟、模拟收到邀请事件。
- 📱 支持 Swift 原生 iOS、Kotlin 原生 Android、React Native、Flutter 和 Web；Release 构建默认不包含 Appduct，可在内部 QA 构建中启用。
- 🔗 智能体通过 Appduct 的 MCP 服务器连接应用：SDK 运行在应用内，daemon 运行在电脑上，移动端可通过短时连接链接或二维码建立会话。
- ⏱️ 时间控制示例：将调度逻辑抽象为时间接口，在 QA 构建中注册 set_time、set_timezone、advance_time、reset_time 等工具，验证提醒出现前后及不同时区行为。
- 📲 事件触发示例：注册 simulate_invite_received，派发 invite_received 事件，复用真实业务代码打开底部弹窗，并用不同邀请数据重复检查布局和交互。
- 📡 异步完成信号：应用可通过 postEvent 上报 invite_sheet_presented，智能体用 appduct_wait_for_event 等待弹窗就绪后再截图检查。
- 🧪 智能体可结合 UI 自动化工具（如 agent-device）操作界面、读取界面和截图，同时通过 Appduct 调用工具控制测试条件。
- 🚀 建议从一个 QA 任务开始，先暴露一个所需的小控制工具，写好描述和 schema，连接智能体并验证行为，再参考快速开始或 playground 集成。

---

### [Maestro MCP 服务器 | Maestro 文档](https://docs.maestro.dev/get-started/maestro-mcp?utm_source=this-week-in-react)

**原文标题**: [Maestro MCP Server | Maestro Docs](https://docs.maestro.dev/get-started/maestro-mcp?utm_source=this-week-in-react)

Maestro MCP Server 将 Maestro 的移动端与 Web UI 测试能力接入支持 MCP 的编码代理，使代理能够编写、运行和调试 UI 测试；文档涵盖安装配置、Viewer 使用、更新方式、核心 MCP 工具及 MCP 基本概念。

- 🚀 Maestro 实现 Model Context Protocol（MCP），可集成 Claude Code、Claude Desktop、Cursor、GitHub Copilot、Codex、Gemini、Windsurf、JetBrains AI Assistant 等编码代理。
- ⚙️ 安装前需先安装 Maestro CLI，并确保所用编码代理支持 MCP。
- 🧩 不同代理的安装方式不同：Claude Code 使用命令安装，Claude Desktop 需编辑 `claude_desktop_config.json`，Codex、Copilot、Cursor、Gemini 等也各有配置方式或交互命令。
- 🛠️ 通用手动安装采用 stdio 配置，默认要求 `maestro` 在 `PATH` 中；否则需使用 Maestro CLI 的完整路径，并可按需显式指定 `PATH` 或 `JAVA_HOME`。
- 🔁 安装完成后需重启编码代理，让代理可连接真实移动模拟器或仿真器，并生成可重复的端到端测试。
- 👁️ Maestro Viewer 可将 iOS 模拟器、Android 模拟器或物理设备嵌入编码代理或浏览器，实时显示 MCP 执行的命令并支持完整交互。
- 🪟 通过 `open_maestro_viewer` MCP 工具可打开 Viewer，只需让编码代理执行类似“open the maestro viewer”的指令。
- ⬆️ Maestro MCP 随 Maestro CLI 捆绑发布，升级 CLI 即升级 MCP；升级后需在编码代理中重连 MCP 或重启代理。
- 🧰 核心工具包括 `list_devices`、`inspect_screen`、`take_screenshot`、`run`、`cheat_sheet`；其中 `run` 支持内联 YAML、指定 `.yaml` 文件或目录/标签过滤。
- ☁️ 云相关工具包括 `list_cloud_devices`、`run_on_cloud`、`get_cloud_run_status`，使用前需通过 `maestro login` 或设置 `MAESTRO_CLOUD_API_KEY` 完成 Maestro Cloud 认证。
- 📚 MCP 是开放标准，采用客户端-服务器架构，通过标准化接口让 LLM 连接外部数据源、工具和服务，传输层使用 JSON-RPC 2.0，支持 stdio、HTTP SSE 或 WebSocket。

---

### [](https://expo.dev/blog/xcode-27-device-hub-expo-device-hub)

**原文标题**: [Xcode 27 replaced Simulator.app. Expo CLI and expo-device-hub already know. â Expo blog](https://expo.dev/blog/xcode-27-device-hub-expo-device-hub)

未提供可总结的正文内容，暂时无法提取文章要点。
- 📄 请在“Use following content”后粘贴需要总结的文章内容。
- ✍️ 收到正文后，我会用中文按“概述 + 表情符号要点”的格式进行简洁总结。

---

### [发布 v10.0.0 · DylanVann/react-native-fast-image · GitHub](https://github.com/DylanVann/react-native-fast-image/releases/tag/v10.0.0)

**原文标题**: [Release v10.0.0 · DylanVann/react-native-fast-image · GitHub](https://github.com/DylanVann/react-native-fast-image/releases/tag/v10.0.0)

本次 v10.0.0 是 react-native-fast-image 的大版本更新，核心包括迁移到 React Native 新架构/TurboModule、用 objectFit/objectPosition 替代旧 API、Android 包名与 Glide/OkHttp 行为调整，以及多项破坏性变更。升级前需满足 RN 0.83+、Expo SDK 55+、iOS/tvOS 15.1、Android API 24 等要求。

- 🚀 发布 v10.0.0（2026-10-12），包含代码重构、新功能和破坏性变更。
- 🧩 新增 New Architecture 原生组件和 TurboModule，要求 React Native 0.83+（仅新架构）、Expo SDK 55+、iOS/tvOS 15.1、Android API 24，默认 compileSdk/targetSdk 36。
- 🖼️ 移除 resizeMode（prop 和 style），改用 objectFit：stretch→fill，center→scale-down，contain/cover 不变；不再支持 repeat 平铺。
- 🎨 新增 objectPosition prop，对应 CSS object-position。
- 📦 Android Java 包名由 com.dylanvann.fastimage 改为 com.fastimage；自动链接应用无需改动，手动集成、导入类或自定义 ProGuard 规则需调整。
- 🧱 FastImage 变为单一原生视图，不再渲染 children；需要在图片上覆盖内容时使用 FastImageBackground，ref 指向原生视图，Jest 快照显示单个 FastImageView。
- 🌫️ Android 默认 300ms 淡入；FastImage.setDefaults({ transition: false }) 可保持 9.x 行为；transition={null} 现在表示默认行为，而非无淡入。
- ❌ 移除 fallback prop：始终使用 FastImage 原生视图加载，需要 fallback 时直接用 React Native 的 Image；同时移除 FastImageProgressListener，overlayColor 从 ImageStyle 移除。
- 📈 onProgress 的 progress 现在来自原生视图。
- 🌐 Android 上应用通过 Glide 加载的图片改用 React Native 的 OkHttp client，带应用拦截器和 cookies，无超时则使用 15 秒连接/读取超时；AppGlideModule 仍可注册其他 client。
- ⚙️ Android 默认使用 Glide 5（5.0.7，4.15+ 仍可用），iOS 需 SDWebImage 5.21.4+；原生模块为 FastImageModule，NativeModules.FastImageView 移除，JS API 基本不变。

---

### [](https://swmansion.com/changelog/react-native-screens-4-30-0/)

**原文标题**: [React Native Screens 4.30.0](https://swmansion.com/changelog/react-native-screens-4-30-0/)

本次 4.30.0 版本重点适配 iOS 26/27 与 iPhone Duo，优化 Stack v4 在导航栏与安全区下的布局行为，并修复 Tabs、Stack 及 Android 的多项问题。

- 📦 发布版本：react-native-screens 4.30.0，2026 年 10 月 13 日的小版本更新。
- 🍎 iOS 26+：原生 Stack 屏幕改为布局在不透明导航栏下方，并通过安全区插入；不透明头部不再随滚动最小化。
- 📏 新增 `unstable_safeAreaEdges` 属性（`ScreenStackItem`），可覆盖 iOS 26+ 应用的安全区边缘。
- 📐 `useHeaderHeight` 现在会在头部最小化时报告可见高度（iOS 27+）。
- 🗂️ `Tabs.Host` 新增 `prominentScreenKey`（iOS 27+），标签栏最小化时仍保持所选标签可见。
- 🧭 建议 iOS 26+ 遵循 Apple 指南使用透明头部；不透明头部在横屏、模态及 iPhone Duo 上存在布局问题。
- 🐞 修复 `Tabs.Host`/`Tabs.Screen` 类型发布、Stack v4 布局偏移与头部子视图位置、Tabs 搜索选择及异步图标等问题。
- 🤖 Android 修复旧版与 Tabs 容器延迟子视图按压状态的问题，原生按钮触摸反馈更及时。
- ✅ 支持 React Native 0.84 及以上版本。

---

### [发布 v3.4.0 · software-mansion/react-native-gesture-handler · GitHub](https://github.com/software-mansion/react-native-gesture-handler/releases/tag/v3.4.0)

**原文标题**: [Release v3.4.0 · software-mansion/react-native-gesture-handler · GitHub](https://github.com/software-mansion/react-native-gesture-handler/releases/tag/v3.4.0)

react-native-gesture-handler v3.4.0 已发布，包含 iOS SPM 构建支持、Touchable 按压行为调整、Web/Android/iOS 手势一致性改进，以及大量手势、坐标、崩溃和兼容性修复，并升级至 React Native 0.88。

- 🚀 发布 v3.4.0：这是最新版本，自 v3.3.0 以来包含 8 个提交。
- ❗ 重要变更：iOS 新增 SPM 构建支持；Touchable 新增 `pressOutAfterAnimation`，随后重命名为 `immediatePressOut`；Android 在原生按压开始时派发 `onPressIn`。
- 👍 改进：Android 的 alpha 遍历门控与 iOS 对齐；Web 的 Tap `maxDelay` 默认值对齐原生 200ms；Web ScrollView 作为拦截检测器；优化挂载关系扫描。
- 🐛 修复：Android 原生视图接管触摸时取消检测手势，修复触摸取消回调中的 NPE、Text 内联 View 崩溃、ScrollView 惯性停止误触等问题。
- 🧭 修复：Android/iOS/Web 支持在首次 `onTouchesDown` 时调用 `GestureStateManager.activate`；iOS 修复手势中配置更新后 `manualActivation` 被忽略。
- 🌐 Web 修复：键盘事件指针键、触摸板平移相对坐标、完整变换坐标映射、组合手势变化检测、DOM 属性保留等。
- 🧩 其他修复：检测器框覆盖变换子元素、SharedValue 平移偏移符号、晚挂载手势对象关联、隐藏/透明按钮命中测试、嵌套滚动与 `ACTION_CANCEL` 处理等。
- 🔢 杂项：升级 React Native 0.88；通过同步 TurboModule 方法暴露模块 ID；更新文档兼容表及依赖、CI/E2E 流程。
- 👏 新贡献者：@teoarjun、@Shexter、@SatvikMishra08、@JacquesLeupin、@gigobyte、@huytdps13400、@mikael-karlsson-weapp。
- 🔗 完整变更日志：v3.3.0...v3.4.0。

---

### [发布 v0.17.0 · software-mansion-labs](https://github.com/software-mansion-labs/react-native-bottom-sheet/releases/tag/v0.17.0)

**原文标题**: [Release v0.17.0 · software-mansion-labs/react-native-bottom-sheet · GitHub](https://github.com/software-mansion-labs/react-native-bottom-sheet/releases/tag/v0.17.0)

概述总结
- 🚀 software-mansion-labs/react-native-bottom-sheet 发布最新版 v0.17.0，解决 #22、#57、#59 等 14 个 issue，并有 @dkulakov、@gabrieldonadel、@giaBaoJS、@JaMinsane、@LeCiel 等外部贡献者参与。
- 🤝 新增 scrollableNegotiation，支持 none、initial、handoff 模式，可分别配置展开与收起；默认 { expand: 'handoff', collapse: 'initial' }，实现 sheet 与嵌套滚动容器间的连续手势交接。旧参数 disableScrollableNegotiation={true} 应替换为 scrollableNegotiation="none"。
- 📐 新增百分比 detent（如 '45%'、'100%'），按可用 sheet 高度解析，并在布局变化时自动更新。
- ✅ 增加 detents 与 index 校验：空数组、非法 detent、非整数或越界 index 会抛出明确 JS 错误；缩短 detents 时需同次渲染更新 index。
- 📱 Android 的 ModalBottomSheet 新增 onCloseRequest，用于系统 Back、预测性返回手势和键盘 Escape，由应用决定是否及如何关闭。
- 🐛 修复拖动与尺寸问题：不可滚动视图覆盖滚动内容时仍可拖动 sheet；修复正 zIndex 下 'content' detent 尺寸；最高 detent 为固定高度或百分比时，内容按该高度适配并受可用高度限制。
- ⚙️ 修复 Android 性能与交互：关闭/空闲时降低 CPU 占用；透明 scrim 下不可见或无响应；重复 scrim 点击导致关闭动画重启和重复 onIndexChange；scrim 点击误触底层 gesture-handler 按钮。
- 🧱 修复 Android 稳定性：原生 overlay 绕过 BackHandler；Fabric 反复开关 sheet 可能导致白屏无响应；AGP 9 内置 Kotlin 的插件冲突；同次渲染新增 detent 后 index 更新被忽略。
- 🍎 修复 iOS：handle/header 拖动被误判为嵌套滚动手势；初始挂载忽略 scrollableNegotiation="none" 或旧参数；RN 0.87 自定义 surface 崩溃；复用 sheet 保留旧 extendUnderStatusBar 设置。

---

### [](https://github.com/uni-stack/uniwind/releases/tag/v1.13.0)

**原文标题**: [Release Release v1.13.0 · uni-stack/uniwind · GitHub](https://github.com/uni-stack/uniwind/releases/tag/v1.13.0)

uniwind 发布 v1.13.0 最新版本，包含 2 个提交并合并至 main，重点改进了原生样式匹配、CSS 级联顺序、React Native 导出及 Metro 热重载，同时修复了发布与样式相关问题。

- 🚀 新增原生样式匹配谓词生成功能（#725）
- 🎨 原生端现在遵循 CSS 级联顺序（#722）
- 🐛 修复原生组件入口未转发全部 React Native 导出的问题（#740）
- 🧪 修复测试主题被包含进已发布 uniwind.css 的问题（#718）
- 🔤 修复字体变体空值未移除的问题（#729）
- 🔥 修复 Metro 未跟踪导入 CSS 依赖、影响热重载的问题（#676）
- 🔨 重构样式元数据与声明，使其分离（#723）
- ⚙️ 改进 CI 发布流程（#715）
- 📅 v1.13.0 于 10 月 19 日发布，距 v1.12.2 后新增 2 个提交
- 🎉 新贡献者 @fendyk 通过 #676 完成首次贡献
- 👥 贡献者包括 dlebedynskyi、jpudysz 及另外 2 人，完整变更见 v1.12.2...v1.13.0
- ❤️ 社区反应：5 个爱心、2 个火箭，共 6 人互动

---

### [发布 Release 1.9.0 · margelo/react-native-n](https://github.com/margelo/react-native-nitro-fetch/releases/tag/v1.9.0)

**原文标题**: [Release Release 1.9.0 · margelo/react-native-nitro-fetch · GitHub](https://github.com/margelo/react-native-nitro-fetch/releases/tag/v1.9.0)

本次发布的重点是为 React Native 网络请求库 react-native-nitro-fetch 推出 v1.9.0。该版本主要带来 iOS WebSocket 默认改用 Network.framework（约快 30%）、大量 Android 和 iOS 的 WebSocket 修复与性能优化，并新增可选证书固定和 nativeBuffer 响应体流式写入能力。需要注意的是，Network.framework 模式会绕过 ATS 与证书固定，且不支持代理和 HTTP 认证；如需要这些能力，可在 Info.plist 中将 NitroWebSocketsUseNetworkFramework 设为 false，回退到 NSURLSessionWebSocketTask。

- 🚀 v1.9.0 由 riteshshukla04 于 10 月 15 日发布，包含 2 个提交，为最新版本。
- ⚡ iOS WebSocket 默认使用 Network.framework，官方称性能约提升 30%。
- ⚠️ 新 iOS WebSocket 传输不应用 ATS 和 NSPinnedDomains 证书固定，ws:// 可连接任意主机，且不支持代理与 HTTP 认证；可通过 Info.plist 设置 NitroWebSocketsUseNetworkFramework=false 回退。
- 🔧 大量 WebSocket 修复：重定向最多 20 次、支持相对重定向、完整读取 Location、跨域重定向移除 Authorization、握手大响应头、预连接替换、close/error 事件、重复 connect、消息大小限制与顺序等。
- 🛠️ Android 修复与优化：响应体按 64KB 分块读取、UTF-8 解码优化、预分配缓冲区、Cronet 网络线程读循环、无效 URL 处理、请求注册与关闭帧处理等。
- 📱 iOS 修复：流式请求 URL 无法解析时不再崩溃、处理晚注册的已完成请求、WebSocket 消息竞态及 close 后事件问题等。
- 🔐 新增 Android/iOS 可选证书固定功能。
- 📦 新增 nativeBuffer 选项，可将响应体流式写入原生缓冲区；修复打包时 Expo 配置插件构建。
- 👥 贡献者包括 pioner92、huytdps13400 和 riteshshukla04，并包含文档修正。

---

### [GitHub - natew/react-native-gpui · GitHub](https://github.com/natew/react-native-gpui)

**原文标题**: [GitHub - natew/react-native-gpui · GitHub](https://github.com/natew/react-native-gpui)

总览：该仓库展示了 **react-native-gpui** 项目，它用 React Native 的组件开发方式，把界面通过 GPUI（Zed 的 GPU 加速 Rust UI 框架）原生渲染，从而避免使用浏览器或 Electron。

- 🧩 使用真实的 `react-reconciler` 驱动 GPUI 窗口，并通过 Metal 渲染。
- 🖥️ 提供与 React Native 类似的类型化组件接口，包括 `View`、`Text`、`Pressable`、`ScrollView`、`TextInput`、`Svg`、`WebView` 和 `StyleSheet`。
- 📦 可通过 `npm install react-native-gpui` 安装，包和完整文档位于 `ts/` 目录。
- 🦀 Rust 渲染服务位于 `rust/` 目录，仓库还包含 `cpp/`、`plans/`、`ts/` 等目录。
- 🍎 目前仅支持 macOS arm64（依赖 GPUI/Metal）。
- 📄 项目采用 MIT 许可证，仓库公开，约有 58 个 Star、0 个 Fork、0 个 Watcher，累计 410 次提交。
- 📝 主要文件包括 `README.md`、`AGENTS.md`、`hybrid-plan.md`、`react-native-gpui.md`、`package.json` 等。
- ℹ️ 仓库未提供描述、网站或主题标签。

---

### [发布 v1.1.0 · gmi-software/react-native-better-pdf · GitHub](https://github.com/gmi-software/react-native-better-pdf/releases/tag/v1.1.0)

**原文标题**: [Release v1.1.0 · gmi-software/react-native-better-pdf · GitHub](https://github.com/gmi-software/react-native-better-pdf/releases/tag/v1.1.0)

react-native-better-pdf 发布 v1.1.0，重点新增“将多个 PDF 作为单一文档打开”和“通过 Base64 字符串打开文档”，并显著优化长文档在 Android/iOS 上的内存占用与主线程性能；同时要求 React Native 0.83+/Expo SDK 55+，并带来若干兼容性与行为变更。

- 🚀 版本发布：v1.1.0（2026-10-19），包含新功能、性能改进、Bug 修复及破坏性变更。
- 📚 多文件合一：`source={[a, b, c]}` 可将多个文件按顺序显示为一个文档，统一页码、缩放、布局、分页和跨文件搜索；每个来源可单独设置密码。
- 🧭 多文件加载细节：`onLoad.sources` 标明各文件起始页；加载为全有或全无，`onError.error.sourceIndex` 指出失败文件；文件内链接指向本文件页，“下一页/上一页”可跨相邻文件。
- ⚠️ 多文件限制：该模式仅用于阅读；`print`、`exportDocument` 和表单填写只支持单文件，多来源时会拒绝。
- 🔐 Base64 文档：`source={{ base64 }}` 可在 `PdfView` 和 `PdfDocument.open` 中打开字符串 PDF；原生在主线程外解码，不向应用提供 `filePath`；适合几 MB 内文档，无需 `data:` 前缀。
- 📉 Android 长文档内存优化：灰度扫描页保持 1 字节/像素，500 页灰度扫描峰值 PSS 从 144.7 MB 降至 110.4 MB；缩小到适配宽度以下时按半尺寸/四分之一尺寸渲染，1000 页 zoom 0.05 峰值约从 240 MB 降至 150 MB；横屏/平板/折叠屏复用页面位图，后台不再视为内存压力。
- ⚡ iOS 性能优化：搜索高亮不再阻塞主线程，528,449 个匹配时上/下一页从 1.23–1.34 秒降至 10–19 毫秒；5000 页长文档表单读取/编辑/导出保持主线程外，编辑后 `getFormFields` 从 3.24 秒降至 <0.1 毫秒。
- 🧱 破坏性变更：要求 React Native 0.83+（Expo SDK 55+）；RN 0.81 的 iOS 关闭查看器不释放内存，Expo SDK 54 应用可继续用 1.0.1；`PdfLoadEvent` 新增必需 `sources` 数组。
- 🔄 行为调整：iOS 在 `onLoad` 中且视图无尺寸时调用 `goToPage`/`goToViewport`/`zoomTo` 会等布局后应用；Android 小数页码四舍五入，`onLoad` 前 `search()` 被忽略，页面渲染失败仅在立即重试也失败时上报。
- 🧩 Android 稳定性/一致性：`renderPage`、`getOutline`、`getPageSizes` 按调用顺序串行执行，导出使用独立线程；关闭/替换文档时排队调用以 “The document was closed” 拒绝；畸形文件解析有时间上限，超时整体失败。
- 🛡️ 其他修复：导出到下载缓存目录会被拒绝；iOS 打印在视图关闭或 `source` 变化时拒绝；AES-128 文档打印不再二次询问密码；iOS 受保护文档填写导出会重新加密；负值/无限 `pageSpacing` 回退 8；iOS `getStats` 不可测计数返回 -1；iOS 17+ 保留已有 `%XX` 转义。

---

### [](https://github.com/retyui/babel-plugin-react-native-direct-imports)

**原文标题**: [GitHub - retyui/babel-plugin-react-native-direct-imports: Babel plugin that rewrites react-native barrel imports into direct module imports, so your bundle only includes the React Native APIs you actually use. · GitHub](https://github.com/retyui/babel-plugin-react-native-direct-imports)

该仓库介绍了一个处于早期阶段的 Babel 插件 babel-plugin-react-native-direct-imports。它能把 `react-native` 的桶导入重写为对底层模块的直接 `require`，以便打包结果只包含实际用到的 React Native API，从而减小包体积。由于 `react-native/index.js` 是带懒加载 getter 的 CommonJS 桶文件，打包器无法进行 tree-shaking，所以即使只导入一个 `View` 也会引入整个 React Native。插件通过生成深路径的 `require(...).default` 来规避这个问题，并避免 Babel 的 interop 辅助代码。

- 📦 **核心功能**：将 `import { View } from 'react-native'` 等导入改写为 `require('react-native/Libraries/Components/View/View').default` 这类直接模块导入
- 🎯 **解决的问题**：`react-native` 的 CommonJS 桶文件无法被 tree-shaking，单个 API 导入会拖入全部 React Native 模块
- ⚙️ **使用 `require` 的原因**：React Native 模块是 CommonJS，若输出 `import`，Babel 会为每个导入添加 `_interopRequireDefault` 等辅助函数；直接 `require(...).default` 更精简
- 🚧 **早期阶段警告**：插件尚不成熟，可能存在粗糙边缘和破坏性变更，遇到问题可提交 issue
- 📥 **安装方式**：`npm install --save-dev babel-plugin-react-native-direct-imports`
- 🔧 **配置要点**：在 `babel.config.js` 的 plugins 中启用，并配合 `@react-native/babel-preset` 设置 `disableDeepImportWarnings: true`，同时传入精确的 `reactNativeVersion`
- 🔄 **缓存重置**：配置后需重置一次 Metro 缓存（`--reset-cache` 或 `--clear`）
- 🗺️ **版本映射**：`maps/` 目录提供 0.70.0 起每个稳定版本的映射，版本必须完全匹配，升级 React Native 后需同步更新插件
- 🔇 **静默警告**：`silenceBatchedUpdatesWarning`（默认 `false`）可隐藏 React Native 0.86+ 中 `unstable_batchedUpdates` 无效的警告
- 📝 **行为细节**：未知名称和类型导入保持不变；re-export 及 `node_modules` 中的 `require('react-native')` 也会被重写；`Platform` 保持本地变量以支持 Metro 内联（别名除外）；`import * as RN` 和 `module.exports = require('react-native')` 会报错
- ✅ **兼容性**：与 Uniwind 的 `withUniwindConfig` 兼容；`react-native-worklets` 低于 0.14.0 的 bundle 模式不兼容，需升级至 0.14.0+
- 🛠️ **生成映射**：可通过 `yarn generate-maps` 生成全部版本映射，或指定具体版本
- 📄 **许可证**：MIT

---

### [GitHub - batical/react-native-skia-webgpu-video：适用于 React Native Skia 3 和 WebGPU 的视频播放、合成与导出。· GitHub](https://github.com/batical/react-native-skia-webgpu-video)

**原文标题**: [GitHub - batical/react-native-skia-webgpu-video: Video playback, composition and export for React Native Skia 3 and WebGPU. · GitHub](https://github.com/batical/react-native-skia-webgpu-video)

该仓库为 React Native Skia 3 / WebGPU 提供视频播放、合成与导出能力，强调显式资源所有权和可配置显存预算；目前处于 Beta 阶段，功能较完整，但长期内存、HDR、音频输出和音画同步等仍未完全验证。

- 🎬 核心功能：支持视频播放器/编辑器、基于时间线的合成与叠加、H.264/HEVC 导出、音频合成以及自定义 GPU 处理。
- ⚠️ Beta 状态：Skia 3.7.0 / WebGPU 0.17.0 已在 iPhone 15 Pro 和 Pixel 8a 上验证；长期内存、HDR、可听音频、A/V 同步尚未认证，两个 4K 场景存在已知问题。
- 📦 环境要求：React Native 0.86.2、React 19.2.3、Skia 3.7.1、WebGPU 0.17.0、Reanimated 4.5.3 / Worklets 0.11.3；需新架构和 Hermes，Android API 28+ / Vulkan 1.1，必须原生重建，Expo Go 不支持。
- 🛠 安装步骤：通过 npm `beta` 标签安装并固定精确版本；Babel 插件中最后添加 `react-native-worklets/plugin`；在应用内运行 `skia-video-patch-canvas` 并纳入 `postinstall`。
- 🧩 使用方式：用绝对本地文件路径构建 composition；使用 `useVideoComposition` 或 `useVideoPlayback`；同一 `drawFrame` 复用于预览和导出；`exportVideoComposition` 输出到可写路径。
- 🚀 性能优化：静态图像建议用 `image.makeTextureImage()`；通过 `onProfile` 查看解码、导入、绘制、GPU、编码等阶段耗时；3.7.0 导出速度基本不变，主要改进屏幕 canvas。
- 🎞 帧传输路径：iOS 使用 AVFoundation/IOSurface，Android 使用 ImageReader/EGL + AHardwareBuffer；预览和导出尽量走 GPU，失败时回退 CPU readback 并警告。
- 🎨 像素格式：`framePixelFormat` 可选 `auto`、`yuv`、`rgba`；`yuv` 更省内存，但 iOS 导出每帧可能多 2–4 ms；HDR 和 10-bit Android 源保留 EGL 解码路径。
- 🔊 音频：默认静音，需设置 `audio: true` 或 `audio: { volume }`；可用 `kind: 'audio'` 添加音乐/旁白；AAC 导出保留，但可听输出和音画同步未验证。
- 🧠 内存管理：`configureVideoMemory()` 设置跟踪的视频资源预算，但不覆盖 codec/Skia/GPU 驱动全部内存；帧辅助函数返回的图像归库所有，不应自行释放。
- ✅ 验证情况：JS 237 项测试、类型检查、包测试和 122 项基准测试通过；iOS 61/61 基准用例、56/58 XCTest；Android CPU/GPU 解码 10/10、仪器测试 126/127。
- 🐞 已知问题：Pixel 8a 上 4K 播放中 seek 会使时钟停滞、120 片段懒加载蒙太奇暂停 seek 不出帧、Android 17 文件缺失识别问题；ImageReader 1:1 导出文件大 5–16%。
- 🔄 迁移注意：移除旧 `@shopify/react-native-skia` 和旧 Skia Video 包，避免同应用加载两代；用 `drawVideoFrame` / `makeVideoFrameImage` 替换旧纹理接口；`copy` 和 `direct` 仍兼容。
- 📄 许可与来源：MIT 许可，作者 Sebastien Hecart；API 灵感来自 `batical/react-native-skia-video` 等早期项目。

---

### [Xcode 27.1 发布说明 | Apple 开发者文档](https://developer.apple.com/documentation/xcode-release-notes/xcode-27_1-release-notes)

**原文标题**: [Xcode 27.1 Release Notes | Apple Developer Documentation](https://developer.apple.com/documentation/xcode-release-notes/xcode-27_1-release-notes)

该页面当前无法直接显示正文，仅提示需要启用 JavaScript；同时为自动化工具和辅助工具提供了 Markdown 版本入口。

- 🔒 页面内容依赖 JavaScript 才能正常查看
- 🔄 需在浏览器中开启 JavaScript 并刷新页面
- 🛠️ 面向自动化工具和辅助工具提供 Markdown 版本
- 📄 可通过“查看 Markdown”获取页面内容
- ℹ️ 所给文本仅为技术提示，未包含实际文章正文

---

### [CrUX 中现已提供实验性软导航指标 | 博客 | web.dev](https://web.dev/blog/crux-experimental-soft-navs/)

**原文标题**: [Experimental soft navigation metrics now available in CrUX  |  Blog  |  web.dev](https://web.dev/blog/crux-experimental-soft-navs/)

Chrome 在 CrUX 中推出实验性“软导航”Core Web Vitals 指标，将单页应用（SPA）中由 JavaScript 动态更新内容和 URL 的页面切换纳入测量，让 LCP、INP、CLS 更完整地反映真实用户体验；大多数网站指标基本不变，变化主要集中在软导航占比高的 SPA，尤其是头部站点。

- 🧭 背景：Core Web Vitals 一直难以覆盖 SPA 的“软导航”，即不重新加载 HTML、仅通过 JavaScript 更新页面内容和 URL 的切换。
- 🚀 新进展：Chrome 151 上线 Soft Navigations Web 平台 API 后，CrUX 从 2026 年 10 月发布版开始提供实验性软导航指标。
- 📊 三项实验指标：`experimental_largest_contentful_paint_with_softnavs`、`experimental_interaction_to_next_paint_with_softnavs`、`experimental_cumulative_layout_shift_with_softnavs`，分别覆盖加载速度、交互响应和视觉稳定性。
- 🔄 测量方式：软导航与硬导航被合并统计；在 CrUX API 中，软导航指标会归到用户实际导航到的 URL，而非初始落地页，便于定位具体页面问题。
- 🌐 影响范围：约 70% 的源站几乎没有软导航流量；仅约 7%–11% 的源站有超过一半页面浏览来自软导航。
- 🏆 头部站点更明显：在 Top 1000 网站中，Android 有 35%、桌面端有 42% 的站点超过一半页面浏览依赖软导航。
- ⚡ LCP：软导航会复用已下载代码和资源，后续页面加载更快，高软导航占比站点的 LCP 表现可能明显改善。
- 🖱️ INP：响应性改为按单次页面视图测量，而非统计整个会话中最慢交互，Android 通过率约可翻倍；但 SPA 重 JavaScript 主线程工作仍可能拖累 INP。
- 📐 CLS：布局偏移按单次页面视图分段统计，不再跨长会话累积，SPA 重度站点的 CLS 预计改善。
- 🛠️ 获取方式：可通过 CrUX BigQuery、CrUX API、CrUX History API 获取，CrUX Vis 也已支持快速查看新指标。
- 🧪 后续计划：指标暂标为“实验性”，欢迎社区反馈；计划在 2027 年 5 月转为正式指标，届时 Search Console 将切换使用新数据；11 月 CrUX 发布版预计增加导航类型和 FCP 的实验性软导航指标。

---

### [CrUX 可视化](https://cruxvis.withgoogle.com/#/?view=cwvsummary&url=https%3A%2F%2Freact.dev%2F&identifier=origin&device=PHONE&periodStart=0&periodEnd=-1&display=p75s)

**原文标题**: [CrUX Vis](https://cruxvis.withgoogle.com/#/?view=cwvsummary&url=https%3A%2F%2Freact.dev%2F&identifier=origin&device=PHONE&periodStart=0&periodEnd=-1&display=p75s)

尚未收到需要总结的文章内容，因此无法提炼摘要与要点。请提供正文后，我将按要求生成中文概览和关键要点。

- 📄 当前未检测到文章正文
- 📝 请粘贴需要总结的内容
- ✅ 收到内容后将提供概览摘要与要点列表

---

### [PHP：新闻存档 - 2026](https://www.php.net/archive/2026.php#2026-10-21-5)

**原文标题**: [PHP: News Archive - 2026](https://www.php.net/archive/2026.php#2026-10-21-5)

2026年10月21日，PHP 发布安全公告，警告两个可导致未认证远程代码执行的关键漏洞，影响所有处理 Web 请求的 PHP 安装；官方强烈建议立即升级至 PHP 8.5.12、8.4.27、8.3.36 或 8.2.35。

- 🚨 **风险范围**：所有处理 Web 请求的 PHP 安装均受影响，包括 PHP-FPM、Apache mod_php、php-cgi、FrankenPHP 和 LiteSpeed；mod_php 风险最高，已演示未认证请求可在应用代码运行前触发攻击。
- 🛠️ **漏洞一 CVE-2026-109618**：内存耗尽（OOM）处理可能在内部请求数据仅部分初始化时中断 PHP，随后请求清理可能将无效数据当作有效数据处理，导致 RCE。
- 🧹 **漏洞二 CVE-2026-109619**：请求所属的内部状态可能在其底层内存释放后继续存在，同一 worker 处理的后续请求可能在正常初始化重置前使用该过期状态，导致 RCE。
- ⬆️ **更新方式**：升级到 PHP 8.5.12、8.4.27、8.3.36 或 8.2.35；源码和 Windows 源码/二进制可从官方下载页面获取。
- 🐧 **Linux 与 LTS 用户**：各发行版和 LTS 厂商已提前收到补丁，请检查厂商提供的更新包。
- ⏳ **旧版本支持**：PHP 8.1 及更早版本不再由 PHP 项目更新；部分发行版或 LTS 厂商提供回溯修复，请联系厂商或升级到受支持版本。
- 📦 **Remi 仓库提醒**：依赖 rpms.remirepo.net 的用户应改用发行版软件包或从源码构建，以便立即应用更新；该仓库当天不会提供更新。
- 🧩 **额外回溯补丁**：PHP 安全团队为 PHP 7.4、8.0 和 8.1 提供了最小源码回溯补丁，方便从源码构建或无法获得 LTS 厂商支持的用户。
- 🛡️ **无法立即更新时的缓解措施（OOM 漏洞）**：将 `memory_limit=-1`，最好通过 FPM 池或 Apache 的 `php_admin_value` 设置以防应用覆盖；设置较低的 `post_max_size`（无上传 8M，有上传 32M），并保持 `upload_max_filesize` 小于它；在 Web 服务器或代理层限制解码请求大小、输入字段数、multipart 分片数、请求头数量和嵌套深度；使用容器或 cgroup 作为可用性边界，仅终止受影响 worker；不要使用 `RLIMIT_AS` 或 `RLIMIT_DATA`。
- 🧷 **无法立即更新时的缓解措施（过期全局状态漏洞）**：设置 `session.upload_progress.enabled=0` 并重启所有 worker，需通过 `php.ini`、FPM 池或服务器配置在请求解析前生效，不能依赖 `ini_set()` 或 `.user.ini`；PHP 8.5 上设置 `fatal_error_backtraces=0` 并重启所有 worker；移除会在初始化前产生诊断信息的无效或弃用按请求设置；隐藏诊断信息无效；修复攻击者可触发的致命错误和执行超时。
- 📚 **更多信息**：上述公告链接包含完整技术细节。

---

### [CSS 的未来 ✨ • Josh W. Comeau](https://www.joshwcomeau.com/css/interop-2027/)

**原文标题**: [The Future of CSS ✨ • Josh W. Comeau](https://www.joshwcomeau.com/css/interop-2027/)

文章回顾 Interop 项目通过主流浏览器厂商协作显著提升 Web 特性兼容性（如 Subgrid 一年内接近全平台支持），并围绕 Interop 2027 投票介绍作者最期待的 10 项 CSS 提案；这些特性多数已在 Chromium 实现，可在其他浏览器中作为渐进增强使用，同时强调在 LLM/代理时代仍需掌握现代 CSS 并主动参与投票。

- 🧩 Interop 由 Google、Apple、Microsoft、Mozilla、Igalia、Bocoup 等合作推进，重点特性通常一年内接近 100% 跨浏览器支持。
- 🗳️ Mozilla 为 Interop 2027 建立功能排名系统，计划依据投票数据决定明年重点，作者据此列出个人 Top 10。
- ⚙️ CSS `@function` 提案允许自定义 CSS 函数并用 `result` 返回值，可实现极坐标转笛卡尔坐标等复杂计算。
- 📐 `corner-shape` 支持 `squircle`、`bevel`、`notch`、`scoop` 等角形状，且会改变实际 border-box，使边框、轮廓和阴影正确跟随。
- 🖌️ `border-shape` 可用直线、弧线和贝塞尔曲线自定义边框形状，并支持形状间动画。
- ⚓ Anchored Container Queries 为锚点定位补充 Level 2 能力，可查询目标元素是否使用回退位置，便于处理 tooltip 翻转等场景。
- 🧮 `inherit()` 函数提案允许继承值后通过 `calc()` 变换，例如修正嵌套圆角的内外半径关系；目前仍很早期。
- 🎬 Scroll-triggered animations 与 scroll-driven animations 不同，目标是在滚动到特定点后触发关键帧动画，减少对 `IntersectionObserver` 的依赖。
- ♿ `reading-flow` 和 `reading-order` 可让焦点/阅读顺序跟随响应式视觉布局，改善 Grid/Flexbox 布局变化下的可访问性。
- 📏 `interpolate-size` 与 `calc-size()` 支持在 `height: 0` 和 `height: auto` 等关键字尺寸间动画，常用于折叠面板。
- 🧱 Gap decorations 提案通过 `rule`、`row-rule`、`column-rule` 为 Grid 间隙绘制类边框线条，避免用空 DOM 节点和背景色取巧。
- 📌 Scroll state container queries 可查询 `position: sticky` 是否“粘住”以及滚动容器是否还能向上/向下滚动，用于动态样式和滚动渐变提示。
- 🤖 结论：截至 2026 年 10 月，多数功能已在 Chrome/Edge 支持但 Firefox/Safari 尚未支持；作者认为现代 CSS 仍值得深入学习，并鼓励大家提交自己的 Interop 2027 排名。

---

### [面向 Web 用例的 JPEG XL 与 AVIF 对比 - JakeArchibald.com](https://jakearchibald.com/2026/jpeg-xl-vs-avif/)

**原文标题**: [JPEG XL vs AVIF for web use-cases - JakeArchibald.com](https://jakearchibald.com/2026/jpeg-xl-vs-avif/)

文章基于多张图片和多种编码器（avifenc 1.4.2、libjxl 0.12.0、jixel 0.4.2、cwebp 1.6.0）在 M4 Pro 上实测，比较 JPEG XL 与 AVIF 在网页有损/无损、截图/插画、透明、HDR、渐进式、动画等场景中的文件大小、编码解码速度和内存占用。总体结论是：当前网页有损场景应默认选 AVIF 4:4:4；JPEG XL 在无损和 JPEG 转码等特定场景更强，jixel 让 JPEG XL 的竞争力明显提升；最终应用自己的图片测试，警惕围绕该话题的错误信息。

- 📉 有损照片：AVIF 通常产生更小文件；默认编码强度下最佳 JPEG XL 约大 15–25%，最高强度下约大 6–20%，但存在 JPEG XL 胜出的离群图片。
- 🧩 编码器差异：jixel 通常比 libjxl 文件更小，但个别图片疑似“刷指标”且视觉质量更差；透明细节场景例外。
- 🖥️ 截图与插画：AVIF 明显更好；等效 JPEG XL 在默认强度下大约 30–90% 更大，最高强度下大约 20–70% 更大。
- 🫥 透明图像：AVIF 明显更好；libjxl 默认大 31–44%、最高大 61–70%；jixel 透明通道无损编码导致文件约为 AVIF 的 2–3 倍。
- ⚡ 编码与内存：计入文件大小后 AVIF 总体更优；jixel 默认更快、更省内存但文件更大；AVIF 解码通常快 2–3 倍，极高质量差距缩小。
- ⚙️ 编码强度：AVIF 与 jixel 提高强度通常值得，jixel 到 slow 较划算；libjxl 高强度很慢、耗内存且收益很小，甚至可能文件更大。
- 🎨 色度子采样：AVIF 4:2:0 不应作为默认；它很少显著减小文件，还会使高质量更难达到；多数情况用 4:4:4。
- 📊 质量稳定性：单一质量设置对三种编码器都较可靠，不同图片的质量波动方向一致；样本小但未见明显风险。
- 🌀 渐进式加载：JPEG XL 在高强度下渐进式几乎免费，jixel 默认会增大约 12%；AVIF 渐进式目前仅 Chrome 支持，控制更多、文件常更小、解码更快。
- 🌈 HDR：JPEG XL 浏览器不支持 gain map，是相对 AVIF 的重要限制；非 gain map HDR 下指标分歧大，但 JPEG XL 文件常更小。
- 🗜️ JPEG 转码：JPEG XL 可无损转码现有 JPEG，文件小 9–20%，大图解码有时更快。
- 🏆 无损压缩：JPEG XL 明显胜出；WebP 大 9–17%，AVIF 大 30–120%；但网页很少需要无损，jixel 高强度无损解码可能很慢。
- 🎞️ 动画：动画图像格式仍不推荐，视频格式更适合视频；动画 AVIF 文件远小于动画 JPEG XL，但播放实现仍有问题。
- ✅ 建议：网页有损默认 AVIF 4:4:4 + 可接受的高强度；若文件异常大，再用 jixel JPEG XL 对比；最终用自己图片实测。

---

### [宣布 TypeScript 7.1 Beta - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-7-1-beta/)

**原文标题**: [Announcing TypeScript 7.1 Beta - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-7-1-beta/)

TypeScript 7.1 Beta 已发布，重点带来导入属性与环境模块声明、Source Phase Imports、`es2026` 目标、新库方法、全新模块化 API、内容映射器（Content Mappers）以及大量性能与内存优化；同时包含若干需要注意的行为变更，后续将进入 RC 和正式版。

- 🚀 **发布信息**：TypeScript 7.1 Beta 于 2026 年 10 月 20 日发布，可通过 `npm install -D typescript@beta` 安装体验。
- 📦 **环境模块支持导入属性**：现在可在 `declare module "*" with { type: "css" | "text" | "bytes" }` 中声明导入属性，从而根据属性获得正确类型，并在缺少必需属性时报错。
- ⚠️ **导入属性声明限制**：匹配这些声明的导入不会校验磁盘文件是否存在；相关声明也不会随 TypeScript 内置库发布，建议由最终用户在项目中自行声明。
- 🧩 **Source Phase Imports**：新增 `import source` 和动态 `import.source()`，可在模块加载前获取已解析的模块源对象；目前主要用于 WebAssembly，并保留模块身份。
- 🎯 **新增 `--target es2026`**：支持稳定的 `es2026` 目标和库选项，包含 `Math.sumPrecise()`、`Iterator.concat()`、`JSON.rawJSON()`、`Error.isError()`、`Uint8Array` Base64/Hex 方法等稳定化特性。
- 📚 **新增库方法**：`--lib esnext` 增加 `Promise.allKeyed`、`Promise.allSettledKeyed`、`Iterator.zip`、`Iterator.zipKeyed`、`Iterator.prototype.chunks/join/includes` 等提案方法。
- 🧱 **全新 TypeScript 7.1 API**：API 拆分为 `typescript/sync`、`typescript/async`、`typescript/fs`、`typescript/ast`、`typescript/ast/is`、`typescript/ast/factory` 等入口。
- ♻️ **可释放对象与快照**：API 和 Program 等对象支持 `using` 自动释放；Snapshot 可基于旧快照增量更新，并保留 Program ID 以便复用。
- 🗂️ **文件系统 API**：提供 `createFileSystem`、`createFileSystemWithLib`、`createFileSystemLayer`，支持内存文件系统、分层覆盖和无需写盘的 `emitToString()`。
- 🧩 **Content Mappers 成为一等公民**：可为 `.vue`、`.svelte`、`.astro`、MDX、CSS Modules 等格式提供虚拟内容与映射，需在 `tsconfig.json` 注册，并在命令行使用 `--runExternalCode`。
- ⚡ **性能显著提升**：大量优化减少内存压力并加快构建；示例中部分项目速度提升 1.2x–1.9x，内存降低约 15.8%–49.6%。
- 🧠 **行为变更**：对分布式类型参数的检查更严格，条件类型分支中的类型参数不再被视为与原类型参数完全等价，可能暴露既有代码中的问题。
- 🔜 **后续计划**：团队将聚焦速度、稳定性和反馈修复，预计约一个月后发布 Release Candidate，随后推出正式版。

---

### [推出 tsrs：TypeScript 到 Rust 的移植 | Cloudflare 博客](https://blog.cloudflare.com/typescript-rust-port/)

**原文标题**: [Introducing tsrs: a Port of TypeScript to Rust | Cloudflare Blog](https://blog.cloudflare.com/typescript-rust-port/)

overview summary
Cloudflare 与 VoidZero 及 Max Schwenk 合作推出 tsrs，将 TypeScript 编译器移植到 Rust，并在 Oxc 工具链中孵化。项目强调这不是对 TypeScript 的分叉，TypeScript 团队仍掌控语言设计；早期基准显示其最多快 8 倍、内存少约 70%，并借助 Rust/Wasm 让开发工具链更便携，可在 Workers、浏览器和嵌入式环境中运行。

- 🚀 tsrs 是 TypeScript 编译器的 Rust 移植，由 Cloudflare、VoidZero 与 Max Schwenk 合作推进，孵化于 Oxc JavaScript 编译器工具链。
- 🧭 明确不是分叉 TypeScript；TypeScript 团队继续负责语言设计与方向，移植需严格跟随上游决策以避免不兼容。
- ⚡ 早期基准：相同类型检查 worker 数下，tsrs 比 TypeScript 7.0 最多快 8 倍，内存占用约少 70%。
- 📈 TypeScript 7.1 beta 已比 7.0 快最多 2.5 倍，部分优化来自 tsrs；基准测试与 TypeScript 团队对齐配置。
- 🛠️ 可通过 npm 试用：`npm install tsrs`，`npx tsrs`；默认自适应配置会使用更多内存但速度更快。
- 🦀 选择 Rust 的关键原因之一是 WebAssembly：Rust 内存管理更适合 Wasm 场景，避免携带 Go 垃圾回收器，利于 Workers、浏览器、嵌入式和 IoT。
- 🔄 维护方式：与 Theo Browne 合并 tsc-rs 和 tsrs，支持 LSP、content mappers 等完整功能；借鉴 Vinext 的每日上游审查、夜间兼容测试和代理修复流程。
- 🤝 将尽量减少与上游差异，并把性能改进回馈 TypeScript Go 代码库；稳定版前会缩小如诊断输出顺序等差异。
- 🌐 Cloudflare 已支持 Vite、Rolldown、Oxlint、Oxfmt 等 Rust 工具，未来探索 tsrs 深度集成，例如 Oxlint 的类型感知 lint 规则。

---

### [](https://building.owner.com/tsrs)

**原文标题**: [tsrs Â· Building @Owner](https://building.owner.com/tsrs)

本文讲述 Owner 团队将 TypeScript 编译器移植为 Rust 项目 tsrs，代码几乎全部由 AI agent 编写；通过忠实移植、测试驱动和系统性内存/并行优化，把大型仓库 Olympus 的 typecheck 从约 80 秒降至约 7 秒，并大幅降低内存占用，使本地多 agent 开发和 CI 重新可行。项目现已并入 Oxc，并获得 Cloudflare、VoidZero 与 TypeScript 团队协作。

- 🚀 tsrs 是 TypeScript 的 Rust 移植，目标是为 coding agent 提供尽可能紧的验证闭环：lint、typecheck、format 可在笔记本、CI、云沙箱运行。
- 🏢 Owner 的 Olympus 单体约 3.7 万个 TypeScript 文件；原 TypeScript 7.0 单线程 typecheck 需 80 秒、19 GiB，叠加 tsgolint 和语言服务后总内存可超 50 GiB。
- ☁️ 旧缓解方案包括云沙箱、让 agent 排队、拆 tsconfig、拆内部包等，但都存在成本、稳定性或重架构问题，难以长期扩展。
- 🌙 作者让 Claude Opus 5.5 一夜完成可工作的 Rust typechecker；首轮 78% 错误基线逐字节匹配，加入类型打印后达 99.97%，13,462 个中仅 4 个不匹配。
- 📐 移植规则强调“同一切”：同算法、函数结构、求值顺序和诊断，并固定上游提交；每个 Go package 对应一个 Rust crate，先定义函数签名，再并行实现。
- 🧪 测试即规范：TypeScript 团队留下 15,197 个 conformance 用例，帮助团队对 Rust 移植的正确性建立信心。
- 🧠 内存优化包括停止复制源文本、惰性成员解析、更小对象布局、指针压缩、释放被检查叶子文件、重复推断 memo 和 work stealing。
- ⚖️ 优化准入门槛严格：单线程指令至少降 1%、墙钟至少降 2%或峰值内存至少降 5%，且输出必须逐字节一致。
- 🧵 并行检查按导入模块分组以减少重复库类型，并支持空闲 checker 从最忙 checker 取任务；默认保证确定性，另设 Go 兼容模式和 CI determinism gate。
- ✅ 正确性验证覆盖 TypeScript conformance suite、故障注入、shadow mode 缓存校验、Olympus CI 双编译器对比，以及 Miri 检查 unsafe arena 代码。
- 📉 Olympus 基准：4 checkers 从 61.4 秒/36.0 GiB 降至 8.75 秒/6.1 GiB（7.0 倍更快、5.9 倍更省内存）；8 checkers 从 56.6 秒/49.8 GiB 降至 5.8 秒/7.5 GiB（9.8 倍、6.6 倍）；默认 16 checkers 为 4.24 秒/9.5 GiB。
- 🧹 tsrslint 将类型感知 lint 移植到 tsrs：60 条规则在 8 个开源项目上耗时 37.3 秒，对比 tsgolint 的 169.4 秒，快 4.5 倍；峰值内存 11.5 GiB 对 45.0 GiB，省 3.9 倍。
- 💼 Owner 全仓库采用后，CI typecheck 约 7 秒、MacBook 约 12 秒；本地可并行多个 agent，沙箱/CI 不必按峰值预留内存，预计每年节省数十万美元。
- 🌐 项目已迁至 oxc-project/tsrs，获 Cloudflare、VoidZero 与 TypeScript 团队协作；可通过 `pnpm add -D tsrs` 使用，并已有浏览器 playground。

---

### [](https://nodejs.org/en/blog/release/v24.22.0)

**原文标题**: [Node.js — Node.js 24.22.0 (LTS)](https://nodejs.org/en/blog/release/v24.22.0)

Node.js 24.22.0（LTS，代号 Krypton）于 2026-10-14 发布，由 @richardlau 发布、@aduh95 准备。该版本包含多项 SEMVER-MINOR 新 API 与功能，覆盖 crypto、net、perf_hooks、sqlite、util 等模块，并合并大量缺陷修复、文档更新、依赖升级与多平台构建/测试改进；同时提供各平台安装包、二进制、源码、文档下载及 SHA256/PGP 校验信息。

- 🚀 **版本信息**：Node.js 24.22.0 LTS（Krypton），发布日期为 2026-10-14。
- 🔐 **crypto 增强**：新增 `crypto.parsePKCS12()`、通用 MAC API、从 OpenSSL provider 发现 cipher/hash、Cipher/Decipher 支持 SIV 与 GCM-SIV 等。
- 🌐 **net 改进**：支持将 `net.BoundSocket` 发送到线程和子进程；文档弃用 `Server.prototype._listen2`。
- 📊 **perf_hooks 扩展**：新增 `SlidingWindowHistogram`、Histogram 的 qrde 分析、`meanCI` API，以及直方图 CBOR 导入/导出。
- 🗄️ **sqlite 增强**：新增 `StatementSync.prototype.close()` 与 `StatementSync.prototype[Symbol.dispose]()`，并修复回调期间关闭数据库等问题。
- 🛠️ **util 新增**：实现 `util.markPromiseAsHandled`、`util.throttle` 与 `util.debounce`。
- 🐞 **广泛修复**：涉及 assert、buffer、fs、http/http2/https、stream、tls、quic、src、zlib、inspector、permission 等模块。
- 📦 **依赖更新**：npm 升级至 11.19.1，并更新 V8 补丁、zlib、simdjson、googletest 等。
- 💻 **下载与校验**：提供 Windows、macOS、Linux、AIX、ARM 等平台安装包/二进制、源码和文档链接，并附 SHA256 与 PGP 签名。
- 🔁 **发布导航**：上一版本为 Node.js 22.23.4 LTS，下一版本为 Node.js 26.12.0 Current。

---

### [宣布 Rsdoctor 2.0 - Rsdoctor](https://rsdoctor.rs/blog/release/release-note-2_0)

**原文标题**: [Announcing Rsdoctor 2.0 - Rsdoctor](https://rsdoctor.rs/blog/release/release-note-2_0)

Rsdoctor 2.0 是面向 Rspack 生态的构建分析工具重大版本，核心亮点包括面向 Agent 的构建分析、安装体积与依赖大幅缩减、分析/重建性能提升、多编译器支持增强，以及 Bundle 分析界面优化。

- 🎉 **版本发布**：Rsdoctor 2.0 正式发布，用于可视化构建过程与产物，帮助定位构建问题和性能瓶颈。
- 🤖 **Agent 构建分析**：推荐使用 Agent CLI 读取 `rsdoctor-data.json`，支持搜索、过滤并返回结构化 JSON；可通过 `brief` 模式生成数据，MCP Server 工作流已退役。
- 📦 **安装体积更小**：安装体积从 25.5 MB 降至 11.1 MB，减少 56.6%；依赖数量从 83 降至 18，减少 78.3%。
- ⚡ **分析更快**：分析时间从 18.07 秒降至 7.77 秒，减少 57.0%；峰值 RSS 降低 19.7%。
- 🔁 **重建更快**：HMR 中位时间从 6.81 秒降至 3.64 秒，减少 47%；重复构建分析时间从 250.9 ms 降至 14.2 ms，减少 94.3%。
- 🧩 **多编译器支持改进**：多个编译器的分析结果可汇总到同一报告并按名称切换，插件创建的子编译器也会自动检测；支持通过 `multiCompiler.group` 自定义分组。
- 🖥️ **Bundle 分析 UI 优化**：Tree Graph 使用虚拟滚动和渲染缓存提升大项目浏览流畅度；Treemap 支持点击缩放、面包屑返回、全屏和侧边栏折叠。
- ⬆️ **升级要求**：需 Node.js `^20.19.0 || >=22.12.0` 和 Rspack 2.0+；使用 `@rsdoctor/core` 替代 `@rsdoctor/rspack-plugin` 并采用 ESM；Rsdoctor 2.0 不再支持 webpack。

---

### [Webpack 5.112 | webpack](https://webpack.js.org/blog/2026-10-13-webpack-5-112/)

**原文标题**: [Webpack 5.112 | webpack](https://webpack.js.org/blog/2026-10-13-webpack-5-112/)

Webpack 5.112 正式发布，重点提升了导入调试体验、服务端渲染时的样式加载、多入口库的导出能力，以及模块联邦中共享依赖的精细控制；同时新增 HTML chunk 命名、DefinePlugin 异步值、共享 chunk 发现、CSS 与 JSON 资源压缩选项，并支持在配置数组上挂载插件。

- 🐛 **按原始名称调试导入**：source map 新增 `-scopes` 后缀（如 `source-map-scopes`），记录导入绑定对应的生成表达式，让调试器能按源码中的名称求值；该功能需手动开启，不改变输出的 JavaScript，但经模块拼接（scope hoisting）合并的模块暂不支持。
- 🖥️ **服务端渲染资源清单**：新增 `SSRManifestPlugin`，在客户端构建中生成 `ssr-manifest.json`，把源模块路径映射到客户端资源（含共享 chunk、异步祖先及按层叠顺序排列的样式表），便于服务端提前加载样式与预加载模块；需正确设置 `output.publicPath`。
- 🎨 **原生 CSS 服务端渲染修复**：`target: "node"` 构建可通过 `__webpack_css_server_styles__` 在无 document 环境收集样式。
- 📦 **导出多个入口模块**：设置 `library.entryExports: "all"`，即可把入口数组中所有模块的导出合并为一个库；默认仍是 `"last"`，同名冲突按 `export *` 规则省略并给出警告。
- 🔗 **选择共享哪些依赖**：模块联邦的 `shared` 新增 `include` / `exclude` 过滤器，可按版本（如 `^8.3.2`）或请求路径（如 `lodash/` 下的 `get`）决定哪些模块参与共享。
- 🏷️ **为 HTML 中的 chunk 命名**：原生 HTML 支持可通过 `webpackChunkName` 注释或 `module.parser.html.chunkName` 模板（支持 `[page]`、`[name]`、`[index]`、`[type]`）命名；兼容的内联脚本会合并为共享 chunk，以保持执行顺序。
- ⏳ **DefinePlugin 支持异步值**：`DefinePlugin.runtimeValue` 可等待异步回调后再解析模块，`async` 函数自动识别，否则传 `{ async: true }`；在编译期完成，不增加运行时开销，列出的依赖文件变更会触发重算。
- 🔍 **发现更多共享 chunk**：新增 `optimization.splitChunks.dedupDepth`（默认 0，`futureDefaults` 下为 1），可探索多组页面间的重叠 chunk；仅对自动命名且满足 `minSize` / `minSizeReduction` 的缓存组生效，建议从 1 开始并对比构建产物与耗时。
- 🎯 **更好地控制 CSS 与 JSON 资源**：新增 `customMedia` / `customSelectors` 压缩选项处理绕过 CSS 解析器的样式表；CSS 压缩更注重浏览器兼容（缺省使用 Browserslist 的 `defaults`）；`dropOverriddenDeclarations`、`convertApproximateColors` 可启用更激进的转换；`minimizeOptions.json` 可压缩 `.json` 与 `.webmanifest` 资源。
- 🧩 **多配置插件**：可直接在配置数组上挂载 `plugins`，Webpack 会把每个插件对 `MultiCompiler` 应用一次，适合 `ProgressPlugin` 等需跨构建工作的插件。
- 🛠️ **其他小改动**：更多位置支持 glob 过滤器（如 `**/node_modules`、`{ glob: "..." }`）；更多内置插件与工具 API 公开；`Harmony*` 名称弃用，改用 `ESM*`；无 source map 的模块在计算构建哈希后释放冗余源码缓冲区。
- 🐞 **问题修复**：修复缓存重建、watch 模式删除文件、HMR 新增延迟导入、共享运行时的异步样式表加载，以及 `output.clean` 保留最新热更新文件等问题。
- 🙏 **致谢**：感谢所有贡献代码、测试修复、改进文档和报告问题的社区成员及赞助者。

---

### [Astro 7.4 | Astro](https://astro.build/blog/astro-740/)

**原文标题**: [Astro 7.4 | Astro](https://astro.build/blog/astro-740/)

Astro 7.4 正式发布，本次更新的重点是为 `astro build` 加入了 `--timings` 构建耗时分析标志。此外，还支持为预渲染页面和按需页面分别指定图片服务，为自定义入口点提供 `notFound()` 处理器，并对字体配置给出警告。本次还更新了最低 Node.js 版本要求，并带来两个实验性功能：多线程并行预渲染，以及可自定义的静态重定向页面。

- 🚀 **构建耗时分析**：`astro build --timings` 会输出构建各阶段、Vite 插件、Markdown 处理、页面渲染、图片转换以及各集成的耗时明细与占比，帮助你快速定位性能瓶颈。
- 📊 **实战示例**：在 blog starter 中，页面生成占总构建时间的 81%，其中最慢的页面都使用同一博客文章布局；改用 `Promise.all()` 并行请求评论与用户资料后，页面生成从 2.10s 降至 1.13s。
- 🖼️ **构建与运行时图片服务分离**：`image.service` 现在可同时配置 `build` 和 `runtime` 两个服务：前者用于预渲染页面，并支持开发环境；后者用于按需页面。只配置一个服务时，行为与之前一致。
- 🔧 **集成作者注意事项**：配置了两套服务时，`entrypoint` 和 `config` 为 `undefined`，因此需检查 `runtime` 属性；自定义预渲染器需在 `getStaticPaths()`、`render()` 中透传图片元数据；需同步升级 `@astrojs/cloudflare` 与 `@astrojs/markdoc`。
- 🧭 **`notFound()` 处理器**：在自行组合 `astro/fetch` 或 `astro/hono` 的处理器时，把 `notFound()` 放在 `pages()` 之前，即可渲染自定义 404 页面，而不是返回空白 404。
- 🔤 **字体配置警告**：字体提供方可通过可选的 `getFontProperties()` 回调上报实际支持的字重、样式、子集与格式，Astro 会对配置中不受支持的值发出警告；该回调在 Astro 7 中可选，到 Astro 8 将成为必需；`init()` 上下文新增带重试的 `fetch()`。
- 📦 **最低 Node.js 版本**：Astro 及官方集成的最低支持版本提升至 Node.js 22.22.0，升级 Astro 前需先升级 Node.js。
- ⚡ **实验性：并行预渲染**：启用 `experimental.parallelPrerender` 后，静态页面会在 Node.js worker 线程中渲染，默认使用除一个核心之外的所有 CPU 核心，可通过 `workers` 调整；适配器自带预渲染方式时（目前只有 `@astrojs/cloudflare`）该标志无效。
- 🔁 **实验性：自定义重定向页**：启用 `experimental.redirectPage` 并创建 `src/pages/3xx.astro`，即可自定义静态构建中 `<meta http-equiv="refresh">` 重定向页的样式与文案，页面会接收 `from`、`to`、`status`、`delay` 属性。
- 🗂️ **其他改进**：集成与 Vite 插件现在可以控制构建输出目录；Vite 构建清单会保留到所有 `buildApp` 钩子执行完毕。
- ⬆️ **升级方式**：推荐使用 `npx @astrojs/upgrade` 自动升级，也可通过 npm、pnpm 或 yarn 手动安装 `astro@latest`。

---

