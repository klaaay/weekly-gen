### [](https://nolanlawson.com/2026/10/03/why-dont-more-developers-use-the-platform/)

**原文标题**: [Why don’t more developers “use the platform”? | Read the Tea Leaves](https://nolanlawson.com/2026/10/03/why-dont-more-developers-use-the-platform/)

本文从“使用平台”这一倡导出发，分析为何许多开发者仍倾向自行造轮子，并探讨历史、习惯、文档、乐趣、理解不足以及 AI 编码可能带来的影响。

- 🌐 “使用平台”主张：浏览器原生能力通常比 JavaScript 自建方案更快、更易用、更可访问。
- 🕰️ 历史原因：浏览器长期落后，jQuery 等库填补空白；IE6 等阻碍新 API 普及，直到近年常青浏览器才成为主流。
- 📦 熟悉度原因：开发者习惯从 npm、React 生态找现成方案，即使平台 API 已足够，例如 CSS `position: sticky`。
- 📚 文档原因：npm 包常有精美 README 和教程；Web 平台文档曾较分散，MDN、web.dev 后来才成为权威来源。
- 🛠️ 自建更有趣：亲手实现弹窗、焦点陷阱、Esc 关闭等虽麻烦，但能学习、定制，并因“宜家效应”更愿维护自己的代码。
- 🧑‍💻 学习路径：许多平台倡导者曾写 polyfill 或库；作者因 PouchDB 深入 IndexedDB，最终参与标准讨论。
- 🤷 无知与 CSS 复杂性：不深入理解 CSS 会导致用 JS 解决本可 CSS 解决的问题；clearfix、floats、`min-width: 0` 等都不直观。
- 🗄️ 跨平台类比：ClickHouse 例子说明，未读文档而自建压缩或键值存储，结果可能不如平台自带的列式压缩与查询。
- 🤖 AI 乐观面：LLM 熟悉平台 API，可能选出更优原生方案；开发者不亲手写代码，宜家效应也会减弱。
- 🤖 AI 悲观面：LLM 可能重复造轮子、忽略已有函数，产生大量非平台惯用代码、过度工程和未充分测试的首版提交。
- ⚖️ 结论：作者喜爱“使用平台”口号，但也理解自建者的乐趣与背景；只要存在平台，这一争论就会持续。

---

### [获取失败](https://news.ycombinator.com/item?id=49950554)

**原文标题**: [Failed to retrieve](https://news.ycombinator.com/item?id=49950554)

无法总结：获取内容失败，状态码 419。

---

### [](https://master.dev/courses/codex/?utm_source=email&utm_medium=javascriptweekly&utm_content=codexcooper)

**原文标题**: [Build Ambitious Interfaces with OpenAI Codex | Master.dev](https://master.dev/courses/codex/?utm_source=email&utm_medium=javascriptweekly&utm_content=codexcooper)

这是一门由 OpenAI 的 Katia Gil Guzman 主讲的免费 Codex 前端开发课程，教你用 Agentic Coding 更快构建、迭代并部署现代前端界面，包含 22 节课、约 3.4 小时内容，并提供完成证书。

- 🚀 课程目标：用 OpenAI Codex 更快构建现代前端界面。
- 🧠 核心理念：前端开发因 Agentic Coding 而改变，需学会指挥 Codex 贯穿计划、构建和迭代流程。
- ⚙️ 设置 Codex：选择合适模型与推理强度，并通过结构良好的 Agents.md 提供项目上下文、插件、技能和浏览器工具。
- 🎯 构建与验证：给 Codex 视觉方向，结合目标设定、明确 UI 测试和迭代反馈保持控制。
- 🔁 提速方法：把团队前端工作流转化为可重复技能，按需生成一致、可预测的组件和功能。
- 🌐 部署：可直接从 Codex 部署到 ChatGPT Sites，分享 UI 作品。
- 📚 学习成果：掌握从想法到应用的实用工作流，并用 App Shots、标注和技能引用减少反复迭代。
- 💡 创新点：探索“Living Frontends”，用动态可视化替代静态截图，服务复杂主题和文档。
- 👩‍🏫 讲师：Katia Gil Guzman，OpenAI 开发者体验工程师，曾任职 Microsoft Azure Cognitive Services、创办 AI SaaS，并在 Stripe 担任解决方案架构师。
- 🧩 先修要求：了解提示词基础，并具备基本软件开发经验。
- 🗓️ 课程大纲：介绍 5 分钟、Codex 概览 31 分钟、Sites 构建 50 分钟、3D/动画/交互 41 分钟、现有代码库 23 分钟、Living Frontends 47 分钟、总结 4 分钟，总计约 3 小时 24 分钟。
- 📈 课程信息：22 节课、3.4 小时、4.5 评分，支持自定进度学习。
- 📝 学习体验：课程播放器、进度续学、转录旁笔记、课后测验和闪卡。
- 🏅 完成证书：完成课程后可获证书，并可分享到 LinkedIn。
- 🆓 免费注册：无需信用卡，注册后可终身访问；已有 Master.dev 账号可登录，需邮箱验证。

---

### [Preact 11 – Preact](https://preactjs.com/blog/preact-11/)

**原文标题**: [Preact 11 – Preact](https://preactjs.com/blog/preact-11/)

Preact 11 正式发布：它是基于 Preact X 稳定性与可靠性的增量更新，带来 Hydration 2.0、自动 ref 转发、hook 参数使用 Object.is 相等性检查等新特性；团队借此打包多年积累的破坏性变更，面向现代 Web 并提升后续支持效率。

- 📅 文章日期为 2026 年 9 月 29 日，由 Preact 团队发布。
- 🚀 Preact 11 发布，作为 Preact X 之后的新主要版本。
- 🆕 新功能包括 Hydration 2.0、自动 ref 转发，以及 hook 参数中的 Object.is 相等性检查。
- 🕰️ “Road to Preact 11” 议题始于六年多前，Preact X 的生命周期被大幅延长。
- 🧹 团队决定整合多年考虑的破坏性变更，发布新主版本，以支持现代 Web、清理未成熟功能并更高效地服务用户。
- 📘 升级指南包含迁移所需全部信息，包括新特性和支持的浏览器版本。
- ⚡ 多数用户升级应较直接快速，主要变化多与类型相关；类型更严格，并从更合适的位置导出。
- 📦 @preact/signals、preact-render-to-string、preact-iso、prefresh、@preact/preset-vite 等官方包自预发布起已支持 Preact 11，依赖很可能已兼容。
- 🙏 团队感谢多年来为 Preact 及其生态做出贡献的所有人。

---

### [](https://github.com/preactjs/preact/issues/2621)

**原文标题**: [The road to Preact 11 · Issue #2621 · preactjs/preact · GitHub](https://github.com/preactjs/preact/issues/2621)

Preact 11 的路线图讨论（GitHub issue #2621）回顾了 Preact X/10.x 在生态兼容性上的成功，并提出下一代框架的多个探索方向；这些内容只是想法集合，并非最终功能清单。

- 🧭 Preact X/10.x 成果：提升生态兼容性，新增 Fragments、hooks、重做 DevTools、prefresh 原生 HMR 等。
- 📦 体积优化：当前体积已接近 4kB，希望 Preact 11 继续缩小，核心理念是“只包含实际用到的功能”。
- 🌳 按需包含：许多项目不使用 class 组件，preact/compat 也可能只用 Portal，因此不应为未使用功能付出成本。
- 🎨 将 IS_NON_DIMENSIONAL 移到 compat：该属性列表在核心中持续增长，且容易让开发者混淆；因 React 兼容不能完全移除，但可移出核心。
- ⚙️ 协调器性能：下一代应完全基于 vnode 树，不再依赖 DOM 遍历，以解决 Fragments 等带来的复杂问题。
- 🚀 潜在优化：为单子元素和挂载添加快速路径，并将 DOM 操作放入 effect 队列以集中批量绘制。
- 🖌️ effect 队列还可能简化 DOM 指针代码，并长远为自定义渲染器打开可能性。
- 💧 水合优化：协调器优化会直接惠及 hydration；需重新评估 SSR 内容启动方式，尤其是相邻文本节点不合并导致的不匹配，可考虑 HTML 注释标记。
- 🔗 移除 forwardRef 需求：提案将 ref 保留在 props 中，使 forwardRef 组件冗余；但可能受第三方库运行时属性检查影响。
- 🌲 将根节点标记为 root：让 DevTools 和 Portal 更好地处理子树，减少 Portal 边缘情况；未来甚至可能实现渲染器切换。
- 🧪 其他说明：以上只是 Preact 11 的想法集合，不是确定功能集，整体工作量可能持续数月。

---

### [从 Preact 10.x 升级 – Preact 指南 v11](https://preactjs.com/guide/v11/upgrade-guide/)

**原文标题**: [Upgrading from Preact 10.x – Preact Guide v11](https://preactjs.com/guide/v11/upgrade-guide/)

Preact 11 是 Preact 10.x 的少量破坏性升级，目标是提高浏览器与 TypeScript 支持版本、移除遗留代码，并让大多数应用顺利迁移；同时引入 Hydration 2.0、默认 ref 转发、Object.is 等更新。

- 🌐 浏览器支持：Chrome ≥71、Safari ≥12.1、Firefox ≥69、Edge ≥79；更旧版本需使用 polyfill。
- 🧾 TypeScript 最低版本为 v5.1，升级 Preact 前需先升级 TS。
- 📦 仅以 ESM 发布核心与附加包，使用 `.mjs`；移除 `.module.js`、CommonJS 和 UMD bundle。支持 `require(esm)` 的运行时仍可 `require('preact')`，其他 CJS/UMD/直接 dist 导入应改用 ESM 或 ESM CDN；`preact/compat/server` 等仍提供 CJS 包装。
- 💧 Hydration 2.0：异步边界现在可返回 0 个或 2+ 个 DOM 节点，并与流式 SSR 输出协调，通过稳定注释标记恢复水合。
- ⚖️ Hook 参数相等性检查改用 `Object.is`，更贴近 React，并支持 `NaN` 作为状态或依赖值。
- 🔁 refs 默认转发，无需 `forwardRef`；纯 Preact 下也会转发到 class 组件，`preact/compat` 下 class 组件不转发；可用 `options.vnode` 恢复旧行为。
- ⚛️ React 兼容层新增：`use()`、`useEffectEvent()`、`useSyncExternalStore()` 的 `getServerSnapshot`、`Children.map/forEach` 的 context 参数；`preact/debug` 新增 `captureOwnerStack()` 和 `setupComponentStack()`。
- 🌀 `createPortal` 进入核心，可直接从 `preact` 导入，同时也继续从 `preact/compat` 导出。
- 🎨 数值 style 自动添加 `px` 与 `defaultProps` 支持移入 `preact/compat`。
- 🧹 `render()` 的第三个 `replaceNode` 参数被移除；需要时使用 `preact-root-fragment` 的 `createRootFragment`。
- 🧍 `Component.base` 属性被移除；可用 `this.__v.__e` 访问关联 DOM。
- ⏳ `preact/compat` 移除 `SuspenseList`。
- 🕒 `useEffect` cleanup 在卸载后延迟到浏览器绘制后执行，与 React 一致；需要同步清理时改用 `useLayoutEffect`。
- 🏷️ `useRef` 类型要求初始值；`RefObject<T>` 的 `current` 为 `T`，必要时写成 `RefObject<HTMLElement | null>`。
- 📛 `JSX` 命名空间缩减，仅保留 TS 必需类型，其余类型移到 `preact` 命名空间。

---

### [Nuxt 4.6 · Nuxt 博客](https://nuxt.com/blog/v4-6)

**原文标题**: [Nuxt 4.6 · Nuxt Blog](https://nuxt.com/blog/v4-6)

Nuxt 4.6 于 2026 年 10 月 5 日发布，是迄今最大的小版本之一，包含 420+ 次提交；随附 Nuxt CLI v4，核心是迈向服务器无关架构，并带来 `nuxt/server`、会话、重建类型化 `$fetch`、Vue Vapor、开发错误页与大量性能提升。

- 🚀 Nuxt 4.6 与 Nuxt CLI v4 同步发布，升级 `nuxt` 即自动获得新 CLI。
- 🖥️ Nuxt CLI v4 的 `nuxt dev` 提供交互面板、URL、启动进度和 `r/o/l/n/p` 快捷键，并支持 `--no-tui` 经典输出。
- 🔎 每个请求都有 id，日志和错误可归因；开发服务器会说明重载原因、配置变更、启动耗时和模块初始化耗时。
- 🔒 `.nuxt/` 锁文件让第二个 `nuxt dev` 接管或让位，并支持 `nuxt curl`、`nuxt task`、`nuxt docs`、`nuxt preview --takeover`。
- 📦 Nuxt CLI v4 更小更快：安装体积 -73%、依赖 -56%、首次绘制快 6.6 倍、端口绑定快 3.2 倍、内存 -30%；要求 Node.js 22.21+/24.11+/26+，移除 `nuxt init`，不再支持 Nuxt 2 与 Bridge。
- 🌐 最大变化是服务器无关：Nuxt 定义公共 API、自有 `RequestEvent`、route rules 和类型化 `$fetch`，并新增 `nuxt/server` 导入面。
- 🧩 `nuxt/server` 提供 `defineEventHandler`、`createError`、URL/headers/query/body/cookies/redirect、`getRouterParam`、`getRequestIP`、`handleCors`、`getRouteRules`、runtimeConfig、appConfig 与 sessions；仍可继续从 h3/nitropack/runtime 导入。
- ⚠️ 混用自动导入的 h3 helper 与 `nuxt/server` 会报 `NUXT_E8012`；`sendRedirect`、`createError`、`event.res.headers` 等行为与 h3 v1 略有不同。
- 🏗️ 底层仍默认 Nitro；实验性 `@nuxt/vite-server` 允许纯 Vite 服务器构建，但缺少 Nitro 的 storage、缓存、任务、服务器插件等完整功能。
- ☠️ Nuxt 3 已于 2026 年 7 月 31 日结束生命周期，因此没有 3.x 并行版本。
- 🔐 新增 `runtimeConfig.appSecret`（`NUXT_APP_SECRET`），模块可用 `deriveSecret` 派生密钥；开发环境自动生成并持久化，构建不会生成。
- 🍪 新增基于 iron 的密封 cookie sessions，无需服务端存储；用 `useSession` 读写并更新会话。
- 🎯 类型化 `$fetch` 基于 `fetchdts` 重建，解决数百/数千路由下的 TS2589 深度实例化错误，并大幅降低类型检查时间和内存。
- ✅ 类型化 `$fetch` 还能根据处理器验证的 body、query、headers 检查调用；Nuxt 4 需 `experimental.routeTypedFetch`，Nuxt 5 默认启用。
- 🐛 开发错误改进：SSR 堆栈映射到源码、`my-bad` 覆盖层与代码框、Copy error、终端报告；CLI v4 统一错误通道可承受 worker 重启。
- 🎨 新 WebGL2 粒子加载屏、404/错误页中性配色与返回按钮；`experimental.prerenderErrorPages` 可预渲染真实错误 HTML。
- ⚡ Vue Vapor 互操作模式支持 Vue 3.6 Vapor：`vue.vapor` 开启，组件/页面可用 `<script setup vapor>`，路由、`useAsyncData`、layouts 大多无需改动。
- 🔮 大部分 Nuxt 5 特性已通过 `future.compatibilityVersion: 5` 提供，包括 typed pages、typed `$fetch`、大小写敏感路由、`navigateToEarlyReturn`、`inlineErrorRendering` 等。
- 🧪 `server.builder: 'vite'` 可选择 `@nuxt/vite-server`，支持 SPA、SSR Node 入口、Web fetch handler 和静态生成；默认仍是 Nitro。
- 🚀 性能提升显著：`@nuxt/kit` 安装体积 -67%、依赖 -39%、构建快 11%–18%、SSR 300 个 `NuxtLink` 吞吐 +26%，内部链接服务端渲染为纯 `<a>`。
- 🧠 模板现在声明失效来源；编辑组件不再重生成全部模板；`useCookie` 每请求只解析一次 cookie header。
- 📉 更轻 payload：`useFetch`/`useAsyncData` 支持 `serialize:false`，`stripNeverHydratedData` 自动剥离；开发环境警告 >100 kB payload 和 noScripts 页面依赖 JS。
- 🧩 `useFetch`/`useAsyncData` 新增 addons 工厂能力，可封装 refreshOnFocus、轮询、重试等自定义逻辑。
- 🛠️ 开发者体验：终端文件路径可点击、组件 hover 显示文档、顶层 `prerender`、public 文件链接回退、组件重命名刷新、layers 预打包、tsconfig 改进等。
- 🧰 模块作者：`addServerHandler` 支持按服务器 API 选择变体，兼容 Nuxt 4/5；新增 `getNitroVersion`、`ServerTypes`、`useTerminal`、module hooks、`onConfigResolved` 等。
- 🩹 修复与安全：`useRequestFetch` 转发请求头、视图过渡修复、自动导入重扫、错误 cause 保留、内部错误路由限制、开发错误报告作用域化。
- ⬆️ 升级建议运行 `npx nuxt upgrade --dedupe`；需 Node.js `^22.22.3 || ^24.15.0 || >=26.0.0`，服务器代码可参考迁移到 `nuxt/server`。

---

### [](https://github.com/nuxt/cli/releases/tag/v4.0.0)

**原文标题**: [Release v4.0.0 · nuxt/cli · GitHub](https://github.com/nuxt/cli/releases/tag/v4.0.0)

Nuxt CLI v4.0.0 正式发布，随 Nuxt 4.6 带来性能、功能与开发体验升级，重点优化 `nuxt dev` 启动速度、错误展示、交互式终端和请求追踪，同时大幅缩小安装体积。

- 🚀 v4.0.0 是下一个大版本，伴随 Nuxt 4.6 发布，包含 200+ 提交，聚焦性能、功能和 DX。
- 🐞 开发时错误改用 `my-bad` 渲染，替代 `youch`，可显示源码映射代码框、调用栈、Vue 组件追踪、请求环境与服务器日志。
- 🌐 新增实时错误通道 `/__nuxt_dev__/error`，即使 Nuxt 未启动或配置语法错误，也能在浏览器显示错误页并自动重载。
- 🖥️ `nuxt dev` 新增交互式终端 UI，底部固定面板显示 URL、启动进度、状态和快捷键。
- ⌨️ 支持单键操作，如 `r` 重启、`o` 打开浏览器、`y` 复制 URL、`i` 查看信息、`l/e` 浏览日志、`n` 浏览请求、`p` 浏览页面、`?` 查看快捷键、`q` 退出。
- 🔍 每个请求带 ID，可追踪中间件、插件、钩子、数据获取、渲染、Vite 编译耗时和请求日志。
- 🧩 新增模块终端原语：`withTerminal()`、`startTask()`、`notify()`，方便模块适配新 UI。
- ⚡ 启动更快：端口在配置加载前绑定，面板优先绘制，首次绘制从 330ms 降至 50ms，端口绑定从 338ms 降至 104ms。
- 📦 体积更小：`@nuxt/cli` 依赖从 70 个降至 31 个，安装体积从 13.1MB 降至 3.5MB；全局 `nuxi` 从 6.0MB 降至 0.8MB。
- 📉 其他性能数据：`nuxt --help` 108ms→73ms，全局 `nuxi --help` 88ms→49ms，首屏服务 3.2s→2.6s，Linux 静息内存 630MB→440MB。
- 🤖 对 Agent 更友好：运行中服务器记录到 `.nuxt/` 锁文件，避免端口竞争，支持接管已有服务器，并可用 `--takeover` 强制接管。
- 🧰 新增命令：`nuxt curl`、`nuxt task list`、`nuxt task run`，无需知道端口即可访问运行中服务器。
- 📚 新增 `nuxt docs`，可在终端搜索与项目 Nuxt 版本匹配的官方文档并打开最佳结果。
- 🛡️ 安全增强：固定并校验 `cloudflared` 下载、内部端点拒绝未知 Host、`GITHUB_TOKEN` 仅发往 GitHub、模板不能写出项目外。
- ⚠️ 破坏性变更：要求 Node.js v22.21+、v24.11+ 或 v26+，不再支持 Nuxt 2 和 `@nuxt/bridge`，`nuxt init` 移出 CLI。
- 🧭 全局 `nuxi` 仅转交给 v3.26+ 的项目 `@nuxt/cli`，更旧锁文件项目会使用全局命令。
- 🖱️ 默认在交互终端启用 TUI，CI 或脚本不受影响，可用 `--no-tui` 或 `NUXT_TUI=plain` 恢复传统输出。
- ⬆️ 升级方式：推荐 `npx nuxt upgrade --dedupe`；想提前试用 CLI v4，可通过覆盖 `@nuxt/cli` 为 `^4.0.0` 实现。

---

### [@sindresorhus.com 在 Bluesky 上](https://bsky.app/profile/sindresorhus.com/post/3mwtgzhv7uk2t)

**原文标题**: [@sindresorhus.com on Bluesky](https://bsky.app/profile/sindresorhus.com/post/3mwtgzhv7uk2t)

Sindre Sorhus 宣布，由于 AI，他已禁用所有仓库的外部拉取请求；他认为传统开源时代已经结束，但仍会继续维护项目和处理问题。

- 🤖 原因：由于 AI 的影响，他决定关闭所有仓库的外部 PR
- 🚫 措施：所有仓库已禁用外部 pull requests
- 🕰️ 感慨：开源如我们熟知的样子曾很有趣，而这段经历对他已持续 15 年
- 🛠️ 承诺：仍会继续维护项目，并处理 issues
- 📅 时间：帖子发布于 2026-10-01T18:04:24.059Z
- 🌐 来源：Sindre Sorhus 在 Bluesky 上的帖子

---

### [](https://github.com/swc-project/swc/pull/12463)

**原文标题**: [feat(ci): restrict pull requests to trusted contributors by kdy1 · Pull Request #12463 · swc-project/swc · GitHub](https://github.com/swc-project/swc/pull/12463)

SWC 通过 PR #12463 引入“仅允许受信任贡献者提交 PR”的 CI 策略，并配套 CI 门禁；随后 #12467 和 #12482 分别补充现有贡献者与 TSRX 贡献者白名单，最终策略已于 2026 年 10 月 2 日合并。

- 🔐 **#12463 核心变更**：新增 YAML 策略，仅允许 GitHub 机器人、拥有 write/maintain/admin 权限的仓库用户、以及白名单分组中的用户名提交 PR 并运行 CI；其他作者收到一次英文通知后 PR 被关闭。
- 👥 **白名单分组**：按大小写不敏感管理 `individuals`、`nextjs`（含 Turbopack）和 `rspack` 组；初始列表为空，由维护者填充。
- 🧩 **触发与执行**：通过序列化的 `pull_request_target` 工作流，在 `opened`、`reopened`、`synchronize` 时检查作者；策略代码和配置从默认分支读取，配置或 API 错误会使检查失败但不关闭 PR。
- 🚦 **CI 门禁**：CI、Benchmark、Binary Size、GitHub Actions Security 受共享 `allowed` 输出控制；被拒绝作者或策略失败无法获得成功的 CI `Done` 结果；push、merge queue 和手动运行绕过作者限制。
- 📚 **文档与流程**：记录贡献者策略，以及添加用户名和重新打开 PR 的流程。
- 🧪 **#12463 验证**：初始化子模块；`cargo fmt --all` 与 `cargo clippy --all --all-targets -- -D warnings` 通过；79 个贡献者策略测试和 25 个现有 GitHub 脚本测试通过；本地 actionlint、pinact、zizmor 检查通过。
- 🚀 **#12463 发布顺序**：策略与 CI 门禁为两个独立提交；需先将 `cb449192c0`（action、配置、自动关闭工作流）应用到默认分支，再应用 `8bb6a3abe9`（CI 门禁）；在 action 可用前，bootstrap PR 的策略任务无法成功。
- ⚠️ **仓库设置与版本**：在把仓库 `collaborators_only` 设置改为 `all` 前，需先填充并验证外部用户名；此 PR 未更改该设置；未修改 Rust crate，无需版本发布。
- 🤖 **机器人反馈**：changeset-bot 提示未找到 changeset，合并不会导致包版本升级；Codex 的代码审查与安全审查均已完成。
- ✅ **合并结果**：PR #12463 由 kdy1 合并为 `ee297d6`，29 项检查中 24 项通过，删除分支并加入 Planned 里程碑。
- 📝 **#12467 后续**：填充白名单，加入 26 个现有 SWC 贡献者：20 个到 `individuals`、3 个到 `nextjs`、3 个到 `rspack`；包含 `hardfist`，因其 triage 权限不符合 writer 豁免。
- 🔍 **#12467 验证**：仅修改 `.github/contributors.yml`；Node.js 24 下 79 个策略测试通过；确认配置恰好包含 26 个账号且无重复；52 个原始大小写/大写作者检查通过；`cargo fmt`、`cargo clippy`、`git diff --check` 通过。
- 🧩 **#12482 后续**：将 `trueadm` 加入专用 `tsrx` 组，使 TSRX PR 和 CI 被策略接受；该账号由 TSRX 介绍提交 `61ff097706` 和已合并 PR #12120 确认。
- 🧪 **#12482 验证**：扩展测试夹具，验证 `trueadm` 与 `TRUEADM` 在 `tsrx` 组无需权限查询即可通过，并断言白名单包含该账号；Node.js 24 下 89 个测试全部通过；`cargo fmt`、`cargo clippy`、`git diff --check` 通过。

---

### [JavaScript 框架基准测试 · 官方结果](https://krausest.github.io/js-framework-benchmark/)

**原文标题**: [JavaScript Framework Benchmark · Official Results](https://krausest.github.io/js-framework-benchmark/)

overview summary
- 🌐 开源、可复现、社区驱动的 JavaScript 框架性能基准，用于衡量框架处理常见 UI 操作的表现。
- ⚡ 比较渲染速度、内存占用和启动成本，并基于官方 benchmark 结果。
- 📊 最新官方发布为 Chrome 154，是探索结果的推荐起点。
- 🧪 开发快照预览可能混合不同浏览器版本与运行次数，解读时需谨慎。
- 🧭 阅读结果要结合上下文，并参考 benchmark 文档与测量说明。
- 🖥️ CPU 性能：创建、更新、选择、删除表格行的耗时，包含浏览器渲染工作；持续时间越低越快。
- 🧠 内存使用：页面加载及重复表格操作后的内存；数值越低，测得任务的内存足迹越小。
- 🚀 启动与体积：加载和启动测量因版本而异；比较时间或传输大小时需核对报告描述与单位。
- ⚖️ 应在同一发布版本内比较；浏览器版本、CPU 限流和测量方法会随时间变化。
- 📐 自 Chrome 118 起，总体结果采用加权几何平均；可查看持续时间如何测量。
- 🔑 Keyed 与非 keyed 实现处理 DOM identity 的方式不同，应选择适合自身应用的模式；表格操作只是框架选型的一部分。
- 🗂️ 官方结果归档收录所有发布：2026 年 7 个、2025 年 12 个、2024 年 12 个、2023 年 12 个、2022 年 13 个、2021 年 9 个、2020 年 5 个，以及更早 4 个。
- 🔗 更早结果托管在 Stefan Krause 网站；项目在开放环境中构建，可探索源码、添加框架或改进 benchmark，并在 GitHub 贡献。

---

### [JavaScript 框架基准测试 — 交互式结果](https://krausest.github.io/js-framework-benchmark/2026/chrome154.html)

**原文标题**: [JavaScript Framework Benchmark — Interactive Results](https://krausest.github.io/js-framework-benchmark/2026/chrome154.html)

该页面是 JavaScript 框架基准测试，提供交互式结果查看与官方存档指引。

- 🧪 主题为 JavaScript 框架基准测试
- ⚙️ 需启用 JavaScript 才能筛选和比较交互式结果
- 📊 可访问官方结果存档，查看基准测试版本与方法论

---

### [](https://github.blog/changelog/2026-10-02-npm-staged-publishing-now-supports-creating-new-packages/)

**原文标题**: [npm staged publishing now supports creating new packages - GitHub Changelog](https://github.blog/changelog/2026-10-02-npm-staged-publishing-now-supports-creating-new-packages/)

npm staged publishing 现在支持创建新包：可通过 `npm stage publish` 搭配本地会话或细粒度访问令牌（包括仅限 stage 的令牌）创建包，让自动化工作流无需手动首次发布即可完成创建。该功能适用于公开 scoped/unscoped 包和私有 scoped 包；首个版本会进入暂存队列，需维护者提升后才可安装，之后可管理设置并配置可信发布。

- 📅 2026年10月2日，npm 发布此改进。
- 🆕 `npm stage publish` 现在可创建新的 npm 包。
- 🔑 支持本地会话或细粒度访问令牌，包括 stage-only 令牌。
- 🤖 可从自动化工作流创建包，无需手动首次发布。
- 📦 适用于公开 scoped、unscoped 包及私有 scoped 包。
- ⏳ 首个版本进入暂存队列，需维护者 promote 后才可安装。
- ⚙️ 创建后可管理包设置并配置可信发布。
- 📚 可进一步了解 staged publishing，并在 GitHub Community 参与 npm roadmap 讨论。
- 🔒 该更新与供应链安全相关。

---

### [](https://github.com/remix-run/remix/releases/tag/remix%403.0.0)

**原文标题**: [Release remix v3.0.0 · remix-run/remix · GitHub](https://github.com/remix-run/remix/releases/tag/remix%403.0.0)

Remix v3.0.0 正式发布，这是 Remix 3 的首个稳定版本，核心变化是将 UI/组件相关入口从 `remix/ui` 迁移到 `remix/component`，并把无头 UI 原语与动画工具拆分到 `@remix-run/ui`。

- 🚀 `remix@3.0.0` 是 Remix 3 的首个稳定版本，安装和新应用示例已改用稳定版。
- 🔄 破坏性变更：大多数 `remix/ui` 用法迁移到 `remix/component`，包括组件运行时、JSX 运行时、服务端渲染、测试助手、样式和通用 mixins。
- 🛠️ 运行时子路径同步重命名，如 `remix/ui/server`、`remix/ui/test`、`remix/ui/dev/refresh` 改为 `remix/component` 对应路径。
- ⚙️ 使用 Remix JSX 运行时需将 `jsxImportSource` 从 `remix/ui` 改为 `remix/component`。
- 🔥 组件 HMR 入口从 `remix/ui-hmr` 迁移到 `remix/component-hmr`，`uiHmr()` 重命名为 `componentHmr()`；Node hook 也改为 `remix/component-hmr/node`。
- 📦 `remix` 包不再导出 UI 组件、原语或动画工具；这些能力移至 `@remix-run/ui`，该包目前不稳定、独立以 v0.x 版本发布，不属于 Remix 3.0 RC。
- 🎞️ 动画导入改为从 `@remix-run/ui/animation` 引入，如 `animateEntrance`、`spring`。
- 🧩 无头 UI 原语改为扁平子路径导入，如 `@remix-run/ui/accordion`，适用于 accordion、anchor、combobox、listbox、menu、popover、select、tabs、toggle。
- 🗑️ 视觉样式组件和样式 mixins 已移除，包括 `breadcrumbs`、`button`、`checkbox`、`input`、`radio` 等模块。
- 🔐 如果资源服务器用 `allowPackages` 限制导入，需要加入 `@remix-run/ui`，例如 `["@remix-run/ui", "remix"]`。
- 📈 Patch 更新：安装/新应用示例使用稳定版，并批量将 `@remix-run/*` 依赖升级到 1.0.0，包括 `component`、`assets`、`cli`、`test` 等。

---

### [](https://remix.run/blog/remix-3-release-candidate)

**原文标题**: [Remix 3 Release Candidate | Remix](https://remix.run/blog/remix-3-release-candidate)

2026年8月31日，Remix 发布首个 Remix 3 候选版本，距 beta 预览约4个月；功能开发已冻结，计划于10月2日在 Remix Jam 正式发布。Remix 3 是单一依赖的真正全栈 JavaScript 框架，整合数据库、类型安全路由、非打包资产服务器与全新 UI 运行时。

- 🚀 发布首个 Remix 3 RC，正式版将于10月2日在 Remix Jam 推出，门票仍可购买。
- 📦 所有能力集中在单一 `remix` 包：数据库管理、schema 校验、快速类型安全路由、非打包资产服务器、可组合事件/样式/动画/内置组件的 UI 运行时。
- 🌱 开发如种树：先扎根理念与 API，beta 后快速成长；今夏完成350+次提交，修复 bug 并提升稳定性。
- 🗄️ 新增完整数据库工作流：迁移、种子、状态检查、重置、清空、回滚均内置于 CLI。
- ⚡ 支持全栈 HMR；资产服务支持 JS、CSS、图片、字体、npm 包和预加载。
- 🧭 路由匹配与 URL 生成更安全快速，支持 `router.mount()` 组合路由和更强 TypeScript 推断；UI 库新增 tabs、toggles、上下文菜单等。
- 🖥️ SPA 支持复用同一 router、middleware、controllers 和 Request-to-Response 模型；链接与表单导航可更新整页或指定 frame。
- ⚙️ 使用 `remix.json` 配置数据库、资产、测试，并可用 `remix doctor` 和 CLI 检查浏览器可达资产。
- 🤖 作者强调 Remix 适合 agentic programming：基于 Web 原语、类型安全，UI 状态即普通 JavaScript 作用域，人和代理都易理解。
- 🧩 真正全栈且单一依赖，减少 `package.json` 体积和供应链风险；可按需替换 schema、数据表或 render middleware 等部件。
- 📌 RC 结束新功能开发，后续聚焦修 bug、安全审计、文档、早期反馈，并开始遵循 SemVer。
- 🧪 试用：`npx remix@next new my-remix-app`；可查看文档、官网源码、Discord 和 newsletter 获取更新。

---

### [](https://github.com/vadimdemedes/ink/releases/tag/v8.0.0)

**原文标题**: [Release v8.0.0 · vadimdemedes/ink · GitHub](https://github.com/vadimdemedes/ink/releases/tag/v8.0.0)

Ink v8.0.0 发布：这是一次包含破坏性变更、新 API 和大量渲染、文本、输入、焦点及可访问性修复的重大更新，要求 React 19.3+。

- 🚀 v8.0.0 由 sindresorhus 于 10 月 3 日发布，包含 Breaking、New 和 Fixes。
- ⚛️ 破坏性变更：要求 React 19.3+。
- 📏 `<Box>` 的 `minWidth` 和 `maxWidth` 现在只接受数字，不再支持百分比字符串。
- 🔌 `stdin`、`stdout`、`stderr` 改为泛型 Node.js 流类型，`stdout.columns` 等 TTY 属性不再包含在类型中。
- ⌨️ `useInput` 不再接收未识别的终端控制序列，例如鼠标报告、焦点事件、光标位置报告等。
- 🆕 `<Box>` 新增 `contentOffsetX` 和 `contentOffsetY`，配合 `overflow="hidden"` 可构建可滚动视图。
- 📐 `useBoxMetrics()` 和 `measureElement()` 新增 `clientWidth`、`clientHeight`，表示不含边框的内容尺寸。
- 🌊 `render()` 的 `stdin`、`stdout`、`stderr` 可接受任意 Node.js 流，如 `PassThrough`、`Readable`、`Writable`。
- ⚡ `incrementalRendering` 模式会跳过未变化行前缀，只写入变化部分，减少输出和闪烁。
- 🔗 React DevTools 移除 `ws` 依赖，改用原生 `WebSocket`。
- ↩️ 应用键盘区 Enter 现在可识别为 `key.return`。
- 🖥️ 渲染修复：保留滚动回看、清屏后恢复帧、终端行数缩小时保留内容、恢复光标位置等。
- 🧱 `<Static>` 修复：停止全清帧重放、恢复备用屏幕时重放、隐藏祖先输出、空白行、并发渲染等问题。
- 📝 文本修复：多行文本逐行截断、自然宽度、控制字符清理、Tab/CRLF、ANSI 样式跨换行、组合字符、宽字符裁剪。
- ⌨️ 输入修复：旧式键盘修饰键、SS3、Kitty 键盘解析、Ctrl+C 与普通输入同时到达、Meta 键解析、终端挂起时副作用。
- 🎯 焦点修复：共享焦点 ID 视为一个 Tab 停靠点、`disableFocus()` 按文档模糊、自动焦点 ID 防冲突、空字符串可作焦点 ID。
- ♿ 其他修复：屏幕阅读器输出、错误展示、`renderToString()`、`useWindowSize()`、动画暂停重置、文本缓存、Yoga 节点释放。
- 🧭 迁移指南：升级 React 19.3+；宽高用数字计算；TTY 属性改用 `useWindowSize()`；`useInput` 不再解析终端控制序列。

---

### [发布 v10.0.0 · infernojs/inferno · GitHub](https://github.com/infernojs/inferno/releases/tag/v10.0.0)

**原文标题**: [Release v10.0.0 · infernojs/inferno · GitHub](https://github.com/infernojs/inferno/releases/tag/v10.0.0)

InfernoJS v10.0.0 是一次以编译期优化为核心的大版本更新，将子节点形状计算从运行时转移到 JSX 编译器，并重写动画系统、增强路由确认、修复核心、Hydration、SSR、Router、Compat 与 MobX 等大量问题。升级需同步更新所有 `inferno*` 包和 JSX 插件，并重新编译 JSX。

- 🚀 核心变化：运行时工作转移到编译器，JSX 插件把子节点形状写入 vNode flags，减少运行时计算、字段、内存占用和分配。
- 🧩 升级要求：所有 `inferno*` 包升级到 10；Babel/TS/SWC JSX 插件升级到 10；Babel/TS 插件需 Node.js 24+，TS 插件依赖 TypeScript 6。
- ⚠️ 破坏性变更：必须使用 v10 JSX 插件；`VNodeFlags` 值变化；移除 `vNode.childFlags`、`vNode.isValidated`、`$ReCreate`；委托事件存储方式改变。
- 📦 浏览器支持：所有 bundle 面向 Chrome 107、Edge 107、Firefox 84、Safari 16；`Component` 为原生 class，组件需编译到 ES2015+。
- 🛠️ 新工厂：`newVNode`、`newComponentVNode`、`newTextVNode`、`newFragment` 替代旧 `create*` API，旧 API 标记 deprecated 但仍可用。
- 🧭 inferno-router：新增 `getUserConfirmation`，支持自定义页面内导航确认，修复 `Prompt`、`Redirect`、`Switch`、loader 等问题。
- 🎞️ inferno-animation：重写且 API 不变，支持推挤项动画、中断续播、离开项滑入、2D transform、shadow root、SVG viewBox 等。
- ✅ 属性改进：新增 `async`、`defer`、`inert`、`noModule`、`playsInline` 等布尔属性；`autoFocus` 在挂载时生效。
- 🧠 TypeScript：`createElement` 重载更准确；`inferno-compat`、`inferno-extras`、`inferno-mobx`、`inferno-redux` 类型均有改进。
- ⚡ 性能优化：vNode 更小；子 flags 编译期确定；委托事件更省内存；keyed diff 使用 `Map` 减少 GC；vNode 复用、归一化、卸载优化。
- 🐞 核心修复：修复 vNode 多位置共享 DOM/状态、Fragment 单子节点卸载、Portal 容器变更、`dangerouslySetInnerHTML`、`style`、`option` value、`forwardRef` ref 等问题。
- 💧 Hydration/SSR 修复：修复 hydration 误用已挂载 vNode、单子 Fragment、SVG camelCase、server 渲染数组/null、流式渲染、`option selected`、`textarea value` 等问题。
- 🧪 其他修复：Router loader/Redirect/Switch/HashRouter、Compat `PureComponent`/`fontVariant`/原型属性、MobX observer 生命周期与 SSR、Redux UMD 等。
- 👩‍💻 贡献者变更：仓库改用 pnpm；浏览器测试改用 Jasmine Browser Runner；测试全面 TypeScript；增加差分 fuzz 测试。

---

### [](https://next.qwik.dev/blog/qwik-2-rc/)

**原文标题**: [Qwik 2.0 RC: JavaScript streaming without the overhead 📚 Qwik Documentation](https://next.qwik.dev/blog/qwik-2-rc/)

Qwik 团队发布 Qwik 2.0 RC，主打“无额外开销的 JavaScript 流式渲染”：通过移除 v1 的 HTML 注释标记、改用末尾编码状态与内存 VNode，大幅提升反应性、启动性能和流式能力，并加入实验性乱序流、可缓存 loaders 以及大量开发体验与基础设施改进。

- 🚀 Qwik 2.0 RC 目标：在小应用与大规模场景中保持启动性能领先，同时在能力、Agent 体验和整体性能上追平主流框架。
- 🤖 AI 时代 Agent 能快速学习 API 和修 Bug，但无法修复框架低效；若框架强制浏览器下载/运行过多 JS，应用会随复杂度变慢。
- 🧠 v1 引入响应式 JavaScript streaming：服务端把状态和事件监听器写入 HTML，浏览器从该状态恢复，并按交互缓冲预加载 JS，使应用 O(1) 可交互。
- ⚠️ v1 的注释/标记必须按序写入，增加 CPU 与内存开销，导致反应性偏慢且无法乱序流；慢请求会阻塞后续内容。
- 🧹 v2 移除注释，改为 HTML 末尾单个编码字符串，并使用 `qwik/state`、`qwik/vnode`，支持实验性乱序流。
- ⚡ 运行时优化：VNode 保留在内存，信号更新文本/属性时不再解析 HTML；调度器每 15ms 让出主线程，避免长渲染阻塞点击和输入。
- 📊 js-framework-benchmark 加权几何均值：Qwik v2 约 1.23×，略优于 Vue 1.25×，优于 Angular 1.42×、React 1.53×、Qwik v1 2.59×；反应性比 v1 快 2 倍以上。
- 🧩 实验性乱序流：用 `<Pending fallback$>` 边界让服务端先发送其余页面与 fallback，再流式补上慢内容；`<Catch>`、`blockSSR:false` 需在 `vite.config.ts` 开启。
- 🔎 `useComputed$` 支持 async，可替代 `<Resource>`；可取消过期请求，配合 `Pending`/`Catch` 处理加载、错误与重试；导航时 route loaders 不再阻塞渲染。
- 🗂️ `routeLoader$` 拥有独立 JSON 端点，支持 `cacheControl`（如 maxAge、immutable）与 `eTag/304`；`<Link>` 默认视口预取代码、悬停/聚焦预取数据。
- 🛠️ 开发体验：Vite 8/Rolldown、HMR 保留 signal/store、Qwik DevTools、`worker$`、`reactify$`、`useSerializer$`、`*.server.ts`、passive/capture 事件、`404.tsx`/`error.tsx`/`useHttpStatus`、实验性 `<Each>`/`<Show>`。
- 🧪 基础改进：可选 TypeScript optimizer 对齐 Rust 优化器；测试覆盖 SSR/恢复与客户端渲染、Chromium/Firefox/WebKit 及双优化器；修复预加载器、重写响应性、支持 backpatching。
- 🗺️ 2.0 前计划：在更多应用中测试 RC，稳定 `Pending`、`Catch`、`.pending`、`.error`，默认启用 TypeScript optimizer，重写 v2 文档。
- 🧪 试用方式：`pnpm create qwik@rc`；访问 `next.qwik.dev/examples` 或 `/playground/`；用 `pnpm qwik migrate-v2` 处理少量破坏性变更。
- 🙏 致谢贡献者、其他前端项目，以及 Claude/Codex 的开源项目支持。

---

### [pnpm 12.10.0 | pnpm](https://pnpm.io/blog/releases/12.10.0)

**原文标题**: [pnpm 12.10.0 | pnpm](https://pnpm.io/blog/releases/12.10.0)

pnpm 12.10.0 发布，带来实验性 loaded node linker、锁文件解析设置记录、注册表元数据缓存加速，并修复多项安全问题，同时改进安装解析、脚本运行、配置、更新/审计/发布和输出信息。

- 🧪 新增实验性 `nodeLinker: { type: loaded }`，兼容依赖通过自动注册的 Node.js loader 直接从内容寻址存储加载；`nodeLinker.excluded` 可让包及其依赖树安装到全局虚拟存储。
- 🔒 `lockfile.includeResolutionSettings: true` 让 `pnpm-lock.yaml` 记录 `autoDedupe`、`dedupeInjectedDeps`、`dedupePeerDependents`、`linkWorkspacePackages`；记录不同值会被视为过期，记录 `autoDedupe` 的锁文件可跨机器复用，`pnpm run` 不再额外触发安装。
- 🛡️ 安全修复：阻止依赖版本通过路径穿越写出全局虚拟存储；配置依赖必须来自 npm registry，并在安装前按 registry 校验；锁文件 `variations` 中的 tarball 也会校验，空 `variations` 被拒绝。
- 🔐 `pnpm audit signatures` 按锁文件记录的 integrity 验证签名；无 integrity 无法通过。`install`/`publish` 拒绝超过 64 MiB 的归档元数据、manifest 和 README。
- 🧾 修复不同 URL/本地路径依赖共享虚拟存储目录的问题；带 `+`、`#`、`:`、`?` 的路径会生成哈希后缀。忽略 `.npmrc` registry 设置的警告不再泄露用户名和密码。
- 🚫 `install` 对不支持的协议（如 Yarn `patch:`）报 `ERR_PNPM_UNSUPPORTED_PROTOCOL`；依赖 specifier 非字符串时报 `ERR_PNPM_PACKAGE_MANIFEST_INVALID_ATTRIBUTE`。
- 🧩 修复 dangling symlink 导致的 `ERR_PNPM_CMD_SHIM_RESOLVE_PATH`、`--frozen-lockfile` 自定义 fetcher 的 resolution shape mismatch、`--fix-lockfile` 缺失 snapshot，以及 peer 依赖自动安装随精确依赖降级移动等问题。
- ⚡ 注册表元数据缓存读取更快，缓存迁移到 `<cache-dir>/v12/`，首次安装会重新下载；`pnpm cache prune` 也清理旧版 `<cache-dir>/v11/` 元数据。
- ⚡ 元数据请求不再排在 tarball 下载队列后；macOS 大工作区已存在依赖链接时安装加速；固定 pnpm 版本的项目命令启动快约 13 ms；二进制体积减小。
- 🖥️ `pnpm run` 在 Ctrl+C 后不再打印 `[ELIFECYCLE]`；支持 JS 正则 lookahead/lookbehind；转发 `--config.*` 给 `verifyDepsBeforeRun` 安装；Windows 子进程可用 `CREATE_BREAKAWAY_FROM_JOB` 继续运行。
- ⚙️ 空 `nodeOptions` 可覆盖低优先级设置；从 `pnpm-workspace.yaml` 读取 `failIfNoMatch`，新增 `--no-fail-if-no-match`；`config get/list --global` 仅显示全局配置；配置加载失败时打印警告。
- 🔄 修复 pnpm 11 旧版无法运行 pnpm 12、Windows `pnpm self-update` 重复执行、`pnpm setup` 的 PATH 顺序和 shell 配置文件提示等问题。
- 📦 `pnpm update --latest` 应用 `savePrefix`；`pnpm audit --fix` 选择器显示 `saveExact`/`savePrefix` 风格；`pnpm unpublish` 在子路径 registry 下正确删除 tarball。
- 📤 输出改进：`devEngines`/`packageManager` 警告改到 stderr；`pnpm list` 在 `hoisted` 下路径正确；解析错误列出依赖及父包；`--reporter=ndjson` 输出结构化错误；runtime 帮助标明 `set` 子命令。

---

### [Ember 7.3 发布](https://blog.emberjs.com/ember-released-7-3/)

**原文标题**: [Ember 7.3 Released](https://blog.emberjs.com/ember-released-7-3/)

Ember 7.3 于 2026 年 10 月 5 日发布，是标准小版本更新；核心亮点是 tracked 支持类外使用与可配置相等性、Vite/Embroider 应用包体积大幅缩小、8 个 bug 修复，且无新废弃。Ember CLI 7.3 为维护版本，测试脚本直接调用 testem。

- 🚀 发布信息：Ember v7.3 由 Jared Galanis 宣布，按 Ember Release Train 流程发布。
- 🧠 响应式状态：RFC #1071 让 tracked() 可在类外创建独立响应式值，支持 .value、.get、.set、.update、.freeze，适合 helper、modifier、测试和演示。
- 🔒 只读模式：可在类内保留私有 tracked 状态，并只通过 getter 暴露只读视图，例如 Session.user。
- ⚖️ 可配置相等性：两种 tracked 都接受 equals；函数形式默认使用 Object.is，相同值写入不再重渲染；装饰器默认保持 always-notify，可选择性启用相等性判断。
- 📦 包体积：ember-source 设置 sideEffects: false 并重构内部，Vite/Rollup 可摇树；hello-world 压缩 JS 从约 64.5 kB 降至约 37 kB，约缩小 42%。仅影响 ESM/Vite/Embroider，经典 ember-cli 不受影响。
- 🐛 8 个修复：包括 @model 在 willDestroy 中错误或 undefined、动态 modifier 销毁内存泄漏、查询参数不必要刷新与重定向问题、LinkTo 的 nullish @query、CoreObject#init、{{component}} 断言、{{debugger}} 消息改进。
- 🔐 安全加固：set() 路径防护扩展至 prototype，关闭原型污染边缘情况。
- 📚 文档：{{each}}/{{each-in}} 文档补充支持原生 Set/Map；修复 Ember.Templates.helpers 链接。
- 🛠️ Ember CLI 7.3：仅维护性依赖更新，无新功能、废弃或修复；新应用仍使用 WarpDrive 5.8。
- 🧪 测试变化：新蓝图 pnpm test 改为 vite build --mode development && testem ci --port 0，并在 testem.cjs 中设置 cwd: 'dist'；现有应用无需改动。
- 🙏 致谢：文章由 AI 协助起草、人工审核；Ember 感谢社区贡献者的持续支持。

---

### [](https://videojs.org/blog/videojs-10)

**原文标题**: [Video.js v10 is GA — let the migrations begin! | Video.js | Open Source Video Player](https://videojs.org/blog/videojs-10)

概述总结
- 🚀 Video.js v10.0.0 于 2026 年 10 月 1 日正式 GA，结束 Beta/RC 阶段，稳定版可投入生产。
- 🧱 v10 是底层重建，汇集 Video.js、Plyr、Vidstack、Media Chrome 和 Mux Player 的经验与贡献者。
- 📦 默认包体积较 v8 减少约 60%，可组合架构让你只打包真正使用的功能。
- ⚛️ 提供 React 一等组件、原生 HTML Web Components、TypeScript 与 Tailwind 支持，状态、UI 和媒体解耦。
- 🎨 默认皮肤设计更完善，并可通过 Shadcn CLI 将皮肤源码加入项目，自由修改布局、控件和样式。
- 🤖 面向编码代理优化，发布官方 Video.js skill，可用 `npx @videojs/cli agents skills` 安装。
- 🌐 支持 HLS、DASH、YouTube、Vimeo、Mux 和 Cloudflare Stream 等多种源与服务。
- 🧭 文档与安装流程重新设计，并提供从 Video.js v8、Mux Player、Media Chrome、Vidstack 迁移的指南。
- 🧩 GA 新增标题显示、章节展示改进，以及 Compat 皮肤，浏览器兼容回溯至 Safari 16。
- ⚙️ SPF 新流媒体引擎带来显著体积节省，但暂不支持广告或真正低延迟直播；这些场景可用 HlsJsVideo。
- 📦 v10 以 `@videojs/react` 和 `@videojs/html` 发布；npm 上的 `video.js` 包目前仍是 v8。
- 🆓 仍为 Apache 2.0 免费开源；作者邀请用户试用、迁移并反馈体验。

---

### [](https://eslint.org/blog/2026/10/eslint-v10.12.0-released/)

**原文标题**: [ESLint v10.12.0 released - ESLint - Pluggable JavaScript Linter](https://eslint.org/blog/2026/10/eslint-v10.12.0-released/)

ESLint v10.12.0 于 2026 年 10 月 2 日发布，属于小版本升级，新增部分功能并修复了上一版本中的多个缺陷，重点改进了 `SourceCode` 对 token 与 comment 的支持，并修复了一批规则在边界情况下的问题。

- 📅 **发布信息**：ESLint v10.12.0 为小版本升级，发布于 2026 年 10 月 2 日，归类于 Release Notes。
- 🔧 **核心亮点**：`SourceCode` 的 `getText()`、`getLoc()`、`getRange()` 现在正式支持传入 token 和 comment，文档与类型定义已同步修正，与实际行为及 `SourceCodeBase` 接口保持一致。
- ⚠️ **潜在影响**：普通调用代码不受影响，但实现或模拟 `SourceCode` 的 TypeScript 代码可能需要更新上述方法的签名。
- 🐛 **规则修复范围**：`consistent-return`、`max-lines-per-function`、`new-cap`、`no-eval`、`no-invalid-this`、`no-loss-of-precision`、`prefer-arrow-callback`、`prefer-exponentiation-operator` 等规则在边界情况下得到修正。
- ✨ **新增特性**：`new-cap` 支持处理星光平面字符（astral letters）；`SourceCode#getText()` 允许接受 token 与 comment。
- 🩹 **典型 Bug 修复**：修复 `prefer-arrow-callback` 在条件测试中的误报、`max-lines-per-function` 多注释行被跳过、`prefer-exponentiation-operator` 对 async 函数基底的自动修复、`curly` 自动修复中 `else` 后缺失空格、`no-loss-of-precision` 对 `0.e5` 的误报，以及 `getFunctionHeadLoc` 对 `TSFunctionType` 的支持等。
- 📚 **文档更新**：更新 README，澄清 `one-var` 的 `separateRequires` 匹配任意 `require()` 调用，修正 `no-unused-expressions` 文档中的拼写错误。
- 🧹 **维护与性能**：更新生态插件与依赖（prettier、eslint-plugin-expect-type、codeql-action 等），按 languageOptions 缓存归一化配置全局变量以提升性能，CI 调整 Nx 缓存策略。
- 📝 **其他变更**：移除 `CLAUDE.md`，改用 `AGENTS.md`。
- 👥 **主要贡献者**：Francesco Trotta（ESLint 技术指导委员会）等社区成员参与贡献。

---

### [](https://claude.dev/blog/getting-started-with-claude-code-mods/)

**原文标题**: [Getting started with Claude Code mods / claude.dev Blog](https://claude.dev/blog/getting-started-with-claude-code-mods/)

Claude Code mods 是运行在会话内的小型 JavaScript/TypeScript 文件，可通过 hooks 观察、改写或扩展 Claude Code，并绘制终端或桌面 UI；教程从零构建约 80 行的 Token Weather，并展示 Blast Radius、Replay Theater、分享方式与最佳实践。

- 🧩 mod 是 Claude Code 插件的模块，能监控事件、改变行为或绘制自定义界面。
- ⚡ 无需先学 API：运行 `claude`，描述想要的 mod，并允许热重载即可开始。
- 🔗 mod 本质是 hooks，事件如 `tool.call`、`turn.complete`、`session.start`、`ui.render` 都会进入链式处理。
- 🎛️ hook 可采取三种动作：观察、改写事件，或直接拒绝/回答而不调用 `next`。
- 🧱 与 settings hooks 不同，mod 加载一次并留在会话中，可保存状态、绘制动态 UI、注册命令和工具。
- 🛠️ Claude Code 自身也用 mod 实现部分功能，例如 AGENTS.md 支持和 `/diff` 面板，源码在公开仓库。
- 🌦️ 教程项目 Token Weather 在提示上方显示上下文窗口占用：天气图标、百分比、token 数、迷你图和上轮增量。
- 📁 构建步骤包括创建插件目录、`plugin.json`、`hooks/hooks.json` 和导出 `register(on)` 的模块。
- 🖥️ 第一个目标是 `AbovePrompt` 组件，通过 `ui.render` 返回 `Box`、`Text` 等元素。
- 📊 使用 `$.session.usage()` 读取真实上下文数据；历史状态应放入 `$.state`，以在热重载后保留。
- 📝 状态需要在类型契约中声明，如 `types/index.d.ts`，否则 `claude plugin validate` 会报错。
- 📈 绘制时注意 `e.props`、`hasSurvey`、`bodyColumns`，并用单宽符号保证终端字体对齐。
- ✅ 用 `claude plugin validate` 检查插件，用 `claude plugin test` 在真实运行时中测试 hooks 和 UI。
- 📦 mod 通过插件市场分享，可用 `/plugin marketplace add`、`/plugin install`、`/reload-plugins` 安装。
- 🔒 mod 运行在本机并拥有 Claude Code 同等权限，因此应只安装可信来源，并先阅读仓库。
- 💥 Blast Radius 示例拦截危险 Bash 命令，预览影响并提供 Proceed/Cancel，必要时降级到提示上方显示。
- 🎬 Replay Theater 示例记录 Edit/Write，回合结束后通过 `/replay` 或快捷键逐步查看 diff。
- 🧠 四个习惯：依赖自动生成类型、从 `e.props` 读属性、热重载状态放 `$.state`、UI 不显示时用 `claude --debug` 查日志。
- 💡 可继续做成本/速率表、团队规范提示注入、文件阅读地图、专注计时器、kubectl/terraform 防护等 mod。

---

### [](https://claude.com/resources/articles/claude-code-mods)

**原文标题**: [Customize Claude Code with mods in TypeScript | Claude by Anthropic](https://claude.com/resources/articles/claude-code-mods)

2026年10月1日，Claude Code 推出 mods：用少量 TypeScript 函数改变其行为与外观，可重写提示、添加界面、替换内置功能或新增能力；mods 随插件分发，支持 CLI 和桌面端，但不受沙箱保护，只应安装可信来源。

- 🧩 mods 是小型 TypeScript 函数，可改变 Claude Code 的工作方式与外观。
- 🛠️ 可重写提示、添加 UI、替换内置功能或新增功能；可自己编写，也可让 Claude Code 代写。
- 📦 mods 随插件分发，安装和分享方式与普通插件相同，适用于 CLI 和桌面应用。
- ⚠️ mods 拥有与 Claude Code 相同的机器访问权限，不受沙箱隔离，只应从可信来源安装。
- 🎯 推出原因：开发者希望无需等待官方发版就能控制 Claude Code；hooks 能力有限，mods 可重写事件、绘制 UI、替换功能。
- ⚙️ 工作机制：Claude Code 每次操作会发出事件，mod 可在事件前、后、替代或包裹事件执行。
- ✍️ 单个 mod 可改写提示、阻止/重写/重试工具调用、批准/拒绝权限请求、在 Claude 读取前对工具输出脱敏。
- 🖥️ 可编辑或替换界面元素，如工具结果、Claude 提问，添加按钮和输入，其他 mod 可响应；可针对终端、桌面端或两者。
- 🔗 多个 mod 钩同一事件时按加载顺序运行；先加载者先见事件、最后见结果，因此可叠加不同作者的 mod。
- 🔁 可用 Claude Code 给 Claude Code 写 mod：生成 TypeScript、安装并在会话中热重载。
- 🧱 部分内置功能已改为 mod，如 /diff 可关闭或替换；未来更多内置功能会转为 mod，便于精简核心并按需添加。
- 🏢 团队/企业：mods 随插件受现有插件管控；管理员可允许或阻止市场；Team/Enterprise 或受管设置机器会先加载 sec-default 限制风险 mod，管理员可自定义加载顺序但应加入 sec-default。
- 📊 团队用例包括：CI/CD 状态面板、生产环境操作确认、审计日志记录所有 mod 调用。
- 🚀 现已在 CLI 和桌面端可用；可从 Claude 目录或 /plugin 安装含 mod 的插件；通过插件打包并提交目录分享；可阅读入门指南和文档。

---

### [](https://dbushell.com/2026/10/03/deno-to-node/)

**原文标题**: [Friendship ended with Deno, now Node is my best friend â David Bushell â Web Dev (UK)](https://dbushell.com/2026/10/03/deno-to-node/)

作者宣布从 Deno 回归 Node，因为 Node 近年大幅现代化，而 Deno 停滞且问题频发；文章分享了包管理、TypeScript、网站迁移和最终卸载 Deno 的经历。

- 🔄 作者结束与 Deno 的长期关系，重新把 Node 当作主力运行时，并在 SvelteKit 客户端项目中大量使用。
- 🚀 Node 进步明显：支持现代 ECMAScript 语法与 API，终于不用再看到 require()。
- ⚠️ Oracle 商标纠纷看起来不会有积极结果。
- 📦 包管理改用 FNM 切换 Node 版本，并选 PNPM 避免恶意包；还设置 alias npm=pnpm、npx=pnpx。
- 🛡️ 在 pnpm-workspace.yaml 中设置 minimumReleaseAge: 1440 和 trustPolicy: no-downgrade；曾设一个月但依赖匹配困难，最终改为一天。
- 🧾 Node 能直接运行 TypeScript，但拒绝处理 node_modules 下的类型剥离，报 ERR_UNSUPPORTED_NODE_MODULES_TYPE_STRIPPING；作者用 Tsdown 打包。
- 🏠 因 GitHub 被破坏，作者自托管 Forgejo；NPM 限制让包失去 provenance，需要配置 PNPM trust policy 放行自己的包。
- 🌐 把静态站点生成器从 Deno 迁到 Node v26.10.0，改动很少：Deno 文件系统 API 换 node:fs，Deno.serve 换 Hono node adapter，@std/path 换 node:path。
- ⚡ 迁移后构建速度提升 15%；作者认为若更多使用 Node 内置 API，性能还有提升空间。
- 📉 Deno 衰退：从创新运行时变成普通创业公司，产品不吸引人，裁员后剩下 AI 幻想和 vibe-coding。
- 💥 离开 Deno 的导火索包括 ZSH 集成坏了几周、JSR 频繁 429、并发 HTTP 请求 bug；JSR 按其要求快速删除账号。
- 🗑️ 作者认为今天没有理由再用 Deno 运行时，最终 brew uninstall deno。

---

### [](https://dbushell.com/2021/03/12/built-with-deno/)

**原文标题**: [Built with Deno â David Bushell â Web Dev (UK)](https://dbushell.com/2021/03/12/built-with-deno/)

作者将个人静态站点生成器从 Node 迁移到 Deno，并分享在生产环境使用后的第一印象：Deno 的 API、模块系统、内建工具和安全权限现代且有潜力，但生态兼容性、运行时体积、Netlify 部署支持等问题仍存；作者会继续自用观察，暂不用于客户项目。

- ⚠️ 文章写于 2021 年，距今已久，个人观点和技术细节可能已过时。
- 🛠️ 作者把自己的静态站点生成器从 Node 改写为 Deno，用 Svelte 模板和 Markdown 数据做服务端渲染。
- 🚀 Deno 感觉更现代：API 和标准库比 Node 更易用，全面基于异步和 Promise。
- 📦 Deno 没有 NPM 等价物，使用 ES 模块和 URL 导入，模块可版本化，支持 import maps，全局缓存，无 node_modules。
- 🔌 许多 NPM 包可在 Deno 中运行，官方有 Node 兼容模块，但 CommonJS 和 require 兼容仍是主要痛点。
- 🧰 Deno 内建格式化、lint、测试、打包等工具，作者担心维护负担和体积膨胀，希望有精简版。
- 🔐 安全权限是重要特性，但开发时可能图方便使用 `--allow-all --unstable`。
- ☁️ Netlify 构建环境暂无 Deno，作者通过脚本在构建时下载安装，增加约一分钟构建时间。
- ⚖️ 结论：Deno 有改进和潜力，长期可能更好，但“更好”不保证替代“足够好”的 Node。
- 👀 作者建议 Node 用户关注 Deno，因为它有势头；自己会继续维护 Deno 网站观察，但暂不用于客户项目。

---

### [](https://serpapi.com/?utm_source=cooperpress-newsletter)

**原文标题**: [SerpApi: Google Search API](https://serpapi.com/?utm_source=cooperpress-newsletter)

未提供任何可摘要的文本内容，因此暂时无法生成要点总结。请补充需要总结的文章或文本，我会按指定格式整理成中文要点。

- 📭 当前输入为空，没有可供提炼的正文内容。
- ✍️ 请粘贴或提供具体文本，我将据此生成摘要。
- 🔍 收到内容后，我会提炼关键信息、核心观点与重要细节。
- 🧾 输出将使用“-”符号与合适的 emoji，并附上概览总结。

---

### [我测试了 11 个 HTTP 弹性库](https://blog.gaborkoos.com/posts/2026-10-04-I-Tested-11-Http-Resilience-Libraries/)

**原文标题**: [I Tested 11 HTTP Resilience Libraries](https://blog.gaborkoos.com/posts/2026-10-04-I-Tested-11-Http-Resilience-Libraries/)

作者在构建 ffetch 时发现，HTTP 韧性模式一旦组合就会暴露大量边界问题，因此用 21 个场景测试了 11 个 HTTP 韧性库。基础重试大多可靠，但取消、总超时、排队中止、半开熔断、对冲和去重组合暴露出明显差异。结果绑定固定版本，代码与报告公开，强调不能只看“是否支持某功能”，而要看实际组合契约。

- 🧪 测试范围：11 个库、21 个场景，覆盖重试、超时、熔断、舱壁、对冲、去重，使用脚本化 fetch、Vitest 假定时器和真实 HTTP 集成。
- 📦 参赛库包括 ffetch、ky、fetch-retry、ofetch、wretch、resilient-fetch-client、fetch-smartly、@resili/fetch、fetch-resilience、flowshield、ts-retry-circuit。
- ✅ 全体通过的基础：重试恢复、重试耗尽、零重试、真实 HTTP 重试、重试时请求体重放；重试基本已是商品化能力。
- ⚠️ 失败集中在组合场景：策略等待期间发生取消、截止时间到期、排队调用者离开、熔断器重开后旧请求才成功。
- ⏱️ 重试 + 退避中止：6 个库延迟结算 promise，5 个库在中止后仍继续发送请求；fetch-retry 的延迟不读取 abort signal。
- 🚧 舱壁 + 排队中止：5 个有队列的库中 4 个失败，取消的等待者仍占容量且替换请求被拒；ffetch 是唯一通过者。
- ⏳ 重试 + 总超时：wretch、resilient-fetch-client、fetch-resilience、flowshield 在截止后继续分派；多库只有单次尝试超时，没有跨重试总超时。
- 📅 Retry-After + 中止：resilient-fetch-client 的等待不可中断；@resili/fetch 不按响应头控制重试时序；6 个库完全不读取该头。
- 🪝 重试钩子抛错：wretch 在回调拒绝后不结算调用者 promise，可能导致应用层永久 await。
- 🌀 对冲最不成熟：仅 3 个库有可配置延迟对冲，产生 32 个 N/A 单元；flowshield 在多个截止时间失败，超时后仍启动或留下分支。
- 🔁 去重 + 重试：@resili/fetch 正确共享重试序列，却把同一个已消费响应交给所有调用者，多数调用者拿到不可用结果。
- ⚡ 熔断 + 半开并发：ffetch 自身因旧成功请求导致 circuitOpen 状态错误但仍正确拒绝流量；fetch-smartly 与 ts-retry-circuit 更严重，旧成功会放行新请求并消耗恢复响应。
- 🧭 作者承认确认偏误：场景源自 ffetch 已修 bug，规则有时主观；测试只衡量固定版本的正确性，不评估性能、API、文档或维护响应。
- 🔄 矩阵可复现并持续更新：GitHub 提供代码，报告每周重建，结果发布在 fetchkit.org/http-resilience。
- 🧩 结论：同名功能不代表相同契约；应针对应用真实使用方式测试组合策略，而不是只看功能列表。

---

### [](https://github.com/sindresorhus/ky)

**原文标题**: [GitHub - sindresorhus/ky: 🌳 Tiny & elegant JavaScript HTTP client based on the Fetch API · GitHub](https://github.com/sindresorhus/ky)

Ky 是一个基于 Fetch API 的轻量、优雅 JavaScript HTTP 客户端，面向现代浏览器、Node.js、Bun 和 Deno，零依赖；它比原生 fetch 提供更多便捷能力，包括重试、超时、钩子、进度、Schema 校验和 TypeScript 支持，并在 GitHub 上拥有约 17.1k stars。

- 🌳 核心定位：微型、优雅、无依赖的 JavaScript HTTP 客户端，基于 Fetch API。
- 🌐 支持环境：现代浏览器、Node.js 22+、Bun、Deno；最新版 Chrome、Firefox、Safari。
- ⭐ 仓库数据：约 17.1k stars、499 forks、64 watchers、549 commits，由 Sindre Sorhus 等维护。
- 🚀 相比原生 fetch：更简单 API、方法快捷方式、非 2xx 自动报错、重试、JSON 快捷、超时、上传/下载进度、baseUrl、自定义实例、hooks。
- 📦 安装使用：`npm install ky`；Deno/CDN 可通过 esm.sh、jsdelivr、unpkg 导入。
- 🔧 核心 API：`ky(input, options?)` 与 fetch 类似，返回增强的 Response，支持 `.json()`、`.text()`、`.formData()`、`.arrayBuffer()`、`.blob()`、`.bytes()`。
- 🧩 方法快捷：`ky.get/post/put/patch/head/delete/query`，自动设置对应 HTTP 方法。
- 🧾 JSON 支持：`json` 选项自动序列化并设置 Content-Type；`.json()` 支持 TypeScript 泛型，默认 `unknown`。
- ✅ Schema 校验：可用 Zod、Valibot 等 Standard Schema 校验响应，失败抛出 `SchemaValidationError`。
- 📊 常用选项：`searchParams`、`baseUrl`、`prefix`、`retry`、`timeout`、`totalTimeout`、`maxResponseSize`、`throwHttpErrors`、进度回调、`parseJson`、`stringifyJson`、自定义 `fetch`、`context`。
- 🔁 重试机制：默认重试 2 次，支持状态码、方法、Retry-After、指数退避、backoffLimit、jitter、超时重试和自定义 `shouldRetry`。
- 🪝 生命周期 hooks：`init`、`beforeRequest`、`beforeRetry`、`beforeError`、`afterResponse`，可修改请求/响应、提前返回响应或强制重试。
- 🧱 实例创建：`ky.create()` 创建全新默认实例，`ky.extend()` 继承并深合并选项，`replaceOption` 可完全替换合并字段。
- ⚠️ 错误体系：`KyError` 为基类；包含 `HTTPError`、`NetworkError`、`TimeoutError`、`ResponseSizeError`、`ForceRetryError`；`SchemaValidationError` 不属于 KyError。
- 🛠️ 实用技巧：FormData、URLSearchParams、自定义 Content-Type、AbortController 取消、Node.js 代理、HTTP/2、流式请求体、SSE、分页、类型扩展。
- 🌐 生态对比：比 got 更小且基于 Fetch；比 axios 更现代、标准兼容且跨浏览器/Node/Bun/Deno。
- 💬 名称含义：KY 是日语“空気読めない”的缩写，意为“不会读空气”，同时也是随机短 npm 包名。
- 🔗 相关资源：`fetch-extras`、`ky-hooks-change-case`；FAQ 覆盖 SSR、认证头、401 token 刷新、测试 mock、按响应体重试等场景。

---

### [](https://github.com/unjs/ofetch)

**原文标题**: [GitHub - unjs/ofetch: 😱 A better fetch API. Works everywhere. · GitHub](https://github.com/unjs/ofetch)

ofetch 是 unjs 推出的增强版 fetch API，目标是在 Node、浏览器和 workers 中提供一致且更易用的请求体验；当前 README 位于 v2 alpha 分支，v1 文档需查看 v1。

- 😱 ofetch 定位为“更好的 fetch API”，可在 Node、浏览器和 workers 运行。
- 📦 安装：`npx nypm i ofetch`；导入：`import { ofetch } from "ofetch"`。
- 🧠 智能解析响应：默认解析 JSON；二进制内容返回 `Blob`，也可用 `parseResponse` 或 `responseType` 指定 `blob`、`arrayBuffer`、`text`、`stream`。
- 📨 JSON body 会自动 `JSON.stringify`；对 PUT/PATCH/POST 自动添加 `content-type` 与 `accept: application/json`，并支持二进制 body 和 `duplex: "half"` 流式请求。
- 🚨 错误处理：`response.ok` 为 false 时抛出 `FetchError`，错误体可通过 `error.data` 获取；可用 `ignoreResponseError` 跳过状态错误。
- 🔁 自动重试：默认重试 1 次，但 POST/PUT/PATCH/DELETE 默认不重试以避免副作用；可配置 `retry`、`retryDelay`、`retryStatusCodes`，默认重试 408、409、425、429、500、502、503、504。
- ⏱️ 超时：通过 `timeout` 设置毫秒数，超时后自动中止请求，默认禁用。
- 🧩 类型友好：支持泛型，如 `ofetch<Article>('/api/article/1')`，可获得自动补全。
- 🔗 URL 处理：`baseURL` 与 `query`/`params` 基于 `ufo` 拼接和合并查询参数。
- 🪝 拦截器：支持 `onRequest`、`onRequestError`、`onResponse`、`onResponseError`，可传数组，也可用 `ofetch.create` 共享。
- 🧰 默认选项与扩展：`ofetch.create` 可创建带默认选项的实例；支持 `headers`、`ofetch.raw` 获取原始响应、`ofetch.native` 使用原生 fetch。
- 📡 SSE：可通过流式响应配合 `getReader()` 与 `TextDecoder` 读取 SSE 分块内容。
- 🕵️ 代理支持：Bun/Deno 支持环境变量，Node 需 `NODE_USE_ENV_PROXY=1` 或使用 undici 的 `ProxyAgent`/`dispatcher`；Bun 也可用 `proxy` 选项。
- 🧬 类型增强：可通过 `declare module "ofetch"` 扩展 `FetchOptions` 接口，获得自定义属性的类型安全。
- 📄 许可证：MIT；仓库约有 5.4k stars、197 forks、14 watchers。

---

### [Wretch - 小巧的 Fetch 封装器](https://elbywan.github.io/wretch/)

**原文标题**: [Wretch - The Tiny Fetch Wrapper](https://elbywan.github.io/wretch/)

Wretch 是一个围绕 fetch 封装的轻量级 HTTP 请求库，体积仅约 1.8KB（gzip），语法直观、不可变、可链式调用、支持同构环境与模块化扩展，适合快速构建简洁优雅的 HTTP 请求。

- 📦 轻量封装：基于 fetch，体积约 1.8KB（gzip），API 直观易用。
- 🔗 链式调用：所有方法 100% 可链式调用，代码更简洁优雅。
- 🧊 不可变设计：不修改内部状态，每次调用返回原对象副本。
- 📖 语法直观：可读性强，包含 TypeScript 定义文件，支持自动补全。
- 🌐 同构兼容：可在浏览器和 Node.js 中使用，并支持任意 polyfill。
- 🧩 模块化扩展：通过 Addons 添加方法，通过 Middlewares 拦截请求并自定义行为。
- 🚀 快速上手：导入 wretch、创建实例、配置 URL、添加请求体、执行方法、处理错误、解析响应。
- 💻 多种安装：支持 npm、yarn、pnpm、bun 和 CDN 引入。
- ✨ 完整示例：可链式使用 `.json()`、`.post()`、`.notFound()`、`.error(500)`、`.json()` 等。
- 🛠️ 功能扩展：Addons 支持 query strings、form data 等，Middlewares 支持重试、缓存、节流和自定义拦截器。
- 📜 开源许可：MIT License，作者为 Julien Elbaz，图标来自 Lucide。

---

### [](https://github.com/fetch-kit/ffetch)

**原文标题**: [GitHub - fetch-kit/ffetch: TypeScript-first fetch wrapper with configurable timeouts, retries, and circuit-breaker baked in. · GitHub](https://github.com/fetch-kit/ffetch)

@fetchkit/ffetch 是 fetch-kit 生态中的 TypeScript 优先 fetch 封装，可作为原生 fetch 或任意 fetch 兼容实现的生产级替代。它保留 fetch 使用体验，同时内置超时、重试和断路器，并通过可选插件提供去重、舱壁、对冲等弹性能力，核心约 3KB、零运行时依赖。

- 🚀 定位：drop-in 替换原生 fetch，可包装 node-fetch、undici 或框架提供的 fetch，适用于 SSR、边缘与自定义运行时。
- 🛡️ 核心保障：可配置超时、指数退避+抖动重试、abort-aware 重试、自定义错误与 throwOnHttpError。
- 🧩 插件架构：按需引入 dedupe、bulkhead、circuit、hedge、contextId、request/response shortcuts、download progress 等插件，均可 tree-shake。
- ⚙️ 可观测与扩展：支持生命周期 hooks、pendingRequests 实时监控、每请求覆盖，以及日志、认证、指标、请求/响应转换。
- 📦 轻量与兼容：约 3KB minified、零运行时依赖、双 ESM/CJS，支持 Node.js、浏览器、Cloudflare Workers、React Native。
- 🧪 使用方式：通过 createClient({ timeout, retries, plugins, hooks }) 创建客户端，支持 api(url)、api.get(url).json() 和自定义 fetchHandler。
- 🌐 环境要求：最好有原生 AbortSignal.any；Node.js 20.6+ 与较新浏览器可直接使用，旧环境需 polyfill，AbortSignal.timeout 有内部兜底。
- 🔁 去重限制：默认关闭；对 ReadableStream、FormData、Blob 跳过；非幂等请求慎用；需保证自定义 hash 唯一。
- 📊 竞品对比：相比 axios/ky，独有插件管道、断路器、去重、bulkhead、hedging、待处理请求监控、强类型和自定义 fetch 支持。
- 🔐 安全与治理：OpenSSF Scorecard、CodeQL、Dependabot、OIDC provenance、SBOM、分支保护、安全策略与私密漏洞报告。
- 🤝 社区与许可：有 ffetch-demo、Fetch-Kit Discord，曾被 Node Weekly #594 收录，采用 MIT 许可证。

---

### [获取失败](https://medium.com/booking-com-development/node-js-at-scale-rebalanced-how-we-cut-cost-by-38-62ce247a3002)

**原文标题**: [Failed to retrieve](https://medium.com/booking-com-development/node-js-at-scale-rebalanced-how-we-cut-cost-by-38-62ce247a3002)

无法总结：获取内容失败，状态码 403。

---

### [Watt 快速入门 | Platformatic 开源软件](https://docs.platformatic.dev/docs/getting-started/quick-start)

**原文标题**: [Watt Quick Start | Platformatic Open Source Software](https://docs.platformatic.dev/docs/getting-started/quick-start)

Platformatic Watt 是一个 Node.js 应用服务器；本指南演示如何快速搭建由 Next.js 前端、原生 node:http 应用和 Platformatic Gateway 组成的多应用项目，并涵盖初始化、启动、应用间通信、生产构建与调试。

- 🚀 Watt 快速入门版本为 3.71.0，目标是创建并运行一个多应用 Node.js 项目。
- 🧰 先决条件：Node.js v22.19.0+、npm，以及任意代码编辑器。
- ⚙️ 使用 `npx wattpm create` 初始化项目，可选择 `@platformatic/node` 创建 Node.js 应用。
- 📦 初始化后会自动生成 `watt.json`，并在 `package.json` 中加入 `@platformatic/node` 依赖。
- 🧩 示例 Node.js 应用使用 `node:http` 的 `createServer`，并通过 `@platformatic/globals` 的 `getLogger()` 记录日志。
- 🧵 Watt 会在独立 worker thread 中运行应用，也支持 Express、Fastify、Koa 等框架。
- ▶️ 在项目根目录运行 `npm start` 或 `wattpm start` 启动服务；运行 `npm run dev` 或 `wattpm dev` 启用监听模式。
- 🌐 添加 Platformatic Gateway 可协调多个应用；默认将 Node.js 应用代理到 `/node` 路径。
- ⚛️ 使用 `npx create-next-app web/next` 添加 Next.js 应用，但需处理 npm workspaces 的依赖提升问题。
- ⚠️ 需将 `web/next/package.json` 的 `name` 改为非依赖包名，例如 `frontend`，避免遮蔽 Next.js 框架。
- ⚠️ 需在 `next.config.mjs` 中设置 `turbopack.root` 指向 Watt 项目根目录，避免 Turbopack 找不到 `next/package.json`。
- 🔗 运行 `npx wattpm-utils import` 将 Next.js 应用导入 Watt，并安装必要依赖。
- 🛣️ 在 `web/next/watt.json` 中设置 `basePath: "/next"`，即可通过 `http://localhost:3042/next` 访问。
- 🔄 Next.js 可通过内部域名 `http://node.plt.local` 获取 Node.js 应用数据，并使用 `{ cache: 'no-store' }` 禁用缓存。
- 🏗️ 生产构建使用 `npm run build` 或 `wattpm build`；生产启动使用 `npm run start` 或 `wattpm start`。
- 🐞 使用 Chrome DevTools 调试：运行 `npm run start -- --inspect`，然后访问 `chrome://inspect`。
- 💻 使用 VS Code 调试：设置断点，开启 `Debug: Toggle Auto Attach` 为 `Always`，再运行 `npm run dev`。
- 📌 文中提到的 npm workspace 与 Turbopack 问题属于依赖解析问题，并非 Watt 运行时本身缺陷。

---

### [JavaScript/TypeScript 的可读正则表达式，灵感来自 Emacs 的 rx | Rahul 的博客](https://www.rahuljuliato.com/posts/emacs-rx-in-typescript)

**原文标题**: [Readable Regular Expressions for JavaScript/TypeScript, Inspired by Emacs' rx | Rahul's Blog](https://www.rahuljuliato.com/posts/emacs-rx-in-typescript)

受 Emacs `rx` 启发，文章提出一套用于 JavaScript/TypeScript 的可读正则 DSL：用命名构件组合正则，自动生成并转义正则字符串，让复杂模式更易读、易改、易维护，并提供完整单文件实现、速查表与大量对照示例。

- 📌 痛点：官方 SemVer 正则等复杂表达式难读难维护，修改时往往需重新解码或重写。
- 🧩 灵感来自 Emacs Lisp 的 `rx` 宏：用树状命名形式描述正则，由宏生成正则字符串。
- 🔧 提出 JS/TS 版 DSL：`RX(...)` 返回可直接使用的 `RegExp`，`rx(...)` 返回正则字符串。
- ⚠️ 文中 `RX` 与 RxJS 无关，只是同名。
- 🧱 核心抽象：每个片段是 `RxNode`，含 `src`、`kind`（`atom`/`seq`/`alt`）及可选字符集信息，普通字符串经 `literal` 转义。
- 🔗 `seq` 顺序连接片段，只给备选分支加 `(?:...)`，并处理反向引用后接数字等边界情况。
- 🎯 `or` 生成备选；若分支全是字符串，按长度降序排序以优先匹配最长项，空分支返回 `unmatchable`。
- 🔢 量词包括 `zeroOrMore`、`oneOrMore`、`optional`、对应 Lazy 版本，以及 `repeat`、`atLeast`、`between`。
- 🔤 字符集支持 `anyOf`、`not`、`notChar`，以及 `digit`、`space`、`wordChar`、`alpha`、`hexDigit` 等 Emacs 风格类别；注意实现为 ASCII。
- 📍 锚点提供 `start`/`end`、`lineStart`/`lineEnd`、`wordBoundary`，并用 lookaround 模拟 `wordStart`/`wordEnd`。
- 👥 分组支持 `group`、`named`、`backref`，命名捕获组可读性更好。
- 🧪 通过 `literal(...)` 明确运行时字符串按字面量匹配，`raw(...)` 作为接入旧正则的逃生舱。
- 📚 文中用 SemVer、邮箱、电话、十六进制颜色、HTML 标签、重复词等示例对比手写正则与 DSL 写法。
- 📋 提供 Emacs `rx`、TypeScript DSL 与 JS 正则的速查表，以及可直接复制使用的无依赖完整源码。
- 🚫 未完全覆盖 Emacs `rx` 的 `point`、`syntax`、`category`、`intersection`、`minimal/maximal-match`、`eval` 等特性。
- ➕ 额外加入 `RX.flags`，因 JS 将大小写等选项放在正则对象上，而非 Emacs 的 `case-fold-search`。
- 💡 总结：该 DSL 并非新概念，但延续了 Emacs `rx` 与 Zod 等“用小构件组合可读结构”的精神，适合在 JS/TS 中逐步采用。

---

### [](https://radekmie.dev/blog/on-automatic-type-refinements/)

**原文标题**: [On Automatic Type Refinements · @radekmie’s take on IT and stuff](https://radekmie.dev/blog/on-automatic-type-refinements/)

概述总结：本文讨论 TypeScript 的自动类型细化，说明 TS 5.5 如何自动推断类型谓词来让 filter 安全收窄类型；同时指出运行时安全的代码未必能被类型系统识别，最后呼吁保持代码“显而易见”。

- 🧠 作者延续此前《On Type Inference》的观点：尽量依赖隐式推断类型，并强调类型细化（类型收窄）的重要性。
- 🗣️ 常见误解是 Array#filter 不安全，尤其 .filter(Boolean) 不会移除 undefined；文章对此进行澄清。
- ✅ TypeScript 5.5 起，x => x !== undefined 与 typeof x === 'number' 等回调可被推断为类型谓词 x is number，从而正确收窄数组类型。
- 🕰️ 在 5.5 之前，这类回调通常只被推断为返回 boolean/unknown，因此 foo 和 bar 都只能返回 (number | undefined)[]。
- ⚠️ 运行时安全不代表类型系统能识别：x => !!x 会移除 undefined，但对 number/string 不会自动细化；对 Date、对象类型甚至 boolean 可能有效。
- 🔁 !!x 与 filter(Boolean) 技术等价，Boolean 可能略快（不分配新函数）；但 0 是 falsy，!!0 为 false，所以 0 也会被过滤掉。
- 🧾 相关开放 issue：#15048（单边类型守卫）、#16655 + #50387（让 Boolean 成为类型谓词）、#42384（字段级细化传播到父对象）。
- 💡 核心结论：让代码保持“显而易见”，类型系统更容易理解并给出安全细化，长期有回报。

---

### [](https://tanstack.com/blog/tanstack-charts-1-0)

**原文标题**: [TanStack Charts 1.0 | TanStack Blog](https://tanstack.com/blog/tanstack-charts-1-0)

TanStack Charts 1.0 正式发布：它由 Tanner Linsley 撰写，主张打造“不会被淘汰”的图表库，让简单折线图到复杂数据可视化都能在同一套基于 marks/scales 的可组合、类型安全系统中持续扩展，并承诺 1.0 API 稳定与长期支持。

- 📅 2026 年 10 月 5 日，Tanner Linsley 宣布 TanStack Charts 1.0 发布。
- 🎯 核心目标是“Charts you don’t have to outgrow”：图表不应随产品增长而被替换。
- 🧱 作者经历涵盖 Nozzle、D3、Chart.js 2.0、react-charts、Observable Plot，积累了约十年图表经验。
- 🤖 AI 在实现阶段帮助作者快速落地多年设计想法，但 API 与体验仍由作者亲自设计打磨。
- 🧩 架构基于 marks：线、点、柱都是 mark；scales 映射数据，再与 axes、interactions 组合成图表。
- ➕ 可组合性很强：想要点就加点，想要柱就加柱，无需寻找或新建“恰好包含所需组合”的图表类型。
- 🛠️ 支持自定义 marks、scales、interactions、renderers，并可深入 scene contracts 实现特殊需求。
- 🔒 类型安全贯穿数据、scales、marks 与 interactions，也便于 AI 辅助构建复杂图表。
- 🖼️ 默认使用 SVG 渲染；Canvas 作为独立导入和渲染器按需使用；动画也按需集成。
- 📦 支持紧凑 scales 与 D3 scales，可拆分为最小片段，重视 bundle budgets、测试和浏览器测试。
- ✅ 1.0 表示 API 稳定与支持承诺：升级不应导致重建，自定义 mark/renderer 也被纳入兼容考虑。
- 🚀 鼓励用户用实际应用图表让 AI 重写为 TanStack Charts，添加搁置功能，构建“奇怪图表”并反馈不便之处。
- 🔗 文末提供浏览图表目录和开始使用 TanStack Charts 的入口。

---

### [图表目录 | TanStack](https://tanstack.com/charts/catalog)

**原文标题**: [Charts Catalog | TanStack](https://tanstack.com/charts/catalog)

shadcn/ui Charts 是一个汇集 188 个图表示例的可视化目录，按大量分类标签组织，覆盖基础图表、统计分布、地图、网络、交互、动效与 shadcn 官方组件示例。
- 📚 页面提供 188 个可打开示例，并按 application、area、bar、trend、interaction、geography 等标签筛选。
- 📈 趋势与时间类包括 Apple 股价、行业失业率、温度区间带、移动平均、Bollinger 带和日历热图。
- 📊 比较与组成类包括排序/分组/堆叠条形、棒棒糖、哑铃、流图、瀑布、马赛克、饼/环/玫瑰图。
- 🔍 关系与分布类包括气泡散点、线性回归、直方图、箱线图、蜂群图、小提琴图、热力图、六边形分箱和平行坐标。
- 🗺️ 空间与层级类包括 Voronoi、Delaunay 网络、等值线、地图投影、树、树图、旭日图、Sankey 和网络图。
- 🎛️ 交互与动效类包括提示框、刷选、缩放平移、播放、同步光标、可编辑区间、弹簧动画和几何变形。
- 🧩 主题与应用类包括主题调色板、KPI 迷你图、活跃条形/环形指标、可钻取旭日图以及 shadcn 仪表盘。
- 🏷️ 内置 shadcn 示例覆盖面积、条形、折线、饼、雷达、径向和提示框的多种变体，如标签、图例、堆叠、交互与图标样式。

---

### [SvelteKit 3 来了](https://svelte.dev/blog/sveltekit-3-is-here)

**原文标题**: [SvelteKit 3 is here](https://svelte.dev/blog/sveltekit-3-is-here)

SvelteKit 3.0 已正式发布，作为 Svelte 官方应用框架的新大版本，它在保持熟悉体验的同时提升了打磨程度、类型安全与简洁性；官方提供迁移工具，并带来配置、别名、环境变量、Service Worker、错误处理等变化。远程函数仍未就绪，Svelte Summit 将于下月在卢布尔雅那举行。

- 🚀 SvelteKit 3.0 现已发布，是 Svelte 官方应用框架的最新版本。
- 🧹 整体体验依旧熟悉，但更精致、类型更安全、冗余更少。
- 🛠️ 可用 `sv migrate sveltekit-3 --tasks all --confirm` 自动迁移代码，并生成 TODO 列表；新项目可用 `sv create` 创建。
- ⚠️ 大版本升级包含若干破坏性变更，详见迁移指南或近期 RC 公告。
- ⚙️ 配置从 `svelte.config.js` 移至 `vite.config.ts`。
- 📦 `$lib` 别名改为 `#lib`，改用标准子路径导入。
- 🌱 环境变量更强大易用；Service Worker 样板更少；错误处理全面改进。
- ⏳ 远程函数尚未就绪，但已是最高优先级；它用于安全、高效、类型安全的客户端-服务端通信，目前需要实验性 Async Svelte 标志。
- 🎉 下一届线下 Svelte Summit 将于 11 月 19-20 日在斯洛文尼亚卢布尔雅那举行，并庆祝 Svelte 十周年。

---

### [远程函数 • SvelteKit 文档](https://svelte.dev/docs/kit/remote-functions)

**原文标题**: [Remote functions • SvelteKit Docs](https://svelte.dev/docs/kit/remote-functions)

远程函数是 SvelteKit 中实验性的类型安全客户端-服务器通信机制。它们从 `*.remote.ts` 等 remote 模块导出，客户端调用会被转换为 HTTP 请求，服务端执行并可安全访问服务端专用模块；结合 Svelte 的实验性 `await`，可直接在组件中加载和修改数据。

- 🧪 启用方式：在 `vite.config.js` 的 SvelteKit 插件中开启 `compilerOptions.experimental.async` 和 `experimental.remoteFunctions`
- 📁 remote 模块：文件名需包含 `remote` 段，可放在 `src` 任意位置，但不能放在 `server` 目录
- 🔎 `query`：读取服务端动态数据，支持参数、Standard Schema 校验、缓存去重与 `refresh()`；整页预渲染时不可用
- ⚡ `query.batch`：在同一宏任务内批量执行查询，解决 n+1 请求问题
- 📡 `query.live`：实时异步迭代查询，支持 `connected` 与 `reconnect()`，但不应被 Service Worker 缓存
- 🧮 参数序列化：使用 devalue 处理 `Date`、`Map` 等类型，并为查询参数生成缓存键
- ♻️ 去重机制：相同参数的查询在服务端按请求缓存，在客户端共享同一实例
- 📝 `form`：创建可展开到 `<form>` 的对象；无 JS 时仍可提交，有 JS 时渐进增强
- 🧩 表单字段：通过 `fields.as(...)` 生成输入属性，支持嵌套对象、数组、文件、radio/checkbox 和多提交按钮
- ✅ 表单校验：使用 Valibot/Zod 等 Standard Schema；支持 `issues()`、`validate()` 和客户端 `preflight`
- 🔒 敏感字段：以下划线开头的字段名可在无效提交回传时避免暴露密码等内容
- ✨ `enhance`：自定义表单提交行为；使用后需手动调用 `form.element.reset()`
- 🛠️ `command`：用于任意写操作，优先使用 `form`；不能在渲染期间调用
- 🚀 单次飞行变更：在 `form`/`command` 中调用 `refresh()`、`set()`、`reconnect()`，让查询更新随变更响应返回
- 📬 客户端请求刷新：通过 `submit().updates` 或 `requested(query, limit)` 请求刷新；必须处理、忽略或重连，`limit` 用于防 DoS
- 🧱 `prerender`：构建时预渲染数据，适合每次部署最多变化一次的数据；支持 `inputs` 和 `dynamic: true`
- 🚨 校验错误：通过 `handleError` 的 `kind: 'validation'` 处理，可记录或定制响应，但应谨慎暴露 issues
- 🧷 `getRequestEvent`：在 `query`、`form`、`command` 中访问请求事件，如 cookies；但 `query` 中不能设置 headers 或依赖 route/params/url
- ↪️ 重定向：可在 `query`、`form`、`prerender` 中使用 `redirect(...)`；`command` 中不允许重定向

---

### [迁移到 SvelteKit v3 • SvelteKit 文档](https://svelte.dev/docs/kit/migrating-to-sveltekit-3)

**原文标题**: [Migrating to SvelteKit v3 • SvelteKit Docs](https://svelte.dev/docs/kit/migrating-to-sveltekit-3)

SvelteKit 3 是一次重大破坏性升级：配置从 `svelte.config.js` 迁移到 `vite.config.js` 的 `sveltekit()` 插件，多个 API/模块被移除、重命名或替换，并提高了最低依赖版本。官方建议先用 `npx sv migrate sveltekit-3` 自动迁移，且最好先升级到最新 2.x 以获取弃用警告。

- 🚀 最低依赖：Node v22.17、TypeScript v6、Svelte v5.57.1、Vite v8.0.12、`@sveltejs/vite-plugin-svelte` v7。
- ⚙️ 配置迁移：不再支持 `svelte.config.js`；配置改到 `vite.config.js` 的 `sveltekit(...)` 插件中，原 `config.kit.*` 变为顶层插件选项。
- 🧹 选项变化：移除 `files.lib`、`preloadStrategy`、`prerender.origin`、`csrf.checkOrigin` 等；新增 `output.linkHeaderPreload`、`csrf.trustedOrigins`、`paths.origin`；`version.pollInterval` 默认每小时。
- 📦 `$lib` 改为 `#lib`：不再自动生成 `$lib`，需在 `package.json` 的 `imports` 中声明 `#lib`，并补充 `.js`/`.ts` 扩展名。
- 🧭 模块重命名/移除：`$app/environment` 改为 `$app/env`；`$app/stores` 移除，改用 `$app/state`；`$env/...` 弃用，改用 `$app/env/private` 与 `$app/env/public`。
- 🧩 新增模块：`$app/manifest` 提供应用元数据；`$app/service-worker` 提供服务 worker 类型；service worker 可导入 `$app/paths`。
- 🔀 导航变化：浅路由用 `goto` 替代 `pushState/replaceState`，支持 `persistState`，并触发导航钩子；`invalidateAll` 弃用，改为 `refreshAll`。
- 📉 导航细节：`goto` 无法解析到应用路由时会 reject；`delta` 仅用于 popstate；`preloadData` 可能返回 error；点击当前页链接会触发刷新。
- 🛡️ 表单：`use:enhance` 指定其他页面 action 时会导航到该页；增强表单响应使用 `fail` 状态码；远程表单字段必须用 `field.as(...)`。
- 🧾 `$app/paths`：移除 `base`、`assets`、`resolveRoute`，改用 `asset` 与 `resolve`；类型改为 `Path`/`AssetPath`，路径不再以 `/` 开头。
- 🗂️ TypeScript：根 `tsconfig.json` 应继承 `$app/tsconfig`；service worker 使用单独 `tsconfig` 并继承 `$app/tsconfig/service-worker`。
- 🔧 `@sveltejs/kit`：`json`/`text` 弃用，改用 `Response.json`/`new Response`；`defineParams` 移至 `@sveltejs/kit/params`；类型分散到 `env`、`hooks`、`$app/server`。
- 🧵 Node/适配器：`getRequest`/`setResponse` 变同步；移除 `@sveltejs/kit/node/polyfills`；`adapter-node` 使用 rolldown，移除 `ORIGIN`，改用 `paths.origin`。
- 🔐 安全：`csrf.checkOrigin` 被 `csrf.trustedOrigins` 取代；跨域表单需带 `Content-Type`；开发环境静态资源 CORS 由 Vite 处理。
- 🍪 Cookie：升级到 cookie v2，名称仅限 ASCII，类型重命名；未指定 `path` 时默认 `'/'`。
- ⚠️ 错误处理：`App.Error` 始终含 `status`；`error(...)` 第二参数必须是字符串，额外属性放第三参数；`handleValidationError` 移除；`handleError` 接收所有错误并可影响状态码。
- 🧪 参数匹配：不再使用 `src/params` 目录，改为单个 `src/params.ts`，并用 `defineParams` 定义。
- 📡 可观测性：存在 `src/instrumentation.server.js` 时自动启用服务端 instrumentation；OpenTelemetry 通过 `tracing.server` 开启。
- ☁️ 适配器变化：Cloudflare 从 `cloudflare:workers` 导入 `env`/`waitUntil`，`request.cf`、全局 `caches`；Netlify 输出遵循 Frameworks API；Vercel 不再支持 edge runtime。
- 🧰 适配器 API：适配器可增强 Vite 配置；`builder.config.kit` 消失；`createEntries`/`generateManifest` 等移除或替换；`instrument` 需先生成环境初始化器。
- 📥 响应：204/空 2xx 返回无内容；`handle` 的 `resolve` 始终返回 `Promise<Response>`。
- 📁 仅服务端模块：以文件名中的 `server` 段标识；任何 `server` 目录（除 `src/routes` 与 `static`）都视为仅服务端。
- 🧪 远程函数：仍为实验性，需开启 `experimental.remoteFunctions` 与 `compilerOptions.experimental.async`；文件名含 `remote`；query 内不可访问 `event.url/params/route`。
- 🧷 其他：`data-sveltekit-*` 的 `'off'` 改为 `false`；外部重定向需显式 `external` 选项；通用 `+page.js`/`+layout.js` 的 `config` 优先于 server 版本；service worker 以 module 方式注册。

---

### [从 Adobe Substance 3D Painter 发布到 Miris | Miris](https://www.miris.com/blog/from-substance-to-browser?utm_source=web_referral&mrls=web_referral&utm_medium=public_relations&mrlc=public_relations&utm_campaign=raz-pr&utm_content=plugin&prg=fidelity&utm_term=javascript&dp=dp)

**原文标题**: [Publish to Miris from Adobe Substance 3D Painter | Miris](https://www.miris.com/blog/from-substance-to-browser?utm_source=web_referral&mrls=web_referral&utm_medium=public_relations&mrlc=public_relations&utm_campaign=raz-pr&utm_content=plugin&prg=fidelity&utm_term=javascript&dp=dp)

概述总结
Miris 通过流式传输高保真 3D 资产，让开发者无需在构建阶段减面、压缩纹理或编写 LOD 代码；新 Adobe Substance 3D Painter 插件支持从创作端全分辨率发布 OpenUSD/OpenPBR 资产，并可通过 Web Components 或 Three.js 快速嵌入网页。

- 🎨 解决传统痛点：网页 3D 通常要减面、缩纹理、压缩并制作 LOD，耗时且牺牲艺术家原貌。
- ⚡ 流式体验：首帧低于 1 秒，随后几秒内细节逐步锐化；同一源资产按设备和网络自适应交付。
- 🧩 新 Painter 插件：在 Adobe Substance 3D Painter 中选择 Miris > Publish，直接上传 OpenUSD 与 OpenPBR。
- 📦 全分辨率支持：支持 UDIM、多纹理集和最高 10 GB；8 MB 到 800 MB 资产均全分辨率上传，Miris 一次性构建流式版本。
- 💻 Web Components 集成：添加 script 标签及 `<miris-scene>`、`<miris-stream>` 两个标签即可使用，也可通过 npm 安装。
- 🧱 Three.js 集成：`@miris-inc/three` 提供 `MirisStream` 和 `MirisScene`，使用 `WebGPURenderer` 与 `requiredLimits`，相机和动画循环可保持不变。
- 🔐 密钥安全：viewer key 可安全放在客户端并按标签限定资产；上传/管理使用单独的 integration key，不能暴露在浏览器。
- ⚠️ 使用限制：需要 WebGPU、HTTPS 或 localhost；`file://` 不可用；WebSocket 连接 `*.miris.com`；目前每场景一个 viewer key；仅支持静态资产，无动画；LOD 自动且无手动控制 API。
- 🚀 试用方式：可在 `app.miris.com/sign-up` 注册 Public Beta，上传资产后几分钟内体验流式播放。
- 🏢 方案与生态：覆盖零售电商、媒体娱乐、Physical AI 与机器人，并提供客户故事、合作伙伴、文档、Web SDK、REST API、CLI、Portal、Player、Playground 等资源。

---

### [Effect 4.](https://effect.website/blog/releases/effect/40)

**原文标题**: [Effect 4.0 | Effect Blog](https://effect.website/blog/releases/effect/40)

Effect 4.0 正式发布，这是迄今最雄心勃勃的版本：从头重建，核心零依赖，包体积、并发吞吐和内存占用均大幅优化；生态更统一，已被主流采用，并提供长期支持，后续将继续稳定和扩展。

- 🚀 Effect 4.0 发布：从头重建，更快、更省内存、tree-shaking 后包更小。
- 📦 包体积缩小 5 倍：最小程序从 35.6 kB 降至 7.1 kB。
- ⚡ 并发任务吞吐提升 6.4 倍：每秒任务从 0.71M 增至 4.57M。
- 🧠 Fiber 内存占用减少 86%：5 万 fiber 堆内存从 157.5 MB 降至 21.8 MB。
- 🔗 生态整合：许多原独立包并入 `effect`，共享单一版本并同步发布。
- 🛡️ 核心零运行时依赖：控制所有发布代码，减少第三方依赖链和供应链攻击风险。
- 🧩 覆盖范围从单个函数到分布式系统：内置类型化错误、依赖注入、资源管理、结构化并发、可观测性、持久化工作流和集群。
- 📈 主流采用：2026 年 9 月 21 日当周 npm 下载量 43.9M，自 3.x 增长 179 倍；4.x 采用率 56%，超过 3.x 的 44%。
- 🌐 社区生态：围绕 Effect 成长出 Alchemy 云基础设施、Foldkit 前端等项目。
- 🛡️ 长期支持：4.x 至少支持 3 年；bug 修复至 2029 年 9 月或 5.0 发布后一年，安全修复至 2029 年 9 月或 5.0 发布后两年，取较晚者。
- 🔜 下一步：稳定标记为 unstable/experimental 的模块，扩展原生平台支持和更高层原语。
- 🧭 迁移与学习：从迁移指南开始，可交给编码代理；也可查看文档或询问代理。
- ⏰ 最后更新：2026 年 9 月 30 日。

---

### [](https://lightpanda.io/blog/posts/lightpanda-1-0)

**原文标题**: [Lightpanda 1.0: Out of Beta and Ready for Production - Blog | Lightpanda](https://lightpanda.io/blog/posts/lightpanda-1-0)

Lightpanda 1.0 正式结束 beta，宣称已可用于生产环境；它通过超过 173 万个 Web Platform Tests 子测试、默认强制执行 CORS，并以 Zig 从零构建、无图形渲染，主打比 Chrome 更低的内存和 CPU 占用，面向 AI agent、搜索、索引与数据抽取等每天获取数十亿网页的场景。

- 🚀 Lightpanda 1.0 结束两年 beta，累计约 10,000 次提交，发布 1.0.0。
- ✅ 通过 1,739,845 个 WPT 子测试，约为 Chrome 2,184,491 个的 80%，接近 Firefox 2,137,997 个。
- 🔒 1.0 默认启用 CORS，页面发出的 fetch() 与 XMLHttpRequest 跨源读取必须遵守同源策略和预检规则。
- 🧠 无图形渲染、用 Zig 编写，运行现代 JavaScript，内存占用约为 headless Chrome 的 1/16。
- 🛠️ 兼容 Puppeteer、Playwright、Selenium、ChromeDP，支持 pip/npm 安装、MCP 服务器、CLI dump 与 agent 模式。
- 📈 WPT 增长显著：2024 年 11 月仅 2,645 个；DOM/HTML/Fetch/URL/cookies/events 推进到约 29 万，encoding/ 增加约 115 万，后续 workers/Shadow DOM/IndexedDB/XPath/WebSockets/forms 再增约 34 万。
- 🧩 与 Chrome 的主要差距在 CSS、editing、SVG 等布局与绘制测试，因为 Lightpanda 按设计不做图形渲染。
- 🛡️ 安全改进包括：可选资源加载、跨源重定向剥离 Authorization、更严格 cookies、CIDR/私有网络阻断、解析器与协议加固。
- ⚙️ 内置最新稳定 V8 15.5.35.13，使 Chrome/Node.js 所用 JS 引擎的安全修复也能覆盖 Lightpanda。
- 🏭 已在生产中使用：AI agent、搜索 API、索引和数据抽取公司每天获取数十亿网页，部分单客户日超 3000 万页。
- 📊 Keenable 表示，35% 以上答案依赖动态渲染页面，渲染成本可高 400 倍；Lightpanda 比 Chromium 快 4 倍、成本效率高 6 倍。
- 🚀 DeveloperHub.io 将 prerender 从 headless Chrome 迁移到 Lightpanda，页面快 4 倍、负载均值降 10 倍，不再需要定时重启和 CPU 告警。
- 🤖 Hermes Agent 将 Lightpanda 列为本地浏览器引擎，启动快 9 倍、内存少 16 倍，三行配置即可切换。
- 🧪 Vercel 的 agent-browser 可通过 --engine lightpanda 运行，并支持多 session 并行批处理。
- 📦 安装方式：curl -fsSL https://pkg.lightpanda.io/install.sh | bash -s "1.0.0"，也可用 npm/pip；建议保持 CORS 开启，遇到问题可临时使用 --disable-features cors。
- 📝 不渲染页面或截图：--dump png/pdf 只是把 markdown 渲染成图/PDF；查看页面可用 --dump markdown 或 --dump semantic_tree_text。
- 🔭 未来将继续提升 Web API 覆盖与 WPT 通过数，坚持速度与内存优先，目标是成为 AI agent 与机器人时代的默认网页浏览器。

---

### [PandaScript - 文档 | Lightpanda](https://lightpanda.io/docs/usage/pandascript)

**原文标题**: [PandaScript - Documentation | Lightpanda](https://lightpanda.io/docs/usage/pandascript)

PandaScript 是 Lightpanda 浏览器可直接运行的网页自动化脚本：无需 Node.js/Python、Puppeteer/Playwright、CDP 序列化或 LLM，只用原生 JavaScript 与少量内置原语，实现可复现、确定且无需 token 的抓取与交互。

- 🐼 **核心定义**：PandaScript 用普通 JavaScript 变量、函数、循环、对象、数组、`JSON.parse`、`JSON.stringify` 等标准 ECMAScript 能力编写。
- 🚀 **运行方式**：通过 `lightpanda run <my_script>.js` 执行，无需额外环境配置。
- 🧠 **运行上下文**：脚本运行在独立 V8 agent 上下文中，不是页面环境，也没有 `window`、`document`、DOM、`localStorage`、`navigator` 等浏览器全局对象。
- 🚫 **不是 Node.js**：没有 `require`、`process`、`fs`、`path`、npm 加载、命令行参数 API 或 Node 网络/文件系统 API。
- 🔒 **上下文隔离**：页面脚本看不到 agent 变量或 Lightpanda 原语，agent 脚本也不能直接访问页面变量。
- ⏳ **异步规则**：`goto` 是唯一异步原语，必须 `await page.goto(...)`；其他页面方法如 `extract`、`evaluate`、`click`、`fill` 等同步阻塞。
- 📤 **输出规则**：脚本顶层 `return` 的内容会被输出，对象和数组自动打印为 JSON；裸表达式不会打印，`console.log` 仅用于调试且不 JSON 格式化。
- 🧩 **数据提取**：首选 `page.extract(...)`，它按 schema 返回正常 JavaScript 值；对象 schema 返回对象，数组 schema 返回数组，值通常是字符串或 `null`。
- 🌐 **页面 JS 逃生舱**：`page.evaluate(...)` 在页面上下文运行，可访问 `window` 和 `document`，但不能访问 agent 变量或原语；`waitForScript(...)` 也在页面上下文轮询。
- 🖱️ **交互原语**：支持 `click`、`fill`、`press`、`waitForSelector`、`hover`、`selectOption`、`setChecked`、`scroll` 等操作当前页面。
- 🔐 **凭据保护**：字符串参数中的 `$LP_*` 占位符会在 Lightpanda 进程内解析，避免凭据写入脚本或 LLM 提示词。
- ⚠️ **错误处理**：原语失败会抛出 JavaScript 异常；常见错误包括 `document is not defined`、`require is not defined`、未先 `goto`、参数无效、schema 选择器全未命中。
- 🧪 **典型流程**：先抓取列表页，再在脚本中用循环 `goto` 每行 URL 并 `extract` 详情；agent 上下文会跨导航保留变量，便于本地组装数据。
- ✅ **完整示例**：抓取 Hacker News 前 5 条故事，访问每条评论页并提取评论，最后 `return stories` 自动输出 JSON。

---

### [](https://github.com/sindresorhus/eslint-cssicorn)

**原文标题**: [GitHub - sindresorhus/eslint-cssicorn: Powerful ESLint rules for CSS · GitHub](https://github.com/sindresorhus/eslint-cssicorn)

eslint-cssicorn 是一个为 CSS 提供强大 ESLint 规则的项目，需配合 @eslint/css 语言插件使用，支持 flat config 与 ESM，要求 ESLint >=10.4；提供 recommended、unopinionated、all 三套预设配置，并内置大量可自动修复或手动建议的 CSS 规则。仓库当前有 47 stars、2 watchers、0 forks、12 commits，采用 MIT 许可证，且明确表示不接受 PR，原因是 AI 生成内容过多。

- 📦 安装：`npm install --save-dev eslint @eslint/css eslint-cssicorn`
- ⚙️ 环境要求：ESLint >=10.4、flat config、ESM
- 🧩 使用方式：可选择预设配置，或在 `eslint.config.js` 中逐条配置规则；非预设需设置 `language: 'css/css'` 并添加 `@eslint/css` 插件
- 🛠️ 规则范围：涵盖选择器顺序、层叠层顺序、小写语法、重复属性/选择器、无效媒体特性、冗余长写属性、嵌套作用域、自定义属性循环、未知动画/伪选择器、零长度单位、`clamp()`、现代视口单位/媒体范围语法、短十六进制颜色等
- ✅ 预设配置：`recommended` 强制良好实践；`unopinionated` 包含错误检查与直接简化；`all` 启用全部规则
- 🔧 修复能力：许多规则可通过 `--fix` 自动修复，部分支持编辑器建议手动修复
- 🚫 PR 政策：仅协作者可创建 PR；README 表示不接受 PR，因为 AI 垃圾内容过多
- 🔗 相关项目：`eslint-plugin-unicorn` 有 300+ 规则且部分也 lint CSS；还有 `eslint-node-test`、`eslint-package-json`
- 📊 仓库状态：47 stars、2 watchers、0 forks、12 commits，MIT 许可证

---

### [发布 v77.0.0 · sindresorhus/eslint-plugin-unicorn · GitHub](https://github.com/sindresorhus/eslint-plugin-unicorn/releases/tag/v77.0.0)

**原文标题**: [Release v77.0.0 · sindresorhus/eslint-plugin-unicorn · GitHub](https://github.com/sindresorhus/eslint-plugin-unicorn/releases/tag/v77.0.0)

overview summary
eslint-plugin-unicorn v77.0.0 发布，核心变化包括 CSS-only 规则迁移、旧 flat 配置移除、28 条新规则、非 JavaScript 语言推荐预设，以及大量规则增强与修复。

- 📦 **版本发布**：v77.0.0 为最新版，自上一版以来包含 16 个提交。
- 🚨 **破坏性变更**：CSS-only 规则迁移到 `eslint-cssicorn`，如 `unicorn/no-deprecated-css-features` → `cssicorn/no-deprecated-features`。
- ⚙️ **配置移除**：弃用 `flat/recommended` 和 `flat/all`，改用 `recommended` 和 `all`。
- ✨ **新增规则**：共 28 条，覆盖安全/正确性，如 `no-invalid-response-options`、`no-prevent-default-in-passive-listener`、`no-invalid-boolean-attribute-value`、`no-conflicting-constraints`、`no-invalid-property-descriptor`、`no-invalid-url-protocol-comparison`、`no-invalid-integrity`、`no-url-in-search-params`、`no-invalid-dom-token`、`require-text-decoder-streaming`、`no-invalid-temporal-arithmetic` 等。
- 🎨 **风格新规则**：包括 `comma-spacing`、`indent`、`no-empty-link-text`、`no-leading-empty-lines`、`no-loss-of-precision`、`prefer-promise-static-methods`、`prefer-literal-ascii`、`prefer-short-escape-sequences`、`key-name-casing` 等。
- 🌐 **多语言预设**：新增 `recommended-css`、`recommended-html`、`recommended-json`、`recommended-markdown`、`recommended-toml`、`recommended-yaml`。
- 🧩 **规则语言扩展**：多个规则支持 JSON、CSS、HTML、Markdown、YAML、TOML，如 `consistent-compound-words`、`empty-brace-spaces`、`escape-case`、`name-replacements`、`no-zero-fractions`、`number-literal-case`、`string-content`。
- 🛠️ **行为改进**：`eslint-disable` 注释现在抑制报告，而不是让规则跳过代码，避免误判未使用。
- 📄 **文档注释规则**：`no-asterisk-prefix-in-documentation-comments` 支持 CSS/JSON，并加入 `recommended` 预设。
- 🎯 **预设调整**：`number-literal-case` 从 `unopinionated` 移至 `recommended`。
- 🔧 **其他增强**：多项规则增加选项、提升性能、修复类型推断和减少误报，如 `prefer-combined-guards`、`prefer-simplified-conditions`、`comment-content`、`no-invalid-argument-count`、`prefer-direct-iteration`、`prefer-single-call` 等。
- 👍 **社区反馈**：获得 👍2、🎉3、❤️1、🚀1、👀1，共 5 人反应。

---

### [错误](https://github.com/mapbox/pixelmatch)

**原文标题**: [Error](https://github.com/mapbox/pixelmatch)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='github.com', port=443): Max retries exceeded with url: /mapbox/pixelmatch (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [](https://humanwhocodes.com/blog/2026/09/introducing-pr-comment-inbox/)

**原文标题**: [Introducing PR Comment Inbox - Human Who Codes](https://humanwhocodes.com/blog/2026/09/introducing-pr-comment-inbox/)

PR Comment Inbox 是 Nicholas C. Zakas 于 2026 年 9 月 30 日介绍的开源工具，帮助 PR 作者在评论繁多的 GitHub 拉取请求中系统追踪、分类和回复对话，灵感来自 Outlook/Gmail 式收件箱。

- 😫 作者长期不满 GitHub PR 界面：更适合小改动，大型 PR 评论多时加载慢、难管理，顶级评论回复难以追踪，Conversations 标签还会隐藏评论和线程。
- 💡 在又一次 PR 迅速积累 90 条评论后，作者决定用 AI 构建自己想要的解决方案。
- 📥 PR Comment Inbox 的核心是左侧窗格列出“对话发起项”：任意行内评论、不以 @ 开头的顶级评论、PR 描述本身。
- 🧵 点击左侧项后，右侧显示线程及上下文，可回复、应用建议和解决线程。
- 🔗 顶级评论线程采用基于 @ 提及的启发式：用户首条非 @ 评论成为入口，该用户其他非 @ 顶级评论归入同一线程。
- 📝 以 @ 开头的评论嵌套在被提及用户最近的前序评论下；PR 描述被视为第一条评论，作者相关讨论归入其中。
- ✅ GitHub API 不提供已读追踪，因此工具用 localStorage 实现读/未读模型；已读不等于已解决，已读线程移出收件箱，直到标为未读或出现新评论。
- 🆓 工具免费开源，已发布在 GitHub，并提供在线演示；最初是给 GitHub 的 demo，后决定公开分享。
- 🎯 作者仍希望 GitHub 原生支持顶级评论线程和类似界面，短期则希望该工具帮助高流量 PR 作者。
- 🚀 作者已将其纳入日常流程，认为在处理评论繁多的 PR 时更高效、更少疲惫。

---

### [发布 v8.0.1 · electron/forge · GitHub](https://github.com/electron/forge/releases/tag/v8.0.1)

**原文标题**: [Release v8.0.1 · electron/forge · GitHub](https://github.com/electron/forge/releases/tag/v8.0.1)

overview summary
Electron Forge 发布 v8.0.1（Latest），汇集从 v8.0.0 alpha 到 8.0.1 的大量变更，核心是 Node 22/ESM、Yarn 4、Vite/Webpack 现代化、CLI 与模板重构、makers/publishers 修复，并为 Forge 8 正式进入 main 做准备。该版本由 electron-npm-package-publisher 于 29 Sep 20:33 发布，提交 48f38bb 通过 GitHub GPG 验证；完整对比 v7.10.2...v8.0.1，含 2 个 assets，贡献者包括 claude、VerteDinde 等 7 人，新贡献者 @0xlau。

- 🚀 v8.0.1 为 Latest 版本，完成 8.0.0 与 8.0.1 的版本提升，并准备将 next 分支提升为 main 作为 Forge 8。
- 🧱 CI/构建现代化：Yarn 4 CI 强化、Yarn 4.18、TypeScript 7 stable、Windows 构建优化、npm trusted publishing 与 .nvmrc。
- ⚙️ 重大运行时升级：迁移到 Node 22 + ESM，升级 Electron 44.4.3，移除 Forge 5 导入代码并处理 Electron 44 丢弃的架构。
- 🧹 破坏性清理：移除全局模块模板与 rechoir/lodash 模板，将 init/import 从 core 移至 create-electron-app。
- 🛠️ CLI/init 增强：新增 --electron-version 与 --package-manager 标志，改进 TTY 检测、交互模式信号代理、重复重启防护与依赖安装错误提示。
- 🧪 测试体系：升级 Vitest 4，使用 Verdaccio 进行 e2e init，覆盖全模板/包管理器，并分片慢测试、修复 Electron 相关临时目录清理。
- ⚡ Vite 插件：生产构建放入隔离子进程，升级 Vite 8，支持主进程热重启与自定义 renderer dev server host，并从实验性毕业。
- 📦 Webpack 插件：ESM 兼容导入，升级 webpack-dev-server，使用 ink 多日志器展示编译输出。
- 🍎 Makers：MakerPKG 增加公证并写 arch 子目录，MakerDMG 写 platform/arch 子目录，MSIX/APPX 修复输出名、版本与架构，APPX 变为 MSIX 的 legacy wrapper。
- 🐙 Publishers：GitHub publisher 支持字节级上传进度，Github 更名为 GitHub，避免多次 dry run 产生重复草稿发布。
- 🔁 发布流程变更：publish 命令重命名为 release，release --from-dry-run 改为 --from-make，make --skip-package 改为 --from-package。
- 🧩 模板与代码质量：统一 JS/TS 模板，采用 moduleResolution: bundler 与 .mts Vite 配置，用 oxc/oxlint/oxfmt 替换 eslint/prettier，增加 knip 死代码检测。
- 📚 文档与治理：从 electron-forge-docs 导入文档，添加 AGENTS.md，移除 Discord 链接，并进行多项依赖安全与去重更新。
- 👥 贡献信息：新贡献者 @0xlau；贡献者包括 claude、VerteDinde 等 7 人，发布资产 2 个。

---

### [发布 v2.13.0 · reduxjs/redux-toolkit · GitHub](https://github.com/reduxjs/redux-toolkit/releases/tag/v2.13.0)

**原文标题**: [Release v2.13.0 · reduxjs/redux-toolkit · GitHub](https://github.com/reduxjs/redux-toolkit/releases/tag/v2.13.0)

Redux Toolkit v2.13.0 已发布，这是一次功能版本，重点包括构建工具全面现代化、官方支持 TypeScript 7，以及针对 RTK Query、createAsyncThunk、createEntityAdapter 和 combineSlices 的大量修复；同时文档合并为统一站点，包布局与导出 API 保持兼容。

- 🚀 **版本发布**：v2.13.0 为最新功能版本，包含自 v2.12.0 以来的多项更新与修复。
- 🛠️ **构建工具更新**：从 Yarn 迁移到 PNPM，ESLint 迁移到 Oxlint，Prettier 迁移到 Oxfmt，TSUp 迁移到 TSDown；包布局、exports 和 API 与 2.12 不变，CJS/ESM/legacy-esm 入口均已验证，并支持 pkg.pr.new 预览。
- 📚 **文档更新**：推出统一 Redux 文档站，redux.js.org 现在覆盖 Redux 核心、Redux Toolkit、React Redux 和 Reselect；旧独立站点重定向，内容去重并现代化，RTK 文档位于 /toolkit/。
- 🧠 **TypeScript 7 支持**：适配 TS 7.0/7.1 并纳入 CI；支持矩阵更新为 TS 5.6+，更早版本不再测试。
- 🔧 **RTK Query 修复**：useQuery/useQueryState 选择器已记忆化并移除渲染期直接读 store；修复 isSuccess 在错误后重取时误变 true、data 不反映 updateQueryData、轮询状态读取、重复查询拒绝导致标签失效丢失、falsy tag id、懒查询重订阅、无限查询 onQueryStarted、fetchBaseQuery 绝对 URL 判断等问题。
- 🐛 **其他修复**：createAsyncThunk 不再吞掉 pending 前 abort，并正确设置 falsy rejectWithValue 的 rejectedWithValue；createEntityAdapter 的 setAll/updateMany 行为修正；combineSlices 状态代理缓存按实例隔离；immutability middleware 支持循环引用；dynamic middleware 缓存未变中间件链。
- 👥 **贡献者**：由 markerikson、chatman-media 及另外 14 位贡献者参与，完整变更集为 v2.12.0...v2.13.0。
- 👍 **反馈**：发布获得多枚点赞、爱心和火箭反应；如遇疑似构建相关行为差异，建议提交 issue。

---

### [Mozilla 嘉年华 - Mozilla 基金会](https://www.mozillafoundation.org/en/festival/?utm_medium=paid&utm_source=newsletter&utm_campaign=26-mozfest&utm_content=ad_javascript-weekly&utm_term=cooperpress)

**原文标题**: [
            
                
                    Mozilla Festival
                
            
            
                
                - Mozilla Foundation
            
        ](https://www.mozillafoundation.org/en/festival/?utm_medium=paid&utm_source=newsletter&utm_campaign=26-mozfest&utm_content=ad_javascript-weekly&utm_term=cooperpress)

提供的内容仅为关键词“Debates”（辩论），没有附带正文或上下文，因此无法提炼具体文章要点；以下仅对该关键词作最简要概括。

- 🗣️ “Debates”中文通常译为“辩论”，指围绕特定议题进行的有组织观点交锋。
- 📌 核心特征包括不同立场、论证与反驳、试图说服听众或裁决者。
- 🧩 由于原文只有该词，缺少主题、背景、论点和结论，无法生成更详细摘要。
- ✅ 如需有效总结，请补充完整文章或更多上下文。

---

### [](https://trigger.dev/?utm_source=fnf&utm_medium=newsletter&utm_campaign=september&utm_term=js-weekly&utm_content=homepage)

**原文标题**: [Trigger.dev | The open source platform for durable AI agents](https://trigger.dev/?utm_source=fnf&utm_medium=newsletter&utm_campaign=september&utm_term=js-weekly&utm_content=homepage)

Trigger.dev 是一个开源平台，用于在 TypeScript 中构建和部署持久耐用的 AI 智能体与工作流，支持长时间运行任务、重试、队列、AI 可观测性和弹性伸缩。

- 🚀 开源 TypeScript 平台，专为构建持久 AI 智能体设计，支持长时间运行、重试、队列和弹性伸缩
- 🤖 核心能力包括 AI 智能体、媒体处理与生成、人在回路、流式传输、Python 运行、浏览器自动化、定时任务、并发与语义搜索
- 💬 提供 `chat.agent` 示例，展示工具调用、人类审批暂停、流式响应及 15 步推理限制
- 🔄 任务可经受刷新、重新部署和崩溃，无需 API 路由即可流式传输至前端，并具备完整可观测性
- 🧩 支持多种智能体模式：自主智能体、提示链、路由、并行化、编排器和评估优化器
- ⏱️ 无超时限制、按使用付费、无需管理服务器，部署与扩展自动化
- 🛠️ 提供错误告警、高级过滤、版本管理和原子部署，确保任务不受代码变更影响
- 📡 Realtime API 可实时显示任务状态和元数据，并支持将 LLM 响应流式传输到前端
- 🐍 运行时自由度高，支持 Python、Prisma、Puppeteer、esbuild、FFmpeg、apt-get 及自定义构建扩展
- 🧰 开发与生产工具齐全：持久 cron、React hooks、MCP 服务器、批量触发、多区域 worker、静态 IP、私有链接、并发队列、检查点等
- 🔁 默认可靠：支持任务重试、条件重试、细粒度重试、请求重试和配置文件默认重试
- 🌍 兼容现有技术栈，Apache 2.0 开源许可，可自托管，GitHub 星标超 16.5k，Discord 社区超 5.1k 成员
- 🗣️ 获得 Supabase、Arena、Magic Patterns、MagicSchool AI、Cal.com 等众多开发者和团队好评
- 🆕 最新更新包括 Ask Trigger 仪表盘聊天调试、预览分支自动归档、并发指标与队列健康、主题与无障碍选项

---

### [](https://2026.stateofdevs.com/en-US/)

**原文标题**: [State of Devs 2026](https://2026.stateofdevs.com/en-US/)

概述总结
- 📅 调查时间为2026年7月5日至9月5日，共5,463名受访者；年度综述由Software Stewardship Lab创始主任兼研究员Miranda Heath撰写。
- ⚠️ 开发者普遍处于不确定时期：近半数经历工作不安全和薪资不足，四分之一曾在职业生涯中被裁员，近十分之一在过去9个月被裁员，超四分之一预计5年内需转行。
- 🧠 心理状态令人担忧：约三分之二近期缺乏工作动力、变得愤世嫉俗；约半数难以专注、拖延增加、异常疲惫、成就感和工作效率下降。
- 🔥 62%的开发者曾在职业生涯中经历倦怠，与去年持平；经历倦怠者通常更不快乐，更容易出现持续的身心健康问题。
- 💼 职场问题普遍：包括糟糕管理、倦怠、工作与生活失衡、无聊、工作不安全、心理健康问题、薪资不足、骚扰和歧视。
- 🤖 对AI看法两极分化：49%受访者持正面态度，42%持负面态度；AI使用很普遍，但近半数认为AI未对其心理状态产生积极影响。
- ⚡ AI风险初现：提示可能令人上瘾，过度依赖AI可能削弱学习，并行运行代理可能导致“AI脑力过载”；超1500人留言讨论AI影响。
- 🗣️ AI讨论焦点：如何安全合理使用AI、AI让工作回报感降低、管理层因AI产生不可持续的生产力期望。
- 🚧 长期问题仍在：女性更易遭遇职场歧视，也更可能回避同事、改变行为或外表，甚至转行；LGBT+、ADHD和自闭症受访者常感到需隐藏身份或伪装，增加倦怠风险。
- 😮‍💨 对科技行业情绪复杂：最常见情绪为疲惫、幻灭、好奇、不堪重负、焦虑、希望、愤怒和兴奋。
- 🌪️ 结论：当前开发者处境像身处沙尘暴，前路难辨；但若持续对话AI影响、工作中带来快乐与意义的部分，尘埃落定后或许能看到更美的风景。

---

### [](https://2026.stateofdevs.com/en-US/ai/)

**原文标题**: [State of Devs 2026: AI](https://2026.stateofdevs.com/en-US/ai/)

2026 年 AI 已深度融入开发者工作流：中位开发者约 63% 的代码由 AI 生成，几乎全用 AI 编码者成为最大单一群体；同时开发者对 AI 的情绪复杂，整体偏中性/正面，但环境、岗位、心理与行业影响等担忧显著。

- 🤖 AI 代码生成：中位约 63% 代码由 AI 生成；87.5% AI 生成比例人数最多（1,009），几乎全 AI 编码成最大群体。
- ⚖️ AI 情绪：总体意见中位数为 50%（中性）；“正面”最多（1,087），但负面与强烈负面也不少；亲 AI 与整体技术乐观及右翼立场相关。
- 🌍 AI 风险：环境影响居首（2,664），其次岗位替代（2,653）与 AI 垃圾内容泛滥（2,297）；环境担忧与左翼立场相关。
- 🏢 公司 AI 立场：中位为“鼓励 AI 但不影响我的行为”（2,421）；1,402 人因公司鼓励而更多使用 AI；但配额或排行榜可能损害幸福感与心理状态。
- 🧠 AI 心理状态：整体偏不同意“AI 对心理状态有积极影响”（中位数 2）；1,023 强烈不同意、1,189 不同意；负面者常感疲惫与幻灭，正面者多感好奇但仍可能不堪重负。
- 💬 AI 前景自由回答：最热主题是开发者影响（428），其次反 AI 情绪（403）、行业影响（337）、亲 AI（302）、中立（265）。
- 🧭 其他关注：AI 职业影响（237）、技术影响（206）、伦理影响（105）、环境影响（66）、代码辅助（48）、信息收集（22）。
- 📊 总体：AI 生产力红利明显，但情绪与风险分化；开发者最在意个人处境与行业生态如何被 AI 改变。

---

### [](https://2026.stateofdevs.com/en-US/hobbies/)

**原文标题**: [State of Devs 2026: Hobbies](https://2026.stateofdevs.com/en-US/hobbies/)

调查汇总了受访者在爱好、运动、饮品、书籍、电子游戏及平台方面的偏好，突出各榜单前列、群体差异与排名变化。
- 🎮 爱好榜：视频游戏以 2,907 票居首，接着是电影/电视、阅读、运动/锻炼；阅读在女性和 60 岁以上群体中排第一。
- 🥾 运动榜：徒步/步行第一（1,946），力量训练第二（1,617）；以色列 30% 做力量训练，法国仅 12%，荷兰在攀岩上领先。
- ☕ 饮品榜：咖啡第一（3,287），茶第二（2,024），汽水/软饮、气泡水、啤酒紧随其后。
- 📚 书籍榜：Dungeon Crawler Carl 第一（165），Project Hail Mary 第二（152），其后有 Dune、The Bible、1984 等。
- 🕹️ 游戏榜：Clair Obscur: Expedition 33 第一（164），Minecraft 第二（160），Baldur's Gate 3 降至第三（125）。
- 🖥️ 平台榜：PC 第一（2,494），Switch 第二（1,159），Playstation 第三（915）；macOS、iOS、Steam Deck 均呈上升。
- 🎸 另类数据：受访者中 Pink Floyd 听众的中位年龄为 47 岁。

---

### [](https://2026.stateofdevs.com/en-US/workplace/)

**原文标题**: [State of Devs 2026: Workplace](https://2026.stateofdevs.com/en-US/workplace/)

这份开发者调查聚焦薪资、公司规模、求职渠道、远程办公、满意度与身心健康，显示经验、公司规模和美国地区仍是高收入核心因素，同时管理问题、倦怠和收入增长趋势值得关注。

- 💰 高收入三大预测因素：更多经验、加入更大公司、在美国工作；全体年薪中位数 $90,000，美国相关薪资指标 $105,000。
- 📈 美国薪资最高，但在“收入增长比例”上仅排第 11；北欧及邻国领先，未来薪资排名可能变化。
- 🏢 大公司仍与更高收入和涨薪相关，过去一年 62% 大公司员工收入增加；自由职业者工时更少、AI 使用更少且态度更负面，但收入更低。
- 🧑💻 “工程师”头衔比“开发者”中位薪资高约 $65,000；Software Engineer 最常见，Developer 次之，前端开发仍是主要工作内容。
- 🧩 工作领域与经验和收入强相关；AI、平台工程、招聘/面试高于趋势线，通常对应更高收入。
- 📨 找到当前工作中位投递 4 份申请；经验越多，平均所需申请越少。
- 🤝 通过开源/社区找工作的收入比整体中位数高 39%；个人网络、直接申请比 LinkedIn/招聘板更高效。
- 🏠 缺乏远程办公与更低收入和更低工作满意度相关；完全远程公司员工中位数仅 35 人。
- ⏰ 每周工时中位数 40 小时；工时与薪资相关性受经验、公司规模等影响，在 10-14 年经验的美国开发者中几乎消失。
- 😊 工作满意度中位数 4/5，多数开发者满意，但不满比例较去年略升。
- 🧑🤝🧑 最受重视的职场福利是同事关系、工作生活平衡和工作条件，高于薪酬。
- ⚠️ 最大职场困难是管理不善，其次薪酬；管理不善作为新增选项直接登顶。
- 🧠 倦怠普遍，受访者平均勾选 4.5 项迹象；最常见为工作动力/兴趣下降、愤世嫉俗、情绪耗竭。
- ⌨️ 键盘偏好：苹果键盘最多（1150），机械键盘（1018）和 Logitech（624）紧随其后，仍有不少人使用笔记本键盘。
- 🖥️ 显示器使用中位数为 2；2454 人用双屏，1426 人仅用一屏。

---

### [IANA 关于 example](https://www.oliverdunk.com/2026/09/30/iana-reply)

**原文标题**: [IANA's email about why example.com changed | Oliver Dunk](https://www.oliverdunk.com/2026/09/30/iana-reply)

IANA 副总裁回复了关于 example.com 内容变更的询问，解释调整主要为了降低带宽需求、提升实用性；该域名本质上是文档示例占位符，并非通用服务端点。

- 📧 作者当天致信 IANA 询问 example.com 新内容，意外收到 IANA 副总裁 Kim Davies 的回复。
- 🌐 IANA 对网站内容的调整通常是为了降低整体带宽需求或提升实用性。
- 🧩 example.com 本质上是“没人应访问的站点”的占位符，但历史上会显示说明，告知访客域名已注册及其用途。
- ⚙️ 由于流量很高，本周把页面拆成更基础页面，并用单独的 JavaScript 文件加载额外内容，以减少带宽消耗。
- 🤖 大多数访问是自动化流量，通常不会获取 JavaScript 文件，因此整体数据需求下降。
- 📄 该域名主要用于文档中的示例，例如说明书里的示例内容；有人复制示例配置却忘记替换 example.com，会带来附带流量。
- 🚫 它并非用于可用性测试等通用目的端点，IANA 不鼓励此类使用；也不要求主机必须提供 HTTP 服务，只是出于礼貌维持。
- ✅ Kim Davies 表示这些信息可自由使用和转发，邮件日期为 2026 年 9 月 30 日。

---

### [](https://www.debugbear.com/blog/example-dot-com-redesign-history)

**原文标题**: [Example.com Just Launched The Biggest Redesign In Decades | DebugBear](https://www.debugbear.com/blog/example-dot-com-redesign-history)

example.com 是 IANA 保留的文档示例域名，自1999年前后上线以来长期保持简单页面；2026年9月28日它迎来数十年来最大改版，加入多语言展示和逐字动画，随后又快速取消动画。文章同时回顾了该站20多年来的文案、设计、基础设施与用途说明变化，并强调它并非可靠服务，不应被用于测试或监控。

- 🌐 example.com 是 IANA 保留域名，主要供文档和示例使用，自上世纪90年代末起可用。
- 🚀 2026年9月28日大改版：从静态英文页变为 JavaScript 多语言页，每5秒轮换英语、阿拉伯语、中文、法语、俄语和西班牙语，并插入 SVG 书本图标。
- ✨ 语言切换动画采用逐字符透明度过渡，每个字符包在 span 中，并通过递增的 CSS transition-delay 实现，基础动画为 transition: opacity .4s。
- 🛑 2026年10月3日又移除动画，改为页面一开始就显示所有语言。
- 🗣️ IANA 声明称，改版主要为了降低带宽需求并提升实用性：页面拆成基础页和额外 JavaScript 内容，自动流量通常不会抓取 JS，从而减少数据传输。
- 📜 1999年上线；Wayback Machine 最早版本为2002年1月20日，使用表格布局、ICANN 标志、Apache 1.3.22，仅列出保留域名。
- ✏️ 2002年3月28日出现现代版文案；2003年2月7日加入 RFC 2606 链接，并升级服务器环境。
- 🕰️ 2010年7月30日加入 example.edu；2011至2013年间曾重定向到 IANA 页面；2013年7月29日恢复自有页面并迁移到 EdgeCast CDN，同时进行卡片式重设计。
- 🔤 2019年10月17日更新字体栈和文案；2025年1月15日 Server 响应头消失；2025年10月9日去掉卡片设计、压缩 HTML；2025年12月17日迁移到 Cloudflare。
- 🧩 2026年6月9日添加空 favicon（data:,）并闭合 p 标签，以减少浏览器对 favicon 等不必要请求。
- ⚠️ 文章提醒不要依赖 example.com 做可用性测试或 HTTP 监控；它并非稳定服务，偶尔会响应异常，使用自有基础设施更可靠。
- 📈 结论：example.com 的改动不定期发生，有时连续数月小改，有时长达七年不变；文章还提到 DebugBear 用于监控页面速度和 Core Web Vitals。

---

### [](https://www.netlify.com/blog/edge-functions-firecracker-microvms/)

**原文标题**: [5x faster Edge Functions: v8 isolates to Unikraft MicroVMs](https://www.netlify.com/blog/edge-functions-firecracker-microvms/)

overview summary
- 🚀 Netlify 已将 Edge Functions 从旧托管执行服务/V8 isolates 迁移到自有边缘网络中的 Unikraft MicroVMs，温暖调用中位数约 5–6ms，较旧架构 25–40ms 快约 5 倍。
- 📊 关键指标：p99 调用快 47.4%，可用性 99.998%，边缘函数日志投递快 5 倍；冷启动约 1.2%，平均约 9ms。
- 🧭 请求路径：最近边缘节点终止 TLS 并匹配路由；未命中继续缓存/源站，命中则转发到内部计算节点，不再离开 Netlify 网络。
- 📦 每个请求携带机器规格（运行时、平台、函数镜像及 CPU/内存/连接限制），规格哈希与站点信息生成 service ID，确保不同部署隔离。
- 🔒 不同代码或环境变量的部署永不共享 MicroVM，隔离强于 V8 isolates，可防止被攻破部署污染其他客户或计算层。
- 🎯 计算节点用 rendezvous hashing 固定服务以保持热实例和缓存；超过阈值后分散到多节点，避免单节点热点。
- 🖥️ 函数运行在 Firecracker MicroVM：创建 <1ms、p99 启动约 2ms；EROFS 镜像内存映射、空闲缩零、从快照恢复。
- 🤝 Unikraft 负责 VM 生命周期（启动、快照、恢复、缩零），并与 Netlify 合作验证正确性和高请求量下的表现。
- 🛠️ 计算节点使用本地 DNS 解析器，增强指标（启动时间、首端口开放、用户代码启动），并设置熔断器快速重路由/下线。
- 🧱 控制平面跟踪健康计算节点；部署时新舰队并行启动并在健康后接管流量。
- ✅ 对用户无迁移/代码变更：URL imports、npm、Node 内建、netlify.toml、本地开发照旧，价格不变。
- 🔓 自有计算提升上限：让 npm 包支持脱离 beta 更可行，重新审视 50ms CPU/512MB 内存/20MB 压缩代码限制，并可构建依赖自有网络路径的能力。

---

### [](https://earendil.com/posts/pi-1-0/)

**原文标题**: [Pi 1.0 | Earendil](https://earendil.com/posts/pi-1-0/)

概述总结
- 🚀 2026 年 10 月 1 日，Earendil 正式发布 Pi 1.0：一个加固、极简、可扩展、可自定义的 agent harness。
- 👥 Pi 每周被全球数十万人使用，社区 issue 和 PR 推动其改进、加固，并成为稳定可依赖的软件。
- 🧭 坚持极简路线：等待特性被证明后再采纳，并权衡真实功能与额外复杂度。
- ✨ Pi 1.0 新增：Codemode（原生 MCP、Jev 等非 LLM 模型与图像模型）、虚拟模型扩展、延迟工具加载、Anthropic 缓存预热、对话中系统消息、新 TUI 主题、默认全屏模式。
- 🧱 这些功能经过数月打磨，仍让 Pi 保持简单。
- 🧪 同时发布实验包 Pi Durable，面向长时运行的 agentic 应用，让 AI 走出编码代理和终端。
- 🌀 Pi Durable 延续极简与超可塑性，并扩展为可构建、可操控、支持更长对话与任务的新基底。
- 🏢 Earendil 的目标是打造增强人类能动性的软件与开放协议。
- 📦 Pi 1.0 安装：`curl -fsSL https://pi.dev/install.sh | sh`；Windows：`powershell -c "irm https://pi.dev/install.ps1 | iex"`。
- 🧩 Pi Durable 安装：`npm install @earendil-works/pi-durable @earendil-works/pi-ai @earendil-works/chord`。
- 📜 两者均为 MIT 许可，文档见 pi.dev，代码见 github.com/earendil-works/pi。
- 💡 示例：Codemode 用脚本总结一周提交；虚拟模型用 Claude Opus 规划、GPT 实现、Jev 决定切换；支持 router/auto 与 /session 成本/缓存分析。

---

### [](https://earendil.com/posts/pi-durable/)

**原文标题**: [Pi Durable | Earendil](https://earendil.com/posts/pi-durable/)

Earendil 与 Pi 社区于 2026 年 10 月 1 日发布 Pi 1.0，并推出实验性新包 Pi Durable。Pi Durable 是面向长期运行、持久、可塑 agent 的 harness/框架，可在任何有 JavaScript 运行时的地方运行，支持崩溃恢复、多对话、多人协作与运行中热更新；它不替代 Pi coding agent，而是共享极简与可塑原则，用于构建各类 agentic 应用，经验会回流。

- 🚀 Pi 1.0 发布，标志经过大量加固、维护与开发后，Pi 成为稳固基础；Pi Durable 同时作为实验包发布。
- 🧭 Pi Durable 为长期、持久、可塑 agent 设计，可运行在任何 JS 运行时；不取代 Pi coding agent，其探索经验会回流。
- 🧱 harness = 存储 + 并行运行一个或多个 LLM 对话的机制，提供工具和执行环境；对话是 transcript，一切运行单元是 task。
- 📦 源码约 15,000 行（无测试），约 150k GPT/250k Claude tokens，便于 agent 理解；存储后端约 3,000 行可跳过。
- 💾 存储支持 memory、SQLite、JSONL，并有一致性套件与基准；SQLite/JSONL 不依赖 Node API，可适配 Bun 或 Cloudflare Durable Object。
- 🧠 SQLite 下仅内存保留工作集，其余在磁盘；活跃 transcript 受上下文窗口和压缩限制，长对话仍可放入内存。
- 🖥️ 执行环境接口小，内置 Node 环境访问本地文件，也可远程；env 按对话工作目录构建，允许 harness 与工具异机运行。
- 🛡️ 每步 task 先写 checkpoint；进程死亡后新进程恢复未完成任务，模型请求重发，安全工具重跑，否则通知模型中断。
- 🔁 requestId 让提交 exactly-once，客户端崩溃后重试会拿回原提交，不会重复请求。
- 🗂️ 一个 harness 可并发运行多对话，支持从 transcript 任意点 fork 且不复制历史；示例 Slack 频道与线程可同时运行。
- 🤖 每个对话独立保存 agent 配置：模型、思考级别、扩展/工具选择、额外指令、执行环境工作目录。
- 🧩 扩展是命名 bundle，含系统提示 sections、tools、hooks、tasks；应用安装到 registry，对话只存名称。
- 📝 系统提示每次请求前重建，变更记录在 transcript 对应位置；重启/fork 看到一致内容，中途变更只发变更以保持 prompt cache。
- 🛠️ 工具调用是独立 durable task，先存意图；按 replay 安全策略决定崩溃后重跑或报告中断；工具 API 可创建子对话，几行实现 subagent。
- 🪄 工具可覆盖或包装：同名后安装者替换，wrap 装饰最终工具，例如统一计时 bash。
- 🪝 hooks 可介入模型请求、工具调用、压缩等任务，改写、阻止、替换、继续或摘要；崩溃后重跑用 memo 保存决策。
- ⛓️ 多扩展 hooks 按选择顺序成链；beforeTool/afterTool/onYield/afterResponse 规则不同，异常处理不同。
- ✅ tasks 内置模型请求、工具调用、压缩，也支持自定义；每步 checkpoint、持久定时器、等待其他任务；任务/对话构成所有权树，中止递归清理。
- ⏱️ 前景任务属于当前工作，对话等待且 Esc 中止；后台任务不阻塞对话，普通中止不影响，适合子代理或提醒。
- 💳 任务示例：多卡支付 charge 幂等，失败 abort 退款；checkout 用 failFast 等待所有支付。
- 🗜️ 压缩后台运行，接近限制时摘要旧消息并放在回合边界；必要时等待或压缩重试；可手动压缩，旧消息保留。
- 🔄 reset 可开新上下文并支持 handoff note；工具可请求 handoff，旧消息仍可通过 search_history 搜索。
- 📄 应用状态存为 documents（typed JSON），与 transcript 同一原子提交；fork 可选 asOf/current/fresh，保证状态一致。
- ♻️ registry 运行中可改，同名安装替换；运行中工具调用用旧代码完成，下一次用新代码，重启后加载新安装。
- 👥 多客户端可同时附加对话，先拿当前视图再收变更；可 steer 或排队 follow-up；远程用 watch() 发送提交操作，watchEvents() 转熟悉事件。
- 🧪 可立即试用但 API 可能变；提供 packages/durable、README、30+ examples、小型 coding agent、约 1,300 行 vacation planner、demo 命令和 npm 安装包。
- 🗣️ 未来几周将展示 Slack bot、GitHub triage bot 等工具；FAQ 称当前选 TypeScript 因易启动，未来可能移植 Rust 或汇编。

---

