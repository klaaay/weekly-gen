# [Tailwind Weekly #240: Styling Vercel's UI SDK, anti-AI slop moves, and spring-physics toasts 🔔](https://tailwindweekly.com/issue-240/)

### [发布 · nuxt/ui · GitHub](https://github.com/nuxt/ui/releases?ref=tailwindweekly.com)

Nuxt UI 近期连续发布 v4.9.0 至 v4.13.0，最新 v4.13.0 新增 Toggle/ToggleGroup、ChatPrompt 文件附件、useToast 的 promise 方法和 ESLint 主题类校验，而 v4.12.1/v4.12.2 修复了服务端渲染不可信 Markdown 时可能触发存储型 XSS 的严重安全问题。各版本还引入 Chart、Splitter、ProgressGroup、InputRating 等组件，并带来 @nuxtjs/i18n 自动 locale、图标打包、页面 JS 体积最高减少 27%、统一焦点样式和 theme.unstyled 等改进，整体强化了交互能力、可访问性、性能与主题定制。

- 🚀 **v4.13.0 新增切换组件**：发布 Toggle 和 ToggleGroup 组件，用于可按下或关闭的按钮；ToggleGroup 在 `type` 设为 `multiple` 时允许多选。两者接受 Button 的 props，并新增 `active-color` 与 `active-variant` 控制按下状态。
- 🧩 **ChatPrompt 文件附件**：ChatPrompt 支持 `v-model:files`，用户可粘贴或拖放文件，并通过新 ChatAttachment 组件列出；可用 `@nuxt/ui/utils/ai` 的 `toFileUIParts` 随 AI SDK 发送，`v-model:queue` 可在响应流式传输时排队消息。
- ⚡ **Promise toast**：`useToast` 新增 `promise` 方法，先显示 loading toast，并在 Promise 完成或失败时更新为 success 或 error；示例中 loading 为 `Saving...`，成功可设置标题和 `color`，失败可根据 `error.message` 构造 toast。
- 🛡️ **XSS 安全修复**：v4.12.1 修复 GHSA-x9jw-j844-v24h，服务端渲染用户或 LLM 可写的 Markdown 时可能执行代码；v4.12.2 补全修复，`as` 值若携带属性（如 `img src=x onerror=…`）仍可能造成存储型 XSS，非纯标签名的 `as` 会回退默认元素，类模板对象也会被拒绝。渲染不可信 Markdown 的应用应升级到 4.12.2，仅渲染自有文件的站点不受影响。
- 📊 **Chart 组件**：v4.12.0 新增基于 TanStack Charts 的 Chart 组件，可将 line、area、bar、donut 图以 SVG 在服务端渲染；系列颜色通过 `--ui-chart-*` CSS 变量跟随主题和色彩模式。`@tanstack/charts` 是可选 peer 依赖，`definition` prop 可传入完整 TanStack 图表定义。
- 🌐 **i18n 自动 locale**：v4.12.0 起安装 `@nuxtjs/i18n` 后，App 组件会跟随当前 i18n locale，并且只打包与 `i18n.locales` 匹配的 Nuxt UI locale；可移除 `import * as locales` 模式，显式 `locale` prop 仍然优先。
- 📈 **页面性能优化**：v4.12.0 使页面加载的 JavaScript 最高减少 27%，示例从 871.6 kB 降至 549.6 kB，gzip 从 251.9 kB 降至 183.9 kB；页面不再加载仅其他页面使用的组件代码，Header、Sidebar、DashboardSidebar 菜单、DashboardSearch 和 ContentSearch 命令面板、Toaster 吐司均改为懒加载。`UButton` 挂载约快 38%，DropdownMenu 每项约快 30%。
- 🔧 **Splitter 与 ProgressGroup**：v4.11.0 新增 Splitter，可用拖拽手柄分隔可调整大小的面板，支持 min/max 尺寸、折叠、嵌套和垂直方向；SSR 时设置 `id` 让 hydration 一致，`auto-save-id` 可将布局持久化到 localStorage。ProgressGroup 用单条进度条的分段展示多个值，带图例，支持主题色或 CSS 颜色，`status` 显示总计。
- 🎨 **动效与主题剥离**：v4.11.0 将动画和移动过渡统一到 `--ease-out`，退出动画也包含，可在 `@theme` 覆盖该 token；`prefers-reduced-motion` 也覆盖 overlay，使其原地淡入并停止 Tabs 指示器等移动过渡。v4.9.0 新增 `theme.unstyled`，剥离所有组件默认主题类，只保留结构及通过 `class`、`ui` 或 `app.config.ui` 提供的类，但会移除定位、过渡、flex/grid 等结构类，Modal、Drawer、Calendar 等需自行补布局。
- 🧭 **useTour 与 Calendar**：v4.9.0 新增 `useTour` composable，通过重锚定单个 Popover 驱动引导步骤，管理步骤状态并将每步 `target` 解析为 `reference` 绑定到 `UPopover`；内容与导航仍由开发者控制。Calendar 新增 `type` prop，支持 `date`、`month`、`year`，在 date 模式标题按钮可循环 day→month→year，并由 `viewControls`、`viewButton` 控制且兼容 `range`。
- 📦 **图标打包与 InputRating**：v4.10.0 新增 InputRating，支持半星、自定义长度、清除、悬停预览和任意图标。Nuxt UI 同时将自身使用的图标嵌入构建，使其在 SSR 时立即渲染并离线可用；Nuxt 借助 @nuxt/icon 的客户端 bundle，Vue/Vite 通过 `@nuxt/ui/vite` 的 `icon.clientBundle` 显式列出或扫描图标，使用前需安装 `@iconify-json/{collection_name}`。
- 🎯 **统一焦点样式**：v4.9.0 让所有组件共享 `focus-visible` 软轮廓光环，按组件 `color` 着色，例如 `outline-primary/25`；Tab 面板、可滚动区域和 overlay 链接等浏览器可聚焦元素也会显示该光环。若想全应用统一颜色，可在 `main.css` 用一条全局规则覆盖。
- 🛠️ **ESLint 配置**：v4.13.0 提供 `@nuxt/ui/eslint` 配置，按主题检查 Tailwind CSS 类，例如存在语义 token `text-muted` 时提示 `text-gray-500`；需要安装 `eslint-plugin-better-tailwindcss`。Nuxt 中设置 `ui.eslint` 为 `true`，Vue 项目可参考指南在无 Nuxt 时使用。
- 🧪 **Vue 组件检测**：v4.11.0 的 `@nuxt/ui/vite` 插件支持实验性 `experimental.componentDetection`，类似 Nuxt 模块扫描源码并仅为使用的组件生成主题 CSS；也可传入组件名数组，以包含通过 `<component :is>` 渲染而无法检测的组件。

