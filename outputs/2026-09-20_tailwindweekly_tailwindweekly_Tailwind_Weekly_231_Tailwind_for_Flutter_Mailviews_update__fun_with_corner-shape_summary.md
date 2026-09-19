### [](https://github.com/fluttersdk/wind/?ref=tailwindweekly.com)

**原文标题**: [GitHub - fluttersdk/wind at tailwindweekly.com · GitHub](https://github.com/fluttersdk/wind/?ref=tailwindweekly.com)

Wind 是一个为 Flutter 打造的 Tailwind CSS 风格样式库，通过 className 字符串生成优化的 Flutter 组件树，让 Web 开发者无需学习新语法即可上手。

- 🌀 **核心理念**：工具类优先（Utility-first）样式，一个字符串加一个组件即可替代原本需要六层嵌套的 Flutter 代码（如圆角卡片加悬停状态）
- 📦 **安装方式**：执行 `flutter pub add fluttersdk_wind`，用 `WindTheme` 包裹应用一次，之后所有样式都通过字符串完成
- 🎨 **Tailwind 词汇表**：支持 `flex`、`p-4`、`bg-blue-500`、`rounded-lg`、`shadow-md` 等类名，由 20 个 token 解析器解析，可与 Web 项目直接复用
- 🧩 **27 个 W 前缀组件**：包括 `WDiv`、`WText`、`WButton`、`WInput`、`WSelect`、`WPopover`、`WDatePicker`、`WCard`、`WTabs`、`WBadge`、`WSwitch`、`WRadio`、`WDynamic` 以及五个表单包装器
- 🌗 **前缀可叠加**：支持 `dark:`、`sm:` 至 `2xl:` 响应式断点、`hover:`/`focus:`/`disabled:`/`loading:`/`selected:` 状态，以及 `ios:`/`android:`/`web:`/`mobile:`/`macos:`/`windows:`/`linux:` 平台前缀
- 🎛️ **可控主题**：`WindThemeData` 提供 24 个字段覆盖颜色、间距、排版、阴影、断点与动画，默认值对齐 Tailwind，并支持别名机制
- 🧪 **变体组合**：`WindRecipe` 与 `WindSlotRecipe` 可按基础样式、变体轴、复合变体及调用方覆盖，依严格顺序生成 className 或每槽位映射
- 📱 **移动端表单优化**：聚焦字段时整个输入框会抬升避开键盘及键盘工具栏，而非仅移动光标所在行；带 `onTap` 的控件只占一个遍历节点，支持 Enter、空格、手柄 A 键与电视遥控
- ☁️ **服务端驱动 UI**：`WDynamic` 可依据 JSON 结合 13 个 Wind 组件与 16 个 Flutter 核心组件白名单渲染组件树，无需发版即可更新布局
- 🤖 **面向 AI 智能体**：内置规范技能、托管 MCP 服务器及 `llms.txt` 清单，可通过 `npx skills add fluttersdk/ai --skill wind-ui` 分发至 Claude Code、Cursor、Gemini CLI、VS Code Copilot 等工具
- ⚙️ **className 规则**：前缀顺序为 `<state>:<breakpoint>:<dark>:<platform>:<utility>`；同类冲突以最后一个为准；深色模式需在同一 className 中配对颜色；未知 token 在 release 中静默丢弃、debug 中提示一次，绝不抛错或显示红屏
- 📏 **间距尺度**：一步等于 4 逻辑像素，因此 `p-4` 即 16；字号与字距同样基于像素；解析结果按 className、断点、亮度、平台与状态组合缓存
- 🚫 **非 Tailwind 直译**：Transform、Filter、`group-*`/`peer-*`、容器查询与 `@apply` 在 Flutter 中无对应实现，被有意排除在范围之外
- 📚 **文档与示例**：完整文档与实时预览见 fluttersdk.com/wind，`example/` 目录即文档站内嵌的展示画廊，可执行 `flutter run -d chrome` 运行
- 🧱 **环境要求**：需 Flutter 3.27.0 与 Dart 3.4.0 及以上版本，自 1.0 起稳定，MIT 许可，运行时依赖仅为 `flutter_svg` 与诊断契约包
- ✅ **贡献与 CI**：新功能须先提交失败测试；CI 强制 `lib/` 目录 90% 行覆盖率、零分析器问题与零格式偏差
- ⭐ **生态定位**：Wind 是 fluttersdk 生态的样式层，也可独立使用；仓库目前获 34 星、1 分支，共 453 次提交

---

### [](https://github.com/panel-ui/panelwind?ref=tailwindweekly.com)

**原文标题**: [GitHub - panel-ui/panelwind at tailwindweekly.com · GitHub](https://github.com/panel-ui/panelwind?ref=tailwindweekly.com)

panelwind 是面向 Expo/React Native 设计系统的 ESLint 插件，基于 Uniwind 与 Tailwind CSS v4，能读取项目主题、组件和变体，报告破坏设计系统的样式，并用项目已有 variant/size 给出可执行的修复建议。它借鉴 @shadcn/lint 思路，同时增加“类在真实设备上是否有效”的检查。

- 🧩 定位：把 @shadcn/lint 的思路带到 React Native/Expo，并补充只有设备才能判断的样式问题。
- ⚙️ 支持：适用于 Expo + Uniwind（Tailwind CSS v4）；PanelUI 项目通过 `panelui.json` 可零配置使用。
- 🚫 核心价值：检测 RN 中不报错但也不生效的类，如 `space-x-2`、`backdrop-blur-sm`、`hover:bg-primary`。
- 🔍 检测方式：使用项目自身的 Tailwind 和样式表编译类，再对照 React Native 类型定义生成的属性表。
- 📋 推荐规则：`no-restyle`、`no-raw-colors`、`no-arbitrary-values`、`no-inline-styles` 为 warn；`require-static-classes`、`no-unknown-classes`、`no-web-only-classes` 为 error。
- 🧱 组件契约：可按 `layout`、`color`、`typography`、`spacing`、`shape`、`effects`、`motion` 等类别配置 allow/deny 和 pattern。
- ✍️ 错误消息：支持自定义 message，并填入组件真实 variants/sizes；可在 settings 中追加全局提示。
- 📦 安装：需要 Node 20.19+ 和 ESLint 9.30+，使用 `npm install -D panelwind eslint`，并在 `eslint.config.mjs` 中引入 `panelwind.configs.recommended`。
- 📖 数据来源：从 `panelui.json` 或 Tailwind 入口读主题，从组件目录/设计系统包读组件，从 `tv()`/`cva()` 读变体，从 `@theme` 读 token。
- 🧪 运行方式：不执行代码、不渲染、不需要模拟器；`configs.strict` 可将全部规则设为 error。
- 🪪 许可：MIT 许可，仓库包含文档、`packages/panelwind`、脚本等，当前约 31 次提交、4 星。

---

### [Mailviews / 官方 Maizzle 组件和模板](https://mailviews.com/?ref=tailwindweekly.com)

**原文标题**: [Mailviews / Official Maizzle components and templates](https://mailviews.com/?ref=tailwindweekly.com)

Mailviews 是一个专为快速构建精美 HTML 邮件而设计的平台，提供基于 Tailwind CSS 的生产级邮件模板和可复用组件，帮助用户节省开发时间。平台包含 227 个精美组件、935 个变体，以及针对不同行业（如电商、文化、SaaS）的现成模板。此外，Mailviews 还提供 MCP 服务器，让 AI 代理（如 Claude、ChatGPT、Cursor）能够直接浏览组件和模板，并生成兼容各大邮件客户端的 HTML 邮件代码。用户可通过拖拽式 Builder 快速组装邮件并导出干净的生产代码。定价方面，个人版每年 99 美元，团队版每年 399 美元（5 个席位），订阅包含所有组件、模板、MCP 访问权限及后续更新。

- ✉️ **核心功能**：用模块化 HTML 组件和 Tailwind CSS 模板，大幅缩短邮件构建时间，产出可直接上线的邮件。
- 🧩 **组件库**：提供 227 个精心设计的组件，共 935 个变体，涵盖 Hero、Bento 网格、CTA、页眉页脚、社交、博客、FAQ、定价等分类。
- 📦 **模板套件**：针对文化、电商等行业提供现成模板，如 Atrium、Monarch、Santos，方便快速适配品牌。
- 🤖 **MCP 服务器**：可连接 Claude、ChatGPT、Cursor、VS Code，让 AI 代理自动挑选组件并返回兼容各邮件客户端的生产级 HTML。
- 🛠️ **Builder 工具**：支持拖拽堆叠组件，快速组装自定义邮件并导出干净的 HTML 代码。
- 💬 **用户好评**：Aaron Francis、Steve Bauman、Eric L. Barnes 等知名开发者称赞其节省数周工作量，体验极佳。
- 💰 **定价方案**：个人版 $99/年，团队版 $399/年（含 5 个席位），订阅涵盖全部组件、模板、MCP 及后续更新。
- 📚 **技术支持**：组件支持 HTML、Maizzle、Tailwind CSS，并有 FAQ 解答许可、订阅、兼容性等问题。
- 🔔 **持续更新**：用户可订阅通知，及时获取新增组件和模板。

---

### [Setapp | 适用于 Mac 和 iOS 的强大应用](https://setapp.com/?irgwc=1&afsrc=1&iradid=343321&irpid=2662107&utm_content=ONLINE_TRACKING_LINK&utm_campaign=Vivian+Guillen&sharedid=&utm_medium=affiliate&mpaid=3&utm_source=impactradius&campaign=impactradius&type=home)

**原文标题**: [Setapp | Powerful apps for Mac & iOS](https://setapp.com/?irgwc=1&afsrc=1&iradid=343321&irpid=2662107&utm_content=ONLINE_TRACKING_LINK&utm_campaign=Vivian+Guillen&sharedid=&utm_medium=affiliate&mpaid=3&utm_source=impactradius&campaign=impactradius&type=home)

Setapp 是集精选 Mac、iPhone、iPad 和 Web 应用于一体的订阅服务，现已支持单应用订阅，并提供 7 天免费试用；用户可订阅单个应用，或通过会员畅享数百款应用，其中包含 AI 工具，价格每月 14.99 美元起，年付最高可省 40%。

- 📱 新增单应用订阅，也可选择 Setapp 会员一次获取数百款应用。
- 🍎 覆盖 macOS 与 iOS，包含 AI 工具、效率、隐私保护等精选应用。
- 🧰 示例应用包括 Bartender 整理菜单栏、TextSniper 提取文字、CleanMyMac 清理 Mac、CleanShot X 截图录屏、Craft 文档创作、Nitro PDF Pro 处理 PDF。
- 🆓 提供 7 天免费试用，可随时取消，支持安全支付加密与 24/7 客服。
- 💰 方案价格：Mac 每月 14.99 美元，含 1 台 Mac 与 1000 AI 积分；Mac+iOS 每月 18.99 美元，含 1 台 Mac、4 台 iOS 设备与 1000 AI 积分；Power User 每月 22.99 美元，含 4 台 Mac、4 台 iOS 设备与 2000 AI 积分。
- 🚀 使用步骤：安装 Setapp、获取所需应用、选择单应用或会员订阅。
- ⭐ 会员权益：人工精选应用、定期新增、自动更新、无广告、应用指南、用户评价。
- 🗣️ 用户评价强调高性价比、品质审核、无试用限制，并能提升专业与个人效率。
- ❓ 常见问题涉及与单独购买的区别、包含应用、收录标准、数据隐私、企业或团队方案。

---

### [](https://css-tricks.com/what-can-we-actually-do-with-corner-shape/?ref=tailwindweekly.com)

**原文标题**: [What Can We Actually Do With corner-shape? | CSS-Tricks](https://css-tricks.com/what-can-we-actually-do-with-corner-shape/?ref=tailwindweekly.com)

本文介绍 CSS 新属性 `corner-shape`，它可配合 `border-radius` 创造出斜切、凹角、圆角方形等多种现代 UI 形状，目前主要由 Chrome 139+ 支持。
- 🧩 `corner-shape` 必须与 `border-radius` 或各方向圆角属性配合使用，用于改变圆角的绘制方式。
- ✂️ `corner-shape: bevel` 可制作时下流行的斜切角、赛博朋克风斜切区块和斜向分区。
- 📐 每个圆角都有水平与垂直两条轴，可为两轴设置不同值，例如 `100% 50px`，从而形成不同倾斜效果。
- 🏷️ 促销标签可用 `corner-shape: round bevel bevel round` 加复杂 `border-radius` 实现，值按顺时针顺序对应四个角。
- 🧭 箭头步骤导航通过继承形状、负外边距、`padding-right` 和 `z-index` 堆叠，模拟连续箭头拼接效果。
- 💬 气泡提示可用 `popover`、锚点定位和 `corner-shape: scoop` 制作小尖角，也可换成 `bevel` 得到经典三角。
- 🖍️ `<mark>` 高亮可用 `squircle bevel` 和不对称圆角模拟手绘荧光笔效果，并用 `box-decoration-break: clone` 处理换行。
- 📱 `squircle` 适合制作图标、按钮、卡片和表单控件，让圆角看起来更现代、更接近 App 图标风格。
- 🖼️ 相同方法放大后可用于手绘风方框；更大规模时作者建议改用 `border-image` 方案。
- 🧲 `corner-shape: notch` 可做背景裁剪，例如把一侧水平裁掉 `30px`，另一轴设为 `50%`。
- ⚠️ 这些形状上的 `border` 和 `outline` 表现不可预测，作者建议谨慎使用或避免依赖。
- 🎉 结论是 `corner-shape` 有趣且用途超出预期，适合在 Chrome 139+ 中实验更多创意 UI。

---

### [](https://css-tricks.com/using-css-cascade-layers-with-tailwind-utilities/?ref=tailwindweekly.com)

**原文标题**: [Using CSS Cascade Layers With Tailwind Utilities | CSS-Tricks](https://css-tricks.com/using-css-cascade-layers-with-tailwind-utilities/?ref=tailwindweekly.com)

概述总结
Tailwind 利用 CSS Cascade Layers 管理样式优先级。Zell Liew 在 2025 年 6 月 30 日文章中比较默认做法与非常规做法，主张把 Tailwind 工具类视为 utilities 层而非最高优先级，并让自有 CSS 位于未命名层或 utilities 之后，从而在快速原型与复杂 CSS 之间取得平衡。

- 🧱 Tailwind 内置 CSS Cascade Layers，典型声明为 `@layer theme, base, components, utilities;`，并分层导入 theme 与 utilities。
- 🧩 默认方案：组件写入 `@layer components`，Tailwind utilities 放最后，因此工具类能覆盖组件样式。
- 🔄 非常规方案：把自有 CSS 放在未命名层或 utilities 之后的层，使其自然覆盖 Tailwind 工具类；作者偏好未命名层。
- 💡 选非常规方案的原因：减少多余层与记忆负担，熟悉 ITCSS 和选择器优先级，并能用 CSS 处理主题、动画等复杂需求。
- 🎯 作者的优先级思路：Tailwind utilities 不是最高层，自有未命名 CSS 层才是最高，以便先用 Tailwind 快速搭原型。
- 🧹 复杂后把样式迁移到 CSS，避免 HTML 被大量工具类淹没，降低阅读和心智负担。
- ⚠️ Tailwind 工具类仍可通过 `!important` 临时提升优先级，这是 CSS Layers 特性，适合一次性快速调整。
- ⚙️ Tailwind utilities 不只是类与属性的 1:1 映射，更像便捷 Sass mixins，可用于布局、主题、排版等工具。
- 📚 作者推广课程《Unorthodox Tailwind》，分享以协同方式使用 Tailwind 与 CSS 的思路。

---

### [aria-expanded 的使用场景 - Piccalilli](https://piccalil.li/blog/use-cases-for-aria-expanded/?ref=tailwindweekly.com)

**原文标题**: [
  Use cases for aria-expanded - Piccalilli
](https://piccalil.li/blog/use-cases-for-aria-expanded/?ref=tailwindweekly.com)

本文由 Steve Frenzel 于 2026 年 7 月 16 日发布，主题为无障碍，系统梳理 `aria-expanded` 的适用场景，区分可折叠区域与可折叠交互元素，并强调优先使用原生 HTML、谨慎照搬 APG、充分用辅助技术测试。

- ♿ 文章聚焦 `aria-expanded` 的正确用例，帮助判断何时该用、何时可用原生元素替代。
- 🧭 同一操作对辅助技术的含义依赖上下文；ARIA 属性不是越多越好。
- 🗂️ 可折叠组件主要分两类：可折叠区域和可折叠交互元素。
- 📂 Disclosure widget：在按钮上使用 `aria-expanded`，通常需 JavaScript 切换；`aria-controls` 可选；优先考虑 `<details>` 和 `<summary>`。
- 🪗 Accordion：由多个 disclosure 组合而成；互斥手风琴被认为可能对用户不友好。
- 🧭 Navigation：飞出菜单可用 `aria-expanded` 表示子菜单展开状态；语义 HTML 支持渐进增强；汉堡按钮若展开导航，`aria-expanded` 通常足够。
- 📋 Menu：若确实是菜单而非导航，需要 `aria-haspopup="true"` 与 `aria-expanded`，并配合 `menu`、`menuitem` 等角色。
- 🌳 Tree view / tree grid：需要 `aria-expanded`，并可能按实现增加 `aria-multiselectable`、`aria-selected`、`aria-level`、`aria-setsize`、`aria-posinset`、roving tabindex 等。
- 🔽 Combo box：优先使用原生 `<select>`；自定义实现则需要 `aria-expanded`，并可能配合 `aria-haspopup`、`aria-activedescendant`、`aria-selected`、`aria-autocomplete` 和标签属性。
- 💬 Dialog / Modal：不应使用 `aria-expanded`，而应使用 `aria-modal` 或原生 `<dialog>`；Invoker Commands 可实现无 JavaScript 弹窗。
- 🗂️ Tabbed interfaces：暂无原生无 JavaScript 方案，常用 `aria-haspopup`，并可能使用 `aria-controls`、`aria-selected`、`aria-orientation` 等。
- ℹ️ Tooltip：APG 没有专门示例；可用 Popover API 与 invoker commands 原生实现，设置 `popover="auto"`、`role="tooltip"`，并支持 light-dismiss。
- ⚠️ APG 模式只是概念验证，并非可直接上生产的无障碍模式，应谨慎使用并彻底测试。
- 🧪 原生 `<details>`、`<summary>`、`<dialog>`、Popover 与 Invoker Commands 已减少许多自建 ARIA 需求，但仍需用辅助技术验证。
- 🌱 核心建议：优先渐进增强与语义 HTML，避免不必要的嵌套交互，并确保自定义组件同样可访问。

---

### [](https://resurf.so/?ref=tailwindweekly.com)

**原文标题**: [Resurf - A Personal Context Library.](https://resurf.so/?ref=tailwindweekly.com)

Resurf 是一个完全本地、隐私优先的个人上下文库，用于保存笔记、链接、图片和文档，并可把这些上下文交给 AI。它面向 Mac、iPhone/iPad 和 Chrome，强调快速捕获、组织、搜索、标注、AI 摘要与问答，数据默认留在设备上，无需账户。

- 🔒 完全本地且默认私密，数据留在 Mac，可离线使用，无需 Resurf 账户。
- ⚡ 使用 ⌘⇧C 快速捕获，不切换当前上下文；先存入 Inbox，之后再整理。
- 🗂️ 用 Spaces 和 Tags 按项目、研究、想法组织内容，并用视觉库按记忆方式浏览。
- 📱 可从 Mac、Chrome、iPhone 等任意应用捕获到同一库，支持文章、PDF、图片、音频、视频、代码等格式。
- 🔍 即时搜索笔记、链接、PDF、图片和文件，并支持语音备忘录、高亮与注释。
- 🤖 可选 AI 功能：AI 摘要、自带 AI Key、通过 MCP/CLI 将上下文交给 AI agents，以及向库提问。
- 🧭 五大界面是 Library、Inbox、View、Notes、Assistant，覆盖捕获、组织、查看、写作和提问。
- 🧱 原生 Swift 构建，适配 Mac、iPhone、iPad；可选通过自己的 iCloud 私有同步。
- 💰 可免费下载试用或购买许可证；Mac 版要求 macOS 14.3+，iPhone 与 iPad 免费。

---

### [适用于 Blade 和 Livewire 的 Laravel UI 组件 | April UI](https://aprilui.dev/?ref=tailwindweekly.com)

**原文标题**: [Laravel UI components for Blade and Livewire | April UI](https://aprilui.dev/?ref=tailwindweekly.com)

April UI 是一个受 shadcn/ui 启发、面向 Laravel 开发者的免费 MIT 许可 Blade/Livewire 组件库，用于以 Laravel 方式构建产品界面；它并非 Flux 的替代品，而是包优先、Blade 工作流的另一种选择。

- 🧩 面向 Laravel Artisans：为 Blade 和 Livewire 打造，不引入多余抽象，模板保持可读、本地化、易修改。
- ⚖️ 与 Flux 对比：Flux 为精良的 Livewire 界面设定了高标准；April 是免费 MIT 许可的替代方案，取舍不同。
- ✨ 设计原则：使用 `<april:button>` 无需 `x-` 前缀；可自由搭配 Alpine 与 Livewire；仅按需发布视图；通过语义 token 和 `data-slot` 定制样式。
- 📦 组件范围：基础组件（按钮、卡片、徽章、头像）、表单（输入框、选择器、编辑器、日期选择器）、浮层（对话框、抽屉、弹出层、命令面板）、数据（表格、图表、日历）、导航（侧边栏、面包屑、标签页）、区块（仪表盘、认证、定价）。
- 🧱 应用示例：产品仪表盘、团队目录、会话工作区，可作为参考、起点或可复制的 Blade 结构。
- 🛠️ 工作流：使用 Composer 安装，用 Blade 渲染，连接数据；仅在需要掌控标记时发布视图。
- ⌨️ Artisan 命令：`php artisan april:list`、`php artisan april:publish button`、`php artisan april:update --diff`；发布文件位于 `resources/views/vendor/april/components`。
- 🚀 下一步：阅读文档、选择组件，并构建 Laravel 应用所需界面；可查看文档和 GitHub。

---

### [WindyBase - 探索免费与高级 Tailwind CSS 模板](https://windybase.com/?ref=tailwindweekly.com)

**原文标题**: [WindyBase - Explore free and premium Tailwind CSS templates ](https://windybase.com/?ref=tailwindweekly.com)

WindyBase 是一个每周精选的 Tailwind CSS 模板与工具目录，面向现代开发者，帮助快速搭建网站和应用；网站汇集免费与付费的模板、组件库和资源，并提供搜索、分类浏览与订阅更新。

- 🧭 定位：每周精选 Tailwind CSS 模板、组件和工具，让开发更轻松。
- 🗂️ 分类：主要包含模板、组件库、免费资源等板块。
- 🔎 功能：支持搜索、分类浏览和查看“更多”内容。
- 🚀 模板类型：涵盖 Landing Page、SaaS、Blog、Dashboard、E-commerce 等。
- 💰 价格模式：既有免费模板，也有付费模板，如 $77、$29、$15、$249、$59、$69 等。
- 🧩 组件库：包括 Mamba UI、HyperUI、Preline Pro、Preline UI，部分免费、部分付费。
- 🏷️ 条目信息：通常展示名称、作者、类型、价格、实时预览和购买按钮。
- 🏢 常见作者/团队：Cosmic Themes、Launchoice、Creative Tim、Ahmed Kamel、Pinia Studio 等。
- 📧 订阅：可订阅新闻通讯，获取新增模板、组件等通知。
- 📌 其他：提供提交条目、联系、隐私政策、条款与条件，版权归 © 2026 WindyBase。

---

### [Sherpa — Statamic，无需终端](https://sherpa.statamic.com/?ref=tailwindweekly.com)

**原文标题**: [Sherpa — Statamic, without the terminal](https://sherpa.statamic.com/?ref=tailwindweekly.com)

Sherpa 是一款面向 Statamic 网站的免费原生 Mac 应用，无需命令行、Composer 或 DevOps 技能，就能完成建站、编辑、本地预览、版本保存和一键部署。

- 🍎 原生 Mac 应用：支持 macOS 14+ 与 Apple silicon，完全免费。
- 🚀 无需终端：选择入门套件或空白站点，Sherpa 会自动完成设置。
- 🖥️ 本地预览：网站以真实本地网址运行，并可检测 Laravel Herd 与 PHP 8.4。
- 🧩 一键安装插件：可浏览 Marketplace 并安装 Statamic 插件与附加组件。
- 🎛️ 控制面板编辑：像普通 CMS 后台一样管理内容，代码可选但非必需。
- 🔐 Git 保存同步：内置备份并同步到 GitHub、GitLab 或 Bitbucket。
- ☁️ 一键部署：动态站点发布到 Laravel Cloud，静态站点发布到 Netlify 或 Cloudflare Pages。
- ⚡ 静态生成：可快速生成静态 HTML，并发布高速站点。
- 🔑 密钥安全：API 令牌和密钥保存在 macOS Keychain，不会写入站点仓库。
- ✅ 兼容已有站点：指向文件夹即可检测 Statamic 版本、安装依赖并启动服务。
- 👶 适合新手：即使从未使用过 Statamic，也无需额外安装其他软件。
- 🪟 平台限制：目前仅支持 Mac，暂无 Windows 或 Linux 版本。
- 📦 下载即用：DMG 已签名并公证，双击安装后即可开始建站。

---

### [提示词 3](https://panic.com/prompt/?ref=tailwindweekly.com)

**原文标题**: [Prompt 3](https://panic.com/prompt/?ref=tailwindweekly.com)

Prompt 3.5 是 Panic 为旗下终端模拟器 Prompt 推出的跨平台更新，覆盖 macOS、iPhone、iPad 与 visionOS，带来空间计算支持、更快性能、更强安全与同步，并降低价格。

- 📱 Prompt 自 2011 年起是受欢迎的 iOS 应用；Prompt 2 获 4,131 条评价和高 App Store 评分，官方邀请用户体验更轻快强大的 Prompt 3。
- 🥽 Prompt 3.5 登陆 macOS、iPhone、iPad 和 visionOS；visionOS 版把强大终端模拟器带入空间计算，可在头显中完美运行。
- 🌌 一键传送到 “Terminal 33”——专为黑客打造的自定义空间环境；所有 Prompt 用户免费获得 visionOS 支持，一价一应用覆盖四平台。
- 💸 Prompt 3 降价，希望减轻用户负担。
- ⚡ 超快 SSH：重做文本引擎，滚动与终端模拟速度最高提升 10 倍，并可选启用 GPU 加速。
- 🔗 新增 MOSH 与 ETERNAL TERMINAL 连接类型，在网络不佳时仍保持终端稳定。
- 📋 Clips：点击或轻点即可插入常用命令和文本片段，并可在设备间同步。
- 🎨 可定制：新增主题、字体和高度可配置的 iOS 键盘，让触屏输入更顺手。
- 🔄 PANIC SYNC：在 Mac 或 iOS 的 Prompt 上轻松同步服务器、密钥和密码，免费、安全且简单。
- 🔐 更高安全性：用 FaceID/TouchID 与安全隔区加密收藏项，支持 YubiKey 双因素验证。
- 🏢 JUMP HOSTS：在维护企业安全的同时访问公司服务器，远程修复服务器。
- 🖥️ 改进模拟：tmux 等复杂终端任务渲染更准确、更快速。
- 🖱️ 鼠标支持：可用鼠标与终端中的 TUI 应用交互。
- 🌑 新增深色图标。
- 📧 需要帮助可联系 prompt@panic.com；支持分类包括问题、问题报告、功能请求和其他，并可附文件与诊断数据。

---

### [KyttoMCP — 适用于 macOS 和 Windows 的 MCP 服务器管理器](https://kytto.jakubhecht.sk/?ref=tailwindweekly.com)

**原文标题**: [KyttoMCP — MCP Server Manager for macOS & Windows](https://kytto.jakubhecht.sk/?ref=tailwindweekly.com)

KyttoMCP 是一款面向 macOS 和 Windows 的本地 MCP 服务器管理器，当前 Beta 1.0.6.1 免费提供；它把 Claude Desktop、Claude Code、Cursor、VS Code 和 Codex 中分散的 MCP 配置集中到一个工作区，方便查看、检查、编辑和切换，同时强调本地运行、备份与隐私。

- 🧩 支持多个客户端：Claude Desktop、Claude Code、Cursor、VS Code、Codex，并尊重各客户端配置格式与规则。
- 🗂️ 统一矩阵视图：查看每个 MCP 服务器在各客户端中的启用状态，并可一处开关，避免逐个翻 JSON/TOML。
- 🏷️ 内置与自定义来源：可手动创建 MCP 条目，或使用内置目录；也可附加只读 JSON、JSONC、TOML 文件。
- 🩺 健康检查：按需执行 MCP 握手，查看工具、提示、资源、协议详情、stderr 和 token 权重估算。
- 🎛️ Profiles：保存 Coding、Research、Minimal 等本地 MCP 组合，预览变更后应用到某个客户端。
- 🔐 密钥管理：敏感环境值默认掩码，可按需显示、全局轮换、存入 Keychain 或限制配置权限。
- 💾 备份与恢复：每次写入前检查外部变更并创建时间戳备份，支持浏览和恢复旧配置。
- 🌐 可选 Gateway 模式：为支持的 stdio 服务器预览本地 Gateway 路由，迁移凭证到原生存储，并可一键恢复 Direct 模式。
- 📏 上下文优化器：估算每个服务器/配置文件的完整 schema 占用，用于一致性比较并标记重复工具名等。
- 🧭 MCP Doctor：把配置与健康证据转为可操作发现，安全修复会在写入前预览。
- 🕵️ 活动日志隐私：查看 Gateway 会话、工具调用、延迟和失败，导出安全支持报告；不记录参数、结果和 payload。
- 🛡️ 本地信任设计：无云账户、无同步、无密钥上传；配置和凭证留在本机，匿名诊断默认关闭。
- ⬇️ 下载与安装：Beta 1.0.6.1 提供 macOS 通用版 DMG（4.5 MB）和 Windows x64 安装包（78.5 MB），首次打开可能需绕过未签名开发者警告。
- ✅ 校验与反馈：页面提供 SHA-256 校验和；可经私密表单或 GitHub issue 报告 bug，并可分享推广。

---

