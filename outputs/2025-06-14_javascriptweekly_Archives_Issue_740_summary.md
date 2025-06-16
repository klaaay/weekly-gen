### [JavaScript 周刊第 740 期：2025 年 6 月 13 日](https://javascriptweekly.com/issues/740)

**原文标题**: [JavaScript Weekly Issue 740: June 13, 2025](https://javascriptweekly.com/issues/740)

- 📧 订阅服务随时可取消，邮箱安全有保障（附隐私政策链接）。  
- ⚛️ React 在 2025 年仍是 JavaScript 生态核心，Redux 维护者 Mark Erikson 解析其发展历程与未来方向。  
- ⚡ Notion 通过优化将输入延迟降低 15%，Palette 赞助商提供免费 JS 性能分析工具。  
- 🚀 Oxlint 1.0 发布：基于 Rust 的超快 JavaScript/TypeScript 代码检查工具，性能提升 50~100 倍。  
- 📦 pnpm 10.12 引入实验性全局虚拟存储，提升多项目依赖共享效率。  
- 🍎 Safari 26（Beta）支持 RegExp 模式修饰符，WWDC25 还有非“液态玻璃”相关更新。  
- 🔒 OpenPGP.js 漏洞曝光；Node.js 版本升级提醒；Gleam 语言 JS 编译速度提升 30%。  
- 🛠️ 发布速递：H3 v2、Node.js 24.2、VS Code 支持 ES 模块、Deno 2.3.6 等。  
- 🚨 Dan Abramov 呼吁谨慎禁用代码检查规则，避免掩盖严重问题。  
- 📜 回顾 2006-2015 年前 ES6 时代的 JavaScript 代码风格。  
- 🔥 Wallaby 推出 AI 集成测试运行器，实时提供覆盖率与调试洞察。  
- 🔄 Node 原生模块钩子实现高效热更新功能。  
- 📺 视频/文章推荐：避免滥用 JSON 解析、ESLint 插件增强 DSL、Angular 20 亮点等。  
- 📊 npmgraph 工具可视化 npm 依赖关系图；Jest 30 发布，性能显著提升。  
- 🍊 Orange ORM：支持 TypeScript/JavaScript 的 Active Record 风格 ORM。  
- 🌙 DarkModeJS 2.0：基于系统偏好管理深色模式的工具库。  
- 🎮 Odyc.js 像素游戏开发库；Midscene.js 让 AI 操作浏览器。  
- 🤖 GitHub 第 10 亿个仓库诞生（NSFW 名称）；Shopify 改进 import maps；TypeScript 编译器正移植至 Go。

---

### [2025 年 React 与社区现状 · Mark 的开发博客](https://blog.isquaredsoftware.com/2025/06/react-community-2025/)

**原文标题**: [
     The State of React and the Community in 2025 ·  Mark's Dev Blog
  ](https://blog.isquaredsoftware.com/2025/06/react-community-2025/)

React 及其社区在 2025 年的状态复杂且分裂，既有成功也有质疑和争议。

- 🚀 React 是最广泛使用的 UI 框架，其概念影响了整个 JavaScript 生态系统。React 19 的发布带来了 React Server Components 的稳定支持、新的 `use` hook、表单集成等。
- 🤔 社区对 React 的发展方向、开发方式以及推荐的使用方法感到越来越沮丧和分歧。
- 🗣️ 沟通问题、自我营销失误以及 React 团队缺乏开发者关系工作加剧了这些争议。
- 📜 React 团队强烈推荐使用框架来构建 React 应用，认为框架能提供更好的性能和开发体验。
- 🔄 React Server Components (RSCs) 是 React 团队的未来愿景，但需要与框架紧密集成才能使用。
- ⚖️ React 的开发由 Meta 和 Vercel 共同赞助，部分核心团队成员从 Meta 转至 Vercel，推动了 RSCs 的发展。
- 📉 Create React App (CRA) 已不再维护，社区逐渐转向 Vite 等现代构建工具。
- 📚 官方文档对 RSCs 的解释不足，导致社区对其理解混乱，甚至产生误解。
- 💡 React 团队的目标是通过框架和 RSCs 提升应用性能，但这一推荐缺乏对多样化使用场景的考虑。
- 🌍 社区对 Vercel 和 Next.js 的主导地位感到担忧，认为其可能影响 React 的中立性。

---

### [React 状态](https://react.statuscode.com/)

**原文标题**: [React Status](https://react.statuscode.com/)

每周汇总最新的 React 和 React Native 相关链接和教程。  

- 📬 57722 位订阅者 — 展示广泛的读者群体  
- 📰 431 期内容 — 提供丰富的资源积累  
- 🔗 支持 RSS 订阅 — 方便获取更新  
- 📌 示例可查看最新一期 — 直观了解内容形式  
- 🏢 由 Cooperpress 发布 — 专业团队运营  
- 🔒 严格的隐私、反垃圾邮件和 GDPR 政策 — 重视用户数据安全

---

### [宣布 Oxlint 1.0 | 零之虚空](https://voidzero.dev/posts/announcing-oxlint-1-stable)

**原文标题**: [Announcing Oxlint 1.0 | VoidZero](https://voidzero.dev/posts/announcing-oxlint-1-stable)

Oxlint 1.0 稳定版正式发布，这是一款基于 Rust 的 JavaScript 和 TypeScript 代码检查工具，性能比 ESLint 快 50~100 倍，支持超过 500 条 ESLint 规则，并被 Shopify、Airbnb 和梅赛德斯 - 奔驰等大型公司采用。

- 🚀 **性能卓越**：Oxlint 在大型代码库中表现优异，例如在 264,925 个文件上仅需 22.5 秒完成检查。
- 💼 **企业应用**：Shopify、Airbnb 和梅赛德斯 - 奔驰等公司已采用 Oxlint，显著减少 CI 时间和成本。
- ⚡ **快速上手**：无需配置即可运行，支持 npm、pnpm、yarn、bun 和 deno 等多种包管理器。
- 🔧 **灵活配置**：支持通过 `.oxlintrc.json` 文件进行配置，兼容 ESLint 的扁平化配置格式。
- 📊 **规则覆盖**：包含 500 多条规则，涵盖 ESLint、TypeScript 及多个流行插件规则。
- 🛠 **编辑器支持**：提供 VS Code、IntelliJ IDEA 和 WebStorm 等编辑器的扩展支持。
- 🔍 **清晰诊断**：提供详细的错误报告和修复建议，帮助开发者快速解决问题。
- 🏗 **未来计划**：包括支持自定义规则、性能优化和更细粒度的配置选项。
- 🙏 **社区贡献**：感谢 200 多位贡献者的努力，特别表彰核心团队的杰出贡献。
- 📢 **加入社区**：通过 Discord、GitHub 和问题跟踪器反馈意见，共同推动 Oxlint 发展。

---

### [pnpm 10.12 引入全局虚拟存储及扩展版本...](https://socket.dev/blog/pnpm-introduces-global-virtual-store-and-expanded-version-catalogs)

**原文标题**: [pnpm 10.12 Introduces Global Virtual Store and Expanded Vers...](https://socket.dev/blog/pnpm-introduces-global-virtual-store-and-expanded-version-catalogs)

研究发现，恶意浏览器扩展正通过可信商店传播，威胁用户安全。  

- 🕵️ Socket 研究人员揭露恶意扩展如何劫持会话、重定向流量并操控用户行为。  
- 🛒 这些扩展伪装成合法工具，潜伏在官方应用商店中，增加了检测难度。  
- 🔄 攻击者利用扩展权限窃取数据、篡改页面内容或诱导用户至钓鱼网站。  
- ⚠️ 用户需谨慎安装扩展，定期检查权限并移除不必要或可疑的插件。  
- 🔍 建议企业部署扩展管理策略，监控员工浏览器环境以降低风险。

---

### [快速、节省磁盘空间的包管理器 | pnpm](https://pnpm.io/)

**原文标题**: [Fast, disk space efficient package manager | pnpm](https://pnpm.io/)

pnpm 是一个快速、高效且严格的包管理工具，支持单体仓库，并采用非扁平的 node_modules 结构来提升安全性和性能。

- ⚡ pnpm 的速度比 npm 快 2 倍  
- 💾 通过硬链接或克隆单一存储来高效管理 node_modules 文件  
- 📦 内置支持单体仓库（monorepo）的多包管理  
- 🔒 默认创建非扁平的 node_modules 结构，防止代码随意访问未声明的包  
- 🏢 由赞助商支持开发

---

### [发布 pnpm 10.12.1 · pnpm/pnpm · GitHub](https://github.com/pnpm/pnpm/releases/tag/v10.12.1)

**原文标题**: [Release pnpm 10.12.1 · pnpm/pnpm · GitHub](https://github.com/pnpm/pnpm/releases/tag/v10.12.1)

pnpm 10.12.1 版本发布，引入全局虚拟存储实验性支持，优化依赖管理并新增多项功能与改进。

- 🚀 **全局虚拟存储支持**：实验性功能，通过中央虚拟存储（默认位于`<store-path>/links`）管理依赖，提升安装速度（需在`pnpm-workspace.yaml`中启用`enableGlobalVirtualStore`）。  
- ⚠️ **CI 环境自动禁用**：在冷缓存环境下可能降低性能，pnpm 会在 CI 中自动关闭此功能。  
- 🔗 **依赖图哈希隔离**：类似 NixOS 的包管理方式，通过哈希创建独立可复用的包目录。  
- 🔄 **catalog 协议依赖更新**：`pnpm update`现支持更新`catalog:`协议依赖，并支持多种模式（`strict`/`prefer`/`manual`）。  
- ➕ **新增 CLI 选项**：`pnpm add`支持`--save-catalog`将依赖保存为 catalog 条目。  
- 🔧 **副作用缓存键变更**：旧版本生成的缓存不再兼容，需重新生成（半破坏性变更）。  
- 🤖 **显式 CI 设置**：新增`ci`配置项明确环境类型。  
- 🐞 **补丁修复**：修复版本排序、错误信息显示及回归问题（如#9596）。  
- 📹 **演示视频**：展示新功能加速效果（[YouTube 链接](https://www.youtube.com/watch?v=pNDFfJvaubY)）。

---

### [WWDC25 消息：Safari 26 测试版中的 WebKit | WebKit](https://webkit.org/blog/16993/news-from-wwdc25-web-technology-coming-this-fall-in-safari-26-beta/)

**原文标题**: [  News from WWDC25: WebKit in Safari 26 beta | WebKit](https://webkit.org/blog/16993/news-from-wwdc25-web-technology-coming-this-fall-in-safari-26-beta/)

WWDC25 发布了 Safari 26 beta 版本，包含 67 项新功能和 107 项改进。以下是关键内容概述：

- 🌐 **SVG 图标支持**：Safari 26 beta 现在支持 SVG 格式的图标，包括网站图标（favicons），提供无限矢量缩放能力。
- 📱 **所有网站均可作为 Web 应用**：在 iOS 和 iPadOS 上，任何添加到主屏幕的网站默认以 Web 应用形式打开，用户可自行选择是否在浏览器中打开。
- 🖼️ **HDR 图像支持**：Safari 26 beta 新增对高动态范围（HDR）图像的支持，提供更生动的视觉效果。
- 🛠️ **WebKit 与 SwiftUI 集成**：新增 `WebView` 和 `WebPage` 类型，简化在 SwiftUI 应用中集成网页内容的过程。
- 🕶️ **visionOS 上的 `<model>` 元素**：支持嵌入交互式 3D 模型，用户可通过手势与模型互动。
- 🎥 **沉浸式视频和音频**：visionOS 上的 Safari 支持空间视频和 Apple 沉浸式视频，提供更丰富的媒体体验。
- 🎮 **WebGPU 支持**：新增对 WebGPU 的支持，提供更高效的图形和计算能力，适用于 macOS、iOS、iPadOS 和 visionOS。
- 🎨 **CSS 新特性**：
  - **锚点定位**：简化元素定位，适用于弹出菜单和工具提示。
  - **滚动驱动动画**：将动画与滚动行为绑定。
  - `text-wrap: pretty`：优化文本换行，提升排版效果。
  - `contrast-color()` 函数：自动选择对比色。
- 🔒 **数字凭证 API**：支持从 Apple Wallet 或其他应用中安全请求身份凭证。
- 🛡️ **隐私增强**：阻止已知指纹脚本访问敏感信息，保护用户隐私。
- 🐞 **大量错误修复**：涵盖可访问性、CSS、Canvas、DOM、表单、JavaScript、媒体等多个领域。

开发者可通过安装 macOS Tahoe 26、iOS 26、iPadOS 26 或 visionOS 26 的 beta 版本，或直接下载 Safari 26 beta 进行测试。反馈可通过官方渠道提交。

---

### [获取失败](https://javascriptweekly.com/link/170478/web)

**原文标题**: [Failed to retrieve](https://javascriptweekly.com/link/170478/web)

无法总结：获取内容失败，状态码 520。

---

### [Node.js — 警惕已终止支持的版本，请升级或寻求终止后支持](https://nodejs.org/en/blog/announcements/node-18-eol-support)

**原文标题**: [Node.js — Beware of End-of-Life Node.js Versions - Upgrade or Seek Post-EOL Support](https://nodejs.org/en/blog/announcements/node-18-eol-support)

Node.js 18 及更早版本已停止支持，存在严重安全风险，建议跳过 Node.js 20 直接升级至 Node.js 22 以获得更长的支持周期和更好的性能。若无法升级，可考虑商业支持服务。

- 🚨 Node.js 18 及更早版本已停止支持，不再接收安全更新，存在严重安全风险。
- 🔍 Node.js 20 存在多个安全漏洞，包括高、中、低严重性问题。
- 📉 老旧版本（如 v16 及以下）仍有数千万次月下载量，面临已知漏洞威胁。
- 🛠️ 使用 is-my-node-vulnerable 工具检查当前 Node.js 版本是否存在已知漏洞。
- 🚀 Node.js 22 是更明智的升级目标，支持至 2027 年 4 月，性能更优且功能更全。
- ⏳ Node.js 20 的支持周期较短，升级至 22 可避免短期内再次升级。
- 📊 目前约 30% 的 Node.js 用户仍在使用不受支持的版本。
- 🔧 开发团队应直接迁移至 Node.js 22，跳过中间版本以减少升级疲劳。
- 💼 无法立即升级的组织可通过 HeroDevs 等商业支持服务获得临时解决方案。
- 🔮 升级至 Node.js 22 是未来保障应用安全与性能的最佳选择。

---

### [Gleam 语言](https://gleam.run/)

**原文标题**: [Gleam language](https://gleam.run/)

Gleam 是一种结合了强大类型系统、函数式编程表达能力和高并发、容错的 Erlang 运行时的现代编程语言，具有简洁的语法和丰富的工具链支持。

- 💪 结合类型系统、函数式编程和 Erlang 运行时，提供可靠性和高并发能力
- 🚀 运行在久经考验的 Erlang 虚拟机上，支持任意规模的工作负载
- 🧵 基于 actor 模型的并发系统，可运行数百万个并发绿色线程
- 🛠️ 内置编译器、构建工具、格式化程序和包管理器，开箱即用
- 📦 可访问整个 BEAM 生态系统，兼容 Erlang 和 Elixir 包
- ❤️ 无空值、无异常，提供清晰的错误信息和实用的类型系统
- 🌍 支持多语言交互，可编译为 JavaScript 和生成 TypeScript 定义
- 🤝 友好的社区环境，欢迎各种背景的开发者
- ✉️ 提供简洁的新闻通讯，保持与社区的沟通

---

### [Gleam JavaScript 速度提升 30%](https://gleam.run/news/gleam-javascript-gets-30-percent-faster/)

**原文标题**: [Gleam JavaScript gets 30% faster](https://gleam.run/news/gleam-javascript-gets-30-percent-faster/)

Gleam v1.11.0 发布，带来性能提升、新功能和多项改进。

- 🚀 **性能提升**：Gleam 编译到 JavaScript 的代码性能提升 30%，尤其对复杂模式匹配的项目效果更显著。
- 🌳 **模式匹配优化**：通过决策树优化模式匹配，减少重复检查，提升效率。
- 🧪 **新测试语法**：引入 `assert` 语法，提供更详细的测试失败信息，提升调试体验。
- 📂 **开发目录支持**：新增 `dev/` 目录，用于存放开发专用代码，避免生产环境误用。
- ⚠️ **未使用值警告**：编译器现在会警告未使用的返回值，帮助避免常见错误。
- 📜 **文档改进**：生成的文档现在显示更清晰的类型变量和模块限定符。
- 🛠️ **语言服务器增强**：提升对常量的支持，新增生成变体代码动作，改进未使用导入的清理。
- 🏗️ **构建工具改进**：`gleam export erlang-shipment` 现在正确处理 POSIX 退出信号。
- 💻 **多平台支持**：新增 Windows ARM64 预编译二进制文件。
- 🧩 **其他改进**：包括位数组截断警告、模式匹配错误标签显示等多项小优化。

---

### [H3 v2 测试版 - H3](https://h3.dev/blog/v2-beta)

**原文标题**: [H3 v2 beta - H3](https://h3.dev/blog/v2-beta)

H3 v2 beta 版本发布，全面基于 Web 标准重构，兼容性强且性能大幅提升。新版本优化了跨运行时兼容性、框架兼容性和开发体验，同时引入了统一的服务器 API 层 srvx 和强类型支持。

- ⚡ **H3 v2 beta 发布** - 完全基于 Web 标准重构，性能更快，兼容性更强。  
- 🌐 **跨运行时支持** - 支持 Node.js、Deno、Bun 及边缘计算环境，实现统一开发体验。  
- 💥 **srvx 统一服务器 API** - 解决不同运行时接口差异，提供一致的开发接口。  
- 🚀 **性能大幅提升** - 请求处理速度提升 5 倍（Node.js）至 156 倍（Deno），核心包体积减少 90%。  
- ✅ **强类型 Web 标准** - 集成 fetchdts 项目，为 Web API 提供完善的类型支持。  
- 🧩 **中间件与插件系统** - 支持链式中间件和可复用插件，开发更灵活。  
- ⬆️ **平滑迁移** - 保留大部分 v1 功能，提供迁移指南降低升级成本。  
- ❤️ **社区驱动** - 由贡献者、赞助商和开源社区共同推动发展。  
- 🗺️ **未来计划** - 收集反馈、完善 API，并确保 Nitro v3 的兼容性。

---

### [Node.js — Node v24.2.0（当前版本）](https://nodejs.org/en/blog/release/v24.2.0)

**原文标题**: [Node.js — Node v24.2.0 (Current)](https://nodejs.org/en/blog/release/v24.2.0)

Node.js v24.2.0（Current）版本发布，包含多项重要更新和变更。

- 🚀 **移除 HTTP/2 优先级信号支持**：根据 RFC 9113，nghttp2 中移除了优先级信号支持，Node.js 24 中同步移除该功能。  
- 📌 **新增 import.meta.main**：ECMAScript 模块中新增布尔值，用于检测当前模块是否为进程入口点。  
- 📜 **文档更新与弃用**：  
  - 弃用`util.isNativeError`，推荐使用`Error.isError`。  
  - 弃用向`options.shell`传递空字符串的行为。  
  - 将`Symbol.dispose`和`asyncDispose`从实验性功能转为正式功能。  
- 🔧 **其他重要变更**：  
  - 文件系统：为`FileHandle`的`readableWebStream`添加`autoClose`选项。  
  - HTTP/2：新增诊断通道`http2.server.stream.finish`。  
  - 性能钩子：使事件循环延迟直方图可销毁。  
  - 权限：隐式允许应用入口点的文件系统读取权限。  
- 🛠️ **构建与依赖更新**：  
  - 更新 nghttp2 至 1.65.0。  
  - 更新 OpenSSL 生成容器至 Ubuntu 22.04。  
  - 更新 undici 至 7.10.0。  
- 📦 **下载与安装**：提供 Windows、macOS、Linux 等多平台安装包和二进制文件。

---

### [2025 年 5 月（版本 1.101）](https://code.visualstudio.com/updates/v1_101)

**原文标题**: [May 2025 (version 1.101)](https://code.visualstudio.com/updates/v1_101)

2025 年 6 月 12 日发布的 Visual Studio Code 1.101 版本带来了多项功能更新和优化，涵盖 MCP 支持、聊天工具集、源代码控制、任务配置等多个方面。

- 🚀 **MCP 支持增强**  
  - 新增对提示、资源和采样的支持  
  - 支持需要身份验证的 MCP 服务器  
  - 提供开发模式调试 MCP 服务器  
  - 支持从扩展发布 MCP 服务器  

- 💬 **聊天工具集**  
  - 支持将相关工具组合成工具集，便于管理和使用  
  - 可通过命令面板创建工具集，并在聊天中通过#提及使用  

- 🔍 **源代码控制改进**  
  - 在源代码控制图中查看文件  
  - 支持为 GitHub Copilot 编码代理分配和跟踪任务  

- 🛠️ **任务配置优化**  
  - 新增`instancePolicy`属性，用于控制任务实例达到限制时的行为  
  - 提供多种策略选项，如提示、静默、终止最新或最旧任务等  

- 🐍 **Python 扩展增强**  
  - 新增 Python 环境信息和包安装等聊天工具  
  - 支持从模板创建项目，包括包和脚本的快速生成  
  - 新增对`pyenv`和`poetry`的支持  

- 🔧 **扩展开发改进**  
  - 扩展现在可以发布 MCP 服务器集合  
  - 打包扩展时新增秘密扫描功能，防止敏感信息泄露  

- 🌐 **远程开发更新**  
  - 支持 SSH 预连接脚本  
  - 远程资源管理器功能改进  

- 🎨 **用户体验优化**  
  - 聊天界面中用户消息和 AI 回复的区分更明显  
  - 新增撤销请求的可见操作按钮和快捷键  
  - 改进编辑时的应用策略，提升大文件编辑效率  

- 📢 **其他亮点**  
  - 新增自定义聊天模式，支持为特定工作流定制聊天行为  
  - 终端支持 Python REPL 会话的语言服务器补全  
  - 新增无障碍提示音，如聊天需用户操作时的信号  

- 🛑 **重大变更**  
  - Node.js 扩展主机升级至 v22，可能影响依赖`navigator`对象的扩展  

- 🙏 **致谢**  
  - 感谢所有贡献者和社区成员的支持与反馈

---

### [2025 年 5 月（版本 1.101）](https://code.visualstudio.com/updates/v1_101#_adopting-esm-in-a-realworld-extension)

**原文标题**: [May 2025 (version 1.101)](https://code.visualstudio.com/updates/v1_101#_adopting-esm-in-a-realworld-extension)

Visual Studio Code 2025 年 5 月更新（版本 1.101）于 6 月 12 日发布，包含多项新功能和改进。

- 🚀 **MCP 功能扩展**：新增提示支持、资源管理、采样功能和认证服务器支持。
- 💬 **聊天工具集**：可将相关工具组合成工具集，便于管理和使用。
- 🔍 **源代码控制**：新增图形视图查看文件，支持在 VS Code 中分配和跟踪 GitHub Copilot 任务。
- 🛠️ **调试改进**：支持 MCP 服务器的开发模式，便于调试 Node.js 和 Python 服务器。
- 📂 **资源管理**：MCP 资源可作为聊天上下文，支持浏览和保存资源。
- 🔐 **认证支持**：支持需要认证的 MCP 服务器，可管理账户访问权限。
- 🎨 **用户体验改进**：聊天消息区分更明显，撤销请求操作更直观。
- ✏️ **编辑效率提升**：优化文件编辑方式，改进键盘快捷键。
- 📝 **隐式上下文**：简化当前文件作为聊天上下文的操作。
- 🔧 **任务配置**：使用 GitHub Copilot 快速修复任务配置错误。
- 🖥️ **自定义聊天模式**：可定义专属聊天模式，适应特定工作流程。
- 📊 **笔记本工具**：新增代理单元格执行的跟随模式，优化代理工作流程。
- 🔗 **源代码控制集成**：扩展 GitHub Pull Requests 功能，支持代理任务分配和跟踪。
- ⚙️ **终端改进**：支持 Python REPL 会话的语言服务器补全。
- 🌐 **远程开发**：SSH 预连接脚本和 Remote Explorer 改进。
- 🐍 **Python 工具**：新增聊天工具，支持环境信息和包管理。
- 📦 **扩展开发**：支持扩展打包时扫描敏感信息，避免泄露。
- 🔄 **Electron 35 更新**：提升至 Chromium 134 和 Node.js 22.15.1。
- 🙏 **社区贡献**：感谢众多开发者的代码提交和问题修复。

---

### [发布 v2.3.6 · denoland/deno · GitHub](https://github.com/denoland/deno/releases/tag/v2.3.6)

**原文标题**: [Release v2.3.6 · denoland/deno · GitHub](https://github.com/denoland/deno/releases/tag/v2.3.6)

Deno 是一个 JavaScript/TypeScript 运行时，最新版本为 v2.3.6，发布于 2025.06.12。该版本包含多项功能更新、错误修复和性能优化。

- 🚀 **功能更新**：新增 esbuild 支持的捆绑功能、fetch 对 vsock 套接字的支持、Node 解析条件标志以及部署子命令。  
- 🐛 **错误修复**：修复了捆绑、编译、覆盖率、HTTP、Node 兼容性等多个模块的问题。  
- 🔧 **Node 兼容性改进**：优化了 Buffer、EventEmitter、fs、sqlite 等模块的行为，使其更符合 Node.js 标准。  
- ⚡ **性能优化**：改进了进程生成路径，确保在 Unix 系统上快速执行。  
- 📦 **安装与升级**：支持通过 `deno upgrade` 或 curl 脚本安装/升级到最新版本。  
- 🔄 **其他修复**：涉及 zlib、Worker、锁文件处理等细节问题的修正。

---

### [发布 v4.43.0 · rollup/rollup · GitHub](https://github.com/rollup/rollup/releases/tag/v4.43.0)

**原文标题**: [Release v4.43.0 · rollup/rollup · GitHub](https://github.com/rollup/rollup/releases/tag/v4.43.0)

Rollup 最新版本 v4.43.0 发布，新增文件系统 API 功能并修复部分问题。

- 🚀 **版本更新**：Rollup 发布 v4.43.0 版本，最新更新于 2025 年 6 月 11 日。  
- 💻 **新功能**：新增 `fs` 选项和 `this.fs` API，用于替换文件系统模块（#5944）。  
- 🔧 **Pull Request**：由 @EggDice 和 @lukastaegert 贡献，添加了在 JS API 中覆盖文件系统模块的选项。  
- 👥 **贡献者**：感谢 EggDice 和 lukastaegert 的代码贡献。  
- ❤️ **社区反馈**：4 位用户（peterhirn, GauBen, cuikho210, mbeckem）对该版本表示支持。  
- ⚠️ **加载问题**：页面部分内容加载异常，需重新刷新以查看完整信息。

---

### [茉莉花/jasmine 发布说明/5.8.0.md · 主分支 · jasmine/jasmine · GitHub](https://github.com/jasmine/jasmine/blob/main/release_notes/5.8.0.md)

**原文标题**: [jasmine/release_notes/5.8.0.md at main · jasmine/jasmine · GitHub](https://github.com/jasmine/jasmine/blob/main/release_notes/5.8.0.md)

这是一个关于 GitHub 上 jasmine 项目的仓库页面概览。

- 🚀 **项目活跃度**: 该项目拥有 15.8k 星标和 2.2k 次分叉，显示出较高的社区关注度。  
- 🔍 **问题追踪**: 当前有 5 个未解决的问题，但暂无拉取请求或讨论。  
- ⚠️ **加载错误**: 页面加载时出现错误提示，可能需要重新加载。  
- 📂 **导航选项**: 提供代码、问题、拉取请求、讨论、操作、项目、Wiki 和安全等多个导航选项。  
- 🔒 **安全设置**: 包含安全相关的选项，但具体内容未显示。

---

### [Vue.js 开发者工具 – 获取此扩展适用于 🦊 Firefox (en-GB)](https://addons.mozilla.org/en-GB/firefox/addon/vue-js-devtools/)

**原文标题**: [Vue.js devtools – Get this Extension for 🦊 Firefox (en-GB)](https://addons.mozilla.org/en-GB/firefox/addon/vue-js-devtools/)

Firefox 浏览器扩展 Vue.js devtools 的介绍页面，提供 Vue.js 应用程序调试工具，支持 Vue3，需 Firefox 浏览器使用。

- 🔧 扩展名称：Vue.js devtools，用于调试 Vue.js 应用程序  
- 🦊 浏览器要求：需使用 Firefox 浏览器  
- ⬇️ 下载方式：提供 Firefox 下载链接及扩展安装  
- 📊 用户数据：78,600 用户使用，611 条评论，评分 4.7/5  
- 📸 功能截图：展示扩展界面  
- ℹ️ 扩展信息：版本 7.7.7，大小 3.61 MB，8 天前更新  
- 🔗 相关链接：主页、支持网站、MIT 许可证  
- ⚠️ 注意事项：v7 仅支持 Vue3，Vue2 用户需安装旧版  
- 🔍 权限要求：扩展开发者工具权限，访问所有网站数据  
- 💖 支持开发：鼓励用户小额捐助支持持续开发  
- 🌐 多语言支持：页面提供多种语言选项

---

### [压制的压制——过度反应](https://overreacted.io/suppressions-of-suppressions/)

**原文标题**: [Suppressions of Suppressions — overreacted](https://overreacted.io/suppressions-of-suppressions/)

构建失败通常由语法错误或模块缺失引起，但更广泛的情况（如 lint 失败）也应阻止部署。合理的规则抑制是必要的，但某些关键规则禁止被抑制，需通过额外 lint 规则或代码审查来约束。社会契约在工具设计中至关重要，需平衡灵活性与安全性。

- 🔧 构建失败不仅限于语法错误，还包括 lint 失败等需阻止部署的情况  
- 🚦 合理的规则抑制有助于处理误报或历史代码，但滥用可能导致严重问题  
- ⚠️ 关键规则应禁止被抑制，可通过新增 lint 规则或自动化检查约束  
- 👥 代码审查和社会契约（如强制链接工单）是防止违规抑制的有效手段  
- 🌐 工具设计需结合组织协作，平衡开发效率与系统稳定性

---

### [JavaScript 的早期编写历程](https://www.trevorlasn.com/blog/revisiting-legacy-javascript)

**原文标题**: [How JavaScript Was Written Back In the Day](https://www.trevorlasn.com/blog/revisiting-legacy-javascript)

回顾早期 JavaScript 的开发历程，作者通过研究 2006-2015 年的代码，发现早期框架的解决方案令人印象深刻。

- 🕰️ 2006 年 Web 开发面临浏览器兼容性问题，如 IE6 的市场主导和事件处理、CSS 选择器支持的不一致。
- 🛠️ jQuery 1.0 通过抽象浏览器差异，提供一致的 API，使 DOM 操作更直观，如链式调用`$('#element').addClass('active').fadeIn()`。
- 🔄 jQuery 的`get`方法通过 API 重载处理多种场景，如传递数组、无参数或数字时返回不同结果，使库更易用。
- 📜 早期 JavaScript 缺乏现代特性如`Array.from()`和展开运算符，开发者使用`[].push.apply(this, arguments)`等巧妙解决方案。
- 🔧 2010 年代初期，代码中常见手动回调管理、变量声明提升和`_.rest(arguments)`处理剩余参数的模式。
- 🌐 AJAX 请求依赖`XMLHttpRequest`或`ActiveXObject`，开发者使用`try/catch`处理兼容性问题。
- 📝 在 ES6 之前，开发者手动复制对象属性、使用构造函数和原型方法实现 OOP，以及`Object.create(null)`创建无原型对象。
- 🔍 全局变量如`Dep.target`用于状态跟踪，`while (i--)`循环用于性能优化，展示了开发者在语言限制下的创造力。
- 📚 文章最后推荐了相关 JavaScript 主题的阅读材料，如导入属性、管道操作符和错误处理等。

---

### [Copilot 代理工具与 MCP 支持](https://wallabyjs.com/blog/wallaby-mcp.html?utm_source=cooperpress&utm_medium=javascriptweekly&utm_content=javascriptweekly)

**原文标题**: [Copilot Agent tools and MCP support](https://wallabyjs.com/blog/wallaby-mcp.html?utm_source=cooperpress&utm_medium=javascriptweekly&utm_content=javascriptweekly)

Wallaby 和 Console Ninja 通过 MCP 服务器和 AI 工具，为开发者提供了深度代码运行时上下文，显著提升了 AI 代理在代码调试、测试生成和代码分析中的能力。  

- 🚀 **AI 代理工具支持** - Wallaby 新增对 Copilot Agent、Cursor、Windsurf 等 AI 代理的支持，使其能实时获取代码运行时数据。  
- 🔍 **深度上下文访问** - AI 代理可访问运行时值、执行路径、代码覆盖率等动态信息，超越静态分析的局限。  
- ⚙️ **两种集成方式** - 通过 VS Code 内置 AI 工具或独立 MCP 服务器，灵活适配不同开发环境和代理工具。  
- 🛠️ **实用场景示例** - 支持修复失败测试、生成新测试、分析代码覆盖率及优化代码等复杂任务。  
- 📌 **优化工作流建议** - 将复杂任务拆解为小步骤，并自定义代理规则以提升效率。  
- 📊 **新功能发布** - 新增交互式图表功能，可视化复杂运行时值。  
- 🔗 **资源与反馈** - 提供详细文档并鼓励用户反馈，以持续改进工具功能。

---

### [Immaculata.dev - Node.js 中原生的 HMR（技术解析）](https://immaculata.dev/blog/native-nodejs-hmr.html)

**原文标题**: [Immaculata.dev - HMR natively in Node.js (technical write up)](https://immaculata.dev/blog/native-nodejs-hmr.html)

Node.js 中原生实现 HMR（热模块替换）的技术方案，通过模块钩子和依赖树管理实现高效的状态更新，避免全量重启。

- 🚀 **快速开发关键**：最小化状态丢弃，仅使更改的模块及其依赖失效，而非全量重启。  
- 🔄 **传统方案缺陷**：基于 `node:vm` 的临时模块系统导致逻辑重复，与原生模块系统隔离。  
- 🎯 **原生解决方案**：通过 `node:module` 的模块钩子实现热更新，避免二次模块系统。  
- 📂 **文件树管理**：`FileTree` 类将文件加载到内存，并通过 `.watch()` 监听更新，利用 `EventEmitter` 触发事件。  
- ⚙️ **双钩子机制**：`useTree` 同时实现加载器钩子（替换 `fs.readFileSync`）和解析器钩子（追加版本号缓存）。  
- 🔗 **依赖树自动更新**：模块依赖变化时递归更新父模块版本，确保依赖链 freshness。  
- 🛠️ **简洁代码示例**：注册钩子后，模块按需重新执行，支持资源清理（如 Shiki 高亮库的销毁）。  
- ♻️ **实际应用**：本网站通过 `onModuleInvalidated` 事件释放高亮资源，实现编辑后无缝更新。

---

### [不要使用 JSON.parse 和 JSON.stringify - YouTube](https://www.youtube.com/watch?v=PtcQwb1uBhc)

**原文标题**: [DON'T Use JSON.parse & JSON.stringify - YouTube](https://www.youtube.com/watch?v=PtcQwb1uBhc)

YouTube 平台相关信息概览  

- 📢 **关于我们** - 提供 YouTube 的背景和基本信息  
- 🗞️ **新闻中心** - 获取 YouTube 的最新动态和公告  
- ©️ **版权信息** - 了解 YouTube 的版权政策和相关内容  
- 📩 **联系我们** - 提供与 YouTube 团队沟通的渠道  
- 🎨 **创作者信息** - 支持和服务内容创作者的资源  
- 💼 **广告合作** - 广告主和商家的合作机会  
- 🛠️ **开发者资源** - 面向开发者的工具和支持  
- 📜 **条款与条件** - 使用 YouTube 平台的法律条款  
- 🔒 **隐私政策** - 用户数据保护和隐私条款  
- ⚖️ **政策与安全** - 平台规则和安全指南  
- 🔧� **测试新功能** - 体验 YouTube 的最新测试功能  
- © **版权声明** - 2025 年 Google LLC 版权所有

---

### [ESLint 语言插件如何提升 DSL 可用性 - ESLint - 可插拔 JavaScript 代码检查工具](https://eslint.org/blog/2025/06/language-plugins-dsl-benefits/)

**原文标题**: [How ESLint language plugins enhance DSL usability - ESLint - Pluggable JavaScript Linter](https://eslint.org/blog/2025/06/language-plugins-dsl-benefits/)

ESLint 语言插件通过集成到领域特定语言（DSL）中，显著提升了开发体验、一致性和采用率。它允许开发者将最佳实践转化为可配置的规则，支持自定义规则开发，并利用现有编辑器集成，从而减少重复工作并加速语言生态的成长。

- 🛠️ **编码最佳实践** - 将语言的最佳实践转化为可配置的 ESLint 规则，确保团队一致性，避免依赖文档或人工审查。  
- 🚀 **超越语法错误** - 不仅处理语法问题，还支持团队根据偏好强制执行编码标准，保持代码库统一性。  
- 🔧 **支持自定义规则** - 用户可创建并分享自定义规则，促进知识共享和语言生态的有机发展。  
- 🎁 **免费功能集成** - 直接利用 ESLint 的成熟功能（如缓存、自动修复、调试配置等），无需从头构建检查工具。  
- 💻 **编辑器无缝兼容** - 自动支持主流编辑器（如 VS Code、JetBrains、Vim 等），节省开发工具集成成本。  
- 🌱 **加速语言采用** - 通过提供开箱即用的开发体验，降低学习门槛，提升 DSL 的采用率和代码质量。

---

### [JavaScript 应避免的事项 | WaspDev](https://waspdev.com/articles/2025-06-13/things-to-avoid-in-javascript)

**原文标题**: [Things to avoid in JavaScript | WaspDev](https://waspdev.com/articles/2025-06-13/things-to-avoid-in-javascript)

JavaScript 开发中应避免的常见错误与实践建议  

- 🚫 **避免使用`innerHTML`设置文本**：可能导致 HTML 解析错误，推荐使用`textContent`或`innerText`。  
- 🔍 **慎用`JSON.parse(JSON.stringify())`克隆对象**：无法处理`NaN`、循环引用等，优先使用`structuredClone()`。  
- 🤹 **不要依赖`JSON.stringify()`比较对象**：属性顺序差异会导致误判，需使用深度比较库（如 Lodash）。  
- 🗺️ **避免过度使用普通对象作为动态关联数组**：性能差且存在`__proto__`污染风险，改用`Map`类型。  
- ⚠️ **禁用`eval()`执行代码**：存在安全漏洞且性能低，改用`new Function()`。  
- ➕ **避免直接追加`innerHTML/textContent`**：会销毁原有 DOM 状态，推荐`insertAdjacentHTML/Text()`。  
- 📦 **务必使用 ES 模块化（`type="module"`）**：提供封装、依赖管理、严格模式等优势。  
- 🔄 **弃用`var`声明变量**：`let/const`作用域更安全，现代引擎已优化其性能。  
- === **严格相等（`===`）优于宽松相等（`==`）**：避免隐式类型转换的意外行为。  
- 💬 **字符串拼接推荐模板字面量**：`${变量}`语法更清晰易读。  

总结：JavaScript 持续进化，开发者应关注新特性以提升代码质量与安全性。

---

### [Angular v20 看似平淡无奇——实则不然的 6 个理由 - LogRocket 博客](https://blog.logrocket.com/angular-v20-update/)

**原文标题**: [Angular v20 might seem boring — Here are 6 reasons it’s not - LogRocket Blog](https://blog.logrocket.com/angular-v20-update/)

Angular v20 虽然看似平淡，但实际上包含了许多实用的升级和改进，以下是关键点总结：

- 🚀 **Angular v20 发布**：2025 年 5 月 28 日正式发布，虽然没有突破性重写，但持续优化架构、性能和开发者体验。  
- 🔗 **linkedSignal API**：用于管理相关状态，简化父子组件间的状态联动，避免复杂的 `effect` 和 `computed` 组合。  
- 🌐 **httpResource（实验性 API）**：基于 `HttpClient` 的声明式 HTTP GET 请求管理，自动处理数据、加载和错误状态。  
- ⚡ **增量水合（Incremental Hydration）**：通过 `@defer` 和触发器延迟加载非关键内容，提升 SSR 性能。  
- 🛠️ **动态组件绑定 API**：简化动态组件的输入/输出绑定，减少样板代码，支持双向绑定。  
- ✨ **模板语法增强**：新增指数运算符（`**`）、`in` 运算符和未标记模板字面量，提升代码可读性。  
- 🤖 **生成式 AI 支持**：提供 `llms.txt` 标准和文档，帮助 LLM 生成更好的 Angular 代码，并集成 AI 工具。  
- 🔧 **其他改进**：Zoneless 模式（开发者预览）、类型检查增强、DevTools 优化，以及 Vitest 实验性支持。  

Angular v20 通过稳定性和实用性升级，帮助开发者构建更高效、易维护的应用。

---

### [npmgraph - NPM 依赖关系图](https://npmgraph.js.org/)

**原文标题**: [npmgraph - NPM Dependency Diagrams](https://npmgraph.js.org/)

好的，请提供需要总结的文本内容，我会按照您要求的格式生成概述和带表情符号的要点列表。  

示例格式：  

这里是文章的概述总结，简明扼要地概括核心内容。  

- 🌟 第一个关键点，简洁描述。  
- 📊 第二个关键点，数据或重点信息。  
- 🔍 第三个关键点，分析或细节补充。  

请提供具体文本以便我为您生成内容！

---

### [Jest 30：更快、更精简、更出色 · Jest](https://jestjs.io/blog/2025/06/04/jest-30)

**原文标题**: [Jest 30: Faster, Leaner, Better · Jest](https://jestjs.io/blog/2025/06/04/jest-30)

Jest 30 发布，带来显著的性能提升、内存优化及多项新功能，目标是未来更频繁地发布主要版本以保持框架的领先地位。

- 🚀 **性能与内存优化**：模块解析更快，内存占用更低，实测某大型应用测试速度提升 37%，内存占用减少 77%。  
- ⚠️ **重大变更**：不再支持 Node 14/16/19/21，升级至 jsdom 26，移除部分 `expect` 别名，默认排除不可枚举对象属性。  
- 🛠️ **新工具支持**：自动修复工具 `eslint-plugin-jest`，新增 `.mts`/`.cts` 文件支持，重命名 `--testPathPattern` 为复数形式。  
- 🧹 **全局变量清理**：新增测试文件间全局变量泄漏检测，未来将自动清理以提升性能。  
- 📦 **模块与类型增强**：原生支持 `import.meta` 和 `file://`，TypeScript 配置文件和 `using` 关键字与间谍函数结合使用。  
- 🔍 **新匹配器与功能**：引入 `expect.arrayOf` 数组验证，`test.each` 新增 `%$` 占位符，定时器支持 `advanceTimersToNextFrame`。  
- 🔄 **可配置重试机制**：`jest.retryTimes()` 新增延迟和立即重试选项，提升测试稳定性。  
- 🧪 **实验性 API**：新增 `unstable_unmockModule` 和 `onGenerateMock` 回调，支持动态调整模拟行为。  
- 📝 **文档与序列化改进**：自定义对象序列化控制，异步 `setupFilesAfterEnv` 支持，快照输出更聚焦。  
- 🔮 **未来计划**：精简核心功能，加快发布周期，提高社区参与透明度，解决技术债务。  
- 🙏 **致谢**：感谢众多贡献者，特别是首次参与的新成员，共同推动 Jest 进步。  

（注：已知问题涉及 `jsdom` 兼容性调整，建议查看迁移指南以应对潜在影响。）

---

### [从 v29 到 v30 · Jest](https://jestjs.io/docs/upgrading-to-jest30)

**原文标题**: [From v29 to v30 · Jest](https://jestjs.io/docs/upgrading-to-jest30)

Jest 30 升级指南，主要涵盖兼容性变更、配置更新、测试运行行为变化、快照与输出调整、Mock API 变更及模块与运行时改动。

- 🚨 **兼容性调整**：Jest 30 不再支持 Node 14、16、19 和 21，最低要求 Node 18.x；TypeScript 最低版本需升级至 5.4；`jest-environment-jsdom` 升级至 JSDOM v26，可能影响 DOM 环境行为。

- 🔄 **别名匹配器移除**：所有别名匹配器（如 `toBeCalled`）已移除，需替换为正式名称（如 `toHaveBeenCalled`），ESLint 插件可辅助自动化替换。

- 🧩 **非枚举属性默认排除**：对象匹配器（如 `expect.objectContaining`）默认忽略非枚举属性，可能影响相等性检查。

- 🛠 **配置更新**：新增对 `.mts` 和 `.cts` 文件扩展的支持；CLI 参数 `--testPathPattern` 更名为 `--testPathPatterns`，支持多模式；移除 `jest --init` 命令，改用 `npm init jest@latest`。

- ⚡ **测试运行行为优化**：改进未处理 Promise 拒绝的逻辑，减少误报失败；自定义测试排序器需适配新增的 `globalConfig` 和 `contexts` 参数。

- 📸 **快照与输出改进**：错误序列化包含 `cause` 属性；React 空字符串子元素不再渲染；`ArrayBuffer` 和 `DataView` 输出更易读。

- 🎭 **Mock API 变更**：移除 `jest.genMockFromModule`，改用 `jest.createMockFromModule`；部分 Mock 函数类型（如 `SpyInstance`）被移除，推荐使用 `jest.Spied`。

- 📦 **模块与运行时重构**：内部模块打包为单文件提升性能，禁止深度导入非公开 API；ESM 支持增强，包导出通过 `package.json` 的 `exports` 字段。

- 🌍 **全局模式匹配更新**：升级 `glob` 至 v10，模式语法更严格，需检查自定义配置（如 `testMatch`）的兼容性。

- ✅ **升级建议**：确保环境符合要求，更新配置与测试代码，处理类型错误，并重跑测试以适配变更。

---

### [将用户数据从 Clerk 同步至 Supabase](https://clerk.com/blog/sync-clerk-user-data-to-supabase?utm_source=cooper-press&utm_medium=newsletter&utm_campaign=clerk-supabase-sync&utm_content=06-11-25&dub_id=k0AEApWTbeiQwYRT)

**原文标题**: [Synchronize user data from Clerk to Supabase](https://clerk.com/blog/sync-clerk-user-data-to-supabase?utm_source=cooper-press&utm_medium=newsletter&utm_campaign=clerk-supabase-sync&utm_content=06-11-25&dub_id=k0AEApWTbeiQwYRT)

本文介绍了如何通过 Clerk 的后端 API 和 Webhooks 与 Supabase Functions 同步用户数据到 Supabase 数据库的方法。

- 🔄 使用 Clerk 的后端 API（BAPI）可以实时获取最新的用户数据，确保信息的准确性和即时性。
- ⚡ 通过 Webhooks 和 Supabase Functions，可以在用户数据发生变化时自动同步到 Supabase 数据库，适用于需要本地访问用户数据的场景。
- 📊 同步用户数据有助于进行自定义查询、分析和报告，以及实施依赖于用户属性的行级安全策略。
- 🛠️ 文章提供了一个实际示例，展示了如何在 Next.js 和 Supabase 项目中实现用户数据的同步。
- 🔧 详细步骤包括创建和配置 Supabase Edge Function、设置 Clerk Webhook，并处理不同的事件类型如用户创建和更新。
- 📌 强调了同步方法的优缺点，如异步处理可能带来的延迟和需要额外管理的基础设施。
- 🔗 提供了相关资源的链接，如 GitHub 仓库和文档，方便读者进一步了解和实践。

---

### [Node 与 TypeScript 的终极 ORM](https://orange-orm.io/)

**原文标题**: [The ultimate ORM for Node and Typescript](https://orange-orm.io/)

Orange ORM 是一个为 Node.js、Bun 和 Deno 设计的终极对象关系映射器（ORM），支持多种流行的数据库，并兼容 TypeScript 和 JavaScript（包括 CommonJS 和 ECMAScript）。

- 🚀 **丰富的查询模型**：提供强大且直观的查询模型，便于从数据库中检索、过滤和操作数据。
- 📝 **Active Record 模式**：通过简洁和表达性强的语法，使用 Active Record 模式与数据库交互。
- 🛠️ **无需代码生成**：享受完整的 IntelliSense，即使在表映射中也不需要繁琐的代码生成。
- 🌐 **TypeScript 和 JavaScript 支持**：完全支持 TypeScript 和 JavaScript，允许利用静态类型和现代 ECMAScript 特性的优势。
- 🖥️ **浏览器中使用**：通过 Express.js 插件安全地在浏览器中使用 Orange，保护敏感数据库凭证免受客户端暴露和 SQL 注入攻击。
- 📊 **支持的数据库和运行时**：包括 Node、Deno、Bun、Cloudflare、Web、Postgres、PGlite、MS SQL、MySQL、Oracle、SAP ASE、SQLite 和 Cloudflare D1。
- 💖 **赞助**：如果认可 Orange 的辛勤工作并希望看到它进一步发展，可以考虑赞助。
- 📥 **安装**：通过 npm 安装 `orange-orm`。
- 📹 **示例**：提供详细的示例代码和教程视频，展示如何使用 Orange ORM 进行数据操作。
- 🔄 **冲突解决**：支持乐观、覆盖和跳过冲突三种并发策略。
- 🗑️ **删除行**：支持级联删除，确保数据完整性。
- 🔒 **安全性**：通过拦截器和基础过滤器增强安全性，确保用户只能访问其授权级别的数据。
- 📝 **日志记录**：通过监听查询事件，记录 SQL 语句和相关参数，便于调试和确保数据完整性。
- 🚫 **不支持的功能**：不支持迁移、NoSQL 数据库和 GraphQL。

---

### [Vue 设备](https://www.vue.equipment/)

**原文标题**: [Vue Equipment](https://www.vue.equipment/)

Vue Equipment 是一个免费开源的前端工具包，提供了一系列即用型插件和组合式函数，用于构建现代 Web 应用程序。它采用无样式设计，完全类型化，并具有灵活而又有明确导向的 API。

- 🛠️ 提供即用型插件和组合式函数，用于构建现代 Web 应用  
- 🎨 无样式设计，完全类型化，API 灵活且有明确导向  
- 📦 开源工具包，免费使用  
- 🔗 支持通过 GitHub 查看项目  
- ⚖️ 采用 MIT 许可证发布  
- 📜 包含法律声明、隐私政策等文档  
- ©️ 版权归属至 2025 年

---

### [简介 | Vue 设备](https://www.vue.equipment/overview/introduction.html)

**原文标题**: [Introduction | Vue Equipment](https://www.vue.equipment/overview/introduction.html)

Vue Equipment 是一个免费开源的前端工具包，提供了一系列即插即用的插件和组合式函数，用于构建现代 Web 应用。它采用无样式设计，具有灵活且规范的 API，支持 Vue 和 Nuxt，并完全类型化。

- 🛠️ **工具包特性**：Vue Equipment 提供无样式、类型化的插件和组合式函数，兼容 Vue 和 Nuxt。  
- 🎯 **开发愿景**：旨在填补 Vue 生态系统的空白，减少重复造轮子，追赶 React 生态的成熟工具。  
- 🏗️ **架构设计**：  
  - 非组件库，专注于降低 Web 应用的开发复杂度。  
  - 关键 CSS 通过变量暴露，支持自定义覆盖。  
  - 选项集中通过 `option` 属性管理，简化模板代码。  
  - 提供组合式函数与注入键，支持深度定制。  
- 💡 **灵感来源**：借鉴了 React 生态的 Sonner、Vaul、Radix 等优秀项目。  
- 🤝 **社区贡献**：鼓励用户提出插件创意或参与开发，未来计划进一步扩展功能。

---

### [GitHub - Assortment/darkmodejs：网页暗色模式管理工具包](https://github.com/Assortment/darkmodejs)

**原文标题**: [GitHub - Assortment/darkmodejs: Utility package for managing Dark Mode on the web](https://github.com/Assortment/darkmodejs)

darkmodejs 是一个用于管理网页暗色模式的实用工具包，支持通过操作系统偏好自动切换主题，并提供灵活的 API 配置和清理功能。

- 🌐 **功能概述**：利用 `matchMedia` API 和 `prefers-color-scheme` 媒体查询，监听并响应系统暗色/亮色主题切换。  
- 📱 **兼容性**：需操作系统支持（如 macOS 10.14+、Windows 10 等）和浏览器支持 `prefers-color-scheme`（详见 caniuse）。  
- ⚠️ **版本注意**：v2+ 弃用旧版 `addListener/removeListener`，改用 `addEventListener/removeEventListener`。  
- 📦 **安装**：通过 npm 安装 `@assortment/darkmodejs`，支持 ES6 `import` 或 ES5 `require`。  
- 🛠️ **API 配置**：  
  - 提供 `onChange(activeTheme, themes)` 回调函数，返回当前主题（`dark`/`light`/`no-preference`/`no-support`）。  
  - 支持 `removeListeners()` 清理监听器，适用于动态路由或组件卸载场景。  
- 🎨 **示例应用**：结合 Emotion Theming 实现主题切换，[Demo 链接](https://darkmodejs-demo.netlify.com/)。  
- 📜 **许可证**：MIT 开源协议，作者 Luke Whitehouse。  
- 🔍 **附加信息**：仓库含 413 Stars、10 Forks，代码 100% JavaScript。

---

### [奥迪克.js](https://odyc.dev/)

**原文标题**: [Odyc.js](https://odyc.dev/)

Odyc.js 是一个小型 JavaScript 库，旨在让用户无需编程经验也能轻松编写视频游戏。  

- 🎮 **创建游戏**：无需编程基础，即可使用该库开发视频游戏。  
- 📚 **学习**：提供学习资源，帮助用户快速上手并掌握游戏开发技巧。  
- 🖼️ **作品展示**：包含游戏画廊，展示其他用户创作的作品以供参考和灵感。

---

### [游乐场 • Odyc.js](https://odyc.dev/playground)

**原文标题**: [Playground • Odyc.js](https://odyc.dev/playground)

Odyc.js 是一个交互式工具，提供多种功能，包括代码编辑、屏幕录制、截图和声音操作等。

- 🔍 **搜索功能** - 支持快速搜索（ctrl K）  
- 📄 **文档与编辑** - 提供文档查看、代码格式化（ctrl ⇧ F）和刷新（ctrl ⇧ R）  
- 🎨 **画布操作** - 包括绘制、镜像、旋转和调整画布大小（Width 8 / Height 8）  
- 📋 **剪贴板管理** - 支持复制、粘贴和从剪贴板加载内容  
- 🔊 **音效选项** - 内置多种音效如激光（LASER）、爆炸（EXPLOSION）等  
- ⚙️ **设置与保存** - 可本地保存（ctrl S）、打开文件（ctrl ⇧ O）和下载内容（ctrl ⇧ E）  
- 🎥 **屏幕录制** - 支持录屏和截图功能  
- 🕹️ **其他功能** - 包括 Vim 模式、自动刷新和自动保存等

---

### [GitHub - web-infra-dev/midscene：面向Web、安卓、自动化与测试的AI操作员](https://github.com/web-infra-dev/midscene)

**原文标题**: [GitHub - web-infra-dev/midscene: Your AI Operator for Web, Android, Automation & Testing.](https://github.com/web-infra-dev/midscene)

Midscene.js 是一个面向 Web 和 Android 的 AI 驱动自动化测试与操作工具，支持自然语言编写脚本，提供可视化调试和多种模型选择。

- 🚀 **核心功能**：支持 Web 和 Android 自动化（Puppeteer/Playwright/ADB），提供自然语言编写脚本和 JavaScript/YAML 支持。  
- 🛠️ **工具特色**：可视化调试报告、缓存加速回放、MCP 多客户端协作能力。  
- 🤖 **AI 集成**：支持多模态模型（如 GPT-4O、Qwen2.5-VL）和视觉语言模型，推荐用于 UI 自动化。  
- 📱 **零代码体验**：通过 Chrome 扩展或 Android Playground 快速上手。  
- 🔄 **两种模式**：自动规划（AI 全流程）或工作流风格（分步控制，稳定性更高）。  
- 🌟 **优势对比**：强调调试体验（可视化报告/Playground）、开源免费、JavaScript 深度集成。  
- 📚 **资源**：提供官网文档、API 参考和 GitHub 仓库，社区支持 Discord/X/飞书群。  
- 📜 **开源协议**：MIT 许可，可自由部署，模型与云服务解耦。  
- 🙏 **致谢**：依赖 Rsbuild、UI-TARS、Qwen2.5-VL 等开源项目。

---

### [GitHub - acornjs/acorn: 一个小巧、快速、基于 JavaScript 的 JavaScript 解析器](https://github.com/acornjs/acorn)

**原文标题**: [GitHub - acornjs/acorn: A small, fast, JavaScript-based JavaScript parser](https://github.com/acornjs/acorn)

Acorn 是一个小型、快速的基于 JavaScript 的 JavaScript 解析器，支持插件扩展，拥有活跃的开源社区。

- 🌟 项目特点：小型、快速，完全用 JavaScript 编写的 JavaScript 解析器  
- 📜 许可证：MIT 开源许可证  
- 🔧 主要包：acorn（主解析器）、acorn-loose（容错解析器）、acorn-walk（语法树遍历器）  
- 🛠️ 插件支持：允许通过插件扩展解析器功能，支持自定义语法和解析逻辑  
- 📦 插件示例：如 acorn-jsx 和 acorn-bigint，可通过 Parser.extend 组合使用  
- 📊 社区活跃：11k stars，934 forks，125+ 贡献者  
- 🌍 使用广泛：被 35.5m+ 项目使用

---

### [GitHub - xojs/xo: ❤️ 拥有出色默认配置的 JavaScript/TypeScript 代码检查工具（ESLint 封装）](https://github.com/xojs/xo)

**原文标题**: [GitHub - xojs/xo: ❤️ JavaScript/TypeScript linter (ESLint wrapper) with great defaults](https://github.com/xojs/xo)

XO 是一个基于 ESLint 的 JavaScript/TypeScript 代码检查工具，提供了一套开箱即用的默认规则，旨在简化代码风格的统一和优化开发流程。

- 🚀 **核心功能**: XO 是一个 ESLint 封装工具，内置了大量有用的插件（如 unicorn、import、ava 等），支持 TypeScript 和 React，并提供自动修复功能（`--fix`）。
- ⚙️ **零配置但可定制**: 默认无需配置即可使用，但也支持通过 `xo.config.js` 文件进行个性化设置（如缩进、分号等）。
- 📦 **安装简单**: 通过 `npm install xo --save-dev` 安装，或直接使用 `npx xo` 运行。
- ✨ **默认代码风格**: 使用制表符缩进（可配置为空格）、分号、单引号等，规则严格但可覆盖。
- 🔧 **工作流推荐**: 建议通过 `npm init xo` 初始化项目，并集成到测试流程中。
- 📂 **文件处理**: 自动检查所有 JS/TS 文件（默认忽略常见路径如 `.gitignore`），支持通过 `ignores` 配置覆盖。
- 🌟 **高级特性**: 支持 Prettier 集成（格式化或兼容模式）、编辑器插件、Monorepo 配置等。
- ❓ **常见问题**: 解释了与 Standard 和 ESLint 的差异，强调 XO 的灵活性和易用性。
- 📛 **徽章与团队**: 提供项目徽章，核心团队包括 Sindre Sorhus 等知名开发者，采用 MIT 许可证。

---

### [GitHub - mochajs/mocha: ☕️ 简单、灵活、有趣的 JavaScript 测试框架，适用于 Node.js 和浏览器](https://github.com/mochajs/mocha)

**原文标题**: [GitHub - mochajs/mocha: ☕️ simple, flexible, fun javascript test framework for node.js & the browser](https://github.com/mochajs/mocha)

Mocha 是一个简单、灵活且有趣的 JavaScript 测试框架，适用于 Node.js 和浏览器环境。它是一个独立的开源项目，由志愿者维护，并且在 npm 上是最受欢迎的模块之一。

- ☕️ Mocha 是一个 JavaScript 测试框架，适用于 Node.js 和浏览器环境。  
- 🏷️ 项目采用 MIT 许可证，由 OpenJS Foundation 和贡献者维护。  
- 🌟 在 GitHub 上拥有 22.8k 星标和 3k 分叉，显示出其广泛的使用和社区支持。  
- 🔧 提供丰富的功能，包括简单、灵活的测试编写方式，支持 TDD 和 BDD。  
- 📚 提供详细的文档、发布说明、行为准则和贡献指南。  
- 💬 社区活跃，有 Discord 频道供开发者交流和提问。  
- 🤝 鼓励赞助和贡献，支持项目维护和新功能开发。  
- 🐞 提供问题跟踪和开发指南，帮助新贡献者参与项目。  
- 📊 被超过 270 万个项目使用，显示出其在 JavaScript 生态系统中的重要性。

---

### [GitHub - lindell/JsBarcode: 适用于浏览器和 Node.js 的 JavaScript 条码生成库](https://github.com/lindell/JsBarcode)

**原文标题**: [GitHub - lindell/JsBarcode: Barcode generation library written in JavaScript that works in both the browser and on Node.js](https://github.com/lindell/JsBarcode)

JsBarcode 是一个用 JavaScript 编写的条形码生成库，支持多种条形码格式，适用于浏览器和 Node.js 环境。

- 📦 **无依赖**：在浏览器中使用时无需依赖，但支持与 jQuery 配合使用。
- 🏷 **支持的条形码格式**：包括 CODE128、EAN、UPC、CODE39、ITF、MSI、Pharmacode、Codabar 和 CODE93 等。
- 🖥 **浏览器示例**：通过简单的代码即可生成条形码，支持 SVG、Canvas 或 Image 元素。
- ⚙️ **灵活配置**：提供多种选项，如条形码格式、颜色、尺寸、文本显示等。
- 📱 **Node.js 支持**：可通过 Canvas 或 SVG 生成条形码。
- 📂 **多种安装方式**：支持通过 CDN、Bower 或 npm 安装。
- 📜 **开源许可**：采用 MIT 许可证，允许自由使用和修改。
- 🤝 **社区支持**：欢迎贡献和反馈，提供详细的贡献指南和讨论渠道。
- 🌟 **活跃项目**：拥有 5.7k 星标和 1.1k 分支，被 24.3k+ 项目使用。

---

### [未找到标题](https://infinitcode.ai/)

**原文标题**: [No title found](https://infinitcode.ai/)

overview summary  
这是一个关于 AI 代码审查工具的网页内容，展示了实时分析、多语言支持、自定义规则等功能，并强调与 GitHub 生态系统的无缝集成、企业级安全性和团队协作优势。  

- 🏠 **主页** - 提供产品的主要入口和核心功能介绍。  
- 🚀 **功能亮点** - 实时分析、多语言支持、自定义规则和团队协作。  
- 🤖 **AI 实时审查** - 通过可视化界面展示代码审查结果，包括安全、性能优化建议（如 2.8 秒内完成分析）。  
- 🔒 **GitHub 集成** - 原生支持 GitHub 工作流，提供 PR 分析、安全扫描和零代码存储的临时处理。  
- 🔧 **多模型选项** - 支持不同编程任务的多种 AI 模型选择。  
- 🛡️ **企业级安全** - 256 位加密和安全连接确保数据隐私。  
- 📧 **联系与试用** - 提供用户联系表单和免费试用入口（Try Alpha）。  
- 📜 **页脚信息** - 包含公司、社区、法律条款及社交媒体链接。

---

### [JavaScript 条码扫描库](https://strich.io/?ref=js-weekly)

**原文标题**: [JavaScript Barcode Scanning Library](https://strich.io/?ref=js-weekly)

STRICH 是一个用于网页应用的 JavaScript 库，支持实时 1D/2D 条形码扫描，无需原生应用或后端支持。它提供简单透明的定价、丰富的文档和多种集成选项，适用于多个行业和场景。

- 🚀 **产品功能**  
  - 支持 1D/2D 条形码扫描，包括 Code 128、EAN、QR Code 等。  
  - 内置扫描 UI，支持相机选择、闪光灯和点击对焦。  
  - 提供弹出式扫描器，集成简单。  

- 💻 **开发者友好**  
  - 零依赖，支持所有主流框架（Angular/Vue/React 等）。  
  - 提供 TypeScript 绑定和详细文档。  
  - 支持离线模式，确保数据安全。  

- 💰 **定价透明**  
  - BASIC：$99/月（10k 次扫描）。  
  - PROFESSIONAL：$249/月（100k 次扫描）。  
  - ENTERPRISE：定制方案，支持无限扫描和白标功能。  

- 🌍 **行业应用**  
  - 公共图书馆、零售、医疗物流等多个行业成功案例。  
  - 客户评价高，强调易集成、高性能和优质支持。  

- 🔍 **技术优势**  
  - 基于 WebAssembly 和 WebGL，速度快且兼容性强。  
  - 支持复杂场景（如模糊、低光、反色条码）。  
  - 完全在设备端处理，数据不外传。  

- ❓ **常见问题**  
  - 免费试用 30 天，超出扫描限制可升级计划。  
  - 支持 GS1 标准，适合企业需求。  
  - 与免费方案（如 ZXing）相比，提供更稳定的维护和支持。  

- 🎯 **网页应用优势**  
  - 无需应用商店审核，分发便捷。  
  - 降低开发成本，支持 PWA 离线功能。  
  - 避免用户安装冗余应用。  

- 📌 **试用与支持**  
  - 提供演示应用和免费试用，可快速集成。  
  - 支持邮件/帮助中心，企业客户可定制方案。

---

### [一丝不苟](https://www.meticulous.ai?utm_source=javascript_weekly&utm_campaign=june13th2025)

**原文标题**: [Meticulous](https://www.meticulous.ai?utm_source=javascript_weekly&utm_campaign=june13th2025)

Meticulous AI 提供了一种无需编写和维护测试的自动化测试解决方案，通过记录用户交互并生成持续演化的测试套件，覆盖应用程序的所有边缘情况。

- 🚀 **无需编写测试** - 自动生成并维护测试套件，覆盖所有用户流程和边缘情况。  
- 🔍 **记录用户交互** - 在开发、预发布和生产环境中记录会话，生成全面的测试覆盖。  
- 🤖 **AI 驱动测试** - 通过分析代码分支和用户交互，动态生成和更新测试用例。  
- ⚡ **快速反馈** - 在合并代码前查看 PR 对用户流程的影响，避免回归问题。  
- 🛠️ **零维护** - 测试自动随应用程序演化，无需手动更新或修复。  
- 🚫 **无 flakes** - 基于 Chromium 的确定性调度引擎，消除测试中的不稳定因素。  
- ⏱️ **高速并行测试** - 支持大规模并行测试，数千次测试可在 120 秒内完成。  
- 🔗 **无缝集成** - 支持多种前端框架（如 React、Vue、Angular 等），并可与其他测试工具共存或替换。  
- 📈 **客户认可** - 被 Dropbox、Lattice 等 100 多家组织信任，显著提升开发效率和代码质量。  
- 📥 **快速上手** - 通过添加简单的脚本标签，几分钟内即可开始使用。

---

### [错误](https://javascriptweekly.com/link/170460/web)

**原文标题**: [Error](https://javascriptweekly.com/link/170460/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='javascriptweekly.com', port=443): Max retries exceeded with url: /link/170460/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [错误](https://javascriptweekly.com/link/170474/web)

**原文标题**: [Error](https://javascriptweekly.com/link/170474/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='javascriptweekly.com', port=443): Max retries exceeded with url: /link/170474/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [错误](https://javascriptweekly.com/link/170475/web)

**原文标题**: [Error](https://javascriptweekly.com/link/170475/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='javascriptweekly.com', port=443): Max retries exceeded with url: /link/170475/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [错误](https://javascriptweekly.com/link/170479/web)

**原文标题**: [Error](https://javascriptweekly.com/link/170479/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='javascriptweekly.com', port=443): Max retries exceeded with url: /link/170479/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

### [错误](https://javascriptweekly.com/link/170476/web)

**原文标题**: [Error](https://javascriptweekly.com/link/170476/web)

无法总结：获取内容时出错 - HTTPSConnectionPool(host='javascriptweekly.com', port=443): Max retries exceeded with url: /link/170476/web (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

---

