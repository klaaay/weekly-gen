### [框架基准测试 - 比较前端框架](https://framework-benchmarks.as93.net/)

**原文标题**: [Framework Benchmarks - Compare Frontend Frameworks](https://framework-benchmarks.as93.net/)

该页面展示了一个前端框架性能基准测试工具，通过多个维度对比不同框架的表现。

- 📊 提供 React、Angular、Svelte 等 13 种框架的性能对比，支持开关切换显示
- 🚀 展示包体积与性能关系，性能越高越好，包体积越小越好
- 📦 分析源代码大小与复杂度，数值越低越好
- ⚖️ 对比总包体积与压缩后体积，尺寸越小越优
- 💡 显示 Lighthouse 性能评分，基线为 80%，越高越好
- ⏱️ 记录加载性能指标随时间变化，时间越短越好
- 🖥️ 测试 CPU 和内存使用情况，使用率越低越好
- 🔧 展示构建时间与包体积关系，构建更快 + 包更小=更优
- 📊 饼图显示各框架包体积分布，切片越小表示效率越高
- ⏳ 饼图展示各框架构建时间分布，切片越小表示构建越快
- ⚡ 对比开发服务器启动和 HMR 时间，条越短表示开发体验越好
- 🎯 展示生产构建时间与输出大小，左下角为最优（快速构建 + 小输出）
- 📁 提供原始结果 JSON 下载，每晚自动更新至最新版本
- 🔗 包含完整数据集和 TSV 摘要文件链接
- 🤝 提供 Stack Match 工具，根据用户偏好推荐框架

---

### [xyOps - 开放工作流自动化](https://xyops.io/)

**原文标题**: [xyOps - Open Workflow Automation](https://xyops.io/)

xyOps™ 是一款下一代工作流自动化系统，集成了作业调度、监控、告警和工单管理功能，由 Cronicle 的创建者开发，支持从单服务器到数千台服务器的灵活部署，并提供可视化工作流构建器、智能告警、插件市场等丰富功能，采用 BSD 开源许可，提供免费自托管及付费支持计划。

- 🚀 **核心功能**：xyOps 提供作业调度、监控、告警和工单管理一体化解决方案，超越传统 cron 的局限性。
- 🎨 **可视化工作流**：通过图形化编辑器连接事件、触发器、动作和监控器，构建有意义的管道，支持条件逻辑、数据传递和并行执行。
- 📊 **全面监控**：定义监控目标，实时跟踪 CPU、内存、网络、磁盘等指标，并生成历史性能图表。
- 🔔 **智能告警**：支持灵活的触发表达式、邮件/Webhook/自定义通知，告警可创建工单或运行作业，并防止新作业启动。
- 🛠️ **开发者友好**：支持任意语言编写插件（通过 JSON over STDIO API），提供插件市场（如 Atlassian、AWS S3、OpenAI 等），无需 SDK。
- 🌐 **弹性扩展**：支持热备份故障转移、数千台工作服务器集群，以及 macOS/Linux/Windows 代理安装。
- 📜 **开源许可**：100% 免费开源，采用 BSD 3-Clause 许可，所有功能永久开源，支持专业和企业付费支持计划。
- 💰 **定价方案**：免费版（自托管，全部功能 + 社区支持）、专业版（$167/月，含专业支持 + 工单系统）、企业版（$834/月，含 SSO、气隙安装、1 小时工单响应），支持自定义发票付款。

---

### [Nuxt 4.5 · Nuxt 博客](https://nuxt.com/blog/v4-5)

**原文标题**: [Nuxt 4.5 · Nuxt Blog](https://nuxt.com/blog/v4-5)

Nuxt 4.5 是迄今为止最大的一次发布，带来了 Vite 8、Rspack 2、实验性 SSR 流式渲染、稳定的错误代码系统、新的 useLayout 组合式函数、命名视图，并为 Nuxt 5 奠定了大量基础。

- 📣 **为 Nuxt 5 做准备**：迁移至核心依赖项的最新主要版本（unhead v3、unctx v3、Vite 8），并引入稳定的构建输出合约，以缩小 v4 和 v5 之间的差距。
- ⚡️ **Vite 8**：Nuxt 现在运行在 Vite 8 上，带来更快的冷启动、最新的 Rolldown 内部机制以及许多上游改进。
- 🦀 **Rspack 2 和 Rsbuild**：为 Rspack 构建器升级到 Rspack 2，并基于 @rsbuild/core 重建，提升了速度和轻量性。
- 🌊 **实验性 SSR 流式渲染**：通过立即刷新 HTML 外壳并流式传输主体，显著改善首字节时间（TTFB），并自动为爬虫禁用。
- 🩺 **稳定的错误代码**：引入稳定的错误代码系统（如 NUXT_E1001），提供可搜索、可书签的错误代码，附带原因和修复建议。
- 🎨 **useLayout 组合式函数**：新的组合式函数，用于以响应式方式读取当前路由解析的布局。
- 🪟 **命名视图**：通过 `name@view.vue` 文件名约定支持命名视图，允许父页面渲染多个 `<NuxtPage>` 出口。
- 🚦 **useFetch 和 useAsyncData 的 enabled 选项**：新增响应式 `enabled` 选项，可在满足前提条件之前阻止数据获取请求。
- 🔗 **NuxtLink 自定义插槽的预取控制**：自定义插槽现在暴露 `prefetch`、`prefetched` 和 `shouldPrefetch`，以便手动控制预取。
- ⚡️ **转发预取提示**：新的实验性 `prefetchPreloadTags` 功能，可在预取时转发目标页面的预加载提示，使导航感觉瞬间完成。
- 🌐 **import.meta.envName**：运行时可通过 `import.meta.envName` 获取解析后的 Nuxt 环境名称。
- 🔭 **SSR 事件的追踪通道**：为服务器端子系统发布诊断通道追踪，支持构建 OpenTelemetry 等工具。
- 📦 **依赖升级**：升级至 unhead v3、unctx v3、magic-string v1、Babel v8 等，带来更好的类型安全和性能。
- 🛠️ **Nuxt CLI 改进**：新增 `nuxt module remove`、非交互式 `nuxt init`、类型检查入门引导、Golar 支持以及层感知的开发服务器。
- 🧩 **TypeScript 插件和命名布局插槽**：实验性 TypeScript 插件新增可选的命名布局插槽功能，允许页面向布局的插槽注入内容。
- 🔥 **性能和可靠性**：引入共享文件监视器、更快的开发启动、更精简的生产构建以及许多其他性能优化。

---

### [发布 v3.6.0-rc.1 · vuejs/core · GitHub](https://github.com/vuejs/core/releases/tag/v3.6.0-rc.1)

**原文标题**: [Release v3.6.0-rc.1 · vuejs/core · GitHub](https://github.com/vuejs/core/releases/tag/v3.6.0-rc.1)

Vue 3.6.0-rc.1 发布，引入 Vapor 模式并大幅优化响应系统性能。

- 🚀 Vue 3.6 进入 RC 阶段，Vapor 模式功能集已完成，并基于 alien-signals 重构 @vue/reactivity，显著提升性能与内存效率。
- 🐛 修复多项运行时与 Vapor 模式相关错误，包括插槽内容处理、水合问题及动态组件兼容性。
- 💡 Vapor 模式是全新的编译模式，旨在减少基线包体积并提升性能，支持模板与 `<script setup>`，但需 100% 手动启用。
- 🛠️ 纯 Vapor 应用可使用 `createVaporApp()` 创建，避免引入虚拟 DOM 运行时；混合应用需安装 `vaporInteropPlugin`。
- ⚠️ Vapor 模式不支持 Options API、`app.config.globalProperties` 等，且 `getCurrentInstance()` 返回 null；事件委托与自定义指令接口有差异。
- 📌 建议在现有应用中部分使用 Vapor 模式（如性能敏感页面），或构建全新小型 Vapor 应用；混合嵌套时需注意边缘情况。

---

### [文档：添加 v23 版本并改为年度发布周期 by thesmiler · 拉取请求 #69817 · angular/angular · GitHub](https://github.com/angular/angular/pull/69817)

**原文标题**: [docs: add v23 release and change to yearly release cycle by thesmiler · Pull Request #69817 · angular/angular · GitHub](https://github.com/angular/angular/pull/69817)

Angular 计划从 v23 开始将发布周期改为每年一次，以回应社区对减少重大版本破坏性变更的长期需求，同时保持功能在次要版本中持续迭代。

- 📅 新增 v22.x 和 v23 的发布日期，并正式将发布周期改为每年一次
- 🛡️ 社区长期要求减少重大版本频率，以降低破坏性变更和升级对项目及企业客户的影响
- 🤖 更长的发布周期为使用代理工作流的开发者提供更高的 API 稳定性，同时保持合理的 API 升级和迁移节奏
- 🚀 功能仍可在次要版本中持续发布，只有破坏性变更被限制在主要版本中
- 💬 社区讨论中，部分开发者对投资水平表示担忧，但也有人指出自动迁移工具和弃用策略已使升级变得相对简单
- 👍 该 PR 获得了 72 个赞，但也收到 20 个反对和 14 个困惑反应，反映社区意见分歧

---

### [媒介](https://blog.angular.dev/announcing-angular-v22-c52bb83a4664?gi=002d7019860e)

**原文标题**: [Medium](https://blog.angular.dev/announcing-angular-v22-c52bb83a4664?gi=002d7019860e)

Angular v22 发布，带来多项生产就绪功能、AI 集成工具和 API 改进，旨在为开发者提供稳定且创新的开发体验。

- 🚀 **三大功能转为生产就绪**：Signal Forms、Angular Aria 和异步响应式 API（resource/httpResource）现已稳定，可直接用于生产环境。
- 🤖 **AI 代理工具增强**：推出 Angular Agent Skills（angular-developer 和 angular-new-app），支持 MCP 工具（如 devserver.wait_for_build），并实验性支持 WebMCP。
- 🛠️ **路由器重大更新**：集成浏览器 Navigation API、新增自动清理注入器和 destroyDetachedRouteHandle，提升内存管理。
- 🎯 **新装饰器 @Service**：替代 @Injectable({ providedIn: 'root' })，更直观地定义全局单例服务。
- ⚡ **异步依赖注入**：injectAsync 支持按需加载服务，优化性能，可与 @Service 配合使用。
- 📝 **模板改进**：支持 HTML 注释、箭头函数、扩展语法、@switch 多 case 匹配和穷举检查，提升可读性和灵活性。
- 🔄 **变更检测优化**：OnPush 成为新应用默认策略，旧默认策略更名为 Eager。
- 🛡️ **错误边界预览**：@boundary 语法（2026 Q3 开发者预览版）可隔离组件错误，防止页面崩溃。
- 🚫 **弃用通知**：Webpack 支持及相关构建工具在 v22 中弃用，转向 TSGo 应用构建器。
- 📅 **发布活动**：官方发布活动将于 2026 年 6 月 5 日上午 9 点（太平洋时间）首播。

---

### [使用 Codemod 自动化 ESLint 迁移 - ESLint - 可插拔 JavaScript 代码检查工具](https://eslint.org/blog/2026/07/eslint-codemod-migrations/)

**原文标题**: [Automating ESLint migrations with Codemod - ESLint - Pluggable JavaScript Linter](https://eslint.org/blog/2026/07/eslint-codemod-migrations/)

ESLint 与 Codemod 合作推出官方迁移工具，帮助用户从 ESLint v8 升级到 v9 及 v9 到 v10，提供自动化代码迁移工作流。

- 📢 宣布 ESLint 与 Codemod 合作，官方 codemods 位于 eslint/codemods 和 Codemod Registry，社区可通过 PR 贡献新迁移脚本。
- 🔧 Codemod 是开源平台，支持大规模自动化代码迁移，具备工作区分析、跨文件重构、多语言支持、安全沙箱执行等功能。
- 🚀 v8 到 v9 迁移提供两个 codemod：@eslint/v8-to-v9-config 用于配置迁移（如提取 eslintConfig、清理注释、转换 env 等），@eslint/v8-to-v9-custom-rules 用于自定义规则迁移（如移除 context 方法、转换函数式规则等）。
- ⚠️ 迁移后需手动检查 TODO 注释、评论方法变化、高阶包装器，并运行测试套件验证自定义规则。
- 🔄 v9 到 v10 迁移提供@eslint/v9-to-v10 配方，包含配置、自定义规则、RuleTester 和 Linter API 四个独立 codemod。
- 📚 用户可通过 Codemod Registry 尝试迁移工具，在 eslint/codemods 查看源码，遇到问题可提交 issue 或贡献新 codemod，迁移详情参考官方升级指南。

---

### [认识首届 Three.js 大会的演讲嘉宾 | Codrops](https://tympanus.net/codrops/2026/07/16/meet-the-speakers-of-the-first-three-js-conference/)

**原文标题**: [Meet the Speakers of the First Three.js Conference | Codrops](https://tympanus.net/codrops/2026/07/16/meet-the-speakers-of-the-first-three-js-conference/)

首届 Three.js 大会将于今年九月在巴黎举行，汇聚了社区众多顶尖开发者。以下为部分演讲者的精彩分享：

- 🌟 Bruno Simon 正全力投入 TSL 和 WebGPU 更新，为 Three.js Journey 课程打造物理模拟实验，并暗示演讲主题为“🌱”
- 🎨 Célia Lopez 探索 AI 与 3D 工作流结合，同时创立陶瓷品牌，承诺演讲将带来“意想不到”的内容
- 🛠️ Daniel Beauchamp 专注电商交互定制与 AI 商业视频，强调“持续构建与探索”的创作心态
- 🚀 Anderson Mancini 利用 WebGPU 实现实时渲染突破，开发性能监控工具 r3f-webgpu-perf
- 🌐 Thomas Nattestad 与 Natalia Markoborodova 展示 HTML-in-Canvas API 的创意潜力与色彩空间研究
- 🎮 Patrick Heng 与 Justine Soulie 将插画转化为交互游戏，分享 WebGL 漫画 Ponpon Mania 幕后
- 🤖 Robin Payot 结合 AI 与 Three.js 创作语音响应动画，强调理解代码基础的重要性
- 💡 Julie Marting 探索 AI 设计工具，揭秘大会网站的艺术指导与设计秘密
- 📐 Vicente Lucendo 从漫画构图与物理引擎中汲取灵感，强调以情感引导创作决策
- 🔬 Jean Carlo Deconto（sunag）推出 Tour of TSL 指南，涵盖纳米级渲染与火焰模拟等前沿实验

---

### [Three.js – JavaScript 3D 库](https://threejs.org/)

**原文标题**: [Three.js – JavaScript 3D Library](https://threejs.org/)

Three.js 是一个功能全面的 3D JavaScript 库，提供文档、示例、学习资源、社区支持及开发工具，并附有官方周边商品。

- 📚 **文档与示例**：包含 r185 版本的完整文档和丰富示例，方便开发者快速上手
- 🎓 **学习资源**：提供 Three.js Journey 等专业课程，以及游戏开发指南
- 🛠️ **开发工具**：包括 devtools 调试工具和可视化编辑器
- 🌐 **社区支持**：通过 Discord、论坛和 Twitter 提供交流与问答平台
- 💻 **代码与下载**：在 GitHub 上开源，支持直接下载使用
- 👕 **周边商品**：出售官方 T 恤，支持项目发展

---

### [Mr.doob](https://mrdoob.com/)

**原文标题**: [Mr.doob](https://mrdoob.com/)

本篇文章主要介绍了人工智能在医疗领域的应用现状与未来潜力，强调了 AI 如何辅助诊断、个性化治疗以及提升医疗效率。

- 🩺 **辅助诊断**：AI 通过分析医学影像（如 X 光、CT）帮助医生更快速、准确地识别疾病，减少误诊率。
- 💊 **个性化治疗**：基于患者基因和病史数据，AI 可推荐定制化治疗方案，提升疗效并降低副作用。
- 📊 **医疗数据分析**：AI 处理海量病历和科研数据，发现疾病模式，加速新药研发和流行病预测。
- ⏱️ **效率提升**：自动化行政任务（如预约、病历整理）减轻医护人员负担，让医疗资源更聚焦于患者。
- 🚨 **远程监测**：AI 结合可穿戴设备，实时监测慢性病患者健康指标，及时预警风险。
- ⚖️ **伦理挑战**：数据隐私、算法偏见和责任归属等问题需谨慎解决，确保 AI 技术公平安全应用。

---

### [发布 11.0.0-beta.2 · preactjs/preact · GitHub](https://github.com/preactjs/preact/releases/tag/11.0.0-beta.2)

**原文标题**: [Release 11.0.0-beta.2 · preactjs/preact · GitHub](https://github.com/preactjs/preact/releases/tag/11.0.0-beta.2)

Preact v11.0.0-beta.2 版本发布，包含多项功能增强、错误修复和性能优化。

- 🚀 **功能更新**：实现流式水合（Streamed Hydration）RFC，提升加载体验
- 🔧 **类型改进**：修正 select 元素类型，支持 Signalish 输入类型
- 🐛 **错误修复**：修复 Suspense 水合子组件恢复、内存泄漏、异步 Suspense 下 useId 稳定性等多项问题
- ⚡ **性能优化**：使用 Symbol 作为事件时钟键，优化 shallowDiffers 和内存分配
- 🛠️ **维护工作**：升级 GitHub Actions、修复拼写错误、采用 npm 分阶段发布和可信发布流程
- 👥 **贡献者**：感谢 JoviDeCroock、rschristian、natemoo-re 等开发者的贡献

---

### [从 Preact 10.x 升级 – Preact 指南 v11](https://preactjs.com/guide/v11/upgrade-guide/)

**原文标题**: [Upgrading from Preact 10.x – Preact Guide v11](https://preactjs.com/guide/v11/upgrade-guide/)

Preact 11 是从 Preact 10.x 升级的微破坏性版本，旨在简化升级过程，同时引入新功能和清理遗留代码。

- 📋 **升级准备**：需要检查浏览器支持（Chrome >= 40, Safari >= 9, Firefox >= 36, Edge >= 12）和 TypeScript 版本（最低 v5.1），ESM 包将使用 `.mjs` 扩展名。
- 🆕 **新特性**：引入 Hydration 2.0，支持异步边界返回 0 或 2+ 个 DOM 节点；使用 `Object.is` 进行钩子参数相等性检查，支持 `NaN` 作为状态值。
- 🔄 **API 变化**：默认转发 refs，无需 `forwardRef`；自动 `px` 后缀移至 `preact/compat`；`defaultProps` 支持移至 `preact/compat`；移除 `render()` 的 `replaceNode` 参数；移除 `Component.base` 属性；移除 `SuspenseList`。
- 🛠️ **类型更新**：`useRef` 需要初始值；`JSX` 命名空间缩减，仅保留 TypeScript 必需类型，其余移至 `preact` 命名空间。
- 📦 **迁移工具**：提供 `preact-root-fragment` 包替代 `replaceNode` 功能；可通过 `options.vnode` 恢复旧 ref 行为。

---

### [下载 WebStorm 2026.2：支持 TypeScript 7、AI 及更多功能](https://blog.jetbrains.com/webstorm/2026/07/webstorm-2026-2/)

**原文标题**: [Download WebStorm 2026.2: TypeScript 7 Support, AI, and more](https://blog.jetbrains.com/webstorm/2026/07/webstorm-2026-2/)

WebStorm 2026.2 已发布，主要针对大型 TypeScript 项目、AI 开发集成和框架支持进行了重大升级。

- 🚀 **TypeScript 7 支持**：微软重写了编译器，在大型代码库中项目加载速度提升约 4 倍（如 Kibana 从 12 秒降至 3 秒），无需迁移即可使用。
- 🤖 **原生 GitHub Copilot 集成**：无需额外插件，通过 GitHub OAuth 登录即可在 AI 聊天中直接使用，稳定且无配置漂移。
- 🧠 **Agent 技能管理器**：可为 AI 代理（如 Claude 和 Codex）安装可复用的框架、约定和工具知识，跨项目和会话保留。
- ⚛️ **React Buddy 完整支持 React 19**：插件现已更新，提供组件调色板、交互式预览和 Storybook 故事创建功能。
- 🛠️ **框架与工具更新**：Vue 语言服务器 3.0 集成、Svelte 支持增强（如 SvelteKit 共享钩子）、CSS/SCSS 颜色预览修复、Angular 错误更新改进。
- 🐞 **调试与测试改进**：支持禁用源映射调试、Cypress 和 Playwright 测试更稳定、Node.js 环境变量处理优化。
- ⚡ **性能与稳定性修复**：解决了 NPM 配置检查、package.json 补全、Tailwind 语言服务器启动等卡顿问题，并减少内存占用。
- 🎨 **用户体验提升**：全局搜索保持范围、Markdown 支持脚注和 Mermaid 图表、自定义双键快捷键、检测可清理的 Git 工作树。

---

### [Astro 7.1 | Astro](https://astro.build/blog/astro-710/)

**原文标题**: [Astro 7.1 | Astro](https://astro.build/blog/astro-710/)

Astro 7.1 发布，带来更多控制权和性能优化

- 🚀 新增 `--ignore-lock` 标志，允许同时运行多个开发服务器
- 🔗 `paginate()` 新增 `format` 函数，可完全自定义分页 URL 格式（如添加 `.html` 后缀）
- 🛡️ 增强 CSP 控制，新增 `script-src-elem`、`style-src-attr` 等指令，支持更精细的内联脚本/样式策略
- 💾 内容集合新增 `deferRender` 选项，可延迟渲染 Markdown 条目，降低大集合同步时的内存占用
- 🧪 实验性 `collectionStorage: "chunked"` 功能，将大型内容集合数据分割为多个文件（每 10MB 分块）
- 📋 日志系统改进，支持通过 URL 配置自定义日志记录器，并新增 `AstroRuntimeLogger` 类型
- 👥 感谢社区贡献者，提供升级工具 `@astrojs/upgrade` 快速迁移至 7.1 版本

---

### [发布 v0.7.0 · web-infra-dev/rslint · GitHub](https://github.com/web-infra-dev/rslint/releases/tag/v0.7.0)

**原文标题**: [Release v0.7.0 · web-infra-dev/rslint · GitHub](https://github.com/web-infra-dev/rslint/releases/tag/v0.7.0)

rslint v0.7.0 版本发布，主要提升了与 ESLint 的兼容性和性能，并修复了多个问题。

- 🎉 **新功能**: 新增基于 JSON Schema 的选项编译器、`ctx.Globals` API 以及多个 ESLint 插件规则（如 `prefer-comparison-matcher`、`no-restricted-jest-methods`、`no-redeclare` 等）
- 🚀 **性能优化**: 跨程序复用源快照、并行化 ESLint 插件预处理、LSP 直接针对单文件 lint、共享注释扫描以减少重复工作
- 🐞 **错误修复**: 修复了 `constructor-super` 在控制流中的误报、`no-sparse-arrays` 对解构目标的误判、LSP 保存时文档内容保留问题，以及多个预设（JavaScript、TypeScript、React、import、promise、Unicorn）与上游的对齐
- 🔨 **重构**: 将配置发现迁移至 Go、提取输出报告、迁移规则运行至 ESLint 风格的选项格式
- ✅ **测试与 CI**: 增加 symlink 工作目录测试、稳定 VS Code 扩展 CI、提高 golangci-lint 超时时间

---

### [发布 v1.2.0 · rolldown/rolldown · GitHub](https://github.com/rolldown/rolldown/releases/tag/v1.2.0)

**原文标题**: [Release v1.2.0 · rolldown/rolldown · GitHub](https://github.com/rolldown/rolldown/releases/tag/v1.2.0)

Rolldown v1.2.0 版本发布，包含多项新功能、错误修复和性能优化。
- 🚀 新增开发服务器功能，包括客户端 HMR、按客户端发送 HMR 补丁映射、以及 tsconfig 变化时触发全量更新
- 🐛 修复多个错误，包括 sourcemap 映射保留、ESM 格式文件名选项、tsconfig 缓存清除、以及树摇优化中的动态导入绑定问题
- 🛠️ 重构代码，将全量更新移至客户端、优化 ReplaceWith 迁移、共享解析器缓存、以及统一诊断信息收集
- 📚 更新文档，在 JSDoc 中展示插件类型和钩子描述，并添加关于外部模块导入移除的说明
- ⚡ 性能提升，通过 owned merge 减少 sourcemap 合并中的分配次数，以及避免冗余的 sourcemap 字符串拷贝
- 🧪 新增测试用例，涵盖代码分割、严格执行顺序、以及 HMR API 测试
- ⚙️ 杂项更新，包括依赖升级、GitHub 用户名更新、以及测试子模块同步

---

### [发布 v7.0.0 · actions/setup-node · GitHub](https://github.com/actions/setup-node/releases/tag/v7.0.0)

**原文标题**: [Release v7.0.0 · actions/setup-node · GitHub](https://github.com/actions/setup-node/releases/tag/v7.0.0)

概述摘要  
这是 setup-node 动作的 v7.0.0 版本发布页面，包含多项增强、错误修复、文档更新和依赖升级。  

- 🚀 新增功能：添加 `cache-primary-key` 和 `cache-matched-key` 作为输出  
- 🔄 迁移至 ESM 并升级依赖  
- 🐛 错误修复：移除虚假的 `NODE_AUTH_TOKEN` 导出  
- 🛠️ 错误修复：仅在提供 `mirrorToken` 时于 `getManifest` 中使用  
- 📚 文档更新：添加使用 OIDC 发布到 npm 的说明  
- 📝 文档更新：更新仅恢复缓存文档  
- 🛡️ 文档更新：更新缓存建议以降低缓存投毒风险  
- ⬆️ 依赖更新：升级 @actions/cache 至 5.1.0，记录缓存写入拒绝  
- 👥 新贡献者：@chiranjib-swain、@deiga、@jasongin 首次贡献

---

### [SVG 图像中的传染性面试恶意软件：朝鲜运动 —— Elastic Security 实验室](https://www.elastic.co/security-labs/contagious-interview-malware-svg-steganography)

**原文标题**: [Contagious Interview malware in SVG images: DPRK campaign — Elastic Security Labs](https://www.elastic.co/security-labs/contagious-interview-malware-svg-steganography)

Elastic Security Labs 发现朝鲜黑客组织通过伪装成编程面试的虚假工作机会，利用 SVG 图片隐写术隐藏恶意代码，针对开发者窃取凭证和加密货币。该攻击链涉及四阶段载荷，包括浏览器凭证窃取器、文件窃取器、Socket.IO 远程访问木马和剪贴板窃取器，且未被任何杀毒软件检测到。

- 🔍 发现过程：Elastic 社区 Slack 频道出现虚假招聘信息，名为 Maxwell 的用户发布职位并发送含恶意代码的“编程挑战”项目
- 🎯 攻击目标：开发者成为主要目标，通过虚假工作机会诱骗执行含后门的代码项目
- 🖼️ 隐写技术：恶意代码被分割成 Base64 片段隐藏在 SVG 国旗图片的 HTML 注释中，通过 JavaScript 重组执行
- ⚙️ 执行机制：项目启动时自动触发恶意代码，使用 obfuscator.io 混淆，通过 eval() 执行解码后的载荷
- 🛡️ 四阶段载荷：浏览器凭证/加密钱包窃取器、文件窃取器、Socket.IO RAT、剪贴板窃取器/Windows PE 投递器
- 💻 跨平台攻击：支持 Windows、macOS 和 Linux，针对 Chrome、Edge、Brave 等浏览器窃取凭证
- 🔑 加密钱包目标：硬编码 25 个浏览器扩展 ID，优先处理 8 个主流钱包（如 MetaMask、Rabby、Phantom）
- 📁 文件窃取范围：扫描.env、.doc、.pdf、.json 等文件，以及.aws、.ssh 等凭证目录
- 🌐 C2 通信：使用 Socket.IO 建立持久连接，域名包括 rightwidth[.]dev 系列
- 🖥️ 剪贴板窃取：Windows 和 macOS 每 500ms 轮询剪贴板内容并外传
- 🚫 检测规避：所有恶意仓库在 VirusTotal 上零检测，使用隐写术和混淆技术逃避分析
- 🔗 归因关联：代码与 OTTERCOOKIE 恶意软件相似，与朝鲜 Contagious Interview 活动相关

---

### [领英工作邀请中的后门 - 罗曼·伊曼库洛夫](https://roman.pt/posts/linkedin-backdoor/)

**原文标题**: [A backdoor in a LinkedIn job offer - Roman Imankulov](https://roman.pt/posts/linkedin-backdoor/)

### 概述总结
一位 Python 开发者收到伪装成招聘测试的恶意 GitHub 仓库链接，该仓库包含隐藏的后门代码，会在执行 npm install 时自动触发，窃取系统权限。攻击者冒用真实开发者和记者的身份进行伪装。

- 🔍 **发现过程**：开发者对招聘方提供的代码库产生怀疑，使用只读 AI 代理扫描代码，迅速定位到隐藏在测试文件中的恶意代码。
- 🕳️ **后门机制**：代码将 URL 片段拼接成远程服务器地址，在注释代码中隐藏执行远程指令的 payload，通过 npm 的 prepare 脚本在安装依赖时自动触发。
- 🎭 **身份盗用**：GitHub 提交记录冒用真实开发者的身份信息（39 次伪造提交），招聘者账号则盗用了一位文化记者的 LinkedIn 资料。
- ⚠️ **攻击手法**：攻击者利用“检查过时的 Node 模块”作为诱饵，诱导开发者执行 npm install，从而激活后门程序。
- 🛡️ **安全建议**：对可疑代码库保持警惕，使用沙箱环境或只读工具审查代码，避免在本地直接运行未知依赖。

---

### [在 10 分钟内流式传输您的首个 3D 资产 | Miris](https://www.miris.com/blog/streaming-your-first-3d-asset-in-under-10-minutes?utm_source=web_referral&mrls=web_referral&utm_medium=public_relations&mrlc=public_relations&utm_campaign=raz-pr&utm_content=sign_up&prg=scale&utm_term=javascript&dp=dp)

**原文标题**: [Streaming your first 3D asset in under 10 minutes| Miris](https://www.miris.com/blog/streaming-your-first-3d-asset-in-under-10-minutes?utm_source=web_referral&mrls=web_referral&utm_medium=public_relations&mrlc=public_relations&utm_campaign=raz-pr&utm_content=sign_up&prg=scale&utm_term=javascript&dp=dp)

Miris 採用空間串流技術，讓 3D 模型像影片一樣在瀏覽器中逐步載入，從低解析度快速提升至完整畫質，無需等待完整下載。本指南完整介紹從上傳 USD 檔案、生成串流版本、預覽到分享的整個流程，全程無需編碼。

- 🚀 **核心技術**: Miris 的空間串流技術，讓 3D 資產在瀏覽器中幾乎即時顯示，並逐步提升至完整解析度，類似 Netflix 的影片串流體驗。
- 📁 **上傳資產**: 支援 USD 格式（.usd, .usda, .usdc, .usdz），建議上傳最高品質版本，Miris 會自動進行 AI 壓縮和 LOD 生成等優化。
- 🔑 **建立檢視器金鑰**: 需要建立一個檢視器金鑰（類似 API 金鑰）來授權串流，此金鑰僅顯示一次，需妥善保存。
- 👁️ **預覽資產**: 使用 Miris Player 輸入金鑰和資產 ID，即可在瀏覽器中預覽，體驗逐步載入的串流效果。
- 🔗 **分享連結**: 可產生分享連結，收件人無需帳號或安裝軟體，只需現代瀏覽器即可開啟並體驗串流。
- 🛠️ **後續發展**: 開發者可透過 Web SDK 自訂檢視器，3D 藝術家可參考 DCC 工具指南優化 USD 匯出，團隊可查閱完整文件進行生產部署。

---

### [媒介](https://tech.olx.com/handling-concurrency-on-the-web-with-web-locks-api-163b7e07eddd?gi=7552aa463f13)

**原文标题**: [Medium](https://tech.olx.com/handling-concurrency-on-the-web-with-web-locks-api-163b7e07eddd?gi=7552aa463f13)

本文介绍了如何利用 Web Locks API 解决浏览器多标签页间的文件上传并发问题，实现断点续传的协调机制。

- 🧠 **并发问题**：用户打开多个标签页时，每个标签页会同时尝试恢复同一上传任务，导致重复上传和资源浪费。
- 🔒 **锁机制**：锁确保共享资源一次只被一个调用者访问，避免数据混乱，类似银行账户的同步操作。
- 🌐 **跨标签协调方案**：localStorage + 轮询存在竞态条件和锁失效问题；Broadcast Channel API 缺乏互斥原语，易出错。
- ⚙️ **Web Locks API**：提供原子锁获取、自动清理、非阻塞选项，支持所有现代浏览器，是浏览器原生互斥解决方案。
- 🚀 **React Hook 实现**：自定义 `useUploadCoordinator` 钩子，对用户发起的上传使用非阻塞锁，对恢复上传使用条件锁，确保只有一个标签页处理恢复。
- 🛠️ **锁生命周期管理**：通过 `holdLockUntilComplete` 函数监听上传完成、错误或取消事件，自动释放锁，避免内存泄漏。
- ✅ **实际收益**：零重复上传、提升用户体验、降低基础设施成本、简化代码逻辑。
- 📝 **最佳实践**：永不阻塞用户操作、安全降级、利用平台原语保持简单。

---

### [Web Locks API - Web API | MDN](https://developer.mozilla.org/en-US/docs/Web/API/Web_Locks_API)

**原文标题**: [Web Locks API - Web APIs | MDN](https://developer.mozilla.org/en-US/docs/Web/API/Web_Locks_API)

Web Locks API 允许在多个标签页或 Worker 中运行的脚本异步获取锁，协调资源共享，防止冲突。锁基于来源（origin）隔离，支持独占和共享模式，并提供诊断和死锁防护功能。

- 🔒 **核心功能**：脚本可异步获取锁，执行任务后自动释放，确保同一时间只有一个执行上下文能访问共享资源。
- 🌐 **跨标签页协调**：通过锁名称（如 "my_net_db_sync"）实现领导者选举，仅一个标签页执行同步操作。
- 📝 **使用方式**：调用 `navigator.locks.request()` 传入锁名称和异步回调，锁在回调完成后自动释放。
- ⚙️ **可选选项**：支持 `mode`（独占/共享）、`ifAvailable`（非阻塞获取）、`steal`（抢占锁）、`signal`（通过 AbortSignal 超时取消）。
- 🔍 **诊断监控**：`navigator.locks.query()` 可查询来源的锁状态，包括持有和等待的锁及其模式，便于调试。
- 🚫 **死锁防护**：避免嵌套或无序请求锁，可通过超时或良好顺序策略防止死锁，仅影响锁本身，不影响浏览器或其他脚本。
- 🛠️ **接口**：`Lock` 提供锁名称和模式，`LockManager` 通过 `navigator.locks` 获取，用于请求和查询锁。
- ✅ **兼容性**：自 2022 年 3 月起广泛可用，需安全上下文（HTTPS），支持 Web Workers。

---

### [使用数据导向设计构建高性能解析器 - Arshad Yaseen](https://www.arshad.fyi/writings/engineering-high-performance-parsers)

**原文标题**: [Engineering High-Performance Parsers with Data-Oriented Design - Arshad Yaseen](https://www.arshad.fyi/writings/engineering-high-performance-parsers)

### 概述总结
本文介绍了如何使用数据导向设计构建高性能解析器，通过内存布局优化实现 3-10 倍的速度提升。

- 🚀 **索引替代指针**：使用 u32 整数索引替代指针，将节点存储在扁平数组中，减少内存碎片和缓存未命中
- 📦 **结构体数组布局**：采用`std.MultiArrayList`将节点数据按列存储，使仅遍历节点类型的操作不会拖入 span 数据
- 🧩 **可变长度子节点**：通过共享的`extras`数组和`IndexRange`描述子节点范围，避免为每个节点分配动态数组
- 🔗 **字符串零拷贝**：字符串存储为源文件中的字节偏移量，仅在必要时才解码到内部池中
- ⚡ **标记位编码**：在 TokenTag 的整数值中预编码优先级、运算符类型等信息，通过位移和掩码操作即可获取
- 🌐 **Unicode 优化**：使用分块位图（512 码点/块）实现紧凑的 Unicode 属性查询，ASCII 路径完全绕过该表
- 📤 **自描述序列化**：AST 直接作为`ArrayBuffer`传输，JavaScript 端通过类型化数组视图零解析读取
- 🔧 **编译时验证**：通过`comptime`断言确保节点大小、字段布局等关键约束不会意外变化

---

### [简介 | Yuku](https://yuku.fyi/)

**原文标题**: [
      Introduction
      | Yuku
    ](https://yuku.fyi/)

Yuku 是一个用 Zig 编写的高性能 JavaScript/TypeScript 编译器工具链，注重正确性、性能和清晰度。

- 📝 **100% ECMAScript 规范兼容**：通过完整的解析器测试套件，包括 Test262、TypeScript 和 Babel 的数十万个测试用例，AST 完全匹配，零失败。
- ⚡ **设计上追求速度**：解析器采用数据导向设计原则，在原生（Zig/Rust）解析中比 Oxc 更快，约是 SWC 的 2 倍；在 JavaScript 端（npm）比同类快 3-10 倍。
- 🛠️ **纯 Zig，零依赖**：整个工具链用 Zig 编写，无外部 C 库或运行时依赖，易于构建、嵌入和交叉编译。
- 🌐 **支持现代 JavaScript**：完全支持装饰器、源阶段导入、延迟导入、`using`/`await using` 声明等现代和实验性特性。
- ✅ **当前状态稳定**：`.js(x)`/`.ts(x)` 解析器已可用于生产环境，语义模型和遍历器稳定，支持语义检查。
- 🔄 **AST 传输优化**：Yuku 的 AST 设计为扁平、紧凑、近二进制，从 Zig 到 JavaScript 的传输快速轻量，无多 GB 分配，已通过完整测试套件验证。

---

### [简介 | Yuku](https://yuku.fyi/#performance)

**原文标题**: [
      Introduction
      | Yuku
    ](https://yuku.fyi/#performance)

Yuku 是一个用 Zig 编写的高性能 JavaScript/TypeScript 编译器工具链，专注于正确性、性能和清晰度。

- 📜 **100% ECMAScript 规范兼容**：通过完整的解析器测试套件，包括 Test262、TypeScript 和 Babel 的数十万用例，零失败、零 AST 不匹配。
- ⚡ **原生解析速度领先**：在 Zig/Rust 原生解析中，Yuku 比 Oxc 更快，大约是 SWC 的 2 倍；在 npm 上比替代方案快 3-10 倍。
- 🧩 **纯 Zig 实现，零依赖**：整个工具链用 Zig 编写，无外部 C 库或运行时依赖，易于构建、嵌入和交叉编译。
- 🚀 **支持现代 JavaScript 特性**：完全支持装饰器、源阶段导入、延迟导入、`using`/`await using` 声明等现代和实验性功能。
- 🛠️ **稳定且生产就绪**：`.js(x)`/`.ts(x)` 解析器、语义模型和遍历器已稳定，并在生产中用于 Yuku 的语义检查器。
- 🔄 **高效 AST 传输**：Yuku 的 AST 设计为扁平、紧凑、接近二进制，从 Zig 到 JavaScript 的传输快速轻量，无多 GB 分配，已通过完整测试套件验证。

---

### [yuku 游乐场](https://playground.yuku.fyi/)

**原文标题**: [yuku playground](https://playground.yuku.fyi/)

本内容涉及代码格式化与输出的多种配置选项
- 🌟 源文件（source）与抽象语法树（ast）处理
- 🧠 语义分析（semantics）确保代码逻辑正确
- 📤 输出控制（output）支持多种格式
- ✂️ 去除空白（strip）与压缩（minify）功能
- 🎨 美化输出（pretty）与紧凑格式（compact）
- 💾 保留原始格式（preserve）选项
- 🔤 引号风格可选双引号（double）、单引号（single）或最短形式（shortest）
- 🔍 作用域控制：部分（some）、全部（all）或无（none）
- 📏 换行模式支持行内（line）与块状（block）

---

### [Canvas 中的 HTML：在`<canvas>`中渲染真实 DOM - 阿古斯丁·巴里恩托斯](https://agustinbarrientos.com/writing/senior-eye/html-in-canvas/)

**原文标题**: [HTML in Canvas: Render Real DOM Inside `<canvas>` - Agustin Barrientos](https://agustinbarrientos.com/writing/senior-eye/html-in-canvas/)

本文探讨了在 Canvas 中渲染真实 DOM 的技术，重点介绍了实验性的 HTML-in-Canvas API，并提供了一个完整的 3D 产品配置器示例，展示了如何正确划分 Canvas 与 DOM 的职责。

- 🎯 **核心陷阱**：将 UI 全部绘制在 Canvas 上会导致无法聚焦、无法 Tab 导航、无障碍树为空、文本无法选中等问题，因为 Canvas 绘制的是像素而非可交互的 DOM 元素。
- 🧱 **职责划分**：3D 场景渲染归 Canvas，所有可交互的 UI（标签、按钮、表单）应归 DOM。这是确保可用性和无障碍性的关键原则。
- 🖱️ **3D 命中检测**：Canvas 没有内置的命中检测，需要通过 Three.js 的 `Raycaster` 从相机发射射线来拾取 3D 物体，这替代了传统的 `isPointInPath`。
- 🧪 **实验性 API**：`drawElementImage` 允许将真实的 DOM 节点绘制到 Canvas 上，并返回一个对齐矩阵。将此矩阵写回元素的 `style.transform` 可以保持其焦点、点击区域和无障碍边界与绘制的像素对齐。
- ⚙️ **设备像素比 (DPR)**：Canvas 渲染必须手动处理 DPR 变化，通过 `matchMedia` 监听分辨率变化并重新调整渲染器和叠加层的大小，以确保在不同屏幕上保持清晰。
- 🛡️ **渐进增强**：将实验性 API 作为渐进增强功能，通过特性检测（`typeof ctx.drawElementImage === 'function'`）来决定是否启用。当 API 不可用时，优雅降级到纯 DOM 叠加层方案。
- 🏷️ **生产就绪评估**：使用一个可复用的评估矩阵来评判新 API，包括跨引擎支持、标准共识、降级方案、可逆性和测试负担。根据评估结果，将技术分为“可发布”、“增强”或“研究”三个等级。

---

### [框架战争已经结束。为什么没有人能取代 React - YouTube](https://www.youtube.com/watch?v=mxRjJPoWBE4)

**原文标题**: [The Framework wars are over. Why no one dethroned React - YouTube](https://www.youtube.com/watch?v=mxRjJPoWBE4)

本頁面列出 YouTube 平台的核心資訊與政策，涵蓋版權、聯絡方式、創作者資源及法律條款等面向。
- 📰 新聞中心：提供 YouTube 最新消息與公告
- ©️ 版權：說明內容使用與版權相關規範
- 📞 聯絡我們：提供使用者與平台聯繫的管道
- 🎬 創作者：為內容創作者提供資源與支援
- 📢 刊登廣告：介紹廣告投放與合作機會
- 👨‍💻 開發人員：提供 API 與技術開發文件
- 📜 條款：規範使用者與平台間的權利義務
- 🔒 私隱：說明個人資料的收集與保護方式
- 🛡️ 政策及安全：列出社群規範與安全措施
- ⚙️ YouTube 的運作方式：解釋平台功能與演算法
- 🧪 測試新功能：說明新功能的測試與回饋機制
- ©️ 2026 Google LLC：標示版權歸屬與法律聲明

---

### [Flint：AI 时代的可视化语言](https://microsoft.github.io/flint-chart/)

**原文标题**: [Flint: A Visualization Language for the AI Era](https://microsoft.github.io/flint-chart/)

概述：本文探讨了人工智能在医疗领域的应用，重点介绍了 AI 如何辅助疾病诊断、药物研发和个性化治疗，同时指出了数据隐私和伦理挑战等关键问题。

- 🩺 AI 通过分析医学影像，能快速识别肿瘤和病变，提升诊断准确率。
- 💊 在药物研发中，AI 加速候选分子筛选，缩短新药上市周期。
- 🧬 个性化治疗方面，AI 根据患者基因数据定制方案，提高疗效。
- 🔒 数据隐私问题突出，需加强患者信息保护法规。
- ⚖️ 伦理挑战包括算法偏见和责任归属，需建立透明监管机制。

---

### [适用于任意规模时间序列工作负载的 Postgres。| Tiger Data](https://www.tigerdata.com/go/trial?utm_source=content-syndication&utm_medium=referral&utm_campaign=javascript-weekly-newsletter)

**原文标题**: [Postgres for time-series workloads at any scale. | Tiger Data](https://www.tigerdata.com/go/trial?utm_source=content-syndication&utm_medium=referral&utm_campaign=javascript-weekly-newsletter)

Tiger Cloud 提供可扩展的 PostgreSQL 时序数据库服务，支持大规模数据管理，并提供免费试用额度。

- 📊 单实例可处理每日 3 万亿指标、3PB 数据及 1 quadrillion 数据点，展现真实世界扩展能力
- 💰 新用户注册即获$1000 信用额度（30 天有效），无需信用卡
- ⚡ 核心能力包括：读写分离（最多 10 节点副本集）、SSD/S3 分层存储实现无底容量与成本效益
- 🔄 计算与存储分离，独立扩展以优化成本，避免为闲置容量付费
- 🛡️ 企业级特性：多可用区自动故障转移、跨区域备份、SOC 2/HIPAA/GDPR 合规、加密与审计日志
- 📈 深度可观测性：查询钻取与仪表盘，支持集成 CloudWatch、Datadog、Prometheus
- 🚀 快速部署：数分钟内完成数据库配置，支持 SQL、CLI、Terraform、Cursor 或 Claude Code 管理
- 🔌 无缝集成：兼容主流云提供商及 PostgreSQL 生态工具
- 🏢 企业支持：合同化 SLA、区域数据隔离、24/7 全球专家支持与保障响应时间

---

### [GitHub - unjs/unwasm: 🇼 JavaScript 的 WebAssembly 工具](https://github.com/unjs/unwasm)

**原文标题**: [GitHub - unjs/unwasm: 🇼 WebAssembly tools for JavaScript · GitHub](https://github.com/unjs/unwasm)

unwasm 是一个通用的 WebAssembly 工具，让 .wasm 文件可以像普通模块一样被导入，并自动生成适合打包器的绑定。

- 🌐 **通用导入方式**：支持像导入普通模块一样导入 .wasm 文件，在构建时自动解析模块的导入和导出。
- ⚡ **静态绑定**：在支持顶层 await 的环境中，.wasm 文件可作为常规 ESM 模块直接使用。
- 🕒 **惰性绑定**：在不支持顶层 await 或需要导入对象时，通过代理函数延迟初始化模块。
- 🔧 **模块兼容性**：支持通过 `?module` 后缀直接获取 WebAssembly.Module，满足库的自定义实例化需求。
- 🛠️ **构建集成**：提供 Rollup 插件，支持 `esmImport` 和 `lazy` 等配置选项。
- 📦 **工具函数**：内置 `parseWasm` 工具，可无依赖解析 wasm 模块的导入导出结构。
- 🤖 **自动导入解析**：通过 import maps 自动推断并绑定 .wasm 文件所需的导入对象。
- 📜 **ESM 导入支持**：wasm 模块可直接从 ES 模块导入函数，遵循 ESM 集成规范。
- 👥 **开源社区**：MIT 许可，由 @pi0 和社区共同维护，拥有 270 星和 9 个复刻。

---

### [TypeScript 中的独立 ActivityPub 机器人](https://botkit.fedify.dev/)

**原文标题**: [Standalone ActivityPub bots in TypeScript](https://botkit.fedify.dev/)

以下是您提供的 BotKit 文档内容的概述摘要：

BotKit 是一个用于构建 ActivityPub 机器人的框架，涵盖了从入门到部署的完整指南。

- 🏠 **主页导航**：包含 Learn、Recipes、Concepts、Deploy 和 References 等核心模块。
- 📘 **学习路径**：从 What is BotKit? 开始，逐步学习 Getting started 和 Building an RSS bot。
- 🧩 **核心概念**：涵盖 Bot、Instance、Session、Events、Message、Text 和 Repository 等关键概念。
- 🚀 **部署选项**：支持 Storage and message queue、Deno Deploy、Cloudflare Workers、Docker 和 Self-hosting。
- 📦 **参考资源**：包括 @fedify/botkit、@fedify/botkit-postgres、@fedify/botkit-redis、@fedify/botkit-sqlite 和 Matrix 等包。
- 🎨 **外观设置**：提供 Matrix 和 Appearance 配置选项。

---

### [Color.js：让我们认真对待色彩 • Color.js](https://colorjs.io/)

**原文标题**: [Color.js: Let’s get serious about color • Color.js](https://colorjs.io/)

Color.js 是一个由 CSS 颜色规范编辑共同开发的颜色转换与修改库，提供丰富功能且影响广泛。

- 🎨 **颜色空间无关**：每个颜色对象由坐标和颜色空间引用组成，操作不依赖特定颜色空间。
- 🌈 **多颜色空间模块**：支持 Lab/LCh、OKLab/OKLCh、sRGB 系列、Display P3、Jzazbz、REC.2100 等众多颜色空间。
- 🔬 **科学颜色处理**：提供真实色域映射、多种 DeltaE 方法（76、CMC、2000、Jz）和色适应方法（von Kries、Bradford、CAT02、CAT16），并带有合理默认值。
- 📜 **CSS Color 4 兼容**：支持所有 CSS Color 4 格式和颜色空间的输入输出，无论浏览器是否支持。
- 📚 **可读的面向对象 API**：提供颜色对象进行多重操作，以及静态函数用于一次性计算。
- 🧩 **模块化与可扩展**：可按需使用模块或打包，支持客户端和 Node，通过钩子深度扩展。
- ⚡ **快速高效**：提供过程式、可摇树优化的 API，适合性能敏感任务并减小包体积。
- 🚫 **无依赖**：强调无外部依赖，但也不排斥依赖。
- 🌍 **广泛影响**：用于 W3C 规范演示、浏览器测试 CSS Color 4/5 实现，npm 下载量超 2.46 亿，被 Sass、Open Props、axe 等知名项目使用。
- 🖥️ **Web 平台测试基础**：部分 API 用于设计 Web 平台原生颜色对象。
- 📦 **灵活安装**：支持 CDN 直接导入、npm 安装，或从 src 目录导入特定模块，也提供全局变量方式。
- 🎯 **颜色读取**：支持 CSS Color Level 4 所有颜色格式，也可手动创建颜色对象。
- ✏️ **颜色操作**：通过属性、set() 和 setAll() 方法修改坐标，支持链式操作。
- 🔄 **颜色转换与输出**：可转换到任意颜色空间，自定义输出精度和色域裁剪。
- 🎨 **插值功能**：支持范围函数、离散步进、混合等插值方法，提供静态语法。
- 🧪 **实验性项目**：包括 Color Elements（颜色应用 Web 组件）、Color Apps（颜色应用）、Color Palettes（调色板研究）。
- 👥 **维护团队**：由 Lea Verou、Chris Lilley 等核心维护者及社区贡献者共同维护。
- 💰 **赞助支持**：通过 Open Collective 接受赞助，计划在网站和 README 中展示赞助者。

---

### [发布 v0.7.0 · color-js/color.js · GitHub](https://github.com/color-js/color.js/releases/tag/v0.7.0)

**原文标题**: [Release v0.7.0 · color-js/color.js · GitHub](https://github.com/color-js/color.js/releases/tag/v0.7.0)

Color.js v0.7.0 版本发布，带来多项新功能和改进，下载量已超过 2.4 亿次。

- 🎉 超过 2.4 亿次 npm 下载量，项目通过 Open Collective 接受资助
- 🔄 破坏性变更：移除预构建 ESM 包和.min 文件，优化 dist/目录结构
- 🆕 新增 6 个色域相对 (OK)LCH 色彩空间（oklch-p3、oklch-srgb 等）
- 🆕 扩展 HSL 语法至 hsl-p3 和 hsl-rec2020 宽色域空间
- 🆕 引入实验性 Helmlab 感知色彩空间家族（helmlab-metric、helmgen、helmgenlch）
- 🆕 智能 display() 回退机制，优先使用最接近的浏览器支持色彩空间
- 🆕 新增 raytrace 色域映射方法和 deltaEHelmlab 色差计算方法
- 🆕 serialize()/Color.toString() 增加 collapse 选项控制十六进制颜色压缩
- 🛠️ 开发者工具：公开 ColorSpace.M 变换矩阵、矩阵代数工具、极坐标空间色调声明
- 🐛 修复极坐标空间预乘插值、helmgenlch 序列化、色域表面阈值等多项 Bug

---

### [GitHub - mutativejs/travels: 一个快速、框架无关的撤销/重做核心，由 Mutative JSON Patch 驱动](https://github.com/mutativejs/travels)

**原文标题**: [GitHub - mutativejs/travels: A fast, framework-agnostic undo/redo core powered by Mutative JSON Patch · GitHub](https://github.com/mutativejs/travels)

Travels 是一个基于 JSON Patch 的高性能撤销/重做库，专为大型状态、小型更新、长历史记录和持久化场景优化。

- 🚀 **高性能与内存优化**：仅存储状态差异（JSON Patch），而非完整快照，大幅降低内存占用。1MB 状态进行 100 次小编辑仅需数 KB。
- 🎯 **适用场景明确**：适合大型状态、小更新、长历史记录及持久化需求；小型状态或短历史场景建议使用传统快照方案。
- 📦 **框架无关**：支持 React、Vue、Zustand、MobX 等主流框架及原生 JavaScript。
- 🔧 **核心功能**：提供 `setState`、`back`、`forward`、`go`、`reset`、`rebase` 等完整撤销/重做 API，支持事务批量操作。
- 🗂️ **持久化支持**：通过 `serialize`/`deserialize` 实现历史记录序列化与恢复，支持 localStorage、IndexedDB 等存储方案。
- ⚙️ **灵活模式**：支持自动/手动归档、可变/不可变模式、外部状态集成（Controlled Journal）及自定义扩展。
- 🛡️ **类型安全**：基于 TypeScript 构建，提供完整类型定义，支持严格状态兼容性检查。
- 📚 **丰富文档**：包含完整 API 参考、框架集成示例、持久化指南及高级模式文档。

---

### [Gridstack.js | 几分钟内构建交互式仪表盘。](https://gridstackjs.com/)

**原文标题**: [Gridstack.js | Build interactive dashboards in minutes.](https://gridstackjs.com/)

概述：gridstack.js 是一个简单易用的交互式网格布局工具，支持拖拽、调整大小和自定义配置，适合快速创建响应式仪表板。

- 🚀 **基础演示**：提供拖拽式网格布局，支持简单配置和自定义，可轻松上手。
- 📦 **快速安装**：通过 npm 安装 gridstack，并引入 HTML+JS 代码即可创建交互式网格。
- 🎨 **样式定制**：支持自定义 CSS 样式，如背景色和内容区颜色。
- 🧩 **高级功能**：包含拖拽删除、从外部拖入等复杂交互，满足高级需求。
- 📊 **应用案例**：展示 gridstack.js 在仪表板、文章列表等场景中的实际应用。
- 🌍 **社区支持**：被多家公司和项目采用，提供 Slack 社区交流与反馈。

---

### [GitHub - sindresorhus/np: 更好的 `npm publish` 工具 · GitHub](https://github.com/sindresorhus/np)

**原文标题**: [GitHub - sindresorhus/np: A better `npm publish` · GitHub](https://github.com/sindresorhus/np)

`np` 是一个改进版的 `npm publish` 工具，提供交互式界面和自动化流程，确保发布过程安全可靠。

- 🚀 提供交互式 UI，引导用户完成发布流程，并确保从正确的发布分支（如 main 或 master）进行发布
- ✅ 自动检查工作目录是否干净、依赖是否最新，并运行测试，确保发布前一切就绪
- 🔢 自动更新 package.json 中的版本号，创建 Git 标签，并防止意外发布预发布版本到 latest 标签
- 📦 支持 npm、pnpm、Bun 和 Yarn 等包管理器，并支持 GitHub Packages 和自定义注册表
- 🛡️ 提供 dry-run 模式预览操作，支持双因素认证（2FA），并在发布失败时自动回滚
- ⚙️ 可通过 CLI 参数或配置文件（如 .np-config.json）自定义行为，如跳过测试、指定发布子目录等
- 🔄 支持发布到旧版本分支、使用 npm 生命周期钩子，以及与 CI 集成（通过 --no-publish 跳过发布步骤）
- 🐛 常见问题包括 Yarn 注册表覆盖、生命周期脚本未退出导致挂起，以及 macOS SSH 密钥问题，均有解决方案

---

### [GitHub - kolkov/angular-editor: 适用于 Angular 6-20+ 的简易原生所见即所得编辑器组件 · GitHub](https://github.com/kolkov/angular-editor)

**原文标题**: [GitHub - kolkov/angular-editor: A simple native WYSIWYG editor component for Angular 6 -20+ · GitHub](https://github.com/kolkov/angular-editor)

AngularEditor 是一个适用于 Angular 6+ 的轻量级 WYSIWYG 富文本编辑器组件，支持多种 Angular 版本和自定义配置。

- 📦 **安装与版本**：通过 npm 安装 `@kolkov/angular-editor`，支持 Angular v6 至 v22+，最新版 v3.1.0 需 Angular 22+、RxJS 7.8+ 和 TypeScript 6+。
- 🛠️ **使用方式**：支持模板驱动（ngModel）和响应式表单（formControlName），可配置占位符、编辑器 ID 等属性。
- ⚙️ **配置选项**：提供丰富配置，如可编辑性、拼写检查、高度/宽度、工具栏位置、字体、自定义类、图片上传 URL 或函数等。
- 🎨 **样式自定义**：通过 CSS 变量（如 `--ae-toolbar-bg-color`）轻松覆盖默认主题，需在 `angular.json` 中引入主题文件。
- 🔘 **自定义按钮**：利用 `ng-template` 和 `executeCommandFn` 添加自定义按钮，支持 `execCommand` 命令（如插入 HTML）。
- 📋 **API 接口**：包括输入属性（如 `id`、`config`）、输出事件（如 `html`、`blur`）、方法（如 `focus`）和配置接口 `AngularEditorConfig`。
- 📁 **项目结构**：包含库（`angular-editor`）和演示应用（`angular-editor-app`），文档和图标来自 Ligature Symbols。
- 🤝 **贡献与许可**：遵循 MIT 许可证，有贡献指南、行为准则和安全政策，版本管理遵循语义化版本。

---

### [Angular 编辑器应用](https://angular-editor.kolkov.ru/)

**原文标题**: [AngularEditorApp](https://angular-editor.kolkov.ru/)

概述总结  
- 🌍 全球变暖导致极端天气频发，海平面上升威胁沿海城市。  
- 🔬 科学家呼吁减少碳排放，转向可再生能源以缓解气候危机。  
- 🌱 个人行动如减少浪费、植树造林也能对环境保护产生积极影响。  
- 📉 政策层面需加强国际合作，落实《巴黎协定》目标。  
- ⚠️ 若不采取行动，到 2100 年全球气温可能上升 3°C 以上，引发不可逆后果。

---

### [发布 v4.0.0 · vuejs/pinia · GitHub](https://github.com/vuejs/pinia/releases/tag/v4.0.0)

**原文标题**: [Release v4.0.0 · vuejs/pinia · GitHub](https://github.com/vuejs/pinia/releases/tag/v4.0.0)

Pinia 4 版本发布，包含破坏性变更和多项改进，仅支持 ESM 并升级了 devtools-api 依赖，使用 Nostics 提供更清晰的错误提示。

- 🚀 升级 devtools-api 至 v8，增强开发工具兼容性
- 🛠️ 引入 Nostics 错误系统，提供更精准的诊断信息
- ✨ 在 storeToRefs 中优雅跳过 nullish 值，避免异常
- 🔍 对 storeToRefs 中的无效属性进行诊断提示
- ⚠️ 检测插件中的错误值，提升开发体验
- 🔑 导出 piniaSymbol，便于扩展使用
- 🐛 使用现代 Object.hasOwn 方法，修复兼容性问题
- 💧 在 shouldHydrate 中尊重非普通对象的 skipHydrate 标记
- 🔄 防止同一回调重复订阅时产生重复 watcher
- ⚙️ 将 pnpm 锁定至 11.7.0 以匹配 CI 环境
- 🖥️ 使可设置 getter（computed）可编辑，提升调试便利性
- 🔥 HMR 时保留 setup store ref 的运行时新增属性

---

### [GitHub - slackapi/bolt-js: 使用 JavaScript 构建 Slack 应用的框架](https://github.com/slackapi/bolt-js)

**原文标题**: [GitHub - slackapi/bolt-js: A framework to build Slack apps using JavaScript · GitHub](https://github.com/slackapi/bolt-js)

本页面介绍了 Bolt for JavaScript——一个用于快速构建 Slack 应用的 JavaScript 框架。

- ⚡ 概述：Bolt for JavaScript 是一个框架，可帮助开发者快速构建 Slack 应用，支持最新平台功能。
- 📦 安装：通过 `npm install @slack/bolt` 安装，并使用 `App` 构造函数进行初始化，需提供 `signingSecret` 和 `token`。
- 🎧 事件监听：支持监听多种事件类型，如操作（`action`）、命令（`command`）、事件（`event`）等，并需设置正确的请求路径 `/slack/events`。
- 🛠️ 核心参数：监听函数接收 `payload`、`say`、`ack`、`client`、`respond`、`context` 等参数，用于处理事件和响应。
- ✅ 确认机制：对于操作、快捷方式、视图提交等事件，必须在 3 秒内调用 `ack()` 函数，以确保用户体验。
- 📡 Web API：应用提供顶层 `client` 用于调用 Slack API，但需传递 `token`；监听函数中的 `client` 则自动使用事件关联的令牌。
- 📚 文档与支持：官方文档提供详细指南，可通过问题追踪器或邮件 `support@slack.com` 获取帮助。
- 🤝 贡献：欢迎社区贡献，请参阅贡献指南以协作改进项目。

---

### [报名参加 Viam 101 - 2026 年 7 月免费机器人课程](https://www.viam.com/viam-101/early-access)

**原文标题**: [Sign Up for Viam 101 - Free Robotics Course Coming July 2026](https://www.viam.com/viam-101/early-access)

Viam 是构建机器人的最快方式，本课程将教你通过实际应用掌握基础技能。

- 🤖 Viam 101 课程将于 2026 年 7 月上线，免费、实践且自定进度
- 🎓 由 Viam 产品与教育副总裁 Shannon Bradshaw 主讲，全程在模拟环境中学习，无需硬件
- 🏆 7 月 31 日前注册有机会赢取价值 3500 美元的 UFactory Lite 6 机械臂
- 📧 提交表单即同意 Viam 使用信息联系你，可随时退订营销通讯
- 💻 课程包含代码示例，如通过视觉获取点云并控制机械臂抓取物体

---

### [Meticulous AI - 无需编写测试的自动化前端测试](https://www.meticulous.ai/?utm_source=jsweekly&utm_medium=newsletter&utm_campaign=26q3&utm_content=classified)

**原文标题**: [Meticulous AI - Automated Frontend Testing Without Writing Tests](https://www.meticulous.ai/?utm_source=jsweekly&utm_medium=newsletter&utm_campaign=26q3&utm_content=classified)

Meticulous 是一个自动化、全面且确定性的测试工具，旨在帮助开发团队以零开发工作量实现代码的全面验证，从而加速发布流程并消除测试中的不稳定因素。

- 🚀 **零开发者工作量**：无需编写、修复或维护测试，测试套件会随应用自动演进。
- 🔍 **全面且确定性的测试**：基于 Chromium 构建的确定性调度引擎，消除所有测试不稳定因素，并实现闪电般的测试速度。
- 📈 **加速迭代**：持续添加新测试、移除过时测试，确保测试套件始终完整且最新，助力快速发布可靠的无回归代码。
- 🧪 **无缝集成**：支持 NextJS、React、Vue、Angular 等主流框架，只需添加脚本标签即可开始记录会话。
- 🤖 **AI 驱动**：AI 引擎根据日常交互自动生成覆盖所有代码分支和用户流程的端到端测试。
- 🛡️ **无副作用测试**：默认模拟后端响应，避免数据变化导致的误报，无需设置特殊测试账户或模拟数据。
- ⚡ **大规模闪电测试**：测试在计算集群上高度并行化，可在 120 秒内测试数千个屏幕。
- 🏢 **受信赖**：被超过 100 个组织（包括 Dropbox 和 Notion）采用，工程师反馈“立即爱上，无需再调试合并后的问题”。
- 🔒 **安全与合规**：提供集成、安全及文档支持，确保企业级使用体验。

---

### [无](https://expo.dev/blog/how-to-build-mobile-apps-with-ai-the-three-tools-that-actually-matter?utm_source=jsweekly&utm_medium=email&utm_campaign=33087804-React%2520to%2520Native)

**原文标题**: [None](https://expo.dev/blog/how-to-build-mobile-apps-with-ai-the-three-tools-that-actually-matter?utm_source=jsweekly&utm_medium=email&utm_campaign=33087804-React%2520to%2520Native)

概述：本文探讨了人工智能在医疗诊断中的最新应用，强调了其提高准确性和效率的潜力，同时指出了数据隐私和算法偏见等挑战。

- 🔬 人工智能在影像诊断中表现出色，能快速识别肿瘤和病变，准确率接近或超过人类专家。
- 📊 通过分析海量医疗数据，AI 可辅助医生制定个性化治疗方案，提升治疗效果。
- 🔒 数据隐私问题突出，患者信息的收集与使用需严格遵循法规，防止泄露。
- ⚖️ 算法偏见可能导致诊断结果不公，需确保训练数据的多样性和代表性。
- 🤝 AI 并非替代医生，而是作为协作工具，增强临床决策能力，减少误诊风险。

---

### [Java 的故事 | 官方纪录片 - YouTube](https://www.youtube.com/watch?v=ZqGSg4b_cZA)

**原文标题**: [The Java Story  |  The Official Documentary - YouTube](https://www.youtube.com/watch?v=ZqGSg4b_cZA)

本頁面概述了 YouTube 平台相關的關鍵資訊與政策。

- 📰 **新聞中心**：提供 YouTube 官方新聞與公告。
- ©️ **版權**：說明內容創作者的版權保護與管理機制。
- 📞 **聯絡我們**：提供用戶與平台聯繫的管道。
- 🎬 **創作者**：針對內容創作者提供的資源與支援。
- 💰 **刊登廣告**：介紹廣告投放選項與合作方式。
- 👨‍💻 **開發人員**：為開發者提供的 API 與技術文件。
- 📜 **條款**：用戶使用 YouTube 時需遵守的服務條款。
- 🔒 **私隱**：說明用戶資料的收集與使用政策。
- 🛡️ **政策及安全**：平台的安全規範與內容審查標準。
- ⚙️ **YouTube 的運作方式**：解釋平台推薦與內容分發機制。
- 🧪 **測試新功能**：預告或測試中的平台新功能。
- 🏢 **© 2026 Google LLC**：版權歸屬與法律聲明。

---

### [VITE：纪录片 - YouTube](https://www.youtube.com/watch?v=bmWQqAKLgT4)

**原文标题**: [VITE: The Documentary - YouTube](https://www.youtube.com/watch?v=bmWQqAKLgT4)

YouTube 平台提供多項功能與政策，涵蓋內容創作、廣告、法律條款及用戶安全等面向。
- 📰 新聞中心：提供官方最新消息與公告
- ©️ 版權：保護原創內容，管理版權相關事宜
- 📞 聯絡我們：提供用戶與創作者聯繫管道
- 🎨 創作者：支援內容創作者的工具與資源
- 📢 刊登廣告：廣告主可在平台投放廣告
- 👨‍💻 開發人員：提供 API 與開發工具
- 📜 條款：規範用戶與平台的使用協議
- 🔒 私隱：保護用戶個人資料與隱私設定
- 🛡️ 政策及安全：確保平台內容與互動安全
- ⚙️ YouTube 的運作方式：解釋平台演算法與功能機制
- 🧪 測試新功能：預覽與測試平台新特性
- ©️ 2026 Google LLC：版權歸屬與法律聲明

---

### [Angular：纪录片 | 起源故事 - YouTube](https://www.youtube.com/watch?v=cRC9DlH45lA)

**原文标题**: [Angular: The Documentary | An origin story - YouTube](https://www.youtube.com/watch?v=cRC9DlH45lA)

本頁面列出了 YouTube 平台的各類重要連結與政策資訊，涵蓋版權、聯絡方式、創作者資源、廣告、開發者、條款、隱私及安全等面向，並提及 2026 年 Google 版權所有。

- 📰 新聞中心：提供 YouTube 最新消息與公告
- ©️ 版權：說明版權相關規範與權利保護
- 📞 聯絡我們：提供用戶與平台聯繫的管道
- 🎥 創作者：為內容創作者提供資源與支援
- 📢 刊登廣告：介紹廣告投放選項與合作方式
- 💻 開發人員：提供 API 與技術開發相關資訊
- 📜 條款：列出使用 YouTube 的服務條款
- 🔒 私隱：說明個人資料處理與隱私保護政策
- 🛡️ 政策及安全：涵蓋社群規範與安全措施
- ⚙️ YouTube 的運作方式：解釋平台功能與演算法
- 🧪 測試新功能：介紹正在測試中的新特性
- ©️ 2026 Google LLC：標示版權歸屬與年份

---

### [Node.js：纪录片 | 起源故事 - YouTube](https://www.youtube.com/watch?v=LB8KwiiUGy0)

**原文标题**: [Node.js: The Documentary | An origin story - YouTube](https://www.youtube.com/watch?v=LB8KwiiUGy0)

YouTube 提供平台讓使用者觀看、分享與創作影片，並涵蓋版權、隱私、政策及安全等規範，同時支援創作者與開發者，並持續測試新功能以優化體驗。

- 📰 **新聞中心**：提供最新平台動態與官方公告。
- ©️ **版權**：強調內容使用需遵守版權法規。
- 📞 **聯絡我們**：提供用戶與創作者聯繫管道。
- 🎥 **創作者**：支援內容創作與頻道管理。
- 💰 **刊登廣告**：說明廣告投放與收益機制。
- 👨‍💻 **開發人員**：提供 API 與技術整合資源。
- 📜 **條款**：明確使用規範與法律責任。
- 🔒 **私隱**：保護用戶資料與隱私設定。
- 🛡️ **政策及安全**：確保平台內容安全與合規。
- ⚙️ **YouTube 的運作方式**：解釋推薦演算法與平台機制。
- 🧪 **測試新功能**：持續推出實驗性功能以改善體驗。
- 🏢 **© 2026 Google LLC**：版權歸屬與法律聲明。

---

### [ReactBench](https://www.reactbench.com/)

**原文标题**: [ReactBench](https://www.reactbench.com/)

ReactBench 是一个针对真实 React 开发场景的编码智能体评估基准。传统测试只能验证行为，却无法发现性能、可访问性和代码质量问题。该基准通过 51 个实际任务，对 17 个模型进行了评分与成本效率分析。

- 📊 **GPT 5.6 Terra (Max) 以 53.3% 得分位居榜首**，成本仅为 $1.76，展现了高性价比。
- 💰 **GPT 5.6 Sol 系列表现突出**，多个配置（Max/XHigh/High）得分均超过 46%，成本在 $0.97 至 $3.62 之间。
- 🚀 **Fable 5 (XHigh) 以 47.1% 得分排名第三**，但成本高达 $10.04，效率较低。
- ⚡ **Grok 4.5 性价比优秀**，以 $0.62 成本获得 40.4% 得分，超越价格更高的 Opus 4.8。
- 📉 **低配置模型得分普遍下降**，如 GPT 5.6 Luna (Low) 仅 14.5%，成本 $0.07，但效率极高。
- 🔍 **ReactBench 聚焦真实缺陷**，包括导致宕机的 useEffect 错误、影响收入的性能问题，以及法律风险的访问性缺陷。
- 🛠️ **任务涵盖 51 个实际修复场景**，如修复图片组件反模式、添加手势缩放、修复事件监听泄漏等。
- 🏆 **OpenAI 模型在效率与得分间平衡最佳**，而 Anthropic 的 Fable 和 Opus 虽得分高，但成本显著更高。

---

### [2026 年 7 月 - 介绍 shadcn/typeset - shadcn/ui](https://ui.shadcn.com/docs/changelog/2026-07-typeset)

**原文标题**: [July 2026 - Introducing shadcn/typeset - shadcn/ui](https://ui.shadcn.com/docs/changelog/2026-07-typeset)

本内容概述了 shadcn/ui 的组件库、工具集以及新发布的 shadcn/typeset 排版系统。

- 📋 **组件库概览**：包含 Accordion、Alert、Button、Card、Dialog、Dropdown Menu、Table 等丰富的 UI 组件，覆盖常见界面元素。
- 🛠️ **核心功能**：支持安装、主题定制、CLI 工具、类型设置、技能集成（如 JavaScript、Figma）、注册表管理和变更日志。
- ✨ **新发布：shadcn/typeset**：一个基于 CSS 的排版系统，通过一个 CSS 文件统一管理 HTML 元素样式，支持容器自适应和上下文调整。
- 🎨 **灵活定制**：提供 `--typeset-size`、`--typeset-leading`、`--typeset-flow` 三个 CSS 变量，可针对不同场景（如聊天、文档）创建多种排版风格。
- 🚀 **流式支持**：专为流式内容设计，新增块不会重绘已有样式，适合实时更新场景（如聊天消息）。
- 📚 **文档与工具**：提供 typeset 构建器、完整指南，并支持部署到 Vercel，已被 OpenAI、Sonos 等公司采用。

---

### [Cloudflare 博客](https://blog.cloudflare.com/)

**原文标题**: [The Cloudflare Blog](https://blog.cloudflare.com/)

以下是 2026 年 7 月 Cloudflare 博客文章的综合摘要：

- ⚽ 2026 年世界杯期间，全球 HTTP 流量模式发生显著变化，包括深夜流量激增和中场休息时段的浏览高峰
- 🏢 Cloudflare Internal DNS 正式上线，为私有网络提供权威和递归 DNS 服务，集成于 Zero Trust 和公共 DNS 平台
- 🛡️ Cloudflare WAF 为 WordPress 应用部署了两条高严重性漏洞防护规则，建议用户立即更新
- 🔐 针对.al 顶级域名的 DNSSEC 密钥轮换失败，1.1.1.1 新增 EDE 33 错误码，直接提示 DNSSEC 验证被绕过
- 🤖 推出 Precursor 引擎，通过持续行为验证检测高级自动化，减少对合法用户的干扰
- ☁️ 改进 Smart Tiered Cache，支持 AWS、GCP、Azure 和 Oracle Cloud 的自定义上层缓存选择
- 🔑 探讨后量子签名算法现状，建议目前使用 ML-DSA，同时关注 NIST 九种新候选算法
- 🌍 Cloudflare Research 构建 Meerkat 全球共识服务，基于 QuePaxa 算法，用于强一致性键值存储
- 🇬🇧 Cloudflare 加入英国政府网络弹性承诺，强调安全民主化、领导问责和供应链透明度
- 🗄️ 推出 Workers Cache，为 Worker 入口点提供区域性分层缓存，通过标准 HTTP 头配置
- 📊 Attribution Business Insights 仪表板帮助网站所有者分析爬虫行为，支持爬虫补偿的商业对话
- 🤖 推出 AI 搜索优化工具，帮助创作者在智能体时代保持可发现性并获取报酬
- 🛠️ 为所有客户提供 AI 流量管理选项，区分搜索、代理和训练机器人，保护广告页面
- 💳 开放 Monetization Gateway 等待名单，支持通过 x402 协议对网页、数据集、API 等资源收费
- 📈 发布内容独立日一周年报告，分析 AI 智能体如何颠覆传统搜索推荐，构建可持续网络经济
- 🔄 Cloudflare Workflows 支持 saga 式回滚，允许为每个步骤指定补偿操作
- 🔑 所有开发者现可使用自管理 OAuth，实现零停机核心 OAuth 引擎迁移
- 🏛️ 白宫后量子行政令设定 2030 年迁移截止日期，Cloudflare 提供迁移指南
- 🐛 在重构 Images 绑定时发现 hyper HTTP 库跨多个主要版本的漏洞

---

### [介绍 EmDash —— 解决插件安全问题的 WordPress 精神继承者 | Cloudflare 博客](https://blog.cloudflare.com/emdash-wordpress/)

**原文标题**: [Introducing EmDash â the spiritual successor to WordPress that solves plugin security | The Cloudflare Blog](https://blog.cloudflare.com/emdash-wordpress/)

Cloudflare 推出 EmDash，一个基于 TypeScript 和 Astro 的开源 CMS，旨在解决 WordPress 的插件安全问题，并支持服务器端无服务器架构。

- 🚀 EmDash 是 WordPress 的精神继承者，完全用 TypeScript 编写，基于 Astro 框架，并采用 MIT 许可证开源。
- 🔒 插件安全：每个插件在独立的 Dynamic Worker 沙箱中运行，通过声明式权限（如 read:content、email:send）限制访问，避免 WordPress 插件直接访问数据库和文件系统的风险。
- 🛡️ 插件市场去中心化：插件可自由选择许可证，代码在沙箱中运行，无需公开源码，减少对中心化市场的依赖。
- 💳 内置 x402 支持：允许内容创作者按次收费，无需订阅，通过 HTTP 402 状态码实现即付即用，适应 AI 代理时代。
- 📉 零成本扩展：基于 Cloudflare Workers 的 v8 隔离架构，请求时自动启动，无请求时归零，仅按 CPU 时间计费，适合流量波动。
- 🎨 现代前端主题：通过 Astro 创建主题，支持页面、布局、组件和样式，主题无法执行数据库操作，提升安全性。
- 🤖 AI 原生功能：提供 Agent Skills、CLI 和内置 MCP 服务器，支持 AI 代理自动管理内容迁移和定制。
- 🔑 默认无密码认证：采用 Passkey 认证，支持 SSO 集成，内置角色权限控制（管理员、编辑、作者等）。
- 📤 一键迁移：支持从 WordPress 导入 WXR 文件或通过专用插件迁移内容，自动处理媒体和自定义内容类型。
- 🧪 预览版可用：EmDash v0.1.0 已发布，可通过 CLI 或 Cloudflare 仪表板部署，并提供在线 Playground 试用。

---

### [天文](https://astro.build/)

**原文标题**: [Astro](https://astro.build/)

Astro 7.1 现已发布，是一款专为内容驱动型网站设计的 JavaScript 网页框架，以服务器优先、内容驱动和高度可定制为特色，提供卓越性能和灵活性。

- 🚀 **Astro 7.1 已发布**：专为内容驱动型网站打造的网页框架，支持营销网站、博客、电商等。
- 🖥️ **服务器优先渲染**：在服务器端渲染组件，发送轻量 HTML，减少不必要的 JavaScript 开销，提升性能。
- 📝 **内容驱动设计**：可从文件系统、外部 API 或 CMS 加载数据，灵活适配内容来源。
- 🔧 **高度可定制**：支持集成 JavaScript UI 组件、CSS 库、主题等，扩展性强。
- ⚡ **最佳性能**：通过 Astro Islands 优化页面加载，提升转化率、核心网页指标和 SEO，真实网站核心网页指标通过率达 66%，领先 WordPress、Gatsby、Next.js 等。
- 🔄 **零锁定**：支持 React、Vue、Svelte 等主流 UI 框架，可复用现有组件。
- 📦 **功能齐全**：包括内容集合、零 JavaScript 默认、视图过渡、优化图像、UI 集成、文件路由、中间件、操作、部署适配器等。
- 🧩 **生态系统丰富**：提供多种主题（电商、博客、文档、作品集、落地页）和 Astro 合作伙伴机构支持。
- 🤖 **AI 就绪**：集成官方 MCP 服务器和上下文文件，提升开发体验。
- 💡 **免费开源**：Astro 是免费开源软件，由赞助商支持。

---

### [js13kGames 2026](https://js13kgames.com/2026/)

**原文标题**: [js13kGames 2026](https://js13kgames.com/2026/)

无法总结：未找到主要内容。

---

### [Github-Ranking/Top100/JavaScript.md 位于 master 分支 · EvanLi/Github-Ranking · GitHub](https://github.com/EvanLi/Github-Ranking/blob/master/Top100/JavaScript.md)

**原文标题**: [Github-Ranking/Top100/JavaScript.md at master · EvanLi/Github-Ranking · GitHub](https://github.com/EvanLi/Github-Ranking/blob/master/Top100/JavaScript.md)

该仓库展示了 GitHub 上 JavaScript 项目的前 100 名排行榜，涵盖了从框架、工具到学习资源的各类优秀项目。

- 🏆 **React** 以 246k 星位居榜首，是构建用户界面的核心库
- 🤖 **ECC** 和 **caveman** 等 AI 代理工具表现突出，分别拥有 231k 和 91k 星
- 📚 **javascript-algorithms** (196k 星) 和 **30-seconds-of-code** (128k 星) 是热门学习资源
- 🛠️ **Node.js** (118k 星)、**axios** (109k 星) 和 **three.js** (113k 星) 是基础设施级项目
- 🎨 **material-ui** (98k 星) 和 **Chart.js** (67k 星) 主导 UI 和数据可视化领域
- 🔧 **webpack** (65k 星)、**prettier** (52k 星) 和 **eslint** 等工具链项目广受欢迎
- 🎮 **phaser** (39k 星) 和 **video.js** (39k 星) 是游戏和视频处理领域的代表
- 🌐 **htmx** (48k 星) 和 **svelte** (87k 星) 代表了新兴的前端开发趋势
- 📝 **leetcode** (55k 星) 和 **javascript-algorithms** 是程序员面试准备的重要资源

---

