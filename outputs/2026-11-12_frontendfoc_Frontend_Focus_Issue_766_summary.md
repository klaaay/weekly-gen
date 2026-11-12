### [超越视口：Introducing Site Seeing](https://ishadeed.com/article/beyond-the-viewport/)

**原文标题**: [Beyond the viewport: Introducing Site Seeing](https://ishadeed.com/article/beyond-the-viewport/)

内容概述：我将推荐高质量内容，这些内容表达简洁清晰，并配有图表或案例，能带来新知识或有效提醒。

- 📌 用简洁语言清楚解释观点，避免冗长。
- 📊 每篇内容至少包含一个图表或清晰示例。
- 💡 帮助你学到新知识，或提醒你已知的重要道理。
- 🏆 承诺提供顶级质量的内容推荐。

---

### [Site Seeing](https://lab.ishadeed.com/tools/site-seeing/)

**原文标题**: [Site Seeing](https://lab.ishadeed.com/tools/site-seeing/)

响应式设计不应只关注视口大小，还需考虑用户访问网页时的多种真实环境与交互状态，例如停靠的开发者工具、打开的软键盘、应用内浏览器和分屏视图等。内容还介绍了来自 iShadeed Lab 的相关实验，并邀请报名交互式 CSS 布局课程。

- 📱 响应式设计不只是适配桌面端和移动端屏幕
- 🧭 用户可能通过停靠的开发者工具、打开的键盘、应用内浏览器、分屏视图等方式浏览网站
- 🔍 iShadeed Lab 的实验展示了多种浏览场景
- 🖥️ 示例场景包括完整浏览器、开发者工具、垂直标签页、垂直标签页加开发者工具、缩放和手机
- 🎓 文中还包含报名交互式 CSS 布局课程的信息

---

### [构建本地 AI 编程工作流 | Master.dev](https://master.dev/courses/local-ai/?utm_source=email&utm_medium=frontendfocus&utm_content=localaicooper)

**原文标题**: [Build a Local AI Coding Workflow | Master.dev](https://master.dev/courses/local-ai/?utm_source=email&utm_medium=frontendfocus&utm_content=localaicooper)

本课程由 Web Dev Simplified/Kyle Cook 主讲，时长约 4 小时 3 分钟，评分 4.9，讲解如何用本地开源模型搭建私有、零按 token 计费的 AI 编程环境：从 LM Studio 安装、模型与量化选择、硬件适配，到接入 VS Code、终端代理和远程访问，帮助开发者摆脱厂商限流、涨价或停服风险。

- 🧠 本地模型已足以支持日常编码，代码不出本机，隐私更强且推理边际成本为零。
- 🖥️ 先决条件：了解代理式 AI 编程，并拥有可运行本地模型的设备，如 Apple Silicon Mac 或带独显的 PC。
- ⚙️ 从安装 LM Studio、开启开发者模式、加载小模型并对话开始，建立本地 AI 基础。
- 🔐 本地 AI 的优势包括隐私、成本可控、可微调和供应商独立；云模型在部分任务上响应更快。
- 🧩 解释神经网络输入、权重、隐藏层，以及训练（调整权重）与推理（固定权重生成输出）的区别。
- 🔤 说明 token、上下文窗口和对话历史重发机制，并演示 temperature、top P/K、min P、seed 对随机性的影响。
- 🚀 硬件上重点关注 CPU、GPU 与显存；GPU（尤其 Nvidia CUDA）更适合 AI，模型需尽量完整放入 VRAM 以避免明显变慢。
- 📦 在 Hugging Face 识别模型家族、命名、参数、任务与格式，检查来源和量化可信度；Mac 优先 MLX 版本。
- 🧠 区分通用/编码、instruct、reasoning、vision、tool calling、embedding/reranker 等能力，并介绍 dense 与 MOE、MTP 多 token 预测。
- 🧮 对比 GGUF 与 MLX 格式及 LM Studio/VLLM 等运行时；用 FP32、FP16、Q8 等解释量化如何压缩模型、影响体积与质量。
- 🧰 根据聊天、编码或自动补全选择上下文窗口，并通过 KV cache 量化、GPU/CPU offload、batch size 等优化内存与速度。
- 🛠️ 在 LM Studio 配置采样参数、最大输出 token 和聊天模板，并用加载时间、首 token 时间、tokens/s、内存占用评估模型。
- 🔌 将 LM Studio 变为本地服务器，推荐 OpenAI 兼容 chat completions API；可接入 VS Code 扩展或手动 JSON 配置，并连接 Pi 终端编辑器。
- 🌐 用 LM Link 或 Tailscale 实现远程访问；也可租用云 GPU 运行开放权重模型，但需权衡隐私与灵活性。
- ✅ 结课建议从 Qwen 较小模型入手，再按硬件逐步尝试更大模型；完成课程可获得证书。

---

### [现代 Web 指南 1.0：你的编码智能体所缺失的 Web 平台专业知识 | 博客 | Chrome 开发者](https://developer.chrome.com/blog/modern-web-guidance-v1)

**原文标题**: [Modern Web Guidance 1.0: The web platform expertise your coding agent is missing  |  Blog  |  Chrome for Developers](https://developer.chrome.com/blog/modern-web-guidance-v1)

Modern Web Guidance 1.0 已于 2026 年 11 月 10 日正式稳定发布。它是 Chrome for Developers 推出的、面向编码代理的 Web 平台专业知识与最佳实践技能库，可将专家经验、浏览器兼容数据和现代 Web 开发建议直接嵌入代理工作流，并已扩展为 Firefox、Edge 共同参与的跨浏览器项目。

- 🚀 **1.0 稳定版发布**：为编码代理提供经过专家审核的 Web 开发最佳实践，帮助生成更快、更无障碍、更安全的代码。
- 🆕 **新增现代化工作流**：可扫描现有 HTML、CSS、JavaScript 和 `package.json`，发现安全升级机会并指导代理修改代码。
- 📚 **指南库扩展**：覆盖数百个已验证的 AI 知识缺口，提供跨浏览器解决方案。
- ✅ **更深入的人工专家审核**：每份指南由内容领域技术负责人签核，用户指南还包含专门的无障碍审查与真实辅助技术测试。
- 📊 **完整评估覆盖**：提供公开评估仪表盘，展示使用 Modern Web Guidance 后相比普通代理的可量化改进。
- 🌐 **跨浏览器协作**：Firefox 和 Edge 加入 Chrome，共同提升跨浏览器兼容性并贡献项目，基于 Baseline 数据持续更新。
- 🧠 **弥补模型常见短板**：重点强化无障碍（键盘焦点、inert、减少动态效果、表单验证）、用户体验、性能和安全性（HTML 净化、CSP、通行密钥）。
- ⚙️ **优先推荐原生 Web 能力**：根据项目浏览器支持目标，推荐更合适的 HTML、CSS 和 API，如 Popover、滚动/滑动交互、页面过渡、Passkeys、Autofill 等。
- 🧰 **可与 Chrome DevTools for agents 配合**：前者提供编码知识，后者提供运行时验证、调试和优化能力，帮助代理减少迭代轮次。
- 🏢 **成功案例显著**：Pensionbazaar/Policybazaar、WeTV、note inc.、MetaMask 在交付速度、性能审计、代码通过率和 PR 审查效率上均取得明显提升。
- 📦 **安装与更新便捷**：运行 `npx modern-web-guidance@latest install` 安装，或运行 `npx modern-web-guidance@latest update` 更新；也可通过 Claude Code、Codex、Cursor、Copilot 等插件市场获取。
- 🤝 **社区与学习价值**：由浏览器工程师、Web 标准和无障碍专家维护，也可作为开发者的学习资源，并欢迎社区贡献指南。

---

### [《网络已然足够》，作者：保罗·福特（Ftrain）](https://ftrain.com/aboard-the-web-is-more-than-enough)

**原文标题**: [The Web Is More Than Enough, by Paul Ford (Ftrain)](https://ftrain.com/aboard-the-web-is-more-than-enough)

浏览器已成为构建丰富应用的强大平台，而且获取这些能力的成本正在快速下降。作者以 TinyLittleOffice 的爆红为例，说明个人开发者如今能低成本、快速地做出功能丰富的 Web 应用；Web Crypto、WebAssembly、WebGL、Web Audio 等内置能力，加上多语言和可访问性基础设施，使 Web 成为极具吸引力的分发平台。文章也讨论了 AI 与软件民主化可能对科技经济、应用商店模式造成冲击，以及软件开发逐渐像写作、价值被重新评估的复杂影响。

- 🚀 TinyLittleOffice.com 上线后流量激增，Cloudflare 免费额度被跑满，作者添加信用卡后吸引约二十万人访问。
- 🗣️ 该项目在 Hacker News 上被批“没意义”，但 GitHub 用户开始提需求和修复建议，《The Register》也做了报道，并短暂进入 Product Hunt 前十。
- 🌐 核心观点是：浏览器是非常强大的应用开发平台，而且使用这些能力的成本几乎每天都在下降。
- 🧩 浏览器内置 Web Crypto、WebAssembly、WebGL、Web Audio 等能力，JavaScript 和 HTML 也足以表达大多数文档功能，PDF.js 还能处理 PDF。
- 💸 作者构建 Web 版办公套件的投入大约只是写一篇长通讯的两倍，托管成本甚至为 0，体现了“快、便宜、好”的开发趋势。
- 🎮 Simon Willison 的浏览器 3D 多人游戏《Battle Drones》被作为例证：非游戏开发者也能做出可离线运行、带多人功能的 Web 游戏。
- 🧱 这些浏览器技术过去主要为 Google 等大团队设计，个人开发者常被忽视；如今个人也能触及原本庞大复杂的能力。
- 🤖 作者对“AI 泡沫”感受复杂：大公司热衷 AGI 叙事，但如果软件开发者数量扩大 100 倍，可能对科技经济产生巨大冲击。
- 🏪 Web 开发成本降低可能动摇应用商店经济：花几周、零服务器成本就能测试想法，应用商店的高抽成显得不再那么值得。
- ✍️ 软件开发越来越像写作，而写作长期不被付费；软件人员可能也会经历“被持续贬值”的新鲜处境。
- 🛠️ 对需要软件解决实际问题的人和企业来说，这是极好的时代：可以修流程、整理数据库、挖掘工业设备价值，但行业调整仍需要时间。

---

### [State of JavaScript 2026](https://survey.devographics.com/en-US/survey/state-of-js/2026?ref=frontendfocus)

**原文标题**: [State of JavaScript 2026](https://survey.devographics.com/en-US/survey/state-of-js/2026?ref=frontendfocus)

当前提供的内容仅为“Loading...”，没有可总结的文章正文或有效信息。

- ⏳ 内容显示为“Loading...”
- 📭 未包含文章主题、观点或具体细节
- ℹ️ 暂无足够信息可供概括

---

### [Firefox 160 开发者发行说明（稳定版）- Mozilla | MDN](https://developer.mozilla.org/en-US/docs/Mozilla/Firefox/Releases/160)

**原文标题**: [Firefox 160 release notes for developers (Stable) - Mozilla | MDN](https://developer.mozilla.org/en-US/docs/Mozilla/Firefox/Releases/160)

Firefox 160 于 2026 年 11 月 10 日发布，面向开发者的变更主要集中在 WebTransport API、CSS 兼容性、本地语音识别、WebDriver BiDi 一致性、附加组件平台信息，以及多项默认关闭的实验性功能。

- 🧩 HTML 与 JavaScript 无显著变更。
- 🎨 CSS 新增对 `::-webkit-input-placeholder` 伪元素的支持，作为 `::placeholder` 的别名，以兼容相关网站。
- 🌐 `WebTransport()` 构造函数支持 `headers` 选项，可通过 `WebTransport.responseHeaders` 读取响应头。
- 📡 `WebTransport.exportKeyingMaterial()` 更新为符合最新规范，`context` 变为必填，并新增 `outputLength` 参数。
- 📦 `WebTransportDatagramDuplexStream` 支持 `incomingMaxBufferedDatagrams` 和 `outgoingMaxBufferedDatagrams`，替代已移除的非标准高水位属性。
- 🧵 `WebTransport()` 支持 `datagramsReadableType: "bytes"`，可用 `ReadableStreamBYOBReader` 复用缓冲区读取数据报。
- 🗣️ 桌面端 Web Speech API 支持设备端实时语音转文字，覆盖 40 种语言；Android 和云端识别不支持。
- 🚫 非标准 `MozScrolledAreaChanged` 事件不再向网页派发，可通过偏好设置恢复。
- 🧪 WebDriver BiDi 增加厂商扩展的机器可读 CDDL，并修复 `script.message` 上下文、`Set-Cookie` 换行头处理、网络事件性能及用户激活标志等问题。
- 🔌 附加组件的 `runtime.PlatformInfo.arch` 在 ARM64 平台返回 `arm64`，与 Chrome 保持一致。
- ⚙️ 实验性功能包括：`blocking="render"` 渲染阻塞、音视频懒加载、`Speculation-Rules` 响应头、`CSSNumericValue` 算术方法、Canvas 2D 色彩空间支持。

---

### [使用 Web Speech API - Web API | MDN](https://developer.mozilla.org/en-US/docs/Web/API/Web_Speech_API/Using_the_Web_Speech_API#on-device_speech_recognition)

**原文标题**: [Using the Web Speech API - Web APIs | MDN](https://developer.mozilla.org/en-US/docs/Web/API/Web_Speech_API/Using_the_Web_Speech_API#on-device_speech_recognition)

overview summary
本文介绍 Web Speech API 的两大核心功能：语音识别与语音合成（TTS），并通过多个示例说明如何实现语音控制颜色切换、设备端离线识别、语言包安装、上下文偏置提升识别准确率，以及文本朗读、语音选择、语速和音调调节。

- 🎙️ Web Speech API 包含语音识别和语音合成两部分，可用于提升可访问性与交互控制。
- 🗣️ 语音识别从麦克风或音频轨道接收声音，识别成功后返回文本，可用于触发后续操作；主接口为 `SpeechRecognition`。
- ⚙️ 识别实例可配置 `continuous`、`lang`、`interimResults`、`maxAlternatives` 等属性；默认通常使用服务器识别，需联网，存在隐私和性能考虑。
- 🎨 `Speech color changer` 示例：点击按钮开始识别，说出 HTML 颜色词即可改变页面背景；`onresult` 读取 `transcript`，`onspeechend` 停止识别，`onnomatch` 和 `onerror` 处理失败情况。
- 🔒 设备端识别通过设置 `processLocally = true` 启用，避免音频和转写文本发送给第三方；需下载语言包，之后可离线使用。
- 📦 使用 `SpeechRecognition.available()` 检查语言包可用性，使用 `install()` 安装语言包；`available()` 可返回 `unavailable`、`available`、`downloadable` 或 `downloading`。
- 🛡️ `available()` 和 `install()` 受 `on-device-speech-recognition` Permissions-Policy 控制，默认允许同源使用；还可通过 `quality` 检查识别质量等级，如 `dictation`。
- 🎯 上下文偏置通过 `SpeechRecognition.phrases` 设置 `SpeechRecognitionPhrase` 对象，每个对象包含 `phrase` 和 `boost`（0.0–10.0），可提升专有名词或易混词的识别准确率。
- 🔊 语音合成使用 `speechSynthesis` 控制器和 `SpeechSynthesisUtterance`；`getVoices()` 获取可用语音并填充下拉菜单。
- 🗣️ `Speech synthesizer` 示例：输入文本、选择语音、调整语速和音调后调用 `speak()` 朗读；`pause` 事件可报告暂停位置。
- 🧩 部分旧浏览器不支持 `voiceschanged` 事件，需要兼容 `getVoices()` 的返回时机；示例还通过 `onchange` 实时更新显示的语速和音调值。

---

### [无障碍声明现在在 GitHub 有了自己的家 - GitHub 博客](https://github.blog/open-source/maintainers/accessibility-statements-now-have-a-home-on-github/)

**原文标题**: [Accessibility statements now have a home on GitHub - The GitHub Blog](https://github.blog/open-source/maintainers/accessibility-statements-now-have-a-home-on-github/)

GitHub 现已支持在仓库概览页突出显示 ACCESSIBILITY.md，为项目提供记录无障碍目标、已知障碍、支持环境、贡献者预期和问题报告流程的固定位置，帮助用户、贡献者和维护者更易发现并持续维护无障碍信息。

- ♿ GitHub 可识别仓库根目录、`.github/` 或 `docs/` 中的 `ACCESSIBILITY.md`，也可继承组织 `.github` 仓库中的声明。
- 🧭 公开仓库可通过 `Insights > Community Standards` 使用简洁模板添加或提议无障碍声明。
- 🏷️ 新仓库默认包含 `accessibility` 问题标签，便于维护者组织和跟踪障碍报告。
- 📌 无障碍声明为项目提供长期、可维护的信息入口，减少信息散落在 issue、审计报告、团队知识和对话中的问题。
- 🧑‍💻 GitHub CLI 与 GitHub Annotation Toolkit 的示例展示了如何记录设置、已知限制、变通方法和贡献者期望。
- 📝 建议记录优先级与目标、贡献者检查要求、无障碍障碍报告路径、响应流程、支持环境、已知限制、维护责任和反馈改进方式。
- 🔍 报告流程应直接且无障碍，不要求披露残障、截图或录音；可邀请提供任务、页面、观察到的行为、浏览器、操作系统和辅助技术等上下文。
- ⚖️ 可指定 WCAG 版本和级别作为目标，但目标不等于已验证符合性；符合性声明需说明评估范围、日期、方法和评估者。
- 🌱 没有固定格式；应从准确且可维护的信息开始，参考 Open Source Accessibility Toolkit 和 GitHub 社区标准模板并按项目情况调整。

---

### [Zigzag：一款轻量级的 Mac 网页浏览器](https://zigzagbrowser.com/)

**原文标题**: [Zigzag: A Lightweight Web Browser for Mac](https://zigzagbrowser.com/)

Zigzag 是一款免费开源的 native Mac 浏览器，主打侧边栏标签页与“空间”分组，面向 Arc 用户快速迁移；基于 macOS 自带 WebKit，体积轻量，强调隐私与可持续使用，目前处于 beta 阶段。

- 🧭 侧边栏管理标签页，并按“空间”分组，用颜色区分工作与生活，支持滑动切换。
- 🔎 命令栏统一搜索标签页、历史记录和网页；⇧⌘\ 可一次查看所有空间并输入筛选。
- 🪟 支持分屏视图：把标签拖到页面上即可并排查看两个页面。
- 👀 Peek 功能：Shift-点击链接可快速预览；另有阅读器模式去除杂乱内容。
- 🎨 每个空间可自定义颜色、玻璃效果和颗粒质感。
- 🧩 支持从 Chrome 网上应用店安装多数热门扩展，包括 Tampermonkey 和用户脚本。
- 🔐 内置广告拦截默认开启，支持 Keychain 与 Touch ID 的密码/通行密钥，以及整页翻译。
- 📥 可从 Arc 及另外九款浏览器导入；Arc 的空间、固定标签、收藏、历史和密码可一步迁移，但打开的标签不会带过来。
- 🪶 使用 macOS 已有 WebKit，无需自带浏览器引擎；应用体积约 18 MB，明显小于 Orion、Zen、Arc、Dia、Chrome 等。
- 🛡️ 无账号、无分析、无遥测，所有网络连接都会列出；不依赖服务器，即使停止维护也仍可继续使用。
- 🧪 目前是 beta，日常浏览可用但仍在打磨；更新自动安装，支持 macOS 15.4 或更高版本。
- 💡 灵感来自 Arc，但从零构建，采用 Safari 引擎与自有设计，并非 Arc 复制品，也与 The Browser Company 无关联。

---

### [使用 CSS 布局进行计算](https://noscript.ing/compute)

**原文标题**: [Computing with CSS Layout](https://noscript.ing/compute)

overview summary
文章介绍把 CSS 布局引擎当作计算器的思路：利用容器查询单位、@property、grid/flex、anchor 等机制，把 auto 列的最大值、flex 行的求和、order 的排序和锚点距离读取为数字，再反馈给样式计算；并延伸到按索引取项、排序、排名等原语、性能对比、受 D3 启发的 dCSS 数据驱动样式表、浏览器支持与未来特性。

- 🧮 浏览器每帧运行高度优化的布局算法；auto 列取最宽元素相当于最大值，flex 行宽度相加相当于求和，order 按数字排序。
- 📏 给元素设置 `container-type: inline-size` 可成为查询容器；`100cqw` 表示其宽度，`round(100cqw / 1px)` 可把长度转为无单位整数。
- 🧾 用 `@property` 把 `--result` 注册为 `<integer>`，查询容器内元素继承该数字，并用 counter 打印出来。
- 📍 通过 `right: anchor(--target left)` 等锚点定位，可把两元素间距离读成数字，例如 flex 行中两个 bar 的宽度和。
- 🗂️ 一个 auto 网格列会增长到最宽元素，查询容器可读取 `max(60, 200, 150) = 200`，无需手写 `max()`。
- 🧩 计算可嵌套：flex 行宽度是子项和，auto 列取最宽行，于是可读出 `max(60 + 200, 150 + 35 + 45) = 260`。
- 🔁 布局得到的数字可再用作宽度、`order`、`grid-column` 或新计算；但使用结果的元素必须位于读取它的查询容器内部。
- ⚖️ 比较大量元素时，逐对写 `calc()` 成本高；让每个值的 `order` 参与排序，可让浏览器完成比较，再结合 `calc()` 做其余数学。
- 🔢 原语“按索引取项”：用 `grid-column: var(--i)` 把查询容器放到第 i 列，读取第 i 项宽度。
- 🏅 原语“排序”：每个 item 的值同时作为 `order`，网格按从小到大排列；查询容器放在中间列可读中位数。
- 📊 原语“排名”：排序后每项占 100px 列，用锚点从网格左边缘拉伸到目标项，距离除以 100px 即前面项数。
- ⚡ Chrome 300 个变化数字的测试中，`calc()` 加布局通常更快且 CSS 更小：如按索引 99.1ms/31KB→3.9ms，排名 95ms/5MB→6ms，排序 36.8ms/1.8MB→3.2ms。
- 🧱 dCSS 是受 D3 启发的开源数据函数库：数字放自定义属性，布局/`calc()` 计算结果；函数作为 class 用在 `figure` 上，`ul/li` 存值，`output` 打印答案。
- 📈 dCSS 可用于 summarize（和、均值、最值、方差等）和图表：用 `dcss-max` 读取最大值，让 y 轴、网格线和柱子按最大值缩放。
- 🌐 支持情况：容器查询单位、`:has()` 已广泛可用；`@property` 2024 新可用；`round()` 等数学函数 2025；锚点、样式查询、`sibling-index()`、视图时间线 2026；长度除长度尚无 Baseline。
- 🚀 未来 `attr()` 可直接从 HTML 取数，`if()` 可让元素按自身数值选择，`@function` 可命名并复用计算；配合视图时间线，CSS 可更像脚本运行计算。
- 🧭 结语：过去无 JS 页面多靠复选框、`:target`、hover 切换；现在布局引擎的数学能力让样式表能完成通常交给脚本的任务，理论上元素和时间足够，CSS 可计算任何东西。

---

### [系统颜色需要协同工作 :: Aaron Gustafson](https://www.aaron-gustafson.com/notebook/system-colors-need-to-work-together/)

**原文标题**: [System Colors Need to Work Together :: Aaron Gustafson](https://www.aaron-gustafson.com/notebook/system-colors-need-to-work-together/)

作者在测试 Web Component 时发现：Android 深色模式下，系统颜色 `HighlightText` 与 `Highlight` 的对比度仅 1.98:1，未通过 WCAG 全部五项阈值；类似问题也出现在 Windows 强制颜色模式。为此他建立了 System Color Study，系统比较不同浏览器、操作系统和偏好下的系统颜色及其预期配对，并呼吁浏览器/系统厂商修复默认配色、邀请用户提交数据。

- 🎯 CSS 系统颜色按用途命名，如 `Canvas`/`CanvasText`、`ButtonFace`/`ButtonText`，但名称本身不能保证前景与背景搭配后可读。
- 📱 具体故障包括 Android 深色模式下的 `HighlightText` 与 `Highlight`，以及此前 Windows 强制颜色模式中标签页界面的类似问题。
- 🧪 System Color Study 收录浅色、深色、强制颜色、更高对比度等设置下的观察结果，供开发者比较系统颜色及其配对。
- 📊 研究提供单个颜色的 sRGB 十六进制值表，也用“Normal/Large”文本和 SVG 表情展示预期前景/背景配对的实际效果。
- ✅ 每个配对显示对比度及五项 WCAG 阈值结果：普通文本 AA/AAA、大文本 AA/AAA、非文本；绿/琥珀/红分别表示全部通过、部分通过、全部失败。
- 🧭 作者建议不要只信颜色名称，而应查找所需角色、检查配对并在实际 UI 中测试；推荐列表要求普通文本 AA 在所有已记录观察中通过。
- 🛠️ 文章向 Chrome、Edge、Firefox、Safari 提出具体修复请求，强调强制颜色模式中的默认前景/背景必须可读。
- 🤝 用户可验证元数据、捕获明暗系统颜色快照并提交 JSON；项目不收集遥测，提交前可自行审查，尤其希望补充 Linux 等未覆盖环境。
- ⚠️ 数据表还提示：`N/A` 表示该浏览器/系统不支持相应关键字；半透明颜色按记录的 `Canvas` 值测量，换背景可能改变对比度。

---

### [实践中的系统颜色](https://aarongustafson.github.io/system-color-study/)

**原文标题**: [System colors, in practice](https://aarongustafson.github.io/system-color-study/)

概述摘要  
这项研究基于真实浏览器与系统快照，检验 CSS 系统颜色关键字在实际配对中的对比度表现，说明“名称代表用途”并不等于“任意环境下都清晰可读”。

- 🔎 研究起因：作者在 Android 上遇到系统颜色对比度差，并有用户反馈 Windows 强制颜色模式下的类似问题，因此系统收集跨平台数据。
- 🧪 研究范围：只覆盖浏览器和操作系统提供的默认配色，包括浅色、深色、强制颜色和高对比主题；不评判用户自定义的功能色方案。
- ♿ 立场说明：这不是反对使用系统颜色；恰恰相反，尤其在 `@media (forced-colors: active)` 中应继续使用它们以尊重用户偏好。
- 📸 数据规模：汇总 34 组快照，并排比较 Android、iPadOS、Linux、macOS、Windows 上不同浏览器与主题下的系统颜色。
- 🎨 观察内容：既比较单个系统颜色及其十六进制值，也比较前景/背景配对，如 `CanvasText` 与 `Canvas`、`ButtonText` 与 `ButtonFace`。
- 📏 评估标准：采用 WCAG 2 相对亮度与 WCAG 2.2 阈值；普通文本 AA 为 4.5:1、AAA 为 7:1，大文本 AA 为 3:1、AAA 为 4.5:1，非文本对比要求为 3:1。
- 🟢 编码提示：绿色表示满足全部列出阈值，琥珀色表示部分满足，红色表示全部不满足；琥珀色应视为“需谨慎”而非必然错误。
- ⚠️ 半透明注意：半透明颜色会因背后背景不同而呈现不同结果，配对评估基于记录时的背景，换背景可能改变结论。
- ✅ 较可靠的普通文本起点：`CanvasText` on `Canvas`、`LinkText` on `Canvas`、`VisitedText` on `Canvas`、`ButtonText` on `ButtonFace`、`FieldText` on `Field`、`MarkText` on `Mark` 在记录的浅色、深色、强制颜色、更多对比四类观察中均满足普通文本 AA。
- 📉 需谨慎的配对：`ActiveText` on `Canvas`、`HighlightText` on `Highlight`、`SelectedItemText` on `SelectedItem`、`AccentColorText` on `AccentColor` 存在失败、不可用或最低对比度很低的情况，最低记录分别可低至 2.86:1、1.53:1、2.56:1、4.21:1。
- 🧭 上下文评估：`GrayText` 用于禁用文本、`ButtonBorder` 用于边界，两者不一定有统一背景，应结合实际组件与场景判断，不能只看单个色块。
- 🌓 强制颜色发现：强制颜色不只存在于 Windows；Firefox 在 macOS/Linux 也可触发覆盖配色，浅色与深色有时会解析为同一强制调色板。
- 🤝 后续参与：作者邀请用户提交缺失浏览器、版本或内置主题的快照，以扩大样本并改进结论。

---

### [自动化调试与 AI 根因分析 | Sentry](https://sentry.io/resources/automated-debugging/?utm_source=frontendfocus&utm_medium=paid-community&utm_campaign=automateddebugging-fy27q4-evergreen&utm_content=newsletter-sponsored-link-resource-hub-learnmore)

**原文标题**: [Automated Debugging & AI Root Cause Analysis | Sentry](https://sentry.io/resources/automated-debugging/?utm_source=frontendfocus&utm_medium=paid-community&utm_campaign=automateddebugging-fy27q4-evergreen&utm_content=newsletter-sponsored-link-resource-hub-learnmore)

overview summary  
Sentry 的自动化调试用 AI 代理把“发现错误—定位根因—生成修复 PR”串成闭环，借助生产上下文提升修复准确性，让开发者主要审核并合并，而不是手动复现和打补丁。

- 🔍 **定义**：自动调试是检测、诊断并修复生产 bug 的代理工作流，尽量减少人工复现与手工修复。
- 🔁 **三步闭环**：检测覆盖 PR 和生产环境；诊断自动追踪根因到具体代码行；修复自动生成补丁并开 PR，还可结合 CI 和评审反馈迭代。
- ⚙️ **流程变化**：Sentry 捕获 bug 后触发 AI 自动化，代理获取 Seer 的根因分析并生成修复，工程师作为 PR 审核者介入。
- 🧠 **上下文优势**：Seer 可利用堆栈跟踪、提交记录、会话回放、日志、指标、源码映射等生产上下文，提高修复准确性。
- 🔌 **代理与工具**：Seer Agent 支持自然语言查询；MCP server 可连接 Claude Code、Cursor 等自有代理；Seer Autofix 自动做根因分析并开修复 PR。
- 🧩 **集成生态**：支持 GitHub、GitLab、Bitbucket、Azure DevOps 等源码管理，并可接入 Slack、Linear、Jira、PagerDuty。
- 🎚️ **自动化可调**：从开发者点击“Find a Fix”并审核 AI PR，到代理夜间自动分诊并自行开 PR，团队可控制自主程度。
- 📈 **价值与案例**：减少手动调试，让任何代理和工作流都能获得生产上下文；文中案例提到 Bolt 将 MTTD 降低 99%、Supabase 每周崩溃减少 60 倍等。
- ❓ **FAQ 要点**：自动根因分析可秒级定位问题；AI 调试依赖生产上下文；支持 MCP 兼容代理；团队可按接受度逐步放权。
- 🚀 **落地方式**：在付费 Sentry 计划中添加 Seer、连接代码库并启用，即可开始自动发现和修复 bug。

---

### [请稍等……](https://css-tricks.com/css-using-declarations-just-once/)

**原文标题**: [One moment, please...](https://css-tricks.com/css-using-declarations-just-once/)

该内容仅为网页加载与请求验证提示，未包含可供总结的文章正文或实质信息。

- ⏳ 页面显示“Loader”，表示内容正在加载。
- 🔒 系统提示正在验证请求，请用户稍候。
- 📄 未提供文章正文、主题或关键信息，无法进一步概括。

---

### [GitHub - j](https://github.com/j9t/css-dedup)

**原文标题**: [GitHub - j9t/css-dedup: CSS declaration deduplicator for maintainability and performance optimization · GitHub](https://github.com/j9t/css-dedup)

CSS Dedup（j9t/css-dedup）是面向 CSS 可维护性与性能优化的声明去重工具，遵循 UDJO 思路，在相同作用域内查找重复声明；默认只报告，启用 `--fix` 时仅在可证明安全时合并，并提供 CLI、配置文件、编程 API 与 PostCSS 插件。

- 🎯 核心原则：同一规范化属性–值对在同一作用域内不应出现于多个规则；工具发现重复并可选择性优化。
- 🔍 报告模式：递归扫描 `.css` 文件或读取 STDIN，展示重复声明、重复选择器、跳过原因和字节估算，默认发现问题时退出码为 1。
- 🛠️ `--fix`：合并安全重复项，原子替换文件；同规则重复保留最后一条，跨规则折叠需通过 intervening-rule 等安全检查。
- 📉 字节权衡：删除声明可省字节，但合并选择器列表会增加字节；报告表并列展示普通、`--aggressive`、`--savings-only` 的估算。
- 💾 `--savings-only`：逐次执行并测量合并结果，回滚会使文件变大的合并，仅与 `--fix` 搭配。
- ⚡ `--aggressive`：允许“可能安全”的合并，如跨同条件 `@media` 块、看似不相交选择器、颜色/角度舍入等价和属性别名；不处理同规则不同值的覆盖回退。
- 🧩 作用域与安全：按根、`@media`/`@supports`/`@layer` 和嵌套规则划分 DRY 边界；默认忽略选择器 hack，并保守跳过无法证明安全的合并。
- 🧼 规范化：忽略空白和大小写等非实质差异，折叠零单位、冗余小数、等价颜色、`font-weight`、简写、时间单位及 `min()`/`max()` 参数顺序；对自定义属性等大小写敏感内容保持谨慎。
- 🖥️ CLI：`npx css-dedup [options] [path…]`，支持文件/目录、STDIN、`--ignore-selector`、`--ignore-path`、`--quiet`、`--exit-zero`、`--config` 等。
- ⚙️ 配置：`css-dedup.config.js` 可设置 `aggressive`、`savingsOnly`、`ignoreSelectors`、`ignoreSelectorsDefaults`、`ignorePaths`、`exitZero`，CLI 参数叠加生效。
- 🧑‍💻 API：`analyze(css)` 返回 findings；`dedup(css)` 返回 css、applied、skipped、bytes；`dedupRoot()` 处理 PostCSS root；`dedup()` 可报告 `sourceMapStale`。
- 🔌 PostCSS 插件：从 `css-dedup/plugin` 引入，可输出 warning 或以 `fix: true` 重写 root，适合构建管线并生成正确 source map。
- 🗺️ 运行建议：源文件阶段利于维护；压缩前用 PostCSS 插件较稳；压缩后用 `--fix --savings-only` 优化实际传输字节；Gzip/Brotli 会显著削弱原始收益。
- ⚠️ Source map：`--fix` 不重建 source map，重写后旧映射会失效；应在压缩器前运行或通过 PostCSS 插件集成。
- 🧪 实现与测试：基于 PostCSS；`npm test` 覆盖分析、合并、CLI、格式与插件，`npm run benchmark` 用于基准测试。

---

### [本地视觉回归测试 | Mainmatter](https://mainmatter.com/blog/2026/11/03/local-visual-regression-testing/)

**原文标题**: [Local visual regression testing | Mainmatter](https://mainmatter.com/blog/2026/11/03/local-visual-regression-testing/)

本文探讨如何用 Playwright 和 Docker 搭建本地视觉回归测试，让 AI 编码代理更快发现 UI 回归并降低截图成本；同时说明其优势、实现方式、代理技能配置及潜在局限。

- 🎯 视觉回归测试用于捕捉“看起来没问题”但实际影响其他页面的 UI 变更，避免登录按钮加粗等改动引发意外回归。
- ⏱️ Percy、Chromatic 等云端工具适合人工审核，但反馈链路长，代理难以直接读取结果，AI 提效后截图量还会显著增加成本。
- 🧪 Playwright 的 `toHaveScreenshot` 可在本地进行视觉比较：首次运行生成基准截图，后续失败时输出预期图、实际图和差异图。
- 🔍 差异 PNG 能让开发者或代理快速定位像素变化，甚至发现需求之外的改动，例如意外移除动画效果。
- 🐳 跨操作系统截图不一致会导致误报，因此建议用 Docker 固定 Linux 环境，官方 Playwright 镜像已包含浏览器和系统依赖。
- ⚙️ 通过 `Dockerfile.visual-tests` 和 `docker-compose.yml` 固定平台与 Playwright 版本，并提供 `pnpm test:visual`、`pnpm test:visual:update` 等统一命令。
- 🤖 可编写代理技能，要求每次视觉变更后运行测试、检查差异，并且仅在变更符合原始需求时更新快照。
- 🧠 更新快照属于破坏性操作，应让代理谨慎判断；可将“运行测试并判断是否符合需求”交给独立子代理，避免上下文污染。
- ⚠️ 本地方案并非万能：视觉回归本身很难，维护质量不足可能反而拖慢开发；提交截图还会快速膨胀 Git 历史。
- 💡 可考虑将基准截图存到 S3 等对象存储，测试前下载、测试后上传，以减少仓库体积；最终需结合团队成本与工作流自行评估。

---

### [构建能理解我们想做什么的界面——Agustin Barrientos](https://agustinbarrientos.com/writing/senior-eye/interfaces-that-understand-what-we-want)

**原文标题**: [Building Interfaces That Understand What We Want to Do - Agustin Barrientos](https://agustinbarrientos.com/writing/senior-eye/interfaces-that-understand-what-we-want)

概述摘要：本文讨论如何用“决策模型”让界面理解用户意图：AI 只从开发者预设的选项中做选择并返回概率，从而兼顾开放输入与结果可控。文章重点介绍 Chrome Decisions API 的本地、免费、私密优势及实验状态，对比多种本地与云端模型，并用游戏 NPC、敏感消息提醒、评论快捷操作等案例说明 UX 设计与阈值策略。

- 🧭 传统界面是确定性的，用户必须自己找到正确按钮或菜单；决策模型可根据自然语言或行为猜测意图，让界面适应用户。
- 🍽️ 核心类比是餐厅：菜单是预设选项，服务员是决策模型。AI 只能从开发者设计的选项中选择，不能自由生成，但仍可能误解，因此需要兜底设计。
- 📊 决策模型与生成式 AI 不同：前者只选预设答案并给出概率，速度快、成本低、结果可控；生成式 AI 更适合复杂开放任务，但更慢、更贵。
- 💻 Chrome Decisions API 可在用户电脑本地运行模型，免费、私密、可离线，所有站点共享同一份模型副本；目前仍是实验功能，需要开启 flag。
- 🗓️ 时间线显示：Chrome 157 将 flag 带入常规版；158 加入 EmbeddingGemma；159 可选择模型；后续 origin trial 与全面开放尚无确定日期，flag 可能在 Chrome 161 后消失。
- 🧠 Chrome 内置模型各有取舍：Gemma 4 更准但较慢，EmbeddingGemma 更快但准确率低；最终正式版会使用哪个模型仍未确定。
- ☁️ 若要在真实网站立即使用，可回退到云端方案，如 Gemini、OpenAI Decisions API、Claude JSON schema、Jev；推荐优先检测 Chrome API，不可用时再降级。
- 🧪 作者用 5 组测试、约 27 万题对比 8 个模型：Jev 1.14 综合准确率最高且快；Gemma 4 on CPU 免费本地但准确率中等；EmbeddingGemma 很快但较弱；云端模型各有优劣。
- ⏱️ 成本与速度差异明显：本地模型零调用费；Jev 百万调用约 47 美元、每次 0.20 秒；GPT-6 Luna 约 84 美元；Claude Haiku 5.5 约 176 美元；Gemini Flash-Lite 约 436 美元。
- 🎮 示例一：游戏 NPC 守卫。玩家自由输入，模型从 7 种反应中选择，代码再结合声望、是否回答问题、置信阈值等规则决定结果，兼顾开放输入与可控性。
- 🔒 示例二：敏感消息提醒。发送前在本地检测消息是否不适合当前频道或受众；输入包含消息、频道、受众，按误报成本设阈值，避免敏感草稿上传云端。
- ⚡ 示例三：评论快捷操作。选中文本后，模型建议“创建任务”“存入日历”“设提醒”或“无操作”；低于阈值时只显示“引用”，响应时间需接近即时。
- 🧩 问题类型主要有 boolean、choice、score。Chrome 使用 DecisionModel，MediaPipe 使用 DecisionMaker，OpenAI 使用 predicate/choice/score，Jev 使用 noul/choice/score，Gemini 与 Claude 则用 JSON schema。
- 🎯 UX 要点：界面应说用户的语言，降低交互成本；模型只返回预设选项，所有展示内容都可审核；阈值需用已知答案的数据测试，并按答错风险调整。
- ⚠️ 局限：小模型在难题、事实知识、选项顺序或措辞变化上表现有限；示例中“模型 + 规则”组合明显优于单模型，因此需持续测试、设置阈值并准备兜底。

---

### [请稍等……](https://css-tricks.com/css-tricks-version-20/)

**原文标题**: [One moment, please...](https://css-tricks.com/css-tricks-version-20/)

当前内容仅为一段加载提示，说明页面正在等待请求验证完成，尚未展示文章正文或更多实质信息。

- ⏳ 页面显示加载器，提示用户耐心等待。
- 🔍 系统正在验证当前请求，可能用于安全校验或访问控制。
- 🚫 正文内容尚未加载，暂无更多可总结的信息。

---

### [SVG 即将迎来突破性升级：关联参数即将上线——Roma 的未润色博](https://blog.kizu.dev/link-parameters-soon/)

**原文标题**: [Groundbreaking Upgrade to SVG is Approaching: Linked Parameters Are Almost Here — Roma’s Unpolished Posts](https://blog.kizu.dev/link-parameters-soon/)

概述：文章介绍 SVG 的 Linked Parameters（链接参数）规范即将落地：它允许从外部 CSS 向 SVG 传入变量，直接控制 SVG 内部样式，从而避免把 SVG 嵌入 JS/React；Firefox、Chromium、WebKit 都在推进实现，作者认为这将显著扩展 SVG 在 Web 中的使用方式。

- 🚀 核心机制：SVG 内部用 `env(--color, pink)` 接收外部值，外部 CSS 通过 `link-parameters: param(--color: deepPink)` 传参。
- 🧩 解决问题：可对外部引用的 SVG（如 `<img>`、`background-image`）进行样式化，减少不可缓存 SVG 打包与 JS 动态渲染。
- 🌐 三引擎推进：Firefox Nightly 已实现，Chromium/Blink 与 WebKit 也在活跃开发中。
- 🦊 Firefox：相关 bug 于 2023-01-24 创建；Tyler Thrailkill 于 2026-03 开始实现。
- 🧭 Blink：Divyansh Mangal 启动、Rahul Singh 继续；Edge explainer 于 2026-06-19 发布，Chromium issue 可追溯到 2023-12-11。
- 🍎 WebKit：Taher Ali 自 2026-07-28 起提交多个 PR；Safari Technology Preview 254（2026-10-08）提及该功能。
- 📜 历史与社区：最早提案可追溯到 2009 年 Doug Schepers 草案，后续有 2018 年非正式草案、Lea Verou 2024 年 issue、作者 2025 年 workaround 文章，以及多篇文章与 Interop 提议推动。
- 💡 意义：作者希望它把现代 CSS 与 SVG 连接起来，让 SVG 可嵌入任意位置、无需打包且可完全外部配置，不再只用于图标。
- ⚠️ 挑战：SVG 仍有性能等问题；作者希望关注度提升能推动浏览器与开发者改进 SVG。
- 🗓️ 规范细节：语法讨论倾向采用类似 `if()` 的冒号写法，旧实验实现可能仍用旧语法；功能“几乎到来”。

---

### [让沉浸式 LLM 聊天体验更无障碍 — Smashing Magazine](https://www.smashingmagazine.com/2026/11/making-immersive-llm-chat-experiences-more-accessible/)

**原文标题**: [Making Immersive LLM Chat Experiences More Accessible — Smashing Magazine](https://www.smashingmagazine.com/2026/11/making-immersive-llm-chat-experiences-more-accessible/)

本文从无障碍设计角度讨论如何让全屏式 LLM 聊天体验对依赖辅助技术的人同样可用，强调聊天界面本质上是 Web 交互，应把实时播报、键盘导航、焦点管理、偏好设置和包容性用户研究作为核心设计内容。

- 🧩 沉浸式 LLM 聊天体验指 ChatGPT、Claude、Copilot 等全屏式 Web/原生应用；其多数实现基于 Web 技术，因此适用 WCAG 与通用无障碍原则。
- ⚠️ 若忽视无障碍，会造成知识、机会、工具、就业和娱乐等方面的排除；应把“排除”理解为数字环境制造的使用障碍。
- 👁️ 软件设计存在强烈视觉偏见；需特别考虑无法看屏或使用屏幕阅读器的人如何输入提示、等待回复并阅读内容。
- 📢 使用专门放在 DOM 末尾的 live region 统一播报新消息，不要给每条 LLM 回复单独加 `aria-live`。
- ✅ 只播报已经完整生成的消息，避免把流式输出逐字播报成混乱、难以理解的体验。
- ⏳ 回复处理中要有非视觉反馈：有文字加载提示时同步播报；无文字动画时，可在提交后约 5 秒播报“Loading”，并每 5 秒重复直到完成。
- ⚡ 回复完成后应立即播报，不必等待下一个加载播报周期；可轮换提示语，避免用户误以为卡死。
- 🔮 `ariaNotify()` 是未来方向，但因浏览器可用性、辅助技术用户升级谨慎和 polyfill 支持范围等因素，当前仍建议优先采用成熟的 live region 技术。
- 🏷️ 在每条消息前加入视觉隐藏标题，如“你说：/Cody 说：”，并用 `article` 包裹消息，帮助屏幕阅读器用户理解消息归属和顺序。
- 🧭 使用 `nav`、`main`、`form`、`aside` 等 landmark 描述整体布局，但避免把每条消息都包成 landmark，以免地标列表过于冗长。
- ⏭️ 提供跳过链接，让用户能快速跳到主对话区、提示输入框或设置区域，减少重复导航负担。
- ⌨️ 将会话列表做成 composite widget：整体只占一个 Tab 停靠点，内部用方向键浏览，并支持 Home/End 与 typeahead。
- 🚫 不建议使用 feed pattern 处理消息流；用 `article` + 视觉隐藏标题更简单、稳定、易维护。
- 🔁 可支持 `Ctrl+F6` / `Ctrl+Shift+F6`（Web）或 `F6` / `Shift+F6`（原生应用）在区域间跳转；焦点应落到输入框或最后一条消息标题，并考虑在设置中说明和允许重新绑定。
- 🔍 检查放大文字和调整窗口后的表现，避免内容裁切或水平溢出；LLM 聊天常用较小字号，更需验证大字号体验。
- 🎛️ 提供偏好设置：可关闭次要操作播报、关闭动画并尊重 `prefers-reduced-motion`、关闭音效并提供原生通知/角标/邮件/应用内横幅等替代方式。
- 🔤 键盘快捷键应可编辑、可关闭、可批量管理，以减少与辅助技术或其他应用快捷键的冲突。
- 📊 对表格和代码块等特殊内容，live region 应播报简明摘要：表格说明行列数与趋势，代码块说明文件名/类型与行数；实际消息仍保留完整语义供回看。
- 🧑‍🤝‍🧑 通过包容性用户研究让残障用户成为自身经验的专家，基于真实反馈超越“合规但不可用”，持续改进体验。

---

### [请稍等……](https://css-tricks.com/re-implementing-nth-child-with-modern-css/)

**原文标题**: [One moment, please...](https://css-tricks.com/re-implementing-nth-child-with-modern-css/)

该文本仅显示一个加载与验证提示页面，未包含可总结的实质性文章内容。

- ⏳ 页面显示“Loader”，表示内容正在加载中。
- 🔒 提示“Please wait while your request is being verified...”，说明请求正在进行验证。
- 📄 未提供具体文章正文、主题或关键信息。
- 🕒 需要等待验证完成后才能访问实际内容。

---

### [Britecharts 3.0：适用于 JavaScript 和 React 的无障碍 D3 图表 | Britecharts](https://britecharts.github.io/britecharts/blog/britecharts-3)

**原文标题**: [Britecharts 3.0: Accessible D3 Charts for JavaScript and React | Britecharts](https://britecharts.github.io/britecharts/blog/britecharts-3)

Britecharts 3.0 已发布，为 JavaScript 和 React 提供基于 D3 的成品图表：选择图表并传入数据，即可获得提示框、动画、加载状态和导出等内置能力。此版本重点提升可访问性，并加入深色模式、TypeScript 类型和面向编码代理的工具，同时拆分包结构并引入破坏性变更。

- 🎯 成品图表：支持柱状图、折线图、环形图、堆叠面积图、散点图、热力图、矩形树图等，默认响应式，统一 API，提供加载状态、跟随指针且不被边缘裁剪的工具提示、`colorMap` 分类配色和 `animationDuration` 动画控制。
- ♿ 可访问性大幅增强：图表具有可访问名称，数据图表会生成视觉隐藏表格，供屏幕阅读器逐格读取；时间序列图表按日期或类别为行、系列为列组织。
- ⌨️ 键盘导航默认支持柱状图、环形图、分组柱状图、热力图、折线图、散点图、堆叠面积图、堆叠柱状图和矩形树图；Tab 进入图表，方向键浏览数据，Home/End 跳转端点，提示框跟随焦点。
- 🌈 无障碍细节：遵循 `prefers-reduced-motion`，提供 Okabe–Ito 色盲友好调色板，并支持 `a11yTitle`、`a11yDescription`；若页面已有同数据表格，可关闭自动生成表格。
- 🎨 主题与导出：通过 `--bc-*` CSS 自定义属性统一控制文本、坐标轴、网格、提示框、图例和加载状态颜色；使用 `color-scheme` 支持亮色、暗色或跟随系统；`exportChart()` 可导出带样式的 SVG 或 PNG。
- 🧩 新增矩形树图：用面积表示总量中的各部分占比，接收 `{ name, value }` 数组，支持标签、提示、动画、加载、导出、屏幕阅读器表格和键盘导航。
- 📊 新增比较能力：堆叠柱状图和堆叠面积图支持 `isNormalized(true)` 归一化为 100%；热力图支持 `xAxisLabels` 与 `yAxisLabels`；柱状图、分组柱状图、堆叠柱状图、刷选和散点图支持负值。
- 🤖 面向编码代理：每类图表提供 `{ chart, config, data }` 形状的 JSON Schema，包装器会校验配置并给出错误建议；提供 agent skill、`llms.txt` 和图表规范指南。
- 📦 包结构拆分：`@britecharts/core` 提供 D3 图表与辅助函数，`@britecharts/wrappers` 提供配置式生命周期层，`@britecharts/react` 提供 React 组件，包含 React 19 与 StrictMode 集成测试。
- 🛠️ 技术栈：基于 D3 v7，附带 TypeScript 类型，支持 ES modules、CommonJS、UMD 与 CDN 构建，打包器可移除未导入的图表。
- ⚠️ 迁移注意：这是包含破坏性变更的大版本，需参考 v2 到 v3 迁移指南；v2 终止于 2.18.2，后续不再计划修补。
- 🤝 开源与社区：采用 Apache 2.0 许可，免费开源；项目需要维护者，欢迎按贡献指南参与图表、包或文档维护。

---

### [Britecharts](https://britecharts.github.io/britecharts/docs/Britecharts)

**原文标题**: [Britecharts](https://britecharts.github.io/britecharts/docs/Britecharts)

Britecharts 是一个基于 D3.js 的成品图表库，提供开箱即用、可访问、可交互的图表，支持通过一个 script 标签、npm 包、React 组件或 JSON 配置快速集成，适用于普通 HTML、各类框架和 AI 编码环境。

- 📊 提供柱状图、折线图、环形图、堆叠图、散点图、热力图、矩形树图、迷你图、子弹图、刷选图等成品图表，并内置 tooltip 和 legend。
- ♿ 默认支持无障碍：屏幕阅读器可读的数据表、键盘导航、减少动态效果适配，以及 Okabe–Ito 色盲友好调色板。
- 🧩 所有图表共享统一配置项，如宽高、颜色方案、加载状态、数字格式、导出和 a11yTitle，减少使用和集成出错。
- ⚡ 可通过 CDN 单脚本引入、npm 安装、React 组件、框架无关 wrapper 或 JSON spec 使用，并支持 schema 校验。
- 🤖 面向编码代理优化：提供 llms.txt、agent skill、JSON Schema，以及可提示修复方式的错误信息。
- 🎨 版本 3 使用 TypeScript 和 D3 v7 重写，拆分为 core、wrappers、react 三个包，支持主题化、暗色模式和 CSS 自定义属性。
- 📤 支持一行调用导出 SVG 或 PNG，并提供各图表数据类型、配置和 React props 的 TypeScript 类型。
- 📱 图表默认响应式缩放，支持负值展示、加载状态、更小的可 tree-shaking 的 ES module 包。
- 🕰️ 项目始于 2015 年 Eventbrite，GitHub 已有 55 位贡献者和超过 3,700 stars，版本 2 仍约每周安装 5,000 次。
- 🛠️ 基于可复用图表模式构建，代码可读可改，并有单元测试和真实浏览器测试覆盖。
- 👥 社区活跃，欢迎通过 issue、D3.js Slack 的 #tool-britecharts 频道和贡献指南参与。
- 📄 项目采用 Apache License 2.0 许可。

---

### [适用于任意规模时间序列工作负载的 Postgres。| Tiger Data](https://www.tigerdata.com/go/trial?utm_source=content-syndication&utm_medium=referral&utm_campaign=frontend-focus-newsletter)

**原文标题**: [Postgres for time-series workloads at any scale. | Tiger Data](https://www.tigerdata.com/go/trial?utm_source=content-syndication&utm_medium=referral&utm_campaign=frontend-focus-newsletter)

Tiger Data 提供面向任意规模时序工作负载的 Postgres 云服务，强调单服务可支撑 3 万亿指标/天、3 PB 数据和 1 千万亿数据点，并提供注册赠金、核心云能力、集成与 enterprise 支持。

- 🚀 面向任意规模时序工作负载的 Postgres 服务，适用于 IoT 等场景。
- 📈 单 Tiger Cloud 服务实测规模：每天 3 万亿指标、3 PB 数据、1 千万亿数据点。
- 💳 新账户注册可获 1000 美元信用额度，有效期 30 天，无需信用卡，仅限新账户。
- 🏢 受数千家 IoT 公司信任。
- ⚡ 通过最多 10 节点副本集分离读写，并用分层 SSD/S3 实现低成本、近乎无限存储。
- 💰 计算与存储解耦，可独立扩缩容，避免为闲置容量付费并优化成本与性能。
- 🛡️ 高可用：多可用区集群、自动故障转移、时间点恢复和跨区域备份。
- 🔐 企业级：SOC 2、HIPAA、GDPR 合规，常开加密、SSO、RBAC 和审计日志。
- 🔍 深度可观测性：查询下钻与仪表盘，指标可发送至 CloudWatch、Datadog、Prometheus。
- ⏱️ 快速开通：几分钟内配置数据库，可用 SQL、CLI、Terraform、Cursor 或 Claude Code 管理。
- 🔌 可接入首选云厂商和更广泛的 Postgres 生态。
- 🏛️ 企业默认就绪：合同化 uptime SLA、区域数据隔离、企业合规认证及 24/7 全球 Postgres 专家支持。
- 📄 页面含隐私、法律、站点地图及 2026 Timescale, Inc.（d/b/a Tiger Data）版权信息。

---

### [This hue shall pass | Colour contrast checker by Clearleft](https://thishueshallpass.clearleft.com/)

**原文标题**: [This hue shall pass | Colour contrast checker by Clearleft](https://thishueshallpass.clearleft.com/)

本文介绍了一款名为“This hue shall pass”的测试版无障碍配色工具，用于审查和优化品牌数字配色方案，通过展示所有颜色组合的对比度通过/失败情况，并帮助用户即时调整亮度，从而解锁更多可用的前景与背景配色组合。

- 🎨 该工具展示所有可能颜色组合的矩阵，并标出哪些组合符合指定的无障碍标准。
- 🛠️ 提供两种调整方式：手动拖动亮度滑块，或用魔棒按钮微调接近达标的组合。
- 🔄 调整某颜色会影响所有涉及该颜色的组合；可复制一行后再编辑，避免影响原始颜色。
- ✅ 并非所有颜色组合都必须通过，只需确保计划搭配使用的前景与背景组合达标。
- 📐 对比度基于 Oklch 数值计算，滑块只调整亮度（L），尽量保留品牌色彩的色相与个性。
- 💡 制作初衷是帮助受限于现有配色、但又希望提升网站无障碍性的组织，在浏览器中即时查看调整效果。
- 🔍 现有对比度检查工具多用于指出问题，而该工具还能当场帮助解决问题。
- 🧪 目前处于 Beta 阶段，细节仍较粗糙，欢迎通过邮件提出改进建议。
- 🙌 灵感来自 Directed Edges 的 Contrast Grid 与 Tanaguru 的 Contrast Finder，使用原生 HTML 和 CSS，并借助 colordx 进行颜色操作。

---

### [修复对比度，同时不丢失品牌 | Clearleft](https://clearleft.com/thinking/fix-the-contrast-without-losing-your-brand)

**原文标题**: [Fix the contrast without losing your brand | Clearleft](https://clearleft.com/thinking/fix-the-contrast-without-losing-your-brand)

低对比度文本是网络上最常见的无障碍问题，文章介绍了其普遍性、真实影响、成因，以及一款帮助团队在保持品牌色感的同时修复对比度的工具“This hue shall pass”。

- 📊 WebAIM 2026 年分析显示，排名前一百万首页中有 83.9% 存在低对比度文本问题，且该统计仅覆盖自动化工具可检测的内容。
- 👥 低对比度会直接影响低视力用户、色觉缺陷用户、老年读者，以及在强光下使用手机的人，使他们难以阅读或识别界面元素。
- 🎨 问题反复出现的原因包括：品牌色板常按氛围和识别度选择，设计不断变化，曾经合格的配色后来可能失效，而修复往往需要设计师手动微调并反复检查。
- 🛠️ 文章团队曾通过小幅调整颜色数值，让品牌色在视觉几乎不变的情况下满足对比度要求，并由此开发了工具“This hue shall pass”。
- 🧮 该工具可导入色板并生成所有颜色组合矩阵，按 AA 或 AAA 标准显示哪些前景/背景配对通过或失败；并非所有组合都需通过，只需实际搭配使用的组合合格。
- 🪄 修复方式有两种：用滑块手动调整明度，或用“魔杖”对接近达标的配对做最小幅度变亮/变暗调整；色相保持不变，修改会同步应用到使用该颜色的所有组合，也可复制颜色进行实验。
- 🔍 工具专注解决颜色对比度这一环节；页面结构、替代文本、表单标签和键盘访问等其他无障碍问题仍需单独处理。
- 💡 工具源于团队自身痛点，结合了品牌色板、开发实现和客户沟通三种视角，并受到 Contrast Grid 与 Contrast Finder 的启发。
- 🚧 目前工具处于 beta 阶段，作者邀请用户试用、反馈问题，并可在项目无障碍受阻时联系团队；文章作者为 Alex Edwards，日期为 2026 年 10 月 7 日。

---

### [GitHub - namipsg/liquid-glass-forge: Open-source WebGL2 and CPU glass refraction for native HTML controls. Vanilla JS, React, Vue, and Angular. · GitHub](https://github.com/namipsg/liquid-glass-forge)

**原文标题**: [GitHub - namipsg/liquid-glass-forge: Open-source WebGL2 and CPU glass refraction for native HTML controls. Vanilla JS, React, Vue, and Angular. · GitHub](https://github.com/namipsg/liquid-glass-forge)

Liquid Glass Forge 是一个开源渲染引擎，可利用可读图像、Canvas、视频或像素源，为普通 HTML 控件实现玻璃折射效果；支持原生 JavaScript、React、Vue 和 Angular，目前以实验性 npm 预览版发布，重点提供 WebGL2/CPU 光学效果、原生可访问性和材质降级。

- 🧊 核心能力：提供折射、模糊、色彩色散、着色和边缘光等玻璃光学效果，并支持显式像素源。
- 🧩 框架支持：可集成 Vanilla JS、React、Vue、Angular，并提供对应的 Provider、组件或指令。
- 📦 包体系：包含 core、cpu、dom、webgl 及 React/Vue/Angular 适配包，统一版本为 `0.1.0-rc.1`。
- ♿ 原生控件：光学层仅作装饰，按钮、输入框、链接和文本仍保留 DOM 语义、键盘操作与无障碍行为。
- 🎨 降级方案：当光学源不可用或需要更高对比度时，可使用 CSS 背景材质或不透明表面。
- 🖥️ 示例丰富：提供在线演练场，以及浏览器控件、视频传输、照片查看器、音乐播放器和交互地图等示例。
- 📊 性能数据：README 记录了 CPU worker、WebGL2 多输出和动态 worker 工作负载的历史测量结果，但广泛设备认证仍未完成。
- 🚧 发布状态：npm 包属实验性，建议固定精确版本，并针对实际素材、布局和目标设备进行测试。
- 🗺️ 路线图：计划推出基于 Forge 的 Web UI 库 ENUI，以及 Flutter 和 Kotlin 实现。
- 📚 文档与贡献：提供 Source API、Host API、核心契约、架构、更新日志和贡献指南，鼓励提交最小复现问题。
- ⚖️ 开源许可：项目采用 MIT 许可证，由 Nami Poursafargholi（Zenixev）创建，灵感来自 Apple 的 Liquid Glass。

---

### [Liquid Glass Forge — A different kind of surface.](https://namipsg.github.io/liquid-glass-forge/#playground)

**原文标题**: [Liquid Glass Forge — A different kind of surface.](https://namipsg.github.io/liquid-glass-forge/#playground)

Liquid Glass Forge 是一个面向 Web 的开源材质引擎，让界面在保持原生 HTML 控件的同时呈现真实光学玻璃效果。它通过 WebGL 与受限 CPU 渲染器对明确来源进行折射、扩散和色散处理，并提供多框架集成、性能基准与设备兼容性说明；目前为实验性 npm 预览，后续将推出基于它的 ENUI UI 库。

- 🧪 **核心定位**：为 Web 提供光学玻璃材质，支持真实折射，同时按钮、表单和链接仍是普通 HTML 控件。
- 🔍 **材质来源**：可处理图像、Canvas、视频或自定义像素源；玻璃只折射明确且 origin-clean 的来源，不会自动栅格化任意 DOM 内容。
- 🌀 **光学能力**：通过 WebGL 渲染器与有界 CPU 渲染器实现折射、色散、模糊、着色和边缘高光，并可塑造圆角与清晰度。
- 🧭 **演示场景**：包含 Apple.com 浏览器研究、视频播放器、照片浏览、音乐播放器和地图等五个可用界面示例。
- 📊 **性能基准**：Galaxy A04s 上 CPU worker p95 完成间隔约 34.3–34.8 ms；WebGL2 四路 640×360 输出 p95 批处理约 13.5–16.3 ms。
- ⏱️ **稳定性测试**：Apple M4 Mac 上 30 分钟 soak 测试中，Vanilla JS、React、Vue、Angular 各适配器完成超过 53,000 帧和 100 次生命周期循环。
- ⚠️ **资格状态**：SwiftShader 和后续 A04s 运行未达时间限制；持续 GPU 与移动端覆盖仍待完善，相关数据仅适用于所列测试活动。
- 🧩 **框架集成**：提供 Vanilla、React、Vue、Angular 四种集成，共享同一来源与材质系统；npm 包仍为实验性预览。
- 📱 **设备覆盖**：Mac、Windows、Android、iPhone 均标注为实验性，iPad 标注为未完成物理设备资格验证。
- ♿ **可访问与回退**：支持键盘操作、可选动效；不透明材质会遵循减少透明度和提高对比度偏好，并保留原生控件行为。
- 🚀 **快速开始**：按框架选择安装命令，先添加 CSS 玻璃表面，可选安装完整 WebGL 光学包并配置折射来源。
- 🗺️ **路线图**：计划推出基于 Forge 的 ENUI Web UI 库，以及 Flutter/Dart 和 Kotlin 实现。
- ✨ **作者与愿景**：项目由 Nami Poursafargholi（AKA Zenixev）创建，强调“光有路径、像素有来源、内容拥有最终决定权”。

---

### [Tinkerfont：字体测试 Chrome 扩展程序与 Firefox 附加组件](https://tinkerfont.com/)

**原文标题**: [Tinkerfont: Font Testing Chrome Extension & Firefox Add-on](https://tinkerfont.com/)

Tinkerfont 是一款用于在真实网站上快速检查、替换和测试字体的 Chrome 扩展与 Firefox 插件，帮助设计师和开发者在修改 CSS 或设计稿前，预览字体在真实内容、布局和断点中的效果。

- 🔍 通过右键菜单查看任意文本的字体规格，并可点击复制字体家族、颜色、对比度或字体文件 URL。
- 🧭 扫描实时 DOM，列出页面实际使用的全部字体及数量，支持按字体家族定位或用 * 全选。
- 🔄 可即时试用 1,900+ Bunny Fonts 字体，或上传自有字体，一键应用到页面，无需 DevTools、部署或账号。
- 🎯 支持将替换范围限定到导航、表格等特定区域，并按域名保存作用域。
- 💾 字体规则按站点持久保存，刷新或稍后回访仍保留，可重新扫描清除。
- 🔗 可分享当前域名下的规则与作用域链接，队友在同一网站粘贴即可复现，也可导出 JSON。
- 🆓 免费安装使用，无需账号，不收集浏览数据；规则、作用域、主题和上传字体均存于本地。
- 🛡️ Bunny Fonts 以内联 data URL 方式加载，通常可绕过严格的外部字体 CDN 限制，但 Chrome Web Store、chrome:// 等受限页面无法运行扩展。
- 📤 支持上传 .woff2、.woff、.ttf、.otf 测试品牌字体；设置可导出/导入，Bunny Fonts 规则导入即用，自定义字体需在新设备重新上传。
- 🌐 官方支持 Google Chrome 和 Mozilla Firefox，部分 Chromium 浏览器或可使用 Chrome 版本，但未官方测试。

---

### [BagUI – 开源 shadcn/ui 组件与区块](https://www.bagui.pro/)

**原文标题**: [BagUI – Open Source shadcn/ui Components & Blocks](https://www.bagui.pro/)

BagUI 是由 Anelka 打造的开源 React 与 shadcn/ui UI 区块库，面向 SaaS 落地页，主打即插即用、可自定义和快速上线。

- 🚀 推出 BagUI v1，定位“开源、共同构建”，帮助开发者更快搭建生产级 SaaS 落地页。
- 🧩 提供手工打造的 React 与 shadcn/ui 区块，可插入、定制并放心发布。
- 📚 UI 区块库包含 Hero 6 个、Feature 6 个、Pricing 4 个、Testimonial 2 个、CTA 2 个、FAQ 1 个、Navbar 4 个、Footer 4 个，共 30 个区块，Blog 即将推出。
- 🛠️ 网站导航涵盖 Blocks、Templates、Changelog、Pricing、Docs、Resources，以及 BagUI MCP 和 VS Code 扩展。
- 🤖 BagUI MCP 可连接 AI 助手；VS Code 扩展支持在编辑器中浏览和安装组件。
- 🆓 提供免费开始入口，邀请开发者加入并使用 BagUI 创建界面。
- ⚖️ 页脚包含产品、更多、法律（License、Privacy、Terms）、联系等信息，版权标注 2026。
- ℹ️ BagUI 与 shadcn/ui 或 Tailwind CSS 无官方关联，由来自刚果（金）的 Anelka Bag 构建。

---

### [GitHub - anelkabag/bag-ui: BagUI is an open-source shadcn/ui registry with production-ready components, blocks, templates, and animations for React, Next.js, and Tailwind CSS. Copy, customize, and build faster. · GitHub](https://github.com/anelkabag/bag-ui)

**原文标题**: [GitHub - anelkabag/bag-ui: BagUI is an open-source shadcn/ui registry with production-ready components, blocks, templates, and animations for React, Next.js, and Tailwind CSS. Copy, customize, and build faster. · GitHub](https://github.com/anelkabag/bag-ui)

BagUI 是一个开源 shadcn/ui 组件注册库，面向 React、Next.js 与 Tailwind CSS，提供可直接用于生产的组件、区块、模板和动画，帮助开发者更快复制、定制并构建精致界面。项目由 Anelka Bag 维护，采用 MIT 许可证，当前获得 513 Stars、42 Forks。

- ✨ 核心定位：提供现代、开源、可复用的 UI 组件与页面区块，如导航栏、Hero、页脚、定价表、CTA 等。
- 🧱 技术栈：Next.js、TypeScript、Tailwind CSS、shadcn/ui 和 Framer Motion。
- 🚀 快速启动：克隆仓库后执行 `npm install`，再运行 `npm run dev`，默认访问 `http://localhost:3000`。
- 🤝 贡献流程：Fork 并创建分支，将组件放入 `registry/default/blocks` 或 `registry/default/ui`，并在 `registry.json` 中注册。
- ✅ 提交前检查：组件可正常渲染、名称唯一、路径与目标配置正确，并通过 `npm run build` 和 `npm run registry:build`。
- 📁 项目结构：`registry/default/blocks` 存放 UI 区块与页面 section，`registry/default/ui` 存放基础 UI 组件，`registry.json` 是组件清单。
- 🔔 发布通知：仅接受 Vercel 生产环境的 GitHub `deployment_status` 事件，首次同步仅建立基线，后续新增才创建邮件活动。
- 🛠️ 通知基础设施：使用 Supabase 持久化队列、`pg_net` 异步派发、`pg_cron` 恢复任务，以及 Resend 发送邮件。
- 🔐 必要配置：需设置 Supabase、Resend、通知分发/Worker、令牌等环境变量，并配置 Resend Webhook 与 GitHub Actions secret。
- 📬 邮件发送机制：Worker 每次最多处理 50 个收件人，带并发控制、投递租约与指数退避重试；管理员可在 `/admin/release-notifications` 查看活动并重试临时失败。
- ⚙️ 用户偏好：已确认账户默认接收产品更新邮件，现有明确退订保持退订，用户可在“Account → Email preferences”中开关。
- 📄 许可证：项目采用 MIT License，欢迎社区贡献。

---

### [精通 CSS 2.0 - 大师](https://master.co/blog/master-css-v2)

**原文标题**: [Master CSS 2.0 - Master](https://master.co/blog/master-css-v2)

Master CSS 2.0 于 2026 年 11 月 9 日发布，核心是让开发者用更具表达力的类名、CSS 定义的设计 token，以及能理解项目设计系统的工具来构建界面，并通过 Fieldwork 示例展示从编写、交付到检查的完整工作流。

- 🚀 **发布与定位**：Master CSS 2.0 将表达型类名、项目 token、可复用样式与理解同一套定义的工具连接起来，强调“你的项目，被理解”。
- 🧩 **类内表达条件**：一个类可同时包含值、选择器和条件，例如 `fg-blue-70:hover@sm`，由浏览器执行生成后的普通 CSS 选择器与媒体查询。
- 🎨 **自有设计系统与宽色域**：提供 17 个色相家族、每族 11 个明暗等级，基于 OKLCH 并覆盖 Display P3 色域；可用 `@theme` 命名品牌色、间距等语义 token。
- 📐 **命名响应式条件**：支持 `@custom-media` 命名视口条件、`@custom-container` 命名容器条件，并可在类中组合 `@reading`、`@container(story_--story-wide)` 等条件。
- 🧱 **原生 CSS 与可复用模式**：预设 `theme`、`base`、`defaults`、`components`、`utilities` 五层级联层；共享组件样式放 `components`，局部调整用 utility。
- ♻️ **按需选择复用方式**：设计值用 `@theme` token，组件样式用原生类，按需类用 `@utility`，声明与条件复用用 `@mixin` + `@apply`。
- 📦 **四种 CSS 交付方式**：默认静态扫描构建；`prerender` 随 HTML 交付生成 CSS；`runtime` 在浏览器生成；`progressive` 先交付初始 CSS，再按需在浏览器补充。
- 📊 **CSS 体积数据**：Master CSS 指南生产构建为 24.5 kB Brotli / 110.4 kB raw（含内联样式与链接样式表），页面生成的 `style#master-css` 块为 833 bytes（压缩前）。
- 🛠️ **编辑器与代码检查**：VS Code 扩展支持类名语义高亮；ESLint 集成推荐规则包括 `sort-classes`、`no-invalid-classes`、`no-conflicting-classes`、`prefer-canonical-classes`，并提供可选团队策略规则。
- 🤖 **AI 项目上下文**：本地 Master CSS MCP 服务可让 Codex、Claude Code、Cursor、Gemini CLI 等客户端查询 token/utility、检查生成 CSS、运行 lint 并预览修复。
- 📓 **Fieldwork 示例**：用一个简朴的线上小期刊展示响应式布局、主题切换、故事展开与静态渲染，说明交互本身不必然需要运行时 CSS 生成。
- ✅ **上手建议**：从一个组件开始，添加状态、命名共享值并检查结果；安装 Master CSS 后可通过 Syntax tutorial 构建第一个界面，并可在 GitHub 上 star 项目。

---

### [Expo 模拟器：](https://expo.dev/services/simulators?utm_campaign=agentic-development&utm_source=email&utm_medium=email&utm_term=Simulators&utm_content=FrontEnd%20Focus)

**原文标题**: [Expo Simulators: Simulators built for agents](https://expo.dev/services/simulators?utm_campaign=agentic-development&utm_source=email&utm_medium=email&utm_term=Simulators&utm_content=FrontEnd%20Focus)

Expo Simulators 是面向 AI 代理的云端 iOS 模拟器与 Android 模拟器服务，可按需启动安全隔离的会话，让代理安装构建、操作应用并自行验证，并支持大规模并行测试。

- ☁️ 按需启动云端 iOS/Android 模拟器，代理可安装构建、点击主界面、截图和录屏，完成自验证。
- ✅ 每次 PR 可附截图、会话录像和构建链接，便于评审查看证据并体验实时构建。
- ⚡ 默认支持并行，按需扩展至 iPhone、Android、折叠屏和平板，共享账户并发与队列。
- 🔒 会话运行在隔离环境，预览链接受访问控制，凭证按会话作用域管理。
- 🧩 安装 Expo Skills 中的 eas-simulator 技能；用 `eas simulator:availability --json` 检查权限，再通过 `eas simulator --platform ios` 启动会话。
- 🛠️ 支持任何能运行 shell 命令的编码代理（如 Claude Code、Codex、Cursor），不要求应用使用 Expo，兼容 React Native、Swift、Kotlin、Flutter、Unity 等构建。
- 🔁 可接入 GitHub Actions、Expo Workflows 或其他 CI，通过 EAS CLI/REST API 安装构建、运行检查并收集结果；也支持 Appium 和部分 Maestro 流程。
- 🧪 典型场景包括 Agentic CI 自动模拟流程与修复、灵感落地后快速验证、测试反馈后的缺陷复现与修复。
- 👥 团队可在浏览器共享实时模拟器会话进行评审，并将截图/录像链接附加到 PR；会话停止后端点不可用。
- 📦 Expo/React Native 应用可借助指纹匹配和重打包最新 JS 避免每次改动都完整重建；开发期可连接 Metro 使用 Fast Refresh。
- 📝 产品页提供加入等待名单入口，并强调其与 Expo Build、Submit、Workflows 使用同一基础设施。

---

### [面向静态网站的托管表单，无需后端 | CraftForms Cloud](https://craftforms.app/developers/?utm_source=frontendfocus&utm_medium=newsletter&utm_campaign=ff-2026-11-11-classified)

**原文标题**: [Hosted Forms for Static Sites, No Backend | CraftForms Cloud](https://craftforms.app/developers/?utm_source=frontendfocus&utm_medium=newsletter&utm_campaign=ff-2026-11-11-classified)

CraftForms 是面向静态网站的无后端表单方案：用可视化编辑器建表，粘贴两行 HTML 即可嵌入任意站点，免费计划也支持无限提交，并支持预约、实时价格与定金。

- 🧩 无需后端运行，静态站点也能收集表单提交，免费计划即可无限提交
- ✍️ 可视化编辑器搭建表单，复制两行 HTML 嵌入任意网站
- ⚡ 字段与价格运行时加载，改价格或字段无需重新构建站点，也无需调整 iframe
- 🔐 每个表单有绑定网站的唯一密钥，防止他人复制表单到其他站点
- 🌍 托管在欧盟，支持 localhost 与 127.0.0.1 任意端口测试，不占用套餐网站名额
- 🧱 纯 HTML 片段兼容 Astro、Hugo、Eleventy、Next 静态导出、Cloudflare、Netlify、Vercel 等
- 🔌 也可用 `fetch()` 以 JSON 提交，自行展示感谢或错误信息；浏览器提交仅限注册网站或 localhost，服务器无 Origin 可任意提交
- 🛡️ 无验证码反垃圾：通过填写行为检测、按地址和表单限流，访客无需解题，也无需第三方验证码
- 💳 所有计划均无限提交；差异在表单数、网站数、通知邮件量与是否支持支付
- 🆓 Free €0:1 个表单、1 个网站加 localhost，每月 100 封通知邮件，不支持支付与文件上传
- 🚀 Solo €6/月：首 30 天免费，25 个表单、1 个网站，每月 2,000 封邮件或自有 SMTP，支持 Stripe/PayPal 支付与文件上传
- 🏢 Studio €22/月：200 个表单、25 个网站，每月 10,000 封邮件，含 PDF 构建器，适合代理机构
- 🚧 限制：表单链接仅在 forms 地址；Solo/Studio 表单可有独立页面但暂不支持自有域名；内置集成仅 Mailchimp 与 Brevo，其他走 webhook；暂不支持普通 HTML form post
- ✅ 免费开始无需信用卡，注册并确认邮箱后即可创建表单、添加 localhost 并在开发服务器测试

---

### [Adobe Sign API 替代方案：更快交付嵌入式签名](https://developer-api.foxit.com/developer-blogs/api-guides-tutorials/adobe-sign-api-alternatives-embedded-signing/?utm_source=draftdev&utm_medium=newsletter&utm_campaign=frontendfocus_20261111)

**原文标题**: [Adobe Sign API Alternatives: Ship Embedded Signing Faster](https://developer-api.foxit.com/developer-blogs/api-guides-tutorials/adobe-sign-api-alternatives-embedded-signing/?utm_source=draftdev&utm_medium=newsletter&utm_campaign=frontendfocus_20261111)

本文介绍 2026 年面向开发者的 8 款 HelloSign（现 Dropbox Sign）API 替代方案，重点对比价格、计费触发条件、Webhook 和 SDK，并提供迁移清单，帮助团队在切换前评估工作量。

- 📌 Dropbox Sign 的嵌入式签署功能被放在每月 250 美元的 Standard 套餐中。
- 🏷️ 白标功能需定制报价，未包含在标准套餐内。
- 🔍 指南对比 8 款 HelloSign API 替代方案。
- 💰 对比维度包括定价与计费触发条件。
- 🔗 同时评估 Webhook 支持与 SDK 易用性。
- ✅ 提供迁移清单，便于切换前明确工作范围与成本。

---

### [请稍等……](https://shkspr.mobi/blog/2026/11/blunt-banhammer-blocks-basic-bots-ballistically/)

**原文标题**: [One moment, please...](https://shkspr.mobi/blog/2026/11/blunt-banhammer-blocks-basic-bots-ballistically/)

页面处于加载状态，正在等待请求验证完成。

- ⏳ 页面显示“Loader”加载提示
- 🛡️ 系统正在验证当前请求
- ⌛ 用户需等待验证完成
- ℹ️ 当前暂无其他可操作内容

---

### [我的网站流量 99% 是机器人 | PatronView](https://patronview.com/news/99-percent-of-my-website-traffic-is-bots/)

**原文标题**: [99% of My Website Traffic Is Bots | PatronView](https://patronview.com/news/99-percent-of-my-website-traffic-is-bots/)

文章作者用一年时间与爬虫对抗，运营着拥有 150 万个人资料页的 PatronView 慈善捐赠者数据库；他发现网站真实请求绝大多数来自机器人，仅靠 JavaScript 访客统计会严重低估攻击流量，“99% 是机器人”甚至还是保守说法。

- 📊 一周内服务器收到 250 万次请求、返回 128 万页面，但访客统计只记录 5,977 次人类浏览，约合 214 次机器人页面加载对应 1 次人类浏览。
- 🤖 早期 SemrushBot、AhrefsBot、MJ12bot 等 SEO 爬虫反复抓取；2025 年 11 月又出现 4,000 个无来源、只抓基金页面的异常“访客”。
- 🌏 2026 年 4 月 22 日单日出现 360 万请求、36 万独立 IP，主要来自中国；作者封锁中国、越南、新加坡，并称真实搜索流量 95.9% 来自美国。
- 🧠 Claude-SearchBot 一周抓取 420,680 页，却只带来 12 个访客，比例约 35,000:1；封锁后其请求从每日约 6 万降到约 25 次。
- 📈 作者用“每带来 1 个访客被抓取多少页”衡量爬虫：Googlebot 为 46:1、Bingbot 为 406:1、Claude 为 35,000:1、Amazon 近乎无限。
- 🛒 Amazon 的 Amzn-SearchBot 每天抓取约 11.7 万页且从不带来流量，已被作者封锁。
- ☁️ 7 月出现 AWS 上的无头 Chrome 抓取浪潮，伪装访客并污染统计；作者改为挑战所有数据中心 ASN。
- ⚡ Cloudflare JavaScript Detections 让中端手机多耗 2,875ms，把 Lighthouse 分数拖到 58；关闭后一小时内升到 99，但随后 Azure 爬虫一小时抓走 2.3 万页。
- 🏠 住宅代理僵尸网络通过普通家庭宽带和大量 IP 伪装真人，浏览器版本还冻结在旧版；作者用挑战非北美大陆、数据中心 ASN、空 UA、旧浏览器和限速 30 请求/10 秒等规则应对。
- 🛡️ 48 小时内 Cloudflare 发出 106,437 次挑战，仅 252 次通过，通过率 0.24%，说明规则主要拦住机器人而非真人。
- 💸 站点月成本约 90 美元，机器人贡献 99% 账单；更麻烦的是统计被污染、真实读者不可见，以及突发缓存未命中导致真人收到 504。
- ✅ 建议包括：看服务器日志而非访客统计；按 ASN 而非 IP 封锁；可能有人类时用挑战而非直接封锁；监控挑战通过率；评估安全功能自身的性能成本。
- 🔁 结论是这场对抗像打地鼠，住宅代理难以在网络层彻底封禁；作者主张按抓取付费等经济方案，并坚持“从不带来访客的爬虫就封锁”。

---

### [诱骗 Deep](https://utkusen.substack.com/p/tricking-deepseek-into-not-hacking)

**原文标题**: [Tricking Deepseek Into Not Hacking Your Website](https://utkusen.substack.com/p/tricking-deepseek-into-not-hacking)

作者通过在被测网站中植入违禁字符串和触发词，让 Deepseek 等模型拒绝进行漏洞扫描，从而将其变成一种“提示词防火墙”。

- 🧪 作者此前用 Deepseek 配合 ARTEX、Strix 等渗透测试工具，成功发现自建漏洞应用中的安全问题。
- 💡 受“在内容中插入违禁词句可阻止 LLM 分析”的博客启发，作者想到把这些字符串放到网站上，测试 Deepseek 是否会拒绝入侵。
- 🧩 作者创建了 `html_comments.go`，并在漏洞应用的所有页面中引入，用于向 HTML 注入违禁字符串。
- 🕵️ 还在网站主 JavaScript 文件中加入无实际功能的 dummy 函数，用函数名触发 LLM 的限制机制。
- 🚫 使用 Pi 测试时，它访问网站后立即终止会话；作者也承认 Pi 并非为网站渗透测试而设计。
- ❌ 使用 ARTEX 评估时，所有代理均失败，并拒绝继续处理该应用。
- 🛡️ 结论是：在网站中加入这些字符串，可能作为一种“防火墙”，让 LLM 拒绝执行漏洞测试。

---

### [我的“人类”访客中有 90% 是机器人 | Luna Park](https://luna-park.app/blog/my-human-visitors-were-bots)

**原文标题**: [90% of my "human" visitors were bots | Luna Park](https://luna-park.app/blog/my-human-visitors-were-bots)

作者原本看到 Luna Park 仪表盘显示每周约 2.5k“人类访客”，深入排查后发现大量流量来自爬虫、无头浏览器和云服务器；通过加载 CSS/JS 校验、排除云服务 IP、与 Turnstile 对照等手段，将真实周访客修正到约 230，并强调真实数据对判断营销效果的重要性。

- 🤖 原统计只按 User-Agent 过滤明显机器人，剩余自称 Chrome、Firefox 或 Safari 的请求都被误算为人类。
- 📈 异常峰值来自同一 IP 的约 200 次请求，只抓取 sitemap 和页面，不加载脚本、样式或图片，疑似 Go 爬虫伪装 Chrome。
- 🧠 新增规则：同一 IP 当天还加载过 `.js` 或 `.css` 才计为页面浏览；缓存回访会少量漏计，约 2%。
- ☁️ 进一步排除腾讯云及其他云/托管网络 IP 段后，周“人类”从 380 降到 290，再降到 230，页面浏览从约 1.3k 降到约 400。
- ✅ 与站内 Turnstile 约 220/周 的计数对照，230 比较可信；但住宅代理上的无头浏览器等仍可能漏过。
- 🕵️ 90 天日志还发现 AI 密钥扫描、法国国家图书馆归档机器人、真实用户活动峰值，以及常见的 `.env`、WordPress 扫描。
- 🛡️ 对明显扫描使用 fail2ban：访问敏感路径或 URL 含 SQL 注入即封 2 小时，一天三次封一周。
- ⚡ 为提升仪表盘速度，夜间任务预存每日 Top 500 页面、来源、UA 和 IP，减少 InfluxDB 单核压力。
- 🔭 后续计划用每日 ASN 查询、浏览器请求头（如 `Sec-Fetch-*`）、TLS/JA4 指纹更准确识别机器人，而不引入 Cloudflare 等第三方。
- 🎯 真实约 230 访客虽不亮眼，但能区分营销效果与爬虫噪声；核心经验是：不加载 CSS 或来自数据中心的 IP，大概率不是人类。

---

