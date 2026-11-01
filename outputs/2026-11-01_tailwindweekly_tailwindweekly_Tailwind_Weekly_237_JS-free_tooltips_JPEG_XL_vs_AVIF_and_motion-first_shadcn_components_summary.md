### [](https://github.com/heroui-inc/tailwind-variants?ref=tailwindweekly.com)

**原文标题**: [GitHub - heroui-inc/tailwind-variants at tailwindweekly.com · GitHub](https://github.com/heroui-inc/tailwind-variants?ref=tailwindweekly.com)

tailwind-variants 是面向 Tailwind CSS 的一等变体 API，提供类型安全、框架无关的变体、slots 与组合能力，并内置类名冲突解析；支持 Tailwind CSS v4，并提供默认版、config 和 lite 等入口。

- 🦄 核心特性：一等变体 API、slots、组合与多重 extend、完整类型、框架无关、内置冲突解析、实验性调试、Tailwind CSS v4 支持。
- 📦 安装方式：支持 npm、yarn、pnpm 安装；需要更小包且不需要冲突解析时，可从 `tailwind-variants/lite` 导入。
- 🚀 快速开始：通过 `tv({ base, variants, compoundVariants, defaultVariants })` 定义组件，调用时传入变体参数生成最终类名。
- ⚔️ 冲突解析：默认入口内置合并表与单遍引擎，`tv`、`cn`、`twMerge` 共用；导出 `twMerge`、`twJoin`、`clsx` 等兼容名称，可别名 `tailwind-merge` 和 `clsx`。
- ⚡ 性能表现：`cn()` 在连接合并和唯一任意值场景较 3.3.1 提升约 3×/2×；热路径 `tv()` 约快 1.6×–2×，但创建组件比 `cva` 慢。
- 🧩 组件组合：`extend` 可合并一个或多个父 recipe，数组从左到右合并且子选项优先；variants、slots、默认值和 compound 会深合并。
- 🛠️ 自定义配置：自定义工具类需使用 `tailwind-variants/config`，支持 `extend`/`override`、`twMergeConfig`、`createTV`、`extendTailwindMerge`、`createTwMerge` 等。
- 🧪 调试能力：`debug: true` 可在浏览器控制台查看类名解析与合并丢弃情况，生产构建会 tree-shake；lite 入口不支持 debug。
- 🔧 工具函数：`cx` 仅拼接，`cn` 拼接并按默认配置合并，`cnMerge` 支持按调用传配置；lite 中 `cn` 只拼接，可用 `createCN({ twMerge })` 绑定合并器，也可用 `{ twMerge: false }` 禁用合并。
- ⚠️ 已知限制：不支持 `experimentalParseClassName`；`twMerge` 接受字符串和嵌套数组，对象语法属于 `cn`/`clsx`；Tailwind v4 移除了响应式变体，需手动添加响应式类。
- 📚 文档与社区：完整文档位于 tailwind-variants.org，项目采用 MIT 许可，欢迎通过 Discord、Twitter、GitHub Discussions 和贡献指南参与。

---

### [fluttersdk_wind 更新日志 | Flutter 包](https://pub.dev/packages/fluttersdk_wind/changelog?ref=tailwindweekly.com)

**原文标题**: [fluttersdk_wind changelog | Flutter package](https://pub.dev/packages/fluttersdk_wind/changelog?ref=tailwindweekly.com)

overview summary  
fluttersdk_wind 1.11.0 是 Flutter 的 Tailwind CSS 风格 UI 工具包更新日志，涵盖从 1.11.0 到 1.0.0 的多个版本，重点增强响应式窗口尺寸类、图片定位、本地化数字输入、无障碍语义、性能计数与文档链接检查，并修复大量布局、焦点、主题透明色和键盘避让问题。

- 📐 1.11.0 新增 `wWindowClassOf(context)`，按窗口宽度返回 compact/medium/expanded，用于选择导航栏或侧边栏，不再依赖平台判断。
- 🖼️ 1.10.0 为 `WImage` 新增 `object-position` 类（如 `object-top`），支持九种对齐方式，避免裁剪时丢失重要区域。
- 🔢 `WInput`/`WFormInput` 新增 `decimalSeparator`，支持逗号等本地化小数分隔符，默认仍为点号。
- ♿ 1.9.3 修复 `WSelect` 语义节点重复问题，关闭状态只发布一个可点击按钮节点。
- 🏷️ 1.9.2 `WSelect` 的无障碍名称改为跟随选中项标签，空状态才使用占位符。
- 🔘 1.9.1 修复 `WButton` 在无回调、禁用或加载状态下的按钮语义，确保辅助技术正确识别。
- 📏 1.9.0 破坏性行为变更：`tracking-*` 改为 em 单位，字母间距随字体大小缩放；同时修复 `WButton` 透明度、`ring-*` 轮廓绘制和 `WPopover` 键盘操作。
- 🧭 1.8.x 修复 `WPopover` 高度限制与滚动、`WSelect` 重新打开时的异步响应竞争、圆角溢出边框裁剪、`WDiv` 焦点行为等。
- 🎨 1.7.0 新增 `contrastRatio` 与 `contrastForeground`，用于 WCAG 对比度计算和前景色选择。
- 🧹 1.6.x 修复 `bg-transparent` 等透明色解析、任意十六进制颜色 alpha、聚焦输入框键盘避让、圆角裁剪抗锯齿等。
- ⌨️ 1.5.x 改进键盘/电视遥控器激活、焦点环层级、`h-full` 渲染层实现、`gap-*` 使用 `Flex.spacing` 减少包装组件。
- 🧪 1.4.x 新增 `skills/wind-ui/references/design-culture.md` 设计品味参考，修复 `capitalize` 按单词首字母大写及土耳其语本地化大小写。
- 📅 1.3.0 `WDatePickerMode.dateTime` 支持选择日期和时间，新增时间行、分钟步长和最小/最大时间约束。
- 🧱 1.2.x 新增 `WBadge`、`WCard`、`WSwitch`、`WRadio`、`WTabs`、`WindRecipe`、`size-*`、`cursor-*` 等，并改进 `grid items-stretch` 等高行。
- 🎉 1.0.0 首个稳定版，包含 22 个公共组件、19 个 className 解析器、主题系统、响应式/暗色模式前缀、无障碍语义和调试桥接。

---

### [获取失败](https://www.npmjs.com/package/shadcn?ref=tailwindweekly.com)

**原文标题**: [Failed to retrieve](https://www.npmjs.com/package/shadcn?ref=tailwindweekly.com)

无法总结：获取内容失败，状态码 403。

---

### [免费 Shadcn UI 组件、区块、图标、模板和 MCP - ReUI](https://reui.io/?ref=tailwindweekly.com)

**原文标题**: [Free Shadcn UI Components, Blocks, Icons, Templates & MCP - ReUI](https://reui.io/?ref=tailwindweekly.com)

ReUI 是面向 shadcn/ui 的设计优先平台，提供 MCP、Agent Skills 与精选注册表，帮助 AI 代理从提示词快速推进到生产级 React + Tailwind 应用。

- 🧩 提供 1,264 个免费 shadcn/ui 组件和 27 个 ReUI 自定义 primitives，采用 MIT 许可，永久免费，可通过 shadcn CLI 安装并自由修改。
- 📦 提供 672 个 Pro 区块，覆盖 7 大组、79 个分类，涵盖应用外壳、仪表盘、数据网格、认证、电商、营销等场景。
- 🤖 免费 ReUI MCP 与 Agent Skills 可让 Codex、Claude、Cursor、Copilot 等编码代理使用真实组件、区块、图标及其 API，减少“AI 生成式 UI”的不可靠问题。
- 🎨 提供 667 个手工制作的付费动画图标，包含 4 种风格、2,668 个变体，并提供多页面 Starter Templates。
- ✅ 获得 shadcn/ui 创作者推荐，被称为可信注册表之一。
- ♿ 基于 Radix UI，内置 WAI-ARIA、键盘导航、焦点管理和屏幕阅读器支持；支持 shadcn 主题变量、暗色模式与运行时主题定制。
- 🛠️ 通过 CLI 将源码复制到项目中，无运行时依赖和版本锁定；安装后可自由修改，并提供更新与分级支持。
- 💳 免费组件永久免费；Pro 全访问一次性 $249，包含终身更新和无限项目授权。
- 👥 已有 5,600+ 开发者和团队使用，社区反馈集中在数据网格、表单、拖拽与 Gantt 等组件。
- 🚀 最新更新提及新增 66 个免费组件、7 个 Pro 区块和 29 个图标。

---

### [Aceternity UI —— React 与 Tailwind CSS 组件库](https://ui.aceternity.com/?ref=tailwindweekly.com)

**原文标题**: [Aceternity UI â React & Tailwind CSS Component Library](https://ui.aceternity.com/?ref=tailwindweekly.com)

该内容介绍 Marquee 设计工具的产品落地页，采用浅色与深色主题，并包含实时画布首屏、注册与导览弹窗、功能展示、定价与转化模块。

- 🎨 Marquee 是运行在代码库上的设计工具，落地页提供浅色与深色两种主题。
- 🖼️ 首屏使用实时设计画布 Hero，并配有带图层选择功能的 Logo 导航栏。
- 📝 页面包含注册弹窗与导览弹窗，帮助用户快速开始并了解产品。
- ☁️ 设有 Logo 云、功能展示、交接（Handoff）与评审评论等模块。
- 💬 通过用户评价与定价方案增强信任并引导转化。
- 📣 包含行动号召（CTA）与页脚，完善整体转化路径。
- 👀 提供实时预览，并可获取代码。

---

### [适用于 React、Next.js 和 React Native 的动画组件 · beUI](https://beui.dev/?ref=tailwindweekly.com)

**原文标题**: [Animated Components for React, Next.js and React Native · beUI](https://beui.dev/?ref=tailwindweekly.com)

overview summary
- 🧩 beUI 是面向 React、Next.js 与 React Native 的动画组件库，主打复制即用、免费开源、完全可定制，提供约 151 个 React 组件和 72 个 React Native 组件。
- ⚙️ 基于 Motion 与 Tailwind CSS 构建，Web 端通过 shadcn 分发；支持 bun、npm、pnpm、yarn 安装，例如 `bunx --bun shadcn add @beui/timeline`，也可手动复制源码。
- 📱 beUI Native 使用 Reanimated、Gesture Handler、Uniwind 为触控场景重建组件，支持 Expo 与裸 React Native；可通过 `npx beui-native add button` 添加，并能在 Expo Go 中扫码预览。
- ✨ 组件覆盖按钮、模态、Toast、Dock、Tabs、Dynamic Island、命令面板、Bottom Sheet、图表、文本/数字动画、主题切换、OTP 输入、滑动列表、Bloom Menu 等。
- 🚀 beUI Pro 提供 350+ 高级区块、完整落地页模板、动画插画、Agent Skill/MCP、私有 registry 与终身更新；免费库为 MIT 许可，可用于商业项目，Pro 另需付费授权。
- 🧱 使用环境建议 React 19、Tailwind CSS 4 与 Motion；组件源码在项目中，可自定义样式、动效和行为，并接入自有主题令牌。
- 💬 用户评价集中称赞动画流畅、交互设计细致、视觉干净，并有人表示会立即用于产品或已长期使用。
- 🔗 页面还包含 FAQ、组件/区块/AI/图表分类导航、更新日志、GitHub、主题与动效模式等资源入口。

---

### [assistant-ui · 面向 AI 智能体的前端库](https://www.assistant-ui.com/?ref=tailwindweekly.com)

**原文标题**: [assistant-ui · The frontend library for AI agents](https://www.assistant-ui.com/?ref=tailwindweekly.com)

assistant-ui 是一个面向 AI 智能体的前端库，提供构建生产级聊天界面的基础原语与运行时，可通过适配器接入任意后端，并内置流式传输、工具调用等完整客户端能力。

- 🚀 定位为 AI 智能体的前端库，提供原语与运行时，适用于生产环境聊天场景
- 🔌 后端无关：通过适配器兼容 AI SDK、LangGraph、LangChain、Mastra 及自定义后端
- ⭐ 社区热度高：拥有 12.9k GitHub Stars 和 280 万次周下载量，并获得 Y Combinator 支持
- 🧠 运行时统一管理线程、流式响应与工具调用，仅需一个 Provider、一个 Hook 和一个组件
- 🧩 组件完全可组合，CLI 可将 UI 源码复制到你的仓库，便于自由改造界面
- 📦 同时支持 React、Native 与 Ink 多端运行
- ⚙️ 内置流式传输、推理、工具、审批、来源、附件、分支、建议、语音、生成式 UI 等能力
- ☁️ 提供 Cloud 托管线程与持久化，实现跨刷新会话保持与上下文累积
- ⚡ 快速上手：新项目运行 `npx assistant-ui@latest create`，现有项目运行 `init`
- 📜 采用 MIT 许可证，当前版本为 @assistant-ui/react@0.15.32

---

### [Shadcnblocks shadcn/ui 区块与组件](https://www.shadcnblocks.com/?ref=tailwindweekly.com)

**原文标题**: [Shadcnblocks shadcn/ui blocks & components](https://www.shadcnblocks.com/?ref=tailwindweekly.com)

Shadcnblocks 于 2026 年 10 月 30 日发布更新，新增 406 个区块；平台面向 shadcn/ui、Tailwind 与 React，提供 2636 个区块、2241 个组件和 21 个模板，支持复制粘贴或通过 Shadcn CLI 安装。

- 🚀 新增 406 个区块，覆盖 Dashboard、Hero、Application Shell、Feature、Contact 等分类，并标注了多项新增数量。
- 🧱 提供 2636 个 Shadcn 区块，适合快速搭建落地页、营销页和后台界面。
- 🧩 包含 2241 个 Shadcn UI 组件，均有文档、安装说明和使用示例。
- 🖼️ 提供 21 个高级模板，基于 Next.js 与 Astro，多数定价 $79，Shadcn Admin Kit 为 $129。
- ⚛️ 作为 React UI 库，兼容 Next.js、Vite、Astro、Remix，并支持 Radix UI、Base UI、React Aria 三种底层实现，一个区块 ID 对应三种构建。
- 🎨 提供 39 个 Shadcn 主题，可通过 CSS 变量应用到区块、组件和页面，支持明暗模式与自定义字体。
- 🛠️ 提供 Shadcn Figma Kit 与 Admin Kit：Figma Kit 含全部组件和 579 个区块设计；Admin Kit 为 219 页 Next.js 16 管理后台。
- 🧑‍💻 新增 Shadcn Page Builder 与 IDE 扩展，可在浏览器拖拽搭建页面，或在 VS Code、Cursor、Windsurf 中搜索、预览并一键安装区块。
- 📦 支持多种安装方式：Shadcn CLI、Shadcn MCP（AI 自然语言安装）、IDE 扩展和 Shadcnblocks App。
- 💳 终身方案定价为 Pro $149、Premium $299、Elite $399；高阶方案包含模板、Figma Kit、Admin Kit，Elite 另含 97+ 预构建页面和页面构建器。
- 📈 平台数据：22162 名免费用户、5420 名 Pro 客户、约每天 10000 次安装；2023 年成立，每月新增 50+ 组件、100+ 区块、10+ 页面、1+ 模板。
- 🆓 可先浏览免费区块，基础层级区块登录后即可使用。

---

### [Mirror：编辑风格 Ghost 主题](https://redpixelthemes.gumroad.com/l/mirror?ref=tailwindweekly.com)

**原文标题**: [Mirror: Editorial Ghost Theme](https://redpixelthemes.gumroad.com/l/mirror?ref=tailwindweekly.com)

未提供可总结的文章内容，因此无法生成准确的要点摘要。
- 📄 请补充需要总结的文本内容
- ✍️ 收到内容后将按“概述+表情符号要点”格式整理
- 🔍 摘要将突出关键信息与核心结论

---

### [面向 Web 使用场景的 JPEG XL 与 AVIF 对比 - JakeArchibald.com](https://jakearchibald.com/2026/jpeg-xl-vs-avif/?ref=tailwindweekly.com)

**原文标题**: [JPEG XL vs AVIF for web use-cases - JakeArchibald.com](https://jakearchibald.com/2026/jpeg-xl-vs-avif/?ref=tailwindweekly.com)

本文用照片、截图、插画、透明图、HDR、大/小图、无损和动画等案例，比较 JPEG XL（libjxl、jixel）与 AVIF 在网页场景中的文件大小、编码/解码速度、内存、渐进式加载和兼容性。总体结论是：网页有损内容默认优先 AVIF 4:4:4；JPEG XL 在无损、JPEG 转码和少数特殊图片上更有优势，但最终应用自己的图片实测。

- 📅 文章发布于 2026-10-15，称 JPEG XL 已进入所有主流浏览器；测试基于 M4 Pro，图片宽度多为 1598px。
- 📉 有损照片：AVIF 几乎总是比 JPEG XL 文件更小；默认设置下最佳 JPEG XL 约大 15–25%，最高努力下约大 6–20%，但存在个别反例。
- 🧩 JPEG XL 编码器差异很大：jixel 通常比 libjxl 更小，但有时会“刷指标”且视觉更差；透明细节是例外。
- 🖼️ 截图/插画：AVIF 明显更好；等效 JPEG XL 在默认努力下大约 30–90%，最高努力下大约 20–70%。
- 🪟 透明图：AVIF 明显更好；libjxl 默认大 31–44%、最高大 61–70%；jixel 因透明通道无损编码，文件可达 AVIF 的 2–3 倍。
- ⚡ 速度与内存：综合文件大小，AVIF 通常编码更快、内存更少、解码更快；jixel 默认编码可能更快但文件明显更大；JPEG XL 中高质量解码常慢 2–3 倍，极高码率差距缩小，Chrome 有时更快。
- ⚙️ 努力程度：AVIF 和 jixel 提高努力通常值得；libjxl 高努力很慢、内存高且收益很小，甚至文件更大。
- 🎨 AVIF 4:2:0 不应默认使用：很少显著减小文件，还更难达到高质量；除非同时测试，否则建议 4:4:4。
- ✅ 质量设置总体可靠：同一质量值下不同图片质量会波动，但各编码器变化方向一致，未发现单一质量设置有明显风险。
- 🌀 渐进式加载：JPEG XL 的 progressive DC 在高努力下几乎免费，jixel 默认反而大 12%；AVIF 渐进式目前仅 Chrome 支持、Firefox 进行中，更复杂但可控、通常更小且解码更快。
- 🌈 HDR：JPEG XL 格式支持 gain map，但浏览器解码器不支持且编码流程混乱；AVIF 支持 gain map，在极端亮度下体验更好；非 gain map HDR 下指标分歧大，但 JPEG XL 可能更小。
- 🔁 JPEG 转码：JPEG XL 可把现有 JPEG 无损缩小 9–20%，大图在 Chrome/Safari 解码更快，小图略慢；jixel 输出比 libjxl 稍慢。
- 🗜️ 无损压缩：JPEG XL 明显胜出；无损 WebP 照片大 9–17%，无损 AVIF 大 30–120%；但网页几乎不需要无损，且 jixel 高努力无损解码可能很慢。
- 🎞️ 动画：作者认为动画图片格式很不明智；同质量下动画 AVIF 725kB，而 JPEG XL 2.17MB 且噪点更多；视频应使用视频格式。
- 🧭 当前建议：网页默认用 AVIF 4:4:4，并选可接受的最高努力；若 AVIF 文件异常大，再用 jixel 的 JPEG XL 试；不要轻信 AI/传言，用自己的图片测试，且两者近期进步很快，建议可能变化。

---

### [](https://allthingssmitty.com/2026/10/05/css-does-your-tooltip-positioning-now/?ref=tailwindweekly.com)

**原文标题**: [
    CSS does your tooltip positioning now - Matt Smith
  ](https://allthingssmitty.com/2026/10/05/css-does-your-tooltip-positioning-now/?ref=tailwindweekly.com)

本文介绍了 CSS 锚点定位如何原生处理 tooltip、脚注、弹出层等元素的定位，减少对 JavaScript、监听器和定位库的依赖，同时说明了实际使用中的命名、兼容性、可见性切换和无障碍注意事项。

- 📌 通过 `anchor-name` 和 `position-anchor` 可以让元素相对指定锚点定位，浏览器会在滚动或窗口尺寸变化时自动重新计算位置。
- 🧭 锚点定位仅适用于已经使用 `absolute` 或 `fixed` 定位的元素；`position-area` 可直接描述在锚点的上方、下方、侧边等位置，无需手写偏移计算。
- ⚠️ `anchor-name` 不需要全页面唯一，但必须确保每个锚点与其目标匹配；在卡片网格等重复组件中应按实例生成名称，避免多个 tooltip 错误绑定到同一锚点。
- 🔄 `position-try-fallbacks: flip-block, flip-inline` 可在空间不足时自动翻转位置，替代过去用 resize/scroll 监听器检测溢出并重新定位的做法。
- 🪟 与原生 `popover` 结合可快速实现下拉菜单：获得顶层渲染、无需处理 `z-index`，并支持点击外部关闭。
- 📏 使用 `anchor-size(width)` 可让下拉菜单宽度直接匹配触发按钮宽度，无需 JavaScript 测量和设置内联样式。
- 🧩 锚点定位只解决“显示在哪里”，不解决“何时显示”；若非兄弟元素需要联动显隐，可在共同祖先上使用 `:has()`，或结合 popover/少量 JavaScript。
- 🧠 经验法则：需要相对特定元素定位时优先用 `anchor-name`/`position-anchor`；只需相对自身容器定位时，用 `position: absolute` 配合 `position: relative` 父元素即可。
- 🌐 当前 Chrome、Firefox、Safari、Edge 支持较好，但 Safari 与 Chrome 在部分回退定位边界情况上存在差异，`popover` 默认 margin 也可能干扰锚点定位，建议保留 `@supports not (anchor-name: --a)` 回退。
- ♿ 锚点关系主要是视觉关系，屏幕阅读器仍按 DOM 顺序播报；`aria-describedby` 只能部分弥补，不能把该特性当作完整的无障碍方案。

---

### [我太常看到的5个CSS犯规 - YouTube](https://www.youtube.com/watch?v=J_cnZa6UzVI&ref=tailwindweekly.com)

**原文标题**: [5 CSS fouls that I see way too often - YouTube](https://www.youtube.com/watch?v=J_cnZa6UzVI&ref=tailwindweekly.com)

该文本是 YouTube 网站页脚信息，主要包含站点导航、政策与帮助链接，以及 Google 的版权声明。

- 🧭 基础导航包括“关于、新闻、版权、联系我们”等链接。
- 👥 提供“创作者、广告、开发者”等入口。
- 📜 包含“条款、隐私、政策与安全”等政策相关链接。
- ⚙️ 包含“YouTube 运作方式、测试新功能”等功能说明。
- ©️ 页面底部标注版权归属：© 2026 Google LLC。

---

### [超级专注 | 要做](https://www.superfocus.me/go/lp1?ref=tailwindweekly.com)

**原文标题**: [Superfocus | Too much to do, not enough time?](https://www.superfocus.me/go/lp1?ref=tailwindweekly.com)

Superfocus 是一款科学支持的生产力系统，面向“事情太多、时间不够”的人群，目标是把时间与精力聚焦在真正重要的目标上，避免过度忙碌和倦怠；它定位为“教练”而非又一个待办清单，已吸引 1,000+ 创始会员，并提供限时创始优惠与 30 天无理由退款保障。

- 🎯 核心痛点：待办事项多达 40 项、日历排满会议，却不知道真正重要的工作何时进行；反复更换 Notion 模板和整理系统只是“假进步”。
- 🧭 产品定位：Superfocus 会围绕本季度重要目标规划时间、保护专注、在计划被打乱时调整，并诚实反馈进度。
- 🪜 三步方法：先明确未来 90 天目标并排序拆解，再把目标转化为可执行的周计划，最后通过每周复盘检查目标达成情况。
- ⏱️ 专注与整合：提供专注时段、屏蔽干扰应用、播放专注音乐、同步 Slack 状态，并支持 Google、Apple、Outlook 日历及 Web、Mac、iPhone。
- 📊 问责机制：每周评估各目标达成概率，分析哪些工作带来能量或消耗能量，并可由教练建议和经同意后调整计划。
- 💬 用户反馈：创始会员称其帮助自己更关注时间分配、保护注意力、聚焦业务和优先事项，并认为是最有效的规划与时间管理工具之一。
- 🧠 科学背景：基于实施意图、时间块、反馈循环和注意力管理等证据支持原则，由 Ali Abdaal 与团队转化为日常实践。
- 💰 创始优惠：创始会员价格为 199 美元/年，约每周不到 4 美元，并永久锁定；创始期结束后常规价为 299 美元/年，优惠即将结束。
- 🛡️ 风险保障：提供 30 天全额退款保证，无需填表或电话，发邮件即可退款。
- 🔌 工具关系：不替代待办清单、日历、Notion 或现有笔记工具，而是连接日历与 Slack，解决“时间是否指向目标”的问题。
- 🤖 与普通 AI 排程区别：不是把整天交给容易因会议变动而失效的算法，而是帮助用户判断什么重要、现实地规划，并与用户一起调整。
- ✅ 低维护成本：核心习惯是每周约 5 分钟复盘，而非每天 20 分钟、忙起来就会被放弃的仪式；系统设计为安静运行、不增加管理负担。
- 👤 创始人背书：Ali Abdaal 是医生转创业者、全球知名生产力专家、《Feel-Good Productivity》纽约时报畅销书作者，Superfocus 将其 GPS 方法落地为日常系统。

---

### [Eased：面向 shadcn 和 AI 智能体的动画 React 组件](https://eased.dev/?ref=tailwindweekly.com)

**原文标题**: [Eased: animated React components for shadcn and AI agents](https://eased.dev/?ref=tailwindweekly.com)

Eased 是面向 shadcn 与 AI 智能体的“动效优先”React 组件库，提供 70 个 MIT 免费组件，Pro 一次性付费解锁全部展示型组件与源码，并内置 MCP、设计技能与模型友好文档。

- 🧩 组件规模：共 105 个组件，其中 70 个免费、35 个 Pro 展示型组件，Pro 每周持续新增。
- 💰 定价规则：Pro 早鸟价 $149（前 200 名 Solo 买家），常规价 $199；Team 早鸟价 $349，常规价 $449。
- ♾️ 终身授权：一次付费，获得当前及未来所有 Pro 组件与区块，并包含源码。
- 🛠️ 安装方式：通过 shadcn CLI 安装，源码直接进入项目仓库，用户拥有并可修改。
- 🤖 AI 智能体支持：提供 MCP 服务器、llms.txt、Markdown 文档，支持 Claude Code、Cursor、VS Code、Codex 搜索、读取和安装组件。
- 🎞️ 设计重点：按交互调校弹簧与曲线，退出动画快于进入动画且可中断；内圆角随 padding 保持同心。
- 🧠 Eased Skill：提供 SKILL.md 设计技能，让智能体遵循同一套动效、间距与圆角规则。
- 🖥️ 场景覆盖：面向 AI、开发工具、金融、加密、SaaS、法律、电商、房地产、健康、HR 等；也支持 Tauri/Electron 的 Mac 菜单栏弹窗与 HUD。
- 👀 真实示例：所有示例均为实时运行的组件，而非录屏；免费组件可用一条命令安装。
- 📄 技术栈：React 19、Tailwind CSS v4、Motion，使用 OKLCH 设计令牌，支持明暗模式与 reduced-motion。
- ✅ 授权与退款：免费组件为 MIT；Pro 可用于无限项目（含客户项目）且无需署名；Stripe 处理支付，退款或争议会立即终止 Pro。

---

### [WindyBase - 探索免费与高级 Tailwind CSS 模板](https://windybase.com/?ref=tailwindweekly.com)

**原文标题**: [WindyBase - Explore free and premium Tailwind CSS templates](https://windybase.com/?ref=tailwindweekly.com)

WindyBase 是一个每周精选 Tailwind CSS 模板、组件与工具的资源目录，面向现代开发者，提供免费和付费资源，并支持搜索、预览与购买，帮助快速搭建网站和应用。

- 🧭 网站定位：每周策划免费与高级 Tailwind CSS 模板、组件和工具，服务现代开发者。
- 🗂️ 资源分类：涵盖落地页、SaaS、博客、仪表盘、组件库和电商模板等。
- 🔎 使用方式：支持搜索、在线预览，并可直接购买付费资源。
- 💰 价格示例：多数模板免费，部分付费资源价格为 $11.58、$29、$99 等。
- 📬 订阅功能：可订阅新闻通讯，获取新模板、组件和工具的上新通知。
- 🌐 其他信息：提供资源提交、联系方式、隐私政策、条款及社交媒体链接，版权标注至 2026 年。

---

### [Snapzy — 强大的工具套件，化繁为简。](https://snapzy.app/?ref=tailwindweekly.com)

**原文标题**: [Snapzy â A powerful suite of tools, refined for simplicity.](https://snapzy.app/?ref=tailwindweekly.com)

Snapzy 是一款面向 macOS 13+ 的免费开源屏幕捕获与录屏应用，主打原生高性能、简约易用和本地隐私；集成截图、标注、录屏、GIF/视频编辑、OCR 与历史管理，并通过自愿赞助维持开发。

- 🖥️ 产品定位：将高级屏幕捕获工具打包为简约、高性能的原生 macOS 应用，免费且开源，已通过 Apple 公证。
- 🚀 快速上手：提供零摩擦权限设置、快捷键偏好配置和交互式引导，降低首次使用门槛。
- 📸 快速访问：截图后立即显示浮动预览，可拖拽、复制、保存或一键进入编辑。
- ✍️ 标注与编辑：支持智能箭头、几何形状、敏感信息模糊、步骤编号、文本和高亮等就地标注。
- 🎬 视频与 GIF 工作室：可裁剪录制、裁切画面、调整播放速度、添加边距，并导出 MP4 或 GIF。
- 🗂️ 本地历史：支持搜索、筛选和检索过往截图/录制，包含丰富元数据，完全离线并保护隐私。
- 🧰 20+ 捕获功能：区域选择、活动窗口、滚动截图、延迟捕获、智能元素捕捉、主体抠图、实时标记、像素放大镜与取色、录屏、OCR 等。
- 🔐 隐私与性能：100% 设备端 OCR、零遥测、本地离线历史；原生 Swift/AppKit 架构强调速度与精度。
- 🌐 多语言支持：支持英语、越南语、简繁中文、日语、韩语、俄语；西班牙语、法语、德语即将推出，并跟随 macOS 每应用语言设置，无需重启。
- 💬 社区口碑：Reddit 100+ 评论称其轻量、快速、无需登录、界面美观，常被拿来与 CleanShotX 比较且免费。
- 💰 定价模式：Community 永久免费 $0，覆盖日常截图、录屏、标注和 OCR；Supporter 为自愿付费，可通过 GitHub Sponsors 或 Ko-fi 支持，无付费墙、广告和追踪。
- 📥 获取与兼容：官网提供 macOS 下载和直接 DMG，另有文档与 GitHub；需 macOS 13+，FAQ 覆盖安装、权限、隐私、滚动截图、定价与更新。

---

### [GitHub - jesseduffield/lazydocker 位于 tailwindweekly.com · GitHub](https://github.com/jesseduffield/lazydocker?ref=tailwindweekly.com)

**原文标题**: [GitHub - jesseduffield/lazydocker at tailwindweekly.com · GitHub](https://github.com/jesseduffield/lazydocker?ref=tailwindweekly.com)

lazydocker 是一个用 Go 和 gocui 编写的 Docker 与 Docker Compose 终端 UI，目标是减少记忆 Docker 命令、切换多个终端窗口和管理容器/服务的麻烦，让常用操作集中在一个界面中完成；项目采用 MIT 许可证，GitHub 上约有 53.2k stars。

- 🐳 项目定位：为 Docker 和 Docker Compose 提供简单直观的终端管理界面，常用操作只需一次按键或鼠标点击。
- ⚙️ 环境要求：Docker >= 29.0.0（API >= 1.24），Docker-Compose >= 1.23.2 为可选依赖。
- 📦 安装方式：支持 Homebrew、Scoop、Chocolatey、asdf-vm、二进制发布包、Go install、Arch Linux AUR 以及 Docker 运行等多种方式。
- 🚀 使用方式：在终端直接运行 `lazydocker`，也可设置别名如 `lzd`；项目提供视频教程和快捷键列表。
- 🖱️ 核心功能：查看 Docker/Docker Compose 环境状态、容器/服务日志、ASCII 指标图、连接容器/服务、重启/删除/重建容器、查看镜像层、清理占用磁盘的资源，并支持鼠标操作。
- 🛠️ 配置与常见问题：可通过项目面板按 `o` 或 `e` 编辑配置；支持开启主面板文本换行、处理文本选择、调整日志时间范围等。
- 🤝 社区与贡献：欢迎贡献代码，提供贡献指南、Discord 讨论渠道和赞助支持；文档中还列出 docui、Portainer 等替代方案。
- 💡 项目理念：把查看状态、日志和常用管理命令集中到一个终端窗口中，并允许添加自定义命令，提升 Docker 日常管理效率。

---

### [HealthLog — 自托管健康追踪应用 | 源码可用的 PWA](https://healthlog.dev/?ref=tailwindweekly.com)

**原文标题**: [HealthLog â Self-Hosted Health Tracking App | Source-Available PWA](https://healthlog.dev/?ref=tailwindweekly.com)

HealthLog 是一款开源、可自托管的个人健康记录平台，用一条 `docker compose up` 即可部署在自己的服务器上，健康数据完全由用户掌控，支持多源设备汇总、加密文档保险库、可选 AI 分析以及家庭共享权限管理。

- 🐳 **自托管零订阅**：一条 `docker compose up` 即可部署，数据放在单个 PostgreSQL 卷中，支持备份到任意 S3 存储桶，无订阅费、无厂商云。
- 🔐 **默认安全**：笔记、文档与密钥用 AES-256-GCM 加密，支持 Passkey、双因素与 OpenID Connect，严格 CSP、服务端会话，无遥测、无第三方追踪。
- 🧩 **开放接口**：源代码基于 PolyForm 非商业许可公开，提供 OpenAPI 3.1 的 REST API、FHIR R4 导出与读取接口，以及供 AI 助手使用的 MCP 服务器。
- 📊 **统一时间轴**：Apple Health、Withings、WHOOP、Oura、Polar、Google Health、Nightscout 及手动记录全部汇入同一条轴线，与用药、化验结果和就诊并列；同一天多设备冲突时由用户决定采信哪个。
- 🗓️ **一键查看任意一天**：点选图表、列表或日历条上的日期，当日数据即在页面侧栏展开，显示各项读数与个人正常范围的对比及当天发生的事。
- 🤖 **AI 可选**：Coach 基于你自己的数据作答并展示推理步骤，可用自己的 OpenAI/Anthropic 密钥、Ollama/LM Studio/vLLM 本地模型，也可完全关闭，其余功能不受影响。
- 📱 **移动端**：原生 iPhone 应用让 Apple Health 与服务器双向同步；Android 及其他平台可通过浏览器安装为 Web 应用。
- ❤️ **追踪内容**：生命体征、睡眠、体成分、ECG、血糖与 CGM、情绪与身心状态、经期、天气空气质量花粉、健康评分与相关性分析。
- 🏥 **医疗记录**：用药计划与库存、补剂、带单位换算的化验结果、疾病日志与症状、就诊与体检、疫苗接种、加密文档保险库、⌘K 搜索。
- 🤝 **共享与导出**：医生报告 PDF、带二维码的分享链接、家庭成员只读或可写权限、儿童档案、9 种语言。
- 🔗 **连接生态**：Withings、WHOOP、Oura、Polar、Google Health（Fitbit 与 Pixel）、Strava、Nightscout、Dawarich、Health Connect 导入，Garmin 经 Apple 或 Google Health 接入，支持推送、Telegram、ntfy、邮件通知。
- 🆓 **授权与价格**：非商业用途免费，无付费层级；iPhone 应用为一次性小额购买，TestFlight 测试版与自行编译版本免费。
- 🧠 **AI 助手接入**：MCP 服务器默认关闭，需自行签发只读或读写令牌，写入操作需预览、确认、仅追加并留审计记录。
- 👨‍👩‍👧 **家庭与照护**：邀请可限定权限范围与失效日期，未勾选的板块一律不可见；可为不登录的被照护者建立托管档案，监护人可一次性移交为独立账户。
- ⚕️ **非医疗器械**：仅为个人健康追踪工具，不作诊断，PHQ-9、GAD-7 等问卷用于自我了解，医疗决策请咨询专业医生。

---

