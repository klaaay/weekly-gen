### [Node.js — Node.js 27.0.0-alpha.0.0.0 (Alpha)](https://nodejs.org/en/blog/release/v27.0.0-alpha.0.0.0)

**原文标题**: [Node.js — Node.js 27.0.0-alpha.0.0.0 (Alpha)](https://nodejs.org/en/blog/release/v27.0.0-alpha.0.0.0)

Node.js 27.0.0-alpha.0.0.0 是 2026-10-29 发布的 Alpha 版本，由 Rafael Gonzaga 发布；核心变化是 V8 15.6 升级以及大量 SemVer-Major 破坏性变更，涉及加密、HTTP、网络、权限、构建工具链和运行时行为。

- 🚀 版本定位：Node.js 27.0.0-alpha.0.0.0 Alpha，2026-10-29 发布，作者 @RafaelGSS。
- 🧠 V8 升级：V8 从 14.6 升至 15.6.75.13，默认启用 Math.sumPrecise、Intl.Locale variants、Iterator.join/includes/zip/zipKeyed 等新特性。
- 🧪 实验特性：import defer、Immutable ArrayBuffer、RegExp buffer boundaries 需通过 flag 启用。
- 💾 内存与序列化：默认堆上限改为物理内存一半并限制在 256MB–4GB；Buffer/ArrayBuffer 计入堆；v8.serialize、structuredClone、postMessage 新格式不兼容旧版 Node.js。
- ⚠️ 行为变化：Math 方法改用 LLVM libm，Math.random 序列随 --random-seed 变化，error.stack 不再沿原型链查找，await 微任务减少，大数组 sort 使用 PowerSort 且保持稳定。
- 📸 堆快照与 WebAssembly：堆快照包含内部对象、数值和完整脚本源码，耗时和文件大小约翻倍；asm.js 不再编译为 WebAssembly，--experimental-wasm-* 重命名为 --wasm-*。
- 🔐 加密与 OpenSSL：要求 OpenSSL 3+，升级至 OpenSSL 4.1.0，移除 FIPS provider、旧 OpenSSL 代码路径和 OpenSSL engine 支持，多项 crypto API 进入 EOL 或加强编码校验。
- 🌐 HTTP 与网络：HTTP 拒绝超限响应头，keepAliveTimeout 默认增至 65 秒，req.headers 使用 null 原型，finish 后拒绝 addTrailers；http2 增大默认窗口。
- 🧩 模块与 API：domain 运行期弃用并迁移至 AsyncLocalStorage；fs 原生实现 glob；新增实验性 net/promises；vfs 解除实验标志；新增 fs.mkstemp()。
- 🛡️ 权限与安全：新增 --allow-env 权限；修复 CVE-2026-58042（dns 大 resolveAny 回复）；权限模型相关修正。
- 🧪 测试与工具：test_runner 改用 AsyncLocalStorage，新增 mockReturnValue 和 promise helpers；npm 升级至 12.1.0；Alpine 升为 Tier 2，最低 3.21。
- 🖥️ 平台与产物：Intel macOS 支持降为实验性；提供 Windows、macOS、Linux、AIX、ARM64 等安装包和源码，macOS Intel 二进制尚未提供。

---

### [Node.js — Node.js 发布计划的演进](https://nodejs.org/en/blog/announcements/evolving-the-nodejs-release-schedule)

**原文标题**: [Node.js — Evolving the Node.js Release Schedule](https://nodejs.org/en/blog/announcements/evolving-the-nodejs-release-schedule)

Node.js 将从 27.x 起把大版本发布频率从每年两次改为每年一次，并取消奇偶版区分，让每个版本都进入 LTS；同时新增 Alpha 通道用于早期测试，以降低维护负担并提升企业升级的可预测性。

- 📅 新节奏：每年 4 月发布 Current，10 月转为 LTS；从 27.x 开始，所有大版本都会成为 LTS。
- 🧪 Alpha 通道：约 6 个月（10 月至次年 3 月），允许 semver-major 变更，发布经签名、打标签并通过 CITGM 测试；面向库作者和 CI，不建议生产使用，发布节奏可灵活调整。
- ⏳ 支持周期：Current 约 6 个月，LTS 30 个月；从首个 Current 发布到 EOL 总计 36 个月。
- 🔢 版本号：与首次 Current 发布年份对齐，例如 27.0.0 于 2027 年、28.0.0 于 2028 年。
- 🎯 变更原因：奇数版采用率低、奇偶区分令新人困惑、企业需要可预测性，且志愿者难以长期维护 4-5 条并行发布线。
- ✅ 保持不变：LTS 时长相近、LTS 版本间迁移重叠保留、质量/CITGM/安全流程不变、4 月发布/10 月 LTS 节奏不变、V8 仍最多约 6 个月旧。
- 🗓️ 过渡安排：Node.js 26 是旧模型最后一条发布线；27 于 2026 年 10 月启动 Alpha、2027 年 4 月发布 27.0.0、2027 年 10 月进入 LTS、2030 年 4 月 EOL。
- 📌 对用户：若只升级 LTS，除版本号外变化不大；库作者应尽早把 Alpha 纳入 CI，以便在影响用户前发现并报告问题。
- 🔮 长期规划：未来十年按每年一个大版本推进（27.x 至 36.x），时间表可能调整，以 schedule.json 为准。
- 🙏 背景：该调整来自 GitHub 讨论、Release WG 会议和 Collaboration Summit 2025 的反馈，后续将在伦敦峰会继续讨论。

---

### [Math.sumPrecise() - JavaScript | MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/sumPrecise)

**原文标题**: [Math.sumPrecise() - JavaScript | MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/sumPrecise)

Math.sumPrecise() 是 JavaScript 中用于更精确求和数字可迭代对象的静态方法，自 2026 年 4 月起在最新设备和浏览器版本中可用，旧版本可能不支持。
- 📅 **可用性**：Baseline 2026，自 2026 年 4 月起跨最新设备与浏览器版本可用。
- 🧮 **功能**：接收数字可迭代对象（如数组），返回其总和；比循环累加更精确，避免中间结果的浮点精度损失。
- ✍️ **语法**：`Math.sumPrecise(numbers)`，参数 `numbers` 是数字可迭代对象。
- 🔁 **返回值**：返回数字总和；若可迭代对象为空，返回 `-0`（不是 `0`）。
- ⚠️ **异常**：若参数不可迭代，或其中包含非 number 类型值，抛出 `TypeError`。
- 🧊 **调用方式**：必须使用 `Math.sumPrecise()`，因为 `Math` 不是构造函数。
- 📌 **示例**：`Math.sumPrecise([1, 2])` 返回 `3`；`Math.sumPrecise([1e20, 0.1, -1e20])` 返回 `0.1`，而普通循环会得到 `0`。
- 🚧 **精度限制**：仍无法避免 `0.1 + 0.2` 问题，`Math.sumPrecise([0.1, 0.2])` 返回 `0.30000000000000004`。
- 📚 **规范与兼容**：属于 ECMAScript 2027 规范；可通过 core-js 或 es-shims polyfill 使用，也可参考 `Array.prototype.reduce()`。

---

### [Iterator.zip() - JavaScript | MD](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/zip)

**原文标题**: [Iterator.zip() - JavaScript | MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/zip)

本文介绍了 JavaScript 的 `Iterator.zip()` 静态方法：它可将多个可迭代对象按位置“拉链式”聚合，生成一个逐项产出数组的新迭代器；同时说明了语法、参数、`mode` 与 `padding` 行为、常见示例、字符串处理方式及浏览器兼容性限制。

- 📌 `Iterator.zip()` 用于聚合多个可迭代对象，每次产出一个数组，包含各输入在同一位置的元素，效果类似“转置”。
- 🧩 类似方法 `Iterator.zipKeyed()` 也会聚合多个输入，但产出的是可指定键的对象而非数组。
- 🛠️ 语法为 `Iterator.zip(iterables)` 或 `Iterator.zip(iterables, options)`。
- 📚 `iterables` 必须是可迭代对象而不是迭代器；外层应有限，但其中的元素可以是无限迭代器；字符串会被拒绝，需先用 `Iterator.from()` 转为迭代器。
- ⚙️ `options.mode` 支持 `"shortest"`（默认，最短输入结束时停止并关闭其他迭代器）、`"longest"`（全部结束后继续，用填充值补齐）、`"strict"`（若输入未同时结束则抛出 `TypeError`）。
- 🧷 `padding` 仅在 `mode: "longest"` 时使用，必须是可迭代对象而非迭代器；调用 `Iterator.zip()` 时就会读取并校验，按索引为较短输入补齐，不足处用 `undefined`。
- 📦 返回值是一个新的 `Iterator`，每个元素为长度等于输入数量的数组；若输入为空，则返回已完成的迭代器。
- 🗺️ 示例包括：结合无限计数器给 `Map` 元素加索引、用键数组和值数组创建 `Map`、并行处理多个数据源。
- 🧮 处理长度不齐的输入时，可配合 `mode: "longest"` 和 `padding` 为缺失项提供占位值。
- 🔤 字符串不能直接传入；可用 `Iterator.from()` 显式转换，若需按字素簇拆分，可使用 `Intl.Segmenter`。
- 🌐 该特性目前“可用性有限”，并非 Baseline，因为部分主流浏览器尚不支持；可通过 `core-js` 或 `es-shims` 的 polyfill 增强兼容性。

---

### [GitHub - tc39/proposal-defer-import-eval：一项引入延迟模块求值方式的提案 · GitHub](https://github.com/tc39/proposal-defer-import-eval)

**原文标题**: [GitHub - tc39/proposal-defer-import-eval: A proposal for introducing a way to defer evaluate of a module · GitHub](https://github.com/tc39/proposal-defer-import-eval)

该提案是 TC39 Stage 3 的 `import defer`（曾称“Lazy Module Initialization”），旨在延迟模块的同步求值：模块及依赖会先被完整加载并进入可执行状态，但只有在访问其命名空间属性时才同步执行，从而减少大型 JS 应用初始化时的 CPU 开销，同时避免像动态 `import()` 那样强制异步化。

- 🚀 **提案状态**：`proposal-defer-import-eval` 已进入 Stage 3，目标是为 ES 模块引入“延迟求值”能力。
- 📦 **核心语法**：使用 `import defer * as ns from "mod";`，只返回模块命名空间 exotic object，不立即执行模块。
- ⚡ **执行时机**：模块图会提前加载完成，但访问命名空间属性时才触发同步求值；类似代理式 `[[Get]]` 行为。
- 🧩 **解决的问题**：动态 `import()` 虽可懒加载，但不能很好解决同步求值延迟问题，还会迫使调用方改为异步模型。
- 🔄 **顶层 await 限制**：`import defer` 的属性访问必须同步，因此含顶层 await 的模块及其异步依赖会被提前求值，只有同步部分可延迟。
- ⚠️ **与 `import *` 不同**：延迟命名空间若模块求值抛错，属性访问会持续抛出该错误；普通已求值命名空间不会在属性访问时重新抛错。
- 🧪 **暂未包含**：延迟 re-export 等扩展仍在考虑中，当前版本未纳入。
- 🛠️ **实现与工具**：已有 engine262、webpack、Babel 插件等相关实现或支持。
- ❓ **为何不用 import attributes**：`import defer` 改变命名空间对象行为，属于模块加载“阶段”修饰符，不能用 `with { defer: true }` 这类属性表达。
- 🎯 **价值**：在不破坏现有 API 消费方式的前提下，减少初始化阶段不必要的同步执行工作，释放主事件循环。

---

### [GitHub - tc39/proposal-immutable-arraybuffer：一个关于不可变 ArrayBuffer 的 TC39 提案 · GitHub](https://github.com/tc39/proposal-immutable-arraybuffer)

**原文标题**: [GitHub - tc39/proposal-immutable-arraybuffer: A TC39 proposal for immutable ArrayBuffers · GitHub](https://github.com/tc39/proposal-immutable-arraybuffer)

该仓库介绍 TC39 的 Immutable ArrayBuffer 提案，目标是为 JavaScript 增加不可变 ArrayBuffer，使其内容不能被修改、调整大小或分离，并让基于它的 DataView/TypedArray 可以被冻结，从而支持 ROM 存储、零拷贝性能优化和 OCapN 等场景。

- 📦 **提案状态**：当前为 TC39 Stage 2.7，提案者为 Mark S. Miller、Peter Hoddie、Richard Gibson、Jack-Works，规范地址为 tc39.es/proposal-immutable-arraybuffer。
- 🧱 **背景**：现有 ArrayBuffer 已有 transfer、transferToFixedLength、resize、slice 及 detached/resizable/byteLength/maxByteLength 等能力，但都不能创建不可变缓冲区。
- 🔒 **核心问题**：TypedArray 是底层缓冲区的视图，若底层内容可变，TypedArray 就无法被真正冻结；不可变 ArrayBuffer 可解决这一点。
- 🎯 **动机一**：Moddable XS 等嵌入式 JavaScript 实现需要把大量固定数据放入 ROM，而 ROM 通常比 RAM 更充足、更便宜。
- ⚡ **动机二**：接收 ArrayBuffer 的 API 在输入不可变时可避免防御性拷贝，从而提升性能。
- 🌐 **动机三**：OCapN 将字符串和字节数组视为按拷贝传输的批量数据；不可变 ArrayBuffer 可为 JavaScript 提供对应的不可变二进制容器。
- 🛠️ **新增 API**：增加只读属性 immutable: boolean，以及 transferToImmutable(newByteLength?) 和 sliceToImmutable(start?, end?) 两个方法。
- 🚫 **不可变语义**：不可变缓冲区不能被分离、调整大小或再次转移；其 maxByteLength 等于 byteLength。
- 🧊 **可冻结视图**：以不可变 ArrayBuffer 为底层存储的 DataView 或 TypedArray 可以被冻结并保持不可变，因此有望放入 ROM。
- 📋 **复制与克隆**：slice 及 filter、map、slice、toReversed 等 TypedArray 方法不保证保留不可变性；structuredClone 不可转移不可变缓冲区，但克隆会保留不可变性和底层数据。
- 💡 **用例示例**：可将二进制数据封装为 netstring，并通过 transferToImmutable 生成由冻结 Uint8Array 支持的不可变数据。
- 🧪 **实现情况**：已有 endo immutable-arraybuffer 作为 polyfill/转译实现；JavaScriptCore、SpiderMonkey、XS、V8 等原生实现跟踪 issue 尚待补充。
- ❓ **设计问答**：不可变缓冲区不能分离/转移，否则会对视图产生可观察变化；TypedArray 索引属性仍不应单独可配置或可写；sliceToImmutable 允许但不强制零拷贝；新 getter 命名为 immutable；在无其他决定因素时更倾向抛出错误而非静默失败。

---

### [依赖项：由 joyeecheung 将 v8 更新至 15.6](https://github.com/nodejs/node/pull/66601)

**原文标题**: [deps: update v8 to 15.6 by joyeecheung · Pull Request #66601 · nodejs/node · GitHub](https://github.com/nodejs/node/pull/66601)

概述：Node.js 主仓库的 PR #66601 将 V8 升级至 15.6.75.13，为 Node.js 27 做准备，涉及 ABI/模块版本、Rust 依赖、多平台编译修复及多项 V8 cherry-pick，最终已合入。

- 🚀 由 Joyee Cheung 发起，目标是将 V8 从 14.6 更新到 15.6，包含 13 个提交，并标记为 semver-major。
- 🧩 核心变更包括升级 V8 至 15.6.75.13、同步更新 Rust crates、将 embedder string 重置为“-node.0”。
- 🔢 由于 V8 大版本通常存在 API/ABI 不兼容，NODE_MODULE_VERSION 更新为 153。
- 🛠️ 包含多个 V8 cherry-pick，用于修复 illumos 的 madvise/sandbox、MSVC ABI/STL、GCC 16 arm64 编译、Torque 对象布局断言等问题。
- 🧪 CI 与 Codecov 通过，覆盖率约 90.48%；Loong64 测试确认修复 #66633 的构建失败。
- ✅ 获得 Richard Lau、Filip Skokan、Chengzhong Wu 等审核批准。
- ⚠️ Commit Queue 曾因两个提交缺少 Signed-off-by 失败，后经手动修正并成功合入。
- 📦 该更新已进入 Node.js 27.0.0-alpha 版本说明，属于破坏性更新的一部分。

---

### [文件系统 | Node.js v27.0.0 文档](https://nodejs.org/docs/v27.0.0-alpha.0.0.0/api/fs.html#fsglobpattern-options-callback)

**原文标题**: [File system | Node.js v27.0.0 Documentation](https://nodejs.org/docs/v27.0.0-alpha.0.0.0/api/fs.html#fsglobpattern-options-callback)

概述总结
- 📁 `node:fs` 是 Node.js 稳定版文件系统模块，以 POSIX 函数为模型，支持 CommonJS 与 ESM。
- 🔀 所有文件系统操作通常提供同步、回调、Promise 三种形式；Promise API 从 `node:fs/promises` 导入，回调/同步 API 从 `node:fs` 导入。
- ⚡ 回调 API 在需要最大性能时优于 Promise API；Promise 和回调操作使用底层线程池，非同步、非线程安全，并发修改同一文件需谨慎。
- 🧱 同步 API 会阻塞事件循环，异常立即抛出，可用 `try...catch` 处理。
- 📦 Promise API 自 v10 起提供，核心对象 `FileHandle` 封装文件描述符；应显式调用 `close()`，不要依赖自动关闭警告机制。
- 🛠️ `FileHandle` 支持 `appendFile`、`chmod`、`chown`、`close`、`createReadStream`、`createWriteStream`、`read`、`readFile`、`readLines`、`readv`、`stat`、`truncate`、`utimes`、`write`、`writeFile`、`writev` 等；实验性 `pull`、`pullSync`、`writer` 需启用 `--experimental-stream-iter`。
- 📚 `fsPromises` 提供 `access`、`appendFile`、`chmod`、`chown`、`copyFile`、`cp`、`glob`、`link`、`lstat`、`mkdir`、`mkdtemp`、`mkstemp`、`open`、`opendir`、`readdir`、`readFile`、`readlink`、`realpath`、`rename`、`rm`、`stat`、`statfs`、`symlink`、`truncate`、`unlink`、`utimes`、`watch`、`writeFile` 等方法。
- ⚠️ `fsPromises.lchmod` 已弃用；`rmdir` 已移除 `recursive` 选项，递归删除应使用 `rm({ recursive: true, force: true })`。
- 🔁 回调 API 异步执行并在完成后调用回调；`fs.exists` 已弃用，建议使用 `stat` 或 `access`；避免先检查可访问性再打开文件造成竞态。
- 🧊 同步 API 阻塞直到操作完成；`existsSync` 未弃用；各异步操作通常都有对应的 `...Sync` 版本。
- 🧩 公共对象包括 `fs.Dir`、`fs.Dirent`、`fs.FSWatcher`、`fs.StatWatcher`、`fs.ReadStream`、`fs.WriteStream`、`fs.Stats`、`fs.StatFs`、实验性 `fs.Utf8Stream` 以及 `fs.constants`。
- 🧭 异步回调/Promise 操作没有保证顺序，需通过 `await` 或嵌套回调确保先后关系。
- 🛤️ 路径支持字符串、`Buffer` 和 `file:` URL；Windows 下 URL、驱动器盘符、UNC 路径和编码斜杠有特殊限制。
- 🌐 glob 模式采用 bash/minimatch 风格，支持 `*`、`?`、`[]`、`**`、extglob、花括号展开；默认不匹配点文件，大小写敏感性取决于平台/文件系统。
- 📌 文件描述符和 `FileHandle` 必须及时关闭以避免泄漏；文件操作使用 libuv 线程池，可通过 `UV_THREADPOOL_SIZE` 调整；文件打开标志包括 `a`、`a+`、`r`、`r+`、`w`、`w+`、`x` 等及 `fs.constants` 数值常量。

---

### [Net | Node.js v27.0.0 文档](https://nodejs.org/docs/v27.0.0-alpha.0.0.0/api/net.html#netpromises-api)

**原文标题**: [Net | Node.js v27.0.0 Documentation](https://nodejs.org/docs/v27.0.0-alpha.0.0.0/api/net.html#netpromises-api)

Node.js 的 `node:net` 模块提供异步、基于流的 TCP 与 IPC 网络能力，用于创建服务器和客户端，并涵盖地址控制、IP 黑名单、Socket 生命周期管理及实验性 Promise API；文档对应 Node.js v27.0.0，`net` 为稳定级别 2。

- 📡 核心 API：`net.createServer()` 创建 TCP/IPC 服务器，`net.createConnection()`/`net.connect()` 创建客户端并返回 `net.Socket`。
- 🧩 IPC 支持：Windows 使用命名管道，其他系统使用 Unix 域套接字；Unix 路径长度有限制，Linux 可用 `\0` 抽象命名空间，Windows 管道不持久。
- 🛡️ `net.BlockList`：可按 IP、地址范围、子网/CIDR 限制入站或出站访问，支持检查、增删规则、JSON 导入导出及 `PRIVATE_RANGES`。
- 📍 `net.SocketAddress`：表示 IPv4/IPv6 地址、端口、family、flowlabel，并提供 `parse()` 解析带端口的地址字符串。
- 🖥️ `net.Server`：基于事件，关键事件包括 `close`、`connection`、`error`、`listening`、`drop`；`listen()` 支持端口、路径、handle 和 options。
- 🔌 `net.Socket`：TCP/IPC 端点，继承 `stream.Duplex`；支持连接、写入、结束、暂停、恢复、销毁，事件包括 `connect`、`data`、`end`、`error`、`timeout` 等。
- ⚙️ Socket 配置：支持 keep-alive、Nagle 算法开关、超时、TOS、编码设置及地址/端口/状态查询；需注意背压和 `data` 事件监听。
- 🧵 线程转移：监听中的 `net.Server`、已连接 TCP `net.Socket`、未采用的 TCP `BoundSocket` 可通过 `worker_threads` 转移；管道绑定不可转移。
- 🔒 `net.BoundSocket`：可同步预绑定 TCP 端口或 Unix/Windows 管道路径，供 `server.listen()` 或 `new net.Socket()` 采用，采用后所有权转移。
- 🌐 地址族自动选择：`autoSelectFamily` 默认开启，会尝试多个 IPv6/IPv4 地址；可通过 `net.get/setDefaultAutoSelectFamily` 及超时设置调整。
- ✅ IP 工具：`net.isIP()` 返回 `0/4/6`，`net.isIPv4()`/`net.isIPv6()` 校验地址格式，并支持 IPv4-mapped IPv6 地址。
- ⏳ `net/promises`：实验性 Promise API，提供 `connect()` 与 `listen()`，可用 `await` 建立连接或启动服务器。

---

### [命令行 API | Node.js v27.0.0 文档](https://nodejs.org/docs/v27.0.0-alpha.0.0.0/api/cli.html#--allow-env)

**原文标题**: [Command-line API | Node.js v27.0.0 Documentation](https://nodejs.org/docs/v27.0.0-alpha.0.0.0/api/cli.html#--allow-env)

该文档是 Node.js v27.0.0 的命令行 API 参考，系统说明启动语法、程序入口解析、CLI 与 V8 选项、环境变量，以及权限模型、调试与性能诊断、测试/基准运行器、监听模式、快照和单可执行文件等能力。

- 🚀 启动语法：`node [options] [V8 options] [入口 | -e "script" | -] [--] [args]`；无参数进入 REPL，`node inspect` 用于调试。
- 🧭 入口解析：入口按 `require()` 规则解析；在 `--import`、`.mjs/.mts/.wasm`、`"type":"module"` 等情况下按 ESM 加载。
- ⚙️ 选项规则：CLI 选项可用 `-` 或 `_`；重复的单值选项以最后一次为准；命令行选项优先于 `NODE_OPTIONS`。
- 🔐 权限模型：`--permission` 限制文件系统、网络、环境变量、子进程、Worker、WASI、原生插件、FFI、Inspector 和 OpenSSL STORE；配合 `--allow-*` 授权，`--permission-audit` 可仅审计不拒绝。
- 🐞 调试与诊断：支持 `--inspect*`、CPU/Heap Profiler、堆快照、诊断报告、trace events、警告重定向；将 Inspector 绑定到公网地址存在远程代码执行风险。
- 🧪 测试与基准：`--test` 提供测试运行器、覆盖率、并发/隔离、随机化、分片、快照更新等；`--bench*` 提供实验性基准运行器。
- 👀 监听与执行：`--watch`、`--watch-path` 自动重启；`--run` 从 `package.json` 执行脚本；`--env-file` 可加载环境变量文件。
- 📦 快照/VFS/单文件应用：支持 `--build-snapshot`、`--snapshot-blob`、`--vfs-load`、`--build-sea` 等打包与运行能力。
- 🌐 环境变量：`NODE_OPTIONS`、`NODE_V8_COVERAGE`、`NODE_EXTRA_CA_CERTS`、`NODE_PATH`、`TZ`、`UV_THREADPOOL_SIZE` 等可调整运行时行为。
- 🧠 V8 选项：可传递 `--max-old-space-size`、`--max-semi-space-size`、`--stack-trace-limit`、`--jitless` 等 V8 参数，但 V8 选项无稳定性保证。

---

### [发布 v12.0.0 · npm/cli · GitHub](https://github.com/npm/cli/releases/tag/v12.0.0)

**原文标题**: [Release v12.0.0 · npm/cli · GitHub](https://github.com/npm/cli/releases/tag/v12.0.0)

npm 发布 v12.0.0（2026-07-08），这是一次包含大量破坏性变更的大版本更新，重点涉及 CLI 输出、废弃命令、安装策略、安全默认值和 Node 版本支持。

- ⚠️ `npm view --json` 现在始终返回数组。
- 📦 `npm sbom --sbom-format=cyclonedx` 的 `name` 改为取自各包 `package.json`，根组件和别名依赖的 `name`、`bom-ref`、`purl` 可能变化。
- 🧾 全局安装不再注册 man 手册页，`man npm-install` 失效，但 `npm help install` 不受影响。
- 📄 `npm pkg` 输出不再强制 JSON，便于直接获取单值，非 JSON 输出更接近 `npm view`。
- 🗑️ 移除 `npm shrinkwrap`、`shrinkwrap` 配置别名；`npm-shrinkwrap.json` 不再从项目根或依赖 tarball 加载，需改用 `package-lock.json` 或 `bundleDependencies`。
- 👤 npm registry 移除 Twitter 和 Freenode 资料字段，用户无法再设置或查看这些字段。
- 🔧 不再通过 `whichnode` 解析 node 路径，改用 Node 已设置的 `process.execPath`；依赖 PATH 解析的脚本可能受影响。
- 🧾 `npm pack` 和 `npm publish` 的 `--json` 输出格式已统一。
- 🗑️ 移除 `star`、`stars`、`unstar` 和 `npm adduser` 命令；账户管理改用网站，命令行认证使用 `npm login`。
- 🔐 处理 git 时保留 HTTPS 协议。
- 📝 `npm init` 默认 license 从 `ISC` 改为空字符串，未设置时省略 license 字段。
- 🟢 npm 现在支持 Node `^22.22.2 || ^24.15.0 || >=26.0.0`。
- 🚫 `allow-git` 和 `allow-remote` 默认改为 `none`；需设为 `all` 或 `root` 才能安装 git 或用户提供 tarball URL 的依赖。
- ⚙️ 根 `preinstall` 现在在依赖安装前运行。
- ❗ 未知 CLI 标志、缩写标志和单连字符多字符简写改为抛错；未知 `.npmrc` 配置默认仍警告，可用 `strict-npmrc` 改为报错。
- 🛡️ 依赖生命周期脚本默认被阻止，除非根包 `allowScripts` 策略允许；安装后可运行 `npm install-scripts approve` 记录批准，并用 `npm rebuild` 执行新批准的脚本。
- 🧹 移除 npm 12 和 workspaces 的预发布模式，并升级多个 `@npmcli/*`、`libnpm*` 依赖。

---

### [npm v12 即将到来的破坏性变更 - GitHub 更新日志](https://github.blog/changelog/2026-06-09-upcoming-breaking-changes-for-npm-v12/)

**原文标题**: [Upcoming breaking changes for npm v12 - GitHub Changelog](https://github.blog/changelog/2026-06-09-upcoming-breaking-changes-for-npm-v12/)

npm v12 预计于 2026 年 7 月发布，将对 `npm install` 引入安全相关的默认行为变更；这些变更已在 npm 11.16.0+ 通过警告形式提供，便于提前准备。
- 🛡️ `allowScripts` 默认关闭：`npm install` 不再自动执行依赖的 `preinstall`、`install`、`postinstall` 脚本，除非项目显式允许。
- ⚙️ 原生 `node-gyp` 隐式构建也会被阻止；来自 git、file、link 依赖的 `prepare` 脚本同样会被阻止。
- ✅ 可用 `npm approve-scripts --allow-scripts-pending` 查看待处理脚本，用 `npm approve-scripts` 批准可信包，用 `npm deny-scripts` 阻止其余包，并将生成的允许列表提交到 `package.json`。
- 🔗 `--allow-git` 默认 `none`：不再解析 Git 依赖（直接或传递），除非显式允许；该变更此前已于 2026-02-18 公布，npm 11.10.0+ 可用。
- 🌐 `--allow-remote` 默认 `none`：不再解析远程 URL 依赖，如 https tarball（直接或传递），除非显式允许；npm 11.15.0+ 可用。
- 📁 `--allow-file` 与 `--allow-directory` 的默认值在 v12 中不变。
- 🚀 准备方式：升级到 npm 11.16.0+，运行常规安装并查看警告，批准可信脚本后提交更新的 `package.json`；升级后仅已批准的脚本继续运行，未批准的将停止。
- 📚 更多信息见 `npm approve-scripts`、`npm deny-scripts`、`allow-scripts` 配置文档及社区讨论。

---

### [GitHub - Agent-Field/CodeAF：面向开放模型的开源软件工厂 · GitHub](https://github.com/Agent-Field/CodeAF)

**原文标题**: [GitHub - Agent-Field/CodeAF: Open-Source Software factory for Open Models · GitHub](https://github.com/Agent-Field/CodeAF)

CodeAF 是 AgentField AI 推出的开源编码“软件工厂”，面向开放模型，以更低成本提供接近前沿的编码能力；它以 Go 单二进制运行，用一个窗口统一管理多项目、多会话、子代理、自动化与远程开发机协作，目前为早期预览版（Apache-2.0）。

- 🏭 **定位**：为开放模型打造的编码 harness/软件工厂，强调每个任务都更省钱，并减少在多个终端间切换的成本。
- 🖥️ **单窗口管理**：`home` 汇总机器上的所有项目与会话，可跳转、切换、恢复；每个会话可独立设置审批规则、模型与花费上限。
- 🗣️ **自然语言转任务**：一段话可拆成多个任务，各自在独立仓库副本与分支上运行；通过检查的改动自动落到你的分支，不会直接进 `main`、`dev` 或发布分支。
- 🏗️ **工厂式流程**：自动评估工作量、拆分任务、并行执行、测试结果并合并通过项；只在必要时提问，问题集中到“needs you”。
- 🧰 **子代理专家**：内置 `senior-dev`（编码改动）、`sec`（本地安全审计）、`review`（GitHub PR 审查），以任务形式运行并返回结果。
- 🥇 **基准表现**：在 DeepSWE 的 113 个真实 GitHub issue 上，与九种编码 harness 使用同一模型比较，解决最多且每个已解决 issue 成本最低。
- 🤖 **多模型调度**：每个任务由 `worker`、`planner`、`checker` 等席位组成，默认自动选模型；可用 `/crew` 查看、固定席位、限制开放权重模型或按任务选择更强/更便宜。
- ⚙️ **自动化**：支持提醒、定时任务与监控（如 CI 变红），用自然语言设置；显示运行时间与单次花费上限，错过的任务会在下次打开时补跑一次。
- 🧑‍💻 **无头模式**：`codeaf do "..." --json` 面向 CI、cron、脚本与基准测试，自动计划、执行、检查并输出 JSON 与退出码。
- 🌐 **远程开发**：界面在本地、会话在工作机（如 `devbox`），通过 SSH 使用；断线可重连，手机终端也能加入同一实时会话。
- 📦 **轻量性能**：单个 Go 二进制约 53 MB；RAM 占用、16 个空闲会话、单轮峰值与 50 轮会话恢复速度均显著优于对比项。
- 🔐 **遥测与隐私**：默认发送匿名使用计数（版本、系统、模式、错误、token 计数等），不发送提示词、代码、路径、仓库名、密钥、IP 等；可通过 `/settings`、`CODEAF_TELEMETRY=off` 或 `DO_NOT_TRACK=1` 关闭。

---

### [Node.js —— 从 Node.js 26 到 27（Alpha）值得关注的 V8 变更](https://nodejs.org/en/blog/announcements/notable-v8-changes-from-node-js-26-to-27-alpha)

**原文标题**: [Node.js — Notable V8 changes from Node.js 26 to 27 (Alpha)](https://nodejs.org/en/blog/announcements/notable-v8-changes-from-node-js-26-to-27-alpha)

Node.js 27 Alpha 将 V8 从 14.6 升级到 15.6，带来一批默认启用的 JavaScript 新特性、实验性功能、语义与兼容性变化，以及显著的内存、性能和诊断工具调整。由于处于 Alpha/Current 阶段，可能出现破坏性 V8 变更；影响原生插件 ABI 的变更会提升 NODE_MODULE_VERSION，进入 LTS 后 V8 版本预计保持稳定。

- 🚀 **默认新特性**：新增 `Math.sumPrecise()` 减少浮点累加误差、`Intl.Locale.prototype.variants`，以及迭代器 `join()`、`includes()`、`Iterator.zip()`、`Iterator.zipKeyed()`。
- 🧪 **实验性特性**：新增 `--js-import-bytes`、`--js-regexp-buffer-boundaries`；修复 `import defer`、不可变 ArrayBuffer 等已有实验特性；`text` 导入在 Node.js 中仍由 `--experimental-import-text` 控制。
- 🔢 **Math 变化**：部分 Math 方法改用 LLVM libm，某些输入结果最后一位可能不同；`Math.random()` 直接运行 xorshift128+ 且不再缓存，同一 `--random-seed` 的序列发生变化。
- 🕰️ **Date 变化**：`getTimezoneOffset()` 不再截断为整分钟，历史时区的本地平均时间偏移可返回小数。
- 📊 **数组排序**：大数组的 `Array.prototype.sort()` 改用 PowerSort，排序仍稳定，但比较器调用次数和带副作用比较器的行为可能不同。
- 🧵 **错误栈**：`error.stack` getter 不再沿原型链查找捕获的栈；`new Error`、错误子类和 `Error.captureStackTrace` 不受影响。
- ⚡ **Promise/async 变化**：含顶层 await 的 ESM 求值不再以查找 `constructor`/`Symbol.species` 的方式调用 `Promise.prototype.then()`；`Promise.try` 在返回同 realm 的 Promise 时直接返回该 Promise。
- 🔄 **Atomics 与迭代器**：已阻塞 worker 上再次 `Atomics.wait()` 会抛 TypeError 而非崩溃；`notify/wait/waitAsync` 先读取长度再转换索引；`take/drop` 超过 2^53-1 会 RangeError 并关闭迭代器；`asyncDispose` 调用 `return()` 时不传参数。
- 📦 **模块与正则**：`new import(...).x` 现在正确抛 SyntaxError；部分模块加载崩溃改为拒绝错误；负向 lookahead/lookbehind 在 `/u`、`/v` 模式下不再匹配代理对内部。
- 🧱 **TypedArray 变化**：`subarray()` 对可调整大小 ArrayBuffer 子类省略第三个 length 参数；`Float16Array` 的 `indexOf/lastIndexOf/includes` 支持负值；不可变缓冲区上负偏移 `set()` 先抛 TypeError。
- 🧩 **语法语义修复**：实例成员后的 static 块中 `await`/`return` 抛 SyntaxError；C 风格 for 初始化器中的 `using` 只释放一次并视为不可变；转义 `get/set` 字段名换行触发 ASI；`delete super[key]` 先检查 this；`new Function` 先检查代码生成策略。
- 🛑 **致命错误处理**：更多 V8 致命错误先交给 Node.js 处理，`--report-on-fatalerror` 可生成诊断报告；极端模板字符串、过多类元素、过大正则等可能改抛 RangeError，但不应依赖此行为。
- 💾 **序列化变化**：`v8.serialize()`、`structuredClone()`、`postMessage` 使用新格式，旧 Node.js 无法反序列化新数据；新版本仍可读旧数据；structuredClone/postMessage 支持大于 4GB 的 TypedArray 和可调整 ArrayBuffer，`v8.serialize()` 仍限 4GB；`cachedDataVersionTag()` 会因 Node.js 补丁变化。
- 🧠 **内存变化**：4–15GB 内存机器默认老生代上限改为物理/ cgroup 内存的一半并限制在 256MB–4GB；Buffer/ArrayBuffer 计入 V8 全局分配限制；字节码按约 3 分钟未使用刷新；每个原生对象约多 16/50 字节，每个 isolate 约多 180KB；最坏 GC 暂停从约 45ms 降至约 10ms；Error 栈帧延迟计算。
- ⚙️ **性能优化**：数组 `flat/copyWithin/fill/join/lastIndexOf/indexOf/sort`、字符串 `split/localeCompare`、对象属性读取、Promise/async、正则首次编译、JSON.parse、BigInt 模除、模块源码扫描、Maglev、Map/Set 迭代和 DataView 内联等均有改进。
- 🔍 **诊断与调试**：堆快照约耗时和体积翻倍，包含内部对象、数值、完整源码及作用域信息，应视为敏感数据；JSON profile 转义和 jitdump 修复；实时编辑被完全移除，`Debugger.setScriptSource` 始终失败；新增 `scopeNumber` 和实验性 `empty` 作用域标志。
- 📡 **Tracing 变化**：由于迁移到 Perfetto 风格宏，多数 V8 trace 事件不再出现在 `--trace-event-categories` 文件中；`--trace-gc` 和 `perf_hooks` 的 gc 条目不受影响；`disabled-by-default-v8.gc` 事件减少，逐步 GC 事件移至 `v8.gc_extra`。
- 🧮 **WebAssembly**：asm.js 不再编译为 Wasm；移除 `WebAssembly.Function`；`--experimental-wasm-<name>` 重命名为 `--wasm-<name>`，移除 lazy validation、async compilation 等旧标志；`memory.copy/fill` 内联带来约 12% 提速，引用类型导出调用约快 2 倍，arm64 默认启用更多 SIMD 优化。
- 🏷️ **标志清理**：大量 `--js-*` 标志被移除，包括 upsert、regexp escape、Promise.try、Error.isError、Base64、显式资源管理、sumPrecise、Intl locale variants 等；矛盾标志处理改为 `--flag-processing-mode` 模式。

---

### [不到一周就不安装：为期 7 天的 npm 冷却期](https://brunoj.com/nothing-installs-at-our-company-until-its-a-week-old/)

**原文标题**: [Nothing Installs Until It's a Week Old: a 7-Day npm Cooldown](https://brunoj.com/nothing-installs-at-our-company-until-its-a-week-old/)

公司通过自建包代理给新发布依赖设置“冷静期”：npm/PyPI 等包发布后 7 天内不进入公司，pub 为 3 天，Maven/Gradle/Go 仅缓存不限龄，CocoaPods、Google Maven、Docker 不走该网关。作者用今年多起供应链劫持事件说明，恶意版本通常几小时内被撤下，但安装可在发布后几十秒内发生，因此一周等待能覆盖高风险窗口；签名和 provenance 也不能证明提交被授权。

- 🧱 网关规则：太新的版本会从版本列表隐藏；锁文件固定到太新版本时下载返回 404；黑名单版本全局 403；下载日志可查“谁装过”。
- ⏱️ 选择代理而非单仓库设置：能覆盖 Dockerfile、同事电脑和自托管 CI，并集中黑名单、日志和多生态配置；Verdaccio 只支持 npm，且其文档称过滤“不是访问控制”。
- 📊 12 天数据：81,710 次下载、14 个账号；6,116 个版本因太新被隐藏；71 次因锁文件固定太新版本被拒；黑名单 0 条。
- 🧩 常见被拒包：vite、rollup、@swc/core、caniuse-lite、electron-to-chromium 等。
- 💥 破坏点：Yarn 1、旧 bun.lockb、uv --frozen、Poetry、pnpm 环境变量、Dependabot/Renovate 冷却期、npm audit 都可能绕过或不感知网关；预发布版本可能被选中；网关宕机会阻断 CI。
- 🚫 局限：只按发布时间判断，不检查包内容；若一周内无人发现，毒版本仍会在第 8 天进入。某分析称 7 天冷却可挡住约 85% 的 npm 劫持；也有 react-native 包 228 天仍为 latest、xz-utils 34 天才被发现的反例。
- ⚙️ 可直接启用各包管理器冷却设置：npm min-release-age、pnpm minimumReleaseAge、Yarn npmMinimalAgeGate、Bun minimumReleaseAge、uv exclude-newer、pip --uploaded-prior-to，以及 Dependabot/Renovate 的 cooldown。
- 🔧 全公司方案使用 git-pkgs/proxy，配置默认 7 天、pub 3 天、黑名单与例外；作者版本中 Maven/Go 不受默认冷却影响。

---

### [2026 年 10 月安全版本发布 · Express.js](https://expressjs.com/en/blog/2026-10-31-security-releases/)

**原文标题**: [October 2026 Security Releases · Express.js](https://expressjs.com/en/blog/2026-10-31-security-releases/)

Express 团队于 2026 年 10 月发布安全更新，修复 body-parser 与 multer 中的两个高危拒绝服务漏洞，并提醒关注 Node.js 内置 Brotli 解码器的上游漏洞；建议尽快升级依赖和 Node.js 运行时。

- 🛡️ **安全更新发布**：body-parser 升级至 2.4.0 / 1.20.9，multer 升级至 2.5.0，修复两个高危拒绝服务漏洞。
- ⚠️ **body-parser 漏洞 CVE-2026-111181**：受影响版本为 >=2.0.0, <2.4.0 和 <1.20.9；压缩请求体后附带尾随字节可触发未捕获异常并导致进程崩溃。
- 🚨 **body-parser 风险特征**：单个未认证请求即可触发，无需匹配路由或认证，因为解析发生在路由之前。
- ✅ **body-parser 修复方式**：2.4.0 和 1.20.9 会处理流错误，避免错误继续传播。
- 📤 **multer 漏洞 CVE-2026-113872**：受影响版本为 >=2.0.0, <2.5.0；异步 fileFilter 在请求中止后仍恢复已销毁的解析流，可导致未处理异常并退出进程。
- 🔍 **multer 风险范围**：单个未认证请求即可触发；使用异步 fileFilter 的应用受影响，与存储引擎无关；同步 fileFilter 不受影响。
- ✅ **multer 修复方式**：2.5.0 阻止待处理的异步 fileFilter 在请求销毁后继续操作流。
- 🌐 **Brotli 上游漏洞 CVE-2026-111497**：Node.js 内置的 Brotli 解码器存在越界写漏洞；接受 Brotli 压缩请求体的 Express 应用可能受影响。
- ⬆️ **Brotli 官方建议**：升级到包含修复版 Brotli 解码器的 Node.js 版本，这是根本修复方案。
- 🧩 **临时缓解措施**：若无法升级 Node.js 且不需要 Brotli 请求体，可在所有 body parser 前拒绝非 identity、gzip、deflate 的 Content-Encoding。
- 📦 **升级建议**：运行 `npm update body-parser multer` 更新依赖，并保持 Node.js 运行时为最新安全版本。

---

### [在安装前和安装期间阻止恶意 npm 包 - Vercel](https://vercel.com/changelog/blocking-malicious-npm-packages-before-and-during-installation)

**原文标题**: [Blocking malicious npm packages before and during installation - Vercel](https://vercel.com/changelog/blocking-malicious-npm-packages-before-and-during-installation)

Vercel 在构建的依赖安装前和安装期间新增了对被封禁 npm 包的检查，自动阻止恶意安装脚本运行；这项保护适用于所有套餐的新构建，无需配置。

- 🛡️ 安装前会检查受支持的 lockfile，包括从构建缓存恢复依赖的场景。
- ⏳ 安装期间会阻止受影响公共 npm 包的下载。
- 🚫 检查使用特定包版本封禁清单，通常因恶意软件或安全漏洞而封禁，新规则一般几分钟内生效。
- ✅ 部署前仍会继续检查已安装依赖和函数输出。
- ⚠️ 检测到被封禁依赖时，部署会失败，错误信息会标明包名和版本，并尝试使受影响的构建缓存失效。
- 🔧 处理方式是更新依赖到安全版本、更新 lockfile，然后重新部署。

---

### [发布 v5.12.8 · fastify/fastify · GitHub](https://github.com/fastify/fastify/releases/tag/v5.12.8)

**原文标题**: [Release v5.12.8 · fastify/fastify · GitHub](https://github.com/fastify/fastify/releases/tag/v5.12.8)

Fastify 发布 v5.12.8 安全版本，修复 GHSA-3qgw-9275-xf8w，并回移了 5.x 分支的多项类型、流式响应、路由编译、错误处理、钩子及文档相关修复。

- 🔐 安全修复：包含针对 GHSA-3qgw-9275-xf8w 的修复
- 🧩 类型改进：恢复路由简写钩子的 this 上下文，支持 socket 路径字符串，并为 RouteShorthandOptions 增加 logSerializers
- 📤 响应修复：流结束后再发送 stream trailers；错误 statusCode 限制在 400–599，异常时回退 500
- 🛣️ 新特性：routerOptions.compile 支持 find-my-way 编译器模式
- 🧯 稳定性增强：捕获自定义 content type parser 的同步抛错；getDecorator 中实例 getter 仅求值一次
- 🪝 钩子能力：onClose 钩子支持 disposables
- 📚 文档与测试：重组 Request/Reply 参考文档、澄清 serverless 可观测性、移除不支持 v5 的插件并修复示例语法错误
- 👥 发布信息：由 mcollina 发布，提交签名已验证；贡献者包括 Tony133

---

### [@fastify/http-proxy 存在通过解码路由参数导致前缀逃逸的漏洞 · 安全公告 ·](https://github.com/fastify/fastify-http-proxy/security/advisories/GHSA-h3vp-4jfr-v364)

**原文标题**: [@fastify/http-proxy vulnerable to prefix escape via decoded route parameters · Advisory · fastify/fastify-http-proxy · GitHub](https://github.com/fastify/fastify-http-proxy/security/advisories/GHSA-h3vp-4jfr-v364)

该安全公告披露 @fastify/http-proxy 存在严重前缀逃逸漏洞：URL 解码后的路由参数被直接代入 `rewritePrefix` 而未重新编码，攻击者可构造编码斜杠及 `#`/`?` 绕过固定上游路径限制。受影响版本为 `>=9.0.0,<11.6.6`，修复版本为 `11.6.6`，官方表示无临时缓解措施，应尽快升级。

- 🚨 漏洞编号为 GHSA-h3vp-4jfr-v364 / CVE-2026-120213，严重等级为 Critical，CVSS 评分为 9.1。
- 🎯 受影响包为 `@fastify/http-proxy`，受影响版本 `>=9.0.0,<11.6.6`；已修复版本为 `11.6.6`。
- 🧩 根因是 URL 解码后的路由参数被替换进 `rewritePrefix` 时未重新编码，导致前缀逃逸。
- 🛠️ 攻击者可在参数中使用解码后的 `/` 配合 `#` 或 `?`，注入额外上游路径段并剥离本应强制保留的后缀，且无需使用 `..` 路径遍历。
- 🌐 示例：`/tenants/admin%2fmaster-keys%23/public-avatar` 可被转发为 `GET /admin/master-keys`；`/tenants/admin%2fusers%3ftruncate=/public-avatar` 可被转发为 `GET /admin/users`。
- ⚠️ 风险包括路径限制绕过，并可能根据上游服务情况引发 SSRF 或授权绕过。
- ✅ 修复方式是升级到 `@fastify/http-proxy >= 11.6.6`；官方表示无临时缓解措施。
- 🧾 相关弱点为 CWE-22（路径名限制不当）和 CWE-436（解释冲突）。
- 👥 报告者为 Panelv4，修复开发者为 UlisesGascon 和 mcollina。

---

### [发布 v4.13.16 · honojs/hono · GitHub](https://github.com/honojs/hono/releases/tag/v4.13.16)

**原文标题**: [Release v4.13.16 · honojs/hono · GitHub](https://github.com/honojs/hono/releases/tag/v4.13.16)

Hono 发布 v4.13.16，集中修复多项安全漏洞，涉及 mount 路径绕过、RegExpRouter 通配中间件、表单验证、CSS 转义与 CSRF 检查，并包含一项 JWT 修复；相关用户应尽快升级。

- 🔐 **mount() 路径绕过**：`mount()` 与 `app.mount()` 可转发路径绕过挂载前缀内的中间件；动态前缀如 `/api/:tenant/*`、URL 解析器重归一化导致的 `\`→`/` 与 `..` 折叠均受影响。`/assets*` 和重复参数名现在会抛错（GHSA-4m76-xfj5-7975）。
- 🛡️ **RegExpRouter 通配中间件遗漏**：`RegExpRouter`（含默认 `SmartRouter`）在特定路由模式及含编码行终止符路径上未应用通配中间件；现已与其他路由器一致，可匹配空字符串的自定义模式会抛 `UnsupportedPathError`，并需重新生成 `PreparedRegExpRouter` 数据（GHSA-h7mg-cq63-vhpq）。
- 📝 **validator('form') 验证跳过**：带额外参数（如 `charset`）的 `multipart/form-data` 请求未被识别为表单，导致 `validator('form')` 看到空对象而处理器仍能读取字段（GHSA-4h7h-rv7c-7m2v）。
- 🎨 **css 助手 HTML 注入**：`</style>` 拆分在模板与值之间或两个值之间时未被转义，可能导致 HTML 注入；现在压缩后会转义闭合标签（GHSA-3gg2-335m-rxc6）。
- 🧾 **csrf() 未检查 text/ping**：Chromium `<a ping>` 发送的 `text/ping` POST 未被 `csrf()` 按 `Origin` 与 `Sec-Fetch-Site` 检查（GHSA-46wx-v44x-9hh2）。
- 🔑 **JWT 修复**：拒绝 base64url 字母表外的签名段，以及带 `crit` 的头部（#5597）。
- ⚠️ **升级建议**：依赖路径作用域中间件、默认路由通配中间件、`validator('form')`、`css` 不可信值或 `csrf()` 的用户被强烈建议升级至 v4.13.16。

---

### [发布 v4.6.4 · nuxt/nuxt · GitHub](https://github.com/nuxt/nuxt/releases/tag/v4.6.4)

**原文标题**: [Release v4.6.4 · nuxt/nuxt · GitHub](https://github.com/nuxt/nuxt/releases/tag/v4.6.4)

Nuxt 发布 v4.6.4 安全版本，修复 Nuxt 的 8 个安全公告，并引入 Nitro 2.13.6 修复另外 3 个问题，官方建议尽快升级。该版本还包含若干行为变更、缺陷修复、文档与测试更新。

- 🔐 **安全更新**：v4.6.4 修复 Nuxt 的 8 个安全公告；Nitro 2.13.6 额外修复 3 个问题。
- ⚠️ **生产错误信息收紧**：服务端渲染失败时，错误页和 payload 仅保留通过 `createError` 创建的 `message` 与 `data`，其他细节会被移除。
- 🛡️ **开发服务器 Host 校验**：Webpack 和 Rspack 开发服务器会拒绝异常 `Host` 请求；自定义主机名或隧道需加入 `devServer.allowedHosts`。
- 📁 **workspaceDir 检测调整**：未设置时，仅扩展到显式 workspace root 或最近的 git 仓库。
- 🧊 **Nitro 缓存规则变化**：`cache`、`swr`、`isr` 仅缓存 `GET`/`HEAD` 请求；不再缓存设置 cookie 或 `Cache-Control: private/no-store` 的响应；通配 `proxy`/`redirect` 规则会拒绝超出作用域的目标。
- 🔗 **编码斜杠路由匹配**：路由规则现在可匹配包含编码斜杠的路径，例如 `/api%2Fadmin` 可被 `/api/**` 覆盖。
- 🩹 **关键修复**：升级 `unrouting`/`nitropack`，修复通配路由尾部、双斜杠路径、大小写不敏感路由、island hash 编码、Vite 重定向尾部、开发 CSS 去重与 hydration、TypeScript 类型稳定性等问题。
- 📖 **文档更新**：澄清模板依赖再生成、调整 README 结构、链接 Nuxt DevTools 文档，并警告不要向服务端组件展开不可信对象。
- ✅ **测试与 CI**：更新包体积快照、改进基准测试、跳过 release PR 的不必要检查，并重新启用 CodSpeed。
- ❤️ **贡献者**：Daniel Roe、Max、Sébastien Chopin、saini-25、Baptiste Leproux 等参与贡献。

---

### [跨包注册表的签名与证明 | Andrew Nesbitt](https://nesbitt.io/2026/10/30/signing-and-attestations-across-package-registries.html)

**原文标题**: [Signing and Attestations Across Package Registries | Andrew Nesbitt](https://nesbitt.io/2026/10/30/signing-and-attestations-across-package-registries.html)

本文系统梳理了主流软件包注册表在签名、来源证明（provenance attestation）和可信发布（trusted publishing）上的现状：签名用于把制品字节绑定到密钥，来源证明用于声明制品由何处、如何构建；可信发布则用 CI 的短期 OIDC 身份替代长期 API token。整体看，完整性校验较普遍，但“谁构建了它”的来源验证覆盖不均，且多数客户端默认安装时并不验证证明。

- 🧾 **签名与证明的区别**：签名把制品字节绑定到注册表或作者密钥；来源证明是签名的来源声明，常用 in-toto + Sigstore，SLSA 记录源码仓库、提交和构建工作流，发布证明则记录可信发布者身份。
- 🔑 **可信发布的双刃剑**：用 CI 短期 OIDC 凭证替代长期 token，注册表可获得已验证的工作流身份并更容易生成证明；但工作流一旦被攻破，也能直接发布恶意版本。
- 🐧 **Linux 发行版与语言注册表不同**：Debian/Fedora 在自有构建设施从源码构建并由归档密钥签名，apt/dnf 接受的是发行版构建的包；npm/PyPI 等语言注册表通常接受作者上传的 wheel、gem、crate，注册表签名只能证明字节与上传内容一致，不能证明构建来源。
- 🧨 **Ultralytics 案例**：2024 年 12 月被入侵时，首批恶意版本来自项目发布工作流且带有有效证明；后续用泄露 API token 上传的版本没有证明，证明因此可用于区分上传路径。
- 📦 **npm**：2023 年推出可选 `--provenance`，2025 年可信发布 GA 后默认生成；每个版本存 SLSA v1 和 npm publish 两个 Sigstore bundle；CircleCI 2026 年加入可信发布，但仍限云托管 runner；SlugFest 后过期未验证配置并拒绝 `issue_comment` 触发。
- 🐍 **PyPI**：2023 年加入可信发布并停止 PGP，2024 年 PEP 740 证明 GA；官方 GitHub Action 默认生成 PyPI publish predicate；证明按文件存储于 integrity API，且允许上传后追加，收集器需重新抓取。
- 💎 **RubyGems**：2023 年支持 GitHub Actions 可信发布，2024 年支持 Sigstore 证明；可通过 `gem push --attestation` 上传；2026 年自动证明进入 RubyGems 4.1；旧 X.509 `gem cert` 很少使用，需 `-P` 信任策略才检查。
- ☕ **JSR、Maven Central、NuGet**：JSR 自 2024 年支持 OIDC 发布并自动记录 SLSA 到 Rekor；Maven Central 仍要求 PGP，2025 年起接受可选 `.sigstore.json` 但无效仅警告；NuGet 默认在恢复时校验仓库/作者签名（Windows 和 Linux .NET 8+，macOS 关闭），2025 年加入 GitHub Actions 可信发布。
- 🧪 **conda 生态**：CEP 27 定义 Sigstore 发布证明，CEP 50 规定 `.sigs` sidecar；prefix.dev 自 2025 年生成；conda-forge 不使用签名或可信发布，靠 staging token 和 output check，客户端校验 repodata 中的 SHA-256 与大小；rattler 2026 年提供可选安装时 Sigstore 验证。
- ✅ **默认验证差异明显**：Go 的校验和数据库和 Hackage 的 TUF 索引对元数据签名，因此客户端默认认证哈希；Cargo、Julia Pkg、conda 只通过 TLS 获取未签名元数据中的哈希，能发现损坏但信任注册表；npm/PyPI 的证明验证通常是单独命令或手动步骤。
- 🪪 **身份校验是第二步**：验证证明签名只说明密钥由 Sigstore 认证；还需比对证书中的仓库身份，`gh attestation verify` 需 `--owner`/`--repo`，`pypi-attestations` 需 `--repository`；PEP 751 可在 lockfile 的 `attestation-identities` 中记录预期身份。
- 🗝️ **密钥、校验和与缓存**：npm 自 2023 年用 ECDSA 注册表密钥；Terraform Registry 要求提供商 GPG 签名 `SHA256SUMS` 且 `terraform init` 默认校验；Open VSX 用注册表密钥签名，安装校验取决于编辑器；Hex 用 RSA 并在每次抓取时校验，2026 年推出 Workload Identity；Nix/Guix/Spack 在项目基础设施构建并签名二进制缓存，客户端默认校验。
- 🏗️ **Forge 的角色**：GitHub/GitLab 既是可信发布身份提供方，也存储证明；GitHub artifact attestations 2024 年 GA，公共仓库用 Sigstore 公共实例和 Rekor，私有仓库无透明日志；GitLab SLSA Level 3 仍为实验；Forgejo v15/Gitea 已支持 OIDC ID token，但注册表尚未普遍接受为可信发布者。
- 🛑 **退役与未签名现状**：Anaconda `conda-content-trust` 2026 年 9 月停止支持；Docker Content Trust 2025 年宣布退役，Notary v1 2026 年 12 月 8 日关闭，推荐 cosign/Notation；pub.dev 有 OIDC 发布但无签名/证明；Packagist 无签名和可信发布，计划引入透明日志及 SLSA/Sigstore；CocoaPods 用 git 完整性，2026 年 12 月停止接收新 podspec。
- 📊 **总体结论**：注册表普遍能提供上传字节的签名或哈希完整性，但来源证明覆盖不均；可信发布降低 token 风险，却把信任转移到 CI 工作流；默认安装时验证仍稀缺，供应链安全需要注册表、CI、客户端和身份策略共同改进。

---

### [宣布 Parcel 3 alpha](https://v3.parceljs.org/blog/v3-alpha/)

**原文标题**: [
      Announcing Parcel 3 alpha
    ](https://v3.parceljs.org/blog/v3-alpha/)

Parcel 3 alpha 已发布，核心从零用 Rust 重写为独立原生二进制，不再依赖 Node；官方称其构建速度最高可达 v2 的 100 倍，并带来原生插件、内置常见 Web 语言支持、集中配置、更智能的打包与库构建能力。

- 🚀 **发布信息**：2026-11-04 发布 Parcel 3 首个 alpha，基于 Rust 全面重写，速度最高提升 100 倍。
- ⚡ **性能基准**：冷启动开发构建中，Storybook 快 29 倍、文档站快 108 倍、库构建快 49 倍。
- 🧠 **内存优化**：对应场景内存占用分别减少 5.1 倍、6.6 倍、2.5 倍。
- 🧱 **架构简化**：CLI、开发服务器、转换器、打包器、优化器等全为原生实现，充分利用多核；优先优化冷构建，减少磁盘缓存开销与陈旧缓存问题。
- 📦 **开箱即用**：单个二进制内置 HTML、CSS、JS、TypeScript、SVG、图片优化、RSS/Atom、Web Manifest 等，并新增 Tailwind、React Compiler、MDX、SVG→JSX、glob imports 支持。
- 🛠 **开发体验**：支持受信任 HTTPS、本地证书、改进的 `--open`、内置 bundle 分析器，以及带 HMR 的 `parcel run`。
- 🪶 **体积更小**：Parcel 3 二进制小于 30 MB、零 npm 依赖，约为 Parcel 2 总安装体积 120 MB 的 1/4。
- 🔌 **原生插件**：支持 Rust、Go、Swift 或 C ABI 语言编写动态库插件，并提供 Rust/Go/Swift SDK 与 GitHub Actions 工作流。
- 🧩 **JavaScript 插件**：通过基于 QuickJS 的内嵌运行时支持 JS/TS 插件与宏，部分兼容 Node 常用能力，但无网络访问；高性能场景建议原生插件。
- ⚙️ **集中配置**：插件配置统一到 `.parcelrc`，构建开始时一次性解析，提升可发现性与性能。
- 📉 **更智能打包**：450 页面站点上每页 HTTP 请求减少 64%、传输字节减少 10%；改进 CSS 顺序安全、SVG tree shaking，并移除 scope hoisting。
- 📚 **库构建增强**：自动读取 `package.json#exports`，支持嵌套与多入口包并并行构建；库输出按模块拆分，便于消费方 tree shaking 和代码分割；`.d.ts` 生成暂未支持。
- 🧪 **试用方式**：安装 `parcel@next`，或安装 `@parcel/parcel3` 后用 `parcel3` 与 v2 并存试用；压缩器插件、`.d.ts`、自定义打包器插件、JS 编程 API 等仍在开发中。

---

### [模糊测试器 vs. AI：在 JavaScript 引擎上比较 Fuzzilli 与 BigSleep - Project Zero](https://projectzero.google/2026/10/fuzzing-v-AI.html)

**原文标题**: [
    
      Fuzzers vs. AI: Comparing Fuzzilli and BigSleep on JavaScript Engines - Project Zero
    
  ](https://projectzero.google/2026/10/fuzzing-v-AI.html)

该文由 Project Zero 比较 Google 用于发现 Chrome V8 JavaScript 引擎漏洞的两套自动化系统：生成式 JS 引擎模糊测试器 Fuzzilli 与基于 LLM 的代理式漏洞发现系统 BigSleep。核心结论是二者目前互补而非替代：近半年漏洞发现数量接近，生产环境重叠约 25%，专项实验估计理论重叠约 60%；不同系统各自擅长不同类型漏洞，建议厂商同时部署模糊测试与代理式代码分析。

- 🎯 研究对象：Fuzzilli 持续运行、基于生成式模糊测试；BigSleep 每日运行、基于 LLM 阅读代码并编写 PoC；二者均通过 Clusterfuzz 上报 V8 缺陷。
- 📈 生产数据：2026 年 4—9 月原始报告 BigSleep 441 条、Fuzzilli 316 条；仅看 vulnerability 为 95 对 178；再去重并限定“可操作 Type-Vuln”后为 45 对 37，BigSleep 略多。
- 🔁 生产重叠：可操作漏洞报告重叠约 25%（20/81），其中略多数由 Fuzzilli 先发现、BigSleep 后报告。
- 🧪 复现实验：用 BigSleep 重发现 112 个历史 Fuzzilli 漏洞，约 62% 成功复现原漏洞，另约 12% 发现其他已修复漏洞，约 26% 未发现；调整提示与起点后正确率约 70%、任意漏洞发现率约 84%。
- 🧠 记忆化风险：所用 Gemini 3.6 flash 知识截止约 2026 年 3 月，未发现统计显著的事先记忆效应，但建议未来模型继续评估。
- 🧗 难度分布：对 fuzzer 很困难的漏洞，对 AI agent 往往也困难，因此“简单漏洞”重叠更高；JIT 编译器组件重叠较低，引擎其他部分重叠较高。
- 🤖 BigSleep 优势：擅长需要复杂逻辑推理与实验才能触发的漏洞、需要特殊“魔法值”的漏洞、新/少见语言特性、非标准 harness/特殊 flag 的漏洞。
- 🧰 Fuzzilli 优势：能发现部分“非局部”但组合不太复杂的漏洞；擅长源码推理难发现的编译器优化/死代码类问题；不受提示词和起点偏差影响；不易被浅层漏洞分散注意力。
- 🐞 典型案例：BigSleep 发现 TDZ hole-check 消除与 labeled break/switch 组合漏洞、异常处理器偏移 28 位截断配超大 bytecode 漏洞；Fuzzilli 发现 Maglev 中 CheckedSmiUntag 与 UnsafeSmiUntag 优化冲突漏洞。
- 💰 成本问题：现阶段难以公平比较两系统成本/漏洞，二者均未针对最优 cost-per-bug 校准。
- ✅ 结论建议：fuzzing 与 LLM 仍高度互补；厂商应同时进行模糊测试和代理式代码分析，以最大化漏洞在上线前被发现的数量；未来模型进步可能提升 agentic 系统占比，但暂不应停掉专用 fuzzer。

---

### [smoores.dev - 不，npm，“estee”并不是“testem”的拼写错误](https://smoores.dev/post/no_npm_estee_is_not_a_typo/)

**原文标题**: [smoores.dev - No, npm, “estee” is not a typo of “testem”](https://smoores.dev/post/no_npm_estee_is_not_a_typo/)

作者因 Storyteller 项目的 npm 命名空间过长，想用昵称“estee”发布 CLI 包，却被 npm 以“与 espree、testem 过于相似”为由拒绝；文章借此批评 npm 基于 Levenshtein 距离的 typosquatting 防护规则过于粗暴，尤其严重压缩了短包名的可用空间，并质疑其申诉与人工豁免机制不够透明有效。

- 😅 Storyteller 的正式包名是 `@storyteller-platform/align`，作者想用更可爱的昵称“estee”作为短 CLI 包名。
- 🚫 发布 `estee` v0.0.1 时收到 403 错误，npm 称其与现有包 `espree`、`testem` 太相似。
- 📏 npm 使用 Levenshtein 距离判断 typosquatting，距离不超过 2 就可能被拦截；从“estee”到“testem”确实只需 2 次编辑。
- 📉 这种规则对短包名影响极大：4 字符包名理论上有 707,281 种，但按距离 2 拦截后可用空间可能只剩极小比例。
- 😵 备用名“hoid”也被列出可能“混淆”的包：hoek、hono、uid、ulid、cuid、uuid、joi、gopd、poi、zod，但多数并不像真实拼写错误。
- ⚠️ 作者认为规则过宽，甚至会阻止 `preact` 因 `react` 存在而创建，或阻止 `estree` 因 `espree` 存在而创建。
- 📧 npm 客服表示无法绕过自动 typosquat 拦截，但引用的博客文章讲的是标点差异规则，与本次情况不符。
- 🔧 作者怀疑 npm/GitHub 内部后台可以手动绕过该限制，并提到此前 `audiobook` 被禁时客服曾迅速帮助解决。
- 🙂 最终作者可能改用“estie”作为 CLI 名，虽不够有趣但能避开相似性检测。
- 😔 作者遗憾地指出，如今 1—4 字符的 npm 包名可能因这类笨拙但或许必要的安全规则而几乎无法再创建。

---

### [下一代开源维基 — Wiki.js](https://js.wiki/)

**原文标题**: [Next Generation Open Source Wiki â Wiki.js](https://js.wiki/)

Wiki.js 3.0 是新一代开源、自托管 Wiki，基于 Node.js 与 PostgreSQL，面向从个人项目到数千人协作的场景，强调高速、可扩展与数据自主，并支持 Docker、Kubernetes、裸机及云平台部署。

- 🚀 **版本定位**：Wiki.js 3.0 已发布，定位为可从周末小项目扩展到数千贡献者的开源 Wiki。
- ✍️ **Markdown 写作**：提供类似 VS Code 的编辑器，支持实时分屏预览、语法高亮、自动补全和表格等。
- 🧩 **多种编辑方式**：除 Markdown 外，还支持可视化编辑器、AsciiDoc、实时笔记、Excalidraw、博客和反馈板。
- 📊 **图表与数学**：支持 Mermaid、PlantUML、Kroki、LaTeX 数学公式，以及 180+ 语言语法高亮。
- 👥 **实时协作**：Live Notes 支持多人同时编辑同一文档，读者也可实时观看内容成形。
- 💬 **评论与审阅**：支持页面评论、段落批注、只读成员提议修改，以及审阅者批准或拒绝。
- 🔔 **通知与集成**：可关注页面、@提及成员、自定义通知，并通过 Webhook 推送事件到外部服务。
- 🗂️ **文件管理**：页面与资源统一管理，支持上传、文件夹、移动、重命名、删除和拖拽操作。
- 🔎 **内置搜索**：由 PostgreSQL 提供全文搜索、布尔搜索和标签过滤，无需额外搜索服务。
- 🌐 **多站点与多语言**：单实例可托管多个独立 Wiki，支持多域名、多语言以及本地化路由。
- 🔄 **Git 与云同步**：内容保持纯 Markdown，支持双向 Git 同步及 S3、Azure、GCP、SFTP 等备份。
- 🔐 **身份认证**：支持 OIDC、LDAP、SAML 2.0 和本地账户，并可在登录时映射用户组。
- 🛡️ **精细权限**：可按站点、路径、语言和用户组授予、拒绝或继承读写与管理权限。
- 🤖 **AI 可选接入**：MCP 服务器默认关闭，开启后 AI 代理只能在连接者权限范围内搜索、阅读和提议修改。
- 🕓 **版本与审计**：每次编辑均有差异记录、归属信息和一键恢复，并支持完整审计日志。
- 🔌 **REST API**：UI 中的每个操作都有对应 REST 端点，并提供 OpenAPI 文档，便于集成自动化。
- 📦 **部署灵活**：支持 Docker/Compose、Kubernetes Helm、Linux/macOS/Windows 裸机及一键云模板。
- 🆓 **开源免费**：采用 AGPL 许可，免费使用，由社区公开构建，适合长期自主掌控知识库。

---

### [GitHub - requarks/wiki：Wiki.js | 下一代开源 Wiki · GitHub](https://github.com/Requarks/wiki)

**原文标题**: [GitHub - requarks/wiki: Wiki.js | Next Generation Open Source Wiki · GitHub](https://github.com/Requarks/wiki)

requarks/wiki 是 Wiki.js 的 GitHub 仓库，定位为“下一代开源 Wiki”，采用 AGPL-3.0 许可证，在开源社区中关注度很高，并提供文档、安装、更新日志、功能请求、Discord 交流及赞助支持等资源。

- 🌐 项目定位：Wiki.js 是一个跨平台、开源、基于 Node.js 的 Wiki 系统，支持 Git、Markdown 等技术主题。
- ⭐ 社区热度：仓库获得约 29.2k Stars、3.3k Forks、313 Watchers，显示较高关注度。
- 📦 仓库活跃度：共有 2,526 次提交，当前有 7 个 Issues、2 个 Pull Requests。
- 📜 开源许可：项目采用 AGPL-3.0 许可证，并提供行为准则、贡献指南和安全政策。
- 🧩 主要目录：包含 backend、frontend、blocks、dev 等核心代码与开发相关文件夹。
- 📚 官方资源：README 提供官方网站、文档、安装说明、更新日志和功能请求入口。
- 💬 社区与本地化：可通过 Discord 交流，并参与翻译贡献；项目方明确表示需要翻译帮助。
- 💰 赞助支持：可通过 GitHub Sponsors、OpenCollective、Patreon、Paypal 等方式赞助，并列出 Gold Tier Sponsors。
- 🙏 特别致谢：BrowserStack、Cloudflare、Icons8、CrowdIn、Porkbun、ProductBridge 等为项目提供测试、CDN、图标、本地化、域名和反馈工具支持。

---

### [日志与指标：何时统计日志就足够了 | Sentry 博客](https://blog.sentry.io/when-you-need-a-metric/?utm_source=nodeweekly&utm_medium=paid-community&utm_campaign=observability-fy27q4-evergreen&utm_content=newsletter-sponsored-link-blog-log-metric-learnmore)

**原文标题**: [Logs vs. metrics: when counting your logs is enough | Sentry Blog](https://blog.sentry.io/when-you-need-a-metric/?utm_source=nodeweekly&utm_medium=paid-community&utm_campaign=observability-fy27q4-evergreen&utm_content=newsletter-sponsored-link-blog-log-metric-learnmore)

日志与指标解决的是不同问题：日志记录事件发生时的状态，用于调试和事后重建现场；指标是预先定义、持续跟踪的数字问题，用于趋势、漏斗和告警。Sentry 将二者与追踪、错误和发布关联，并建议只发送调试所需的应用日志，以及真正会查看的少量指标。

- 📝 日志回答“当时发生了什么”：在代码决策点记录状态、严重级别、消息和属性，便于还原单个用户经历或失败原因。
- 📊 指标回答“预先决定要问的问题”：命名后用于仪表盘、告警、趋势和漏斗，即使系统正常也会主动查看。
- 🔍 追踪自动回答“耗时与去向”，但会被采样；日志和指标不采样，更适合精确计数和保留关键上下文。
- 🧭 选择准则：调试时想计数，可以数已有日志；如果某个数字需要长期跟踪，就直接发送指标。
- 👤 注册示例：在作用域设置 `user.id`、`signup.method`、`plan` 等共享属性，自动附加到错误、日志和指标。
- 🧮 计数器适合“发生多少次”，如 `user.signup`、`email.verified`、`project.created`，可构建注册漏斗并按 `plan` 或发布版本分组。
- 📈 仪表记录当前值，如邮件队列深度；分布记录“多少/多长时间”并保留单位，如验证邮箱耗时，用于均值与百分位分析。
- 🚫 不要为计数而记录一切：访问日志、基础设施日志、合规归档、CPU/内存图和 debug 噪音应留在原处。
- ✂️ 用 `beforeSendLog` 或 Pino 集成在 SDK 过滤，只转发调试所需级别；Sentry 计划每月包含 5 GB 日志和 5 GB 应用指标。
- 🏷️ 实践：日志和指标使用同一事件名与属性键；在顶部设置 `setUser()` 和共享属性；谨慎发送 PII；给 gauge/distribution 加单位；不要把唯一数据只放在 span 上。
- 🚀 入门：日志在 SDK v10.71.0 默认开启，旧版需设置 `enableLogs: true`；可用 Sentry agent 插件协助应用日志与指标模式并识别哪些日志应改为指标。

---

### [发布 v4.0.0 · porsager/postgres · GitHub](https://github.com/porsager/postgres/releases/tag/v4.0.0)

**原文标题**: [Release v4.0.0 · porsager/postgres · GitHub](https://github.com/porsager/postgres/releases/tag/v4.0.0)

Postgres.js v4.0.0 是一次底层重大重写：连接池、连接、协议、启动流程和 socket 层全部重写，查询、事务、游标、COPY、listen、subscribe、大对象与选项大体延续 3.4.9 的行为，但默认参数类型推断、运行时支持、事务/连接语义、性能与安全性均有明显变化，并修复了大量正确性问题。

- 🔐 安全修复：连接参数中的 NUL 字符不再能注入额外启动参数；查询文本、标识符等协议字符串含 NUL 会拒绝为 `NUL_CHARACTER`；名为 `__proto__` 的列作为自有属性处理，避免原型污染。
- ⬆️ 升级重点：默认改为服务器推断参数类型（`infer: false`），`Date`、布尔、`Buffer`、`bigint` 等不再由客户端强制类型；`infer: true` 保留 v3 行为；非 UTC 下写入/比较 `timestamp`/`date` 的 `Date` 按 UTC 处理，必要时需显式 cast。
- 🧩 运行时与模块：支持 Node.js 20+、Bun、Cloudflare Workers，Deno 通过 Node 兼容层；仅提供 ES module，Node 20.19/22.12+ 可用 `require` 加载；移除 `sql.array()`，改用 `${ids}::int[]`。
- 🧾 事务与连接语义更严格：服务器对 `COMMIT` 返回 `ROLLBACK` 时 `sql.begin` 拒绝 `TRANSACTION_ROLLED_BACK`；`release()` 后或事务结束后的查询会拒绝；不安全的 `begin` 拒绝 `UNSAFE_TRANSACTION`；事务内查询构建/序列化失败会中止事务。
- 🔁 连接与错误处理：`53300` 连接过多会按 backoff 重试至 `connect_timeout`；无匹配 `target_session_attrs` 拒绝 `CONNECTION_DESTROYED`；未知认证拒绝 `AUTH_TYPE_NOT_IMPLEMENTED`；`subscribe` 无 `onerror` 时错误写入日志；`infinity` 时间戳映射为 `Infinity`/`-Infinity`。
- 🚀 新调度器：忙时把查询流水线到预计最快完成的连接，慢查询集中处理，快查询 p99 显著下降；`scheduler: false` 改为选择在途查询最少的忙连接；`max: 1` 时关闭。
- ⏱️ 新增控制能力：`queue_timeout`、查询级 `.signal(abortSignal)`、游标取消、`sql.join(items)`、嵌套 `sql.begin` 使用 savepoint、`sql.rollback()` 不抛错、事务内任意位置流水线、自定义类型按名称、`using`/`await using`、`unref_sockets`、`min`/`idle_timeout`、`user` 函数、`PGPASSFILE`、命名参数。
- 📡 复制/订阅增强：支持持久化 replication slot、`truncate` 事件、每次变更的 `lsn`/`time`/`xid`；异步 handler 按提交顺序执行，失败事务会重投，重连带 backoff。
- 🔒 TLS/认证：TLS 上 SCRAM 支持 `SCRAM-SHA-256-PLUS` 通道绑定，`channel_binding` 默认 `prefer`，可 `require`/`disable`；Node 支持 `sslnegotiation: 'direct'` 直连 TLS（PostgreSQL 17+）；Cloudflare Workers 通过 `cloudflare:sockets` 与 `startTls` 工作。
- 🔍 可观测性：新增 `query.text`/`query.parameters`、`sql.stats`、诊断 tracing 通道 `postgres:query`/`connect`/`transaction`，以及普通通道 `postgres:pool`/`notice`；无订阅者时零开销。
- 🧠 预处理语句：列类型变化时会重新准备；参数类型不匹配时先失败，再用新描述重试；每个连接只按自身服务器描述读写。
- 🧰 其他 API 改进：`sql.close()`、命名游标、查询错误堆栈定位到调用行、`options.socket` 获得 host/port、`onread: false`、COPY 行数 `count`/`command`、错误文档化、TypeScript 类型改为 ESM 默认导出与命名类型。
- 🐛 修复 33 个正确性 bug：冷池只开一个连接、错误字段 `data_type_name`、`JSON.stringify(PostgresError)` 包含消息、游标最后批次等待/拒绝、大对象 `end` 生效、Bun/Cloudflare 错误、池化器语句名冲突、TypeScript 类型、helper 子句上下文、连接 URL IPv6/编码 socket/密码、取消后答案错配、连接丢失事务拒绝等。
- ⚡ 性能：已知参数类型时 prepare/describe/run 一次往返；`int2`/`int4`/`oid`/`bool` 直接字节解码；空闲连接直达；每连接单缓冲区；结果形状编译行读取，20 列时每行 CPU 约减半。
- 🧪 测试：单元测试覆盖协议、类型、查询构建和错误；假服务器/假时钟故障模拟；集成套件覆盖 PostgreSQL 14–18 与 Node 20/22/24；CI 还跑 Bun、Deno、Cloudflare Workers 和 TypeScript 类型测试；使用 V8 覆盖率门禁。

---

### [GitHub - porsager/postgres：Postgres.js - 最快的全功能 PostgreSQL 客户端 · GitHub](https://github.com/porsager/postgres#upgrading-from-v3)

**原文标题**: [GitHub - porsager/postgres: Postgres.js - The Fastest full featured PostgreSQL client · GitHub](https://github.com/porsager/postgres#upgrading-from-v3)

Postgres.js 是一个高性能、全功能 PostgreSQL 客户端，核心使用 ES6 标签模板字符串实现安全查询与动态查询构建，无依赖，支持 Node.js 18+、Bun、Cloudflare Workers，并可通过 Node 兼容层运行于 Deno。它提供连接池、事务、游标、流式 COPY、监听通知、逻辑复制订阅、自定义类型、数据转换和 TypeScript 支持，并针对 v4 调整了参数类型由服务端推断的行为。

- 🚀 定位为“最快、全功能”的 PostgreSQL 客户端，仓库约 8.8k stars、404 forks。
- 📦 安装方式为 `npm install postgres`，ES 模块、无依赖，支持 Node.js 18+、Bun、Cloudflare Workers 和 Deno 兼容运行。
- 🧩 查询基于 `sql\`...\`` 标签模板，参数自动序列化并由数据库处理，避免 SQL 注入。
- 🔧 支持动态列选择、动态插入/更新、多行插入、`where in`、条件查询片段、动态排序、表名/列名标识符和函数调用。
- 🏊 连接池按需惰性创建连接，默认最多 10 个连接；支持多主机、高可用、SSL、通道绑定和 PgBouncer 的会话/事务模式。
- 🔄 事务使用 `sql.begin()`，支持 `SAVEPOINT`、嵌套事务转 savepoint、`sql.rollback()`、`PREPARE TRANSACTION` 和批量查询。
- 📤 高级查询能力包括游标、`forEach`、`describe`、`.values()`、`.raw()`、`sql.file()`、简单协议多语句、COPY 流式导入导出和查询取消/超时控制。
- 📡 支持 `LISTEN/NOTIFY` 与基于逻辑复制的实时订阅，可订阅 insert/update/delete/truncate，并支持持久化复制槽。
- 🔤 提供 camelCase、PascalCase、Kebab-Case 等数据转换，支持将 `undefined` 转为 `null`，也可自定义列名、值、行转换函数。
- 🧪 支持自定义 PostgreSQL 类型、`sql.typed`、按 OID 或类型名注册序列化/解析逻辑。
- 🛡️ 错误以 `PostgresError` 和明确错误码暴露，包含 `UNSAFE_TRANSACTION`、`UNDEFINED_VALUE`、`QUERY_TIMEOUT`、`CONNECTION_DESTROYED` 等，便于处理连接、事务和查询问题。
- 🧭 提供 TypeScript 类型支持，可传入行结果类型；v4 主要变化是参数类型由服务端决定，必要时可用 `infer: true` 保持 v3 行为。

---

### [发布 v12.3.0 · nestjs/nest · GitHub](https://github.com/nestjs/nest/releases/tag/v12.3.0)

**原文标题**: [Release v12.3.0 · nestjs/nest · GitHub](https://github.com/nestjs/nest/releases/tag/v12.3.0)

NestJS 发布 v12.3.0（2026-10-27），新增原生 Node.js HTTP 平台适配器，并集中修复核心、通用模块、Express/Fastify、WebSocket 与微服务相关问题。
- 🚀 新功能：`platform-node` 新增原生 Node HTTP 平台适配器。
- 🐛 核心修复：改进中间件执行、版本路由、SSE 请求、请求作用域 forward refs、流式文件中断等行为。
- 🌐 平台适配器：修复 Express/Fastify 的 HTTP 错误映射、CORS 顺序、空流响应、文件描述符监听等问题。
- 🔌 微服务：修复 Redis/NATS/Kafka/TCP/MQTT/RMQ 的重试、连接、消息头与请求响应处理。
- 📦 依赖更新：升级 `multer` v2.5.0（安全）、`file-type` v22.2.0、`@fastify/middie` v9.3.6。
- 👥 社区贡献：16 位提交者参与本次发布，包含多项社区 PR 修复。

---

### [feat(node): add a native node http platform adapter by kamilmysliwiec · Pull Request #18063 · nestjs/nest · GitHub](https://github.com/nestjs/nest/pull/18063)

**原文标题**: [feat(node): add a native node http platform adapter by kamilmysliwiec · Pull Request #18063 · nestjs/nest · GitHub](https://github.com/nestjs/nest/pull/18063)

NestJS 合并 PR #18063，新增 `@nestjs/platform-node` 原生 Node HTTP 适配器，直接基于 `node:http`/`node:https`，提供 Express 风格 API 与中间件兼容性，性能接近 Fastify 且显著优于 Express；该适配器计划从 v12.3 起作为可选方案，并在 v13 成为默认。

- 🚀 **新适配器**：`@nestjs/platform-node` 的 `NodeAdapter` 可直接用于 `NestFactory.create(AppModule, new NodeAdapter())`，`getType()` 返回 `'node'`。
- ⚡ **性能提升**：基准中 Nest + Node 约比 Nest + Fastify 快 5%，比 Nest + Express 快约 50%；`GET /` 达 55.1k req/s，Fastify 为 52.4k，Express 为 37.1k。
- 🔌 **Express 兼容**：请求/响应对象继承 `IncomingMessage`/`ServerResponse`，支持 `res.status/send/json/set/cookie/redirect/sendFile`、`res.locals`、`req.get/header/is` 等常用 API。
- 🧱 **中间件兼容**：中间件运行在 Express 风格栈上；与 21 个流行中间件包及 `@nestjs/passport` 守卫对比结果一致。
- 🛣️ **路由机制**：连续路由合并为 `find-my-way` 查找，保留 `path-to-regexp v8` 语法，无法表达的模式回退到 `path-to-regexp`。
- 📏 **参数限制**：路由参数默认上限 100 字符，可用 `new NodeAdapter({ maxParamLength })` 配置；超长且无其他匹配路由时返回 414。
- 📦 **内置能力**：替换 `body-parser`，内置 json/urlencoded/text/raw 解析器，支持 CORS、HTTPS、静态资源、视图引擎和 multer 文件上传拦截器。
- 🛡️ **代理与安全**：`trustProxy` 支持读取 `X-Forwarded-*` 来设置 `req.ip/ips/protocol/secure/hostname`；body parser 默认拒绝原型污染。
- 🔍 **查询解析**：默认使用 `fast-querystring` 扁平解析；可通过 `querystringParser` 自定义嵌套对象/数组解析。
- ⚠️ **与 Express 的差异**：路由按具体程度匹配而非声明顺序；处理器返回字符串为 `text/plain`；路径大小写敏感；`req.path` 为解码后的匹配路径。
- 🧪 **测试覆盖**：新增单元测试、共享集成测试的 Node 版本，以及 `integration/http-adapters` 套件，对比 Express/Fastify/Node 行为。
- 🐛 **评审修复**：修复了通配符路由、版本/主机过滤回退、视图 `views` 目录、中间件错误透传、二进制响应、大小写匹配等问题。
- 📚 **文档与发布**：文档新增 Node 适配器页面并更新性能页；`@nestjs/serve-static` 和 `@nestjs/apollo` 的 Node 支持将另行发布。
- 🧩 **后续事项**：核心层的重复/遮蔽路由策略需后续处理；部分极端 Express 兼容场景未追求 100% 对齐。

---

### [发布 v31.0.0 · jsdom/jsdom · GitHub](https://github.com/jsdom/jsdom/releases/tag/v31.0.0)

**原文标题**: [Release v31.0.0 · jsdom/jsdom · GitHub](https://github.com/jsdom/jsdom/releases/tag/v31.0.0)

jsdom v31.0.0 已发布，主要变更包括 canvas 后端迁移、CSS 引擎重构、HTML/XML 解析对阻塞脚本的处理调整，以及大量 DOM、脚本、资源加载、焦点和内存相关修复。

- 🎨 **破坏性变更**：可选 canvas 与图像解码后端由 `canvas` 改为 `@napi-rs/canvas`，需安装 v1.0.13 或更高版本；仅安装 `canvas` 不再启用该支持，使用原生 canvas 对象或自定义字体注册的项目需迁移。
- 🖼️ 新增通过 `canvas.toDataURL()` 和 `canvas.toBlob()` 进行 WebP 序列化；修复图像加载等待解码、丢弃过期请求、尺寸变化时重复请求、失败图像绘制旧内容等问题。
- 🧩 修复 canvas 上下文与序列化行为，包括不支持的上下文类型、只读 `ctx.canvas`、绘图异常、MIME 类型与质量归一化，以及空画布或编码失败时 `toBlob()` 异步返回 `null`。
- 🎯 CSS 解析、选择器匹配和计算样式改用新的集成实现，支持级联层、嵌套、`@scope`、自定义属性替换与注册、`@property`、`CSS.registerProperty()`、typed `attr()`、`if()`、Shadow DOM 样式、伪元素计算样式和可构造样式表等，并提升查询与重复样式读取性能。
- 🧷 修复大量 CSS 级联、简写、序列化和默认样式问题；计算声明会随 DOM 与样式表变化保持实时更新，但序列化与计算值可能与旧版本不同。
- ⏸️ HTML/XML 解析会在阻塞脚本所需资源就绪前暂停；`JSDOM`、`JSDOM.fromURL()`、`JSDOM.fromFile()` 可能返回部分解析的文档，应等待 `DOMContentLoaded` 或 window 的 `load` 事件，并先检查 `document.readyState`。
- 🪵 异步解析恢复后遇到的 XML 语法错误会通过虚拟控制台以 `"xml-parsing"` 错误报告。
- 🧰 新增 `window.reportError()`、`element.ariaBrailleLabel` 和 `element.ariaBrailleRoleDescription`。
- 📄 页面完成时的 `load` 事件现在只在 window 上触发；`document.open()` 会清除文档、其后代及 window 上的事件监听器和处理器。
- ✍️ 修复 `document.write()` 的连续写入、嵌套脚本插入点保持、已完成文本立即可见，以及脚本创建的输入流保持打开直到 `document.close()` 等问题。
- ⚙️ 修复动态插入脚本对 `script.async = false` 执行顺序、准备时源文本与文档的使用、被其他文档收养后执行，以及惰性片段解析脚本后续插入时不应执行等问题。
- 🚦 修复无关图像、样式表和框架被脚本延迟，资源完成事件早于嵌套样式表导入完成，循环导入阻止完成，以及 Shadow DOM 中 `<style>` 的 `load` 事件等问题。
- 🛑 修复 `window.stop()` 取消子框架待处理请求并抑制取消加载的完成事件、重复 `document.close()` 重放就绪与加载事件、iframe 加载事件错误，以及 v28.0.0 引入的内存泄漏。
- 🎯 修复元素变为不可聚焦后焦点残留、`element.blur()` 立即释放焦点、`document.hasFocus()` 在聚焦前或聚焦切换期间误报 `false` 等问题。
- 🧾 修复 XML 文档中 `<template>` 解析与 `template.innerHTML` 序列化，以及 `rect.toJSON()`、`performance.toJSON()` 结果对象创建 realm 不正确的问题。
- 👥 贡献者包括 Brooooooklyn、b84330808 等 4 人。

---

### [错误](https://vitest.dev/blog/vitest-5-1)

**原文标题**: [Error](https://vitest.dev/blog/vitest-5-1)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='vitest.dev', port=443): Max retries exceeded with url: /blog/vitest-5-1 (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [Nitro v3 候选发布版来了！ - Nitro](https://nitro.build/blog/v3-rc)

**原文标题**: [Nitro v3 Release Candidate is here! - Nitro](https://nitro.build/blog/v3-rc)

Nitro v3 发布候选版（RC），API 已稳定，距离正式版很近。此次版本包含 240+ 次提交、40+ 位贡献者参与，重点带来运行时模式、统一构建插件、极小安装体积、Vitest 支持、服务器入口配置、自定义环境以及 Vercel/Cloudflare 等平台集成改进，并给出了从 beta 升级的注意事项。

- 🚀 **发布状态**：Nitro v3 RC 已发布，API 稳定，主要新功能已补齐，并清理了旧代码，为 v3 稳定版做准备。
- 📦 **运行时模式**：新增实验性运行时模式，可用 `nitro serve`/`nitro start` 直接从源码启动生产服务器，无需构建；支持 WebSocket、定时任务、静态资源、`.env` 和优雅关闭。
- 🧪 **单次请求工具**：新增 `nitro fetch`/`nitro curl`，从源码启动服务器、发送一次请求并输出响应，适合脚本和 CI 冒烟测试。
- 🧩 **统一构建插件**：新增 `buildPlugins`，使用 Rollup 插件接口，兼容 rollup、rolldown、vite 以及运行时模式。
- 🪶 **安装体积大幅缩小**：仅 6 个直接依赖，安装体积约 4.7 MB、558 个文件；相较 Nitro v2 约小 15 倍，依赖和文件数显著减少。
- 🧪 **Vitest 零配置测试**：在 Vite 配置中添加 `nitro()` 后即可运行 Vitest；测试环境中的路由、插件、运行时配置和 KV 与服务端一致。
- 🔌 **服务器入口选项**：`server.ts` 可通过 `defineServerEntry()` 配置端口、请求体大小、TLS、优雅关闭等；环境变量如 `NITRO_PORT` 仍优先。
- 🏷️ **自定义环境**：新增 `--envName`，可为 `nitro dev/build/serve/deploy` 选择任意环境，并支持 `$env` 配置覆盖及 `import.meta.envName`。
- 🥟 **Bun/Deno 原生开发服务器**：`nitro dev` 在 Bun 和 Deno 上使用原生服务器，WebSocket 与 `devProxy` 也可用；Node.js 行为不变。
- ▲ **Vercel 改进**：ISR 仅由 `isr` 路由规则显式开启；支持查询参数传递、与运行时一致的路由匹配、从 `package.json` 选择运行时，以及 `waitUntil` 和可观测性。
- ☁️ **本地 Cloudflare 支持**：Durable Objects、Workflows 和 RPC 服务绑定可在 `nitro dev`/`vite dev` 中使用并热重载；`cloudflare_durable` 合并进 `cloudflare_module`。
- 🎁 **其他更新**：升级到 H3 v2 和 rou3 v1；`useStorage` 改为 `useKV`；新增缓存存储、异步插件、QUERY 方法、405/HEAD 处理、中间件缓存路由支持、`FastResponse`、资源 URL 输出和 tsconfig paths 支持等。
- 🏁 **快速开始**：内置 `nitro create` 替代 `create-nitro-app`，提供 Vite、Rolldown、Runtime 三种模板。
- ⬆️ **升级注意**：需 Node.js >=22.22.0，并将构建器加入 `devDependencies`；缓存默认存内存、catch-all 路由匹配 `/docs`、点号后缀文件名规则、钩子顺序和 `FastResponse` 等行为有变化，另有重命名与移除项需参考迁移指南。

---

### [AI 令牌欺诈预防 | Fingerprint](https://fingerprint.com/use-cases/ai-token-fraud/?utm_source=NodeWeekly110526&utm_medium=newsletter)

**原文标题**: [AI Token Fraud Prevention | Fingerprint](https://fingerprint.com/use-cases/ai-token-fraud/?utm_source=NodeWeekly110526&utm_medium=newsletter)

Fingerprint 的设备智能方案旨在阻止 AI token 欺诈：攻击者通过批量注册免费试用账户，反复消耗企业支付的 GPU 推理额度，并将赠送 credits 转售或用于蒸馏模型。该方案通过持久 Visitor ID 与 Smart Signals，在注册、发放免费额度和 API 调用等环节识别同一设备，即使对方更换邮箱、清除 Cookie、使用隐私窗口、VPN 或代理，也能关联账户并实时限制滥用，同时尽量不增加真实用户摩擦。

- 🤖 **AI token 欺诈本质**：重复免费试用注册会放大推理成本，目标不是只抓单个假账户，而是识别其背后的整组关联账户。
- 🧠 **核心机制**：Fingerprint 为每个注册和登录识别设备，生成持久 Visitor ID，实现“一设备一账户”，即使邮箱、IP、Cookie 变化仍可关联。
- 🛡️ **主要防滥用场景**：安全发放促销 credits、识别账户农场/反检测浏览器/设备农场、限制重复设备领取免费 tokens，同时保持免费层开放且无需 CAPTCHA。
- 📡 **Smart Signals**：提供速度信号、虚拟机、篡改、AI Agent、Suspect Score、高活跃设备、VPN/代理等信号，用于实时判断 token 滥用风险。
- 💻 **代码落地方式**：可在免费额度发放时按设备限制，在模型调用时限流伪造代理和异常请求，在登录时执行套餐设备上限并识别 VPN/代理轮换。
- 🤝 **AI Agent 区分**：对签名请求的合法 AI Agent 标记为已签名并允许，对冒充已知身份但签名无效的 Agent 标记为伪造并拦截。
- 📈 **客户成效**：ZBD 结合 Visitor ID 与 Smart Signals，将多账户欺诈创建量降低 95%，并消除单小时数千假账户的峰值。
- 🌍 **规模数据**：过去 12 个月防止超过 10 亿美元欺诈损失，每年识别 70 亿以上唯一浏览器/移动设备，每日处理 1 亿以上实时设备智能 API 事件。
- ❓ **实施与兼容性**：识别在后台毫秒级完成，不增加用户步骤；覆盖 Web、iOS、Android，并可通过事件 ID 关联 API 请求，也可将 Visitor ID、信号和 Suspect Score 接入自有风控模型。

---

### [加拿大 11 月 1 日时间变更后时间错误：Java、Go、PHP、Node.js、Kubernetes CronJobs 和 MySQL 仍差一小时，以及经过测试的修复方案](https://cybernative.ai/guides/canada-time-zone-change-2026-runtimes/?utm_source=nodeweekly&utm_medium=classified&utm_campaign=paid1-canada-node)

**原文标题**: [Wrong time after Canada's November 1 time change: Java, Go, PHP, Node.js, Kubernetes CronJobs and MySQL still an hour off, and tested fixes — CyberNative](https://cybernative.ai/guides/canada-time-zone-change-2026-runtimes/?utm_source=nodeweekly&utm_medium=classified&utm_campaign=paid1-canada-node)

2026 年 11 月 1 日 02:00 起，加拿大不列颠哥伦比亚省、阿尔伯塔省、西北地区和曼尼托巴省停止季节性调钟；使用旧时区规则的软件会把温哥华、埃德蒙顿、伊努维克、温尼伯的时间显示慢 1 小时。核心修复是 IANA 时区数据库 2026e，但许多运行时自带时区数据，更新操作系统并不够，且已运行进程可能需要重启。

- 🕒 **变更范围**：11 月 1 日 02:00 后，旧数据会让卡尔加里、埃德蒙顿、伊努维克、温尼伯慢 1 小时；比 2026 年 4 月更旧的数据还会弄错温哥华。
- 🧭 **版本对应**：2026b 修不列颠哥伦比亚省，2026c 修阿尔伯塔省，2026d 修伊努维克，2026e 修温尼伯；目标版本是 2026e 或更新。
- ⚠️ **仍可能出错**：Java/Temurin、PHP 8.2/8.3、Go 内置数据、旧版 Node.js、Rust chrono-tz、Kubernetes CronJob、MySQL/MariaDB 命名时区、Windows 新时区映射等。
- ☕ **Java 修复**：Temurin 8/11 及部分 17/镜像仍带旧数据；可替换 `tzdb.dat`。Temurin 17.0.21、21.0.13、25.0.5 和 Corretto 10 月版、Debian 12 的 openjdk-17 已带 2026e。
- 🐘 **PHP 修复**：8.3.36 和 8.2.35 不会在这些分支修复；用 PECL `timezonedb-2026.5`。PHP 8.4.27 和 8.5.12 已带 2026e。
- 🐹 **Go 修复**：Go 1.27.3 内置 2026c，正式修复要到 Go 1.28（2027 年 2 月）；scratch 和 `static-debian12` 镜像需注入当前 zoneinfo，当前 distroless static 镜像已修。
- 🟢 **Node.js 修复**：官方 24.22.1 和 22.23.4 已带 2026e；旧版或发行版包可用 `ICU_TIMEZONE_FILES_DIR` 指向四个 2026e `.res` 文件，注意文件权限。
- 🦀 **Rust 修复**：chrono-tz 0.10.4 仍是 2025b，且项目已软弃用；jiff 在 Unix 上读系统 zoneinfo，并自带 2026e 备用数据。
- ☸️ **Kubernetes 修复**：设置 `timeZone` 的 CronJob 由 `kube-controller-manager` 镜像决定，支持版本多为 2026b；可挂载 2026e zoneinfo，或改用 `Etc/UTC` 并按 UTC 写计划。
- 🐬 **MySQL/MariaDB 修复**：命名时区表只初始化一次，升级或更新 OS `tzdata` 不会刷新；用 `mysql_tzinfo_to_sql` / `mariadb-tzinfo-to-sql` 载入 2026e 并重启服务器。
- 🪟 **Windows 修复**：新增 `British Columbia Standard Time`、`Alberta Standard Time`、`Manitoba Standard Time`；自动时区会迁移，手动设置需用 `Set-TimeZone`，映射表需 CLDR 49、ICU 79.1、TimeZoneConverter 8.0.0、tzlocal 5.4.5。
- 🐳 **基础镜像**：Ubuntu 22.04/24.04/26.04 于 10 月 14 日、Debian 13 于 10 月 22 日、Debian 12 于 10 月 23 日、Amazon Linux 2023 release 2023.12.20261013 已带 2026e；安装 `tzdata` 后要重启服务。
- ✅ **检查方法**：Java 查 `tzdb.dat`；PHP 查 `timezone_version_get()` ≥ 2026.5；Node 查 `process.versions.tz` ≥ 2026e；2026-12-15 偏移应为 Edmonton `-06:00`、Inuvik `-06:00`、Winnipeg `-05:00`。
- 💼 **付费检查**：CyberNative 提供每镜像/技术栈 99 美元的检查，邮件 `hello@cybernative.ai`，主题“Canada check”，结果交付后付款。

---

### [GitHub - sindresorhus/ora：优雅的终端加载动画 · GitHub](https://github.com/sindresorhus/ora)

**原文标题**: [GitHub - sindresorhus/ora: Elegant terminal spinner · GitHub](https://github.com/sindresorhus/ora)

ora 是一个优雅的终端加载动画（spinner）库，支持自定义文本、颜色、前后缀、缩进、输出流和启用状态，提供成功、失败、警告、信息等状态方法，并提供 `oraPromise` 封装 Promise 流程；同时说明了日志集成、终端高度截断、单 spinner 限制和 Worker 线程不适用等注意事项。

- 🌀 安装方式：`npm install ora`，也可选择更小的替代品 `yocto-spinner`。
- ✨ 基本用法：`ora('Loading unicorns').start()`，运行中可动态修改 `text` 和 `color`。
- ⚙️ 主要选项：`text`、`prefixText`、`suffixText`、`spinner`、`color`、`hideCursor`、`indent`、`interval`、`stream`、`isEnabled`、`isSilent`、`discardStdin`。
- 🎨 默认配置：颜色为 `cyan`，spinner 为 `dots`；部分 Windows 终端会自动使用 `line` spinner。
- 🧩 实例控制：支持 `.start()`、`.stop()`、`.succeed()`、`.fail()`、`.warn()`、`.info()`、`.stopAndPersist()`、`.clear()`、`.render()`、`.frame()` 等方法。
- 🤝 `oraPromise`：可为 Promise 或返回 Promise 的函数自动启动 spinner，成功调用 `.succeed()`，失败调用 `.fail()`，并支持自定义成功/失败文本与符号。
- 📝 日志兼容：运行中 `console.log()`、`console.error()`、`console.warn()` 会临时清除并重绘 spinner；应写入完整行，进度建议更新 `spinner.text`。
- ⚠️ 使用限制：不要并发运行多个 spinner；终端高度不足时内容会被截断；不支持 Node.js Worker 线程，需在主线程控制。
- 🔁 相关生态：包括 `yocto-spinner`、`cli-spinners`，以及 Swift、Python、Rust、Go、Deno 等移植项目。

---

### [vite-plus v1.5.0 发布 · voidzero-dev/vite-plus · GitHub](https://github.com/voidzero-dev/vite-plus/releases/tag/v1.5.0)

**原文标题**: [Release vite-plus v1.5.0 · voidzero-dev/vite-plus · GitHub](https://github.com/voidzero-dev/vite-plus/releases/tag/v1.5.0)

Vite+ v1.5.0 已发布，重点新增官方 Homebrew tap、支持通过 `node --import vite-plus/register` 运行 TypeScript，并增强 `vp migrate` 对 `oxnode` 和仅转译 `ts-node` 脚本的迁移能力；同时升级捆绑工具链并修复安全、兼容性与性能问题。升级后若 CI 使用 `vp check`，建议运行 `vp fmt`，因为新版 oxlint/oxfmt 可能标记旧代码。

- 🍺 新增官方 Homebrew tap，macOS 和 glibc Linux 可通过 `brew tap`/`brew install` 安装 `vp`。
- 🟦 `node --import vite-plus/register` 使用与 `vpx` 相同的加载器运行 TypeScript，支持 Node 测试运行器、AVA、`NODE_OPTIONS` 等自行启动 Node 的工具。
- 🔄 `vp migrate` 可将 `oxnode` 和仅转译的 `ts-node` 命令迁移到 `vpx`，并迁移预加载和字面量 `NODE_OPTIONS`；带类型检查的 `ts-node` 保留并给出警告。
- ⚠️ `vp migrate` 会警告 Rollup、Rolldown、Jest 依赖及匹配配置，并说明迁移到 Vite、tsdown、Vitest 的方法。
- 🧩 新增 `resolveConfigFromFile(configFile, options?)`，按配置文件目录解析配置，适配多工作区编辑器插件。
- 🔒 安全修复：内置 `minimatch@11.0.4` 修复 glob 模式放大导致的 DoS，`zstd@0.13.4` 修复多项 RUSTSEC 漏洞。
- ⬆️ 升级捆绑工具：rolldown 1.2.16、tsdown 0.23.4、vitest 5.1.0、oxlint 1.91.0、oxfmt 0.76.0 等，带来新规则、HTML 格式化、环境文件与测试增强。
- 🚨 新版 oxlint/oxfmt 可能命中旧代码；若 CI 运行 `vp check`，升级后应执行 `vp fmt`。已知 `oxlint@1.91.0` 可能在 effect 内 `let` 被闭包重赋值时误报 `react/immutability`。
- 🛠️ 修复与增强：`vp create` 对符号链接目标只删除链接；`vp implode` 仅删除可验证的 Vite+ 安装并拒绝危险目录；`vp run` 在共享缓存模式工作区更快，npm 项目启动约快 110ms。
- 🌐 `vp env` 的 `latest` 别名解析到最新稳定版，支持 `VP_NODE_VERSION=22` 等部分版本；并发 `vp install -g` 不再互删；`vp config` 遇 git 配置锁会重试。
- ✅ `vp env doctor` 将 Node 解析失败、配置不可读、系统 `node` 失败、缺失 shim 视为错误并以 1 退出；仅有警告时显示“Some warnings found”。
- 🧰 其他改进包括 Nushell 补全更新、`vp migrate` 更准确处理 `tsx`、`prefer-vite-plus-imports` 自动修复更安全、Zed 设置遵循 `vite.config.ts`，以及 npm 兼容性、`dlx`、`outdated` 等行为修复。
- 📦 安装方式支持 Homebrew、macOS/Linux 脚本、Windows 脚本或 `vp-setup.exe`、Docker；也可用 `create-vite-plus` 免全局安装创建新项目。

---

### [发布 v16.2.0 · sindresorhus/got · GitHub](https://github.com/sindresorhus/got/releases/tag/v16.2.0)

**原文标题**: [Release v16.2.0 · sindresorhus/got · GitHub](https://github.com/sindresorhus/got/releases/tag/v16.2.0)

got 发布最新版本 v16.2.0，核心更新是为 `.json()` 增加 Standard Schema 支持；该版本于 10 月 30 日 08:46 发布，可与 v16.1.0 对比，并提供 2 个资源文件。

- 🚀 v16.2.0 为最新版本，发布提交为 6b5aafc。
- 🧩 主要变更：`.json()` 新增 Standard Schema 支持（#2477）。
- 🗓️ 发布日期为 10 月 30 日 08:46。
- 🔍 支持查看 v16.1.0...v16.2.0 的版本对比。
- 📦 发布页面提供 2 个资源文件。
- 🔐 仓库仅协作者可创建 PR；页面包含 Code、Issues、Discussions、Actions、Security 等入口。
- 👍 获得 1 个点赞反应。

---

### [发布 v7.3.0 · fastify/fast-json-stringify · GitHub](https://github.com/fastify/fast-json-stringify/releases/tag/v7.3.0)

**原文标题**: [Release v7.3.0 · fastify/fast-json-stringify · GitHub](https://github.com/fastify/fast-json-stringify/releases/tag/v7.3.0)

fast-json-stringify 发布 v7.3.0 版本，本次更新包含 2 个提交，核心变更是新增 `objectMechanism: 'native'` 特性，使对象投影后交由 `JSON.stringify` 处理。

- 🚀 发布版本：fast-json-stringify v7.3.0
- 📅 发布时间：11 月 05 日 10:24
- 🔧 核心更新：新增 `objectMechanism 'native'`，用于对象投影并委托给 `JSON.stringify`
- 👤 贡献者：Tony133，对应 PR #906
- 📜 完整变更记录：v7.2.1...v7.3.0
- 📦 发布资源：包含 2 个 Assets

---

### [feat: objectMechanism 'native' projects objects and delegates to JSON.stringify by Tony133 · Pull Request #906 · fastify/fast-json-stringify · GitHub](https://github.com/fastify/fast-json-stringify/pull/906)

**原文标题**: [feat: objectMechanism 'native' projects objects and delegates to JSON.stringify by Tony133 · Pull Request #906 · fastify/fast-json-stringify · GitHub](https://github.com/fastify/fast-json-stringify/pull/906)

该 PR 为 fast-json-stringify 新增可选 `objectMechanism: 'native'`：生成代码将输入投影到按 schema 预分配的纯对象，再委托 `JSON.stringify`，以利用 Node 25+ / V8 13.8+ 的原生快速路径，同时保持 schema 语义与默认机制输出字节一致；PR 已合并，属 semver-minor。

- 🚀 **核心机制**：`native` 模式不自行拼接 JSON 字符串，而是复制到仅含 schema 属性的 scratch 对象后调用 `JSON.stringify`，避免 Date、toJSON、额外属性等导致 V8 退出快速路径。
- 🛡️ **默认行为不变**：默认仍是 `'default'`，需显式启用；未覆盖的 schema 会静默回退到默认代码生成，因此启用该选项是安全的。
- 📋 **覆盖范围**：支持含 `properties` 的 object、string/date-time/date/time、number、integer、boolean、enum/const、部分组合类型、二元素 nullable 形式及嵌套数组；不支持 `additionalProperties`、`patternProperties`、`nullable`、`$ref` 等复杂 schema。
- ⚡ **Node 26 性能**：干净数据上相对默认代码生成提升约 +38% 至 +157%，与裸 `JSON.stringify` 差距缩小到 5%–16%；ORM 类数据上比 `JSON.stringify` 快 7–14 倍，比默认代码生成快约 +63%/+106%。
- 🧱 **运行时门控**：Node < 25 上该选项为 no-op；强制启用时因缺少 V8 快速路径，单对象场景可能比默认代码生成慢 10%–57%，列表场景有胜有负。
- 🧪 **测试与质量**：新增 native/default 差分测试、数组隔离、schema 覆盖、门控测试等；完整测试 675/675 通过，Node 22/26 的 `c8 --100`、`tstyche` 与 lint 均通过。
- 🔀 **合并与后续**：已由 mcollina 合并到 main；讨论建议在 Fastify 6 中将其设为默认，并继续评估 Node 22/24 上按 schema 特征启用投影的门控策略。

---

### [Release v1.6.0 · richardgirges/express-fileupload · GitHub](https://github.com/richardgirges/express-fileupload/releases/tag/v1.6.0)

**原文标题**: [Release v1.6.0 · richardgirges/express-fileupload · GitHub](https://github.com/richardgirges/express-fileupload/releases/tag/v1.6.0)

概述：express-fileupload 仓库发布了最新版本 v1.6.0，主要变更是修复 multipart Content-Type 检查中的 ReDoS 安全问题。  
- 📦 仓库：richardgirges/express-fileupload  
- 🏷️ 最新版本：v1.6.0  
- 👤 发布者：richardgirges  
- 🕒 发布时间：11 月 04 日 19:43  
- 🔧 主要变更：修复 multipart Content-Type 检查中的 ReDoS 漏洞（#392）  
- 🔗 提交记录：3813cf2  
- 📊 当前状态：20 个 Issues、5 个 Pull requests  
- 📁 其他信息：包含 Actions、Projects、Wiki、Security and quality、Insights 等仓库功能入口  
- ⚠️ 页面提示：发布资源区域出现加载错误，建议重新加载页面

---

### [发布 v8.0.0 · mikaelbr/marked-terminal · GitHub](https://github.com/mikaelbr/marked-terminal/releases/tag/v8.0.0)

**原文标题**: [Release v8.0.0 · mikaelbr/marked-terminal · GitHub](https://github.com/mikaelbr/marked-terminal/releases/tag/v8.0.0)

marked-terminal 发布 v8.0.0，完成 TypeScript 重写、减少依赖，并新增 CLI、图片渲染、超链接控制与更完善的 reflow 能力，同时包含多项破坏性变更和问题修复。

- 🚀 **重大版本更新**：v8.0.0 对 marked-terminal 进行现代化重写，改用 TypeScript，减少依赖，并改进文本重排。
- ⚠️ **破坏性变更**：要求 Node.js >= 22.12、marked >= 13，且包改为 ESM-only；`require('marked-terminal')` 仍可通过 Node 原生 `require(esm)` 使用。
- 🔁 **API 迁移**：移除 `TerminalRenderer` 类和默认导出，改用 `markedTerminal` 扩展；迁移方式为 `marked.use(markedTerminal(options, highlightOptions))`。
- 🎨 **高亮与样式调整**：语法高亮改用 `emphasize`，`highlightOptions` 变为 `{ sheet, subset }`；默认样式改用 `node:util` 的 `styleText`，不再依赖 chalk。
- 📋 **列表渲染改进**：开启 `reflowText` 时列表也会换行；顶层列表不再缩进，嵌套列表仍按 tab 缩进。
- 💻 **新增 mt CLI**：可直接渲染 Markdown 文件或处理 shell 管道输入，并默认绘制图片，支持 `--no-images`、`--remote-images`。
- 🖼️ **图片支持**：新增 `images` 选项，支持 iTerm2/Kitty 图形协议全分辨率显示，其他终端用彩色半块像素化显示；远程图片仅在 `remote: true` 时下载。
- 📏 **表格与超链接**：开启 `reflowText` 时表格会收缩以适应宽度；新增 `hyperlinks` 选项控制终端可点击链接，未设置时从 stdout 检测。
- 📦 **类型与兼容性**：内置 TypeScript 类型，支持 marked 至 v18；使用 `@types/marked-terminal` 的用户可移除该依赖。
- 🐛 **问题修复**：修复 marked v13+ 列表项中的粗体、斜体、代码等行内格式渲染，修复彩色嵌套列表多余空行，以及 GFM 任务列表渲染问题。

---

### [发布 v3.3.0 · koajs/koa · GitHub](https://github.com/koajs/koa/releases/tag/v3.3.0)

**原文标题**: [Release v3.3.0 · koajs/koa · GitHub](https://github.com/koajs/koa/releases/tag/v3.3.0)

Koa 发布 v3.3.0，主要包含依赖升级、文档修正，以及请求解析、响应头、查询参数和 HttpError 处理等多项修复，同时将 CI 的 Node.js 版本覆盖扩展到 22–26。

- 🚀 发布 v3.3.0：由 yowainwright 于 11 月 3 日发布，标签和提交均通过验证签名。
- 📦 依赖升级：更新 GitHub Actions 的 checkout、setup-node 至 v6，codecov-action 至 v7，并升级 flatted、c8、supertest、type-is、minimatch 等。
- 🐛 响应修复：保留 Blob 的 Content-Type，避免强制为 octet-stream；拒绝单值响应头出现多个值。
- 🧭 请求解析修复：支持 absolute-form 请求目标，改进 request.URL、IPv6 hostname 和 request.host 解析，并将 X-Forwarded-Proto 转为小写。
- 🧩 查询参数修复：赋值时保留布尔值，解析时防止原型污染和原型变更。
- 🛡️ 错误处理改进：使 ctx.assert 错误成为 HttpError 实例，并保留 HttpError 子类及基于原型的 instanceof 检查。
- 🔁 新增 http-errors 工具再导出。
- 📝 文档改进：修正 app.currentContext 示例、Application 构造函数 JSDoc 和 request.hostname 链接。
- ⚙️ CI 调整：Node.js 版本覆盖提升至 22–26。
- 👥 新贡献者：@PoChenKuo、@DucMinhNe、@kshitijanurag、@nuintun、@xia-chao 等首次贡献。
- 🔗 完整变更：v3.2.1...v3.3.0，包含 3 个资产及 12 位以上贡献者。

---

