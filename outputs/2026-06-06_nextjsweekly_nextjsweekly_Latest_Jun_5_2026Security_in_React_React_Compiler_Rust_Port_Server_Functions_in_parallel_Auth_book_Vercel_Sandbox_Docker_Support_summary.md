### [React 应用中的安全性 - Certificates.dev](https://certificates.dev/blog/security-in-react-applications)

**原文标题**: [Security in React Applications - Certificates.dev](https://certificates.dev/blog/security-in-react-applications)

本篇文章详细介绍了React应用中的安全实践，涵盖XSS防护、安全认证、服务端输入验证及内容安全策略。

- 🛡️ **React内置XSS防护**：React默认通过JSX自动转义特殊字符（如`<`、`>`），防止恶意脚本注入，用户输入渲染为纯文本。
- ⚠️ **dangerouslySetInnerHTML风险**：使用此属性会绕过React的自动防护，直接解析HTML，可能导致XSS攻击。必须先用DOMPurify库净化内容。
- 🔐 **安全认证与CSRF防护**：避免将令牌存储在`localStorage`或`sessionStorage`中，改用`HttpOnly`、`Secure`、`SameSite=Strict`属性的Cookie。同时使用CSRF令牌保护状态变更请求。
- ✅ **服务端输入验证**：使用Zod库在服务端进行类型安全的模式验证，结合参数化查询防止SQL注入，并确保用户授权。
- 🚫 **内容安全策略（CSP）**：通过HTTP头限制资源加载，如`script-src 'self'`阻止内联脚本。对必要的内联脚本使用Nonce，并用`Content-Security-Policy-Report-Only`测试策略。
- 🔄 **综合安全措施**：React应用需结合内置防护、安全认证模式、服务端验证和浏览器级策略，形成多层防御体系。

---

### [[编译器] 由 josephsavona 将 React 编译器移植到 Rust · 拉取请求 #36173 · facebook/react · GitHub](https://github.com/facebook/react/pull/36173)

**原文标题**: [[compiler] Port React Compiler to Rust by josephsavona · Pull Request #36173 · facebook/react · GitHub](https://github.com/facebook/react/pull/36173)

React 编译器正被移植到 Rust，这是一个实验性项目，旨在提升性能和跨工具集成能力。

- 🚀 **性能显著提升**：Rust 版本作为 Babel 插件运行时速度快 3 倍，其中实际转换逻辑快约 10 倍，与 OXC/SWC 等原生集成将更快。
- ✅ **高正确性与覆盖率**：所有 1725 个测试用例均通过，在 Meta 内部测试中，Rust 编译器与 TypeScript 版本输出一致率达 99.9%，剩余差异为改进或 Bug 修复。
- 🔧 **架构与集成**：采用与 TS 版本相同的架构（HIR、CFG、SSA），但使用竞技场式数据结构。目前提供 Babel、OXC 和 SWC 三种集成方式，未来计划将公共 API 统一为 Rust 表示的 Babel AST。
- 🤖 **AI 辅助开发**：架构由人类主导，但大部分代码由 AI 生成，开发过程中通过严格测试和人工审查确保代码质量。
- 📈 **内部测试结果**：在 Meta 内部使用后，后端变更带来了 25% 的性能提升（含 Babel 流水线的序列化开销），并修复了 TS 实现中的若干 Bug。
- 🛠️ **未来规划**：计划将返回 `Option<Program>` 改为返回补丁序列，优化 AST 表示（如使用竞技场分配和 `smol_str`），并实现自己的作用域解析。
- 🔗 **社区反馈**：已收到 Biome、SWC 等项目的反馈，正在考虑发布 crate 到 crates.io 以方便集成，并改进错误信息的类型化。

---

### [一个功能完备的TypeScript存储SDK——跨不同提供商的统一便携接口](https://storagesdk.dev/?utm_source=nextjs-weekly&utm_medium=newsletter&utm_date=2026-06-05)

**原文标题**: [A fully-featured TypeScript SDK for storage — one portable interface across different providers](https://storagesdk.dev/?utm_source=nextjs-weekly&utm_medium=newsletter&utm_date=2026-06-05)

StorageSDK 是一个跨提供商统一存储的 TypeScript SDK，核心特色是快照和分支功能，专为代理工作流设计，支持多种存储提供商。

- 📦 统一 API：通过切换适配器即可在不同提供商（Tigris、S3、R2、GCS、Azure 等）间切换，代码无需改动
- 📸 快照功能：冻结存储桶的某个时间点状态，父桶继续写入，快照保持只读不变，支持后续读取
- 🌿 分支功能：从快照或实时状态创建分支，代理可在分支上自由读写，完成后合并或丢弃，不影响父桶
- 🤖 代理友好：分支作为代理沙盒，每次运行可创建独立分支，快照确保每次运行可重现
- 🛠️ 丰富操作：支持上传、下载（文本/字节/流/完整项）、查看元数据、列表、复制、移动、删除等
- 🔗 签名 URL：支持 PUT 和 POST 方式生成预签名 URL，可设置大小和内容类型限制
- 🚫 中止支持：所有操作支持 AbortSignal，可取消上传、列表扫描等，中断写入不会提交
- ❌ 类型化错误：使用 StorageError 代码（NotFound、Conflict 等），保持跨提供商可移植性
- 🌐 Web 流：支持 ReadableStream 下载和上传，背压和取消传播端到端
- 🔌 可扩展：可编写自定义适配器，实现接口并通过一致性测试套件，支持第三方适配器
- 📦 轻量安装：ESM 仅限 Node 20+，核心零运行时依赖，适配器自带原生 SDK 作为可选对等依赖

---

### [通过 devjiwonchoi 并行运行服务器函数 · 拉取请求 #94277 · vercel/next.js · GitHub](https://github.com/vercel/next.js/pull/94277/files)

**原文标题**: [Run Server Functions in parallel by devjiwonchoi · Pull Request #94277 · vercel/next.js · GitHub](https://github.com/vercel/next.js/pull/94277/files)

此 Pull Request 旨在为 Next.js 添加实验性的并行服务端函数功能，以提升并发执行效率。

- 🚀 **核心功能**：引入 `experimental.parallelServerFunctions` 配置，允许客户端调用的服务端函数并行执行，而非串行排队。
- 🔄 **并行调用机制**：新增 `callServerParallel` 函数，在 `callServer` 中根据环境变量 `__NEXT_EXPERIMENTAL_PARALLEL_SERVER_FUNCTIONS` 进行分流，实现离线队列的并行请求。
- 🧵 **状态一致性保障**：并行路径在请求时记录 `expectedTree`，提交时与当前树对比，避免因导航或刷新导致的结果过期问题。
- 🧪 **测试覆盖**：新增 `test/e2e/app-dir/server-functions-parallel` 目录，包含多个测试场景（如缓存、目标页面、变更、读取、协调等），验证并行功能的正确性。
- ⚙️ **配置与构建**：在 `define-env.ts` 中添加环境变量定义，并在 `config-schema.ts` 和 `config-shared.ts` 中支持新配置项。
- 📁 **文件变更**：涉及 25 个文件（JS/TS/TSX），主要修改 `app-call-server.ts` 和 `server-action-reducer.ts`，以及新增测试套件。

---

### [React 编译器渲染指南 - Mark Erikson - YouTube](https://www.youtube.com/watch?v=WsAmM-sx9kA)

**原文标题**: [A Guide to React Compiler Rendering - Mark Erikson - YouTube](https://www.youtube.com/watch?v=WsAmM-sx9kA)

本頁面概述了YouTube平台的各項基本資訊與政策。
- 📰 新聞中心：提供YouTube官方新聞與公告。
- ©️ 版權：說明版權相關規範與保護機制。
- 📞 聯絡我們：提供用戶與YouTube聯繫的管道。
- 🎨 創作者：為內容創作者提供的資源與支援。
- 📢 刊登廣告：說明廣告投放選項與合作方式。
- 👨‍💻 開發人員：提供API與開發工具資訊。
- 📄 條款：列舉使用YouTube服務的條款與條件。
- 🔒 私隱：說明用戶資料的收集與使用政策。
- 🛡️ 政策及安全：涵蓋社群規範與安全措施。
- ⚙️ YouTube 的運作方式：解釋平台推薦與內容管理機制。
- 🧪 測試新功能：介紹YouTube正在測試的新功能。
- ©️ 2026 Google LLC：版權歸屬與法律聲明。

---

### [React性能优化：停止记忆化，开始优化——Depender Sethi](https://www.sethi.io/blog/react-performance-from-sluggish-to-lightning)

**原文标题**: [React Performance: Stop Memoizing, Start Optimizing — Depender Sethi](https://www.sethi.io/blog/react-performance-from-sluggish-to-lightning)

### 概述总结
React性能优化的核心在于减少不必要的工作，而非盲目添加记忆化。通过状态下移、并发特性、代码分割和合理分析，可以显著提升应用性能。

- 🚗 **状态下移是首要优化**：将状态放在实际使用的组件中，避免整个子树不必要的重新渲染，这是最有效的性能改进方法。
- 🧒 **子组件模式**：通过将子组件作为`children`传递，避免父组件状态更新时子组件重新渲染，无需记忆化。
- 🛑 **停止滥用记忆化**：`useMemo`和`useCallback`有额外开销，React编译器（React 19+）已自动处理大部分记忆化，手动添加只在真正必要时进行。
- 🚀 **使用并发特性**：`useTransition`和`useDeferredValue`可让非紧急更新在后台处理，保持用户输入流畅，是2026年最被低估的性能工具。
- 🧩 **代码分割与懒加载**：通过`lazy()`和`Suspense`按需加载页面和重型组件，但避免过度分割。
- 📊 **先分析再优化**：使用React DevTools分析器、Chrome性能标签和Core Web Vitals指标，找到真正的瓶颈（如16ms以上渲染或50ms以上长任务）。
- ⚠️ **避免常见陷阱**：不要在组件内定义组件、使用稳定key、拆分上下文、合并`useEffect`链、将静态JSX对象移出组件。

---

### [未找到标题](https://x.com/aidenybai/status/2062202659143115216)

**原文标题**: [No title found](https://x.com/aidenybai/status/2062202659143115216)

本页提示浏览器未启用JavaScript，需启用或更换支持的浏览器才能正常使用x.com。

- 🔒 检测到浏览器中JavaScript被禁用
- 🌐 请启用JavaScript或切换到支持的浏览器
- 📋 支持浏览器列表可在帮助中心查看
- ⚠️ 隐私相关扩展可能导致问题，建议禁用后重试
- 🔄 页面提供“重试”选项以应对临时错误
- 📜 页面底部包含服务条款、隐私政策等法律信息
- © 2026 X Corp. 版权声明

---

### [Pilcrow的认证手册](https://auth.pilcrowonpaper.com/)

**原文标题**: [Pilcrow's auth book](https://auth.pilcrowonpaper.com/)

这本个人编写的认证书籍专注于Web应用的身份验证与登录系统，提供免费、无广告的实用指南与示例。

- 📘 概述：这是一本聚焦Web应用认证与登录系统的免费个人技术书籍，包含指南、建议和代码示例
- 🔐 核心主题涵盖：认证方法、会话管理、邮箱地址、密码、浏览器客户端存储、CSRF防护等
- 🛠️ 技术细节包括：Argon2/Bcrypt加密算法、WebAuthn API、ECDSA/EdDSA/RSA签名方案
- 📂 提供完整开源示例：Go语言编写的密码认证示例（含邮箱验证和密码重置）和无密码认证示例（含Passkey和邮箱验证码）
- 🌐 支持资源：Discord服务器和GitHub Discussions可提问，GitHub Sponsors可赞助
- 👤 作者：Pilcrow，源码托管于GitHub

---

### [在Vercel沙箱中运行Docker容器 - Vercel](https://vercel.com/changelog/run-docker-containers-inside-vercel-sandbox)

**原文标题**: [Run Docker containers inside Vercel Sandbox - Vercel](https://vercel.com/changelog/run-docker-containers-inside-vercel-sandbox)

Vercel Sandbox 现在支持在沙箱内安装和运行 Docker，无需影响主机系统。

- 🐳 支持在沙箱内安装 Docker 并启动守护进程，可运行容器化应用（如 Redis）
- 🔧 通过 `runCommand` API 实现安装、启动和容器管理，支持 sudo 权限
- 💾 结合持久化沙箱功能，Docker 安装和拉取的镜像可在会话间保留
- 🧪 适用于运行测试依赖（如 Redis/Postgres）、验证容器镜像、预览容器化应用
- 🚀 新增对 FUSE 文件系统驱动和 VPN 客户端的支持，扩展了沙箱能力

---

### [更新日志 - shadcn/ui](https://ui.shadcn.com/docs/changelog)

**原文标题**: [Changelog - shadcn/ui](https://ui.shadcn.com/docs/changelog)

这是一个关于 shadcn/ui 库的更新日志和功能文档的摘要。

概述
- 🎉 **新增 GitHub 注册表**：可将任何公共 GitHub 仓库作为组件源，通过 CLI 直接安装，无需构建或发布。
- ⚡ **推出 `shadcn eject` 命令**：将共享的 Tailwind CSS 内联到项目全局样式文件中，移除对 `shadcn` 包的依赖。
- 🎨 **引入新样式 Rhea**：基于 Luma 的紧凑版本，提供更小的间距和更密集的界面，适合注重信息密度的产品。
- 🧩 **注册表支持 `include` 和 `validate`**：允许通过多个 `registry.json` 文件组合大型注册表，并新增验证命令确保配置正确。
- 📦 **支持包导入和目标别名**：CLI 现支持 `package.json#imports` 以及文件安装目标别名，提升组件安装灵活性。
- 🚀 **其他更新**：包括预设、指针光标、组件组合、Luma 样式、v4 CLI、RTL 支持、Base UI 文档、MCP 服务器、Tailwind v4 等多项功能。

---

### [概述](https://legendapp.com/open-source/list/v3/overview/)

**原文标题**: [Overview](https://legendapp.com/open-source/list/v3/overview/)

### 概述
Legend List 是一款高性能虚拟化列表组件，支持 React Native 和 React DOM，可替代 FlatList/FlashList，专为聊天、动态流和复杂列表场景优化。

- 🚀 **高性能虚拟化列表**：无需手动测量动态尺寸，支持初始滚动索引和末尾滚动，资源占用低（CPU 和内存均优于同类方案）。
- 💬 **聊天与动态流优化**：内置 `initialScrollAtEnd`、`maintainScrollAtEnd` 和 `anchoredEndSpace`，支持双向分页和滚动锚定，无需倒置列表或复杂 hack。
- 📱 **跨平台支持**：提供 React Native、React（Web）和 React Native Web 入口，共享同一 JS 引擎，仅类型不同。
- 🧲 **高级列表功能**：包括 SectionList（粘性标题）、`alwaysRender`（保持行挂载）、网格布局（`numColumns`）、视图性配置和异步滚动方法。
- 🆕 **v3 新特性**：新增 Web 支持、`initialScrollAtEnd`、`anchoredEndSpace`、键盘感知组件（`KeyboardAwareLegendList`）、Reanimated 动画集成和扩展的 `getState()` 工具。
- 📚 **快速入门**：从 `@legendapp/list/react-native` 或 `@legendapp/list/react` 导入，参考官方指南和迁移文档。

---

### [世博观察](https://expo.dev/solutions/expo-observe?utm_source=nextjsweekly&utm_medium=email&utm_campaign=observe-beta)

**原文标题**: [Expo Observe](https://expo.dev/solutions/expo-observe?utm_source=nextjsweekly&utm_medium=email&utm_campaign=observe-beta)

本页介绍的是 EAS Observe 工具，它将性能监控与每次构建和更新直接关联，帮助快速定位问题。

- 📊 **观察与构建管线深度集成**：Observe 能自动关联每次构建和 OTA 更新的性能指标，在几分钟内发现回归问题，而非几天。
- 🚀 **自动捕获用户真实体验**：自动测量 TTI、冷启动/热启动、帧率和包加载时间，无需手动添加自定义追踪。
- 🔍 **一键查看每次发布影响**：每个版本在时间线上显示为标记，悬停可看变化，点击可查看该构建或更新的所有事件。
- 🤖 **一键交接给 AI 分析**：在仪表盘或 CLI 中一键将数据传递给 Claude Code、Cursor 等 AI 工具，获取真实会话的答案。
- 📱 **深入分析慢速会话**：可按指标排序并深入单个会话，查看设备、OS、国家、更新渠道，并追踪完整事件时间线。
- 🧭 **按屏幕定位性能瓶颈**：Expo Router 集成后，导航标签页按路由分解 TTI，帮助快速找到慢速屏幕。
- 📈 **自动覆盖全设备范围**：P50、P90、P99 指标自动捕捉预算硬件、旧 OS、弱网络等场景，无需额外配置。
- ❓ **常见问题解答**：Observe 与 Sentry/Datadog 互补，支持采样率设置，仅适用于 Expo SDK 55+ 和 EAS，不收集个人身份信息。
- 🛠️ **一行代码快速集成**：安装 expo-observe 包并添加两行代码，即可开始收集性能数据。

---

### [导致60帧卡顿的DOM操作：基于275个代码仓库的布局抖动与反模式基准测试研究](https://stackinsight.dev/blog/dom-manipulation-empirical-study/)

**原文标题**: [DOM Manipulation That Kills Your 60fps: A Benchmarked Study of Layout Thrashing and Anti-Patterns Across 275 Repositories](https://stackinsight.dev/blog/dom-manipulation-empirical-study/)

本研究报告对275个开源仓库中常见的DOM操作反模式进行了基准测试和实证分析，揭示了导致60fps卡顿的关键瓶颈。

- 📊 **54.9%的仓库存在反模式**：在275个高DOM活动仓库中，超过一半（151个）至少存在一种反模式，总计发现2789个问题。
- 🔥 **innerHTML循环是最严重的性能杀手**：在1000个节点时，反模式比优化版本慢570倍（223ms vs 0.39ms），10000个节点时差距达7955倍（24.8秒 vs 3.12ms），呈O(n²)复杂度。
- ⚡ **强制同步布局是常见高严重性问题**：861个发现（高严重性），在10000个节点时基线耗时4.25ms vs 优化后1.89ms，每秒60帧下累计消耗255ms。
- 🎨 **循环中样式突变影响显著**：691个发现，10000个节点时基线15.18ms接近16.67ms帧预算，优化后降至4.72ms（3.2倍加速）。
- 🔍 **循环中DOM查询影响最小**：1110个发现（最多），但现代浏览器缓存使10000个节点时仅差0.69ms，优化效果有限。
- 🧩 **appendChild循环已非问题**：现代浏览器自动批处理，DocumentFragment反而可能稍慢（0.8-1.0倍），无需为性能使用。
- 🏢 **Vanilla JS仓库问题最多**：平均每个仓库38.9个发现，React为7.1个，Angular仅0.7个（因框架抽象）。
- 🚨 **顶级问题仓库**：Three.js（195个）、Highcharts（156个）、SortableJS（134个）、AG Grid（133个）等流行库存在大量反模式。
- 💡 **核心建议**：永远不要在循环中使用innerHTML +=；读写布局属性分离；批量样式变更用CSS类；无需为性能使用DocumentFragment；扫描依赖库。

---

### [我的2026年前端技术栈 - T型开发者](https://thetshaped.dev/p/my-frontend-stack-in-2026-react-nextjs-pnpm-vite-ts-tailwind-storybook-tanstack-zustand-zod-oxlint-oxfmt-msw-vitest-playright-sentry)

**原文标题**: [My Frontend Stack In 2026 - The T-Shaped Dev](https://thetshaped.dev/p/my-frontend-stack-in-2026-react-nextjs-pnpm-vite-ts-tailwind-storybook-tanstack-zustand-zod-oxlint-oxfmt-msw-vitest-playright-sentry)

本文介绍了作者在2026年实际用于构建生产级应用的前端技术栈，强调工具应简洁、协作良好且能节省时间，而非追求最新。

- 🚀 **基础框架**：根据场景选择——内容型网站用Next.js，内部工具和SPA用Vite 8 + React + TypeScript，搭配pnpm实现快速安装与磁盘节省。
- 🎨 **样式与组件**：Tailwind CSS处理样式，shadcn/ui提供可复用的组件原语，无需npm依赖，直接拥有代码所有权。
- 📚 **组件文档**：Storybook用于组件库的开发和文档，尤其适合组件数量超过20个的团队，但小项目可能过度。
- 🔄 **状态管理**：TanStack Query处理服务器状态（缓存、后台刷新），TanStack Router提供全类型安全路由；Zustand用于客户端共享状态，但简单状态仍用useState。
- 🛡️ **运行时验证**：Zod用于所有跨信任边界的验证（API响应、表单输入、环境变量），弥补TypeScript运行时缺失。
- ⚡ **代码质量工具**：Oxlint和Oxfmt基于Rust，速度比ESLint快50-100倍，改变开发者习惯，实现即时检查。
- 🧪 **测试体系**：Vitest用于单元测试，Playwright用于端到端测试，MSW作为网络模拟层，三者协同工作。
- 🔍 **生产监控**：Sentry提供错误监控和会话回放，AI摘要可快速定位问题，尤其适合排查用户实际遇到的bug。
- 💡 **核心理念**：每个工具专注单一功能且能良好协作，不试图成为平台或锁定用户，最终目标是让工具“隐形”并随时待命。

---

### [从Radix UI迁移到Base UI的9个简单步骤](https://shadcnstudio.com/blog/migrate-from-radix-ui-to-base-ui)

**原文标题**: [Migrate from Radix UI to Base UI in 9 Easy Steps](https://shadcnstudio.com/blog/migrate-from-radix-ui-to-base-ui)

本指南详细介绍了如何将 shadcn/ui 项目从 Radix UI 迁移至 Base UI，包括迁移原因、步骤、常见问题及未来展望。

- 🚀 **迁移原因**：Base UI 由 Radix UI、Floating UI 和 Material UI 的创建者共同打造，提供更清晰的 `render` prop API、统一的 `@base-ui/react` 包，并致力于长期稳定。
- 📋 **迁移步骤**：包括创建分支、配置 Base UI、更新自定义组件、将 `asChild` 改为 `render` prop、处理组件特有差异（如 Accordion、Select 等）、更新状态类名、清理依赖、全面测试。
- ⚠️ **常见陷阱**：注意 TypeScript 类型错误、CSS 中 `data-*` 属性需改为 `aria-*`、缺失的 prop 需查阅文档、构建错误需清理缓存、运行时警告需逐个解决。
- 🔮 **未来方向**：Base UI 获得强大团队支持，shadcn/ui 已默认支持 Base UI，建议新项目直接选用；现有项目可根据稳定性需求决定迁移时机。
- 📚 **资源推荐**：官方文档、GitHub 示例、社区讨论和 Discord 频道可提供迁移支持。

---

### [深入解析新版Raycast的技术细节 - Raycast博客](https://www.raycast.com/blog/a-technical-deep-dive-into-the-new-raycast)

**原文标题**: [A Technical Deep Dive Into the New Raycast - Raycast Blog](https://www.raycast.com/blog/a-technical-deep-dive-into-the-new-raycast)

Raycast 2.0 进行了从零开始的跨平台重写，采用混合技术栈以在 macOS 和 Windows 上实现原生体验和开发效率的平衡。

- 🚀 **跨平台重写**：从原生 Swift/AppKit 转向混合架构，结合 TypeScript、Swift、C#、Rust、Node 和 React，实现 macOS 和 Windows 统一代码库。
- ⚙️ **技术栈选择**：放弃 Electron 和 Tauri，采用自定义原生壳（Swift/C#）包裹系统 WebView，以获得最大平台控制和原生集成能力。
- 🧩 **四层架构**：分层设计包括原生宿主应用、React 前端、Node 后端和 Rust 核心，通过类型化 IPC 确保跨运行时通信安全。
- 🔍 **自研文件索引器**：用 Rust 构建全新文件索引器，支持 NTFS 主文件表直接扫描，实现秒级全盘索引，摆脱对 Spotlight 的依赖。
- 🎨 **原生体验优化**：通过禁用光标指针、避免悬停高亮、使用原生弹窗和材料效果等细节，让 WebView 界面行为完全符合桌面应用规范。
- 🛠️ **WebKit 调优**：解决动画节流、窗口缩放闪烁、emoji 渲染延迟等问题，通过预渲染和帧同步技术消除 WebView 常见缺陷。
- 💾 **内存权衡**：v2 内存占用约 350-450 MB（v1 为 200-300 MB），但通过压缩内存和共享框架降低实际系统压力，并持续优化中。
- ⚡ **性能提升**：搜索速度因 Rust 索引器显著加快，文本渲染利用 WebKit 优化，AI Chat 和富文本处理更流畅。
- 👥 **开发优势**：热重载加速迭代，多数团队在共享前端/后端工作，招聘更易，扩展无需额外下载 Node。
- 🔄 **权衡取舍**：栈复杂度增加、Windows 多样性挑战、部分原生行为需额外适配、窗口冷启动有延迟，但整体收益大于成本。

---

