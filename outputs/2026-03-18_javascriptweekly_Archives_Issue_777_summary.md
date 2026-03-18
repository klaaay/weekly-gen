### [JavaScript 周刊第 777 期：2026 年 3 月 17 日](https://javascriptweekly.com/issues/777)

**原文标题**: [JavaScript Weekly Issue 777: March 17, 2026](https://javascriptweekly.com/issues/777)

本期 JavaScript 周刊聚焦于 JavaScript 生态的重要更新与工具发布，包括 Temporal API 的进展、Vite 8.0 发布、多项框架更新以及开发实践分享。

- 🗓️ **Temporal API 接近完成**：历经 9 年开发，旨在彻底解决 JavaScript 中日期时间处理的混乱问题，目前支持度持续增长，仅 Safari 和 Node.js 尚未跟进。
- 🤖 **AI 自动化测试工具 Meticulous**：由前 Palantir 工程师开发，可自动创建并维护端到端 UI 测试套件，已被 Notion、Dropbox 等公司采用，实现零开发投入的全面测试覆盖。
- ⚡ **Vite 8.0 正式发布**：作为一次重大升级，默认集成 Rolldown 替代 Rollup 和 esbuild，移除 Babel 依赖，支持 Wasm SSR 和浏览器控制台转发至终端，性能显著提升。
- 🧩 **VoidZero 开源 Vite+ 工具链**：原计划商业化的项目，现以 alpha 版本开源，整合 Vite、Vitest、Oxlint 等工具为统一开发套件。
- 📋 **TC39 会议提案进展**：包括 Temporal、Import Text、Error Stack Accessor 和 Iterator Includes 等提案获得推进，同时出现 BigInt.PI=3 的趣味提案。
- 🎉 **Vue.js 阿姆斯特丹大会亮点**：宣布 Vue Router 5、Vite 8 及 Void Cloud 等新动态，Vue 3.6.0 Beta 8 同步发布。
- 🔧 **多项重要版本更新**：Electron 41.0 增强跨平台支持，Nitro v3 Beta 扩展 Vite 应用服务端能力，Vitest 4.1 适配 Vite 8，Preact、Prisma、Babel 等均有新版本。
- 📚 **开发实践深度解析**：涵盖 Source Maps 标准化进程、利用 LLM 两周内将 13 万行 React 代码迁移至 Svelte 的经验、前端内存泄漏实证研究，以及 TypeScript 重写旧库的案例。
- 🛠️ **新工具与框架发布**：Nuxt 4.4 强化全栈 Vue 开发，Reveal.js 6.0 改用 Vite 并推出 React 包装器，RedwoodSDK 1.0 成为 Cloudflare 原生 React 框架，Defuddle 等工具更新提升开发效率。
- 🌐 **生态周边动态**：包括《纽约时报》单页加载 49MB 数据的性能反思、基于语法的代码对比工具 Difftastic、VS Code 改为每周稳定版发布节奏，以及 AWS S3 存储服务迎来 20 周年。

---

### [《时间之旅：修复 JavaScript 中时间问题的九年征程》| 彭博社 JS 博客](https://bloomberg.github.io/js-blog/post/temporal/)

**原文标题**: [Temporal: The 9-Year Journey to Fix Time in JavaScript | Bloomberg JS Blog](https://bloomberg.github.io/js-blog/post/temporal/)

本文概述了 JavaScript 中新的日期时间 API——Temporal 的九年发展历程，从旧 Date 对象的缺陷、社区努力到最终标准化，展示了跨公司合作如何解决长期痛点。

- 🕰️ **JavaScript Date 对象的历史遗留问题**：源于 1995 年对 Java Date 的直接移植，存在可变性、月份计算不一致、解析歧义等设计缺陷，随着 Web 应用复杂化成为开发痛点。
- 📚 **库时代的临时解决方案**：Moment.js 等库虽缓解问题，但带来了包体积膨胀、维护负担等新挑战，促使社区寻求标准化解决方案。
- 🤝 **Temporal 提案的跨公司协作**：由微软、彭博、Google、Igalia 等公司工程师组成的 TC39 委员会推动，历经多年需求梳理、设计迭代与引擎实现合作。
- 🛠️ **Temporal 的核心设计优势**：提供不可变、显式时区与日历支持、纳秒级精度的时间类型（如 ZonedDateTime、Instant），彻底解决 Date 的常见陷阱。
- 🌍 **国际化与日历支持**：内置多日历系统（如希伯来历），支持跨文化日期运算，避免传统 Date 仅支持公历的局限性。
- ⚙️ **实现挑战与创新协作**：作为 ECMAScript 史上最大提案，通过跨引擎共享库 temporal_rs（Rust 实现）降低实现门槛，提升代码质量与维护性。
- 🚀 **标准化与浏览器支持**：2026 年 3 月达到 TC39 Stage 4，已登陆 Firefox、Chrome、Edge 等主流浏览器，TypeScript 6.0 同步支持。
- 🔮 **未来生态整合方向**：需与日期选择器、DOMHighResTimeStamp 等 Web API 深度集成，进一步取代 Date 在生态中的使用场景。
- 🌟 **社区协作的里程碑意义**：Temporal 不仅提供了现代日期时间 API，更证明了 JavaScript 社区通过开放合作能系统性解决长期技术债务。

---

### [Temporal - JavaScript | MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal#background_and_concepts)

**原文标题**: [Temporal - JavaScript | MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal#background_and_concepts)

Temporal 是 JavaScript 中用于处理日期和时间的新 API，旨在完全替代传统的 Date 对象。它提供了更强大和灵活的功能，包括内置时区支持、多种日历系统、精确的时间点表示以及不可变对象设计，解决了 Date 对象在时区处理、日历支持和易用性方面的诸多缺陷。

- 🕐 **替代 Date 对象**：Temporal 设计为 Date 的全面替代品，解决了 Date 的时区局限性和日历单一性问题。
- 🌍 **时区与日历支持**：内置支持多种时区和日历系统（如公历、农历等），允许处理无时区的日历日期和挂钟时间。
- 🧩 **模块化 API 结构**：通过多个类（如 Instant、ZonedDateTime、PlainDate 等）分别处理时间点、时区日期、日历日期等不同场景。
- 🔧 **不可变与静态方法**：所有 Temporal 对象不可变，避免副作用；API 通过静态方法调用（类似 Math 对象），而非构造函数。
- 📅 **日历概念详解**：支持多种日历类型（太阳历、太阴历、阴阳历），提供年、月、日、周等多维度属性，并强调正确使用 era、monthCode 等属性。
- ⚙️ **丰富的操作方法**：包括时间算术（加减、比较）、舍入、序列化（RFC 9557 格式）以及类之间的转换。
- 📏 **时间范围限制**：所有日期时间对象限制在约 ±10^8 天的范围内（约 -271821 年至 +275760 年），确保转换一致性。
- 🛠️ **工具类补充**：提供 Duration 表示时间间隔，Now 获取当前时间，以及完整浏览器兼容性信息（目前非基线功能）。

---

### [Moment.js | 首页](https://momentjs.com/)

**原文标题**: [Moment.js | Home](https://momentjs.com/)

Moment.js 是一个用于在 JavaScript 中解析、验证、操作和显示日期与时间的库，提供丰富的格式化、相对时间计算和多语言支持，但项目已进入维护状态，建议考虑现代替代方案。

- 📅 **日期时间处理** – 解析、验证、操作和显示日期与时间
- 📦 **多种安装方式** – 支持 npm、Yarn、spm、Meteor 和 Bower 安装
- 🎨 **灵活格式化** – 提供多种日期时间格式化和自定义选项
- ⏳ **相对时间显示** – 支持 fromNow() 和 calendar() 等相对时间功能
- 🌍 **多语言支持** – 包含全球众多语言和地区设置
- ⚠️ **项目状态提示** – 已进入维护阶段，建议考虑现代替代方案
- 📜 **MIT 许可证** – 开源且可自由分发使用

---

### [时间性文档](https://tc39.es/proposal-temporal/docs/)

**原文标题**: [Temporal documentation](https://tc39.es/proposal-temporal/docs/)

Temporal 是 JavaScript 新的日期时间 API，旨在解决传统 Date 对象的长期问题，提供更直观、安全且功能丰富的日期时间处理能力。

- 📅 解决 Date 对象痛点，提供现代化日期时间 API
- 🌍 原生支持所有时区，包括夏令时安全计算
- 🗓️ 支持非公历日历系统
- 🔗 提供日期、时间、时区等分离的专用类
- 📚 包含详细使用指南和 API 文档
- ⏱️ Temporal.Now 提供当前系统时间相关方法
- 🕐 Temporal.Instant 表示精确时间点
- 🌐 Temporal.ZonedDateTime 结合时区和日历的日期时间
- 📆 Temporal.PlainDate 表示纯日历日期
- 🕰️ Temporal.PlainTime 表示纯时钟时间
- ⏳ Temporal.Duration 表示时间长度，用于计算
- 🔄 提供时间平衡和时区处理机制

---

### [Temporal | 我能用... HTML5、CSS3 等支持表格吗](https://caniuse.com/temporal)

**原文标题**: [Temporal | Can I use... Support tables for HTML5, CSS3, etc](https://caniuse.com/temporal)

Temporal 是一个现代日期时间 API，旨在取代 JavaScript 原有的 Date API，目前全球浏览器支持率约为 64.32%，但各浏览器版本支持情况差异较大。

- 🌐 Temporal API 全球使用率约为 64.32%，旨在替代传统的 Date API
- ✅ Chrome 从版本 144 开始支持，Edge 从版本 144 开始支持
- 🚫 Safari 目前所有版本均不支持，Firefox 从版本 139 开始支持
- 📱 移动端浏览器支持有限，如 Chrome for Android 145+ 和 Firefox for Android 147+ 支持
- 🔧 相关资源包括入门博客、各浏览器实现追踪和修复 Date 问题的讨论

---

### [精密 AI——无需编写测试的自动化前端测试](https://www.meticulous.ai?utm_source=jsweekly&utm_medium=referral&utm_campaign=26q1&utm_content=primary)

**原文标题**: [Meticulous AI - Automated Frontend Testing Without Writing Tests](https://www.meticulous.ai?utm_source=jsweekly&utm_medium=referral&utm_campaign=26q1&utm_content=primary)

Meticulous AI 是一款创新的自动化测试工具，通过记录用户与应用的日常交互，利用 AI 生成持续演进的测试套件，覆盖所有代码分支和用户流程，从而实现无需编写、修复或维护测试，帮助开发团队快速、可靠地发布无回归代码。

- 🎯 **自动化测试生成**：通过记录开发、预演和生产环境中的用户交互，AI 自动生成全面覆盖代码和用户流程的测试套件。
- ⚡ **高效无维护**：测试套件随应用演进自动更新，无需人工干预，消除测试维护负担，显著提升开发速度。
- 🛡️ **零误报与高稳定性**：内置确定性调度引擎，从底层消除测试波动，确保测试结果稳定可靠，无虚假失败。
- 🔗 **无缝集成**：轻松与现有测试套件结合或完全替代，支持主流前端框架（如 React、Vue、Angular），快速部署。
- 🌟 **企业级信任**：已被 Dropbox、Notion 等超过 100 家组织采用，开发者赞誉其能彻底改变测试流程，提升代码质量。

---

### [Vite 8.0 正式发布！ | Vite](https://vite.dev/blog/announcing-vite8)

**原文标题**: [Vite 8.0 is out! | Vite](https://vite.dev/blog/announcing-vite8)

Vite 8.0 正式发布，采用 Rust 编写的 Rolldown 作为统一构建工具，带来高达 10-30 倍的构建速度提升，同时保持插件兼容性，并引入了多项新功能与优化。

- 🚀 **性能飞跃**：Vite 8 集成 Rolldown 作为单一 Rust 构建工具，生产构建速度提升 10-30 倍，并保持与现有 Vite/Rollup 插件的完全兼容。
- 🌐 **生态扩展**：推出 registry.vite.dev 插件目录，方便开发者查找适用于 Vite、Rolldown 和 Rollup 的插件，每日同步 npm 数据。
- 🔧 **开发体验升级**：内置开发工具（devtools）、支持 TypeScript 路径别名（resolve.tsconfigPaths）、自动 emitDecoratorMetadata 支持，以及 SSR 环境下的 WebAssembly 支持。
- ⚡ **实际性能提升**：多家公司实测生产构建时间大幅减少，如 Linear 从 46 秒降至 6 秒，Beehiiv 减少 64%。
- 🛠️ **工具链统一**：Vite 8 与 Rolldown、Oxc 编译器深度集成，形成端到端工具链，确保从解析到压缩的整个流程行为一致。
- 📦 **安装包增大**：由于 lightningcss 成为默认依赖及 Rolldown 二进制文件优化，Vite 8 安装体积比 Vite 7 增加约 15 MB。
- 🔄 **平滑迁移**：提供兼容层自动转换现有配置，建议大型项目先通过 rolldown-vite 包在 Vite 7 上测试，再升级至 Vite 8。
- 🙏 **致谢社区**：感谢 Rollup 和 esbuild 的历史贡献，以及早期测试者和框架团队（如 SvelteKit、Astro、Nuxt）的反馈与支持。
- 🔮 **未来展望**：正在开发实验性全打包模式、原始 AST 传输、原生 MagicString 转换，并致力于稳定环境 API。

---

### [卷下](https://rolldown.rs/)

**原文标题**: [Rolldown](https://rolldown.rs/)

Rolldown 是一款基于 Rust 开发的新一代开源 JavaScript 打包工具，旨在提供高性能、兼容 Rollup 生态并支持 Vite 8+ 的下一代统一打包方案。

- 🚀 **高性能 Rust 内核**：基于 Rust 构建，可高效处理数万模块，打包速度显著优于传统工具
- 🔌 **Rollup 生态兼容**：提供与 Rollup 兼容的 API 和选项，支持丰富的插件生态系统
- ⚡ **esbuild 功能对标**：内置代码转换、注入、压缩、CSS 打包等现代化构建功能
- 🧩 **Vite 深度集成**：作为 Vite 8+ 的默认打包工具，提供统一的构建体验
- 🆓 **完全开源免费**：由专业团队和开源社区共同维护，可自由使用和贡献
- 📦 **现代化打包方案**：针对 JavaScript 项目优化，解决现代前端开发的构建需求

---

### [Vite+ Alpha 发布公告 | VoidZero](https://voidzero.dev/posts/announcing-vite-plus-alpha)

**原文标题**: [Announcing Vite+ Alpha | VoidZero](https://voidzero.dev/posts/announcing-vite-plus-alpha)

Vite+ Alpha 是一款开源、统一的下一代 Web 应用开发工具链，集成了 Vite、Vitest、Oxlint、Oxfmt、Rolldown 和 tsdown 等工具，通过 Vite Task 任务运行器管理开发、测试、构建等全流程，并支持自动管理 Node.js 和包管理器，旨在简化配置、提升性能。

- 🚀 **统一工具链**：整合 Vite、Vitest、Oxlint 等工具，通过单一配置文件和命令覆盖开发、测试、构建全流程。
- ⚡ **极致性能**：基于 Rust 工具链，生产构建速度提升 1.6–7.7 倍，代码检查与格式化速度最高提升 100 倍。
- 🔧 **简化开发**：通过 `vp` 命令统一管理项目创建、依赖安装、开发服务器、代码检查等操作，减少配置复杂度。
- 📦 **智能任务管理**：Vite Task 支持依赖感知的任务执行、自动化缓存和输入跟踪，提升 monorepo 工作效率。
- 🌍 **开源免费**：采用 MIT 许可证完全开源，兼容 React、Vue、Svelte 等主流框架生态。
- 🛠️ **轻松迁移**：提供 `vp migrate` 迁移工具和详细指南，支持从现有项目平滑过渡到 Vite+。

---

### [TC39 将 Temporal 推进至第四阶段，同时多项 ECMAScript 提案取得进展...](https://socket.dev/blog/tc39-advances-temporal-to-stage-4)

**原文标题**: [TC39 Advances Temporal to Stage 4 Alongside Several ECMAScri...](https://socket.dev/blog/tc39-advances-temporal-to-stage-4)

自 2026 年 1 月 31 日起，研究人员发现至少 72 个新的恶意 Open VSX 扩展，这些扩展通过传递依赖链传播 GlassWorm 恶意软件，主要针对开发者群体。

- 🕵️ 恶意扩展数量增加：新发现至少 72 个恶意 Open VSX 扩展，与 GlassWorm 攻击活动相关
- 🔗 利用传递依赖：攻击者通过依赖链间接加载恶意代码，增加检测难度
- 👨‍💻 目标明确：主要针对软件开发人员，利用其开发环境进行渗透
- 📅 活跃时间：活动至少从 2026 年 1 月 31 日开始持续进行
- 🛡️ 安全威胁：这些扩展可能窃取代码、凭证或植入后门，危害开发安全

---

### [GitHub - tc39/proposal-import-text: TC39 关于导入文本的提案 · GitHub](https://github.com/tc39/proposal-import-text)

**原文标题**: [GitHub - tc39/proposal-import-text: A TC39 proposal for importing text · GitHub](https://github.com/tc39/proposal-import-text)

该提案旨在为 JavaScript 引入导入文本文件的功能，通过新增`type: "text"`导入属性，使开发者能够像导入 JSON 模块一样直接导入文本文件为字符串，从而简化常见操作并提升性能。

- 📄 提案目标：为 JavaScript 添加导入文本文件的功能，使其像导入 JSON 一样简便
- 🔧 解决方案：新增`type: "text"`导入属性，允许将文本文件作为字符串导入
- 🚀 当前进展：提案已进入 Stage 3，由 Eemeli Aro 主导，得到 Jordan Harband 和 Nicolò Ribaudo 的评审
- 📈 现有方案对比：相比 Fetch API，该提案支持同步导入、基于模块路径解析，且加载时机更早
- 🌍 生态支持：Deno 和 Bun 等运行时已实现类似功能，HTML、Fetch 和 CSP 标准也在同步更新
- ⚠️ 已知限制：不支持指定编码，需通过`type: "bytes"`导入后手动解码处理
- 📚 相关资源：包含规范文档、测试用例及演示材料，代码托管于 GitHub

---

### [GitHub - tc39/proposal-error-stack-accessor: ECMAScript 提案、规范及 Error.prototype.stack 访问器的参考实现 · GitHub](https://github.com/tc39/proposal-error-stack-accessor)

**原文标题**: [GitHub - tc39/proposal-error-stack-accessor: ECMAScript Proposal, specs, and reference implementation for Error.prototype.stack accessor · GitHub](https://github.com/tc39/proposal-error-stack-accessor)

该提案旨在标准化 JavaScript 中 Error 对象的 stack 属性，提供一个访问器来获取和设置错误堆栈信息，同时考虑安全性和现有浏览器行为的兼容性。

- 📜 **提案目标**：标准化 Error.prototype.stack 属性，使其成为语言规范的一部分，同时确保实现的安全性和兼容性。
- 🔄 **历史背景**：从“Error Stacks”提案中分离出来，专注于现有 stack 属性的标准化，避免引入新的 API。
- ⚙️ **访问器设计**：包含 getter 和 setter，其中 setter 主要用于 Web 兼容性，对非 Error 对象或无效输入有特定处理逻辑。
- 🛡️ **安全考虑**：旨在解决标准化堆栈跟踪时可能引发的安全问题，确保实现既能符合规范又提供安全保证。
- 📄 **规范状态**：目前处于 TC39 流程的第二阶段，包含详细的规范文档和参考实现。
- 🌐 **命名固定**：Error.prototype.stack 名称已为 Web 事实标准，不可更改。
- 🔗 **资源链接**：提供规范 HTML 渲染、代码仓库及相关贡献指南，采用 MIT 许可证。

---

### [GitHub - tc39/proposal-iterator-includes: 适用于迭代器的 Array.prototype.includes 方法 · GitHub](https://github.com/tc39/proposal-iterator-includes)

**原文标题**: [GitHub - tc39/proposal-iterator-includes: Array.prototype.includes but for iterators · GitHub](https://github.com/tc39/proposal-iterator-includes)

该提案旨在为 JavaScript 迭代器添加一个 `includes` 方法，用于检查迭代器是否包含特定值，功能类似于 `Array.prototype.includes`。

- 🔍 **动机**：提供一种简洁、标准的方法来检查迭代器是否包含某个值，避免使用 `some` 方法配合自定义比较器带来的表达不直接和选择困难。
- ⚖️ **比较操作**：采用与 `Array.prototype.includes` 相同的 SameValueZero 比较算法，确保一致性。
- 📍 **参数设计**：包含第二个参数 `fromIndex` 以指定搜索起始位置，但不同于数组方法，不支持负偏移量。
- 🛠️ **实现方案**：在 `Iterator.prototype` 上添加 `includes` 方法，示例显示其基本用法和与 `drop` 方法的配合效果。
- 📊 **提案状态**：目前处于 TC39 流程的第 2.7 阶段，已有规范文档和向委员会提交的演示。

---

### [GitHub - qntm/proposal-bigint-constants：ECMAScript 提案：用于数学的大整数常量 · GitHub](https://github.com/qntm/proposal-bigint-constants)

**原文标题**: [GitHub - qntm/proposal-bigint-constants: ECMAScript Proposal: BigInt constants for mathematics · GitHub](https://github.com/qntm/proposal-bigint-constants)

该提案旨在为 ECMAScript 的 BigInt 类型引入数学常量，以对称于 Math 对象中已有的浮点数常量，但实际提供的 BigInt 常量值仅为粗略近似（如 BigInt.PI = 3），并借此幽默地呼吁完善 BigInt 的内置方法（如 BigInt.abs()）。

- 📜 提案为 BigInt 类型添加数学常量（如 BigInt.PI），以匹配 Math 对象中现有的浮点数常量
- 🤔 提供的 BigInt 常量值仅为整数近似（例如π取值为 3），实际数学意义有限
- 😅 作者通过夸张的示例调侃当前 BigInt 功能缺失，并呼吁增加 BigInt.abs() 等基础方法
- 🔄 提案处于 Stage 0 阶段，由开发者 qntm 在 GitHub 上维护，目前关注度较低（12 个星标）

---

### [Vue 与 Vite 2026 年现状：阿姆斯特丹回顾](https://laurentcazanove.com/blog/state-of-vue-vite-2026-amsterdam-recap)

**原文标题**: [State of Vue & Vite 2026: Amsterdam recap](https://laurentcazanove.com/blog/state-of-vue-vite-2026-amsterdam-recap)

2026 年 Vue.js 阿姆斯特丹大会总结了 Vue 及 Vite 生态系统的重要进展，涵盖框架更新、性能优化和新工具发布。

- 🚀 Nuxt 4.4 发布，集成 Vue Router 5 并全面提升开发体验与性能
- 💨 Vue 3.6 推出 Vapor 模式测试版，通过消除虚拟 DOM 提升应用性能
- 🔄 Vue Router 5.0 作为内部更新版本，整合了 unplugin-vue-router 功能
- ⚡ Vite 8 采用 Rust 编写的 rolldown 替代 Rollup，带来显著的性能提升
- 🧰 Vite+ 开源工具链发布，整合构建、检查、测试等前端开发全流程功能
- ☁️ Void Cloud 云服务平台推出，为 Vite 应用提供全栈部署解决方案

---

### [VueJS 阿姆斯特丹](https://vuejs.amsterdam/)

**原文标题**: [VueJS Amsterdam](https://vuejs.amsterdam/)

VueJS Amsterdam 2026 是规模最大且最具特色的 Vue.js 会议，将于 3 月 12 日至 13 日在阿姆斯特丹剧院举行，预计吸引来自 50 多个国家、437 家公司的 1098 名 Vue 爱好者参与。会议包含 25 场专业演讲，涵盖 Vue、Vite、Nuxt 等核心生态更新，并提供现场直播、全天餐饮、交流派对等丰富体验。

- 🗓️ **会议信息**：VueJS Amsterdam 2026 将于 3 月 12 日至 13 日在阿姆斯特丹剧院举办，设有 25 场演讲，预计 1098 人参与，提供门票与直播选项。
- 🎤 **核心演讲者**：包括 Vue/Vite 创始人尤雨溪（Evan You）、Vue 核心团队成员 Guillaume Chau、Pinia 创作者 Eduardo 等，分享 Vue、Nuxt、Astro 等最新动态。
- 🌍 **多元议题**：涵盖 AI 工作流、性能优化、本地优先应用、可访问性、安全风险等前沿主题，聚焦 Vue 生态实践与创新。
- 🏢 **赞助与支持**：会议提供企业赞助机会，涵盖品牌曝光、招聘推广，并获多家技术公司支持。
- 🎪 **独特体验**：会场配备 500 平方米巨幕、影院式座位、工作站、全天餐饮及交流派对，兼顾学习与社交。
- 🚀 **社区影响**：自 2018 年起连续售罄，汇聚全球 Vue 开发者、框架创作者与核心团队，是年度核心社区活动。

---

### [虚空](https://void.cloud/)

**原文标题**: [Void](https://void.cloud/)

Void 是一个专为 Vite 设计的全栈部署平台，提供内置后端服务和 AI 原生功能，旨在实现极速部署和开发体验。

- 🚀 **一键部署生产**：通过`void deploy`命令自动构建应用、运行迁移、配置资源并完成部署
- 🔧 **全栈功能内置**：集成数据库、KV 存储、对象存储、AI 推理、身份验证、队列和定时任务等后端服务
- 📁 **代码即基础设施**：自动扫描源代码并配置所需资源，无需手动配置文件或控制台操作
- 🌐 **高性能可靠**：基于 Cloudflare 全球网络构建，保障应用快速、安全且高可用
- ⚙️ **多框架支持**：兼容 React、Vue、Svelte、Solid 等 Vite 生态框架，支持 SSR、SSG、ISR 等多种渲染模式
- 🤖 **AI 原生集成**：内置技能和 MCP 支持，可通过智能代理快速搭建和部署全栈应用
- ⚡ **极致优化部署**：专为 Vite 优化，提供同构部署能力，实现“极速部署”体验

---

### [Electron 41.0 | Electron](https://www.electronjs.org/blog/electron-41-0)

**原文标题**: [Electron 41.0 | Electron](https://www.electronjs.org/blog/electron-41-0)

Electron 41.0 版本发布，包含 Chromium、V8 和 Node.js 的升级，引入了多项安全增强、功能改进和平台支持优化。

- 🔒 **ASAR 完整性摘要**：macOS 应用可嵌入 ASAR 完整性摘要，增强应用防篡改检测能力。
- 🖥️ **Wayland 支持改进**：Linux 平台下无边框窗口现支持阴影和扩展调整边界，提升视觉体验。
- 🔄 **MSIX 自动更新支持**：新增 MSIX 格式自动更新功能，与 Squirrel.Mac 更新服务器兼容。
- 📦 **底层堆栈升级**：Chromium 升级至 146.0.7680.65，Node.js 升级至 v24.14.0，V8 升级至 14.6。
- 🛠️ **新功能与优化**：包括禁用地理位置服务、NV12 纹理支持、通知关闭原因追踪等多项 API 增强。
- ⚠️ **行为变更与弃用**：PDF 渲染改为同进程处理，Cookie 变更事件原因细化，Electron 38.x.y 停止支持。
- 🚀 **后续计划**：团队将持续跟进 Chromium、Node 和 V8 的更新，维护版本兼容性与功能演进。

---

### [Nitro v3 Beta 版现已发布！ - Nitro](https://nitro.build/blog/v3-beta)

**原文标题**: [Nitro v3 Beta is here! - Nitro](https://nitro.build/blog/v3-beta)

Nitro v3 Beta 正式发布，这是一个基于 Web 标准、Rolldown 和 Vite v8 重构的服务器框架，保持了随处部署的特性，性能更优，API 更简洁，并提供了原生 Vite 集成和新的包标识。

- 🚀 **性能优化与轻量化**：默认编译路由，按需加载代码，服务器包最小可小于 10kB，依赖从 321 个大幅减少至不到 20 个。
- ⚡ **原生 Vite 集成**：通过 Vite 插件支持全栈应用开发，单次构建即可生成优化的前后端输出，轻松为任何 Vite 项目添加后端功能。
- 🖌️ **新包标识与导入路径**：包名改为 `nitro`，导入路径更简洁（如 `nitro/*`），替代旧的 `nitropack`，提升开发体验。
- 🌐 **基于 Web 标准的 H3 v2**：完全围绕 `Request`、`Response` 等 Web 标准重写，代码更清晰、可移植，无需额外抽象层。
- 🔧 **框架无绑定**：支持内置文件系统路由或自定义 `server.ts` 入口，可集成 Hono、Elysia 等任何兼容 Web 标准的框架。
- 🗄️ **内置可选的服务器原语**：提供存储、缓存、数据库等运行时无关的原语，完全按需使用，支持多种驱动和平台。
- 🌍 **随处部署**：构建输出兼容 Node.js、Bun、Deno 及 Cloudflare Workers、Vercel 等主流平台，无需配置即可自动适配。
- 🎨 **服务器端渲染支持**：支持多种模板引擎和 React、Vue 等组件库，可逐步实现从 API 路由到全 SSR 的渲染方案。
- 🟢 **为 Nuxt v5 提供核心**：Nitro v3 将作为 Nuxt v5 的基础，带来 Web 标准处理和 Rolldown 构建等先进特性。
- 🏁 **快速入门与迁移指南**：提供 `create-nitro-app` 工具快速创建项目，并详细列出从 v2 迁移的关键变更，如包重命名和 API 更新。

---

### [Vitest 4.1 版本发布！ | Vitest](https://vitest.dev/blog/vitest-4-1.html)

**原文标题**: [Vitest 4.1 is out! | Vitest](https://vitest.dev/blog/vitest-4-1.html)

Vitest 4.1 版本发布，带来多项新功能和改进，包括对 Vite 8 的支持、测试标签系统、实验性模块运行器选项、浏览器 UI 增强、新的测试钩子、更好的堆栈跟踪工具、异步泄漏检测、VS Code 扩展更新、GitHub Actions 集成、AI 代理报告器、新的模拟 API 以及覆盖率改进。

- 🚀 **支持 Vite 8**：Vitest 现在兼容 Vite 8，并使用已安装的 Vite 版本，避免类型不一致问题。
- 🏷️ **测试标签功能**：允许为测试添加标签进行分组和过滤，支持复杂过滤语法，并可配置共享选项如超时和重试。
- 🧪 **实验性模块运行器**：新增 `experimental.viteModuleRunner` 选项，可禁用 Vite 模块运行器，直接使用原生 Node.js 运行测试，提升启动速度和行为一致性。
- 🖥️ **浏览器 UI 配置**：引入 `browser.detailsPanelPosition` 选项，允许调整浏览器 UI 中详情面板的位置，优化小屏幕体验。
- 🔍 **增强浏览器跟踪视图**：改进 Playwright 跟踪查看器集成，自动分组浏览器交互并支持自定义标记，提升调试体验。
- 🧩 **类型推断的 `test.extend`**：新增构建器模式，支持从工厂函数返回值自动推断类型，简化夹具定义。
- 🔄 **新的 `aroundAll` 和 `aroundEach` 钩子**：提供包装测试的上下文，适用于异步本地存储、跟踪跨度或数据库事务等场景。
- 🛠️ **堆栈跟踪辅助工具**：`vi.defineHelper` 可包装函数，使错误堆栈指向调用点而非辅助函数内部，便于定位问题。
- 🚨 **异步泄漏检测**：新增 `--detect-async-leaks` 选项，帮助识别未清理的定时器、句柄和异步资源，减少测试不稳定性。
- 💻 **VS Code 扩展改进**：减少后台进程占用，新增“运行相关测试”命令、支持 Deno 运行时、显示模块加载时间等。
- 📊 **GitHub Actions 任务摘要**：内置 `github-actions` 报告器自动生成测试结果摘要，突出显示不稳定测试并链接到源代码。
- 🤖 **AI 代理报告器**：新增 `agent` 报告器，仅输出失败测试信息，减少 AI 编码代理的令牌使用量。
- 🎯 **新的模拟 API**：`mockThrow` 和 `mockThrowOnce` 方法简化模拟函数抛出错误的设置。
- ⚠️ **WebdriverIO 和预览严格模式**：元素定位默认启用严格模式，匹配多个元素时抛出错误，避免歧义查询。
- 🔄 **Chai 风格模拟断言**：扩展支持 Chai 风格的模拟断言，便于从 Sinon 迁移。
- 📈 **覆盖率改进**：重新支持 `ignore start/stop` 注释忽略代码块，新增 `coverage.changed` 选项仅报告更改文件的覆盖率，优化 HTML 报告器在子路径部署中的表现。

---

### [发布 10.29.0 版本 · preactjs/preact · GitHub](https://github.com/preactjs/preact/releases/tag/10.29.0)

**原文标题**: [Release 10.29.0 · preactjs/preact · GitHub](https://github.com/preactjs/preact/releases/tag/10.29.0)

Preact 10.29.0 版本发布，包含新功能、修复和性能优化，由 JoviDeCroock 主导贡献。

- 🚀 实现 flushSync 功能，提升渲染控制灵活性
- 🔧 修复 renderCount 重置问题，确保状态一致性
- 🛡️ 解决 undefined prototype 相关错误，增强稳定性
- ⚡ 通过代码优化提升兼容性处理性能
- 👥 社区积极反馈，获得多种表情反应支持

---

### [发布 7.5.0 版本 · prisma/prisma · GitHub](https://github.com/prisma/prisma/releases/tag/7.5.0)

**原文标题**: [Release 7.5.0 · prisma/prisma · GitHub](https://github.com/prisma/prisma/releases/tag/7.5.0)

Prisma ORM 发布了 7.5.0 稳定版本，主要包含 ORM 功能增强、错误修复、驱动适配器改进以及 Prisma Studio 的新功能更新。

- 🎉 **ORM 功能增强**：新增对嵌套事务回滚的支持，通过保存点实现 SQL 数据库的嵌套事务回滚行为。
- 🐛 **错误修复**：解决了 Prisma.DbNull 序列化问题、DateTime 字段返回无效日期及游标分页问题。
- 🔧 **驱动适配器改进**：优化了 adapter-mariadb 使用二进制 MySQL 协议，并提升了 adapter-pg 的 TypeScript 体验。
- 🛠️ **Schema Engine 优化**：改进了部分索引的处理，避免不必要的迁移和索引重建。
- 🖥️ **Prisma Studio 更新**：新增多单元格选择、全表搜索、更直观的过滤选项、Cmd+K 命令面板和原始 SQL 查询功能。
- 💼 **企业支持**：推出了企业级支持计划，提供优先问题处理、性能调优和安全合规帮助。
- 🌟 **社区互动**：鼓励用户关注项目更新，并提供了加入 Prisma 团队的职业机会。

---

### [发布 v8.0.0-rc.3 · babel/babel · GitHub](https://github.com/babel/babel/releases/tag/v8.0.0-rc.3)

**原文标题**: [Release v8.0.0-rc.3 · babel/babel · GitHub](https://github.com/babel/babel/releases/tag/v8.0.0-rc.3)

Babel 项目发布了 v8.0.0-rc.3 预发布版本，包含多项更新，涉及规范遵循、破坏性变更、新功能、错误修复、性能优化等方面。

- 🚀 **新功能**：为 `@babel/plugin-transform-react-jsx-development` 添加 `sourceSelf` 选项，并引入解析器的 `locations` 选项
- 💥 **破坏性变更**：从 `Expression` 别名中移除 `Import`，并调整了 `TSDeclareMethod` 和 `decorators` 相关定义
- 🐛 **错误修复**：修复了 Safari 数组解构问题、TypeScript 解析器在异步调用中的错误，以及多个包的可执行性和类型定义问题
- 👓 **规范遵循**：修正了异步箭头函数和管道操作符中 `await` 的解析规则
- 💅 **代码优化**：改进了尾随逗号的注释处理和 `await yield` 的生成逻辑
- 📝 **文档更新**：将 npmjs.com 链接替换为 npmx.dev
- 🏠 **内部改进**：重构解析器以使用统一的 AST 定义，并移除了 `@babel/runtime` 的 `engines` 字段
- 🏃‍♀️ **性能提升**：并行加载 Wasm 和 JSON 导入，并修复了因调试代码导致的解析器性能问题

---

### [core/CHANGELOG.md 在 minor 分支 · vuejs/core · GitHub](https://github.com/vuejs/core/blob/minor/CHANGELOG.md#360-beta8-2026-03-16)

**原文标题**: [core/CHANGELOG.md at minor · vuejs/core · GitHub](https://github.com/vuejs/core/blob/minor/CHANGELOG.md#360-beta8-2026-03-16)

Vue 3.6 版本已进入测试阶段，主要引入了全新的 Vapor Mode 编译模式，旨在减少基础包体积并提升性能。此版本还包含基于 alien-signals 的重大响应式系统重构，显著改善了性能和内存使用。Vapor Mode 现已具备与虚拟 DOM 模式相同的稳定功能特性（Suspense 除外），但当前仍被视为不稳定，建议在性能敏感的子页面或小型新应用中使用。

- 🚀 **Vapor Mode 发布**：新的 SFC 编译模式，可显著提升性能并减少包体积，需通过 `<script setup vapor>` 显式启用。
- 🔧 **功能特性完整**：Vapor Mode 现已支持虚拟 DOM 模式的所有稳定功能（除 Suspense 外），包括 Transition、KeepAlive、Teleport 等。
- ⚡ **响应式系统重构**：基于 alien-signals 重构了 `@vue/reactivity`，带来了性能和内存使用的显著改进。
- 🔌 **互操作性支持**：通过 `vaporInteropPlugin` 插件，Vapor 组件和虚拟 DOM 组件可以相互嵌套使用，但可能存在部分边缘情况。
- 🚫 **功能子集限制**：Vapor Mode 仅支持 Vue 功能的一个子集，明确不支持 Options API、`app.config.globalProperties`、`getCurrentInstance()` 等。
- 🛠️ **自定义指令变更**：Vapor 中的自定义指令接口不同，`value` 参数是一个响应式 getter，并需通过 `watchEffect` 建立副作用。
- ⚠️ **当前稳定性**：Vapor Mode 在 3.6 测试版中功能已完整，但仍被视为不稳定，不建议用于迁移现有组件。
- 📦 **两种使用场景**：可创建纯 Vapor 应用 (`createVaporApp`) 以获得最小包体积，或在虚拟 DOM 应用中通过互操作插件集成 Vapor 组件。

---

### [源映射：通过标准发布功能 | 彭博 JS 博客](https://bloomberg.github.io/js-blog/post/standardizing-source-maps/)

**原文标题**: [Source Maps: Shipping Features Through Standards | Bloomberg JS Blog](https://bloomberg.github.io/js-blog/post/standardizing-source-maps/)

Source Maps 是连接开发源代码与编译后代码的关键工具，经历了从非正式协作到标准化规范的发展历程，如今在 ECMA-426 标准下持续演进，以支持更复杂的调试需求。

- 🗺️ **Source Maps 的作用**：在复杂 Web 开发中，将优化、压缩后的代码映射回原始源代码，方便调试。
- 📜 **发展历程**：最初基于非正式 Google Doc 协作，2024 年正式成为 ECMA-426 标准，由 TC39-TG4 工作组推动。
- 🔍 **文件结构**：JSON 格式，包含版本、源文件列表、映射数据等字段，其中 `mappings` 使用 Base64 VLQ 编码以减小体积。
- 📉 **映射优化**：Revision 3 改用分段映射和相对编码，大幅减少了文件大小，提升编解码效率。
- 🚀 **新特性演进**：通过 `x_` 前缀等非正式方式逐步引入功能（如忽略列表），凸显标准化必要性。
- 🛠️ **未来方向**：工作组正推进 Scopes（增强作用域和变量映射）和 Range Mappings（提升映射精度）等新特性，以改善调试体验。

---

### [源映射 - 术语表 | MDN](https://developer.mozilla.org/en-US/docs/Glossary/Source_map)

**原文标题**: [Source map - Glossary | MDN](https://developer.mozilla.org/en-US/docs/Glossary/Source_map)

Source map 是一种 JSON 格式文件，用于将浏览器接收到的压缩或转换后的代码映射回其原始未修改形式，从而在调试时能够重构和使用原始代码。

- 🗺️ Source map 是一种 JSON 文件，用于将压缩或转换后的代码映射回原始代码，便于调试。
- ⚙️ 代码转换的原因包括：提高服务器传输效率、支持旧版浏览器兼容性，以及使用 TypeScript 或 Sass 等浏览器不直接支持的语言。
- 🔍 浏览器通过 HTTP 响应头 `SourceMap` 或代码中的 `sourceMappingURL` 注释来检测 source map。
- 🛠️ 在构建过程中，如 SCSS 转换为 CSS 时，会生成 source map 文件（如 `index.css.map`），其中包含原始代码与生成代码的映射关系及原始源代码的编码形式。
- 🧩 Source map 文件包含版本、源文件路径、映射数据等字段，使浏览器开发者工具能够显示原始源代码并链接到具体行号。

---

### [源映射格式规范](https://tc39.es/ecma426/)

**原文标题**: [Source map format specification](https://tc39.es/ecma426/)

该文档是 ECMA-426 标准草案，定义了用于将编译后的源代码映射回原始源代码的源映射格式规范，旨在支持源代码级调试和服务器端堆栈跟踪反混淆。

- 📜 **规范定义**：详细规定了源映射的 JSON 格式、编码方式（如 base64 VLQ）和解码算法，确保工具间的互操作性。
- 🔗 **映射结构**：通过`mappings`字段以分段编码形式关联生成代码与原始源代码的位置（行、列），支持名称映射和忽略列表。
- 🌐 **多语言支持**：适用于 JavaScript、WebAssembly 和 CSS，定义了从这些语言中提取源映射 URL 的方法（如通过注释或 HTTP 头部）。
- 📂 **索引源映射**：允许通过`sections`字段将多个源映射组合，以处理代码拼接等后处理场景。
- ⚙️ **操作与查询**：提供解码后的源映射记录查询接口（如`GetOriginalPositions`），便于调试器定位原始源代码位置。
- 📚 **附录与参考**：包含实现惯例、术语定义及外部标准引用（如 ECMA-262、WHATWG 规范），确保技术一致性。

---

### [如何在两周内将 13 万行代码从 React 重写为 Svelte | Strawberry 博客](https://strawberrybrowser.com/blog/react-to-svelte)

**原文标题**: [How we Rewrote 130K Lines from React to Svelte in Two Weeks | Strawberry Blog](https://strawberrybrowser.com/blog/react-to-svelte)

我们利用编码代理在两周内将 Strawberry 浏览器的整个前端从 React 迁移到 Svelte，使浏览器性能提升两倍。

- 🚀 **性能飞跃**：迁移后浏览器响应速度提升 2 倍，首次内容绘制时间从 300ms 降至 124ms，AI 令牌流渲染更流畅，重渲染减少 10 倍。
- 🔄 **技术选型原因**：React 的虚拟 DOM 模型在浏览器多进程、AI 持续更新的场景下导致渲染级联和性能瓶颈，而 Svelte 的细粒度响应式更新能实现零运行时开销。
- 🤖 **高效迁移策略**：通过制定严格的 Svelte 编码规则，利用 Cursor 等 AI 编码代理进行模块化迁移（先研究规则→移植代码→测试），单人两周完成 13 万行代码重构。
- 📦 **生态与挑战**：Svelte 生态基本满足需求，仅拖拽库需自研；同步开发时部分功能遗漏，但性能提升值得代价。
- ⚡ **AI 产品启示**：对于需要实时响应 AI 输出的产品（如并行代理、流式输出），Svelte 的编译时优化比 React 更具优势，且 AI 辅助开发使大规模迁移更可行。
- 🧹 **附带优化**：代码库更简洁，移除 56 个未使用依赖，测试覆盖提升，更利于 AI 代理协作开发。

---

### [TimescaleDB — 排名第一的时序数据库 | 泰格数据](https://www.tigerdata.com/timescaledb?utm_source=cooperpress&utm_medium=referral&utm_campaign=javascript-weekly-newsletter)

**原文标题**: [TimescaleDB — The #1 Time-Series Database | Tiger Data](https://www.tigerdata.com/timescaledb?utm_source=cooperpress&utm_medium=referral&utm_campaign=javascript-weekly-newsletter)

TimescaleDB 是一个基于 Postgres 构建的开源时序数据库，专为处理传感器、链上及客户数据而设计，提供实时分析、高效压缩和自动管理功能，适用于初创公司和企业。

- 🚀 自动分区：通过超表将 Postgres 表按时间或 ID 自动分区，实现快速数据写入和可预测查询
- 💾 行列混合存储：结合行存储的写入速度和列存储的查询性能，数据老化时自动转换
- 📉 高效压缩：支持高达 95% 的数据压缩，降低历史数据存储成本并提升查询速度
- 🔄 增量物化视图：通过连续聚合实现增量刷新的数据汇总，支持实时仪表板展示
- ⚙️ 自动化管理：内置任务调度器和可配置的数据保留策略，提供完整的审计能力
- 📊 时序函数库：提供约 200 个原生 SQL 函数，简化复杂时序分析如时间加权平均和插值计算
- ☁️ 云原生兼容：100% 兼容 PostgreSQL，拥有超过 1.2 万开发者社区，支持 Helm 快速部署
- 🌟 企业验证：获 Cloudflare、Replicated 等企业认可，在 GitHub 收获 2.2 万星标，体现社区活跃度

---

### [最佳实践 • Svelte 文档](https://svelte.dev/docs/svelte/best-practices)

**原文标题**: [Best practices • Svelte Docs](https://svelte.dev/docs/svelte/best-practices)

本文档概述了 Svelte 5 的最佳实践，旨在帮助开发者编写高效、健壮的 Svelte 应用，涵盖状态管理、响应式编程、模板语法、样式处理及避免使用遗留功能等方面。

- 🧠 **状态管理**：仅对需要响应式的变量使用 `$state`，对于大型且仅重新赋值而非变异的对象，使用 `$state.raw` 以减少性能开销。
- 🔄 **派生状态**：优先使用 `$derived` 而非 `$effect` 来计算依赖状态的值，避免副作用，且派生状态可写。
- ⚠️ **副作用处理**：`$effect` 应作为最后手段，避免在其中更新状态，推荐使用事件处理器、`{@attach ...}` 或 `$inspect` 进行调试。
- 📦 **属性处理**：将属性视为可变，使用 `$derived` 处理依赖属性的值，确保属性变化时能正确更新。
- 🔍 **调试工具**：使用 `$inspect.trace` 在 `$effect` 或 `$derived.by` 中追踪响应式依赖，帮助诊断更新问题。
- 🎯 **事件监听**：通过 `on` 前缀属性处理事件，对于 `window` 或 `document` 事件，使用 `<svelte:window>` 和 `<svelte:document>`，避免 `onMount` 或 `$effect`。
- 🧩 **代码片段**：使用 `{#snippet ...}` 和 `{@render ...}` 定义和渲染可复用的模板片段，提升代码模块化。
- 📊 **循环优化**：优先使用带键值的 `{#each ...}` 块，避免使用索引作为键，以提升 DOM 更新性能。
- 🎨 **样式集成**：通过 `style:` 指令将 JavaScript 变量作为 CSS 自定义属性传递，在样式中使用 `var()` 引用。
- 👶 **子组件样式**：使用 CSS 自定义属性控制子组件样式，或通过 `:global` 覆盖库组件的样式，保持样式作用域清晰。
- 🌐 **上下文管理**：使用 `createContext` 替代 `setContext` 和 `getContext`，提供类型安全的状态共享，避免服务器端渲染时的状态泄漏。
- ⏳ **异步支持**：在 Svelte 5.36+ 中，利用 `await` 表达式和 `hydratable` 直接在组件中使用 Promise，需启用实验性选项。
- 🚫 **避免遗留功能**：始终使用符文模式，用 `$state`、`$derived`、`$props` 等现代 API 替代旧有特性，如 `export let`、`$:` 和 `<slot>`。

---

### [前端内存泄漏：基于 500 个仓库的静态分析与五种场景基准研究](https://stackinsight.dev/blog/memory-leak-empirical-study/)

**原文标题**: [Frontend Memory Leaks: A 500-Repository Static Analysis and Five-Scenario Benchmark Study](https://stackinsight.dev/blog/memory-leak-empirical-study/)

本文通过对 500 个开源仓库的静态分析和五种场景的基准测试，系统性地研究了前端内存泄漏的普遍性和实际成本。研究发现，86% 的仓库存在至少一种缺失清理的模式，共发现 55,864 个潜在泄漏实例。基准测试表明，每种缺失清理的模式在每个组件挂载/卸载周期中平均导致约 8 KB 的堆内存增长，而正确清理后增长近乎为零。研究涵盖了 React、Vue 和 Angular 三大框架，并提供了具体的检测方法和修复方案。

- 🔍 **普遍性高**：在扫描的 500 个仓库中，86% 存在至少一种缺失清理的模式，共发现 55,864 个潜在泄漏实例。
- ⏱️ **定时器为首要问题**：缺失清理的定时器（如`setTimeout`、`setInterval`）占比最高，达 43.9%。
- 🧩 **框架差异明显**：React 占泄漏实例的 62.3%，Vue 占 28.2%，Angular 占 9.5%，反映了各框架的架构特点。
- 📊 **基准测试量化成本**：五种常见泄漏模式（如事件监听器、定时器、订阅）在每个周期平均导致约 8 KB 内存增长，而正确清理后增长可忽略不计。
- 🔧 **修复简单有效**：大多数泄漏只需添加一行清理代码（如`useEffect`的返回函数、`onUnmounted`钩子）即可避免。
- 📱 **实际影响显著**：在长时间会话（如仪表盘、视频会议）中，泄漏内存可能累积至数十 MB，导致移动设备标签页崩溃或桌面应用卡顿。
- 🛠️ **工具支持不足**：现有 linting 规则对缺失清理的检测覆盖不全，需依赖静态分析或生产环境堆内存监控。
- 📈 **线性累积模式**：泄漏内存随组件挂载/卸载次数线性增长，多模式叠加时累积效应更明显。
- 🎯 **检测优先级建议**：优先检查定时器、事件监听器和订阅的清理，再处理框架特定模式（如 Vue 的`watch`停止句柄）。
- 📚 **开源资源可用**：研究提供了完整的静态分析工具和基准测试代码，便于开发者自查和复现。

---

### [用 TypeScript 重写一个 12 年历史的 JavaScript 库 | if(and)else](https://ifandelse.com/blog/rewriting-a-12-year-old-javascript-library-in-typescript/)

**原文标题**: [Rewriting a 12-Year-Old JavaScript Library in TypeScript | if(and)else](https://ifandelse.com/blog/rewriting-a-12-year-old-javascript-library-in-typescript/)

作者将一款已有 12 年历史的 JavaScript 库 machina 用 TypeScript 进行了重写，旨在提供更现代、类型安全且简洁的有限状态机解决方案，以应对当前前端开发中复杂的状态管理挑战。

- 🚀 **重写动机**：原库因作者生活重心转移而缺乏维护，面对现代前端日益复杂的状态管理需求，作者决定用 TypeScript 彻底重写，以提升类型安全和开发体验。
- 🛠️ **核心设计**：新版本强调有限状态机（FSM）的简洁性，避免过度复杂的 Actor 系统，并通过分离行为与状态、延迟输入处理等机制，优化性能与可维护性。
- 📦 **代码示例**：展示了新版 machina 的 API，如`createFsm`创建交通灯状态机，代码简洁且类型安全，无需繁琐的类型定义。
- 🔄 **行为状态分离**：引入`BehavioralFsm`类型，允许单个状态规则应用于多个实体，显著提升性能，适用于管理大量实体的场景（如连接状态）。
- ⏳ **异步处理**：通过`defer`方法实现同步 API 下的异步输入队列处理，避免内置异步机制，保持核心逻辑的简洁性。
- 🧩 **类型安全简化**：TypeScript 自动推断类型，减少显式类型声明，仅在`BehavioralFsm`中需指定客户端类型，降低了使用门槛。
- 🌐 **资源与推广**：新版库已发布至 npm，提供详细文档和示例，鼓励开发者尝试 FSM 来替代复杂的布尔逻辑和条件分支，适用于前端和 Node.js 环境。

---

### [机械 | 机械](https://machina-js.org/)

**原文标题**: [machina | machina](https://machina-js.org/)

Machina 是一个专为 JavaScript 和 TypeScript 设计的有限状态机库，强调简洁、类型安全和高效的状态管理。

- 🚀 **TypeScript 优先**：完全使用 TypeScript 编写，提供完整的类型推断，涵盖状态、输入和转换。
- 🏗️ **分层状态**：支持嵌套子状态机，自动处理输入冒泡和父子状态间的委托。
- 🔄 **行为化状态机**：定义一次行为，可应用于多个独立客户端，无需额外开销。
- ⚡ **简洁设计**：只需定义状态、处理输入和转换，无需复杂泛型，专注于解决问题。
- ⏳ **延迟输入处理**：自动排队处理未就绪状态到达的输入，并在转换时重放。
- 🎯 **生命周期钩子与事件**：提供细粒度的进入、退出和转换事件钩子，按需订阅。
- 🔍 **静态分析**：通过 machina-inspect 和 ESLint 插件，在开发时检测不可达状态、无限循环和缺失处理程序。

---

### [关于协作编辑的谎言，第二部分：为何我们不使用 Yjs / Moment 开发日志](https://www.moment.dev/blog/lies-i-was-told-pt-2)

**原文标题**: [Lies I was Told About Collaborative Editing, Part 2: Why we don't use Yjs / Moment devlog](https://www.moment.dev/blog/lies-i-was-told-pt-2)

本文探讨了为什么在协作编辑中不推荐使用 Yjs，并提出了一个更简单的替代方案。文章指出，尽管 Yjs 在无主对等（masterless p2p）编辑中有其优势，但对于大多数实时协作场景，它存在性能、复杂性和数据一致性等问题。相比之下，基于权威服务器和简单版本控制的方案（如 prosemirror-collab）在实现乐观更新、离线编辑和细粒度历史记录方面同样有效，且更易于维护和调试。

- 🚫 **Yjs 在实时协作中的局限性**：尽管 Yjs 流行，但其在冲突解决时可能静默破坏文档，且不适合离线场景，因为用户无法避免冲突。
- ⚙️ **性能问题严重**：Yjs 每次按键都会重建整个文档，导致性能下降、插件兼容性问题，以及光标、选择和撤销功能的异常行为。
- 🔄 **简单替代方案**：使用 prosemirror-collab 等库，仅需约 40 行代码即可实现乐观更新、离线编辑和版本同步，无需复杂 CRDT。
- 🧩 **架构复杂性高**：Yjs 将文档转换为 XML 处理，增加了转换开销，且与 ProseMirror 的架构不兼容，导致调试和维护困难。
- 📜 **模式与权限挑战**：Yjs 的无主设计使得文档模式验证和权限控制变得复杂，容易在升级或网络中断时导致数据丢失。
- 🗑️ **数据存储问题**：Yjs 的“墓碑”机制可能导致内存占用增加或数据丢失，而简单方案通过版本历史存储步骤，更高效可靠。
- 🐛 **调试难度大**：CRDT 的最终一致性使得调试异常困难，而简单方案提供了更多工具（如幂等键、重复请求）来排查问题。
- 🎯 **用户体验优先**：设计协作库时应以最终用户体验为目标（如 60fps、可预测的数据行为），而非单纯追求算法特性。

---

### [前端 OAuth 2.0 的攻防解析 • Philippe De Ryck • YOW! 2025 - YouTube](https://www.youtube.com/watch?v=oGktdQ45bTg)

**原文标题**: [Breaking & Securing OAuth 2.0 in Frontends • Philippe De Ryck • YOW! 2025 - YouTube](https://www.youtube.com/watch?v=oGktdQ45bTg)

该文本是 YouTube 网站页脚的标准法律与信息链接列表，概述了平台提供的各类政策说明、功能及联系渠道。

- 📄 关于平台的基本信息与公司介绍
- 📰 查看新闻稿和官方公告
- ©️ 版权政策与侵权处理
- 📞 联系平台与用户支持
- 🧑‍🎨 创作者相关资源与计划
- 📢 广告合作与商业推广
- 👩‍💻 开发者工具与 API 资源
- 📑 服务条款与使用协议
- 🔒 隐私保护政策与数据使用
- ⚖️ 平台安全政策与社区准则
- ⚙️ YouTube 功能运作机制说明
- 🧪 新功能测试与更新信息
- 🏢 版权所有方及年份声明

---

### [我是如何将 Bluesky 点赞功能添加到我的 Astro 博客的](https://loige.co/how-i-added-bluesky-likes-to-my-astro-blog/)

**原文标题**: [How I added Bluesky likes to my Astro blog](https://loige.co/how-i-added-bluesky-likes-to-my-astro-blog/)

本文介绍了作者如何在 Astro 博客中添加 Bluesky 点赞展示功能，无需 API 密钥或服务器端代码，通过使用 Lea Verou 开发的 bluesky-likes Web 组件包实现。

- 🛠️ 使用 bluesky-likes 包：通过两个 Web 组件（`<bluesky-likes>`和`<bluesky-likers>`）展示点赞数和用户头像，无需 API 密钥，仅需指向 Bluesky 帖子 URL
- 📝 扩展博客架构：在 Astro 的内容集合模式中添加`bluesky_url`字段，用于关联每篇博文对应的 Bluesky 帖子
- 🧩 创建专用组件：开发 BlueskyReactions.astro 组件，包含点赞展示、头像网格和跳转链接，支持 CSS 自定义属性主题适配
- 🔗 集成到页面模板：在博文页面中条件渲染该组件，仅当`bluesky_url`存在时加载相关脚本和内容
- 🔍 匹配历史帖子：使用 bsky CLI 工具查找并关联已发布的博文对应的 Bluesky 帖子，通过 AI 辅助完成批量匹配工作

---

### [获取失败](https://javascriptweekly.com/link/182308/web)

**原文标题**: [Failed to retrieve](https://javascriptweekly.com/link/182308/web)

无法总结：获取内容失败，状态码 429。

---

### [原生 JSON 模块终于成为现实 - 马特·史密斯](https://allthingssmitty.com/2026/03/16/native-json-modules-are-finally-real/)

**原文标题**: [
    Native JSON modules are finally real - Matt Smith
  ](https://allthingssmitty.com/2026/03/16/native-json-modules-are-finally-real/)

原生 JSON 模块现已正式成为 JavaScript 标准，通过 import 属性实现，无需构建工具即可在浏览器中直接导入 JSON 文件。

- 📜 原生 JSON 模块支持通过`import config from "./config.json" with { type: "json" }`语法直接导入，无需构建步骤
- 🔍 必须使用`with { type: "json" }`明确声明文件类型，避免引擎猜测执行方式，确保安全性和一致性
- 🧩 导入的 JSON 作为模块默认导出，遵循 ES 模块缓存规则，相同文件多次导入会返回同一实例
- ⚙️ 与构建工具方案对比：原生方案在运行时解析、无需构建步骤、遵循标准安全模型
- 🌐 所有现代环境（浏览器/Node/Deno/Bun）均已支持，但构建工具仍提供文件内联、资源哈希等附加功能
- 🚀 该特性标志着模块系统向显式类型声明演进，未来可扩展支持 CSS 等更多模块类型

---

### [Nuxt 4.4 · Nuxt 博客](https://nuxt.com/blog/v4-4)

**原文标题**: [Nuxt 4.4 · Nuxt Blog](https://nuxt.com/blog/v4-4)

Nuxt 4.4 版本引入了多项新功能和改进，包括自定义 `useFetch`/`useAsyncData` 工厂函数、升级至 Vue Router v5、新增无障碍播报器、类型化布局属性、构建性能分析、更智能的负载处理等，旨在提升开发体验和应用性能。

- 🏭 新增 `createUseFetch` 和 `createUseAsyncData` 工厂函数，支持创建带有自定义默认选项的实例，便于统一管理 API 请求和异步数据逻辑。
- 🗺️ 升级至 Vue Router v5，移除了对 `unplugin-vue-router` 的依赖，为后续类型化路由功能铺平道路。
- 💪 在 `definePageMeta` 中支持类型化布局属性，允许页面直接向布局传递参数化属性，并享受完整的类型提示。
- 🗣️ 新增 `useAnnouncer` 组合式函数和 `<NuxtAnnouncer>` 组件，用于动态播报页面内容变化，提升无障碍访问体验。
- 🚀 路由生成迁移至 `unrouting` 库，利用字典树数据结构，使开发服务器在文件未变动时的更新速度提升高达 28 倍。
- 🍫 针对缓存路由（如 ISR/SWR）优化了负载处理，新增 `payloadExtraction: 'client'` 模式，并在运行时引入内存 LRU 缓存，减少不必要的服务器渲染。
- 🍪 `useCookie` 新增 `refresh` 选项，可在不改变 cookie 值的情况下刷新其过期时间，便于会话管理。
- ♻️ `useState` 和 `clearNuxtState` 现在支持重置到初始值而非 `undefined`，与 `useAsyncData` 的行为保持一致。
- 🕵️‍♂️ 改进了导入保护机制，当服务器端代码被意外导入客户端时，会提供更清晰的错误追踪和建议。
- 🔮 实验性的视图过渡功能现支持定义过渡类型，允许为不同的导航模式（如前进/后退、标签页切换）应用不同的动画效果。
- 💡 优化了 `optimizeDeps` 提示，当 Vite 发现新依赖时会提供可复制到配置中的代码片段，并警告无法解析的条目。
- 🏷️ 新增实验性选项 `normalizeComponentNames`，可将页面组件名称规范化以匹配路由名称，便于开发和调试。
- ⚡ 新增构建性能分析功能，通过 `nuxt build --profile` 命令生成详细报告，帮助识别构建过程中的性能瓶颈。
- 🔥 包含多项性能优化，如模块 ID 解析速度提升 14,000 倍，以及在开发环境中禁用 `NuxtLink` 的预取以减少不必要的重载。
- ⬆︎ 推荐使用 `npx nuxt upgrade --dedupe` 进行升级，并参考官方升级指南以确保平滑过渡。

---

### [HTML 演示框架 | reveal.js](https://revealjs.com/)

**原文标题**: [The HTML presentation framework | reveal.js](https://revealjs.com/)

reveal.js 是一款开源 HTML 演示框架，允许用户通过网页浏览器免费创建功能全面且美观的演示文稿。它基于开放的 Web 技术，支持 CSS 样式调整、iframe 嵌入外部页面及 JavaScript API 自定义功能，并提供嵌套幻灯片、Markdown 支持、自动动画、PDF 导出、演讲者备注、LaTeX 公式和高亮代码等丰富特性。用户可通过安装指南快速入门，或使用在线编辑器 Slides.com 进行可视化制作。该项目由@hakimel 主导并依托社区贡献维护，支持方式包括成为 Slides.com 付费会员。

- 🌐 开源 HTML 框架，免费创建网页演示文稿
- 🛠️ 基于开放 Web 技术，支持 CSS、iframe 和 JavaScript API 自定义
- ✨ 内置嵌套幻灯片、Markdown、自动动画、PDF 导出等多项功能
- ⚡ 提供安装指南，一分钟即可快速上手
- 🖥️ 可使用在线编辑器 Slides.com，无需编写代码
- ❤️ 由@hakimel 主导，社区共同维护，支持通过 Slides.com 付费会员赞助项目

---

### [发布 6.0.0 版本 · hakimel/reveal.js · GitHub](https://github.com/hakimel/reveal.js/releases/tag/6.0.0)

**原文标题**: [Release 6.0.0 · hakimel/reveal.js · GitHub](https://github.com/hakimel/reveal.js/releases/tag/6.0.0)

reveal.js 发布了 6.0.0 版本，主要引入了官方的 React 封装包 @revealjs/react，允许开发者使用 React 组件构建演示文稿。此次更新包含多项重大变更，如插件路径、ES 模块和 CSS 路径的调整，并内置了 TypeScript 类型支持。此外，版本还带来了多项新功能和改进，包括构建工具迁移至 Vite、新增演讲者视图控制选项、视频自动播放优化、MathJax 4 支持、无障碍功能增强等，同时修复了多个已知问题。

- 🎉 发布官方 React 封装包 @revealjs/react，支持使用 React 组件构建演示文稿
- ⚠️ 包含多项重大变更：插件路径、ES 模块和 CSS 路径调整，需参考升级指南
- 📦 内置 TypeScript 类型支持，无需额外安装 @types/reveal.js
- 🛠️ 构建工具从 gulp 迁移至 Vite，提升开发体验
- 🎤 新增 controls: 'speaker' 配置选项，仅在演讲者视图显示控制按钮
- 📹 优化视频自动播放逻辑，被阻止的视频将静音播放并显示取消静音按钮
- 🔢 数学插件新增对 MathJax 4 的支持
- ♿ 改进无障碍功能：图像和视频的 alt 标签现可被屏幕阅读器识别
- 🔧 新增 removeHiddenSlides() API 方法，并优化了 sync() 功能
- 🐛 修复了 Android 和 iOS 上的视频播放问题及主题字体缺失等错误

---

### [专为 React Native 打造的移动 CI/CD](https://expo.dev/services/workflows?utm_source=jsweekly&utm_medium=email&utm_campaign=34911156-NDR%2520-%2520Starter%2520Plan%2520Growth%2520%2526%2520Retention&utm_content=workflows-lp)

**原文标题**: [Mobile CI/CD built for React Native](https://expo.dev/services/workflows?utm_source=jsweekly&utm_medium=email&utm_campaign=34911156-NDR%2520-%2520Starter%2520Plan%2520Growth%2520%2526%2520Retention&utm_content=workflows-lp)

Expo Workflows 是一款专为 React Native 设计的移动端 CI/CD 平台，能够无缝集成到现有 CI 系统中，提供构建、提交、重新打包和 OTA 更新等一站式服务，显著提升开发效率和部署速度。

- 🚀 **集成与扩展**：无需替换现有 CI 系统，可逐步将移动端构建任务迁移至 Expo Workflows，简化配置和管理。
- ⚙️ **专用基础设施**：提供预置的移动任务模块（如构建、提交、更新等），支持在优化的 M4 Pro 硬件上运行，构建速度比通用虚拟机快 50% 以上。
- 🔐 **统一签名管理**：仅需一个 EXPO_TOKEN 即可替代复杂的签名配置，实现加密存储和按需注入，提升安全性。
- ⚡ **智能缓存与优化**：自动检测代码变更，通过缓存和增量构建（如重新打包仅需约 2 分钟）减少不必要的全量构建，部署速度提升 40-60%。
- 💰 **降低成本与运维负担**：减少对 macOS 运行器的依赖，降低 CI 分钟消耗，据称可削减 80% 的 DevOps 隐性成本，让团队更专注于功能开发。
- 🌐 **灵活触发方式**：支持通过 GitHub 事件、CLI 命令或手动触发，轻松融入现有工作流，并提供企业级可靠性和 99.9% 的正常运行时间保障。

---

### [RedwoodSDK：面向人类的简易框架](https://rwsdk.com/blog/redwood-v1-getting-out-of-the-weeds)

**原文标题**: [RedwoodSDK: A simple framework for humans](https://rwsdk.com/blog/redwood-v1-getting-out-of-the-weeds)

RedwoodSDK 1.0 正式发布，标志着从 2020 年开始的五年旅程达到新阶段。创始人 Peter Pistorius 回顾了从参与 RedwoodJS 开发到创业失败，最终回归并重塑框架理念的历程，强调开发者需超越技术本身，聚焦业务本质。新版本围绕三大设计原则构建：无魔法实现透明编码、组合性优先于配置、基于原生 Web API 的架构，旨在让开发者专注于业务而非技术细节。

- 🚀 **RedwoodSDK 1.0 发布**：历经五年开发，于 2026 年 3 月 11 日正式推出，是 RedwoodJS 框架的演进成果。
- 🌱 **创始历程**：始于 2020 年 Tom 的一条推特邀请，Peter 从南非到硅谷的追梦之旅，经历了框架开发、离职创业失败后回归的转折。
- 💡 **关键教训**：主动争取机会（如请求全职工作报酬）能改变局面；开发者常陷入技术细节的“牢笼”，需平衡代码与商业目标。
- 🔄 **理念转变**：创业经历让 Peter 意识到，早期初创公司需要关注业务而非纯粹技术优化，这促使 RedwoodSDK 转向解决实际业务问题。
- 🧩 **设计原则**：以“无魔法”（代码透明）、组合性优先（提供基础模块而非强制配置）、Web 原生架构（直接使用 Web API）为核心。
- 👥 **团队贡献**：特别感谢 Justin van der Merwe 的辛勤工作，以及数百名贡献者共同塑造了 Redwood 社区的人文精神。

---

### [RedwoodSDK：面向人类的简易框架](https://rwsdk.com/blog/why-cloudflare-unified-platform)

**原文标题**: [RedwoodSDK: A simple framework for humans](https://rwsdk.com/blog/why-cloudflare-unified-platform)

本文阐述了选择 Cloudflare 作为统一平台的理由，旨在通过整合计算、数据库、存储和队列服务，消除传统 SaaS 方案中的隐藏成本与集成负担，从而让开发者专注于产品开发本身。

- 🧩 **统一平台优势**：避免使用多个“最佳单品”服务带来的发现、注册、集成、本地开发及生产部署等隐性成本，转向一体化开发环境。
- 🔍 **平台评估结果**：对比 Vercel、Supabase、Pocketbase 后，Cloudflare 在提供完整四要素（计算、数据库、存储、队列）方面最为契合。
- ⚙️ **技术整合魔力**：Cloudflare 的 Workers、Durable Objects 和 Bindings 让服务间像内存通信一样高效，大幅简化配置与协作。
- 🚀 **延迟优化策略**：通过 Bindings 直连和骨干网加速，消除架构性延迟，使代码与服务近乎零距离交互。
- 🔓 **开放与灵活性**：基于 Cloudflare 构建“开放绑定”规范，实现服务商无感切换，兼顾平台优化与避免供应商锁定。
- 🌍 **经济与地域包容**：Cloudflare 无需信用卡的免费层，降低了全球开发者（尤其非洲地区）使用高性能基础设施的门槛。
- 🎯 **愿景升级**：从 RedwoodJS 的“集成 Web 框架”演进为 RedwoodSDK on Cloudflare 的“集成 Web 平台”，让开发者回归产品工程本质。

---

### [GitHub - kepano/defuddle：以Markdown格式获取任意页面的主要内容。· GitHub](https://github.com/kepano/defuddle)

**原文标题**: [GitHub - kepano/defuddle: Get the main content of any page as Markdown. · GitHub](https://github.com/kepano/defuddle)

Defuddle 是一个用于从网页中提取和清理主要内容的 JavaScript 库，它能移除广告、侧边栏、页脚等非必要元素，并支持输出为干净的 HTML 或 Markdown 格式。

- 🧹 **核心功能**：自动提取网页正文，移除广告、评论、导航栏等干扰元素，专注于核心内容。
- 🛠️ **多环境支持**：既可在浏览器中直接使用，也可在 Node.js 环境中运行，并提供了命令行工具。
- 📄 **输出格式灵活**：支持输出为 HTML 或 Markdown，并可提取标题、作者、描述等丰富的元数据。
- 🔧 **高度可配置**：提供多种选项以控制清理行为，如是否移除隐藏元素、小图片，以及是否启用调试模式等。
- 📦 **模块化设计**：提供核心包、完整功能包和 Node.js 专用包，以适应不同的使用场景和依赖需求。
- ⚙️ **标准化处理**：对代码块、脚注、数学公式、提示框等元素进行标准化转换，确保输出的一致性。
- 🐛 **易于调试**：内置调试模式，可详细查看内容选择逻辑和被移除的元素，方便排查问题。

---

### [GitHub - mozilla/readability: 可读性库的独立版本 · GitHub](https://github.com/mozilla/readability)

**原文标题**: [GitHub - mozilla/readability: A standalone version of the readability lib · GitHub](https://github.com/mozilla/readability)

Mozilla Readability 是一个用于提取网页正文内容的独立 JavaScript 库，最初为 Firefox 阅读模式开发，支持在浏览器和 Node.js 环境中使用，提供可配置的解析选项与安全建议。

- 📦 可通过 npm 安装，支持浏览器与 Node.js 环境使用
- 🛠️ 提供可配置的解析选项，如调试模式、元素数量限制与内容保留规则
- 📄 解析方法返回标题、内容、摘要等结构化文章信息
- ⚡ 包含快速检测函数，用于预先判断页面是否适合解析
- 🔒 强烈建议配合 DOMPurify 等消毒库使用，以防止脚本注入攻击
- 🌐 在 Node.js 中需借助 jsdom 等库提供 DOM 环境
- 📜 基于 Apache 2.0 许可证开源，接受社区贡献
- 📊 项目在 GitHub 上拥有超过 1.1 万星标，表明其广泛采用与活跃度

---

### [跨浏览器扩展框架](https://extension.js.org/)

**原文标题**: [The cross-browser extension framework](https://extension.js.org/)

Extension.js 是一个跨浏览器扩展开发框架，它通过统一的现代化工作流，让开发者能够同时为 Chrome、Edge 和 Firefox 构建浏览器扩展。该框架处理了清单编译、浏览器特定输出、重载行为和打包等任务，使开发者能专注于产品功能开发。它支持多种前端框架和语言，提供从脚手架到打包发布的完整工具链，并注重开发体验和生产就绪性。

- 🛠️ **统一构建流程**：一次开发即可为 Chrome、Edge、Firefox 及自定义 Chromium/Gecko 目标生成浏览器特定的输出，保持开发、测试和发布版本的一致性。
- 📁 **结构清晰可维护**：随着扩展规模增长，保持清单文件、路径和生成资源的同步，确保项目结构明确。
- ⚡ **高效安全的热更新**：为每次变更提供最快且安全的更新路径，支持从热模块替换到完整重启的不同场景。
- 🧩 **技术栈灵活可选**：支持 React、Vue、Svelte、TypeScript 或 JavaScript 等多种技术栈，团队可自由选择 UI 模型而不改变核心扩展工具链。
- 📦 **一体化构建预览打包**：提供从本地检查到商店就绪制品的清晰发布流程，支持为各浏览器构建、预览和打包。
- 🔧 **环境变量干净注入**：按浏览器和模式加载环境变量，并可在 JavaScript、JSON 和 HTML 中替换使用。
- 🚀 **快速启动与模板支持**：提供 React、Preact、Vue、Svelte、TypeScript 和 JavaScript 的生产就绪模板，支持开发者快速从创意到运行扩展。
- 🌐 **专为跨浏览器设计**：单一项目即可支持 Chrome、Edge 和 Firefox，保持工作流一致，简化本地测试并减少浏览器间差异。
- 🏗️ **适合生产团队**：帮助团队标准化构建、测试、预览和发布流程，使工作流更可重复，适用于从实验到生产的过程。
- 📚 **文档引导清晰**：建议从“入门指南”和“首个扩展指南”开始，快速上手后可根据所选技术栈查阅模板指南和功能页面。

---

### [GitHub - callstackincubator/react-native-sandbox: 在单个应用中运行多个隔离的 React Native 实例 · GitHub](https://github.com/callstackincubator/react-native-sandbox)

**原文标题**: [GitHub - callstackincubator/react-native-sandbox: Run multiple, isolated React Native instances within a single application · GitHub](https://github.com/callstackincubator/react-native-sandbox)

这是一个用于在单个应用中运行多个隔离的 React Native 实例的库，允许嵌入第三方或特定功能的“微应用”于沙盒环境中，通过明确的 API 进行安全通信，防止对主应用的未授权干扰。

- 🏝️ **项目目的**：安全地在 React Native 应用中运行第三方代码，实现隔离、安全性和可控通信。
- 📦 **核心功能**：提供基于组件的 API 创建沙盒化 React Native 实例，无需编写原生代码。
- 🔄 **通信机制**：通过 `postMessage`/`onMessage` 进行主机与沙盒间的序列化数据通信。
- 🛡️ **安全特性**：支持通过 `allowedTurboModules` 属性白名单控制沙盒可访问的 TurboModules，默认仅允许 `NativeMicrotasksCxx`。
- 📁 **项目结构**：采用 monorepo 结构，包含核心库包和多个示例应用。
- 🚀 **使用示例**：提供主机应用与沙盒应用的代码示例，展示消息传递和错误处理。
- 🗺️ **发展路线**：计划支持 Android、沙盒间通信、RE.Pack 集成、增强安全功能、存储隔离和开发者工具。
- ⚠️ **安全考虑**：涵盖 TurboModules 状态共享、性能资源耗尽、文件系统存储冲突及平台特定风险（如 iOS 的 `NSNotificationCenter`）。
- 📄 **许可证与资源**：项目采用 MIT 许可证，提供详细 API 文档和示例，欢迎贡献与反馈。

---

### [GitHub - xojs/xo: ❤️ 拥有出色默认配置的 JavaScript/TypeScript 代码检查工具（ESLint 封装）· GitHub](https://github.com/xojs/xo)

**原文标题**: [GitHub - xojs/xo: ❤️ JavaScript/TypeScript linter (ESLint wrapper) with great defaults · GitHub](https://github.com/xojs/xo)

XO 是一个基于 ESLint 的 JavaScript/TypeScript 代码检查工具，提供开箱即用的严格且可读的代码规范，支持零配置使用，同时允许通过配置文件进行自定义。它集成了多个实用的 ESLint 插件，支持 TypeScript、React 等框架，并具备自动修复、缓存等便捷功能。

- 🛠️ **零配置与高度可定制**：提供预设的严格代码规范，无需额外配置即可使用，同时也支持通过 `xo.config.js` 等文件进行详细设置。
- 🔧 **多框架与语言支持**：默认支持 TypeScript，并可轻松扩展以支持 React、Astro、Svelte 和 Vue 等框架。
- ⚡ **高效与便捷功能**：包含自动修复错误、缓存提升性能、编辑器集成以及通过命令行快速检查和修复代码。
- 🎨 **代码风格与格式化**：默认使用制表符缩进和分号，但可通过选项调整为空格或无分号风格，并支持与 Prettier 集成以实现自动代码格式化。
- 📦 **丰富的生态系统**：提供适用于各种编辑器和构建系统的插件，以及可独立使用的 ESLint 共享配置，方便不同开发场景集成。

---

### [Poku - 让测试变得简单](https://poku.io/)

**原文标题**: [Poku - Making Testing Easy](https://poku.io/)

Poku 是一款免费开源的跨平台测试运行器，旨在为 JavaScript 测试带来简洁高效的体验，支持 Node.js、Bun 和 Deno 等多平台。

- 🐷 **核心定位**：免费开源的跨平台测试运行器，专注于还原 JavaScript 测试的本质
- ⚡️ **学习路径**：提供从初级到高级的教程，涵盖断言基础、测试组织（TDD/BDD）到 API、容器等复杂测试场景
- 🌐 **跨平台测试**：支持同时为 Node.js、Bun 和 Deno 运行相同测试套件，确保代码兼容性
- 🧪 **实际应用**：已被 MySQL2 等开源项目采用，支持 CommonJS 与 ES 模块，并能自测试（使用 TypeScript 无需编译）
- 📦 **安装方式**：可通过 npm、Bun、Deno 等包管理器快速安装，遵循 MIT 开源协议

---

### [GitHub - isaacs/sax-js：适用于JavaScript的SAX风格解析器 · GitHub](https://github.com/isaacs/sax-js)

**原文标题**: [GitHub - isaacs/sax-js: A sax style parser for JS · GitHub](https://github.com/isaacs/sax-js)

sax-js 是一个用于解析 XML 和 HTML 的 SAX 风格解析器，主要设计用于 Node.js 环境，但也适用于浏览器或其他 CommonJS 实现。它支持流式处理，提供多种事件监听和配置选项，适用于处理 RSS 等 XML 文档，但并非完整的 HTML 解析器或 DOM 构建工具。

- 📄 **SAX 风格解析器**：用于解析 XML 和 HTML，支持流式处理，适用于 Node.js 和浏览器环境。
- ⚙️ **灵活配置**：提供严格模式、格式化选项（如修剪、规范化、小写转换）和命名空间支持。
- 🚫 **功能限制**：非 HTML 解析器、DOM 构建器或 XML 验证器，对 DTD 和实体支持有限。
- 📖 **基本用法**：通过事件监听（如 `opentag`、`text`、`error`）处理数据，支持写入和关闭流。
- 🔧 **高级特性**：包括错误恢复、位置跟踪、处理指令和 CDATA 块解析。
- 🐛 **问题报告**：鼓励通过编写失败测试来报告问题，确保准确复现和修复。
- 📚 **资源丰富**：提供完整的文档、贡献指南、行为准则和安全策略，项目活跃且维护良好。

---

### [发布 v17.0.0 · LuanRT/YouTube.js · GitHub](https://github.com/LuanRT/YouTube.js/releases/tag/v17.0.0)

**原文标题**: [Release v17.0.0 · LuanRT/YouTube.js · GitHub](https://github.com/LuanRT/YouTube.js/releases/tag/v17.0.0)

这是一个名为 YouTube.js 的开源 JavaScript 库的 GitHub 仓库页面，主要展示了其最新版本 v17.0.0 的发布信息。

- 🚨 **重大变更**：更新了搜索过滤器以匹配 YouTube 的改动，并移除了因 YouTube 不再提供而失效的“热门”趋势获取功能。
- ✨ **新增功能**：支持“语音增强”和“超分辨率”格式，新增了视频摘要内容解析器，并添加了 ANDROID_VR 客户端支持。
- 🐛 **问题修复**：修复了包括频道子菜单解析、内容元数据处理、播放器新变体支持在内的多个问题，并更新了工作流配置。

---

### [GitHub - ItalyPaleAle/svelte-spa-router: 使用 Svelte 的单页面应用路由器 · GitHub](https://github.com/ItalyPaleAle/svelte-spa-router)

**原文标题**: [GitHub - ItalyPaleAle/svelte-spa-router: Router for SPAs using Svelte · GitHub](https://github.com/ItalyPaleAle/svelte-spa-router)

这是一个专为 Svelte 5 应用设计的单页面应用（SPA）路由器，采用哈希路由实现，无需服务器端处理，适合静态 SPA。它支持动态导入、路由参数、查询字符串解析和活动链接高亮等功能，可通过编程或链接进行导航。

- 🚀 **专为 Svelte 5 设计**：优化用于单页面应用，采用轻量级哈希路由，无需服务器支持。
- 📦 **简单易用**：通过对象或 Map 定义路由，支持参数（如`/book/:id?`）和正则表达式匹配。
- 🔄 **动态导入与代码分割**：支持`wrap()`方法实现按需加载组件，提升性能。
- 🔗 **多种导航方式**：支持`<a>`标签、`use:link`动作及`push()`、`pop()`等编程式导航。
- 🎯 **路由参数与查询字符串**：通过`params`传递路径参数，`router.querystring`获取查询字符串。
- 💡 **高级功能**：包括路由包装、预条件、静态属性、嵌套路由和滚动位置恢复等。
- 📚 **丰富资源**：提供示例代码、升级指南和高级用法文档，社区活跃（1.6k 星）。

---

### [发布 0.18.0 版本 · foliojs/pdfkit · GitHub](https://github.com/foliojs/pdfkit/releases/tag/v0.18.0)

**原文标题**: [Release 0.18.0 · foliojs/pdfkit · GitHub](https://github.com/foliojs/pdfkit/releases/tag/v0.18.0)

PDFKit 是一个用于 Node.js 和浏览器的 PDF 文档生成库，最新版本 v0.18.0 修复了多项问题并增加了新功能。

- 🐛 修复了 Chrome/Edge 中复制文本时字符混乱的问题
- ♿ 解决了链接和表格的可访问性问题
- 🖼️ 修正了交错 PNG 图像和 SVG 路径解析错误
- 📄 新增页面布局和用户单位自定义选项
- 🔗 支持带自定义缩放级别的页面跳转大纲
- 🛡️ 增强了 JPEG 图像和加密库的稳定性
- 📝 修复了换页时的文本缩进问题

---

### [GitHub - cypress-io/eslint-plugin-cypress：适用于使用Cypress项目的ESLint插件 · GitHub](https://github.com/cypress-io/eslint-plugin-cypress)

**原文标题**: [GitHub - cypress-io/eslint-plugin-cypress: An ESLint plugin for projects that use Cypress · GitHub](https://github.com/cypress-io/eslint-plugin-cypress)

这是一个用于 Cypress 测试的 ESLint 插件，提供代码规范检查和最佳实践规则，支持 ESLint v9 及以上版本，并采用 Flat 配置文件格式。

- 🛠️ **插件功能**：为 Cypress 测试提供 ESLint 规则，强制执行最佳实践，如禁止不必要的等待、避免链式调用等
- 📦 **安装要求**：需要 ESLint v9 或 v10，通过 npm 或 yarn 安装 eslint-plugin-cypress
- ⚙️ **配置方式**：必须使用 Flat 配置文件格式（eslint.config.mjs），不再支持旧版 eslintrc 格式
- 🌐 **全局变量**：提供 configs.globals 配置，定义 Cypress 测试中常用的全局变量如 cy、Cypress 等
- ✅ **推荐规则**：提供 configs.recommended 配置，包含多个推荐的代码规范规则
- 🔧 **规则示例**：包括禁止异步测试、禁止使用 cy.pause()、禁止不必要的等待时间等规则
- 🧩 **扩展集成**：支持与 eslint-plugin-mocha 和 eslint-plugin-chai-friendly 插件配合使用
- 📝 **规则禁用**：支持在文件、代码块或单行级别禁用特定规则
- 🤝 **开源贡献**：项目采用 MIT 许可证，欢迎贡献规则、修复和功能改进

---

### [GitHub - cypress-io/cypress：为任何在浏览器中运行的程序提供快速、简便且可靠的测试。· GitHub](https://github.com/cypress-io/cypress)

**原文标题**: [GitHub - cypress-io/cypress: Fast, easy and reliable testing for anything that runs in a browser. · GitHub](https://github.com/cypress-io/cypress)

Cypress 是一个现代化的前端测试框架，专注于为浏览器中运行的任何应用提供快速、简单且可靠的测试解决方案。

- 🚀 **快速易用的测试工具** – 支持 Mac、Linux 和 Windows，可通过 npm、yarn 或 pnpm 轻松安装。
- 🌐 **全面的测试能力** – 提供端到端测试、组件测试，并支持 React、Vue、Angular、Svelte 等前端框架的测试库。
- 📈 **活跃的开源项目** – 拥有 49.6k 星标、3.4k 分支和 1.5m+ 用户，社区贡献规范清晰。
- 📜 **MIT 许可证** – 项目采用 MIT 开源协议，提供完整的代码行为准则、贡献指南和安全政策。
- 🛠️ **丰富的开发资源** – 包含详细的文档、更新日志、路线图，并支持 Cypress Cloud 集成和测试状态徽章。

---

### [JSNation——2026 年主要 JavaScript 大会](https://jsnation.com/?utm_source=partner&utm_medium=jsweekly)

**原文标题**: [JSNation – the main JavaScript conference of 2026](https://jsnation.com/?utm_source=partner&utm_medium=jsweekly)

JSNation 是一场为期两天的 JavaScript 国际会议，将于 2026 年 6 月 11 日（阿姆斯特丹线下 + 线上）和 6 月 15 日（纯线上）举行。会议聚焦全栈开发、AI 工程等前沿趋势，汇聚 50 多位行业顶尖演讲者和数千名开发者，旨在通过主题演讲、深度研讨会和丰富的社交活动，共同探索 Web 开发的未来。

- 🗓️ **会议时间**：2026 年 6 月 11 日（混合模式）与 6 月 15 日（远程）
- 🎤 **核心规模**：50+ 位演讲者，1500 名现场参会者，超 1 万人远程参与
- 🚀 **聚焦主题**：全栈开发与架构、AI 辅助编程、AI 工程、向高级工程师与 Tech Lead 的成长路径
- 🌐 **技术热点**：涵盖 TypeScript、Vite、Node.js、Docker、AI 工具链（如 Claude Code、Cursor）等
- 🏙️ **活动亮点**：线下派对、城市导览、工作坊、开源奖项及丰富的社交环节
- 🎟️ **票务选择**：提供线下 + 线上混合票、纯远程票以及包含酒店的组合票等多种选项
- 🤝 **社区支持**：提供多样性奖学金，并设有 JS 开源奖项以鼓励社区贡献

---

### [49MB 的网页 | thatshubham](https://thatshubham.com/blog/news-audit)

**原文标题**: [The 49MB Web Page | thatshubham](https://thatshubham.com/blog/news-audit)

现代新闻网站为了追求短期广告收益，普遍采用对用户不友好的设计，导致页面臃肿、加载缓慢，并严重侵犯用户体验与隐私。

- 📰 **页面臃肿与性能问题**：以《纽约时报》为例，加载一个页面需要 49MB 数据和 422 个网络请求，耗时两分钟，远超早期操作系统或整张音乐专辑的大小。
- 🕵️ **过度追踪与隐私侵犯**：网站加载时，浏览器被迫处理大量程序化广告竞价请求和跟踪脚本，导致 CPU 占用高、电池消耗快，用户数据在未经充分同意下被多方收集。
- 💸 **敌对性用户体验设计**：为了提升广告展示时间和点击率，网站普遍采用侵入式弹窗、自动播放视频、布局偏移（CLS）等设计，迫使用户进行大量无关操作才能阅读内容。
- 📱 **移动端体验恶化**：有限的屏幕空间被广告、固定栏位和弹窗大量占据，实际内容区域仅占一小部分，增加了用户的交互成本和阅读负担。
- 🔧 **可行的改进方案**：通过延迟弹窗触发、预留广告空间、使用轻量级文本版本（如 text.npr.org）和 RSS 订阅等方式，可以在不牺牲收益的前提下大幅提升用户体验。
- ⚖️ **商业与用户体验的平衡**：当前新闻网站的设计源于短期广告收益的激励，而非工程师的本意；用户可以通过关闭页面、使用 RSS 等方式表达不满，促使行业反思与改进。

---

### [Difftastic，一种结构化差异工具](https://difftastic.wilfred.me.uk/)

**原文标题**: [Difftastic, a structural diff](https://difftastic.wilfred.me.uk/)

Difftastic 是一款基于语法而非逐行比较的 CLI 差异工具，它通过解析代码结构提供更准确、易读的差异对比，支持多种编程语言和文件格式，并能与 Git 集成。

- 🧠 基于语法解析差异：使用 tree-sitter 解析代码结构，精准识别表达式层面的变化，避免逐行对比的局限
- 🎨 忽略格式变动：自动过滤换行、缩进等纯格式修改，突出实际内容变更
- 🔗 智能匹配包装层：即使修改内部内容，也能清晰显示新增的包装结构（如函数或条件语句）
- 📏 直观行号显示：直接展示文件修改前后的真实行号，替代传统的`@@`语法标记
- 🌍 多语言支持：兼容 C++、Java、Python、Rust 等主流编程语言及 JSON、YAML 等文件格式
- 🔧 Git 集成：可通过配置与 Git 工作流无缝结合
- 📜 开源免费：采用 MIT 许可证，支持自由使用、修改和分享

---

### [支持的语言 - Difftastic 手册](https://difftastic.wilfred.me.uk/languages_supported.html)

**原文标题**: [Languages Supported - Difftastic Manual](https://difftastic.wilfred.me.uk/languages_supported.html)

本文列出了 difftastic 工具支持的所有编程语言与结构化文本格式，并提供了每种语言对应的解析器来源。

- 📜 支持通过命令 `difft --list-languages` 查看当前安装版本支持的语言列表
- 💻 涵盖多种编程语言，包括 Ada、C/C++、Java、Python、Rust、Go、JavaScript 等，均使用 tree-sitter 解析器
- 🏗️ 支持结构化文本格式，如 JSON、YAML、XML、HTML、CSS 和 TOML 等
- 🔗 每种语言均对应明确的 tree-sitter 语法库来源，便于开发者查阅和扩展

---

### [Visual Studio Code 1.111](https://code.visualstudio.com/updates/v1_111)

**原文标题**: [Visual Studio Code 1.111](https://code.visualstudio.com/updates/v1_111)

Visual Studio Code 1.111 版本于 2026 年 3 月 9 日发布，这是首个每周稳定版。本次更新重点增强了 AI 代理体验，引入了代理权限控制、Autopilot 预览、代理作用域钩子预览和调试事件快照等功能，同时改进了聊天提示、终端 AI CLI 分组，并优化了扩展开发和工程流程。

- 🚀 **代理权限控制**：新增权限选择器，可针对每个会话调整代理的自主程度，包括默认批准、绕过批准和 Autopilot 预览三级权限。
- 🤖 **Autopilot 预览**：代理可自主迭代直至完成任务，默认在 Insiders 版本中启用，稳定版需通过设置开启。
- 🔗 **代理作用域钩子预览**：支持在特定代理的 YAML 前言中定义钩子，实现专属的前后处理逻辑，不影响其他聊天交互。
- 🐛 **调试事件快照**：可通过`#debugEventsSnapshot`将代理调试事件快照附加为聊天上下文，便于排查代理行为和自定义问题。
- 💡 **聊天提示改进**：重新设计了提示体验，提供结构化入门引导，并新增`/init`和`/fork`命令提示，优化多会话下的显示逻辑。
- 📁 **终端 AI CLI 分组实验功能**：AI CLI 终端配置（如 GitHub Copilot CLI）现可在终端配置下拉菜单的专属分组中显示，提升可发现性。
- 🛠️ **扩展开发支持**：为扩展`package.json`中的本地化字符串添加了基础 IntelliSense 功能，包括跳转到定义和查找所有引用。
- ⚙️ **工程流程优化**：新增一键创建测试计划项、自动生成验证步骤、PR 媒体自动附加至关联问题等功能，提升开发效率。
- ⏳ **功能弃用通知**：编辑模式自 1.110 版本起正式弃用，临时启用设置将支持至 1.125 版本，之后将完全移除。
- 🙏 **致谢贡献者**：列出了对 vscode、vscode-copilot-chat 和 language-server-protocol 仓库做出贡献的开发者及修复内容。

---

### [Amazon S3 通用存储桶账户区域命名空间简介 | AWS 新闻博客](https://aws.amazon.com/blogs/aws/introducing-account-regional-namespaces-for-amazon-s3-general-purpose-buckets/)

**原文标题**: [Introducing account regional namespaces for Amazon S3 general purpose buckets | AWS News Blog](https://aws.amazon.com/blogs/aws/introducing-account-regional-namespaces-for-amazon-s3-general-purpose-buckets/)

AWS 宣布为 Amazon S3 通用存储桶推出账户区域命名空间功能，允许用户基于自身账户和区域创建唯一命名的存储桶，简化存储桶管理并确保名称可用性。

- 🆔 账户区域命名空间通过附加账户和区域后缀（如 `-123456789012-us-east-1-an`）确保存储桶名称在账户内唯一，其他账户无法使用相同后缀
- 🔐 支持通过 IAM 策略和 AWS Organizations 服务控制策略，利用 `s3:x-amz-bucket-namespace` 条件键强制团队仅创建账户区域命名空间内的存储桶
- 🖥️ 用户可通过 Amazon S3 控制台、AWS CLI 或 AWS SDK（如 Boto3）创建账户区域命名空间存储桶，需指定 `x-amz-bucket-namespace:account-regional` 请求头
- 📝 AWS CloudFormation 支持通过伪参数（如 `AWS::AccountId` 和 `AWS::Region`）或 `BucketNamePrefix` 属性简化账户区域命名空间存储桶的模板创建
- ⚠️ 现有全局存储桶无法重命名为账户区域命名空间格式，该功能仅适用于新建通用存储桶，且已在 37 个 AWS 区域（包括中国和 GovCloud 区域）免费推出

---

### [桶占位终告终结——一朵云足矣](https://onecloudplease.com/blog/bucketsquatting-is-finally-dead)

**原文标题**: [Bucketsquatting is (Finally) Dead – One Cloud Please](https://onecloudplease.com/blog/bucketsquatting-is-finally-dead)

AWS S3 引入新的命名空间机制，有效防止桶名被恶意抢注的安全问题，推荐用户在新创建存储桶时采用此模式。

- 🛡️ AWS S3 新增命名空间保护机制，格式为`<前缀>-<账户ID>-<区域>-an`，防止桶名被其他账户抢注
- 🔒 新机制通过账户专属命名空间确保桶名唯一性，抢注尝试将返回`InvalidBucketNamespace`错误
- 📝 AWS 建议默认采用此命名模式，并支持通过 SCP 策略强制实施
- ⚠️ 现有存储桶不受自动保护，需手动迁移至新命名桶
- ☁️ 其他云服务商采用不同防护策略：Google Cloud 依赖域名验证，Azure 则受限于存储账户名称长度

---

### [亚马逊 S3 二十年：构建未来之路 | AWS 新闻博客](https://aws.amazon.com/blogs/aws/twenty-years-of-amazon-s3-and-building-whats-next/)

**原文标题**: [Twenty years of Amazon S3 and building what’s next | AWS News Blog](https://aws.amazon.com/blogs/aws/twenty-years-of-amazon-s3-and-building-whats-next/)

Amazon S3 在 20 年前以低调姿态推出，现已发展成为存储行业基石，服务数百万客户，存储超 500 万亿对象，价格下降约 85%，并始终保持核心设计原则与 API 向后兼容性，未来致力于成为所有数据和 AI 工作负载的通用基础。

- 🚀 **推出与理念**：2006 年 3 月 14 日，Amazon S3 以极简公告推出，旨在通过简单接口提供可扩展、可靠且经济的存储，让开发者专注于高阶工作。
- 🛡️ **核心原则**：始终遵循安全、持久性（11 个 9 设计）、可用性、性能和弹性五大基础，确保服务稳定可靠。
- 📈 **规模增长**：从最初 1PB 存储、5GB 最大对象，扩展到如今数百 EB 数据、500 万亿对象、50TB 最大对象，覆盖 123 个可用区和 39 个 AWS 区域。
- 💰 **成本降低**：价格从每 GB 15 美分降至略高于 2 美分，降幅约 85%，并通过智能分层等为客户节省超 60 亿美元存储成本。
- 🔧 **技术演进**：通过微服务持续检查数据完整性，使用形式化方法验证代码正确性，并逐步用 Rust 重写性能关键代码以提升安全与效率。
- 🔄 **行业影响**：S3 API 已成为存储行业参考标准，多厂商提供兼容工具，技能可跨平台转移，且 2006 年的代码至今仍可无缝运行。
- 🧠 **未来愿景**：超越存储服务，成为 AI 与分析的数据基础，推出 S3 Tables、S3 Vectors 和 S3 Metadata 等功能，支持多数据类型直接处理，降低成本与复杂性。

---

