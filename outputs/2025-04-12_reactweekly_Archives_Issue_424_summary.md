## [Read on the Web](https://react.statuscode.com/issues/424)

**原文标题**: [React Status Issue 424: April 9, 2025](https://react.statuscode.com/issues/424)

**中文标题**: React 状态周报第 424 期：2025 年 4 月 9 日

概述总结  
本期内容涵盖了 React 技术的最新动态、工具更新、会议信息以及 JavaScript 生态中的其他有趣内容。  

- 📧 **订阅与隐私** — 提供订阅服务，可随时取消，隐私政策保障邮箱安全。  
- 🎤 **React Conf 2025** — 门票抽签将于 4 月 25 日开始，活动于 10 月在拉斯维加斯附近举行。  
- ☕ **React 技术深度探讨** — Dan Abramov 分享 React Server Components 的架构与理论思考。  
- 🍜 **Tonkotsu IDE** — 为 JavaScript 和 TypeScript 开发者提供 AI 代理支持的 IDE，开放免费早期访问。  
- ⚙️ **React 协调算法** — 深入解析 React 如何通过虚拟 DOM 更新实际 DOM，提升应用性能。  
- ☁️ **Next.js 部署** — 使用 OpenNext 工具将 Next.js 应用优化部署到 Cloudflare Workers 等平台。  
- 🤖 **LLM 驱动测试迁移** — Airbnb 分享如何利用 LLM 从 Enzyme 迁移到 React Testing Library。  
- 📦 **React Native 0.79** — 工具链提速，Android 应用启动显著加快。  
- 🎨 **动画组件库** — Fancy Components 提供多种动画 React 组件，丰富 UI 效果。  
- 🛠 **工具更新** — React Testing Library、TanStack Form、Embla Carousel 等工具迎来新版本。  
- 🌍 **JavaScript 生态动态** — 包括 Notebook 编程、Node.js 测试指南、Deno 商标争议及 JSHeroes 会议信息。

---

## [React for Two Computers](https://overreacted.io/react-for-two-computers/)

**原文标题**: [React for Two Computers — overreacted](https://overreacted.io/react-for-two-computers/)

**中文标题**: "双机 React——过度反应"

- 🚀 **文章概述**：作者探讨了如何将 React 程序拆分为在两个计算机上运行，通过时间与空间的分离实现分布式计算。文章分为两部分，前半部分讨论时间拆分（Early 和 Late 世界），后半部分讨论空间拆分（客户端与服务器）。  

- 🧩 **核心概念**：  
  - **Early 世界**：执行初始计算的计算机（如服务器）。  
  - **Late 世界**：完成剩余计算的计算机（如客户端）。  
  - **Components**（组件）：可跨世界拆分，不依赖执行顺序。  
  - **Primitives**（原语）：必须在同一世界执行，依赖具体实现（如 DOM 操作）。  

- 🔄 **时间拆分**：  
  - 通过**标签（tags）**表示潜在的函数调用，延迟执行。  
  - **interpret 函数**：溶解 Early 组件，生成 Late 组件的蓝图。  
  - **perform 函数**：在 Late 世界执行原语，生成最终结果（如 DOM）。  

- 🌐 **空间拆分**：  
  - **import tag 语法**：在 Early 世界引用 Late 世界的代码，但不执行。  
  - **JSON 序列化**：将 Late 组件及其数据发送到 Late 世界。  
  - **动态加载**：Late 世界解析 JSON 并加载所需组件。  

- 🧠 **关键突破**：  
  - **闭包跨网络**：Early 世界传递代码和数据到 Late 世界。  
  - **无状态组件**：Early 组件不依赖 Late 世界的状态。  
  - **组合性**：通过包装（如`<Donut>`）实现跨世界交互。  

- 🎯 **挑战与解决**：  
  - **时间依赖问题**：通过区分**Components**（无状态）和**Primitives**（有状态）解决。  
  - **跨世界通信**：`import tag`和`import rpc`语法实现引用而非导入。  

- 🔮 **未来方向**：  
  - **流式执行**：逐步填充未完成的 Late 组件。  
  - **状态管理**：Late 组件的状态变化不影响 Early 世界。  
  - **缓存优化**：预计算 Early 世界结果（静态生成）。  

- 💡 **总结**：通过分离计算的时间和空间维度，React 程序可以更灵活地分布在多台计算机上运行，同时保持逻辑一致性。  

- 🌟 **最终示例**：通过`<Donut>`组件包装`<Clock>`，实现 Early 世界时间与 Late 世界样式的结合。  

- 📚 **扩展阅读**：  
  - **Poison Pills**：防止模块在错误世界执行。  
  - **指令语法**：如`'use client'`标记 Late 组件。  
  - **数据获取**：Early 世界适合低延迟数据预取。  

- 🎉 **实践建议**：尝试 Parcel 的 React Server Components 支持，体验真实场景。

---

## [▶️ React for Two Computers talk](https://www.youtube.com/watch?v=ozI4V_29fj4)

**原文标题**: [React for Two Computers | Dan Abramov - YouTube](https://www.youtube.com/watch?v=ozI4V_29fj4)

**中文标题**: "双机 React | Dan Abramov - YouTube"

该内容为 YouTube 网站底部的导航链接列表，涵盖关于、版权、联系方式、开发者信息、广告合作、条款政策及功能测试等相关条目。

- ℹ️ 关于  
- 📰 新闻稿  
- ©️ 版权  
- 📞 联系我们  
- 🎨 创作者  
- 💼 广告合作  
- 👩💻 开发者  
- 📜 条款  
- 🔒 隐私与安全  
- ⚖️ 政策与安全  
- ▶️ YouTube 运作机制  
- 🧪 测试新功能  
- ®️ 谷歌公司版权声明（2025）

---

## [the ticket lottery for React Conf 2025](https://forms.reform.app/react-conf/ticket-lottery/piaae1)

**原文标题**: [Join the React Conf Ticket Lottery](https://forms.reform.app/react-conf/ticket-lottery/piaae1)

**中文标题**: "参与 React Conf 门票抽签"

好的，请提供需要总结的文本内容，我会按照您要求的格式生成概述和带表情符号的要点列表。  

示例格式：  

这里是文章的概述总结，简明扼要地概括全文核心内容。  

- 🌟 第一个关键点，简洁描述。  
- 📌 第二个关键点，突出重要信息。  
- 🔍 第三个关键点，补充细节或背景。  

请提供具体文本以便我为您生成内容！

---

## [React Reconciliation: The Hidden Engine Behind Your Components](https://cekrem.github.io/posts/react-reconciliation-deep-dive/)

**原文标题**: [React Reconciliation: The Hidden Engine Behind Your Components · cekrem.github.io
](https://cekrem.github.io/posts/react-reconciliation-deep-dive/)

**中文标题**: "React 协调机制：组件背后的隐形引擎 · cekrem.github.io"

React 协调机制是 React 更新 DOM 以匹配组件树的核心算法，它通过高效的比较和更新策略实现声明式编程模型。理解这一机制有助于优化性能并设计更合理的组件结构。

- 🔄 **协调机制概述**：React 通过比较新旧元素树来决定如何高效更新 DOM，而非直接操作虚拟 DOM。
- 🏷️ **组件身份与状态保留**：相同类型的元素在同一位置会保留状态，仅更新属性；不同类型则会导致重新挂载。
- 🌳 **元素树结构**：JSX 被转换为轻量级的 JavaScript 对象树，DOM 元素类型为字符串，自定义组件类型为函数引用。
- ⚙️ **协调过程**：React 创建新树并与旧树比较，遵循类型优先、位置关键的原则，决定更新或重建子树。
- 🔑 **Key 的作用**：Key 覆盖基于位置的比较，用于列表时避免全量重渲染，也可在非列表场景中控制组件身份。
- 🚀 **性能优化模式**：
  - 避免内联组件定义（防止函数引用变化导致重挂载）。
  - 使用组合模式隔离状态变化的影响范围。
  - 通过 Key 实现高级状态保留（如跨组件传递状态）。
- 📍 **状态共置**：将状态尽可能靠近使用它的组件，减少不必要的重新渲染。
- 🧩 **组件设计优化**：拆分混合职责的组件，避免状态提升过高，自然减少渲染范围。
- 🏛️ **与整洁架构的契合**：协调机制符合单一职责、依赖倒置和接口隔离原则。
- 📝 **实践建议**：
  - 保持组件定义稳定。
  - 向下移动状态。
  - 合理使用 Key。
  - 优先通过结构调整而非强制记忆化优化性能。

---

## [Deploy Your Next.js App to Cloudflare Workers with the Cloudflare Adapter for OpenNext](https://blog.cloudflare.com/deploying-nextjs-apps-to-cloudflare-workers-with-the-opennext-adapter/)

**原文标题**: [Deploy your Next.js app to Cloudflare Workers with the Cloudflare adapter for OpenNext](https://blog.cloudflare.com/deploying-nextjs-apps-to-cloudflare-workers-with-the-opennext-adapter/)

**中文标题**: "使用 OpenNext 的 Cloudflare 适配器将 Next.js 应用部署到 Cloudflare Workers"

Cloudflare 推出了适配 OpenNext 的 Cloudflare 适配器 1.0.0-beta 版本，使 Next.js 应用能更高效地部署在 Cloudflare Workers 上，支持更多 Next.js 功能并优化性能。

- 🚀 **Cloudflare 适配器发布**：1.0.0-beta 版本发布，支持 Next.js 应用部署到 Cloudflare Workers，取代了 Next on Pages。  
- 🔧 **功能增强**：改进了与 OpenNext 的集成，支持更多 Next.js 功能，并优化了 Node.js 兼容性。  
- 🌐 **OpenNext 工具**：OpenNext 是一个构建工具，可将 Next.js 应用优化为适合多种平台部署的包，包括 Cloudflare Workers。  
- 📅 **版本支持**：计划支持 Next.js 14 的最新次要版本和 Next.js 15 的所有次要版本。  
- ⚡ **关键功能**：  
  - 缓存优化（ISR/SSG 和数据缓存）  
  - 部分预渲染（PPR）  
  - 中间件支持  
  - 同时支持 App 和 Pages 路由  
  - 图像优化（与 Cloudflare Images 集成）  
- 🛠 **待支持功能**：  
  - 完整支持 Windows 开发  
  - 支持 Edge 运行时  
  - 组合式缓存（use cache）  
- 📈 **生态系统改进**：  
  - Workers 的 Node.js 兼容性增强  
  - Worker 大小限制提升（免费计划 3 MiB，付费计划 15 MiB）  
- 🏁 **未来计划**：  
  - 减少包大小  
  - 提升应用性能  
  - 支持部署到多个 Workers  
- 🚀 **快速部署步骤**：  
  - 使用模板创建应用  
  - 开发时使用 Next.js 开发服务器  
  - 本地预览或部署到 Workers  
- 📢 **反馈与社区**：欢迎在 GitHub 提交问题或加入 OpenNext Discord 讨论。

---

## [OpenNext](https://opennext.js.org/)

**原文标题**: [OpenNext - OpenNext](https://opennext.js.org/)

**中文标题**: OpenNext - OpenNext

OpenNext 是一个旨在统一 Next.js 自托管解决方案的开源项目，支持跨平台部署，目前由多个团队共同维护并已应用于多个生产环境。

- 🚀 OpenNext 解决了 Next.js 无法跨平台自托管的问题，不同于 Remix 或 Astro 等现代前端框架。  
- 🔧 现有解决方案分为两类：开源框架特定实现和闭源产品特定实现，但因 Next.js 频繁更新而难以单独维护。  
- 🤝 目前由 SST（AWS 适配器）、Cloudflare 团队（Cloudflare 适配器）和 Netlify 团队（Netlify 适配器）共同支持。  
- 🌍 已在 NHS England、Udacity、Gymshark UK 等生产环境中广泛部署。  
- 💬 欢迎通过 Discord 加入社区协作，目标是全面支持 Next.js 所有功能。

---

## [Accelerating Large-Scale Test Migration with LLMs](https://medium.com/airbnb-engineering/accelerating-large-scale-test-migration-with-llms-9565c208023b)

**原文标题**: [Accelerating Large-Scale Test Migration with LLMs | by Charles Covey-Brandt | The Airbnb Tech Blog | Mar, 2025 | Medium](https://medium.com/airbnb-engineering/accelerating-large-scale-test-migration-with-llms-9565c208023b)

**中文标题**: "利用 LLM 加速大规模测试迁移 | Charles Covey-Brandt | Airbnb 技术博客 | 2025 年 3 月 | Medium"

Airbnb 利用 LLMs（大型语言模型）成功将约 3500 个 React 组件测试文件从 Enzyme 迁移至 React Testing Library（RTL），原预计需 1.5 年手工完成，实际仅耗时 6 周。  

- 🚀 **高效迁移**：通过 LLM 和自动化工具，Airbnb 在 6 周内完成预计 1.5 年的测试文件迁移工作。  
- 🔄 **技术背景**：2020 年采用 RTL 替代 Enzyme，因 Enzyme 不再适配现代 React 测试实践，但手动迁移复杂且耗时。  
- 🤖 **自动化流程**：将迁移分解为多步骤并行处理，结合状态机模型和验证机制，确保文件逐步迁移。  
- 🔁 **重试机制**：通过动态提示和多次重试（最多 10 次），成功迁移大部分中低复杂度文件。  
- 📚 **丰富上下文**：为复杂文件提供多达 10 万 token 的上下文，包括相关文件、示例和迁移指南，显著提升成功率。  
- 📊 **持续优化**：采用“抽样 - 调整 - 扫描”循环，4 天内将成功率从 75% 提升至 97%，剩余 3% 手动完成。  
- 💰 **成本效益**：包括 LLM API 费用和 6 周工程时间，总成本远低于原手工迁移预估。  
- 🔮 **未来计划**：探索 LLM 在更多代码转换和开发者工具中的应用，提升工程效率。

---

## [{transitions} = f(state)](https://jordaneldredge.com/blog/transitions-f-of-state/)

**原文标题**: [{transitions} = f(state) / Jordan Eldredge](https://jordaneldredge.com/blog/transitions-f-of-state/)

**中文标题**: "过渡 = 函数 (状态) / 乔丹·埃尔德里奇"

将 React 应用视为状态机模型有助于理解异步更新和并发特性的影响。状态机通过明确系统状态和转移表来描述状态变化，而 React 通过组件树隐式定义状态转移规则。

- 🤖 **状态机模型**：React 应用可视为状态机，UI = f(state) 描述状态到 UI 的映射，同时隐式定义状态转移规则 {transitions} = f(state)。  
- 🛡️ **隐式防护**：组件通过事件处理函数限制用户操作，例如待办事项删除后不会渲染“完成”按钮，避免无效操作。  
- ⚡ **异步更新挑战**：网络请求导致状态延迟更新时（如删除待办需等待 API 响应），需手动防护（如乐观更新或禁用按钮）。  
- 🔄 **并发模式风险**：`startTransition`等特性可能允许无效操作窗口，需搭配同步更新（如`isPending`标志或乐观更新）确保安全。  
- 🛠️ **解决方案工具**：React 内置如`useOptimistic`和`useTransition`，帮助管理异步/并发更新的状态一致性。  
- 💡 **核心价值**：{transitions} = f(state) 模型强调组件在状态防护中的作用，指导安全实现异步/并发逻辑。  

（注：原文提及的示例、技术细节及致谢部分已浓缩至要点中。）

---

## [How I Reduced My React Bundle Size by Thirty Percent](https://www.frontendjoy.com/p/how-i-reduced-my-react-bundle-size-by-30-with-real-examples)

**原文标题**: [✨ How I Reduced My React Bundle Size by 30% (With Real Examples)](https://www.frontendjoy.com/p/how-i-reduced-my-react-bundle-size-by-30-with-real-examples)

**中文标题**: "✨ 我是如何将 React 包体积减小 30% 的（附真实案例）"

这篇文章分享了如何通过七个步骤减少 React 应用的打包体积，并提供了实际示例和代码变更。

- 🚀 通过七个步骤成功将 React 打包体积减少 30%，从 283.39kB 降至 198.33kB。  
- 🛠️ 使用 Vite 和 GitHub 上的示例项目进行演示，每个优化步骤都有独立分支。  
- 🌳 第一步：消除文件中的副作用，避免未使用的代码被打包。  
- 🔍 第二步：检测并删除未使用的文件和包，减少处理模块数量。  
- 📦 第三步：避免使用桶文件（barrel files），防止不必要的文件处理和副作用传播。  
- 📌 第四步：直接导出函数而非对象或类，避免未使用的方法被打包。  
- ⚖️ 第五步：用轻量级库（如 dayjs）替代重型库（如 moment.js）。  
- ⏳ 第六步：动态加载非关键包（如 Fuse.js），减少初始加载体积。  
- ⚛️ 第七步：使用 React.lazy 懒加载非关键组件，优化首次加载速度。  
- 📝 额外建议：在 package.json 中标记无副作用、使用工具监控打包体积、启用更多代码分割和压缩。  
- ✅ 最终效果：应用运行更快，构建时间更短，用户体验更佳。

---

## [How a Steam Locomotive from 1993 Broke My Yarn Test](https://blog.cloudflare.com/yarn-test-suffers-strange-derailment/)

**原文标题**: [A steam locomotive from 1993 broke my yarn test](https://blog.cloudflare.com/yarn-test-suffers-strange-derailment/)

**中文标题**: "一台 1993 年的蒸汽机车弄坏了我的纱线测试"

概述：作者在首次尝试运行 `yarn test` 时遭遇了神秘的 27 秒超时崩溃，最终发现是 Jest 与一个名为 `sl`（蒸汽火车动画程序）的命令行工具冲突所致。

- 🚂 作者在首次提交 React 代码时运行 `yarn test` 失败，报错信息极其模糊，仅显示 `[Error]`  
- 🔍 通过多次尝试发现测试总在 27 秒后崩溃，且与终端宽度无关  
- 🐧 Linux 系统复现问题，但同事的 MacOS 正常  
- 🛠️ 使用 `strace` 追踪发现 Jest 调用了 368 次 `sl` 命令（原为拼写错误的 `ls` 彩蛋程序）  
- 🚄 冲突源于 Jest 误将蒸汽火车程序当作版本控制工具 Sapling（`sl`）调用  
- ⏱️ 27 秒崩溃是因 4 轮并行测试（每轮 5 个 `sl` 进程，各耗时 6.7 秒）  
- 📜 错误日志显示 Jest 试图解析火车动画的 ANSI 转义码作为代码仓库路径  
- 🤖 问题修复后，Jest 团队幽默地加入了火车表情回应  
- 🔧 根本解决方案：重命名或卸载 `sl` 程序

---

## [Authorization in Next.js](https://www.robinwieruch.de/next-authorization/)

**原文标题**: [Authorization in Next.js](https://www.robinwieruch.de/next-authorization/)

**中文标题**: "Next.js 中的授权"

Next.js 中的授权实现指南，探讨了在 React Server Components 和 Server Actions 中如何通过 API 层、路由、UI 和中间件进行授权管理，强调授权应尽可能靠近数据源以确保安全性。

- 🔒 授权核心应放在 API 层，作为读写操作的第一道防线，通过自定义查询函数和 Server Actions 实现。
- 🛠 使用 `getAuth` 和 `getAuthOrRedirect` 函数验证用户会话，未授权时抛出错误或重定向到登录页。
- 🏗 随着应用规模增长，引入服务层和数据访问层进行更复杂的权限、角色和所有者检查。
- 🚧 路由授权可通过页面组件或布局组件实现，但布局组件的安全性较弱，建议在页面组件中进行独立检查。
- 👁 UI 授权主要用于提升用户体验，如隐藏未授权功能，但不可依赖其作为安全措施。
- ⚡ 中间件可用于路由保护，但应避免数据库密集型操作，仅进行轻量级检查如会话令牌验证。
- ⚠ 中间件存在性能限制和运行时环境问题，建议将关键授权逻辑放在后端层。
- 🔑 关键结论：授权应尽可能靠近敏感数据，确保 API、服务和数据访问层的安全性。

---

## [React Native 0.79: Faster Tooling and Much More](https://reactnative.dev/blog/2025/04/08/react-native-0.79)

**原文标题**: [React Native 0.79 - Faster tooling and much more · React Native](https://reactnative.dev/blog/2025/04/08/react-native-0.79)

**中文标题**: "React Native 0.79 - 更快的工具链及其他改进 · React Native"

React Native 0.79 版本带来了多项性能改进和新功能，包括更快的工具链、Android 启动优化、iOS 原生模块注册改进等，同时移除了一些旧特性。

- 🚀 **Metro 工具链提速**：Metro 0.82 支持延迟哈希，首次启动速度提升 3 倍以上，并稳定支持 `package.json` 的 `exports` 和 `imports` 解析。  
- 📦 **JSC 迁移至社区包**：JavaScriptCore (JSC) 引擎移至 `@react-native-community/javascriptcore`，未来将从核心库移除，Hermes 用户不受影响。  
- 🍏 **iOS Swift 兼容原生模块注册**：通过 `package.json` 的 `modulesProvider` 字段简化原生模块注册，支持纯 C++ 模块和 Swift `AppDelegate`。  
- ⚡ **Android 启动优化**：默认不再压缩 JS Bundle，显著减少启动时间（如 Discord TTI 减少 400ms），但会占用更多存储空间，可通过 `enableBundleCompression` 配置。  
- 🔧 **移除远程 JS 调试**：弃用 Chrome 远程调试，推荐使用 React Native DevTools 或 Expo DevTools 插件。  
- ♻️ **内部模块改用 `export` 语法**：约 46 个 API 更新为 ES 模块语法，建议从根路径导入（如 `import {ImageBackground} from 'react-native'`）。  
- ⚠️ **其他破坏性变更**：包括不支持无单位阴影/滤镜值、修正 `hwb()` 语法、更新 `ExceptionsManager` 导出方式等。  
- 🙏 **致谢**：感谢 100 位贡献者的 944 次提交，特别提及 Marc Rousavy、Kudo Chien 等社区成员的关键贡献。  
- 🔄 **升级指南**：建议使用 React Native Upgrade Helper 或通过 CLI 创建新项目（`npx @react-native-community/cli init`），Expo SDK 53 将默认支持此版本。

---

## [Fancy Components: A Growing Library of Ready-to-Use Animated React Components](https://www.fancycomponents.dev/)

**原文标题**: [Fancy Components](https://www.fancycomponents.dev/)

**中文标题**: "精美组件"

网站提供免费开源的 React 组件和微交互库，帮助用户轻松打造精美网站。

- 🌟 提供丰富的 React 组件和微交互效果  
- 🆓 完全免费且开源  
- 📚 附带详细文档方便查阅  
- ⚡ 可快速提升网站视觉吸引力  
- 💻 GitHub 上可获取资源

---

## [Try them out here](https://www.fancycomponents.dev/components)

**原文标题**: [Fancy Components](https://www.fancycomponents.dev/components)

**中文标题**: "精美组件"

这是一个关于网页组件库的文档页面，展示了各种动态文本、背景、物理效果、图像和区块组件的分类列表。

- 📚 **文档与资源** - 提供文档、组件说明和 GitHub 链接，支持主题切换。  
- 🚀 **入门指南** - 包含简介、安装步骤、组件列表和更新日志。  
- ✍️ **文本效果（18 种）** - 如字母交换悬停、垂直切割显示、变量字体悬停、打字机效果等，部分标记为“更新”。  
- 🎨 **背景效果（2 种）** - 含 SVG 动画渐变和像素轨迹，部分标记为“更新”。  
- ⚛️ **物理效果（3 种）** - 弹性线条、重力模拟和光标吸引效果，部分标记为“更新”。  
- 🖼️ **图像组件（2 种）** - 图像拖尾和视差漂浮效果，含 Beta 测试功能。  
- 🔍 **滤镜效果（2 种）** - 粘性 SVG 滤镜和像素化 SVG 滤镜。  
- 🧱 **区块组件（9 种）** - 拖拽元素、环绕元素、堆叠卡片等，含“新”功能和“更新”标记。  
- ❤️ **制作信息** - 由“nonzeroexitcode”基于爱心构建。

---

## [Konva: A JavaScript 2D Canvas Library](https://konvajs.org/)

**原文标题**: [Konva - JavaScript Canvas 2d Library](https://konvajs.org/)

**中文标题**: "Konva - JavaScript 2D 画布库"

全球团队信赖的 2D 画布框架 Konva，基于 npm 下载量最受欢迎  

- 🌍 **全球团队信赖**  
  被 Meta、Microsoft、Polotno 等知名团队广泛使用  

- 📊 **领先的 2D 框架**  
  npm 下载量最高的 2D 画布框架  

- 🧩 **面向对象 API**  
  提供丰富的图形支持和直观的画布操作  

- 📱 **跨平台兼容**  
  支持桌面和移动设备，体验一致  

- 🎬 **动画与过渡**  
  内置动画和补间功能，打造动态交互  

- 🏗️ **高级节点管理**  
  支持节点嵌套、分组和事件冒泡  

- 🖼️ **高质量导出**  
  可导出为多种格式，适用不同场景  

- 🎨 **内置滤镜**  
  提供多种预设滤镜，轻松添加视觉效果  

- 🔌 **框架集成**  
  与 React、Vue、Svelte 等主流框架无缝兼容  

- 🖱️ **拖放功能**  
  内置拖放支持，提升用户交互体验  

- 🛠️ **应用案例**  
  包括 Polotno 设计编辑器、SMMplanner 故事制作、Pixteller 图像工具等多样化场景  

- ➕ **开放生态**  
  欢迎开发者提交自己的应用案例

---

## [demos with code](https://konvajs.org/docs/sandbox.html)

**原文标题**: [Demos | Konva - JavaScript Canvas 2d Library](https://konvajs.org/docs/sandbox.html)

**中文标题**: "演示 | Konva - JavaScript 2D 画布库"

Konva 是一个功能丰富的 Canvas 库，提供多种演示和教程，适用于游戏、应用开发和常见用例。

- 🎮 **游戏与应用** - 包括“命运之轮”、“自由绘图”和“海滩动物游戏”等互动示例。  
- 🖌️ **常见用例** - 支持可编辑文本、富文本渲染、Canvas 滚动、GIF 动画、视频显示和 SVG 渲染等功能。  
- ⚡ **性能测试** - 提供压力测试，如拖放压力测试、动画压力测试和 20000 个节点的渲染测试。  
- 🛠️ **其他演示** - 包含碰撞检测、触摸手势、多触点缩放和响应式 Canvas 舞台等多样化示例。  
- 📚 **文档与社区** - 提供教程、API 参考和社区支持（Stack Overflow、Discord、Twitter 等）。  
- 🔗 **框架集成** - 支持 React、Vue 和 Svelte 等流行框架。

---

## [Vue](https://konvajs.org/docs/vue/index.html)

**原文标题**: [Getting started with Vue and Canvas via Konva | Konva - JavaScript Canvas 2d Library](https://konvajs.org/docs/vue/index.html)

**中文标题**: "使用 Konva 入门 Vue 与 Canvas | Konva - JavaScript 2d Canvas 库"

Vue Konva 是一个用于通过 Vue 绘制复杂 Canvas 图形的 JavaScript 库，它提供了对 Konva 框架的声明式和响应式绑定。

- 🎨 **Vue Konva 简介**：Vue Konva 是一个 JavaScript 库，用于在 Vue 中绘制复杂的 Canvas 图形，提供对 Konva 框架的声明式和响应式绑定。
- 🔧 **组件对应关系**：所有 `vue-konva` 组件与 `Konva` 组件同名，前缀为 `v-`，所有 `Konva` 对象的参数可作为 `config` 属性传递给对应的 `vue-konva` 组件。
- 📐 **核心形状**：包括 `v-rect`、`v-circle`、`v-ellipse`、`v-line`、`v-image`、`v-text`、`v-text-path`、`v-star`、`v-label`、`v-path`、`v-regular-polygon`，还支持自定义形状。
- 🚀 **快速开始**：需要 Vue.js 3，通过 npm 安装 `vue-konva` 和 `konva`，导入并使用 `VueKonva`。
- 💻 **使用示例**：提供了一个拖拽星星的示例，星星在拖拽时会放大，释放后恢复原大小。
- 📦 **CDN 使用**：也可以通过 CDN 引入 Vue、Konva 和 VueKonva，快速在 HTML 中使用。
- 🔗 **更多信息**：可以参考 [Konva 概述](https://konvajs.org/docs/overview.html) 获取更多关于 Konva 的信息。

---

## [Svelte](https://konvajs.org/docs/svelte/index.html)

**原文标题**: [Getting started with Svelte and canvas via Konva | Konva - JavaScript Canvas 2d Library](https://konvajs.org/docs/svelte/index.html)

**中文标题**: "通过 Konva 入门 Svelte 与 Canvas | Konva - JavaScript 2d Canvas 库"

概述：  
Svelte-Konva 是一个用于在 Svelte 中绘制复杂 Canvas 图形的 JavaScript 库，它提供了对 Konva 框架的声明式和响应式绑定。  

- 🎨 **Svelte-Konva 简介**：一个通过 Svelte 绘制复杂 Canvas 图形的库，基于 Konva 框架。  
- 🔗 **GitHub 地址**：[konvajs/svelte-konva](https://github.com/konvajs/svelte-konva)  
- 📌 **组件对应关系**：所有 `svelte-konva` 组件与 `Konva` 组件同名，参数通过 `config` 属性传递。  
- 📚 **Konva 文档**：更多信息可参考 [Konva Overview](https://konvajs.org/docs/overview.html)。  
- ⚡ **快速开始**：  
  - 1️⃣ **安装**：通过 npm 安装 `svelte-konva` 和 `konva`（`npm i svelte-konva konva`）。  
  - 2️⃣ **使用示例**：导入组件并配置 Canvas 图形（如矩形）。  
- 💡 **示例代码**：展示了如何创建一个带蓝色矩形的 Canvas 画布。

---

## [React.](https://konvajs.org/docs/react/index.html)

**原文标题**: [Getting started with React and Canvas via Konva | Konva - JavaScript Canvas 2d Library](https://konvajs.org/docs/react/index.html)

**中文标题**: "通过 Konva 入门 React 与 Canvas | Konva - JavaScript 2D Canvas 库"

概述：react-konva 是一个用于通过 React 绘制复杂 Canvas 图形的 JavaScript 库，提供了对 Konva 框架的声明式和响应式绑定，但不支持 React Native 环境。

- 🎨 react-konva 是一个 JavaScript 库，用于通过 React 绘制复杂的 Canvas 图形。  
- 🔗 它提供了对 Konva Framework 的声明式和响应式绑定。  
- ⚠️ 目前不支持 React Native 环境。  
- 🖱️ 支持所有 Konva 节点、形状和事件作为 React 组件。  
- 🌐 更多示例可参考 [Konva 官网](https://konvajs.org/)。  
- 📦 安装方式：`npm install react-konva konva --save`。  
- 📝 示例代码展示了如何创建带有文本、矩形和圆形的 Canvas。  
- 🔄 Konva 对于 react-konva 就像 DOM 对于 React 一样。

---

## [React Testing Library 16.3](https://github.com/testing-library/react-testing-library)

**原文标题**: [GitHub - testing-library/react-testing-library: 🐐 Simple and complete React DOM testing utilities that encourage good testing practices.](https://github.com/testing-library/react-testing-library)

**中文标题**: GitHub - testing-library/react-testing-library: � 简单而全面的 React DOM 测试工具，助力良好测试实践

React Testing Library 是一个轻量级的 React DOM 测试工具库，旨在鼓励良好的测试实践，使测试更接近用户实际使用方式，从而提高测试的可信度。

- 🐐 简单且完整的 React DOM 测试工具，鼓励良好的测试实践  
- 📜 遵循 MIT 许可证  
- ⭐ 19.2k 星标，1.1k 复刻  
- 🚀 主要目标：测试应避免包含组件的实现细节，而是关注功能  
- 🛠️ 安装方式：通过 npm 或 yarn 安装 `@testing-library/react` 和 `@testing-library/dom`  
- 📚 提供丰富的文档和示例，包括基础示例和复杂示例  
- 🔧 支持 React Hooks 测试，推荐使用 React Hooks Testing Library  
- 🧩 兼容 React DOM 16.8 及以上版本，提供解决兼容性问题的方案  
- 🤝 鼓励社区贡献，提供 Good First Issue 标签供新手参与  
- 🌍 支持多种测试场景，包括 Redux、Router 和 Context 等  
- 📖 文档详细，包括安装指南、示例和贡献指南

---

## [TanStack Form 1.3](https://github.com/TanStack/form)

**原文标题**: [GitHub - TanStack/form: 🤖 Headless, performant, and type-safe form state management for TS/JS, React, Vue, Angular, Solid, and Lit.](https://github.com/TanStack/form)

**中文标题**: GitHub - TanStack/form: 🤖 为 TS/JS、React、Vue、Angular、Solid 和 Lit 提供的无头、高性能且类型安全的表单状态管理工具

TanStack Form 是一个无头、高性能且类型安全的表单状态管理库，支持多种前端框架和技术栈。

- 🤖 无头、高性能且类型安全的表单状态管理，适用于 TS/JS、React、Vue、Angular、Solid 和 Lit  
- 🌐 官网：[tanstack.com/form](https://tanstack.com/form)  
- 📜 许可证：MIT  
- ⭐ GitHub 星标：5.2k  
- 🍴 Fork 数：435  
- 🔧 支持多种技术栈：React、Angular、Vue、Solid、Lit  
- 📚 提供文档、指南和 API 参考  
- 🏷️ 相关主题：react、hooks、angular、vue、solid、forms、tanstack  
- 🛠️ 活跃开发：1,258 次提交，139 位贡献者  
- 📦 主要语言：TypeScript (99.2%)

---

## [Embla Carousel 8.6](https://github.com/davidjerleke/embla-carousel)

**原文标题**: [GitHub - davidjerleke/embla-carousel: A lightweight carousel library with fluid motion and great swipe precision.](https://github.com/davidjerleke/embla-carousel)

**中文标题**: GitHub - davidjerleke/embla-carousel: 轻量级轮播库，流畅动画，精准滑动。

Embla Carousel 是一个轻量级的轮播库，具有流畅的动画效果和精确的滑动控制，支持多种框架且无依赖。

- 🚀 **开源项目** - MIT 许可证，完全开源，由 David Jerleke 创建。  
- 🌟 **受欢迎程度** - 获得 6.9k 星标，被 225k+ 项目使用。  
- 🛠 **跨框架支持** - 提供 React、Solid、Angular 等框架的封装。  
- 📱 **响应式设计** - 专为移动端优化，支持触摸滑动和手势操作。  
- 📂 **插件扩展** - 支持插件如 Embla Carousel Wheel Gestures 等。  
- 🤝 **社区贡献** - 有 48 位贡献者，欢迎更多参与。  
- 🌍 **资源丰富** - 提供文档、示例和生成器工具。

---

## [simpleParallax.js 6.1](https://github.com/geosigno/simpleParallax.js)

**原文标题**: [GitHub - geosigno/simpleParallax.js: Easy Parallax Effect for React & JavaScript](https://github.com/geosigno/simpleParallax.js)

**中文标题**: "GitHub - geosigno/simpleParallax.js: 适用于 React 和 JavaScript 的简易视差效果"

simpleParallax.js 是一个轻量级且易于使用的 React 和 JavaScript 库，用于为任何图像添加视差动画效果。它以其简单性和出色的视觉效果著称，支持直接应用于图像标签，无需背景图像。

- 🚀 **功能特点**：简单易用，支持任何图像和视频，提供多种自定义设置如方向、缩放、延迟等。
- 📦 **安装方式**：可通过 npm 或 yarn 安装，支持 React 和原生 JavaScript 版本。
- ⚙️ **初始化**：提供 React 和原生 JavaScript 的初始化代码示例，支持多图像和视频。
- 🛠️ **设置选项**：包括方向（上下左右及对角线）、缩放比例、溢出控制、延迟时间、过渡效果等。
- 🔄 **方法**：支持刷新和销毁实例，适应动态内容变化。
- 🌍 **兼容性**：支持现代浏览器，旧版浏览器需额外 polyfill。
- 📜 **许可证**：MIT 许可证，开源免费使用。
- 👨💻 **作者与贡献**：由 Geoffrey Signorato 创建，欢迎社区贡献。
- 🔗 **资源与示例**：提供详细文档和示例，方便快速上手。

---

## [This article on using notebook-style programming](https://deno.com/blog/exploring-art-with-typescript-and-jupyter)

**原文标题**: [Exploring Art with TypeScript, Jupyter, Polars, and Observable Plot](https://deno.com/blog/exploring-art-with-typescript-and-jupyter)

**中文标题**: "使用 TypeScript、Jupyter、Polars 和 Observable Plot 探索艺术"

概述：本文介绍了如何使用 TypeScript、Jupyter、Polars 和 Observable Plot 来探索艺术数据，特别是美国国家美术馆（NGA）的开放数据集。文章详细说明了如何加载、清理和分析数据，并通过可视化和交互式组件揭示数据集中的模式和见解。

- 🚀 Deno 内置 Jupyter 内核，简化了 JavaScript 和 TypeScript 在数据科学中的应用。  
- 📊 使用 Polars 进行高效的数据清理和合并，创建统一的数据集。  
- 🎨 通过 Observable Plot 生成静态图表，分析艺术品类型、年代和公共领域状态。  
- 🔍 发现数据中的异常现象，如 1940 年代公共领域绘画的激增。  
- 🛠️ 利用自定义 JSX 组件和 anywidgets 增加交互性，提升数据探索体验。  
- 📚 最终揭示数据集中的历史背景，如大萧条时期的联邦艺术项目。

---

## [A detailed guide to modern testing with Node.js](https://github.com/goldbergyoni/nodejs-testing-best-practices#readme)

**原文标题**: [GitHub - goldbergyoni/nodejs-testing-best-practices: Beyond the basics of Node.js testing. Including a super-comprehensive best practices list and an example app (April 2025)](https://github.com/goldbergyoni/nodejs-testing-best-practices#readme)

**中文标题**: GitHub - goldbergyoni/nodejs-testing-best-practices: Node.js 测试进阶指南。包含一份超级全面的最佳实践清单和示例应用（2025 年 4 月）

overview summary  
Node.js 测试最佳实践指南，涵盖 50+ 条现代测试实践，包含示例应用和高级主题（如数据库、外部服务、消息队列测试等）。作者团队基于 50+ 公司咨询经验总结，提供从策略到具体技术的完整方案。

- 🚀 **核心策略**  
  - 优先编写组件/集成测试（覆盖 99% 的 bug）  
  - 少量 E2E 测试（3-10 个）  
  - 测试功能而非函数  

- 🛠 **基础设施**  
  - 使用 Docker-Compose 管理测试数据库  
  - 优化数据库配置（牺牲持久性换性能）  
  - 测试时数据存储在内存目录  

- 🌐 **Web 服务器**  
  - 测试与后端同进程运行  
  - 测试控制服务器启停  
  - 生产环境固定端口，测试环境随机端口  

- 🧩 **测试结构**  
  - 按路由/用户故事组织测试  
  - 断言整个 HTTP 响应对象  
  - 测试 5 类结果：响应、新状态、外部调用、消息队列、可观测性  

- 🔗 **外部服务**  
  - 使用 Nock 拦截 HTTP 请求  
  - 默认拒绝未拦截的请求  
  - 模拟网络异常（超时/错误）  

- 🗃 **数据处理**  
  - 每个测试仅操作自己的数据  
  - 通过公共 API 断言新状态  
  - 唯一字段添加随机后缀  

- 📨 **消息队列**  
  - 使用内存假队列（避免 Flaky 测试）  
  - 测试消息确认/重试逻辑  
  - 验证消息幂等性  

- 🤹 **Mocking**  
  - 区分隔离 Mock（推荐）/模拟 Mock/实现 Mock（避免）  
  - 每次测试前清理 Mock  
  - 优先选择类型安全的 Mock 方案  

- 🎓 **学习资源**  
  - 包含完整示例应用（40 个测试 5 秒完成）  
  - 提供在线课程/工作坊  
  - 支持 Nest.js/Fastify 等额外场景

---

## [Ryan Dahl gives us an update](https://deno.com/blog/deno-v-oracle3)

**原文标题**: [Deno v Oracle Update 3: Fighting the JavaScript Trademark](https://deno.com/blog/deno-v-oracle3)

**中文标题**: Deno 对 Oracle 第三回合：JavaScript 商标之争

Oracle 与 Deno 就 JavaScript 商标权的争议持续发酵，目前案件进展至关键阶段，等待美国专利商标局（USPTO）的裁决。

- 🕰️ **历史背景**：1995 年 Sun Microsystems 与 Netscape 合作创建 JavaScript 语言并持有商标，2009 年 Oracle 收购 Sun 后继承商标，但长期未参与语言发展。  
- 📜 **关键事件**：2024 年 9 月，Ryan Dahl 联合 1.8 万名开发者发布公开信，指控商标被滥用；11 月 Deno 正式提交撤销商标申请，理由包括通用性、废弃及欺诈（Oracle 提交 Node.js 作为使用证据）。  
- ⚖️ **法律交锋**：2025 年 2 月 Oracle 申请驳回欺诈指控，辩称提交的 Node.js 证据无关紧要；3 月 Deno 反驳称误导行为不可忽视。  
- 🔍 **争议焦点**：Oracle 是否通过虚假材料维持商标权，以及“JavaScript”是否已成为通用术语或遭废弃。  
- ⏳ **后续流程**：未来 3-4 周商标审判委员会将裁定欺诈指控是否成立，若驳回则案件继续基于通用性和废弃条款审理；若成立，Oracle 需全面回应。  
- 🏻 **核心问题**：商标法旨在保护商品来源标识，而非允许企业囤积未实际使用的商标。Oracle 长期未参与 JavaScript 生态却持有商标，形成法律灰色地带。  
- ✊ **行动呼吁**：开发者可通过签署公开信（已超 1.8 万人）或分享事件推动商标回归公共领域。  

（注：Emoji 已按规则添加，概述部分未加标题，直接呈现核心内容。）

---

## [JSHeroes conference](https://jsheroes.io/)

**原文标题**: [JSHeroes 2025 | Community Organized JS Conference](https://jsheroes.io/)

**中文标题**: "JSHeroes 2025 | 社区组织的 JS 大会"

2025 年 JSHeroes 大会将于 5 月 29 日至 30 日在罗马尼亚克卢日举行，这是一个由社区组织的非营利性 JavaScript 和前端技术盛会。以下是关键信息：

- 🎉 **活动概述**：为期两天的单轨道会议，聚焦 JS 和 Web 技术，注重高质量内容、社交和趣味性。
- 📅 **日期**：2025 年 5 月 29 日 -30 日。
- 🎟️ **门票**：可通过 ti.to 页面购买。
- 🌍 **主题**：弥合技术债务与工具之间的差距，涵盖 Web 开发的各个方面。
- 🎤 **演讲嘉宾**：
  - Andrei Pfeiffer：代码词源学与文档重要性。
  - Atila Fassina：安全优先的 Web 应用开发。
  - Bramus Van Damme：CSS 滚动驱动动画。
  - Chelsea Troy：LLM 对软件工程的影响。
  - Dan Shappir：RPC 的复兴。
  - Emilia Mureșan：技术债务管理。
  - 更多嘉宾涵盖 TypeScript、React、Angular、Qwik 等技术。
- 📝 **议程亮点**：
  - 第一天：代码管理、表单验证、React 性能、技术迁移等。
  - 第二天：RPC、Express 5.0、可访问性、CSS 层、Angular 最新动态等。
- 🏛️ **场地**：克卢日 Grand Hotel Italia，无障碍设施完善。
- 💡 **透明度**：活动完全开源，数据公开，鼓励知识共享。
- 🤝 **赞助与合作伙伴**：包括金牌、银牌和铜牌赞助商及媒体合作伙伴。
- 👥 **组织团队**：由 Ale Retegan、Alex Moldovan 等领导，多位志愿者支持。
- 🌟 **大使**：包括 Andrei Antal、Carmen Popoviciu 等社区领袖。

---

