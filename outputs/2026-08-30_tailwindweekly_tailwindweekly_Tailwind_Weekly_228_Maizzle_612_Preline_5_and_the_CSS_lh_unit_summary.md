### [Preline UI 更新日志 | Tailwind CSS 组件库更新](https://preline.co/docs/changelog.html?ref=tailwindweekly.com)

**原文标题**: [Preline UI Changelog | Tailwind CSS Component Library Updates](https://preline.co/docs/changelog.html?ref=tailwindweekly.com)

Preline UI 的更新日志记录了从 v1.0.0 到 v5.0 的完整演进，涵盖新组件、插件、框架指南、主题系统、Tailwind CSS 版本升级以及大量 GitHub 问题修复，持续优化性能、可访问性和开发体验。

- 🚀 v5.0 引入 Preline MCP（Pro）、AI 提示和动画图标，升级 Tailwind CSS 至 v4.3，并修复高级日期选择器、范围滑块、焦点陷阱等多项问题。
- 🎠 v4.2.0 新增 Marquee 组件和 13 个框架指南，扩展 Stepper 与 Spinner 示例，支持 Tailwind v4.2.x 并移除旧版 aspect-ratio 插件。
- 🛠️ v4.1.x 改进插件模块架构以增强 tree-shaking，修复插件导出和构建问题，并为 Advanced Select 增加搜索匹配模式。
- 🎨 v4.0.0 推出 Preline Themes 主题系统，新增 10+ 框架指南（Vite、Laravel、Django 等），并完成大量可访问性和组件修复。
- 🧩 v3.2.0 新增 CMS 和 AI Chat 演示模板，推出集中式可访问性管理系统，并为 Tooltip 与 Popover 增加自动定位。
- ✨ v3.0.0 升级到 Tailwind v4，新增高级日期选择器、滚动导航、TimePicker 等组件，并用 Floating UI 替换 Popper.js。
- 🧭 v2.7.0 新增 Sidebar 和 Maps 组件，支持将 HTML 复制为 JSX，同时增强 Advanced Select 与 Combobox 功能。
- 🧰 v2.6.0 新增 5 个插件（Textarea Autoheight、Layout Splitter、Toast、Confetti、Leaflet Maps），并为大多数插件补充 destroy 方法。
- 📊 v2.5.0 新增高级范围滑块、树视图和拖放集成，扩展 Carousel 与 Advanced Select 的远程数据能力。
- 🗃️ v2.4.0 新增 Datatables 和文件上传插件，附大量新示例页面，并系统改进了可访问性。
- 🔤 v2.1.0 新增 ComboBox（自动完成）和 Theme-Switch 深色模式插件，升级 Tailwind 至 v3.4.x。
- 🏗️ v2.0.0 迎来重大版本更新：数百个新组件、9 个新插件、TypeScript 支持，并以 Lucide 替换 Bootstrap Icons。
- 📚 v1.x 系列持续添加示例页面（定价、英雄区块、博客等）和框架指南（Astro、SolidJS、Qwik、Svelte 等），并推出 Figma 资源。
- 🐛 各版本修复了大量反馈问题，涵盖日期选择器对齐、下拉定位、模态框焦点陷阱、滚动监听、远程请求错误等。

---

### [](https://github.com/maizzle/framework/releases/tag/v6.1.2?ref=tailwindweekly.com)

**原文标题**: [Release v6.1.2 · maizzle/framework · GitHub](https://github.com/maizzle/framework/releases/tag/v6.1.2?ref=tailwindweekly.com)

该仓库是 maizzle/framework 开源项目，主要提供 HTML 邮件构建框架。最新版本 v6.1.2 已发布，包含多项针对文件收集、Tailwind 源扫描和跨平台兼容性的修复，并加强了测试覆盖。

- ⭐ 项目当前拥有 1.6k Star 和 66 个 Fork，属于活跃维护的开源框架。
- 🚀 最新版本 v6.1.2 于 2024 年 8 月 24 日发布，并附有已签名的提交验证。
- 🧪 新增测试，覆盖渐变名称冲突及剩余的 Tailwind CSS 分支逻辑。
- 🔍 修复了 `collectSourceFiles` 中将 `node_modules` 作为路径段匹配的问题。
- 📁 修复遍历虚拟模块和查询变体时的源文件收集缺陷。
- 🪟 改进 Windows 路径处理，并在测试夹具中补充了 doctype 声明。
- 🎯 将 Tailwind 源码扫描范围限定到模板导入闭包，提升打包精度。
- 🔐 发布提交采用 SSH 密钥签名，指纹为 `TONi476WraK/eFfqp4CdFAATtW9bkm9S9/g8NuudtAI`。

---

### [更新日志 - shadcn/ui](https://ui.shadcn.com/docs/changelog?ref=tailwindweekly.com)

**原文标题**: [Changelog - shadcn/ui](https://ui.shadcn.com/docs/changelog?ref=tailwindweekly.com)

这是 shadcn 的更新日志，涵盖了从 2026 年 8 月到近期的多项重要发布。主要更新包括私有 GitHub 注册表支持、AI 辅助功能增强、新的 Questionnaire 组件、动态搜索能力以及 Toast 组件，同时还有 CLI 工具和框架集成方面的持续演进。

- 🔐 2026年8月：支持私有 GitHub 注册表，通过 gh 凭据或 GH_TOKEN 安装组件，零配置且支持 CI。
- 🤖 2026年8月：@shadcn/helpers 新增 Human-in-the-Loop 模拟，可在 AI SDK 中暂停等待审批或输入，并流式传输结果。
- 📋 2026年8月：发布 Questionnaire 组件，用于多步骤问题流程，支持单选/多选、自由输入、跳过、验证和条件问题。
- 🔍 2026年7月：注册表支持动态搜索，CLI 将查询参数转发给服务端，返回分页结果，静态注册表不受影响。
- 🔔 2026年7月：新增 Toast 组件（Base UI），支持操作、状态类型、Promise、堆叠和滑动关闭。
- 🧩 其他更新：CLI v4、GitHub 注册表、shadcn eject/apply/preset、RTL 支持、Base UI 默认、Tailwind v4、React 19、Monorepo 支持等。

---

### [React Bits - React](https://reactbits.dev/?ref=tailwindweekly.com)

**原文标题**: [React Bits - Animated UI Components For React](https://reactbits.dev/?ref=tailwindweekly.com)

您没有提供需要总结的文本内容，请发送文章或文本，我会按照模板为您生成中文摘要。

---

### [](https://chanhdai.com/components?ref=tailwindweekly.com)

**原文标题**: [Components – Chánh Đại](https://chanhdai.com/components?ref=tailwindweekly.com)

overview summary
- 🧩 提供像素级完美、独特设计的可复制组件库，支持多种包管理器安装。
- 🚀 包含 37 个免费组件，如 Apple Hello Effect、状态按钮、时间线等，可直接复制使用。
- 📦 支持 pnpm、yarn、npm、bun 和 shadcn add 命令，灵活集成到项目中。
- ✨ 组件覆盖动效、交互、导航、图标、测试等多个场景，满足多样化 UI 需求。
- 🏆 该组件库被列为“可信注册表”，可靠性有保障。

---

### [](https://beui.dev/?ref=tailwindweekly.com)

**原文标题**: [Animated Components for React and Next.js · beUI](https://beui.dev/?ref=tailwindweekly.com)

beUI 是一个为 React 和 Next.js 打造的开源动画组件库，基于 Tailwind CSS 与 Motion 构建，提供丰富的高质量交互动画组件，并备有 Pro 版本和页面区块，深受开发者喜爱。

- 🚀 基于 Tailwind 4 + React 19 + Motion 构建，兼容 React 和 Next.js，可通过 shadcn 快速复制安装。
- 💻 支持 bun、npm、pnpm、yarn 等包管理器，使用如 `bunx shadcn add @beui/tilt-card` 的命令添加组件。
- 🧩 提供 41+ 个动画组件，涵盖多选、文件树、金属按钮、模态框、通知堆栈、Dock、标签页、动态岛、命令面板、抽屉、OTP 输入等。
- ✨ 组件动效细腻：弹性布局、模糊过渡、方向感知滑动、3D 倾斜、数字滚动、主题切换转场等。
- 📦 另有 22+ 个页面区块（Blocks），如 404 页面、反馈组件、注册表单、钱包卡片、文件上传等。
- 💬 社区高度评价，称赞动画流畅自然、交互设计细致，是“最喜欢的组件库”之一。
- 🎁 提供 beUI Pro 付费版本，也支持按需定制前端组件与动效系统。
- 📄 项目基于 MIT 许可证，免费开源，作者为 Saurabh。

---

### [](https://inspira-ui.com/docs/en/components/html-in-canvas/html-in-canvas?ref=tailwindweekly.com)

**原文标题**: [HTML in Canvas - Inspira UI](https://inspira-ui.com/docs/en/components/html-in-canvas/html-in-canvas?ref=tailwindweekly.com)

本次更新发布了一系列新组件，并优化了部分现有组件，涵盖背景、按钮、卡片、文本动画、HTML画布特效等多种类别，适用于创意网页和交互体验。

- ✨ 新增多种背景与卡片组件：Ribbon Background、Card Stack、Cube Carousel、Circular Gallery、Float、Parallax Float、Path Marquee 等
- 🖼️ 新增 HTML 画布特效系列：HTML ASCII、HTML Blaze、HTML Chromatic、HTML Cloth、HTML Drag、HTML in Canvas、HTML Liquid
- 🔤 新增丰富文本动画效果：Breathing Text、Highlight Text、Letter Swap、Screw Text、Scroll Swap Text、Typewriter Text、Underline Text、Variable Letter Text、Variable Text
- 🔄 更新三项组件：Shader Toy Viewer、Infinite Grid、Spline，提升性能与表现
- 🧩 组件按类别整理，包括背景、按钮、卡片、光标、设备模型、输入框、杂项、特殊效果、评价、文本动画、可视化等
- 🎯 重点介绍 HTML in Canvas 页面：支持将 ShaderToy 风格片段着色器应用于实时 HTML 内容，基于 WebGL 实现交互式视觉效果

---

### [](https://zardui.com/?ref=tailwindweekly.com)

**原文标题**: [Zard UI - The @shadcn/ui Alternative for Angular - zard/ui](https://zardui.com/?ref=tailwindweekly.com)

概述：这是一个为 Angular 项目打造的 UI 组件库，提供类似 shadcn/ui 的体验，基于现代化技术栈，并展示丰富的界面组件与场景。

- 🚀 专为 Angular 设计，提供 shadcn/ui 风格的原生体验
- ⚡ 基于 Signals 与 TailwindCSS v4，支持 SSR 且无需 zone.js
- 📦 通过 `npx zard-cli init` 快速初始化项目
- 🧩 包含表单、按钮、开关、卡片、对话框等常用组件示例
- 👥 覆盖团队协作、支付设置、身份验证、外观配置等界面场景
- ☁️ 支持 Kubernetes 与虚拟机等计算环境配置
- 🔒 强调安全与加密，如支付信息、两步验证等
- ❤️ 开源项目，在 GitHub 上发布，源自巴西

---

### [lucide-animated | 免费动画React图标库](https://lucide-animated.com/?ref=tailwindweekly.com)

**原文标题**: [lucide-animated | Free Animated React Icons Library](https://lucide-animated.com/?ref=tailwindweekly.com)

这是一个开源的动画图标库，基于 Motion 和 Lucide 构建，提供流畅精致的动画效果，并欢迎社区反馈与贡献。
- 🎨 开源动画图标集合：采用 MIT 许可证，可自由使用，旨在打造高品质的界面图标库
- ⚙️ 技术驱动：基于 Motion 动画库与 Lucide 图标体系，确保动画流畅且风格统一
- 📦 多种安装方式：支持 pnpm、npm、yarn、bun，可通过 `pnpm dlx shadcn add @lucide-animated/` 快速集成
- 🖱️ 注重细节体验：强调时序、状态、反馈与点击重量等“隐形细节”，让界面交互更自然
- 👤 创作者理念：由 dmytro 开发，认为好图标是让界面“感觉对”的关键，并推出相关课程
- 🔍 丰富图标列表：包含方向、辅助功能、医疗、对齐等大量分类图标，如 airplane、alarm-clock、align-center 等

---

### [](https://github.com/aidenybai/tailwind-stylex?ref=tailwindweekly.com)

**原文标题**: [GitHub - aidenybai/tailwind-stylex at tailwindweekly.com · GitHub](https://github.com/aidenybai/tailwind-stylex?ref=tailwindweekly.com)

overview summary  
tailwind-stylex 是一个将 Tailwind 默认设计令牌无缝集成到 StyleX 的工具，提供类型安全、自动补全的使用体验，无需额外配置或生成流程。

- 📦 安装：通过 `pnpm add tailwind-stylex @stylexjs/stylex` 即可使用。
- ⚙️ 编译器配置：需让 StyleX 编译器处理该包，例如启用 `externalPackages: ["tailwind-stylex"]` 或在 postcss-plugin 的 `include` 中添加 token 模块。
- 🎨 基本用法：从 `tailwind-stylex/tokens.stylex` 导入 `colors`、`spacing`、`radii` 等令牌，并直接在 `stylex.create` 中引用。
- 🔢 数值令牌：使用括号语法访问数字命名的令牌，如 `fontSizes["2xl"]`、`containers["7xl"]`。
- 📚 令牌分类：涵盖颜色、布局（间距/断点/容器等）、排版（字体/字号/行高/字重等）、表面（圆角/阴影/模糊）、动效（缓动/动画/透视）以及默认值。
- 🧩 核心优势：编辑器可自动补全每个令牌并显示实际值，无需扫描、生成或额外配置。
- 📄 开源许可：基于 MIT 许可证发布。

---

### [](https://github.com/aidenybai?ref=tailwindweekly.com)

**原文标题**: [aidenybai (Aiden Bai) · GitHub](https://github.com/aidenybai?ref=tailwindweekly.com)

overview summary  
- 👤 GitHub用户Aiden Bai（aidenybai），位于旧金山，拥有5.8k关注者，个人网站及X账号@aidenybai。  
- 🏢 属于millionco组织，拥有191个公开仓库、1.2k星标，并参与2项赞助。  
- ⭐ 置顶开源项目均为TypeScript，专注React生态：react-scan（21.8k星，定位React性能问题）、million（17.7k星，React优化编译器）、react-doctor（14.7k星，检测不良React代码）、react-grab（7.6k星，复制UI元素）、bippy（1.4k星，探索React内部）、cnfast（1.2k星，快速cn替代）。  
- 🏅 拥有GitHub开发者计划成员和Pro身份，并展示多项成就徽章。  
- 🔧 整体专注于React性能优化、工具链与开发体验提升。

---

### [Picmal：你的Mac媒体工具包，用于转换和压缩](https://picmal.app/?atp=redpixel&ref=tailwindweekly.com)

**原文标题**: [Picmal: your Mac's media toolkit to convert & compress](https://picmal.app/?atp=redpixel&ref=tailwindweekly.com)

overview summary  
Picmal v1.8.6 是一款专为 Mac 设计的本地媒体工具包，支持图片、视频、音频和 PDF 的转换、压缩与编辑，强调隐私安全，无需上传或登录，可离线使用，并以简洁高效处理批量任务见长。

- 🖥️ 在 Mac 上本地完成图片、视频、音频和 PDF 的转换、压缩与编辑，无需依赖可疑网站。
- 🔒 100% 本地处理：无文件上传、无需账户、支持离线使用，保护隐私安全。
- 🔄 提供转换、压缩和 PDF 工具等核心功能，覆盖常见媒体处理需求。
- ⚡ 以简洁和速度著称，能高效管理任意规模的批量转换与压缩任务。
- 👍 获得评测推荐：Picmal 在文件转换和压缩管理方面操作简单、速度快，值得尝试。

---

### [](https://nerdy.dev/css-infinity-use-cases?ref=tailwindweekly.com)

**原文标题**: [CSS Infinity Use Cases · July 25, 2026](https://nerdy.dev/css-infinity-use-cases?ref=tailwindweekly.com)

CSS 中的 `infinity`（及 `-infinity`）虽然看似简单，却能优雅解决许多特殊问题，甚至带来纯粹的乐趣。本文介绍了从基础语法到高级应用的多种场景，如创建完美圆形、冰冻动画、最大化层级、解除 `clamp()` 限制、实现响应式圆角、构造布尔逻辑、冻结视图过渡、滚动触发等，同时也指出了某些技巧的无效性。

- 🔧 基础用法：`infinity` 必须写在 `calc()` 中，且表示尺寸时需乘以单位，如 `calc(infinity * 1px)`；也可用于 `clamp()`、`min()`、`max()` 等函数。
- ⚪ 圆形与胶囊：`border-radius: calc(infinity * 1px)` 可替代 `1e9px` 的旧方法，在任何尺寸下生成完美圆角。
- ❄️ 永久状态：将动画或过渡时长设为 `calc(infinity * 1s)`，看似冻结，实际会在页面生命周期内保持最终状态。
- 📚 z-index 极限：`z-index: calc(infinity)` 能直接拉满到浏览器最大值 `2147483647`，并可用 `counter` 验证。
- 🚀 解除 clamp 限制：使用 `calc(-infinity * 1px)` 和 `calc(infinity * 1px)` 可分别移除 `clamp()` 的上下边界。
- 🧊 冻结视图过渡：将视图过渡动画时长设为无限，使其永不结束，方便在 DevTools 中检查伪元素树。
- 📐 响应式圆角：类似 `clamp(0px, (100vi - 100%) * infinity, 20px)` 可让圆角根据元素与视口的大小关系自动切换。
- 🔢 布尔开关：通过 `clamp()` 配合 `infinity`，将任意数值压缩为 `0` 或 `1`，驱动多种样式变化。
- 🎭 背景遮罩：用 `box-shadow: 0 0 0 calc(infinity * 1px)` 制作非交互背景——但实际无效，需改用很大的字面数字。
- 📜 滚动触发：设置 `timeline-trigger-activation-range-end: calc(infinity * 1px)` 让滚动驱动的动画只进不退，也可与 scroll-driven 版本对比。
- 💬 结尾互动：作者邀请读者在评论区分享更多 `infinity` 的创意用法。

---

### [](https://ishadeed.com/article/lh-unit/?ref=tailwindweekly.com)

**原文标题**: [The CSS lh unit](https://ishadeed.com/article/lh-unit/?ref=tailwindweekly.com)

overview summary
- 📌 要点需清晰直接，避免冗长废话。
- 📊 每条内容至少包含一个图表或具体示例，帮助理解。
- 🧠 目标是让你学到新知识，或至少唤起你对旧知识的记忆。
- ✅ 请放心，你会收到顶级质量的内容推荐。

---

### [获取失败](https://master.dev/blog/typographic-css-tricks/?ref=tailwindweekly.com)

**原文标题**: [Failed to retrieve](https://master.dev/blog/typographic-css-tricks/?ref=tailwindweekly.com)

无法总结：获取内容失败，状态码 403。

---

### [](https://verifykit.io/?ref=tailwindweekly.com)

**原文标题**: [VerifyKit — The simplest way to verify your users](https://verifykit.io/?ref=tailwindweekly.com)

overview summary
VerifyKit 是一个用户验证服务平台，通过单一 API 提供邮箱验证与 OTP 双重认证，帮助拦截虚假注册、清理营销列表并提升安全性，已在全球边缘网络部署。

- ✅ 一站式 API 实现邮箱验证与 OTP，阻止虚假注册进入数据库
- 🛡️ 特色功能：拦截一次性邮箱、捕捉注册拼写错误、发送邮件 2FA 验证码、清理营销列表
- ⚡ 全球边缘网络部署，覆盖 200+ 城市，p50 响应时间低于 200ms，具备 DDoS 缓解与 99.99% 可用性
- 🔧 提供 Node.js、TypeScript、PHP、Go、Python、Rust 等原生 SDK，支持快速集成
- 🔢 邮件 OTP 为六位数字、10 分钟有效，无需短信或 Twilio，并有专门 2FA 文档
- 📡 REST + JSON 单一端点，任何编程语言均可通过 curl 调用，返回有效性评分
- 💵 定价从每验证 $0.001 起，支持按量计费；新用户可免费试用，并有 14 天无理由退款
- 📋 提供 Starter、Growth、Pro、Unlimited 四种套餐，按验证量、API 密钥数量、OTP 用量等区分，首三个月享 20% 折扣
- 📜 支持 GDPR、PSD2 SCA、APP、NIST 800-63 等合规要求，适合强认证场景
- 🌍 全球边缘网络优势：用户就近验证，基础设施抗峰值流量，滥用流量在边缘即被拦截

---

### [](https://tailmotion.moumen.dev/?ref=tailwindweekly.com)

**原文标题**: [TailMotion — Motion that speaks Tailwind](https://tailmotion.moumen.dev/?ref=tailwindweekly.com)

您没有提供需要总结的文章内容。请粘贴文本，我会按您的要求用中文生成概述和带表情符号的要点。

---

### [](https://windybase.com/?ref=tailwindweekly.com)

**原文标题**: [WindyBase - Explore free and premium Tailwind CSS templates ](https://windybase.com/?ref=tailwindweekly.com)

WindyBase 是一个每周精选的 Tailwind CSS 模板与工具目录，为开发者提供大量免费和付费的网站构建资源，涵盖多种分类，并支持订阅更新与资源提交。

- 🧭 平台定位：WindyBase 是面向现代开发者的 Tailwind CSS 模板和工具导航站，每周更新精选内容。
- 📂 丰富分类：包含着陆页、SaaS、博客、仪表盘、电商模板以及组件库等主要类别。
- 🧩 组件库资源：收录如 Mamba UI、HyperUI、Preline 等免费与付费组件库，方便快速搭建界面。
- 💰 免费与付费选项：既有 Horizon、Landing Pad 等免费资源，也有 Voyager、Nova 等付费模板（价格约 $15–$249）。
- 📧 订阅功能：支持订阅新闻通讯，第一时间获取新增模板和组件通知。
- 🔍 其他功能：提供搜索、资源提交入口，并可通过 Twitter/X、Bluesky 等社交平台关注。

---

### [](https://www.getoutline.com/?ref=tailwindweekly.com)

**原文标题**: [Outline – Team knowledge base & wiki](https://www.getoutline.com/?ref=tailwindweekly.com)

Outline 是一款开源团队知识库工具，旨在帮助团队摆脱文档混乱、权限不清和重复询问的困境。它提供云端托管、本地部署和自托管等多种方式，拥有直观编辑、实时协作、AI 问答、Slack 集成、暗黑模式、安全权限管理等丰富功能，并支持 20 多种语言，拥有 2000+ 客户和 40k GitHub Star。

- 📚 解决知识库痛点：告别文档堆砌与权限混乱，统一组织团队知识，避免同事重复索要信息。
- ☁️ 多种部署方式：支持云端托管（30 天免费试用）、本地部署或自托管服务器。
- 🏆 值得信赖：拥有 2000+ 客户、10 年开源历史、40k GitHub Star，社区活跃。
- ✏️ 直观编辑体验：极速编辑器支持 Markdown、斜杠命令和互动嵌入等丰富功能。
- 🤝 多人实时协作：支持文档实时协同编辑，评论和话题讨论让沟通井然有序。
- 🔍 强大搜索与 AI 问答：瞬时搜索工作区内容，还可直接向文档提问获得 AI 答案。
- 💬 Slack 集成：无需离开聊天即可搜索、分享和提问，文档更新时自动推送通知到频道。
- 🔗 灵活共享：可通过链接公开分享，也可团队私有共享，并支持自定义品牌色、Logo 和域名。
- ⚡ 极速性能：毫秒级响应，文档加载、搜索和界面导航都快速流畅。
- 🌙 暗黑模式：提供美观且护眼的深色界面，适合夜间使用。
- 🔒 安全与权限管理：支持读写权限、用户组、访客用户、公开共享等精细管控。
- 🧩 20+ 集成：与 Slack、Figma、Loom 等日常工具无缝集成，另有开放 API 可扩展。
- 🌍 多语言支持：支持 RTL 及 20 种语言，包括法语、西班牙语、德语、韩语和中文。
- 📢 公开开发与更新：定期发布新功能和修复，公开变更日志，发展透明。
- 🆓 开源可自托：源代码公开，可部署在自有基础设施，完全掌控数据。
- 🎨 高度可定制：支持自定义域名（如 docs.yourteam.com）和白标品牌。

---

### [](https://webclaw.io/?ref=tailwindweekly.com)

**原文标题**: [webclaw: Web Scraping API for LLMs and AI Agents](https://webclaw.io/?ref=tailwindweekly.com)

Webclaw 是一个面向 AI 代理的网页抓取 API，可将任何 URL 转换为干净的 Markdown 或 JSON，比原始 HTML 减少约 90% 的 token 消耗；它是 Firecrawl 的开源替代品，提供云 API、CLI 工具和 MCP 服务器，支持自托管，并拥有统一信用池的多种定价方案。

- 🌐 将任何 URL 转为 LLM-ready Markdown 或 JSON，token 量较原始 HTML 减少约 90%。
- 🔄 作为 Firecrawl 的即插即用替代品，兼容 /v2 路由，只需替换 base URL 即可迁移。
- ⚙️ 提供 11 个 REST 端点，涵盖 scrape、crawl、search、extract、map、batch、summarize、research、brand、diff、lead。
- 🤖 内置 MCP 服务器，暴露 14 个工具，可直接接入 Claude、Cursor、Codex 等代理环境。
- ⌨️ 提供终端原生 CLI 工具，方便在命令行中直接进行数据提取。
- 🔑 一个 API key 即可访问所有端点，统一信用池，按使用量计费。
- 💰 定价从 Starter $19/月起步，另有 Growth $49、Pro $99、Scale $399，年付可享 20% 折扣。
- 🧠 Research 深度研究功能有独立计数器，避免大量运行耗尽预算。
- 🛡️ 采用 HTTP 与 TLS 指纹模拟而非无头浏览器，响应低于 200ms，无需 Selenium 或 Playwright。
- 📄 支持六种输出格式：Markdown、JSON、HTML、纯文本、LLM 优化文本和原始 HTML。
- 🔓 能够绕过 bot 防护墙，渲染 JavaScript 页面，让代理读到真实内容。
- 🏠 开源核心基于 Rust，遵循 AGPL-3.0 协议，可免费自托管，支持 Docker 一键部署。
- 📊 典型应用场景包括库存监控、旅行价格监控、销售线索挖掘、AI agents、RAG 管道和深度研究。
- 🔒 提取内容不会在服务器存储或记录，支持实时处理，并可配置自托管以实现完全数据控制。
- 🎁 无需信用卡即可体验，每天免费运行 3 次；另为开源开发者提供免费信用额度。
- 🌍 已在实际大型网站上验证，涵盖 Nike、Airbnb、Shopify、IMDb、GitHub 等众多知名平台。

---

### [](https://openlogi.org/?ref=tailwindweekly.com)

**原文标题**: [OpenLogi](https://openlogi.org/?ref=tailwindweekly.com)

OpenLogi 是一款本地优先的 Logitech 设备配置工具，用 Rust 编写，可直接通过 HID++ 协议操控鼠标、键盘和摄像头，替代 Logitech Options+。无需账户、无遥测，配置以可移植的 TOML 文件保存，支持多平台安装，并注重用户隐私与设备掌控。

- 🖱️ 核心功能：通过 HID++ 2.0 直接控制设备，支持按钮重映射（44 种内置动作）、DPI 预设与切换、SmartShift 滚轮模式（棘轮/自由滚动），以及自定义快捷键和应用启动器。
- 📄 配置透明：所有设置保存在 `~/.config/openlogi/config.toml`，用户可手编辑、备份并跨机器迁移；设备按物理序列号标识，无需云端同步。
- 🔒 隐私至上：无账户、无遥测、无云；更新检查默认关闭，绑定和配置永不离开本地设备。
- 🔌 连接广泛：支持 Logi Bolt、Unifying、Lightspeed、蓝牙及 USB 有线连接，无需专用接收器。
- 📦 安装方式：macOS 可 Homebrew 安装（`brew install --cask openlogi`）或下载 .dmg；Linux 提供 .deb/.rpm/.pkg.tar.zst；Windows 提供 .msi（x86_64/arm64），均签名。
- 🧩 设备视图：实时显示已配对设备列表，含电池电量和充电状态；macOS 侧键重映射需要辅助功能权限，但 HID++ 路径（手势键、DPI 等）不需要。
- 🚧 开发中功能：每应用配置（按前台应用自动切换）、导入 Options+ 设置、Logitech Flow 支持规划中；Bolt 配对已支持，Unifying/Lightspeed 配对进行中。
- ⚠️ 使用提示：需先退出 Logi Options+ 或 Solaar，避免 HID++ 访问冲突；FAQ 中强调更新仅手动触发，绑定文件可随时复制移动。

---

