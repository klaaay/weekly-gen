### [Discord 将弃用 Electron，其新应用占用更少内存 | The Verge](https://www.theverge.com/news/1027379/discord-ditching-electron-web-app)

**原文标题**: [Discord is ditching Electron and its new app uses less RAM | The Verge](https://www.theverge.com/news/1027379/discord-ditching-electron-web-app)

Discord 正推动桌面应用从 Electron 全面迁移到 Rust，以降低资源占用并提升性能；移动端将保留原生 UI，但通过 Rust 与桌面端共享应用代码。完整切换时间尚未公布，Discord 希望尽快进入用户测试阶段。

- 🦀 Discord 将桌面客户端全面转向 Rust，目标是把整个客户端迁移到 Rust
- 🚫 Electron 将被弃用，React Native 也不再用于该迁移方案
- 📱 移动端继续保留原生 UI，但会通过 Rust 与桌面端共享应用代码
- 🧠 Electron 应用以占用系统资源高著称，迁移有望显著降低内存使用
- 📉 Discord CTO 展示 Windows 客户端仅占用 290MB RAM，而当前版本在多服务器场景下常超过 1GB
- 🛠️ Discord 自 2018 年起已采用 Rust，部分基础设施、语音技术和现有客户端已使用 Rust
- ⏳ 全面切换时间未定，但官方希望很快让用户参与测试
- ✍️ 该消息由 The Verge 的 Tom Warren 于 2026 年 11 月 5 日报道

---

### [Stanislav on X: "We've been early adopters of Rust since 2018 and a lot of our infra, voice tech, and even some of the current client is already Rust, the holy grail was getting the whole client there. That means Electron goes away, and so does React Native, mobile keeps native UI but shares app co… / X](https://x.com/svishnevskiy/status/2118081920194203799)

**原文标题**: [Stanislav on X: "We've been early adopters of Rust since 2018 and a lot of our infra, voice tech, and even some of the current client is already Rust, the holy grail was getting the whole client there. That means Electron goes away, and so does React Native, mobile keeps native UI but shares app co… / X](https://x.com/svishnevskiy/status/2118081920194203799)

Discord CTO 表示，Discord 正推进将桌面客户端从 Electron 重写为完全原生 Rust 客户端；移动端保留原生 UI，并通过 Rust 与桌面端共享应用代码。该计划已酝酿多时，目标是把整个客户端迁移到 Rust，并希望很快进入用户测试阶段。

- 🦀 Discord 自 2018 年起就是 Rust 的早期采用者，部分基础设施、语音技术和现有客户端已使用 Rust。
- 🖥️ 桌面客户端的“终极目标”是整体迁移到 Rust，届时 Electron 将被移除。
- 📱 React Native 也将不再使用；移动端保留原生 UI，但通过 Rust 与桌面端共享应用代码。
- ⚙️ 新客户端并非使用 Tauri，而是基于 GPUI 构建。
- 🧪 Discord 希望尽快让新客户端进入用户测试阶段。
- 😄 该 CTO 还调侃称，之后要继续盯着《WoW Forever》的登录界面。

---

### [“Maybe React Native Is Impossible” Alex Mikucki x Chas Jhin From Discord | Software Mention Podcast - YouTube](https://www.youtube.com/watch?v=NYOM5ujWI9Y)

**原文标题**: [“Maybe React Native Is Impossible” Alex Mikucki x Chas Jhin From Discord | Software Mention Podcast - YouTube](https://www.youtube.com/watch?v=NYOM5ujWI9Y)

该内容为 YouTube 页面底部导航与版权信息。该页面并未包含具体文章正文，主要列出平台介绍、政策条款、创作者、广告主、开发者等入口，以及 Google LLC 的版权声明。

- 🧭 提供 About、Press、Copyright、Contact us 等基础信息入口。
- 👥 包含 Creators、Advertise、Developers 等面向创作者、广告主和开发者的链接。
- 📜 列出 Terms、Privacy、Policy & Safety 等条款、隐私与安全政策。
- ⚙️ 包含 How YouTube works，用于说明平台运作方式。
- 🧪 提供 Test new features 入口，用于测试新功能。
- ©️ 底部声明版权归属 © 2026 Google LLC。

---

### [构建本地 AI 编程工作流 | Master.dev](https://master.dev/courses/local-ai/?utm_source=email&utm_medium=reactstatus&utm_content=localaicooper)

**原文标题**: [Build a Local AI Coding Workflow | Master.dev](https://master.dev/courses/local-ai/?utm_source=email&utm_medium=reactstatus&utm_content=localaicooper)

本课程由 Web Dev Simplified 的 Kyle Cook 主讲，时长约 4 小时 3 分钟，评分 4.9，发布于 2026 年 9 月 10 日，属于 AI Engineering 与 Coding with AI 学习路径。课程主张用本地模型掌控 AI 栈：代码保持私有、每 token 成本为零，并避免供应商限流、涨价或停服。学员将理解模型家族、格式与量化如何匹配硬件，并用 LM Studio 为 VS Code 和终端智能体提供开源模型服务，支持远程访问；前提是了解智能体 AI 编码，并拥有可运行本地模型的电脑，如 Apple Silicon Mac 或带独显 PC。

- 🔒 本地运行 AI 模型可保护代码隐私，且每 token 成本为零，不受供应商限流、重新定价或关停影响。
- 🧠 课程讲解模型如何运行：神经网络结构、训练与推理、token 与上下文、温度/Top K/Top P/seed 等采样参数。
- 💻 硬件重点包括 CPU、GPU、显存与内存；GPU（如 Nvidia CUDA）更适合 AI，模型需尽量完整放入显存以避免明显变慢。
- 🗂️ 学习在 Hugging Face 查找模型：理解模型家族、命名、参数、任务、格式、来源可信度与量化版本。
- 🧩 区分通用/编码、instruct、reasoning、vision、tool calling、embedding/re-ranker 等能力模型，以及 dense 与 MOE。
- ⚙️ 介绍多 token 预测、GPU/CPU 卸载、上下文长度、KV cache 量化、批大小等运行与内存优化设置。
- 📦 比较 GGUF 与 MLX 格式及 LM Studio、VLLM 等运行时；MLX 对 Apple 系统更优化。
- 🧮 解释 FP32、FP16、Q8 等量化如何压缩模型、影响文件大小与质量，并按硬件与上下文需求选型。
- 🛠️ 将 LM Studio 配置为本地服务器，使用 OpenAI 兼容接口连接 VS Code 扩展、Pi 终端编辑器等智能体编码工具。
- 🌐 通过 LM Link 或 Tailscale 实现远程访问本地模型，并涉及设备审批、访问控制等团队/企业功能。
- ☁️ 讨论租用云 GPU 运行开源权重模型的取舍：更灵活但失去本地隐私，且需前期成本权衡。
- 🏁 结课建议从 Qwen 较小模型开始，再按硬件尝试更大模型；完成课程可获得结业证书。

---

### [Redux Toolkit v2.x 与 v3.0 路线图 · reduxjs/redux-toolkit · 讨论 #5536 · GitHub](https://github.com/reduxjs/redux-toolkit/discussions/5536)

**原文标题**: [Redux Toolkit v2.x and v3.0 roadmap · reduxjs/redux-toolkit · Discussion #5536 · GitHub](https://github.com/reduxjs/redux-toolkit/discussions/5536)

Redux Toolkit 维护者公布了 RTK 2.x 与 3.0 路线图：3.0 将改为仅发布 ESM、重构 RTK Query 和 createSlice 定制能力，并带来适度的破坏性变更；2.x 会先通过增量版本修复问题、清理内部实现并加入新功能。3.0 预计约 6-8 个月后发布，当前重点是收集社区反馈。

- 📦 RTK 3.0 将全面改为 ESM-only，以减小安装体积并简化构建与发布流程。
- 🛠️ RTK Query 将重构 `createApi` 的类型与模块扩展方式，计划把 endpoint 的 `query` 字段改名为 `request`，并调整 `state.api.queries` 结构以提升更新性能。
- 🧩 `createSlice` 将增强定制能力，支持添加自定义 creator，并改善未使用 thunk 时的 tree shaking。
- 🔁 计划将 `extraReducers` 重命名为 `respondTo`，先在 2.17 提供别名并弃用旧名，3.0 中移除。
- ⚙️ 探索可替换 Immer 的不可变更新接口；同时计划把 thunk 中间件移入 `redux` 核心包，并弃用 `redux-thunk`。
- 🚀 2.x 路线包括：2.14 内部正确性与性能、2.15 RTKQ 请求行为、2.16 缓存写入/更新语义、2.17 hydration/Suspense 与 3.0 准备。
- 🔮 后续 2.x 可能加入 `injectEndpoints` 命名空间、entity adapter 多索引、类型化派生 upsert 等能力。
- ⏳ 3.0 被视为“React 19 级别”的变更，多数代码无需改动，将提供 codemod、迁移指南和 lint 规则等辅助升级。
- 🧪 最低 TypeScript 版本可能提升至 TS6，并继续优化类型、性能与 Redux DevTools。
- 💬 维护者公开征集社区对 RTK Query 使用痛点和 3.0 破坏性变更的反馈，并强调“准备好再发布”。

---

### [November 2026 Security Release | Next.js](https://nextjs.org/blog/november-2026-security-release)

**原文标题**: [November 2026 Security Release | Next.js](https://nextjs.org/blog/november-2026-security-release)

Next.js 于2026年11月发布安全更新，修复多个缓存、响应处理与图片优化相关漏洞；建议尽快将依赖升级至 v16.4.5（Active LTS）或 v15.5.29（Maintenance LTS）。

- 🔴 **高危：跨租户缓存泄露**：同时使用 `unstable_cache` 与 `use cache` 且缓存函数读取租户等根参数时，冷缓存填充期间可能把其他租户的缓存结果返回并复用。
- 🟠 **中危：嵌套 `use cache` 跨根参数泄露**：内外层缓存函数异步完成顺序可能导致外层条目提前存储，从而向不同租户、站点或语言环境展示错误内容。
- 🟠 **中危：二进制参数导致跨用户缓存泄露/污染**：不同二进制参数可能产生相同缓存标识，若用于区分用户或账户，可能让调用者收到他人的缓存结果或把自己的结果暴露给他人。
- 🟠 **中危：自托管共享 shell 缓存污染**：启用 Cache Components、禁用或未设置 Partial Prefetching 的 `next start` 应用，可能被未认证请求污染共享页面 shell，导致错误服务端渲染内容或持续 404。
- 🟠 **中危：压缩响应帧残留导致跨客户端响应注入/泄露**：自托管应用原样转发解压后的响应体但保留原压缩帧头时，在特定 HTTP/1.1 反向代理与共享后端连接条件下，响应可能被分配给错误客户端。
- 🟠 **中危：Edge 路由通过内部响应头暴露 Cookie**：Edge Route Handlers/API routes 使用 `NextResponse.cookies.set()` 设置 Cookie 时，序列化 Cookie 可能出现在可被同源 JavaScript 读取的 `x-middleware-set-cookie` 头中，即使标记了 `HttpOnly`。
- 🟠 **中危：图片优化 SVG 拒绝绕过**：来自允许来源的攻击者控制图片可能被误判为 AVIF，绕过 `images.dangerouslyAllowSVG: false` 并进入 SVG 解析器；来源允许列表仍生效，需原生图片后端支持 SVG 解码。
- 🛡️ **安全计划**：Vercel 通过 Open Source Bug Bounty 与安全研究者合作；相关问题可联系 `security@vercel.com`。

---

### [@tkdodo.eu 在 Bluesky 上](https://bsky.app/profile/tkdodo.eu/post/3mzdpknm7x227)

**原文标题**: [@tkdodo.eu on Bluesky](https://bsky.app/profile/tkdodo.eu/post/3mzdpknm7x227)

Dominik 在 Bluesky 上表示，只有等低质量、灌水式的 PR 不再持续涌入，并且不再占用他大部分开源时间之后，他才能开始开发 Query v6。

- 🧑‍💻 发帖人：Dominik（tkdodo.eu）
- 🧩 核心信息：Query v6 的开发启动被推迟
- 🚧 主要原因：大量“slop PR”持续占用其分配的开源时间
- ⏳ 启动条件：待这类 PR 停止涌入后，才开始 Query v6
- 😮‍💨 语气：配以 🫠 表情，表达无奈与疲惫
- 🕒 发帖时间：2026-11-02T16:10:08.780Z

---

### [简化 Vercel 上的运行时缓存 - Vercel](https://vercel.com/blog/simplifying-runtime-caching-on-vercel)

**原文标题**: [Simplifying runtime caching on Vercel - Vercel](https://vercel.com/blog/simplifying-runtime-caching-on-vercel)

Vercel 将 Data Cache 整合进 Runtime Cache，为开发者提供统一的数据缓存产品，覆盖 Next.js 与其他框架/API。现有 Next.js `fetch` 缓存和 `unstable_cache` 用户无需改代码，Pro 与 Enterprise 项目将获得更大的存储配额，同时缓存计费与可观测性也统一到 Runtime Cache。

- 🗂️ Data Cache 并入 Runtime Cache，统一 Vercel 上的数据缓存能力，减少多套缓存体系带来的管理复杂度。
- 🔁 使用 Next.js `fetch` 缓存或 `unstable_cache` 的代码无需修改；Pro 和 Enterprise 项目会获得更大存储空间。
- 🧩 Runtime Cache 支持通过 `@vercel/functions` 的 `getCache` 直接使用，可用于 Routing Middleware 功能开关查询、构建期 CMS 内容缓存，以及 SvelteKit、Nuxt 等框架的数据缓存。
- ⚙️ Next.js 的 `'use cache: remote'` 也通过 Runtime Cache API 缓存函数和组件输出。
- 🌍 基础设施由 Go API 和每个 Vercel 区域的 Redis 集群组成；每小时处理超过 4.4 亿次读取、移动超过 18 TB 数据。
- 🏎️ 每个区域独立缓存，命中通常只需一次区域内往返；Vercel 通过短期凭证处理认证，开发者无需管理 API Key。
- 🏷️ 缓存条目保存标签和写入时间；标签失效只写入一个时间戳，并通过全球推送管道在数百毫秒内同步到其他区域。
- ⚡ 新增熔断机制，在流量高峰时用内存中的标签时间戳临时判断新鲜度，避免慢分片拖慢读取；最大区域 p99 读取延迟降至约原来的五分之一。
- 📈 Pro 项目 6 月、Enterprise 项目 10 月提高存储预算，减少缓存驱逐；频繁驱逐的 Enterprise 项目缓存未命中率约一天内减半。
- 🔍 Observability 中新增部署标记、重新验证原因和写入利用率，便于关联发布与缓存行为、排查刷新原因和识别低效写入。
- 💳 迁移后四类 API 统一使用 Runtime Cache 的存储预算和用量工具；Pro 每个项目和环境获得此前团队池 8 倍空间，Enterprise 获得此前 Data Cache 存储的 10 倍。
- 🧾 此前未计费的 Data Cache 读写将按 Runtime Cache 定价计费；新团队自动使用 Runtime Cache，现有团队会提前收到迁移与账单详情，建议迁移前检查缓存用量并遵循优化指南。

---

### [Data Cache 正在迁移至 Runtime Cache - Vercel](https://vercel.com/changelog/data-cache-is-moving-to-runtime-cache)

**原文标题**: [Data Cache is moving to Runtime Cache - Vercel](https://vercel.com/changelog/data-cache-is-moving-to-runtime-cache)

Data Cache 退出 beta 并迁移至 Runtime Cache；Next.js 的 `fetch` 缓存与 `unstable_cache` 将随版本自动切换、无需改代码。Pro 和 Enterprise 获得更大的独立存储配额，迁移后按 Runtime Cache 用量计费，并公布 Hobby、Pro、Enterprise 的迁移与提前选择加入安排。

- 💾 **缓存迁移**：Data Cache 退出 beta，迁移至 Runtime Cache；Next.js `fetch` 与 `unstable_cache` 会在每个版本自动切换，无需修改代码。
- 📦 **存储配额**：Pro 每个项目和环境获得独立 Runtime Cache 存储，容量为旧 Data Cache 团队共享池的 8 倍；Enterprise 项目为旧 Data Cache 存储的 10 倍。
- 💰 **计费变化**：团队迁移后，原本不计费的 Data Cache 读写按 Runtime Cache 定价收费；起价为每百万读单元 $0.40、每百万写单元 $4.00，并因区域而异。
- 🆓 **免费额度**：Hobby 团队所有项目每月合计免费 100 万读单元和 20 万写单元；Pro 用量从每月 $20 基础设施额度中扣除，超出部分按区域费率计费；Enterprise 定价需联系客户团队。
- 🗓️ **默认与迁移时间**：2026 年 10 月 30 日及之后创建的团队默认使用 Runtime Cache；已有 Data Cache 的 Hobby 团队将于 2026 年 11 月 29 日迁移，Pro 会通知迁移日期和计费生效时间，Enterprise 由客户团队联系。
- 📊 **迁移前优化**：迁移前可在 Observability 查看项目 Data Cache 用量，按优化指南或代理提示减少不必要的读写；也可在 Runtime Cache 仪表盘选择 Vercel Agent 优化。
- ⏩ **提前选择加入**：2026 年 10 月 30 日起，现有 Hobby 和 Pro 团队可在团队 CDN 设置中提前选择加入；选择加入后立即适用 Runtime Cache 定价。
- ⚙️ **禁用缓存**：可在 CDN 设置中禁用 `fetch` 和 `unstable_cache` 缓存，这会增加对数据源的请求，但不会阻止迁移。
- 📝 **延伸阅读**：架构和近期改进可查看相关博客文章。

---

### [在安装前和安装过程中阻止恶意 npm 包 - Vercel](https://vercel.com/changelog/blocking-malicious-npm-packages-before-and-during-installation)

**原文标题**: [Blocking malicious npm packages before and during installation - Vercel](https://vercel.com/changelog/blocking-malicious-npm-packages-before-and-during-installation)

Vercel 新增 npm 依赖安全检查，在构建安装依赖前后拦截被封锁的软件包版本，防止恶意安装脚本运行，并自动应用于所有套餐的新构建。

- 🛡️ Vercel 在构建的依赖安装前和安装过程中检查被封锁的 npm 包，帮助阻止恶意安装脚本执行。
- 🚫 检查基于特定包版本的封锁列表，这些版本因恶意软件或安全漏洞被选中；新规则通常几分钟内生效于新构建。
- 📦 安装前，Vercel 会检查支持的 lockfile，包括从构建缓存恢复依赖时。
- ⏳ 安装期间，Vercel 会阻止受影响公共 npm 包的下载。
- ✅ 部署前仍会继续检查已安装依赖和函数输出。
- ⚙️ 这些保护自动应用于所有套餐的新构建，无需配置。
- ❌ 若检测到被封锁依赖，部署会失败，错误中会标明包和版本，并尝试使受影响的构建缓存失效。
- 🔄 需将依赖更新到安全版本并更新 lockfile，然后重新部署。

---

### [[experiment] support App Router route.go handlers by timneutkens · Pull Request #100130 · vercel/next.js · GitHub](https://github.com/vercel/next.js/pull/100130)

**原文标题**: [[experiment] support App Router route.go handlers by timneutkens · Pull Request #100130 · vercel/next.js · GitHub](https://github.com/vercel/next.js/pull/100130)

该 PR（#100130）已合并至 vercel/next.js 的 canary 分支，为 App Router 增加实验性的 `route.go` 处理器支持；开启 `experimental.goRoutes` 并使用 Turbopack 时，可通过 Go 的 `package main` 定义 `GET`、`POST` 等 HTTP 方法，并自动获得 HEAD/OPTIONS 行为及处理器签名校验。

- 🚀 基于 #99980 扩展，允许在 App Router 中使用 Go 编写路由处理器。
- 🧩 Go 源码发现、声明分析、编译、持久化缓存、目标构建和编译器生命周期由 `turbopack-go` 负责；本 PR 提供 Next.js 路由约定、生成的 HTTP 入口、原生端点元数据和运行时集成。
- ⚙️ 开发环境和自托管 `next start` 仍由 Node.js 处理路由、重写和 `proxy.ts`；受监管的私有 Go worker 保留流式响应、headers、cookies、参数、取消与故障恢复，生产环境会重试临时启动失败。
- 📦 部署适配器可获得带 `runtime: 'go'` 和可执行 `filePath` 的 `APP_ROUTE` 输出；`goTarget` 选择可执行目标，复制出的基于 PORT 的服务器无需 Next.js 或 Go 工具链即可运行。
- 🛡️ NAPI 通过端点的外部输入有效性接口工作，而非检查 Go 文件系统；适配器路由元数据和参数处理仍属于 Next.js 集成。
- ✅ 验证包括 Rust clippy、完整工作区/原生构建与 TypeScript 检查；Go 路由开发测试 18 项通过，生产测试 15 项通过（含 host/amd64/arm64），服务器追踪测试与快照通过。
- 🔍 无关的图片滚动断言已拆分至 #101009；已知原生事件监听失败记录在 #99980，托管部署测试限制记录在 fixture README。
- 🧾 该 PR 共 39 个提交，125 项检查通过，jamiboym 批准后合并；后续还有 #100918 整合 Turbopack 开发路由发现。

---

### [理解 React 内部机制](https://www.alexandretrotel.org/articles/understanding-react-internals)

**原文标题**: [Understanding React internals](https://www.alexandretrotel.org/articles/understanding-react-internals)

这篇文章旨在深入讲解 React 内部机制，而不是停留在 hooks 的使用层面；核心观点是 React 本质上是一个调度器，负责决定渲染内容、渲染时机以及哪些工作可以等待。文章将覆盖异步 React、lanes、服务端到客户端的组件序列化、hydration 等通常隐藏的机制，并强调阅读源码和反复理解的重要性。

- 🧩 大多数人通过 hooks 学习 React，但 hooks 只是表层接口，并不是 React 的核心。
- ⚙️ React 底层是一个调度器：它决定渲染什么、何时渲染、哪些任务可以延迟，并与浏览器交互、拆分任务、在更高优先级任务到来时暂停。
- 🌐 文章深入探讨异步 React、lanes、服务端与客户端之间的组件序列化、hydration 以及通常不可见的内部机制。
- 📚 部分内容较难理解，作者建议不必一次全部掌握，可以阅读后回顾并反复学习。
- 🔍 理解 React 的最佳方式是阅读 React 源码；包括本文在内，其他材料都只是对源码的解读。
- 🧠 读完后应能更好地掌握 React，理解每个 hook 的使用场景及原因，并建立服务端、客户端与浏览器交互的心智模型。

---

### [宣布 Vega 2.0 正式发布](https://developer.amazon.com/apps-and-games/blogs/2026/10/vega-2-0-sdk-launch)

**原文标题**: [Announcing Vega 2.0 general availability ](https://developer.amazon.com/apps-and-games/blogs/2026/10/vega-2-0-sdk-launch)

Vega 2.0 正式发布：Vega OS 2.0、Vega SDK 2.0 与高级 Vega 开发者工具全面可用，并结束开放测试；Vega OS 已运行于全球数千万台设备，包括 Echo 与 Fire TV，Vega OS 2.0 已推送至所有由 Vega 驱动的 Fire TV 设备。

- 🚀 三大提升：应用性能、构建速度与开发信心。
- ⚛️ 引入 React Native 0.83、React 19 与 React Compiler：构建期自动处理记忆化，减少手动 `React.memo`、`useCallback` 和依赖数组维护，降低 CPU 开销，改善目录页等大量瓦片场景的渲染性能。
- ⚡ Hermes v1 与 React Native DevTools：优化代码编译和设备运行表现，便于定位性能瓶颈；React Navigation、Reanimated、Lottie 等常用库已兼容更新，并新增 `boxShadow`、`outline` 等 TV 焦点样式能力。
- 🧩 Vega 原生 API：支持任务调度、自定义 UI 组件等 React Native/WebView 之外的能力，可在 React Native 应用中按需加入原生功能；原生工具与 AI 开发能力处于早期访问阶段。
- 🤖 Amazon Devices Builder Tools（ADBT）for AI：为 AI 编码代理提供 Vega 与 Fire TV 专属知识和工作流，支持 Java/Kotlin 应用从 Fire OS 迁移、React Native 0.72 升级至 0.83 规划、性能调试与无障碍流程；合作伙伴反馈 AI 辅助代码迁移可少于 1 天（不含测试）。
- 💬 DevAssistant：在开发者文档门户中用官方文档回答 Vega 问题，新增领域选择、聊天历史、页面级上下文、搜索概览和语言本地化支持。
- 🛡️ API 稳定性：次要 SDK 版本保持 API 一致，破坏性变更仅随年度大版本发布；未来每年一次大版本，并按固定节奏发布小版本。
- ✅ 下一步：现有应用可下载 Vega 2.0 SDK 并查看发布说明；React Native 0.72 应用建议迁移至 0.83，并用 ADBT 生成迁移计划；新开发者可通过教程、示例应用和 GitHub 资源上手。

---

### [Vega SDK 发行说明 - Amazon Vega 文档](https://developer.amazon.com/docs/vega/2.0/vega-release-notes)

**原文标题**: [Vega SDK Release Notes - Amazon Vega Docs](https://developer.amazon.com/docs/vega/2.0/vega-release-notes)

Vega SDK 2.0、Vega OS 2.0 与 Vega 开发者工具正式全面可用，核心升级到 React Native 0.83，并新增 C++ 原生 UI/后台任务、AI 迁移辅助、JavaScript/TypeScript 与原生代码兼容性 lint。此次发布同时引入 API 稳定性承诺和多项破坏性变更，修复媒体、输入、测试等问题，但仍列出若干需规避的已知问题。

- 🚀 正式发布：Vega SDK 2.0、Vega OS 2.0 和开发者工具结束公测；OS 2.0 已推送至所有 Vega Fire TV 设备，开发需使用 OS 2.0。
- ⚛️ React Native 0.83：带来 React 19、React Compiler、Hermes v1、React Native DevTools，以及 `boxShadow`、`outline` 等焦点样式；React Navigation、Reanimated、Lottie 等库已支持。
- 🧩 原生能力：可用 Vega native APIs 在 C++ 中构建自定义 UI 组件和周期性后台任务；后台任务最短间隔 60 秒，单次最长运行 5 分钟，原生工具处于公测。
- 🤖 AI 辅助迁移：推荐使用 Amazon Devices Builder Tools (ADBT) for AI 规划 RN 0.72 到 0.83 升级、Fire OS 应用迁移和性能问题调试。
- ✅ 兼容性检查：`vega project doctor` 新增 JS/TS 和原生代码 lint，可报告未保护的新 API、已移除 API、已弃用 API，并可作为 CI 门禁。
- 📌 API 稳定性：从 2.0 起，API 在次要版本间保持稳定，破坏性变更仅随每年一次的大版本发布；manifest 支持声明 `min`/`target` OS 版本范围，需设置 `[os.version]` 并重新构建。
- ⚠️ 破坏性变更：OS 版本模块条目改为构建时生成；RN 0.83 库不再支持深层导入；`@amazon-devices/react-linear-gradient` 改为 `experimental_backgroundImage`；FlashList 改用 `@shopify/flash-list`；实验性 API 不再支持。
- ⌨️ TextInput 行为调整：未来 OS 版本中，单行 RN 0.83 `TextInput` 默认使用 `blurAndSubmit`；Done/Back 会触发 `onSubmitEditing` 并失焦/关闭键盘，需按 `submitAction` 过滤 `'previous'` 或设置 `submitBehavior="submit"`。
- ♿ Vega Studio 无障碍检查：A11y Inspector 可在编辑 `.tsx`/`.jsx` 时发现 VoiceView 等辅助技术无法描述或操作的组件，并提供快速修复建议。
- 🔐 账户登录验证：`kcp-cli-v2` 可在设备上读取或实时监视 Content Launcher Account Login 状态，需开发者模式和旁加载应用，不支持 Vega Virtual Device。
- 🎬 媒体改进：React Native SVG 完整支持 `TextPath`；MSE 音频拼接实现更平滑的段边界处理，减少点击声、间隙和漂移。
- 🛠️ 已修复问题：包括 AC-3/E-AC-3 能力检查、dash.js 重试错误上报、暂停时视频表面缩放、MSSE 模式 `seeked` 事件、TextInput 焦点后光标位置、`vpm install-async` 退出、W3C Media API 文档格式、OS 1.2+ Appium 测试等。
- 🚨 已知问题：RN 0.83 应用若引入 RN 0.72 运行时会在启动时崩溃；Fire TV Stick HD (2026) HEVC 播放失败；部分 HEVC 直播 HLS/MPEG-TS、`removeSourceBuffer()` 卡死、视频像素宽高比、大型 DASH 清单卡顿、HMAC 密钥长度、刷新率/VPN IPv6/语音控制等问题仍存在。
- 📱 OS 构建号：Fire TV Stick 4K (3rd Gen) 2.0 为 `2502000007420`；Fire TV Stick HD 与 Fire TV Stick 4K Select 2.0 均为 `2602000052920`。

---

### [为什么我们最终离开 NextJS，转向 TanStack Start · Harrison Milbradt](https://harrisonmilbradt.com/writing/nextjs-to-tanstack-start)

**原文标题**: [Why we finally left NextJS for TanStack Start Â· Harrison Milbradt](https://harrisonmilbradt.com/writing/nextjs-to-tanstack-start)

文章回顾了作者将大型生产应用从 NextJS 迁移到 TanStack Start（部署于 Cloudflare Workers）的全过程：起因是 NextJS 多次升级带来内存泄漏、构建问题和版本回退；迁移采用渐进式“接缝”方案，让两套框架并行运行，并通过自动化校验确保行为不变；最终在 10 月完成切换，删除约 4.2 万行 NextJS 代码，并显著降低成本和提升开发效率。

- 🚨 离开 NextJS 的核心原因：16.3.0 与 16.3.4 出现不同原因的内存泄漏，`use cache` 命中时 `tee()` 分支未消费导致缓冲堆积。
- 🧱 还遇到 Turbopack 资源文件名含 `..` 被 Cloudflare 判定为路径穿越而 403，只能回退版本，半年内频繁 pin/revert。
- 🧭 先尝试 OpenNext，但大型应用因 bundle 体积、Redis Cache Components、依赖补丁和性能问题基本不可行。
- 🛠️ 迁移策略不是“大爆炸重写”，而是建立框架适配层，把导航、图片、headers、Sentry、Sanity、缓存、env 等导入统一封装。
- 🔁 通过构建时别名在 NextJS 与 TanStack 版本间切换，并用 codemod 迁移旧导入，再加 lint 规则禁止业务代码直接引用 `next/*`。
- ✅ 切换前先写校验脚本：把 NextJS `src/app` 转成 URL 模式，检查 TanStack 路由树是否缺失；再对比数百 URL 的状态码、重定向、headers、cookies 和 SEO 标签。
- 📊 建议先拿生产环境对生产环境跑基线，识别原本就存在的噪声，如 307/301 差异和偶发 404/200，避免误判为迁移 bug。
- 🚀 上线时每个构建先上传为 Workers 版本，检查 secrets、扫描客户端 bundle、限制体积；切换当天主要只是改 DNS，随后删除旧 ECS 部署和 NextJS 应用。
- ⚠️ 迁移后的坑包括：Vite 丢弃 Zod locale 导致错误信息变成 “Invalid input”、部署后旧标签页找不到 JS chunk、删除 NextJS 页面时测试覆盖丢失，以及年轻生态的安全公告。
- 💰 迁移收益明显：NextJS 服务器渲染成本约每月 500–1000 美元，日志查询报价约 1400 美元/月；切换后本地开发与构建更快，依赖升级更干净。
- 📈 作者提交频率从迁移前约 40 次/周，迁移中约 130 次/周，切换后约 210 次/周；后续小 PR 还减小了客户端 JS，并提升移动端 Lighthouse 分数。
- 🎯 最大经验：先明确目标并围绕目标验证；保持框架边界干净；迁移前建立验证流程；先做原型，不要假设一切会顺利。

---

### [可写派生状态：停止同步状态 | 趣味编程](https://playfulprogramming.com/posts/writable-derived-state/)

**原文标题**: [
	Writable Derived State: Stop Synchronizing State | Playful Programming
](https://playfulprogramming.com/posts/writable-derived-state/)

概述：本文介绍 React 中的“可写派生状态”模式：当界面需要先显示服务端默认值、又允许用户修改时，不应使用 `useEffect` 将服务端状态同步到本地状态，而应让本地用户状态可为空，并通过派生值优先使用用户数据、缺失时回退到服务端数据。

- 🔄 常见实现是用 `useState` 保存服务端数据和本地数据，再用 `useEffect` 在服务端数据更新时覆盖本地状态。
- ⚠️ 这种做法会导致刷新服务端数据或重新访问标签页时，用户未保存的修改被重置，因为服务端状态被默认为“总是获胜”。
- ✅ 更优方案是把用户状态设为 `null`，最终数据用 `userTodos ?? serverState.payload ?? []` 派生：有用户数据时用用户数据，否则用服务端数据。
- 🧠 心智模型应从“把服务端状态同步到客户端”改为“仅在客户端数据缺失时使用服务端数据”。
- ⚛️ 该模式同样适用于 TanStack Query：用 `manualTodos ?? serverTodos ?? []` 派生数据，并在保存成功后重新获取服务端数据、再把本地覆盖状态设回 `null`。
- 🧹 这种写法还能移除不必要的 `useEffect`，符合 React 官方“You Might Not Need an Effect”的建议。
- 📌 结论：可写派生状态能让客户端与服务端状态管理更可预测、更简单，并减少副作用与同步逻辑。

---

### [Skullet 🦴 Smart skeleton states](https://skullet.lochie.me/)

**原文标题**: [Skullet 🦴 Smart skeleton states](https://skullet.lochie.me/)

文章强调“为等待而设计”的重要性，指出加载状态是用户首先看到的内容，在慢速网络下更是用户最常看到的部分。

- ⏳ 主题是“为等待而设计”，关注加载状态与用户等待体验。
- 👀 加载状态是用户首先看到的内容。
- 🐢 在慢速连接下，加载状态是用户最常看到的内容。
- ✍️ 作者为 John Doe。
- ⏱️ 全文阅读时长约 4 分钟。

---

### [宣布 Parcel 3 alpha](https://v3.parceljs.org/blog/v3-alpha/)

**原文标题**: [
      Announcing Parcel 3 alpha
    ](https://v3.parceljs.org/blog/v3-alpha/)

Parcel 3 首个 alpha 发布：这是用 Rust 从零重写的版本，构建速度最高提升 100 倍，并支持原生插件、内置常用 Web 语言处理、集中式配置和更智能的打包。整体架构不再依赖 Node，目标是显著提升冷构建性能、降低内存占用并减少缓存相关问题。

- 🚀 **发布信息**：2026-11-04 发布 Parcel 3 alpha，核心完全用 Rust 重写，最高比 v2 快 100 倍。
- ⚡ **性能基准**：Storybook 冷构建从 16.62s 降至 572ms（29×），文档站从 87.59s 降至 810ms（108×），库构建从 131.47s 降至 2.71s（49×）。
- 🧠 **内存优化**：三个基准场景内存占用分别减少 5.1×、6.6×、2.5×，最低降至 1.5GB。
- 🦀 **全原生架构**：CLI、开发服务器、转换器、打包器、优化器等均为原生实现，不再依赖 Node，可充分利用多核硬件。
- 🧩 **原生插件**：支持 Rust、Go、Swift 及 C ABI 语言编写动态库插件，可扩展语言支持、模块解析和产物优化。
- 🟨 **JavaScript/TypeScript 插件**：基于 QuickJS 的内嵌运行时，兼容部分 Node 能力，适合简单或低频插件；高性能场景建议用原生插件。
- 📦 **开箱即用**：内置 HTML、CSS、JS、TS、SVG、图片优化、RSS/Atom、Web Manifest，并新增 Tailwind、React Compiler、MDX、SVG→JSX、glob imports 等支持。
- ⚙️ **集中配置**：插件配置统一到 `.parcelrc`，构建开始时一次性解析，减少文件系统搜索并提升性能。
- ✂️ **更智能打包**：改进代码分割与合并成本模型，450 页站点每页 HTTP 请求减少 64%，传输字节减少 10%；CSS 顺序更安全，SVG 也支持 tree shaking。
- 📚 **库构建增强**：自动读取 `package.json#exports`，并行构建多入口/嵌套入口，按模块输出文件以利于使用方 tree shaking 和代码分割；`.d.ts` 生成后续回归。
- 🛠️ **开发体验**：支持受信任 HTTPS、本地证书、`--open` 复用浏览器标签页、内置 bundle analyzer，以及带 HMR 的 `parcel run` 命令。
- 💾 **简化缓存策略**：优先优化冷构建，仍支持内存增量重建，减少磁盘缓存和失效追踪带来的复杂性与 stale-cache bug。
- 📥 **试用方式**：安装 `parcel@next`，或安装 `@parcel/parcel3` 使用 `parcel3` 命令与 v2 并行试用；压缩器插件、`.d.ts`、自定义打包器插件、JS API 等仍在开发中。

---

### [GitHub - reticlehq/reticle: AI agents can generate code, but still struggle to understand what they build. Reticle brings Jev-style machine-native runtime perception to web & desktop applications. · GitHub](https://github.com/reticlehq/reticle)

**原文标题**: [GitHub - reticlehq/reticle: AI agents can generate code, but still struggle to understand what they build. Reticle brings Jev-style machine-native runtime perception to web & desktop applications. · GitHub](https://github.com/reticlehq/reticle)

overview summary  
Reticle 是一个开源、仅开发环境使用的运行时验证层，让 AI 编码代理通过 MCP 工具在真实运行的应用中“看、操作、观察、断言”，并返回 pass / fail / cannot tell 判定、证据和 file:line。它解决代理写完代码后只假设成功、不打开应用的问题，支持 Web 与 Electron/Tauri，并可用无模型回放流程和 CI gate 防止回归。

- 🧩 核心问题：AI 代理倾向于“产出改动并假设成功”，缺少真实运行验证；Reticle 把运行中应用里的真相变成可执行检查。
- 🔌 工作方式：在应用内注入 dev-only SDK，读取网络请求、store 状态、console、React 渲染、DOM 与源码位置，而不只看截图。
- ✅ 判定机制：每次检查输出 yes / no / unknown，只有 yes 算通过；结果附带请求、状态变化、console 行和 file:line。
- 🤖 代理兼容：通过 MCP 接入 Claude Code、Cursor、Codex、Windsurf、VS Code、Gemini CLI 等，覆盖多种 Web 框架和桌面端。
- 🚀 快速开始：`npx @reticlehq/server` 可零安装检查运行中的应用；`init` 接线 SDK 与代理；重启代理后验证真实流程。
- 🔁 流程回放：可保存验证为 flow，后续无需 AI 模型即可确定性重放，防止旧功能被新改动悄悄破坏。
- 🚦 CI 门禁：`reticle gate --since HEAD~1` 要求受改动影响的已保存流程有新的通过记录。
- 🛡️ 安全默认：SDK 不进入生产构建；本地桥仅监听 `127.0.0.1`；无 `evaluate` 工具；不绕过客户端权限提示；敏感信息替换为 `[REDACTED]`。
- 📦 供应链透明：Apache-2.0、公开仓库、CI 签名与 SLSA provenance、无 install 脚本、OpenSSF Scorecard 评分。
- 🔐 数据本地：默认不上传应用数据；链接项目或 CI 设置密钥后才同步；匿名 telemetry 可关闭。
- 🧪 适用验证：静默 500、界面与状态不一致、重复提交、缓存过期、权限与安全行为、可访问性、性能、SEO 等。
- 🆚 对比 Playwright：Playwright 适合外部站点、跨浏览器和像素级检查；Reticle 适合自有应用内部运行时，两者互补。
- 📊 基准：用 88 个注入 bug 的受控应用对比 Playwright；无模型回放成本低，第二轮起更快。
- ⚠️ 限制：暂不能看到 IndexedDB、Web Workers、closed shadow roots、跨源 iframe；对单动作竞态仅部分覆盖；无法判断时明确返回 unknown。
- 🧰 常用命令：`init`、`status`、`doctor`、`open`、`verify`、`gate`、`report`、`connect/sync`、`update`、`telemetry`、`feedback`。
- 🌍 社区与许可：Discord、GitHub Discussions、贡献指南与行为准则；npm 包 Apache-2.0，`reticle-tauri` 为 MIT。

---

### [Release 4.16.0 · bvaughn/react-resizable-panels · GitHub](https://github.com/bvaughn/react-resizable-panels/releases/tag/4.16.0)

**原文标题**: [Release 4.16.0 · bvaughn/react-resizable-panels · GitHub](https://github.com/bvaughn/react-resizable-panels/releases/tag/4.16.0)

本次发布为 react-resizable-panels 4.16.0，重点新增可拖拽重排的 Workspace 组件，并修复缩放、跨窗口 iframe 与分隔条预览相关问题。

- 🆕 新增 Workspace 组件，支持标签组之间拖拽、组内排序、拖到边缘拆分，以及调整大小和最大化。
- 🧩 Workspace 布局使用可序列化模型描述，标签移动时内容不会重新挂载；并支持自定义标签、工具栏、空标签组、关闭按钮及样式。
- ⚙️ Workspace 为非受控组件，类似 Group；可通过 useWorkspaceRef 和 useWorkspaceCallbackRef 获取命令式 API。
- 🔗 标签内容可使用 useParentWorkspace、useParentTabset、useParentTabsetState、useParentTab、useParentTabState 等 Hook 访问父级状态。
- 👁️ 未选中标签内容默认保持挂载，也可卸载或放入隐藏的 React <Activity>；选中标签内容可选择服务端渲染，并支持鼠标、触摸和键盘交互。
- 🛠️ 修复祖先元素存在 CSS zoom 或缩放变换时分隔条/网格线移动距离不准确的问题，改为将屏幕像素转换为布局像素。
- 🪟 修复跨窗口 iframe 导致分隔条停留在 hover 状态，以及另一窗口文档创建元素时分隔条调整预览缺少样式的问题。

---

### [react-resizable-panels | 灵活布局组件](https://react-resizable-panels.vercel.app/examples/workspace)

**原文标题**: [react-resizable-panels | flexible layout components](https://react-resizable-panels.vercel.app/examples/workspace)

未收到可摘要的正文内容，暂时无法提取文章要点；请补充原文后再生成摘要。
- 📭 当前输入为空，未包含可供总结的文章正文。
- ❓ 无法确认文章主题、关键信息与核心结论。
- 📝 请提供完整文本，我将按“概述摘要 + 表情符号要点”格式整理。

---

### [发布 11.1.0 · preactjs/preact · GitHub](https://github.com/preactjs/preact/releases/tag/11.1.0)

**原文标题**: [Release 11.1.0 · preactjs/preact · GitHub](https://github.com/preactjs/preact/releases/tag/11.1.0)

Preact 11.1.0 已发布，主要新增对 React Compiler 编译应用的支持，并包含 VNode 识别、布局副作用错误隔离、compat 样式处理及类型定义方面的修复与改进。

- 🚀 新增 `preact/compat/compiler-runtime`，支持使用 React Compiler 编译的应用
- 🔒 通过共享 symbol 标记强化 VNode 识别机制
- 🧩 将 layout-effect 错误隔离到抛错的组件，避免影响其他无关 effects 和生命周期回调
- 🎨 在 compat 中停止为无单位的 SVG paint 和 aspect-ratio 值追加 `px`
- 🧾 允许在所有有效 input 类型上使用 `list` 属性
- ⚠️ 新的 VNode 标记要求 `@preact/signals` 2.11.4 或更高版本，以及 `preact-render-to-string` 6.8.2 或更高版本
- 👏 本次发布贡献者包括 JoviDeCroock、dylanpulver 和 playlikeboy

---

### [xstate@6.0.0-beta.0 发布 · statelyai/xstate · GitHub](https://github.com/statelyai/xstate/releases/tag/xstate%406.0.0-beta.0)

**原文标题**: [Release xstate@6.0.0-beta.0 · statelyai/xstate · GitHub](https://github.com/statelyai/xstate/releases/tag/xstate%406.0.0-beta.0)

overview summary  
XState v6.0.0-beta.0 发布，标志 v6 进入 Beta；公开 API 不再计划破坏性变更，实验性 API 仍可能调整。本次重点包括快照恢复 API 重构、v5 遗留配置全面报错、错误诊断与类型改进。

- 🚀 **进入 Beta**：`xstate@6.0.0-beta.0` 为预发布版本，`@public` API 预计不再有破坏性变更，`@experimental` API 仍可能变化。
- 💾 **快照恢复迁移**：从 `createActor` 移至 `restoreActor`，并从新入口 `xstate/persist` 导出；`createActor` 仅创建新 actor，传入 `snapshot` 会抛错。
- 🔄 **`restoreActor` 能力**：支持任意 actor logic，接受除 `input` 外的 `createActor` 选项，可传入 `system`；会校验/迁移 machine 快照并恢复子 actor，无法恢复时产生 `'error'` 快照。
- 🗑️ **移除 `machine.restoreSnapshot()`**：该 API 被删除，改用 `restoreActor`。
- 🧩 **Schema API 改为函数**：`snapshotSchema` 和 `eventSchema` 现在需以函数调用，分别从 `xstate/persist` 和 `xstate` 导入。
- ⚠️ **v5 遗留配置全面抛错**：`createMachine(config, implementations)`、`setup(...).createMachine(config, implementations)`、机器配置中的 `services`/`activities`/`devTools` 等不再仅开发环境警告。
- 🛠️ **`createActor` 严格校验选项**：未知选项会抛错；`systemId` 改名为 `registryKey`，并提示替代用法。
- ♾️ **宏步默认无界**：`maxIterations` 不再默认 `1000`；开发构建超过 1000 微步会警告一次，可显式设置 `maxIterations` 触发 `InfiniteTransitionError`。
- 🧪 **生产错误短码**：生产构建用短错误码和诊断信息，并附错误码文档链接；开发消息保持不变。
- 🔍 **生命周期事件校验**：在 `on` 中使用 v5 后缀生命周期事件类型会抛错；应改用类别类型配合 `matches`，通配符和 `xstate.snapshot.actor` 不受影响。

---

### [发布 @tanstack/redact@0.3.0 · TanStack/redact · GitHub](https://github.com/TanStack/redact/releases/tag/%40tanstack%2Fredact%400.3.0)

**原文标题**: [Release @tanstack/redact@0.3.0 · TanStack/redact · GitHub](https://github.com/TanStack/redact/releases/tag/%40tanstack%2Fredact%400.3.0)

TanStack 发布 `@tanstack/redact@0.3.0`，这是一次包含浏览器 SPA 插件支持和 Vite 相关能力共享的次要版本更新。

- 📦 发布版本为 `@tanstack/redact@0.3.0`，包含 8 个提交并合入 `main`。
- 🧩 新增面向 Webpack 和 Rspack 的浏览器 SPA 插件，并提供 Rsbuild 配置指南。
- 🔧 共享 Vite 的功能选择与包解析逻辑，保留精确别名和包归属信息。
- ⚛️ 必要时将所选运行时适配到 React 18。
- 🔗 相关变更对应 PR `#143`。
- 🔒 该发布为不可变版本，仅发布标题和说明可修改。

---

### [发布 0.89.0-rc.0 · react/react-native · GitHub](https://github.com/react/react-native/releases/tag/v0.89.0-rc.0)

**原文标题**: [Release 0.89.0-rc.0 · react/react-native · GitHub](https://github.com/react/react-native/releases/tag/v0.89.0-rc.0)

React Native v0.89.0-rc.0 是预发布版本，包含 52 个提交，重点涵盖破坏性变更、新架构清理、性能优化、Android/iOS 修复以及旧 API 移除。升级时需重点关注 Codegen JNI 重新生成、Community CLI 配置、CocoaPods/SwiftPM 头文件路径和已弃用 API。

- 🚨 破坏性变更较多：`AccessibilityState::selected` 改为 `std::optional<bool>`，`react-native/assets-registry` 被移除，CLI 插件需显式加入 `devDependencies`。
- 🧱 新架构进一步收紧：bridgeless 始终启用，移除 `bridgelessEnabled`、`fabricEnabled`、`turboModulesEnabled` 等旧配置入口及相关初始化方法。
- 🍎 iOS 旧架构 API 大量清理：移除多个废弃 `RCTBridge` 初始化器、`RCTModuleData`、旧 `RCTTimingModule`、旧动画模块等。
- 🤖 Android 侧移除 `rncore.h`，Codegen 需用 0.89 重新生成 JNI；`targetSdk` 更新至 37，Kotlin、NDK、fbjni、Fresco 等依赖升级。
- ✨ 新增 `useAppState()` Hook，便于订阅应用前后台状态变化。
- 🌐 Web API 增强：全局暴露 `structuredClone` 和 `DOMException`，并扩展对 ArrayBuffer、DataView、TypedArray、BigInt、Error 子类等的支持。
- 📝 Text 能力增强：Android 13+ 新增 `lineBreak`、`wordBreak`；新增实验性最长行宽测量；默认启用文本布局缓存和 Android 文本测量优化。
- 📐 新增 `experimental_onSafeAreaInsetsChange` 视图属性，用于报告被系统 UI 覆盖的安全区域。
- ⚡ 性能优化覆盖渲染、JNI、Yoga、VirtualizedList、Text、Touch Handling 等路径，减少动态转换、重复分配和 JNI 调用。
- 🧪 新增/增强开发能力：Android TurboModules 支持 Activity Result API，CocoaPods/SwiftPM 增加严格 C++ API 选项，DevTools 升级并修复多项调试问题。
- 🧹 移除/弃用旧 API：`TextInput` 的 `blurOnSubmit`、`hasTVPreferredFocus`、`unstable_getScrollParent`、旧 UIManager 生命周期方法等被移除或弃用。
- 🛠️ 修复大量问题：包括 Animated 插值/原生驱动、Babel、WebSocket、Text/TextInput、ScrollView、Modal、Accessibility、Yoga、DevTools 和样式解析等。

---

### [发布 v11.0.0-beta.0 · storybookjs/storybook · GitHub](https://github.com/storybookjs/storybook/releases/tag/v11.0.0-beta.0)

**原文标题**: [Release v11.0.0-beta.0 · storybookjs/storybook · GitHub](https://github.com/storybookjs/storybook/releases/tag/v11.0.0-beta.0)

Storybook 发布 v11.0.0-beta.0 预发布版本，由 github-actions 于 11 月 3 日发布，带来 Astro 初始化支持、核心与侧边栏修复、UI 清理及多项交互改进。

- 🚀 发布 v11.0.0-beta.0 预发布版本，提交标识为 e4ec607
- 🧩 Astro：新增初始化支持、文档提及和生态 CI 沙盒（#37122，@Sidnioulz）
- 🛠️ Core：修复 camelCase 键的组合引用导致侧边栏崩溃（#36703）
- 🧹 Core：从发布包中移除未使用的文档图片（#37138）
- 🔁 Sidebar：避免焦点回调中的无限递归（#37073）
- 📂 Sidebar：支持从根上下文菜单展开/折叠全部并运行测试（#37038）
- 🧼 UI：移除 Storybook 11 中已弃用的组件（#36534）
- 🖱️ UI：在粘性分支行上显示上下文菜单按钮（#37042）
- 👥 贡献者包括 kasperpeulen、MichaelArestad 及另外 2 位贡献者

---

### [GitHub - tetherto/qvac: Open-source local AI SDK - run AI on-device with no cloud, no API keys. Supports GGUF, RAG, image, music, and video generation, speech-to-text, P2P inference, and more. Cross-platform: Linux, macOS, Windows, Android, iOS. · GitHub](https://github.com/tetherto/qvac)

**原文标题**: [GitHub - tetherto/qvac: Open-source local AI SDK - run AI on-device with no cloud, no API keys. Supports GGUF, RAG, image, music, and video generation, speech-to-text, P2P inference, and more. Cross-platform: Linux, macOS, Windows, Android, iOS. · GitHub](https://github.com/tetherto/qvac)

QVAC 是 Tether 推出的开源本地 AI SDK，让用户无需云服务或 API 密钥，即可在 Linux、macOS、Windows、Android 和 iOS 等平台上本地运行大语言模型、语音、视觉、图像/视频生成等多种 AI 任务，并提供 JavaScript/TypeScript 与 Python SDK 以及兼容 OpenAI 接口的本地 HTTP 服务器。

- 🏠 **本地优先**：AI 推理完全离线运行，针对普通消费级硬件优化，适用于消费应用、嵌入式系统及本地部署场景。
- 🔒 **隐私与控制**：数据保留在本地，无需云服务或第三方 API，用户完全掌控 AI 系统。
- 🧰 **一体化 SDK**：通过单一接口提供全面的 AI 能力，支持 JS/TS 与 Python，一份代码即可跨五大平台。
- 🌐 **点对点能力**：支持从对等节点直接下载模型（分布式模型注册表），并通过盲中继在 NAT/防火墙环境下保持网络连通。
- 💬 **丰富 AI 能力**：涵盖文本生成、文本嵌入、RAG、LoRA 微调、多模态推理、图像/视频/音乐生成、语音转文字、说话人分离、语音合成、翻译、OCR、图像分类，甚至脑机接口（BCI）与机器人视觉-语言-动作（VLA）。
- 🖥️ **OpenAI 兼容服务器**：通过 `qvac serve openai` 启动本地模型提供方，可接入 OpenCode、OpenClaw 等任意兼容工具。
- 🚀 **快速上手**：JS 使用 `npm i @qvac/sdk`，Python 使用 `pip install tetherto-qvac-sdk`，数步即可加载模型并流式输出推理结果。
- 📊 **社区活跃**：Apache-2.0 开源许可，获 750 星标、154 次复刻、3,551 次提交，社区通过 Discord 与 Keet 交流。
- ⭐ **生态资源**：提供完整文档、示例应用、本地模型提供方指南、博客教程及边缘设备优化研究论文。

---

### [Prepack，重获新生](https://jamesbox.exe.xyz/artifacts/prepack-revived/)

**原文标题**: [Prepack, revived](https://jamesbox.exe.xyz/artifacts/prepack-revived/)

文章回顾了 Facebook 的 JavaScript 部分求值器 Prepack 在 2018 年停摆后，于 2026 年借助 AI 代理、SMT 求解器 Z3 和差分模糊测试“复活”的过程：194 个难题语料通过率从 40/194 提升到 190/194，静默错误从 43 降到 0，并逐项处理了循环、递归、控制流汇合、路径条件、数值域、外部对象、环境建模和输出体积等八类难题，同时给出 React SSR 真实场景性能与剩余边界。

- 🧩 背景：Prepack 是 Facebook 的 JS 部分求值器，2018 年停更；原作者称循环、递归、环境建模等问题“不可判定”或“过于困难”。
- 🛠️ 方法：用 AI 代理、Z3 SMT 求解器和 fuzzer 重建；核心原则是“不能证明正确就停止并报诊断”，不输出可能错误的代码。
- 📊 总成绩：0.2.54 版仅 40/194 通过、43 个静默错误；复活版 190/194 通过、0 静默错误，回归测试 3,744/3,744，22 个真实库 × 6 配置无错误输出。
- 🔁 P1 循环：采用“残差循环 + 一次符号迭代效果检查”；局部效果已解决，涉及全局/外部状态仍诊断拒绝。
- ♻️ P2 递归：未知条件下停止展开并生成残差调用；无法证明安全时以 PP0050 拒绝。
- 🧠 P4 路径条件：Z3 负责蕴含/可行性判断和重写审计，修复 13 条不可靠规则，审计 34,047 次检查零失败。
- 🔢 P5 数值：区间域加最多 8 个值的分支拆分，支持短抽象数组 push、索引等；宽/无界范围仍需关系摘要。
- 📦 P6/P7：81 个内置函数效果摘要、外部不动点；开放世界全局、生成 DOM/Node/Intl 模型、`--assume` 运行守卫。
- 🧹 P8/P9：成本模型与窥孔优化抑制膨胀；支持 ES2022、私有字段、初始化内完成生成器/async，挂起生成器明确拒绝。
- ⚛️ React SSR：将 React 18 服务端渲染专门化到“已知应用 + 未知请求数据”；500/500 与 `renderToString` 字节一致，整页快 4–5.5×（`--jitless` 下 9–10×），且不加载 React。
- 📈 真实库：132 次编译 0 错误输出；18/22 至少一种配置成功；moment、handlebars 等初始化重负载显著加速，4 个因开放环境进入难汇总循环而干净停止。
- ⚠️ 限制：循环/递归一般不可判定，规范覆盖仍有缺口，@babel/standalone 编译 279 秒，UMD 可能使输出翻倍；两种 React 列表形状仍会构建后抛错，应改为拒绝。
- 🔗 资源：提供代码、194 例语料、设计笔记和 Northstar Supply 在线 demo；仓库暂私有。

---

### [Node.js — Node.js 27.0.0-alpha.0.0.0（Alpha）](https://nodejs.org/en/blog/release/v27.0.0-alpha.0.0.0)

**原文标题**: [Node.js — Node.js 27.0.0-alpha.0.0.0 (Alpha)](https://nodejs.org/en/blog/release/v27.0.0-alpha.0.0.0)

Node.js 27.0.0-alpha.0.0.0 已发布，这是一次 Alpha 预览版，包含 V8 15.6 引擎升级、大量 SEMVER-MAJOR 破坏性变更，以及加密、HTTP、文件系统、网络等核心模块的调整，主要面向提前适配与测试，不建议用于生产环境。

- 🚀 **版本信息**：2026-10-29 发布，版本号为 27.0.0-alpha.0.0.0，由 Rafael Gonzaga 发布。
- 🧠 **V8 升级至 15.6**：由 Node.js 26 的 14.6 升级到 15.6.75.13，默认启用 `Math.sumPrecise()`、`Iterator.join()`、`Iterator.zip()` 等新语言特性。
- 🧪 **实验性功能**：`import defer`、不可变 `ArrayBuffer`、RegExp 缓冲区边界等需通过命令行标志启用。
- 💾 **内存默认值变化**：未设置 `--max-old-space-size` 时，默认堆上限变为物理内存的一半，并限制在 256 MB 到 4 GB 之间；`Buffer` 和 `ArrayBuffer` 占用也计入堆限制。
- 🔄 **序列化格式变更**：`v8.serialize()`、`structuredClone()` 和 `postMessage()` 使用新格式，旧版 Node.js 无法读取。
- ⚠️ **可观察行为变化**：`Math` 方法结果可能在最后一位不同，`Math.random()` 序列变化，`error.stack` 不再沿原型链查找，堆快照更大且耗时约翻倍。
- 🔐 **加密与 OpenSSL 重大变更**：要求 OpenSSL 3 或更高版本，移除捆绑 FIPS 提供程序及旧版 OpenSSL 代码路径，多项加密 API 进入生命周期终止或运行时弃用。
- 🌐 **HTTP/网络调整**：HTTP 拒绝超过头部限制的响应，`keepAliveTimeout` 默认增至 65 秒，`req.headers` 改为空原型，新增实验性 `net/promises` API。
- 📁 **文件系统与模块**：原生实现 `fs.glob`，新增 `fs.mkstemp()`，`domain` 模块被运行时弃用并迁移至 `AsyncLocalStorage`，`vfs` 不再需要标志。
- 📦 **依赖与平台**：npm 升级至 12.1.0，Intel macOS 支持降级为实验性，Alpine 提升至 Tier 2。
- 🖥️ **下载与文档**：提供 Windows、macOS、Linux、AIX 等多平台安装包和源码，并附 SHA256 校验值与 PGP 签名。

---

### [Node.js — Node.js 版本发布](https://nodejs.org/en/about/previous-releases)

**原文标题**: [Node.js — Node.js Releases](https://nodejs.org/en/about/previous-releases)

该页面介绍 Node.js 的版本发布与支持周期、LTS/EOL 状态、版本时间表，以及下载页中“推荐”和“社区”安装方式的分类与准入标准。

- 🗓️ Node.js 主要版本进入 Current 状态六个月，便于库作者有时间增加支持。
- 🔄 历史上（截至 Node.js 26），奇数版本发布六个月后不再支持，偶数版本转为 Active LTS；从 Node.js 27 起改为每年发布，每个大版本在六个月 Current 后进入 LTS，并另有六个月 Alpha 阶段。
- 🛟 LTS 即长期支持，通常保证关键缺陷在总计 30 个月内得到修复；生产应用应只使用 Active LTS 或 Maintenance LTS。
- 📊 当前版本状态包括：v27 为 Alpha，v26、v24、v22 为 LTS；v25、v23、v21、v20、v18 等已 EOL，完整时间表可在 GitHub 查看。
- 💼 超过 Maintenance LTS 阶段的版本可通过 OpenJS Ecosystem Sustainability Program 合作伙伴获得商业支持。
- ⬇️ Downloads 页面提供 CLI、操作系统包管理器（如 brew）和 Node.js 版本管理器（如 nvm）等非交互式安装方式。
- ✅ 下载页将安装方式分为“Recommended”和“Community”，以兼顾灵活性、选择性与简洁的起步列表。
- 🧩 “Recommended”方法需与官方发布同步、使用未经修改的官方二进制（无预构建时才从源码构建）、支持多版本并存，并与 Node.js 项目保持紧密联系和直接沟通渠道。
- 🌐 “Community”方法需支持所有受支持且非 EOL 的 Node.js 版本，至少在一个官方支持的操作系统上运行且不局限于部分发行版或版本，并保持免费、开源、非商业产品或付费服务。
- 📝 任何人都可提议新的安装方式，但最终是否收录由 Node.js 项目决定。

---

### [HTML-in-Canvas in Chrome 157: Interactive DOM inside 2D, WebGL, and WebGPU  |  Blog  |  Chrome for Developers](https://developer.chrome.com/blog/html-in-canvas)

**原文标题**: [HTML-in-Canvas in Chrome 157: Interactive DOM inside 2D, WebGL, and WebGPU  |  Blog  |  Chrome for Developers](https://developer.chrome.com/blog/html-in-canvas)

Chrome 157 正式稳定发布 HTML-in-Canvas API，在 2D、WebGL 和 WebGPU 画布中渲染可交互、可访问的 DOM 内容，兼顾浏览器原生能力与 GPU 加速的像素级控制。

- 🚀 **正式发布**：继成功完成 Origin Trial 后，HTML-in-Canvas 在 Chrome 157 稳定版上线，打通 DOM 与 `<canvas>` 之间的能力鸿沟。
- ⚖️ **解决取舍难题**：传统 `<canvas>` 缺少文本选择、复制粘贴、右键菜单、屏幕阅读器、页内查找、自动翻译和自动填充；纯 HTML 又难以实现复杂高性能视觉效果。
- ✅ **核心优势**：画布内 HTML 支持文本排版、表单控件、选择复制、右键菜单、无障碍树、浏览器翻译/自动填充/页内查找、扩展、DevTools、爬虫与 AI 索引，以及导出图片或视频流。
- 🎯 **主要场景**：大型画布应用、3D 场景与游戏/WebXR、媒体编辑与导出、着色器驱动的表现型 UI。
- 🛠️ **快速上手**：为 `<canvas>` 设置 `content="drawable"`，子元素标记 `drawable`；2D 使用 `drawElementImage()`，3D 通过 `DOMMatrix` 和 `updateElementGeometry()` 同步几何。
- 🧩 **生态支持**：Three.js 提供 `THREE.HTMLTexture`，PlayCanvas 支持 `setSource()`，Babylon.js 提供 `BABYLON.HtmlTexture`，PixiJS v8.19.0 支持 `HTMLSource`，另有 CanvasUI；均为第三方社区项目。
- 🧪 **兼容与降级**：可用 `supportsHtmlInCanvas()` 检测支持情况；不支持时可回退到浮动 HTML 覆盖层或 `three-html-render`、`html2canvas`、`dom-to-image` 等方案。
- 📚 **后续资源**：可查阅完整文档、使用 Modern Web Guidance、在 WICG GitHub 仓库反馈，并查看社区演示。

---

### [发布 v1.9.0 · vercel/geist-font · GitHub](https://github.com/vercel/geist-font/releases/tag/v1.9.0)

**原文标题**: [Release v1.9.0 · vercel/geist-font · GitHub](https://github.com/vercel/geist-font/releases/tag/v1.9.0)

Geist Font 发布 v1.9.0，新增 Geist Serif 字体家族；该字体提供四种点形变体，既可分别导入，也可通过可变字体轴切换。
- 🚀 v1.9.0 于 10 月 30 日发布，自上次发布以来包含 6 个提交。
- ✒️ Geist Serif 是高对比度展示衬线字体，具有细密锯齿状衬线和锐利细线。
- 🔤 Regular 与 Square 适合主排版，Triangle 与 Heart 更具装饰性。
- 📦 四种变体可分别导入：GeistSerifRegular、GeistSerifSquare、GeistSerifTriangle、GeistSerifHeart，对应 CSS 变量 `--font-geist-serif-regular/square/triangle/heart`。
- 🎛️ 也可从 `geist/font/serif/variable` 导入 GeistSerif 可变字体，通过 ELSH 轴选择形状：0 Regular、25 Square、50 Triangle、100 Heart。
- ❤️ 该发布获得 19 人互动，包括 🎉13、❤️8、🚀5 反应。

---

