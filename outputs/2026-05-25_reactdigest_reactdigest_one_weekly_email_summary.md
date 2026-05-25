### [React 文摘：电子邮件通讯](https://reactdigest.net/)

**原文标题**: [React Digest: Email Newsletter](https://reactdigest.net/)

这是一份为 React 开发者精心策划的每周通讯，已有超过 22,522 名前端工程师订阅，旨在通过精选文章和简短摘要帮助读者节省时间并每周学到新知识。

- 📬 每周一封邮件，精选 React 相关文章与摘要
- ⏱️ 帮助开发者节省筛选内容的时间
- 🧠 每周都能学到新东西，保持知识更新
- 👍 读者反馈积极，尤其称赞关于 React 并发模式的文章
- 👥 订阅者包括众多前端工程师，覆盖广泛

---

### [我对 AI 的思考，第二部分：智能体设置、工作流程与工具 · Mark 的开发博客](https://blog.isquaredsoftware.com/2026/05/ai-thoughts-part-2-agent-workflow-tools/)

**原文标题**: [
     My Thoughts on AI, Part 2: Agent Setup, Workflow, and Tools ·  Mark's Dev Blog
  ](https://blog.isquaredsoftware.com/2026/05/ai-thoughts-part-2-agent-workflow-tools/)

### 概述总结
作者分享了个人 AI 开发代理的设置、工作流程和工具配置，强调以人为中心的控制、确定性和脚本化自动化，同时平衡效率与理解。

- 🤖 **代理选择**：使用 OpenCode 作为代理，并通过 CodeNomad Web UI 进行交互，避免 TUI 的局限性，支持多标签和复制粘贴。
- 🧠 **模型偏好**：主要使用 Anthropic 的 Opus 4.5/4.6模型，通过API调用，避免频繁切换模型以追求微小性能提升。
- 🛠️ **开发工具**：VS Code 主要用于文件查看和差异对比，Fork 作为 Git GUI 客户端，但工作流主要在 CodeNomad 中完成。
- 🔄 **工作流核心**：采用“父编排器 + 子任务”模式，父会话管理整体上下文，子任务进行具体开发，强调人为控制所有决策和代码审查。
- 📁 **上下文管理**：使用 grepika 和 tilth 进行代码结构搜索，cachebro 缓存文件读取，以及 OpenCode 动态上下文修剪插件，有效控制会话上下文大小。
- 📝 **文档管理**：建立独立的 dev-plans 仓库存储个人开发文档，通过 devplans.ts 脚本自动化进度更新、子任务交接和文件管理。
- ⚙️ **权限控制**：通过自定义插件实现确定性命令审批，自动批准安全命令并阻止危险操作，避免不必要的权限提示。
- 🚀 **未来改进**：计划增强长期记忆和上下文索引能力，自动扫描会话提取模式和改进建议，并改进代码审查工具 diffloupe。

---

### [Meticulous AI - 无需编写测试的自动化前端测试](https://www.meticulous.ai/?utm_source=react-digest&utm_medium=newsletter&utm_campaign=26q1&utm_content=primary)

**原文标题**: [Meticulous AI - Automated Frontend Testing Without Writing Tests](https://www.meticulous.ai/?utm_source=react-digest&utm_medium=newsletter&utm_campaign=26q1&utm_content=primary)

Meticulous 是一款无需开发者编写代码即可自动生成全面、确定性测试的测试工具，帮助团队在复杂代码库中快速交付可靠代码。

- 🧪 **零开发者投入的全面验证**：自动生成覆盖所有代码路径和用户流程的端到端测试，无需手动编写、修复或维护测试用例。
- 🤖 **AI 驱动测试套件持续进化**：通过记录开发环境中的交互，AI 引擎自动生成并更新测试套件，确保测试始终与代码变化同步。
- ⚡ **闪电般快速测试**：测试在计算集群上高度并行化，可在 120 秒内完成数千个屏幕的测试，且从 Chromium 层面消除所有不稳定测试。
- 🔒 **确定性测试，无假阳性**：默认模拟后端响应，通过保存和重放原始记录，避免因数据变化导致的误报，无需特殊测试账户或模拟数据。
- 🚀 **加速迭代与合并**：在拉取请求合并前即可预览对用户工作流的影响，大幅提升交付速度，同时确保回归代码的可靠性。
- 🛠️ **与现有工具无缝集成**：支持 NextJS、React、Vue、Angular 等主流框架，可补充或替代现有测试套件，且提供安全文档和 CI 集成。
- 💬 **行业验证与用户好评**：被 Dropbox、Notion 等 100 多家组织采用，工程师称赞其“无需调试合并后问题、零维护、无不稳定测试”。

---

### [从延迟到即时：现代化 GitHub Issues 导航性能 - GitHub 博客](https://github.blog/engineering/architecture-optimization/from-latency-to-instant-modernizing-github-issues-navigation-performance/)

**原文标题**: [From latency to instant: Modernizing GitHub Issues navigation performance - The GitHub Blog](https://github.blog/engineering/architecture-optimization/from-latency-to-instant-modernizing-github-issues-navigation-performance/)

GitHub Issues 团队通过客户端缓存、智能预取和服务工作者，将导航延迟从秒级降至即时响应，显著提升了用户体验。

- 🚀 **核心目标**：将导航感知延迟降至“即时”水平，通过本地优先架构实现从本地数据即时渲染，后台再异步验证更新。
- 📊 **性能指标**：采用 HPC（最高优先级内容）指标，将导航分为即时（<200ms）、快速（<1000ms）和慢速（>=1000ms）三类，并优化整体分布而非仅关注尾部。
- 💾 **客户端缓存**：使用 IndexedDB 实现持久化客户端缓存，结合 Stale-While-Revalidate 策略，使约 22% 的 React 导航变为即时，缓存命中率约 33%。
- 🔥 **预加热策略**：通过低优先级预取高意图页面（如问题列表），仅补充缺失缓存，避免过度请求，将缓存命中率提升至约 96%，React 导航即时率增至 70%。
- ⚙️ **服务工作者**：拦截硬导航请求，利用缓存数据跳过服务器渲染，仅返回 HTML 骨架，显著加速 Turbo 导航，并优化硬导航的 JavaScript 加载。
- 📈 **实际效果**：HPC 指标全面改善：P10 从 600ms 降至 70ms，P25 从 800ms 降至 120ms，P50 从 1200ms 降至 700ms，P75 和 P90 也分别下降 400ms 和 300ms。
- 🔮 **未来方向**：继续优化冷启动场景，计划重写后端堆栈以支持低延迟交付，并投资边缘计算层，目标是让“快速”成为所有导航路径的默认体验。

---

### [React 应用中的安全性 - Certificates.dev](https://certificates.dev/blog/security-in-react-applications)

**原文标题**: [Security in React Applications - Certificates.dev](https://certificates.dev/blog/security-in-react-applications)

本次在线活动聚焦于 Web 开发与 AI，涵盖安全、认证及防御策略，旨在提升 React 应用的安全性。

- 🗓️ **活动概况**：为期两天（6 月 3-4 日）的免费在线活动，包含演讲、现场讨论和研讨会，主题为 Web 开发与 AI。
- 🛡️ **React 内置 XSS 防护**：React 通过 JSX 自动转义特殊字符（如`<`、`>`），防止恶意脚本执行，但需注意`dangerouslySetInnerHTML`会绕过此保护。
- 🧹 **使用 DOMPurify 清理 HTML**：当必须渲染原始 HTML 时，应使用 DOMPurify 库清理，以移除危险标签和属性，避免 XSS 攻击。
- 🔐 **安全认证与 CSRF 防护**：避免将令牌存储在`localStorage`或`sessionStorage`中，改用`HttpOnly`、`Secure`和`SameSite=Strict`属性的 Cookie，并添加 CSRF 令牌防止跨站请求伪造。
- ✅ **服务器端输入验证**：使用 Zod 进行类型安全的模式验证，确保服务器端验证用户输入，并结合参数化查询防止 SQL 注入。
- 🚧 **内容安全策略（CSP）**：通过 HTTP 头配置 CSP，限制资源加载来源，并使用 nonce 允许内联脚本，同时利用`Content-Security-Policy-Report-Only`测试策略。
- 📚 **其他相关文章**：网站还提供自定义 React Hooks、Nuxt 状态管理、Laravel Eloquent 等主题的实用指南，并支持开发者认证和招聘服务。

---

### [动画容器边界](https://www.userinterface.wiki/animating-container-bounds)

**原文标题**: [Animating Container Bounds](https://www.userinterface.wiki/animating-container-bounds)

本文介绍了如何利用 Motion 和 ResizeObserver 实现容器宽高的平滑动画，解决直接改变容器尺寸时出现的跳跃问题。

- 📏 **核心问题**：浏览器无法直接动画化 `width` 和 `height` 属性，导致容器尺寸变化时瞬间跳跃。
- 🛠️ **解决方案**：使用 `useMeasure` 钩子（基于 `ResizeObserver`）实时测量内部内容尺寸，并将其传递给 Motion 的 `animate` 属性。
- 🎯 **实现技巧**：将 `ref` 绑定到内部包装元素（测量用），`animate` 应用于外部容器（动画用），避免循环更新。
- ⚡ **宽度动画**：适用于按钮标签变化等场景，通过测量内部宽度并动画化外部容器实现平滑过渡。
- 📐 **高度动画**：适用于可展开/折叠区域（如 FAQ、手风琴），通过测量内部高度并动画化外部容器实现流畅展开效果。
- ⚠️ **注意事项**：初始渲染时需检查 `bounds.height > 0` 避免从 0 开始动画；不要在同一元素上同时测量和动画；可添加微小延迟提升自然感；避免过度使用此模式。

---

### [React.Activity 的隐性成本 | Peter Piekarczyk](https://www.peterp.me/articles/hidden-cost-of-react-activity/)

**原文标题**: [The hidden cost of React.Activity | Peter Piekarczyk](https://www.peterp.me/articles/hidden-cost-of-react-activity/)

### 概述总结
React.Activity 在隐藏子树时保留状态但销毁副作用，重新显示时重建所有副作用，这可能导致性能开销被转移到用户交互路径上。

- 🎭 **核心机制**：Activity 隐藏时保留状态但销毁 Effects，显示时恢复状态并重新创建 Effects，并非简单的“保持挂载但不可见”
- ⚠️ **副作用重建成本**：隐藏子树重新显示时，所有订阅、观察者、测量逻辑和效果驱动的 setState 都会重新触发，导致渲染风暴
- 📱 **React Native 特有风险**：移动端代码天然包含大量 Effect（应用状态、键盘事件、布局变化等），嵌套组件库会加剧此问题
- 🔄 **setState 乘数效应**：Effect 中同步调用 setState 会触发额外渲染，密集屏幕中多个组件同时执行此模式会显著增加开销
- 🧩 **生态库影响**：TanStack Query、Jotai 等库依赖 Effect 进行订阅管理，Activity 隐藏/显示会触发大量重新订阅
- 🏗️ **密集屏幕问题**：设置页、结账流程等包含大量嵌套设计系统组件的屏幕，Activity 会将工作从初始加载转移到用户返回时刻
- ✅ **适用场景**：适合表单、小型详情面板等子树小、Effect 轻量的内容
- ⚡ **需谨慎场景**：避免用于包含大量嵌套组件、重复订阅、Effect 驱动状态的复杂屏幕
- 🔍 **实践建议**：使用 Activity 前审计子树，检查 Effect 中立即 setState、挂载逻辑、重复订阅和昂贵钩子
- 💡 **核心洞察**：Activity 保留状态，但真正考验的是 Effect 的整洁度——重新显示时 Effect 重建成本可能比预期高得多

---

### [smoores.dev - ProseMirror 模型在富文本转换中的非凡效果](https://smoores.dev/post/unreasonable_effectiveness_of_prosemirror/)

**原文标题**: [smoores.dev - The Unreasonable Effectiveness of ProseMirror Model in Rich Text Transformation](https://smoores.dev/post/unreasonable_effectiveness_of_prosemirror/)

### 概述总结
本文介绍了如何利用 ProseMirror 的数据模型高效解决电子书与有声书文本对齐问题，通过解析、转换和序列化步骤，实现句子级别的精确标记。

- 📚 **核心问题**：EPUB 文件仅支持元素级别的音频同步，无法实现句子或单词级对齐，需修改 XHTML 标记来包裹每个句子。
- 🔧 **ProseMirror 模型优势**：采用扁平化文本节点结构（无嵌套），通过位置（positions）和映射（mappings）轻松跟踪文档变更，适合处理复杂内联标记。
- 🧩 **三步解决方案**：
  - **解析**：将 DOM 转换为 ProseMirror 数据模型，内联标记（如`<em>`）作为文本节点的属性（marks）。
  - **转换**：通过`liftText`提取纯文本，分割句子后利用反向映射在原文档中添加句子标记（`<span id="sentenceN">`）。
  - **序列化**：按首标记分组相邻文本节点，递归生成 XHTML，保证标记连续性和可预测性。
- ✨ **优雅实现**：代码简洁（约 20 行核心逻辑），利用 ProseMirror 的`descendants`迭代器和`addMark`函数，无需复杂 DOM 操作。
- ⚠️ **权衡**：序列化不追求最优连续性，但保证可预测性；可能破坏依赖特定标记结构的 CSS，但在实际测试中有效。
- 🎯 **最终效果**：生成每个句子包裹唯一`<span>`的 XHTML，支持句子级音频同步，且保留原有内联标记（如强调）。

---

### [Google I/O 2026 的 15 项更新：借助 Chrome 的新功能、工具和特性赋能代理网络 | 博客 | Chrome 开发者](https://developer.chrome.com/blog/chrome-at-io26)

**原文标题**: [15 updates from Google I﻿/﻿O 2026: Powering the agentic web with new capabilities, tools, and features in Chrome  |  Blog  |  Chrome for Developers](https://developer.chrome.com/blog/chrome-at-io26)

Google I/O 2026 发布了 15 项 Chrome 更新，聚焦于赋能 AI 代理、提升 Web UI 和性能，以及通过 Gemini 增强浏览体验，推动代理化网络的发展。

- 🚀 **WebMCP 标准**：提出开放标准，允许网站向浏览器代理暴露结构化工具（如 JS 函数），实现更可靠、精准的复杂任务自动化，Chrome 149 开始试验。
- 📘 **现代 Web 指南**：提供专家验证的编码技能集，指导 AI 代理构建现代、安全、可访问的 Web 体验，支持 100+ 用例，一键安装。
- 🔧 **Chrome DevTools 代理**：让 AI 代理直接访问 DevTools 功能（控制台、网络、可访问性树），实现自动调试和优化，LY 公司减少 96-98% 手动分析。
- 🤖 **AI 辅助调试**：DevTools 集成 Lighthouse 数据和 Gemini 推理，支持开放式问题，简化性能调试流程。
- 🧠 **内置 AI 功能**：浏览器端运行 AI 模型（如 Gemini Nano、Gemma 197M），无需服务器成本，支持摘要、翻译等，Trip.com 用于生成个性化旅行摘要。
- 🖼️ **HTML-in-Canvas API**：将真实 DOM 元素集成到 Canvas 中，实现沉浸式 3D 体验，结合元素级视图过渡，提升 UI 逼真度。
- ⚡ **性能与 UI 更新**：Soft Navigations API 支持 SPA 的 Core Web Vitals 测量，Declarative Partial Updates 简化 HTML 更新。
- 🔐 **即时 UI 模式**：统一密码和通行密钥的登录流程，自动显示可用凭据，简化身份验证。
- 📊 **Baseline Checker 工具**：连接 Google Analytics，实时查看用户对现代功能的支持率，帮助选择 Baseline 目标。
- 📱 **Android 版 Gemini**：6 月推出，作为个人浏览助手，可总结文章、回答问题，并连接 Google 应用（日历、Keep、Gmail）完成任务。
- 🤖 **自动浏览功能**：在 Android 上自动化繁琐任务（如订停车位），桌面版将集成 Gemini Spark。
- 🎨 **Nano Banana 图像处理**：在 Android 上即时创建或编辑图像，如生成信息图或修改图片元素。
- 🛠️ **Chrome 技能**：在桌面版保存和复用 AI 提示，一键执行多标签工作流（如比较商品、扫描文档）。
- 🖱️ **屏幕选择交互**：用鼠标选择网页内容后直接提问 Gemini，无需描述，支持图像编辑。
- 🎤 **语音输入**：在桌面版用语音填写表单、写邮件，Gemini 模型可清理转录内容（去除语气词）。

---

### [跨实时重载保留 DOM 更改 | Kitty Giraudel](https://kittygiraudel.com/2026/05/01/preserving-dom-changes-across-live-reloads/)

**原文标题**: [Preserving DOM Changes Across Live Reloads | Kitty Giraudel](https://kittygiraudel.com/2026/05/01/preserving-dom-changes-across-live-reloads/)

以下是根据您提供的文章内容生成的摘要：

概述摘要  
- 🔍 发现一个问题：在 Eleventy 的 watch 模式下保存文件时，客户端 JavaScript 应用的 DOM 操作（如 data-theme 属性）会被 morphdom 的 DOM diffing 清除。  
- 🎨 主题切换器通过 JavaScript 在 <html> 元素上设置 data-theme 属性，并依赖 localStorage 和 OS 偏好。  
- 🔄 实时重载机制：服务器通过 WebSocket 通知客户端，Eleventy 使用 morphdom 进行精细 DOM 更新，仅在全失败时执行页面刷新。  
- ⚠️ 问题根源：文件本身没有 data-theme 属性，morphdom 比较新旧 DOM 后移除该属性，导致主题状态丢失。  
- ✅ 解决方案：插入一个 MutationObserver 监听 data-theme 属性变化，若被移除则重新应用主题，并仅在开发环境启用。  
- ❌ 尝试的通用方案失败：通过重新触发 DOMContentLoaded 事件来“重新挂载”页面，但会导致重复事件监听器和其他副作用。  
- 💡 最终修复简单有效（约 10 行代码），但问题本质适用于任何客户端 DOM 变更场景。

---

### [告别 Tailwind，学习组织我的 CSS](https://jvns.ca/blog/2026/05/15/moving-away-from-tailwind--and-learning-to-structure-my-css-/)

**原文标题**: [Moving away from Tailwind, and learning to structure my CSS](https://jvns.ca/blog/2026/05/15/moving-away-from-tailwind--and-learning-to-structure-my-css-/)

概述总结
- 🎨 作者从 Tailwind 迁移到语义化 HTML+ 原生 CSS，发现 Tailwind 教会了他很多 CSS 系统化方法
- 📐 直接复制了 Tailwind 的"preflight"重置样式，包括 box-sizing 和 line-height 等基础设置
- 🧩 采用组件化 CSS 架构：每个组件有独立 class 和文件，避免样式冲突，使用嵌套选择器组织代码
- 🎨 颜色系统：将所有颜色定义为 CSS 变量，统一管理在 colors.css 文件中
- 🔤 字体大小：参考 Tailwind 定义变量体系（--size-xs 到--size-2xl），方便快速调整字号
- 🛠 工具类：保留.sr-only 等实用类，但严格控制数量避免滥用
- 📏 基础样式：仅设置 section 居中布局和链接颜色，采用自下而上逐步扩展的策略
- 📐 间距管理：通过外层布局组件控制间距，使用相邻兄弟选择器（*+*）实现均匀分布
- 📱 响应式设计：改用 CSS Grid 的 auto-fit 和 minmax() 实现自适应布局，减少媒体查询依赖
- ⚙️ 构建系统：开发时直接使用 CSS @import 和嵌套语法，生产环境用 esbuild 打包
- 🚫 迁移原因：Tailwind 依赖构建系统、文件体积大、限制创意、混合使用维护困难
- 💡 学习收获：通过 CSS 新特性（@layer、@scope、容器查询等）提升了对 CSS 的尊重和理解
- ❤️ 核心感悟：CSS 本身是解决复杂问题的强大工具，不应被框架贬低其价值

---

### [你不了解 HTML 列表——弗兰克·M·泰勒](https://blog.frankmtaylor.com/2026/05/13/you-dont-know-html-lists/)

**原文标题**: [You don’t know HTML Lists – Frank M Taylor](https://blog.frankmtaylor.com/2026/05/13/you-dont-know-html-lists/)

本文深入探讨了 HTML 中五种列表类型及其正确用法，强调语义化选择而非视觉呈现，并提供了丰富的实践技巧和代码示例。

- 📋 **五种列表类型**：HTML 包含有序列表（`<ol>`）、无序列表（`<ul>`）、描述列表（`<dl>`）、菜单列表（`<menu>`）和控制列表（`<select>`/`<datalist>`），每种都有特定用途。
- 🎯 **选择依据**：若顺序改变影响含义用`<ol>`；键值对用`<dl>`；界面操作控件用`<menu>`；用户输入控制用`<select>`或`<datalist>`；其余用`<ul>`。
- 🔧 **控制列表进阶**：`<select>`支持`multiple`、`optgroup`分组和`disabled`属性；`<datalist>`可配合任何`<input>`类型（如 week、range），但需注意`value`与标签的差异。
- 🔄 **有序列表特性**：`reversed`属性可倒序编号但不改变 DOM 顺序；`start`属性可设定起始值；嵌套列表能清晰表达复杂流程（如食谱）。
- 📝 **描述列表新用**：HTML5 扩展了`<dl>`用途，支持`<div>`分组；适用于元数据展示、JSON 调试等键值对场景，可配合 Flexbox 实现灵活布局。
- 🖥️ **菜单列表定位**：`<menu>`专用于工具栏或命令集合（如视频控件），与`<nav>`不同（`<nav>`是区块元素可含多种内容，`<menu>`仅含`<li>`）。
- 🚫 **语义化误区**：避免仅凭视觉（如数字/圆点）选择列表类型；`<ul>`是“万能抽屉”，但应优先考虑更语义化的列表。
- 💡 **实用技巧**：`<datalist>`可配合`<input type="range">`创建带标签的滑块；`<select>`中可插入`<hr>`实现视觉分隔；`<li>`的结束标签可省略（但作者建议保留）。

---

### [React 项目实战 — 坦纳·林斯利](https://tannerlinsley.com/posts/projecting-react)

**原文标题**: [Projecting React â Tanner Linsley](https://tannerlinsley.com/posts/projecting-react)

### 概述总结
Tanner Linsley 通过 AI 辅助构建了 React 的轻量级投影版本 `@tanstack/redact`，将 React 运行时从约 60KB 压缩至 7-9KB，并在两个生产站点验证了其性能提升与功能兼容性，同时探讨了代码投影化对前端生态的深远影响。

- 🚀 **核心动机**：React 运行时体积过大（~60KB gzip），而 TanStack 工具链中其他库体积总和更小，促使作者探索更轻量的替代方案。
- ⚡ **Preact 兼容性失败**：`preact/compat` 与 React 19 的 `use()`、服务端操作、Portal 等特性存在大量兼容问题，修复成本过高。
- 💡 **代码即投影**：借鉴 Kyle Mathews 的观点，将代码视为思想的“物化视图”，React 的公共 API 是基础表，而 `@tanstack/redact` 是专为 TanStack Start 优化的投影。
- 🛠️ **AI 辅助构建**：使用 AI 代理在一天内完成核心投影开发，后续通过生产环境流量发现并修复了 6 个真实 React 错误模式（如协调顺序、Effect 清理时机）。
- 📦 **体积与性能**：`full` 预设 9.39KB，`nano` 预设 7.08KB（相比 React 减小 80-85%）；客户端导航速度提升 2.24 倍，SSR 吞吐量提升约 3 倍。
- 🔧 **模块化特性开关**：8 个可切换特性（Portal、Context、Suspense 等），通过 Vite 插件在构建时完全移除未用代码，无运行时分支。
- 🌐 **生产验证**：tannerlinsley.com 和 tanstack.com 已运行于该投影，FCP 降低 18%，LCP 降低 12%，总 JS 传输量减少 33%（个人博客）或近 1MB（完整应用）。
- ⚠️ **已知回归**：RSC 密集型页面 LCP 增加 8-43%（因 `use(pendingPromise)` 延迟），但所有受影响页面仍保持 Core Web Vitals“良好”评级。
- 🧪 **性能测试方法论**：使用真实 Chrome 浏览器通过 Playwright 进行基准测试，避免 jsdom 的 CPU 开销误导优化方向。
- 🏗️ **架构设计**：保留 Fiber 协调器、标准 Hook 表面、Suspense/SSR 流式渲染，移除并发调度、时间切片、React DevTools 等 TanStack Start 不需要的特性。
- 🤖 **AI 协作模式**：描述生产环境 bug → AI 生成修复代码，形成“观察 - 描述 - 修复”的高效循环，无需深入调试。
- 📉 **成本效益分析**：构建成本从数月降至一个周末，使“不投影”成为更冒险的选择——继续使用通用库相当于为未使用功能付费。
- 🧩 **生态类比**：将投影比作 Linux 发行版（内核→发行版）或歌曲混音版，强调多样性不会伤害原项目，反而丰富生态。
- 🔮 **未来展望**：预测前端开发将进入“发行版与混音”时代，开发者会构建自己的库投影，而 `@tanstack/redact` 保持实验性，不纳入 TanStack 核心依赖。
- 🚫 **非营销立场**：避免宣传以避免社区混淆、比较成本和对 React 核心团队的干扰，仅作为个人实验和好奇者的参考。

---

### [编程文摘：邮件通讯](https://programmingdigest.net/?utm_source=web-archive&utm_campaign=react)

**原文标题**: [Programming Digest: Email Newsletter](https://programmingdigest.net/?utm_source=web-archive&utm_campaign=react)

概述：一份为软件工程师精心策划的每周通讯，提供精选文章和简短摘要，帮助读者节省时间并每周学习新内容。

- 📬 每周一封邮件，面向超过 23,134 名软件工程师
- 📚 精选文章并附有简短摘要，节省寻找有价值内容的时间
- 🧠 每周学习新知识
- 💬 读者反馈积极，称赞内容实用，如 API 设计和“Moving Faster”文章
- 🏢 读者来自多家知名公司
- 📅 通讯覆盖 2013-2026 年，由 Bonobo Press 出版

---

### [科技领导力：电子邮件通讯](https://leadershipintech.com/?utm_source=web-archive&utm_campaign=react)

**原文标题**: [Leadership in Tech: Email Newsletter](https://leadershipintech.com/?utm_source=web-archive&utm_campaign=react)

这份简报专为 CTO、工程经理及资深工程师打造，助您提升领导力。每周一和周四发送一封邮件，精选文章并附简短摘要，帮您节省时间、每周学新知。

- 📧 每周两封邮件，覆盖 28,926 名工程领导者
- 📚 精心挑选文章，附带简短摘要，节省阅读时间
- 🧠 每周学习新知识，聚焦领导力提升
- 💬 读者反馈：领导力文章无人能及，涵盖架构、会议、规划与沟通
- 🏢 被众多技术领导者阅读，来自知名企业
- 🔒 版权保护（2013-2026），提供隐私与广告选项

---

### [C# 文摘：电子邮件通讯](https://csharpdigest.net/?utm_source=web-archive&utm_campaign=react)

**原文标题**: [C# Digest: Email Newsletter](https://csharpdigest.net/?utm_source=web-archive&utm_campaign=react)

本内容介绍了 C# Digest 周刊，专为.NET 开发者精心策划的每周邮件通讯。

- 📧 每周一封邮件，服务超过20,535名C#工程师
- 📝 精选文章并附简短摘要，节省寻找优质内容的时间
- 🎯 每周学习新知识，提升.NET 开发技能
- 💼 读者反馈：文章内容实用，已在实际工作中应用
- 🔍 涵盖标准功能标志、LINQ、DiagnosticListener、操作结果模式等主题
- 🌍 读者来自全球.NET 工程师社区
- 📅 由 Bonobo Press 于 2013-2026 年持续运营，提供通讯、隐私及广告服务

---

### [让开发者保持最新动态 – Bonobo Press](https://bonobopress.com/)

**原文标题**: [Keeping developers up to date â Bonobo Press](https://bonobopress.com/)

Bonobo Press 是一家专注服务软件开发者的媒体平台，自 2013 年起通过简洁的新闻通讯为超过 8 万名技术人员提供最新资讯，并提供广告投放服务。

- 📰 发布面向软件开发者、技术主管和 CTO 的精选新闻通讯，内容简洁高效
- 👨‍💻 覆盖超过 80,000 名软件工程师、IT 专业人士和技术爱好者
- 📢 提供精准广告服务，帮助触达技术决策者与工程师群体
- 📋 设有媒体工具包，方便广告主了解合作方式并开始投放
- ✉️ 支持通过联系页面咨询问题、提出建议或洽谈广告合作

---

### [过往新闻简报：第 1 页](https://reactdigest.net/newsletters)

**原文标题**: [Past Newsletters: Page 1](https://reactdigest.net/newsletters)

以下是根据您提供的 React Digest 内容整理的摘要：

React Digest 是一份涵盖 React 生态系统的每周新闻简报，涉及 AI 编码设置、性能优化、安全漏洞、无障碍改进、新特性解析及架构最佳实践。

- 🤖 Mark Erikson 的 AI 编码设置通过父任务生成子任务并保持上下文精简，提升开发效率
- ⚡ GitHub Issues 利用 IndexedDB 缓存和服务工作者将加载时间从 1200ms 降至 700ms
- 🔒 React Flight 协议发现严重远程代码执行漏洞，影响默认 Next.js 应用
- 🛡️ TanStack npm 包遭 GitHub Actions 链式攻击，30 分钟内泄露云密钥
- ♿ 常见 React 无障碍错误包括缺失语义、焦点断裂及动态更新无声问题
- 🚀 React 19 的 useTransition 和 useActionState 钩子简化异步代码，自动处理状态和竞态条件
- 🏗️ Railway 从 Next.js 迁移到 Vite，构建时间从 10 分钟降至 2 分钟
- 📦 研究发现仅 lodash 和 moment.js 导致真实包体积膨胀，而非 barrel 导入
- 🌐 MDN 从 React SPA 转向服务器端 HTML 和 Lit 组件，开发启动时间从 2 分钟降至 2 秒
- 🧵 React Fiber 将渲染分解为约 5ms 的块，确保高优先级更新可中断慢任务
- 🧪 React 的 use() 钩子跳过传统规则，在渲染时读取 Promise 并与 Suspense 配合
- 🗑️ 前端内存泄漏影响 86% 项目，55,864 种模式来自未清理的定时器和事件
- 🔧 重建 18 个月代码的经验强调未测试代码库对用户的危害
- 🧩 功能型 React 架构强调 setState 异步队列和 AsyncLocalStorage 用于上下文传递
- 🎨 虚拟滚动技术处理数十亿行数据，结合 React Router 加载器和微前端
- 💔 一个心形表情符号导致应用变慢的调试故事，以及 React Native 的改进
- 🤖 AI 在 React 调试中的能力评估，包括 ViewTransition 元素和测试策略
- ⚠️ useOptimistic 钩子的复杂性及 React Compiler 在库更新中的问题
- 🏆 React 最佳实践来自 Vercel，涵盖性能优化和客户端组件使用
- 🕵️ 无需源码即可重建 React 组件的方法，以及 React Conf 2025 的亮点
- 📊 AI 在 React 编码中的表现参差不齐，以及 30 年 Web 开发演变

---

### [隐私](https://reactdigest.net/privacy)

**原文标题**: [Privacy](https://reactdigest.net/privacy)

概述摘要  
该隐私政策详细说明了 React Digest 如何收集、使用和保护用户个人信息，强调遵守法律、透明操作及用户权利。

- 🔒 隐私承诺：我们高度重视用户隐私，所有信息收集和使用均遵循明确目的，并依法或经用户同意进行。
- 📧 信息收集：仅收集电子邮件地址，用于发送新闻通讯，不用于其他用途。
- 🧒 儿童保护：遵守 COPPA 法案，不故意收集 13 岁以下儿童信息，若发现请联系我们。
- 📋 数据访问权：根据英国《数据保护法》，用户可申请获取我们存储的全部个人信息，需发送邮件至指定地址。
- 🗑️ 数据删除：用户可要求删除个人数据，通过邮件提交请求。
- 🚫 反垃圾邮件：我们坚决反对垃圾邮件，仅通过邮件发送新闻通讯，用户可随时点击退订链接取消订阅。
- 🛡️ 安全保障：采取合理安全措施保护个人信息，防止丢失、盗窃或未经授权访问。
- 📢 政策透明：向客户公开信息管理政策和实践，确保保密性得到维护。

---

### [媒体资料包 – 倭黑猩猩出版社](https://bonobopress.com/media-kit/)

**原文标题**: [Media Kit â Bonobo Press](https://bonobopress.com/media-kit/)

本媒体工具包介绍了 Bonobo Press 旗下四份面向技术人员的新闻通讯的订阅数据、广告价格与合作流程，旨在帮助广告主精准触达目标受众。

- 📊 **高互动率受众**：所有新闻通讯的打开率和点击率均高于行业基准，订阅者多为决策者或技术专家。
- 📬 **Leadership in Tech**：面向技术领导者，22,325 订阅者，打开率 57.95%，每期赞助费$2,235，预计点击 365-585 次。
- 📬 **Programming Digest**：面向软件工程师，20,032 订阅者，打开率 50.41%，每期赞助费$985，预计点击 273-493 次。
- 📬 **C# Digest**：面向.NET 开发者，17,098 订阅者，打开率 54.92%，每期赞助费$1,220，预计点击 411-631 次。
- 📬 **React Digest**：面向前端开发者，20,075 订阅者，打开率 54.06%，每期赞助费$1,375，预计点击 303-523 次。
- 💰 **价格与 CPC**：CPC 范围从$1.93 到$6.12，部分新闻通讯提供次级广告位（如 Leadership in Tech 次级位$1,565）。
- 📝 **纯文本广告格式**：广告嵌入新闻通讯正文，需提供链接、标题（<100 字符）和描述（<400 字符），截止日期为发布前 4 天。
- 🗓️ **预订流程**：需提前数周联系，流程包括产品介绍、排期、付款锁定、素材提交、上线及效果报告。
- 🤝 **合作案例**：合作伙伴包括 Okta、GitLab、Datadog、MongoDB、Pluralsight 等，常重复投放。

---

