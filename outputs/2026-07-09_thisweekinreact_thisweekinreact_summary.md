### [如何使用 OpenTelemetry 导出 Next.js 追踪 | Sentry 博客](https://blog.sentry.io/nextjs-export-traces-opentelemetry/?utm_source=thisweekinreact&utm_medium=paid-community&utm_campaign=nextjs-fy27q2-evergreen&utm_content=newsletter-first-sponsor-traces-otel-blog-learnmore)

**原文标题**: [How to Export Next.js Traces with OpenTelemetry | Sentry Blog](https://blog.sentry.io/nextjs-export-traces-opentelemetry/?utm_source=thisweekinreact&utm_medium=paid-community&utm_campaign=nextjs-fy27q2-evergreen&utm_content=newsletter-first-sponsor-traces-otel-blog-learnmore)

### 概述总结
Next.js 内置了对请求追踪的支持，但需要配置 OpenTelemetry 导出器才能查看追踪数据。通过 @vercel/otel 库，可以轻松将追踪数据导出到任何兼容 OpenTelemetry 的后端（如 Sentry）。本文详细介绍了如何配置、添加自定义跨度，并比较了直接使用 OTLP 与 Sentry SDK 的优劣。

- 🧩 **追踪的价值**：追踪能精确定位请求中的慢速环节（如中间件、API 路由、数据库查询等），避免凭猜测排查问题。
- ⚙️ **配置方法**：使用 `@vercel/otel` 库，在 `instrumentation.ts` 中调用 `registerOTel()`，并设置 `OTEL_EXPORTER_OTLP_*` 环境变量即可导出追踪数据。
- ✏️ **自定义跨度**：在关键业务操作（如生成发票、调用 AI 模型）中添加自定义跨度，使用点号命名（如 `invoice.generate-pdf`）并添加相关属性（如行数、模板），但注意 Edge 运行时不支持自定义跨度。
- 🚀 **导出到 OTLP 后端**：通过设置 `OTEL_EXPORTER_OTLP_TRACES_ENDPOINT` 和 `OTEL_EXPORTER_OTLP_TRACES_HEADERS` 环境变量，可将追踪数据直接发送到 Sentry 的 OTLP 端点。
- 🔍 **OTLP vs Sentry SDK**：OTLP 适合已有 OpenTelemetry 管道的团队，但功能有限（无浏览器追踪、错误监控等）；Sentry SDK 功能更全面（支持浏览器、错误监控、Session Replay 等），推荐首次配置时使用。
- 🛠️ **后续行动**：利用追踪数据创建监控器、告警和仪表盘，将追踪融入日常运维流程，并尝试使用 Seer Agent 自动分析慢请求原因。
- ❓ **常见问题**：无需 OpenTelemetry Collector 即可发送追踪；@vercel/otel 不支持浏览器追踪；不要同时使用 @vercel/otel 和 Sentry SDK；可通过环境变量控制跨度细节。

---

### [Formity：React 多步骤表单库](https://formity.app/)

**原文标题**: [Formity: React Multi-Step Form Library](https://formity.app/)

概述总结  
React 开发者可以轻松使用这个库创建动态多步骤表单，它完全类型安全，支持高级逻辑，并能与现有表单库配合使用。

- 🚀 **快速上手**：提供简单的入门指南和示例代码  
- 🔒 **类型安全**：完全支持 TypeScript，确保代码健壮性  
- 🧩 **动态步骤**：支持灵活的多步骤表单流程设计  
- 🔗 **兼容性强**：可与主流表单库（如 React Hook Form）无缝集成  
- 🎯 **高级逻辑**：内置条件分支、数据验证等复杂功能

---

### [RFC：路由处理器中的 WebSocket 升级 · vercel/next.js · 讨论 #95514 · GitHub](https://github.com/vercel/next.js/discussions/95514)

**原文标题**: [RFC: WebSocket Upgrades in Route Handlers · vercel/next.js · Discussion #95514 · GitHub](https://github.com/vercel/next.js/discussions/95514)

该 RFC 提议在 Next.js App Router 的路由处理器中，为 WebSocket 升级提供原生支持。

- 📜 **核心 API：`NextResponse.upgrade()`** 在 `route.ts` 文件中使用，可接受 WebSocket 连接，并支持在握手前进行身份验证、设置响应头和 Cookie。
- 🔒 **条件接受与安全** 路由处理器可检查请求（如来源、认证），若拒绝则返回普通 HTTP 响应（如 401），确保安全。
- 🔗 **生命周期钩子** 通过 `open`、`message`、`close`、`error` 四个钩子管理连接，并使用 CrossWS 提供的 `Peer` 和 `Message` 高级 API。
- 🚀 **部署兼容性** 支持 `next dev`、`next start`、独立输出及适配器，但 Edge 运行时、静态导出及不支持原始升级原语的适配器不可用。
- 🧩 **路由与集成** 保留现有路由（如重写、`proxy.ts`），且 WebSocket 路径不会干扰内部 HMR 路径。
- ⚙️ **实验性功能** 通过 `experimental.webSocketRouteHandlers` 标志启用，未来可能稳定化。

---

### [WebSocket 支持现已进入公开测试阶段 - Vercel](https://vercel.com/changelog/websocket-support-is-now-in-public-beta)

**原文标题**: [WebSocket support is now in Public Beta - Vercel](https://vercel.com/changelog/websocket-support-is-now-in-public-beta)

Vercel Functions 现支持 WebSocket 连接，实现客户端与服务器端代码的双向通信。

- 🌐 WebSocket 支持实时功能，如交互式 AI 流、聊天和协作应用
- ⚡ WebSocket 连接运行在 Fluid compute 上，遵循与其他函数调用相同的限制和定价
- 💰 采用活跃 CPU 计费模式，仅对处理消息的时间收费，空闲连接不产生费用
- 📦 可使用标准 Node.js 库（如 Express 和 ws）直接提供 WebSocket 连接，无需额外配置
- 🔗 支持更高级的库，如 Socket.IO
- 📚 提供文档帮助快速上手

---

### [逆向工程 ChatGPT 网页版：OpenAI 如何为十亿用户构建](https://performance.dev/chatgpt)

**原文标题**: [Reverse Engineering ChatGPT Web:
How OpenAI Built for a Billion Users](https://performance.dev/chatgpt)

本篇文章深入分析了 ChatGPT 网页应用的技术架构与设计哲学，揭示了 OpenAI 如何为全球十亿用户构建一个高效、可访问的 AI 交互界面。

- 🧠 **核心设计原则**：以“让全球用户都能快速开始使用 AI”为目标，优先考虑首次加载速度和低门槛体验，所有技术决策围绕这一目标展开。
- 🔧 **技术栈迁移**：从 Next.js Pages Router 迁移至 Remix，最终采用 React Router 7 框架模式，实现服务端渲染（SSR）以优化首次加载性能。
- ⚡ **极致性能优化**：通过服务端渲染、流式传输、内联关键脚本、预加载策略和性能监控（如 TTI），确保用户从打开页面到可输入的时间极短。
- 🎨 **CSS 与 UI 设计**：使用 Tailwind CSS 和语义化 CSS 变量实现主题切换，采用系统字体栈避免额外字体加载，组件库选用 Radix UI 等成熟方案。
- 🖥️ **复杂渲染处理**：对 AI 生成的流式内容（如 Markdown、代码块、数学公式）进行实时解析与渲染，使用 ProseMirror 和 CodeMirror 等专业编辑器。
- 🔒 **安全与防滥用**：通过 Cloudflare 挑战、自研 Sentinel 反滥用系统、匿名用户 ID 和预检查机制，在无登录状态下防御机器人攻击。
- 🚩 **功能标志与实验**：使用 Statsig 进行服务端评估的功能标志（556 个），支持 A/B 测试和渐进式发布，所有决策基于数据驱动。
- 🌍 **开放与对比**：ChatGPT 选择“无登录即可使用”的开放策略，与 Claude 的登录墙形成对比，体现了不同的用户定位和工程权衡。

---

### [我让 React 编译器处理记忆化：实际出问题的地方 - LogRocket 博客](https://blog.logrocket.com/react-compiler-memoization-what-actually-broke/)

**原文标题**: [I let React Compiler handle memoization: Here's what actually broke - LogRocket Blog](https://blog.logrocket.com/react-compiler-memoization-what-actually-broke/)

React Compiler 1.0 承诺自动处理 memoization，但在生产环境中启用后，大部分功能正常，但“大部分”是关键，那些微妙的错误如果没有测试就会发布。文章记录了在 Next.js 项目中的迁移过程、遇到的坑和解决方案。

- 🧠 **编译器原理**：作为 Babel 插件，自动分析数据流并生成更细粒度的 memoization 代码，但要求代码严格遵循 React 规则，否则会暴露隐藏的 bug 或静默跳过优化。
- ⚠️ **React Hook Form 兼容性问题**：`watch()` 函数因“内部可变性”导致实时预览冻结，需使用 `"use no memo"` 指令创建包装钩子来绕过编译器优化。
- ⏳ **Chart.js 回调稳定性问题**：删除 `useCallback` 后，点击处理程序出现陈旧数据，原因是回调身份不稳定导致 `useEffect` 重新注册时序错乱，最终需保留 `useCallback` 并添加注释说明。
- 🔍 **DevTools 徽章误导**：Memo ✨ 徽章仅表示编译器处理了组件，不代表优化成功或组件无问题。例如，直接修改 prop 的组件仍会显示徽章，但 linter 会报错。
- ✅ **迁移清单**：先升级 lint 规则并修复问题；在功能分支上启用编译器；不要依赖徽章作为正确性信号；审计具有内部可变性的库；运行端到端测试；定期审查 `"use no memo"` 指令。
- 💡 **保留 useMemo/useCallback 的场景**：第三方库依赖函数身份（如图表库）、直接操作 DOM API 或外部 SDK、或经过性能分析确认的昂贵计算。其他情况应删除，让编译器处理。
- 🧩 **心态转变**：从“在哪里 memoize”转变为“这段代码是否跨越了编译器看不到的边界”，保留的每个钩子都应有明确的文档说明理由。

---

### [补水不匹配的隐性成本 · PerfPerfPerf](https://3perf.com/blog/hydration-mismatch/)

**原文标题**: [Hidden Cost of Hydration Mismatches · PerfPerfPerf](https://3perf.com/blog/hydration-mismatch/)

### 概述  
本文解释了 React 应用中水合不匹配如何导致 LCP（最大内容绘制）性能严重下降，并提供了解决方案。

- 💧 **水合不匹配的定义**：当客户端渲染的 DOM 与服务端不同时，React 会重新创建整个 DOM，而非简单修补。
- 🔄 **事实 1：强制重建 DOM**：水合不匹配迫使 React 从最近的 Suspense 边界开始重建 DOM，若无边界则整个页面重建。
- 📏 **事实 2：字体加载导致文本尺寸变化**：使用`font-display: swap`的 Web 字体时，加载后文本尺寸改变，可能引发布局偏移。
- 🖼️ **事实 3：LCP 仅测量新 DOM 节点**：LCP 只记录新添加元素的尺寸，忽略现有元素的尺寸变化。
- 💥 **组合效应**：水合不匹配 + 字体加载后文本变大→React 重建 DOM→浏览器误认为新节点更大→LCP 时间延迟至水合完成（5 秒+），导致 LCP 从绿色变为红色。
- 🛠️ **解决方案**：避免水合不匹配；若无法避免，用`<Suspense>`包裹不匹配元素，限制 DOM 重建范围。

---

### [Cloudflare Workers 与 Hyperdrive 结合 TanStack Start – Master.dev 博客](https://master.dev/blog/cloudflare-workers-and-hyperdrive-with-tanstack-start/)

**原文标题**: [Cloudflare Workers and Hyperdrive with TanStack Start – Master.dev Blog](https://master.dev/blog/cloudflare-workers-and-hyperdrive-with-tanstack-start/)

本文介绍了如何在 Cloudflare Workers 中使用 Hyperdrive 和 TanStack Start 高效连接数据库，并解决了常见性能与资源清理问题。

- 🚀 **性能优化**：通过 Hyperdrive 连接池预建数据库连接，避免每次 Worker 启动时新建连接，减少延迟。
- 🔗 **连接管理**：使用 Hyperdrive 作为代理，限制数据库连接数，防止因 Worker 数量增长导致连接超限。
- 🧹 **请求级清理**：利用 TanStack Start 的全局请求中间件，每次请求创建新的数据库对象，避免长期占用 I/O 资源。
- ⚙️ **配置要点**：在 Wrangler 文件中添加 Hyperdrive 绑定，并设置 `placement` 区域与数据库同地，降低查询延迟（如从 80ms 降至 7ms）。
- 📦 **开发环境**：在 `.env` 文件中设置 `CLOUDFLARE_HYPERDRIVE_LOCAL_CONNECTION_STRING_HYPERDRIVE`，解决本地开发连接错误。
- 🛠️ **工具集成**：使用 Drizzle ORM 和 pg 库，通过 `drizzle.config.ts` 自动生成模式，简化数据库操作。

---

### [24 个 S 级演示技巧 - 作者：Jina Yoon](https://newsletter.posthog.com/p/how-to-demo?r=5t1b8o)

**原文标题**: [24 tips for giving S-tier demos - by Jina Yoon](https://newsletter.posthog.com/p/how-to-demo?r=5t1b8o)

以下是对文章《24 tips for giving S-tier demos》的总结：

一次出色的演示能决定项目成败或创业公司能否获得融资，但多数开发者不擅长此道。以下是 S 级演示的 24 个实用技巧，分为基本结构、叙事策略、准备与呈现、趣味性四部分。

- 📌 **聚焦一个核心信息**：选择观众最需要记住的一个要点（通常是问题及解决方案），让所有内容围绕它展开。
- ⏱️ **快速切入主题**：尽快展示核心内容，背景介绍不超过 1-2 句话，避免冗长铺垫。
- 🎯 **像推销而非产品演示**：目标是激发观众兴趣，而非单纯展示功能。
- 📞 **结尾要有行动号召**：如提供二维码、邀请贡献者或提问，让观众能立即参与。
- 🚀 **演示前先上线**：展示真实用户数据或已部署的项目，能极大增强说服力。
- 🤝 **以共同痛点开场**：用观众都经历过的难题引发共鸣，例如设计师找不到素材的困扰。
- 🧩 **借用熟悉概念解释新事物**：如将 AI 协作工具命名为“PostHog Work”，让观众快速理解。
- 🎮 **创建独立演示应用**：展示开发工具时，用单独的示例应用（如 OnlyHogs）让效果更直观。
- 👤 **使用“你”的视角**：让观众代入场景，例如“想象你正在处理六个紧急事件”。
- ⚖️ **对比现有方案**：并排展示旧流程的繁琐与新方案的简洁，突显改进价值。
- 🔮 **先展示效果，后解释原理**：像魔术师一样保留技术细节，结尾再提供链接作为行动号召。
- ⚡ **充满能量**：像 Steve Ballmer 一样用热情感染观众，活力能提升演示效果。
- 🚫 **不要道歉**：避免说“还有点粗糙”，直接开始，否则会降低观众期待。
- 🏁 **明确结束信号**：用总结句、降调或庆祝画面，避免尴尬的停顿。
- ✅ **做好技术准备**：使用演示项目、关闭通知、测试投影仪，并准备离线备份。
- 📊 **使用真实数据**：避免虚假占位符，真实数据让演示更可信。
- ⏳ **预加载内容**：提前缓存或准备，消除等待时间，像电视厨师一样高效利用时间。
- 🗣️ **至少大声排练一次**：增强自信，让表达更自然流畅。
- 🎭 **不要追求完美**：即使项目未完成也要演示，因为演示本身就是展示进展。
- 🖼️ **避免纯代码展示**：即使无 UI，也要用架构图等视觉元素辅助理解。
- 🎬 **用动态演示代替静态幻灯片**：主动展示比空谈想法更有说服力。
- 🎥 **使用专业录屏工具**：如 Screen Studio，支持缩放和动画，让操作更清晰。
- 🎨 **视觉不追求精美**：只需突出关键信息，简单标注也能有效传达。
- 🔊 **善用音频**：如海员号子或纯音频演示，能增加趣味性和记忆点。
- 🍹 **加入创意元素**：如背景中喝 Piña Colada 的片段，让演示更独特难忘。

---

### [发布 vinext@1.0.0-beta.0 · cloudflare/vinext · GitHub](https://github.com/cloudflare/vinext/releases/tag/vinext%401.0.0-beta.0)

**原文标题**: [Release vinext@1.0.0-beta.0 · cloudflare/vinext · GitHub](https://github.com/cloudflare/vinext/releases/tag/vinext%401.0.0-beta.0)

以下是对您提供内容的总结：

vinext@1.0.0-beta.0 版本发布，包含多项新功能、错误修复和性能改进。

- 🚀 **新功能**：新增 CDN 预热标记、Cloudflare 预渲染路径预热、KV 缓存填充、create-vinext-app 工具、Vite 8 依赖要求，以及默认使用 Workers Cache。
- 🐛 **错误修复**：修复了 Wrangler 配置部署脚本、App Router 响应头变化、客户端状态重验证、HTML 字符集、全局 polyfill、trailingSlash 图像端点、缓存组件支持及 tsconfig 路径匹配等问题。
- ⚡ **性能优化**：过滤虚拟模块钩子以提升构建性能。
- 👥 **贡献者**：感谢 @camc314、@james-elicx 和 @southpolesteve 的贡献。
- 🔐 **安全验证**：提交使用 GitHub 验证签名，GPG 密钥 ID 为 B5690EEEBB952194。

---

### [2026 年 7 月 - Base UI 成为默认 - shadcn/ui](https://ui.shadcn.com/docs/changelog/2026-07-base-ui-default)

**原文标题**: [July 2026 - Base UI as the Default - shadcn/ui](https://ui.shadcn.com/docs/changelog/2026-07-base-ui-default)

以下是您提供的文本内容的摘要：

shadcn/ui 现已将 Base UI 设为默认组件库，但 Radix 仍受支持且不会被弃用。新项目初始化时默认使用 Base UI，并提供了从 Radix 迁移到 Base UI 的智能工具（技能）。

- 🎉 **Base UI 成为默认**：新项目运行 `npx shadcn init` 时，Base UI 是默认选择，Radix 仍可通过 `-b radix` 参数指定。
- 🔄 **Radix 未被弃用**：所有更新和新组件仍会同时支持 Radix 和 Base UI，现有项目无需迁移。
- 🛠️ **智能迁移工具**：提供了一个“技能”（skill），允许用户逐步将单个组件从 Radix 迁移到 Base UI，同时保持项目可运行。
- 📄 **迁移结果透明**：每次迁移会生成工作代码、每个组件的详细报告（位于 `.migration/` 目录），以及清晰的 Git 历史记录（每个组件一个提交）。
- 🧠 **为何用技能而非代码转换**：因为用户自定义了代码，技能让 AI 代理理解并保留这些自定义修改，而非机械替换。
- 🚀 **推荐使用 Base UI**：Base UI 已稳定（1.6.0 版本，周下载量超 600 万），社区选择比例已达 2:1，官方推荐新项目使用。

---

### [发布 takumi@2.0.0 · kane50613/takumi · GitHub](https://github.com/kane50613/takumi/releases/tag/takumi%402.0.0)

**原文标题**: [Release takumi@2.0.0 · kane50613/takumi · GitHub](https://github.com/kane50613/takumi/releases/tag/takumi%402.0.0)

该版本对 Takumi 渲染引擎进行了大量优化、修复和功能增强，主要聚焦于性能、稳定性、字体处理和 API 改进。

- 🚀 **性能与内存优化**：流式编码动画帧，避免内存爆炸；复用场景状态，减少重复快照；优化缓冲池，防止越界分配；裁剪发布二进制体积。
- 🐛 **关键 Bug 修复**：修复 `renderAnimation` 中结构化关键帧未生效的问题；修复子集字体选择非确定性（并发注册导致渲染结果不一致）；修复渐变停止点过多时的 panic；修复阴影/模糊缓冲区溢出与 panic。
- 🔤 **字体与排版改进**：嵌入字体改为真正的最后备选，不抢占 `sans-serif`；新增 `FontResource::last_resort` 标记；`fonts` 选项支持直接传入 URL 字符串；`googleFonts` 缓存 Promise 而非结果，并支持自定义 `baseUrl`；修复 `fontFamilies` 顺序被忽略的问题；`googleFonts` 返回结果按请求家族顺序排序。
- 🛠️ **API 变更与重构**：移除 `encodeFrames`，统一使用 `renderAnimation`；`fetchResources`/`extractResourceUrls` 替换为 `prepareImages`；`render` 选项的 `format`/`quality`/`lossless` 联合类型修复；新增 `@takumi-rs/helpers/renderer` 共享入口；新增 `takumi-html` crate 支持 HTML + Tailwind 解析。
- 🎨 **样式与渲染修复**：`background` 简写不再重置 `background-blend-mode`；`:lang()` 伪类现在实际生效；`max-width`/`max-height` 初始值改为 `none`；`gap` 初始值改为 `normal`；无文本元素保持为容器，背景等样式正常绘制。
- 🔒 **安全与边界处理**：远程获取添加字节上限（默认 32 MiB，CSS 2 MiB）和默认 5 秒超时；图片解码限制 8192x8192，GIF 限制总帧像素预算；`allowUrl` 钩子可拒绝特定 URL。
- 📦 **依赖与构建改进**：`@takumi-rs/*` 依赖锁定到匹配版本；`./wasm` 导出移除；`svg` 特性重命名为 `svg-source`；`KeyframesMap` 类型改用 `csstype`，无需 DOM lib。

---

### [纸张着色器——超快速零依赖着色器](https://shaders.paper.design/)

**原文标题**: [Paper Shaders – Ultra-fast zero-dependency shaders](https://shaders.paper.design/)

本文介绍了多种图像滤镜、Logo 动画及视觉效果类型，涵盖纹理、渐变、噪点、动态图形等创意工具。

- 📄 图像滤镜：包括纸质纹理、磨砂玻璃、水纹、图像抖动、半调点及 CMYK 半调效果
- 🎬 Logo 动画：支持热力图、液态金属、宝石烟雾等动态效果
- ✨ 视觉效果：涵盖网格渐变、静态径向渐变、抖动、颗粒渐变、点轨道、点阵、扭曲、螺旋、漩涡、波浪
- 🌌 噪点与纹理：神经噪点、柏林噪声、单纯形噪声、沃罗诺伊图
- 🔥 动态特效：脉冲边框、元球、色彩面板、烟圈、上帝光

---

### [GitHub - unlayer/elements: 一次编写，React 组件。从同一组件树渲染电子邮件、网页和 PDF。](https://github.com/unlayer/elements)

**原文标题**: [GitHub - unlayer/elements: Write once in React. Render emails, web pages, and PDFs from the same component tree. · GitHub](https://github.com/unlayer/elements)

Unlayer Elements 是一个开源 React 组件库，允许开发者使用同一套组件树生成电子邮件、网页和 PDF 文档，支持三种输出模式，由 Unlayer 团队维护。

- 📧 **三合一渲染** — 同一组件树可同时输出电子邮件（兼容 Outlook、Gmail 等）、响应式网页和打印用 PDF
- ⚡ **快速上手** — 通过 `npm install @unlayer/react-elements` 安装，使用熟悉的 JSX 语法即可构建
- 🧩 **核心组件** — 提供 Email、Page、Document 根组件，以及 Row、Column、Button、Heading 等丰富组件
- 🎨 **列布局灵活** — 支持单列、双列、三列、四列及自定义比例布局，满足各种排版需求
- 🏭 **生产级输出** — 生成无 React 痕迹的干净 HTML，支持 `renderToHtml()` 和 `renderToHtmlParts()` 方法
- 🔄 **可视化编辑器兼容** — 通过 `renderToJson()` 导出设计 JSON，实现代码与可视化编辑的来回切换
- 🛡️ **TypeScript 优先** — 完整的类型定义和自动补全，提升开发安全性和 IDE 支持
- 📦 **轻量高效** — 约 12KB gzipped，可 tree-shaking，零客户端 JavaScript 依赖
- 💼 **实际应用场景** — 适用于交易邮件、PDF 生成、CMS 驱动内容和邮件网页同步发布

---

### [发布 · react-hook-form/react-hook-form · GitHub](https://github.com/react-hook-form/react-hook-form/releases#release-v7.81.0)

**原文标题**: [Releases · react-hook-form/react-hook-form · GitHub](https://github.com/react-hook-form/react-hook-form/releases#release-v7.81.0)

react-hook-form 发布了多个版本更新，包含新功能、错误修复和性能优化。

- ⚜️ **v7.81.0**: 新增 FieldArray 组件，修复 useFieldArray 验证错误位置、reset 触发订阅、useController 字段清除等问题，并改进 setValue 和 re-render 性能。
- 🧄 **v7.80.0**: 新增 useFieldArray 禁用功能，提升整体性能，修复深比较中空数组与空对象不等问题。
- 🚷 **v7.79.0**: 新增 useFieldArray disabled 属性，修复 Controller onChange Promise、深比较共享对象引用、原生验证行为等多项问题。
- 🦷 **v7.78.0**: 更新 dirtyFields 类型，修复 Controller 重置后字段恢复、useFormState isDirty 竞争条件、reactive values 属性等。
- 🥡 **v7.77.0**: 新增 resetDefaultValues API，加强原型路径遍历防护，修复 FieldArray 错误覆盖、reset 不一致行为、shouldUnregister 值保留等问题。
- 🐞 **v7.76.1**: 修复 setValues 验证参数传递、表单变更发射、跳过冗余深克隆等性能优化，并回滚 NaN 处理。
- 🦾 **v8.0.0-beta.2**: 同步 v8 beta 与最新 master，集成 v7 错误修复、性能改进和 DX 更新。
- 🪭 **v7.76.0**: 改进 isDirty 同步、修复 isValidating 响应性、表单级验证错误、append null 值替换、原生验证提示、Controller 字段更新等多项问题。
- 🦧 **v7.75.0**: 改进脏字段修剪空节点、支持 TypeScript 6.0、修复 FormProvider 上下文、重新注册字段 isDirty 计算、watch 更新保留等。
- 🪇 **v7.74.0**: 新增 setValues 函数，修复 useController 名称变化字段值、嵌套字段注销、NaN 视为空值等。

---

### [发布 v1.9.0 · visgl/react-google-maps · GitHub](https://github.com/visgl/react-google-maps/releases/tag/v1.9.0)

**原文标题**: [Release v1.9.0 · visgl/react-google-maps · GitHub](https://github.com/visgl/react-google-maps/releases/tag/v1.9.0)

概述摘要  
visgl/react-google-maps 发布了 v1.9.0 版本，包含新功能、错误修复和依赖更新。

- 🆕 新增高级标记的基本键盘事件支持  
- 🗺️ 添加了 3D 地图与自定义路线元素的示例（v=alpha）  
- 🧩 map-control 组件新增 className 属性  
- 🔧 修复了构建时不将示例包含在库构建中的问题  
- 🔄 改进了外部加载 importLibrary 的处理方式  
- 🛡️ 为 useInsertionEffect 添加 SafeReact 和回退方案，确保兼容 React 16/17  
- 🚫 修复了重新挂载时因缓存地图实例损坏而崩溃的问题  
- ⏳ 防止 API 提供程序竞态条件，延迟加载状态更新  
- 📦 更新了依赖项和 importLibrary 类型定义  
- 🖱️ 修正了指针事件的行为

---

### [发布 react-doctor@0.7.0 · millionco/react-doctor · GitHub](https://github.com/millionco/react-doctor/releases/tag/react-doctor%400.7.0)

**原文标题**: [Release react-doctor@0.7.0 · millionco/react-doctor · GitHub](https://github.com/millionco/react-doctor/releases/tag/react-doctor%400.7.0)

以下是您提供的文本摘要：

react-doctor 0.7.0 版本发布，重点优化了缓存机制，大幅提升了大型仓库的重新扫描速度，并增强了缓存的有效性和可靠性。

- 🚀 **缓存全面优化**：缓存系统现在能跨越 CI 的干净检出工作，GitHub Action 的缓存目录能预热所有层，而不仅仅是内容寻址层。整个仓库的扫描结果缓存也移至共享的项目缓存根目录下。
- 🔑 **缓存键值强化**：死代码结果缓存键值现在包含`@react-doctor/core`自身版本和从`deslop-js/analyzed-inputs`导入的指纹列表，防止因工具升级或配置变更导致的静默缓存失效。
- ⚡ **增量死代码分析**：死代码分析现在支持跨扫描的增量执行。通过按文件解析摘要、文件列表、模块解析图和包引用事实等独立分层的缓存，仅重新解析发生变化的文件，大型仓库（如 sentry，9k 文件）的重新扫描时间从约 8.0 秒降至约 3.2 秒。
- 🛠️ **支持脏工作区缓存**：即使存在未提交的更改，整个仓库的扫描结果缓存也能命中。缓存键值基于确切的脏状态（修改、暂存、重命名、删除和未跟踪文件及其内容哈希），确保编辑操作仍能使缓存失效。
- 🐛 **修复大仓库缓存问题**：提高了`runGit`的输出上限至 64 MiB，解决了在约 15-25k 个跟踪文件的大型仓库中，因默认`maxBuffer`限制（1 MiB）导致缓存静默失效的问题，恢复了即时重运行功能。
- 🔍 **跨文件检查缓存**：热重扫描现在会跳过依赖项未发生变化的文件的跨文件 lint sidecar。每个文件携带一个依赖指纹，只有当依赖项集合发生变化时才会重新进行 lint 检查。
- 📊 **新增缓存温度遥测**：在每次扫描的 Sentry 事件中添加了缓存温度遥测，通过`cache.temperature`（turbo/warm/cold/disabled）和`cache.warmth`（0-1 数值）指标，直观地展示缓存效率。

---

### [TMiR 2026-06：React 编译器正在生锈，AI 对工程文化意味着什么](https://www.reactiflux.com/transcripts/tmir-2026-06)

**原文标题**: [TMiR 2026-06: React Compiler is getting rusty, what does AI mean for engineering culture](https://www.reactiflux.com/transcripts/tmir-2026-06)

React 2026 年 6 月月度总结：React 编译器改用 Rust，AI 对工程文化的影响，以及多项工具更新。

- 🦀 React 编译器已移植到 Rust 并合并，多个构建工具（Oxlint、SWC、RSPack、Next、Bun）正在集成，但 Rolldown 因二进制体积增加而回退。
- 🏗️ React Router v8 发布，采用特性标志实现无痛升级，要求 React 19.2+ 且仅支持 ESM。
- 📦 Babel 8 和 TypeScript 7.0 RC 发布，均转向 ESM-only 并默认现代目标，TS 7.0 暂缺程序化 API。
- 🌟 Astro 7 发布，改进构建速度、支持高级路由和 AI 代理检测，可输出结构化 JSON。
- 🔧 Nub JS（Zod 作者）发布，基于 Node 但内置 TypeScript 剥离、改进的包管理，号称跨兼容现有锁文件。
- ⚡ Legend List 3.0 支持 DOM，TSRX 重新设计语法以更接近 JSX。
- 🧩 React 核心动态：Fragment Refs 进入 Canary，React DevTools 新增 MCP 工具供 AI 代理查询组件树和性能分析。
- 🏛️ React 基金会网站上线，旨在资助维护者和社区活动，但核心开发似乎碎片化。
- 📉 Meta 工程文化恶化：强制调岗、追踪击键、Llama 4 落后，工程师被迫从事数据标注。
- 🤖 AI 要求更高工程纪律：代码变得可丢弃，但需要更好的文档、测试和架构设计；Christoph Nakazawa 分享现代工程价值观，强调所有权和快速反馈。
- 🔒 安全更新：GitHub Actions 支持锁定 SHA，npm 12 默认禁用安装脚本和 Git 依赖。
- 🚀 Cloudflare 收购 VoidZero（VitePlus 团队），不影响开源 Vite。
- 📊 代码优化仍重要：TanStack Table 内存减少 90%，Pierre Diffs 优化虚拟化，CompileCat 和 RSPack 团队开发新优化编译器。
- 💡 Mark Erikson 发布 React-Redux 性能优化 PR（提速 20-30%），并更新基准测试仓库。
- 📝 Aurora Scharff 分享 RSC 组件架构偏好，Lovable 项目默认使用 TanStack Start。

---

### [大规模下的 URL 状态管理：与 François Best 探讨 | nuqs、React、TypeScript - YouTube](https://www.youtube.com/watch?v=b3AYuuRdyf4)

**原文标题**: [URL State at Scale with François Best | nuqs, React, Typescript - YouTube](https://www.youtube.com/watch?v=b3AYuuRdyf4)

YouTube 平台相關資訊總覽
- 📰 提供新聞中心，發布官方消息與更新
- ©️ 明確版權規範，保護創作者與內容權益
- 📞 設有聯絡我們管道，供用戶諮詢與反饋
- 🎥 為創作者提供專屬支援與資源
- 📢 開放刊登廣告功能，協助品牌推廣
- 👨‍💻 提供開發人員工具與 API 整合服務
- 📜 訂有使用條款，規範平台行為
- 🔒 重視私隱保護，確保用戶資料安全
- 🛡️ 制定政策及安全措施，維護社群環境
- ⚙️ 說明 YouTube 的運作方式，提升透明度
- 🧪 測試新功能以優化用戶體驗
- 🏢 版權歸屬 Google LLC（© 2026）

---

### [Meticulous AI - 无需编写测试的自动化前端测试](https://www.meticulous.ai/?utm_source=thisweekinreact&utm_medium=newsletter&utm_campaign=26q3&utm_content=2nd)

**原文标题**: [Meticulous AI - Automated Frontend Testing Without Writing Tests](https://www.meticulous.ai/?utm_source=thisweekinreact&utm_medium=newsletter&utm_campaign=26q3&utm_content=2nd)

该平台提供自动化、全面且确定性的测试解决方案，让开发者无需手动编写或维护测试用例，即可在代码合并前发现所有潜在问题。

- 🚀 零开发工作量：通过记录日常开发交互，AI 自动生成覆盖所有代码分支和用户流程的测试套件
- ⚡ 极速迭代：测试随应用自动演进，新增或废弃用例无需人工干预，大幅提升代码发布速度
- 🛡️ 彻底消除误报：基于 Chromium 确定性调度引擎，从底层消除测试不稳定因素，支持复杂应用
- 🔍 即时反馈：提交 PR 即可查看对用户工作流的影响，通过模拟后端响应实现无副作用测试
- ⏱️ 闪电速度：测试在计算集群中高度并行化，1000+ 屏幕测试可在 120 秒内完成
- 🔧 灵活集成：支持 NextJS/React/Vue/Angular 等主流框架，可补充或替代现有测试套件
- 🏢 企业级信任：获 Dropbox、Notion 等 100+ 组织采用，工程师评价"无法想象没有它的工作"

---

### [Meticulous AI - 无需编写测试的自动化前端测试](https://www.meticulous.ai/?utm_source=thisweekinreact&utm_medium=newsletter&utm_campaign=26q2&utm_content=1st)

**原文标题**: [Meticulous AI - Automated Frontend Testing Without Writing Tests](https://www.meticulous.ai/?utm_source=thisweekinreact&utm_medium=newsletter&utm_campaign=26q2&utm_content=1st)

Meticulous 是一款自动化、全面且确定性的测试工具，让开发者在零维护成本下快速交付可靠代码，深受 Dropbox、Notion 等企业信赖。

- 🚀 **零开发者精力投入**：自动化生成并持续更新测试套件，无需手动编写、修复或维护测试用例。
- 🧪 **全面且确定性测试**：基于 Chromium 的确定性调度引擎，彻底消除测试不稳定（flakes），实现闪电般快速执行。
- 👁️ **实时监控与智能生成**：通过记录开发、预发布环境的用户交互，AI 引擎自动覆盖每一行代码、每个用户流程和边缘情况。
- 🔍 **PR 影响预览**：在合并前即可查看代码变更对用户工作流的影响，并自动模拟后端响应，避免假阳性。
- ⚡ **高速迭代**：持续为新增功能或边缘情况添加测试，自动淘汰过时测试，确保测试套件始终最新且完整。
- 🔄 **灵活集成**：可补充或替代现有测试套件，支持 NextJS、React、Vue、Angular 等主流框架，数分钟内完成设置。
- 🛡️ **企业级安全与规模**：测试在计算集群上高度并行化，1000+ 屏幕测试结果可在 120 秒内获取，已获 100+ 组织信赖。

---

### [Meticulous AI - 无需编写测试的自动化前端测试](https://www.meticulous.ai/?utm_source=thisweekinreact&utm_medium=newsletter&utm_campaign=26q2&utm_content=1st#:~:text=Once%20we%20started%20using%20Meticulous%2C%20we%20couldn%27t%20imagine%20working%20without%20it.)

**原文标题**: [Meticulous AI - Automated Frontend Testing Without Writing Tests](https://www.meticulous.ai/?utm_source=thisweekinreact&utm_medium=newsletter&utm_campaign=26q2&utm_content=1st#:~:text=Once%20we%20started%20using%20Meticulous%2C%20we%20couldn%27t%20imagine%20working%20without%20it.)

Meticulous 是一款自动化、详尽且确定性的测试工具，帮助开发者在无需手动编写或维护测试的情况下，快速交付可靠代码，已被多家大型企业采用。

- 🚀 **零开发者投入的详尽验证**：自动化、确定性测试，让开发者无需再手动编写、修复或维护测试用例。
- ⏱️ **快速迭代与即时反馈**：在合并代码前即可看到变更对用户工作流的影响，大幅提升交付速度。
- 🧪 **AI 自动生成并进化测试套件**：通过记录日常开发交互，AI 引擎持续生成覆盖所有代码路径和边缘用例的测试。
- 🔒 **从底层消除不稳定测试**：基于 Chromium 的确定性调度引擎，彻底消除测试假阳性，确保结果可靠。
- ⚡ **闪电般的大规模测试**：测试在计算集群中高度并行化，1000+ 屏幕测试可在 120 秒内完成。
- 🔧 **无缝集成与低门槛**：添加脚本标签即可开始录制，支持 NextJS、React、Vue 等主流框架，无需特殊测试账号或模拟数据。
- 🏢 **受知名企业信赖**：已被 Dropbox、Notion、Engine 等组织采用，开发者反馈“无法想象没有它的工作”。
- 🔄 **可补充或替代现有测试**：既可配合现有测试套件使用，也可完全取代，自动适应应用演进。

---

### [React Navigation 8.0 - 七月进度报告 | React Navigation](https://reactnavigation.org/blog/2026/07/08/react-navigation-8.0-july-progress/)

**原文标题**: [React Navigation 8.0 - July Progress Report | React Navigation](https://reactnavigation.org/blog/2026/07/08/react-navigation-8.0-july-progress/)

React Navigation 8.0 自 3 月以來新增多項改進和新功能，包括懸浮啟用導航、實驗性數據加載器、類型鉤子增強、共享深度連結路徑、堆疊導航器預加載和保留螢幕、動態屬性、Material 3 設計、SF Symbols 內容轉場、串流伺服器渲染、標準導航 API 以及升級遷移代理技能。

- 🚀 **懸浮啟用導航**：支援並發渲染和過渡，導航可中斷、避免加載指示器，並等待待處理動作。
- 📊 **實驗性數據加載器**：螢幕支援 `UNSTABLE_loader` 屬性，用於預取數據，避免瀑布效應，並與現有數據庫集成。
- 🔧 **動態導航器類型鉤子**：`useNavigation` 和 `useNavigationState` 現在知道導航器類型，無需手動註解，減少樣板代碼。
- 🔗 **共享深度連結路徑**：同一螢幕在多個導航器中可使用相同路徑，自動或手動標記為共享，並根據用戶位置正確導航。
- 🗂️ **堆疊導航器預加載改進**：預加載螢幕現在像常規螢幕一樣運作，支援事件、參數更新和嵌套導航器，且重複預加載會更新而非添加。
- 💾 **保留螢幕**：堆疊導航器支援保留螢幕，即使導航離開仍保持渲染，適用於頻繁使用的重螢幕或背景播放。
- 🎨 **動態屬性**：靜態配置導航器新增 `with` 方法，可根據動態狀態（如螢幕大小）配置選項。
- 🖌️ **Material 3 設計**：Material 頂部標籤和標籤視圖更新為 Material Design 3，支援圓角指示器和多種變體。
- 🌐 **SF Symbols 內容轉場**：`SFSymbol` 組件支援 `contentTransition`，在 iOS 17 上實現符號變更動畫。
- 📡 **串流伺服器渲染**：支援 `renderToPipeableStream` API，實現 HTML 串流傳輸到客戶端。
- 🔄 **標準導航 API**：為庫作者提供標準導航介面，便於與 React Navigation 和 Expo Router 整合。
- 🤖 **升級遷移代理技能**：提供代理技能，協助從 6.x 升級到 7.x 或 8.x，以及從動態配置遷移到靜態配置。

---

### [使用 Argent 关闭代理循环](https://swmansion.com/blog/closing-the-agent-loop-autonomous-react-native-bug-reproduction-with-argent/)

**原文标题**: [Closing the Agent Loop with Argent](https://swmansion.com/blog/closing-the-agent-loop-autonomous-react-native-bug-reproduction-with-argent/)

本文探讨了使用 Argent AI 代理自主复现 React Native 应用中的 bug，并生成详细报告的过程，旨在减少手动操作，提高开发效率。

- 🤖 **自主代理执行**：Argent AI 代理能够自主处理模拟器设置、身份验证和导航，无需人工干预，即可复现 GitHub 上的真实问题。
- 📋 **结构化报告生成**：代理会生成包含明确结论（是否成功复现）、关键证据（截图、日志）和追踪要求的 Markdown 报告，便于后续审查。
- 🔒 **安全考量**：通过直接调用 Gmail API 并提取验证码，避免模型接触原始邮件内容，从而防范提示注入攻击。
- 🧪 **实验验证**：代理成功复现了一个 React Native 应用中的 bug，包括 UI 行为异常和运行时警告（如重复的列表键），并提供了详细证据。
- 🔍 **追溯性分析**：报告将问题描述中的每个前提条件与执行证据一一对应，确保复现过程的透明性和可验证性。
- 🚀 **未来改进**：下一步计划将代理直接连接到代码工作区，使其不仅能复现 bug，还能尝试修复、创建分支和拉取请求，实现完全自主的 AI 工作流。

---

### [发布 v0.14.0 · software-mansion/argent · GitHub](https://github.com/software-mansion/argent/releases/tag/v0.14.0)

**原文标题**: [Release v0.14.0 · software-mansion/argent · GitHub](https://github.com/software-mansion/argent/releases/tag/v0.14.0)

这是一个关于软件项目 argent v0.14.0 版本的发布说明。

- 🥇 **新功能亮点**：新增 Apple TV (tvOS) 和 Android TV 支持；对 argent lens 进行了重新设计；新增 Kiro CLI 支持；新增 sim-remote 支持；为 DescribeNode 传递 ax 标识符。
- 🐛 **问题修复与改进**：修复了 stop-metro 中只终止监听器的问题；修复了 argent-lens 中变体帧裁剪导致可见元素标记为屏幕外的问题；修复了调试器返回对象/数组结果的问题；修复了 argent-lens 原生窗口控件、光标和卡片布局的问题；修复了工具服务器中 Chromium WebSocket 升级的认证问题；修复了分析器中同名组件和平台变体的显示问题；修复了 vega CLI 通过 ps 探测停止 VVD 的问题；修复了调试器中 device_id 未匹配导致静默合并的问题；修复了 argent-lens 预览路由中设备列表验证的缓存问题；修复了 nvm 切换节点后工具服务器重复启动的问题；修复了 list-devices 命令挂起的问题。
- 🔢 **内部优化**：CI 流程中每次推送主分支时发布“next”预览版；修复了下载 dylib Mach-O 平台验证的脚本；将所有工作区包升级到 0.14.0；更新了 npm-major 和 github-actions 依赖；为每个托管 CI 平台添加了设备端到端冒烟测试；检测云/远程 AI 代理环境并标记事件；用标准包替换了手动编写的解析器。
- 👥 **新贡献者**：j-piasecki 和 scianek 首次贡献。

---

### [发布 v0.19.0 · callstack/agent-device · GitHub](https://github.com/callstack/agent-device/releases/tag/v0.19.0)

**原文标题**: [Release v0.19.0 · callstack/agent-device · GitHub](https://github.com/callstack/agent-device/releases/tag/v0.19.0)

v0.19.0 版本发布，包含多项新功能、改进和修复，重点提升自动化测试的可靠性、诊断能力和用户体验。

- 🎯 **一键操作与观察**：`--settle` 现在可返回带有最新引用的稳定差异，并支持可选的 `--verify` 验证。
- 🔒 **更安全的引用、选择器和点击**：新增 `tap` 作为 `press` 的别名，对过期或视口外的引用发出警告，对不可点击目标提供提示，MCP 可自动固定快照引用。
- 🧹 **更清晰的快照验证**：快照输出去重继承的标签/标识符，并推广 `diff snapshot` 用于紧凑的前后对比。
- 🩺 **更好的代理诊断**：引入类型化错误、ADB 超时提示、标准错误摘录，以及新的 `capabilities` 命令。
- 📱 **更可靠的 iOS 自动化**：限制捕获卡顿，运行器恢复保留会话，文本输入更快，主线程超时提示更清晰。
- 🗂️ **更持久的工件和录制**：工件具有语义类型和确定性下载，Android 录制可在守护进程重启后恢复。
- 🔧 **大量代码重构与性能优化**：包括拆分模块、压缩输出、优化启动路径、迁移构建工具等。
- 🐛 **多项错误修复**：修复了引用提示、命令报告、超时处理、录制恢复、文本输入速度等多个问题。

---

### [Maestro MCP | 移动应用的智能 UI 测试](https://maestro.dev/mcp?utm_source=this-week-in-react)

**原文标题**: [Maestro MCP | Agentic UI Testing for Mobile Apps](https://maestro.dev/mcp?utm_source=this-week-in-react)

概述总结
Maestro MCP 是一个免费开源的 AI 原生移动应用测试工具，允许 Claude、Cursor 等编码代理在模拟器上自动编写、运行和修复端到端测试，生成可重复的 YAML 测试流。

- 🤖 **AI 驱动测试**：编码代理能自动打开模拟器、检查视图层次、编写 Maestro 流并运行测试，失败时自动修复，无需离开代理环境。
- 📝 **自然语言描述**：用普通语言告诉代理要测试什么（如“登录、添加商品到购物车并结账”），无需记忆选择器或编写样板代码。
- 🔄 **闭环迭代**：代理检查屏幕、编写 YAML 流、在实时模拟器上运行，并自我修正直到测试通过，生成可重复的端到端测试。
- ⚙️ **功能丰富**：支持结构测试、内容正确性、选择器、持久化、重置、导航和可访问性测试（如 15 个具体测试用例）。
- 🔓 **开源无锁定**：基于开源构建，可扩展，无供应商锁定，测试流是纯 YAML 文件，可版本控制并在 CI 中持续运行。
- 🚀 **快速设置**：约 5 分钟完成设置，先安装 Maestro CLI（需 Java 17+），再在编码代理上安装 MCP 服务器，重启后即可使用。
- 📱 **跨平台支持**：支持 iOS 和 Android，可在模拟器或物理设备上运行，适用于多种编码代理（Claude Code、Cursor、Copilot 等）。

---

### [CHANGELOG.md](https://raw.githubusercontent.com/react/react-native/main/CHANGELOG.md)

**原文标题**: [CHANGELOG.md](https://raw.githubusercontent.com/react/react-native/main/CHANGELOG.md)

React Native 0.87.0-rc.0 版本更新，包含大量破坏性变更、新增功能、性能优化和问题修复。

- 🚨 **破坏性变更**：移除多个已弃用的 API，如 `StatusBar` 的 `backgroundColor` 等属性、`ScrollView` 的 `keyboardShouldPersistTaps` 布尔值支持、`InteractionManager`、`NativeMethods` 类型等；限制对 `react-native/src/private/...` 的深层导入；要求 Node.js >= 22.13.0；移除对独立 `react-devtools` 的 WebSocket 支持；`useColorScheme()` 返回类型改为 `ColorSchemeName | null`；Android 采用 AGP v9；iOS 移除大量旧架构协议和代码。
- ✨ **新增功能**：新增 `react-native/asset-utils` 包；支持 `textAlign: 'start'` 和 `'end'`；`TextInput` 新增 `selection` 事件数据；支持原生驱动的 `AnimatedValue` 插值缓动；新增 `Page.addScriptToEvaluateOnNewDocument` 等 CDP 方法；`StatusBar` 支持 `barStyle="auto"`；新增 `ArrayBuffer` 支持 C++ 和 ObjC TurboModules；新增 CSS Flexbox §4.5 自动最小尺寸支持；Android 新增 `ACCESS_LOCAL_NETWORK` 权限；iOS 新增 `enableIOSCompressedTextFrameAdjustment` 特性标志。
- 🔧 **变更**：Metro 升级到 0.86.0；默认转换配置文件改为 `hermes-stable`；`window` 和 `navigator` 全局对象变为不可写；`EventTarget` 方法变为可枚举；`flattenStyle` 优化性能；移除 `experimental_` 前缀从 `backgroundImage`；`useTurboModules` 默认启用；Android 最低 `compileSdk` 提升至 34，Gradle 升级至 9.4.1，Kotlin 升级至 2.2.0；iOS 修复死锁问题。
- 📝 **弃用**：弃用 `react-native/assets-registry`、`ImageBackground`、`DrawerLayoutAndroid`、`UTFSequence`、`NativeMethods` 接口、`Appearance.setColorScheme('unspecified')`、`UIBlock` 接口等。
- ❌ **移除**：移除已弃用的 `Modal` 的 `animated` 属性、`PublicScrollViewInstance` 和 `PublicModalInstance` 类型、`InteractionManager`、`useTurboModules` 特性标志、`enableVirtualViewDebugFeatures` 等；Android 移除 `DisplayMetricsHolder` 相关方法、`UIImplementation`；iOS 移除 `TimingModule` 和旧架构代码。
- 🐛 **修复**：修复 `AbortSignal.any()` 处理逻辑、`Blob.slice()` 负数偏移问题、`FileReader` 状态设置、文本测量重复使用问题、`Animated.Value` 回调值同步、`Image` 的 `srcSet` 解析、`TextInput` 多行切换问题、Android 文本装饰线颜色和宽度、iOS 弹窗和模态框位置、数据竞争崩溃、内存泄漏等大量问题。
- 🔒 **安全**：修复 `xmldom/xmldom`、`fast-xml-parser`、`yaml`、`fast-uri` 和 `addressable` 等依赖中的安全漏洞。

---

### [移除已弃用的 API · 问题 #57384 · react/react-native · GitHub](https://github.com/react/react-native/issues/57384)

**原文标题**: [Remove deprecated APIs · Issue #57384 · react/react-native · GitHub](https://github.com/react/react-native/issues/57384)

概述摘要
React Native 计划移除一批已废弃的 API，以精简代码库并避免新用户混淆。

- 🗑️ 移除 Modal 组件的 `animated` 属性（自 0.60 版本起废弃）
- 📜 移除 ScrollView 的 `keyboardShouldPersistTaps` 布尔值支持（自 0.60 版本起废弃）
- 🚫 移除 VirtualizedList 的 `disableVirtualization` 属性（自 0.60 版本起废弃）
- 📱 移除 StatusBar 的 `backgroundColor` 和 `translucent`（Android，自 0.76 版本起废弃）
- 📱 移除 StatusBar 的 `setNetworkActivityIndicatorVisible()`（iOS，自 0.77 版本起废弃）
- ⌨️ 移除 TextInput 的 `blurOnSubmit` 属性（自 0.77 版本起废弃）
- ⚡ 移除 InteractionManager 剩余内容（自 0.80 版本起废弃）
- 🛡️ 从公开 API 中移除 SafeAreaView（自 0.81 版本起废弃）

---

### [React Native 连接大会](https://reactnativeconnection.io/?utm_source=thisweekinreact.com)

**原文标题**: [React Native Connection Conference](https://reactnativeconnection.io/?utm_source=thisweekinreact.com)

本次会议是法国首届完全专注于 React Native 开发者社区的会议，将于 2026 年 9 月 24 日在巴黎举行，旨在促进开发者交流并分享最新实践与趋势。

- 🗓️ 会议将于 2026 年 9 月 24 日在巴黎举行，为期一整天，聚焦 React Native 社区。
- 🎤 演讲嘉宾阵容强大，包括 Legend State 创始人、Software Mansion 团队成员、React Navigation 维护者等。
- 🎫 门票分为早鸟（229€）、常规（289€）和晚期（349€）三档，均含完整会议、餐饮和社交活动，数量有限，先到先得。
- 📢 演讲征集（CfP）已开放，欢迎提交研究或想法，有机会登台分享。
- 🏢 赞助商包括 Codemagic（提供 CI/CD 和 OTA 更新服务）和媒体伙伴 weshipit.today 与 This Week in React。
- 👥 组织团队由多位资深 React Native 开发者组成，涵盖性能优化、开源维护、社区活动等领域。
- ❓ 常见问题与赞助信息可通过官网查询，欢迎联系获取更多详情。

---

### [Kotlin 多平台 vs React Native（2026 基准测试）](https://swmansion.com/blog/we-built-the-same-app-in-kmp-and-react-native-here-s-what-we-found/)

**原文标题**: [Kotlin Multiplatform vs React Native (2026 Benchmark)](https://swmansion.com/blog/we-built-the-same-app-in-kmp-and-react-native-here-s-what-we-found/)

本文通过构建相同的应用，对比了 Kotlin Multiplatform (KMP) 和 React Native (RN) 在多个性能指标上的表现，发现两者各有优劣，没有绝对的赢家。

- 📱 **Android 上 KMP 全面领先**：在应用体积、启动时间和内存占用上，KMP 均优于 RN，主要原因是 KMP 没有 JavaScript 运行时开销。
- 📦 **应用体积差异巨大**：在 Android 上，KMP 的下载大小仅为 2.0 MB，而 RN 高达 15.8 MB；在 iOS 上两者差距很小，RN 略小 1.3 MB。
- ⏱️ **启动时间因平台而异**：Android 上 KMP 比 RN 快 2-4 倍；iOS 上两者在现代设备上几乎无差异，RN 甚至在部分设备上更快。
- 🧠 **内存占用平台反转**：Android 上 KMP 内存占用约为 RN 的一半；iOS 上 RN 内存占用仅为 KMP 的 1/3 到 1/4，因其使用原生 UIKit 渲染。
- ⚙️ **CPU 使用率无显著差异**：在测试场景中，两者的 CPU 占用接近，结果受设备和其他因素影响，无法判定优劣。
- 🧪 **Flashlight 工具验证**：独立测试工具的结果与手动测量一致，KMP 在 Android 上 RAM 更低，但整体性能评分几乎相同。

---

### [使用 Re.Pack 的移动模块联邦：当运行时交付值得复杂化时](https://www.callstack.com/blog/mobile-module-federation-with-re-pack-when-runtime-delivery-is-worth-the-complexity)

**原文标题**: [Mobile Module Federation With Re.Pack: When Runtime Delivery Is Worth the Complexity](https://www.callstack.com/blog/mobile-module-federation-with-re-pack-when-runtime-delivery-is-worth-the-complexity)

本文探讨了在大型 React Native 应用中使用 Module Federation 实现模块化架构的利弊，以及何时适用。

- 📱 **核心概念**：Module Federation 允许将独立构建的 JavaScript 模块（远程模块）在运行时加载到主应用（宿主）中，实现团队独立交付。
- 🧩 **适用场景**：当多个团队拥有独立产品域，且完整应用发布成为业务瓶颈时，Module Federation 能提供运行时独立交付能力。
- ⚙️ **技术实现**：通过 Re.Pack 工具，React Native 应用可实现 Module Federation，但远程模块只能动态加载 JavaScript，无法添加新的原生代码。
- 🚀 **主要优势**：团队可独立发布 JavaScript 变更，减少协调工作，提升交付速度，并支持超级应用架构。
- ⚠️ **引入的复杂性**：需处理远程模块不可用、兼容性、回滚、监控等运行时故障，并加强依赖管理。
- 🛠️ **验证步骤**：建议从单一远程模块开始，验证导航、认证、分析、回滚等关键环节，再逐步扩展。
- ❌ **避免场景**：当问题源于代码库过大、团队规模小或产品边界不清时，应优先考虑包共享或代码拆分，而非 Module Federation。

---

### [我们如何通过 React Native Brownfield 让混合 iOS 应用编译速度提升 39%](https://www.callstack.com/blog/how-we-made-hybrid-ios-apps-compile-39-faster-with-react-native-brownfield)

**原文标题**: [How we made Hybrid iOS apps compile 39% faster with React Native Brownfield](https://www.callstack.com/blog/how-we-made-hybrid-ios-apps-compile-39-faster-with-react-native-brownfield)

React Native Brownfield 3.10+ 通过使用 React Native 0.83+ 和 Expo 55+ 的预编译 XCFramework，将 iOS 打包速度提升最高 39%，大幅缩短 CI 构建时间。

- 📦 **预编译核心组件**：React Native 0.83+ 开始提供预编译的 `React.xcframework` 和 `ReactNativeDependencies.xcframework`，避免每次打包都编译数千个 C++/Objective-C 文件。
- ⚡ **显著性能提升**：实测显示，Expo 应用平均构建时间从 503 秒降至 305 秒（-39.3%），React Native 应用从 218 秒降至 155 秒（-29%），且统计上显著。
- 🛠️ **自动启用与兼容**：Brownfield 3.10+ 自动检测项目版本：RN ≥ 0.84 或 Expo ≥ SDK 55 默认启用预编译；RN 0.81-0.83 需手动传入 `--use-prebuilt-rn-core` 开启。
- 🔧 **底层技术调整**：包括 CocoaPods 条件依赖 `React-Core-prebuilt`、修复 Expo 框架的 `@rpath` 安装名、以及剥离辅助框架的二进制符号以避免链接冲突。
- 🚀 **CI 友好**：预编译消除了大型重复编译步骤，使 CI 流水线从“难以忍受”变为“可迭代”，尤其对频繁打包的团队价值巨大。
- ✅ **安全降级**：若在不支持的版本上尝试启用预编译，CLI 会提前报错，避免在 500 秒构建后出现晦涩的 Xcode 错误。

---

### [Drizz Vision AI 移动应用测试（iOS 与 Android）](https://www.drizz.dev/?utm_source=thisweekinreact&utm_medium=newsletter&utm_campaign=twir_w3&utm_content=ui-change-pain)

**原文标题**: [Drizz Vision AI Mobile App Testing for iOS & Android](https://www.drizz.dev/?utm_source=thisweekinreact&utm_medium=newsletter&utm_campaign=twir_w3&utm_content=ui-change-pain)

Drizz 是一家专注于移动端测试自动化平台的公司，已获得 270 万美元种子轮融资，并登上福布斯。其核心产品利用视觉 AI 和自然语言编写测试，解决传统自动化测试的痛点，如编写慢、易出错、维护成本高等问题，旨在帮助团队快速、稳定地交付移动应用。

- 💰 **融资与认可**：Drizz 获得 270 万美元种子轮融资，并登上福布斯，获得行业关注。
- 🤖 **核心能力：视觉 AI 测试**：利用企业级视觉 AI，像人类一样理解应用界面，实现自我修复、低误报的自动化测试。
- ✍️ **简化测试编写**：支持用“纯英语”描述测试步骤，无需编码经验即可快速创建测试用例，大幅降低编写门槛。
- 🛠️ **解决行业痛点**：针对传统工具（如 Appium）的测试编写慢、高误报率、维护成本高、覆盖不全等问题，提供高效的解决方案。
- 🚀 **提升团队效率**：通过 AI 驱动的稳定性、自我修复和精准调试，显著减少测试时间、降低误报率（降至约 5%），并提升发布信心。
- 📱 **全面平台支持**：支持 Android 和 iOS 应用在真实设备上执行测试，并可与 CI/CD 流水线无缝集成。
- 🏢 **企业级安全与部署**：提供企业级安全合规（如 SSO/SAML、RBAC），支持本地或 VPC 部署，满足金融、医疗等监管行业需求。
- 📊 **显著客户成果**：客户案例显示，测试周期缩短高达 10 倍，捕获的问题数量增加 5 倍，并大幅减少因 UI 变化导致的故障。
- 📚 **丰富的资源与社区**：提供详细的博客、案例研究、ROI 计算器等资源，帮助团队了解并实施现代化移动测试。

---

### [介绍 Sniffler：仅运行受变更影响的端到端测试](https://www.callstack.com/blog/introducing-sniffler-run-only-the-e2e-tests-your-changes-can-affect)

**原文标题**: [Introducing Sniffler: Run only the E2E tests your changes can affect](https://www.callstack.com/blog/introducing-sniffler-run-only-the-e2e-tests-your-changes-can-affect)

Sniffler 是一款工具，能识别受代码变更影响的端到端（E2E）测试，从而避免运行整个测试套件，在保持高信心的同时提升 CI 速度。

- 🚀 **核心问题**：每次拉取请求都运行全部 E2E 测试会拖慢开发速度，尤其在使用 AI 辅助工作流时，成本高昂。
- 🎯 **Sniffler 功能**：通过分析 JavaScript/TypeScript 项目的模块依赖关系，精准找出受变更影响的 E2E 测试，只运行相关部分。
- ⚙️ **快速入门**：安装简单（`npm install -D sniffler`），配置源文件和测试映射表后，即可使用 `npx sniffler impact` 或 `npx sniffler run` 命令。
- 🧠 **工作原理**：专注分析 import/export 语句构建依赖图，能追踪到具体导出实体，避免因 barrel 文件等产生误报。
- 🛠️ **灵活集成**：可配合任何接受文件参数的命令（如测试运行器、linter 等），将受影响文件列表传递过去。
- ⚠️ **当前局限**：仅支持 JavaScript/TypeScript，不分析原生代码（如 Kotlin、Swift）；测试映射表需手动维护，但团队正开发自动生成方案。
- 💡 **适用场景**：当 E2E 测试套件庞大，CI 管道因运行无关测试而耗时过长时，Sniffler 能帮助团队在速度和覆盖率间取得平衡。

---

### [GitHub - jo-duchan/tapflow: 面向全团队的自托管 iOS 与安卓模拟器流媒体服务 · GitHub](https://github.com/jo-duchan/tapflow)

**原文标题**: [GitHub - jo-duchan/tapflow: Self-hosted iOS & Android simulator streaming for the whole team · GitHub](https://github.com/jo-duchan/tapflow)

tapflow 是一个自托管的移动端 QA 工具，让团队通过浏览器远程使用 iOS 模拟器和 Android 模拟器，无需安装本地工具链，数据完全由自己控制。

- 🖥️ **自托管替代方案** — 作为 Appetize 和 BrowserStack 的开源替代，所有构建文件、设备流和录制数据都保留在自己的基础设施上，不上传第三方云。
- 🔧 **极简设置** — 只需 `npm install -g tapflow` 和 `tapflow start` 两步即可启动，无需 WebDriverAgent 或复杂配置。
- 🌐 **浏览器内 QA** — 团队成员无需安装 Xcode、Android Studio 或模拟器工具，通过浏览器即可实时与 iOS/Android 模拟器交互。
- 📡 **高效流媒体** — 使用 H.264 零缓冲解码器（WebCodecs 或 WASM/tinyh264）实现约 30 fps 的流传输，延迟低至 11-17 毫秒。
- 🔒 **安全与隐私优先** — 默认本地认证，远程访问需登录和角色权限（Admin/Developer/QA/Viewer），支持 Personal Access Tokens。
- 🛠️ **丰富功能** — 包括触摸/滑动/捏合输入、深度链接工具栏、应用中心（上传 .app.zip/.apk）、会话录制（72 小时自动清除）、截图 REST 端点、MCP 服务器等。
- 🤝 **团队协作** — 支持邀请链接、团队角色管理、Mac 资源监控，让后端、产品经理、设计师等非开发者也能轻松测试。
- 🚀 **灵活部署** — 单 Mac 即可运行，也可将中继服务器与代理分离部署，支持 PM2 自动重启和 nginx/Caddy 反向代理。
- 📜 **MIT 许可证** — 完全开源免费，积极开发中（v0.x），欢迎贡献代码和 PR。

---

### [ai/packages/adk 主分支 · callstackincubator/ai · GitHub](https://github.com/callstackincubator/ai/tree/main/packages/adk)

**原文标题**: [ai/packages/adk at main · callstackincubator/ai · GitHub](https://github.com/callstackincubator/ai/tree/main/packages/adk)

本页面介绍了 `@react-native-ai/adk` 包，这是一个为 Android 平台提供的 Vercel AI SDK 适配器，用于集成 Google 的 Agent Development Kit (ADK)，支持设备端 Gemini Nano 和云端 Gemini 模型。

- 📋 **概述**：该包是一个 Vercel AI SDK 提供者，用于在 Android 上使用 Google 的 Agent Development Kit (ADK)，支持设备端 Gemini Nano 或云端 Gemini，具备工具调用和多轮会话功能。
- 📱 **环境要求**：需要 Android `minSdkVersion` 26 或更高、React Native 新架构以及 Vercel AI SDK v6；使用设备端模型还需支持 Gemini Nano 的硬件。
- ⚙️ **配置指南**：消费应用需设置 `minSdkVersion` 为 26，并在打包时排除 `META-INF/INDEX.LIST` 和 `META-INF/DEPENDENCIES`；Expo 和裸 React Native 项目有对应的配置示例。
- 🚀 **快速开始**：通过 `import { adk } from '@react-native-ai/adk'` 引入，然后使用 `generateText` 等 AI SDK 函数即可调用模型。
- ✨ **核心特性**：支持云端 Gemini 模型、设备端 Gemini Nano、JavaScript 工具调用、流式响应、多模态输入（文本 + 图像）、结构化 JSON 输出以及 Vercel AI SDK v6 集成。
- 📊 **使用元数据**：ADK 会返回 token 用量（`promptTokenCount`、`candidatesTokenCount`、`totalTokenCount`），提供者会将其映射到 AI SDK 的 `usage` 对象中。
- 🖼️ **多模态输入**：支持在用户消息中通过标准 AI SDK 格式传递文件部分（如图片），示例展示了如何发送文本和图像。
- ☁️ **云端 Gemini 示例**：通过 `createAdkProvider` 配置 API 密钥、模型类型和名称，即可使用云端 Gemini 模型；注意不要在客户端应用中硬编码 API 密钥。
- 📱 **设备端 Gemini Nano**：提供了 `isNanoSupported()` 和 `isAvailable('genai-nano')` 两个检查方法，用于判断设备是否支持及运行时是否就绪；推荐在 UI 中根据状态显示或隐藏模型选项。
- 🔧 **工具调用示例**：展示了如何创建工具（如获取当前时间），并通过 `createAdkProvider` 的 `availableTools` 选项传递给模型，支持流式工具调用。
- 📄 **许可证**：该项目采用 MIT 许可证。

---

### [发布 v0.7.0 · software-mansion/react-native-enriched-markdown · GitHub](https://github.com/software-mansion/react-native-enriched-markdown/releases/tag/v0.7.0)

**原文标题**: [Release v0.7.0 · software-mansion/react-native-enriched-markdown · GitHub](https://github.com/software-mansion/react-native-enriched-markdown/releases/tag/v0.7.0)

react-native-enriched-markdown 发布了 v0.7.0 版本，包含多项新功能、修复和改进。

- 🚀 新增功能：支持 nativeID/testID 传递、==高亮==文本、嵌套无序列表不同标记、RaTeX 数学引擎（Android/iOS）、文本换行/断行属性、RTL 支持、选择菜单/格式菜单配置、本地化标签、复制为 Markdown/HTML、无障碍标签等。
- 🛠️ 修复与改进：修复 iOS 代码块边框、Android 任务列表点击、预测文本格式保持、表格渲染、颜色过滤、输入测量、自动聚焦、段落空白行、链接颜色、加粗/斜体冲突、模态闪烁、数学公式裁剪、手势冲突等问题。
- 🔄 重构：优化文本输入组件属性、提取选择菜单配置解析共享逻辑。
- 📚 文档与杂项：升级 RN 0.85/0.86、TypeScript 6、bob 0.41；同步 md4c 上游；更新 GitHub 链接；添加 Storybook 故事；配置 Android 示例应用；更新 CI 和截图。
- 🧪 测试：添加 Android CommonMark 渲染器、Compose 样式、Maestro E2E 测试。
- 🎉 新贡献者：hknakn、PierreCapo、p-malecki、graszka22、andreavrr、marcellov7、multiplechuks、eliotgevers、mvanhorn。

---

### [发布 8.17.0 · getsentry/sentry-react-native · GitHub](https://github.com/getsentry/sentry-react-native/releases/tag/8.17.0)

**原文标题**: [Release 8.17.0 · getsentry/sentry-react-native · GitHub](https://github.com/getsentry/sentry-react-native/releases/tag/8.17.0)

Sentry React Native 8.17.0 版本发布，包含新功能、修复和依赖更新，但存在已知的 Android 兼容性问题。

- ⚠️ **已知问题**：Android 版本在 16 KB 页面大小设备上存在兼容性问题，建议使用 8.17.1 版本。
- 🚀 **新功能**：添加实验性 `enableStandaloneAppStartTracing`，可将应用启动作为独立事务发送。
- 📱 **新功能**：新增 `Sentry.setAttribute` 和 `Sentry.setAttributes` 顶层 API。
- ⚡ **性能改进**：使用原生 `btoa` 进行信封 base64 编码，提升 `captureEnvelope` 性能。
- 🛠️ **构建优化**：支持 Expo Router 的 `ErrorBoundary` 自动包装，无需手动修改路由文件。
- 🔧 **默认值变更**：`mobileReplayIntegration({ networkCaptureBodies })` 默认设为 `true`。
- 🐛 **修复**：转发 Session Replay 网络详情选项到原生 SDK，以显示请求和响应体。
- 📦 **依赖更新**：Android SDK 升级至 v8.47.0，JavaScript SDK 升级至 v10.63.0，CLI 升级至 v3.6.0，Cocoa SDK 升级至 v9.19.1。

---

### [发布 1.5.0 版本 · margelo/react-native-nitro-fetch · GitHub](https://github.com/margelo/react-native-nitro-fetch/releases/tag/v1.5.0)

**原文标题**: [Release Release 1.5.0 · margelo/react-native-nitro-fetch · GitHub](https://github.com/margelo/react-native-nitro-fetch/releases/tag/v1.5.0)

概述摘要
- 🚨 页面加载时出现错误，提示重新加载
- ⭐ react-native-nitro-fetch 项目获得 907 颗星，有 32 个复刻
- 🔖 发布 v1.5.0 版本，包含多项更新
- 🛠️ 新增凭据支持功能（#135）
- 🔄 重构自动预取器的原生代码结构（#133）
- 🐛 修复 Response.blob() 和 Request.blob() 的二进制安全（#128）
- 🧪 添加令牌刷新测试（#131）
- 🔒 提交由 GitHub 验证签名，GPG 密钥 ID 为 B5690EEEBB952194
- 📁 包含锁文件更新（6d55fff）

---

### [发布 v2.1.0 · callstackincubator/voltra · GitHub](https://github.com/callstackincubator/voltra/releases/tag/v2.1.0)

**原文标题**: [Release v2.1.0 · callstackincubator/voltra · GitHub](https://github.com/callstackincubator/voltra/releases/tag/v2.1.0)

该页面显示了一个 GitHub 仓库的发布页面，介绍了 Voltra 项目的最新版本 v2.1.0，其中包含动态组件功能，但页面加载时出现错误。

- 🚀 **版本发布**：Voltra 项目发布了 v2.1.0 版本，由 V3RON 于 7 月 3 日发布。
- 🧩 **动态组件**：新版本引入了“动态组件”功能，由 Voltra 的原生端渲染引擎驱动。
- 🔄 **独立渲染**：组件被单独打包并在专用 JS 虚拟机中渲染，即使应用未运行也能响应环境变化。
- 📱 **iOS 支持**：可基于属性或环境变量（如 iOS 渲染模式：全色或强调色）动态调整布局。
- ⚠️ **实验性功能**：该功能标记为实验性，需要用户明确选择启用。
- 📚 **文档链接**：提供了 iOS 和 Android 文档链接供用户参考使用。
- ❤️ **社区反馈**：页面显示有 4 人做出反应，包括点赞、庆祝、爱心和火箭表情。
- ❌ **加载错误**：页面多次出现“加载错误”提示，建议用户重新加载。

---

### [发布 v15.0.0 · react-native-webview/react-native-webview · GitHub](https://github.com/react-native-webview/react-native-webview/releases/tag/v15.0.0)

**原文标题**: [Release v15.0.0 · react-native-webview/react-native-webview · GitHub](https://github.com/react-native-webview/react-native-webview/releases/tag/v15.0.0)

react-native-webview 发布了 v15.0.0 版本，这是一个重大更新，主要支持 Windows 平台的新架构，并升级了所有平台到最新的 React Native 版本。该版本包含许多破坏性变更和修复，目前通过 `@next` 标签安装，而稳定版仍为 v14。

- 🚀 **Windows 新架构支持**：Windows 实现现在需要 `react-native-windows` 的新架构（Fabric），移除了旧架构的 WebView 和 WebView2 实现。
- 📱 **平台升级**：所有平台升级到最新 React Native 版本，包括 Android/iOS 0.86.0、macOS 0.81.8、Windows 0.83.2 等，React 升级到 19.2.7。
- 🛠️ **CI 和构建修复**：修复了 CI 中的多个问题，如调整 Visual Studio 版本、修复 Windows 端到端测试、优化测试顺序等。
- 🐛 **Bug 修复**：修复了 Windows 上 `alert()` 导致 UI 线程冻结的问题，以及组件卸载时未正确清理 XamlIsland 和 WebView2 的问题。
- 🔄 **npm 发布策略**：v15 系列通过 `@next` 标签发布，不影响稳定版 v14 的用户。

---

### [发布 v0.86.0 · react/metro · GitHub](https://github.com/react/metro/releases/tag/v0.86.0)

**原文标题**: [Release v0.86.0 · react/metro · GitHub](https://github.com/react/metro/releases/tag/v0.86.0)

概述：Metro v0.86.0 版本发布，包含多项破坏性变更、性能改进和错误修复。

- 🚨 **破坏性变更**：Metro 现在始终生成整包索引映射源地图，并要求自定义序列化器/转换器使用 `VlqMap` 格式，而非元组。
- 🗑️ **移除废弃功能**：删除了公共入口点的废弃默认导出、YAML 和 `.es6` 配置文件支持，以及 `resolver.blacklistRE` 配置（改用 `blockList`）。
- 🐛 **错误修复**：修复了 `HttpStore` 写入重试时错误使用读取端点配置的问题。
- ⚡ **性能提升**：源地图处理优化使 Metro 内存使用减少 **50%**，源地图加载速度提升 **2 倍**，从而加快 RNDT 加载。
- 👥 **贡献者**：本次更新由 robhogan 和 durvesh1992 贡献。

---

### [GitHub - janicduplessis/rn-iso: 每个项目或工作树拥有独立的 React Native / Expo 开发环境——每个项目都有自己的 Metro 和模拟器。](https://github.com/janicduplessis/rn-iso)

**原文标题**: [GitHub - janicduplessis/rn-iso: Isolated React Native / Expo dev environments per project or worktree — each project gets its own Metro and simulator. · GitHub](https://github.com/janicduplessis/rn-iso)

rn-iso 是一个为 React Native / Expo 项目提供隔离开发环境的实验性工具，允许同一应用的多个工作树或编码代理并行构建，而不会发生端口或设备冲突。

- 🧪 **实验性工具**：为每个项目分配独立的 Metro 服务器和模拟器，支持并行开发，状态存储在 `~/.rn-iso/config.json` 中。
- 🚀 **快速启动**：通过 `npx rn-iso ios` 或 `npx rn-iso android` 命令即可运行，无需安装；使用 `--auto` 标志可跳过交互式选择。
- 📋 **丰富命令**：提供 `ios`、`android`、`start`、`stop`、`logs`、`device`、`status`、`reserve`、`release`、`shutdown` 和 `config` 等命令，管理项目和设备。
- 🔧 **工作原理**：自动分配端口（如 8082、8083），从模拟器池中选择设备，支持通过脚本或默认命令构建，并可选托管 Metro。
- 💾 **项目设置**：使用 `rn-iso config` 持久化 `packageManager`、`ios.script` 和 `android.script` 等设置，避免重复输入标志。
- 🏷️ **项目快捷方式**：通过 `--label` 为项目设置别名，方便后续命令引用。
- 🖥️ **系统要求**：macOS（iOS）或 macOS/Linux（Android），Node 20+，Xcode（iOS）或 Android SDK（Android）。
- 📄 **许可证**：MIT 许可证，开源且可自由使用。

---

### [发布 v0.16.0 · software-mansion-labs/react-native-bottom-sheet · GitHub](https://github.com/software-mansion-labs/react-native-bottom-sheet/releases/tag/v0.16.0)

**原文标题**: [Release v0.16.0 · software-mansion-labs/react-native-bottom-sheet · GitHub](https://github.com/software-mansion-labs/react-native-bottom-sheet/releases/tag/v0.16.0)

概述摘要  
react-native-bottom-sheet v0.16.0 版本发布，修复多项问题并优化性能，同时移除对 react-native-safe-area-context 的依赖。

- 🛠️ 修复拖拽过程中 detents 更新时的行为，基于拖拽开始时的快照进行位置锁定和索引选择  
- 📐 修复 `nativeOverlay` 模式下的尺寸问题，确保其基于全窗口而非 React 父容器  
- 🐛 修复 Android 底部面板有时无法打开的问题（由 @Titozzz 贡献）  
- 🔄 修复 Android 面板在分离时自动完全打开的问题（由 @lklima 贡献）  
- 📱 修复 iOS 上 `nativeOverlay` 模态面板可能重新以内联方式打开的问题  
- 🛡️ 修复 React Native 0.82 以下版本的 Android 构建问题  
- 🖱️ 修复 iOS 上嵌套滚动元素的滚动交互问题（由 @bjjeong 贡献）  
- 📍 修复 `nativeOverlay` 模态面板在非零原点挂载时的阴影节点坐标问题  
- 🔒 修复 iOS 面板内容意外变为不可交互的问题（由 @Thiago-Candia 贡献）  
- 🚫 修复 Android `nativeOverlay` 面板内容意外不可交互的问题  
- 📏 修复 Android `nativeOverlay` 面板高度被过度限制的问题  
- 🧹 移除对 `react-native-safe-area-context` 的依赖  
- 👥 感谢贡献者 bjjeong、Titozzz 等

---

### [发布 0.13.0 · software-mansion/react-native-audio-api · GitHub](https://github.com/software-mansion/react-native-audio-api/releases/tag/0.13.0)

**原文标题**: [Release 0.13.0 · software-mansion/react-native-audio-api · GitHub](https://github.com/software-mansion/react-native-audio-api/releases/tag/0.13.0)

这是 react-native-audio-api 库 0.13.0 版本的发布说明，包含多项新功能、错误修复和文档更新。

- 🚀 新增音频文件拼接、媒体元素音频源节点、播放速率支持及远程 URL 播放等功能
- 📖 更新了音频标签相关文档
- 🐛 修复了多项错误，包括 Android 构建问题、竞态条件、音频录制器回调重启、以及内存释放后使用等问题
- 🔧 重构了事件分发器、解码器、录制器和事件注册表，提升了稳定性和性能
- 🧪 新增了周期性波形输出和音频缓冲区队列的测试
- 🛠️ 改进了 CI 流程、构建配置和依赖管理
- 👥 新增了多位贡献者，如 Nezz、Traviskn、christian-apollo 等

---

### [发布 v0.14.0 · callstackincubator/rock · GitHub](https://github.com/callstackincubator/rock/releases/tag/v0.14.0-latest)

**原文标题**: [Release v0.14.0 · callstackincubator/rock · GitHub](https://github.com/callstackincubator/rock/releases/tag/v0.14.0-latest)

概述总结
- 🚀 新增功能：支持从静态库生成 xcframework（由@hurali97 在#716 中实现）
- 📦 发布版本：v0.14.0-latest（于 7 月 2 日发布）
- 🔐 签名验证：提交使用 GitHub 验证签名（GPG 密钥 ID: B5690EEEBB952194）
- ⚠️ 页面加载错误：多次出现“Uh oh! 加载错误，请重新加载页面”提示
- 👥 社区互动：1 人点赞（Brah-Timo）

---

### [GitHub - sagawrr/react-native-nitro-vision-kit: 适用于 React Native 的设备端背景移除与图像分类——原生 Vision（iOS）和 ML Kit（Android），零拷贝像素，基于 Nitro Modules 构建。](https://github.com/sagawrr/react-native-nitro-vision-kit)

**原文标题**: [GitHub - sagawrr/react-native-nitro-vision-kit: On-device background removal & image classification for React  Native — native Vision (iOS) and ML Kit (Android), zero-copy  pixels, built with Nitro Modules. · GitHub](https://github.com/sagawrr/react-native-nitro-vision-kit)

react-native-nitro-vision-kit 是一个 React Native 库，可在设备端实现背景去除和图像分类，通过 Nitro Modules 桥接到 iOS 的 Vision 和 Android 的 ML Kit。

- 🎯 **核心功能**：支持图像分割（抠出前景主体）和图像分类（为图像添加标签和置信度分数），并可单次解码同时执行两项操作。
- 📱 **平台支持**：iOS 17.0+ 支持分割，13.0+ 支持分类；Android 依赖 ML Kit 和 Play 服务；建议使用前检查 `VisionKit.capabilities`。
- 🛠️ **安装与使用**：需安装 `react-native-nitro-vision-kit` 和 `react-native-nitro-modules`，并通过 CocoaPods 配置；所有方法接受本地文件路径或 `file://` URI。
- 📄 **API 概览**：提供 `analyzeImage`、`removeBackground`、`classifyImage` 等方法，返回 `SegmentationResult` 对象，包含保存、内存访问和释放功能。
- ⚙️ **配置选项**：支持裁剪（`trim`）、最大像素（`maxPixels`）、保留遮罩（`retainMask`）、分类结果数量（`maxResults`）和置信度阈值（`minConfidence`）等参数。
- 📊 **输出结果**：分割结果包含尺寸、边界框和前景覆盖率；分类结果按置信度排序，返回标签和索引。
- 📜 **许可证**：采用 MIT 许可证，开源可用。

---

### [Reanimated 的未来发展方向 | 专访 Bartłomiej Błoniarz - YouTube](https://www.youtube.com/watch?v=T3ov18PfZRU)

**原文标题**: [Where Reanimated Goes Next | Interview With Bartłomiej Błoniarz - YouTube](https://www.youtube.com/watch?v=T3ov18PfZRU)

本頁面為 YouTube 平台的相關資訊與政策總覽，涵蓋版權、條款、私隱及營運方式等核心內容。

- 📰 提供新聞中心與聯絡我們，方便用戶獲取官方資訊與支援
- ©️ 明確版權與創作者權益，規範內容使用與刊登廣告
- 🔒 列出條款、私隱及政策安全，保障用戶與平台權益
- ⚙️ 說明 YouTube 的運作方式及測試新功能，提升透明度
- 🗓️ 標示版權年份為 2026 Google LLC，確認法律歸屬

---

### [为什么 Nitro 不仅仅是一座更快的桥梁 | 专访 Marc Rousavy - YouTube](https://www.youtube.com/watch?v=HueOt0ctSGQ)

**原文标题**: [Why Nitro Is More Than a Faster Bridge | Interview With Marc Rousavy - YouTube](https://www.youtube.com/watch?v=HueOt0ctSGQ)

本頁面為 YouTube 平台的各項基本資訊與政策總覽，涵蓋版權、聯絡方式、創作者支援及法律條款等核心內容。

- 📰 **新聞中心**：提供 YouTube 官方新聞與最新動態。
- ©️ **版權**：說明版權相關規範與權益保護。
- 📞 **聯絡我們**：提供與 YouTube 團隊聯繫的管道。
- 🎬 **創作者**：為內容創作者提供的資源與支援。
- 📢 **刊登廣告**：說明廣告投放與合作機會。
- ⚖️ **條款**：列出使用 YouTube 服務的相關條款。
- 🔒 **私隱**：說明用戶資料的收集與使用方式。
- 🛡️ **政策及安全**：涵蓋平台安全與內容政策。
- 🤖 **YouTube 的運作方式**：解釋平台的推薦與運作機制。
- 🧪 **測試新功能**：介紹 YouTube 正在測試的新功能。
- 🏢 **© 2026 Google LLC**：版權歸屬與法律聲明。

---

### [React Native 轻松实现：无需额外工作的平台原生动画](https://www.callstack.com/podcasts/react-native-ease-platform-native-animations-without-the-extra-work)

**原文标题**: [React Native Ease: Platform-Native Animations Without the Extra Work](https://www.callstack.com/podcasts/react-native-ease-platform-native-animations-without-the-extra-work)

本集播客讨论了 React Native Ease 库，它利用原生平台动画 API 简化简单动画的实现，同时不取代 Reanimated 等复杂工具。

- 🎙️ **React Native 动画新选择**：React Native Ease 库通过使用 iOS 的 Core Animation、Android 的 Animator API 和 Web 的 CSS 过渡，为简单动画提供原生性能。
- 🔧 **解决长期存在的痛点**：开发者 Janic 注意到 iOS 开发者常用 Core Animation，但 React Native 缺少直接暴露该路径的库，因此创建了 React Native Ease。
- 🚀 **性能优势**：在 iOS 上，Core Animation 将动画工作交给渲染服务器，避免占用 UI 线程，减少丢帧问题，尤其适合持续动画如缓慢移动的背景。
- ⚡ **简单 API 设计**：该库提供类似 React Native View 的组件，通过状态变化驱动过渡，无需学习共享值或命令式控制，保持代码简洁。
- 🤝 **与 Reanimated 互补**：React Native Ease 不替代 Reanimated，后者仍适用于手势驱动、复杂交互和逐帧计算，而 Ease 专注于简单、即用即弃的动画场景。
- 🎯 **实用案例驱动**：库的灵感来自客户端应用中的缓慢移动背景动画，使用 Core Animation 后消除了可见卡顿，促使 Janic 将其转化为可复用库。

---

### [Ecma International 批准新标准 - Ecma International](https://ecma-international.org/news/ecma-international-approves-new-standards-14/)

**原文标题**: [Ecma International approves new standards - Ecma International](https://ecma-international.org/news/ecma-international-approves-new-standards-14/)

Ecma International 在 2026 年 6 月 30 日的第 131 届大会上批准了多项新标准，涵盖 ECMAScript 语言规范、生态声明、国际化 API、嵌入式系统 API 及运行时密钥技术报告。

- 📜 ECMA-262 第 17 版：ECMAScript® 2026 语言规范
- 🌱 ECMA-370 第 7 版：TED 生态声明
- 🌐 ECMA-402 第 13 版：ECMAScript® 2025 国际化 API 规范
- 🔧 ECMA-419 第 4 版：ECMAScript®嵌入式系统 API 规范
- 🔑 ECMA TR/114第1版：运行时密钥技术报告

---

### [ECMAScript 2026 新特性 | pawelgrzybek.com](https://pawelgrzybek.com/whats-new-in-ecmascript-2026/)

**原文标题**: [What's new in ECMAScript 2026 | pawelgrzybek.com](https://pawelgrzybek.com/whats-new-in-ecmascript-2026/)

ECMAScript 2026 新增了多项实用功能，包括异步数组转换、错误类型安全检测、精确数值求和、Base64/十六进制转换、迭代器合并、JSON 解析源文本访问以及 Map/WeakMap 的便捷插入方法。

- 📜 **Array.fromAsync**：新增静态方法，可将异步迭代器或返回 Promise 的同步生成器转换为数组，填补了之前只有 `for await` 循环的空白。
- 🛡️ **Error.isError**：提供比 `instanceof Error` 更安全的错误类型检测方法，避免跨 realm 或原型修改导致的误判。
- ➕ **Math.sumPrecise**：精确求和函数，能避免浮点数精度损失（如 `1e20 + 0.1 - 1e20` 返回 `0.1` 而非 `0`），替代 `Array.reduce`。
- 🔄 **Uint8Array to/from Base64 和 hex**：内置方法支持 `Uint8Array` 与 Base64/十六进制字符串的相互转换，无需额外依赖库。
- 🔗 **Iterator Sequencing**：通过 `Iterator.concat` 方法轻松合并多个迭代器，并支持在中间插入普通值（如 `[2024]`），简化代码。
- 📝 **JSON.parse 源文本访问**：`JSON.parse` 的 reviver 回调新增 `source` 参数，可获取原始字符串，解决大数精度丢失和 BigInt 序列化问题（配合 `JSON.rawJSON`）。
- 🗂️ **Upsert**：Map/WeakMap 新增 `getOrInsert` 方法，一键实现“获取或插入”操作，减少条件判断的样板代码。

---

### [RFC 10008：HTTP QUERY 方法 | RFC 编辑者](https://www.rfc-editor.org/info/rfc10008/)

**原文标题**: [RFC 10008: The HTTP QUERY Method | RFC Editor](https://www.rfc-editor.org/info/rfc10008/)

RFC 10008 定义了 HTTP QUERY 方法，作为一种安全且幂等的请求方式，用于在服务器端执行查询操作，其请求内容包含查询参数，弥补了 GET 和 POST 方法在查询场景下的不足。

- 📜 **核心定义**：QUERY 方法是一种安全且幂等的 HTTP 方法，用于向目标资源发起查询请求，请求内容（而非 URI）包含查询参数。
- 🔄 **与 GET/POST 对比**：QUERY 克服了 GET 方法在查询参数过多或复杂时的局限性（如 URI 长度限制、编码效率低），同时明确了 POST 方法可能不具备的安全性和幂等性。
- 🛡️ **安全与幂等**：QUERY 请求被明确定义为安全（不改变资源状态）和幂等（可安全重试），支持缓存和自动重试机制。
- 🏷️ **媒体类型与协商**：QUERY 请求必须包含 `Content-Type` 头字段，服务器需根据媒体类型处理请求，并可通过 `Accept-Query` 响应头告知支持的查询格式。
- 🔗 **资源标识**：服务器可通过 `Content-Location` 或 `Location` 响应头为查询结果或查询本身分配 URI，支持后续通过 GET 请求直接访问。
- 💾 **缓存机制**：QUERY 响应可被缓存，缓存键必须包含请求内容及相关元数据，但缓存处理比 GET 更复杂。
- ⚠️ **安全考量**：QUERY 方法可能涉及敏感信息，服务器应避免在 URI 中暴露敏感数据；CORS 预检请求是必需的。
- 📋 **IANA 注册**：QUERY 方法和 `Accept-Query` 头字段已分别注册到 HTTP 方法注册表和字段名注册表。

---

### [供应链安全的分阶段发布 | nuqs](https://nuqs.dev/blog/staged-publishing-for-supply-chain-security)

**原文标题**: [Staged publishing for supply-chain security | nuqs](https://nuqs.dev/blog/staged-publishing-for-supply-chain-security)

本文介绍了 nuqs 包为应对供应链攻击，如何重构其发布流程以增强安全性。

- 🔒 **采用 npm 分阶段发布**：将发布拆分为“草稿”、“验证”和“最终确定”三个阶段，通过 2FA 验证和人工审批防止恶意代码直接进入仓库。
- 🛡️ **引入可重现构建验证**：通过比对本地生成的 tarball 哈希值与 npm 注册表上的哈希值，确保代码未被篡改，并提供离线验证脚本。
- ⚙️ **强化 GitHub Actions 工作流**：包括 SHA-1 固定所有依赖、限制权限范围、避免缓存中毒、禁用凭据持久化等，减少攻击面。
- 📦 **拆分原子发布流程**：将版本计算、npm 发布、GitHub 发布和通知解耦，允许失败无永久影响，提高流程的幂等性和安全性。
- 🧹 **优化发布说明生成**：自动化从 Git 提交生成变更日志，包含机器可读的 JSON 数据，减少手动维护工作并提升效率。
- 🚫 **暂停外部贡献者 PR**：在评估安全风险期间临时停止接受外部 PR，并扫描其他项目的工作流以发现类似问题。
- 📅 **事件时间线**：从 TanStack 攻击（5 月 11 日）到最终发布 nuqs@2.9.0（6 月 30 日），展示了逐步加固的过程。
- 🛠️ **消费者防护建议**：使用 pnpm 11 的安全默认值、设置 `minimumReleaseAge` 为 24 小时、安装 Socket Firewall 等，但指出这些措施仍有局限。

---

### [开始使用锚点定位 • Josh W. Comeau](https://www.joshwcomeau.com/css/anchor-positioning/)

**原文标题**: [Getting Started with Anchor Positioning • Josh W. Comeau](https://www.joshwcomeau.com/css/anchor-positioning/)

## 概述总结
- 📌 Anchor Positioning API 是 CSS 新功能，允许元素（目标）相对于另一个元素（锚点）进行定位，替代传统 JavaScript 方案
- 🔗 通过`anchor-name`和`position-anchor`属性建立锚点与目标的关联，使用`position-area`控制位置（如`top`、`bottom`）
- 🛠️ 支持自动溢出处理，当空间不足时目标元素会自动调整大小或通过`position-try-fallbacks`切换到备用位置
- 🔄 `position: fixed`与`position: absolute`的区别：固定定位以视口为包含块，滚动时更易触发溢出检测
- 💡 使用`flip-block`关键字可自动翻转方向，并同时翻转相关属性（如`margin`），兼容所有主流浏览器
- 🎨 Level 2 版本引入`container-type: anchored`容器查询，可基于备用位置动态调整样式（如翻转工具提示箭头方向）
- 🌐 浏览器支持：2026 年 1 月起主流浏览器均支持 Level 1，Level 2 仅 Chromium 支持，可通过 polyfill 或`@supports`提供降级方案
- ⚠️ 建议根据项目需求选择方案：简单场景用`flip-block`，复杂场景可继续使用 JavaScript 库，未来 1-2 年内 API 将更成熟稳定

---

### [宣布 TypeScript 7.0 - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-7-0/)

**原文标题**: [Announcing TypeScript 7.0 - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-7-0/)

TypeScript 7.0 正式发布，这是一个用 Go 语言重写的原生版本，速度提升高达 10 倍，并带来了全新的并行化架构和编辑器体验。

- 🚀 **性能飞跃**：全量构建速度提升 8-12 倍，例如 VS Code 代码库从 125.7 秒降至 10.6 秒；编辑器首次报错从 17.5 秒缩短至 1.3 秒以下。
- 🧠 **并行化架构**：引入 `--checkers`（类型检查器数量，默认 4）和 `--builders`（项目构建器数量）标志，可进一步利用多核 CPU 实现更高加速（如 VS Code 达 16.7 倍），同时提供 `--singleThreaded` 单线程模式。
- 💾 **更低内存占用**：在多数项目上内存使用减少 6%-26%，例如 VS Code 从 5.2GB 降至 4.2GB。
- 🔧 **编辑器全面支持**：基于 LSP 协议，支持 VS Code（专用扩展）、Visual Studio、WebStorm 等编辑器，并新增语义高亮、排序导入等缺失功能。
- 🏭 **生产就绪**：经微软内部（Loop、Office、PowerBI 等）及外部公司（Slack、Vanta、Canva 等）大规模验证，Slack 将 CI 类型检查从 7.5 分钟降至 1.25 分钟，Vanta 获得最高 9 倍加速。
- 📦 **安装与兼容**：通过 `npm install -D typescript` 安装；提供 `@typescript/typescript6` 包实现与 TypeScript 6.0 并行运行，方便工具过渡。
- 👁️ **改进的 `--watch` 模式**：基于 Parcel 文件监听器重写，大幅提升跨平台性能和资源效率。
- ⚠️ **配置默认值变更**：`strict` 默认开启，`module` 默认为 `esnext`，`target` 默认为当前稳定 ECMAScript 版本，`types` 默认改为 `[]` 等，需注意调整。
- 🔤 **模板字面量类型改进**：现在按 Unicode 码点（而非 UTF-16 代理对）分割字符，如 `"😀abc"` 的 `Head` 推断为 `"😀"`。
- 🧩 **JavaScript 支持重构**：JSDoc 类型推断更严格，废弃 `@enum`、`@class` 等旧模式，与 `.ts` 文件分析更一致。
- 🚫 **嵌入式语言暂不支持**：Vue、MDX、Svelte、Angular 等需继续使用 TypeScript 6.0，团队正积极合作解决。
- 🔮 **未来路线图**：7.1 将推出新 API，后续每 3-4 个月发布新特性版本，持续优化性能与体验。

---

### [Node.js — Node.js 26.5.0（当前版本）](https://nodejs.org/en/blog/release/v26.5.0)

**原文标题**: [Node.js — Node.js 26.5.0 (Current)](https://nodejs.org/en/blog/release/v26.5.0)

Node.js 26.5.0 版本发布，包含新发布密钥、多项功能增强和大量错误修复。

- 🔑 新增发布者 Stewart X Addison，其发布密钥为 655F3B5C1FB3FA8D1A0CA6BDE4A7D232B936D2FD
- 📦 buffer 模块新增 blob.textStream() 方法
- 🚩 ESM 模块新增 --experimental-import-text 实验性标志
- ⏱️ perf_hooks 支持按事件循环迭代采样延迟
- 🌊 stream 模块公开 ReadableStreamTee
- 🔒 TLS 模块可报告协商的 TLS 组
- 🛠️ 大量依赖更新：undici 8.7.0、nghttp3 1.17.0、sqlite 3.53.3 等
- 🐛 修复多项问题：权限模型传播、DH 生成器验证、inspector 崩溃等
- 📝 文档改进：新增首次贡献者指南、修复多处拼写错误和链接
- 🧪 测试与工具链优化：新增 GHA 基准测试运行器、改进覆盖率诊断
- 🗑️ 废弃与移除：宣布 macOS x64 二级支持即将结束
- 🔧 其他改进：zlib 新增 rejectGarbageAfterEnd 选项、VFS 支持虚拟文件描述符写入等

---

### [宣布 Vite+ Beta 版 | VoidZero](https://voidzero.dev/posts/announcing-vite-plus-beta)

**原文标题**: [Announcing Vite+ Beta | VoidZero](https://voidzero.dev/posts/announcing-vite-plus-beta)

Vite+ 测试版发布，统一了 Web 开发工具链，提供一致的工作流程。

- 🚀 Vite+ 测试版发布，统一运行时、包管理器和前端工具，提供一致的工作流程。
- 🛠️ 核心命令包括 `vp dev`（开发服务器）、`vp check`（代码检查）、`vp test`（测试）、`vp build`（构建）、`vp pack`（打包库）和 `vp run`（运行脚本）。
- 📦 集成了 Vite、Vitest、Rolldown、tsdown、Oxlint 和 Oxfmt 等最佳工具，完全开源且框架无关。
- 🔄 从 Alpha 到 Beta 阶段，发布了十几个版本，合并了超过 500 个拉取请求，改进了缓存、迁移、企业功能和跨平台支持。
- 🌍 已被超过 1300 个公共仓库采用，包括 Dify、BlockNote 和 npmx 等项目。
- 🎯 1.0 版本路线图包括远程缓存、GitLab CI/CD 支持、框架兼容性改进和更多迁移目标。
- 📥 可通过 `curl` 或 `powershell` 命令安装，并使用 `vp create` 或 `vp migrate` 开始使用。

---

### [发布 Tailwind CSS v4 · francoismassart/eslint-plugin-tailwindcss · GitHub](https://github.com/francoismassart/eslint-plugin-tailwindcss/releases/tag/v4.0.3)

**原文标题**: [Release Tailwind CSS v4 · francoismassart/eslint-plugin-tailwindcss · GitHub](https://github.com/francoismassart/eslint-plugin-tailwindcss/releases/tag/v4.0.3)

eslint-plugin-tailwindcss v4.0.3 版本发布，专为 Tailwind CSS v4 打造，完全重写并采用 TypeScript，依赖 Tailwind CSS 内部资源。

- 🎉 版本 v4.0.3 发布，专为 Tailwind CSS v4 设计
- 🔄 从零开始使用 TypeScript 重写
- 📦 基于 Tailwind CSS 内部资源（prettier-plugin-tailwindcss 和 tailwind-api-utils）
- 🚫 仅兼容 Tailwind CSS v4.x.x、ESLint flat config 格式和 Node >= 20.19.0
- 👏 感谢 hyoban 和 tailwind-api-utils 项目的贡献
- 🧪 在 Nx monorepo（使用 Next.js、React 和 Tailwind CSS 4）上测试

---

### [发布 v6.0.0 · webpack/webpack-dev-server · GitHub](https://github.com/webpack/webpack-dev-server/releases/tag/v6.0.0)

**原文标题**: [Release v6.0.0 · webpack/webpack-dev-server · GitHub](https://github.com/webpack/webpack-dev-server/releases/tag/v6.0.0)

webpack-dev-server v6.0.0 发布，包含多项重大变更、次要改进和补丁修复。

- 🚀 重大变更：Express 升级至 v5，webpack 依赖范围提升至 ^5.101.0，并放弃对 Node.js < 22.15.0 的支持。
- 📦 模块化：源码转换为原生 ES 模块，同时通过 exports 字段提供 ESM 和 CommonJS 两种构建版本。
- 🗑️ 移除功能：移除 CLI 标志、internalIP 方法、代理 bypass 选项、SockJS 支持和 spdy 依赖。
- 🔧 更新依赖：http-proxy-middleware 升级至 v4，webpack-dev-middleware 升级至 v8，并同步 originalUrl 以增强中间件兼容性。
- 🧩 新增插件支持：webpack-dev-server 现可作为 webpack 插件使用，避免多服务器启动并支持 MultiCompiler 设置。
- 🔒 安全增强：拒绝跨站请求至 open-editor 和 invalidate 端点，要求同源验证。
- 🛠️ 其他改进：启用 HTTP/2 压缩中间件，移除 colorette 依赖，更新 chokidar 至 v5 并支持 glob 模式，使用 WHATWG URL API 替代 url.parse。

---

### [pnpm 11.10 | pnpm](https://pnpm.io/blog/releases/11.10)

**原文标题**: [pnpm 11.10 | pnpm](https://pnpm.io/blog/releases/11.10)

以下是 pnpm 11.10 版本的更新摘要：

pnpm 11.10 新增了 CI 友好的认证设置、新命令 `pnpm prefix` 和 `pnpm issues`，以及支持通过 `pnpm self-update` 安装 Rust 移植版 v12。同时改进了 `pnpm up` 的准确性、加速了对忽略缩写元数据的注册表的解析，并强化了全局包管理、`pnpm deploy` 和 `pnpm pack-app` 的安全性。

- 🔐 **新增 `_auth` 设置**：支持通过环境变量或全局配置进行结构化注册表认证，避免 CI 环境中的变量名限制问题。
- 🚀 **`pnpm self-update` 支持 v12**：可安装 Rust 移植版 pnpm v12，无 Node.js 启动成本，性能更优。
- 📍 **新命令 `pnpm prefix`**：打印当前包前缀目录或全局前缀目录。
- 🐛 **新命令 `pnpm issues`**：作为 `pnpm bugs` 的别名，快速打开包的问题跟踪器 URL。
- 🔧 **修复 `pnpm up -r <pkg>`**：避免更新特定包时意外提升无关包的版本范围。
- ⚡ **加速解析**：针对忽略缩写元数据的注册表，裁剪完整文档后缓存，减少内存使用。
- 🛡️ **强化全局包管理**：修复 Windows 上 bin 清理问题，拒绝 `pnpm add -g pnpm@<version>`，验证依赖别名等。
- 📦 **`pnpm pack-app` 安全加固**：拒绝绝对路径或越界路径，防止覆盖非普通文件，并确保签名工具不被劫持。
- 🧩 **修复 `pnpm peers`**：不再报告被 `peerDependencyRules.ignoreMissing` 忽略的缺失依赖冲突。
- 🔄 **修复拓扑顺序**：确保 `--filter` 命令在项目间仅通过未选中项目传递依赖时正确排序。
- 🗝️ **新增 Node.js 签名密钥**：支持新发布者 Stewart X Addison 的密钥，确保运行时验证通过。

---

