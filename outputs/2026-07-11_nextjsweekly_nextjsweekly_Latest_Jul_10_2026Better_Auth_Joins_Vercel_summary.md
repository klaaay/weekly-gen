### [Better Auth 加入 Vercel](https://better-auth.com/blog/better-auth-joins-vercel)

**原文标题**: [Better Auth is joining Vercel](https://better-auth.com/blog/better-auth-joins-vercel)

Better Auth 宣布加入 Vercel，以加速开源认证和代理工作流安全的发展。该项目始于三年前，由 Bereket Engida 创建，旨在提供一个框架无关、插件可扩展的认证框架，并已获得社区广泛支持。未来将专注于开源认证框架的维护和代理认证协议的研究。

- 🚀 Better Auth 加入 Vercel，共同推动开源认证和代理工作流安全
- 🔑 项目始于对多租户认证的需求，最初基于 NextAuth 构建
- 🛠️ 经过多次迭代，发布了框架无关的认证框架，支持插件扩展
- 🌟 社区反响热烈，获得开发者好评，并吸引了 YouTube 教程和博客文章
- 💼 通过 YC 孵化，获得 Peak XV 等投资，正式成立公司
- 🤝 收购了 Auth.js/NextAuth.js，整合资源继续维护
- 🧠 专注于代理认证协议，应对 AI 时代的安全挑战
- 🎯 未来将利用 Vercel 资源，深化开源认证框架和代理安全栈

---

### [GitHub - Blazity/next-migration-skills · GitHub](https://github.com/Blazity/next-migration-skills)

**原文标题**: [GitHub - Blazity/next-migration-skills · GitHub](https://github.com/Blazity/next-migration-skills)

本仓库提供了一个面向代理的工具包，用于将 Next.js 从 Pages Router 迁移到 App Router，基于 Skills.sh 构建。

- 📦 **安装方式**：通过 `npx skills add blazity/next-migration-skills` 命令即可快速安装。
- 🛠️ **核心技能**：包括 `nextjs-migration-toolkit`（AST 分析与转换基础）、`migration-assessment`（评估迁移就绪度）、`migration-planning`（制定分阶段迁移计划）等。
- 🔗 **依赖关系**：所有其他技能都依赖 `nextjs-migration-toolkit` 作为基础工具，安装时需注意路径引用。
- 🗂️ **架构清晰**：技能按功能分目录组织，如 `route-conversion`（路由转换）、`component-migration`（组件迁移）、`data-layer-migration`（数据层迁移）等。
- 🧪 **测试与评估**：包含 `tests/`（单元和集成测试）和 `evaluation/`（评估框架），确保迁移正确性。
- 📊 **语言组成**：主要使用 TypeScript（97.9%），辅以 Handlebars（1.8%）和 Shell（0.3%）。
- ⭐ **社区状态**：拥有 22 个星标，0 个 Fork，暂无发布版本或包。

---

### [不同的水合与渲染策略——Nechiu Dan](https://neciudan.dev/hydration-and-rendering-strategies)

**原文标题**: [Different hydration and rendering strategies — Neciu Dan](https://neciudan.dev/hydration-and-rendering-strategies)

该文章深入探讨了现代Web应用中的水合（hydration）与渲染策略，从静态生成到前沿的可恢复性技术，并提供了在不同场景下的选型建议。

- 📄 **静态生成 (SSG)**：在构建时预渲染HTML，从CDN直接提供，速度极快，但内容可能过时。通过增量静态再生 (ISR) 可在后台按间隔或按需更新。
- 🖥️ **客户端渲染 (CSR)**：发送空HTML壳，由浏览器下载并执行JavaScript构建UI。简单但首屏加载慢，对SEO不友好，可能导致白屏。
- 🖨️ **服务端渲染 (SSR)**：在服务端渲染HTML，发送给浏览器后由客户端“水合”为交互式应用。解决了白屏和SEO问题，但水合过程会重复工作，导致“看起来就绪”到“实际可用”之间的延迟。
- 🚰 **流式SSR**：通过`Suspense`将页面分块流式传输，让用户更快看到内容，无需等待最慢的组件。水合也变为按需、按优先级进行，但总下载的JavaScript量不变。
- 🏝️ **岛屿架构**：页面主体为静态HTML，只对交互部分（如评论区、搜索框）进行独立水合。未标记的部分永远不加载JavaScript，性能极佳，适合内容为主的网站。
- ⚛️ **React服务端组件 (RSC)**：组件仅在服务端运行，不向客户端发送代码，只发送序列化后的UI描述。大幅减小客户端包体积，可直接在组件内查询数据库。需注意“use client”蔓延和潜在的安全风险。
- 🔄 **TanStack Start**：采用客户端优先、可选的RSC模式。将RSC视为可通过HTTP获取的数据流，能无缝融入现有缓存工具。适合在现有SPA中逐步引入服务端渲染。
- ⚡ **细粒度响应式**：SolidJS、Svelte 5等框架采用信号机制，组件只运行一次，状态变化时直接更新特定DOM节点。水合成本极低，适合高频更新的交互式UI。
- 🧘 **可恢复性 (Resumability)**：Qwik框架的核心思想。将框架的执行状态序列化到HTML中，客户端无需重新执行任何水合代码。通过惰性加载交互代码，实现“零JavaScript”启动。
- 🚀 **Next.js 16.3 即时导航**：通过缓存组件和部分预取，让服务端驱动的应用也能实现类似SPA的即时导航体验。需要开发者对每个动态部分做出“流式/缓存/阻塞”的决策。
- 🧭 **如何选择**：内容网站选静态生成和岛屿架构；应用选React + RSC框架；特定性能瓶颈再考虑细粒度响应式或可恢复性；登录后的页面可用CSR。核心是匹配策略与页面的实际交互程度。

---

### [RFC：路由处理器中的WebSocket升级 · vercel/next.js · 讨论 #95514 · GitHub](https://github.com/vercel/next.js/discussions/95514)

**原文标题**: [RFC: WebSocket Upgrades in Route Handlers · vercel/next.js · Discussion #95514 · GitHub](https://github.com/vercel/next.js/discussions/95514)

概述摘要
- 🚀 提出在Next.js App Router路由处理器中提供原生WebSocket支持，使用`NextResponse.upgrade()` API。
- 🔐 处理器在握手前可检查请求，支持条件接受（如返回401/403）和设置响应头与Cookie。
- 📡 使用CrossWS库提供高级Peer和Message API，而非底层`ws.WebSocket`，支持订阅和发布。
- 🏠 自托管部署通过Node.js的`upgrade`事件处理，适配器需转发原始升级原语。
- 🎯 目标包括支持`route.ts`、保留路由控制流、与`next dev`/`next start`兼容，无需自定义服务器。
- ❌ 非目标包括Pages Router支持、Edge运行时、跨实例pub/sub或暴露原始`ws`对象。
- ⚙️ 响应语义：返回普通Response拒绝升级，返回`NextResponse.upgrade()`接受连接，钩子错误关闭连接并记录。
- 🧪 测试计划包括e2e套件、验证握手执行、钩子行为、路由重写、优雅关闭和适配器集成。

---

### [React 性能：实战指南](https://reactperf.dev/)

**原文标题**: [React Performance: A Field Guide](https://reactperf.dev/)

本文提供了一份全面的React性能优化指南，涵盖从浏览器渲染原理到具体优化技巧的40个步骤，帮助开发者识别并解决React应用中的性能瓶颈。

- ⚛️ **React渲染机制**：单个状态更新会级联触发所有子组件重新渲染，理解这一机制是性能优化的基础
- 🧠 **记忆化技术**：React.memo、useMemo和useCallback能精确控制组件重渲染，React编译器可自动生成这些优化代码
- 🔄 **组合模式**：将组件作为children prop传递可避免重渲染级联，无需使用React.memo
- ⚠️ **Context陷阱**：所有Context消费者会同时重渲染，可通过store-via-context模式解决
- 🔑 **Keys与协调**：使用索引作为key在列表重新排序时会引发问题，React依赖key来识别元素
- ⏳ **副作用管理**：useEffect容易导致无限循环、依赖缺失和双重挂载问题，需谨慎使用
- 🔒 **闭包与过期状态**：setTimeout和异步回调中常看到过期状态，可使用ref解决
- 📊 **状态管理选择**：当多个useState变得难以管理时，useReducer提供更好的状态管理方案
- 📍 **状态下沉**：将状态放在组件树中尽可能低的位置，避免不必要的全局重渲染
- ⚡ **并发渲染**：useTransition和useDeferredValue为渲染调度器提供优先级控制
- 🔄 **自动批处理**：React 18在异步边界自动批处理更新，需注意特定场景下的行为变化
- 🌀 **Suspense数据加载**：Suspense边界支持流式HTML和渐进式水合，提升加载性能
- 📡 **数据获取优化**：React Query提供缓存、去重和结构共享等关键模式
- ❌ **请求取消**：使用AbortController解决最常见的异步竞态问题——乱序响应
- 🖥️ **服务端组件**：Next.js、TanStack Start等框架中的RSC实现各有特点
- 📋 **长列表虚拟化**：超过几百条数据时，虚拟化技术将DOM元素从10000个减少到30个
- 👁️ **IntersectionObserver**：比滚动监听更高效，由浏览器主动通知元素可见性变化
- 🎨 **content-visibility**：通过CSS属性让浏览器跳过渲染屏幕外的子树
- ⏱️ **主线程调度**：防抖与节流有不同语义，需根据场景选择合适方案
- 🧵 **Web Workers**：200ms的计算任务就足以区分流畅UI和掉帧
- 🖼️ **requestAnimationFrame**：与setTimeout(16)不同，在120Hz显示器上错误使用会导致性能问题
- 🕐 **requestIdleCallback**：在帧间隙执行低优先级任务，不阻塞用户输入
- 📦 **打包优化**：import { x } from "lodash"可能仍会打包整个库，需注意tree-shaking效果
- ✂️ **代码分割**：路由级和组件级分割各有优劣，错误的分割边界会带来性能损失
- 🔗 **预加载与预取**：资源提示和fetchpriority可影响浏览器优先级
- 🖼️ **图片优化**：AVIF格式、srcset属性、懒加载和宽高比设置对CLS指标至关重要
- 🔤 **字体优化**：FOIT与FOUT的选择、font-display属性和size-adjust设置影响LCP指标
- 🖥️ **浏览器渲染路径**：理解HTML、CSS和JS如何组合成像素，以及性能预算分配
- 📐 **布局抖动**：读写交替模式会强制每帧执行30次同步布局
- 🎮 **GPU合成**：transform和opacity属性仅触发合成，而top和left会触发布局
- 📦 **CSS Containment**：通过contain属性告诉浏览器哪些变化可以局部处理
- 🎨 **CSS-in-JS开销**：每个css()调用在每次渲染时都执行序列化、哈希和插入操作
- 🎬 **动画优化**：优先选择仅触发合成的属性，避免全管道动画
- 🔄 **FLIP动画**：通过变换模拟布局变化，实现流畅的布局动画
- 🖼️ **视图过渡**：浏览器自动执行FLIP，支持SPA和页面间导航
- 🎯 **事件委托**：在父元素上设置一个监听器优于在子元素上设置一千个
- 💾 **内存泄漏**：定时器、事件监听器和订阅可能比创建它们的组件存活更久
- 📊 **性能API**：使用performance.mark和performance.measure进行性能测量
- 📈 **核心Web指标**：LCP、INP和CLS是Google报告的关键性能指标

---

### [AI SDK 7 现已发布 - Vercel](https://vercel.com/blog/ai-sdk-7)

**原文标题**: [AI SDK 7 is now available - Vercel](https://vercel.com/blog/ai-sdk-7)

AI SDK 7 正式发布，每周下载量超过1600万次，是构建AI应用的TypeScript SDK，支持多种模型提供商。

- 📊 **概述**：AI SDK 7 是构建AI应用的核心TypeScript库，每周下载量超1600万，Vercel的开源代理框架也基于此构建。
- 🧠 **开发代理**：新增推理控制、工具上下文、运行时上下文、文件上传和技能上传功能，支持MCP应用和终端UI。
- 🚀 **运行代理**：支持工具审批、持久化工作流代理、超时设置和沙箱支持，增强生产环境可靠性。
- 🔗 **集成代理框架**：通过HarnessAgent统一接口，可集成Claude Code、Codex、Deep Agents等第三方代理框架。
- 👁️ **观察代理**：重构遥测系统，支持OpenTelemetry、Node.js追踪通道、生命周期事件和性能统计。
- 🎤 **超越文本代理**：新增提供商无关的实时语音支持和视频生成功能。
- ⚙️ **快速上手**：使用`pnpm add ai@latest`安装，或通过`npx @ai-sdk/codemod v7`从v6迁移。
- 🤝 **社区贡献**：感谢Vercel核心团队和众多社区贡献者的共同努力。

---

### [GitHub - facebook/astryx：一个完全可定制且支持智能体的开源设计系统](https://github.com/facebook/astryx)

**原文标题**: [GitHub - facebook/astryx: An open source design system that's fully customizable and agent ready · GitHub](https://github.com/facebook/astryx)

Astryx 是 Meta 内部开发八年、现开源的 React 设计系统，支持 150+ 组件、主题定制、暗黑模式及 CLI，专为人与 AI 代理协同构建而设计。

- 🎨 **开源设计系统**：基于 React 和 StyleX，提供 150+ 无障碍组件、品牌级主题、暗黑模式及 CLI 工具
- 🔧 **无锁定架构**：组件内部使用 StyleX，但用户可通过 className 自由覆盖（Tailwind、CSS 模块等），无需额外构建插件
- 🧩 **开放内部结构**：组件支持任意层级组合，swizzle 功能可导出完整源码供用户自主修改
- 🌈 **主题自定义**：通过 CSS 自定义属性覆盖实现主题，无需分叉或包裹组件源码
- 🤖 **人机协同设计**：API、文档和 CLI 统一设计，确保人类开发者与 AI 助手使用相同工具和参考
- 📦 **快速入门**：通过 npm/pnpm/yarn 安装核心包和主题，仅需 CSS 导入和主题提供者即可运行
- 📚 **丰富包生态**：包括核心组件、CLI、构建插件、7 个预制主题、实验组件及图表库（图表尚在开发中）
- 🧭 **项目结构清晰**：包含示例应用、文档站点、Storybook、发布包及内部工具，遵循 Node 22+ 和 pnpm 11
- 📜 **开源许可**：采用 MIT 许可证，欢迎贡献，提供完整贡献指南

---

### [噫，真臭！介绍 react-stinky | Sascha Becker](https://saschb2b.com/blog/react-stinky)

**原文标题**: [Eww, That Stinks! Introducing react-stinky | Sascha Becker](https://saschb2b.com/blog/react-stinky)

## 概述总结
react-stinky 是一个 React 代码异味检测工具，能全面扫描组件、钩子或模块，识别问题并给出具体修复建议，同时通过智能过滤机制避免误报。

- 🧠 **全方位检测**：覆盖组件 API、状态流、副作用、结构、渲染、可访问性、TypeScript 和跨文件重复八大支柱
- 📊 **三级臭味评级**：Rancid（严重错误）、Funky（维护问题）、Whiff（轻微问题），帮助开发者按优先级处理
- 🔧 **提供具体修复**：每个发现都包含成本说明、前后对比修复示例和官方文档链接，而非笼统建议
- 🚫 **智能静默机制**：尊重原生 HTML 属性、库约定、配置对象属性等，避免产生噪音报告
- 🎯 **灵活作用域**：支持片段、文件、文件夹和仓库级别扫描，并诚实告知未检查的内容
- 🤝 **专注核心领域**：不处理记忆化（交给 React Compiler）和颜色字面量（交给主题工具），避免功能膨胀

---

### [GitHub - unlayer/elements：一次编写，React 实现。从同一组件树渲染电子邮件、网页和PDF。· GitHub](https://github.com/unlayer/elements)

**原文标题**: [GitHub - unlayer/elements: Write once in React. Render emails, web pages, and PDFs from the same component tree. · GitHub](https://github.com/unlayer/elements)

Unlayer Elements 是一個開源的 React 元件庫，可讓開發者「一次編寫，三處渲染」，將同一份元件樹轉換為電子郵件、網頁和 PDF 文件，大幅提升開發效率。

- 📧 **三合一渲染**：支援 Email（Outlook/Gmail 等）、Web（響應式網頁）和 Document（PDF 列印）三種輸出模式，取代 React Email、MJML 和 PDF 函式庫的組合。
- ⚛️ **React 開發者體驗**：與 React、Next.js、Remix 和 Server Components 相容，使用熟悉的 JSX 語法，無需學習新模板語言。
- 🎨 **可視化編輯器相容**：透過 `renderToJson()` 匯出設計 JSON，可與 Unlayer 拖放式編輯器雙向協作，開發者與非技術團隊皆可使用。
- 🧩 **豐富的元件庫**：包含 Email、Page、Document、Row、Column、Button、Heading、Paragraph、Image、Divider、Social、Menu、Table、Video、Html 等 15 種元件。
- 🧹 **乾淨的 HTML 輸出**：`renderToHtml()` 產生無 React 水合標記、無框架殘留的完整 HTML 文件，`renderToHtmlParts()` 可分別取得 head 和 body。
- 🪶 **輕量高效**：約 12KB gzipped（低於 60KB ESM），支援 Tree Shaking，零客戶端 JavaScript，適合效能敏感與伺服器端渲染場景。
- 🔒 **生產級品質**：通過快照測試、黃金模板測試、瀏覽器 E2E 測試、視覺漂移測試和 Next.js 整合測試，確保輸出穩定可靠。
- 📄 **PDF 生成**：可使用 Unlayer PDF 匯出服務或將 `<Document>` 的 HTML 傳遞給任何 HTML-to-PDF 函式庫。
- 🆓 **MIT 授權**：完全開源，無需 API 金鑰或帳號，無網路請求，無平台依賴，輸出 HTML 完全歸您所有。
- 🛠️ **自訂元件**：透過 `registerElementsTool()` 建立自訂工具，可在三種渲染模式中擁有完整控制權。

---

### [世博观察](https://expo.dev/solutions/expo-observe?utm_source=nextjsweekly&utm_medium=email&utm_campaign=observe-beta)

**原文标题**: [Expo Observe](https://expo.dev/solutions/expo-observe?utm_source=nextjsweekly&utm_medium=email&utm_campaign=observe-beta)

### 概述总结
Expo Observe 是一款深度集成于移动应用发布流程的性能监控工具，能自动将每个性能指标与具体构建或更新关联，帮助开发者快速发现回归问题，并通过AI实现一键排查。

- 🚀 **快速定位性能回归**：Observe 将每个性能指标与具体构建和更新绑定，让开发者几分钟内找到回归问题，而非数天。
- 📊 **自动捕获用户感知指标**：无需自定义追踪，自动测量TTI、冷启动、热启动、帧率下降和包加载时间等真实设备性能。
- 🏷️ **每个版本可视化标记**：每次发布在时间线上显示为标记，悬停可看差异，点击可查看该构建或OTA更新的所有事件。
- 🤖 **AI一键转交**：在仪表板一键操作，或从CLI输出JSON到Claude Code、Cursor等AI工具，获取基于真实会话的答案。
- 🔍 **深入排查慢会话**：按指标排序（慢速优先），深入单个会话查看设备、系统版本、国家、更新频道，并通过`<logEvent>`追踪关键用户流程。
- 🧩 **完整上下文传递**：Observe 在复制前预览AI提示，确保AI获得指标、受影响会话、构建和回归差异等完整信息，无需手动解释。
- 📈 **每个屏幕性能分析**：通过Expo Router集成，将交互时间按路由分解，帮助定位具体慢速屏幕，支持多选路由跨版本对比。
- 🌐 **全面覆盖所有设备**：自动捕获P50、P90、P99指标，涵盖低端硬件、旧系统版本、弱网络环境，无需自定义工具。
- 🔒 **隐私与采样控制**：收集匿名性能数据（无PII），支持采样率设置（0-1）和运行时禁用，确保隐私合规。
- ❓ **常见问题解答**：Observe 与Sentry/Datadog互补，专为Expo应用设计（SDK 55+），支持EAS构建和OTA更新。

---

### [龙湖](https://longho.dev/posts/react-compiler-is-a-retrofit/)

**原文标题**: [Long Ho](https://longho.dev/posts/react-compiler-is-a-retrofit/)

概述摘要：本文探讨了人工智能在医疗领域的应用，重点分析了其提升诊断效率、个性化治疗方案及数据隐私挑战等方面的关键影响。

- 🔬 提升诊断效率：AI通过分析医学影像和患者数据，能够快速识别疾病模式，辅助医生做出更准确的诊断。
- 💊 个性化治疗：基于大数据和机器学习，AI可针对患者基因、病史等特征，定制更有效的治疗方案。
- 🔒 数据隐私挑战：医疗数据的高度敏感性要求AI系统必须严格保护患者隐私，避免数据泄露和滥用。
- 🤖 自动化流程：AI可优化医院管理、药物研发等环节，减少人力成本并加速医疗创新。
- ⚖️ 伦理与监管：AI决策的透明性和责任归属问题需要明确的法规框架，以确保技术安全可靠。

---

### [为React编写自定义渲染器](https://www.callstack.com/blog/writing-custom-renderers-for-react)

**原文标题**: [Writing Custom Renderers for React](https://www.callstack.com/blog/writing-custom-renderers-for-react)

本文探讨了React渲染器的工作原理，以及作者为React Native Testing Library构建自定义测试渲染器的经验。

- 🎯 **React 19 弃用 RTR 催生新方案**：React Test Renderer (RTR) 被弃用后，React Native Testing Library 需要寻找长期替代方案，最终决定构建新的测试渲染器。
- 🧩 **React 渲染依赖三层树结构**：React 通过元素树、Fiber 树和平台视图树来管理 UI，并由 React、Reconciler 和 Renderer 三个包协作完成转换。
- ⚙️ **Reconciler 与 Renderer 通过 HostConfig 通信**：Renderer 需实现 `HostConfig` 接口（如 `createInstance`、`appendChild` 等），将 Reconciler 的通用操作转化为平台特定的视图更新。
- 🛠️ **测试渲染器简化了宿主实例树**：新渲染器使用轻量级对象（Container、Instance、TextInstance）存储节点信息，无需真实 UI 支持，便于测试断言。
- 🔥 **Fire Event API 面临兼容挑战**：为支持事件模拟，需通过 `unstable_fiber` 逃逸机制访问复合组件属性，这是迁移中的主要难点。
- 💡 **构建渲染器深化了对 React 的理解**：作者强调理解元素树、Fiber 树和宿主实例树的关系是核心，而 React 的并发、Suspense 等特性由 Reconciler 统一实现。

---

### [为什么 Drizzle ORM 一个月无法在 NPM 上发布新版本 | vlt /vōlt/](https://www.vlt.io/blog/packument-size-limits)

**原文标题**: [Why Drizzle ORM couldn't publish new releases on NPM for a month | vlt /vōlt/](https://www.vlt.io/blog/packument-size-limits)

### 概述总结

Drizzle ORM 因NPM包文档（packument）达到100MB限制而无法发布新版本长达一个月，最终通过NPM支持团队删除旧版本解决。本文解释了该限制的成因、影响及预防措施。

- 📦 **问题根源**：NPM的"packument"包含所有版本清单（manifest），每个Drizzle版本清单约131KB，763个版本即可达到100MB限制。
- 🚫 **自动发布加速问题**：Drizzle近期自动从Git提交发布快照版本，导致版本数量激增，更快触及限制。
- 🛑 **删除限制**：NPM禁止在发布72小时后删除版本，只能联系NPM团队手动处理。
- 📏 **自查方法**：使用`curl -s https://registry.npmjs.org/包名 | wc -c`命令可查看当前packument大小。
- 💡 **避免建议**：不发布所有开发版本，使用替代注册表存放快照，并监控packument大小。
- 🔧 **改进方向**：支持客户端按版本范围请求，减少传输数据量；镜像注册表通过白名单机制仅保留必要版本。

---