### [发布 · uni-stack/uniwind · GitHub](https://github.com/uni-stack/uniwind/releases?ref=tailwindweekly.com)

UniWind 从 v1.10.0 到 v1.14.0 连续发布多个版本，核心集中在原生端 CSS 级联与 scoped variables 支持、Metro/Vite 打包解析、React Native 0.87 和 Expo 57 兼容性、Web 热更新以及样式缓存性能。最新 v1.14.0 新增 `platform-color()` 系统色回退与原生文本断行类透传，同时修复主题、颜色变量和圆角别名等问题，显示项目正在持续补齐跨端样式一致性与构建稳定性。

- 🚀 **v1.14.0 新功能**：新增 `platform-color()`，可为系统颜色提供回退值；原生端会把 `line-break`、`word-break` 类传给 `Text` 的 props，改善文本断行控制。
- 🐛 **v1.14.0 修复与优化**：修复 bundler 对 `start-end`/`end-start` 圆角未生成 top/bottom 别名、scoped theme 下 `light-dark` 解析、原生颜色函数内变量通道解析；并缓存 CSS 变量归一化结果、移除原生样式记录中的 `index` 和 `className`、缓存使用 `data-[…]` 变体的原生样式。
- 🧩 **原生 CSS 级联**：v1.13.0 在原生端遵循 CSS 级联顺序，并生成原生样式匹配谓词；同时分离样式元数据与声明，为复杂变体和级联匹配提供基础。
- ⚡ **编译器与缓存**：v1.13.1 修复 `useUniwind` 经 React Compiler 编译后失步、保留原生 transform 中 `rotate-x/y/z` 角度、支持主题生成中的 Tailwind import options，并用非 `localeCompare` 排序 scoped variable 缓存键；v1.13.2 修复初始主题竞态，并让 Metro 在跟踪导入 CSS 时跳过生成的 `uniwind.css`。
- 🎨 **字体与文本布局**：v1.12.1 支持 `fontVariationSettings`，并覆盖 `textAlign` 的 `start`/`end`；同时修复媒体查询保留、排除式媒体查询边界以及 `InputAccessoryView` 在 Web 的循环依赖。
- 🛠️ **Metro/Vite 解析**：v1.12.1 为根入口补充 Metro 的 `main`/`react-native` fallback，处理 Expo autolinking 选中 hoisted 副本时的别名解析，避免 Expo tree shaking 优化 uniwind 注入的 JS，移除已废弃的 Vite `customResolver` 用法，原子写入 `uniwind.css`，并修复 `no-types.d.ts` 未发布问题。
- 🌐 **Web 生命周期**：v1.12.0 使用 `useSyncExternalStore` 改善 `withUniwind` 与状态 hooks 对 React 生命周期的兼容，修复 Web 懒加载组件 CSS 热更新、冻结监听器、符号链接 uniwind 来源的 Metro 解析；v1.12.2 继续修复 Web 新样式通知和根解析器状态重置。
- 🚀 **v1.12.0 能力**：支持 `drop-shadow` filter function，并修复从扁平化类选择器读取变体 token、跳过未变化的原生样式表重新初始化。
- 🧩 **scoped variables**：v1.11.0 引入 scoped variables，为作用域主题变量提供支持；同时新增 iOS 和 React Native 0.87 canary 的 filter 支持，并补齐 React Native 0.87 类型与颜色方案兼容。
- 📦 **Web 与 Expo 兼容**：v1.11.0 通过 `browser` exports 字段修复 Web RN 打包；v1.10.1 让 `withUniwind` 在 Web 转换后移除 `className`，支持多行 class、采用已应用的 HTML 主题、修复 Vite 8 未预打包 react-native-web，并为 Uniwind Metro 配置加入内部 Expo 项目标记以惰性选择 transform worker。
- 🎨 **v1.10.0 特性**：v1.10.0 支持 RTL safe area 类和 CSS `min()` 函数，并修复 `!important` 与状态选择器 specificity 的配合。
- 🧪 **测试与依赖**：v1.14.0 增加原生 text decoration style/color 与 `mix-blend-mode` 测试；v1.12.0 将 Web 测试迁移到 Vitest；v1.10.1 将依赖更新到 Expo 57。

### [RenderPixels · 来自你的 AI 助手的像素级精确图像](https://renderpixels.com/?ref=tailwindweekly.com)

RenderPixels 是一个可通过远程 MCP 接入 AI 助手的图像渲染服务：助手把设计写成 HTML 与 Tailwind CSS，RenderPixels 在真实浏览器中渲染，并按各平台要求的精确尺寸返回可直接使用的文件，覆盖 Open Graph 分享图、Instagram 帖子、横幅、Logo 和 favicon 套件。它支持 Claude、Claude Code、ChatGPT、GrokBot 及任何支持远程 MCP + OAuth 的助手，无需 API key；每月提供 50 次免费渲染，超出后按不设有效期的 credit 包计费。

