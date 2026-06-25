### [ui.sh](https://ui.sh/?ref=tailwindweekly.com)

**原文标题**: [ui.sh](https://ui.sh/?ref=tailwindweekly.com)

本内容介绍了一组专为界面构建者设计的 AI 代理技能，旨在帮助用户高效创建不糟糕的用户界面，并提供了多种实用工具。

- 🛠️ **设计代理**：以资深设计师的专业水平构建新 UI。
- 💡 **创意代理**：在浏览器中生成并对比多种设计方向。
- 🎨 **品牌工具包代理**：为新产品创意生成视觉品牌方向。
- 🧩 **组件化代理**：将大型 UI 代码重构为组织良好的可复用组件。
- ✂️ **Tailwind 规范化代理**：排序、标准化、去重并解决 Tailwind CSS 类冲突。
- 🌙 **暗黑模式代理**：实现经过深思熟虑的暗黑模式，而非简单反转。
- 🖼️ **暗黑模式图片代理**：适配亮色模式光栅图像以在暗黑模式下工作。
- 📱 **响应式代理**：使现有设计适配移动端、平板和桌面断点。
- 📄 **图片转标记代理**：将截图、模型和线框图转换为语义化标记。

---

### [Wispr Flow | 轻松语音听写](https://wisprflow.ai/?utm_source=dub.co&utm_medium=affiliate&utm_campaign=AffiliateProgram&via=vivian-guillen&dub_id=MBe1TOcnDvAVflxj&ref=tailwindweekly.com)

**原文标题**: [Wispr Flow | Effortless Voice Dictation](https://wisprflow.ai/?utm_source=dub.co&utm_medium=affiliate&utm_campaign=AffiliateProgram&via=vivian-guillen&dub_id=MBe1TOcnDvAVflxj&ref=tailwindweekly.com)

这是一款名为 Flow 的语音转文字 AI 工具，它能让你在几乎所有应用里通过说话来快速、清晰地输入文字，速度比打字快 4 倍，并支持多种设备和语言。

- 🎤 **核心功能**：只需说话，AI 就能自动将语音转成清晰、无填充词的文字，并支持 100 多种语言。
- ⚡ **速度优势**：输入速度可达 220 词/分钟，比传统键盘打字快 4 倍。
- 💻 **多平台支持**：可在 Mac、Windows、iPhone 和 Android 设备上无缝使用，工作场景同步。
- 🛠️ **智能特性**：拥有个人词典（自动学习专有词汇）和片段库（创建语音快捷方式），提升效率。
- 👥 **场景化应用**：专为团队、学生、开发者、创作者、销售、客服、律师、领导者和有特殊需求人士（如行动不便者）优化。
- 🔒 **安全合规**：支持 HIPAA 合规（所有方案）和 SOC 2 Type II 认证（企业方案），适合专业领域。
- 🎧 **用户反馈**：被用户誉为“改变游戏规则”的工具，能显著提升工作流、减少打字负担，并改善沟通体验。
- 🆓 **免费试用**：提供 14 天免费试用，可在官网下载并开始使用。

---

### [框架无关的设计系统：Web 组件的实用方法 - Piccalilli](https://piccalil.li/blog/framework-agnostic-design-systems-part-1/?ref=tailwindweekly.com)

**原文标题**: [
  Framework-agnostic design systems: a practical approach to web components - Piccalilli
](https://piccalil.li/blog/framework-agnostic-design-systems-part-1/?ref=tailwindweekly.com)

本文介绍了一种基于 Web Components 的框架无关设计系统构建方法，强调使用 Web 标准、渐进增强和文档驱动开发。

- 📦 **项目结构**：采用 monorepo 结构，将组件库（使用 Elena 构建）和文档（使用 VitePress）整合在单一仓库中，便于管理和部署。
- 🧩 **组件原则**：组件应保持原始、简单且尽可能未来-proof，避免框架锁定，直接使用 Web 标准（如自定义元素、Shadow DOM）构建。
- 🛠️ **工具选择**：使用 Elena（轻量级 Web Components 库）处理跨框架兼容性，VitePress 作为文档框架，两者结合实现高效开发。
- 🎨 **样式与主题**：通过 CSS 自定义属性和`@scope`规则实现组件样式封装与主题化，支持变体（如 primary、danger）通过属性选择器轻松扩展。
- 📝 **文档自动化**：利用 JSDoc 注释和 Elena 生成的`custom-elements.json`，自动生成组件属性表、描述等文档内容，减少手动维护。
- 🔄 **开发工作流**：通过`concurrently`同时运行 Elena 的 watch 和 VitePress 的 dev 模式，实现组件修改后文档即时更新。
- 🚀 **可发布性**：组件库可打包为 npm 包（如`@my-ds/components`），文档可部署为静态站点，实现跨项目复用。
- 💡 **扩展建议**：后续可探索设计令牌（tokens）集成、组件测试自动化、以及更复杂的复合组件（如对话框、表单字段）构建。

---

### [优秀动画与卓越动画](https://emilkowal.ski/ui/good-vs-great-animations?ref=tailwindweekly.com)

**原文标题**: [Good vs Great Animations](https://emilkowal.ski/ui/good-vs-great-animations?ref=tailwindweekly.com)

以下是您提供的文章内容摘要：

动画课程报名已开放，但目前已截止。本文由设计工程师 Emil Kowalski 撰写，分享了从“好”动画进阶到“优秀”动画的实用技巧。

- 🎯 **起源感知动画**：元素动画应源于触发位置（如按钮），通过调整 CSS 的`transform-origin`属性（如`bottom center`）实现自然效果。Radix 和 shadcn/ui 可简化此过程。
- ⚙️ **正确缓动曲线**：缓动是动画的核心。移动元素时推荐使用`ease-in-out`曲线（模拟自然加速/减速），日常场景默认用`ease-out`。
- 🎨 **自定义缓动曲线**：CSS 内置曲线通常力度不足，建议使用自定义曲线（如通过 easing.dev 或 easings.co 获取）来增强动画活力，`ease`仅适用于基础悬停效果。
- 🌱 **弹簧式交互**：鼠标位置驱动的 UI 变化应使用 Framer Motion 的`useSpring`钩子，通过弹簧行为插值数值变化，让交互更自然（仅适用于装饰性动画）。
- 🛠️ **精通工具属性**：了解 CSS 属性（如`clip-path`）能优化动画细节，例如实现标签切换时颜色与高亮条的平滑过渡。3D 变换（如`transform`）可创造轨道旋转等创意效果。
- 💡 **动画的战略价值**：当软件功能趋同时，精心设计的动画能让产品脱颖而出，提升用户感知与体验。

---

### [深入探讨 CSS 中的@property 属性](https://utilitybend.com/blog/taking-a-closer-look-at-property-in-css/?ref=tailwindweekly.com)

**原文标题**: [Taking a closer look at @property in CSS | utilitybend](https://utilitybend.com/blog/taking-a-closer-look-at-property-in-css/?ref=tailwindweekly.com)

### 概述摘要
本文深入探讨了 CSS `@property` 规则的技术细节、优势及应用场景，涵盖类型检查、继承控制、动画新可能性等核心内容，并展示了 Chrome DevTools 的调试支持。

- 🔍 **`@property` 规则简介**：作为 CSS Houdini API 的一部分，允许开发者显式定义自定义属性，支持类型约束、默认值设置和继承行为控制。
- 🎨 **类型检查与约束**：通过指定`syntax`（如`<color>`、`<length>`），确保属性值正确，无效值时自动回退到`initial-value`，提升代码健壮性。
- 🛠 **DevTools 调试增强**：Chrome 118+ 可显示类型、继承状态、初始值及错误警告，便于排查自定义属性问题。
- 🔄 **继承行为控制**：`inherits`属性决定子元素是否继承属性值，设为`false`可避免意外覆盖，适合设计系统或 Web 组件。
- ✨ **动画新可能**：`@property`使浏览器能理解自定义属性类型，实现渐变、`clip-path`、`background-image`梯度等原本无法直接动画的效果。
- 🌈 **实际应用示例**：包括色相旋转动画、滚动驱动动画中的`clip-path`渐变、以及`background-image`梯度颜色过渡。
- 📚 **设计系统价值**：类型约束和继承控制简化维护，尤其适合多作者项目或第三方使用场景，减少错误并提升可预测性。

---

### [QuiverAI – 构建矢量设计的未来](https://quiver.ai/?ref=tailwindweekly.com)

**原文标题**: [QuiverAI â Building the Future of Vector Design](https://quiver.ai/?ref=tailwindweekly.com)

概述  
QuiverAI 是一个前沿的矢量图形生成、编辑和动画平台，专为设计师打造，提供从标志到插画再到动画的多种创意工具，并支持开发者通过 API 集成。

- 🎨 **核心功能**：支持文本生成、编辑和动画化矢量图形，提供生产就绪的 SVG 输出  
- ✨ **应用场景**：涵盖标志设计、字体排版、插画创作和动画制作，强调精确控制和创意探索  
- 🚀 **开发者工具**：提供 REST API，包括模型列表、文本转 SVG 和图像转 SVG 等功能，方便集成  
- 📰 **最新动态**：发布 MCP 支持代理工作流、与 Timbal AI 和 Paper 等平台合作，拓展 AI 设计生态  
- 🔧 **产品特色**：由研究人员构建，注重轻量、可控和高质量，适合 UI、营销和产品设计

---

### [ReUI – Shadcn UI 组件与模块](https://reui.io/?ref=tailwindweekly.com)

**原文标题**: [ReUI – Shadcn UI Components and Blocks](https://reui.io/?ref=tailwindweekly.com)

概述摘要
ReUI Pro 是一个基于 shadcn/ui 的 React 和 Tailwind CSS 组件库，提供超过 1003 个免费开源组件，旨在提升开发效率并加速项目交付。目前正在开放 Pro 版本的等待名单，可享受 40% 的发布折扣。

- 🚀 加入等待名单，锁定 40% 的发布折扣，抢先体验 ReUI Pro。
- 🧩 提供 1003+ 免费开源组件，覆盖按钮、数据网格、文件上传等常用类别。
- ⚡ 与 shadcn/ui 深度集成，兼容所有 5 种 Shadcn Create 样式和设置。
- 🔧 支持 Base UI 和 Radix UI 双库版本，灵活适配不同项目需求。
- 💬 社区反馈热烈，用户称赞其节省时间、提升生产力，尤其数据网格和过滤器组件备受好评。
- 📚 包含详细文档和常见问题解答，帮助开发者快速上手。
- 🔔 支持订阅更新，获取最新发布通知。

---

### [WindyBase - 探索免费和高级的 Tailwind CSS 模板](https://windybase.com/?ref=tailwindweekly.com)

**原文标题**: [WindyBase - Explore free and premium Tailwind CSS templates ](https://windybase.com/?ref=tailwindweekly.com)

WindyBase 是一个每周精选的 Tailwind CSS 模板和工具目录，专为现代开发者打造，提供免费和付费资源。

- 🎨 提供多种类别的模板，包括落地页、SaaS、博客、仪表盘和电商模板，价格从免费到 $77 不等。
- 🧩 包含组件库资源，如 HyperUI、Mamba UI 和 Preline UI，部分免费，部分付费（如 Preline Pro 售价 $249）。
- 🔍 支持搜索功能，方便用户快速查找所需的模板和组件。
- 📬 提供新闻订阅服务，用户可接收新模板和组件更新的通知。
- 🌐 网站包含社交链接（Twitter/X、Bluesky）、提交项目入口以及隐私政策和条款等法律信息。

---

### [zot. 又一个编码代理工具。](https://www.zot.sh/?ref=tailwindweekly.com)

**原文标题**: [zot. Yet another coding agent harness.](https://www.zot.sh/?ref=tailwindweekly.com)

### 概述
zot 是一个轻量级、单二进制文件的终端编码助手，无需运行时或 Docker，专注于高效代理循环，支持多种 AI 提供商和扩展功能。

- 🚀 **单二进制部署**：用 Go 编写，无运行时、无 Docker、无包管理器，直接放入 `$PATH` 即可使用。
- 🛠️ **内置四工具**：读取、写入、编辑、bash，为实际编码提供最小必要工具箱。
- 🌐 **多模型支持**：兼容 Anthropic、OpenAI、Gemini、DeepSeek、本地模型等，通过统一 ID 管理。
- 🔌 **扩展与子代理**：支持 JSON-RPC 扩展，可注册命令、工具和权限门；后台子代理可并行运行。
- 📂 **会话控制**：支持恢复、分叉、分支、压缩和导出会话，自动压缩避免窗口溢出。
- 📱 **Telegram 桥接**：通过机器人令牌实现远程操作，支持读写、编辑和运行。
- 🧩 **核心精简**：无强制 MCP、无插件商店、无复杂配置，保持二进制小巧灵活。
- 💻 **跨平台兼容**：macOS、Linux、Windows 一键安装，仅需 `curl` 命令。

---

### [Marked 3 — Mac 上的 Markdown 预览工具](https://markedapp.com/?ref=tailwindweekly.com)

**原文标题**: [Marked 3 — Markdown Preview for Mac](https://markedapp.com/?ref=tailwindweekly.com)

Marked 3 是一款 Markdown 预览和发布工具，已在 Product Hunt 上线，支持用户预览和发布 Markdown 内容。

- 🚀 Marked 3 正式在 Product Hunt 上线，提供 Markdown 预览和发布功能。
- 👀 用户可访问 Product Hunt 页面，表达支持或留下评论。
- 📝 该工具专注于简化 Markdown 内容的预览与发布流程。

---

### [Peeker — 知道何时有人在你身后。· macOS](https://getpeeker.com/?ref=tailwindweekly.com)

**原文标题**: [Peeker — Know when someone's behind you. · macOS](https://getpeeker.com/?ref=tailwindweekly.com)

### 概述总结
Peeker 是一款专为 Mac 用户设计的隐私保护工具，能在有人靠近时通过实时预览提醒用户，所有处理均在本地完成，不保存任何数据。

- 👀 **实时预览**：当有人进入摄像头范围时，自动在屏幕角落显示实时画面，人离开后立即消失。
- 🔒 **完全本地处理**：所有帧在 Mac 内存中分析，不录制、不上传、不写入磁盘，无网络访问。
- 🛡️ **隐私优先**：无遥测、无云模型，静默运行，会议和屏幕共享时自动隐藏。
- 🖥️ **多屏支持**：适配宽屏和多显示器，仅显示在用户当前使用的屏幕上。
- 🎛️ **可自定义设置**：调整预览位置（右下角）、大小、灵敏度，不影响性能。
- 💰 **低价订阅**：每年仅 5 美元，支持所有 Mac（macOS 13+），含 30 天无理由退款。

---

