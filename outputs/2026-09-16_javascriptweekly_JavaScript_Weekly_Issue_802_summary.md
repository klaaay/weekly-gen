### [](https://hemanth.github.io/functional-programming-jargon/)

**原文标题**: [FP Jargon — Interactive Functional Programming Knowledge Graph](https://hemanth.github.io/functional-programming-jargon/)

未提供可供总结的内容，请补充文本后再生成摘要。
- 📭 当前消息中“Use the following content:”后为空，无法提取要点。
- ✍️ 请粘贴或发送需要总结的文章、段落或材料。
- ✅ 收到内容后，我会按“概述 + 表情符号项目符号”的中文格式输出。

---

### [](https://github.com/hemanth/functional-programming-jargon)

**原文标题**: [GitHub - hemanth/functional-programming-jargon: Jargon from the functional programming world in simple terms! · GitHub](https://github.com/hemanth/functional-programming-jargon)

这是一个面向函数式编程学习者的 GitHub 术语表项目，由 hemanth 维护，采用 MIT 许可证，旨在用通俗解释和 JavaScript ES2015 示例降低函数式编程概念的学习门槛。仓库约 18.7k stars、997 forks，并遵循 Fantasy Land 规范，还提供交互图、LLM/Agent 规范和多种语言翻译。

- 📚 项目定位：整理函数式编程世界的术语与行话，帮助开发者更容易理解 FP。
- 💻 示例语言：主要使用 JavaScript ES2015，并在适用处引用 Fantasy Land 规范。
- 🌐 扩展资源：提供交互式图谱、LLM/Agent 规范，以及葡萄牙语、中文、韩语、法语等多语言翻译。
- 🧠 基础概念：涵盖 Arity、高阶函数、闭包、偏应用、柯里化、自动柯里化、函数组合、续延、IO、Trampoline、Thunk 和代数效应。
- ✅ 函数原则：解释纯函数、副作用、幂等性、无点风格、谓词和契约。
- 🧱 范畴论相关：包括 Category、Semigroupoid、函子、Pointed Functor、Lift、引用透明和等式推理。
- ⚡ 优化与抽象：涉及 Memoization、Lambda、Lambda 演算、函数组合子和惰性求值。
- 📦 代数结构：介绍 Monoid、Monad、Comonad、Kleisli 组合、Free Monad 和 Monad Transformer。
- 🧩 高级函子：包括 Applicative Functor、Bifunctor、Contravariant Functor、Profunctor 和 Alternative。
- 🔁 态射体系：讲解同态、自同态、同构、Catamorphism、Anamorphism、Hylomorphism、Paramorphism、Apomorphism 和自然变换。
- 🧷 比较与折叠：涉及 Setoid、Semigroup、Foldable 和 Traversable。
- 🔍 光学结构：介绍 Lens、Prism、Iso 和 Traversal，用于不可变数据访问与变换。
- ✍️ 类型系统：包含类型签名、代数数据类型、和类型、积类型、Option 和 Either。
- ⚠️ 函数完整性：区分全函数与偏函数，并说明如何用默认值、守卫或 Option 处理偏函数。
- 🛠️ 常用库：列出 Ramda、Folktale、monet.js、lodash、fp-ts、Sanctuary、Crocks、Fluture 等 JavaScript 函数式编程库。
- 👥 社区状态：仓库约有 305 次提交、24 个 issue、3 个 PR，依赖贡献者共同完善。

---

### [](https://master.dev/sale/?utm_source=javascriptweekly&utm_medium=newsletter&utm_campaign=buildersale)

**原文标题**: [Build Better With AI Sale | Master.dev](https://master.dev/sale/?utm_source=javascriptweekly&utm_medium=newsletter&utm_campaign=buildersale)

秋季促销：立减 100 美元，帮助你掌握基础并用 AI 构建得更好，限时优惠即将结束，可立即领取折扣。
- 💰 秋季促销立减 100 美元
- 🧠 掌握基础，借助 AI 构建更佳
- ⏳ 促销以倒计时天数计算，即将结束
- 🛒 立即获取折扣 →

---

### [](https://philipwalton.com/articles/modern-web-types/)

**原文标题**: [Modern Web Types â Philip Walton](https://philipwalton.com/articles/modern-web-types/)

现代 Web 类型缺失长期困扰 TypeScript 用户：官方 DOM/WebWorker 库因双引擎支持政策，不包含许多已在单一现代浏览器中可用、可作渐进增强的新 API 类型。作者因此创建 `modern-web-types`，用同一套上游生成器但把阈值降为一个浏览器引擎，为使用新 Web 功能的项目提供更完整、可自动更新的类型定义。

- 😤 常见痛点：使用 `startViewTransition`、长动画帧 API 的 `scripts`、`fetchLater()` 等新 API 时，TypeScript 会报“属性不存在”。
- 🧭 原因：TypeScript 的 Web API 类型生成器只纳入至少两个浏览器引擎支持的 API，导致许多现代 API 缺失官方类型。
- 🧩 方案：`modern-web-types` 是官方“DOM”和“WebWorker”库的替代品，基于 TypeScript 自己的生成器，但支持阈值降为一个浏览器引擎。
- 📦 安装：推荐执行 `npm install --save-dev @typescript/lib-dom@npm:modern-web-types`；TypeScript 6+ 还需在 `tsconfig.json` 中设置 `"libReplacement": true`。
- 📊 类型增量：新增 DOM/WebWorker 接口 433/144 个、类型别名 96/35 个、全局 223/56 个，并为已有接口新增成员 311/64 个。
- 🔧 维护自动化：使用 `TypeScript-DOM-lib-generator` 和 `w3c/webref` 数据源，GitHub Actions 每周生成并对比，有变化就开 PR，批准后发布新版本。
- ⚖️ 质疑双引擎规则：缺少官方类型不会阻止站点使用新 API，反而常导致 `@ts-ignore`、`any` 或不完整/错误类型；支持引擎数量也不能判断 API 是否适合某站点。
- 🚀 单引擎 API 的价值：`LargestContentfulPaint`、`PerformanceEventTiming`、`LayoutShift`、`fetchpriority`、Speculation Rules 等最初仅 Chrome 可用，却已在数百万站点用于改善 Core Web Vitals。
- ✅ 使用建议：没遇到缺失类型就不一定需要；若经常遇到，使用该库比手写类型更省力、更不易冲突，并能跟随上游更新。
- 🤔 未来展望：如果采用者足够多，TypeScript 可能放宽双引擎政策，届时该库或许不再必要。

---

### [GitHub - philipwalton/modern-web-types：适用于尚未加入 lib.dom 的新 Web 平台 API 的 TypeScript](https://github.com/philipwalton/modern-web-types)

**原文标题**: [GitHub - philipwalton/modern-web-types: TypeScript types for new web platform APIs that aren't yet in lib.dom. · GitHub](https://github.com/philipwalton/modern-web-types)

本仓库 `philipwalton/modern-web-types` 旨在为已在至少一个稳定浏览器中可用、但尚未进入 TypeScript 官方内置类型定义的 Web 平台 API 提供 TypeScript 类型；它复用 TypeScript 官方生成管线，输出完整 lib，可作为官方 DOM/Worker 类型的替代或补充。

- 📦 项目提供 `modern-web-types`，包含五个环境 lib：DOM、WebWorker、ServiceWorker、SharedWorker、AudioWorklet。
- 🧩 类型由与 TypeScript 官方相同的生成器生成，质量与正确性一致，区别只在于收录 API 的数量。
- 🎯 TypeScript 官方 `lib.dom.d.ts` 等只收录已在两个及以上浏览器引擎发布的特性，因此单引擎已可用且广泛使用的 API 会缺少官方类型。
- ⚙️ 推荐安装方式：`npm install --save-dev @typescript/lib-dom@npm:modern-web-types`，用别名替换 TypeScript 解析的 DOM 库。
- 🧷 TypeScript 6+ 需在 `tsconfig.json` 中启用 `libReplacement: true`；TypeScript 4.5–5.x 默认支持库替换。
- 👷 对 Worker 等环境，需从 `lib` 移除对应库，并在 `types` 中引用入口，如 `modern-web-types/webworker`。
- 📚 入口映射包括：`modern-web-types` / `modern-web-types/dom` 替代 DOM；`webworker` 替代 WebWorker；`serviceworker`、`sharedworker`、`audioworklet` 对应相应 @types 包。
- ⚠️ 若项目原本未设置 `types`，添加后 TypeScript 将只包含列出的 @types 包，不再自动包含 `node_modules` 中所有 `@types/*`。
- 🔄 更新机制：每周一 workflow 重新固定生成器和条目注册表到最新提交，重新生成全部五个 lib、运行测试，并自动开 PR。
- 🛠️ 生成流程：固定并补丁生成器，使引擎阈值可配置；用同一数据快照构建两次，分别为两引擎 baseline 和一引擎 full；再用 TypeScript 编译器 API 做结构化 diff；最后按环境生成完整 lib。
- 📝 `report.md` 列出官方类型与一引擎类型之间的差距，冒烟测试由当前 delta 自动生成；API 一旦升级到两引擎，就会移出 delta 和测试。
- 🧪 开发命令：`npm run update` 执行 fetch-upstream → fetch-registry → build → diff → emit-lib → emit-test → emit-readme → report；`npm test` 对每个生成 lib 做类型检查并限制增量大小。
- 🧰 同时安装 TypeScript 6 与 7：diff/emit 脚本用 TS 6，因为 TS 7 将编译器 API 移到 `typescript/unstable/*`；测试则在两个版本下检查生成输出。
- 🚀 发布由 `pkg/package.json` 的 `version` 驱动：合并到 `main` 且版本变化会触发 publish workflow，发布 `pkg/` 到 npm 并打 tag；版本不变则不发布。
- 🧾 相关项目：`lib.dom.d.ts` / `@types/web` 是官方类型；`@types/dom-*` 是手写单特性补丁，本项目用生成的完整 lib 覆盖同类空白。
- 📜 许可证为 Apache-2.0，生成输出源自 `TypeScript-DOM-lib-generator` 和 `webref` 的 Web IDL。

---

### [](https://react.dev/blog/2026/09/09/react-19-3)

**原文标题**: [React 19.3 – React](https://react.dev/blog/2026/09/09/react-19-3)

React 19.3 已在 npm 发布，核心亮点是 View Transitions 与 Fragment Refs 转为稳定 API，同时带来 browser()、Trusted Types 支持，以及 Server Components 可直接渲染 Context 等改进。  
- 🚀 React 19.3 于 2026 年 9 月 9 日由 React 团队发布，并已上线 npm。  
- 🎞️ `<ViewTransition>` 稳定，可使用浏览器 View Transition API 为进入、退出、更新、共享元素添加动画，且仅由 Transition 更新触发。  
- 🧩 新增 `addTransitionType`，可区分同一状态更新的不同原因，例如轮播“前进”与“后退”，并匹配不同动画。  
- ⏳ View Transitions 可与 Suspense 集成，让 fallback 到最终内容的切换更顺滑，也可让图片、字体等资源参与 Suspense 加载。  
- 🖼️ Suspense 动画最佳实践：fallback 应立即无动画显示，fallback 到最终内容应有动画，不挂起的子项应立即无动画显示。  
- 📌 Fragment Refs 稳定：可将 ref 传给 `<Fragment>` 获得 `FragmentInstance`，对一组子 DOM 执行事件、焦点、观察器、测量与滚动等操作。  
- 🧭 `browser()` 新 API：组件可用 `use(browser())` 退出服务端渲染，服务端触发 Suspense，客户端不触发，适合时区、`localStorage` 等浏览器专属逻辑。  
- 🔐 React 19.3 集成 Trusted Types API，不再强制将值转为字符串，支持 `TrustedHTML`、`TrustedScript`、`TrustedScriptURL`，增强防 XSS 能力。  
- 🖥️ Server Components 可直接从 `'use client'` 模块导入并渲染 `<Context>`，不再必须额外导出 Provider 包装组件。  
- 🔄 其他更新包括：Render Transitions 独立执行、Strict Mode hydration 双调用 Effects、新增全屏事件、`maskType`、`fetchPriority`、`submitter`、`credentialless` 等支持。  
- 🐛 重要修复涵盖 `useDeferredValue` 卡旧值、Suspense fallback 的 Context 传递、`useSyncExternalStore` 在 `<Activity>` 隐藏时漏更新、`<ViewTransition>` 在 Mobile Safari 与 SuspenseList 中的崩溃等。  
- 📚 完整变更列表可查阅官方 Changelog。

---

### [](https://react.statuscode.com/issues/490)

**原文标题**: [Issue #490: Why Shopify is moving off React Native — React Status](https://react.statuscode.com/issues/490)

本期 React Status #490 聚焦 React 19.3 正式发布，带来 Fragment Refs、View Transitions 等实验性 API 转正与 Server Components 增强；同时涵盖 Shopify 转向原生移动开发、Tailwind 加入 Shopify、React DevTools 8.0、Jotai 3.0、Rust 版 React Compiler 性能提升及多篇迁移与工具文章。

- ⚛️ React 19.3 发布：两个实验性 API 转正，并加入 Server Components 相关增强。
- 🧩 Fragment Refs：无需额外包裹元素即可跨一组 DOM 节点管理焦点、事件和测量，避免破坏布局。
- 🎞️ View Transitions：`<ViewTransition>` 让元素进入、离开或变化时有动画，支持 Suspense 展示与 CSS 自定义。
- 🔐 Trusted Types：向 `innerHTML` 等 DOM API 传值时保留 trusted 对象，避免字符串转换被浏览器拒绝。
- 🖥️ `use(browser())`：组件可仅在浏览器渲染，服务端 HTML 中显示最近的 Suspense fallback。
- 🧱 其他 React 19.3 变化：`<Activity>` 支持 Server Components，适配新 `<select>` 解析规则，transition 可独立渲染。
- 🛍️ Shopify 在投入 React Native 六年后，改用 Swift/Kotlin 重建应用，认为编码智能体降低了双端开发成本；React Native Skia、FlashList、Restyle 去向受关注。
- 🤔 Expo 创始人等质疑该决定更像政治选择而非技术选择，称比较的是旧架构应用与全新重写。
- 🎨 Tailwind Labs 加入 Shopify，开源项目仍保持 MIT 许可和原团队。
- 🛠️ React DevTools 8.0 发布：默认开启 Suspense 标签，移除 Timeline profiler，由浏览器 Performance 面板接管；另有面向编码智能体的实验包。
- ⚡ 1000+ 文件 React Router 应用迁移到 oxc 的 Rust 版 React Compiler，编译从 14.3s 降至 0.81s，并支持 Babel 版跳过的模式。
- 📱 Discord 迁移到 React Native 新架构：仅 14% 工单涉及迁移本身，其余为长尾问题。
- 🤖 Next.js 团队一个月关闭 1500 个 GitHub issue，过程中使用智能体。
- 🌐 文章解释 Chrome 翻译会让 React 应用卸载并触发 `removeChild` 错误，常规 monkey-patch 可能隐藏崩溃但 UI 仍损坏。
- 🚀 Gatsby 迁到 Astro 的案例：9¾ 天内完成，保留 React 组件，但需大量准备。
- 🧪 Jotai 3.0：仅 ESM，要求 React 18/TypeScript 5.5+；`atomFamily` 移至 `jotai-family`，`loadable` 改为 `unwrap`。
- 📦 React Native ExecuTorch 0.10：重写设备端 AI 库，用可检查的 TypeScript 管线取代不透明原生模块，支持 Core ML、MLX、Vulkan。
- 🧬 Vidact：把 React 函数组件和 hooks 编译为直接 DOM 操作，无 VDOM/React 运行时；Beta，不支持的模式会在构建时报错。
- 🗺️ 工具更新：React Google Maps 1.10 增加声明式 3D 组件；Lexical 0.50 支持 HMR；Base UI 1.8 成为 shadcn/ui 默认；wouter 3.11 约 2KB；React Native 0.88 RC。

---

### [](https://www.f5.com/labs/articles/cloud-takeover-mass-scanning-for-exposed-vite-endpoints-cve-2026-39364)

**原文标题**: [Cloud Takeover: Mass Scanning for Exposed Vite Endpoints (CVE-2026-39364) | F5 Labs](https://www.f5.com/labs/articles/cloud-takeover-mass-scanning-for-exposed-vite-endpoints-cve-2026-39364)

2026 年 8 月，F5 Labs 传感器记录到大规模自动化扫描，攻击者集中利用暴露在互联网上的 Vite 开发服务器，通过 CVE-2026-39364 等漏洞读取敏感文件并窃取云凭据与基础设施状态。活动从前期约 1,732 起事件激增至当月超 32,000 起，目标包括 .env、AWS/Azure 凭据、Terraform 状态和 /proc 环境文件。报告还汇总了当月 Top 10 CVE、长期趋势、攻击类型、来源国、目标地，并给出补丁、网络隔离、WAF、反向 DNS 验证和密钥轮换建议。

- 🛡️ CVE-2026-39364 是 Vite 开发服务器未认证文件读取/访问控制绕过漏洞，CVSS 7.5，CWE-200，影响 Vite 7.1.0 至 7.3.2 之前及 8.0.5 之前版本。
- 🔓 攻击者通过 `?raw`、`?import&raw`、`?import&url&inline` 等查询参数绕过 `server.fs.deny`，获取 .env、证书、源码等受限文件并返回 HTTP 200。
- 🧩 相关 Vite 漏洞包括 CVE-2025-30208、CVE-2025-31125、CVE-2024-45811，均利用 `@fs` 路径与查询字符串绕过；其中 CVE-2025-31125 已被列入 CISA KEV。
- 🌐 默认 Vite 绑定 localhost，但使用 `--host`、`server.host` 或错误 Docker 端口映射后，开发服务器可被局域网/公网直接访问。
- ⚙️ 攻击链为：未认证 GET `/@fs/` 请求敏感路径并附加绕过参数；服务器路径规范化/查询解析未触发 deny 检查；明文返回文件。
- 📊 8 月观测：信息泄露 32,010 起、可预测资源位置 1,729 起、路径遍历 1,586 起；出现双编码 `%252f` 以绕过代理/WAF。
- 📂 目标文件涵盖 .env 各环境、各用户目录下 `.aws/credentials`、AWS 配置/备份、`terraform.tfstate`/`tfvars`、Azure 凭据、`/etc/passwd`、`/proc/self/environ`、`/proc/self/cwd/.env`。
- 🤖 请求使用 HTTP/1.0 和 `Connection: close`，伪造 Googlebot、ClaudeBot、GPTBot、PerplexityBot、OAI-SearchBot、Amazonbot 等 User-Agent，并伪造 `X-Forwarded-For`/`X-Real-IP`。
- ☁️ 威胁评估认为这是租用云基础设施上的自动化凭据收集活动，IP 多集中在 Google Cloud 34.x/35.x；美国 17,297 起、比利时 4,407、荷兰 4,011、新加坡 2,842、台湾 1,994、日本 1,353。
- 🎯 同一扫描集群还以 103 起事件探测 CVE-2025-29927（Next.js 中间件绕过），显示多框架探测能力。
- 🧭 MITRE ATT&CK 映射：侦察 T1595.002、初始访问 T1190、凭据访问 T1552.001、收集 T1005、发现 T1083。
- 📈 8 月 Top CVE：CVE-2017-9841 以 4,201 起居首；CVE-2018-14028 激增 3,258 起至 4,102 起升至第二；CVE-2024-4577 增 2,612 起至 3,023 起升至第四。
- 🆕 新进 Top 10：CVE-2021-34523（Exchange 提权，1,853 起）、CVE-2024-44000（LiteSpeed Cache 凭据暴露，1,079 起）、CVE-2016-4800（Jetty 路径规范化绕过，1,078 起）。
- 📉 CVE-2022-41040 与 CVE-2021-34473 本月跌出榜且无利用活动，但 Exchange 仍被 CVE-2021-26855、CVE-2022-41082、CVE-2021-34523 持续攻击。
- ⏳ 长期趋势：CVE-2017-9841 从 2025 年 11 月峰值 27,075 降至 4,201；CVE-2018-20062 降至 3,482；CVE-2018-14028 达 2026 年 2 月以来最高；CVE-2024-4577 从 7 月 411 回升至 3,023。
- 🔬 攻击类型：可预测资源位置 945,081 起（+153%）、信息泄露 620,931 起（+148%）、命令执行 234,256 起（+47%）、服务端代码注入 249,433 起（+32%）；木马/后门/间谍软件近 +700% 至 51,537，漏洞扫描 +184% 至 8,711。
- 🌍 来源国：美国 +178% 至超 450 万，法国翻倍至 250 万，德国 1,359,473，新加坡 911,605；中国略降至 816,154。建议 ASN 级过滤而非全国封禁。
- 🗺️ 目标地：韩国多目录遍历/文件泄露；加拿大最受新漏洞武器化影响；美国攻击组合最广；英国新旧漏洞混合；日本长期探测老旧服务端漏洞。
- ✅ 结论：Vite 相关文件读取尝试从前三个月基线 1,732 升至 8 月超 32,000；风险主要由暴露面决定，开发工具不应暴露公网。
- 🛠️ 建议：升级 Vite 至 7.3.2、8.0.5 或 4.5.x/5.4.x/6.x 最新补丁；限制开发服务器绑定；审计 Docker/K8s/安全组，禁止暴露 5173 等端口。
- 🧱 建议：部署现代 WAF（如 F5 Advanced WAF）并拒绝包含 `/@fs/` 的请求；对爬虫做反向 DNS 验证，不依赖 User-Agent；若 8 月暴露过未修补 Vite，立即轮换 .env、AWS、Azure、Terraform 等凭据。

---

### [](https://developer.apple.com/documentation/safari-release-notes/safari-27-release-notes)

**原文标题**: [Safari 27 Release Notes | Apple Developer Documentation](https://developer.apple.com/documentation/safari-release-notes/safari-27-release-notes)

该页面依赖 JavaScript 才能显示内容，并为自动化工具和辅助工具提供了 Markdown 版本作为替代访问方式。

- ⚠️ 页面提示必须启用 JavaScript。
- 🔄 需要在浏览器中开启 JavaScript 并刷新页面，才能查看内容。
- 🤖 自动化工具和辅助工具可使用专门的 Markdown 版本。
- 📄 可通过“查看 Markdown”入口访问页面内容的 Markdown 版本。

---

### [](https://webkit.org/blog/18227/fixing-top-level-await-in-safari/)

**原文标题**: [  Fixing Top-Level Await in Safari | WebKit](https://webkit.org/blog/18227/fixing-top-level-await-in-safari/)

WebKit 为 Safari 27 从底层重写模块加载器，实现顶层 await 的完整规范兼容，修复长期存在的“初始化前访问”错误，并显著提升 ES 模块整体的可靠性。

- 🧩 顶层 await 允许在模块顶层使用 await，像 async 函数一样简化 Promise 链；遇到 await 时暂停执行，并挂起依赖它的导入模块，但不影响无关兄弟模块。
- 🐞 旧版 Safari 会因模块加载顺序错误，导致动态 import 同一模块时出现乱序和“Cannot access ... before initialization”错误。
- 🧪 示例中旧加载器输出顺序为 2、3、1 且访问导出失败；新加载器按预期输出 1、2、3，并正确访问所有导出。
- 📜 根因是旧模块加载器基于已过时的 WHATWG Loader 提案，未按 ECMAScript 2022 的异步模块执行算法实现顶层 await。
- 🛠️ WebKit 从 2026 年 1 月开始重写：删除旧的自托管 JavaScript 模块加载器，逐项按 ECMAScript 规范用 C++ 实现。
- ⚙️ 放弃自托管 JavaScript builtins 是为了避免启动慢、JIT 难以优化、非热路径下性能不稳定等问题，改用原生 C++ 提升稳定性与可预测性。
- 🔁 实现时先处理 ExecuteModule、ModuleRequestsEqual 等叶子函数，并借助调用关系流程图推进复杂状态机。
- 🧷 测试包括 Bun 团队提供的失败用例、通过 jsc 集成测试、用 fuzzer 生成复杂模块图，并与其他 JS 引擎输出逐字节对比。
- ✅ 新加载器通过 test262 模块测试，修复多个 WPT 模块测试且无回归；团队已每日使用集成新加载器的 Safari 构建数周。
- 🚀 用户可下载 Safari Technology Preview 251 或 Safari 27 beta 试用；Safari 27 正式发布后即可在生产中使用顶层 await，反馈可提交至 bugs.webkit.org。

---

### [](https://github.com/tc39/agendas/blob/main/2026/09.md)

**原文标题**: [agendas/2026/09.md at main · tc39/agendas · GitHub](https://github.com/tc39/agendas/blob/main/2026/09.md)

Ecma TC39 第 116 次会议将于 2026 年 9 月 29 日至 10 月 1 日在日本东京举行，由 Sony 主办，时间按 JST 计算；前两天为 10:00–17:00，最后一天为 10:00–16:00。预计会议容量为 15:00h，关键截止包括提案晋级截止 9 月 19 日 10:00 JST、日程限制截止 9 月 26 日 10:00 JST。议程涵盖报告、需共识 PR、各阶段提案讨论、长时讨论及日程约束等内容。

- 🏢 主办与地点：Sony 主办，会议地点为日本东京。
- 🗓️ 日期时间：2026 年 9 月 29 日–10 月 1 日；前两天 10:00–17:00 JST，第三天 10:00–16:00 JST。
- ⏳ 关键截止：会前一个月里程碑为 8 月 29 日；提案晋级截止为 9 月 19 日 10:00 JST；日程限制截止为 9 月 26 日 10:00 JST。
- 📋 议程规则：Stage 0/1/2/2.7/3/4 晋级均需在截止前加入并注明；Stage 4 必须链接规范 PR；材料大幅变更可能影响共识。
- 🗂️ 排序规则：提案类议程主要按阶段降序、timebox 升序、插入日期排序。
- 🏷️ 议程标记：❄️ 表示硬日程限制，🔒 表示日程限制，⌛️ 表示迟交或日程优先，🔁 表示延续议题。
- 👋 开场事项：欢迎、点名、行为准则、参会者介绍、IPR 政策、沟通工具、GitHub Delegate 团队提醒、速记支持、通过议程与上次纪要等。
- 📊 报告环节：秘书报告；ECMA262、ECMA402、ECMA404、Test262 编辑报告；TG3 安全、TG4 Source Maps、TG5 标准化实验；CoC 委员会更新。
- ⚖️ 需共识/Web 兼容 PR：DataView 分离缓冲区行为、尾调用优化设为规范性可选、WeakRef KeptAlive 语义变更。
- 🧩 短时讨论：TC39 数据仓库与提案状态跟踪更新。
- 🚀 Stage 3 提案：Iterator Join、Iterator Includes、Iterator Chunking 争取 Stage 4；禁止向不可扩展对象添加新私有字段。
- 🔄 其他阶段提案：ESM Phase Imports、Amount、export defer、export * 默认包含、BigInt from exponential、Composites 等。
- 💬 长时讨论：重构 Cover 与 Supplemental Grammars。
- 🕒 日程限制：Kevin Gibbons 不愿 15:00 JST 后发言；Nicolò Ribaudo 希望 export * 议题先于 export defer 且偏好 15:00 后；Guy Bedford 仅最后一天 10:00–12:00 JST 可发言，第一天可能在飞行 WiFi 上参会。
- 🙏 其他事项：感谢主办方，随后休会。

---

### [](https://github.com/tc39/proposal-iterator-join)

**原文标题**: [GitHub - tc39/proposal-iterator-join: JS proposal for a means to concatenate the contents of an iterator into a string · GitHub](https://github.com/tc39/proposal-iterator-join)

该仓库是 TC39 的 Iterator Join 提案：为 JavaScript 增加把迭代器内容拼接成字符串的能力。当前处于 Stage 3，已有规范与 test262 测试，准备进入实现。

- 🧭 提案目标：新增 `Iterator.prototype.join`，用于将迭代器内容连接为字符串。
- 🧱 接口设计：行为与 `Array.prototype.join` 类似，但作用于迭代器接收者，而不是数组。
- 🚦 进展状态：TC39 Stage 3，已有 specification 和 test262 tests，可供实现。
- 👤 相关人员：作者与 Champion 均为 Kevin Gibbons。
- 💡 动机：把字符串列表拼接成单个字符串是常见操作；数组可直接用 `.join(sep)`，其他可迭代对象则缺少便捷方法。
- ⚠️ 现有替代方案：`Iterator.from(it).reduce(...)` 会分配中间字符串且空迭代器会出问题；`Array.from(it).join(sep)` 需要先转换为数组。
- 📂 仓库内容：包含 README、LICENSE、package.json、polyfill.js、run-test262.mjs、spec.html 等文件。
- 📈 仓库数据：16 stars、2 forks、1 issue、8 watchers、6 commits，采用 MIT 许可证。
- 🌐 页面提示：页面顶部显示加载错误，需重新加载页面。

---

### [](https://github.com/tc39/proposal-iterator-includes)

**原文标题**: [GitHub - tc39/proposal-iterator-includes: Array.prototype.includes but for iterators · GitHub](https://github.com/tc39/proposal-iterator-includes)

该仓库是 TC39 的 `proposal-iterator-includes` 提案，目标是让开发者判断迭代器是否会产出某个值，类似 `Array.prototype.includes`；目前处于 Stage 3，进一步推进需至少 2 个已发布实现。

- 🎯 新增 `Iterator.prototype.includes` 方法，用于查询迭代器是否产出指定值。
- 🧩 动机与 `Array.prototype.includes` 相同：用 `some` 加自定义比较器不够直接，标准方法应简单、简洁。
- ⚖️ 比较算法选用 SameValueZero，以与 `Array.prototype.includes` 保持一致。
- 🔍 支持第二参数 `fromIndex`，用于从指定位置开始搜索；迭代器虽可用 `drop` 替代，但为减少数组用户困惑而保留。
- 🚫 `fromIndex` 不支持负偏移，这是与数组版本的不同点，但在迭代器语境下合理。
- 🧪 示例：`gen().includes(1)` 为 `true`，`gen().includes(2)` 为 `false`，`gen().drop(1).includes(1)` 为 `false`。
- 📜 规范地址：https://tc39.es/proposal-iterator-includes/
- 🗂️ 仓库公开于 `tc39/proposal-iterator-includes`，包含源码、测试、规范与配置文件。
- 📊 当前仓库约 12 stars、3 forks、1 issue、13 commits。
- 🗓️ 委员会演示材料标注为 2026 年 3 月。

---

### [](https://github.com/tc39/proposal-iterator-chunking)

**原文标题**: [GitHub - tc39/proposal-iterator-chunking: a proposal to add a method to iterators for producing an iterator of its subsequences · GitHub](https://github.com/tc39/proposal-iterator-chunking)

该仓库是 TC39 的 Iterator Chunking 提案，目标是为迭代器添加按可配置大小消费为重叠或非重叠子序列的方法，目前处于 Stage 3，后续推进需至少两个已发布实现。

- 📦 提案核心：让迭代器支持 `chunks`（非重叠子序列）与 `windows`（重叠滑动窗口）。
- 🧩 `chunks(n)` 示例：`[0..9].chunks(2)` 得到 `[ [0,1], [2,3], ... ]`；不足末尾的一组可能保留较短序列。
- 🪟 `windows(n)` 示例：`[0..9].windows(2)` 得到 `[ [0,1], [1,2], ... ]`，用于滑动窗口。
- 🎯 用例：分页、日历/网格布局、批/流处理、矩阵操作、格式化/编码、分桶、运行平均值、成对比较、轮播等。
- 🌐 先例：C++、Clojure、Elm、Haskell、Java、Kotlin、.NET、PHP、Python、Ruby、Rust、Scala 以及多个 JS 库均有类似实现，但 0 大小/窗口截断等边界行为不一。
- 📜 规范与仓库：规范见 tc39.es/proposal-iterator-chunking；仓库公开，含 src、test、spec.emu、demo 等，约 104 stars、2 forks、52 commits、1 issue。

---

### [](https://openjsf.org/blog/the-openjs-foundation-cna-is-taking-a-coordinated-break)

**原文标题**: [The OpenJS Foundation CNA is taking a coordinated break: September 17 to October 6, 2026 | OpenJS Foundation](https://openjsf.org/blog/the-openjs-foundation-cna-is-taking-a-coordinated-break)

OpenJS 基金会 CNA 将于 2026 年 9 月 17 日至 10 月 6 日暂停安全运营，以应对 AI 生成漏洞报告激增导致的志愿者倦怠，并倡导开源维护者重视休息与可持续性；Express 也加入，团队将于 10 月 7 日恢复。

- ⏸️ 暂停时间：2026 年 9 月 17 日至 10 月 6 日（含首尾），OpenJS 基金会 CNA 所有安全运营暂停。
- 🤖 主要原因：大语言模型生成或辅助的漏洞报告激增，低信号报告多，人工审核耗时耗力，志愿者不堪重负。
- 🧑💻 团队健康：此举优先保障志愿者可持续性、休息与长期工作质量，避免过度倦怠。
- 📅 时间考量：暂停期与 Node.js Collaborator Summit 重叠，便于社区成员线下参与；Express 项目也加入。
- 🌴 先例参考：curl 项目曾进行为期一个月的“Summer of Bliss”漏洞接收暂停，并称效果积极。
- 🚫 暂停范围：新报告分类与确认、公告验证、CVE 分配、发布以及升级处理均暂停。
- 📬 渠道状态：邮件、公告和报告提交仍可发送，但期间不会回复；请求将排队至 10 月 7 日后处理。
- 🚨 紧急例外：若漏洞正被积极利用或构成严重即时风险，仍会响应；可通过 OpenJS Slack #security 频道求助，首条消息应高层级、不含敏感细节并标注紧急。
- ❤️ 维护者提醒：鼓励开源维护者允许自己休息，倦怠真实存在，长期可持续性比持续产出更重要。
- 🔜 恢复时间：团队将于 2026 年 10 月 7 日回归。

---

### [](https://github.blog/changelog/2026-09-09-npm-extends-recovery-code-security-holds-to-all-accounts/)

**原文标题**: [npm extends recovery-code security holds to all accounts - GitHub Changelog](https://github.blog/changelog/2026-09-09-npm-extends-recovery-code-security-holds-to-all-accounts/)

overview summary
npm 将恢复代码登录后的临时安全冻结从高影响账户扩展至所有账户，以加强账户接管防护并降低供应链风险。

- 🛡️ npm 现在会对任何账户在成功使用恢复代码登录后实施 72 小时临时安全冻结。
- ⏸️ 冻结期间，发布和创建访问令牌等安全敏感写入操作会暂停；用户仍可登录、浏览和安装包。
- ⏰ 冻结会自动到期，无需操作或联系支持即可恢复完整访问。
- 🔒 此扩展基于此前针对高影响账户的保护措施，旨在减缓账户接管并降低恢复代码泄露后的恶意发布风险。
- 🆘 如果未使用恢复代码登录却被意外阻止发布，应立即联系 npm Support。
- 📅 该改进发布于 2026 年 9 月 9 日，属于供应链安全更新。

---

### [pnpm 12.4 | pnpm](https://pnpm.io/blog/releases/12.4)

**原文标题**: [pnpm 12.4 | pnpm](https://pnpm.io/blog/releases/12.4)

pnpm 12.4 于 2026 年 9 月 10 日发布，作者 Zoltan Kochan；重点是在同一 workspace 中支持 npm、Cargo、Python 依赖，新增类似 CI 的 `pnpm pipeline`，增加六个平台二进制，并随附 `pnpr 0.1.0-alpha.11`：支持 Cargo/Python/容器注册中心、跨生态单事务发布和 OIDC 登录。12.4.1 主要修复兼容性问题并提升重复安装性能。

- 🧩 同一 workspace 可管理 npm、Cargo、Python：在 `pnpm-workspace.yaml` 开启 `cargo.enabled` / `python.enabled`，用 `pnpm install` 安装，`pnpm add crate:serde` / `pypi:httpx` 添加依赖。
- 🦀 Cargo 保持自身语义：使用 `Cargo.toml`/`Cargo.lock`，解析 crates.io 或 `cargo.indexUrl` 稀疏注册表，vendor 到 Cargo 目录源，支持 git/patch 检出，并通过 pnpm 凭据、`CARGO_REGISTRY_TOKEN`、`$CARGO_HOME/credentials.toml` 认证。
- 🐍 Python 使用 `pyproject.toml` 与 `pylock.toml`，每项目维护 `.venv`，`pnpm run`/`pnpm exec` 将其加入 PATH，锁文件格式已用 `uv` 独立验证。
- 🔗 三生态共享底层 HTTP/认证预算、验证制品摄取路径和内容寻址存储；支持 frozen/offline，可把解析交给 `pnprServer` 并在不支持时回退本地；当前仍属早期，设置和布局可能变化。
- ⚙️ 新增 `pnpm pipeline [name]`：安装冻结依赖并运行命名 workspace 任务集，选择受影响项目、按任务图执行，任务失败后继续，以一次运行报告所有失败。
- 🧠 pipeline 任务可声明 `dependsOn`、`outputs`、`inputs`、`env`、`cache`；`outputs` 决定可缓存性，`outputs: []` 表示无文件输出；命中时恢复输出并重放日志。
- 🧪 `pipelines.default` 可组合 build/test 等任务；Cargo 任务可用 `tasks.<name>.cargoTargetDir` 复用本地构建状态；`--dry-run` 只打印图，不安装也不运行 hook。
- 💻 新增六个平台二进制：Android arm64/x64、FreeBSD x64、Linux ppc64le、s390x、RISC-V。
- 🧹 `trustPolicyExcludePrune` 可清理 `trustPolicyExclude` 中锁文件不再解析的条目，默认关闭，保留 `@scope/*`，`sharedWorkspaceLockfile=false` 时跳过。
- ✅ `pnpm change check` 按 `versioning.epics` 与 `versioning.fixed` 校验 workspace 提交版本，不读取 change intents，适合每个 PR 的 CI，并报告所有违规。
- 🌐 注册表元数据按完整 URL 区分 path/scheme，避免混用不同注册表的版本/tarball URL，也避免 HTTP 元数据复用于 HTTPS；升级后首次安装会重新获取元数据。
- 🧾 `pnpm cache view` 现在显示完整注册表 URL，解析 `pnpm cache

---

### [](https://github.com/microsoft/playwright/releases/tag/v1.63.0)

**原文标题**: [Release v1.63.0 · microsoft/playwright · GitHub](https://github.com/microsoft/playwright/releases/tag/v1.63.0)

Playwright v1.63.0 发布，重点带来测试锁、跨 frame 定位、可见元素定位、步骤参数与副标题、trace 的 Aria/屏幕快照等能力，并扩展 API、报告器、CLI 与浏览器支持；同时宣布部分实验组件包停止更新及 Ubuntu 20.04 不再支持。

- 🔒 测试锁：访问共享资源的测试可声明命名锁，跨文件、worker、项目互不并发，其他测试仍并行；支持多个锁及 `test.describe()` 组级锁。
- 🪟 跨 frame 定位：`page.frameLocator()` 和 `frame.frameLocator()` 不传选择器时可在任意子 frame 中搜索，匹配多个 frame 会报错。
- 👁️ 可见定位器：新增 `locator.visible()`，仅匹配可见元素，推荐替代 `:visible` CSS 伪类。
- 🧾 步骤增强：Playwright API 步骤会报告目标定位器和调用参数；`test.step()` 支持 `subtitle` 和 `params`，报告器可读取并在 trace viewer/HTML 报告中展示。
- 🖼️ Trace 快照：`tracing.start()` 和 `testOptions.trace` 的 `snapshots` 可选择捕获 `dom`、`aria`、`screen`；trace viewer 新增 Display Aria 模式，可并排查看并悬停高亮。
- 🔐 认证扩展：`httpCredentials` 支持凭据数组，按请求 origin 匹配，无 origin 的条目可匹配任意请求。
- 🗂️ 存储状态：新增 `opfs` 选项，将 origin private file system 纳入 storage state，便于持久化与恢复。
- 🔔 新事件：`page.on('dialogclosed')` 和 `browserContext.on('dialogclosed')` 在 JS 对话框被接受、关闭或用户关闭时触发。
- 🧩 Aria API：新增 `locator.ariaSnapshotJSON()` 和 `page.ariaSnapshotJSON()`，以 JSON 返回 Aria 快照，支持 `mode`、`depth`、`boxes`。
- 🌐 请求类型化：`apiRequestContext.get()` 等请求方法支持类型参数，使 `response.json()` 返回指定类型。
- 🧪 测试选项：新增独立的 `testOptions.reducedMotion`、`testOptions.forcedColors`、`testOptions.contrast`。
- ➕ CLI 增强：`--add-reporter` 可追加报告器；`npx playwright install --no-remove` 保留其他 Playwright 安装的浏览器；`codegen --http-credentials` 支持录制 HTTP 认证页面。
- 🏷️ 报告器标签：`list`、`line`、`dot`、`github`、`junit` 报告器新增 `omitTags`，可抑制自动附加到测试标题的标签。
- 📈 报告与时间线：内置 `perfetto` 报告器输出 Trace Event Format 文件，可在 Perfetto UI 或 `chrome://tracing` 中查看；HTML 报告显示测试步骤时长瀑布。
- ⚠️ 重要公告：实验性 `@playwright/experimental-ct-react`、`ct-react17`、`ct-vue` 不再更新，需迁移到 stories 模型；Ubuntu 20.04 不再支持；Linux arm64 改用 Chrome for Testing 构建的 Chromium。
- 🌍 浏览器版本：Chromium 153.0.8010.12、Mozilla Firefox 155.0、WebKit 26.6；同时测试兼容 Google Chrome 153 和 Microsoft Edge 153。

---

### [Node](https://nodejs.org/en/blog/release/v26.8.2)

**原文标题**: [Node.js — Node.js 26.8.2 (Current)](https://nodejs.org/en/blog/release/v26.8.2)

Node.js 26.8.2 是 Current 版本，发布于 2026-09-09，由 Antoine du Hamel（@aduh95）发布，主要内容包括依赖升级、文档修正、测试稳定性改进、类型定义补充，以及部分 API 弃用和实验特性安全策略调整。

- 📌 版本：Node.js 26.8.2（Current），发布日期 2026-09-09，发布者 @aduh95。
- ⚠️ 重要变更：`node:net` 中 `Server.prototype._listen2` 被弃用。
- 🛡️ 安全策略：细化实验性功能的安全漏洞处理姿态。
- 📦 核心依赖升级：Undici 升至 8.10.2，OpenSSL 升至 3.5.8。
- 📦 其他依赖更新：npm 11.19.1、Corepack 0.36.0、googletest、simdjson 4.6.9、Perfetto 58.2、zlib 1.3.2.1-motley 等。
- 📝 文档改进：修正 `fs.mkdtemp*` 返回类型、`crypto.setEngine` 稳定性状态、TLS 警告、链接与目录、AI 指南、AbortSignal 清理建议等。
- 🧪 测试稳定性：大量 deflake 测试，并针对 AIX、IBM i、riscv64、WASI、Windows 等平台进行跳过或修复。
- 🏗️ 构建系统：改进 riscv64 默认标志、GN 构建中的 `NODE_ARCH` 推导，以及 Windows LTO 并行限制调整。
- 🧹 元信息维护：更新 GitHub Actions/CodeQL 相关依赖，清理 emeritus 变更，记录协作自动化。
- 🛠️ 工具链维护：更新 ESLint 依赖，避免硬编码 yamllint/Ruff 路径，完善首次贡献者欢迎与查询流程。
- 🧩 类型定义：补充 `fs_event_wrap`、`stream_pipe`、`profiler`、`ffi` 等内部绑定类型，并更新 zlib 声明。
- 💻 下载支持：提供 Windows、macOS、Linux、AIX、ARM64 等平台安装包、二进制与源码。
- 🔐 完整性校验：发布 SHA256 校验和及 PGP 签名，覆盖安装包、二进制和源码等文件。
- 📄 发布文件与文档：可从 `https://nodejs.org/dist/v26.8.2/` 和 `https://nodejs.org/docs/v26.8.2/api/` 获取。
- ⏭️ 下一版本：Node.js 24.21.0（LTS）。

---

### [Node.js —— Node.js 24.21.0（长期支持版）](https://nodejs.org/en/blog/release/v24.21.0)

**原文标题**: [Node.js — Node.js 24.21.0 (LTS)](https://nodejs.org/en/blog/release/v24.21.0)

Node.js 24.21.0 'Krypton'（LTS）于 2026-09-08 发布，带来多项 SEMVER-MINOR 功能、依赖升级、性能优化，以及大量核心模块修复、文档、测试、构建与工具链改进。

- 🚀 发布信息：Node.js 24.21.0（LTS，代号 Krypton），由 @aduh95 发布。
- 🔐 加密更新：根证书升级至 NSS 3.126；支持通过 STORE loaders 加载私钥；修复 ASN1、FIPS、BoringSSL 等相关问题。
- 📦 依赖升级：OpenSSL 升至 3.5.8，Undici 升至 7.29.1，Corepack 升至 0.36.0，并更新 zlib、simdjson、googletest 等。
- ⚡ 性能优化：改进 histogram 实现、net.BlockList、HTTP end()、URL 解析、URLSearchParams、stream/webstreams 热路径等性能。
- 🧰 API 增强：perf_hooks 直方图新增统计假设检验；util 新增非抛错的 MIMEType.parse；tty 增加 raw-vt 和 io raw 模式。
- 🛠️ 核心修复：覆盖 buffer、fs、http/http2、quic、sqlite、stream、tls、url、dns、dgram、child_process、permission、SEA 等模块。
- 🧪 测试与文档：大量 WPT 更新、测试稳定性与覆盖率改进；文档修正与新增说明，涉及 AI 指南、SQLite、QUIC、WebCrypto 等。
- 🔧 构建与工具：改进构建系统、FIPS/OpenSSL 处理、PGO 脚本、commit queue、依赖 bump 和工作流权限。
- 📥 下载与校验：提供 Windows、macOS、Linux、AIX、ARMv8 等安装包/二进制/源码/文档链接，并附 SHASUMS 与 PGP 签名。

---

### [](https://reactrouter.com/changelog#v840)

**原文标题**: [CHANGELOG.md  | React Router](https://reactrouter.com/changelog#v840)

这份文档是 React Router 的完整更新日志，涵盖从 v7.0.0 到 v8.4.0 的所有版本发布说明。它详细记录了每个版本的新功能、破坏性变更、补丁修复和不稳定特性。核心内容包括 v8 系列的正式发布、性能优化、RSC 支持演进，以及 v7 系列中中间件、路由匹配和类型安全等 API 的逐步稳定化过程。

- 🚀 **v8.4.0 性能优化**：重构内部数据路由器上下文，减少路由组件不必要的重渲染；引入基于 `@remix-run/route-pattern` 的更高效路由匹配（unstable），基准测试显示导航和 fetcher 完成时间提升约 19%–88%。
- 🧩 **v8.0.0 重大版本发布**：最低支持 Node 22.22.0、React 19.2.7、Vite 7+，改为 ESM-only；所有 `future.v8_*` 标志行为成为默认，正式移除 `react-router-dom` 包和已弃用的 `meta` 的 `data` 字段。
- 🌊 **v8.2.0 Web Streams 默认入口**：非 Node 运行时框架模式应用默认使用 `renderToReadableStream`，Node 应用可通过 `future.unstable_enableNodeReadableStream` 标志选择启用。
- 🤖 **v8.1.0 Agent Skills 与可观测性**：`create-react-router` 支持安装官方 Agent Skill；服务器处理器、客户端导航和 fetcher 的插桩结果新增 URL、路由模式、参数和状态码等元数据。
- ⚛️ **RSC（React Server Components）支持演进**：从 v7.7.0 引入实验性 Data Mode RSC API，到 v7.9.2 支持 RSC 框架模式，再到 v8.3.0 完善 RSC 入口、子资源完整性和 CSP nonce 支持。
- 🛡️ **安全性修复**：v7.12.0 修复 CSRF、开放重定向 XSS 和 ScrollRestoration XSS 三个漏洞；v7.5.2 修复缓存投毒；v7.5.2/v7.4.1 修复 Host 头操作和端口清理漏洞。
- 🧱 **中间件与上下文 API 稳定化**：v7.9.0 移除 `unstable_` 前缀，正式稳定 `RouterContextProvider`、`createContext` 等 API；v8 中中间件始终启用，`context` 参数统一为 `RouterContextProvider` 实例。
- ⚡ **路由匹配优化**：v7.15.0 通过缓存扁平化/排序后的路由分支，将服务器端请求处理性能提升约 10%–30%；v7.1.4 起持续优化 `matchRoutes` 调用。
- 🔗 **类型安全增强**：v7.2.0 新增类型安全的 `href` 工具函数；v7.6.0 支持未来标志自动生成类型；v7.0.0 起为每个路由模块生成类型并提供类型化组件 props。
- 🗂️ **路由配置与预渲染**：v7.0.0 引入 `app/routes.ts` 配置式路由和 `prerender` 配置支持 SSG；v7.6.0 新增 `routeDiscovery` 配置项控制懒路由发现。
- 🔄 **客户端状态与导航改进**：v7.15.1 新增 `unstable_useRouterState()` 钩子整合活跃和待处理路由状态；v7.10.0 稳定 `fetcher.reset()` 和 `DataStrategyMatch.shouldCallHandler()`。

---

### [](https://github.com/vitejs/vite/releases/tag/v8.3.0)

**原文标题**: [Release v8.3.0 · vitejs/vite · GitHub](https://github.com/vitejs/vite/releases/tag/v8.3.0)

Vite 发布 v8.3.0，由 GitHub Actions 于 9 月 10 日 11:25 发布，属于不可变发布，提交 434e8e9 已使用 GitHub 验证签名。该版本包含构建性能优化、CRLF 处理、node_modules 路径判断修复以及代理匹配器预编译性能改进；仓库当前约 82.8k 星标、8.7k Fork、502 个 Issue、272 个 PR。页面中多次出现加载错误提示。

- 🚀 **版本发布**：Vite v8.3.0 于 9 月 10 日 11:25 由 github-actions 发布，发布不可修改。
- ✅ **提交与签名**：提交 434e8e9 经 GitHub 验证签名，GPG key ID 为 B5690EEEBB952194。
- 🏗️ **新特性**：build 中避免结算已见过的预加载依赖以提升性能（#23446）。
- 🐛 **Bug 修复**：处理代码帧位置中的 CRLF 换行符（#23219）。
- 📦 **Bug 修复**：仅将完整的 node_modules 路径段视为依赖，修复 #17467（#23437）。
- ⚡ **性能改进**：proxy 在服务器创建时预编译上下文匹配器（#23263）。
- 📊 **仓库数据**：82.8k 星标、8.7k Fork、502 个 Issue、272 个 Pull Request。
- ⚠️ **页面提示**：内容中多次出现“Uh oh! There was an error while loading. Please reload this page.”加载错误。
- 🎉 **社区反应**：18 人参与反应；👍9、😄1、🎉5、❤️6、🚀3、👀2。

---

### [发布 2.31.0 · moment/moment · GitHub](https://github.com/moment/moment/releases/tag/2.31.0)

**原文标题**: [Release 2.31.0 · moment/moment · GitHub](https://github.com/moment/moment/releases/tag/2.31.0)

Moment.js 2.31.0 已作为最新版本发布，重点包括安全修复、缺陷修复、新功能、新增语言及大量本地化更新；页面中多次出现加载错误提示。

- 🗓️ 发布时间：2.31.0 于 2026 年 9 月 14 日发布，并标记为 Latest。
- 🔐 安全修复：修复 CVE-2026-17495（GHSA-4p3w-j4w9-5jqw）。
- 🐛 缺陷修复：防止对象原型属性被用作格式标记，并修复解析、缓存、locale 污染等问题。
- 🧾 解析与格式：修复 eHHmm 解析、仅含部分日期的星期错配、继承的小写长日期格式等。
- 🧮 参数与范围：min/max 忽略非 Moment 参数，解析时区偏移时验证范围。
- 🌐 本地化机制：规范化懒加载语言名，更新后重置解析缓存，避免 locale('__proto__') 污染全局。
- 🧹 其他改进：duration.humanize 避免 Object.assign，所有语言包包含元数据，相对时间方法应用 postformat。
- ⚠️ 调试增强：为条件性弃用警告添加堆栈跟踪。
- ✨ 新功能：为 Moment Timezone 增加内部日期默认钩子（#6451）。
- 🌍 新增语言：Pashto（'ps'）与 Amharic（Ethiopia，'am-et'）。
- 🇧🇷 语言更新示例：葡萄牙语（巴西）修复时间复数，印尼语修正八月缩写。
- 🇪🇺 更多语言更新：格鲁吉亚语、荷兰语（比利时）、瑞典语、加泰罗尼亚语、斯瓦希里语、乌克兰语、匈牙利语、德语、乌兹别克语、波兰语等均有修正。
- 📊 仓库与发布：moment/moment 公开仓库约 47.9k Star、7k Fork；本次发布含 2 个资源。
- 👍 社区互动：发布获得 👍😄🎉❤️🚀👀 等表情反应。
- ⚠️ 页面问题：内容中多次出现“加载错误，请刷新页面”的提示。

---

### [](https://cel.cs.brown.edu/blog/design-space-async-await/)

**原文标题**: [A Design Space Exploration of Async/Await](https://cel.cs.brown.edu/blog/design-space-async-await/)

overview summary
- 🧵 现代语言常用 async/await 表达并发，目标是让并发程序看起来像直线式代码，作者称之为“直线式异步”。
- 🔍 该项目研究不同语言 async/await 的相似与差异，结论是差异远超预期，并写下论文《A Design Space Exploration of Async/Await》。
- 🧪 用一个伪代码示例：后台任务写日志但不被 await，主函数等待后打印 C；七个运行时给出多种不同输出，三个变体中没有两个运行时完全一致。
- 🧭 论文从现代实现中总结出九个影响可观察语义的设计维度，并分为任务生命周期的三类：开始、结束与取消。
- 🚀 开始阶段包括：Eagerness（惰性/急切）与 Suspension（是否保证 await 点挂起）。
- 🏁 结束阶段包括：Extent（任务存活范围）、Reference Strength（运行时强/弱引用）、Destruction（等待完成/取消/终止）、Propagation（未等待任务异常处理）。
- 🛑 取消阶段包括：Awareness（是否可响应取消）、Direction（取消传播方向）、Persistence（取消是否持久）。
- 🐍 不同语言和运行时选择不同组合，例如 Python、Rust、C#、JavaScript、Swift、Tokio、Smol、Asyncio、Trio。
- 🍎 示例中 Swift 与 Trio 都采用 Dynamic Extent，但 Destruction 不同：Swift 取消任务并打印“AC”，Trio 等待任务完成并打印“ABC”。
- 🧮 作者把设计空间形式化为异步核心演算的语义，用执行轨迹解释同一程序为何产生不同结果。
- ⚖️ 每个设计维度都有性能、内存、人机工程和语义等权衡，没有绝对对错，但说明即使小程序的输出也难以凭直觉预测。
- 📄 想理解自己常用语言的 async/await 语义和设计取舍，可阅读该论文。

---

### [](https://shopify.engineering/back-to-native)

**原文标题**: [Native is now the future of mobile at Shopify (2026) - Shopify](https://shopify.engineering/back-to-native)

Shopify 宣布移动端战略从 React Native 转向 Swift 与 Kotlin 原生开发。LLM/编码代理大幅降低了双平台实现、翻译、测试和审查成本，改变了 2020 年全面采用 React Native 时的核心假设；原生则让代码更贴近平台能力和第一方工具。迁移将用 AI 辅助重建，Shop 已率先发布原生版，Shopify 主应用等将跟进，且不降低性能、稳定性、可访问性和产品质量标准。

- 🧭 2020 年 Shopify 全力投入 React Native，节省重复开发、让非移动背景开发者参与，并减少功能对齐成本。
- 🤖 2025 年后编码模型显著变强，Shopify 重新评估技术栈；代理可用 iOS 版参考实现 Android 版，反之亦然，并帮助跨栈贡献。
- ⚖️ 原生仍需维护两个平台，但代理承担了足够多的实现、翻译、测试和审查工作，使双平台成本不再是决定性因素。
- 📱 原生优势在于更接近平台能力与第一方工具，减少框架和依赖层；React Native 仍快，但共享实现的优势被代理削弱。
- 📦 React Native Skia：Shopify 继续赞助至 2026 年底，William Candillon 将 fork 并以新名称发布，原仓库随后归档。
- 🗂️ FlashList 每周约 200 万下载，Shopify 将继续修复关键兼容问题，并寻找长期维护者；Restyle 将在 2026 年底后停止维护并归档。
- 🏗️ 迁移选择 greenfield 从零重建，而非 brownfield 渐进迁移；LLM 可参考 RN 版构建 Swift/Kotlin，且原型显示重建快得多。
- 🛍️ Shop 应用是首个迁移项目，借助 AI 用 12 周从概念验证到发布原生应用；Shopify 主应用（300+ 屏幕、小组件、Apple Watch 等）也在迁移，今年晚些发布。
- 🧬 为避免“AI slop”，Shopify 构建 Helix：把屏幕拆成检查点，每个检查点需通过测试、视觉审查、两个对抗性代码审查和人工批准，反馈会被记住。
- 🧪 为加速反馈，业务逻辑与 UI 解耦并可在桌面 headless 运行；CLI 让代理毫秒级检查状态、导航和操作，模拟器远程模式驱动 UI 而无需无障碍树。
- 🚀 下一步：所有 Shopify 移动应用都将用 AI 迁移到 Swift/Kotlin；成功指标是产品速度、应用质量及代理自主完成的工作量，并将分享 Helix 等经验。
- 🙏 文章致谢 Meta、William Candillon、Software Mansion、Shopify 工程师和 React Native 社区，并提到正在招聘移动、基础设施和 AI 软件工程人才。

---

### [](https://sentry.io/resources/beyond-logs-basics-workshop/?utm_source=javascriptweekly&utm_medium=paid-community&utm_campaign=logs-fy27q3-logsworkshop&utm_content=newsletter-sponsored-link-beyond-basics-register)

**原文标题**: [Sentry Logs, Beyond the Basics | Sentry](https://sentry.io/resources/beyond-logs-basics-workshop/?utm_source=javascriptweekly&utm_medium=paid-community&utm_campaign=logs-fy27q3-logsworkshop&utm_content=newsletter-sponsored-link-beyond-basics-register)

Sentry Logs, Beyond the Basics 工作坊聚焦于把日志与追踪、错误结合使用，以更快找到根因，并在跨服务、跨语言请求中保持上下文，同时优化信噪比，避免错过关键日志。

- 🧰 Sentry Logs 是调试工具包的重要组成部分，为解释“为什么会发生”提供必要上下文。
- 🔍 工作坊演示如何将日志、追踪和错误结合，加速定位根本原因。
- 🌐 介绍跨服务边界记录日志的最佳实践，确保请求跨进程和语言时上下文不丢失。
- 📈 讲解如何调整信号与噪声：哪些日志级别真正重要，以及如何采样而不丢掉关键日志。
- 🎥 若错过上一期工作坊《Writing Useful Logs For Production》，可在线点播观看。
- 📚 更多资源包括《Writing Useful Logs For Production》与《Debugging Next.js Best Practices: Logs and Tracing》。
- 🚀 还可查看《Sentry 101: Live Demo》。

---

### [深入探究 StyleX](https://flaviocopes.com/stylex/)

**原文标题**: [A deep dive into StyleX](https://flaviocopes.com/stylex/)

overview summary
StyleX 是 Meta 推出的编译时样式方案：用 JavaScript 对象写样式，构建时生成可复用的原子 CSS 类，浏览器最终只收到普通 CSS。它通过类型、lint 和可预测组合来解决大型应用中的命名冲突、覆盖混乱、复用和一致性等问题，但需要编译器配置、较严格约束，并且不能替代对 CSS 本身的理解。

- 🧩 StyleX 是 JavaScript 语法和编译器，用 JS 对象定义样式，构建时转换为普通 CSS。
- 🚫 生产环境不做运行时样式注入；浏览器接收静态 CSS 类，样式在构建期提取。
- 🎯 它主要解决大型应用 CSS 问题：类名冲突、作用域、删除安全、覆盖原因、样式归属、共享组件定制和未使用 CSS。
- 🏢 由 Meta 创建，用于 Facebook、Instagram、WhatsApp、Messenger、Threads；Linear 在 2026 年迁移，涉及 1000+ PR。
- 🧠 心智模型：`stylex.create()` 定义样式对象，编译器生成哈希原子类，组件用 `stylex.props()` 应用。
- ⚛️ React + Vite 设置：安装 `@stylexjs/stylex` 和 `@stylexjs/unplugin`，在 `vite.config.ts` 中把 `stylex.vite()` 放在 `react()` 前。
- 🃏 第一个组件：用 `stylex.create()` 定义 `card`、`title` 等样式组，再用 `{...stylex.props(styles.card)}` 展开。
- 🔍 StyleX DevTools：开发模式添加 `data-style-src` 和可读标记类，Chrome 扩展可查看样式来源并跳转源文件。
- 🧑🚀 Astro：复用 Vite 插件，在 React 组件内使用；开发需要 `/virtual:stylex.css` 和运行时，生产提取到 Astro CSS。
- 🧱 原子 CSS：每个声明生成一个小类，公共声明可去重；HTML 类名更多，但 CSS 重复更少。
- 🧬 组合样式：`stylex.props(styles.card, styles.featured)`，同属性后者胜出，不依赖 CSS 源顺序或 specificity。
- 🎛️ 条件样式：使用普通 JavaScript 的 `&&` 或三元表达式，`false`、`null`、`undefined` 会被忽略。
- 🎨 变体：用对象查找如 `colorStyles[color]`，TypeScript 可限制可选键，无需额外变体配置。
- 🖱️ 状态样式：`:hover`、`:active`、`:disabled`、`:focus-visible` 写在属性内部；伪元素写在样式顶层。
- 📱 响应式：媒体查询、容器查询和 `@supports` 写在属性内部，可与伪类组合，`null` 表示该条件下不应用值。
- ⏳ 动态值：使用样式函数生成 CSS 变量和内联 `style`，仅用于真正运行时值；参数和函数体有静态限制。
- 🎫 设计令牌：`stylex.defineVars()` 创建类型化 CSS 变量，必须放在 `.stylex.ts` 等文件并命名导出。
- 🌗 主题：`stylex.createTheme()` 覆盖一组变量，像普通样式一样应用；子组件继续引用同一 token。
- 🧩 父组件传样式：使用 `StyleXStyles` 类型，可限制允许覆盖的属性，比无限制 `className` 更安全。
- 🎞️ 动画：`stylex.keyframes()` 定义关键帧，在样式中引用 `animationName`。
- 🧪 内联原子：`@stylexjs/atoms` 适合小型一次性例外；可复用组件仍更适合命名样式。
- 🧱 静态约束：样式对象不能运行任意 JS，不能导入普通变量或对象展开；共享值用 `defineVars/defineConsts`，组合用 `stylex.props()`。
- 🌐 全局 CSS：仅用于 reset、body 默认、字体、CMS 原始 HTML；启用 layers 时把 reset 放入独立层，并注意未分层规则优先级更高。
- ✅ Lint：`@stylexjs/eslint-plugin` 可检查有效样式、未使用样式、简写、排序，并能限制属性值以强制设计尺度。
- 🤖 对编码代理：StyleX 更啰嗦但选择空间更小，更容易让代理生成一致、可审查的代码；仍需要好 token、组件边界和 lint。
- 💰 成本：配置更复杂、语法更长、生态多与 Tailwind 相关，且需要放弃部分全局样式和深层选择器模式。
- ⚖️ 对比其他方案：普通 CSS 灵活但需自管作用域；Tailwind 书写快但标记膨胀；运行时 CSS-in-JS 动态但增加 JS；StyleX 生成 CSS + 小合并运行时，换取可预测组合。
- 🚀 适用场景：新 React 应用、增长中的组件库、大量代理改 UI；不建议为小项目迁移，也不适合以静态 Markdown 为主的 Astro 站点。
- 📦 生产构建：Vite build 后生成带哈希的原子 CSS，应用代码中不再有原始 `stylex.create()` 对象。
- 🧭 核心结论：StyleX 是编译器和约束系统，不是另一种 CSS 拼写；仍需理解布局、继承、响应式、可访问性和浏览器行为。

---

### [](https://stylexjs.com/)

**原文标题**: [StyleX — styling system for ambitious interfaces](https://stylexjs.com/)

StyleX 是一个面向雄心勃勃界面的样式系统，强调表达力、类型安全、可组合、可预测和可主题化。站点提供文档、API、博客、Playground 等入口，并涵盖开发、学习、探索、参与和 GitHub 等资源，页脚包含致谢、法律、隐私、条款及版权信息。

- 🎨 StyleX 是用于 ambitious interfaces 的样式系统
- 🧱 核心特性：表达力强、类型安全、可组合、可预测、可主题化
- 🚀 主要入口：Get Started、Thinking in StyleX
- 📚 资源导航：Docs、API、Blog、Playground、Search（⌘ K）
- 🛠️ 开发与学习：Develop、Learn、API、Explore
- 🧪 Playground 用于试验，Blog 用于阅读动态
- 🤝 社区参与：Participate、GitHub
- 📄 页脚链接：Acknowledgements、Legal、Privacy、Terms
- ©️ 版权 © 2026 Meta Platforms, Inc.
- 🦋 提供 Bluesky 链接

---

### [](https://seldo.com/posts/nobody-pays-for-open-source-we-can-force-them-to/)

**原文标题**: [Nobody pays for open source. We can force them to. | Seldo.com](https://seldo.com/posts/nobody-pays-for-open-source-we-can-force-them-to/)

开源生态的稳定均衡让免费代码赢得使用、闭源软件赢得利润，但关键维护者长期无偿承担风险。作者主张由 npm、PyPI、Docker Hub 等注册表向大型企业收取“供应费”，再按依赖树比例自动把版税分给维护者：不改许可证、不靠慈善或强制，而是把企业已经在付的供应链账单导向真正创造价值的人。

- 🌍 开源与闭源可类比进化博弈中的“鸽子与鹰”：开源合作赢得代码和使用，闭源竞争赢得利润，稳定结果是两者共存。
- 🏆 自由许可如 MIT、BSD、Apache 是代码游戏的进化稳定策略；试图在许可证层收费的项目，通常会被更开放的分叉击败。
- 📉 React、Elasticsearch、Terraform、Redis 等限制许可的尝试都失败或回退，说明“靠许可证收钱”难以对抗分叉与市场结构。
- 😥 约 60% 开源维护者没有报酬，近 60% 想过或已经退出；极少数人支撑大量关键代码，替代开源的估算成本高达 8.8 万亿美元。
- 🚨 xz 后门事件暴露了风险：无偿维护者被社工攻击，而关键基础设施却依赖少数倦怠个人。
- ⚖️ 系统不是“正在崩溃”，而是稳定在可接受的人力代价上；真正变化的是软件重要性和安全漏洞利用的速度。
- 💸 打赏、基金会、企业捐赠、付费安全、政府基金、Mozilla 模式、改许可证等都已尝试，但多为自愿、慈善或局部，无法改变均衡。
- 🏢 企业其实已为开源支付大量费用，只是付给 JFrog、Snyk、Docker、Chainguard、Sonatype 等供应链、镜像和安全供应商，而非维护者。
- 🛡️ 这些公司卖的是“可靠供应自由代码”：缓存、扫描、签名、漏洞响应，本质是对维护者风险的保险，却在错误层级收费。
- 🎮 存在两个游戏：代码游戏由免费获胜；供应游戏由默认基础设施获胜，而默认可以收费，Docker 就是例证。
- 🧱 注册表是代码变成供应的关键交汇点，不能像许可证那样被复制绕过；企业宁愿付费，也不愿自己维护镜像。
- ❌ 注册表层过去的尝试均失败：npm 终端广告被禁、npm fund 只是链接、Flossbank 因选择加入而亡、Ruby Together 依赖单一赞助商。
- 🐳 Docker 证明非自愿的供应收费可行：对企业收费、对个人和开源免费，收入大幅增长，用户也未大规模逃离。
- 🧾 提议一：注册表计量大型企业使用并收费；个人、小团队、学生和开源项目免费，大公司支付类似现有供应链工具的订阅费。
- 💰 提议二：固定比例收入作为版税，按付费客户依赖树自动、按月、按比例分配给所有相关包，不经过基金会或申请流程。
- 🏗️ 提议三：由拥有域名的注册表执行；它们已有账户、计费和付款路径，技术管道不是主要障碍。
- 🤔 质疑回应：公司不会都转向免费镜像，因为付费是为省事；这不同于 Tidelift 的独立采购，而是附加在既有账单上的条目；欺诈可用依赖树加权缓解。
- 🧬 该方案不要求改变均衡：许可不变、免费仍赢代码、不是慈善也非强制，还能支付长尾维护者，奖励“有用”而非“会募资”。
- 🤖 LLM 与 AI 代理使问题更紧迫：写软件更便宜、软件更多、AI 大规模消耗注册表；RubyGems 遭代理冲击，curl 悬赏被 AI 垃圾淹没，修复负担仍落在无偿维护者身上。
- ✊ 结论：开源开发者已有协调拒绝的力量，曾迫使 Facebook、Redis 等改变；新规范应是“运行计量的人，付钱给让计量有价值的人”，向少数供应者发指令，而非继续向大量消费者呼吁。

---

### [](https://evanhahn.com/posts/2026-09-13-programmers-dislike-reduce/)

**原文标题**: [Anecdotally, programmers dislike "reduce"](https://evanhahn.com/posts/2026-09-13-programmers-dislike-reduce/)

作者埃文·哈恩（Evan Hahn）根据个人经验观察到，程序员普遍喜欢 `map` 和 `filter`，却不太喜欢 `reduce`；提交包含 `reduce` 的代码时更容易收到“难读”的评论，而 `reduce` 的使用频率也明显低于 `map`、`filter`、`some` 等函数。作者提出了一些可能原因，并认为也可能只是自己的错觉或趋势并不真实。

- 🧑‍💻 作者是 Evan Hahn，文章发布于 2026 年 9 月 13 日，标签为软件开发与文化。
- 👍 从经验看，人们喜欢 `map` 和 `filter`，代码审查中很少因此被批评。
- 👎 但人们不喜欢 `reduce`，包含它的补丁常被评论“这部分很难读”。
- 📉 `reduce` 的出现频率远低于 `map`、`filter`、`some` 等函数。
- 🤔 作者猜测原因包括：`reduce` 更难读、更不熟悉、性能可能更差。
- 🧩 在 JavaScript、Python、Swift 等语言中，`reduce` 可能不够优雅；但作者做 Clojure 开发时没有收到这类反馈。
- ❓ 作者也承认自己可能是错的，看到的可能并非真实趋势。
- 🔁 他通常会把 `reduce` 改成别的写法，然后继续工作，并不太在意。
- 🕰️ 最近这种现象变少了，可能是因为代码审查不如以前细致。
- 💬 作者最后询问读者：你是否也注意到这一点？你喜欢 `reduce` 吗？

---

### [SnapDOM：浏览器捕获引擎](https://snapdom.dev/)

**原文标题**: [SnapDOM: Browser Capture Engine](https://snapdom.dev/)

SnapDOM 是一个零依赖的浏览器捕获引擎，可把网页 UI 的结构、样式与资源捕获为图像，并从同一次捕获导出图片、Canvas、HTML、PDF、矢量、GIF/视频等多种结果；核心 MIT 许可，插件按需加载。

- 📸 **核心能力**：捕获 UI 为图像，支持导出图片与 Canvas，并可复用同一次捕获。
- 🧩 **插件扩展**：插件可生成自包含 HTML、面向 Agent 的上下文、PDF 和录制内容。
- ⚡ **安装使用**：支持 `npm i @zumer/snapdom@latest`，也可通过 unpkg 引入脚本；当前 v3.x，月下载量 1m+，MIT 许可。
- 🎯 **捕获细节**：可捕获 Web 字体、伪元素、SVG、背景、开放 Shadow DOM 以及表单控件当前状态。
- 🔁 **快速重复捕获**：V3 复用资源与未变化捕获，按需导出；变化元素会重新捕获。
- 🖼️ **一次捕获，多种导出**：支持 PNG、JPG、WebP、SVG、Canvas、Blob，Canvas 可作为 WebGL 纹理。
- 🤖 **HTML 与 Agent 上下文**：插件可导出文本或 JSON 大纲，以及带交互元素映射的截图。
- 🎞️ **GIF 与视频**：录制插件逐帧捕获实时元素，适合动画、交互演示与短片。
- 🛠️ **适用场景**：产品仪表盘导出图表/KPI 卡片，图形用 Canvas 纹理，Agent 获取页面上下文，测试创建视觉基线。
- 📚 **文档与示例**：提供安装、API、选项、框架指南、配方、对比文档，以及 21 个实时演示。
- 💎 **SnapDOM Pro**：支持可搜索 PDF、可编辑矢量，为 PDF 添加文本层与分页，或导出 SVG/Figma 可编辑形状与文本。
- 🏷️ **发布优惠**：PDF 与 Vector 插件首年 5 折，个人 $19.50、商业 $49.50；之后 $39/$99 每年；前 30 名购买，截止 2026 年 9 月 29 日或售罄。
- ⭐ **行动入口**：可开始使用、探索实时演示，并在 GitHub 上 Star。

---

### [](https://github.com/niklasvh/html2canvas)

**原文标题**: [GitHub - niklasvh/html2canvas: Screenshots with JavaScript · GitHub](https://github.com/niklasvh/html2canvas)

html2canvas 是一个 JavaScript HTML 渲染器，可在浏览器端对网页或页面局部进行“截图”；它基于 DOM 和元素样式构建 canvas 图像，而非真实截图，因此可能与实际显示不完全一致。项目仍处于实验阶段，不建议用于生产环境。

- 📸 核心功能：允许直接在用户浏览器中截取网页或部分网页的“屏幕截图”。
- 🧱 实现原理：读取 DOM 及元素应用的不同样式，将当前页面渲染为 canvas 图像。
- 🌐 运行方式：整个图像在客户端浏览器生成，不需要服务端渲染；不适合在 Node.js 中使用。
- 🔐 跨域限制：不能绕过浏览器内容策略，渲染跨域内容需要代理以使其同源。
- ⚠️ 项目状态：仍非常实验性，未来可能有重大变更，不建议用于生产或直接基于它构建应用。
- 🧩 CSS 支持：每种 CSS 属性都需手动实现支持，因此仍有许多属性不受支持。
- ✅ 浏览器兼容：在 Promise polyfill 下支持 Firefox 3.5+、Google Chrome、Opera 12+、IE9+、Safari 6+。
- 🧪 Promise 依赖：库使用 Promise 并期望全局可用；旧浏览器需先引入 es6-promise 等 polyfill。
- 🖥️ 基本用法：调用 `html2canvas(element[, options]);`，返回包含 `<canvas>` 的 Promise。
- ➕ 结果处理：可通过 `then` 添加回调，例如 `html2canvas(document.body).then(function(canvas) { document.body.appendChild(canvas); });`。
- 🛠️ 构建方式：可下载现成构建包，或克隆仓库后执行 `npm install` 和 `npm run build`。
- 📚 示例资源：更多信息和示例可访问 homepage 或 test console。
- 🤝 贡献方式：PR 应提交到 develop 分支；提交前需在所有支持浏览器中测试，并为不支持或不完整的 CSS 属性添加测试。
- ⭐ 项目热度：约 31.9k stars、4.9k forks、976 issues、78 pull requests、1,066 commits。
- 📄 许可证：MIT license。

---

### [](https://github.com/zumerlab/snapdom/releases/tag/v3.0.0)

**原文标题**: [Release v3.0.0 · zumerlab/snapdom · GitHub](https://github.com/zumerlab/snapdom/releases/tag/v3.0.0)

SnapDOM v3.0.0 于 2026 年 9 月 14 日发布，是 v3 首个稳定版本；核心库与官方插件统一到 v3 发布线，带来自动捕获复用、增量重捕获、自动字体嵌入和新捕获 API，并包含破坏性变更、布局/字体/Canvas/Shadow DOM 修复、插件与文档更新。升级 v2 用户需查阅迁移指南，v2 源码和文档仍可用。

- 🚀 自动复用符合条件的未变更捕获，并为安全的本地变更重建受影响子树。
- 🧩 新增按捕获会话隔离并发捕获、`fromString()` 捕获 HTML 字符串、`preCapture()` 在悬停/焦点时准备捕获。
- 🔤 自动嵌入被捕获内容使用的 Web 字体。
- ⚙️ SVG 引擎仍为默认；原生 `html-in-canvas` 引擎仍为实验性，需要自定义构建。
- ⚠️ 破坏性变更：`width`/`height` 优先于 `scale`；字体嵌入自动启用；移除 `preCache`，不再支持过时捕获选项。
- 🔐 核心脱敏仅限密码字段；`afterExport` 钩子只观察结果，不再链式使用返回值。
- 🧱 修复伪元素盒、滚动容器、图片对齐，以及变换元素协调与离屏捕获。
- 📐 修复分数宽度导致意外换行，保留 wrapper 高度和块化 span 的作者指定宽度。
- 👁️ 对齐浏览器 `visibility`/`content-visibility` 行为，测量文本截断时不替换实时文本节点，中和捕获根上的 CSS `zoom`。
- 🎨 保留 SVG `<use>` 图标继承填充色，以及图标字形字体样式（含斜体）和自定义 `@font-face` 规则。
- 🖼️ Canvas/兼容性：限制 canvas 帧等待、空 canvas 警告、WebGL 保留 `toDataURL()` 前帧；修复 Shadow DOM slot、跨窗口/iframe 类型检查和 legacy bundle 全局泄漏。
- 🔌 插件与导出：官方插件对齐 v3，向插件暴露捕获几何、精确导出选项和 canvas 裁剪；color-tint 插件支持其他窗口/iframe 的 clone roots。
- 📚 文档：更新包引用、版本标签、插件展示、钩子契约、服务端捕获与 DOM 捕获边界指南，并重写 `llms.txt`/`llms-full.txt`。
- 🧪 测试维护：扩展回归覆盖，视觉套件拆分为 6 个分片，改进网络依赖测试调度，等待 iframe 样式表、导入字体和图片解码，固定 DPR 测试。
- 🛠️ `npm run build` 不再自动推送 changelog；完整变更见 `v2.23.1...v3.0.0`。

---

### [](https://www.tigerdata.com/go/trial?utm_source=content-syndication&utm_medium=referral&utm_campaign=javascript-weekly-newsletter)

**原文标题**: [Postgres for time-series workloads at any scale. | Tiger Data](https://www.tigerdata.com/go/trial?utm_source=content-syndication&utm_medium=referral&utm_campaign=javascript-weekly-newsletter)

Tiger Data（Timescale）提供面向任意规模时序工作负载的 Postgres 云服务，主打超大规模、弹性独立扩缩、企业级合规、深度可观测性与快速部署。

- 🚀 单个 Tiger Cloud 服务可达每天 3 万亿指标、3 PB 数据、1 千万亿数据点。
- 🎁 注册即获 1000 美元信用额度，30 天有效；无需信用卡，仅限新账户。
- 🏭 受 IoT 领域数千家公司信赖。
- ⚖️ 复制集最多 10 节点，支持读写分离，以及 SSD/S3 分层存储，实现近乎无限且高性价比的存储。
- 💸 计算与存储解耦，可分别扩缩，避免为闲置容量付费并优化性能。
- 🛡️ 多可用区集群，支持自动故障转移、时间点恢复和跨区域备份，保障高可用。
- 🔐 企业级能力：SOC 2、HIPAA、GDPR 合规，始终加密、SSO、RBAC 和审计日志。
- 🔍 深度可观测性：查询下钻和仪表板，指标可发送至 CloudWatch、Datadog、Prometheus。
- ⚡ 数分钟内可完成数据库配置，并支持 SQL、CLI、Terraform、Cursor 或 Claude Code 管理。
- ☁️ 可集成首选云厂商及更广泛的 Postgres 生态。
- 🏢 企业就绪：合同化 SLA、区域数据隔离、企业合规认证，以及 24/7 全球 Postgres 专家支持。
- ©️ 版权归属 2026 Timescale, Inc., d/b/a Tiger Data，保留所有权利。

---

### [](https://docs.fallow.tools/)

**原文标题**: [fallow: codebase intelligence for TypeScript and JavaScript](https://docs.fallow.tools/)

Fallow 是面向 TypeScript 和 JavaScript 的代码库智能工具，提供免费的静态代码与样式分析，可检测未使用代码、重复、复杂度、架构漂移和设计系统一致性问题，并可选配运行时智能以了解生产环境中实际执行情况。

- 🚀 **快速上手**：无需安装，直接运行 `npx fallow` 即可，首次使用无需配置
- 🔍 **静态分析能力**：一次运行即可发现死代码、重复代码、复杂度和样式问题
- 🗑️ **删除冷代码**：放心移除未使用的文件、导出和依赖
- ♻️ **减少重复**：在重复逻辑扩散前将其找出
- 🎯 **优先重构**：利用复杂度和健康度分析聚焦清理工作
- 🧾 **TypeScript 证据**：确认具体符号使用、类契约、受影响文件和针对性测试
- ⏱️ **运行时证据**：查看热路径、冷路径以及基于运行时的删除依据
- 💻 **CLI 工作流**：最佳起点，可在本地、CI 和代理循环中使用
- 🧩 **VS Code 集成**：编辑器内实时诊断、Code Lens 和一键修复
- 🤖 **MCP 与代理**：为 Claude Code、Cursor 等代理提供结构化工具调用
- 🧠 **双层模型**：静态分析回答“什么和什么相连”，运行时智能回答“实际运行了什么”，二者在 `fallow health` 中交汇
- 📚 **常用页面**：快速开始、配置、CI 集成、CLI 参考

---

### [](https://github.com/fallow-rs/fallow)

**原文标题**: [GitHub - fallow-rs/fallow: Codebase intelligence for TypeScript and JavaScript. Free static analysis of code and styles: unused code, duplication, circular deps, complexity hotspots, architecture boundaries, design-system drift. Optional paid runtime layer (Fallow Runtime): hot-path review and cold-path deletion evidence from real production traffic. · GitHub](https://github.com/fallow-rs/fallow)

Fallow 是面向 TypeScript 与 JavaScript 的代码库智能工具，以 Rust 单二进制提供静态分析，覆盖死代码、循环依赖、重复、复杂度、架构边界和样式漂移，并可选付费运行时证据；强调确定性、类型化 JSON、无 AI、无需 Node.js 或 TS 编译器，适合本地、CI 与智能体。
- 🦀 核心：Rust 单二进制运行，静态分析无需 Node.js 或 TypeScript 编译器，分析器内不内置 AI。
- 🧹 检测未使用文件、导出、类型、枚举/类成员、依赖，以及循环依赖和重复代码。
- 📈 提供复杂度热点、0–100 健康分与等级、架构边界违规、设计系统样式漂移。
- 🚦 `fallow audit` 做变更文件 PR 门禁，只对本次变更引入的问题给出 pass/warn/fail，旧问题可用 baseline 隔离。
- 💰 Fallow Runtime 是可选付费层，将生产执行证据合并到 health/audit；单次本地覆盖免费，持续或云端监控需许可。
- ⚡ 快速开始：`npx fallow` 全流程，`npx fallow audit` PR 门禁，`npm install --save-dev fallow`；`--format json --quiet` 提供机器契约。
- 🧾 退出码：0/1 都表示运行成功（1 有发现），2 是真实错误；JSON 输出含 kind、actions、auto_fixable、next_steps 等类型化字段。
- 🔍 支持 `--type-aware` 可选 TypeScript 语义证据，用于精确符号使用、跨文件类型泄漏、目标测试与公共签名耦合，但不替代 `tsc --noEmit` 或 Oxlint。
- ⚙️ 配置优先级为 `.fallowrc.json` > `.fallowrc.jsonc` > `fallow.toml` > `.fallow.toml`；`fallow recommend` 可检测技术栈并生成建议配置。
- 🛠️ 命令覆盖 dead-code、dupes、similar-code、health、fix、guard、security、explain、doctor、init、migrate、viz、schema 等。
- 📤 输出格式包括 human、json、sarif、compact、markdown、codeclimate、GitHub annotations、PR 评论和健康徽章。
- 🤖 为智能体设计：MCP 服务器、版本匹配 agent skill、`fallow agent install` 可接入 Claude Code/Codex/Cursor，并提供只读 Code Mode。
- 🧪 CI 支持 GitHub Action `fallow-rs/fallow@v3` 与 GitLab 模板；Action 默认阻塞，可设 `fail-on-issues: false` 或 `command: audit` 分阶段采用。
- 🔌 编辑器集成包括 VS Code、Zed/Neovim、`fallow-lsp`，Node API 导出 detectDeadCode 等函数。
- 🚫 可用 `fallow-ignore-next-line`、`fallow-ignore-file`、JSDoc 标签和 baseline 抑制或隔离发现。
- 🏁 性能示例：fastify 64ms vs knip 205ms，preact 74ms vs 2.01s（27.1x）；但 knip 在 astro/TS 和 jscpd 原始重复扫描上更快。
- 📚 文档在 docs.fallow.tools，项目 MIT 许可，仓库约 4.5k stars、160 forks、3,843 commits。

---

### [](https://mattstromawn.com/writing/the-least-wrong-colors-version-2/)

**原文标题**: [ The least wrong colors, version 2 || Matt StrÃ¶m-Awn, designer-leader](https://mattstromawn.com/writing/the-least-wrong-colors-version-2/)

四年前作者提出，挑选分类调色板是一个优化问题：不存在“正确”颜色，只有借助合适成本函数和爬山法得到“最不错误”的颜色。第二版更新了算法，发布 npm 包与可视化 UI，新增模块化评估器、更多控制、公共 API 和 CLI，并改进退火算法、色彩空间与距离度量，结果优于其他生成工具和行业标准调色板。

- 🎯 核心观点：分类配色没有唯一正确答案，而是通过成本函数和优化算法逼近“最不错误”的方案。
- 🚀 第二版发布：更新算法，提供 npm 包和更易用的 GUI；AI 编码助手帮助改进代码并验证原有假设。
- 🧩 新增评估器：包括 JND、Avoid、Contrast、Saliency、Name difference，均可加权，且支持自定义插件式评估器。
- 🎛️ 更多控制：颜色可固定位置或顺序，单个色彩通道也可锁定，便于加载并部分优化已有调色板。
- 📦 公共 API 与 CLI：支持完整配置、加载颜色优化，输出原始颜色值、CSS 属性或 DTCG JSON，并新增 reportJndIssues 端点。
- 🔥 退火算法改进：根据随机初始样本选择起始温度，变异幅度随优化进程缩放，可限制迭代次数，性能大幅提升。
- 🌈 可配置色彩空间与距离度量：默认使用 okhsl 和 CIEDE2000，从 chroma.js 迁移到 culori，支持自由组合。
- 📊 结果优势：category-colors 相比其他生成工具和行业标准调色板，在 ΔE 最小值、色盲最差情况、名称差异和均匀性等指标上表现更优，高基数时尤其明显。
- 🖥️ 新 UI：可直接生成和优化调色板，是初版文章发布以来用户最期待的功能，虽然实现上“过度工程化”。
- 🙏 研究致谢：基于 CIEDE2000、色盲模拟、JND、颜色命名模型等研究，并参考 Okabe–Ito、ColorBrewer、Palettailor、Colorgorical、QualPal、culori 等前人工作。

---

### [](https://mattstromawn.com/writing/how-to-pick-the-least-wrong-colors/)

**原文标题**: [ How to pick the least wrong colors || Matt StrÃ¶m-Awn, designer-leader](https://mattstromawn.com/writing/how-to-pick-the-least-wrong-colors/)

文章讲述一位自学设计师为解决数据可视化中的分类配色问题，从零学习颜色理论，并用模拟退火算法在“好看、适用广、无障碍”等冲突目标中寻找较优解的过程。

- 🎨 问题：为 Stripe 仪表板的分类数据挑选配色，需好看且贴近品牌、覆盖大量类别、满足 WCAG 3:1 对比度。
- 📊 现有方案：Viridis、ColorBrewer、Colorgorical、Adobe/IBM 设计系统等，但各有取舍，无法同时满足需求。
- 🧠 突破点：作者受“模拟退火”视频启发，发现它适合解空间巨大、多目标冲突、允许近似解的问题。
- 🔥 模拟退火：先随机扰动数据，按评分保留或回退；初期偶尔接受更差解以跳出局部最优，随后逐渐“冷却”，倾向更优解。
- 📐 评分核心：需要把“好看、适用广、无障碍”转为可计算的损失函数。
- 👀 好看：用 CIE ΔE* 测量与人工选定“好看”配色的感知距离，越小越好。
- 🌈 适用广：颜色彼此差异要大（平均距离最大化），且差异要均匀（距离范围最小化）。
- ♿ 无障碍：模拟不同色盲类型，计算色盲视角下的颜色差异；WCAG 对比度也可用边框辅助满足。
- ⚖️ 损失函数：将好看、适用性、三类色盲得分加权相加，权重可调；损失越低越好。
- 💻 运行结果：2016 MacBook 约 3 秒，评估约 16,000 个配色；随机配色损失 217.8 降至 136.3，约提升 38%。
- ✅ 效果：优化后色相/明度更分散，色盲模拟下多数颜色仍可区分；但并非完美，仍需真实用户测试。
- 🧪 压力测试：与 Adobe、IBM、d3 的 12 色方案比，作者算法在 JND 问题上总数更少（7 vs 14/21/29）。
- 🎛️ 可“艺术指导”：以品牌色或流行调色板为目标，可生成既接近目标又经过优化的配色。
- 🧭 结论：颜色很复杂，没有唯一最佳，只有“最不坏”；模拟退火可高效搜索可接受方案，作者也开放了源码。

---

### [GitHub - ilikescience/类别颜色 · GitHub](https://github.com/ilikescience/category-colors)

**原文标题**: [GitHub - ilikescience/category-colors · GitHub](https://github.com/ilikescience/category-colors)

category-colors 是一个用于分类数据可视化的调色板生成库，将调色板设计视为多目标优化问题，通过模拟退火在可区分性、色盲友好、对比度、协调性等冲突目标之间寻找最小错误折中。它提供 API、CLI、评估器和配置，可生成并审计分类颜色，但结果仍需用真实读者测试。

- 🎯 项目目的：让分类调色板中每对颜色可区分、对色盲可区分、满足对比度，并看起来协调；这些目标相互冲突。
- 🔬 核心方法：把调色板设计当作优化问题，加权你关心的目标，用模拟退火搜索“最少错误”的折中方案。
- 📝 背景：这是文章《How to pick the least wrong colors》背后的代码；色盲模拟已从 1997 年模型改为 Machado 等 2009 年模型，通过 culori 实现。
- ⚠️ 重要提醒：评估器只测量可计算指标，不衡量人们是否喜欢或颜色是否适合标签；结果是起点，不是完成品。
- 📦 安装：`npm install category-colors`；需要 Node.js 22.12+，包为 ESM，CommonJS 调用者也可用。
- 🚀 快速开始：使用 `createDefaultConfig`、`createDefaultState`、`prepareInitialState`、`runWithOrderOptimization` 生成调色板。
- 💻 命令行：`npx category-colors run` 生成，`report` 审计现有调色板；支持配置、状态、格式、输出、跳过排序等选项。
- 🧩 入口点：主入口浏览器安全；`report`、`evaluators`、`evaluators/saliency`、`evaluators/names`、`cli` 等为独立子路径。
- 📉 包体积：包无副作用；`saliency` 带约 150 kB 查找表，`names` 约 260 kB，按需导入可被 tree-shake。
- ⚙️ 优化 API：包括 `prepareInitialState`、`runSimulatedAnnealing`、`runWithOrderOptimization`、`cost`、`costBreakdown`、`simulateCvd`。
- 🎛️ 配置：`evalFunctions` 是 `{ function, weight, ...options }` 数组；权重相对归一化，同一评估器可用不同设置多次出现。
- 👁️ 色觉权衡：默认含 protanopia、deuteranopia、tritanopia、grayscale 的 JND 项；权重看似低但会饱和，最差颜色对受 grayscale 约束。
- 🎨 颜色距离与空间：`config.colorDistance` 选择距离方法和空间；`config.colorSpace` 控制工作空间与通道范围，支持 okhsl、oklab、rgb 等。
- 🔒 通道锁定：用 `lockedChannels` 保留部分通道（如品牌色相），`fixedColor` 完全固定颜色，`fixedOrder` 在排序优化中固定位置。
- ⚖️ WCAG 对比度：`contrast` 评估器对低于要求比率的颜色施加指数惩罚，可设置背景、比率、是否检查相邻色。
- 🚫 避免颜色：`avoid` 评估器将调色板推离指定颜色（背景、品牌色、语义色），按侵入半径线性惩罚。
- 🏷️ 名称差异与显著性：`names` 评估器用 Heer & Stone 模型计算名称相似度；`saliency` 返回 1-平均显著性，拉向典型可命名颜色。
- 🛠️ 自定义评估器：函数签名 `(state, config, descriptor)` 返回成本；从描述符读参数；硬性要求适合用指数惩罚。
- 📊 JND 报告：`reportJndIssues` 审计颜色对是否低于可察觉差异阈值；支持 CVD 模拟、阈值、距离方法；可排除 `pairs` 减小体积。
- 🧪 开发：`npm test` 使用 Node 内置测试运行器，无 dev 依赖；测试子路径解析和主入口不引入 Node 内置模块。
- 📚 致谢：基于 CIEDE2000、Machado 等 CVD 模拟、Stone 等 JND、Heer & Stone 颜色命名模型；MIT 许可。

---

### [类别颜色](https://categorycolors.com/)

**原文标题**: [Category Colors](https://categorycolors.com/)

概述：当前未检测到可总结的正文内容，请补充文本后再进行摘要。

- 📄 你发送的消息中“Use the following content:”后面没有附上任何文章或文本。
- ✍️ 请把需要总结的内容粘贴过来。
- ✅ 收到内容后，我会用中文输出“概述 + 表情符号要点列表”的摘要。

---

### [](https://github.com/react/react/blob/main/packages/react-devtools/CHANGELOG.md#800)

**原文标题**: [react/packages/react-devtools/CHANGELOG.md at main · react/react · GitHub](https://github.com/react/react/blob/main/packages/react-devtools/CHANGELOG.md#800)

React DevTools 更新日志记录了从 8.0.0 到 4.0.0 的持续演进：新版聚焦 Suspense 默认支持、Timeline 移除与 Elements 面板集成；7.x/6.x 强化 Server Components 和挂起诊断；5.x/4.x 完善 Hooks、Profiler、组件树、搜索与性能体验，并伴随大量兼容性和稳定性修复。

- 🧭 8.0.0（2026-09-08）：Suspense 标签页默认开启，可直接查看组件挂起原因。
- 🗑️ 8.0.0：移除 Timeline profiler 标签页，建议改用浏览器 Performance 面板中的 React 轨道进行性能分析。
- 🧩 8.0.0：浏览器 Elements 面板可显示匹配的 React 组件，并新增 React Element 面板。
- 🔎 8.0.0：组件搜索结果可直接导航；Profiler 提交视图支持组件搜索、父级堆栈和忽略列表堆栈帧展开。
- ⚙️ 8.0.0：支持自定义 DevTools 客户端连接主机/端口/路径、sandbox CSP 最小支持、在 React 检测前创建扩展面板，以及过滤变更时更新检查元素。
- 🛠️ 8.0.0：大量修复，包括 fallback Fiber 协调、HOC 名称提取、重连消息缓冲、预渲染时不连接、错误注入防护、内存泄漏和 Profiler 提交树问题。
- 🌀 7.0.0/7.0.1（2025-10）：新增“suspended by”区域，展示 Server Components await、React.lazy、use()、Suspense 图片/CSS/字体等挂起原因；增加 Chrome Sources 代码编辑侧栏和外部编辑器打开本地文件。
- 🖥️ 7.0.0：支持流式渲染完成前检查 React 树、dehydrated roots 挂载、Suspense/Activity 的 name prop、Thenables 一等支持、Errors props 内省、Owner Stacks 与 Index Source Maps 符号化。
- 🧪 6.0.0（2024-09）：重点支持 Server Components 树、环境名称过滤、函数即点即跳转，并修复 Profiler 崩溃、扩展 API、路径处理等。
- 🪝 5.x（2024）：加入 Forget 徽章、useFormStatus/useTransition/useOptimistic 等 Hook 支持、源码符号化、自定义后端协议、Firefox Manifest v3，以及大量扩展/控制台/主题修复。
- 🚀 4.x（2019-2022）：4.0.0 大幅降低性能开销，引入组件栈、组件过滤、rendered by/owners tree、新版 hooks 检查、行内搜索、HOC 徽章、Suspense 开关，以及 Profiler 的 reload-and-profile、导入/导出和“Why did this render?”。
- 🧱 4.x 后续：持续完善 Bridge 协议检查、Profiler 快照/时间线、React Native 高亮、StrictMode 日志、DevTools UI 与编辑体验，并修复大量边界问题。

---

### [React 开发者工具 - Chrome 网上应用店](https://chromewebstore.google.com/detail/react-developer-tools/fmkadmapgofadopljbjfkapdkoienihi)

**原文标题**: [React Developer Tools - Chrome Web Store](https://chromewebstore.google.com/detail/react-developer-tools/fmkadmapgofadopljbjfkapdkoienihi)

React Developer Tools 是一款由 Meta 提供的 Chrome DevTools 扩展，用于调试开源 React 应用。它在开发者工具中新增 Components 和 Profiler 两个面板，当前评分 3.9，约 500 万用户，完全开源，并声明不收集或使用用户数据。
- 🧩 在 Chrome DevTools 中添加“Components ⚛”和“Profiler ⚛”两个标签页。
- 🌳 Components 标签显示页面渲染的 React 根组件及其子组件层级树。
- ✏️ 可选中组件并查看、编辑其当前 props 和 state；面包屑可追溯创建它的父级组件链。
- 🔄 在 Elements 标签检查 React 元素后切换到 React 标签，会自动在组件树中选中对应元素。
- ⏱️ Profiler 标签用于记录性能信息，帮助分析 React 应用性能。
- 🔐 需要权限访问页面 React 树，但不会远程传输数据；完全开源，源码位于 GitHub。
- ⭐ 评分 3.9/5，基于 1.6K 条评分；评分每日更新，可能不反映最新评论。
- 👥 约 5,000,000 用户；扩展分类为开发者工具。
- 🧾 版本 8.0.0，更新于 2026 年 9 月 11 日，大小 655KiB，语言为英语，提供者为 Meta Platforms, INC.。
- 🛡️ 开发者声明：数据不会出售给第三方，不会用于与核心功能无关的目的，也不会用于信用评估或贷款用途。
- 🏢 支持通过 Chrome Enterprise Core 管理扩展并了解组织内使用情况。
- 🔗 相关扩展包括 Vue.js devtools、Angular DevTools、Redux DevTools、MobX Developer Tools、React Context DevTool、JSON Formatter、GraphQL Network Inspector、LocatorJS 等。

---

### [Zod 4.6](https://zod.dev/blog/zod-4-6)

**原文标题**: [Zod 4.6](https://zod.dev/blog/zod-4-6)

Zod 4.6 已发布，重点提升校验性能与内存表现，新增 IBAN、实例属性校验、外部 parser、塔吉克语 locale 等能力，并扩展 JSON Schema 支持；同时包含多项需注意的行为变更。

- 🚀 升级方式：`npm install zod@latest`；本次发布汇总 72 个提交。
- ✅ 新增 `.validate()` / `.validateAsync()`：只返回布尔值、不构造 `ZodError`，可短路报错；配合 `z.compile()` 对无效输入最高比 `.safeParse().success` 快 35 倍。
- 🧩 Zod Classic schema 也有 `.validate()`，校验成功时可对输入类型进行收窄。
- 🏛️ `z.instanceof().properties()` 可原地校验实例属性，保留原型和方法，不像 `z.object()` 会返回普通对象。
- 📜 `z.fromJSONSchema()` 新增支持 6 个关键字：`minProperties`/`maxProperties`、`uniqueItems`、`contains`、`minContains`/`maxContains`。
- 🏦 新增 `z.iban()`：校验电子格式 IBAN，并检查 ISO 7064 MOD 97-10 校验和。
- 🌍 4.6.1 新增塔吉克语 locale：`z.locales.tg()`。
- 🔌 新增 `z.withParser()`：可安装外部生成的 parser，适用于禁用 `new Function` 的严格 CSP 环境。
- 📦 CommonJS 性能提升：移除导出 getter，`require` 下编译 schema 的 `z.validate()` 约快 3 倍。
- 🔗 `z.url()` 拒绝性能提升：4.6.4 使用 `URL.canParse()`，无效输入约 86ns，而此前约 4.6µs；带 hostname/protocol/normalize 时使用 `URL.parse()`。
- 🧠 修复递归 schema 内存保留：释放已解析输入，29k 节点树保留 2.2MB 而非 10.1MB；递归解析约慢 6%。
- 📦 `@zod/mini` 成为独立包，自 4.5 起与 `zod` 同步版本发布。
- ⚠️ `safeParse()` 惰性构建错误：error maps 在首次读取 `result.error` 时运行，期间切换 `z.config()` 会使用新配置；未读取错误时，带副作用的 error map 不会运行。
- 😀 `z.emoji()` 拒绝仅由 Emoji_Component 组成的字符串，如 `"123"`、`"#"`、`"*"`、单独 ZWJ/变体选择符/肤色修饰符；需至少一个 pictograph、区域指示符或 keycap。
- 🔢 数值 TypeScript enum 的 `.options` 不再包含反向映射值。
- 🔐 `z.base64()` / `z.base64url()` 运行时正则改为线性，避免超大输入导致正则栈溢出；`z.toJSONSchema()` 输出保持不变。
- 📧 `z.email()` 正则移除 lookahead，有效地址约快 2 倍；`z.regexes.email` 无捕获组，`issue.pattern` 与 JSON Schema pattern 也变化，模板字面量组合行为有变。
- 🧮 JSON Schema 链式检查改为合取折叠，不再互相覆盖边界；例如 `z.number().min(0).max(23).int()` 正确输出 `minimum: 0, maximum: 23`。
- 🏷️ 8 个元数据成员（`format`、`minLength`、`maxLength`、`minValue`、`maxValue`、`isInt`、`minDate`、`maxDate`）改为首次读取时物化；初始 `Object.keys()` 更少，读取后会新增属性。

---

### [Javet 6.0.0 文档](https://www.caoccao.com/Javet/)

**原文标题**: [Javet 6.0.0 documentation](https://www.caoccao.com/Javet/)

overview summary
- 🚀 Javet 是 Java + V8（JAVa + V + EighT）的缩写，目标是在 Java 中嵌入 Node.js 和 V8。
- 👨‍💻 作者鼓励 Star 项目，可关注 @sjtucaocao、访问博客，并加入 Discord 官方支持频道；也欢迎捐赠支持。
- ⚙️ 主要特性：支持 Node.js v26.8.1 + V8 v15.3.76.9，提供 i18n 与 non-i18n 版本，可在 Node.js 和 V8 模式间动态切换。
- 🧩 提供 Javenode 为 V8 模式补齐 Node.js 能力，在 JVM 中暴露 V8 API，并支持 JavaScript 与 Java 互操作、原生 BigInt 和 Date。
- 🏊 支持 Javet 引擎池、Spring 集成，以及通过 Chrome DevTools 进行实时调试。
- 🛠️ 通过 swc4j 支持 AST 分析及 JS/TS/JSX/TSX 转换与转译；JavetBuddy 可增强 JVM 字节码；JavetShell 支持实时交互。
- 💻 平台支持：Android（x86/x86_64/arm/arm64）、Linux（x86_64/arm64）、macOS（x86_64/arm64）、Windows（x86_64）。
- 📦 快速开始：Maven/Gradle 依赖版本为 6.0.0；核心为 com.caoccao.javet:javet，另需按平台引入 Node.js 或 V8 原生包。
- 👋 Hello Javet 示例：Node.js 模式用 V8Host.getNodeInstance().createV8Runtime()，V8 模式用 V8Host.getV8Instance().createV8Runtime()，均可执行字符串。
- 🤝 赞助商包括 HiveMQ、SheetJS、momen.app；许可证为 Apache License 2.0。
- 📚 提供博客文章（如 GraalJS/Javet/Nashorn 性能比较、在 Java 中运行 TypeScript、React + Spring Boot SSR 等）以及教程、API 参考、迁移指南、发布说明、FAQ 和开发构建测试文档。

---

### [](https://rgrove.github.io/parse-xml/)

**原文标题**: [@rgrove/parse-xml - v5.0.0](https://rgrove.github.io/parse-xml/)

@rgrove/parse-xml v5.0.0 是一个面向 Node.js 与浏览器的快速、安全、合规、零依赖 XML 解析器，适合需要非流式、非验证、浏览器友好解析方案的场景。

- 📦 安装方式：使用 `npm install @rgrove/parse-xml`，或在浏览器中通过 Unpkg 加载压缩包并使用全局 `parseXml`。
- 🌳 解析结果：返回 `XmlDocument` 对象树，包含 type、name、attributes、children、parent 等结构，所有对象支持 `toJSON()`，方便转为 JSON。
- ✅ 合规与测试：基本符合 XML 1.0（第五版）非验证解析器规范，并通过 XML Conformance Test Suite 中的相关测试。
- ⚠️ 友好错误：解析失败时提供详细错误信息与上下文，包括 message、line、column、pos、excerpt，并显示出错位置。
- 🚫 非功能限制：能解析 `<!DOCTYPE ...>` 但不加载外部 DTD、不验证文档、不解析 DTD 自定义实体；仅支持 UTF-8 编码。
- 🧩 技术实现：使用 TypeScript 编写，Node.js 编译为 ES2020，浏览器编译为 ES2017，浏览器构建优化压缩，体积极小且零依赖。
- ⚡ 性能表现：小文档基准中最快，约 210,841 ops/s；中大型文档通常慢于原生 libxmljs2，但后者依赖 C、无浏览器支持且有安全漏洞历史。
- 🎯 设计定位：避免原生依赖、非标准宽松解析、臃肿 API、仅流式解析、错误处理差等问题，专注小型、快速、安全、浏览器友好的 XML 解析。
- 📄 许可证：ISC License。

---

### [发布 v5.0.0 · rgrove/parse-xml · GitHub](https://github.com/rgrove/parse-xml/releases/tag/v5.0.0)

**原文标题**: [Release v5.0.0 · rgrove/parse-xml · GitHub](https://github.com/rgrove/parse-xml/releases/tag/v5.0.0)

parse-xml v5.0.0 已发布，API 保持不变，但包格式、最低 Node.js 版本和导出范围有破坏性变更；npm 包体积也明显缩小。

- 🚀 v5.0.0 由 rgrove 发布，包含 1 个提交到 main，为当前最新标签。
- 📦 parse-xml 现在改为 ES 模块，package.json 设置 `"type": "module"`，发布 ESM 而非 CommonJS。
- ✅ 已使用 `import { parseXml } from '@rgrove/parse-xml'` 的项目无需改动。
- ✅ Node.js 22+ 中 `require('@rgrove/parse-xml')` 仍可工作，因为支持 `require(esm)`。
- ⚠️ 无法解析 ESM 的打包器或运行时将不再可用。
- 🧩 若项目是 CommonJS 且使用 TypeScript，需要 TypeScript 5.8+ 和 `"module": "nodenext"`；旧版 TS 或 `"module": "node16"` 会报错。
- 🟢 最低支持 Node.js 版本提升到 22.12.0，原为 14.0.0，且该旧版本已长期未测试。
- 🔒 新增 `exports` 映射，仅允许导入公共 API；`Parser`、`StringScanner`、`syntax`、`types` 不再可导入。
- 🧱 根入口和 `Xml*` 节点类不受影响，例如仍可导入 `parseXml`、`XmlElement` 及 `dist/lib/XmlElement.js`。
- 🌐 `dist/browser.js` 浏览器 bundle 改为 ESM，体积小 1.1 KB；`dist/global.min.js` 全局 bundle 不变，CDN `<script>` 和 `parseXml` 全局用法照旧。
- 📉 npm 包缩小约 40%，打包后 48 KB，低于 4.2.3 的 82 KB，因移除了仅开发时有用的 sourcemaps。
- 🔗 完整变更可查看 `v4.2.3...v5.0.0` changelog。

---

### [GitHub - hulkholden/n64js](https://github.com/hulkholden/n64js)

**原文标题**: [GitHub - hulkholden/n64js: An n64 emulator in JavaScript · GitHub](https://github.com/hulkholden/n64js)

n64js 是 hulkholden 开发的一款以 ES6 JavaScript 为主的 N64 模拟器，许多 ROM 可全帧率运行；项目公开于 GitHub，采用 MIT 许可证，并提供在线版、开发构建、测试、发布与兼容性说明。

- 🎯 项目目标：主要是为了挑战，作者约 25 年断续开发 N64 模拟器，并用 JavaScript 展示现代浏览器的强大能力。
- 🌐 在线体验：托管版位于 https://hulkholden.github.io/n64js/。
- 🧰 开发环境：需安装 Bun；从仓库根目录运行 `bun install`，用 `bun run build` 编译，可加 `--watch`；`build/` 被 Git 忽略，CI 检查 lint 和构建。
- ✅ 代码检查：`bun run lint` / `bun run lint:fix`，覆盖 `src/`、`tools/` 和 ESLint 配置；警告也失败；`eslint-suppressions.json` 记录 `no-unused-vars` 基线。
- 🖥️ 本地运行：根目录执行 `python3 -m http.server`，访问 `http://localhost:8000/`。
- 🎮 无头输入：Bun 脚本可通过 `createHeadlessEmulator` 的 `inputs` 数组设置控制器；`buttons` 为 16 位掩码，`stick_x`/`stick_y` 为有符号 8 位；更新现有对象字段；四个独立中性输入状态，默认仅端口 0 连接。
- 🚀 发布流程：推送 `v*` 标签（如 `v1.2.3`）触发 GitHub Pages 发布；使用固定 Bun 版本安装、构建并部署；普通分支推送不更新站点；需将 Pages 源设为 GitHub Actions，并允许 `v*` 标签部署。
- ✅ 兼容性：截至 2023-09-23，95% `n64-systemtest` 测试通过；失败集中在 64 位内存访问、RDP（因使用 HLE 影响不大）和浮点精度。
- ⚠️ 已知问题：周期计数不精确、图形 HLE 仍有大量 TODO；多数 ROM 可玩但有图形问题；GoldenEye 在 RSP 的 LLE 音频开启时可能挂起。
- 🌐 浏览器要求：保存/加载需原生 `Uint8Array.prototype.toBase64()` 和 `Uint8Array.fromBase64()`，即 Chrome/Edge 140+、Firefox 133+、Safari 18.2+；推荐 Chrome。
- ⚡ 性能：在 Apple M2 Max 上多数 ROM 多数时间全帧率；LLE 音频模拟是最大性能负担。
- 📦 实现状态：CPU 已有 cop0、cop1、TLB 等；RSP 有控制器、静态/可配置键位和 Gamepad API；图形 HLE 中 GBI0 大部分实现，GBI1/2 部分实现，LLE 未实现；音频 HLE 未实现，LLE 已实现；存档支持持久化、导入/导出、Mempack、Eeprom 4k/16k、SRAM、FlashRAM。
- 🧭 待办：修复图形问题、存档导入/导出、即时存档、Gamepad 支持。
- 📜 历史：源自 1999 年左右的 Daedalus；2012 年作者与 @mmalex 打赌用 JavaScript 移植，n64js 由此诞生。
- 📊 仓库数据：公开仓库，MIT 许可证，648 Star、87 Fork、47 Watching、26 Issues、5 Pull Requests，约 1,957 次提交。

---

### [](https://fingerprint.com/webinar/workshop-new-account-fraud/?utm_source=JSWeekly09152026)

**原文标题**: [Live Build: The Device Intelligence Method to Stop New Account Fraud](https://fingerprint.com/webinar/workshop-new-account-fraud/?utm_source=JSWeekly09152026)

这是一场由 Fingerprint 举办的线上 Live Build 工作坊，主题是用设备智能在注册环节识别并阻止同一设备重复创建新账户的欺诈行为，重点防范刷试用额度、推荐奖励和促销优惠的虚假注册。活动时间为 9 月 16 日 9AM PT / 12PM ET，由 Keshia Rose 带领实时编码，并提供实施指导与 Q&A。

- 🛡️ 核心问题：虚假注册刷试用金、推荐奖励和促销，是常见滥用方式；邮箱验证、手机验证、IP 限速都容易被绕过，还会误伤真实用户。
- 📅 活动信息：9 月 16 日，太平洋时间上午 9 点 / 东部时间中午 12 点，线上 Live Build。
- 🎯 解决方案：在注册瞬间识别设备，检查风险信号，并阻止同一设备重复开户。
- 🧑‍💻 讲师：Keshia Rose，Fingerprint 高级开发者布道师，专注帮助开发者落地反欺诈与设备智能方案。
- 🛠️ 实战内容：这是引导式构建，不是演示；可打开编辑器、克隆 starter repo，跟随讲师写代码，也可带入自己的注册流程和问题。
- ✅ 你将构建：在注册页加入 JavaScript agent 并在服务端获取已验证访客数据；创建账户前检查 bot detection 与 Suspect Score；用 visitor ID 执行“一设备一账户”；阻止来自无痕窗口或 VPN 的重复注册。
- ⏱️ 互动安排：最后 15 分钟用于实施指导与 Q&A。
- 📝 注册方式：填写姓名、邮箱、公司名称、职位等信息报名，也可请求个性化演示；主办方承诺保护隐私，可随时退订。
- 🚀 延伸信息：Fingerprint 可帮助快速识别 Web 和移动端流量，免费开始收集 visitor IDs 和信号。

---

### [](https://www.meticulous.ai/?utm_source=jsweekly&utm_medium=newsletter&utm_campaign=26q3&utm_content=classified)

**原文标题**: [Meticulous AI - Automated Frontend Testing Without Writing Tests](https://www.meticulous.ai/?utm_source=jsweekly&utm_medium=newsletter&utm_campaign=26q3&utm_content=classified)

Meticulous 是一个面向复杂代码库的自动化端到端测试平台，通过录制用户交互、AI 生成并持续演化测试套件，在 PR 阶段提供确定性、无 flake 的回归验证，开发者几乎无需维护测试。

- 🚀 核心承诺：自动化、穷尽、确定性的验证，零开发者投入，让发布速度匹配 AI 写代码速度。
- 🧠 工作流程：在本地、预发、预览 URL 等环境添加 recorder 脚本记录会话，可选记录生产环境。
- 🤖 AI 测试生成：跟踪每次交互执行的代码分支，生成覆盖每条代码行、每个用户流程和边缘案例的视觉端到端测试。
- 🔁 自动演进：测试随应用变化自动新增或淘汰，无需编写、修复或维护测试。
- ✅ PR 影响预览：提交 PR 后，合并前即可查看变更对用户工作流的影响；默认保存并回放后端响应，避免副作用和误报。
- ⚡ 无 flake 与高速：从 Chromium 层级构建确定性调度引擎，消除 flaky，并支持极快执行。
- 🧩 兼容集成：可补充或替代现有测试；支持 NextJS、React、Vue、Angular、Nuxt、SvelteKit，通过脚本标签或 recorder-loader 接入。
- 📈 规模化：测试在计算集群中高度并行，可测数千屏幕，结果可在 120 秒内返回。
- 🏢 客户信任：超过 100 家组织使用，包括 Dropbox、Notion、Engine；反馈强调零维护、无 flake、开发者喜爱与全组织推广。
- 🔐 资源入口：提供安全、文档、集成、登录、预约演示和开始使用等入口。

---

### [面向 API、AI 和 MCP 的统一网关 - Zuplo](https://zuplo.com/?utm_source=react_status&utm_medium=newsletter&utm_campaign=cooper_press_unified_1q&utm_content=classified_listing)

**原文标题**: [The Unified Gateway for APIs, AI, and MCP - Zuplo](https://zuplo.com/?utm_source=react_status&utm_medium=newsletter&utm_campaign=cooper_press_unified_1q&utm_content=classified_listing)

Zuplo 是面向 API、LLM 与 MCP 的统一网关，通过一个可编程策略引擎统一认证、限流、预算、审计与可观测性，让出站模型调用和入站 AI Agent/MCP 调用在同一处被治理、计量与变现。

- 🧭 新流量格局：应用向外调用 LLM，AI Agent 向内调用你的 API；两类流量都应由同一网关管理。
- 🛡️ 统一策略引擎：认证、限流、花费上限与审计一次编写，覆盖每个 API、LLM 和 MCP 调用。
- 🤖 四项核心能力：Agents 范围化访问、用户 API Key/JWT/OAuth、REST/GraphQL/MCP 统一接入、LLM 路由与预算护栏。
- 🔐 MCP 治理：支持 OAuth 2.1 与 PKCE，记录每次工具调用的客户端、用户、策略、scope、限流与计量。
- 💸 成本控制：动态限流阻止源站成本飙升；按团队设置 AI token 硬预算，示例 14 天节省 42.9k 美元、总支出降低 41%。
- 🚫 安全前置：认证、schema 校验、限流和提示注入防御在网关拦截；示例一周阻止 12.4k 请求，0 到达源站。
- 📊 可见性：按用户和客户端归因分析工具调用、拒绝、延迟，并导出到 Datadog 或 SIEM。
- 💳 变现能力：内置套餐、配额和用量计费，连接 Stripe，无需自建计费基础设施。
- ⚙️ 集成简单：出站保留 OpenAI SDK 仅替换 base URL；入站用 OpenAPI 扩展将操作暴露为 MCP tools/resources，并复用同一策略。
- 📈 关键指标：99.99% SLA、1B+ 终端用户、SOC 2 Type II、300+ 边缘位置、约 20 秒部署、免费层 100K 请求/月。
- ✅ 生产案例：Blockdaemon 硬件足迹降低 90%、成本节省超 70%；Yext 提升扩展与合规；Finsolutia 数小时上线 MCP Server。
- 🎯 首月价值：降低成本、缩小攻击面、证明调用合规、将流量变现、加快排障，并满足 CISO 的 AI 治理要求。

---

### [](https://js13kgames.com/2026/)

**原文标题**: [js13kGames 2026](https://js13kgames.com/2026/)

无法总结：未找到主要内容。

---

### [投票已开启！ | js13kGames 2026](https://js13kgames.com/2026/blog/voting-open)

**原文标题**: [Voting is open! | js13kGames 2026](https://js13kgames.com/2026/blog/voting-open)

无法总结：未找到主要内容。

---

### [SP13KTRA | js13kGames 2026](https://js13kgames.com/2026/games/sp13ktra)

**原文标题**: [SP13KTRA | js13kGames 2026](https://js13kgames.com/2026/games/sp13ktra)

无法总结：未找到主要内容。

---

### [](https://js13kgames.com/2026/games/hornbound)

**原文标题**: [Hornbound | js13kGames 2026](https://js13kgames.com/2026/games/hornbound)

无法总结：未找到主要内容。

---

### [2026 年中你应该了解的 HTML 新特性 – Master.dev 博客](https://blog.master.dev/new-things-you-should-know-about-html-here-in-mid-2026/)

**原文标题**: [New Things You Should Know About HTML Here in Mid 2026 – Master.dev Blog](https://blog.master.dev/new-things-you-should-know-about-html-here-in-mid-2026/)

HTML 在 2026 年中迎来一批新元素、属性和 Web Components 能力，重点提升权限恢复、声明式交互、可定制控件、SSR 与流式包含；不少特性仍处实验或单浏览器主导阶段，但大多可渐进增强。

- 🧭 总体趋势：HTML 更新虽慢但更稳健，近期新特性集中在权限、Web Components 和声明式 HTML。
- 🔐 权限恢复：专用权限元素让用户拒绝后能轻松重新授权，避免翻找浏览器设置；Cisco 数据显示新流程授权成功率从约 10% 升至 65%+。
- 📍 `<geolocation>`：封装按钮触发定位请求，不受历史允许/拒绝影响；Chrome 支持，非支持浏览器可降级为普通按钮流程。
- 🎥 `<usermedia>`：管理摄像头与麦克风权限，捕获用户意图、处理浏览器提示并返回 `MediaStream`；计划推出 `<camera>` 和 `<microphone>`。
- 📲 `<install>`：Chrome 主导的 PWA 安装语义按钮，可放在页面任意位置，缓解安装入口碎片化；需 manifest，可能还需 service worker。
- 🎛️ `<select>` 可定制：通过 CSS 完全重设计下拉框，需 `appearance: base-select`、`::picker(select)` 等；Safari 已支持。
- 🧩 Web Components：不是单一功能，而是一组独立演进的 API。
- 🗂️ Scoped Element Registries：可创建多个自定义元素注册表并指定给 Shadow DOM，解决同名但不同版本组件共存问题。
- 🌑 Declarative Shadow DOM：无需 JavaScript 即可声明 Shadow DOM，使用 `<template shadowrootmode="open">`，适合 SSR 输出。
- 🎯 Reference Target：允许 Shadow DOM 内外元素互相引用，例如外部 `<label>` 关联内部 `<input>`，提升可访问性。
- 🎨 Declarative CSS Module Scripts：实验性 Chrome 功能，通过 importmap 和 `<link import="foo">` 在 Shadow DOM 中声明式引入 CSS。
- 📥 HTML Includes / 流式包含：探索声明式局部更新与原生 include，用 `<template for="placeholder">` 等把流式 HTML 插入指定位置。
- 🪟 Persistent Widgets：`<persistentwidget>` 类似 iframe，但可在同源导航间持久存在而不重载。
- 🖼️ HTML-in-Canvas：可在 `<canvas>` 内写 HTML，借助 `layoutsubtree` 和 JS 绘制到画布，内容仍可交互。
- ⌨️ Commands & Invokers：用 `commandfor` / `command` 替代部分 popover 属性，支持内置与自定义命令；interest invoker 可用 hover 触发命令或工具提示。
- 🧊 `<model>`：Safari 在 WWDC 2026 展示的原生 3D 模型元素，如 `<model src="mallet.usdz">`，已有草案规范。
- 🔘 `focusgroup` 属性：Chrome 实验，容器内实现 roving tabindex，Tab 进入组后用方向键切换，如工具栏。
- 🔍 `hidden="until-found"`：元素可隐藏但能被页面搜索发现并自动展开，适合 FAQ 或折叠内容。
- 🏷️ `<h1>` 尺寸调整：浏览器统一 UA 样式，不再因嵌套在 `<section>` 中而降级字号和边距。
- 🖼️ `sizes="auto"`：图片可配合 `srcset` 和懒加载自动响应式，免去手写 `sizes` 的麻烦。
- 💡 其他：`popover="hint"` 提供轻量提示弹层并保留点击外部关闭；许多特性仍属实验性或单浏览器支持，但可渐进增强。

---

### [Three.js 大会 巴黎 2026 | 9 月 10-11](https://threejs.paris/)

**原文标题**: [Three.js Conf Paris 2026 | September 10-11](https://threejs.paris/)

overview summary
- 🎉 首届 Three.js Conf Paris 2026 将于 2026 年 9 月 10-11 日在巴黎 Maison de la Chimie（28 Rue Saint-Dominique, 75007）举行。
- 🗓️ 两天活动包括演讲、圆桌、闪电演讲、交流联谊，以及塞纳河游船 after party。
- 🧑‍💻 面向开发者、设计师、3D 艺术家及 Web 图形从业者，主题涵盖 WebGPU、Three.js Shading Language、React Three Fiber、创意开发、交互设计与性能。
- 🎤 演讲嘉宾包括 Makio64、Justine Soulié、Patrick Heng、Ponpon Mania、MrDoob、Vicente Lucendo、Célia Lopez、Bruno Simon、Sunag、Renaud、Daria Nevezhyna、Damien Mortini、Marcus McLean、Kim Boutin 等。
- 🎟️ 会议通行证 249 欧元起；常规票 309 欧元，商务票 799 欧元，学生票经审核后 129 欧元。
- 💶 价格在适用时含增值税；会议票含两天演讲与圆桌、全天饮品、交流及塞纳河 after party。
- 📧 门票为电子票，通过 Mollie 安全支付后以邮件发送。
- ❌ 固定日期活动票不可退款，依据法国消费者法第 L221-28 12° 条；可在活动日前转让，若主办方取消则 30 天内全额退款。
- 🏢 数据控制者与活动主办方为 MAKIO，地址 9 rue des Colonnes, 75002 Paris, France；SIREN 883 228 116，SIRET 883 228 116 00041，RCS Paris，VAT FR59 883 228 116。
- 📮 联系邮箱 contact@threejs.paris，用于隐私请求、无障碍问题或票务支持。
- 🔗 官网提供演讲者与阵容、票务、商品、日程、Advanced R3F 工作坊、Advanced TSL 工作坊、巴黎包含工作坊、FAQ、条款、Game Kit 及文档等入口，并可查看完整条款、隐私信息、法律声明与行为准则。

---

### [走进巴黎首届 Three.js](https://tympanus.net/codrops/2026/09/10/inside-the-first-three-js-conference-in-paris/)

**原文标题**: [Inside the First Three.js Conference in Paris | Codrops](https://tympanus.net/codrops/2026/09/10/inside-the-first-three-js-conference-in-paris/)

overview summary
首届 Three.js Conference 在巴黎举行，是 Three.js 社区首次专门大会，汇聚创作者、开发者、设计师与艺术家。Codrops 团队现场记录两天的大会演讲、实验、演示、圆桌与社区时刻，主题涵盖 AI、WebGPU、动画、创意工具和 Web 3D 的未来。

- 🇫🇷 首届 Three.js Conference 在巴黎举办，Codrops 的 Houmahani Kane、Adel Sanaa、Rafael Teixeira 现场记录大会点滴。
- 🎤 开场由 David Ronai 欢迎；Vicente Lucendo 分享《Messenger》，Robin Payot 用 Three.js/WebGPU 重制《塞尔达》部分内容。
- 🤖 Mr.doob、Renaud Rohlinger、Nicolas Barrateau、Florian Zumbrunn 讨论 AI 对 Three.js 创作的影响：加速实现，但基础与判断力仍关键。
- ✨ Cassie Evans 宣布 GSAP 4 将推出，带来弹簧动画、更好的 Three.js 集成，以及 DOM/WebGL 性能工具。
- 🌐 Daria Nevezhyna 与 Kim Boutin 分别谈沉浸式产品配置器和实验性、故障美学，强调 Web 可以更有表现力。
- 🎨 Célia Lopez 鼓励持续学习并公开未完成作品；Natalia Markoborodova 和 Thomas Nattestad 展示 HTML in Canvas 与 THREE.HTMLTexture。
- 🧠 Lovis Odin 展示生成式 AI 进入生产流程，包括 Blender、图像转视频、LoRA、Gaussian splats 与实时生成。
- 🔥 “Roast My Folio”中 Bruno Simon、Cassie Evans、Nicolas Barradeau 点评作品集，提醒避免过长加载、过多特效和大段文字。
- ⚡ 首日十场闪电演讲覆盖 AI+Three.js、浏览器 3D 工具、交互装置、Anime.js、实时渲染和游戏等，强调感知与品味。
- 💙 Hervé Studio 的 Julie Martin 与 Romain Briaux 用约七个月打造大会视觉、网站、场景、周边与互动 3D 地图，并制作可互动的电子徽章。
- 🧑💻 Mr.doob 谈 AI 与 Three.js：AI 像 90 年代抗锯齿，把创作抽象层级推高；建议保持好奇。
- 📦 Day Two 中 Justine Soulié 和 Patrick Heng 展示手工插画互动故事《Ponpon Mania》；Poimandres 谈 React Three Fiber 面向 WebGPU/TSL 的未来。
- 🕹️ Damien Mortini 回顾 Flash 精神与 Christmas Experiments；Marcus McLean 展示辐射场与流式照片级 3D。
- 🤝 Design & AI Workflows 圆桌认为 AI 缩短想象与执行的距离，但经验仍决定如何引导与修正工具。
- 🚀 Misha Kiiatkin 分享游戏资产优化管线；Anderson Mancini 展示约 6MB 的 WebGPU 场景；Renaud Rohlinger 介绍 Expo 2025 大阪百万粒子水装置。
- 🎭 Cassandre Leguay 用表演艺术讲 UX：框架、注意力、预期、打破框架；Sunag 介绍 TSL；Edan Kwan 拆解 Lusion 的视觉技巧。
- 🏆 次日八场闪电演讲包括无代码 3D、Blackbird Awards、iJewel、AI+3D 喜剧、JOYCO 工具等。
- 🧭 最后 Antoine Ménard 与 Bruno Simon 谈如何创造令人难忘的 Web 体验：早期原型、动画、声音、原创点、快速迭代与灵感收集。
- 🇫🇷✨ 大会落幕，感谢 David Ronai、所有讲者与 Codrops 现场团队；社区期待下一届，并留下船派对悬念。

---

### [](https://tailwindcss.com/blog/tailwind-is-joining-shopify)

**原文标题**: [Tailwind Labs is joining Shopify - Tailwind CSS](https://tailwindcss.com/blog/tailwind-is-joining-shopify)

Tailwind CSS 正式加入 Shopify，创始人表示这将为框架提供长期稳定的归属；Tailwind CSS 及其他开源项目仍将保持 MIT 许可并持续维护，同时商业业务将收缩，停止新用户注册，团队将专注于在 Shopify 支持下发展 Tailwind CSS。

- 🚀 Tailwind 宣布加入 Shopify，创始人回顾九年前仅为个人项目而创建它，如今每周安装量超过 1.1 亿次。
- 🌍 Tailwind 已被 ChatGPT、X、Cloudflare、Reddit、Shopify 等全球大型公司用于产品样式。
- 🏠 加入 Shopify 是为了给 Tailwind 一个稳定长期的家，确保为数百万依赖者持续维护。
- 🛍️ Shopify 提供真实且复杂的产品场景，包括商家店铺、后台管理、购物结账、Shop App 和代理式商务。
- 🤝 Shopify 是最早大规模采用 Tailwind 的公司之一，既自用也为其客户押注，Tailwind 已是其技术栈的重要部分。
- 💡 创始人认同 Shopify 帮助更多人创业的使命，并因创业改变人生而对此充满热情。
- 🔓 Tailwind CSS 和其他开源项目不会改变，仍将永久保持 MIT 许可，团队继续在 Shopify 支持下领导维护。
- 📦 商业方面不再试图围绕 Tailwind 扩张业务；现有客户保留 Tailwind Plus 和 ui.sh 访问权，但关闭新用户注册。
- 🙏 创始人感谢九年来所有使用和支持 Tailwind 的人，并认为 Shopify 是继续这项工作的最佳地点。

---

