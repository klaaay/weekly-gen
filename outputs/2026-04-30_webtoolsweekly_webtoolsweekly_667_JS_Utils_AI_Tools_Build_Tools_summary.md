### [#1 可视化网站反馈工具，用于 Bug 追踪 | BugHerd](https://bugherd.com/ref/home?utm_campaign=546ab5cc34f8&utm_medium=partnerships&utm_source=partnerstack&pscd=partners.bugherd.com&ps_partner_key=NTQ2YWI1Y2MzNGY4&ps_xid=Kvx64pph9uhCju&gsxid=Kvx64pph9uhCju&gspk=NTQ2YWI1Y2MzNGY4)

**原文标题**: [#1 Visual Website Feedback Tool For Bug Tracking | BugHerd](https://bugherd.com/ref/home?utm_campaign=546ab5cc34f8&utm_medium=partnerships&utm_source=partnerstack&pscd=partners.bugherd.com&ps_partner_key=NTQ2YWI1Y2MzNGY4&ps_xid=Kvx64pph9uhCju&gsxid=Kvx64pph9uhCju&gspk=NTQ2YWI1Y2MzNGY4)

BugHerd 是一款让客户反馈变得极其简单的网站反馈工具，用户只需点击和评论即可，系统会自动抓取截图和技术细节并生成任务。

- 🎯 **核心功能**：客户无需登录即可在网页上直接点击留下反馈，系统自动捕获截图、浏览器、操作系统等技术细节，并生成可追踪的任务卡片。
- 🗂️ **任务管理**：所有反馈自动转化为看板任务，支持与 Asana、Jira、Trello 等 20 多种项目管理工具集成，方便团队优先处理。
- 🤝 **客户协作**：客户无需账户即可参与反馈，支持设置反馈截止日期、权限控制，并拥有专属的任务看板视图。
- 🎥 **视频反馈**：支持录制和分享交互式反馈会话，让沟通更直观。
- 🤖 **AI 辅助**：BugHerd AI（Beta 版）可智能辅助反馈管理，提升效率。
- 🌐 **公共反馈**：网站上线后可通过公共反馈小部件持续收集访客意见。
- 💰 **定价与试用**：计划从 $42/月起，提供 7 天免费试用和 60 天退款保证，无需信用卡。
- 📈 **用户口碑**：4.8/5 评分，全球超过 35 万用户和 1 万家公司使用，94% 用户报告客户满意度提升，93% 缩短交付时间。
- 🔧 **适用场景**：特别适合营销机构、网页开发团队和内部团队，用于 UAT 测试、Bug 追踪、网站反馈、在线校对等。

---

### [GitHub - pinojs/redact · GitHub](https://github.com/pinojs/redact)

**原文标题**: [GitHub - pinojs/redact · GitHub](https://github.com/pinojs/redact)

@pinojs/redact 是一个用于 JavaScript 应用的智能对象编辑库，它通过选择性克隆而非直接修改原始对象，提供安全且高性能的数据编辑功能。

- 🔒 **安全性优先**：采用选择性克隆技术，绝不修改原始对象，并支持在 `serialize: false` 模式下恢复原始值
- ⚡ **性能优化**：通过路径预分析和选择性克隆，仅复制需要编辑的分支，非编辑属性共享原始引用，大幅降低内存使用
- 🔧 **完整 API 支持**：兼容 fast-redact 的路径语法（点号、括号、数组索引、通配符），并支持自定义编辑值、序列化函数和键移除功能
- 🚀 **性能对比**：小对象约 690ns（比 fast-redact 慢 3.5 倍），大对象最小编辑时约 18μs（性能相近），通配符模式约 48μs（仅慢 1.3 倍）
- 🎯 **适用场景**：当不可变性、对象共享、函数式编程或调试时需要保留原始数据时使用；高速场景（>100,000 ops/sec）建议使用 fast-redact
- 🧪 **全面测试**：包含 16 个单元测试和 16 个集成测试，覆盖核心功能、边缘情况以及与 fast-redact 的输出兼容性

---

### [GitHub - GoogleChromeLabs/view-transitions-mock: 同文档视图转换的非视觉填充库 · GitHub](https://github.com/GoogleChromeLabs/view-transitions-mock)

**原文标题**: [GitHub - GoogleChromeLabs/view-transitions-mock: A non-visual polyfill for Same-Document View Transitions · GitHub](https://github.com/GoogleChromeLabs/view-transitions-mock)

view-transitions-mock 是一个非视觉的 Same-Document View Transitions 模拟实现，它符合规范但省略了动画部分，允许在任何浏览器中使用 View Transitions 的 JavaScript API，无需担心原生支持问题。

- 📦 提供 `document.startViewTransition()` 和 `ViewTransition` 类的完整 API 模拟，包括 Promise 和 View Transition Types
- 🚫 不模拟伪元素树、CSS 属性和选择器以及动画，仅聚焦于 JavaScript 接口
- ✨ 通过 `register()` 函数注册后，可消除代码中的 `if (document.startViewTransition)` 检查，简化跨浏览器开发
- ⚙️ 支持自定义注册配置：`requireTypes`（默认 true）和 `forced`（默认 false），可灵活控制模拟行为
- 🌐 兼容多种浏览器环境，包括无原生 VT 支持、部分支持（如无 View Transition Types）和完全支持的浏览器
- 🧪 使用 Playwright 在 Chromium、Firefox 和 WebKit 上进行测试，确保可靠性
- 📄 基于 Apache 2.0 许可证开源，并欢迎社区贡献

---

### [GitHub - open-circle/formisch: 适用于任何框架的模块化且类型安全的表单库 · GitHub](https://github.com/open-circle/formisch)

**原文标题**: [GitHub - open-circle/formisch: The modular and type-safe form library for any framework · GitHub](https://github.com/open-circle/formisch)

Formisch 是一个基于 schema、无头表单库，支持多种 JS 框架，具有类型安全、高性能和模块化设计的特点。

- 📦 极小的包体积，起步仅 2.5 kB
- ✅ 基于 Valibot 的 schema 验证，支持编辑器自动补全
- ⚡ 细粒度的 DOM 更新，性能出色
- 🧩 简洁、可读且经过深思熟虑的 API
- 🌐 支持所有原生 HTML 表单字段
- 🛠️ 提供多种方法（如 focus、reset、validate）以编程方式控制表单
- 🔗 框架无关的核心，针对不同框架插入原生响应式块，实现原生性能
- 👥 有合作伙伴支持，并鼓励社区贡献
- 📜 基于 MIT 许可证免费开源

---

### [GitHub - 0xGF/boneyard: 自动生成的骨架加载框架 · GitHub](https://github.com/0xGF/boneyard)

**原文标题**: [GitHub - 0xGF/boneyard: Auto generated skeleton loading framework · GitHub](https://github.com/0xGF/boneyard)

boneyard 是一个像素级精确的骨架屏加载框架，能从真实 UI 自动提取占位元素，无需手动测量或调整。支持 React、Vue、Svelte 5、Angular、Preact 和 React Native，提供 CLI、Vite 插件和多种配置选项。

- 🚀 支持 React、Vue、Svelte 5、Angular、Preact 和 React Native 框架
- 🎯 通过 CLI 或 Vite 插件自动生成骨架屏，无需手动测量
- 📱 支持响应式断点（默认 375、768、1280）和动态字体缩放
- 🔧 提供丰富的动画样式（脉冲、闪烁、实心）和自定义配置
- 📦 使用 `npx boneyard-js build` 命令即可生成骨架屏文件
- 🖼️ React Native 支持设备端自动扫描，零生产开销
- 🛠️ 支持 watch 模式，在 HMR 更新时重新捕获骨架
- 📚 提供详细的文档、npm 包和 Twitter 支持

---

### [GitHub - isaac-mason/crashcat: 用于 JavaScript 的物理引擎，专为游戏、模拟和创意网站构建 · GitHub](https://github.com/isaac-mason/crashcat)

**原文标题**: [GitHub - isaac-mason/crashcat: physics engine for javascript, built for games, simulations, and creative websites · GitHub](https://github.com/isaac-mason/crashcat)

crashcat 是一个专为游戏、模拟和创意网站设计的纯 JavaScript 物理引擎，支持刚体模拟、约束、碰撞检测等功能，并具有高度可摇树优化的特性。

- 🎯 支持刚体模拟，包括静态、动态和运动学三种运动类型
- 📦 提供多种碰撞形状：球体、盒子、胶囊体、圆柱体、凸包、三角网格和复合形状
- 🔗 内置 8 种约束类型（铰链、滑块、距离、点、固定、锥形、摇摆 - 扭转、六自由度），支持电机和弹簧
- ⚡ 实现连续碰撞检测（CCD），防止快速移动物体穿模
- 🎭 灵活的两层碰撞过滤系统：宽相位层和对象层，支持位掩码和自定义回调
- 🔧 提供监听器钩子，可响应和修改碰撞事件（接触添加、持久化、移除）
- 🌳 使用动态包围盒层次结构（BVH）加速宽相位空间查询
- 😴 支持刚体休眠，提升性能
- 👻 传感器刚体用于触发区域检测，不施加物理力
- 🌲 纯 JavaScript 编写，高度可摇树优化，仅加载所需功能
- 🔌 与任何 JavaScript 引擎/库兼容（Three.js、Babylon.js、PlayCanvas 等）
- 📚 提供完整的 API 文档和多种示例（射线投射、车辆、布娃娃、角色控制器等）
- 🛠️ 支持自定义形状，适用于体素世界、可破坏地形等高级场景
- 🔄 支持多物理世界和世界状态序列化（JSON）
- 🧪 提供 Three.js 调试渲染器，可视化物理状态
- 💡 优化建议：使用简单形状、复用形状、启用休眠、减少求解器迭代次数

---

### [officeParser | 适用于 Node.js 和浏览器的最多功能 Office 解析器](https://officeparser.harshankur.com/)

**原文标题**: [officeParser | The Most Versatile Office Parser for Node.js & Browser](https://officeparser.harshankur.com/)

概述摘要
- 📊 每周下载量超过 26 万次，总下载量突破 1000 万次
- 📁 支持 8 种以上办公文档格式：DOCX、XLSX、PPTX、PDF、ODT、ODS、ODP、RTF
- 🌳 输出结构化抽象语法树 (AST)，精准反映文档层级
- 📎 支持提取嵌入的图片、图表和对象等附件
- 🔍 集成 OCR 功能，可识别文档图片中的文字（基于 Tesseract.js）
- ℹ️ 提供完整的文档元数据，包括作者、创建日期等
- ⚡ 针对服务端和浏览器环境均优化了性能
- ⚙️ 支持自定义分隔符、注释处理和解析深度
- 🛠️ 提供详细配置说明、AST 参考文档和调试指南
- 🖥️ 配备 AST 可视化工具，可实时预览解析结果

---

### [GitHub - adrianbrowning/mdcode-ts · GitHub](https://github.com/adrianbrowning/mdcode-ts)

**原文标题**: [GitHub - adrianbrowning/mdcode-ts · GitHub](https://github.com/adrianbrowning/mdcode-ts)

mdcode-ts 是一个用 TypeScript 重写的 Markdown 代码块管理工具，用于提取、更新和管理 Markdown 文档中的代码块。

- 📝 支持从 Markdown 文档中提取、更新和管理代码块
- 🛠️ 提供多种命令：列出代码块、提取到文件、从文件更新、运行 shell 命令、创建 tar 存档
- 🧩 项目结构清晰，包含核心类型定义、自定义解析器、区域处理模块和命令实现
- 🔧 技术栈为 TypeScript（严格模式）、Node 22 内置 API、commander 命令行解析、node:test 测试框架
- 🧪 支持单元测试和端到端集成测试，使用 pnpm 管理依赖
- 📜 基于 MIT 许可证，原始 Go 实现由 szkiba 开发

---

### [GitHub - Secreto31126/whatsapp-api-js：一个轻量级、无依赖、高效的TypeScript库，用于与WhatsApp Cloud API 交互 · GitHub](https://github.com/Secreto31126/whatsapp-api-js)

**原文标题**: [GitHub - Secreto31126/whatsapp-api-js: A lightweight, dependency-less, efficient TS library for interacting with WhatsApp Cloud API · GitHub](https://github.com/Secreto31126/whatsapp-api-js)

这是一个轻量级、无依赖的 TypeScript 库，用于与 WhatsApp Cloud API 交互，支持消息收发、Webhook 设置和多种消息类型。

- 📦 **轻量高效**：无外部依赖，使用 TypeScript 开发，性能优越。
- 🤖 **消息处理**：支持文本、图片、文档等多种消息类型的发送和接收。
- 🔗 **Webhook 集成**：内置 GET 和 POST 处理程序，方便设置 Webhook 认证与消息更新。
- 📚 **完整文档**：提供详细文档、示例和类型定义，便于快速上手。
- 🛠️ **灵活配置**：支持临时或永久 API 令牌，以及应用密钥设置。
- 🌐 **跨平台兼容**：适用于 Node.js、Deno 等多种运行环境。
- 📅 **持续更新**：拥有 112 个版本发布，包括 Beta 版本和新功能（如语音笔记支持）。
- 👥 **社区贡献**：由多位贡献者维护，支持贡献指南和安全策略。

---

### [GitHub - maximhq/bifrost: 最快企业级 AI 网关（比 LiteLLM 快 50 倍），具备自适应负载均衡器、集群模式、防护机制、支持 1000+ 模型，在 5000 RPS 下开销低于 100 微秒。](https://github.com/maximhq/bifrost)

**原文标题**: [GitHub - maximhq/bifrost: Fastest enterprise AI gateway (50x faster than LiteLLM) with adaptive load balancer, cluster mode, guardrails, 1000+ models support & <100 µs overhead at 5k RPS. · GitHub](https://github.com/maximhq/bifrost)

Bifrost AI Gateway 是一款高性能 AI 网关，通过统一的 OpenAI 兼容 API，快速连接 15+AI 提供商，具备自动故障转移、负载均衡、语义缓存和企业级功能。

- ⚡ **极速部署**：30 秒内即可通过 npx 或 Docker 启动，零配置即可运行，并配有 Web 界面进行可视化管理。
- 🔗 **统一接口**：提供单一 OpenAI 兼容 API，支持 OpenAI、Anthropic、AWS Bedrock、Google Vertex 等 15+ 提供商。
- 🛡️ **高可靠性**：具备自动故障转移和智能负载均衡，确保零停机时间，在 5k RPS 下实现 100% 成功率。
- 🧠 **智能缓存**：基于语义相似度的响应缓存，有效降低成本和延迟。
- 🔧 **高级功能**：支持 MCP 协议、多模态、自定义插件、预算管理、SSO 集成和 Vault 密钥管理。
- 📊 **卓越性能**：在 5k RPS 基准测试中，每个请求仅增加 11 微秒的极低开销。
- 🎯 **灵活集成**：可作为 HTTP 网关、Go SDK 或直接替换 OpenAI/Anthropic SDK，无需修改代码。
- 🏢 **企业就绪**：支持私有部署、集群模式、安全控制和治理功能，适合大规模生产环境。

---

### [GitHub - punkpeye/fastmcp：用于构建MCP服务器的TypeScript框架。· GitHub](https://github.com/punkpeye/fastmcp)

**原文标题**: [GitHub - punkpeye/fastmcp: A TypeScript framework for building MCP servers. · GitHub](https://github.com/punkpeye/fastmcp)

FastMCP 是一个基于 TypeScript 的框架，用于快速构建 MCP 服务器，它封装了官方 SDK 的复杂性，提供开箱即用的功能。

- 🚀 **核心功能**：提供工具、资源和提示的简单定义，支持认证、会话跟踪、日志、错误处理、HTTP 流式传输、HTTPS、自定义路由、边缘运行时和无状态模式。
- 🛠️ **工具定义**：支持使用 Zod、ArkType、Valibot 等标准模式库定义工具参数，并可返回文本、图片、音频等多种内容类型。
- 🔐 **认证与授权**：内置 OAuth 2.1 支持（Google、GitHub、Azure 等），并提供 `requireAuth`、`requireScopes` 等辅助函数进行细粒度工具访问控制。
- 🌐 **传输方式**：支持 stdio、HTTP 流式传输和 SSE，并可配置 HTTPS 和自定义 HTTP 路由。
- ☁️ **边缘计算**：提供 `EdgeFastMCP` 类，支持部署到 Cloudflare Workers、Deno Deploy 等边缘运行时。
- 📊 **会话与事件**：自动管理会话 ID 和请求 ID，支持会话级状态、服务器事件监听和采样请求。
- 🧪 **测试与调试**：提供 `fastmcp dev` 和 `fastmcp inspect` CLI 命令，方便在终端或 Web UI 中测试和调试服务器。

---

### [CanIRun.ai — 你的机器能运行 AI 模型吗？](https://www.canirun.ai/)

**原文标题**: [CanIRun.ai — Can your machine run AI models?](https://www.canirun.ai/)

该页面是一个本地运行 AI 模型的兼容性查询工具，帮助用户根据硬件配置选择可运行的模型，并提供了丰富的模型列表和筛选选项。

- 🖥️ 页面核心功能是检测用户电脑的 GPU、VRAM、RAM 等硬件规格，并据此评估不同 AI 模型的运行表现（从“运行极佳”到“过于沉重”共 6 个等级）。
- 📊 模型列表按评分、参数量、上下文长度、速度、VRAM 占用等维度排序，并支持按任务类型（聊天、代码、推理、视觉）、提供商（如 Meta、Alibaba、Google）和许可证（如 Apache 2.0、MIT）筛选。
- 🏆 热门模型包括 Llama 3.1 8B（Meta）、Qwen 3.5 9B（Alibaba）、Phi-4 14B（Microsoft）、DeepSeek R1（DeepSeek）等，覆盖从 0.6B 到 1T 参数量的多种规模。
- 🔧 每个模型提供量化版本（如 Q2_K、Q4_K_M、F16）和详细规格（参数量、上下文长度、架构类型、活跃参数等），方便用户根据硬件选择最优配置。
- 🌐 数据来源包括 llama.cpp、Ollama 和 LM Studio，页面由 midudev 为本地 AI 社区构建，不隶属于任何商业公司。

---

### [订阅 | 超人 AI](https://www.superhuman.ai/subscribe?utm_source=wp_ads&utm_medium=Web+Tools+Weekly&utm_content=v2-r648962-p828140-c45336&transaction_id=10235a7b79bc32ce4da5095ca4dff7)

**原文标题**: [Subscribe | Superhuman AI](https://www.superhuman.ai/subscribe?utm_source=wp_ads&utm_medium=Web+Tools+Weekly&utm_content=v2-r648962-p828140-c45336&transaction_id=10235a7b79bc32ce4da5095ca4dff7)

概述摘要  
- 🤖 **SUPERHUMAN AI** 专注于 AI 工具、教程和新闻，每日仅需 3 分钟学习。  
- 📈 **百万读者** 已加入，旨在通过 AI 提升生产力和加速职业发展。  
- 🔑 **注册即可获取** 超过 1000 个提示词、AI 课程和速查表。  
- 🔒 **隐私政策** 和 **使用条款** 确保用户数据安全与合规。

---

### [GitHub - google/A2UI · GitHub](https://github.com/google/A2UI)

**原文标题**: [GitHub - google/A2UI · GitHub](https://github.com/google/A2UI)

A2UI 是一个开源项目，提供了一种声明式格式和渲染器，让 AI 智能体能够生成或填充丰富的用户界面，旨在实现安全、跨平台且可增量更新的 UI 交互。

- 🛡️ **安全优先**：A2UI 使用声明式 JSON 数据格式而非可执行代码，客户端维护可信组件目录，智能体只能请求渲染这些组件，确保安全。
- 🤖 **LLM 友好且可增量更新**：UI 表示为扁平组件列表，带有 ID 引用，便于 LLM 逐步生成，支持渐进式渲染和高效增量更新。
- 🔄 **框架无关且可移植**：将 UI 结构与其实现分离，智能体发送抽象组件描述，客户端可映射到 Flutter、Angular、Lit 等不同框架的原生组件。
- 🧩 **灵活性与开放注册**：提供开放注册模式，允许开发者将服务器端类型映射到自定义客户端实现，包括安全 iframe 容器，并可在自定义组件逻辑中强制执行沙箱策略。
- 🚀 **多种使用场景**：支持动态数据收集（如生成定制表单）、远程子智能体（如旅行预订代理返回 UI 负载）和自适应工作流（如企业代理动态生成审批仪表板）。
- 🏗️ **清晰架构**：流程包括智能体生成 A2UI JSON 响应、通过传输协议发送、客户端解析 JSON、渲染器将抽象组件映射到具体实现。
- 🛠️ **快速入门选项**：提供多种入门路径，包括约 5 分钟的完整餐厅查找器演示、与 CopilotKit 集成的 AG-UI 设置、可视化编辑器 A2UI Composer，以及无需安装的 A2UI Theater。
- 🗺️ **未来路线图**：计划包括规范稳定化（v1.0）、增加更多渲染器（React、Jetpack Compose、SwiftUI 等）、支持更多传输协议（REST）和更多智能体框架（Genkit、LangGraph 等）。

---

### [GitHub - numman-ali/openskills: AI 编码代理的通用技能加载器 - npm i -g openskills · GitHub](https://github.com/numman-ali/openskills)

**原文标题**: [GitHub - numman-ali/openskills: Universal skills loader for AI coding agents - npm i -g openskills · GitHub](https://github.com/numman-ali/openskills)

OpenSkills 是一個為 AI 編碼代理提供通用技能加載器的工具，能讓任何支援 `AGENTS.md` 的代理使用 Anthropic 的技能系統。

- 🚀 **快速入門**：通過 `npx openskills install` 和 `npx openskills sync` 即可安裝和同步技能，支援專案本地或全域安裝。
- ✅ **核心優勢**：與 Claude Code 完全相容，適用於多種 AI 代理（如 Cursor、Windsurf），支援按需加載以保持上下文簡潔，並可與專案版本控制整合。
- 🧠 **運作原理**：在 `AGENTS.md` 中生成與 Claude Code 相同的 `<available_skills>` XML，代理通過 `npx openskills read <name>` 動態加載技能。
- 🔧 **安裝來源**：可從 Anthropic 市場、任意 GitHub 倉庫、本地路徑或私有 Git 倉庫安裝技能。
- 🌍 **通用模式**：使用 `--universal` 參數將技能安裝到 `.agent/skills/`，避免與 Claude 插件市場衝突，支援多代理配置。
- 🧰 **命令列表**：提供 install、sync、list、read、update、manage、remove 等命令，並支援 `--global`、`--universal` 等選項。
- 🧬 **技能格式**：技能使用 `SKILL.md` 文件，包含名稱、描述和具體指令，按需加載以保持代理上下文整潔。
- 🧪 **自創技能**：只需 `SKILL.md` 文件即可創建技能，支援資源文件夾和符號鏈接進行本地開發。
- 🔄 **更新技能**：可通過 `npx openskills update` 刷新從 Git 倉庫安裝的技能，支援指定技能名稱。
- ❓ **常見問題**：CLI 設計比 MCP 更輕量，適合靜態指令和資源，無需伺服器，與所有代理相容。
- 📋 **要求**：需要 Node.js 20.6+ 和 Git。

---

### [claude-devtools — 你的 Claude 在盲目编码](https://www.claude-dev.tools/)

**原文标题**: [claude-devtools — Your Claude is coding blind](https://www.claude-dev.tools/)

概述总结  
- 🔍 Claude Code 从版本 v2.1.20 开始隐藏了详细操作记录，仅显示模糊摘要，引发社区不满  
- 🛠️ claude-devtools 是一款开源工具，无需 API 密钥或配置，能读取本地 `~/.claude/` 会话日志，还原被隐藏的细节  
- 📊 上下文重构功能：按 7 个类别（如 CLAUDE.md、工具 I/O、思考步骤等）可视化每次对话的 token 使用和压缩过程  
- 🔧 工具调用检查器：可展开被折叠的“读取 3 个文件”等操作，显示语法高亮的代码、差异和子代理执行树  
- 🌳 团队与子代理树：为每个代理显示独立执行树，包含工具追踪、token 指标、耗时和成本  
- 🔔 通知触发器：支持对 .env 文件访问、工具错误、高 token 使用等设置系统通知和正则匹配  
- 🌐 SSH 远程会话：支持检查远程机器上的会话，兼容代理转发和密钥认证  
- ⌨️ 命令面板（Cmd+K）：跨会话搜索，显示上下文片段和高亮关键词，可直接跳转到特定消息  
- 📐 多面板布局：可并排打开多个会话，拖放标签页，分割视图，对比会话  
- 🖥️ 支持 macOS（Homebrew 或 .dmg）、Windows、Linux（AppImage/.deb/.rpm），以及 Docker 自托管（浏览器 UI，零出站网络调用）

---

### [Stagehand | Browserbase](https://www.browserbase.com/stagehand)

**原文标题**: [Stagehand | Browserbase](https://www.browserbase.com/stagehand)

### 概述摘要
Stagehand 是一个开源 AI 浏览器代理 SDK，结合了脚本的精确性与 AI 的灵活性，通过自然语言指令实现浏览器自动化，支持 act、extract、observe、agent 四种核心操作，并具备自愈能力，可应对页面变化。

- 🤖 **核心功能**：提供 act（执行操作）、extract（提取数据）、observe（观察页面）、agent（自主工作流）四种原语，支持自然语言指令。
- 🔧 **自愈能力**：使用自然语言指令（如“点击提交按钮”）而非硬编码选择器，能自动适应页面 DOM 变化，减少维护成本。
- 📊 **数据提取**：通过 Zod 模式验证从页面提取结构化数据，确保输出准确可靠。
- 🛡️ **安全可控**：比传统框架（如 Selenium）更智能，比黑盒 AI 代理更安全，兼具代码可预测性与 AI 适应性。
- 🌐 **开源免费**：完全开源（MIT 许可），支持 TypeScript 和 Python，可本地运行或部署到 Browserbase 云浏览器。
- ⚡ **生产就绪**：支持多种 LLM 提供商（OpenAI、Anthropic、Google Gemini），与 Browserbase 集成后可获得会话重放、验证码解决等高级功能。
- 📚 **社区支持**：提供 Discord 社区和 GitHub 仓库，方便获取帮助和贡献代码。

---

### [GitHub - mindfold-ai/Trellis：最佳智能体框架](https://github.com/mindfold-ai/Trellis)

**原文标题**: [GitHub - mindfold-ai/Trellis: The best agent harness. · GitHub](https://github.com/mindfold-ai/Trellis)

Trellis 是一个面向团队的 AI 编码工具链，通过渐进式规范、任务上下文和跨平台支持，提升 AI 编码的可靠性和效率。

- 🎯 **核心定位**：Trellis 是一个内置的团队 AI 编码工具链，将大型系统提示转化为渐进式 Wiki，包含规范、任务、工作流和日志，仅在需要时加载。
- 🔧 **工作原理**：在仓库中安装 `.trellis/` 目录，为不同 AI 编码平台生成入口点，通过规范、任务、工作区和平台适配器分层管理。
- 🔄 **核心循环**：捕获任务为 PRD → 注入相关规范 → 代理在边界内实现 → 检查后交接 → 将可复用经验提升为规范 → 记录会话供后续代理使用。
- 📦 **安装与使用**：需要 Node.js >= 18 和 Python >= 3.9，通过 `npm install -g @mindfoldhq/trellis@beta` 安装，用 `trellis init -u your-name` 初始化仓库。
- 🚀 **任务启动**：在支持钩子的平台上自动加载会话上下文，否则通过 `/start` 或 `/trellis:start` 手动加载，用自然语言描述任务，通过技能路由工作。
- 🤔 **常见问题**：Trellis 不同于单一文件如 `CLAUDE.md`，它添加了范围规范、任务 PRD、工作流门控和工作区内存；不仅限于 Claude Code，支持多种编码代理；适用于个人和团队。
- 📊 **项目状态**：拥有 6.8k 星标、374 个分支、73 个发布标签，采用 AGPL-3.0 许可证，主要语言为 TypeScript (49.5%) 和 Python (41.1%)。

---

### [FrontendAtlas 核心 60 题与面试练习 | FrontendAtlas](https://frontendatlas.com/?utm_source=webtoolsweekly&utm_medium=sponsorship&utm_campaign=middle_image_ad_apr30)

**原文标题**: [FrontendAtlas Essential 60 and Interview Practice | FrontendAtlas](https://frontendatlas.com/?utm_source=webtoolsweekly&utm_medium=sponsorship&utm_campaign=middle_image_ad_apr30)

overview summary
FrontendAtlas 是一个前端面试准备平台，提供真实编码工作流程的练习，包含 500+ 问题、实时反馈和面试官导向的评估。

- 🎯 核心练习流程：在真实 IDE 中编写代码、运行确定性测试、预览 UI 输出、审查边界情况和权衡
- 📚 推荐准备路径：Essential 60 → 问题库 → 学习计划/框架准备 → 最终轮覆盖
- 🛠️ 支持多种技术栈：React、Angular、Vue、HTML/CSS、JavaScript，并提供交互式演示
- 🧠 高级练习模式：包含调试场景和权衡对决，测试压力下的思考能力
- 💼 公司专项练习：提供 Google、Amazon、Netflix、Apple 等公司的定制化面试准备
- ⚡ 独特功能：框架感知问题、真实编辑器、前端系统设计、离线优先持久化、实用测试
- 📈 学习路径：提供 7 天冲刺和 30 天基础两种结构化学习计划
- 💰 定价方案：月付$12、季付$29、年付$79、终身$199
- 🔍 额外工具：ATS 简历扫描器，帮助优化简历通过率

---

### [GitHub - twoslashes/twoslash：用于提前在文档中生成丰富类型信息的标记语言](https://github.com/twoslashes/twoslash)

**原文标题**: [GitHub - twoslashes/twoslash: Markup for generating rich type information in your documentations ahead of time. · GitHub](https://github.com/twoslashes/twoslash)

Twoslash 是一个为 TypeScript 代码设计的标记格式，旨在创建自包含的代码示例，让 TypeScript 编译器提前完成类型信息的生成工作。它是 @typescript/twoslash 的继任项目，基于 MIT 许可证开源。

- 📚 **文档与迁移指南**：提供详细的文档和迁移指南，帮助用户快速上手。
- 🔧 **核心功能**：通过标记格式，在文档中提前生成丰富的类型信息，提升代码示例的准确性。
- ⚙️ **技术栈**：主要使用 TypeScript（96.9%），辅以 HTML 和 JavaScript。
- 🌟 **社区活跃**：获得 886 颗星标、43 个复刻，并有 36 个发布版本。
- 🏗️ **项目结构**：包含 .github、.vscode、bench、docs、packages 等目录，支持贡献和协作。
- 🔗 **相关主题**：与 typescript、shiki、twoslash 紧密相关，适用于文档生成场景。
- 📄 **许可证**：采用 MIT 许可证，由 Orta Therox、Anthony Fu 和微软公司共同维护。

---

### [GitHub - voidzero-dev/vite-plus: Vite+ 是统一的工具链和 Web 开发入口点。它在一个地方管理您的运行时、包管理器和前端工具链。](https://github.com/voidzero-dev/vite-plus)

**原文标题**: [GitHub - voidzero-dev/vite-plus: Vite+ is the unified toolchain and entry point for web development. It manages your runtime, package manager, and frontend toolchain in one place. · GitHub](https://github.com/voidzero-dev/vite-plus)

Vite+ 是一个面向 Web 开发的统一工具链，集成了运行时管理、包管理、开发、测试、构建、代码检查、格式化、打包及单仓库任务缓存等功能，全部通过一个零配置工具实现。

- 🚀 **统一工具链**：整合 Vite、Vitest、Oxlint、Oxfmt、Rolldown、tsdown 和 Vite Task，提供单一依赖的开发体验。
- 🛠️ **核心命令**：支持 `vp env`（Node.js 版本管理）、`vp install`（自动检测包管理器安装依赖）、`vp dev`（快速开发服务器）、`vp check`（格式化+lint+ 类型检查）、`vp test`（测试）、`vp build`（生产构建）、`vp run`（单仓库任务缓存调度）、`vp pack`（库打包）、`vp create`/`vp migrate`（项目脚手架和迁移）。
- ⚙️ **单一配置**：通过 `vite.config.ts` 统一配置开发服务器、测试、lint、格式化、任务运行和暂存文件工作流，类型安全且共享默认值。
- 📦 **包管理集成**：自动封装 pnpm、npm 或 Yarn，支持 `add`、`remove`、`update`、`dedupe`、`outdated`、`list`、`why`、`info`、`link`/`unlink` 和 `pm` 命令。
- 🚀 **快速入门**：Linux/macOS 使用 `curl -fsSL https://vite.plus | bash`，Windows 使用 `irm https://viteplus.dev/install.ps1 | iex` 全局安装 `vp`。
- 🔄 **项目迁移**：`vp migrate` 自动将 `.oxlintrc*`、`.oxfmtrc*` 和 lint-staged 配置合并到 `vite.config.ts`。
- 🤖 **CI/CD 支持**：提供官方 `setup-vp` GitHub Actions，支持 Node.js 版本和缓存。
- 🔧 **手动安装**：需安装 `vite-plus` 和 `@voidzero-dev/vite-plus-core`，并在包管理器配置 overrides 以使用 Vite+ 版本。
- 📜 **开源许可**：完全开源，采用 MIT 许可证。
- 🏆 **社区支持**：感谢 namespace.so 提供免费的 CI/CD 运行环境。

---

### [GitHub - frakjs/frak: 一个用于将文件同步到远程服务器的命令行部署工具。](https://github.com/frakjs/frak)

**原文标题**: [GitHub - frakjs/frak: A commandline deployment tool for syncing files to remote servers. · GitHub](https://github.com/frakjs/frak)

概述摘要  
frak 是一个轻量级 JavaScript 部署工具，通过 SSH 和 rsync 实现快速、可靠的文件传输，支持差异预览、历史备份和回滚等功能。

- 🔌 一次初始化，随时部署，简化文件同步流程  
- 🔎 推送前提供交互式差异预览，方便检查变更  
- 📦 在服务器上存储基于补丁的备份，支持轻松回滚  
- 🧾 支持部署后执行自定义命令（如重启服务）  
- 📡 提供快速 SSH 控制台访问部署目录  
- 🔁 支持拉取功能，便于同步回本地更改  
- 📋 备份检查功能，显示新增和删除文件摘要  
- ⚙️ 通过 npx 运行，无需全局安装，配置简单  
- 🚀 未来计划包括 Slack 通知和并行多环境部署

---

### [学习 Visual Studio Code](https://lazarpress.gumroad.com/l/learnvscode)

**原文标题**: [Learn Visual Studio Code](https://lazarpress.gumroad.com/l/learnvscode)

概述：本文探讨了人工智能在医疗诊断中的应用，强调了其提升准确性和效率的潜力，同时指出了数据隐私和算法偏见等挑战。

- 🩺 人工智能通过分析医学影像和患者数据，显著提高了疾病诊断的准确率。
- ⏱️ 自动化诊断工具减少了医生的工作负担，加快了诊断流程。
- 🔒 数据隐私问题成为主要障碍，需要严格保护患者信息不被滥用。
- ⚖️ 算法偏见可能导致诊断结果不公平，需确保训练数据的多样性。
- 🌐 跨机构数据共享有助于提升 AI 模型性能，但需解决法律和伦理问题。

---

### [JavaScript 单体仓库中的依赖版本一致性 | Syncpack](https://syncpack.dev/)

**原文标题**: [Consistent dependency versions in JavaScript Monorepos | Syncpack](https://syncpack.dev/)

Syncpack 是一款用于大型 JavaScript Monorepo 中保持依赖版本一致性的命令行工具，被 AWS、Microsoft、Vercel 等众多知名公司使用。

- 🔧 可查找并修复依赖版本不匹配问题
- 🧩 支持单一版本策略或分区独立策略
- 📦 能从 npm 注册表中查找并更新过时版本
- 🔒 确保某些依赖始终固定在特定版本
- 🚫 禁止某些依赖在全局或特定位置使用
- 🎯 定义精确或宽松 semver 范围的使用规则
- 📋 将特定包设为依赖版本的唯一来源
- ✨ 统一排序和格式化 package.json 文件
- 🚀 通过 npx 快速试用，如 `npx syncpack list --dependency-types prod`
- 📥 正式安装时建议放入 devDependencies，使用 `npm install syncpack --save-dev`
- 🔍 支持 `lint`、`fix`、`update` 等命令，可配合 `--help` 查看文档
- ⚙️ 通过 `.syncpackrc` 配置文件自定义行为，如使用 Version Groups 管理依赖
- 🏷️ 支持 `workspace:*` 协议确保本地包引用正确
- 📚 建议阅读 Peer Dependencies 和 Semver Groups 配置指南以深入理解

---

### [Deno 沙箱](https://deno.com/deploy/sandbox)

**原文标题**: [Deno Sandbox](https://deno.com/deploy/sandbox)

Deno Sandbox 是一个用于安全运行不可信代码的云端微虚拟机 SDK，专为 AI 代理和开发者设计，提供即时启动、严格隔离和灵活控制。

- 🚀 **极速启动**：新沙箱可在 93 毫秒内创建完成，支持按需即时启动
- 🔒 **安全隔离**：每个沙箱都是独立的 Firecracker 微 VM，拥有自己的文件系统、网络栈和进程树
- 🌐 **网络控制**：可精确限制沙箱的对外连接，防止数据泄露或未经授权的通信
- 🔑 **安全密钥管理**：密钥仅在连接授权目标时注入网络层，恶意代码无法读取
- 💻 **多语言支持**：当前支持 JavaScript、TypeScript 和 Python，Deno 预装可直接运行
- 🛠 **开发工具集成**：支持 HTTP 预览、SSH 连接和 VSCode 编辑器即时访问
- 📦 **持久化文件系统**：每个沙箱拥有独立的持久化存储空间
- 💰 **按需付费**：CPU $0.05/小时，内存 $0.016/GiB-小时，存储 $0.20/GiB-月
- 🌍 **全球部署**：可选择美国或欧洲区域运行沙箱，亚洲区域即将推出
- ✅ **合规认证**：SOC2 和 ISO27001 认证，企业合同可提供 HIPAA BAA

---

### [Frontmatter — 面向 Astro 开发者的构建时工具](https://www.frontmatter.tech/)

**原文标题**: [Frontmatter — Build-time tools for Astro developers](https://www.frontmatter.tech/)

概述摘要  
- 🛠️ 提供一套构建时工具，用于在 Astro 中构建 UI，并自动生成数据契约和后端集成模板。  
- 🔓 核心层为开源且免费，可扫描 Astro 项目并输出稳定的 JSON IR，作为其他工具的基础。  
- 💰 Solo 版一次性付费 49 美元，可从 Astro 项目生成渲染包（Twig 或纯 PHP 模板），无需重写或运行时。  
- 🚀 Studio 版即将推出，为 Astro 站点添加可编辑层，代码保留布局，内容转为数据。  
- 👤 Frontmatter 由 Alexandre Desane 开发，核心采用 MIT 许可，付费工具为一次性购买，无订阅或托管服务，集成由开发者负责。

---

### [GitHub - davialabs/davia: 为编码代理设计的交互式可编辑文档 · GitHub](https://github.com/davialabs/davia)

**原文标题**: [GitHub - davialabs/davia: Interactive, editable docs designed for coding agents · GitHub](https://github.com/davialabs/davia)

Davia 是一个面向 AI 编码代理的开源工具，用于生成交互式、可编辑的代码库文档，支持本地和云端协作。

- 📖 **核心功能**：为 AI 编码代理生成交互式内部文档，包含可视化图表和可编辑白板，支持 Notion 式平台或 IDE 内编辑
- 🚀 **快速启动**：通过 npm 全局安装 CLI 工具，使用`davia init`初始化并指定代理名称（如 cursor、github-copilot 等）
- 📝 **文档生成**：AI 代理利用 Davia 工具生成带可视化和白板的交互式文档，通过`davia open`在浏览器查看
- 🤝 **团队协作**：使用`davia push`将本地文档同步至云端工作区，支持实时协作（当前暂不支持更新已推送的工作区）
- 🔧 **技术栈**：基于 TypeScript（96.3%）、CSS、JavaScript 构建，采用 MIT 许可证开源
- 🌟 **社区贡献**：欢迎通过提交 Issue、Pull Request 或 Discord 反馈参与项目改进
- 🎯 **项目定位**：专为 AI 工具设计的文档生成器，支持本地 wiki、知识库和文档生成，已有 1.6k 星标和 121 个复刻

---

### [GitHub - chr15m/minimal-pwa: 渐进式 Web 应用的最小文件与配置](https://github.com/chr15m/minimal-pwa)

**原文标题**: [GitHub - chr15m/minimal-pwa: Minimal files + config for a PWA · GitHub](https://github.com/chr15m/minimal-pwa)

概述总结  
- 📂 这是一个名为 minimal-pwa 的公开代码仓库，包含构建渐进式 Web 应用所需的最少文件集。  
- ⭐ 该项目获得 472 颗星，26 个分支，拥有 4 位关注者。  
- 📄 核心文件包括 manifest.json、sw.js 和 index.html，用于在 Android 和 iOS 上实现 PWA 安装功能。  
- 🔧 提供单文件版本 single-file-pwa.html，通过 JavaScript 动态生成 manifest.json，无需 service worker 即可安装。  
- 🏷️ 项目主题标签包括：template、pwa、minimal、web-app。  
- 🌐 项目主页为 mccormick.cx/minimal-pwa，主要使用 HTML（97.7%）编写，辅以 Makefile 和 JavaScript。

---

### [联系 Web Tools Weekly](https://webtoolsweekly.com/contact?opt=classifieds)

**原文标题**: [Contact Web Tools Weekly](https://webtoolsweekly.com/contact?opt=classifieds)

### 概述总结
本文提供了联系方式和广告咨询的详细说明，包括不同广告方案的选择及提交表单的指引。

- 📧 广告咨询需通过指定表单提交，仅限广告相关询问
- 💼 提供多种广告方案：顶部广告 + 文本链接、付费产品评测、中部图片广告、文本链接组合、分类列表、广告交换
- 🚫 非广告咨询（如新闻订阅或工具提交）需通过 X、Bluesky 私信或回复订阅邮件联系
- 📝 表单必填项包括：姓名、邮箱、广告链接及所选方案
- 💬 评论/说明栏可补充额外信息

---

### [命令代码](https://commandcode.ai/)

**原文标题**: [Command Code](https://commandcode.ai/)

Command Code 是一款能持续学习开发者编码偏好的 AI 编程助手，通过其专有的 taste-1 模型实现个性化编码体验，大幅提升开发效率。

- 🚀 **核心功能**：Command Code 能持续学习你的编码风格，从每一次接受、拒绝和编辑中自动构建项目级别的“taste”技能。
- 🧠 **技术驱动**：采用 taste-1 元神经符号 AI 模型，结合持续强化学习，将 LLM 与你的编码偏好深度融合。
- ⚡ **效率提升**：宣称可实现编码快 10 倍、代码审查快 2 倍、Bug 减少 5 倍，避免重复修正 AI 生成的“平庸代码”。
- 🛠️ **多种模式**：提供交互式 CLI、无头模式（-p, --yolo）和后台沙盒模式，适应不同工作流。
- 📦 **完整工具链**：支持全栈项目开发，包括文件操作、shell 命令、grep 搜索、扩展思考，以及 /skills、/review 等指令。
- 🔧 **可扩展性**：支持自定义 /agents、/memory、/skills、/commands、MCP 服务器和插件，方便团队协作。
- 🤝 **团队协作**：通过 /share sessions 和 `npx taste push/pull` 实现跨项目和团队的 taste 共享。
- 🌟 **社区反馈**：开发者表示使用一周后，AI 不再重复之前需要手动修正的错误，减少了 80% 的修正工作，无需重复说明偏好。

---

### [Refind – 每日精选，滋养大脑](https://refind.com/?utm_source=xn6y&utm_medium=ran-x-rfnd)

**原文标题**: [Refind – Brain food, delivered daily](https://refind.com/?utm_source=xn6y&utm_medium=ran-x-rfnd)

每日为您精选优质资讯，助您拓展思维。

- 📚 每日精选：从海量文章中筛选出最精华的内容，每日推送。
- ✉️ 便捷订阅：只需提供邮箱，即可每日接收高质量资讯。
- 🧠 广受欢迎：已获得超过 50 万求知者的信赖与喜爱。
- ⭐ 口碑卓越：用户评分高达 4.9/5 星，品质备受认可。

---

### [svelte0](https://svelte0.com/)

**原文标题**: [svelte0](https://svelte0.com/)

这是一个基于文本提示，利用 AI 快速构建 Svelte Web 应用的工具。

- 🤖 通过简单的文字描述，即可生成 Svelte Web 应用
- 🧠 使用 Claude Sonnet 4.5 模型驱动，智能理解需求
- 📝 支持生成注册表单、定价卡片、产品网格、认证表单和用户资料卡等多种 UI 组件

---

### [Solo - 免费 AI 网站创建工具](https://soloist.ai/)

**原文标题**: [Solo - Free AI Website Creator](https://soloist.ai/)

本服务提供免费快速建站方案，支持多行业模板与 AI 辅助设计，帮助用户轻松创建专业网站。

- 🚀 免费建站：无需编程，输入简单信息即可快速生成网站，并免费连接自定义域名
- 🎯 多行业覆盖：提供会计师、理发店、餐厅等 30+ 行业模板，满足不同业务需求
- 🤖 AI 智能辅助：自动组织页面结构、生成初始图片，并添加 SEO 关键词提升搜索流量
- 📱 移动端适配：网站自动优化桌面和移动端显示，无需额外操作
- 📅 预约集成：支持连接 Calendly 等日历服务，方便客户在线预约服务
- 💬 客户联系：内置联系表单，客户消息直达邮箱，便于跟进
- 🔗 社交媒体链接：可在页眉页脚展示社交媒体链接，提升品牌曝光
- 🛒 产品销售：通过服务版块添加产品定价，集成 Stripe/PayPal 支付链接
- 👥 团队协作：支持邀请编辑者共同设计网站，或转移所有权
- 📊 数据分析：可连接 Google Analytics 查看访问来源、页面浏览量等数据
- ⭐ 用户好评：用户称赞界面直观、操作简单，20 分钟内即可完成建站
- ❓ 常见问题：提供免费基础版和付费 Pro 版，非营利组织可享折扣

---

### [2026 年生成式 AI 与 ChatGPT 大师课程套装 | StackSocial](https://www.stacksocial.com/sales/the-2025-generative-ai-chatgpt-master-course-bundle?aid=a-lq08jv8f)

**原文标题**: [The 2026 Generative AI & ChatGPT Master Course Bundle | StackSocial](https://www.stacksocial.com/sales/the-2025-generative-ai-chatgpt-master-course-bundle?aid=a-lq08jv8f)

本课程包提供从零基础到精通的 Python 及生成式 AI 综合训练，包含 5 门课程共 41.6 小时内容，现以 19.99 美元特价出售（节省 80%）。

- 🐍 **Python 编程基础与实战**：101 节课程（10.6 小时），涵盖安装、数据类型、循环、函数、类等核心内容，适合所有水平学习者
- 🤖 **机器学习项目：心脏病预测分析**：53 节课程（7 小时），通过实际项目掌握机器学习应用
- 📊 **数据科学：ChatGPT 在 Python 与数据科学中的应用**：36 节课程（5 小时），学习如何利用 ChatGPT 提升数据分析效率
- 🎨 **生成式 AI 与 ChatGPT 大师课程（含 20 种 AI 工具）**：74 节课程（7 小时），探索多种 AI 工具的实际应用场景
- 🔬 **生成式 AI 在数据分析与工程中的应用**：99 节课程（12 小时），深入掌握 AI 驱动的数据处理与工程实践
- ✅ **终身访问权限**：所有课程均可永久回看，支持桌面和移动设备访问
- 🏆 **证书与支持**：完成课程可获得结业证书，但无字幕且不支持离线下载
- ⏳ **兑换期限**：购买后 30 天内需兑换代码，未兑换可 30 天内退换

---

### [Alloy · 使用真实产品进行 AI 原型设计](https://alloy.app/)

**原文标题**: [Alloy · AI prototyping with your real product](https://alloy.app/)

### 概述总结
Alloy 是一个面向产品团队的云端开发平台，支持连接代码库、即时分享原型，并可直接推送生产级代码，加速产品迭代。

- 🚀 **云端开发环境**：无需本地配置，直接连接代码库或通过浏览器扩展捕获页面，从真实产品开始构建。
- 🔗 **即时分享与协作**：每个会话通过链接分享，团队成员和客户可实时查看、评论和反馈。
- 💡 **快速原型构建**：通过提示生成新想法，自动匹配现有组件和设计系统，确保品牌一致性。
- 🛠️ **从灵感到代码**：支持从 20 多个集成导入需求，直接构建并推送至 GitHub 生成 Pull Request。
- 🔒 **企业级安全**：平台设计注重数据安全，支持代码库会话、文件夹组织、评论和响应式聊天等功能。
- 📅 **最新功能**：2026 年新增代码库会话、文件夹管理、上下文评论和实时生成进度显示。
- ❓ **常见问题**：支持现有产品集成（代码库或扩展），与 Claude Code 区别在于云端协作，无需本地环境；与 Figma 暂不直接导入，但可导出原型。

---

### [桌面优先环境管理 | Ghostable](https://ghostable.dev/)

**原文标题**: [Desktop-First Environment Management | Ghostable](https://ghostable.dev/)

### 概述总结
Ghostable 是一款桌面端环境变量管理工具，旨在替代繁琐的 .env 文件传递和终端操作，提供集中化的变量查看、验证、历史追踪和零知识加密功能。

- 🖥️ **桌面优先**：提供 macOS 桌面应用，作为日常环境管理的专属工作空间，告别在仪表盘、仓库和旧消息中翻找变量。
- 🔍 **集中浏览与搜索**：按组织、项目和环境统一管理变量，支持按键名搜索、表格/分组视图切换，并可导入/导出 .env 文件。
- ✅ **配置验证**：利用共享的 schema 文件（.ghostable）定义全局或环境特定规则，在部署前捕获缺失键、错误值或错误假设。
- 📜 **变更历史**：追踪组织、项目和环境的操作记录，查看每个变量的版本历史，并可一键恢复到旧值，避免配置管理变成“考古”。
- 🔑 **自动化隔离**：为 CI 和脚本签发作用域受限的部署令牌，人类使用 UI，自动化使用令牌和 CLI，互不干扰。
- 🔒 **零知识加密**：环境数据在可信客户端加密后才存储或同步，明文和私钥仅保留在需要它们的客户端上，Ghostable 无法读取。
- ❓ **常见问题**：支持与 Laravel、Node、Python 等主流技术栈配合使用；不强制使用 CLI；可导入现有 .env 文件；提供部署前验证；通过客户端加密和令牌机制实现零知识安全。

---

### [未找到标题](https://x.com/primemans/status/2049409920647463303)

**原文标题**: [No title found](https://x.com/primemans/status/2049409920647463303)

此页面提示浏览器需启用 JavaScript 才能正常访问 x.com，并提供了相关帮助与政策信息。

- 🔒 检测到浏览器中 JavaScript 被禁用，需启用或更换支持的浏览器以继续使用 x.com
- 📋 提供支持浏览器列表，可通过帮助中心查看
- ⚖️ 页面底部包含服务条款、隐私政策、Cookie 政策、版权信息等法律声明
- 🔄 若页面加载失败，可尝试重新加载
- 🛡️ 部分隐私相关扩展可能导致 x.com 异常，建议禁用后重试

---

### [未找到标题](https://x.com/LouisLazaris)

**原文标题**: [No title found](https://x.com/LouisLazaris)

此页面提示浏览器未启用 JavaScript，导致无法正常访问 x.com。

- 🔒 检测到浏览器禁用了 JavaScript，需启用后才能继续使用 x.com
- 🌐 可切换至支持的浏览器，或查看帮助中心获取浏览器列表
- 📜 页面底部提供了服务条款、隐私政策、Cookie 政策等链接
- ⚠️ 隐私相关扩展程序可能导致问题，建议禁用后重试
- 🔄 若遇到错误，可点击“重试”按钮再次尝试

---

### [@louislazaris.com 在 Bluesky 上](https://bsky.app/profile/louislazaris.com)

**原文标题**: [@louislazaris.com on Bluesky](https://bsky.app/profile/louislazaris.com)

### 概述总结
该页面是关于前端开发者 Louis Lazaris 的个人简介及资源链接集合。

- 🌐 页面需要 JavaScript 支持，属于高交互性 Web 应用
- 🔗 提供 Bluesky、AT Protocol 等平台链接
- 👤 用户 Louis Lazaris，身份为前端开发者及新闻通讯策展人
- ⚙️ 关联多个专业网站：Web Tools Weekly、Tech Productivity、VS Code Email
- 💻 个人官网及 YouTube 频道（吉他教学）链接

---

### [向 Web Tools Weekly 提交一个工具](https://webtoolsweekly.com/submit)

**原文标题**: [Submit a Tool to Web Tools Weekly](https://webtoolsweekly.com/submit)

概述摘要  
- 🔧 推荐工具：如果您开发或知道对前端开发者有用的工具，可通过 X 或 Bluesky 提交。  
- 💬 开放私信：X 平台联系@LouisLazaris，Bluesky 联系@LouisLazaris.com。  
- 📦 可提交类型：库、框架、插件、脚本、Web 应用、桌面应用、移动应用、API/服务、编辑器/IDE 等。  
- 🚫 排除内容：请勿提交文章或教程，此类内容不会被收录。  
- ⚙️ 生产力工具：已迁移至另一新闻通讯《Tech Productivity》，也可通过上述方式提交。

---

### [WeLib - 4300 万本书，9800 万篇论文。全部免费。全部属于你。](https://welib.org/)

**原文标题**: [WeLib - 43 million books, 98 million papers. All free. All yours.](https://welib.org/)

该平台提供了海量知识资源，涵盖书籍与学术论文，旨在促进深度阅读与思考，助力个人成长与精神探索。

- 📚 资源丰富：包含 4300 万册书籍与 9850 万篇学术论文，覆盖广泛领域。
- 🧬 学术直达：可直接访问近 1 亿篇学术论文，支持高效研究。
- 📖 热门推荐：精选《神圣之爱的秘密》《山就是你》《思考致富》等畅销书，涉及灵性、自我提升、成功学等主题。
- 🌱 成长导向：书籍如《心态》《铁焰》等聚焦心理成长、韧性培养与潜能开发。
- 🌍 宏观视角：《国家为什么会失败》《孙子兵法》等探讨政治、经济与战略智慧。
- 💭 反思工具：提供“诚实时刻”引导，鼓励通过日记进行深度自我反思。

---

### [Web 工具周刊 | 前端开发者周报](https://webtoolsweekly.com/)

**原文标题**: [Web Tools Weekly | A Weekly Newsletter for Front-end Developers](https://webtoolsweekly.com/)

本内容介绍了面向 Web 开发者的周刊《Web Tools Weekly》，包括订阅信息、读者评价和隐私政策。

- 📧 每周一封邮件，已有 13,569 名订阅者，无垃圾邮件
- 🔒 订阅需同意隐私政策和条款，数据通过 EmailOctopus 存储和追踪
- ⭐ 读者高度评价：多位订阅者称其为“最佳技术新闻通讯之一”
- 💡 内容实用：提供 JS 技巧、新工具和库，帮助开发者保持更新
- 📅 长期订阅者反馈：多年阅读后仍认为是最有价值的每周总结
- 👍 订阅体验：读者表示期待每一期，从未错过任何一期

---

