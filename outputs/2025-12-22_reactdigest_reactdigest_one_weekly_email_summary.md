### [React 文摘：电子邮件通讯](https://reactdigest.net/)

**原文标题**: [React Digest: Email Newsletter](https://reactdigest.net/)

React Digest 是一份面向 React 开发者精心策划的每周通讯，汇集了精选文章与简短摘要，帮助超过 25,034 名前端工程师高效学习新知、节省寻找优质内容的时间。

- 📰 每周为 React 开发者推送精选文章与摘要
- 👥 已吸引超过 25,034 名前端工程师订阅
- ⏱️ 帮助开发者节省筛选内容时间，每周持续学习
- 📚 内容涵盖 React 并发模式等实用技术主题
- 🌍 受到全球前端工程师广泛好评与使用

---

### [React RCE 事件的经验教训](https://sgued.fr/blog/react-rce/)

**原文标题**: [Lessons learned from React's RCE](https://sgued.fr/blog/react-rce/)

近期在 React 框架中发现三个安全漏洞，其中最严重的是利用 Flight 协议实现的服务器端远程代码执行（RCE）漏洞，其余两个分别为拒绝服务攻击和源代码暴露漏洞。本文探讨了通过 Node.js 运行时配置来缓解此类漏洞的潜在方案。

- 🚨 **高危漏洞**：CVE-2025-55182 利用 Flight 协议中 Promise 序列化、块引用和原型链特性，通过`__proto__`访问构造函数实现远程代码执行
- 🔄 **协议缺陷**：Flight 协议尝试序列化包含行为逻辑的完整对象（如闭包状态），类似 PHP 反序列化漏洞的设计模式存在安全隐患
- ⚡ **阻断攻击**：CVE-2025-67779 通过创建循环引用的数据块使解析器陷入无限循环，导致服务器拒绝服务
- 📜 **源码泄露**：CVE-2025-55183 利用函数默认的`toString()`方法暴露服务器端源代码
- 🛡️ **关键防护**：Node.js 的`--disallow-code-generation-from-strings`标志可禁用`eval`和 Function 构造函数，能有效阻断 RCE 攻击向量
- 🔧 **原型防护**：`--disable-proto=delete`标志可移除对象的`__proto__`属性，增加原型污染攻击难度
- ❄️ **实验特性**：`--frozen-intrinsics`标志通过冻结内置对象原型防止原型污染，目前仍处于实验阶段
- 📊 **现状反思**：现有 Node.js 安全实践文档未充分推荐这些防护标志，尽管它们能显著提升应用安全性且兼容性良好

---

### [精密 AI - 无需编写测试的自动化前端测试](https://www.meticulous.ai/?utm_source=react_digest)

**原文标题**: [Meticulous AI - Automated Frontend Testing Without Writing Tests](https://www.meticulous.ai/?utm_source=react_digest)

Meticulous AI 是一款创新的自动化测试工具，通过记录用户与应用交互生成并维护测试套件，无需手动编写或修复测试，帮助开发团队高效、无差错地发布代码。

- 🚀 **无需编写测试** – 通过记录用户交互自动生成覆盖所有代码分支和边缘情况的测试套件，无需手动编写或维护测试。
- 🔄 **测试自动演进** – 随着应用更新，测试套件自动添加新功能测试并淘汰过时测试，保持测试始终最新且完整。
- ⚡ **闪电般快速执行** – 利用并行计算集群，可在 120 秒内完成数千个屏幕的测试，大幅提升测试效率。
- 🛡️ **彻底消除测试波动** – 从底层构建确定性调度引擎，确保测试结果稳定可靠，无随机失败。
- 🔗 **无缝集成现有流程** – 可单独使用或与现有测试套件结合，支持多种前端框架（如 React、Vue、Angular 等）。
- 📈 **提升开发信心** – 已在 Dropbox、Notion 等超过 100 家机构中应用，帮助团队预防回归错误，加速可靠代码的交付。

---

### [你可能不需要使用 Effect – React](https://react.dev/learn/you-might-not-need-an-effect)

**原文标题**: [You Might Not Need an Effect – React](https://react.dev/learn/you-might-not-need-an-effect)

React 的 Effect 是用于与外部系统同步的“逃生舱”，但许多场景下并不需要它。移除不必要的 Effect 可以使代码更易维护、性能更高且减少错误。

- 🚫 **避免在渲染数据转换时使用 Effect**：例如过滤列表，应在渲染时直接计算，而非通过 Effect 更新状态，以避免不必要的渲染循环。
- 🎯 **用户事件处理应放在事件处理器中**：如发送 API 请求或显示通知，事件处理器能明确用户操作意图，而 Effect 可能无法区分。
- 🔄 **基于 props 或 state 的状态更新无需 Effect**：例如计算全名，应在渲染时直接派生，而非通过 Effect 设置额外状态。
- 💾 **使用 useMemo 缓存昂贵计算**：避免重复执行慢速函数，仅在依赖项变化时重新计算。
- 🔑 **通过 key 重置组件状态**：当 prop 变化时，使用 key 属性让 React 重新创建组件，以自动重置内部状态。
- ⚡ **在事件处理器中批量更新状态**：避免链式 Effect 导致多次渲染，将相关状态更新集中在同一事件中处理。
- 📡 **仅将 Effect 用于同步外部系统**：如订阅浏览器 API 或第三方库，但优先使用 useSyncExternalStore 等内置 Hook。
- 🧹 **数据获取时需处理竞态条件**：添加清理函数忽略过时响应，或使用框架提供的数据获取机制。
- 🏗️ **应用初始化逻辑应放在模块作用域**：避免在 Effect 中运行仅需执行一次的代码，防止开发环境重复执行。
- 🔁 **状态提升简化数据流**：当子组件需通知父组件时，考虑将状态提升至父组件，使数据流向更清晰。

---

### [介绍 RSC Explorer — 过度反应](https://overreacted.io/introducing-rsc-explorer/)

**原文标题**: [Introducing RSC Explorer — overreacted](https://overreacted.io/introducing-rsc-explorer/)

本文介绍了 RSC Explorer 工具，它通过可视化方式演示 React Server Components（RSC）协议的工作原理，帮助开发者理解 RSC 的序列化、流式传输和客户端 - 服务器交互机制。

- 🔍 **RSC 协议背景**：近期因安全漏洞披露，RSC 协议受到关注。该协议是 React 用于序列化/反序列化组件树的格式，属于 React 内部实现细节，未公开文档。
- 🛠️ **工具诞生动机**：作者为满足社区对 RSC 底层原理的兴趣，开发了 RSC Explorer（https://rscexplorer.dev/），以交互方式展示 RSC 协议运作过程。
- 🌐 **核心功能演示**：
  - **基础示例**：展示 JSX（如`<h1>Hello</h1>`）如何通过 RSC 协议跨网络传输并在客户端重建。
  - **流式传输**：通过异步组件示例演示 Suspense 边界和部分 UI 流式渲染。
  - **代码传输**：计数器示例显示服务器可向客户端发送组件代码（如`Counter`模块引用），而非静态 HTML。
  - **双向交互**：表单操作示例展示客户端如何调用服务器端声明的 Server Action。
  - **无框架路由**：通过定时器示例演示如何在不依赖框架的情况下实现服务器内容刷新和状态保持。
- 📚 **扩展示例**：工具还提供分页、错误处理、客户端引用等高级案例，甚至包含安全漏洞 CVE-2025-55182 的演示。
- 🎯 **开源与共享**：工具完全在浏览器端运行，支持代码片段嵌入和链接分享，源码已开放于 Tangled 和 GitHub 平台。

---

### [React 编译器的静默故障（及修复方法）| acusti.ca](https://acusti.ca/blog/2025/12/16/react-compiler-silent-failures-and-how-to-fix-them/)

**原文标题**: [React Compiler’s Silent Failures (And How to Fix Them) | acusti.ca](https://acusti.ca/blog/2025/12/16/react-compiler-silent-failures-and-how-to-fix-them/)

React Compiler 消除了手动记忆化的认知负担，但存在静默失败问题，即无法编译某些组件时不会报错，可能导致性能下降。通过启用未记录的 ESLint 规则 `react-hooks/todo`，可以在编译失败时中断构建，确保关键组件的优化。常见的不支持模式包括解构后修改 props 和复杂的 try/catch 块，但可通过代码调整或禁用规则来处理非关键组件。

- 🧠 React Compiler 自动处理记忆化，解放开发者心智负担，不再需要手动使用 `useMemo` 和 `useCallback`。
- ⚠️ 编译器在无法优化组件时会静默失败，回退到标准 React 行为，可能影响高性能交互界面的用户体验。
- 🔍 通过启用 ESLint 规则 `react-hooks/todo`，可以将编译失败转为构建错误，确保关键组件被正确优化。
- 🚫 常见的不支持模式包括：解构 props 后直接修改、try/catch 块中包含条件语句或复杂逻辑。
- 🔧 解决方案包括：避免修改解构的 props、简化 try/catch 逻辑，或对非关键组件禁用 lint 规则。
- 📈 尽管存在临时限制，React Compiler 仍推荐用于高性能交互界面，其长期收益远大于当前局限。

---

### [React 服务器组件性能入门 - 网页性能日历](https://calendar.perfplanet.com/2025/intro-to-performance-of-react-server-components/)

**原文标题**: [  Intro to Performance of React Server Components - Web Performance Calendar](https://calendar.perfplanet.com/2025/intro-to-performance-of-react-server-components/)

本文探讨了 React 服务器组件（RSC）对 Web 性能的影响，通过对比客户端渲染（CSR）、服务器端渲染（SSR）及 RSC 在不同场景下的性能数据，分析了 RSC 在提升初始加载速度、减少 JavaScript 捆绑包大小方面的潜力，同时指出了其实现复杂度、对数据获取的依赖以及迁移成本等挑战。

- 🚀 React 服务器组件通过将更多工作移至服务器、减少客户端 JavaScript 加载，显著提升初始页面加载性能，尤其是在涉及数据获取时。
- ⏱️ 实验数据显示，使用 Next.js App 路由器（支持 Suspense 的服务器获取）时，LCP、侧边栏和消息列表的显示时间均优化至约 1.28 秒，优于传统 SSR。
- 🔄 RSC 结合流式渲染，允许服务器分块发送内容，实现渐进式加载，从而更快地显示动态数据，但可能导致 HTML 响应时间延长。
- ⚖️ 性能提升高度依赖于数据获取场景；若无需动态数据，RSC 与传统 SSR 性能相近，且迁移需全面重构应用架构，成本较高。
- 🛡️ RSC 仍处于快速发展阶段，存在模式不成熟、工具支持有限及安全风险（如近期漏洞），需谨慎评估其适用性。

---

### [CSS 2025 年度回顾](https://chrome.dev/css-wrapped-2025/)

**原文标题**: [CSS Wrapped 2025](https://chrome.dev/css-wrapped-2025/)

本文介绍了 2024 年 CSS 和 HTML 的一系列新特性与改进，涵盖交互组件、滚动体验、动画优化及样式增强等方面，旨在提升开发者构建现代 Web 应用的能力与效率。

- 🎛️ **调用器命令**：通过`commandfor`和`command`属性，无需 JavaScript 即可声明式控制`<dialog>`和`[popover]`元素的显示、隐藏等操作，支持自定义命令。
- 🖱️ **对话框轻量关闭**：`<dialog>`新增`closedby`属性，支持点击外部或按 ESC 键关闭对话框，提升用户体验。
- 💡 **提示弹出层**：`popover="hint"`创建临时性弹出层（如工具提示），不关闭其他弹出层，并可结合`interestfor`属性实现悬停触发。
- 🎨 **可自定义选择框**：通过`appearance: base-select`完全用 CSS 样式化`<select>`元素，支持 HTML 内容嵌入和下拉列表顶层渲染。
- 🚗 **滚动按钮与标记**：`::scroll-button()`和`::scroll-marker()`伪元素实现原生可访问的轮播图导航，无需 JavaScript。
- 🔗 **滚动目标组**：`scroll-target-group`属性将锚点链接列表转换为滚动标记，结合`:target-current`实现滚动高亮导航。
- 🎯 **锚定容器查询**：`container-type: anchored`和`anchored()`函数使元素能根据锚点位置变化调整样式，如自动翻转工具提示箭头。
- 🕵️ **兴趣调用器**：`interestfor`属性声明式实现悬停或聚焦触发的 UI（如提示卡片），支持延迟设置，提升可访问性。
- 📜 **滚动状态查询**：`container-type: scroll-state`允许 CSS 查询元素的滚动状态（如吸附、可滚动），并据此样式化后代元素。
- 🔢 **树计数函数**：`sibling-index()`和`sibling-count()`函数简化基于元素位置的动画和布局，实现自动适应的交错效果。
- 🖼️ **嵌套视图过渡组**：`view-transition-group`属性支持在视图过渡中嵌套`::view-transition-group`，保留 3D 和裁剪效果。
- 🏗️ **DOM 状态保留移动**：`moveBefore`方法在移动 DOM 元素（如 iframe、视频）时保持其状态（如播放、焦点），避免重新加载。
- 🛠️ **高级 attr() 函数**：增强版`attr()`支持更多 CSS 属性和数据类型（如颜色、长度），实现基于 HTML 属性的动态样式。
- 🔍 **ToggleEvent.source**：`ToggleEvent`的`source`属性标识触发弹出层、对话框等切换事件的元素，便于事件处理。
- 📏 **文本框特性**：`text-box-trim`和`text-box-edge`属性优化文本垂直对齐，实现视觉居中效果。
- ✂️ **shape() 函数**：`clip-path: shape()`创建复杂响应式裁剪形状，支持动画和自定义属性，增强视觉效果。
- ⚖️ **if() 语句**：CSS 中的`if()`函数提供条件样式，支持媒体查询、特性查询和样式查询，简化动态样式逻辑。
- 🔧 **自定义函数**：`@function`定义可重用的 CSS 函数，提高代码复用性和可维护性，如条件性圆角函数。
- 📊 **扩展范围语法**：样式查询和`if()`语句支持范围比较（如`>`、`<`），实现基于数值条件的样式调整。
- 📐 **拉伸尺寸关键字**：`stretch`关键字使元素填充包含块，同时保留外边距，不同于`100%`的盒模型计算。
- 🟦 **角形状**：`corner-shape`属性提供多种角形状（如斜角、凹口、圆形），超越传统圆角，支持动画和超级椭圆曲线。

---

### [深度卡片难题 – Frontend Masters 博客](https://frontendmasters.com/blog/the-deep-card-conundrum/)

**原文标题**: [The Deep Card Conundrum – Frontend Masters Blog](https://frontendmasters.com/blog/the-deep-card-conundrum/)

本文探讨了在网页设计中实现“深度卡片”效果的挑战与解决方案，即让卡片内部呈现 3D 立体空间并随卡片旋转而保持透视效果，同时确保内容不超出卡片边界。

- 🧩 **深度卡片概念**：将传统扁平卡片转变为内含 3D 立体空间的“窗口”，旋转时内部元素呈现透视深度，增强交互体验与视觉冲击力。
- 🚫 **CSS 限制**：使用`overflow: clip`或`hidden`会强制元素扁平化，导致 3D 效果消失，这是 CSS 规范中“分组属性”与`transform-style: preserve-3d`的冲突。
- 🎭 **模拟方案**：通过`scale()`和`translate()`模拟透视效果，但在大幅旋转时会出现失真，无法完全替代真实 3D。
- 💡 **突破性解决方案**：利用`perspective-origin`动态调整透视原点，配合数学计算校正旋转导致的变形，实现在扁平化容器中投影出 3D 场景的错觉。
- 🛠️ **实现步骤**：结合 HTML 结构、JavaScript 鼠标追踪、CSS 变量与变换，动态计算`perspective`和`perspective-origin`，使内部图层在 Z 轴分层并保持裁剪。
- 🌟 **扩展应用**：可添加阴影、透明度增强深度感，支持卡片翻转显示背面内容，内部图层动画以及创建全 3D 物体旋转效果。
- 🧠 **核心启示**：打破对 CSS 属性的固有偏见，通过创新思维与协作，能够解决看似无法实现的技术难题。

---

### [强制色彩模式 | 动手创造](https://gomakethings.com/forced-colors-mode/)

**原文标题**: [Forced Colors Mode | Go Make Things](https://gomakethings.com/forced-colors-mode/)

强制颜色模式是一种无障碍功能，可将网站颜色替换为用户自定义的简化调色板，并简化界面外观。本文探讨了其影响及适配方法。

- 🖥️ **强制颜色模式的作用**：替换网站背景、边框等颜色为高对比度调色板，提升视觉障碍用户的访问体验  
- 🚨 **常见设计问题**：该模式会移除背景色，导致选项卡、单选按钮等组件的状态无法辨识  
- 🪟 **平台支持现状**：目前主要支持 Windows 系统，可通过浏览器开发者工具模拟测试  
- 🛠️ **CSS 适配方案**：使用`@media (forced-colors: active)`媒体查询，通过加粗边框或`CanvasText`颜色值保持元素可见性  
- 🎯 **设计核心原则**：在强制颜色模式下应以功能清晰为首要目标，允许用户覆盖设计偏好  
- 🔧 **实际应用示例**：为对话框添加粗边框、使用`CanvasText`背景色保持开关组件辨识度

---

### [如何快速加载 CSS - 网页性能日历](https://calendar.perfplanet.com/2025/how-to-load-css-fast/)

**原文标题**: [  How to load CSS (fast) - Web Performance Calendar](https://calendar.perfplanet.com/2025/how-to-load-css-fast/)

本文介绍了如何利用压缩字典技术优化 CSS 加载速度，通过创建共享字典减少重复传输，实现首次加载快速、后续导航接近零带宽消耗的效果，并在不支持该技术的浏览器中优雅降级为关键 CSS 方案。

- 🚀 压缩字典技术为 CSS 加载提供了第三种优化方案，避免传统关键 CSS 与全量 CSS 之间的取舍问题
- 📚 通过创建全站共享的 CSS 字典文件，后续页面只需传输差异部分，大幅减少带宽消耗
- ⚡ 首次加载仅需关键 CSS，空闲时加载字典差异，后续导航 CSS 加载接近零成本
- 🔄 支持内容更新场景，新旧版本间仅需传输代码变更部分
- 🛠️ 需要服务器端逻辑处理不同变体，并考虑 CDN 缓存策略
- 🌐 目前 Chromium 浏览器已支持，Firefox 正在开发中，不支持时可降级为关键 CSS 方案
- 📊 对于多页面类型站点，需要静态生成 N 个关键 CSS 文件及其与全量字典的差异变体

---

### [宣布适用于 VS Code 的 JavaScript/TypeScript 现代化工具 - Microsoft 开发者平台](https://developer.microsoft.com/blog/jsts-modernizer-preview)

**原文标题**: [Announcing the JavaScript/TypeScript Modernizer for VS Code - Microsoft for Developers](https://developer.microsoft.com/blog/jsts-modernizer-preview)

微软发布了 Visual Studio Code 的 JavaScript/TypeScript Modernizer 工具，这是一个由 GitHub Copilot 驱动的 AI 辅助工具，旨在帮助开发者自动化升级 npm 包和更新代码以适应新版本，从而简化项目现代化过程。

- 🚀 **工具介绍**：VS Code 新推出的 AI 辅助工具，利用 GitHub Copilot 自动升级 JS/TS 项目的 npm 包并协助代码适配。
- 🔧 **核心功能**：分析项目依赖，制定升级计划，自动更新 package.json 并应用必要的代码变更以处理破坏性更改。
- 📦 **安装要求**：需预先安装 Node.js/npm、在 VS Code 中启用 GitHub Copilot，并安装 GitHub Copilot App Modernization 预览版扩展。
- ⚙️ **启用步骤**：在 VS Code 设置中添加实验性标志`"appmod.experimental.task.typescript.upgrade": true`并重启编辑器。
- 🛠️ **使用流程**：在 Copilot App Modernization 面板中点击“Upgrade npm Packages”，随后通过聊天界面跟随 AI 指导完成升级。
- ⚠️ **注意事项**：目前仅支持单项目升级（不适用于多项目工作区），且功能仍处于预览阶段，可能存在稳定性问题。
- 📝 **反馈与调试**：遇到问题时可通过检查 MCP 服务器日志、PROGRESS.md 文件或本地日志目录来诊断，并向微软团队反馈以改进工具。

---

### [马克西姆·欧齐埃](https://xem.github.io/articles/2D-physics.html)

**原文标题**: [Maxime Euzière](https://xem.github.io/articles/2D-physics.html)

作者基于对 JS 物理引擎的长期探索，在 2025 年 11-12 月期间，通过跟随一个 YouTube 教程系列，逐步构建并优化了一个功能完整的 2D 物理引擎。该引擎支持圆形和矩形物体的碰撞检测与响应、刚体动力学、多种关节（如弹簧关节、固定关节、铰链关节）以及稳定的堆叠效果，最终代码经过极致压缩，大小约 1.4kb（gzip 压缩）。

- 🎯 **探索历程**：作者自 2019 年起研究 2D 物理，曾创建 Mini2DPhysics 等作品，但苦于缺乏高级物理（如关节、弹簧）的详细资料，直到 2025 年发现一个完整的 JS 2D 物理教程系列，并以此为基础开发了自己的引擎。
- 🛠️ **引擎构建**：从零开始实现，包括画布设置、主循环、向量运算、形状定义、碰撞检测（圆 - 圆、圆 - 矩形、矩形 - 矩形）、刚体属性、积分方法、碰撞响应（线性与旋转冲量）、摩擦力、锚点和多种关节（力关节、弹簧关节、反向力关节、固定关节、铰链关节）。
- 🐛 **问题与优化**：初期版本存在堆叠不稳定、关节松动等问题，通过引入多接触点检测、暖启动（warm starting）、Baumgarte 校正等技术，并参考其他引擎（如 Box2D-lite 的 JS 移植），显著提升了稳定性。
- ⚡ **代码压缩**：经过多轮简化与混淆，将代码从初始的 12kb+ 压缩至约 1.4kb（gzip），同时保持了引擎的核心功能，包括稳定的物理模拟和关节支持。
- 🎮 **演示与发布**：提供了多个交互式演示，展示引擎在复杂场景（如堆叠、多关节组合）中的表现，并于 2025 年 12 月发布了 1.0 版本，后续还尝试添加自推进功能。
- 📚 **学习资源**：作者详细记录了开发过程，参考了教程、书籍、论坛帖子和现有引擎代码，特别感谢一位日本开发者的 Box2D-lite 改进版，为解决堆叠稳定性提供了关键思路。

---

### [我们如何保护新闻编辑室免受 npm 供应链攻击 | pnpm](https://pnpm.io/blog/2025/12/05/newsroom-npm-supply-chain-security)

**原文标题**: [How We're Protecting Our Newsroom from npm Supply Chain Attacks | pnpm](https://pnpm.io/blog/2025/12/05/newsroom-npm-supply-chain-security)

《西雅图时报》通过采用 pnpm 的三层客户端安全控制来防御 npm 供应链攻击，包括默认阻止生命周期脚本、设置发布冷却期和信任策略，构建了深度防御体系，确保在必要时可做例外处理的同时，多层防护依然有效。

- 🛡️ **采用 pnpm 的客户端安全控制**：作为 npm 的补充，pnpm 通过阻止恶意生命周期脚本执行、设置发布冷却期和检测信任降级，构建了深度防御体系，防止在安装时运行恶意代码。
- ⚙️ **三层控制机制**：包括严格的生命周期脚本管理（默认阻止并可选严格模式）、发布冷却期（延迟安装新包以留出检测时间）和信任策略（阻止认证强度降低的版本安装），各层均支持例外处理。
- 🔄 **深度防御实践**：通过分层防护，即使因紧急补丁等例外情况绕过某一控制，其他层仍能提供保护，例如在 React 关键漏洞修补时，冷却期可豁免，但脚本管理和信任策略依然有效。
- 🧪 **试点经验总结**：在单个后端服务中实施仅需数小时，成功识别并阻止了非必要的生命周期脚本；控制措施虽引入摩擦，但强制团队审慎决策，适合中型团队且具有实际可操作性。
- 📝 **实施建议**：建议从单一项目开始试点，预设例外情况并严格记录，启用严格模式确保立即失败而非警告，同时信任分层防护的互补性，以平衡安全与灵活性。

---

### [React 中 useEffectEvent 的注意事项](https://slicker.me/react/useEffectEvent.html)

**原文标题**: [Do's and Don'ts of useEffectEvent in React](https://slicker.me/react/useEffectEvent.html)

useEffectEvent 是 React 的一个 Hook，用于从 Effect 中提取非响应式逻辑，允许在 Effect 内部读取最新的 props 或 state 值，而不会因这些值的变化导致 Effect 重新执行。

- 🎯 **解决核心问题**：在 Effect 中读取最新值（如主题、用户偏好）而无需将其加入依赖项，避免不必要的重新运行。
- 🔄 **稳定函数引用**：创建一个始终读取最新值但不会触发 Effect 重新执行的函数。
- ✅ **正确使用场景**：在 Effect 内部直接调用、用于读取最新 props/state、结合清理逻辑、处理日志或分析事件。
- ❌ **避免使用情况**：在常规事件处理器、渲染过程中、异步调用或延迟后调用，或将其作为 prop 传递给组件。
- 📊 **常见应用**：日志记录与分析、携带最新状态的回调、基于最新值的防抖操作。
- ⚠️ **最佳实践**：仅在确实需要读取非响应式值时使用，保持函数目的单一，等待稳定版再用于生产。

---

### [编程文摘：电子邮件通讯](https://programmingdigest.net/?utm_source=web-archive&utm_campaign=react)

**原文标题**: [Programming Digest: Email Newsletter](https://programmingdigest.net/?utm_source=web-archive&utm_campaign=react)

《编程文摘》是一份面向软件工程师的每周精选简报，提供高质量内容以节省读者时间并促进持续学习。

- 📬 超过 23,595 名软件工程师订阅的每周电子邮件简报
- 🎯 每期精选附带简短摘要的优质技术文章
- ⏱️ 帮助工程师高效获取有价值内容，节省信息筛选时间
- 🌱 每周持续学习新知识，涵盖 API 设计等前沿话题
- 🌍 读者遍布全球科技公司，获得“每期都有收获”的好评
- 📚 由 Bonobo Press 自 2013 年持续运营至今

---

### [科技领导力：电子邮件通讯](https://leadershipintech.com/?utm_source=web-archive&utm_campaign=react)

**原文标题**: [Leadership in Tech: Email Newsletter](https://leadershipintech.com/?utm_source=web-archive&utm_campaign=react)

这是一份为技术领导者精心打造的每周通讯，旨在通过精选文章帮助他们提升领导力。

- 📬 超过 27,923 名工程领导者订阅，每周一封邮件
- 📄 提供附有简短摘要的精选文章
- ⏱️ 节省寻找有价值内容的时间
- 🧠 每周都能学到新知识
- ❤️ 读者好评：内容精准，尤其擅长汇编软件领域的领导力建设、架构讨论和沟通技巧等文章
- 🌍 受到众多科技公司领导者的阅读

---

### [C#文摘：电子邮件通讯](https://csharpdigest.net/?utm_source=web-archive&utm_campaign=react)

**原文标题**: [C# Digest: Email Newsletter](https://csharpdigest.net/?utm_source=web-archive&utm_campaign=react)

《C# Digest》是一份专为.NET 开发者精心策划的每周通讯，旨在通过精选文章和简短摘要，帮助开发者高效获取有价值的内容，每周学习新知识。

- 📧 超过19,470名C#工程师订阅这份每周电子邮件
- 📄 提供人工筛选的文章及简洁摘要，节省寻找优质内容的时间
- 🆕 每周持续学习，掌握.NET 开发新技能
- 💬 读者反馈积极，内容包括功能标志、LINQ、DiagnosticListener 等实用主题
- 🌍 受到全球.NET 工程师的阅读与认可

---

### [让开发者保持最新动态——Bonobo Press](https://bonobopress.com/)

**原文标题**: [Keeping developers up to date â Bonobo Press](https://bonobopress.com/)

Bonobo Press 是一家自 2013 年起为软件开发者、IT 专业人士和技术人员提供新闻资讯的出版商，通过每周精选的简洁通讯，覆盖超过 93,000 名读者，并为广告商提供针对技术决策者的精准推广渠道。

- 📰 自 2013 年起为超过 93,000 名软件开发者、IT 专业人士和技术人员提供最新资讯
- 📧 每周发布简洁、省时的精选通讯，受众包括开发者、工程经理和 CTO 等
- 🎯 为广告商提供精准触达技术决策者（如软件工程师、CTO）的推广渠道
- 📞 支持通过联系渠道进行咨询、建议或广告合作

---

### [往期通讯：第一页](https://reactdigest.net/newsletters)

**原文标题**: [Past Newsletters: Page 1](https://reactdigest.net/newsletters)

《React Digest》是一份专注于 React 生态的电子周刊，涵盖版本更新、性能优化、安全漏洞、新特性（如服务器组件）及开发实践等内容，旨在帮助开发者掌握最新动态与最佳实践。

- 🛡️ 探讨 React 与 Next.js 的关键安全漏洞及经验教训
- ⚡ 介绍 React 19.2 版本对 INP 指标的优化及性能提升策略
- ♿ 分享 React 中自动化无障碍测试的方法与工具
- 🧪 提供从 Enzyme 迁移至 React Testing Library 的实践指南
- 🔗 分析 URL 作为状态管理的优势及服务器组件的性能影响
- 🧠 深入解析 React 的渲染行为、状态管理与并发特性
- 🛠️ 涵盖 TanStack 生态工具（如 Router、DB）的使用与集成
- 📚 持续关注 React 服务器组件、序列化、缓存一致性等进阶主题

---

### [隐私](https://reactdigest.net/privacy)

**原文标题**: [Privacy](https://reactdigest.net/privacy)

React Digest 的隐私政策概述了其如何收集、使用和保护用户的个人信息，强调透明度、合法性和用户控制权，并遵守相关数据保护法规。

- 🔍 在收集个人信息前会明确说明用途，仅用于指定或兼容目的，且仅在必要时保留
- 📧 仅收集用户邮箱地址用于发送每周通讯，不会用于其他目的或垃圾邮件
- 🛡️ 采取合理安全措施保护个人信息，防止丢失、盗窃或未经授权的访问
- 📋 向用户公开个人信息管理政策，并允许用户查询或删除自身数据
- 👶 遵守 COPPA 法规，不故意收集或存储 13 岁以下儿童的信息
- 📬 用户可随时通过邮件联系查询、删除数据或取消订阅通讯

---

### [媒体资料包 – Bonobo Press](https://bonobopress.com/media-kit/)

**原文标题**: [Media Kit â Bonobo Press](https://bonobopress.com/media-kit/)

Bonobo Press 为技术专业人士提供高参与度的新闻简报广告服务，通过精准定位帮助广告商接触目标受众、提升参与度并实现转化。

- 📧 **使命与定位**：致力于让程序员和技术人员了解最新趋势、工具和技术，为软件开发者、工程经理、CTO 等提供精心策划的周报内容。
- 📊 **高参与度优势**：新闻简报的参与度是行业基准的两倍以上，通过严格的列表清理实践，优先考虑活跃读者而非列表规模。
- 👔 **领导力技术简报**：面向工程经理、技术领导、CTO 等决策者，订阅者 27,818 人，打开率 57.95%，点击率 11.38%，赞助费每期 2,235 美元，主要受众来自欧洲和美国。
- 💻 **编程摘要简报**：针对软件工程师和开发人员，订阅者 21,632 人，打开率 50.41%，点击率 14.83%，赞助费每期 985 美元，受众经验水平涵盖初级到管理层。
- 🔧 **C#摘要简报**：专注于 Windows 和.NET 开发者，订阅者 19,856 人，打开率 54.92%，点击率 21.63%，赞助费每期 1,220 美元，受众多就职于大型企业。
- ⚛️ **React 摘要简报**：服务于使用 React 的前端开发者，订阅者 23,831 人，打开率 54.06%，点击率 12.17%，赞助费每期 1,375 美元，提供次级广告位选项。
- 📝 **广告格式与流程**：广告为纯文本格式，包含链接、标题和描述；订购流程包括需求沟通、排期规划、发票支付、素材交付、广告上线和效果报告。
- 🤝 **合作伙伴与联系**：已与 Okta、GitLab、MongoDB 等多个知名品牌合作，提供定制化广告方案以提升潜在客户和转化率。

---

