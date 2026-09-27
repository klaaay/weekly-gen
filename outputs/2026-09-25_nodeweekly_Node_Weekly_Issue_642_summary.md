### [取代 npm 包的 Node.js 内置模块](https://flaviocopes.com/node-builtins/)

**原文标题**: [Node.js built-ins that replaced npm packages](https://flaviocopes.com/node-builtins/)

Node.js 现在内置了十二个功能，可以直接替代过去几乎每个项目都会安装的 npm 包，涵盖数据库、测试、HTTP 请求、热重载、环境变量、命令行解析、终端着色、文件匹配、WebSocket、UUID 生成、文件系统操作和 TypeScript 运行等场景。文章逐一给出最短示例、在 Node 24（LTS）中的稳定程度以及每个内置方案相比原包缺失的能力，并说明 Node 22 与 24 之间的差异，最后建议在删除依赖前先确认部署环境版本并把版本固定到 engines 字段。

- 🗄️ `node:sqlite` 替代 `better-sqlite3`：同步 API、用法相似，Node 24 中为 1.2 发布候选（24.15.0 起），Node 22 仍为 1.1；缺点是没有 `db.transaction()` 自动事务封装，需自己写 BEGIN/COMMIT/ROLLBACK。
- 🧪 `node:test` 与 `node:assert` 替代 Jest 和 Mocha：零配置，`node --test` 自动发现测试文件，Node 20 起稳定；但代码覆盖率、模块级 mock 和 watch 模式仍是实验性，重度依赖模块 mock 的项目暂时保留 Jest。
- 🌐 全局 `fetch()` 替代 `axios` 和 `node-fetch`：基于 undici，自带 Request/Response/Headers/FormData，Node 21 起稳定；但 404/500 不会抛错（需自行检查 `res.ok`），没有拦截器和自动重试，代理需 `--use-env-proxy`。
- 🔄 `node --watch` 替代 `nodemon`：一条命令即可在文件变更时重启进程，Node 22 起稳定；默认只监听入口文件和被导入模块，`--watch-path` 仅支持 macOS 和 Windows，且不能与 `--run` 组合。
- 🔐 `--env-file` 和 `process.loadEnvFile()` 替代 `dotenv`：支持引号、多行值和 `#` 注释，命令行标志还能解析 `NODE_OPTIONS`；但无变量展开（需 dotenv-expand），文件缺失会报错（可用 `--env-file-if-exists`），且 shell 中已设的变量优先。
- ⌨️ `util.parseArgs()` 替代 `yargs`、`commander` 和 `minimist`：Node 20 起稳定，支持短选项和默认值；但类型仅支持 string/boolean，无 `--help` 生成、无子命令，未声明的选项默认抛错，正式对外 CLI 仍建议用 commander。
- 🎨 `util.styleText()` 替代 `chalk`：Node 22.13 起稳定，支持样式数组组合、遵循 NO_COLOR/FORCE_COLOR；但输出非终端时自动去掉颜色码（测试时需 `validateStream: false`），且没有链式调用 API。
- 📂 `fs.glob()` 替代 `glob`：Node 24 稳定（Node 22 为实验性），支持花括号扩展和 exclude；但 Promise 版返回异步迭代器而非数组，选项也远少于 glob 包。
- 🔌 全局 `WebSocket` 替代 `ws` 的客户端部分：Node 22.4 起稳定，浏览器同款 API；但仅限客户端，服务端仍需安装 `ws`，核心中没有 WebSocketServer。
- 🆔 `crypto.randomUUID()` 替代 `uuid`：全局可用，稳定；但只能生成 v4 随机 UUID，没有 v7（时间有序、适合做数据库主键）、validate、parse 和 v5 等能力。
- 🧹 `fs.rm()` 与带 `recursive` 的 `fs.mkdir()` 替代 `rimraf` 和 `mkdirp`：均有同步版本，可用于 clean 脚本；但 `rm()` 只接受单个路径不支持模式匹配，且不加 `recursive: true` 删目录会报 ERR_FS_EISDIR。
- 📘 TypeScript 类型擦除替代 `ts-node` 和 `tsx`：Node 24.12 起稳定，无需安装配置，不做类型检查也没有 source map；但仅支持可擦除语法，enum、namespace、构造函数参数属性等会抛错，Node 26 移除了 `--experimental-transform-types`，且 tsconfig paths 被忽略、不支持 .tsx。
- ⚖️ 总体建议：内置方案只覆盖常见场景，旧包在缺失的功能上仍有价值，例如需要拦截器就用 axios、服务端用 ws、模块 mock 用 Jest；移除依赖前先阅读对应“短板”，并确认部署目标的 Node 版本（Node 22 上 sqlite、glob、env-file 等仍为实验性），在 engines 中固定版本。

---

### [](https://github.com/Agent-Field/CodeAF)

**原文标题**: [GitHub - Agent-Field/CodeAF: Open-Source Software factory for Open Models · GitHub](https://github.com/Agent-Field/CodeAF)

CodeAF 是 AgentField AI 推出的开源 coding harness，面向开放模型，主打“软件工厂”式工作流：一个窗口管理多项目，将对话转为任务，自动调度、检查、合并，并支持子 harness、多模型座席、远程/无头和低资源占用。项目为 Apache 2.0 许可，Go 单二进制，目前处于早期预览阶段。

- 🏭 定位：为开放模型打造的前沿级编码 harness，强调以更低成本完成编码，并把多代理工作集中到一个控制室。
- 🪟 单窗口多项目：home 列出所有项目和会话，enter 打开，tab 切换，alt+k 跳转；每个项目有独立审批、模型和花费限制。
- 💬 对话变任务：像对同事说话一样描述问题，一条消息可拆成多个任务，各自在仓库副本和分支运行，对话不中断。
- ✅ 自动合并：通过检查的工作自动落到你的分支，绝不直接到 main/dev/release；无法检查的结果进入 unread，等待 accept 或 not right。
- 🏗️ “工厂”模式：自动评估、拆分、并行执行、测试并合并通过部分，只在必须时提问，问题汇总到 needs you。
- 🧩 子 harness：为审查 PR、修复 issue、审计依赖等特定工作构建专家，类型化输入/输出；PR-AF 即将原生加入。
- 🧠 多模型 crew：同一会话可多模型协作，含 reflex、small work、worker、careful work、mastermind 五席，可用 /crew frugal、balanced、max 一键设置。
- 📊 模型池：默认从其他安装的匿名计算结果中辅助选模型，不发送代码、提示、路径或身份；可关闭，relay 索引公开在 model-pool 分支。
- 📌 常驻指令：规则、提醒和监控可通过自然语言设置，一次确认后持续生效，并受每日花费限制。
- 🤖 Headless：codeaf do 用于 CI、cron、脚本和基准，接受自然语言简报，计划、运行、检查后输出 JSON 和退出码。
- 🌐 远程工作：屏幕在本地，会话在工作机；codeaf chat --host devbox 通过现有 SSH 连接，手机也可 ssh 接入同一实时会话。
- ⚡ 性能：单个 Go 二进制约 53 MB，最多比同类小 21 倍；新增会话内存 27 MB，16 个空闲会话约 507 MB，恢复 50 轮会话约 145 ms。
- 🔐 遥测与许可：Apache 2.0；默认发送匿名使用计数，可用 CODEAF_TELEMETRY=off 关闭；绝不收集提示、代码、路径、仓库名等。
- 📚 文档与安装：curl 安装脚本，或 git clone + make build；内置手册、指南和 docs/ 覆盖架构、headless、远程与限制。

---

### [Node.js — Node.js 26.10.0（当前版本）](https://nodejs.org/en/blog/release/v26.10.0)

**原文标题**: [Node.js — Node.js 26.10.0 (Current)](https://nodejs.org/en/blog/release/v26.10.0)

Node.js 26.10.0（Current）于 2026-09-22 发布，由 @aduh95 / Antoine du Hamel 参与发布，包含多项 SEMVER-MINOR 新功能、大量修复与性能优化，并提供 Windows、macOS、Linux、AIX、ARM 等平台的安装包、二进制、源码、文档及 SHA256/PGP 校验文件。

- 🚀 版本信息：Node.js 26.10.0 属于 Current 版本线，发布于 2026-09-22。
- 🔐 加密增强：新增 crypto.parsePKCS12()，并为 Web Cryptography 加入混合 KEM。
- 📦 FFI 与文件系统：FFI 支持从挂载的 VFS 加载库；fs 新增 openAsBlobSync。
- 🧵 线程与进程：net 支持将 net.BoundSocket 发送到线程和子进程。
- 📊 性能监控：perf_hooks 实现 SlidingWindowHistogram，并为 Histogram 加入 qrde 分析支持。
- 🗄️ SQLite：支持将 undefined 绑定为 NULL，并减少无效 URL 路径导致的异常。
- 🛠️ 工具增强：util 新增 util.throttle、debounce，并加入 util.markPromiseAsHandled。
- 🐛 修复与优化：涵盖 crypto、stream、QUIC、VFS、zlib、TLS、HTTP/2、test_runner 等大量提交，包括 provider 重构、zstd 修复、CRL 加载和流性能优化。
- 📚 文档与协作：更新协作者、triager、Python 支持说明、DOMException、zstd 文档等内容。
- 💾 下载与校验：提供多平台安装包、二进制、源码、文档链接，以及 SHA256 校验和和 PGP 签名。

---

### [](https://github.com/nodejs/node/pull/65899)

**原文标题**: [util: implement debounce by jasnell · Pull Request #65899 · nodejs/node · GitHub](https://github.com/nodejs/node/pull/65899)

Node.js 核心仓库通过 PR #65899 新增内置 util.debounce 与 util.throttle，经 AbortSignal、leading 选项和测试稳定性讨论后，作为 semver-minor 功能合并并随 v26.10.0 发布。

- 🚀 PR #65899 由 jasnell 发起，目标是把 debounce 从 npm 依赖变为 Node.js 内置 util 能力。
- 🛠️ 动机来自 quic、dtls、perf_hooks 等测试中频繁使用 debounce，作者认为它“应该就在那里”。
- 💡 示例：util.debounce(() => console.log(123), 1000)；重复调用会重置计时器，1 秒内无新调用才执行。
- 🧵 讨论中问及 AbortSignal 先例，jasnell 引用 Deno std 和 p-debounce；bakkot 指出 AbortSignal 只能中止一次，若使用应取消所有未来调用。
- ⚠️ bakkot 还建议增加 leading/immediate 选项，让首次调用立即执行，仅对间隔内后续调用延迟；jasnell 接受并更新实现。
- 🧰 在 bricss 建议下，PR 同时加入 util.throttle，用于限制 fn 的调用频率/并发，常与 debounce 搭配。
- ✅ mcollina 批准变更并称几乎所有应用都会用到；PR 随后合并，提交落地于 312db1e...c081d10。
- 🧪 后续 #66034 修复 util.throttle 测试偶发失败：短窗口在调度延迟下可能导致计时断言失败，改用 mock timer 与匹配的 libuv 时钟。
- 📦 该功能作为 semver-minor 出现在 Node.js v26.10.0 (Current) 发布说明中，标签包括 util、semver-minor、author ready、needs-ci。
- 📈 Codecov 显示补丁覆盖率约 95.5%，涉及 lib/internal/util/debounce.js 与 throttle.js，项目覆盖率约 90.23%。

---

### [](https://github.com/nodejs/node/pull/65805)

**原文标题**: [src,lib: add util.markPromiseAsHandled by jasnell · Pull Request #65805 · nodejs/node · GitHub](https://github.com/nodejs/node/pull/65805)

Node.js 主仓库合并了 PR #65805，新增 `util.markPromiseAsHandled`，用于把 Promise 标记为已处理，避免开发者为了抑制 `unhandledRejection` 警告而到处写 `promise.catch(() => {})`。该功能属于 semver-minor 新特性，并已纳入 Node.js 26.10.0。

- 🚀 PR #65805 由 jasnell 提交，标题为 “src,lib: add util.markPromiseAsHandled”，已合并进 `nodejs:main`，合并提交为 `8fb89ab`。
- 💡 动机是作者不想再看到 `promise.catch(() => {})` 这种写法，新 API 可更语义化地处理 Promise 拒绝。
- 🏷️ 该变更被标记为 `semver-minor`，涉及 `util` 模块和 C++ 源码，属于应进入下个次版本的新功能。
- 🧪 代码改动涉及 `src/node_util.cc` 与 `lib/util.js`；Codecov 显示补丁覆盖率为 94.11765%，项目覆盖率为 90.18%，其中 `src/node_util.cc` 有 1 行部分未覆盖。
- ✅ 审查方面，mcollina、MoLow、LiviaMedeiros 已批准；joyeecheung 仍待审查；mcollina 评论 “LGTM”，并认为这可能是性能更好的工具。
- 📝 LiviaMedeiros 建议同步更新 `doc/api/process.md` 中关于非操作 `.catch(() => {})` 处理器的示例，可在本 PR 或后续跟进处理。
- ⚙️ CI 曾通过 86/87 项检查，PR 先后带有 `author ready`、`needs-ci`、`commit-queue-squash` 等标签，最终经 Commit Queue 合入。
- 📦 该功能包含在 2026-09-22 发布的 Node.js 26.10.0 (Current) 中，列为 `src,lib` 的 SEMVER-MINOR 变更。
- 👥 PR 共有 6 位参与者；最终 Reviewed-By 包括 Matteo Collina、Moshe Atlow、LiviaMedeiros。

---

### [](https://github.com/nodejs/node/pull/65427)

**原文标题**: [build: downgrade Intel macOS support to experimental by aduh95 · Pull Request #65427 · nodejs/node · GitHub](https://github.com/nodejs/node/pull/65427)

Node.js 项目合并了 PR #65427，将 Intel macOS（x86_64-darwin）支持降级为实验性，并计划从 Node.js 27 起不再提供官方兼容二进制，原因是用于构建 universal binaries 的 Rosetta 支持预计将在 Node.js 27 生命周期内结束。Intel Mac 用户未来需依赖非官方二进制或转向 Linux。

- 🛠️ PR #65427 标题为 “build: downgrade Intel macOS support to experimental”，已合并进 nodejs/node:main。
- 🍎 将 Intel macOS（x86_64-darwin）支持降级为实验性，并计划自 Node.js 27.0.0-alpha 起停止发布官方 x86_64-darwin 二进制。
- 🧩 核心原因：构建 universal binaries 所依赖的 Rosetta 支持预计会在 Node.js 27 生命周期内结束。
- 💻 Intel Mac 用户将需要依赖非官方二进制，或考虑转向 Linux；评论中也提到 Docker/Podman 可作为替代方案。
- 📦 该 PR 包含 2 个提交：降级 Intel macOS 支持为实验性；回滚 “build: update Makefile to support fat binary”。
- 🏷️ 被标记为 semver-major、build、doc，属于破坏性变更，应在下一个主版本发布。
- ✅ 获得 10 位审核者批准，包括多位 TSC 成员，如 marco-ippolito、tniessen、richardlau、legendecas、anonrig、mcollina、cjihrig、sxa、UlisesGascon、RafaelGSS 等。
- ⏳ Commit Queue 曾失败：无法获取作者邮箱/姓名，且未检测到 Jenkins CI 运行，后经手动处理并重试。
- 🔀 最终提交 87a4efb 于 2026-09-23 合并进 main，29 项检查通过，随后删除分支 x86_64-darwin-eol。
- 🔗 关联 nodejs/build#4317 “macOS future strategy” 和 nodejs/build#4470 “macos: drop x64 macOS tarball from release matrix”。
- 📊 Codecov 报告显示修改且可覆盖行均被测试覆盖，项目覆盖率为 90.31%。
- ⚠️ 有评论提醒：不应默认非官方构建项目会为 Intel macOS 提供二进制支持。

---

### [](https://github.com/nodejs/node/pull/66138)

**原文标题**: [src: add --process-timeout=N by jasnell · Pull Request #66138 · nodejs/node · GitHub](https://github.com/nodejs/node/pull/66138)

Node.js PR #66138 提议新增 `--process-timeout=N`，用原生看门狗线程实现跨平台一致的进程超时，可强制中断主线程、输出诊断信息并以退出码 124 结束；该改动被标记为 semver-minor 和 notable-change，已获 mcollina 批准，但仍需审查与处理 CI/测试稳定性问题。

- ⏱️ 新增 `--process-timeout=N`，为 Node.js 进程设置统一超时限制。
- 🧵 通过原生 watchdog 线程中断主线程，即使卡在忙碌循环或原生代码中也能退出。
- 📋 超时时打印 JavaScript 调用栈、保持事件循环活跃的资源，并可选输出完整诊断报告。
- 🚪 进程以独特退出码 `124` 退出，示例：`node --process-timeout=10s -e "while(true) {}"`。
- ❌ 现有方案有缺陷：OS/CI 超时不一致且无诊断，macOS 和 Windows 默认不带 coreutils `timeout`。
- ⚠️ `setTimeout` 只在事件循环空闲时触发，漏掉忙碌循环和线程阻塞，也看不到栈；信号诊断同样受限。
- 🔍 与 `timeout` 命令对比，后者只发送信号且无诊断，新选项能说明主线程正在执行什么。
- 🧪 需要审查与 `--watch`、`--inspect` 等选项的交互，并评估测试是否容易失败。
- ⏳ 测试风险包括固定 2 秒宽限期、极短窗口、Windows pid 复用、慢机器启动超过约 5 秒。
- 📈 Codecov 补丁覆盖率为 91.86%，28 行缺少覆盖；项目覆盖率约 90.28%。
- ✅ 已获 mcollina 批准；ShogunPanda 待审；曾因 Windows CI 失败阻塞，后 CI 全绿。
- 🏷️ 标签包括 semver-minor、notable-change、author ready、review wanted、c++、lib/src 等。

---

### [](https://github.blog/changelog/2026-09-23-node-20-is-no-longer-available-in-github-actions/)

**原文标题**: [Node 20 is no longer available in GitHub Actions - GitHub Changelog](https://github.blog/changelog/2026-09-23-node-20-is-no-longer-available-in-github-actions/)

GitHub Actions 已正式停止支持 Node 20，运行器改用 Node 24；JavaScript Actions 维护者需更新 `runs.using` 为 `node24` 并尽快发布新版本，使用者也应升级到支持 Node 24 的 actions。部分旧版 macOS 和 ARM32 自托管运行器不再受支持。

- 📅 2026 年 9 月 23 日起，Node 20 在 GitHub Actions 中不再可用，这是最终通知。
- ⚙️ GitHub Actions 运行器现在对 JavaScript actions 使用 Node 24。
- 🔓 临时退出选项 `ACTIONS_ALLOW_USE_UNSECURE_NODE_VERSION` 已不再可用。
- 🛠️ 如果维护 JavaScript action，请将 `runs.using` 更新为 `node24`，并尽快发布新版本。
- ⬆️ 如果工作流使用 JavaScript actions，请更新到支持 Node 24 的最新版本。
- ✅ 所有第一方 actions 的最新版本已更新为使用 Node 24。
- ⚠️ Node 24 与 macOS 13.4 及更早版本不兼容，且不正式支持 ARM32。
- 🖥️ 使用这些操作系统或架构的自托管运行器不再受支持。
- 🌐 此变更适用于 github.com 和 GitHub with Data Residency。

---

### [](https://github.com/nodejs/node/pull/66186)

**原文标题**: [src: compress embedded icu, builtins, and snapshot by anonrig · Pull Request #66186 · nodejs/node · GitHub](https://github.com/nodejs/node/pull/66186)

该 PR #66186 讨论如何通过 zstd 压缩 Node.js 嵌入式 builtin 源码、V8 启动快照与 code cache，以缩小 macOS Release 二进制；最初还尝试压缩完整 ICU 数据，但因会破坏 ICU 文件映射的按需分页、干净页和跨进程共享特性而遭到反对，最终将 ICU 压缩移出本 PR，仅保留 builtin/snapshot 压缩与部分 linker 调整。

- 📦 PR #66186 由 anonrig 提交，目标合并 4 个提交到 nodejs:main，分支为 compress-embedded-blobs。
- 📉 初始 macOS arm64 Release 测量：二进制从 140 MB 降到 91 MB，__LINKEDIT 从 44.1 MB 降到 5.7 MB，__cstring 从 12.9 MB 降到 2.3 MB。
- 🗜️ builtin 单字节源码从 10,513,764 字节压到 2,128,812 字节；快照加 code cache 从 6,593,200 字节压到 1,508,240 字节。
- 🚀 压缩后的 builtin 与快照以 zstd 帧存储，启动时解压一次，并在进程生命周期内保留。
- ⚠️ 早期方案还压缩完整 ICU 数据，反对者指出这会让原本文件映射、可共享、按需分页的 ICU 变成每进程私有匿名内存。
- 🧠 jasnell 计算：压缩 ICU 会让每进程约多出 31.6 MiB 私有内存，ICU 启动工作集可能接近 40.4 MiB，而旧方案只按实际使用页加载。
- 🔄 anonrig 随后把 ICU 压缩移出本 PR，ICU 数据保持文件映射；共享缓存压缩版本转到 #66211。
- 🧪 移除 ICU 压缩后，10 个并行进程测试中每个约 33–34 MB footprint，__TEXT 映射 26.1 MB resident、0 dirty、SM=COW，没有额外约 30 MB 私有 ICU 内存。
- 🧊 #66211 共享缓存方案：ICU 压成 9.2 MB 帧，首次启动写入临时目录并只读映射，后续进程共享；冷启动约 32 MB footprint，约 3.7 MB resident、0 dirty，总二进制 68 MB。
- 🧱 macOS Release linker 使用 -x 和 -S 缩小 __LINKEDIT；-dead_strip 曾剥离 napi_* 符号，导致 lightningcss 文档构建段错误，已被移除。
- 🗣️ srl295 认为应上游与 ICU 讨论，或作为类似 small-icu 的构建选项，并质疑该方案只是用内存换磁盘体积。
- 🛑 jasnell 仍对压缩部分持 -1，建议 linker flag 改动拆成单独 PR 交 nodejs/build 审，并指出 js2c.cc 可能存在端序 bug。
- 📊 Codecov 显示补丁覆盖率 78.08%，项目覆盖率 90.27%，其中 src/zstd_blob.cc 覆盖率约 45%。
- 🏷️ PR 仍为 Open，标签包括 lib/src、needs-ci，已请求 nodejs/gyp、security-wg、startup 等评审，jasnell 要求修改，srl295 等待评审。

---

### [](https://x.com/yagiznizipli/status/2102476047786844494)

**原文标题**: [Yagiz Nizipli on X: "Thanks to Grok 4.7 - Node.js is getting 50% smaller

https://t.co/ZWEs7SnFJI" / X](https://x.com/yagiznizipli/status/2102476047786844494)

Yagiz Nizipli 在 X 上表示，借助 Grok 4.7，Node.js 体积将缩小 50%，并附上了 GitHub PR 链接；该帖发布于 2026 年 9 月 22 日 7:12 PM，浏览量约 12.52 万，互动数据为 50、48、954、117。

- 👤 发布者：Yagiz Nizipli（@yagiznizipli）
- 📉 核心声明：得益于 Grok 4.7，Node.js 将缩小 50%
- 🔗 附带链接：指向 nodejs/node 的 GitHub PR
- 🗓️ 发布时间：2026 年 9 月 22 日 7:12 PM
- 👀 浏览量：约 125.2K
- 📊 互动数据：50、48、954、117

---

### [获取失败](https://lemire.me/blog/2026/09/22/a-summer-of-ai-optimization/)

**原文标题**: [Failed to retrieve](https://lemire.me/blog/2026/09/22/a-summer-of-ai-optimization/)

无法总结：获取内容失败，状态码 520。

---

### [](https://github.blog/changelog/2026-09-18-stage-only-npm-tokens-for-safer-automation/)

**原文标题**: [Stage-only npm tokens for safer automation - GitHub Changelog](https://github.blog/changelog/2026-09-18-stage-only-npm-tokens-for-safer-automation/)

npm 于 2026 年 9 月 18 日发布改进：仅限 stage 的 npm 细粒度访问令牌，让自动化工作流可提交版本供审核，但不能直接发布到 npm registry，以提升供应链安全。

- 📅 该更新属于 Improvement，阅读约 1 分钟。
- 🆕 创建 npm granular access token 时，可选择 “Read and write (stage only)”。
- 🔒 工作流使用 `npm stage publish` 提交版本，维护者通过 2FA 审核批准后发布；直接 `npm publish` 会被拒绝，即使令牌配置为绕过 2FA。
- ⚠️ Stage-only 令牌仍保留其他包写权限，包括移动 dist-tags 和弃用版本，需像其他写令牌一样保护。
- 🔁 此功能为可选启用，不改变现有令牌或直接发布能力；npm 计划 2027 年 1 月移除通过绕过 2FA 令牌直接发布。
- 🧭 若暂不能迁移到 trusted publishing，stage-only 令牌可作为基于令牌自动化的迁移路径。
- ✅ 入门步骤：创建所需包的 granular token；替换工作流发布令牌；使用 `npm stage publish`；由维护者用 2FA 审核并批准 staged 版本。
- 📋 使用要求：对包有发布权限、npm 账号启用 2FA、npm CLI 11.15.0+、Node.js 22.14.0+；适用于现有 npm 包。
- 💬 可查阅 staged publishing 文档，并在 npm 社区讨论区反馈问题或迁移阻碍。

---

### [](https://docs.npmjs.com/trusted-publishers/)

**原文标题**: [Trusted publishing for npm packages | npm Docs](https://docs.npmjs.com/trusted-publishers/)

npm 可信发布通过 OpenID Connect（OIDC）让 CI/CD 工作流直接发布 npm 包，无需长期令牌，提升供应链安全性，并遵循 OpenSSF Trusted Publishers 标准；使用需 npm CLI 11.5.1+ 与 Node 22.14.0+。

- 🔐 工作原理：在 npm 与 CI/CD 提供商之间建立信任，npm CLI 自动检测 OIDC 并优先使用短期、加密签名且不可提取或复用的令牌。
- 🏗️ 支持平台：GitHub Actions（GitHub 托管运行器）、GitLab CI/CD（GitLab.com 共享运行器）、CircleCI（云托管）；暂不支持自托管运行器。
- ⚙️ 配置入口：在 npmjs.com 的包设置中找到 “Trusted Publisher”，选择提供商并填写组织、仓库、工作流、环境等字段。
- 📦 配置限制：每个包最多可配置 10 个可信发布者；现有连接不可修改，只能删除后重新创建。
- 📝 GitHub Actions 字段：需填组织或用户、仓库、工作流文件名，可选环境名与允许动作；工作流文件须位于 `.github/workflows/`。
- 🦊 GitLab CI/CD 字段：需填命名空间、项目名、顶层 CI 文件路径，可选环境名与允许动作。
- 🟠 CircleCI 字段：需填组织 ID、项目 ID、流水线定义 ID、VCS 来源，可选上下文 ID 与允许动作。
- 🚀 GitHub 工作流要求：必须设置 `id-token: write` 权限，npm CLI 才能生成并使用 OIDC 令牌发布。
- 🧪 GitLab 工作流要求：需配置 `id_tokens`，并将 `aud` 设为 `npm:registry.npmjs.org`。
- 🔁 CircleCI 工作流要求：设置 `NPM_ID_TOKEN` 环境变量，通过 `circleci run oidc get` 获取 OIDC 令牌，npm CLI 自动交换。
- 🛡️ 安全建议：配置可信发布后，建议在发布访问设置中选择“要求双因素认证并禁止令牌”，减少长期令牌风险。
- 🔒 最大安全：可将可信发布者设为仅允许 `npm stage publish`，让每次 CI 发布都需维护者通过 2FA 审核批准。
- 🔄 迁移建议：先设置并验证可信发布，再限制令牌访问，最后撤销不再需要的自动化令牌。
- 📜 自动 provenance：从 GitHub Actions 或 GitLab CI/CD 可信发布时，会自动生成 provenance 证明；CircleCI 暂不支持。
- ✅ provenance 条件：需同时满足 OIDC 发布、公共仓库、公共包；私有仓库即使发布公共包也不会生成。
- ⛔ 禁用 provenance：可通过 `NPM_CONFIG_PROVENANCE=false`、`.npmrc` 的 `provenance=false` 或 `package.json` 的 `publishConfig.provenance=false` 关闭。
- 🔑 私有依赖：可信发布只用于 `npm publish`；安装私有依赖仍需使用只读粒度访问令牌。
- 🧯 故障排除：`ENEEDAUTH` 时检查工作流文件名、大小写、`.yml` 扩展名、云运行器及 OIDC 权限是否精确匹配。
- 🔎 GitHub 发布注意：`package.json` 中的 `repository.url` 必须与 GitHub 仓库完全匹配，否则可能发布失败。
- ⚠️ 限制：OIDC 仅支持 `npm publish` 和 `npm stage publish`；其他 stage 子命令及 `install`、`view`、`access` 等仍需传统认证，`npm whoami` 不反映 OIDC 状态。

---

### [我是如何追踪 Duplex.from() 中的 Node.js Streams bug 的](https://amanchadha.substack.com/p/how-i-traced-a-nodejs-streams-bug)

**原文标题**: [How I Traced a Node.js Streams Bug in Duplex.from()](https://amanchadha.substack.com/p/how-i-traced-a-nodejs-streams-bug)

overview summary
作者回顾了自己首次为 Node.js 贡献代码的经历：他追踪并修复了 `Duplex.from()` 中一个流生命周期 bug，问题出在 async 函数提前成功返回后，内部握手停滞，导致 `pipeline()` 卡住且上游 `Readable` 无法销毁。最终通过一个小补丁在 `PR #65963` 中修复。

- 🐛 问题来自 Node.js issue `#55077`：`Readable.from(...)` 通过 `pipeline()` 接入 `Duplex.from(async function () {})`，如果函数不消费输入，流不会正常清理。
- 🚧 异常表现是：上游 `Readable` 未被销毁，`pipeline()` 回调可能永远不执行。
- 🔍 关键点是：出错的 async 函数并没有失败，而是成功返回了，这让 bug 更隐蔽。
- 🧭 作者从实现入手追踪：`Duplex.from()` 本质是包装 `duplexify()`，函数参数会进入 `fromAsyncGen()`。
- 🔗 `fromAsyncGen()` 创建内部 async generator，并用 Promise 作为流与 generator 之间的握手机制。
- 🛣️ `Duplex.from(function)` 有两条路径：async generator 走 transform-like 流；普通 async function 走 writable-only `Duplexify`，bug 在后者。
- ⏳ 当 async function 提前返回 fulfilled Promise，而内部 async iterable 没有被消费时，write 握手无法完成，流无法正常 finalization。
- 🧩 原有 `final()` 逻辑中，async function 拒绝会调用 `destroyer(d, err)`，但成功返回时没有对应清理。
- 🛠️ 修复方式很小：增加 `finalized` 标志，在 `final()` 开始时设为 `true`；async function 成功 resolve 时若 `!finalized`，调用 `destroyer(d)`。
- ✅ `finalized` 表示 `final()` 是否已经开始，而不是流是否已经完成，这个区别很重要。
- 🧱 作者没有改动共享的 `fromAsyncGen()`，因为此前更广的修复 `PR #55096` 曾导致 async-generator transform 问题，并在 `#56278` 被回滚。
- 🧪 回归测试创建 `Readable`，接入故意不消费输入的 async function，并断言原 `Readable` 最终 `destroyed === true`。
- 📉 修复前流程是：async function 成功返回 → 成功处理器不清理 → 握手停滞 → Duplex 不结束 → pipeline 等待 → Readable 不销毁。
- 📈 修复后流程是：async function 成功返回 → 检测 `final()` 未开始 → 销毁 Duplex → pipeline 清理传播 → Readable 被销毁。
- 🧠 作者最大收获：异步 bug 往往是生命周期 bug，涉及 async function、async iterable、writable finalization、pipeline 和销毁传播的交互。
- 🌱 这也是作者第一次向 Node.js 贡献：PR 经过 review 和 CI，最初 Jenkins 日志权限受限，重跑 CI 后通过并最终合并。

---

### [](https://www.bram.us/2026/09/20/npm-publish-subfolder/)

**原文标题**: [Ship cleaner packages (without the ./dist or ./src folder) by publishing a subfolder to NPM – Bram.us](https://www.bram.us/2026/09/20/npm-publish-subfolder/)

文章介绍如何用 `npm publish ./dist` 将构建产物子文件夹作为包根发布，从而避免 `dist/`、`src/` 等实现目录泄漏到公共导入路径，并给出自动化、防误操作与本地验证方案。

- 🎯 痛点：npm 包常把 `dist/` 或 `src/` 暴露在 CDN 导入路径中，路径笨拙且暴露内部结构；Node/bundler 用户可通过 `exports` 隐藏，但 CDN 用户不行。
- 💡 核心技巧：`npm publish` 可接受文件夹路径，`npm publish ./dist` 会把 `./dist` 当作包根，其中的文件直接位于发布包顶层。
- 📁 准备步骤：发布前需把 `package.json`、`README.md`、`LICENSE` 等元数据文件复制进 `./dist`。
- 🔧 路径重写：`./dist/package.json` 中要删除内部 `scripts`，并把所有 `./dist/` 前缀替换成 `./`，否则发布后会失效。
- ⚙️ 自动化：可在根 `package.json` 设置 `postbuild`，用零依赖 Node 脚本在构建后复制文件并重写 `package.json`。
- 🛡️ 防误发：把 `prepublishOnly` 改成守卫脚本，要求通过 `npm run pub` 发布；该脚本设置 `PUBLISH=true`，再执行构建和 `npm publish ./dist`。
- 🧪 测试：用 `npm publish ./dist --dry-run` 查看 tarball 清单，或 `npm pack ./dist` 解压检查，确认没有 `dist/` 前缀。
- 🌐 效果：CDN 导入路径更干净，例如 `https://cdn.jsdelivr.net/npm/hic-pageflip`，而不是包含 `dist/`。
- 📌 背景：PNPM 已支持 `publishConfig.directory`，NPM 原生仍不支持；开发者已呼吁类似功能超过 10 年，作者希望 NPM 增加 `publishDirectory`。
- ✅ 实践：作者已在 `hic-pageflip`、`mermaid-element`、`rich-input` 等包使用该模式。

---

### [使用异步生成器和 Promise.race() 实现更快的 SSE 响应 | www.thecodebarbarian.com](https://thecodebarbarian.com/sse-yield-star.html)

**原文标题**: [Faster SSE Responses with Async Generators and Promise.race() | www.thecodebarbarian.com](https://thecodebarbarian.com/sse-yield-star.html)

SSE 允许 HTTP 服务器以事件流方式逐步向客户端发送数据，把传统一次性响应变成类似异步生成器的多次 `yield`；文章用 Express、MongoDB 和 Node.js 展示如何按查询完成顺序推送结果，并用 `yield*` 与 `asCompleted()` 解决异步生成器中无法从回调里 `yield` 的问题，从而提升首屏与感知加载速度。

- 🌊 SSE 是 HTTP 服务器向客户端流式发送数据的方式，传统请求只有一个响应，而 SSE 可以逐个发送中间响应。
- ⚡ 传统 HTTP 处理器类似普通 `async` 函数，SSE 则类似异步生成器函数，每次 `yield` 都会向客户端发送数据。
- 🗄️ 示例中 Express 路由先并行执行用户和消息两个 MongoDB 查询，传统做法要等全部完成后再返回。
- 🚀 使用 SSE 后，可以在每个查询完成时用 `res.write()` 立即推送，客户端不必等待最慢的查询才能开始渲染有用内容。
- 🧩 作者偏好“无框架 JavaScript”，用异步生成器编写业务逻辑，并通过 `toRoute()` 把每次 `yield` 转成 SSE。
- 🚧 异步生成器不能在 `then()` 回调里直接 `yield`，因此需要 `yield*` 和辅助函数 `asCompleted()`。
- 🔁 `asCompleted()` 循环使用 `Promise.race()`，按 Promise 完成顺序逐个 `yield` 结果，而不是保持原始顺序。
- ⚖️ `Promise.all()` 适合必须等全部数据完成后才能处理的场景；`asCompleted()` 适合只关心完成顺序的异步任务。
- 📦 最终可以并行启动多个操作，谁先完成谁先 `yield`，让 SSE 在数据可用时立即发送。

---

### [](https://blog.platformatic.dev/introducing-secure-eval-worker)

**原文标题**: [secure-eval-worker: Least-Privilege JavaScript in Node.js](https://blog.platformatic.dev/introducing-secure-eval-worker)

最小权限执行 JavaScript 的新库 secure-eval-worker 支持在 Node.js 中以受限权限运行不可信代码，兼顾一次性脚本与持久化组件，通过权限模型、宿主函数和白名单协议控制代码能力。

- 🔐 **核心问题**：普通 eval() 继承宿主全部权限，即使放入 worker 线程，代码仍可访问文件系统、网络和环境变量
- 🎯 **设计目标**：并非完美沙箱，而是让最小权限成为在 Node.js 中运行本地代码的标准做法
- ⚙️ **双 API 设计**：runUntrustedCode() 用于一次性执行；createUntrustedWorker() 支持带状态、可处理消息的持久组件
- 🧩 **宿主函数机制**：只暴露 records.find(id)、audit.record(event) 等特定能力，而非完整的数据库或网络客户端
- 🛡️ **权限顺序关键**：在编译、导入或运行任何调用方代码之前，先移除多余权限并加固已知逃逸面
- 🔏 **协议安全**：使用私有 MessageChannel、每会话 HMAC 与单调序列号认证消息，拒绝共享内存、端口、句柄等值类型
- 📁 **本地模块支持**：将允许文件复制到私有临时目录，跳过符号链接并限制文件数量与大小，防止源树篡改影响导入
- ⏱️ **全生命周期限制**：默认最多 4 个并发 worker、源码 64 KiB、启动与请求各 1 秒、持久生命周期 30 秒，超出即失败
- 🚫 **不做 worker 池化**：难以验证环境是否真正干净，因此每次一次性调用都创建全新 worker
- ✅ **测试与兼容性**：跨 Ubuntu、macOS、Windows 测试权限拒绝、协议限制等场景；目前仅支持 Node.js 26.3.0 至 26.x，尚未发布到 npm
- 🧭 **最佳实践**：从无宿主函数的一次性字符串开始，仅添加必要能力，并为高风险工作负载叠加进程或容器级隔离

---

### [](https://owasp.github.io/cve-lite-cli/)

**原文标题**: [Free, local-first JS/TS vulnerability scanner | CVE Lite CLI](https://owasp.github.io/cve-lite-cli/)

CVE Lite CLI 是 OWASP 基金会的 JavaScript/TypeScript 依赖扫描工具，主打本地优先、快速、可操作的安全修复，帮助开发者在推送代码前扫描锁文件、理解漏洞依赖路径并执行修复命令，无需账户或云服务。

- 🛡️ OWASP 项目，面向 JS/TS 依赖安全，核心理念是“扫描、理解、修复”。
- ⚡ 本地扫描 lockfile，数秒出结果，重新扫描近乎即时。
- 🔌 支持 npm、pnpm、Yarn、Bun，并提供 GitHub Action。
- 🧭 具备可达性感知、离线扫描、传递依赖指导和复制即用修复命令。
- 🛠️ 支持自动修复（--fix）、批量修复 PR、AI 助手技能、覆盖项卫生审计和冷却期感知。
- 📜 同时支持许可证扫描，标记 GPL/AGPL/LGPL 与未声明许可证。
- 💸 免费使用，无需账户、订阅或云服务，数据不离开本机。
- 🖥️ 支持终端、HTML 报告和详细模式；HTML 报告含严重性卡片、搜索和可复制修复命令。
- 🏛️ 被法国政府、加拿大不列颠哥伦比亚省政府等团队和项目使用。
- 🚀 安装命令：npm install -g cve-lite-cli；运行示例：cve-lite /path/to/project --verbose。
- 🔁 适合修复循环：扫描、执行建议命令、立即重扫，不必等待 CI。
- 📦 对使用 Dependabot 的团队，可生成一个批量安全修复 PR，而不是 20 个，并包含 OSV 验证版本、公告 ID 和发现数量前后对比。
- 👪 父级感知修复：避免对仅传递依赖直接安装，优先更新或升级控制漏洞路径的父包，并理解 npm 父范围和 workspace hoisting。
- 📚 指南覆盖 HTML 报告、离线公告数据库、工具对比、覆盖项卫生审计、许可证合规扫描和发布冷却期感知。

---

### [](https://www.tigerdata.com/go/trial?utm_source=content-syndication&utm_medium=referral&utm_campaign=node-weekly-newsletter)

**原文标题**: [Postgres for time-series workloads at any scale. | Tiger Data](https://www.tigerdata.com/go/trial?utm_source=content-syndication&utm_medium=referral&utm_campaign=node-weekly-newsletter)

Tiger Data 提供面向时序工作负载的 Postgres 云服务，支持超大规模、弹性独立扩缩、高可用、企业级合规、深度可观测性和快速部署，并向新账户提供 $1000 信用额度。

- 📊 单 Tiger Cloud 服务可承载每天 3 万亿指标、3 PB 数据和 1 千万亿数据点。
- 💳 新账户注册可获 $1000 信用额度，30 天有效，无需信用卡，仅限新用户。
- 🏭 受数千家 IoT 公司信赖。
- ⚙️ 核心扩展：副本集最多 10 节点，读写分离，分层 SSD/S3 提供低成本海量存储。
- 💰 计算与存储分离，可独立扩缩，避免为空闲容量付费并优化性能。
- 🛟 高可用：多可用区集群、自动故障转移、时间点恢复和跨区域备份。
- 🔐 企业级：SOC 2、HIPAA、GDPR 合规，常开加密、SSO、RBAC 和审计日志。
- 🔍 深度可观测性：查询钻取和仪表盘，指标可发送至 CloudWatch、Datadog、Prometheus。
- ⚡ 快速启动：几分钟内配置数据库，可用 SQL、CLI、Terraform、Cursor 或 Claude Code 管理。
- ☁️ 集成与支持：兼容首选云和 Postgres 生态，提供合同化 uptime SLA、区域数据隔离及 24/7 全球专家支持。

---

### [](https://github.com/huggingface/transformers.js/releases/tag/4.3.0)

**原文标题**: [Release 4.3.0 · huggingface/transformers.js · GitHub](https://github.com/huggingface/transformers.js/releases/tag/4.3.0)

Transformers.js v4.3.0 发布，升级 ONNX Runtime，并带来结构化输出、三种新模型架构、Safari 26+ WebGPU 支持、文档大改与多项修复。

- 🚀 v4.3.0 由 xenova 发布，主线包含 2 个提交，重点为结构化输出、新模型、WebGPU 与文档升级。
- 🧩 新增实验性、无依赖的 `@huggingface/transformers-structured-output`，可将生成约束为 JSON Schema、JSON 对象或正则表达式。
- ⚠️ 结构化输出目前一次仅支持生成一个序列，需要设置足够的 token 预算以确保输出完成。
- 🤖 新增 DeepSeek-V4、Zaya、HRM-Text 三种模型架构支持。
- 🌐 为 Safari 26 及以上启用 WebGPU；改进跨源存储，允许所有来源，并跳过非 HTTP(S) 资源的浏览器缓存写入。
- 🛠️ 修复 Rspack/Webpack `import.meta` 警告，以及 `progress_callback` 导致的重复模型下载、Whisper 进度回调等问题。
- 🧪 多项生成与模型修复：`num_logits_to_keep` 固定为 1、Granite Speech 特征数、Moonshine ASR 解码、Chatterbox KV 缓存释放、Gemma3n/Gemma4 WebGPU KV 缓存等。
- 📚 文档全面改版；启用 GitHub Actions 每周 Dependabot 更新；移除未使用代码/导出并更新依赖。
- 👏 感谢新贡献者：@anishesg、@Mr-Neutr0n、@m96-chan、@shoemoney、@patrickkettner、@yushuosun。
- 🔗 完整变更日志为 4.2.0...4.3.0；贡献者包括 tomayac、shoemoney 等 6 人，发布获得 6 个 🎉 反应。

---

### [](https://huggingface.co/docs/transformers.js/index)

**原文标题**: [Transformers.js · Hugging Face](https://huggingface.co/docs/transformers.js/index)

Transformers.js 是 Hugging Face 的 JavaScript 库，让开发者无需服务器即可在浏览器或 Node.js 中直接运行最先进的机器学习模型；其 API 与 Python transformers 高度相似，基于 ONNX Runtime，覆盖自然语言处理、计算机视觉、音频和多模态任务，并提供安装、教程、开发者指南、集成和 API 参考。

- 🤗 可在浏览器中直接运行 🤗 Transformers，无需后端服务器，目标是功能上等价于 Python transformers。
- ⚙️ 使用 ONNX Runtime 推理，并可通过 🤗 Optimum 将 PyTorch、TensorFlow 或 JAX 预训练模型转换为 ONNX。
- 🧩 支持简单易用的 `pipeline` API，自动组合模型、输入预处理和输出后处理。
- 📝 NLP 任务包括文本分类、命名实体识别、问答、摘要、翻译、文本生成、零样本分类等。
- 🖼️ 视觉任务包括图像分类、目标检测、图像分割、深度估计、背景移除、图像特征提取等。
- 🎙️ 音频任务包括自动语音识别、音频分类、文本转语音、零样本音频分类等。
- 🐙 多模态任务包括嵌入、文档问答、图像转文本、零样本图像分类和零样本目标检测等。
- 🚀 默认在浏览器 CPU 上通过 WASM 运行，也可设置 `device: 'webgpu'` 使用 WebGPU 加速。
- 📦 资源受限环境可用 `dtype` 选择量化模型，如 `fp32`、`fp16`、`q8`、`q4`；WASM 默认 `q8`，WebGPU 默认 `fp32`。
- 📚 文档分为 5 部分：入门、教程、开发者指南、集成、API 参考。
- 🧪 教程覆盖 Vanilla JS、React、Next.js、浏览器扩展、Electron、Node.js 服务端推理、Vercel AI SDK 聊天机器人等。
- 🔌 支持与 Vercel AI SDK 等框架集成，并提供环境变量、后端、生成、工具等 API 参考。
- 🏷️ 可在 Hugging Face Hub 用 `transformers.js` 标签筛选兼容模型，并按任务进一步筛选。
- 🧬 支持大量模型架构，如 BERT、T5、CLIP、Whisper、Llama、Qwen、Gemma、DETR、SAM、ResNet 等。
- ⚠️ 当前查看的 `main` 版本需要从源码安装；常规 npm 安装应使用最新稳定版 v3.8.1。
- ✅ 任务支持表覆盖多类模态，但表格问答、视频分类、文生图、视觉问答等部分任务暂不支持。

---

### [获取失败](https://github.com/huggingface/transformers.js/blob/main/.ai/skills/transformers-js/SKILL.md)

**原文标题**: [Failed to retrieve](https://github.com/huggingface/transformers.js/blob/main/.ai/skills/transformers-js/SKILL.md)

无法总结：获取内容失败，状态码 429。

---

### [](https://ben3d.ca/blog/native-gpu-testing-for-vitest-and-jest)

**原文标题**: [2.4x Faster Native GPU Testing for Vitest and Jest without a Browser](https://ben3d.ca/blog/native-gpu-testing-for-vitest-and-jest)

本文介绍为 Vitest 和 Jest 构建的原生 GPU 测试环境，让 Node.js 直接运行真实 WebGL/WebGPU 测试，使用与 Chrome 相同的 ANGLE 和 Dawn，实现无需浏览器的快速渲染、截图与计算测试。

- 🚀 核心目标：摆脱 Puppeteer/Playwright 启动浏览器的慢重流程，让 GPU 测试像普通单元测试一样易写、快跑。
- 🧩 提供两个项目：`vitest-gpu` 包含 `vitest-environment-webgl-node`、`vitest-environment-webgpu-node`、`vitest-screenshot`；`jest-gpu` 包含对应 Jest 环境包。
- 🖥️ 切换测试环境后，`getContext('webgl2')`、`navigator.gpu.requestAdapter()` 可直接使用，Three.js、Babylon.js 等代码无需改动。
- ⚙️ 不是模拟或重实现：WebGL 基于 Chrome 的 ANGLE，WebGPU 基于 Chrome 的 Dawn，因此着色器编译和 GPU 后端结果与浏览器一致。
- 📸 Vitest 支持 `toMatchScreenshot` 图像基线：首次本地生成 `__screenshots__`，CI 缺失基线会失败，`vitest -u` 可更新。
- 🧪 Jest 环境通过 `readPixels` 读取像素，可配合 `jest-image-snapshot` 做图像快照，并同时提供 ESM 与 CommonJS 构建。
- 🧮 不止截图：还可测试计算着色器、GLSL/WGSL 编译错误、纹理上传、缓冲区布局和 readback 等真实 GPU 行为。
- ⏱️ 灵感来自 Three.js 的 PR：约四分之三示例移出 Chrome，最慢 CI 分片从约 15 分钟降至 6 分钟以内，约 2.6 倍加速。
- 🐧 macOS/Windows 使用预编译二进制；Linux CI 安装 Mesa 后可软件渲染，无需 CI 机器配备 GPU。
- 📦 两个项目均为 MIT 许可，开发由 Land of Assets 赞助；早期反馈积极，认为解决了安装复杂依赖、放弃测试的痛点。

---

### [](https://github.com/DoneDeal0/superdiff)

**原文标题**: [GitHub - DoneDeal0/superdiff: Superdiff provides a rich and readable diff for arrays, objects, code, text and coordinates. It supports stream and file inputs for handling large datasets efficiently, is battle-tested, has zero dependencies, and offers top-tier performance. · GitHub](https://github.com/DoneDeal0/superdiff)

Superdiff 是一个零依赖、高性能、经过实战测试的差异比较库，支持对象、数组、代码、文本和地理坐标，并能以流/文件方式高效处理大规模数据。
- 🚀 仓库为 DoneDeal0/superdiff，TypeScript 编写，约 1.1k stars、9 forks、82 commits。
- 🧩 提供 6 个核心函数：getObjectDiff、getListDiff、streamListDiff、getTextDiff、getCodeDiff、getGeoDiff。
- 📦 getObjectDiff：递归比较嵌套对象，支持忽略数组顺序和按状态/粒度过滤输出。
- 📋 getListDiff：识别数组新增、删除、更新、移动与相等项，支持重复值、对象和 referenceKey。
- 🌊 streamListDiff：通过流、文件或数组增量处理大列表，按 chunk 返回，支持 Worker 和事件监听。
- ✍️ getTextDiff：按字符、词或句子比较文本，支持 LCS、移动检测、大小写/标点忽略、locale 和高精度模式。
- 💻 getCodeDiff：先按行、再按 token 比较代码，保留空白，可报告缩进变化。
- 🌍 getGeoDiff：比较经纬度，返回距离和方向，支持 9 种单位、Haversine/Vincenty 精度和本地化标签。
- ⚔️ 竞品优势：相较 deep-object-diff、deep-diff、diff、microdiff，独有坐标 diff、流式处理、移动检测和输出细化等能力。
- ⚡ 性能：基准显示在大列表、对象、文本和代码 diff 中常优于竞品，并可线性扩展。
- 🧪 工程属性：零依赖、支持 ESM/浏览器/服务端，附带测试、基准和文档网站。
- 🤝 支持：欢迎 issue/PR，可赞助项目或获取高级支持，联系 talk.donedeal0@gmail.com。

---

### [发布 v4.3.0 · DoneDeal0/superdiff · GitHub](https://github.com/DoneDeal0/superdiff/releases/tag/v4.3.0)

**原文标题**: [Release v4.3.0 · DoneDeal0/superdiff · GitHub](https://github.com/DoneDeal0/superdiff/releases/tag/v4.3.0)

DoneDeal0/superdiff 发布 v4.3.0，核心是 `getCodeDiff`：用于比较两段代码并返回结构化差异，先按行、再对变更行做 token 级比较，并保留空白以报告缩进变化。

- 📦 仓库为公开项目 `DoneDeal0/superdiff`，约 1.1k Star、9 Fork。
- 🚀 最新版本为 `v4.3.0`，由 `github-actions` 于 9 月 19 日 09:29 发布，提交 `130bf4a` 带有 GitHub 验证签名。
- 🧩 从 `@donedeal0/superdiff` 导入 `getCodeDiff`，即可比较两段代码。
- 🧾 输出 `CodeDiff`：顶层 `type` 为 `"code"`，`status` 可为 `added`、`deleted`、`equal`、`updated`。
- 📄 输入为 `previousCode` 和 `currentCode`，类型均可为 `string | null | undefined`；比较文件需先读取文本：`getCodeDiff(await previousFile.text(), await currentFile.text())`。
- 📊 差异先按行展示，每行包含 `value`、`previousValue`、`line`、`previousLine`、`status`；更新行还会包含 token 级 `diff`。
- 🔢 行号从 1 开始；`line` 为 `null` 表示该行被删除，`previousLine` 为 `null` 表示该行是新增。
- 🔬 示例显示可识别常量名/值变化、函数体语句更新、新增 `return` 行，并标记 `equal`、`updated`、`added` 等状态。
- ⚠️ 页面部分资源加载出错，通知设置需登录后才能修改；页面还显示有 2 个资产。

---

### [](https://github.com/motdotla/dotenv)

**原文标题**: [GitHub - motdotla/dotenv: Loads environment variables from .env for nodejs projects. · GitHub](https://github.com/motdotla/dotenv)

dotenv 是一个零依赖模块，用于把 `.env` 文件中的环境变量加载到 `process.env`，遵循 Twelve-Factor App 方法论；它支持 Node.js、ESM 和 CLI，并借助 dotenvx 扩展变量展开、命令替换、加密、多环境同步与生产部署。

- 📦 **核心功能**：从 `.env` 读取配置并注入 `process.env`，让配置与代码分离。
- ⭐ **仓库数据**：约 20.5k Star、966 Fork、1,100 次提交，采用 BSD-2-Clause 许可证。
- 🚀 **基本用法**：`npm install dotenv --save`，创建 `.env`，尽早调用 `require('dotenv').config()` 或 `import 'dotenv/config'`。
- 🖥️ **CLI 支持**：可用 `npx dotenv run -- node index.js` 在运行命令前注入环境变量。
- 📁 **多文件加载**：CLI 支持 `-f/--file` 指定多个 `.env` 文件，默认第一个值优先，除非启用 `--override`。
- ⚙️ **CLI 选项**：支持 `-q/--quiet`、`--debug`、`--override`、`--fast`；`--fast` 使用更快的字符扫描解析器。
- 🌱 **环境变量默认值**：支持 `DOTENV_PATH`、`DOTENV_ENCODING`、`DOTENV_QUIET`、`DOTENV_DEBUG`、`DOTENV_OVERRIDE`、`DOTENV_FAST`，旧版 `DOTENV_CONFIG_*` 可作为回退。
- 🧩 **SDK 函数**：暴露 `config`、`parse`、`populate` 三个函数；`config` 读取并写入，`parse` 解析字符串或 Buffer，`populate` 自定义目标与来源。
- 🛠️ **config 选项**：支持 `path`、`quiet`、`encoding`、`debug`、`override`、`fast`、`processEnv` 等配置。
- 📝 **解析规则**：支持注释、空行、空值、单双引号、反引号、多行值；值中含 `#` 时需用引号包裹。
- 🧮 **默认不覆盖**：若环境变量已存在，默认跳过；使用 `override: true` 或 `--override` 才会覆盖。
- 🔐 **dotenvx 扩展**：变量展开、命令替换、`.env` 加密、多环境管理、生产部署和密钥同步推荐使用 dotenvx。
- 🌍 **多环境实践**：建议每个环境一个 `.env` 文件，如 `.env`、`.env.production`，避免继承式自定义配置。
- 📤 **提交 `.env`**：默认不应提交；若使用 dotenvx 加密，则可以安全纳入版本控制。
- ⚛️ **React/Webpack**：React 变量通常需加 `REACT_APP_` 前缀；Webpack 前端使用可能需 polyfill 或 `dotenv-webpack`。
- 🐳 **Docker 防护**：可用 dotenvx prebuild hook 防止把 `.env` 提交进 Docker 构建。
- 🔎 **调试建议**：设置 `debug: true` 可输出日志，帮助排查键值未生效或 `.env` 路径错误。
- 🔗 **相关工具**：dotenv-expand 用于变量扩展，dotenvx 用于加密与同步，VS Code 插件可隐藏密钥。

---

### [](https://github.com/motdotla/dotenv/blob/master/CHANGELOG.md#1800-2026-09-17)

**原文标题**: [dotenv/CHANGELOG.md at master · motdotla/dotenv · GitHub](https://github.com/motdotla/dotenv/blob/master/CHANGELOG.md#1800-2026-09-17)

dotenv 的 CHANGELOG 记录了该环境变量加载库从 1.0.0 到 18.0.3 的演进，重点包括 18.x 引入 CLI 与快速解析器、移除旧功能，17.x 面向 AI agent 与日志优化，以及历史上多次解析行为、Node 支持和 TypeScript 相关的重大变更。

- 📦 **项目热度**：dotenv 在 GitHub 上约 20.5k stars、966 forks，当前查看的是 master 分支的 `CHANGELOG.md`。
- 🚀 **18.0.0 核心新增**：新增 CLI（`dotenv run -- node index.js`）和快速解析器（`config({ fast: true })`、`--fast`、`DOTENV_FAST=true`，约 2 倍速）。
- 🧹 **18.0.0 移除/调整**：移除 tips、skill files、西班牙语 README、`.env.vault` 支持和 preloading；注入消息改到 stderr，推荐改用 CLI。
- 🛠️ **18.0.1-18.0.3 修补**：处理 config 日志中的 file URL、快速解析器边缘情况，并允许在 `.env` 中设置 `DOTENV_QUIET`。
- 🤖 **17.4.0 AI agent 支持**：新增 `skills/` 文件夹，含 `dotenv` 核心用法与 `dotenvx` 加密、多环境、变量展开技能，便于 AI 编码代理发现。
- 📝 **17.3.0 README 重构**：面向人类快速上手，同时更便于 LLM/agent 深入阅读，并增加 agentic future 章节。
- 🔇 **日志与静默**：17.2.0 支持 `DOTENV_CONFIG_QUIET=true`；17.0.0 将 `quiet` 默认改为 false，默认显示注入信息；16.6.0 开始默认记录 helpful message。
- 🧩 **16.x 功能扩展**：加入 `populate`、URL 作为 path、`.env.vault` 支持、`DOTENV_KEY` 选项、自定义目标对象等，其中 `.env.vault` 后在 18.0.0 移除。
- 💥 **15.0.0 重大解析变更**：支持多行解析，`#` 作为注释起点，移除 `multiline` 选项；含 `#` 的值需加引号。
- ⚙️ **14.x 配置增强**：新增 `override` 选项、`DOTENV_CONFIG_OVERRIDE`、内联注释支持，并在加载 `.env` 失败时记录错误。
- 📉 **旧 Node/类型支持变化**：8-12.x 逐步移除 Node 6/8/10 与 Flow 支持，增强 TypeScript 类型定义与 exports。
- 📜 **早期里程碑**：5.0.0 默认 path 改为 `path.resolve(process.cwd(), '.env')`；2.0.0 添加 CHANGELOG；1.0.0 移除多 `.env` 文件支持。
- 🔐 **生态方向**：项目推广 dotenvx，用于加密 `.env`、防止提交/构建泄露，并服务代理时代的密钥管理。

---

### [](https://github.com/tinylibs/tinypool)

**原文标题**: [GitHub - tinylibs/tinypool: 🧵 A minimal and tiny Node.js Worker Thread Pool implementation (38KB) · GitHub](https://github.com/tinylibs/tinypool)

Tinypool 是一个基于 Piscina 分叉的极简 Node.js Worker 线程池，安装体积仅 38KB、无依赖，主要服务 Vitest，支持 worker_threads 与 child_process，适合需要轻量线程池的场景。

- 🧵 Tinypool 是 Piscina 的友好分叉，目标是移除目标用户不需要的依赖和功能，使安装体积远小于 Piscina。
- 📦 核心特点：体积小（38KB）、极简、无依赖、使用物理核心而非逻辑核心，并支持 worker_threads 和 child_process。
- 🚫 不包含 utilization 和操作系统特定线程优先级设置；需要这些功能时建议使用 Piscina。
- 🧑‍💻 使用 TypeScript 编写，仅支持 ESM，要求 Node.js 18.x 及以上。
- ⚙️ 基本用法：创建 Tinypool 实例并指定 worker 文件，调用 pool.run() 执行任务，完成后用 pool.destroy() 终止空闲 worker。
- 🔄 通信支持：worker_threads 通过 MessagePort 和 transferList；child_process 通过 TinypoolChannel/channel，并可用 TinypoolWorkerMessage 过滤内部消息。
- 🛠️ Tinypool 特有构造选项包括 isolateWorkers、terminateTimeout、maxMemoryLimitBeforeRecycle、runtime、teardown、serialization。
- 🧹 池方法包括 cancelPendingTasks() 优雅取消待处理任务，以及 recycleWorkers(options) 等待当前任务完成后重建所有 worker。
- 🆔 导出 workerId：每个 worker 有不超过 maxThreads 的 id，可在 worker 内从 tinypool 导入，或通过 process.__tinypool_state__.workerId 获取。
- 🙌 项目由 Mohammad Bagher 维护，致谢 Vitest 团队和 Piscina；GitHub 约 1.6k stars、52 forks、8 watchers。

---

### [](https://github.com/tinylibs/tinypool/pull/141)

**原文标题**: [feat: accept a URL instance as filename by shaurya703 · Pull Request #141 · tinylibs/tinypool · GitHub](https://github.com/tinylibs/tinypool/pull/141)

overview summary
- 🚀 tinypool PR #141 已合并，核心变更是让 `filename` 直接接收 `URL` 实例，关闭 issue #109。
- 📝 此前 `filename` 只接受字符串，调用者需要手动写 `new URL('./worker.mjs', import.meta.url).href`；README 示例也都这样解包。
- 🔧 新实现让 `URL` 与等价字符串走同一套逻辑：`file:` URL 经 `fileURLToPath` 转为路径，其他 scheme 则用 `.href` 传给 worker 的 `import()`。
- 🧩 改动覆盖三处：`Options.filename` 和 `RunOptions.filename` 类型变为 `string | URL | null`；`maybeFileURLToPath` 接受 `string | URL`；`runTask()` 不再只接受字符串，支持每个任务的 URL。
- ✅ 新增 7 个测试，覆盖构造函数、`run()`、每任务 URL 覆盖字符串池文件名、`child_process` 运行时、非 `file:` scheme，以及非字符串/非 URL 仍被拒绝。
- 🧪 通过回退验证改动有效性：移除 `runTask` 守卫导致 2 个测试失败；移除 URL 分支导致 6 个测试失败；回退类型导致 6 行编译报错。最终 98 个测试通过，build、typecheck、lint 均干净。
- 📚 README 四个示例已改为直接传 `URL`，不再使用 `.href`；`worker_threads` 和 `child_process` 示例验证后仍输出 10。
- 👀 审查中 AriPerkkio 要求同步更新 README，之后批准合并；Windows 下 `file:` 路径处理依赖 `fileURLToPath`，作者未在 Windows 上实测。
- 🔀 最终以提交 `dd30ced` 合并进 `tinylibs:main`，8 项检查通过。

---

### [发布 v12.1.0 · nestjs/nest · GitHub](https://github.com/nestjs/nest/releases/tag/v12.1.0)

**原文标题**: [Release v12.1.0 · nestjs/nest · GitHub](https://github.com/nestjs/nest/releases/tag/v12.1.0)

NestJS 发布 v12.1.0（2026-09-23），这是最新版本，包含 18 个提交，由 Kamil Mysliwiec 发布，共 9 位提交者参与，重点集中在 Bug 修复与功能增强。  
- 🚀 版本发布：v12.1.0 为 Latest 版本，18 个提交合并至 master。  
- 🐛 core 修复：构造函数未重新声明时继承可选构造参数；元数据条目无效时命名模块。  
- 🧩 微服务修复：Redis 客户端连接失败后可重试；回调抛错时让所有待处理请求失败。  
- 🔄 core 增强：瞬时中间件后不再跳过后续中间件；保留路由处理器名称。  
- 🌐 新功能：支持全局前缀数组，并新增内置、适配器无关的 Cookies。  
- 🛡️ 安全增强：内置 CSRF 防护和安全响应头，覆盖 common、core、platform-fastify。  
- 📤 Fastify 增强：新增基于 @fastify/multipart 的文件上传拦截器；initHttpServer 尊重 forceCloseConnections。  
- 📅 common 修复：ParseDatePipe 默认值应用于每个缺失值。  
- 👥 贡献者：9 位提交者，包括 kamilmysliwiec、micalevisk、xia-chao、hktitof 等。  
- 📊 发布数据：2 个资产；社区反应包括 👍5、🎉2。

---

### [](https://github.com/nestjs/nest/pull/17834)

**原文标题**: [feat(common,core): add built-in, adapter-agnostic cookies by kamilmysliwiec · Pull Request #17834 · nestjs/nest · GitHub](https://github.com/nestjs/nest/pull/17834)

NestJS 合并 PR #17834，为框架引入内置、跨适配器的 Cookie 支持：无需再依赖 cookie-parser 或 @fastify/cookie，在 Express 与 Fastify 上行为一致，仅使用 Node 内置 crypto。新增装饰器、适配器方法、签名配置与安全校验，同时尽量保持向后兼容。

- 🍪 新增 `@Cookies(name?, ...pipes)` 与 `@SignedCookies(name?, ...pipes)` 参数装饰器，支持管道，可读取全部或单个 Cookie，以及签名验证通过的 Cookie。
- 🔌 `HttpServer` 增加可选 `setCookie()` / `clearCookie()`，由 `AbstractHttpAdapter` 基于 `appendHeader()` 统一实现，所有适配器均可获得，且同一响应可设置多个 Cookie。
- ⚙️ 新增应用选项 `cookies: { secret }`（`CookiesOptions`）；`setCookie(..., { signed: true })` 可签名，secret 数组会用第一个签名、全部验证以支持轮换。
- 🧩 Cookie 解析遵循 RFC 6265，按 `;` 和首个 `=` 拆分，去引号、安全百分号解码，重名时首个生效；仅在需要时解析并缓存，避免修改请求对象。
- 🧱 序列化会拒绝非法输入：名称需为 RFC 7230 token，`path`、`domain`、`maxAge`、`expires`、`sameSite`、`priority` 均会校验，防止头注入；值用 `encodeURIComponent` 编码。
- ⏱️ `maxAge` 以秒为单位，与 RFC 6265、`cookie`、`@fastify/cookie` 一致，不同于 Express `res.cookie()` 的毫秒；`path` 默认 `/`；`SameSite=None` 或 `Partitioned` 未配 `Secure` 会抛错。
- 🔐 签名采用 `cookie-signature` 格式 `s:value.HMAC-SHA256`，与 Express、cookie-parser、express-session 可互操作；使用常量时间比较，并针对全部 secret 验证。
- 🧯 `@SignedCookies` 验证原始 `Cookie` 头；无 Nest secret 时回退到 `req.signedCookies`；两者都没有则抛 500；空 secret 会在启动时报错。
- 🔄 兼容现有 cookie-parser 与 `@fastify/cookie` 设置；`@Cookies()` 返回其填充的 `req.cookies`。但 `@fastify/cookie` 的 `unsignCookie()` 因 `s:` 前缀无法验证 Nest 签名 Cookie，反向可以。
- ✅ 测试覆盖解析、序列化、签名与 `cookie-signature` 双向一致、请求辅助、适配器方法、路由参数工厂及 `cookies` 配置接线；集成测试在 Express 和 Fastify 上运行同一控制器。
- 📚 文档已更新，cookies 章节以内置 API 为主，并保留 cookie-parser / `@fastify/cookie` 兼容说明与 `maxAge` 单位迁移提示。
- ⚠️ 破坏性变更基本没有：`RouteParamtypes.COOKIES=14`、`SIGNED_COOKIES=15` 追加在枚举末尾；`setCookie` / `clearCookie` 在 `HttpServer` 上为可选；仅第三方适配器若已有同名方法可能冲突。

---

### [](https://github.com/nestjs/nest/pull/17836)

**原文标题**: [feat(common,core,fastify): built-in CSRF protection and security headers by kamilmysliwiec · Pull Request #17836 · nestjs/nest · GitHub](https://github.com/nestjs/nest/pull/17836)

NestJS 已合并 PR #17836，为 Express 与 Fastify 带来内置、可选、无新增依赖的 CSRF 防护和安全响应头；两者共用一个早期请求钩子，并同步更新了官方文档。

- 🛡️ PR #17836 已合入 nestjs/nest master，新增内置 CSRF 防护与安全响应头。
- ⚙️ 新增两个可选方法：`app.enableCsrfProtection()` 和 `app.useSecurityHeaders()`，在 Express 和 Fastify 上行为一致。
- 🔐 CSRF 采用 Go 1.25 `net/http.CrossOriginProtection` 思路：GET/HEAD/OPTIONS 放行；检查 `Sec-Fetch-Site` 是否为 `same-origin` 或 `none`；否则要求 `Origin` 主机与请求 authority 匹配。
- 🌐 无 `Sec-Fetch-Site` 和 `Origin` 时视为非浏览器客户端并放行；忽略 `X-Forwarded-Host`；Origin 比较不区分大小写并忽略默认端口。
- ✅ 支持 `trustedOrigins` 与 `exclude` 豁免；排除路由在 `app.init()` 解析，带全局前缀和 URI 版本，精确匹配、区分大小写、无尾斜杠。
- 🚫 非规范路径如 `//`、点段、`;`、`#`、`\`、编码的 `.` 或 `/` 永不匹配排除，保护失败时关闭以避免绕过。
- 🧩 两功能共用一个请求钩子；核心构建钩子，适配器通过新的可选 `HttpServer.registerSecurityHook()` 安装：Express 用 `use()`，Fastify 用 `onRequest`。
- ⏱️ 钩子在 Nest 中间件、body 解析、守卫、处理器之前运行，也覆盖 404；安全头先于 CSRF 检查写入，因此 403 也带安全头。
- 🛑 CSRF 拒绝会转为 `ForbiddenException`，由异常过滤器塑造 403；错误配置启动时失败，`app.init()` 后调用、重复调用或不支持适配器会抛错。
- 🧱 安全头默认值对齐 helmet 8.3.0：CSP、COOP、CORP、Origin-Agent-Cluster、Referrer-Policy、HSTS、X-Content-Type-Options、X-Frame-Options 等，并移除 X-Powered-By。
- 🧪 头选项按 helmet 命名校验；未知选项和旧别名如 `hsts` 被拒；CSP 指令与默认合并、可 Report-Only、安全序列化；`@Header()` 仍可按路由覆盖。
- 🔄 无破坏性变更：功能可选，未调用前行为不变；手写 `INestApplication` 实现或 mock 需要补充新方法。
- ⚠️ 限制：CSRF 不是 token 方案；状态变更的 GET 不受保护；Origin/Host 回退不感知 scheme，HTTP→HTTPS 可能失败开放；代理改写 Host 可能导致 403。
- 📌 其他限制：CORS 允许的 origin 不会自动信任；CORS 在钩子后注册时 403 可能无 CORS 头；`app.use()` 中间件若先运行可抢先结束响应；Fastify 排除匹配在 `rewriteUrl` 前；WebSocket 升级不覆盖。
- 🔮 后续计划：按请求 CSP nonce、双提交 token、按路由覆盖如 `@SkipCsrfProtection()`、`NestApplicationOptions` 中的相关标志、WebSocket 网关 Origin 检查、可信代理下支持 `X-Forwarded-Host`。
- 📚 文档已更新：CSRF Protection 与 Security headers 页面主推内置方法，`csrf-csrf`/`@fastify/csrf-protection` 与 `helmet`/`@fastify/helmet` 保留为替代方案。

---

### [](https://github.com/typegoose/mongodb-memory-server)

**原文标题**: [GitHub - typegoose/mongodb-memory-server: Manage & spin up mongodb server binaries with zero(or slight) configuration for tests. · GitHub](https://github.com/typegoose/mongodb-memory-server)

mongodb-memory-server 是 typegoose 维护的 MIT 许可开源工具，用于在 Node.js 中以编程方式启动真实 MongoDB 服务器，默认将数据保存在内存中，适合测试、模拟和隔离的集成测试。

- 🚀 项目定位：从 Node.js 程序内启动真实/实际 MongoDB 服务器，用于测试或开发模拟。
- 🧠 内存模式：默认数据保存在内存，单个新 mongod 进程约占用 7MB 内存。
- 📦 包类型：提供 mongodb-memory-server、mongodb-memory-server-global-*（npm install 时自动下载）和 mongodb-memory-server-core（不在 postinstall 下载），功能相同但默认配置不同。
- 💾 二进制管理：安装时下载 MongoDB 二进制到缓存；若找不到且 RUNTIME_DOWNLOAD 为真，首次启动会自动下载，后续运行会更快。
- 🌍 下载来源：从 https://fastdl.mongodb.org/ 按操作系统自动下载，支持 Linux、macOS、Windows；代理需配置 HTTPS_PROXY 或 HTTP_PROXY。
- 🔌 实例管理：每个 MongoMemoryServer 在空闲端口启动独立服务器，可同时启动多个；调用 stop() 或脚本结束时自动关闭。
- ⚙️ 主要 API：MongoMemoryServer.create() 创建并启动，getUri() 获取连接串，stop() 停止；MongoMemoryReplSet.create() 可创建副本集。
- 🛠️ 配置选项：支持 instance（port、ip、dbName、dbPath、storageEngine、replSet、args、auth）、binary（version、downloadDir、platform、arch、checkMD5、systemBinary）和 auth 等。
- 🔁 副本集：MongoMemoryReplSet 支持 count、name、auth、args、configSettings 等选项，可启动多个 mongod 成员。
- 🧪 测试集成：可与 MongoClient、mongoose 等 ODM/客户端配合，在 Jest 等测试框架中运行隔离集成测试，兼容可运行 NodeJS 的 CI。
- 🐳 特殊平台：Alpine 等无官方 MongoDB 二进制的平台，可通过 MONGOMS_SYSTEM_BINARY 指向手动安装的 mongod，或使用内置 mongod 的 Docker 镜像。
- 🐞 调试：可通过 MONGOMS_DEBUG=1 或 package.json 的 config.mongodbMemoryServer.debug 启用调试模式。
- 📋 系统要求：NodeJS 20.19.0+，TypeScript 5.9+；Linux 需要 lsb-core 或 /etc/os-release 等，并可能需要 libcurl4。
- 🏷️ 默认版本：默认下载 MongoDB 8.2.6，可用 MONGOMS_DOWNLOAD_URL 和 MONGOMS_VERSION 覆盖。
- 📜 项目状态：MIT 许可证，约 2.9k stars、191 forks、17 issues、1 PR；由 @nodkz、@AJRdev、@hasezoey 等维护。

---

### [](https://github.com/forwardemail/supertest)

**原文标题**: [GitHub - forwardemail/supertest: 🕷 Super-agent driven library for testing node.js HTTP servers using a fluent API.   Maintained for @forwardemail, @ladjs, @spamscanner, @breejs, @cabinjs, and @lassjs. · GitHub](https://github.com/forwardemail/supertest)

supertest 是一个基于 superagent 的 Node.js HTTP 测试库，通过链式 API 简化 HTTP 服务器断言；仓库由 forwardemail 维护，约 14.4k stars、783 forks、536 commits，采用 MIT 许可证。
- 🧪 核心定位：为 HTTP 测试提供高层抽象，同时允许使用 superagent 的底层 API。
- 📦 安装引用：通过 `npm install supertest --save-dev` 安装，并使用 `require('supertest')` 引入。
- 🌐 请求方式：可传入 `http.Server` 或函数给 `request()`；若服务器未监听，会自动绑定临时端口。
- ⚙️ 框架兼容：适用于任意测试框架，示例涵盖 Express、Mocha 以及无框架写法。
- 🔒 认证与 HTTP/2：支持 `.auth('username','password')`，并可通过 `{ http2: true }` 启用 HTTP/2。
- ✅ 断言 API：支持 `.expect(status/body/header/custom fn)`，断言按定义顺序执行，可在断言前修改响应。
- ⚠️ 错误处理：未添加状态码断言时，非 2XX 响应会作为错误传给回调；`.end()` 中失败的 `.expect()` 不会抛出，需重抛或传给 `done()`。
- ⏩ 异步写法：支持 `.then()` Promise 以及 `async/await` 语法。
- 📎 高级请求：可复用 superagent 的 `.write()`、`.pipe()` 等方法，并支持 multipart 文件上传。
- 🍪 Cookie 测试：`request.agent(app)` 可持久化 cookie；`cookies` 断言支持 `set`、`not`、`reset`、`new`、`renew`、`contain`，且可链式调用。
- 📚 其他信息：灵感来自 api-easy（去除 vows 耦合），采用 MIT 许可证，并由 @forwardemail、@ladjs 等组织维护使用。

---

### [GitHub - sql-formatter-org/sql-formatter：](https://github.com/sql-formatter-org/sql-formatter)

**原文标题**: [GitHub - sql-formatter-org/sql-formatter: A whitespace formatter for different query languages · GitHub](https://github.com/sql-formatter-org/sql-formatter)

SQL Formatter 是一个用于美化、格式化 SQL 查询的 JavaScript 库，支持多种 SQL 方言，并提供库、CLI、编辑器插件等使用方式；项目目前处于维护模式，主要修复问题，不再积极添加新功能。

- ⭐ 仓库为 `sql-formatter-org/sql-formatter`，公开项目，约 2.9k Stars、457 Forks、70 Issues、11 Pull Requests，采用 MIT 许可证。
- 🧩 核心功能是 pretty-print SQL 查询，最初从 PHP 库移植，但后续已大幅分化。
- 🗣️ 支持 BigQuery、ClickHouse、DB2、DuckDB、Hive、MariaDB、MySQL、TiDB、N1QL、PL/SQL、PostgreSQL、Redshift、SingleStoreDB、Snowflake、Spark、T-SQL、Trino/Presto 等多种方言。
- 🚫 不支持存储过程，也不支持将分隔符从 `;` 改为其他类型。
- 📦 安装方式：`npm install sql-formatter`，也可使用 yarn、pnpm、bun 等。
- 💻 作为库使用时，可调用 `format(sql, { language: 'mysql' })`，并配置 `tabWidth`、`keywordCase`、`linesBetweenQueries` 等选项。
- 🔕 可用 `/* sql-formatter-disable */` 和 `/* sql-formatter-enable */` 注释禁用某段 SQL 的格式化，禁用区间不会被解析。
- 🔁 支持占位符替换，例如通过 `params: ["'bar'"]` 处理 prepared SQL 语句中的 `?`。
- 🖥️ CLI 可通过 `npx sql-formatter` 使用，支持 stdin/stdout、输入文件、`-o` 输出、`--fix` 原地更新、`-l` 指定方言、`-c` 指定配置。
- ⚙️ 可读取 `.sql-formatter.json` 配置文件；主要配置包括 `language`/`dialect`、缩进、关键字大小写、换行、表达式宽度、参数类型等，`identifierCase` 为实验性，`indentStyle` 已弃用。
- 🌐 非 NPM 环境可克隆仓库后使用 `/dist` 文件，暴露 `window.sqlFormatter`；编辑器集成包括 VSCode、Vim、Prettier 插件，并提供 JSON Schema 和 ESLint 插件。
- 🛠️ 常见解析错误多因未指定 SQL 方言；Webpack/Babel 问题通常需支持 class properties；模板语法可用 `paramTypes.custom` 正则变通处理。
- 🧭 项目未来：开发处于维护模式，仅修复可行 bug；作者推荐新工具 `prettier-plugin-sql-cst`，基于 Prettier 布局算法，已支持 SQLite 和 BigQuery 等。
- 📄 贡献说明见 `CONTRIBUTING.md`，项目许可证为 MIT。

---

### [](https://fingerprint.com/use-cases/new-account-fraud-prevention/?utm_source=NodeWeekly09242026)

**原文标题**: [New Account Fraud Detection and Prevention | Fingerprint Device Intelligence](https://fingerprint.com/use-cases/new-account-fraud-prevention/?utm_source=NodeWeekly09242026)

核心目标是制止激励滥用，并识别那些通过推荐奖金、欢迎优惠和营销促销牟利的欺诈者。

- 🚫 制止激励滥用行为  
- 🕵️ 识别刷取推荐奖金的欺诈者  
- 🎁 发现滥用欢迎优惠的欺诈行为  
- 📣 防范营销促销被恶意套利

---

### [](https://select.supabase.com/?utm_source=newsletter&utm_medium=email&utm_campaign=nodeweekly&dub_id=IYpa4S8iVaYejoPU)

**原文标题**: [Select26 | Oct 2 | Supabase curated day of talks](https://select.supabase.com/?utm_source=newsletter&utm_medium=email&utm_campaign=nodeweekly&dub_id=IYpa4S8iVaYejoPU)

Supabase Select 26 是 Supabase 与业内顶尖开发者共同策划的一日线下演讲活动，聚焦开发者工具、Postgres 与真实产品构建；活动已售罄，可加入 Luma 候补名单。

- 🗓️ 10月2日在旧金山 555 20th Street 举行，仅限线下且需申请，票价 $256/人。
- 🎟️ 活动已售罄，官方引导通过 Luma 加入候补名单。
- 🎙️ 嘉宾阵容包括 Apple 联合创始人 Steve Wozniak、DeepLearning.AI 创始人 Andrew Ng、Supabase CEO Paul Copplestone/CTO Ant Wilson，以及 Y Combinator、OpenAI、Anthropic、Replit、Stripe、Postman 等公司代表。
- 🔍 核心看点：第一时间了解 Supabase 即将推出的功能、热门开发者工具公司动态，以及 Postgres 最新进展。
- 🧱 内容形式：主舞台炉边对话与 Build Stage 功能深度解析，强调真实产品如何被构建。
- 🤝 可在 Ask Supabase 展台直接向 Supabase 工程师提问，提出最难的问题。
- 🏢 由 Supabase 主办，设有首席赞助商与 After Party 赞助商，并遵循行为准则。
- 🔗 行动：通过 Luma 加入候补名单。

---

### [pnpm 12.6 | pnpm](https://pnpm.io/blog/releases/12.6)

**原文标题**: [pnpm 12.6 | pnpm](https://pnpm.io/blog/releases/12.6)

pnpm 12.6 于 2026 年 9 月 22 日发布，由 Zoltan Kochan 撰写，约 8 分钟阅读。该版本引入自动依赖去重、可重定位的 `node_modules`、`--save-types`、`package.yaml` 清单编辑、catalogs 中的 `file:`/`link:` 协议，并包含大量安装、解析、脚本、配置、Windows 与安全修复。

- 🚀 **自动去重**：启用 `autoDedupe: true` 后，安装时会去重兼容的依赖版本；若某版本满足所有范围，整个工作区使用该版本，冻结安装不会改动 lockfile。
- 📦 **可重定位 `node_modules`**：macOS/Linux 上 `pnpm install/run/exec` 可复用随项目移动或复制的 `node_modules` 与 bin shims，首次命令会检查并记录新位置。
- 🧩 **`--save-types`**：`pnpm add express --save-types` 会把 `@types/express` 保存到 `devDependencies`；已声明内置类型的包会跳过，可用 `saveTypes: true` 默认启用。
- 📝 **`package.yaml` 清单**：`pnpm add/update/remove/pkg/link/set-script/version` 可更新 `package.yaml`，并保留注释和键顺序。
- 🔗 **catalogs 支持 `file:`/`link:`**：目录项可使用 `file:` 和 `link:` 协议，相对路径从 `pnpm-workspace.yaml` 所在目录计算。
- 📋 **`pnpm tasks status`**：列出各并发组中运行和等待的任务；等待任务按优先级降序占用空位，同优先级按到达顺序；存在 `tasks` 脚本时用 `pnpm pm tasks status`。
- 🕒 **macOS Time Machine 排除**：`macosBackup.excludeModulesDir` 和 `excludeStoreDir` 可将新建 modules、virtual-store、package-store 目录排除备份，支持全局配置或环境变量。
- ➕ **小新增**：`pnpm add --tilde` 等价于 `--save-prefix=~`；`progress`/`--no-progress` 关闭依赖与下载进度；`pnpm cache prune` 清理旧注册表元数据缓存，`--dry-run` 可预览。
- 🔐 **安全修复**：POSIX bin shims 在 Cygwin/MSYS2/WSL2 从系统默认路径取 `cygpath`/`wslpath`，防止依赖重定向 shim；弃用警告不再输出通知全文；项目 `.npmrc` 凭据环境变量被忽略时会警告。
- 📥 **安装改进**：`--frozen-lockfile` 支持可选依赖不可解析被跳过、不再安装已从工作区移除项目的依赖；`pnpm ci` 在声明 `clean` 脚本时先清空 `node_modules`；`--force` 重新导入所有包并清理过时链接；根项目 `preinstall` 更早运行；`--prod` 不再下载仅 devDependency 可达的包；SSH 提示不再卡住；复用进行中的 tarball 下载。
- 🔍 **解析与链接**：安装/更新优先选择未弃用的最新匹配版本；`pnpm add <pkg>` 可复用 catalog 条目；裸路径 overrides 从工作区文件目录计算；peers 检查支持命名 registry；outdated/update 包含命名 registry 依赖并保留前缀；并发检查 overrides 加速 dedupe/install。
- 🏃 **脚本运行**：`pnpm run` 不再额外发送第二个 `SIGINT`，并可无终端转发终止信号；`pnpm test --filter` 正确转发；`deploy/rebuild/rb/setup` 优先同名 `package.json` 脚本。
- ⚙️ **配置修复**：编辑 `pnpm-workspace.yaml` 保留 YAML 锚点/别名；`pnpmfile` 按最近 `package.json` 加载 CommonJS/ESM；`readPackage` 钩子更新 lockfile；保留 CRLF；全局 `storeDir` 展开 `~/`。
- 🪟 **Windows 修复**：从长全局 virtual store 路径运行构建脚本；共享全局 virtual store 不再出现 `Access is denied` 或文件存在错误；Git Bash/MSYS2/Cygwin 下 `pn`/`pnpx`/`pnx`/`pnpm` 可运行；`pipeline --watch` 解析短路径以共享构建缓存。
- 🛠️ **其他修复**：`pnpm remove` 运行卸载生命周期脚本；`remove -r` 若依赖缺失则先失败；`update --peer` 更新 `peerDependencies`；`update -g` 跳过未变包；`publish` 允许 CI 中 detached HEAD；`store prune` 清理未引用与过期 `dlx` 缓存；`deploy` 在只读文件系统不触发安装；`sbom` 校验 SPDX；shell 补全建议包名/脚本；`--version` 不再创建临时文件。
- 📚 完整变更见 v12.6.0 release notes；标签为 release。

---

### [](https://linear.app/now/ci-bottleneck-reworked)

**原文标题**: [AI coding has made CI a bottleneck, so we reworked ours to keep up](https://linear.app/now/ci-bottleneck-reworked)

概述摘要  
Linear 为应对 AI 编码加速后 CI 成为瓶颈的问题，从基础设施、门禁任务、重复设置和测试执行四方面优化 CI。尽管测试套件自年初近乎四倍增长，PR 等待时间仍从超过 6 分钟降至略高于 5 分钟，每测试 runner 时间约减半；若未优化，当前套件约需 11 分钟。

- 🚦 AI 编码让代码交付更快，但验证速度未同步，CI 成为瓶颈并推高成本、拉长反馈等待。
- 🎯 优化目标：缩短 PR 等待 CI 的时间，并降低 runner 时间消耗。
- 🏗️ 升级基础设施：迁至第三方 runner，同类任务平均快 34%，tsc 快 52%；采用 tsgo 后 tsc 周中位数降 73%。
- 🧹 重写 lint 规则：用 AST 静态分析替代类型依赖，API lint 时间降 68%，全仓 lint 降 55%，并便于迁移 Oxlint。
- 🚪 优化门禁任务：按需 fetch、限制深度、稀疏无 blob checkout，change-detection 中位数 26→8 秒，p90 31→12 秒，最慢 138→37 秒。
- 🛡️ 自研 checkout action：重试与退避、约 30 秒低速超时中断、持久 git mirror 缓存，减少网络不稳导致的挂起。
- ⏱️ 移出关键路径：缓存标记写入改为不阻塞 job，API PR/合并队列省 42 秒；缓存未命中时必需检查约省 1 分钟。
- 📦 减少重复设置：CI 镜像预装 Postgres 客户端与构建头；pnpm 仅安装所需包，API install 44–73 秒→16–18 秒；重建比缓存 node_modules 更快。
- 🗂️ 避免重放未变设置：无 schema 变更时用快照+引导，数据库设置 12 秒→1–2 秒/容器；合并 7 个短检查为 2 个并发 job，每月省约 87,000 runner 分钟，占 CI 总用量 11.8%。
- 🧪 测试执行优化：拆分大测试文件；Vitest 分片 4→8，关键 job 快 19%、便宜 19%，最慢分片 5.25→4.33 分钟。
- 🔗 启用 isolate:false 的 opt-in 项目共享模块注册表：最大单项提升，月省约 17%；最慢分片约 300–379 秒→195 秒，API 分片 runner 时间 32.8→22 分钟/次。
- ⚠️ 共享状态风险最高：逐文件 opt-in、必要 teardown，不安全文件保持隔离，并更新 agent skills。
- 📈 分片受设置开销限制：优化后 8 分片可行；此前 4 分片 setup 8.3 分钟，之后 8 分片 setup 7.5 分钟。
- 🔄 CI 优化是持续工作：每周新增约 2,000 测试；未优化则当前套件约 11 分钟，接近如今等待时间两倍。

---

### [](https://sunilpai.dev/posts/the-senior-engineer-death-spiral/)

**原文标题**: [the senior engineer death spiral • Solving the decision problem](https://sunilpai.dev/posts/the-senior-engineer-death-spiral/)

本文是资深工程师给新入职高级工程师朋友的忠告：急于证明自己、追求晋升时，容易陷入“资深工程师死亡螺旋”——装成更高阶、做过于宏大的项目、长期不透明和秘密硬撑，最终倦怠或失败；更有效的做法是主动分享进展、以善意协作、先降半级成为最佳队友，用每日动量重建可靠性与声誉。

- 🌀 “死亡螺旋”常在换新工作、升职、接大项目或主动要更大项目时出现。
- 💼 朋友拿到高薪高级岗，却问如何每周干60–80小时、如何晋升；作者看出其冒名顶替感。
- 🎭 当事人试图扮演更高阶工程师，设计过度宏大的方案。
- 🔇 随后数周消失，站会只说“进展顺利、很快展示”，却没有实质产出。
- 📉 因久未交付而恐慌，秘密加倍工作、少睡、漏餐、抑郁，工作与私人关系受损。
- 🔥 最坏结局：倦怠休假、被PIP、被裁、辞职，觉得局面无法挽救。
- 🧠 作者亲历多次，现已能早期识别并主动跳出。
- 🌐 远程办公、疫情和编码代理让人更孤立，必须让别人知道你在做什么，避免被误解。
- 🤝 反直觉解法：假定他人善意；他们雇佣的是现在的你，不是半年后的你。
- 🧑‍🤝‍🧑 先“降半级”做最佳队友：修bug、接烦人任务、做杂活、写文档、帮助团队。
- 🐢 从结果导向转为动量导向：建立日常习惯；大项目靠慢而稳的每日推进，而非大爆发。
- 🧱 目标是可靠、修复关系、替队友和经理减负；建立信任后，更大的工作自然会来。
- 🏆 你在经营声誉，软件产出只是下游；保持动量，慢慢来。

---

### [HTML 元素周期表](https://blog.alena.rocks/en/artifacts/html-elements/)

**原文标题**: [Periodic Table of HTML Elements](https://blog.alena.rocks/en/artifacts/html-elements/)

该页面以“元素周期表”形式梳理 HTML Living Standard 中的 HTML 元素，统计其数量、规范章节、新增状态与元素类型，并展示各类别分布及部分元素详情。

- 📊 共收录 115 个 HTML 元素，覆盖 11 个规范章节。
- 🆕 其中 7 个元素是在 HTML5 之后新增的。
- 🕳️ 共有 13 个 void 元素，即没有内容、也没有闭合标签的元素。
- 🧩 按类别统计：Root 1、Metadata 6、Sections 16、Grouping 15、Text-level 29、Edits 2、Embedded 13、Tabular 10、Forms 15、Interactive 3、Scripting 5。
- 📚 Text-level semantics 数量最多，为 29 个，位于 §4.5。
- 🌳 `<html>` 是文档树的根元素，属于 §4.1、周期 I、组 1、Root 类；它正好包含 `head` 和 `body` 两个子元素。
- ⚠️ void 元素用虚线边框标记，表示无内容且无闭合标签。
- 🌐 `math` 和 `svg` 是 MathML 与 SVG 的入口点，正式属于其他命名空间。
- 📋 页面还列出 Metadata、Sections、Forms、Tabular、Embedded、Scripting 等大量具体元素，并提供 MDN 链接。

---

