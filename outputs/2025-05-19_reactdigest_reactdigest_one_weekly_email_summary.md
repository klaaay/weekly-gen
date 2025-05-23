### [React 文摘：电子邮件通讯](https://reactdigest.net/)

**原文标题**: [React Digest: Email Newsletter](https://reactdigest.net/)

《React Digest》是一份为 React 开发者精心策划的每周通讯，旨在为前端工程师提供精选内容和学习资源。  

- 📰 **精选内容**：每周推送经过筛选的高质量文章，附有简短摘要。  
- ⏱️ **节省时间**：帮助开发者快速获取有价值的信息，避免自行搜索的麻烦。  
- 📚 **持续学习**：每周提供新知识，涵盖 React 及相关技术的最新动态。。  
- 👥 **广泛认可**：已有超过 22,889 名前端工程师订阅，读者反馈积极，认为内容实用且更新及时。  
- 🌍 **全球读者**：受到世界各地前端工程师的欢迎，包括 React 并发模式等深度内容的讨论。  
- ©️ **品牌信息**：由 Bonobo Press 发行，涵盖 2013 至 2025 年，提供隐私政策和广告合作信息。

---

### [使用 React Router 实现 OpenAuth | Sean Campbell 的博客](https://seanpaulcampbell.com/blog/openauth-react-router/)

**原文标题**: [OpenAuth with React Router | Sean Campbell's Blog](https://seanpaulcampbell.com/blog/openauth-react-router/)

本文介绍了如何使用 OpenAuth 和 React Router 实现身份验证系统的完整指南。

- 🚀 使用 OpenAuth 作为用户身份验证方式，并通过数据库进行授权
- 🔧 项目设置包括创建 SST 项目、安装依赖和配置环境变量
- 🔐 设置 SST 身份验证服务器和创建身份验证处理程序
- 📦 在 React Router 中配置身份验证模块，包括会话存储和验证器
- 🔄 实现 React Router 中的身份验证路由：登录、回调和登出
- 🛡️ 创建受保护路由和用户引导组件
- 🧪 部署并测试完整的身份验证流程
- 💡 系统优势包括 JWT 令牌安全验证、多提供商支持和无服务器基础设施
- 🔮 未来计划添加 GitHub 提供商支持和自定义 UI 页面

---

### [Clerk Billing 入门指南](https://clerk.com/blog/intro-to-clerk-billing?utm_source=react-digest&utm_medium=newsletter&utm_campaign=getting-started-with-billing&utm_content=05-19-25&dub_id=zpRpqKKAKQBLwkic)

**原文标题**: [Getting started with Clerk Billing](https://clerk.com/blog/intro-to-clerk-billing?utm_source=react-digest&utm_medium=newsletter&utm_campaign=getting-started-with-billing&utm_content=05-19-25&dub_id=zpRpqKKAKQBLwkic)

Clerk Billing 提供了一种无需自定义 UI 或 Webhooks 的完整计费解决方案，通过与 Stripe 直接集成，简化了订阅、按使用量计费和组织级账单的设置流程。

- 💡 Clerk Billing 直接集成 Stripe，由 Stripe 处理支付，Clerk 负责用户界面和权限逻辑。  
- 🛠️ 提供预构建组件和 API，支持订阅、按使用量计费和组织级账单设置。  
- 🔒 支持基于角色的访问、安全升级和客户自助服务，与现有身份验证层无缝集成。  
- 🚀 无需胶水代码即可从原型快速过渡到生产环境，简化用户从入门到升级的全流程。  
- 🌍 在 Stripe 支持的全球范围内可用，并能与现有 Clerk 应用直接同步。  
- ▶️ 提供快速启用 Billing 的选项，开发者可立即开始使用。

---

### [Clerk 如何通过 Supabase 与 Next.js 应用集成](https://clerk.com/blog/how-clerk-integrates-nextjs-supabase?utm_source=react-digest&utm_medium=newsletter&utm_campaign=supabase-clerk&utm_content=04-21-25&dub_id=dlwyDt8lmUiyd1Mi)

**原文标题**: [How Clerk integrates with a Next.js application using Supabase](https://clerk.com/blog/how-clerk-integrates-nextjs-supabase?utm_source=react-digest&utm_medium=newsletter&utm_campaign=supabase-clerk&utm_content=04-21-25&dub_id=dlwyDt8lmUiyd1Mi)

本文介绍了如何在 Next.js 应用中集成 Supabase 和 Clerk，以提高安全性并减少开发时间。文章详细解释了 Supabase 如何与 Next.js 应用协同工作，以及 Clerk 如何与这一技术栈集成，并提供了一个实际应用案例 Quillmate 的代码实现。

- 🚀 Supabase 允许直接从客户端访问数据，无需传统后端，通过 Row Level Security (RLS) 确保数据安全。
- 🔑 Clerk 通过短生命周期的令牌验证用户身份，适用于传统后端和 Supabase 的直接访问模式。
- 🔗 Supabase 支持与 Clerk 集成，通过 JWKS 端点验证 JWT，确保请求的安全性。
- 👤 在 JWT 中设置正确的角色（如"authenticated"）以确保请求具有适当的访问权限。
- 📝 使用 Clerk 的 getToken 函数获取会话令牌，并将其传递给 Supabase 客户端以验证请求。
- 🛡️ 利用 RLS 策略和 Clerk 用户 ID（sub claim）在 Postgres 中实现行级数据访问控制。
- 💻 通过 Quillmate 案例展示了如何在实际应用中配置和使用 Clerk 与 Supabase 的集成。
- ⏱️ 使用 Supabase 和 Clerk 可以节省开发时间，同时通过 RLS 增强数据安全性。

---

### [如何构建自定义 React 渲染器 | Software Mansion](https://blog.swmansion.com/how-to-build-a-custom-react-renderer-595dc4a9cb1c?gi=da6a5169fb8a)

**原文标题**: [How to Build a Custom React Renderer | Software Mansion](https://blog.swmansion.com/how-to-build-a-custom-react-renderer-595dc4a9cb1c?gi=da6a5169fb8a)

React 最初是为构建 Web 用户界面而设计的库，但随着 React Native 的出现，它迅速成为跨平台构建 UI 的可靠选择。由于其灵活性，React 现在可用于构建 Web、iOS、Android、macOS、Windows、终端甚至某些电视平台的应用程序。本文将介绍如何将自定义 API 与 React 集成，并以视频合成软件 Smelter 为例，探讨如何实现自定义 React 渲染器。

- 🌐 **React 的跨平台能力**  
  React 不仅适用于 Web，还可用于构建多种平台的用户界面，包括移动端、桌面端和终端。

- 🔧 **自定义 React 渲染器的两种方式**  
  1. 实现新的 React 渲染器（适用于 JavaScript 环境，如浏览器或 Node.js）。  
  2. 为 React Native 实现新的目标平台（适用于需要在 JavaScript 运行时之外运行的情况）。

- 🎥 **Smelter 简介**  
  Smelter 是一款视频合成软件，通过 Rust 服务器提供 JSON 格式的 HTTP API，用于组合视频源并生成单一视频流。

- 📦 **使用 react-reconciler 实现自定义渲染器**  
  React 通过 `react-reconciler` 包提供自定义渲染器的 API，开发者只需实现 `HostConfig` 对象来与底层平台交互。

- 🔄 **渲染模式选择**  
  - **Mutation 模式**：适用于可动态添加和删除节点的 API（如浏览器 DOM）。  
  - **Persistance 模式**：适用于需要替换整个树的 API（如 React Native 的 Fabric 渲染器）。

- 📝 **核心实现函数**  
  包括 `createInstance`、`cloneInstance`、`appendInitialChild`、`replaceContainerChildren` 等，用于构建和更新组件树。

- ⚠️ **React 的局限性**  
  React 主要用于交互式 UI，但在非 UI 场景（如视频合成）中可能遇到更新顺序和网络可靠性等问题，需要开发者自行处理。

- 🚀 **Smelter 的实践**  
  在 Smelter 中，通过将 React 组件树转换为 JSON 并发送到渲染服务器来实现视频布局的更新。

- 🔗 **进一步学习**  
  可以参考 [Smelter 的渲染器实现](https://smelter.dev) 和 [react-reconciler 文档](https://reactjs.org/docs/react-reconciler.html) 了解更多细节。

---

### [React 中的依赖倒置：构建真正可测试的组件 · cekrem.github.io](https://cekrem.github.io/posts/dependency-inversion-in-react/)

**原文标题**: [Dependency Inversion in React: Building Truly Testable Components · cekrem.github.io
](https://cekrem.github.io/posts/dependency-inversion-in-react/)

概述  
React 开发中，组件与依赖的紧密耦合会导致测试、维护和修改困难。依赖倒置原则（DIP）通过抽象依赖关系，使组件更易测试和维护。  

- 🏗️ **问题：React 中的紧耦合**  
  - 组件直接依赖具体实现（如 fetch API），难以测试和修改数据源。  

- 🔄 **解决方案：依赖倒置原则**  
  - 高层组件不依赖低层模块，双方依赖抽象接口（如`UserRepository`）。  

- 📦 **实现抽象仓库**  
  - 定义接口（如`getUser`），并通过具体实现（如`ApiUserRepository`和`MockUserRepository`）解耦依赖。  

- 🧪 **测试简化**  
  - 使用模拟仓库（如`MockUserRepository`）轻松测试加载状态、数据渲染和异常情况。  

- ✅ **最佳实践**  
  - 明确接口定义、通过 props/context 注入依赖、隔离测试组件。  

- 🎯 **优势**  
  - 提升可测试性、可维护性、关注点分离和代码灵活性。  

- 📚 **延伸阅读**  
  - 《Clean Architecture》、React Testing Library 文档等。  

- ⚠️ **注意**  
  - 依赖注入（如使用 TSyringe）可进一步优化依赖管理，但需平衡复杂度。

---

### [不，React 上下文不会导致过多渲染](https://blacksheepcode.com/posts/no_react_context_is_not_causing_too_many_renders)

**原文标题**: [No, react context is not causing too many renders](https://blacksheepcode.com/posts/no_react_context_is_not_causing_too_many_renders)

概述：  
本文通过实际代码演示和交互示例，反驳了“React Context 会导致过多渲染”的常见误解，解释了 Context 的实际行为，并提供了优化建议。

- 🚀 **误解澄清**：React Context 不会导致所有子组件重新渲染，只有消费该 Context 的组件会更新。  
- 🔍 **代码演示**：通过示例展示点击“Change state”按钮仅触发相关组件渲染，无关组件不受影响。  
- ⚠️ **误区来源**：  
  - 1️⃣ 将不相关的状态塞进同一个 Provider 会导致不必要的渲染（应拆分多个 Provider）。  
  - 2️⃣ 误认为 Provider 的渲染会触发所有子组件渲染（实际通过 `children` 传递的子组件不会重新渲染）。  
- 🛠️ **优化建议**：  
  - 对无关状态使用独立 Context Provider。  
  - 优先用 Context 管理局部共享状态，而非全局状态工具（如 Redux）。  
- 💡 **适用场景**：Context 适合同一页面内跨层级组件共享状态，而非全局复杂状态管理。  
- ⚡ **性能隐患**：受控组件（如输入框）的频繁更新才是常见性能问题来源。  
- 📌 **结论**：Context 是轻量级状态共享的合理选择，不必过度依赖全局状态库。

---

### [静态如服务器——反应过度](https://overreacted.io/static-as-a-server/)

**原文标题**: [Static as a Server — overreacted](https://overreacted.io/static-as-a-server/)

这篇博客介绍了如何利用“混合”框架（如 Next.js）将 React 服务器组件（RSC）以静态形式部署，并探讨了“服务器”与“静态”框架的融合趋势。

- 💡 博客使用 RSC 构建，但通过 Cloudflare CDN 免费静态托管，实现零成本运行。  
- 🔄 传统观念中，“服务器”和“静态”框架是分开的，但现代框架支持两种输出模式。  
- 🤖 “混合”框架通过构建时预运行服务器代码生成静态页面，兼具灵活性和统一性。  
- 🛠️ 例如 Next.js 默认生成静态站点，并通过`output: "export"`禁用服务器功能，确保纯静态输出。  
- ⚙️ 博客中的 RSC 在部署时运行（如`await getPosts()`读取文件系统），而非客户端或实时服务器。  
- 🌐 作者呼吁接受“静态即预运行的服务器”概念，强调代码无需修改即可适应不同模式。  
- 🔗 其他“混合”框架（如 Astro）也支持类似特性，非 RSC 专属。

---

### [容器查询：“此元素外部是否有足够空间？”——Frontend Masters 博客](https://frontendmasters.com/blog/container-query-for-is-there-enough-space-outside-this-element/)

**原文标题**: [Container Query for “is there enough space outside this element?” – Frontend Masters Blog](https://frontendmasters.com/blog/container-query-for-is-there-enough-space-outside-this-element/)

概述：Chris Coyier 探讨了如何利用容器查询（Container Queries）和视口单位（Viewport Units）动态调整 UI 组件（如轮播箭头）的位置，使其根据外部空间自动选择放置在内部或外部，而无需依赖固定数值。

- 🎨 **容器查询与视口单位结合**：通过 `@container` 查询和 `100vw` 视口单位，检测外部空间是否足够容纳箭头，避免硬编码尺寸。  
- 🔄 **动态位置调整**：当容器宽度小于 `视口宽度 - 箭头宽度 - 间隙` 时，使用 CSS 变换（如 `translate`）将箭头移至内部。  
- 📦 **容器包装元素必要性**：需外层包装元素（`.box`）作为容器查询的目标，因其无法直接查询自身。  
- 🛠️ **代码示例**：  
  - 容器设置：`.box { container: box / inline-size; inline-size: min(500px, 100vw); }`  
  - 查询逻辑：`@container box (inline-size <= calc(100vw - 80px * 2 - 1rem * 2)) { ... }`  
- 💡 **灵活性与应用场景**：不依赖固定容器尺寸，适用于响应式设计；类似逻辑可扩展至弹出层边距优化等场景。  
- 👏 **灵感来源**：Adam Argyle 的原方案更巧妙，使用 `cqi` 单位处理非视口父容器。  
- 📚 **延伸学习**：推荐 Jen Kramer 的现代 CSS 布局课程（含 Grid、Flexbox 和容器查询）。

---

### [高度之谜 • 乔希·W·科莫](https://www.joshwcomeau.com/css/height-enigma/)

**原文标题**: [The Height Enigma • Josh W. Comeau](https://www.joshwcomeau.com/css/height-enigma/)

概述：本文深入探讨了 CSS 中百分比高度（height: 50%）失效的原因及解决方案，解释了宽度与高度计算的本质差异，并提供了通过固定高度、Flexbox 和 Grid 布局等方法实现预期效果的技巧。

- 🧩 **核心问题**：CSS 中百分比高度失效是因为父元素和子元素的高度计算相互依赖，形成循环悖论，导致浏览器忽略声明。
- 🔄 **宽度与高度的差异**：默认情况下，宽度基于父元素计算，而高度基于子元素内容计算，导致百分比行为不同。
- 📏 **解决方案 1 - 固定高度**：为父元素设置明确高度（如`height: 300px`或`24rem`），使子元素的百分比高度有计算基准。
- 🧠 **“Knowable”概念**：父元素高度需独立于子元素（如固定值或视窗高度），百分比高度才能生效。
- 📦 **内容框影响**：百分比高度基于父元素的**内容框**（扣除 padding 后的空间），而非总高度。
- 🌐 **根元素特殊性**：`<html>`的`height: 100%`基于视窗，可向下传递百分比高度。
- ⚠️ **min-height 的陷阱**：`min-height`不固定实际高度，仍会导致百分比高度失效。
- 🎯 **终极方案 - Flexbox/Grid**：使用`display: grid`或`flex: 1`可避免高度依赖问题，子元素自动填充空间。
- 📚 **扩展学习**：推荐课程《CSS for JavaScript Developers》系统掌握 CSS 布局模型。

---

### [CSS 中的吉他和弦 - DEV 社区](https://dev.to/madsstoumann/guitar-chords-in-css-3hk8?utm_source=cassidoo&utm_medium=email&utm_campaign=birds-born-in-a-cage-think-flying-is-an-illness)

**原文标题**: [Guitar Chords in CSS - DEV Community](https://dev.to/madsstoumann/guitar-chords-in-css-3hk8?utm_source=cassidoo&utm_medium=email&utm_campaign=birds-born-in-a-cage-think-flying-is-an-illness)

Mads Stoumann 分享了一篇关于使用纯 CSS 创建吉他弦和品的教程，展示了如何通过 HTML 属性和 CSS 新特性`attr()`方法构建可交互的吉他指板组件，无需 JavaScript。

- 🎸 使用 CSS 的`attr()`方法动态生成吉他指板的弦和品，通过 HTML 属性控制弦数、品数和和弦类型。  
- 🖥️ 利用 CSS Grid 布局和线性渐变创建指板的视觉结构，支持自定义弦和品的样式。  
- 🎵 通过 HTML 属性标记音符位置、手指按法，以及开放弦和闷弦的显示效果。  
- 👐 支持横按和弦（Barre Chords）的显示，通过`barre`属性标记按住的弦数。  
- ♿ 后续增加了无障碍支持，使用`details/summary`元素让屏幕阅读器能朗读和弦信息。  
- 🎨 演示了如何适配其他乐器（如尤克里里和班卓琴），仅需调整弦数属性即可。  
- 🔍 目前仅兼容 Chrome 浏览器，因依赖 CSS 新特性，但提供了 polyfill 方案。  

教程还包含用户互动，如开发者讨论如何优化无障碍体验，以及扩展功能（如播放声音）的可能性。

---

### [JavaScript 中展开与剩余语法的强大之处 - Matt Smith](https://allthingssmitty.com/2025/05/05/the-power-of-spread-and-rest-patterns-in-javascript.md/)

**原文标题**: [
    The power of the spread and rest syntax in JavaScript - Matt Smith
  ](https://allthingssmitty.com/2025/05/05/the-power-of-spread-and-rest-patterns-in-javascript.md/)

JavaScript 中的展开和剩余语法是一种强大且常用的特性，能够简化代码并提高表达力。

- 🔄 展开语法（Spread）用于解构数组、对象等可迭代结构，如复制数组、合并数组或传递函数参数。  
- 📦 剩余参数（Rest）用于收集多个元素，常用于函数参数或解构赋值中。  
- 📝 展开语法在 React 中常用于不可变更新，如状态管理或表单处理。  
- ⚠️ 注意展开语法仅进行浅拷贝，嵌套结构仍为引用。  
- 🔄 对象展开的顺序很重要，右侧属性会覆盖左侧。  
- 🛠️ 剩余参数适用于不定参数的函数，如工具函数中的求和操作。  
- 🌟 这些语法在 React、工具库和原生 JS 中广泛应用，是现代 JavaScript 开发的必备技能。

---

### [分类你的依赖项](https://antfu.me/posts/categorize-deps?utm_source=weeklyfoo&utm_medium=email&utm_campaign=weeklyfoo)

**原文标题**: [Categorize Your Dependencies](https://antfu.me/posts/categorize-deps?utm_source=weeklyfoo&utm_medium=email&utm_campaign=weeklyfoo)

项目依赖分类的探讨与实践，以及 pnpm catalogs 的创新应用。

- 📦 **依赖类型区分**：`dependencies`（生产依赖）和`devDependencies`（开发依赖）是 npm 项目的核心分类，前者为运行时必需，后者仅用于开发和构建阶段。
- �️ **项目类型影响**：依赖分类对发布到 npm 的库（Libraries）最有效，而应用（Apps）和内部项目（Internal）的分类意义可能不同。
- 🛠️ **工具扩展用途**：构建工具如 Vite、tsup 等重新定义依赖分类的用途，例如 Vite 将`dependencies`视为客户端包进行预优化。
- 🤔 **分类模糊性**：仅靠`dependencies`和`devDependencies`无法清晰表达包的用途（如测试、类型检查、打包内联等），缺乏灵活性。
- 🏷️ **新分类思路**：提出按功能分类（如`test`、`lint`、`build`、`frontend`等），但原生 npm 不支持此类细化。
- 🔍 **pnpm catalogs 解决方案**：通过`pnpm-workspace.yaml`中的`catalogs`字段实现依赖版本集中管理和分类（如`frontend`、`prod`），支持命名分类和注释。
- 🛠️ **工具链适配**：配套开发了 VS Code 扩展`PNPM Catalog Lens`显示版本，并整合了`taze`、`eslint-plugin-pnpm`等工具支持 catalog 操作。
- 🚀 **未来潜力**：依赖分类可优化工具配置（如 Vite 依赖预优化、unbuild 外部化控制），增强代码审查和安全漏洞评估。
- 🌱 **实践倡议**：作者已在部分项目迁移至命名 catalogs，鼓励社区尝试并探索更佳实践。

---

### [复杂 React/Next.js 应用的健壮数据获取架构](https://www.trevorlasn.com/blog/fetching-data-for-complex-next-and-react-apps)

**原文标题**: [Robust Data Fetching Architecture For Complex React/Next.js Apps](https://www.trevorlasn.com/blog/fetching-data-for-complex-next-and-react-apps)

概述  
本文介绍了在复杂的 React/Next.js 应用中采用“三层数据架构”模式来优化数据获取，避免常见问题和技术债务，提升性能的方法。  

- 🚀 **数据获取的常见问题**：包括重复请求、状态管理混乱、缓存失效、竞态条件等，这些问题会随着应用规模扩大而加剧。  
- 🛠️ **传统方法的缺陷**：直接使用`useEffect`和`fetch`会导致请求瀑布流、状态管理混乱、内存泄漏等问题，难以维护和测试。  
- 🏗️ **三层数据架构解决方案**：  
  - **第一层（服务端组件）**：负责初始数据获取，提升首屏加载速度。  
  - **第二层（React Query）**：管理客户端缓存和状态更新，处理加载和错误状态。  
  - **第三层（乐观更新）**：通过即时 UI 反馈提升用户体验。  
- 📂 **代码结构示例**：展示了如何通过分层组织代码，实现数据流的清晰分离。  
- 🔄 **数据流逻辑**：服务端组件提供初始数据，React Query 管理动态更新，乐观更新确保 UI 响应速度。  
- 🧩 **上下文整合**：使用 Context API 集中管理数据访问，避免组件间冗余传递。  
- ⚖️ **适用场景**：该架构适合复杂应用，简单应用可能显得过度设计，但能显著提升可维护性和测试性。  
- 💡 **额外建议**：推荐使用`<ReactQueryDevtools>`调试工具，并提及类似模式可应用于其他框架（如 Vue.js、Svelte）。

---

### [编程文摘：电子邮件通讯](https://programmingdigest.net/?utm_source=web-archive&utm_campaign=react)

**原文标题**: [Programming Digest: Email Newsletter](https://programmingdigest.net/?utm_source=web-archive&utm_campaign=react)

《Programming Digest》是一份专为软件工程师精心挑选的每周通讯，提供精选文章和简短摘要，帮助读者节省时间并每周学习新知识。  

- 📧 **加入社群**：超过 18,234 名软件工程师订阅，每周一封邮件。  
- 📖 **精选内容**：提供人工筛选的文章与简短摘要，节省寻找优质内容的时间。  
- 🎯 **高效学习**：每周都能学到新知识，涵盖 API 设计等热门话题。  
- 💬 **读者好评**：用户称赞其内容实用，如“每期都能学到东西”“感谢推荐优质文章”。  
- 🌍 **广泛受众**：被全球软件工程师阅读，由 Bonobo Press 发行。  
- 🔒 **附加信息**：提供隐私政策、广告合作等链接（© 2013-2025）。

---

### [科技领导力：电子邮件通讯](https://leadershipintech.com/?utm_source=web-archive&utm_campaign=react)

**原文标题**: [Leadership in Tech: Email Newsletter](https://leadershipintech.com/?utm_source=web-archive&utm_campaign=react)

概述总结  
一份精心策划的每周通讯，面向 CTO、工程经理和高级工程师，旨在帮助他们成为更优秀的领导者。  

- 📰 **每周精选** - 为技术领导者提供精心挑选的文章和简短摘要。  
- ⏳ **节省时间** - 无需费力寻找有价值的内容，直接获取优质资源。  
- 📚 **持续学习** - 每周都能学到新知识，提升领导力技能。  
- 👥 **读者反馈** - 用户称赞文章内容精准，尤其在软件领域的领导力建设方面独具优势。  
- 🏢 **广泛认可** - 来自全球科技领导者的信赖与阅读。  
- 🔒 **品牌保障** - 由 Bonobo Press 出品，涵盖多个主题，包括隐私和广告服务。

---

### [C#文摘：电子邮件通讯](https://csharpdigest.net/?utm_source=web-archive&utm_campaign=react)

**原文标题**: [C# Digest: Email Newsletter](https://csharpdigest.net/?utm_source=web-archive&utm_campaign=react)

概述总结  
一份为.NET 开发者精心挑选的每周通讯，提供精选文章和简短摘要，帮助开发者节省时间并每周学习新知识。  

- 📧 **加入超过19,672名C#工程师**：每周一封电子邮件，涵盖精选内容。  
- 📖 **阅读精选文章**：附带简短摘要，节省寻找有价值内容的时间。  
- 🎓 **每周学习新知识**：持续提升技能，了解最新.NET 技术动态。  
- 💬 **读者反馈**：内容包括实用技巧（如功能标志、LINQ）、诊断工具（DiagnosticListener）和设计模式（Operation Result Pattern），受到广泛推荐。  
- 🌍 **覆盖范围**：被全球.NET 工程师阅读，来自知名机构如 Microsoft、Amazon 等。  
- © **版权信息**：由 Bonobo Press 发布（2013-2025 年），提供隐私政策和广告服务。

---

### [让开发者与时俱进——Bonobo Press](https://bonobopress.com/)

**原文标题**: [Keeping developers up to date â Bonobo Press](https://bonobopress.com/)

Bonobo Press 是一家自 2013 年起为软件开发者、IT 专业人士和技术人员提供最新资讯的出版商，拥有超过 89,000 名订阅用户，提供简洁高效的新闻简报服务。

- 📧 **新闻简报**：每日和每周针对开发者、工程经理、技术主管和 CTO 的精选内容，以简洁高效著称。  
- 📢 **广告服务**：帮助广告主精准触达软件工程师、团队领导、工程经理及 IT 决策者等目标受众。  
- 📂 **媒体资料**：提供详细的媒体资料包，方便广告主了解合作细节。  
- 📬 **联系我们**：欢迎通过指定渠道咨询、建议或洽谈广告合作。

---

### [往期通讯：第一页](https://reactdigest.net/newsletters)

**原文标题**: [Past Newsletters: Page 1](https://reactdigest.net/newsletters)

概述总结  
本期 React Digest 涵盖了从 2025 年 1 月至 5 月的多个关键主题，包括 React Router 的 OpenAuth、数据获取架构、React Server Components、性能优化、状态管理、设计模式等，同时涉及 Next.js、React Native 及生态工具的最新动态。  

- 🔐 5 月 18 日：探讨 React Router 的 OpenAuth、自定义渲染器及依赖倒置原则，揭秘 React Context 效率与静态站点生成。  
- 🏗️ 5 月 11 日：复杂应用的数据获取架构、颜色方案切换实现及媒体查询自定义 Hook。  
- 🎭 5 月 4 日：React 视图过渡与 Activity 组件优化 UI 动画，useEffect 顺序及 Promise 序列化解析。  
- 🧩 4 月 27 日：Dan Abramov 谈“不可能组件”，React Query 状态简化及 React 编译器生产优化。  
- ⚡ 4 月 20 日：服务端渲染前沿实践、全栈 AI 聊天应用构建及 React 架构演进。  
- 🛠️ 4 月 13 日：高级 React 技巧（如 React Query 机制、协调算法）及动态表单挑战。  
- ⚖️ 4 月 6 日：React 架构权衡、Zustand/Immer 最佳实践及无库表单构建。  
- 🔒 3 月 30 日：Next.js 授权、View Transition API 及国际化技巧。  
- 📊 3 月 23 日：React SSR 深度解析、TanStack 实时数据更新及 URL 状态管理。  
- 🚀 3 月 16 日：Next.js 性能优化、Toast 通知实现及 React.memo 替代方案。  
- ⚠️ 3 月 9 日：React 中 Signals 的挑战、状态管理对比及布局效应探讨。  
- 🧠 3 月 2 日：React 函数式编程、React 19 缓存 API 及 Vite 迁移指南。  
- ☀️ 2 月 23 日：Create React App 弃用、现代框架集成及自定义 Hook 实践。  
- ✍️ 2 月 16 日：ProseMirror 渲染器重构、类组件升级及 React Router 内部原理。  
- 📐 2 月 9 日：React 设计模式、动态样式加载及单一职责原则应用。  
- 💡 2 月 2 日：React Server Components 优势、Next.js 14 解析及 WebSocket 扩展。  
- ⏱️ 1 月 26 日：React 初始加载性能优化、View Transitions API 及 LangChain 流式聊天。  
- 🛒 1 月 20 日：Shopify 的 React Native 五年经验、路由拆分及动画 API 实验。  
- 🎣 1 月 12 日：自定义 Hook 避坑指南、Next.js 缓存改进及 Server Components 优势。  
- 🆕 1 月 5 日：新年特辑涵盖实例 Hook 模式、React Router 必读资源等。

---

### [隐私](https://reactdigest.net/privacy)

**原文标题**: [Privacy](https://reactdigest.net/privacy)

React Digest 的隐私政策概述，强调保护用户隐私的重要性，明确信息收集、使用及保护的原则，并提供用户数据管理的具体指引。

- 🔒 隐私至关重要，因此制定了明确的隐私政策，说明如何收集、使用、披露个人信息。  
- 🎯 收集个人信息前会明确目的，并仅在达成该目的或获得用户同意时使用。  
- ⏳ 仅在必要期限内保留个人信息。  
- 📝 通过合法公平手段收集信息，并在适当时获得用户知情或同意。  
- ✔️ 确保个人数据准确、完整、最新，且与使用目的相关。  
- 🛡️ 采取合理安全措施保护个人信息，防止丢失、盗窃或未经授权的访问。  
- 📢 向用户公开个人信息管理政策及实践。  
- ✉️ 仅收集用户邮箱地址用于发送周刊，不用于其他目的。  
- 🚸 遵守 COPPA，不收集或存储 13 岁以下儿童信息。  
- 📬 用户可依据《数据保护法》请求获取或删除存储的个人信息，联系邮箱：[email protected]。  
- 🚫 反对垃圾邮件，提供随时退订选项。  
- ©️ 版权归 Bonobo Press 所有（2013-2025）。

---

### [媒体资料包 —— Bonobo 出版社](https://bonobopress.com/media-kit/)

**原文标题**: [Media Kit â Bonobo Press](https://bonobopress.com/media-kit/)

Bonobo Press 是一家专注于为程序员和技术人员提供最新趋势、工具和技术更新的媒体平台，通过每日和每周的新闻简报服务高度活跃的读者群体，并提供精准的广告投放服务。

- 📊 **受众群体**：主要订阅者位于美国和欧洲，涵盖软件开发者、工程经理、技术副总裁及 CTO 等技术决策者。  
- ✉️ **高互动简报**：简报互动率超行业标准两倍，严格清理不活跃用户，优先保持读者参与度。  
- 📧 **简报详情**：  
  - **Leadership in Tech**：24,616 订阅，58.95% 打开率，$1,620/期  
  - **Programming Digest**：15,535 订阅，52.39% 打开率，$760/期  
  - **C# Digest**：21,467 订阅，51.82% 打开率，$1,080/期  
  - **React Digest**：27,849 订阅，46.35% 打开率，$1,320/期  
- 📝 **广告格式**：纯文本内嵌，需包含链接、标题（<100 字符）及描述（<400 字符），提前 4 天提交内容。  
- 🔄 **合作流程**：确认档期→付款→内容优化→广告发布，建议提前数周预订。  
- 🤝 **知名合作伙伴**：Okta、GitLab、MongoDB、Twilio 等，多次复投率高。  
- 📩 **联系方式**：提供定制化广告方案，助力提升潜在客户与转化率。

---

