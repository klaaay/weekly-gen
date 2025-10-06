### [Node周刊第594期：2025年9月30日](https://nodeweekly.com/issues/594)

**原文标题**: [Node Weekly Issue 594: September 30, 2025](https://nodeweekly.com/issues/594)

本期通讯在停更一周后恢复发布，涵盖技术动态与工具更新。

- 🎉 编辑团队结束休假恢复每周更新，持续至圣诞节
- ☁️ Cloudflare Workers 新增 Node.js HTTP 服务器兼容支持，深入解析标准库与文件系统实现
- 🐛 Electron 38.2/37.6/36.9.2 版本修复导致 macOS 系统卡顿的私有 API 兼容问题
- 🏗️ Frontend Masters 推出单体架构向 TypeScript 单体仓库重构课程
- 🔄 Node.js v24.9.0 与 v22.20 LTS 同步更新，涉及 http/sqlite/worker 模块及 OpenSSL 升级
- 🎂 AdonisJS 框架庆祝十周年，State of JS 年度调查启动
- 🛡️ GitHub 公布 npm 供应链安全加固计划，应对近期恶意软件攻击
- 💡 npx 命令使用技巧详解，包含本地/远程包执行特性
- 📚 技术文章推荐：findLast() 方法替代方案、BigInt 数据存储、eBPF 事件循环监控
- 🛠️ 新工具发布：Skia Canvas 3.0 图形渲染、Pompelmi 文件上传恶意软件扫描
- 🤖 GitHub Copilot CLI 公开预览版发布，新增 modern-tar/ffetch 等开发工具
- 📦 核心工具更新：pnpm 10.17/TypeBox 1.0/OpenAI Node 5.23.1 等版本迭代
- 🌐 生态动态：TC39 会议推进 Import Bytes 提案、Bun 1.2.23 发布、IINA 媒体播放器新增插件系统

---

### [Cloudflare Workers 中 Node.js 兼容性提升之年](https://blog.cloudflare.com/nodejs-workers-2025/)

**原文标题**: [A year of improving Node.js compatibility in Cloudflare Workers](https://blog.cloudflare.com/nodejs-workers-2025/)

过去一年Cloudflare Workers团队大幅提升了与Node.js生态系统的兼容性，通过原生运行时实现了核心Node.js标准库模块，使数千个npm包可直接运行。

- 🚀 **原生运行时支持** - 在TypeScript和C++层面原生实现Node.js API，替代原有的polyfill方案，提升性能并减少内存占用
- 🌐 **网络栈兼容** - 基于现有Sockets API和fetch实现了node:http、node:https、node:net等网络模块，支持Express/Koa等流行框架
- 💾 **虚拟文件系统** - 为node:fs模块实现内存虚拟文件系统，支持临时文件读写操作，可与Durable Objects结合使用
- 🔐 **完整加密功能** - 通过ncrypto项目完整实现node:crypto模块，支持哈希、加密、签名等密码学操作
- ⚙️ **进程环境支持** - 实现process.env环境变量访问、stdin/stdout/stderr流处理以及process.nextTick等核心API
- 📦 **模块化启用** - 通过nodejs_compat标志一键启用所有功能，也可按需单独启用/禁用特定模块
- 🔄 **持续贡献生态** - 团队成员积极参与Node.js开源项目开发，推动跨运行时兼容性改进

---

### [将Node.js HTTP服务器引入Cloudflare Workers](https://blog.cloudflare.com/bringing-node-js-http-servers-to-cloudflare-workers/)

**原文标题**: [Bringing Node.js HTTP servers to Cloudflare Workers](https://blog.cloudflare.com/bringing-node-js-http-servers-to-cloudflare-workers/)

Cloudflare Workers 现在支持 Node.js 的 node:http 客户端和服务器 API，使开发者能够直接在边缘环境中运行现有的 Express.js、Koa 等 Node.js 应用，无需重写代码即可享受零冷启动、自动扩展和更低延迟的优势。

- 🌐 **兼容 Node.js HTTP API**：在 Workers 环境中实现了 node:http 的核心功能，包括 http.get() 和 http.request() 等客户端 API
- ⚡ **基于 Fetch API 构建**：客户端实现基于 Workers 原生的 fetch() API，在保持兼容性的同时提供高性能
- 🔄 **服务器 API 桥接机制**：通过内部端口映射表将 Node.js 服务器连接到 Workers 请求处理模型，无需实际绑定 TCP 端口
- 🛠️ **两种集成方式**：提供 handleAsNodeRequest 手动集成和 httpServerHandler 自动集成两种方法，适应不同复杂度需求
- 🚀 **框架支持**：完全兼容 Express.js、Koa 等流行 Node.js 框架，可直接迁移现有应用
- ⚙️ **配置要求**：需要在 Workers 中启用 nodejs_compat 兼容性标志，且兼容日期需晚于 2025-08-15
- 🎯 **优势特性**：享受企业级网络管理、自动 TLS 处理、连接池维护等 Workers 原生优势
- 📋 **当前限制**：不支持 Agent API、Trailers、早期提示和 1xx 响应等高级功能

---

### [基于Electron的应用程序在macOS 26上引发严重系统卡顿问题 · Issue #48311 · electron/electron · GitHub](https://github.com/electron/electron/issues/48311)

**原文标题**: [Electron-based apps cause a huge system-wide lag on macOS 26 · Issue #48311 · electron/electron · GitHub](https://github.com/electron/electron/issues/48311)

Electron 应用在 macOS 26 系统中引发严重全局卡顿问题

- 🐛 用户反馈 Electron 应用在 macOS 26 系统上导致严重系统卡顿
- 🖥️ 受影响设备包括 M1 Max MacBook Pro 等 Apple Silicon 芯片设备
- 📉 表现为窗口移动/滚动卡顿，CPU和GPU使用率却保持低位
- 🔍 问题在同时开启多个Electron应用（如Discord和VS Code）时更为明显
- 🚫 最小化Electron应用可暂时缓解卡顿现象
- 🆚 该问题在macOS 15系统中不存在，仅出现在macOS 26版本
- 📋 维护人员建议用户通过Feedback Assistant向苹果提交错误报告
- 🔧 当前Electron版本为37.3.1，暂未确定具体解决方案

---

### [电子版发布](https://releases.electronjs.org/)

**原文标题**: [Electron Releases](https://releases.electronjs.org/)

Electron项目当前包含稳定版、预发布版和夜间构建版三个主要版本分支，各版本均基于Chromium和Node.js进行开发。

- 🚀 稳定版v38.2.0已于4天前发布，采用Chromium 140和Node.js 22.19
- 🔄 稳定版v37.6.0同步更新，搭载Chromium 138与Node.js 22.19
- ⚡ 稳定版v36.9.3昨日发布，集成Chromium 136及Node.js 22.19
- 🧪 预发布版v39.0.0-alpha.8今日推出，内置Chromium 142与Node.js 22.19
- 🌙 夜间构建版v40.0.0-nightly今日更新，同步最新Chromium 142引擎
- 🔧 当前活跃构建版本为基于main分支的v40.0.0-nightly.20251002

---

### [Node.js](https://nodejs.org/en/blog/release/v24.9.0)

**原文标题**: [Node.js](https://nodejs.org/en/blog/release/v24.9.0)

Node.js v24.9.0 版本发布，主要包含 HTTP 升级控制、SQLite 功能增强、Worker 堆分析 API 等新特性，同时进行了多项性能优化和错误修复。

- 🚀 HTTP 模块新增 shouldUpgradeCallback，允许服务器控制 HTTP 升级流程
- 🗃️ SQLite 支持标记模板并优化了 ERM 支持，导出 Session 类
- 📊 Worker 线程新增堆分析 API，便于内存性能分析
- 🔧 加密模块改进 X509Certificate 的 signatureAlgorithm 暴露和 Promise 处理
- 🌐 网络模块优化了 IPv6 代理处理和 HTTP token 检查性能
- 📦 构建系统更新了 OpenHarmony 支持并优化了 ESLint 规则打包
- 🛠️ 核心代码重构了字符串处理和 Eternal 设置逻辑，提升运行效率
- 📚 文档更新了安全升级策略和 V8 快速 API 使用指南
- 🐛 修复了 REPL 大字符串粘贴性能、SQLite 会话崩溃等多个问题
- 🔄 依赖项升级至 OpenSSL 3.5.3 和 Undici 7.16.0

---

### [Node.js](https://nodejs.org/en/blog/release/v22.20.0)

**原文标题**: [Node.js](https://nodejs.org/en/blog/release/v22.20.0)

Node.js v22.20.0 (LTS) 版本发布，主要更新了 OpenSSL 至 3.5.2 以延长支持周期至 2027 年，并包含多项功能增强和错误修复。

- 🔐 OpenSSL 升级至 3.5.2，确保长期支持兼容性
- 🌐 HTTP/2 支持原始头数组，提升网络处理能力
- 📦 SEA（Single Executable Applications）新增 execArgv 配置和扩展支持
- 🔧 流处理增加 Brotli 压缩支持，优化数据传输效率
- 🧪 测试运行器支持对象属性模拟，增强测试灵活性
- 👷 Worker 线程新增 CPU 性能分析 API，便于多线程调试
- 📄 文档和类型定义更新，提升开发体验
- 🐛 多项错误修复和性能优化，增强稳定性

---

### [AdonisJS - 功能齐全的Node.js网页框架](https://adonisjs.com/)

**原文标题**: [AdonisJS - A fully featured web framework for Node.js](https://adonisjs.com/)

AdonisJS是一个功能丰富的Node.js全栈框架，提供类型安全、现代化工具链和开箱即用的开发体验，让开发者能够快速构建高性能的Web应用。

- 🛡️ 提供类型安全的API设计，支持智能提示和自动导入功能
- 📦 基于ES模块构建，采用现代化JavaScript标准
- ⚡ 内置高性能验证库和HTTP服务器，速度媲美Fastify
- 🎯 核心框架包含完整功能集，无需额外组装依赖包
- 🔧 集成配置管理、路由、中间件、文件上传等基础功能
- 🧪 提供世界级测试体验，支持浏览器测试、API测试和邮件模拟
- 📚 拥有大量官方维护的扩展包，涵盖ORM、认证、缓存等场景
- 💬 开发者社区高度评价，认为其文档完善、体验接近Laravel
- 🌐 支持多语言、实时通信、健康检查等企业级功能
- 🛠️ 配备强大的CLI工具和IoC容器，提升开发效率

---

### [AdonisJS十年历程——个人回顾与未来展望](https://adonisjs.com/blog/a-decade-of-adonisjs-and-the-future)

**原文标题**: [10 Years of AdonisJS — A Personal Reflection and What’s Next](https://adonisjs.com/blog/a-decade-of-adonisjs-and-the-future)

AdonisJS框架已走过十年历程，从解决Node.js全栈开发痛点的初心，逐步发展成为深受全球开发者信赖的开源项目。它并非一夜成名，却凭借纯净的架构设计和活跃社区的支持持续成长。项目创始人宣布将全职投入框架开发，并通过商业化路径确保项目长期发展。

- 🎉 项目成立十周年，从解决Node.js开发痛点逐步演变为成熟框架
- 🌱 坚持渐进式发展路线，依靠热情社区而非商业资本推动
- ⚖️ 持续平衡功能迭代、工具更新与可持续发展之间的挑战
- 🚀 以现代无技术债为核心优势，拒绝遗留包袱保持架构纯净
- 💼 创始人宣布全职投入，通过赞助计划与商业版本实现长期运营
- 👥 专注服务个人开发者与小团队，助力创意快速产品化
- 🔮 未来将通过AdonisJS Insiders赞助计划与Plus商业版本加速发展

---

### [JavaScript 2025 现状](https://survey.devographics.com/en-US/survey/state-of-js/2025)

**原文标题**: [State of JavaScript 2025](https://survey.devographics.com/en-US/survey/state-of-js/2025)

JavaScript生态系统已趋于稳定，前端框架创新放缓，竞争转向元框架与构建工具领域。

- 🎂 前端框架进入稳定期，九年历史的Svelte已称得上"老牌"
- ⚔️ 元框架竞争白热化，Astro正挑战Next.js的领先地位
- 🛠️ 构建工具领域Vite即将超越webpack成为新标准
- 🦀 Rust生态可能孕育下一代颠覆性技术
- 📊 2025年度JavaScript现状调查于10月1日至11月1日进行
- ⏱️ 调查耗时约15-20分钟，面向所有JavaScript/TypeScript使用者
- 🌍 调查结果将公开，助力开发者技术选型与浏览器厂商决策
- 🤝 由Devographics联合全球志愿者共同运营，支持多语言翻译

---

### [我们的npm供应链安全强化计划 - GitHub博客](https://github.blog/security/supply-chain-security/our-plan-for-a-more-secure-npm-supply-chain/)

**原文标题**: [Our plan for a more secure npm supply chain - The GitHub Blog](https://github.blog/security/supply-chain-security/our-plan-for-a-more-secure-npm-supply-chain/)

GitHub针对npm供应链安全威胁推出强化措施，包括强制双因素认证、细粒度令牌和可信发布机制，以应对近期恶意软件攻击并重建开源生态系统信任。

- 🚨 近期npm注册表遭遇大规模账户劫持攻击，自复制蠕虫通过受维护者账户传播恶意软件
- 🛡️ GitHub已移除500+受感染包并阻断恶意软件传播模式
- 🔐 即将实施强制双因素认证和7天有效期的细粒度令牌
- 📦 大力推广可信发布机制以替代传统API令牌
- ⚙️ 逐步淘汰经典令牌和TOTP双因素认证，转向FIDO认证
- 📋 维护者可立即启用可信发布、强化发布设置并采用WebAuthn认证
- 🌐 强调生态系统安全需要开发者共同参与和持续警惕

---

### [获取失败](https://nodeweekly.com/link/174923/web)

**原文标题**: [Failed to retrieve](https://nodeweekly.com/link/174923/web)

无法总结：获取内容失败，状态码 403。

---

### [npm 包的可信发布 | npm 文档](https://docs.npmjs.com/trusted-publishers/)

**原文标题**: [Trusted publishing for npm packages | npm Docs](https://docs.npmjs.com/trusted-publishers/)

可信发布允许通过CI/CD工作流直接发布npm包，使用OpenID Connect认证替代传统令牌，提升安全性并自动生成来源证明。

- 🔐 通过OIDC建立npm与CI/CD平台的信任关系，消除长期令牌泄露风险
- ⚙️ 支持GitHub Actions和GitLab CI/CD云托管运行器，需npm CLI 11.5.1+
- 📝 配置步骤：在npmjs.com添加发布者+在CI工作流添加OIDC权限
- 🛡️ 强烈建议启用后限制令牌访问，选择"要求双因素认证并禁用令牌"
- 🔄 迁移时先验证可信发布再撤销旧令牌，确保发布流程不间断
- 📦 公有仓库发布公有包时自动生成来源证明，私有仓库不支持此功能
- ⚠️ 当前限制：仅支持云托管运行器、每个包仅限一个发布者配置
- 🔧 故障排查重点检查工作流文件名匹配、OIDC权限设置及运行环境

---

### [加强npm安全性：认证与令牌管理的重要更新 - GitHub更新日志](https://github.blog/changelog/2025-09-29-strengthening-npm-security-important-changes-to-authentication-and-token-management/)

**原文标题**: [Strengthening npm security: Important changes to authentication and token management - GitHub Changelog](https://github.blog/changelog/2025-09-29-strengthening-npm-security-important-changes-to-authentication-and-token-management/)

npm正在实施安全改进措施，包括调整令牌生命周期、淘汰经典令牌及升级双因素认证方式，以增强生态系统安全性。

- 🔐 精细令牌默认有效期缩短至7天，最长90天
- 🚫 逐步淘汰经典npm令牌，改用精细权限令牌
- 🔄 新TOTP双因素认证设置将被禁用，推荐使用WebAuthn
- 📅 变更分阶段实施：10月初生效新令牌规则，11月中旬停用经典令牌
- 🤝 推荐采用信任发布机制替代长期令牌
- 📚 提供文档、社区讨论和技术支持协助过渡
- ⚠️ 现有TOTP配置暂可继续使用但将被逐步淘汰

---

### [掌握NPX：npm与Node.js高手的速查手册](https://www.nodejs-security.com/blog/mastering-npx-cheatsheet-npm-nodejs-power-users)

**原文标题**: [Mastering NPX: A Cheatsheet for npm and Node.js Power Users](https://www.nodejs-security.com/blog/mastering-npx-cheatsheet-npm-nodejs-power-users)

NPX是Node.js生态中一个强大的命令行工具，主要用于直接执行npm包而无需全局安装，适用于一次性命令或测试场景。

- 🚀 无需全局安装即可运行npm包（如`npx create-react-app my-new-app`）
- 📍 使用`-p`标志查找可执行文件路径（如`npx -p shellcheck which shellcheck`）
- 🔧 支持指定Node.js版本运行命令（如`npx -p node@14 <command>`）
- 💻 可直接执行GitHub Gists脚本（`npx gist <gist-id>`）
- 🌡️ 支持传递环境变量（如`MY_VAR=value npx <package-name>`）
- ⚠️ 需注意安全风险，建议使用npq等工具审计第三方包
- 🔄 自动清理临时缓存，保持系统整洁
- 🔒 支持私有包执行（需配置npm认证）

---

### [停止使用.reverse().find()：认识findLast() - 马特·史密斯](https://allthingssmitty.com/2025/09/22/stop-using-reverse-find-meet-findlast/)

**原文标题**: [
    Stop using .reverse().find(): meet findLast() - Matt Smith
  ](https://allthingssmitty.com/2025/09/22/stop-using-reverse-find-meet-findlast/)

ES2023新增的findLast()和findLastIndex()方法可直接从数组末尾搜索元素，无需反转数组，提供更简洁高效的解决方案。

- 🔍 替代传统反转搜索方式，避免数组复制和反转操作
- 📋 适用于聊天记录、活动日志等需要查找最后匹配项的场景
- ⚡ 提升代码可读性和性能，特别适合处理大型数据集
- 🎯 findLast()返回匹配元素，findLastIndex()返回匹配索引
- 🚫 自动跳过稀疏数组中的空槽位，但不跳过显式undefined值
- ⚠️ 仅适用于真实数组，不支持类数组对象
- 🌐 主流浏览器和Node.js 18.12+均已支持
- 💡 比反向搜索更安全，不会改变原始数组

---

### [在JavaScript BigInt中存储不明智的数据量 | 乔纳森的博客](https://jonathan-frere.com/posts/bigints-are-cool/)

**原文标题**: [Storing Unwise Amounts of Data in JavaScript Bigints | Jonathan's Blog
](https://jonathan-frere.com/posts/bigints-are-cool/)

本文探讨了在JavaScript中使用Bigint类型存储数据的实验性方法，旨在解决配置对象存储时的性能问题，通过位操作实现紧凑数据存储和快速比较，但存在字段宽度限制和代码复杂度等挑战。

- 🎯 解决配置对象存储性能问题：重复键导致序列化字符串过大、对象比较成本高、批量操作缓慢
- 💡 使用Bigint作为数据存储载体：通过位偏移和掩码操作实现字段的紧凑存储
- 🛠️ 实现技术方案：定义字段位宽和偏移量，编写getBits/setBits函数，配合存在位标记字段状态
- 📦 核心优势：内存使用极致压缩、序列化速度快、利用位运算优化比较和交集操作
- ⚠️ 主要局限：字段必须预设最大宽度、Bigint位操作性能较低、代码复杂度显著增加
- 🔬 实验性质：目前仍为侧项目探索，需在实际使用中验证能否通过快速比较启用其他优化
- 💭 适用场景：仅推荐在特定性能敏感场景中使用，普通情况不建议采用此方案

---

### [使用eBPF检测Node.js事件循环 | Coroot](https://coroot.com/blog/instrumenting-the-node-js-event-loop-with-ebpf/)

**原文标题**: [Instrumenting the Node.js event loop with eBPF | Coroot](https://coroot.com/blog/instrumenting-the-node-js-event-loop-with-ebpf/)

本文介绍了如何使用eBPF技术监测Node.js事件循环的阻塞情况，通过轻量级的内核计数器实现生产环境可用的性能指标，帮助定位单线程事件循环导致的性能瓶颈。

- 🌀 Node.js单线程事件循环在CPU核心饱和时会导致性能骤降，即使系统仍有空闲CPU资源
- ⏱️ 通过eBPF在libuv的uv__io_poll函数中测量同步回调执行时间，准确捕获事件循环阻塞时长
- 🚀 采用内核计数器方案替代事件流，仅维护累加纳秒数，实现极低开销的生产级监控
- 🔍 在OpenTelemetry演示场景中验证：前端服务事件循环阻塞达0.81秒/秒，明确显示单核性能瓶颈
- 📈 解决方案是通过水平扩展部署多个实例，使负载分散到不同事件循环以利用多核CPU
- 🛠️ 该功能已集成至Coroot社区版和企业版，可开箱即用诊断Node.js服务性能问题

---

### [Skia 画布](https://skia-canvas.org/)

**原文标题**: [Skia Canvas](https://skia-canvas.org/)

Skia Canvas 是一个基于 Node.js 实现的 HTML Canvas 绘图 API，采用谷歌 Skia 图形引擎，支持离屏和窗口渲染，具备超越浏览器 Canvas 的功能特性。

- 🎨 支持矢量（PDF/SVG）和位图（JPEG/PNG/WEBP）格式输出
- 🖼️ 可绘制交互式 GUI 窗口并提供浏览器级事件框架
- 💾 支持保存至文件、生成 DataURL 字符串、返回 Buffer 或 Sharp 对象
- ⚡ 通过可配置线程池实现异步渲染和文件 I/O
- 📄 支持多页面绘制并导出为多页 PDF 或序列图片
- ✏️ 提供贝塞尔路径的布尔运算与插值编辑功能
- 🔄 支持 3D 透视变换及缩放旋转平移操作
- 🌈 支持矢量纹理填充、自定义标记和完整 CSS 滤镜
- 🔠 提供多行文本排版、字距调整、可变字体等高级文字特性
- ☁️ 兼容 Linux 标准主机及 Vercel/AWS Lambda 无服务器平台
- 🚀 性能基准测试显示其启动延迟低于 1ms，异步渲染效率显著提升

---

### [GitHub - samizdatco/skia-canvas: Node.js的多线程GPU加速2D矢量图形环境](https://github.com/samizdatco/skia-canvas)

**原文标题**: [GitHub - samizdatco/skia-canvas: A multi-threaded, GPU-powered, 2D vector graphics environment for Node.js](https://github.com/samizdatco/skia-canvas)

Skia Canvas 是一个基于 Google Skia 图形引擎的 Node.js 2D 矢量图形库，提供多线程 GPU 加速渲染，支持浏览器 Canvas API 及扩展功能。

- 🎨 支持矢量（PDF/SVG）和位图（JPEG/PNG/WEBP）格式输出
- ⚡ 通过多线程 worker 池实现异步渲染和文件 I/O
- 📄 支持多页面绘制与合并输出（如多页 PDF）
- 🛠️ 提供 3D 透视变换、CSS 滤镜和高级路径操作
- 🔤 支持可变字体、OpenType 特性及非系统字体加载
- 🌐 兼容 Linux/macOS/Windows 及 Vercel/AWS Lambda 等无服务器平台
- 📦 可通过 npm 直接安装预编译版本或从源码编译
- 🎯 在性能基准测试中表现优于同类库（如 canvaskit-wasm、node-canvas）
- ⚙️ 支持环境变量配置线程数和严格模式参数验证

---

### [柚子](https://pompelmi.github.io/pompelmi/)

**原文标题**: [Pompelmi](https://pompelmi.github.io/pompelmi/)

概述：ZIP文件深度检测技术通过多重安全机制确保压缩文件处理的安全性。

- 💣 炸弹/比率限制 - 防止恶意构造的压缩炸弹攻击
- 🔄 遍历安全提取 - 阻止路径遍历攻击，确保安全解压
- 🔍 内部MIME类型嗅探 - 自动检测压缩包内文件的真实格式

---

### [YARA——恶意软件研究人员的模式匹配瑞士军刀](https://virustotal.github.io/yara/)

**原文标题**: [YARA - The pattern matching swiss knife for malware researchers](https://virustotal.github.io/yara/)

YARA是一款面向恶意软件研究人员的多功能模式匹配工具，可用于识别和分类恶意样本。它通过基于文本或二进制模式创建规则来描述恶意软件家族，支持跨平台运行并提供多种扩展资源。

- 🛠️ 核心功能：通过字符串匹配与布尔表达式创建检测规则，示例规则可识别包含特定十六进制码或字符串的文件
- 🌐 跨平台支持：兼容Windows、Linux和Mac OS X系统，提供命令行界面和Python扩展接口
- 🔧 生态工具：集成yara-ci持续测试规则、yextend压缩文件扫描等开源扩展
- 📚 资源汇总：包含GitHub项目库、官方文档、技术交流群组和漏洞反馈渠道
- 🏢 广泛应用：被Avast、Cisco、McAfee等近百家安全企业和组织采用

---

### [GitHub - pompelmi/pompelmi：免费开源文件扫描器](https://github.com/pompelmi/pompelmi)

**原文标题**: [GitHub - pompelmi/pompelmi: free, open-source file scanner](https://github.com/pompelmi/pompelmi)

pompelmi 是一个专为 Node.js 设计的免费开源文件扫描工具，专注于在文件上传到磁盘前进行恶意软件检测。它提供可组合的扫描器、深度 ZIP 文件检查以及针对 Express、Koa 和 Next.js 等流行框架的即插即用适配器，强调隐私保护、无外部数据传输和轻量级设计。

- 🛡️ **隐私优先设计** - 所有扫描均在进程内完成，文件字节数据不会外传，确保数据私密性
- 🔧 **可组合扫描器** - 支持混合使用启发式扫描和签名引擎，可设置停止条件和超时机制
- 📦 **ZIP 文件强化** - 提供路径遍历防护、压缩炸弹检测及多格式文件识别功能
- 🚀 **框架适配器** - 为 Express、Koa、Fastify 和 Next.js 提供开箱即用的中间件支持
- ⚡ **类型安全与轻量** - 基于现代 TypeScript 开发，API 简洁且类型完备
- 🛑 **早期风险拦截** - 通过扩展名白名单、MIME 类型嗅探和文件大小限制等多层防护机制
- 🔍 **深度内容检测** - 内置通用启发式扫描器，可检测 PDF 风险操作、Office 宏及 PE 头信息
- 🔄 **灵活扫描策略** - 支持并行或串行扫描组合，可配置超时和短路检测逻辑
- 🏭 **生产就绪** - 提供详细的生产环境检查清单和 GitHub Action 集成方案
- 📚 **规则引擎扩展** - 可选 YARA 集成，支持自定义检测规则和匹配策略

---

### [AI代码审查工具 - 发版前分析拉取请求 | Sentry](https://sentry.io/product/ai-code-review/?utm_source=nodeweekly&utm_medium=paid-community&utm_campaign=aicodereview-fy26q3-aicodereviewlaunch&utm_content=newsletter-ai-code-review-beta-learnmore)

**原文标题**: [AI Code Review Tool - Analyze PRs Before Shipping | Sentry](https://sentry.io/product/ai-code-review/?utm_source=nodeweekly&utm_medium=paid-community&utm_campaign=aicodereview-fy26q3-aicodereviewlaunch&utm_content=newsletter-ai-code-review-beta-learnmore)

Sentry AI代码审查平台通过智能预测和自动化测试提升开发效率，在代码合并前主动识别问题。

- 🐛 错误预测：结合历史错误数据与实时代码分析，在PR中精准预警潜在故障并提供修复方案
- 🔍 即时审查：自动检测拼写、格式及逻辑错误，整合代码库上下文信息加速代码合并
- 🤖 测试生成：自动创建覆盖所有代码行的可执行单元测试，生成独立分支供审核
- 🌍 可用范围：目前支持GitHub/GitHub企业版，欧盟地区暂不可用
- 💰 成本政策：公开测试阶段完全免费
- 🛡️ 隐私保护：用户数据默认不用于AI训练，生成内容仅对当前用户可见
- 📬 更新订阅：提供月度产品通讯，避免信息过载

---

### [GitHub - raineorshine/npm-check-updates：检查package.json中依赖包的最新可用版本](https://github.com/raineorshine/npm-check-updates)

**原文标题**: [GitHub - raineorshine/npm-check-updates: Find newer versions of package dependencies than what your package.json allows](https://github.com/raineorshine/npm-check-updates)

npm-check-updates 是一个用于检查并升级 package.json 中依赖包版本的工具，支持 npm、yarn、pnpm、deno 和 bun 等多种包管理器，能够智能更新依赖版本并保持原有的语义版本控制策略。

- 🔍 **检查依赖更新** - 自动检测项目中 package.json 文件内依赖包的最新可用版本
- ⬆️ **升级依赖版本** - 使用 `ncu -u` 命令直接更新 package.json 中的依赖版本号
- 🎯 **多种升级目标** - 支持 latest、greatest、minor、patch 等多种升级策略
- 🔧 **高度可定制** - 提供过滤、排除、交互模式等丰富选项满足不同需求
- 🛡️ **安全保护机制** - 包含医生模式测试升级兼容性，冷却期功能防止供应链攻击
- 📁 **配置文件支持** - 支持 .ncurc 配置文件，可定义复杂升级规则
- 🌐 **多包管理器兼容** - 兼容主流包管理器并自动检测对应锁文件
- 💻 **模块化使用** - 支持命令行和程序化调用两种使用方式

---

### [GitHub Copilot CLI 现已进入公开预览阶段 - GitHub 更新日志](https://github.blog/changelog/2025-09-25-github-copilot-cli-is-now-in-public-preview/)

**原文标题**: [GitHub Copilot CLI is now in public preview - GitHub Changelog](https://github.blog/changelog/2025-09-25-github-copilot-cli-is-now-in-public-preview/)

GitHub Copilot CLI 现已进入公开预览阶段，将AI编程助手直接集成至终端，支持本地同步开发并具备完整的代码操作能力。

- 💻 终端原生开发：直接在命令行中使用Copilot编程助手，无需切换上下文
- 🔗 原生GitHub集成：通过自然语言访问仓库、议题和拉取请求，自动使用现有GitHub账户认证
- 🤖 智能代理能力：AI助手可规划并执行复杂任务，支持代码构建、编辑、调试和重构
- 🔧 MCP扩展支持：默认搭载GitHub MCP服务器，支持自定义MCP服务器扩展功能
- ⚡ 完全操作控制：每个操作执行前均需用户明确批准，确保安全可控
- 📦 快速安装：通过npm安装命令 `npm install -g @github/copilot` 即可使用
- 🆓 订阅兼容：支持现有Copilot Pro、Pro+、Business或Enterprise订阅计划

---

### [GitHub - ayuhito/modern-tar: 🗄 适用于所有 JavaScript 运行时的零依赖流式 tar 解析器与写入器](https://github.com/ayuhito/modern-tar)

**原文标题**: [GitHub - ayuhito/modern-tar: 🗄 Zero dependency streaming tar parser and writer for every JavaScript runtime.](https://github.com/ayuhito/modern-tar)

modern-tar 是一个零依赖的流式 tar 解析与生成库，适用于所有 JavaScript 运行时，采用 Web Streams API 实现高性能与内存效率。

- 🗄️ 零依赖的流式 tar 处理库，支持所有 JavaScript 运行环境
- 🚀 基于 Web Streams API 的流式架构，可处理大型归档文件
- 📋 完全兼容 USTAR 格式标准，支持 PAX 扩展
- 🗜️ 内置 gzip 压缩与解压缩辅助功能
- 📝 完全 TypeScript 支持，提供详细类型文档
- 🌐 跨平台支持浏览器、Node.js、Cloudflare Workers 等环境
- 📁 提供 Node.js 专用的高级文件系统 API
- ⚡ 核心包无外部依赖，打包体积最小化
- 🔧 支持动态添加条目、过滤转换、权限设置等高级功能

---

### [tar（计算机） - 维基百科](https://en.wikipedia.org/wiki/Tar_(computing))

**原文标题**: [tar (computing) - Wikipedia](https://en.wikipedia.org/wiki/Tar_(computing))

tar是一种用于将多个文件打包成单个归档文件的Unix/Linux命令工具，最初为磁带存储设计，现广泛用于软件分发和备份。

- 📦 文件归档工具，可将多个文件合并为单一归档文件（tarball）
- 🕰️ 诞生于1979年，最初用于磁带存储设备
- 📁 支持保留文件元数据（权限、时间戳、目录结构等）
- 🔄 采用512字节块记录格式，通过填充零字节对齐数据
- 🌍 存在多种格式标准：传统格式、USTAR、PAX（支持扩展属性）
- ⚠️ 存在路径长度限制（早期仅100字符），现代格式已扩展
- 🛠️ 常与压缩工具联用（如.gz/.bz2/.xz）形成压缩包
- 💥 需注意“tarbomb”风险（文件直接解压到当前目录）
- 🐧 主流实现包括GNU tar、BSD tar、star等
- 📊 缺乏中央索引，需顺序读取，但容错性较强

---

### [GitHub - fetch-kit/ffetch：基于TypeScript的fetch封装库，内置可配置超时、重试和熔断机制。](https://github.com/fetch-kit/ffetch)

**原文标题**: [GitHub - fetch-kit/ffetch: TypeScript-first fetch wrapper with configurable timeouts, retries, and circuit-breaker baked in.](https://github.com/fetch-kit/ffetch)

ffetch 是一个基于 TypeScript 的现代化 fetch 封装库，提供可配置的超时、重试和熔断器功能，适用于浏览器、Node.js 和各种边缘计算环境。

- ⚡ 支持全局或单次请求的超时设置、指数退避重试机制和自动熔断保护
- 🔧 可包装任何兼容 fetch 的实现（包括原生 fetch、node-fetch 及各框架提供的 fetch）
- 🎯 完整的 TypeScript 类型支持，零运行时依赖，提供双模式 ESM/CJS 打包
- 🪝 提供丰富的生命周期钩子，支持请求/响应转换、认证、日志和监控
- 🌐 支持实时查看活跃请求数，可针对单次请求进行行为定制
- 🚨 可配置错误处理，支持通过 throwOnHttpError 标志在 HTTP 错误时抛出异常
- 📦 轻量级设计，压缩后约 3KB，兼容现代浏览器和 Node.js 20.6+ 环境
- 🔌 提供 CDN 直接使用方式，支持在各种 JavaScript 框架和环境中无缝集成

---

### [pnpm 10.17 | pnpm](https://pnpm.io/blog/releases/10.17)

**原文标题**: [pnpm 10.17 | pnpm](https://pnpm.io/blog/releases/10.17)

pnpm 10.17版本更新了依赖包成熟期检查机制，优化了版本筛选逻辑

- 🔧 `minimumReleaseAgeExclude` 设置新增通配符支持，可批量排除指定范围的包（如`@eslint/*`）
- 🗃️ 修复缓存场景下精确版本请求仍会触发成熟期检查的问题
- 🚫 当正式版本未达成熟期要求时，系统不再自动降级至预发布版本
- ⏱️ 所有改进均围绕`minimumReleaseAge`配置展开，提升依赖管理的稳定性

---

### [GitHub - sinclairzx81/typebox: JavaScript 运行时类型系统](https://github.com/sinclairzx81/typebox)

**原文标题**: [GitHub - sinclairzx81/typebox: A Runtime Type System for JavaScript](https://github.com/sinclairzx81/typebox)

TypeBox 是一个用于 JavaScript 的运行时类型系统，它通过创建内存中的 JSON Schema 对象来推断 TypeScript 类型，同时提供静态类型检查和运行时验证功能。

- 🛠️ 运行时类型系统：通过 JSON Schema 对象实现类型推断和验证
- 🔄 统一类型支持：同时兼容 TypeScript 静态检查和 JSON Schema 运行时验证
- 📦 模块化设计：提供 Type、Script、Value 和 Compile 四个核心模块
- 🚀 高性能编译：Compile 模块可将类型转换为高性能验证器
- 💡 语法灵活性：支持函数组合和原生 TypeScript 语法构建复杂类型
- 📄 丰富文档：包含完整的使用示例和迁移指南
- 🌐 社区活跃：拥有 6.1k Stars 和 189 Forks，被 970 万+项目使用
- ⚖️ MIT 许可：开源项目，欢迎社区贡献

---

### [GitHub - openai/openai-node：OpenAI API 官方 JavaScript / TypeScript 库](https://github.com/openai/openai-node)

**原文标题**: [GitHub - openai/openai-node: Official JavaScript / TypeScript library for the OpenAI API](https://github.com/openai/openai-node)

OpenAI官方提供的JavaScript/TypeScript库，用于访问OpenAI REST API，支持多种运行环境和高级功能。

- 🚀 官方JavaScript/TypeScript库，提供对OpenAI API的便捷访问
- 📦 支持npm安装和JSR安装，兼容Node.js、Deno、Bun等运行时
- 💬 支持响应API和聊天补全API两种文本生成方式
- 🌊 提供流式响应支持，可实现实时数据接收
- 📁 支持多种文件上传方式（File对象、fetch响应、文件流等）
- 🔐 包含Webhook验证功能，确保数据安全性
- ⚠️ 完善的错误处理机制，涵盖各类API错误类型
- 🔄 自动重试机制，默认重试2次连接错误和服务器错误
- ⏱️ 可配置超时设置，默认10分钟
- 📄 支持自动分页，方便处理大量数据
- 🌐 提供实时API，支持WebSocket连接实现低延迟交互
- ☁️ 支持Microsoft Azure OpenAI服务
- 🔧 提供高级功能：原始响应访问、自定义日志、代理配置等
- ⚡ 支持自定义请求和未记录参数访问
- 📊 详细的日志记录系统，支持多级别日志输出
- 🌍 支持浏览器环境（需显式启用dangerouslyAllowBrowser选项）

---

### [GitHub - sindresorhus/pretty-bytes：将字节转换为人类可读的字符串：1337 → 1.34 kB](https://github.com/sindresorhus/pretty-bytes)

**原文标题**: [GitHub - sindresorhus/pretty-bytes: Convert bytes to a human readable string: 1337 → 1.34 kB](https://github.com/sindresorhus/pretty-bytes)

这是一个用于将字节数转换为人类可读格式的JavaScript工具库，支持多种自定义格式选项。

- 📦 核心功能是将字节数值转换为易读字符串（如1337→1.34 kB）
- ⚙️ 支持多种配置选项：符号显示、位单位、二进制前缀、本地化等
- 📐 提供精确控制：最小/最大小数位数、固定宽度对齐功能
- 🌍 支持国际化，可指定不同语言环境显示数字格式
- 📊 特别适用于文件大小显示、进度条和表格对齐等场景
- 🔧 基于MIT开源协议，可通过npm安装使用
- 📈 项目活跃度高，拥有1.3k星标和大量用户群体

---

### [发布 v0.18.0 · wasp-lang/wasp · GitHub](https://github.com/wasp-lang/wasp/releases/tag/v0.18.0)

**原文标题**: [Release v0.18.0 · wasp-lang/wasp · GitHub](https://github.com/wasp-lang/wasp/releases/tag/v0.18.0)

Wasp语言发布了0.18.0版本更新，包含多项功能改进和问题修复

- ⚠️ 重大变更：要求Node.js版本≥v22.12，Tailwind配置改用ESM模块，升级至Vite 7
- 🚀 新增功能：添加wasp build start命令，可在本地运行构建后的应用
- 🐛 问题修复：修复JSON环境变量解析、Bash补全循环等多项问题
- 🔧 优化改进：支持Prisma模式文档注释、移除Stitches减小打包体积、改进移动端字体显示
- 📚 文档更新：新增自定义认证操作的代码示例
- 👥 贡献者：Genyus和Vickram-T-G等开发者的贡献

---

### [黄蜂](https://wasp.sh/)

**原文标题**: [Wasp](https://wasp.sh/)

Wasp是一个全栈Web开发框架，通过声明式配置语言和代码生成技术，显著提升React+Node.js+Prisma技术栈的开发效率。

- 🚀 通过.wasp配置文件快速定义应用核心功能，支持单命令部署
- 🔐 内置全栈身份验证系统，支持谷歌/GitHub/邮箱登录
- 🔄 提供类型安全的RPC层，自动客户端缓存失效机制
- 📧 集成邮件发送、后台任务调度等企业级功能
- 🛠️ 保持90%代码使用React/Node.js/Prisma开发，仅自动化样板代码
- ⚡ 支持实时WebSocket应用、TypeScript全栈类型安全
- 🌐 可部署到任意平台，提供CLI部署工具
- 📚 开源项目，提供待办应用、智能求职信等完整示例
- 🎯 相比传统框架，更专注于减少配置和重复代码编写

---

### [发布 v6.20.0 · mongodb/node-mongodb-native · GitHub](https://github.com/mongodb/node-mongodb-native/releases/tag/v6.20.0)

**原文标题**: [Release v6.20.0 · mongodb/node-mongodb-native · GitHub](https://github.com/mongodb/node-mongodb-native/releases/tag/v6.20.0)

MongoDB Node.js驱动发布6.20.0版本，新增集合与数据库对象引用功能，优化变更流容错机制，并弃用部分历史遗留API。

- 🎉 集合与数据库对象新增client/db属性引用，可直接获取关联的MongoClient和Db实例
- 🚀 未确认写入操作现支持hint参数，适用于delete、update和findAndModify命令
- ⚠️ 弃用ServerCapabilities类、driverInfo配置项及CommandOperationOptions.retryWrites等历史遗留功能
- 🔄 ChangeStream.tryNext()方法现自动缓存resumeToken，避免故障恢复时出现重复数据
- 🌐 变更流新增对MongoServerSelectionError的自动恢复支持，增强网络容错能力
- 🛠️ 修复MongoClient.appendMetadata()重复添加元数据的问题
- 📚 包含7项功能更新、3项错误修复及1项文档改进

---

### [发布 11.0.0 版本 · timgit/pg-boss · GitHub](https://github.com/timgit/pg-boss/releases/tag/11.0.0)

**原文标题**: [Release 11.0.0 · timgit/pg-boss · GitHub](https://github.com/timgit/pg-boss/releases/tag/11.0.0)

pg-boss 11.0.0版本发布，包含多项重大变更和功能优化，主要涉及分区策略调整、API简化、监控机制改进和新增配置选项。

- ⚠️ 不支持从v10自动迁移，需手动转移数据
- 🗃️ 队列分区改为可选配置（partition属性）
- 🗂️ 移除归档表，新增deleteAfterSeconds配置（默认7天）
- ⏱️ 统一时间单位为秒，移除分钟/小时/天级配置
- 🔄 重构监控机制，新增superviseIntervalSeconds（默认60秒）
- 📝 API变更：insert方法需指定队列名，参数名标准化
- 📊 移除事件监控，新增getQueueStats实时统计
- 🛠️ 维护函数重组，supervise替代maintain
- ⚡ 最低要求Node.js 22版本
- 🔔 新增warning事件支持慢查询和队列积压预警
- 🎯 队列支持多定时任务（key参数）
- ⏳ 新增retryDelayMax限制重试退避上限

---

### [GitHub - verdaccio/verdaccio：一个轻量级的 Node.js 私有代理注册表](https://github.com/verdaccio/verdaccio)

**原文标题**: [GitHub - verdaccio/verdaccio: A lightweight Node.js private proxy registry](https://github.com/verdaccio/verdaccio)

Verdaccio 是一个轻量级的 Node.js 私有代理注册中心，无需复杂配置即可搭建本地私有 npm 仓库，支持缓存公共包和插件扩展。

- 🏠 **零配置私有注册中心** - 内置微型数据库，无需外部数据库即可快速搭建私有 npm 仓库
- 🔄 **代理与缓存功能** - 可代理 npmjs.org 等公共注册中心，缓存下载的包以减少延迟
- 🔌 **插件生态系统** - 支持 AWS S3、Google Cloud Storage 等存储插件，可自定义扩展
- 🐳 **多方式部署** - 支持 npm/yarn/pnpm 全局安装、Docker 容器和 Helm Chart 部署
- 🧪 **完整的包管理功能** - 支持发布、安装、撤销发布、标签管理、搜索等核心 npm 命令
- 🔒 **安全与权限控制** - 支持用户管理、密码修改、令牌认证和漏洞审计功能
- 🤝 **活跃的开源社区** - 被 create-react-app、Babel、Vue CLI 等知名项目使用，拥有丰富的生态系统

---

### [Holepunch - 高级Node.js软件工程师（全球远程，全职）](https://holepunch.recruitee.com/o/senior-node-engineer?source=Node-Weekly)

**原文标题**: [Holepunch - Senior Node.js Software Engineer (100% Remote, Worldwide)](https://holepunch.recruitee.com/o/senior-node-engineer?source=Node-Weekly)

Holepunch是一家专注于构建去中心化互联网基础设施的科技公司，通过其开源技术栈Pear开发点对点（P2P）平台，旨在消除传统服务器依赖，保障用户数据隐私与自主权。

- 🌐 采用P2P技术重构互联网架构，确保用户数据完全自主控制
- ⚡ 基于Node.js开发类似BitTorrent的P2P连接与数据复制系统
- 📱 旗舰应用Keet展示P2P通信潜力，支持消息、文件共享等功能
- 💻 招聘全远程Node.js工程师，要求具备模块化开发和npm模块经验
- 🔧 优先考虑掌握C/C++、网络协议及分布式系统的候选人
- 🌍 团队分布全球，强调远程协作能力与对去中心化技术的热情
- 🚀 提供参与前沿技术开发机会，共同构建更安全包容的网络未来

---

### [Holepunch - 高级Node.js软件工程师（全球远程，全职）](https://holepunch.recruitee.com/o/senior-node-engineer?source=Node-Weekly)

**原文标题**: [Holepunch - Senior Node.js Software Engineer (100% Remote, Worldwide)](https://holepunch.recruitee.com/o/senior-node-engineer?source=Node-Weekly)

Holepunch正在招聘一名高级Node.js软件工程师，该职位完全远程，面向全球。公司致力于通过其开源技术栈Pear重新定义互联网架构，构建去中心化的点对点平台，以增强用户数据控制和隐私保护。

- 🌐 开发点对点技术栈，基于类似BitTorrent的Node.js技术，实现去中心化应用部署和数据复制
- 💻 要求具备Node.js丰富经验，能编写高质量代码，熟悉C/C++或原生绑定者优先
- 📦 强调模块化开发，需有构建和管理npm模块的背景
- 🧪 负责测试与调试，确保软件可靠性和性能优化
- 🔗 热爱P2P技术，有相关开发经验或对去中心化充满热情
- 🌍 需适应全球远程协作，与分布式团队高效沟通
- 🚀 提供机会参与突破性技术项目，推动互联网演进，优先考虑用户自主权和隐私

---

### [开始使用Redis](https://redis.io/lp/get-started2/?utm_source=cooper-press&utm_medium=cpa&utm_campaign=2025-08-app_performance-node-weekly-2&utm_content=cloud_-_redis_cloud_users)

**原文标题**: [Get started with Redis](https://redis.io/lp/get-started2/?utm_source=cooper-press&utm_medium=cpa&utm_campaign=2025-08-app_performance-node-weekly-2&utm_content=cloud_-_redis_cloud_users)

Redis是一个专为速度设计的数据平台，提供云端和本地部署解决方案，帮助团队快速构建高性能应用。

- 🚀 作为全球最快的内存数据库，支持向量数据库、缓存和NoSQL等多种数据架构
- 🧠 先进的向量数据库功能，可构建最快速可靠的生成式AI应用
- ⚡ 通过内存键值存储支持多种数据结构，专为实时应用优化效率
- 🌩️ 提供Redis Cloud服务，轻松创建首个数据库并快速上手
- 🔧 为开发者提供多语言支持和技术中心，为架构师和运维团队提供演示和技术讲座
- 📈 支持从实验到生产级AI应用的无缝扩展，让团队更专注于开发
- 🆓 提供免费试用选项，助力快速开始构建

---

### [开始使用Redis](https://redis.io/lp/get-started2/?utm_source=cooper-press&utm_medium=cpa&utm_campaign=2025-08-app_performance-node-weekly-2&utm_content=cloud_-_redis_cloud_users%20)

**原文标题**: [Get started with Redis](https://redis.io/lp/get-started2/?utm_source=cooper-press&utm_medium=cpa&utm_campaign=2025-08-app_performance-node-weekly-2&utm_content=cloud_-_redis_cloud_users%20)

Redis是一个专为速度设计的数据平台，提供云端和本地部署解决方案，帮助团队快速构建高性能应用。

- 🚀 快速部署向量数据库、缓存和NoSQL数据库，支持实时应用开发
- 🧠 先进的向量数据库助力构建最快速可靠的生成式AI应用
- ⚡ 全球最快内存数据库显著提升应用性能
- 🗄️ 支持多种数据结构的内存键值存储，适用于实时场景
- 🌟 提供免费试用，从实验到生产环境无缝扩展
- 💻 支持多语言开发，为开发者、架构师和运维团队提供专属资源中心

---

### [tc39/agendas 仓库主分支下的 agendas/2025/09.md 文件](https://github.com/tc39/agendas/blob/main/2025/09.md)

**原文标题**: [agendas/2025/09.md at main · tc39/agendas · GitHub](https://github.com/tc39/agendas/blob/main/2025/09.md)

这是一个关于TC39议程仓库的GitHub页面概览

- 📋 公共仓库包含TC39会议的议程和相关信息
- 🔔 需要登录GitHub账户才能更改通知设置
- 🍴 已被198个用户复刻
- ⭐ 获得1.2k个星标收藏
- 🐛 目前没有开放的议题
- 🔄 有4个拉取请求待处理
- ⚠️ 页面加载时出现错误提示
- 📊 提供代码、议题、安全等导航选项

---

### [GitHub - tc39/proposal-import-bytes：JavaScript中导入字节的适度提案](https://github.com/tc39/proposal-import-bytes)

**原文标题**: [GitHub - tc39/proposal-import-bytes: A modest proposal for importing bytes in javascript](https://github.com/tc39/proposal-import-bytes)

该提案旨在为JavaScript添加导入任意字节数据的能力，通过统一的语法实现跨环境文件读取，当前处于TC39流程第二阶段。

- 💡 支持通过`import bytes from "./file" with {type: "bytes"}`语法直接导入字节数据
- 🔄 返回基于不可变ArrayBuffer的Uint8Array对象，确保数据一致性
- 🌐 解决多平台兼容性问题，替代现有的Deno/Bun/Node.js/浏览器差异化代码
- ⚡ 支持静态和动态导入两种方式，便于打包工具进行基64内联优化
- 🔒 采用不可变设计避免内存重复、数据竞争和嵌入式系统内存压力
- 📋 选择Uint8Array而非ArrayBuffer因其与Node.js Buffer兼容且无需额外创建视图
- 🚫 排除Blob/ReadableStream等方案因它们不属于JavaScript语言标准
- 📁 使用`type: bytes`属性与JSON模块保持设计一致性，明确区分代码与数据加载

---

### [GitHub - tc39/proposal-iterator-chunking：为迭代器添加生成子序列迭代器方法的提案](https://github.com/tc39/proposal-iterator-chunking/)

**原文标题**: [GitHub - tc39/proposal-iterator-chunking: a proposal to add a method to iterators for producing an iterator of its subsequences](https://github.com/tc39/proposal-iterator-chunking/)

这是一个TC39提案，旨在为迭代器添加将序列分割为子序列的方法，包括非重叠的分块和重叠的滑动窗口两种模式。

- 📋 提案状态：目前处于Stage 2.7阶段，已制定规范文档
- 🔄 核心功能：为迭代器添加chunks()和windows()方法，分别实现非重叠分块和重叠滑动窗口
- 📊 分块示例：将[0-9]序列按大小2分块得到[[0,1],[2,3],[4,5],[6,7],[8,9]]
- 🪟 滑动窗口示例：窗口大小为3时，生成[0,1,2]、[1,2,3]等重叠子序列
- 💼 应用场景：分页、网格布局、批处理、矩阵运算、格式编码、分桶等
- 🎯 滑动窗口用途：连续计算（如平均值）、上下文敏感算法、轮播组件等
- 🌍 多语言参考：列举了C++、Java、Python、Rust等10多种语言的类似实现
- 📚 JS生态支持：汇总了chunk、iter-tools等9个主流JS库的相关功能
- 👥 开发团队：由Michael Ficarra和Kevin Gibbons两位主要贡献者维护

---

### [获取失败](https://nodeweekly.com/link/174956/web)

**原文标题**: [Failed to retrieve](https://nodeweekly.com/link/174956/web)

无法总结：获取内容失败，状态码 404。

---

### [Bun v1.2.23 | Bun 博客](https://bun.com/blog/bun-v1.2.23)

**原文标题**: [Bun v1.2.23 | Bun Blog](https://bun.com/blog/bun-v1.2.23)

本次Bun版本更新修复了119个问题，主要涵盖安装优化、包管理器增强、测试框架升级、Node.js兼容性改进及核心功能优化等方面。

- 🛠️ 安装方式多样化：支持curl、npm、PowerShell、scoop、brew和docker等多种安装命令
- 📦 包管理增强：bun install自动迁移pnpm锁文件，新增--cpu/--os标志控制平台特定依赖安装
- 🔔 Redis客户端升级：支持Pub/Sub消息模式，新增subscribe()和publish()方法
- ⚡ 测试框架优化：支持test.concurrent并发测试，新增--randomize随机执行顺序，严格CI环境检测
- 🔄 Node.js兼容性提升：改进node:http、node:dns、node:worker_threads等模块功能
- 🔒 安全增强：新增--use-system-ca标志使用系统CA证书，Windows支持process.report.getReport()
- 📟 构建工具升级：bun build支持JSX配置对象，Windows编译支持代码签名剥离
- 🗄️ 数据库功能增强：Bun.SQL新增sql.array助手支持PostgreSQL数组类型
- 🐛 问题修复：解决bundler循环依赖、包版本解析溢出、测试框架异常处理等关键问题
- 👥 社区贡献：感谢16位贡献者的代码提交

---

### [IINA - macOS 现代媒体播放器](https://iina.io/)

**原文标题**: [IINA - The modern media player for macOS](https://iina.io/)

IINA是一款基于开源媒体播放器mpv的多功能播放器，支持本地与在线流媒体播放。

- 🎬 支持播放几乎所有本地媒体文件
- 🔓 基于开源播放器mpv技术开发
- 🌐 通过浏览器扩展一键播放在线流媒体
- 📺 兼容youtube-dl支持的各类网络视频

---

### [插件系统 | IINA - macOS 现代媒体播放器](https://iina.io/plugins/)

**原文标题**: [Plugin System | IINA - The modern media player for macOS](https://iina.io/plugins/)

IINA 插件系统允许通过 JavaScript 扩展播放器功能，提供简洁而强大的 API 实现个性化需求

- 🧩 插件系统基于 JavaScript，可控制播放、调用 mpv API、访问网络和文件系统
- 🚀 自 1.4.0 版本起支持，通过官方用户脚本插件可直接粘贴代码片段
- 🎬 示例1：视频加载时在画面上方以大字体显示标题
- ⏸️ 示例2：暂停时自动最小化窗口，恢复时继续播放
- 🔧 核心功能涵盖播放控制、MPV API 调用、事件监听、网络请求
- 📺 支持自定义界面：覆盖层、侧边栏、独立窗口、菜单项
- 💾 提供文件访问、偏好设置、系统对话框等实用工具
- 🛠️ 内置命令行工具协助创建和调试插件
- 📚 完整文档和 TypeScript 类型定义支持开发

---

### [仙女座](https://tryandromeda.dev/)

**原文标题**: [Andromeda](https://tryandromeda.dev/)

Andromeda是一个基于Rust构建的现代JavaScript/TypeScript运行时，采用Nova引擎实现高性能和内存安全，提供零配置TypeScript支持和完整的Web API兼容性

- 🚀 基于Rust构建，具备内存安全特性和卓越性能
- ⚡ 集成Nova引擎，提供硬件加速图形和快速启动时间
- 📝 零配置TypeScript支持，内置语言服务器协议
- 🛡️ 符合WinterTC标准，支持完整的Web API
- 🔧 包含完整开发工具链：REPL、格式化器、打包器等
- 🎯 支持单文件编译和跨平台部署
- 📊 专为图形可视化、高性能脚本和科学计算设计
- 📦 内置SQLite数据库和Web Crypto API支持
- 🌐 相比Node.js和Deno具有更低内存占用和更完整功能
- 🔄 提供一键安装脚本，支持Linux/macOS/Windows平台

---

### [GitHub - alshdavid/ion：带正电荷的JavaScript运行时](https://github.com/alshdavid/ion)

**原文标题**: [GitHub - alshdavid/ion: A Positively Charged JavaScript Runtime](https://github.com/alshdavid/ion)

Ion是一个基于Rust构建的JavaScript运行时，专为在Rust应用程序中嵌入JavaScript引擎而设计，适用于插件系统、SSR服务和FaaS等场景。

- ⚡ 采用分层架构，核心运行时包含V8引擎和基于Tokio的事件循环
- 🔧 提供易于使用的高级API，支持多线程和独立上下文
- 📦 可通过解析器、扩展和预处理器灵活扩展标准库功能
- 🔄 支持Rust与JavaScript双向调用，包含Promise异步处理
- 🌐 优先兼容Web标准，当前支持基础定时器和控制台API
- 🚫 明确不兼容Node.js/Deno/Bun的嵌入方案，解决分发和API易用性问题
- 🧵 运行时、工作线程和上下文均绑定专用线程，确保线程安全

---

