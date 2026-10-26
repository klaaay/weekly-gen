### [React 文摘：电子邮件通讯](https://reactdigest.net/)

**原文标题**: [React Digest: Email Newsletter](https://reactdigest.net/)

React Digest 是一份面向 React 开发者的每周精选通讯，主打人工挑选的优质文章和简短摘要，帮助读者节省筛选内容的时间，并持续学习新知识。

- 📬 每周发送一封邮件，为 React 开发者提供精心策划的内容
- 👥 已有超过 22,109 名前端软件工程师订阅
- 📝 精选文章附带简短摘要，帮助读者快速获取有价值的信息
- ⏱️ 节省寻找优质内容的时间，让学习更高效
- 📚 每周都能学到新东西，跟上 React 生态的持续变化
- 💬 读者反馈积极，称赞文章实用且能及时更新行业信息
- 🏢 读者群体为前端工程师，通讯由 Bonobo Press 运营（© 2013-2026）

---

### [CSS 的未来 ✨ • Josh W. Comeau](https://www.joshwcomeau.com/css/interop-2027/)

**原文标题**: [The Future of CSS ✨ • Josh W. Comeau](https://www.joshwcomeau.com/css/interop-2027/)

概述：文章介绍 Interop 项目如何推动各大浏览器统一支持 Web 技术，并列出作者为 Interop 2027 投票的十大 CSS 提案。多数特性已在 Chromium 浏览器中实现，但 Firefox 和 Safari 尚未支持，因此适合作为渐进增强使用；作者也强调在 AI 时代开发者仍需掌握现代 CSS，并积极参与投票。

- 🌐 Interop 由 Google、Apple、Microsoft、Mozilla、Igalia 和 Bocoup 协作推进，焦点特性通常能在一年内接近全浏览器支持，CSS Subgrid 是成功案例。
- 🗳️ Interop 2027 正在规划中，Mozilla 提供排名系统供开发者投票，作者据此选出十大 CSS 特性并展望未来一年。
- 🧩 CSS `@function` 允许定义可复用函数并用 `result` 返回值，例如极坐标转笛卡尔坐标；Chromium 已实现，Firefox/Safari 未支持。
- 🔲 `corner-shape` 提供 `squircle`、`bevel`、`notch`、`scoop` 等角形，会真正改变 border-box，边框、轮廓和阴影可正确跟随。
- 🖋️ `border-shape` 可用直线、弧线和贝塞尔曲线自定义边框形状，并支持动画，同样会改变元素实际边框盒。
- ⚓ Anchored Container Queries 属于 Anchor Positioning Level 2，可查询定位元素是否使用回退位置，解决 tooltip 翻转后指示箭头等难题。
- ♻️ `inherit()` 提案允许在 `calc()` 中读取并修改继承值，如 `calc(inherit() - 4px)`，适合嵌套圆角等场景；目前尚未实现。
- 🎬 scroll-triggered animations 可在滚动到特定点时触发关键帧动画，区别于滚动驱动动画；目前多用 `IntersectionObserver` 实现。
- ♿ `reading-flow` 和 `reading-order` 让 Tab 顺序跟随视觉布局而非 DOM 顺序，改善响应式网格/弹性布局中的无障碍导航。
- 📏 `interpolate-size` 与 `calc-size()` 支持 `height: auto` 等关键字尺寸动画，常用于手风琴展开收起；建议用 `@supports` 渐进增强。
- 📐 gap decorations 的 `rule`、`row-rule`、`column-rule` 可直接在 Grid 间隙画线，解决空单元格没有元素可加边框的问题。
- 📌 scroll-state container queries 可查询 sticky 元素是否“粘住”，以及滚动容器是否还能向上/向下滚动，用于粘性头部样式和滚动渐变提示。
- 🚀 结论：Interop 持续成功；现代 CSS 可先作为渐进增强；LLM 训练数据偏旧，开发者更需掌握新特性并引导代理使用，同时应参与 Interop 2027 投票。

---

### [Meticulous AI——无需编写测试的自动化前端测试](https://www.meticulous.ai/?utm_source=react_digest&utm_medium=newsletter&utm_campaign=26q4&utm_term=primary+content)

**原文标题**: [Meticulous AI - Automated Frontend Testing Without Writing Tests](https://www.meticulous.ai/?utm_source=react_digest&utm_medium=newsletter&utm_campaign=26q4&utm_term=primary+content)

Meticulous 是一个面向复杂代码库的自动化端到端视觉测试平台，主打零开发者维护、穷尽覆盖与确定性执行，帮助团队以更快速度发布无回归代码。它通过记录真实用户交互，由 AI 持续生成并演化测试套件，在合并 PR 前展示变更对用户流程的影响。

- 🚀 **零维护测试**：无需编写、修复或维护测试，测试会随应用和功能变化自动新增、淘汰并保持最新。
- 🧠 **AI 持续生成测试**：监控本地、预发布和预览环境中的交互，基于代码分支覆盖生成覆盖每条代码路径、用户流程和边缘情况的视觉端到端测试。
- 🔍 **PR 前影响分析**：打开拉取请求即可看到变更对用户工作流的影响，默认通过保存并回放后端响应实现无副作用测试，减少数据变化导致的误报。
- ⚡ **极速并行执行**：测试在计算集群中高度并行化，可测试数千个页面并在 120 秒内获得结果。
- 🧱 **从底层消除不稳定测试**：基于 Chromium 层构建确定性调度引擎，号称唯一能从根源消除 flaky tests 的测试工具，并适用于复杂应用。
- 🔌 **多框架集成**：通过添加 recorder script 标签或 recorder loader 接入，支持 Next.js、React、Vue、Angular、Nuxt、SvelteKit 等。
- 🛡️ **可与现有测试共存或替代**：既能补充现有测试套件，也能完全替换现有测试。
- 🏢 **广泛采用与客户认可**：已被 100 多家组织使用，Dropbox、Notion、Engine 等团队评价其在减少合并后调试、提升开发体验和提供反馈价值方面效果显著。
- ⏱️ **快速上手**：几分钟内完成设置并生成覆盖整个应用的测试，适合希望提升发布速度与质量的工程团队。

---

### [智能体时代的纯 UI | Matt Rothenberg](https://mattrothenberg.com/notes/pure-ui-agentic-era/)

**原文标题**: [Pure UI in the Agentic Era | Matt Rothenberg](https://mattrothenberg.com/notes/pure-ui-agentic-era/)

文章讨论“Pure UI”在智能体参与前端开发时代的重要性：界面应尽量是应用状态的纯函数（ui = fn(state)），而代理和人一样，必须先看清影响显示的状态组合，才能避免只验证一个账号或一种路径就宣称完成。

- 🧠 **核心理念**：把 UI 视为某一时刻数据状态的快照，而不是零散的事件处理与 DOM 修改。
- 🧩 **状态往往分散**：角色、套餐、账单状态、功能开关等可能来自 hooks、context、布局组件和全局标志，组件本身很难完整说明屏幕可能处于哪些状态。
- 🤖 **代理容易“单状态成功”**：示例中代理给表格加了删除按钮，却只在 owner 账号下检查；viewer 角色仍能看到删除按钮，但代理仍报告完成。
- 🧪 **测试只覆盖被写下的状态**：测试有帮助，但若状态通过 hooks 隐式读取，mock 成本高，也容易漏掉未写出的组合。
- 🖼️ **显式状态更易验证**：将显示相关状态作为明确输入，可借助 Storybook 渲染状态、用 Playwright 验证真实应用中的可达性，并生成多状态视觉网格。
- 🔁 **重构方向**：把影响显示的状态提升到页面或视图边界，再作为参数传给需要演练的组件，使 API 成为“哪些输入会改变输出”的清单。
- 🔍 **合并前追问信心来源**：不要只问代理“做完了吗”，而要问它实际看到了哪些状态；一个账号只是一条路径，不是整个屏幕。
- ✅ **最终收益**：检查关键状态组合不能保证捕获所有问题，但能提高发布信心，并在客户之前发现尴尬的边缘情况。

---

### [获取失败](https://lemire.me/blog/2026/10/10/websocket-servers-in-javascript-node-js-bun-and-deno-in-2026/)

**原文标题**: [Failed to retrieve](https://lemire.me/blog/2026/10/10/websocket-servers-in-javascript-node-js-bun-and-deno-in-2026/)

无法总结：获取内容失败，状态码 520。

---

### [React Native 0.88 - 基于 Web 的事件分发、可变字体、SceneDelegate，无破坏性变更 · React Native](https://reactnative.dev/blog/2026/10/19/react-native-0.88)

**原文标题**: [React Native 0.88 - Web-Based Event Dispatching, Variable Fonts, SceneDelegate, no breaking changes · React Native](https://reactnative.dev/blog/2026/10/19/react-native-0.88)

React Native 0.88 正式发布，核心变化包括默认切换到基于 Web 的事件分发、为 Text/TextInput 引入可变字体、iOS 增加 SceneDelegate 生命周期支持，并升级 React 19.3.0 与 Metro 0.87。这是连续第三个无用户可见破坏性变更的版本，升级预期更稳定。

- 🚀 事件分发默认改用 W3C EventTarget：事件具备真实捕获与冒泡路径，支持 stopPropagation()、preventDefault()，是 0.88 最大运行时变化。
- 🧩 Canary 通道在原生 ref 上暴露 addEventListener、removeEventListener、dispatchEvent；现有事件属性名称、顺序和合成事件对象保持不变，旧插件路径暂由内部标志保留。
- 🔤 Text 和 TextInput 在 Android/iOS 均支持 fontVariationSettings，可使用 CSS 字符串或对象形式设置字体轴，如 wght、slnt。
- 📦 Java TurboModules 支持 ArrayBuffer：Codegen 映射到 com.facebook.react.bridge.ArrayBuffer，二进制数据无需再编码为字符串或数字数组；同步方法可借用 JS 内存至返回，需保留时应复制。
- 📱 iOS 支持 SceneDelegate：为 iOS 27 SDK 的 UIScene 生命周期要求做准备，同时兼容 AppDelegate；0.88 仅支持单场景，需迁移入口、转发 URL/用户活动回调到 RCTLinkingManager，并在 Info.plist 添加 UIApplicationSceneManifest。
- 🧪 Swift Package Manager 仍为实验性、可选启用；0.87 引入，0.88 加固，计划 0.89 设为默认并保留 CocoaPods 退出选项，后续再移除 CocoaPods。
- 🛠️ SwiftPM 改进包括：读取应用最低 iOS 版本、Xcode 构建更稳定、项目可移植、构建脚本使用 bash、支持 package.json 的 swiftpmConfig、从 podspec 获取名称、镜像优先下载预构建产物。
- ⚠️ 弃用项：InitializeCore 改用 react-native/setup-env；experimental_backgroundSize/Position/Repeat 改用无前缀名称；InputAccessoryView（iOS）弃用；ReactFragment.fabricEnabled 不再生效；ReactImageManager 的 String? 重载改用 Dynamic。
- 🧱 其他运行时与 Web 规范对齐：backgroundSize、backgroundPosition、backgroundRepeat 转为稳定；RuntimeScheduler、CallInvoker、FileReader、Blob、i18n 等获得修复或规范对齐。
- 🎞️ 渲染、布局与动画修复：iOS RTL 文本默认右对齐；径向渐变拒绝百分比半径；Animated addListener 恢复；ScrollView 位置、触摸和键盘行为改进；Image 的 data URI、header、百分比圆角、aria 状态等修复。
- 🧾 TypeScript/JS API：支持通过模块增强扩展生成的 props 与 style 类型；补充 requestIdleCallback、LogBox、FlatList strictMode、VirtualizedList ListItemComponent 等声明。
- 🔧 基础设施与依赖：React 19.3.0、Metro 0.87（最低 0.87.1）、Hermes 260318099.0.4；iOS 支持资源目录与 CocoaPods C++ API 依赖；Android 默认 User-Agent 包含应用名和版本；DevTools 默认支持截图，Canary 支持 WebSocket 检查。
- 🧑‍🤝‍🧑 本版本包含 568 个提交、91 位贡献者，特别感谢 SceneDelegate、C++ Stable API、SwiftPM、依赖下载、类型增强和 Metro 等贡献者。
- ⬆️ 0.88 已成为最新稳定版，0.85.x 不再受支持；建议使用 React Native Upgrade Helper 升级，新项目可用 npx @react-native-community/cli@latest init MyProject --version latest 创建，Expo 用户将通过 SDK 58 获得。

---

### [构建适用于所有人的可筛选菜单 · Base UI](https://base-ui.com/blog/building-a-filterable-menu)

**原文标题**: [Building a filterable menu that works for everyone · Base UI](https://base-ui.com/blog/building-a-filterable-menu)

本文介绍了在 Base UI 中构建可筛选菜单时，如何兼顾键盘、屏幕阅读器与子菜单交互；核心结论是：真正的难点不在过滤文本，而在于让角色语义、焦点管理、按键行为与弹出层交互保持一致，最终通过 `Menu.FilterProvider` 以可选方式为现有菜单整体启用筛选能力。

- 🔍 添加文本输入框会改变整个菜单交互：按键既要导航又要编辑文本，焦点移动可能中断输入，屏幕阅读器对弹窗的预期也会变化。
- 🧩 未采用 combobox：组合框通常用于“选择值”，而菜单项执行命令，选择“Duplicate”并不会把该词填入搜索框，违背角色承诺。
- 🚫 也未使用 `aria-autocomplete`：其语义预期会暗示补全文本或可展开的建议弹窗，但该菜单始终与输入框并列显示，Esc 等行为也不符合。
- 🪟 最终采用“对话框 + 搜索框 + 菜单”模式，并在触发器上使用 `aria-haspopup="dialog"`，提前告知用户打开的是可探索的对话框。
- ⌨️ 键盘用户可在输入框中按 `↓` 进入高亮菜单项，用方向键浏览，按 `Enter` 执行；高亮项通过 `aria-activedescendant` 标识。
- 👓 屏幕阅读器用户的虚拟光标通常先进入菜单，再通过对话框语义和“Filter actions”搜索框标签找到输入框。
- 🔁 在最后一项按 `↓` 或在第一项按 `↑` 会将高亮返回输入框；通过 `data-highlighted` 让视觉用户也看出已回到输入框。
- 🏠 `Home`/`End` 的语义依赖上下文：输入为空且菜单项高亮时跳首/末项；高亮回到输入框时移动光标；输入非空时始终移动光标。
- 📂 子菜单焦点策略：按 `→` 进入子菜单时立即聚焦其输入框；悬停仅显示子菜单，待指针进入子菜单后才聚焦，避免抢走下一次击键。
- 🚪 菜单不困住焦点，`Tab` 可离开并关闭菜单；`Menu.Clear` 不进入 Tab 顺序，避免离开菜单需要按两次 Tab。
- 🔎 使用 text input 加 `role="searchbox"`，而非 `type="search"`，以避免浏览器内置清除按钮，并让 `Menu.Clear` 成为开发者主动选择。
- 🐞 测试中还修复了普通菜单的共享问题：VoiceOver 重复播报、Shift+Tab 焦点丢失、iPhone 子菜单返回后未关闭、TalkBack 无法关闭子菜单等。
- ⚙️ 通过 `Menu.FilterProvider` 选择性启用筛选：保留现有菜单部件和样式，触发器可在输入框挂载前声明对话框，非筛选菜单不加载相关代码。

---

### [面向网页用例的 JPEG XL 与 AVIF 对比 - JakeArchibald.com](https://jakearchibald.com/2026/jpeg-xl-vs-avif/)

**原文标题**: [JPEG XL vs AVIF for web use-cases - JakeArchibald.com](https://jakearchibald.com/2026/jpeg-xl-vs-avif/)

作者在 JPEG XL 进入所有主流浏览器后，通过自建基准测试比较 AVIF 与 JPEG XL 在 Web 场景中的表现。总体来看，AVIF 在有损照片、截图、插画、透明图像以及编码/解码效率上更均衡；JPEG XL 在无损压缩、JPEG 无损转码和部分特殊图像/HDR PQ 场景中更有优势。当前建议默认使用 AVIF 4:4:4，并选择可接受的最高 effort；若 AVIF 文件异常大，再尝试 jixel 编码的 JPEG XL。

- 📉 有损照片：AVIF 通常生成更小文件；默认 effort 下最佳 JPEG XL 约大 15–25%，最大 effort 下约大 6–20%，但存在 JPEG XL 胜出的异常样本。
- 🧩 编码器差异：jixel 通常比 libjxl 更小，透明细节场景例外；但有时疑似“刷指标”，视觉质量反而更差。
- 🖼️ 截图与插画：AVIF 明显胜出；JPEG XL 默认 effort 大约 30–90%，最大 effort 大约 20–70%，有损 AVIF 已足够好。
- 🪟 透明图像：AVIF 大幅领先；libjxl 默认约大 31–44%、最大 effort 约大 61–70%；jixel 因透明通道无损编码，文件可达 AVIF 的 2–3 倍。
- ⚙️ 编码效率：综合文件大小，AVIF 编码更快、内存更少；jixel 编码快但文件偏大；AVIF 解码通常快 2–3 倍，极高质量差距缩小。
- 🎚️ effort 设置：AVIF 和 jixel 提高 effort 通常值得；libjxl 高 effort 很慢、内存高、收益小，有时文件反而更大。
- 🌈 AVIF 4:2:0：不应作为默认，通常不会显著减小文件，还限制高质量；无时间验证时建议用 4:4:4。
- ✅ 质量设置：各编码器的单一质量设置表现较一致可靠，不同图像间波动方向相似。
- 🌀 渐进渲染：JPEG XL 高 effort 渐进几乎免费，但可能让用户误以为图片已加载完且质量差；AVIF 渐进目前主要支持 Chrome，更复杂但预览可控、文件常更小、解码更快。
- 🌞 HDR：JPEG XL 格式支持增益图但浏览器不支持且编码流程混乱；AVIF 增益图可用，在极端亮度或 HDR 余量不足时体验更好。
- 🔁 JPEG 转码：JPEG XL 可无损转码现有 JPEG，文件小 9–20%，大图解码常更快，小图略慢。
- 🏆 无损压缩：JPEG XL 明显最佳；WebP 大约 9–17%，AVIF 大约 30–120%；但 Web 很少需要无损，注意 jixel 高 effort 解码慢。
- 🎞️ 动画：不建议使用动画图像格式，视频格式更适合运动内容；动画 AVIF 性能好，但 Chrome/Safari 播放实现较差。
- 🧪 方法：自建脚本测试 avifenc 1.4.2、libjxl 0.12.0、jixel 0.4.2、cwebp 1.6.0；图像宽 1598px，在 M4 Pro 上运行，并用 SSIMULACRA2/ColorVideoVDP 评估多类样本。
- 🧭 推荐：Web 默认 AVIF 4:4:4 + 可接受最高 effort；若 AVIF 文件异常大，再试 jixel JPEG XL；两种格式仍在快速改进，且围绕 JPEG XL 有大量错误信息，应用自己的图片实测。

---

### [编程文摘：电子邮件通讯](https://programmingdigest.net/?utm_source=web-archive&utm_campaign=react)

**原文标题**: [Programming Digest: Email Newsletter](https://programmingdigest.net/?utm_source=web-archive&utm_campaign=react)

Programming Digest 是一份面向软件工程师的精选周刊，主打人工筛选文章与简短摘要，帮助读者节省时间并持续学习。

- 📬 每周为软件工程师精心策划一封新闻通讯
- 👥 已有超过 20,547 名软件工程师订阅每周邮件
- 📝 提供人工精选文章，并附简短摘要
- ⏱️ 帮助读者节省寻找优质内容的时间
- 📚 让读者每周都能学到新东西
- 💬 读者反馈积极：API 设计相关内容很贴合需求，“Moving Faster”是很好的发现，每期都有收获
- 🏢 受到软件工程师群体阅读（原文未列出具体公司）
- ©️ 由 Bonobo Press 运营，版权标注为 2013-2026，页面包含新闻通讯、隐私和广告链接

---

### [科技领导力：电子邮件通讯](https://leadershipintech.com/?utm_source=web-archive&utm_campaign=react)

**原文标题**: [Leadership in Tech: Email Newsletter](https://leadershipintech.com/?utm_source=web-archive&utm_campaign=react)

这是一个面向CTO、工程经理和资深工程师的精选通讯，旨在帮助技术领导者提升领导力。它每周一和周四发送，提供带简短摘要的精选文章，帮助读者节省筛选内容的时间，并持续学习新知识。

- 📬 专为CTO、工程经理和资深工程师打造，帮助技术人提升领导力
- 🗓️ 每周一和周四发送一封邮件，订阅者超过28,575名工程领导者
- 📝 每期包含人工精选文章，并附有简短摘要，方便快速阅读
- ⏱️ 帮助读者节省寻找优质内容的时间，每周都能学到新东西
- 💬 读者评价聚焦领导力文章、架构讨论、会议与规划，以及沟通和授权能力
- 👥 内容受到技术领导者阅读，品牌信息显示为Bonobo Press，版权年份为2013-2026
- 🔗 网站包含Newsletters、Articles、Privacy、Advertise等栏目或链接

---

### [C# 文摘：电子邮件通讯](https://csharpdigest.net/?utm_source=web-archive&utm_campaign=react)

**原文标题**: [C# Digest: Email Newsletter](https://csharpdigest.net/?utm_source=web-archive&utm_campaign=react)

C# Digest 是一份面向 .NET 开发者的每周精选邮件通讯，旨在帮助读者节省筛选内容的时间，获取值得阅读的文章与摘要，并持续学习新知识；目前已有超过 22,189 名 C# 工程师订阅。

- 📰 每周为 .NET 开发者精心策划并发送精选文章，并附上简短摘要。
- ⏱️ 帮助读者节省寻找有价值内容的时间，提高信息获取效率。
- 📚 鼓励读者每周学习新知识，持续提升技术能力。
- 👥 已吸引超过 22,189 名 C# 工程师订阅。
- 💼 读者反馈称，部分内容已应用于实际工作，并希望未来在新 .NET 版本中继续使用。
- 💡 内容涉及标准功能标志、LINQ、DiagnosticListener 等主题，部分文章让读者感到意外或认为未来可能有用。
- 🧩 有读者喜欢“Operation Result Pattern”相关文章，并推荐给朋友和同事，还因此迁移了自己的 Azure Function。
- 🧑‍💻 读者群体包括 .NET 工程师；该通讯由 Bonobo Press 运营，版权年份为 2013-2026。

---

### [让开发者紧跟最新动态——Bonobo Press](https://bonobopress.com/)

**原文标题**: [Keeping developers up to date â Bonobo Press](https://bonobopress.com/)

Bonobo Press 自2013年起为软件开发者、IT专业人士和技术人员提供软件通讯，覆盖超过94,000名读者，帮助其了解最新动态。

- 📰 发布面向软件开发者、工程经理、技术负责人和CTO的精选通讯，内容简洁、省时，深受技术人士欢迎。
- 🔗 可查看各出版物并订阅。
- 🎯 广告服务可触达技术细分受众，包括活跃的软件工程师、团队负责人、工程经理、CTO和IT决策者。
- 📈 通过媒体资料包了解并开始投放广告，将产品或服务呈现给合适人群。
- ✉️ 如有问题、建议或广告合作需求，可联系获取帮助。
- ©️ 网站版权为2013-2026 Bonobo Press，并附条款。

---

### [往期通讯：第1页](https://reactdigest.net/newsletters)

**原文标题**: [Past Newsletters: Page 1](https://reactdigest.net/newsletters)

React Digest 汇总了 2026 年 6–10 月的前端与 React 生态动态，重点涵盖 CSS 与图片格式演进、React Compiler 与性能优化、AI 设计工具与设计系统、表单和状态管理、测试与排查、Next.js/React 19 新特性，以及 hydration 与渲染策略。

- 🎨 CSS 与可访问性：Interop 2027 将带来 squircles、滚动动画和新 CSS 函数，部分已在 Chrome 可用；可过滤菜单需谨慎选择 role 并管理焦点，确保键盘和读屏用户可用。
- 🖼️ 图片与设计系统：AVIF 在多数 Web 场景优于 JPEG XL，文件更小、编码更快、内存更少；React Compiler 可通过内联和更聪明的 memoization 提速；设计系统组件接受 `className` 易造成难追踪的不一致。
- ⚛️ React Compiler 与性能数据：Compiler 自动复用未变 JSX，让 Context 更便宜；Cloudflare BEACON 数据集按国家和设备映射数十亿页面加载的真实 Web 性能。
- 🤖 AI 设计工具与工程实践：AI 设计工具会编造假组件；Claude Design 的 sync 命令把真实组件编译成可用镜像；GitHub 从 CSS-in-JS 转向 CSS Modules，服务端渲染时间降低 55%。
- 💸 抽象成本与渲染性能：过度抽象使 AI agent 费用高 30%，特定任务高至 5 倍；1,175 项 React 下拉通过只渲染可见行，将 INP 从 1,256ms 降至 96ms。
- 📱 架构选择与替代方案：Shopify 放弃 React Native 转向原生 Swift/Kotlin；浏览器翻译可能分离文本节点并破坏 React；Vidact 将 React 编译为直接 DOM 操作，无需虚拟 DOM。
- ⏱️ React 19.3 与主线程：新增 ViewTransition 和 Fragment Refs；主线程每帧约 10ms 预算，批处理更新和用 Web Worker 卸载工作更重要。
- 🧠 React 原理与表单：教程拆解 fiber 树、reconciliation、hooks 和并发；TanStack Form v2 alpha 引入验证器管道和更清晰的服务端验证。
- 🧪 测试与类型安全：三项修复避免 jsdom 每次查询扫描表单标签，测试运行快 43%；TypeScript 可在编译期强制稳定 prop 引用。
- 🩺 Next.js 与排查：Next.js 15.3–16.2 存在三种内存泄漏模式，16.3 已修复；client hints 用一次 cookie 重载解决服务端时区渲染。
- 📏 现代 Web 指南与 SSR：Google modern-web-guidance 在真实 React 应用中发现暗色模式、过期验证、表单原生提交等问题，并绑定 Baseline 日期；TanStack 因依赖精简后普通 SSR 足够快而放弃 RSC。
- 📝 表单与状态管理：`useActionState` 减少样板但 pending 标志陷阱会允许重复提交；Next.js 状态可从 URL 到乐观更新统一管理；表单是复杂状态机，状态管理很大程度是缓存，CRDT 可能更优。
- 🚀 乐观 UI 与 useEffect：快速连点会让重叠请求乱序并使数据库不同步，逐项 pending 锁可修复；`useMemo` 常常无效，`useEffect` 多数 bug 源于不稳定对象引用，最好移除不必要 effect。
- 🧭 生态更新与渲染：React Compiler 在构建期消除 `useMemo`/`useCallback` 需求；React Router v8 用中间件集中鉴权、日志和重定向，要求 React 19 与 Node 22；ChatGPT 前端为标准 React SSR 流式 <100ms，hydration 不匹配会伤 LCP；React 19 移除 Test Renderer，团队用 reconciler 自建；Next.js 16.3 预览即时导航和更智能预取。
- 📦 组件通信与数据获取：邻近组件用 props，慢变值如主题用 context，高频更新用 Zustand；TanStack Query 处理竞态、缓存和后台重新获取；性能衰退是熵，需要系统化编码知识。

---

### [隐私](https://reactdigest.net/privacy)

**原文标题**: [Privacy](https://reactdigest.net/privacy)

React Digest 的隐私政策概述了其收集、使用、保留、保护和披露个人信息的规则，强调仅将信息用于明确目的，并保障用户对数据的访问、删除和退订权利。

- 📌 在收集个人信息前或收集时，明确说明收集目的。
- 🎯 个人信息仅用于实现指定目的或其他兼容目的，除非获得个人同意或法律要求。
- ⏳ 仅在实现目的所需期限内保留个人信息。
- ⚖️ 通过合法、公平的方式收集个人信息，并在适当情况下告知或征得同意。
- ✅ 个人数据应与使用目的相关，并在必要范围内保持准确、完整和最新。
- 🔐 采取合理安全措施，防止信息丢失、被盗、未经授权访问、披露、复制、使用或修改。
- 📧 仅收集电子邮箱地址，用于发送电子邮件新闻通讯。
- 🧒 不会故意收集或存储13岁以下儿童的信息；如发现相关情况可联系其处理。
- 🛡️ 根据英国《1998年数据保护法》，用户可申请获取其持有的个人信息。
- 🗑️ 用户可通过电子邮件申请删除其数据。
- 🚫 反对垃圾邮件，邮箱地址不用于其他目的，用户可随时通过邮件中的退订链接取消订阅。
- 🏢 页面版权归 Bonobo Press 所有（2013-2026），并包含新闻通讯、隐私和广告相关链接。

---

### [媒体资料包 – Bonobo Press](https://bonobopress.com/media-kit/)

**原文标题**: [Media Kit â Bonobo Press](https://bonobopress.com/media-kit/)

Bonobo Press 媒体资料包介绍其面向程序员和技术人员的新闻通讯赞助机会，覆盖软件开发者、工程经理、CTO 等受众；强调高互动、严格名单清理和精准触达，并提供广告格式、价格、投放流程及合作品牌信息。

- 📰 提供四份技术类新闻通讯：Leadership in Tech、Programming Digest、C# Digest、React Digest，面向不同技术与管理人群。
- 👥 Leadership in Tech：29,158 订阅者；打开率 51.47%；点击率 11.38%；每期 $2,570；预计点击 365–585；CPC $4.39–$7.04；次级广告位 $1,799；受众多为 CTO、工程负责人等决策者，欧洲 40%、美国 35%。
- 💻 Programming Digest：21,149 订阅者；打开率 45.57%；点击率 14.83%；每期 $1,135；预计点击 273–493；CPC $2.3–$4.16；偏后端/全栈工程师，欧洲 40%、美国 35%。
- ⚙️ C# Digest：21,077 订阅者；打开率 53.41%；点击率 21.63%；每期 $1,345；预计点击 411–631；CPC $2.13–$3.27；面向 Windows/.NET 开发者，欧洲 48%、美国 32%，企业级受众较多。
- ⚛️ React Digest：22,463 订阅者；打开率 49.86%；点击率 12.17%；每期 $1,375；预计点击 180–400；CPC $3.44–$7.64；面向 React/前端开发者，欧洲 35%、美国 30%；次级广告位 $962。
- 📈 新闻通讯互动率超过行业基准两倍以上，采用严格名单清理策略，更重视活跃读者而非单纯订阅量。
- 📝 广告为纯文本格式，嵌入新闻通讯正文；文案需提供 URL、标题（建议少于 100 字符）、描述（建议少于 400 字符、单段），截止时间为发布前 4 天。
- 🗓️ 多数广告位需提前 1–2 个月预订；时间敏感活动建议至少提前 6–8 周联系；流程包括需求沟通、排期与发票、付款锁定档期、素材交付、上线和效果报告。
- 🤝 近期合作伙伴包括 Okta、GitLab、Datadog、OWASP、MongoDB、Twilio、Pluralsight、Retool、Webflow 等，且不少伙伴会重复赞助。
- 📬 资料最后更新于 2026 年 10 月 19 日；可通过 Bonobo Press 联系投放，以触达目标受众并提升线索与转化。

---

