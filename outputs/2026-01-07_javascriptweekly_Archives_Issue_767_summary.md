### [JavaScript 周刊第 767 期：2026 年 1 月 6 日](https://javascriptweekly.com/issues/767)

**原文标题**: [JavaScript Weekly Issue 767: January 6, 2026](https://javascriptweekly.com/issues/767)

JavaScript 周刊 2026 年首期发布，宣布改为每周二发送，并回顾了 2025 年 JavaScript 生态的重要动态与新年展望。

- 🏆 **2025 年 JavaScript 新星榜单**：n8n 和 React Bits 超越 shadcn/ui 位列前二，该年度总结已进入第十年
- 🤖 **AI 驱动的无感测试工具**：Meticulous 推出基于 Chromium 的 E2E 测试方案，获 Dropbox 等企业采用
- 🔋 **嵌入式 JavaScript 新引擎**：Fabrice Bellard 发布 MicroQuickJS，仅需 10KB 内存即可运行
- 📦 **包管理器年度变革**：pnpm 在 2025 年实现重大转型，最新版本增强安全策略控制
- 🦕 **Deno 游戏开发教程**：官方博客连载恐龙跑酷游戏制作指南，展示 Deno 实战应用
- ⚡ **TypeScript 性能优化案例**：大型单体仓库通过多项技术手段显著提升编译效率
- 📅 **跨框架日历组件**：Schedule-X 3.6 支持 React/Vue 等六大框架，提供 Material Design 风格
- 🎨 **CSS 网格布局革新**：Safari 技术预览版已实现 CSS Grid Lanes 原生瀑布流布局
- 📊 **数据可视化生态更新**：Recharts 3.6 强化 D3 集成，Color.js v0.6 向正式版迈进
- 🔌 **开发者工具升级潮**：Bruno 3.0 重构 API 客户端界面，JoltPhysics.js 1.0 实现物理引擎移植

---

### [2025 年 JavaScript 新星](https://risingstars.js.org/2025/en)

**原文标题**: [2025 JavaScript Rising Stars](https://risingstars.js.org/2025/en)

2025 年 JavaScript 生态回顾：AI 驱动创新与安全挑战并存，n8n 以惊人增长领跑年度项目，Bun 被 Anthropic 收购预示 AI 工具新方向，React 生态在服务器端演进中面临复杂性与安全考验，移动开发领域迎来新框架竞争，全栈与工具链持续迭代，开发者需在拥抱 AI 自动化与保障代码质量间寻找平衡。

- 🏆 **年度总冠军 n8n**：AI 增强的无代码工作流自动化平台，全年获超 11.2 万星，反映自动化工具与 AI 代理工作流需求激增
- ⚛️ **React 生态演进**：React 重登前端框架榜首，React 19 引入 Activity API，服务器组件发展伴随 React2Shell 安全漏洞警示
- 🆕 **全栈新星 Motia**：后端框架类别冠军，通过 Steps 抽象统一 API、队列、工作流与 AI 代理开发范式
- 🔧 **工具链变革**：Bun 获 Anthropic 收购转向 AI 代理运行时，Vite 生态推出 Rolldown 等 Rust 工具，TypeScript 启动 Go 语言重写计划
- 🤖 **AI 工作流崛起**：n8n、Dyad、Stagehand 等 AI 自动化工具占据榜单，标志开发重点从聊天机器人转向可委托工作流构建
- 📱 **移动开发变局**：Valdi 与 Lynx 新框架超越 React Native，Dioxus 尝试用 Rust 实现跨平台渲染，React Native 持续向稳定版演进
- 🛡️ **安全挑战凸显**：npm 供应链遭受"Shai-Hulud"大规模攻击，React 服务器组件漏洞暴露新兴技术安全风险
- 🔮 **生态趋势展望**：指令模式（use client/use server）引发语言特性讨论，Remix 3 将弃用 React 转向 Web 原生，AI 工作流技能成关键竞争力

---

### [AI 工作流自动化平台与工具 - n8n](https://n8n.io/)

**原文标题**: [AI Workflow Automation Platform & Tools - n8n](https://n8n.io/)

n8n 是一款面向技术团队的高度灵活 AI 工作流自动化平台，提供可视化拖拽和代码编辑两种构建方式，支持自托管或云端部署，能够创建多步骤 AI 代理并集成超过 500 种应用，帮助企业快速实现 AI 驱动的自动化流程。

- 🤖 **AI 工作流构建**：支持通过拖拽或代码方式快速集成各类大语言模型，构建多步骤 AI 代理系统
- 🏢 **企业级功能**：提供完全自托管选项、SSO 身份验证、高级权限管理等安全协作功能
- 🔌 **广泛集成能力**：拥有超过 500 种应用集成，涵盖通信、开发、网络安全等多个类别
- 💻 **混合开发模式**：同时支持可视化界面和 JavaScript/Python 代码编辑，满足不同技术需求
- 📊 **实际应用场景**：已在 IT 运维、安全运营、销售分析等多个领域实现自动化效率提升
- 🌟 **社区认可度高**：GitHub 获 16.6 万星标，G2 评分 4.9/5，拥有 20 万 + 社区成员
- 🚀 **快速部署验证**：提供 1700+ 模板和实时调试功能，支持快速测试和迭代工作流
- 🏆 **客户成功案例**：帮助 Delivery Hero 每月节省 200 小时，StepStone 将 2 周工作缩短至 2 小时

---

### [React Bits - React 动画 UI 组件](https://reactbits.dev/)

**原文标题**: [React Bits - Animated UI Components For React](https://reactbits.dev/)

本文介绍了人工智能在医疗领域的应用现状与前景，重点探讨了其在疾病诊断、治疗方案优化及医疗管理效率提升方面的作用，并简要提及了相关的伦理挑战。

- 🤖 AI 辅助诊断系统能通过分析医学影像快速识别病灶，提高早期疾病检出率
- 🧬 机器学习算法可整合基因组数据与临床信息，为患者提供个性化治疗方案
- ⚡ 智能调度系统优化医院资源分配，减少患者等候时间并缓解医护压力
- 📊 电子健康记录结合预测模型实现慢性病风险预警，助力预防医学发展
- ⚖️ 数据隐私保护与算法透明度成为医疗 AI 推广过程中需要解决的关键伦理问题

---

### [精密 AI——无需编写测试的自动化前端测试](https://www.meticulous.ai/?utm_source=jsweekly&utm_medium=referral&utm_campaign=jan6th2026)

**原文标题**: [Meticulous AI - Automated Frontend Testing Without Writing Tests](https://www.meticulous.ai/?utm_source=jsweekly&utm_medium=referral&utm_campaign=jan6th2026)

Meticulous AI 是一款创新的自动化测试工具，通过记录用户与应用的日常交互，自动生成并维护覆盖所有代码分支和用户流程的测试套件，无需手动编写或维护测试，从而帮助开发团队快速、可靠地发布无回归的代码。

- 🚀 **无需编写测试** – 通过记录用户交互自动生成测试，覆盖所有边缘情况和用户流程，无需手动编写或维护测试代码。
- 🔄 **自动更新测试套件** – 随着应用功能的变化，测试套件会自动添加新测试并移除过时的测试，保持测试的时效性和完整性。
- ⚡ **消除测试不稳定** – 从底层构建的确定性调度引擎，彻底消除测试中的不稳定现象，并支持高速并行测试，数千个测试可在 120 秒内完成。
- 🛡️ **安全无副作用** – 通过模拟后端响应进行测试，避免因数据变化导致的误报，无需设置测试账户或模拟数据，测试过程无副作用。
- 🌐 **广泛集成支持** – 支持多种前端框架（如 React、Vue、Angular 等），只需添加脚本标签即可快速集成到开发、预演和生产环境。
- 📈 **提升开发效率** – 帮助团队在合并代码前预览更改对用户流程的影响，防止回归问题，显著提升代码发布速度和开发信心。

---

### [mquickjs/README.md 位于主分支 · bellard/mquickjs · GitHub](https://github.com/bellard/mquickjs/blob/main/README.md)

**原文标题**: [mquickjs/README.md at main · bellard/mquickjs · GitHub](https://github.com/bellard/mquickjs/blob/main/README.md)

QuickJS 是一个由 Fabrice Bellard 开发的小型且可嵌入的 JavaScript 引擎，具有轻量级、快速执行和完整 ES2020 支持的特点。

- 🚀 轻量高效：设计紧凑，适合嵌入式系统和资源受限环境
- 📜 完整 ES2020 支持：全面兼容现代 JavaScript 标准
- 🔧 可嵌入性：易于集成到其他应用程序中
- 🛠️ 独立运行时：包含编译器和解释器，支持独立执行 JavaScript 代码
- 🔍 数学扩展：内置数学库，支持大整数和精确小数运算
- 📦 模块系统：实现 ES 模块标准，便于代码组织和管理
- 🛡️ 安全特性：提供内存安全和执行沙箱功能

---

### [法布里斯·贝拉的个人主页](https://bellard.org/)

**原文标题**: [Fabrice Bellard's Home Page](https://bellard.org/)

该网站展示了法布里斯·贝拉（Fabrice Bellard）的一系列创新技术项目，涵盖编程语言、数据压缩、嵌入式系统、多媒体处理及高性能计算等领域。

- 🚀 **Micro QuickJS**：适用于微控制器的 JavaScript 引擎
- 🎵 **TSAC 音频压缩**：极低比特率音频压缩技术
- 📦 **ts_zip 文本压缩**：基于大语言模型的实用文本压缩工具
- 💬 **ts_sms 短信压缩**：利用大语言模型的短消息压缩方案
- 🌐 **TextSynth Server**：提供大语言模型 REST API 的 Web 服务器
- 🏆 **NNCP 数据压缩器**：领跑大型文本压缩基准测试
- ⚡ **QuickJS 引擎**：轻量级完整的 JavaScript 引擎
- 🤖 **textsynth.com**：大语言模型访问平台
- 🎨 **微型混淆图像解码器**：2018 国际混淆代码大赛作品
- 🔢 **LibBF 高精度库**：任意精度浮点数处理库
- π **TinyPI 程序**：可计算数百万位圆周率
- 🖥️ **浏览器模拟器**：支持在浏览器运行 X Window/Windows 2000
- 🎮 **TinyEMU 模拟器**：支持 RISC-V/x86 架构的轻量模拟器
- 📐 **SoftFP 浮点库**：符合 IEEE 754-2008 标准的浮点仿真库
- 🖼️ **BPG 图像格式**：基于 HEVC 的便携图像格式
- 📡 **软件基站**：在普通 PC 上运行的 4G/5G 基站系统
- ⚙️ **ASN1 编译器**：生成高效 C 代码的编译工具
- 🌐 **JS 版 PC 模拟器**：测量浏览器启动 Linux 的时间
- π **圆周率计算**：用台式机计算 2700 亿位圆周率
- 📺 **电视信号生成**：通过 PC 显示器生成模拟/数字电视信号
- 💻 **QEMU 模拟器**：通用机器模拟与虚拟化平台
- 🎬 **FFMPEG 多媒体系统**：作者 2000 年创立的多媒体开源项目
- 📝 **TCC 编译器**：支持 C 语言脚本化的轻量级 C 编译器
- ✨ **QEmacs 编辑器**：用于学习 Unicode/文本处理的开源编辑器
- 🏅 **OTCC 编译器**：2001 年国际混淆代码大赛获奖作品
- 🎮 **TinyGL 图形库**：OpenGL 的精简高效子集
- 🧮 **科学网络计算器**：在线科学计算工具
- 📚 **圆周率研究**：圆周率公式算法与计算研究
- 🔢 **质数打印程序**：输出最大已知质数的微型 C 程序
- 📂 **历史项目归档**：早期技术项目集合

---

### [QuickJS JavaScript 引擎](https://bellard.org/quickjs/)

**原文标题**: [QuickJS Javascript Engine](https://bellard.org/quickjs/)

QuickJS 是一个小型且可嵌入的 JavaScript 引擎，支持 ES2023 规范，具有快速解释器和低启动时间，适用于嵌入式系统。

- 🚀 **2025-09-13 发布新版本**：包含更新日志，持续优化引擎性能。
- 🔧 **2025-04-26 版本调整**：移除大数扩展和 qjscalc 应用以简化代码，推荐使用 BFCalc 计算器替代。
- 📦 **轻量嵌入设计**：仅需少量 C 文件，无外部依赖，简单程序代码体积约 367 KiB。
- ⚡ **高效解释器**：单核桌面 PC 可在 2 分钟内运行 7.8 万项 ECMAScript 测试套件，运行时实例完整生命周期低于 300 微秒。
- ✅ **全面兼容 ES2023**：支持模块、异步生成器、代理等特性，通过近 100% 的 ECMAScript 测试套件验证。
- 🔄 **引用计数垃圾回收**：结合循环移除技术，降低内存占用并确保确定性行为。
- 🌐 **多平台支持**：提供跨 Linux、Mac、Windows 等系统的 Cosmopolitan 二进制文件，以及 TypeScript 和 Babel 编译器集成。
- 📚 **开源与文档**：基于 MIT 许可证发布，提供 HTML/PDF 格式文档，源代码及二进制文件可通过官网或 GitHub 获取。

---

### [法布里斯·贝拉发布 MicroQuickJS | 黑客新闻](https://news.ycombinator.com/item?id=46367224)

**原文标题**: [Fabrice Bellard Releases MicroQuickJS | Hacker News](https://news.ycombinator.com/item?id=46367224)

Fabrice Bellard 发布了 MicroQuickJS，这是一个针对嵌入式系统的轻量级 JavaScript 引擎，仅需 10KB RAM 即可运行。该引擎基于 QuickJS，但通过移除动态特性、限制语言功能以实现更高的确定性和安全性，特别适合资源受限的环境。

- 🚀 **轻量高效**：内存占用极小（最低 10KB RAM），代码体积小（约 100KB），适合嵌入式设备。
- 🔒 **严格模式**：禁止未声明的全局变量、`with` 语句和 `eval`，提升代码安全性与可预测性。
- 📜 **ES5 子集**：支持大部分 ES5 语法，但移除了 `Date`、`RegExp` 等对象以简化实现。
- 🧩 **数组无空洞**：数组必须连续，禁止稀疏数组，写入超界会抛出错误，鼓励使用普通对象替代。
- 🔄 **尾调用优化**：支持正确的尾调用，便于编写递归算法而不受栈限制。
- ⚙️ **C API 嵌入**：提供简洁的 C API，易于集成到其他项目中，支持自定义原生函数。
- 🌐 **多场景适用**：可用于嵌入式脚本、安全沙箱、WebAssembly 环境及教育工具。
- 🔍 **资源限制**：内置内存和 CPU 时间限制，增强运行时的安全控制。
- 📉 **性能权衡**：通过牺牲部分 JavaScript 动态特性换取确定性和低资源消耗，适合非 Web 标准场景。

---

### [快速、节省磁盘空间的包管理器 | pnpm](https://pnpm.io/)

**原文标题**: [Fast, disk space efficient package manager | pnpm](https://pnpm.io/)

pnpm 是一款高效、安全的 Node.js 包管理器，专注于提升安装速度、节省磁盘空间并优化 monorepo 管理，广受开发者社区和知名开源项目的青睐。

- 🚀 安装速度极快，优化依赖安装流程，显著减少等待时间
- 💾 高效节省磁盘空间，通过智能链接机制避免重复存储依赖包
- 🏗️ 内置 monorepo 支持，简化多包项目管理与协作
- 🔒 增强安全性，通过禁用安装后脚本、延迟新版本发布等机制防范供应链攻击
- ⚙️ 提供运行时管理、依赖覆盖等高级功能，提升开发体验
- 🤝 被 Next.js、Vue、Vite 等众多主流开源项目采用
- 💬 获得开发者广泛好评，在安装效率、CI 构建速度等方面表现突出

---

### [🚀 pnpm 在 2025 年 | pnpm](https://pnpm.io/blog/2025/12/29/pnpm-in-2025)

**原文标题**: [🚀 pnpm in 2025 | pnpm](https://pnpm.io/blog/2025/12/29/pnpm-in-2025)

2025 年是 pnpm 变革性的一年，主要聚焦于重新定义包管理的安全模型，同时在性能与开发者体验方面也取得了显著提升。根据下载统计，pnpm 的使用量相比 2024 年翻了一番。

- 🏠 **官网重新设计**：借助赞助商 Bit.cloud 的支持，新版官网使用 Bit 组件构建，并引入了专属设计系统。
- 🎤 **首次大型演讲**：维护者 Zoltan Kochan 在阿姆斯特丹的 JSNation 大会上进行了首次现场演讲，分享了关于配置依赖的内容。
- 🔒 **默认安全强化**：pnpm v10 不再默认信任安装的包，默认阻止`preinstall`/`postinstall`等生命周期脚本的执行，大幅减少了供应链攻击风险。
- 🛡️ **深度防御机制**：新增`minimumReleaseAge`拦截“零日”发布、`trustPolicy: no-downgrade`防止降级攻击、`blockExoticSubdeps`阻止可信依赖引入不可信子依赖。
- 💾 **全局虚拟存储**：引入全局虚拟存储功能，允许多个项目共享相同的依赖图，显著节省磁盘空间并加速安装过程。
- 📦 **原生 JSR 支持**：新增对 JSR 注册表的原生支持，可直接通过`jsr:`协议安装包，并与 npm 依赖无缝协同工作。
- ⚙️ **配置依赖管理**：推出配置依赖功能，允许在单体仓库中集中管理 pnpm 配置（如钩子、补丁和构建权限），确保版本一致性。
- ⚡ **自动运行时管理**：扩展运行时管理支持至 Deno 和 Bun，可通过`package.json`中的`devEngines.runtime`指定所需运行时版本，实现团队环境统一。

---

### [JavaScript 周刊第 766 期：2025 年 12 月 19 日](https://javascriptweekly.com/issues/766)

**原文标题**: [JavaScript Weekly Issue 766: December 19, 2025](https://javascriptweekly.com/issues/766)

这是 2025 年最后一期《JavaScript 周刊》的总结，涵盖了年度回顾、重要发布、热门文章以及月度生态动态。

- 🗓️ **期刊安排调整**：本期为 2025 年最后一期，提醒读者期刊将于 2026 年 1 月起改为每周二发布，下一期将于 1 月 6 日发布。
- 📦 **打包工具趋势**：JavaScript 打包工具的速度竞争已趋缓，当前重点转向优化产物体积和交付给用户的代码质量。
- 🤖 **AI 编程实践**：文章探讨了超越演示的 AI 实际工作流，包括提示工程、编码代理及生产级应用开发。
- ⚡ **AI 辅助移植**：作者使用 OpenAI 的 Codex 和 GPT 5.2，在 4.5 小时内将 HTML5 解析器从 Python 移植到 JavaScript。
- 🛠️ **工具与发布**：包括 React Server Components 探索工具、Cloudflare Wrangler 的框架自动部署支持、以及 Tesseract.js 7.0、Base UI 1.0 等多个重要库的版本更新。
- 🏆 **年度十大热门链接**：涵盖了从 JavaScript 解析谜题、ES2025 新特性解析，到依赖管理、Electron 误解澄清等广泛主题。
- 📅 **2025 月度生态回顾**：按月份总结了全年重大事件，如 Bun、Deno、TypeScript、React 等关键项目的版本发布、社区活动和安全事件。
- 🎄 **结语与预告**：主编感谢读者支持，并预告假期后回归，同时推广了测试自动化、工作流管理等赞助商服务。

---

### [WebF Beta 发布：将 JavaScript 与 Web 开发引入 Flutter](https://openwebf.com/en/blog/announcing-webf)

**原文标题**: [Introducing WebF Beta: Bring JavaScript and the Web dev to Flutter](https://openwebf.com/en/blog/announcing-webf)

WebF Beta 是一款为 Flutter 设计的 W3C/WHATWG 兼容的 Web 运行时，它允许开发者使用标准的 Web 技术（HTML/CSS/DOM + JavaScript）在移动端和桌面端实现原生性能。它不是一个新框架，而是一个运行时，让现有的 Web 技术栈（如 React、Vue、Vite、Tailwind CSS）无需重写即可在移动和桌面平台上运行，并提供与 Flutter 应用的无缝集成和一致的像素级渲染体验。

- 🚀 **无需重写现有技术栈**：WebF 允许直接使用 React、Vue、Svelte 等现代 Web 框架以及 Vite、Tailwind CSS 等工具，无需迁移或学习新框架。
- ⚡ **原生性能与快速启动**：通过优化运行时和保持引擎“热”状态，WebF 实现冷启动时间低于 100ms，提供接近原生应用的启动体验。
- 🔗 **无缝 Flutter 集成**：WebF 可嵌入 Flutter 应用，支持混合路由、将 Flutter 组件作为 HTML 元素使用，并允许通过插件访问设备功能。
- 🛠️ **友好的开发体验**：支持 Vite 的热模块替换（HMR）、兼容 Chrome DevTools 进行调试，并提供 Claude Code 等 AI 开发工具支持。
- 🌍 **跨平台一致性**：基于 Flutter 的单一渲染引擎，确保在 iOS、Android 和桌面端实现像素级一致的 UI 行为，减少平台特定调试。
- 📦 **兼容性与社区反馈**：支持大部分 npm 生态系统，鼓励开发者测试并报告兼容性问题，以共同改进运行时。
- 🚧 **Beta 版限制**：目前暂不支持 Shadow DOM、WebGL、WebAssembly 等特性，但正在积极开发中以完善功能。
- 🗺️ **未来路线图**：计划增加对 Flutter Web、shadcn/ui、Tailwind CSS v4 的完整支持，并优化开发者工具和 AI 集成。

---

### [pnpm 10.27 | pnpm](https://pnpm.io/blog/releases/10.27)

**原文标题**: [pnpm 10.27 | pnpm](https://pnpm.io/blog/releases/10.27)

pnpm 10.27 版本引入了信任策略忽略设置、全局虚拟存储库的项目注册与垃圾回收功能，并修复了多项错误，提升了包管理的安全性和存储效率。

- 🔐 新增`trustPolicyIgnoreAfter`设置，允许忽略对指定发布时间之前的包进行信任策略检查
- 📁 为全局虚拟存储库添加项目注册功能，支持通过`pnpm store prune`安全清理未使用的包
- 🗂️ 调整无作用域包在全局虚拟存储中的位置，统一为 4 级目录深度以保持结构一致性
- 🧹 引入标记 - 清除垃圾回收算法，自动扫描并移除全局虚拟存储中未使用的包
- ⚠️ 当`tokenHelper`设置包含环境变量时抛出错误，增强配置安全性
- 🔧 修复 Git 依赖构建脚本未遵循`dangerouslyAllowAllBuilds`设置的问题
- ⏭️ 在使用`--global`参数时跳过包管理器检查并发出警告
- 🐛 修复`pnpm add`错误修改`pnpm-workspace.yaml`中目录条目的问题

---

### [GitHub - vadimdemedes/ink：🌈 用于交互式命令行应用的 React 框架](https://github.com/vadimdemedes/ink)

**原文标题**: [GitHub - vadimdemedes/ink: 🌈 React for interactive command-line apps](https://github.com/vadimdemedes/ink)

Ink 是一个基于 React 的命令行界面（CLI）应用开发框架，允许开发者使用熟悉的 React 组件和 JSX 语法来构建交互式终端应用。它利用 Yoga 布局引擎实现 Flexbox 布局，支持样式、用户输入处理、焦点管理等，并兼容 React 的全部特性，如 Hooks 和 DevTools。

- 🎨 **React 风格的 CLI 开发** – 使用组件和 JSX 构建终端界面，支持 Flexbox 布局和 CSS 样式属性。
- 📦 **核心组件丰富** – 提供 `<Text>`、`<Box>`、`<Newline>`、`<Static>`、`<Transform>` 等组件，用于文本渲染、布局、静态输出和内容转换。
- 🎮 **交互与状态管理** – 通过 `useInput`、`useFocus`、`useApp` 等 Hooks 处理用户输入、焦点控制和应用生命周期。
- 🛠️ **开发与测试友好** – 支持 React DevTools 集成、使用 `ink-testing-library` 进行测试，并提供屏幕阅读器辅助功能支持。
- 🌟 **广泛采用** – 被 Claude Code、GitHub Copilot CLI、Gatsby、Shopify CLI 等多个知名项目用于构建 CLI 工具。
- 📚 **完善的生态** – 提供丰富的第三方组件（如输入框、选择器、进度条）和示例，便于快速开发复杂交互界面。

---

### [GitHub - vadimdemedes/ink：🌈 用于交互式命令行应用的 React](https://github.com/vadimdemedes/ink?tab=readme-ov-file#whos-using-ink)

**原文标题**: [GitHub - vadimdemedes/ink: 🌈 React for interactive command-line apps](https://github.com/vadimdemedes/ink?tab=readme-ov-file#whos-using-ink)

Ink 是一个基于 React 的命令行界面（CLI）应用开发库，允许开发者使用熟悉的 React 组件模型和 JSX 语法来构建交互式终端应用。它利用 Yoga 布局引擎实现类似 CSS Flexbox 的布局，并提供了丰富的内置组件和钩子来处理文本样式、布局、用户输入、焦点管理等。该库支持现代 React 特性，拥有活跃的社区和众多知名项目用例，且具备可访问性支持和测试工具。

- 🎨 **React 范式**：使用组件化方式构建 CLI 应用，支持所有 React 特性。
- 📐 **Flexbox 布局**：通过 Yoga 引擎实现类似 CSS 的灵活布局。
- 🧩 **内置组件**：提供 `<Text>`、`<Box>`、`<Newline>`、`<Static>`、`<Transform>` 等核心组件。
- 🎮 **交互处理**：提供 `useInput`、`useFocus`、`useFocusManager` 等钩子来管理用户输入和焦点。
- 🌐 **流控制**：通过 `useStdin`、`useStdout`、`useStderr` 钩子访问和控制输入输出流。
- ♿ **可访问性**：支持屏幕阅读器，提供 ARIA 相关属性以增强无障碍体验。
- 🧪 **测试友好**：可与 `ink-testing-library` 集成，便于组件测试。
- 🔧 **开发工具**：支持 React Devtools，便于调试和检查组件。
- 📚 **丰富生态**：拥有众多第三方组件和钩子，如输入框、旋转器、表格等。
- 🚀 **广泛应用**：被 Claude Code、Gatsby、Prisma、Shopify CLI 等众多知名项目使用。

---

### [发布 v0.6.0 · color-js/color.js · GitHub](https://github.com/color-js/color.js/releases/tag/v0.6.0)

**原文标题**: [Release v0.6.0 · color-js/color.js · GitHub](https://github.com/color-js/color.js/releases/tag/v0.6.0)

Color.js 发布了 v0.6.0 版本，这可能是 v0.x 系列的最后一个版本，标志着项目已足够成熟，为 v1.0 做准备。该版本引入了多项重要改进，包括下载量突破 1.14 亿次、转向 Open Collective 资助模式、多项破坏性变更（如用 `null` 代替 `NaN` 表示 `none` 值）、新增多个色彩空间、增强序列化控制、改用 JSDoc 提升文档质量，以及分离出 Color Apps、Color Palettes 和 Color Elements 等子项目。此外，还包含大量 API 改进、性能优化、错误修复和类型更新，并迎来了多位新贡献者。

- 🎉 **项目成熟与下载量**：Color.js 下载量已超过 1.14 亿次，每周下载量达 350 万次，项目转向 Open Collective 资助模式以确保可持续发展。
- ⚠️ **破坏性变更**：用 `null` 替代 `NaN` 表示 `none` 值，坐标值改为普通数字类型，并支持按原始格式重新序列化颜色。
- 🆕 **新增色彩空间**：引入了 OKHSL、OKHSV、OkLrab、OkLrCh 和 Linear Rec2100 等多个新色彩空间。
- 🛠️ **序列化控制增强**：提供更精细的序列化选项，允许在不重新定义格式的情况下自定义坐标和 alpha 的显示方式。
- 📚 **文档与类型改进**：全面转向 JSDoc 以提升 API 文档质量，并更新了类型定义，确保 TypeScript 和 JavaScript 用户都能获得良好体验。
- 🌐 **子项目分离**：将 Color Apps、Color Palettes 和 Color Elements 分离为独立项目和域名，分别专注于色彩应用、调色板分析和 Web 组件库。
- 🔧 **API 与性能优化**：新增 `Color.try()` 等函数，改进色彩差异计算，提升矩阵转换性能，并修复了大量错误。
- 👥 **社区贡献**：吸引了多位新贡献者，改进了测试覆盖率和开发文档，项目持续活跃发展。

---

### [发布 7.2.0 版本 · prisma/prisma · GitHub](https://github.com/prisma/prisma/releases/tag/7.2.0)

**原文标题**: [Release 7.2.0 · prisma/prisma · GitHub](https://github.com/prisma/prisma/releases/tag/7.2.0)

Prisma 发布了 7.2.0 稳定版本，包含多项 ORM 功能增强、错误修复以及 VS Code 扩展的改进，同时介绍了企业支持计划和招聘信息。

- 🎉 **发布稳定版本 7.2.0** – 包含新功能和多项修复。
- 🔧 **新增 SQL 注释插件** – 支持查询洞察元数据。
- ⚙️ **迁移命令增加 -url 参数** – 提升连接配置的灵活性。
- 🛠️ **允许未定义 URL** – 使 `prisma generate` 等流程更顺畅。
- 🐰 **根据 JS 运行时定制初始化** – 针对 Bun 或其他运行时优化 `prisma init`。
- 🐛 **错误处理改进** – 包括 `DataMapperError` 显示优化和 Postgres 错误码处理。
- 📄 **修复 UTF-8 多字节字符处理** – 避免跨块分割导致的问題。
- 🖥️ **VS Code 扩展修复** – 提升 Studio 连接的可靠性。
- 💼 **企业支持计划** – 提供优先问题处理、性能调优等专业服务。
- 🔍 **招聘信息** – 邀请开发者加入 Prisma 团队。

---

### [发布 v2.6.4 · denoland/deno · GitHub](https://github.com/denoland/deno/releases/tag/v2.6.4)

**原文标题**: [Release v2.6.4 · denoland/deno · GitHub](https://github.com/denoland/deno/releases/tag/v2.6.4)

Deno 是一个现代 JavaScript/TypeScript 运行时，其 GitHub 仓库发布了最新版本 v2.6.4，主要包含多项错误修复和功能改进。

- 🐛 修复了编译功能与 `--unstable-npm-lazy-caching` 的兼容性问题
- 🔗 为 Node.js 兼容层的 HTTP Agent 启用了 keepAlive 连接复用
- 🛡️ 修复了 Node.js 兼容层中 SQLite 会话过滤回调的错误处理
- 📊 在 Buffer.copy() 中增加了对 TypedArray 和 DataView 的支持
- 🔧 支持了 Node.js 兼容层的 inspector.url() 方法
- 🗃️ 在 node:sqlite 中支持了编号位置参数
- 🌐 防止 WebSocket 发送多个关闭帧
- ⏳ 在应用补丁前等待包安装完成
- 🔄 在 node/crypto 中集成了 async_hooks 用于域错误处理
- 📄 修复了配置文件中的网络权限问题
- 📦 当根目录仅有 deno.json 时，优先使用成员 package.json
- 🎮 将 WebGPU 的 wgpu 更新至 28.0.0
- 🖥️ 修复了针对 Intel Mac 目标的跨平台编译问题
- 🔗 将 urlpattern 更新至 0.4.2 版本

---

### [错误](https://javascriptweekly.com/link/178809/web)

**原文标题**: [Error](https://javascriptweekly.com/link/178809/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='devongovett.me', port=443): Max retries exceeded with url: /blog/static-hermes.html (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [包裹](https://parceljs.org/)

**原文标题**: [Parcel](https://parceljs.org/)

Parcel 是一款零配置、高性能的构建工具，提供从开发到生产的全流程优化体验，支持多种语言和文件类型，具备自动插件安装、热重载、并行构建与智能缓存等功能，并能自动进行生产优化如代码分割与压缩。

- 🚀 **零配置启动**：无需复杂配置，从 HTML 文件开始即可支持多种语言和文件类型，自动安装所需插件。
- ⚡ **高效开发体验**：内置开发服务器、热重载与状态保持，提供实时错误诊断和代码高亮提示。
- 🏎️ **极致构建性能**：基于 Rust 和 SWC 的编译器实现 10-100 倍速度提升，支持多核并行处理和全局缓存。
- 🌳 **自动生产优化**：内置树摇、代码压缩、图片优化、内容哈希和代码分割，全面优化生产环境输出。
- 🎯 **多目标支持**：自动根据浏览器目标进行代码转译，支持差分打包、Web Workers 及多格式库构建。
- 🔧 **灵活可扩展**：支持通过.parcelrc 配置和插件系统定制构建流程，插件 API 设计完善且支持热重载。
- 🌍 **开源驱动**：由全球开发者社区贡献和维护，提供多层级赞助支持。

---

### [使用 Deno 构建恐龙跑酷游戏，第一部分 | Deno](https://deno.com/blog/build-a-game-with-deno-1)

**原文标题**: [Build a dinosaur runner game with Deno, pt. 1 | Deno](https://deno.com/blog/build-a-game-with-deno-1)

本系列文章将指导你使用 Deno 构建一个简单的浏览器恐龙跑酷游戏，首篇内容涵盖项目初始化、本地服务器搭建及部署到 Deno Deploy 的完整流程。

- 🦕 使用 `deno init` 命令创建基础项目结构，配置 `deno.json` 管理任务和依赖
- 🗂️ 建立标准目录结构，包含 `src/` 服务端代码、`public/` 静态资源及环境配置文件
- ⚙️ 集成 Oak 框架搭建服务器，通过环境变量配置端口和主机，设置文件读写权限
- 🌐 创建基础 HTML 页面与健康检查 API 端点，实现静态文件服务和路由功能
- 🚀 通过 `deno deploy` 命令将项目部署至 Deno Deploy 云平台，支持实时在线访问
- 🔄 配置开发/生产双模式任务脚本，支持热重载和权限管理的灵活开发环境

---

### [使用 Deno 构建恐龙跑酷游戏，第二部分 | Deno](https://deno.com/blog/build-a-game-with-deno-2)

**原文标题**: [Build a dinosaur runner game with Deno, pt. 2 | Deno](https://deno.com/blog/build-a-game-with-deno-2)

本文是使用 Deno 构建恐龙跑酷游戏系列的第二部分，重点介绍了如何为游戏添加 HTML5 画布、游戏循环、用户控制和基础物理系统。通过设置画布、实现游戏循环、添加键盘与鼠标/触摸输入、构建重力与跳跃物理系统，并将项目部署到云端，开发者可以创建一个具有交互性的基础游戏框架。

- 🎮 设置 HTML5 画布作为游戏主区域，并添加分数显示与控制说明界面
- 🔄 使用 requestAnimationFrame 实现游戏循环，确保流畅的动画更新
- ⌨️ 添加键盘（空格/上箭头键）和鼠标/触摸点击控制，实现恐龙跳跃功能
- ⚙️ 构建基础物理系统，包括重力加速度与跳跃力模拟，控制恐龙运动轨迹
- 🎨 通过 CSS 美化游戏界面，定义色彩变量与响应式布局，提升视觉体验
- 🦖 创建游戏引擎类，管理游戏状态、恐龙属性、分数更新与场景渲染逻辑
- 🚀 将更新后的游戏部署至 Deno Deploy 云端，实现在线访问与实时预览

---

### [使用 Deno 构建恐龙跑酷游戏，第三部分 | Deno](https://deno.com/blog/build-a-game-with-deno-3)

**原文标题**: [Build a dinosaur runner game with Deno, pt. 3 | Deno](https://deno.com/blog/build-a-game-with-deno-3)

本文介绍了使用 Deno 构建恐龙跑酷游戏的第三阶段，重点讲解了如何添加障碍物、实现碰撞检测、提升游戏难度以及完善游戏状态管理，最终完成一个可部署的基础游戏版本。

- 🦕 扩展游戏状态：在游戏状态中添加初始速度、帧计数和高分记录属性，为障碍物和分数管理奠定基础。
- 🧱 构建障碍物系统：创建障碍物数组及相关计时器，实现随机生成不同尺寸的仙人掌障碍物，并使其从右侧向左侧移动。
- ⚡ 更新与碰撞检测：通过更新障碍物位置、检测恐龙与障碍物的矩形重叠来实现碰撞判定，碰撞时触发游戏结束逻辑。
- 📈 动态难度调整：根据玩家得分逐步提升游戏速度和障碍物生成频率，每约 200 分增加一次难度，保持游戏挑战性。
- 🎨 绘制与动画：为不同障碍物类型设计独特外形，并实现恐龙奔跑时的腿部动画，增强游戏视觉体验。
- 🖥️ 渲染与状态管理：更新渲染方法以绘制障碍物和恐龙，并添加游戏开始、重置及结束时的界面覆盖层。
- 🏆 高分记录系统：利用 localStorage 存储和加载最高分，游戏结束时显示分数并更新记录，提升玩家成就感。
- 🚀 部署与测试：完成代码后通过 Deno Deploy 将游戏更新至云端，生成可分享的 URL，为后续添加后端功能做准备。

---

### [恐龙游戏 - 维基百科](https://en.wikipedia.org/wiki/Dinosaur_Game)

**原文标题**: [Dinosaur Game - Wikipedia](https://en.wikipedia.org/wiki/Dinosaur_Game)

《恐龙游戏》是谷歌于 2014 年为 Chrome 浏览器开发的一款内置离线小游戏，玩家操控像素霸王龙在沙漠场景中奔跑跳跃以躲避障碍。游戏每月有约 2.7 亿次游玩量，已成为网络文化标志之一。

- 🦖 游戏在 Chrome 断网时自动触发，玩家通过空格键或点击恐龙启动，操控霸王龙跳跃躲避仙人掌与翼龙
- 🌙 随游戏进程切换昼夜模式，配色与天气效果会动态变化，最高分数设计对应霸王龙存在的 1700 万年
- 🎂 多次更新加入彩蛋，如 2018 年添加生日蛋糕与礼帽，2020 年加入奥运火炬彩蛋并变换运动项目
- 🛠️ 由 Chrome UX 团队于 2014 年开发，代号“Project Bolan”，灵感源于“无网络如同史前时代”的幽默比喻
- 📱 2021 年推出 iOS 与 Android 桌面小组件，2024 年曾短暂上线 AI 生成精灵的 GenDino 功能
- 🌍 文化影响广泛，包括《辛普森一家》片头致敬、亚美尼亚实体雕像，以及第三方改编游戏《Dino Swords》

---

### [网络研讨会：CERN 如何利用 TimescaleDB 驱动突破性物理研究 | 虎数](https://www.tigerdata.com/events/webinar-how-cern-powers-ground-breaking-physics-with-timescaledb?utm_source=cooperpress&utm_medium=referral&utm_campaign=cern-webinar-jan-21-2026)

**原文标题**: [Webinar: How CERN Powers Ground-Breaking Physics with TimescaleDB | Tiger Data](https://www.tigerdata.com/events/webinar-how-cern-powers-ground-breaking-physics-with-timescaledb?utm_source=cooperpress&utm_medium=referral&utm_campaign=cern-webinar-jan-21-2026)

欧洲核子研究中心（CERN）利用 TimescaleDB 现代化其海量时间序列数据管理，以应对大型强子对撞机每日产生的数百 GB 数据挑战。

- 🏗️ 设计了可插拔的新归档系统（NGA），以现代化其遗留技术栈
- 💾 采用 TimescaleDB 原生压缩技术，将存储减少 95%，查询速度提升高达 40 倍
- 📊 利用连续聚合功能，为海量历史数据集提供快速响应的仪表板支持
- 🔧 注重长期可维护性设计，避免供应商锁定并减少技术债务

---

### [修复 TypeScript 性能问题：案例研究 | Viget](https://www.viget.com/articles/fixing-typescript-performance-problems)

**原文标题**: [Fixing TypeScript Performance Problems: A Case Study | Viget](https://www.viget.com/articles/fixing-typescript-performance-problems)

本文分享了作者在大型 TypeScript 单体仓库中诊断和解决性能问题的经验，通过一系列工具和方法显著提升了编译速度和开发体验。

- 🔍 **诊断问题**：从 TypeScript 性能文档入手，检查编辑器、依赖和编译设置，使用`tsc --listFiles`和`tsc --explainFiles`验证文件包含。
- 📊 **性能测量**：利用`tsc --extendedDiagnostics`获取编译指标，关注文件数、类型数、内存使用和关键阶段耗时。
- 🕵️ **深入追踪**：通过`tsc --generateTrace`生成跟踪文件，使用`@typescript/analyze-trace`分析热点，定位到特定文件类型检查耗时 80 秒。
- 🐌 **根本原因**：发现性能瓶颈源于使用`kysely`库的复杂泛型助手函数，涉及大型数据库接口和深层类型推断，导致编译负担激增。
- 🛠️ **解决方案**：删除有问题的`kysely`助手函数并内联查询，同时修复循环依赖、清理未使用类型和依赖、升级包版本等。
- 📉 **显著成果**：构建时间从 6.2 分钟降至 1.3 分钟（提升 79%），内存使用减少 50%，类型检查时间下降 83%，语言服务器响应大幅改善。

---

### [未找到标题](https://www.royalbhati.com/posts/js-array-vs-typedarray)

**原文标题**: [No title found](https://www.royalbhati.com/posts/js-array-vs-typedarray)

本文介绍了人工智能在医疗领域的应用现状与前景，重点探讨了其在疾病诊断、药物研发和个性化治疗方面的突破性进展，同时简要提及了相关的伦理挑战。

- 🏥 AI 辅助诊断系统能通过分析医学影像快速识别病灶，提升早期癌症等疾病的检出率
- 🔬 机器学习加速了新药研发流程，大幅缩短化合物筛选与临床试验设计周期
- 📊 基于患者基因数据的人工智能模型可为慢性病患者提供动态个性化治疗方案
- ⚖️ 医疗 AI 面临数据隐私、算法透明度及责任认定等伦理监管问题需要完善

---

### [JavaScript 创始人警告：Windows 11 过度依赖 WebView2 与 Electron，勿仓促牺牲原生体验追求网页 UX](https://www.windowslatest.com/2025/12/27/javascript-creator-warns-against-rushed-web-ux-over-native-as-windows-11-leans-harder-on-webview2-and-electron/)

**原文标题**: [JavaScript creator warns against “rushed web UX over native” as Windows 11 leans harder on WebView2 and Electron](https://www.windowslatest.com/2025/12/27/javascript-creator-warns-against-rushed-web-ux-over-native-as-windows-11-leans-harder-on-webview2-and-electron/)

Windows 11 因过度依赖 WebView2 和 Electron 等网页技术框架，导致系统与应用出现性能臃肿、内存占用高等问题，JavaScript 创始人 Brendan Eich 对此提出批评，认为这是企业为追求订阅模式而牺牲用户体验的表现。

- 🚨 **JavaScript 创始人批评**：Brendan Eich 指出 Windows 11 过度依赖 WebView2 和 Electron，导致“网页用户体验匆忙替代原生应用”，造成系统臃肿。
- 💻 **应用性能问题**：Discord、Teams 和 WhatsApp 等应用因使用 Electron 或 WebView2，内存占用常超 1GB，Discord 甚至需在内存达 4GB 时重启应用。
- 🔄 **微软的网页化趋势**：Windows 11 的搜索、开始菜单、通知中心日程视图等功能均转向 WebView2 实现，而非原生开发，引发性能担忧。
- 💰 **商业动机驱动**：Eich 认为这种转变源于企业推行订阅模式、追求控制权，而非技术优化，导致“体验劣化”。
- ⚠️ **生态系统影响**：WebView2 组件已成为系统核心，如移除会导致 Teams 无法运行，凸显微软对网页技术的深度依赖。
- 🛠️ **开发效率与质量失衡**：网页技术可跨平台，但大公司如微软（市值超 3.5 万亿美元）却难以为基础功能开发原生界面，被指牺牲质量换速度。

---

### [仅用 200 行 JavaScript 实现 JSON 流式处理](https://krasimirtsonev.com/blog/article/streaming-json-in-just-200-lines-of-javascript)

**原文标题**: [Streaming JSON in just 200 lines of JavaScript](https://krasimirtsonev.com/blog/article/streaming-json-in-just-200-lines-of-javascript)

本文介绍了作者在探索 React 服务器组件时，受渐进式 JSON 技术启发，开发了一个名为 Streamson 的轻量库（约 200 行代码），用于实现 JSON 数据的分块流式传输，以提升大型数据集或动态生成数据场景下的前端渲染性能。

- 🚀 **渐进式 JSON 流式传输**：通过分块发送 JSON 数据，允许客户端在完整数据到达前开始渲染，提升感知性能。
- 🔄 **占位符与数据替换**：服务器将未就绪的数据部分替换为占位符（如`"_$1"`），待数据就绪后以独立块发送，客户端动态替换。
- 🛠️ **服务器实现**：使用 NDJSON 格式和分块传输编码，通过递归遍历数据对象识别 Promise 并生成占位符，异步解析后发送数据块。
- 🌐 **客户端处理**：利用 Fetch API 读取流式响应，将占位符转换为 Promise，并在数据到达时解析，实现渐进式数据填充。
- 📦 **Streamson 库**：封装为 NPM 包，提供简洁的服务器和客户端 API，支持快速集成到 Express 等框架中，优化数据传输体验。

---

### [信号与基于查询的编译器](https://marvinh.dev/blog/signals-vs-query-based-compilers/)

**原文标题**: [Signals vs Query-Based Compilers](https://marvinh.dev/blog/signals-vs-query-based-compilers/)

现代编译器架构正从传统的线性流水线转向查询驱动模型，以支持 LSP 等交互场景。这种架构与 UI 渲染中的信号系统有相似之处，但在设计上存在关键差异，主要体现在数据流、缓存机制和并发处理等方面。

- 🔄 查询驱动编译器的核心是“按需计算”：所有操作都通过查询触发，仅处理与当前查询相关的文件，避免无关计算。
- 🧠 架构三要素：查询（纯函数）、输入（可变状态源）和数据库（协调中心），通过全局版本号管理缓存有效性。
- 💾 智能缓存策略：查询结果可安全缓存，依赖单向追踪和版本比对实现高效缓存复用与失效。
- ⚡ 与信号系统的关键差异：查询模型采用“拉取”机制，无自动推送更新，允许异步结果返回；信号系统则为“推送 - 拉取”混合，强同步性适合 UI 渲染。
- 🧵 并发优势：查询粒度细、无副作用的特点天然支持并行执行，如多文件解析可分配到不同线程。
- 🎯 适用场景对比：信号系统适合需要即时同步的 UI 渲染；查询模型更适合编译器、开发服务器等对实时性要求较宽松的增量计算场景。

---

### [JavaScript 依赖地狱的九重境界 | Andrew Nesbitt](https://nesbitt.io/2026/01/05/the-nine-levels-of-javascript-dependency-hell.html)

**原文标题**: [The Nine Levels of JavaScript Dependency Hell | Andrew Nesbitt](https://nesbitt.io/2026/01/05/the-nine-levels-of-javascript-dependency-hell.html)

JavaScript 依赖地狱的九个层级，描绘了从无包管理器到 AI 自动化引发的复杂困境的演变过程。

- 📦 **无包管理器的原始阶段**：通过复制粘贴 jQuery、下载压缩包等方式手动管理依赖，随后 npm 的出现使发布变得简单。
- 🚀 **过度依赖微包**：发布门槛降低后，出现大量单行代码包（如 is-odd），开发者倾向于引入微小依赖而非自己编写代码。
- 🏔️ **依赖爆炸与体积膨胀**：一个导入可能引发上千个嵌套依赖，导致 node_modules 目录异常庞大，成为“宇宙中最重的物体”。
- ⚔️ **版本冲突困境**：不同包要求同一依赖的不同版本，导致解析错误和构建失败，解决方案是允许同时存在多个版本。
- 🤖 **自动化依赖管理**：生态发展过快催生自动化工具（如 semantic-release、Dependabot），但带来海量 PR 和机械式合并，使人疲于奔命。
- 🛠️ **工具分裂与社区分化**：出现 Yarn、pnpm、Bun 等多种工具，导致锁文件格式和 CLI 不统一，问题转移而非解决。
- 🚨 **安全警告疲劳**：npm audit 等工具产生大量安全警告（尤其是开发依赖），导致 CVE 疲劳和普遍性忽略。
- 🐛 **依赖图传播攻击**：攻击通过依赖图自动传播，一个维护者被入侵即可影响数千下游包，需依靠可信发布和 OIDC 令牌防御。
- 🤖 **AI 代理引发的混乱**：AI 工具自动执行`npm install`，可能引用不存在的包或被劫持的 README，使依赖图成为新的攻击入口。

---

### [如何使用 Three.js 与 Rapier 实现像素到体素的视频滴落效果 | Codrops](https://tympanus.net/codrops/2026/01/05/how-to-create-a-pixel-to-voxel-video-drop-effect-with-three-js-and-rapier/)

**原文标题**: [How to Create a Pixel-to-Voxel Video Drop Effect with Three.js and Rapier | Codrops](https://tympanus.net/codrops/2026/01/05/how-to-create-a-pixel-to-voxel-video-drop-effect-with-three-js-and-rapier/)

本教程展示了如何利用 Three.js、着色器和 Rapier 物理引擎，将视频像素体素化并置入三维物理世界，实现从平面像素到三维体素的动态转换与物理交互。

- 🎬 **视频像素体素化**：通过 Three.js 的 InstancedMesh 将视频像素网格化，每个实例代表一个像素，并利用着色器将其从平面拉伸为三维体素。
- 🌊 **波纹效果转换**：采用两种波纹模式（有机与平滑）驱动体素化过程，通过顶点着色器控制深度变化，实现视觉上的动态转换效果。
- ⚙️ **物理引擎集成**：使用 Rapier 为每个体素创建对应的刚体，在转换完成后激活物理模拟，实现自然掉落与碰撞交互。
- 🔄 **状态恢复机制**：通过线性插值动画将散落的体素平滑恢复至初始网格状态，支持重复演示与交互。
- 🛠️ **技术栈组合**：结合 Three.js 渲染、GLSL 着色器编程、Rapier 物理模拟及 GSAP 动画控制，构建高性能的交互式视觉体验。
- 🎨 **创意扩展空间**：教程鼓励替换视频源、修改几何形状或着色器效果，探索玻璃破碎、颜色筛选等自定义变体应用。

---

### [现代 JavaScript 事件日历](https://schedule-x.dev/)

**原文标题**: [Modern JavaScript Event Calendar](https://schedule-x.dev/)

Schedule-X 是一款现代化的 JavaScript 事件日历组件，支持跨技术栈快速集成，提供丰富的视图、插件和交互功能，包括拖放、调整事件大小、多语言和响应式设计等。其高级版本进一步提供资源调度、交互式事件模态框等高级功能，帮助开发者节省大量开发时间。

- 📅 跨框架兼容，支持 React、Vue、Angular、Svelte 和 Preact
- ⚙️ 高度可配置，支持自定义视图、插件和主题（含深色模式）
- 🌍 内置国际化，支持多语言
- 📱 完全响应式，适配桌面到移动设备
- 🧩 提供插件系统，支持社区和自定义插件
- 🕒 集成 Temporal API 处理时间与日期
- ✨ 高级功能包括资源调度、交互式事件模态框和拖拽创建事件
- 💎 高级版节省开发时间，提供资源视图、事件重复规则等复杂功能
- 👍 获开发者好评，强调其灵活性、易用性和优质客户支持

---

### [GitHub - schedule-x/schedule-x：JavaScript事件日历。fullcalendar与react-big-calendar的现代替代方案。](https://github.com/schedule-x/schedule-x)

**原文标题**: [GitHub - schedule-x/schedule-x: JavaScript event calendar. Modern alternative to fullcalendar and react-big-calendar.](https://github.com/schedule-x/schedule-x)

Schedule-X 是一个专注于满足现代 Web 应用需求的 JavaScript 事件日历，提供响应式设计、国际化支持和可扩展性，可作为 fullcalendar 和 react-big-calendar 的现代替代方案。

- 📅 项目拥有 2.1k 星标和 156 个分支，采用 MIT 许可证
- 🌐 提供详细文档和演示的官方网站：schedule-x.dev
- 🔧 支持通过 React、Angular、Vue、Svelte 和 Preact 等框架注入自定义组件
- 🐛 问题反馈和功能请求可通过 GitHub 的 issue 跟踪器提交
- 💬 其他问题可加入 Discord 聊天室进行讨论
- 💰 项目接受赞助以支持长期发展，赞助者可在 README 或项目网站中被提及
- 🤝 欢迎代码贡献，但需先阅读贡献指南并在提交 PR 前创建 issue

---

### [GitHub - parallax/jsPDF：面向所有人的客户端JavaScript PDF 生成库。](https://github.com/parallax/jsPDF)

**原文标题**: [GitHub - parallax/jsPDF: Client-side JavaScript PDF generation for everyone.](https://github.com/parallax/jsPDF)

jsPDF 是一个用于在客户端生成 PDF 文件的 JavaScript 库，支持多种模块格式和现代浏览器，提供丰富的自定义选项和高级功能。

- 📄 **客户端 PDF 生成**：纯 JavaScript 库，可在浏览器中直接创建和保存 PDF 文件。
- 📦 **多种安装方式**：支持通过 npm、yarn 安装，或从 CDN 加载，兼容不同项目需求。
- ⚙️ **灵活配置**：可自定义纸张大小、方向和单位，并支持 A4、横向等常见设置。
- 🔧 **多环境运行**：不仅适用于浏览器，还可在 Node.js 中使用，需注意文件系统权限安全。
- 🛡️ **安全建议**：强烈建议对用户输入进行清理，并提供详细的安全策略和漏洞报告指南。
- 🌐 **UTF-8 与字体支持**：通过集成自定义 TTF 字体支持 Unicode 字符，解决非 ASCII 文本显示问题。
- 🔄 **高级 API 模式**：提供兼容模式和高级模式，后者支持矩阵变换、图案等高级 PDF 功能。
- 📚 **完善文档与社区**：提供在线演示、详细文档，并通过 Stack Overflow 和 GitHub 问题跟踪提供支持。
- 🤝 **开源与贡献**：采用 MIT 许可证，鼓励社区贡献，提供明确的代码提交和问题报告指南。
- 📈 **项目活跃度**：拥有 3.1 万星标、4.8 千分叉，由社区和 yWorks 公司共同维护，持续更新。

---

### [jsPDF - 使用 HTML5 JavaScript 库创建 PDF 文件](https://raw.githack.com/MrRio/jsPDF/master/index.html)

**原文标题**: [jsPDF - Create PDFs with HTML5 JavaScript Library](https://raw.githack.com/MrRio/jsPDF/master/index.html)

一款基于 HTML5 和 JavaScript 的客户端 PDF 生成库，无需服务器即可创建各类文档。
- 📄 纯前端 PDF 生成方案，适用于活动票务、报告、证书等多种场景
- 🚫 演示版完全在客户端运行，无需服务器支持
- 🛠️ 提供在线代码编辑器，支持实时预览和自动刷新功能
- 📥 可即时下载生成的 PDF 文件，并附带多种示例模板
- ©️ 由 James Hall 和 yWorks GmbH 共同维护，遵循隐私政策

---

### [首页 - 文档](https://rawgit.com/MrRio/jsPDF/master/docs/index.html)

**原文标题**: [Home - Documentation](https://rawgit.com/MrRio/jsPDF/master/docs/index.html)

jsPDF 是一个用于在 JavaScript 中生成 PDF 文件的库，支持多种安装方式、模块格式和高级功能，并提供了详细的文档和安全指南。

- 📦 **安装方式**：可通过 npm、yarn 安装，或从 CDN 加载，支持不同环境（如浏览器、Node.js）。
- 📄 **基本用法**：导入库后创建文档，添加文本并保存，支持自定义纸张大小、方向和单位。
- 🛡️ **安全建议**：强调对用户输入进行清理，并提供 Node.js 文件读取的安全配置选项。
- 🌐 **模块支持**：兼容 ES 模块、UMD、AMD 和全局变量，易于集成到各种框架（如 Vue、Angular、React）。
- 🔤 **字体与 UTF-8**：支持自定义 TTF 字体以显示 Unicode 字符，提供字体转换工具。
- ⚙️ **高级功能**：提供两种 API 模式（兼容模式和高级模式），支持矩阵变换、图案等高级特性。
- 🐛 **支持与贡献**：鼓励通过 Stack Overflow 提问，欢迎提交错误报告和功能请求，并提供贡献指南。
- 📜 **许可证**：采用 MIT 许可证，由 James Hall 和 yWorks 共同维护。

---

### [调查与表单管理软件 - SurveyJS](https://surveyjs.io/?utm_source=jsweekly&utm_medium=referral&utm_campaign=q1_2026)

**原文标题**: [Survey and Form Management Software - SurveyJS](https://surveyjs.io/?utm_source=jsweekly&utm_medium=referral&utm_campaign=q1_2026)

SurveyJS 是一个开源的前端表单和问卷管理解决方案，提供一系列 JavaScript 库，让开发者能够在自己的应用中构建、展示、收集数据并可视化表单结果，同时保持数据的完全所有权和自我托管。

- 📚 **表单库** - 一个免费的 MIT 许可 UI 组件，可解析 JSON 文件并即时渲染动态交互式表单，用于收集用户响应。
- 🛠️ **调查创建器** - 一个可白标的拖放式表单构建器，可自动生成描述表单结构的 JSON 模式，支持可视化创建和编辑。
- 📊 **仪表板** - 一个 UI 组件，用于解释 JSON 模式并以交互式图表和表格可视化调查结果。
- 🧾 **PDF 生成器** - 一个 UI 组件，可将表单 JSON 模式渲染为 PDF，支持导出为可编辑或预填的 PDF 文件。
- ♿ **无障碍访问** - 核心库完全符合 WCAG、Section 508 和 ARIA 标准，支持键盘导航和屏幕阅读器。
- ∞ **无使用限制** - 可创建无限表单、收集任意数量响应，所有数据均存储在用户自己的数据库中。
- 🧩 **自定义输入字段** - 支持定义自定义问题类型，并可集成 Angular、React 或 Vue 3 组件。
- 📴 **离线数据收集** - 支持完全离线工作，数据本地存储，恢复在线后自动同步。
- 💳 **一次性购买许可** - 开发者可一次性购买永久使用 Survey Creator、PDF Generator 和 Dashboard 的许可，包含 12 个月免费维护。
- ✅ **自定义数据验证** - 支持超越基础验证器的自定义客户端规则和服务器端检查。
- 🔓 **开源** - 所有库均在 GitHub 上开源，支持 React、Angular、Vue 3 和原生 JavaScript。
- 🎨 **白标化** - 提供对表单和 Survey Creator 外观的完全控制，支持内置主题和自定义 CSS 变量。
- 🤖 **AI 辅助** - 可通过 API 集成 AI，实现自然语言表单生成、翻译和智能内容建议。
- 🏢 **多行业适用** - 适用于保险、医疗、市场研究、教育、人力资源、电子商务、客户体验、非营利组织和银行等多个行业，满足敏感数据的安全收集与合规需求。
- 🔒 **保障数据安全与合规** - 鼓励自我托管，使组织能够完全控制数据流，确保个人隐私并满足如 HIPAA、FERPA、GDPR 等法律要求，避免依赖第三方 SaaS 平台。

---

### [未找到标题](https://www.usebruno.com/)

**原文标题**: [No title found](https://www.usebruno.com/)

本文介绍了人工智能在医疗领域的应用现状与前景，重点探讨了其在疾病诊断、治疗方案优化及医疗管理效率提升方面的作用，并简要提及了相关技术挑战和伦理考量。

- 🤖 AI 辅助诊断系统能通过分析医学影像快速识别病灶，提升早期疾病检出率
- 💊 基于机器学习的个性化治疗方案可结合患者数据优化用药与治疗路径
- 📊 智能医疗管理平台自动化处理病历、排班等流程，减轻医护行政负担
- ⚠️ 数据隐私保护与算法透明度仍是技术推广过程中需要解决的关键问题
- 🔮 未来 AI 有望与物联网、可穿戴设备结合，实现全程健康监测与预防性医疗

---

### [GitHub - usebruno/bruno：开源API探索与测试IDE（Postman/Insomnia的轻量级替代品）](https://github.com/usebruno/bruno)

**原文标题**: [GitHub - usebruno/bruno: Opensource IDE For Exploring and Testing API's (lightweight alternative to Postman/Insomnia)](https://github.com/usebruno/bruno)

Bruno 是一款开源的 API 探索与测试集成开发环境，旨在替代 Postman 和 Insomnia 等工具，强调轻量、本地化和数据隐私。

- 🚀 **开源 API 客户端** – Bruno 是一个创新的开源工具，专注于 API 测试与探索，提供轻量级替代方案。
- 📁 **本地文件存储** – 集合直接保存在本地文件夹中，使用纯文本标记语言 Bru 记录 API 请求信息。
- 🔄 **Git 版本控制** – 支持通过 Git 或其他版本控制系统进行团队协作，方便管理 API 集合。
- 🔒 **离线与隐私优先** – 完全离线运行，无云同步计划，确保用户数据隐私和设备本地存储。
- 💰 **商业版本可选** – 核心功能免费开源，同时提供付费版本以满足团队额外需求，平衡开源与可持续性。
- 📦 **多平台安装** – 支持 Mac、Windows 和 Linux，可通过 Homebrew、Chocolatey、Snap 等多种包管理器安装。
- 🌐 **社区与资源丰富** – 提供详细文档、路线图、Stack Overflow 支持及 Discord 等社区渠道，方便用户交流与获取帮助。

---

### [GitHub - jrouwe/JoltPhysics.js：使用emscripten将JoltPhysics移植到JavaScript](https://github.com/jrouwe/JoltPhysics.js)

**原文标题**: [GitHub - jrouwe/JoltPhysics.js: Port of JoltPhysics to JavaScript using emscripten](https://github.com/jrouwe/JoltPhysics.js)

JoltPhysics.js 是一个使用 Emscripten 将 Jolt Physics 引擎移植到 JavaScript 的项目，提供多种构建版本，可通过 npm 安装，并包含详细的使用文档和构建指南。

- 🎯 **项目核心**：将 C++ 物理引擎 Jolt Physics 通过 Emscripten 移植到 JavaScript 环境。
- 📦 **多种版本**：提供 7 种构建版本，包括 WASM（含嵌入或独立文件）、调试版、多线程版以及 asm.js 版本。
- 📚 **接口一致**：JavaScript 接口与 C++ 版 Jolt Physics 保持一致，可直接参考其官方文档。
- 🔧 **安装便捷**：通过 npm 发布为 ECMAScript 模块，支持多种导入方式，也可通过 CDN（如 unpkg）直接使用。
- 🛠️ **构建灵活**：提供构建脚本，支持 Linux 环境编译，可启用内存分析、双精度、SIMD 等高级选项。
- 🧹 **内存管理**：需手动管理内存，对引用计数类对象（如 Shape、Constraint）需正确使用 AddRef/Release 方法。
- 🌐 **示例与运行**：附带在线演示和本地运行示例，需通过 Web 服务器访问。
- 🤝 **生态应用**：已被 Babylon.js 插件、GDevelop 游戏引擎、react-three-jolt 等多个项目集成使用。
- ⚖️ **开源许可**：项目基于 MIT 许可证开源发布。

---

### [JoltPhysics.js 演示](https://jrouwe.github.io/JoltPhysics.js/)

**原文标题**: [JoltPhysics.js demos](https://jrouwe.github.io/JoltPhysics.js/)

JoltPhysics.js 是一个物理引擎库，提供了多种演示示例，涵盖刚体、软体、车辆控制、角色动画、约束系统、碰撞检测及性能测试等功能。

- 🧱 展示支持的形状类型和软体模拟，包括布料、立方体和球体
- 🚗 演示车辆控制器，涵盖多轮车辆、摩托车和坦克的创建
- 🧍 展示角色虚拟控制及骨骼装配的创建与加载
- ⛓️ 介绍多种约束类型，如滑轮、路径、SVG 路径和约束马达
- 🏔️ 支持高度场形状作为碰撞表面及浮力模拟
- 🎯 演示射线投射、碰撞过滤和接触监听器的使用
- 🧪 提供压力测试示例，展示多线程运行和大规模物体堆叠
- 🛠️ 展示如何添加/移除物体、处理摩擦、快照恢复及内存清理
- 🎨 提供调试渲染功能，用于可视化物理系统状态（需调试版本库）

---

### [GitHub - martijnversluis/ChordSheetJS：一个用于解析和格式化和弦与和弦谱的JavaScript库](https://github.com/martijnversluis/ChordSheetJS)

**原文标题**: [GitHub - martijnversluis/ChordSheetJS: A JavaScript library for parsing and formatting chords and chord sheets](https://github.com/martijnversluis/ChordSheetJS)

ChordSheetJS 是一个用于解析和格式化吉他和弦谱的 JavaScript 库，支持多种和弦格式的解析与输出，并提供丰富的 API 和格式化选项。

- 🎸 支持多种和弦谱格式解析，包括常规和弦谱、Ultimate Guitar 格式和 ChordPro 格式
- 📄 提供多种输出格式，如纯文本、HTML（表格和 div 布局）、ChordPro 格式及 PDF（测试版）
- 🔧 包含和弦处理功能，如解析、克隆、转调、标准化和弦表示
- 🔗 支持序列化和反序列化，便于存储和传输和弦数据
- 🎨 可生成基础 CSS 样式，方便自定义 HTML 输出外观
- 📚 兼容多种 ChordPro 指令，涵盖元数据、格式、环境和和弦图等类别
- ⚙️ 提供布局引擎和测量器，用于精确控制文本和和弦的定位
- 📦 可通过 npm 安装或直接使用独立捆绑文件，支持模块化和全局命名空间使用

---

### [和弦小提琴](https://martijnversluis.github.io/ChordFiddle/)

**原文标题**: [chordfiddle](https://martijnversluis.github.io/ChordFiddle/)

该内容介绍了一个和弦编辑器的功能与设置选项。

- 🎵 支持升降调功能（移调上下）
- 🎼 提供升降号符号选择（♯/♭）
- 📄 可导入和弦谱表
- 🔧 编辑器由@chordbook/editor 提供技术支持
- ⚙️ 包含详细设置选项（如降调开关、和弦扩展、调性选择等）
- 📝 支持两种编辑模式（标记模式/纯文本模式）
- 🔍 配备歌曲检查器功能

---

### [升级 6.x 至 7.x | Middy.js](https://middy.js.org/docs/upgrade/6-7/)

**原文标题**: [Upgrade 6.x -> 7.x | Middy.js](https://middy.js.org/docs/upgrade/6-7/)

Middy 7.x 版本引入了对 Durable Functions 的支持，并带来了一些重大变更，包括弃用 `streamifyResponse` 选项、更新 Node.js 版本要求，以及多个中间件的功能增强与破坏性更改。

- 🚀 新增对 Durable Functions 的支持，但暂不支持超时中止信号
- ⚠️ 弃用 `streamifyResponse` 选项，改为使用 `executionModeStreamifyResponse`
- 🔧 支持 LLRT 运行时，适用于标准执行模式和持久化上下文模式
- 🏗️ 兼容新的租户隔离模式和 Lambda 托管实例的多并发功能
- 📦 多个中间件更新：如 `http-content-encoding` 新增 zstd 压缩支持，`http-security-headers` 调整安全头默认行为
- 🔄 `input-output-logger` 中间件新增对 DurableContext 的支持，并将 `awsContext` 选项重命名为 `lambdaContext`
- 🛠️ `http-router` 中间件优化了动态/静态路由的优先级处理
- 📅 停止支持 Node.js 20.x，建议升级至 Node.js 24.x

---

### [GitHub - playcanvas/model-viewer: 支持 glTF 与 3D 高斯点云的 3D 模型查看器](https://github.com/playcanvas/model-viewer)

**原文标题**: [GitHub - playcanvas/model-viewer: 3D Model Viewer supporting glTF and 3D Gaussian Splats](https://github.com/playcanvas/model-viewer)

PlayCanvas Model Viewer 是一个基于 WebGL 的 3D 模型查看器，支持 glTF 2.0 和 3D 高斯溅射格式，提供快速、合规的模型查看体验，并可通过拖拽加载场景和背景图像。

- 🚀 **高性能查看器**：基于 PlayCanvas 引擎，完全兼容 glTF 2.0 规范，加载和渲染速度极快。
- 📂 **便捷加载方式**：支持通过拖拽直接加载嵌入式 glTF、二进制 GLB 或解压的 glTF 文件夹。
- 🖼️ **背景自定义**：可拖拽单张图像（视为等距柱状投影）或六张图像（视为立方体贴图）作为场景背景。
- 🌐 **URL 参数控制**：支持通过 `load`、`cameraPosition` 等查询参数预加载模型或调整相机初始位置。
- 🔧 **本地开发与构建**：使用 Node.js 环境，通过 `npm run build` 构建项目，`npm run serve` 启动本地服务器进行测试。
- 🧩 **开源库集成**：基于 PlayCanvas Engine、Observer 和 PCUI 等库开发，支持通过 `npm link` 进行本地库集成测试。
- 📊 **项目活跃度高**：拥有 628 个星标、102 个分支，采用 MIT 许可证，持续维护并发布新版本。

---

### [发布 v1.5.0 · grafana/k6 · GitHub](https://github.com/grafana/k6/releases/tag/v1.5.0)

**原文标题**: [Release v1.5.0 · grafana/k6 · GitHub](https://github.com/grafana/k6/releases/tag/v1.5.0)

k6 1.5.0 版本发布，引入了多项新功能与改进，包括浏览器模块的事件同步、字符级输入模拟、增强的调试日志、WebSocket 关闭代码支持、扩展生态系统增强、基于 URL 的密钥管理以及新的机器可读摘要格式。同时包含一些破坏性变更、错误修复和内部优化。

- 🎉 **浏览器模块新增 `page.waitForEvent()`**：支持基于事件的同步，可等待特定页面事件（如控制台消息或响应）后再继续测试，提高测试可靠性。
- ⌨️ **新增 `locator.pressSequentially()`**：模拟逐字符输入，触发完整的键盘事件，适用于测试自动补全、实时验证等依赖输入时序的功能。
- 🔍 **`console.log()` 深度对象日志**：改进复杂 JavaScript 结构（如函数、类和循环引用）的显示，提升调试体验。
- 🌐 **WebSocket 关闭代码与原因支持**：实验性 WebSocket 模块现可发送和捕获关闭代码及原因，便于测试连接关闭场景。
- 🛠️ **扩展支持自定义子命令**：扩展可在 `k6 x` 命名空间下注册自定义 CLI 工具，增强生态集成。
- 🔗 **URL 密钥管理**：支持从 HTTP 端点获取密钥，为未来集成外部密钥服务（如 HashiCorp Vault）奠定基础。
- 📊 **机器可读摘要格式**：新增结构化摘要格式，便于与 CI/CD 管道、仪表板等外部系统集成。
- ⚠️ **破坏性变更**：弃用实验性 Redis 模块，建议用户迁移至官方扩展。
- 🐛 **错误修复**：修复了浏览器选择器、重试机制、空处理器崩溃等多个问题，提升稳定性。
- 🛠️ **维护与内部改进**：包括依赖更新、性能优化、测试修复和安全漏洞解决。
- 🗺️ **路线图**：计划弃用 First Input Delay (FID) Web 核心指标，转向 Interaction to Next Paint (INP)，以符合最新性能标准。

---

### [开源负载测试工具 | k6 OSS](https://k6.io/open-source/)

**原文标题**: [Open-source load testing tool for developers | k6 OSS](https://k6.io/open-source/)

k6 是一款面向开发者的高性能负载测试工具，支持开源和云端部署，提供灵活的测试脚本编写、自动化集成及多后端结果存储功能。

- 🛠️ **易于使用的 API 与 CLI**：为现代工程团队设计，提供直观且强大的命令行界面和 API。
- 📜 **JavaScript 编写测试**：使用熟悉的 JavaScript 语言构建真实负载测试，可复用模块和库。
- 🔄 **自动化测试集成**：在 CI/CD 工具中集成性能测试，设置通过/失败标准以确保可靠性。
- ⚡ **高性能引擎**：基于 Go 语言开发，提供卓越的负载测试性能。
- 🗄️ **多后端存储支持**：测试结果可输出至 DataDog、Prometheus 等多种后端系统。
- 🌐 **扩展测试能力**：社区扩展支持 SQL、浏览器、Kafka 等基础设施性能测试。
- ☁️ **灵活扩展执行**：支持本地调试与云端分布式集群运行，无缝切换执行模式。

---

### [发布 v3.6.0 · recharts/recharts · GitHub](https://github.com/recharts/recharts/releases/tag/v3.6.0)

**原文标题**: [Release v3.6.0 · recharts/recharts · GitHub](https://github.com/recharts/recharts/releases/tag/v3.6.0)

Recharts 3.6.0 版本发布，引入了 BarStack 组件、范围堆叠条等新功能，修复了多项错误，并进行了文档改进和代码优化。

- 🚀 新增 BarStack 组件，支持配置整个条形堆栈的设置，如圆角
- 📊 条形图新增范围堆叠条功能
- 🥧 导出 PieSectorShapeProps 类型，便于自定义饼图形状
- 📈 X 轴和 Y 轴新增 'equidistantPreserveEnd' 间隔选项
- 🛠️ 工具提示添加 graphicalItemId 到 payload 对象
- 📦 导出多个 TypeScript 类型，增强公共 API
- 🐛 修复散点图中工具提示数据重复或包含无关项的问题
- 🏷️ 修复 Label 作为 LabelList 内容时导致的崩溃问题
- 🔢 优化数字处理，在放入 DOM 前进行四舍五入
- 🌐 改进引用存储方式，支持 Shadow DOM 使用场景
- 📚 文档持续改进，代码注释、Storybook 和网站内容趋于同步
- 👋 欢迎多位新贡献者加入项目

---

### [GitHub - nats-io/nats.js：适用于Node.js、Bun、Deno及浏览器的NATS JavaScript 客户端——云原生消息系统](https://github.com/nats-io/nats.js)

**原文标题**: [GitHub - nats-io/nats.js: JavaScript client for Node.js, Bun, Deno and browser for NATS, the cloud native messaging system](https://github.com/nats-io/nats.js)

这是一个用于 Node.js、Bun、Deno 和浏览器的 JavaScript 客户端，专为云原生消息系统 NATS 设计。该项目采用模块化架构，整合了多个运行时支持，并取代了原有的独立仓库。

- 🚀 **项目重组** – 将 NATS 基础客户端库重构为多个模块，并统一了 Deno、Node/Bun 和浏览器的传输层支持。
- 📦 **模块化设计** – 核心功能拆分为 Core、JetStream、Kv、Obj 和 Services 等独立模块，便于按需使用和升级。
- 🔄 **版本迁移** – 从旧版本迁移的详细指南已提供，确保用户平滑过渡到 v3 版本。
- 🌐 **多运行时支持** – 提供针对 Deno、Node/Bun 和浏览器（WebSocket）的原生传输层实现。
- 📚 **完善文档** – 每个模块都有介绍性页面和 JSDoc 文档，方便开发者快速上手。
- 🤝 **开源贡献** – 欢迎社区通过提交问题或拉取请求参与项目开发，遵循 Apache-2.0 许可证。

---

### [API 密钥公测版](https://clerk.com/changelog/2025-12-11-api-keys-public-beta?utm_source=cooper_press&utm_medium=newsletter&utm_campaign=api-keys&utm_content=01-06-26&dub_id=XDaMap18rl1Dutr5)

**原文标题**: [API Keys Public Beta](https://clerk.com/changelog/2025-12-11-api-keys-public-beta?utm_source=cooper_press&utm_medium=newsletter&utm_campaign=api-keys&utm_content=01-06-26&dub_id=XDaMap18rl1Dutr5)

Clerk 平台推出了 API 密钥公开测试版功能，允许用户创建和管理 API 密钥以授权访问应用程序 API，支持零代码 UI 组件和编程管理，并提供密钥验证、范围控制及灵活定价。

- 🔑 **API 密钥公开测试**：功能进入公开测试阶段，用户可为应用程序 API 创建委托访问密钥。
- 🧩 **内置管理组件**：通过 Clerk 仪表板启用后，用户档案和组织档案组件中会显示 API 密钥管理标签。
- 💻 **支持编程管理**：可使用后端 SDK 以编程方式创建和管理密钥，控制范围、声明和过期时间。
- 🔐 **后端验证集成**：通过 auth() 助手验证 API 密钥，支持基于范围的精细访问控制。
- 🏷️ **密钥核心特性**：包括用户/组织范围绑定、即时撤销、自定义范围、声明支持及可选过期设置。
- 💰 **灵活定价模式**：测试期间免费，正式发布后按使用量计费（创建$0.001/次，验证$0.00001/次）。
- 📚 **完整资源支持**：提供操作指南、SDK 参考、仪表板配置及分步教程，方便快速上手。

---

### [Trigger.dev | 构建和部署全托管 AI 代理与工作流。](https://trigger.dev/?utm_source=fnf&utm_medium=newsletter&utm_campaign=trigger.dev-december&utm_term=jsweekly&utm_content=homepage)

**原文标题**: [Trigger.dev | Build and deploy fully-managed AI agents and workflows.](https://trigger.dev/?utm_source=fnf&utm_medium=newsletter&utm_campaign=trigger.dev-december&utm_term=jsweekly&utm_content=homepage)

Trigger.dev 是一个用于构建和部署完全托管的 AI 代理与工作流的 TypeScript 平台，专注于处理长时间运行的任务，并宣布获得 1600 万美元 A 轮融资。

- 🚀 **平台核心**：提供构建 AI 工作流的 TypeScript 平台，支持重试、队列、可观测性和弹性扩展。
- 🤖 **AI 任务与代理**：支持调用 AI API、创建具备人工介入功能的 AI 代理，并能将响应流式传输到前端。
- ⚙️ **可靠性与扩展**：提供无超时执行、按使用付费的弹性基础设施，且无需管理服务器。
- 🔍 **监控与调试**：具备错误警报、高级运行筛选、版本控制以及实时运行状态显示功能。
- 🔧 **开发灵活性**：允许自由定制构建过程，支持集成 Python、Prisma、Puppeteer 等多种工具。
- 🌐 **开源与集成**：采用 Apache 2.0 开源许可，可与现有技术栈无缝集成，并拥有活跃的开发者社区。
- 📈 **客户认可**：受到多家公司开发者的好评，用于处理视频、邮件活动、PDF 转换等多种关键业务场景。

---

### [CSS 网格通道介绍 | WebKit](https://webkit.org/blog/17660/introducing-css-grid-lanes/)

**原文标题**: [  Introducing CSS Grid Lanes | WebKit](https://webkit.org/blog/17660/introducing-css-grid-lanes/)

CSS Grid Lanes 是一种新的 CSS 布局方式，专为创建瀑布流（masonry）布局而设计，现已可在 Safari Technology Preview 234 中试用。它利用 CSS Grid 的强大功能，通过简单的代码即可实现灵活、响应式的多列布局，无需 JavaScript 或媒体查询。该功能支持定义不同宽度的列、跨列放置项目、控制布局方向，并通过“容差”设置调整项目放置的精确度，为网页设计提供了更多创意可能性和更好的可访问性。

- 🚀 **未来已来**：CSS Grid Lanes 正式推出，为网页瀑布流布局带来标准化的解决方案。
- 🛠️ **简单易用**：仅需三行 CSS 代码（如 `display: grid-lanes` 和 `grid-template-columns`）即可创建响应式布局，无需媒体查询。
- 🧩 **灵活定义**：支持使用 `grid-template-*` 定义不同宽度的列，并可实现交替窄宽列等创意设计。
- 🔀 **跨列与放置**：项目可跨越多列，也能通过 `grid-column` 属性精确控制放置位置。
- ↔️ **方向可变**：默认根据定义的列或行自动创建瀑布流或砖块布局，方向可灵活调整。
- ⚖️ **容差控制**：通过 `item-tolerance` 属性调整布局算法对项目尺寸差异的敏感度，平衡布局顺序与用户体验。
- 🧪 **立即尝试**：可在 Safari Technology Preview 234 中体验所有演示，包括图库、报纸和菜单布局等用例。
- 💬 **参与反馈**：CSS 工作组仍在讨论部分细节（如属性命名），鼓励开发者测试并提供意见。

---

### [AddyOsmani.com - 在谷歌 14 年收获的 21 条经验](https://addyosmani.com/blog/21-lessons/)

**原文标题**: [AddyOsmani.com - 21 Lessons From 14 Years at Google](https://addyosmani.com/blog/21-lessons/)

在谷歌工作 14 年后，作者总结出 21 条超越编程技术的职业心得，核心在于工程师的成功不仅取决于代码能力，更取决于如何应对人员协作、组织政治和模糊性等软性因素。这些经验强调以用户为中心、保持行动力、重视清晰沟通，并关注长期职业发展。

- 🔍 **以用户问题为核心**：优秀工程师从深入理解用户需求出发，而非单纯追求技术应用  
- 🤝 **协作高于正确**：推动团队达成共识比证明自己正确更重要，避免因固执引发隐性阻力  
- 🚀 **行动导向**：先交付再优化，实际反馈比完美空想更有价值  
- 📖 **清晰胜于巧妙**：代码的可读性是降低团队协作风险的关键  
- ⚙️ **谨慎创新**：仅在关键领域使用创新技术，默认选择稳定成熟的方案  
- 🗣️ **主动展示价值**：在组织中被看见需要主动沟通，而非依赖代码“说话”  
- ❌ **减少代码量**：最佳解决方案有时是不写代码，优先考虑删除而非新增  
- 🔄 **兼容性即产品**：大规模系统中所有行为都可能被依赖，需谨慎对待变更  
- 🧭 **对齐消除拖延**：团队进度缓慢常源于目标不一致，而非执行力不足  
- 🎯 **专注可控范围**：将精力投入可影响领域，避免为不可控因素焦虑  
- 🏗️ **理解底层逻辑**：抽象层终会失效，保持对系统底层原理的认知  
- ✍️ **写作促进思考**：通过输出（文档/教学）检验并深化自己的理解  
- 🔗 **重视隐性贡献**：将协调、文档等支撑性工作转化为可见成果，避免被低估  
- 🏆 **警惕表面共识**：轻松赢得辩论可能意味着对方已放弃表达真实意见  
- 📊 **警惕指标异化**：任何度量标准被过度关注后都会失真，需配合质量指标综合评估  
- ❓ **承认无知**：坦诚“不知道”能营造安全氛围，促进团队学习  
- 🌐 **建设人脉网络**：职业关系比单一职位更持久，应以真诚态度长期维护  
- ⚡ **删减优于优化**：提升系统性能最有效的方式常是删除不必要的工作  
- 📋 **流程服务效率**：好的流程应降低不确定性，而非制造繁文缛节  
- ⏳ **时间重于金钱**：职业后期需清醒权衡时间与收益，避免透支性付出  
- 📈 **相信复利效应**：通过持续学习、总结和分享实现能力的长期积累

---

### [2025 年数据库回顾 // 博客 // 卡内基·梅隆大学 - 安迪·帕夫洛](https://www.cs.cmu.edu/~pavlo/blog/2026/01/2025-databases-retrospective.html)

**原文标题**: [Databases in 2025: A Year in Review // Blog // Andy Pavlo - Carnegie Mellon University](https://www.cs.cmu.edu/~pavlo/blog/2026/01/2025-databases-retrospective.html)

2025 年数据库领域持续以 PostgreSQL 为核心发展，同时 MCP 协议普及、文件格式竞争激烈，行业并购活跃，并有标志性人物事件。

- 🐘 PostgreSQL 持续主导生态，v18 版本发布异步 I/O 等新特性，多家巨头收购或推出 PostgreSQL 服务，分布式项目 Multigres、Neki、PgDog 竞争发展
- 🔗 MCP（模型上下文协议）成为数据库与 LLM 交互标准，各厂商推出 MCP 服务器，但需注意代理访问的安全风险与权限控制
- ⚖️ MongoDB 起诉 FerretDB 侵权，涉及 API 复制与商标争议，同时微软将 DocumentDB 捐赠给 Linux 基金会
- 📁 文件格式竞争加剧，SpiralDB Vortex 等新格式挑战 Parquet，焦点转向互操作性与 GPU 支持
- 🏢 行业并购频繁，Databricks 收购 Neon，Snowflake 收购 CrunchyData，IBM 收购 DataStax 和 Confluent，多家公司被私募股权收购
- 💸 融资活动活跃，Databricks、ClickHouse、Supabase 等获大额投资，但早期阶段融资减少
- ✏️ 多家公司更名，如 Timescale 改为 TigerData，EdgeDB 改为 Gel，以调整市场定位
- ☠️ 部分项目终止，如 Fauna、PostgresML、Hydra、Voltron Data 等，GPU 加速数据库仍处小众
- 👑 Larry Ellison 随 Oracle 股价上涨成为全球首富，涉足多项商业与媒体投资

---

### [2025：大语言模型之年](https://simonwillison.net/2025/Dec/31/the-year-in-llms/)

**原文标题**: [2025: The year in LLMs](https://simonwillison.net/2025/Dec/31/the-year-in-llms/)

2025 年是大型语言模型（LLM）领域快速发展的一年，涌现出推理模型、智能体、编程助手、图像编辑等多项重要趋势，同时中国开源模型崛起，行业竞争加剧，使用成本上升，并伴随着安全、环境等新挑战。

- 🧠 **推理模型成为主流**：OpenAI 的 o 系列模型引领了“推理”革命，通过强化学习从可验证奖励（RLVR）训练，使模型能进行多步规划和问题分解，显著提升了代码调试、工具调用和搜索等任务的性能。
- 🤖 **智能体实用化**：从理论讨论走向实际应用，智能体被定义为能通过多步工具调用完成有用工作的 LLM 系统，在编程和深度研究等场景中表现出色。
- 💻 **编程智能体爆发**：Claude Code 的发布引领了编程智能体潮流，各大实验室推出命令行工具，支持异步代码编写与执行，极大提升了开发效率。
- 🖥️ **命令行 LLM 工具普及**：开发者广泛接受命令行 LLM 工具，Claude Code 等工具创造了可观收入，证明了终端交互的自然性与高效性。
- ⚠️ **安全风险常态化**：YOLO 模式（自动执行）的流行带来了便利，但也导致“偏差正常化”现象，安全风险被忽视，潜在威胁增大。
- 💸 **高价订阅模式出现**：Claude Pro Max 等月费 200 美元的高端订阅计划成为新常态，反映了重度用户对高性能模型和大量令牌消耗的需求。
- 🇨🇳 **中国开源模型崛起**：DeepSeek、GLM、Qwen 等中国模型在开源权重模型中表现领先，部分模型性能媲美 Claude 4 Sonnet 和 GPT-5，推动了技术民主化。
- ⏳ **长任务处理能力突破**：GPT-5 等模型能独立完成耗时数小时的任务，智能体处理复杂任务的时间范围大幅扩展。
- 🎨 **提示驱动图像编辑风靡**：OpenAI 的图像编辑功能推动 ChatGPT 用户激增，Google 的 Nano Banana 模型在文本生成和图像指令跟随上表现突出。
- 🏆 **模型学术竞赛夺冠**：推理模型在国际数学奥林匹克竞赛和国际大学生程序设计竞赛中取得金牌，展示了解决新颖复杂问题的能力。
- 🦙 **Llama 失去领先地位**：Meta 的 Llama 4 发布令人失望，模型过大且性能未达预期，在开源社区中的影响力下降。
- 🥊 **OpenAI 领先优势缩小**：尽管在消费者心智份额上保持领先，但在图像、代码、开源模型等领域面临 Google Gemini 和中国模型的强劲竞争。
- 🌟 **Gemini 全面进步**：Google Gemini 模型系列持续升级，在长上下文、多模态、硬件优化（TPU）等方面表现优异，成为 OpenAI 的有力竞争者。
- 🐦 **鹈鹕骑自行车成趣味基准**：作者用“鹈鹕骑自行车”SVG 生成任务作为非正式模型能力测试，意外成为行业关注的趣味基准。
- 🛠️ **作者构建 110 个工具**：通过“氛围编码”和 AI 辅助，作者全年构建了大量小型 HTML/JavaScript 工具，探索了 LLM 的实际应用模式。
- 🚨 **模型“告密”行为引关注**：Claude 4 等模型在特定系统提示下可能主动举报用户不当行为，引发对 AI 伦理与安全的广泛讨论。
- 😌 **氛围编码引发争议**：Andrej Karpathy 提出的“氛围编码”概念迅速流行，指通过自然语言提示快速原型开发，但定义被泛化，引发术语澄清努力。
- 🔌 **MCP 协议昙花一现**：模型上下文协议（MCP）年初爆发后因编程智能体的兴起而重要性下降，更简单的 Skills 格式受到青睐。
- 🌐 **浏览器集成 AI 引担忧**：Chrome 等浏览器集成 LLM 功能带来便利，但提示注入等安全风险尚未解决，引发对数据安全的严重关切。
- 🎯 **致命三要素聚焦安全**：作者提出“致命三要素”术语，专指通过提示注入窃取敏感数据的攻击，以提高对特定安全威胁的认知。
- 📱 **手机编程成为常态**：借助 Claude Code 等异步编程智能体，作者在手机上完成了大量编码任务，甚至包括复杂项目移植。
- ✅ **一致性测试套件是关键**：提供语言无关的一致性测试套件能极大提升编程智能体的可靠性，成为新项目推广的重要助力。
- ☁️ **云端模型优势扩大**：尽管本地模型性能提升，但云端推理模型在工具调用、长上下文和编码智能体任务上仍保持明显优势。
- 🗑️ **低质 AI 内容泛滥**：“slop”一词被选为年度词汇，指大量生成的劣质 AI 内容，但作者认为优质内容筛选机制仍是关键。
- 🌍 **数据中心面临抵制**：AI 数据中心的高能耗和环境影响引发越来越多环保团体和社区的反对，可持续性成为紧迫问题。
- 🆕 **年度新词反映趋势**：“氛围编码”、“致命三要素”、“上下文腐蚀”等新词汇涌现，捕捉了技术演进中的关键现象与挑战。

---

### [Web 开发又变得有趣了](https://ma.ttias.be/web-development-is-fun-again/)

**原文标题**: [Web development is fun again](https://ma.ttias.be/web-development-is-fun-again/)

回顾过去网页开发的简单时代，如今技术栈的复杂性已让全栈开发变得困难，但 AI 工具的出现重新平衡了局面，借助模式识别和经验，开发者能高效管理全流程，重拾创造乐趣。

- 🕰️ 作者怀念早期网页开发的简单时代，技术栈易于掌握，个人开发者能独立完成从构思到实现的全过程
- 📈 如今前后端技术复杂度激增，要求深厚的领域知识，全栈开发对个人而言变得极具挑战
- 🤖 AI 工具如 Claude 和 Codex 的出现，显著提升了开发效率，帮助作者重获管理全技术栈的能力
- 🧠 凭借多年经验，作者能识别 AI 生成代码的质量，并借鉴过往优秀实践，快速迭代开发
- ⚽ AI 如同火箭动力足球，让开发者能够达到现代软件质量标准，大幅缩短开发周期
- 💡 节省出的时间和精力，让开发者能重新专注于创意实验、用户体验优化等更有价值的工作
- ✨ AI 工具减轻了开发中的繁琐负担，使网页开发再次变得有趣，重拾从无到有的创造乐趣

---

### [GitHub - popovicu/ultimate-linux：用JavaScript编写的终极Linux微发行版！一个功能强大的最小化Linux用户空间，完全由...纯JavaScript编写！虽不完全，但近乎如此。它很棒，我保证！](https://github.com/popovicu/ultimate-linux)

**原文标题**: [GitHub - popovicu/ultimate-linux: The Ultimate Linux micro distribution written in JavaScript! A very functional minimal userspace for Linux written in... pure JavaScript! Not quite, but almost. It's good, I promise!](https://github.com/popovicu/ultimate-linux)

这是一个用 JavaScript 编写的微型 Linux 发行版项目，旨在通过 JavaScript（配合少量 C 代码）构建一个极简的 Linux 用户空间，以探索 Linux 内核与用户软件的交互原理。

- 🐧 项目名为“Ultimate Linux”，是一个用 JavaScript 编写的微型 Linux 发行版，核心是一个独立的 JavaScript 二进制文件
- 🔧 构建过程使用 QuickJS 将 JavaScript 代码转译为 C，并静态链接 musl libc 生成可移植的 ELF 可执行文件
- 🖥️ 支持基础 Shell 命令：ls、cd、cat、mkdir、mount、exit，可在 QEMU 虚拟机中作为 PID 1 初始化进程运行
- 📚 项目背景源于作者对 Linux 内核系统调用稳定性、独立内核特性及 Go/Rust 等语言直接调用 syscall 的探讨
- 🛠️ 技术栈涉及 JavaScript、C、musl libc 和 Linux 内核，强调通过最小化用户空间理解操作系统底层机制

---