- 🚀 **产品定位**：RenderPixels 面向需要在聊天中直接产出成品图片的用户：连接一次后，用自然语言描述文字、颜色和氛围，即可拿到 1200×630 分享图、1080×1440 Instagram 帖、1500×500 X header、透明 PNG Logo 或整套 favicon 等按平台规格渲染好的文件。
- 🧩 **核心机制**：AI 助手负责把设计写成 HTML 和 Tailwind CSS，RenderPixels 在真实浏览器里渲染。它能绘制文字、形状和 SVG 插画，也可以按 https URL 放入照片；字体支持任意 Google Fonts 字族或自有的 .woff2 文件。因此尺寸、文案和品牌色都按写定的值精确输出，而不是估算。
- 🔍 **渲染自检**：每次渲染都会报告文字被裁切、字体或缺图等问题，助手可据此修正并重试；同时提供预览页，Claude 中直接显示 Download 与 Open image，其他助手中可查看分享链接的展开效果。
- 🔗 **永久链接**：每个产出文件都会获得一个永久 URL，可直接放进页面、meta 标签或消息里使用，无需另行托管。
- 📊 **与图像模型对比**：同一提示词下，ChatGPT 内置图像生成器返回 1731×909、2.5 MB PNG，并非要求的 1200×630，体积约重 29 倍，需要再缩放压缩；RenderPixels 返回 1200×630、85 KB PNG，1 秒内渲染完成，可直接上传，且同一设计能一次输出其他所有尺寸。文中也承认，照片和插画仍应交给图像模型。
- 🎨 **品牌套件**：可把主色、辅色、强调色、背景、前景、标题与正文字体以及 Logo 存为 brand kit，之后按名字调用。示例中一次请求即从同一设计产出 Instagram 帖、X header、Open Graph 图和 Story 四种尺寸，第二次请求生成 favicon 套装。
- 🛠️ **接入方式**：Claude 在设置 → Connectors 中添加自定义连接器并粘贴 MCP 地址；Claude Code 执行 `claude mcp add --scope user --transport http renderpixels https://renderpixels.com/mcp` 后用 `/mcp` 认证；ChatGPT 在 Plugins 中添加自定义 MCP 服务器并在聊天里 @RenderPixels；GrokBot 直接下指令。其他助手需支持 Streamable HTTP 传输与 OAuth 登录，不支持 OAuth 的助手无法连接。
- 📦 **定价**：每月 50 次免费渲染，UTC 每月 1 日重置，无需信用卡。1 credit 对应 1 次渲染，完整 favicon 套件仍算一次；credit 不过期、无订阅。套餐为 2,000 credits / $10、6,000 / $25、15,000 / $50、40,000 / $100，使用优惠码 BF2026 在 11 月 30 日前结账可享 8 折，折后单次渲染分别约 $0.005、$0.0042、$0.0033、$0.0025。
- ⚠️ **限制与注意**：它不生成照片或写实插画，只能渲染 HTML/CSS 并通过 URL 引入外部照片；每次修改、以及为修复裁切文字或缺字体而重渲染都会各计一次渲染；图片可商用，但需自备字体、Logo、照片的授权；删除账户会同时删除渲染结果与图片，其链接将失效。

### [使用 Tailwind CSS 为 Vercel 的 UI SDK 设置样式 — HextaUI](https://hextaui.com/blog/style-vercel-ui-sdk-tailwind?ref=tailwindweekly.com)

Vercel Labs 于 2026 年 11 月 12 日将 UI SDK 发布到 npm，提供面向 React、Vue、Svelte、Solid 和 Web Components 的无样式可访问组件；本文基于 0.1.0-beta.1，用 Tailwind CSS v4 和 shadcn 风格 token 为 Select、Popover、Rating、Color Picker 演示如何通过 data-slot、状态属性、CSS 变量以及 data-starting-style/data-ending-style 完成主题化与进出场动画，并给出迁移和排错要点。

