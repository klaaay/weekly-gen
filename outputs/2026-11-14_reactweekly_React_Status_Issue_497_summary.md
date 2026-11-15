### [声明式拖拽](https://declarative-dragging.github.io/)

**原文标题**: [Declarative Dragging](https://declarative-dragging.github.io/)

本文介绍 UIST 2026 最佳论文“Declarative Dragging”（声明式拖拽）：它提出一种模型驱动的交互开发方法。开发者无需编写大量几何、反馈和动画代码，只需声明元素被拖动后应到达哪些未来应用状态；系统会推测式渲染这些状态，提取元素位置，并合成流畅、响应式的拖放交互。该方法通过 Dragology 库在 Web SVG 界面中实现，并展示了数学探索、编程环境等多种应用。

- 🏆 论文作者为 Joshua Horowitz、Andrew Blinn、Jeffrey Heer，获 UIST 2026 最佳论文奖。
- 🧩 传统定制拖拽需处理几何、反馈、动画等繁琐代码，导致许多教育者、游戏设计师、数学家和创意工具开发者望而却步。
- 🔄 声明式拖拽反转问题：不直接编程视觉行为，而是为每个可拖元素声明拖动应导向哪些未来状态。
- 🧠 D2 是模型驱动系统：引擎推测式渲染未来模型状态为视图树，提取被拖元素在各渲染中的位置，并据此合成拖放交互。
- 🧱 系统具备可组合性：简单拖拽行为可组合成复杂行为，修饰器可叠加悬浮、吸附、过渡等效果。
- 🛠️ Dragology 是面向 Web SVG 界面的实现库，提供代数、扭曲树、贝塞尔曲线、辫子、牌堆、人脸、三格骨牌、发芽树等演示。
- 🌱 项目源于 Andrew 2022 年的数学游戏原型和 2023 年白板草图，后经与 Josh 在 Seattle 的散步交流发展成库。
- 🔗 论文发表后已应用于并行表示界面（如排列实验室）和 Hazel 编程环境，使重构等操作更可触、可发现；Andrew 也重启数学游戏并适配手柄与 3D。

---

### [更新日志直播 | Sentry](https://sentry.io/resources/changelog-live/?utm_source=reactstatus&utm_medium=paid-community&utm_campaign=brand-fy27q4-changeloglive&utm_content=newsletter-primary-register)

**原文标题**: [Changelog Live | Sentry](https://sentry.io/resources/changelog-live/?utm_source=reactstatus&utm_medium=paid-community&utm_campaign=brand-fy27q4-changeloglive&utm_content=newsletter-primary-register)

Sentry 将举办 Changelog Live 直播活动，集中展示最新版本发布与可能错过的更新，帮助用户及其智能代理在一个场次中调试错误和性能问题；活动包含实时问答并会录制，同时推广其赞助的 Syntax 开发者播客。

- 📺 Sentry Changelog Live 将以直播形式展示最新发布内容，并补充一些容易错过的更新。
- 🛠️ 更快的调查体验包括：更丰富的错误上下文、更智能的问题分类、更强的搜索能力，以及可跨技术栈拉取数据的升级版 Seer Agent。
- 🤖 AI 工作流亮点包括：用 Seer 修复生产问题，以及追踪和调试你构建的智能代理。
- ⚙️ 活动还会快速介绍 SDK 更新、新集成和告警改进等底层能力。
- 🎙️ 直播将提供实时问答环节，并会录制存档；可提前预约席位。
- 🎧 Sentry 同时赞助了 Syntax 开发者播客，可在常用收听平台收听。

---

### [启动框架性能项目 | e18e](https://e18e.dev/blog/launching-the-framework-performance-project.html)

**原文标题**: [Launching the Framework Performance project | e18e](https://e18e.dev/blog/launching-the-framework-performance-project.html)

该项目于2026年11月10日发布 Framework Performance，旨在通过一套透明、可比较的基准测试，衡量各类元框架在开发期与运行期的真实性能，并帮助框架维护者发现瓶颈、持续改进。

- 🎯 **项目目标**：为框架维护者提供性能测量工具，同时为社区提供清晰透明的多维度基准数据。
- 🧩 **解决痛点**：现有基准各自为政、指标和侧重点不同，难以公平比较；单一数字也无法反映元框架的完整成本。
- 📦 **首版覆盖**：Nuxt、Next.js、TanStack Start (React)、Solid Start、Solid 2.0、Astro、SvelteKit、React Router 和 Pracht。
- ⏱️ **DevTime 基准**：衡量依赖数量、node_modules 大小、构建/安装时间、开发服务器启动、Core-JS polyfills、浏览器基线、最低 Node 版本等。
- 🚀 **RunTime 基准**：使用同一应用对比各框架，覆盖 Lighthouse 的 CSR/SSR 指标、首屏加载体积、SSR 吞吐量、负载测试及框架 Link 组件性能。
- 📊 **真实世界数据**：引入 HTTP Archive 的桌面端与移动端数据，并补充 TanStack 检测，避免仅依赖孤立基准。
- 🛠️ **已产生的影响**：Nuxt 内部链接渲染时间降低约 58%；Next.js 的 RSC payload 解析快约 75%；Solid 2.0 的 SSR 负载测试从 170 提升到 280 req/s；Vue Router 链接在服务端快 1.5–2.2 倍。
- 🔄 **持续跟踪**：项目会记录各元框架每个主要和次要版本的性能变化，展示长期进步而非单次排名。
- 🔮 **下一步**：继续新增基准和框架，欢迎社区反馈测试是否公平、是否缺少指标，并通过 issue 提出建议。
- 🙏 **致谢与支持**：感谢各框架团队、核心贡献者及 Depot 赞助；项目开源，可通过 Open Collective 赞助支持。

---

### [使用 `__vite-browser-external` 虚拟模块进行远程代码执行 · 安全公告 · vitejs/vite · GitHub](https://github.com/vitejs/vite/security/advisories/GHSA-p4f5-76q4-ffq7)

**原文标题**: [Remote code execution using `__vite-browser-external` virtual module · Advisory · vitejs/vite · GitHub](https://github.com/vitejs/vite/security/advisories/GHSA-p4f5-76q4-ffq7)

Vite 发布严重安全公告 GHSA-p4f5-76q4-ffq7：当 Vite 开发服务器被显式暴露到网络时，攻击者可通过特制 HTTP 请求利用 `__vite-browser-external` 等虚拟模块实现远程代码执行，并可能读取允许列表外的敏感文件。

- 🚨 **漏洞类型**：远程代码执行（RCE），严重等级为 Critical，CVSS v4 评分 9.1。
- 🎯 **受影响条件**：仅影响通过 `--host` 或 `server.host` 将 Vite 开发服务器显式暴露到网络的应用程序。
- 🧩 **根本原因**：`__vite-browser-external:<suffix>` 和 `__vite-optional-peer-dep:<suffix>` 虚拟模块未正确转义模块 ID，攻击者可注入任意代码。
- 🔓 **影响一**：被模块引用的文件可绕过 `server.fs` 检查，例如读取 `/path/to/some-secret-file.txt` 等敏感文件。
- ⚙️ **影响二**：Vite 使用 `eval` 提取 `new Worker` 和 `import.meta.glob` 中的值，攻击者可借此在服务器端执行注入代码。
- 🧪 **PoC 要点**：攻击者先确认 `/@fs/tmp/decoy-secret.txt` 被 403 阻止，再通过构造的 `__vite-browser-external` 模块 ID 将其引入模块图，最终成功读取文件内容。
- 📦 **受影响版本**：`vite` 的 `>=4.0.0,<=6.4.5`、`>=7.0.0,<=7.3.7`、`>=8.0.0,<=8.1.6`、`>=8.2.0,<=8.2.4`、`>=8.3.0,<=8.3.6`；`vite-plus <=1.5.0`。
- ✅ **修复版本**：`vite` 升级至 `6.4.6`、`7.3.8`、`8.1.7`、`8.2.5`、`8.3.7`；`vite-plus` 升级至 `1.5.1`。
- 🛠️ **修复说明**：Vite 8.3.7 和 8.2.5 依赖 Rolldown 1.2.17 的修复，Vite 8.1.7 依赖 Rolldown 1.1.7 的修复。
- 🧾 **其他信息**：弱点为 CWE-116（输出编码或转义不当），暂无已知 CVE；报告由 g2hsec、spansh、martinpriest、zooyeon 提交。

---

### [Storybook 11 测试版](https://storybook.js.org/blog/storybook-11-beta/)

**原文标题**: [Storybook 11 beta](https://storybook.js.org/blog/storybook-11-beta/)

Storybook 11 Beta 正式发布，核心方向是让设计系统更适合 AI 编码代理使用：通过官方 Skills、无头 CLI 和更快的上下文获取，让代理能基于团队现有组件、故事与测试自主构建、测试和提交 UI 供人工审查，同时包体积缩小 25%，上下文交付速度最高提升 10 倍。

- 🚀 **代理就绪的设计系统**：Storybook 11 Beta 面向 React、Vue、Angular、Web Components 和 Svelte，帮助代理避免重复组件、错误 API 和缺失状态。
- 🌟 **官方 Skills**：`ui-workflow` 引导代理使用现有组件构建 UI、编写 stories、测试并提交审查。
- 🔍 **组件文档查询**：`component-docs` 让代理以更省 token 的方式查找组件及其 API、元数据、文档和代码示例。
- ✅ **自动测试**：通过 `storybook tools test run` 运行基于 Vitest 的功能与可访问性测试，支持定位失败、修复并重跑。
- 👀 **浏览器审查**：`storybook tools review create` 按变更组件和受影响页面分组 stories，附变更摘要与关键状态，方便人工审查。
- 🧩 **Skills 获取方式**：升级或新建项目时自动安装，也可从 skills.sh、Claude Code 和 Codex 插件获取；MCP 仍受支持，但官方更推荐 Skills。
- 🛠️ **无头 CLI**：新增 `tools` 命令，提供快速无头 Storybook，支持 `docs list`、`docs show` 等，便于自定义 skills、工具和工作流。
- ⚡ **性能提升**：仅在需要浏览器时连接开发服务器；大型项目冷启动 docgen 结果交付约快 10 倍，TypeScript 7.1 稳定后预计再快 2 倍。
- 🧪 **类型安全 stories**：CSF 4 提供完全类型安全的现代 factories API，支持 addon 扩展类型系统；提供 codemod，CSF 3 仍受支持。
- ⚛️ **React 支持**：使用 `react-component-meta` 替代 `react-docgen` 和 `react-docgen-typescript`，元数据更准确、性能更好。
- 🟢 **Vue 支持**：升级到 `vue-component-meta`，并与维护者合作推进 Nuxt 的代理就绪支持。
- 🅰️ **Angular 支持**：新增 `@storybook/angular-vite`，与 Analog.js 和 Angular 核心团队合作，速度快、元数据质量高，Angular 21+ 可迁移。
- 🧱 **Web Components 支持**：基于自定义元素清单增强 slots、events、CSS variables 等 controls，并自动计算和更新 CEM。
- 🔥 **Svelte 支持**：Svelte 升级为核心框架，支持 Svelte 5 和 SvelteKit 3，Svelte CSF 不再需要 addon，docgen 性能显著提升。
- 🧭 **升级与试用**：可运行 `npx storybook@next upgrade` 升级现有项目，或 `npm create storybook@next` 新建项目；迁移指南列出所有破坏性变更。

---

### [<form> – React](https://react.dev/reference/react-dom/components/form#preserve-form-values-after-an-action)

**原文标题**: [<form> – React](https://react.dev/reference/react-dom/components/form#preserve-form-values-after-an-action)

该文档是 React 内置 `<form>` 组件的 API 参考，介绍其用于创建交互式表单控件的属性、提交处理方式、状态管理、错误处理及常见问题。核心是：React 19 起推荐使用 `action` 处理表单提交，并支持 Transition、Server Function、乐观更新和渐进增强。

- 📝 `<form>` 是浏览器内置组件，用于创建可提交信息的交互式控件。
- ⚙️ `action` 可传 URL 或函数：传 URL 时按标准 HTML 表单行为运行；传函数时由 React 处理提交。
- 🔁 当 `action` 为函数时，React 会在 Transition 中运行它，并向函数传入包含表单数据的 `FormData`。
- 📮 若 `action` 或 `formAction` 为函数，HTTP 方法固定为 `POST`，不受 `method` 属性影响。
- 🧹 函数型 `action` 成功后，React 会重置非受控字段；如需保留值，可用 `useState` + `defaultValue`。
- 🖱️ `onSubmit` 是传统事件处理方式，可调用 `e.preventDefault()` 阻止浏览器默认提交和刷新。
- ⏳ 使用 `useFormStatus` 可在子组件中读取表单提交的 `pending` 状态并显示加载中。
- ⚡ 使用 `useOptimistic` 可在服务器响应前乐观更新 UI，提升表单交互体验。
- 🧾 `action` 可运行带 `'use server'` 的 Server Function，支持 JavaScript 加载前或禁用时提交。
- 📦 向 Action 传递额外数据可用隐藏字段、`bind` 绑定参数，或在客户端组件函数中读取 props/state。
- 🛑 函数型 `action` 抛错时，可用 Error Boundary 捕获并展示回退 UI。
- 🧩 渐进增强场景可结合 `useActionState` 在 JavaScript 加载前显示错误或保留表单值。
- 🔀 多个提交按钮可通过 `formAction` 分别执行不同 Action，如“发布”和“保存草稿”。
- 🧯 表单字段提交后被清空通常是成功 Action 后的自动重置；可通过状态保存值、`defaultValue`、`requestFormReset` 或调整重置时机解决。

---

### [requestFormReset – React](https://react.dev/reference/react-dom/requestFormReset)

**原文标题**: [requestFormReset – React](https://react.dev/reference/react-dom/requestFormReset)

`requestFormReset` 是 React DOM 提供的 API，用于在当前 Action 或 Transition 完成后，请求重置由 React 管理的表单；它适合在自行实现表单提交逻辑时复用 React 的表单重置行为。

- 🧩 调用方式：`requestFormReset(form)`，其中 `form` 是 React 渲染的 HTML 表单元素。
- 🔁 主要用途：在 Action 或 Transition 结束后重置表单。
- 🛠️ 自定义提交场景：配合 `onSubmit` 和 `startTransition` 使用时，可手动触发 React 的表单重置行为。
- ⚠️ 参数限制：传入非表单元素或非 React 管理的表单会抛出错误。
- 🚫 返回值：该 API 不返回任何内容。
- ⏱️ 调用时机：应在 Action 或 Transition 内调用；若在外部调用，开发环境会警告并同步执行重置。
- 🧾 适用字段：主要请求重置非受控表单字段；受控字段应通过状态更新处理，例如在 `onReset` 中重置。
- ✅ 内置表单行为：使用 `<form action={...}>` 时 React 会自动重置非受控字段，无需手动调用 `requestFormReset`。

---

### [推出 UI SDK · UI SDK](https://ui-sdk.dev/docs/core/changelog/introducing-ui-sdk)

**原文标题**: [Introducing UI SDK · UI SDK](https://ui-sdk.dev/docs/core/changelog/introducing-ui-sdk)

UI SDK 是一个面向智能体、用于构建组件的 TypeScript UI 行为库，提供 50 多种可组合的交互行为与跨框架组件库，并支持智能体读取和操作界面。

- 🚀 2026年11月12日发布 UI SDK，定位为“为智能体而做”的 UI 行为库。
- 🧱 提供键盘导航、焦点、选择、弹窗、拖拽以及这些交互所需的 ARIA 属性等基础能力。
- 🧩 包含 50 多种行为，例如 `createRovingFocus`、`createTypeahead`、`createPopup`，可组合构建自定义组件。
- ⚛️ 使用 `@ui-sdk/core` 定义一次组件，再接入 React 等框架；智能体也可学习编写，用户可直接向智能体索取组件。
- 📚 基于相同行为提供跨框架组件库：50 多个现成组件，覆盖 React、Vue、Svelte、Solid 和 Web Components，样式由用户自带。
- 🤖 专为智能体构建与使用：`createAgent` 让智能体在权限范围内读取页面，并像人一样点击、输入和选择。
- 🌐 通过 WebMCP 的 `registerTools`，浏览器内置智能体也能读取组件并调用其动作。
- 🛠️ 可复制 setup prompt 让智能体自动配置 UI SDK；目前处于 beta，API 可能变化，可在 GitHub 反馈。
- 🙏 致谢 Radix、Base UI、React Aria、shadcn/ui、Nuxt UI、Geist 以及 WAI-ARIA Authoring Practices。

---

### [简介 · UI SDK](https://ui-sdk.dev/docs/core)

**原文标题**: [Introduction · UI SDK](https://ui-sdk.dev/docs/core)

@ui-sdk/core 是一个 TypeScript UI 行为库，提供键盘导航、焦点、选择、弹窗、拖放和 ARIA 等可复用行为层；开发者与智能体可将这些“积木”组合成 headless、可访问的自定义组件，并将行为与框架渲染分离。文中以图标选择器为例，说明如何组合弹窗、漫游焦点、空间方向移动、模糊搜索排序和屏幕阅读器播报来构建完整交互。

- 🧱 **核心定位**：@ui-sdk/core 提供构建组件库所需的行为层，而不是现成样式组件。
- ♿ **可访问性内置**：涵盖键盘、焦点、选择、弹窗、拖放及相应 ARIA 属性支持。
- 🧩 **组合式构建**：将多个行为组合起来，可创建产品所需的非标准组件。
- 🎯 **示例组件**：图标选择器由智能体组合 @ui-sdk/core 的行为构建，并非 @ui-sdk/react 现成组件。
- 🪟 **弹窗行为**：createPopup 与 popover preset 负责打开、聚焦搜索框、Esc/外部点击关闭及焦点返回。
- ⌨️ **单一 Tab 停靠点**：createRovingFocus 让 Tab 只进入网格一次，方向键在图标间移动。
- 🧭 **布局感知移动**：spatialMove 根据屏幕布局选择按键方向上最近的图标。
- 🔍 **模糊搜索排序**：fuzzyScore 对图标名称和关键词排名，支持如 “idea” 找到灯泡、“launch” 找到火箭。
- 📣 **屏幕阅读器播报**：announce 告知搜索匹配的图标数量。
- 🔌 **Primitive 整合**：统一定义状态、部件与行为，React、Vue、Svelte、Solid、Web Components 适配器负责渲染。
- 🎨 **无样式部件**：部件暴露属性和 CSS 变量，样式可完全自定义。
- 🧪 **测试支持**：测试工具可检查键盘行为、ARIA 关系和服务器渲染属性。
- 🚧 **Beta 状态**：UI SDK 仍处于 beta，部分 API 可能变化。
- 🚀 **入门路径**：从 Build a Component 开始，依次学习定义 Primitive、渲染、样式、组合行为和处理变更。

---

### [获取失败](https://blog.x.com/en/engineering/rebuilding-the-global-town-square-from-scratch)

**原文标题**: [Failed to retrieve](https://blog.x.com/en/engineering/rebuilding-the-global-town-square-from-scratch)

无法总结：获取内容失败，状态码 403。

---

### [六大 React 图表库与手写 SVG 对比：我的发现 - DEV Community](https://dev.to/gusevp/six-react-chart-libraries-against-hand-written-svg-what-i-found-46ib)

**原文标题**: [Six React chart libraries against hand-written SVG: what I found - DEV Community](https://dev.to/gusevp/six-react-chart-libraries-against-hand-written-svg-what-i-found-46ib)

作者用同一规范、同一合成数据并关闭动画，在无头 Chromium 中对比 nivo、Recharts、ECharts、visx、TanStack Charts、Chart.js 与手写 React+SVG 构建生存曲线和散点图的挂载性能、交互、包体积与代码量。结论是：常规尺寸下差距小于一帧，难以排名；10,000 点散点才拉开差距，手写 SVG、visx、TanStack 更优，nivo 的 SVG 散点和 Recharts 明显偏慢；TanStack 代码最少但较年轻，visx/手写 SVG 更可控且体积小。

- 🧪 测试覆盖两张图：生存曲线（阶梯线、置信带、删失刻度、提示框）与散点图（点大小/颜色、最近点提示）；七种实现均按同一规格、同一数据、关闭动画。
- ⏱️ 计时从图表挂载开始，到图表报告完成后两个 `requestAnimationFrame` 停止；SVG 以 React commit 为完成，Canvas 以库的 `finished`/`afterRender` 为完成，再统一等待两帧。
- 📊 常规尺寸下没有明显赢家：原生速度下生存曲线约 19–29 ms、散点约 22–37 ms，均在 1 帧内；4× CPU 降速下手写 SVG、visx、TanStack 基本同一组。
- 🚀 10,000 点散点差距明显：手写 SVG 24 ms、visx 33 ms、TanStack 53 ms、Chart.js/ECharts 80–86 ms、Recharts 310 ms、nivo SVG 3.2 s；Canvas 实现并未因 Canvas 而胜出。
- 🖱️ Hover 大多数场景为 1 帧；10,000 点散点上 Recharts 最长帧 133 ms，Chart.js/visx 50 ms，手写 SVG/TanStack 33 ms，nivo/ECharts 保持 1 帧（nivo 用预计算 Voronoi 做命中测试）。
- 📦 包体积（gzip）从低到高约为：无库 2.2 KB、visx 25 KB、Chart.js 55.6 KB、TanStack 56.8 KB、nivo 103.1 KB、Recharts 106.2 KB、ECharts 164.2 KB；代码 token 最少的是 TanStack（720），visx 为 1,683，手写方案为 3,134（后者含共享轴代码，偏高）。
- 🧩 各库使用体验：nivo 需自定义图层且默认 `nice` 会拉伸 x 轴；Recharts 需重塑数据、逐元素关动画且每散点渲染 3 个 DOM 节点；ECharts 顶层选项拼写错误可绕过类型检查；visx 需自己组合与命中测试；TanStack 用 mark grammar，多数需求是现成 mark；Chart.js 原生能力强但命名和交互模式需注意。
- ✅ 作者建议：想少写代码可先试 TanStack，但需考虑其年轻风险；想控制力强、包小可选 visx 或手写 SVG；不要用 nivo SVG 渲染大散点；用 Recharts 前重点检查生存提示框的数据重塑与压力场景性能。
- ⚠️ 局限：单机、单浏览器引擎、无头且机器繁忙，库运行顺序固定；只测两类图；代码 token 依赖具体规格与写法；Hover 是脚本化扫描，不等于真实输入延迟。

---

### [Remix v3：快速页面，精简生态](https://marmelab.com/blog/2026/11/12/remix-v3-fast-pages-thin-ecosystem.html)

**原文标题**: [Remix v3: Fast Pages, Thin Ecosystem](https://marmelab.com/blog/2026/11/12/remix-v3-fast-pages-thin-ecosystem.html)

本文通过同一套高端房产演示项目 Keyhaven，对比 Remix v3 与 TanStack Start 在开发体验、组件模型、表单、测试和性能上的差异，并评估 Claude Code 对 Remix v3 的辅助开发效果。

- 🏠 两个应用共享 `domain` 包中的 Zod 模型、校验与 Supabase 数据访问，后端使用 Supabase/Postgres RLS 作为信任边界。
- ⚙️ Remix v3 不再依赖 React，以单一 `remix` 包发布，内置 router、组件模型、资源服务器和测试运行器；开发中使用 Claude Code、Context7、Ponytail、框架 skill 与规则/agent 团队。
- 🧵 Remix v3 没有 Vite 和插件系统，Tailwind 需并行运行 CLI 并手动接入资源服务器；工具多时可用 Turborepo 等任务运行器编排。
- 🏝️ 组件默认只在服务端渲染且不下发 JavaScript；用 `clientEntry` 标记 islands，浏览器通过 `run()` 加载并 hydrate，props 必须可序列化。
- 🔒 资源服务器只提供 `public/` 和白名单包/文件；islands 不共享组件树，收藏等状态需通过外部 store 同步。
- 🔁 Remix 组件由 setup 函数和 render 函数组成，状态在闭包中，只有调用 `handle.update()` 才重渲染；忘记调用会静默导致 UI 陈旧。
- 🧠 Claude Code 未漏掉 `handle.update()`，但倾向避免客户端状态，甚至牺牲滑动等功能；评审发现后换回 island 轮播。
- 📝 表单方面，Remix 使用原生 HTML 与服务端校验，无 JavaScript，但每个错误一次往返；TanStack Form 提供客户端即时反馈，代价是表单库、mutation 和 server function。
- 🔄 共享 Zod schema 时，Remix 需用 `Object.fromEntries(FormData)` 再校验；若 schema 只服务 Remix，建议用 `f.object()` 直接校验 FormData。
- 🧪 测试方面，Remix 使用 CSS 选择器 `$`/`$$` 与 `act`，需单独 runner 且浏览器测试从仓库根运行；Vitest 浏览器模式按角色查询更易读，但 CommonJS 不兼容。
- ⚡ 性能上首屏相近；Remix 的 LCP 快约 0.26–0.28 秒，TBT 接近 0，传输 132KB 且只 hydrate islands；TanStack Start 传输 490KB，TBT 约 44–60ms。
- 📉 默认模拟节流曾显示 2.5× 差距，但 DevTools 真实节流下消失，建议用真实节流测量。
- 🧩 结论：Agentic 开发开箱可用，但 Remix v3 生态与工具集成较弱，缺少 Vite 插件、Vitest 集成和 shadcn/ui 等价物；性能不是选型关键；Marmelab 多数项目仍推荐 TanStack Start，Remix v3 适合小型、独立、依赖少的项目。

---

### [五名Web开发者如何使用Expo构建iOS键盘扩展](https://expo.dev/blog/supernova-ios-keyboard-extension-expo)

**原文标题**: [How five web developers built an iOS keyboard extension with Expo](https://expo.dev/blog/supernova-ios-keyboard-extension-expo)

未提供可摘要的正文内容，暂无法生成文章摘要。

- 📄 当前输入中缺少需要总结的文章文本。
- ✍️ 请补充或粘贴文章内容，我将按“概述 + 表情符号要点”的格式用中文总结。
- 🔍 收到内容后，我会提炼关键信息并生成简洁、有效的要点列表。

---

### [Text.js | 控制台框架](https://textjs.org/)

**原文标题**: [Text.js | The Console Framework](https://textjs.org/)

概述：Text.js 是一个让全栈 React 应用直接渲染在浏览器 `console.log`/DevTools 控制台中的框架，结合 React 19、App Router、控制台 UI 组件、Turbolog 增量渲染，以及服务端、终端和 Agent 运行能力。

- 🚀 使用 `bunx create-text-app` 快速创建项目，应用可直接在控制台中运行并交互。
- ⚛️ 支持 React 19 并发渲染、Suspense 和错误边界；App Router 中文件夹即路由，支持前进/后退与深链。
- 🧩 提供响应式网格和丰富组件：布局、列表/表格/树、Markdown/代码/差异、图表、表单控件、键盘映射与命令面板。
- ⌨️ 键盘、粘贴和 IME 输入通过隐藏的 `<textarea>` 传入应用。
- 🖥️ Turbolog 渲染流程：自定义 reconciler → Yoga 布局 → CellBuffer 绘制 → 行哈希脏检查 → RLE 编码 → `%c` spans → `console.log` 输出。
- 📉 只有帧发生变化时才输出，未变化帧为 0 次调用；帧间隔至少 66ms，并采用追加方式减少清屏造成的空白闪烁。
- ⚡ 性能基准：100×32 仪表盘平均 1000 帧下，完整重绘 0.163ms，单行编辑 0.011ms；3200 个单元格可编码为 149 个 `%c` spans。
- 🌐 服务端渲染：设置 `runtime = "server"` 可在服务端渲染路由和异步组件，浏览器仅加载 21kB gzip 帧播放器并通过 SSE 接收行增量。
- 📦 支持 Partial Prerendering、中间件、缓存与 stale-while-revalidate，以及 static、bun、vercel、cloudflare 部署适配器。
- 💻 同一 App Router 应用可通过 `text run` 在终端以 truecolor ANSI 运行，并在进程内执行路由处理器。
- 🤖 `text mcp` 让编码 Agent 通过 MCP 导航路由、按键并读取纯文本帧；OpenCode Lite 可在 DevTools 中运行。
- 🛠️ 工具链包括 DevTools 扩展（组件树、帧检查器、逐帧时间线）、VS Code 预览/脚手架、ESLint 插件、测试工具和 `TX` 错误码。
- 🔍 额外能力包括 `window.text` 控制台 REPL、完整 Unicode 双向文本算法支持，以及 FIGlet 字体解析。
- 🎓 提供 10 章、约 65 分钟的免费课程，覆盖入门、布局、样式、输入、路由、数据、测试、终端与部署。

---

### [A preview of Exact Â· Wholly Unreasonable](https://ccheever.expo.app/)

**原文标题**: [A preview of Exact Â· Wholly Unreasonable](https://ccheever.expo.app/)

Exact 是 Charlie Cheever 正在开发的一个用 Rust 编写的 Agent Native 应用框架预览版，目标是兼顾极高性能、原生体验和 AI Agent 友好的开发方式。它引入专为 Agent 设计的 Contract 语言，并支持 Web、iOS、macOS、Android、Windows、Linux 等平台，目前处于 pre-alpha 阶段，采用 MIT 许可证。

- 🚀 **Exact 定位**：用 Rust 编写的新型 Agent Native 应用框架，强调极快性能、无妥协地构建理想体验，并让 Agent 更容易开发、调试和迭代。
- ⚡ **Web 性能突出**：在 Pokédex 基准中与 Astro 接近，明显领先 Next.js 和 SvelteKit；兼具静态站点速度与 React 式动态能力。
- 🧠 **Contract 语言**：外观类似 Python，缩进有意义、显式强类型；同时描述 UI、状态和数据流，替代 React、Redux、Zustand、TanStack Query 等组合。
- 🔒 **可分析、少踩坑**：Contract 是受限语言，可被完整分析；不支持递归循环、useEffect 或任意 TypeScript/JavaScript，减少性能问题和分析困难。
- 🛠️ **面向 Agent 的编译器反馈**：编译器通过针对性错误信息按需教会 Agent 语法和规则，避免一次性塞满上下文窗口。
- 🕹️ **Agent 原生调试能力**：Agent 可控制时钟、截图录像、检查 UI 树抽象状态和布局属性，减少等待动画和竞态问题。
- ⚡ **快速更新机制**：编译时掌握布局和数据关系，更新更精准；无虚拟 DOM、重渲染或单独 hydration，Contract 改动可毫秒级热更新并支持 OTA。
- 🦀 **Rust 与 TypeScript 可选**：深层逻辑可用 Rust 或 TS，也可混用；可做纯 Rust、不带 JS VM 的原生应用，也能用 TS 提升开发迭代效率。
- 🪝 **Access Hatches**：除常规原生逃生舱外，还能访问框架生成的每个原生节点，用 Swift、Kotlin 等精细控制细节，例如修复 Liquid Glass 示例中的动画裁剪问题。
- 📈 **原生性能强**：在富内容滚动测试中保持 120fps、零掉帧，优于 SwiftUI 的 30–50fps；启动时可由 Rust 直接绘制首帧，无需等待 JS。
- 🎨 **布局与图形**：使用基于 CSS 的 Taffy 在 Rust 中布局，作者体验接近 Web；内置 GPU 支持，可做丰富动画、着色器内实时 UI 和文字测量效果。
- 💻 **多平台与渲染器**：iOS/macOS/Web 优先使用平台原生元素；Android/Windows/Linux 更多由 Exact 自绘，使用 Ink 渲染器；还支持桌面应用、游戏引擎和 TUI。
- 🧪 **可用性与生态**：iOS 最成熟，Web 和 macOS 较好，Android/Windows/Linux 可用但较不成熟；提供 GitHub 仓库和模板应用，Expo 继续支持 React Native 并与 Exact 云服务协同。
- 📬 **反馈方式**：鼓励报告问题、请求功能和提交反馈；最有帮助的是让 Agent 将使用 Exact 的详细体验日志提交到反馈端点。

---

### [Andrew Clark on X: "Looks very good and is eerily (or perhaps not) similar to what I think React 20 is shaping up to be. @RyanCarniato's ReactiveScript seems to be converging on something similar, too. https://t.co/Dge0pGD5N0" / X](https://x.com/acdlite/status/2119784287436415149)

**原文标题**: [Andrew Clark on X: "Looks very good and is eerily (or perhaps not) similar to what I think React 20 is shaping up to be. @RyanCarniato's ReactiveScript seems to be converging on something similar, too. https://t.co/Dge0pGD5N0" / X](https://x.com/acdlite/status/2119784287436415149)

Charlie Cheever 预览了新项目 Exact——一个用 Rust 编写的 Agent Native 应用框架，强调极快性能与不妥协的定制体验；Andrew Clark 认为它看起来很好，且与他设想的 React 20 方向惊人相似，并指出 Ryan Carniato 的 ReactiveScript 也在朝类似方向收敛。

- 🧩 Charlie Cheever 正在开发并预览新框架 **Exact**
- ⚡ Exact 使用 **Rust** 编写，主打极快性能
- 🎯 目标是让开发者构建理想体验时“无需妥协”
- 🤖 它被定位为 **Agent Native** 应用框架
- 👀 Andrew Clark 评价其“看起来非常好”
- 🔮 他认为 Exact 与自己所设想的 **React 20** 方向惊人相似
- 🔁 他还提到 Ryan Carniato 的 **ReactiveScript** 似乎也在趋同于类似方案

---

### [发布 v8.0.0-react-shepherd · shipshapecode/shepherd · GitHub](https://github.com/shipshapecode/shepherd/releases/tag/v8.0.0-react-shepherd)

**原文标题**: [Release v8.0.0-react-shepherd · shipshapecode/shepherd · GitHub](https://github.com/shipshapecode/shepherd/releases/tag/v8.0.0-react-shepherd)

本次发布于 2026-11-11 推出 `react-shepherd 8.0.0` 与 `shepherd.js 16.0.0` 两个 major 版本，核心变化包括移除全部依赖、启用自研定位引擎、构建工具迁移至 tsdown，并修复多项交互与 tour 生命周期问题；同时更新了官网、文档与测试基础设施。

- 💥 `react-shepherd` 与 `shepherd.js` 均发布 major 版本，包含破坏性变更。
- 📦 两个包移除全部依赖，改用自研定位引擎，体积缩小约 37%，并新增面向 agent 的文档。
- 🛠️ `react-shepherd` 改用 tsdown 构建，测试中也移除了 Floating UI。
- 🐛 修复 pinch-zoom 遮罩覆盖、步骤内触控滚动及不可见对话框焦点问题。
- 🧭 修复 `beforeShowPromise`、`start`、`confirmCancel` 相关的 tour 生命周期竞态。
- 🪟 修复 modal 场景下的 iframe 偏移、`overflow: hidden` 裁剪判断及根元素裁剪高亮问题。
- 📱 修复移动端 tooltip 重新定位时输入框失焦问题。
- 🧪 内部更新包括 cypress-plugin-tab 2.0.0、依赖升级与审计问题修复。
- 🌐 官网新增 about/contact/privacy 页面、agent 友好的 404 与 `llms.txt`，升级 Astro v7，并完善 canonical、Open Graph、JSON-LD 及 markdown 协商服务。

---

### [React 用法 | 文档](https://docs.shepherdjs.dev/recipes/react/)

**原文标题**: [React Usage | Documentation](https://docs.shepherdjs.dev/recipes/react/)

Shepherd 提供了 React 包，主要用于封装默认的 Shepherd 类，并增加在 React 应用中初始化导览的语法糖；它通过暴露 Tour 对象和方法支持动态交互，同时官方更倾向于提供示例而非强制单一实现模式。

- 🧩 React 包多年持续发布，核心仍是导出默认 Shepherd 类，并提供在 React 应用中配置 Shepherd 的语法糖。
- 🧱 该封装在根 API 之上增加一层，提供有倾向性的模式，主要将 Tour 对象和方法暴露到 context，便于通过 props 实现动态交互。
- 🪝 自定义 Hook 模式：可创建 Hook 来初始化和共享 Tour 实例，并按需替换；示例中使用 useMemo 创建 Shepherd.Tour、调用 addSteps 添加步骤并返回实例。
- 🌐 Context/Provider 模式：使用 React.createContext 创建上下文，在 Provider 中传入 shepherdTourInstance，组件内通过 useContext 获取 tour 并调用 start 等方法。
- 💡 官方认为创建解决方案的方式不止一种，因此更倾向于提供若干示例，而不是规定唯一做法。

---

### [发布 10.0.0 · bvaughn/react-virtualized · GitHub](https://github.com/bvaughn/react-virtualized/releases/tag/10.0.0)

**原文标题**: [Release 10.0.0 · bvaughn/react-virtualized · GitHub](https://github.com/bvaughn/react-virtualized/releases/tag/10.0.0)

react-virtualized 10.0.0 是一次重大现代化升级：源码迁移至 TypeScript，所有组件重写为函数组件并采用 hooks，要求 React 18+，同时修复了 9.x 架构中的多项长期缺陷，并带来一系列破坏性 API 变更与完整迁移指南。

- 🚀 版本核心：10.0.0 完成现代化改造，全面使用 TypeScript、函数组件和 hooks，最低要求 React 18。
- 📦 导入方式：仅支持从包根导入，移除深层导入和 UMD 构建，未使用组件可被 tree-shaking。
- 📐 AutoSizer：从主包移除，改用 `react-virtualized-auto-sizer` 2.x，通过 `renderProp`/`ChildComponent` 使用，尺寸未测量时为 `undefined`。
- 🎯 滚动控制：移除受控滚动 props，改用 ref 命令式方法；`scrollToRow`、`scrollToPosition` 等改为对象参数，并新增 `initialScrollTop`/`initialScrollLeft` 支持初始位置与服务端渲染。
- 🔧 Ref 与类型：refs 暴露 `*ImperativeAPI` 命令式句柄，不再指向组件实例；移除 `propTypes` 和静态 `defaultProps`，新增完整的 TypeScript 类型导出。
- 🪟 窗口滚动：移除 `WindowScroller`，改用 `scrollElement="window"` 或可滚动元素；组件按完整高度渲染，并只渲染视口内行。
- 🔗 子组件驱动：`ScrollSync` 和 `ArrowKeyStepper` 改为通过 `registerChild` 驱动子组件，不再传递受控滚动 props。
- 🧱 组件调整：`Column` 子类改为包装组件；`CellMeasurer` 子元素必须可测量或使用 `registerChild`；`Collection` 已移除。
- ♿ List 语义：`List` 默认 `role="list"`，行默认 `role="listitem"`，不再默认设置 `aria-label` 和 `aria-readonly`。
- 🐛 关键修复：修复 React 19 下 `Table` 崩溃、`Masonry`/`MultiGrid`/`Grid` 多种边界问题、`InfiniteLoader` 从新加载行重算、`CellMeasurerCache` 增量更新性能等。
- 📚 其他变化：构建不再压缩，移除 `prop-types`、`@babel/runtime` 等依赖，新增文档站点与在线示例。

---

### [react-native-audio-api 1.0.0](https://swmansion.com/changelog/react-native-audio-api-1-0-0/)

**原文标题**: [react-native-audio-api 1.0.0](https://swmansion.com/changelog/react-native-audio-api-1-0-0/)

Audio API 1.0.0 是 react-native-audio-api 的首个稳定版本（2026年11月3日发布）。它大幅提升了与 Web Audio API 规范的兼容性，将可选功能（如 FFmpeg、Worklets）移出默认构建并独立成包，同时清理了在 0.x 阶段自然形成的 API。升级需修改代码，官方提供迁移指南，TypeScript 项目可先运行 tsc 排查大部分问题。本版还引入了 PannerNode/AudioListener 空间音频、重写的音频图、录音编码层以及大量性能优化与缺陷修复。

- 🎯 规范一致性：与 0.13.6 相比，Web Platform Tests 通过率从 1758/2503（70.2%）升至 2643/3109（85.0%），AudioBuffer、ChannelMergerNode、ChannelSplitterNode、GainNode、OscillatorNode、PeriodicWave 六接口全部通过
- 📦 破坏性变更之一：FFmpeg 默认关闭，本地文件/资源改用平台解码器；远程 URL 流、HLS、远程时长仍需 FFmpeg，构建选项迁至 package.json，Expo 的 disableFFmpeg 改为 enableFFmpeg
- 🧵 Worklets 独立为 react-native-audio-worklets 包，需 react-native-worklets ≥0.10.0 与新架构；WorkletAudioContext、频域模式、通道数回调
- 🔤 事件处理器改为规范小写命名（onEnded→onended、onPositionChanged→onpositionchanged），重新赋值会替换而非叠加；<Audio>、AudioRecorder、系统事件名称不变
- ⚙️ setAudioSessionOptions 更名 setSystemOptions，iOS 选项嵌套于 ios 键，新增 android 通信会话配置；recorder 直接连接音频图，pause/resume/disableFileOutput 返回 Promise 并与 start/stop 串行
- 🧭 空间音频：新增 PannerNode（等功率声像、距离模型、锥形增益）与 AudioListener；另增 ChannelMergerNode/ChannelSplitterNode
- 📊 新增 baseLatency、outputLatency；音频图重写为链路感知的拓扑排序与按上下文事件队列
- 🎙️ 录音编码层支持 Opus 与 ADTS AAC（崩溃后文件仍可用），Android 新增 androidInputPreset、setInputDevice（含蓝牙 SCO）、通信会话与输出配置
- 📱 Android 录音可脱离 UI 存活（androidFSStopWithTask: false）；MediaCodec 异步解码与裸 WAV 路径提速
- 🔊 播放与构建：支持 Swift Package Manager、<Audio> 缓冲状态 onWaiting/onPlaying、isLiveStream、可配置快进快退间隔、getSystemVolume()、React Native 0.88 支持
- ⚡ 性能：卷积器共享 4 个线程而非各自 4 个，音频线程不再等待；缓冲区跨渲染量子复用，每上下文的线程数从 7 降至 2；外部内存按缓冲区上报以避免 Hermes OOM；引擎懒初始化
- 🛠️ 主要修复：iOS 引擎/工作线程死锁、播放器 use-after-free、录音中断后无法恢复；Android 前台服务销毁时结束录音；exponentialRampToValueAtTime、ConvolverNode.buffer、AudioScheduledSourceNode 内存泄漏等
- 📚 文档：全双工语音 AI 助手指南与配套 Demo、版本化文档（latest/next 各含 WPT 报告）、C++ 引擎内部文档

---

### [Expo 模拟器：为智能体打造的模拟器](https://expo.dev/services/simulators?utm_campaign=agentic-development&utm_source=email&utm_medium=email&utm_term=Simulators&utm_content=React%20Status)

**原文标题**: [Expo Simulators: Simulators built for agents](https://expo.dev/services/simulators?utm_campaign=agentic-development&utm_source=email&utm_medium=email&utm_term=Simulators&utm_content=React%20Status)

Expo Simulators 是为 AI 编程代理打造的按需云端 iOS 模拟器与 Android 模拟器服务：代理可安装构建、操作应用、验证结果，并并行运行多个会话来闭环验证代码。

- ☁️ 按需启动安全云端 iOS 模拟器与 Android 模拟器，代理可安装构建、驱动应用并自行验证工作。
- 🤖 任何能运行 Shell 命令的编程代理都可使用，如 Claude Code、Codex、Cursor；建议安装 `eas-simulator` skill。
- 🚀 一条命令启动会话：`eas simulator --platform ios`，代理获得可驱动会话，用户可观看实时流。
- ✅ 面向代理生成代码提供“证据”：每次检查的截图、会话录像、构建链接，便于 PR 审查和点击实时构建。
- 🧪 默认支持并行测试，可同时覆盖 iPhone、Android 设备、折叠屏和平板，并按需扩展。
- 🔒 会话隔离运行，支持访问控制预览和会话级凭证；会话停止后模拟器与控制端点不可用。
- 🔁 典型场景包括 Agentic CI、灵感快速验证、Bug 复现与修复，以及自动提交带前后对比的 PR。
- 🧰 不要求应用必须用 Expo 构建，支持 React Native、Swift、Kotlin、Flutter、Unity 等框架。
- 🔗 可通过 EAS CLI 或 REST API 接入 GitHub Actions、Expo Workflows 等现有 CI。
- 🧪 可连接 Appium 测试套件，也可通过 agent-device 运行部分 Maestro YAML 流程。
- 📱 支持 iPhone/iPad 模拟器和 Android 模拟器，启动会话时选择设备；多会话共享账户并发额度。
- 👥 团队可通过浏览器查看共享的实时模拟器会话，也可在 PR 中添加入口启动新会话；默认需登录并有项目权限。
- 🖼️ 会话可记录并保存截图、录像和任务日志，代理或 CI 可把证据链接附到 PR。
- ♻️ Expo/React Native 应用可通过 fingerprinting 复用匹配的 native 构建并重打包最新 JavaScript，开发时也可用 Metro Fast Refresh，减少完整原生重建。

---

### [Trigger.dev | 面向持久 AI 智能体的开源平台](https://trigger.dev/?utm_source=fnf&utm_medium=newsletter&utm_campaign=october&utm_term=react-weekly&utm_content=homepage)

**原文标题**: [Trigger.dev | The open source platform for durable AI agents](https://trigger.dev/?utm_source=fnf&utm_medium=newsletter&utm_campaign=october&utm_term=react-weekly&utm_content=homepage)

Trigger.dev 是面向 TypeScript AI Agent 的开源平台，主打可持久运行、可重试、可观测、可弹性扩展的后台任务与工作流，帮助开发者将长耗时 AI 任务交给基础设施处理，并实时展示状态、流式输出到前端。

- 🆕 推出面向 AI Agent 的 Webhooks，可构建并部署持久化 AI Agent 与工作流。
- 🧠 使用 TypeScript 编写任务，支持长运行任务、重试、队列、AI 可观测性与弹性伸缩。
- 🔁 Agent 可承受刷新、重部署和崩溃，支持工具调用、人工审批（HITL）与流式响应，无需自建 API 路由。
- 🧩 覆盖 AI Agent、Webhook、媒体处理/生成、人在回路、流式输出、Python、营销、浏览器自动化、定时任务、并发、重试、语义搜索、邮件序列等场景。
- 🏗️ 支持多种 Agent 模式：自主 Agent、提示链、路由、并行化、编排器、评估-优化器。
- ⚙️ 无超时限制，按实际执行付费，无需管理服务器，并提供错误告警、高级筛选、批量操作与版本控制。
- 📡 Realtime 可展示任务状态与元数据，并将 LLM 或其他来源的流实时转发到前端。
- 🐍 运行时自由度高，可定制构建流程与容器镜像，支持 Python、Prisma、Puppeteer、esbuild、FFmpeg、apt-get 与自定义构建扩展。
- 🛡️ 默认可靠：支持任务重试、catchError、retry.onThrow、retry.fetch 和 trigger.config 配置重试策略。
- 👀 提供日志追踪、LLM 可观测性、标签、运行筛选、仪表盘、错误监控与实时告警。
- 🔓 Apache 2.0 开源，可自托管，GitHub 16.8k+ stars，Discord 5.1k+ 成员。
- 💬 Cal.com、Supabase、Magic Patterns、MagicSchool AI、Pallet、Comp AI、HeroUI、Midday 等团队用于数百万级工作流与 AI 任务。
- 💳 按使用量付费，支持自托管，并具备 SOC 2 Type II、HIPAA BAA、GDPR 合规能力。
- 📝 近期更新包括 GitHub Actions 可信发布、API Key 自定义权限与预设、工作负载身份 OIDC、Bun 运行时优化等。

---

### [Modern Web Guidance 1.0: The web platform expertise your coding agent is missing  |  Blog  |  Chrome for Developers](https://developer.chrome.com/blog/modern-web-guidance-v1)

**原文标题**: [Modern Web Guidance 1.0: The web platform expertise your coding agent is missing  |  Blog  |  Chrome for Developers](https://developer.chrome.com/blog/modern-web-guidance-v1)

现代 Web 指南（Modern Web Guidance）1.0 正式稳定发布，旨在为编码智能体注入经过专家审核的 Web 开发最佳实践、浏览器兼容性数据和现代化工作流，帮助开发者生成更快、更可访问、更安全的代码，并与 Chrome DevTools for agents 配合形成从编写到验证的完整智能体开发闭环。

- 🚀 1.0 稳定版发布：为编码智能体提供专家审核的 Web 平台知识、最佳实践和浏览器兼容性数据，覆盖现代 Web 开发核心场景。
- 🧭 新增现代化工作流：可扫描现有 HTML、CSS、JavaScript 和 package.json，帮助智能体发现并安全升级过时写法、冗余依赖和不再需要的 polyfill。
- 📚 扩展指南数据库：针对数百个已验证的 AI 知识缺口提供跨浏览器解决方案，并由内容领域技术负责人和无障碍专家深度审核。
- 📊 完整评估覆盖：所有指南均提供公开评估仪表盘，展示相比未使用 Modern Web Guidance 的智能体所获得的 measurable 改进。
- 🌐 跨浏览器协作：Firefox 和 Edge 加入 Chrome 共同支持项目，基于 Baseline 数据提升跨浏览器兼容性并推动现代 Web 平台能力普及。
- 🧩 弥补模型短板：重点强化可访问性、用户体验、性能和安全性方面的最佳实践，例如键盘焦点管理、减少动态效果支持、主线程任务调度、安全 HTML 清洗和通行密钥管理。
- ⚡ 推荐最佳 Web 特性：引导智能体优先使用原生 HTML/CSS 特性而非自定义 JavaScript，例如弹窗动画、滚动与滑动交互、页面过渡、自动填充和 WebAuthn/通行密钥。
- 🛠️ 与 Chrome DevTools for agents 配合：前者提供编写代码所需的前置专业知识，后者提供运行时可见性，用于验证、调试和优化性能、动画、内存等表现。
- 📈 实际成效显著：Pensionbazaar/Policybazaar 将新页面交付周期缩短 90% 以上、UI 缺陷减少 90% 以上；WeTV 自动诊断并解决 90% 的性能检查失败，调试时间减少 87%；note inc. 现代 Web 检查通过率从 61% 提升至 94%；MetaMask 用三行提示配置自动审查机器人，五周内审查约 480 个 PR 并推动修复 43 个问题。
- 💻 安装与更新便捷：在项目目录运行 `npx modern-web-guidance@latest install` 安装，或运行 `npx modern-web-guidance@latest update` 升级到 1.0；也可通过 Claude Code、Codex、Cursor、Copilot、WebStorm 等主流智能体插件市场安装。
- 🤝 社区与生态支持：项目由 Chrome 发起，汇聚浏览器合作伙伴、Web 标准与无障碍专家、开源贡献者共同维护，并提供贡献指南方便社区参与改进。

---

### [AI 在 Web 开发中常犯的 10 大错误 | 博客 | Chrome 开发者](https://developer.chrome.com/blog/top-10-things-ai-gets-wrong-in-web-dev)

**原文标题**: [Top 10 things AI gets wrong in web development  |  Blog  |  Chrome for Developers](https://developer.chrome.com/blog/top-10-things-ai-gets-wrong-in-web-dev)

Modern Web Guidance 已发布 1.0 稳定版，旨在将 Web 平台专业知识、最佳实践和浏览器兼容性数据直接嵌入 AI 编码代理。评估显示，未使用该指南的代理平均仅通过约 50% 的检查，而使用后约 90%，文章据此总结了 AI 在 Web 开发中最常出错的 10 个领域。

- 🚀 Modern Web Guidance 1.0 正式稳定发布，帮助使用 AI 编码代理的开发者更好地利用现代 Web 平台能力。
- 📊 评估方式是对比“安装指南”和“未安装指南”的代理输出；未引导代理平均通过约 50%，引导后约 90%。
- ♿ 可访问性焦点管理是最大缺口之一：常见问题包括未移动/恢复焦点、手写 tab 陷阱、未使用 `inert`、焦点轮廓对比度不足等。
- 🌀 减少动态效果支持常被忽略：平滑滚动、视图过渡、滚动驱动动画等场景容易缺少 `prefers-reduced-motion` 处理或处理不当。
- 📝 表单细节易错：包括 `:user-invalid`、`aria-invalid` 同步、持久格式提示、自动填充状态的非颜色提示等。
- 👆 触控手势应优先使用 CSS Scroll Snap、原生滚动 API 和滚动驱动动画，并兼顾 `overscroll-behavior` 与键盘可访问性。
- 🪟 对话框和弹层应更多使用 `<dialog>`、`popover`、`@starting-style`、`transition-behavior` 等原生能力，而非手写状态机、滚动锁和返回键监听。
- 🌓 深色模式需正确设置 `color-scheme`、使用 `light-dark()`、避免白屏闪烁，并同步系统偏好与多标签页状态。
- ⚡ 运行时性能方面，AI 常忽略 `scheduler.postTask()`、`scheduler.yield()`、`content-visibility`、`contain-intrinsic-size` 等主线程优化手段。
- 📐 布局偏移与闪烁常源于视频尺寸缺失、字体切换未用 `font-size-adjust`、静态 `vh` 单位、客户端实验隐藏方式不当等。
- 🔐 安全性方面，模型很少主动添加 CSP 或跨域隔离头；DOM XSS 防护中常手写不完整 sanitizer、滥用 Trusted Types 或未优先使用原生 `setHTML()`。
- 🔑 通行密钥实现常遗漏 WebAuthn 的 JSON 序列化、能力检测、`signalUnknownCredential()`、`AbortSignal` 和 `uiMode` 等关键 API。
- 🛠️ 可通过 `npx modern-web-guidance@latest install` 安装使用，也可在 GitHub 仓库反馈问题或贡献指南。

---

### [JavaScript 2026 现状](https://survey.devographics.com/en-US/survey/state-of-js/2026)

**原文标题**: [State of JavaScript 2026](https://survey.devographics.com/en-US/survey/state-of-js/2026)

当前提供的内容仅为“Loading...”，没有可供总结的文章正文或关键信息，因此无法提取实质要点。

- ⏳ 输入内容显示为“Loading...”，可能表示页面或文章尚未加载完成。
- 📄 未包含文章主题、核心观点、数据或结论。
- 🔁 请提供完整文章内容，以便生成准确的中文要点摘要。

---

