### [发布 v4.3.2 · tailwindlabs/tailwindcss · GitHub](https://github.com/tailwindlabs/tailwindcss/releases/tag/v4.3.2?ref=tailwindweekly.com)

**原文标题**: [Release v4.3.2 · tailwindlabs/tailwindcss · GitHub](https://github.com/tailwindlabs/tailwindcss/releases/tag/v4.3.2?ref=tailwindweekly.com)

Tailwind CSS v4.3.2 版本发布，主要修复了多个错误并提升了稳定性。

- 🐛 修复 `auto-rows-*` 和 `auto-cols-*` 工具类对裸间距值的支持（如 `auto-rows-12` 和 `auto-cols-16`）
- 🪟 修复 Windows 上 `@tailwindcss/cli` 在 `--watch` 模式下因 `@source` 指向不存在的目录而崩溃的问题
- 🦕 修复 Deno v2.8.x 中 `@tailwindcss/vite` 因 `context.parentURL` 无效而崩溃的问题
- 🔄 确保 `@tailwindcss/cli` 在 `--watch` 模式下，当输入 CSS 文件位于被忽略目录中时能正确重建
- 🧩 允许 `addBase(…)` 中使用的 `@variant` 规则引用之后定义的自定义变体
- 🗑️ 修复 `@tailwindcss/vite` 在 HMR 期间因扫描文件或目录被删除而崩溃的问题
- 🎨 为 `text-[--spacing(…)]` 生成 `font-size` 而非 `color` 声明
- 📁 防止 `@source` 模式扫描无关的兄弟文件和文件夹
- 🔍 在 `.tt`、`.tt2` 和 `.tx` 文件中提取模板工具包分隔符（如 `%]…[%`）旁的类候选
- 🖋️ 提取条件性 Maud 语法（如 `p.text-black[condition]`）中的类候选
- ⚠️ 防止 `@position-try` 规则在优化 CSS 时触发未知 at-rule 警告
- 🎯 支持从 `--opacity` 主题值为命名不透明度修饰符提供类建议
- 📦 修复 `@tailwindcss/postcss` 与较新 PostCSS 补丁版本一起使用时出现的类型错误

---

### [GitHub - francoismassart/eslint-plugin-tailwindcss 在 tailwindweekly.com · GitHub](https://github.com/francoismassart/eslint-plugin-tailwindcss?ref=tailwindweekly.com)

**原文标题**: [GitHub - francoismassart/eslint-plugin-tailwindcss at tailwindweekly.com · GitHub](https://github.com/francoismassart/eslint-plugin-tailwindcss?ref=tailwindweekly.com)

eslint-plugin-tailwindcss 是一个专为 Tailwind CSS v4 设计的 ESLint 插件，提供 7 条规则以增强代码一致性和最佳实践，支持自动修复和自定义配置，并鼓励社区贡献。

- 📦 **安装与配置**：通过 `npm i -D eslint-plugin-tailwindcss` 安装，需在 `eslint.config` 文件中导入并设置 `cssConfigPath` 指向 Tailwind CSS v4 的 `.css` 配置文件。
- 🛠️ **核心规则**：包含 7 条规则，如 `classnames-order`（排序）、`enforces-shorthand`（简写）、`no-contradicting-classname`（避免矛盾）等，部分支持自动修复（🔧）或手动修复（💡）。
- ⚙️ **灵活设置**：支持自定义属性、函数、忽略键、缓存大小等共享设置，默认值通过 `DEFAULT_SETTINGS` 导出，并支持 TypeScript 类型安全配置。
- 🌟 **开源与赞助**：项目基于 MIT 许可证，鼓励开发者贡献，并接受 GitHub Sponsors 和 thanks.dev 赞助以维持维护。
- 🚀 **版本与兼容**：最新版本 v4.0.6（2026 年 7 月），支持 ESLint v10；旧版 Tailwind CSS v3 用户可使用 `eslint-plugin-tailwindcss@3.x.x`。

---

### [ui.sh](https://ui.sh/?ref=tailwindweekly.com)

**原文标题**: [ui.sh](https://ui.sh/?ref=tailwindweekly.com)

概述总结  
- 🎨 提供由资深设计师精心打造的任务导向提示与工作流，帮助构建不糟糕的UI界面  
- 🔧 基于Tailwind CSS和Refactoring UI团队的经验，专注于提升界面设计与开发效率  
- 💡 支持在浏览器中生成并对比多种设计方向，快速迭代创意  
- 🏷️ 可生成新产品视觉品牌方向，统一设计风格  
- 📦 将大型UI代码重构为可复用的组件，提升代码组织性  
- 🛠️ 提供Tailwind CSS类排序、规范化、去重及冲突解决功能  
- 🌙 实现深思熟虑的暗色模式，避免简单反转导致的视觉问题  
- 🖼️ 适配亮色模式图像至暗色模式，保持视觉效果  
- 📱 使现有设计适配移动端、平板及桌面断点，实现响应式  
- 📷 将截图、原型和线框图转换为语义化标记代码

---

### [Wispr Flow | 轻松语音听写](https://wisprflow.ai/?utm_source=dub.co&utm_medium=affiliate&utm_campaign=AffiliateProgram&via=vivian-guillen&dub_id=CkxGh4v4p7DXZVyh&ref=tailwindweekly.com)

**原文标题**: [Wispr Flow | Effortless Voice Dictation](https://wisprflow.ai/?utm_source=dub.co&utm_medium=affiliate&utm_campaign=AffiliateProgram&via=vivian-guillen&dub_id=CkxGh4v4p7DXZVyh&ref=tailwindweekly.com)

这是一款名为Flow的语音转文字AI工具，它能将语音快速转化为清晰、精炼的文字，适用于任何应用，比打字快4倍。

- 🎤 **告别打字，用说的**：Flow是一款语音转文字AI，能将语音瞬间转化为清晰、精炼的文字，适用于所有应用。
- 💻 **多平台支持**：可在Mac、Windows、iPhone和Android设备上使用，随时随地高效工作。
- ⚡ **速度提升4倍**：相比键盘打字（45词/分钟），Flow的语音输入速度可达220词/分钟，大幅提升效率。
- 🔧 **智能编辑与个性化**：自动去除语气词和错别字，支持个人词典（自动学习专属词汇）和快捷短语库（语音触发常用文本）。
- 🌐 **支持100+种语言**：自动检测并转录多种语言，无缝切换。
- 👥 **针对不同职业优化**：为团队、学生、开发者、创作者、销售、客服、律师、领导者及无障碍需求者提供定制化功能。
- 🔒 **安全合规**：所有计划符合HIPAA标准，企业计划符合SOC 2 Type II标准，保障数据安全。
- ❤️ **用户好评如潮**：被用户称为“改变游戏规则的产品”，尤其受到行动不便人士的青睐，极大简化了生活。

---

### [CSS 与 JavaScript • Josh W. Comeau](https://www.joshwcomeau.com/animation/css-vs-javascript/?ref=tailwindweekly.com)

**原文标题**: [CSS vs. JavaScript • Josh W. Comeau](https://www.joshwcomeau.com/animation/css-vs-javascript/?ref=tailwindweekly.com)

本文探讨了CSS与JavaScript动画的性能差异，并提供了选择合适工具的建议。

- 🎯 **核心发现**：CSS关键帧动画运行在独立线程，不受主线程阻塞影响；而基于`requestAnimationFrame`的JS动画会因主线程繁忙而卡顿。
- 🧩 **库的差异**：使用Web Animations API的库（如Motion）可绕过主线程限制，实现平滑动画；而GSAP等传统库仍受主线程影响，且可能不同步。
- ⏱️ **同步问题**：GSAP在帧延迟后不会自动追赶进度，导致动画不同步；而CSS和Motion能保持时间准确性。
- 📦 **加载成本**：JS动画库（如Motion 48kB、GSAP 27kB）需下载解析，但通常不影响用户体验，除非需要立即播放首屏动画。
- 🛠️ **工具选择建议**：优先使用原生CSS动画；复杂场景选择Motion等支持WAAPI的库；避免使用仅封装CSS功能的冗余库。
- 🌟 **现代CSS能力**：新API（如View Transitions、`linear()`、Animation Timeline）已能实现许多无需JS的复杂动画。

---

### [font-family 的回退方式与你想的不同 – CSS Wizardry](https://csswizardry.com/2026/04/font-family-doesnt-fall-back-the-way-you-think/?ref=tailwindweekly.com)

**原文标题**: [font-family Doesn’t Fall Back the Way You Think – CSS Wizardry](https://csswizardry.com/2026/04/font-family-doesnt-fall-back-the-way-you-think/?ref=tailwindweekly.com)

### 概述总结
本文揭示了CSS中`font-family`属性在回退机制上的常见误解，解释了为何仅指定单个字体值会导致意外回退到浏览器默认字体（如Times New Roman），并提供了通过始终声明完整字体栈来避免视觉闪烁和布局偏移的解决方案。

- 📝 **关键发现**：`font-family`回退机制是自包含的，子元素不会继承父元素的字体栈，而是仅基于自身声明进行回退。
- ⚠️ **问题现象**：仅指定单个自定义字体（如`"Open Sans"`）时，若字体未加载，浏览器会回退到默认的Times New Roman，导致视觉闪烁。
- 🔧 **修复方法**：每次声明`font-family`时，必须包含完整的字体栈，至少添加通用字体族（如`sans-serif`）作为后备。
- 📊 **影响范围**：不正确的字体回退不仅影响视觉一致性，还可能导致Core Web Vitals中的CLS（累积布局偏移）分数恶化。
- 💡 **最佳实践**：无论使用CSS变量还是直接声明，都应确保每个`font-family`值都包含完整的回退方案，避免依赖DOM继承。

---

### [position: sticky; 的怪异之处 – Master.dev 博客](https://frontendmasters.com/blog/the-weird-parts-of-position-sticky/?utm_source=CSS-Weekly&utm_medium=newsletter&utm_campaign=issue-626-november-5-2025&_bhlid=2d00372e4a8ea3e6fed561869d6bceca741c03d9)

**原文标题**: [The Weird Parts of position: sticky; – Master.dev Blog](https://frontendmasters.com/blog/the-weird-parts-of-position-sticky/?utm_source=CSS-Weekly&utm_medium=newsletter&utm_campaign=issue-626-november-5-2025&_bhlid=2d00372e4a8ea3e6fed561869d6bceca741c03d9)

概述摘要  
本文深入探讨了CSS `position: sticky` 的常见陷阱和调试方法，重点分析了粘性元素无法正常工作的两个主要原因：元素超出滚动容器尺寸和父容器约束过小，并提供了通过`align-self: flex-start`等对齐方式解决问题的具体方案。  

- 📌 **粘性定位基础**：`position: sticky` 结合 `top: 0` 等属性，可使元素在滚动时固定在指定位置，但需确保滚动容器正确设置。  
- ⚠️ **问题一：元素过大**：粘性元素不能大于滚动容器；否则滚动到底部时，元素会因浏览器强制显示全部内容而失去粘性。  
- 🔍 **问题二：父容器约束**：粘性元素不能“突破”其父容器边界；若父容器高度不足，浏览器会阻止粘性效果，直到父容器底部对齐才恢复。  
- 🛠️ **Flex/Grid子元素陷阱**：默认`align-self: stretch`会使子元素拉伸填满容器，导致粘性失效；改用`self-start`（即`align-self: flex-start`）可让元素按需生长，保留粘性空间。  
- 🧩 **实际案例**：在导航布局中，通过给网格容器和粘性元素添加`self-start`，并限制侧边栏高度（如`max-h`+`overflow-auto`），可同时实现粘性和可滚动性。  
- 💡 **调试关键**：理解CSS规范中“粘性元素必须包含在包含块内”的规则，是解决大多数粘性问题的核心。  
- 📝 **代码示例**：使用Tailwind和JSX展示，但核心原理适用于纯HTML/CSS；读者可忽略框架细节，专注逻辑。

---

### [Cozy — 本地优先的私人日记，始终属于你](https://cozyjournal.app/?utm_campaign=tailwind-weekly-221&utm_source=Tailwind+Weekly)

**原文标题**: [Cozy — The local-first private journal that stays yours](https://cozyjournal.app/?utm_campaign=tailwind-weekly-221&utm_source=Tailwind+Weekly)

该文本介绍了一个本地日记应用，强调数据完全存储在用户设备上，不依赖服务器，确保隐私和安全。以下是摘要：

📁 所有文件都存储在本地电脑上，无需担心服务器存储问题  
🔒 用户的思绪、经历和写作内容永久归用户所有，隐私有保障  
📝 示例日记条目包括与朋友喝咖啡、悠闲的一天、河边早晨、回到山区和与父母参加节日等主题  
🗂️ 日记以Markdown格式保存，文件名包含日期和标题，大小从1KB到3KB不等

---

### [BlatUI — 面向BLAT技术栈的shadcn/ui](https://blatui.remix-it.com/?ref=tailwindweekly.com)

**原文标题**: [BlatUI — shadcn/ui for the BLAT stack](https://blatui.remix-it.com/?ref=tailwindweekly.com)

### 概述摘要
BlatUI 是一个为 Laravel 开发者打造的 UI 组件库，基于 Blade、Alpine.js 和 Tailwind v4，提供 shadcn/ui 的完整体验。它强调可访问性、无运行时依赖和代码所有权，支持一键复制组件到项目，并包含丰富的模板、图表和主题定制功能。

- 🎨 **完整 UI 工具集**：提供 154 个组件、643 种变体、64 个区块、70 个图表和 34 个模板，覆盖从按钮到完整页面的所有需求。
- 🚀 **零运行时依赖**：无需 npm 或构建工具，组件通过 Artisan 命令直接复制为 Blade 文件，代码完全归你所有。
- ♿ **默认可访问**：所有组件遵循 WAI-ARIA 标准，支持键盘导航和 WCAG AA 对比度，并通过 axe-core 审计。
- 🌗 **主题与暗色模式**：基于 CSS 变量实现实时主题定制（颜色、圆角、字体、阴影），内置明暗模式切换并持久化。
- 🧩 **灵活集成**：与 Laravel、Livewire、Inertia 等框架无缝协作，支持 shadcn 注册表和 MCP 服务器，AI 工具也可直接安装组件。
- 📦 **一键安装与使用**：通过 `composer require anousss007/blatui` 安装，`php artisan blatui:init` 初始化，`php artisan blatui:add` 添加组件。
- 🖥️ **实时预览**：页面组件可实时响应主题定制，展示收入仪表盘、注册表单等实际交互效果。
- 📄 **丰富模板库**：提供 34 个艺术导向的页面模板，涵盖 SaaS、Web3、餐饮、音乐节等场景，风格从玻璃态到极简主义。
- 🔒 **MIT 开源许可**：免费永久使用，代码透明可编辑，无黑盒依赖。

---

### [PikaPods - 即时开源应用托管](https://www.pikapods.com/?utm_source=tailwind-weekly&utm_medium=newsletter&utm_campaign=first&ref=tailwindweekly.com)

**原文标题**: [PikaPods - Instant Open Source App Hosting](https://www.pikapods.com/?utm_source=tailwind-weekly&utm_medium=newsletter&utm_campaign=first&ref=tailwindweekly.com)

### 概述摘要
PikaPods提供开源应用托管服务，起价每月1.80美元，强调隐私、简单性和对开源开发者的支持。

- 🚀 **即时开源应用托管**：从每月1.80美元起，免费试用含5美元欢迎信用额度，无需系统管理技能。
- 🔒 **隐私优先**：无追踪、无广告、无数据窥探，支持欧盟和美国服务器位置，可使用自定义域名。
- 🛠️ **特色应用**：包括n8n（工作流自动化）、Immich（Google Photos替代品）、Actual（隐私财务管理）等。
- 💡 **为什么选择PikaPods**：数据隐私、简单界面、支持开源开发者（20%收入分成）、安全设计、无供应商锁定、透明定价。
- 🖥️ **一站式管理**：通过简单界面管理所有应用，调整资源或使用自定义域名。
- 💰 **灵活定价**：CPU、内存、存储可自定义，起价1.80美元/月，按使用付费。
- 🔄 **对比优势**：相比自建服务器或广告支持的云服务，PikaPods提供易用性、隐私、自动更新和备份支持。
- 🌐 **公司背景**：由Peakford Ltd运营，拥有超过十年托管经验，位于马耳他。

---

### [Mochi - 间隔重复闪卡](https://mochi.cards/?ref=tailwindweekly.com)

**原文标题**: [Mochi - Spaced repetition flashcards](https://mochi.cards/?ref=tailwindweekly.com)

概述总结  
Mochi是一款支持间隔重复学习的笔记与闪卡应用，提供高效复习、本地存储、Markdown编辑、语言学习及AI辅助功能，适用于多平台。  

- 📈 性能改进：1.21.17版本优化了性能，提升使用流畅度  
- 🔄 间隔重复：通过智能复习计划，帮助长期记忆更高效  
- 💾 本地优先：数据安全存储于设备，在线时自动同步  
- 📝 Markdown支持：用简洁语法格式化笔记，包含标题、列表、代码等  
- 🌍 语言学习：内置词典、翻译、文本转语音，支持词汇、语法和发音学习  
- 🔍 内置词典：无需离开笔记即可多语言即时查词  
- 🎧 文本转语音：卡片朗读功能，提升发音和听力练习  
- 🖼️ 图片搜索：为闪卡添加图像，增强视觉记忆  
- 🌐 自动翻译：卡片内容可翻译为目标语言或从目标语言翻译  
- 📚 笔记与学习：用Markdown记笔记，结合智能复习系统，将阅读转化为长期知识  
- 🔗 双向链接：笔记间相互关联，构建知识网络，发现新联系  
- 🏷️ 标签分类：灵活标签管理笔记，便于导航和整理  
- 🔍 筛选与视图：可自定义过滤器、保存视图和强大搜索，快速定位内容  
- 🤖 AI生成文本：利用最新AI模型创建例句或学习提示

---

### [首页 | 借助AI保持领先](https://newsletter.stayingahead.com/?ref=tailwindweekly.com)

**原文标题**: [Home | Staying Ahead with AI](https://newsletter.stayingahead.com/?ref=tailwindweekly.com)

以下是您提供的文本内容的概述和要点总结：

该页面是一个AI资讯平台，提供最新AI新闻、热门文章和订阅服务，涵盖从研究突破到工具更新的广泛主题。

- 🤖 OpenAI推出Sora：文本转视频AI的新纪元（2024年12月）
- 💔 AI布拉德·皮特85.5万美元爱情骗局引发社交媒体风暴（2025年1月）
- 🎥 YouTube推出创作者内容可选择参与AI训练的功能（2024年12月）
- 🚫 Meta删除Instagram/Facebook上的AI个人资料（2025年1月）
- 🔍 Google可能用AI取代“手气不错”按钮（2025年5月）
- 💰 从韩国电视节目角色到筹集1亿美元AI基金（2024年12月）
- 📧 订阅更新：每周获取AI前沿资讯，专为思考者、构建者和好奇者设计

---

### [GitHub - mnapoli/vibephp 位于 tailwindweekly.com · GitHub](https://github.com/mnapoli/vibephp?ref=tailwindweekly.com)

**原文标题**: [GitHub - mnapoli/vibephp at tailwindweekly.com · GitHub](https://github.com/mnapoli/vibephp?ref=tailwindweekly.com)

VibePHP 是一個創新的 PHP 執行環境，它不實際執行程式碼，而是透過 AI 來「理解」並「想像」程式碼的執行結果。

- 🤖 **AI 驅動的 PHP 引擎**：VibePHP 不使用傳統的直譯器或編譯器，而是將 PHP 原始碼交給 AI，讓 AI 在「腦中」執行並生成 HTTP 回應，所有缺失的資料（如資料庫、時間、網路請求）都由 AI 憑空創造。
- ⚡ **突破語言限制**：由於程式碼從不被實際編譯，VibePHP 能「支援」泛型、async/await，甚至內嵌 Go 或 Rust 語法，因為沒有任何約束能限制 AI 的想像力。
- 📊 **效能與成本**：相較於 nginx + PHP-FPM（延遲 ~1ms）和 FrankenPHP（延遲 ~1ms），VibePHP 的延遲約為 7 秒，每次請求成本約 $0.0063，但透過「勞動幻覺效應」可提升感知價值。
- 🚀 **快速開始**：只需在 `.env` 設定 `OPENAI_API_KEY`，在 `vibe/` 目錄建立 `index.php`，執行 `php artisan vibe`，即可在 `http://localhost:8000` 訪問網站。
- 🔧 **運作原理**：Laravel 路由將 URL 映射到 `vibe/` 目錄的檔案，原始碼與 HTTP 請求上下文被傳遞給 `VibePhpRuntime` AI 代理，AI 模擬執行流程，按需讀取包含檔案，並即興創造所有缺失資料，最後回傳 `{status, headers, body}`。
- 🌐 **示範功能**：包括首頁（5 篇虛構部落格文章）、關於頁面、文章頁面（從未存在的完整文章）、JSON API（想像的負載指標），每次重新整理都會產生不同內容。
- ☁️ **Vibe Cloud（即將推出）**：完全託管的無伺服器 VibePHP 託管服務，以「粒子」（1 粒子 = 1 MB 記憶體）計費，支援自動擴展、Heisenberg 企業級方案，以及「投機性預振動」功能來回收閒置 CPU 週期。

---