- 🚀 **Beta 发布**：Vercel Labs 于 2026 年 11 月 12 日将 UI SDK 发布到 npm，当前示例使用 `0.1.0-beta.1`；它面向 React、Vue、Svelte、Solid 和 Web Components，提供无样式但处理焦点、键盘和 ARIA 的可访问组件，beta 阶段 API 仍可能变化。
- 🧩 **三层架构**：`@ui-sdk/core` 承载 roving focus、typeahead、弹层、拖放等行为，`definePrimitive` 将行为、状态、API 和命名插槽组合成 primitive，`@ui-sdk/react` 等适配器把插槽暴露为 `SelectTrigger`、`RatingItem` 等 part；每个 part 以 `data-slot`、状态属性和 CSS 变量作为样式挂载点。
- 🎨 **Tailwind 配置**：使用 Tailwind CSS v4 时需在全局样式表先写 `@layer ui-sdk;` 再导入 Tailwind，因为 SDK 运行时将自身 CSS 注入该层；没有 Provider 或包内样式表，shadcn 风格 token 不被 SDK 读取但可与 shadcn/ui 共用。若 CSP 禁用内联样式，运行时 CSS 需要 nonce 或 constructed style sheets。
- ⚡ **弹层生命周期**：弹层打开第一帧带 `data-starting-style`，关闭时带 `data-ending-style` 并保持挂载至过渡结束；退出样式应挂在 `data-ending-style` 而非 `data-closed`。弹层使用浏览器 top layer，作为组件子节点原位渲染，没有 `Portal`/`Positioner`，`z-index` 不决定其是否高于 sticky header；需保留关闭内容时可设 `keepMounted`，`onOpenChangeComplete` 在动画结束后触发。
- 🎯 **Select**：Select 用 `data-open:bg-accent` 标记触发器的打开态，`min-w-(--anchor-width)` 让列表至少与触发器同宽，`origin-(--transform-origin)` 从弹出侧缩放，`data-highlighted`/`data-selected` 区分高亮与选中项，`SelectItemIndicator` 只在选中项内渲染。传入 `items` 可选但推荐，便于列表未渲染时显示选中标签并让 agent bridge 读取选项。
- 💬 **Popover**：Popover 入场通过 `data-starting-style` 从 `-translate-y-1`、`scale-95`、`opacity-0` 过渡到正常态，退出用 `data-ending-style:duration-100` 比 200ms 入场更快，`motion-reduce:transition-none` 在减少动态偏好下关闭过渡。`PopoverTitle` 与 `PopoverDescription` 为 dialog 提供可访问名称和描述，无标题时需给内容 `aria-label`。
- ♿ **Rating**：Rating 是渲染为星级的单选组，`step={0.5}` 让每个半星成为独立 radio；`RatingItem` 用 `--rating-fill`（0 到 1）表示填充比例，`data-filled`、`data-partial`、`data-highlighted` 分别标记整星、部分星和指针预览。星形 mask 要放在内部 span 而非可聚焦的 `RatingItem`，否则会裁剪焦点轮廓；键盘方向键可直接改分。
- 🎨 **Color Picker**：Color Picker 各 part 写入 `--color-picker-color`，区域提供 `--color-area-background`，滑块提供 `--color-slider-background`；绘制渐变必须用 `bg-(image:--color-area-background)` 而非把变量当颜色。ColorPicker 应包住 Popover 以共享颜色，thumb 的绝对定位和百分比由内联样式给出，类名只需 `-translate-1/2`，滑块 thumb 还需 `top-1/2`；OKLCH 区域需加入 `ColorPickerAreaCanvas` 逐像素绘制色域边缘。
- 🔄 **迁移要点**：除在每个 part 上写工具类，也可用 `[data-slot=select-item]` 等纯 CSS 按插槽集中主题；`data-slot` 是受管属性，不能被 props 覆盖。迁移 shadcn 风格组件时，Radix 的 `data-[state=open]` 改成 `data-open`，进/出场改成 `data-starting-style`/`data-ending-style`，`--radix-popover-content-transform-origin` 和 `--radix-popover-trigger-width` 分别改为 `--transform-origin`、`--anchor-width`，并删除 `Portal`/`Positioner`，把 `side`、`align`、`sideOffset` 放到 content。
- ⚠️ **常见坑**：常见坑包括把退出样式写到 `data-closed` 导致无动画、忘记首先声明 `@layer ui-sdk;` 使运行时 CSS 压过自定义样式、在可聚焦 part 上使用 mask 裁剪焦点环、误以为 `--available-height` 会继承到子元素，以及用 `bg-(--name)` 读取渐变变量；应分别改用 `data-ending-style`、声明层、内层 mask、在弹层上复制变量并用 `bg-(image:--name)`。

### [10 个对抗 AI 垃圾内容的前端项目招数：当项目进展快过人类审核速度——Martian Chronicles，Evil Martians 团队博客](https://evilmartians.com/chronicles/ten-anti-ai-slop-moves-for-frontend-projects-going-faster-than-humans-can-review?ref=tailwindweekly.com)

AI 让单个开发者一周产出上万行代码，速度已经超过人工评审和理解的能力，而模型不记得昨天的约定、不为生产负责、半年后也无法解释自己的决策。文章面向 TypeScript/React 前端，给出 10 项检查，分为三类：用契约、类型、层边界和自定义规则阻止多余代码被写出来；用变异测试、死代码检测和重复代码检测发现已经写下的问题；最后用 CI 让所有检查不可跳过。作者把流程打包为 `anti-slop-audit` 和 `anti-slop-rollout` 两个 agent skills，并强调这些检查只能减少人工需要逐行查看的代码量，不能替代理解、品味和产品判断。

