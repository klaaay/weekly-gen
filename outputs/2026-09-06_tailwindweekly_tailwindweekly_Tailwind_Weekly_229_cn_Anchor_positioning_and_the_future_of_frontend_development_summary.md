### [](https://github.com/shadcn-ui/cn?ref=tailwindweekly.com)

**原文标题**: [GitHub - shadcn-ui/cn at tailwindweekly.com · GitHub](https://github.com/shadcn-ui/cn?ref=tailwindweekly.com)

cn 是 shadcn 与 aidenybai 打造的新一代 Tailwind CSS 类名合并与冲突解决引擎，目标是替代 `tailwind-merge` 和 `clsx`。它保持相同的 API 与完全一致的输出，但速度大幅提升：典型组件调用约 30× 更快，真实仓库语料上平均约 37× 更快。该库零依赖、跨框架、可在多种运行时使用，并支持自定义主题与 Tailwind v4，同时提供 CLI 命令方便迁移。

- ⚙️ 核心用途：统一处理条件式类名拼接（类似 `clsx`）与 Tailwind 类冲突解决（类似 `tailwind-merge`），API 同名、输出完全对齐。
- 🚀 性能优势：常见 `cn(base, variant, condition && extra)` 场景约 10 ns vs 320 ns（30× 快）；缓存命中场景约 1.9× 快；真实 58 个仓库、144,265 次调用回放中几何平均快 37×。
- 📦 零依赖与通用性：不依赖任何框架，支持 React、Vue、Svelte、Solid、Astro 等；可在浏览器、Node、Bun、Deno 及边缘运行时中工作。
- 🛠️ 安装与迁移：通过 `npm i cn` 安装；现有 shadcn/ui 项目可用 `npx shadcn@latest migrate cn` 一键替换 `clsx` + `tailwind-merge`。
- 📉 包体积：minified 后约 26 KB；需要更小体积时可使用 `cn build` 生成编译期表。
- 🎨 自定义配置：`cn/config` 导出 `createCn()`，支持 `extend`、`override`、`prefix`；与 tailwind-merge 的 `extendTailwindMerge` 用法一致，也支持 Tailwind v4 前缀。
- ✅ 兼容保证：通过 356,000 项差分测试，验证每个输入的输出结果与 tailwind-merge 一致；从 tailwind-merge 迁移时导出名称基本一一对应。
- ⚠️ 注意事项：支持 Tailwind CSS v4；若仍用 v3，建议继续使用 tailwind-merge v2；动态拼接类名（如 `"p-" + size`）在 `cn build` 下无法识别，需用 `--safelist`；CLI 需 Node 20+。
- 🔌 API 概览：主包提供 `cn()`、`twMerge()`、`twJoin()`、`clsx()`；另有 `cn/config`（配置）、`cn/engine`（编译表引擎）、`cn/lite`（纯字符串连接）等子路径。

---

### [](https://reactbits.dev/?ref=tailwindweekly.com)

**原文标题**: [React Bits - Animated UI Components For React](https://reactbits.dev/?ref=tailwindweekly.com)

您似乎没有附上需要总结的文本内容。请提供文章内容，我会按照要求用中文为您生成“概述总结 + 表情符号要点列表”。

---

### [](https://magicui.design/?ref=tailwindweekly.com)

**原文标题**: [Magic UI](https://magicui.design/?ref=tailwindweekly.com)

overview summary
🎉 Magic UI 发布了全新的“Floating 3D Particles”特效库，专为设计工程师打造，提供 150+ 免费开源的动画组件与效果，并搭配多个实际应用案例展示。

- 🎊 推出全新 UI 库，主打“Floating 3D Particles”浮动 3D 粒子效果
- 🧩 提供 150+ 免费且开源的动画组件与效果，可直接用于页面构建
- ⚛️ 技术栈基于 React、TypeScript、Tailwind CSS 和 Motion
- 🔧 可与 shadcn/ui 完美搭配，适合设计工程师快速使用
- 🖥️ 提供“浏览组件”和“浏览模板”入口，方便用户直接查看使用
- 🏢 受多家企业青睐，用于构建落地页（Landing Pages）
- 🚀 展示案例包含多个知名项目：Anara（YC S24）、Cognosys（Google Ventures 投资）、Infisical（YC W23）等
- 💼 案例涵盖个人作品集、开源项目、独立开发产品和创业公司，类型多样
- 🌟 个人作品集包括 Aryan Karma、Darshan Paccha、Elhussary 等设计师
- 🎓 多个案例获得 YC、Google Ventures、Vercel AI Accelerator 等机构资助或奖项
- 🛠️ 一些项目为开源库或工具，如 guarahooks、robot-toast、writora.xyz
- 📢 包含 Twitter 用户评价展示区，提升社区认可度
- ▶️ 页面还集成了 YouTube 视频演示板块，提供播放按钮展示特效效果

---

### [](https://reui.io/?ref=tailwindweekly.com)

**原文标题**: [Free Shadcn UI Components, Blocks, Icons, Templates & MCP - ReUI](https://reui.io/?ref=tailwindweekly.com)

overview summary
- 🧩 ReUI 是为 shadcn/ui 打造的设计优先组件平台，提供 533+ Pro Blocks、1,105+ 免费组件及 638+ 图标，覆盖应用、数据网格、电商、营销、AI 代理等场景。
- 📊 数据网格模块基于 TanStack Table v9 构建，支持编辑、分组、筛选、虚拟化、拖放及新增 spreadsheet 任务网格，并获社区高度评价。
- 🤖 内置 MCP 服务器与 Agent Skills，可连接 Claude、Codex、Cursor、Copilot 等十余种 AI 编码工具，让代理直接搜索、安装并使用真实组件。
- 🧱 提供完整多页面模板（Next.js、Vite、TanStack Start、Astro、Laravel 等），覆盖 SaaS、仪表盘、CRM、HR 等业务场景。
- 💎 组件由资深设计工程师手工打造，注重可访问性、键盘操作与 ARIA，强调生产级质量，避免 AI 生成的“通用垃圾代码”。
- 💰 Pro 采用一次性 $249 买断制，源码永久归用户所有，节省大量 AI token 与反复修改时间。
- 🎨 免费组件持续更新且永久免费，同时提供 Figma 设计系统、深色模式与 RTL 支持，适合实际产品使用。
- 🗣️ 获得 shadcn/ui 创作者及大量开发者认可，社区反馈称赞数据表格、Gantt 组件、拖放与整体设计品质。

---

### [意图 UI](https://intentui.com/?ref=tailwindweekly.com)

**原文标题**: [Intent UI](https://intentui.com/?ref=tailwindweekly.com)

overview summary
- 🧩 Intent UI 是一套可访问的 React 组件库，基于 React Aria 构建，支持快速复制、自定义，并使用 Tailwind CSS 进行样式设计。
- 📂 提供丰富的组件分类，包括覆盖层、控件、表单、日期时间、拖放、布局、媒体、导航、状态、选择器、文本和可视化图表等。
- 🎨 内置多种主题与样式选项，可整体定制外观，满足不同项目的视觉需求。
- 🧱 提供现成的应用块与模板，如侧边栏、导航、认证布局等，帮助加速现代 Web 应用开发。
- ⚡ 配套多种 Starter Kit，包括 Next.js、Laravel、Tanstack Router 和 Vite，预配置项目以快速启动。
- 🔓 完全开源，采用 MIT 许可证，支持自由使用、查看源码或参与贡献。
- 🤝 项目由 Irsyad 制作，托管于 Vercel，并提供赞助渠道与社区资源（如 GitHub、Discord、Twitter）。
- 📈 展示多种可视化组件，如面积图、柱状图、饼图、雷达图、径向条形图和追踪器等。
- 🔒 示例内容覆盖用户权限、通知偏好、隐私设置等实际交互场景，强调可访问性与用户体验。
- 🚀 旨在让开发者“复制、定制并拥有”自己的 UI，以高效方式构建现代界面。

---

### [](https://blocks.so/?ref=tailwindweekly.com)

**原文标题**: [Shadcn Blocks - 60+ Free shadcn/ui Components for React](https://blocks.so/?ref=tailwindweekly.com)

这是一套面向 Web 开发的开源“构建块”集合，提供基于 shadcn/ui 与 Tailwind CSS 的可复制粘贴 React 组件，覆盖 AI、弹窗、上传、表单、统计等多种场景，并适用于所有 React 框架。

- 🎯 项目定位：为 Web 提供可复用的“积木”组件，基于 React 实现，支持复制粘贴直接使用。
- 🔧 技术栈：基于 shadcn/ui 与 Tailwind CSS 构建，兼容所有 React 框架。
- 🌍 开源特性：完全开源，组件可访问，并已为生产环境做好准备。
- 🤖 AI 组件：AI Chat 共 3 个，AI Components 共 5 个。
- 🗂️ 命令与弹窗：Command Menu 共 3 个，Dialogs 共 12 个。
- 📤 上传与表单：File Upload 共 6 个，Form Layout 共 5 个。
- 📋 布局与登录：Grid List 共 3 个，Login & Signup 共 9 个。
- 🚀 引导与导航：Onboarding 共 7 个，Sidebar 共 6 个。
- 📊 数据展示：Stats 共 15 个，Tables 共 5 个。
- 👨‍💻 作者与来源：由 Ephraim Duncan 构建，源码托管于 GitHub，访问 blocks.so 获取，© 2026 Blocks.so。

---

### [](https://beui.dev/?ref=tailwindweekly.com)

**原文标题**: [Animated Components for React and Next.js · beUI](https://beui.dev/?ref=tailwindweekly.com)

beUI 是一个免费、开源的动画组件库，专为 React 与 Next.js 构建，内置 115 个基于 Tailwind CSS 4 和 Motion 的可复制组件，并可通过 shadcn 方式快捷安装与定制。
- ✨ 提供 115 个组件，支持 Tailwind 4 + React 19，全面适配 Motion 动画。
- 🧩 组件可复制粘贴、开源免费，并通过 shadcn registry 分发，支持自定义定制。
- 🎯 覆盖丰富交互场景：按钮、模态框、Toast、标签页、底部抽屉、命令菜单、滑块、开关等。
- 📦 包含多种 Blocks 区块模板，如 404 页面、OTP 输入、反馈组件、表单、文件上传等。
- 🛠️ 特色组件如 Tilt Card、Digit Swap、Adaptive Stepper、Bloom Menu 等，动效细腻。
- 💻 支持 bun、npm、pnpm、yarn 等快捷安装方式，便于直接集成到项目中。
- 💬 获得开发者社区大量好评，作者为 Saurabh（@saurra3h），并提供 Pro 版本及定制服务。

---

### [](https://github.com/arihantcodes/spectrum-ui?ref=tailwindweekly.com)

**原文标题**: [GitHub - arihantcodes/spectrum-ui at tailwindweekly.com · GitHub](https://github.com/arihantcodes/spectrum-ui?ref=tailwindweekly.com)

Spectrum UI 是一个免费的 React 组件库，基于 shadcn/ui、Tailwind CSS 和 Motion 构建，所有源码都直接放入你的项目，没有任何包依赖，可自由修改。目前提供 250+ 组件、页面块和模板，每个都有实时预览和代码展示。

- 🧩 获取组件有三种方式：让 AI 编辑器通过 MCP 服务器安装、使用 shadcn CLI 命令安装，或直接复制页面代码粘贴到项目。
- 🤖 MCP 服务器支持：连接后可在 Claude Code、Cursor、Windsurf 中直接描述需求，由 AI 自动查找并安装组件。
- 📦 内容丰富：包含表单、卡片、按钮、评分、弹层、媒体、认证等组件，以及 Hero、Pricing、FAQ、页脚等区块和整套仪表盘/落地页模板。
- 🎨 额外提供调色板浏览器页面，方便探索和选用配色。
- 🖥️ 本地运行只需克隆仓库、执行 `yarn install` 和 `yarn dev`，即可访问 `localhost:3000`；但认证、支付、书签等功能需要配置 `.env` 密钥才会显示。
- ⚙️ 技术栈为 Next.js 14 (App Router)、TypeScript、Tailwind、Radix、Motion，账户系统用 Supabase 与 NextAuth，邮件走 Resend，部署在 Vercel。
- 👥 欢迎贡献：新组件通常包含源码、文档页、注册表和目录条目，提交 PR 前需运行 `yarn test` 保持各部分同步；缺少组件可在 Issues 中提出。
- 📄 采用 Apache-2.0 许可证，由 Arihant 及贡献者共同维护。

---

### [](https://picmal.app/?atp=redpixel&ref=tailwindweekly.com)

**原文标题**: [Picmal: convert and compress media on your Mac, offline](https://picmal.app/?atp=redpixel&ref=tailwindweekly.com)

Picmal 是一款专为 Mac 设计的本地文件转换与压缩工具，支持图片、视频、音频和 PDF 的批量处理与格式转换。所有操作均在设备本地完成，文件不会上传，采用一次付费、无订阅的模式，价格 29 美元，并受到大量用户的积极评价。

- 🆕 新版本 v1.8.8：可在 Mac 上转换和压缩图片、视频、音频与 PDF，支持批量处理，无需上传文件。
- 💰 售价 $29 一次性买断，包含后续更新，无需账户或订阅，可离线使用。
- ⭐ 用户普遍称赞其简洁易用、速度快、界面干净，并认可持续的功能更新。
- 🔄 支持超过 100 种格式互转，如 HEIC↔JPG、MOV↔MP4、FLAC↔ALAC 等，也可直接压缩并调整文件大小。
- 📑 提供全套 PDF 工具：合并、拆分、图片转 PDF、页面排序、旋转、删除及密码保护。
- 🎬 视频支持合并片段、添加水印、下载网页视频并重新封装；可去除背景并导出透明 PNG。
- 🖼️ 可裁剪图片和 PDF、将位图转为 SVG 矢量图、生成 macOS/iOS/Windows 应用图标。
- 🔁 具备文件夹监视自动处理、剪贴板优化压缩、Finder/Shortcuts/Raycast 集成，以及命令行 CLI。
- 🔒 隐私保护出色：所有处理均在本机完成，文件永不离开你的 Mac，无需联网。
- 💳 授权可选 1/2/5/10 台 Mac，支持随时补差价升级；提供 14 天无理由退款及学生/地区折扣。
- 👨‍💻 由创始人 Alberto 独立开发，重视用户反馈，持续改进产品，并提供免费教程帮助用户完成常见转换任务。

---

### [](https://www.joshwcomeau.com/css/anchor-positioning/?ref=tailwindweekly.com)

**原文标题**: [Getting Started with Anchor Positioning • Josh W. Comeau](https://www.joshwcomeau.com/css/anchor-positioning/?ref=tailwindweekly.com)

CSS Anchor Positioning API 是一套新原生机制，让开发者无需复杂 JavaScript，即可将工具提示、下拉菜单等目标元素固定到页面上其他元素（锚点）上，并自动处理溢出翻转、定位回退和视觉箭头方向调整等常见难题。文章介绍了核心用法、位置回退机制、新版容器查询特性、浏览器支持状况及降级策略。

- 🎯 核心价值：用来解决工具提示/下拉菜单等 UI 元素的“锚定-溢出”问题，替代过去复杂易错的原生 JS 实现。
- 🌐 浏览器支持：截至 2026 年 7 月约 81% 支持；Level 2 的 “anchored container queries” 覆盖率约 64%，目前主要可用在 Chromium，但已纳入 Interop 2026。
- 🧩 基础用法：锚点元素通过 `anchor-name` 命名；目标元素设置 `position: absolute/fixed`、`position-anchor` 指向锚点，再用 `position-area` 指定相对位置（类似 3×3 网格）。
- 📏 间距与扩展：可用 `margin` 制造目标与锚点间距；还支持逻辑属性（如 `inline-start`）以及 `span-*` 实现跨行/跨列布局。
- 🔄 溢出保护：配合 `position: fixed` 与 `position-try-fallbacks`，当目标元素溢出视口时可自动切换到备用位置（如 `bottom`）。
- 🧠 行为特点：一旦启用备用位置，即使原位置重新有空间也不会自动切回——这符合规范意图，可避免 UI 反复跳动。
- 💡 翻转箭头：通过 Level 2 的 `container-type: anchored` 和 `@container anchored(fallback: …)`，可在目标元素使用回退位置时，同步调整 tooltip 箭头 / 内边距等样式。
- 🔃 更简单方案：`flip-block` 关键字可自动在块轴方向翻转，并同步翻转 margin 等方向相关属性；且已被所有主流浏览器支持。
- 🛠️ 兼容降级：可使用 Oddbird 提供的 polyfill，或用 `@supports` 构建从基础回退到理想体验的分级方案；部分复杂场景仍可继续考虑 JS 库。
- 📚 扩展知识：文章未深入介绍 `anchor()` / `anchor-size()` 等高级函数；文末附有 CSS Tricks 指南、web.dev、CSSWG 规范及 Anchoreum 练习游戏等学习资源。

---

### [](https://caniuse.com/css-anchor-positioning?ref=tailwindweekly.com)

**原文标题**: [CSS Anchor Positioning | Can I use... Support tables for HTML5, CSS3, etc](https://caniuse.com/css-anchor-positioning?ref=tailwindweekly.com)

CSS Anchor Positioning 用于让元素相对于“锚元素”自由定位，不受页面其他元素布局影响，目前处于工作草案阶段，全球总体可用率约 85.93%。

- 🌐 全球使用率：85.93%（57.74% 完整支持 + 28.19% 部分支持）
- 📌 核心功能：可将元素放置在页面任意位置，仅需相对“锚元素”并忽略其他元素的布局约束
- 📄 规范状态：WD（工作草案）
- ✅ Chrome：151 及以上完整支持，117–150 为部分支持或默认禁用
- ✅ Edge：151 及以上完整支持，117–150 为部分支持或默认禁用
- ✅ Safari：27 及以上完整支持，26.0–26.6 为部分支持
- ⚠️ Firefox：尚未完整支持，145 起默认禁用，147–158 仍为部分支持
- ⚠️ Opera：仅部分支持，111–135 均为部分支持状态
- ❌ 完全不支持：IE、Opera Mini、UC Browser、QQ Browser、Baidu Browser、KaiOS 等
- 📱 移动端：Chrome for Android 152+、Android Browser 152 支持；Safari iOS 与桌面类似；Firefox for Android 仅部分支持
- 📦 相关资源：包含官方博客、Firefox 支持 bug 追踪、使用说明文章、Polyfill 及 WebKit 官方立场文档

---

### [我曾讨厌Tailwind CSS。以下是我改变想法的原因 — Yann](https://yannickkouakou.com/blog/why-i-hated-tailwind-css/?ref=tailwindweekly.com)

**原文标题**: [I used to hate Tailwind CSS. Here’s what changed my mind — Yannick Kouakou](https://yannickkouakou.com/blog/why-i-hated-tailwind-css/?ref=tailwindweekly.com)

作者曾因早期学习 CSS 的经历，对 Tailwind CSS 抱有五年以上的偏见；后来在法国留学和工作中被迫大量使用 Tailwind，加上深入理解其设计原理，最终彻底改变态度，并将 Tailwind 作为项目默认方案。以下为文章要点：

- 🧑‍🎓 作者从 14 岁起被导师严格要求先掌握 CSS 基础，因此一度把所有 CSS 框架视为“走捷径”，并由此产生敌意。
- 😠 他讨厌 Tailwind 的主要原因：违背“结构与样式分离”、周围人盲目追新，以及担心类名堆叠导致代码难以维护。
- 💼 搬到法国后，学校和学徒项目中每天都在使用 Tailwind，他不得不重新接触、在实战中放下成见。
- 📚 阅读 Adam Wathan 关于 utility classes 的文章、看 Fireship 视频后，他意识到 Tailwind 的底层逻辑，也看到 NASA、Vercel、ChatGPT 等大型项目都在使用它。
- 📉 最关键的认知转变：Tailwind 只生成实际用到的 CSS，页面再多最终样式表也很小，不会像传统 CSS 那样不断膨胀。
- 🧠 它同时解决了 CSS 中“命名困难”和“级联副作用”问题：一个类对应一条声明、特异性恒定，样式就近可见。
- ✅ 类名冗长其实依靠组件化解决：按钮等组件只需定义一次，其他地方直接使用组件变体即可，维护风险并不高。
- 🚀 如今 Tailwind 成为他的默认选择，因为它在速度、一致性、可维护性和生态（如 shadcn/ui）上都表现优异。
- 🗣️ 他会对过去的自己说：保持扎实学习 CSS，但别傲慢地贬低框架和使用者；框架不是敌人，只是工具。
- 💭 最终结论：很多看似坚定的技术偏见，其实源于从未真正实践；给讨厌的技术一次诚实尝试，可能会改变想法。

---

### [](https://adamwathan.me/css-utility-classes-and-separation-of-concerns/?ref=tailwindweekly.com)

**原文标题**: [CSS Utility Classes and "Separation of Concerns"](https://adamwathan.me/css-utility-classes-and-separation-of-concerns/?ref=tailwindweekly.com)

overview summary
作者從語意化 CSS 逐步轉向功能式／工具優先（utility-first）CSS，說明「分離關注點」並非二元對立，而應思考依賴方向。透過組合可重用類別、刪除多餘抽象，並以既有工具類別建構元件，能減少 CSS 膨脹、強化一致性，並避免過早抽象。

- 🧠 作者最早遵循「語意化 CSS」與分離關注點，但發現 CSS 仍高度依賴 HTML 結構，並非真正分離。
- 🔀 改用 BEM 後，CSS 與 DOM 結構脫鉤，但遇到相似元件（作者簡介 vs. 文章預覽）時，只能複製樣式或依賴 @extend，造成冗餘。
- 🧩 解決方案是建立「內容無關」的元件（如 .media-card），讓 CSS 重用，但也讓 HTML 依賴 CSS——關鍵在於取捨：要可換膚的 HTML，還是要可重用的 CSS？
- ⚖️ 所謂「分離關注點」不如思考「依賴方向」：CSS 依賴 HTML 時，CSS 不可重用；HTML 依賴 CSS 時，CSS 可重用但 HTML 不可隨意換膚。
- 🛠️ 作者選擇重用 CSS，開始建立內容無關的元件；元件越特定越難重用，於是以組合取代子元件。
- 📏 當元件只是為了「對齊」而存在時，可直接用工具類別（如 .align-left、.align-right）組合，避免無意義的抽象。
- 🧹 進一步刪除如 .actions-list 僅為排列子項的元件，改用間距工具類別（如 .mar-r-sm），讓 CSS 更小、類別更可重用。
- 🧱 最後進入「utility-first」階段：預先建立文字、顏色、邊框、背景、flex、間距等工具類別，不需新增 CSS 即可拼出新 UI。
- 🎯 工具類別提供固定選項（如 text-sm、py-3、text-dark-soft），避免開發者隨意取值，大幅減少樣式表中的顏色／字體尺寸數量。
- 🧬 仍應建立元件，但先以工具類別建構，等重複模式出現再萃取（如按鈕 .btn-purple），避免過早抽象與樣式表膨脹。
- 🚫 這不是 inline styles：工具類別限制了選擇範圍，強制一致性；inline styles 則是完全無限制的空白畫布。
- 📚 參考框架包括 Tachyons、Basscss、Beard、turretcss，作者並推薦自己的 Tailwind CSS。

---

### [Intrivio — 在线专业简历](https://intrivio.cv/?ref=tailwindweekly.com)

**原文标题**: [Intrivio — Professional CV & Resume Builder Online](https://intrivio.cv/?ref=tailwindweekly.com)

您没有提供需要总结的文本内容。请发送文章或文字材料，我会按照要求格式（概述 + 带 emoji 的“-”项目符号列表）用中文为您提炼要点。

---

### [渗透测试管理平台与自动化复测 - Rigma](https://rigma.io/en?ref=tailwindweekly.com)

**原文标题**: [Pentest Management Platform & Automated Retesting - Rigma](https://rigma.io/en?ref=tailwindweekly.com)

overview summary
Rigma 是 Mobeta（拥有超过 10 年渗透测试经验）推出的漏洞管理平台，旨在弥补传统渗透测试在提交报告后即结束的缺陷。通过集中管理、自动化复测和实时 KPI 跟踪，Rigma 将渗透测试转化为持续的安全监控流程，并符合 NIS2、DORA、ISO 27001 等主流标准。

- 🎯 **核心定位**：将传统一次性渗透测试升级为持续监控和可量化的安全修复流程。
- 📄 **传统痛点**：PDF 报告易被遗忘、缺少修复证明、复测成本高昂、结果分散、无法提供管理层所需指标。
- ⚙️ **三步工作流**：导入既有渗透测试（PDF/CSV等）→ 自动重测漏洞 → 实时追踪修复状态与合规指标。
- 🤖 **自动化复测**：脚本自动验证漏洞修复状态，无需人工干预，支持无限次重测。
- 💶 **成本效益**：每次自动化复测可节省约 1,000 欧元；平均多修复 30% 的漏洞，而手动复测后 50% 漏洞仍未修复。
- 📊 **可视化与管理**：提供实时仪表板、集中化标准化漏洞结果，以及适用于 COMEX/管理层的 KPI。
- 🔐 **合规与安全**：符合 NIS2、DORA、ISO 27001 和 HDS；数据托管在法国 Scaleway，使用开源 AI 模型，满足 GDPR。
- 🏅 **资质与认可**：审计团队持有 OSCP 与 OSWE 认证；入选 2025 法国网络安全创新雷达；已被 20 多家企业采用。
- 🧩 **兼容性**：可导入 Mobeta 或其他供应商的渗透测试报告，实现漏洞统一管理。
- 🏢 **部署方式**：SaaS 即时开通；On-Premise 版本仅需两条 Docker 命令即可在 5 分钟内完成部署，并支持内网（如 Active Directory）漏洞复测。
- 💰 **价格方案**：免费 14 天试用；Standard 100 欧元/月；Pro 200 欧元/月；Enterprise 定制报价。
- 🎟️ **Credit 机制**：1 credit = 100 欧元，可对一个漏洞进行不限次数自动重测；Mobeta 客户执行渗透测试时免费获得 credits。
- 📅 **演示与 FAQ**：提供 15 分钟个性化演示、无强制承诺；Rigma 不替代内部工单系统，而是与之互补，负责技术验证并提供高层 KPI。

---

### [获取失败](https://nolanlawson.com/2026/08/23/the-asteroid-currently-hitting-frontend-web-development/?ref=tailwindweekly.com)

**原文标题**: [Failed to retrieve](https://nolanlawson.com/2026/08/23/the-asteroid-currently-hitting-frontend-web-development/?ref=tailwindweekly.com)

无法总结：获取内容失败，状态码 403。

---

### [Ente Photos：以绝对隐私存储和分享你的照片](https://ente.com/?ref=tailwindweekly.com)

**原文标题**: [Ente Photos: Store and share your photos with absolute privacy](https://ente.com/?ref=tailwindweekly.com)

overview summary  
Ente 是一款注重隐私的云端照片备份与管理服务，主打端到端加密、跨平台支持和开源属性，提供免费与付费方案，并因安全性和易用性备受用户好评。

- 🔐 提供端到端加密备份，照片存储在 3 个不同位置，确保数据安全与隐私。  
- 📱 支持 Android、iOS、Web、Mac、Linux、Windows 及命令行工具，所有应用均开源。  
- 🧠 具备设备端人脸识别、自然语言搜索、智能相册和精选回忆等 AI 功能。  
- 👨👩👧👦 支持家庭共享计划（最多 5 人），成员拥有独立私密空间，不额外收费。  
- 🆓 免费方案提供 10GB 永久存储；付费方案从 50GB 到 2TB，价格具竞争力。  
- 🎁 推荐计划可为邀请双方各增加 10GB 免费存储。  
- 🔄 支持从 Google 和 Apple 轻松迁移照片，也可方便导出。  
- 🌐 可通过公开链接或共享相册与他人协作，上传内容同样经过端到端加密。  
- 🛡️ 开放源码并经过密码学审计，无广告、不监视、不训练用户数据。  
- ⭐ 大量用户评价其为最佳 Google Photos 隐私替代品，称赞界面美观、功能强大、开发团队响应迅速。  
- 🐣 “Ente” 在马拉雅拉姆语中意为“我的”，在德语中意为“鸭子”，品牌形象可爱且富有深意。

---

### [](https://github.com/benface/monowind?ref=tailwindweekly.com)

**原文标题**: [GitHub - benface/monowind at tailwindweekly.com · GitHub](https://github.com/benface/monowind?ref=tailwindweekly.com)

monowind 是一个开源库，用于使用普通 HTML 和 Tailwind 工具类在 Web 上构建文本用户界面（TUI）。它通过 `<mono-wind>` 自定义元素将 DOM 渲染为严格的字符网格，同时保留原生链接、按钮、表单、焦点和无障碍语义；支持 React、Svelte、Solid、Vue 等任意框架。项目当前处于早期开发阶段，已包含多种布局引擎、合成指针状态、ASCII 艺术组件、可定制主题及丰富的示例与自动化开发流程。

- 🧩 **基于 HTML/Tailwind 构建 TUI**：用普通标记和 Tailwind 类编写界面，`<mono-wind>` 渲染为精确字符网格，保持原生控件可用。
- 📐 **广泛的布局支持**：已实现 block、flex、grid（含 subgrid 和命名区域）、多列（columns、平衡、列规则）以及表格布局，支持边框合并、单元格间距和滚动容器。
- 🖱️ **合成 hover/active 状态**：非交互元素在网格模式下无真实指针目标，引擎通过在剪贴板布局上做命中测试让 `hover:`、`active:`、`group-*`、`peer-*` 及 `cursor-*` 照常生效；只有事件处理与 title 提示需要显式添加 `pointer-events-auto!`。
- 🅰️ **ASCII 艺术横幅**：`@monowind/ascii` 提供 `<mono-ascii>` 组件，可渲染 FIGlet/TOIlet 横幅文本，自带 44 款许可字体，支持 SGR 颜色与彩虹/金属等动效，并保持语义字符串可被屏幕阅读器访问。
- 🎨 **复古主题系统**：`@monowind/themes` 提供 DOS、C64、绿色磷光、琥珀色、电传打字机、BBS 等拟真主题，每个 Tailwind 颜色被量化到该系统真实调色板，并用时代正确的边框字符，也可按 CSS 契约自定义主题。
- 📂 **Monorepo 结构**：基于 pnpm workspaces，核心代码在 `packages/`，应用（Storybook、Playground、示例）在 `apps/`，AI 代理设计文档位于 `.agents/`，README 有完整开发说明。
- 🚀 **丰富演示与示例**：Storybook 展示所有支持特性，Playground 提供可分享 URL 的实时编辑器，并包含 HTML、Tailwind、Vite、React、Solid 等不同消费方式的示例应用。
- ⚙️ **自动化开发流程**：提供 `pnpm install`、`dev`、`check`、`test`、`test:visual`、`build` 等命令，覆盖 lint、格式化、类型检查、单测、Golden 测试、视觉回归及依赖更新。
- 📝 **开源协议**：项目采用 MIT 许可证，目前为早期开发状态，代码托管在 GitHub，包含完整 README、折叠结构与资源入口。

---

### [](https://play.monowind.benface.com/?ref=tailwindweekly.com)

**原文标题**: [monowind play](https://play.monowind.benface.com/?ref=tailwindweekly.com)

您所给的内容只有一个词“tidy”。它通常表示“整洁、有条理”，也可作为动词指“整理、收拾”，核心含义与秩序和清爽相关。

- 🧹 作为形容词，形容房间、桌面等干净整洁，如 a tidy room。  
- 📦 作为动词，常搭配 tidy up，指把物品归位、清理杂乱。  
- 🏠 它广泛用于家居与办公场景，是维持良好环境秩序的重要概念。  
- 💰 在非正式表达中可引申为“可观的”，如 a tidy sum（一笔不小的金额）。  
- 🔄 将 tidying 变成日常习惯，有助于减少混乱、提升专注力与生活效率。

---

### [](https://windybase.com/?ref=tailwindweekly.com)

**原文标题**: [WindyBase - Explore free and premium Tailwind CSS templates ](https://windybase.com/?ref=tailwindweekly.com)

overview summary
WindyBase 是一个面向开发者的 Tailwind CSS 模板与工具目录，每周精选免费及付费资源，涵盖落地页、SaaS、博客、仪表盘、组件库和电商等多类模板。

- 🎯 核心定位：WindyBase 为现代开发者提供精选 Tailwind CSS 模板、组件和工具，支持高效搭建网站与应用。
- 🗂️ 分类丰富：包含 Landing Page、SaaS、Blog、Dashboard、E-commerce 等模板，以及独立组件库专区。
- 💰 免费与付费并存：多数模板/组件提供免费版本，付费项目价格从 $14 至 $249 不等，适配不同预算需求。
- 🧩 热门产品示例：展示 Voyager、Atlas、Nova、Galaxy、HyperUI、Mamba UI、Cleopatra 等资源，附实时预览与购买入口。
- 📬 邮件订阅：用户可通过订阅获取新模板和组件更新通知，并需邮件确认。
- 🌐 站点功能齐全：支持分类浏览、提交资源、联系与法律条款页面，并设有社交媒体链接。

---

### [Frame0 ― 一款用于](https://frame0.app/?ref=tailwindweekly.com)

**原文标题**: [Frame0 ― A sleek Balsamiq alternative for wireframing](https://frame0.app/?ref=tailwindweekly.com)

Frame0 是一款专注于快速创建手绘风格线框图的工具，旨在帮助用户从创意直接过渡到可视化原型，并通过 AI、丰富素材与多功能导出提升效率。

- ✏️ 能从想法快速生成手绘风格线框，无需在样式与像素上花费过多精力。
- 🤖 内置 AI Agent，支持聊天创建线框并转代码，可接入 OpenAI、Anthropic、Gemini 或 Grok，也可通过 MCP 服务端用于 Claude/Cursor 等。
- 🧩 提供覆盖桌面、移动、智能手表和 Web 的丰富 UI 组件库，包含按钮、表单、导航、卡片、弹窗及可调状态。
- 🎨 包含 1,500+ 手工转换自 Lucide 的草图风图标，保持视觉一致。
- 🔁 支持帧镜像功能，主帧更新时所有镜像同步，适合重复元素（如页眉、导航栏）。
- 🖇️ 可将图元链接到其他页面，并通过演示模式以幻灯片方式展示用户流程。
- 📑 内置多种设备模板（Web、桌面、手机、平板等），提供常见布局以快速起步。
- 📤 支持将可交互原型导出为单个 HTML 或 PDF 文件，便于分享反馈，无需安装软件。
- 📊 也能创建流程图、UML（用例图、类图）和 ER 图，将设计文档集中在一处。
- ⚙️ 全面功能包括跨平台支持、深色模式、形状锁定/解锁、PNG/SVG/JPEG/WebP 图片导出及手绘涂鸦。
- 👍 用户评价称其像 Balsamiq 结合 Figma 的优点，尤其适合离线使用且速度流畅，显著节省线框制作时间。

---

### [Irid - Mac 的设计工具栏](https://irid.app/?ref=tailwindweekly.com)

**原文标题**: [Irid - a design toolbar for Mac](https://irid.app/?ref=tailwindweekly.com)

这是一款专为 macOS 设计的屏幕设计与开发辅助工具栏，将取色、测量、网格对齐和设计稿对比等功能整合在一个应用中，帮助用户快速检查布局和像素级还原设计，目前处于免费早期访问阶段。

- 🎨 屏幕取色器：支持任意格式取色，一键复制到剪贴板或存入调色板库，方便后续使用。
- 📏 尺寸测量：快速测量屏幕元素间的距离，或拖动测量任意区域的大小，用于确认布局尺寸。
- 🔲 网格辅助：可在任何窗口上叠加网格，快速检查间距与对齐是否准确。
- 🖼️ 设计叠加：将设计稿以任意透明度固定在实时应用上方，逐像素比对，发现偏离原稿的位置。
- 💬 用户好评：获得设计团队负责人推荐，称其比 Chrome 扩展更便捷、易用，无需依赖多个插件。
- ⌨️ 快捷操作：取色、测量、网格等常用工具均可通过键盘快捷键随时调用，提升效率。
- 💻 兼容平台：提供 Apple Silicon 原生版本和 Intel 构建版本，适用于 macOS 12 及以上系统。
- 🆓 免费获取：早期访问阶段完全免费，可下载试用。
- 📬 更新订阅：可留下邮箱获取版本发布说明、新工具和修复信息，承诺无垃圾邮件且保护隐私。

---

### [Supaste — Mac 剪贴板历史管理器](https://www.supaste.com/?ref=tailwindweekly.com)

**原文标题**: [Supaste â Clipboard History Manager for Mac](https://www.supaste.com/?ref=tailwindweekly.com)

您似乎没有附上需要总结的文本内容。请提供文章或段落，我会按照“概述摘要 + Emoji 项目符号”的模板为您生成中文总结。

---

