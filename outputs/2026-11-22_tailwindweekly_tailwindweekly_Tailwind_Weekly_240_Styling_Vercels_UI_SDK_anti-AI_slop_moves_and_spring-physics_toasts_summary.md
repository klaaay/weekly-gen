### [版本发布 · nuxt/ui · GitHub](https://github.com/nuxt/ui/releases?ref=tailwindweekly.com)

**原文标题**: [Releases · nuxt/ui · GitHub](https://github.com/nuxt/ui/releases?ref=tailwindweekly.com)

Nuxt UI 近期发布 v4.9.0 至 v4.13.0，重点新增多种交互与数据展示组件，强化 Chat/AI 能力、i18n 集成、开发体验与性能，同时修复了关键 Markdown XSS 安全问题。

- ✨ v4.13.0 新增 Toggle/ToggleGroup 按压按钮、ChatPrompt 文件附件与消息队列、useToast.promise 加载提示，以及 ESLint Tailwind 主题检查配置。
- 📊 v4.12.0 新增基于 TanStack Charts 的 Chart 组件，支持 SSR SVG 图表；App 可自动跟随 @nuxtjs/i18n locale，并减少最多 27% 的 JS 体积。
- 🔒 v4.12.1/v4.12.2 修复 GHSA-x9jw-j844-v24h：不可信 Markdown 可能导致 SSR 代码执行和存储型 XSS，建议渲染用户或 LLM 生成 Markdown 的应用升级。
- ↔️ v4.11.0 新增 Splitter 可调整面板布局与 ProgressGroup 分段进度条，并改进动画缓动、减少动效偏好支持和 Vue 组件检测。
- 📦 v4.10.0 新增 InputRating 评分组件，支持图标离线打包与 SSR 即时渲染，Modal/Slideover 支持 unmountOnHide 保留关闭时状态。
- 🧭 v4.9.0 新增 Calendar 月/年选择、useTour 引导式导览、theme.unstyled 默认样式剥离，以及统一 focus-visible 焦点样式。
- 🐛 多个版本持续修复组件可访问性、表单状态同步、表格虚拟化、Chat 流式交互、SSR hydration 和 XSS 等问题。
- ⚡ 性能优化包括减少页面 JS 加载、懒加载浮层、缓存组件主题与 props 计算，并加快按钮和菜单渲染。
- 🌐 本地化方面新增或修正多种语言，包括塞尔维亚语、奥地利语、拉脱维亚语等，并改进多语言可访问性标签。

---

### [发布 · uni-stack/uniwind · GitHub](https://github.com/uni-stack/uniwind/releases?ref=tailwindweekly.com)

**原文标题**: [Releases · uni-stack/uniwind · GitHub](https://github.com/uni-stack/uniwind/releases?ref=tailwindweekly.com)

UniWind 仓库发布页汇总了 v1.14.0 至 v1.10.0 的主要更新，内容涵盖新特性、Bug 修复和性能优化，重点涉及原生/Web 样式兼容、主题与颜色、Metro/Vite/Expo 打包、缓存优化及测试完善；最新版为 11 月 17 日发布的 v1.14.0。

- 🚀 最新 v1.14.0 新增 platform-color() 系统颜色回退、原生 Text 的 line-break/word-break 支持，并修复圆角别名、light-dark scoped theme、原生颜色函数变量解析等问题。
- ⚡ v1.14.0 还通过缓存 CSS 变量归一化、原生样式记录和 data-[…] 变体样式提升性能，并补充文本装饰与 mix-blend-mode 测试。
- 🐛 v1.13.2（11月5日）修复 Metro 导入 CSS 跟踪时误处理生成的 uniwind.css，以及初始主题竞态条件。
- 🔧 v1.13.1（10月28日）修复原生 transform 旋转角度、Tailwind 导入选项、React Compiler 下 useUniwind 同步、Web scoped 变量重复变更，并优化缓存键排序。
- ✨ v1.13.0（10月19日）新增原生样式匹配谓词和原生 CSS 级联顺序支持，修复 React Native 导出、测试主题泄漏、空字体变体及 Metro 热重载依赖跟踪。
- 🩹 v1.12.x 系列修复 Web 样式加载监听、根解析器状态重置、InputAccessoryView 循环依赖/Web 缺失、媒体查询边界和 uniwind.css 原子写入，并支持 fontVariationSettings 与 textAlign start/end。
- 🎨 v1.12.0 与 v1.11.0 增加 drop-shadow 滤镜、iOS/RN 0.87 canary 滤镜、scoped variables，修复 useSyncExternalStore 生命周期兼容、Web 懒加载 CSS 热重载和 RN 0.87 类型/打包问题。
- 🛠️ v1.10.x 支持 RTL 安全区域类、min() CSS 函数、多行类名、HTML 主题采用和 Expo 57，并包含多项 Web/Expo/Vite 修复。
- 👥 多个版本迎来新贡献者（如 @JaydeepAgravat、@Wadiou、@mkantautas、@eliotgevers、@juliusmarminge 等），各版本均提供 Full Changelog 对比链接。

---

### [RenderPixels · 来自你的 AI 助手的像素级精确图像](https://renderpixels.com/?ref=tailwindweekly.com)

**原文标题**: [RenderPixels · Pixel-exact images from your AI assistant](https://renderpixels.com/?ref=tailwindweekly.com)

RenderPixels 是面向 AI 助手的图像渲染服务：用户用自然语言让 Claude、ChatGPT 等设计 Instagram 帖子、横幅、Logo 或 favicon，它按平台要求的精确尺寸在真实浏览器中渲染，并返回可直接使用的文件与永久链接。

- 🖼️ 向 AI 助手描述需求即可生成 Instagram 帖子、横幅、Logo、favicon 等，输出尺寸精确、可直接上传。
- 🔌 通过远程 MCP 与 OAuth 连接 Claude、Claude Code、ChatGPT、GrokBot 等，无需 API Key，设置约一分钟。
- ⚙️ AI 将设计写成代码，RenderPixels 在真实浏览器中渲染，并检查文字裁切、字体或图片缺失，便于修正。
- 📐 与 ChatGPT 图像生成器对比：同样提示下 ChatGPT 返回 1731×909、2.5MB PNG；RenderPixels 返回 1200×630、85KB PNG，文字正确且渲染不到一秒。
- 🎨 可保存品牌套件的颜色、字体和 Logo，一次请求生成多种格式，如 Open Graph、Story、Instagram 帖、X header 和 favicon set。
- 🔗 每个文件都有永久 URL，可直接用于网页、meta 标签或消息；聊天中可预览、下载或打开图片。
- 🆓 每月 50 次免费渲染，无需信用卡，按 UTC 每月 1 日重置；超出后购买积分，1 积分=1 次渲染，积分不过期且无订阅。
- 💳 积分包为 2,000/$10、6,000/$25、15,000/$50、40,000/$100；使用 BF2026 可享 20% 优惠至 11 月 30 日，折后分别为 $8、$20、$40、$80。
- ⚠️ 它不生成照片或插画，只渲染 HTML/CSS/SVG，并可引用 https 图片；编辑或重新渲染各计 1 次，完整 favicon set 仍算 1 次。
- ✅ 用户拥有生成图片的商用权，但需拥有字体、Logo、照片等输入素材权利；删除账号会删除渲染文件及链接，需提前下载。

---

### [Style Vercel's UI SDK with Tailwind CSS — HextaUI](https://hextaui.com/blog/style-vercel-ui-sdk-tailwind?ref=tailwindweekly.com)

**原文标题**: [Style Vercel's UI SDK with Tailwind CSS — HextaUI](https://hextaui.com/blog/style-vercel-ui-sdk-tailwind?ref=tailwindweekly.com)

概述总结：Vercel Labs 于 2026 年 11 月发布 UI SDK，提供无样式、可访问的 React/Vue/Svelte/Solid/Web Components 组件；文章基于 `0.1.0-beta.1`，用 Tailwind CSS v4 和 shadcn 风格 token，演示 Select、Popover、Rating、Color Picker 四个组件的样式定制，核心是通过 `data-slot`、状态属性和 CSS 变量接入样式，并处理进入/退出动画与迁移差异。

- 🧱 UI SDK 分三层：`@ui-sdk/core` 负责行为，`definePrimitive` 定义原语与插槽，框架适配器将插槽渲染为可导入的 parts。
- 🎨 样式钩子主要有三类：`data-slot` 标识部件，状态属性表达交互状态，CSS 变量传递类名难以表达的值。
- 🛠️ 全局样式需先声明 `@layer ui-sdk;`，再导入 Tailwind，并用 shadcn 风格 token 与 `@theme inline` 共享主题。
- 🎛️ Select 用 `data-open` 控制触发器，`data-highlighted`/`data-selected` 控制选项高亮与选中，`min-w-(--anchor-width)` 和 `origin-(--transform-origin)` 控制弹层尺寸与缩放原点。
- 🪟 弹层动画用 `data-starting-style` 设入场首帧，用 `data-ending-style` 设退场并保持挂载至动画结束；不要用 `data-closed` 做退出动画。
- 🧭 UI SDK 弹层使用浏览器 top layer，没有 `Portal`/`Positioner`，`z-index` 不决定层级；需要让关闭内容留在 DOM 时可用 `keepMounted`。
- 💨 Popover 可让入场和退场使用不同时长：入场 200ms 滑入并缩放淡入，退场 100ms 仅缩放淡出，`motion-reduce:transition-none` 照顾减动效用户。
- ⭐ Rating 用 `--rating-fill` 绘制半星填充，`data-filled`、`data-partial`、`data-highlighted` 表示星级状态；遮罩应放在内部元素上，避免裁掉焦点环。
- 🎨 Color Picker 用 `--color-picker-color`、`--color-area-background`、`--color-slider-background` 绘制色块、区域和滑杆；渐变变量需写成 `bg-(image:--name)`。
- 🧾 除工具类外，也可用纯 CSS 按 `[data-slot="..."]` 集中管理主题；从 Radix/Base UI 迁移时需替换 open/动画属性名，并删除多余弹层包装。
- ⚠️ 常见坑包括：忘记 `@layer ui-sdk;`、遮罩裁掉焦点轮廓、`--available-height` 不继承、渐变变量缺少 `image:` 类型提示。
- 🧪 文章基于 Vite 8、React 19.3、Tailwind CSS 4.3 和 `@ui-sdk` `0.1.0-beta.1`；SDK 仍为 beta，API 可能变化，安装前需核对版本文档。

---

### [10 anti-AI slop moves for frontend projects going faster than humans can review—Martian Chronicles, Evil Martians’ team blog](https://evilmartians.com/chronicles/ten-anti-ai-slop-moves-for-frontend-projects-going-faster-than-humans-can-review?ref=tailwindweekly.com)

**原文标题**: [10 anti-AI slop moves for frontend projects going faster than humans can review—Martian Chronicles, Evil Martians’ team blog](https://evilmartians.com/chronicles/ten-anti-ai-slop-moves-for-frontend-projects-going-faster-than-humans-can-review?ref=tailwindweekly.com)

AI 生成代码的速度已超过人类审查能力，而模型缺乏长期记忆与生产责任。文章面向 TypeScript/React 前端项目，提出 10 项“反 AI 粗制代码”检查：先用契约、类型和边界阻止问题代码产生，再用变异测试、死代码与重复代码检测发现问题，最后通过 CI 强制执行，并建议渐进式落地，避免规则一次性全开导致团队放弃。

- 🧠 **核心背景**：AI 能一周写出过去一个团队规模的代码量，但不记得昨日约定、不为生产负责，也无法在半年后解释决策；审查与理解责任仍归人类。
- 📜 **API 契约优先**：用 OpenAPI 生成类型、客户端和 Zod 校验，避免模型臆造 `user.fullName` 这类不存在的字段；前提是契约权威且后端持续维护。
- 🔒 **严格 TypeScript**：开启 `strict`、`noUncheckedIndexedAccess`、`exactOptionalPropertyTypes`，迫使代码显式处理空数组、缺失字段和可选属性。
- 🧹 **把 Linter 当行为过滤器**：重点使用 sonarjs、检测多余 Effect 的规则、Vitest/Playwright 测试规则、jsx-a11y，以及禁止 `any`、非空断言、缺失返回类型等 TypeScript 规则。
- 🧱 **预设分层边界**：用 eslint-plugin-boundaries、dependency-cruiser 或 oxlint 限制依赖方向，例如组件可依赖服务、服务不可依赖组件，设计系统与业务状态隔离，mock 不进入生产构建。
- 🩹 **把重复错误变成自定义规则**：自定义规则成本已大幅降低；行为过滤器用于抵消 AI 默认习惯，“伤疤规则”用于记录真实事故，若说不出事故就不要写规则。
- 🧭 **把规则放到模型面前**：通过项目规则文件、skills 和 react-doctor 等在生成时提供约束；但预防是概率性的，不能替代后续检查，分数应作诊断而非目标。
- 🧪 **用变异测试测试测试**：Stryker 故意破坏代码，暴露只覆盖不断言、快照未验证、断言复刻实现、只检查 mock 等弱测试；不要设失败阈值或把分数当 KPI。
- 📉 **用 Knip 找死代码**：AI 更爱加代码而非删代码；Knip 可找未引用文件、导出和依赖，但要定期审查 ignore 列表，并用小型自定义脚本补充可达性、过期 `vi.mock()` 等仓库特有问题。
- 👯 **用 jscpd 找重复代码**：AI 常另写一份实现而不搜索已有 helper；jscpd 查文本重复，标记与逻辑应用不同阈值，语义重复仍需人工判断。
- 🚦 **CI 强制执行**：格式与 lint、`tsc`、单测、PR diff 上的变异测试、构建应拆成独立任务，部署依赖其通过；可跳过的检查等于没有检查。
- 💸 **承认成本**：误报、规则老化、变异测试耗时、自定义检测器维护、新人被大量规则淹没都是代价；错误信息要解释“为什么”和“该怎么改”。
- 🪜 **渐进式推广**：先在新代码/变更文件上以 warning 建立基线，再逐条把抓到真实问题的规则升级为 error，最后才加 CI 门禁，避免数千错误导致放弃。
- 🎯 **适用条件**：代码会存活超过一个季度、作者之外有人读、bug 会影响开发团队之外时更值得；若只做一件事，先上 API 契约，其次变异测试，最后 CI 门禁。
- 🧑‍⚖️ **自动化不能替代判断**：这些检查无法判断功能是否错误、抽象是否过早、状态是否该放 URL、架构与产品品味是否合理；全绿只说明未发现其设计内的问题，不证明有人理解了代码。
- 🛠️ **配套技能**：文章提供 `anti-slop-audit` 评估仓库中各项检查的收益并规划小 PR，`anti-slop-rollout` 每次执行一步，按“先警告、最后 CI 门禁”的顺序落地。

---

### [Better Stack 介绍 ES2027 的四项 JavaScript 特性](https://www.youtube.com/watch?v=DLT6n3wCkuc&ref=tailwindweekly.com)

**原文标题**: [JavaScript's Biggest Update in Years (ES2027) - YouTube](https://www.youtube.com/watch?v=DLT6n3wCkuc&ref=tailwindweekly.com)

Better Stack 的视频介绍了 JavaScript 在日期时间、资源清理、迭代器和并发方面的更新。这段摘要依据周刊导读整理。[Tailwind Weekly 第 240 期](https://tailwindweekly.com/issue-240/)

- 📅 `Temporal` 提供日期、时间和时区处理 API。
- 🧹 `using` 声明让可释放资源在离开作用域时自动清理。
- 🧩 `Iterator.zip` 将多个可迭代对象的元素按位置组合。
- ⏳ `Atomics.pause` 为自旋等待循环提供提示。
- 🧪 视频还介绍了 `import defer`、`Promise.allKeyed` 和仍处早期阶段的 signals 提案。

---

### [DuckyHelper：理解一切。做任何事。](https://www.duckyhelper.com/?ref=tailwindweekly.com)

**原文标题**: [DuckyHelper: Understand anything. Do anything.](https://www.duckyhelper.com/?ref=tailwindweekly.com)

DuckyHelper 是一款面向 Mac 的语音 AI 助手，按下 fn 即可唤醒，能查看当前屏幕、口头解释并用标注/黑板/3D 模型展示内容，还能把任务交给它在后台应用内自动完成，用户可继续工作并随时接管或停止。

- 🖥️ **一键唤醒**：在任意 Mac 应用中按 fn 说话，无需切换标签页或复制粘贴。
- 👀 **屏幕理解**：读取当前页面、文件和已打开应用，在具体位置画圈、箭头和标注来讲解。
- 🎙️ **语音互动**：像和旁边的人交谈一样提问，它以语音回答，并可逐步演示。
- 🧠 **多形式讲解**：支持屏幕标注、黑板逐步演算、可视化模拟，以及可旋转的 3D 模型。
- 🤖 **自动执行任务**：说出任务或把悬浮球拖到窗口上，它在后台用独立光标点击、输入、滚动，并标注每一步。
- ⏯️ **后台与可控**：任务在自己的窗口运行，不占用用户鼠标键盘；可随时停止、接管，登录步骤会交还给用户。
- 🔒 **隐私与记录**：不输入密码或卡号，任务记录保存在本机；仅在悬浮球打开时查看屏幕。
- 🗂️ **多任务与例程**：可同时运行多个任务机器人，支持“每个工作日 9 点整理下载文件夹”等定时例程。
- ↩️ **可撤销与仪表盘**：文件任务会说明改动并支持撤销；仪表盘保存对话、任务、绘图、笔记和学习时间。
- 🎓 **学习理念与背书**：强调“先展示、再实践”，基于大量辅导案例和学习科学研究，并获得 YC Startup School、NVIDIA Inception、AWS Activate、Microsoft、OpenAI Daybreak、Anthropic 等支持。
- 💻 **获取方式**：提供 Mac 应用和浏览器版本，可下载体验。

---

### [Ding：适用于 React、Svelte、Vue 和 JS](https://ding.yusufcengiz.dev/?ref=tailwindweekly.com)

**原文标题**: [Ding: spring-physics toasts for React, Svelte, Vue and JS](https://ding.yusufcengiz.dev/?ref=tailwindweekly.com)

Ding 是一个基于真实弹簧物理效果的通知（Toast）库，支持在新调用时原位变形、错误等常驻通知默认保持位置；它无依赖、MIT 许可，并提供 React、Svelte 5、Vue 3 与原生 JavaScript 版本。

- 🌀 **真实弹簧动画**：尺寸、形状和文本由弹簧求解器驱动，动画被打断时仍能保留动量。
- 🧩 **多框架支持**：可用于 React、Svelte 5、Vue 3、Nuxt 和原生 JavaScript。
- 📦 **安装方式**：React 用 `@yusufceng1z/ding-react`，Svelte 5 用 `@yusufceng1z/ding-svelte`，Vue 3/Nuxt 用 `@yusufceng1z/ding-vue`，原生 JS 用 `@yusufceng1z/ding`；也支持 shadcn/ui registry。
- 🪶 **轻量无依赖**：无需引入样式表，样式由 JavaScript 注入，MIT 许可。
- 🎨 **主题与布局**：支持浅色、深色、系统主题，六种位置和从右到左（RTL）布局。
- 🛠️ **易于定制**：颜色和圆角通过 CSS 变量控制，方便重新设计样式。
- 📝 **内容丰富**：支持描述、头像、按钮、进度条、倒计时线和尾部小文本。
- ♿ **默认可访问**：包含 live regions、键盘关闭和 `prefers-reduced-motion` 支持。
- 📚 **配套资源**：提供 React、Next.js、Svelte 5、shadcn/ui、原生 JS 指南，以及加载 Toast、撤销 Toast、Toast UX、Toast 与 Snackbar 对比等文档。
- 🧪 **在线体验**：可通过 Playground 调整 Toast 样式并复制 CSS。

---

### [Glance。原生 macOS Markdown 查看器](https://glance.md/?ref=tailwindweekly.com)

**原文标题**: [Glance. Native macOS markdown viewer](https://glance.md/?ref=tailwindweekly.com)

Glance 是一款面向 Mac 的轻量原生 Markdown 编辑器与查看器，v0.3.0，主打即时预览、原生渲染和 Quick Look 集成；阅读永久免费，编辑需购买 Pro。

- 📝 原生编辑/查看 Markdown，支持 Mermaid、LaTeX、表格、代码，渲染美观且无需 WebView。
- 👀 在 Finder 中按空格即可用 Quick Look 预览 .md 文件，⌘F 可查找并高亮所有匹配项。
- 📂 可打开整个文件夹，Markdown 笔记显示在侧边栏，输入时自动保存，外部修改也会同步更新。
- ✍️ Pro 支持页面内直接编辑、⌘\ 源码并排、表格就地编辑和 Mermaid 图源修改，并保存干净 Markdown。
- 🔍 支持围绕指针的智能捏合缩放；代码、JSON、YAML、CSV、日志等有语法颜色和行号。
- 💾 体积仅 15.0 MB，离线可用；仅检查更新和验证 Pro 许可，无分析、无跟踪。
- 🆓 阅读免费且无需账号；Pro 提供 14 天试用，无需银行卡或注册，之后一次性 $9.99，最多三台 Mac，含一年更新。
- 🖥️ 支持 macOS 14 Sonoma 及更新版本，仅 Apple Silicon；无 Intel、iPad 或 iOS 版本且暂无计划。
- 📄 支持 .md、.markdown、.mdown、.mkd、.mkdn，以及代码/配置文件等文本格式。
- ⭐ 用户评价其轻量、Quick Look 集成出色，适合快速查看 README，Mermaid 与 LaTeX 渲染在同体积产品中表现突出。

---

### [magpie：一个适用于 Claude Code、Codex 和 Gemini CLI 的模型切换器](https://usemagpie.ai/?ref=tailwindweekly.com)

**原文标题**: [magpie: one model switcher for Claude Code, Codex and Gemini CLI](https://usemagpie.ai/?ref=tailwindweekly.com)

magpie 是一款免费、稳定、开源的原生工具，让每个 AI 编码代理都能统一接入并使用任意模型：只需添加一次提供商，即可在 Codex、Claude Code、Gemini CLI 等代理中一键切换，并通过本机网关完成不同 API 协议的双向翻译。

- 🧩 统一接入：每个代理、每个模型集中管理，支持 DeepSeek、Kimi、GLM、Qwen、OpenRouter、Ollama 以及已付费的 Claude/ChatGPT 计划等。
- 🔁 一键切换：在菜单栏查看并修改各代理所用模型，仅重写对应配置项，下次会话生效。
- 🌉 本地网关：兼容 OpenAI Responses/Chat、Anthropic Messages、Google Gemini，处理流式输出、工具调用与推理内容。
- 🗂️ 配置与档案：精细编辑 `settings.json`、`config.toml`、`config.yaml`，保留注释与格式并原子写入；支持一键切换多代理配置档案。
- 🔐 隐私掩码：请求离开本机前将密钥、令牌、邮箱、卡号等替换为占位符，回复中再还原，且不落盘、可审计。
- 🔑 订阅共享：Claude Pro/Max、ChatGPT Plus/Pro、GitHub Copilot 等登录可成为提供商，供其他代理复用。
- 🧠 智能路由：按意图选择模型；多账号按重置时间、额度、限流与故障自动切换和失败转移。
- ⚙️ 提供商预设：粘贴密钥即可添加约二十种厂商、中转与本地服务，并自动刷新可用模型列表。
- 💻 轻量原生：约 15 MB，无 Electron，MIT 开源，支持 macOS、Windows、Linux，并自动更新。
- ⌨️ 终端支持：提供 TUI 与 CLI，可通过命令添加提供商、为代理指定模型、管理分组与档案。
- 📊 用量洞察：按代理和模型查看 token、缓存命中与成本。

---

### [GitHub - velvet-shark/timebar 在 tailwindweekly.com · GitHub](https://github.com/velvet-shark/timebar?ref=tailwindweekly.com)

**原文标题**: [GitHub - velvet-shark/timebar at tailwindweekly.com · GitHub](https://github.com/velvet-shark/timebar?ref=tailwindweekly.com)

Timebar 是一款原生 macOS 菜单栏计时器应用，通过菜单栏下方的细进度线直观显示剩余时间；它主打安静、轻量和隐私友好，使用 Swift 编写，无账户、无分析、无网络请求、无第三方依赖。

- ⏱️ 启动计时后，菜单栏下方会出现一条细线，右边缘随时间向左移动；归零时线条消失，菜单栏图标变为勾选。
- 🕒 支持 5、15、25、50、60、90 分钟预设，也可自定义 1 秒至 24 小时；可从菜单暂停、继续、停止或重启。
- 🎨 可调线条粗细、颜色、透明度、位置和显示屏幕，还可开启背景轨道、菜单栏倒计时和完成提示音。
- 🖥️ 要求 macOS 14 Sonoma 或更高版本；下载包为通用版本，包含 Apple 芯片和 Intel 二进制，已由 Apple 公证。
- 🔒 设置和计时状态仅保存在本地 macOS 偏好设置中，无服务器、遥测、广告或后台网络服务，也不需要辅助功能或录屏权限。
- ⚡ 后台资源占用较低；官方测量显示菜单关闭时平均 CPU 约 0.033%–0.067%，但内存峰值和电池续航未作最终结论。
- 💤 计时基于保存的截止时间，睡眠或回调延迟不会累积漂移；退出应用不会取消计时，停止才会。
- 🧱 源码分为 TimebarCore 和 Timebar，分别负责可测试的计时逻辑与 SwiftUI/AppKit 界面；构建需 Xcode 16 或更高版本及 Swift 6。
- 🧪 提供 `swift test` 和构建脚本，可生成本地或通用 macOS 应用包；发布流程支持 Developer ID 签名、公证和 DMG 打包。
- 📄 项目采用 MIT 许可证，版权归 Radek Sienkiewicz 所有，仓库约有 15 个 Star。

---

### [Mailflare — 基于 Cloudflare 和 Docker 的自托管 Google Workspace 替代方案](https://mailflare.co/?ref=tailwindweekly.com)

**原文标题**: [Mailflare — Self-Hosted Google Workspace Alternative on Cloudflare & Docker](https://mailflare.co/?ref=tailwindweekly.com)

这是一款面向自定义域名的快速、专注型邮箱服务，支持在无限域名上收发邮件，并提供完整的邮件管理、提醒与搜索能力，兼容 Cloudflare、Resend 和 SES。

- ⚡ 快速、专注的收件箱，可覆盖无限域名
- 📨 使用自有域名收发邮件，支持会话串连
- ✍️ 支持富文本格式、附件、别名、签名等邮件功能
- ⏰ 提供稍后提醒、撤销发送和跟进提醒
- ☁️ 集成 Cloudflare、Resend、SES
- ♾️ 支持无限域名与别名
- 🔍 支持全文搜索

---