- 🚀 **配套 Skills**：`anti-slop-audit` 先测量仓库在 strict TypeScript、sonarjs、层边界、Stryker、knip、jscpd、react-doctor 下会命中什么，并规划值得做的项；`anti-slop-rollout` 每次运行推进一个 PR，先 warning 后 CI gate。支持 Claude Code、Cursor、Codex、GitHub Copilot、Gemini CLI，可用 `npx skills add gretchenfitze/anti-slop -a claude-code -g` 安装。
- 🔗 **OpenAPI 契约**：用 OpenAPI spec 作为唯一描述，Hey API 生成类型、客户端和 Zod schema。模型常写不存在的字段，例如后端返回 `firstName`/`lastName` 却写 `user.fullName`；有契约后该字段无法编译，Zod 在运行时做第二道闸。生成客户端不必逐行评审，评审对象变成更小的契约；前提是契约权威且后端持续维护，没有 spec 就跳过。文中引用 2025 Stack Overflow 调查：66% 受访者最大的挫败是 AI 方案“几乎对但不完全对”。
- 🛡️ **严格 TypeScript**：除了 `strict: true`，再加 `noUncheckedIndexedAccess`，让 `arr[0]` 变成“元素或 undefined”，强制代码处理空数组；`exactOptionalPropertyTypes` 收窄类型声明与实际值之间的差距。这些配置专门消除生成代码最容易做出自信假设的地方。
- 🧩 **Linter 行为过滤**：sonarjs 负责认知复杂度、相同分支、重复字符串字面量、嵌套控制流；react-you-might-not-need-an-effect 检测用 effect 做状态同步、派生值和 prop 变化；@vitest/eslint-plugin 的 `expect-expect`、`no-focused-tests` 抓无断言测试和漏删的 `.only`；eslint-plugin-playwright 查测试内条件、漏 `await`、`.only`；jsx-a11y 查可访问性。TS 侧禁 `any`、禁非空断言、导出显式返回类型、`consistent-type-definitions`；文件名与导出名一致、只通过别名导入，否则死代码检测会失真。
- 🏢 **层边界**：eslint-plugin-boundaries、dependency-cruiser、oxlint 的 boundaries 声明层与允许的导入。模型不记得架构，会向 GitHub 平均写法漂移。规则包括：依赖单向，组件可依赖服务、服务不可依赖组件；工具、类型、配置不含领域逻辑；设计系统与状态和 API 隔离；mock 不进生产构建；router 只做路由到页面的映射。报错信息要说明依赖应该放到哪里。
- 🛠️ **自定义规则**：写规则的成本降到约十分钟，从投资变成对重复错误的常规响应。两类值得写：抵消模型默认行为的行为过滤器，以及编码已发生 bug 的“伤疤”。例子是服务把小时四舍五入到十分位、formatter 再舍入一次，26h15m 变成 26h18m，排查花了半天；规则禁止服务返回值使用 `Math.round` 和 `toFixed` 并打印原因。说不出背后事故的规则不要写。
- 🧠 **规则前置**：项目规则文件在会话开始时被 agent 读取，配合 skills 或 tools 提供更具体的指导；react-doctor 既能做项目扫描，也能作为 skill 在生成代码时提供规则。但预防是概率性的：一条规则要和文件里其他四十行以及模型权重里的上百万仓库竞争，只能降低频率，不能替代后续检查，因此应把保障移到对改动文件运行 linter 的 hook 里。单一安全、性能、架构评分只当诊断，不当目标。
- 🧪 **变异测试**：Stryker 故意改坏代码，例如把 `<` 换成 `<=`、清空数组、反转条件、替换返回值，找出没有测试捕获的变异体。存活变异体通常意味着测试只查 shape（`toHaveBeenCalled()` 而非 `toHaveBeenCalledWith(...)`、`toBeDefined()`）、使用未验证的快照、照抄实现的断言、只验证 mock。不要设失败阈值，等价变异体永远存在，分数变成目标就会写出为杀变异体而写的测试。项目约 4700 个变异体，增量运行约 6 分钟；CI 中只跑 PR 改动文件。
- 🔍 **死代码**：AI 加代码比删代码容易。Knip 找无人导入的文件、无人使用的导出和不再需要的依赖；`ignore` 列表会因生成文件、特殊导入等增长，需定期审查，每个被忽略路径都是探测器被禁止检查的区域。通用工具覆盖不到仓库特有问题：自写 Node 脚本从入口遍历 import 图找出不可达文件；另一个脚本解析 `vi.mock()` 路径、读取模块真实导出并与 factory 的 key 比对，找出过期 mock。自定义检测器也要测试，至少用一个故意留下的死文件验证它能发现。
- 📦 **重复代码**：模型倾向写第二份实现而不是搜索已有的。jscpd 查文本相似块，关键是给 markup 和逻辑设不同阈值：重复 JSX 可能是有意的，重复业务逻辑更可能变成维护问题。局限是只能发现文本重复，两份写法不同的同一规则实现会漏掉，语义重复仍需人工。文中引用 GitClear 对 623M 次变更的分析：块重复上升 81%，移动代码即重构的占比下降五倍，但数据是观察性的、未标记 AI 代码，还不能当证明。实际案例是同一工资总额一处显示 23h30m，另一处显示 0h00m。
- ✅ **CI 强制**：检查只有在 CI 阻止分支合并时才是强制的。流水线包括格式与 linter、`tsc` 独立 job、单测、PR diff 上的变异测试、构建；部署依赖这些 job 通过。检查保持独立，不要藏在一个脚本后面，否则 `typecheck` 失败时要翻合并日志。
- ⚠️ **成本与推广**：误报是主要噪音，sonarjs 会标记正常代码，jscpd 会标记测试和 fixture 中有意的重复；`eslint-disable` 和忽略路径悄悄增长说明检查正在失去覆盖。规则会过期，一年没抓到有用问题的规则应审查或临时移除。变异测试给每个 PR 增加数分钟，检测器本身也要维护。最大成本是 onboarding，新人可能先撞上数百条规则，因此错误信息要说明为什么存在、应该怎么做。推广顺序：先基线，新规则用 warning、只查改动文件；再逐条把抓到真 bug 的 warning 升为 error；最后加 CI gate。在存量仓库一次性全开会立刻产生数千错误并很快放弃。适用条件是代码活过一个季度、作者之外有人读、bug 对团队外有后果；小团队找 PMF、一半代码一个月后作废时，这套可能得不偿失。只做一件事就选契约，其次变异测试，最后 gate。
- 🔮 **覆盖不到**：这些检查不会告诉你功能是错的、抽象引入过早、某些状态该放进 URL，或者这已经是代码库里第三种解决同一问题的模式。全部通过只说明检查没有发现它们被设计来发现的问题，不代表有人理解了代码；目标是减少人工逐行检查的量，而不是取消 code review。

### [Better Stack 介绍 ES2027 的四项 JavaScript 特性](https://www.youtube.com/watch?v=DLT6n3wCkuc&ref=tailwindweekly.com)

Better Stack 以 ES2027 为主题，用代码示例讲解 JavaScript 在日期时间、资源管理、迭代器和并发方面的变化。这段摘要依据视频发布者提供的简介与章节整理。

- 🗓️ **日期与时区**：视频用跨越夏令时切换的航班时间计算演示 `Temporal`。
- 🔄 **资源清理**：`using` 声明让可释放资源在离开作用域时自动清理。
- 🔗 **并行遍历**：`Iterator.zip` 将多个可迭代对象的元素按位置组合。
- ⚡ **自旋等待**：`Atomics.pause` 为自旋等待循环提供提示。
- 🧪 **其他提案**：视频还讨论了 `import defer`、`Promise.allKeyed`、装饰器和仍处早期阶段的 Signals 提案。

### [DuckyHelper：理解一切。做任何事。](https://www.duckyhelper.com/?ref=tailwindweekly.com)

DuckyHelper 是面向 Mac 的 AI 助手，以任意应用中的 `fn` 键和屏幕上的 `pill`/`orb` 为入口，把屏幕理解、语音讲解、屏幕标注、黑板/3D 演示与 computer use 串成一条工作流：用户口述问题或任务后，它既能看见当前页面并绘制解释，也能在应用内用独立光标后台点击、输入和滚动执行任务。其核心变化是把聊天式问答扩展为“看着你的屏幕解释并直接动手”的连续体验，同时加入多 bot、任务接管、撤销、例程和本机记录等控制机制。

