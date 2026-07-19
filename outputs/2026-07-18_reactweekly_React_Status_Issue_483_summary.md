### [ReactBench](https://www.reactbench.com/)

**原文标题**: [ReactBench](https://www.reactbench.com/)

ReactBench 是一个评估编码智能体在实际 React 开发中表现的基准测试。传统测试只检查行为是否正确，但忽略了性能、可访问性和代码质量等关键问题。

- 📊 测试显示，即使是顶级模型（如 GPT 5.6 Sol）的 Pass@1 也仅达 43%，说明模型在真实 React 代码中仍有大量缺陷。
- 💰 评分与成本并非正相关，例如 Fable 5 成本高达 $9.05，但评分仅 41.2%，而 GPT 5.6 Sol 成本仅 $1.35，评分却更高。
- 🚨 模型生成的 React 代码易导致生产事故，包括：因 `useEffect` 错误引发的服务宕机、界面卡顿造成的收入损失，以及无障碍问题带来的法律风险。
- 🛠️ 基准测试包含 51 个真实任务，涵盖列拖拽调整大小、修复反模式、事件泄漏等实际场景。
- 🔒 为确保数据纯净，ReactBench 使用了 `reactbench-canary` 标识符，防止测试数据混入训练语料。

---

### [认识团队 – React](https://react.dev/community/team)

**原文标题**: [Meet the Team – React](https://react.dev/community/team)

React 团队由来自全球公司和社区的贡献者组成，工作按工作组划分，由领导委员会协调方向。

- 👥 **领导委员会成员**：包括 Andrew Clark、Jack Pope、Mofei Zhang 等，各自负责 Fiber、DOM、Compiler、DevX、React Native 等不同领域。
- 🧑‍💻 **工作组核心成员**：如 Dan Abramov、Josh Story、Lauren Tan 等，专注于 Docs & Community、Server、Compiler 等方向。
- 🏆 **顾问团队**：Eli White、Jason Bonta、Seth Webster 等提供战略指导。
- 🏁 **荣誉成员**：包括 Joe Savona、Sebastian Markbåge 等前核心贡献者。
- 📜 **更多信息**：过往团队成员和重要贡献者可查阅致谢页面。

---

### [AI代码审查 | CodeRabbit | 免费试用](https://www.coderabbit.ai/?utm_source=newsletter&utm_medium=email&utm_campaign=coderabbit_cooperpress&utm_term=cooperpressreact&dub_id=cQ7ovjUfBK1N7LdP)

**原文标题**: [AI Code Reviews | CodeRabbit | Try for Free.](https://www.coderabbit.ai/?utm_source=newsletter&utm_medium=email&utm_campaign=coderabbit_cooperpress&utm_term=cooperpressreact&dub_id=cQ7ovjUfBK1N7LdP)

概述总结
- 🐰 CodeRabbit的出现，让代码审查质量不再因人而异，统一了标准。
- 📋 过去，代码审查质量取决于审查者的个人水平。
- 🔄 现在，所有拉取请求都遵循相同的质量标准。

---

### [Guillermo Rauch在X上表示：“我很激动地欢迎两位开发者工具领域的传奇人物Pete Hunt（@floydophone）和Nick Schrock（@schrockn）加入Vercel。

Pete是Meta公司@reactjs的先驱之一。他早期就押注用⚛️ React驱动Instagram网页版，并在内部和外部推广这项技术。他——” / X](https://x.com/rauchg/status/2077870043833229692)

**原文标题**: [Guillermo Rauch on X: "I’m excited to welcome two legends of developer tools, Pete Hunt (@floydophone) and Nick Schrock (@schrockn), to Vercel.

Pete was one of the pioneers of @reactjs at Meta. He made an early bet to power Instagram Web with ⚛️ React, evangelizing it internally and externally. He" / X](https://x.com/rauchg/status/2077870043833229692)

Vercel 宣布两位开发者工具领域的传奇人物加入公司，Pete Hunt 将领导 Next.js 框架，Nick Schrock 将负责代理开发者体验。

- 🎉 欢迎 Pete Hunt 和 Nick Schrock 加入 Vercel
- ⚛️ Pete Hunt 是 React 早期推广者，曾推动 Instagram Web 使用 React
- 🚀 Pete 将领导 Frameworks 团队和 Next.js 项目
- 📊 Nick Schrock 是 GraphQL 的共同发明者，解决了 Facebook 规模的数据问题
- 🤖 Nick 将专注于代理开发者体验，推动自我改进软件的未来
- 💼 两位高管正在招聘，欢迎通过私信联系他们

---

### [Next.js 转向定期安全发布 - Socket](https://socket.dev/blog/nextjs-moves-to-scheduled-security-releases)

**原文标题**: [Next.js moves to scheduled security releases - Socket](https://socket.dev/blog/nextjs-moves-to-scheduled-security-releases)

概述摘要  
- 🐛 Suno 遭 Shai-Hulud 蠕虫攻击，源代码泄露  
- 🎵 泄露代码显示 Suno 使用流媒体抓取技术获取音乐片段训练 AI 模型  
- 🔓 此次入侵暴露了 AI 音乐初创公司的数据采集方式  
- ⚠️ 事件引发对 AI 训练数据来源合法性的关注

---

### [我维护Linaria已有六年。这是我构建新东西的原因——dx-styles博客](https://dx-styles.dev/blog/why-dx-styles/)

**原文标题**: [I've maintained Linaria for six years. Here's why I built something new â dx-styles blog](https://dx-styles.dev/blog/why-dx-styles/)

概述总结
- 🎯 作者维护Linaria六年，因运行时CSS-in-JS模式过时（如styled-components进入维护模式、Server Components不兼容）而创建新工具dx-styles
- ⚠️ Linaria两大核心问题：`styled(Component)`导致构建时依赖泄漏，以及缺乏对变体/插槽/主题等设计系统基础功能的一流支持
- 🚀 Pigment CSS经验表明：迁移现有代码库时构建速度可能慢10倍以上，静态评估是优化关键，但`styled(Component)`会破坏静态评估
- 💡 团队自建组件库时发现Linaria在设计系统场景（令牌、变体、多部件组件）中表现笨拙，最终决定从头构建
- 🛠️ dx-styles核心特性：静态CSS提取、类型安全的配方/令牌合约、无运行时/无Provider、支持React Server Components
- 🎁 额外惊喜：基于wyw-in-js处理器机制可同时静态执行应用逻辑，实现编译时宏功能
- 📜 承诺MIT开源、零未解决问题（通过AI代理自动化工单处理）、wyw-in-js@3有公开路线图但无时间表
- 🔗 提供StackBlitz演示、Next.js示例、从styled-components/Linaria/Pigment CSS迁移指南

---

### [dx-styles/docs/migration/from-linaria.md 在 main 分支 · dx-styles/dx-styles · GitHub](https://github.com/dx-styles/dx-styles/blob/main/docs/migration/from-linaria.md)

**原文标题**: [dx-styles/docs/migration/from-linaria.md at main · dx-styles/dx-styles · GitHub](https://github.com/dx-styles/dx-styles/blob/main/docs/migration/from-linaria.md)

### 概述摘要
从 Linaria 迁移到 dx-styles 的完整指南，涵盖设置、模式映射和逐步迁移策略。

- 🔄 **核心优势**：获得对象语法、类型化令牌、一等变体支持（recipe）、多部件组件（slotRecipe）、令牌合约替代手动CSS变量，以及可选的编译时RTL支持。
- ⚙️ **简易设置**：若Linaria 6+已通过@wyw-in-js/vite构建，只需安装dx-styles包并更新vite配置，单个插件即可同时支持两个库。
- 📋 **模式映射**：提供详细的转换对照表，包括模板→对象语法、styled组件→recipe+组件、插值常量→对象值、主题变量→createTokenContract等。
- 🎨 **模板转对象**：将Linaria的模板字面量css转换为dx-styles的对象语法，属性名变为驼峰式，值变为字符串或数字。
- 🧩 **styled组件**：dx-styles无元素工厂，需将Linaria的styled组件拆分为recipe和普通React组件，明确分离有限分支（变体）和连续值（assignVars）。
- 🔗 **组件选择器**：避免直接移植组件选择器插值，应使用slotRecipe或显式类名/数据属性来建模协调元素组。
- 🎭 **主题系统**：用createTokenContract创建类型化令牌合约，用createTheme定义主题，实现端到端类型安全的CSS变量管理。
- 📈 **增量迁移**：在现有wyw构建中添加dx-styles，逐文件迁移：模板css→对象css，styled→组件+recipe，类可自由组合（cx），最后移除@linaria依赖。
- ✅ **检查清单**：确保构建同时运行两个库、模板字面量已转换、无组件选择器插值、CSS变量已替换为令牌合约、最终移除Linaria依赖。

---

### [Next.js 中的缓存组件 - Certificates.dev](https://certificates.dev/blog/cache-components-in-nextjs)

**原文标题**: [Cache Components in Next.js - Certificates.dev](https://certificates.dev/blog/cache-components-in-nextjs)

### 概述摘要
Next.js 16 引入的 Cache Components 模型将缓存默认行为从“默认缓存”改为“默认动态”，开发者需通过 `"use cache"` 指令显式选择缓存，从而更精确地控制数据缓存策略。

- 🔄 **默认动态化**：`cacheComponents: true` 后，所有数据默认动态执行，仅通过 `"use cache"` 指令启用缓存，开发环境会标记未决策的数据。
- 🧩 **三种处理方式**：异步数据可通过 `<Suspense>` 流式加载、`"use cache"` 缓存，或 `export const instant = false` 阻塞渲染，框架在开发时提示未决数据。
- 📦 **灵活缓存范围**：`"use cache"` 可应用于文件、组件或函数级别，Next.js 自动根据函数身份和序列化参数生成缓存键，无需手动定义。
- ⏱️ **生命周期与失效**：`cacheLife` 设置缓存有效期（如 `'hours'`），`cacheTag` 结合 `revalidateTag`/`updateTag` 实现按需失效，支持后台刷新和即时更新。
- 🔒 **请求API隔离**：缓存作用域内禁止读取 `cookies()`、`headers()` 等请求级数据，需在外部读取后作为参数传入，避免用户数据泄露。
- 🚀 **即时导航支持**：预渲染的缓存壳（如产品目录）可被客户端复用，实现无服务器往返的即时页面切换，推荐部分通过流式加载。
- 🧹 **简化API**：旧版 `dynamic`、`revalidate`、`unstable_cache` 等配置被取代，缓存默认基于内存，持久化需配置缓存处理器或使用 `"use cache: remote"`。

---

### [杰克·赫林顿想不出再选择Next.js的理由 - YouTube](https://www.youtube.com/watch?v=PpyepQmLDTY)

**原文标题**: [Jack Herrington Can’t Think of a Reason to Choose Next.js Anymore - YouTube](https://www.youtube.com/watch?v=PpyepQmLDTY)

本頁面列出了 YouTube 平台相關的各項連結與資訊，包括公司資訊、政策、合作與法律條款。

- 📰 新聞中心：提供 YouTube 的最新消息與公告
- ©️ 版權：說明平台上的版權相關規範與保護機制
- 📞 聯絡我們：提供用戶與 YouTube 聯繫的管道
- 🎬 創作者：為內容創作者提供的資源與支援
- 📢 刊登廣告：說明在 YouTube 上投放廣告的方式與選項
- 👨‍💻 開發人員：提供 API 與技術文件給開發者
- 📜 條款：列出使用 YouTube 服務的相關條款
- 🔒 私隱：說明用戶資料的收集與使用方式
- 🛡️ 政策及安全：涵蓋平台的安全規範與社群準則
- ⚙️ YouTube 的運作方式：解釋推薦系統與平台機制
- 🧪 測試新功能：介紹正在測試中的新功能
- ©️ 2026 Google LLC：版權宣告與所屬公司資訊

---

### [框架战争已经结束。为什么没有人能取代React - YouTube](https://www.youtube.com/watch?v=mxRjJPoWBE4)

**原文标题**: [The Framework wars are over. Why no one dethroned React - YouTube](https://www.youtube.com/watch?v=mxRjJPoWBE4)

本頁面為 YouTube 平台的相關資訊總覽，涵蓋法律、政策、合作與功能等面向。

- 📰 新聞中心：提供 YouTube 官方新聞與最新動態
- ©️ 版權：說明內容版權相關規範與保護機制
- 📞 聯絡我們：提供使用者與 YouTube 團隊聯繫的管道
- 🎨 創作者：專為內容創作者提供的資源與支援
- 📢 刊登廣告：說明在 YouTube 上投放廣告的選項與方式
- 👨‍💻 開發人員：提供 API 與技術文件給開發者使用
- 📜 條款：列出使用 YouTube 服務需遵守的條款與條件
- 🔒 私隱：說明 YouTube 如何收集與處理使用者資料
- 🛡️ 政策及安全：涵蓋平台安全規範與內容審查政策
- ⚙️ YouTube 的運作方式：解釋推薦系統、演算法等平台運作機制
- 🧪 測試新功能：介紹 YouTube 正在測試中的新功能
- 📅 © 2026 Google LLC：顯示版權年份與所屬公司

---

### [使用RAG和流式传输在React Native中构建ChatGPT风格的AI聊天应用 — Margelo博客](https://blog.margelo.com/building-native-llm-chat-app-with-rag)

**原文标题**: [Building a ChatGPT-Style AI Chat App in React Native with RAG & Streaming — Margelo Blog](https://blog.margelo.com/building-native-llm-chat-app-with-rag)

本文展示了如何使用React Native构建一个具有原生体验的AI聊天应用MargeloChat，该应用集成了RAG技术、流畅动画和原生性能优化。

- 🎯 **原生体验的RN聊天应用**：使用React Native构建，通过Reanimated动画、原生键盘控制器和原生列表组件，实现与Swift/Kotlin原生应用相媲美的流畅交互体验。
- 💎 **液态玻璃浮动输入框**：利用@callstack/liquid-glass库实现iOS 26+的真实玻璃材质效果，并在旧设备上优雅降级为纯色圆角视图。
- ⌨️ **键盘跟随与动画同步**：通过react-native-keyboard-controller的KeyboardStickyView实现输入框与键盘的精确同步，所有动画均在UI线程运行，无JS线程延迟。
- 📎 **附件展开动画**：使用Reanimated的withTiming驱动高度和透明度动画，配合onLayout测量实际内容高度，实现附件缩略图条的平滑展开与收起。
- 🚀 **消息发送与流式渲染**：采用Reanimated的SlideInDown入场动画，结合Legend List的anchoredEndSpace功能将消息锚定在顶部，并使用react-native-enriched-markdown原生渲染流式Markdown内容。
- 💡 **推理过程展示**：通过可折叠的推理摘要行和react-native-true-sheet原生底部弹窗，展示AI模型的思考过程，弹窗支持自动高度和全屏两种模式。
- 🔌 **原生WebSocket通信**：使用react-native-nitro-websockets建立与OpenAI Responses API的WebSocket连接，支持工具调用循环，并在应用启动前预连接以节省150-250ms。
- 📚 **RAG知识库检索**：通过OpenAI函数调用触发Pinecone向量搜索，使用react-native-nitro-fetch进行原生HTTP请求，确保检索过程不影响UI线程性能。
- 📱 **原生页面切换**：使用react-native-pager-view实现聊天与最近对话列表之间的原生滑动切换，手势跟踪精确到像素级别。
- ⚡ **性能优化要点**：所有动画在UI线程运行、WebSocket数据原生解码、Markdown原生解析渲染、HTTP请求使用原生fetch，在iPhone 16上保持57-60fps流畅度。

---

### [2026年7月 - 介绍 shadcn/typeset - shadcn/ui](https://ui.shadcn.com/docs/changelog/2026-07-typeset)

**原文标题**: [July 2026 - Introducing shadcn/typeset - shadcn/ui](https://ui.shadcn.com/docs/changelog/2026-07-typeset)

### 概述总结
shadcn/typeset 是一个全新的排版系统，通过单一CSS文件为HTML和Markdown内容提供统一的样式解决方案，支持流式渲染和灵活的自定义配置。

- 📄 **核心功能**：通过添加 `typeset` 类名，自动为所有HTML元素（标题、段落、列表等）应用统一样式
- 🎨 **自定义控制**：提供 `--typeset-size`、`--typeset-leading`、`--typeset-flow` 三个CSS变量，可针对不同场景（如聊天、文档）调整排版节奏
- ⚡ **流式渲染优化**：专为流式内容设计，新增内容不会影响已有元素的样式
- 🔧 **零依赖**：无需额外包或配置层，CSS文件直接存在于项目中
- 🏗️ **组件生态**：包含70+组件（如Accordion、Data Table、Dialog等），支持CLI、主题、暗黑模式、Monorepo等特性
- 📚 **集成支持**：兼容React Hook Form、TanStack Form、AI SDK、Figma等工具
- 🆕 **最新发布**：2026年7月推出shadcn/typeset，提供在线构建器和完整文档

---

### [排版 - shadcn/ui](https://ui.shadcn.com/typeset)

**原文标题**: [Typeset - shadcn/ui](https://ui.shadcn.com/typeset)

本篇文章探讨了人工智能在医疗领域的应用现状与未来潜力，重点分析了AI如何辅助诊断、个性化治疗及药物研发，同时指出了数据隐私、算法偏见和监管挑战等关键问题。

- 🩺 **AI辅助诊断**：通过分析医学影像和患者数据，AI能提高疾病检测的准确性和效率，尤其在癌症和眼科疾病方面表现突出。
- 💊 **个性化治疗**：基于基因组学和患者历史数据，AI可定制治疗方案，提升疗效并减少副作用。
- 🔬 **药物研发加速**：AI通过模拟分子相互作用，大幅缩短新药发现和临床试验周期，降低成本。
- 🔒 **数据隐私风险**：医疗数据的高度敏感性要求严格保护患者隐私，但现有系统仍存在泄露和滥用隐患。
- ⚖️ **算法偏见问题**：训练数据的不平衡可能导致AI对特定人群的诊断不准确，需加强数据多样性和公平性审核。
- 🏛️ **监管挑战**：AI医疗产品的审批标准尚未统一，需要制定更清晰的法规以确保安全性和有效性。

---

### [错误](https://dsssp.io/)

**原文标题**: [Error](https://dsssp.io/)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='dsssp.io', port=443): Max retries exceeded with url: / (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [错误](https://dsssp.io/demo/)

**原文标题**: [Error](https://dsssp.io/demo/)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='dsssp.io', port=443): Max retries exceeded with url: /demo/ (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [react-拖放区](https://react-dropzone.js.org/)

**原文标题**: [react-dropzone](https://react-dropzone.js.org/)

该库是一个基于React Hooks的文件拖拽上传组件，支持文件夹拖拽、文件验证和自定义UI，提供简洁的API和多种安装方式。

- 📦 支持npm、pnpm、yarn、bun等多种包管理器安装
- 🖱️ 提供拖拽上传区域组件，支持文件夹拖拽
- ✅ 内置文件验证功能，可自定义校验规则
- 🎨 完全控制HTML标记，灵活定制上传界面
- 🔗 提供入门示例和GitHub源码链接

---

### [基本示例 – react-dropzone](https://react-dropzone.js.org/examples/basic/)

**原文标题**: [Basic example – react-dropzone](https://react-dropzone.js.org/examples/basic/)

### 概述总结
本文介绍了`useDropzone`钩子的基本用法，包括如何创建拖放区域、处理文件选择以及禁用状态下的实现。

- 📦 **核心功能**：`useDropzone`钩子绑定必要的事件处理程序，实现拖放文件功能
- 🖱️ **根元素配置**：使用`getRootProps()`获取拖放所需的属性，可应用于任意元素
- 📄 **输入元素绑定**：通过`getInputProps()`获取点击和键盘行为所需的属性，需绑定到`<input>`元素
- 📂 **文件夹支持**：默认支持文件夹拖放，详情可参考`file-selector`文档
- 🚫 **禁用状态**：通过设置`disabled: true`参数可禁用拖放功能
- 💻 **代码示例**：展示了Basic组件和Disabled组件的完整实现，包括文件列表渲染

---

### [GitHub - nomcopter/react-mosaic: 一个React平铺窗口管理器 · GitHub](https://github.com/nomcopter/react-mosaic)

**原文标题**: [GitHub - nomcopter/react-mosaic: A React tiling window manager · GitHub](https://github.com/nomcopter/react-mosaic)

react-mosaic 是一个基于 React 的平铺窗口管理器，灵感来自 IDE 窗口管理和 i3 风格布局，支持拖拽调整大小和重新排列面板。

- 📦 安装简单：通过 npm 安装 `react-mosaic-component`，并导入 CSS 样式文件即可快速使用。
- 🚀 快速上手：用 `Mosaic` 和 `MosaicWindow` 组件，15 行代码即可创建带拖拽分隔线和工具栏的两面板布局。
- 🌳 N 叉树布局：支持任意数量的子节点，而非仅限二叉树，提供更灵活的布局结构。
- 📑 标签页优先：标签容器是原生节点类型，而非附加功能，提升用户体验。
- 🎛️ 受控与非受控模式：可通过 `value` + `onChange` 控制树结构，或使用 `initialValue` 让组件自动管理。
- 🖱️ 拖放功能：基于 react-dnd 构建，支持 HTML5 和触摸后端，实现流畅的拖拽操作。
- 🎨 主题定制：支持 Blueprint 主题，自带默认 CSS 主题和 CSS 变量，方便自定义样式。
- 🔄 零配置迁移：v6 版本的二叉树布局在渲染时自动转换，并提供 `convertLegacyToNary` 函数用于显式升级。
- 🤝 开源贡献：遵循 Apache License 2.0，欢迎通过 GitHub 提交问题、拉取请求或参与开发。

---

### [无脑](https://brainless.swerdlow.dev/)

**原文标题**: [brainless](https://brainless.swerdlow.dev/)

### 概述总结
本文展示了多个AI编程助手（Claude Code、Codex、Grok）通过命令行界面，将"brainless pricing"组件集成到网站中的操作流程。

- 💻 **Claude Code** 通过 `bunx shadcn add brainless/pricing` 命令添加了1个代码块和2个文件，并在页面中插入 `<Pricing tiers={TIERS} />` 组件。
- 🛠️ **Codex** 读取营销页面并编辑 `components/pricing.tsx` 文件（+22行），随后运行 `pnpm build` 构建验证。
- 🤖 **Grok** 打开营销页面并写入定价组件，在 `page.tsx` 中将 `<Features />` 替换为 `<Pricing tiers={TIERS} />`，整个操作耗时9.2秒。
- ⚡ **统一操作模式**：所有工具均通过命令行界面执行"添加brainless定价区块"任务，展示了AI辅助开发的高效性。

---

### [积木 · 无脑](https://brainless.swerdlow.dev/blocks#pied-piper-onboarding)

**原文标题**: [Blocks · brainless](https://brainless.swerdlow.dev/blocks#pied-piper-onboarding)

本页面展示了多个AI编程助手的完整交互界面，包括Claude Code、Codex、Grok等，以及一个Pied Piper注册流程组件。

- 🖥️ **Claude Code界面**：展示完整的Claude Code交互回合，包含计划、工具调用、代码差异、审批和运行状态行。
- 🤖 **Codex CLI界面**：展示完整的Codex CLI交互回合，包含消息、执行行和工作状态，底部有命令输入区。
- 🧠 **Grok CLI界面**：展示完整的Grok CLI交互回合，包含状态栏、思考过程、工具卡片、写入预览和审批步骤。
- ⏳ **Grok中间状态**：展示Grok CLI在思考、写入和工作中的中间状态，包含流式思考和停止按钮。
- 🚀 **Pied Piper注册流程**：展示交互式注册界面，包含标题、助手输入、思考过程和真实输入框，用于收集姓名和意图。

---

### [组件 · 无脑](https://brainless.swerdlow.dev/components#claude-diff)

**原文标题**: [Components · brainless](https://brainless.swerdlow.dev/components#claude-diff)

本文档收录了 Claude Code、Codex 和 Grok 三大 CLI 工具的全部 UI 组件，每个组件都作为可访问的 React 组件重新构建，并附有预览、使用说明和安装命令。

- 🧩 **Claude Code 组件**：包含从欢迎框 (Claude Header)、对话消息 (Claude Message)、思考状态 (Claude Thinking)、工具调用 (Claude Tool Call)、待办列表 (Claude Todo List)、代码差异 (Claude Diff)、权限确认 (Claude Permission)、斜杠菜单 (Claude Slash Menu) 到输入编辑器 (Claude Prompt) 的完整交互流程。
- 🖥️ **Codex 组件**：覆盖了启动卡片 (Codex Header)、对话消息 (Codex Message)、执行状态 (Codex Exec)、工作状态 (Codex Working)、全屏差异页面 (Codex Diff)、权限选择器 (Codex Permissions)、斜杠菜单 (Codex Slash Menu) 和输入提示 (Codex Prompt) 等核心界面元素。
- 🤖 **Grok 组件**：提供了丰富的界面组件，包括启动卡片 (Grok Header)、状态栏 (Grok Status)、对话消息 (Grok Message)、事件线 (Grok Event)、思考过程 (Grok Thought)、工作状态 (Grok Thinking 和 Grok Working)、工具操作 (Grok Tool)、写入编辑 (Grok Write)、权限卡片 (Grok Permission)、计划审批 (Grok Plan)、项目选择器 (Grok Project Picker)、快捷键 (Grok Shortcuts)、设置 (Grok Settings)、回合结束 (Grok Turn End)、斜杠菜单 (Grok Slash Menu) 和输入提示 (Grok Prompt)。
- 📦 **安装方式统一**：所有组件均支持通过 `bunx --bun shadcn@latest add` 命令安装，并提供了对应的 Prompt 文档链接，方便开发者快速集成到项目中。

---

### [发布 v3.4.0 · FortAwesome/react-fontawesome · GitHub](https://github.com/FortAwesome/react-fontawesome/releases/tag/v3.4.0)

**原文标题**: [Release v3.4.0 · FortAwesome/react-fontawesome · GitHub](https://github.com/FortAwesome/react-fontawesome/releases/tag/v3.4.0)

以下是您提供的 GitHub 发布页面的内容摘要：

该页面为 FortAwesome/react-fontawesome 仓库的 v3.4.0 版本发布记录，展示了版本更新详情及页面加载错误信息。

- 🚀 新增功能：支持 FontAwesome v7.3.0 引入的新动画效果（#651）
- 🔧 依赖更新：升级 fast-uri 依赖至 3.1.2 版本（a193c11）
- 📦 开发依赖：更新开发依赖至 FA 7.3.0 版本（cc540d8）
- ⚠️ 页面错误：加载时出现错误，需重新加载页面
- 🔄 版本对比：提供 v3.3.1 至 v3.4.0 的完整变更日志

---

### [Font Awesome 7.3 来了！——博客 Awesome](https://blog.fontawesome.com/font-awesome-7-3-release/)

**原文标题**: [Font Awesome 7.3 Is Here!—Blog Awesome](https://blog.fontawesome.com/font-awesome-7-3-release/)

Font Awesome 7.3 已发布！本次更新带来了三个全新的 Pro+ 图标包、两种 Slab 风格、六种新动画以及多项修复和改进。

- 🎉 **三个全新 Pro+ 图标包**：Pixel（像素风格）、Mosaic（马赛克风格）和 Vellum（层次叠加风格），为项目增添个性与深度。
- 🧱 **新增 Slab 风格**：Slab Duo 和 Slab Press Duo，为图标增加第二层颜色和立体感。
- 🌀 **六种全新动画**：包括 fa-wag、fa-swing、fa-float、fa-buzz、fa-spin-snap 和 fa-jello，基于经典动画原则设计，支持无障碍设置。
- 🖼️ **新增填充工具**：fa-canvas-square 和 fa-canvas-roomy，为图标提供更整洁或更宽松的显示空间，与 Figma 组件同步。
- 🔧 **修复与改进**：包含大量错误修复和全新图标，详情见更新日志。

---

### [发布 11.0.0-beta.2 · preactjs/preact · GitHub](https://github.com/preactjs/preact/releases/tag/11.0.0-beta.2)

**原文标题**: [Release 11.0.0-beta.2 · preactjs/preact · GitHub](https://github.com/preactjs/preact/releases/tag/11.0.0-beta.2)

Preact 11.0.0-beta.2 版本发布，包含多项改进和修复。

- 🔄 从 v10.x 版本向前移植了多项修复，包括 #5139、#5122、#5089 和 #5053
- 💧 实现了流式水合（hydration）RFC（#5035）
- 🏷️ 移除了 select 元素类型中错误的 'type' 属性（#5097），并接受 Signalish 作为输入类型（#5095）
- 🐛 修复了多个问题，包括 Suspense 水合子元素恢复（#5146）、节点类型检查（#5119）、Suspense 未定义属性重验证（#5133）、部分渲染子树错误恢复（#5120）、useId 在异步 Suspense 中的稳定性（#5108）、子树效果刷新（#5055）、内存泄漏热点（#5116）、水合恢复中 null 多余 DOM 子元素（#5112）、边缘情况 bug（#5092）以及 cloneElement 中保留假值 key 和 ref（#5082）
- ⚡ 性能优化：使用 Symbols 作为事件时钟键（#5143）、优化 compat 的 shallowDiffers（#4780）、减少冗余分配和写入（#5115）、使用 .push.apply（#5024）
- 🛠️ 维护工作：升级 GitHub Actions（#5110）、修复 vitest 配置拼写错误（#5111）、使用 npm 分阶段发布（#5100）、强化可信发布工作流（#5099）、添加三级赞助商标志（#5093）、添加主分支可信发布工作流（#5086）、添加 chai 作为开发依赖以支持 pnpm 安装（#5043）

---

### [从 Preact 10.x 升级 – Preact 指南 v11](https://preactjs.com/guide/v11/upgrade-guide/)

**原文标题**: [Upgrading from Preact 10.x – Preact Guide v11](https://preactjs.com/guide/v11/upgrade-guide/)

Preact 11 是从 Preact 10.x 升级的最小破坏性版本，主要更新了浏览器和 TypeScript 支持版本，并清理了遗留代码。

- 📦 **浏览器支持升级**：Preact 11 支持 Chrome >= 40、Safari >= 9、Firefox >= 36、Edge >= 12，旧浏览器需使用 polyfill。
- 🔧 **TypeScript 版本要求**：最低支持 TS v5.1，以利用 JSX 类型改进。
- 📁 **ESM 包分发格式变更**：ESM 包使用 `.mjs` 扩展名，简化工具链问题。
- 💧 **Hydration 2.0 改进**：允许异步边界返回 0 或 2+ 个 DOM 节点，提升组件设计灵活性。
- 🔍 **`Object.is` 用于钩子参数**：更接近 React 行为，支持 `NaN` 作为状态值或依赖项。
- 🔄 **默认转发 ref**：不再需要 `forwardRef`，ref 可直接作为 prop 使用。
- 🎨 **自动 `px` 后缀移至 `preact/compat`**：核心不再自动添加 `px`，需通过 compat 层启用。
- 📦 **`defaultProps` 移至 `preact/compat`**：减少核心负担，适应函数组件趋势。
- ❌ **移除 `render()` 的 `replaceNode` 参数**：改用 `preact-root-fragment` 包实现类似功能。
- 🗑️ **移除 `Component.base` 属性**：可通过 `this.__v.__e` 访问 DOM 节点。
- 🚫 **移除 `SuspenseList`**：因实现不完整，从 `preact/compat` 中移除。
- 📝 **`useRef` 要求初始值**：简化类型推断，避免类型问题。
- 🏷️ **JSX 命名空间缩减**：仅保留 TypeScript 必需类型，其余移至 `preact` 命名空间。

---

### [GitHub - astoilkov/use-local-storage-state: 在localStorage中持久化数据的React钩子](https://github.com/astoilkov/use-local-storage-state)

**原文标题**: [GitHub - astoilkov/use-local-storage-state: React hook that persists data in localStorage · GitHub](https://github.com/astoilkov/use-local-storage-state)

use-local-storage-state 是一个用于在 localStorage 中持久化数据的 React 钩子，支持 SSR、React 18 并发渲染和 React 19，并提供内存回退机制。

- 📦 安装简单：支持 React 18 及以上版本（`npm install use-local-storage-state`），React 17 及以下使用 `@17` 版本。
- 🛠️ 核心功能：提供 `useLocalStorageState` 钩子，返回 `[value, setValue, { removeItem, isPersistent }]`，类似 `useState`。
- 💾 数据持久化：默认将数据存储到 `localStorage`，并处理 `Window` 的 `storage` 事件，支持跨标签页、窗口和 iframe 同步。
- ⚠️ 错误回退：当 `localStorage` 不可用时，自动使用内存存储，并通过 `isPersistent` 属性通知用户。
- 🗑️ 数据重置：`removeItem()` 方法可删除 `localStorage` 中的键并重置为默认值。
- 🔧 配置选项：支持 `defaultValue`、`defaultServerValue`、`storageSync`（默认启用同步）和 `serializer`（默认使用 JSON，可替换为 superjson 等）。
- 🎯 适用场景：适合需要持久化用户数据的 React 应用，如待办列表、表单等。
- 📚 相关项目：提供 `use-storage-state`（支持多种存储 API）、`use-session-storage-state`（sessionStorage）和 `use-db`（IndexedDB）等扩展。

---

### [react-dropdown — 适用于React的无障碍下拉菜单](https://fraserxu.github.io/react-dropdown/)

**原文标题**: [react-dropdown — Accessible dropdown for React](https://fraserxu.github.io/react-dropdown/)

概述总结
- 📝 文章主要讨论了人工智能在医疗领域的应用，包括诊断辅助、药物研发和患者监护等方面。
- 🔬 重点介绍了AI如何通过分析医学影像提高疾病检测的准确性和效率。
- 💊 提到了AI在加速新药开发过程中的作用，例如预测药物分子特性。
- 🏥 强调了AI在远程患者监护和个性化治疗方案中的潜力。
- ⚠️ 同时指出了数据隐私、算法偏见和监管挑战等关键问题。

---

### [错误](https://react-joyride.com/)

**原文标题**: [Error](https://react-joyride.com/)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='react-joyride.com', port=443): Max retries exceeded with url: / (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [发布 v2.9.0 · Shopify/react-native-skia · GitHub](https://github.com/Shopify/react-native-skia/releases/tag/v2.9.0)

**原文标题**: [Release v2.9.0 · Shopify/react-native-skia · GitHub](https://github.com/Shopify/react-native-skia/releases/tag/v2.9.0)

以下是您提供的 Shopify/react-native-skia 仓库 v2.9.0 发布说明的摘要：

react-native-skia v2.9.0 版本发布，包含多项错误修复和新功能，提升稳定性与兼容性。

- 🌎 修复 ES 模块互操作中字体/图片资源的加载问题
- 🌐 在 Web 端实现 Font.measureText 方法
- 🗿 修复 graphite 版本的发布流程
- 🤖 在 OpenGL 上下文或表面无法创建时优雅失败，避免崩溃
- 📝 统一 matchFont 和 Paragraph 字体样式类型

---

### [适用于任何规模的时间序列工作负载的Postgres。| Tiger Data](https://www.tigerdata.com/go/trial?utm_source=content-syndication&utm_medium=referral&utm_campaign=react-status-newsletter)

**原文标题**: [Postgres for time-series workloads at any scale. | Tiger Data](https://www.tigerdata.com/go/trial?utm_source=content-syndication&utm_medium=referral&utm_campaign=react-status-newsletter)

Tiger Cloud 提供可扩展的 Postgres 时序数据服务，支持大规模工作负载，并为企业提供高可用性和合规性。

- 📊 单服务可处理每天3万亿指标、3 PB数据和1万亿数据点
- 💰 新用户注册即获$1000信用额度（30天有效），无需信用卡
- 🔄 支持读写分离，最多10个节点副本集，搭配分层SSD/S3存储实现无限扩展
- ⚡ 计算与存储分离，独立扩展，避免为闲置容量付费
- 🛡️ 多可用区集群自动故障转移，支持时间点恢复和跨区域备份
- 🔒 符合SOC 2、HIPAA和GDPR标准，提供加密、SSO、RBAC和审计日志
- 📈 深度可观测性：查询钻取和仪表盘，集成CloudWatch、Datadog、Prometheus
- 🚀 几分钟内完成数据库部署，支持SQL、CLI、Terraform、Cursor或Claude Code管理
- 🤝 与主流云提供商和Postgres生态系统集成
- 🏢 企业级服务：合同SLA、区域数据隔离、24/7全球专家支持

---

### [TanStack 对比 Next.js 对比 React Router 对比 Astro 对比 Vue 对比 Angular 对比 Expo 对比 Svelte 对比 Vite 对比 React - NPM 下载统计与趋势 | 包对比](https://tanstack.com/stats/npm?packageGroups=%5B%7B%22label%22%3A%22TanStack%22%2C%22packages%22%3A%5B%7B%22name%22%3A%22%40tanstack%2Fquery-core%22%7D%2C%7B%22name%22%3A%22react-query%22%7D%2C%7B%22name%22%3A%22%40tanstack%2Ftable-core%22%7D%2C%7B%22name%22%3A%22react-table%22%7D%2C%7B%22name%22%3A%22%40tanstack%2Frouter-core%22%7D%2C%7B%22name%22%3A%22%40tanstack%2Fstart-client-core%22%7D%2C%7B%22name%22%3A%22%40tanstack%2Fform-core%22%7D%2C%7B%22name%22%3A%22%40tanstack%2Fvirtual-core%22%7D%2C%7B%22name%22%3A%22react-virtual%22%7D%2C%7B%22name%22%3A%22%40tanstack%2Fdb%22%7D%2C%7B%22name%22%3A%22%40tanstack%2Fpacer%22%7D%2C%7B%22name%22%3A%22%40tanstack%2Fai%22%7D%2C%7B%22name%22%3A%22%40tanstack%2Fintent%22%7D%2C%7B%22name%22%3A%22%40tanstack%2Fstore%22%2C%22hidden%22%3Atrue%7D%5D%2C%22color%22%3A%22%2301a7b9%22%7D%2C%7B%22label%22%3A%22Next.js%22%2C%22packages%22%3A%5B%7B%22name%22%3A%22next%22%7D%2C%7B%22name%22%3A%22ai%22%7D%2C%7B%22name%22%3A%22workflow%22%7D%5D%2C%22color%22%3A%22%236d6a6a%22%7D%2C%7B%22label%22%3A%22React+Router%22%2C%22packages%22%3A%5B%7B%22name%22%3A%22react-router%22%7D%2C%7B%22name%22%3A%22%40remix-run%2Freact%22%7D%2C%7B%22name%22%3A%22remix%22%7D%5D%2C%22color%22%3A%22%23ff7580%22%7D%2C%7B%22label%22%3A%22Astro%22%2C%22packages%22%3A%5B%7B%22name%22%3A%22astro%22%7D%5D%2C%22color%22%3A%22%23BC52EE%22%7D%2C%7B%22label%22%3A%22Vue%22%2C%22packages%22%3A%5B%7B%22name%22%3A%22vue%22%7D%5D%2C%22color%22%3A%22%236aaf04%22%7D%2C%7B%22label%22%3A%22Angular%22%2C%22packages%22%3A%5B%7B%22name%22%3A%22%40angular%2Fcore%22%7D%2C%7B%22name%22%3A%22angular%22%7D%5D%2C%22color%22%3A%22%23DD0031%22%7D%2C%7B%22label%22%3A%22Expo%22%2C%22packages%22%3A%5B%7B%22name%22%3A%22expo%22%7D%5D%2C%22color%22%3A%22%23F59E0B%22%7D%2C%7B%22packages%22%3A%5B%7B%22name%22%3A%22svelte%22%7D%5D%7D%2C%7B%22packages%22%3A%5B%7B%22name%22%3A%22vite%22%7D%5D%7D%2C%7B%22label%22%3A%22React%22%2C%22packages%22%3A%5B%7B%22name%22%3A%22react%22%2C%22hidden%22%3Atrue%7D%5D%2C%22color%22%3A%22%2361DAFB%22%2C%22baseline%22%3Atrue%2C%22baselineLabel%22%3A%22React%22%7D%5D&range=1825-days&transform=none&binType=weekly&viewMode=history&chartType=line&barSort=value&bucketOffset=0&playbackIntervalMs=350&playbackLoop=false&playbackPlaying=false&showDataMode=all&normalizeBaseline=true&showBaseline=false&showLegend=false&height=400)

**原文标题**: [TanStack vs Next.js vs React Router vs Astro vs Vue vs Angular vs Expo vs svelte vs vite vs React - NPM Download Stats & Trends | Compare Packages](https://tanstack.com/stats/npm?packageGroups=%5B%7B%22label%22%3A%22TanStack%22%2C%22packages%22%3A%5B%7B%22name%22%3A%22%40tanstack%2Fquery-core%22%7D%2C%7B%22name%22%3A%22react-query%22%7D%2C%7B%22name%22%3A%22%40tanstack%2Ftable-core%22%7D%2C%7B%22name%22%3A%22react-table%22%7D%2C%7B%22name%22%3A%22%40tanstack%2Frouter-core%22%7D%2C%7B%22name%22%3A%22%40tanstack%2Fstart-client-core%22%7D%2C%7B%22name%22%3A%22%40tanstack%2Fform-core%22%7D%2C%7B%22name%22%3A%22%40tanstack%2Fvirtual-core%22%7D%2C%7B%22name%22%3A%22react-virtual%22%7D%2C%7B%22name%22%3A%22%40tanstack%2Fdb%22%7D%2C%7B%22name%22%3A%22%40tanstack%2Fpacer%22%7D%2C%7B%22name%22%3A%22%40tanstack%2Fai%22%7D%2C%7B%22name%22%3A%22%40tanstack%2Fintent%22%7D%2C%7B%22name%22%3A%22%40tanstack%2Fstore%22%2C%22hidden%22%3Atrue%7D%5D%2C%22color%22%3A%22%2301a7b9%22%7D%2C%7B%22label%22%3A%22Next.js%22%2C%22packages%22%3A%5B%7B%22name%22%3A%22next%22%7D%2C%7B%22name%22%3A%22ai%22%7D%2C%7B%22name%22%3A%22workflow%22%7D%5D%2C%22color%22%3A%22%236d6a6a%22%7D%2C%7B%22label%22%3A%22React+Router%22%2C%22packages%22%3A%5B%7B%22name%22%3A%22react-router%22%7D%2C%7B%22name%22%3A%22%40remix-run%2Freact%22%7D%2C%7B%22name%22%3A%22remix%22%7D%5D%2C%22color%22%3A%22%23ff7580%22%7D%2C%7B%22label%22%3A%22Astro%22%2C%22packages%22%3A%5B%7B%22name%22%3A%22astro%22%7D%5D%2C%22color%22%3A%22%23BC52EE%22%7D%2C%7B%22label%22%3A%22Vue%22%2C%22packages%22%3A%5B%7B%22name%22%3A%22vue%22%7D%5D%2C%22color%22%3A%22%236aaf04%22%7D%2C%7B%22label%22%3A%22Angular%22%2C%22packages%22%3A%5B%7B%22name%22%3A%22%40angular%2Fcore%22%7D%2C%7B%22name%22%3A%22angular%22%7D%5D%2C%22color%22%3A%22%23DD0031%22%7D%2C%7B%22label%22%3A%22Expo%22%2C%22packages%22%3A%5B%7B%22name%22%3A%22expo%22%7D%5D%2C%22color%22%3A%22%23F59E0B%22%7D%2C%7B%22packages%22%3A%5B%7B%22name%22%3A%22svelte%22%7D%5D%7D%2C%7B%22packages%22%3A%5B%7B%22name%22%3A%22vite%22%7D%5D%7D%2C%7B%22label%22%3A%22React%22%2C%22packages%22%3A%5B%7B%22name%22%3A%22react%22%2C%22hidden%22%3Atrue%7D%5D%2C%22color%22%3A%22%2361DAFB%22%2C%22baseline%22%3Atrue%2C%22baselineLabel%22%3A%22React%22%7D%5D&range=1825-days&transform=none&binType=weekly&viewMode=history&chartType=line&barSort=value&bucketOffset=0&playbackIntervalMs=350&playbackLoop=false&playbackPlaying=false&showDataMode=all&normalizeBaseline=true&showBaseline=false&showLegend=false&height=400)

TanStack 是一个提供多种开源 JavaScript 库和工具的生态系统，涵盖框架、数据管理、UI/UX、性能优化和工具链等领域，并支持 NPM 下载统计对比。

- 📊 **NPM 下载统计**：提供交互式图表，可对比 TanStack、Next.js、React Router 等主流库的下载趋势，支持自定义时间范围和基线比较。
- 🛠️ **核心库分类**：包括框架（Start、Router）、数据管理（Query、DB、Store、AI）、UI/UX（Table、Form、Hotkeys）、性能（Virtual、Pacer）和工具（Devtools、Config、CLI、Intent）。
- 🌐 **社区与资源**：提供 Discord、GitHub 社区支持，以及博客、YouTube 频道和专业工作坊，帮助开发者学习和协作。
- 🛒 **产品与支持**：提供官方周边商品、合作伙伴计划、企业支持和 OSS 赞助，确保项目可持续发展。
- 📈 **高级对比功能**：支持组合多个包为单一趋势线（如迁移跟踪），并包含缓存加速、历史数据回溯（自 2015 年）等特性。

---

