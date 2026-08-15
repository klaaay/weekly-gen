### [](https://tanstack.com/blog/announcing-tanstack-form-v2-alpha)

**原文标题**: [Form v2 is here: All you need to know about the alpha | TanStack Blog](https://tanstack.com/blog/announcing-tanstack-form-v2-alpha)

TanStack Form v2 推出了 alpha 版本，这是基于 v1 一年来反馈进行的核心重写。v2 在保持基本 API 风格的同时，大幅改进了验证器、监听器、类型安全、SSR 等关键体验，并开放试用。

- 🚀 Form v2 alpha 正式发布，核心重写，API 基本兼容 v1，运行时性能更快、类型更安全。
- 🔄 验证器从事件键控对象改为管道模型，每个验证器独立声明自己的触发事件。
- 📌 一个验证器可以同时绑定多个触发事件（如 change 和 blur），避免重复注册和重复报错。
- 🔗 多个验证器可以共享同一触发事件，并通过 `bailIfInvalid` 控制执行顺序。
- 🎯 新增 `when` 条件，支持只在特定条件下触发验证（例如首次提交后才验证 change）。
- 🎧 监听器也改为同样的管道模型，支持多触发、多监听器共享触发以及条件执行。
- 🧩 新增 `strictSchema` 和 `looseSchema` 模式，解决 defaultValues 与 schema 类型不匹配时的问题。
- 🛡️ Form Composition 组件支持类型品牌约束，不兼容的组件（如字符串字段上的 `NumberInput`）会在编译期报错。
- 🌐 SSR 改进：服务端验证器移入共享 formOpts，`serverValidate` 返回结果而非抛错，客户端直接使用 `serverState`，省去手动合并。
- ⏳ v2 alpha 暂缺：内置表单持久化、非 React 适配器的 Form Composition、Submit meta。
- 📚 试用 alpha 需要查阅迁移指南，并关注两个 RFC 议题（#2296 与 #1823）。
- 🙏 感谢社区反馈，团队期待在 alpha 阶段收集更多意见以完善 v2。

---

### [](https://reactnative.dev/blog/2026/08/11/react-native-0.87)

**原文标题**: [React Native 0.87 - Strict TypeScript API, Metro Update, Swift Package Manager, AGP 9 Support · React Native](https://reactnative.dev/blog/2026/08/11/react-native-0.87)

React Native 0.87 正式发布，默认启用 Strict TypeScript API，更新 Metro 至 0.87，新增 Swift Package Manager 实验性支持，并提升了最低工具链要求（Node 22、AGP 9、Kotlin 2.0+）。同时包含多项破坏性变更、废弃与移除，以及社区贡献致谢。

- 🚀 Strict TypeScript API 成为默认 JS API：类型由源码直接生成，更准确稳定；根导出为 API 范围，内部文件改动不再影响外部。
- 🧩 破坏性变更：深层导入（如 react-native/Libraries/*）变为类型错误，部分类型名称重构（如 ViewInstance），并提供临时 opt-out 开关（0.88 前可用）。
- ⚡ Metro 升级至 0.87：源码映射生成快 2 倍，内存占用减半；支持 TypeScript/ESM 配置，移除 YAML 和 .es6 支持。
- 📦 实验性 SwiftPM 支持（iOS）：替代 CocoaPods，仅需 Xcode；使用 npx react-native spm 命令集成，仍有库需 Package.swift 等限制，暂不建议生产使用。
- 🧱 Headers 重构：新增 Headers-only XCFramework，头文件需带命名空间导入（如 #import <React/RCTAppDelegate.h>）。
- 🤖 Android 支持 AGP 9：提供 opt-out 内置 Kotlin/新 DSL 的 flags，compileSdk 升至 37，minCompileSdk 为 34。
- 📋 工具链最低要求：Node ≥ 22.13.0、Kotlin ≥ 2.0（内置 2.2.0）；移除 InteractionManager、废弃 Modal/StatusBar 相关属性等。
- 🧹 其他移除：react-native/rn-get-polyfills 废弃、react-devtools 独立连接移除、useTurboModules 移除等；多 API 标记弃用（如 ImageBackground、NativeMethods）。
- 🎉 致谢与升级：265 commits、74 位贡献者；使用 Upgrade Helper 或 npx 创建新项目；Expo 项目通过 expo@canary 可用。

---

### [严格 TypeScript API · React Native](https://reactnative.dev/docs/strict-typescript-api)

**原文标题**: [Strict TypeScript API · React Native](https://reactnative.dev/docs/strict-typescript-api)

overview summary：React Native 0.87 起默认启用严格 TypeScript API，这是一项破坏性变更，旨在用从源码生成的类型取代手写类型，提供更严谨、更稳定的公共 API 契约。文档详述了主要破坏性变更、迁移方法、退出机制及常见问题。

- 🔧 严格 API 自 0.87 起默认开启，替代旧的、人工维护的 TypeScript 类型定义（此前自 0.80 起可选用）。
- 🚫 禁止深层导入（deep imports）：API 仅限从 `react-native` 主入口导出，内部路径变化不再影响外部。
- 📜 类型直接从源码生成，提升覆盖率、正确性和兼容性保证。
- ↩️ 可通过 `tsconfig.json` 的 `customConditions` 临时恢复旧类型，但未来版本将移除该退出选项。
- ⚠️ 迁移时请保持 `skipLibCheck` 开启（`@react-native/typescript-config` 默认开启），避免第三方 `.d.ts` 错误干扰。
- 📦 依赖出现类型错误时，先更新库版本；如遇到不兼容库，可用 `paths` 将深层导入映射到未类型化存根，并上报问题。
- 🆕 新增 `CodegenTypes` 命名空间（如 `Int32`、`WithDefault`），`codegenNativeComponent` 和 `codegenNativeCommands` 可直接从 `react-native` 导入。
- 🏷️ 各内置组件新增专用实例类型（如 `ViewInstance`、`TextInputInstance`），推荐用于 ref，替代旧的 `useRef<View>` 写法。
- ❌ 移除 `*Static` 类型（如 `LinkingStatic`、`PlatformStatic` 等），直接使用同名值作为类型。
- 🩹 测试 mock 大多无需改动；若测试文件深层导入内部模块，可用 `@ts-expect-error` 抑制错误。
- 🔄 `InitializeCore` 深层导入改为 `react-native/setup-env`；`InitializeCore` 自 0.87 起弃用。
- 🎭 Animated 节点改为非泛型类型，`Animated.LegacyRef` 被移除，改用对应的 `*Instance` 类型。
- 🎛️ 所有可选属性统一类型为 `type | undefined`；移除废弃的 `*Properties` 别名（如 `ViewProperties` → `ViewProps`）。
- 🧹 清理了组件未使用的属性类型及内部辅助类型（如 `RecursiveArray`、`RegisteredStyle` 等）。
- 💡 运行时无变化：严格 API 仅影响 TypeScript 类型解析，不改变 JavaScript 行为和 bundle。
- 🤝 库和应用可独立迁移：严格 API 按项目通过各自 `tsconfig.json` 启用；但库若发布原始 TS 源码需确保无深层导入。
- 📢 若所需 API 未从根导出，可能是设计意图；可在讨论帖中反馈，合理情况会提升为公开 API。
- 🎬 官方在 App.js 2025 分享了严格 API 的动机与实现细节，可观看视频深入了解。

---

### [](https://master.dev/courses/frontend-architecture/?utm_source=email&utm_medium=reactstatus&utm_content=frontendcooper)

**原文标题**: [Architect Scalable Frontend Applications | Master.dev](https://master.dev/courses/frontend-architecture/?utm_source=email&utm_medium=reactstatus&utm_content=frontendcooper)

本課程深入探討前端架構從單體到微前端的演進，涵蓋架構基礎、模組化單體、Monorepo 工具鏈，以及微前端的實踐與通訊方式，適合具備前端開發經驗、想提升架構能力的工程師。

- 🏛️ 課程介紹架構四大支柱：風格、特性、決策與邏輯元件，並以 RPG 角色比喻幫助理解。
- 🧱 單體架構以電商平台為例，使用 C4 模型視覺化系統，並探討邊界模糊導致的「大泥球」問題。
- 📦 模組化單體透過領域驅動設計（DDD）識別子域，定義資料夾結構與依賴邊界。
- 🚧 使用 ESLint boundaries 外掛與 Dependency Cruiser 強制執行架構規則，防止跨模組依賴。
- 🗂️ Monorepo 架構將所有套件集中於單一工作區，搭配 Turborepo 進行快取、任務編排與依賴管理。
- 🔄 透過 TurboRepo 標記套件與定義規則，確保依賴方向正確，並產生依賴圖視覺化專案結構。
- 🧩 微前端解決獨立部署與團隊擴展問題，比較 iframe、Web Components 與 Module Federation 等方案。
- ⚙️ 從零建立微前端，使用不同 port 與 proxy 達成無縫導覽，並以 localStorage 分享狀態。
- 🔌 Module Federation 實現運行時共享程式碼，透過 react-lazy 非同步載入遠端模組，並需處理錯誤與 Suspense。
- 💬 微前端通訊方式包括 postMessage、props 傳遞與 Nanostores，強調元件間需保持解耦與獨立性。
- 🆕 Module Federation 2.0 引入 MFManifest.json、運行時註冊遠端，並透過 RSBuild 外掛簡化升級與型別產生。
- 🏁 課程總結指出不必要的 Module Federation 可能導致 CSS 衝突等缺點，應根據成本分析決定是否採用。

---

### [](https://engineeringblog.yelp.com/2026/08/migrating-a-large-flow-monorepo-to-typescript.html)

**原文标题**: [Migrating a Large Flow Monorepo to TypeScript](https://engineeringblog.yelp.com/2026/08/migrating-a-large-flow-monorepo-to-typescript.html)

overview summary  
- 🔄 文章讲述了Yelp从Flow迁移到TypeScript的全过程，强调在保持类型安全的前提下逐步完成大型Monorepo的迁移。  
- 🎯 核心目标是维护开发者对类型检查的信任，避免临时禁用类型检查或批量插入忽略注释，确保迁移过程中类型完整性不妥协。  
- 🛠️ 实现方案是逐包转换，使用flowts和flowgen等工具，结合自研codemod处理边缘情况，并从依赖树最底层开始向上迁移。  
- 🧪 通过长达数月的内测（dogfooding）打磨工具链和文档，转换了90个基础包，为全面推广做好准备。  
- 🚀 2023年5月向功能团队正式发布TypeScript，迁移初期进展迅速，但随后趋于平缓，需通过依赖图分析锁定关键包推动进度。  
- 📈 最终在2026年2月完成迁移，共转换140万行源码，类型覆盖率从83.15%提升至96.44%，工程师普遍反馈生产力提升。  
- 💡 关键经验包括：大量宣传和文档工作至关重要，设定阶段截止日期比自由推进更有效，以及在关键时刻介入迁移瓶颈包能起到杠杆作用。  
- 🎉 文章感谢Webcore团队和所有参与迁移的工程师，并提及一些未成功的尝试（如早期LLM自动化转换）作为经验教训。

---

### [红迪](https://www.reddit.com/r/nextjs/comments/1vnlcsk/were_the_nextjs_team_ask_us_anything/)

**原文标题**: [Reddit](https://www.reddit.com/r/nextjs/comments/1vnlcsk/were_the_nextjs_team_ask_us_anything/)

overview summary  
- 📝 您尚未提供需要总结的文本内容。  
- 🔍 请发送文章或段落，我将按“概述 + Emoji 要点”的格式为您生成中文总结。

---

### [](https://biomejs.dev/linter/rules/use-react-compiler/)

**原文标题**: [useReactCompiler | Biome](https://biomejs.dev/linter/rules/use-react-compiler/)

该规则是 Biome 的实验性 lint 规则，用于通过 React Compiler 验证组件和 Hook 是否可安全编译，仅对 React 19 及以上项目生效，并支持多种编译模式配置。

- 🔬 属于 `nursery` 组，处于实验阶段，行为可能随时变化，默认严重级别为“信息”。
- ⚙️ 配置方式：在 `biome.json` 的 `linter.rules.nursery` 中设置 `useReactCompiler` 为 `"error"` 等。
- 🚀 仅在最近的 `package.json` 声明 React 19 或更新版本时运行；React 18 及以下或无 React 依赖的项目会跳过。
- ❌ 无效示例：在条件语句中调用 `useState` 会触发诊断，提示 Hook 必须始终在顶层以固定顺序调用。
- ✅ 有效示例：组件内只返回 JSX 且不违反 Hook 规则时不会报错。
- 🧩 提供 `compilationMode` 选项：`"infer"`（默认，分析符合 React 约定的函数）、`"annotation"`（仅分析带 `"use memo"` 指令的函数）、`"all"`（分析所有函数，可能在非 React 代码中产生诊断）。
- 📦 使用 `"all"` 模式时，即使函数不符合 React 命名规范（如普通工具函数）也会检查外部变量修改等滥用问题。
- 🩹 该规则仍在积极开发中，可能缺少功能或存在粗糙之处，可通过相关 GitHub 链接反馈问题。

---

### [React Native 连接大会](https://reactnativeconnection.io/)

**原文标题**: [React Native Connection Conference](https://reactnativeconnection.io/)

overview summary
React Native Connection 是法国首个完全专注于 React Native 开发者社区的全天会议，2026年9月24日在巴黎举行，汇聚法国及国际开发者，分享最新实践与趋势，并提供丰富的演讲、交流与社交机会。

- 🗓️ 会议将于2026年9月24日在巴黎举办，全天活动，聚焦React Native社区最新实践与趋势。
- 🎤 演讲嘉宾包括来自Meta、Expo、Callstack、Margelo、Software Mansion等公司的专家，如Jay Meistrich、Satyajit Sahoo、Alex Hunt等。
- 📋 日程涵盖欢迎、咖啡休息、午餐及多个技术演讲，主题涉及Agent测试、键盘同步、导航库、Web端React Native、程序化动画、XR等。
- 🎟️ 门票分为早鸟票（已售罄）、普通票（289€+税）和免费社区票（需申请），所有门票包含完整会议、餐饮和社交活动。
- 🤝 赞助商包括RevenueCat、The Mobile-First Company、Codemagic，媒体伙伴有weshipit.today和This Week In React。
- 👥 组织团队由多位资深React Native开发者组成，包括Simone Civetta、Alexandre Moureaux、Delphine Bugner等。
- 📍 会议地点为Fondation Biermans-Lapôtre，位于巴黎14区，并提供FAQ和赞助咨询渠道。

---

### [](https://nextjs.org/blog/making-v0-navigations-instant)

**原文标题**: [Making Navigations Instant in v0 | Next.js](https://nextjs.org/blog/making-v0-navigations-instant)

概述：本文介绍了Vercel如何利用Next.js 16.3的新特性，通过Agent驱动的测试循环，在v0平台中实现即时页面导航，并分享了具体方法、代码示例及对框架意义的思考。

- 🚀 Next.js 16.3 新增“动态应用预渲染”能力，可在用户浏览时预取并缓存动态UI，使个性化应用也能实现即时导航，避免静态预渲染的不适用和全量预取的高成本。
- 🔁 使用“Agent循环”自动化优化：为每条慢导航编写失败测试，应用修复后重跑测试，直到通过，再将测试纳入CI防止回归；关键依赖可验证目标、失败测试、技能模式、真实反馈四项要素。
- 🧪 新测试助手 `instant()`（来自 `@next/playwright`）能暂停导航并断言UI是否无需网络请求即可见，将“快”这种模糊体验转化为确定性测试。
- 🛠️ v0团队针对聊天、设置、个人资料等关键页面运行该循环，常见改动是把动态数据访问移到Suspense边界下，或从根布局中移除阻塞依赖，最终16条新测试守护这些即时路由。
- 📦 发布两个Skill帮助开发者复现：`next-cache-components-optimizer`（优化现有应用）和`next-cache-components-adoption`（迁移到Cache Components），配合Agent即可自动优化导航。
- 🧠 框架在Agent时代依然关键：确定性验证器（如`instant()`）能将模糊的UX质量转化为可测试标准，引导Agent产出更好的UI，这正是Next.js未来的方向。

---

### [](https://www.youtube.com/watch?v=6lSH1-ytd7E)

**原文标题**: [ - YouTube](https://www.youtube.com/watch?v=6lSH1-ytd7E)

该内容为 YouTube 网站页脚的常规导航及法律信息链接集合，涵盖媒体、版权、联络方式、创作者与广告服务、开发者选项、条款隐私及平台运作说明，并标注版权归属 Google。
- 📰 提供媒体相关入口与新闻资讯
- ⚖️ 明确著作权政策与知识产权说明
- 📩 设置“与我们联络”的用户支持通道
- 🎬 面向创作者提供创作工具与资源
- 📢 包含广告合作及商业推广选项
- 💻 为开发者开放技术接口与文档
- 📜 列出使用条款与平台规范
- 🔒 说明隐私权保护及数据处理方式
- 🛡️ 展示政策与安全性管理措施
- ⚙️ 介绍 YouTube 运作方式及功能测试
- ©️ 标注版权归属为 Google LLC（2026）

---

### [](https://www.jovidecroock.com/blog/referential-stability-types/)

**原文标题**: [Making Referential Stability a Type](https://www.jovidecroock.com/blog/referential-stability-types/)

本文提出一个在 React/Preact 中把“引用稳定性”建模为类型约束的实验性方案。作者设计了一个带 unique symbol 隐形标记的 `Stable<T>` 类型，并通过单独入口提供严格版本的 hooks 与 context 工具，使不稳定的依赖在编译期直接报错，从而保护 `memo` 等优化手段不被意外打破。文章还讨论了方案局限、与 React Compiler 的关系，以及对 AI 编程 Agent 的潜在价值。

- 🔧 问题根源：新数组/函数字面量导致引用不稳定，使 memo 失效并引发无谓重渲染，这类问题隐蔽且难以排查。
- 💡 核心思路：将“引用稳定性”编码进类型系统，用 `Stable<T>` 标记预期稳定的对象、数组和函数；基本类型按值比较，因此无需标记。
- 🏷️ 实现方法：类型定义为 `Stable<T> = T extends object ? T & { readonly [stableBrand]: true } : T`，用 `unique symbol` 防止应用代码伪造。
- 📏 稳定性定义：并非不可变，而是引用在无关渲染间保持稳定，仅在状态更新或依赖失效时变化；这是优化契约，而非正确性保证。
- ⚠️ 模块增强方案失败：无法移除 React 原生宽松重载，一旦某个依赖缺少证明，就会静默回退到原始类型，无法在依赖位置报错。
- 🚪 单独入口方案：从 `'stableref/react'` 导入严格版 `useMemo`/`useCallback` 等，依赖元组逐项检查，不稳定的依赖直接在该处报错，并附带可读的修复提示。
- ✅ 承认 React 自有稳定值：`useState` 的 state 和 setter、`useRef` 容器等被标记为 `Stable`，无需额外证明；初始化器闭包本身也不要求稳定。
- 🧰 工具函数 `stable()`：运行时就是 `x => x`，用于标记模块作用域的稳定常量，如 `EMPTY_ITEMS`，让证明留在真正成立的顶层。
- 🌳 context 改造：`createStableContext` 要求 Provider 的 value 必须为 `Stable<T>`，把稳定性责任放在值拥有者身上，保护深层消费者。
- 🔄 Preact 支持：提供 `'stableref/preact'` 入口，用同样原理覆盖 Preact/hooks，证明属于值契约而非特定框架。
- 🚧 局限：类型断言 `as Stable<T>` 仍可绕过，需要审查和约定；React Compiler 与此问题不同，两者互补而非替代。
- 🤖 对 AI Agent 友好：类型错误是 agent 易于响应的反馈，错误信息直接指出“使用 useMemo/useCallback、源自 useState、依赖 useRef 容器或包装 stable()”等修复方式，让构建保持红色直到稳定。
- 🧭 更广泛愿景：许多类似“稳定性”的隐含属性都应成为类型系统可承载的证明，而非依赖注释、lint 规则和口口相传。作者正以实验包 `stableref` 继续探索。

---

### [React Native 应用中的条形码扫描：完整指南（2026）-](https://margelo.com/blog/react-native-barcode-scanner)

**原文标题**: [Scanning Barcodes in React Native Apps: The Complete Guide (2026) - Margelo](https://margelo.com/blog/react-native-barcode-scanner)

本文全面比较了 2026 年 React Native 中可用的 QR 码/条码扫描方案，从免费到商用，按使用场景给出选型建议，并剖析底层引擎差异、平台特有行为及常见陷阱。

- 📱 最简单的扫描方案是 `react-native-data-scanner`：调用 `scanBarcode()` 一行即可，使用 iOS VisionKit / Android Google Code Scanner 系统原生 UI；Android 甚至无需相机权限；但不能自定义 UI、只能单次扫描、无法预验证，且要求 iOS 16+、Google Play 服务，也不支持 Expo Go。
- 🎥 最强大的方案是 `react-native-vision-camera`：提供应用内相机视图，支持自定义取景框、连续扫描多码、可在 JS 中验证后再关闭；跨平台推荐其 ML Kit 插件，iOS 上可用零额外依赖的 Object Output（基于 AVFoundation）。
- 🧩 底层四大引擎决定行为差异：ML Kit（跨平台）、AVFoundation（iOS）、VisionKit（iOS）、ZXing（iOS 部分格式）；各家库只是包装，解码器怪癖会继承自引擎。
- 📸 Expo 环境中若必须用 Expo Go，只能选 `expo-camera`（或 `launchScanner()`）；VisionCamera 和 react-native-data-scanner 需要开发构建（dev build）。
- 🖼️ 从图片/相册扫描 QR 码可用 VisionCamera 的 `scanCodesInImageAsync(...)`，Expo 的 `scanFromURLAsync(...)` 在 iOS 上仅支持 QR 格式。
- ⚠️ 平台坑：iOS 会把 UPC-A 报告为 EAN-13，需在 JS 中剥离前导零；expo-camera 已自动处理，勿重复清洗；PDF417 在密集/损坏时可能失败，建议用最高分辨率并考虑商用引擎。
- 💰 付费 SDK（Scandit/Scanbot）仅在高吞吐工业场景、高密度受损条码、批量驾照 PDF417 等场景下值得；免费方案对多数 App 足够，厂商基准数据需谨慎看待。
- ♻️ 应弃用并替换：`react-native-camera`（已归档）、`react-native-qrcode-scanner`（已归档）、`expo-barcode-scanner`（已移除），分别改用 VisionCamera、VisionCamera、expo-camera。
- 🔦 常见问题处理：Expo 中可用将 `onBarcodeScanned` 设为 `undefined` 来防止重复触发；VisionCamera 中用 `torchMode` 控制闪光灯，Expo 中用 `enableTorch`；彻底免权限扫描仅 Android 的 react-native-data-scanner 可行。
- 🏁 最终建议：先选最简单的 `react-native-data-scanner`，若需自定义相机体验再升级到 VisionCamera；2026 年 React Native 条码扫描已是成熟问题，重点在于按需选择。

---

### [](https://www.youtube.com/watch?v=PypMPaW0wu4)

**原文标题**: [ - YouTube](https://www.youtube.com/watch?v=PypMPaW0wu4)

overview summary
- ℹ️ 此內容為 YouTube 的標準頁面導覽與法律資訊清單，涵蓋簡介、媒體、著作權、聯絡方式、創作者與廣告等連結。
- 📄 包含開發人員、條款、隱私權、政策與安全性等法律與平台規範項目。
- ⚙️ 說明 YouTube 運作方式與新功能測試，並顯示版權所有 © 2026 Google LLC。

---

### [](https://gtkx.dev/blog/gtkx-1-0)

**原文标题**: [GTKX 1.0: The React framework for Linux | GTKX](https://gtkx.dev/blog/gtkx-1-0)

GTKX 1.0 正式发布，这是一个面向 Linux 的 React 框架，在 GTK4 之上提供声明式 UI 开发能力，通过 JSX 构建 GObject 实例，并整合了 React 生态、代码生成、测试工具与开发流程，同时冻结了 1.x 的公共 API 以保持稳定。

- 🚀 GTKX 1.0 发布，为 Linux 桌面带来 React 声明式开发体验，弥补 GTK4 缺乏的声明式层。
- ⚛️ 使用 JSX 直接创建 GObject 实例，支持 React 19 的 hooks、context、Suspense、portals 等特性。
- 📦 应用运行在普通 Node.js 进程中，可访问 node:fs、fetch、npm 等生态，GTK 与 JS 共享单线程。
- 🎯 仅支持 Linux 平台，目标明确：换取向开发者暴露完整的 GTK 工具包，而非跨平台子集。
- ⚙️ 通过读取系统 .gir 文件，生成类型化的 @gtkx/gi 和 @gtkx/jsx 绑定，覆盖全部 GObject 与属性。
- 🧩 所有 GObject 都能作为 JSX 元素使用；对于属性无法表达的 API，通过 behavior 机制扩展，可自定义。
- 📋 复杂视图如 ListView、ColumnView 等提供组件封装，数据驱动渲染，性能大幅提升（同步百万行耗时从 2228ms 降至 277ms）。
- 🧪 @gtkx/testing 基于无障碍树查询，userEvent 检查真实交互条件，测试无 mock，并有独立 headless Wayland 环境。
- 🔧 开发体验完善：Fast Refresh、打包、资源导入、GSettings schema 类型化，以及文档生成与 MCP 服务器支持。
- 🛡️ 1.0 冻结生成元素、prop 规则、行为契约及相关库 API，1.x 版本保持兼容。
- 🔄 从 v0 迁移的改动是机械性的：导入路径、挂载方式等有清晰迁移指南。
- 🗺️ 未来计划包括 gtkx deploy、动画、导航、表单等模块，路线图公开并欢迎社区参与排序。
- 🙏 感谢 GTK、GObject-Introspection、React 等上游项目及所有测试反馈者；鼓励通过 npm create gtkx 快速上手。

---

### [](https://kbar.vercel.app/)

**原文标题**: [kbar – command+k interface for your site](https://kbar.vercel.app/)

overview summary
- ❗ 您尚未提供需要总结的文本内容，请补充文章或段落，我将按照要求生成中文要点列表。

---

### [](https://gooey.jakubantalik.com/)

**原文标题**: [Liquid Gooey — liquid UI for React](https://gooey.jakubantalik.com/)

您尚未提供需要总结的文章内容，请补充后我将按照以下格式为您输出：

overview summary
- 😊 要点一
- 📌 要点二
- ✨ 要点三

请把需要总结的文本发送给我即可。

---

### [](https://github.com/react-hook-form/react-hook-form/releases/tag/v7.85.0)

**原文标题**: [Release Version 7.85.0 · react-hook-form/react-hook-form · GitHub](https://github.com/react-hook-form/react-hook-form/releases/tag/v7.85.0)

react-hook-form 发布了 v7.85.0 版本，包含新功能支持、多项 bug 修复以及代码清理，旨在提升表单处理的稳定性与类型体验。

- ✨ 新增对 React `<Activity />` 组件的支持
- 🐞 修复 `valueAsDate` 字段下 min/max 验证被跳过的问题
- 🐞 修复 field array 在 `append`、`prepend`、`insert`、`remove` 时根错误丢失的问题
- 🐞 修复 field array 操作后因陈旧渲染而重复创建路径的问题
- 🐞 修复 `useWatch` 优先使用表单 `defaultValues` 而非 hook 自身 `defaultValue` 的问题
- 🐞 修复 `setValue` 重复发出 `values` 状态通知的问题
- 🐞 修复 TypeScript `getFieldState` 对字段路径的错误解析
- 🧹 移除 `tinybench` 依赖及无用代码、过期的 API Extractor 报告
- 🎉 感谢多位贡献者的参与和支持

---

### [](https://reactadvanced.com/?utm_source=partner&utm_medium=reactstatus)

**原文标题**: [React Conference In London, October 23 & 26, 2026](https://reactadvanced.com/?utm_source=partner&utm_medium=reactstatus)

overview summary
- 🎤 React Advanced 大会将于 2026 年 10 月 23 日（伦敦现场+远程）与 26 日（全球远程）举行，汇聚 40+ 位顶尖讲者，预计 800+ 现场与会者和 5000+ 远程开发者。
- 📍 活动地点为伦敦 The Brewery，采用混合形式：首日含现场互动与远程直播，次日为全球远程专场及多场免费工作坊。
- 🧩 四大核心 Deep Dive 主题：全栈开发与架构、AI Agents 与辅助编程、AI 工程实践、从工程师成长为 Tech Lead 的进阶路径。
- 🤖 大会聚焦 React 19、Server Components、React Compiler、AI 集成、性能优化、安全性与无障碍等前沿话题，覆盖实战案例与底层原理。
- 🎓 提供 5+ 场免费及专业工作坊，主题包括现代 React 架构、Claude Code、TanStack AI、AI Agents 优化 Web 应用、React DevOps 等。
- 🌟 重量级讲者包括 Jack Herrington、Matt Pocock、Aurora Scharff、Ryan Skinner、Vercel 工程师等，还有来自 Google DeepMind、Meta、Wix、Apollo 的专家。
- 🎟️ 票务选项多样：Hybrid Full Ticket £540，Combo（含 TechLead Conf）£690，Remote Early Bird €180，以及 Multipass 订阅方案（月付 €17）。
- 🎁 早期购票（8 月 31 日前）可免费获得 Claude Code 工作坊资格；邀请 3 位朋友注册还可获赠免费远程门票。
- 🌍 GitNation 提供 100 个多元化奖学金名额，并为内容创作者提供合作机会，致力于打造包容性社区。
- 📅 活动还包括 MC 主持、项目委员会、线下派对、卡拉 OK 及丰富社交环节，帮助开发者拓展人脉、交流最佳实践。

---

### [介绍聊天代理 | 更新日志](https://trigger.dev/changelog/chat-agent?utm_source=fnf&utm_medium=newsletter&utm_campaign=august&utm_term=react-weekly&utm_content=chat-agent-launch)

**原文标题**: [Introducing chat agent | Changelog](https://trigger.dev/changelog/chat-agent?utm_source=fnf&utm_medium=newsletter&utm_campaign=august&utm_term=react-weekly&utm_content=chat-agent-launch)

Trigger.dev 推出了 chat.agent，一种用于构建持久化 AI 聊天体验的方案。每个会话运行在一台无超时的状态机器上，支持流式传输、崩溃恢复和跨请求内存保持。相比传统请求/响应后端，它提供真实 Linux 环境、快速首轮、等待零成本、内置可观测性，并继续复用 AI SDK，且已具备大规模生产验证，代码完全开源。

- 🤖 全新 chat agent：每次对话对应一台有状态机器，全程在后台休眠与唤醒，无需手动管理状态。
- 📝 极简后端实现：回合只需写成一个 Trigger.dev 任务，前端 useChat 直接对接，中间无需 API 路由。
- 🏆 生产验证：自 6 月已服务数百万会话，Arena 等团队采用，并获得正向评价。
- 🖥️ 真实 Linux 机器：可自由安装软件、执行 CLI（如 ffmpeg），按需选择 CPU 与内存规格。
- ⏳ 持久计算与流：单回合无超时，内存跨回合保留；刷新或崩溃后流可重放，会话始终可恢复。
- ⚡ 快速首轮：Head Start 功能在 agent 启动的同时于服务器执行首个 LLM 调用，显著降低首 token 延迟。
- 💤 等待不收费：工具可暂停回合等待人工审批，挂起期间不计费，可跨天等待。
- 📊 内置可观测性：每次回合均为 span，并提供 AI 指标仪表板，可追踪成本、token、延迟及模型明细。
- 🔌 沿用 AI SDK：服务端 streamText、客户端 useChat 不变，聊天历史保存在服务器，只传输新增消息。
- 🧠 高级能力：支持自定义 agent、原始会话原语、上下文压缩、prompt caching、版本化 prompts、MCP server 与 skills。
- 🧪 测试与扩展：可在单元测试中驱动真实回合；能作为任务集成队列、批处理、调度及 eval 流程。
- 💰 开源与定价：项目为 Apache 2.0 开源；费用按实际运行的计算时间结算，挂起状态完全免费。

---

