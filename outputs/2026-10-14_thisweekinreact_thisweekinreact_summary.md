### [](https://trustedrouter.com/?utm_source=thisweekinreact&utm_medium=sponsored_newsletter&utm_campaign=primary_20261014&utm_content=privacy_with_proof)

**原文标题**: [TrustedRouter: The AI router that shows its work](https://trustedrouter.com/?utm_source=thisweekinreact&utm_medium=sponsored_newsletter&utm_campaign=primary_20261014&utm_content=privacy_with_proof)

TrustedRouter 是一个隐私优先的 AI 网关，通过单一 OpenAI 兼容 API 提供 662 个模型的访问，强调加密、可验证性和灵活路由。

- 🔐 所有 AI 对话全程加密，支持机密访问数百个模型
- 🔌 只需更改 base_url，即可无缝迁移现有 OpenAI 格式调用
- 🆓 无需信用卡，赠送 100 万免费 token
- 🤖 支持 Claude、GPT、Gemini、Grok、DeepSeek、GLM、Kimi、MiniMax 等主流模型
- 🏷️ 每个路由均标注隐私级别（ZDR、E2EE），价格透明可查
- 💰 按 token 计费，仅收取 5.5% 提供商成本费，无月费、无席位费
- 🛡️ 支持 BYOK（自带密钥），可使用自有提供商账户
- ✅ 网关运行于可信执行环境，提供可验证的构建证明
- 🚫 若无可满足隐私最低要求的路由，请求会在推理前停止（故障关闭）
- 📊 三大云平台持续监控，公开延迟与可用性历史
- 💳 支持信用卡、ACH、PayPal 或加密货币支付，并可设置严格预算控制
- ⚖️ 客户案例：RRH 在三周内处理 17 万份法律文档、数十亿 token，全程通过可信网关

---

### [](https://trustedrouter.com/trust?utm_source=thisweekinreact&utm_medium=sponsored_newsletter&utm_campaign=primary_20261014&utm_content=verify_privacy)

**原文标题**: [Verify TrustedRouter Attestation and Running Code](https://trustedrouter.com/trust?utm_source=thisweekinreact&utm_medium=sponsored_newsletter&utm_campaign=primary_20261014&utm_content=verify_privacy)

TrustedRouter 的信任页面说明如何通过新鲜、TLS 绑定的远程证明验证托管推理服务：将运行中的构建追溯到已发布源码与构建来源，区分路由器防护和模型提供商隐私声明，并报告已验证证据、失败项及无法验证的内容。

- 🔎 验证方式：让代理访问 https://trust.trustedrouter.com，核验 https://trustedrouter.com 的新鲜、TLS 绑定证明，并把运行构建追溯到公开源码与构建来源。
- 🧱 信任边界：托管 API 应运行已发布开源工作负载；api.trustedrouter.com 是提示路径，公共 TLS 在已测量的 GCP Confidential Space 工作负载内部终止。
- 🚫 控制面隔离：TrustedRouter 控制面不提供生产推理路由，也不接收提示或输出正文。
- ✅ 客户端验证：获取实时证明，验证 JWT 签发者/受众/摘要，并将测量镜像摘要与此处发布数据比较。
- 📄 当前 GCP 工作负载：源码提交 9dd1571d；镜像为 us-central1-docker.pkg.dev/quill-cloud-proxy/quill/enclave-multi:gcp-release-9dd1571d；摘要为 sha256:2bff68260ef529eec790262fb0c1acebc042a79061fd8e164b58a76ef5c18a96；网关仓库为 Lore-Hex/quill-cloud-proxy。
- 🧪 验证步骤：经普通公共 TLS 获取 /attestation；确认 JWT issuer 为 https://confidentialcomputing.googleapis.com；audience 为 quill-cloud；比对镜像摘要；检查 TLS 证书指纹绑定到证明 nonce。
- 🌐 DNS 要求：api.trustedrouter.com 必须保持 DNS-only 或 TCP 直通；若由 CDN 终止 TLS，会破坏托管代码信任声明。
- 📦 已发布文件：image-digest-gcp.txt、image-reference-gcp.txt、gcp-release.json、aws-release.json、azure-release.json。
- ☁️ GCP Confidential Space：测量容器镜像摘要；attestation issuer 为 confidentialcomputing.googleapis.com；发布记录为 gcp-release.json；需将实时证明 JWT 中的 image_digest 与 audience 对照检查。
- 🧊 AWS Nitro Enclaves：测量 enclave 镜像文件的 PCR0（SHA-384），使用 COSE_Sign1 与 AWS Nitro PKI；API 为 https://api-aws.trustedrouter.com/v1；发布记录为 aws-release.json。
- 🔐 AWS 特殊点：该平面使用 enclave 内部生成的证书而非公共 CA；证书指纹与 TLS exporter 绑定进证明，需用 --attested-cert-only 验证。
- 🛡️ Azure Confidential Containers：测量 SEV-SNP hostdata（对 CCE policy 的 sha256）；MAA issuer 包括 trquilluaen 与 trquillsyd；API 为 https://api-azure.trustedrouter.com/v1；发布记录为 azure-release.json。
- 🧩 三种测量不同：GCP 测容器镜像，AWS 测 enclave 镜像文件到 PCR0，Azure 测约束容器的策略；验证者一次针对一个平面使用该平面的记录。
- 🔄 测量是集合而非单值：滚动发布时密钥同时绑定旧/新测量；只固定单值的验证者会在发布窗口失败。
- 🙈 无提示日志：普通同步与流式提示/输出存储已禁用；可选 Batch API 使用单独记录的加密保留；生成内容端点返回兼容的 content_not_stored。
- 📚 开源组件：control plane、attested gateway、cloud infra、Python/JS SDK、provider conformance suite 等仓库公开。
- ⛔ Fail closed：若证明、计费授权或网关契约不可用，提示路径应失败，而不是静默降级到非证明路由。
- 🤖 机器可读发布：JSON 列出可接受镜像摘要/引用、API 基址与别名、audience、issuer、数据策略、平台、滚动发布状态、源码仓库和 TLS 模式 acme-inside-confidential-space。

---

### [](https://trustedrouter.com/?utm_source=thisweekinreact&utm_medium=sponsored_newsletter&utm_campaign=primary_20261014&utm_content=body_cta)

**原文标题**: [TrustedRouter: The AI router that shows its work](https://trustedrouter.com/?utm_source=thisweekinreact&utm_medium=sponsored_newsletter&utm_campaign=primary_20261014&utm_content=body_cta)

TrustedRouter 是一个隐私优先的 AI 网关，通过单一 OpenAI 兼容 API 聚合数百个模型，提供可验证的安全路由。

- 🔒 **隐私优先设计**：不记录提示词或输出内容，所有 AI 聊天加密处理，支持端到端加密（E2EE）与零数据保留（ZDR）
- 🔌 **一站式模型访问**：接入 662 个模型（如 Claude、GPT、Gemini、DeepSeek、GLM 等），通过一个 API 密钥即可调用
- 🚀 **快速迁移**：仅需更改 `base_url`，即可从 OpenAI 或 OpenRouter 无缝迁移，保留现有代码结构
- 🛡️ **可验证信任**：网关运行在可信执行环境（TEE），开源代码与运行时构建认证绑定，支持公开验证
- ⚠️ **失败即关闭**：若无路由满足隐私最低要求，请求会在推理前停止，绝不静默降级到弱隐私路由
- 💰 **灵活定价**：仅按提供商成本收取 5.5% 费用，无月费、无座位费，支持自带密钥（BYOK）及多种支付方式
- 📊 **精细支出控制**：按密钥设置日/周/月预算，严格统计正在运行的请求，避免超额
- 🏢 **企业级案例**：RRH 律所用其处理 17 万份法律文档和数十亿令牌，三周内投产，确保特权文件安全

---

### [](https://tanstack.com/blog/tanstack-start-1-0)

**原文标题**: [TanStack Start 1.0 is Stable | TanStack Blog](https://tanstack.com/blog/tanstack-start-1-0)

TanStack Start 1.0 正式发布稳定版，经过漫长开发与大量企业生产环境验证后，官方正式承诺 API 稳定性，并回顾了从 Router 起步、框架设计理念、RSC 探索、AI 代理冲击以及合作伙伴支持等完整历程。

- 🎉 **1.0 正式稳定**：TanStack Start 1.0 终于发布稳定版，官方宣布可正式用于生产环境，不再附带 RC 警告。
- 🏢 **企业提前押注**：许多初创公司乃至财富 500 强企业早在 beta 阶段就坚持将其投入生产，体现了社区的高度信任。
- 🧭 **始于 Router**：项目最初源于作者想打造一个类型安全的 Router，让路由、参数、搜索参数、loader 数据与上下文都能被编辑器精确推断。
- 💡 **TypeScript 观念的转变**：作者曾认为 TS 多余，但在 React Query 实践中意识到类型可以作为 API 设计的一部分，提前减少开发者的记忆负担。
- 🚀 **Start 的诞生**：2023 年 12 月出现服务端工具雏形，2024 年 5 月 `react-router-server` 包正式更名为 `start`。
- 🧩 **提供另一种选择**：在 Next.js 押注 RSC、React Router/Remix 变革之际，Start 希望保留 SPA 开发的高效体验，同时加入 SSR、流式渲染与服务端函数。
- 🔀 **显式控制运行位置**：通过 `createIsomorphicFn` 与 `createServerFn`，开发者能明确指定代码在服务端还是客户端运行，并自动剔除无用实现。
- 👥 **核心贡献者功不可没**：Manuel、Flo、Chris 分别推进了 SSR 性能（吞吐量约提升 5.5 倍）、类型安全性能与 API 设计，让框架远超作者最初设想。
- 🌍 **框架无关性**：坚持跨框架设计，支持 Solid、Rsbuild，并采纳 Ryan Carniato 建议使用 Vite 与 Nitro 避免自维护部署适配器。
- ⚛️ **对 RSC 的理性取舍**：虽投入大量精力支持 RSC，但作者最终在 tanstack.com 上停止使用它，认为其增加理解成本，并庆幸能自由选择是否启用。
- 🤖 **AI 代理改变开发**：2025 年底起 AI 显著影响工作流，安全审计、性能优化与 PR 数量激增，类型安全与显式 API 设计意外成为 AI 代理的重要助力。
- 🛠️ **TanStack Intent**：将最佳实践以 skills 形式嵌入 npm 包，帮助代理理解 API 使用方式，而非仅依赖训练数据。
- 🤝 **合作伙伴生态**：CodeRabbit、Render、Netlify、Lovable、Cloudflare、Vercel、Railway、Clerk、WorkOS、Sentry、Prisma 等企业提供集成、资金与安全支持。
- 📚 **上手与迁移指引**：官方提供完整文档与迁移指南，作者建议直接让 AI 代理辅助新项目或迁移，可尝试提示“use TanStack Start”。
- 🙏 **致谢社区**：感谢所有维护者、贡献者、写教程、提复现、改文档的人，正是这些细碎贡献成就了 1.0 的打磨与质量。
- 🎯 **初心未变**：作者最初只想为自己打造更好的应用构建方式，最终在众多人参与下成长为更强大的开源项目。

---

### [获取失败](https://dub.sh/3jnUg5C)

**原文标题**: [Failed to retrieve](https://dub.sh/3jnUg5C)

无法总结：获取内容失败，状态码 429。

---

### [](https://github.com/reactjs/rfcs/pull/284)

**原文标题**: [RFC: Production React work counters by theKashey · Pull Request #284 · reactjs/rfcs · GitHub](https://github.com/reactjs/rfcs/pull/284)

该 RFC 提议为生产环境 React 增加工作计数器，以增强运行时可观测性与透明度；讨论中既有历史尝试，也有现有替代工具。
- 📌 reactjs/rfcs 仓库中的 RFC #284“Production React work counters”处于 Open 状态，作者 theKashey 希望将 1 个提交合并到 main。
- 🎯 目标是为 React 运行时定义可观测性并提升透明度，定位类似“React 的 CPU profiler”。
- 📊 希望统计有多少组件更新、多少组件提前 bail out，以及多少组件实际渲染。
- ⏱️ 还希望知道一次 commit 需要多少 tick，以及总共发生了多少次 commit。
- 🔄 同时追踪 setState、context 更新和 effects 的发生次数。
- 🛠️ 作者称已通过 patch-package 使用该能力一年，改进与事故都能通过数字清晰可见。
- ❓ 作者以 SRE 视角发问：我对自己的应用知道什么，又应该知道什么？
- 🧵 markerikson 回应称以往类似尝试失败，包括 React DevTools Performance Insight #22723 和 Tracing Hooks API 初始实现 #25763。
- 🧰 他补充 React DevTools 现在已有某种程序化 API：react-devtools-facade 的 profiler tools #36598。
- 📈 markerikson 还在 Replay.io 构建了复杂 React 渲染分析系统，并在 Replay MCP 中提供深度渲染分析。
- 👀 当前有 3 个 eyes 反应、2 位参与者，暂无审查者、指派者、标签、项目或里程碑。

---

### [](https://github.com/mobxjs/mobx/pull/4735)

**原文标题**: [MobX React plugin by kubk · Pull Request #4735 · mobxjs/mobx · GitHub](https://github.com/mobxjs/mobx/pull/4735)

本 PR 是 mobxjs/mobx 的草稿 PR #4735（MobX React plugin），由 kubk 发起，计划将 17 个提交从 mobx-react-plugin 分支合入 main，目标是简化 MobX 与 React 的配合，并让 React Compiler 能在同一项目中使用。

- 🧩 关联修复：该 PR 修复 #3874、#4594、#3836、#4734。
- ⚙️ 功能一：自动把组件包装为 observer，避免遗漏 observer 导致 bug，并支持排除文件/文件夹。
- ⚛️ 功能二：为组件添加 "use no memo"，让 MobX 接管重渲染，其余代码仍可由 React Compiler 优化/记忆化。
- ⏳ 功能三：把普通 async 方法编译为 MobX flow，修复 async/await 与 MobX action 的配合问题，避免 runInAction/action 嵌套和 TS 问题。
- 🧭 设计权衡：为兼容 React Compiler，插件需在 MobX 使用处关闭编译器 memo；替代方案 useValue 会牺牲自动依赖发现，且现有 MobX 应用需重写。
- 🚀 初步性能：MobX + 插件略快于 MobX + useValue + 编译器。
- 📦 发布状态：changeset 检测到将发布 mobx-react-plugin 的 major 版本。
- 🧪 测试与文档：新增单元、运行时、React Native、Vite、React Compiler、flow 等测试，并补充文档、示例（react-compiler-vite）和共享 Jest 设置。
- 🤖 Copilot 审查：给出“建议更改”，指出 6 个开放问题，包括不安全 flow 检测、遗漏 observer 别名、Vite transform 被丢弃、Next.js 配置无效等。
- 🚧 当前状态：仍为 WIP/草稿，作者正在精简依赖 React 内部实现、较脆弱的测试，并欢迎反馈（可能发起 Twitter 投票，@mweststrate）。

---

### [](https://github.com/vercel/next.js/pull/99628)

**原文标题**: [eslint-config-next: support ESLint 10 by jamiboym · Pull Request #99628 · vercel/next.js · GitHub](https://github.com/vercel/next.js/pull/99628)

该 PR #99628 已合并到 canary，使 `eslint-config-next` 支持 ESLint 10，同时继续兼容 ESLint 9，并且不提高 Next.js 的 Node.js 最低要求；通过升级依赖、修补旧插件/解析器和新增隔离安装测试，确保 lint 结果一致。

- 🎯 核心目标：让 `eslint-config-next` 在 ESLint 9 与 ESLint 10 下都能工作；ESLint 10 自身要求 Node `^20.19.0 || ^22.13.0 || >=24`，旧 Node 20 用户继续使用 ESLint 9。
- ⬆️ 依赖升级：`typescript-eslint` 升至 `^8.56.0`，`eslint-plugin-react-hooks` 升至 `^7.1.0`；后者移除已废弃的 `react-hooks/component-hook-factories` 规则。
- 🧩 Babel 解析器补丁：ESLint 10 调用 `scopeManager.addGlobals()`，而 Next.js 内置的 `@babel/eslint-parser` 7.24.6 缺少该方法；`eslint-config-next/parser` 仅在缺失时补上。
- 🛠️ 规则上下文补丁：ESLint 10 移除了 `getCwd()`、`getFilename()`、`getSourceCode()`、`parserOptions` 等成员；对 `eslint-plugin-react` 和 `eslint-plugin-import` 的规则原地修补，以保持插件对象身份。
- 🔍 导入解析器补丁：ESLint 10 下 npm 可能将 `eslint-plugin-import` 与 `eslint-import-resolver-typescript` 嵌套安装，导致解析器按名称查找失败；现改回按绝对路径加载，恢复 TypeScript 路径别名解析。
- ✅ 未改动项：`eslint-plugin-jsx-a11y` 6.10.2 和 `@next/eslint-plugin-next` 不使用被移除 API；`eslint-plugin-react-hooks` 会回退到替代实现。
- 📝 文档与构建：更新 ESLint 10 支持、Node.js 要求和 peer dependency 警告说明；添加 `@types/node` 开发依赖及 `"types": ["node"]`，因为 TypeScript 6 不再自动包含 `@types` 包。
- ⚠️ 已知限制：`eslint-plugin-react`、`eslint-plugin-import`、`eslint-plugin-jsx-a11y` 尚未在 peer 依赖中声明 ESLint 10；安装会出现 npm/pnpm peer 警告，严格 peer 依赖安装会失败，npm 项目直接依赖 `eslint-plugin-react` 时可能需 `--legacy-peer-deps` 或 `--force`。
- 🧪 验证方式：新增 `test/production/eslint-config-next` 测试，用 ESLint 9.37.0 和 10.11.0 安装打包配置，要求 JavaScript 与 TypeScript 项目的诊断一致；禁用补丁会导致崩溃、配置错误或导入解析失败，CI 在 Node 20.9.0 上运行。
- 🚫 迁移注意：不要用 overrides、`--legacy-peer-deps` 或 `.npmrc` 消除警告，也不要直接添加相关插件为依赖；暂不要启用 `import/order` 及部分 `react/jsx-*` 规则，它们会调用 ESLint 10 已移除的 `SourceCode` 方法并崩溃。
- 📦 依赖与结果：移除不再需要的 `@eslint/eslintrc`，保留 `js-yaml` override；`src/` lint 结果不变，`npm audit` 不变，审计、lint 和 build 均通过。
- 🔄 后续影响：ESLint 9 已于 2026-08-06 EOL；多个外部仓库引用该 PR 升级到 ESLint 10，并确认 `eslint-config-next 16.4.0` 提供兼容修补。

---

### [](https://github.com/jsx-eslint/eslint-plugin-react/pull/4022)

**原文标题**: [fix: complete ESLint 10 compatibility by plthomasva · Pull Request #4022 · jsx-eslint/eslint-plugin-react · GitHub](https://github.com/jsx-eslint/eslint-plugin-react/pull/4022)

该 PR #4022 为 `eslint-plugin-react` 完成 ESLint 10 兼容，整合了 #3979 等多位贡献者的工作，修复单元测试和 CI 矩阵问题，并包含临时依赖覆盖与破坏性变更，目前等待维护者审核合并。
- 🚀 使用 `eslintUtil.getFilename(context)` 替代已移除的 `context.getFilename()`，适配 ESLint 10 的 RuleContext API。
- 🧪 在 ESLint >= 10 的 `RuleTester` 中移除错误断言里的 `type:` 属性，并清理有效测试用例中的 `output` 和 `errors` 字段。
- 🧹 新增 `eslintUtil.isSpaceBetween`，替代被移除的 `sourceCode.isSpaceBetweenTokens`。
- 📄 为 JSDoc 增加回退逻辑，用 `sourceCode.getCommentsBefore(node)` 替代不可用的 `getJSDocComment`，修复 `@extends React.Component` 检测。
- 🌳 将已弃用或移除的旧 AST 节点迁移到现代 `sourceCode` 等价 API。
- 🔧 其他修复包括：canary 版 `@typescript-eslint/parser` 匹配、`no-undef` 的 JSX 注释覆盖、Windows 路径 `ENOENT` 处理、CI 中动态移除冲突依赖并排除不支持的 Node 版本。
- ⚠️ 破坏性变更：正式放弃对 Node 4 以及 ESLint 3/4 的支持。
- 📦 由于 `@babel/eslint-parser`、`eslint-plugin-import`、`@typescript-eslint/parser` 等尚未正式支持 ESLint 10，`package.json` 中临时添加了依赖 overrides 以通过 CI。
- 🔗 该 PR 关联并关闭 ESLint v10 兼容性问题 #3977 和 #3979，但仍需维护者审批。
- 💬 社区讨论指出 ESLint 9 已 EOL，而大量 Next.js 用户依赖该插件；ESLint TSC 曾推荐 `@eslint-react/eslint-plugin` 作为替代，Vercel 也在 `next@16.5.0-canary.3` 中尝试让现有插件兼容 ESLint 10。

---

### [即将发布的 Next.js 安全更新，针对上游漏洞 | Next.js](https://nextjs.org/blog/upcoming-nextjs-security-update-october-2026)

**原文标题**: [Upcoming Next.js Security Update for Upstream Vulnerabilities | Next.js](https://nextjs.org/blog/upcoming-nextjs-security-update-october-2026)

Next.js 计划于 2026 年 10 月 14 日（下周三）发布带外安全更新，修复上游依赖中的三个漏洞，其中两个为严重、一个为高危；其中两个修复因上游协调从 9 月安全版本推迟。更新将附带完整公告，说明影响范围、受影响版本和升级方法，建议补丁发布后尽快升级。Vercel 通过开源漏洞赏金计划与安全研究人员合作，相关问题可联系 security@vercel.com。

- 📅 2026 年 10 月 14 日（下周三）计划发布 Next.js 带外安全更新。
- 🛡️ 更新修复上游依赖中的三个漏洞：2 个严重、1 个高危。
- ⏳ 其中两个修复原定于 9 月安全版本，因上游协调而推迟。
- 📄 完整安全公告将与更新一同发布，涵盖影响、受影响版本和升级说明。
- ⬆️ 补丁可用后应尽快升级到已修复版本。
- 🐛 Vercel 开源漏洞赏金计划与安全研究人员合作，保护 Next.js 等开源框架。
- 📧 有关安全计划或漏洞管理的问题可发送至 security@vercel.com。
- ✍️ 文章作者为 Sebastian Silbermann、Josh Story、Karim Rahal。

---

### [](https://jimmyhmiller.com/what-does-the-react-compiler-even-do)

**原文标题**: [Can we Make React Faster using the React Compiler? — Jimmy Miller](https://jimmyhmiller.com/what-does-the-react-compiler-even-do)

文章记录了作者以学习为目的，用 React Compiler 做原型实验，验证它能让 React 更快，并结合内联、blocks、列表缓存、选择器等优化，在 13 个工作负载中取得最高约 51× 加速；但这些都只是概念验证，并非生产建议或 React 官方承诺。

- 🧪 作者写这篇文章是为了深入理解 React Compiler，并通过向他人解释来学习，而不是提出正式生产方案。
- 📊 基准图表显示：React Compiler 本身已能加速 React，叠加原型优化后效果更明显，13 个工作负载中最高达到 51.0×。
- 🔍 作者习惯从输出而不是内部实现入手，展示编译器会生成缓存槽、`_c`、`react.memo_cache_sentinel`、顶层函数等“难读但更优”的代码。
- ⚛️ React Compiler 能绕过 Hooks 的部分限制，在条件分支等场景生成更灵活的缓存代码，适合作为编译目标而非用户 API。
- 🧠 编译器先把代码转成 SSA，再通过多轮 pass 简化语言、推断信息、重写代码，并能识别 `user`、`canEdit`、`actions` 这类一起变化的值。
- 🧩 原型优化包括内联组件、blocks、列表 memoization、选择感知列表缓存、Context selectors、外部 store selectors 等。
- 📉 单独内联可能让性能变差：2,000 行逐个添加从 React Compiler 的 444.1 ms 变成 1038.1 ms。
- 🚀 内联配合 blocks 后反转变快：该基准降到 409.9 ms；内联 + blocks + 列表缓存达到 158.8 ms。
- 🎯 选择优化收益很大：2,000 行中做 200 次选择，从无编译器的 249.7 ms 降到选择感知列表缓存的 5.4 ms。
- 🏪 外部状态库也有优化空间：Zustand 场景中，通过 selector 分析，无编译器 474.6 ms 可降到 48.9 ms，原型整体约 9.5×。
- ⚖️ 作者反复强调：微基准上的胜利不等于生产默认优化，还需考虑内存、真实负载、生态影响和长期维护。
- 🌐 还有很多未探索方向，如 SSR、hydration、服务端到客户端通信、跨组件优化和更高级 lint。

---

### [className 被认为有害 | Matt Rothen](https://mattrothenberg.com/notes/classname-considered-harmful/)

**原文标题**: [className Considered Harmful | Matt Rothenberg](https://mattrothenberg.com/notes/classname-considered-harmful/)

设计系统组件普遍接受 `className`，短期看似灵活，长期却会造成大量覆盖、外观分裂、实现细节变成公共 API，并让变更管理变得困难。文章以假想产品中 6 个组件出现多种外观为例，比较不同设计系统的限制策略，并提出清点、审计、危险命名和 CI 检查等做法。

- 🧩 `className` 让组件内部 class 和元素都成为 API 的一部分；一旦调用方依赖，就受 Hyrum 定律影响。
- 🎨 设计 token 只能限制可选颜色和尺寸，不能阻止团队自由组合；同一个 `success` Badge 仍可被改成四种外观。
- 📊 示例中 6 个组件来自同一设计系统，却各自出现 4 到 8 种外观，覆盖包括按钮高度、输入框边框、下拉圆角、标签边框等。
- 📚 各库策略从严格到宽松：Polaris、Braid 主要通过 props 控制；Atlassian 推荐 lint 禁止 `className`，改用基于 token 的 `xcss`。
- ⚠️ Spectrum 和 React Spectrum 使用 `UNSAFE_className` 或 `styles`，仍可覆盖，但名称明确警示风险。
- 🧩 shadcn/ui 接受 `className` 且调用方类胜出，因为你拥有源码；React Aria 组件无样式，`className` 是主要样式方式，还可按组件状态返回不同类名。
- ⚖️ 核心权衡是灵活性放在库还是使用团队：取决于设计系统团队发布新 variant 的速度，以及使用团队能等待多久。
- 🔍 建议先做覆盖清单：收集所有传给设计系统组件的 `className`、`style` 和针对其标记的 CSS，按组件与 class 分组。
- 🚨 使用 `UNSAFE_` 或 `DANGEROUS_` 这类“吓人”命名，便于全局搜索；重复覆盖可能暴露缺失 variant 或未报告 bug。
- 🤖 通过 lint 和 CI 审计每个 PR 的新覆盖，并通知设计系统团队；可仅提示，也可阻塞，取决于现存覆盖规模。
- ✍️ 作者在 Cloudflare Kumo 中希望把所有组件的 `className` 重命名为 `DANGEROUS_className`；`Text` 已如此，grep 发现 `font-bold` 频繁后促成了 `bold` prop 和规则，但大规模重命名 PR 尚未提交。

---

### [](https://bra31k.dev/en/blog/same-bytes-17-percent-faster)

**原文标题**: [How we made a 9 MB WebAssembly module feel faster without removing a single byte — Sergey Patrakeev](https://bra31k.dev/en/blog/same-bytes-17-percent-faster)

Recraft Studio 的编辑器页面在不删减、不压缩任何字节的情况下，仅调整 9.2 MB Skia/CanvasKit WebAssembly 模块的加载时机，并用约 300 行代码，让画布首次渲染在 p50、p75、p90 上提升 15–19%。页面下载量几乎不变（16.75 MB → 16.71 MB），核心是让浏览器更早发现并请求最大文件。该改动通过真实对照实验验证，每组约 1.8 万用户，持续五天。

- 🧭 问题发现：自定义性能埋点显示，p75 用户看到画布完整渲染场景约需 8.5 秒，但此前无人投诉，说明监控本身揭示了性能盲区。
- 📦 最大瓶颈：9.2 MB 的 WASM 渲染引擎被放在最后请求，因为它的 import 藏在 lazy chunk 中，浏览器要先解析大量 JS 并等样式返回后才知道它存在。
- 🐢 旧加载链路：HTML/JS → 授权并连接实时存储 → 获取项目数据 → 基础样式 → 下载并初始化 CanvasKit → 字体 → 首帧渲染；而 WASM URL 本可在第零步就知道。
- ⚛️ React 树阻塞：EngineProvider、Content、Stage 中多个 Suspense/初始化 hook 串行等待，首个 hook 挂起后，后续字体请求和 WASM 初始化都只能排队。
- 🛠️ 修复一：在 `<head>` 中为 CanvasKit WASM 和默认字体加 `preload` 提示，让浏览器尽早开始下载关键资源。
- 🚀 修复二：把 `initSkia()` 提升到模块作用域，让 `initKit()` 和 `initFont()` 并行触发，不再相互等待；同时将字体初始化改成幂等的 memoized promise。
- ⏩ 修复三：尽早发出基础样式请求，不做 Suspense 阻塞，等 React 树走到对应位置时响应已在缓存或接近完成。
- 🔀 preload vs prefetch：编辑器页用 `preload`，项目列表页用 `prefetch`，避免列表页资源竞争；并考虑悬停项目卡片时预热编辑器 JS chunk。
- 📊 实验结果：Skia Loaded 约 -18%~-19%，Engine Initialized 约 -15%~-17%，Canvas Rendered 约 -17%~-18%，Images Loaded 约 -16%~-18%。
- 📉 代价与补救：首波加载更多资源导致 `loading-state-shown` 在 p75 约 +123 ms（+10%）；随后通过代码分割和悬停预取，使该指标 p50 239→36 ms、p75 631→193 ms、p90 1680→708 ms。
- 🧪 假设验证：四个假设中三个奏效；提前连接房间不是瓶颈，后来由同事换方式解决。
- 🚧 新瓶颈：现在 CanvasKit 已提前加载并等待编辑器代码，主要耗时转为认证、WebSocket 连接、握手和获取房间数据；最大资源已不在关键路径上。
- 💡 核心收获：指标能暴露无人讨论的性能问题；不删一个字节、不压缩资源，仅改变最大文件开始加载的时机，也能让相同数据量交付快约 17%。
- 🔮 后续内容：作者还优化了 WASM 模块体积，并计划在下一篇文章分享具体做法。

---

### [](https://julesblom.com/writing/react-visual-notation)

**原文标题**: [A visual notation for React's parent and owner trees | JulesBlom.com](https://julesblom.com/writing/react-visual-notation)

本文介绍 Jules Blom 提出的一种可视化记法，用于展示 React 的父级树与所有者树，将 React 组件表示为图表，从而提供仅靠代码难以呈现的结构化概览。文章发布于 2026 年 10 月 8 日。

- 👤 作者：Jules Blom
- 🧩 主题：面向 React 父级树与所有者树的可视化表示法
- 📊 形式：将 React 组件绘制成图示或图表
- 🌲 目的：展示组件之间的父级与所有者关系
- 🔍 价值：提供比单独阅读代码更清晰的结构性概览
- 🗓️ 发布时间：2026 年 10 月 8 日

---

### [使用 React Suspense 面板调试 Suspense - Certificates.dev](https://certificates.dev/blog/debugging-suspense-with-the-react-suspense-panel)

**原文标题**: [Debugging Suspense with the React Suspense Panel - Certificates.dev](https://certificates.dev/blog/debugging-suspense-with-the-react-suspense-panel)

本文以商店仪表盘为例，介绍如何使用 React Developer Tools 的 Suspense 面板定位 Suspense 边界、查看等待内容与揭示顺序，并修复统计卡片加载造成的布局偏移。  
- 🧭 Suspense 面板默认在 React Developer Tools 8.0 中启用，React 19.2+ 开发构建显示最详细。  
- 🧱 面板包含工具栏、迷你地图、时间线和检查器，可检查边界、等待原因、子节点与 fallback。  
- ⏱️ 时间线逐步重放页面揭示过程，帮助发现统计卡片出现时把底部快速操作区向下推。  
- 🔍 “Inspect Suspense Nodes” 可从页面内容直接选中最近的 Suspense 边界，找到负责 `<SalesStats />` 的边界。  
- ⏳ “Suspended by” 显示边界等待的 Promise；本例等待 `getSalesStats()` 约两秒，但无法解释为何慢。  
- 🧪 用检查器中的“Suspend the selected component”可强制显示 fallback，无需改代码或网络来对比骨架屏。  
- 🦴 原骨架屏只是固定高度的灰块，与真实统计卡片形状和尺寸不符，因此加载完成时发生跳动。  
- ✨ 改进后的骨架屏渲染四个真实标签，并用 `height: 1lh` 的占位行替代数值和变化，使尺寸与真实卡片一致。  
- ✅ 关键经验：时间线找布局偏移，Inspect 找边界，Suspended by 找等待数据，强制 fallback 对比骨架。  
- 📚 结论：Suspense 面板让加载序列可检查，但不能说明异步慢的根因；页面还列出其他开发者文章与认证资讯。

---

### [](https://sentry.io/resources/201-session-replays/?utm_source=thisweekinreact&utm_medium=paid-community&utm_campaign=replay-fy27q3-sessionreplayworkshop&utm_content=newsletter-react-link-register)

**原文标题**: [The session replays you want without the noise | Sentry](https://sentry.io/resources/201-session-replays/?utm_source=thisweekinreact&utm_medium=paid-community&utm_campaign=replay-fy27q3-sessionreplayworkshop&utm_content=newsletter-react-link-register)

本次工作坊聚焦于更精准地使用 Session Replay，减少无关噪音，并获取真正需要的会话回放。内容涵盖自定义 React Hooks、附带回放的用户反馈、过滤器与标签、采样设置及隐私配置，同时推荐了 Syntax 开发者播客。

- 🎯 工作坊主题：获取想要的会话回放，而不被噪音干扰
- 🎥 Session Replay 不只是错误旁边附带的视频
- ⚙️ 实操创建自定义 React Hooks
- 👥 精准捕获特定用户群、已知坏 URL 或刚上线流程的会话
- 📝 用户反馈：接入组件，让 Bug 报告自动附带回放
- 🔍 查找合适回放：过滤器、死点击、暴怒点击和自定义标签
- 📊 采样：两种采样率、缓冲模式的作用及推荐默认值
- 🔒 隐私：默认设置以及如何自定义
- 🎙️ 推荐收听 Syntax Podcast 开发者播客

---

### [v1.22.0 | React Aria](https://react-aria.adobe.com/releases/v1-22-0)

**原文标题**: [v1.22.0 | React Aria](https://react-aria.adobe.com/releases/v1-22-0)

React Aria 发布 v1.22.0（2026年10月8日），重点新增 Sheet 滑动叠加层组件，并加入 Turbopack 支持、虚拟键盘感知的叠加层定位及多项开发警告与修复。

- 🆕 新增 Sheet 组件：从视口边缘滑入的可滑动叠加层，基于原生浏览器滚动手势，适用于移动端 sheet、导航抽屉和通知横幅。
- ⚡ @react-aria/optimize-locales-plugin 新增 Turbopack 支持。
- ⌨️ 叠加层定位现支持虚拟键盘等交互式小组件。
- 🧰 常规修复：GlobalDOMAttributes 增加 suppressHydrationWarning 并可经 filterDOMProps 转发；修复 preventFocus 的 TypeError；开发环境跳过 Focusable/Pressable 可见性检查；无效 rgb()/rgba() 抛错；React Native 启用 useControlledState 早期 effect。
- 📚 Collections 开发时警告重复 collection keys。
- 🔽 ComboBox 在空响应后异步项到达时重新打开 popover。
- 📅 Date/Time：年份选择器包含最终约束年份；CLDR 不支持本地化值时使用默认 era。
- 📝 文档修复拼写错误。
- 🧾 Forms 增加开发警告，检测表单中无效焦点移动。
- 🔗 Link 的 LinkContext 支持 aria-current。
- 🪟 Popover 内部清除 Popover context。
- 📊 Table 修复 useGridCell 覆盖可聚焦子项（如单元格内 dialog 触发器）的焦点恢复。
- 🎨 Tailwind 文档补充 data 属性到 Tailwind 选择器的映射说明。
- 🏷️ TokenField 将 TokenFieldContext 作为值导出而非类型；修复编辑 token 后光标跳动。
- 🌳 Tree 修复 useTreeData 子树移动验证。
- 📦 发布包：@internationalized/number@3.6.9、@react-types/shared@3.37.0、@react-aria/optimize-locales-plugin@2.1.0、react-aria@3.53.0、react-aria-components@1.22.0、react-stately@3.51.0。
- 🙏 感谢所有贡献者。

---

### [](https://react-aria.adobe.com/blog/sheet)

**原文标题**: [Scrolling is All You Need: Building a Swipeable Sheet | React Aria](https://react-aria.adobe.com/blog/sheet)

React Aria 推出全新 Sheet 组件：一种从视口边缘滑入的覆盖层，支持滑动关闭，并具备手势同步动画、吸附点、堆叠、过度滚动内边距、软件键盘感知，以及多种位置和滑动方向。其核心实现基于原生 CSS 滚动吸附与视图时间线，构建在现有 Modal 组件之上，无需 JavaScript 触摸处理即可获得原生刷新率、惯性滚动和弹性物理。

- 📦 Sheet 是可从视口边缘滑入、可滑动关闭的覆盖层，支持 bottom、top、left、right、start、end、center 等位置。
- 🧭 支持多个滑动方向与 `preventDismissal`、`overscrollPadding` 等配置，适配不同交互场景。
- 🎞️ 使用原生 CSS 滚动吸附与 `view-timeline`，滑动手势脱离主线程运行，动画流畅且无需 JS 触摸处理。
- 📐 视口设置通过双倍视口高度的可滚动覆盖层、隐藏滚动条和滚动吸附点，模拟 Sheet 打开与关闭。
- 👀 关闭时 `scrollTop = 0`，Sheet 位于屏幕外；打开时平滑滚动到最大位置；完全滑出后由 `IntersectionObserver` 卸载。
- 📍 `snapPoints` 通过不可见的 1px 标记与 `scroll-margin-top: 100dvh` 实现，让 Sheet 可停在部分可见高度。
- 🔒 部分可见时内部内容 `overflow: hidden`，用户可在任意位置滑动展开；完全打开后内容才可滚动。
- 🔗 `overscroll-behavior: auto` 允许滚动链：内容顶部继续下滑可关闭 Sheet，已滚动内容时则正常滚动内容。
- 🚫 `preventDismissal` 可禁止滑动关闭，但仍允许在吸附点之间滑动，并通过调整 stage 保持原生回弹。
- 🧱 Sheet 可堆叠，使用 `stackAnimation`、`timeline-scope` 与 `animation-composition: accumulate` 表现堆叠深度。
- ⌨️ 针对 iOS 软件键盘，使用动态视口高度补偿底部内边距，并改进 `usePreventScroll` 减少布局偏移。
- 🧾 总结：现代 CSS 的滚动吸附、视图时间线、过度滚动行为和动态视口单位，使原生滑动 Sheet 与流畅动画成为可能。
- 🔗 可查看 React Aria Sheet 组件，了解如何在自己的应用或组件库中使用。

---

### [](https://github.com/vercel/satori/releases)

**原文标题**: [Releases · vercel/satori · GitHub](https://github.com/vercel/satori/releases)

该页面是 vercel/satori 的 GitHub Releases 记录，显示 2026-10-13 连续发布 0.53.0 至 0.56.1 共 10 个版本；最新版为 0.56.1，更新重点集中在 CSS/浏览器兼容性、布局、字体支持与样式解析修复。

- 📅 所有列出的版本均在 2026-10-13 发布，最新版本为 0.56.1。
- 🔐 发布均由 github-actions 完成，提交带 GitHub 验证签名，GPG key ID 为 B5690EEEBB952194。
- 🐛 0.56.1：修复样式表中以函数结尾的 important 值解析。
- ✨ 0.56.0：支持逻辑属性、mask 简写/mask-clip/mask-composite；修复行内元素文本平衡、继承 text-wrap、hidden 元素与隐藏输入、SVG 属性中的 CSS 变量解析。
- 🖼️ 0.55.5：允许样式覆盖图片的 size 属性。
- 📐 0.55.4：让部分元素按浏览器方式布局（原文标签名缺失）。
- 🌳 0.55.3：在样式表中接受 shadow tree 的伪类。
- 🎨 0.55.2：像浏览器一样解析 CSS 变量。
- 🔤 0.55.1：从 inflateSync 返回值读取 WOFF 表。
- 🧩 0.55.0：支持 WOFF2 字体；无需 Node Buffer 即可解码 layout.wasm。
- 🧹 0.54.0：像浏览器一样丢弃样式表中的无效声明。
- 🏷️ 0.53.0：支持 ::before 和 ::after 伪元素。
- 📊 仓库导航显示 103 个 Issues、51 个 Pull Requests、1 个安全与质量项目。

---

### [发布 v0.3.0 · storybookjs/vitest-plugin-rsc · GitHub](https://github.com/storybookjs/vitest-plugin-rsc/releases/tag/v0.3.0)

**原文标题**: [Release v0.3.0 · storybookjs/vitest-plugin-rsc · GitHub](https://github.com/storybookjs/vitest-plugin-rsc/releases/tag/v0.3.0)

vitest-plugin-rsc 发布 v0.3.0（2026-10-08），这是一次包含破坏性变更的更新：Next.js 支持改为在浏览器中运行 Next 自己的服务器和路由器，因此升级时需要调整要求、设置、MSW、路由、导航、rerender、screen 和导入方式；同时新增 renderServer 的 proxy 与 layouts 标志，并修复相关一致性问题。  

- ⚠️ **破坏性变更**：从 0.2.5 升级时，Next.js 支持现在会在浏览器中、测试旁边运行 Next 自己的服务器和路由器。  
- 📦 **版本信息**：v0.3.0 是最新版本，发布于 2026-10-08，对应提交 a9e6b60。  
- 🧩 **环境要求**：需要 Next.js 16.4 或更高版本，并安装与 next 同版本的 @next/routing；最低要求 Vitest 5.0.3 和 Vite 8。  
- 🛠️ **设置变更**：移除 initialize() 和自定义的 afterEach(cleanup)；vitestPluginNext() 会添加 setup 文件，在每个测试前后调用 cleanup()。  
- 🌐 **MSW 调整**：移除 nextRscRequestHandlers 和 nextRscRequestsViaMsw；Server Actions 直接调用 Next 服务器，MSW 仍可用于应用自身的出站请求。  
- 🧭 **route 参数**：renderServer(<Page />, { url, route }) 不再接受 route；插件已知应用路由，仅用 url 即可获取 params。  
- ➡️ **导航断言**：移除 expectToHaveBeenNavigatedTo()；导航会打开应用真实页面，应改为断言屏幕内容或 window.location。  
- 🔁 **rerender 移除**：结果中不再提供 rerender，需要重新调用 renderServer。  
- 🖥️ **screen 限制**：打开的页面拥有自己的 <body>，Testing Library 的 screen 无法看到；应使用 vitest/browser 的 page，或 within(document.body)。  
- 📥 **导出与导入**：vitest-plugin-rsc/nextjs/testing-library 导出 renderServer、handleRequest 和 cleanup；旧内部入口不再导出，node:os 也不再被 shim，需要时添加 vite-plugin-node-polyfills。  
- ✨ **新增功能**：renderServer 新增 proxy 和 layouts 标志；支持在 Vitest Browser Mode 中运行 Next.js App Router 应用。  
- 🐛 **问题修复**：按 fetch 的方式发送请求；修复 Next.js 服务器的三个一致性错误。

---

### [v1.9.0 · 基础 UI](https://base-ui.com/react/overview/releases/v1-9-0)

**原文标题**: [v1.9.0 · Base UI](https://base-ui.com/react/overview/releases/v1-9-0)

v1.9.0（2026-10-9）是一次覆盖全组件的维护与功能更新，重点包括通用类型导出与焦点、动画、挂载修复，Menu 新增筛选预览，Drawer 强化手势与键盘处理，以及 Combobox、Select、Menu 等大列表性能优化。

- 🧩 通用修复：导出 `CssVariables` 和 `DataAttributes` 类型；修复聚焦字段状态、动画等待保留已分离元素、Strict Mode 下项目注册同步、非活动触发器开闭时重复渲染。
- 📂 Accordion / Collapsible：修复 Trigger 的 `data-value`、`data-index` 与原生 `disabled`；`hiddenUntilFound` 面板在 `beforematch` 时同步展开；修复移除面板后的关闭与重开动画。
- 🪟 Dialog / Alert Dialog：程序化打开的弹窗不再错误关联未打开它的触发器；关闭 Shadow Root 中的嵌套对话框时保持父级打开。
- 🔍 输入类组件（Autocomplete / Combobox / Select）：修复异步 `autoHighlight`、Shadow DOM 标签聚焦、typeahead 重置；`onItemHighlighted` 传递原始事件；可通过 `preventUnmountOnClose()` 控制自动卸载；支持只读数组多值。
- ☑️ 选择控件（Checkbox / Radio Group / Switch）：优先使用 `aria-label`；修复 Radio Group 方向键重聚焦选择、`inputRef` 转发与清理。
- 🖱️ Drawer：修复滑动释放速度、120Hz 输入、虚拟键盘滚动与间距、iOS 焦点滚动；改进 CloseWatcher、`swipe-ignore` 的 x/y 选项、SVG 拖动、触摸开销与键盘取消时的点击保留。
- 🏷️ Field：避免非受控 `Field.Control` 的 `defaultValue` 变更警告；修复 Shadow DOM 标签聚焦。
- 📋 Menu：新增 `Menu.FilterProvider`、`Menu.Input` 与 `onItemHighlighted` 的筛选预览；修复嵌套菜单、事件清理、子菜单订阅释放、打开变更原生事件、守卫焦点、重复触发切换、typeahead、过渡状态与大列表性能。
- 🔢 Number Field / OTP Field：`ScrubArea` 的 `onClick` 每次点击只触发一次；修复 Safari IME 组合输入导致 OTP 槽位溢出。
- 🪶 Popover / Preview Card / Tooltip：修复唯一可聚焦触发器的焦点守卫循环、分离触发器悬停动画；触发器关闭时重挂载不启动视口过渡；重开保留弹窗过渡状态。
- 🎚️ Scroll Area / Slider：移除展示性 viewport 角色；修复 Shadow DOM 标签聚焦；`touchcancel` / `pointercancel` 结束拖动；触摸轨道点击触发 `onValueCommitted`；指针交互保留单元素数组值。
- 🗂️ Tabs / Toast：修复函数值选择标签页；Toast 在重叠交互期间保持计时器暂停。
- 🚀 性能与一致性：多个组件提升大列表挂载性能、合并 item store 订阅、共享 item indicator 实现、同步根 props。

---

### [发布 styled-components@6.6.0 · styled-components/styled-components · GitHub](https://github.com/styled-components/styled-components/releases/tag/styled-components%406.6.0)

**原文标题**: [Release styled-components@6.6.0 · styled-components/styled-components · GitHub](https://github.com/styled-components/styled-components/releases/tag/styled-components%406.6.0)

styled-components 发布 6.6.0，新增用于显式类型导出的 `StyledComponent<Target, Props>` 公共类型，并集中修复 `attrs`、RSC/SSR 与 Suspense 流式渲染、React Native 注释、类型声明兼容性等问题，同时加入服务端与浏览器版本不一致的开发警告。

- 🧩 新增 `StyledComponent<Target, Props>` 类型：用于显式标注导出的 styled 组件，适合 `isolatedDeclarations` 和生成声明文件的项目；从 web/native 入口导出，精确对应 `styled(Target)<Props>`，不丢失 hoisted statics。
- 🛠️ 修复 `attrs` 默认值：当 prop 显式为 `undefined` 时，`attrs` 返回的键现在始终优先；未覆盖的显式 `undefined` 会转发给包裹组件以启用其默认值，DOM 标签仍丢弃；若要用 `undefined` 清除 `attrs` 默认值，应改用函数形式检查属性是否存在。
- ⚡ 显式类型注解可加速类型检查，尤其大量 `styled.div/span/button` 和多态组件包装器；运行时与类型行为不变。
- 🖥️ Edge runtime 服务端渲染 styled-components 现在会明确报错并建议改用 Node.js runtime，而不是模糊崩溃。
- 🧵 修复 `createGlobalStyle` 在 RSC/Suspense/客户端导航中消失：每个服务端渲染实例携带自己的样式，避免 fallback 替换或 layout/page 重复渲染时丢失。
- 🌊 修复从 Suspense 边界揭示的服务端组件样式消失（含流式 Next.js 与 `cacheComponents`）：每个实例自带 inline `<style>`；React 19 数据去重，重复列表很大时开发警告建议从单一父元素重构。
- 🪝 修复样式插值中调用 React hook 或读取外部值导致的“Rendered fewer hooks than expected”崩溃和 stale style，回归自 6.4.0，影响 MUI X DataGrid；插值现在每次渲染运行，昂贵时可配合 `React.memo`。
- ✏️ 修复 `useTheme` 错误示例拼写，以及 React Native 样式中 `//` 行注释解析；URL 原始值不受影响。
- 📦 修复类型声明兼容性：内置 `stylis` 类型，兼容 `@types/react` 16/17/18.2.6–18.2.11 及缺少 `@types/react-dom` 的项目；`ServerStyleSheet` 流式 API 行为不变。
- 🚨 新增开发警告：服务端与浏览器 styled-components 版本不一致会导致类名/hydration 问题，提示用 `npm ls styled-components` 排查；微前端可忽略，生产构建中移除。

---

### [发布版本 7.90.0 · react-hook-form/react-hook-form · GitHub](https://github.com/react-hook-form/react-hook-form/releases/tag/v7.90.0)

**原文标题**: [Release Version 7.90.0 · react-hook-form/react-hook-form · GitHub](https://github.com/react-hook-form/react-hook-form/releases/tag/v7.90.0)

react-hook-form 发布最新版本 v7.90.0，包含 17 个提交，重点修复表单状态、字段注册、校验与订阅相关问题，同时带来性能优化、重构、测试补充和依赖更新。

- 🚀 v7.90.0 由 bluebill1049 发布，属于最新版本，主要围绕稳定性与性能改进。
- 🐞 修复 useForm 相关问题：Object.prototype 属性命名字段被误标为 touched、setValue 行为、重新渲染时保留已移除选项等。
- 🐞 修复 reset()、Controller、watch、useWatch 等钩子问题，包括 blur 校验、过期 shouldUnregister、观察对象更新、默认值优先级。
- 🐞 修复 cloneObject 对稀疏数组长度、null 原型对象的处理，以及 hasOwnProperty 字段的脏值提取。
- 🐞 修复 useFieldArray 的重复索引 remove、父数组重排时反注册、索引边界与无操作行为。
- 🐞 修复表单就绪前输入值丢失、错误对象引用不更新、setError/clearErrors 不产生新引用等问题。
- ⚡ 性能优化：改进脏字段检查、订阅值处理、watch API、命名作用域订阅、取消订阅状态跟踪和通知合并。
- 🧹 重构：减小打包体积，清理测试并修复警告。
- 🧪 测试：增加 useFieldArray 索引边界、no-op 行为，以及 JSON stringify/parse 边缘用例覆盖。
- 📦 依赖更新：fast-uri 从 3.1.2 升至 3.1.8，joi 从 18.2.5 升至 18.2.6。
- ❤️ 感谢 @charan-rathore、@zigzagdev、@AdzerKI、@huytdps13400、@dfedoryshchev 等贡献者。

---

### [](https://astryx.atmeta.com/blog/astryx-v0-7-0)

**原文标题**: [Astryx v0.7.0: better mobile experiences, clearer inputs, and stronger foundations · Astryx](https://astryx.atmeta.com/blog/astryx-v0-7-0)

overview summary
- 🚀 Astryx v0.7.0 发布，汇总 v0.6.1 至 v0.6.8 的更新，重点提升表单、移动端、菜单、Markdown、表格、主题与 CLI 的可预测性。
- 🧾 表单与输入：样式、ID 和事件处理器现在作用于真实控件；可搜索选择器可通过 hasSearch/hasCreate 创建缺失选项，onChange 返回 `{type:'create', query}`。
- 📱 移动与触控：手机正文 16px，列表支持滑动操作，日期/时间输入可选用底部弹层、弹窗或系统选择器。
- 🧭 菜单与浮层：菜单可容纳头部/底部控件，触屏子菜单会钻取并带返回行；Escape 优先关闭顶层，Toast 可显示在对话框上方，BottomSheet 默认增加内容内边距。
- 📊 数据展示：表格展开行与首列对齐、条纹稳定，列宽调整在悬停时显示边界并保持拖动后的宽度。
- 📝 Markdown：支持软换行、frontmatter 解析为数据、文本转链接、自定义代码围栏组件、标题链接复制、源码行映射和自定义数学渲染。
- 🎨 主题与视觉：数据颜色统一到 StyleX dataVars；Kbd 达到 WCAG AA；Slider 标记颜色随填充变化；图标默认跟随 Button 尺寸。
- ♿ 无障碍与本地化：布局间距随浏览器字体大小缩放；焦点提示匹配最后一次输入；Banner 默认静默，异步结果通过 useAnnounce() 显式播报。
- 🧩 CLI 与集成：其他库可通过 Astryx CLI 贡献组件、文档、模板、升级脚本、编码指南和源主题，并支持 add/verify component。
- ⬆️ 升级到 0.7.0：需将 Core、CLI、Build、主题等稳定包固定到 0.7.0，运行 `npx @astryxdesign/cli upgrade --from "$OLD_VERSION" --apply --path .`。
- ⚠️ 最大风险：过去被忽略的 BaseProps 现在会传到 DOM，涉及 Layout、MetadataList、NavHeadingMenuItem、TopNavMegaMenuItem，需审计依赖“无效果”的调用点。
- ✍️ 4 项需手动修改：Banner 播报、忽略 props 审计、完整图标注册表添加 upload、独立空操作过滤器不再打开即保存。
- 🛠️ 10 项 CLI/脚本破坏性变更：theme add 改为 theme eject、无效输入报错、冲突选项拒绝、layout 命令组移除、Astryx 前缀 agent 变量移除等。
- 👀 4 项视觉/Token 变更：reset.css 覆盖伪元素与搜索框、四个主题手机排版从 16px 起、Core 与 Matcha/Y2K 间距改用 rem。
- 🤖 8 项由 astryx upgrade 处理/检查：数据颜色迁移到 StyleX、输入控件样式目标变更、BottomSheet 默认内边距、emptySearchResultsText 重命名等。
- 🙌 感谢 v0.6.1–v0.7.0 的贡献者，完整逐包说明见 Astryx v0.7.0 发布页。

---

### [发布 vinext@1.1.0 · cloudflare/vinext · GitHub](https://github.com/cloudflare/vinext/releases/tag/vinext%401.1.0)

**原文标题**: [Release vinext@1.1.0 · cloudflare/vinext · GitHub](https://github.com/cloudflare/vinext/releases/tag/vinext%401.1.0)

Cloudflare vinext 发布 vinext@1.1.0，自上一版本以来包含 107 个提交，重点新增预渲染特殊错误状态处理，并集中修复 App Router、缓存、服务端、字体、图片、中间件、Cloudflare、开发体验与 Use Cache 等问题，同时包含性能优化。

- 🚀 发布 `vinext@1.1.0`，时间为 08 Oct 23:04，自该版本以来 main 分支有 107 个提交。
- ✅ 发布提交已在 GitHub 上签名并通过验证，GPG key ID 为 `B5690EEEBB952194`。
- ✨ 新功能：Prerender 支持写入页面的特殊错误，使其携带状态码逃逸 shell（#3716）。
- 🧭 App Router 修复：编码静态页优先于动态兄弟页、预取布局重定向受 `cacheLife` 限制、跟随预取 `Link` 导航的 `redirect()`。
- 🔐 App Router 修复：授权拦截源作为直接请求、通过代理重写解析拦截源、恢复流式 metadata 与 `__next_f` 镜像。
- 🧩 App Router 修复：生成 metadata 放入 `<head>`、Suspense 特殊错误按 200 流式返回、RSC-first ISR 使用真实状态且不缓存未匹配 404。
- ♻️ App Router 修复：保留乐观 shell 提交后的浅历史写入、将特殊错误渲染存入 ISR 缓存、停止自重定向页面重复获取、仅由渲染决定页面是否动态。
- ⚡ 缓存修复：同步哈希 `use cache` 参数键、使用 Flight 参数作为缓存身份与重放、支持类作为缓存适配器默认导出并拒绝不可调用导出。
- 🖥️ 服务端修复：生产服务器压缩 RSC 响应、将客户端断开传播到请求信号、像 Next.js 一样重定向重复斜杠和反斜杠。
- 🛠️ 其他修复：Pages Router 编码动态渲染隔离 ISR、字体缓存路径处理、`/_next/image` 返回 MISS 头、Headers 异步上下文泄漏、Middleware matcher 安全分析。
- ☁️ Cloudflare 与其他修复：整体渲染 Response Store 和 Workers Cache 再生/预热、Dev 请求体取消时保持存活、Use Cache 后台再生 stale/过期条目、传递真实 `defaultConfig`、CSS `customMedia` 推导、Worker 请求阶段保留原始 `req.url`。
- 🚀 性能优化：App Router 在 RSC 渲染前停止探测页面（#3699）。
- 👥 贡献者包括 `@Adnan-Husayn`、`@AhmedElBanna80`、`@james-elicx`、`@mhsnook`、`@SisyphusZheng`、`@sppidy`、`@Tiscs` 等 7 人。
- 📦 该发布附带 2 个资产，页面在加载标签和资产时出现错误提示，需重新加载。

---

### [Remocn Studio — 发布视频，由你的 AI](https://remocn.studio/)

**原文标题**: [Remocn Studio — launch videos, built by your AI agent](https://remocn.studio/)

Remocn Studio 是一款 macOS 桌面应用，让已有 AI 编程代理（Claude Code、Codex、GitHub Copilot、Grok）把用户描述的视频需求生成真实 Remotion 代码项目。它提供实时预览、直接指点修改、素材库与多平台 mp4 导出，且完全免费、无锁定、无需额外 API 费用，项目归用户所有。

- 🎬 代理制作视频：用户描述想要的视频，Remocn Studio 按动效设计规则规划、构建并检查修复。
- 🪄 三步流程：创建项目、向代理描述需求、实时预览并在满意时导出 mp4。
- 🏭 工作室级流程：分析、品牌、脚本、场景、组装、审核，用户只需批准结果而非全程盯守。
- 🎞️ 内置动效知识：涵盖缓动、节奏、字体动画等技能，代理直接知道什么好看。
- 🖱️ 直接指导而非描述：点击视频中的元素说修改点，无需找代码或描述“从上往下第三个文本框”。
- 📸 展示而非截图：在画面上拖框即可送入聊天，无需截图工具或拖拽文件。
- 📚 一句话调用素材：片段、图片、音频存入素材库后，说“使用片头片段”即可自动接入。
- 💻 真实代码且属于你：每个视频都是磁盘上的 Remotion 项目，可编辑、提交 git、自由带走。
- ♻️ 动画组件可复用：保存可用动画代码为组件，跨项目复用，并预装 Remocn 组件集。
- 📐 适配所有平台：TikTok、YouTube、Instagram，竖屏、方形、宽屏一键导出。
- 🔑 无需 API key 或新账单：运行在已有编码代理订阅上，登录一次即可。
- ⚖️ 第三种选择：不是不可编辑的 AI 生成像素，也不是云端模板，而是精确品牌、确定性渲染、可复用代码。
- 💰 完全免费：macOS 桌面应用全部功能免费，无试用、无卡、无账号，只需已有代理订阅。
- 🧑‍💻 无需会编码：通过对话、指点、批准即可完成；代码仍保留给想深入编辑的人。
- 🚀 现已推出 macOS 版：安装后用已有编码代理登录，第一个视频只需一个提示。

---

### [Next.js](https://www.youtube.com/watch?v=paQbukUXE8w)

**原文标题**: [Next.js 16.4 Is Built for Agents (Here’s Why) - YouTube](https://www.youtube.com/watch?v=paQbukUXE8w)

这是 YouTube 网站页脚/底部导航内容，主要包含平台介绍、联系与合作入口、创作者与开发者资源、法律政策链接、功能说明及版权信息。

- ℹ️ 关于：YouTube 平台介绍入口
- 📰 新闻：媒体与新闻信息
- ©️ 版权：版权相关说明
- 📞 联系我们：提供联系渠道
- 🎬 创作者：面向内容创作者的资源
- 📢 广告：广告投放与合作入口
- 👨‍💻 开发者：面向开发者的资源
- 📜 条款：服务条款与使用规则
- 🔒 隐私：隐私政策说明
- 🛡️ 政策与安全：平台政策及安全信息
- ⚙️ YouTube 运作方式：平台机制说明
- 🧪 测试新功能：新功能测试入口
- © 2026 Google LLC：版权归属声明

---

### [](https://share.transistor.fm/s/0c8a4fc2)

**原文标题**: [This Month in React | TMiR 2026-09: React 19.3; a eulogy to software engineering?](https://share.transistor.fm/s/0c8a4fc2)

这是一段播客节目页面或播放器界面的功能菜单与收听平台列表，主要涵盖预告/附加内容、订阅、分享、下载、转录、章节播放及多平台分发入口。
- 🎬 包含 Trailer（预告）与 Bonus（附加内容）入口。
- 🔔 提供 Subscribe（订阅）和 More episodes（更多剧集）。
- 📤 支持 Share（分享）、复制到剪贴板及 Embed（嵌入）。
- ⬇️ 设有 Download（下载）与 More Info（更多信息）。
- 📝 提供 Full Transcript（完整转录）、Chapters（章节）与 View the website（访问网站）。
- ▶️ 可通过 Start at 设置从指定位置开始播放。
- 🌐 汇集 Apple Podcasts、Spotify、YouTube、Amazon Music、SoundCloud、Deezer 等大量播客平台。
- 🔁 部分平台如 Goodpods、Anghami、TuneIn、SoundCloud 出现重复，可能为界面重复项。

---

### [面向编码智能体的 Wallaby](https://wallabyjs.com/blog/wallaby-for-coding-agents.html?referrer=ThisWeekInReactOct26)

**原文标题**: [Wallaby for coding agents](https://wallabyjs.com/blog/wallaby-for-coding-agents.html?referrer=ThisWeekInReactOct26)

Wallaby 为编码代理提供实时测试结果、覆盖率、执行路径和运行时值，帮助编写与强化能真正捕获回归的测试；支持多种代理和运行环境，beta 期间免费。

- 🧪 编码代理可能写出“通过但漏 bug”的测试，原因包括弱断言、漏边缘案例或检查与实现雷同。
- ⚙️ 通过技能集成：在终端运行 `npx skills add wallabyjs/skills`，并在项目中选择编码代理。
- ✍️ `/wallaby write` 为改动编写或更新测试，并检查结果、覆盖率和断言。
- 🛠️ `/wallaby improve` 强化现有测试、补齐缺失场景、移除重复检查；可指定文件、目录或分支改动。
- 🔄 Wallaby 在后台运行现有 JavaScript、TypeScript 和 Python 测试，并随文件变化保持最新。
- 🔍 它提供哪些分支被触达、运行时值是什么等证据，便于代理对比预期与实际。
- 🧭 不同于传统测试运行器的大段终端输出，Wallaby 可按需打开失败、覆盖率、Trace 或运行时值，减少 token。
- 🧵 一个测试会话贯穿任务：从 exclusive mode 的选定文件扩展到 project mode 全项目验证，无需重启。
- 🧱 Covering Tests 显示覆盖某行或表达式的测试及其状态、位置、耗时；WCOV 标记完全、部分或未覆盖。
- 🧬 Test Execution Trace 按执行顺序列出源码行，跨文件展示调用路径，替代堆栈跟踪与反复读文件。
- 📊 文件指标包括覆盖率、测试数量与耗时、大小、复杂度、变更风险，帮助定位弱覆盖、慢测试和需补测处。
- 🔎 可无需改代码检查表达式或变量，在到达该行的每个测试上下文中求值，并绑定到具体测试。
- 🧰 不绑定编辑器，支持 Claude Code、Codex、GitHub Copilot、Cursor、Windsurf、OpenCode、Pi 等；可本地、编辑器、Standalone、容器/DevContainer、云或远程运行。
- 🆓 Beta 免费：终端运行 `npx --package @wallabyjs/cli wallaby access` 激活本地 CLI；容器和云代理需 `WALLABY_CLI_TOKEN`。
- 💬 已有授权编辑器扩展可直接使用 skills；CLI 激活不启动编辑器试用；反馈可发至 hello@wallabyjs.com。

---

### [](https://wallabyjs.com/?referrer=ThisWeekInReactOct26)

**原文标题**: [Wallaby - AI-Ready Test Runner with Instant Feedback in Your Editor](https://wallabyjs.com/?referrer=ThisWeekInReactOct26)

Wallaby.js 是一款面向 JavaScript/TypeScript 的即时测试运行器，可在你编写代码时实时运行测试，并将结果直接流式显示在代码旁；它还能为 AI 工具提供运行时上下文，帮助更快编写和修复代码。

- ⚡ 边写边测：JavaScript/TypeScript 测试随输入实时运行，结果即时显示在编辑器代码旁。
- 🤖 AI 就绪：为 AI 代理提供测试结果、运行时值、执行路径、覆盖率和依赖关系，支持 Copilot Agent、Codex、Claude Code、Cursor、Windsurf 等。
- 🐞 编辑器内智能调试：时间旅行调试、值浏览器和实时覆盖率帮助快速定位问题，无需打断心流。
- 🎯 极致高效：只计算并运行受代码变更影响的最少测试，常只需运行单个测试，速度远超普通 watch 模式。
- 🔌 无锁定：作为现有测试/UI 框架和 IDE 的插件，不绑定供应商、API 或框架，必要时仍可脱离 Wallaby 运行测试。
- 🛠️ 灵活组合：可选择 VS Code、React、Jest 等，获得更快测试、更高效调试和更实时的细粒度结果。
- ⏳ 时间旅行调试器：可前后移动执行，查看运行时值，编辑并继续，支持步入、步过和步出代码。
- 🚀 最快测试执行：未保存更改也会立即运行，必要时并行执行并实时流式输出，大型项目也能近乎即时反馈。
- 📊 实时洞察：运行时值、console.log 结果、内联错误报告和内联代码覆盖率直接显示在代码旁。
- 🧪 选择性测试运行：Smart Start 和 Exclusive Test Run 只运行当前正在处理的测试文件，工作流更高效。
- 🔍 深度对象检查：复杂数据结构以可展开树状视图显示，并支持交互式运行时值图，便于探索深层数据。
- 📋 交互式测试输出：失败测试、错误、diff/snapshot、错误堆栈和日志集中展示，超链接可跳转到对应文件。
- 🧭 Test Story Viewer：在单一逻辑视图中查看测试执行轨迹，无需在多个函数或文件间跳转。
- 📈 性能分析与快照管理：Test Profiler 可记录 CPU 使用情况；支持 Jest 快照更新和并排 diff 查看。
- 🗂️ Practical Test Insights：侧边视图总览项目测试与代码覆盖率，可按名称、时长、通过/失败和覆盖率排序过滤。
- 💰 ROI 估算：仅使用基础功能，预计编码效率提高约 10.84%，每年节省约 2396 美元。
- 🏢 广泛采用：10,000+ 家公司使用，包括多家财富 500 强；用户好评集中在 TDD、覆盖率、重构和开发体验提升。
- 🆓 可免费试用：提供试用；用户消息中还提到 OSS 项目可申请免费许可。

---

### [](https://posthog.com/blog/10k-prs-a-month?utm_source=twir&utm_campaign=oct14)

**原文标题**: [10,000 PRs a month is easy: How devex is evolving at PostHog - PostHog](https://posthog.com/blog/10k-prs-a-month?utm_source=twir&utm_campaign=oct14)

PostHog 的开发者体验正围绕“每月 1 万 PR 很轻松”快速演进：在工程人数仅增加 10% 的情况下，PR 量从 1 月的 1,441 增至 6 月的 4,725，并可能最早在 9 月达到 10,000；增长主要来自 AI 代理、内部工具、云端开发机、CI 优化和代理审查，同时通过测试、指标和稳定性监控控制风险。

- 🚀 **PR 量激增**：6 个月内从 1 月 1,441 个 PR 增至 6 月 4,725 个，工程人数只增加 10%，北极星目标是“每月 1 万 PR 很轻松”。
- 🎯 **目标不是 PR 数量本身**：更多 PR 来自优秀人才与代理自动化；真正目标是让本地开发、CI 和验证更快更好。
- 🤖 **AI 使用加速**：没有自上而下的 token 预算，强调信任与反馈；代理打开的 monorepo PR 从约 20% 升至 70%。
- 🔁 **自驱动循环**：self-driving 目前约占 4% 但增长很快；代理循环负责保持 trunk 更新、CI 通过、处理评审反馈。
- 🧰 **工程师自建工具**：如 review、qa-swarm、babysit-prs 等技能和 PR 管理工具；有人同时开约 40 个 PR，约 60% token 花费用于自动化 CI 和评审杂务。
- ☁️ **摆脱本地机器**：技术栈沉重，开始构建云端开发机；可通过技能提示启动 dev box、运行 PR 并录制测试视频。
- ⚙️ **内部 CLI hogli**：把 CI 检查下推到本地开发，帮助代理更好测试代码，并快速向 devex 团队反馈问题。
- 🏗️ **CI 瓶颈**：PR 量每月增 50% 像给火灾浇汽油；Depot 支撑 CI，2026 年 6 月用了 21,643,653 分钟 CI 时间，相当于 41 年。
- 🧪 **优化 CI**：隔离 flaky 测试、基于 AST 更选择性跑测试、使用 merge queue、预迁移数据库 schema 将后端 CI 从约 23 分钟降至约 15 分钟。
- 📊 **工程分析**：将 GitHub 数据流入 PostHog，用 PostHog AI 查看哪些 workflow 最贵、最慢、最常失败，从而针对性优化。
- ✅ **验证与安全**：UI、图表、权限、过滤器更重快速修复；核心数据服务不能坏，因此依赖约 25 万个 Python 后端测试等自动化验证。
- 📏 **质量指标**：PR 行数 p50 +20%、p75 +91%、p90 +43%、p99 +82%；平均 PR 没有巨大膨胀，PR 类型分布稳定，revert 比例几乎未变。
- 🛡️ **稳定性良好**：事件摄取、会话回放摄取、Feature Flags API 近 90 天可用性 100%；App 99.993%，REST API 查询端点 99.985%。
- 👀 **不是每个 PR 都需要人类评审**：所有 PR 仍需批准；StampHog 先做确定性安全检查，再用 LLM 查致命问题，通过则批准，否则升级人工。
- 💸 **StampHog 高效**：约 20% PR 由 StampHog 批准，每月 token 成本约 300 美元；ReviewHog 面向复杂评审，提供代理舰队式深入审查。
- 🧠 **人类评审聚焦关键问题**：是否理解变更、作者是否理解、是否安全、是否有价值；简单评审应像 linting 一样交给代理。
- 🧪 **代理需要测试更多代码**：不再只靠手写 Playwright 慢测试；代理可点击 UI、判断是否正常、生成标注截图、动画回放和视频，qa-frontend 是早期版本。
- 📦 **PostHog 定位**：作为产品上下文层，整合 AI 可观测性、产品分析、会话回放、功能开关、实验、错误追踪、日志等，并由数据仓库和 CDP 统一，可从 Slack、Web、桌面端和 MCP 操作。

---

### [react-native-web 的维护与现代化 · necolas/react-native-web · 讨论 #2872 · GitHub](https://github.com/necolas/react-native-web/discussions/2872)

**原文标题**: [Maintenance and modernization of react-native-web · necolas/react-native-web · Discussion #2872 · GitHub](https://github.com/necolas/react-native-web/discussions/2872)

overview summary
React Native Web 将恢复积极维护，并由 zoontek、necolas、Expo 和社区推动迁移到 React Foundation；计划在 0.22-dev 分支进行现代化改造，包括提高浏览器目标、放弃 React 18、迁移 TypeScript/ESM、更新工具链、移除旧模块和补充缺失 API。社区可参与 PR 审查、预发布测试，并讨论后续打包器插件。

- 🚀 react-native-web 恢复主动维护与开发，仓库将迁移至 React Foundation GitHub 组织，与 React 和 React Native 并列。
- 🎯 方向保持保守：尽量贴近 React Native；React Native API 与原生/Web 融合问题属于 React Native 和 react-strict-dom。
- 🧹 维护计划：处理开放 issue 和 PR，修复、合并或关闭；通过常规版本发布 bug 修复。
- 🏗️ 现代化在 0.22-dev 分支进行，多数不改变 API，但包含破坏性变更。
- 🌐 最低浏览器目标提升至 2021 年 10 月版本：Chrome/Edge 95+、Firefox 93+、Safari/iOS Safari 15.1+，以移除前缀、UA 嗅探和旧回退。
- ⚛️ 放弃 React 18，react/react-dom peer 依赖改为 ^19.0.0，移除 findDOMNode 和 forwardRef。
- 🔄 Flow 迁移到 TypeScript，覆盖源码、测试、示例应用和 benchmark 应用。
- 🛠️ 工具链转向 pnpm、tsdown、vitest、oxlint 等；包以 ESM 发布（"type": "module"）。
- 📦 减少依赖：移除 inline-style-prefixer、@babel/runtime 等。
- 🗑️ 移除 React Native 核心已移除的模块：CheckBox、Picker、ProgressBar、YellowBox、InteractionManager、Touchable（旧 mixin）。
- ➕ 补充缺失 API，如 PlatformColor、useAnimatedValue、usePressability、Modal backdropColor、Text onTextLayout、TextInput clearButtonMode 等。
- 🧩 弃用 babel-plugin-react-native-web，因为现代打包器可用别名和 tree shaking，Expo CLI 也未使用。
- 🔮 后续打包器插件设想：配置别名和扩展解析、构建时替换 Platform.*、处理 @2x/@3x/@4x 资源、构建时提取 CSS 到单文件。
- 🤝 社区帮助：审查 PR、测试预发布并报告回归、评论“Later”想法；necolas 称 Expo 接手是理想结果，并希望未来也能支持 RSD。

---

### [](https://github.com/react/react-native/pull/58664)

**原文标题**: [[RNTester][iOS] Add tab bar controller, minimally support iPhone Duo by huntie · Pull Request #58664 · react/react-native · GitHub](https://github.com/react/react-native/pull/58664)

该 PR（#58664）将 RNTester 在 iOS 上的标签栏改为原生 `UITabBarController`，由应用内 Fabric 组件 `<RNTesterTabsIOS>` 托管，同时保持单一 React Native 根视图；目标是在不为 React Native 核心新增能力的前提下，最小化支持 iPhone Duo 的安全区与侧边标签栏布局。Android 保持不变。该 PR 经讨论后调整方案，最终由 javache 批准，并由 meta-codesync 合并（`ba89b39`）。

- 🧩 核心改动：新增应用内 Fabric 组件 `<RNTesterTabsIOS>`，包装 `UITabBarController`，并将 React 内容放入当前选中标签页，保持在安全区内。
- 🍎 iOS 行为：RNTester 的标签栏改为原生实现，以利用平台标签栏和安全区行为，适配 iPhone Duo 等布局。
- 🤖 Android 行为：保持不变，继续使用原有的 JS 头部和标签栏，标签页显示 Components、APIs、Playground。
- 🧭 动机：原 iOS RNTester 用 JS 绘制头部和底部标签栏，无法适配 iPhone Duo 的状态栏侧边挖孔与侧边标签栏布局。
- 🛠️ 实现方式：有意采用应用本地原生 fork，不在核心中改动 `<SafeAreaView>`，也不对自定义标签栏做硬编码修补。
- 📦 依赖选择：标签栏组件内联实现，而非引入 `react-native-screens`，避免在核心中添加依赖。
- 🔄 状态共享：标签选择仍保留在 `RNTesterNavigationReducer` 中，与 Android 共享；原生上报标签按压和安全区内边距。
- 📐 布局调整：在所有平台上，将模块列表和示例框架最大宽度限制为 600pt。
- 🧭 标签顺序：在两端平台都将 Playground 移至最后一个标签。
- ⚠️ 关键取舍：头部仍保留在 JS 中，因此没有原生返回按钮或返回滑动手势；原生头部需要每个导航层级对应视图控制器，暂不在范围内。
- 🧪 测试计划：使用 xcodebuild 构建 iOS 模拟器，并在 iPhone 18 Pro（iOS 27.0）和 iPhone Duo（iOS 27.1）上运行。
- ✅ 验证内容：标签可切换，包括 Maestro 流程使用的 `apis-tab` 测试 ID；模块和示例可通过原生返回与文档按钮推入；Recently Viewed 会更新。
- 🔗 深链：`rntester://example/Switch` 热启动和 `rntester://example/Image` 冷启动均能打开 Components 标签页中的目标。
- 📱 iPhone Duo：折叠和展开时各页面均处于安全区内；展开时列表和示例框架宽度上限为 600pt。
- 🧪 未运行：Maestro 测试。
- 💬 讨论焦点：javache 担心多根视图影响较大，建议用基础原生组件保持单根；cortinico 也支持单根，并认为不必专门为 iPhone Duo 优化 RNTester。
- 🔧 方案调整：huntie 后续更新为从 JS 视角保持单根设计，称为“最小化使其不出错”的修复；仍保留自定义头部、无返回/滑动，以及 Duo 特定内边距逻辑和伪 SafeAreaView 回调。
- ✅ 评审结果：javache 批准变更；cortinico 和 cipolleschi 仍待评审；最终该 PR 被合并。
- 🏷️ 标签与状态：获得 CLA Signed、Shared with Meta、Merged 标签；分支 `rntester-native-navigator` 已删除。

---

### [你的技能需要一个评估机制 — Expo 博客](https://expo.dev/blog/your-skills-need-an-evaluation-mechanism)

**原文标题**: [Your skills need an evaluation mechanism â Expo blog](https://expo.dev/blog/your-skills-need-an-evaluation-mechanism)

未提供可总结的文本内容，因此暂时无法生成文章摘要。请把需要总结的内容发来，我会按“概览 + emoji 要点”的格式用中文整理。

- 📄 当前缺少待总结的正文
- ✍️ 请补充文章或段落内容
- ✅ 收到内容后我会提取关键信息并生成要点列表

---

### [](https://www.dainemawer.com/shared-typescript-nextjs-expo-monorepo)

**原文标题**: [Sharing a TypeScript Domain Layer Between Next.js and Expo](https://www.dainemawer.com/shared-typescript-nextjs-expo-monorepo)

本文介绍如何在 pnpm/Turborepo monorepo 中让 Next.js 与 Expo 共享一个窄的 TypeScript 领域层：共享类型、校验 schema 和轻量 API 客户端；避免共享导航、存储与 UI；并解释 Metro 解析 pnpm 符号链接的历史问题，以及 Expo SDK 54 后内置 monorepo 支持带来的变化。核心收益是后端契约变更能在两端同时被类型错误或 schema 校验捕获。

- 📦 适合共享：TypeScript 类型、Zod/Valibot 校验 schema、调用 API 并解析响应的薄函数，它们不依赖 DOM 或原生模块。
- ✅ 校验 schema 是最大收益：Next.js 路由处理器与 Expo 页面用同一套代码校验同一响应，后端字段或结构变更会在开发阶段两端同时报错。
- 🧠 纯计算业务逻辑（定价、日期、权限检查）若无副作用也可放入；一旦依赖 `localStorage`、`document` 或 `expo-secure-store`，就不应跨端共享。
- 🚫 不要共享导航：Next.js App Router 面向服务器流式响应，Expo Router 面向原生栈或标签导航，强行抽象只会转移复杂度。
- 🔐 不要共享存储与会话：浏览器有 cookies/localStorage，Expo 有 SecureStore/AsyncStorage；共享 API 客户端只应接收 token 参数，不应知道 token 存储位置。
- 🎨 不要共享 UI：Web 与原生组件模型不同；跨端组件库应作为独立项目，使用 Tamagui、NativeWind 等专门方案，而不是塞进类型包。
- 🧭 判断规则：返回类型取决于运行环境（浏览器/设备）就留在 App；只取决于数据才可移入共享包。
- 🔗 pnpm 用内容寻址存储加符号链接构建 `node_modules`；Metro 历史上按真实文件路径解析、不跟随符号链接，可能导致找不到共享包或解析到错误依赖副本。
- 🛠️ Expo SDK 54 起，`expo/metro-config` 内置 pnpm/npm/Yarn/Bun monorepo 支持（含符号链接），大多数场景不再需要手动配置 `watchFolders`、`resolver.nodeModulesPaths`、`disableHierarchicalLookup`。
- 🧹 若从旧项目继承这些配置，应移除并运行 `expo start --clear` 一次，避免旧 Metro 缓存继续造成解析问题。
- ⚙️ 旧 SDK（53 及更早）或仍解析失败时，可在 `.npmrc` 设 `node-linker=hoisted` 作为可靠兜底，但会牺牲 pnpm 的磁盘与安装速度优势。
- 📱 EAS 构建与原生模块自动链接是另一个失败面；若只在 EAS 报 `Cannot find module`，检查构建日志实际使用的安装策略，它未必匹配本地 `.npmrc`。
- 📄 共享包可将 `main`/`types` 指向 `./src/index.ts`：Next.js 需加入 `transpilePackages`，Metro 通常直接转译 TS 源码；若需编译产物，用 `tsup` 或 `tsc` 构建并指向 `dist`。
- 🧩 为编辑器解析可加根 `tsconfig.json` 的 `paths` 或项目引用；在 CI 中对共享包单独运行 `tsc --noEmit`，让类型错误在包内尽早失败。
- 🎯 最终收益：共享包保持小而专注，只消除一个失败模式——后端响应结构变更能在两个 App 中同时被类型错误或 schema 解析失败捕获。

---

### [获取失败](https://shift.infinite.red/you-dont-need-a-rewrite-expo-s-new-brownfield-react-native-story-c072b4e971dd)

**原文标题**: [Failed to retrieve](https://shift.infinite.red/you-dont-need-a-rewrite-expo-s-new-brownfield-react-native-story-c072b4e971dd)

无法总结：获取内容失败，状态码 403。

---

### [面向 AI 编程代理的 Maestro MCP](https://maestro.dev/blog/maestro-mcp-for-ai-coding-agents?utm_source=this-week-in-react)

**原文标题**: [Maestro MCP for AI Coding Agents](https://maestro.dev/blog/maestro-mcp-for-ai-coding-agents?utm_source=this-week-in-react)

Maestro MCP 让 Claude Code、Cursor、Codex 等 AI 编码代理通过 MCP 连接真实设备或模拟器，在聊天中直接操作应用、运行流程、检查 UI 并截图，支持 iOS、Android、React Native、Flutter 和 Web。

- 🧩 Maestro MCP 随 Maestro CLI 提供，添加 MCP 服务器后，代理会话中会出现 UI 自动化工具。
- 📱 只需启动 iOS 模拟器、Android 模拟器或连接 Android 真机，代理即可通过 `list_devices` 确认目标设备。
- 🤖 兼容 Claude Code、Cursor、Codex、Copilot、Gemini、Windsurf、JetBrains AI Assistant、Grok Build 等代理。
- 🛠️ 核心工具包括 `inspect_screen`、`run`、`take_screenshot`、`cheat_sheet`、`open_maestro_viewer`、`run_on_cloud` 等。
- 👀 Maestro Viewer 可并排展示实时设备画面与命令流，让人类在 IDE 中跟随代理操作。
- 🔁 常见用法包括确认功能是否正常、遍历主标签或设置页、保存 PR 截图，以及失败后检查屏幕并重试。
- 🚀 快速开始：安装 Maestro CLI，添加 MCP，启动设备，安装并启动应用，然后用自然语言让代理检查 UI。
- ✅ 价值在于 UI 检查与代码实现处于同一会话，反馈更快，并有截图和 Viewer 作为可分享证据。

---

### [](https://github.com/wcandillon/react-native-skia/releases)

**原文标题**: [Releases · wcandillon/react-native-skia · GitHub](https://github.com/wcandillon/react-native-skia/releases)

该页面是 wcandillon/react-native-skia 的 GitHub Releases 列表，展示从 v3.0.6 到 v3.4.2 等多个版本，发布时间集中在 2026 年 10 月；更新以 Bug 修复和平台/图形后端支持为主，最新版为 v3.4.2。

- 📦 仓库为 wcandillon/react-native-skia，页面包含 Releases/Tags、版本比较入口，以及 Code、Issues(45)、Pull requests(79)、Actions 等导航。
- 🏷️ 最新版 v3.4.2 于 2026-10-13 发布，修复 Canvas ref、Graphite 录制、Canvas onLayout、Android 绘制重绘、worklet 序列化与 CanvasRef 类型等问题。
- 🍏 v3.4.1 于 2026-10-12 发布，补上缺失的 react-native-skia-graphite-apple-tvos 依赖。
- 📱 v3.4.0 于 2026-10-11 发布，新增 Skia Graphite 和 Dawn 的 tvOS 支持。
- 🖥️ v3.3.0 于 2026-10-08 发布，新增 Mac Catalyst 支持（Skia Graphite 和 Dawn），并修复 Android Vulkan shared-fence 问题。
- 📸 v3.2.0 于 2026-10-08 发布，引入新 snapshot API，并修复 RN 0.87+ Web 资源注册、GPU 资源删除、Android 原生视图发布和 ProGuard 规则。
- 🌐 v2.15.1 于 2026-10-08 发布，专门修复 React Native 0.87+ Web 上的资源注册问题。
- 🔗 v3.1.0 于 2026-10-07 发布，从 react-native-webgpu-dawn 包链接 Dawn。
- 🧱 v3.0.8 于 2026-10-07 发布，将 canvas provider 层级折叠到 RNSkWindowSurface 中。
- ⚙️ v3.0.7 于 2026-10-07 发布，避免与 react-native-webgpu 同时出现重复的 libwebgpu_dawn.so。
- 🛠️ v3.0.6 于 2026-10-07 发布，修复 SwiftPM 二进制发布令牌问题，发布 Skia Graphite 154.1.0 二进制，并在 Android 上启用 Skia RTTI。

---

### [](https://github.com/callstack/react-native-testing-library/releases/tag/v14.1.0)

**原文标题**: [Release v14.1.0 · callstack/react-native-testing-library · GitHub](https://github.com/callstack/react-native-testing-library/releases/tag/v14.1.0)

react-native-testing-library 发布 v14.1.0（2026-10-08），重点支持 React Native 0.88 / React 19.3，增强 UserEvent 与 fireEvent，并修复多项问题、更新文档。
- 🚀 v14.1.0 为最新版本，由 mdjastrzebski 发布，含 3 个提交合入 main
- ✨ 新增 fireEvent.layout、UserEvent.accessibilityAction、UserEvent.pullToRefresh()
- 📱 支持 React Native 0.88（React 19.3）
- ⚠️ 在禁用元素上触发事件时会发出警告
- 🐛 修复 fireEvent.layout 直接事件、fireEvent 直接事件冒泡弃用、nightly RN 0.88、scroll to event seq、jsdom 假定时器 setImmediate 等问题
- 📚 文档更新：澄清可访问名称说明、贡献者文档、v14.1.0 文档
- 📂 仓库导航显示当前有 1 个 issue、6 个 pull requests，以及 Discussions、Actions、Wiki、Security and quality 等入口

---

### [](https://tamagui.dev/blog/version-three)

**原文标题**: [Tamagui 3: a new native runtime, more native compilation, flat style props, React Strict DOM, and Tailwind syntax for one cross-platform UI codebase.](https://tamagui.dev/blog/version-three)

Tamagui 3 是一次大版本升级：引入 C++ 原生样式运行时和更强优化编译器，以扁平 style props、React Strict DOM 与 Tailwind 前端让样式更多脱离 React 渲染路径，同时保持 React Native 与 Web 共用一套 UI 代码库。

- 🚀 新原生运行时 @tamagui/native-registry：主题更新写入 C++ 注册表，并通过 Fabric 直达符合条件的原生视图，无需重渲染使用它们的 React 组件。
- ⚙️ 该运行时是 React Native 新架构的可选 beta；需启用编译器 nativeFastPath、启动时注册引擎并重建原生应用，要求 RN 0.82+。
- 🧠 编译器增强：原生端可处理更多条件表达式、嵌套三元、多个独立条件 props、静态 spread，并解析已知输入的 styled.dynamic() 变体与 .resolve() 链。
- 🧩 扁平 style props：基础值与条件写在同一属性中，支持字符串和对象形式，如 bg="background hover:background-hover"、p="4 sm:6"。
- 🌬️ 修饰符语法接近 Tailwind：可链接 dark:sm:hover:，支持平台、group、container 条件；同一值内字符串与对象形式可混用。
- 🏷️ Config v6 将多词主题键改为 kebab-case，如 border-color、background-hover；提供 flat-values codemod，先 report 再 --write。
- 🧱 React Strict DOM：用 html.* 语义元素编写，Web 渲染为 DOM，原生渲染为 React Native 等价组件；Tamagui Tailwind 则在 className 写工具类，Web 提取为原子 CSS，原生解析为 RN 样式。
- 📦 styled 与 unstyled 按导入路径拆分：tamagui 是带默认样式的 styled kit；@tamagui/button 等提供行为与部件；tamagui/unstyled 汇总无样式层。
- 🪶 可选零运行时：Web 上 experimental.zeroRuntime: 'report' 可找出可降级入口；普通编译应用仍保留所需运行时。
- 🧠 新增 Rust 编写的 @tamagui/lsp：提供补全、诊断、悬停 token 解析、色块，支持多种编辑器；VS Code 扩展暂未上架 Marketplace。
- 🧮 样式优先级分层：base styled < variants < component resolvers < callsite style props < style；同层内后写胜出，className 与 callsite props 同层。
- 🧬 同一扁平值内子句顺序不影响结果；子句按平台、条件数量、类别（media/container/theme/group/state）排序，更具体的条件应显式写出。
- 🧰 样式复用：style() 定义可复用样式；styled.dynamic() 处理依赖单 prop 的动态变体；.resolve() 处理依赖完整 props 的解析样式。
- 🧹 移除大量废弃 API：focusable、fullscreen、themeInverse、Theme inverse、styleable 静态、forwardRef 包装、inlineWhenUnflattened、旧别名、旧平台样式键、$true token 键等。
- 🔧 useProps/usePropsAndStyle 移除，useStyle 仅解析 style piece；可用 splitStyleProps 与 getExpandedShorthand 处理作者 props。
- 🅾️ 移除 $true token：布局用显式 space token；控件尺寸改为 xs/sm/md/lg/xl，默认 md；size={true} 选择默认控件尺寸。
- 📏 移除 token stepping：getSize/getSpace/getRadius 只解析传入键，stepTokenUpOrDown/getTokenRelative 删除；组件改为对解析后的数值乘调优常量。
- 🔢 字号区分数值与精确像素：fontSize={17} 使用平台默认行高，fontSize="17px" 表示精确像素；v5 配置字号/行高固定为 px 字符串以保持视觉。
- 🌗 inverse 推荐用普通 sub-theme；themeInverse 移除，改用 theme="inverse" 与 <Theme name="inverse">。
- 🪟 Sheet 结构显式化：Sheet.Frame 拆为 Sheet.Container 和 Sheet.Background；Sheet.Overlay 必须是 Sheet 直接子级。
- 🔄 Dialog、Popover、Select 统一 Adapt handoff：open 状态位于 Adapt 父级之上，适配 Sheet 内容保持挂载并通过 part 管理 presence 动画。
- 🎞️ 一等动画 API：导出 useAnimationDriver、useAnimatedNumber、useAnimatedNumberStyle 等；CSS 驱动改用 rAF ticker 和真实完成回调；onTransition 提供类型化生命周期。
- ♿ FocusScope 支持 noFocus 零焦点模式，渲染 display: contents 包装器，不再支持 function-as-children。
- 🧭 组件状态更一致：更多 trigger/content 提供 data-state；Select.Trigger/Viewport 暴露 data-state；Select.Content 支持 onEscapeKeyDown/onInteractOutside；新增 Select.Separator。
- ✅ Select 支持 multiple：跨 Web 与原生使用有序 string[]；Web 自定义 Select 提交重复表单条目；native="web" 使用真实 <select multiple>。
- 📝 新增行为型 Field，Form 升级为跨平台字段协调器；支持函数或 Standard Schema（Zod 4、Valibot、ArkType）校验，异步校验不阻塞提交。
- 🎯 图标按文本字号缩放：<Icon size="4" /> 对齐 font.size.4；主题图标不再支持 media/pseudo props；移除 @tamagui/lucide-icons-2，改用 npx @tamagui/cli icons add。
- 📜 @tamagui/scroll-view 提供干净 Web 实现，不再经由 react-native-web；支持 scrollTo、scrollToEnd、onScroll、contentContainerStyle 等。
- ⚡ optimizeFor：Web 默认 'updates'（细粒度追踪、最小重渲染），原生默认 'first-render'（跳过追踪、初始渲染更快，变更时可能重渲染更多）。
- 🧪 新增 <ThemeUpdate> 与自定义 variables：可为子树调整主题值，支持 dark:、ios: 等修饰符；变量像主题键一样可用于 style props/useTheme；defaultProps 移除。
- 🛠️ 迁移：用 @tamagui/cli setup/migrate，复制 CLI 打印的 agent prompt；运行 tamagui check 与 codemod-flat-values --write --report；搜索移除 API、旧 token sigil、隐藏条件样式、size="$..."、半阶 token 等。
- ⚠️ 迁移注意：SafeAreaProvider 放在 TamaguiProvider 外；在改动层做 typecheck/build/Web 验证，并在使用 Adapt 的断点测试 Dialog、Popover、Select、Sheet。

---

### [](https://onestack.dev/)

**原文标题**: [One: React Native, all in one | The faster, easier and more complete way to build React Native apps: works with what you use, with 100% native API coverage built in.](https://onestack.dev/)

One v2 已发布，定位为 React Native 的一体化开发方案，主打更快、更易用、更完整；它兼容你已有的库，并开箱提供其余能力，实现 100% 原生 API 覆盖。

- 🚀 发布与起步：One v2 面向 React Native，支持 `npx one` 快速开始，并提供完整文档。
- ⚡ 速度优势：比 Metro 快 5.4 倍；生产 iOS 应用冷启动开发打包中，One 为 3.6 秒，Metro 为 19.5 秒（同一机器）。
- 🧩 One Native：所有原生视图和 API 都有类型；SwiftUI 和 Jetpack Compose 直接从平台 SDK 生成；触觉、存储、更新、通知等在 iOS 和 Android 上共用一次调用。
- 📦 开箱即用：内置路由、原生 UI、原生 API、OTA 更新与回滚、数据加载、部署、DevTools 和构建能力。
- 🗺️ 路由与数据：支持类型化文件系统路由、布局、栈和标签页；每个路由可选择 SSR、SSG 或 SPA。
- 🚀 部署与构建：可部署到 Vercel、Cloudflare 或自有 Hono 服务器；支持 prebuild、`run:ios` 和 `run:android`，无需 Expo。
- 🛠️ DevTools：提供路由调试、loader 计时和源码检查器。
- 🔓 无锁定：兼容 Expo modules、React Navigation、Reanimated、Nitro modules、Tamagui、NativeWind 和 Metro 模式。
- 👥 背景与社区：由 Tamagui 团队基于 Tamagui Takeout 和 Uniswap 的跨平台经验打造；提供 X、GitHub、Discord、博客，版权归 Tamagui, LLC 所有（2024）。

---

### [](https://github.com/gmi-software/react-native-better-pdf)

**原文标题**: [GitHub - gmi-software/react-native-better-pdf: Native, virtualized PDF viewer for React Native, built on Nitro Views · GitHub](https://github.com/gmi-software/react-native-better-pdf)

overview summary
- 📦 react-native-better-pdf 是面向 React Native 的原生、虚拟化 PDF 查看器，基于 Nitro Views 与新架构 Fabric 构建。
- 🧱 iOS 使用 PDFKit，Android 使用平台 PdfRenderer；不捆绑 PDFium、不使用 WebView，滚动、缩放和渲染路径不经过 JS 线程。
- ⚡ 性能优先：滚动、缩放、渲染、缓存和预取都不触碰 JS 线程，JS 只接收配置、命令和稳定事件，没有逐帧事件。
- 📄 支持多种来源：本地文件、打包资源 require()、content:// URI，以及带请求头的远程 PDF，并原生下载。
- 📚 离线阅读与缓存：支持 session/persistent 缓存、ETag/Last-Modified 校验，PdfCache 可提前下载并显示进度、支持取消。
- 🧭 阅读位置：通过 onViewportChange、initialViewport、goToViewport 恢复阅读位置，并检测是否读到文档末尾。
- 📐 布局能力：垂直连续、水平、分页、单页、从右到左，适配宽度/高度/页面，平板对页，contentInset 和圆角卡片。
- 🔍 原生全文搜索：高亮匹配项，支持上一个/下一个导航，并报告搜索进度与当前匹配。
- ✍️ 表单支持：AcroForm 字段可通过触摸或代码填写、按名称读回，并导出填写后的 PDF。
- 🧩 页面叠加层：React 视图可附着到页面坐标，页面滚动和缩放时由原生代码同步移动。
- 🌙 深色页面：反转亮度并保留色相，适合夜间阅读；搜索和选择高亮保持原有颜色。
- 🖨️ 支持大纲、页面尺寸、页面图片、系统打印，以及无需视图的 PdfDocument，用于文档列表和封面。
- 🔐 支持密码保护 PDF，错误码在双平台稳定一致，并支持 VoiceOver/TalkBack 无障碍阅读。
- 🧠 内存由视口限制：页面虚拟化、渲染缓存、预取、取消，并在内存压力或页面隐藏时释放像素。
- 📱 环境要求：React Native 0.81+、新架构、Nitro Modules >=0.37.0、iOS 15.1+、Android minSdk 24+；Expo SDK 54+ 开发构建，不支持 Expo Go。
- ⚙️ 安装方式：添加 react-native-better-pdf 与 react-native-nitro-modules；裸 React Native 需 pod install；Expo 无需 config plugin，但需重建开发构建。
- 🆚 对比 react-native-pdf：原生代码体积更小，Android 约 1.9 MB vs 约 5.3 MB；加载更快，大型扫描件的内存和 CPU 优势明显。
- 📊 基准示例：1000 页扫描件加载约 91 ms vs 746 ms，滚动 CPU 约 27% vs 114%，峰值内存约 144 MB vs 897 MB。
- 🧪 针对 react-native-pdf 常见痛点：16 KB 页大小、新架构、blob-util 崩溃、Android 已关闭崩溃、链接点击、搜索、视口恢复、表单和缓存控制。
- 🧩 公共 API：PdfView、PdfPageOverlay、PdfDocument、PdfCache、PdfOpenError/PdfDownloadError，以及 PdfViewRef 的跳页、缩放、渲染、打印、搜索和表单方法。
- 🚧 当前限制：暂不支持编辑注释；部分 Android 功能需 Android 15+ 或 Android 12–14 加 SDK 扩展 13；data:/base64 不支持；Expo Go 不支持。
- 📚 文档位于 docs/，包含迁移指南、架构、API 设计、基准、审计和社区请求；项目采用 MIT 许可证。

---

### [](https://github.com/chrispader/expo-native-variants)

**原文标题**: [GitHub - chrispader/expo-native-variants: Generate every native Expo app variant in one prebuild. · GitHub](https://github.com/chrispader/expo-native-variants)

expo-native-variants 是一个社区维护、面向 Expo SDK 57 的早期发布插件，可在一次 Expo prebuild 中为同一项目生成 development、preview、production 等所有 iOS/Android 原生变体，并让 `ios/` 与 `android/` 保持生成且被 Git 忽略。它通过 app 配置中的 `variants` 定义应用标识、图标、URL scheme、更新通道等，支持 Xcode scheme、Android flavor、iOS 扩展目标和运行时变体识别；EAS 支持仍属实验性，兼容性有明确限制。

- 🧩 安装 `expo-native-variants` 并加入 `app.config` 的 `plugins` 数组；每个变体必须提供完整且唯一的 `applicationId`，第一个声明的是主变体。
- ⚙️ 运行 `expo prebuild --clean` 后，可在 Xcode 或 Android Studio 中选择对应 scheme/flavor；原生依赖或配置变更需再次 prebuild，仅切换变体不需要。
- 📱 变体生成 iOS scheme（如 MyApp-Development、MyApp-Preview、MyApp-Production）及 Android 构建变体（developmentDebug/Release、previewDebug/Release、productionDebug/Release）。
- 🔁 同一变体的 debug 与 release 共用标识符，安装其中一个会替换另一个。
- 🛠️ `variants` 是唯一必填选项；可选 `variant` 可覆盖 `NATIVE_VARIANT`，`ios.targets` 用于扩展目标，且不会限制生成完整变体矩阵。
- 🎨 变体可配置 `icon`、`displayName`、`urlScheme`、`updateChannel`、`runMode` 及 iOS/Android 平台覆盖；省略图标时继承共享 Expo 图标设置。
- 🖼️ 插件生成 iOS asset catalog 和 Android flavor 资源并清理自己拥有的旧文件，但拒绝覆盖手动修改；不支持 Icon Composer `.icon` 目录。
- 🧱 iOS 扩展目标可通过精确 Xcode target 名和 `bundleIdentifierSuffix` 接入；目标生成插件需先注册，`expo-native-variants` 放在插件列表最后。
- 🔐 共享 App Group 可用 `group.$(EXPO_NATIVE_VARIANT_BUNDLE_IDENTIFIER)`，Xcode 会按配置展开为主应用标识符。
- 🧭 运行时用 `expo-application` 读取 `applicationId`，再调用 `getNativeVariant` 得到变体键；未知、缺失或歧义时返回 `null`，不会默认 production。
- 📡 不同 applicationId 不能隔离 OTA；需用独立 EAS Update 通道与分支。本地构建可设 `updateChannel`，显式通道优先于 EAS profile 的 channel。
- ☁️ EAS Build 每个 job 构建一个应用，需在 `eas.json` 的 profile `env` 中设置 `NATIVE_VARIANT` 与 `channel`；云构建、签名和凭据选择尚未验证，属实验性。
- 🚦 `EAS_BUILD_PROFILE` 在本地 app 配置评估时不可用；不要仅依赖云 profile 名称推断变体。
- 🧪 开发客户端应为 `expo-dev-client` 设置 `addGeneratedScheme: false` 并置于插件前；Metro 仍服务共享 manifest，需用 `NATIVE_VARIANT` 与 `--scheme` 启动。
- ⚠️ 兼容 Expo SDK 57 的 Android Groovy 模板、一个 iOS 应用目标及明确配置的扩展目标；不支持现有 Android flavors、多 flavor dimension、Kotlin DSL、App Clips、watch 等。
- 🍎 与 `@bacons/apple-targets@5.0.0` 测试时需 clean prebuild；iOS 27 目标需配置 scene support，否则可能启动崩溃。
- 📦 示例包含三个变体，展示已安装标识符、解析变体与 debug/release 模式；根脚本含 build、typecheck、test、test:integration、verify:package 等。
- 📄 项目采用 MIT 许可证，稳定版走 npm `latest`，预发布走 `next`。

---

### [](https://github.com/mahdidavoodi7/react-native-wifi-aware)

**原文标题**: [GitHub - mahdidavoodi7/react-native-wifi-aware: Peer-to-peer discovery and high-bandwidth local data paths over Wi-Fi Aware (NAN) for React Native and Expo. Wraps Apple's WiFiAware framework (iOS 26) and Android's WifiAwareManager behind one typed API. Swift + Kotlin via Nitro Modules. · GitHub](https://github.com/mahdidavoodi7/react-native-wifi-aware)

react-native-wifi-aware 是一个面向 React Native 与 Expo 的 Wi-Fi Aware（NAN）点对点网络库，用统一 TypeScript API 封装 Apple WiFiAware（iOS 26+）和 Android WifiAwareManager（API 26+），基于 Nitro Modules 提供 Swift/Kotlin 实现，用于附近设备发现、强制配对、加密连接和高速本地二进制数据传输；但仅支持 Apple↔Apple 与 Android↔Android，iPhone↔Android 不被支持或承诺。

- 📡 核心能力：无需路由器、热点或互联网，设备间可通过 Wi-Fi Aware 直接发现、配对并建立高带宽数据路径。
- 🧩 技术实现：Nitro Modules + Swift/Kotlin，统一 TypeScript API，支持 React Native 0.75+，并提供 Expo config plugin。
- 🔐 安全设计：连接默认认证并加密，库拒绝打开未加密数据路径；数据路径密钥可由配对派生或双方共享。
- 🤝 配对机制：同时支持系统配对 `presentPairingUI()` 和 App 自建配对 `getProgrammaticPairing()`，可使用 PIN、密码、QR、NFC。
- ⚠️ 强制配对：Wi-Fi Aware 数据路径必须先配对；配对一次后持久保存，由用户管理或撤销，没有匿名通道。
- 📦 数据传输：使用 `ArrayBuffer` 传输二进制负载，长度前缀分帧，一次 `send()` 对应一次 `onMessage`，最大约 64 MB。
- 🎛️ 性能模式：支持 `'bulk'` 与 `'realtime'`，双方必须选择相同模式；还可设置 `accessCategory` 作为 QoS 提示。
- 📶 链路质量：`getPerformance()` 可读取信号强度、吞吐上限/容量、各分类发送延迟。
- 🧭 错误处理：提供结构化错误码 `getWifiAwareErrorCode()` 和错误监听器，并保留原生 domain、code、description。
- 🧪 服务名校验：Expo 插件会在 prebuild 校验 DNS-SD 服务名，避免无效 `Info.plist` 导致真机启动崩溃。
- 🍏 iOS 要求：需要 iOS/iPadOS 26+、Xcode 16.4+/26+、Swift 5.9+；`com.apple.developer.wifi-aware` 是 Apple 管理权限，需提前申请。
- 🤖 Android 要求：API 26+ 可发现，API 29+ 支持数据路径，API 34+ 支持配对；硬件支持按设备/厂商而异，必须运行时检查。
- 🚫 运行限制：不支持 Expo Go、iOS 模拟器或无硬件 CI；测试至少需要每平台两台真机。
- 🔁 互操作性：Apple↔Apple 和 Android↔Android 是官方支持产品；iPhone↔Android 未被证明可用，Android 多数设备 `isAwarePairingSupported()` 返回 false。
- 🧪 跨平台实验：仅通过 `initiatePairingWithForeignPeer()` 隔离入口尝试 iPhone↔Android，预期失败，其他 API 不会静默尝试。
- 📵 非普通 Wi-Fi：不会加入、扫描或配置基础设施 Wi-Fi，也不适合房间 mesh、匿名陌生人共享或自动唤醒。
- 🛠️ 生命周期：连接后应停止会话以节省功耗；所有 `addOn...Listener` 返回订阅，需调用 `remove()`；连接也需显式关闭。
- 🎯 适用场景：大文件本地传输、离线设备同步、本地多人、无网络现场、设备迁移、相机/无人机卸载、邻近触发、ESP32 等 NAN 硬件。
- 📚 作者与许可：由 Motionary 的 Mehdi 构建维护，MIT 许可证，仓库当前约 61 stars。

---

### [发布 v1.0.0 · gronxb/hot-updater · GitHub](https://github.com/gronxb/hot-updater/releases/tag/v1.0.0)

**原文标题**: [Release v1.0.0 · gronxb/hot-updater · GitHub](https://github.com/gronxb/hot-updater/releases/tag/v1.0.0)

Hot Updater v1.0.0 正式发布首个稳定版，由 gronxb 于 10 月 11 日发布，包含 14 次提交合并到 main；核心亮点包括更快的更新检查、Insights、Remote Config、插件化、可自托管 Console、AI Agent 配置与 v0 升级指引。

- 🚀 v1.0.0 是 Hot Updater 的首个稳定版本，已发布并附有博客文章与完整变更日志（v0.36.18...v1.0.0）。
- ⚡ 更新检查改为共享读取：服务端按 scope 发布一个可缓存的 Release Catalog，每台设备自行选择更新；中位检查时间从 v0 的 301 ms 降至 Cloudflare 上的 50 ms。
- 📊 Insights：跟踪下载、启动、崩溃恢复和更新失败，并在 Console 中提供 Release health 与回滚建议。
- 🛠️ Remote Config：无需新 bundle 或原生构建即可修改应用读取的配置值。
- 🧩 Plugins：Insights、Remote Config 和客户端 API keys 在服务端与 App 中均以插件形式提供，也支持自写插件。
- ☁️ Console Deployments：可从 hot-updater/console 在 Node、Docker、Vercel、Netlify 或 Cloudflare Workers 上为团队托管 Console，并支持 GitHub 或 Google 登录。
- 🤖 AI agent setup：可通过编码代理设置、升级和验证基础设施，并运行 hot-updater doctor --fix 修复项目。
- 📦 快速开始：安装 @hot-updater/react-native、开发依赖 hot-updater 与对应插件，并运行 npx skills@latest add hot-updater/skills，然后按 Start here 操作。
- ⬆️ 从 v0 升级：v1.0 需要独立的 v1 基础设施和新的原生构建；保留 v0 端点以服务现有 binary，并遵循 Move from v0 to v1 与 BREAKING_CHANGES.md；v0 保留在 v0 分支。
- 🎉 发布获得 11 个 🎉 和 8 个 🚀 反应；GitHub 签名验证通过。

---

### [](https://github.com/getsentry/sentry-react-native/releases/tag/8.30.0)

**原文标题**: [Release 8.30.0 · getsentry/sentry-react-native · GitHub](https://github.com/getsentry/sentry-react-native/releases/tag/8.30.0)

sentry-react-native 8.30.0 已发布，主要新增蜂窝网络技术类型上报，移除旧 span 属性，并修复 Expo、Hermes、iOS、Android 等多处问题，同时升级底层 SDK 依赖。

- 📶 新增在 `device.connection_effective_type` 中上报蜂窝网络技术类型，例如 `4g` 或 `5g`，支持 Android 和 iOS；Android 11 及更早版本需 `READ_PHONE_STATE` 权限，但 SDK 不会主动请求。
- 🧹 移除未文档化的 `maxTransactionDurationExceeded` span 属性，改用 `deadline_exceeded` span 状态筛选超时事务。
- 🧩 修复重写 Expo 堆栈跟踪时，Hermes 内部字节码帧未保留为非应用帧的问题。
- 🐛 修复 Android 原生崩溃中残留的 `turbo_module.*` 标签。
- 🖼️ 将图片附件转发到 Spotlight，而不是从 envelope 中剥离。
- 📱 修复 iOS 应用在使用无效 DSN 初始化 Sentry 时崩溃的问题。
- 📊 在 JS profiles 中填充 Hermes 运行时版本，避免发送空值。
- 🌳 将 `@sentry/react-native` 标记为无副作用，便于打包器 tree-shake 未使用的导出。
- 🛠️ Expo 插件改为从 Android 项目目录解析 `@sentry/react-native`，而不是从 Gradle 启动目录解析。
- ⚠️ 修复设置 `beforeSendLog` 等回调选项时，iOS 原生 SDK 输出日志导致应用崩溃的问题；回调选项仅用于 JavaScript 层，启动原生 SDK 前会被移除。
- ⬆️ 依赖升级：JavaScript SDK 从 v10.75.2 升至 v10.76.0，Cocoa SDK 从 v9.30.0 升至 v9.30.1，Android SDK 从 v8.59.0 升至 v8.60.0。

---

### [](https://swmansion.com/changelog/react-native-nano-icons-1-0-0/)

**原文标题**: [React Native Nano Icons 1.0.0](https://swmansion.com/changelog/react-native-nano-icons-1-0-0/)

React Native Nano Icons 1.0.0 于 2026 年 10 月 12 日发布，是一次重大版本更新，核心亮点包括 Metro 热重载、原生 Tab 栏符号、可动画的尺寸与颜色，并包含 React Native 0.81+ 等破坏性变更、多项改进和跨平台修复。

- 🚀 **重大发布**：React Native Nano Icons 1.0.0，发布于 2026 年 10 月 12 日。
- 🔥 **Metro 热重载**：用 `withNanoIcons` 包装 Metro 配置后，编辑 SVG 可在运行中的开发 App 内重载，无需原生重建；也支持图标字体热重载。
- 📱 **原生 Tab 符号**：SVG 可生成 iOS SF Symbols 和 Android VectorDrawables，并通过 `nativeNanoSymbol` 用于 react-navigation 原生 Tab；需 react-navigation 8 与 react-native-screens 4.29+。
- 🎞️ **可动画属性**：`size` 和 `color` 现在是原生 props，可用 Reanimated 动画，或通过 Unistyles 设置。
- ⚠️ **破坏性变更**：要求 React Native 0.81+（原为 0.74+）；升级后需重新生成字体并重建原生 App。
- 🛠️ **CLI 破坏性变更**：`--dynamic --app-config` 改为 `--dynamic-app-config`；`.nanoicons.json` 中路径相对于该文件解析；新增 `--help`。
- 🎨 **颜色改进**：支持 `PlatformColor` 和 `DynamicColorIOS`；新增 `tintMode="currentColor"`，可仅着色 `currentColor` 图层。
- 🔤 **字体与 Web**：每次字体构建生成指纹并在运行时校验；Web 端输出 `.woff2` 字体并按配置字体族渲染；`className` 会转发到容器元素。
- ⚙️ **流水线与性能**：用 TypeScript 版 picosvg 替代 Pyodide，重构 SVG 扁平化流程，使用 worker pool 编译图标，并精简 tarball 与生成字体。
- 🍎 **iOS 修复**：修复复用图标视图的缩放过期和状态泄漏；内联图标对齐文本基线；暴露 FabricComponents 头文件以支持基线校正。
- 🤖 **Android 修复**：字形适配视图边界以应用字体缩放；当 AGP 注册 Kotlin 扩展时跳过显式 Kotlin 插件。
- 📦 **CLI 与打包修复**：跳过含 `<text>`、`<style>`、`<foreignObject>`、`<a>`、`<switch>` 的图标而非使整个集合失败；从 target build settings 解析 iOS Info.plist；按 upm 缩放默认 safeZone；补充缺失的 `react-native` 导出字段；发布包包含 codegen specs。
- 👥 **新贡献者**：@huextrat、@vanHoi、@johankasperi、@yalanyali、@gabrieldonadel 首次贡献。
- 🔗 **来源与下载**：见 GitHub v1.0.0 release notes，完整变更对比 v0.2.1...v1.0.0，并提供 Release card 下载。

---

### [](https://swmansion.com/changelog/react-native-screens-4-29-0/)

**原文标题**: [React Native Screens 4.29.0](https://swmansion.com/changelog/react-native-screens-4-29-0/)

react-native-screens 4.29.0 是 2026 年 10 月 9 日发布的次要版本，重点包括 iOS Tabs 迁移至 UITab API、新增多个 Tabs/Stack 属性，并强化 Android Fragment 生命周期与修复 iOS form sheet 滚动问题。

- 🧭 iOS Tabs：在 iOS 26.1 及以上迁移到 UITab API（#4675）。
- ➕ Tabs 新属性：支持 tabBarHiddenAnimationEnabled、tabBarSidebarPreferredPlacement、automaticallyActivatesSearch（基于 UISearchTab）。
- 🎨 Tabs 图标：支持自定义 drawable/符号图标，可按槽位着色、按标签调整尺寸，并提供 iOS 回退方案。
- 🏷️ Stack v4（iOS）：头部项新增 visibilityPriority 属性。
- 🤖 Android 修复：Fragment 恢复兼容 R8，清理孤立 Fragment，实例销毁时 setupFabric 不再崩溃。
- 📜 iOS 修复：form sheet 不再错误调整/缩放 ScrollView，pop 动画结束后向 JS 发送 dismiss 事件。
- 📱 Tabs 修复：避免首次渲染触发隐藏动画，统一底部附件宽度，UITab API 下隐藏侧边栏 Edit 按钮。
- 🔄 其他 Android 修复：旋转后恢复触摸坐标，隐藏标签栏不再拦截触摸，Stack v4 分离屏幕不更新头部。
- 🧪 杂项：示例默认使用 scene 生命周期，移除无用 ScreenModalFragment，并调整测试位置。
- 🔗 来源：4.29.0 release notes；完整变更见 4.28.0...4.29.0。

---

### [发布 v0.28.0 · software-mansion/argent · GitHub](https://github.com/software-mansion/argent/releases/tag/v0.28.0)

**原文标题**: [Release v0.28.0 · software-mansion/argent · GitHub](https://github.com/software-mansion/argent/releases/tag/v0.28.0)

Argent v0.28.0 已发布，为最新版本，包含自 v0.27.0 以来的 22 个提交，主要带来 iOS 启动参数、UI 树信息增强、流程远程执行与失败截图、MCP/CLI 修复，并由 szdziedzic、hubgan 和 filip131311 贡献。

- 🚀 版本发布：v0.28.0 于 10 月 9 日 20:47 发布，包含 22 个提交，仓库为 software-mansion/argent。
- 📱 iOS 启动参数：支持在流程 launch 步骤、物理 iPhone 和链接流程中传递，并提示数字或布尔参数需加引号。
- 🌳 UI 树增强：iOS 新增类型、密码、占位符、隐藏、前台 App 和远程模拟器支持；Android 新增占位符、可编辑、隐藏、标题、键盘和前台 App 支持。
- 🧰 工具与注册表：callTool 工具名与参数支持类型；新增 hideFromMcp 隐藏工具；新增仅 SDK 可用的 ui-tree 工具。
- 🔗 链接运行流程：支持自包含流程、run/snapshot/tool 片段、嵌套流程记录与回放，以及文件参数随调用上传。
- 🖼️ 失败截图：流程失败时附加截图，并可通过 --output 导出失败步骤截图。
- 🛠️ 修复改进：CLI 重新链接同一地址时保存新 token；安装器探测更安全；MCP 工具调用经 @argent/tools-client 上传文件输入。
- 🤖 Android DevTools：helper 升至 versionCode 2，并拒绝与清单不匹配的 release APK。
- 📝 文档与杂项：Node 客户端页面改称 Argent SDK；添加 mcprush 列表声明 token；CI 重试与 npm staged 版本冲突的 canary。
- 👥 贡献者：filip131311、hubgan、szdziedzic；@szdziedzic 在 #843 首次贡献。
- 📜 完整变更日志：v0.27.0...v0.28.0。

---

### [](https://expo.dev/changelog/native-crash-reporting-in-eas-observe)

**原文标题**: [Native crash reporting in Expo's Observability service — Expo changelog](https://expo.dev/changelog/native-crash-reporting-in-eas-observe)

EAS Observe 现在会在 JavaScript 错误之外记录原生崩溃；在 SDK 57 上更新到 57.0.21 或更高版本即可启用，无需额外配置，支持 Android 和 iOS。
- 📦 更新到 SDK 57 的 57.0.21 或更高版本以启用原生崩溃记录。
- 🧠 此前 Errors 页面只显示 JavaScript 错误，原生代码崩溃会导致应用退出且没有记录。
- 🤖 Android 覆盖未捕获的 Java/Kotlin 异常，以及 Android 11 及更高版本中系统保留的崩溃记录。
- 🍎 iOS 覆盖 Mach 异常（如 EXC_BAD_ACCESS）、Unix 信号（如 SIGSEGV），以及未捕获的 Objective-C/Swift 异常。
- 📋 原生崩溃与 JavaScript 错误会出现在同一列表中，可按来源筛选，也能查看无崩溃会话的整体情况。
- 🔍 打开崩溃可查看堆栈跟踪、导致崩溃的会话记录，以及按应用版本、操作系统、设备和国家的细分。
- 🤝 在错误详情页选择“Hand off to AI”，可将崩溃及其上下文发送到 Claude Code 或 Codex。
- 🧪 错误报告功能目前处于预览阶段，可查阅错误报告文档。

---

### [](https://github.com/callstackincubator/rozenite/releases/tag/v2.5.0)

**原文标题**: [Release v2.5.0 · callstackincubator/rozenite · GitHub](https://github.com/callstackincubator/rozenite/releases/tag/v2.5.0)

Rozenite v2.5.0 已发布，重点围绕 React Native 与 Lynx 重新定位，并集中改进 CLI、Agent 契约、插件、UI 与网站，同时修复多平台兼容和安全问题。

- 🚀 v2.5.0 于 10 月 12 日发布，提交 f3d34eb，包含 3 个资产。
- 📝 文档重新定位 Rozenite，聚焦 React Native 和 Lynx；新增 Agent 列表契约、CLI grammar v3 和主机协议相关 ADR。
- 🧩 CLI 可在 `rozenite init` 中检测 Lynx（rspeedy）项目，并推出 agent grammar v3，支持隐式会话和基于 schema 的 flags。
- 🔌 插件目录新增 `rozenite-i18n-devtools`；Redux DevTools 插件新增 `actionsDenylist` 与 `actionsAllowlist` 选项。
- 🌐 网络活动插件重写为 XHR-first HTTP 捕获，并修复 `fetch` 传入的 Request body 捕获。
- 🛡️ Electron 更新以修复 CVE；修复含 emoji 的主机到设备消息被丢弃问题。
- 🪟 修复多项 Windows 兼容问题：Vite 插件路径、web 构建脚本、Metro release-bundle fixture。
- 🧱 统一 Agent 分页默认 20、最大 100；限制并裁剪内置 Agent 域载荷，限制会话启动并超时 CDP 命令。
- 📦 官方插件迁移到共享列表契约并限制大读取；统一 Rozenite host protocol 与 app/agent 握手。
- 🎨 网站迁移到 Astro 并重新设计，插件目录使用构建时真实数据，移除 violet；DevTools 面板 UI 与 rozenite.dev 设计统一。
- 🧰 SQLite 和 Network Activity 面板迁移到 `@rozenite/ui`，并让 `@rozenite/ui` 支持 tree-shaking。
- 🚢 发布流程仅发布消费者所需内容，移除 development condition；版本化依赖安装后再并行检查。
- 👥 新贡献者：@hdjvieira、@sbaiahmed1、@theluckystrike；贡献者包括 V3RON、hdjvieira 等。
- 🔗 完整变更日志：v2.4.0...v2.5.0。

---

### [](https://github.com/nandorojo/galeria/releases/tag/v3.1.0)

**原文标题**: [Release v3.1.0 · nandorojo/galeria · GitHub](https://github.com/nandorojo/galeria/releases/tag/v3.1.0)

nandorojo/galeria 发布 v3.1.0 最新版本，主要新增跨平台照片与视频图库功能，并修复 Android、iOS、Web 多个问题，同时迎来多位首次贡献者。

- 🚀 v3.1.0 由 gtokman 于 10 月 12 日 16:58 发布，提交为 b6f38e3，并带有 GitHub 已验证签名。
- 🖼️ 新增照片和视频图库，支持 iOS、Android 和 Web（#132，@erickreutz）。
- 🤖 Android：当 AGP 注册 kotlin 扩展时，跳过显式 Kotlin 插件（#130，@gabrieldonadel）。
- 🍎 iOS：图片查看器支持加载 data: URL（#134，@huytdps13400）。
- 🐛 iOS：修复无效图像帧导致查看器卡住的问题（#131，@PhilCantrel）。
- 🌐 Web：Web 实现不再导入 react-native（#133，@huytdps13400）。
- 👥 新贡献者：@gabrieldonadel、@huytdps13400、@PhilCantrel、@erickreutz 首次贡献。
- 📜 完整变更日志：v3.0.3...v3.1.0；贡献者共 4 人，发布资产 2 个；获得 1 个 🚀 反应。

---

### [](https://www.youtube.com/watch?v=dj6fhEwXZ6I)

**原文标题**: [Ten Agents Waiting for Input: Tzvetan Mikov on AI Coding and Hermes - YouTube](https://www.youtube.com/watch?v=dj6fhEwXZ6I)

该内容主要是 YouTube/Google 页面底部的导航与法律信息，涵盖平台介绍、用户支持、创作者与开发者资源、广告合作、政策条款、版权声明，并标注 © 2026 Google LLC。

- 🏢 关于：平台或公司背景介绍
- 📰 新闻：官方动态与媒体信息
- ©️ 版权：知识产权与版权说明
- 📞 联系我们：提供联系渠道
- 🎬 创作者：面向内容创作者的支持
- 📣 广告：广告合作与投放信息
- 💻 开发者：开发者相关资源
- 📜 条款：服务条款与使用规则
- 🔒 隐私：隐私政策说明
- 🛡️ 政策与安全：平台规范与安全指南
- ⚙️ YouTube 运作方式：平台机制说明
- 🧪 测试新功能：体验与反馈新特性
- 🏛️ © 2026 Google LLC：版权归属信息

---

### [](https://infinite.red/react-native-radio/rnr-375-rnr-explains-ota-updates)

**原文标题**: [React Native Radio - RNR 375 - RNR Explains: EAS Update](https://infinite.red/react-native-radio/rnr-375-rnr-explains-ota-updates)

本期《React Native Radio》第375集由 Robin Heinze 和 Mazen Chami 讲解 Expo 的 EAS Update：它如何为 React Native 应用提供 OTA（空中更新），让 JavaScript 包无需应用商店审核即可替换，并说明可安全发布的内容、更新到达用户的流程、runtime version 与回滚机制。

- 🎙️ 本集是 RNR Explains 系列，主题是 OTA 更新；Robin 是 Infinite Red 工程总监，Mazen 是高级软件工程师，赞助商为 Infinite Red。
- 🚀 OTA 更新是 React Native 的“超能力”：通过替换 JS bundle，在不提交新版本到应用商店的情况下发布变更。
- ⚠️ 但不能用来绕过商店审核；适合修 JS 相关崩溃、文案/样式/业务逻辑等小改动，仍应正常走商店发布。
- 📜 历史背景：微软 CodePush 曾是事实标准，2025 年停止支持；后来 Codemagic 让其复活，而 Expo EAS Update 是当前主流方案。
- 🧱 原理：原生层包含 Swift/Java/Kotlin、权限等；JS 层包含组件、逻辑、样式、图片、字体；React Native 将 JS 编译成 bundle 嵌入二进制。
- 🔗 启用 OTA 的应用启动时会检查 manifest URL：有新版就下载到私有存储，后续启动从缓存加载；没有则使用内置的“首日回退”bundle。
- 🏠 manifest URL 和 bundle 可由 EAS 托管，也可自托管；更新不是实时流式加载，而是下载一次、缓存本地。
- ⚡ SDK 55+ 与 Hermes 字节码差分可只下载增量 diff，而不是完整 bundle，提升速度和弱网体验。
- 🔄 生命周期：启动检查→下载→应用；应用后通常需冷启动或调用 Updates.reloadAsync 才生效，可能造成闪屏/重开，也可设计为静默更新或强制更新。
- 🧩 runtime version 是兼容性关键：build 和 update 必须完全匹配；原生代码或配置变化时要提升版本，防止不兼容 bundle 被应用。
- 🌿 channels 是构建监听的更新流（如 production/preview/alpha）；branches 更细粒度，可用于 A/B 测试或功能分支，但实际中很多人只用 channels。
- 🚀 发布命令是 eas update：执行 expo export 打包 JS，并上传到 Expo 服务器，由 manifest URL 引用；Expo 仪表盘提供 rollout 和统计等能力。
- 🛡️ 安全机制：新 bundle 若 10 秒内崩溃会自动回滚到最后可用版本；下载失败回退到内置 bundle；还可手动回滚，但回滚同样需要冷启动生效。
- 🧪 实践案例：Chain React 2024 应用完全使用 EAS，并在大会期间推送过一次更新测试；Discord 等 RN 应用也使用 OTA 更新体验。
- ✅ 结论：EAS Update 让 React Native 能快速修复和迭代 JS 层问题，但必须清楚安全边界、兼容性和用户体验，不能替代原生构建与商店审核。

---

### [](https://github.com/whatwg/html/pull/13063)

**原文标题**: [AsyncContext proposal integration by nicolo-ribaudo · Pull Request #13063 · whatwg/html · GitHub](https://github.com/whatwg/html/pull/13063)

该 PR #13063 旨在将 TC39 AsyncContext 提案集成到 HTML 规范中，让异步执行流关联的 JavaScript 状态能在多种异步延续中保存和传播，并覆盖回调、脚本、事件等场景。

- 🧩 由 nicolo-ribaudo 发起，计划将 19 个提交合入 whatwg/html:main。
- 📚 集成内容包括：对提案的基本引用、通过回调表示完成的 API 传播、顶层脚本执行传播，以及通过触发事件的 API 传播。
- ✅ PR 大部分工作集中在事件传播；许多 API 无需修改，因为它们是同步的，或事件本应运行在空上下文中。
- 🧭 设计遵循既往 WHATNOT 会议决策，并记录在 AsyncContext 的 WEB-INTEGRATION.md 与 html__events.md 中。
- 🚧 尚未处理自定义元素和 `[CEReaction]` 相关传播，作者仍在继续开发。
- 🌿 作者维护了平行的 gh stack PR，便于审查具体修改原因与 WPT 测试细节。
- ❓ 开放问题包括：是否自动通过 `queue a microtask` 传播；是否采用 `[PropagatesAsyncContextToEvents]`；`<img>` 和媒体元素时序；媒体算法重构；EventSource 连接期间保持上下文是否可行。
- 🔗 需与 whatwg/webidl#1568、whatwg/dom#1451 同步落地，另有待开的 WebIDL PR 用于捕获 WebIDL 管理 Promise 的拒绝上下文。
- 🧪 至少两个实现者感兴趣且无人反对；WPT 测试已编写；Chromium、Gecko、WebKit、Deno、Node.js 等实现问题已提交。
- 🛠️ 具体覆盖 microtasks、timers、延迟脚本、focus/blur，以及 style、link、img、iframe、embed、object、input type=image、EventSource、details/dialog/popover、track、media、Worker 等事件传播。
- 📌 还暴露 Promise 拒绝事件和 error 事件的 Async Context Mapping；相关处理依赖 tc39/proposal-async-context#148 与 #150 被接受。
- ⚠️ PR Preview 因 Wattsi Server 返回 503 而构建失败，属于外部服务问题；当前无评审、无分配、无标签和里程碑。

---

### [Deno 加入 Cloudflare | Deno](https://deno.com/blog/cloudflare)

**原文标题**: [Deno is joining Cloudflare | Deno](https://deno.com/blog/cloudflare)

Deno 团队将整体加入 Cloudflare，未来开发重点转向基于 Cloudflare Workers 与 Durable Objects 的共享平台，不再继续独立开发 Deno 运行时和托管服务。现有 Deno 运行时、Deno Deploy、JSR 等将有明确的过渡安排。

- 📅 2026年10月9日，Ryan Dahl 宣布 Deno 团队整体加入 Cloudflare。
- 🛠️ Deno 多年来致力于简化服务器软件开发，涵盖模块分发、安全运行时、完整工具链、独立可执行文件与 Node.js 兼容。
- ☁️ Deno Deploy 让应用部署更简单，但也暴露出底层复杂性；celld 基于 Cloudflare Workers 编程模型，将扩展能力内建到编程模型中。
- 🤝 加入 Cloudflare 后，将与 Workers 和 Durable Objects 团队合作，目标让该编程模型成为构建服务器的默认方式。
- 🌐 这一模式既适用于 Cloudflare 网络，也适用于用户自有基础设施。
- ⚠️ 这是重大变化：未来开发将投入共享平台，而非继续开发独立运行时和托管服务。
- ⏳ Deno 运行时将继续支持一年，每月发布错误修复和安全更新；之后停止开发。
- 🔓 Deno 将保持开源，欢迎其他人继续推进其开发。
- 🚚 Deno Deploy 将继续运行六个月后关闭；付费客户迁移到 Cloudflare Workers 将获得支持。
- 📦 JSR 将继续运营，其基础设施迁移到 Cloudflare。
- 🧩 继续支持 rusty_v8，并推动将其集成到 workerd。
- 🤖 AI 需要更好的抽象；Durable Objects 适合 agent harness，具备低成本无服务器执行、持久状态、WebSockets 和高层 JavaScript 接口。
- 🎯 celld 因此聚焦 Durable Objects；Ryan Dahl 与 Kenton Varda 在 Cloudflare 博客联合发文说明更多。
- 📧 若要在自有基础设施上大规模运行 agents，可联系 ry@cloudflare.com。

---

### [](https://lea.verou.me/blog/2026/icons/)

**原文标题**: [
		The best way to use icons in Web UIs • Lea Verou](https://lea.verou.me/blog/2026/icons/)

overview summary
本文介绍一种纯 CSS 图标系统：将图标作为设计令牌存为 `--icon-*` 自定义属性，通过伪元素、mask 和 style queries 按需插入与覆盖，无需改动 HTML。文章讨论设计原则、实现细节、Safari 兼容变通、当前局限与未来 CSS 特性，并发布 `@nudeui/icons` 包。

- 🎯 目标：让图标完全由 CSS 插入和调整，比内联 SVG 更灵活、可维护，且无需触碰 HTML。
- 🧩 设计原则：高信噪比、简单默认、复杂可覆盖、无可用性悬崖，同时保持性能与一致性。
- ⚠️ 现有方案问题：内联 SVG 样板多且易不一致；图标字体有下载、回退、屏幕阅读器和用户字体覆盖等问题。
- 💡 CSS 优势：支持响应式聚合，可基于选择器、交互状态、媒体查询、容器查询、书写模式等动态增删改图标。
- 🗂️ 图标即设计令牌：在 `:root` 定义 `--icon-trash` 等变量，存内嵌或远程 SVG 的 `<image>` 值，由设计系统统一管理。
- 🧱 核心机制：伪元素设为 `1em` 方块，`background: currentColor`，`mask: var(--icon-start)` 等，用 `--icon-start`、`--icon-end` 指定图标。
- 🎛️ 高层属性 `--icon`：组件可将其重定向到 `--icon-start`、`--icon-end`、`--icon-marker`，支持悬停、深色模式、打印等条件覆盖。
- 🧪 条件插入：用 `@container style(--icon-start)` 仅让真正有图标的元素生成伪元素，配合 `@property` 防止继承污染。
- 🛠️ 抛光细节：可定制颜色、尺寸、偏移、间距；`pointer-events:none`、`flex:none`、垂直对齐、`forced-color-adjust`、alt 文本提升无障碍。
- 🐞 Safari 兼容：发现并绕过 WebKit 三个 bug，包括零时长动画强制重新解析、非继承注册属性 `inherit` 不可靠等。
- 🌐 远程图标注意：相对 URL 基于使用图标的 CSS 文件解析，建议根相对路径，或用 `@property` + `initial-value` 注册。
- ⛔ 当前局限：只能单色遮罩；不能给伪元素单独加背景或边框；任意动画仍需内联 SVG。
- 🚀 未来特性：CSS Linked Parameters 可定制 SVG 参数，`ident()` 可用标识符代替变量，`@mixin` 集中伪元素样式，更简 `@property` 语法。
- 📦 可用工具：作者发布 `@nudeui/icons` 包，包含图标系统与 `.icon`、`.icon-start`、`.icon-end` 回退类，可立即使用。

---

### [终于能适配其内容的 iframe](https://alfy.blog/2026/10/09/iframe-that-finally-fit-their-content.html)

**原文标题**: [Iframes that finally fit their content](https://alfy.blog/2026/10/09/iframe-that-finally-fit-their-content.html)

Chrome 154 推出 `frame-sizing`，让跨域 iframe 能自动匹配内容高度，减少传统 postMessage 测量和 resize 脚本；但需要 iframe 内页面通过 meta 标签授权，并在内容变化时调用 `requestResize()`，目前仅 Chromium 支持。

- 🧩 核心用法：父页给 iframe 加 `frame-sizing: content-height`，浏览器即可根据内容调整高度，无需消息监听和 origin 检查。
- 📜 配合条件：iframe 内页面必须在 `<head>` 中放置 `<meta name="responsive-embedded-sizing" content="allow-origins=https://shop.example">`，且必须初始 HTML 就有，后加 JS 无效。
- 🔁 动态内容：内容后续变化时，嵌入页调用 `window.requestResize()`，浏览器重新测量；因此并非完全不需要 JavaScript。
- 📐 可选值：`frame-sizing` 还支持 `content-width`、`content-inline-size`、`content-block-size`，多数场景用 `content-height`，可配合 `max-height` 限制。
- 🧮 旧方案：过去由于父页无法读取跨域 iframe 内容高度，只能靠子页测量 `scrollHeight` 并 `postMessage`，父页再设置高度。
- ⚠️ 旧问题：宽度变化、字体/图片延迟加载、动态显示隐藏、多个 iframe 需标识、第三方不配合等，都会让高度测量变得不可靠。
- 💳 支付表单：错误提示、钱包切换、保存卡列表都会改变高度，但只有支付提供商能添加 meta 并调用 `requestResize()`，因此关键在供应商是否支持。
- 🧾 第三方组件：评论、联系表单、订阅、预订等小部件适合采用，因为服务商控制嵌入页，且 `allow-origins` 可列出允许的客户站点。
- 🪜 多步表单/问卷：每步高度不同，可在切换步骤后调用 `requestResize()`，避免预留最高步骤空间或出现内部滚动条。
- 🧑‍💻 自有内容：用 `srcdoc` 渲染邮件预览、富文本或代码演示时最容易采用，因为嵌入 HTML 由自己控制，可直接加 meta。
- 🌐 兼容与回退：目前仅 Chromium 支持；应默认设固定高度，再用 `@supports (frame-sizing: content-height)` 渐进增强，并检查 `requestResize` 是否存在。
- 📉 布局偏移：iframe 加载后增长会推移下方内容，可能影响 Core Web Vitals，建议设置 `min-height` 减少跳动。
- 🔒 安全注意：不要无理由使用 `allow-origins=*`，高度可能泄露登录状态等信息；只列出必要站点，并与 CSP `frame-ancestors` 配合。
- 🏁 结论：浏览器接管了繁琐的测量工作，但生态支持取决于嵌入页面方；支付网关、评论服务和 widget 提供商应主动支持，才能让嵌入体验更无缝。

---

### [JPEG XL 终于登陆 Chrome！](https://tonisagrista.com/blog/2026/chrome-jpegxl/)

**原文标题**: [JPEG XL finally lands in Chrome!](https://tonisagrista.com/blog/2026/chrome-jpegxl/)

Chrome 155 将正式内置 JPEG XL 解码器，结束多年来围绕该格式的争议；在 Firefox 推进默认支持、Safari 仍仅部分支持的背景下，这被视为 JPEG XL 走向主流和开放网络的重要胜利。

- 🚀 Chrome 155 将搭载 JPEG XL 解码器，作者称“Google kills JPEG XL”的黑暗时代结束。
- 📰 消息来自 Hacker News 上的 Chrome 公告，经确认并非玩笑。
- 🖼️ JPEG XL 支持较 JPEG 减少约 20–60% 体积、无损 JPEG 转码、渐进解码、广色域、HDR、32 位、动画和透明度。
- 📸 它在高保真摄影、无损压缩、渐进解码方面优势明显，支持最高约 1 terapixel 图像，编码/解码较快，且免版税、FOSS。
- 🌐 Chrome 约占 66.5% 浏览器市场份额，其支持被看作该格式成为主流的关键最后一块拼图。
- 🗣️ Chrome 转向的原因是 Web 开发者持续反馈与 Interop 2026 中的高人气，社区压力促成支持。
- 🦀 实现上集成纯 Rust 解码器 jxl-rs，规避 C++ 解码器的内存安全攻击面，并用 jxl_simd 提升性能。
- 🔁 无损转码现有 JPEG 可无像素损失升级旧图库，同时节省磁盘空间和带宽。
- 🦊 Firefox 158 将默认启用 JPEG XL；Safari 仅部分支持，是主要例外。
- 🛠️ 作者建议开始转换图库、更新 `<picture>` 标签并开始提供 `.jxl` 文件。

---

### [](https://developer.mozilla.org/en-US/docs/Mozilla/Firefox/Releases/158)

**原文标题**: [Firefox 158 release notes for developers (Stable) - Mozilla | MDN](https://developer.mozilla.org/en-US/docs/Mozilla/Firefox/Releases/158)

overview summary
Firefox 158 于 2026 年 10 月 13 日发布，主要面向 Web 与附加组件开发者，带来 CSS、HTTP、API、DOM、WebRTC、WebDriver 等更新，并默认启用 JPEG XL，同时加入多项默认关闭的实验功能。

- 📅 Firefox 158 稳定版发布，重点更新面向开发者。
- ♿ Firefox for Android 支持 `aria-busy`，便于辅助技术等待内容更新完成后再通知用户。
- 🧮 CSS 支持类型化算术，`calc()` 可对同数据类型但不同单位的值做除法并生成无单位结果。
- 🌐 HTTP 图片请求默认 `Accept` 头加入 `image/jxl`，默认值包含 `image/avif,image/jxl,image/webp,image/png,image/svg+xml,image/*;q=0.8,*/*;q=0.5`。
- 🧩 API 更新包括：`WebTransport.getStats()`、`WebTransport.supportsReliableOnly`、通知 `navigate` 选项、WebGPU 的 `float32-blendable` 与 macOS `clip-distances`、WebGL `EXT_polygon_offset_clamp`、`PerformanceResourceTiming.deliveryType` 支持 `cache`。
- 📐 DOM 更新包括：`SVGGraphicsElement.getBBox()` 对 `<tspan>` 和 `<textPath>` 支持 `fill`/`stroke`；HTML Sanitizer 支持 `javascriptURLs` 配置与 `Sanitizer.setJavascriptURLs()`。
- 📹 WebRTC 发送 H.264/AV1 时会按协商的编解码器级别降低分辨率与帧率；`MediaCapabilities.encodingInfo()` 可报告 `webrtc` 配置支持。
- 🤖 WebDriver：BiDi 与 Marionette 可设置摄像头/麦克风权限；触摸容差变为零；BiDi 截图支持 `imageSize`，录屏支持 `destinationFolder`；Marionette 零尺寸截图会报错。
- 🖼️ JPEG XL（`image/jxl`）默认启用，支持有损/无损压缩、透明、动画、HDR，并可无损转码现有 JPEG。
- 🧩 附加组件：`publicSuffix.isKnownSuffix()` 对无效主机名改为抛错；新增 `runtime.getVersion()` 返回扩展清单版本。
- 🧪 实验功能默认关闭，需通过 `about:config` 启用：`random()` CSS 函数、`corner-shape`、`import defer`、本地语音识别、Speculation Rules 的 `moderate`、流式请求体、`CSSNumericValue.equals()`。
- 📝 HTML 与 JavaScript 无重大变化；MDN 页面最后修改于 2026 年 10 月 12 日。

---

### [](https://bun.com/blog/bun-v1.4.3)

**原文标题**: [Bun v1.4.3 | Bun Blog](https://bun.com/blog/bun-v1.4.3)

Bun v1.4.3 于 2026 年 10 月 10 日发布，最大亮点是内置 TypeScript 类型检查器 bun check；它移植自 typescript-go，通过 TypeScript 7.0.2 全量一致性测试，速度与内存显著优于 tsc。版本还带来运行时、HTTP、构建、安装、编译、Node.js 兼容性、安全与 Web API 的大量改进和修复。

- 🚀 **发布与升级**：Bun v1.4.3 由 Jarred Sumner 发布；支持 curl、npm、PowerShell、Scoop、Homebrew、Docker 安装，使用 `bun upgrade` 升级。
- 🧠 **bun check**：内置 TypeScript 类型检查器，读取 `tsconfig.json`，报告与 `tsc` 相同错误，不需要安装 `typescript`；只检查类型，不输出 JS/`.d.ts`，也没有语言服务器。
- ⚡ **检查性能**：`bun check` 比 `tsc 7.0.2` 快 3x–6.4x，内存少 2.2x–4.9x；使用所有 CPU 核心。
- ✅ **检查集成**：支持 `bun run --check`、`bun test --check`、`bun build --check`、`Bun.build({ check: true })`；类型错误会阻止运行、测试或构建。
- 🧪 **一致性验证**：通过 51,210 项 TypeScript 7.0.2 一致性测试；在 72 个开源项目、1,103 份配置中，1,102 份输出与 `tsc` 完全一致，286,267 条错误仅 1 处不匹配；另有大量 fuzz 和 mutation 测试。
- 🖥️ **运行时省电与请求会话**：服务器空闲时 CPU 降低 67–89%；新增 `Bun.FetchSession`，为请求组隔离 TLS、代理、keep-alive 和连接池。
- 🌐 **fetch 代理增强**：`NO_PROXY` 支持通配符、CIDR、裸 IPv6、`host:port`；支持 `ALL_PROXY`、单请求 `proxy: false`；代理 `CONNECT` 失败会抛 `ERR_PROXY_TUNNEL`。
- 🧩 **实验性 Bun.ModuleGraph**：单进程可运行多个应用实例，拥有独立模块状态、`require.cache`、定时器和 I/O，并共享解析代码/字节码；不是安全沙箱。
- 🔒 **禁用字符串代码生成**：`--disallow-code-generation-from-strings` 阻止 `eval()` 和 `new Function()`；`=strict` 还阻止 `node:vm`、`data:` 导入、`Worker(eval)`、`module._compile()`、N-API 脚本等。
- 🚄 **HTTP 与 JSC 升级**：`node:http`/`Bun.serve` 超过 16KB 的响应最高快 2.7x，`Bun.serve` 支持 `If-Range`；JavaScriptCore 提升 `JSON.parse`、正则、数组、`for...of`/解构等性能并修复规范问题。
- 📦 **bun install**：无锁文件时跳过不会安装的 tarball（bundled 依赖、其他平台、`--production`/`--omit` 排除项），显著减少下载量。
- 🏗️ **bun build**：多入口/分包构建内存大幅降低；支持 `[hash9]`–`[hash13]` 输出名避免重名；metafile 为分包 `import()` 标注 `entryPoint`。
- 🧊 **bun build --compile**：新增 `--bytecode-order` 按真实运行 profile 布局字节码，冷启动 1.01s→0.53s、常驻字节码内存 59.5MB→20.5MB；ESM + bytecode 启动更快，新增 `--compile-jit-policy`。
- 🛠️ **性能修复与依赖更新**：修复 `crypto.randomInt` 约 20x 变慢、zstd/zlib/color/transpiler/vm 性能回归；GC 更及时归还内存；更新 SQLite、libarchive、brotli、根证书和 Alpine 镜像等。
- 🔐 **安全与 Node.js 兼容**：TLS 握手期验证、证书名匹配 CVE-2026-48618、HTTP/2 reset 限流 CVE-2023-44487/CVE-2025-8671；大量修复 `node:http`、`http2`、`tls`、`net/dns`、`child_process`、`vm`、`fs`、`crypto` 等行为。
- 🌍 **Web API 与工具链**：修复 `fetch`、WebSocket、streams、TLS，以及 transpiler、bundler、minifier、CSS 解析、`bun test`、Bun Shell、SQL/SQLite/S3 客户端、TypeScript 类型和 Windows 问题。

---

### [](https://github.com/pingdotgg/ts-rust)

**原文标题**: [GitHub - pingdotgg/ts-rust: An experimental Rust port of the TypeScript 7 compiler (tsc) · GitHub](https://github.com/pingdotgg/ts-rust)

ts-rust（tsc-rs）是由 pingdotgg 发起的一个实验性项目，尝试用 LLM 将微软的 TypeScript 7 原生编译器（原本用 Go 编写）移植到 Rust，并以 tsc 命令行、语言服务器与 API 保持一致为目标。

- 🦀 **项目定位**：这是 Microsoft 原生 TypeScript 编译器（Go 版，前身 typescript-go）的直接 Rust 移植，保留 Go 算法与行为，命令行、LSP 和 API 均对齐 tsc。
- 🤖 **LLM 移植实验**：作者最初用 GPT-5.6 Sol / GPT 6 Astra 等 OpenAI 模型耗费超 40 万美元 token，写了 130 万行 Rust 却只到约 84% 兼容；改用 Opus 5.5 后从头重写，10 小时出可运行 v0，两周 API 花费约 24,047 美元。
- ⚡ **性能领先**：在 T3 Code 带 Effect 诊断的完整类型检查中，tsc-rs --fast 用时 9.77s，是 tsc 7 的 4.35 倍速，tsc-rs 默认模式为 2.98 倍速，远超 bun check（0.72×）和 tsc 6（0.22×）。
- 📊 **真实应用基准**：在六个开源项目上，tsc-rs 0.6.0 几何平均比 tsc 7 快 2.10 倍，--fast 快 2.90 倍，Bun 快 3.29 倍；VS Code 检查从 9.57s（tsc 7）降到 2.64s（--fast）。
- ✅ **高度兼容**：全部 184,749 个移植的 Go 测试通过，语言服务器与 API 在 oracle 测试集上与 Go 一致；在 120 个开源仓库中命令行输出仅在上述已知问题处与 Go 不同。
- 🔌 **内置 Effect 诊断**：直接内置 Effect 语言服务诊断（377xxx 代码），无需第二个编译器；移植自 Effect-TS/tsgo 0.51.1，含悬停、内联提示、快速修复、补全、重构等编辑器功能。
- 🚀 **加速开关**：--fast（或 GOPORT_FAST=1）启用更多检查器与并行，每个核心一个检查器（最多 16 个，每 32 个源文件最多一个，不少于 Go 的 4 个）；另有 GOPORT_FAST_STEAL、--checkers N、GOPORT_LAZY_MEMBERS、GOPORT_FAST_NEVER_ORDER 可选。
- 📦 **安装与平台**：npm 包名为 tsc-rs（避免与 typescript 冲突），用法 `npm install -D tsc-rs` 后 `npx tsc-rs -p tsconfig.json`；支持 Linux x64/arm64、macOS arm64/x64、Windows x64/arm64（0.2.0 后）。
- 🧩 **WASM 与架构**：crates/ts_wasm 提供 WebAssembly 构建；核心编译器在 crates/ts_goport，分为 goport_core、goport_util、goport_lsproto 三部分，配套代码生成工具与 lib 快照。
- ⚠️ **已知问题**：部分 monorepo 中 node_modules 与直接导入双重可达时可能多写输出并报 TS6059；tsc -b 中无项目引用的跨项目导入可能读到旧/缺失输出；编辑器长会话内存增长略高于 tsc；`--version` 打印的是移植的 TypeScript 版本（7.1.0-dev）。
- 📜 **许可证**：MIT，同时保留所移植代码的许可证与声明（TypeScript Apache-2.0、部分 Go 标准库 BSD-3-Clause），见 NOTICE.md。
- 📌 **状态与警告**：这是早期版本，在测试过的真实项目中 100% 兼容，可作为多数应用的 drop-in 替代；作者坦言自己从未读过一行代码，使用时需谨慎。

---

### [发布 v1.64.0 · microsoft/playwright · GitHub](https://github.com/microsoft/playwright/releases/tag/v1.64.0)

**原文标题**: [Release v1.64.0 · microsoft/playwright · GitHub](https://github.com/microsoft/playwright/releases/tag/v1.64.0)

Microsoft Playwright 发布 v1.64.0，重点带来 WebMCP 支持、视频录制增强、测试运行器改进、Locator.within()、新 API 以及若干破坏性变更，并更新了浏览器版本。

- 🧰 WebMCP：新增 page.webmcp 与 frame.webmcp，可列出并调用页面注册的工具；Playwright MCP 默认支持 webmcp_<tool>，CLI 提供 webmcp-list 和 webmcp-call。
- 🎬 视频增强：支持自定义 fps，动作标记可用 CSS 自定义，光标保留并平滑移动，改用 VP9 编码以降低 CPU 并缩小文件；MCP 与 CLI 也支持相关选项。
- 🎯 测试运行器：新增 testProject.default、--shuffle、test.describe.configure 的 lock，以及 toHaveScreenshot 的 WebP 类型配置。
- 🪆 Locator.within()：可组合两个定位器并按自然顺序限定范围；nth/first 等相对定位器会在每个父级内分别解析。
- 🆕 新 API：page.getByRef()、content() 的 includeShadow、虚拟凭证 signCount、fullConfig.filteredProjects，以及 apiRequestContext 的 Cookie 管理方法。
- ⚠️ 破坏性变更：screen 从设备描述符转发；测试文件 JSX 遵循 tsconfig.json；--update-snapshots=missing 现在通过；隐藏 iframe 内元素视为隐藏。
- 🌐 浏览器版本：Chromium 156.0.8078.4、Firefox 157.0、WebKit 27.2，并兼容 Chrome 155 与 Edge 155。

---

### [博客 | pnpm](https://pnpm.io/blog?type=releases)

**原文标题**: [Blog | pnpm](https://pnpm.io/blog?type=releases)

本批发布涵盖 pnpm 12.13.0 到 11.28.5，重点包括新增 profile/token 命令、远程缓存、Rust 工具链、实验性 node linker、安全修复，以及性能与发布流程改进。

- 🚀 pnpm 12.13.0（2026-10-13）：新增 `pnpm profile` 和 `pnpm token` 命令，支持 `storeIndexFormat: files` 用于网络文件系统共享存储，并加快 Python 依赖解析。
- 🔐 pnpm 12.12.1（2026-10-11）：`pnpm dist-tag` 支持 OIDC 认证，新增 `tool:` 协议；`pnpm publish` 使用 `NPM_ID_TOKEN` 前会检查其签发 registry。
- 🌐 pnpm 12.12.0（2026-10-10）：通过远程缓存共享任务结果和依赖构建；新增 `addMissingPeerTypes`；`pnpm add --config` 与 `pnpm update` 可管理配置依赖；修复 `dangerouslyAllowAllBuilds` 与 `allowBuilds` 的冲突。
- 🛠️ pnpm 12.11.2（2026-10-09）：修复 `--workspace-concurrency=Infinity`、`updateConfig` hook 设置的过滤器，以及 `enable-modules-dir=false` 时的 store 拉取问题。
- 🧰 pnpm 12.11.1（2026-10-09）：修复两种 `pnpm install` 失败；`pnx` 可运行任意 Rust 版本工具；将 `registry.npmjs.com` 视为 npm registry 别名。
- 🦀 pnpm 12.11.0（2026-10-09）：新增 Rust 工具链管理，链接依赖附带的 agent skills，新增 `permissions` 设置，并保留流式脚本输出颜色。
- 🐛 pnpm 12.10.1（2026-10-06）：修复 `overrides` 变更后及带 `catalogPrune` 的过滤 frozen install 失败；修复实验性 `nodeLinker.type: loaded` 的多个 bug，生成文件保留在 `node_modules`。
- 🔗 pnpm 12.10.0（2026-10-06）：新增实验性 `loaded` node linker；`pnpm-lock.yaml` 可记录解析设置；更快读取缓存 registry 元数据；含安全修复，阻止依赖版本写入全局虚拟 store 之外。
- ⚡ pnpm 11.28.5（2026-10-06）：更快读取缓存 registry 元数据；`pnpm config get --global` 忽略项目设置；修复包归档、git 依赖和配置依赖的多项安全问题。
- 📦 pnpm 12.9.1（2026-10-03）：WebContainer 构建迁移到独立 `@pnpm/wasm` 包，`pnpm` 包体积缩至约 4 MB，并修复 GitLab CI 的 provenance 发布问题。

---

### [发布 v1.0.0 · QwikDev/partytown · GitHub](https://github.com/QwikDev/partytown/releases/tag/v1.0.0)

**原文标题**: [Release v1.0.0 · QwikDev/partytown · GitHub](https://github.com/QwikDev/partytown/releases/tag/v1.0.0)

QwikDev/partytown 发布最新稳定版 v1.0.0，标志着项目正式退出 beta 阶段，并由 GitHub Actions 创建、带有已验证签名。

- 🚀 Partytown 退出 beta，正式发布 v1.0.0 稳定版。
- 📅 发布日期为 10 月 10 日 12:18。
- 🧩 主要变更由 @gioboa 提交，对应 PR #785。
- ✅ 提交哈希为 538b79b，带有 GitHub 已验证签名，GPG 密钥 ID 为 B5690EEEBB952194。
- 📦 该发布包含 2 个资源文件。
- 👍 获得 9 个火箭表情反应，来自 SkyZeroZx、nokazn、thegauravthakur 等用户。

---

### [](https://webkit.org/blog/18420/release-notes-for-safari-technology-preview-254/)

**原文标题**: [  Release Notes for Safari Technology Preview 254 | WebKit](https://webkit.org/blog/18420/release-notes-for-safari-technology-preview-254/)

Safari Technology Preview 254 于 2026 年 10 月 8 日发布，适用于 macOS Golden Gate 与 macOS Tahoe；已安装用户可在“系统设置 → 通用 → 软件更新”中更新。本次版本汇总 WebKit 321068@main…322634@main 的变更，重点覆盖 CSS 新特性与布局修复、JavaScript/Web API 稳定性、媒体与 WebCodecs/WebGPU/WebRTC、无障碍、网络、扩展和开发者工具等。

- 🧭 发布信息：Safari Technology Preview 254 现已开放下载，支持 macOS Golden Gate 和 macOS Tahoe。
- ♿ 无障碍：修复 VoiceOver 对 iOS 日期/时间/颜色输入、`pointer-events: none` 控件、ARIA 菜单项“selected”播报，以及 iOS 多段错误信息倒序重复朗读等问题。
- 🎞️ 动画：修复粘性定位内联祖先吸附后视图时间线动画冻结，以及透明度加速动画到 0 时元素仍可见的问题。
- 🎨 CSS 新特性：新增 `size`/`min-size`/`max-size` 简写、`border-*-radius` 侧边简写、`interpolate-size`、`symbols()` 匿名计数器样式、SVG 链接参数 `link-parameters`/`param()`、`calc-size()`。
- 📐 CSS Grid/布局修复：修复大量 `order` 值导致重排成本平方增长、跨轨道尺寸分配、`fit-content()` 轨道、margin box 最小贡献、`contain: inline-size` 固有宽度、表格固定布局与 intrinsic/calc-size 等问题。
- ✂️ CSS 文本/行截断/颜色：修复 `line-clamp` 与 `-webkit-line-clamp` 级联、`max-lines`/`block-ellipsis` 语法、嵌套块/多列/浮动/绝对定位等截断行为；修复相对颜色 `none` 通道、`alpha()` 序列化与参数、系统色、边框图像重复等。
- 🖌️ Canvas 与弃用：修复 `rect()` 负宽高绕向、`TextMetrics` 基线/em 高度、图像源尺寸遵循 CSS 对象尺寸协商；移除非标准 `globalCompositeOperation: darker`。
- ✍️ 编辑与表单：改善粘贴后光标可见性、固定定位元素拖选自动滚动、列表转换属性；修复 `<select>` 的 `::picker-icon` 箭头、`valueAsNumber` 无限/NaN 处理、搜索框图标。
- 🧱 HTML 与图片：修复 iframe 首载前改 `src` 导致前进后退异常、`about:blank` 子框架历史替换、overlay scrollbar 下 `scrolling` 属性即时生效；修复图片查看器深色模式、空 `alt` 破图、`naturalWidth`/`naturalHeight`、生成图像 `image-rendering`。
- 🟨 JavaScript：修复 `BigInt("-")`/`BigInt("0x ")`、模块循环读取旧值、`arguments` 截断、`Error.stackTraceLimit`、正则 lookbehind 反向引用与 `lastIndex`、ArrayBuffer/Array 构造顺序、Intl 格式化/分段、Promise 跨 realm、可选链调用、标签模板 `this`/`super`、TypedArray Proxy 等。
- 🎬 媒体与 WebCodecs：WebCodecs 新增 `transfer` 选项和 `VideoEncoder` 的 `hevc` 输出；修复隐藏页暂停媒体自动播放、PiP 全屏视频消失、文本轨道覆盖、媒体范围丢末字节、镜像 `VideoFrame`、MSE `play()` 不解析、`flush()` 挂起、VP9 色彩/位深错误。
- 🌐 网络：修复非 ASCII cookie 截断并改为 UTF-8 读取、自定义 URL scheme 跨源检查、Apple Wallet `data:` URL、推测规则预取影响导航、结构化头 `*` 键解析、跨源样式表缓存复用。
- 📄 PDF、性能与渲染：PDF 选中文本支持翻译；优化 `::before`/`::after` 样式解析、合成粗体测量、深层 column flex 百分比 `flex-basis` 指数级布局；macOS 新增实时捏合缩放，并修复粗体度量、overlay 滚动条动画、替换元素固有宽度、3D 变换命中测试、`nowrap` 空格溢出、`line-clamp` 内联边框、固定 iframe 移动渲染。
- 🧩 SVG：修复 `patternTransform.clear()`、`getComputedTextLength()` 处理 `lengthAdjust`、角度序列化、无 `viewBox` 的 flex 项宽度、外层 `<svg>` 的 `transform`、`stroke: none` 时 `pointer-events`、暂停动画恢复。
- 🔐 安全与 Web API：`hardwareConcurrency` 改为 4/8 交替以降低指纹风险；修复 Worker CSP 违规事件；修复 Navigation API `dispose`、IndexedDB 事务死锁、`outerWidth`/`outerHeight` 为 0、跨站 `pagehide`/`visibilitychange`/`unload`、Blob 内存增长、`navigate` 中 `preventDefault()`、LCP 使用图片自然尺寸。
- 🧩 Web Extensions 与 Web Inspector：修复 `webRequest` 子框架/popup/types/parentFrameId/iframe CSP、后台 service worker 消息、offscreen `window.close()`；Web Inspector 修复大值溢出、Sources 旧远程目标、断点状态、Timeline 导出导入 DOM 节点。
- ⚙️ WebAssembly 与 WebDriver：Wasm 支持宽算术（128 位加减、64×64→128 乘法），解释器提速约 5%，优化 GC structs/arrays 编译；WebDriver BiDi 支持 `browsingContext.captureScreenshot` 生成 PNG，并修复按键、命令排队、导航等待、stale element 等。
- 🖥️ WebGL、WebGPU 与 WebRTC：修复 WebGL 预乘 alpha 上传；WebGPU 透明 alpha、异步管线 settle、NaN、刷新率下降、着色器缓存、render bundle 动态偏移、冗余 sampler；WebRTC/WebCodecs 改进 H.265/H.264 色彩空间与全范围处理、canvas 编码 sRGB。

---

