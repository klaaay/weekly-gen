### [](https://nodejs.org/en/blog/events/nodejs-interactive-2026)

**原文标题**: [Node.js — Node.js Interactive 2026: A Recap](https://nodejs.org/en/blog/events/nodejs-interactive-2026)

Node.js Interactive 2026 在亚特兰大与 RenderATL 及亚特兰大科技周同期举行，两天议程聚焦开源维护、供应链安全、标准协作、平台工程和 AI 时代责任。会议指出，Node.js 的未来不只靠 API，更依赖维护者、互操作标准、安全平台、文档测试，以及开发者的持续贡献。

- 🎉 大会时隔多年回归，于 2026 年 8 月 12-13 日举办，强调 Node.js 生态的多元未来。
- 🧑‍🤝‍🧑 开源基础设施靠人：Robin Bender Ginn 指出 Node.js、Express 等依赖少量维护者，他们是“缺失的中间层”，需可持续支持。
- 🤝 标准协作推进互操作性：Joe Sepi 介绍 WinterCG 已转为 Ecma TC55，为服务端 JS 运行时定义最小通用 API。
- 🔐 供应链安全即身份安全：Kate Holterhoff 回顾 Shai-Hulud、Axios 等 npm 账户劫持事件，强调可信发布、短凭据、防钓鱼等防御，并指出 AI 是双刃剑。
- 📦 版本元数据扩展：Darcy Clarke 提出利用 SemVer 构建元数据作为向后兼容扩展点，并推出 semver.xyz 规范变体。
- 🛡️ 平台思维应对 AI 提速：Bekah Suttner Cheek 认为 AI 生成更多代码时，快速 CI、测试、回滚和默认安全护栏比以往更重要。
- 🔋 Node.js 内置能力增强：Matteo Collina 介绍内置 TypeScript、node:test、.env、fetch、node:sqlite、Permission Model 等；发布节奏改为每年一个 major。
- 🚀 QUIC/HTTP/3 还在路上：James Snell 介绍 node:quic 仍需实验标志，并提议统一 HTTP/1.1/2/3 服务器 API，提交 WinterTC 讨论。
- 📚 文档与测试是基础设施：doc-kit 重建文档管线，支持网页、man pages、llms.txt 等输出；@harperfast/integration-testing 提供并行、动态端口的真实进程集成测试。
- 🤖 AI 改变流程但不改变责任：多位演讲者讨论 MCP、规范驱动开发、INP/TTFT 等指标，强调开发者始终对系统负责，人类仍负责构想未有的创新。
- 👩‍💻 Code & Learn 收尾：与 Harper 合作，参会者在核心维护者指导下向 Node.js 提交真实贡献，践行开源协作精神。

---

### [](https://github.com/Agent-Field/pr-af)

**原文标题**: [GitHub - Agent-Field/pr-af: #1 open-source code reviewer on Code-Review-Bench · GitHub](https://github.com/Agent-Field/pr-af)

PR-AF 是一个基于 AgentField 构建的开源智能代码审查工具，在 Martian Code-Review-Bench 上排名第一。它以深度代码审查为核心，采用动态流水线架构，通过证据基础、复合漏洞合成和可证伪性门控等机制，提供高精度、低成本、可自托管的 PR 审查体验，并支持多种部署方式和模型灵活切换。

- 🏆 基准领先：在 38 个可运行 PR 上，使用 GLM-5.2 的 PR-AF 以 0.706 黄金召回率成为 42 个对比工具中排名第一的开源审查器，发现的有效问题约为领先商业工具的 3 倍。
- 💸 成本优势：每次审查成本约为闭源工具的 1/10，且模型灵活：常规 PR 用 DeepSeek 级模型，开源 CI 门禁用 GLM-5.2，高 stakes 审查用 Opus 级前沿模型。
- 📞 一键调用：支持通过 `af` CLI 或原始 HTTP API（curl）触发，自动在 GitHub 上发布带证据的 inline 评论，包含严重级别、文件行号、修复建议和证据链。
- 🧠 动态架构：不执行静态脚本，而是根据传入 PR 的拓扑动态编译审查维度（语义、机械、系统），并生成临时的专业化审查代理线程。
- 🔍 证据基础：在标记缺失校验等问题前，会从仓库提取真实调用方片段和导入上下文，验证发现是否扎根于代码，而非直接接受。
- 🧩 复合漏洞综合：跨文件聚类相关风险，评估孤立发现是否组合成更大的系统性问题，输出 compound_risk 信息。
- 🛡️ 可证伪性门：每条发现发布前会尝试否定它（安全行为、预期行为、现有缓解、弱证据），只有幸存者才会作为 GitHub 评论输出，极大降低误报。
- ⚙️ 部署灵活：支持 AgentField `af install`、Railway 一键部署、Docker Compose 本地运行，以及 GitHub Actions 零配置集成（通过 `pr-af` 标签触发，使用内置 GITHUB_TOKEN）。
- 🔑 配置简单：核心环境变量为 `OPENROUTER_API_KEY` 和 `GH_TOKEN`，另有模型选择、单次成本上限（默认 2 美元）、最大时长（默认 3600 秒）等可调参数。
- 📚 生态与实现：维护中的 Go 实现位于 `go/` 目录，Python 实现仍可用；属于 AgentField 生态系统，相关项目包括 SWE-AF 和 SEC-AF。

---

### [](https://nodejs.org/en/blog/release/v26.8.0)

**原文标题**: [Node.js — Node.js 26.8.0 (Current)](https://nodejs.org/en/blog/release/v26.8.0)

overview summary
Node.js 26.8.0 为当前版本，发布于 2026-08-26，包含多项新功能与性能优化，涉及加密、SQLite、Zlib、直方图、REPL 及网络模块等。

- 🔐 加密模块：更新根证书至 NSS 3.126，并支持 Cipher/Decipher 的 SIV 和 GCM-SIV 模式。
- 📊 直方图与性能：改进直方图实现，新增统计假设检验功能；优化 net.BlockList 性能。
- 💾 SQLite 增强：为 StatementSync 新增 close() 与 Symbol.dispose() 方法，并增加诊断通道与多项安全校验。
- 📦 Zlib 新增：引入 ZipEntry、ZipFile 和 ZipBuffer，支持 ZIP 归档处理，并强化头校验与防 DoS 保护。
- 🎨 REPL 改进：新增基础语法高亮功能，并优化历史记录加载行为。
- 🔧 工具与构建：更新多项依赖（zlib、simdjson、undici 等），改进构建脚本与 FIPS 模式支持。
- 🚀 性能与修复：优化 HTTP、流处理、URL 解析及文件系统相关性能，修复多处边界条件与崩溃问题。
- 📝 文档与类型：大量文档修正，新增多种内部绑定类型定义，完善 API 说明。

---

### [Zlib | Node.js v26.8.1 文档](https://nodejs.org/api/zlib.html#class-zlibzipbuffer)

**原文标题**: [Zlib | Node.js v26.8.1 Documentation](https://nodejs.org/api/zlib.html#class-zlibzipbuffer)

`node:zlib` 模块是 Node.js 内置的压缩功能库，实现了 Gzip、Deflate/Inflate、Brotli 和 Zstd 等算法，并基于 Streams API 构建，支持流式管道处理、HTTP 内容编码、单步压缩/解压以及实验性的 ZIP 归档操作，同时提供了丰富的配置选项、常量与同步/异步方法。

- 📦 **核心功能**：`node:zlib` 提供基于 Gzip、Deflate/Inflate、Brotli 与 Zstd 的压缩/解压能力，可通过 `import zlib from 'node:zlib'` 或 `require('node:zlib')` 访问。
- 🔄 **流式处理**：压缩与解压基于 Node.js Streams API，支持将源流经 zlib Transform 管道传输到目标流（如文件读写），也支持 Promise 版 `pipeline` API。
- ⚡ **线程池与性能**：除同步 API 外，所有 zlib API 均使用 Node.js 内部线程池；同时创建大量 zlib 对象可能导致显著的内存碎片化，建议缓存压缩结果以避免重复工作。
- 🌐 **HTTP 压缩应用**：可用于实现 HTTP 的 `gzip`、`deflate`、`br`、`zstd` 内容编码机制，文档提供了客户端请求与服务端响应的简化示例。
- 🧠 **内存调优**：deflate 内存需求约 `(1 << (windowBits + 2)) + (1 << (memLevel + 9))` 字节，inflate 约 `1 << windowBits` 字节；降低 `windowBits`/`memLevel` 可减少内存但通常降低压缩率，`level` 设置对速度影响最大。
- 💧 **Flushing 刷新**：在压缩流上调用 `.flush()` 可尽快输出数据，示例展示了通过定时 `flush()` 向客户端发送压缩的 HTTP 分块响应。
- 📊 **常量体系**：包含 zlib 常量（flush 值、返回码、压缩级别、策略）、Brotli 常量（`BROTLI_PARAM_*` 压缩参数与解码选项）及 Zstd 常量（`ZSTD_c_*`、`ZSTD_e_*` 与策略选项），可通过 `zlib.constants` 访问。
- 🗜️ **压缩类**：提供 `Deflate`、`DeflateRaw`、`Gzip`、`Inflate`、`InflateRaw`、`Gunzip`、`Unzip`、`BrotliCompress`、`BrotliDecompress`、`ZstdCompress`、`ZstdDecompress` 等类，以及基类 `ZlibBase`（支持 `bytesWritten`、`flush()`、`params()`、`reset()`）。
- 🗃️ **实验性 ZIP 归档 API**：新增 `ZipBuffer`（内存零拷贝视图）、`ZipEntry`（单个文件/目录条目）、`ZipFile`（磁盘随机访问视图），配套 `createZipArchive`/`createZipArchiveSync`/`zipFiles` 等函数，支持增删条目、流式读取、Zip64 自动切换与 `baseOffset` 偏移；并可通过 `setMaxZipContentSize()` 设置解压上限以防 ZIP 炸弹。
- ⚙️ **便捷方法**：提供 `deflate`、`deflateRaw`、`gzip`、`gunzip`、`inflate`、`inflateRaw`、`unzip`、`brotliCompress`、`brotliDecompress`、`zstdCompress`、`zstdDecompress` 等回调式方法，且每个方法都有 `*Sync` 同步版本。
- 🔁 **CRC32 校验**：`zlib.crc32(data[, value])` 计算 32 位循环冗余校验和，支持字符串（按 UTF-8 编码）与 Buffer 输入，适合数据传输错误检测而非加密认证。
- 🧪 **可迭代压缩（实验性）**：`node:zlib/iter` 模块提供与 `node:stream/iter` 配合的有状态压缩/解压转换（`compressGzip`、`decompressBrotli` 等），需启用 `--experimental-stream-iter` 标志，默认参数针对流式吞吐量调优。

---

### [](https://github.com/nodejs/node/pull/64591)

**原文标题**: [repl: add basic syntax highlighting by avivkeller · Pull Request #64591 · nodejs/node · GitHub](https://github.com/nodejs/node/pull/64591)

overview summary  
- 🎨 Node.js REPL 新增基础语法高亮功能，利用 `util.inspect.styles` 使配色与 inspect 输出保持一致。  
- ⚠️ 行为变更：当 `useColors: true` 时，REPL 会自动启用语法高亮。  
- 📦 新增核心模块 `lib/internal/repl/highlight.js`，补丁覆盖率高达 98.13%，项目覆盖率提升至 90.15%。  
- ✅ PR 获得 jasnell 批准，并合并至 main 分支（commit `4a5eb1c`），随后关闭。  
- 🔁 因未干净合并，需手动 backport 至 v26.x-staging，通过 PR #65267 完成回溯。  
- 📌 该特性被标记为 notable-change，并收录于 Node.js v26.8.0 正式版本的 Notable Changes 列表中。  
- 🧩 涉及标签包括 `repl`、`readline`、`needs-ci`、`author ready` 及 `backport-requested-v26.x`。

---

### [](https://nodejs.org/en/blog/release/v26.8.1)

**原文标题**: [Node.js — Node.js 26.8.1 (Current)](https://nodejs.org/en/blog/release/v26.8.1)

overview summary
- 🚀 Node.js 26.8.1 为当前（Current）版本，属于紧急修复的临时发布。
- 🔧 主要修复了 `node --version` 错误显示为 alpha 版本的问题。
- 📝 包含两个提交：回滚意外的 alpha 标识，以及修复 Nix 工具脚本。
- 💻 提供 Windows、macOS、Linux、AIX 及 ARM 等多平台安装包与二进制文件。
- 🔐 附带完整的 SHA256 校验和及 PGP 签名，确保下载安全。

---

### [Node.js 用户调查 2026](https://linuxfoundation.surveymonkey.com/r/nodejs-users-2026)

**原文标题**: [Node.js User Survey 2026](https://linuxfoundation.surveymonkey.com/r/nodejs-users-2026)

概述：这是一份包含5个问题的调查问卷，旨在收集受访者的地理位置、语言、职业组织类型、行业领域及组织规模等信息，并附有进度指示和“下一步”按钮。

- 🌍 调查第一个问题：当前居住的国家或地区（包含阿富汗、中国、美国等众多选项）
- 🗣️ 调查第二个问题：使用的主要语言（如英语、西班牙语、中文等）
- 🏢 调查第三个问题：所属组织的类型（学术机构、公司、非营利组织、自由职业等）
- 🏭 调查第四个问题：若在公司工作，所属的行业领域（如信息技术、医疗保健、金融等）
- 👥 调查第五个问题：组织的员工或成员数量（分为1-9到1000+等区间）
- 📊 问卷还显示当前进度为25%，并设有“下一步”按钮以供继续填写

---

### [](https://github.com/nodejs/node/pull/65392)

**原文标题**: [fs: implement glob natively by avivkeller · Pull Request #65392 · nodejs/node · GitHub](https://github.com/nodejs/node/pull/65392)

Node.js 的 PR #65392 提出将 `fs.glob` 从 JavaScript 实现改为 C++ 原生实现，目标是提升性能并保持与现有行为完全兼容。该实现参考了 minimatch 并吸收了多个高性能 glob 库的优化思路，基准测试显示在多数场景下性能大幅提升，尤其在异步和受限深度模式下优势明显。经过多轮评审、测试覆盖补充以及 CI 验证，最终获得多位维护者批准。

- 🔧 由 avivkeller 提交，将 `fs.glob` 用 C++ 原生重写，替代原有 JS 实现。
- 🔄 移植 minimatch 逻辑，并借鉴 Rust fast-glob (oxc) 和 picomatch 等实现的优化技巧。
- ⚡ 初始基准测试显示比旧实现快 2 倍以上，部分模式提升超过 150%。
- 💬 作者解释原生实现的优势：直接调用 libuv、避免 V8 中的字符串分配和 GC 开销，针对 Node.js 使用场景定制。
- 📊 isaacs 独立测试指出同步性能优于 node-glob，但异步性能仍较慢，建议继续优化缓存和并行化。
- 🧪 移植了 minimatch 的完整测试套件，确保向后兼容且无回归。
- ⚠️ 引入一个微小的 breaking change：包含全部 Unicode 字符的字符串会报错，因此标记为 semver-major。
- 👥 多位维护者（mcollina、jasnell、panva、anonrig）审核并批准，期间要求扩展测试覆盖并修复若干 bug。
- 🚀 最终基准测试全面大幅提升，`maxDepth=2` 的异步场景提升高达 500% 以上。

---

### [](https://github.com/nodejs/node/issues/65314)

**原文标题**: [Request for early feedback: Fetch server API · Issue #65314 · nodejs/node · GitHub](https://github.com/nodejs/node/issues/65314)

该 GitHub issue 由 Node.js 维护者 jasnell 发起，请求社区对新的 “Fetch Server API” 草案提供早期反馈。该 API 旨在成为运行时无关的服务器端 HTTP 接口，统一支持 HTTP/1.1、HTTP/2 和 HTTP/3，并解决现有 Fetch Request/Response 规范在服务器端的局限。目前草案尚未成为 TC55 正式工作项，预计在下次会议提交。

- 🚀 提出新的 “Fetch Server API” 草案，作为统一 HTTP API 战略倡议的一部分。  
- 🌍 目标是设计运行时无关的服务器 API，不绑定 Node.js，同时覆盖 h1、h2、h3。  
- 📄 草案渲染版和讨论仓库已公开（链接详见 issue）。  
- ⚠️ 指出现有 Fetch Request/Response 规范不适合服务器端使用，此提案旨在解决这些限制。  
- 🗓️ 目前还不是 TC55 官方工作项，计划在下次会议提交，希望提前收集反馈。  
- 🔍 征询 @nodejs/quic、@nodejs/http、@nodejs/http2、@nodejs/net 等相关团队意见。  
- 📚 提供多篇背景文章，介绍思路演进和 QUIC 等背景。

---

### [TermDOM | 使用HTML、CSS和DOM构建终端应用](https://termdom.org/)

**原文标题**: [TermDOM | Build terminal apps with HTML, CSS and the DOM](https://termdom.org/)

TermDOM 是一个用 HTML、CSS 和 DOM 构建终端应用的 JavaScript/TypeScript 库。它实现真实的 DOM/CSSOM，将网页技术渲染到终端字符网格，支持样式、布局、事件，并能直接复用浏览器生态。

- 🖥️ 渲染真实 DOM：直接绘制 DOM 节点到终端，节点变更自动重绘，无需自定义组件。
- 🎨 完整样式支持：CSS 级联、内联样式、颜色和文字装饰均转换为 ANSI 转义序列。
- 📐 浏览器级布局：实现 flexbox、grid、表格和盒模型，以字符单元格为长度单位。
- ⌨️ 原生事件系统：解码终端输入为 keydown、click、paste 等 DOM 事件，支持焦点管理。
- 🧩 生态兼容：无需修改即可使用 Prism 等浏览器库，也支持多数前端框架。
- 📊 示例丰富：涵盖纸牌游戏、动态图表、表单、语法高亮等应用场景。
- 🚀 快速开始：通过 npm 安装，提供指南、playground 和 GitHub 源码。

---

### [发布 TermDOM 0.1.5 · bikeshaving/termdom · GitHub](https://github.com/bikeshaving/termdom/releases/tag/v0.1.5)

**原文标题**: [Release TermDOM 0.1.5 · bikeshaving/termdom · GitHub](https://github.com/bikeshaving/termdom/releases/tag/v0.1.5)

TermDOM v0.1.5 发布，为终端环境带来更完整的 DOM/CSS 引擎实现，重点涵盖布局、交互、焦点、剪贴板及一致性修复。

- 🧱 新增 CSS Grid 支持：轨道尺寸、放置、对齐，以及简写解析和 CSSOM 解析。
- 📜 元素滚动：溢出裁剪、scrollTop/scrollLeft 限制、滚轮事件链，支持 scrollWidth/scrollHeight。
- 📋 剪贴板：引入 ClipboardEvent 和 DataTransfer，支持 paste 事件与用户激活门控。
- 🎯 实现 Selection.modify()，支持字符、单词和行粒度。
- 🔍 顺序焦点导航符合 HTML scope 模型，涵盖 shadow root、slot、delegatesFocus 和负 tabindex。
- 🚫 支持 user-select: none/text，正确约束选择和绘制高亮。
- 📐 新增 aspect-ratio（按单元格计数）以及 CSS 系统颜色映射到终端调色板。
- 🔧 <details> 获得用户代理 shadow tree，闭合时隐藏主体内容。
- 🔢 数字输入支持显式语法、输入过滤、箭头步进和 valueAsNumber 家族。
- 🔀 新增 Node.moveBefore 原子移动原语，含验证、范围更新和回调。
- 🧩 新增多个事件接口：MessageEvent、HashChangeEvent、StorageEvent、DragEvent、TextEvent 等。
- 🖱️ 几何与命中测试：elementsFromPoint、checkVisibility、Range.createContextualFragment 等。
- ⌨️ IME 组合输入：透传按键、显示音节并整体交付。
- 🎨 行为变更：<kbd> 渲染为粗体加下划线，:focus 等伪类支持 shadow 感知，isTrusted 更真实，initial 按规范解析。
- ⚡ 性能修复：大量 widget 的初始渲染从 43 秒降至 374 毫秒。
- ✅ 修复 focus()、全屏、requestAnimationFrame 链、网格序列化等细节问题。
- 📊 一致性测试：WPT DOM 套件共 95,064 个子测试通过，1,389 个失败，并记录了原因。

---

### [](https://aws.amazon.com/blogs/compute/introducing-public-preview-runtimes-on-aws-lambda-starting-with-node-js-26-and-python-3-15/)

**原文标题**: [Introducing public preview runtimes on AWS Lambda, starting with Node.js 26 and Python 3.15 | AWS Compute Blog](https://aws.amazon.com/blogs/compute/introducing-public-preview-runtimes-on-aws-lambda-starting-with-node-js-26-and-python-3-15/)

概述：AWS Lambda 推出公共预览运行时，首批支持 Node.js 26 和 Python 3.15，让用户在正式发布前体验并反馈，以优化运行时质量。

- 🚀 发布预览运行时：Lambda 首次提供预发布语言版本的公共预览，从 Node.js 26 和 Python 3.15 开始，可在所有 AWS 区域使用。
- 🎯 核心目的：通过真实工作负载提前收集反馈，在 GA 前解决潜在问题，减少正式发布后的破坏性变更风险。
- 🔄 自动升级：预览运行时使用与 GA 相同的标识符（如 nodejs26.x），GA 后函数自动过渡，无需修改配置。
- 📦 包含内容：基于上游最新预发布版本构建，无额外增强；支持托管运行时和基础容器镜像（带 preview 标签）。
- ⚠️ 注意事项：预览期间可能有破坏性变更，不适用 SLA 和技术支持，冷启动会向 CloudWatch Logs 输出警告，性能可能较慢。
- 💰 计费与功能：按标准 Lambda 费率计费，无额外费用；支持全部现有 Lambda 功能（如托管实例、持久化函数）。
- 💬 反馈渠道：通过 GitHub issue 提交反馈，可报告 bug、建议新功能或改进编程模型，也用于发布更新公告。
- 📅 GA 时间：预计上游稳定版于 2026 年 10 月发布，Lambda GA 目标在之后两个月内；Node.js 需等到 Active LTS。
- 🔧 使用方式：支持控制台、CLI、CloudFormation、SAM、CDK；CDK 暂用 Runtime 构造器指定运行时标识符。
- 👍 鼓励试用：欢迎用户部署测试套件并反馈，预览运行时今日已在所有区域上线。

---

### [](https://github.com/nodejs/node/blob/main/doc/contributing/ai-guidelines.md)

**原文标题**: [node/doc/contributing/ai-guidelines.md at main · nodejs/node · GitHub](https://github.com/nodejs/node/blob/main/doc/contributing/ai-guidelines.md)

overview summary
该指南规定了Node.js项目中AI工具的使用原则，核心是强调人类判断与责任，要求诚实披露AI辅助，并限制自动化及沟通中AI生成内容的使用。

- 🧠 AI工具永远不能替代人类判断，贡献者必须理解并对每个提议的变更负全责。
- 📝 若使用AI辅助生成贡献，需诚实披露，但披露不等于免除责任。
- 🏷️ 避免在提交信息中提及营利性商标或商业品牌，可匿名化或仅写在PR描述中。
- ⛔ 未经理解、测试和验证的AI生成代码可能导致PR直接关闭，重复违规者或被禁止贡献。
- 🤖 禁止自动工具直接开启PR，除非事先获得项目批准（如通过issue或工作流PR申请）。
- 📚 使用AI编码助理前需先熟悉代码库，用人类判断验证工具生成的分析与代码。
- ✅ 贡献者需对自己提交的每一行代码负责，确保遵守DCO和许可要求，并能解释任何改动。
- 🧪 测试必须经过人工验证，不得随意移除或修改现有测试，新测试需独立验证其正确性。
- 🕒 开启PR后需跟进反馈，不得中途消失；无法继续时应主动关闭PR。
- 🚫 不得使用AI认领“good first issue”任务，这些任务目的是让新人亲自动手学习。
- 💬 禁止在PR、issue或沟通渠道中粘贴完全由AI生成的消息，验证主张需引用实际代码、文档和规范。
- ✅ 语法和拼写检查工具可以接受，只要有助于提升清晰度和简洁性。

---

### [](https://blog.platformatic.dev/query-pipelining-in-node-postgres-2-3x-throughput-with-one-line-of-code)

**原文标题**: [Query Pipelining in node-postgres: 2-3x More Throughput](https://blog.platformatic.dev/query-pipelining-in-node-postgres-2-3x-throughput-with-one-line-of-code)

overview summary：node-postgres 在 pg 8.23.0 和 pg-native 3.9.0 中引入了可选的查询流水线功能，只需设置 `pipeline: true` 即可将吞吐量提升 2 到 3 倍。该功能通过批量发送多个独立查询、减少往返延迟来实现性能优化，并与原生客户端、池、PgBouncer 及命名预编译语句兼容，同时支持优雅关闭。  
- 🚀 一行启用：只需在 `Client` 或 `Pool` 配置中设置 `pipeline: true`，无需学习新 API。  
- ⚙️ 内部机制：使用三个队列（待发送、已发送等待响应、正在处理）批量将查询推到线缆，每个查询自带 Sync 消息，错误互不影响。  
- 📊 性能提升：简单查询 2.35 倍、参数化查询 1.50 倍、命名预编译语句 2.22 倍；本地网络延迟越高收益越明显。  
- 🖥️ JS 与原生对比：简单查询 JS 客户端更快（25,294 vs 21,524 qps），参数化查询原生客户端更快（20,792 vs 14,226 qps）。  
- 📦 原生客户端支持：`pg-native` 使用 libpq 的 PostgreSQL 14+ 流水线 API，但要求客户端库版本 ≥14。  
- 📝 命名预编译优化：同一语句仅发送一次 Parse，其余只发 Bind/Execute/Sync，避免重复解析。  
- 🔌 池集成：`Pool({ pipeline: true })` 启用后，需通过 `pool.connect()` 获取客户端；`pool.query()` 单条查询路径不受影响。  
- 🛡️ PgBouncer 兼容：支持 session、transaction、statement 模式；命名预编译需 PgBouncer 1.21.0+。  
- 🛑 优雅关闭：`client.end()` 会等待所有流水线查询完成后再关闭连接。  
- 💡 适用场景：适合互不依赖的批量查询（如加载多表数据、批量更新、分析报告）；依赖前序结果时必须顺序 `await`。  
- 📥 获取方式：`npm install pg@^8.23.0`（原生客户端 `pg-native@^3.9.0`），默认关闭，需显式开启。

---

### [你的模块在对你撒谎](https://blog.gaborkoos.com/posts/2026-08-14-Your-Modules-Are-Lying-to-You/)

**原文标题**: [Your Modules Are Lying to You](https://blog.gaborkoos.com/posts/2026-08-14-Your-Modules-Are-Lying-to-You/)

概述总结：本文深入剖析了ESM与CommonJS模块系统的核心差异，解释了为什么看似等价的代码会因模块机制不同而产生不同结果，涵盖绑定、求值顺序、循环依赖、跨模块互操作、双包发布陷阱及实用调试规则。

- 📦 ESM具名导入是“活绑定”，直接绑定到导出模块的变量；CommonJS解构则复制当前值，因此修改导出对象属性后，前者能看到更新，后者不能。
- 🔄 CommonJS返回`module.exports`的值，保留对象引用才能观察到后续属性变化；解构会丢失共享引用。
- ⏳ ESM静态导入会提升并在依赖图构建后按依赖顺序求值，`import`语句位置不影响执行顺序；CommonJS的`require()`按源码顺序同步执行。
- 🧩 ESM模块缓存按URL区分，查询字符串可创建多个实例；CommonJS缓存键基于解析后的模块路径，重复`require`返回同一实例。
- 🔁 循环依赖中，CommonJS可返回部分构造的导出对象；ESM可能在绑定初始化前访问而抛出`ReferenceError`，延迟读取可绕过但留下脆弱性。
- 🌉 ESM导入CommonJS时，`module.exports`作为默认导出可用，具名导出是静态检测的“快照”，后续属性变化不可见；CommonJS加载ESM需用动态`import()`返回命名空间对象，同步`require()`仅在无顶层await时可用。
- 🏷️ `__esModule`是转译器产生的互操作标记，不提供原生活绑定；不同构建工具可能生成不同的包装形状。
- 📦 双包发布（`"import"`与`"require"`条件指向不同文件）会导致同一包出现两个实例，类与共享状态不互通，需通过单一实现或设计共享外部状态来避免。
- ✅ 推荐使用ESM、保持具名导出、将可变状态私有化、保留CommonJS导出对象以观察变更、移除循环依赖、明确文件格式、分别测试两种入口。
- 🐛 调试时需依次确认：文件格式、导出映射选中的文件、返回值的形状（命名空间/导出对象/包装）、局部变量持有的是绑定还是复制值、求值是否完成、模块身份是否唯一、是否经过转译或打包。

---

### [](https://pnpm.io/blog/releases/12.0)

**原文标题**: [pnpm 12.0 | pnpm](https://pnpm.io/blog/releases/12.0)

pnpm 12 是基于 Rust 的完全重写版本，在兼容 pnpm 11 命令、设置与锁文件格式的基础上，引入了多项破坏性变更、新功能与修复。本文介绍了安装方式、关键变化及重要细节。

- 💻 安装：npm 的 `latest` 标签仍指向 pnpm 11，需通过 `pnpm self-update next-12` 获取 pnpm 12，也支持无需 Node.js 的其他安装方式。
- 🔑 Git 依赖现在被解析为“仓库身份”，统一使用主机规范 HTTPS URL，不再记录 SSH URL；未知主机保留原始 URL。
- ⚠️ `pnpm-workspace.yaml` 中无法识别的设置会报告错误或警告，并提示最接近的正确名称，不再静默忽略。
- 🔄 循环依赖图的锁文件生成被规范化，成为依赖图的纯函数，可产生字节一致的锁文件，且解析速度提升 2–3 倍、内存减少约 25%。
- 🖇️ 在 Linux 上，`packageImportMethod: auto` 默认优先使用硬链接（再回退到克隆），以加快安装速度；macOS 仍保持 clone 优先。
- ⛔ `engineStrict` 现在基于“边”而非子树判断失败，使不兼容依赖的安装限制更加严格。
- 🌍 新增“项目感知全局 bin”：全局安装的 node/deno/bun 可跟随当前项目固定版本，支持 `globalShims` 配置与信任提示。
- 📦 pnpm 可直接安装并运行其他包管理器（npm、Yarn、Bun 等），用于 git 依赖、`pnx` 命令和 shim，并验证签名。
- 🔄 Registry revisions：注册表可为已发布版本提供替换产物，锁文件可记录 `revision` 行，并支持 `pnpm update --patches` 刷新。
- 🎯 `pnpm init` 现在固定最新版 pnpm 而非当前运行版本；网络不可用或版本被拒时回退。
- ✅ `pnpm stage approve` 支持批量审批分阶段发布，使用单个一次性密码，并按依赖顺序处理。
- 🔍 新增 `audit.ignorePrune` 配置，`pnpm audit --fix` 可移除不再出现的忽略项。
- 🚫 全局修改类命令在 `sudo` 下运行会报错 `ERR_PNPM_SUDO_NOT_SUPPORTED`，只读全局命令不受影响。
- ☁️ 远程副作用缓存（概念验证）：可通过 `pnpr` 共享签名构建产物，避免本地执行生命周期脚本。
- 🧹 修复：兼容性数据库移除静态分析条目，避免多余 types 依赖；无上层可链接目录时默认 store 创建在项目内；`filterLog` hook 已弃用。

---

### [](https://pnpm.io/blog/whats-different-in-pnpm-12)

**原文标题**: [What's different in pnpm 12 | pnpm](https://pnpm.io/blog/whats-different-in-pnpm-12)

pnpm 12 是基于 Rust 的重写，兼容 pnpm 11 的命令、配置和锁文件格式，但带来了七项关键变化，包括项目感知的全局运行时、Git 依赖解析统一、包管理器安装逻辑调整、循环依赖锁文件稳定化、Linux 下默认硬链接优先、engineStrict 行为收紧，以及移除 `--resolution-only` 标志。

- 🔄 **项目感知的全局二进制**：全局安装的 `node`、`deno`、`bun` 会优先使用当前项目锁定的版本，无需单独版本管理器；由 `globalShims` 控制。
- 🌐 **Git 依赖解析统一**：同一仓库的不同写法（如 `owner/repo`、`github:`、`git+https:`、`git+ssh:`）都通过主机规范 HTTPS URL 解析，不再记录 SSH 地址，锁文件跨机器可移植；旧锁文件需用 `pnpm update <package>` 重新解析。
- 📦 **包管理器安装行为变化**：`pnpm add` 和 `pnx` 现在直接安装/运行真正的工具（如 Yarn 4/6、Bun、Node），而非同名 npm 包或包装器；全局安装的包管理器会遵循项目的锁定版本。
- 🔁 **循环依赖锁文件稳定化**：循环依赖按固定顺序切断边，锁文件仅由依赖图决定，重复安装或调整顺序可生成字节级一致的锁文件；循环多的 workspace 解析更快、内存更省。
- ⚡ **Linux 默认硬链接优先**：`packageImportMethod: auto` 在 Linux 上先尝试硬链接再尝试 reflink，btrfs 上安装速度更快；ext4 行为不变，macOS 仍以 clone 优先。
- 🛡️ **engineStrict 更严格**：当不兼容的包通过常规 `dependencies` 边被安装（即使整个子树挂在 `optionalDependencies` 下）也会导致 install 失败，而 pnpm 11 仅警告。
- ⛔ **移除 `--resolution-only`**：该标志已被删除，直接报错；需要检查 peer 依赖问题应使用 `pnpm peers check`。
- 📥 **安装方式**：pnpm 12 需从 `next-12` 标签安装，Homebrew 等包管理器尚未提供。

---

### [更好的认证 1.7](https://better-auth.com/blog/1-7)

**原文标题**: [Better Auth 1.7](https://better-auth.com/blog/1-7)

Better Auth 1.7 是一次重大版本更新，主要围绕 OAuth/OpenID Connect 扩展、MCP 授权、SCIM 企业身份、统一身份模型及设备访问等方向，带来多项破坏性变更与迁移要求。

- 🎉 发布 Better Auth 1.7，重点强化 OAuth/OpenID Connect、企业身份、MCP 授权和设备访问能力。
- 🔐 OAuth 提供者升级：每个受保护 API 可配置独立权限、令牌生命周期和签名策略，并加入 DPoP、后端注销、max_age、更强客户端认证及动态注册支持。
- 🧩 MCP 授权迁移至独立包 @better-auth/mcp，支持最新授权 Profile、官方 SDK v2、CIMD 文档认证和按 MCP 服务器绑定令牌。
- 📱 新增设备授权（RFC 8628），让 CLI、智能电视、游戏机等有限输入设备通过浏览器审批获取 OAuth 令牌。
- 👥 SCIM 服务全面重建：新增 Groups、组成员角色映射、更丰富的员工资料，并改善对 Entra ID、Okta、Google 的兼容性。
- 🔗 SCIM 与 SSO 精确桥接：通过稳定目录身份实现事务安全的用户关联，禁用或删除身份后阻止后续 SSO 登录。
- 🆔 引入统一身份模型：外部账号基于 provider + subject（OpenID sub、SAML NameID、OAuth account ID）识别，需审查并迁移现有数据。
- 🌐 OAuth 客户端改进：通用 OAuth 统一走社交登录路径，PKCE 默认开启，支持 Cognito、Entra ID domain hint、Google offline access 等配置。
- 🌍 其他改进：内置翻译增至 22 种语言、Drizzle Relations v2、稳定数据库 join、签名 session 缓存、passkey 注册创建会话、2FA 显式选择 OTP/TOTP 等。
- ⚠️ 破坏性变更：需同步升级所有 @better-auth/* 包并执行 schema 迁移；SCIM、OAuth 客户端和账号身份还需手动数据迁移，且 Cloudflare D1 无法支持 SCIM 事务。
- 🛠️ 迁移指南：使用 npx auth upgrade 升级，再运行 auth generate/migrate，并严格参照 1.7 升级指南处理手动步骤。
- 👏 感谢众多社区贡献者共同推动该版本落地。

---

### [](https://xyops.io/)

**原文标题**: [xyOps: The Next Generation of Cronicle | Open Source Ops Automation](https://xyops.io/)

overview summary
xyOps 是 Cronicle 的下一代开源运维与任务调度平台，延续 Cronicle 的调度理念，并加入可视化工作流、实时监控、告警上下文与自动响应能力。它完全自托管、BSD 许可、无遥测，支持从 Cronicle 平滑迁移，并提供免费与付费支持模式。

- 🚀 xyOps 是 Cronicle 的进化版，由原作者打造，定位为“调度、运行、监控、告警、响应”一体的运维系统。
- 🔓 完全开源（BSD 3-Clause），无功能锁定、无许可证密钥、无遥测，支持离线与隔离网络部署。
- 📅 调度灵活：支持日历、间隔、Webhook、自定义触发器和按需运行；可在一台、一组或整个服务器集群上执行。
- 🧩 可视化编排：支持分支、并行、合并、人工审批、重放与数据传递，并能复用子工作流。
- 📊 实时监控：服务器与任务统一观察，支持自定义指标、进程连接检查、历史性能对比和实时仪表盘。
- ⚠️ 告警上下文：告警触发时自动冻结服务器快照，从告警到根因定位只需两次点击，并可自动开票、调用 Webhook 或执行修复。
- 🔄 Cronicle 迁移：可导入 Cronicle 数据、保留兼容插件，并将多路事件转换为可视化工作流；新工人端 xySat 无需 Node.js。
- ⚡ 实际成效：Inkarnate 将高负载迁移从 AWS Lambda 移到 xyOps 后平均提速 2.4 倍，并曾在 75 台服务器上两小时内运行 75,000 个任务。
- 👨‍💻 支持模式：软件全部功能免费；付费计划提供工单支持、部署迁移指导、SSO/air-gap 协助，以及直接联系原作者 Joe 的服务。

---

### [GTKX：用于Linux的React框架](https://gtkx.dev/)

**原文标题**: [GTKX: The React framework for Linux](https://gtkx.dev/)

overview summary
GTKX 是一个专为 Linux 设计的 React 框架，基于 GNOME 栈和标准 Web 工具，让开发者使用 React 与 TypeScript 编写原生 Linux 应用程序。它提供 JSX 原生对象映射、热重载、完整类型支持、测试工具、AI 代理集成、Rust 核心以及一体化 CLI，并配有详细教程和开源社区。

- ⚛️ 用 React/TypeScript 构建 Linux 原生应用，底层基于 GNOME 技术栈与常规 Web 工具链。
- 🧩 所有 GObject 派生类均可作为 JSX 元素使用，属性直接映射到 JSX，支持声明式组合整个对象图。
- 🔥 具备 Fast Refresh 热重载，保存时即时更新运行窗口，无法修补的场景自动安全重启。
- 🔒 从 GIR 文件生成完整类型绑定，类、信号、枚举和属性在 IDE 中拥有全量类型提示。
- 🧪 提供类似 React Testing Library 的 GTK4 测试方案，可在 Vitest 中借助 headless Wayland 合成器运行虚拟显示测试。
- 🤖 内置 MCP 服务器，将实时应用暴露给 AI 代理，实现自动化测试、调试乃至自主开发。
- 🦀 原生 Rust 核心负责将 GLib/GObject 调用翻译为运行时原生架构，性能可靠。
- 📦 通过 gtkx.config.ts 声明所需的 GIR 库，自动生成对应命名空间的类型绑定，例如 Gtk、Adw、WebKit。
- 🏗️ 任意 GObject 都能写成 JSX，父子对象通过 props 嵌套，如 header bar 和 adjustment 也作为元素使用。
- 📁 应用是普通 Node 程序，支持使用所有 npm 包和 Node API，生态兼容无阻碍。
- 🛠️ 提供单一 CLI 管理完整生命周期：create、dev、build、deploy、codegen。
- 📘 文档包含完整 GNOME 应用教程（Tasks），涵盖自适应分屏、GSettings、通知及 Flatpak 打包。
- 🌍 项目遵循 MPL-2.0 开源许可，公开开发，欢迎贡献与反馈。

---

### [](https://stryker-mutator.io/)

**原文标题**: [Stryker Mutator](https://stryker-mutator.io/)

overview summary
Stryker 是一款开源突变测试工具，支持多种编程语言，提供丰富的突变类型、高速执行、灵活的测试运行器集成，并借助智能报告帮助开发者提升测试的有效性。

- 🧬 支持超过30种受控突变操作，全面覆盖常见代码变更模式
- ⚡ 通过代码分析和并行测试运行进程显著加速测试流程
- 🧪 不绑定特定测试运行器，可自由选用你偏好的测试工具
- 🌐 完全开源，由 GitHub 上的开源社区积极维护
- 💻 多语言支持，涵盖 JavaScript、TypeScript、C# 和 Scala
- 📊 利用智能报告定位存活突变，精准改进测试薄弱环节

---

### [](https://stryker-mutator.io/docs/mutation-testing-elements/supported-mutators/)

**原文标题**: [Supported mutators | Stryker Mutator](https://stryker-mutator.io/docs/mutation-testing-elements/supported-mutators/)

Stryker 系列（StrykerJS、Stryker.NET、Stryker4s）提供了多种标准化的突变测试算子，用于通过修改代码结构来验证测试的有效性。不同框架对各类突变算子的支持程度有所不同，涵盖算术、逻辑、字符串、正则表达式、方法调用等常见语法元素。

- ➕ 算术运算符突变：支持 `+` ↔ `-`、`*` ↔ `/`、`%` ↔ `*` 等，StrykerJS 和 Stryker.NET 支持，Stryker4s 不支持。
- 📦 数组声明突变：可移除数组构造器或数组字面量中的元素，例如 `[1, 2, 3, 4]` 变为 `[]`。
- 🔄 赋值表达式突变：包括 `+=` ↔ `-=`、`*=` ↔ `/=`、`&=` ↔ `|=` 等，部分仅特定框架支持。
- 🧱 块语句突变：通过 `BlockRemoval` 删除块语句内部内容，例如函数体变为空 `{}`。
- 🔘 布尔字面量突变：将 `true` 改为 `false`，或移除 `!` 取反操作。
- ✅ 条件表达式突变：将 `a > b` 改为 `true` 或 `false`，用于变异循环和 if 条件。
- ⚖️ 等式运算符突变：包括 `<` ↔ `<=`、`==` ↔ `!=`、`===` ↔ `!==` 等边界与否定变化。
- 🔣 逻辑运算符突变：支持 `&&` ↔ `||`，以及空值合并 `??` 与 `&&` 之间的转换。
- 🧩 方法表达式突变：各框架差异较大，例如 JS 的 `sort()`、`filter()`，.NET 的 `First()`/`Last()`，Scala 的 `filter`/`filterNot` 等。
- 🧪 对象字面量突变：仅 StrykerJS 支持，可移除对象属性，如 `{ foo: 'bar' }` 变为 `{}`。
- ❓ 可选链突变：StrykerJS 专属，将 `foo?.bar` 改为 `foo.bar`，移除可选调用保护。
- 🔍 正则表达式突变：使用 weapon-regex 生成变异，如 `^abc` 去掉锚点、字符类取反、量词删除等。
- 📝 字符串字面量突变：将非空字符串改为空字符串，或将空字符串替换为 `"Stryker was here!"`。
- ➖ 一元运算符突变：支持 `+a` ↔ `-a`。
- 🔺 更新运算符突变：支持 `a++` ↔ `a--`、`++a` ↔ `--a` 等前后缀增减变异。

---

### [](https://stryker-mutator.io/docs/stryker-js/getting-started/)

**原文标题**: [Getting started | Stryker Mutator](https://stryker-mutator.io/docs/stryker-js/getting-started/)

overview summary  
StrykerJS 的入门指南，介绍了从安装准备到运行突变测试的完整流程，并通过初始化工具简化配置。

- 📦 确保已安装 npm 和 Node.js，并在终端中进入项目根目录。
- 🚀 使用 `npm init stryker@latest` 命令安装并初始化 Stryker。
- ⚙️ 初始化过程中会询问一系列问题，需根据项目情况完成配置。
- ✅ 若提示安装 Stryker，选择“Yes”继续。
- 📝 初始化完成后，检查生成的 `stryker.config.mjs` 配置文件。
- 🧪 运行 `npx stryker run` 执行突变测试。
- 🐛 遇到问题时可使用 `npx stryker run --logLevel trace` 开启详细日志排查。
- 🔗 可查阅配置文档、故障排查指南，或通过 Slack 报告问题。

---

### [](https://svgo.dev/)

**原文标题**: [SVGO](https://svgo.dev/)

SVGO 是一款易用的 SVG 优化工具，既支持命令行也支持 JavaScript API，同时与许多主流工具集成，并且是一个欢迎社区贡献的开源项目。

- 🖥️ 使用简单：可通过命令行界面和 JavaScript API 操作，均配有帮助文档
- 🔗 集成广泛：Docusaurus、PostCSS、webpack 等工具已内置或提供集成
- 🌍 开源项目：欢迎提交 bug 报告、功能请求或发起 Pull Request

---

### [](https://github.com/svg/svgo/releases/tag/v4.1.0)

**原文标题**: [Release v4.1.0 · svg/svgo · GitHub](https://github.com/svg/svgo/releases/tag/v4.1.0)

概述：SVGO v4.1.0 发布，重点升级了 XML 解析器并引入更严格的校验，同时强化了 removeScripts 插件的安全性，修复多个安全漏洞，并更新了依赖项。

- 🚀 发布 v4.1.0：升级 SAX 解析器至 1.6.1，并引入更严格的 XML 校验规则
- ❌ 拒绝无效字符引用：包括控制字符（如 &#1;、&#xB;、&#x1F;）、UTF-16 代理项（如 &#xD800;）及非法 XML 码点（如 &#xFFFF;）
- ✅ 保留合法边界值：U+0020、U+D7FF、U+E000、U+FFFD 及至 U+10FFFF 的字符仍受支持
- 🐛 解析错误统一抛出 `SvgoParserError`，并注明“Invalid character entity”原因；行为变化可能使部分畸形 SVG 报错
- 🔒 加固 `removeScripts` 插件：过滤可执行的 `data:` HTML/XHTML/SVG 及 `vbscript:` 链接，保留 PNG 等惰性数据
- 🛡️ 清理 `<foreignObject>` 内容：移除 HTML 事件属性、`srcdoc` 及可执行 URL（action、data、formaction、href、src）
- ✂️ 识别命名空间前缀的 `<a>` 元素，并在检查 URL scheme 前去除 ASCII 制表符与换行，防止 `java&#9;script:` 绕过
- 🔗 修复安全公告：GHSA-4vpr-x523-8j87、GHSA-w27v-7q3p-w38r
- 📦 依赖更新：`css-select` 升级至 v6，`css-what` 升级至 v7，并适配新增选择器适配器
- 👥 维护变更：@TrySound 恢复为活跃维护者，感谢 @KTibow、@SethFalco、@XhmikosR 的贡献

---

### [发布 electron v44.0.0 · electron/electron · GitHub](https://github.com/electron/electron/releases/tag/v44.0.0)

**原文标题**: [Release electron v44.0.0 · electron/electron · GitHub](https://github.com/electron/electron/releases/tag/v44.0.0)

overview summary
Electron v44.0.0 是一个重大版本更新，升级了 Chromium 152、Node 24.18.1 和 V8 15.2，并引入多项破坏性变更、新功能、修复与性能优化。

- 🚀 升级 Chromium 152、Node v24.18.1、V8 15.2，带来底层改进与安全更新。
- ⚠️ 破坏性变更：移除 Linux Unity 桌面环境支持、32 位构建（Windows ia32/Linux armv7l）以及 macOS 12（Monterey）支持。
- 🔗 ANGLE 改为静态链接，不再随发行版提供 libEGL 和 libGLESv2 库。
- ✂️ clipboard 模块不再暴露给渲染进程，与 W3C Clipboard API 对齐。
- 🆕 新增 net.WebSocket（主进程 WHATWG 兼容 WebSocket 客户端）、webContents 缩放模式控制、跨平台窗口状态保存/恢复 API。
- 🔔 macOS 新增 Notification.remove()/removeAll()/removeGroup() 静态方法，并支持 MenuItem 徽标属性。
- 🐛 修复大量问题，包括 DevTools 网络面板、Linux 无边框窗口、ASAR 相关崩溃、Windows 尺寸损坏等。
- ⚡ 性能改进：启用 ThinLTO、嵌入式 Node.js 启动快照、沙箱渲染器冷启动时间减少约 35%。
- 📦 Linux 发行版体积减少约 37 MB，仅包含实际使用的语言资源。
- 📄 其他更新：更新 Squirrel.Mac 后端，并包含上游 Chromium/V8 修复。

---

### [](https://github.com/antoniomuso/lz4-napi)

**原文标题**: [GitHub - antoniomuso/lz4-napi: Fastest lz4 compression library in Node.js, powered by napi-rs and lz4-flex. · GitHub](https://github.com/antoniomuso/lz4-napi)

lz4-napi 是一个基于 Rust、napi-rs 和 lz4-flex 构建的 Node.js LZ4 压缩绑定库，提供异步和同步 API，支持字典、帧压缩与校验和，并附有基准测试与贡献指南。

- ⚡ 提供 Promise 与同步两套 API，支持 `compress`、`uncompress`、`compressFrame` 及对应 Sync 版本。
- 🔒 内存安全，由 Rust 与 napi-rs 驱动，并利用 libuv 线程池执行压缩任务。
- 📦 支持 Buffer、string、ArrayBuffer、Uint8Array 输入，可选字典参数。
- 🧩 帧压缩支持 `contentChecksum` 与 `blockChecksums` 选项，默认关闭，开启后可检测损坏帧。
- 📊 基准测试（M4 Pro 硬件）：压缩时 snappy 最快，lz4 接近；解压时 lz4 最快，大幅领先 gzip/deflate。
- 📁 安装方式简单：`npm install lz4-napi` 或 `yarn add lz4-napi`。
- 🛠 项目遵循 Conventional Commits，欢迎 Fork 并提交 PR，许可证为 MIT。

---

### [](https://github.com/pseitz/lz4_flex)

**原文标题**: [GitHub - PSeitz/lz4_flex: Fastest pure Rust implementation of LZ4 compression/decompression. · GitHub](https://github.com/pseitz/lz4_flex)

lz4_flex 是一个用 Rust 编写的高性能 LZ4 压缩/解压库，号称是 Rust 中速度最快的 LZ4 实现。它最初基于 redox-os 的代码，但现在已完全重写，支持块格式与帧格式，并提供安全/不安全代码的灵活配置。基准测试表明，在压缩和解压速度上，它优于 lz4 的 C 绑定、lz4_fear 和 snappy 等实现。项目还提供了 no_std 支持、模糊测试、Miri 检查以及多种语言绑定。

- 🚀 性能卓越：在基准测试中，lz4_flex 的解压速度最高可达 5973 MiB/s（66KB JSON 数据，unsafe 模式），压缩速度达 1615 MiB/s，明显快于 lzzz、lz4_fear 和 snap。
- 📦 支持两种格式：完整支持 LZ4 块格式和帧格式，块格式适合小数据，帧格式由多块组成，适合大数据。
- 🔧 灵活的特性开关：默认使用安全编码/解码，禁用默认特性可获得更高性能（`default-features = false`）。
- 🧩 no_std 支持：块格式支持 no_std 环境，可进一步禁用 `alloc`，压缩哈希表可放在栈上或由调用者提供。
- 📝 使用简单：提供了 `compress_prepend_size` 和 `decompress_size_prepended` 等 API，示例代码清晰易用。
- ⚙️ 测试工具丰富：项目包含基于 criterion 的基准测试、用于检测不安全代码问题的 Miri 检查，以及多个模糊测试目标（如损坏数据、缓冲区泄漏、往返一致性等）。
- 🌐 多语言绑定：已有 Node.js（lz4-napi）、Wasm（lz4-wasm）和 Python（safelz4）绑定。
- 📄 项目属性：MIT 许可证，约 615 星，60 fork，代码托管在 GitHub，仓库包含完整的 README、安全策略和变更日志。
- 🛠️ 迁移提示：从 v0.10 升级到 v0.11.1 时，只需移除 `checked-decode` 特性标志。

---

### [](https://github.com/grammyjs/grammY)

**原文标题**: [GitHub - grammyjs/grammY: The Telegram Bot Framework. · GitHub](https://github.com/grammyjs/grammY)

grammY 是一个用 TypeScript/JavaScript 编写的 Telegram Bot 框架，支持 Node.js 和 Deno，以易用性、强大功能和出色文档为特色，提供快速启动、丰富插件、社区支持和多种部署方式。

- 🤖 grammY 是 Telegram Bot 框架，支持 TypeScript/JavaScript，可运行于 Node.js 或 Deno。
- ⚡ 设计简洁易用，同时功能强大，始终与最新 API 保持同步，并具备出色的扩展能力。
- 🚀 快速开始：通过 @BotFather 获取 token，安装 `grammy` 包后，几行代码即可创建回声机器人。
- 📚 提供完整官方文档、API 参考和编辑器集成（如 VS Code），便于开发者查阅与学习。
- 💬 拥有友好的 Telegram 社区聊天，可解答问题、收集反馈并接受贡献。
- 🧩 插件生态丰富，可无缝集成 Web 框架与数据库，适应从入门到大规模场景。
- 🌐 全面支持 Deno 原生运行，并可通过 JavaScript 打包在浏览器或 Cloudflare Workers 中使用。
- 📦 npm 包附带 web bundle，支持 `import { Bot } from "grammy/web"` 快速接入。
- 👥 项目遵循 all-contributors 规范，拥有大量贡献者，欢迎任何形式的帮助。
- 🛠️ 提供示例仓库、Awesome grammY 列表、新闻频道等额外资源，助力实际开发。

---

### [](https://core.telegram.org/bots/api#august-24-2026)

**原文标题**: [Telegram Bot API](https://core.telegram.org/bots/api#august-24-2026)

Telegram Bot API 是面向开发者的 HTTP 接口，用于创建和管理 Telegram 机器人。文档涵盖从认证授权、获取更新、消息收发到富媒体、内联模式、支付、礼品、Passport 等完整功能，并包含多个 10.x 版本的重大更新，例如富消息、临时消息、社区模式、访客模式等。

- 🤖 Bot API 基于 HTTPS，每个机器人使用唯一 token 认证，请求地址格式为 `https://api.telegram.org/bot<token>/METHOD_NAME`，支持 GET/POST 及多种参数传递方式。
- 📡 获取更新有 `getUpdates` 长轮询和 webhook 两种互斥方式，更新类型包括消息、回调、成员变动、订阅变化等，并且更新只保留 24 小时。
- 💬 核心对象包含 User、Chat、Message 等，支持文本、照片、视频、音频、贴纸、位置、投票、清单等多种消息类型，也支持消息编辑、删除、转发和复制。
- 🆕 Bot API 10.x 版本引入富消息（Rich Messages），支持高度结构化文本、Markdown/HTML 格式、媒体块、表格、公式、可折叠引用和流式 AI 回复草稿。
- 👻 新增临时消息（Ephemeral Messages）功能，机器人可向指定用户发送仅该用户可见的消息，并支持临时命令和专用编辑/删除方法。
- 🌐 引入 Communities 社区概念，可将多个超级群组、频道和机器人关联在一起，并添加社区相关服务消息和字段。
- 🚪 支持访客模式（Guest Mode），机器人可在非成员聊天中接收消息并回复，还支持加入请求查询和 Web App 审批流程。
- 🖼 新增 Live Photo 实时照片类型，可发送带动画的照片并用于媒体组和付费媒体，也支持投票中嵌入媒体、链接等。
- ⌨️ 交互界面支持自定义键盘、内联键盘、禁用按钮、强制回复、Mini App 等，并提供丰富的按钮类型和样式。
- 📤 发送文件可用 file_id 免上传复用、URL 下载或 multipart/form-data 上传；本地 Bot API Server 可解除大小限制并允许自定义 webhook 端口。
- 🧩 内联模式允许用户通过 `@bot` 查询并分享文章、图片、视频、位置、发票等结果，支持 20 种结果类型。
- 💳 支付系统支持 Telegram Stars 和自定义货币，涵盖发票、订阅、退款、交易记录、星币余额及提现等完整流程。
- 🎮 提供游戏、Telegram Passport 身份验证、贴纸集管理、礼物系统等高级功能，同时支持业务账户管理和故事发布。
- 📊 群组管理功能全面，包括管理员权限、限制、封禁、邀请链接、主题管理、消息反应删除等。

---

### [](https://github.com/axios/axios)

**原文标题**: [GitHub - axios/axios: Promise based HTTP client for the browser and node.js · GitHub](https://github.com/axios/axios)

axios 是一个基于 Promise 的 HTTP 客户端，可同时用于浏览器和 Node.js，提供请求/响应拦截、数据转换、取消请求、自动序列化、进度追踪、限速、自定义适配器（如 Fetch）等丰富功能，并内置完整 TypeScript 类型定义。本文档摘要涵盖其核心特性、安装方式、API 用法、配置项、错误处理、取消机制、序列化方式及高级功能。

- 📦 **安装与导入**：支持 npm、yarn、pnpm、bun、Deno 安装，提供 CDN 引入；可通过 ESM `import` 或 CJS `require` 导入，兼容各类构建环境。
- ⚙️ **核心特性**：浏览器端发起 XMLHttpRequest、Node.js 发起 http 请求；支持 Promise、拦截器、请求/响应转换、取消 API、JSON 与表单序列化、XSRF 防护。
- 🔧 **请求配置**：支持 `url`、`method`、`baseURL`、`headers`、`params`、`data`、`timeout`、`auth`、`responseType`、`proxy`、`signal`、`maxContentLength`、`maxBodyLength`、`validateStatus` 等大量配置项。
- 📦 **响应结构**：响应包含 `data`、`status`、`statusText`、`headers`、`config` 和 `request`，便于在 `then` 或 `catch` 中读取。
- 🔄 **拦截器**：支持请求和响应拦截器，可同步或异步运行；提供 `runWhen` 条件执行，且请求拦截器按 LIFO、响应拦截器按 FIFO 顺序执行。
- ⚠️ **错误处理**：统一 `AxiosError` 结构，包含 `message`、`code`、`status`、`config` 等；内置 `ERR_BAD_REQUEST`、`ECONNABORTED`、`ERR_CANCELED` 等多种错误码；可用 `validateStatus` 自定义成功状态，用 `redact` 屏蔽敏感配置。
- 🛑 **取消请求**：支持现代 `AbortController` 和已弃用的 `CancelToken` 两种方式，可取消单个或多个请求；取消后返回 `CanceledError`。
- 📝 **序列化与表单**：支持 `application/x-www-form-urlencoded` 和 `multipart/form-data` 自动序列化，可提交文件、HTML 表单，并提供 `postForm`、`putForm`、`patchForm` 快捷方法。
- 📈 **进度与限速**：提供 `onUploadProgress` 和 `onDownloadProgress` 回调，可跟踪上传/下载进度；Node.js 下支持 `maxRate` 限速。
- 🗂️ **AxiosHeaders**：提供 Map 风格的 headers 操作类，支持 `set`、`get`、`has`、`delete`、`clear`、`concat` 等方法，并保留大小写与合并逻辑。
- 🚀 **Fetch adapter**：v1.7.0 起支持 `adapter: 'fetch'`，可通过 `env.fetch` 注入自定义 fetch（如 Tauri、SvelteKit），并支持进度捕获。
- 🧩 **其他亮点**：实验性 HTTP/2 支持、遵循 Semver、完整 TypeScript 定义、针对深度嵌套的 `maxDepth` 保护、以及 `sensitiveHeaders` 等安全增强。

---

### [发布 v7.6.0 · mongodb/node-mongodb-native · GitHub](https://github.com/mongodb/node-mongodb-native/releases/tag/v7.6.0)

**原文标题**: [Release v7.6.0 · mongodb/node-mongodb-native · GitHub](https://github.com/mongodb/node-mongodb-native/releases/tag/v7.6.0)

MongoDB Node.js 驱动发布 v7.6.0，移除了对 MongoDB 4.2 的支持，新增 KMS 请求的 HTTP 代理能力，并修复 ESM 打包时的 require 错误，同时优化批量写入性能。

- 🚀 发布 v7.6.0（2026-08-21），由 MongoDB Node.js 团队推出
- ⚠️ 移除对 MongoDB 4.2 及更低版本的支持，连接旧版本服务器将直接抛错
- 🔒 CSFLE 与 Queryable Encryption 新增 HTTP 代理支持，通过 `kmsConnectCallback` 自定义 KMS 连接
- 📈 改进 Intelligent Workload Management，仅在预期不加重服务器负担时重试过载错误
- 🔧 修复将驱动打包进 ESM 时 `ReferenceError: require is not defined` 的问题，`new MongoClient()` 现可正常工作
- ⚡ 优化批量写入性能：`insertMany` 和 `bulkWrite` 仅序列化文档一次，降低 CPU 占用和事件循环阻塞
- ✨ 其他更新：支持 `baseBackoffMS` 配置，并更新客户端背压退避逻辑
- 🐛 修复动态导入 `os` 模块的相关问题，确保跨构建环境兼容性

---

### [](https://github.com/LuanRT/YouTube.js/releases/tag/v18.0.0)

**原文标题**: [Release v18.0.0 · LuanRT/YouTube.js · GitHub](https://github.com/LuanRT/YouTube.js/releases/tag/v18.0.0)

YouTube.js 库发布了 v18.0.0 版本，主要包含一项破坏性变更、多项新功能以及若干错误修复，涉及评论线程、协作者支持、解析器新增类、新客户端支持等。

- 💥 破坏性变更：Comments.ts 新增对 threaded comments 的支持（#1194）
- 🆕 功能：为 Author 和 Playlist 添加协作者支持（#1203）
- 🆕 功能：LockupView 支持将 station 作为 content_type（#1229）
- 🧩 解析器：新增 VideoDescriptionYouchatSectionView 并修复相关解析警告
- 🧩 解析器：新增 ThumbnailOverlayAvatarStackView 类（#1200）
- 🧩 解析器：新增 TicketEvent 和 TicketShelf 类（#1205）
- 📦 protos：新增 ClipParams（#1215）
- 📱 Session：新增 VISIONOS 客户端（#1213）
- 🐛 修复：Comments.ts 支持 threaded comments（#1194）
- 🐛 修复：CommentView 处理 mutation 时未定义 endpoint 的问题（#1208）
- 🐛 修复：HTTPClient 为 ANDROID_VR 客户端添加 User-Agent 覆盖（#1184）
- 🐛 修复：Innertube#getHashtag 使用 URL-safe Base64 编码（#1211）
- 🐛 修复：MusicResponsiveListItem 匹配音乐时长的时间戳（#1230）
- 🐛 修复：SubscriptionButton 中 subscription_type 因拼写错误未设置，以及 text/subscribed 字段缺失问题
- 🐛 修复：VideoOwner 的解析问题
- 👍 社区反响：收到 🎉 和 ❤️ 等 reaction

---

### [首页 | node-x11](https://sidorares.github.io/node-x11/)

**原文标题**: [Home | node-x11](https://sidorares.github.io/node-x11/)

该库是一个纯 JavaScript 编写的 X11 协议实现，可直接与 X 服务器通信，并在浏览器中运行。

- 🧹 纯 JavaScript 实现，零依赖，无原生代码或 node-gyp，运行时无依赖。
- 🔌 直接通过 Unix 套接字或 TCP 使用 X11 线协议，无需额外中间层。
- 📦 支持全部 120 个核心请求和 34 个事件，以及 RENDER、RANDR、XFIXES、Composite、Damage、SHAPE、XTEST、XKB、XInput、MIT-SHM 等扩展。
- 🎮 完整支持 GLX 1.4 及供应商扩展，可在 Node.js 中创建 GL 上下文并渲染 OpenGL。
- 🌐 可插拔传输层支持任意双工流，因此也能在浏览器中运行（在线演示即将推出）。
- 🖥️ 直接与 X 服务器对话，通过 `npm install x11` 安装，单次调用即可连接。
- 🛠️ 每个核心请求都作为客户端方法提供，涵盖窗口、图形上下文、绘图和事件处理。
- ⚙️ 示例代码演示了创建窗口、映射窗口、创建图形上下文、监听事件并绘制文本的完整流程。

---

