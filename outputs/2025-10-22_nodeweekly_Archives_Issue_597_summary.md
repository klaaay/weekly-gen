### [Node 周刊第 597 期：2025 年 10 月 21 日](https://nodeweekly.com/issues/597)

**原文标题**: [Node Weekly Issue 597: October 21, 2025](https://nodeweekly.com/issues/597)

overview summary
本期 Node 周报重点介绍了 Node.js v25.0.0 版本的重大更新，包含多项性能优化和新特性，同时汇总了 TigerData 对 PostgreSQL 的扩展突破、多场技术大会的精彩内容，以及十余个热门开发工具的最新版本发布。

- 🚀 Node.js v25.0.0 正式发布，默认启用 Web 存储并带来 JSON 性能优化
- 📊 TigerData 将 PostgreSQL 扩展至 2PB 规模，支持每日 1.5 万亿指标处理
- 🎥 Nordic.js 2025 技术大会视频上线，涵盖 Node.js 生态最新进展
- 🛠️ Ace CLI 框架教程：使用 Node/Bun 构建书签管理应用
- ⚡ 通过 DTrace 工具深入分析 Node.js 流背压机制对垃圾回收的影响
- 📦 多款开发工具更新：Wretch 3.0 强化 fetch 功能、DOMPurify 3.3 提升 XSS 防护
- 🔧 开发资源推荐：Node 测试覆盖率文档、typeof null 历史渊源解析
- 🌐 行业动态：Cloudflare 推出代码沙盒服务、PostgreSQL 18 性能基准测试

---

### [Node.js — Node.js v25.0.0（当前版本）](https://nodejs.org/en/blog/release/v25.0.0)

**原文标题**: [Node.js — Node.js v25.0.0 (Current)](https://nodejs.org/en/blog/release/v25.0.0)

Node.js v25.0.0 正式发布，带来 V8 引擎升级至 14.1 版本，显著提升 JSON 序列化性能，默认启用 Web Storage API，并引入权限模型的网络控制功能，同时移除多项已弃用 API 以优化安全性和开发体验。

- 🚀 V8 引擎升级至 14.1，大幅优化 JSON.stringify 性能并支持 Uint8Array 的 base64/hex 转换  
- 🔒 权限模型新增 --allow-net 标志，强化应用默认安全机制  
- 🌐 默认启用 Web Storage API，ErrorEvent 设为全局对象  
- 🗑️ 移除 SlowBuffer 等长期弃用 API，提升代码清洁度  
- ⚡ 新增便携式编译缓存和 WebAssembly JSPI 支持，改善开发效率  
- 🔧 更新构建工具链，包括 Python 3.14 测试支持和 Clang 最低版本要求提升至 19

---

### [权限 | Node.js v25.0.0 文档](https://nodejs.org/api/permissions.html)

**原文标题**: [Permissions | Node.js v25.0.0 Documentation](https://nodejs.org/api/permissions.html)

Node.js 权限模型通过进程级权限控制来限制对系统资源的访问，采用"安全带"机制防止可信代码意外操作未授权资源，但无法防范恶意代码绕过限制。

- 🛡️ 权限模型通过--permission 标志启用，默认限制文件系统、网络、子进程等核心模块的访问权限
- ⚙️ 运行时可通过 process.permission.has() 动态检查权限状态，支持按作用域和具体资源进行验证
- 📁 文件系统权限需显式使用--allow-fs-read/--allow-fs-write 开启，支持通配符和绝对路径配置
- 🔄 与 npx 配合使用时需通过--node-options 传递权限参数，并妥善处理全局模块和缓存目录的读取权限
- ⚠️ 存在已知限制：不继承到工作线程、符号链接可能绕过路径限制、OpenSSL 引擎等部分功能受限
- 🚫 权限模型在环境初始化后生效，因此--env-file 等启动阶段读取文件的标志不受权限规则约束

---

### [Node.js — Node.js v22.21.0（长期支持版）](https://nodejs.org/en/blog/release/v22.21.0)

**原文标题**: [Node.js — Node.js v22.21.0 (LTS)](https://nodejs.org/en/blog/release/v22.21.0)

Node.js v22.21.0 (LTS) 版本发布，主要新增了 HTTP 代理支持、内存管理优化和多项功能改进。

- 🌐 新增命令行选项 `--use-env-proxy` 和环境变量 `NODE_USE_ENV_PROXY` 支持 HTTP 代理
- 🔄 为 HTTP 服务器添加 `shouldUpgradeCallback` 回调函数，增强升级协议控制能力
- 📊 `--max-old-space-size` 内存参数新增百分比配置支持
- ⚡ 内置 HTTP/HTTPS 请求和 Agent 现在支持代理功能
- 🔧 多项依赖更新：OpenSSL 升级至 3.5.4、npm 更新至 10.9.4、Undici 更新至 6.22.0
- 🐛 修复了 REPL 大字符串粘贴性能问题、诊断通道竞争条件等多个 Bug
- 📚 文档改进：新增安全升级策略、.env 文件支持标记为稳定等功能说明

---

### [您也能将 Postgres 扩展至每日处理 2.45 PB 数据和 2.5 T 指标 | TigerData](https://www.tigerdata.com/blog/scaling-postgresql-to-petabyte-scale?utm_source=cooperpress&utm_medium=referral&utm_campaign=project-eyeballs-2025&utm_content=node-weekly-newsletter-owl-1)

**原文标题**: [You, Too, Can Scale Postgres to 2.45 PB and 2.5 T Metrics per Day | TigerData](https://www.tigerdata.com/blog/scaling-postgresql-to-petabyte-scale?utm_source=cooperpress&utm_medium=referral&utm_campaign=project-eyeballs-2025&utm_content=node-weekly-newsletter-owl-1)

TigerData 公司通过其 Tiger Cloud 云平台成功将 PostgreSQL 数据库扩展至每日处理 2.5 万亿指标、存储 2.45PB 数据的规模，证明了 PostgreSQL 在时序数据和实时分析场景下的强大扩展能力。

- 🚀 单日指标处理量突破 2.5 万亿，总数据存储量达 2.45PB
- 🗄️ 采用分层存储架构，活跃数据集保持在 12TB，其余 1.5PB 数据自动分层
- ⚡ 通过时序数据库特性实现高速查询，持续聚合技术保障查询性能
- 🔄 使用 UDDSketch 算法压缩原始数据，采样率优化至 25%
- 🌳 建立分层连续聚合树结构（分钟/小时/天级），避免直接查询原始表
- 📈 三年来数据量每年增长约 1PB，无需读写分离仍保持稳定运行
- 🆓 强调所有用户均可通过 Tiger Cloud 达到相同规模，平台功能完全开放

---

### [北欧.js - YouTube](https://www.youtube.com/@nordicjs/videos)

**原文标题**: [Nordic.js - YouTube](https://www.youtube.com/@nordicjs/videos)

这是一个关于 YouTube 平台信息和政策页面的概述

- ℹ️ 关于平台的基本介绍
- 📢 媒体联系与新闻发布
- ©️ 版权相关声明
- 📞 联系方式
- 👥 内容创作者信息
- 💼 广告合作业务
- 💻 开发者资源
- 📋 服务条款
- 🔒 隐私政策
- ⚖️ 平台安全政策
- 🔧 平台运作机制
- 🧪 新功能测试
- Ⓜ️ 版权所有声明（谷歌公司 2025）

---

### [北欧.js 2025 • 张怡怡 - 2025 年 Node.js 软件包发布实战 - YouTube](https://www.youtube.com/watch?v=I0jvOJW7NaI)

**原文标题**: [Nordic.js 2025 • Joyee Cheung - Shipping Node.js packages in 2025 - YouTube](https://www.youtube.com/watch?v=I0jvOJW7NaI)

这是一个关于 YouTube 平台信息页面的概述，包含主要功能板块与政策条款。

- 📄 关于平台的基本信息与介绍
- 📢 媒体联系与新闻发布相关
- ©️ 版权声明与知识产权保护
- 📞 用户联系与客服渠道
- 🎬 内容创作者专属资源
- 💼 广告合作与商业推广
- 🔧 开发者工具与技术支持
- 📑 服务条款与使用协议
- 🔒 隐私政策与数据保护
- 🛡️ 平台安全与政策指南
- ⚙️ 产品功能运作机制说明
- 🧪 新功能测试与体验
- ⏳ 2025 年谷歌公司版权所有

---

### [北欧.js 2025 • Marco Ippolito - 又一份配置文件：介绍 node.config.json - YouTube](https://www.youtube.com/watch?v=KayS7U-ivNo)

**原文标题**: [Nordic.js 2025 • Marco Ippolito - Yet Another Config File: introducing node.config.json - YouTube](https://www.youtube.com/watch?v=KayS7U-ivNo)

这是一个关于 YouTube 平台信息与服务的页面概览

- ℹ️ 关于平台的基本介绍
- 📢 媒体与新闻相关内容
- ©️ 版权信息与政策
- 📞 联系方式与用户支持
- 👥 内容创作者资源
- 💼 广告与商业合作
- 🔧 开发者工具与接口
- 📜 服务条款与使用协议
- 🔒 隐私保护政策
- ⚖️ 平台安全政策与规范
- 🔄 平台运作机制说明
- 🧪 新功能测试与体验
- Ⓜ️ 版权所有方标识

---

### [JSConf | LF 活动](https://events.linuxfoundation.org/jsconf-north-america/)

**原文标题**: [JSConf | LF Events](https://events.linuxfoundation.org/jsconf-north-america/)

JSConf 北美大会已于 2025 年 10 月 14-16 日在马里兰州切萨皮克湾成功举办，作为 JavaScript 社区的顶级活动，本次会议与 ng-conf 联合举办，提供技术交流与特色体验日。

- 🗓️ 活动时间：2025 年 10 月 14-16 日 | 地点：马里兰州切萨皮克湾凯悦度假村
- 🎯 核心内容：主题演讲/分组讨论/社交活动 | 特色环节：第二天自选冒险体验（高尔夫/皮划艇/海滩篝火等）
- 👨‍👩‍👧‍👦 家庭友好：提供宾客通行证与免费儿童看护服务 | ✈️ 含机场接送
- 🎥 资源回顾：会议录像发布于 OpenJS 基金会 YouTube 频道 | 演讲资料可通过活动日程获取
- 🤝 行业影响：作为 JavaScript 生态创新发源地 | 本次与 ng-conf 联合举办形成技术双峰会
- 🌟 演讲嘉宾：包含 Charlie Gerard/Evan You/Robin Bender Ginn 等 15 位行业专家
- 💫 活动特色：开放式可视化协作工作坊 | 航空数据可视化等前沿议题

---

### [Node.js 2025：新特性与未来展望 - Speaker Deck](https://speakerdeck.com/ruyadorno/node-dot-js-2025-whats-new-and-whats-next)

**原文标题**: [Node.js 2025: What's new and what's next - Speaker Deck](https://speakerdeck.com/ruyadorno/node-dot-js-2025-whats-new-and-whats-next)

好的，请提供您需要总结的文本内容，我将按照您要求的格式进行整理：
- 顶部提供概述总结
- 用"-"符号列出带表情符号的要点
- 全程使用中文输出

请粘贴需要总结的文本内容。

---

### [NestJS 零配置支持 - Vercel](https://vercel.com/changelog/zero-configuration-support-for-nestjs)

**原文标题**: [Zero-configuration support for NestJS - Vercel](https://vercel.com/changelog/zero-configuration-support-for-nestjs)

Vercel 现已支持零配置部署 NestJS 应用，这是一个用于构建高效可扩展 Node.js 服务端应用的流行框架。平台默认采用动态计算资源与按需计费模式，实现自动扩缩容与成本优化。

- 🚀 **零配置部署**：无需额外配置即可在 Vercel 平台快速部署 NestJS 应用程序
- ⚡ **动态资源分配**：基于流量自动调节计算资源，支持应用弹性扩缩容
- 💰 **按需计费**：采用活跃 CPU 计费模式，仅根据实际使用量付费
- 📚 **开发友好**：提供完整示例代码与官方文档支持快速入门
- 🌐 **高效运行**：内置反射元数据支持，保持 NestJS 框架原生特性

---

### [使用 Ace 构建 CLI：Node.js 与 Bun 中的书签应用 - Galaxy 博客](https://blog.galaxycloud.app/building-clis-with-ace-a-bookmarks-app-in-node-js-and-bun/)

**原文标题**: [Building CLIs with Ace: a Bookmarks App in Node.js and Bun - Galaxy Blog](https://blog.galaxycloud.app/building-clis-with-ace-a-bookmarks-app-in-node-js-and-bun/)

本文介绍了如何使用 Ace 框架构建一个书签管理 CLI 应用，涵盖项目初始化、命令创建、交互式提示、数据持久化及测试等完整开发流程。

- 🛠️ 使用 Ace 框架构建 Node.js/Bun 命令行应用，集成提示、日志和表格等功能
- 📁 通过 TypeScript 创建 ESM 项目结构，配置 Ace 内核与命令加载器
- ✨ 实现添加书签命令，支持参数验证与交互式提示补全
- 💾 使用 configstore 持久化存储书签数据到本地 JSON 文件
- 📋 开发查看命令以表格形式展示存储的书签列表
- 🎨 通过全局标志支持 ANSI 彩色输出控制
- ⚡ 利用 Bun 将应用编译为独立可执行文件
- 🧪 框架内置测试支持，可断言日志输出和捕获提示交互

---

### [介绍（Ace 命令）| AdonisJS 文档](https://docs.adonisjs.com/guides/ace/introduction)

**原文标题**: [Introduction (Ace commands) | AdonisJS Documentation](https://docs.adonisjs.com/guides/ace/introduction)

Ace 是 AdonisJS 的命令行框架，用于创建和运行控制台命令，支持别名扩展和编程式执行。

- 🚀 通过`node ace`执行命令，支持 TypeScript 代码运行
- 📋 使用`list`命令或直接运行查看可用命令列表
- ❓ 通过`--help`标志获取单个命令的详细帮助信息
- 🎨 使用`--ansi`标志手动控制彩色输出显示
- 🔄 在`adonisrc.ts`中配置命令别名简化常用命令
- ⚙️ 别名扩展时自动附加预设参数到原命令
- 💻 通过`ace.exec`方法编程式执行命令
- 🔍 使用`ace.hasCommand`检查命令是否存在后再执行

---

### [GitHub - adonisjs/ace：用于创建命令行应用程序的Node.js框架](https://github.com/adonisjs/ace)

**原文标题**: [GitHub - adonisjs/ace: Node.js framework for creating command line applications](https://github.com/adonisjs/ace)

AdonisJS Ace 是一个专为 Node.js 设计的命令行应用开发框架，注重轻量化和测试友好性。

- 🛠️ **轻量级 CLI 框架** - 相比其他命令行框架更加精简，提供简洁的 API
- 🧪 **测试友好设计** - 在构建时充分考虑了测试需求
- 🌐 **活跃社区支持** - 拥有 385 个星标和 36 个分支，被 31,490 个项目使用
- 📄 **MIT 许可证** - 采用开源 MIT 许可证
- 🔄 **持续维护** - 已有 111 个版本发布，最新更新于 2025 年 9 月
- 💻 **TypeScript 开发** - 主要使用 TypeScript 语言（占比 99.6%）

---

### [引言（前言）| AdonisJS 文档](https://docs.adonisjs.com/guides/preface/introduction)

**原文标题**: [Introduction (Preface) | AdonisJS Documentation](https://docs.adonisjs.com/guides/preface/introduction)

AdonisJS 是一个基于 Node.js 的 TypeScript 优先全栈 Web 框架，专注于提供结构化应用开发、现代化工具链和类型安全支持。

- 🚀 提供应用结构、TypeScript 开发环境和 HMR 支持
- ⚡ 减少技术选型时间，专注业务功能开发
- 🎯 后端专注，支持传统模板引擎、JSON API 和 Inertia 前端集成
- 🔒 基于现代 ES 模块、SWC 和 Vite，提供完整类型安全
- 🏗️ 采用 MVC 模式，支持路由、控制器和模型的数据流
- 📚 文档侧重模块参考，推荐 Adocasts 教程入门学习
- 🔄 持续更新维护，近期发布 REPL、ESLint 配置等模块更新

---

### [泰勒试用 DTrace——泰勒·希勒里](https://tylerhillery.com/blog/tyler-tries-dtrace/)

**原文标题**: [Tyler Tries DTrace â Tyler Hillery](https://tylerhillery.com/blog/tyler-tries-dtrace/)

作者在学习 Node.js 流背压机制时，通过官方文档接触到了 DTrace 动态追踪工具，并尝试复现文档中通过 DTrace 测量垃圾回收时间的示例。过程中经历了下载测试视频、修改 Node.js 源码禁用背压机制、编译自定义 Node 版本、配置 DTrace 环境等挑战，最终成功通过 DTrace 观测到禁用背压导致的 GC 时间增加现象。

- 🛠️ 作者在 Node.js 官方文档中发现 DTrace 工具，受 Oxide and Friends 播客影响决定尝试实践
- 📚 背压机制指数据生产速度超过消费速度时，通过暂停生产者防止内存堆积的流量控制机制
- 🎬 为复现示例下载 Big Buck Bunny 测试视频，使用 ffmpeg 合成 9GB 测试文件
- 🔧 通过修改 Node.js 源码中 writeOrBuffer 函数的返回值来禁用背压机制
- 🖥️ 编译 Node.js 时解决环境配置问题，最终成功构建自定义版本
- 🔍 在 macOS 虚拟机上配置 DTrace，发现新版 Node.js 已移除 DTrace 支持后通过 AI 辅助重新添加
- 📊 使用 DTrace 成功测量 GC 时间，验证禁用背压会导致垃圾回收更频繁
- ⚠️ 实验证实背压机制能有效缓解内存压力，避免 GC 过载

---

### [Node.js — 流中的背压机制](https://nodejs.org/en/learn/modules/backpressuring-in-streams)

**原文标题**: [Node.js — Backpressuring in Streams](https://nodejs.org/en/learn/modules/backpressuring-in-streams)

本文介绍了 Node.js 中流（Streams）的反压机制（Backpressure），解释了数据在传输过程中当接收端处理速度跟不上发送端时，数据会在缓冲区堆积的问题。文章详细说明了 Node.js 如何通过流机制自动管理反压，确保内存高效使用，避免系统资源耗尽，并提供了实现自定义流时的最佳实践指南。

- 💥 反压机制防止数据在传输过程中因处理速度不匹配而导致的内存堆积和系统资源耗尽
- 🔄 Node.js 通过流的.pipe() 方法自动处理反压，确保数据平滑流动
- 📊 当 Writable 流的.write() 方法返回 false 时，触发反压，暂停 Readable 流的数据发送
- 🚀 使用 pipeline API 替代.pipe() 可以更好地处理错误和清理资源，特别是在 Node.js 10.x 及以上版本
- 🛠️ 实现自定义流时，必须遵守反压规则，如检查.push() 和.write() 的返回值，避免强制推送数据
- 📉 忽略反压会导致内存使用激增、垃圾回收效率低下，甚至系统崩溃
- 🔧 通过设置 highWaterMark 可以调整流的缓冲区大小，但需谨慎操作
- 📚 使用 readable-stream 库可以确保在不同 Node.js 版本和浏览器中的兼容性

---

### [使用 Node.js 和 Vonage 构建实时交互式 RCS 体验](https://developer.vonage.com/en/blog/build-a-real-time-interactive-rcs-experience-with-node-js-and-vonage)

**原文标题**: [Build a Real-Time Interactive RCS Experience with Node.js and Vonage](https://developer.vonage.com/en/blog/build-a-real-time-interactive-rcs-experience-with-node-js-and-vonage)

本教程展示了如何使用 Node.js 和 Vonage Messages API 构建实时交互式 RCS 体验，通过足球比赛场景演示多步骤互动流程。

- 🚀 RCS 技术通过富媒体和交互按钮提升用户参与度，支持品牌在默认消息应用中创建沉浸式体验
- ⚽ 示例流程：用户选择比赛结果→投票最佳球员→浏览商品轮播，完整代码可在 GitHub 获取
- 🛠️ 环境要求：Node.js、ngrok、Vonage API 账户和 RCS 测试设备，需联系销售团队开通开发者权限
- 📁 项目采用模块化结构，核心文件包括配置管理、消息模板和服务层，便于维护扩展
- 🔗 使用 Express 服务器处理 webhook，根据用户选择动态发送建议回复/独立富卡片/轮播卡片
- 🌐 通过 ngrok 暴露本地服务，配置 Vonage 应用并关联 RCS 代理，实现消息收发功能
- 🎯 消息模板封装了三种 RCS 交互类型，支持快速替换媒体资源和商品链接
- 📱 测试时通过 API 触发初始消息，用户交互会触发后续流程，目前仅实现巴西队分支
- 💡 可扩展其他分支流程，结合设备定位 API 在特定场景触发互动，适用于体育/音乐/零售等多种场景

---

### [Node.js — 在 Node.js 中收集代码覆盖率](https://nodejs.org/en/learn/test-runner/collecting-code-coverage)

**原文标题**: [Node.js — Collecting code coverage in Node.js](https://nodejs.org/en/learn/test-runner/collecting-code-coverage)

Node.js 通过内置测试运行器支持代码覆盖率收集，可使用实验性标志或 API 启用。代码覆盖率是衡量测试期间执行源代码比例的指标，帮助识别测试盲区，通常以百分比形式呈现，数值越高代表测试覆盖越全面。

- 🚀 启用覆盖率：通过`--experimental-test-coverage`标志或`run()`API 的`coverage:true`选项激活
- 📊 覆盖率类型：包含行覆盖率（执行代码行比例）、分支覆盖率（条件分支测试比例）和函数覆盖率（被调用函数比例）
- 🔍 基础示例：演示包含三个函数的模块，其中未测试的`multiply`函数导致覆盖率下降至 66.67%
- 🚫 排除代码：支持通过`/* node:coverage ignore */`注释忽略特定代码段，或使用 CLI 参数排除文件模式
- 🎯 阈值控制：可设置行/分支/函数覆盖率的最低阈值，未达标时进程返回失败状态码
- 📁 文件过滤：通过`--test-coverage-include`和`--test-coverage-exclude`参数精确控制覆盖范围

---

### [为什么 typeof null === object | Piotr Zarycki - 编程博客](https://pzarycki.com/en/posts/js-null/)

**原文标题**: [Why typeof null === object | Piotr Zarycki - Programming Blog](https://pzarycki.com/en/posts/js-null/)

JavaScript 中`typeof null`返回`"object"`是由于历史遗留的设计缺陷，源自 1995 年 Netscape 浏览器的原始实现。在 32 位系统中采用类型标记机制时，空指针（null）的二进制表示与对象类型标记相同（低 3 位均为 000），导致类型判断错误。虽然存在简单的修复方案，但为保持与海量现有代码的兼容性，该行为被保留至今。

- 🔍 `typeof null`返回`"object"`是 JavaScript 的著名历史遗留问题
- ⚙️ 根源在于 Netscape 1.3 的 32 位类型标记系统：对象与 null 共享相同的低位标记（000）
- 🖥️ 空指针`0x00000000`的二进制表示被错误识别为对象类型
- 🔧 当时已有检测 null 的宏（`JSVAL_IS_NULL`）但未在`typeof`实现中使用
- 🌍 2013 年修复提案因破坏向后兼容性被 ECMAScript 标准拒绝
- 💡 正确检测对象应使用：`value !== null && typeof value === 'object'`

---

### [GitHub - elbywan/wretch: 一个围绕 fetch 构建的语法直观的微型封装库。:candy:](https://github.com/elbywan/wretch)

**原文标题**: [GitHub - elbywan/wretch: A tiny wrapper built around fetch with an intuitive syntax. :candy:](https://github.com/elbywan/wretch)

Wretch 是一个轻量级的 fetch 封装库，提供直观的语法简化网络请求和响应处理。

- 🍬 **轻量封装** - 核心代码仅 1.8KB，提供比原生 fetch 更简洁的 API
- 🔄 **自动处理** - 自动处理 JSON 序列化、错误状态码和响应解析
- 🧊 **不可变实例** - 每次调用创建克隆实例，可安全复用配置
- 🔌 **模块化设计** - 支持插件和中间件扩展功能
- 🌐 **多平台兼容** - 支持现代浏览器、Node.js 22+、Deno 和 Bun
- 🦺 **类型安全** - 使用 TypeScript 编写，提供完整类型支持
- 🛡️ **优雅错误处理** - 提供针对不同状态码的错误处理方法
- 📦 **丰富功能** - 包含查询字符串、FormData、进度跟踪、请求中止等常用功能
- 🔄 **请求重试** - 内置重试中间件，支持自定义重试条件
- ⚡ **性能优化** - 支持请求去重和缓存中间件，提升应用性能

---

### [GitHub - elbywan/wretch: 一个围绕 fetch 构建的语法直观的微型封装库。:candy:](https://github.com/elbywan/wretch#because-having-to-write-a-second-callback-to-process-a-response-body-feels-awkward)

**原文标题**: [GitHub - elbywan/wretch: A tiny wrapper built around fetch with an intuitive syntax. :candy:](https://github.com/elbywan/wretch#because-having-to-write-a-second-callback-to-process-a-response-body-feels-awkward)

Wretch 是一个轻量级的 fetch 封装库，提供直观的语法简化网络请求和响应处理。

- 🍬 **轻量简洁** - 核心代码仅 1.8KB，提供比原生 fetch 更优雅的 API
- 🔄 **自动处理** - 自动处理 JSON 序列化、错误状态码检查和响应解析
- 🧩 **模块化设计** - 支持插件系统和中间件，可扩展功能
- 🌐 **多平台兼容** - 支持现代浏览器、Node.js 22+、Deno 和 Bun
- 🛡️ **类型安全** - 使用 TypeScript 编写，提供完整的类型支持
- ⚡ **常用功能** - 内置查询字符串、FormData、进度监控、请求重试等
- 🔧 **配置复用** - 不可变实例设计，可安全重用配置
- 📦 **灵活安装** - 支持 npm、CDN 等多种安装方式

---

### [Release 3.0.0 · elbywan/wretch · GitHub](https://github.com/elbywan/wretch/releases/tag/3.0.0)

**原文标题**: [Release 3.0.0 · elbywan/wretch · GitHub](https://github.com/elbywan/wretch/releases/tag/3.0.0)

Wretch v3 是一个重大版本更新，带来了更小、更快、功能更强大的 fetch 封装库，具备改进的类型安全、更智能的默认设置和令人兴奋的新特性。

- 🚀 要求 Node.js 22 或更高版本，直接使用原生 Web API，实现零 polyfill 开销，显著减小包体积并提升性能
- 🎯 引入 `.customError()` 方法替代 `.errorType()`，提供完整的 TypeScript 支持，允许自定义错误属性和解析方式
- 🔄 重试中间件默认跳过 4xx 客户端错误，仅针对 5xx 服务器错误和网络故障进行重试，符合 HTTP 语义
- 📤 进度插件新增上传进度监控功能，支持实时跟踪上传进度，在 Node.js 中无缝工作
- 🎨 支持一次性传递多个插件，使配置更简洁清晰
- 💎 多个插件方法改用选项对象而非位置参数，提升 API 可维护性和可读性
- 🔗 新增 `.toFetch()` 方法，可将 Wretch 请求链转换为标准 fetch 调用
- 🧹 移除全局配置方法，改为每个实例单独配置，架构更简洁
- 🔧 现代化开发栈：使用 Rolldown 打包、原生 Node.js 测试、文档代码片段自动化测试、全面跨运行时测试和安全更新

---

### [格拉夫尔](https://graffle.js.org/)

**原文标题**: [Graffle](https://graffle.js.org/)

overview summary
Graffle 遵循 GraphQL over HTTP 和 GraphQL 多部分请求规范，确保与标准兼容。

- 🎯 符合 GraphQL over HTTP 规范
- 📄 遵循 GraphQL 多部分请求规范
- ✅ 确保技术标准兼容性

---

### [GitHub - cure53/DOMPurify：DOMPurify - 一款仅限 DOM、超快速、极度宽容的 HTML、MathML 和 SVG 跨站脚本（XSS）清理器。DOMPurify 采用安全默认设置工作，同时提供大量可配置选项和钩子。演示：](https://github.com/cure53/DOMPurify)

**原文标题**: [GitHub - cure53/DOMPurify: DOMPurify - a DOM-only, super-fast, uber-tolerant XSS sanitizer for HTML, MathML and SVG. DOMPurify works with a secure default, but offers a lot of configurability and hooks. Demo:](https://github.com/cure53/DOMPurify)

DOMPurify 是一个专为 HTML、MathML 和 SVG 设计的快速、高容错性的 XSS 净化库，通过默认安全配置提供高度可定制性，能有效清除恶意代码并防止跨站脚本攻击。

- 🛡️ 核心功能是净化 HTML 内容并阻止 XSS 攻击，支持现代浏览器及 Node.js 环境
- ⚡ 采用浏览器原生技术实现极致净化速度，输入脏 HTML 即可返回安全内容
- 🎯 默认支持 HTML5/SVG/MathML，可通过配置限定特定标签和属性
- 🚫 自动移除危险元素（如 onerror 事件）并保留安全内容（如纯图片标签）
- 🔧 提供丰富配置选项：自定义允许列表/禁止列表、URI 处理、返回类型控制等
- 🌐 支持服务端运行（需配合 jsdom），提供 TypeScript 类型定义和 React 绑定
- 🐛 设有安全漏洞奖励计划，持续更新维护并经过多浏览器自动化测试验证
- 📚 提供实时演示页面和详细文档，包含大量代码示例和配置案例

---

### [DOMPurify 3.3.0 "极光"](https://cure53.de/purify)

**原文标题**: [DOMPurify 3.3.0 "Aurora"](https://cure53.de/purify)

DOMPurify 3.3.0 版本是一个专注于 DOM 处理的超快速 XSS 净化工具，支持 HTML、SVG 和 MathML 内容的安全清理。

- 🛡️ 专为防御 XSS 攻击设计的 DOM 净化工具
- ⚡ 具备超高速处理性能与高容错特性
- 🌐 支持 HTML/SVG/MathML 多种格式内容净化
- 🧪 提供实时演示环境可测试自定义 payload
- 📝 支持多种输出方式：控制台显示/DOM 写入/jQuery 处理
- ⏱️ 内置性能监控显示原始/净化 HTML 处理耗时
- 🔄 可选自动转换功能增强兼容性

---

### [首页 - 文档](https://imapflow.com/)

**原文标题**: [
      Home - Documentation
  ](https://imapflow.com/)

ImapFlow 是一个专为 Node.js 设计的现代化、易用的 IMAP 客户端库，旨在简化 IMAP 协议交互，无需深入了解 IMAP 细节即可通过直观 API 管理邮件。

- 📧 专为 Node.js 设计的 IMAP 客户端库，提供简单易用的 API 接口
- 🔗 可搭配 EmailEngine 将 IMAP 账户转换为 REST API，便于集成
- 🛠️ 自动处理 IMAP 扩展功能，兼容不同服务器特性
- 📥 通过 npm 安装：`npm install imapflow`，支持 Promise 异步操作
- 🔒 提供邮箱锁定机制，确保操作安全并支持邮件获取和列表读取
- 📚 详细 API 文档和 MIT 开源许可，代码托管于 GitHub

---

### [GitHub - lukeacl/atsippy: 支持重连压缩的 Bluesky Jetstream 服务客户端 (https://github.com/bluesky-social/jetstream)](https://github.com/lukeacl/atsippy)

**原文标题**: [GitHub - lukeacl/atsippy: A reconnecting compression supporting client for the Bluesky Jetstream (https://github.com/bluesky-social/jetstream) service.](https://github.com/lukeacl/atsippy)

ATSippy 是一个为 Bluesky Jetstream 服务设计的客户端，支持重连和压缩功能，用于订阅和处理来自 Bluesky 社交网络的数据流。

- 🔄 支持自动重连和压缩功能，确保稳定连接和数据传输
- 📦 可通过 npm 安装，使用 TypeScript 编写，兼容 Bluesky Jetstream 服务
- ⚙️ 可配置连接参数，包括端点、重连延迟、压缩使用及订阅的数据集合和 DID
- 📡 提供多种事件监听，如连接、心跳、数据提交、创建、更新、删除等操作
- 📄 采用 MPL-2.0 许可证，项目开源，目前有 5 个星标，暂无分支

---

### [介绍 Jetstream | Bluesky](https://docs.bsky.app/blog/jetstream)

**原文标题**: [Introducing Jetstream | Bluesky](https://docs.bsky.app/blog/jetstream)

Jetstream 是 AT 协议中 Firehose 数据流的简化替代方案，专为降低开发门槛和带宽消耗而设计，支持 JSON 格式和数据过滤功能。

- 🚀 提供简化的 JSON 数据格式，替代复杂的二进制 CBOR/CAR 解析
- 📡 支持按数据集合 (NSID) 和存储库 (DID) 进行灵活过滤
- 💻 作为开源中间件，消费 Firehose 数据并分发给多个订阅者
- 🌐 已在美东美西部署多个公共实例供开发者使用
- ⚡ 显著降低带宽消耗并支持数据压缩
- 🔄 源于工程师个人项目，现已升级为团队维护项目
- ⚠️ 不含密码学签名验证，适用于非关键业务场景
- 🎯 特别适合实验项目、原型开发和新应用调试
- 📊 不适用于数据归档、内容审核等需要身份验证的场景
- 🛠️ 未来计划将部分优势整合至正式协议规范

---

### [GitHub - faker-js/faker：在浏览器和Node.js中生成海量模拟数据](https://github.com/faker-js/faker)

**原文标题**: [GitHub - faker-js/faker: Generate massive amounts of fake data in the browser and node.js](https://github.com/faker-js/faker)

Faker 是一个用于生成大量虚假但逼真数据的 JavaScript 库，支持浏览器和 Node.js 环境，主要用于测试和开发。

- 🚀 支持生成人物信息、地理位置、日期时间、金融数据、商业产品等多种类型的虚假数据
- 🌍 提供超过 70 种本地化语言版本，可生成符合不同地区习惯的逼真数据
- 📦 通过 npm 安装，支持 ESM 和 CommonJS 两种模块系统
- ⚙️ 支持设置随机种子，确保生成结果可重现
- 🔧 提供模板功能，可以组合多个 API 方法生成复杂数据格式
- 📊 项目在 GitHub 上获得 14.5k 星标，被 24.3 万多个项目使用
- 🤝 采用 MIT 开源协议，由社区共同维护开发
- 💻 支持 TypeScript 和 JavaScript，主要使用 TypeScript 开发

---

### [发布 v1.8.0 · yamadashy/repomix · GitHub](https://github.com/yamadashy/repomix/releases/tag/v1.8.0)

**原文标题**: [Release v1.8.0 · yamadashy/repomix · GitHub](https://github.com/yamadashy/repomix/releases/tag/v1.8.0)

Repomix v1.8.0 版本发布，新增 Claude Code 官方插件支持、完整目录结构显示功能和 Dart 语言压缩优化，同时修复了若干问题。

- 🚀 新增 Claude Code 官方插件，支持代码库打包、搜索和自然语言操作
- 📁 新增完整目录结构显示选项，提供更全面的项目上下文
- ⚡ 新增 Dart 语言树形压缩支持，可减少约 50% 的 token 使用
- 🐛 修复了 Claude Code 插件市场模式验证问题
- 👥 感谢贡献者 slavakurilyak 和 ramarivera 的代码贡献
- 📦 可通过 npm update -g repomix 命令进行更新

---

### [Node-oracledb 6.10 在精简模式下引入高级队列 (AQ) 支持及其他多项功能 | Sharad Chandran | Oracle 开发者 | 2025 年 10 月 | Medium](https://medium.com/oracledevs/node-oracledb-6-10-introduces-advanced-queuing-aq-support-in-thin-mode-and-much-more-d8a88bf5966d)

**原文标题**: [Node-oracledb 6.10 introduces Advanced Queuing (AQ) support in Thin mode and much more | by Sharad Chandran | Oracle Developers | Oct, 2025 | Medium](https://medium.com/oracledevs/node-oracledb-6-10-introduces-advanced-queuing-aq-support-in-thin-mode-and-much-more-d8a88bf5966d)

node-oracledb 6.10 版本发布，新增 Thin 模式高级队列支持、连接池代理用户外部认证、配置缓存时间控制及 SODA 扩展 JSON 数据类型等功能，提升开发灵活性与应用部署效率。

- 🚀 Thin 模式支持 Oracle 高级队列 (AQ)，无需启用 Thick 模式即可使用经典队列
- 🔐 连接池新增代理用户外部认证功能，增强数据库连接安全性  
- ⏱️ 支持配置缓存存活时间参数，灵活控制集中配置提供商的缓存策略
- 📄 SODA 操作新增扩展 JSON 数据类型支持，实现无缝数据转换
- 📦 消息出队选项新增传递模式设置，支持持久化与缓冲两种模式
- 🏷️ 查询结果元数据新增数据库原始列名字段，便于精准识别数据来源
- 🔧 修复多项 GitHub 反馈问题，优化模块稳定性

（注：原文中关于安装方式、资源链接等辅助信息已按摘要要求过滤）

---

### [GitHub - Blizzard/node-rdkafka: Node.js 的 librdkafka 绑定库](https://github.com/Blizzard/node-rdkafka)

**原文标题**: [GitHub - Blizzard/node-rdkafka: Node.js bindings for librdkafka](https://github.com/Blizzard/node-rdkafka)

这是一个基于 Node.js 的 Apache Kafka 客户端库，它封装了 librdkafka C/C++ 库，提供高性能的消息生产和消费功能。

- 🚀 高性能 Node.js Kafka 客户端，基于 librdkafka 2.12.0 构建
- 📝 支持消息生产和消费，提供流式 API 和标准 API 两种使用方式
- ⚙️ 丰富的配置选项，支持回调函数和事件监听
- 🔄 内置消费者组重平衡机制，支持手动和自动分区分配
- 📊 提供管理客户端，支持主题创建、删除和分区扩展
- 🖥️ 支持多种操作系统，包括 Linux、Mac 和 Windows
- 🧪 包含完整的单元测试和端到端集成测试
- 📄 采用 MIT 开源协议，目前有 2.2k 星标和 407 个分支

---

### [GitHub - openai/openai-node：OpenAI API 官方 JavaScript / TypeScript 库](https://github.com/openai/openai-node)

**原文标题**: [GitHub - openai/openai-node: Official JavaScript / TypeScript library for the OpenAI API](https://github.com/openai/openai-node)

OpenAI 官方提供的 JavaScript/TypeScript 库，用于访问 OpenAI REST API，支持多种运行环境和高级功能。

- 📦 提供官方 JavaScript/TypeScript 库，可通过 npm 安装或从 JSR 导入
- 🤖 支持 Responses API 和 Chat Completions API 两种文本生成方式
- 🌊 支持流式响应和多种文件上传格式
- 🔒 提供 Webhook 验证功能，确保请求安全性
- ⚠️ 完善的错误处理机制，包含多种错误类型分类
- 🔄 自动重试机制，可配置重试次数和超时时间
- 📄 支持自动分页，方便处理大量数据
- ☁️ 兼容 Microsoft Azure OpenAI 服务
- 🛠️ 提供高级功能：原始响应访问、自定义日志、代理配置等
- 🌐 支持多种运行时环境：Node.js、Deno、Bun、Cloudflare Workers 等
- ⚡ 包含实时 API，支持 WebSocket 连接实现低延迟交互

---

### [GitHub - google/zx：编写更优脚本的工具](https://github.com/google/zx)

**原文标题**: [GitHub - google/zx: A tool for writing better scripts](https://github.com/google/zx)

这是一个用于编写更好脚本的 JavaScript 工具库，提供跨平台子进程封装和参数转义功能。

- 🚀 支持多种 JavaScript 运行时（Node.js、Bun、Deno、GraalVM）
- 📦 提供便捷的子进程操作和参数处理功能
- 🌐 兼容 Linux、macOS 和 Windows 系统
- 📚 支持 CommonJS 和 ESM 模块规范
- ⭐ 在 GitHub 上获得 44.7k 星标和 1.2k 分支
- 🔧 可同时使用 JavaScript 和 TypeScript 进行开发
- 📄 采用 Apache-2.0 开源协议
- 💻 旨在简化复杂脚本的编写过程

---

### [GitHub - sindresorhus/terminal-image：在终端中显示图像](https://github.com/sindresorhus/terminal-image)

**原文标题**: [GitHub - sindresorhus/terminal-image: Display images in the terminal](https://github.com/sindresorhus/terminal-image)

该仓库是一个用于在终端中显示图像的开源 Node.js 模块，支持多种终端协议和图像格式。

- 🖼️ 支持在终端中显示 PNG、JPEG 和 GIF 图像，可自动适配不同终端的图形协议
- 🎯 提供灵活的尺寸设置选项，支持百分比或行列数定义，默认保持宽高比
- ⚡ 支持 GIF 动画播放，可自定义帧率和渲染方式
- 🔧 提供 buffer 和 file 两种 API 调用方式，支持远程图像显示
- 🌈 自动选择最佳渲染协议：Kitty 图形协议、iTerm2 内联图像协议或 ANSI 块字符回退
- 📦 采用 MIT 开源协议，在 npm 上有 25k+ 项目使用
- 🛠️ 包含完整的类型定义和测试用例，开发文档详细

---

### [GitHub - sindresorhus/got：🌐 适用于 Node.js 的人性化且功能强大的 HTTP 请求库](https://github.com/sindresorhus/got)

**原文标题**: [GitHub - sindresorhus/got: 🌐 Human-friendly and powerful HTTP request library for Node.js](https://github.com/sindresorhus/got)

这是一个名为 Got 的 Node.js HTTP 请求库的 GitHub 仓库页面概览，该库功能强大且易于使用。

- 🌐 专为 Node.js 设计的人性化且功能强大的 HTTP 请求库
- ⭐ 获得 14.8k 星标和 972 次分叉，表明其受欢迎程度和社区活跃度
- 📦 仅支持 ESM 模块，不再提供 CommonJS 导出
- 🔄 默认支持失败重试、JSON 模式处理和进度事件等高级功能
- 🔌 提供插件系统，支持 AWS、GitHub、GitLab 等服务的便捷封装
- 📊 与 axios、node-fetch 等库相比，支持 HTTP/2、分页 API 等更多功能
- 🏢 被 Segment、Natural Cycles 等多家公司用于生产环境
- 📄 采用 MIT 许可证，由社区支持维护

---

### [GitHub - pinojs/pino：🌲 超快速、纯天然的 JSON 日志记录器](https://github.com/pinojs/pino)

**原文标题**: [GitHub - pinojs/pino: 🌲 super fast, all natural json logger](https://github.com/pinojs/pino)

Pino 是一个专为 Node.js 设计的高性能 JSON 日志记录库，具有极低的开销和丰富的生态系统支持。

- 🌲 超快速且纯天然的 JSON 日志记录器，适用于 Node.js 环境
- 📊 极低的开销设计，性能比同类日志库快 5 倍以上
- 🚀 支持异步日志记录和子日志记录器功能
- 🔧 提供传输机制，建议在独立线程中处理日志
- 📦 支持通过 webpack 或 esbuild 等工具进行打包
- 🌐 兼容多种 Web 框架，包括 Fastify、Express、Hapi 等
- 📄 采用 MIT 开源许可证，拥有活跃的社区贡献
- ⭐ GitHub 上获得 16.6k 星标，被 61.5 万多个项目使用

---

### [ESLint v9.38.0 发布 - ESLint - 可插拔 JavaScript 代码检查工具](https://eslint.org/blog/2025/10/eslint-v9.38.0-released/)

**原文标题**: [ESLint v9.38.0 released - ESLint - Pluggable JavaScript Linter](https://eslint.org/blog/2025/10/eslint-v9.38.0-released/)

ESLint v9.38.0 版本发布，作为一次小版本更新，主要改进了插件配置解析机制并修复了若干问题。

- 🔧 插件配置解析增强：defineConfig() 助手现支持直接识别 flat/recommended 配置格式
- 🎯 复杂度规则优化：仅高亮函数头部而非整个函数体
- 🐛 精度丢失修复：修正 no-loss-of-precision 规则对科学计数法的误报
- 📦 依赖类型支持：提升 pnpm 孤立依赖的类型检测准确性
- 📖 文档改进：增强网页可访问性与规则文档格式规范
- 🔄 核心升级：同步更新 @eslint/js 至 9.38.0 版本
- 🧹 代码维护：重构类型引用、修复拼写错误并更新 CI 工作流

---

### [Holepunch - 高级 Node.js 软件工程师（全球远程，全职）](https://holepunch.recruitee.com/o/senior-node-engineer?source=Node-Weekly)

**原文标题**: [Holepunch - Senior Node.js Software Engineer (100% Remote, Worldwide)](https://holepunch.recruitee.com/o/senior-node-engineer?source=Node-Weekly)

Holepunch 是一家专注于构建去中心化互联网架构的科技公司，通过其开源技术栈 Pear 开发点对点（P2P）平台，旨在赋予用户数据控制权并提升隐私保护。公司正在招聘远程 Node.js 软件工程师，以推动 P2P 技术发展和生态系统扩展。

- 🌐 公司使命是重新定义互联网架构，利用 P2P 技术消除传统服务器需求，确保用户数据自主权和隐私
- 📱 旗舰产品 Keet 展示 P2P 通信应用的潜力，支持消息传递、文件共享和协作功能
- 💻 招聘 Node.js 工程师需具备高质量代码编写经验，熟悉 C/C++ 或本地绑定为加分项
- 🧩 要求模块化开发能力，包括构建 npm 模块和管理模块化代码库
- 🔍 强调测试与调试技能，确保软件可靠性和性能优化
- ❤️ 候选人需对 P2P 技术充满热情，有相关开发经验者优先
- 🌍 职位完全远程，要求具备全球团队协作经验
- 🚀 加入后将参与开创性技术工作，推动去中心化网络未来建设

---

### [ConfigCat - 团队功能特性开关服务](https://configcat.com/promotions/node-weekly/?utm_source=cooperpress_newsletter&utm_medium=sponsor&utm_campaign=cooperpress_node_202510)

**原文标题**: [ConfigCat - Feature Flag Service for Teams](https://configcat.com/promotions/node-weekly/?utm_source=cooperpress_newsletter&utm_medium=sponsor&utm_campaign=cooperpress_node_202510)

ConfigCat 是一个功能开关管理平台，帮助开发团队通过功能标志控制功能发布流程，支持渐进式发布和即时回滚。

- 🚀 **功能发布控制** - 支持定向用户群体、渐进式功能发布，出现问题时立即关闭功能
- ⚡ **快速集成** - 10 分钟完成设置，无需信用卡，提供 NODE25 优惠码享 25% 折扣
- 🔧 **技术实现** - 通过 ConfigCat.js SDK 轻松管理功能开关，支持暗黑模式、销售模式等场景
- 🛡️ **安全隐私** - 不收集用户数据，功能标志在客户端评估，满足合规要求
- 💰 **透明定价** - 永久免费版含 10 个功能标志，专业版$82/月起，支持无供应商锁定
- 🌟 **用户认可** - 获多家企业好评，比 LaunchDarkly 更优性价比，简单易用且功能强大
- 🏢 **企业级服务** - 提供私有化部署选项，支持 ISO 27001 认证，99.99% 高可用性保障

---

### [如何修复任何 Bug——过度反应篇](https://overreacted.io/how-to-fix-any-bug/)

**原文标题**: [How to Fix Any Bug — overreacted](https://overreacted.io/how-to-fix-any-bug/)

在 React Router 应用中，滚动功能因网络请求调用而失效，作者通过系统化调试方法定位到 ScrollRestoration 组件与滚动操作的冲突问题。

- 🐛 滚动抖动问题出现在调用服务器请求后，原本正常的 scrollIntoView 功能失效
- 🤖 尝试用 Claude 修复失败，因 AI 缺乏可视化验证能力且未建立有效复现步骤
- 🔍 建立可靠复现案例：通过测量滚动位置变化验证问题存在
- ⚠️ 复现案例简化风险：需确保新案例与原始问题关联性
- 🧪 采用逐步删除法：持续移除代码组件并验证问题是否依然存在
- 📉 保持调试纪律：每次修改后必须确认 bug 仍然重现
- 🎯 最终定位根因：React Router 旧版 ScrollRestoration 组件在路由验证时错误触发
- 💡 解决方案：更新 React Router 版本或调整组件嵌套结构

---

### [沙盒 SDK](https://sandbox.cloudflare.com/)

**原文标题**: [Sandbox SDK](https://sandbox.cloudflare.com/)

好的，请提供您需要总结的文本内容，我将按照您要求的格式进行整理：
- 顶部提供概述摘要
- 用中文生成带表情符号的要点列表
- 确保内容简洁且包含关键信息

请粘贴需要总结的文本。

---

### [PostgreSQL：PostgreSQL 18 正式发布！](https://www.postgresql.org/about/news/postgresql-18-released-3142/)

**原文标题**: [PostgreSQL: PostgreSQL 18 Released!](https://www.postgresql.org/about/news/postgresql-18-released-3142/)

PostgreSQL 18 正式发布，这是世界上最先进的开源数据库的最新版本，通过异步 I/O 子系统提升性能达 3 倍，支持虚拟生成列和 OAuth 2.0 认证，优化了升级流程和查询性能，增强了开发者体验和安全性。

- 🚀 异步 I/O 子系统提升存储读取性能达 3 倍，支持并发 I/O 请求
- 📊 升级时保留规划器统计信息，减少性能波动，加速升级过程
- 🔍 多列 B 树索引支持"跳过扫描"，优化 OR 条件查询和表连接性能
- 💻 虚拟生成列默认计算查询时值，支持逻辑复制和 UUIDv7 生成
- 🔒 引入 OAuth 2.0 认证，弃用 MD5 密码验证，支持 SCRAM 认证
- 📝 新增 PG_UNICODE_FAST 排序规则，加速文本处理和模式匹配
- 🔄 逻辑复制默认并行流式传输，支持自动删除空闲复制槽
- 📈 优化 VACUUM 策略，EXPLAIN 增强显示缓冲区和索引查找详情
- ⚙️ 默认启用页面校验和，新增 PostgreSQL 有线协议版本 3.2

---

### [等待 Postgres 18：利用异步 I/O 加速磁盘读取](https://pganalyze.com/blog/postgres-18-async-io)

**原文标题**: [Waiting for Postgres 18: Accelerating Disk Reads with Asynchronous I/O](https://pganalyze.com/blog/postgres-18-async-io)

PostgreSQL 18 引入异步 I/O 架构革新，通过新的 io_method 配置实现非阻塞磁盘读取，在云环境中显著提升查询性能，同时带来监控方式和参数调优的新挑战。

- 🚀 异步 I/O 支持三种模式：sync（同步）、worker（工作进程）、io_uring（Linux 高性能接口）
- ⚡ AWS 基准测试显示 worker 模式提升 1.5 倍性能，io_uring 模式实现近 3 倍性能飞跃
- 🔧 新增 io_method 参数需重启生效，effective_io_concurrency 现可直接控制预读请求数量
- 📊 监控方式变革：需使用 pg_aios 视图追踪异步 I/O 状态，EXPLAIN ANALYZE 可能低估实际 I/O 耗时
- 🌩️ 特别适合云环境：有效降低网络存储延迟影响，为未来异步写入功能奠定基础
- ⚠️ 当前限制：仅支持顺序扫描、位图堆扫描和 VACUUM 等读操作，写入仍保持同步

---

### [Postgres 17 与 18 性能基准测试对比 —— PlanetScale](https://planetscale.com/blog/benchmarking-postgres-17-vs-18)

**原文标题**: [Benchmarking Postgres 17 vs 18 â PlanetScale](https://planetscale.com/blog/benchmarking-postgres-17-vs-18)

PostgreSQL 18 与 17 的性能基准测试对比，重点评估新增的 I/O 处理方式在不同硬件配置下的表现。

- 📊 PostgreSQL 18 引入 io_method 配置选项，支持 sync（兼容 17）、worker（新默认）和 io_uring 三种 I/O 处理模式
- ⚡ 单连接测试中，网络存储场景下 worker 模式性能最优，本地 NVMe 硬盘则各模式差异不大
- 🔄 高并发测试显示 io_uring 在本地 NVMe 存储的极端场景下略有优势，但整体仍以 worker 模式表现更稳定
- 💸 成本分析表明配备本地 NVMe 硬盘的实例兼具最佳性价比和性能表现
- 🔍 io_uring 未全面领先的原因包括：索引扫描暂不支持异步、内存操作瓶颈及特定场景并发需求
- 🏆 结论推荐：本地硬盘为性能首选，worker 模式作为默认配置平衡性最佳，不同 I/O 配置需按实际场景选择

---

### [破解《纽约时报》点数谜题——安德鲁·希利](https://healeycodes.com/solving-nyt-pips-puzzle)

**原文标题**: [Solving NYT's Pips Puzzle — Andrew Healey](https://healeycodes.com/solving-nyt-pips-puzzle)

作者开发了一个用于解决《纽约时报》Pips 骨牌拼图游戏的求解器，通过深度优先搜索算法结合多种优化策略，将求解效率提升了约 16 倍，并构建了可视化界面用于调试和展示搜索过程。

- 🧩 游戏规则涉及在特定区域内放置骨牌，需满足求和、相等、不等或大小比较等限制条件
- 🖥️ 采用 TypeScript 定义了游戏数据结构，包括骨牌类型、坐标系统和区域规则
- 🔍 核心算法基于深度优先搜索，通过构建邻接表处理非矩形游戏板
- 🚫 优化一：跳过相同数字骨牌的重复方向检查，节点数从 21337 降至 7618
- 🧱 优化二：检测并避免创建孤立空单元格，节点数进一步降至 5777
- 📊 优化三：智能区域检查，提前排除不可行分支，最终节点数降至 1355
- 🎨 开发了 React 可视化界面，包含游戏板展示和搜索树动态绘制
- ⚡ 通过缓冲区和帧率控制解决了性能问题，完整代码已开源

---

