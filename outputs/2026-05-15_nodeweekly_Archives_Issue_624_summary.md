### [Node Weekly 第624期：2026年5月14日](https://nodeweekly.com/issues/624)

**原文标题**: [Node Weekly Issue 624: May 14, 2026](https://nodeweekly.com/issues/624)

Node Weekly 第624期涵盖了Node.js生态系统的多项重要更新和工具发布。

- 📗 **NodeBook：Node.js内部机制高级指南** — 第一卷已完成，涵盖事件循环、V8操作、缓冲区分配、流、模块解析、async/await和进程生命周期等高级主题，作者正着手第二卷网络I/O和API内容。

- 💡 **AppSignal MCP服务器** — 可将错误、堆栈跟踪和部署上下文输入AI编辑器，由AI起草修复方案，提供30天免费试用。

- 🆕 **Node.js 26新特性** — 实用指南介绍v26中易被忽视的功能，该版本将于10月成为LTS版本，年底即可在生产环境使用。

- 📰 **简讯** — Node v22.22.3 LTS更新大量依赖和V8修复；Jest 30.4.0改进ESM、Temporal和React 19支持；Socket发布vm2安全补丁；Vercel Sandbox支持Node.js 26.x。

- 🔧 **Sentry改进JavaScript可观测性** — 采用基于诊断通道的方法替代猴子补丁，推动流行包加入这一新方案。

- 🔄 **递归的真相** — ES2015指定尾调用优化但V8未实现，文章展示“蹦床”模式以保持递归风格而不导致栈溢出。

- 📄 **Node.js中使用HTTP/3 over QUIC** — node:quic仍为实验性功能，但为构建HTTP/3客户端或服务器提供了实用入门指南。

- 🛠 **Bun v1.3.14** — 新增图像处理API（可替代Sharp）、HTTP/3支持、HTTP/2 Fetch、全局虚拟存储，以及多项Node.js兼容性改进。

- 📱 **使用Node.js和Google Cloud Run发送SMS** — 部署容器化Node.js应用，通过Vonage Messages API发送短信和处理入站Webhook。

- 🔗 **Syncpack 15.0** — 用于JS monorepo的CLI工具，可查找和修复版本不匹配，新增对pnpm和Bun目录的支持。

- 🎭 **Counterfact：OpenAPI驱动的API模拟器** — 指向OpenAPI规范即可获得实时、有状态的Node服务器，支持类型化处理程序、热重载和REPL。

- 📦 **pnpm 11.1** — 新增pnpm bugs和pnpm audit signatures命令，支持gh:前缀从GitHub Packages注册表安装包。

- 🌐 **wf：Web平台特性CLI工具** — 用于查询Web平台特性支持、错误和文档的命令行工具，可配合npx使用。

- 📰 **分类广告** — Clerk API Keys正式可用；AI代理中间件支持Claude Code、Codex和Gemini；zero-native是Vercel的桌面应用框架；Wakaru用于解构混淆JS代码；开发者分享从Electron转向Tauri的经验。

---

### [Node.js 内部机制、运行时与网络指南 | NodeBook](https://www.thenodebook.com/)

**原文标题**: [Node.js Internals, Runtime & Networking Guide | NodeBook](https://www.thenodebook.com/)

NodeBook 是一本深入讲解 Node.js 运行时内部机制的免费在线书籍，目前第一卷已完成，并提供付费数字版合集。本书面向有经验的开发者，旨在帮助他们理解 Node.js 在底层如何处理 I/O、内存、流等核心机制，从而提升生产环境中的问题排查与性能优化能力。

- 📚 **完整的第一卷**：涵盖运行时基础，包括架构、缓冲区、流、文件系统、进程、模块、异步模式等 8 个章节，共 39 个子章节。
- 🔧 **深入运行时机制**：聚焦 Libuv 事件循环、V8 编译管道、零拷贝流架构、原生插件开发、生产可观测性与内存管理等关键主题。
- 💡 **实战示例对比**：通过 `memory_crash.js` 与 `stream_flow.js` 展示背压机制如何避免内存溢出，强调运行时行为而非语法。
- 🎯 **目标读者明确**：适合已熟悉 JavaScript 的开发者，帮助弥补运行时可见性不足、内存泄漏发现滞后等常见短板。
- 📖 **免费在线阅读**：全书无付费墙、无广告，提供深色/浅色阅读模式、全局搜索与读者讨论功能。
- 💰 **付费数字版**：$19.99 起，包含第一卷 EPUB、PDF（浅色/深色）、幻灯片与速查表，支持离线阅读与更新。
- 🚧 **后续规划**：第二卷（网络 API）正在开发中，后续还有任务执行、安全、生产工程、架构扩展等卷。
- 📬 **订阅更新**：可订阅邮件，在新章节发布时获得通知，无需担心垃圾邮件，随时可退订。
- 👤 **作者背景**：Ishtmeet Singh，自 2014 年起使用 Node.js，拥有 10 年以上经验，读者超过 7 万人，致力于知识开放共享。

---

### [Node.js 事件循环：阶段、微任务与 libuv](https://www.thenodebook.com/node-arch/event-loop-intro#what-the-nodejs-event-loop-does)

**原文标题**: [Node.js Event Loop: Phases, Microtasks & libuv](https://www.thenodebook.com/node-arch/event-loop-intro#what-the-nodejs-event-loop-does)

Node.js 事件循环由 libuv 的循环阶段和 Node 的 JavaScript 端优先级队列共同驱动。定时器、I/O 回调、check 回调、close 回调、Promise 反应以及 `process.nextTick()` 回调都有不同的队列和清空点。核心规则是：JavaScript 运行在单个调用栈上，当栈被占用时，没有排队回调能运行。栈清空后，Node 会在定义的点清空高优先级队列，然后让 libuv 进入其阶段。

- 🧠 **单调用栈**：JavaScript 执行的基础是 LIFO 调用栈，一次只做一件事。阻塞就是某个函数长时间占据栈顶，导致其他所有操作被冻结。
- ⏱️ **事件循环阶段**：libuv 的循环包括六个阶段：定时器、待处理回调、空闲/准备、轮询、检查、关闭回调。每个阶段按 FIFO 顺序处理其宏任务队列。
- 🔄 **微任务与宏任务**：微任务（`process.nextTick` 和 Promise 任务）优先级高于宏任务。每个宏任务执行后，会立即清空所有微任务队列，再进入下一阶段。
- ⚡ **nextTick 的陷阱**：`process.nextTick` 是最高优先级的微任务，但递归调用会饿死事件循环，阻止定时器和 I/O 运行。
- 📂 **I/O 与线程池**：文件系统和部分加密操作通过 libuv 线程池（默认4个线程）异步执行。线程池是共享资源，可能成为瓶颈。
- 🛠️ **性能优化**：避免同步阻塞（如 `JSON.parse`、复杂正则），使用 `setImmediate` 分块处理 CPU 密集型任务，或用 `worker_threads` 实现真正并行。
- 🔍 **调试工具**：使用 `setInterval` 延迟检查、`perf_hooks.monitorEventLoopDelay` 或 `async_hooks` 监控事件循环延迟。
- 🧩 **setTimeout vs setImmediate**：在主模块中顺序不确定（取决于启动时间），但在 I/O 回调中 `setImmediate` 总是先执行（因为它在检查阶段运行）。
- 🗑️ **垃圾回收影响**：V8 的“停止世界”GC 会冻结事件循环，良好内存管理（如使用流）可减少停顿。

---

### [Node.js中的V8：JIT、隐藏类与去优化](https://www.thenodebook.com/node-arch/v8-engine-intro)

**原文标题**: [V8 in Node.js: JIT, Hidden Classes & Deoptimization](https://www.thenodebook.com/node-arch/v8-engine-intro)

### 概述总结
V8是Node.js内置的JavaScript引擎，通过多层级JIT编译管道（Ignition→Sparkplug→Maglev→TurboFan）将代码优化为机器码。其性能核心在于隐藏类（Hidden Classes）和内联缓存（Inline Caches），稳定的对象形状和类型一致性可大幅提升执行效率。任何违反编译器假设的操作（如动态添加属性、混合类型、使用delete）都会触发去优化（Deoptimization），导致性能断崖式下降。

- 🔍 **V8编译管道**：从解析源码生成字节码（Ignition），经基线编译（Sparkplug）到中阶优化（Maglev）和高级优化（TurboFan），热代码逐步升级，冷代码保持轻量。
- 🧩 **隐藏类与对象形状**：V8为每个对象创建隐藏类记录属性布局，属性添加顺序决定隐藏类路径，一致形状使属性访问转为固定内存偏移，速度极快。
- ⚡ **内联缓存（IC）**：在属性访问点缓存隐藏类信息，单态（Monomorphic）最快，多态（Polymorphic）较慢，超多态（Megamorphic）回退为慢速查找。
- 🚨 **去优化触发器**：隐藏类不匹配、数组元素类型变化、使用`delete`、`arguments`对象、混合`BigInt`与`Number`等都会导致优化代码被丢弃。
- 📉 **性能悬崖案例**：一个条件属性添加（`config.optionalFeature = true`）导致对象形状分裂，P99延迟从2ms飙升到200ms，修复后恢复。
- 🛠️ **优化策略**：构造函数中初始化所有属性、保持函数单态、用`undefined`替代`delete`、使用`...args`替代`arguments`、避免混合数组元素类型。
- 🔬 **诊断工具**：使用`--trace-deopt`追踪去优化原因，`--prof`进行CPU分析，`--allow-natives-syntax`配合`%HaveSameMap`验证形状一致性。
- 🧠 **内存布局**：小整数（Smi）直接编码在指针中，堆对象通过指针压缩节省内存，字符串内联化（Interning）加速比较。
- 📋 **V8友好代码模式**：使用类或工厂函数确保形状稳定，热路径函数只处理单一类型，优先使用整数运算（Smi），避免动态特性。
- ⏳ **历史演进**：从Full-Codegen+Crankshaft到Ignition+TurboFan，再到引入Sparkplug和Maglev，现代管道更平滑、内存更低、去优化影响更小。

---

### [Node.js 缓冲区分配：内存池与内存安全](https://www.thenodebook.com/buffers/allocation-patterns)

**原文标题**: [Node.js Buffer Allocation: Pools & Memory Safety](https://www.thenodebook.com/buffers/allocation-patterns)

以下是您提供的文章摘要，以中文呈现，包含概述和要点列表。

---

Node.js 的 Buffer 分配机制涉及安全与性能的权衡。`Buffer.alloc()` 是安全的默认选择，但会因零填充而消耗 CPU；`Buffer.allocUnsafe()` 速度更快，但会返回未初始化的内存，可能泄露敏感数据；`Buffer.from()` 行为复杂，可能创建共享内存视图而非副本。文章通过实际案例和性能基准测试，详细解释了这些函数的风险、工作原理及最佳实践，并提供了生产环境中的决策框架。

- 🛡️ **默认使用 `Buffer.alloc()`**：这是最安全的选择，保证内存被零填充，防止数据泄露。除非有性能分析证明它是瓶颈，否则不要轻易更换。
- ⚠️ **谨慎使用 `Buffer.allocUnsafe()`**：它跳过零填充，速度更快，但返回的内存可能包含其他进程的敏感数据（如 JWT、密码）。**必须**在分配后立即、无条件地覆盖所有字节，否则就是安全漏洞。
- 🔍 **理解 `Buffer.from()` 的陷阱**：它看似方便，但行为多变。从字符串创建会进行编码；从数组创建会逐个复制；从 `ArrayBuffer` 创建可能只是创建一个**共享内存视图**，原始数据变化会导致缓冲区内容静默损坏。
- 💾 **认识 Buffer 池化机制**：Node.js 内部有一个 8KB 的 Buffer 池，用于小 Buffer 的快速分配。这提高了性能，但也意味着 `allocUnsafe()` 返回的内存很可能来自本进程之前释放的、包含敏感数据的 Buffer。
- 📊 **性能基准测试**：对于 100 字节的小 Buffer，`allocUnsafe` 比 `alloc` 快约 2.5 倍；对于 1MB 的大 Buffer，快约 1.2 倍。性能差异真实存在，但必须通过性能分析来验证。
- 🚫 **立即废弃 `new Buffer()`**：这是旧版、不安全的构造函数，行为不可预测。必须全部替换为 `Buffer.alloc()` 或 `Buffer.from()`。
- 🛠️ **使用 linter 强制执行**：通过 `eslint-plugin-node` 等工具自动禁止 `new Buffer()` 的使用，并对 `Buffer.allocUnsafe` 的使用进行标记和审查。
- 🧠 **遵循生产决策框架**：先默认用 `alloc()`，只有性能分析证明它是瓶颈后，才考虑使用 `allocUnsafe()`，且必须保证能立即完全覆盖。对于 `ArrayBuffer`，始终显式复制一份。
- 📝 **为危险代码添加注释**：如果必须使用 `allocUnsafe()`，务必留下详细注释，说明性能分析结果和为什么当前使用是安全的，方便后续维护者理解。
- 🏗️ **选择合适的工具**：如果 Node.js 的 Buffer 操作成为性能瓶颈（如视频处理、大量数据计算），应考虑使用 Rust、Go 等更适合 CPU 密集型任务的语言，而非在 Node.js 中强行优化。

---

### [Node.js 流：背压与数据流](https://www.thenodebook.com/streams/foundation-of-streams)

**原文标题**: [Node.js Streams: Backpressure & Data Flow](https://www.thenodebook.com/streams/foundation-of-streams)

### 概述总结
Node.js 流是处理大数据的核心机制，通过分块传输、背压控制和混合推拉模型，实现高效、内存安全的数据处理。

- 📦 **核心问题**：流解决内存无法容纳大数据的问题，避免一次性加载整个文件（如2GB视频）导致内存溢出。
- 🔄 **分块处理优势**：将数据分成小块（如64KB）处理，内存使用从2000MB降至64MB，且允许读、处理、写操作并发进行。
- ⚡ **推模型（Push）**：基于EventEmitter，生产者主动推送数据，适合事件驱动架构，但需额外实现背压防止消费者被淹没。
- 🔌 **拉模型（Pull）**：基于迭代器/生成器，消费者主动请求数据，背压隐式存在，适合惰性求值和异步处理（如`for await...of`）。
- 🧩 **混合架构**：Node.js流结合推（事件驱动）和拉（异步迭代）模型，通过`drain`事件和暂停机制实现背压控制。
- 📊 **四种流类型**：Readable（数据源）、Writable（数据汇）、Transform（转换）、Duplex（双向），支持构建管道式处理。
- 🔙 **背压机制**：数据正向流动，控制信号反向传播，确保整个管道以最慢环节的速度运行，内存使用有界。
- 🛠️ **适用场景**：处理大文件、网络通信、数据转换管道、实时数据处理和代理/多路复用，小数据则无需流。
- 📜 **历史演进**：从Node 0.10的Streams2引入背压，到v10+的`pipeline()`和异步迭代支持，流API日趋成熟。

---

### [Node.js 模块解析：node_modules 与 exports](https://www.thenodebook.com/modules/resolution-algorithm)

**原文标题**: [Node.js Module Resolution: node_modules & exports](https://www.thenodebook.com/modules/resolution-algorithm)

Node.js 模块解析系统将一个导入或 require 的字符串转化为具体的模块记录，涵盖内置模块、相对路径、绝对路径、包名、node_modules 目录遍历以及包元数据。CommonJS 和 ESM 共享部分概念，但各自拥有独立的解析规则。解析过程是元数据密集型的，package.json 可以重定向入口点、隐藏文件、定义条件分支和更改模块格式。

- 📂 **三种说明符类别**：解析算法根据字符串首字符将说明符分为内置模块、相对/绝对路径和裸说明符三类，每类走不同的代码路径。内置模块（如 'fs'）立即从内部注册表中返回，不涉及文件系统。
- 🔍 **扩展探测与目录模块**：对于相对/绝对路径，Node 会按顺序尝试 `.js`、`.json`、`.node` 扩展名，若路径指向目录则检查 `package.json` 的 `"main"` 字段，否则回退到 `index.js`。明确包含扩展名可节省 stat 调用。
- ⛰️ **node_modules 爬升算法**：裸说明符触发从调用者目录向上逐级检查 `node_modules` 的复杂算法，直至文件系统根目录。这支持嵌套依赖隔离，但可能导致大量同步 stat 调用，影响启动性能。
- 📦 **package.json 字段**：`"main"` 字段是 CJS 时代的入口点；`"exports"` 字段是现代方式，优先于 `"main"`，可限制包内文件的访问并提供条件导出（如区分 `require` 和 `import`）。`"imports"` 字段定义包内私有别名，以 `#` 为前缀，作用域仅限于定义它的包。
- 🔗 **符号链接与缓存**：解析最终路径时调用 `fs.realpathSync()` 规范化符号链接，确保同一真实路径的模块只缓存一次。`-preserve-symlinks` 标志可禁用此步骤，但可能导致模块重复实例化。`_findPath` 内部有字符串键缓存，避免重复文件系统探测。
- 🛠️ **调试工具**：`require.resolve()` 返回模块的绝对路径而不加载；`Module._nodeModulePaths()` 显示搜索目录列表；`NODE_DEBUG=module` 环境变量可输出详细的模块加载日志；也可通过猴子补丁 `Module._findPath` 来跟踪每次探测。
- ⚠️ **常见边界情况**：自引用（需 `"exports"` 字段）、大小写敏感（macOS/Windows 不敏感，Linux 敏感）、`"type"` 字段不影响 `require()` 解析、`NODE_PATH` 环境变量（已过时）、以及 `require.cache` 操作（用于热重载但脆弱）。

---

### [Node.js中的Async/Await：挂起与微任务](https://www.thenodebook.com/async-patterns/async-await)

**原文标题**: [Async/Await in Node.js: Suspension & Microtasks](https://www.thenodebook.com/async-patterns/async-await)

### 概述总结
本文详细解释了Node.js中async/await的工作原理、执行顺序、错误处理模式及性能考量，涵盖V8引擎的状态机实现、微任务调度规则和实际生产建议。

- 🔄 **async函数始终返回Promise**：即使返回普通值或抛出错误，V8都会将其包装为Promise，调用者始终获得一个Promise对象
- ⏸️ **await会暂停当前async函数**：执行到await时，V8保存函数状态并注册微任务，当前同步代码继续执行，恢复时从微任务队列调度
- 📋 **执行顺序规则**：await后的代码作为微任务执行，`process.nextTick()`优先级高于Promise微任务，多个async函数按FIFO顺序恢复
- 🎯 **V8状态机实现**：每个await都是挂起点，V8使用`JSAsyncFunctionObject`保存执行上下文，Promise结算后通过`PromiseReactionJob`恢复执行
- ⚠️ **错误处理要点**：使用try/catch捕获await的拒绝，`return await`在try/catch中保留错误捕获能力，浮动的Promise应添加.catch()
- 💡 **并发模式选择**：顺序依赖用连续await，独立操作用`Promise.all()`，大数量操作需分批控制并发度
- 🚀 **性能模型**：每个await产生微任务开销，但网络I/O主导的应用中差异可忽略；需注意挂起函数会保留作用域引用，大对象应在长等待前释放
- 🔧 **生产建议**：默认使用async/await，避免在`forEach/map/sort`中使用async回调，用`for...of`处理有序异步循环，性能优化前先分析瓶颈

---

### [Node.js 进程生命周期：启动、信号与退出](https://www.thenodebook.com/node-arch/node-process-lifecycle)

**原文标题**: [Node.js Process Lifecycle: Bootstrap, Signals & Exit](https://www.thenodebook.com/node-arch/node-process-lifecycle)

### 概述总结
Node.js进程生命周期从启动前开始，涉及V8初始化、libuv事件循环设置、原生模块注册、模块加载等阶段，直到进程因引用句柄、定时器、子进程等保持存活。理解启动顺序、信号处理、优雅关闭、资源清理和退出码对生产环境至关重要。

- 🔄 **启动序列**：Node进程启动包括解析CLI参数、初始化V8隔离区、创建libuv事件循环、加载原生模块、执行内部引导脚本，最后才运行用户代码，整个过程可能耗时数百毫秒。
- ⚡ **V8与原生模块初始化**：V8分配大块堆内存，原生模块（如`fs`、`crypto`）采用懒加载，首次`require()`会触发C++初始化，可能导致首次请求延迟。
- 📦 **模块加载性能**：`require()`是同步操作，涉及文件系统查找和`node_modules`遍历，大量依赖会导致启动缓慢；`require.cache`可能引发内存泄漏。
- 🌐 **ES模块生命周期**：ESM采用三阶段加载（解析、实例化、求值），支持顶层`await`和静态分析，但缺少`__dirname`等变量，需使用`import.meta.url`替代。
- 🛠️ **启动模式**：推荐使用异步初始化器封装启动逻辑，实现显式依赖注入、重试机制和状态管理，避免同步阻塞和CrashLoopBackOff。
- 📡 **信号处理**：关键信号包括`SIGTERM`（优雅关闭）、`SIGINT`（Ctrl+C）、`SIGKILL`（强制终止），需使用状态标志防止重复处理，并设置超时兜底。
- 🧹 **优雅关闭**：应遵循“停止接收新请求→等待处理中请求→清理资源→退出”的顺序，使用`server.close()`和数据库连接池关闭，避免直接调用`process.exit()`。
- 🔗 **句柄管理**：libuv句柄（服务器、套接字、定时器）默认保持进程存活，需使用`.unref()`释放后台任务，并通过`process._getActiveHandles()`调试泄漏。
- 💾 **内存生命周期**：启动时内存因V8堆初始化和模块缓存快速上升，运行时呈锯齿状模式；`Buffer`对象占用外部内存，需注意RSS而非仅V8堆。
- 🔢 **退出码**：`0`表示成功，非零表示失败；使用`process.exitCode`设置退出码而非直接调用`process.exit()`，容器编排工具依赖退出码判断状态。
- 👨‍👩‍👧 **子进程管理**：父进程必须负责清理子进程，在`SIGTERM`处理中向所有子进程发送信号并等待其退出，避免产生孤儿进程。
- 🔍 **调试工具**：使用`--cpu-prof`分析启动性能，`--trace-sync-io`检测同步I/O，堆快照排查内存泄漏，`lsof`查看文件描述符，`process._getActiveHandles()`定位句柄泄漏。

---

### [AppSignal — 错误追踪与性能监控 | AppSignal](https://www.appsignal.com/?variant=treatment&utm_source=newsletter&utm_medium=paid&utm_campaign=nodeweekly&utm_term=5-14&utm_content=primary)

**原文标题**: [AppSignal — Error Tracking & Performance Monitoring | AppSignal](https://www.appsignal.com/?variant=treatment&utm_source=newsletter&utm_medium=paid&utm_campaign=nodeweekly&utm_term=5-14&utm_content=primary)

AppSignal 是一款集错误追踪、性能监控和日志管理于一体的全栈监控工具，帮助开发者快速定位并修复应用问题。

- 🔍 **错误追踪**：自动捕获每个异常及其堆栈跟踪，按模式分组，让开发者能迅速发现并解决错误。
- ⚡ **性能监控**：从首次部署起即监控响应时间、吞吐量和慢查询，帮助找到拖慢应用的瓶颈。
- 🔗 **分布式追踪**：支持端到端请求追踪，清晰显示各服务间的调用链和瓶颈所在。
- 📊 **自定义指标与仪表盘**：可发送任何应用指标，仪表盘自动生成并支持自定义，满足个性化监控需求。
- 📝 **日志搜索与过滤**：提供全文搜索、属性过滤和保存查询功能，无需SSH即可高效检索日志。
- 🕒 **实时日志流**：支持所有服务的日志实时流式显示，无需刷新或轮询，即时掌握运行状态。
- 🔄 **追踪链接日志**：点击错误即可查看相关的日志行，时间戳自动对齐，简化排查过程。
- 🚨 **基于日志的告警**：可针对任何日志模式设置告警，如错误字符串或警告峰值，提前发现问题。
- 🤖 **AI 集成**：通过 MCP 服务器连接 Claude、Cursor 或 Zed，让 AI 助手直接获取错误、追踪和部署信息，辅助编写修复代码。
- 🚀 **部署追踪**：标记每次部署并与错误关联，快速定位导致生产环境问题的部署。
- 🌍 **多语言支持**：支持 Ruby、Python、Elixir、Node.js、PHP、Go、Java、Rust 等主流语言，基于 OpenTelemetry 构建。
- 💰 **透明定价**：计划从 $0 起，提供 30 天全功能试用，无隐藏费用，支持突发流量而不额外收费。
- 🛠️ **集成丰富**：与 Slack、GitHub、Jira、Linear、GitLab、PagerDuty 等工具无缝集成，也可自带工具。
- 🏆 **用户好评**：被开发者称赞为比 Datadog、Sentry 等更简单、快速且性价比高的监控工具，G2 评分 4.8。

---

### [Node.js 26 的新特性](https://nodejsdesignpatterns.com/blog/whats-new-in-nodejs-26/)

**原文标题**: [What's new in Node.js 26](https://nodejsdesignpatterns.com/blog/whats-new-in-nodejs-26/)

Node.js 26 于2026年5月5日发布，带来了多项实用更新，包括Temporal API稳定可用、Map和Iterator新方法、V8和Undici升级，以及一些旧API的清理。

- 🕐 **Temporal API稳定可用**：不可变、时区感知的日期时间API，默认启用，替代易出错的`Date`对象，支持时区转换、DST处理、日期比较等。
- 🗺️ **Map.getOrInsert和getOrInsertComputed**：简化缓存和分组模式，避免重复查找和样板代码，支持`WeakMap`。
- 🔗 **Iterator.concat()**：惰性组合多个迭代器，无需构建中间数组，支持链式调用`.map`、`.filter`、`.take`等。
- 🔐 **Crypto原始Ed25519密钥支持**：简化原始密钥导入，无需手动包装PKCS#8格式，`sign()`和`verify()`新增`context`选项。
- ⚡ **V8 14.6和Undici 8**：带来JIT/GC性能提升和`fetch()`改进，`NODE_MODULE_VERSION`更新至147。
- 🧹 **清理旧API**：移除`_stream_*`私有模块、`writeHeader()`、`--experimental-transform-types`，`module.register()`运行时弃用，`localStorage`无持久化文件时返回`undefined`。
- 📅 **发布周期**：当前为Current版本，将于2026年10月进入LTS，v25已停止支持。

---

### [Node.js — Node.js 22.22.3（长期支持版）](https://nodejs.org/en/blog/release/v22.22.3)

**原文标题**: [Node.js — Node.js 22.22.3 (LTS)](https://nodejs.org/en/blog/release/v22.22.3)

Node.js 22.22.3 (LTS) 版本发布，主要包含安全修复、依赖更新和文档改进。

- 🔒 **安全修复**：修复了crypto模块中BIO_meth_new()失败时的空指针解引用问题，以及zlib中reset()调用时的释放后使用漏洞
- 📦 **依赖更新**：升级了OpenSSL到3.5.6、npm到10.9.8、SQLite到3.52.0、V8等多个核心依赖
- 🛠️ **模块改进**：修复了ESM模块解析、require缓存和同步钩子等问题
- 📝 **文档完善**：修正了多处文档错误，包括process.md、net.md和TypeScript相关说明
- 🐛 **Bug修复**：修复了HTTP keep-alive连接复用竞争、HTTP2文件句柄泄漏、URL路径解析崩溃等问题
- 🔧 **工具优化**：改进了CI自动化、发布提案检查和标签管理工具
- 💻 **多平台支持**：提供Windows、macOS、Linux、AIX等平台的安装包和二进制文件

---

### [发布 v30.4.0 · jestjs/jest · GitHub](https://github.com/jestjs/jest/releases/tag/v30.4.0)

**原文标题**: [Release v30.4.0 · jestjs/jest · GitHub](https://github.com/jestjs/jest/releases/tag/v30.4.0)

Jest v30.4.0 发布，这是一个重大版本更新，主要重写了自定义运行时以支持 ESM 稳定化，并新增了对 Temporal API 和 React 19 的支持。

- 🎉 主要特性：重写自定义运行时，为 ESM 原生支持做准备，并在 Node 24.9+ 上支持 `require(esm)` 模块。
- ⏰ 假定时钟：新增对 Node v26 中 Temporal API 的支持，包括 `Temporal.Duration`、`Temporal.Instant` 等。
- ⚛️ React 19 支持：`pretty-format` 现在能正确处理 React 19 组件的快照。
- 🚩 新功能：添加 `--collect-tests` 标志，用于发现和列出测试而不执行；支持 `jest.config.mts` 配置文件。
- 🔧 配置改进：`verbose` 和 `silent` 选项现在可以按项目设置；新增 `workerGracefulExitTimeout` 配置。
- 🐛 修复：修复了 `toStrictEqual` 在 `structuredClone` 上的跨 realm 问题；改进了 CJS 与 ESM 的互操作性。
- 🛠️ 维护：升级了 `@sinonjs/fake-timers`；在 Node v24.9+ 上使用同步 ESM 链接。
- 👥 新贡献者：包括 alexander-turner、jmuransky、afiiif 等 13 位新贡献者。

---

### [Socket 发布针对关键 vm2 沙箱的免费认证补丁](https://socket.dev/blog/free-certified-patches-for-critical-vm2-sandbox-escape)

**原文标题**: [Socket Releases Free Certified Patches for Critical vm2 Sand...](https://socket.dev/blog/free-certified-patches-for-critical-vm2-sandbox-escape)

概述：node-ipc npm包遭供应链攻击，恶意版本含混淆窃密/后门行为，由Socket研究团队于2026年5月14日披露。

- 🔍 Socket研究团队检测到node-ipc npm包的恶意版本，存在混淆的窃密/后门行为。
- 🚨 这是一起正在发展的npm供应链攻击事件，影响广泛。
- 🛡️ 攻击者通过篡改合法包（node-ipc）植入恶意代码，危害依赖该包的项目。
- ⚠️ 建议开发者立即检查并更新node-ipc版本，避免使用受影响版本。

---

### [Node.js 26.x 现已在 Vercel Sandboxes 上可用 - Vercel](https://vercel.com/changelog/node-js-26-x-now-available-on-vercel-sandboxes)

**原文标题**: [Node.js 26.x now available on Vercel Sandboxes - Vercel](https://vercel.com/changelog/node-js-26-x-now-available-on-vercel-sandboxes)

Vercel Sandbox现已支持Node.js 26版本。

- 🚀 Vercel Sandbox 新增对 Node.js 26 的支持
- ⬆️ 升级 @vercel/sandbox 至 1.10.2 或更高版本（v2 用户需升级至 2.0.0-beta.19 或更高）
- ⚙️ 在创建 Sandbox 时将 runtime 属性设置为 "node26"
- 📄 提供代码示例展示如何创建 Sandbox 并运行 Node.js 命令
- 🔗 可查阅官方文档了解更多详情

---

### [逐个库修复JavaScript可观测性 | Sentry博客](https://blog.sentry.io/fixing-javascript-observability/)

**原文标题**: [Fixing JavaScript observability, one library at a time | Sentry Blog](https://blog.sentry.io/fixing-javascript-observability/)

以下是您提供的文章的总结：

JavaScript 可观测性正从“猴子补丁”转向内置运行时 API，Sentry 正主导这一跨生态系统的迁移。

- 🐒 猴子补丁无法扩展：所有 JS APM 工具依赖的运行时拦截（如 import-in-the-middle）存在 ESM 兼容性、初始化顺序、打包器冲突等问题，且无法在非 Node 运行时工作。
- 📡 TracingChannels 是无补丁的可观测性方案：Node.js 内置的 `diagnostics_channel` API 允许库发布结构化事件，APM 工具可订阅而无需补丁，零开销且跨运行时兼容。
- 🤝 共识存在但缺乏推动：社区普遍认可 TracingChannel 是未来，但缺乏实际推动库采用的工作。Sentry 主动提供代码并协助维护，已获得 pg、mysql2、redis 等顶级库的同意。
- 🤖 借助 AI 规模化：作者使用 Claude Code 处理研究、实现和审查反馈，将原本数年的单人工作转化为每日产出提案的生产线，同时保持人类主导架构决策和维护者沟通。
- ✅ 进展显著：44 个目标库中已有 10 个合并（如 mysql2、node-redis、ioredis、h3），4 个 PR 开放，8 个在讨论中，22 个未启动。
- 🔄 飞轮效应启动：库添加 TracingChannel 支持后，社区自发构建订阅者（如 mysql2-otel-instrumentation），APM 工具无需维护运行时特定 hack。
- 🔮 未来计划：继续推动 Express、PostgreSQL、Knex、GraphQL 等库的 PR，设计共享映射器注册表以标准化事件到 OpenTelemetry 的转换，最终实现库原生发射事件、社区维护映射器、APM 工具专注于数据分析。

---

### [诊断通道 | Node.js v26.1.0 文档](https://nodejs.org/api/diagnostics_channel.html#diagnostics-channel)

**原文标题**: [Diagnostics Channel | Node.js v26.1.0 Documentation](https://nodejs.org/api/diagnostics_channel.html#diagnostics-channel)

Node.js 的 `node:diagnostics_channel` 模块提供了一套用于诊断目的、可命名通道的发布/订阅 API，允许模块发布任意消息数据，并支持同步/异步追踪、上下文存储绑定以及多种内置通道（如 HTTP、控制台等）。

- 📡 **核心概念**：通过 `diagnostics_channel.channel(name)` 创建可复用的命名通道，用于高效发布和订阅诊断消息，避免运行时查找开销。
- 🔌 **订阅与发布**：使用 `subscribe(name, onMessage)` 注册同步处理函数，通过 `channel.publish(message)` 发布消息，处理函数中的错误会触发 `'uncaughtException'`。
- 🔍 **性能优化**：通过 `channel.hasSubscribers` 或 `diagnostics_channel.hasSubscribers(name)` 预检查是否有活跃订阅者，避免昂贵消息的无效准备。
- 🧵 **追踪通道**：`TracingChannel` 封装 `start`、`end`、`asyncStart`、`asyncEnd`、`error` 五个事件，支持 `traceSync`、`tracePromise`、`traceCallback` 方法，自动管理上下文存储。
- 📦 **有界通道**：`BoundedChannel` 是简化版追踪通道，仅含 `start` 和 `end` 事件，适用于纯同步操作，支持 `run` 和 `withScope` 方法。
- 🗃️ **异步存储绑定**：通过 `channel.bindStore(store, transform)` 将 `AsyncLocalStorage` 绑定到通道，`runStores` 和 `withStoreScope` 在作用域内自动设置和恢复上下文。
- 🧹 **资源管理**：`withStoreScope` 和 `withScope` 方法返回可处置作用域对象，配合 `using` 语法自动清理，避免手动恢复上下文。
- 🏗️ **内置通道**：提供 `console`、`HTTP`、`HTTP/2`、`NET`、`UDP`、`Process`、`Modules`、`Web Locks`、`Worker Thread` 等模块的预定义诊断事件，用于监控关键操作。

---

### [逐步修复JavaScript可观测性，一次一个库 | Sentry博客](https://blog.sentry.io/fixing-javascript-observability/#10-merged-34-to-go-4)

**原文标题**: [Fixing JavaScript observability, one library at a time | Sentry Blog](https://blog.sentry.io/fixing-javascript-observability/#10-merged-34-to-go-4)

### 概述总结
JavaScript APM工具长期依赖monkey-patching进行库检测，但这种方法在ESM、非Node运行时和打包器中存在根本性缺陷。Sentry团队正推动使用Node.js内置的`diagnostics_channel`模块中的`TracingChannel` API，让库自身发布结构化事件，APM工具无需修补即可订阅。目前已在44个库中推进，10个已合并，并利用AI辅助加速实现。

- 🐒 **Monkey-patching的局限性**：拦截`require()`和`import`的方式在ESM中失效，不兼容非Node运行时和打包器，且要求SDK必须在库之前加载，否则检测静默失败。
- 🔧 **TracingChannel解决方案**：库通过`diagnostics_channel`发布事件（如“查询开始/结束”），APM工具直接订阅，无需修补、零开销、跨运行时（Node/Bun/Deno）且兼容打包器。
- 🤝 **生态合作现状**：各方认可TracingChannel是未来，但缺乏推动力。Sentry主动提供PR并承担维护责任，已获得pg、mysql2、redis等主流库的接纳。
- 🤖 **AI辅助规模化**：使用Claude Code处理研究、提案、实现和审查反馈，人类负责架构决策和维护者沟通，将单人多年工作转化为每日并行产出的流水线。
- 📊 **进展数据**：44个库中10个已合并（如mysql2、node-redis、ioredis、h3），4个PR开放，8个在讨论，22个未启动。涵盖数据库、Web框架、消息队列和AI提供商。
- 🚀 **对Sentry的意义**：从“外部修补”转为“订阅库自有事件”，解决ESM、初始化顺序、运行时锁定和打包器冲突问题，简化检测代码。
- 🔄 **飞轮效应启动**：如node-redis团队主动对齐TracingChannel与自有OTel检测；mysql2合并后社区独立构建了纯diagnostics_channel订阅者。
- 📋 **下一步计划**：推进Express、PostgreSQL、Knex、GraphQL等库的PR；设计共享映射器注册表，将TracingChannel事件标准化为OTel span；长期目标是让库事件成为一等公民，APM工具竞争数据分析而非检测技巧。

---

### [你的递归在欺骗你](https://blog.gaborkoos.com/posts/2026-05-09-Your-Recursion-Is-Lying-to-You/)

**原文标题**: [Your Recursion Is Lying to You](https://blog.gaborkoos.com/posts/2026-05-09-Your-Recursion-Is-Lying-to-You/)

### 概述总结
递归在逻辑上优雅，但受限于运行时栈空间，尾递归优化（TCO）在JavaScript中并不可靠，生产环境中应优先使用迭代或蹦床模式。

- 🔄 **递归的陷阱**：即使逻辑正确，深层递归仍会因栈空间耗尽导致`RangeError`，例如`sum(100000)`在多数JS运行时会崩溃。
- 🚫 **尾递归并非万能**：虽然结构上优化了栈使用，但多数JS引擎（如Chrome V8、Firefox SpiderMonkey）未完全实现TCO，尾递归代码仍可能栈溢出。
- ⏱️ **斐波那契的额外问题**：朴素递归版本呈指数级时间复杂度（O(2ⁿ)），导致页面冻结，与栈溢出是不同问题。
- 🧩 **运行时兼容性**：截至2026年，主流运行时（Chrome、Node、Deno、Firefox）均不保证TCO，Safari的JavaScriptCore实现也不一致。
- 🛠️ **生产实践建议**：用迭代替代递归（如`sumIter`）或采用蹦床模式（`trampoline`），以显式控制栈行为，避免依赖运行时优化。
- ✅ **实用清单**：不假设TCO存在；用真实边界测试；深度未知时用迭代；将递归视为可读性工具而非安全保证。

---

### [获取失败](https://nodeweekly.com/link/185153/web)

**原文标题**: [Failed to retrieve](https://nodeweekly.com/link/185153/web)

无法总结：获取内容失败，状态码 404。

---

### [Node.js 中基于 QUIC 的 HTTP/3 | James M Snell](https://www.jasnell.me/posts/quic-part-4)

**原文标题**: [HTTP/3 Over QUIC in Node.js | James M Snell](https://www.jasnell.me/posts/quic-part-4)

本篇文章详细介绍了 Node.js 中 `node:quic` 模块的 HTTP/3 功能，包括请求/响应模型、头部、尾部、流优先级、GOAWAY 和 ORIGIN 帧等核心特性。

- 📡 **HTTP/3 自动激活**：当 ALPN 协议默认为 `'h3'` 时，QUIC 会话自动升级为 HTTP/3 会话，支持头部、尾部、优先级等高级功能。
- 🔄 **基础请求/响应**：通过 `onheaders` 回调处理请求头部，使用 `sendHeaders()` 发送响应头部，支持 GET 和 POST 请求，POST 可附带文件或 JSON 数据。
- ℹ️ **信息性响应 (1xx)**：支持 103 Early Hints 等状态码，通过 `sendInformationalHeaders()` 发送，客户端用 `oninfo` 回调接收。
- 📦 **尾部头部 (Trailers)**：在响应体发送完毕后，通过 `onwanttrailers` 回调触发 `sendTrailers()` 发送元数据，客户端用 `ontrailers` 接收。
- ⚡ **流优先级**：支持 RFC 9218 优先级方案，可在创建流时设置 `priority` 和 `incremental`，并可通过 `setPriority()` 动态调整。
- 🚪 **GOAWAY 优雅关闭**：服务器调用 `session.close()` 时发送 GOAWAY 帧，客户端通过 `ongoaway` 回调接收，之后新流创建会失败。
- 🌐 **ORIGIN 帧**：服务器通过 `onorigin` 回调广告其权威来源，支持连接合并（connection coalescing）。
- 📨 **HTTP/3 数据报**：通过 `enableDatagrams` 选项启用，支持不可靠、无序的消息传输，适用于实时低延迟场景。
- ⚙️ **HTTP/3 设置**：通过 `application` 选项配置头部限制、QPACK 表容量、扩展 CONNECT 协议等参数。
- ❌ **未实现功能**：不包括服务器推送、WebTransport、高级路由、内容协商、自动压缩等高层语义，这些留待后续框架实现。

---

### [Bun v1.3.14 | Bun 博客](https://bun.com/blog/bun-v1.3.14)

**原文标题**: [Bun v1.3.14 | Bun Blog](https://bun.com/blog/bun-v1.3.14)

## 概述摘要

Bun 发布了重大更新，包含内置图像处理 API、HTTP/3 支持、性能大幅提升以及大量 Bug 修复。

- 🖼️ **内置图像处理** - Bun.Image 提供链式图像处理管道，支持 JPEG/PNG/WebP/GIF/BMP 等格式，性能比 sharp 快 1.2-70 倍
- 🚀 **HTTP/3 (QUIC) 支持** - Bun.serve 新增实验性 HTTP/3 支持，静态路由性能达 509,135 req/s，比 HTTPS/1.1 快 2.7 倍
- 🌐 **HTTP/2 客户端** - fetch() 实验性支持 HTTP/2 多路复用，同一连接共享 TLS 握手
- ⚡ **全局虚拟存储** - bun install 新增 globalStore 选项，热安装速度提升 7 倍（841ms → 115ms）
- 🛡️ **--no-orphans 模式** - 父进程死亡时自动退出并清理子进程，支持 Linux/macOS
- 🔧 **process.execve() 支持** - 实现 Node.js v24 API，可替换当前进程映像
- 📦 **更小的二进制体积** - Linux 减少 6-9MB，Windows 减少 17-18MB
- 🔄 **重写 fs.watch()** - 直接使用 inotify/FSEvents/kqueue，修复递归监控新目录等长期 Bug
- 🎯 **ESM 模块加载提速 12%** - 修复解析器 struct 复制开销问题
- 💾 **减少 GC 开销** - 移除 63 种内置对象的冗余重新扫描
- 🐛 **修复 200+ Bug** - 涵盖内存泄漏、崩溃、安全漏洞、兼容性问题等
- 🏆 **性能基准** - HTTP 吞吐量提升 3.5%，Bun.escapeHTML 快 6.5%，TextDecoder 快 2.6%

---

### [高性能Node.js图像处理 | sharp](https://sharp.pixelplumbing.com/)

**原文标题**: [High performance Node.js image processing | sharp](https://sharp.pixelplumbing.com/)

Sharp 是一个高性能 Node.js 图像处理模块，基于 libvips 库实现快速图像缩放、格式转换和优化，支持多种运行环境和输入输出方式。

- 🚀 性能卓越：利用 libvips 库，图像缩放速度比 ImageMagick 和 GraphicsMagick 快 4-5 倍，支持多核 CPU 和缓存优化。
- 🖼️ 格式广泛：支持读取 JPEG、PNG、WebP、GIF、AVIF、TIFF 和 SVG，输出格式包括 JPEG、PNG、WebP、GIF、AVIF、TIFF 及原始像素数据。
- 🔧 功能丰富：提供缩放、旋转、裁剪、合成和伽马校正等操作，采用 Lanczos 重采样保证质量。
- 🌐 跨平台兼容：支持 Node.js >= 18.17.0、Deno 和 Bun，无需额外依赖即可在 macOS、Windows 和 Linux 上运行。
- 📦 灵活输入输出：支持流、Buffer 和文件系统，单个输入流可拆分为多个处理管道。
- 🗺️ 高级功能：可生成 Deep Zoom 图像金字塔，适用于 OpenSeadragon 等地图查看器。
- ⚡ 非阻塞处理：基于 libuv 实现异步操作，支持 Promise 和 async/await，无子进程开销。
- 🎯 文件优化：集成 mozjpeg 和 pngquant 优化 JPEG/PNG 大小，自动优化 Huffman 表和 GIF 动画。
- 🤝 开源贡献：遵循 Apache 2.0 许可证，欢迎通过指南报告问题或提交代码。

---

### [全球虚拟商店 | pnpm](https://pnpm.io/global-virtual-store)

**原文标题**: [Global Virtual Store | pnpm](https://pnpm.io/global-virtual-store)

pnpm 的全局虚拟存储功能，通过共享依赖来优化磁盘空间和安装速度。

- 📦 **默认行为**：每个项目在 `node_modules/.pnpm` 中创建独立的虚拟存储，包含指向内容可寻址存储的硬链接。文件内容不重复，但目录结构会重复，在大型项目或多分支开发时，创建硬链接耗时较长。
- 🌐 **全局虚拟存储**：启用后，所有项目共享一个位于 `<store-path>/links/` 的虚拟存储。每个项目的 `node_modules` 只包含指向此共享位置的符号链接，避免了重复的目录结构。
- 🔗 **包标识机制**：每个包目录根据其依赖图的哈希值命名。相同依赖树的项目指向同一目录，依赖树不同时则创建独立条目，类似 NixOS 的管理方式。
- 🛠️ **适用场景**：最适合同一项目的多个检出（如使用 `git worktrees`），或同一机器上多个不相关项目，能显著加速安装过程。
- ⚠️ **限制**：在 CI 环境中无缓存优势；对 ESM 导入不支持 `NODE_PATH`，可能导致解析失败，需通过 `packageExtensions` 或插件解决。
- 🧪 **实验性状态**：默认禁用，需在 `pnpm-workspace.yaml` 中设置 `enableGlobalVirtualStore: true`。pnpm v11 中，`pnpm dlx` 和全局安装默认启用。
- 🌍 **全局包管理**：pnpm v11 中，全局安装和 `pnpm dlx` 默认使用全局虚拟存储，详情见全局包指南。

---

### [Bun v1.3.14 | Bun 博客](https://bun.com/blog/bun-v1.3.14#node-js-compatibility-improvements)

**原文标题**: [Bun v1.3.14 | Bun Blog](https://bun.com/blog/bun-v1.3.14#node-js-compatibility-improvements)

## 概述

Bun 发布了重大更新，引入了内置图像处理API、HTTP/3支持、实验性HTTP/2客户端、全局虚拟存储、改进的文件监视系统、父进程死亡自动退出功能，以及大量性能优化和错误修复。

- 🖼️ **内置图像处理** - Bun.Image 提供链式图像处理管道，支持JPEG、PNG、WebP、GIF、BMP等格式，无需安装任何原生模块，性能比sharp快1.2-70倍
- 🌐 **HTTP/3 (QUIC) 支持** - 通过 `http3: true` 标志启用，性能比HTTPS/1.1快2.7倍，支持流式传输、文件响应和请求体透传
- 🔄 **实验性HTTP/2客户端** - fetch() 支持HTTP/2多路复用，多个并发请求共享单个TCP+TLS连接，支持连接合并和流控制
- 🚀 **实验性HTTP/3客户端** - fetch() 支持HTTP/3协议，可通过 `protocol: "http3"` 选项启用，支持Alt-Svc自动升级
- 💾 **全局虚拟存储** - bun install 新增 `globalStore` 选项，将包链接到全局目录而非每个项目复制，安装速度提升7倍
- 👁️ **文件监视重写** - fs.watch() 在Linux/macOS/FreeBSD上完全重写，支持递归监视新创建目录，修复了多个长期存在的bug
- 👻 **--no-orphans 功能** - 父进程死亡时自动退出，并递归终止所有子进程，支持Linux的prctl和macOS的kqueue
- ⚡ **性能优化** - Zig↔C++跨语言LTO优化使HTTP吞吐量提升3.5%，ESM模块加载速度提升12%，减少GC开销和二进制体积
- 🛠️ **Node.js兼容性改进** - 修复了node:http、node:zlib、crypto、TLS等多个模块的内存泄漏和崩溃问题
- 🪟 **Windows增强** - Bun.Terminal通过ConPTY API支持Windows，SIGHUP/SIGBREAK信号处理，改进系统CA证书加载
- 📦 **bun publish 改进** - 现在自动发送README元数据到npm注册表，确保包描述正确显示
- 🔒 **安全修复** - 修复了HTTP请求走私、Blob反序列化边界检查、IPC序列化整数溢出等安全问题
- 🐛 **大量Bug修复** - 修复了超过100个bug，涵盖Bun Shell、WebSocket、Worker、定时器、bun install、打包器、CSS解析器等

---

### [如何使用Node.js和Google Cloud Run发送和接收短信](https://developer.vonage.com/en/blog/how-to-send-and-receive-sms-messages-with-node-js-and-google-cloud-run?cmp=eml-api-api-gbl-cooperpress-prosp-news)

**原文标题**: [How to Send and Receive SMS Messages with Node.js and Google Cloud Run](https://developer.vonage.com/en/blog/how-to-send-and-receive-sms-messages-with-node-js-and-google-cloud-run?cmp=eml-api-api-gbl-cooperpress-prosp-news)

本教程详细介绍了如何使用Node.js、Express和Vonage Messages API在Google Cloud Run上构建和部署短信应用，涵盖从项目初始化、依赖安装、服务器搭建到云部署和测试的完整流程。

- 📱 **项目概述**：使用Node.js、Express和Vonage Messages API构建短信应用，部署在Google Cloud Run上，支持自动伸缩和按需付费。
- 🛠️ **前提条件**：需要Node.js v18+、Google Cloud CLI、Google Cloud账号（已启用结算）以及JavaScript/Node.js基础知识。
- 📂 **项目结构**：包含index.js（主逻辑）、package.json（依赖）、.env.example（环境变量模板）、.gitignore和private.key（私钥）。
- 🔑 **创建Vonage应用**：在Vonage Dashboard创建应用，生成公私钥对（私钥需安全存储），并配置Messages API能力及Webhook URL。
- 📞 **购买和链接虚拟号码**：在Vonage Dashboard购买虚拟号码，并将其链接到应用，同时确保在设置中将Messages API设为默认SMS API。
- 📦 **初始化与安装**：创建项目目录，运行`npm init -y`，安装express、@vonage/server-sdk和@vonage/jwt依赖。
- 🚀 **服务器搭建**：创建index.js，初始化Express服务器和Vonage客户端，配置环境变量读取，并添加首页表单、发送端点及Webhook端点（含JWT验证）。
- ☁️ **部署到Cloud Run**：设置Google Cloud项目、启用Cloud Build和Cloud Run API，使用`gcloud run deploy`命令部署，并传递环境变量。
- 🔄 **更新Webhook**：部署后，将Vonage应用中的Webhook URL更新为Cloud Run提供的URL（/webhooks/inbound和/webhooks/status）。
- ✅ **测试功能**：通过浏览器访问Cloud Run URL发送短信，并用手机回复购买的虚拟号码接收短信，同时通过命令行或Dashboard查看日志。

---

### [JavaScript 单体仓库中的一致依赖版本 | Syncpack](https://syncpack.dev/)

**原文标题**: [Consistent dependency versions in JavaScript Monorepos | Syncpack](https://syncpack.dev/)

Syncpack 是一个用于大型 JavaScript 单体仓库（Monorepo）的命令行工具，旨在确保依赖版本的一致性，被 AWS、Cloudflare、微软等众多知名公司使用。

- 🔧 查找并修复依赖版本不匹配问题
- 🎯 强制执行单一版本策略或为不同分区设置独立策略
- 🔄 从 npm 注册表查找并升级过时版本
- 📌 确保某些依赖始终固定在特定版本
- 🚫 禁止某些依赖在特定位置或全局使用
- ⚙️ 定义精确或宽松 semver 范围的使用规则（包括在目录中）
- 📂 将特定包指定为依赖版本的来源
- 📝 统一排序和格式化 package.json 文件
- 🚀 自动迁移仓库到 pnpm 或 bun 目录
- 🔄 更新目录中的过时版本
- 🧪 通过 `npx syncpack` 快速试用
- 📖 支持 `--help` 查看命令选项和文档
- 🛠️ 安装到 devDependencies 以确保团队版本一致
- 🔍 使用 `list`、`lint`、`fix`、`update` 等命令管理依赖
- ⚡ 支持过滤特定依赖或依赖类型（如 prod、dev）
- 📁 通过 `.syncpackrc` 配置文件自定义行为（如版本组、semver 组）
- 🔗 推荐使用 `workspace:*` 协议引用本地包
- 📚 提供 Peer Dependencies 和 Semver Groups 等进阶指南

---

### [发布 15.0.0 · JamieMason/syncpack · GitHub](https://github.com/JamieMason/syncpack/releases/tag/15.0.0)

**原文标题**: [Release 15.0.0 · JamieMason/syncpack · GitHub](https://github.com/JamieMason/syncpack/releases/tag/15.0.0)

以下是您提供的文本摘要：

syncpack 15.0.0 版本发布，主要新增了对 pnpm 和 bun 目录的全面支持，并引入了一些新功能和破坏性变更。

- 🚀 新增对 pnpm 和 bun 目录的完整支持，使其成为 syncpack 中的一等公民，可进行分组、定位、更新或禁用。
- 📦 引入“目录版本组”功能，可自动将仓库的全部或部分迁移到目录，并确保未来使用正确的目录。
- 🔄 `syncpack update --dependency-types pnpmCatalog` 命令可更新默认目录至 npm 注册表的最新版本，而“语义版本组”可确保目录使用精确版本号。
- ⏳ 新增 `minimumReleaseAge` 配置，默认值为 1 天，若未设置则遵循 pnpm 配置。
- 📝 重写了 `customTypes` 文档，并在 `syncpack update` 文档中添加了目录示例。
- ⚠️ 破坏性变更：`pnpmOverrides` 现在从 `pnpm-workspace.yaml` 读取覆盖项，而非 `package.json`。如需恢复旧行为，可在配置中定义 `pnpmOverridesLegacy`。
- 🐛 修复了多个问题，包括 Cargo 依赖更新、CLI 错误显示、Windows 上的 ESM URL 方案错误、项目检测、musl libc 二进制解析以及 Rust 版本更新。

---

### [Counterfact — API 模拟器](https://counterfact.dev/)

**原文标题**: [Counterfact — API Simulator](https://counterfact.dev/)

Counterfact 是一个超越传统 mock 服务器的 API 模拟工具，它根据 OpenAPI 规范即时生成一个带状态、可编程的实时 API，并提供 TypeScript 类型安全、热重载、共享状态和 REPL 控制台等强大功能。

- ⚡ **一键生成实时 API**：只需一个命令 `npx counterfact@latest` 指向 OpenAPI 规范，即可在几秒内获得一个带状态、类型安全的实时 API 服务器。
- 🧩 **契约驱动代码生成**：自动为每个端点生成 TypeScript 处理器和类型接口，确保代码与规范同步，杜绝漂移。
- 🔄 **热重载保状态**：保存路由文件后服务器即时更新，内存状态在每次重载中完整保留，无需中断。
- 💻 **可编程 REPL 控制台**：提供与运行中服务器直连的 JavaScript 交互式环境，可实时检查状态、注入故障、切换代理路由。
- 🗃️ **跨路由共享状态**：通过 `_.context.ts` 文件在任意目录下共享类型化的内存状态，所有路由（POST、GET、DELETE 等）访问同一数据源。
- 🌐 **混合代理模式**：可将部分路由转发到真实后端，其余部分继续使用模拟，并支持从 REPL 实时切换。
- 🔄 **确定性重置**：重启后系统回到已知状态，需要时可重复，需要真实感时可编程，并支持通过 TypeScript 实现持久化。
- 👥 **面向多角色用户**：前端开发者可提前构建应用，测试工程师可获得可复现的测试状态，AI 代理/自动化工作流可获得稳定、可脚本化的 API 基础。

---

### [GitHub - counterfact/api-simulator：不仅仅是模拟服务器。将OpenAPI规范转化为基于TypeScript的模拟，具备状态管理、热重载和REPL功能。](https://github.com/counterfact/api-simulator)

**原文标题**: [GitHub - counterfact/api-simulator: Not just a mock server. Turn an OpenAPI spec into TypeScript-based simulation, with state management, hot reload, and a REPL. · GitHub](https://github.com/counterfact/api-simulator)

Counterfact 是一个基于 OpenAPI 规范的 API 模拟器，提供有状态、可热重载且支持运行时控制的 TypeScript 仿真环境。

- 🚀 支持 Swagger 2.0、OpenAPI 3.0/3.1/3.2，快速生成有状态 API
- 🔧 提供类型安全的 TypeScript 端点处理器，支持热重载
- 🔗 跨路由共享状态，内置 REPL 可运行时控制行为
- 🔄 可选代理到真实后端，灵活适配开发与测试场景
- 🎯 面向前端开发者、测试工程师和 AI 代理，兼具真实性与可用性
- 📦 通过 `npx counterfact@latest` 快速启动，需 Node ≥ 22.0.0
- 📚 提供详细文档、示例仓库和对比指南（json-server、WireMock 等）
- ⭐ GitHub 上获得 144 星，20 个 fork，127 个发布版本

---

### [pnpm 11.1 | pnpm](https://pnpm.io/blog/releases/11.1)

**原文标题**: [pnpm 11.1 | pnpm](https://pnpm.io/blog/releases/11.1)

以下是 pnpm 11.1 版本的总结：

pnpm 11.1 新增了多个命令和功能，包括包签名验证、命名注册表支持、CI 优化以及多项修复。

- 🔍 **新增 `pnpm audit signatures` 命令**：验证已安装包的 ECDSA 注册表签名，确保包来源可信。
- 🏷️ **支持命名注册表及内置 `gh:` 别名**：可通过 `gh:@acme/private` 安装 GitHub Packages，并支持在 `pnpm-workspace.yaml` 中自定义别名。
- 📦 **`pnpm sbom` 新增 `--sbom-spec-version` 标志**：可选择 CycloneDX 规范版本（1.5、1.6 或 1.7），默认 1.7。
- ⏭️ **CI 中新增 `--no-runtime` 标志**：跳过运行时安装（如 Node.js），不修改锁文件，适合外部提供运行时的 CI 矩阵。
- 🐛 **新增 `pnpm bugs` 命令**：在浏览器中打开包的 bug 追踪器 URL，支持当前项目或指定包。
- 👤 **新增 `pnpm owner` 命令**：管理注册表上的包所有者，支持列出、添加和删除操作。
- 📝 **`pnpm view` 显示发布时间**：输出中包含“published X ago by Y”信息，便于与 `minimumReleaseAge` 比较。
- 🌐 **`pnpm publish` 尊重 HTTP/HTTPS 代理**：在基于 Web 的身份验证流程中正确使用代理，修复 403 错误。
- 📂 **`pnpm add -g` 默认隔离安装**：每个包独立安装，逗号分隔的包可共享依赖并一起移除。
- 🛠️ **修复 `pnpm runtime set` 在多包工作区根目录失败问题**：不再触发 `ADDING_TO_ROOT` 错误。
- 🚀 **修复 `pnpm --version` 挂起问题**：版本输出后正确关闭工作池。

---

### [获取失败](https://nodeweekly.com/link/185165/web)

**原文标题**: [Failed to retrieve](https://nodeweekly.com/link/185165/web)

无法总结：获取内容失败，状态码 403。

---

### [帕特里克](https://patrickbrosset.com/)

**原文标题**: [Patrick ](https://patrickbrosset.com/)

概述总结  
- 🧑‍💻 Patrick是微软Edge团队的产品经理，拥有20多年网页开发经验，曾任职于Mozilla和多个技术岗位。  
- 🌐 他参与Open Web Docs治理委员会、W3C WebDX社区联合主席，并运营DevTools Tips网站。  
- 📧 联系方式：可通过页面底部社交链接或邮箱patrickbrosset@gmail.com联系。  
- 📦 2026年5月13日：新HTML `<install>` 元素简化网页应用安装。  
- ⚡ 2026年3月17日：Edge团队提出“网络效率护栏”功能，帮助开发者监控和优化网页加载性能。  
- 🎨 2026年3月11日：利用可定制 `<select>` 元素制作趣味演示，探索新功能的创意用途。  
- 🔷 2026年4月30日：CSS `shape()` 函数可实现星形变形等动态裁剪效果。  
- 🌀 2026年2月25日：滥用CSS间隙装饰功能，通过旋转网格和空内容创建艺术图案。  
- 🎤 2026年4月21日：在BlinkOn主持历史讨论小组，回顾IE到Chromium Edge的过渡时期。  
- 📊 2026年1月31日：在FOSDEM演讲中介绍browser-compat-data、web-features和Baseline项目，提升开发者体验。

---

### [API 密钥正式发布](https://clerk.com/changelog/2026-04-17-api-keys-ga?utm_source=cooper_press&utm_medium=newsletter&utm_campaign=api-keys&utm_content=05-14-26&dub_id=p9BtV3U40eWQ0ME2)

**原文标题**: [API Keys General Availability](https://clerk.com/changelog/2026-04-17-api-keys-ga?utm_source=cooper_press&utm_medium=newsletter&utm_campaign=api-keys&utm_content=05-14-26&dub_id=p9BtV3U40eWQ0ME2)

概述：API密钥现已全面上线，并启用基于使用量的计费模式。

- 🔑 API密钥现已正式发布，属于机器认证套件的一部分，允许用户创建代表其应用API访问权限的凭证。
- 💰 计费已启用，每月包含免费额度：1000次密钥创建（超出后每次$0.001）和100,000次密钥验证（超出后每次$0.00001）。
- 📘 提供API密钥指南，完整介绍启用和使用API密钥的步骤。
- 🛠️ 后端SDK参考文档包含创建、列出、验证和撤销密钥的完整API。
- 🖥️ 可在仪表盘中为应用程序启用API密钥。

---

### [GitHub - Agent-Field/agentfield: 像API和微服务一样构建、运行和扩展AI代理——从第一天起就具备可观察、可审计和身份感知能力。](https://github.com/Agent-Field/agentfield)

**原文标题**: [GitHub - Agent-Field/agentfield: Build, run and scale AI agents like API and microservices - observable,auditable and identity-aware from day one. · GitHub](https://github.com/Agent-Field/agentfield)

AgentField 是一个开源 AI 后端控制平面，能将 AI 智能体像 API 和微服务一样构建、运行和扩展，具备开箱即用的可观测性、审计和身份认证。

- 🚀 **核心能力**：将智能体逻辑（Python/Go/TypeScript）自动转为 REST 端点，支持结构化 AI 输出、跨智能体调用、异步执行和人类审批暂停。
- 🧠 **AI 与 LLM**：通过 `app.ai(schema=MyModel)` 获取结构化输出，支持 100+ 模型、流式响应、多模态和工具自动发现。
- 🏗️ **智能体网格**：支持按标签发现智能体、跨智能体路由（带追踪）、并行执行和自动上下文传播。
- ⏳ **执行引擎**：提供同步/异步 REST、SSE 流式、Webhook 回调、无限超时、自动重试和基于 PostgreSQL 的持久队列。
- 💾 **分布式记忆**：内置 KV 存储、向量语义搜索、四种作用域（全局/智能体/会话/运行）和响应式事件。
- 👤 **人机协同**：`app.pause()` 实现持久化暂停/恢复、审批工作流、可配置超时和崩溃安全状态。
- 🚦 **金丝雀部署**：支持流量权重路由、A/B 测试、蓝绿部署，以及按版本健康状态自动移除。
- 🔐 **身份与治理**：每个智能体拥有 W3C DID 加密身份，提供可验证凭证、标签策略、签名请求和不可否认审计。
- 📊 **可观测性**：自动 DAG 可视化、Prometheus 指标、结构化日志、执行时间线和健康检查。
- 🛠️ **开发者体验**：CLI 脚手架、本地仪表盘、热重载、多语言 SDK 和 MCP 服务器集成。
- 🏢 **适用场景**：适合构建生产级后端智能体系统（如理赔处理、研究引擎、安全审计），而非简单的聊天机器人或早期工作流。

---

### [GitHub - Agent-Field/agentfield: 像API和微服务一样构建、运行和扩展AI代理——从第一天起就具备可观察、可审计和身份感知能力。](https://github.com/Agent-Field/agentfield)

**原文标题**: [GitHub - Agent-Field/agentfield: Build, run and scale AI agents like API and microservices - observable,auditable and identity-aware from day one. · GitHub](https://github.com/Agent-Field/agentfield)

AgentField 是一个开源 AI 后端控制平面，可将 AI 代理构建为可调用的 API，并提供生产级基础设施。

- 🚀 **核心概念**：将 AI 代理构建为类似 API 的后端服务，支持 Python、Go、TypeScript 编写，每个函数自动成为 REST 端点。
- 🧠 **结构化 AI 输出**：通过 `app.ai(schema=MyModel)` 调用 LLM 并返回类型化输出（如 Pydantic/Zod），支持 100+ 模型。
- ⏸️ **人工审批**：`app.pause()` 可暂停执行等待人工批准，支持超时和自动升级，崩溃安全且可审计。
- 🔗 **跨代理路由**：`app.call("agent.func")` 通过控制平面路由到其他代理，并带有完整追踪。
- ⚙️ **异步执行**：支持即发即弃、SSE 流式传输、Webhook 回调，无超时限制，可运行数小时或数天。
- 🛡️ **加密身份与治理**：每个代理自动生成 W3C DID 和 Ed25519 密钥，提供可验证凭证和基于标签的策略执行。
- 📊 **可观测性**：自动生成工作流 DAG 图、Prometheus 指标、结构化日志和执行时间线。
- 🚦 **金丝雀部署**：支持流量权重路由、A/B 测试和蓝绿部署，可逐步推出代理版本。
- 🧩 **多代理网格**：通过标签发现代理和功能，支持并行执行和自动上下文传播。
- 💾 **分布式内存**：内置 KV 存储和向量搜索，支持全局、代理、会话和运行四种作用域，无需 Redis。
- 🔧 **开发者体验**：提供 CLI 脚手架、本地仪表盘、热重载，以及 Python、Go、TypeScript SDK。
- 🏗️ **架构**：控制平面为无状态 Go 服务，代理可连接自任何地方，支持 Docker 和 Kubernetes 部署。

---

### [zero-native | 使用Zig和WebView构建桌面应用](https://zero-native.dev/)

**原文标题**: [zero-native | Desktop Apps with Zig + WebView](https://zero-native.dev/)

### 概览摘要
zero-native 是一个用于构建原生桌面应用的框架，使用 Web UI 技术，生成极小的二进制文件，内存占用低，并支持即时重建。

- 📦 **极致小巧**：使用系统 WebView 时，二进制文件小于 1MB，内存占用远低于传统框架，无运行时臃肿。
- 🌐 **灵活引擎选择**：可根据项目需求选择轻量系统 WebView 或通过 CEF 捆绑 Chromium，API 一致但权衡不同。
- ⚡ **快速原生重建**：Zig 编译极快，修改桥接命令或系统集成后数秒内重建二进制，前端仍可即时热重载。
- 🔗 **直接调用 C 库**：无需绑定生成或胶水代码，直接包含头文件即可调用原生 SDK、音频编解码器或 ML 运行时，深度集成无限制。
- 🖥️ **跨平台基础**：目前支持 macOS 和 Linux 桌面壳，Windows 和移动端开发中，原生层简洁，WebView 层熟悉。
- 🧠 **简化原生层**：无需借用检查器、生命周期或复杂编译冲突，Zig 语言简单易读，Web 开发者可快速上手。
- 🚀 **快速启动**：通过 `zero-native init my_app --frontend next` 命令创建项目，首次运行自动安装依赖并打开原生窗口，提供完整快速入门指南。

---

### [GitHub - pionxzh/wakaru: 🔪📦 现代前端的JavaScript反编译器](https://github.com/pionxzh/wakaru)

**原文标题**: [GitHub - pionxzh/wakaru: 🔪📦 Javascript decompiler for modern frontend · GitHub](https://github.com/pionxzh/wakaru)

Wakaru 是一款专为现代前端设计的快速 JavaScript 反编译器和包拆分工具，能一键将混淆、打包后的代码还原为可读的模块。

- 🔪 支持多种打包工具拆分：webpack 4/5、esbuild、Bun、Browserify
- 🔄 恢复多种转译与压缩工具处理：Terser、Babel、SWC、TypeScript
- 🗺️ 支持 Source map，实现更好的标识符恢复与导入去重
- ⚙️ 提供三种重写级别：minimal、standard、aggressive，适应不同需求
- 🚀 快速上手：使用 `npx @wakaru/cli input.js -o output.js` 即可反编译单个文件
- 📦 支持包解包：`wakaru bundle.js --unpack -o out/` 拆分并还原整个包
- 🛡️ 内置覆盖保护，除非使用 `--force` 否则不会覆盖已有文件
- 🤝 欢迎贡献：鼓励分享难以处理的真实包、报告语义或正确性问题
- 📄 基于 Rust 开发，许可证为 Apache-2.0，仅限合法用途

---

### [将Fluxzy从Electron切换到Tauri五个月后](https://fluxzy.io/resources/blogs/electron-to-tauri-migration-fluxzy-desktop)

**原文标题**: [Five months after switching Fluxzy from Electron to Tauri](https://fluxzy.io/resources/blogs/electron-to-tauri-migration-fluxzy-desktop)

以下是对文章内容的总结：

Fluxzy 从 Electron 迁移到 Tauri 五个月后，整体体验积极，但存在一些痛点和注意事项。

- 📦 安装包大小从约 190MB 降至 55MB，内存占用显著减少。
- 🖥️ 从 Chromium 切换到不同 WebView 后，几乎没有出现视觉回归问题。
- 🧠 Electron 在开发者中口碑不佳，迁移到 Tauri 有助于提升产品形象。
- ⚡ 冷启动和文件打开速度明显提升，用户无需提示就能察觉。
- 🔒 Tauri 的权限模型清晰且安全，通过 JSON 文件即可管理，无需像 Electron 那样手动处理 IPC。
- 🛠️ 用 Rust 替换 Node 主进程后，代码更严谨，减少了维护负担。
- 🔄 IPC 迁移相对顺利，因为 Fluxzy 的渲染层和主进程已有清晰分离。
- ❗ 缺少 Yes/No/Cancel 对话框，需额外引入 Rust crate 解决。
- ⚠️ 自动更新器不兼容，需发布中间版本引导用户手动升级。
- 🔑 Windows 代码签名需注意顺序：先 Authenticode，再重新生成 minisign 签名。
- 🛑 自托管 Windows 运行环境可能出现工具链漂移，需显式固定 Rust 默认主机。
- 🐧 Linux 上 WebKitGTK 在 Wayland 下有问题，需禁用硬件加速并手动设置深色模式。
- ✅ 代码签名和公证速度更快，Windows SmartScreen 也更快通过。
- 🎯 不选择 Avalonia 或 MAUI 的原因：重写 Angular 前端成本过高，且 Monaco 编辑器无替代品。
- 💡 如果你的 Electron 应用已有清晰的前后端分离，迁移到 Tauri 是值得的；但需提前规划自动更新器桥接和慢速 Rust 构建。

---

