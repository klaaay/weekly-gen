### [JavaScript 周刊第 768 期：2026 年 1 月 13 日](https://javascriptweekly.com/issues/768)

**原文标题**: [JavaScript Weekly Issue 768: January 13, 2026](https://javascriptweekly.com/issues/768)

本期 JavaScript 周刊聚焦于 Web 依赖管理问题、新工具发布及技术趋势，涵盖 React Conf 视频上线、Temporal API 的兴起以及多项框架更新。

- 🎬 **React Conf 2025 完整视频上线**：包含 25 场演讲和 23 次访谈，涵盖核心团队深度对话。
- ⚖️ **Deno 与 Oracle 商标纠纷延期**：双方同意将案件审理延长 60 天，预计持续至 2027 年。
- 📘 **免费 TypeScript 简明指南发布**：《The Concise TypeScript Book》提供开源精要教程。
- 🔒 **Node.js 多版本安全更新**：针对 v20.x 至 25.x 版本修复五个安全漏洞。
- 🚀 **Bun v1.3.6 功能升级**：新增 tar 压缩包处理、注释 JSON 解析及性能优化。
- ⏳ **Temporal API 逐步取代 Date 对象**：Chrome 144 全面支持，提供 Polyfill 过渡方案。
- 🔄 **迭代器助手优化数据处理**：通过惰性迭代提升大规模数据操作效率。
- 🧩 **memlab 2.0 内存泄漏检测框架**：基于 Facebook 实践，支持堆快照对比与泄漏分析。
- 🎨 **Fabric.js 7.1 增强 Canvas 交互**：为 SVG 元素提供抽象层，支持 Node.js 环境。
- 📊 **State of HTML 2025 调研结果公布**：揭示前端生态最新发展趋势。

---

### [网络依赖关系已断裂，我们能否修复？ • 莉亚·维鲁](https://lea.verou.me/blog/2026/web-deps/)

**原文标题**: [
		Web dependencies are broken. Can we fix them? • Lea Verou](https://lea.verou.me/blog/2026/web-deps/)

本文探讨了 Web 平台中 JavaScript 依赖管理的现状与问题，指出当前依赖管理过于依赖第三方打包工具，而缺乏原生、轻量的解决方案，导致开发者面临复杂的配置和工具链负担。文章分析了现有无打包方案的局限性，并提出了改进方向。

- 🚫 **依赖管理外包问题**：Web 平台将依赖管理功能外包给第三方打包工具，导致代码复用成为权衡取舍的难题，而其他生态系统（如 Node.js、Python、Rust）中依赖管理是原生、无缝的。
- 🛠️ **打包工具的滥用**：打包工具本应用于性能优化，但现在却成为依赖管理的必需品，增加了新手上手门槛，形成了“可用性悬崖”。
- 🌐 **无打包方案的缺陷**：现有无打包方案（如直接引用 node_modules、使用公共 CDN、本地重写 CDN 等）均存在安全、封装性或工具链复杂性问题，无法优雅处理依赖的依赖。
- 📦 **“浏览器”捆绑包的局限**：库提供的“浏览器”捆绑包虽可避免打包，但会导致依赖重复打包，无法共享相同依赖，且将打包工作外包给库作者。
- 🗺️ **导入映射的不足**：导入映射（import maps）虽允许浏览器解析说明符，但需在 HTML 中内联、无法外部化，且需手动映射所有传递依赖，缺乏局部性和可组合性。
- 🔄 **改进方向**：提出通过外部导入映射、JS 导入映射、HTTP 头部映射等方式改进导入映射；建议在 package.json 中标记客户端依赖；探索将说明符视为 URL 类型的激进方案，以实现服务器透明解析。
- 📢 **呼吁行动**：强调依赖管理应作为平台原生功能，呼吁浏览器厂商、标准组织和开发者共同解决这一根本问题，以提升 Web 开发生态的健康性。

---

### [打造沉浸式体验 | 前端大师](https://frontendmasters.com/courses/winning-websites/?utm_source=email&utm_medium=javascriptweekly&utm_content=winningwebsites)

**原文标题**: [Build Immersive Experiences | Frontend Masters](https://frontendmasters.com/courses/winning-websites/?utm_source=email&utm_medium=javascriptweekly&utm_content=winningwebsites)

本课程教授如何运用现代网页动画与交互技术，打造引人入胜、获奖级别的营销网站，涵盖从基础动画到高级 3D 集成的全流程技能。

- 🎨 学习使用 GSAP 动画库和 CSS 创建流畅、高性能的动画效果
- 📜 掌握基于滚动的动画叙事技巧，实现元素固定、图像序列动画等交互体验
- ⚡ 优化动画性能，利用 GPU 加速并高效管理渲染，确保流畅运行
- 🧊 集成 Three.js 与 React Fiber 构建和动画化 3D 场景，包括灯光与摄像机控制
- ♿ 创建兼顾可访问性的动画，尊重用户运动偏好、设备性能与电池状况
- 🏆 课程包含 24 节课、4.3 小时内容，提供结业证书，适合自学提升创意编码能力
- 👨‍🏫 由 Vercel 设计工程师 Matias Gonzales 授课，分享十年动画与 WebGL 经验
- 📝 学习平台支持进度跟踪、笔记记录、测验和闪卡，助力巩固知识

---

### [React Conf 2025 | 10 月 7-8 日 | 内华达州亨德森及线上 | 欢迎加入！](https://conf.react.dev/)

**原文标题**: [React Conf 2025 | October 7-8 | Henderson, Nevada & online | Join us!](https://conf.react.dev/)

React Conf 2025 活动页面，包含演讲者名单、赞助商信息及订阅更新功能。

- 📸 提供活动照片、演讲者介绍及赞助商展示
- 🎤 列出多位知名演讲者，包括 Alex Hunt、Kent C. Dodds、Zeno Rocha 等
- 🤝 展示铂金、黄金、直播、白银等级别的赞助商
- 📩 支持订阅新闻通讯，获取会议更新、视频和公告
- ⚖️ 包含隐私政策、行为准则及往届会议（2015-2024）信息
- 🌐 由 Meta 和 Callstack 等组织方支持举办

---

### [React 团队访谈 - YouTube](https://www.youtube.com/watch?v=NJUXAWTuaTo&list=PLNG_1j3cPCaZQCTcTinGsD-s8Wt9PIsYA&index=4)

**原文标题**: [React team interview - YouTube](https://www.youtube.com/watch?v=NJUXAWTuaTo&list=PLNG_1j3cPCaZQCTcTinGsD-s8Wt9PIsYA&index=4)

该内容为 YouTube 平台页脚导航链接，列出了网站的主要政策、功能说明及公司信息。

- 📄 关于平台的基本介绍
- 📰 新闻与媒体相关
- ©️ 版权信息说明
- 📧 联系渠道
- 🧑‍🎨 创作者服务
- 📢 广告合作
- 👩‍💻 开发者资源
- 📑 使用条款
- 🔒 隐私政策
- ⚙️ 平台运作机制
- 🧪 新功能测试
- 🏢 公司所有权声明（谷歌 2026）

---

### [@deno.land 在蓝天上](https://bsky.app/profile/deno.land/post/3mbuirnjqxc22)

**原文标题**: [@deno.land on Bluesky](https://bsky.app/profile/deno.land/post/3mbuirnjqxc22)

这是一个关于 JavaScript 商标争议和 Bluesky 社交平台技术基础的说明。

- 🚀 Bluesky 是一个高度交互的网络应用，需要 JavaScript 运行
- 🔗 了解更多信息可访问 bsky.social 和 atproto.com 网站
- ⚖️ Oracle 已请求将 JavaScript 商标撤销案延期 60 天审理
- 📊 Mozilla 正在收集证据，证明“JavaScript”已成为行业通用术语
- 📅 案件最新进展更新于 2026 年 1 月 7 日

---

### [GitHub - gibbok/typescript-book: 《简明 TypeScript 指南》：TypeScript 高效开发简明指南。免费开源。](https://github.com/gibbok/typescript-book)

**原文标题**: [GitHub - gibbok/typescript-book: The Concise TypeScript Book: A Concise Guide to Effective Development in TypeScript. Free and Open Source.](https://github.com/gibbok/typescript-book)

《简明 TypeScript 手册》是一本免费开源的 TypeScript 开发指南，全面覆盖 TypeScript 5.2 的核心概念与高级特性，适合从初学者到有经验的开发者使用。

- 📚 **开源免费** – 本书完全免费开源，旨在让高质量技术教育普及化，支持自愿付费或赞助以持续更新内容。
- 🌐 **多语言版本** – 提供中文、意大利文等多种语言翻译，方便全球开发者学习。
- 📖 **内容全面** – 从基础类型系统、配置安装到高级特性如泛型、装饰器、工具类型等，涵盖 TypeScript 开发的各个方面。
- 🛠️ **实用指南** – 包含迁移建议、类型推断、类型收窄、模块系统等实战技巧，帮助编写健壮且类型安全的代码。
- 🔧 **工具与生态** – 介绍 TypeScript 编译器配置、语言服务、第三方类型定义（@types）及现代 JavaScript 特性支持。
- 🧩 **高级主题** – 深入讲解条件类型、映射类型、可变元组类型、协变与逆变、satisfies 操作符等高级类型操作。
- 📦 **资源与社区** – 提供 EPUB 下载、在线版本访问及作者联系方式，便于进一步学习和支持。

---

### [Node.js — 2026 年 1 月 13 日星期二安全更新发布](https://nodejs.org/en/blog/vulnerability/december-2025-security-releases)

**原文标题**: [Node.js — Tuesday, January 13, 2026 Security Releases](https://nodejs.org/en/blog/vulnerability/december-2025-security-releases)

Node.js 项目于 2026 年 1 月 13 日发布了安全更新，针对 20.x、22.x、24.x 和 25.x 等活跃发布线，共修复了 8 个安全漏洞，其中包括 3 个高危问题。此次更新旨在解决可能引发内存泄露、权限绕过、服务崩溃等风险的安全隐患，并提供了相应的补丁版本。用户应尽快升级至 Node.js 20.20.0、22.22.0、24.13.0 或 25.3.0 版本以确保系统安全。

- 🚨 **高危漏洞修复**：修复了 3 个高危漏洞，包括缓冲区未初始化内存泄露（CVE-2025-55131）、文件系统权限绕过（CVE-2025-55130）和 HTTP/2 服务崩溃（CVE-2025-59465）。
- ⚠️ **中危问题处理**：解决了 4 个中危问题，涉及不可捕获的调用栈错误（CVE-2025-59466）、TLS 证书内存泄露（CVE-2025-59464）、Unix 域套接字权限绕过（CVE-2026-21636）和 TLS 回调异常（CVE-2026-21637）。
- 🔧 **低危漏洞修补**：修复了 1 个低危漏洞（CVE-2025-55132），该漏洞允许在只读权限下修改文件时间戳。
- 📦 **依赖项更新**：安全版本包含对 c-ares（1.34.6）和 undici（6.23.0, 7.18.0）的依赖更新，以解决公开漏洞。
- 📅 **发布与支持**：更新版本已于 2025 年 12 月 15 日或之后发布，对于已结束维护的版本，可通过 OpenJS 生态系统可持续性计划合作伙伴获得商业支持。
- 🔗 **安全资源**：建议用户关注 Node.js 安全政策页面和 nodejs-sec 邮件列表，及时获取安全公告和更新信息。

---

### [Bun v1.3.6 | Bun 博客](https://bun.com/blog/bun-v1.3.6)

**原文标题**: [Bun v1.3.6 | Bun Blog](https://bun.com/blog/bun-v1.3.6)

本文介绍了 Bun 的最新更新，包括安装与升级方法、新增 API 功能、性能优化、bug 修复及多项改进。

- 🚀 **安装与升级**：支持多种安装方式（curl、npm、PowerShell 等），升级命令为`bun upgrade`
- 📦 **Bun.Archive API**：新增内置 API，支持创建和提取 tar 归档文件，可选 gzip 压缩，并兼容 S3 存储
- 📝 **Bun.JSONC API**：新增`Bun.JSONC.parse()`，支持解析带注释的 JSONC 格式文件
- 🔧 **构建功能增强**：`Bun.build()`新增`metafile`选项生成构建元数据，支持`files`选项处理虚拟文件
- ⚙️ **编译与构建优化**：新增`--compile-executable-path`标志指定本地 Bun 可执行文件，支持`reactFastRefresh`选项
- ⚡ **性能大幅提升**：`Response.json()`提速 3.5 倍，`async/await`提速 15%，`Promise.race()`提速 30%，`Buffer.indexOf`使用 SIMD 优化提速 2 倍
- 🔌 **功能扩展**：新增`--grep`测试标志，`Bun.hash.crc32`提速 20 倍，支持 S3 Requester Pays 和 WebSocket 代理
- 🐛 **大量 bug 修复**：涵盖 Node.js 兼容性、Bun API、Web API、安装、构建、CSS 解析、TypeScript 类型和 Windows 平台问题
- 👥 **贡献者致谢**：感谢 23 位贡献者的代码提交

---

### [pnpm 10.28 | pnpm](https://pnpm.io/blog/releases/10.28)

**原文标题**: [pnpm 10.28 | pnpm](https://pnpm.io/blog/releases/10.28)

pnpm 10.28 版本引入了新的 beforePacking 钩子，允许在发布时自定义 package.json，同时优化了过滤安装的性能，并修复了若干错误。

- 🪝 新增 beforePacking 钩子，可在运行 `pnpm pack` 或 `pnpm publish` 时修改即将发布的 package.json，不影响本地文件
- ⚡ 修复了过滤安装（如 `pnpm install --filter ...`）的性能回归问题，使其速度与完整安装相当或更快
- 🔗 当存储库位于项目子目录时，不再向存储的项目注册表添加项目符号链接
- 📄 现在可以在 `pnpm-workspace.yaml` 中声明 `requiredScripts` 设置

---

### [发布 21.1.0-rc.0 · angular/angular · GitHub](https://github.com/angular/angular/releases/tag/v21.1.0-rc.0)

**原文标题**: [Release 21.1.0-rc.0 · angular/angular · GitHub](https://github.com/angular/angular/releases/tag/v21.1.0-rc.0)

Angular 发布了 v21.1.0-rc.0 预发布版本，包含多项编译器、核心模块、表单和路由的更新与修复。

- 🖼️ 为 Cloudflare、Cloudinary、ImageKit 和 Imgix 图像加载器添加自定义转换支持
- 🔧 编译器增强：支持多 switch case 匹配、改进表达式 AST 节点类型、提供更准确的表达式位置信息
- 🩺 编译器 CLI 改进：确保组件导入诊断在导入表达式中报告，支持 typeof 类型引用中的限定名称
- 🧩 核心模块更新：添加稳定性调试工具，支持函数调用中的剩余参数、数组和对象字面量中的展开元素，修复动画中的视图数据泄漏和内存泄漏问题
- 📝 表单模块新增 formField 指令，允许自定义控件要求 dirty、hidden 或 pending 输入，支持非基于信号的模型和只读数组
- 🧭 路由功能扩展：添加路由清理控制，创建计算 isActive 的独立函数，扩展重定向函数的参数，实验性集成平台导航 API，修复 RouterLink href 更新问题

---

### [Ember 6.9 版本发布](https://blog.emberjs.com/ember-released-6-9/)

**原文标题**: [Ember 6.9 Released](https://blog.emberjs.com/ember-released-6-9/)

Ember 6.9 版本已发布，这是一个标准的小版本更新，同时 Ember.js 6.8 升级为长期支持版本，将获得安全更新和错误修复支持。

- 🚀 Ember.js 6.9 版本发布，所有变更均为内部改进、文档更新或向后移植的错误修复。
- 🛡️ Ember.js 6.8 版本升级为长期支持版本，提供 54 周安全更新和 36 周错误修复。
- 🔧 Ember CLI 6.9 将 broccoli 升级至^4.0.0，以解决安全漏洞和依赖项弃用问题。
- ⚙️ 最低 Node 版本要求提升至 20.19，以支持 require(esm) 功能。
- 🙏 感谢社区贡献者的持续支持，使 Ember 项目得以不断发展。

---

### [ESLint v10.0.0-rc.0 发布 - ESLint - 可插拔的 JavaScript 代码检查工具](https://eslint.org/blog/2026/01/eslint-v10.0.0-rc.0-released/)

**原文标题**: [ESLint v10.0.0-rc.0 released - ESLint - Pluggable JavaScript Linter](https://eslint.org/blog/2026/01/eslint-v10.0.0-rc.0-released/)

ESLint v10.0.0-rc.0 已发布，这是一个包含新功能、错误修复和重大变更的主要版本预发布，旨在收集社区反馈，暂不建议用于生产环境。

- 🚀 **预发布版本**：ESLint v10.0.0-rc.0 是主要版本升级，提供新功能和错误修复，但包含重大变更，需谨慎评估。
- 🧪 **RuleTester 增强**：新增 `requireData` 断言选项，要求测试用例在消息包含占位符时提供 `data` 对象，确保测试一致性。
- 🔍 **测试调试改进**：`RuleTester` 现在在失败测试的堆栈跟踪中提供更精确的位置信息，便于快速定位问题代码行。
- ⚙️ **规则选项更新**：`max-params` 规则新增 `countThis` 选项，取代已弃用的 `countVoidThis`，用于忽略 TypeScript 函数中 `this` 注解的参数计数。
- 📦 **安装方式**：需通过 `npm i eslint@next --save-dev` 或指定版本 `eslint@10.0.0-rc.0` 安装此预发布版本。
- 📚 **迁移指南**：官方提供了详细的迁移指南，帮助用户处理重大变更，大多数用户可无构建更改升级，但建议参考指南以应对问题。
- 🐛 **错误修复与优化**：包括更新依赖、修复 `RuleTester` 错误位置报告、调整类型定义等多项修复和文档更新。

---

### [Rspack 1.7 版本发布公告 - Rspack](https://rspack.rs/blog/announcing-1-7)

**原文标题**: [Announcing Rspack 1.7 - Rspack](https://rspack.rs/blog/announcing-1-7)

Rspack 1.7 是 Rspack 1.x 系列的最后一个次要版本，专注于稳定现有功能，并为 Rspack 2.0 做准备。此版本包含多项新功能、实验性功能的稳定化，以及 Rstack 生态中多个工具的更新。

- 🛠️ **SWC 插件兼容性提升**：通过贡献兼容性改进至 SWC 社区，包括采用 CBOR 序列化方案和引入 Unknown 枚举变体，使得 SWC 版本升级时不太可能破坏基于旧版本构建的插件。
- 📦 **支持以字节形式导入资源**：原生支持 Import Bytes 提案，允许将资源作为 Uint8Array 导入，并使用 TextDecoder 进行解码。
- ⚡ **默认启用惰性编译**：在 Rspack CLI 中为动态导入的模块默认启用惰性编译，减少初始构建的模块数量，从而加快开发服务器启动速度。
- ✅ **实验性功能稳定化**：包括常量内联优化、TypeScript 枚举内联优化和类型重新导出检查在内的多项功能已通过生产验证，现视为稳定功能，相关实验性标志已被弃用或默认启用。
- 🚀 **Rstack 生态更新**：
  - **Rsbuild 1.7**：错误覆盖层支持显示运行时错误；新增资源大小差异报告功能；create-rsbuild 工具集成更多开箱即用的工具选项。
  - **Rsdoctor 1.4**：引入改进的树状图视图，帮助更直观地分析打包产物的整体构成和模块大小比例。
  - **Rslib 0.19**：ESM 输出功能稳定化，默认启用；新增 JavaScript API，支持以编程方式调用构建能力。
  - **Rstest 0.7**：引入配置适配器机制，支持直接复用现有工具配置；改进测试反馈，包括标记长时间未完成的测试用例和更清晰的超时失败信息。
  - **Rspress 2.0 RC**：引入 SSG-MD 功能，将页面渲染为 Markdown 文件，生成更高质量的静态内容，便于 AI 理解文档语义信息。
- 📋 **升级指南**：建议升级 SWC Wasm 插件至兼容 swc_core@54 或更高版本，并移除已弃用的实验性配置选项。

---

### [日期已过，时代已来 - Piccalilli](https://piccalil.li/blog/date-is-out-and-temporal-is-in/)

**原文标题**: [
  Date is out, Temporal is in  - Piccalilli
](https://piccalil.li/blog/date-is-out-and-temporal-is-in/)

JavaScript 的 Date 对象存在诸多问题，包括不一致的日期解析、时区支持有限、使用不便以及内部可变性导致的意外修改风险。这些问题促使开发社区寻求替代方案，而 Temporal 提案应运而生，旨在提供更现代、可靠且易于使用的日期时间处理方式。Temporal 通过不可变操作、清晰的 API 设计和更好的时区支持，显著改善了 JavaScript 中的日期时间处理体验。

- 📅 **Date 对象的问题**：JavaScript 的 Date 对象在日期解析上表现不一致，例如月份从 0 开始索引，而年份和日期则不是，导致开发者容易出错。
- 🌍 **时区与日历限制**：Date 仅支持本地时区和 GMT，且只遵循公历，无法处理夏令时或其他日历系统，限制了其在全球 web 应用中的使用。
- 🔧 **可变性风险**：Date 实例是可变对象，这意味着在传递或修改时可能意外改变原始值，违反了日期作为不可变真实世界概念的本质。
- 🚀 **Temporal 的解决方案**：Temporal 是一个命名空间对象，提供如 PlainDate、ZonedDateTime 等不可变类，确保操作安全且易于理解，例如通过 `add` 和 `subtract` 方法生成新对象而非修改原值。
- ⏳ **标准化进展**：Temporal 已进入标准化过程的第三阶段，并在 Chrome 和 Firefox 等浏览器中实现，允许开发者提前试用并提供反馈，以进一步完善规范。
- 📈 **性能与开发体验**：Temporal 的设计减少了对外部库的依赖，提升了性能，并通过更直观的 API（如 `Temporal.Now.plainDateISO()`）改善了开发者的编码体验。

---

### [时间性文档](https://tc39.es/proposal-temporal/docs/)

**原文标题**: [Temporal documentation](https://tc39.es/proposal-temporal/docs/)

Temporal 是 JavaScript 中用于处理日期和时间的新提案，旨在解决传统 Date 对象的诸多问题，提供更现代、易用且功能全面的 API。

- 📅 **解决 Date 对象痛点**：Temporal 旨在修复 JavaScript 中 Date 对象的长期问题，提供更清晰的日期时间处理方式。
- 🌍 **全面时区支持**：内置对所有时区的支持，包括夏令时安全的算术运算，避免时区混淆。
- 🧩 **模块化类型设计**：提供多种独立类型，如日期、时间、日期时间等，使代码更易读且减少错误。
- 📚 **详细文档与示例**：提供完整的 API 文档和实用示例，帮助开发者快速上手。
- 🔗 **字符串解析与序列化**：支持严格的字符串格式解析，并遵循 ISO 8601 等标准，确保数据一致性。
- 🗓️ **多日历系统支持**：不仅支持 ISO 8601 日历，还可处理其他日历系统，满足多样化需求。
- ⏱️ **精确时间与时长处理**：提供 Temporal.Instant 表示精确时间点，Temporal.Duration 处理时间长度，适用于复杂计算。

---

### [修复 JavaScript 日期问题——入门指南——玛吉的博客](https://maggiepint.com/2017/04/09/fixing-javascript-date-getting-started/)

**原文标题**: [Fixing JavaScript Date – Getting Started – Maggie's Blog](https://maggiepint.com/2017/04/09/fixing-javascript-date-getting-started/)

作者回归博客，分享参与修复 JavaScript Date 对象这一重要项目的经历。该项目旨在解决当前 Date 实现中的多个长期问题，并与 TC39 委员会成员合作推进。

- 🗓️ JavaScript 的 Date 对象源自 1995 年 Brendan Eich 在十天内借鉴 Java 的早期实现，该实现本身存在缺陷且早已被 Java 弃用。
- 🔍 当前 Date 的主要问题包括：缺乏时区支持、解析器不可靠、对象可变、夏令时行为不可预测、计算 API 笨拙以及不支持非公历日历。
- 🛠️ 部分问题可在现有基础上修复，例如通过新增工厂函数支持更多时区和日历，或添加更便捷的计算方法（如 addDays()）。
- 🐛 不可预测的夏令时行为被确认为 ECMA262 规范中的一个错误，计划在 ECMAScript 2018 中通过拉取请求修复。
- 🌐 但可变性和解析问题因“网络兼容性”和“网络现实”限制而难以修正，这将是后续文章讨论的重点。
- 💼 作者强调参与标准委员会并非其本职工作，而是出于对 JavaScript 和开源社区的热情，并感谢 JS 基金会和微软团队的支持。

---

### [Temporal | 我可以使用... HTML5、CSS3 等支持表格](https://caniuse.com/temporal)

**原文标题**: [Temporal | Can I use... Support tables for HTML5, CSS3, etc](https://caniuse.com/temporal)

Temporal 是一个现代 JavaScript 日期时间 API，旨在取代传统的 Date 对象，目前全球使用率约为 1.81%，其浏览器支持情况因版本而异。

- 🌐 **全球使用率**：Temporal API 的全球使用率约为 1.81%，表明它正在逐步被采用。
- 🚀 **API 目标**：该 API 旨在提供一个更现代、更强大的日期时间处理方案，以取代 JavaScript 中原有的 Date 对象。
- ✅ **浏览器支持**：在 Chrome 144-146、Firefox 139-149 及 Firefox for Android 146 等版本中已获得支持。
- ❌ **不支持或默认禁用**：许多浏览器版本（如 Safari 全系列、IE、Opera Mini 等）尚未支持或默认禁用该功能。
- 🔧 **实现状态**：各大浏览器（Chromium、WebKit、Firefox）均有相关的实现 bug 和开发进展，显示其仍在积极完善中。

---

### [Chrome 144 测试版  |  博客  |  面向开发者的 Chrome](https://developer.chrome.com/blog/chrome-144-beta#the_temporal_api)

**原文标题**: [Chrome 144 beta  |  Blog  |  Chrome for Developers](https://developer.chrome.com/blog/chrome-144-beta#the_temporal_api)

Chrome 144 Beta 版本引入了多项 CSS、Web API 及性能改进，同时宣布了多项 API 的弃用计划，主要涉及隐私沙盒相关功能。

- 🎨 CSS 锚点定位现支持变换效果，提升动态布局灵活性
- 🔍 新增 CSS 伪元素`::search-text`，允许自定义页面内搜索高亮样式
- 🖱️ `overscroll-behavior`属性现全面支持键盘滚动操作
- 🎭 View Transitions API 新增`waitUntil()`方法，支持高级滚动驱动动画
- 📍 引入`<geolocation>`元素，提供声明式地理位置获取控件
- 📋 新增`clipboardchange`事件，实现系统剪贴板内容同步监听
- ⚡ WebGPU 新增`subgroup_id`特性，优化着色器并行处理能力
- 📊 新增`performance.interactionCount`属性，助力 INP 性能指标计算
- 🚫 宣布弃用 Topics API、Protected Audience API 等隐私沙盒相关技术
- 🔧 移除 XML 解析中的外部实体加载功能，增强安全性

---

### [GitHub - js-temporal/temporal-polyfill：Temporal 的 Polyfill（建设中）](https://github.com/js-temporal/temporal-polyfill)

**原文标题**: [GitHub - js-temporal/temporal-polyfill: Polyfill for Temporal (under construction)](https://github.com/js-temporal/temporal-polyfill)

这是一个为 TC39 的 Temporal 提案提供的 polyfill 项目，旨在为 JavaScript 提供现代化的日期和时间 API，目前处于开发阶段，欢迎贡献者参与。

- 🚧 **项目状态**：正在开发中的 Temporal 提案 polyfill，目标是在提案进入 Stage 4 时可用于生产环境
- 📦 **安装使用**：通过 npm 安装`@js-temporal/polyfill`，支持 CJS 和 ESM 模块导入
- ⚠️ **版本注意**：v0.5.0 包含重大变更，需参考变更日志迁移代码
- 🛠️ **技术栈**：使用 TypeScript（85.1%）和 JavaScript（14.9%）开发，依赖 JSBI 处理 BigInt 兼容性
- 📚 **文档资源**：提供 API 参考文档和实用指南，文档正在迁移至 MDN
- 🐛 **问题反馈**：API 问题反馈至 TC39 提案仓库，polyfill 实现问题反馈至本项目
- 🤝 **贡献欢迎**：积极招募贡献者参与开发和维护，接受 PR 提交
- 📈 **项目数据**：699 星标，36 分支，36 位贡献者，采用 ISC 许可证

---

### [JavaScript 日期计算能离谱到什么程度？](https://philna.sh/blog/2026/01/11/javascript-date-calculation/)

**原文标题**: [How wrong can a JavaScript Date calculation go?](https://philna.sh/blog/2026/01/11/javascript-date-calculation/)

JavaScript 的 Date 对象在处理日期时容易因时区问题产生意外结果，例如在特定时区下进行月份加减可能导致日期错误跳转。使用 setUTC 方法可避免此类问题，而未来的 Temporal API 将提供更直观、安全的日期操作方式。

- 🗓️ JavaScript 的 Date 对象常因时区问题导致日期计算错误，例如从 2024 年 1 月 1 日加一个月可能意外得到 2023 年 3 月 4 日
- 🌍 问题根源在于 Date 同时处理日期和时间，时区转换（如 UTC 与太平洋时间差异）会引发非预期结果
- 🔧 解决方案是使用 setUTCMonth 等 UTC 专用方法，确保日期操作不受本地时区影响
- 🚀 Temporal API 将提供更优方案，通过 Temporal.PlainDate 实现纯日期操作，避免时间与时区干扰
- ⚠️ 目前 Temporal 仅支持 Firefox，开发中需注意时区陷阱，建议提前学习或使用 polyfill

---

### [管道 – WorkOS 文档](https://workos.com/docs/pipes?utm_source=cpjavascript&utm_medium=referral&utm_campaign=q12026&utm_content=no_rebuild)

**原文标题**: [Pipes – WorkOS Docs](https://workos.com/docs/pipes?utm_source=cpjavascript&utm_medium=referral&utm_campaign=q12026&utm_content=no_rebuild)

WorkOS Pipes 是一个让用户安全连接第三方账户到应用程序的服务，它简化了与流行服务（如 GitHub、Slack、Google）的集成，无需处理 OAuth 流程、令牌刷新逻辑或凭证存储。

- 🔧 **配置提供者**：在 WorkOS 仪表板的 Pipes 部分配置提供者，选择所需服务或联系团队添加未列出的提供者。
- 🛠️ **共享凭证**：在沙盒环境中使用 WorkOS 管理的共享凭证，快速设置，无需为每个提供者创建 OAuth 应用，只需指定所需范围和可选描述。
- 🔐 **自定义凭证**：为生产应用配置自己的 OAuth 凭证，包括创建 OAuth 应用、设置重定向 URI、提供客户端 ID 和密钥，并指定范围。
- 🖥️ **提供者管理**：使用 Pipes Widget 提供预建 UI，让用户连接和管理账户，显示可用提供者并处理授权流程，自动存储连接信息。
- 🔑 **获取访问令牌**：用户连接后，从后端获取访问令牌以代表用户调用 API，Pipes 自动处理令牌刷新，并在出现问题时返回错误信息以便修复。

---

### [停止把所有东西都变成数组（并减少工作量）- 马特·史密斯](https://allthingssmitty.com/2026/01/12/stop-turning-everything-into-arrays-and-do-less-work-instead/)

**原文标题**: [
    Stop turning everything into arrays (and do less work instead) - Matt Smith
  ](https://allthingssmitty.com/2026/01/12/stop-turning-everything-into-arrays-and-do-less-work-instead/)

JavaScript 开发中常因过早将数据转为数组并进行链式处理，导致不必要的计算和内存分配。迭代器助手提供了一种惰性处理方案，能按需处理数据，避免中间数组的创建和多余操作，特别适合大数据集、流式数据和 UI 渲染场景。

- 🚫 **避免不必要的数组转换**：传统数组方法如 `map`、`filter` 会创建多个中间数组，即使只需少量数据也可能处理全部条目。
- 🔄 **惰性迭代的优势**：迭代器助手（如 `filter`、`map`、`take`）仅在需要时处理数据，可提前停止，减少计算和内存占用。
- 🖥️ **优化 UI 渲染**：在处理大型列表、虚拟滚动或流式数据时，惰性迭代确保只处理实际显示的内容，提升性能。
- 📚 **原生支持无需依赖**：迭代器助手是 JavaScript 原生功能，无需第三方库即可构建清晰的数据处理管道。
- ⚠️ **使用注意事项**：迭代器为一次性消耗，不支持随机访问，调试时需注意避免意外消耗数据。
- 🛠️ **适用场景选择**：适合处理大型或流式数据，但在需要随机访问、数据量小或依赖数组突变时，传统数组方法可能更简单直观。

---

### [迭代器助手 · V8](https://v8.dev/features/iterator-helpers)

**原文标题**: [Iterator helpers · V8](https://v8.dev/features/iterator-helpers)

迭代器助手是 ECMAScript 中新增的一组迭代器原型方法，旨在简化迭代器的通用操作。这些方法适用于所有继承自 Iterator.prototype 的对象，例如数组迭代器，并通过一系列实用功能提升数据处理的灵活性和效率。

- 🔄 **.map(mapperFn)**：对迭代器中的每个值应用映射函数，返回处理后的新迭代器。
- 🎯 **.filter(filtererFn)**：根据条件函数筛选迭代器中的值，仅返回符合条件的值。
- 📥 **.take(limit)**：从迭代器中提取前 N 个值，限制输出数量。
- 📤 **.drop(limit)**：跳过迭代器中的前 N 个值，返回剩余部分。
- 🧩 **.flatMap(mapperFn)**：对每个值应用映射函数，并将结果迭代器扁平化为单一迭代器。
- 📊 **.reduce(reducer [, initialValue])**：通过归约函数累积处理所有值，返回单一结果。
- 📋 **.toArray()**：将迭代器中的所有值转换为数组。
- 🔁 **.forEach(fn)**：对每个值执行函数，主要用于副作用操作，无返回值。
- ✅ **.some(fn)**：检查是否有任意值满足条件函数，返回布尔值。
- ✔️ **.every(fn)**：验证所有值是否均满足条件函数，返回布尔值。
- 🔍 **.find(fn)**：查找并返回第一个满足条件的值，若无则返回 undefined。
- 🛠️ **Iterator.from(object)**：静态方法，将对象转换为迭代器，支持现有迭代器、可迭代对象或普通对象包装。

---

### [如何窃取任何 React 组件](https://fant.io/react/)

**原文标题**: [How to Steal Any React Component](https://fant.io/react/)

本文介绍了人工智能在医疗领域的应用现状与前景，重点探讨了其在疾病诊断、治疗方案优化及医疗管理效率提升方面的作用，并简要提及了相关的伦理挑战。

- 🤖 AI 辅助诊断系统能通过分析医学影像快速识别病灶，提高早期疾病检出率
- 💊 基于机器学习的个性化治疗方案可结合患者数据优化用药与治疗路径
- 📊 智能医疗管理平台能整合病历信息，减少行政负荷，提升医院运营效率
- ⚖️ 数据隐私与算法透明度等伦理问题仍需在技术发展中同步完善规范

---

### [GitHub - acdlite/react-fiber-architecture: React 新核心算法 React Fiber 的解析](https://github.com/acdlite/react-fiber-architecture)

**原文标题**: [GitHub - acdlite/react-fiber-architecture: A description of React's new core algorithm, React Fiber](https://github.com/acdlite/react-fiber-architecture)

React Fiber 是 React 核心算法的重新实现，旨在通过增量渲染等特性提升动画、布局和手势处理的适用性，并引入优先级调度、可中断和重用工作等能力，以优化用户体验和性能。

- 🎯 **核心目标**：增强 React 在动画、布局等领域的适用性，支持增量渲染，将渲染工作拆分为可调度的块。
- 🔄 **算法重写**：重新实现协调器（reconciler），专注于调度，而非渲染，保持与现有高阶算法兼容。
- ⏱️ **调度机制**：采用“拉取”模式，允许 React 智能决定工作优先级，避免帧丢失，提升交互响应。
- 🧱 **Fiber 单元**：作为虚拟堆栈帧，表示工作单元，支持暂停、重用、中止和优先级分配，实现更灵活的控制。
- 🌳 **结构设计**：Fiber 是包含组件类型、子节点、兄弟节点等信息的 JavaScript 对象，通过链表结构管理组件树。
- 🔗 **协调与渲染分离**：协调器计算变更，渲染器负责更新，支持多平台（如 DOM、React Native）共享协调器。
- 🚀 **未来特性**：计划涵盖工作调度算法、优先级传播、副作用处理等，以进一步提升并发能力和性能优化。

---

### [JavaScript 的 for-of 循环实际上很快 | WaspDev 博客](https://waspdev.com/articles/2026-01-01/javascript-for-of-loops-are-actually-fast)

**原文标题**: [JavaScript's for-of loops are actually fast | WaspDev Blog](https://waspdev.com/articles/2026-01-01/javascript-for-of-loops-are-actually-fast)

JavaScript 的 for-of 循环性能表现优异，与传统的索引循环速度相当，尤其在 V8 引擎持续优化下，对于大多数应用场景而言，其性能差异可忽略不计。

- 🔍 **基准测试设计**：通过 jsbenchmark.com 在 Chrome 143 环境下，测试了五种数据类型（整数、浮点数、字符串、对象、混合值）和三种数组规模（5000/50000/500000 元素）的六种循环方式性能对比。
- ⚡ **性能表现分析**：在中小型数组（5 万元素内）测试中，for-of 循环与经典的缓存长度 for 循环（i++）性能几乎持平，而 for-in 循环始终表现最差。
- 🔄 **大规模数据差异**：当数组规模达到 50 万元素时，for-of 循环在初始运行阶段性能略有下降，但经过充分预热（重复执行 1500 次）后，其性能可恢复至与经典循环同等水平。
- 🏆 **经典循环稳定性**：缓存数组长度的经典 for 循环（i++）在所有测试场景中表现最为稳定可靠，始终保持着最优或接近最优的性能表现。
- 💡 **实践建议**：对于性能敏感型代码，for-of 循环可作为可行选择，但需在实际场景中进行基准验证；在非性能关键场景中，for-of 循环因其更佳的代码可读性而值得推荐使用。

---

### [今日所学：ARM 架构为何包含 JavaScript 指令](https://notnotp.com/notes/til-why-arm-has-a-js-instruction/)

**原文标题**: [TIL: Why ARM Has a JavaScript Instruction](https://notnotp.com/notes/til-why-arm-has-a-js-instruction/)

ARM 架构为 JavaScript 的 ToInt32 操作定义了一个专用指令 FJCVTZS，用于将 Float64 转换为 Int32，并严格遵循 ECMAScript 规范处理 NaN、Infinity 和溢出值，而标准 FCVTZS 指令在这些边缘情况下行为未定义。该指令在 ARMv8.3-A 中引入，旨在优化 JavaScript 运行时中频繁的类型转换，但现代引擎已通过内部优化（如 V8 的 SMI）减少了对这类转换的依赖。

- 🏗️ ARM 的 FJCVTZS 指令专为 JavaScript 设计，将 Float64 转换为 Int32，并遵循 ECMAScript 的 ToInt32 规范处理边缘情况
- 🔄 JavaScript 使用 Float64 表示数字，但位运算和数组操作等需要 Int32，导致运行时频繁进行类型转换
- ⚠️ 标准 C 语言转换对 NaN、Infinity 和溢出值的行为未定义，而 JavaScript 规范要求明确处理这些情况
- ⚙️ 在 ARMv8.3-A 之前，JavaScript 引擎用软件处理转换；专用指令通过硬件加速提升性能
- 🖥️ x86-64 架构没有等效指令，JavaScript 引擎需用软件模拟相同行为
- 🛠️ 现代引擎如 V8 使用“小整数”（SMI）等技术内部优化，减少显式转换需求
- 🤔 尽管该指令有趣，但由于引擎优化，其实际性能影响可能有限，且 x86-64 未引入类似指令仍能高效运行 JavaScript

---

### [如何使用 lit-html 编写自定义元素——Frontend Masters 博客](https://frontendmasters.com/blog/custom-elements-with-lit-html/)

**原文标题**: [How I Write Custom Elements with lit-html – Frontend Masters Blog](https://frontendmasters.com/blog/custom-elements-with-lit-html/)

作者分享使用 lit-html 编写自定义 Web 组件的经验，强调其轻量、接近原生 JavaScript 的优势，并通过无状态与有状态渲染的两个实例展示实际应用。

- 🚀 选择 lit-html 而非完整 Lit 包，因其更轻量（约 3.1kb gzip）、无需强制使用 Shadow DOM，且语法更简洁
- 📝 无状态渲染示例：包装 `<textarea>` 并添加状态栏，通过原生事件更新内容，虽未充分利用 lit-html 性能优势，但提升了代码可读性
- 🎨 有状态渲染示例：创建 `<pokemon-card>` 组件，结合 Signals 管理状态，并集成随机生成、导航与预加载等交互功能
- 🔄 使用 Signals 处理状态，视为未来可能纳入 JavaScript 标准的方案，并搭配效果监听实现响应式更新
- 🛠️ 组件额外功能：通过 Intersection Observer 实现滚动同步、键盘导航支持，以及预加载优化用户体验

---

### [`document.currentScript` 比我想象的更有用。 – Frontend Masters 博客](https://frontendmasters.com/blog/document-currentscript-is-more-useful-than-i-thought/)

**原文标题**: [`document.currentScript` is more useful than I thought. – Frontend Masters Blog](https://frontendmasters.com/blog/document-currentscript-is-more-useful-than-i-thought/)

本文介绍了`document.currentScript`属性的实用功能，它允许非模块脚本访问自身`<script>`元素，从而通过自定义属性传递配置数据，简化脚本与 HTML 的交互。

- 📚 `document.currentScript`可获取当前执行的`<script>`元素（非模块类型）
- 🔧 通过自定义属性（如`data-*`）在脚本标签中存储配置数据
- 💡 示例：从`dataset`读取数据并动态更新页面内容
- 🚀 推荐通过 Frontend Masters 平台深入学习 JavaScript

---

### [WebAssembly 发生了什么](https://emnudge.dev/blog/what-happened-to-webassembly/)

**原文标题**: [What Happened To WebAssembly](https://emnudge.dev/blog/what-happened-to-webassembly/)

WebAssembly（Wasm）作为一种语言和编译目标，在现实世界中已得到广泛应用，例如游戏开发、图像处理、插件生态系统和代码转换等场景。它通过接近汇编语言的设计实现高效硬件映射，支持多种语言编译，并具备强大的安全性和可移植性。尽管性能受限于浏览器引擎且存在跨边界成本，但 Wasm 在安全隔离和嵌入性方面表现突出，逐渐成为连接不同语言生态的桥梁。目前，其发展主要由工具和库作者推动，对普通开发者可能不够透明，但标准化和社区进展仍在快速推进。

- 🎮 **实际应用广泛**：Godot、Figma、Squoosh 等工具利用 Wasm 实现游戏开发、代码转换和图像处理，成为其核心功能。
- 🔧 **语言与编译目标**：Wasm 是一种语言，可作为 Rust、C 等多种语言的编译目标，支持独立运行时和浏览器引擎。
- ⚡ **高效硬件映射**：设计接近汇编语言，便于高效编译，手动编写 WAT（文本格式）可实现精细控制。
- 🛡️ **安全优势显著**：通过显式导入和最小攻击面，提供进程级隔离，被 Cloudflare 等用于安全运行不受信任代码。
- 🌍 **可移植与嵌入性**：轻量级运行时支持跨平台插件生态，允许在 JavaScript 环境中集成图像处理、数据库等工具。
- 📊 **性能与尺寸权衡**：性能受浏览器引擎限制，但类型系统丰富的语言可优化效率；Zig 能生成最小二进制文件，跨边界操作可能增加成本。
- 🚀 **快速发展与争议**：社区通过 W3C 和 Bytecode 联盟推进标准化，但快速变化引发内部争议，普通开发者可能感知有限。
- 🔮 **未来展望**：Wasm 不太可能取代 JavaScript，但通过 Blazor 等框架，开发者可间接使用其能力，主要影响库和工具层。

---

### [内存实验室](https://facebook.github.io/memlab/)

**原文标题**: [memlab](https://facebook.github.io/memlab/)

概述了 Memlab 工具的使用方法，包括定义端到端测试场景、通过命令行检测内存泄漏、支持多种内存分析命令，以及编程 API 的调用方式，并提及了该工具的实际应用情况。

- 🧪 定义浏览器交互的端到端测试场景，包括设置 URL、页面操作和返回函数
- 🔍 通过命令行运行 Memlab 检测自定义测试场景中的内存泄漏
- 📊 支持多种内存分析功能，如重复字符串、未绑定对象和形状增长分析
- 💻 提供编程 API 接口，允许通过 JavaScript 代码进行堆快照和内存泄漏检测
- 🌐 提及了 Memlab 工具的实际使用者情况

---

### [MemLab：一个用于发现 JavaScript 内存泄漏的开源框架](https://engineering.fb.com/2022/09/12/open-source/memlab/)

**原文标题**: [MemLab: An open source framework for finding JavaScript memory leaks](https://engineering.fb.com/2022/09/12/open-source/memlab/)

Meta 开源了 MemLab，这是一个用于自动化检测 JavaScript 内存泄漏的测试框架，旨在帮助开发者识别和解决 Web 应用中的内存问题，以提升用户体验和性能。

- 🛠️ **开源框架**：MemLab 是 Meta 开源的 JavaScript 内存测试框架，可自动检测内存泄漏，帮助优化客户端内存管理。
- 🌐 **背景与需求**：随着 Facebook.com 等 Meta 应用转向单页应用架构，客户端内存管理变得复杂，内存泄漏虽不易察觉但会逐渐影响性能。
- 🔍 **工作原理**：通过无头浏览器运行测试场景，比较 JavaScript 堆快照，经过六步流程（如浏览器交互、堆差异分析、保留路径追踪）来定位泄漏对象。
- 📊 **功能特性**：包括内存泄漏检测、堆的图视图 API、内存断言以及内存工具箱（如对象形状分析和重复字符串检测），支持自定义泄漏过滤器。
- 📈 **应用案例**：在 Meta 内部，MemLab 帮助将 Facebook.com 的 OOM 崩溃减少 50%，并通过 React Fiber 节点清理和 Relay 字符串驻留优化显著降低内存使用。
- 🚀 **社区推广**：鼓励开发者通过 npm 安装或 GitHub 仓库使用 MemLab，并提供快速入门指南，以促进更广泛的 JavaScript 社区应用。

---

### [TimescaleDB：排名第一的 PostgreSQL 时序数据库 | 开源与云端 | Tiger Data](https://www.tigerdata.com/timescaledb?utm_source=cooperpress&utm_medium=referral&utm_campaign=javascript-weekly-newsletter)

**原文标题**: [TimescaleDB: #1 PostgreSQL Time-Series Database | Open Source & Cloud | Tiger Data](https://www.tigerdata.com/timescaledb?utm_source=cooperpress&utm_medium=referral&utm_campaign=javascript-weekly-newsletter)

TimescaleDB 是一款基于 PostgreSQL 构建的时序数据库，专为处理传感器、链上数据和客户数据等时序数据而设计，提供实时分析、高效压缩和自动分区等功能。它既可作为完全托管的云服务（Tiger Cloud）使用，也支持自托管部署，适用于物联网、金融科技和实时分析等多种场景。

- 🚀 **核心能力**：具备自动分区、行列混合存储、高达 95% 的压缩率、增量物化视图、自动化数据管理和专用时序函数，确保高性能和大规模数据处理的可靠性。
- ☁️ **云服务优势**：Tiger Cloud 提供一键式管理、自动化分层存储、独立扩展的计算与存储、高可用架构以及企业级安全合规支持，简化运维并优化成本。
- 🛠️ **灵活部署**：支持自托管（社区版/企业版），保留 PostgreSQL 的完整 SQL 和生态系统，同时允许用户自主管理基础设施，适合需要高度控制的环境。
- 📊 **应用场景**：广泛应用于物联网设备监控、加密货币与金融科技数据分析以及实时客户仪表板，帮助团队高效处理海量时序数据并快速获得洞察。
- ⭐ **客户认可**：受到 Cloudflare、Replicated 和 Julep 等企业的信赖，因其在性能、可扩展性和与 PostgreSQL 的兼容性方面表现出色。
- 🔧 **全面支持**：提供 24/7 专家协助和技术指导，涵盖从原型开发到大规模生产的全周期，确保用户能够充分利用数据库功能。

---

### [GitHub - fabricjs/fabric.js: JavaScript 画布库，SVG 转画布（及画布转 SVG）解析器](https://github.com/fabricjs/fabric.js)

**原文标题**: [GitHub - fabricjs/fabric.js: Javascript Canvas Library, SVG-to-Canvas (& canvas-to-SVG) Parser](https://github.com/fabricjs/fabric.js)

Fabric.js 是一个功能强大的 JavaScript HTML5 画布库，提供丰富的图形操作、内置形状、滤镜和跨格式支持，适用于浏览器和 Node.js 环境。

- 🎨 **功能丰富**：支持缩放、移动、旋转、倾斜、分组等交互操作，内置形状、动画、图像滤镜、渐变和画笔
- 🔄 **格式兼容**：支持 JPG、PNG、JSON 和 SVG 格式的输入输出，实现 SVG 与画布之间的双向解析
- 🌐 **跨平台支持**：兼容现代浏览器（Chrome、Firefox、Safari、Edge）和 Node.js 环境
- 📦 **安装灵活**：可通过 npm、yarn、pnpm 安装，也支持 CDN 直接引入
- ⚛️ **框架集成**：提供 React.js 和 Node.js 的快速入门示例，包含服务端渲染和图像生成功能
- 🔧 **开发完善**：采用 TypeScript 编写，包含单元测试，拥有活跃的社区和详细的贡献指南
- 📚 **资源丰富**：提供官方文档、在线演示、Stack Overflow 支持和社交媒体渠道

---

### [Ohm：适用于 JavaScript 和 TypeScript 的易用解析工具包](https://ohmjs.org/)

**原文标题**: [Ohm: a user-friendly parsing toolkit for JavaScript and Typescript](https://ohmjs.org/)

Ohm 是一个包含库和领域特定语言的解析工具包，用于解析自定义文件格式或快速构建编程语言的解析器、解释器和编译器。

- ⚙️ Ohm 基于解析表达式文法（PEG），提供类似正则表达式和上下文无关文法的语法描述形式
- 🔧 支持左递归，可自然定义左结合运算符；面向对象的语法扩展便于为现有语言添加新语法
- 🧩 采用模块化语义动作设计，实现语法与语义完全分离，提升可读性和可扩展性
- 🌐 提供在线编辑器和可视化工具，支持实时反馈与交互式解析过程演示
- 🛠️ 已应用于多个项目：包括 Shopify 主题工具、Seymour 课堂编程环境、Shadama 粒子模拟语言等
- 📚 相关学术成果涵盖增量式解析、实时编程环境语言扩展等研究方向

---

### [欧姆编辑器](https://ohmjs.org/editor/)

**原文标题**: [Ohm Editor](https://ohmjs.org/editor/)

本文介绍了人工智能在医疗领域的应用现状与前景，重点探讨了其在疾病诊断、治疗方案优化及医疗管理效率提升方面的作用，并提及了相关的伦理挑战。

- 🏥 AI 辅助诊断系统能通过分析医学影像提高早期疾病检出率
- 💊 机器学习算法可基于患者数据生成个性化治疗建议
- ⚡ 智能流程自动化有效缩短行政作业时间，减轻医护负担
- 🧠 自然语言处理技术助力从海量文献中快速提取医疗知识
- ⚖️ 数据隐私与算法透明度等伦理问题仍需建立规范框架

---

### [GitHub - DoneDeal0/superdiff：Superdiff为数组和对象提供丰富且可读的差异对比。它支持流和文件输入以高效处理大型数据集，经过实战检验，零依赖，并提供顶级性能。](https://github.com/DoneDeal0/superdiff)

**原文标题**: [GitHub - DoneDeal0/superdiff: Superdiff provides a rich and readable diff for both arrays and objects. It supports stream and file inputs for handling large datasets efficiently, is battle-tested, has zero dependencies, and offer a top-tier performance.](https://github.com/DoneDeal0/superdiff)

Superdiff 是一个高性能的 JavaScript 库，用于生成数组和对象的详细、可读的差异对比。它支持流和文件输入以高效处理大型数据集，经过实战测试，无任何依赖，并提供顶级的性能表现。

- 📊 **功能全面**：支持对象和数组的深度差异对比，包含五个核心函数：`getObjectDiff`、`getListDiff`、`streamListDiff`、`isEqual` 和 `isObject`。
- ⚡ **性能卓越**：基准测试显示，在处理大规模数据（如 10 万条目的数组或嵌套对象）时，Superdiff 的速度显著优于同类库（如 `deep-diff`、`arr-diff`）。
- 🌊 **流式处理**：独有的 `streamListDiff` 函数支持流和文件输入，专为处理超大型数据集而设计，可在服务器和浏览器环境中使用。
- 🧩 **灵活配置**：提供丰富的选项，如忽略数组顺序、按状态过滤结果、设置参考属性以识别对象更新，以及将移动视为更新等。
- 📦 **零依赖**：库本身不依赖任何外部包，确保了轻量化和安全性。
- 🆚 **竞争优势**：在功能对比中，Superdiff 在对象差异、列表差异、流式处理、移动检测和零依赖方面均表现突出。
- 🤝 **社区支持**：项目鼓励赞助，并提供高级支持选项，代码开源，欢迎问题反馈和拉取请求。
- 📚 **详细文档**：提供完整的 API 文档、使用示例和基准测试结果，便于开发者集成和使用。

---

### [GitHub - swiftwasm/JavaScriptKit：通过WebAssembly与JavaScript交互的Swift框架。](https://github.com/swiftwasm/JavaScriptKit)

**原文标题**: [GitHub - swiftwasm/JavaScriptKit: Swift framework to interact with JavaScript through WebAssembly.](https://github.com/swiftwasm/JavaScriptKit)

JavaScriptKit 是一个 Swift 框架，用于在 WebAssembly 环境中与 JavaScript 进行交互，使 Swift 开发者能够便捷地操作 JavaScript 对象、处理事件和使用异步功能。

- 🚀 **框架用途**：允许 Swift 代码在编译为 WebAssembly 后与 JavaScript 无缝交互，支持访问对象、函数和数据类型转换。
- 🌐 **核心功能**：提供创建 DOM 元素、处理事件（如点击警报）以及利用 Swift 的 async/await 处理 JavaScript Promise 的能力。
- 📚 **学习资源**：包含快速入门教程和示例代码，帮助开发者快速上手并实现“Hello World”等基础操作。
- 🤝 **开源贡献**：欢迎社区贡献，提供贡献指南和赞助选项，支持项目持续发展。
- 📊 **项目状态**：拥有 826 个星标、61 个分支，采用 MIT 许可证，主要使用 Swift 和 JavaScript 语言开发。

---

### [v1.8 | alphaTab](https://alphatab.net/docs/releases/release1_8)

**原文标题**: [v1.8 | alphaTab](https://alphatab.net/docs/releases/release1_8)

alphaTab 1.8 版本在短短一个月内发布了 17 项新功能和改进，并修复了 10 个错误，是迄今为止最快的 alpha 版本之一。此次更新涵盖了音乐符号渲染、播放器功能、Guitar Pro 兼容性增强、alphaTex 扩展以及多项性能优化和错误修复。

- 🎼 扩展小节线跨谱表显示，提升视觉引导
- 🎵 支持跨多系统连音线渲染，改善对齐效果
- 🎶 改进音符头对齐和位移，遵循更常见的排版实践
- 🎸 新增谱内和弦图显示功能
- 🔢 优化数字谱记号的连音线和破折号显示
- 👻 新增隐藏空谱表选项，优化多轨显示
- 📜 引入羊皮纸布局，优化打印和固定布局
- 🥁 支持 buzzroll 震音符号
- 🔤 增强字体配置和歌词间距自定义
- 🔢 可配置小节编号显示方式（全部/无/每系统首小节）
- 🎼 新增自定义符杠规则，支持 27 种优化规则
- 🎵 修复歌曲开头装饰音符的播放问题
- 🖱️ 新增平滑光标和滚动模式，支持自定义滚动逻辑
- 🎸 改进 Guitar Pro RSE 兼容性，增强导出功能
- 🎸 改进旧版 Guitar Pro 文件低音谱号检测
- 📝 alphaTex 新增按小节声部编写模式
- 🔧 扩展选择 API，支持自定义 UI 元素
- 🐛 修复 Monaco 编辑器诊断显示问题
- 🛠️ 改进开发游乐场，支持文件拖拽导入
- 🎨 合并效果带渲染器，减少空白并提升性能
- 📄 改用 textContent 加载 alphaTex，避免 HTML 实体转义
- 🎼 改进符杠辅助系统，提升渲染精度
- ⚠️ 运行时检测缺失的打包插件并警告
- 🎵 始终应用系统标签左侧填充，确保显示一致性
- 🖨️ 修复打印对话框中的字体显示问题
- 🎵 处理无效 BPM 值，避免播放器挂起
- 🎼 修复符杠渲染抖动问题
- 🎨 避免布局切换时的闪烁和错误显示

---

### [发布 Neo.mjs v11.20.0 版本说明 · neomjs/neo · GitHub](https://github.com/neomjs/neo/releases/tag/11.20.0)

**原文标题**: [Release Neo.mjs v11.20.0 Release Notes · neomjs/neo · GitHub](https://github.com/neomjs/neo/releases/tag/11.20.0)

Neo.mjs v11.20.0 版本标志着项目架构的重大演变，首次由 AI 作为核心架构师驱动创新，实现了“人机协作”的开发新范式。该版本在 58 小时内解决了 97 个工单，推出了门户知识库 2.0 和基于物理的神经时间线等关键功能，并通过“结构注入”等新模式使引擎原生支持 AI 驱动的深度定制。

- 🤖 **AI 晋升为核心架构师**：Gemini 3 Pro 从代码助手转变为项目核心架构师，驱动了引擎架构的适应性演变，以更好地服务于 AI 这一主要用户。
- 🧩 **引入结构注入模式**：新增 `mergeFrom` 声明式配置注入，允许通过纯配置深度定制嵌套组件树，实现了骨架与配置的解耦，使复杂 UI 更易于 AI 代理操作。
- ⚡ **展示人机协作速度**：以“陈旧矩形”竞态条件修复为例，AI 在 2 分 40 秒内完成从问题分析到架构解决方案的提交，验证了“思维速度”级的开发效率。
- 🎨 **发布神经时间线**：这是一个跨线程（应用 Worker、Canvas Worker、Service Worker）的神经网络模拟可视化功能，作为共享 Worker 架构的压力测试场，并实现了基于交通模型的物理动画。
- 🌐 **强化 Service Worker**：将其转变为可编程网络层“运行时角色”，支持通过 `preloadAssets` 等方法实现“预测性代码分割”，允许 AI 代理根据用户意图预加载资源。
- 📚 **重构门户知识库**：执行史诗工单 #8398，将 GitHub 工单深度技术上下文转化为可搜索的文档，构建了包含解析、过滤和生成高性能树状索引的数据摄取引擎。
- 🚀 **实施“零延迟”性能优化**：通过 DOM 修剪、被动监听器切换和原子批处理（如使用 `DocumentFragment`）等一系列措施，显著减少了主线程延迟。
- 🛠️ **增强基础设施与工具**：引入了通用的 ChromaDB 碎片整理工具，并将其集成到知识库上传流程中，以支持 AI 生成知识向量的高速维护。
- 📝 **完善文档与核心增强**：新增了关于声明式配置合并等指南，并为核心类库和新增功能（如 TicketCanvas、TimelineCanvas）提供了丰富的 JSDoc 文档。

---

### [GitHub - getify/monio: 最强大的 JS IO 单子实现，可能也是所有语言中最强的！](https://github.com/getify/monio)

**原文标题**: [GitHub - getify/monio: The most powerful IO monad implementation in JS, possibly in any language!](https://github.com/getify/monio)

Monio 是一个 JavaScript 库，提供异步能力的 IO Monad 及其相关工具，旨在结合函数式编程的威力与 JavaScript 的实用性和混合范式开发风格。

- 🚀 **强大的 IO Monad**：Monio 的 IO/IOx 被宣称为 JavaScript 乃至所有语言中最强大的 IO 单子实现，支持异步操作和副作用管理。
- 🔄 **异步与同步统一**：IO 单子自动处理 Promise，使得异步代码可以像同步一样编写，并在调用 `run()` 时执行。
- 📝 **Do 风格语法**：通过 `do()` 方法支持生成器语法，允许使用 `yield` 和 `await` 编写类似 `async..await` 的代码，提升可读性。
- 🛡️ **错误处理灵活**：支持常规的 Promise 异常捕获，也可通过 Either 单子进行函数式错误处理。
- 🌍 **环境读取能力**：IO 单子内置 Reader 功能，可以携带并传递副作用所需的环境数据。
- 📦 **丰富的单子集合**：除 IO 外，还提供 Maybe、Either、State 等单子，满足多种函数式编程需求。
- 🖥️ **多环境支持**：支持 Node.js 和浏览器环境，提供 CommonJS、ESM 和 UMD 多种模块格式。
- 📚 **详细文档与示例**：包含全面的使用指南、API 文档和多个在线演示，帮助开发者快速上手。
- ⚙️ **工具函数齐全**：提供如 `curry`、`fold` 等实用工具函数，辅助函数式编程开发。
- ✅ **测试与质量保障**：内置 QUnit 测试套件，支持通过 NYC 生成测试覆盖率报告，确保代码可靠性。

---

### [发布 6.2.0 版本 · ant-design/ant-design · GitHub](https://github.com/ant-design/ant-design/releases/tag/6.2.0)

**原文标题**: [Release 6.2.0 · ant-design/ant-design · GitHub](https://github.com/ant-design/ant-design/releases/tag/6.2.0)

Ant Design 发布了 6.2.0 版本，包含多项组件功能增强、问题修复和优化，提升了稳定性和用户体验。

- 🛠 多个组件（如 Button、Select 等）使用 `genCssVar` 方法生成更稳定的 CSS 变量名
- 🆕 QRCode 新增 `marginSize` 属性，用于控制二维码留白区显示
- 🆕 Tour 组件新增 `keyboard` 属性，支持键盘操作配置
- 🛠 Tooltip 增加 `maxWidth` 设计令牌，并默认支持 ESC 关闭
- 🛠 Steps 组件移除无用样式，优化代码结构
- 🆕 Form 组件新增支持 `tel` 类型校验
- 🐞 修复 Badge 组件在使用 `text` 属性时 `ref` 无效的问题
- 🆕 Calendar 和 DatePicker 的 `locale` 配置现支持部分内容填充
- 🐞 修复 ConfigProvider 中 `theme.cssVar` 对图标无效的问题
- 🐞 修复 Collapse 组件 `items` 语义化属性无效的问题
- 🆕 Modal 新增 `focusable.trap` 配置，支持焦点锁定，并优化了焦点捕获逻辑
- 🆕 ConfigProvider 新增支持 `pagination` 的 `totalBoundary` 和 `showSizeChanger` 配置
- 🆕 Drawer 新增 `focusable` 配置，支持焦点行为定制
- 🐞 修复 Drawer 的 `size` 定义不支持字符串类型的问题
- 🐞 修复 Image 嵌套在 Modal 内时，ESC 无法顺序关闭的问题
- 🆕 Pagination 新增支持 `size` 属性
- 🆕 Breadcrumb 新增支持 `dropdownIcon` 自定义
- 🆕 Checkbox.Group 新增支持 `role` 配置
- 💄 修复 Mentions 组件在不同尺寸下 `padding: undefined` 的样式问题
- 🐞 修复 Select 组件在 `size="small"` 时清除按钮对齐问题

---

### [GitHub - styled-components/xstyled：一个为React构建的实用优先CSS-in-JS框架。💅👩‍🎤⚡️](https://github.com/styled-components/xstyled)

**原文标题**: [GitHub - styled-components/xstyled: A utility-first CSS-in-JS framework built for React. 💅👩‍🎤⚡️](https://github.com/styled-components/xstyled)

xstyled 是一个基于 React 构建的实用优先的 CSS-in-JS 框架，它扩展了 styled-components，提供了一套类似 Tailwind CSS 的实用类系统，用于快速构建样式化的 React 组件。

- 🎨 **实用优先的 CSS-in-JS 框架** – 结合了 styled-components 的灵活性和实用类的高效性。
- ⚛️ **专为 React 设计** – 深度集成 React，提供声明式的样式编写方式。
- 📚 **文档齐全** – 提供详细文档和快速入门指南，包含代码示例。
- 📦 **安装简便** – 通过 npm 安装 `@xstyled/styled-components` 和 `styled-components` 即可使用。
- 🌐 **活跃社区** – 项目在 GitHub 上获得 2.3k 星标、106 个分支，被 1.2k 多个项目使用。
- 📄 **MIT 许可证** – 开源且允许自由使用和修改。
- 🔄 **持续维护** – 拥有活跃的贡献者团队，定期发布更新版本。

---

### [GitHub - sebastienros/jint: .NET 的 JavaScript 解释器](https://github.com/sebastienros/jint)

**原文标题**: [GitHub - sebastienros/jint: Javascript Interpreter for .NET](https://github.com/sebastienros/jint)

Jint 是一个用于 .NET 平台的 JavaScript 解释器，支持在安全的沙箱环境中运行 JavaScript 代码，并允许与 .NET 对象进行互操作。

- 🚀 **项目简介**：Jint 是一个 .NET 的 JavaScript 解释器，支持 .NET Standard 2.0 及更高版本，可在现代 .NET 平台上运行。
- 🛡️ **主要用途**：在 .NET 应用中安全执行 JavaScript、暴露 .NET 对象给 JavaScript 调用，以及支持应用脚本化定制。
- 📜 **许可证**：采用 BSD-2-Clause 开源许可证。
- 🌐 **用户案例**：被 RavenDB、EventStore、OrchardCore 等多个知名项目使用。
- ✅ **功能支持**：全面支持 ECMAScript 2015 至 2025 的大多数特性，包括模块、Promise、类、异步迭代等。
- ⚡ **性能特点**：不生成 .NET 字节码，小脚本执行速度快；建议缓存脚本实例并启用严格模式以提升性能。
- 🔧 **互操作性**：可直接在 JavaScript 中操作 .NET 对象、调用方法，并支持泛型类型和自定义程序集加载。
- 🌍 **国际化**：可配置时区和区域文化，以控制日期、数字的本地化格式。
- ⏳ **执行约束**：支持设置内存、执行时间、语句数等限制，并可自定义约束条件（如 CPU 使用率）。
- 📦 **模块系统**：支持 ES 模块，可从文件或代码字符串定义模块，并导出 .NET 类型和值。
- 🔒 **安全性**：提供沙箱环境，可通过内存限制、禁用 BCL、超时设置等方式确保安全执行。
- 🔄 **开发状态**：主分支为 main，通过 MyGet 持续集成，并定期发布至 NuGet。

---

### [STRICH：适用于网页应用的条形码扫描](https://strich.io/?ref=js-weekly)

**原文标题**: [STRICH: Barcode Scanning for Web Apps](https://strich.io/?ref=js-weekly)

STRICH 是一款用于网页应用的 JavaScript 条形码扫描库，支持实时 1D/2D 条形码扫描，无需原生应用或后端支持。它提供简单透明的定价、全面的文档和框架支持，适用于多种行业场景。

- 📦 **产品与文档** – 提供完整的开发资源，包括 API 参考、支持条码类型、框架集成指南和示例代码。
- 💰 **透明定价** – 采用月度/年度订阅制，无设备限制，提供免费 30 天试用，含 BASIC、PROFESSIONAL 和 ENTERPRISE 三档方案。
- 🌐 **网页应用优势** – 无需应用商店审核，易于分发，降低开发成本，支持 PWA 离线操作和推送通知。
- 🔧 **技术特性** – 基于 WebAssembly 和 WebGL，兼容所有主流浏览器，零依赖，支持 TypeScript，内置扫描 UI 和弹窗扫描器。
- 🏢 **企业级功能** – 提供白标定制、离线许可证检查、GS1 标准支持，并包含专业维护与技术支持。
- 📈 **客户案例** – 已成功应用于公共图书馆、零售、物流、医疗等多个行业，客户反馈扫描速度快、集成简便、性价比高。
- ❓ **常见问题** – 支持常见条码类型，与 Angular/Vue/React 等框架兼容，提供免费演示应用，与 ZXing-JS 等免费方案相比性能更优。

---

### [精密 AI - 无需编写测试的自动化前端测试](https://www.meticulous.ai/?utm_source=jsweekly&utm_medium=referral&utm_campaign=jan13th2026)

**原文标题**: [Meticulous AI - Automated Frontend Testing Without Writing Tests](https://www.meticulous.ai/?utm_source=jsweekly&utm_medium=referral&utm_campaign=jan13th2026)

Meticulous AI 是一款创新的自动化测试工具，通过记录用户与应用的交互来生成并维护端到端测试，无需手动编写或维护测试代码，从而帮助开发团队高效、可靠地发布无回归的代码。

- 🚀 **无需编写测试** – 通过记录用户交互自动生成测试，覆盖所有代码分支和边缘情况，无需手动编写或维护测试。
- 🔄 **测试自动演进** – 测试套件随应用更新而自动更新，新增功能时自动添加测试，旧测试失效时自动移除，保持测试套件始终最新。
- ⚡ **快速无抖动测试** – 基于 Chromium 构建的确定性调度引擎，消除测试抖动，支持大规模并行测试，可在 120 秒内完成数千次测试。
- 🛡️ **安全无副作用** – 通过记录和回放后端响应，实现无副作用的测试，无需设置测试账户或模拟数据，避免误报。
- 🌐 **广泛集成支持** – 支持 NextJS、React、Vue、Angular、Nuxt、SvelteKit 等多种前端框架，只需添加脚本标签即可快速集成。
- 📈 **提升开发效率** – 被 Dropbox、Notion、Lattice 等超过 100 家组织信任，帮助团队预防回归、增强代码信心，加速可靠代码的交付。

---

### [注册 - Auth0](https://auth0.com/signup?onboard_app=auth_for_aa&ocid=701KZ000000cXXxYAM_aPA4z0000008OZeGAM?utm_source=cooperpress&utm_campaign=amer_namer_usa_all_ciam_dev_dg_plg_auth0_native_cooperpress_native_aud_jan_2026_placements_utm2&utm_medium=cpc&utm_id=aNKWR000002m8zp4AA)

**原文标题**: [Sign Up - Auth0](https://auth0.com/signup?onboard_app=auth_for_aa&ocid=701KZ000000cXXxYAM_aPA4z0000008OZeGAM?utm_source=cooperpress&utm_campaign=amer_namer_usa_all_ciam_dev_dg_plg_auth0_native_cooperpress_native_aud_jan_2026_placements_utm2&utm_medium=cpc&utm_id=aNKWR000002m8zp4AA)

这是一个用户注册页面，提供多种注册方式并支持全球用户。

- 📧 可通过邮箱直接注册
- 🌍 支持从全球众多国家/地区中选择
- 🔐 提供第三方快速登录选项（GitHub、Google、Microsoft）
- 📄 注册需同意服务条款和隐私政策
- 🛡️ 平台提供 AI 代理安全连接、防暴力破解等安全功能
- 🆓 提供免费套餐，每月支持 2.5 万活跃用户
- ⚙️ 提供可定制的注册/登录流程和社交登录功能

---

### [连林纳斯·托瓦兹现在也在氛围编程了 | ZDNET](https://www.zdnet.com/article/linus-torvalds-vibe-coding-ai/)

**原文标题**: [Even Linus Torvalds is vibe coding now | ZDNET](https://www.zdnet.com/article/linus-torvalds-vibe-coding-ai/)

Linux 创始人 Linus Torvalds 在个人兴趣项目中尝试使用 AI 辅助编程，引发了关于代码质量与开发者技能的讨论。

- 🧑💻 Linus Torvalds 在音频处理兴趣项目中使用 Google Antigravity 生成 Python 代码，但核心 C 代码仍手动编写
- ⚠️ 氛围编程（vibe coding）指通过自然语言提示生成代码，适合非关键项目但存在严重风险案例
- 🔧 开发者社区正将 AI 用于代码维护等重复性工作，Torvalds 称 AI 是“强大的工具”但厌恶其炒作
- 🤖 主流工具如 Google Vibe Code 与微软 Windsurf 正推动自然语言编程，可能改变开发工作流程
- 💬 该实践引发对代码可维护性与开发者核心技能的担忧，Torvalds 认为需以扎实基础为前提使用

---

### [GitHub - torvalds/AudioNoise：随机数字音频效果器](https://github.com/torvalds/AudioNoise)

**原文标题**: [GitHub - torvalds/AudioNoise: Random digital audio effects](https://github.com/torvalds/AudioNoise)

这是一个关于 AudioNoise 数字音频效果处理库的 GitHub 仓库，由 Linus Torvalds 创建，主要用于学习和实验数字音频处理基础。

- 🎸 项目源于吉他效果器硬件设计，现专注于纯数字效果模拟
- 🧠 核心目标是学习数字音频处理基础知识，采用简单直接的实现方式
- ⚡ 采用“单样本输入/输出无延迟”处理模式，使用 IIR 滤波器和基本延迟循环
- 🐍 包含 Python 可视化工具，但作者自认 Python 编程经验有限
- 📜 采用 GPL-2.0 开源许可证，目前获得 3.5k 星标和 152 次复刻
- 🔧 主要编程语言为 C（53.4%）和 Python（41.3%），包含 22 次提交记录
- 🎯 强调这是“玩具级”效果，不追求商业级复杂功能，重在教育目的

---

### [npm 在动荡迁移后实施分阶段发布...](https://socket.dev/blog/npm-to-implement-staged-publishing)

**原文标题**: [npm to Implement Staged Publishing After Turbulent Shift Off...](https://socket.dev/blog/npm-to-implement-staged-publishing)

研究人员发现一款恶意 Chrome 扩展程序，专门窃取新创建的 MEXC 交易所 API 密钥，通过 Telegram 外传数据，并获取账户完全控制权以进行交易和提现操作。

- 🕵️ 恶意扩展程序针对 MEXC 交易所用户，窃取新生成的 API 密钥
- 📤 通过 Telegram 渠道将窃取的密钥数据外传至攻击者
- 💸 攻击者可完全控制账户，获得交易和资金提现权限
- ⚠️ 该威胁由 Kirill Boychenko 于 2026 年 1 月 12 日披露

---

### [2025 年度回顾 | Astro](https://astro.build/blog/year-in-review-2025/)

**原文标题**: [2025 year in review | Astro](https://astro.build/blog/year-in-review-2025/)

本文回顾了 Astro 在 2025 年的发展，重点介绍了项目健康指标、新功能、相关项目及未来展望。Astro 在 2025 年取得了显著增长，GitHub 星标数超过 55,000，npm 周下载量增长至 90 万以上，并在多项开发者调查中受到高度评价。新功能包括实时内容集合、响应式图片、字体 API、会话 API、内容安全策略等，同时 Starlight 文档主题和 Astro 生态持续壮大。2026 年，Astro v6 即将发布，预计带来路由缓存等新特性。

- 🚀 **项目健康指标亮眼**：GitHub 星标超 55,000，npm 周下载量达 90 万，在 Stack Overflow 调查中受 62.2% 开发者喜爱。
- 🆕 **新功能丰富实用**：推出实时内容集合、响应式图片优化、字体 API、会话 API 和内容安全策略等实验性功能。
- 📚 **Starlight 主题蓬勃发展**：支持 Cloudflare、Google 等大型文档站点，拥有 50 多个社区插件和 10K+ 活跃项目。
- 🤝 **生态合作与赞助增强**：Cloudflare、Netlify 等公司提供赞助，并推出 Astro 代理商合作计划，促进项目可持续发展。
- 🔮 **展望 2026 与 Astro v6**：即将发布 v6 版本，重点改进路由缓存和追踪钩子，进一步提升开发体验与性能。

---

### [Markdown 如何征服世界——阿尼尔·达什](https://www.anildash.com/2026/01/09/how-markdown-took-over-the-world/)

**原文标题**: [How Markdown took over the world - Anil Dash](https://www.anildash.com/2026/01/09/how-markdown-took-over-the-world/)

Markdown 作为一种简单的纯文本格式，由 John Gruber 于 2004 年创建，最初旨在简化博客写作中的 HTML 格式问题。它凭借直观的语法和易用性，迅速从博客圈扩散至整个科技行业，如今已成为从日常笔记、协作工具到尖端 AI 系统提示工程的通用格式。其成功源于解决了真实需求、建立在现有行为之上、拥有活跃社区支持，并以开放免费的方式分享，体现了互联网早期开放协作的精神。

- 📝 Markdown 由 John Gruber 在 2004 年创建，初衷是让博客作者能轻松地用简单符号（如 `#`、`**`）替代复杂 HTML 来格式化文本。
- 🍎 Gruber 的博客 Daring Fireball 专注报道苹果公司，其成功与苹果的崛起同步，为 Markdown 的传播提供了平台。
- 🤝 青少年 Aaron Swartz 作为关键测试者，帮助打磨 Markdown，使其在发布前就变得稳健灵活。
- 🌐 Markdown 迅速超越博客领域，被 Google Docs、Microsoft Notepad、Slack、Discord 及 Apple Notes 等主流应用采纳。
- 💻 在开发者世界中，Markdown 成为 GitHub 等平台的标准文档格式，几乎每个代码库都包含 README.md 文件。
- 🧠 如今，最先进的 AI 系统（如 ChatGPT、Claude）也使用 Markdown 文件来编写和控制复杂的提示工程。
- 🆓 Markdown 始终免费开放，没有专利限制，这种开放精神是其得以广泛普及和改编（如 CommonMark、GitHub Flavored Markdown）的基础。
- 🔧 其成功可归因于十大因素：出色的品牌名称、解决真实痛点、基于现有行为、借助社区力量、允许不同“风味”变体、在行为变革期发布、契合开发者工作流、支持“查看源代码”理念以及无知识产权束缚。
- ✨ Markdown 的故事象征着互联网的初心：普通人出于热情创造好东西并免费分享，最终惠及全球，而非仅由商业巨头驱动。

---

### [HTML 2025 现状](https://2025.stateofhtml.com/en-US/)

**原文标题**: [State of HTML 2025](https://2025.stateofhtml.com/en-US/)

2025 年 HTML 现状调查展示了 Web 平台的快速发展，涵盖了表单、图形、性能、设备 API 交互和可访问性等多个领域，旨在帮助开发者了解行业趋势和共同挑战。

- 📊 调查覆盖了 Web 平台的多个关键领域，包括表单、图形和性能等
- 🔄 由 Lea Verou 设计并更新，今年特别关注了对开发者痛点的深入分析
- 🌐 新增了分类数据和原始回答的搜索功能，便于深入挖掘
- 🤝 由 Google Chrome 团队等合作伙伴支持，提供开发资源和就业机会
- 📧 提供邮件订阅服务，方便开发者获取未来调查通知
- 🌍 支持多语言翻译，包括中文、日语、韩语等十几种语言

---

### [验证 deno 的 PyPI 分发 · Issue #31254 · denoland/deno · GitHub](https://github.com/denoland/deno/issues/31254)

**原文标题**: [verify pypi distribution of deno · Issue #31254 · denoland/deno · GitHub](https://github.com/denoland/deno/issues/31254)

Deno 项目在 PyPI 上存在一个非官方发布的包，社区成员建议官方审查或合作以确保其可靠性。

- 🔍 **非官方发布** – 有用户在 PyPI 上发现了名为 "deno" 的包，但该发布并非由 Deno 官方团队管理。
- 🤝 **社区建议合作** – 提出者认为此举能让 Deno 在更多场景中被使用，但希望官方能参与审查或协作，以保障项目的规范性和安全性。
- 📦 **包信息参考** – 相关链接指向 PyPI 上的 deno 包以及与之关联的 GitHub 仓库 `manzt/denop`。
- 🏷️ **问题标签** – 该议题被标记为 "build"，属于构建系统或持续集成相关的内容。
- ✅ **议题状态** – 该问题已被关闭，编号为 #31254 和 #31799。

---

### [未找到标题](https://x.com/bunjavascript/status/2010933884196962724)

**原文标题**: [No title found](https://x.com/bunjavascript/status/2010933884196962724)

由于 JavaScript 未启用，当前浏览器无法正常使用 x.com 平台。  
- 🔧 请启用 JavaScript 或切换至支持的浏览器以继续访问。  
- 🌐 可在帮助中心查看支持的浏览器列表。  
- 🛡️ 部分隐私相关扩展可能导致问题，建议暂时禁用后重试。  
- 📜 页脚包含服务条款、隐私政策及版权信息等链接。

---

