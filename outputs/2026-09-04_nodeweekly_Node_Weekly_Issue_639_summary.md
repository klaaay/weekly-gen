### [](https://trilon.io/blog/nestjs-12-is-now-available)

**原文标题**: [NestJS v12 is Now Available - Trilon Consulting](https://trilon.io/blog/nestjs-12-is-now-available)

NestJS 12 正式发布，这是一次覆盖框架核心、CLI、默认工具链和文档的重大版本更新。它引入了 ESM-first 支持（但对现有项目保持可选）、Rspack 取代 webpack、Standard Schema 原生验证、结构化日志、路由冲突诊断、原生可观测性 SDK、多项微服务与 GraphQL/WebSocket 增强，并改版了官网和文档，同时提供了简便的升级命令与可选的 ESM 迁移路径。

- 🚀 ESM-first：NestJS 核心包现在以 ESM 形式发布，但借助 Node.js 的 `require(esm)`，现有 CommonJS 项目无需重写即可升级；CLI 新增 `nest upgrade` 命令，并会保留现有模块格式。
- ⚙️ 项目初始化可选模块格式：`nest new` 会询问使用 CommonJS 还是 ESM；ESM 新项目默认采用 Vitest 和 oxlint，CJS 项目继续生成 Jest 和 ESLint 配置。
- 🧱 Rspack 取代 webpack：Nest CLI 弃用 webpack 工作流（`--webpack` 标记已弃用），Rspack 成为 monorepo 默认打包器；`tsc` 仍是标准项目的默认编译器。
- 📐 Standard Schema 支持：`@Body()`、`@Query()`、`@Param()` 等装饰器可直接接受 schema 选项（如 Zod、Valibot、ArkType），并新增 `StandardSchemaValidationPipe` 和 `StandardSchemaSerializerInterceptor`；`@nestjs/config` 也支持任意 Standard Schema 对象（Joi 仍可继续使用，这并不取代 class-validator）。
- 📊 结构化日志与机器可读错误码：`ConsoleLogger` 将附加对象参数作为结构化字段处理（JSON 模式下可用 `params` 或 `flattenParams`）；`HttpExceptionOptions` 新增 `errorCode`，让错误响应携带稳定、可编程的错误标识。
- 🧭 路由冲突诊断：新增 `routeConflictPolicy` 和 `routeResolutionStrategy` 应用选项，帮助开发者检测并处理路由遮蔽和重复路由问题。
- 📡 原生可观测性：发布官方 `@nestjs/observe` SDK，通过 `instrument` 选项接入 Nest 请求生命周期，可自动采集请求、后台任务、错误、日志与分布式追踪。
- 🔌 微服务丰富更新：支持 NATS v3（使用新的 `@nats-io/transport-node`）、Kafka 正则 topic 匹配、pre-request hooks 以及专属 gRPC 异常过滤器。
- ⚡ GraphQL 与 WebSocket：GraphiQL 成为默认 IDE，移除 `subscriptions-transport-ws` 并改用 `graphql-ws`；WebSocket 网关支持请求作用域和断开原因回调。
- ✨ 其他改进：Express 应用支持优雅停机、生命周期钩子调用顺序优化、`PipeTransform` 类型签名更安全；NestJS 12 要求 Node.js v20.19+ 或 v22.12+。
- 🎨 官网与文档改版：NestJS 官网和官方文档迎来约九年来的首次大改版，阅读体验和导航更现代、清晰。
- 🔄 升级与可选 ESM 迁移：安装最新 CLI 后运行 `nest upgrade` 即可保留当前 CJS/ESM 格式完成升级；如需将项目本身转为 ESM，可按步骤添加 `"type": "module"`、设置 nodenext、为相对导入添加 `.js` 扩展名，并用 `import.meta.dirname` 替换 `__dirname`。

---

### [](https://standardschema.dev/)

**原文标题**: [Standard Schema](https://standardschema.dev/)

Standard Schema 是一套用于 TypeScript 生态系统的标准化接口规范，旨在统一数据验证与转换功能的实现与消费方式。它通过定义通用接口，让工具能够以单一输入形式获取所需类型和能力，从而避免库特定适配器与额外依赖，构建更公平、友好且开放的生态。规范分为 Standard Typed、Standard Schema 与 Standard JSON Schema 三个层次，并提供了完整可复制的 TypeScript 类型定义。

- 📐 项目包含三项核心规范：Standard Typed 作为基础类型、Standard Schema 负责实体数据验证与转换、Standard JSON Schema 用于 JSON Schema 生成与互转
- 🎯 主要目标：允许工具接受统一的标准输入，涵盖全部所需类型与能力，无需编写库特定适配器，也不引入额外依赖
- 🔧 Standard Schema 通过可选的 `"~standard"` 属性对外暴露 `version`、`vendor`、`types` 及 `validate` 方法，`validate` 可同步或异步返回结果
- ✅ 验证成功时返回 `value`；失败时返回 `issues` 数组，其中包含错误 `message` 和可选 `path` 路径信息
- 📄 Standard JSON Schema 定义了 `input` 和 `output` 转换方法，可将模式转换为 JSON Schema，并支持 `draft-2020-12`、`draft-07` 及 `openapi-3.0` 等目标版本，遇到不支持版本时抛出异常
- 🏷️ 提供 `InferInput` 与 `InferOutput` 类型工具，可从任意 Standard Schema 中推断输入与输出类型
- 📦 完整规范实现代码可在 npm 与 JSR 上的 `@standard-schema/spec` 包中获取，库作者可直接复制相关接口代码到项目中
- 🌍 通过标准化“单一输入”范式，最终让实现方更公平、消费方更方便、最终用户更开放

---

### [NestJS - 一个渐进式 Node.js 框架](https://nestjs.com/)

**原文标题**: [NestJS - A progressive Node.js framework](https://nestjs.com/)

NestJS 是一个基于 TypeScript 和 Node.js 的现代后端框架，以模块化架构、依赖注入和类型安全为核心，提供企业级支持、开发工具链、课程认证与社区生态，助力开发者高效构建可扩展应用。

- 🚀 NestJS 是增长最快的 Node 框架，专为高效、可靠、可扩展的服务端应用而设计，代码整洁且易于维护。
- 🧩 通过模块化组织、内置依赖注入、TypeScript 类型安全和装饰器，提升可维护性与可读性。
- ⚙️ 提供官方工具：Observe 实现零配置自动观测、错误监控与日志流；Devtools 支持可视化架构图、代码沙箱和 CI/CD 集成。
- ☁️ Deploy Mau 支持一键部署 AWS、实时日志与指标监控，简化 DevOps 工作。
- 🏢 提供企业级官方支持，包括技术指导、架构评审、团队培训、最佳实践、安全与性能咨询、代码审查及长期支持。
- 📚 官方文档包含引导示例（Bootstrap, Controller, Module），并提供高级架构、认证授权、微服务、基础等系列课程。
- 🎓 提供 Nest 认证专家课程，超 200 节课时，可学习掌握任意规模的现代后端开发。
- 💬 多家企业（如 O2、Clipboard Health、Munich Re、Plotly）认可 NestJS 在架构一致性、微服务扩展和代码质量上的表现。
- 🤝 支持社区赞助（Principal/Gold/Silver/Backer），并可通过 `npm i -g @nestjs/cli` 快速创建项目。
- 📬 提供新闻订阅入口，便于获取最新动态与更新。

---

### [](https://www.tigerdata.com/go/trial?utm_source=content-syndication&utm_medium=referral&utm_campaign=node-weekly-newsletter)

**原文标题**: [Postgres for time-series workloads at any scale. | Tiger Data](https://www.tigerdata.com/go/trial?utm_source=content-syndication&utm_medium=referral&utm_campaign=node-weekly-newsletter)

概述：Tiger Cloud 提供专为时间序列工作负载设计的 Postgres 服务，支持超大规模数据存储与管理，强调弹性伸缩、高可用、企业级安全与深度可观测性，并可与现有技术栈无缝集成。

- 🚀 超大规模处理能力：单服务可承载每日 3 万亿指标、3 PB 数据与 1 千万亿数据点。
- 💰 免费试用额度：新账户可获 $1000 信用额度（30 天有效），无需信用卡。
- 📈 弹性伸缩：读写分离，支持最多 10 个副本节点，SSD/S3 分层存储实现无限且经济高效的容量。
- 💸 成本优化：计算与存储分离，可独立扩展，避免闲置容量浪费。
- 🛡️ 高可用保障：多可用区集群、自动故障转移、时间点恢复及跨区域备份。
- 🔐 企业级安全：符合 SOC 2、HIPAA、GDPR，支持全程加密、SSO、RBAC 与审计日志。
- 📊 深度可观测性：提供查询下钻与仪表盘，可发送指标至 CloudWatch、Datadog、Prometheus。
- ⚡ 快速部署：数分钟内即可完成数据库配置，支持 SQL、CLI、Terraform、Cursor 及 Claude Code 管理。
- 🔌 生态集成：可与主流云提供商及 Postgres 生态工具无缝对接。
- 🤝 企业支持：提供合同化 SLA、区域数据隔离、24/7 专家支持与企业级响应保障。

---

### [Bun · Node.js 测试](https://bun.com/node-test-suite)

**原文标题**: [Bun · Node.js test suite tracker](https://bun.com/node-test-suite)

概述摘要  
此内容展示的是 Bun 运行时对 Node.js 官方测试套件的兼容性追踪器界面。它通过可视化和筛选方式，呈现 Bun 在 Node.js v26.3.0 各测试中的通过情况，并支持与 Deno 进行对比。

- ⚡ 项目为 oven-sh/bun 下的“node.js test suite tracker”，用于追踪 Bun 的 Node.js 兼容进度。  
- 🧪 追踪来源为 Node.js v26.3.0 的上游测试，涵盖 test/parallel、test/sequential、test/js-native-api 与 test/node-api 等类别。  
- 🩷 每个圆点代表一个上游测试，粉色圆点表示该测试在 Bun 中已经通过。  
- 📁 支持按模块、文件或全部测试进行浏览，并可按名称 A-Z 排序。  
- 🚫 提供“排除 experimental”和“排除 internals”筛选选项，方便聚焦稳定或通用测试。  
- 📊 呈现通过数、未通过数及百分比统计，并可切换与 Deno 的兼容测试结果进行对比。  
- 🖱️ 点击任意圆点或文件名，即可跳转到 GitHub 打开对应测试源码。  
- 🔄 Bun 的测试数据基于当前代码引用实时抓取，而 Deno 的数据来自 tests/node_compat/config.jsonc。

---

### [Bun 1.](https://bun.com/blog/bun-v1.4)

**原文标题**: [Bun 1.4 | Bun Blog](https://bun.com/blog/bun-v1.4)

Bun 1.4 是 Bun 的重大版本更新，核心亮点包括：底层由 Zig 重写为 Rust、Node.js 兼容性大幅跃升（新增 1,517 个通过测试）、CPU/内存/启动性能显著优化，并加入多项内建功能（影像处理、浏览器自动化、Markdown、定时任务、终端等）。此外，包管理、测试运行器和打包器也有大量实用升级。

- 🚀 重大架构变化：Bun 由 Zig 重写为 Rust，修复超过 2,900 个问题。
- 📦 Node.js 兼容性：新增 +1,517 项 Node.js 官方测试；node:quic、node:sqlite 等通过率达 100%，主流框架（Next.js、Playwright、vitest 等）可直接运行。
- ⚡ 性能提升：空闲 CPU 使用率降低 5 倍，内存最多降低 35%，Linux 启动快约 50%，二进制体积缩小最多 17%。
- 🧰 内建标准库大增：新增 Bun.Image、Bun.WebView、Bun.markdown、Bun.cron()、Bun.Terminal、Bun.JSON5、Bun.XML、Bun.Archive 等，取代大量 npm 依赖。
- 🌐 Web 标准增强：ReadableStream/WritableStream 原生化，CompressionStream/DecompressionStream 落地，实现请求/响应背压，Response.clone() 效率大幅提高。
- 🔐 安全加固：多项 TLS 证书验证与 HTTP 解析默认收紧，fetch() 支持 mTLS、证书固定，并对证书主机名校验做了更严格处理。
- 📦 包管理器升级：bun install 在多场景下远快于 npm/pnpm/yarn，加入全局虚拟存储、bun audit fix、bun dedupe、bun prune、bun pm diff 等命令。
- 🧪 测试运行器：新增 bun test --parallel / --isolate / --shard / --timings / --changed，支持 retry、fake timers、onTestFinished 等。
- 🏗️ 打包器与编译器：内建 React Compiler（大幅加速构建）、barrel import 优化、TC39 标准装饰器、--asset 嵌入资源、更快的代码分割与字节码编译。
- ⚙️ 平台支持扩展：原生 FreeBSD 构建、Windows ARM64、实验性 Android 支持，Linux glibc 最低要求降至 2.17。
- 📉 升级注意事项：Node.js 版本升至 26（NODE_MODULE_VERSION 147），新 monorepo 默认 isolated linker，Bun 以 node 身份运行时不再自动加载 .env，以及多项行为变更需要适配。

---

### [Bun 1.4 | Bun 博客](https://bun.com/blog/bun-v1.4#node-js-compatibility)

**原文标题**: [Bun 1.4 | Bun Blog](https://bun.com/blog/bun-v1.4#node-js-compatibility)

Bun 1.4 是一个重大版本更新，大幅提升 Node.js 兼容性、运行时性能和新内置能力：新增 1,517 项 Node 测试通过，修复超过 2,900 个问题；空闲 CPU、内存占用和启动时间显著下降；加入 Bun.Image、WebView、Markdown、cron、Terminal 等内置工具；并将 Bun 核心从 Zig 重写为 Rust。

- 🎯 Node.js 兼容性显著提升：`http`、`fs`、`cluster`、`stream` 等模块通过约 97% 的 Node 上游测试，`quic` 达 99%，`events`、`trace_events`、`sqlite` 为 100%；Playwright、Next.js 16、vitest、OpenTelemetry、dd-trace 等生态现已可用。
- 🚀 生产环境更省资源：空闲 CPU 最高降低 5 倍，HTTP 服务内存占用减少 13–48%，Linux/Windows 启动耗时明显缩短，二进制体积最多缩小 17%。
- ⚡ 原生流重写：`ReadableStream`/`WritableStream`/`TransformStream` 性能大幅提升，压缩、转码、子进程管道的吞吐与内存表现优于 Node.js/Deno，并完整支持背压。
- 🖼️ 内置 Bun.Image：可解码、缩放、旋转、编码 JPEG/PNG/WebP/GIF/BMP，API 类似 sharp，无需原生依赖，典型场景比 sharp 快约 1.38 倍。
- 🤖 内置 Bun.WebView：无头浏览器自动化，支持导航、点击、截图，可驱动 WebKit、Chrome、Edge，无需 Puppeteer/Playwright。
- 📝 更多内置服务：新增 Bun.markdown、Bun.Terminal、Bun.cron；内置 JSON5/JSONC/JSONL/XML/TOML、Bun.Archive、CompressionStream、URLPattern、ANSI 字符串工具等，减少大量 npm 依赖。
- 🧩 后量子密码支持：Web Crypto 和 `node:crypto` 加入 ML-DSA、ML-KEM，符合 NIST FIPS 203/204 标准。
- 🔄 Rust 重写：Bun 1.4 是首个完全使用 Rust 编写的版本，为后续内存与性能优化打下基础。
- ⌨️ 并行 CLI：新增 `bun run --parallel`、`bun test --parallel`，支持 `--shard`、`--changed`、`--timings`，可跨 CPU/CI 分发测试，提升执行效率。
- 🧰 bun install 工具链增强：加入 `bun audit fix`、`bun dedupe`、`bun prune`、`bun pm diff`/`licenses`；全局虚拟存储让依赖安装最多快 7 倍。
- 📦 包管理器更完善：支持嵌套 overrides、catalog、workspace `--filter`、更新传递依赖、锁定 git/tarball 完整性哈希，并兼容 npm/pnpm 更多场景。
- 🔬 可观测性升级：`--cpu-prof`/`--heap-prof` 可输出 Markdown 报告，便于终端排查和 LLM 分析；另支持 `BUN_CPU_PROFILE`、`--mem-pressure` 事件、async stack traces。
- 🌐 网络能力进步：`Bun.serve()` 支持 HTTP/3、静态目录、Range/条件请求、响应背压；`fetch()` 支持 HTTP/2/3、代理自定义头、请求压缩和 TLS 会话复用。
- 🛡️ 安全强化：默认启用更严格的 TLS 证书校验、加固 HTTP 解析与 tarball 提取、防止路径穿越和凭据泄露，官方建议所有用户尽快升级。
- 💻 平台扩展到更多系统：新增原生 FreeBSD、Windows ARM64 构建，实验性 Android 构建，并将 Linux glibc 最低要求降至 2.17。
- ⏱️ 大量底层性能优化：URL 解析最快提升 4.6 倍，RegExp 显著提速，Promise 快 1.5–2.4 倍，`node:zlib` 改用 zlib-ng，SIMD 加速 hex/base64url 解码、sourcemap、字符串处理等。

---

### [](https://github.com/nodejs/node/pull/65475)

**原文标题**: [ffi: enable module by default by mcollina · Pull Request #65475 · nodejs/node · GitHub](https://github.com/nodejs/node/pull/65475)

Node.js 的 PR #65475 将实验性的 `node:ffi` 模块在支持 FFI 的构建中默认开启。该模块由 Matteo Collina 提交，保留了 `--experimental-ffi` 参数作为兼容性空操作，并新增 `--no-experimental-ffi` 实现按需禁用；模块仍标记为实验性，首次加载时继续输出警告。多个核心维护者审核通过后，PR 被合入 main，并附带调整了相关测试（#65636）与文档（#65632）。

- 📦 在支持 FFI 的 Node.js 构建中，使 `node:ffi` 无需任何标志即可加载。
- 🚩 保留 `--experimental-ffi` 作为兼容性 no-op，同时通过 `--no-experimental-ffi` 提供退出机制。
- ⚠️ 模块仍处于实验阶段，首次加载时保持实验性警告。
- ✅ 获得多位维护者（如 jasnell、panva、benjamingr 等）审核通过并成功合并到 main。
- 🏷️ 标记为 semver-minor 和 notable-change，因引入新功能并需要变更日志突出显示。
- 🔧 合并后发现既有测试与默认开启行为冲突，后续 PR #65636 更新测试；#65632 修复文档链接。
- 📊 CI 全部通过，代码覆盖率为 90.13%，改动主要集中于 Node 选项解析。

---

### [](https://github.com/nodejs/node/pull/65675)

**原文标题**: [sea: mount bundled assets as a virtual file system by mcollina · Pull Request #65675 · nodejs/node · GitHub](https://github.com/nodejs/node/pull/65675)

该 PR 为 Node.js 的单可执行应用（SEA）集成了虚拟文件系统（VFS）功能：通过设置 `"useVfs": true`，打包的资源会以只读 VFS 方式挂载，并直接从挂载点运行主脚本，从而支持更自然的路径解析、模块加载及 ESM 用法，同时避免与真实文件系统冲突。该实现已通过审查与 CI，最终合入 Node.js 主分支。

- 🎯 核心目标：为 SEA 配置新增 `"useVfs": true`，将打包资源挂载为只读虚拟文件系统，并在挂载内执行注入的主脚本。
- 📂 路径行为：VFS 不遮蔽真实文件系统且挂载点运行时动态选择，因此没有固定 `/sea` 路径；主脚本位于挂载根目录，`__filename` 和 `__dirname` 指向虚拟文件系统。
- 🔗 资源与模块解析：可通过 `__dirname` 相对路径配合常规 `node:fs` API 访问资源；相对 `require()` 和 `node_modules` 查找也在挂载内解析。
- ⚙️ 实现要点：主脚本源码不额外复制，直接取自 SEA blob 并注入运行时；SEAProvider 只读且惰性加载，仅在打开文件时读取内容并缓存 `stat` 大小。
- ⚠️ 警告处理：隐式 SEA 挂载不再额外触发 `VirtualFileSystem` 实验警告，SEA 自身的警告已覆盖。
- 📦 ESM 支持：`"mainFormat": "module"` 时，ESM 主脚本从挂载内加载，`import.meta.url/filename/dirname` 正确反映挂载路径，静态导入、动态 `import()` 和裸说明符均解析到打包资源。
- 🚫 配置互斥：`"useVfs"` 与 `"useSnapshot"`、`"useCodeCache"` 同时使用时会被拒绝。
- ✅ 质量与合并：补丁覆盖率约 99.4%，经多位维护者审查批准，最终以 commit `4e207b1` 合入 `nodejs:main`。

---

### [2026 年 8 月安全发布 · Express.js](https://expressjs.com/en/blog/2026-08-31-security-releases/)

**原文标题**: [August 2026 Security Releases · Express.js](https://expressjs.com/en/blog/2026-08-31-security-releases/)

Express 团队于 2026 年 8 月发布了 hbs 4.3.0、multer 2.3.0 和 morgan 1.12.0，共修复六项安全漏洞（涉及模板渲染、multipart 解析与访问日志）。建议所有受影响用户立即升级到最新版本，可通过 `npm update hbs multer morgan` 完成更新。

- 🚨 CVE-2026-16231（高危，hbs）：hbs 2.1.0 至 4.2.1 的 `registerAsyncHelper` 异步助手输出未转义，可能导致跨站脚本（XSS）；4.3.0 起与同步助手保持一致转义。
- 🚨 CVE-2026-77037（高危，multer）：2.2.0 版本在磁盘上传被中止时泄漏文件描述符并占用磁盘块，远程可致资源耗尽；2.3.0 已修复异常终止时的流关闭与清理问题。
- 🚨 CVE-2026-77078（高危，multer）：2.3.0 以下版本处理特殊构造的多部分字段名时会触发未捕获 RangeError 导致进程崩溃；单次请求即可远程 DoS。
- 🚨 CVE-2026-82333（高危，multer）：2.3.0 以下版本因超大数组索引导致事件循环阻塞，单请求即可令 worker 无响应；2.3.0 新增 `limits.fieldArrayIndexLimit` 选项防御。
- ⚠️ CVE-2026-15603（中危，morgan）：1.12.0 以下版本未转义 Unicode 行分隔符（U+0085、U+2028、U+2029），可被利用进行日志伪造；1.12.0 已扩展转义范围。
- 🔽 CVE-2026-77063（低危，multer）：2.3.0 以下版本中，异步 `fileFilter` 与 `fileSize` 限制存在竞态条件，可绕过文件大小限制拒绝；2.3.0 已调整处理顺序修复。
- 🛡️ 建议所有使用 hbs、multer、morgan 的应用升级至 4.3.0、2.3.0、1.12.0 或更高版本，以规避上述风险。

---

### [](https://github.com/nodejs/node/issues/65536)

**原文标题**: [Proposal: Remove ESM/CJS duality from code samples in API docs · Issue #65536 · nodejs/node · GitHub](https://github.com/nodejs/node/issues/65536)

overview summary
该提案建议移除 Node.js API 文档中 ESM 和 CJS 双代码示例的冗余写法，统一采用单个 JavaScript 代码块并优先使用 ESM 导入，以减轻文档维护负担。

- 📄 指出 ESM 引入后，API 文档需提供 ESM/CJS 两种可切换示例，但核心导入差异导致大量代码重复。
- 🔄 说明文档覆盖不一致，部分示例仅 ESM、仅 CJS 或两者兼有，维护质量参差不齐。
- 🙋 提及社区贡献者常提交将 CJS 示例补充为 ESM 的双份代码，但浪费了审阅者的时间。
- 💡 建议移除`mjs`和`cjs`代码块，改用统一的`js`代码块。
- ⚡ 主张除非示例专门展示 CJS 特性，否则默认使用 ESM 导入作为标准范式。
- 🗂️ 该问题被标记为“discuss”和“doc”，用于文档讨论与反馈。

---

### [](https://www.checklyhq.com/blog/agentic-rewrite-nodejs-to-go/)

**原文标题**: [Rewriting a Node.js Service in Go With AI Agents](https://www.checklyhq.com/blog/agentic-rewrite-nodejs-to-go/)

Checkly 团队用 Claude Code 将日均处理 9200 万条消息的 Results Daemon 从 Node.js 重写为 Go，整个迁移零事故并显著降低资源消耗。核心成功因素是在编写新代码之前构建了严格的黑盒测试 harness，并用真实生产数据生成测试用例，同时结合人工监督修正代理代码中的问题。最终实现 pods 减少 70%、数据库负载大幅下降，也验证了代理工程在高吞吐关键服务中的可行性。

- 🚀 重写成果：Results Daemon 每日处理约 9200 万条消息，从 Node.js 迁移到 Go 后实现零事故上线，运行 pods 减少 70%，数据库负载显著降低。
- 🔒 Go 的优势：Go 更强的类型系统比 JavaScript 更适合代理编写代码，减少回归风险，也让功能迭代和部署更快速、更有信心。
- 🧪 测试 harness 优先：在设计阶段先构建黑盒测试框架，让代理在明确“正确”定义的环境中工作，而非依赖人工代码审查。
- 🗂️ 黄金文件与确定性输出：测试用例输入后与 legacy 系统生成的 golden files 做字节级比对，非确定性字段用 `<uuid>`、`<timestamp>` 占位但仍做类型检查。
- 🧱 边界管理：数据库、队列、缓存等外部组件用真实实例（如 PostgreSQL 容器）或自建高效模拟器，由 harness 统一管理，系统只通过环境变量连接。
- 🛠️ 技术选型：Harness 基于 Playwright、Docker Compose 和 Toxiproxy，分别提供可靠测试执行、容器编排和故障注入能力。
- 📊 测试用例来源：从内部数据湖提取 24 小时内的账户/分组/检查配置及结果状态，构造覆盖 `(accountConfigs × groupConfigs × checkConfigs × resultOutcomes)` 组合的真实场景。
- 🎯 覆盖率与迭代：用代码覆盖率报告评估 harness 有效性（目标 90%-100%），并将报告反馈给代理补充缺失用例，同时用 Toxiproxy 额外测试基础设施故障模式。
- 🤖 代理编写代码：Claude Code 通过 Fable 派发，一夜生成约 13,000 行可部署 Go 代码，日常 token 消耗控制在 $200 订阅限额内；早期 Opus 版本未达标被弃用。
- 👨‍💻 人工监督修正：审查后移除运行时派生配置、改为静态环境变量，并扩展端到端可观测性（数据库连接、CPU、内存等指标），提升长期运维能力。
- ⚠️ 首次部署教训：内部迁移时发现重试队列拓扑与生产不一致——本地简化成 3 个队列，生产实际有 18 个/区域，根因是 harness 环境过度简化。
- 🔧 修正原则：Harness 环境必须尽量贴近生产；每个边界需细化到最低单元（每条队列、每张表）；所有基础设施假设必须书面化并验证，不能凭空推断。
- 🧭 分阶段客户迁移：按免费 → 付费 → 企业账户依次用 feature flag 切换流量，每批监控 24-48 小时，期间 legacy 和新 daemon 同时运行并共享 harness CI 检查。
- 🔁 TDD 修复流程：客户报告的 bug 先在 harness 中复现差距，再修复底层问题，整个闭环约 1 小时完成；绝大多数问题只是 harness 未覆盖的边缘情况。
- ✅ 最终成效：数据库总平均活跃会话数下降 60%、CPU 降低约 15%；释放约 15 vCPU 和 45GB 内存；开发者获得更快部署、更少告警和更高信心。
- 📚 核心经验：严格测试、清晰边界定义、知道何时人工介入，是让代理高效重写遗留系统的关键，这套原则比具体工具更持久。

---

### [](https://blog.sentry.io/otel-spans-errors-sentry-trace/?utm_source=nodeweekly&utm_medium=paid-community&utm_campaign=tracing-fy27q3-evergreen&utm_content=newsletter-sponsored-link-blog-otel-learnmore)

**原文标题**: [OTel spans + Sentry errors: Connected in one trace | Sentry Blog](https://blog.sentry.io/otel-spans-errors-sentry-trace/?utm_source=nodeweekly&utm_medium=paid-community&utm_campaign=tracing-fy27q3-evergreen&utm_content=newsletter-sponsored-link-blog-otel-learnmore)

Sentry 的 OtlpIntegration 解决了一个核心问题：原始 OTLP endpoint 虽然能把 OTel span 导入 Sentry，却无法把 Sentry 错误和 OTel trace 连接起来。新集成会在 Sentry SDK 侧读取当前 OTel trace context，并把它标注到 Sentry 事件上，让错误与 span 在同一个 trace 瀑布中互相可见；取代了部分 SDK 原有的深层 POTel 集成，配置更轻、跨语言更一致，但错误仍然必须通过 Sentry SDK 上报。

- 🧩 原始 OTLP endpoint 只接收 span，这些 span 是“孤岛”：错误看不到触发它的 OTel trace，span 也看不到执行期间发生的 Sentry 错误。
- 🔗 OtlpIntegration 把当前 active 的 OTel `trace_id` 和 `span_id` 自动写入每个 Sentry 事件，实现错误、日志、指标与 trace 的关联。
- ⚙️ 集成核心做三件事：配置指向 Sentry 的 OTLP exporter、将 OTel trace context 注入 Sentry 事件、可选注册 `SentryPropagator`。
- ♻️ 它取代了之前 POTel 深度集成：新的后端 SDK 不再强制依赖或耦合 OpenTelemetry，代价是进程内 span 不再与 Sentry span 交错。
- ✅ 配置非常简单：Python 示例只需设置两个环境变量 `OTEL_EXPORTER_OTLP_TRACES_ENDPOINT` 和 `OTEL_EXPORTER_OTLP_TRACES_HEADERS`，再在 `init` 中加入 `OtlpIntegration()`；若已有自己的 `TracerProvider`，会自动跳过初始化。
- 🏢 最适合已有 OTel 做后端追踪、同时用 Sentry 处理错误的团队，尤其多语言后端：OTel trace 保留，Sentry 负责错误，两者互相穿透。
- 📈 你能获得：OTel span 在 Sentry trace 瀑布中与 Sentry 错误/日志拼接、跨服务分布式 trace、OTLP log 接入。
- ⛔ 你不能获得：通过 OTLP 上报错误（错误仍必须用 Sentry SDK）；同一进程内 Sentry 与 OTel span 交错；没有 OTLP trace 时，OTLP log 无法关联错误。
- 🔮 `SentryPropagator` 自动注册即将在下一大版本移除，因为 OTel 全局只允许一个 propagator；未来会改为文档化的显式 opt-in 配置。

---

### [在 Node.js 中检测 SQLite 全表扫描 | CodeSilva](https://codesilva.com/programacao/2026/08/13/detecting-sqlite-full-table-scans-in-nodejs)

**原文标题**: [Detecting SQLite Full Table Scans in Node.js | CodeSilva](https://codesilva.com/programacao/2026/08/13/detecting-sqlite-full-table-scans-in-nodejs)

文章介绍了 Node.js 的 `node:sqlite` 新增的语句级扫描计数器功能：通过 `StatementSync` 上的 `stat()` 和 `resetStats()`，开发者可以直接读取 `fullscanStep` 等 SQLite 内部统计值，从而便捷地检测全表扫描。该方法特别适合作为测试/开发环境中的安全护栏，能够捕获未走索引的查询，对 AI 生成的 SQL 也很重要。该功能已合入 main，并将在下个 Node.js 版本中发布。

- 📰 `node:sqlite` 现在支持检测 SQLite 全表扫描，受 Aaron Patterson 的 Ruby 示例启发，Node.js issue 推动实现落地。
- 🔧 为 `StatementSync` 新增了两个方法：`stat(counter)` 读取一个计数器，`resetStats()` 清零所有累计值。
- 📊 示例查询无索引时 `fullscanStep: 999`，建索引后 `fullscanStep: 0`；`vmStep` 也从 3059 降至 101。
- ⏱️ 计数器在 prepared statement 生命周期内是累积的，每次测量前须调用 `resetStats()` 清零。
- 📋 可用计数器包括 `fullscanStep`、`sort`、`autoindex`、`vmStep`、`reprepare`、`run`、`filterMiss`、`filterHit`、`memused` 等。
- ⚠️ `filterMiss`/`filterHit` 需要 SQLite 3.38.0+，否则抛 `ERR_INVALID_ARG_VALUE`；`memused` 是当前内存占用，`resetStats()` 不会重置它。
- 🛡️ 六行代码即可实现 `assertNoScan` 助手，在测试/开发中捕获意外全表扫描并输出触发 SQL。
- 🤖 对 AI 生成的 SQL 尤其有价值——模型不知道字段是否被索引，评审也难发现，该断言可在 CI 中直接失败。
- ✅ 小表（如五行的带索引表）仍会报零，不会误报；按语句逐个启用，不影响正常扫描查询。
- 🚀 功能已合入 `main` 分支，将在下一个 Node.js 版本中随 `node:sqlite` 发布。

---

### [](https://www.thenodebook.com/worker-threads/workers-vs-processes)

**原文标题**: [Workers vs Processes](https://www.thenodebook.com/worker-threads/workers-vs-processes)

在一个 CPU 密集任务运行在主线程时，整个事件循环都会停滞；Worker Threads 提供了在同一进程内并行执行 JavaScript 的能力，而 Child Processes 则提供完整的进程级隔离。文章深入比较了三种执行方式的适用场景、启动成本、内存模型以及常见误区。

- 🧵 Worker Thread 是在同一 Node.js 进程内创建的独立 JS 执行线程，拥有独立的 V8 isolate、heap、libuv event loop 和 Node 环境。
- ⏳ 如果主线程执行 CPU-heavy 循环，所有 timer、socket 回调和 Promise 续体都会一直等待，直到该函数返回。
- 🔄 用 `Promise.resolve().then()` 或 `setImmediate()` 只是调整同一线程的任务顺序，无法把 CPU 工作移出主线程。
- 📊 Worker 适合 CPU-bound JavaScript（如大 JSON 解析、模板渲染、压缩计算），不适用于异步 I/O 等待。
- 🛠️ 创建 Worker 时建议用 `require.resolve('./xxx.js')` 而不是相对字符串，避免路径依赖 `process.cwd()`。
- 🚦 常见的单文件 worker 模式依赖 `isMainThread` 分支；如果不加保护地 `new Worker(__filename)`，会无限递归创建 worker。
- 🧠 Worker 之间不共享普通 JavaScript 对象；消息传递只有三种方式：copy（结构化克隆）、transfer（ArrayBuffer 转交所有权）、share（SharedArrayBuffer 双方可见）。
- 💰 `new Worker()` 的一次性成本很高：需要创建 OS 线程、V8 isolate、Node 环境、模块加载器和消息通道；小任务用 worker 可能得不偿失。
- ⚖️ Worker 是同一进程内的轻量线程，崩溃或进程级致命错误会连累整个进程；Child Process 是独立 OS 进程，有更强隔离和崩溃恢复能力。
- 🌍 Child Process 更适用于外部可执行文件、独立 stdio/env/cwd、需要 supervisor 监控 PID 以及需要真正内存隔离的场景。
- ❌ 常见错误：每个小操作都开新 Worker、用 Worker 处理本来就基于事件的 I/O 等待，或在需要子进程隔离时错误地使用 Worker。
- 🎯 实际决策可以简化为：CPU-heavy JavaScript 且数据量有限 → Worker；外部工具或独立进程 → Child Process；普通异步 I/O → 留在主线程。

---

### [](https://drydock.org/)

**原文标题**: [Drydock Package Review: pre-publish package security](https://drydock.org/)

在软件包发布到公共注册中心之前，Drydock 会对候选包的实际构建产物与上一个已发布版本做确定性差异审查，将供应链风险（如新增安装脚本）锚定到具体代码行，并通过 Stage Watchtower（咨询）或 Workflow Gate（强制门禁）融入现有发布流程，同时支持 npm、PyPI 和 VS Code 等工作流。它用只读令牌获取包内容，不持有发布凭据，最终审批权仍在维护者手中。

- 🔍 审查对象是“构建产物”而非源码：Drydock 精确对比发布候选与已发布版本的 tarball，包含可能只存在于产物中的文件或代码。
- ⚠️ 风险信号定位：检测新增的 postinstall/lifecycle 脚本、进程执行、网络访问、凭据读取、新二进制等，并把每条发现钉在 diff 的变更行上。
- 🧩 两种接入方式：Stage Watchtower 是 advisory 模式，配合 npm stage 由维护者用 2FA 审批；Workflow Gate 用 GitHub Environment 暂停受保护的发布作业，强制审查后才能继续。
- 🔁 依赖更新集成：提供 Renovate preset 和 Dependabot workflow，能在依赖 PR 中自动生成包差异链接，支持分组更新，无需账号/token。
- 📚 真实攻击案例：event-stream、ua-parser-js、node-ipc、chalk/debug 等事件都说明恶意代码可以只在 npm tarball 中、不进 Git 仓库，所以发布前必须检查成品。
- 🔒 安全设计：Drydock 使用只读 token 拉取发布证据，报告保留脱敏内容而不留原始归档；发布凭据始终留在 npm/GitHub Actions 中，工具无法自行发布。
- 🚀 易用上手：无需注册即可阅读公开差异和真实事件报告，配置一个受保护发布路径只需几分钟，可“让下一次发布进船坞”。

---

### [srvx - 通用服务器](https://srvx.h3.dev/)

**原文标题**: [srvx - Universal Server](https://srvx.h3.dev/)

srvx 是一个基于 Web 标准的通用服务器，集成了 Node.js、Deno 与 Bun 支持，通过简洁的 fetch API 和内置 CLI 提供接近原生性能的开发体验。

- 🚀 支持 Node.js、Deno 与 Bun，可通过 `npx srvx`、`deno -A npm:srvx`、`bunx --bun srvx` 等方式快速运行
- 📡 基于 Web 标准构建，在 Deno 和 Bun 环境中可获得原生适配
- ⚡ 对 Node.js 兼容性极高，原生性能可达约 96.98%
- 🛠️ 内置 CLI 提供文件监听、日志记录、错误处理及静态文件服务
- ✨ 代码示例极简：只需导出包含 `fetch` 方法的默认对象即可返回 JSON
- 🌐 提供在线试用入口与 GitHub 开源仓库，便于随时体验和查看源码
- 💰 获得 Vercel、VoidZero、StackBlitz 等知名团队赞助支持

---

### [](https://docs.nvm-windows.com/features/newv2/)

**原文标题**: [What's new in v2 | nvm-windows Documentation](https://docs.nvm-windows.com/features/newv2/)

该文章介绍了 NVM for Windows v2 的主要新特性，涵盖安装模式、自动化、安全性及企业级功能。

- 🚀 无需强制管理员权限，且不再依赖符号链接，工作流更现代、权限要求更低  
- 📌 支持版本固定：通过 `.nvmrc`、`.node-version`、`package.json` 或自定义文件自动识别所需 Node 版本  
- ⚡ 下载和安装速度更快，体积缩小 40%，使用紧凑 `.7z` 压缩包，并可自动安装缺失的 Node.js 版本  
- 🔧 使用 Go 和 Zig 完全重写，分为社区版（MIT）和认证版（EULA）；认证版提供代码签名及额外治理功能  
- 🖥️ 引入两种操作模式：轻量 shim 模式（支持按目录切换版本和自动化）与零延迟链接模式（传统场景）  
- 🔁 自动化增强：支持按目录自动切换版本、自动安装缺失版本、自动安装默认全局模块  
- ⚙️ 新增用户偏好设置：自定义别名、默认全局模块列表，以及通过注册表或 `nvm config` 管理配置  
- 🔔 原生 Windows 集成：版本出现在“应用和功能”中，支持事件查看器、桌面通知中心及注册表存储  
- 🛡️ 安全与治理（认证版附加）：可限制 Node 版本（允许/阻止列表）、通过 ADMX/GPO/Entra 控制设置、支持高级代理和自定义镜像  
- 📦 可观测性附加组件：提供 SBOM、软件来源证明和 VEX 信任工件，以及适用于 SIEM/审计的结构化日志

---

### [](https://github.com/nvm-windows/nvm)

**原文标题**: [GitHub - nvm-windows/nvm: The Node.js version manager for Windows. · GitHub](https://github.com/nvm-windows/nvm)

nvm-windows 是一个专为 Windows 设计的 Node.js 版本管理器，与 Mac/Linux 版 nvm 不同，现已推出完全重写的 v2 版本。它无需管理员权限，支持多种运行模式，提供自动切换版本、并行安装、缓存加速等功能，并针对企业环境规划了商业认证构建服务。

- ⚠️ 明确区分：nvm-windows 与 Mac/Linux 上的原版 nvm 是不同项目，二者理念与实现完全不同
- 🚀 v2 重大更新：已完全重写，面向现代开发工作流，详情见官方文档
- 🏆 广泛认可：被 Microsoft 和 Google 推荐，拥有约 47.6k Stars 与 3.9k Forks
- 🛠️ 兼容模式多样：支持无管理员权限运行，提供 Zig 编写的快速 Shim 模式（无符号链接），以及零延迟 Link 模式（junction + symlink 回退）
- 🔄 自动化能力：支持按目录固定版本自动切换，自动安装缺失版本与默认全局模块
- ⚡ 速度优化：并行执行多个安装、采用 7z 压缩减少下载体积、原生解压与内置缓存
- 🪟 原生 Windows 集成：支持 Windows 应用、事件查看器日志、注册表及桌面通知中心
- 🎨 高度可定制：可定义用户别名、默认全局模块，并支持配置本地（离线/air-gapped）下载源
- 🏢 商业认证构建（预告）：计划于 2026 年 9 月推出，包含代码签名、MSI/MST/Intune 安装包、高级审计日志、策略强制执行（如限制 Node 版本范围）、SBOM/SLSA/VEX 等信任工件

---

### [](https://github.com/sindresorhus/got/releases/tag/v16.0.0)

**原文标题**: [Release v16.0.0 · sindresorhus/got · GitHub](https://github.com/sindresorhus/got/releases/tag/v16.0.0)

这是 got v16.0.0 发布说明的关键总结。该版本是一次大型更新，重点是内置 HTTP/2 与 DNS 缓存能力、移除外部依赖，同时调整了跨源凭据处理并修复多项协议与流相关行为。

- ♻️ 重写 HTTP/2 支持并移除 http2-wrapper：内置客户端支持 ALPN 协商、会话池复用、GOAWAY 下线、请求/响应 trailers、1xx 响应、中止信号、响应缓存、IPv6 authority 以及 h2c。
- ⚙️ `agent.http2` 不再是 agent 槽位，仅作为退出会话池的开关：传 `false` 可跳过连接池；传 agent 实例会抛错。
- 🎛️ 响应头不再包含 HTTP/2 伪头，请改用 `response.statusCode`；HTTP/2 代理支持已移除，且自定义 `agent.https` 配合 `http2: true` 时会回退到 HTTP/1.1。
- 🔀 当 `options.request` 返回 request/response 对象时，会绕过内置 HTTP/2 传输；返回 `undefined` 则继续使用 Got 自身传输。
- 🗂️ DNS 缓存被重写并移除 cacheable-lookup 依赖：`dnsCache: true` 使用内置缓存；也可传入包含 `lookup` 和可选 `clear(hostname?)` 的对象，已有 CacheableLookup 实例仍兼容。
- 📌 内置 DNS 缓存会分别解析 A 和 AAAA 记录，因此可能不再保留操作系统层面的 `verbatim` 地址顺序。
- 🔐 跨源场景（beforeRequest 钩子、afterResponse 重试或分页跳转）会清除 `authorization`、`cookie`、`cookie2`、`host`、`proxy-authorization`、URL 凭据并丢弃请求体；需要时应在钩子中显式设置。
- 🚰 `copyPipedHeaders` 不再复制凭据头（如 `authorization`、`cookie`、`set-cookie` 等）；受信上游需通过 `headers` 显式传递。
- 🗑️ 移除已废弃的 `searchParameters`、`followRedirects`、`auth` 占位选项，以及 `OptionsOfUnknownResponseBody` 类型。
- ➕ 新增对 `QUERY` HTTP 方法的支持：`got.query()` 和 `got.stream.query()`；QUERY 安全且幂等，默认可重试，在 301/302/307/308 重定向中保留可重放请求体，但不会进入内置缓存。
- ⏱️ `timeout.socket` 现在覆盖 HTTP/2 TLS 协商与会话建立阶段，并报告为真实的 `socket` 超时，不再计入 DNS 查询时间。
- 🔧 多项修复：连接错误可通过 `request.end()` 正确重试；`Retry-After: 0` 时立即重试而非退避；cookie 写入异常时保留完整响应体；异步 cookie 写入在终态重定向中会被等待；仅在响应含 `set-cookie` 时才缓冲 body；修复 `got.stream` 事件时序；修复 `strictContentLength` 对未解压响应的字节计数；冻结 `hooks.beforeCache` 等非可变默认钩子。
- 📦 依赖减少两个：正式移除 cacheable-lookup 与 http2-wrapper。
- 🧭 迁移方面：HTTP/2 现在内置，h2session 钩子无需再手动设置 `request` 或 `http2`；如需 HTTP/2 代理，仍可借助 `request` 选项使用 http2-wrapper。

---

### [](https://www.rfc-editor.org/info/rfc10008/)

**原文标题**: [RFC 10008: The HTTP QUERY Method | RFC Editor](https://www.rfc-editor.org/info/rfc10008/)

overview summary
- 📘 RFC 10008 定义了新的 HTTP QUERY 方法，允许客户端将查询内容放在请求体中，以安全且幂等的方式请求服务端处理并返回结果。
- ⚖️ QUERY 介于 GET 与 POST 之间：既不像 GET 那样受 URI 长度与编码限制，也不像 POST 那样可能引起状态变更；它明确是安全且可重复的。
- 📦 QUERY 请求必须携带与内容一致的 Content-Type；媒体类型缺失或不支持时，服务器应返回 400、415 或 422 等相应 4xx 状态码。
- 🧩 引入了“等价资源”概念，服务器可通过 Content-Location 返回本次结果资源的 URI，或通过 Location 返回可重复执行同一查询的资源 URI。
- 🔀 对于重定向，301/302/307/308 均要求客户端向新目标重新发送 QUERY；303 则引导客户端用 GET 获取查询结果。
- 🗃️ QUERY 响应可被缓存，缓存键必须包含请求内容和相关元数据；缓存也可对内容进行规范化以提高效率。
- 🏷️ 新增 Accept-Query 响应头字段，以结构化字段语法声明资源支持的查询媒体类型列表。
- 🔐 安全方面需注意：URI 更容易被记录日志，若查询含敏感信息建议使用 QUERY；服务器为结果生成的 URI 不应包含敏感内容；缓存规范化不当可能导致错误响应。
- 📋 IANA 已注册 QUERY 方法（安全、幂等）及 Accept-Query 字段；选择“QUERY”而非 PROPFIND、REPORT 或 SEARCH，因其更贴合 URI 查询组件语义，且不受 WebDAV 历史包袱影响。

---

### [](https://github.com/MasterKale/SimpleWebAuthn/releases/tag/v14.0.0)

**原文标题**: [Release v14.0.0 - The one after they go quantum · MasterKale/SimpleWebAuthn · GitHub](https://github.com/MasterKale/SimpleWebAuthn/releases/tag/v14.0.0)

overview summary
SimpleWebAuthn v14.0.0 釋出重點：伺服器端新增對 ML-DSA 後量子密碼演算法的通行金鑰支援，瀏覽器端則引入 sendSignal() 及更完善的 WebAuthn 能力偵測輔助方法；同時更新多項驗證與相容性功能，並提高 Node.js 與 Deno 的最低版本需求。

- 🚀 伺服器端支援 ML-DSA-44/65/87 後量子簽章演算法，並在支援環境中優先建議註冊 ML-DSA-44 通行金鑰
- 🛜 瀏覽器新增 sendSignal() 方法，統整呼叫 WebAuthn Signal API
- 🔍 新增 browserSupportsPasskeys()，更精確偵測通行金鑰相關 WebAuthn 功能
- 🧩 新增 getBrowserCapabilities()，結合 getClientCapabilities() 作額外功能偵測
- 🔗 verifyAuthenticationResponse() 接受新的 expectedTopOrigin 參數，支援跨來源驗證
- 📝 MetadataService.initialize() 可傳入 logger，自訂 MetadataService 狀態輸出方式
- 🏷️ generateRegistrationOptions() 與 generateAuthenticationOptions() 中的 transports 型別放寬為 string[]
- 🔧 更寬鬆處理 TPM 製造商 ID 的大小寫差異，強化 "tpm" 證明驗證
- ⚙️ generateRegistrationOptions() 與 verifyRegistrationResponse() 現在使用相同的預設 supportedAlgorithmIDs 清單
- 🔏 validateCertificatePath() 支援含交叉簽章憑證的 x5c 陣列
- ⚠️ 破壞性變更：最低執行環境提高為 Node.js LTS 22.x 與 Deno v2.4.x 以上
- 👏 特別感謝貢獻者 agektmr 等社群成員協助本次更新

---

### [](https://github.com/restify/node-restify)

**原文标题**: [GitHub - restify/node-restify: The future of Node.js REST development · GitHub](https://github.com/restify/node-restify)

overview summary：restify 是一个基于 connect 风格中间件的 Node.js REST API 框架，提供服务器与客户端支持，可快速构建和管理 REST 服务。该仓库包含完整文档、示例及 MIT 许可，当前支持 Node.js v22.x、v24.x 和 v26.x。

- 🚀 restify 是用于构建 REST API 的 Node.js 框架，采用 connect 风格中间件架构。
- 📦 可通过 `npm install restify` 轻松安装。
- 🖥️ 服务端示例：使用 `restify.createServer()` 创建服务器，并配合 acceptParser、queryParser、bodyParser 等插件。
- 🔗 客户端示例：通过 `restify-clients` 的 `createJsonClient()` 发起 HTTP 请求。
- ✅ 目前支持 Node.js v22.x、v24.x 和 v26.x。
- 📜 采用 MIT 许可证，可自由使用和修改。
- 🐛 问题反馈可前往 GitHub Issues 页面。
- 📚 更多文档与详情请访问 restify.com。

---

### [](https://github.com/restify/node-restify/releases/tag/v12.0.0)

**原文标题**: [Release v12.0.0 · restify/node-restify · GitHub](https://github.com/restify/node-restify/releases/tag/v12.0.0)

overview summary  
- v12.0.0 是 node-restify 的一个重要版本发布，主要包含破坏性变更、新功能与缺陷修复，并已获得社区积极反馈。

- ⚠️ 破坏性变更：升级 qs 依赖、支持 Node.js 26、移除已废弃的 spdy 协议。
- ✨ 新功能：新增 `useSemicolonDelimiter` 选项，并继续支持 Node.js 26。
- 🔄 维护更新：移除废弃的 spdy 协议、替换废弃的 Node API，改用 WHATWG URL 替代 `url.resolve()` 与 `url.parse()`。
- 📦 依赖升级：更新若干依赖项，并分多次升级 qs 依赖（#1991、#1995）。
- 🐛 Bug 修复：修复 benchmark 测试，并修复 npm 发布工作流问题。
- 👍 社区反响：发布获得 👍、🎉、❤️、🚀 等表情回应，共有 3 人参与互动。

---

### [Zod 4.5](https://zod.dev/blog/zod-4-5)

**原文标题**: [Zod 4.5](https://zod.dev/blog/zod-4-5)

Zod 4.5 正式发布，带来性能、内存和类型安全方面的重大改进。核心亮点是全新的 `z.compile()` 预编译机制和多项 API 增强，并包含一批破坏性 bug 修复。

- 🚀 **旗舰功能 `z.compile()`**：可预编译任意 Zod schema，解析速度提升约 3-9 倍；通过 `import "zod/compile"` 或在入口文件顶部设置，可自动全局编译所有 schema。
- 💳 **新增 `z.creditCard()`**：用于校验信用卡号，支持 12-19 位数字，可含空格或连字符分隔，并执行有效的 Luhn 校验和检查。
- 🔗 **新增 `z.properties()`**：作为 `z.property()` 的多属性版本，可对 `z.instanceof()` schema 进行多个属性的校验。
- 🧩 **回归 `z.deepPartial()`**：以函数形式回归（Zod 4 中曾被移除），递归地将 schema 内所有字段变为可选，且仍返回 `ZodObject`。
- 🎯 **新增 `.exactPartial()`**：类似 `.partial()`，但使用 `z.exactOptional()` 包裹字段，允许省略键但拒绝显式 `undefined`，与 TypeScript 的 `Partial<T>` 在 `exactOptionalPropertyTypes` 下的行为一致。
- ⚡ **新增 `z.validate()`**：提供独立的布尔校验快速路径，无需构造 `ZodError`，无效输入时比 `.safeParse().success` 快达 16 倍；对应异步版本为 `z.validateAsync()`。
- 🔄 **新增 `z.input()` / `z.output()`**：可将 schema 投影到其输入或输出侧，便于独立验证 codec 的双半部分。
- 📝 **新增 `z.toZod<T>()`**：帮助定义一个与已有静态类型完全一致的 Zod schema，schema 本身不会被修改。
- 🗂️ **新增 `z.getDiscriminatedOption()`**：通过判别值直接提取判别联合（discriminated union）中的成员。
- ♻️ **支持循环输入**：Zod 递归 schema 现在可以解析循环引用的数据（Zod Mini 需显式注册 memoizer）。
- 🧠 **内存占用减少 9 倍**：通过方法记忆化和原型链优化，`z.string()` 的堆占用从 7.5kb 降至 784 字节。
- 🏎️ **失败路径大幅提速**：`safeParse()` 不再捕获堆栈跟踪，使验证失败的解析速度提升约 7.5 倍。
- 🔑 **`z.object()` 支持 Symbol 键**：shape 现在可以声明 symbol 类型的键，TypeScript 可正确推断其 `unique symbol` 类型并强制校验。
- ⚠️ **破坏性修复 1**：`z.iso.datetime()` 现在强制要求秒数（RFC 3339），不再接受 `2020-01-01T06:15Z` 这类分钟级精度的输入。
- ⚠️ **破坏性修复 2**：字符串长度（`.min()` / `.max()` / `.length()`）改为按 Unicode 码点而非 UTF-16 码元计数，例如 5 个 emoji 现在能通过 `.max(5)` 校验。
- ⚠️ **破坏性修复 3**：Record 键 schema 和交集（intersection）行为现在与 TypeScript 的索引签名语义对齐，不再错误拒绝对象自身匹配的键。
- ⚠️ **破坏性修复 4**：`__proto__` 键始终被剥离（无论来自输入、schema 声明还是 transform 产生均如此），`.strict()` 模式会将其报告为 `unrecognized_keys`。
- ⚠️ **破坏性修复 5**：若干字符串格式收紧——`z.ipv6()` 直接校验地址字母表、`z.ulid()` 限制首字符为 0-7、`z.httpUrl()` 强制主机名长度限制、`z.emoji()` 消除指数级回溯。
- 🌐 **新增 8 种语言环境**：孟加拉语（bn）、中库尔德语（ckb）、印地语（hi）、卡纳达语（kn）、挪威尼诺斯克语（nn）、巴西葡萄牙语（pt-BR）、斯洛伐克语（sk）和土库曼语（tk）。

---

### [](https://github.com/sindresorhus/np)

**原文标题**: [GitHub - sindresorhus/np: A better `npm publish` · GitHub](https://github.com/sindresorhus/np)

np 是一个更好的 `npm publish` CLI 工具，提供交互式 UI，并在发布前自动执行清理、测试、版本管理、Git 推送等步骤，帮助开发者更安全可靠地发布 npm 包。

- 🎯 **核心定位**：np 旨在替代 `npm publish`，提供交互式发布体验，并自动完成一系列预发布检查。
- ✅ **发布前检查**：确保从发布分支（默认 main/master）发布、工作区干净、依赖已重装、Node/npm 版本兼容。
- 🧪 **自动测试**：发布前自动运行测试脚本，并可使用 `--test-script` 或 `testScript` 配置指定其他测试命令。
- 🔖 **版本管理**：自动更新 `package.json` 和 `package-lock.json` 的版本号，并创建对应的 Git tag。
- 🛡️ **发布安全**：防止预发布版本意外发布到 `latest`；发布失败时自动回滚到之前状态。
- 📤 **推送与 Release**：发布后自动推送 commits/tags 到 GitHub/GitLab，并支持打开预填的 GitHub Release 草稿。
- 🔐 **双因素认证（2FA）**：默认在新包上启用 2FA，并提示使用 2FA 以提升安全。
- 🧪 **预演模式**：提供 `--dry-run`/`--preview`，在不实际推送或发布的情况下查看将执行的任务。
- 📦 **包管理器支持**：支持 npm、pnpm、Bun、Yarn（Classic 和 Berry），并可通过 package.json 的 `packageManager` 字段指定。
- ❌ **不适用场景**：不支持 monorepo；设计为本地交互工具，不适合在 CI 环境中使用。
- 💻 **环境要求**：需要 Node.js 22+、npm 10+、Git 2.11+。
- ⚙️ **安装与使用**：运行 `npm install --global np` 全局安装，然后可用 `np`、`np patch`、`np 1.0.2` 等命令。
- 🗂️ **配置方式**：可在 `.np-config.js`、`.np-config.cjs`、`.np-config.mjs`、`.np-config.json` 或 `package.json` 的 `np` 字段中进行配置；本地配置优先于全局。
- 📝 **常用配置项**：如 `branch`、`cleanup`、`tests`、`yolo`、`dryRun`、`tag`、`contents`、`releaseDraft`、`testScript`、`packageManager` 等。
- 🔗 **npm lifecycle hooks**：可在 `version` 等脚本中添加构建文档等额外操作；也可在 package.json 里自定义 `release` 脚本统一流程。
- 🔏 **已签名 Git tag**：可通过设置 `sign-git-tag`（npm）或 `version-sign-git-tag`（Yarn）来启用 tag 签名。
- 🏠 **私有包支持**：若 `package.json` 声明 `"private": true`，np 会跳过发布步骤，但仍执行版本升级与推送。
- 🌍 **Scoped 包发布**：公开 scoped 包需设置 `publishConfig.access: "public"`；私有 org-scoped 包则设为 `"restricted"`。
- 🏢 **自定义 registry**：可通过 `publishConfig.registry` 指定内部 registry，避免 Yarn 覆盖 registry 导致认证失败。
- 🤖 **CI 发布**：若通过 CI 发布 tagged commits，可使用 `--no-publish` 跳过 np 的发布步骤。
- 🍎 **macOS SSH 问题**：若 SSH passphrase 未保存导致发布前检查挂起，可在 `~/.ssh/config` 添加 `AddKeysToAgent` 和 `UseKeychain`。
- 📋 **忽略策略检查**：np 会提示新增但未进入发布包的 Git 文件，以避免意外忽略必要文件造成包损坏。
- ⚠️ **常见挂起原因**：生命周期脚本不退出、测试命令处于 watch 模式、registry URL 缺少结尾斜杠；解决方法是改用 `release` 脚本、使用 `vitest run` 等非 watch 命令，并确保 registry 以 `/` 结尾。

---

### [](https://github.com/express-rate-limit/express-rate-limit)

**原文标题**: [GitHub - express-rate-limit/express-rate-limit: Basic rate-limiting middleware for the Express web server · GitHub](https://github.com/express-rate-limit/express-rate-limit)

express-rate-limit 是一款 Express 基础限流中间件，用于限制对公共 API、密码重置等端点的重复请求，以缓解滥用。它内置内存存储，同时支持 Redis 等外部数据存储，并提供大量配置项，可灵活调整限流窗口、请求上限、响应头与用户识别方式。

- 🚦 核心功能：基于固定窗口（如 15 分钟）限制每个 IP 的请求次数，默认超出后返回 HTTP 429 状态码。
- 📦 快速上手：导入 `rateLimit`，配置 `windowMs` 与 `limit`，通过 `app.use(limiter)` 即可全局启用。
- 🧩 兼容扩展：可与 express-slow-down、ratelimit-header-parser 配合使用，也支持 Redis、Memcached 等外部数据存储。
- ⚙️ 配置丰富：支持 `message`、`handler`、`statusCode`、`keyGenerator`、`store`、`skip` 等，所有函数选项均可设为异步。
- 📊 响应头控制：可通过 `standardHeaders`（draft-6/7/8）或 `legacyHeaders`（X-RateLimit-*）返回限流相关信息。
- 🌐 用户识别：默认按 IP 识别，可用 `keyGenerator` 自定义；`ipv6Subnet` 可调整 IPv6 匹配位数，以权衡限流粒度。
- ✅ 精细跳过：支持 `skip` 绕过部分请求，也支持通过 `skipSuccessfulRequests` / `skipFailedRequests` 不计入成功或失败请求。
- 🛡️ 容错策略：存储不可用时可用 `passOnStoreError` 选择放行或阻止流量，默认状态码为 429。
- 🤝 开源项目：遵循 MIT 许可证，接受 issue、讨论与贡献，完整文档托管于 Mintlify。

---

### [](https://zuplo.com/?utm_source=node_weekly&utm_medium=newsletter&utm_campaign=cooper_press_unified_1q&utm_content=classified_listing)

**原文标题**: [The Unified Gateway for APIs, AI, and MCP - Zuplo](https://zuplo.com/?utm_source=node_weekly&utm_medium=newsletter&utm_campaign=cooper_press_unified_1q&utm_content=classified_listing)

Zuplo 是一个统一的 API/AI/MCP 网关，通过单一可编程策略引擎管理 API、LLM 与 MCP 调用。它同时覆盖出站（应用调用模型）和入站（AI 代理调用你的 API）双向流量，并提供认证、限流、预算控制、审计、可见性与变现能力，帮助企业安全、可控、高效地运行 AI 相关业务。

- 🔀 统一策略引擎：认证、限速、预算和审计可一次编写，应用到所有 API、LLM 和 MCP 调用，无需引入多个供应商。
- 📥📤 双向流量支持：既管理应用调用 LLM 的出站流量，也管理 AI 代理通过 MCP 访问 API 的入站流量。
- 🤖 代理身份与审计：Claude、Cursor、Codex、ChatGPT 等代理通过 OAuth 2.1/PKCE 认证，每次工具调用都可追溯到客户端、用户及执行的策略。
- 💸 动态成本控制：动态限流可吸收流量高峰，示例显示 14 天节省 4.29 万美元，总支出降低 41%。
- 🎯 团队预算与硬限额：每个 Token 消费归因到团队，并设置预算上限；达到上限后直接返回 429，防止失控代理超支。
- 🛡️ 安全与拦截：认证失败、无效 Schema、提示注入等恶意流量在网关处即被阻断；示例中拦截 12.4k 次请求，0 次到达源站。
- 📈 实时可观测性：仪表盘展示代理/工具调用、延迟、拒绝原因等，并可导出至 Datadog 或 SIEM。
- 💳 内置计量与变现：支持计划、配额、基于用量的计费并直连 Stripe；示例中月计量收入 3 万美元，环比增长 12%。
- 🔌 极简集成：出站只需把 OpenAI SDK 的 baseURL 指向 Zuplo；入站通过 OpenAPI 的 `x-zuplo-route` 扩展即可将操作暴露为 MCP 工具。
- ✅ 企业级特性：99.99% SLA、SOC 2 Type II、分钟级部署，免费层含每月 10 万次请求。
- 🏆 生产验证：Blockdaemon 节省 70% 成本并减少 90% 硬件占用；Finsolutia 数小时上线 MCP 服务器；Yext 获得安全与可扩展性保障。

---

### [支付欺诈检测与防护 | Fingerprint](https://fingerprint.com/use-cases/payment-fraud/?utm_source=NodeWeekly)

**原文标题**: [Payment Fraud Detection and Prevention | Fingerprint](https://fingerprint.com/use-cases/payment-fraud/?utm_source=NodeWeekly)

这段内容旨在强调全面阻止各类交易欺诈，重点防范欺诈性退单、信用卡非法破解以及促销滥用行为。

- 🛡️ 全面停止所有交易欺诈行为
- 💳 防范欺诈性退单（chargeback）与信用卡破解攻击
- 🎁 杜绝促销活动被恶意滥用

---

### [](https://select.supabase.com/?utm_source=newsletter&utm_medium=email&utm_campaign=nodeweekly&dub_id=UvWeQL5Zoytd5n4W)

**原文标题**: [Select26 | Oct 2 | Supabase curated day of talks](https://select.supabase.com/?utm_source=newsletter&utm_medium=email&utm_campaign=nodeweekly&dub_id=UvWeQL5Zoytd5n4W)

Supabase Select 26 是 Supabase 于 10 月 2 日在旧金山举办的线下技术交流活动，仅限受邀申请者入场，门票为每人 256 美元。活动汇聚行业顶尖演讲者，围绕 Supabase 最新动态、Postgres 生态及真实产品构建经验展开，并提供与 Supabase 工程师面对面交流的机会。

- 📅 活动于 10 月 2 日举行，地点为旧金山 555 20th Street。
- 🎟️ 采用线下形式，仅限申请制，每人 $256，需通过 Luma 申请。
- 🗣️ 演讲者包括 Supabase CEO Paul Copplestone、CTO Ant Wilson、Y Combinator 总裁 Garry Tan、前 Twitter CEO Parag Agrawal 等。
- 👥 其他嘉宾还有 Michael Seibel、Dalton Caldwell、Thomas Dohmke，以及来自 Anthropic 的 Katelyn Lesse 和 Angela Jiang 等。
- 🔭 抢先获取 Supabase 即将发布的一手信息，了解当下热议的开发者工具公司与 Postgres 最新进展。
- 🛠️ 每个环节聚焦真实产品的构建方法，包括主舞台炉边对话与 Build Stage 功能深度剖析。
- 🤝 可在 Ask Supabase 展位直接与 Supabase 工程师交流，带来你最棘手的问题。
- 🎫 门票现已开放申请，另有赞助商即将公布，也接受演讲者申请。

---

### [](https://four.htmx.org/announcements/2026-08-28-htmx-4.0.0-is-released)

**原文标题**: [htmx 4.0.0 has been released! ~ htmx](https://four.htmx.org/announcements/2026-08-28-htmx-4.0.0-is-released)

htmx 4.0.0 正式发布，这是 8 个月工作的成果，核心从 XMLHttpRequest 迁移到 fetch()，同时引入了属性继承显式化、事件名标准化、历史缓存调整等主要变化。2.x 在 npm 中仍保持 latest，4.0 作为 next，htmx 2 会继续获得长期支持。

- 🎉 发布背景：历时 8 个月，受 fixi 项目启发，并在 Christian 的流式 HTML 想法推动下完成向 fetch() 的内部迁移。
- ⚠️ 版本策略：npm 上 4.0 暂不设为 latest，2.x 继续为 latest 且无限期支持；官网已改用 4.0。
- 🔄 属性继承：htmx 2 的隐式继承改为显式，需要继承的父级属性必须加上 :inherited 后缀，例如 hx-confirm:inherited="..."；旧的 hx-disinherit 等已不再需要。
- 🏷️ 事件名标准化：事件统一为 htmx:phase:action 格式，如 htmx:beforeRequest 变成 htmx:before:request；多数错误事件归并为 htmx:error，xhr 与 validation 事件被移除。
- 🕰️ 历史支持：不再用 localStorage 快照页面，后退时重新 fetch 并替换 body；若需本地缓存可使用新的 hx-history-cache 扩展。
- ✨ 新特性：支持 morph swaps（基于 idiomorph）和全新的 <hx-partial> 标签，可更清晰地进行多区域 DOM 更新；并推出 hx-live 脚本方案。
- 🧩 扩展生态：新增 hx-preload、hx-download、hx-alpine-compat、hx-history-cache 等；流式扩展支持 SSE、WebSocket 和 multipart；htmax.js 打包了常用扩展。
- 🔧 升级工具：通过 npx htmx.org@4.0.0 upgrade-check 可扫描模板，找出需要 :inherited 的属性、旧事件名和已移除 API 等问题。
- 📦 安装与资源：可通过 CDN（如 unpkg 4.0.0）或包管理器安装；还提供了面向 LLM 的技能文件（htmx-guidance、htmx-debugging 等）。
- 🙏 致谢与展望：感谢 Michael、Christian、Alex 等核心贡献者；htmx 2 用户无需强制升级，可安心过渡。

---

### [](https://four.htmx.org/docs/whats-new-in-htmx-4)

**原文标题**: [What's New in htmx 4 ~ htmx](https://four.htmx.org/docs/whats-new-in-htmx-4)

htmx 4 是一次重大版本升级，引入了破坏性变更、属性重命名以及多项新特性，全面转向 fetch()，要求显式继承，并提供了更丰富的响应处理与事件系统。

- 🔄 所有请求改用原生 fetch()，不再支持 XMLHttpRequest，无法回退。
- 🧬 属性继承需显式添加 `:inherited`，可用 `:append` 叠加，旧隐式继承可通过配置恢复。
- 🌐 所有 HTTP 响应（除 204/304）默认参与 DOM 交换，4xx/5xx 错误页也会被换入目标。
- 📤 `hx-delete` 不再自动包含表单数据，需手动添加 `hx-include="closest form"`。
- 🗄️ 历史记录不再用 localStorage 缓存，后退时重新请求页面。
- 🔄 OOB 交换顺序调整：先交换主内容，再处理 OOB/`<hx-partial>` 元素。
- ⏳ 移除 `hx-trigger` 的 `queue:` 修饰符，改用 `hx-sync` 控制请求排队。
- 💬 `from:`/`target:` 选择器含空格或逗号时需用单引号包裹。
- ⏱️ 新增默认 60 秒请求超时，可配置 `defaultTimeout` 恢复为 0。
- 📦 扩展无需通过 `hx-ext` 属性加载，直接引入脚本即可，可用 meta 限制允许的扩展。
- 🔁 属性迁移：`hx-disable` 改为 `hx-ignore`，`hx-disabled-elt` 变为 `hx-disable`，另有 `hx-vars`、`hx-params`、`hx-prompt`、`hx-ext` 等被移除或调整。
- 🏷️ 事件全面重命名并统一为 `htmx:phase:action` 模式，错误事件合并到 `htmx:error` 和 `htmx:response:error`。
- ⚙️ 配置项大量更名，如 `timeout`→`defaultTimeout`、`historyEnabled`→`history`、`globalViewTransitions`→`transitions`、`defaultSwapStyle`→`defaultSwap`。
- 🚧 移除多项旧 API（如 `htmx.addClass` 改用原生 classList），简化 JavaScript 接口。
- 🌟 新增属性：`hx-action`、`hx-method`、`hx-query`、`hx-config`、`hx-ignore`、`hx-validate` 等。
- 🖱️ `hx-swap` 扩展：支持 `innerMorph`/`outerMorph`/`textContent`/`delete` 新样式，并引入 `show`/`scroll` 的独立修饰键。
- 🔢 新增基于状态码的交换控制：`hx-status:422` 等可为不同状态码指定不同 swap 策略。
- 📑 引入 `<hx-partial>` 标签，可从一个响应中指定多个目标进行局部更新。
- ✨ 支持 View Transitions API（默认关闭），并增加 JSX 友好的 `metaCharacter` 配置替换冒号。
- 📡 新增 `htmx.timeout()` 等 JavaScript 方法，核心工具类方法迁移至 `hx-live` 扩展。
- 🧩 提供一系列核心扩展（如 `hx-multipart`、`hx-sse`、`hx-ws`、`hx-live`、`hx-prompt`、`hx-targets` 等），并附兼容扩展 `htmx-2-compat` 帮助平滑升级。

---

### [](https://yob.id.au/2026/09/01/major-version-bumps.html)

**原文标题**: [
    
      Bumping the major version of your Javascript library is user hostile · James Healy
    
  ](https://yob.id.au/2026/09/01/major-version-bumps.html)

该文章批评 JavaScript 库频繁进行主版本升级，给用户带来沉重负担，并呼吁维护者减少破坏性变更、优化依赖管理，以帮助用户整合依赖版本、降低安全维护成本。

- 📦 作者所在项目竟同时使用 8 个版本的 glob、7 个 minimatch、3 个 brace-expansion，跨 5 条主版本线，导致依赖碎片化严重。
- ⚠️ 过去 12 个月这些包引发数十个 GitHub 安全警报，虽大多不可利用，但消耗大量工程时间排查，也迫使维护者处理大量依赖约束更新请求。
- 🧱 根本原因在于 Node 依赖系统允许同一包多版本共存，使破坏性变更看似代价低廉，实则将升级成本转嫁给下游用户。
- 🙏 恳请库维护者尽量少做主版本升级：语义化版本虽允许破坏性变更，但不等于必须频繁使用，最好每 2-3 年才 bump 一次 major。
- 🔧 优先采用增量 API 扩展并弃用而非移除旧功能，慎重移除旧 Node 版本支持，避免不必要地更改 ESM 默认导出。
- 🧩 尽量减少运行时依赖和 peer 依赖（当前 npm 热门包中约 47% 零依赖），这既能减轻用户负担，也降低自身维护压力。
- 📏 若必须依赖，选择主版本升级不频繁且表现良好的包，并声明尽量宽的范围，例如使用 `axios: ^1` 而非 `^1.18.0`，让下游能灵活去重和修复漏洞。
- 🔀 可像 `brace-expansion: ^2 || ^3 || ^4` 一样同时兼容多个主版本，给解析器更多选择空间，帮助用户避免安全漏洞。
- ⭐ 表扬 debug、semver、strip-ansi、axios 等优秀案例：它们长期维持少数主版本线，通过大量 minor 版本迭代，极大减轻用户升级压力。
- 💬 引用 semver.org 与 Mike Taylor 观点：破坏性变更应谨慎权衡成本与收益；即使 bump major，用户仍需阅读更新日志、修改代码并验证，负担并未消失。

---

### [](https://yui.dev/blog/minesweeper-in-247-bytes)

**原文标题**: [The Depths of JavaScript: Minesweeper in 247 Bytes](https://yui.dev/blog/minesweeper-in-247-bytes)

概述：这篇文章详细解说了如何用 247 个字节的 JavaScript 实现一个可玩的扫雷游戏，包括代码压缩技巧、HTML 解析特性、一维数组思维、位运算与类型转换的巧妙运用，以及作者与 DNEK 共同进行代码高尔夫优化的过程。

- 🧩 仅用 247 个字符实现 8x8 扫雷，支持左键开格、右键插旗、递归翻开空白格和胜利检测。
- ⚙️ 核心分为两个函数：`b` 负责游戏逻辑，`m` 负责生成界面与棋盘，并通过函数内定义省去分隔符字节。
- 🏷️ 利用 HTML 解析器自动闭合 `<a>` 和 `<p>` 的特性，省略所有闭合标签，大幅压缩代码。
- 🖱️ 用 `onmouseup` + `event.which` 统一处理左右键，用 XOR 切换单元格状态，但代价是右键插旗需要点两次。
- 🗃️ 不额外创建数组，而是把游戏状态直接存在函数对象 `b` 和 `m` 的属性上，作为一维“数组”使用。
- 🎲 棋盘初始化用 `Math.random()<0.1` 生成雷区，并通过 `??=` 保证只初始化一次，同时用逗号表达式压缩逻辑。
- 🔣 可见棋盘用整数表示，再通过 `"*#F"` 映射成 `*`（雷）、`#`（未开）、`F`（旗）；已开格子用负数存储并用 `~x` 转换显示。
- ➕ 用一维偏移量替代二维循环，检查邻居雷数并递归开格，利用右侧隐藏列和 `undefined` 的假值避免越界问题。
- 🔀 通过 `map` 与位运算技巧，在递归时同时完成打开空格、计数、更新棋盘与重绘 UI。
- ✂️ 大量使用位运算（`|`、`&`、`^`、`~`）和字符串拆解技巧，例如用 `~9` 代替 `-10`、用展开运算符拆分数字字符串。
- 🧠 最终版本从 658 字节逐步压缩到 247 字节，期间与 DNEK 反复试验，但并未移除主要功能。
- 🎯 由于柯尔莫哥洛夫复杂性不可计算，无法证明这是最小实现，但作者认为已非常接近极限。
- 💡 作者感叹代码高尔夫是“无聊但美丽的艺术”，也借机展示 JavaScript 的灵活与怪异之处。

---

### [Node.js 用户调查 2026](https://linuxfoundation.surveymonkey.com/r/nodejs-users-2026)

**原文标题**: [Node.js User Survey 2026](https://linuxfoundation.surveymonkey.com/r/nodejs-users-2026)

overview summary
- 🌍 询问当前居住国家或地区，提供全球各国及地区的长列表供选择。
- 🗣️ 调查主要使用语言，包含英语、法语、中文等常见语言及“其他”选项。
- 🏢 了解职业所在的组织类型，涵盖学术、政府、企业、非营利等分类。
- 💼 针对公司从业者，进一步询问所在行业领域，如科技、金融、医疗等。
- 👥 统计组织规模，按员工或成员人数划分五个区间，从 1 人到 1000 人以上。

---

