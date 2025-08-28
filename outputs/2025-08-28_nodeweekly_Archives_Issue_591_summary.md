### [Node Weekly 第 591 期：2025 年 8 月 26 日](https://nodeweekly.com/issues/591)

**原文标题**: [Node Weekly Issue 591: August 26, 2025](https://nodeweekly.com/issues/591)

概述一份关于 JavaScript 和 Web 开发最新动态的简报，包含工具更新、技术文章和行业资讯。

- 📧 邮件订阅服务，支持随时退订并保障隐私安全
- 🚀 Node.js v23.6+ 支持直接运行 TypeScript 代码（通过类型剥离），Calm 团队分享了迁移经验
- ⚡ JavaScript 生态性能优化：semver 库速度提升 33 倍，Bun 1.2.1 发布（含 500 倍速的 postMessage 优化）
- 🔧 工具更新：ESLint 支持多线程检测，Next.js 15.5 稳定支持 Node 中间件，Vercel 支持 fetch 处理器
- ❄️ Porffor 编译器解决 AWS Lambda 的 JavaScript 冷启动问题（启动时间<1 毫秒）
- 📚 技术文章：Promise.any() 解析、Intl 单元格式化、Promise 基础教程等
- 🛠️ 新工具推荐：Cronicle（分布式任务调度）、ImageJS（图像处理）、Rocketadmin（无代码管理后台）
- 🌈 开发库更新：pg-promise、yoctocolors、Faker、OpenAI Node 等 20+ 工具版本升级
- 🔍 生态动态：Big O 符号图解指南、JS 压缩器基准测试、CSS random() 函数介绍、AWS 认知更新

---

### [我们如何将 Rush.js 单体仓库迁移至 Node 类型剥离——Calm 博客](https://blog.calm.com/engineering/how-we-migrated-our-rushjs-monorepo-to-node-type-stripping)

**原文标题**: [How we migrated our Rush.js monorepo to Node type stripping — Calm Blog](https://blog.calm.com/engineering/how-we-migrated-our-rushjs-monorepo-to-node-type-stripping)

概述了将 Rush.js monorepo 迁移到 Node 类型剥离的过程，包括迁移动机、技术挑战、实施策略和最终效果。

- 🚀 通过跳过转译直接运行 TypeScript 文件，使本地开发任务提速 30-40%，CI 流程节省 3-6 分钟
- ⚠️ 最大挑战是重构数千处 Sinon 模块桩/间谍代码，采用"桩类而非模块"的新测试策略
- 🔧 必须迁移到 ESM 模块系统，修复文件扩展名、JSON 导入属性等兼容性问题
- 📦 为 Rush.js 项目导入创建条件导出配置，解决.ts 扩展名在生产环境的路径问题
- 🧪 编写自定义 ESLint 规则和 codemod 工具逐步重构，防御式推进迁移
- ⚡ 移除了所有转译步骤和 source map，保留类型检查但设置 noEmit: true
- 💡 使用 Node 实验性标志 (--experimental-strip-types) 逐步启用类型剥离功能
- 📊 量化收益：单测文件运行速度从 6.6 秒降至 4.4 秒，团队每月节省约 100 小时 CI 时间

---

### [Node.js](https://nodejs.org/en/blog/release/v22.18.0)

**原文标题**: [Node.js](https://nodejs.org/en/blog/release/v22.18.0)

Node.js v22.18.0 LTS 版本发布，主要特性包括默认启用 TypeScript 类型剥离功能，并带来多项模块、文件系统、权限管理等核心功能更新。

- 🚀 默认启用实验性 TypeScript 类型剥离功能，无需配置可直接运行.ts 文件
- ⚠️ 类型剥离功能仍存在语法限制，可通过--no-experimental-strip-types 禁用
- 🔧 新增 import.meta.main 支持，改进 ES 模块功能
- 📁 文件系统优化：增强 fs-events 异步迭代器处理能力，改进目录操作
- 🔐 权限管理增强：支持 addon 权限检查，完善 spawn 操作的权限标志传播
- 💾 SQLite 扩展：新增 readBigInts 连接选项支持
- 🌐 URL 模块新增 fileURLToPathBuffer API
- 👀 监视模式：新增--watch-kill-signal 终止信号配置选项
- 🧵 Worker 线程支持异步销毁接口
- 📦 依赖项更新：npm 升级至 10.9.3，SQLite 升级至 3.50.2

---

### [Node.js — 原生运行 TypeScript](https://nodejs.org/en/learn/typescript/run-natively)

**原文标题**: [Node.js — Running TypeScript Natively](https://nodejs.org/en/learn/typescript/run-natively)

Node.js 从 v23.6.0 开始默认支持 TypeScript 类型剥离功能，允许直接运行仅含可擦除类型语法的代码，无需转译。

- 🚀 从 v22.6.0 开始，Node.js 通过 `--experimental-strip-types` 标志实验性支持 TypeScript 类型注解剥离
- 🔄 v22.7.0 新增 `--experimental-transform-types` 标志，支持转换 `enum` 和 `namespace` 等语法
- ✅ v23.6.0 起默认启用类型剥离功能，可直接运行 `node file.ts`
- ⚠️ 需要转换的语法（如枚举）仍需使用 `--experimental-transform-types` 标志
- 📝 无需 `tsconfig.json`，但建议配置编辑器与 TypeScript 5.7+ 保持行为一致
- 🔮 未来版本将无需命令行标志即可完整支持 TypeScript
- ⚠️ 当前仍存在实验性限制，建议查阅 API 文档并酌情使用替代方案

---

### [加速 JavaScript 生态系统 - 语义化版本](https://marvinh.dev/blog/speeding-up-javascript-ecosystem-part-12/)

**原文标题**: [Speeding up the JavaScript ecosystem - Semver](https://marvinh.dev/blog/speeding-up-javascript-ecosystem-part-12/)

文章探讨了 JavaScript 生态中包管理器安装过程中 semver 库的性能问题，通过优化解析逻辑和避免重复验证，可将版本比较速度提升 33 倍。

- 🚀 作者发现 npm install 过程耗时过长，经分析发现 semver 库在 Preact 项目安装中被调用超过 2.1 万次
- 🔍 主要耗时函数为 satisfies（11,151 次）、valid（4,878 次）和 validRange（4,911 次），存在重复验证问题
- ⚡ 通过消除验证函数与解析函数的重叠操作（遵循"解析而非验证"原则），性能提升约 70%
- 💾 现有 LRU 缓存方案效果有限（仅节省 133ms），作者认为缓存应是最后手段而非首选优化方案
- 🛠️ 作者实现自定义解析器，即使保留验证步骤也比原库快 25 倍，去除验证后仍快 10 倍，综合提升达 33 倍
- 📦 该优化适用于 npm/yarn/pnpm 等主流包管理器，能显著提升整个 JavaScript 生态的依赖安装速度

---

### [Bun v1.2.21 | Bun 博客](https://bun.com/blog/bun-v1.2.21)

**原文标题**: [Bun v1.2.21 | Bun Blog](https://bun.com/blog/bun-v1.2.21)

Bun 发布新版本，修复了 69 个问题，新增多项功能，包括统一的 SQL 客户端 Bun.SQL、原生 YAML 支持、性能优化、安全增强和开发者工具改进。

- 🚀 新增 Bun.SQL 统一客户端，支持 MySQL、SQLite 和 PostgreSQL，无需额外依赖
- 📄 内置 YAML 解析器，支持直接导入.yaml 文件和运行时解析
- ⚡ postMessage(string) 性能提升 500 倍，字符串传输和克隆更高效
- 🔒 新增 Bun.secrets，基于操作系统原生凭证存储管理敏感信息
- 🔍 bun install 支持安全扫描 API，可在安装前检测包漏洞
- 🎯 bun audit 新增过滤选项，支持按严重级别、生产依赖和特定 CVE 忽略
- 📦 bun install --lockfile-only 优化，仅获取包清单提升速度
- 🖱️ bun update --interactive 支持滚动和响应式终端显示
- 💤 减少 Bun.serve 空闲 CPU 使用，无请求时进程真正休眠
- 🛠️ Bun.build() 支持编译可执行文件，包括跨平台和 Windows 元数据设置
- 🏷️ bun build --compile 支持嵌入运行时参数和 Windows 可执行文件元数据
- 🧹 新增 Bun.stripANSI()，SIMD 加速去除 ANSI 转义码
- ✅ Windows 版 bun.exe 现已代码签名，消除安全警告
- 📦 bunx 支持--package 标志，运行包中不同名二进制文件
- 🌐 package.json sideEffects 支持通配符模式，优化 tree-shaking
- 🌍 新增--user-agent 标志，自定义所有 fetch 请求的 User-Agent 头
- 🔧 多项 Node.js 兼容性改进和 bug 修复

---

### [500 倍速的 postMessage(字符串) | Bun 博客](https://bun.com/blog/how-we-made-postMessage-string-500x-faster)

**原文标题**: [500x faster postMessage(string) | Bun Blog](https://bun.com/blog/how-we-made-postMessage-string-500x-faster)

Bun v1.2.21 通过优化字符串在线程间的传输机制，实现了 postMessage 性能的显著提升，特别适用于多线程 JavaScript 服务器和 CLI 工具。

- 🚀 Bun v1.2.21 的 postMessage(string) 性能几乎与字符串大小无关，比之前版本快达 500 倍
- 💾 峰值内存使用减少约 22 倍，通过避免安全字符串的序列化实现
- 📊 在 3MB 字符串传输测试中，Bun 仅需 593 纳秒，而之前版本需要 326 微秒
- 🧠 利用 JavaScriptCore 字符串本身线程安全的特性（引用计数使用 std::atomic）
- ⚡ 优化自动触发条件：纯字符串传输、非子串/原子字符串、长度≥256 字符
- 📡 特别适合 API 服务器、数据处理管道等需要传输大型 JSON 数据的场景
- 🔮 未来可能扩展至对象和数组中的字符串值优化

---

### [ESLint v9.34.0 新特性：多线程代码检查 - ESLint - 可插拔 JavaScript 代码检查工具](https://eslint.org/blog/2025/08/multithread-linting/)

**原文标题**: [New in ESLint v9.34.0: Multithread Linting - ESLint - Pluggable JavaScript Linter](https://eslint.org/blog/2025/08/multithread-linting/)

ESLint v9.34.0 正式推出多线程检查功能，通过利用多核 CPU 并行处理文件，显著提升大型项目的代码检查速度。

- 🚀 支持多线程检查，可同时处理多个文件，大幅减少大型项目的检查时间
- ⚙️ 提供三种并发模式：数字指定线程数、自动模式（auto）以及关闭多线程（off）
- 📊 测试显示性能提升显著，早期测试者报告速度提升最高达 3.01 倍
- 🔧 自动模式根据 CPU 核心数和文件数量智能选择线程数，默认为 CPU 核心数的一半
- ⚠️ 需要注意选项的可克隆性限制，非可克隆值（如函数）会导致错误
- 📦 引入选项模块（Options Modules）解决克隆限制问题，支持通过模块导入配置
- 🖥️ 同时支持 CLI 和 Node.js API 使用多线程功能
- 💡 建议通过基准测试选择最佳线程数，并结合缓存功能进一步提升性能
- 🌐 在 CI 和容器环境中可能需要重新测试以确认性能提升效果

---

### [Node.js Vercel Functions 现已支持 fetch web 处理程序 - Vercel](https://vercel.com/changelog/node-js-vercel-functions-now-support-fetch-web-handlers)

**原文标题**: [Node.js Vercel Functions now support fetch web handlers - Vercel](https://vercel.com/changelog/node-js-vercel-functions-now-support-fetch-web-handlers)

Vercel Functions 现支持基于 Node.js 运行时的 fetch Web 处理程序，提升了 JavaScript 运行时与框架间的互操作性。

- 🌐 支持 fetch Web 处理程序
- ⚡ 提升 JavaScript 运行时互操作性
- 🔄 兼容传统 HTTP 方法导出方式
- 📚 提供官方文档指导

---

### [Next.js 15.5 | Next.js](https://nextjs.org/blog/next-15-5)

**原文标题**: [Next.js 15.5 | Next.js](https://nextjs.org/blog/next-15-5)

Next.js 15.5 版本发布，包含 Turbopack 构建功能进入测试阶段、Node.js 中间件稳定化、TypeScript 改进、next lint 弃用以及 Next.js 16 的弃用警告。

- 🚀 Turbopack 构建进入测试阶段，生产环境构建速度提升显著，支持大规模项目优化
- ⚙️ Node.js 中间件运行时正式稳定，支持完整 Node.js API 和复杂用例处理
- 📘 TypeScript 路由类型改进，提供编译时类型安全和自动生成全局类型支持
- ⚠️ next lint 命令已弃用，推荐迁移至显式 ESLint 配置或 Biome 工具
- 🔔 新增 Next.js 16 弃用警告，涉及 legacyBehavior、AMP 支持及 Image 组件配置调整
- 📦 提供自动化升级工具和详细迁移指南，帮助开发者平滑过渡到新版本

---

### [消除 AWS Lambda 中的 JavaScript 冷启动](https://goose.icu/lambda/)

**原文标题**: [Eliminating JavaScript cold starts on AWS Lambda](https://goose.icu/lambda/)

Porffor 是一种可将 JavaScript 提前编译为 WebAssembly 和原生二进制文件的引擎，现已在 AWS Lambda 上运行，显著优化冷启动性能和成本效率。

- 🚀 Porffor 将 JS 编译为原生二进制文件（<1MB），冷启动速度比 Node 快约 12 倍，比 LLRT 快近 4 倍  
- 💰 在 Lambda 上运行成本比 Node 低 2 倍以上，且不受托管运行时初始化计费策略影响  
- ⚠️ 目前仅支持约 60% JS 特性，缺乏完整 I/O 和 Node 兼容性，处于早期开发阶段  
- 📊 测试代码及数据已开源，适用于无复杂依赖的小型 Lambda 函数场景  
- 📧 作者邀请适合场景的用户联系试用，但强调工具尚未达到生产就绪状态

---

### [紫红](https://porffor.dev/)

**原文标题**: [Porffor](https://porffor.dev/)

Porffor 是一款将 JavaScript 提前编译为 WebAssembly 和原生二进制文件的编译器，旨在解决传统 JS 运行时的性能与体积问题，支持 TypeScript 并无须转译。

- 🚀 编译性能卓越：WebAssembly 输出体积和速度比现有方案提升 10-30 倍，原生二进制体积缩小 1000 倍（从 90MB 降至<100KB）
- 🔒 增强安全性：支持 Wasm 沙箱隔离执行，避免逆向工程，适合敏感代码和边缘计算场景
- 🎯 多场景适用：原生编译支持嵌入式设备、游戏主机和 CLI 工具，生成小于 1MB 的可执行文件
- ⚙️ 技术架构创新：完全重写的 AOT 编译器，采用 JS 编写避免内存安全问题，支持静态优化
- 📉 当前限制：不支持运行时 eval 等动态执行，处于预 Alpha 阶段，2025 年可用性初步完善
- ✅ 标准兼容：通过 Test262 测试套件验证 ECMAScript 合规性，提供在线体验和本地安装方式

---

### [理解 Promise.any()：一个成功即为足矣 - 马特·史密斯](https://allthingssmitty.com/2025/08/25/understanding-promise-any-when-one-success-is-enough/)

**原文标题**: [
    Understanding Promise.any(): when one success is enough - Matt Smith
  ](https://allthingssmitty.com/2025/08/25/understanding-promise-any-when-one-success-is-enough/)

Promise.any() 是 JavaScript 中处理异步操作的方法，它会在传入的 Promise 数组中返回第一个成功解析的结果，忽略所有失败，仅当所有 Promise 都失败时才抛出 AggregateError 错误。

- 🎯 返回第一个成功的 Promise 结果，忽略失败
- ⚠️ 全部失败时抛出 AggregateError 错误，包含所有错误信息
- 🔄 不取消其他进行中的 Promise，需手动使用 AbortController 控制
- 🌐 适用于多镜像 API 请求或功能降级场景
- 📱 浏览器支持 Chrome 85+、Firefox 79+、Safari 14+ 等现代版本
- ⚖️ 与 Promise.all()、Promise.race() 等方法形成互补，根据需求选择使用

---

### [JavaScript 中使用 Intl 进行单位格式化](https://www.raymondcamden.com/2025/08/22/unit-formatting-with-intl-in-javascript)

**原文标题**: [Unit Formatting with Intl in JavaScript](https://www.raymondcamden.com/2025/08/22/unit-formatting-with-intl-in-javascript)

文章概述了 JavaScript 中 Intl API 的单位格式化功能，重点介绍了数字与单位结合的区域化显示方法，并分享了处理文件大小格式化的实用代码示例。

- 📅 作者回顾了过去几年对 Intl API 的探索历程，包括时间格式化和动态时长处理
- 📏 重点介绍 NumberFormat 的 unit 样式，用于格式化带单位的数字（如 5 盎司、9 磅）
- 🌍 支持通过 Intl.supportedValuesOf('unit') 获取所有可用单位列表（包含 acre、bit、byte 等 46 种单位）
- 💻 提供了实时演示链接，展示不同区域设置下的单位格式化效果
- 💾 分享了一个智能的文件大小格式化函数，可自动选择合适单位（字节到 TB）并进行本地化渲染
- 🔢 特别提到 JavaScript 数字可使用下划线分隔符（如 1_024）提升可读性
- 📝 作者最后表达了求职意向，寻求开发者布道师相关职位

---

### [从零开始的 Promise 探索 • 乔希·W·科莫](https://www.joshwcomeau.com/javascript/promises/)

**原文标题**: [Promises From The Ground Up • Josh W. Comeau](https://www.joshwcomeau.com/javascript/promises/)

本文介绍了 JavaScript 中 Promise 的概念、工作原理及其在异步编程中的应用，从回调地狱问题出发，逐步解析 Promise 的创建、链式调用、错误处理，并最终引入 async/await 语法糖。

- 🚀 Promise 是 JavaScript 处理异步操作的核心 API，用于解决回调地狱问题，需结合事件循环机制理解
- ⏰ JavaScript 单线程特性导致无法使用同步休眠函数，setTimeout 等异步方法通过回调实现非阻塞等待
- 🔗 Promise 有三种状态：pending（进行中）、fulfilled（已成功）、rejected（已失败），通过.then() 和.catch() 处理不同状态
- 🛠️ 可通过 new Promise() 自定义 Promise 对象，resolve 和 reject 参数分别控制成功和失败状态
- ➰ Promise 链式调用允许顺序执行多个异步操作，通过 return 传递新 Promise 实现连续异步任务
- 📦 Promise 可传递数据，resolve(value) 可将数据传递给后续.then() 回调
- ❌ 使用 reject() 处理异步操作失败情况，.catch() 专门捕获拒绝状态的 Promise
- ✨ async/await是Promise的语法糖，async函数隐式返回Promise，await可"同步"等待异步操作完成
- 🌐 现代 Web API（如 fetch）基于 Promise 构建，但需注意 HTTP 错误状态不会自动触发 reject
- 🔄 事件循环机制是 Promise 异步执行的底层支撑，保证非阻塞调用和准确的事件调度

---

### [编年史](https://cronicle.net/)

**原文标题**: [Cronicle](https://cronicle.net/)

Cronicle 是一个基于 Node.js 的多服务器任务调度和运行系统，提供 Web 前端界面，支持定时、重复和按需任务，无需数据库即可运行。  
- 🚀 多服务器任务调度器，支持自动故障转移和任务重试  
- ⏰ 可视化时间选择器设置单次或循环任务  
- 🎯 可定制运行模式（指定服务器或随机分组）  
- 📊 实时统计与日志查看，含进度条和预估时间  
- 📈 自动追踪 CPU/内存使用量及历史性能图表  
- 🔌 支持多语言插件 API 和自定义 UI 参数  
- 🌍 多时区自动检测与事件调度  
- ⛓️ 事件链式触发与数据传递  
- 🔑 提供 REST API 和 Webhook 通知  
- 📁 无数据库依赖，数据存储为 JSON 文件  
- 📜 开源 MIT 许可，基于 Node.js 开发

---

### [GitHub - jhuckaby/Cronicle：一个简单的分布式任务调度器和运行器，带有基于Web的用户界面。](https://github.com/jhuckaby/Cronicle)

**原文标题**: [GitHub - jhuckaby/Cronicle: A simple, distributed task scheduler and runner with a web based UI.](https://github.com/jhuckaby/Cronicle)

Cronicle 是一个基于 Node.js 开发的分布式任务调度和运行系统，提供 Web 界面管理，支持多服务器部署和故障自动转移，可作为功能增强版的 Cron 替代方案。

- 🕒 支持单机或多服务器集群部署，具备主备服务器自动故障转移和节点自动发现功能
- 🌐 提供 Web 管理界面，实时监控任务状态并支持实时日志查看
- 🔌 插件系统支持任何语言编写任务，提供简单的 JSON 消息通信机制
- 📅 支持多时区调度，可处理定时、重复和按需任务，支持任务队列管理
- 📊 记录任务历史统计和性能图表，监控 CPU 和内存使用情况
- 🔑 提供 REST API 和 API 密钥认证，支持外部系统集成和 Webhook 通知
- ⚖️ 采用 MIT 开源协议，已知被 Agnes & Dora 和 Sling TV 等公司使用
- ⭐ GitHub 获得 4.8k 星标，最新版本 0.9.90（2025 年 8 月发布）

---

### [ImageJS 1.0 发布 | ImageJS](https://docs.image-js.org/blog/releases/1.0/)

**原文标题**: [Announcing ImageJS 1.0 | ImageJS](https://docs.image-js.org/blog/releases/1.0/)

ImageJS 1.0 版本正式发布，带来 TypeScript 支持、更直观的 API 设计及多项功能优化与新增，同时包含部分破坏性变更和移除旧功能。

- 🎯 全面支持 TypeScript，提供严格类型定义，减少运行时错误并增强 IDE 智能提示
- ⚠️ 包含多项破坏性变更：如图像加载/保存改用 `read()`/`write()`、坐标系统改用 `Point` 对象、二进制图像由专用 `Mask` 类处理
- 🔄 API 方法名称调整：如绘图方法统一使用 `draw` 前缀、堆栈方法简化命名（`getMinImage()` → `minImage()`）
- 🆕 新增功能：图像变换（`transform()`）、双三次插值缩放、Prewitt 滤波器、颜色校正（`correctColor()`）、像素化效果（`pixelate()`）等
- 🎨 Mask 类增强：支持 Feret 直径计算、边框点提取和清除连接图像边框的区域
- 📊 Stack 类扩展：新增筛选（`filter()`）、映射（`map()`）、中值图像生成和像素值访问方法
- 🐛 修复了 `cannyEdgeDetector()`、`resize()` 和 `drawCircle()` 等多个函数的错误
- 📖 提供完整的 API 文档和示例教程，鼓励社区贡献

---

### [功能 | ImageJS](https://docs.image-js.org/docs/Features/)

**原文标题**: [Features | ImageJS](https://docs.image-js.org/docs/Features/)

概述：本文介绍了图像处理和分析中的关键功能模块及其包含的工具数量。

- 🗃️ 过滤器：包含 9 种图像处理工具
- 📊 比较功能：提供 5 项对比分析操作
- 📐 几何处理：涵盖 6 种几何变换工具
- 🔬 形态学操作：包含 8 种形态学处理方法
- ⚙️ 运算功能：提供 6 种图像运算操作
- 🎯 感兴趣区域：包含 13 种 ROI 处理工具

---

### [GitHub - image-js/fast-jpeg: 完全用 JavaScript 编写的 JPEG 图像解码器](https://github.com/image-js/fast-jpeg)

**原文标题**: [GitHub - image-js/fast-jpeg: JPEG image decoder written entirely in JavaScript](https://github.com/image-js/fast-jpeg)

这是一个完全用 JavaScript 编写的 JPEG 图像解码器开源项目，主要用于读取 JPIF 信息而非完整图像数据解码。

- 🖼️ 纯 JavaScript 实现的 JPEG 解码器，当前仅支持 EXIF 信息读取
- 📦 通过 npm 安装（npm install fast-jpeg），采用 MIT 开源协议
- ⭐ GitHub 项目获得 7 个 star 和 1 个 fork，由 Zakodium 团队维护
- 🔧 项目主要使用 TypeScript（90.1%）和 JavaScript（9.9%）开发
- 🌐 提供完整的 API 文档，可通过 jpeg.decode(data) 方法调用

---

### [GitHub - image-js/fast-png: 完全使用 JavaScript 编写的 PNG 图像解码器和编码器](https://github.com/image-js/fast-png)

**原文标题**: [GitHub - image-js/fast-png: PNG image decoder and encoder written entirely in JavaScript](https://github.com/image-js/fast-png)

一个完全用 JavaScript 编写的 PNG 图像解码器和编码器库，支持 Node.js 环境，提供完整的 PNG 标准实现和灵活的 API 配置选项。

- 🖼️ 纯 JavaScript 实现的 PNG 解码与编码工具
- 📦 通过 npm 安装，支持 Node.js 和浏览器环境
- ⚙️ 提供 decode() 和 encode() 核心 API，支持 CRC 校验和文本元数据
- 📄 遵循 W3C PNG 标准规范，支持 8/16 位色深和 1-4 通道
- 🌟 获得 439 个星标和 24 个分支，被 2.8k 项目使用
- 🔧 基于 TypeScript 开发（99.7%），维护活跃
- 📝 采用 MIT 开源协议，由 Zakodium 团队维护

---

### [GitHub - image-js/image-js: JavaScript 图像处理与操作库](https://github.com/image-js/image-js)

**原文标题**: [GitHub - image-js/image-js: Image processing and manipulation in JavaScript](https://github.com/image-js/image-js)

image-js 是一个用于 JavaScript 图像处理和操作的库，提供完整的 API 文档和开发指南，采用 MIT 许可证，由 Zakodium 维护。

- 🖼️ 提供 JavaScript 图像处理和操作功能
- 📦 可通过 npm 安装，使用命令 npm install image-js
- 📚 完整的 API 文档和使用指南可在 api.image-js.org/ 查看
- 🔧 包含开发文档，支持 TypeScript 语言开发
- ⭐ 项目获得 796 个星标和 71 个复刻，被 2000 多个项目使用
- 📄 采用 MIT 许可证，由 19 位贡献者共同维护

---

### [首页 | 火箭管理](https://rocketadmin.com/?utm_source=nodeweekly)

**原文标题**: [Home | Rocketadmin](https://rocketadmin.com/?utm_source=nodeweekly)

一款可在 5 分钟内快速部署的数据库管理面板解决方案，支持 MySQL/PostgreSQL/MSSQL/Oracle/MongoDB 等多种数据库，无需编码即可生成可视化界面，帮助用户节省开发成本和时间。

- 💰 节省 90,547 美元开发成本，避免从零开发管理面板的高额投入
- ⏱️ 节省 10,000 小时开发时间，专注核心业务而非系统维护
- 🚀 提供无限小时级高性能体验，采用优化技术确保极速响应
- 🔒 通过 1,432 项安全测试，采用多重保护机制防止数据泄露
- 📞 每周 5 天专业技术支持，提供 GMT+2 时段 10:00-02:00 的实时协助
- ☕ 经过 658 杯咖啡打磨的直观 UI，提供可扩展的友好操作界面
- 📱 支持全设备响应式访问，从电脑到移动端均可无缝操作
- 🔧 支持 API 集成和自定义操作，无需代码即可配置 webhook 和组件
- 👥 提供灵活权限管理系统，可自定义用户组和分级访问权限
- 🌍 适合远程团队协作，仅需邮箱密码即可全球范围访问管理
- 🛡️ 内置 SQL 操作防护机制，所有变更留痕可供安全审计
- 🆓 提供免费起始方案，付费计划含 30 天试用期（5-10 美元/用户）

---

### [google-spreadsheet - Google 电子表格 API：用于读写数据和管理工作表的简洁接口](https://theoephraim.github.io/node-google-spreadsheet/)

**原文标题**: [google-spreadsheet - Google Spreadsheets API -- simple interface to read/write data and manage sheets](https://theoephraim.github.io/node-google-spreadsheet/)

文章概述了人工智能在教育领域的应用现状与未来趋势，重点关注个性化学习、教学效率提升及伦理挑战。

- 🤖 人工智能通过自适应学习系统为学生提供个性化学习路径
- 📊 教育数据分析帮助教师精准识别学生知识薄弱点并提供针对性辅导
- 🌐 智能教学平台打破地域限制，使优质教育资源实现更广泛覆盖
- ⚠️ 需关注数据隐私保护与算法偏见等伦理问题
- 🔮 未来将深化人机协作教学模式，推动教育生态变革

---

### [GitHub - theoephraim/node-google-spreadsheet: JavaScript/TypeScript 版 Google Sheets API 封装库](https://github.com/theoephraim/node-google-spreadsheet)

**原文标题**: [GitHub - theoephraim/node-google-spreadsheet: Google Sheets API wrapper for Javascript / Typescript](https://github.com/theoephraim/node-google-spreadsheet)

这是一个用于 JavaScript/TypeScript 的 Google Sheets API 封装库，提供多种认证方式和丰富的表格操作功能。

- 📊 支持多种认证方式（服务账户、OAuth、API 密钥等）
- 📝 提供单元格级和行级的读写操作 API
- 📑 支持工作表管理（添加、删除、调整大小、复制）
- 🌐 支持文档管理（创建、删除、共享权限设置）
- 📦 支持多种格式的文档导出功能
- ⭐ 项目获得 2.4k 星标和 395 个 fork
- 📄 采用 MIT 开源许可证
- 🔧 提供完整的文档网站和详细的使用示例
- 🚀 支持 TypeScript 类型定义
- 💻 需要 Node.js 环境运行

---

### [GitHub - yuniko-software/minecraft-mcp-server：基于Mineflayer API 的 Minecraft MCP 服务器。可实时控制游戏角色，使 AI 助手能通过自然语言指令建造结构、探索世界并与游戏环境交互。](https://github.com/yuniko-software/minecraft-mcp-server)

**原文标题**: [GitHub - yuniko-software/minecraft-mcp-server: A Minecraft MCP Server powered by Mineflayer API. It allows to control a Minecraft character in real-time, allowing AI assistants to build structures, explore the world, and interact with the game environment through natural language instruction](https://github.com/yuniko-software/minecraft-mcp-server)

这是一个基于 Mineflayer API 开发的 Minecraft MCP 服务器项目，通过自然语言指令让 AI 助手实时控制游戏角色进行建造、探索和交互。

- 🤖 使用 Model Context Protocol 协议，支持 Claude 等 AI 模型控制游戏角色
- ⚠️ 当前仅兼容 Minecraft 1.21.6 及以下版本
- 🎮 需要配合 Claude Desktop 使用，通过配置文件连接 Minecraft 游戏
- 🏃 支持移动、飞行、物品管理、方块操作等丰富游戏指令
- 🏗️ 可通过自然语言指令让 AI 建造结构、探索世界
- 🌟 开源项目，采用 Apache-2.0 许可证，已有 261 个 star
- 📝 代码基于 TypeScript 开发，欢迎贡献功能和改进

---

### [GitHub - PrismarineJS/mineflayer：使用强大、稳定且高级的JavaScript API 创建 Minecraft 机器人](https://github.com/PrismarineJS/mineflayer)

**原文标题**: [GitHub - PrismarineJS/mineflayer: Create Minecraft bots with a powerful, stable, and high level JavaScript API.](https://github.com/PrismarineJS/mineflayer)

Mineflayer 是一个用于创建 Minecraft 机器人的强大 JavaScript 库，提供稳定高级的 API 接口，支持多种 Minecraft 版本和丰富功能。  
- 🤖 支持 Minecraft 1.8 至 1.21 版本，提供实体追踪、方块查询、物理运动等功能  
- 📦 包含物品管理、合成系统、容器交互等完整游戏机制支持  
- 🌐 可通过 Python 调用，并提供浏览器实时视角查看功能  
- 🔌 高度模块化设计，支持第三方插件扩展（如路径规划、PVP 模块等）  
- 📚 提供详细文档、视频教程和大量代码示例便于快速上手  
- ⚙️ 支持微软账号认证和领域服务器连接，采用 MIT 开源协议

---

### [发布 v1.4.0 · yamadashy/repomix · GitHub](https://github.com/yamadashy/repomix/releases/tag/v1.4.0)

**原文标题**: [Release v1.4.0 · yamadashy/repomix · GitHub](https://github.com/yamadashy/repomix/releases/tag/v1.4.0)

Repomix v1.4.0 版本发布，新增 Git 提交历史集成和二进制文件检测功能，提升 AI 分析能力和用户体验。

- 🚀 新增--include-logs 选项，可包含 Git 提交历史记录（默认最近 50 次提交）
- 🔍 增强二进制文件内容检测功能，明确列出被排除的二进制文件
- 🔒 强化 Git 命令执行安全性（感谢@szepeviktor 贡献）
- 🌐 官网新增 URL 参数支持，支持预设配置分享和书签功能
- ⚙️ 配置文件中新增 git.includeLogs 和 includeLogsCount 选项
- 📦 通过 npm update -g repomix 命令即可更新
- 👥 特别感谢@szepeviktor 和@BBboy01 的贡献

---

### [Release 12.0.0 · vitaly-t/pg-promise · GitHub](https://github.com/vitaly-t/pg-promise/releases/tag/12.0.0)

**原文标题**: [Release 12.0.0 · vitaly-t/pg-promise · GitHub](https://github.com/vitaly-t/pg-promise/releases/tag/12.0.0)

pg-promise 12.0.0 版本发布，移除了对自定义 Promise 库的支持，全面转向 ES6 Promise。  
- 🔨 移除自定义 Promise 支持，不再兼容 Bluebird 等外部 Promise 库  
- 📦 删除 promiseLib 初始化选项，不再提供 Promise 定制功能  
- 🚀 全面采用 ES6 Promise，简化库架构  
- 🏷️ 版本号 12.0.0，由 vitaly-t 于 8 月 26 日发布  
- ⭐ GitHub 项目获 3.5k 星标，社区反响积极（2 人点赞、1 人欢呼）

---

### [GitHub - sindresorhus/yoctocolors：互联网上最小最快的命令行着色包](https://github.com/sindresorhus/yoctocolors)

**原文标题**: [GitHub - sindresorhus/yoctocolors: The smallest and fastest command-line coloring package on the internet](https://github.com/sindresorhus/yoctocolors)

yoctocolors 是互联网上最小且最快的命令行着色包，专为 Node.js 设计，提供丰富的颜色和样式修饰功能。  
- 🌈 支持嵌套颜色处理和树摇优化  
- ⚡ 性能卓越，基准测试显示其速度与同类顶级库持平  
- 📦 无依赖且采用 MIT 开源协议  
- 🎨 提供多种颜色、背景色及文本修饰符（如粗体、下划线）  
- 🌐 可检测环境自动禁用颜色，支持强制启用/禁用配置  
- 🔧 提供 ESM 和 CommonJS 双版本，活跃维护中

---

### [GitHub - chalk/chalk：🖍 终端字符串样式处理的正确方式](https://github.com/chalk/chalk)

**原文标题**: [GitHub - chalk/chalk: 🖍 Terminal string styling done right](https://github.com/chalk/chalk)

Chalk 是一个用于终端字符串样式化的 JavaScript 库，提供丰富的颜色和样式 API，支持嵌套样式和自动颜色检测，被广泛用于命令行工具开发。

- 🎨 支持 256 色和真彩色，提供链式 API 和样式嵌套功能
- ⚡ 无依赖、高性能，且自动检测终端颜色支持
- 📦 已被约 11.5 万个包使用，采用 MIT 开源协议
- 🖥️ 支持浏览器和 Windows Terminal，提供错误加载提示功能
- 🔧 包含多种颜色模型（RGB/HEX/ANSI256）和样式修饰器
- 🌐 提供独立的标准错误输出流颜色支持实例

---

### [发布 v10.0.0 · faker-js/faker · GitHub](https://github.com/faker-js/faker/releases/tag/v10.0.0)

**原文标题**: [Release v10.0.0 · faker-js/faker · GitHub](https://github.com/faker-js/faker/releases/tag/v10.0.0)

Faker.js 项目发布了 v10.0.0 主要版本更新，该版本包含重大变更和功能改进，需要用户参考迁移指南进行适配。

- 🚀 仅支持 ESM 模块格式（CommonJS 需通过迁移指南适配）
- 🔧 移除了 v9 版本的废弃功能
- ⚠️ 单词模块默认错误策略改为"fail"
- 🎨 扩展了波兰语颜色列表
- 💳 移除无效信用卡发行商模式
- 📦 依赖项全面升级（Node.js 24、TypeScript 5.9.2 等）
- 📘 提供详细的 v10 迁移指南
- 👥 由 8 位贡献者共同完成本次更新

---

### [Sidequest.js](https://sidequestjs.com/)

**原文标题**: [Sidequest.js](https://sidequestjs.com/)

Sidequest.js 是一个专为 Node.js 设计的持久化、分布式且云无关的任务队列系统，旨在提供高性能、易用性和跨平台兼容性。

- 🌍 云无关性：可在任何云平台或本地环境运行，避免供应商锁定，无需修改代码
- 🚀 分布式扩展：支持多节点横向扩展，能高效协调高吞吐量任务并确保持久性
- 🖥️ 可视化监控：提供直观的管理界面，实时监控任务状态和调试问题
- ⚙️ 开发友好：包含简洁的 API 和完整文档，可快速集成到现有 Node.js 应用
- 📦 生产就绪：专为实际工作负载设计，解决传统调度工具（如 node-cron）的局限性

---

### [发布 v11.2.0 · secretlint/secretlint · GitHub](https://github.com/secretlint/secretlint/releases/tag/v11.2.0)

**原文标题**: [Release v11.2.0 · secretlint/secretlint · GitHub](https://github.com/secretlint/secretlint/releases/tag/v11.2.0)

secretlint 项目发布了 v11.2.0 版本更新，包含功能增强、错误修复和依赖项更新  
- 🚀 新增对@secretlint/secretlint-rule-pattern 中模式数组的支持  
- 🐛 修复了 database-connection-string 规则中对 Makefile 变量模式$(VARIABLE) 的支持  
- 📦 更新了 chalk 依赖至^5.6.0 版本  
- ⚙️ 更新了 rollup 依赖至^4.46.3 版本  
- 👥 新增贡献者@Copilot 的首次参与  
- 🔖 版本由 github-actions 于 8 月 25 日发布，包含 4 次提交

---

### [发布 v5.15.0 · openai/openai-node · GitHub](https://github.com/openai/openai-node/releases/tag/v5.15.0)

**原文标题**: [Release v5.15.0 · openai/openai-node · GitHub](https://github.com/openai/openai-node/releases/tag/v5.15.0)

OpenAI Node.js 库发布了 5.15.0 版本更新，包含新功能添加和常规维护

- 🆕 新增 MCP 工具连接器支持（048bee3 提交）
- 💬 为 API 添加/v1/conversations 端点支持（1380d17 提交）
- 📦 在 package.json 中添加包配置（6748b2b 提交）
- 🏷️ 版本于 2025 年 8 月 21 日由 stainless-app 发布
- ⭐ GitHub 仓库获得 10k 星标和 1.2k 分叉

---

### [InversifyJS v7.9.0 版本发布 · inversify/InversifyJS · GitHub](https://github.com/inversify/InversifyJS/releases/tag/v7.9.0)

**原文标题**: [Release v7.9.0 · inversify/InversifyJS · GitHub](https://github.com/inversify/InversifyJS/releases/tag/v7.9.0)

InversifyJS 项目发布了 v7.9.0 版本，主要更新了装饰器功能以支持方法参数装饰。

- 🆕 版本 v7.9.0 于 8 月 20 日发布
- ⭐ GitHub 星标数达 11.9k
- 🔧 改进了 decorate 功能支持方法参数装饰
- 📦 包含 10 个提交至 master 分支
- 🔐 采用 GPG 签名验证发布安全性

---

### [GitHub - mscdex/ssh2：用纯 JavaScript 为 Node.js 编写的 SSH2 客户端和服务器模块](https://github.com/mscdex/ssh2)

**原文标题**: [GitHub - mscdex/ssh2: SSH2 client and server modules written in pure JavaScript for node.js](https://github.com/mscdex/ssh2)

这是一个用纯 JavaScript 为 Node.js 编写的 SSH2 客户端和服务器模块，支持多种认证方式和功能。

- 🔑 支持多种认证方式，包括密码、公钥、键盘交互和基于主机的认证
- 🌐 提供客户端和服务器实现，支持远程命令执行、交互式 Shell 和端口转发
- 📁 包含完整的 SFTP 客户端和服务器功能，支持文件操作和目录列表
- 🔄 支持连接跳转和 X11 转发等高级功能
- 📦 提供实用的工具函数，如密钥生成和解析
- ⚙️ 高度可配置，支持自定义算法和调试选项
- 📄 采用 MIT 许可证，拥有活跃的社区支持和丰富的文档示例

---

### [pnpm 10.15 | pnpm](https://pnpm.io/blog/releases/10.15)

**原文标题**: [pnpm 10.15 | pnpm](https://pnpm.io/blog/releases/10.15)

pnpm 10.15 版本带来配置管理优化、依赖处理改进和多项问题修复  
- 🔧 新增 cleanupUnusedCatalogs 配置可自动清理未使用的目录条目  
- ⚙️ 自动加载符合命名规范的 config dependencies 中的 pnpmfiles  
- 🎯 config 命令支持属性路径查询和 JSON 格式输入输出  
- 🔄 安装缺失对等依赖时优先选择根工作区现有版本  
- ✅ pnpm create 命令增加节点版本验证机制  
- 🌐 修复 AWS CodeArtifact 的 406 错误请求头问题  
- 🐛 修复独立执行版兼容性和 dlx 命令参数传递异常

---

### [nodejs/undici v7.15.0 版本发布 · GitHub](https://github.com/nodejs/undici/releases/tag/v7.15.0)

**原文标题**: [Release v7.15.0 · nodejs/undici · GitHub](https://github.com/nodejs/undici/releases/tag/v7.15.0)

Node.js 的 Undici 库发布了 7.15.0 版本，包含性能优化、错误修复和新功能添加。

- 🚀 从 fetch 提取 SRI 并升级至最新规范
- 🐛 修复了 Agent 中的内存泄漏问题
- 🔧 移除了未使用的 lib/api/util.js 文件
- 📦 重新启用了共享内置 CI 测试
- ✨ 新增解压缩拦截器功能
- 🔄 更新了 llhttp 依赖
- 🧹 清理了未使用的异常捕获块
- 📝 移除了 diagnostic-channels 的未知错误类型
- ⚡ 优化了缓存序列化逻辑避免错误抛出
- 🌟 新增了快照记录器模式类型定义
- 👥 迎来首位贡献者@hexchain

---

### [Node.js 异步上下文的隐藏成本](https://blog.platformatic.dev/the-hidden-cost-of-context)

**原文标题**: [The Hidden Cost of Async Context in Node.js ](https://blog.platformatic.dev/the-hidden-cost-of-context)

本文探讨了 Node.js 中 AsyncLocalStorage 与 OpenTelemetry 的性能开销，通过基准测试揭示不同配置下的性能差异，并给出可观测性方案的成本效益建议。

- 📊 Node.js v24.4.1 相比 v22.17.1 在 AsyncLocalStorage 场景有 5% 性能提升，得益于底层优化
- ⚡ 纯 AsyncLocalStorage 开销约为 7%，Fastify 框架基础性能接近原生 Node.js
- 😱 全量 OpenTelemetry 自动插桩导致性能下降超 80%，选择性插桩仍降低约 65%
- 📈 指标（Metrics）和性能分析（Profiling）能以最小开销提供大部分可观测需求
- 🎯 建议优先采用指标监控和性能分析，分布式追踪仅用于异常调查场景
- 💡 Node.js v24 对上下文密集型应用具有明显性能优势，建议升级
- ⚖️ 需根据实际业务需求权衡可观测性价值与性能成本，避免过度插桩

---

### [开始使用 Redis](https://redis.io/lp/get-started2/?utm_source=cooper-press&utm_medium=cpa&utm_campaign=2025-08-app_performance-node-weekly-1&utm_content=cloud_-_redis_cloud_users)

**原文标题**: [Get started with Redis](https://redis.io/lp/get-started2/?utm_source=cooper-press&utm_medium=cpa&utm_campaign=2025-08-app_performance-node-weekly-1&utm_content=cloud_-_redis_cloud_users)

Redis 是一个高速数据平台，提供云端和本地部署解决方案，帮助团队快速构建应用程序。

- 🚀 作为矢量数据库支持快速生成 AI 应用
- ⚡ 通过内存缓存技术加速应用开发
- 🗄️ 作为 NoSQL 键值存储支持实时数据处理
- 🌩️ 提供云端服务轻松创建和部署数据库
- 🔧 支持多语言开发并提供开发者资源中心
- 📈 可无缝从实验环境扩展到生产级 AI 应用
- 🆓 提供免费试用选项

---

### [大 O 表示法](https://samwho.dev/big-o/)

**原文标题**: [Big O](https://samwho.dev/big-o/)

大 O 符号用于描述函数输入规模与执行时间增长之间的关系，不关注具体耗时，而关注增长趋势。本文通过 JavaScript 示例介绍了四种常见时间复杂度类别及其应用场景。

- 📊 大 O 符号描述函数输入规模与执行时间的关系，而非具体耗时
- ⏱️ 线性时间复杂度 O(n)：示例中循环求和函数耗时随输入规模线性增长
- ⚡ 常数时间复杂度 O(1)：数学公式求和函数耗时与输入规模无关
- 🔄 二次时间复杂度 O(n²)：冒泡排序在最坏情况下需要 n²次操作
- 🔍 对数时间复杂度 O(log n)：二分搜索每次排除一半可能性
- 💡 优化建议：使用 Set 替代数组查找、避免循环内嵌套 O(n) 操作、缓存中间结果
- ⚠️ 注意事项：大 O 默认描述最坏情况，实际性能需具体测试验证

---

### [GitHub - privatenumber/minification-benchmarks: 🏃‍♂️🏃‍♀️🏃 JS 压缩性能基准测试：babel-minify、esbuild、terser、uglify-js、swc、Google Closure Compiler、tdewolff/minify、oxc-minify](https://github.com/privatenumber/minification-benchmarks)

**原文标题**: [GitHub - privatenumber/minification-benchmarks: 🏃‍♂️🏃‍♀️🏃 JS minification benchmarks: babel-minify, esbuild, terser, uglify-js, swc, google closure compiler, tdewolff/minify, oxc-minify](https://github.com/privatenumber/minification-benchmarks)

该项目对多个 JavaScript 压缩工具进行了全面的性能基准测试，旨在帮助开发者根据压缩率和速度选择最适合的工具。

- 🏆 **综合优胜者**：@swc/core 在压缩率和速度间取得了最佳平衡，特别在处理大型文件时表现突出
- ⚡ **速度冠军**：@tdewolff/minify 在几乎所有测试中都展现了最快的压缩速度
- 📦 **压缩效率**：uglify-js 在多个小型到中型包测试中获得了最佳压缩率
- 🚀 **新兴竞争者**：oxc-minify 表现均衡，在多个测试中都有不错的表现
- ❌ **淘汰工具**：babel-minify、tedivm/jshrink 和 bun 因压缩失败或验证错误被淘汰
- 📊 **测试方法**：采用严格的测试流程，包括完整性验证和超时控制，确保结果可靠性
- ⚖️ **评分标准**：综合考量压缩后大小 (85% 权重) 和压缩时间 (15% 权重)，采用自适应权重算法

---

### [Jumping-Beaver/cminify：用C语言编写的CSS、JavaScript、XML、HTML、JSON命令行压缩工具。提供小于50 kB 的二进制版本。- Codeberg.org](https://codeberg.org/Jumping-Beaver/cminify)

**原文标题**: [Jumping-Beaver/cminify: Command-line minifier written in C for CSS, JavaScript, XML, HTML, JSON. Binary releases with less than 50 kB size are available. - Codeberg.org](https://codeberg.org/Jumping-Beaver/cminify)

文章概述了人工智能在现代社会中的关键作用及其对多个行业的影响。

- 🤖 人工智能技术正在推动各行各业的数字化转型
- 📊 机器学习算法可高效处理海量数据并提取有价值信息
- 🏥 医疗领域借助 AI 实现疾病诊断和治疗方案优化
- 🏭 智能制造通过自动化系统提升生产效率和产品质量
- 🔒 数据安全和伦理规范成为 AI 发展中的重要考量因素
- 🌐 自然语言处理技术打破语言障碍促进全球交流
- 📱 智能助手和推荐系统改善用户体验和个性化服务

---

### [CSS random() 的随机探索 | WebKit](https://webkit.org/blog/17285/rolling-the-dice-with-css-random/)

**原文标题**: [  Rolling the Dice with CSS random() | WebKit](https://webkit.org/blog/17285/rolling-the-dice-with-css-random/)

CSS 的 random() 函数即将推出，它允许开发者在无需 JavaScript 的情况下生成随机数，用于动画延迟、布局位置、颜色生成等多种场景。该函数支持定义范围、步长参数，并可通过命名标识或 element-shared 实现随机值的共享。文章通过星空效果、网格布局、照片堆叠和幸运转盘等示例展示了其应用潜力，目前已在 Safari Technology Preview 中开放测试，并鼓励开发者反馈使用体验。

- 🌌 使用 random() 创建随机分布的星空效果，包括位置、大小和发光颜色
- 🎲 函数格式为 random(min, max, step)，支持各种数值类型和步长参数
- 🔗 通过命名标识（如 --foo）在单个元素内共享随机值
- 🌍 使用 element-shared 实现跨元素随机值共享
- 🖼️ 结合网格布局生成随机位置和颜色的矩形
- 📸 实现照片堆叠的随机旋转和交互效果
- 🎡 创建幸运转盘动画，随机决定旋转停止位置
- 🔍 目前仅在 Safari Technology Preview 可用，欢迎开发者测试反馈

---

### [AWS 2025：那些你以为正确实则错误的认知 - 《上周 AWS 动态》博客](https://www.lastweekinaws.com/blog/aws-in-2025-the-stuff-you-think-you-know-thats-now-wrong/)

**原文标题**: [AWS in 2025: The Stuff You Think You Know That's Now Wrong - Last Week in AWS Blog](https://www.lastweekinaws.com/blog/aws-in-2025-the-stuff-you-think-you-know-thats-now-wrong/)

AWS 作为已有近 20 年历史的云平台，其基础服务持续演进，许多旧有操作方式和功能特性已发生显著变化。本文梳理了关键服务的现代化改进，帮助用户避免使用过时方案。

- 🖥️ EC2 实例支持运行时修改安全组、IAM 角色、EBS 卷调整，并可强制终止实例
- 🔄 实例支持实时迁移物理主机，可靠性大幅提升，Spot 实例定价机制更稳定
- 🛡️ 新账户默认启用 AMI 和 S3 存储桶的公有访问阻断功能，S3 实现读写强一致性
- ❄️ Glacier 存储类恢复费用降低且速度提升，不再需要键名随机化避免热点
- 🌐 VPC 对等连接优化，新增 Transit Gateway 和 VPC Lattice 等高级网络方案
- ⚡ CloudFront 部署时间从 45 分钟缩短至 5 分钟，负载均衡器跨 AZ 流量计费规则调整
- 🐑 Lambda 支持 15 分钟超时、容器镜像、10GB 内存/tmp 存储，冷启动和 VPC 调用性能优化
- 💾 EFS 支持独立调整 IO 性能，EBS 空卷全性能可用但需预读快照数据
- 🗃️ DynamoDB 允许空字段，性能监控更透明，按需计费成为主流选择
- 💰 节省计划逐步替代预留实例，EC2 按秒计费，成本异常检测器可免费使用
- 🔐 IAM 角色替代用户权限管理，根账户支持多 MFA 设备，成员账户无需配置根凭证
- 📊 CloudWatch 数据一致性提升，账户可通过组织根账户统一关闭
- ⚠️ 服务弃用频率增加，但核心服务稳定，us-east-1 区域可靠性显著改善

（注：最后部分关于 Malphas 的虚构新闻及通讯订阅内容未纳入摘要范围）

---

### [图解 OAuth - 作者：Aditya Bhargava](https://www.ducktyped.org/p/an-illustrated-guide-to-oauth)

**原文标题**: [An Illustrated Guide to OAuth - by Aditya Bhargava](https://www.ducktyped.org/p/an-illustrated-guide-to-oauth)

OAuth 是一种授权协议，允许第三方应用在用户授权后安全访问其数据，而无需共享密码。它通过访问令牌和授权代码流程确保安全性，并强调用户对数据访问的主动控制。

- 🚫 OAuth 解决了第三方应用直接索要用户密码的安全隐患，避免密码泄露风险
- 🔑 核心机制是使用访问令牌（类似用户专属 API 密钥）替代密码进行授权
- 🌐 典型流程：用户被重定向至授权服务器登录 → 选择授权范围 → 返回授权代码 → 应用通过后端交换获取访问令牌
- 🛡️ 安全设计：授权代码通过前端传递，访问令牌仅通过后端 HTTPS 请求交换防止泄露
- 📋 关键术语：资源所有者（用户）、OAuth 客户端（应用）、授权服务器、资源服务器、范围（权限）
- 📱 支持多种场景：Web 应用使用客户端密钥，无后端应用可采用 PKCE 方案
- ⚠️ 注意事项：存在多种流程变体（如隐式流程），令牌需要刷新机制，登录场景通常使用 OIDC 扩展
- 🔄 复杂性原因：兼顾用户参与体验与安全性，历经多次安全修补

---

