### [npkill 1.0：现代开发吃掉了你的磁盘](https://zaldih.com/en/post/npkill-1-0-0/)

**原文标题**: [ npkill 1.0: modern development ate your disk](https://zaldih.com/en/post/npkill-1-0-0/)

npkill 1.0 正式发布，标志着这款工具从清理 `node_modules` 的小脚本，升级为面向“现代开发”产生的多种重型目录的磁盘清理工具。新版本引入 profiles（配置档）、多选、结果过滤、`.npkillrc`、JSON 模式，并将核心与 CLI 重构分离；普通用户仍可用 `npx npkill` 保持基本用法，但存在多项破坏性变更。

- 🚀 历经 7 年、45 个版本后发布 1.0，目标从单一 `node_modules` 扩展到更广泛的开发缓存与构建产物。
- 🧩 默认使用 `node` profile，不再只有单一 target；支持 `-p node,python`、`-p all`，内置约 20 个 profiles，并支持自定义。
- 🛡️ 敏感结果默认隐藏；对 `target`、`.venv` 等通用名称结合上下文判断，减少误删风险，且不会未经确认自动删除。
- 🖥️ 新增 Help、Options、Delete、Info 面板，可用左右键切换；Options 面板可实时修改参数并自动重启搜索。
- ✅ 新增多选模式：按 `t` 开启，空格选择/取消，Enter 删除，`a` 全选，`v` 范围选择。
- 🔎 支持按 `/` 过滤结果，可按类型、路径甚至正则筛选，并能与多选模式组合批量清理。
- ⚙️ `.npkillrc` 可配置 `rootDir`、`defaultProfiles`、自定义 profiles、`exclude`、`sortBy`、`sizeUnit` 等；优先级为配置文件 < CLI 启动参数 < 面板临时修改。
- 📊 新增结果计数、滚动条、`--json` 与 `--json-stream` 模式，便于脚本、CI 或 cron 使用；`--delete-all` 仅配合 `--targets`，建议先用 `--dry-run`。
- 🧱 内部重构为 core 与 cli 分离，开放 core API 供自定义实现和自动化，但 API 仍可能在后续小版本中变化。
- ⚠️ 破坏性变更包括：`--target` 改为 `--targets`；默认 `node` profile 会匹配 `.next`、`.nx`、`.angular`、`coverage` 等；旧行为可用 `-t node_modules`；移除 `-x`、`--bg-color`、`-nu`、`-gb`；`--sort last-mod` 改为 `--sort age`；要求 Node.js 20.19+。
- ⚡ 其他改进包括搜索最高快 3 倍、新增 `--no-size`/`--no-age`/`--no-stats`、`--older-than`、自动 MB/GB 单位、修复非 TTY 环境与 Android 问题等。
- 💬 作者强调不想改变用法的用户仍可只清理 `node_modules`，并感谢多年社区反馈、问题报告与贡献。

---

### [npkill — 清理你的磁盘空间](https://npkill.js.org/)

**原文标题**: [npkill — Clean up your disk space](https://npkill.js.org/)

npkill 1.0 是一款开源 CLI 清理工具，用于查找并删除系统中的 node_modules、构建产物和缓存目录，以释放磁盘空间；它支持多种语言/框架配置、交互式浏览与批量删除，并获得社区积极反馈和资助。

- 🧹 核心功能：扫描并删除 node_modules、构建产物及缓存目录，回收数 GB 磁盘空间。
- 🚀 快速使用：运行 `npx npkill` 即开始扫描。
- 🗂️ 多项目支持：内置 Node、Python、Rust、PHP、Java、Unity、Godot、Dart 等配置，并可 Ctrl+单击多选。
- 🧭 交互操作：用 ↑/↓ 浏览结果，按 → 查看详情。
- 🗑️ 删除方式：按 Del 删除，按 t 多选并批量删除。
- 💬 社区认可：用户分享清理约 10.59 GB、13.45 GB、34.45 GB 等案例，称其有效释放 SSD 空间。
- 🌍 开源项目：由 voidcosmos 团队及贡献者维护，提供 GitHub、npm、文档与问题反馈入口。
- 💖 社区支持：项目获得社区捐款与赞助支持。

---

### [工作原理](https://www.meticulous.ai/how-it-works?utm_source=javascript_weekly&utm_medium=newsletter&utm_campaign=26q4_1&utm_content=primary)

**原文标题**: [How it Works](https://www.meticulous.ai/how-it-works?utm_source=javascript_weekly&utm_medium=newsletter&utm_campaign=26q4_1&utm_content=primary)

Meticulous 是一个面向开发者和 AI Agent 的全自动端到端测试平台，通过真实交互记录、静态分析和并行浏览器执行，在合并前展示代码变更对现有流程、边缘情况、视觉与行为的影响。

- 🚀 **三步流程**：安装、执行、审查，帮助团队在合并前全面了解变更影响。
- 🧠 **自动构建会话库**：记录开发者与 Agent 的真实日常交互，持续补充并维护覆盖各类边缘情况的测试会话。
- 🔌 **CI 与 MCP 集成**：安装 CI 集成和 MCP Server，允许 PR/MR 评论、触发测试和读取结果；建议在内部环境加入脚本标签以捕获更多工作流。
- 🔍 **静态分析定位影响范围**：针对每次代码变更追踪完整影响链，找出可能受影响的边缘情况并执行对应会话。
- ⚡ **大规模并行执行**：在计算集群中并行运行测试，部分变更可驱动多达 10,000 个浏览器，几分钟内完成。
- 🎥 **视频关键帧对比**：分别录制变更前后的应用行为视频，逐关键帧比较像素差异，检测视觉、行为和逻辑变化。
- 🤖 **Agent 补位与 QA**：对覆盖缺口启动 Agent 测试，并在新功能 QA 中回写会话库。
- 🧪 **确定性浏览器与零噪音**：浏览器各层被增强为完全确定性，前端变更自动 mock 网络请求并长期维护，保证无副作用、减少误报。
- 📝 **PR 审查摘要**：自动评论变更对现有工作流、新功能、性能和无障碍的影响，支持人工几键审查或让 Agent 继续修改。
- 🔁 **Agent 迭代闭环**：在代码进入人工审查前，为 Agent 提供迭代测试与反馈循环。
- 📈 **适配复杂大规模代码库**：可处理数千万行代码、数十万边缘情况，并在无法完全测试时发出警告。
- 🔐 **合规与生态**：SOC2 Type II 合规，支持 React、Vue、Angular、Vite、Svelte、Next.js 等框架，以及 GitHub、GitLab、Vercel 和任意 CI。
- 🛡️ **自动维护测试套件**：随功能新增而增加测试、随过时而移除测试，减少维护；底层确定性调度引擎用于消除 flaky 测试并提升速度。
- 💡 **市场认可**：获得 Y Combinator、Coatue、GitHub CTO、Adobe CPO、Vercel 创始人等投资人支持，并被 Notion、Dropbox、Engine 等团队使用。

---

### [推出 UI SDK · UI SDK](https://ui-sdk.dev/docs/core/changelog/introducing-ui-sdk)

**原文标题**: [Introducing UI SDK · UI SDK](https://ui-sdk.dev/docs/core/changelog/introducing-ui-sdk)

UI SDK 于 2026 年 11 月 12 日发布，是一款面向智能体与开发者的 TypeScript UI 行为库，提供 50 多种可组合的交互基础能力，并配套跨框架组件库与智能体操作接口；目前处于 Beta 阶段。

- 🧩 UI SDK 是 TypeScript UI 行为库，提供构建组件库所需的行为层，专为智能体设计。
- ⌨️ 内置键盘导航、焦点、选择、弹层、拖放及对应 ARIA 属性等基础能力。
- 🔧 提供 50 多种行为，如 createRovingFocus、createTypeahead、createPopup，可组合构建自有组件。
- ⚛️ 使用 @ui-sdk/core 定义一次组件，再适配 React 等框架；文中以 Share 弹层组件为例。
- 📚 基于相同行为提供 50 多个现成组件，覆盖 React、Vue、Svelte、Solid 和 Web Components，样式由使用者提供。
- 🤖 面向智能体构建与使用：createAgent 可在权限控制下读取页面并执行点击、输入、选择等操作。
- 🌐 WebMCP 的 registerTools 可让浏览器内置智能体读取组件并调用其动作。
- 🚀 可通过设置提示词快速接入；Beta 期间 API 可能变化，反馈可提交至 GitHub。
- 🙏 致谢 Radix、Base UI、React Aria、shadcn/ui、Nuxt UI、Geist 及 WAI-ARIA Authoring Practices 等团队与规范。

---

### [错误](https://github.com/solidjs/solid)

**原文标题**: [Error](https://github.com/solidjs/solid)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='github.com', port=443): Max retries exceeded with url: /solidjs/solid (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [获取失败](https://www.npmjs.com/package/solid-js)

**原文标题**: [Failed to retrieve](https://www.npmjs.com/package/solid-js)

无法总结：获取内容失败，状态码 403。

---

### [概览 - SolidJS 文档](https://docs.solidjs.com/)

**原文标题**: [Overview - SolidJS Documentation](https://docs.solidjs.com/)

Solid 2.0 文档介绍了一个用于构建 Web 用户界面的框架：使用 JSX 编写组件，用 signals 和 stores 管理状态，并精确更新页面中读取了变更值的部分；它没有虚拟 DOM，也不会重新渲染组件，组件函数只运行一次，内部的响应式表达式会随输入变化持续运行。Solid 2.0 是核心库、DOM 渲染器、路由、head 管理与 Vite 插件协同设计的整体平台。

- 🧩 **组件模型**：组件函数只执行一次，响应式表达式负责后续更新，避免传统组件反复渲染。
- ⚡ **响应式状态**：使用 signals 和 stores 保存状态，更新时只影响实际读取该值的页面部分。
- 🚀 **快速入门**：新用户应先阅读 Quick start，创建应用、了解生成文件并完成第一次修改。
- 📚 **推荐阅读顺序**：Quick start → Thinking in Solid → Reactivity → Components and JSX → Stores → 避免不必要的 effects → 异步响应式与 Boundaries → Mutations → 状态管理 → 渲染与 SSR → 应用结构 → 路由。
- 🧭 **项目选择**：已有 Solid 经验可从 Quick start 开始，并通过 Project shapes 了解应选哪种模板。
- 🔁 **框架迁移**：React/Vue 用户可读 Thinking in Solid 和 From React；Solid 1.x/SolidStart 用户查看 Migration 指南。
- 📖 **参考文档**：Reference 按导入来源组织，如 `solid-js`、`@solidjs/web`、`@solidjs/router`，便于查 API 签名与参数。
- 🏗️ **应用构建**：Learn 部分涵盖 Vite 插件、服务端函数、会话、部署、路由等内容。
- 🤖 **AI 辅助**：Solid for AI tools 提供速查表、技能、诊断信息和可粘贴到助手配置中的规则块。
- 💬 **反馈与术语**：Glossary 解释 Solid 专有术语；缺少内容可提交 issue 或到 Discord 提问。

---

### [Solid 2.0 RC：重大揭晓 | Solid](https://www.solidjs.com/blog/solid-2-0-rc-the-big-reveal/)

**原文标题**: [Solid 2.0 RC: The Big <Reveal> | Solid](https://www.solidjs.com/blog/solid-2-0-rc-the-big-reveal/)

Solid 2.0 进入 Release Candidate：核心变化是把异步变成响应式图本身的属性，计算可直接返回 Promise 或异步迭代器，下游自动理解，无需专门资源原语或手动 loading 状态。同时，SolidStart 被退休并由 start mode 取代，新的 Rust/OXC 编译器默认随 Vite 插件提供，框架通过移除旧有变通方案来降低学习成本，并强化服务端函数、路由、部署与生态支持。

- 🚀 异步进入响应式图：memo 可直接异步，`<Loading>` 覆盖等待状态，`isPending` 表示“这个问题的更新是否在途”，派生状态、错误处理、过渡与乐观更新都由此统一。
- 🧹 大量旧 API 被移除：`createResource`、`batch`、`startTransition/useTransition`、`on`、`createComputed`、`produce`、`createMutable` 等不再需要，1.x 迁移指南提供替代映射。
- 🧩 新写法更统一：效果拆分为 `createEffect(compute, apply)`，store setter 直接给出可修改 draft，减少跟踪与副作用混杂及写回模式。
- ⚡ 新编译器默认启用：`@solidjs/vite-plugin` 默认使用基于 Rust/Oxc 的编译器，零配置；基准中相对 Babel 插件最高约 355 倍加速，Babel preset 仍可用。
- 🛠️ start mode 内置完整应用方案：`solid({ start: true })` 在纯 Vite 上提供入口、开发服务与构建；默认 SPA，可选文件系统路由、SSR、中间件、每请求 setup、类型化环境变量及服务端密钥泄漏检查。
- 🔌 服务端函数进入核心：`"use server"` 由 `@solidjs/web/server-functions` 支持，提供类型化 RPC、流式返回、渐进增强与自定义序列化；构建产物输出 Web 标准 Fetchable handler，便于 Cloudflare、Netlify、Nitro、Bun、Deno 等平台部署。
- 🪦 SolidStart 完成使命：其能力已分别迁入核心、start mode 和路由中立包，因此不再发布空心 3.0；生产项目不会立即中断，仍会获得维护版本并提供迁移指南。
- 🧱 运行时与 API 更新：新增/重做 `<Loading>`、`<Errored>`、`<Reveal>`；核心内置 actions 与乐观状态；draft-first stores；统一 `<For>` 并引入 `<Repeat>`；DOM 语义更接近 HTML；包结构拆为 `@solidjs/signals`、`@solidjs/web` 等。
- 📦 迁移与生态就绪：预览文档在 v2.solidjs.com，新项目可用 `create solid@latest`，迁移助手 `npx solid-migration-assistant`；Solid Router 2.0、Solid Meta 1.0、TanStack 相关方案及常用库已支持或跟进。
- 🔭 后续重点：将推出异步模型深度系列；响应式服务端组件处于实验预览，由 `serverFunctions: { components: true }` 标志控制，稳定版后进一步公布。
- 🙌 RC 意味着 API 冻结但仍可能有 bug，作者感谢社区、测试者、赞助方与 AI 工具支持，并呼吁生态维护者尽快迁移和反馈问题。

---

### [推出跨源存储 API | 博客 | Chrome 开发者](https://developer.chrome.com/blog/introducing-cross-origin-storage)

**原文标题**: [Introducing the Cross-Origin Storage API  |  Blog  |  Chrome for Developers](https://developer.chrome.com/blog/introducing-cross-origin-storage)

Chrome for Developers 于 2026 年 11 月 10 日介绍早期提案 Cross-Origin Storage API（COS）：客户端用内容哈希定位资源，并从任意 URL 获取，使指定站点或所有站点共享同一份精确资源，减少重复下载，同时带来安全收益与安全挑战。
- 📣 页面顶部公告称 Modern Web Guidance 已稳定，可帮助编码代理采用专家审核的 Web 开发最佳实践。
- 🔐 COS 通过 `navigator.crossOriginStorage.getFileHandle()` 跨源存取文件，并以加密哈希标识内容；还计划集成 HTML、CSS、JavaScript 和 `fetch()`。
- 🤖 主要用例包括 AI 模型、Wasm 模块、流行 JavaScript 库/框架、游戏引擎和大型 Web 字体，避免相同资源被大量重复下载。
- 🧪 可从 Chrome Web Store、Firefox Add-ons 或 Safari App Store 安装扩展来 polyfill API，并在浏览器中测试流程。
- 🌱 生态已有实验性支持：Emscripten、Flutter、Transformers.js、WebLLM、wllama、Nuxt.js、Prompt API Polyfill、Prebid.js 等。
- 🏛️ 这是 WICG 早期提案，已进行 W3C TAG 设计评审，并向 WHATWG、CSS WG、Fetch Standard 提交宿主集成，向 Mozilla 和 WebKit 征求标准立场。
- 🧰 资源包括解释器、规范草案、Chrome umbrella bug、Public Hash List、安全与隐私问卷、Intent to Prototype、Chrome Platform Status、工具与演示，以及相关文章和播客。

---

### [Val Town 即将停止运营 | Val Town 博客](https://blog.val.town/winding-down)

**原文标题**: [Val Town is winding down | Val Town Blog](https://blog.val.town/winding-down)

Val Town 宣布将逐步关停，原因是无法在云计算领域竞争；官方建议用户迁移到其他托管平台，并公布了服务终止时间表与退款安排。

- 🛑 Val Town 决定停止运营，团队对用户一直以来的信任表示感谢并致歉。
- ☁️ 关停主因是无法在云计算市场保持竞争力，但用户可迁移到 Cloudflare、Vercel、Netlify、Render 等托管平台。
- 🧭 官方提供迁移指南，并可通过 support@val.town 或 Discord 寻求帮助。
- 💳 即日起暂停计费，现有订阅继续免费服务；预付年费用户将获得部分退款。
- 📅 2026年11月10日起停止新注册和套餐升级。
- 🔒 2026年12月10日起进入只读模式，但不包括 SQLite 和 Blob 存储。
- ⏳ 2027年1月10日起所有其他服务终止。
- 📢 2027年2月1日 Val Town 将开源。
- 🙏 作者感谢团队成员、投资者、客户和用户过去四年的支持与贡献。

---

### [Bun 的提前编译器如何工作](https://bun.com/bun-aot-how)

**原文标题**: [How Bun's ahead-of-time compiler works](https://bun.com/bun-aot-how)

Bun 的提前编译（AOT）核心思路是：`bun compile` 把包含 npm 依赖的完整 TypeScript/JavaScript 程序编译为机器码，并附加到 Bun 运行时副本中；运行时仍基于 JavaScriptCore，但二进制中不含 JIT。编译器不依赖运行时 profiling、OSR 退出、watchpoint 或 IC 回填，而是通过全程序类型推断、推测检查、专用循环/函数版本和静态布局生成代码。该功能在 2026 年 11 月仍是实验性。

- 🧩 编译范围：`bun compile` 编译整个程序及可达的 npm 包，生成机器码并加入 Bun 运行时副本；运行时保留 JSValue 编码、Structure、GC、数组、字符串和解释器，但移除 JIT。
- ⚙️ 编译管线：Load→Check→Lower→Scan→Link→Plan→Walk→Emit→Image；前端在 lowering 阶段构建 SSA，IR 由 `AOTSchema.def` 定义并生成 C++/Rust 代码。
- 🔗 全程序类型链接：Scan 为每个函数生成无局部变量的摘要，Link 对可达函数摘要做不动点；字段写入者已知时推导字段类型和槽位表示，若对象逃逸到不可见代码，字段类型降为 `anything`。
- 🧠 TypeScript 类型只是推测：声明类型不会移除检查；值类型可由定义、支配检查、Link 或直接调用者证明；知识级别分为 Proven、Expected、Unknown；`int32` 特例要求构建时证明所有存储都在范围内。
- 🛡️ 检查失败处理：没有 OSR 退出值恢复和退出点栈；失败边用 diamond 通用分支、循环第二版本或函数版本承接；diamond 会丢失事实和拆箱表示。
- 🔀 函数版本：当函数依赖声明参数类型且存在不可见调用者时，生成 `ParameterGuard`、`Body`、`SlowBody`；已证明参数类型的调用者可直接调用 `Body` 并传拆箱参数。
- 🔁 循环版本与迭代重启：依赖推测的循环编译两份；类型化版本检查失败时，若当前迭代无可观察效果，可带循环携带值重启该迭代，否则改用 diamond；重启性由声明效果计算。
- 🚀 循环优化：不变量 shape/字段读取可提升；多种数组种类或布局可 unswitching；边界检查合并到循环头；计数循环按 8 展开，小常量循环完全展开；数值归约留在 FPR。
- 📏 无 profile 的代码大小选择：按静态位置选择 Open、Closed、Runtime 形式；Open 内联快路径用于循环，Closed 调用共享 stub 用于冷块和一次性代码。
- 📦 对象布局：编译对象为 `AOT::Object`，使用 `CompiledStructure`，无 butterfly；8–15 字节含 order 和 shape 字；联合布局连续编号便于范围检查；字段类型在存储时强制，不匹配则移到该对象的 extra properties。
- 🧮 值表示：JSValue 不变；SSA 值、参数、结果和槽位可选 Boolean、Int32、Int64、Double、OptionalInt64、OptionalDouble、Cell、Cell32、JSValue；Optional 用特殊位型编码 undefined/null/absent；Cell32 受 32GB cage 限制，`--aot-huge-heap` 使用 64 位引用。
- 📞 调用优化：已知被调用者用 `CallDirect` 并拆箱/内联；少数布局用 `CallTable` 通过 shape 索引方法表；闭包用 `IsClosureOf`；未知函数值或方法用共享 stub 和站点缓存；运行时代码不打补丁。
- 🧵 字符串、生成器与 async：循环累加可转成栈上 string builder；生成器跨 yield 的值存堆帧；`await` 复制机器帧到 cell 并保留 double 拆箱；可内联的生成器和已知 async 调用可避免分配。
- 🧯 异常与 GC：异常处理器按调用点表化；局部 catch 可转为跳转并消除 Error 分配；运行帧无栈映射，仅挂起点发帧映射；非逃逸对象可标量替换或放机器帧；写屏障按存储类型、所有者、分配时间等条件跳过。
- 🧰 内建、RegExp、Wasm：内建由 TypeScript 表描述并生成 C++/Rust；RegExp 构建期经 Yarr 编译；Wasm 主要经 OMG，部分 SIMD/GC/拒绝情况用 BBQ，运行时生成 Wasm 字节则解释执行。
- 🖼️ 镜像格式：代码以 `PROT_READ | PROT_EXEC` 映射且不写入；数据只读，方法表页按需可写；位置和内联帧在镜像中，栈追踪无需 source map。
- 🧪 测试与硬化：`bun test --aot` 使用同一编译器和 pass；构建先读测试找出可 mock 导出/内建成员并仅移除其证明；测试比较 `bun run` 的输出和退出码并注入推测失败；`--aot-harden` 在读和索引处加检查。
- ⚖️ 取舍：比 JIT 差在无法解析的多态、运行时生成代码、构建时间、大型程序代码体积、无断点/交叉编译/冻结内建；比 JIT 好在启动、内存、类型化字段访问和跨函数拆箱；文档给出何时继续使用 JIT。

---

### [Prettier 3.10：新的 Flow 语法、新的 JavaScript 语法，以及由 Yuku 驱动的新插件 · Prettier](https://prettier.io/blog/2026/11/11/3.10.0)

**原文标题**: [Prettier 3.10: New Flow syntax, new JavaScript syntax, and new plugin powered by Yuku · Prettier](https://prettier.io/blog/2026/11/11/3.10.0)

Prettier 3.10 正式发布，重点带来全新 Flow 语法支持、最新 JavaScript 提案支持，以及基于高性能 Yuku 工具链的新官方插件，同时包含跨 JavaScript、TypeScript、Markdown、HTML、CSS、Vue、Angular、GraphQL、YAML 等大量修复与改进。

- 🚀 新增官方插件 `@prettier/plugin-yuku`，由 Zig 编写的高性能 JavaScript/TypeScript 工具链 Yuku 驱动。
- 🧩 该插件提供 `yuku` 和 `yuku-ts` 两个解析器，但因包体积限制需单独安装并配置到 `.prettierrc`。
- 🧠 Flow 解析器支持 `flow-parser 0.332.0` 引入的新语法，包括模板字面量类型、构造函数类型、映射类型修饰符与键重映射、抽象/重写类成员、内联 import 类型、CommonJS 导入导出绑定和 `unique symbol` 类型。
- 🛠️ Flow 还新增支持构造函数参数属性、`in out` 型变、非空断言、`export as namespace`、可选元组成员、声明类私有字段及声明类继承 mixin 调用。
- ✨ JavaScript 新增支持 Structs 提案（非共享结构体）、`import.sync()` 提案和延迟重导出提案。
- 🐛 修复大量注释稳定性问题，包括标签模板、类型转换、序列表达式、箭头链、`for` 头部、导出装饰器、JSX 父类等场景。
- 🔧 修复必要括号丢失或多余问题，涉及 `yield`、`throw`、`TSInstantiationExpression`、二元表达式、类型断言和比较表达式等。
- ⚡ 提升含大量注释文件的格式化性能，并避免格式化超长二元表达式时发生调用栈溢出。
- 🧹 修复 `prettier-ignore` 相关输出问题，包括 for 初始化器、ASI 保护分号和类属性后多余分号。
- 🎯 TypeScript 改进包括属性签名注释、heritage clause 注释、`satisfies`/`as` 类型注释、类型参数列表范围格式化及实例化表达式括号。
- 🎨 CSS/SCSS/Less 修复 An+B 写法、函数调用后空行、单元素列表尾逗号、注释被吞、间接属性查找空格及 at-rule 插值解析。
- 🌐 HTML/Vue/Angular/Ember 修复属性名归一化、CDATA 保留、插值空行、`ngNonBindable` 内容保留、Angular 微语法、嵌入 `<script>`/`<style>` 等。
- 📊 GraphQL、Markdown、YAML 改进包括空选择集、GraphQL 字符串回车符、Markdown 链接转义、中文/日文换行、YAML 锚点顺序和块标量尾随空白保留。
- 🧰 API/CLI 和其他改进包括支持带 UTF-8 BOM 的配置文件、注释挂载辅助函数返回 `true`、Unicode 零宽标记处理及缓存 `.editorconfig` 提升配置解析速度。

---

### [简介 | Yuku](https://yuku.fyi/)

**原文标题**: [
      Introduction
      | Yuku
    ](https://yuku.fyi/)

Yuku 是一个用 Zig 编写的高性能 JavaScript/TypeScript 编译器工具链，强调正确性、性能和清晰性；它完全符合 ECMAScript 规范，零依赖，可在多种运行时中使用，并提供解析器、AST、语义分析、遍历与代码生成等文档及性能基准。

- 🧩 **Zig 实现**：Yuku 是使用 Zig 编写的高性能 JavaScript/TypeScript 编译器工具链，注重正确性、性能与清晰性。
- ✅ **规范兼容**：Yuku 100% 符合 ECMAScript 规范，测试结果为零失败、零 AST 不匹配。
- ⚡ **性能突出**：基于数据导向设计并进行性能优化；基准显示其原生解析速度快于 Oxc 和 SWC，npm 上解析小文件和大文件也快于替代方案。
- 🌍 **跨平台支持**：可在 Node.js、Bun、Deno、浏览器、边缘运行时及原生 Zig 中使用。
- 📦 **零依赖**：纯 Zig 实现，构建过程和 npm 包均无第三方依赖。
- 🆕 **现代语法**：支持新语法与提案语法，包括装饰器、source phase imports、deferred imports 和 `using` 声明。
- 📚 **文档完善**：提供 JavaScript 指南，以及 Zig 侧的解析器、AST、语义分析、遍历和代码生成文档。
- 📊 **分析性能**：在整个代码库分析、跨文件引用解析和导入链接方面，Yuku 快于 typescript-eslint 和 TypeScript API，单一大文件分析也更快。

---

### [发布 v2.4.0 · processing/p5.js · GitHub](https://github.com/processing/p5.js/releases/tag/v2.4.0)

**原文标题**: [Release v2.4.0 · processing/p5.js · GitHub](https://github.com/processing/p5.js/releases/tag/v2.4.0)

p5.js 2.4.0 是一次功能与稳定性更新，重点增强 SVG、3D 模型材质与变换、加载动画、p5.strands/WebGPU 能力，并改进错误提示、测试、安全与社区协作。

- 🚀 p5.js 2.4.0 发布，扩展 SVG、3D 模型材质、3D 模型旋转/缩放等图形能力。
- 🖼️ 新增 SVG 导入/导出，开箱即用，无需额外导入。
- 🎬 新增 loadingAnimation(...)，可关闭默认加载动画或自定义；默认动画为旋转 p5.js 星形。
- 🧊 p5.strands 增加简化实例化 API、变换矩阵支持、有状态辅助函数，并修复转译器/着色器问题。
- 🧱 loadModel() 支持 .obj 多材质模型，含多部件渲染、纹理贴图、凹凸贴图等增强。
- 🛠️ FES 错误系统模块化、支持本地/CDN 翻译、性能优化，并加入实验性功能日志。
- 🔢 向量与数学 API 修复跨维度一致性，如 lerp() 通用维度、equals() 非对称、rem() 负除数等。
- 🩹 2.3.1–2.3.4 补丁带来 HDR 更名 P3、加载动画、安全加固、TypeScript 声明修复等。
- 🌐 WebGPU/WebGL 改进：WebGPU 失败回退 WebGL、可变长度缓冲、媒体元素/createCapture 支持；WebGL 增加 SEGMENTED 平面着色等。
- 🔐 更新安全政策与事件响应计划，更新依赖/构建/CI，并增加自动化与性能测试。
- ♿ 为屏幕阅读器加入多语言支持，继续扩展无障碍创作工具。
- 📦 使用 2.4 可通过 starter sketch 或引入 p5.js 与 p5.webgpu.js 脚本；WebGPU 模式需 async/await createCanvas(..., WEBGPU)。
- 👥 社区贡献活跃，多位首次贡献者参与，维护者与导师持续评审和支持。

---

### [获取失败](https://openprocessing.org/@p5js/3047798)

**原文标题**: [Failed to retrieve](https://openprocessing.org/@p5js/3047798)

无法总结：获取内容失败，状态码 403。

---

### [Node.js — Node.js 26.](https://nodejs.org/en/blog/release/v26.13.1)

**原文标题**: [Node.js — Node.js 26.13.1 (LTS)](https://nodejs.org/en/blog/release/v26.13.1)

Node.js 26.13.1（LTS，代号“Lithium”）于 2026-11-11 发布，由 @aduh95 发布，是一次安全版本更新，重点修复 http2、TLS/HTTP 等组件的多个高危及中低危漏洞，并同步更新多项依赖。

- 🔒 本次为安全发布，建议受影响的 Node.js 26.x LTS 用户尽快升级。
- 🚨 高危修复集中在 http2 与 TLS：包括流移除时释放头部、检测被 nghttp2 放弃的流、保留待写缓冲、防止空写入触发嵌套解析，以及修复可远程触发的 TLS 服务端崩溃等。
- 🛡️ TLS 安全加固：禁止 mTLS 无会话 ID 上下文时恢复会话，禁止重协商/HRR 或 TLS 恢复改变 SNI。
- ⚠️ 中危修复涉及 http2 的 ALTSVC 缓冲区溢出、入站 DATA 内存计费、取消流上的空写请求保护，以及 http 代理凭据脱敏、https Agent TLS 策略键隔离等。
- 🧩 低危修复包括 permission 模块的递归 fs.watch 信息泄露与堆快照目标检查，以及 zlib 销毁后的参数回调处理。
- 📦 依赖更新：brotli 1.2.1、llhttp 9.4.4、sqlite 3.54.1、undici 8.12.4。
- 🏗️ 其他提交包括构建系统适配 OpenSSL API 级别、修复旧版 OpenSSL 3.0 构建问题，以及工具链调整。
- 💻 提供 Windows x64/ARM64、macOS Intel/Apple Silicon、Linux x64/ppc64le/s390x/arm64、AIX ppc64 和源码等下载。
- 🔗 发布页同时提供 SHASUMS 校验值和 PGP 签名，便于验证下载文件完整性。

---

### [Node.js — Node.js 24.22.3 (LTS)](https://nodejs.org/en/blog/release/v24.22.3)

**原文标题**: [Node.js — Node.js 24.22.3 (LTS)](https://nodejs.org/en/blog/release/v24.22.3)

Node.js 24.22.3（LTS，代号“Krypton”）于 2026-11-11 发布，是一次安全更新，主要修复 http2、TLS/HTTP、权限、zlib 等模块中的多个高危、中危和低危漏洞，并同步更新 brotli、llhttp、sqlite、undici 等依赖，同时提供多平台安装包、二进制文件、源码和校验文件。

- 🔐 **版本信息**：Node.js 24.22.3“Krypton”为 LTS 安全版本，发布于 2026-11-11，由 @aduh95 发布。
- 🚨 **高危漏洞**：修复多个 http2 与 TLS 高危问题，涉及流移除时释放 headers、空写入导致嵌套解析器执行、nghttp2 遗弃流检测、socket 写入完成前保留缓冲区、mTLS 会话恢复限制、SNI 变更限制、可远程触发的 TLS 服务端崩溃等。
- ⚠️ **中危漏洞**：修复 http2 ALTSVC 缓冲区溢出、SNI 上下文 CA 应用、入站 DATA 计入 maxSessionMemory、无效代理 URL 错误信息泄露代理凭据、取消流上的空写入保护、https Agent TLS 策略键隔离等问题。
- 🛡️ **低危漏洞**：修复递归 `fs.watch` 中拒绝访问的后代路径泄露、zlib 销毁后的参数回调处理、权限模块对堆快照目标路径的检查等问题。
- 📦 **依赖更新**：brotli 更新至 1.2.1，llhttp 更新至 9.4.4，sqlite 更新至 3.54.1，undici 更新至 7.30.2。
- 💻 **发布产物**：提供 Windows 64-bit/ARM64 安装包与二进制、macOS Intel/Apple Silicon、Linux x64/ppc64le/s390x/arm64、AIX 等平台文件，以及源码包。
- 🔗 **校验与文档**：发布页面包含 SHASUMS 与 PGP 签名，另提供 v24.22.3 文档和所有发布文件下载入口。

---

### [Node.js — Node.js 22.23.5（长期支持版）](https://nodejs.org/en/blog/release/v22.23.5)

**原文标题**: [Node.js — Node.js 22.23.5 (LTS)](https://nodejs.org/en/blog/release/v22.23.5)

Node.js 22.23.5（LTS，代号 Jod）于 2026-11-11 发布，是一次安全更新，主要修复 http2、TLS、HTTP、权限等模块中的多个漏洞，并更新相关依赖。

- 🔐 版本性质：Node.js 22.23.5 是 LTS 安全版本，建议相关用户升级。
- 🚨 高危修复：涉及 http2、tls/http 等模块，包括流移除时释放头部、空写入导致嵌套解析、检测被 nghttp2 放弃的流、保留缓冲区至套接字写入完成、mTLS 会话恢复限制、SNI 变更限制等。
- ⚠️ 中危修复：包括 ALTSVC 缓冲区溢出、无证书时应用 SNI 上下文 CA、inbound DATA 计入 maxSessionMemory、代理 URL 错误中隐藏凭据、取消流上的空写请求保护、隔离 Agent TLS 策略键等。
- 🛡️ 低危修复：涉及递归 fs.watch 权限泄漏、zlib 销毁后的参数回调、堆快照目标权限检查等。
- 📦 依赖更新：llhttp 更新至 9.4.4，SQLite 更新至 3.54.1。
- 💻 发布产物：提供 Windows、macOS、Linux、AIX、ARM 等多平台安装包和二进制文件，以及源码包、文档、SHA256 校验和与 PGP 签名。
- 🔗 下载与文档：可通过 Node.js 官方发行目录获取各平台文件，并查看 v22.23.5 API 文档。

---

### [Node.js — Wednesday, November 11, 2026 Security Releases](https://nodejs.org/en/blog/vulnerability/november-2026-security-releases)

**原文标题**: [Node.js — Wednesday, November 11, 2026 Security Releases](https://nodejs.org/en/blog/vulnerability/november-2026-security-releases)

overview summary
Node.js 项目于 2026 年 11 月 11 日发布 22.x、24.x、26.x 安全更新，最高严重性为 HIGH，修复 HTTP/2、TLS/HTTPS、证书校验、权限模型、zlib 与代理配置等多项漏洞，并更新 llhttp、undici、sqlite 依赖；建议尽快升级到 v22.23.5、v24.22.3、v26.13.1。

- 🚨 发布信息：2026 年 11 月 11 日安全版本，覆盖 22.x、24.x、26.x，最高严重性为 HIGH。
- 📦 升级版本：v22.23.5、v24.22.3、v26.13.1，发布当天或稍后可用。
- 🔧 依赖更新：修复 llhttp（22/24/26）、undici（24/26）、sqlite（22/24）相关公开漏洞。
- 💥 HTTP/2 远程中止：CVE-2026-123863（高），未认证客户端可触发会话析构断言失败并终止进程。
- 🔐 HTTPS 内存泄露：CVE-2026-123864（高），零长度 TLS 写入引发解析器重入，可能泄露其他连接内存，包括 TLS 私钥和请求内容。
- 🧹 HTTP/2 资源泄漏：CVE-2026-123865（高），连接关闭期间触发协议错误可永久泄漏内存和文件描述符。
- ♻️ HTTP/2 释放后使用：CVE-2026-123866（高），流在写背压时被拆除，可能把已释放或无关内存发送给对端。
- 📞 TLS 延迟回调崩溃：CVE-2026-126051（高），使用 SNICallback、OCSPRequest、newSession、resumeSession 或 addContext 的 TLS 服务器可被远程触发未捕获异常。
- 🪪 TLS 1.2 客户端证书绕过：CVE-2026-123872（高），重协商时更改 servername 可绕过按主机名区分的客户端证书策略。
- 📂 HTTP/2 文件流 UAF：CVE-2026-123874（高），客户端重置 respondWithFile/respondWithFD 的待写流可造成释放后使用和内存破坏。
- 🧨 中危漏洞：包括 altsvc 堆溢出 CVE-2026-123828、CA-only SNI 失败开放 CVE-2026-123867、HTTP/2 maxSessionMemory 失效 CVE-2026-123868、代理凭据泄露 CVE-2026-123871、https.Agent 证书校验绕过 CVE-2026-123877、取消 respondWithFile 导致空指针崩溃 CVE-2026-123875。
- ⚠️ 低危漏洞：递归 fs.watch 泄露被拒路径名 CVE-2026-123829、zlib params+destroy 不可捕获断言 CVE-2026-123862、权限模型通配符过度授权 CVE-2026-106071。
- 🛡️ 建议：所有 active release line 用户应升级；EOL 版本始终受影响，应遵循发布计划保持最新。
- 🤝 支持与报告：Maintenance LTS 后的商业支持可通过 OpenJS Ecosystem Sustainability Program 合作伙伴获取；漏洞按 Node.js 安全流程报告，并可订阅 nodejs-sec 获取更新。

---

### [PixiJS 3D 简介 | PixiJS](https://pixijs.com/blog/pixi-3d-open-beta)

**原文标题**: [Introducing PixiJS 3D | PixiJS](https://pixijs.com/blog/pixi-3d-open-beta)

PixiJS 3D 于 2026 年 11 月 12 日发布并开放公测，使 PixiJS 同时成为完整的 2D 与 3D 引擎。二者共享同一舞台，3D 场景作为显示对象接入现有项目，默认性能优化，并优先支持 WebGPU、兼容 WebGL2。

- 🚀 PixiJS 3D 进入开放测试，目标是让 2D 与 3D 在同一引擎、同一舞台中高效协作。
- 🧩 3D 场景是显示对象：添加 `View3D` 后即可使用熟悉的 `addChild`、`Assets` 和指针事件，可放置多个并像精灵一样定位缩放。
- 🔄 2D 与 3D 可深度混合：滤镜和遮罩适用于 3D 视图，2D 可跟随 3D，2D 容器也可实时贴到 3D 表面并相互嵌套。
- ⚡ 默认性能优化：自动批处理共享几何体与材质的对象，按设备、浏览器和场景选择最佳渲染路径，并只更新发生变化的网格。
- 🧠 WebGPU 优先并自动回退：同一代码可在 WebGPU 与 WebGL2 运行；WebGPU 使用计算着色器裁剪，Safari 和 iPhone/iPad 会自动切换到合适路径。
- 🌲 支持大规模场景：`BatchedMesh3D` 可绘制数万份副本，演示中 10 万个带阴影对象可保持 60fps。
- 🎨 内置完整 3D 能力：glTF 蒙皮、变形目标、动画、压缩纹理，PBR/Phong/平面/卡通及自定义多 Pass 材质，另有渲染图、HDR、色调映射、后处理、粒子、阴影和级联阴影。
- 🎮 面向游戏开发：2D HUD、菜单和触控控件与 3D 同舞台，无需 DOM 覆盖层；官方展示了《Nightward》和《Mach 2》两个游戏。
- 🤖 AI 就绪：提供 `pixijs-3d` 技能，包含起始应用、可运行配方和常见错误说明，可通过 `npx skills add` 安装，并随 npm 包发布。
- 🛠️ 快速开始：运行 `npm install pixi.js @pixi/3d`，要求 `pixi.js` 8.23.0 或更高；在 `app.init` 前导入并向舞台添加 `View3D` 即可。
- 📚 文档资源充足：包含 35 篇指南、100 多个实时示例、3 个实时编辑器教程和完整 API 参考。
- 🧪 公测反馈重要：封闭测试收到 30 多个 bug 报告和功能请求，多数已进入本版本；API 仍可能调整，目标为 1.0。
- 🆓 开源免费：采用 MIT 许可，并承诺持续保持免费。

---

### [启动框架性能项目 | e18e](https://e18e.dev/blog/launching-the-framework-performance-project)

**原文标题**: [Launching the Framework Performance project | e18e](https://e18e.dev/blog/launching-the-framework-performance-project)

e18e 于 2026 年 11 月 10 日发布 Framework Performance 项目，旨在通过统一、透明、持续的多维基准测试比较元框架性能，帮助维护者发现瓶颈、推动优化，并为社区提供更全面的性能参考。

- 🚀 **项目目标**：帮助框架维护者测量并改进自身性能，同时向社区公开清晰透明的跨框架性能数据。
- 🍎 **解决痛点**：各元框架自建基准侧重点不同，容易只测试自身擅长领域；部分团队也缺乏时间长期维护基准。
- 🧩 **首批覆盖框架**：Nuxt、Next.js、TanStack Start (React)、Solid Start、Solid 2.0、Astro、SvelteKit、React Router、Pracht。
- ⏱️ **两类基准**：分为 DevTime 与 RunTime，既衡量页面渲染，也衡量构建、安装、依赖等使用成本。
- 🛠️ **DevTime 指标**：依赖数量、node_modules 体积、构建/安装时间、开发服务器启动、Core-JS polyfills、浏览器基线、最低 Node 版本；使用各框架默认/推荐配置以保持公平。
- 🌐 **RunTime 指标**：同一应用在各框架中构建，覆盖 CSR/SSR 的 Lighthouse FP、FCP、INP，初始加载体积、SSR 吞吐、SSR 负载测试及框架 Link 组件负载测试；多次运行并记录 min、max、median、variance。
- 📊 **真实世界数据**：引入 HTTP Archive 的桌面/移动端统计，并补充 TanStack 检测；同时提醒真实性能受托管、流量来源、样本量等因素影响，需多角度评估。
- 🔍 **持续跟踪**：记录各框架主要和次要版本变化，观察性能演进，而非只做一次性“X 比 Y 好”的排名。
- 💡 **已产生实际影响**：Nuxt 内部链接 SSR 渲染时间约降低 58%；Next.js RSC payload 解析约快 75%；Solid 2.0 上游修复将 SSR 负载测试从 170 提升到 280 req/s（单连接）、约 200 到 390 req/s（并发）；Vue Router/TanStack Router 链接渲染优化提案。
- 🤝 **合作与支持**：与多个框架团队、Google、e18e 社区及 Depot 合作；Depot 赞助稳定基准运行环境。
- 🔮 **后续计划**：继续新增基准和框架，欢迎社区反馈测试公平性与缺失项，并可通过 Open Collective 赞助支持项目。

---

### [e18e | 生态系统性能](https://e18e.dev/)

**原文标题**: [e18e | Ecosystem Performance](https://e18e.dev/)

本次清理工作主要是移除冗余依赖，并用现代替代方案进行替换，以精简依赖结构。
- 🧹 移除冗余依赖
- 🔄 用现代替代方案替换旧依赖

---

### [框架性能 | 框架性能](https://frameworks.e18e.dev/)

**原文标题**: [Framework Performance | Framework Performance](https://frameworks.e18e.dev/)

Framework Performance 项目旨在对比现代 Web 框架的真实构建与运行成本，关注开发者启动项目时继承的负担，以及用户和服务器在运行时的体验；目标是让技术取舍更清晰，并帮助框架作者持续迭代优化。项目基于 E18E 改善 JavaScript 生态的使命，测试列表持续增长，并欢迎社区反馈与贡献。

- 🎯 **项目定位**：比较现代 Web 框架的真实成本，帮助开发者理解框架带来的开发与运行权衡。
- 🧪 **测试分类**：目前分为 Dev Time（开发时）和 Run Time（运行时）两大部分。
- 🛠️ **开发时指标**：依赖数量、Node Modules 体积、构建与安装时间、开发服务器启动时间、Core-JS Polyfills、浏览器基线、最低 Node 版本。
- ⚙️ **运行时指标**：Lighthouse 客户端渲染与服务端渲染、初始加载、服务端吞吐量、SSR 负载测试、SS 框架路由链接负载测试、Core Web Vitals。
- 📊 **Core Web Vitals**：覆盖 LCP、CLS、FCP、TTFB、INP，并分别测量桌面端与移动端。
- 🔁 **CI 与结果展示**：开发时和运行时测试在 CI 流水线中运行，结果保存为 JSON，由 Astro 文档站点加载展示。
- 📈 **版本跟踪**：跟踪所有 major 和 minor 版本，统计展示最新版本，并可进入各框架详情页查看随时间的变化。
- 🏗️ **测试基础设施**：全部测试与统计生成由基础设施合作伙伴 Depot 运行，以保证一致、公平和更快的测试。
- 📦 **覆盖框架**：Astro 7.4.12、Next.js 16.4.6、Nuxt 4.6.4、Pracht 1.0.0、React Router 8.5.1、SolidStart 2.2.2、Solid 2.0 2.0.0-rc.21、SvelteKit 3.2.0、TanStack Start 1.169.5、Void 1.9.1。
- 📝 **社区参与**：如发现测试问题或有新测试想法，可在 GitHub 仓库中提交 issue。

---

### [AI 在 Web 开发中最常出错的 10 件事 | 博客 | Chrome for Developers](https://developer.chrome.com/blog/top-10-things-ai-gets-wrong-in-web-dev)

**原文标题**: [Top 10 things AI gets wrong in web development  |  Blog  |  Chrome for Developers](https://developer.chrome.com/blog/top-10-things-ai-gets-wrong-in-web-dev)

概述：Modern Web Guidance 1.0 已稳定发布，为 AI 编码代理提供经过专家审核的 Web 开发最佳实践和浏览器兼容性知识，帮助开发者更好地利用现代 Web 平台。评测显示，未使用该指南的代理平均仅通过约 50% 的检查，使用后提升至约 90%。

- 🚀 Modern Web Guidance 1.0 正式发布，可通过 `npx modern-web-guidance@latest install` 安装。
- 🧪 评测方式：将同一提示分别交给启用和未启用指南的代理，再按指南定义的预期检查通过率。
- 📉 即使是最新前沿模型，未引导时也不能稳定遵循现代 Web 最佳实践，平均通过率约 50%。
- 📈 使用 Modern Web Guidance 后，平均通过率提升至约 90%。
- ♿ 无障碍焦点管理：常见错误包括未移动或恢复焦点、手写 Tab 键焦点捕获、工具栏每项都成为独立 Tab 停靠点、焦点轮廓对比度不足。
- 🌀 减少动态效果：常忽略 `prefers-reduced-motion`，或在全局平滑滚动、滚动驱动动画、过渡重置中处理不当。
- 📝 表单体验：常见问题有重复实现 `:user-invalid`、`aria-invalid` 不同步、用占位符代替持久格式提示、自动填充状态仅靠颜色提示。
- 👆 触摸手势：应优先使用 CSS Scroll Snap、`overscroll-behavior`、滚动驱动动画和原生滚动能力，而非主线程 JavaScript 手势。
- 🪟 对话框与浮层：应使用 `<dialog>`、`popover`、`@starting-style`、`transition-behavior` 等原生能力，避免手写滚动锁定、历史记录和动画状态机。
- 🌓 深色模式：需设置 `color-scheme`、相关 meta 标签和 `light-dark()`，并支持跟随系统及多标签页同步。
- ⚡ 运行时性能：常见问题是自定义 `setTimeout()` 队列、未使用 `scheduler.postTask()`/`scheduler.yield()`、`content-visibility`、`contain-intrinsic-size` 等。
- 📐 布局稳定性：需关注 `<video>` 尺寸、字体回退 `font-size-adjust`、`dvh`/`svh`、渲染阻塞与视图过渡等 CLS/闪烁来源。
- 🔐 安全：模型常不主动添加 CSP 或跨源隔离；DOM XSS 防护应优先使用原生 `setHTML()`、DOMPurify 回退、严格 Trusted Types 与 CSP。
- 🔑 Passkey/WebAuthn：常见错误包括手写 Base64URL、遗漏 `signalUnknownCredential()`、`getClientCapabilities()`、`AbortController` 及 `uiMode:"immediate"`。
- 🛠️ 项目将持续演进，欢迎通过 GitHub issue 反馈问题或贡献代码；页面内容采用 CC BY 4.0，代码示例采用 Apache 2.0。

---

### [SonarQube Hunter 代理 | AI 逻辑缺陷检测工具 | Sonar](https://www.sonarsource.com/products/sonarqube/hunter-agent/?utm_source=fnf&utm_medium=paid&utm_campaign=ss-hunteragents26&utm_term=newsletter-javascriptweekly&utm_content=v1&s_category=Paid&s_source=Paid%20Other&s_origin=influencer)

**原文标题**: [SonarQube Hunter Agent | AI Logic Flaw Detection Tools | Sonar](https://www.sonarsource.com/products/sonarqube/hunter-agent/?utm_source=fnf&utm_medium=paid&utm_campaign=ss-hunteragents26&utm_term=newsletter-javascriptweekly&utm_content=v1&s_category=Paid&s_source=Paid%20Other&s_origin=influencer)

SonarSource 发布 2027 年代码开发者调查状态报告，同时重点介绍其 AI 安全代理 SonarQube Hunter Agent。该代理专为发现传统分析工具无法捕获的意图型漏洞而设计，可与现有 SAST/SCA 形成多层验证体系。

- 🎯 **Hunter Agent 定位**：AI 驱动的安全代理，深度分析 SonarQube 项目，专门猎捕访问控制、业务逻辑和认证会话三大类逻辑漏洞。
- 🧠 **检测能力对比**：传统 SAST/SCA 覆盖已知模式与 CVE，而 Hunter Agent 负责意图型漏洞，如 IDOR、权限提升、业务逻辑滥用等，二者互补形成完整覆盖。
- 📊 **核心数据**：已发现 200+ 个开源应用零日漏洞，精度达 90%，结果可重复（相同扫描得到一致结果，避免 AI 提示的随机性）。
- 🔄 **四步工作流**：Hunt（全代码库探索与假设）→ Confirm（验证每项发现）→ Explain（提供严重性、原因与精确位置）→ Integrate（自动进入 SonarQube 问题列表）。
- 🛡️ **零信任设计**：审查代码的代理与编写代码的代理相互独立，职责分离，发现可审计且可重复。
- 🚀 **无缝集成**：确认的发现直接落地为 SonarQube issue，无需安装新工具，融入团队现有工作流与 CI 管道。
- 🏢 **市场信任**：获 700 万+ 开发者和 75% 财富 100 强企业信赖，支持 SonarQube Cloud 所支持的全部语言。

---

### [全球最大品牌通过 Optimizely 遭恶意软件感染](https://blog.report-uri.com/worlds-largest-brands-infected-with-malware-via-optimizely/)

**原文标题**: [World's Largest Brands Infected With Malware Via Optimizely](https://blog.report-uri.com/worlds-largest-brands-infected-with-malware-via-optimizely/)

概述总结
2026年11月16日，攻击者利用 Optimizely Web 的 Project JavaScript 向178家组织、188个代码片段注入恶意 JavaScript，并借由受信任的 cdn.optimizely.com 分发。该恶意软件同时具备加密钱包地址替换、银行卡盗刷、Cookie/截图窃取及 iOS 漏洞利用能力，造成约7千美元加密资产损失，并凸显第三方脚本供应链与 CSP 监控的重要性。

- 📅 事件规模：178家组织受影响，涉及 Zoom、BBC、CNN、Salesforce、GitLab、IKEA、HSBC、Equifax、Air France-KLM、Ledger、Peacock 等全球知名品牌。
- 🧩 入侵入口：攻击者篡改 Optimizely 客户项目中的 Project JavaScript，恶意代码仍由受信任的 cdn.optimizely.com 和 Optimizely 证书提供，并非 CDN 缓存投毒。
- 🦠 核心载荷：track.js 会替换 BTC、ETH、TRON、Solana、TON、LTC、BCH、DOGE 等钱包地址，覆盖页面文本、表单、链接、剪贴板、fetch/XHR、window.open、导航和 iOS 分享面板。
- 💳 银行卡盗刷：13:43 UTC 加入卡号、有效期、CVV 监控，通过 sendBeacon 发送至 1688360.cc/card.php；托管支付 iframe 中的卡片不受影响。
- 🍪 数据窃取：在钱包/支付相关场景触发地址替换时，向 hit.php 发送页面 URL、非 HttpOnly Cookie、被替换的原始地址及 html2canvas 页面截图。
- 📱 iOS 漏洞利用：加载 .icu 域名上的 boot.js，iOS 13–17 使用 Coruna，iOS 18.x 使用 DarkSword，iOS 26 为独立指纹链；iOS 18.6 及更早版本每60秒重载以重试漏洞利用。
- 🕵️ 三种加载器：明文 script 指向 1688360.cc/track.js；base64+atob 隐藏 URL；若被阻止则通过 eval 执行内联完整载荷；Smartsheet 曾清理后再次被感染。
- ⏱️ 关键时间线：04:21 首次出现 Optimizely 注入；08:10 首个 track.js 构建；11:20 Zoom 片段被修改；13:03 攻击者归集加密资产；13:43 加入卡盗刷；17:13–17:57 加入第二 iOS 主机；20:40–21:10 大规模清理；21:52 TalkTalk 仍受影响。
- 💰 资金损失：截至19:25 UTC 约7,040美元，后续更新约7,151美元；涉及 BTC、LTC、TRON、ETH、BSC，钱包资金随后被转出；TRON 钱包自2026年3月起已在使用。
- 🏢 行业分布：金融32家、科技/SaaS 23家、零售20家、流媒体娱乐12家、新闻媒体10家、航空旅行9家，另有医疗、制造、电信、加密交易、保险、房地产等。
- 🔍 可检测信号：Report URI 的 Script Watch 可发现新脚本依赖，Data Watch 可发现新数据目的地，Frame Watch 可发现新 iframe，CSP Integrity/JS Time Machine/Script Vault 可发现可信脚本指纹变化。
- 🛡️ CSP 效果评估：256个受影响站点中，68个无 CSP；50个允许载荷与数据外传；17个通过 connect-src 阻止数据外传但地址替换仍生效；24个（15%）成功阻止载荷。仅允许 cdn.optimizely.com 无帮助，限制性 script-src 才是关键。
- ⚠️ CSP 绕过点：'strict-dynamic' 会信任受信任片段插入的脚本；'unsafe-eval' 可让内联回退版本通过 eval 执行；HSBC 的 CSP 阻止了 track.js 和数据外传，但内联副本仍运行。
- ✅ Optimizely 用户处置：检查所有 Project JavaScript 和实验自定义代码，搜索 1688360.cc、atob( 及未知脚本；审查并轮换写入权限、API Token 和集成凭据。
- 🔐 暴露数据处置：将11月16日在自有表单输入的银行卡视为可能泄露；轮换非 HttpOnly Cookie 中的会话令牌和密钥；部署限制 connect-src、避免 unsafe-eval 并启用报告的 CSP。
- 📱 访客处置：iPhone/iPad 升级至 iOS 18.7.3+ 或 26.3+；核对当天加密转账地址是否被替换；在受影响站点用卡后监控账单。
- 🚫 关键 IoC：阻断 1688360.cc、5vobauua3ojpklx.icu、eil786npto9u5bq.icu、webshell.lol、linkforge.cc、l7bcsnwc7nzr3uo.icu 等域名及其子域；同时监控相关 SHA-256 哈希与攻击者钱包地址。
- 📢 后续更新：11月16日23:11 UTC 所有受感染 Optimizely 文件已清理；1688360.cc 和 webshell.lol 被置为 clientHold；部分 .icu 域名停止解析或响应；Optimizely 已在状态页确认事件；攻击者钱包于11月17日清晨被清空。
- ⚠️ 核心教训：受信任的 JavaScript 并不始终可信；网站可能因第三方依赖被攻破而受影响，自身代码和基础设施未必被入侵，持续监控浏览器端脚本并执行严格 CSP 至关重要。

---

### [Optimizely 服务状态 - 网页实验安全事件](https://status.optimizely.com/incidents/ftw0fh9wx43z)

**原文标题**: [Optimizely Service Status - Web Experimentation Security Incident](https://status.optimizely.com/incidents/ftw0fh9wx43z)

Optimizely 披露了一起 Web Experimentation 安全事件：未经授权方利用 Experimentation 中的漏洞，向部分客户项目注入恶意 JavaScript。目前漏洞已修复、注入代码已移除，并采取了账户保护与防止未授权代码交付的额外措施；事件状态为监控中。

- 🛡️ 事件性质：Optimizely 发现一起安全事件，未经授权方利用 Experimentation 漏洞实施攻击。
- 💻 攻击影响：攻击者向部分客户项目添加了恶意 JavaScript。
- ✅ 处置措施：已修复漏洞，并从受影响项目中移除注入代码。
- 🔐 账户与防护：已保护受影响用户账户，并增加防护措施以防止未授权代码交付。
- 📅 时间与状态：发布于 2026年11月17日 01:02 UTC，当前状态为监控中。
- 🌐 影响范围：Web Experimentation（Snippet Delivery）。
- 🔔 更新订阅：可通过电子邮件、短信、Webhook、Atom Feed 或 RSS Feed 订阅事件更新。

---

### [修复一个 WebKit 漏洞，看看承诺是否由铁轨铺成](https://alistair.sh/thenables)

**原文标题**: [Fixing a WebKit bug to see if promises are made of train tracks](https://alistair.sh/thenables)

文章从一段在 Bun/Safari 中会永久挂起的 `await p` 程序出发，解释 Promise 的 resolve 过程、thenable 同化、`Symbol.species` getter 抛错，以及 JavaScriptCore 因执行顺序错误导致 promise 永久 pending 的 WebKit bug；作者用仅 +16 行的修复让 Bun 1.4 和 Safari 27 与规范及 Node.js 一致，并由此说明 Promise 的失败轨道无法静态标注，因此 TypeScript 的 `Promise<T>` 没有 `E` 类型参数。

- 🧪 示例程序给 `p.constructor` 设置会抛错的 `[Symbol.species]` getter，`await p` 在 Node.js 中抛错退出，但 Safari 26 和 Bun 1.3.14 打印 `before`、报告错误后挂起。
- 🐞 根因是 Bun 和 Safari 共用 JavaScriptCore；其快速路径在调用 `then` 前先读取 species，抛错时尚未创建 resolve/reject 函数，promise 既未 fulfilled 也未 rejected，永久 pending。
- 🛠 修复对应 WebKit bug 318399 和 WebKit/WebKit#68749：先创建 resolve/reject 再调用 `then`，这样 getter 抛错时仍能 reject promise；修复仅 +16 行。
- 📜 `resolve(value)` 不会立即 fulfilled：它先读取 `value.then`；不存在或非函数则 fulfill，getter 抛错则 reject，若是函数则同化/flatten thenable。
- 🔁 thenable 是任何带 `.then()` 的值，Promise 本身也是 thenable；resolve 会把外层 promise 的 resolve/reject 传给 thenable.then，由其决定最终状态。
- ⏳ “resolved”不是规范中的真实状态；promise 可以已锁定结果但仍 pending，例如 `resolve(inner)` 且 `inner` 永不 settle。
- 🚂 文章用 Railway Oriented Programming 类比 Promise：有成功/失败双轨，`.then` 是切换点，但失败轨道可能由引擎写入。
- 🧬 `Promise.prototype.then` 为链式调用创建新 promise，因此会读取 `this.constructor[Symbol.species]`；普通属性读取可能触发 getter 并抛错。
- 🧾 规范要求 `NewPromiseResolveThenableJob` 在调用 `then` 抛错时 reject promise；JSC 旧实现因顺序错误让异常逃逸，导致“脱轨”并永久 pending。
- 🧠 结论：`Promise<T>` 无法标注失败类型 `E`，因为引擎可在远离用户 `reject()` 的地方把任意异常放到 rejected 轨道；这解释了 TypeScript 为何长期只有 `Promise<T>` 而没有 `Promise<T, E>`。

---

### [JavaScriptCore - WebKit 文档](https://docs.webkit.org/Deep%20Dive/JSC/JavaScriptCore.html)

**原文标题**: [JavaScriptCore - WebKit Documentation](https://docs.webkit.org/Deep%20Dive/JSC/JavaScriptCore.html)

JavaScriptCore 是 WebKit 内置的 JavaScript 引擎，实现 ECMA-262 规范的 ECMAScript；文档介绍其源码位置、核心架构以及由 LLInt、Baseline、DFG、FTL 组成的分层优化执行体系。

- 🧩 JavaScriptCore 又称 SquirrelFish、SquirrelFish Extreme，Safari 中的 Nitro/Nitro Extreme 是营销名称，项目与库名始终为 JavaScriptCore。
- 📁 源码位于 WebKit 源码树的 `Source/JavaScriptCore` 目录。
- ⚙️ 它是一台优化虚拟机，主要构件包括词法分析器、语法分析器、启动解释器 LLInt、Baseline JIT、低延迟优化 JIT DFG 和高吞吐优化 JIT FTL。
- 🔤 Lexer 负责词法分析，把脚本源码拆成 token；采用手写实现，主要位于 `parser/Lexer.h` 和 `parser/Lexer.cpp`。
- 🌳 Parser 负责语法分析，消费 token 并构建语法树；采用手写递归下降解析器，位于 `parser/JSParser.h` 和 `parser/JSParser.cpp`。
- 🚀 LLInt 执行解析器生成的字节码，主体在 `llint/`，用可移植汇编 offlineasm 编写，可编译到 x86、ARMv7 和 C，并包含内联缓存等优化。
- 🧱 Baseline JIT 面向至少调用 6 次或循环至少 100 次的函数，支持 OSR、回退处理和复杂多态内联缓存，并收集轻量性能分析信息。
- 🔍 DFG JIT 面向至少调用 60 次或循环至少 1000 次的函数，基于低层收集的信息进行激进类型推测，并通过 OSR exit、watchpointing 和指数退避重优化处理推测失败。
- 🏎️ FTL JIT 面向调用数千次或循环数万次的函数，是更高吞吐的优化层。
- 🔄 LLInt、Baseline、DFG、FTL 可在同一程序中混合执行，包括递归调用栈中的不同帧；它们保持一致的执行语义，通常只会带来性能差异。

---

### [The Web Is More Than Enough, by Paul Ford (Ftrain)](https://ftrain.com/aboard-the-web-is-more-than-enough)

**原文标题**: [The Web Is More Than Enough, by Paul Ford (Ftrain)](https://ftrain.com/aboard-the-web-is-more-than-enough)

本文是2026年10月21日Aboard Newsletter的文章《The Web Is More Than Enough》。作者以TinyLittleOffice意外走红为例，说明现代浏览器已能低成本、快速地构建功能丰富的应用；浏览器能力增强与开发成本下降正在降低软件创造门槛，并可能冲击应用商店经济和科技行业，同时让软件开发越来越像写作。

- 🏢 发布 tinylittleoffice.com：一个将数据存储在URL中的“办公套件”，意外吸引大量用户。
- 📈 流量一度导致服务器宕机、Cloudflare免费额度耗尽；付费升级后吸引数十万人访问。Hacker News有人批评它无意义，GitHub用户则提出功能与修复请求，The Register也做了报道，产品还短暂进入Product Hunt前十。
- 💡 作者的核心感受是：浏览器是非常强大的应用开发平台，而且获取这些能力的成本似乎每天都在下降。
- ⚡ 开发这个网页办公套件的投入约为写一篇长通讯的两倍；Cloudflare托管成本为0美元，计算速度和开发速度都极快。
- 🧰 浏览器已具备Web Crypto安全能力、WebAssembly原生速度、WebGL 3D/2D图形、Web Audio音频处理、PDF.js处理PDF等能力，并支持多语言与无障碍基础设施。
- 🌍 TinyLittleOffice发布了21种语言版本，包括克里奥尔语和意第绪语，体现Web作为分发平台的多语言优势。
- 🎮 Simon Willison的Battle Drones是浏览器中的3D多人游戏，支持离线运行；他并非游戏开发者，这显示“vibe coded”游戏也能被认真看待。
- 🏗️ 这些浏览器技术原本庞大复杂、面向Google等大团队，如今个人也能低成本使用；作者由此讨论AI泡沫与“百倍软件创作者”可能带来的经济冲击。
- 📱 低成本Web测试会削弱应用商店高抽成模式的吸引力，过去工业化的软件开发正变成更个人化的过程。
- ✍️ 软件开发越来越像写作：作家长期面临不被付费的困境，软件人员也可能感受到贬值；但对需要解决问题的客户而言，现在是能做成几乎任何事的好时代，最终各方会形成新的平衡。

---

### [你的 JS 错误在对你撒谎](https://blog.gaborkoos.com/posts/2026-11-12-Your-JS-Error-Is-Lying-to-You/)

**原文标题**: [Your JS Error Is Lying to You](https://blog.gaborkoos.com/posts/2026-11-12-Your-JS-Error-Is-Lying-to-You/)

概述总结：文章揭示 JavaScript 错误对象在序列化、堆栈、包装、跨运行时/边界传输和日志记录中会丢失关键信息，并给出保留错误因果链与诊断数据的实践方案。

- 🧱 `JSON.stringify(err)` 常得到 `{}`，因为 `message`、`cause` 等是非枚举属性；`Object.keys`、展开运算符和 `Object.assign` 也会漏掉它们。
- ⚠️ `catch` 捕获的不一定是 `Error`，可能是字符串、`null` 或普通对象；跨 realm 时 `instanceof Error` 也可能失效，应使用更稳健的判断。
- 🧵 堆栈不是 ECMAScript 标准的一部分：V8 默认只保留约 10 帧，记录的是错误创建位置而非抛出位置，且 `stack` 可被覆盖或定制。
- 🔗 包装错误时若不传 `{ cause }`，原始失败会丢失；即使传了，也必须遍历因果链才能看到根因，并需防止循环和过深链条。
- 🌳 一个错误可能是树而非单链：`AggregateError` 用 `errors` 聚合多个失败，`SuppressedError` 用 `error`/`suppressed` 记录清理失败与被替换的失败。
- 🌐 不同运行时和引擎在堆栈格式、深度、额外属性、错误消息文本上不一致；语言保证之外的信息不能当作可移植标准。
- 📦 序列化和跨边界传输都会改变证据：`structuredClone`、`postMessage`、Worker、IPC 会保留不同字段，通常无法恢复原始对象。
- 🚚 HTTP 响应不应暴露堆栈、文件路径或内部细节；应返回类似 RFC 9457 的小型 problem document，把完整错误留在服务端日志。
- 🪵 日志器可能隐藏失败：Pino 取决于错误放在哪个 key 及序列化器；Winston 默认甚至可能只写 `{"level":"error"}`，且默认序列化可能泄露敏感字段。
- ✅ 实践建议：包装时始终传 `cause`；重试/恢复决策依据错误 `code`；自建提取函数按允许字段记录，遍历 `cause`、`errors`、`error`/`suppressed`，处理循环、深度和成员数量限制。

---

### [修复栈溢出使 Js_of_ocaml 输出缩减了 16% | Tarides](https://tarides.com/blog/2026-11-12-fixing-a-stack-overflow-shrank-js-of-ocaml-output-by-16/)

**原文标题**: [Fixing a Stack Overflow Shrank Js_of_ocaml Output by 16% | Tarides](https://tarides.com/blog/2026-11-12-fixing-a-stack-overflow-shrank-js-of-ocaml-output-by-16/)

该文讲述了 js_of_ocaml 如何通过“变量合并”和“常量下沉”两项优化，解决大型顶层函数导致的栈溢出问题，并意外显著减小生成 JS 的体积，尤其是 gzip 压缩后的体积。

- 🧩 问题根源：客户程序编译成 JavaScript 后发生栈溢出，但调用栈并不深，原因是单个函数包含数万个局部变量，V8 为每个未捕获局部变量分配栈槽，13,000 个变量约消耗 100 KB 栈空间。
- 🏗️ js_of_ocaml 特性：它把初始化代码放进一个巨大的顶层函数，以便做死代码消除、常量传播和内联等全程序优化，因此更容易产生超大函数。
- 🔁 变量合并：通过活跃性分析，让生命周期不重叠的变量复用同一个名字；采用线性扫描寄存器分配思路，支持活跃区间中的“空洞”，兼顾速度与效果。
- 🧠 复制提示：遇到 `var x = y` 时优先让 `x` 复用 `y` 的名字，使赋值变成无操作；这对 SSA 形式在控制流汇合点产生的赋值尤其有效。
- 🧵 精确活跃性：把每条指令拆成输入/输出两个时间点，确保 `var x = y` 中 `y` 的最后使用与 `x` 的定义不重叠，从而允许共用名字。
- 🛡️ 例外与捕获变量：异常处理会延长相关变量活跃区间；被嵌套函数捕获的变量不做合并，因为它们位于堆上，不是栈溢出主因，且安全合并较复杂。
- 📦 常量下沉：把常量和分配的定义移动到更接近使用处的作用域；原始声明集中在顶部会长期阻塞变量合并，下沉后缩短活跃区间并支持单次使用常量内联。
- ⚠️ 安全限制：数组、对象等分配不能移入循环或嵌套函数，以免改变对象创建次数、引用身份或可变语义；分析阶段和转换阶段必须以相同顺序遍历作用域。
- 📊 效果数据：PRT 基准中局部变量从 13,539 降到 1,263，减少 91%；ocamlc 中从 3,005 降到 771，减少 74%；两者结合使未压缩输出约减小 4–8%，gzip 后减小 10–16%。
- ⚙️ 代价与可用性：编译时间约增加 5%；js_of_ocaml 6.4.0 及以后默认启用这两项优化，用户无需改代码即可受益。

---

### [uBlock Origin 中由网站驱动的元素选择器导致的通用 XSS](https://iter.ca/post/ubo-uxss/)

**原文标题**: [Universal XSS in uBlock Origin from website-driven element picker](https://iter.ca/post/ubo-uxss/)

近期发现 uBlock Origin（Firefox MV2 版本）存在一键式通用 XSS 漏洞：恶意网站可诱使扩展添加任意“受信任过滤器”，从而在任意站点上下文中注入并执行任意 JavaScript；MV3 版本 uBO Lite 也受影响但问题较轻。该漏洞现已修复，详情见 GitHub 安全公告。GPT-5.6 Sol 主要负责发现漏洞，作者进行了验证；文章文字由作者撰写，PoC 大部分代码由 Claude 编写。

- 🐞 漏洞属于一键式通用 XSS，攻击者可利用 uBlock Origin 的元素选择器添加恶意受信任过滤器。
- 🎯 受信任过滤器能够向页面注入 JavaScript，因此攻击者可在其他网站甚至任意站点执行任意 JS。
- 🧩 元素选择器通过注入 `moz-extension://.../web_accessible_resources/epicker-ui.html` iframe 实现，并能与扩展后台通信以添加过滤器。
- 🕵️ 攻击第一步是获取扩展内部随机 UUID；可利用默认过滤器 `no-fetch-if` 内部发起的 XHR，通过劫持 `XMLHttpRequest.prototype.open` 提取 `moz-extension://` URL 中的 UUID。
- 🪟 获取 UUID 后，攻击者可创建不可见 iframe 嵌入元素选择器，并通过 `MessageChannel`/`postMessage` 驱动选择器。
- 💉 关键漏洞在于选择器接受攻击者消息；攻击者可滥用 `opt` 字段插入换行，构造如 `image\ngoogle.com##+js(trusted-rpnt, script, ...)` 的任意受信任过滤器。
- 🖱️ 攻击者还可将 iframe 设为透明或覆盖页面，诱导用户点击不可见的“Create”按钮，从而完成过滤器添加。
- 🔒 修复措施之一是引入只有真实元素选择器才能从内容脚本获得的秘密口令，并在初始 `postMessage` 中校验。
- ⏳ 元素选择器添加的过滤器通常被视为受信任，直到重新编译；攻击者可立即打开受害者页面，因此实际风险较高。

---

### [我们在3周内将10,144个测试从Jest迁移到Vitest：一份诚实、AI辅助的真相 - DEV社区](https://dev.to/subito/we-migrated-10144-tests-from-jest-to-vitest-in-3-weeks-the-honest-ai-assisted-truth-527)

**原文标题**: [We Migrated 10,144 Tests from Jest to Vitest in 3 Weeks: The Honest, AI-Assisted Truth - DEV Community](https://dev.to/subito/we-migrated-10144-tests-from-jest-to-vitest-in-3-weeks-the-honest-ai-assisted-truth-527)

概述：Subito 前端团队在约 3 周内将 8 个仓库的 Jest 测试套件迁移到 Vitest 4（2026 年 8 月），实际执行 10,144 个单元测试、覆盖 1,799 个测试文件；迁移借助 Claude Code 完成大量机械转换，但并非“即换即跑”，需要 worker/pool 调优、修复被 Jest 隐式 mocking 掩盖的问题，并经历一次回滚。

- 📊 迁移规模：8 个仓库、1,799 个测试文件、10,144 个实际执行的单元测试，约 3 周完成，0 个仓库停留在半迁移状态。
- 🤖 AI 作用：将数千个重复、定义明确的转换交给 Claude Code；没有 AI 难以在此时间线完成，但工程师仍需做池选择、验证修复和判断是否完成。
- 🧭 迁移原因：Jest 的 CommonJS/ESM 摩擦、Jest 专用工具链臃肿，以及维护成本成为持续性工程负担；同时生态正向 Vitest/Vite 倾斜。
- ⚠️ ESM 痛点：next/jest 默认跳过 node_modules 转换，ESM-only 依赖会破坏 Jest；团队曾维护 transformIgnorePatterns 白名单，甚至因 uuid v14 纯 ESM 而移除依赖。
- ⚡ 性能不是自动提升：至少两个仓库中，未调优的 Vitest 反而更慢；一个仓库因 worker 上限导致约 35 秒测试变成约 3 分钟，执行时间本身接近。
- 🧵 Worker 调优：通过提高 maxWorkers（如 2→8）解决池/worker 开销；另一仓库基准中 6 workers 为甜点（26.6 秒），继续增加无益。
- 🧱 Pool 选择是正确性问题：最终所有仓库改用 forks，因真实子进程能让环境变量在 Node 初始化前生效；threads 会导致 TZ 等变量过晚生效，造成 CI 快照问题。
- 🪤 隐式 mocking 陷阱：Jest 的 __mocks__ 会静默全局生效，Vitest 需要显式 vi.mock()；迁移后暴露了遥测定时器未处理 rejection、错误追踪 SDK 调用变 undefined、组件测试走错代码路径等隐藏问题。
- ↩️ 回滚正常化：一个仓库合并迁移后出现非确定性 flaky 测试，团队立即 revert，调查后约 5 天成功重试；这不是失败，而是大型变更的正常过程。
- ⚖️ Jest 仍有优势：多年稳定“开箱即用”，无需思考 pool/worker；自动 mocking 减少显式 mock；至少两个仓库中未调优 Jest 比未调优 Vitest 更快。
- 💰 AI 成本：约 25 万输入 token、970 万输出 token、14.6 亿缓存读/6000 万缓存写，匹配 70 个会话（7/8 仓库）；估算约 751 美元，约 107 美元/仓库，但因缓存折扣假设和关键词过滤，应视为上限。
- 📦 公开迁移技能：团队将通用化 Jest→Vitest 迁移 skill 开源，包含逐文件迁移规则和踩坑经验，供其他团队复用。

---

### [BrowserPod 4.0：可在浏览器中运行的微型虚拟机，现已免费供任何用途使用](https://browserpod.io/blog/browserpod-40/)

**原文标题**: [BrowserPod 4.0: the microVM that runs in the browser, now free for any use](https://browserpod.io/blog/browserpod-40/)

BrowserPod 4.0 发布：这是一个基于 WebAssembly、可在浏览器中运行的类 Linux microVM，现已免费开放给任何用途使用。无需账号或 API key，不计费、无遥测，支持个人、商业和生产环境。它让网页获得本地隔离的 Linux 环境，具备零延迟与零云端扩展成本，主要面向 AI 代理、浏览器内 IDE/演示，以及嵌入 AI 辅助开发的平台。

- 🚀 核心变化：BrowserPod 从托管计费服务转为可免费使用的库，安装 `@leaningtech/browserpod` 后调用 `BrowserPod.boot` 即可启动。
- 🆓 新许可证：BrowserPod Community Licence 允许任意用途免费使用，无使用量限制；已发布运行时版本不可变并长期可用；自托管、打包或再分发需企业许可证。
- ⚡ 技术架构：从零为 Web 平台编写的类 Linux 内核，运行 WebAssembly 程序；支持 Node.js、Rust、git、bash、npm、pnpm，Python 为预览版，Go 即将推出。
- 🧩 运行方式：进程在各 Web Worker 中并行运行，共享虚拟化系统与按需加载、可持久化的流式文件系统，启动快、占用小。
- 🌐 新 fetch 网络：无需 API key，出站 HTTP/HTTPS 由浏览器 `fetch()` 或自定义 fetch 实现发送；TLS 终止与 CA 均在页面内完成，但受 CORS 限制，暂不支持入站流量和 Portals。
- 🔐 Edge 网络：原托管代理更名为 BrowserPod Edge，仍需 API key；新增按 key 的域名策略，并支持任意端口 TCP 连接，Free 计划也可用。
- 🖥️ 新工具：基础镜像加入 OpenSSH、ripgrep、fd 和基于 Rust 的 pnpm 12；可直接作为 SSH 客户端，或更快速地安装 Node.js 依赖。
- 🎯 适用场景：AI 代理自行运行代码、浏览器内 IDE/Playground/文档演示，以及让 AI 辅助开发在用户设备本地执行；长时间、无头、GPU 工作负载仍应使用云沙箱。
- 🛠️ 后续路线：fetch 网络入站流量（Portals/Service Worker）、Go 工具链、C/C++ SDK、Python 原生模块动态加载。

---

### [更新日志直播 | Sentry](https://sentry.io/resources/changelog-live/?utm_source=javascriptweekly&utm_medium=paid-social&utm_campaign=brand-fy27q4-changeloglive&utm_content=newsletter-sponsored-link-register)

**原文标题**: [Changelog Live | Sentry](https://sentry.io/resources/changelog-live/?utm_source=javascriptweekly&utm_medium=paid-social&utm_campaign=brand-fy27q4-changeloglive&utm_content=newsletter-sponsored-link-register)

Sentry 将举办 Changelog Live 直播，集中展示最新版本与实用调试能力，涵盖更快的故障调查、AI 工作流集成、SDK/集成/告警更新，并提供录制与实时问答。

- 📺 **直播活动**：Sentry Changelog Live 将展示最新发布内容，以及一些你可能错过的更新，帮助你和你的代理调试错误与性能问题。
- 🔍 **更快调查**：提供更多错误上下文、更智能的问题分类、更丰富的搜索，以及可跨技术栈拉取数据的升级版 Seer Agent。
- 🤖 **AI 工作流**：展示 Sentry 如何融入 AI 工作流，包括用 Seer 修复生产问题，以及追踪和调试你构建的代理。
- ⚙️ **技术速览**：快速介绍 SDK 更新、新集成和告警改进。
- 🎙️ **录制与问答**：活动将录制，并设有实时 Q&A，可保存席位了解最新动态。
- 🎧 **播客赞助**：Sentry 赞助了 Syntax Podcast，可在喜欢的收听平台收听。

---

### [Kitesurf 现已开源 | Cloudflare 博客](https://blog.cloudflare.com/kitesurf-open-source/)

**原文标题**: [Kitesurf is now open source | Cloudflare Blog](https://blog.cloudflare.com/kitesurf-open-source/)

Cloudflare 宣布将面向 AI Agent 的无状态浏览器 Kitesurf 开源，采用 Apache 2.0 许可证，代码托管于 GitHub，可本地运行、修改并部署到 Cloudflare Workers。

- 🧩 **开源发布**：Kitesurf 已在 GitHub 开源，开发者可查看代码、本地运行、修改，并部署自己的实例。
- 🦾 **为 Agent 设计**：Kitesurf 完全运行在 Cloudflare Workers 上，无需浏览器容器，可解析 HTML、应用 CSS、执行页面 JavaScript 并生成截图。
- 🔌 **兼容 CDP**：支持 Chrome DevTools Protocol，可连接 Puppeteer 等客户端，方便 AI Agent 控制浏览器。
- ⚡ **轻量高效**：目标是比 Chromium 等完整浏览器使用更少 CPU 和内存，并借助 Cloudflare 全球 Workers 网络按需扩展。
- 🧱 **核心组件**：基于 Blitz、Stylo、Boa、Linebender 库和 Krilla 等开源 Rust 包编译为 WebAssembly；主要分为 Engine、PageScript、PageRenderer 三部分。
- 🖥️ **本地与部署**：提供 Kitesurf CLI；本地可通过克隆仓库、安装依赖并运行开发服务器启动，也可部署到自己的 Cloudflare 账户。
- 💳 **部署要求**：部署到 Cloudflare 账户需要 Workers Paid 计划，因为 Kitesurf 使用 Dynamic Workers 为页面创建隔离 Worker。
- 🛠️ **欢迎贡献**：项目仍在快速开发中，重点提升兼容性、可靠性和效率；欢迎提交最小复现、修复、测试和文档改进。
- 📈 **持续更新**：可通过博客、更新日志、Web Platform Tests 页面和基准测试关注项目进展，并在 Discord 与团队交流。

---

### [GitHub - flyfish-dev/file-viewer: Preview 275+ file formats in the browser: Office, PDF, OFD, CAD, 3D, archives. Pure frontend, no server conversion. Vue / React / Svelte / Web Components. · GitHub](https://github.com/flyfish-dev/file-viewer)

**原文标题**: [GitHub - flyfish-dev/file-viewer: Preview 275+ file formats in the browser: Office, PDF, OFD, CAD, 3D, archives. Pure frontend, no server conversion. Vue / React / Svelte / Web Components. · GitHub](https://github.com/flyfish-dev/file-viewer)

File Viewer 是一个纯前端的浏览器文件预览库，支持 275+ 种文件格式（Office、PDF、OFD、CAD、3D、压缩包等），无需服务器转换即可渲染，兼容 Vue、React、Svelte 与 Web Components，并提供 Flutter SDK 开发预览版，采用 Apache-2.0 许可（CAD 运行时为 AGPL-3.0-only）。

- 📄 支持 275+ 种文件格式（225 稳定、50 实验性），横跨 47 条预览管线，涵盖 Office、PDF/OFD、DWG/DXF、STEP/IFC、压缩包、邮件、图像、媒体、代码、DICOM 等
- ⚡ 内置渲染器无需转换服务器，文件在浏览器中解析渲染；Workers、WASM 与字体可自托管以满足离线网络
- 🧩 按文件格式懒加载重型引擎（PDF、CAD、Office、3D 等），一套 API 适配 Web Component、Vue 3/2.7/2.6、React 16.8–19、Svelte 和 jQuery
- 🚀 快速上手：`npm install @file-viewer/web-full` 后通过 `mountViewer` 挂载；新项目可用 `npm create file-viewer@latest`，存量项目可用 `npx file-viewer-cli@latest add .`
- 🌐 离线 UI 内置 7 种语言：简体中文、英语、日语、繁体中文（台湾/香港）、德语、俄语，可通过 `options.locale` 切换
- 📱 独立的 Flutter SDK 已发布开发预览版 0.1.0-dev.2，覆盖 Android、iOS、Web、Windows、macOS 和 Linux
- 📦 八款 `*-full` 包保留 v2.4 preset-all 兼容基线（221 扩展、32 条管线）；Adobe 设计文件、DICOM、二进制检查等新渲染器需显式安装
- ⚠️ 仅为查看器而非编辑器；字体、厂商特性、加密文件与超大输入可能影响保真度或内存，生产使用前应查阅格式矩阵并用真实文件测试
- 🛠️ Full 包包含版本匹配的 Worker、WASM、字体等资源，需随应用一起部署，默认路径为 `<deployment-base>/file-viewer/`；Vite 用插件复制，Webpack/Rspack/Rollup 等用复制命令
- 🤝 若文档化格式预览失败，需提供脱敏样本或公开复现链接、浏览器版本与预期结果；维护通过 GitHub Sponsors 支持，企业需求可走企业支持
- 📜 自身源码为 Apache-2.0；DWG/DWF/DWFX 运行时（`@flyfish-dev/cad-viewer`、`dwf-viewer`）为 AGPL-3.0-only，使用或分发 CAD 功能需遵守该许可
- 🔗 PDF URL 默认同源流式加载，CORS 签名 URL 可配 `pdf.streaming: true` 并指定文件名/类型；Range 读取需同时设 `pdf.disableStream` 与 `pdf.disableAutoFetch` 为 `true`

---

### [文件查看器 - Office、PDF、CAD 浏览器文件预览](https://file-viewer.app/)

**原文标题**: [File Viewer - Office、PDF、CAD 浏览器文件预览](https://file-viewer.app/)

File Viewer 是一个纯前端、离线优先且支持私有化部署的文件预览组件生态，覆盖多种业务文件格式，并维护大量 npm 发布目标、扩展名与预览链路；同时针对 PPT/PPTX 采用隔离的浏览器原生预览链路，并明确了 Full 资产复制规则与关键入口资源。

- 🧩 纯前端、离线优先、可私有化部署，定位为文件预览组件生态
- 📂 支持 Office、PDF、OFD、Typst、XMind、CAD、EDA、压缩包、邮件、媒体、代码、3D、地理数据等业务文件
- 📦 当前源码维护 89 个 npm 发布目标、275 个已注册扩展名、47 条预览链路
- ✅ 其中 225 个链路稳定，50 个为实验性链路
- 🖥️ 二进制 PPT 与 PPTX 使用彼此隔离的浏览器原生链路
- ⚙️ Full 资产契约延续自 2.1.30：Vite 用 copyAssets:true 自动发布包内资产；非 Vite 项目运行一次包内复制 CLI；完整 web-full dist 无需复制
- 🔗 关键入口包括在线 Demo、官方文档、GitHub 开源总仓、npm 生态包及 v3.3.4 release reference

---

### [Flashwright：最快的端到端测试框架，Playwright 的即插即用替代方案](https://flashwright.dev/)

**原文标题**: [Flashwright: the fastest end-to-end testing framework, a drop-in Playwright](https://flashwright.dev/)

Flashwright 是可直接替换 Playwright 的超快端到端测试框架，保持相同 API、测试运行器与 `npx playwright test` 命令，现有测试套件无需修改即可运行，并在基准测试中显著快于 Playwright 及其他主流工具。

- 🚀 直接替换 Playwright：导入、配置、命令行、浏览器、报告器、Trace Viewer 和 VS Code 扩展均沿用 Playwright。
- ⚡ 性能突出：24 个 TodoMVC 测试在 1 worker 下为 2.36 秒，Playwright 为 4.48 秒；4 workers 下为 1.47 秒，Playwright 为 3.02 秒。
- 🥇 对比 9 种工具仍最快：同一机器、同一 Chromium、各自推荐等待与隔离策略下，Flashwright 中位耗时最低。
- 📦 安装简单：`npm i -D @playwright/test@npm:flashwright-test`，随后继续使用 `npx playwright test`。
- 🛠️ 提速机制：复用热浏览器但重置上下文、页面变化驱动等待、输入不等待动画、提前启动 workers、V8 代码缓存、更快截图编码。
- 🤖 适合编码代理：暖会话下重跑一个 TodoMVC 测试仅 72 毫秒，Playwright 为 652 毫秒；MCP 支持自适应等待。
- ⚙️ 默认更快但可配置：`isolation: 'recycled'`、`failFastWhenIdle: true`、`waitForAnimations: false`、`testOrder: 'longest-first'` 等。
- 🔄 可恢复 Playwright 行为：可在项目、文件或 `describe` 块中逐项开启 Playwright 默认行为。
- 🌐 浏览器差异：主要提升 Chromium；Firefox 与 WebKit 基本保持 Playwright 行为，仅复用每 worker 一个标签页。
- ✅ 兼容性验证：Playwright 自有测试套件在 Chromium 上通过 2610/2610，runner、library 和 MCP 套件与 Playwright 1.64.1 一致。
- ↩️ 可随时回退：执行 `npm i -D @playwright/test@1.64.1` 即可，代码中不引用 Flashwright。

---

### [Flashwright：我如何将 Playwright 提速 2-4 倍 — Codebeast](https://codebeast.io/blog/flashwright)

**原文标题**: [Flashwright: how I made Playwright 2-4Ã faster â Codebeast](https://codebeast.io/blog/flashwright)

Flashwright 是 Playwright 1.64.1 的兼容分支，保留原有 API、测试运行器和 `npx playwright test` 命令；通过复用上下文、减少轮询等待、缓存与底层通信优化等手段，让同一套端到端测试运行速度快 2–4 倍，平均约 2.83 倍，目标是替换包后即可继续使用现有测试。

- ⚡ **性能提升显著**：在 20 个基准场景中至少快 2 倍，平均 2.83 倍；TodoMVC 单 worker 从 3617ms 降至 968ms，约 3.74 倍。
- 🧠 **最大瓶颈在浏览器冷启动**：Playwright 每个测试新建 browser context，导致应用 JavaScript 反复编译；Flashwright 改为每个 worker 复用一个 context，每个测试开新标签页并重置状态。
- 🛠️ **默认优化丰富**：包括上下文复用、页面变化时立即重试、空闲时提前失败、跳过输入前动画帧等待、提前启动 worker/浏览器、长测试优先、代码缓存、CBOR 浏览器消息、更便宜的 locator 与截图处理等。
- 🔄 **可选优化有取舍**：如 `workersPerProcess`、`preloadPages`、`instantAnimations`、`blockResources`、`locatorPolicy: 'test-id'`，默认关闭，因为会牺牲隔离性、兼容性或资源加载完整性。
- ❌ **改 Chromium 不划算**：团队尝试从源码构建 Chromium 并逐项测量，但收益太小，不足以维护浏览器 fork；Flashwright 仍使用 Playwright 官方浏览器构建。
- ⚠️ **行为默认值有变化**：上下文会重置复用而非每次新建；指针操作不等待动画；断言可能在页面空闲时提前失败；多 worker 时最长测试先跑；本地暖会话会保留浏览器最多 5 分钟。
- ✅ **兼容性较好**：在 Chromium 上通过 Playwright 自身 `tests/page` 的 2616/2616 项测试；runner、library、MCP、Electron、extension 套件与原始 Playwright 1.64.1 基本一致。
- 📦 **替换方式简单**：执行 `npm i -D @playwright/test@npm:flashwright-test`，再运行 `npx playwright install chromium` 和 `npx playwright test`；需要 Node.js 22.18+。
- 🧪 **基准方法可靠**：每个数字取完整测试命令 15 次运行的中位数，在同一台 6-CPU Linux 机器和 Chromium headless shell 上对比。
- 📜 **开源与反馈**：项目采用 Apache-2.0 许可证，仓库包含基准、完整选项文档和源码，并欢迎提交问题与 PR。

---

### [React Flow 13 - xyflow](https://xyflow.com/blog/react-flow-13-major-release)

**原文标题**: [React Flow 13 - xyflow](https://xyflow.com/blog/react-flow-13-major-release)

React Flow 13 于 2026 年 11 月 16 日正式发布，距上次大版本已两年。此次升级以性能优化和开发者体验改善为核心，同时回顾了 React Flow 生态的快速增长、Strudel Flow 与 Pro 内容进展，并预告 Vue Flow 加入 xyflow 家族等后续动态。

- 🚀 **React Flow 13 发布**：新版本带来显著性能提升和多项开发者体验改进，并提供迁移指南帮助升级。
- 📈 **生态增长迅猛**：React Flow 月下载量从 2024 年的 100 万增长到预计突破 6000 万，约占 React 下载量的 6–8%。
- 🧩 **应用案例丰富**：Google Stitch、Figma Weave、Supabase 的 database.build 等项目都在使用 React Flow，社区展示区也持续开放投稿。
- 🎵 **Strudel Flow 更新**：基于 Strudel 实时编码语言的音乐创作工具新增社区音色/补丁投稿功能，支持在模块化硬件风格界面中创作音乐。
- 💎 **Pro 内容扩展**：React Flow Pro 订阅用于资助库的持续开发，现可直接在 reactflow.dev 访问自由手绘、libavoid 复杂边路由、AI 工作流构建器模板等 Pro 示例。
- ⚡ **性能优化是重点**：为升级 Zustand 5 并解决 Vite 8 等现代构建问题而启动的维护版本，最终演变为大规模性能更新。
- 🧠 **状态管理重构**：不再使用单一全局 store，改为多个专用 hook，分别处理配置、节点、边、选择和连接等状态。
- 🔄 **减少不必要的重渲染**：新增 useNode 和 useEdge hook，让组件只订阅自己关心的节点或边。
- 🛠️ **开发体验提升**：不再发布 UMD 包，转向 ESM；最低要求 React 18，并借助 React Compiler 获得优化。
- 📦 **源码与调试更友好**：包内包含 src/ 目录和 source map，编辑器中的“转到定义”可直接跳转到 API 背后的源码。
- 👨‍👩‍👧 **父子节点处理更简单**：父节点不再必须排在子节点之前；useReactFlow 新增 changeParentNode 工具，可自动更新新父节点边界以包含子节点。
- 🎨 **样式与颜色模式改进**：自动检测深色/浅色模式，样式支持分层控制，并新增可通过 @xyflow/react/xy-theme.css 引入的 xy-theme.css 主题。
- 🔮 **后续动态**：Vue Flow 正式加入 xyflow 家族并发布 Vue Flow 2；Strudel Flow 2 也已发布，带来新的可视化音乐创作方式。

---

### [Vue Flow 加入 xyflow！ - xyflow](https://xyflow.com/blog/vue-flow-joins-xyflow)

**原文标题**: [Vue Flow joins xyflow! - xyflow](https://xyflow.com/blog/vue-flow-joins-xyflow)

overview summary  
Vue Flow 及其开发者 Burak 正式加入 xyflow，并发布 Vue Flow 2：统一包结构、共享底层核心、对齐 API，同时带来显著性能提升，并保留 Vue 原生开发体验。

- 🤝 2026年11月17日宣布，Vue Flow 与开发者 Burak 正式加入 xyflow 家族。
- 📈 Vue Flow 五年前作为聊天机器人爱好项目起步，现已达到每周 100 万 npm 下载，并被 DHL、Huawei 内部工具及 n8n、Kestra 等产品使用。
- 🌐 Vue Flow 网站已改版，与 React Flow、Svelte Flow 的示例和指南对齐；代码迁入 xyflow monorepo，Burak 将继续主导开发，并于明年全职加入。
- 📦 Vue Flow 2 将核心库及背景、控件、小地图、节点缩放器、节点工具栏等整合为单一 @xyflow/vue 包。
- ⚙️ 底层改用共享 @xyflow/system，统一缩放、平移、拖拽、连接、边路径和测量核心，并对齐节点/边模型、访问器、store、CSS 变量和 DOM 结构，同时保留 Vue 惯用 API。
- 🚀 性能显著提升：挂载 100/900 节点分别快 31%/53%，拖动 50/100 节点快 25%，拖动 900/900 节点快 55%。
- 🔁 性能提升主要来自不可变节点与边：不再追踪就地修改，需通过 useVueFlow store helpers 或不可变重新赋值来更新。
- 🧭 官方提供迁移指南和快速开始指南，并推荐 Vue Flow Pro 以获取高级指南并支持项目可持续发展。

---

### [GitHub - 6pac/SlickGrid：一个闪电般快速的 JavaScript 网格/电子表格 · GitHub](https://github.com/6pac/SlickGrid)

**原文标题**: [GitHub - 6pac/SlickGrid: A lightning fast JavaScript grid/spreadsheet · GitHub](https://github.com/6pac/SlickGrid)

6pac SlickGrid 是一个高速 JavaScript 网格/电子表格库的主基础仓库，源自2014年停止更新的 mleibman/SlickGrid，并持续扩展插件、现代构建方式与零依赖能力；Angular、React、Vue 等框架的官方封装可参考 Slickgrid-Universal。

- ⚡ 项目定位：闪电般快速的 JavaScript 网格/电子表格，采用 MIT 许可，GitHub 约 2.1k 星、429 个 Fork。
- 🧩 插件扩展：在原始 SlickGrid 基础上增加 RowDetail、CellMenu、ContextMenu、GridMenu、CustomTooltip、GridState 等插件。
- 🔁 版本演进：v2 合并 X-SlickGrid 实现行列冻结；v3 移除 jQueryUI 改用 SortableJS；v4 移除 jQuery；v5 迁移 TypeScript 并提供 IIFE/ES6/ESM 构建与 Alpine 主题；v6 重写 Pinning、新增 Sticky 行列并移除 SortableJS，实现零依赖。
- 🧱 框架支持：提供 ES6/ESM 构建，可配合多数框架使用；Angular、React、Vue 等可使用 Slickgrid-Universal 官方封装。
- 🛠️ 使用门槛：TypeScript 并非必需，可用普通 JavaScript，通过 dist/browser、ESM 或 CDN 使用；jQuery 自 v4 起完全可选。
- 📚 文档与示例：提供文档网站、Vite 演示、Stackblitz 演示、Examples Wiki 与 GitHub Releases。
- 📦 安装方式：支持 CDN 独立 script（IIFE）、Alpine 主题 CSS，以及 npm 安装后通过 ESM import 或 require 使用。
- ✅ 测试与贡献：大量示例带有 Cypress E2E 测试，覆盖 50+ 示例、约 800 项测试，并在 GitHub Actions CI 中运行；欢迎贡献。
- 🔒 CSP 合规：自 v5.5.0 起大部分符合 CSP，但使用 HTML 字符串模板时需结合 sanitizer 与 DOMPurify 返回 TrustedHTML 才能完全合规。
- 📝 其他信息：提供迁移指南，并有关于最新版本最激动人心变化的小型调查。

---

### [SlickGrid 示例：固定列和行](https://6pac.github.io/SlickGrid/examples/example-pinning-columns-and-rows.html)

**原文标题**: [SlickGrid example: Pinned Columns and Rows](https://6pac.github.io/SlickGrid/examples/example-pinning-columns-and-rows.html)

该示例展示 SlickGrid 的固定行与固定列功能，以及基于 DataView 过滤模型的高性能实时网格交互；即使数据量很大，也能流畅进行排序、筛选、滚动、导航和编辑。

- 📌 固定行可位于顶部/底部，固定列可位于左侧/右侧，并通过 Apply 应用设置。
- ✅ 支持选择前 10 行。
- 🔄 使用经过筛选的 DataView 模型作为数据源，而不是简单数组。
- ⚡ 网格会响应模型事件（onRowCountChanged、onRowsChanged），并实现 DataView 重算与实时更新。
- 🚀 即使网格包含 50,000 行，也能像只有 50 行一样进行排序、筛选、滚动、导航和编辑。
- ➕ 支持新增行和双向排序。
- ⚙️ 列选项包含 cannotTriggerInsert；相关事件包括 onCellChange、onAddNewRow、onKeyDown、onSelectedRowsChanged、onSort。
- 🧩 所有筛选条件都会立即应用于新增或编辑过的行。
- 🎯 涵盖模型变更时的行选择处理、分页和内联筛选面板。
- 🔗 可在 Github 查看源代码；支持按标题包含指定内容显示任务。

---

### [SlickGrid](https://6pac.github.io/SlickGrid/)

**原文标题**: [SlickGrid](https://6pac.github.io/SlickGrid/)

本内容介绍如何构建第一个网格，并掌握日常使用中的选项、列、事件及 DataView 基础知识。

- 🧱 构建你的第一个网格
- ⚙️ 学习常用配置选项
- 📊 了解列的使用
- 🎯 掌握事件处理
- 🗂️ 认识 DataView 基础知识

---

### [Announcing XState v6 beta | Stately](https://stately.ai/blog/2026-11-05-xstate-v6-beta)

**原文标题**: [Announcing XState v6 beta | Stately](https://stately.ai/blog/2026-11-05-xstate-v6-beta)

XState v6 首个 beta 发布，作为新的主版本，目标是让状态机与状态图更易读、易写、易验证，并可在内存、无服务器函数或持久化执行主机等任意环境运行。它延续 MIT 开源、零依赖的状态管理与编排定位，并针对 AI agent 大量编写代码的趋势强化类型、文档和工具反馈。

- 🚀 **发布与安装**：可通过 `npm i xstate@beta` 试用；核心 API 已视为稳定，持久化执行等新 API 仍为实验性。
- 🧠 **面向 Agent 设计**：减少 API 学习成本，强化类型错误、包内文档和 CLI 反馈，让 agent 或人类能从代码、类型和文档中获得正确答案。
- 🧩 **转换即函数**：v6 中 transition 可写成普通函数，接收 `context`、`event` 等并返回下一状态与上下文更新；副作用用 `enq` 入队，不再需要 action creators 和 guard 属性。
- 🛡️ **更强类型安全**：用 Zod 或 Standard Schema 声明 `schemas`，事件、上下文和 `on` 键均受类型检查；新增 typestates 与 state input 精确描述状态相关数据。
- 🪶 **轻量 FSM 回归**：`xstate/fsm` 回归，约 0.5 kB min+gzip，语法与完整状态机一致，可无缝升级到 `xstate`。
- 📚 **包内文档与 CLI**：安装包自带对应版本文档和 agent guide；CLI 支持 `inspect`、`validate`、`simulate`、`test`、`replay`、`diff`、`migrate`，操作 JSON 且不运行应用代码。
- 🖥️ **可视化编辑器**：新编辑器支持 XState v6，可展示函数式 transition 的条件与上下文更新，并通过 Editor Sync 与代码双向同步。
- ⏳ **持久化执行**：实验性 `xstate/durable` 模块让纯 transition、稳定 effect ID 和确定性 actor 地址适配持久化主机，支持 journal/replay。
- 🤖 **Agent 状态机**：仓库新增大量 agent 示例，包括工具循环、人工审批、模型回退、流式响应、RAG、MCP 和多 agent 编排；Stately Agent 2.0 处于 alpha。
- ✨ **其他改进**：并行区域保持、状态级 `onError`、未处理事件、choice states、状态超时、时长字符串、route states、actor registry、快照版本化等。
- 🧹 **移除与统一**：移除 action creators、高阶 guards、字符串 transition、`types`、`fromPromise` 等旧模式，改用 transition 函数、`enq`、`schemas` 和 `createAsyncLogic` 等；`interpret` 被移除。
- 🔄 **迁移与支持**：提供 `npx xstate migrate` codemod，支持 v5 与 v6 并存逐步迁移；XState v5 仍受支持，框架集成也提供 beta 版本。

---

### [Excalibur v1.0.0 发布！| Excalibur.js](https://excaliburjs.com/blog/excalibur-1-0-0-released/)

**原文标题**: [Excalibur v1.0.0 Released! | Excalibur.js](https://excaliburjs.com/blog/excalibur-1-0-0-released/)

Excalibur.js 在历经 13 年开发后正式发布 v1.0.0，标志着引擎进入稳定版本阶段；未来将遵循语义化版本，尽量把破坏性变更视为 bug 修复或用特性开关处理，并提供 codemod 与升级工具。此次版本带来性能、2D 光照、着色器管线、序列化、音频混音、CLI 等大量更新，同时已有商业游戏登陆 Steam 与 Itch.io。

- 🎉 2026 年 11 月 11 日发布 v1.0.0，项目从 2013 年起步，历经 13 年达到首个正式大版本。
- 📦 开始遵循语义化版本；破坏性变更会尽量修补或特性标记，并提供 codemods 与 `create-excalibur upgrade` 降低迁移成本。
- 🎮 已有 Excalibur 商业游戏在 Steam、Itch.io 等平台发布，包括《Now THAT'S a Big Dragon!》《A Nibble Tale》等。
- ⚡ 性能优化显著：减少热循环对象分配、对象池、优化碰撞系统，并在 PR 中运行 benchmark 防止回退。
- 💡 新增 2D 光照：支持环境光、点光、锥光、遮挡物与阴影，可选开启，适合夜景、手电筒、火把等效果。
- ⏸️ 新增暂停系统：通过 `PauseComponent`、场景 `pause()`/`resume()` 实现暂停，同时可让 UI/HUD 继续运行。
- 🧩 着色器管线增强：材质与后处理支持多 pass 组合，便于实现 Blur、Glow、Bloom；`glsl` 标签简化预乘 alpha 与 GLSL 样板代码。
- 💾 新增序列化 API：支持内置与自定义类型 JSON 序列化/反序列化，适合存档、localStorage 和多人同步，并可结合插件实现自动保存。
- 🔌 新增插件 API 与自定义渲染器：可安装 ECS 系统、自定义渲染器、生命周期钩子；渲染器可自定义顶点布局，实现水面等特殊效果。
- 🔊 音频系统重构为真正混音器：支持通道/主总线、音量与静音增益节点、效果节点、空间音频、分层自适应音乐、音高与并发控制。
- 🛠️ CLI 工具增强：`create-excalibur` 支持脚手架、升级、诊断、生成资源、离线文档搜索与 MCP 服务；全局 `ex` 命令提供快捷操作。
- 🧭 其他重要功能：核心 A* / Dijkstra / BFS / DFS、NineSlice、像素艺术模式、GPU 粒子、协程、场景转场、贝塞尔曲线、输入映射、TiledSprite、固定更新、调试绘制、类型化事件等。
- 🔄 迁移 v1：推荐使用 `npx create-excalibur@latest upgrade` 进行 codemod 式升级。
- 🔮 未来计划包括 WebGPU + HTML-in-Canvas、Excalibur 编辑器、主机移植、首届 Excalibur Game Jam，以及 Caliburn Games 的商业游戏。
- 🙏 特别致谢核心团队、长期贡献者与美术作者 HintOfLime，强调社区持续贡献推动引擎走到 v1。

---

### [示例 | Excalibur.js](https://excaliburjs.com/samples/)

**原文标题**: [Samples | Excalibur.js](https://excaliburjs.com/samples/)

该页面汇总了 Excalibur 的示例游戏与模板，每项均提供演示和代码，覆盖 UI、平台跳跃、寻路、地图、物理、桌面发布等常见游戏开发场景。

- 🎮 Excalitris：用 Excalibur 构建的俄罗斯方块克隆，演示如何用 React 作为 UI。
- 🍮 Jelly Jumper：高保真平台游戏示例，跳跃物理灵感来自《超级马力欧世界》。
- 🧭 Pathfinding：使用寻路插件演示 A* 与 Dijkstra 算法。
- 🖥️ UI with HTML/CSS/JS：在 canvas 上方叠加 HTML 层，构建原生 HTML/CSS/JS UI。
- 🧠 Tiny Tactics：高保真战术游戏示例，包含多关卡、AI 和寻路。
- 🔲 Grid Movement：展示基于网格的移动方式。
- 🗺️ Tiled 系列：Tiled 插件分别配合 Parcel、Vite、Webpack 打包器的小关卡示例。
- 🏃 Platformer：小型平台游戏示例。
- ⚙️ Matter.js：演示接入第三方物理引擎替代 Excalibur 自带物理。
- 💻 Electron Template：Electron 集成模板，便于将游戏发布到桌面或 Steam。
- 🐦 Excalibird：热门手游 Flappy Bird 的克隆示例。
- 🚀 Shoot 'Em Up：创建射击游戏（Shoot 'Em Up）的示例。
- 🧱 Breakout：打砖块游戏示例。

---

### [发布 3.0.0 · bfirsh/jsnes · GitHub](https://github.com/bfirsh/jsnes/releases/tag/v3.0.0)

**原文标题**: [Release 3.0.0 · bfirsh/jsnes · GitHub](https://github.com/bfirsh/jsnes/releases/tag/v3.0.0)

JSNES 3.0.0 发布，模拟核心升级为周期精确实现，CPU、PPU、APU 按真实硬件方式同步运行；AccuracyCoin 测试全部通过且性能略有提升。公共 API 保持不变，但因 2.x 存档不兼容而进行主版本升级。

- 🚀 **核心升级**：JSNES 3.0 用周期精确核心替换旧模拟核心，CPU、PPU、APU 同步运行。
- ✅ **测试提升**：AccuracyCoin 通过 134/134 项测试，高于 2.1.0 的 107 项。
- ⚠️ **破坏性变更**：2.x 存档状态不兼容；`nes.toJSON()` 增加 `version` 字段，`nes.fromJSON()` 加载旧存档会抛出“不兼容版本”错误，需捕获并丢弃旧存档。
- 🔇 **音频选项修复**：`emulateSound: false` 现在真正跳过音频合成，也不再调用 `onAudioSample`。
- 🧠 **CPU 重写**：改为周期步进的 6502，总线访问按 CPU 周期计时，并更准确模拟中断轮询、分支延迟、NMI 抢占、DMA 停顿与对齐周期等行为。
- 🎮 **PPU 重写**：实现点精确渲染器，包含滚动寄存器、背景取指流水线、精灵评估状态机及多种硬件怪癖。
- 🔊 **APU 精确化**：帧计数器、长度计数器、IRQ 标志和 DMC 精确到 CPU 周期，音频按输出样本合成。
- ⚡ **性能表现**：尽管模拟更精确，3.0 仍比 2.1.0 约快 4%，基准测试平均 967 fps 对 927 fps。
- 🧪 **测试覆盖**：加入约 80 个 `nes-test-roms` 测试 ROM，并检查不同 CPU/PPU/APU 上电对齐情况。

---

### [JSNES：一个 JavaScript NES 模拟器](https://jsnes.org/)

**原文标题**: [JSNES: A JavaScript NES emulator](https://jsnes.org/)

未提供可总结的文章内容，暂时无法生成要点摘要。

- 📄 请提供需要概括的文本内容。
- ✅ 收到内容后，我会按要求用中文输出概述摘要和带表情符号的“-”项目符号列表。

---

### [发布 v6.0.0 · sindresorhus/type-fest · GitHub](https://github.com/sindresorhus/type-fest/releases/tag/v6.0.0)

**原文标题**: [Release v6.0.0 · sindresorhus/type-fest · GitHub](https://github.com/sindresorhus/type-fest/releases/tag/v6.0.0)

type-fest v6.0.0 是一次重大版本更新，带来 120 个新类型、全部开放问题关闭，以及大量性能与正确性修复；同时包含多项破坏性变更和迁移要求。

- 🚀 版本规模：新增 120 个类型，所有 open issues 已解决，并包含大量性能和正确性修复。
- ⚙️ 运行环境：要求 TypeScript 6 和 Node.js 22，并要求 tsconfig 开启 `exactOptionalPropertyTypes: true`；`strict` 默认开启，不应关闭。
- ❌ 移除弃用类型：删除 `IfAny`、`IfNever`、`IfUnknown`、`IfNull`、`IfEmptyObject`，改用 `If` 配合对应 `Is*` 类型；删除 `ReadonlyTuple`，改用 `Readonly<TupleOf<...>>`。
- 🔤 大小写转换默认值变更：默认按标点分割；`CamelCase`/`PascalCase` 默认保留前导下划线且不按数字分割。例如 `KebabCase<'div.card::after'>` 变为 `'div-card-after'`，`CamelCase<'_id'>` 保持 `'_id'`。
- 🧩 深度类型默认行为变更：`PartialDeep`/`PartialOnUndefinedDeep` 默认启用 `recurseIntoArrays`，数组和元组元素也会深度可选；可用 `{recurseIntoArrays: false}` 恢复旧行为。
- 🔁 选项重命名/调整：`Split` 的 `strictLiteralChecks` 改为 `strict`；`StringToArray` 的 `mapNonLiteralsDirectly` 改为 `strict`，且含义相反；旧选项名会编译报错。
- 🕒 `ReadonlyDeep` 与 `Date`：`ReadonlyDeep<Date>` 现在转为 `ReadonlyDate`（无 `set*` 方法），`WritableDeep` 可转回 `Date`；也可用 `keep` 选项保留 `Date`。
- ✅ 谓词行为调整：多个谓词对 `never` 输入返回 `false` 而非 `never`；`IsNull`/`IsUndefined` 对 `any` 和 `never` 返回 `false`；`IsNull<any>` 由 `true` 变为 `false`。
- 🧱 `TsConfigJson` 更新：移除 TypeScript 5.5/6.0 已删除或弃用的 `compilerOptions` 和值，如 `baseUrl`、`outFile`、`module: 'AMD'`、`target: 'ES3'` 等。
- ✨ 新增类型覆盖广泛：包括 `AnyFunction`/`AnyAsyncFunction`、`ArrayChunk`/`ArrayZip`/`ArrayUnique`、`Curry`/`Pipe`、`JsonPointer`、`RouteParameters`、`ReadonlyDate`、`StrictEventTarget`、`TupleToEnum` 等。
- 🛠️ 改进：深度类型新增 `keep` 选项；`ConditionalKeys`/`ConditionalPick`/`ConditionalExcept` 新增 `strict` 选项；`Paths` 增加 `valueType`、`recurseIntoArrays`、`requiredOnly`、`maxCircularDepth`；比较类型支持 `bigint`，并优化 `Get`/`PickDeep`/`OmitDeep`/`Set*Deep` 性能。
- 🐞 修复重点：`Jsonify`、`Exact`、`PickDeep`、`OmitDeep`、`Merge`/`Spread`/`MergeDeep`、`Replace`、`Join`、大小写转换，以及深度类型对元组、函数和内置类型的处理等。
- 📦 迁移提示：升级 TypeScript/Node.js 与 tsconfig；替换被移除类型；按需传入旧的大小写或数组递归选项；检查谓词结果是否依赖 `never`/`any` 旧行为；处理 `ReadonlyDate` 兼容性。

---

### [GitHub - sindresorhus/type-fest：TypeScript 必备类型集合 · GitHub](https://github.com/sindresorhus/type-fest#api)

**原文标题**: [GitHub - sindresorhus/type-fest: A collection of essential TypeScript types · GitHub](https://github.com/sindresorhus/type-fest#api)

type-fest 是 Sindre Sorhus 维护的 TypeScript 类型工具集合，旨在补充许多本应内置的类型；它支持作为依赖安装或直接复制所需类型且无需署名，当前约有 17.5k stars、748 forks、51 watchers 与 1,615 commits，采用 MIT 或 CC0-1.0 双许可。

- 📦 安装方式：`npm install type-fest`，要求 TypeScript >=6、ESM、`strict: true`，并强制启用 `exactOptionalPropertyTypes: true`。
- 🧩 使用示例：可引入 `Except` 等类型，例如 `Except<Foo, 'rainbow'>` 会从对象类型中移除指定键。
- ⭐ 社区与协作：项目欢迎新增常用类型和文档改进；GitHub 界面显示仅协作者可创建 PR，README 建议先阅读贡献指南，并欢迎协助审查提案和 PR。
- 📚 API 范围广：覆盖基础类型、对象工具、类型守卫、JSON、结构化克隆、函数、异步、字符串、数组、数字、大小写转换与杂项工具。
- 🛠️ 对象操作：提供 `Except`、`Merge`、`MergeDeep`、`WritableDeep`、`ReadonlyDeep`、`PartialDeep`、`RequiredDeep`、`PickDeep`、`OmitDeep` 等。
- 🔒 修饰与约束：支持可选/必选/只读/可写/可空/非空、深层路径、互斥键、至少一个/恰好一个/全有或全无等约束。
- 🧠 类型推导与判断：包含 `ValueOf`、`ConditionalKeys`、`UnionToIntersection`、`IsEqual`、`IsUnion`、`IsAny`、`IsNever` 等实用类型。
- 🧾 JSON 与克隆：提供 `JsonValue`、`JsonObject`、`Jsonifiable`、`Jsonify`、`StructuredCloneable` 等类型。
- 🔧 函数与异步：包括 `FunctionParameters`、`Overloads`、`SetReturnType`、`Curry`、`Pipe`、`Uncurry`、`Promisable`、`Asyncify` 等。
- 🔤 字符串与数组：支持大小写转换、Trim/Split/Replace、`RouteParameters`、`Join`、`ArraySlice`、`TupleToUnion`、`UnionToTuple`、`ArrayZip`、`ArrayChunk` 等。
- 🔢 数字与字面量：提供有限数/整数/负数/非负数、比较与求和、`IntRange`、`LiteralUnion`、`Tagged`、`Flavor` 等。
- 🚫 拒绝类型与别名：文档记录被拒绝的类型及原因，并提供常见替代名称索引，便于发现兼容类型。
- 💡 实践提示：可扩展 `PackageJson`；声明文件出现 “cannot be named” 错误时，应为导出添加显式类型注解，并确保 `type-fest` 是直接依赖。
- 🔗 相关工具：推荐 `eslint-plugin-typefest`、`ts-extras` 与 `typed-query-selector`；内置类型示例涵盖 `Awaited`、`Partial`、`Pick`、`Record`、`Exclude`、`ReturnType` 等。
- 👥 维护与许可：由 Sindre Sorhus 等维护；MIT 与 CC0-1.0 双许可，SPDX 标识为 `(MIT OR CC0-1.0)`。

---

### [GitHub - foliojs/fontkit：适用于 Node 和浏览器的高级字体引擎 · GitHub](https://github.com/foliojs/fontkit)

**原文标题**: [GitHub - foliojs/fontkit: An advanced font engine for Node and the browser · GitHub](https://github.com/foliojs/fontkit)

fontkit 是一个面向 Node.js 和浏览器的高级字体引擎，被 PDFKit 使用，支持多字体格式、复杂字形替换与排版、字形路径提取、彩色 emoji、可变字体及字体子集化。

- 📦 支持 TrueType、OpenType、WOFF、WOFF2、TTC 和 DFont 等字体格式。
- 🔤 支持字符到字形映射，包括连字和高级替换；支持 GSUB、GPOS 及 AAT morx 表。
- 📐 支持字形度量、字距调整、复杂布局，以及 TrueType glyf 和 PostScript CFF 轮廓。
- 🎨 支持彩色字形（如 emoji），包括 Apple SBIX 表和 Microsoft COLR 表。
- 🧬 支持 AAT 可变字体，可调 weight、width 等轴，并提供命名变体与自定义变体。
- ✂️ 支持字体子集化，只保留指定字形以减小字体体积，适合 PDF 嵌入等场景。
- 🚀 安装方式为 `npm install fontkit`；可通过 `openSync`/`open`/`create` 打开或创建字体对象。
- 🧭 示例包括：`font.layout()` 排版、`glyph.path.toSVG()` 获取 SVG 路径、`createSubset()` 创建子集并 `encode()` 输出。
- 🧩 可按需导入 `fontkit/core` 并注册 `TTFFont`、`WOFFFont`、`WOFF2Font`、`TrueTypeCollection`、`DFont` 等格式模块。
- 🗣️ 提供 8 种 shaper：Default、Universal、Arabic、Indic、Hangul、Hebrew、Myanmar、Thai；`DefaultShaper` 始终作为回退。
- 🛠️ `registerShaper(Shaper, scripts)` 可按 OpenType 脚本标签注册 shaper，也支持自定义 shaper 继承内置类并声明脚本。
- 📊 字体对象提供元数据、度量、字符集、可用特性、字形映射、布局、变体和子集等 API。
- 🧱 Glyph 对象包含 id、name、codePoints、path、bbox、cbox、advanceWidth，并支持 `render(ctx, size)` 渲染。
- 🖋️ Path 对象支持 moveTo、lineTo、quadraticCurveTo、bezierCurveTo、closePath、toFunction、toSVG，以及 bbox/cbox。
- ⚠️ 当前子集生成的是面向 PDF 嵌入的最小字体，可能缺少 cmap 等独立使用所需表，未来会改进。
- 📈 仓库约有 1.7k stars、256 forks、693 次提交，采用 MIT 许可证。

---

### [Release 10.0.0 · timocov/dts-bundle-generator · GitHub](https://github.com/timocov/dts-bundle-generator/releases/tag/v10.0.0)

**原文标题**: [Release 10.0.0 · timocov/dts-bundle-generator · GitHub](https://github.com/timocov/dts-bundle-generator/releases/tag/v10.0.0)

dts-bundle-generator v10.0.0 是一次重大版本更新，重点包括包改为 ES 模块、CLI 从 yargs 迁移到 commander、提高最低 Node.js 和 TypeScript 版本要求，并带来大量命名冲突/重命名修复及大型项目性能提升。

- 📦 包现在为 ES 模块（`"type": "module"`），但仍可通过 Node.js 24 的 `require(esm)` 从 CommonJS 加载。
- 🚫 仅支持从主入口 `dts-bundle-generator` 和 `dts-bundle-generator/config-schema` 导入，其他深层导入（如 `dist/...`）不再可用。
- 🖥️ CLI 改用 `commander` 替代 `yargs`：布尔选项不再接受值（如 `--sort=false` 会报错），帮助信息布局略有变化，并新增 `-h`、`-v` 短选项。
- ⬆️ 最低支持 Node.js 24；最低支持 TypeScript 5.4，支持范围上限为 `<7`，并新增 TypeScript 6 支持。
- 🔧 `exportReferencedTypes` 默认改为禁用（`--export-referenced-types` 默认 `false`），仅导出根源文件导出的节点；显式启用时，若引用类型因重命名避冲突而无法导出，会生成失败。
- 🧩 配置文件现在既支持 CommonJS，也支持带默认导出的 ES 模块。
- ✅ 新增 `--check-project`（配置中为 `checkConfigPath`），可用单独的 tsconfig 校验生成文件，例如使用更严格选项验证输出。
- ⚠️ 新增 `--allow-unresolved-import-types`（配置中为 `compilationOptions.allowUnresolvedImportTypes`），无法解析模块的 `import()` 类型将保留并打印警告，而不是直接失败。
- 🏷️ 使用 `module` 关键字声明的命名空间（如 `declare module Foo {}`）现在打印为 `namespace`。
- 🐛 修复了 `esModuleInterop` 兼容性、未直接导出的顶层导出 JSDoc 被剥离、axios 1.7.8 打包错误、express 的 `Request`/`Response` 重命名错误、嵌套作用域遮蔽导致引用错误、`checkJs: true` 下 TS5055 回归等问题。
- ⚡ 对包含大量导出的项目进行了性能优化，CLI 启动速度也因移除 yargs 依赖而提升约 45ms/次。
- 🙏 感谢贡献者 `@mnaoumov`、`@matortheeternal` 和 `@slhck`。

---

### [2026年面向开发者的10个最佳文档解析API](https://developer-api.foxit.com/developer-blogs/api-guides-tutorials/best-document-parsing-apis/?utm_source=draftdev&utm_medium=newsletter&utm_campaign=javascriptweekly_20261117)

**原文标题**: [10 Best Document Parsing APIs for Developers in 2026](https://developer-api.foxit.com/developer-blogs/api-guides-tutorials/best-document-parsing-apis/?utm_source=draftdev&utm_medium=newsletter&utm_campaign=javascriptweekly_20261117)

本文聚焦 2026 年 8 款最佳 Unstructured.io 文档解析替代方案，说明从原型走向生产时，往往需要更换解析器、分块器、连接器，或三者全部替换，并给出选型与迁移前的评估要点。

- 📄 文章主题：2026 年 8 款最佳 Unstructured.io 文档解析替代方案。
- 🔁 生产化常见需求：替换解析器、分块器、连接器，或三者全部更换。
- 🧩 对比工具包括 Foxit PDF Services API、LlamaParse、Reducto、Docling 等 8 款方案。
- 📊 核心评估维度：成本、表格处理、分块能力、文件格式覆盖。
- 🧭 迁移准备：提供元素映射、计费测算和测试计划，帮助切换前完成评估。

---

### [Expo Simulators: Simulators built for agents](https://expo.dev/services/simulators?utm_campaign=agentic-development&utm_source=email&utm_medium=email&utm_term=Simulators&utm_content=JavaScript%20Weekly)

**原文标题**: [Expo Simulators: Simulators built for agents](https://expo.dev/services/simulators?utm_campaign=agentic-development&utm_source=email&utm_medium=email&utm_term=Simulators&utm_content=JavaScript%20Weekly)

Expo Simulators 是面向 AI 编码代理的按需云模拟器服务，可启动安全的 iOS 模拟器与 Android 模拟器，让代理安装构建、操作应用并自行验证；同时生成截图、录屏和构建链接，供团队在 PR 或浏览器中审阅。

- ☁️ 按需启动云端 iOS 模拟器和 Android 模拟器，支持多个会话并行运行，并按账户并发额度排队扩展。
- 🤖 代理可安装构建、点击浏览主要页面、执行验证并收集截图/录屏等证据，形成“写代码—验证—修复”的闭环。
- ✅ 每次 PR 可附带检查截图、会话录屏和构建链接，审查者可查看证据并直接体验实时构建。
- 🔒 会话运行在隔离环境中，支持访问控制、会话级凭证和受控预览链接，停止后模拟器与控制器端点不可用。
- 🧰 兼容 Claude Code、Codex、Cursor、Grok、Appium、Maestro 等工具，也支持 React Native、Flutter、Swift、Kotlin、Unity 等应用构建。
- 🚀 可通过 EAS CLI 或 REST API 从 GitHub Actions、Expo Workflows 等 CI 启动会话，运行检查和收集结果。
- 🧪 可接入现有 Appium 测试套件，或通过 agent-device 运行部分 Maestro YAML 流程。
- 👀 支持共享实时模拟器会话，让团队在浏览器中审阅运行中的应用，无需本地开发环境。
- 🔁 对 Expo/React Native 应用，Expo Workflows 可用指纹匹配已有原生构建并重打包最新 JavaScript，减少每次变更的完整原生重建；开发时可配合 Metro/Fast Refresh。
- 🛠️ 快速开始需参考 EAS Simulator 文档，安装 Expo Skills 并使用 eas-simulator 技能，先运行 `eas simulator:availability --json` 检查权限，再用如 `eas simulator --platform ios` 启动会话。

---

### [GitHub - Agent-Field/CodeAF：面向开放模型的开源软件工厂 · GitHub](https://github.com/Agent-Field/CodeAF)

**原文标题**: [GitHub - Agent-Field/CodeAF: Open-Source Software factory for Open Models · GitHub](https://github.com/Agent-Field/CodeAF)

CodeAF 是 AgentField AI 推出的开源“软件工厂”式编码工具，面向开放模型，以单一 Go 二进制提供多项目控制台、任务编排、专业子代理、自动化与无头执行，主打低成本、高性能和本地优先。

- 🏭 **产品定位**：为开放模型打造的编码 harness，目标是用更低成本获得前沿级编码能力，并统一管理多个项目与代理任务。
- 🥇 **基准表现**：在 DeepSWE 的 113 个真实 GitHub issue 上，使用同一模型对比十种编码 harness，解决数量最多且单 issue 成本最低，领先 Claude Code、Codex、OpenCode 等。
- 🖥️ **单窗口工作台**：一个窗口列出机器上所有项目与对话，支持标签切换、会话跳转、后台持续运行，并分别管理审批规则、模型与花费上限。
- 🗣️ **对话转任务**：用自然语言描述问题，可自动拆分为多个任务，在独立仓库副本和分支上运行；通过检查的改动自动进入你的分支，不直接进入 main/dev/发布分支。
- 🏗️ **“工厂”式编排**：自动评估、拆分、并行执行、测试并合并工作，仅在必须时询问；问题集中到“需要你”区域，其余事项自行决策并记录。
- 🧩 **内置子代理**：senior-dev 负责代码修改与测试，sec 做本地安全审计，review 审查 GitHub PR；结果返回聊天，并支持 Markdown/JSON/SARIF 报告。
- 🤖 **多模型分工**：每个任务由 worker、planner、checker 等席位组成，按任务类型自动选模型；支持固定席位模型、限制为开放权重模型、按任务选择更贵或更便宜方案。
- ⏰ **自动化能力**：通过自然语言设置提醒、定时任务与监控，如每周草稿、CI 变红通知；错过的任务会在下次启动时补跑。
- 🚪 **无头模式**：`codeaf do` 可接收完整任务说明，自动规划、执行、检查并输出 JSON 与退出码，适合 CI、cron、脚本和基准测试。
- 🌐 **远程开发架构**：界面在本机运行，对话与任务在远程开发机运行；支持 SSH、断线重连、文件双向传输、手机终端接入，输入不依赖网络往返。
- ⚡ **性能与体积**：单二进制约 53 MB，显著小于竞品；内存占用、会话恢复速度等指标也大幅优于 Claude 等工具。
- 🔐 **遥测与许可**：默认发送匿名使用计数，不包含提示词、代码、路径、仓库名、密钥或 IP；可通过设置或环境变量关闭。项目采用 Apache-2.0 许可，目前为早期预览。

---

### [GitHub - camsong/You-Dont-Need-jQuery：用纯 JavaScript 实现类似 jQuery 的查询、样式、DOM、Ajax、](https://github.com/camsong/You-Dont-Need-jQuery)

**原文标题**: [GitHub - camsong/You-Dont-Need-jQuery: Examples of how to do query, style, dom, ajax, event etc like jQuery with plain javascript. · GitHub](https://github.com/camsong/You-Dont-Need-jQuery)

该仓库是一个“你可能不需要 jQuery”的原生 JavaScript 替代方案合集，系统整理查询、样式、DOM、Ajax、事件、工具函数、Promise 与动画等常见 jQuery 用法的现代浏览器实现，并提醒迁移前需按场景测试。

- 📌 仓库汇集用原生 JS 实现 jQuery 常见功能的示例，覆盖选择器、CSS/样式、DOM 操作、Ajax、事件、工具函数、Promise 和动画。
- 🌐 示例面向当前主流常青浏览器（Chrome、Edge、Firefox、Safari），已移除 IE 专用兼容方案。
- 🧩 常用替代包括 `querySelector(All)`、`classList`、`fetch`、`addEventListener`、`Promise`/`async await` 和 Web Animations API。
- ⚠️ jQuery 仍是有价值的库，并非所有替代方案在所有场景完全等价，使用前建议测试。
- 📈 仓库热度较高：约 20.1k stars、1.7k forks，采用 MIT 许可证，并提供多语言 README。
- 🧪 部分片段使用较新 API（如 `Promise.withResolvers()`、`replaceChildren()`、`AbortSignal.timeout()`），需结合 Baseline 检查浏览器支持。
- 🔗 参考资源包括 MDN Web Docs、Baseline 和 You Might Not Need jQuery。

---

### [发布 Release 3.0 · camsong](https://github.com/camsong/You-Dont-Need-jQuery/releases/tag/v3.0)

**原文标题**: [Release Release 3.0 · camsong/You-Dont-Need-jQuery · GitHub](https://github.com/camsong/You-Dont-Need-jQuery/releases/tag/v3.0)

概述：You-Dont-Need-jQuery v3.0 已发布，全面面向现代常青浏览器，所有改动片段均通过针对 jQuery 4 的测试，并正式放弃 Internet Explorer 支持。

- 🚀 v3.0 发布：指南目标改为最新 Chrome、Edge、Firefox、Safari 和 Opera，不再包含 IE 专用兼容回退。
- 🌐 破坏性变更：不再支持 IE；如需 IE，请使用最后兼容版本或 v2.0。
- 🧩 原生一行替代：如 `el.remove()/before()/after()`、`replaceChildren()`、`replaceWith()`、`<template>`、`structuredClone()`、`Promise.withResolvers()`、`scrollY`、`offsetHeight/Width` 等。
- 🆕 新增章节：JSON 请求与 `response.ok` 注意事项、POST JSON、Abort 与超时、`{ once: true }`、事件委托、用 `AbortController` 批量移除监听、`async/await` 版 `always/then`。
- 🎞️ 效果实现更新：使用 Web Animations API（`el.animate()`）；`slideUp/slideDown` 测量真实高度。
- 🛠️ 修复片段：包括 `nextAll/prevAll`、`:contains`、HTML 字符串 `append/prepend`、深拷贝 `clone`、`trigger`、`inArray`、`isPlainObject(null)`、`merge`、`globalEval`、`parseHTML`、`Deferred`、`fadeOut/fadeTo/animate` 等，并修复 README 的 Markdown、锚点和语法错误。
- 🧪 测试与工具：用 Vitest + jsdom 替换 Karma/webpack 1/Babel 6；通过 GitHub Actions 在 PR 和 `master` 上运行测试，移除 Travis CI 配置与徽章。
- 🌍 翻译同步：全部 15 种翻译均已与当前片段同步；完整变更见 `v2.0...v3.0`。

---

### [PropFLIP · 2026年11月10日](https://nerdy.dev/prop-flip)

**原文标题**: [PropFLIP Â· November 10, 2026](https://nerdy.dev/prop-flip)

文章介绍了一种名为 PropFLIP 的布局动画技巧：它沿用 FLIP 思路，用 4 个可通过 `@property` 注册的自定义属性构造 `transform`，再借助 CSS `transition` 实现可中断的布局动画，并讨论了缩放导致的圆角/文字挤压问题、JS 实现流程与性能边界。

- 🧩 核心思路：布局先到达 Last 状态，再用 4 个 typed props 在 `transform` 中表示位移与缩放，让 CSS 过渡完成动画。
- 📐 4 个属性：`--tx`、`--ty` 默认 0，`--sx`、`--sy` 默认 1；注册为 `<number>`；`transform-origin: top left` 可简化 `getBoundingClientRect()` 的数学计算。
- ⏱️ 过渡优势：每个属性可独立设置 duration、easing、delay，可做出弧线与摆动效果；CSS transition 天然支持可中断动画。
- 🟦 圆角修复：用 `border-radius: calc(var(--r)/var(--sx)) / calc(var(--r)/var(--sy))` 抵消缩放造成的圆角变形。
- 🔤 子元素修复：直接子元素通过反缩放和基于 padding 的位移抵消父级缩放；`--sx`、`--sy` 继承可让后代跟随。
- 🧪 JS FLIP 流程：测量 First → 关闭 transition → 修改 DOM → 测量 Last → 设置反向位移/缩放比例 → 用 `offsetHeight` 强制 reflow → 恢复 transition → 将属性设回 0/1。
- ⚡ 性能限制：布局只计算一次，但每帧仍有 style recalc；4 个自定义属性变化会触发 transform 重算，继承还会使后代失效；注册属性动画目前通常仍在主线程。
- 🎯 适用场景：少量元素如卡片、对话框、短列表效果很好；数百元素或主线程繁忙时，应考虑用 `element.animate()` 对 `transform` 做绝对值动画。
- 🔮 作者期望：希望 typed custom properties 能脱离主线程动画，由合成器处理仅用于 `transform` 的数值动画；PropFLIP 是一种减少 JS 的权衡。
- 💬 社区反馈：圆角修复很实用，可中断动画是亮点；也有人讨论图标/内部元素防挤压、打断时是否会出现一帧挤压等细节。

---

### [错误](https://css-tricks.com/animating-layouts-with-the-flip-technique/)

**原文标题**: [Error](https://css-tricks.com/animating-layouts-with-the-flip-technique/)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='css-tricks.com', port=443): Max retries exceeded with url: /animating-layouts-with-the-flip-technique/ (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [GitHub - aws/aws-emulator：AWS Emulator 是 AWS API 的本地模拟器。 · GitHub](https://github.com/aws/aws-emulator)

**原文标题**: [GitHub - aws/aws-emulator: AWS Emulator is a local emulator of the AWS APIs. · GitHub](https://github.com/aws/aws-emulator)

AWS Emulator 是一个在本地模拟 AWS API 的开源工具，适合在开发机、测试服务器或 CI 中测试软件，无需 AWS 账号，也不会调用真实 AWS，因此不会产生额外服务费；它仅用于构建和测试，不建议用于生产或安全测试。

- 🧪 本地运行 AWS API 模拟器，请求发往模拟器而不是 AWS，使用模拟资源进行测试
- 💰 无额外服务费；部署到 AWS 时仍需为真实 AWS 资源付费
- 🖥️ 提供本地进程模式：启动后通过环境变量将 AWS CLI 或 SDK 指向模拟器端点
- 🧩 支持嵌入式模式：作为开发依赖在测试进程内运行，每个测试可隔离实例，无需端点 URL、证书或环境变量
- 🤖 可通过 AI 编码代理快速安装 `aws-emulator` skill，要求 AWS CLI 2.35.0 及以上
- 🐧 从源码构建支持 Linux x86_64 和 aarch64；Windows/macOS 建议使用 Docker
- 🛠️ 源码构建需要 Rust/Cargo、C 编译器、至少 100GB 磁盘空间和多核机器；首次全量构建较慢
- 🚀 构建并运行 `aws-emulator-router` 后，默认在 `127.0.0.1:9297` 提供 HTTPS 服务，使用自签名证书
- 📁 仓库按服务组织：每个 AWS 服务一个 crate，核心包含 router 和 embedded，`issues/` 跟踪功能缺口与已修复项
- 📊 Telemetry 默认开启，强调数据最小化，不记录请求/响应内容、代码、凭证或个人数据，也不与第三方共享
- 🔕 可通过 `--telemetry off`、`EMULATOR_TELEMETRY=off`、`config.toml` 或嵌入式配置 API 关闭遥测
- ⭐ 仓库约有 9.1k stars、404 forks、23 watchers；不接受 pull request，由 AI agents 定期保持与 AWS 同步更新
- 📜 许可证为 CC0-1.0，但 `vendor/` 目录代码使用 Apache License 2.0
- ⚠️ 官方提供各服务与 AWS 的保真度评分、已知问题目录及项目兼容性检查指引

---

### [AWS 模拟器：一个 100% 由自主 AI 智能体构建的本地模拟器](https://www.aboutamazon.com/news/aws/how-autonomous-ai-agents-built-aws-emulator)

**原文标题**: [AWS Emulator: a local emulator built 100% by autonomous AI agents](https://www.aboutamazon.com/news/aws/how-autonomous-ai-agents-built-aws-emulator)

AWS Emulator 是一个可在本地运行的 AWS 服务模拟器，代码完全由自主 AI 代理编写，团队未编写或审查代码；它通过测试、发现问题、修复问题三组代理协作，并依靠合并门禁等护栏保证质量，已在 GitHub 以 CC0 协议开源并持续更新。

- 🧪 AWS Emulator 可在本机运行，用于构建和测试 AWS 应用。
- 🤖 代码 100% 由自主 AI 代理完成，团队未编写或审查任何代码。
- 💡 项目源于周末实验：受 Anthropic 智能体自主构建 C 编译器启发，Kiro 先用 15 分钟做出可用的 Amazon SQS 初版，周末扩展到更多 AWS 服务。
- 🛡️ 产品化关键在护栏：以 AWS API Models 为规范、真实 AWS 为参考实现，让代理在明确边界内工作。
- 🧑‍💻 三组代理分工：测试组编写并验证真实场景保真测试；问题组重放测试、定位并归组失败；修复组逐项修复。
- ✅ 修复需通过合并门禁：编译、编码规范、安全审查、保真度不回归等检查，失败则返工；数百代理可并发工作，每天修复数千问题。
- 🚀 发布流程基于 AWS Developer Tools/CodeCommit，打包二进制，最后将代码发布到 GitHub。
- 📂 GitHub 仓库公开所有问题：已修复在 “issues/things-that-now-work”，待修复在 “issues/things-that-do-not-work”；源码和保真测试均公开。
- 📝 后续系列将深入多代理工作流架构、保真度衡量、质量与安全标准。

---

### [Svelte • Web development for the rest of us](https://svelte.dev/)

**原文标题**: [Svelte • Web development for the rest of us](https://svelte.dev/)

Svelte 是一个通过编译器实现简洁 UI 组件的 Web 开发框架，强调使用熟悉的 HTML、CSS 和 JavaScript，让浏览器端只做最少的工作。它受到开发者喜爱，被众多公司采用，并拥有活跃社区与长期维护支持。

- 🧩 Svelte 是 UI 框架，利用编译器编写极其简洁的组件。
- 🌐 组件使用 HTML、CSS 和 JavaScript，浏览器端运行负担最小。
- ❤️ 开发者持续将 Svelte 评为最令他们兴奋使用的框架之一。
- 🏢 被许多知名公司采用。
- 🎥 可观看完整的 Svelte Origins 纪录片。
- 🌍 姐妹组织 Svelte Society 在全球举办活动，可通过 Discord 加入友好社区。
- 🤝 由 Vercel、众多捐赠者以及全职和兼职维护者支持，项目持续发展。
- 📜 Svelte 是免费开源软件，采用 MIT 许可证，版权标注至 2026 年 Svelte 贡献者。

---

### [初始提交 · sveltejs/svelte@fc7e6e6 · GitHub](https://github.com/sveltejs/svelte/commit/fc7e6e6827c3e9f2a29ec1c6ec957bab9f195841)

**原文标题**: [initial commit · sveltejs/svelte@fc7e6e6 · GitHub](https://github.com/sveltejs/svelte/commit/fc7e6e6827c3e9f2a29ec1c6ec957bab9f195841)

这是 Svelte 仓库的初始提交（fc7e6e6），由 Rich-Harris 创建，共变更 7 个文件、新增 206 行，奠定了编译器、解析器、测试与项目配置的基础结构。

- 🧱 该提交是项目初始版本，包含编译器入口、模板解析器、测试文件及项目配置文件。
- 📦 package.json 将项目命名为 svelte，版本为 1.0.0，描述为“The frameworkless UI framework”，主入口为 dist/svelte-compiler.js，采用 MIT 许可证。
- 🔍 compiler/parse/index.js 实现模板解析器，将模板解析为 Fragment、Element、Text 等 AST 节点，并包含标签、文本、Mustache 与属性解析的初步逻辑。
- 🧪 compiler/parse/__test__.js 添加解析器测试，验证 parse 是函数，并能解析单个 `<span>test</span>` 元素。
- 🔌 compiler/index.js 导出 parse 与 generate，形成编译器模块的基础入口。
- ⚙️ package.json 配置 mocha 测试脚本；mocha.opts 指定 `--require reify`；开发依赖包括 mocha 和 reify，运行时依赖为 locate-character。
- 🙈 .gitignore 忽略 `.DS_Store` 与 `node_modules`。
- 📝 提交还包含 compiler/generate/index.js，但显示为空白字符变更。

---

