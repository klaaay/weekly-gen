### [TanStack AI 1.0：依然是你的 AI，依然按你的方式 | TanStack 博客](https://tanstack.com/blog/tanstack-ai-1-0)

**原文标题**: [TanStack AI 1.0: Still Your AI, Still Your Way | TanStack Blog](https://tanstack.com/blog/tanstack-ai-1-0)

TanStack AI 于 2026 年 10 月 23 日发布 1.0，核心 API 进入稳定阶段，可用于生产环境；同时推出仍处于实验阶段的 Agent Harness。文章回顾了从 Alpha 到 1.0 的演进，强调“无锁定”承诺不变：提供商、框架、沙箱和通信协议都由开发者选择。

- 🎉 **1.0 正式发布**：核心 API 稳定，面向生产；新增 Agent Harness 为实验性功能。
- 🔓 **坚持无锁定**：用户可自由选择模型提供商、UI 框架、沙箱和线协议。
- 📈 **生态大幅扩张**：从 `chat()` + 4 个提供商，发展到 23 个提供商适配器、9 个 UI 框架、11 个沙箱提供商，并支持多种编码代理。
- 🧩 **1.0 没有新概念**：移除 0.x 中已弃用的 API，替换方案此前已在 0.x 提供。
- ⚠️ **升级需整体同步**：所有稳定的 `@tanstack/ai*` 包应一起升级；Harness 相关包仍为 0.x 实验版。
- 🤖 **RC 后新增能力**：子代理、`decide()`、Agent Skills、上下文压缩、计算机使用、统一推理选项、自动提示缓存、重试、跨模型历史、Files API。
- 🔑 **密钥与登录增强**：支持 BYOK、`defineByok`、ChatGPT/GitHub Copilot/OpenRouter 登录及 Claude OAuth。
- 🔌 **MCP 能力扩展**：可将 TanStack 工具作为 MCP 服务器提供，支持工具过滤、审批、任务型工具及双向 WebMCP。
- 🌐 **适配器与框架扩展**：新增 Cloudflare Workers AI、Azure OpenAI 等适配器，支持 Remix 3、Svelte 开发工具及 5 个新沙箱提供商。
- 🧪 **开发与测试体验**：类型化无头聊天 UI 工厂、`fakeText()` 无网络测试、面向编码助手的 Agent Skills；文档已为 1.0 全面重写。
- 🛠️ **升级重点**：运行 codemod；`body` → `forwardedProps`，`conversationId` → `threadId`；`threadId` 变为必填；用 `interrupts.resolveInterrupt` 替代 `addToolApprovalResponse`；移除旧 UI 包；流结束发送 `RUN_FINISHED`；迁移已存储数据。
- 🧠 **Agent Harness**：面向长会话和持久化代理，支持持久会话、重启恢复、steer/follow-up、类型化代理、插件、多用户和后台任务。
- 💻 **可构建编码代理**：组合文件工具、权限、快照、待办、压缩等插件，并通过 `runCli` 在终端、脚本/CI、Web、ACP、MCP 中复用同一套定义。
- 🧪 **Harness 明确实验性**：`@tanstack/ai-harness` 及 CLI 为 0.x，API 可能在小版本中变化。
- 🙏 **社区与合作伙伴**：143 位贡献者参与建设，OpenRouter 等合作伙伴长期支持。
- 🔭 **后续计划**：打磨体验、支持团队落地 AI 功能、推动 Harness 稳定、增加更多提供商与沙箱。
- 📦 **快速开始**：`pnpm add @tanstack/ai @tanstack/ai-react @tanstack/ai-openai`，然后参考 Quick Start 或升级指南。

---

### [TanStack AI 1.0：依然是你的 AI，依然按你的方式 | TanStack 博客](https://tanstack.com/blog/tanstack-ai-1-0#one-more-thing-the-agent-harness)

**原文标题**: [TanStack AI 1.0: Still Your AI, Still Your Way | TanStack Blog](https://tanstack.com/blog/tanstack-ai-1-0#one-more-thing-the-agent-harness)

TanStack AI 正式发布 1.0：核心 API 稳定并可用于生产，继续坚持“不锁定供应商、框架、沙箱”的理念；同时推出实验性的 Agent Harness，并将最初单一的 `chat()` 能力扩展为覆盖聊天、工具、媒体、MCP、持久化、沙箱和智能体的完整工具集。

- 🚀 1.0 是对核心 API 的正式承诺：稳定 API 可投入生产，新 Agent Harness API 仍属实验性。
- 🧩 升级不引入新概念：0.x 中标记弃用的 API 已被移除，替代方案此前已发布；所有稳定的 `@tanstack/ai*` 包需一起升级，客户端与服务器都需 1.0，实验性 harness 包仍留在 0.x。
- 📈 生态显著扩张：从 `chat()` 和 4 个供应商适配器发展为 23 个适配器，另有 `openaiCompatible` 支持任意 OpenAI 风格 API；UI 框架覆盖 React、Vue、Solid、Svelte、Preact、Angular、Octane、Remix 和原生 JS；140 多人参与贡献。
- 🛠️ RC 后新增能力包括子智能体、`decide()` 类型化决策、可移植 Agent Skills、上下文压缩、计算机使用；统一 `reasoning`、自动提示缓存、重试、跨模型历史、Files API；BYOK 与 ChatGPT、GitHub Copilot、OpenRouter、Claude OAuth 登录。
- 🔌 MCP 能力增强：可将 TanStack 工具作为 MCP Server 提供给 Claude Desktop、Cursor 等宿主，并支持工具过滤、审批、任务型工具与双向 WebMCP。
- ☁️ 新增 Cloudflare Workers AI、Azure OpenAI、Lovable AI Gateway 等适配器，以及 Blaxel、Upstash Box、E2B、boxd、Railway 等沙箱供应商。
- 🧪 测试与开发体验提升：类型化无头聊天 UI 工厂、自定义适配器、`fakeText()` 无网络测试，以及帮助 Claude Code、Cursor 生成正确代码的 Agent Skills。
- 📚 文档为 1.0 全面重写：每页先讲问题与可运行设置，高级细节后置，适配器页面统一结构，便于横向比较。
- ⚠️ 0.x 升级要点：使用 codemod；`body` 改为 `forwardedProps`，`conversationId` 改为 `threadId`，且 `threadId` 变为必填；移除 `addToolApprovalResponse()`，改用 `interrupts.resolveInterrupt()`；流结束不再发送 `data: [DONE]`，改用 `RUN_FINISHED`；如有旧数据需按指南迁移。
- 🤖 新 Agent Harness 面向长会话与后台智能体：持久化会话、重启后继续等待审批/提问/登录、类型化智能体、插件、多用户访问控制与后台任务。
- 🧑‍💻 可用官方插件快速构建终端编码智能体，并通过 `runCli` 在终端、脚本/CI、HTTP、ACP 编辑器、MCP 宿主等场景复用一个 harness 定义。
- 🧭 Harness 被有意标为实验性：`@tanstack/ai-harness` 与 CLI 为 0.x，可能在小版本中变更；后续将打磨核心、支持团队落地、推动 harness 稳定，并扩充供应商与沙箱。

---

### [Meticulous AI - 无需编写测试的自动化前端测试](https://www.meticulous.ai/?utm_source=javascript_weekly&utm_medium=newsletter&utm_campaign=26q3_1&utm_term=primary+content)

**原文标题**: [Meticulous AI - Automated Frontend Testing Without Writing Tests](https://www.meticulous.ai/?utm_source=javascript_weekly&utm_medium=newsletter&utm_campaign=26q3_1&utm_term=primary+content)

Meticulous 是一款面向复杂代码库的自动化、穷尽式、确定性端到端视觉测试平台。它通过记录真实用户交互，由 AI 持续生成并维护覆盖全代码分支的测试套件，让开发者在合并代码前就能看到变更对用户流程的影响，并以零开发者维护成本实现可靠、无 flakes 的回归测试。

- 🚀 **零开发工作量**：无需编写、修复或维护测试，测试会随应用演进自动新增和淘汰。
- 🧠 **AI 持续生成测试**：跟踪每次交互执行的代码分支，自动策划覆盖每行代码、每个用户流程和边缘案例的视觉端到端测试。
- 📌 **开发过程即记录**：在本地开发、预发和预览 URL 中加入脚本标签即可记录会话，也可选择记录生产会话以扩大覆盖。
- 🔍 **PR 阶段预判影响**：打开拉取请求即可查看变更对用户工作流的影响，在合并前发现回归风险。
- 🧪 **后端响应回放**：默认保存并重放原始后端响应，实现无副作用测试，避免数据变化导致误报，也无需特殊测试账号或 mock 数据。
- ⚡ **从底层消除 flakes**：基于 Chromium 构建确定性调度引擎，支持极快执行，并经过复杂应用实战验证。
- 🧩 **兼容或替代现有测试**：既可补充现有测试套件，也可完全替换现有测试。
- 🖥️ **大规模并行测试**：测试在计算集群中高度并行化，可在 120 秒内测试数千个屏幕。
- 🔗 **多框架集成**：支持 NextJS、React、Vue、Angular、Nuxt、SvelteKit，并可通过 CI 集成快速接入。
- 🏢 **广泛信任**：已被 100 多家组织使用，包括 Dropbox、Notion、Engine 等；客户评价强调开发者喜爱、无需维护、无 flakes，并已成为开发流程的重要护栏。

---

### [宣布 TypeScript 7.1 Beta - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-7-1-beta/)

**原文标题**: [Announcing TypeScript 7.1 Beta - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-7-1-beta/)

TypeScript 7.1 Beta 已发布，重点带来环境模块导入属性、源阶段导入、es2026 目标与库、全新多入口 API、快照与文件系统 API、Content Mappers，以及显著的性能和内存优化；同时包含若干需要注意的行为变化，后续将推进 RC 与正式版。

- 🚀 **Beta 发布**：可通过 `npm install -D typescript@beta` 安装体验。
- 📦 **环境模块支持导入属性**：支持 `declare module "*" with { type: "css" | "text" | "bytes" }`，可根据导入属性提供正确类型，并强制导入时携带所需属性；不会校验磁盘文件，也不随 TypeScript 内置库提供。
- 🧩 **源阶段导入**：新增 `import source` 与 `import.source()`，返回 `AbstractModuleSource`；WASM 源导入可直接传给 `WebAssembly.instantiate`，并保持模块身份；需配置合适的 `--module`、`--lib` 或 `--target`。
- 🎯 **新增 `--target es2026` / `--lib es2026`**：稳定声明包括 `Math.sumPrecise()`、`Iterator.concat()`、`JSON.rawJSON()`、`Error.isError()`、`Map`/`WeakMap` 的 `getOrInsert*`、`Uint8Array` 的 Base64/Hex 方法、`Array.fromAsync()` 等。
- 🧪 **`--lib esnext` 新提案方法**：加入 `Promise.allKeyed`、`Promise.allSettledKeyed`、`Iterator.zip`、`Iterator.zipKeyed`、`Iterator.prototype.chunks/join/includes` 等。
- 🔌 **全新 TypeScript 7.1 API**：按用途拆分为 `typescript/sync`、`typescript/async`、`typescript/fs`、`typescript/ast`、`typescript/ast/is`、`typescript/ast/factory` 等入口。
- 🗂 **快照与文件系统 API**：通过 `createSnapshot` / `update` 支持增量状态更新；提供完整、带默认库、分层文件系统；`emitToString()` 可在不写盘的情况下获取输出。
- 🧱 **Content Mappers**：允许按扩展名将文件映射为虚拟内容，支持 Vue、Svelte、Astro、Ember、MDX、CSS Modules 等；需在 `tsconfig.json` 注册，CLI 使用需 `--runExternalCode`，VS Code 需工作区信任与权限。
- ⚡ **性能与内存优化**：包含大量解析、检查、构建和内存分配优化；示例中 `mui-docs` 从 22.2s 降至 11.9s（约 1.9x），内存降低 49.6%；`vscode` 从 21.6s 降至 17.7s。
- ⚠️ **行为变化**：分布式类型参数检查更严格，可能暴露既有代码中的新错误；DOM 与 `lib.d.ts` 更新也可能影响类型检查。
- 🗓 **后续计划**：接下来聚焦速度、稳定性和新功能反馈，约一个月后发布 Release Candidate，随后推出正式版。

---

### [宣布 TypeScript 7.1 Beta 发布 - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-7-1-beta/#typescript-7.1-api)

**原文标题**: [Announcing TypeScript 7.1 Beta - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-7-1-beta/#typescript-7.1-api)

TypeScript 7.1 Beta 于 2026 年 10 月 20 日发布，可通过 `npm install -D typescript@beta` 试用。本次更新重点包括环境模块导入属性、Source Phase Imports、`es2026` 目标、全新模块化 API、Content Mappers，以及显著的性能与内存优化，同时包含若干需要注意的行为变更。

- 🚀 **Beta 发布**：TypeScript 7.1 Beta 开放试用，后续将推出 Release Candidate 和正式版。
- 📦 **环境模块支持导入属性**：可在 `declare module` 中根据 `type: "css"`、`type: "text"`、`type: "bytes"` 等属性声明类型，并校验导入是否缺少必要属性。
- 🧩 **Source Phase Imports**：新增 `import source` 和动态 `import.source()`，可在模块加载前获取 `AbstractModuleSource`，尤其适用于 WebAssembly 模块实例化。
- 🎯 **新增 `es2026` 目标**：支持 `--target es2026` 和 `--lib es2026`，稳定化 `Math.sumPrecise()`、`Iterator.concat()`、`JSON.rawJSON()`、`Error.isError()`、`Uint8Array` Base64/Hex 方法等声明。
- 📚 **新增库方法**：`--lib esnext` 加入 `Promise.allKeyed`、`Promise.allSettledKeyed`、`Iterator.zip`、`Iterator.zipKeyed`、`Iterator.prototype.chunks/join/includes` 等提案方法。
- 🛠️ **全新模块化 API**：提供 `typescript/sync`、`typescript/async`、`typescript/fs`、`typescript/ast`、`typescript/ast/is`、`typescript/ast/factory` 等入口，支持编译、类型检查、AST 操作和文件系统抽象。
- 🧠 **Snapshot 与生命周期管理**：支持基于快照增量更新程序状态；`API`、`Program`、`Snapshot` 等对象为 `Disposable`，可使用 `using` 或手动释放。
- 🗂️ **文件系统 API**：提供完整虚拟文件系统、带默认库的虚拟文件系统、分层覆盖文件系统，并支持内存中编译和 `emitToString()`。
- 🧩 **Content Mappers**：将 Volar 核心模型引入 TypeScript，支持 `.vue`、`.svelte`、`.astro`、MDX、CSS Modules 等嵌入式格式；命令行需 `--runExternalCode`，VS Code 中需工作区信任和权限。
- ⚡ **性能与内存优化**：包含大量编译、类型检查、AST、缓存和内存优化；示例中 `mui-docs` 提速约 1.9x、内存降低约 49.6%，`t3code-server` 提速约 1.4x、内存降低约 24.6%。
- ⚠️ **行为变更**：对分布式类型参数的条件类型检查更严格；DOM 相关 `lib.d.ts` 更新可能影响现有类型检查。
- 🗓️ **下一步计划**：团队将聚焦速度、稳定性和新特性反馈，预计约一个月后发布 RC，随后推出正式版。

---

### [宣布 TypeScript 7.](https://devblogs.microsoft.com/typescript/announcing-typescript-7-1-beta/#source-phase-imports)

**原文标题**: [Announcing TypeScript 7.1 Beta - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-7-1-beta/#source-phase-imports)

TypeScript 7.1 Beta 已于 2026 年 10 月 20 日发布，可通过 `npm install -D typescript@beta` 安装。本次更新重点包括：环境模块中的导入属性、Source Phase Imports、`es2026` 目标、新库方法与全新 TypeScript API，同时带来显著的性能与内存优化、内容映射器支持，以及更严格的类型检查行为。

- 🚀 **环境模块导入属性**：支持 `declare module "*" with { type: "css" | "text" | "bytes" }`，可根据导入属性提供正确类型，并提示缺失属性。
- 📦 **Source Phase Imports**：新增 `import source` 与 `import.source()`，返回 `AbstractModuleSource`，可直接用于 `WebAssembly.instantiate`，并保持模块源身份一致性。
- 🎯 **新增 `--target es2026`**：稳定支持 `Math.sumPrecise()`、`Iterator.concat()`、`JSON.rawJSON()`、`Error.isError()`、`Uint8Array` Base64/Hex 方法、`Array.fromAsync()` 等。
- 🧩 **新增库方法**：`--lib esnext` 加入 `Promise.allKeyed`、`Promise.allSettledKeyed`、`Iterator.zip`、`Iterator.zipKeyed`、`Iterator.prototype.chunks/join/includes` 等提案方法。
- 🛠️ **全新 API 架构**：拆分为 `typescript/sync`、`typescript/async`、`typescript/fs`、`typescript/ast`、`typescript/ast/is`、`typescript/ast/factory` 等入口，支持同步/异步编译、AST 操作和文件系统抽象。
- ♻️ **Snapshots 与可释放对象**：API 和 Program 等对象为 `Disposable`，推荐使用 `using` 自动释放；快照可基于旧状态增量更新，避免全量重建。
- 📁 **文件系统 API**：提供 `createFileSystem`、`createFileSystemWithLib`、`createFileSystemLayer`，支持内存文件系统、分层覆盖和 `emitToString()` 等能力。
- 🧱 **Content Mappers**：Volar 核心模型成为一等公民，可为 `.vue`、`.svelte`、`.astro`、MDX、CSS Modules 等格式提供虚拟内容和映射；命令行需使用 `--runExternalCode`。
- ⚡ **性能与内存优化**：大量编译器优化使部分代码库构建速度提升最高约 1.9 倍，内存占用最高降低约 49.6%。
- ⚠️ **行为变更**：对分布式类型参数的条件类型检查更严格；`lib.d.ts` 与 DOM 类型更新可能影响现有代码。
- 🗓️ **后续计划**：接下来将聚焦速度、稳定性和反馈修复，预计约一个月后发布 Release Candidate，随后发布正式版。

---

### [GTA.js：用 JavaScript 和 WebGL 重新实现 1997 年《侠盗猎车手》引擎——Bram.us](https://www.bram.us/2026/10/22/gta-js/)

**原文标题**: [GTA.js, a reimplementation of the 1997 Grand Theft Auto engine in JavaScript and WebGL – Bram.us](https://www.bram.us/2026/10/22/gta-js/)

GTA.js 是作者 Bramus 用 JavaScript 和 WebGL 重新实现 1997 年《Grand Theft Auto》引擎的副项目，已发布且可玩，但尚未完全完成。

- 🎮 项目名为 GTA.js，项目地址为 https://gtajs.wtf/
- 🛠️ 这是对 1997 年 GTA 引擎的重新实现，并非 DOSBox 包装器、模拟器或反编译版本
- ⚠️ 由于是重写版本，部分物理行为和动画与原版存在差异；任务引擎较准确，依据公开文档 mtd.doc
- 🤖 作者让 Gemini 实现了大部分内容，并参考开源重实现、公开文档、社区笔记以及个人游玩和修改游戏的记忆
- 🏖️ 作者在机场准备度假时发布了现有成果，认为目前完成度已经相当高
- 🚧 项目仍有大量工作待完成，例如警察系统，但当前已经可以游玩

---

### [GTA.js —— 用 JavaScript 和 WebGL 重新实现 1997 年原版《侠盗猎车手》引擎](https://gtajs.wtf/)

**原文标题**: [GTA.js — A reimplementation of the original 1997 Grand Theft Auto engine in JavaScript and WebGL.](https://gtajs.wtf/)

GTA.js 是用 TypeScript 和 Three.js 重写的 1997 年《Grand Theft Auto》引擎，可直接解析原版 PC 共享版演示的未修改二进制与文本文件，并在浏览器中重现自由城；它不是 DOSBox 封装、模拟器或反编译产物，因属于重实现，物理、动画和部分系统与原版存在差异，目前范围限于 1997 年自由城演示关卡。

- 🧱 已实现 3D 城市与地图渲染：堆叠街区、40 种斜坡、动态水面、红绿灯和 24 位调色板重映射精灵。
- 🚗 已实现车辆与操控：每车独立操控参数、四角碰撞、方向性凹陷与车门变化、刹车痕和车辆爆炸。
- 🔫 已实现武器与箱子：拳头、手枪、机枪、火箭筒、火焰喷射器、护甲、额外生命和可破坏油桶。
- 🧩 已实现 MISSION.INI 引擎：多进程脚本解释器、响铃电话亭、目标引导箭头、计时器和 HUD 简报。
- 🚦 已实现 NPC 交通与行人：环境车辆、劫车、行人行走/惊慌/逃跑 AI，以及空间化 Web Audio 效果。
- 🏗️ 已实现码头吊车：可吊起、摆动并压碎车辆以获得现金奖励。
- 🎯 已实现 Kill Frenzy：隐藏限时狂暴挑战，提供无限弹药和分数倍率奖励。
- 🚫 未实现警察与通缉系统：巡警车、路障、通缉等级头像和被捕机制。
- 🚑 未实现紧急服务：救护车响应受伤行人、消防车扑灭燃烧车辆。
- 🎨 未实现喷漆店与炸弹店：驶入式喷漆和给车辆安装定时炸弹。
- 🚆 未实现火车与有轨电车：高架/地铁列车及沿铁路街区的有轨电车。
- 🕉️ 未实现 Gouranga!：碾过 Hare Krishna 队列获得经典奖励。
- 🔊 未实现多种音频：车辆鸣笛、行人喊叫、警笛和电台。
- 🎮 未实现完整战役与多人模式：仅覆盖 1997 年自由城演示关卡，无圣安地列斯、罪恶都市或网络玩法。
- ⌨️ 游戏内按 ? 或 Esc 打开完整控制/选项/测试覆盖，按 H 切换调试 HUD；方向键移动/转向，Shift 奔跑，Enter 上下车，Ctrl 或 Alt 开火，Space 跳跃/滑行/手刹，1–5 或 Z/X 选武器。
- 📚 项目参考 DMA Design 官方技术规格、GTA 社区文档/工具及 gta-webgl、carnage3d、OpenGTA、gta1-webedition 等重实现成果。

---

### [Cloudflare 发布公告后 Deno 的现状 · Issue #37030 · denoland/deno · GitHub](https://github.com/denoland/deno/issues/37030#issuecomment-6310897867)

**原文标题**: [The state of Deno after the Cloudflare announcement · Issue #37030 · denoland/deno · GitHub](https://github.com/denoland/deno/issues/37030#issuecomment-6310897867)

Deno 公司加入 Cloudflare 后，Deno 运行时进入以维护为主的阶段：官方承诺至少维护到 2027 年 10 月，继续发布月度版本、2.9.x LTS、安全更新和 canary 构建，但不再开发新功能；社区高度关注项目治理、基金会接管、JSR、@std/*、deno desktop 以及 Node.js 兼容性的未来。

- 🏢 Deno 公司加入 Cloudflare；官方称将持续维护 Deno 至 2027 年 10 月。
- 📦 每月发布 2.9.x LTS，包含 bug 修复和安全更新；安全漏洞报告流程保持不变。
- 🧪 Canary 构建继续从 main 自动发布，新修复会先进入 canary。
- ✅ 欢迎并合并质量较好的 bug 修复 PR；不计划开发新功能，功能类 PR 会被关闭。
- 📝 功能请求 issue 不会被关闭，而是打标签保留。
- ↩️ 2.9 分支之后进入 main 的 canary 专属功能会被回滚，使 main 与 2.9 一致；例如 `deno sync-types` 和移除内部 TypeScript fork，完整列表待公布。
- 🪪 Deno 为 MIT 开源许可，任何人可 fork；官方正在考虑 2027 年 10 月后的开发组织方式，可联系 @bartlomieju。
- 🧱 JSR 将继续运营，其基础设施迁移到 Cloudflare。
- 🏛️ 维护者表示正在推动 Deno 进入基金会，但暂无具体消息；社区已有人协调 fork，但多数更希望由可靠的非营利/现有基金会（如 OpenJS）接管。
- 💬 社区关注 @std/*、deno desktop 等未来维护；对是否保留 Node.js 兼容性存在争论：一方希望逐步移除，另一方认为兼容性是迁移、安全和采用的关键。
- 🔐 有用户强调 Deno 的权限白名单适合运行 AI 生成代码，Rust 实现也避免了部分 Node 漏洞。

---

### [结束](https://ende.sh/)

**原文标题**: [Ende](https://ende.sh/)

内容以“Deno 已死，Ende 将至”为宣传口号，预告一个面向 Deno 用户的替代项目；Ende 并非 Deno 的直接替代品，而是强调专注、精简，并保留 TypeScript 与安全特性的有主见方案，更多信息“敬请期待”。

- ⚠️ 口号宣称“Deno 已死，Ende 将至”，并提示持续关注。
- 🚫 明确 Ende 不是 Deno 的即插即用替代品；需要这种兼容性的用户不适合使用。
- 🎯 Ende 定位为 Deno 的有主见、专注型替代方案。
- ✨ 保留优秀的 TypeScript 与安全特性，同时去除臃肿。
- 📚 页面提供公告、文档、GitHub、Mastodon、Bluesky 等入口。

---

### [Safari 27.1 的 WebKit 功能 | WebKit](https://webkit.org/blog/18486/webkit-features-for-safari-27-1/)

**原文标题**: [  WebKit Features for Safari 27.1 | WebKit](https://webkit.org/blog/18486/webkit-features-for-safari-27-1/)

Safari 27.1 随 iPhone Duo 发布，核心信息是“没有大新闻”：它沿用与其他 iPhone 相同的 WebKit 引擎和 Web 技术，网站与 Web 应用无需特殊适配即可运行；同时带来 PDF 双页显示、折叠屏相关开发者预览 API，并继续倡导响应式设计与特性检测。

- 😌 最大新闻是没有新闻：Safari 27.1 使用与其他 iPhone 相同的 WebKit 引擎和 Web 技术，网站和 Web 应用在 iPhone Duo 上照常工作。
- 📄 唯一面向用户的变化：当 iPhone Duo 像书一样半折叠并查看网页 PDF 时，Safari 27.1 自动并排显示两页；展开或合上后恢复单页。
- 🧪 开发者可在功能标志后预览 Device Posture API 与 Viewport Segments API，开启路径为“设置 > App > Safari > 高级 > 功能标志”。
- 📐 Safari 27.1 在 iPhone Duo 上的视口宽度约为 382–951 CSS 像素，高度约为 368–902；外屏、内屏、横竖屏和分屏组合会产生不同尺寸。
- 🧩 建议使用媒体查询、CSS Grid、Flexbox 等现代响应式技术，避免 UA 嗅探，改用特性检测；可用 Xcode 27.1 的 Device Hub 模拟器测试。
- 📱 Device Posture API 通过 `device-posture` 媒体查询和 `navigator.devicePosture` 报告 `folded`（半折叠书本/笔记本姿态）与 `continuous`（平整，含全开或全合）。
- 🪟 Viewport Segments API 使用 `horizontal-viewport-segments` 和 `vertical-viewport-segments` 媒体查询识别并排或上下堆叠分段，并提供六个 `viewport-segment-*` 环境变量；JavaScript 可用 `window.viewport.segments` 获取 `DOMRect` 数组。
- 🔲 外屏更宽更矮，iOS 将控件移到侧边；目前 Web 内容不会延伸到控件后方，Safari 用页面背景色填充，团队正研究比 `viewport-fit=cover` 更稳妥的方案并征集想法。
- 💬 可通过 Bluesky/Mastodon 联系 Jen Simmons，或提交 Safari UI Feedback、WebKit bug report 反馈问题与建议。

---

### [Chrome 156 发布说明 - Chrome 平台状态](https://chromestatus.com/release-notes/156)

**原文标题**: [Chrome 156 Release Notes - Chrome Platform Status](https://chromestatus.com/release-notes/156)

本文汇总 Chrome 157 在网络连接、CSS、存储、图形、实时通信及弃用移除方面的更新，重点包括可重试的模块加载、WebTransport 自定义请求头、CSS 随机函数与滚动控制、IndexedDB SQLite 后端、WebGPU 优化、WebRTC 诊断日志，以及分阶段移除 FencedFrame 与 window.fence API。

- 🌐 避免缓存模块加载失败：失败模块不再被永久缓存，开发者可通过再次调用 `import()` 手动重试，改善不稳定网络下的模块使用体验。
- 📦 压缩字典传输更新：获取 `rel=compression-dictionary` 链接时使用 `compression-dictionary` 作为请求目标，并正确设置 mode、credentials、referrer、referrerpolicy，同时考虑 `crossorigin` 与 `referrer` 属性。
- 🔗 WebTransport 请求与响应头：支持通过 `WebTransportOptions` 传递自定义 HTTP 请求头，并可检查服务器响应头，用于认证令牌、元数据和自定义参数。
- 🎯 CSS 导航来源伪类：可选择发起导航的元素（链接、按钮或表单），并在整个导航过程中保持选中状态。
- 🎲 CSS `random()` 函数：为 CSS 引入生成式随机能力，可在指定范围内生成随机数值，并支持通过 `<random-key>` 控制随机值在不同属性和元素间的共享与缓存。
- 📜 单轴滚动容器：扩展 `overflow` 以支持 `scroll` 与 `clip` 组合值，使 `position: sticky` 可按轴受不同祖先滚动容器约束。
- 🧲 `scroll-snap-type: pair`：新增 `pair` 关键字，使容器在一个轴上吸附到某元素时，另一轴也吸附到同一元素，而非独立选择目标。
- 🗄️ IndexedDB SQLite 后端：将 IndexedDB 实现重写为基于 SQLite，Web API 不变，旨在提升可靠性和一定性能；当前适用于新数据存储，现有 LevelDB 数据不受影响，后续将迁移旧数据。
- 🎮 WebGPU WGSL 片段深度：为 `@builtin(frag_depth)` 增加 `less` 或 `greater` 修饰符，可显式设置缓冲区模式并启用 early-Z 优化。
- 📞 WebRTC 诊断日志 API：授权 Web 应用可触发收集 WebRTC 诊断数据用于本地调试，并可在用户授权下与浏览器厂商共享，以帮助修复问题；管理员可通过企业策略启用。
- 🚫 移除 FencedFrame 与 `window.fence` API：由于 Protected Audience 和 selectURL 已在 M152 弃用移除，Fenced Frames 无法再导航；计划在 M156 将元素与相关 IDL、`window.fence` API 存根化，M157 Canary/Beta 通过实验逐步移除元素，M157 Stable 在无回归后全面移除。

---

### [Node.js — Node.js 26.12.1（当前版本）](https://nodejs.org/en/blog/release/v26.12.1)

**原文标题**: [Node.js — Node.js 26.12.1 (Current)](https://nodejs.org/en/blog/release/v26.12.1)

本次发布为 Node.js 26.12.1（Current）安全版本，发布于 2026-10-21，由 @aduh95 准备、@RafaelGSS 协助，主要包含多项高、中、低危安全修复及依赖更新。

- 🔒 **高危及关键修复**：修复 TLS 拒绝非规范 IP 地址（CVE-2026-106069、CVE-2026-106072）、DNS 解析输入空字节校验（CVE-2026-105482）、TLS IP 规范化回归（CVE-2026-105483）以及 Brotli 相关补丁（CVE-2026-111497）。
- 🛡️ **中危修复**：确保 HTTP agent 数据保护机制在无 I/O 时仍生效（CVE-2026-105481），并在快照间重置 crypto 随机缓存（CVE-2026-106074）。
- 🧩 **低危修复**：避免 zlib 缓存无效 ZIP 本地头（CVE-2026-106070），并在 `realpathSync` 中检查权限模型（CVE-2026-106073）。
- 🔐 **证书与加密加固**：更新根证书至 NSS 3.131.1，强化 X.509 转换与格式化，并拒绝包含被阻止公钥的 TLS 证书链。
- ⚙️ **依赖与底层更新**：V8 回移植补丁、c-ares 更新至 1.34.9、undici 更新至 8.12.2，并包含 Brotli 解码错误暴露等源码调整。
- 🧰 **工具与发布流程**：在公证后重试 Gatekeeper 检查和 stapling，提升 macOS 发布产物可靠性。
- 💻 **多平台产物**：提供 Windows x64/ARM64 安装包与二进制、macOS Intel/Apple Silicon、Linux x64/ARM64/PPC LE/s390x、AIX 及源码包。
- 📦 **校验与文档**：发布文件附带 SHASUMS 与 PGP 签名，文档地址为 `https://nodejs.org/docs/v26.12.1/api/`。
- ⏭️ **后续版本**：页面标注下一版本为 Node.js 24.22.1（LTS）。

---

### [Node.js — Node.js 24.22.1（长期支持版）](https://nodejs.org/en/blog/release/v24.22.1)

**原文标题**: [Node.js — Node.js 24.22.1 (LTS)](https://nodejs.org/en/blog/release/v24.22.1)

Node.js 24.22.1（LTS，代号 Krypton）于 2026-10-21 发布，是一次安全更新，修复多项高、中、低危漏洞，并同步升级加密根证书、OpenSSL、c-ares、时区数据和 undici 等依赖；同时提供各平台安装包、二进制、源码及 SHA256 校验信息。

- 🔐 高危修复：TLS 拒绝非规范 IP 地址（CVE-2026-106069、CVE-2026-106072）
- 🌐 高危修复：DNS 对 resolve 输入进行空字节校验（CVE-2026-105482）
- 🧩 高危修复：修复 TLS IP 规范化回归问题（CVE-2026-105483）
- 🧱 高危修复：Brotli 合并安全补丁（CVE-2026-111497）
- 🛡️ 中危修复：HTTP agent 数据保护在无 I/O 时仍生效（CVE-2026-105481）
- 🎲 中危修复：跨快照重置加密随机缓存（CVE-2026-106074）
- 🔒 低危修复：在 realpathSync 中检查权限模型（CVE-2026-106073）
- 📜 其他安全加固：TLS 拒绝含被阻止公钥的证书链，强化 X.509 转换与格式化，并回移植 V8 补丁
- 📦 依赖更新：根证书至 NSS 3.131.1、c-ares 1.34.9、时区数据 2026e、OpenSSL 3.5.9、undici 7.30.1
- 💻 发布物覆盖 Windows、macOS、Linux、AIX、ARMv8 等平台，包含安装包、二进制、源码、文档与 SHASUMS 校验信息

---

### [Node.js — Node.js 22.23.4 (LTS)](https://nodejs.org/en/blog/release/v22.23.4)

**原文标题**: [Node.js — Node.js 22.23.4 (LTS)](https://nodejs.org/en/blog/release/v22.23.4)

Node.js 22.23.4（LTS，代号 Jod）于 2026-10-21 发布，是一次安全版本更新，修复多个高、中、低危漏洞，并同步更新根证书与多项依赖，提供多平台安装包、二进制和源码下载。

- 🔐 版本定位：Node.js 22.23.4 为 LTS 安全发布，建议关注并升级至该版本。
- 🚨 高危修复：TLS 拒绝非规范 IP 地址（CVE-2026-106069、CVE-2026-106072）；DNS 校验 resolve 输入中的空字节（CVE-2026-105482）；Brotli 依赖补丁（CVE-2026-111497）。
- ⚠️ 中危修复：HTTP agent 数据保护在无 I/O 时仍生效（CVE-2026-105481）；crypto 跨快照重置随机缓存（CVE-2026-106074）。
- 🛡️ 低危修复：permission 模块在 realpathSync 中检查权限模型（CVE-2026-106073）。
- 🔎 其他安全相关提交：TLS 拒绝包含被阻止公钥的证书链；TLS 将 IPv6 主机与 IP-Address SAN 匹配；加固 X.509 转换与格式化。
- 📦 依赖更新：c-ares 1.34.9、时区 2026e、OpenSSL 3.5.9、SQLite 3.53.4、undici 6.29.1。
- 📜 证书更新：根证书更新至 NSS 3.131.1。
- 💻 发布产物：提供 Windows（x86/x64/ARM64）、macOS（Intel/Apple Silicon）、Linux（x64/ARMv7/ARM64/PPC64LE/s390x）、AIX 及源码等下载。
- ✅ 完整性校验：发布页包含 SHASUMS 与 PGP 签名，文档链接指向 v22.23.4 API。

---

### [Node2Shell（CVE-2026-111497），又名 HTTP2Shell 和 Broccoli2Shell：RCE 分析 | ELLIO 博客](https://ellio.tech/en/blog/node2shell-cve-2026-111497-rce-on-stock-nodejs-builds/)

**原文标题**: [Node2Shell (CVE-2026-111497) aka HTTP2Shell and Broccoli2Shell: RCE analysis | ELLIO Blog](https://ellio.tech/en/blog/node2shell-cve-2026-111497-rce-on-stock-nodejs-builds/)

overview summary
- 🚨 CVE-2026-111497（Node2Shell/HTTP2Shell/Broccoli2Shell）是 Google Brotli 解码器越界写漏洞，CVSS 4.0 评分 9.2 Critical；恶意 Brotli 请求体可在官方未修改 Node.js 上触发远程代码执行。
- 🧠 根因是块切换辅助函数用布尔值混淆“无效块切换”和“需要更多输入”，导致内部 8 字节缓冲区未清空并发生越界写；对应 CWE-252 与 CWE-787，修复提交 0ed4268a 改为返回错误码 -17。
- 🎯 ELLIO 在 x86-64 复现：原生 node:http、官方 node:24.22.0-slim（root）、Express 5.3.0、Koa 3 均获 shell，且以服务自身账户运行；补丁版本以 400/ERR_FORMAT_BLOCK_SWITCH 拒绝。
- 🧩 攻击面包括入站 Content-Encoding: br（Express body-parser、Koa bodyparser 等）、出站 br 响应自动解压（undici/fetch、axios、got、Next.js 等）以及直接调用 node:zlib Brotli。
- ⚠️ 影响 Node.js 22/24/26，EOL 的 20/23/25 不修复；还涉及 Bun <1.4.4、Python Brotli/brotlicffi、urllib3/requests/httpx/aiohttp/Scrapy、Envoy、PHP/Ruby 等生态。
- 🛠️ 修复版本：Node.js 22.23.4、24.22.1、26.12.1；Google Brotli 1.0.10/1.1.1/1.2.1；Bun 1.4.4；PyPI Brotli 1.2.1、brotlicffi 1.2.1.0；Envoy 多个版本。注意 process.versions.brotli 不可靠，应查发布版本。
- 🔍 已出现野外活动：node2shell-check 扫描主机是否解压 Brotli，随后不同来源发送公开利用流量；ELLIO 提醒按“已遭利用”处置并立即打补丁。
- 💥 失败利用会造成拒绝服务：多数 Express 尝试崩溃 worker；若启用 core dump，崩溃转储可能泄露会话 Cookie、Bearer Token、RSA 密钥等敏感内存数据。
- 🌀 部分解码器（Python Brotli/brotlicffi、PHP 流式 API、Ruby gem）遇到同样字节会返回 0 字节、永不结束或 100% CPU，形成静默 DoS。
- 🧱 临时缓解：无法立即全量修复时，尽量丢弃入站 Content-Encoding: br；升级 Node.js 只覆盖其内置副本，还需更新系统 libbrotli、DuckDB、.NET、PHP 扩展、bun --compile 产物及镜像/锁文件/CI/无服务器运行时。
- 📡 10 月 26 日更新：传感器观察到 23,069,983 字节的定向利用请求，目标为 Node.js v24.22.0 x86-64；投递层与公开 PoC 一致，ROP 链为原创但测试 50 次零命中，显示攻击者可能仍在迭代。
- 🧾 其他要点：官方 Node 构建为非 PIE，ASLR 不保护代码/库地址；重启循环给攻击者反复尝试机会；每个 Node 构建需独立偏移，版本指纹使大规模定向攻击更经济。

---

### [Bun v1.4.4 | Bun 博客](https://bun.com/blog/bun-v1.4.4)

**原文标题**: [Bun v1.4.4 | Bun Blog](https://bun.com/blog/bun-v1.4.4)

Bun v1.4.4 于 2026 年 10 月 22 日发布，核心亮点包括内置格式化器 `bun fmt`、`bun check` 与 `bun install` 的大幅性能和兼容性提升，并强化 `Bun.SQL`、SQLite、WebSocket/ws、运行时、开发服务器及安全性，同时修复大量 Node.js 兼容性问题。

- 🚀 发布版本为 Bun v1.4.4，可通过 `bun upgrade` 升级，并提供 curl、npm、PowerShell、Scoop、Homebrew、Docker 等安装方式。
- 🧰 新增内置格式化器 `bun fmt`，兼容 Prettier 和 oxfmt 配置，支持 JS、TS、JSX、CSS、HTML、Vue、Svelte、Markdown、GraphQL 等大量语言及嵌入式代码。
- ⚡ `bun fmt` 在 Prettier 仓库中约 60ms 完成检查，而 Prettier 约 17 秒，官方称快 286 倍；对比 oxfmt 也快 3 到 6 倍，部分项目更高。
- 🧩 `bun fmt` 支持 `.prettierrc*`、`prettier.config.*`、`.editorconfig`、`.prettierignore`、`.oxfmtrc.json` 等配置，并支持 `--check`、`--staged`、`--changed`、`--doctor`、`--init`。
- 🎯 内置 Tailwind CSS、`package.json` 和 Svelte 插件能力；官方测试中与 Prettier 输出约 99.1% 字节级一致，并有意修复部分会改变代码语义的格式化行为。
- ✅ `bun check` 在大项目上快 1.4 到 7.8 倍；使用 `bun check -b` 时，多项目场景最高约快 15.7 倍，并显著降低内存占用。
- 📦 `bun install` 现在可迁移 Yarn Berry 的 `yarn.lock` 到 `bun.lock`，保留固定版本、workspace、alias、resolutions、git、tarball、`file:`、`patch:` 和 catalog 等信息。
- 🔁 安装请求支持最多 5 次指数退避重试，等待时间约为 50、100、200、400、800ms，并支持 `Retry-After`、429 和 408 响应。
- 🧠 该版本关闭了 133 个 `bun install` 相关问题；hoisted 安装在 Linux 热缓存场景最高快 3.2 倍，并会跳过不匹配当前 libc 的 Linux 原生包。
- 🔗 Peer dependency 解析更接近 pnpm：优先使用项目或祖先依赖版本，否则选择满足所有依赖的共享版本，减少重复副本和错误 peer 警告。
- 🗂️ 新增 `bun pm fetch`、`bun pm cache pack/unpack/prune`、`bun publish --recursive`、`--filter`、`packageExtensions`、`link:` 路径依赖、弃用包警告、`minimumReleaseAge` 单位与排除项等。
- 🧪 包管理器命令支持 `--env-file`、`bunx --cwd`、`bunx --trust`、`--minimum-release-age`，并能翻译 npm、Yarn、pnpm 常用参数，未知参数会报错。
- 🗄️ `Bun.SQL` 重构后单次查询 CPU 使用最多降低 48%，`await sql\`select 1\`` 的 GC 对象显著减少；新增查询取消、PostgreSQL COPY 流、列名转换、PostgreSQL 数组、`sql.json()` 等能力。
- 🔥 `bun --hot` 现在会复用数据库连接，避免热重载不断创建新连接；`Bun.SQL` 还新增 channel binding、TLS 校验、连接超时、MySQL `foundRows` 等连接选项。
- 🧬 `bun:sqlite` 新增用户自定义函数、聚合函数、插入/更新/删除钩子，以及 `stmt.reader`、`stmt.readonly` 等能力。
- 🔌 `ws` 在 Bun 中重写为基于原生 WebSocket 的 `ws` 8.22.0 兼容实现；其测试通过数从 94/271 提升到 234/271，客户端和服务器脚本兼容性明显增强。
- 🛑 WebSocket 关闭语义更接近浏览器和 Node.js：会等待关闭握手，失败连接先触发 `error` 再以 1006 触发 `close`，并支持 `ws.pause()`、`ws.resume()`、`websocket.error(error, ws)` 和 `proxy.tls`。
- 🌐 运行时升级 JavaScriptCore，包含 1,013 个 WebKit 上游提交；`toLocaleString` 在基准中快 54 倍，数组字面量、字符串遍历、异常处理等也有明显提速。
- 🧭 `Bun.Glob` 支持 extglob 和 brace ranges，例如 `!(*.test).ts`、`@(app|lib)`、`{1..3}`，并可用于 `--filter`、workspaces、`files`、`sideEffects` 等场景。
- 🚦 `Headers` 迭代速度提升 1.7 到 2.8 倍，内存中的 `response.body` 流读取速度提升 1.5 到 2.6 倍，并显著减少小响应体的内存分配。
- 🖥️ 开发服务器错误覆盖层重新设计，支持同类错误分组、滚动查看、浅色主题，并避免重复展示构建错误。
- 🔐 本次更新包含 TLS、WebSocket、数据库客户端和包管理器相关安全修复，并带来大量 Node.js 兼容性、Bun API、Web API、TLS、WebSocket、运行时、`bun test`、Shell、SQL 和 TypeScript 类型修复。
- 🙏 官方感谢 39 位贡献者参与该版本开发。

---

### [Electron 45 | Electron](https://www.electronjs.org/blog/electron-45-0)

**原文标题**: [Electron 45 | Electron](https://www.electronjs.org/blog/electron-45-0)

Electron 45 已于 2026 年 10 月 21 日发布，核心升级为 Chromium 156.0.8078.48、V8 15.6 和 Node v24.22.0；该版本重点优化启动、菜单和原生 API 性能，并新增本地 AI Prompt API、macOS 系统通行密钥、Windows 更广崩溃报告、ASAR 直读及 Perfetto 原生堆分析，同时包含多项破坏性变更。

- 🚀 性能提升：减少沙盒渲染器启动开销，macOS 冷启动预取框架文件，菜单构建和窗口、视图、WebContents 的原生调用更快。
- 🧩 破坏性变更：沙盒预加载脚本不再内置 Buffer、setImmediate、clearImmediate 及 events、timers、url 模块 shim，需改用 Web API 或自行打包 polyfill。
- 🖥️ 屏幕共享权限：屏幕、窗口、标签页捕获请求改为 display-capture 权限；仅允许 media 的权限处理器需同时允许 display-capture。
- 🤖 实验性本地 AI：支持 session.registerLocalAIHandler()、localAIHandler 和 LanguageModelUtility，由应用在 utility process 中提供模型实现。
- 🔐 macOS 通行密钥：app.configureWebAuthn() 支持 platformPasskeys，可调用 iCloud Keychain、1Password 等系统通行密钥，并新增 select-webauthn-authenticator 事件。
- 🧯 Windows 崩溃报告：新增 WER helper，可捕获 __fastfail 等绕过进程内处理器的崩溃；需将 electron_wer.dll 与可执行文件同名打包。
- 📦 ASAR 直读：fs.open()、createReadStream()、copyFile()、cp() 等直接从 ASAR 读取文件，大文件冷读最高快 100 倍且不再产生临时文件。
- 🌐 网络与下载归因：webRequest、protocol、DownloadItem、will-download、preconnect 等可识别发起请求的 frame / initiatorOrigin，便于按 frame 制定权限与网络策略。
- 📊 原生堆分析：contentTracing 支持 Perfetto nativeHeapProfiling，用于采样 C/C++ 原生内存分配；录制格式改为 Perfetto protobuf。
- 🧱 其他新功能：macOS app shims、Linux 通知操作按钮、protocol.registerSource()、disableWakeLocks、webFrame.getIsolatedWorlds() 等。
- ⚠️ 其他行为变更：iframe Worker 需 nodeIntegrationInSubFrames；扩展预加载遵循嵌入 frame；WebContents 捕获改用 chromeMediaSource: 'tab'；window.open() 沙箱子窗口默认独立进程。
- 🗂️ ASAR 文件描述符限制：fs.open() 返回的 ASAR 文件描述符仅适用于 Node fs，不支持原生插件、child_process stdio 或 net.Socket({ fd })；写入类操作失败。
- 🧹 弃用与移除：同步 safeStorage 方法弃用，Electron 46 移除；contentTracing.enableHeapProfiling() 移除；document.requestStorageAccessFor 默认禁用。
- 🛑 支持终止：Electron 42.x.y 已结束支持，建议升级到受支持版本。

---

### [Prompt API | Chrome 中的 AI | 面向开发者的 Chrome](https://developer.chrome.com/docs/ai/prompt-api)

**原文标题**: [The Prompt API  |  AI in Chrome  |  Chrome for Developers](https://developer.chrome.com/docs/ai/prompt-api)

Chrome 内置的 Prompt API 允许开发者用自然语言向浏览器内的 Gemini Nano 基础模型发送请求，从而在网页和 Chrome 扩展中构建本地运行的 AI 功能，如智能搜索、内容分类与过滤、日历事件提取等；该 API 分阶段推出，对硬件、系统和存储有明确要求，并提供会话管理、多模态输入、结构化输出等完整能力。

- 🧠 **核心功能**：Prompt API 让开发者向 Chrome 内置的 Gemini Nano 模型发送自然语言提示，可用于 AI 搜索、个性化新闻流、内容过滤、日历事件创建、联系人信息提取等场景。
- ⚠️ **AI 伦理提示**：内置模型属于生成式 AI，开发前应查阅 People + AI Guidebook 以了解设计最佳实践。
- 💻 **硬件要求**：需 Windows 10/11、macOS 13+、Linux 或 Chromebook Plus 版 ChromeOS；至少 22 GB 可用存储空间；GPU 需超过 4 GB 显存，或 CPU 需 16 GB 内存加 4 核以上。
- 🌐 **网络与隐私**：仅首次下载模型需要无限量或不计量网络，后续使用可离线；数据不会发送给 Google 或第三方；存储低于 10 GB 时模型会被移除。
- 🔍 **可用性检查**：通过 `LanguageModel.availability()` 判断模型是否就绪，且必须传入与 `prompt()` 相同的选项；再用 `create()` 创建会话并监听下载进度。
- 🎛️ **采样参数**：网页端使用 `samplingMode` 枚举值（从 `most-predictable` 到 `most-creative`）调节输出的确定性与创造性；Chrome 扩展仍支持 `topK`、`temperature` 及 `LanguageModel.params()`。
- 💬 **上下文与约束**：支持用 `initialPrompts` 注入历史上下文，也支持给末尾 assistant 消息加 `prefix: true` 来预填回复格式；`append()` 可在会话中追加带上下文的提示。
- 🖼️ **多模态支持**：`expectedInputs` 可接受文本、图像、音频（音频输入需 GPU），输出仅限文本；支持语言目前包括 en、ja、es、de、fr，不支持时抛出 `NotSupportedError`。
- 📤 **输出方式**：`prompt()` 一次性返回短结果，`promptStreaming()` 返回 `ReadableStream` 流式输出长结果；两者均可用 `AbortSignal` 中止。
- 🧩 **结构化输出**：通过 `responseConstraint` 传入 JSON Schema 或正则表达式约束回复格式，可用 `omitResponseConstraintInput` 节省上下文窗口。
- 🗂️ **会话管理**：会话会自动累积上下文，可用 `contextUsage`/`contextWindow` 查看用量；溢出时触发 `contextoverflow` 事件并逐对删除早期对话（系统提示永不删除），无法腾出空间时抛出 `QuotaExceededError`。
- ♻️ **克隆与销毁**：`clone()` 可低成本复制会话分支，`destroy()` 释放资源并中止进行中的任务。
- 🔐 **权限与范围**：默认仅限顶层窗口及同源 iframe，可通过 `allow="language-model"` 委托给跨源 iframe；目前不支持 Web Worker。
- 🧪 **示例与反馈**：官方提供 Prompt API playground、音频与图像输入演示及扩展示例；开发者可通过 Bug 报告、GitHub Issue 和早期预览计划参与共建。

---

### [pnpm 12.16.0 | pnpm](https://pnpm.io/blog/releases/12.16.0)

**原文标题**: [pnpm 12.16.0 | pnpm](https://pnpm.io/blog/releases/12.16.0)

pnpm 12.16.0 是一次覆盖新功能、安全修复、安装与锁文件行为、命令体验、存储及性能优化的大型版本；核心亮点包括全局 `--env-file`、支持更新符号链接形式的 `pnpm-lock.yaml`、`pnpm setup --no-modify-path`，以及 zstd 解压和签名相关安全修复。

- 🆕 新增可重复使用的全局 `--env-file <path>`：运行命令前加载 dotenv 文件，后加载文件覆盖先前文件，已有环境变量保留，且对用户级 `.npmrc` 插值和生命周期脚本可见。
- 🔗 支持更新作为符号链接的 `pnpm-lock.yaml`：通过 `symlinkedLockfileTargetDirs` 或 `PNPM_CONFIG_SYMLINKED_LOCKFILE_TARGET_DIRS` 指定可写入目标目录，符号链接保持不变；该设置在工作区 YAML 中会被忽略。
- 🛠️ `pnpm setup` 新增 `--no-modify-path`：不修改 PATH、shell 配置、Windows 注册表和 GitHub Actions 环境文件，并打印需手动添加的行。
- 🔒 修复两处安全问题：zstd 压缩数据处理中的内存暴露与分配漏洞，以及签名中可能通过计时泄露私钥的算术问题，涉及共享产物、OCI registry token 和 OIDC 登录状态。
- 🧷 安装可靠性改进：依赖符号链接无法指向目标时明确报错并命名链接，避免无限删除和段错误；并发工作区安装不再丢失 SQLite store-index 行；包含被拒绝路径的包归档会立即失败。
- 🧱 安装行为修复：git 托管依赖会在每个新链接位置构建或从副作用缓存恢复；`preResolution` 钩子对锁文件的修改会生效；pnpmfile 自定义 fetcher 可使用 `fetchers.directory`；`packageImportMethod: copy` 也适用于含生命周期脚本或补丁的包。
- 🧩 hoisted 模式改进：`autoInstallPeers: false` 下按 peer 变体安装；已就位的补丁包不再被重复处理；安装中断后下一次安装不会误信半替换的包。
- ⚙️ 重复安装与设置变更更可靠：`storeDir`、`virtualStoreDir`、`globalVirtualStoreDir`、`virtualStoreDirMaxLength`、`dangerouslyAllowAllBuilds`、`trustLockfile` 的变化会被识别；`add/remove/update` 在 `node_modules` 与设置不匹配时报错而非静默重装。
- 🧭 工作区与 `bin` 修复：过滤安装遇到 `nodeLinker`、hoist、store 等不匹配会失败；工作区包 `bin` 字段变化会重新链接或移除旧 shim；`verifyDepsBeforeRun` 能发现补丁文件编辑。
- 📦 锁文件解析改进：同一 registry 的普通范围与带前缀说明符只记录和安装一次；scope 路由到新 registry 会重新解析；`autoDedupe: false` 下项目按自身范围解析；相对路径 `workspace:` 注入、catalog 依赖等得到修复。
- ➕ `pnpm add` 改进：`pkg@tag` 或 `pkg@range` 安装解析到的版本；无版本时按 `tag` 设置解析，默认 `latest`；支持 `-p/-d/-o/-e` 短选项；`pnpm -D install <pkg>` 正确写入 devDependencies。
- 🌐 全局包与冲突检查：`pnpm add -g` 从全局虚拟存储链接，共享依赖只存一份；`--global` 与 `--virtual-store-dir`、`--hoist-pattern`、`--link-workspace-packages` 等冲突时明确报错。
- 🔐 Registry、代理与登录：`strictSsl`、`localAddress` 从工作区 YAML、全局配置、环境变量和 `--config.*` 读取；Corepack 下载原生二进制时使用 pnpm 代理配置并信任 `.npmrc` CA；`pnpm login` 恢复写入 `auth.ini` 并清理旧 `_auth`。
- 🧪 命令与脚本：`pnpm ci` 始终保留锁文件并执行 frozen 安装；`deploy --legacy` 检查 `minimumReleaseAge` 等策略；`pack/publish` 保留并包含 `pnpm.config`；`audit --ignore` 仍有漏洞时非零退出，`audit --fix` 与 ignore 组合会报错。
- 🖥️ 运行体验：`-r run` 遵循 `requiredScripts`；macOS 终止 pnpm 会结束所有并行脚本；`run/exec/dlx` 不再因被信号终止而生成 core 文件；新增 `runtime` 设置；`help --all` 正常输出全部命令。
- 🗄️ Store 修复：`pnpm store prune` 保留项目仍在使用的复制或克隆包、补丁包、构建包及符号链接路径项目；并清理 `metadata*` 缓存以解决 registry 重新发布导致的完整性错误。
- 🚀 性能优化：大型工作区依赖解析更快；macOS 冷安装和 `fetch` 使用单独线程链接下载包；peer 较多的锁文件新增项目更快；warm install 不读取每个 git 依赖的 `package.json`；大 `--depth` 的 `update` 接近 `Infinity` 速度。
- ⚠️ 输出与警告：填满终端的输出只写一次；警告 pnpmfile 的 `importPackage` 钩子不会执行；警告并在 `pnpm config set` 中拒绝把 `ci`、`globalShims`、`tools` 写入项目 `pnpm-workspace.yaml`；不再文档化无效的 `scriptsPrependNodePath`。

---

### [发布 remix v3.1.0 · remix-run/remix · GitHub](https://github.com/remix-run/remix/releases/tag/remix%403.1.0)

**原文标题**: [Release remix v3.1.0 · remix-run/remix · GitHub](https://github.com/remix-run/remix/releases/tag/remix%403.1.0)

Remix 3.1.0 已发布，重点带来服务端渲染性能提升、Frame 预取与导航控制增强、S3 流式分片上传，以及面向未来的流式表单/多部分上传 API；同时包含若干修复和依赖升级。

- 🚀 Remix 3.1.0 发布，涵盖性能优化、Frame 导航/预取增强、流式上传与新未来 API。
- ⚙️ `remix/component` 新增 `createMixin(setup, { ssr: false })`，可在服务端跳过 setup/render，同时保留浏览器行为和水合；默认仍启用 SSR。
- ⚡ SSR 约快 2 倍且更省内存：48 商品列表页 `renderToString()` 为 244µs（原 513µs）；持续 HTTP 负载下常驻内存从 793MiB 降至 527MiB。
- 🧠 `remix/assets` 的 `getScriptEntry()` 缓存使热查询约 3µs（原 210µs）。
- 🔄 `frame.reload({ src, method, encType, body })` 可重载其他源或提交数据并渲染响应，不改变浏览器历史；`FormData` 遵循 GET/POST 编码默认，支持 multipart/plain-text。
- 📦 支持 `data-rmx-prefetch="intent|viewport"` 和命令式 `prefetch()` 预取 Frame HTML/资源，支持命名 Frame、源覆盖，尊重 Save-Data，并跳过 slow-2g/2g。
- 🎯 可通过 `resetFocus: 'manual'` 或 `data-rmx-reset-focus="manual"` 关闭拦截导航自动焦点重置；滚动/焦点控制接受 Navigation API 的 `"after-transition"`（默认）和 `"manual"`，兼容布尔值。
- ☁️ `remix/file-storage/s3` 的 `storage.set()` 改为分片上传流式写入 S3，新增 `partSize`，大文件无需全量载入内存。
- 🌊 新增 `/future` 入口（multipart-parser、form-data-parser、middleware/form-data）以流式解析上传；100MiB 上传解析 37ms（原 68ms），上传处理器调用 0.2ms（原 45ms），峰值内存增加 29MiB（原 396MiB），小表单性能不变；官方征集反馈。
- 🔧 `remix/*` 入口保留底层包默认导出（如 `remix/assert` 的可调用断言助手、`remix/headers` 的 `SuperHeaders`），并新增 future 相关 `package.json` exports。
- 🩹 修复 HMR 后客户端入口使用最新 cache-busting URL；在 raw HTML prop 错误中加入 `unsafeHTML()` 指引并说明 host 元素不支持 `outerHTML`；升级多个 `@remix-run/*` 依赖。

---

### [发布 v1.21.0 · axios/axios · GitHub](https://github.com/axios/axios/releases/tag/v1.21.0)

**原文标题**: [Release v1.21.0 · axios/axios · GitHub](https://github.com/axios/axios/releases/tag/v1.21.0)

Axios v1.21.0 发布，重点新增响应耗时统计与可选的 UTF-8 Basic 认证，并改进多运行时请求处理；同时调整默认请求头的识别规则，包含一项破坏性变更，并修复 Fetch、代理、TLS、XHR、HTTP/2、URL/Data URL 解析及错误诊断等问题。

- ⚠️ 破坏性变更：仅普通对象、null 原型映射和兼容的 AxiosHeaders 实例会被视为公共或方法级默认头；`Link` 等字面头会保留，自定义类实例需转换为普通映射或 AxiosHeaders。
- ⏱️ 新功能：新增 `response.duration`（毫秒），`error.response` 中也可见；仅统计适配器执行时间，不含拦截器与转换，流式响应在流可用时停止计时。
- 🔐 新功能：新增 `transitional.encodeBasicAuthUsername: true`，支持 XHR/Fetch 的 Unicode 用户名；默认 `false`，保持原有认证行为。
- 🐛 Fetch 兼容：恢复 Cloudflare Workers 等拒绝隐式 `cache: 'default'` 的运行时的请求，同时保留调用方显式设置；响应大小错误保留 `ERR_BAD_RESPONSE` 与请求上下文。
- 🔄 运行时一致性：统一编码字节大小、multipart 上传、代理路由、同源解析、参数合并和表单序列化；循环参数报 `ERR_BAD_OPTION_VALUE`，稀疏或非索引数字表单字段序列化为键控对象。
- 🧭 代理与 TLS：`proxy: false` 时，使用不受支持池管理或 TLS 会话生命周期覆盖的 native `proxyEnv` agent 会报错；HTTPS CONNECT 隧道应用显式 `httpsAgent` 或 `https.globalAgent` 的当前源 TLS 选项。
- 🏷️ 头处理：以安全大小写保留 `__proto__` 头且不改变 AxiosHeaders 原型；`has()`、`delete()`、`clear()` 的函数匹配器现在以 headers 实例作为 `this`。
- 🔗 URL/Data URL：支持大小写不敏感的 URL scheme 与 Base64 标记，修正百分号编码 Base64 data URL 解码，并让 Node data URL 分配估算与解码一致。
- 🧰 错误与拦截器：保留短重建请求栈，并用 `Caused by:` 附加包装错误栈；恢复通过规范数字字符串拦截器 ID 移除拦截器，包括 registry compaction 后。
- 📡 XHR/HTTP/2：XSRF 使用异步 Cookie Store 读取并保留回退、超时与取消；完成后移除进度监听；GOAWAY 后停止复用会话，避免 draining 会话调度空闲计时器延迟退出。
- 🧾 TypeScript：公开 response-default 标记类型，解决涉及未解析响应泛型的 `TS2527` 声明生成问题。
- ⚙️ 维护：降低请求配置合并开销，移除过时 IE 检测，更新 `follow-redirects` 等依赖及文档/CI，完善贡献者流程、赞助商信息和 `NO_PROXY` 回归测试。
- 🌟 社区：欢迎 24 位新贡献者，并完成 1.21.0 版本元数据准备。

---

### [发布 v2.9.8 · denoland/deno · GitHub](https://github.com/denoland/deno/releases/tag/v2.9.8)

**原文标题**: [Release v2.9.8 · denoland/deno · GitHub](https://github.com/denoland/deno/releases/tag/v2.9.8)

Deno 发布 v2.9.8 最新版本，重点包含权限、N-API、Node 兼容性、网络与 TLS 安全等多项修复。

- 🚀 Deno v2.9.8 为最新版本，发布于 2026 年 10 月 21 日；自上一版本以来，main 分支已有 407 次提交。
- 🛠️ 修复 `compile` 对动态导入本地文件的读取权限检查。
- 🐚 修复 zsh 补全，使直接执行 `deno run` 时可补全脚本路径。
- 🧠 修复 core 中 op contexts 的生命周期：让它们保持存活，直到 isolate 被释放。
- 📊 修复 coverage 收集逻辑：跳过 V8 code cache。
- 🌐 fetch 升级 `hyper-util` 0.1.21 和 `hyper` 1.11.1，在连接池为空时取消 idle interval。
- 🧩 修复 N-API：检查 `napi_create_dataview` 的边界溢出；异常待处理时忽略回调返回值。
- 🟢 改进 Node 兼容性：包括 X.509v1 证书处理对齐 OpenSSL、`mock.reset()` 恢复 `mock.method()` 实现、`assert` 支持消息函数和格式化参数。
- 📦 修复 npm 对 package link 名称的校验。
- 🔒 修复 TLS：不再信任受入侵的 eMudhra 证书机构。
- 🎲 将 `rand` 0.9.x 升级到已修补版本。
- 👍 该发布附带 59 个资产，约 30 人进行了互动反应。

---

### [解析器组合子](https://t3.at/blog/parser-combinators/)

**原文标题**: [Parser Combinators](https://t3.at/blog/parser-combinators/)

本文介绍了解析器组合子（Parser Combinators）这一轻量而优雅的解析方法：它介于正则表达式与 tree-sitter 等重型解析库之间，适合把非结构化文本转换成结构化数据。文章从最小解析单元讲起，逐步实现 `pSeq`、`pMap`、`pRepeat` 等组合子，并用解析 `ping` 输出这一完整示例展示其威力。

- 🧩 解析器组合子适合中等复杂度解析任务：比正则更易维护，比 tree-sitter 更轻量。
- 🔹 部分解析器 `Parser<T>` 是一个函数：`(input: string) => [T, string]`，返回“解析结果 + 剩余字符串”。
- 🔗 多个解析器可以按顺序串联，前一个的剩余字符串会交给下一个继续解析。
- 🧱 `pSeq` 把多个解析器组合成一个新解析器，返回元组结果，例如 `["Hello", null, 100]`。
- 🗺️ `pMap` 在解析完成后对结果做映射，把元组转换成更易读的对象结构。
- 🔁 `pRepeat` 会反复应用某个解析器直到失败，类似正则中的 `*`。
- 🧠 文章指出解析串联在函数式编程中类似 `unfold`，与 `reduce/fold` 互为对偶。
- 🛠️ 实战中用 `pString`、`pInteger`、`pDecimal`、`pIpV4Address`、`pWhitespace` 等基础解析器逐步拼出 `ping` 输出的完整解析器。
- 📦 最终可把 `ping` 文本解析为包含 `header`、`packets`、`statistics` 的结构化 `PingResult` 对象。
- ✨ 相比复杂正则，解析器组合子更清晰、可组合、易维护，也支持回溯、前瞻等高级能力。

---

### [死代码不应存在](https://tkdodo.eu/blog/dead-code-shouldnt-exist)

**原文标题**: [Dead Code Shouldn't Exist](https://tkdodo.eu/blog/dead-code-shouldnt-exist)

作者分享了其在多个技术会议上关于清理死代码的演讲，主题是如何借助 Knip 逐步移除 28,000 行代码，并提供了幻灯片、文字记录及联系方式。

- 🗑️ 演讲主题为“Dead Code Shouldn't Exist: How We Removed 28k Lines of Code, One Knip at a Time”，核心是清理死代码。
- 🧰 内容涉及 Talk、TypeScript、JavaScript 和 Knip 等关键词。
- 🎤 该演讲已在 React Paris、JSHeroes、JSNation、React Norway、React Alicante 和 ZurichJS 等多个会议上进行。
- 🔗 文中会议名称链接可跳转到对应演讲录像。
- 📑 文章提供幻灯片和文字记录，支持左右滑动、箭头按钮或方向键切换。
- 🌗 幻灯片会跟随用户的浅色或深色主题。
- 💬 如有问题可通过 Bluesky 联系作者，或在文章下方留言。
- 🔤 文中还推荐了代码块使用的等宽字体 monolisa.dev。

---

### [](https://knip.dev/)

**原文标题**: [Declutter your JavaScript & TypeScript projects | Knip](https://knip.dev/)

Knip 是一款面向 JavaScript/TypeScript 项目的开源清理工具，可自动发现并修复未使用的依赖、导出和文件，帮助开发者精简代码库；它基于项目实际使用的框架与工具链进行细粒度入口分析，适用于单体仓库，结果准确且可执行。

- 🧹 核心功能：查找并修复未使用的依赖、导出和文件，删除死代码，精简项目。
- 🔍 分析方式：从细粒度入口点出发，结合实际框架和工具链进行分析（包括 monorepo），提供准确、可操作的结果。
- 📈 采用广泛：每月 8600 万次下载，超过 21,000 个公开项目使用；Khan Academy、Shopify 等团队信赖。
- 🔌 插件丰富：内置 190+ 插件，支持 Astro、Cypress、ESLint、Jest、GitHub Actions、Next.js、Nx、Remix、Storybook、Svelte、Vite、Vitest、Webpack 等。
- 🧪 易用支持：提供在线 Playground、故障排查文档和介绍视频。
- 👥 社区活跃：由 329 位贡献者共同创建，并有大量文章和用户推荐。
- 💬 用户反馈：被称为“史上最爱软件”“必备工具”，可像 ESLint 一样用于 CI 保持项目整洁。
- 🗑️ 清理效果显著：有用户报告删除约 10 万行、30 万行、4.1 万行死代码，或在 30 分钟内删除 6 千行。
- ✅ 准确度高：有用户在 mono-repo 上使用后称没有误报；工具能自动检测环境并构建代码使用图。
- 🧰 生态扩展：支持 VS Code/Cursor 扩展，并可用 Knip MCP 生成配置文件；TanStack 等 monorepo 也在使用。

---

### [AI JS Day 2026 — 面向前端开发者的直播](https://lp.jetbrains.com/ai-js-day-2026/?utm_source=newsletter_js_weekly&utm_medium=cpc&utm_campaign=webstorm_javascript_day_2026_js_weekly)

**原文标题**: [AI JS Day 2026 â Live Broadcast for Frontend Devs](https://lp.jetbrains.com/ai-js-day-2026/?utm_source=newsletter_js_weekly&utm_medium=cpc&utm_campaign=webstorm_javascript_day_2026_js_weekly)

AI.js Day 2026 是 JetBrains 于 11 月 13 日举办的免费线上活动，以“CH-13”频道形式呈现，主题为“Tune In. Get Uncomfortable.”，面向 JS/TS 与前端开发者，聚焦 AI 时代的职业前景、技能需求、工程判断与 AI 原生工作流。

- 📅 活动时间：11 月 13 日，线上举行，完全免费，需提前注册以保留名额。
- 📺 活动形式：以“Channel 13”深夜节目为创意包装，包含欢迎、主题演讲、联合讨论与总结环节。
- 🧠 核心议题：五年后是否还有工作、前端开发者需要哪些新技能、AI 如何改变代码库与开发流程。
- 🎤 讲者阵容：Danny Thompson、Kent C. Dodds、Marina Wyss、Michael Hablich、Michael Shilman、Danail Hadjiatanasov、Daniel Williams、Jason Torres、Craig Walker、Jesse Lumarie 等。
- 🛠️ 重点演讲：提示与结果之间的分支工程、AI 时代工程师的判断力、从前端转型 AI 工程师的路径、AI 原生前端工作流。
- ⏰ 议程时间：约 16:00–19:00 CET，涵盖多场主题分享与跨工具联合讨论。
- 🔧 工具生态：讨论涉及 Figma、Chrome DevTools、Storybook、MUI、Callstack、WebStorm 等。
- 📝 注册信息：需填写名、姓、邮箱，可选择接收未来 JetBrains WebStorm 活动邮件。
- ❓ FAQ：所有场次将录制并发布到 YouTube；活动免费；观众可在演讲期间通过聊天提问。

---

### [为 AI 生成的 HTML 构建隔离预览 – Master.dev 博客](https://blog.master.dev/building-an-isolated-preview-for-ai-generated-html/)

**原文标题**: [Building an Isolated Preview for AI-Generated HTML – Master.dev Blog](https://blog.master.dev/building-an-isolated-preview-for-ai-generated-html/)

文章聚焦“如何安全预览 AI 生成 HTML”：作者先复现常见的 `srcdoc` 预览，并从同源读取、跳出 iframe、网络外传三个方向证明风险，再给出沙箱、独立源、CSP 与 `postMessage` 校验组合的四层防护方案。

- ⚠️ 常见做法是把模型返回的 HTML 直接写入 iframe 的 `srcdoc`；看似隔离，但未加 `sandbox` 时仍与宿主同源。
- 🕵️ 攻击一：生成页面可读取 `parent.document`、`localStorage`、Cookie 等宿主数据；`sandbox="allow-scripts"` 会因 opaque origin 阻止。
- 🚪 攻击二：页面可尝试顶层导航、弹窗、表单提交；仅有 `allow-scripts` 时会被拦截，添加 `allow-top-navigation` 等权限会重新放开风险。
- 🌐 攻击三：沙箱不能阻止 `fetch` 或图片请求外传数据；需用 CSP 限制网络，如 `default-src 'none'`。
- 🧱 安全基线：从 `sandbox=""` 开始，只按需添加 `allow-scripts`，并说明每个额外权限的理由。
- 🚫 禁止组合：不要同时使用 `allow-scripts` 与 `allow-same-origin`，否则页面可能触及宿主并移除自身沙箱。
- 🆔 身份校验：沙箱页面的 opaque origin 在消息中序列化为 `"null"`，不能白名单该字符串；应使用 `event.source` 校验真实窗口引用。
- 🏰 独立源：高价值场景应把用户内容放到一次性或专用域名，降低沙箱逃逸后的影响。
- 🛡️ CSP：通过可信 `meta` 标签或响应头部署 CSP；响应头更强，且 `srcdoc` 会继承宿主 CSP。
- 🔗 消息通道：预览与父页面通信时校验 `event.source`、消息结构和数值范围，必要时使用 `MessageChannel`。
- ✅ 加固效果：读取宿主、顶层导航、网络外传、伪造 resize 消息均被阻止；合法 resize 消息经限幅后仍可用。
- ⚙️ 实践原则：先最小权限，再加独立源与 CSP，最后守护消息通道；每次放宽策略都应是可命名、可辩护的取舍。
- 🧪 演示说明：五个 Demo 使用真实 iframe 与 `srcdoc`；本地复现需通过 HTTP 和两个端口，`file://` 不适用。

---

### [tsserver 插件之后：嗒](https://jovidecroock.com/blog/typescript-7-content-mappers/)

**原文标题**: [Tada after tsserver plugins](https://jovidecroock.com/blog/typescript-7-content-mappers/)

文章回顾了 TypeScript 7（Go 移植版 tsgo）不再加载 tsserver 插件后，GraphQLSP 提供的编辑器内 GraphQL 诊断、补全与悬停提示会失效的问题；作者借助 TypeScript 7.1 的内容映射器和编程 API，把部分能力迁移到编译器侧，并先用 CSS Modules 项目验证可行性。

- 🔌 GraphQLSP 是 tsserver 插件，可在 `graphql()` 调用中提供诊断、自动补全和悬停信息。
- 🚫 TypeScript 7 不加载 tsserver 插件，`tsconfig.json` 里的 `plugins` 会被解析但不生效，`tsrs` 也一样。
- ⚠️ 切换到 TypeScript 7 后，gql.tada 的类型仍然可用，但字段拼写错误、未知片段、废弃字段、未使用字段等 GraphQL 编辑器错误会全部消失。
- 🧩 TypeScript 7.1 提供两项关键能力：内容映射器（content mappers）和与运行中编译器通信的编程 API。
- 🔄 内容映射器是由 TypeScript 启动并通过 JSON-RPC 通信的进程，在 `tsconfig.json` 中按扩展名注册，包内通过 `package.json` 指定启动方式。
- 📄 TypeScript 遇到对应扩展名文件时，会发送 `transform` 请求；映射器返回 TypeScript 文本、源位置映射和诊断信息，之后编译器把该文件当作 TypeScript 处理。
- 🛑 映射器不能声明内置扩展名（如 `.json`、`.ts`、`.tsx`）；外部代码默认不运行，需要 `tsc --runExternalCode`、工作区信任和编辑器设置启用。
- 🎨 作者先用 `typed-css-modules-mapper` 验证 CSS Modules：直接从 CSS 生成类型，无需维护生成的 `.d.ts` 文件，并支持跳转定义、悬停文档和类名补全。
- 📁 由于映射器看不到 `.ts` 文件内的 `graphql()` 调用，GraphQL 方案改为处理独立 `.graphql` 文件，并把 `# import` 注释转换为真实模块导入。
- 🧬 映射器会把每个 `.graphql` 文件转换为等价的 gql.tada `graphql()` 调用，因此结果类型、`FragmentOf`、`readFragment` 等能力保持一致。
- ✅ 映射器还会加载 schema 并校验文档，未知字段、变量错误和语法错误可在 `.graphql` 文件、`tsc` 和编辑器中显示。
- 💡 作者认为内容映射器适合承接 GraphQLSP 的许多能力，`.graphql` 文件获得模块语义，编辑器工作由编译器完成；内联文档仍需单独检查器，7.1 API 足以构建。
- 🛠️ 相关尝试位于 gql.tada #610、#614、#616 和 GraphQLSP #438，CSS 映射器已发布到 npm。

---

### [对象、属性、映射，天哪！| Max Bernstein](https://bernsteinbear.com/blog/object-shapes/)

**原文标题**: [Objects, attributes, maps, oh my! | Max Bernstein](https://bernsteinbear.com/blog/object-shapes/)

overview summary
文章讨论动态语言对象属性访问的性能问题：朴素实现把对象属性存进哈希表，简单但慢；更优方案是用 map/shape/layout 描述对象布局，结合不可变映射树和内联缓存加速属性读写，并延伸到类与形状分离、类型特化、存储策略及真实运行时内存布局。

- 🐍 动态语言常把对象视为“名称到值”的映射，Python、Ruby、JavaScript 的写法都鼓励这种灵活属性模型。
- ⚠️ 直接用哈希表保存属性虽然直观，但每次属性访问都可能涉及哈希、探测、多次依赖内存加载和缓存未命中，热路径成本很高。
- 🗺️ Map/layout/shape/hidden class 的核心是把属性名映射为小整数索引或偏移量，让快路径不再处理字符串和哈希。
- 🧊 Map 通常是不可变的持久化树/trie；新增属性会生成新 map，对象保存 map 与属性存储，布局变化可通过 map 身份快速判断。
- ⚡ 内联缓存会缓存“期望 map + 属性索引”，先用指针相等检查 map 是否匹配；命中后按索引读取，未命中再按字符串查找并更新缓存。
- 🔀 属性添加顺序和条件初始化会影响对象形状，可能导致多态和缓存未命中；热路径中缓存命中与未命中的性能差异可能很大。
- 🧮 多数对象字段数量较少，字段过多可能退回哈希表或复杂模式；不同类可以共享同一形状，因此形状不能替代类信息。
- 🧪 进一步优化包括按属性类型特化 map、集合存储策略、类版本化；C++ 小运行时草图展示了紧凑对象头、内联属性和溢出槽等真实布局思路。

---

### [软件慢是因为设计糟糕，而不是语言慢](https://www.seangoedecke.com/software-is-slow-because-of-bad-design-not-slow-languages/)

**原文标题**: [Software is slow because of bad design, not slow languages](https://www.seangoedecke.com/software-is-slow-because-of-bad-design-not-slow-languages/)

文章核心观点是：软件性能通常由设计决定，而非编程语言速度。大多数真实程序受 I/O 限制，重写成 C、Rust 或汇编只能优化局部 CPU 热点，难以带来数量级提升；更有效的做法是通过剖析与重新设计减少工作、缓存、异步、并行和优化查询。AI 应帮助发现热点并提出重构方案，而不是盲目重写语言。

- 🧠 软件慢往往源于糟糕设计，而不是使用了“慢语言”；语言速度并非性能主导因素。
- ⏳ 多数真实程序是 I/O-bound，时间主要花在数据库、第三方 API、磁盘和网络等待上。
- 📉 重写成 C/Rust 只能加速非 I/O 部分，受 Amdahl 定律限制，整体收益通常有限。
- 📚 慢语言常已通过 C 扩展和成熟库委托高性能工作，如 Python 的机器学习库、Markdown 渲染库。
- 🔍 真正有效的提速通常来自重新设计：缓存、异步/后台任务、并行、合并 SQL、消除 N+1、跳过不必要操作。
- 🎯 只有少数真正 CPU-bound 且无法减少工作的热点，才适合用更快语言重写局部代码。
- 🤖 使用 AI 优化软件时，应让代理做性能剖析、定位热点、建议重构，而非一开始就要求用 C/Rust/汇编重写。
- 💬 评论区争议包括 CRUD 是否真为 I/O-bound、CPU-bound 程序占比、语言生态对设计难易度的影响；作者仍坚持设计优先。
- 🧩 换语言对可移植性、效率、可维护性有价值，但若目标是原始速度，应优先优化程序设计与工作方式。

---

### [Structs 文档](https://structs.arv.tools/)

**原文标题**: [Structs Docs](https://structs.arv.tools/)

这是 TC39 structs 提案（Stage 2，2024 年 12 月草案）的 JavaScript 实现，提供 structs、shared structs、SharedArray、Atomics.Mutex 与 Atomics.Condition，并包含遵循规范算法的运行时和提案语法编译器。项目状态为实验性，可在浏览器 Playground 中并排查看源码与编译后的 JavaScript。

- 🧱 实现 `struct` 声明：编译器将其降级为调用运行时的类。
- 🔗 实现 `shared struct`：通过一个 `SharedArrayBuffer` 堆上的代理共享同一对象。
- 🧵 示例中 `shared struct Counter` 传给 worker 后仍是同一对象，而不是副本。
- 🔒 使用 `Atomics.Mutex.lock` 配合 `using` 保护共享计数器自增。
- ⚛️ 支持结构体字段上的 Atomics：`load`、`store`、`exchange`、`compareExchange` 可接收 struct。
- 🧷 提供并安装 `Reflect.canBeShared`。
- 📦 提供全局 `SharedArray`：本质是带索引字段和固定长度的 Shared Struct。
- 🔐 提供 `Atomics.Mutex` 与 `UnlockToken`：基于堆字的 futex 风格锁，token 可与 `using` 配合。
- ⏱️ 提供 `Atomics.Condition`：支持 `wait`、带超时与谓词的 `waitFor`、`notify`。
- 🧩 导入 `@arv/structs` 会安装全局对象；编译器输出会导入 `@arv/structs/runtime` 并同样安装。
- 🛠️ TypeScript 编译器可利用类型让 shared struct 字段访问更直接；项目源自 `arv/threads`，并尽量贴近规范、列出与规范的差异。
- 🚀 文档涵盖安装运行、Node hook、CLI、编译器 API、Structs/Shared Structs、Playground 等后续内容。

---

### [GitHub - tc39/proposal-structs：JavaScript 结构体：固定布局对象 · GitHub](https://github.com/tc39/proposal-structs)

**原文标题**: [GitHub - tc39/proposal-structs: JavaScript Structs: Fixed Layout Objects · GitHub](https://github.com/tc39/proposal-structs)

该提案是 TC39 Stage 2 的 JavaScript Structs 提案，旨在引入固定布局对象与共享内存同步原语，以支持高性能共享内存多线程，并为开发者提供比 `class` 更利于优化和静态分析的对象模型。

- 🧩 **四项核心能力**：普通 Structs、共享 Shared Structs、`Atomics.Mutex` 和 `Atomics.Condition`；Shared Arrays 是共享结构体的特殊形式。
- 📦 **普通 Structs**：使用 `struct` 关键字声明，具有密封的固定布局、一次性初始化、字段不可新增、原型不可变、只能继承其他 struct，方法为非泛型。
- 🔐 **Shared Structs**：只能继承共享 struct，原型为 `null`，不能有实例方法，字段只能是原始值或其他共享 struct，可跨 agent 无拷贝传递，不可冻结。
- 🧵 **共享数组**：固定长度、可跨 agent 共享、`length` 只读，元素默认初始化为 `undefined`。
- 🧠 **内存模型**：共享 struct 字段默认无序访问；通过 `Atomics.load/store/exchange/compareExchange` 提供顺序一致性操作，且字段访问不会撕裂。
- 🔒 **Mutex**：非递归互斥锁，本身是无字段共享 struct，通过静态方法加锁；使用 `UnlockToken` 解锁能力降低重复解锁等误用风险。
- ⏳ **Condition**：条件变量，提供 `wait`、`waitFor`、`notify`，用于在锁保护下阻塞、超时等待和唤醒其他 agent。
- 🚧 **待解决问题**：如何为 shared structs 附加方法仍是开放问题，涉及 per-Realm 原型和跨 agent 声明关联机制。
- 🔭 **未来工作**：计划支持异步加锁/等待，并探索与 WasmGC 的互操作及统一内存模型。
- ❌ **明确不在范围**：值语义、不可变性、运算符重载、复杂类型系统、二进制数据覆盖视图等。
- ⚙️ **实现建议**：引擎应使用不可变 shape；共享字段需按指针宽度对齐；字符串共享较困难；同步原语需兼容移动式 GC，可通过固定对象或用户态实现解决。

---

### [结构体游乐场](https://structs.arv.tools/playground/)

**原文标题**: [Structs playground](https://structs.arv.tools/playground/)

TypeScript 可结合结构体（structs）使用，并支持边编辑边编译，最终生成编译后的 JavaScript。

- 🧩 TypeScript 可与结构体（structs）结合使用。
- ⚡ 编辑代码时会即时编译，提供快速反馈。
- 🛠️ 编译输出为 JavaScript。
- 📦 核心流程是从 TypeScript/structs 转换为编译后的 JavaScript。

---

### [推出 TanStack Redact | TanStack 博客](https://tanstack.com/blog/introducing-tanstack-redact)

**原文标题**: [Introducing TanStack Redact | TanStack Blog](https://tanstack.com/blog/introducing-tanstack-redact)

TanStack Redact 0.2.0 发布，它是一个更小的 React 与 React DOM 浏览器替代实现，覆盖应用渲染和更新所需的 React API，无需修改业务代码即可减少浏览器端 JavaScript；已为 TanStack Start、Vite、Vinext 和 Next.js 提供稳定集成，在 Vinext 与 Next.js 中 React 继续负责服务端渲染和 Server Components，Redact 接管水合与客户端渲染。

- 🧩 通过构建配置接入，现有 React 导入、组件、Hook 和依赖可直接在浏览器中使用 Redact。
- 📦 0.2.0 提供 TanStack Start、Vite、Vinext、Next.js 的稳定集成，覆盖 App Router 与 Pages Router。
- ⚙️ 在 Vinext 与 Next.js 中，框架继续负责路由、缓存和 Server Action 传输，React 保留服务端职责。
- 📉 官方小应用 gzip 体积对比：TanStack Start 109.3→62.3 KB，节省 43.0%；Vite 68.3→20.1 KB，节省 70.5%；Vinext 138.1→98.8 KB，节省 28.5%；Next.js 175.6→139.9 KB，节省 20.4%。
- 🔧 默认 Redact 构建已可更小；Start 和 Vite 在关闭未使用可选功能后可分别降至 59.8 KB 和 12.6 KB。
- 🧪 Vinext 六轮基准测试从 154.9 KB 降至 115.5 KB，减少 39.4 KB；生产构建时间基本不变，开发启动略快。
- 🧱 兼容性工作覆盖水合、导航、Suspense、表单、乐观更新和框架内部等场景，是本版本能够发布的关键。
- ⚠️ Redact 同步渲染，不包含 React 的时间切片或可中断渲染；重渲染仍可能延迟输入，建议在应用最繁忙页面实测。
- 🤝 项目仍认可 React 生态的价值，目标是为选择 React API 的团队和代理提供更小、更快的实现，并持续提升兼容性。

---

### [面向编码智能体的 Wallaby | 能捕获真实缺陷的 AI 测试](https://wallabyjs.com/ai/?utm_source=cooperpress&utm_medium=javascriptweekly&utm_content=javascriptweekly)

**原文标题**: [Wallaby for coding agents | AI tests that catch real bugs](https://wallabyjs.com/ai/?utm_source=cooperpress&utm_medium=javascriptweekly&utm_content=javascriptweekly)

Wallaby 是面向编码代理的测试增强工具，帮助 AI 写出能捕获真实缺陷的高价值测试，而不是仅通过但不验证关键行为。它通过技能与命令让代理编写、改进和验证测试，并利用覆盖率、执行轨迹、运行时值和实时结果提升测试质量。

- 🧪 AI 容易生成低价值测试：它们可能通过，但未真正检查关键行为；Wallaby 帮助代理强化断言并验证测试能否捕获回归。
- ⚙️ 安装技能可在终端运行 `npx skills add wallabyjs/skills`，然后在代理聊天中使用 `/wallaby write` 或 `/wallaby improve` 执行任务。
- ✍️ 写测试时，代理会检查预期行为与边界情况，并验证断言；改进测试时，会强化弱断言、补充缺失用例并移除重复检查。
- 📈 内部 Wallaby Bench 评估显示，使用 Wallaby 及技能的代理结果最多提升 40%，综合考量代码与测试质量、速度和 token 效率。
- 🔍 核心反馈包括：按测试的表达式覆盖率、执行轨迹、运行时值和实时测试结果，帮助代理定位未测试代码并判断断言强度。
- 🧬 代理可结合变异测试：引入小变异，检查测试是否失败；若变异存活，则强化断言并复查。
- ✅ 即使测试通过且覆盖率很高，Wallaby 仍可帮助检查金额错误、边界条件等“通过但未验证正确性”的问题。
- 🧹 不会让项目充斥无用测试：代理会检查已有覆盖、补充缺失场景，并移除低价值重复测试，同时保留不同行为。
- 🤖 可用于代理循环或软件工厂流程，通过 `/wallaby write`、`/wallaby improve` 或 `wallaby-cli` 技能运行测试并查看覆盖率、轨迹和运行时值。
- 🧩 支持具备技能能力的代理，包括 Claude Code、Codex、GitHub Copilot、Cursor、OpenCode、Pi 等；容器或云代理在 beta 阶段需要 CLI token。
- 🐍 支持 JavaScript/TypeScript 的 Jest、Vitest、node:test、Mocha、Jasmine、AVA、QUnit、Karma；Python 处于 beta，支持 pytest 和 unittest。
- 🆓 beta 期间可免费使用本地 CLI：运行 `npx --package @wallabyjs/cli wallaby access`，输入邮箱并激活；现有许可证在本机使用无需额外激活或 token。

---

### [发布 v7.0.0 · verdaccio/verdaccio · GitHub](https://github.com/verdaccio/verdaccio/releases/tag/v7.0.0)

**原文标题**: [Release v7.0.0 · verdaccio/verdaccio · GitHub](https://github.com/verdaccio/verdaccio/releases/tag/v7.0.0)

Verdaccio 7.0.0 是 7.x 系列首个稳定版，已发布至 npm 的 latest 和 Docker Hub 的 verdaccio/verdaccio:7、7.0、latest；6.x 继续使用 latest-6 npm 标签和 6 镜像标签，并提供了迁移指南与发布说明。

- 🚀 版本发布：7.0.0 成为 npm latest 和 Docker latest，6.x 进入维护通道。
- 🧪 分阶段发布：实验性 flags.stage 支持先上传版本、维护者审核后再可安装，并提供版本 published/staged 状态查询接口。
- 🔐 安全与认证：实验性 TFA 支持基于时间的一次性密码；htpasswd 增加 verify_cache_ms；npm、yarn、pnpm 登录通过 Basic 例外继续可用。
- 🛡️ 发布权限：publish.check_owners 覆盖 npm deprecate、版本取消发布和 dist-tag 变更；取消版本需独立 unpublish 权限；tarball 上传校验和写入顺序改进。
- 🧩 插件与存储：支持纯 ESM 插件异步加载；提供 Promise 存储插件 API，并为回调式存储插件保留兼容适配器。
- 🎨 Web UI：新增暗色模式、登录/注册/密码页刷新、SWR 状态、按更新时间排序、web.assetFolder、首页工具栏、空注册引导、footer/poweredBy/help、URL 包标签、bun 支持、翻译进度和账户菜单改密。
- 🔎 过滤与通知：包过滤插件支持 allow/block、glob 和 excludeDeprecated；新增发布与取消发布通知钩子。
- ⚙️ 配置与搜索：ConfigBuilder 覆盖 web、listen、https、publish、flags、notify、middlewares、filters 等；新增 server.cors、server.dotfiles、server.hideStaticLogs、server.hidePingLogs、server.legacyAuthCache；/-/v1/search 增加限流、分页、批处理权限检查和上游错误保留。
- 🐞 关键修复：改进 tarball 下载选择、失败清理、content-length 和 304 缓存刷新；避免抓取客户端控制的 off-uplink dist.tarball；权限规则大小写不敏感；名称、令牌、搜索验证更严格；修复 401、Windows HOME 和缺失 Host 头处理。
- ⚠️ 破坏性变更：需 Node.js 24+；升级 Express 5，中间件需使用命名通配符、sendFile 需 root、req.body 已预解析；仅支持 YAML 配置；包 API 使用 Bearer token，_auth 需改为 _authToken；移除 /-/all、npm star/unstar、AES 助手、searchRemote 和调试路由；程序化 API 改为异步 runServer。
- 📦 构建与迁移：Vite 生成 ESM/CJS 双输出，package exports 变更；aws-s3-storage、google-cloud、active-directory 插件迁至独立仓库；server secret 少于 32 字符会停止服务，不再读取 .sinopia-db.json。
- 🔁 6.x 回移：双 ESM/CJS、包过滤插件、发布/取消发布通知、受限搜索、e2e-cli、共享 UI 主题、htpasswd/名称/搜索修复和新 Web UI 首页也已回移至 6.x。
- 🛠️ 工具链与依赖：pnpm 12 替代 Yarn；CI 支持 Windows；e2e 使用 @verdaccio/e2e-cli；升级 Express 5.3、got 15、js-yaml 5、TypeScript 7、Vite 8，并修补多项安全公告；Docker 构建禁用依赖生命周期脚本，并要求第三方依赖至少发布 3 天。
- ⬆️ 升级建议：备份配置、存储和 .verdaccio-db.json；升级至 Node.js 24；将 JSON/JS 配置转为 YAML；用存储副本测试后再切换；不要同时让 6.x 和 7.x 操作同一存储。
- 🙏 贡献者：@juanpicado、@mbtools、@dianmorales、@jotadeveloper 等 12 位贡献者参与本版本发布。

---

### [Biome v2.6——支持新语言、JavaScript 插件、更好的 Tailwind 集成以及 biome inspect 命令 | Biome](https://biomejs.dev/blog/biome-v2-6/)

**原文标题**: [Biome v2.6—Support for new languages, JavaScript plugins, better Tailwind integration and the biome inspect command | Biome](https://biomejs.dev/blog/biome-v2-6/)

Biome v2.6 是一次覆盖语言支持、插件体系、Tailwind 集成、调试工具和底层架构的大版本更新，新增 Markdown、SCSS、YAML 支持，并引入 JavaScript 插件开发者预览、Tailwind v4 感知排序、`biome inspect` 命令、Stylelint 迁移和新推理引擎。

- 📝 Markdown 支持：解析器实现 100% CommonMark 一致性，格式化器约 92% 兼容 Prettier，默认支持 GFM 任务列表、表格和短链接，并可配置 frontmatter 与嵌入代码块分析。
- 🎨 SCSS 支持：格式化开箱即用，现有 CSS lint 规则可用于 SCSS；官方测试套件兼容性超过 90%，剩余问题多与旧特性相关。
- 📦 YAML 支持：解析器对官方测试套件 100% 一致，格式化器 100% 兼容 Prettier；目前提供一条 YAML lint 规则，后续将增加更多规则和 GitHub Workflows 安全规则。
- 🧩 JavaScript 插件开发者预览：可用 `.js` 或 `.ts` 编写自定义 lint 规则，基于 CST、错误恢复解析器和 Rust 基础设施，并可通过 `@biomejs/runtime/plugin` 定义规则。
- 📦 插件分发增强：可通过 npm 包和 `biome-manifest.json` 统一分发配置、GritQL 插件、JavaScript 插件和规则预设；旧式配置分发被视为 legacy。
- 🔗 共享配置插件解析：新增 `resolutionKind` 选项，让插件路径可相对于共享配置解析，便于复用外部配置包。
- 🌬️ Tailwind v4 集成：`useTailwindSortedClasses` 按 Tailwind v4 语义排序，并可读取配置样式表以纳入设计系统变量。
- 🚫 Tailwind 新规则：新增/增强 `noTailwindRawColors`、`noTailwindRestyledComponents`、`useTailwindStaticClassStrings`，帮助避免原始颜色、覆盖组件样式和动态拼接类名。
- 🧭 Tailwind 类名检测统一：所有 Tailwind 规则在 JSX、TSX、HTML、Vue、Svelte、Astro 中以一致方式检测类名，并支持配置 `mergeFunctions`、`variantFunctions`、`attributes`。
- 🔍 `biome inspect` 命令：可检查解析后的完整配置、单个字段、插件启用规则和文件调试信息，包括 CST、格式化 IR 与语义模型。
- ♻️ 递归配置继承：支持从多级祖先扩展配置和插件，仍保留最多 10 层的深度限制以避免循环或溢出。
- 🧳 Stylelint 迁移：新增 `biome migrate stylelint --write`，可迁移规则、覆盖项和忽略模式；目前仅支持 JSON/JavaScript 配置，YAML 尚未支持。
- ✅ 规则推广：将 59 条 nursery 规则提升至稳定分组，覆盖 correctness、suspicious、security、performance、complexity、style 等类别。
- 🏗️ 新架构与推理引擎：底层重写并采用 `salsa` 实现按需增量计算、缓存和取消机制，CLI 与 LSP 更快、更省内存；类型推断改为按需进行，并新增 `--profile-type-inference` 用于分析。
- 💻 独立安装：新增跨平台独立安装脚本，Linux/macOS 使用 `curl`，Windows 使用 PowerShell 即可安装 Biome。
- 🤝 社区参与：可通过测试预览版本、翻译网站、加入 Discord、贡献代码/规则/LSP/编辑器扩展，或通过 Open Collective、GitHub Sponsors 和企业支持计划提供帮助。

---

### [版本 2.7.1 · jashkenas/coffeescript · GitHub](https://github.com/jashkenas/coffeescript/releases/tag/2.7.1)

**原文标题**: [Release 2.7.1 · jashkenas/coffeescript · GitHub](https://github.com/jashkenas/coffeescript/releases/tag/2.7.1)

CoffeeScript 2.7.1 已发布，主要提升对 Node.js 22 及更高版本的兼容性，修复 source map、堆栈跟踪和导入属性支持，并包含数字字面量、性能、文档及 CI 测试范围方面的更新。

- 🚀 发布版本 2.7.1，由 GeoffreyBooth 于 10 月 25 日发布，包含 1 个提交。
- 🧩 兼容 Node.js 22 及更高版本：堆栈跟踪修补和 source map 现已正常工作。
- 📦 支持新的 `with { type: 'json' }` 导入属性语法，同时保留对 `assert` 的支持。
- 🔢 数字字面量支持科学计数法中的大写 `E`。
- 🛠️ 修复带下划线的数字方法调用编译问题，例如 `1_000.toString()`。
- ⚡ 性能改进：`flatten` 辅助函数不再递归，优化 `checkShebangLine` 和数字匹配正则表达式。
- 📝 文档修复：代码片段恢复可运行，修复悬停时行高跳动问题。
- ✅ 持续集成现测试 Node 16 至 Node 26。
- 👥 新贡献者：@cclauss、@Connormiha、@abhayagarwal-dev。
- 🔗 完整更新日志：https://github.com/jashkenas/coffeescript/compare/2.7.0…2.7.1

---

### [发布 oxlint v1.89.0 · oxc-project/oxc · GitHub](https://github.com/oxc-project/oxc/releases/tag/oxlint_v1.89.0)

**原文标题**: [Release oxlint v1.89.0 · oxc-project/oxc · GitHub](https://github.com/oxc-project/oxc/releases/tag/oxlint_v1.89.0)

oxlint v1.89.0 已发布，包含 2 项破坏性变更、广泛的规则推荐级别调整、大量 lint 规则边界修复、性能优化和文档修正。

- 💥 破坏性变更：AST 现在保留静态属性名和静态成员名中的孤立代理项（lone surrogates）。
- 🚀 功能更新：将 Vue 3、React/React Hooks、Promise、Node、Next.js、JSX-a11y、JSDoc、Jest/Vitest、Import、Unicorn、TypeScript 和 ESLint 等规则标记为 recommended。
- 🐛 代理项修复：检查模块说明符和字符串值中是否包含孤立代理项，并在搜索字符串值时避免 UTF-8 转换。
- 🧹 规则修复：修正 `unicorn/no-useless-undefined` 允许 `React.useRef(undefined)`、`prefer-spread` 忽略 `super` 调用等行为。
- 🧠 ESLint 规则修复：覆盖 `prefer-const`、`sort-vars`、`no-loop-func`、`block-scoped-var`、`no-lonely-if`、`sort-imports`、`prefer-arrow-callback`、`sort-keys` 等边界场景。
- 🛠️ 其他规则修复：改进 `prefer-at`、`prefer-native-coercion-functions`、`prefer-string-raw`、`prefer-template`、`no-unused-vars`、`prefer-regexp-test`、`class-methods-use-this`、`no-param-reassign` 等检测逻辑。
- ⚡ 性能优化：`react/jsx-key` 避免冗余的 key 克隆。
- 📚 文档修正：修复规则文档中的无效代码示例。
- 📦 发布信息：本次发布包含 178 个提交，发布于 10 月 19 日。

---

### [宣布 Mutative 2.0：更快的更新与更安全的补丁 | Mutative](https://mutative.js.org/blog/releases/2.0/)

**原文标题**: [Announcing Mutative 2.0: Faster Updates and Safer Patches | Mutative](https://mutative.js.org/blog/releases/2.0/)

概述总结：Mutative 2.0 在保持 1.x API 的前提下重做底层更新路径，显著加速数组、集合、快照与补丁应用，并修复边界情况下的补丁正确性；同时改变自动冻结、构建选择和部分类型行为，升级前需按清单逐项检查。
- 🚀 **总体性能**：在 97 个基准场景中，匹配设置下几何平均比 Immer 11.1.18 快 3.6 倍、比 Mutative 1.3.0 快 4.3 倍；614 个测量单元中仅 6 个慢于 Immer。
- ⚡ **数组优化**：`shift()`、`unshift()`、`splice()`、`reverse()` 等在副本上原生移动元素；删除 1 万项首元素从 8.2ms 降至 7µs，提升超过 1000 倍。
- 🔍 **快照搜索**：大数组只读查找建议先搜索 `current(draft)` 快照，再通过 draft 修改匹配项；1 万项示例耗时 257µs，而 1.3.0 为 15,717µs。
- 🗺️ **Set/Map 与 apply**：Set/Map 查找和更新减少代理开销，Set 只跟踪含 draft 的项；`apply()` 利用原生 `splice()`，并减少路径类型读取。
- 🧩 **补丁正确性**：补丁顺序改为子补丁先于父补丁，补丁值不再深拷贝；修复 `sort()`、赋值、Set 增删并修改、`0/-0`、数组缩扩等回放问题。
- 🛡️ **apply 更严格**：拒绝以 `__proto__` 结尾的路径，Set 仅按索引读取，避免经 Set 触及 `Array.prototype`；`mutable: true` 时替换根状态会抛错。
- ❄️ **自动冻结变化**：`enableAutoFreeze` 会冻结 Map/Set 实例；返回值中的 draft 搜索在开发构建仍检查，冻结对象内不要放 draft；`rawReturn()` 可跳过搜索。
- 🏗️ **构建与错误**：开发/生产构建由 `process.env.NODE_ENV` 选择；生产错误使用编号链接；构建目标改为 ES2018，Node.js 最低仍为 14。
- 🧾 **类型改进**：异步 recipe 返回 `Promise<State>`，`apply()` 支持 `enableAutoFreeze` 并返回 `Immutable<State>`；类型声明支持 TypeScript 5.0+。
- 📦 **包体积代价**：`create()` 生产压缩约 7.9kB，比 1.3.0 多 2.1kB；`create/apply/current/original` 合计 8.5kB，多 2.2kB；Immer 对应约 3.6kB/6.4kB。
- 📉 **性能局限**：手写 reducer 在多数场景仍更快；自动冻结下多字段类实例更新、Set 加补丁、WebKit 冻结大数组等场景可能变慢。
- ⚠️ **升级注意**：无函数或选项重命名/移除，但需用开发与生产构建跑测试、在打包中定义 `NODE_ENV`、更新补丁断言、检查自动冻结和 draft 生命周期；依赖 1.x peer 的库可能导致 npm `ERESOLVE`。
- 🔄 **从 Immer 迁移**：`produce→create`、`produceWithPatches→create+enablePatches`、`applyPatches→apply`、`nothing→rawReturn(undefined)`，去掉插件并用 `mark`；默认不冻结，需按需开启 `enableAutoFreeze`。

---

### [发布 v3.0.0 · SonicJs-Org/sonicjs · GitHub](https://github.com/SonicJs-Org/sonicjs/releases/tag/v3.0.0)

**原文标题**: [Release v3.0.0 · SonicJs-Org/sonicjs · GitHub](https://github.com/SonicJs-Org/sonicjs/releases/tag/v3.0.0)

SonicJS 3.0.0 是在长期 Beta 后发布的首个官方稳定版，基于全新架构重建数据层、认证栈与插件系统，并新增多租户、双因素认证、GraphQL 和项目脚手架等能力，同时完成多项安全加固与问题修复。

- 🚀 发布首个稳定版：SonicJS 3.0.0 是新架构上的首个正式稳定版本，属于重要里程碑。
- 🗂️ Document Model 数据层：统一 5 张表文档仓储，并通过 `q_*` JSON 虚拟生成列支持快速索引查询。
- 🔐 Better Auth 认证栈：支持会话 Cookie、JWT API Token 和基于文档的 RBAC，全面替换旧认证系统。
- 📦 Code-only Collections：通过 `registerCollections([...])` 注册集合，无需数据库表或 UI 建表，并在 `/admin/collections` 提供只读列表。
- 🧩 新 Plugin SDK：引入 `definePlugin()` 和 `registerPlugins()`，移除旧版 `PluginBuilder` 类。
- 🏢 多租户支持：包含租户切换、角色成员、邮件邀请和 `is_super_admin` 标记。
- ✍️ Lexical 富文本编辑器：替代旧编辑器，成为默认富文本字段类型。
- 🔑 双因素认证：支持 TOTP 身份验证器应用及备用码。
- 🌐 GraphQL 插件：通过 GraphQL 端点实现完整文档 CRUD。
- ⚡ 项目脚手架：可使用 `npx create-sonicjs@latest my-app` 快速创建带 D1 + Wrangler 配置的新项目。
- 🛡️ 安全加固：修复管理模板中的 XSS 与 Header 注入风险，升级 Better Auth 1.7.7，修复首次启动外键竞态，并在 CI 中运行完整 E2E 与禁用跳过测试的 lint 门禁。
- 🐛 问题修复：管理端删除改为确认页，保存并关闭后列表与标题更新更准确，并包含多项依赖更新。
- 📥 安装与升级：新建项目使用 `npm create sonicjs@latest my-app`，已有项目可执行 `npm install @sonicjs-cms/core@3.0.0`。

---

### [SonicJS - 面向 Cloudflare Workers 的现代无头 CMS](https://sonicjs.com/)

**原文标题**: [SonicJS - Modern Headless CMS for Cloudflare Workers](https://sonicjs.com/)

SonicJS 发布 v3.0.0，定位为“生于边缘”的无头 CMS：零冷启动、100% MIT 开源且全部功能免费，基于 Cloudflare Workers，也可运行在 Docker、VPS 及任何支持 SQLite 的环境。它主打 AI 原生、边缘性能、无迁移痛苦与无供应商锁定。

- 🚀 **v3.0.0 已发布**：无需注册即可体验真实后台，通过 `npx create-sonicjs@latest my-app` 快速创建项目。
- 🌍 **边缘原生架构**：覆盖 330+ 边缘城市，冷启动 0–5ms，API 响应 15–50ms，默认全球低延迟。
- 🆓 **完全开源免费**：100% MIT 许可，所有功能包含在核心中，无付费墙、无按席位收费、无企业版门槛。
- 🤖 **AI 原生能力**：内置原生 MCP 服务器，支持 Claude Code、Cursor、VS Code 直接读写和发布内容。
- 🔎 **语义搜索**：基于 Cloudflare Vectorize 的 RAG 语义搜索，支持自然语言查询且无需额外基础设施。
- 🧩 **Agent-ready API**：结构化 schema、一致的 REST 接口和自动生成文档，便于 LLM 工具直接理解。
- ⚡ **性能对比突出**：相比 Node.js CMS，冷启动从 500–2000ms 降至 0–5ms，带关联查询的 API 响应从 1–4s 降至 15–50ms。
- 💸 **成本极低**：部署到自己的 Cloudflare 账户，免费额度覆盖每天 10 万请求；典型流量下约 $0–5/月。
- 🛠️ **开发者体验友好**：TypeScript 优先，schema-as-code，自动生成 REST API 和管理后台，一条命令部署。
- 🔌 **插件生态**：内置 25+ 核心插件，涵盖 AI 搜索、表单构建、灵活认证、三级缓存、内容工作流等。
- 🔓 **无锁定、可移植**：同一套代码可运行在 Cloudflare Workers、Docker、VPS、PaaS、Homelab、本地部署等环境。
- 🧭 **解决迁移与付费痛点**：强调语义化版本与自动迁移，避免 Strapi 等产品升级痛苦和高级功能付费墙。
- 👥 **开源社区驱动**：MIT 许可、公开开发、每周发布，提供 Discord 社区与完整更新日志。

---

### [GitHub - sindresorhus/query-string：解析和序列化 URL 查询字符串 · GitHub](https://github.com/sindresorhus/query-string)

**原文标题**: [GitHub - sindresorhus/query-string: Parse and stringify URL query strings · GitHub](https://github.com/sindresorhus/query-string)

query-string 是由 sindresorhus 维护的 npm 包，主要用于解析和序列化 URL 查询字符串，提供 parse、stringify、extract、parseUrl、stringifyUrl、pick、exclude 等 API，支持多种数组格式、类型转换、排序与 URL 片段处理；仓库约 6.9k stars，采用 MIT 许可证。

- 📦 安装方式为 `npm install query-string`；注意包名中的连字符，不要安装已废弃的 `querystring` 包。
- 🌐 浏览器端面向最新版 Chrome、Firefox 和 Safari；简单场景可考虑原生 `URLSearchParams`。
- 🔍 `parse(string, options?)` 可将查询字符串解析为对象，自动忽略开头的 `?` 或 `#`，返回无原型对象。
- 🧩 `arrayFormat` 支持 `none`、`bracket`、`index`、`comma`、`separator`、`bracket-separator`、`colon-list-separator` 等数组表示方式。
- 🎯 `types` 可为指定参数显式声明类型，如 `boolean`、`string`、`number`、`string[]`、`number[]` 或自定义函数，并优先于 `parseNumbers`、`parseBooleans`、`arrayFormat` 等通用选项。
- 🧵 `stringify(object, options?)` 可将对象序列化为查询字符串并默认排序键名，支持字符串、数字、bigint、布尔值、null、undefined 及其数组。
- ⚠️ `stringify` 遇到 Symbol、函数或普通对象等非支持类型会抛错；数组需通过 `arrayFormat` 控制序列化形式。
- 🔧 常用选项包括 `decode`、`encode`、`strict`、`sort`、`skipNull`、`skipEmptyString`、`replacer`，可用于编码控制、排序、跳过空值和自定义转换。
- 🌐 `extract` 可从 URL 中提取查询字符串；`parseUrl` 返回 `url`、`query`，并可选解析 `fragmentIdentifier`；`stringifyUrl` 是其逆向操作。
- ✂️ `pick` 与 `exclude` 可按键名或过滤函数筛选 URL 查询参数，返回新的 URL 字符串。
- 🚫 该模块有意不支持嵌套查询参数，因为缺乏统一规范且边界情况多；建议将嵌套对象用 `JSON.stringify` 后作为普通值传递。
- 🔁 支持同一键的多个实例，解析时会形成数组；序列化数组时也可通过重复键输出。
- ❓ 假值序列化规则：`false` 输出为 `foo=false`，`null` 输出为 `foo`，`undefined` 会被省略。

---

### [发布 v10.0.0 · sindresorhus/query-string · GitHub](https://github.com/sindresorhus/query-string/releases/tag/v10.0.0)

**原文标题**: [Release v10.0.0 · sindresorhus/query-string · GitHub](https://github.com/sindresorhus/query-string/releases/tag/v10.0.0)

query-string v10.0.0 是一次包含破坏性变更的大版本更新，要求 Node.js 22，并重点修正 stringify/parse 的编码、数组格式、类型解析与 URL 往返一致性，同时带来线性时间解码和多项 TypeScript、排序、空值处理修复。

- ⚠️ 破坏性变更：要求 Node.js 22；`stringify()` 对对象、函数、Symbol、`Date` 等无法表示的值抛出 `TypeError`，需用 `replacer` 转换。
- 🔁 `parse()` 对所有 `arrayFormat` 都将重复键收集为数组，不再只保留最后一个值。
- 🧮 显式 `types` 优先于 `parseNumbers`/`parseBooleans`；不匹配类型的值保持字符串；`string[]`/`number[]` 始终返回数组（`arrayFormat: 'none'` 除外）。
- 🌐 非法 UTF-8 的百分号编码字节解码为 `U+FFFD`；`bracket-separator` 不再按百分号编码的分隔符拆分。
- 🔗 `stringifyUrl()` 对 `fragmentIdentifier` 中的 `%` 编码；片段标识符按解码值处理，可与 `parseUrl()` 往返。
- 🎯 `pick()`/`exclude()` 原样写回保留参数；解析选项仅影响过滤判断，不再改写 URL 中的值。
- ⚡ 移除 `decode-uri-component`，解码改为线性时间；修复 `comma`/`separator` 下重复键解析的二次复杂度。
- 🧾 TypeScript 解析类型跟随 `parseNumbers`、`parseBooleans`、`types`，覆盖 `parseUrl()`、`pick()`、`exclude()`；显式 `undefined` 使用默认值。
- 🐞 修复 `stringify()` 往返不一致、孤立代理项 `URIError`、`sort` 选项多种异常，以及 `stringifyUrl()`/`pick()`/`exclude()` 在 `encode: false`、已有参数、空白、`index` 数组等场景的损坏问题。
- 🛡️ 其他修复包括 `parse()` 的 `index` 格式普通值顺序、`Object.prototype` 继承键、`replacer` 与 `skipNull`/`skipEmptyString`、重复读取触发 getter/Proxy，以及 `stringifyUrl()` 接受 `interface` 查询对象。

---

### [GitHub - share/sharedb：基于操作转换（OT）的实时数据库后端 · GitHub](https://github.com/share/sharedb)

**原文标题**: [GitHub - share/sharedb: Realtime database backend based on Operational Transformation (OT) · GitHub](https://github.com/share/sharedb)

ShareDB 是一个基于操作转换（OT）处理 JSON 文档的实时数据库后端，也是 DerbyJS Web 应用框架的实时后端；仓库提供文档、示例和开发说明，适合构建多用户实时协作应用。GitHub 页面显示其约有 6.5k Star、458 Fork、99 Watcher，并有 152 个 Issue、24 个 Pull Request 和 1,692 次提交。

- 🚀 核心定位：基于 Operational Transformation（OT）的实时数据库后端，支持 JSON 文档实时同步。
- 👥 协作能力：支持多用户并发协作，提供同步编辑 API，并通过异步最终一致性处理更新。
- 🔍 实时查询：支持实时查询订阅，并可通过投影选择文档和操作中的所需字段。
- 🗄️ 数据库集成：可与任意数据库简单集成，并通过 pub/sub 集成实现水平扩展。
- 🧩 扩展能力：提供中间件，用于实现访问控制和自定义扩展。
- 💻 运行环境：适用于浏览器端和服务器端。
- 📡 离线与在线：支持断线重连后的离线变更同步，以及实时用户在线状态同步。
- 🕰️ 历史版本：支持访问文档的历史版本。
- 🧪 测试支持：内置数据库和 pub/sub 的内存实现，便于单元测试。
- 📚 文档与示例：官方文档位于 share.github.io/sharedb，提供计数器、排行榜等示例。
- 🛠️ 本地开发：文档使用 Jekyll，需要 Ruby >2.4.0 和 Bundler，可通过 npm 脚本安装并启动本地文档服务。
- 📊 仓库概况：6.5k stars、458 forks、99 watching、152 issues、24 pull requests、1,692 commits。

---

### [Expo — 使用 React 构建原生应用](https://expo.dev/?utm_campaign=mobile-ai-infra&utm_source=email&utm_medium=javascriptweekly&utm_term=home&utm_content=Cooperpress)

**原文标题**: [Expo — Build native apps with React](https://expo.dev/?utm_campaign=mobile-ai-infra&utm_source=email&utm_medium=javascriptweekly&utm_term=home&utm_content=Cooperpress)

Expo 是面向 AI/智能体时代的移动基础设施平台，提供从开发、测试、部署到监控的全流程工具，帮助团队用单一代码库构建并发布 Android、iOS 和 Web 应用。

- 🧠 定位为“Agentic mobile infrastructure”，服务智能体工作流，覆盖 Develop、Test、Deploy、Monitor 四大环节。
- 🛠️ 开发工具包括 Expo CLI、Skills、MCP；可用 Expo Go 真机测试，用 Simulators 验证，并通过 Launch 或 Builds 分发。
- ☁️ 测试基础设施提供云端模拟器和设备能力；Workflows 可在每次变更时运行测试套件，编码智能体无需 Mac 即可驱动模拟器，并附截图、录屏和日志作为证明。
- 🚀 部署支持 Build 发布到 Android、iOS、Web、TestFlight 和应用商店；Update 提供 OTA 更新、渠道和分批发布控制。
- 📈 Observe 提供生产环境崩溃信息、性能指标和 Update 采用率监控，并可通过 Update 快速推送修复。
- 📦 Expo SDK 已发展 10+ 年，提供 100+ 生产级 API，一次安装即可使用，并欢迎原生代码。
- 🧩 基础设施支持 Expo、React Native、Swift、Jetpack Compose、Kotlin 等技术栈。
- 👥 社区与规模数据：3M+ 开发者、50K+ GitHub stars、7M+ 周下载、100K+ 活跃开发者、500K+ 项目、100K+ 日构建；80% React Native 开发者选择 Expo。
- 💬 开发者反馈积极，称 Expo 简化 React Native 开发、跨平台高效、升级和更新便捷；Discord 社区有 70K+ 成员。
- ✅ 合规与认可：获 Meta 推荐、为 React Foundation 成员，符合 SOC 2 Type II、GDPR、CCPA，并支持 SSO。

---

### [Fingerprint | 业界领先的机器人检测](https://fingerprint.com/try/bot-detection/?utm_source=JSWeekly102726&utm_medium=newsletter)

**原文标题**: [Fingerprint | Industry-leading Bot Detection](https://fingerprint.com/try/bot-detection/?utm_source=JSWeekly102726&utm_medium=newsletter)

Fingerprint 提供面向开发者与反欺诈团队的隐形机器人检测 API，可在约 10 行代码内接入网站，无需 CAPTCHA 或用户挑战，即可在保持流畅体验的同时识别并拦截恶意自动化流量，并区分合法 AI 代理与恶意机器人。

- 🛡️ **隐形检测**：无需验证码、拼图或复选框，不打断真实用户和合法 AI 代理的体验。
- ⚡ **快速集成**：通过 `npm i @fingerprint/agent` 安装，使用 API Key，约 10 行代码即可接入。
- 🤖 **AI 代理识别**：可识别已签名、已验证和未知代理，如 ChatGPT Agent、Gemini、Claude、Manus 等，并持续更新机器人库。
- 🧾 **服务端判断**：通过事件数据判断 `event.bot !== "not_detected"`，可阻止可疑注册、交易或登录行为。
- 🚫 **反欺诈场景**：防止虚假注册、优惠券滥用、账户接管、内容抓取等自动化攻击。
- 🧩 **技术栈友好**：支持 JavaScript、React、Next.js、Vue、Nuxt、Angular、Svelte 等前端框架，后端可自由消费数据。
- 🧠 **多信号检测**：不仅判断是否为机器人，还结合更多信号分析流量真实意图，区分好坏自动化。
- ⚙️ **规则引擎**：无需写代码即可部署规则，拦截复杂机器人、开发者工具、反检测浏览器、虚拟机与数据中心 IP。
- 🌍 **广泛信任**：Booking.com、Dropbox、Plaid、Binance、Resend 等公司使用。
- 📈 **开源基础**：基于 Fingerprint 开源库，GitHub 星标 31.2K+，NPM 月下载量 5,400,000+。
- ✅ **低门槛上手**：支持包管理器或 CDN 快速设置，无需信用卡或销售电话即可免费开始。

---

### [eMudhra、Brotli 与安全修复的长尾 | Socket](https://socket.dev/blog/emudhra-brotli-security-fix)

**原文标题**: [eMudhra, Brotli, and the Long Tail of a Security Fix | Socket](https://socket.dev/blog/emudhra-brotli-security-fix)

文章指出，eMudhra 证书弱密钥与 Brotli 解码器漏洞的修复不只是升级主项目，还要追踪捆绑库、运行时和证书存储，并确认实际运行的服务已使用修复版本。

- 🔑 eMudhra 八个中间 CA 私钥可被恢复，实际仅约 8 位强度、可穷举，弱密钥问题近 18 个月未被发现。
- 🌐 浏览器可通过 OneCRL/CRLSet 在数小时内阻断相关证书，但命令行工具、SDK 和独立证书包可能仍然信任它们。
- 🧩 Brotli 漏洞 CVE-2026-111497 可在解码恶意输入时破坏内存，影响 Node 以及复用 Google Brotli 库的项目。
- 📦 Bun、Python Requests、.NET 等也可能受影响；打包进可执行文件的运行时不重新构建就不会自动修复。
- 🛠️ 更新系统库不等于更新应用内捆绑副本；共享库或运行中的服务可能还需重启才能加载修复。
- 🍎 证书验证尤其隐蔽：macOS 安全框架的更新不一定覆盖读取 `/etc/ssl/cert.pem` 的命令行工具。
- 🧭 建议梳理每次发布内容，追踪依赖、捆绑运行时/库/工具链和证书配置，并准备自动化重建路径。
- ⏳ 补丁未到时可禁用受影响功能或阻断不可信输入，并验证缓解措施确实有效。
- ✅ 最终要测试应用实际使用的验证器/解码器，确认发布物和运行服务都包含修复，并跟踪安装部署而非只看公告。
- 🤖 AI 有助于发现漏洞，也会带来更多待追踪修复；同样可用于依赖挖掘，但仍需人工确认实际交付物。

---

### [我们刚刚向开源维护者捐赠了一百万美元 | Sentry 博客](https://blog.sentry.io/another-year-another-1-000-000-to-open-source-maintainers/)

**原文标题**: [We just gave a million dollars to Open Source maintainers | Sentry Blog](https://blog.sentry.io/another-year-another-1-000-000-to-open-source-maintainers/)

Sentry 今年将资助开源维护者的预算从 75 万美元提高到 100 万美元，并通过直接赞助、基金会捐赠和 Open Source Pledge 等方式，把资金分配给其依赖的开源项目与维护者，强调使用开源的公司应回馈生态。

- 💰 Sentry 向开源维护者捐赠 100 万美元，预算较此前的 75 万美元增加。
- 🔄 理由：开源软件是“终极作弊码”，公司受益于共享库、框架和工具，应支持维护者，让生态持续运转。
- 🤖 AI 技术栈也依赖开源；Sentry 继续支持 NumFOCUS，资助科学计算工具。
- 🤝 Open Source Pledge 成立两周年，37 家成员公司已向维护者和基金会支付 8,421,535 美元。
- ⚠️ 以 PSF 为例：其 AWS 支出同比增长约 69%，反映 AI、代理和 CI 对 Python 基础设施需求上升，需要更多资金。
- 💸 分配：49.5 万美元给 thanks.dev，分发给数百名依赖维护者；10 万美元通过 ecosyste.ms Funds 支持 Python、Django、Ruby、Rust、JS、Go 等关键包。
- 🔍 与 Software Stewardship Lab 合作，识别并资助常规依赖分析遗漏的“幽灵依赖”维护者。
- 🏛️ 向多个基金会捐款：PSF 6 万、PHP Foundation 4.5 万、Ruby Central 4 万、Django 4 万、Packagist 3.5 万等。
- 🎙️ Syntax 团队另用 10 万美元赞助 FFmpeg、Jellyfin、OBS、pnpm、Three.js 维护者等项目。
- 🙏 文末感谢所有开源维护者，并呼吁更多公司加入 Open Source Pledge 或 thanks.dev 回馈生态。

---

### [请稍等……](https://css-tricks.com/css-tricks-has-a-new-owner/)

**原文标题**: [One moment, please...](https://css-tricks.com/css-tricks-has-a-new-owner/)

当前内容仅为网页加载与验证等待提示，未包含可总结的文章正文或关键信息。

- ⏳ 页面显示“Loader”，表示内容正在加载。
- 🔍 提示“Please wait while your request is being verified...”，说明请求正在验证中。
- 📄 未提供实际文章内容，因此无法提炼更多要点。

---

### [告别 Arc](https://arc.net/)

**原文标题**: [A farewell to Arc](https://arc.net/)

Arc 团队宣布将于 2026 年 12 月 22 日正式停用 Arc，并将工程与安全团队的重心转向新浏览器 Dia；现有用户需要在截止日期前迁移或导出数据，移动端功能也会分阶段关闭。

- 🗓️ Arc 将于 2026 年 12 月 22 日停止在 macOS 和 Windows 上使用，届时账号将被停用，个人数据将在 30 天内删除。
- 🔐 官方表示，持续维护浏览器安全需要大量投入，而且在 AI 时代安全挑战加剧，因此团队将资源集中到从底层为当前安全标准打造的 Dia。
- 📅 2026 年 10 月 22 日起，Arc 不再创建新账号；现有用户暂时不受影响，最新版 Arc 支持导出全部数据，并可更顺畅地导入 Dia。
- 📱 2026 年 11 月 23 日起，iOS 和 Android 版 Arc 的 Browse for Me 等 AI 功能将关闭，用户不能再登录或同步标签页；Arc Search 仍可作为轻量浏览器使用。
- 🗑️ 2026 年 12 月 22 日，Arc 账号将停用，相关个人数据在 30 天内删除；Android 版 Arc Search 将从 Google Play 下架并从设备移除。
- 🔄 迁移到 Dia 较简便：密码、书签、扩展、历史记录、Spaces、Folders 和 Tab Groups 可完整导入。
- 🧭 Arc 的 Spaces 在 Dia 中变为 Profiles；侧边栏标签、固定标签、收藏和文件夹等熟悉功能都会保留。
- 🆓 Dia 中 Arc 常用浏览器功能免费，AI 功能为可选；官方称 Dia 在稳定性、速度和安全性上已超过 Arc。
- 🛟 用户应在 2026 年 12 月 22 日前将 Arc 数据导入 Dia 或导出；截止前可通过 Arc 帮助中心聊天获得支持。

---

### [Dia | 让工作日更美好的浏览器。](https://www.diabrowser.com/)

**原文标题**: [Dia | The browser for better days at work.](https://www.diabrowser.com/)

Dia 定位为“不止是浏览器”的 AI 工作浏览器，旨在通过整合日历、收件箱、Slack、Notion、Teams、GSuite 等工具与标签页上下文，帮助用户更高效地开始工作、查找答案、生成报告和演示文稿，并提供分屏、标签分组、隐私控制及企业级安全功能，支持 macOS 与 Windows 免费下载。

- 🌅 **晨间简报**：Morning Brief 汇总日历、收件箱和关键链接，让用户提前了解当天安排。
- 🔗 **跨工具整合**：向 Dia 提问即可收集 Slack、Notion、Teams 等分散信息，并生成可分享的报告。
- 🔍 **上下文问答**：一次提问即可跨 GSuite、Teams 和标签页深入检索，像熟悉所有讨论的人一样作答。
- 👤 **多场景 Profiles**：将工作、自由职业和个人生活分开，独立标签、登录与 AI，滑动即可切换。
- 💼 **Live Work 聚合**：把 GitHub、Notion 等工作发生地放入标签栏，一键直达 PR、规格或草稿。
- 📅 **更好会议体验**：自动打开会议页面、议程、笔记和相关文档，并倒计时提醒准时参会。
- 🪟 **Splits 分屏**：并排查看会议与文档，记住常用布局，一键恢复 1:1 或专注场景。
- 📊 **Decks 生成演示**：让 Dia 将零散上下文整理成带标题、布局和流程的幻灯片。
- 🗂️ **标签整理**：按主题命名并分组相关标签，如“Design Review”“Q2 Planning”，保持工作区整洁。
- 🔒 **隐私优先**：用户可控记忆、连接工具、追踪器、广告与数据共享；数据不出售、不用于广告画像，Sync 端到端加密。
- 🏢 **Dia for Work**：提供 SSO 和管理员工具等企业级安全护栏。
- ⬇️ **免费下载**：Dia 可免费下载，适用于 macOS 和 Windows。

---

### [在 Google Docs 和 Drive 中原生预览、编辑和协作处理 Markdown（.md）文件 - Google 开发者博客](https://developers.googleblog.com/preview-edit-and-collaborate-on-markdown-md-files-natively-in-google-docs-and-drive/)

**原文标题**: [
            
            Preview, edit, and collaborate on markdown (.md) files natively in Google Docs and Drive
            
            
            - Google Developers Blog
            
        ](https://developers.googleblog.com/preview-edit-and-collaborate-on-markdown-md-files-natively-in-google-docs-and-drive/)

Google Workspace 正在打通代码与协作之间的壁垒，让开发者与 AI 代理能在熟悉的实时环境中共同处理文档。Google Docs 与 Drive 现已原生支持 Markdown（.md）文件的预览、编辑和协作，无需手动转换格式，从而提升技术文档的编写与审阅效率。

- 📄 **原生 Markdown 支持**：可直接在 Google Docs 中查看、编辑和协作处理 .md 文件，无需转换文件类型，并在文档头部显示 .md 标识。
- 👀 **Drive 内预览**：在 Google Drive 中可预览格式丰富的 Markdown 文件，支持表格和超链接，也可切换查看原始文本。
- 🤝 **人机协作**：Markdown 作为人与 AI 工具之间的通用语言，便于团队成员和 AI 代理共同编辑同一文档。
- 💬 **实时协作与评论**：支持多人及 AI 代理同时编辑，并可通过 Google Docs 评论功能进行行级反馈和建议跟踪。
- 🕘 **版本历史**：保留完整修订记录，清晰追踪人类贡献者和 AI 代理的所有修改。
- 🚀 **无需额外工具**：省去手动转换和单独查看器的麻烦，保持底层文档适用于开发者工具和 Git 仓库。
- 🌐 **可用性**：任何拥有 Google 或 Workspace 账户的用户，均可将 .md 文件上传至 Google Drive，并直接在 Google Docs 中开始协作。

---