- 🚀 **产品入口**：DuckyHelper 提供 Mac 应用下载和浏览器入口；在任意应用按 `fn` 唤醒并口述，或把 `orb` 拖到目标窗口后口述任务，Mac 应用内提供 computer use 能力。
- 🧩 **屏幕理解**：它读取当前页面、文件和已打开应用，答案从用户所在位置开始；可在所指位置画圈、箭头和标签，并说明只会在 `pill` 打开期间查看屏幕。
- 🎨 **语音与可视化**：按 `fn` 说话后，它用自身语音回答，文字随语音高亮；可在屏幕或黑板上逐步画数学步骤和分数条，按需生成测验，并用 3D 模型逐部件演示喷气发动机或涡扇等工作原理。
- ⚙️ **Computer use**：口述任务后，它在目标窗口后台用独立光标点击、输入和滚动，光标旁标签显示每一步；用户鼠标键盘保持可用，可随时停止或接管。
- 🔄 **多 bot 并行**：每个任务由一个 bot 在屏幕右侧接管并显示当前步骤；可同时运行两个任务，例如一个整理文件、另一个在浏览器窗口工作，每个 bot 有独立行。
- 🛡️ **安全与接管**：它不会输入密码或卡号；遇到登录会把步骤交还用户，登录后继续执行；每个任务都会记录在 Mac 上。
- ✅ **撤销与记录**：完成的文件任务会说明改了什么，并在卡片上保留 `Undo` 按钮；Dashboard 保存每次对话、任务、绘图和笔记，并显示每周学习时长和学习时段。
- 🧪 **代表场景**：页面示例包括在 `Numbers` 中填充 D 列合计（示例为 D3 到 D5）、由独立光标解开文字谜题、标记作业中出错步骤、运行乙酸加 NaOH 的 pH 模拟（加一滴或倾倒改变 pH），以及生成可旋转的涡扇 3D 模型。
- 📈 **训练与依据**：页面称其基于 100+ 学习科学论文和 1,000,000+ 辅导示例训练，并引用 Benjamin Bloom 的研究称平均受辅导学生比常规班级领先 98% 的课程进度。
- ⚠️ **范围与限制**：Computer use 被描述为 Mac 应用内面向所有人的能力；浏览器入口未说明具备同等 computer use；屏幕观察仅在 `pill` 打开时进行，例程仅在 DuckyHelper 打开时后台运行。

### [Ding：面向 React、Svelte、Vue 和 JS 的弹簧动效 Toast 通知](https://ding.yusufcengiz.dev/?ref=tailwindweekly.com)

Ding 是一个无依赖、MIT 许可的 toast 通知库，以真实弹簧物理驱动尺寸、形状和文字动画，新调用可在原位变形快速 toast，错误和需要驻留的 toast 默认保持位置；它支持 React、Svelte 5、Vue 3/Nuxt 和原生 JavaScript，并提供 npm 包与 shadcn/ui registry 安装方式。

- 🚀 **多框架发布**：Ding 支持 React、Svelte 5、Vue 3/Nuxt 和原生 JavaScript，对应 npm 包为 @yusufceng1z/ding-react、@yusufceng1z/ding-svelte、@yusufceng1z/ding-vue 和 @yusufceng1z/ding，也可通过 npx shadcn@latest add @ding/ding 从 shadcn/ui registry 安装。
- 🧩 **弹簧物理**：尺寸、形状和文字由弹簧求解器驱动；动画被打断时保留动量，新的调用会让快速 toast 在原位变形。
- 🔄 **驻留策略**：错误 toast 和其他 held toast 默认保持原有位置，避免新通知把它们挤走。
- 🛠️ **零依赖**：无需导入样式表，也没有依赖，样式由 JavaScript 注入；项目采用 MIT 许可。
- 🎨 **主题与布局**：提供浅色、深色和跟随系统主题，六种位置及从右到左布局；颜色和圆角通过 CSS 变量暴露，便于重设样式。
- 📦 **富内容**：支持 description、avatar、buttons、progress bar、countdown line 和尾部小文本等内容。
- ♿ **可访问性**：默认使用 live regions、键盘关闭，并适配 prefers-reduced-motion。
- 📚 **文档与示例**：指南覆盖 React、Next.js、Svelte 5、shadcn/ui 和无框架 JavaScript 用法，并提供 loading toast、undo toast、通知 UX、toast 与 snackbar 对比及可访问性指南；Playground 可调样式并复制 CSS。

### [Glance：原生 macOS Markdown 查看器](https://glance.md/?ref=tailwindweekly.com)

Glance 推出 v0.3.0，一款面向 macOS 的原生 Markdown 查看与编辑器，安装包 15.0 MB，采用原生渲染而非 WebView，重点是在 Finder Quick Look 中即时预览 .md，并支持 Mermaid、LaTeX、表格和代码。免费层可永久阅读，Pro 通过一次性买断解锁页面内编辑、表格与图表编辑和源码并排编辑，提供 14 天试用；产品仅支持 macOS 14 及以上的 Apple Silicon，强调离线、轻量和隐私。

