### [React 文摘：电子邮件通讯](https://reactdigest.net/)

**原文标题**: [React Digest: Email Newsletter](https://reactdigest.net/)

《React Digest》是一份专为 React 开发者精心策划的周报，汇集精选文章与简短摘要，帮助开发者高效获取有价值的内容。

- 📰 每周为 22,525 名前端工程师推送一封精选邮件  
- 🎯 精选文章搭配简短摘要，节省筛选时间  
- 🧠 每周学习新知识，紧跟技术演进  
- 👍 读者好评：内容实用、更新及时（如 React 并发模式专题）  
- 🌍 订阅者覆盖全球前端工程师  
- © 由 Bonobo Press 于 2013-2025 年发行，含隐私与广告政策

---

### [微小模块的暴政：过度模块化如何损害现代前端开发 | JavaScript 简明英语](https://javascript.plainenglish.io/the-tyranny-of-tiny-modules-d42cbd8e1e17?gi=bf3f7717e7b1)

**原文标题**: [The Tyranny of Tiny Modules: Why Over-Modularization Hurts Modern Frontend Development | JavaScript in Plain English](https://javascript.plainenglish.io/the-tyranny-of-tiny-modules-d42cbd8e1e17?gi=bf3f7717e7b1)

前端开发中过度模块化的问题  

- 🧩 当前 React 和 Next.js 代码库中存在一种不成文的规定：组件必须保持小巧，超过 250 行就会被要求拆分或“抽象化”。  
- 🏗️ 表面上，这种追求模块化的做法带来了整洁性，但也导致文件夹结构围绕微组件和`index.ts`文件构建。  
- 📚 这种趋势源于可读性、可复用性和可测试性的理想，受到《代码整洁之道》、原子设计等理念的影响。  
- 🔄 社区普遍认为大文件是问题，应拆分为可复用的部分，教程和论坛进一步强化了这一观念。  
- 📦 使用`index.ts`（桶文件）来简化导入路径成为流行做法，例如从`import Button from '@/components/Button/Button.tsx'`简化为`import { Button } from '@/components'`。  
- 🏗️ 许多项目模板（尤其是旧版 Next.js 和“防弹”React 架构）鼓励广泛使用桶文件以提供简洁的接口。

---

### [Requestly——面向开发与测试的强大 API 模拟与测试工具](https://requestly.com/?utm_source=newsletter&utm_medium=pr&utm_platform&utm_content=pr&utm_campaign=PR-Apr-2025-Requestly&utm_campaigncode=701OW00000MFPsnYAH&utm_term=reactdigest)

**原文标题**: [Requestly – A Powerful API Mocking and Testing Tool for Developers and QAs](https://requestly.com/?utm_source=newsletter&utm_medium=pr&utm_platform&utm_content=pr&utm_campaign=PR-Apr-2025-Requestly&utm_campaigncode=701OW00000MFPsnYAH&utm_term=reactdigest)

Requestly 是一款强大的开源 HTTP 拦截和模拟工具，支持实时拦截、记录和修改 HTTP 请求，适用于前端开发、API 测试和移动应用调试。  

- 🚀 **功能概述**：拦截、修改和模拟 HTTP/HTTPS 请求，支持 URL 重定向、请求头修改和 API 响应覆盖。  
- 🖥️ **桌面专用**：需在桌面浏览器或 Mac 应用上使用，提供 Chrome 扩展和 Mac 客户端。  
- ⚡ **高效轻量**：Chrome 扩展一键安装，Mac 应用支持移动端（Android/iOS）流量拦截。  
- 📊 **API Mocking**：快速创建自定义 API 模拟，支持 REST 和 GraphQL，可本地运行并共享给团队。  
- 🔧 **团队协作**：提供共享工作区、Git 同步和即时链接分享功能，提升团队效率。  
- 🔒 **企业级安全**：SOC-II 合规、SSO 集成、角色权限控制和数据加密，确保数据安全。  
- 🌟 **用户口碑**：获 200,000+ 开发者信赖，包括 Adobe、Autodesk 等企业用户，Chrome 商店评分 4.4⭐。  
- 📱 **移动开发支持**：解决 iOS/Android/Electron 等环境的网络请求调试难题。  
- 🎥 **会话记录**：捕获网络流量和屏幕操作，便于问题复现和文档共享。  
- 💡 **客户评价**：被誉为“前端开发神器”，替代 Charles Proxy 和 Postman，显著提升工作效率。

---

### [🎉 打造你的个人语音 AI 助手，掌控所有应用⚡ - DEV 开发者社区](https://dev.to/composiodev/build-your-own-personal-voice-ai-agent-to-control-all-your-apps-2dfa)

**原文标题**: [🎉 Build Your Own Personal Voice AI Agent to Control All Your Apps⚡ - DEV Community](https://dev.to/composiodev/build-your-own-personal-voice-ai-agent-to-control-all-your-apps-2dfa)

### 概述  
本文详细介绍了如何使用 Next.js 和 Composio 构建一个语音控制的 AI 助手，能够通过语音指令操作 Gmail、Notion、Google Sheets 等应用。  

### 关键点  
- 🎤 **语音识别与 AI 控制**：通过语音指令控制应用，无需键盘操作。  
- 🛠️ **技术栈**：使用 Next.js、React、TailwindCSS、LangChain 和 OpenAI 等技术。  
- 📦 **依赖安装**：包括`composio-core`、`zustand`、`react-speech-recognition`等关键库。  
- 🔑 **Composio 配置**：需要 API 密钥和 CLI 工具来集成应用。  
- 🎨 **UI 组件**：使用 Shadcn/UI 构建界面，包括聊天消息、设置模态框等。  
- 🔄 **逻辑实现**：包括语音识别、工具调用、错误处理和消息验证。  
- 🚀 **项目演示**：展示了如何通过语音指令操作 Gmail 和 Google Sheets。  

### 详细步骤  
1. **初始化项目**：使用 Next.js 和 TypeScript 创建项目。  
2. **安装依赖**：添加必要的库和工具。  
3. **配置 Composio**：获取 API 密钥并设置集成。  
4. **构建 UI**：实现聊天界面、语音输入和设置管理。  
5. **实现逻辑**：处理语音识别、工具调用和消息传递。  
6. **测试与优化**：确保功能完整并优化用户体验。  

### 结论  
通过本文的指导，开发者可以构建一个功能强大的语音控制 AI 助手，提升工作效率和用户体验。

---

### [多选组件演示 | shadcn/ui + Next.js 15](https://multi-select-component-demo.vercel.app/)

**原文标题**: [MultiSelect Component Demo | shadcn/ui + Next.js 15](https://multi-select-component-demo.vercel.app/)

这是一个关于 MultiSelect 组件的交互式示例和使用说明。

- 🔍 探索 MultiSelect 组件的不同用例，包括多选、搜索功能和各种场景处理
- 💻 预设选项示例：展示已选中的 JavaScript 和 TypeScript 编程语言
- ⏳ 加载状态演示：通过骨架占位符显示 5 秒的加载效果
- 🛠️ 使用代码示例：提供如何在项目中实现 MultiSelect 组件的具体代码
- 📝 包含状态管理：示例中展示了如何使用 useState 管理选中项和加载状态
- 🖥️ 框架选项示例：包含 Next.js、React 和 Vue.js 等前端框架作为可选项

---

### [学习指南：React 中的数据获取](https://reactpractice.dev/articles/study-guide-data-fetching-in-react/)

**原文标题**: [Study guide: Data fetching in React](https://reactpractice.dev/articles/study-guide-data-fetching-in-react/)

React 数据获取学习指南：从入门到进阶的分阶段指导  

- 🎯 **入门阶段**：初学 React 时，先用 `useEffect` 和 Fetch API 理解基础数据获取，区分“用户点击触发”和“页面加载触发”场景。  
  - ✅ 任务示例：构建电影搜索页（点击获取）或 Hacker News 热门文章列表（页面加载获取）。  
  - 📚 资源：MDN Fetch API 教程、React Hooks 数据获取指南。  

- 🛠️ **进阶阶段**：掌握生产级实践，用 React Query 替代 `useEffect`，解决手动处理加载/错误状态、请求竞态等问题。  
  - ✅ 任务示例：用 React Query 构建公共假期应用或 GitHub 仓库搜索。  
  - 📚 资源：React Query 优势解析、快速入门文档。  

- 🚀 **实战阶段**：熟练使用 React Query 处理数据更新与缓存失效（如 CRUD 应用），理解“陈旧数据”默认行为。  
  - ✅ 任务示例：仿 Google Keep 的便签应用。  
  - 📚 资源：突变（Mutations）指南、缓存失效策略。  

- 🌊 **深入优化**：解决高阶问题（如请求瀑布流、竞态条件），参考 Nadia 的长文深度解析性能优化与竞态修复。  
  - 📚 资源：React 高性能数据获取、竞态条件案例分析。  

- 🌐 **扩展探索**：按需学习服务端数据获取（如 Next.js、React Router）、替代工具（RTK Query、SWR）或新兴技术（React Server Components、`use` API）。  
  - 📚 资源：React 数据获取方式全景、现代架构策略讨论。  

（注：文末推广内容未纳入摘要）

---

### [前端设计模式必备知识 - The Miners](https://blog.codeminer42.com/what-you-need-to-know-about-frontend-design-patterns/)

**原文标题**: [What you need to know about frontend design patterns - The Miners](https://blog.codeminer42.com/what-you-need-to-know-about-frontend-design-patterns/)

概述：本文介绍了前端设计模式的概念，重点讨论了 React 中的自定义钩子（Custom Hooks）模式，并通过实例展示了如何通过自定义钩子优化代码结构、提高可重用性和可维护性。

- 🛠️ 设计模式是解决常见问题的通用方案，不能直接复制但可适应具体场景。  
- 🔄 使用设计模式能提升代码组织性、可读性和可维护性，促进团队协作。  
- ⚛️ 前端开发中，React 的自定义钩子是一种常见设计模式，用于封装可复用的逻辑。  
- 📦 自定义钩子可分离业务逻辑与 UI，避免代码重复，例如加载状态和 API 错误处理。  
- 💰 示例 1：通过`useProducts`钩子集中管理数据获取、加载和错误状态，简化组件代码。  
- 🌍 示例 2：`useCurrency`钩子统一处理多国货币格式化，减少重复代码。  
- ✅ 自定义钩子的优势：逻辑复用、职责分离、代码更清晰且易于测试和维护。  
- 🚀 结论：合理应用设计模式（如自定义钩子）能提升项目质量和团队协作效率。

---

### [让 JavaScript 中的正则表达式更易用的小技巧](https://2ality.com/2025/06/javascript-regexp-tips.html)

**原文标题**: [Tips for making regular expressions easier to use in JavaScript](https://2ality.com/2025/06/javascript-regexp-tips.html)

概述  
本文介绍了在 JavaScript 中使正则表达式更易用的多种技巧，包括使用/v 标志、命名捕获组、添加注释和空白以提高可读性，以及通过测试和文档示例确保正确性。  

- 🚀 **使用/v 标志**：提供更少特性和更多功能，如支持多码位字符和字符类集合操作。  
- 🔤 **按字母顺序排列标志**：例如/pattern/giv，保持一致性并符合 JavaScript 的显示方式。  
- 🏷️ **命名捕获组**：通过命名组提高可读性，减少外部文档依赖。  
- 📝 **添加注释和空白**：使用 Regex+ 库的 regex 模板标签，支持忽略空白和行内注释（#），提升可读性。  
- 🧪 **编写测试**：通过测试验证正则表达式的功能，确保其按预期工作。  
- 📚 **文档示例**：在文档中提供匹配示例，帮助理解正则表达式的用途。  
- 🔄 **模式复用**：通过 Regex+ 库的插值功能，复用正则表达式片段，减少冗余。  
- 🛠️ **无库实现空白忽略**：使用 String.raw 和.replaceAll() 手动移除空白，模拟忽略空白功能。  
- 🎯 **结论**：通过合理使用空白、注释和命名组，正则表达式可读性大幅提升，接近代码的书写方式。

---

### [Ecma 国际批准 ECMAScript 2025：有哪些新变化？](https://2ality.com/2025/06/ecmascript-2025.html)

**原文标题**: [Ecma International approves ECMAScript 2025: What’s new?](https://2ality.com/2025/06/ecmascript-2025.html)

ECMA 国际已批准 ECMAScript 2025 语言规范，正式成为标准。以下是新特性的概述：

- 🎉 **ECMAScript 2025 获批**：2025 年 6 月 25 日，第 129 届 Ecma 大会批准了该规范。  
- 📥 **导入属性和 JSON 模块**：支持通过`import with`语法导入非 JavaScript 资源（如 JSON）。  
- 🔄 **迭代器辅助方法**：新增`filter`、`map`、`drop`等方法，支持链式操作和惰性计算。  
- 🧩 **新 Set 方法**：包括集合运算（`union`、`intersection`）和关系检查（`isSubsetOf`）。  
- 🛡️ **RegExp.escape()**：转义文本以安全用于正则表达式。  
- 🏷️ **正则表达式内联标志**：局部应用标志（如`i`）到部分模式。  
- 🔖 **重复命名捕获组**：允许在不同分支使用相同组名。  
- ⏳ **Promise.try()**：包装可能同步抛出的代码，启动 Promise 链。  
- 🔢 **16 位浮点数支持**：新增`Float16Array`类型和`Math.f16round()`等方法。  
- 📚 **免费电子书**：作者提供在线书籍《Exploring JavaScript (ES2025 Edition)》详解新特性。  

编辑团队包括 Shu-yu Guo、Michael Ficarra 和 Kevin Gibbons。

---

### [JavaScript 新动态 | Deno](https://deno.com/blog/updates-from-tc39)

**原文标题**: [What's coming to JavaScript | Deno](https://deno.com/blog/updates-from-tc39)

Deno 致力于推动 JavaScript 生态发展，参与 TC39 标准制定，近期有 9 项提案进入不同阶段，涵盖资源管理、异步数组处理、错误检测等功能优化，旨在提升开发效率和代码安全性。

- 🚀 **TC39 提案进展**：9 项提案分属 4 个阶段，从初步构思（Stage 0）到完全标准化（Stage 4）。  
- 🔄 **Stage 4 特性**：  
  - `using`声明：自动资源清理（如文件句柄），支持同步/异步释放（`Symbol.dispose`/`Symbol.asyncDispose`）。  
  - `Array.fromAsync`：异步可迭代对象转数组，简化异步数据收集。  
  - `Error.isError`：可靠检测错误对象（包括跨域或子类错误）。  
- 🛡️ **Stage 3 特性**：  
  - 不可变`ArrayBuffer`：通过`transferToImmutable()`和`sliceToImmutable()`确保二进制数据安全共享。  
- 🎲 **Stage 2 特性**：  
  - `Random.Seeded`：可复现的伪随机数生成器（指定种子值）。  
  - `Number.prototype.clamp`：限制数值范围，避免`Math.min/max`嵌套。  
- 📊 **Stage 1 特性**：  
  - 保留尾随零：`Intl.NumberFormat`新增格式化选项，支持货币等场景。  
  - 标准化值比较：为测试框架提供一致的差异输出。  
  - `Random`命名空间：新增随机数生成、数组采样/洗牌等方法，减少常见错误。  
- 🌐 **Deno 的实践**：  
  - 已集成`using`管理资源（如 HTTP 服务自动关闭）。  
  - 计划利用不可变`ArrayBuffer`优化 API 性能（如`Deno.writeFile`）。  
- ⏭️ **下一步**：TC39 将于 9 月下旬继续讨论提案，Deno 持续推动 Web 标准落地（如异步上下文传播）。

---

### [理解 CSS 的 corner-shape 属性及超椭圆的强大之处——Frontend Masters 博客](https://frontendmasters.com/blog/understanding-css-corner-shape-and-the-power-of-the-superellipse/)

**原文标题**: [Understanding CSS corner-shape and the Power of the Superellipse – Frontend Masters Blog](https://frontendmasters.com/blog/understanding-css-corner-shape-and-the-power-of-the-superellipse/)

CSS 的`corner-shape`属性为网页设计带来了全新的几何形状控制能力，扩展了传统的`border-radius`功能。

- 🎨 **基础背景**：`border-radius`属性在过去十多年中用于创建圆角，但其功能局限于椭圆曲线。
- 🆕 **新特性介绍**：`corner-shape`属性作为`border-radius`的补充，定义了曲线的外观，提供了多种预设形状如圆形、方形、凹形等。
- 🛠️ **多种形状创建**：通过结合`border-radius`和`corner-shape`，可以轻松创建菱形、六边形等复杂形状。
- 🔢 **多值应用**：`border-radius`和`corner-shape`均支持多值输入，为设计提供了更多可能性。
- 🎭 **动画与过渡**：`corner-shape`属性支持动画和过渡效果，可以平滑地从一个形状转换到另一个形状。
- ✨ **超级椭圆的力量**：`superellipse()`函数允许更精细地控制形状，通过调整参数可以创建从圆形到方形的各种过渡形态。
- 📐 **数学背景**：超级椭圆基于 Gabriel Lamé的数学公式，CSS 通过简化使其更易用。
- 🚀 **未来展望**：虽然目前`superellipse()`功能有限，但未来可能会支持更多参数，进一步扩展设计可能性。
- 📢 **社区互动**：鼓励开发者尝试这一新特性，分享创意，推动其在日常设计中的应用。

---

### [使用 CSS oklch() 函数生成颜色 | Go Make Things](https://gomakethings.com/generating-colors-with-the-css-oklch-function/)

**原文标题**: [Generating colors with the CSS oklch() function | Go Make Things](https://gomakethings.com/generating-colors-with-the-css-oklch-function/)

以下是符合您要求的总结内容：

CSS 的 oklch() 函数是一种基于 Oklab 色彩空间的 CSS 方法，通过输入亮度、色度和色调参数来生成颜色。它简化了创建可访问颜色调色板的过程，并支持相对颜色转换。通过调整亮度和色度，可以轻松创建一系列颜色变体，而无需手动生成多个十六进制值。此外，结合 CSS 的 calc() 函数，可以动态调整颜色的饱和度，使颜色管理更加灵活和高效。

- 🌈 CSS 的 oklch() 函数基于 Oklab 色彩空间生成颜色  
- 🎨 通过亮度、色度和色调参数定义颜色  
- 🔄 支持相对颜色转换，简化颜色调整  
- 🖌️ 简化创建可访问颜色调色板的过程  
- 📊 动态调整亮度和色度生成颜色变体  
- ➕ 结合 calc() 函数动态调整饱和度  
- 🛠️ 已在 Kelp 主题生成器中应用此方法

---

### [理解 React 重新渲染：触发原因及其重要性](https://shramko.dev/blog/react-rerender)

**原文标题**: [Understanding React Re-Renders: What Triggers Them and Why They Matter](https://shramko.dev/blog/react-rerender)

React Re-Renders 系列文章，探讨了 React 重渲染机制及其性能优化策略，适合有一定 React 基础的开发者深入学习。

- 🚀 作者 Andy 拥有六年 React 经验，发现即使是熟练开发者也可能对 React 底层机制理解不足，影响代码质量和性能。  
- 📚 现有学习资源多面向初学者，高级内容稀缺，因此推出本系列填补知识空白。  
- ⚡ 理解重渲染机制对性能至关重要，需掌握触发条件、传播路径及影响。  
- 🐢 案例中，在顶层组件添加状态导致整个应用重渲染，出现明显延迟，突显问题严重性。  
- 🔍 默认情况下，状态变更会触发组件及其子组件全部重渲染，但不会向上传播。  
- 🛑 使用 React.memo 可中断重渲染流程，但需注意其复杂性和适用场景。  
- 🧩 更优方案是将状态及相关组件封装为独立小组件（状态下沉），显著提升性能。  
- ✨ 通过 ButtonWithModalDialog 组件重构，快速解决性能问题，展示组合技术的威力。  
- 🔗 文末推荐延伸阅读：自定义 Hook 陷阱、约定式提交和 JS 命名规范等话题。

---

### [编程文摘：电子邮件通讯](https://programmingdigest.net/?utm_source=web-archive&utm_campaign=react)

**原文标题**: [Programming Digest: Email Newsletter](https://programmingdigest.net/?utm_source=web-archive&utm_campaign=react)

《Programming Digest》是一份专为软件工程师精心挑选的每周通讯，提供精选文章和简短摘要，帮助读者节省时间并每周学习新知识。  

- 📧 每周一封电子邮件，超过 18,521 名软件工程师订阅  
- 📖 精选文章配简短摘要，节省寻找优质内容的时间  
- 🎯 每周学习新知识，满足持续学习需求  
- 💬 读者反馈积极，认为内容实用且具有启发性  
- 🌍 订阅者遍布全球，来自不同公司和背景  
- ©️ 由 Bonobo Press 发行，涵盖 2013-2025 年

---

### [科技领导力：电子邮件通讯](https://leadershipintech.com/?utm_source=web-archive&utm_campaign=react)

**原文标题**: [Leadership in Tech: Email Newsletter](https://leadershipintech.com/?utm_source=web-archive&utm_campaign=react)

科技领导力周刊概述  
- 📰 精心策划的每周通讯，面向 CTO、工程经理和高级工程师，助力成为更优秀的领导者  
- 👥 已有超过 27,011 名工程领导者订阅，每周一封邮件  
- 📚 精选文章附简短摘要，节省寻找优质内容的时间  
- 🌱 每周学习新知识，持续提升领导力技能  
- 💬 读者好评：内容精准，涵盖架构讨论、会议规划及沟通技巧等，尤其推荐关于授权的重要性的文章  
- 🌍 来自全球科技领导者的选择，由 Bonobo Press 出品

---

### [C#文摘：电子邮件通讯](https://csharpdigest.net/?utm_source=web-archive&utm_campaign=react)

**原文标题**: [C# Digest: Email Newsletter](https://csharpdigest.net/?utm_source=web-archive&utm_campaign=react)

C# Digest 是一份专为 .NET 开发者精心策划的每周通讯，提供精选文章和简短摘要，帮助开发者节省时间并每周学习新知识。

- 📧 超过 19,905 名 C# 工程师订阅这份每周电子邮件  
- 📖 阅读精选文章并附有简短摘要  
- ⏳ 节省寻找有价值内容的时间  
- 🌱 每周学习新知识  
- 💬 读者反馈：  
  - 🏢 部分内容已在实际工作中应用  
  - 🔍 发现了标准功能标志和 LINQ 的新知识  
  - ❤️ 推荐了《操作结果模式》一文，并迁移了 Azure Function  
- 🌍 读者来自全球各地的 .NET 工程师  
- ©️ 由 Bonobo Press 2013-2025 年发布

---

### [让开发者与时俱进——Bonobo 出版社](https://bonobopress.com/)

**原文标题**: [Keeping developers up to date â Bonobo Press](https://bonobopress.com/)

Bonobo Press 是一家自 2013 年起为软件开发者、IT 专业人士和技术专家提供最新资讯的出版商，拥有超过 88,000 名订阅用户。

- 📧 提供精选的每周新闻简报，服务于软件开发者、工程经理、技术主管和 CTO，内容简洁高效，深受技术人士喜爱。  
- 📢 提供广告服务，帮助广告主精准触达软件工程师、团队领导、工程经理、CTO 及 IT 决策者等目标受众。  
- 📞 欢迎通过联系页面进行咨询、提出建议或洽谈广告合作。  
- ©️ 2013-2025 年版权所有，保留所有权利。

---

### [往期通讯：第 1 页](https://reactdigest.net/newsletters)

**原文标题**: [Past Newsletters: Page 1](https://reactdigest.net/newsletters)

以下是 React Digest 的摘要列表：

- 📰 2025 年 7 月 6 日：探讨 React 组件模块化哲学、个人 AI 代理构建及数据获取技术，涵盖前端设计模式和 MultiSelect 组件用例。
- ⚡ 2025 年 6 月 29 日：优化 React 性能，介绍 Zero-UI、MCP 服务器连接，以及使用 gaps 替代 margins 和 Server Components 在 Expo 中的作用。
- ✋ 2025 年 6 月 22 日：实时手势识别在视频会议中的应用，比较 React 数据获取方法，创建自定义 useState 钩子，探讨本地优先数据策略和 React 的 ViewTransition。
- 🔄 2025 年 6 月 15 日：细粒度响应式编程，避免 Next.js 中的 props drilling，将 URL 搜索参数视为状态，并在 React 中重现 Clash of Clans 机制。
- 🛠️ 2025 年 6 月 8 日：现代 React 框架的复杂性分析，API 使用指南，Progressive JSON 等创新技术，以及 React 和 Remix 的未来发展。
- 🔄 2025 年 6 月 1 日：与 Dan Abramov 探讨高效数据获取，构建“长按删除”组件，TanStack Router 的现代路由解决方案，React 错误边界和 Puck 可视化编辑器。
- 🎯 2025 年 5 月 25 日：使用 flushSync 掌握焦点管理，并发渲染的力量，构建自定义 TanStack Query，RSC 限制和 AI 辅助 React 开发的实用见解。
- 🔐 2025 年 5 月 18 日：React Router 中的 OpenAuth，自定义渲染器，依赖反转原则，React 上下文效率的真相，以及 React Server Components 的静态站点生成。
- 🏗️ 2025 年 5 月 11 日：复杂应用中的数据获取架构，颜色方案切换实现，媒体查询变化的自定义钩子，以及 Dan Abramov 对 HTML 的新视角。
- � 2025 年 5 月 4 日：React 的 View Transitions 和 Activity 组件，高效上下文提供者，useEffect 钩子顺序，Promise 序列化和'use client'指令的重要性。
- 🧩 2025 年 4 月 27 日：Dan Abramov 的“不可能组件”，简化 React Query 状态处理，React 编译器 RC 的生产优化，AI 聊天 SDK 和记忆策略。
- 🌐 2025 年 4 月 20 日：服务器端渲染 React，状态管理挑战，构建全栈 AI 聊天应用，React 功能演进和性能提升架构。
- 🏆 2025 年 4 月 13 日：高级 React 技术，React Query 机制，React 协调算法，动态表单挑战和服务器组件。
- ⚖️ 2025 年 4 月 6 日：React 架构权衡，记忆化解析，Zustand 和 Immer 构建健壮应用，无库表单创建和 Dash.js 自适应流实现。
- 🔒 2025 年 3 月 30 日：Next.js 授权，React 的 View Transition API，React 内部工作原理，Next.js 治理和国际化技巧。
- 🖥️ 2025 年 3 月 23 日：React 服务器端渲染，React 库的通用架构，TanStack 实时数据更新，URL 状态管理，从 Next.js 转向 TanStack。
- 🚀 2025 年 3 月 16 日：Next.js 性能优化，React 中的 Toast 通知，React.memo 的替代方案，Next.js API 构建和 NYT 测试库迁移。
- 📶 2025 年 3 月 9 日：React 中使用信号的挑战，状态管理工具比较，Server Actions 中的 Toast 反馈，布局效果和状态转换。
- 🧠 2025 年 3 月 2 日：React 中的函数式编程，React 19 缓存 API 优化数据获取，从 Create React App 迁移到 Vite，提升 Next.js 的 INP 指标。
- 🌅 2025 年 2 月 23 日：React 生态系统更新，Create React App 的弃用，现代框架集成，自定义钩子和实用设计技巧。

---

### [隐私](https://reactdigest.net/privacy)

**原文标题**: [Privacy](https://reactdigest.net/privacy)

隐私政策概述，强调保护用户个人信息的重要性，明确信息收集、使用及保护的原则，并提供用户数据访问与删除的途径。

- 🔒 隐私至关重要，制定政策以明确个人信息如何被收集、使用及披露。  
- 🎯 收集个人信息前会明确目的，并仅用于指定或兼容目的，需用户同意或法律要求。  
- ⏳ 仅在必要时保留个人信息，确保数据使用期限合理。  
- 📝 通过合法公平手段收集信息，适当时需用户知情或同意。  
- ✔️ 确保个人数据准确、完整且最新，符合使用目的。  
- 🛡️ 采取合理安全措施保护信息，防止丢失、盗窃或未经授权访问。  
- 📢 向用户公开个人信息管理政策及实践。  
- ✉️ 仅收集用户邮箱地址用于发送周刊，不用于其他目的。  
- 🚸 严格遵守 COPPA，不收集或存储 13 岁以下儿童信息。  
- 📬 用户可依据《数据保护法》申请获取或删除存储的个人信息，联系邮箱：[email protected]。  
- 🚫 坚决反对垃圾邮件，提供随时退订链接。  
- ©️ 版权归 Bonobo Press 所有，政策更新至 2025 年。

---

### [媒体资料包——Bonobo 出版社](https://bonobopress.com/media-kit/)

**原文标题**: [Media Kit â Bonobo Press](https://bonobopress.com/media-kit/)

Bonobo Press 致力于为程序员和技术人员提供最新的趋势、工具和技术信息，通过精心策划的每周新闻简报吸引高度参与的读者群体，涵盖软件开发者、工程经理、CTO 等目标受众。其广告合作伙伴包括软件工具、招聘、会议等多种类型，旨在帮助广告商精准触达目标用户并提升转化率。

- 📧 **Newsletters 高参与度**：新闻简报的参与度是行业基准的两倍以上，严格清理邮件列表，优先考虑活跃读者。
- 🎯 **精准受众定位**：主要读者群来自欧洲和美国，涵盖从初创公司到大型企业的各类技术岗位。
- 💼 **Leadership in Tech**：面向技术领导者，订阅者 26,385 人，开信率 57.95%，点击率 11.38%，赞助费$1,940/期。
- 👨‍💻 **Programming Digest**：面向软件工程师，订阅者 18,263 人，开信率 51.83%，点击率 14.83%，赞助费$875/期。
- ⚙️ **C# Digest**：面向.NET 开发者，订阅者 19,724 人，开信率 52.61%，点击率 21.63%，赞助费$1,220/期。
- 🖥️ **React Digest**：面向 React 开发者，订阅者 23,279 人，开信率 47.56%，点击率 12.17%，赞助费$1,320/期。
- 📊 **广告格式与流程**：仅支持文本广告，需提前 4 天提交文案，建议尽早预订以确保档期。
- 🤝 **合作品牌**：包括 Okta、GitLab、MongoDB 等知名企业，许多合作伙伴多次预订广告位。
- 📩 **联系方式**：欢迎潜在广告商联系，以获取更多关于广告投放和效果报告的详细信息。

---

