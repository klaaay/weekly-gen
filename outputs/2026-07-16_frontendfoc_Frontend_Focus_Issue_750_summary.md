### [我们还需要构建工具吗？](https://olliewilliams.xyz/blog/no-build/)

**原文标题**: [Do we still need build tools?](https://olliewilliams.xyz/blog/no-build/)

## 概述总结
2026 年，前端构建工具在大型项目中仍不可或缺，但必要性因项目规模而异。CSS 方面，前缀处理、语法降级和预处理器需求减少，但文件合并和压缩仍推荐；JavaScript 方面，模块打包、依赖管理和转译在复杂场景下至关重要，但小型项目可跳过构建步骤。

- 📦 **CSS 构建工具需求降低**：自动前缀工具（如 Autoprefixer）对标准属性非必需；语法降级（如 PostCSS）存在局限性，无法完美模拟新功能；Sass 等预处理器因 CSS 原生特性（如嵌套、颜色函数）而失宠。

- 🔗 **文件合并仍推荐**：通过`@import`或构建工具合并 CSS 文件可减少 HTTP 请求，提升压缩效率（如 gzip/brotli），即使 HTTP/2 下，大量请求仍会造成瓶颈。

- ⚡ **JavaScript 打包优势明显**：打包可优化压缩效率、消除未用代码、减少请求瀑布流，尤其适用于模块数量超过 100 或依赖树深度大于 5 的项目。

- 🌐 **模块预加载替代打包**：使用`<link rel="modulepreload">`可并行加载模块，避免瀑布流，但需手动管理预加载语句，复杂项目可能繁琐。

- 📚 **依赖管理仍依赖工具**：NPM 包管理器处理传递依赖，但直接使用`node_modules`不现实；CDN（如 esm.sh）有维护和安全隐患；现代打包器（如 esbuild、Rolldown）仍是可靠选择。

- 🔄 **转译器需求减少**：Babel 等工具默认不再转译为 ES5，避免不必要的代码膨胀；等待新特性获得浏览器原生支持是有效策略。

- 🛠️ **框架与类型检查**：JSX、TypeScript 和 Tailwind 等流行技术仍需构建步骤；JSDoc 可在无构建时提供类型检查，但语法不友好。

- 😣 **开发者满意度未提升**：构建工具复杂度、配置和性能仍是主要痛点，但完全放弃构建在大型项目中不可行。

---

### [TREX：运行你代码的 AI 代码审查工具 | Greptile](https://www.greptile.com/trex?utm_source=frontendfocus&utm_medium=paid-community&utm_campaign=frontendfocus_primary_jul15)

**原文标题**: [TREX: AI Code Review That Runs Your Code | Greptile](https://www.greptile.com/trex?utm_source=frontendfocus&utm_medium=paid-community&utm_campaign=frontendfocus_primary_jul15)

### 概述总结
TREX 是一款在沙盒环境中自动执行 PR 分支的运行时测试工具，能捕获仅在实际运行时才暴露的缺陷，并提供日志、截图等证据。

- 🧪 **理解变更**：TREX 分析 PR、仓库、测试套件和技术栈，确定需要运行的内容。
- 🛠️ **沙盒执行**：自动启动服务、模拟输入、调用 API 或运行浏览器代理，在隔离环境中执行测试。
- 🔍 **定位故障**：当测试失败时，TREX 追溯至相关代码，并在 PR 评论中附上日志、截图、视频等证据。
- 📈 **提升缺陷捕获率**：相比仅代码审查，TREX 能多捕获约 20% 的运行时缺陷。
- 🔗 **兼容现有技术栈**：支持仓库已有的依赖、框架和测试配置，无需额外适配。
- 🖥️ **端到端测试**：通过模拟输入、启动开发服务器和浏览器代理，完整验证 UI 流程。
- 📋 **证据详尽**：每条发现都附带日志、截图、追踪记录或 API 输出，而非简单报错。
- 🚀 **快速上手**：提供 14 天免费试用，无需信用卡，并支持联系销售获取更多功能。

---

### [为 polyfills 辩护 • Lea Verou](https://lea.verou.me/blog/2026/polyfills/)

**原文标题**: [
		In defense of polyfills • Lea Verou](https://lea.verou.me/blog/2026/polyfills/)

本文探讨了 polyfill 对 Web 平台的价值，反驳了“polyfill 有害”的观点，强调其正面作用远大于负面案例。

- 📌 Polyfill 并非问题根源，开发者使用原生功能的需求才是限制设计灵活性的关键，消除 polyfill 无法消除这一需求。
- 🧩 Polyfill 将 API 设计与实现解耦，标准化 API 是 Web 的“公共广场”，能降低生态系统的耦合成本。
- 🚫 使用独立命名空间（如 vendor prefixes）并未解决问题，开发者会同时使用新旧语法，导致 DX 变差且无设计灵活性。
- ❌ 移除特性检测的 polyfill 会永久增加用户负担，牺牲性能、可访问性等实际利益，成本远高于理论风险。
- 🔄 Ponyfill 缺乏 polyfill 的优势，不利用原生实现、无法轻松移除，本质上是营销更好的用户库。
- ⏳ Polyfill 不会阻碍浏览器实现新特性，反而能激励先行者，若无 polyfill，Web 平台可能停滞。
- ⚠️ Polyfill 仅在标准流程失败时才会造成问题，开发者需求长期未被满足才是根本原因。
- 🛠️ WHATWG 的被动流程（需实现者兴趣才推进）加剧了问题，polyfill 是展示需求的原型工具。
- ⚖️ Polyfill 恢复了生态系统的权力平衡，防止单一浏览器拖慢 Web 发展。
- 🌐 Polyfill 让 Web 更快、更包容、更健壮，原生特性优于任何用户实现，polyfill 是过渡期的必要工具。
- 🧠 应理性进行成本效益分析，而非因少数案例情绪化地反对 polyfill，需主动响应开发者需求。

---

### [Cloudflare 掉线](https://www.cloudflare.com/drop/)

**原文标题**: [Cloudflare Drop](https://www.cloudflare.com/drop/)

Cloudflare Drop 可讓您無需帳號即可將靜態網站部署到 Cloudflare 全球網絡。

- 📂 上傳靜態網站：直接拖曳資料夾或 .zip 檔案（包含 HTML、CSS、JS）即可上傳。
- 🌐 全球分發：Cloudflare Drop 會將網站上傳並分發到其全球網絡。
- 🔗 即時網址：部署完成後，您會獲得一個即時的 `workers.dev` 網址。
- ⏳ 60 分鐘認領：您需要在 60 分鐘內認領部署，否則會失效。
- 🤖 AI 代理適用：僅在具備瀏覽器自動化及完整靜態網站資料夾或 .zip 檔案時使用，部署後需回傳即時網址與認領網址。
- 🛠️ CLI 工作流程：對於本地 CLI 專案，建議使用 Wrangler 而非 Cloudflare Drop；若未認證，可使用 `npx` 或 `npm exec` 指令部署。
- 📁 輸出目錄：部署時需指定專案輸出目錄（如 `./dist`、`./build`），並確保包含 `index.html`。
- ✅ 部署驗證：部署後請驗證即時網址，若返回 404，請稍候再試，因為路由和資源可能需要短暫時間才能生效。
- 🔐 認領網址：認領網址可授予臨時預覽帳號的所有權，請視為敏感資訊，並告知用戶其 60 分鐘後過期。
- 🚫 認證環境：若 Wrangler 已通過 OAuth、API Token 或 API Key 認證，請勿使用 `--temporary` 參數，改用正常的 `wrangler deploy`。

---

### [Netlify](https://app.netlify.com/drop)

**原文标题**: [Netlify](https://app.netlify.com/drop)

概述：Netlify 仪表盘需要启用 JavaScript 才能正常运行，否则无法使用。

- 😞 Netlify 仪表盘需要 JavaScript 支持，否则无法加载
- ⚙️ 用户需在浏览器设置中启用 JavaScript 功能

---

### [Firefox 发布节奏实验：从 9 月起改为每两周一次](https://groups.google.com/a/mozilla.org/g/dev-platform/c/qlaQ1YSlOP8?pli=1)

**原文标题**: [Firefox release cadence experiment: moving to 2 weeks starting in September](https://groups.google.com/a/mozilla.org/g/dev-platform/c/qlaQ1YSlOP8?pli=1)

概述摘要
Mozilla 计划从 2026 年 9 月开始，将 Firefox 桌面版和 Android 版的发布周期从 4 周缩短至 2 周，作为一项实验性调整。

- 📅 从 2026 年 9 月起，Firefox 桌面版和 Android 版发布周期从 4 周改为 2 周
- 🧪 这是一项实验，旨在让就绪的工作更快触达用户
- 🔄 目标包括提高发布流程的可预测性，并减少紧急升级的压力
- ⏳ 未就绪的工作不会被催促，功能仍可按需打磨
- 🎯 首个目标：Firefox 155 计划于 2026 年 9 月 1 日发布，而非 9 月 15 日
- 📊 将密切监测实际效果，并根据需要调整

---

### [获取失败](https://www.w3.org/TR/2026/WD-css-link-params-1-20260714/)

**原文标题**: [Failed to retrieve](https://www.w3.org/TR/2026/WD-css-link-params-1-20260714/)

无法总结：获取内容失败，状态码 403。

---

### [无限滚动可能因加州争议性法律而面临风险](https://www.sfgate.com/politics/article/meta-social-media-teenagers-22337724.php)

**原文标题**: [The infinite scroll may become endangered if controversial Calif. law](https://www.sfgate.com/politics/article/meta-social-media-teenagers-22337724.php)

概述总结
- 🚨 海岸警卫队将暂停搜寻阿尔卡特拉斯附近沉船失踪乘客
- 📱 加州新法案可能要求社交媒体移除“无限滚动”等成瘾功能，保护青少年
- ⚖️ 法案最初拟禁止 16 岁以下儿童使用成瘾性平台，后改为要求平台提供低成瘾性选项
- 🧠 “成瘾功能”定义为旨在最大化用户参与度、导致强迫性使用的心理操纵特性
- 🗓️ 公司需在 2028 年前调整平台，否则将禁止 16 岁以下用户注册
- 👥 法案设立专家监督小组，协助加州总检察长办公室执行
- 🌏 受澳大利亚全球首例青少年社交媒体禁令启发，但考虑 LGBTQ 等群体需求后修正
- 💡 法案支持者认为美国在保护年轻用户方面“落后”，这是加州的正确回应
- 🏛️ 法案现已提交至参议院拨款委员会审议

---

### [“互联网之父”终于要退休了 | TechCrunch](https://techcrunch.com/2026/06/30/the-father-of-the-internet-is-finally-retiring/)

**原文标题**: [The 'Father of the Internet' is finally retiring | TechCrunch](https://techcrunch.com/2026/06/30/the-father-of-the-internet-is-finally-retiring/)

概述总结
- 🔌 互联网先驱 Vint Cerf 将于下周从谷歌首席互联网布道师职位退休，结束其数十年技术生涯。
- 🏆 Cerf 与 Robert Kahn 因共同开发 TCP/IP 协议被誉为互联网之父，曾获总统自由勋章和图灵奖。
- 🤖 Cerf 预测 AI 代理的兴起将推动技术公司回归标准化协议，强调互操作性和精确性对代理间通信的重要性。
- 🌐 会议讨论聚焦于高级 AI 模型集中在少数实验室的问题，与 Cerf 倡导的开放互联网去中心化理念形成对比。
- 👔 同事 Dave Patterson 回忆 Cerf 在 1970 年代作为研究生时便以西装革履的着装风格闻名，称其“穿着最讲究的计算机科学家”。
- 📜 Cerf 认为自然语言（如英语）不适合代理间通信，因其存在歧义，需采用正式标准确保精确协作。

---

### [每次都可以安全遵循的视觉设计规则](https://anthonyhobday.com/sideprojects/saferules/)

**原文标题**: [Visual design rules you can safely follow every time](https://anthonyhobday.com/sideprojects/saferules/)

以下是您提供的视觉设计规则的中文总结：

概述总结
这些是安全可靠的视觉设计规则，但如果有充分理由，也可以打破它们。

- 🎨 使用接近黑色和接近白色，而非纯黑纯白：纯黑对比度过高，纯白过于刺眼，使用接近色更舒适。
- 🎭 为中性色添加饱和度：在灰、黑、白中加入少量界面主色（HSB 饱和度<5%），让调色板更协调。
- 🔍 重要元素使用高对比度：按钮、内容等需用户注意的部分用高对比度吸引目光；次要元素（如结构线、阴影）可用低对比度。
- 🧠 设计中每个元素都应有意图：空白、对齐、大小、间距、颜色、阴影等，每个细节都要能解释其存在理由。
- 👁️ 视觉对齐常优于数学对齐：某些形状的视觉中心与数学中心不同，需用肉眼调整对齐。
- 🔤 大文字降低字间距和行高，小文字增加：文字越大，字间距和行高应越小；反之亦然。
- 🖼️ 容器边框需与容器和背景都形成对比：边框亮度应比容器和背景都亮（暗背景）或都暗（亮背景），确保边缘清晰。
- 📐 每个元素都应与某物对齐：对齐建立元素间的关联，无对齐的元素会显得格格不入。
- 🌈 调色板中的颜色应有明显亮度差异：不同亮度值让颜色在色相和亮度上都有区分，避免相互竞争。
- 🌡️ 中性色添加饱和度时，只选暖色或冷色：同时使用暖色和冷色会让调色板不协调。
- 📏 测量值应有数学关系：元素间距和尺寸应基于某种比例（如 8 的倍数），让设计更连贯。
- ⚖️ 元素按视觉重量排序：一行或一列中的元素，按视觉重量从重到轻排列，最重元素放在外侧边缘。
- 🏛️ 使用水平网格时，选 12 列：12 列网格可灵活拆分为 1、2、3、4 列，提供最大灵活性。
- 📏 间距应从高对比点之间测量：例如段落间距应从一段结束到下一段开始（或到背景色边界）。
- 🌑 越靠近用户的元素应越亮：无论浅色还是深色模式，靠近用户的元素颜色更亮，符合现实世界规律。
- 💡 投影模糊值设为距离值的两倍：例如 Y 轴偏移 4px，模糊值用 8px；元素越“近”，阴影不透明度越低。
- 🧩 简单背景配复杂前景，或复杂背景配简单前景：避免复杂对复杂，以免视觉杂乱。
- 🎚️ 容器颜色亮度差控制在 12%（深色界面）或 7%（浅色界面）以内：基于对约 100 个优秀网站的研究。
- 📦 容器外内边距关系：外内边距（容器边缘与内部元素间距）应大于或等于内内边距（内部元素间距）。
- 📝 正文文字至少 16px：16px 是浏览器默认大小，低于此值难以阅读。
- 📖 行长约 70 个字符：60-80 字符范围内均可，过短或过长影响可读性。
- 🔘 按钮水平内边距是垂直内边距的两倍：标准按钮形状更宽，遵循此模式更易识别。
- ✒️ 最多使用两种字体：第二种字体可强化设计概念，超过两种容易造成视觉混乱。
- 🔲 嵌套圆角正确计算：内角半径 = 外角半径 - 间距，例如外角 30px、间距 20px，内角 10px。
- 🚫 避免两个硬分割相邻：背景过渡、容器边缘、分割线等硬分割不要相邻，以免视觉杂乱。
- 🌙 深色界面避免使用阴影：深色背景难以显示阴影，且阴影在暗处不自然。
- 🛑 不要混用不同深度技术：整个界面统一使用一种阴影风格（软阴影、硬阴影或无阴影），保持一致性。
- 🔽 图标与文字搭配时降低对比度：图标视觉重量通常比文字重，降低其背景对比度（如调整不透明度）使视觉平衡。

---

### [一个只影响左撇子用户的漏洞——特伦斯·伊甸的博客](https://shkspr.mobi/blog/2026/07/a-bug-which-only-affected-left-handed-users/)

**原文标题**: [A bug which only affected left-handed users – Terence Eden’s Blog](https://shkspr.mobi/blog/2026/07/a-bug-which-only-affected-left-handed-users/)

概述总结  
- 🐛 一个仅影响左撇子用户的 WordPress 评论 bug，因触摸事件监听导致左撇子用户在滚动时意外触发回复框。  
- 📱 作者通过优化博客 JavaScript，发现 bug 源于 2017 年添加的`touchstart`监听器，该代码在触摸延迟已解决的 2013 年后仍存在。  
- 🛠️ 作者在报告七年后提交修复，仅删除两行代码，但幽默调侃无法阻止“不洁用户”使用网站。  
- 💬 评论区用户分享左右手使用习惯差异，指出 bug 也影响右撇子用户，并提供了 CSS/JS 解决方案。

---

### [适用于任何规模的时间序列工作负载的 Postgres。| Tiger Data](https://www.tigerdata.com/go/trial?utm_source=content-syndication&utm_medium=referral&utm_campaign=frontend-focus-newsletter)

**原文标题**: [Postgres for time-series workloads at any scale. | Tiger Data](https://www.tigerdata.com/go/trial?utm_source=content-syndication&utm_medium=referral&utm_campaign=frontend-focus-newsletter)

Tiger Cloud 提供大规模时间序列数据处理的 Postgres 服务，支持高达 3 万亿指标/天和 1 千万亿数据点，并为企业提供免费试用和全方位功能。

- 📊 支持每天处理 3 万亿指标和 1 千万亿数据点，具备真实世界的大规模扩展能力
- 💰 提供$1000 免费试用额度（30 天有效），无需信用卡，仅限新用户
- 🚀 通过最多 10 个节点的副本集实现读写分离，结合 SSD/S3 分层存储实现无限制、低成本扩展
- 💡 计算与存储分离架构，可独立扩展，避免为闲置容量付费
- 🔒 多可用区集群支持自动故障转移、时间点恢复和跨区域备份，确保高可用性
- 🛡️ 企业级安全：SOC 2、HIPAA、GDPR 合规，全程加密、SSO 集成、RBAC 和审计日志
- 📈 深度可观测性：查询钻取和仪表盘，支持集成 CloudWatch、Datadog、Prometheus 等工具
- ⚡ 快速部署：数分钟内完成数据库配置，支持 SQL、CLI、Terraform、Cursor 或 Claude Code 管理
- 🔌 与主流云提供商和 Postgres 生态系统无缝集成
- 🏢 企业级支持：合同化 SLA、区域数据隔离、24/7 全球专家支持和保证响应时间

---

### [CSS @layer 中的水平思考 – Master.dev 博客](https://master.dev/blog/thinking-horizontally-in-css-layer/)

**原文标题**: [Thinking Horizontally in CSS @layer – Master.dev Blog](https://master.dev/blog/thinking-horizontally-in-css-layer/)

本文探讨了 CSS @layer 的一种横向思维方式，强调通过弱化层叠顺序来简化组件样式管理。

- 📚 核心概念：@layer 像 CSS 的 z-index，但用于控制样式优先级，可创建垂直堆叠的层
- 🧩 子层语法：使用点号定义子层（如@layer components.button），支持更精细的层级管理
- 🏗️ 组件化挑战：大量组件无需关心彼此优先级，可统一放入 components 层，避免垂直排序
- 🎨 分层策略：将组件的 CSS 自定义属性放入@layer 中弱化，而作用域样式不放入层，保持灵活性
- ⚡ 横向思维：将组件视为水平排列的“双叠层”，而非垂直堆叠，降低优先级管理复杂度
- 💡 实际应用：CodePen 将组件自定义属性放入@layer，使其容易被未分层样式覆盖，简化覆盖操作
- 🔧 技术优势：通过弱化层内属性，任何未分层样式（即使选择器较弱）都能轻松覆盖组件变量

---

### [使用 HTML 和 CSS 构建一个神奇的 3D 按钮 • Josh W. Comeau](https://www.joshwcomeau.com/animation/3d-button/)

**原文标题**: [Building a Magical 3D Button with HTML and CSS • Josh W. Comeau](https://www.joshwcomeau.com/animation/3d-button/)

本教程详细讲解了如何使用 HTML 和 CSS 创建一个具有 3D 立体感和生动交互反馈的按钮，涵盖了从基础结构到高级动画和移动端优化的完整流程。

- 🎯 **核心策略**：通过滑动前景层（.front）在静态背景（按钮边缘）上制造 3D 按压错觉，避免使用性能昂贵的`box-shadow`或`border`动画。
- 🧱 **基础结构**：按钮包含`<button>`容器、前景层`<span class="front">`，通过`transform: translateY()`控制上下位移，并利用`:active`伪类实现按压效果。
- 👁️ **焦点管理**：使用`:focus:not(:focus-visible)`选择器，在鼠标点击时隐藏轮廓，同时保留键盘导航用户的焦点指示，兼顾美观与无障碍。
- 🖱️ **悬停与过渡**：为不同状态（悬停、按压、释放）设置独立的`transition`时长和贝塞尔曲线，实现快速按压、弹性回弹和缓慢恢复的个性化动画。
- 🌟 **阴影与层次**：新增`.shadow`层（带模糊滤镜）和`.edge`层（带渐变背景），阴影与前景反向移动，强化 3D 立体感；悬停时使用`filter: brightness(110%)`整体提亮。
- 📱 **移动端优化**：通过`-webkit-tap-highlight-color: transparent`去除点击高亮，`user-select: none`禁止文本选择，提升触屏体验。
- 🎨 **最终效果**：按钮包含三层结构（阴影、边缘、前景），结合多状态过渡、颜色渐变和亮度滤镜，打造出富有弹性和个性的 3D 交互按钮。

---

### [永无止境的故事：使用 GSAP 和 Lenis 构建无缝无限滚动体验 | Codrops](https://tympanus.net/codrops/2026/05/28/the-never-ending-story-building-a-seamless-infinite-scroll-experience-with-gsap-lenis/)

**原文标题**: [The Never Ending Story: Building a Seamless Infinite Scroll Experience with GSAP & Lenis | Codrops](https://tympanus.net/codrops/2026/05/28/the-never-ending-story-building-a-seamless-infinite-scroll-experience-with-gsap-lenis/)

本教程详细讲解如何利用 GSAP 和 Lenis 构建无缝无限滚动体验，并加入视差深度效果，让页面滚动变得流畅且令人上瘾。

- 🔄 **无限循环机制**：通过复制第一个区块并放置在末尾，配合 Lenis 的`infinite: true`设置，实现无缝滚动，用户感觉不到页面重置。
- 🎨 **视差深度效果**：使用 GSAP 的`fromTo`动画，让媒体元素在滚动时从`-50%`移动到`50%`，产生层次感和深度，增强视觉体验。
- 📐 **快照控制节奏**：通过 Lenis Snap 插件实现强制快照，设置对齐方式和缓动函数，让滚动节奏更清晰、操作更可控。
- 🛠️ **轻量级技术栈**：教程使用纯 HTML、CSS 和 JavaScript，不依赖框架，降低学习门槛，核心依赖仅为 Lenis 和 GSAP。
- 📱 **iOS 兼容性修复**：针对 Safari 工具栏问题，通过自定义滚动容器（wrapper）和`scroll-scroller`代理，确保无缝循环在 iOS 设备上正常工作。
- 🧩 **高级集成扩展**：可添加曲线跑马灯等组件，利用 ScrollTrigger 控制速度和缩放，以细节提升整体质感，避免过度编码。

---

### [无缝无限滚动体验 | Codrops](https://tympanus.net/Tutorials/InfiniteScrollParallax/)

**原文标题**: [Seamless Infinite Scroll Experience | Codrops](https://tympanus.net/Tutorials/InfiniteScrollParallax/)

本教程展示了如何利用 GSAP 和滚动技术实现无缝无限滚动体验，包含多个演示和 GitHub 源码。

- 🎯 核心功能：实现平滑的无缝无限滚动效果
- 📚 教程资源：包含详细教程、多个演示示例及 GitHub 源码
- ⚙️ 技术栈：使用 GSAP 动画库结合滚动与视差效果
- 👤 作者信息：由 Joe Taylor（创始人/创作者/制作人）提供

---

### [如何使用 CSS "zoom"缩放元素及其布局 | Stefan Judis Web 开发](https://www.stefanjudis.com/today-i-learned/css-zoom-to-scale-elements/)

**原文标题**: [How to scale elements and their layout with CSS "zoom" | Stefan Judis Web Development](https://www.stefanjudis.com/today-i-learned/css-zoom-to-scale-elements/)

### 概述
本文介绍了 CSS `zoom` 属性，它能够真正缩放元素及其布局，与仅改变视觉外观的 `transform: scale()` 不同。文章还涵盖了浏览器支持情况、使用注意事项以及已知的浏览器不一致性问题。

- 🔍 `zoom` 属性可以同时缩放元素的视觉大小和布局尺寸，而 `transform: scale()` 只改变视觉外观，布局空间保持不变
- 🌐 浏览器支持情况良好，主流浏览器（Chrome、Firefox、Safari）均已支持
- ⚠️ 应避免对 `zoom` 进行动画处理，因为布局变化可能导致浏览器性能问题
- 🐛 Safari 存在已知问题：使用 `getBoundingClientRect()` 时不会返回缩放后的实际布局尺寸，仍显示原始大小（120×120px），而 Chrome 和 Firefox 表现正常
- 📚 本文来自作者“今日学习”系列，分享 Web 开发中的实用技巧

---

### [我曾以为 AVIF 能让每张图片更小，但事实并非如此。——Stuff & Nonsense](https://stuffandnonsense.co.uk/blog/webp-to-avif-gotcha/)

**原文标题**: [I thought AVIF would make every image smaller. It didn’t. - Stuff & Nonsense](https://stuffandnonsense.co.uk/blog/webp-to-avif-gotcha/)

Eleventy in a Box 是一款高级 Eleventy 启动套件，旨在帮助设计师和开发者减少项目搭建时间，专注于设计独特的网站。

- 🎨 专为设计师和开发者打造的高级启动套件
- ⏱️ 减少重复的项目结构设置时间
- 🌟 帮助用户更专注于设计独特网站
- 🛒 提供购买选项，可直接获取使用

---

### [如何在 CSS 中创建令人惊叹的交错动画 - LogRocket 博客](https://blog.logrocket.com/css-staggered-animations/)

**原文标题**: [How to create awesome staggered animations in CSS - LogRocket Blog](https://blog.logrocket.com/css-staggered-animations/)

本文介绍了如何使用现代 CSS 实现交错动画，并探讨了其优势、实现方法及无障碍性考量。

- 📝 **交错动画定义**：通过为多个元素设置不同的动画延迟，使其依次启动，形成连贯、自然的视觉效果，避免所有元素同时运动。
- 🎯 **使用原因**：引导用户注意力、建立 UI 层次、让信息分块呈现，提升用户体验。
- ⚙️ **核心实现**：利用 CSS 函数 `sibling-index()` 和 `sibling-count()` 计算延迟，通过 `animation-delay` 属性设置，实现递增或递减的交错效果。
- 🧩 **代码示例**：列表项淡入放大动画，使用 `calc((sibling-index() - 1) * 100ms)` 计算延迟，支持重叠与非重叠效果。
- 🔄 **方向控制**：通过 `sibling-count() - sibling-index()` 实现反向交错，适用于关闭或移除元素的动画。
- 🎨 **应用场景**：英雄区内容引导、聊天界面逐字动画等，让用户逐步消费内容。
- 🛠️ **JavaScript 必要性**：用于触发交互（如点击展开/收起）、退出动画（元素移除时）及复杂逻辑动画（如电影卡片选择）。
- 📉 **降级方案**：使用 `@supports not` 规则，为不支持 `sibling-index()` 的浏览器提供备用样式（如 `nth-child` 或自定义属性）。
- ♿ **无障碍性**：通过 `prefers-reduced-motion` 媒体查询关闭或简化动画，避免引发用户不适。
- 🌐 **浏览器支持**：`sibling-index()` 和 `sibling-count()` 在 Chromium 和 Safari 中支持，覆盖约 75% 浏览器，可作为渐进增强使用。

---

### [介绍 Precursor：通过持续客户端信号检测代理行为 | Cloudflare 博客](https://blog.cloudflare.com/introducing-precursor/)

**原文标题**: [Introducing Precursor: detecting agentic behavior with continuous client-side signals | The Cloudflare Blog](https://blog.cloudflare.com/introducing-precursor/)

Cloudflare 推出 Precursor，一种基于客户端会话的验证系统，通过持续收集用户行为信号来区分人类与自动化流量，弥补现有检测的可见性缺口。

- 🤖 Precursor 是一种客户端、基于会话的验证系统，通过动态注入 JavaScript 持续收集行为信号，实时区分人类与自动化流量
- 🎯 它弥补了 Turnstile 等挑战式验证的可见性缺口，覆盖整个用户旅程，而不仅仅是登录、注册等关键端点
- 🖱️ 人类鼠标运动受物理限制（如手腕旋转、认知延迟、手部震颤），而机器人运动常呈现直线或完美曲线，难以模拟真实行为
- 🔄 Precursor 通过注入轻量脚本收集指针移动、键盘活动、焦点变化等信号，并在边缘服务器实时分析，跨会话累积行为特征
- 🔒 隐私设计：仅捕获行为模式（如键盘节奏而非按键内容），信号不暴露给客户仪表盘，不关联用户身份或持久档案
- 📊 提供基于会话的分析仪表盘，帮助客户理解典型会话行为、识别异常和自动化迹象
- 🚀 Precursor 现已推出，可免费使用至正式发布，与现有 Bot Management 和 Turnstile 无缝集成，无需修改应用

---

### [前身 · Cloudflare 挑战文档](https://developers.cloudflare.com/cloudflare-challenges/precursor/)

**原文标题**: [Precursor Â· Cloudflare challenges docs](https://developers.cloudflare.com/cloudflare-challenges/precursor/)

### 概述总结
Precursor 是 Cloudflare 推出的客户端持续验证系统，通过行为分析检测自动化流量，提供两种模式平衡用户体验与安全性。

- 🔍 **持续验证机制**：在浏览器中注入脚本，持续收集行为信号并评估会话状态，替代一次性挑战。
- ⚙️ **两种操作模式**：默认"最小摩擦"（后台验证）与推荐"最大安全"（显示轻量挑战），用户可根据需求选择。
- 🛡️ **规则灵活配置**：可针对不同路径（如/checkout）或 API 端点应用不同模式，支持混合流量场景。
- 🔗 **与 API 兼容**：需确保浏览器 API 请求包含 cookies（如`credentials: "include"`），非浏览器客户端可能受影响。
- 🚫 **替代 JavaScript 检测**：启用 Precursor 后应禁用 JSD，因其提供更全面的会话级验证。
- 🔄 **增强现有挑战**：不取代传统挑战，而是通过持续评估决定何时触发额外验证，识别随时间演变的自动化行为。
- 📊 **可见性提升**：检测结果会显示在安全分析中，包括机器人评分分布和 WAF 规则匹配计数。

---

### [无](https://expo.dev/blog/a-hell-of-a-time-to-be-a-builder?utm_source=frontendfocus&utm_medium=email&utm_campaign=33087804-React%2520to%2520Native)

**原文标题**: [None](https://expo.dev/blog/a-hell-of-a-time-to-be-a-builder?utm_source=frontendfocus&utm_medium=email&utm_campaign=33087804-React%2520to%2520Native)

概述摘要：  
本文探讨了人工智能在医疗领域的应用，包括诊断辅助、药物研发和个性化治疗，同时强调了数据隐私和伦理挑战的重要性。  

- 🩺 人工智能通过分析医学影像（如 X 光片和 CT 扫描）提升疾病诊断的准确性和效率。  
- 💊 机器学习算法加速药物发现过程，通过模拟分子相互作用缩短研发周期。  
- 🧬 个性化治疗方案利用患者基因数据，优化药物剂量和疗法选择。  
- 🔒 数据隐私问题需严格保护，确保患者信息在 AI 系统中的安全使用。  
- ⚖️ 伦理挑战包括算法偏见和医疗决策责任归属，需建立透明监管框架。

---

### [Color.js：让我们认真对待色彩 • Color.js](https://colorjs.io/)

**原文标题**: [Color.js: Let’s get serious about color • Color.js](https://colorjs.io/)

Color.js 是一个专业的色彩转换与处理库，由 CSS 颜色规范编辑共同开发，支持多种色彩空间和高级色彩科学功能。

- 🎨 支持多种色彩空间：涵盖 Lab/LCh、OKLab/OKLCh、sRGB、Display P3 等丰富色彩模型
- 🔬 专业色彩科学：提供真实色域映射、多种 DeltaE 色差算法和色适应方法
- 🌐 兼容 CSS Color 4：支持所有 CSS 颜色格式的输入与输出，无需浏览器支持
- 🧩 模块化可扩展：可按需加载模块，支持客户端和 Node.js，提供钩子扩展
- ⚡ 高效无依赖：提供过程式 API 优化性能，零外部依赖
- 📈 广泛影响力：超 2.41 亿 npm 下载量，被 Sass、axe 等知名项目采用
- 🛠 灵活安装：支持 CDN 直接导入、npm 安装或源码模块化引用
- 📝 易用 API：支持链式操作、属性直接修改和静态函数调用
- 🔄 色彩转换：轻松在不同色彩空间间转换，支持色域裁剪控制
- 🎯 插值功能：提供百分比步进、离散步数和混合等插值方法
- 🧪 实验项目：包含色彩元素 Web 组件、色彩应用和调色板研究项目
- 👥 核心团队：由 Lea Verou 和 Chris Lilley 等 8 位维护者共同管理
- 💰 开源赞助：通过 Open Collective 接受赞助，支持项目可持续发展

---

### [发布 v0.7.0 · color-js/color.js · GitHub](https://github.com/color-js/color.js/releases/tag/v0.7.0)

**原文标题**: [Release v0.7.0 · color-js/color.js · GitHub](https://github.com/color-js/color.js/releases/tag/v0.7.0)

以下是您提供的文本的概述和要点总结：

Color.js v0.7.0 版本发布，带来了大量新功能、新色彩空间、改进的色域映射方法，以及多项修复和优化，下载量已超过 2.4 亿次。

- 🚀 下载量突破 2.4 亿次：Color.js 在 npm 上的下载量已超过 2.4 亿次，项目依赖 Open Collective 支持可持续发展。
- 🆕 新增 6 个色域相对色彩空间：引入 oklch-p3、oklch-srgb 等，其中 c=1 表示色域内最鲜艳的颜色，避免出界问题。
- 🆕 扩展 HSL 语法：新增 hsl-p3 和 hsl-rec2020，支持更广色域的 HSL 表示。
- 🆕 实验性 Helmlab 色彩空间：包括 helmlab-metric、helmgen 和 helmgenlch，提供新的感知色彩模型。
- 🆕 智能 display() 回退：当浏览器不支持颜色时，自动选择最接近的受支持色彩空间，保留色域信息。
- 🆕 新增 raytrace 色域映射方法：通过射线追踪到色域边界，替代二分搜索，提高映射效率。
- 🆕 新增 deltaEHelmlab 色差方法：基于 Helmlab 模型计算色差。
- 🆕 serialize() 新增 collapse 选项：可选择禁用十六进制颜色压缩，如保留 #ff0066 而非 #f06。
- 🔧 内部改进：暴露变换矩阵、矩阵代数工具，以及极坐标空间的色调坐标声明，方便插件开发。
- 🐛 修复极坐标空间插值问题：修正预乘插值中色调角度的处理，避免 NaN 和错误结果。
- 🐛 其他修复：修复 helmgenlch 序列化、色域表面阈值更新、类型字段恢复等。

---

### [UX 组件](https://www.ux-components.com/)

**原文标题**: [UX Components](https://www.ux-components.com/)

本页面提供了一个跨设计系统的 UI 组件实用参考工具，帮助用户浏览、比较并理解各组件的用途与使用时机。

- 🧩 提供每个组件的使用指南、状态说明及 AI 提示，支持默认与原子化视图
- 🔍 支持跨设计系统对比同一组件的命名差异，涵盖组件与状态维度
- 📂 提供设计系统与图标库的目录浏览，包含 W3C ARIA 无障碍模式映射
- 🎨 支持通用图标浏览与对比，可并排预览不同库中的图标名称
- 🤖 提供 UX Components MCP 服务器，支持 AI 工具通过 MCP 连接组件数据
- 📝 提供 DESIGN.md 参考，可将品牌标识交给 AI 设计代理处理

---

### [Rombo | Tailwind CSS 动画库](https://rombo.co/tailwind/)

**原文标题**: [Rombo | Animation library for Tailwind CSS Library](https://rombo.co/tailwind/)

概述摘要  
tailwindcss-motion 是一个为 Tailwind CSS 设计的动画库，提供简洁语法、高性能和可访问性，支持多种预设动画和自定义配置，并附带可视化动画工具。  

- 🎬 提供多种预设动画效果，如淡入、滑动、聚焦、模糊、弹跳、打字机等  
- ⚙️ 支持自定义动画设置，包括持续时间、缩放、平移、旋转、模糊等参数  
- ♿ 默认内置动画可访问性，确保无障碍体验  
- 🚀 经过性能测试和优化，兼容浏览器并保障帧率稳定  
- 📦 安装简单，通过 npm 安装后添加到 tailwind.config.js 插件即可  
- 🔧 提供可视化动画器，支持拖拽创建动画并导出为 Tailwind CSS、Framer Motion 等代码  
- 🆓 开源且基于 MIT 许可证，可自由使用和修改

---

### [A-Frame – 制作 WebVR](https://aframe.io/)

**原文标题**: [A-Frame – Make WebVR](https://aframe.io/)

A-Frame 是一个用于构建 3D/AR/VR 体验的 Web 框架，支持通过 HTML 和实体组件创建 3D 世界，并兼容各种头显、移动设备和桌面端。最新版本 1.8.0 带来了 ThreeJS 更新、20 多个错误修复和 15 项改进。

- 🚀 **A-Frame 1.8.0 发布**：更新了 ThreeJS，修复了 20 多个错误并进行了 15 项改进
- 🌐 **跨平台支持**：可在任何头显、移动设备和桌面端运行
- 📝 **HTML 实体组件**：通过简单的 HTML 和实体组件构建 3D 世界
- 🎮 **丰富示例**：包括 Hello WebVR、模型查看器、手部追踪、360°图像/视频、后处理等
- 🕶️ **WebGPU 和 TSL 支持**：新增对 WebGPU 和 TSL 技术的支持
- 🎯 **社区与资源**：提供文档、FAQ、博客、社区和展示案例
- 🏆 **特别赞助商**：有专门的赞助商支持

---

### [GitHub - mozilla/web-ext: 一个帮助构建、运行和测试网络扩展的命令行工具 · GitHub](https://github.com/mozilla/web-ext)

**原文标题**: [GitHub - mozilla/web-ext: A command line tool to help build, run, and test web extensions · GitHub](https://github.com/mozilla/web-ext)

这是一个 Mozilla 开发的命令行工具，用于帮助构建、运行和测试 WebExtensions（浏览器扩展），支持跨平台使用，并针对 Firefox 扩展开发进行了优化。

- 🛠️ **核心功能**：提供 `run`（运行扩展）、`lint`（验证源码）、`sign`（签名扩展）、`build`（打包扩展）和 `docs`（打开文档）等命令。
- 📦 **安装方式**：支持通过 npm 全局安装或作为项目依赖安装，也提供 Homebrew 非官方安装方式，以及从源码构建。
- 💻 **NodeJS 集成**：从 7.0.0 版本起支持在 NodeJS 代码中直接调用 web-ext 命令，例如通过 `webExt.cmd.run()` 运行扩展，并支持自定义日志级别和禁用标准输入。
- 🔧 **高级用法**：支持 Firefox for Android 扩展运行、通过 `webExt.cmd.sign()` 签名扩展、以及直接使用内部模块 `signAddon` 提交 xpi 文件。
- 🌟 **社区与贡献**：项目活跃，拥有 3.1k 星标和 381 个分支，鼓励通过提交 issue、pull request 或联系团队参与开发。

---

### [GitHub - pwa-today/pwa-check: 一个自动化的 PWA 健康检查工具 · GitHub](https://github.com/pwa-today/pwa-check)

**原文标题**: [GitHub - pwa-today/pwa-check: An automated PWA health check tool · GitHub](https://github.com/pwa-today/pwa-check)

概述：pwa-check 是一个自动化 PWA 健康检查工具，用于检测 Web 应用是否具备安装、离线运行和像真实 PWA 一样工作的能力。

- 📱 **Web App Manifest 检查**：检测 HTML 或 JavaScript 中的清单文件，验证 scope、display、start_url、图标等关键属性，确保资源可访问。
- 🖥️ **视口 meta 标签检查**：确认是否包含 width=device-width、initial-scale=1 和 viewport-fit=cover 配置，缺失时会给出具体警告。
- 📲 **iOS 启动图像检查**：检测是否通过 apple-touch-startup-image 链接定义了 iOS 启动画面，避免首次启动体验不佳。
- ⚙️ **Service Worker 检查**：验证注册及 install、activate、fetch 等处理程序，支持 Workbox 风格，确保离线行为正常。
- ✅ **输出与 CI 集成**：CLI 输出 pass/warn/fail 状态，失败时退出码非零，支持--json、--fail-on-warn 等标志，便于集成到 CI 流程。
- 🚀 **使用方式灵活**：可直接运行于 URL，或通过 npm 全局/本地安装使用，支持超时、忽略警告等参数。
- ⚠️ **警告代码系统**：提供稳定警告代码（如 manifest.share-target.missing），可通过--ignore-warn 忽略特定问题。
- 🧪 **测试与许可**：运行 npm test 执行测试套件，采用 ISC 许可证。

---

### [使用 Foxit eSign API 进行嵌入式签名](https://developer-api.foxit.com/developer-blogs/api-guides-tutorials/embedded-signing-esign-api/?utm_source=draftdev&utm_medium=newsletter&utm_campaign=frontendfocus_20260715)

**原文标题**: [Embedded Signing with the Foxit eSign API](https://developer-api.foxit.com/developer-blogs/api-guides-tutorials/embedded-signing-esign-api/?utm_source=draftdev&utm_medium=newsletter&utm_campaign=frontendfocus_20260715)

概述总结  
本文介绍了如何利用大型语言模型（LLM）智能体与 PDF API 结合，实现文档的自动化转换、提取和签名，从而构建无需人工干预的智能文档工作流。

- 🤖 智能体工作流超越传统文档检索，能自动完成转换、合并和签名等操作  
- 📄 通过 Foxit 的生产级 PDF API，实现文档处理流程的自动化  
- 🔄 LLM 智能体驱动文档任务，无需人工介入即可高效执行  
- 🛠️ 本指南提供具体方法，展示如何集成这些技术以扩展文档处理规模

---

### [Puter 开发者 - AI 生成应用的后端](https://developer.puter.com/?utm_source=frontend-focus&utm_medium=sponsored-email&utm_campaign=puter-2026-07-15&utm_content=start-building)

**原文标题**: [Puter Developer - The Backend for AI-Generated Apps](https://developer.puter.com/?utm_source=frontend-focus&utm_medium=sponsored-email&utm_campaign=puter-2026-07-15&utm_content=start-building)

## 概述总结
Puter.js 是一个专为 AI 生成应用设计的无服务器、无密钥 JavaScript SDK，提供安全、生产就绪的后端解决方案，包含认证、存储、数据库和 AI 网关等功能，采用创新的“用户付费”模式，让开发者无需承担基础设施成本。

- 🚀 **一站式后端解决方案**：整合认证、存储、数据库、AI 网关（500+ 模型）等所有 API，仅需一个`<script>`标签即可使用
- 🔑 **无密钥设计**：无需 API 密钥，前端直接调用后端功能，消除密钥泄露、窃取或轮换的安全风险
- 🛡️ **内置安全防护**：每个请求都经过认证、用户范围限定、速率限制和滥用过滤，自动阻止机器人流量、DDoS 攻击等威胁
- 💰 **开发者零成本**：采用“用户付费”模式，用户使用自己的资源配额，开发者无论用户数量多少都无需支付基础设施费用
- 🤖 **AI 编码优化**：语法简洁一致，LLM 可准确使用；提供`llms.txt`让 AI 工具一次性读取完整 API；相比 Supabase、Vercel 等方案可减少 90% 的 AI 代币消耗
- 📊 **广泛采用**：已有 80K+ 开发者、130K+ 应用和 400K+ 安装量
- 🔄 **框架兼容**：可与 React、Next.js、Vue、Angular、Svelte 等任何现代 JavaScript 框架集成
- 🎯 **AI 代理通用**：兼容 Claude Code、Codex、Cursor、GitHub Copilot、v0、Bolt、Lovable 等所有 AI 编码助手和平台

---

### [Hyperblam 文档首页：HYPERBLAM](https://hyperblam.how/)

**原文标题**: [Hyperblam Docs Home : HYPERBLAM](https://hyperblam.how/)

概述总结  
HYPERBLAM 是一个基于 HTML 的声明式音乐制作工具，完全依赖 Web Audio API，无需编写 JavaScript 即可创建音效、鼓机和采样乐器。它强调独立性、灵活性和概率性，支持多种音乐创作方式，并提供沙盒环境供用户快速上手。

- 🎵 用 HTML 声明式创建音乐，无需 JavaScript 基础  
- 🎛️ 支持制作踏板效果、鼓机、采样乐器等  
- 🔧 自定义元素处理采样、排序等所有功能  
- 🚫 不依赖大型库或专有技术，完全独立  
- ⚡ 可无限叠加效果、低频振荡器和辅助包络  
- 🎶 灵活创建多节奏节拍、生成式音效或游戏背景音  
- 🎲 通过随机因子和调制模拟即兴创作  
- 🤖 专注于原创声音，不涉及 AI 抄袭  
- 💻 提供 CodePen 沙盒环境，含示例和指南，方便快速上手

---

### [我身兼多职：HYPERBLAM](https://hyperblam.how/examples/01-i-wear-many-hats/)

**原文标题**: [I wear many hats : HYPERBLAM](https://hyperblam.how/examples/01-i-wear-many-hats/)

概述摘要：该内容涉及安装和采样文件的操作步骤，重点在于文件处理流程。

- 🔧 安装过程：包含对系统或软件的初始化设置步骤。
- 📂 采样文件：指定对特定文件进行数据提取或处理操作。

---

### [获取失败](https://codepen.io/heydon/pen/RNKgMEe)

**原文标题**: [Failed to retrieve](https://codepen.io/heydon/pen/RNKgMEe)

无法总结：获取内容失败，状态码 403。

---

