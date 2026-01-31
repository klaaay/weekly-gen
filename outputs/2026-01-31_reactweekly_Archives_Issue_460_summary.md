### [React 状态周报 第 460 期：2026 年 1 月 30 日](https://react.statuscode.com/issues/460)

**原文标题**: [React Status Issue 460: January 30, 2026](https://react.statuscode.com/issues/460)

本期 React Status 通讯聚焦于 React 生态系统的技术更新、安全修复及工具发布，涵盖 GitHub Copilot CLI 的动画实现、React 安全补丁、框架发展趋势及多个新库的推出。

- 🚀 GitHub 团队详解了 Copilot CLI 中动画 ASCII 横幅的工程实现，并开源了相关工具 ASCII Motion
- 🔒 React 发布 19.2.4 等版本，修复服务器组件中存在的多个拒绝服务漏洞
- 📈 SolidJS 创始人分析 2026 年 JavaScript 框架发展趋势，指出当前为"极其激动人心的时期"
- ⚡ 开发者分享使用 React 编译器后性能得到"昼夜分明"的提升体验
- 🛠️ 多个新工具发布：包括头像生成组件 Facehash、3D 按钮库 React Tilt Button 和高效撤销库 Travels 1.0
- 🤖 Vercel 研究发现 AGENTS.md 文件在评估中优于技能触发，Clerk 推出 AI 助手连接服务
- 📦 生态更新：Bun 性能提升 35%、Yarn 6 预览版发布、StyleX 推出新网站和在线编辑器

---

### [从像素到字符：GitHub Copilot CLI 动态 ASCII 横幅背后的工程揭秘 - GitHub 博客](https://github.blog/engineering/from-pixels-to-characters-the-engineering-behind-github-copilot-clis-animated-ascii-banner/)

**原文标题**: [From pixels to characters: The engineering behind GitHub Copilot CLI’s animated ASCII banner - The GitHub Blog](https://github.blog/engineering/from-pixels-to-characters-the-engineering-behind-github-copilot-clis-animated-ascii-banner/)

GitHub Copilot CLI 团队为命令行工具设计了一个 3 秒的 ASCII 艺术动画横幅，这看似简单的任务背后涉及了复杂的终端工程挑战。由于终端环境缺乏统一的渲染标准和动画框架，且需兼顾不同终端的兼容性、颜色显示差异以及无障碍访问需求，团队最终编写了超过 6000 行 TypeScript 代码来实现这一功能。项目由设计师与工程师紧密合作，开发了自定义的动画编辑工具，并采用语义化颜色角色映射来确保动画在各种终端和主题下都能优雅降级。该动画默认为关闭状态，以优先保障无障碍访问体验，其架构设计也为未来的终端动画提供了可扩展的解决方案。

- 🎨 **终端动画的复杂性**：在终端中实现 ASCII 动画面临无画布、无标准动画框架、渲染模型碎片化等独特挑战，需手动处理帧重绘和光标控制。
- 🖥️ **颜色与兼容性工程**：ANSI 颜色代码在不同终端和主题下表现不一致，团队采用 4 位调色板和语义化颜色角色映射，确保品牌色彩在各类环境中可识别且兼容无障碍设置。
- ♿ **无障碍优先设计**：动画默认为关闭状态，支持屏幕阅读器模式自动跳过，避免快速变化的字符造成干扰，并尊重用户的全局颜色覆盖和对比度设置。
- 🛠️ **自定义工具链开发**：由于缺乏现成的 ASCII 动画设计工具，设计师使用 GitHub Copilot 辅助构建了一个原型动画编辑器，实现了帧序列编辑和 ANSI 颜色预览功能。
- ⚙️ **工程化与架构**：动画最终以纯文本帧存储，通过主题映射和运行时着色实现，代码量超 6000 行，主要处理终端差异、渲染逻辑和无障碍需求，而非视觉效果本身。
- 🔄 **协作与开源影响**：项目促进了设计师与工程师的紧密合作，并将原型工具开源为“ASCII Motion”应用，吸引了社区贡献，体现了在终端领域构建工具的必要性。

---

### [GitHub Copilot CLI · GitHub](https://github.com/features/copilot/cli)

**原文标题**: [GitHub Copilot CLI · GitHub](https://github.com/features/copilot/cli)

GitHub Copilot CLI 是一款集成在终端中的 AI 助手，旨在帮助开发者通过自然语言交互更高效地编写、运行和管理代码。它作为 GitHub Copilot 付费订阅的一部分提供，支持多种开发任务，如代码探索、依赖安装、文件编辑和调试，同时强调安全性与用户控制，需显式批准所有修改和命令执行。

- 🚀 **快速上手**：通过 npm 安装并认证即可使用，无需额外费用，支持 macOS、Linux 和 Windows（通过 WSL）。
- 💼 **订阅集成**：包含在 Copilot Pro、Pro+、Business 和 Enterprise 计划中，使用现有订阅额度，简化设置与成本。
- 🤖 **智能代理**：基于 GitHub 原生上下文（如仓库、问题和拉取请求）执行编码任务，支持自主任务处理。
- 🔧 **灵活扩展**：可通过 Model Context Protocol (MCP) 服务器集成自定义工具，适配个性化开发环境。
- 🛡️ **安全可控**：自动继承组织治理策略，所有文件修改和命令执行需用户显式批准，确保透明与安全。
- 🔄 **会话持久**：支持跨会话的聊天历史记录，保持上下文连续性，提升协作效率。
- 📚 **广泛适用**：适用于遗留代码导航、跨平台开发设置和多步骤实现等场景，独立于代码编辑器运行。
- 🚧 **预览状态**：目前处于公开预览阶段，部分功能（如子代理、VS Code 直接集成）已在未来路线图中规划。

---

### [GitHub - vadimdemedes/ink：🌈 用于交互式命令行应用的 React](https://github.com/vadimdemedes/ink)

**原文标题**: [GitHub - vadimdemedes/ink: 🌈 React for interactive command-line apps](https://github.com/vadimdemedes/ink)

Ink 是一个基于 React 的命令行界面（CLI）渲染库，允许开发者使用熟悉的 React 组件模型构建交互式命令行应用程序。它利用 Flexbox 布局引擎在终端中创建灵活的 UI，并支持样式、用户输入处理、焦点管理等丰富功能。

- 🎨 **React 风格的 CLI 开发** – 使用 React 组件和 JSX 语法构建命令行界面，支持 Hooks、状态管理等所有 React 特性。
- 📦 **Flexbox 布局支持** – 通过 Yoga 引擎实现类似 CSS 的 Flexbox 布局，支持盒模型、边距、对齐等属性。
- 🖋️ **丰富的内置组件** – 提供 `<Text>`（文本样式）、`<Box>`（布局容器）、`<Newline>`（换行）、`<Static>`（静态输出）等核心组件。
- ⌨️ **用户输入处理** – 通过 `useInput` Hook 监听键盘输入，支持箭头键、回车、Ctrl+C 等常用快捷键。
- 🎯 **焦点管理** – 使用 `useFocus` 和 `useFocusManager` 实现组件间的焦点切换，适合构建复杂的交互式 CLI。
- 🧪 **测试友好** – 提供 `ink-testing-library` 支持，便于对 CLI 输出进行单元测试。
- 🔧 **开发者工具集成** – 支持 React Devtools，可在开发时实时检查和调试组件树。
- ♿ **屏幕阅读器辅助** – 提供 ARIA 属性支持，增强 CLI 应用的无障碍访问能力。
- 📚 **活跃的生态系统** – 被许多知名项目（如 Gatsby、Cloudflare Wrangler、Shopify CLI 等）使用，并有丰富的第三方组件和示例。

---

### [ASCII 动态](https://ascii-motion.app/)

**原文标题**: [ASCII Motion](https://ascii-motion.app/)

本文介绍了 ASCII 动态加载动画的视觉呈现过程，通过简单的字符序列变化模拟动态效果。

- 🌀 使用 ASCII 字符模拟动态加载的视觉效果
- ⏳ 通过字符变化展现进度与等待状态
- 🖥️ 适用于命令行界面等纯文本环境
- 🔄 动态序列由字符轮替形成动画错觉

---

### [GitHub - CameronFoxly/Ascii-Motion：一款用于创建和动画化ASCII艺术的现代Web应用](https://github.com/cameronfoxly/Ascii-Motion)

**原文标题**: [GitHub - CameronFoxly/Ascii-Motion: A modern web application for creating and animating ASCII art](https://github.com/cameronfoxly/Ascii-Motion)

Ascii-Motion 是一个用于创建和动画化 ASCII/ANSI 艺术的现代 Web 应用程序，采用双许可证和单体仓库结构，提供丰富的编辑、动画和导出功能。

- 🎨 **功能特性**：提供基于网格的 ASCII 艺术编辑器、动画时间轴、自定义调色板、图像/视频转 ASCII、多种导出格式以及社区画廊分享。
- 🚀 **快速开始**：项目需要 Node.js 18+ 环境，通过 `git clone` 和 `npm install` 安装，使用 `npm run dev` 进行开发。
- 🌐 **部署结构**：包含三个可独立部署的应用（主应用、营销站点、文档站点），分别部署到不同域名，支持自动化版本管理。
- 🏗️ **技术栈**：基于 React 18、TypeScript、Vite、Tailwind CSS、Shadcn/ui、Zustand 和 Lucide React 构建。
- 📦 **项目结构**：采用单体仓库设计，核心功能（MIT 许可证）与高级功能（专有许可证）分离，便于贡献者参与开源部分开发。
- 📋 **开发状态**：项目由个人维护，已完成基础编辑器、动画系统、导出/导入系统和高级工具等阶段，未来计划包括数据库集成和社区功能。
- 🤝 **贡献指南**：欢迎对核心开源包贡献新工具、动画功能、UI 改进等，需遵循项目代码规范并通过 PR 流程提交。
- 📜 **许可证**：核心功能采用 MIT 许可证，高级功能（如认证和云存储）为专有许可证，禁止未经授权的复制或分发。

---

### [TimescaleDB：排名第一的 PostgreSQL 时序数据库 | 开源与云端 | Tiger Data](https://www.tigerdata.com/timescaledb?utm_source=cooperpress&utm_medium=referral&utm_campaign=react-status-newsletter)

**原文标题**: [TimescaleDB: #1 PostgreSQL Time-Series Database | Open Source & Cloud | Tiger Data](https://www.tigerdata.com/timescaledb?utm_source=cooperpress&utm_medium=referral&utm_campaign=react-status-newsletter)

TimescaleDB 是基于 PostgreSQL 构建的时序数据库，提供自动分区、行列混合存储、高达 95% 的压缩率、增量物化视图、自动化数据管理和专用时序函数等核心功能，适用于物联网、加密金融和实时分析等场景。其托管云服务 Tiger Cloud 提供弹性扩展、数据分层、高可用性和安全合规等优势，同时支持自托管部署。

- 🗂️ 自动分区：通过超表实现按时间或 ID 自动分区，支持快速数据摄取和大规模查询优化
- 💾 行列混合存储：结合行存储与列存储，在降低成本的同时提升分析查询性能
- 📉 高效压缩：采用列式编码技术，压缩率高达 95%，支持在压缩数据上直接进行过滤和聚合
- 🔄 增量物化视图：通过连续聚合实现增量刷新的数据汇总，支持实时模式包含最新变更
- 🤖 自动化数据管理：内置任务调度器，可配置列存储、保留策略和连续聚合的自动化策略
- ⏱️ 专用时序函数：提供约 200 个原生 SQL 函数，简化高级时序分析并支持部分聚合以避免重复处理
- 🌐 托管云服务优势：Tiger Cloud 提供数据分层、统一数据架构、按需扩展计算、高可用架构和安全合规保障
- 🏭 多样化应用场景：广泛应用于物联网设备监控、加密金融数据分析和客户实时仪表板等领域
- 🛠️ 灵活部署选项：支持完全托管的云服务与自托管（社区版/企业版）两种部署方式
- 📊 企业级功能：包括多可用区架构、点对点恢复、跨区域复制和 SOC2/HIPAA/GDPR 合规认证

---

### [React Server Components 中的拒绝服务漏洞 · 安全通告 · facebook/react · GitHub](https://github.com/facebook/react/security/advisories/GHSA-83fc-fqcc-2hmg)

**原文标题**: [Denial of Service Vulnerabilities in React Server Components · Advisory · facebook/react · GitHub](https://github.com/facebook/react/security/advisories/GHSA-83fc-fqcc-2hmg)

React 官方披露了 React Server Components 中存在多个拒绝服务漏洞，这些漏洞源于之前修复不完整，攻击者可通过发送特制的 HTTP 请求触发，可能导致服务器崩溃、内存耗尽或 CPU 使用率激增，建议受影响用户立即升级至已修复版本。

- 🚨 **漏洞影响**：React Server Components 中存在多个拒绝服务漏洞，攻击者可利用特制 HTTP 请求导致服务器崩溃、内存异常或 CPU 占用过高。
- 📦 **受影响包**：`react-server-dom-webpack`、`react-server-dom-parcel`、`react-server-dom-turbopack` 的 19.0.0 至 19.2.3 版本。
- 🔧 **修复版本**：漏洞已在 19.0.4、19.1.5 和 19.2.4 版本中修复，建议用户立即升级。
- ⚠️ **漏洞条件**：仅在使用支持 React Server Components 的框架、打包工具或插件，且应用包含服务器端代码时受影响。
- 📊 **严重程度**：漏洞评级为高危（CVSS 7.5），攻击复杂度低，无需权限和用户交互，主要影响服务可用性。
- 🔗 **相关参考**：漏洞对应 CVE-2026-23864，涉及资源消耗不受控（CWE-400）和反序列化不可信数据（CWE-502）两类弱点。

---

### [CVE-2025-59471 与 CVE-2025-59472 漏洞摘要 - Vercel](https://vercel.com/changelog/summaries-of-cve-2025-59471-and-cve-2025-59472)

**原文标题**: [Summaries of CVE-2025-59471 and CVE-2025-59472 - Vercel](https://vercel.com/changelog/summaries-of-cve-2025-59471-and-cve-2025-59472)

Next.js 自托管应用中发现两个可能导致服务器内存耗尽的中等严重性拒绝服务漏洞，已发布修复版本，Vercel 托管的应用不受影响。

- 🖼️ **CVE-2025-59471**：当启用外部图像优化时，`/_next/image` 端点加载远程图像至内存且无大小限制，攻击者可通过超大图像导致内存耗尽。
- 🔄 **CVE-2025-59472**：在启用部分预渲染（PPR）且为最小模式的应用中，PPR 恢复端点处理未认证的 POST 请求时，可能因无限制的请求缓冲或解压导致内存耗尽。
- 📦 **受影响版本**：CVE-2025-59471 影响 Next.js 10 至 15.5.10 之前版本及 16 至 16.1.5 之前版本；CVE-2025-59472 影响 Next.js 15 至 15.6.0-canary.61 之前版本及 16 至 16.1.5 之前版本。
- ⚠️ **影响范围**：两个漏洞均可导致 Node.js 进程因内存耗尽而终止，造成应用停机；需特定配置条件才可被利用。
- 🛠️ **解决方案**：已发布修复版本 15.5.10、15.6.0-canary.61、16.1.5 和 16.2.0-canary.9；无法立即升级可采取限制远程图像模式、禁用 PPR 或最小模式、在反向代理层设置严格请求大小限制等临时措施。
- 🙏 **致谢**：感谢 Andrew MacPherson 通过漏洞赏金计划负责任地披露此问题。

---

### [JavaScript 框架 - 迈向 2026 年 - DEV 社区](https://dev.to/this-is-learning/javascript-frameworks-heading-into-2026-2hel)

**原文标题**: [JavaScript Frameworks - Heading into 2026 - DEV Community](https://dev.to/this-is-learning/javascript-frameworks-heading-into-2026-2hel)

本文回顾了 2025 年 JavaScript 框架的发展趋势，指出行业焦点已从性能优化转向更宏观的战略思考，尤其是 AI 的全面渗透重塑了开发范式。框架设计正经历核心重构，强调通用性、同构优先和异步优先架构，以应对日益复杂的应用需求和 AI 工具带来的挑战。

- 🤖 **AI 优先框架兴起**：AI 正深刻影响框架设计，Remix 3 等框架开始减少领域特定语言，以更好地与 AI 生成的通用代码集成，这标志着开发重心从性能转向与 AI 协作的适应性。
- 🔄 **同构优先架构成为主流**：开发者对服务器驱动方案（如岛屿架构和 RSC）的复杂性感到不满，因此 Tanstack Start、SvelteKit 等框架推动同构优先模式，允许代码在服务器和客户端共享，平衡效率与开发体验。
- ⚡ **异步处理成为核心演进方向**：框架如 React 和 Svelte 正在深化异步更新的原生支持，通过“Transitions”等机制确保 UI 一致性，这预示着异步能力将成为未来框架的基础标配。
- 🧩 **AI 推动底层模式复兴**：AI 工具倾向于组合底层代码片段，促使开发者重新关注原始模式而非复杂抽象，这间接简化了系统设计，但也要求框架提供更明确的局部控制与全局协调能力。
- 🛠️ **行业进入核心 refinement 阶段**：与往年追求颠覆性架构不同，当前框架更注重基于经验教训的通用优化，这种变化将深刻影响开发思维，而不仅仅是代码编写方式。

---

### [未找到标题](https://www.solidjs.com/)

**原文标题**: [No title found](https://www.solidjs.com/)

本文介绍了人工智能在医疗领域的应用现状与前景，重点探讨了其在疾病诊断、药物研发和个性化治疗方面的突破性进展，同时简要提及了相关的伦理挑战。

- 🏥 AI 辅助诊断系统能通过分析医学影像快速识别病灶，提升早期癌症等疾病的检出率
- 🔬 机器学习加速了新药研发流程，大幅缩短化合物筛选与临床试验设计周期
- 📊 基于患者基因数据的人工智能模型可为慢性病患者提供个性化治疗方案
- ⚖️ 医疗 AI 面临数据隐私、算法透明度及责任认定等伦理监管问题

---

### [Reddit——互联网之心](https://www.reddit.com/r/reactjs/comments/1qkthp8/started_using_the_react_compiler_and_was_pretty/?rdt=39738)

**原文标题**: [Reddit - The heart of the internet](https://www.reddit.com/r/reactjs/comments/1qkthp8/started_using_the_react_compiler_and_was_pretty/?rdt=39738)

作者尝试使用 React 编译器后，应用性能显著提升，体验流畅度明显改善。

- 🚀 应用响应速度大幅提升，路由、表单和过渡效果都变得更加迅捷顺滑
- ⚙️ 在已有 Webpack 和 SWC 配置基础上，通过重新安装 Babel 成功运行 React 编译器
- 📈 对性能改善预期不高，但实际效果远超预期，即使应用本身存在大量优化空间
- 🧠 应用中原有手动记忆化使用很少，编译器自动优化减少了性能调优负担
- 🔄 正在借助 Claude 工具迁移 Formik 以兼容 React 19 特性并集成编译器
- 📦 计划将优化成果打包发布，收集社区反馈后再整合到现有项目中

---

### [Reddit——互联网之心](https://www.reddit.com/r/reactjs/comments/1qqu390/tanstack_vs_react_router_vs_next/?rdt=45520)

**原文标题**: [Reddit - The heart of the internet](https://www.reddit.com/r/reactjs/comments/1qqu390/tanstack_vs_react_router_vs_next/?rdt=45520)

一位开发者询问在 2026 年构建前端 Web 应用时，如何在 TanStack、React Router 和 Next.js 之间选择，特别关注 PWA 开发。

- 🤔 开发者长期维护遗留 React 代码，现计划新建一个最终转为 PWA 的 Web 应用
- ⚖️ 在 TanStack、React Router（已与 Remix 合并）和 Next.js 之间权衡选择
- 🚀 Next.js 看似是明显选择，但听说 TanStack 表现优异
- 🔄 对 React Router 与 Remix 合并后的发展表示认可，但缺乏使用经验
- ❓ 征求社区意见，以决定从当前（2026 年）视角出发的最佳框架选择

---

### [Expo SDK 55 Beta 现已发布 - Expo 更新日志](https://expo.dev/changelog/sdk-55-beta)

**原文标题**: [Expo SDK 55 Beta is now available - Expo Changelog](https://expo.dev/changelog/sdk-55-beta)

Expo SDK 55 Beta 现已发布，为期约两周，供开发者测试新功能并反馈问题。此版本包含多项重要更新与改进。

- 🚀 **SDK 55 Beta 发布**：包含 React Native 0.83.1 和 React 19.2.0，开发者可通过测试帮助完善稳定版本。
- 🏗️ **移除旧架构支持**：SDK 55 起不再支持 Legacy Architecture，相关配置选项已删除。
- 📱 **全新默认项目模板**：采用原生标签页 API，优化设计，并引入 `/src` 文件夹结构以分离代码与配置。
- ⚡ **Hermes v1 可选启用**：带来性能提升和现代 JavaScript 功能支持，但需从源码构建 React Native。
- 📦 **Hermes 字节码差分更新**：通过 `expo-updates` 和 EAS Update 减少更新包大小，提升下载速度。
- 🤖 **AI 工具扩展**：新增 MCP 服务器支持 CLI 操作，并提供官方 AI 技能库辅助开发。
- 🧭 **Expo Router 功能增强**：包括新的 Colors API、Apple Zoom 过渡、Stack.Toolbar API 及实验性 SplitView 支持。
- 🔗 **改进现有原生应用集成**：推出 `expo-brownfield` 包，简化将 Expo 嵌入现有原生应用的过程。
- 🎨 **Expo UI 测试版进展**：SwiftUI 组件 API 更新以更贴近原生，Jetpack Compose API 测试版即将推出。
- 📦 **统一包版本管理**：所有 Expo SDK 包现使用与 SDK 相同的主版本号，便于兼容性识别。
- 🛠️ **Expo Modules Core 升级**：支持 Swift 6 语言模式、ArrayBuffer 及新的静态函数 API。
- 📲 **实验性 iOS 主屏幕小工具**：通过 `expo-widgets` 可用 Expo UI 组件创建小工具和实时活动。
- 🌫️ **Android 模糊效果稳定**：`expo-blur` 在 Android 12+ 上使用高效 RenderNode API。
- 📤 **实验性数据分享支持**：`expo-sharing` 新增接收共享数据的功能，通过配置插件实现。
- 🌐 **Expo Web 改进**：重写错误覆盖层，新增服务器端渲染和数据加载器实验性支持。
- 🛠️ **模块功能更新**：包括 `expo-contacts`、`expo-media-library`、`expo-calendar` 的新 API，以及 `expo-audio`、`expo-sqlite`、`expo-camera`、`expo-video`、`expo-image` 的增强。
- ⚠️ **弃用与破坏性变更**：移除 `app.json` 中的 `notification` 配置，弃用部分 API，并停止对 Android 上 Expo Go 的推送通知支持。
- 🐛 **已知问题与测试指南**：鼓励开发者升级项目并报告问题，参与测试以帮助完善版本。

---

### [Gal Schlezinger @ ReactNext '25 | 使用 React 服务器组件提升性能！ - YouTube](https://www.youtube.com/watch?v=TInTm-M5yBs)

**原文标题**: [Gal Schlezinger @  ReactNext '25 | Improving Performance using React Server Components! - YouTube](https://www.youtube.com/watch?v=TInTm-M5yBs)

该文本为 YouTube 网站底部的通用信息与链接列表，概述了平台的功能、政策与公司信息。

- 📄 关于平台的基本信息与公司介绍
- 📰 新闻与媒体相关资源
- ©️ 版权声明与知识产权
- 📞 联系与反馈渠道
- 🧑‍🎨 内容创作者相关资源
- 📢 广告与商业合作信息
- 👨‍💻 开发者工具与资源
- 📜 服务条款与使用协议
- 🔒 隐私政策与数据保护
- ⚙️ 平台政策与安全指南
- 🔧 YouTube 功能运作说明
- 🧪 新功能测试与更新
- 🏢 谷歌公司所有权与年份信息

---

### [AGENTS.md 在我们的代理评估中表现优于技能 - Vercel](https://vercel.com/blog/agents-md-outperforms-skills-in-our-agent-evals)

**原文标题**: [AGENTS.md outperforms skills in our agent evals - Vercel](https://vercel.com/blog/agents-md-outperforms-skills-in-our-agent-evals)

我们原本预期技能（skills）是教授 AI 编程助手框架特定知识的最佳方案。但在针对 Next.js 16 API 构建评估测试后，我们发现了意想不到的结果：直接嵌入在 AGENTS.md 中的一个压缩的 8KB 文档索引实现了 100% 的通过率，而技能方案即使在明确指示助手使用的情况下，最高也只能达到 79%。如果没有这些指示，技能的表现与完全没有文档时无异。

- 🎯 **问题背景**：AI 编程助手依赖的训练数据会过时。Next.js 16 引入了如 `'use cache'`、`connection()` 和 `forbidden()` 等新 API，这些内容尚未包含在现有模型的训练数据中，导致助手生成错误代码或使用旧模式。

- 🔄 **两种方法**：我们测试了两种方案：1) **技能**：一种按需调用的、打包了提示、工具和文档的开放标准。2) **AGENTS.md**：一个位于项目根目录的 Markdown 文件，为助手提供持久化的上下文信息，无需助手主动加载。

- ❌ **技能的局限性**：在默认情况下，技能在 56% 的评估案例中从未被触发，通过率与无文档基线（53%）相同。即使添加了技能，也未带来任何提升。

- 📝 **指令的脆弱性**：在 AGENTS.md 中添加明确指令（如“先探索项目结构，然后调用技能”）能将技能触发率提升至 95% 以上，通过率提高到 79%。但指令的细微措辞变化会导致助手行为结果差异巨大，方案显得脆弱。

- 🧪 **可靠的评估**：我们强化了评估测试套件，专注于测试那些不在模型训练数据中的 Next.js 16 API，确保了结果的可信度。

- 💡 **关键洞察与方案**：我们尝试将文档索引直接嵌入 AGENTS.md，并添加关键指令：“对于任何 Next.js 任务，优先采用检索引导的推理，而非预训练引导的推理”。这移除了助手“是否需要查找”的决策点。

- 🏆 **出乎意料的结果**：AGENTS.md 文档索引方案在强化评估中实现了 100% 的通过率，在构建、代码检查和测试各项细分指标上均获满分，显著超越了技能方案（即使有明确指令）。

- 🤔 **原因分析**：被动上下文（AGENTS.md）优于主动检索（技能）的原因可能在于：1) 无决策点；2) 信息持续可用；3) 避免了“先读文档还是先探索项目”的排序问题。

- 📦 **处理上下文膨胀**：通过压缩，我们将初始约 40KB 的文档注入内容减少到 8KB（压缩 80%），同时保持了 100% 的通过率。压缩格式使用管道分隔的结构，将文档索引打包到最小空间，助手在需要时可读取`.next-docs/`目录中的具体文件。

- 🛠️ **如何尝试**：可以通过命令 `npx @next/codemod@canary agents-md` 为你的 Next.js 项目一键设置。该命令会检测 Next.js 版本，下载匹配的文档到`.next-docs/`，并将压缩索引注入到你的 AGENTS.md 中。

- 📚 **对框架作者的启示**：技能并非无用，它更适用于用户明确触发的、垂直的、特定动作的工作流（如升级版本、迁移路由）。而对于通用的框架知识，目前被动的上下文方案表现更优。建议：不要等待技能改进；积极压缩内容；使用针对未训练 API 的评估进行测试；设计便于检索的文档结构。最终目标是推动助手从“预训练引导的推理”转向“检索引导的推理”，而 AGENTS.md 是目前实现这一目标最可靠的方式。

---

### [介绍：React 最佳实践 - Vercel](https://vercel.com/blog/introducing-react-best-practices)

**原文标题**: [Introducing: React Best Practices - Vercel](https://vercel.com/blog/introducing-react-best-practices)

该文章介绍了名为“react-best-practices”的代码仓库，它总结了超过 10 年的 React 和 Next.js 性能优化经验，旨在帮助开发者系统性地识别和解决常见的性能问题，如异步瀑布流、包体积过大和过度重渲染等。该框架按影响程度排序优化规则，并支持 AI 代码助手集成，以提升团队协作和代码审查效率。

- 🚀 **核心优化框架**：提出按影响程度排序的性能优化方法，优先解决异步瀑布流和包体积过大等高影响问题。
- 📦 **结构化规则库**：包含 8 个类别、40 多条规则，涵盖服务器端性能、客户端数据获取、重渲染优化等，每条规则标注影响等级并提供代码示例。
- 🤖 **AI 助手集成**：规则可编译为`AGENTS.md`文档，支持 Opencode、Claude Code 等 AI 编码助手调用，实现自动化代码审查与优化建议。
- ⚡ **实战经验提炼**：规则源于真实生产环境案例，如合并循环迭代、并行化异步操作、惰性状态初始化等具体优化技巧。
- 🎯 **问题驱动设计**：针对“响应式优化”（事后补救）的痛点，提供前瞻性优化框架，降低长期维护成本。

---

### [文员 MCP 服务器](https://clerk.com/changelog/2026-01-20-clerk-mcp-server?utm_source=cooper-press&utm_medium=newsletter&utm_campaign=mcp-server&utm_content=01-30-26&dub_id=iSB6FHmczlGq94Uq)

**原文标题**: [Clerk MCP Server](https://clerk.com/changelog/2026-01-20-clerk-mcp-server?utm_source=cooper-press&utm_medium=newsletter&utm_campaign=mcp-server&utm_content=01-30-26&dub_id=iSB6FHmczlGq94Uq)

Clerk 推出 MCP 服务器公开测试版，使 AI 编程助手能直接获取最新的 Clerk SDK 代码片段和实现模式，提升开发效率。

- 🚀 Clerk 发布 MCP 服务器公开测试版，为 AI 编程助手提供实时 SDK 支持
- 🤖 兼容 Claude、Cursor 和 GitHub Copilot 等工具，实现智能代码辅助
- 💡 可查询 Next.js 身份验证钩子、B2B SaaS 权限设置等具体实现方案
- 📚 提供完整设置指南和文档，方便开发者快速集成
- 💬 开放反馈渠道，鼓励用户通过门户和 Discord 社区参与讨论

---

### [TanStack Start 中的单次飞行突变：第一部分 – Frontend Masters 博客](https://frontendmasters.com/blog/single-flight-mutations-in-tanstack-start-part-1/)

**原文标题**: [Single Flight Mutations in TanStack Start: Part 1 – Frontend Masters Blog](https://frontendmasters.com/blog/single-flight-mutations-in-tanstack-start-part-1/)

本文介绍了在 TanStack Start 中实现“单次飞行突变”的基础概念和简单实现，通过结合 TanStack Query、Router 和 Start 工具，实现在一次网络往返中完成数据突变和 UI 更新，从而提升应用性能。

- 🚀 **单次飞行突变概念**：指在一次网络请求中同时完成数据变更和 UI 更新，减少网络往返次数以优化性能。
- 🛠️ **技术栈依赖**：利用 TanStack 生态（Query、Router、Start）的现有工具实现，其中 Start 提供服务器端功能如 SSR 和 API 路由。
- 📊 **性能优化动机**：网络请求是 Web 应用中最耗时的环节，减少往返次数能显著提升用户体验，类似服务端渲染的优势。
- 🔄 **传统更新流程问题**：通常需要先发送更新请求，再重新获取数据来刷新 UI，可能导致额外请求或数据不一致。
- 🧪 **简单实现示例**：通过 TanStack Start 的服务器函数，在更新数据后直接获取并返回相关查询结果，客户端使用 QueryClient 更新 UI 缓存。
- ⚙️ **迭代与改进方向**：当前实现硬编码数据获取逻辑，后续可通过中间件机制解耦，提高代码复用性和灵活性。
- 📚 **系列文章结构**：本文为第一部分，介绍基础实现；第二部分将深入中间件和 TypeScript 高级应用。

---

### [将 CSS 裁剪引入 React Native](https://www.callstack.com/blog/bringing-css-clipping-to-react-native)

**原文标题**: [Bringing CSS Clipping to React Native](https://www.callstack.com/blog/bringing-css-clipping-to-react-native)

本文探讨了在 React Native 中原生实现 CSS clip-path 属性的技术方案，旨在让开发者能够像在 Web 上一样轻松创建非矩形裁剪效果，而无需依赖第三方库。

- 🎯 **clip-path 功能引入**：React Native 目前缺乏类似 Web CSS 中 clip-path 的裁剪功能，导致创建复杂形状（如星形、圆形）界面元素时需借助第三方库，本文提出了原生集成该属性的完整技术路径。
- 🏗️ **架构适配挑战**：由于 React Native 采用与 Web 不同的渲染架构（通过原生 UI 组件而非统一图形引擎），实现 clip-path 需在 JavaScript 层、C++ 核心层及 iOS/Android 平台层进行系统化改造。
- 📱 **平台具体实现**：在 iOS 端通过扩展`RCTViewComponentView`的`invalidateLayer`方法，利用 Core Animation 的`CALayer`掩码功能实现裁剪；在 Android 端则通过重写`View`的`draw`方法，使用`Canvas.clipPath`进行画布裁剪。
- 🔄 **新架构优势利用**：方案基于 React Native 新架构（Fabric），通过 C++ 统一数据类型定义、影子节点（Shadow Node）属性传递和跨平台渲染管线协同，确保裁剪功能的高性能与一致性。
- 🚀 **开发体验提升**：实现后将允许开发者直接使用类似 CSS 的语法（如`clipPath: 'circle(50%)'`）在 React Native 中创建裁剪效果，减少跨平台代码差异，提升样式代码复用性。

---

### [博客 > 编写优质单元测试](https://eliocapella.com/blog/writing-good-unit-tests/)

**原文标题**: [Blog > Writing Good Unit Tests](https://eliocapella.com/blog/writing-good-unit-tests/)

本文探讨了编写高质量单元测试的核心原则，强调测试应关注行为而非实现细节，以提升部署信心和代码质量。

- 🎯 测试行为而非实现细节：避免测试内部函数或结构，应通过公共接口验证业务逻辑，确保重构时无需修改测试。
- 🚫 谨慎使用模拟：仅模拟系统边缘（如网络请求），而非内部层，以减少测试与实现的耦合，提升测试可靠性。
- 🛠️ 务实选择测试工具：对于后端数据库测试，使用内存数据库而非模拟客户端，以兼顾测试速度和置信度。
- 📡 合理模拟 HTTP 请求：通过录制真实 HTTP 请求生成测试夹具，确保第三方库更新时测试仍能可靠验证行为。
- ⚡ 避免性能陷阱：警惕 Jest+jsdom 组合的性能问题，考虑使用真实浏览器或高效替代方案（如 Vitest）提升测试速度。
- 📊 覆盖率的价值与风险：100% 覆盖率可作为质量目标，但需避免为达标而编写无效测试，应鼓励通过测试优化代码结构。
- ✅ 终极检验标准：优秀的测试套件应赋予团队在周五晚上自信部署的能力，体现其实际价值。

---

### [Facehash - 适用于 React 的优雅极简头像](https://www.facehash.dev/)

**原文标题**: [Facehash - Beautiful Minimalist Avatars for React](https://www.facehash.dev/)

Facehash 是一个轻量级 React 组件，能够根据任意字符串生成独特的头像。它无需依赖外部服务，完全离线运行，确保相同输入始终产生相同头像，并支持通过 Next.js 路由生成 PNG 图片。该组件适用于用户资料、聊天应用、评论区和 AI 代理等多种场景。

- 🎨 **生成独特头像**：根据字符串（如邮箱、用户名）生成友好、一致的头像
- 📦 **零依赖轻量**：无外部依赖，适用于 Next.js、Vite、Remix 等框架
- 🔄 **完全确定性**：相同输入必得相同头像，无需 API 调用或存储
- 🖼️ **支持图片生成**：通过 Next.js 路由处理程序生成可缓存的 PNG 图片
- ⚙️ **高度可定制**：支持调整尺寸、颜色、3D 强度、变体等属性
- ♿ **默认无障碍**：内置可访问性支持，提供完整的 TypeScript 类型
- 🛠️ **灵活使用方式**：可直接使用 React 组件或通过图片 URL 调用
- 🧩 **包含头像包装器**：提供 Avatar 组件支持图片加载失败时的回退显示
- 🌐 **广泛适用场景**：适用于用户资料、聊天应用、评论系统、游戏及 AI 代理等

---

### [React Tilt 按钮 - 带弹性按压与悬停倾斜的 3D 触感 React 按钮组件](https://react-tilt-button.vercel.app/)

**原文标题**: [React Tilt Button - 3D Tactile React Button Component with Squishy Press & Hover Tilt](https://react-tilt-button.vercel.app/)

本文介绍了人工智能在医疗领域的应用现状与前景，重点探讨了其在疾病诊断、治疗方案优化及医疗管理效率提升方面的作用，并简要提及了相关的伦理挑战。

- 🤖 AI 辅助诊断系统能通过分析医学影像快速识别病灶，提高早期疾病检出率
- 💊 机器学习算法可基于患者数据生成个性化治疗方案，提升治疗效果
- 📊 智能管理系统优化医院资源分配，减少患者等待时间并降低运营成本
- ⚖️ 数据隐私与算法透明度成为 AI 医疗应用过程中需要关注的核心伦理议题

---

### [GitHub - archisvaze/react-tilt-button：一款适用于React的触感3D按钮，悬停时倾斜，按压时挤压。现代设计，无依赖。](https://github.com/archisvaze/react-tilt-button)

**原文标题**: [GitHub - archisvaze/react-tilt-button: A tactile 3D button for React that tilts on hover and squishes on press.  Modern and dependency-free.](https://github.com/archisvaze/react-tilt-button)

这是一个用于 React 的触感 3D 按钮组件，具有悬停倾斜和按压挤压效果，设计现代且无依赖。

- 🎛️ **功能特性**：悬停时倾斜（左/中/右）、按压时挤压、具有可见“侧壁”深度、通过物理约束确保视觉不崩溃、支持预定义样式变体、可通过属性完全配置。
- 📦 **安装使用**：通过 npm 安装，导入组件和 CSS 即可使用，提供基础点击功能和多种预定义视觉变体（如 solid、outline、arcade 等）。
- 🛠️ **自定义配置**：支持手动覆盖几何参数（宽度、高度、深度等）、颜色、边框及动态高光效果，所有值均受物理约束自动限制。
- 🎨 **样式与主题**：视觉由 CSS 变量驱动，便于外部主题定制；组件行为基于物理 UI 原语，响应鼠标释放动作，悬停分区域检测。
- 🔗 **资源与演示**：提供在线演示页面，可测试所有变体、调整参数并查看实时效果；项目开源，包含详细文档和示例代码。

---

### [GitHub - mutativejs/travels：一个基于Mutative JSON Patch 的快速、框架无关的撤销/重做核心库](https://github.com/mutativejs/travels)

**原文标题**: [GitHub - mutativejs/travels: A fast, framework-agnostic undo/redo core powered by Mutative JSON Patch](https://github.com/mutativejs/travels)

Travels 是一个基于 Mutative JSON Patch 构建的快速、框架无关的撤销/重做核心库，它通过仅存储状态变化而非完整快照来实现高效的内存使用和性能。

- 🚀 **高性能与内存高效** – 采用 JSON Patch 仅存储状态差异，相比传统快照方式内存占用显著降低，并基于 Mutative 实现比 Immer 快 10 倍的不可变更新。
- 🔧 **框架无关** – 可与 React、Vue、Zustand、MobX、Pinia 或原生 JavaScript 无缝集成。
- 📦 **灵活的归档模式** – 支持自动归档（每次 `setState` 创建历史记录）和手动归档（通过 `archive()` 控制，支持批量操作合并为单个撤销步骤）。
- 🔄 **可变模式支持** – 通过 `mutable: true` 选项保持状态引用稳定，适用于依赖对象身份的可观察库（如 MobX、Vue/Pinia）。
- ⚠️ **状态要求** – 状态必须为 JSON 可序列化（对象、数组、字符串、数字、布尔值、null），不支持 Date、类实例、函数等复杂类型。
- 📖 **丰富的 API** – 提供 `back()`、`forward()`、`go()`、`reset()`、`subscribe()` 等方法，支持历史记录限制（`maxHistory`）和持久化存储。
- 🛠️ **高级扩展** – 可通过包装方法添加验证、权限控制、日志记录、元数据附加等自定义逻辑。

---

### [GitHub - mutativejs/use-travel：一个具备撤销、重做、重置及存档功能的React状态时光旅行钩子。](https://github.com/mutativejs/use-travel)

**原文标题**: [GitHub - mutativejs/use-travel: A React hook for state time travel with undo, redo, reset and archive functionalities.](https://github.com/mutativejs/use-travel)

use-travel 是一个基于 Mutative 和 Travels 构建的 React Hook，用于实现状态时间旅行功能，支持撤销、重做、重置和存档等操作，具有高性能和可定制化特性。

- 🚀 **功能特性**：提供撤销、重做、重置、跳转和存档功能，支持通过 JSON Patch 记录历史，可自定义历史记录大小和初始补丁。
- ⚙️ **使用方式**：通过 `useTravel` Hook 管理状态，返回当前状态、状态设置器和控制对象，包含 `back()`、`forward()`、`reset()` 等方法。
- 🧩 **存档模式**：支持自动存档（默认）和手动存档模式，手动模式下可通过 `archive()` 将多个状态变更合并为一个历史记录点。
- ⚠️ **注意事项**：在同步调用栈中，`setState` 只能调用一次，以确保撤销/重做行为的可预测性。
- 💾 **持久化支持**：可通过 `state`、`controls.patches` 和 `controls.position` 保存历史记录，并在初始化时恢复。
- 🔧 **扩展用法**：通过 `useTravelStore` 可在 React 组件外管理共享的 Travels 实例，实现跨组件的状态历史同步。

---

### [React2AWS - 基础设施即 React 组件](https://www.react2aws.xyz/)

**原文标题**: [React2AWS - Infrastructure as React Components](https://www.react2aws.xyz/)

AWS 基础设施即代码工具，通过 React JSX 语法和类 Tailwind 样式配置，自动生成生产就绪的 Terraform 代码。

- 🚀 **创新开发体验**：使用 React 组件语法定义云资源，类 Tailwind 的 className 配置方式让基础设施编写更直观
- ⚡ **三步工作流**：编写 JSX → 配置属性 → 自动生成符合最佳实践的 Terraform 文件
- 🏗️ **全面资源支持**：覆盖 VPC、RDS、Fargate、Lambda、S3、DynamoDB 等核心 AWS 服务，持续扩展中
- 🛠️ **开发者友好功能**：实时预览、智能补全、安全内置的 Terraform 模块、一键导出和分享
- 🌐 **零配置启动**：完全浏览器端运行，无需安装即可开始构建基础设施

---

### [GitHub - xzdarcy/react-timeline-editor: react-timeline-editor 是一个用于快速构建时间轴动画编辑器的 React 组件。](https://github.com/xzdarcy/react-timeline-editor)

**原文标题**: [GitHub - xzdarcy/react-timeline-editor: react-timeline-editor is a react component used to quickly build a timeline animation editor.](https://github.com/xzdarcy/react-timeline-editor)

这是一个用于快速构建时间轴动画编辑器的 React 组件，提供丰富的功能和灵活的配置选项。

- 🚀 **快速构建**：通过 React 组件快速搭建时间轴动画编辑器界面
- 📦 **简单集成**：通过 npm 安装即可使用，支持 TypeScript
- 🎬 **动画编辑**：支持时间轴上的动作管理和效果配置
- 📚 **完整文档**：提供详细文档展示基础功能和高级特性
- ⚙️ **灵活配置**：可自定义时间轴数据、效果和编辑器行为
- 🔧 **技术栈**：基于 TypeScript 开发，包含 Less、MDX 等多语言支持
- 📄 **开源许可**：采用 MIT 许可证，拥有活跃的社区贡献
- 🌟 **受欢迎度**：获得 662 个星标和 155 个分支，表明项目受到开发者认可

---

### [无](https://zdarcy.com/guide/editor/101-basic.html)

**原文标题**: [None](https://zdarcy.com/guide/editor/101-basic.html)

本文介绍了人工智能在医疗领域的应用现状与前景，重点探讨了其在疾病诊断、药物研发和个性化治疗方面的突破性进展，同时提及了相关的伦理挑战和未来发展趋势。

- 🤖 AI 辅助诊断系统能通过分析医学影像快速识别病灶，提升早期疾病检出率
- 💊 机器学习加速新药研发流程，大幅缩短化合物筛选与临床试验周期
- 🧬 基于基因数据的个性化治疗方案正成为精准医疗的核心发展方向
- ⚖️ 医疗 AI 面临数据隐私、算法透明度与责任归属等伦理监管挑战
- 🌐 跨机构医疗数据共享与联邦学习技术有望突破数据孤岛困境
- 🏥 智能手术机器人已实现亚毫米级操作精度，推动微创外科革新
- 📱 可穿戴设备结合 AI 实现全天候健康监测与慢性病管理
- 🔮 量子计算与 AI 融合将在未来十年引发医疗数据分析范式变革

---

### [GitHub - callstackincubator/ai：在React Native 中通过 Vercel AI SDK 兼容实现设备端 LLM 执行](https://github.com/callstackincubator/ai)

**原文标题**: [GitHub - callstackincubator/ai: On-device LLM execution in React Native with Vercel AI SDK compatibility](https://github.com/callstackincubator/ai)

这是一个用于 React Native 的本地 AI 工具库，提供与 Vercel AI SDK 兼容的 API，支持在用户设备上直接运行 AI 模型，以实现隐私保护、低延迟且无需服务器成本的推理。

- 🚀 **即时 AI** - 无需下载即可立即使用内置系统模型
- 🔒 **隐私优先** - 所有处理均在设备本地进行，数据不会离开设备
- 🎯 **兼容 Vercel AI SDK** - 可作为替代方案，使用熟悉的 API
- 🎨 **完整工具包** - 提供文本生成、嵌入、转录、语音合成等功能
- 🍎 **Apple 原生集成** - 支持 iOS 设备上的 Apple 基础模型、嵌入、转录和语音合成
- 🦙 **Llama 支持** - 可通过 llama.rn 运行任何 GGUF 模型，需从 HuggingFace 下载
- ⚙️ **MLC 运行时** - 使用 MLC LLM 优化的运行时在设备上运行流行的开源 LLM
- 📱 **跨平台** - 支持 iOS 和 Android 平台
- 📚 **详细文档** - 提供全面的指南和 API 参考，网站为 react-native-ai.dev

---

### [react-dropzone](https://react-dropzone.js.org/)

**原文标题**: [react-dropzone](https://react-dropzone.js.org/)

本文介绍了人工智能在医疗领域的应用现状与前景，重点探讨了其在疾病诊断、治疗方案优化及医疗管理效率提升方面的作用，并简要提及了相关的伦理考量。

- 🏥 AI 辅助诊断系统能通过分析医学影像快速识别病灶，提升早期疾病检出率
- 💊 基于机器学习的个性化治疗方案可结合患者数据优化用药与治疗路径
- 📊 智能医疗管理平台能整合病例信息，自动化流程，减轻医护人员行政负担
- ⚖️ 需重视数据隐私保护与算法透明度，建立合理的医疗 AI 伦理监管框架

---

### [GitHub - focus-trap/focus-trap-react: 一个用于捕获焦点的 React 组件](https://github.com/focus-trap/focus-trap-react)

**原文标题**: [GitHub - focus-trap/focus-trap-react: A React component that traps focus](https://github.com/focus-trap/focus-trap-react)

focus-trap-react 是一个 React 组件，用于在界面中创建一个焦点陷阱，确保键盘焦点被限制在特定区域内，常用于实现可访问的模态框等交互组件。

- 🎯 **功能核心**：基于 focus-trap 库封装，提供 React 专用的焦点陷阱管理，自动在挂载时激活、卸载时停用。
- ⚙️ **安装使用**：通过 npm 安装，支持 React 18+，需注意 React 19 不再支持 propTypes 和 defaultProps。
- 🖥️ **浏览器兼容**：主要支持现代桌面浏览器（Chrome、Edge、Firefox 等），不再支持 IE。
- 🧩 **组件用法**：包裹单个子元素（不能是 Fragment），可通过 props 控制激活、停用、暂停状态。
- ⚠️ **注意事项**：在 React 18 严格模式下需避免使用 onActivate/onDeactivate 等回调影响组件状态，防止意外行为。
- 🔧 **高级配置**：支持 focusTrapOptions 传递配置，可使用 containerElements 属性以编程方式指定陷阱边界元素。
- 🧪 **测试提示**：建议在真实浏览器环境（如 Cypress）测试，JSDom 中需配置 tabbableOptions.displayCheck: 'none'。
- 👥 **开源贡献**：项目遵循 MIT 许可，提供贡献指南和安全政策，由社区共同维护。

---

### [发布 v2.0.0-alpha.1 · web-infra-dev/rspack · GitHub](https://github.com/web-infra-dev/rspack/releases/tag/v2.0.0-alpha.1)

**原文标题**: [Release v2.0.0-alpha.1 · web-infra-dev/rspack · GitHub](https://github.com/web-infra-dev/rspack/releases/tag/v2.0.0-alpha.1)

Rspack 发布了 2.0.0-alpha.1 版本，包含多项重大变更、新功能、错误修复、重构及文档更新。

- 🛠 **重大变更**：恢复了 `enable verbatimModuleSyntax` 功能
- 🎉 **新功能**：包括改进外部模块渲染、内置 React 服务器组件、向 JavaScript 暴露依赖位置
- 🐞 **错误修复**：涉及模板依赖、路径标准化、模块联邦、状态访问及清单生成等多个方面
- 🔨 **重构优化**：统一了缓存恢复逻辑，调整了钩子命名和构建流程
- 📖 **文档更新**：更新了外部函数回调类型说明，并添加了生产构建中 `devtool` 使用的提示
- 📦 **其他变更**：发布了上一个 alpha 版本，更新了安全依赖，并调整了 CI 和测试配置

---

### [rsbuild-plugin-rsc/examples 位于 main · rstackjs/rsbuild-plugin-rsc · GitHub](https://github.com/rstackjs/rsbuild-plugin-rsc/tree/main/examples)

**原文标题**: [rsbuild-plugin-rsc/examples at main · rstackjs/rsbuild-plugin-rsc · GitHub](https://github.com/rstackjs/rsbuild-plugin-rsc/tree/main/examples)

这是一个用于 React 服务端组件（RSC）的 Rsbuild 插件项目，由 rstackjs 组织维护，目前处于公开可访问状态。

- 🛠️ 这是一个 Rsbuild 插件，用于支持 React 服务端组件（RSC）
- 📂 项目托管在 GitHub 上，属于 rstackjs 组织
- 🌟 目前获得了 6 个星标，暂无复刻
- 📊 项目包含代码、议题、拉取请求等功能模块
- 🔒 包含安全性和项目洞察等高级管理选项
- 🔔 提供通知设置功能，但需要登录才能更改

---

### [注册 - Auth0](https://auth0.com/signup?onboard_app=auth_for_aa&ocid=701KZ000000cXXxYAM_aPA4z0000008OZeGAM?utm_source=cooperpress&utm_campaign=amer_namer_usa_all_ciam_dev_dg_plg_auth0_native_cooperpress_native_aud_jan_2026_placements_utm2&utm_medium=cpc&utm_id=aNKWR000002m8zp4AA)

**原文标题**: [Sign Up - Auth0](https://auth0.com/signup?onboard_app=auth_for_aa&ocid=701KZ000000cXXxYAM_aPA4z0000008OZeGAM?utm_source=cooperpress&utm_campaign=amer_namer_usa_all_ciam_dev_dg_plg_auth0_native_cooperpress_native_aud_jan_2026_placements_utm2&utm_medium=cpc&utm_id=aNKWR000002m8zp4AA)

这是一个 Auth0 平台的用户注册页面，提供多种注册方式并列出支持的国家/地区。

- 📧 可通过邮箱直接注册账户
- 🌍 注册时需选择国家，列表涵盖全球众多国家和地区
- 🔐 支持第三方快速登录：GitHub、Google、Microsoft 账户
- 📄 注册需同意服务条款和隐私政策
- 🆓 提供免费套餐，每月支持最多 2.5 万活跃用户
- 🛡️ 提供可定制的注册/登录流程和安全防护功能
- 🤖 新增 AI 代理连接外部应用及敏感操作的人工审批功能
- 👥 支持自定义社交登录和无密码连接方式
- 🛠️ 专为开发者设计，含暴力破解防护和渐进式画像功能

---

### [React 峰会 2026](https://ti.to/gitnation/react-summit-2026/discount/REACTSTATUS)

**原文标题**: [React Summit 2026](https://ti.to/gitnation/react-summit-2026/discount/REACTSTATUS)

React Summit 2026 是一场关于 React 技术的年度国际会议，将于 2026 年 6 月 12 日至 16 日在荷兰阿姆斯特丹举行，汇聚全球前端和全栈工程师。2025 年起，活动将采用混合形式，首日线下举办并包含线上互动，次日及多个免费工作坊将向全球在线直播。

- 🗓️ **时间**：2026 年 6 月 12 日至 16 日
- 🌍 **地点**：荷兰阿姆斯特丹的 Kromhouthal 场馆
- 👥 **参与者**：全球数千名前端和全栈工程师
- 🔄 **2025 年新形式**：混合模式（首日线下 + 线上互动，次日及工作坊在线直播）
- 🌐 **官方网站**：https://reactsummit.com/
- 🐦 **社交媒体**：X (Twitter) 和 Bluesky 官方账号
- 🎫 **票务与咨询**：通过官网获取门票，联系邮箱 events@gitnation.org

---

### [Bun v1.3.7 | Bun 博客](https://bun.com/blog/bun-v1.3.7)

**原文标题**: [Bun v1.3.7 | Bun Blog](https://bun.com/blog/bun-v1.3.7)

Bun v1.3.7 版本发布，带来了性能提升、新功能、API 增强和大量错误修复，涵盖安装、JavaScript 引擎、内置工具、Node.js 兼容性及开发体验优化。

- 🚀 **性能提升**：多项 JavaScript 内置方法（如 `Buffer.from()`、`async/await`、`Array.from`、字符串填充、数组扁平化）和 ARM64 平台性能得到显著优化。
- 🔧 **安装与升级**：支持通过 curl、npm、PowerShell、Scoop、Homebrew 和 Docker 多种方式安装 Bun，并使用 `bun upgrade` 命令进行升级。
- ⚙️ **JavaScriptCore 引擎升级**：底层引擎升级至最新版 WebKit JavaScriptCore，带来性能改进和错误修复。
- 🛠️ **新内置工具**：新增 `Bun.wrapAnsi()` 用于处理 ANSI 转义码的文本换行，性能远超现有 npm 包；新增 `Bun.JSON5` 和 `Bun.JSONL` 支持，用于解析 JSON5 和 JSONL 格式。
- 📊 **性能分析增强**：CPU 性能分析器支持生成 Markdown 格式报告；新增堆内存分析功能，支持生成 V8 快照和 Markdown 报告。
- 🔌 **API 与兼容性改进**：`fetch` 和 `node:https` 现在保留 HTTP 请求头的原始大小写；WebSocket 支持 URL 中的凭据；`node:inspector` Profiler API 现已实现；`bun:ffi` 尊重 `C_INCLUDE_PATH` 和 `LIBRARY_PATH` 环境变量。
- 📦 **包管理与构建**：`bun pm pack` 现在尊重 `package.json` 生命周期脚本的修改；`bun build --compile` 相关问题得到修复；捆绑器（bundler）多个错误被修复。
- 🐛 **大量错误修复**：修复了涉及 `bun install`、`bun test`、`Bun.serve()`、Bun Shell、Node.js 兼容性模块（如 `node:http2`、`node:fs`、`node:https`）、WebSocket、Streams、`bun:sql` 以及 Windows 平台等的众多问题。
- 🙏 **致谢贡献者**：感谢 11 位贡献者的付出。

---

### [Bun v1.3.8 | Bun 博客](https://bun.com/blog/bun-v1.3.8)

**原文标题**: [Bun v1.3.8 | Bun Blog](https://bun.com/blog/bun-v1.3.8)

本文介绍了 Bun 的安装与升级方法，以及其最新版本中新增的 Markdown 解析器、构建分析工具和一系列错误修复。

- 📦 **安装 Bun**：支持多种安装方式，包括 curl、npm、PowerShell、Scoop、Homebrew 和 Docker。
- 🔄 **升级 Bun**：通过 `bun upgrade` 命令可轻松升级。
- 📝 **内置 Markdown 解析器**：Bun 新增了基于 Zig 的快速、符合 CommonMark 标准的 Markdown 解析器，提供 `html()`、`render()` 和 `react()` 三种渲染方式，并默认支持 GitHub 风格的扩展功能。
- 📊 **构建分析工具**：`bun build` 新增 `--metafile-md` 选项，可生成 Markdown 格式的模块依赖图，便于使用 LLM 分析包体积和依赖链。
- 🐛 **错误修复**：包括修复了 `napi_typeof` 返回值错误、堆快照生成崩溃、`node:vm` 模块崩溃、HTTP/2 流状态处理问题以及 Windows 上 `npm i -g bun` 安装失败等问题。

---

### [Yarn 6 预览版 | Yarn](https://yarn6.netlify.app/blog/2026-01-28-yarn-6-preview/)

**原文标题**: [Yarn 6 Preview | Yarn](https://yarn6.netlify.app/blog/2026-01-28-yarn-6-preview/)

Yarn 6 预览版正式发布，标志着 Yarn 将用 Rust 重写，以大幅提升性能、降低内存占用，并引入新功能如 Yarn Switch 和 Lazy Installs，预计稳定版将于 2026 年第三季度推出。

- 🚀 **性能大幅提升**：通过 Rust 重写，Yarn 6 在冷热缓存下安装速度显著加快，例如 Next.js 项目冷缓存从 4.1 秒降至 2.5 秒。
- 🔄 **Yarn Switch 工具**：替代 Corepack，自动根据项目配置下载并切换 Yarn 版本，提升开发体验。
- ⚡ **Lazy Installs 默认模式**：在运行命令时自动检测并静默安装依赖，结合零安装优势，避免仓库臃肿。
- 🗺️ **版本路线图**：Yarn 5.x 将作为过渡版本发布，6.x 稳定后，5.x 进入长期支持阶段，确保向后兼容。
- 🔧 **持续开发与社区参与**：Windows 支持、交互命令等关键功能仍在开发中，鼓励社区贡献和赞助支持。

---

### [StyleX — 面向雄心勃勃界面的样式系统](https://stylexjs.com/)

**原文标题**: [StyleX — styling system for ambitious interfaces](https://stylexjs.com/)

StyleX 是一个用于构建雄心勃勃界面的表达性强、类型安全、可组合、可预测且可主题化的样式系统。

- 🚀 **快速上手** – 提供入门指南和开发资源
- 🧠 **设计理念** – 介绍“Thinking in StyleX”设计思路
- 🔧 **开发工具** – 包含 API 文档、学习资源和在线演练场
- 🌐 **社区参与** – 提供博客、GitHub 等社区交流渠道
- 📄 **法律信息** – 包含版权声明、隐私政策等法律文档

---

### [新年新气象，StyleX 网站焕新登场](https://stylexjs.com/blog/a-new-year-2026)

**原文标题**: [New Year, New Website | StyleX](https://stylexjs.com/blog/a-new-year-2026)

StyleX 是一个由 Meta 开发并开源的 CSS-in-JS 解决方案，经过六年发展，已成为 Meta 内部默认的 Web 样式编写方式，并于 2023 年底开源。2025 年，它获得了 Figma、Snowflake 和 HubSpot 等公司的采用，并基于社区反馈新增了多项 API 和功能。项目近期推出了新的无插件集成包、完全在浏览器中运行的在线 Playground，以及一个使用 Waku 和 Fumadocs 重建的全新官网，以更好地展示其特性。团队对社区的支持表示感谢，并计划在 2026 年继续改进开发者体验和工具。

- 🎉 **开源与采用**：StyleX 在 Meta 内部成熟后于 2023 年底开源，2025 年获多家知名公司采用。
- 🛠️ **功能增强**：根据反馈新增了共享媒体查询、视图过渡、锚点定位和组合器样式等 API。
- 📦 **简化集成**：发布了 `@stylexjs/unplugin` 包，显著降低了在 Web 项目中的集成配置复杂度。
- 🌐 **新版 Playground**：推出了基于浏览器的全新 Playground，无需搭建项目即可快速体验，并支持代码分享。
- 🏗️ **官网重建**：使用 Waku 和 Fumadocs 从头重建了官网，完全采用 StyleX 编写样式，展示了其对 React 服务器组件的兼容性。
- 🚀 **未来规划**：计划在 2026 年着重改善开发者体验、开发新功能和增强工具链。

---

### [游乐场 | StyleX](https://stylexjs.com/playground)

**原文标题**: [Playground | StyleX](https://stylexjs.com/playground)

该网站是 Meta Platforms 公司推出的一个 AI 开发平台，提供全面的工具和资源，支持开发者学习、构建和探索人工智能应用。

- 📚 **开发与学习资源** – 提供 API 文档、教程和指南，帮助开发者掌握 AI 技术
- 🧪 **交互式实验环境** – 设有 Playground 沙盒，供用户实时测试和调试 AI 模型
- 🌐 **社区与开源生态** – 通过 GitHub 等渠道鼓励开发者参与协作和贡献
- 📄 **内容与更新** – 设有博客板块，定期发布技术动态和产品更新
- ⚖️ **法律与规范** – 明确标注隐私政策、服务条款及版权声明，确保合规性

---

### [经过两年的氛围编程，我回归手写创作。](https://atmoio.substack.com/p/after-two-years-of-vibecoding-im)

**原文标题**: [After two years of vibecoding, I'm back to writing by hand](https://atmoio.substack.com/p/after-two-years-of-vibecoding-im)

作者回顾了两年使用 AI 编程的经历，最终回归手动编码。他认识到 AI 在初期任务中表现令人惊艳，但处理复杂项目时，其代码缺乏整体一致性和结构性，导致代码质量低下，无法满足实际生产需求。因此，他选择回归传统编程方式，认为综合考虑效率、准确性和创造力后，手动编码更具优势。

- 🤖 初期使用 AI 编程时，对简单和大型任务的表现都令人印象深刻，引发对职业替代的担忧
- 📝 尝试通过详细规范文档指导 AI，但发现规范在真实开发中需动态调整，而 AI 无法灵活适应
- 🧩 AI 生成的代码在孤立查看时看似合理，但缺乏整体架构一致性和对现有代码模式的尊重
- 🚫 累积的 AI 代码质量低下，作者因不愿向用户交付不可靠产品而放弃使用
- ✍️ 回归手动编码后，作者在效率、准确性、创造力和整体生产力上均超越 AI
- 📢 作者在社交媒体分享 AI 编程经验，并提供了相关视频内容的链接

---

### [Svg 路径编辑器](https://yqnn.github.io/svg-path-editor/)

**原文标题**: [SvgPathEditor](https://yqnn.github.io/svg-path-editor/)

该页面提示需要启用 JavaScript 才能正常使用此应用或网站。

- 🔧 请确保浏览器设置中已启用 JavaScript 功能
- 🌐 部分现代网页应用依赖 JavaScript 实现核心交互
- 📱 若使用移动设备，请检查浏览器权限设置
- 🔄 尝试刷新页面或重启浏览器后重新访问

---

