### [前端聚焦 第 706 期：2025 年 8 月 27 日](https://frontendfoc.us/issues/706)

**原文标题**: [Frontend Focus Issue 706: August 27, 2025](https://frontendfoc.us/issues/706)

本期简报介绍了前端开发领域的最新动态，包括 CSS 新特性、工具更新和技术文章。重点涵盖 CSS random() 函数、自定义高亮 API、浏览器功能更新以及性能优化等内容。

- 🎲 CSS random() 函数即将推出，可在 Safari Technology Preview 测试，无需 JavaScript 即可实现随机动画延迟和布局
- 🔦 CSS 自定义高亮 API 现已获得所有主流浏览器支持，可用于页面内搜索和语法高亮
- ⚡️ 浏览器更新：Firefox 142 发布、实验性 PWA 支持，Chrome DevTools 正在测试 AI 辅助面板
- 📚 技术文章涵盖字体加载优化、径向渐变技巧、CSS 长度单位和 OKLCH 色彩模型等主题
- 🧰 新工具包括基于黄金比例的 UI 框架 LiftKit、JavaScript 文件上传器 Uppy 5.0 和 JSON 编辑器
- 🤔 最后提供了 CSS 知识测试 quiz，包含 20-60 道选择题

---

### [CSS random() 的随机探索 | WebKit](https://webkit.org/blog/17285/rolling-the-dice-with-css-random/)

**原文标题**: [  Rolling the Dice with CSS random() | WebKit](https://webkit.org/blog/17285/rolling-the-dice-with-css-random/)

CSS 的 random() 函数即将推出，它允许开发者在无需 JavaScript 的情况下生成随机值，用于动画延迟、布局定位、颜色生成等多种场景。该函数支持定义数值范围与步长，并可通过命名标识或 element-shared 实现随机值的共享或独立生成。文章通过星空背景、网格矩形、照片堆叠和幸运转盘等示例演示了其应用潜力，目前该功能已在 Safari Technology Preview 开放测试，并邀请开发者反馈使用体验。

- 🌌 使用 random() 创建随机分布的星空效果，包括位置、大小和发光颜色
- 🎲 函数格式为 random(min, max, step)，支持各类数值单位与步长控制
- 🔗 通过命名标识（如 --foo）实现单元素内多属性的随机值共享
- 🌐 使用 element-shared 使同一属性在所有元素间共享随机值
- 🖼️ 结合 grid 布局生成随机位置与颜色的矩形矩阵
- 📸 为照片堆叠添加随机旋转与交互式悬停位移效果
- 🎯 在动画关键帧中应用随机旋转实现幸运转盘交互
- ⚠️ 功能目前处于 Safari 技术预览阶段，欢迎开发者提交使用反馈

---

### [CSS 值与单位模块第五级](https://www.w3.org/TR/css-values-5/#randomness)

**原文标题**: [CSS Values and Units Module Level 5](https://www.w3.org/TR/css-values-5/#randomness)

该规范是 CSS 值和单位模块第 5 级的草案，扩展了 CSS 值和单位第 4 级，引入了新的数据类型、函数和语法特性以增强 CSS 的表达能力和灵活性。

- 📝 扩展了 CSS 值和单位第 4 级，定义了新的数据类型和函数语法
- 🔧 引入了逗号包装语法，使用花括号{}区分函数参数中的逗号
- 🧩 定义了<boolean-expr[]>语法，支持布尔逻辑组合条件表达式
- 📋 新增了<syntax>类型，用于指定 CSS 值的解析语法
- 🌐 为<url>类型添加了请求修饰符，如 crossorigin、integrity 等
- 📍 扩展了<position>类型，支持流相对定位和更复杂的定位语法
- 📊 引入了*-progress() 函数族，用于计算数值在起始值和结束值之间的进度
- 🔀 新增了*-mix() 函数族，用于在不同值之间进行插值计算
- ✅ 添加了 first-valid() 函数，选择第一个有效的值
- ❓ 引入了 if() 条件函数，支持基于条件的值选择
- 🔁 添加了 toggle() 函数，允许在值之间切换
- 📦 新增了 attr() 函数，用于引用 HTML 属性值
- 🎲 引入了 random() 和 random-item() 函数，用于生成随机值
- 🔢 添加了 sibling-count() 和 sibling-index() 函数，用于计算兄弟元素数量和索引
- 📏 引入了 calc-size() 函数，支持对内在尺寸进行计算
- 🔄 新增了 interpolate-size 属性，控制尺寸关键字的插值行为
- ⚠️ 包含了安全考虑，特别是 attr() 函数可能带来的安全风险

---

### [资源 - Safari - Apple Developer](https://developer.apple.com/safari/resources/)

**原文标题**: [Resources - Safari - Apple Developer](https://developer.apple.com/safari/resources/)

概述了苹果为开发者提供的 Safari 及 Web 开发相关资源，包括技术预览版、文档、视频和论坛支持，并介绍了关键网络技术如扩展功能、通用链接和推送通知等。

- 🆕 Safari 技术预览版支持 macOS Tahoe 和 Sequoia 系统，可提前体验新网络技术
- 📚 提供开发指南、示例代码及 Safari 扩展/Apple Pay/密码钥匙等完整文档
- 🎥 设有工程师教学视频和开发者论坛交流平台
- 🔌 Safari 扩展支持跨设备分发，可使用 HTML5/CSS3/JavaScript 开发
- 🔗 通用链接和智能应用横幅实现应用与网页无缝跳转
- 📹 HTTP 直播流技术支持 iOS 端媒体流传输
- 🔐 iCloud 钥匙串验证码简化多步骤登录流程
- 🔔 支持 Safari 推送通知直达 Mac 桌面
- 🧪 WebDriver 提供 Safari 自动化测试框架

---

### [CSS 中极早期使用 random() 的探索——Frontend Masters 博客](https://frontendmasters.com/blog/very-early-playing-with-random-in-css/)

**原文标题**: [Very Early Playing with random() in CSS – Frontend Masters Blog](https://frontendmasters.com/blog/very-early-playing-with-random-in-css/)

WebKit/Safari技术预览版首次推出CSS的random()函数，使开发者无需预处理即可直接在CSS中生成动态随机值，支持灵活的范围控制与跨元素随机值共享机制。

- 🌐 WebKit/Safari技术预览版首次支持CSS原生random()函数，实现真正动态随机值生成
- 🔄 相比 Sass 编译时随机值，CSS random() 支持页面刷新时实时更新随机结果
- 🎯 通过 random(--foo element-shared) 语法可实现跨元素随机值共享或独立控制
- 🎨 支持带单位数值（如 100px）和无单位数值（如 RGB 色彩参数）的随机生成
- 📐 第三参数可控制随机值增量（如 random(10px,100px,20px) 仅生成 10/30/50/70/90px）
- ⚡ 可应用于定位、尺寸、颜色、动画延迟等 CSS 属性，极大简化随机效果实现代码
- 💡 实际演示显示原本需要 200 行 Sass 代码的效果，现仅需数行原生 CSS 即可实现

---

### [使用自定义高亮 API – Frontend Masters 博客](https://frontendmasters.com/blog/using-the-custom-highlight-api/)

**原文标题**: [Using the Custom Highlight API – Frontend Masters Blog](https://frontendmasters.com/blog/using-the-custom-highlight-api/)

Custom Highlight API 允许通过 JavaScript 的 Range() 对象选择文本范围并应用 CSS 样式，无需操作 DOM 结构，适用于搜索高亮和语法高亮等场景。

- 🔍 Firefox 140 于 2025 年 6 月支持 Custom Highlight API，至此所有主流浏览器均已兼容
- 📝 通过 Range() 设置文本起始/结束位置，使用 CSS.highlights.set() 注册高亮区域，CSS 中通过 ::highlight() 选择器应用样式
- ⚡ 优势：避免大量 DOM 操作（如添加 span 标签），提升页面性能，尤其适用于高频文本处理场景
- 🔎 支持多范围高亮，可构建自定义搜索功能（如案例中通过正则匹配用户输入实现实时搜索高亮）
- 💻 可用于语法高亮（如结合 Prism.js 的 Web Component），但需注意客户端渲染可能导致的样式延迟加载问题
- ⚠️ 局限性：仅支持客户端渲染，服务端预渲染语法高亮仍更具优势

---

### [CSS 自定义高亮 API](https://developer.mozilla.org/en-US/docs/Web/API/CSS_Custom_Highlight_API)

**原文标题**: [CSS Custom Highlight API](https://developer.mozilla.org/en-US/docs/Web/API/CSS_Custom_Highlight_API)

CSS Custom Highlight API 允许通过 JavaScript 创建文本范围并用 CSS 进行样式化，无需影响 DOM 结构，适用于文本编辑器高亮等场景。

- 🛠️ 通过创建 Range 对象定义需要样式化的文本范围
- 🌈 使用 Highlight 对象管理多个文本范围，支持不同样式
- 📝 通过 HighlightRegistry 注册高亮对象并自定义标识符
- 🎨 使用 ::highlight() 伪元素为注册的高亮对象应用 CSS 样式
- 🔍 支持搜索高亮等实用功能，示例展示实时文本匹配效果
- 📱 包含 Highlight 和 HighlightRegistry 两个核心接口
- 🌐 需要检查浏览器兼容性，目前属于 CSS Custom Highlight API Module Level 1 规范

---

### [不，谷歌并未单方面决定扼杀 XSLT——埃里克的存档思考](https://meyerweb.com/eric/thoughts/2025/08/22/no-google-did-not-unilaterally-decide-to-kill-xslt/)

**原文标题**: [No, Google Did Not Unilaterally Decide to Kill XSLT  –  Eric’s Archived Thoughts](https://meyerweb.com/eric/thoughts/2025/08/22/no-google-did-not-unilaterally-decide-to-kill-xslt/)

关于谷歌提议移除浏览器中 XSLT 支持的争议并非单方面决策，而是多方浏览器厂商共同发起的标准化流程讨论，旨在评估该低使用率功能的安全性和维护成本。

- 🔥 WHATWG 论坛因 XSLT 移除提案引发激烈争论，最终因人身攻击锁定讨论
- 🌐 XSLT 是一种 XML 转换语言，常用于 RSS/Atomfeed 样式化等场景
- ⚠️ 移除动因包括代码内存安全隐患、低使用率及维护资源有限
- 🤝 提案由谷歌员工发起但获 Mozilla/WebKit 团队初步支持，非谷歌单方面决定
- 📉 浏览器仅支持 XSLT1.0（现行标准为 3.0），且采用非内存安全的 C++ 实现
- 🔬 移除评估采用渐进式流程：通过灰度发布测试影响，全程可能耗时数年
- 💡 替代方案包括 WASMpolyfill、服务器端处理或浏览器扩展支持
- ⚖️ 反对意见认为移除会破坏历史网页内容，削弱 Web 平台完整性
- 📊 作者强调决策过程透明但缺乏公众可见的流程说明导致误解

---

### [基于 llms.txt 的 HTML 内联 LLM 指令提案 - Vercel](https://vercel.com/blog/a-proposal-for-inline-llm-instructions-in-html)

**原文标题**: [A proposal for inline LLM instructions in HTML based on llms.txt - Vercel](https://vercel.com/blog/a-proposal-for-inline-llm-instructions-in-html)

本文提出在 HTML 中嵌入<script type="text/llms.txt">标签的方案，为 AI 代理提供即时操作指引，特别针对需要身份验证的受保护页面访问场景。

- 🚀 通过 HTML 内嵌指令解决 AI 代理访问受限页面的引导问题，无需依赖外部文档
- 🔧 采用<script type="text/llms.txt">格式，浏览器会忽略但 LLM 能识别其中的指令内容
- 🛡️ Vercel 已在 401 错误页面实际应用，指导代理使用认证绕过令牌或 MCP 服务器功能
- 🌐 基于 llms.txt 标准，与现有网络发布规范保持兼容
- ⚡ 无需 LLM 提供商特别支持，即插即用，具有即时发现特性
- 📋 指令包含具体操作步骤、MCP 服务器调用方法和相关文档链接
- 🔍 适用于多种场景：页面访问权限获取、错误调查指引、MCP 服务发现等

---

### [获取失败](https://frontendfoc.us/link/173421/web)

**原文标题**: [Failed to retrieve](https://frontendfoc.us/link/173421/web)

无法总结：获取内容失败，状态码 403。

---

### [Firefox 142 开发者版本](https://developer.mozilla.org/en-US/docs/Mozilla/Firefox/Releases/142)

**原文标题**: [Firefox 142 for developers](https://developer.mozilla.org/en-US/docs/Mozilla/Firefox/Releases/142)

Firefox 142 版本于 2025 年 8 月 19 日发布，主要针对开发者进行了多项功能更新、API 支持改进和实验性特性引入，涵盖 Web 开发、扩展开发和 WebDriver 兼容性等方面。

- 🌐 HTML 移除了`<object>`元素的废弃`codebase`属性，需改用`data`属性
- 🎨 CSS 调整`@scope`内`&`选择器的特异性规则，使其与 CSS 嵌套保持一致
- 🔗 全面支持 URL Pattern API，提供标准化 URL 匹配和解析功能
- 📁 文件与目录条目 API 现支持`webkitdirectory`属性和`File.webkitRelativePath`，允许处理目录上传
- 👆 DOM 新增`Selection.getComposedRanges()`方法，支持跨影子 DOM 获取文本选择范围
- ⏯️ 新增`Animation.overallProgress`属性，用于追踪动画进度
- 🚀 支持优先级任务调度 API（Scheduler 等接口），提供标准化任务优先级管理
- 📊 WebRTC 新增多项 RTC 统计属性，如往返时间测量和流状态指标
- 🤖 WebDriver 移除 FTP 代理支持，并更新 Cookie 过期时间限制为 400 天
- 🛠️ 扩展开发中加强 Cookie 验证，并新增用户设置变更监听事件
- 🧪 实验性功能包括 CSS 锚点尺寸定位、标题伪类选择器、视图过渡命名自动匹配等
- 🔒 新增完整性策略 HTTP 头支持，用于脚本和样式表的资源完整性验证

---

### [AI 辅助网络功能 | Chrome DevTools | Chrome 开发者指南](https://developer.chrome.com/docs/devtools/ai-assistance/network)

**原文标题**: [AI assistance for network  |  Chrome DevTools  |  Chrome for Developers](https://developer.chrome.com/docs/devtools/ai-assistance/network)

Chrome DevTools 中的 AI 辅助功能（网络面板）是一项实验性功能，通过分析网络请求数据（URL、头部、时间轴等）帮助开发者理解网站请求行为，支持会话历史保存与多入口调用。

- 🚀 需在 Chrome Canary 132+ 版本使用，开启前请查阅已知问题与数据使用政策
- 🖱️ 可通过右键网络请求选择"Ask AI"、命令菜单输入"AI"或更多工具菜单开启面板
- 🔍 自动关联当前选中的网络请求上下文，点击其他请求可切换分析对象
- 📝 提供示例提示词快捷输入，支持自定义提问并保留完整会话历史记录
- ⚠️ 敏感头部信息会自动脱敏，可通过展开按钮查看 AI 使用的原始数据
- 💬 支持对答案进行点赞/踩反馈，可举报不当内容以帮助改进实验功能
- 💾 会话历史跨页面重载保留，可通过顶部控件新建/续聊/删除对话记录

---

### [你加载字体的方式错了（而且正在拖垮你的性能）- 乔诺·奥尔德森](https://www.jonoalderson.com/conjecture/youre-loading-fonts-wrong/)

**原文标题**: [You’re loading fonts wrong (and it’s crippling your performance) - Jono Alderson](https://www.jonoalderson.com/conjecture/youre-loading-fonts-wrong/)

网页字体加载普遍存在性能问题，需从历史、技术、策略多维度优化。字体应视为核心基础设施而非装饰，直接影响渲染性能、布局稳定性和用户体验。

- 📜 历史遗留问题：从早期「网络安全字体」到@font-face 兼容性混乱，再到 Google Fonts 的滥用，形成「字体即装饰」的错误认知
- ⚙️ 技术基础认知：WOFF2 为现代标准格式，字体加载涉及注册、匹配、字形覆盖等多阶段渲染管线，默认合成样式会破坏设计一致性
- 📉 性能核心影响：字体文件体积过大（单样式可达 800KB）和布局偏移（CLS）是主要性能杀手，尤其 fallback 字体度量值不匹配时
- 🎛️ 现代 CSS 解决方案：font-display 控制加载行为，size-adjust/ascent-override 等度量覆盖描述符消除布局偏移，unicode-range 实现按需加载
- 🌐 全球化考量：非拉丁文字（阿拉伯文/中文等）需要保留完整字形表，RTL 语言需要特殊处理，emoji 应使用系统原生字体
- ⚡ 加载策略优化：自托管 WOFF2 格式，关键字体预加载，非关键字体延迟加载，避免@import 和第三方 CDN（隐私和性能问题）
- 🔧 工具化实践：使用 Glyphhanger 等工具分析实际用到的字形，用 pyftsubset 生成子集，用 Font Style Matcher 调整 fallback 匹配
- 🚫 摒弃过时方案：停止使用图标字体（改用 SVG），避免多格式冗余（仅需 WOFF2），不再依赖 Google Fonts 等第三方 CDN
- 📱 响应式设计：可变字体可提供更精细的控制，但需评估文件体积权衡，非必需时多个静态字体可能更高效
- 🔍 测试与监控：必须在慢速网络和冷缓存环境下测试字体加载行为，监控 CLS 等核心 Web 指标

---

### [痴迷于平滑径向渐变圆盘边缘——前端大师博客](https://frontendmasters.com/blog/obsessing-over-smooth-radial-gradient-disc-edges/)

**原文标题**: [Obsessing Over Smooth radial-gradient() Disc Edges – Frontend Masters Blog](https://frontendmasters.com/blog/obsessing-over-smooth-radial-gradient-disc-edges/)

本文探讨了使用 CSS radial-gradient() 创建平滑边缘圆形时遇到的锯齿问题，并提出了基于分辨率媒体查询和 JavaScript 的动态解决方案。

- 🎯 使用 radial-gradient() 创建圆形时边缘会出现锯齿问题，而伪元素方法则能保持平滑
- 🔍 常见的 1% 色标距离解决方案在大圆中会产生模糊边缘，小圆中仍存在锯齿
- 📏 作者原本采用 1px 距离的"防弹"方案，但在高 DPI 显示或缩放时仍会失效
- 📱 发现 CSS 分辨率媒体查询功能，可根据设备像素密度或缩放级别调整样式
- 🔧 使用 Sass 循环为不同缩放级别生成媒体查询，确保在各种情况下边缘平滑
- 🌐 针对不同浏览器（Chromium 和 Firefox）的缩放级别差异，优化了媒体查询策略
- ⚡ 提供了更灵活的 JavaScript 解决方案，通过 devicePixelRatio 动态调整参数
- 💡 指出在某些情况下（如形状遮罩回退）平滑边缘至关重要，而在其他场景（如渐变背景）可接受模糊效果

---

### [设计内置 AI Web API | 多梅尼克·德尼科拉](https://domenic.me/builtin-ai-api-design/)

**原文标题**: [Designing the Built-in AI Web APIs | Domenic Denicola](https://domenic.me/builtin-ai-api-design/)

概述了 Chrome 内置 AI 团队设计 Web API 的过程，重点探讨了提示 API 的设计挑战、客户端与服务器 API 的差异，以及互操作性和未来兼容性的考量。

- 🤖 设计目标是将 AI 模型引入浏览器，并推动成为 Web 标准库的一部分
- ⚡ 面临快速发展的 AI 领域与传统 Web API 设计流程的冲突
- 📝 提示 API 采用消息数组格式（系统/用户/助理角色），支持多模态输入输出
- 🎯 客户端 API 直接使用 JavaScript 类型，支持异步工具函数调用
- 💾 采用有状态的 LanguageModelSession 设计，优化资源管理和上下文窗口
- 🌐 强调跨浏览器和跨模型实现的互操作性要求
- 🔮 通过预配置选项和可用性检查机制实现未来兼容性
- ⚙️ 正在讨论超参数定制、设备约束和提示注入防护等开放问题
- ⏱️ 面临 Web 标准发展速度与 AI 技术快速演进之间的时间差挑战

---

### [内置 AI API | Chrome AI 功能 | Chrome 开发者](https://developer.chrome.com/docs/ai/built-in-apis)

**原文标题**: [Built-in AI APIs  |  AI on Chrome  |  Chrome for Developers](https://developer.chrome.com/docs/ai/built-in-apis)

Chrome 浏览器内置了多种 AI API，涵盖翻译、语言检测、摘要生成、写作辅助等功能，部分 API 已稳定可用，其他处于实验或预览阶段，开发者可通过不同渠道参与测试和使用。

- 🌐 翻译 API（Chrome 138 稳定版）：支持动态内容实时翻译，适用于多语言社交网络或客服场景
- 🔤 语言检测 API（Chrome 138 稳定版）：自动识别文本语言，为翻译流程提供前置支持
- 📝 摘要 API（Chrome 138 稳定版）：可生成会议记录、产品评论、长篇文章的浓缩内容
- ✍️ 写作/重写 API（Origin Trial 阶段）：帮助创建符合特定风格的新内容或修改现有文本
- 💬 提示 API（扩展程序专用）：允许通过自然语言与 Gemini Nano 模型交互
- ✅ 校对 API（早期预览阶段）：为浏览器内编辑的文档提供实时语法检查功能
- 🧪 多阶段开发模式：提供稳定版、Origin Trial 和早期预览计划三种参与方式，开发者可按需选择

---

### [理解 CSS 长度单位](https://blog.scottlogic.com/2025/08/22/css-length-units.html)

**原文标题**: [Making Sense of CSS Length Units](https://blog.scottlogic.com/2025/08/22/css-length-units.html)

CSS 长度单位是网页设计中控制元素尺寸的关键工具，分为绝对单位（如 px）和相对单位（如 em、rem、vw 等）。合理选择单位能提升布局的灵活性与响应式效果。

- 📏 绝对单位（如 px）固定不变，适合精确控制元素尺寸
- 🔗 相对单位（如 em、rem）基于父元素或根元素字体大小，增强可伸缩性
- 🌐 视口单位（vw/vh）依据屏幕尺寸自适应，优化响应式设计
- ⚖️ 单位组合使用可实现更精细的布局控制
- 🎯 推荐优先使用 rem 和 vw 单位兼顾可访问性与跨设备兼容性

---

### [优化 PWA 以适应不同显示模式——Smashing Magazine](https://www.smashingmagazine.com/2025/08/optimizing-pwas-different-display-modes/)

**原文标题**: [Optimizing PWAs For Different Display Modes — Smashing Magazine](https://www.smashingmagazine.com/2025/08/optimizing-pwas-different-display-modes/)

渐进式 Web 应用（PWA）通过不同显示模式优化用户体验，需针对独立应用环境调整设计功能和内容交互方式。

- 📱 PWA 显示模式包括全屏、独立应用、最小化 UI 和浏览器模式，影响浏览器控件的可见性
- 🎨 使用 display-mode 媒体查询和 JavaScript 检测当前模式，针对性调整 CSS 样式和功能逻辑
- 🚫 应隐藏已安装 PWA 用户不需要的安装提示和营销内容，提供应用内替代功能
- 🔧 通过 manifest 文件的 scope 和 start_url 属性控制 PWA 作用范围和启动页面
- 🌐 不同浏览器对 PWA 支持程度不同，需进行多平台测试确保兼容性

---

### [什么是 OKLCH 颜色？](https://jakub.kr/components/oklch-colors)

**原文标题**: [What are OKLCH colors?](https://jakub.kr/components/oklch-colors)

OKLCH 是一种新型色彩模型，专为感知均匀性设计，能更准确地反映人类视觉感知，简化色彩处理流程。

- 🎨 OKLCH 基于 OKLab 色彩空间，采用亮度、色度和色调三值结构，确保色彩变化符合视觉一致性
- 🔄 相比 HSL 等传统模型，OKLCH 能创建感知统一的调色板，仅调整色调即可保持色彩亮度和饱和度一致
- 🌈 在渐变处理中，OKLCH 通过亮度/色度/色调插值避免 sRGB 渐变常见的灰暗过渡和不均匀问题
- 📱 支持 Display-P3 广色域，可呈现 sRGB 无法覆盖的鲜艳色彩，浏览器会自动处理色域映射
- ⚠️ 需要注意超高色度值可能超出物理设备显示范围，实际使用时需计算各色调的最大有效色度值
- 🌐 所有现代浏览器均支持 OKLCH 语法，可通过@supports 实现向后兼容的降级方案
- 🛠️ 开发者可使用 oklch.fyi 工具快速生成 OKLCH 调色板并进行色彩转换

---

### [渐变风格的诞生 · 2025 年 8 月 27 日](https://nerdy.dev/the-making-of-gradient.style)

**原文标题**: [The Making of gradient.style · August 27, 2025](https://nerdy.dev/the-making-of-gradient.style)

本文概述了 2023 年开发符合 CSS 规范的渐变生成器 gradient.style 的设计过程与核心功能。  
- 🎨 支持 CSS5 HDR 色彩空间的渐变工具，可可视化简写语法效果  
- 📐 创新采用双位置语法控制色标分布，支持过渡提示参数调节  
- 🖌️ 包含线性/径向/锥形渐变线条的交互式设计草图与实现测试  
- 🎛️ 界面包含图层列表、渐变画布预览、色标控制面板及 CSS 代码输出  
- 🔮 未来计划增加多层渐变和背景图像尺寸调整功能  
- 💬 社区讨论涉及色彩空间分级（sRGB/P3/HDR）的技术定义辨析

---

### [CSS 高清渐变](https://gradient.style)

**原文标题**: [CSS HD Gradients](https://gradient.style)

本文介绍了 CSS 渐变工具的功能和选项，重点支持多种色彩空间和渐变类型。

- 🎨 支持多种色彩空间：包括 oklab、lch、oklch、hsl、hwb、lab 等现代色彩格式
- 🌈 提供三种渐变类型：线性渐变 (linear)、径向渐变 (radial) 和锥形渐变 (conic)
- 📋 包含实用功能：CSS 代码生成、复制、导入导出渐变、明暗模式切换
- 🎯 支持方向控制：八个基本方向 (to right/to left 等) 和角度精确控制 (°)
- 💡 示例代码展示：使用 oklab 色彩空间创建 HDR 渐变效果
- 🔧 辅助工具：随机颜色生成、重置、帮助反馈和学习资源

---

### [interpolate-size 属性是渐进增强的一个绝佳范例——Piccalilli](https://piccalil.li/blog/the-interpolate-size-property-is-a-great-example-of-progressive-enhancement/)

**原文标题**: [
  The interpolate-size property is a great example of progressive enhancement - Piccalilli
](https://piccalil.li/blog/the-interpolate-size-property-is-a-great-example-of-progressive-enhancement/)

interpolate-size 属性作为渐进增强的示例，展示了如何优雅处理 CSS 动画到 auto 高度的过渡效果，目前仅 Chromium 浏览器支持，但通过合理设计可确保所有浏览器获得可用的基础体验。

- 🌐 interpolate-size 属性允许 CSS 动画过渡到 auto 高度或宽度等内在尺寸关键词
- ⏳ 该特性已需求近 18 年，但目前仍仅 Chromium 浏览器支持
- 🛡️ 通过@supports 规则可实现渐进增强，不支持此特性的浏览器会自动忽略相关代码
- 📐 使用 lh 单位和自定义属性计算高度，结合 padding 实现平滑过渡效果
- 🔧 代码设计考虑了多 details 元素的折叠面板场景，支持分组行为
- 🎯 老版本浏览器虽无动画效果，但仍能获得基本可用的体验且不会破坏布局
- 💡 体现了 CSS 渐进增强的强大能力，无需额外加载 polyfill 资源

---

### [停止使用 CSS 预处理器的 4 个理由 — 安瑟姆·汉尼曼](https://helloanselm.com/writings/4-reasons-to-stop-using-css-preprocessors)

**原文标题**: [4 Reasons to stop using CSS Preprocessors — Anselm Hannemann](https://helloanselm.com/writings/4-reasons-to-stop-using-css-preprocessors)

现在可以停止使用 CSS 预处理器，因为原生 CSS 已具备许多过去需依赖预处理器的功能。
- 🚀 许多开发者已转向 CSS-in-JavaScript 方案，实际编写的不再是传统 CSS
- ✅ CSS 原生支持嵌套语法，无需预处理器实现
- 🎯 随着 CSS 层叠层和原生嵌套等新特性出现，BEM 等命名规范逐渐过时
- 🌐 现代浏览器兼容性大幅提升，可直接使用 CSS 特性并优雅降级
- 🔧 作者建议仅保留 PostCSS 进行文件优化和兼容性处理
- 📦 使用 Tailwind 等框架但缺乏 CSS 基础知识的开发者面临使用困境
- 😲 部分 MUI 框架使用者甚至不了解 CSS 基础特性

---

### [GitHub - Chainlift/liftkit: 从设计到生产的组件库](https://github.com/Chainlift/liftkit)

**原文标题**: [GitHub - Chainlift/liftkit: Components from design to production](https://github.com/Chainlift/liftkit)

LiftKit 是一个基于黄金比例的 UI 框架，提供光学间距校正和动态色彩等高级设计功能，由 Material 3 驱动。

- 🎢 核心框架：基于黄金比例公式和变量，支持高级视觉设计功能
- 📦 组件生态：包含实际 UI 组件（需单独安装），构建时自动移除未使用的 CSS
- ⚡ 快速开始：支持通过模板克隆或现有 Next.js 项目集成（需 Node.js/npm 环境）
- 🎨 设计资源：提供 Figma 模板（当前存在按钮变体控制问题）和 Webflow 模板
- 📜 开源协议：采用 Apache-2.0 许可证，GitHub 获 1.7k 星标
- 🌐 技术栈：主要使用 CSS(50.4%) 和 TypeScript(46.4%) 开发
- ⚠️ 已知问题：按钮变体控制不足，Figma 模板需完善（欢迎贡献者参与改进）

---

### [LiftKit：Chainlift.io 为完美主义者打造的 UI 框架](https://www.chainlift.io/liftkit)

**原文标题**: [LiftKit: The UI Framework for Perfectionists by Chainlift.io](https://www.chainlift.io/liftkit)

LiftKit 是一个开源的 UI 框架，专注于通过黄金比例和光学校正技术解决界面设计中的对称性问题，提供高度可定制的组件和实用工具类，帮助开发者快速构建视觉精致的应用程序。

- 🎨 采用黄金比例和亚像素精度技术，确保所有元素呈现完美比例
- ⚙️ 提供模块化控制面板，支持实时预览颜色、排版和材质等全局样式调整
- 🧩 包含光学校正属性（如 opticalCorrection），智能调整组件内边距和留白
- 📚 提供详细文档、视频教程和实用工具类快速参考
- 🌈 支持动态色彩系统和组件级独立配置，满足深度定制需求
- 🚀 支持多种集成方式（新建项目/现有项目），特别优化 Next.js 框架
- 💡 通过专业设计细节提升产品视觉质感，使 MVP 版本呈现完整产品级效果

---

### [M2M 代币公测版](https://clerk.com/changelog/2025-08-15-m2m-beta?utm_source=cooper-press&utm_medium=newsletter&utm_campaign=m2m-tokens&utm_content=08-27-25&dub_id=HrknuDZPIZxBqhTY)

**原文标题**: [M2M Tokens Public Beta](https://clerk.com/changelog/2025-08-15-m2m-beta?utm_source=cooper-press&utm_medium=newsletter&utm_campaign=m2m-tokens&utm_content=08-27-25&dub_id=HrknuDZPIZxBqhTY)

M2M 令牌现已进入公开测试阶段，专为后端服务间安全通信设计，支持自定义声明与即时撤销功能，测试期间可免费使用。

- 🔐 专为后端基础设施中机器间请求认证设计，适用于微服务/分布式系统
- ⚙️ 支持通过仪表板/API/SDK 创建机器并配置通信权限
- 🎨 可定制声明内容、过期时间并支持即时令牌撤销
- 💻 提供简洁 SDK 实现令牌创建（$0.001/次）与验证（$0.0001/次）
- 🆓 测试期间完全免费，正式版将采用按量计费模式
- 📊 即将在仪表板提供使用统计、监控和速率限制功能
- 🔮 测试结束前将新增 JWT 令牌支持（仅收取创建费用）
- 📚 提供详细指南、示例代码库和仪表板帮助快速入门

---

### [Uppy](https://uppy.io/)

**原文标题**: [Uppy](https://uppy.io/)

Uppy 是一个功能强大、响应式且可扩展的文件上传仪表板，支持从远程源添加文件、编辑图像、生成缩略图等多种操作。

- 🌐 支持从 Google Drive 等远程源获取文件，通过 Companion 服务器处理认证和下载
- 🖼️ 内置图像编辑器和摄像头拍摄功能，可直接在仪表板中处理媒体文件
- ⚡ 采用 Tus 协议实现可恢复的大文件上传，避免网络中断导致上传失败
- 🔌 提供 React、Vue、Svelte 和 Angular 等主流框架的集成支持
- 🌍 具备多语言支持和无障碍访问设计，注重国际化体验
- 🛡️ 通过 Golden Retriever 插件实现浏览器崩溃后的文件恢复功能
- 🐙 开源项目，积极采纳社区反馈并持续改进
- 🔄 可与 Transloadit 文件编码处理后端完美配合工作

---

### [GitHub - transloadit/uppy: 下一代开源网页浏览器文件上传工具](https://github.com/transloadit/uppy)

**原文标题**: [GitHub - transloadit/uppy: The next open source file uploader for web browsers](https://github.com/transloadit/uppy)

Uppy 是一款开源、模块化的网页浏览器文件上传工具，支持多来源文件获取、可恢复上传及丰富的自定义选项。

- 🐶 专为网页浏览器设计的开源文件上传工具，支持拖放、远程 URL 及云服务（如 Google Drive、Dropbox）获取文件
- ⚡ 采用轻量级模块化架构，支持通过 Tus 协议实现可恢复上传，避免网络中断导致上传失败
- 🛠️ 提供丰富的插件生态，包括图像编辑、元数据预览、摄像头拍摄及多语言支持
- 📦 可无缝集成 React、Vue、Svelte 等前端框架，支持无头组件和高度自定义 UI
- 🌍 完全免费（MIT 许可证），由 Transloadit 团队维护，注重可访问性和用户体验

---

### [GitHub - json-editor/json-editor: 基于 JSON 模式的编辑器](https://github.com/json-editor/json-editor)

**原文标题**: [GitHub - json-editor/json-editor: JSON Schema Based Editor](https://github.com/json-editor/json-editor)

这是一个基于 JSON Schema 的开源编辑器项目，能够根据 JSON Schema 动态生成 HTML 表单，支持多种 CSS 框架和扩展功能。

- 🚀 项目拥有 4.8k 星标和 699 个分支，采用 MIT 开源协议
- 🎯 完全支持 JSON Schema 3 和 4 版本，可集成 Bootstrap、Tailwind 等 CSS 框架
- 🌐 提供在线演示和交互式游乐场，支持通过 CDN 或 npm 安装
- 🛠️ 支持多种第三方编辑器扩展（如 Ace 编辑器、Markdown 编辑器等）
- 📋 提供丰富的配置选项，包括主题设置、图标库、验证规则等
- 🔧 支持动态依赖、条件渲染、自定义模板和国际化功能
- 📦 包含数组表格显示、对象网格布局、分类标签等高级功能
- 🌍 支持多语言定制，开发者可以创建自定义编辑器和验证规则

---

### [JSON 编辑器交互式示例](https://json-editor.github.io/json-editor/)

**原文标题**: [JSON Editor Interactive Example](https://json-editor.github.io/json-editor/)

这是一个 JSON Schema 编辑器功能说明文档的概述总结

- 🎛️ 提供 JSON Schema 编辑器生成和配置功能
- 🔗 支持直接链接访问和 GitHub 集成
- 📝 可实时编辑 JSON 数据并更新表单
- ✅ 包含表单验证功能，实时显示错误信息
- ⚙️ 提供丰富的配置选项和主题样式选择
- 🎨 支持多种图标库和布局方式
- 📋 集成多种外部编辑器库和工具
- 🔄 可动态更新 Schema 配置并查看效果

---

### [GitHub - subframe7536/maple-font: Maple Mono：开源圆角等宽字体，带连字和 Nerd-Font 图标，适用于 IDE 和终端，提供细粒度自定义选项。中英文宽度完美 2:1。](https://github.com/subframe7536/maple-font)

**原文标题**: [GitHub - subframe7536/maple-font: Maple Mono: Open source monospace font with round corner, ligatures and Nerd-Font icons for IDE and terminal, fine-grained customization options. 带连字和控制台图标的圆角等宽字体，中英文宽度完美 2:1，细粒度的自定义选项](https://github.com/subframe7536/maple-font)

Maple Mono 是一款开源的圆角等宽字体，专为编程和终端设计，支持连字、Nerd-Font 图标及细粒度自定义选项，提供多语言版本和多种格式下载。

- 🌐 开源圆角等宽字体，支持连字和终端图标，中英文宽度完美 2:1 对齐
- 🎛️ 提供可变字重、斜体智能连字和自定义功能选项，可禁用或启用特定特性
- 🖥️ 支持简体中文、繁体中文和日文字符集，基于 Resource Han Rounded 优化显示
- 📦 支持多种包管理器安装（Scoop、Homebrew、Arch Linux、Nixpkgs）及 CDN 分发
- 🔧 支持本地和在线自定义构建，可通过配置文件或命令行调整字体特性和格式
- 🌍 提供在线预览和 Playground 实时调试，支持 GitHub Actions 和 Docker 构建
- 📜 采用 SIL Open Font License 1.1 许可证，完全免费开源

---

### [Maple Mono：开源等宽字体](https://font.subf.dev/en/)

**原文标题**: [Maple Mono: Open source monospace font](https://font.subf.dev/en/)

Maple Mono 是一款专为程序员设计的开源等宽字体，融合优雅设计与实用功能，旨在提升编码体验与生产力。

- 🎨 圆角字形与流畅设计，提供全新字形和斜体连笔风格
- ⚙️ 支持精细配置，可自定义或冻结 OpenType 功能
- 🌐 内置 Nerd-Font 图标并完整支持中文字符（2:1 等宽比例）
- 🔤 提供可变字重支持，满足不同粗细需求
- ✨ 智能连字功能，支持标签美化与特殊符号连接
- 🔄 提供 Maple Mono Normal 预设版本，兼容 JetBrains Mono 风格
- 📱 适用于多种编程语言和现代终端环境
- 💬 获得开发者社区积极反馈，特别好评斜体设计与图标支持

---

### [CSS-问题](https://css-questions.com/)

**原文标题**: [CSS-Questions](https://css-questions.com/)

文章概述了人工智能在医疗领域的应用现状与未来潜力，重点分析了其对诊断效率、个性化治疗及医疗资源分配的变革性影响。

- 🤖 人工智能通过深度学习提升医学影像诊断准确率，如 CT 扫描和 MRI 分析
- ⚕️ 基于患者数据的个性化治疗方案开发，显著提高慢性病管理效果
- 🌐 远程医疗与 AI 结合，缓解偏远地区医疗资源不均问题
- 🔬 药物研发周期缩短，AI 算法加速新药靶点发现与临床试验设计
- 📊 医疗大数据分析助力流行病预测和公共卫生决策优化
- ⚠️ 面临数据隐私、算法透明度和监管框架等伦理挑战

---

### [非 HTML 内容](https://frontendfoc.us/open/706/*%7CUID%7C*?ipx=t)

**原文标题**: [Non-HTML content](https://frontendfoc.us/open/706/*%7CUID%7C*?ipx=t)

无法总结：非 HTML 内容。

---

