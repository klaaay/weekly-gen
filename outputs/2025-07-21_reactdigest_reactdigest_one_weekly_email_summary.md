### [React 文摘：电子邮件通讯](https://reactdigest.net/)

**原文标题**: [React Digest: Email Newsletter](https://reactdigest.net/)

React Digest 是一份为 React 开发者精心策划的每周通讯，汇集了精选文章和实用资源，帮助开发者节省时间并持续学习。

- 📰 每周一封邮件，为超过 22,364 名前端工程师提供精选内容  
- 🔍 包含手选文章及简短摘要，节省寻找有价值内容的时间  
- 📚 每周学习新知识，涵盖 React 生态的最新动态  
- 💬 读者反馈积极，称赞内容实用且更新及时  
- 🌍 被全球前端工程师广泛阅读  
- ©️ 由 Bonobo Press 发行，涵盖 2013-2025 年

---

### [《架构师微前端指南：React 与 Angular 的模块联邦实践》](https://developersvoice.com/blog/frontend/micro-frontends-with-react-and-angular/)

**原文标题**: [The Architectâs Guide to Micro-Frontends: Module Federation with React & Angular](https://developersvoice.com/blog/frontend/micro-frontends-with-react-and-angular/)

### 概述总结  
本文深入探讨了微前端架构及其在现代企业中的应用，重点介绍了使用 React 和 Angular 实现模块联邦（Module Federation）的技术细节。文章从微前端的战略意义、实现策略、架构设计到实际应用和未来趋势，全面解析了如何通过模块联邦解决前端单体应用的扩展性问题，提升团队自治和开发效率。

- 🏗️ **微前端的战略意义**：解决单体前端应用的技术债务、开发瓶颈和团队自治问题，通过独立部署、自治团队和技术无关性实现业务对齐。  
- 🔍 **实现策略对比**：分析了构建时集成（如 NPM 包）、服务端集成（如 SSI）、客户端集成（如 iframe 和 Web 组件）的优缺点，强调运行时集成（如模块联邦）的优势。  
- 🧩 **模块联邦核心概念**：介绍了宿主（Host）、远程模块（Remote）、共享依赖（Shared Dependencies）和双向托管（Bidirectional Hosting）的关键设计模式。  
- 🛠️ **React 与 Angular 实践**：分别详细说明了如何配置宿主和远程应用，动态加载组件，以及跨框架状态管理和路由协调的策略。  
- 🔄 **多框架混合架构**：探讨 React 与 Angular 的互操作性，通过 Web 组件或手动挂载实现框架无关的集成，强调事件总线和共享服务的通信模式。  
- 🚀 **生产级考量**：涵盖认证授权、CI/CD 流水线、性能优化（缓存、监控）和共享组件库的治理，确保分布式前端的稳定性和一致性。  
- 🌐 **未来趋势**：展望浏览器原生模块支持（如 Import Maps）、服务端渲染（SSR）和新兴工具链（如 Vite Federation、Rspack）的发展。  
- ⚖️ **决策框架**：总结微前端的收益（团队自治、渐进式现代化）与成本（复杂度、测试负担），建议根据团队规模和业务需求评估是否采用。  

文章强调微前端不仅是技术变革，更是组织文化的转型，需结合业务上下文逐步演进。

---

### [WorkOS —— 让您的应用具备企业级能力。](https://workos.com/?utm_source=reactdigest&utm_medium=newsletter&utm_campaign=q22025)

**原文标题**: [WorkOS â Your app, Enterprise Ready.](https://workos.com/?utm_source=reactdigest&utm_medium=newsletter&utm_campaign=q22025)

WorkOS 是一个面向企业的开发平台，提供快速集成企业级功能（如单点登录、目录同步等）的解决方案，帮助开发者轻松拓展企业客户市场。

- 🚀 **企业级功能快速集成**：通过几行代码即可实现单点登录（SSO）等功能，节省数月开发时间。  
- 🔐 **全面认证支持**：支持所有 SAML/OIDC 身份提供商、社交登录（如 Microsoft、Google）及无密码验证（Magic Auth）。  
- 🛠 **开发者友好设计**：提供现代化 API、多语言 SDK（Node.js、Ruby 等）及实时 Webhook 事件通知。  
- 🔄 **目录同步与 SCIM**：无缝集成企业 HRIS 系统（如 Okta、Bamboo），简化用户生命周期管理。  
- 🏢 **管理员门户**：提供品牌化托管界面，供 IT 管理员自助配置 SSO，减少支持团队负担。  
- 📈 **市场拓展助力**：解决企业客户复杂需求，避免因 IT 限制丢失商机，案例显示客户集成效率显著提升。  
- 💬 **客户高度评价**：多家企业称赞其易用性、文档完善及卓越的 Slack 技术支持，部分客户认为“早合作会带来更多业务”。

---

### [架构设计中的约束：实用指南 | 洛伦·斯图尔特](https://www.lorenstew.art/blog/always-architect-with-contraints)

**原文标题**: [Architecting with Constraints: A Pragmatic Guide | Loren Stewart](https://www.lorenstew.art/blog/always-architect-with-contraints)

Loren Stewart 是一位软件开发者，近期发表了一系列关于前端架构和开发实践的文章，强调基于约束的架构设计，避免过度工程化，并提倡根据项目需求选择合适的工具。

- 🏗️ 文章探讨了基于约束的架构设计方法，强调应根据项目需求而非习惯选择工具，避免过度工程化。
- 🔍 通过一个简单的产品页面案例，对比了使用 Next.js 和 Astro + Lit 的实现方式，展示了后者在性能和简洁性上的优势。
- ⚖️ 分析了不同框架（如 Next.js、SvelteKit 和 Astro + Lit）的优缺点，指出在简单交互场景下，轻量级方案更优。
- 📊 提供了实际数据对比，显示 Astro + Lit 方案在 JavaScript 包大小上显著优于其他框架，提升了用户体验和性能。
- 🛠️ 提倡开发者从架构师的角度思考，基于项目约束和需求做出技术决策，而非仅依赖熟悉的工具。

---

### [使用谢尔宾斯基三角演示测试 React Fiber 的并发 API | 作者：NOUINOU Saâd | 2025 年 7 月 | Medium](https://medium.com/@nouinou.saad/putting-react-fibers-concurrency-apis-to-the-test-with-the-sierpinski-triangle-demo-01bf95c1179a)

**原文标题**: [Putting React Fiber’s concurrency APIs to the test with the Sierpinski Triangle demo. | by NOUINOU Saâd | Jul, 2025 | Medium](https://medium.com/@nouinou.saad/putting-react-fibers-concurrency-apis-to-the-test-with-the-sierpinski-triangle-demo-01bf95c1179a)

React Fiber 通过并发 API 优化渲染性能，但在高频动画场景下仍需结合浏览器原生 API 实现流畅效果。

- 🌀 React Fiber 自 2017 年引入可中断渲染机制，通过实验性 API 演示了 Sierpinski 三角形动画的响应式效果  
- 🔍 团队尝试用官方并发 API（如 startTransition/useDeferredValue）复现该效果，发现动画仍存在卡顿  
- ⚡️ useTransition 虽能延迟数字更新保持悬停交互流畅，但无法解决动画帧率问题  
- 📊 性能分析显示：动画渲染延迟高达 300ms，而交互响应始终保持在 16ms 帧预算内  
- 🎬 最终解决方案：使用 requestAnimationFrame 直接将动画逻辑移出 React 渲染周期  
- 💡 关键结论：并发 API 擅长调度逻辑更新，高频动画仍需依赖浏览器原生 API 控制  
- 🔗 完整代码示例见 GitHub 仓库：react-fiber-vs-stack-demo

---

### [世界上最长的一次 React Hooks 迁移 | 作者：Chris Krogh | 2025 年 6 月 | The Craft](https://craft.faire.com/the-worlds-longest-react-hooks-migration-8f357cdcdbe9?gi=525804fe7c4d)

**原文标题**: [The world’s longest React hooks migration | by Chris Krogh | Jun, 2025 | The Craft](https://craft.faire.com/the-worlds-longest-react-hooks-migration-8f357cdcdbe9?gi=525804fe7c4d)

Faire 公司完成了史上最长的前端代码迁移，将 React 类组件和 MobX 类转换为功能组件和钩子，提升了代码可维护性和性能，同时为 NextJS 的服务器组件做好了准备。

- 🚀 **迁移背景**：Faire 完成了从 React 类组件和 MobX 到功能组件和钩子的迁移，提升了代码可维护性和性能。  
- ⏳ **延迟原因**：2019 年钩子发布时，公司刚完成 MobX 迁移，且业务快速增长，未立即采用钩子。  
- 📈 **问题积累**：代码库增长 5 倍，团队仅翻倍，导致迁移复杂度和范围大幅增加。  
- 🛠 **维护性问题**：类组件和 MobX 导致代码臃肿，缺乏统一标准，难以维护。  
- ⚡ **性能问题**：包体积增大，数据获取层缺乏客户端缓存，影响性能。  
- 🔧 **迁移策略**：2022 年决定迁移，使用 ESLint 规则跟踪进度，升级 mobx-react 以支持钩子。  
- 🤖 **自动化工具**：与 Grit 合作，部分自动化转换类组件和 MobX 类到钩子。  
- 🧪 **测试挑战**：迁移后出现 useEffect 无限循环等问题，需手动测试和专家审核。  
- 🏆 **团队激励**：通过 useQuery 简化数据获取，激励开发者自愿迁移，但整体进展不均。  
- 📊 **强制迁移**：2025 年批准强制迁移，AI 工具提升后加速剩余工作。  
- 💡 **迁移成果**：数据预取提升页面加载速度，订单量增加 5%；移除 MobX 后，React 编译器实验提升交互性能 25%。  
- 🔮 **未来计划**：继续在其他 React 应用中移除 MobX，利用 AI 加速迁移。  
- 🎯 **总结**：迁移是 UI 构建方式的现代化，提升了代码模块化和工具兼容性，为未来开发奠定基础。

---

### [介绍 DataQueue | Nico 的博客](https://www.nico.fyi/blog/dataqueue-dev-background-job-queue-postgresql-typescript)

**原文标题**: [Introducing DataQueue | Nico's Blog](https://www.nico.fyi/blog/dataqueue-dev-background-job-queue-postgresql-typescript)

DataQueue 是一个为 Node.js 和 PostgreSQL 设计的开源后台任务队列库，特别适合现代全栈 React 项目，提供类型安全和便捷的任务管理功能。

- 📅 发布日期：2025 年 7 月 15 日，作者 Nico Prananta  
- 🛠️ **背景任务解决方案**：DataQueue 允许在 PostgreSQL 中存储后台任务队列，避免额外技术栈（如 Redis）或付费服务。  
- 🚀 **核心优势**：  
  - 原生 TypeScript 支持，确保任务类型与数据传递的强类型安全。  
  - 示例：可定义 `send_email` 和 `generate_report` 任务，并严格校验载荷数据结构。  
- 📝 **代码示例**：  
  - 通过 `JobPayloadMap` 定义任务类型，在处理器中自动匹配载荷类型。  
  - 支持延迟执行（如 5 秒后发送邮件）、优先级设置和任务标签分组。  
- ⚙️ **适用场景**：  
  - 适用于无服务器环境（如 Vercel），通过定时任务（Cron）处理队列。  
  - 功能扩展：任务重试、延迟执行、标签管理等。  
- 📚 **文档与资源**：  
  - 提供详细[文档](https://github.com/nicnocquee/dataqueue)和 GitHub 开源链接。  
- 🔥 **社区互动**：作者鼓励试用并反馈，支持 Bluesky 和 Twitter 讨论。

---

### [比起我之后打造的一切，我更以这 128 千字节为豪 | Mike Hall | 2025 年 7 月 | Medium](https://medium.com/@mikehall314/im-more-proud-of-these-128-kilobytes-than-anything-i-ve-built-since-53706cfbdc18)

**原文标题**: [I’m more proud of these 128 kilobytes than anything I’ve built since | by Mike Hall | Jul, 2025 | Medium](https://medium.com/@mikehall314/im-more-proud-of-these-128-kilobytes-than-anything-i-ve-built-since-53706cfbdc18)

概述总结  
作者 Mike Hall 分享了一个在极端技术限制下（如 128KB 页面预算、老旧设备兼容性）设计高性能网页的经历，通过创新优化手段（如系统字体、SVG 极致压缩、无框架开发）实现了既美观又高度可访问的产品，并反思约束如何激发更优雅的解决方案。  

- 🚫 **设计误区**：同事认为美观与可访问性（WCAG 标准）不可兼得，但作者认为约束是优秀设计的催化剂。  
- 🌍 **项目背景**：非洲客户用户设备落后（40% 功能机、240px 屏幕、EDGE 网络），需适配极端环境。  
- 📏 **核心约束**：128KB 页面预算（含所有资源）、跨设备响应式（240px-4K）、Opera Mini 兼容（仅 2 秒 JS 执行）。  
- ✂️ **优化策略**：  
  - 放弃网页字体（零字节成本，避免 FOUT 问题）。  
  - 自研轻量库 Whizz（替代 jQuery/框架，仅实现必要功能）。  
  - 图片极致压缩（TinyPNG、双倍缩放 JPEG、SVG 手工优化）。  
- 🖌️ **品牌妥协**：用 SVG 双路径技巧实现客户要求的描边字体，避免体积暴增。  
- 🌐 **意外兼容性**：在 Lynx、PSP、智能电视等非标准设备上流畅运行。  
- 💡 **设计哲学**：约束不是限制，而是推动普适性创新的基石，对比现代 Web 的过度冗余（如 3MB 的 DOOM vs 现代登录表单的 MB 级 JS）。

---

### [在 CSS 中设置行长度（并使文本适应容器） | CSS-Tricks](https://css-tricks.com/setting-line-length-in-css-and-fitting-text-to-a-container/)

**原文标题**: [Setting Line Length in CSS (and Fitting Text to a Container) | CSS-Tricks](https://css-tricks.com/setting-line-length-in-css-and-fitting-text-to-a-container/)

文章概述了如何通过 CSS 设置文本行长度以及如何使文本适应容器宽度，涵盖了最佳实践、响应式设计技巧及未来 CSS 属性展望。

- 📏 **行长度定义**：指多行文本容器的宽度，过长会导致阅读困难。  
- 🎯 **WCAG 建议**：每行不超过 80 字符（中文等语言 40 字符），可用`width: 80ch`实现。  
- 🔍 **最佳行长度**：研究显示 50-75 字符更优，需结合响应式设计使用`clamp()`和`min()`函数动态调整。  
- ⚙️ **动态调整技巧**：  
  - 示例代码：`width: clamp(min(93.75vw, 50ch), 70vw, 75ch)`  
  - 支持嵌套`min()`/`max()`/`calc()`增强灵活性。  
- 🖥️ **文本适应容器（JS 方案）**：  
  - 使用 SVG+JS 动态计算文本宽度并匹配容器，代码简洁且继承 CSS 样式。  
- 🎨 **纯 CSS 方案**：Roman Komarov 的复杂技巧，需复制文本、容器查询及数学计算实现缩放。  
- 🔮 **未来 CSS 属性**：  
  - 提案`text-grow`/`text-shrink`支持多行文本适配，但可能过于复杂。  
  - 更倾向简化版`font-size: fit-width`。  
- 💡 **总结与参与**：当前技术已大幅优化行长度控制，鼓励通过 GitHub 反馈未来属性需求。

---

### [font-size-adjust 很有用](https://matklad.github.io/2025/07/16/font-size-adjust.html)

**原文标题**: [font-size-adjust Is Useful](https://matklad.github.io/2025/07/16/font-size-adjust.html)

本文介绍了 CSS 中的`font-size-adjust`属性，并指出该属性的实际用途被普遍误解。作者认为该属性不仅适用于字体回退情况，还能确保不同字体在网页中保持一致的视觉大小。

- 🖥️ `font-size-adjust`是 CSS 的一个属性，用于调整字体大小，使其在不同字体间保持一致。
- 📏 字体大小（`font-size`）实际上是指围绕字形（glyph）的盒子大小，而非字形本身的大小。
- 🔍 不同字体的字形大小存在显著差异，即使设置了相同的`font-size`。
- ⚖️ 通过`font-size-adjust: ex-height 0.5`，可以确保字母“x”的高度为盒子高度的一半，从而使不同字体的视觉大小一致。
- ❌ 普遍认为`font-size-adjust`仅适用于字体回退（fallback）情况，但作者认为这种观点不够全面。
- 🛠️ 作者建议将`font-size-adjust: ex-height 0.53`加入 CSS 重置（reset）中，以确保字体大小的一致性。
- 🔢 选择`0.53`是因为这是 Helvetica 字体的固有比例，但附近的其他数值也能达到类似效果。

---

### [粘滑效果 | CSS 技巧](https://css-tricks.com/gooey-effect/)

**原文标题**: [The Gooey Effect | CSS-Tricks](https://css-tricks.com/gooey-effect/)

Lucas Bebber 介绍了如何使用 SVG 滤镜创建粘性（Gooey）效果，并解释了其基本原理和实现方法。

- 🎨 **SVG 滤镜基础**：SVG 滤镜可以通过 CSS 应用到常规 DOM 元素上，使用 `<filter>` 元素定义滤镜效果，并通过 `filter: url('#filter-name')` 调用。
  
- 🔍 **滤镜原语**：SVG 滤镜包含多种原语（如模糊、颜色变换等），可以通过 `in` 和 `result` 属性链式组合，实现复杂效果。
  
- 🌈 **颜色矩阵**：通过 `feColorMatrix` 可以调整颜色和透明度的对比度，特别是通过修改 Alpha 通道的值来实现粘性效果。
  
- 🧩 **粘性效果实现**：结合 `feGaussianBlur` 和 `feColorMatrix` 对元素进行模糊和高对比度处理，再通过 `feBlend` 或 `feComposite` 将原始图形与效果混合。
  
- ⚠️ **注意事项**：滤镜应应用于容器而非单个元素；容器需要留出额外空间以避免边缘瑕疵；滤镜可能对性能有较高要求。
  
- 🌍 **浏览器支持**：SVG 滤镜在大多数现代浏览器中可用，但在 Safari 中可能受限，需注意兼容性问题。

---

### [WebAssembly：是的，但用在哪里？ - ACM Queue](https://queue.acm.org/detail.cfm?id=3746171)

**原文标题**: [WebAssembly: Yes, but for What? - ACM Queue](https://queue.acm.org/detail.cfm?id=3746171)

WebAssembly（Wasm）诞生 10 周年，已从技术探索阶段进入实际应用，但发展不均衡。本文分析了 Wasm 的成功与失败案例，总结了其适用场景，并预测了未来 2-3 年的发展方向。

- 🎯 **核心优势**：Wasm 作为抽象边界，在隔离与协作间提供平衡，兼具内存安全性和高效冷启动（毫秒级）。  
- 🌐 **Web 应用表现**：  
  - ✅ **成功案例**：C++/Rust 编写的桌面应用移植（如 Adobe Photoshop）、组件化功能（SQLite、Perfetto 追踪工具）。  
  - ❌ **失败领域**：游戏行业未大规模采用（如 Unreal 引擎已放弃 Wasm 后端）；前端界面仍以 JS/TypeScript 为主。  
  - 🔄 **新机遇**：WasmGC 扩展支持垃圾回收语言（如 Kotlin/Java），Google Sheets 已全面切换。  

- 🔌 **非 Web 场景**：  
  - 🛡️ **安全隔离**：Firefox 通过 RLBox 隔离不安全 C 库；字体引擎 HarfBuzz 用 Wasm 实现扩展。  
  - ☁️ **轻量虚拟化**：WALI 工具链编译应用为 Wasm，降低短任务开销；IoT 领域利用 Wasm 实现固件升级。  
  - 🧩 **组件模型**：定义高阶组件接口，支持云服务（如 Shopify 插件），微软等公司推动边缘计算创新。  

- 🚀 **未来方向**：  
  - 🔐 **安全关键系统**：内核驱动、操作系统级隔离，或替代 eBPF。  
  - 🤖 **AI 与隐私计算**：作为轻量沙箱处理敏感数据。  
  - ⚡ **持续优化**：快照恢复、虚拟内存技术进一步提升启动速度（微秒级）。  

- 📉 **挑战**：技术叙事与实际落地的差距，需避免过度炒作；生态碎片化（如 IoT 领域工具分散）。  

作者 Andy Wingo 指出，Wasm 的成功模式集中于**跨团队开发的隔离需求**，未来将在更多安全边界场景中发挥作用。

---

### [现代 JavaScript 在 NGINX 中的应用：njs 对 QuickJS 引擎的支持 – NGINX 社区博客](https://blog.nginx.org/blog/quickjs-engine-support-for-njs)

**原文标题**: [Modern JavaScript in NGINX: QuickJS Engine Support for njs – NGINX Community Blog](https://blog.nginx.org/blog/quickjs-engine-support-for-njs)

NGINX 的 njs 模块现在支持 QuickJS 引擎，提供 ES2023 兼容性，为开发者带来更多现代 JavaScript 特性。

- 🚀 **QuickJS 引擎支持**：njs 0.9.1 版本引入 QuickJS 引擎，支持完整的 ES2023 规范，包括模块、异步生成器等现代特性。
- ⚖️ **平衡性能与兼容性**：QuickJS 在保持轻量级的同时，解决了 njs 原有引擎的语言限制和生态系统兼容性问题。
- 🔧 **简单配置**：通过`js_engine`指令可轻松切换引擎，现有脚本无需修改即可运行。
- 📊 **性能考量**：QuickJS 在复杂逻辑和长运行脚本中表现优异，但上下文创建时间较长，可通过`js_context_reuse`优化。
- 🔮 **未来规划**：QuickJS 可能成为默认引擎，鼓励开发者逐步迁移以利用现代 JavaScript 特性。
- 📝 **反馈与改进**：鼓励用户试用并提供反馈，以进一步优化 JavaScript 在 NGINX 中的集成。

---

### [JavaScript 作用域提升存在问题](https://devongovett.me/blog/scope-hoisting.html)

**原文标题**: [JavaScript scope hoisting is broken](https://devongovett.me/blog/scope-hoisting.html)

现代 JavaScript 打包工具普遍采用"作用域提升"优化技术，但该技术与代码分割存在根本性冲突，导致模块执行顺序错乱、this 值异常等问题，实际优化效果有限且带来显著复杂性。

- 🌀 作用域提升原理：将模块代码直接拼接至同一作用域，替代传统函数包裹模块的方式，减少运行时间接引用  
- ⚡ 传统打包方式：每个模块被独立函数包裹，通过 require/exports 对象交互，导致体积增大和性能损耗  
- 🧩 代码分割冲突：共享模块被提取为独立包后，作用域提升破坏模块间原有的执行顺序  
- 🚨 副作用问题：模块包含 console.log 等副作用代码时，拼接后执行顺序与预期不符（如 shared1→shared2→a1→a2）  
- 🛠️ 解决方案：回归函数包裹模式（如 Parcel），通过延迟执行控制模块顺序，但丧失优化收益  
- 🎭 this 值异常：提升后模块导出函数的 this 指向变为 undefined，违反 ES 模块规范  
- 📊 现实局限性：实测仅不足 5% 模块能真正受益于作用域提升，优化覆盖范围有限  
- ⚖️ 取舍考量：相比带来的复杂性，其树摇优化和性能提升效果可被其他技术替代  
- 🔮 未来方向：Parcel 考虑放弃该优化，转向函数包裹默认设计以保障正确性

---

### [JavaScript 中普通函数和箭头函数的区别是什么？](https://jrsinclair.com/articles/2025/whats-the-difference-between-named-functions-and-arrow-functions/)

**原文标题**: [What’s the difference between ordinary functions and arrow functions in JavaScript?](https://jrsinclair.com/articles/2025/whats-the-difference-between-named-functions-and-arrow-functions/)

JavaScript 中普通函数与箭头函数的区别  

- 🏺 函数声明与函数表达式：普通函数通过`function`关键字声明或表达式创建，可命名或匿名，存在变量提升特性。  
- 🏹 箭头函数：使用`=>`语法，始终匿名且为表达式，更简洁（可省略`return`和括号），但无法用作构造函数或生成器。  
- 🔗 `this`绑定差异：箭头函数无自身`this`，继承外层上下文；普通函数的`this`由调用方式决定。  
- 🚫 限制场景：箭头函数不能用于`new`实例化、生成器（`yield`）或需要动态`this`的方法（如对象方法）。  
- 📜 代码风格：箭头函数适合回调和高阶函数；普通函数适合需要`this`绑定或前置声明的场景。  
- 🔄 选择建议：根据是否需要`this`、`new`或生成器功能决定，优先箭头函数以保持简洁性。

---

### [JavaScript 日期小测验](https://jsdate.wtf/)

**原文标题**: [The JavaScript Date Quiz](https://jsdate.wtf/)

JavaScript 的 Date 类知识测试  
- 📅 测试内容：关于 JavaScript 的 Date 类的知识  
- 🖥️ 测试环境：使用 NodeJS 24.4.0 在 MacBook Pro 上运行，时区设置为 BST（UTC+1）  
- ❤️ 制作者：samwho  
- 🔢 测试题目：共 20 个问题  
- �️ 当前进度：0/0（刚开始或未记录得分）  
- 📤 功能选项：分享或复制测试链接

---

### [React 代码演变史 | 趣味编程](https://playfulprogramming.com/posts/react-history-through-code)

**原文标题**: [
	The History of React Through Code | Playful Programming
](https://playfulprogramming.com/posts/react-history-through-code)

React 的发展历程及其核心设计理念的演变，展示了其从诞生至今的持续一致性和对未来功能的深远规划。

- 🚀 **React 的起源**：2011 年由 Jordan Walke 创建，最初为 Facebook 内部解决广告团队的问题，后因 Instagram 的需求而开源。
- 🔄 **虚拟 DOM (VDOM)**：React 引入 VDOM 以提高性能，通过对比和局部更新来优化渲染。
- 🏗️ **组件化设计**：早期使用类组件，2019 年引入 Hooks，使函数组件也能管理状态和副作用，提升代码复用性。
- ⚡ **并发特性**：React 18 引入并发渲染，通过 Fiber 架构实现任务的中断和优先级调度，优化用户体验。
- 🔄 **数据获取**：React 19 的 `use` API 和 Suspense 结合，简化数据获取和加载状态管理，避免瀑布式请求。
- 🌐 **服务器组件**：React 19 稳定了服务器组件（RSC），支持在服务器端渲染并优化客户端水合过程。
- 🔄 **双向数据流**：通过服务器动作（Server Actions）和 `useActionState` 实现客户端与服务器的无缝交互。
- 🔮 **未来方向**：包括实验性的 `<Activity>` API 和 React 编译器，旨在进一步提升性能和开发者体验。

React 的设计始终围绕一致性、可组合性和性能优化，其每个新功能都建立在原有基础之上，体现了长远的规划和持续的创新。

---

### [编程文摘：电子邮件通讯](https://programmingdigest.net/?utm_source=web-archive&utm_campaign=react)

**原文标题**: [Programming Digest: Email Newsletter](https://programmingdigest.net/?utm_source=web-archive&utm_campaign=react)

《Programming Digest》是一份专为软件工程师精心挑选的每周通讯，旨在为读者节省时间并提供有价值的学习内容。

- 📧 超过 18,966 名软件工程师订阅这份每周电子邮件  
- 📖 每期包含精选文章及简短摘要  
- ⏱️ 帮助读者节省寻找优质内容的时间  
- 🌱 每周学习新知识  
- 💬 读者反馈积极，认为内容实用且具有启发性  
- 🌍 订阅者遍布全球各地  
- ©️ 由 Bonobo Press 于 2013-2025 年发布

---

### [科技领导力：电子邮件通讯](https://leadershipintech.com/?utm_source=web-archive&utm_campaign=react)

**原文标题**: [Leadership in Tech: Email Newsletter](https://leadershipintech.com/?utm_source=web-archive&utm_campaign=react)

overview summary  
一份精心策划的每周通讯，面向 CTO、工程经理和高级工程师，旨在帮助他们成为更优秀的领导者。  

- 📩 每周一封邮件，汇集 26,952 名工程领导者  
- 📚 精选文章附简短摘要，节省寻找有价值内容的时间  
- 🌱 每周学习新知识，提升领导力技能  
- ❤️ 读者好评：内容精准，涵盖架构讨论、会议规划及沟通技巧  
- 🎯 特别推荐关于“授权”的文章，强调其重要性  
- 🌍 来自全球科技领导者的阅读选择  
- ©️ 由 Bonobo Press 提供，2013-2025 年持续更新

---

### [C#文摘：电子邮件通讯](https://csharpdigest.net/?utm_source=web-archive&utm_campaign=react)

**原文标题**: [C# Digest: Email Newsletter](https://csharpdigest.net/?utm_source=web-archive&utm_campaign=react)

C# Digest 是一份为.NET 开发者精心策划的每周通讯，提供精选文章和简短摘要，帮助开发者节省时间并每周学习新知识。

- 📧 超过19,925名C#工程师订阅这份每周电子邮件  
- 📖 阅读精选文章及简短摘要  
- ⏱️ 节省寻找有价值内容的时间  
- 🌱 每周学习新知识  
- 💬 读者反馈：  
  - 🏢 实际工作中应用了部分内容  
  - 🔍 了解到标准功能标志和 LINQ 的新知识  
  - ❤️ 推荐《The Operation Result Pattern》给同事  
- 🌍 读者来自全球.NET 工程师  
- ©️ 2013-2025 Bonobo Press

---

### [让开发者与时俱进——Bonobo 出版社](https://bonobopress.com/)

**原文标题**: [Keeping developers up to date â Bonobo Press](https://bonobopress.com/)

Bonobo Press 是一家自 2013 年起为软件开发者和技术专业人士提供新闻资讯的出版商，拥有超过 88,000 名订阅者，提供简洁高效的每周通讯，并为企业提供广告投放服务。

- 📧 提供每周精选通讯，服务于开发者、工程经理、技术主管和 CTO，内容简洁高效  
- 🎯 广告服务针对技术领域专业人士，包括软件工程师、团队领导、工程经理和 IT 决策者  
- 📩 欢迎通过联系页面进行咨询、建议或广告合作  
- ©️ 2013-2025 Bonobo Press 版权所有，附有使用条款

---

### [往期通讯：第一页](https://reactdigest.net/newsletters)

**原文标题**: [Past Newsletters: Page 1](https://reactdigest.net/newsletters)

React Digest 的精选内容概览，涵盖从模块联邦到性能优化的多个 React 技术主题。

- 🚀 2025 年 7 月 20 日：探讨 React 模块联邦、Astro 高效架构及并发 API，附带 React Hooks 迁移与 DataQueue 实战  
- 🔍 2025 年 7 月 13 日：通过代码回顾 React 演进史，涵盖 PDF.js 集成、动态动画及 Server Components 测试方法  
- 🧩 2025 年 7 月 6 日：分析 React 组件模块化哲学，涉及 AI 代理构建与数据获取技术  
- ⚡ 2025 年 6 月 29 日：优化 React 重渲染性能，介绍 Zero-UI、MCP 连接及 Server Components 应用  
- ✋ 2025 年 6 月 22 日：视频会议实时手势识别，对比 React 数据获取方法与自定义 useState 钩子  
- 🌀 2025 年 6 月 15 日：细粒度响应式实践，Next.js 中避免 Props 透传及 URL 状态管理技巧  
- 🛠️ 2025 年 6 月 8 日：剖析现代 React 框架痛点，含 API 消费指南与 Progressive JSON 创新技术  
- 🚦 2025 年 6 月 1 日：Dan Abramov 谈高效数据获取，含"长按删除"组件与 TanStack 路由方案  
- 🎯 2025 年 5 月 25 日：flushSync 焦点管理实战，并发渲染原理与自建 TanStack Query 教程  
- 🔐 2025 年 5 月 18 日：React Router 实现 OpenAuth，探讨 Context 效率与 Server Components 静态生成  
- 📊 2025 年 5 月 11 日：复杂应用数据获取架构，含色彩方案切换与媒体查询自定义钩子  
- ✨ 2025 年 5 月 4 日：View Transitions 动画优化，useEffect 执行顺序与 Promise 序列化解析  
- 🤯 2025 年 4 月 27 日：Dan Abramov 谈"不可能组件"，React Query 状态简化与编译器 RC 发布  
- 📡 2025 年 4 月 20 日：服务端渲染深度解析，全栈 AI 聊天应用构建与 React 架构演进  
- 🏗️ 2025 年 4 月 13 日：高级 React 技巧，含 React Query 原理与动态表单挑战  
- ⚖️ 2025 年 4 月 6 日：架构权衡分析，无库表单构建与 Dash.js 自适应流实现  
- 🔑 2025 年 3 月 30 日：Next.js 授权实践，View Transition API 及国际化技巧  
- 🌐 2025 年 3 月 23 日：SSR 深度指南，TanStack 实时数据与 URL 状态管理  
- ⚡ 2025 年 3 月 16 日：Next.js 性能优化，Toast 通知实现与 React.memo 替代方案  
- 📶 2025 年 3 月 9 日：React 信号系统挑战，状态管理工具对比与布局效应研究

---

### [隐私](https://reactdigest.net/privacy)

**原文标题**: [Privacy](https://reactdigest.net/privacy)

隐私政策概述，强调个人信息保护的重要性，明确信息收集、使用及披露的原则，并提供用户数据管理选项。

- 🔒 隐私至关重要，制定政策以明确如何收集、使用、披露个人信息。  
- 🎯 收集个人信息前会明确目的，仅用于指定或兼容用途，需用户同意或法律要求。  
- ⏳ 仅在必要时保留个人信息，确保数据使用期限合理。  
- 📝 通过合法公平手段收集信息，尽可能获得用户知情或同意。  
- ✔️ 确保个人数据准确、完整、最新，符合使用目的。  
- 🛡️ 采取合理安全措施保护信息，防止丢失、盗用或未授权访问。  
- 📢 向用户公开个人信息管理政策及实践。  
- ✉️ 仅收集用户邮箱地址用于发送周刊，不用于其他目的。  
- 🚸 遵守 COPPA，不故意收集或存储 13 岁以下儿童信息。  
- 📬 用户可依据《数据保护法》请求获取或删除存储的个人信息，联系邮箱：[email protected]。  
- 🚫 反对垃圾邮件，提供随时退订选项，绝不滥用用户邮箱。  
- ©️ 版权归属 Bonobo Press（2013-2025），提供新闻通讯、隐私及广告相关链接。

---

### [媒体资料包——Bonobo 出版社](https://bonobopress.com/media-kit/)

**原文标题**: [Media Kit â Bonobo Press](https://bonobopress.com/media-kit/)

Bonobo Press 为程序员和技术人员提供最新趋势、工具和技术的周报，涵盖软件开发者、工程经理、CTO 等受众，内容精选且读者参与度高。广告合作伙伴包括软件工具、招聘、会议等，旨在精准触达目标受众并提升转化率。

- 📧 **Newsletters 统计**：各周报订阅数、打开率、点击率及赞助费用详实，如《Leadership in Tech》订阅 26,385，打开率 57.95%，点击率 11.38%，赞助费$1,940/期。  
- 🌍 **受众分布**：主要读者来自欧洲（40%）和美国（35%），涵盖 Google、Amazon 等公司及不同规模企业。  
- 💼 **职位覆盖**：包括 CTO、工程经理、全栈工程师等，各周报侧重不同技术领域（如 C#、React）。  
- 💰 **广告价值**：CPC（每次点击成本）范围明确，如《Programming Digest》CPC 为$1.98-$3.92，点击量 223-443 次。  
- ✍️ **广告格式**：纯文本嵌入，需提供链接、标题（<100 字符）和描述（<400 字符），截止日期为发布前 4 天。  
- 📅 **预订流程**：需提前数周沟通，流程包括产品介绍、排期、付款、素材提交及效果报告。  
- 🤝 **合作伙伴**：涵盖 Okta、GitLab、MongoDB 等知名企业，重复合作率高。  
- 📩 **联系方式**：提供合作咨询入口，强调提升潜在客户与转化的目标。

---

