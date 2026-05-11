### [发布 · tailwindlabs/tailwindcss · GitHub](https://github.com/tailwindlabs/tailwindcss/releases?ref=tailwindweekly.com)

**原文标题**: [Releases · tailwindlabs/tailwindcss · GitHub](https://github.com/tailwindlabs/tailwindcss/releases?ref=tailwindweekly.com)

Tailwind CSS v4.3.0 版本发布，新增多项实用工具和功能，并修复了多个问题。

- 🎉 **v4.3.0 新增多项实用工具**：包括 `@container-size`、`scrollbar-*`、`zoom-*`、`tab-*` 等，并支持 `@variant` 堆叠和复合变体
- 🛠️ **v4.2.4 修复 Vite 别名导入问题**：确保 `@import` 和 `@plugin` 在使用 Vite 别名时能正确解析
- 🔧 **v4.2.3 大量规范化改进**：优化 `tracking-*`、`border-*`、`scroll-*` 等工具的规范化，并修复升级过程中的文件清空问题
- 🚀 **v4.2.2 支持 Vite 8 并修复崩溃**：新增对 Vite 8 的支持，修复候选值包含原型属性时的崩溃问题
- 🐛 **v4.2.1 修复兼容性问题**：允许功能工具名称末尾带破折号，并正确检测 MDX 文件中包含 `.` 字符的类
- 🌈 **v4.2.0 新增颜色调色板和逻辑属性**：添加 mauve、olive、mist、taupe 颜色，以及 `pbs-*`、`mbs-*`、`inline-*` 等逻辑属性工具
- ⚡ **v4.1.18 改进验证和规范化**：确保 `source()` 验证相对于文件路径，支持环境 API，并改进 JS 配置的向后兼容性
- 🧹 **v3.4.19 修复 `calc()` 中的 `sibling-*()` 函数**：确保在 `calc()` 内使用时不中断
- 🪟 **v4.1.17 修复 Windows 工作线程崩溃**：防止在 Windows 上加载到工作线程时偶尔崩溃
- 🎯 **v4.1.16 修复空数据类型和规范化问题**：丢弃空数据类型的候选值，修复任意变体的规范化和颜色问题

---

### [发布 · maizzle/framework · GitHub](https://github.com/maizzle/framework/releases?ref=tailwindweekly.com)

**原文标题**: [Releases · maizzle/framework · GitHub](https://github.com/maizzle/framework/releases?ref=tailwindweekly.com)

Maizzle 框架 v6.0.0 发布了一系列候选版本，引入了大量新功能、重构和破坏性变更，旨在提升开发体验和邮件模板的构建效率。

- 🚀 **核心功能增强**：CSS 内联和清除、简写 CSS 及 HTML 美化默认开启，并新增了 `useTransformers()` 组合式函数，允许在单个模板中精细控制这些转换流程。
- ✨ **新组件与属性**：新增了 `<Tailwind>`、`<Raw>`、`<Font>` 组件，以及 `<Button>`、`<Container>` 等组件的 `outlookFallback`、`msoStyle` 等新属性，增强了组件灵活性和 Outlook 兼容性。
- 🛠️ **开发体验优化**：引入了暗黑模式模拟器、设备尺寸输入框、跳转到编辑器功能，并改进了命令面板（支持目录名搜索、顺序无关的令牌搜索、显示结果计数）。
- 📝 **Markdown 模板支持**：`.md` 模板现在自动包裹在 `MarkdownLayout` 中，并支持通过 frontmatter 指定自定义布局，简化了 Markdown 邮件的创建。
- 🔧 **配置与 API 重构**：`build()` API 选项被扁平化，`<Divider>` 重命名为 `<Hr>`，并新增了 `maizzle prepare` 脚本以在编辑器中提供类型定义。
- 🐛 **问题修复**：修复了 `useEvent()` 在 `.vue` 和 `.md` 模板中不触发、`useTransformers()` 覆盖全局默认值、以及 `pnpm` 下的组件自动导入等问题。

---

### [LookAway - 智能屏幕休息、眨眼与坐姿提醒工具（Mac 版）](https://lookaway.com/?via=vivian&ref=tailwindweekly.com)

**原文标题**: [LookAway - Smart Screen Breaks, Blink & Posture Reminders for Mac](https://lookaway.com/?via=vivian&ref=tailwindweekly.com)

LookAway 2.0 是一款专为 Mac 设计的健康应用，通过智能休息提醒、姿势矫正和眨眼提醒，帮助用户减少眼疲劳和屏幕疲劳，同时保持工作流畅。

- 👀 智能休息提醒：在合适时机弹出休息提示，并提供提前通知和暂停选项，不打断工作流。
- 🧘 姿势与眨眼提醒：温和提醒用户保持正确姿势和眨眼频率，促进健康屏幕习惯。
- 🎨 可定制体验：支持自定义计时器、声音、背景和消息，适应个人工作风格。
- 📱 多设备同步：休息时自动同步到 iPhone/iPad，确保跨屏幕休息不间断。
- ⚙️ 智能自动化：集成 AppleScript 和 Shortcuts，实现休息与工作流程的自动衔接。
- 💻 原生 Mac 设计：支持全局快捷键、Focus Filters 和外观自适应，体验流畅。
- 🗣️ 用户好评：多位用户反馈有效缓解头痛、眼疲劳，并改善工作效率和健康习惯。
- 🔄 最新更新：2.1 版新增网站使用统计和每次会话暂停限制；2.0 版引入屏幕评分、动态背景等功能。
- 🛒 多平台获取：支持直接下载、Homebrew 安装，以及 Setapp 订阅免费使用。

---

### [合成与混合 • 尼克拉斯·加德曼](https://nik.digital/posts/compositing-blending?ref=tailwindweekly.com)

**原文标题**: [Compositing & Blending • Niklas Gadermann](https://nik.digital/posts/compositing-blending?ref=tailwindweekly.com)

以下是您提供的文章摘要：

本文深入探讨了浏览器中合成与混合的数学原理和实际应用，涵盖了从基础概念到高级技巧的全面内容。

- 🖥️ **浏览器合成基础**：浏览器通过将多个图层叠加并逐像素计算来显示网页，合成是将元素与其背景结合的过程，分为源图层和背景图层。
- 🧩 **Porter-Duff 合成算子**：定义了 12 种合成操作，通过调整源和背景的贡献因子（Fₛ和 Fb），控制重叠区域的像素显示方式，如“源在上”、“背景在上”等。
- 🎨 **混合模式原理**：混合发生在源与背景重叠区域，通过混合函数 B(Cb, Cs) 改变颜色，分为可分离（逐通道处理 RGB）和不可分离（基于色相、饱和度、亮度）两类。
- 📊 **混合模式分类**：包括变亮（lighten、screen、color-dodge）、变暗（darken、multiply、color-burn）、对比（overlay、hard-light、soft-light）、反转（difference、exclusion）及组件模式（hue、saturation、color、luminosity）。
- 🛠️ **浏览器中的使用**：通过 CSS 属性`mix-blend-mode`（元素混合）和`background-blend-mode`（背景混合）应用，支持 16 种标准混合模式及新增的`plus-lighter`。
- ⚠️ **色彩空间问题**：混合计算在显示器的色彩空间（如 Display P3）中进行，可能导致 sRGB 颜色转换后结果异常（如红绿混合变棕），可通过直接指定 P3 颜色解决。
- 🔒 **隔离与堆叠上下文**：使用`isolation: isolate`创建新堆叠上下文，限制混合范围，避免元素与无关背景混合（如维恩图示例）。
- 💡 **实际应用案例**：包括图像文字叠加（overlay 模式）、双色调图像效果、不规则形状边框（lighten 模式消除重叠暗边）、以及结合滤镜的模糊对比效果（如黑色斑点叠加颜色）。

---

### [内联关键 CSS：它能让你的网站更快吗？| DebugBear](https://www.debugbear.com/blog/critical-css?ref=tailwindweekly.com)

**原文标题**: [Inlining Critical CSS: Does It Make Your Website Faster? | DebugBear](https://www.debugbear.com/blog/critical-css?ref=tailwindweekly.com)

本文讨论了内联关键 CSS 对网站速度的影响，包括其优势、实现方法和潜在缺点。

- 📄 **关键 CSS 的作用**：内联关键 CSS 可消除渲染阻塞，使页面在 HTML 加载后立即显示内容，提升加载速度。
- 🛠️ **生成关键 CSS 的工具**：可使用 penthouse 等工具，根据视口大小识别必要的样式规则，但需在网站更新后重新生成。
- ⚡ **延迟加载完整样式表**：通过`<link rel="preload">`标签非阻塞加载完整 CSS，并在加载后通过`onload`事件应用样式。
- ⚠️ **内联 CSS 的缺点**：增加 HTML 文件大小、无法缓存重复使用，可能导致后续页面加载变慢，并存在样式遗漏风险。
- 🔍 **优先检查其他瓶颈**：若存在渲染阻塞的 JavaScript 或跨域 CSS 加载问题，内联 CSS 可能不是最有效的优化。
- 📊 **衡量优化效果**：使用性能监测工具（如 DebugBear）定期测试，确保优化真正提升页面速度。

---

### [让您的网站对 LLM 可见：6 种有效技巧与 8 种无效方法——火星编年史，邪恶火星人团队博客](https://evilmartians.com/chronicles/how-to-make-your-website-visible-to-llms?ref=tailwindweekly.com)

**原文标题**: [Making your site visible to LLMs: 6 techniques that work, 8 that don't—Martian Chronicles, Evil Martians’ team blog](https://evilmartians.com/chronicles/how-to-make-your-website-visible-to-llms?ref=tailwindweekly.com)

本文章介绍了 6 种有效的技术和 8 种无效的技术，帮助网站提高对 LLM（大语言模型）的可见性。核心思路是提供干净、结构良好的 Markdown 内容，并通过多种方式让 AI 系统发现这些内容。

- 📝 **/llms.txt**：在网站根目录创建 Markdown 文件，作为 AI 系统的内容地图，列出最重要的页面链接。这是最简单且推荐优先实施的技术。
- 📄 **.md 路由**：为每个页面提供干净的 Markdown 版本（如`example.com/page.md`），减少 HTML 中的噪音，让 LLM 更易理解内容。
- 🔗 **`<link>`标签和 HTTP `Link`头**：在 HTML 头部和 HTTP 响应头中声明 Markdown 版本的链接，帮助 AI 爬虫和工具发现内容。
- 🕵️ **隐藏`<div>`提示**：在页面中添加对用户不可见但存在于 DOM 中的提示，引导 LLM 找到 Markdown 版本，适用于用户粘贴 URL 到 AI 工具的场景。
- 📚 **/llms-full.txt**：提供网站全部内容的完整 Markdown 文件，适合文档类网站，让 AI 一次性获取所有信息。
- 🔄 **Accept: text/markdown内容协商**：基于 HTTP 标准，让客户端请求 Markdown 格式，服务器根据请求头返回相应内容，是未来最可能成为标准的技术。
- ❌ **无效技术**：包括`<meta name="ai-content-url">`、`<meta name="llms">`、`/.well-known/ai.txt`、HTML 注释、人/AI 切换按钮、User-Agent 嗅探、专用“AI 信息页”以及 Schema.org/JSON-LD，这些方法缺乏证据或已被证明无效。
- 📊 **测量与监控**：通过服务器端日志跟踪 Markdown 端点的访问情况，区分 AI 爬虫和人类请求，以评估技术效果。

---

### [Featurebase – 现代化支持与反馈平台](https://www.featurebase.app/?ref=tailwindweekly.com)

**原文标题**: [Featurebase – Modern Support & Feedback Platform](https://www.featurebase.app/?ref=tailwindweekly.com)

Featurebase 是一个集 AI 客服、用户反馈收集和产品更新公告于一体的现代化客户支持与反馈平台。

- 🤖 **AI 驱动客服**：通过 AI 客服代理（Fibi）自动解决客户问题，降低团队支持负担，并整合多渠道收件箱（应用内、Slack、Discord、邮件等）。
- 💡 **集中化反馈管理**：提供反馈门户、应用内小组件和集成功能，让用户投票和查看公开路线图，并通过 AI 优先排序最有影响力的产品机会。
- 📚 **智能帮助中心**：AI 原生搜索栏可快速提供即时答案，支持多品牌、多语言（40+ 语言），并拥有类似 Notion 的强大编辑器。
- 🚀 **产品更新日志**：通过独立页面、应用内小组件和用户属性分段，轻松发布更新并驱动用户参与。
- 🔗 **跨团队协作**：支持支持团队、产品团队和 GTM 团队共享数据，自动将反馈与客户信息关联，提升效率。
- 🌐 **集成与安全**：与多种工具快速集成，并具备 SOC 2、GDPR、CCPA 等安全认证，支持高扩展性（99.9% 正常运行时间）。

---

### [Tailwind | JOYCO 中心](https://hub.joyco.studio/toolbox/tailwind?ref=tailwindweekly.com)

**原文标题**: [Tailwind | JOYCO Hub](https://hub.joyco.studio/toolbox/tailwind?ref=tailwindweekly.com)

### 概述总结
Tailwind CSS 工具集，提供多种实用变体和自定义配置方法。

- 🛠️ **hocus 变体**：组合 `hover` 和 `focus-visible`，通过 `@custom-variant hocus (&:is(:hover, :focus-visible))` 实现悬停或聚焦时的样式统一。
- 📏 **字体行高配置**：在 `@theme` 中为每个字号设置独立行高，例如 `--text-tiny` 搭配 `--text-tiny--line-height`。
- 🧩 **祖先状态样式**：使用 `in-*` 变体，根据祖先元素的类或状态（如 `.notifs-drawer-open`）来条件化子元素样式。
- 🖱️ **指针类型检测**：通过 `@variant has-mouse` 和 `@variant has-touch-screen` 区分鼠标（`pointer: fine`）与触屏（`pointer: coarse`），调整元素尺寸。
- 🎯 **Slot 变体**：利用 `matchVariant` 创建 `slot-*` 变体，通过 `data-slot` 属性直接为子元素设置样式，避免嵌套选择器。

---

### [WindyBase - 探索免费和高级的 Tailwind CSS 模板](https://windybase.com/?ref=tailwindweekly.com)

**原文标题**: [WindyBase - Explore free and premium Tailwind CSS templates ](https://windybase.com/?ref=tailwindweekly.com)

WindyBase 是一个每周精选的 Tailwind CSS 模板与工具目录，旨在帮助开发者快速构建现代网站和应用。

- 🧩 提供丰富的模板分类：包括落地页、SaaS、博客、仪表盘、电商等模板
- 🆓 包含免费与付费资源：从免费模板到 $249 的专业组件库，满足不同预算需求
- 🔍 支持搜索功能：方便开发者快速查找所需的模板或组件
- 🛒 模板可直接购买：每个模板均提供预览和购买链接，价格从 $14 到 $249 不等
- 📧 提供订阅服务：用户可订阅新闻邮件，及时获取新模板和组件更新
- 🎯 聚焦 Tailwind CSS：所有资源均围绕 Tailwind CSS 生态，专为现代开发者设计
- 📄 包含法律条款：网站设有隐私政策和条款与条件，保障用户权益

---

### [1Panel：开源 VPS 控制面板 | cPanel 替代方案](https://1panel.pro/?ref=tailwindweekly.com)

**原文标题**: [1Panel: Open-Source VPS Control Panel | cPanel Alternative](https://1panel.pro/?ref=tailwindweekly.com)

1Panel 是一个现代化的开源 VPS 控制面板，专为 AI 时代设计，提供全面的服务器管理功能，支持一键部署 AI 代理、管理 Docker 容器和网站托管，拥有丰富的应用商店，并确保数据安全可靠。

- 🤖 **AI 集成**：一键部署 OpenClaw 代理、通过 Ollama 管理本地 LLM，并监控 GPU 使用情况。
- 🛠️ **高效管理**：通过 Web 界面轻松管理 Linux 服务器，包括实时监控、文件管理、数据库和 Docker 管理。
- 🌐 **快速建站**：深度集成 WordPress，支持一键部署、自动 SSL 证书和域名管理。
- 🛍️ **丰富应用商店**：提供 180+ 高质量开源应用，涵盖 AI、网站、数据库、工具等类别，一键安装和更新。
- 🔒 **安全可靠**：提供漏洞防护、病毒扫描、防火墙和日志审计功能，确保系统安全。
- 💾 **数据备份**：支持计划备份到多种云存储，并具备数据恢复功能。
- 🚀 **快速开始**：支持主流 Linux 发行版和多种架构，通过一键脚本即可安装并访问管理面板。

---

### [Unraid | 释放你的硬件潜能](https://unraid.net/?ref=tailwindweekly.com)

**原文标题**: [Unraid | Unleash Your Hardware](https://unraid.net/?ref=tailwindweekly.com)

概述摘要
Unraid 是一款功能强大且易于使用的操作系统，专为自托管服务器和网络附加存储设计，能最大化利用各种硬件资源。

- 🖥️ **灵活存储**：支持混合使用不同大小硬盘，轻松构建和扩展存储容量。
- 🐳 **Docker 应用**：通过简洁界面管理 Docker 应用，可添加社区模板或自定义应用。
- 💻 **虚拟机支持**：可直通显卡进行游戏或视频编辑，实现高速文件访问。
- 👥 **社区驱动**：拥有丰富的指南、视频教程和多语言社区，提供全程支持。
- 🔧 **多样化用途**：从简单存储到游戏服务器托管，适应各种场景。
- 🛒 **实惠定价**：起价仅 49 美元，提供 30 天免费试用。
- 🌟 **用户好评**：用户称赞其稳定性和持续发现新功能的乐趣。

---

### [Nota - 专为本地 Markdown 文件设计的专业笔记应用](https://nota.md/?ref=tailwindweekly.com)

**原文标题**: [Nota - Pro notes app designed for local Markdown files.](https://nota.md/?ref=tailwindweekly.com)

概述总结  
- 📝 专为本地 Markdown 文件设计的笔记应用，支持从简单笔记、待办事项到文章、日记、维基和第二大脑等多种用途，无需账户、订阅或供应商锁定。  
- ✍️ 高效编辑器：提供简洁熟悉的写作体验，编辑工具在不需要时隐形，需要时强大。  
- 🔄 多重选择：可同时进行十处编辑，而非重复操作。  
- 🔍 扩展选择：轻松选择当前元素或其任何父级。  
- 🤖 智能辅助：上下文感知的补全和视觉提示。  
- 📄 纯文本：打开时不重新格式化，复制粘贴无转换。  
- ⚡ 快速对话框：通过模糊匹配加速文件打开、搜索或命令调用，如 Quick Open 显示预览、Go to Heading 跳转标题、Command Palette 运行命令。  
- 🔗 Wiki 链接：支持[[wiki]]语法，自动更新重命名文件的链接，提供快捷键和反向链接功能。  
- 🗂️ 完全数据所有权：笔记为常规 Markdown 文件，可存储在 Dropbox、通过 Finder 管理，并在任何支持纯文本的应用中打开。  
- 🧩 扩展功能：通过简单脚本扩展应用，包括自定义命令、事件钩子、高亮器和补全（部分即将推出）。  
- 🚀 试用信息：提供 macOS 测试版，可通过申请加入等待列表或预购获取。

---