- 🚀 **发布定位**：Glance v0.3.0 面向 macOS 用户，定位为原生 Markdown 查看与编辑器，免费阅读、Pro 编辑，应用离线运行。
- 🧩 **原生渲染**：LaTeX 和 Mermaid 由原生引擎渲染，无 WebView，宣称即时渲染。
- 📦 **文件支持**：可打开 `.md`、`.markdown`、`.mdown`、`.mkd`、`.mkdn`，以及源码、JSON、YAML、CSV、日志和纯文本；非 Markdown 文件进入带语法颜色和行号的代码视图。
- 📚 **文件夹模式**：用 `⌘O` 或拖到 Dock 图标打开文件夹，Markdown 文件在侧边栏列出；输入即保存，其他应用中的修改会就地更新，且不会向文件夹添加索引或配置文件。
- 🔍 **快速查看与查找**：Quick Look 扩展支持在 Finder 按空格预览 `.md`；首次打开应用以让 macOS 识别扩展；`⌘F` 查找并高亮全部匹配；双指缩放围绕指针进行。
- 💡 **Pro 编辑**：Pro 可直接在页面上点击输入，或并排查看与编辑 Markdown 源码；支持内联格式、表格单元格与列编辑、Mermaid 源码修改并用 `⌘↩` 更新；保存回同一文件的干净 Markdown。
- 📈 **试用与买断**：阅读永久免费且无需账号；Pro 试用从第一次编辑开始，14 天，无需信用卡或注册，之后回到只读。当前一次性购买 $9.99（原价 $14.99），覆盖最多三台 Mac，包含一年更新。
- 🛡️ **隐私与网络**：仅两类窄用途网络请求：检查 `glance.md` 更新；若拥有 Pro 许可证，启动时通过 Polar 验证。文档链接的网络图片会被下载；无分析或跟踪，更新检查可在设置中关闭。
- ⚠️ **平台限制**：仅支持 macOS 14 Sonoma 及以上的 Apple Silicon Mac；无 Intel 构建，无 iPad 或 iOS 版本，且暂无计划。

### [magpie：一个用于 Claude Code、Codex 和 Gemini CLI 的模型切换器](https://usemagpie.ai/?ref=tailwindweekly.com)

magpie 是一款免费、开源、原生的本机模型网关，让 Codex、Claude Code、Gemini CLI、OpenCode 等编码代理统一接入 DeepSeek、Kimi、GLM、Qwen、Claude、ChatGPT 订阅及本地 Ollama 等模型。它在 `127.0.0.1:3425` 上双向翻译 OpenAI、Anthropic 与 Gemini 协议，并把模型切换、隐私掩码、多账号故障转移和用量统计集中到一个菜单栏应用与 CLI/TUI 中，从而减少多代理、多模型环境下的配置重复和密钥暴露。

- 🚀 **产品定位**：面向编码代理的统一模型接入层，免费、稳定、开源，提供 macOS、Windows 和 Linux 版本；Mac 版下载约 15 MB，基于系统 webview，不含 Electron 或额外运行时，采用 MIT 许可证并在 GitHub 开源。
- 🧩 **协议网关**：本机网关监听 `127.0.0.1:3425`，同时支持 OpenAI Chat、OpenAI Responses、Anthropic Messages 和 Google Gemini 协议，并在两个方向翻译流式输出、工具调用和推理内容。例如 Codex 只使用 OpenAI Responses，Claude Code 只使用 Anthropic Messages，经网关后也能调用其他厂商模型。
- 🎨 **菜单栏换模型**：菜单栏一眼显示每个代理当前使用的模型，点击即可改写该代理的配置文件，且只改被修改的键。Codex 会在自己的 `/model` 列表中获得 DeepSeek 及对应推理强度；Claude Code 可把 Kimi、GLM 或 GPT 映射到 `opus`、`sonnet`、`haiku`；选择原生模型时会恢复原配置；Profiles 可一次切换所有代理，例如 Budget、Focus。
- 🛡️ **隐私掩码**：请求离开本机前，把 `.env`、配置文件和日志中的 API key、私钥、令牌、邮箱、校验和有效的卡号与身份证号等替换为 `{{API_KEY_k3v9x2mq}}` 形式的占位符，并在流式文本和工具调用回复中还原；同一值始终使用同一占位符以保持提示缓存和 thinking 签名有效，值仅存内存，记录只保留类型、长度和首字符，掩码失败则拦截请求；Insights 可并排查看原值与厂商实际收到的内容，也可选用本地模型识别规则找不到的姓名、地址和密码，并支持 Never mask、自定义掩码词以及警告或阻止。
- 🔑 **订阅复用**：已登录的 Claude Pro/Max、ChatGPT Plus/Pro 和 GitHub Copilot 可直接成为 provider，其模型出现在其他代理的选择器中，例如 `claude/claude-sonnet-5`、`codex/gpt-5.5`、`copilot/claude-sonnet-4.5`；不复制令牌，无需粘贴密钥，按代理自身方式刷新登录态。
- 🔄 **多账号容灾**：可加入多个 Claude、ChatGPT、Copilot 或 Grok 账号以及同一厂商的多个密钥并全部启用，按 Smart、In order、In turn、Least used first 策略为每个请求选账号；Smart 默认优先使用最早重置额度的账号，以保留其剩余额度和提示缓存，余额耗尽的密钥停用半小时，被限流的账号按厂商 `Retry-After` 与重置头跳过，失败账号逐次延长退避，并在回复首字节到达代理前切到下一个账号。
- 🧠 **意图路由**：可为模型标注用途，例如“快速问题”或“编写和修复测试”；每轮开始时由一个小而快的模型判断意图，把该轮请求及其工具轮次固定到对应模型。
- 📦 **Provider 预设**：提供 20 个厂商、中转和本地服务器预设，粘贴密钥即可添加，并自动向厂商查询可用模型，新模型在下一次刷新时进入选择器；密钥只保存在 magpie 中。任何支持 base URL 的客户端也可通过 `OPENAI_BASE_URL`、`ANTHROPIC_BASE_URL`、`GOOGLE_GEMINI_BASE_URL` 使用该网关。
- 🛠️ **配置安全**：修改 `settings.json`、`config.toml`、`config.yaml` 时保留注释、顺序和缩进，写入为原子操作；magpie 从不读取 shell 环境变量中的 API 密钥，只使用用户显式添加的密钥。
- 💻 **CLI 与运维**：安装脚本把 `magpie` 命令放入 `~/.local/bin`，提供 `provider add`、`codex`/`claude`/`gemini`/`opencode` 绑定、`group add` 多 provider 路由、`save`/`use` profiles 和 `tui` 等命令；Windows 提供 `magpie.exe` 与终端专用构建。应用可按代理和模型统计 token、缓存命中与成本，并静默下载更新、重启安装，macOS 版本经过签名和公证。

### [GitHub - velvet-shark/timebar（tailwindweekly.com）· GitHub](https://github.com/velvet-shark/timebar?ref=tailwindweekly.com)

Timebar 1.0.1 是一款用原生 Swift 编写的 macOS 菜单栏静默计时器：启动计时后，菜单栏下方会出现一条细进度线，线的右边缘随时间向左移动，最多只需抬头看一眼就能判断剩余时间。应用不依赖账号、分析上报、网络请求或第三方依赖，采用 universal 构建，包含 Apple silicon 与 Intel 两种架构，要求 macOS 14 Sonoma 或更高版本，并已通过 Developer ID 签名与 Apple 公证，采用 MIT 许可。

- 🚀 **发布与安装包**：Timebar 1.0.1 下载包为 1.73 MB，应用包内文件合计 3.35 MB；universal 版本同时包含 Apple silicon 与 Intel 二进制。交互测试仅在 Apple silicon 上完成，覆盖范围见验证文档。安装时打开 DMG 把 Timebar 拖入 Applications，再从菜单栏计时器图标启动，没有 Dock 图标；首次启动时 macOS 可能要求确认打开下载的应用。
- 🎯 **计时操作**：可直接启动 5、15、25、50、60、90 分钟预设，也可自定义 1 秒到 24 小时；支持按小时、分钟、秒输入，或用步进器和方向键调整，按 Return 或启动箭头开始。菜单内显示剩余时间与百分比，并可暂停、继续、停止、重开。启动新计时会替换当前计时；暂停时进度线停在当前宽度；归零后线消失、菜单图标变为对勾，可选播放轻提示音。
- 🎨 **外观自定义**：默认使用 Subtle：蓝色、1 point 粗、65% 不透明度。可调粗细 0.5 到 8 points（半 point 步进）、六种色板或自定义颜色、不透明度 10% 到 100%、位置（菜单栏下方、顶部边缘或底部边缘）、显示范围（所有显示器或主显示器），以及淡背景轨道、菜单栏倒计时、完成音等附加项。
- 🧩 **覆盖层行为**：在 Retina 屏上 0.5 point 等于一个物理像素，标准分辨率屏幕最低为一个像素。覆盖层从不拦截点击，也不获取键盘焦点。菜单栏自动隐藏时，默认进度线仍在正常菜单区域下方；顶部边缘位置为全屏工作提供替代方案，并避开 MacBook 的刘海。
- ⚡ **性能实测**：在运行 macOS 27.0 的 Apple silicon 桌面上：计时运行、菜单未打开且尚未首次打开过菜单时，平均 CPU 0.067%、物理内存 13.2 MiB；打开并关闭菜单后为 0.033% / 35.3 MiB；菜单可见时为 1.332% / 37.4 MiB。背景采样各持续 30 秒，菜单可见采样持续 15 秒，使用 1 小时 45 分钟计时；这些是 2026-09-22 的测量值而非固定上限，该次运行中打开界面时瞬时内存峰值达 273.5 MiB，低启动数值不代表永久占用。笔记本电池续航未做测量。
- 🔧 **按需刷新机制**：Timebar 只在进度线发生可见变化时安排更新，而不是持续重绘界面；菜单界面在打开时创建、关闭时释放，同时保留用户输入的自定义时长；空闲与暂停的计时器没有计划中的 tick；显示器休眠时只保留完成回调。
- 🔄 **基于截止时间的计时**：计时使用保存的截止时间，因此系统睡眠与延迟回调不会累积漂移。退出应用不会取消计时，只有 Stop 会；重新启动后按截止时间继续计算。若在应用关闭期间到期，会显示为已完成且不播放过期提醒；暂停的计时保持暂停；修改系统时钟会改变基于截止时间的倒计时。
- 🛡️ **隐私与权限**：所有设置与计时状态都保存在 com.velvetshark.timebar 下的本地 macOS 偏好中。Timebar 没有服务器、遥测、广告或后台网络服务，不阻止系统睡眠，也不需要辅助功能或屏幕录制权限。如需登录时启动，先移到 Applications，再到系统设置 > 通用 > 登录项中添加。
- 💻 **源码构建与模块**：需要 Xcode 16 或更高版本与 Swift 6；单架构本地构建也可使用匹配的 Xcode 命令行工具，universal 构建需要完整 Xcode。流程为 git clone 仓库后运行 swift test 与 ./scripts/run.sh，或执行 ./scripts/build-app.sh --universal 输出到 dist/Timebar.app，默认使用本地 ad hoc 签名。TimebarCore 包含确定性计时状态、刷新调度、时长校验、外观设置与显示几何；Timebar 包含 SwiftUI 菜单以及 AppKit 状态项与覆盖层，计时运算与真实时钟、UI 分离，便于无需等待或驱动桌面进行测试。
- 🗓️ **更新方式**：更新时退出 Timebar，下载最新 DMG 并替换 Applications 中的应用，偏好设置与计时状态会保留。安装后可弹出磁盘映像。目前版本为 1.0.1，仓库共 9 次提交，采用 MIT 许可，版权归 Radek Sienkiewicz（2026）。

### [Mailflare — 基于 Cloudflare 和 Docker 的自托管 Google Workspace 替代方案](https://mailflare.co/?ref=tailwindweekly.com)

Custom-Domain Email 是一款面向自有域名的快速、专注型收件箱，支持在无限域名和别名下收发邮件，并提供会话、附件、签名、稍后处理、撤销发送、跟进提醒与全文搜索等能力；页面还列出 Cloudflare、Resend、SES 作为相关邮件基础设施或服务。

- 🎯 **产品定位**：面向自定义域名邮箱场景，强调快速、专注的收件箱体验，并支持跨无限域名收发邮件。
- 🧩 **邮件能力**：支持会话串接、富文本格式、附件、别名、签名、snooze、撤销发送和跟进提醒。
- 🌐 **基础设施**：页面列出 Cloudflare、Resend、SES，作为相关邮件基础设施或服务，但未说明具体接入方式。
- 🔍 **寻址与检索**：提供无限域名和别名，并支持全文搜索。
