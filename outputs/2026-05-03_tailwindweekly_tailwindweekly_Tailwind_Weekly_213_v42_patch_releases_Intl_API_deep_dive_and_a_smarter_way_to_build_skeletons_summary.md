### [发布 · tailwindlabs/tailwindcss · GitHub](https://github.com/tailwindlabs/tailwindcss/releases?ref=tailwindweekly.com)

**原文标题**: [Releases · tailwindlabs/tailwindcss · GitHub](https://github.com/tailwindlabs/tailwindcss/releases?ref=tailwindweekly.com)

Tailwind CSS 是一个流行的开源 CSS 框架，在 GitHub 上拥有 94.8k 星标和 5.2k 分支。以下是其最新版本 (v4.2.4) 及近期版本的发布摘要。

- 🚀 **最新版本 v4.2.4**：修复了在 `@tailwindcss/vite` 中使用 Vite 别名时，`@import` 和 `@plugin` 的导入解析问题。
- 🛠️ **v4.2.3 大量修复**：改进了 `tracking-*`、`border-*`、`scroll-m/p-*`、`overflow-*`、`overscroll-*` 等工具类的规范化；修复了无效字符导致的崩溃；支持 `NODE_PATH` 环境变量。
- ✨ **v4.2.2 新增与修复**：支持 Vite 8；修复了原型属性导致的崩溃；改进了 `calc()` 表达式和间距值的规范化；优化了 Vite 的热重载。
- 🐛 **v4.2.1 小版本修复**：允许功能工具类名末尾有破折号；正确检测 MDX 文件中花括号内的类。
- 🎉 **v4.2.0 重大更新**：新增了淡紫色、橄榄色、雾色和灰褐色等默认调色板；新增了 `@tailwindcss/webpack` 包；增加了大量逻辑属性工具类（如 `pbs-*`、`mbs-*`、`inline-*`、`block-*`、`inset-s-*` 等）；弃用了 `start-*` 和 `end-*` 工具类。
- 🔧 **v4.1.18 稳定性提升**：改进 CSS 解析错误提示；支持环境 API；正确生成源映射；增强与 JS 配置的向后兼容性。
- 📦 **v3.4.19 维护版本**：修复了 `calc()` 中 `sibling-*()` 函数的兼容性问题。

---

### [我们将您的设计转换为Tailwind CSS代码 | Design2Tailwind](https://design2tailwind.com/?ref=tailwindweekly.com#cta)

**原文标题**: [We convert your design to Tailwind CSS code | Design2Tailwind](https://design2tailwind.com/?ref=tailwindweekly.com#cta)

本頁介紹 Design2Tailwind 服務，由 Vivian 和 Daniela 姊妹團隊提供將設計稿轉換為 Tailwind CSS 的專業服務。

- 🎨 專注將 Figma、PSD、XD、Sketch 設計稿轉換為乾淨、可維護的 Tailwind CSS 代碼
- 👩‍💻 姊妹團隊擁有超過15年前端經驗，自2018年起每日使用 Tailwind CSS
- ✅ 提供6大優勢：極少自訂CSS、對代理商友好、快速可靠交付、易於交接、無框架鎖定、支援NDA
- 🔄 流程分5步驟：歡迎與分析、溝通對齊、編碼、展示與反饋、交付最終代碼
- 💰 價格從第一頁$350起，額外頁面每頁$120，依設計複雜度調整
- 🛠️ 支援多種工具：Figma、Adobe XD、Sketch、Photoshop，以及 React、Vue、Alpine.js、Astro 等框架
- 🌐 支援最新版 Chrome、Safari、Firefox、Edge 瀏覽器，並進行跨瀏覽器測試
- 📝 提供3輪修訂，小錯誤免費修正，重大變更另行計費
- ⭐ 客戶好評如潮，已交付超過100個專案，專注於乾淨、可重複使用的前端代碼

---

### [Intl API：你尚未使用的最佳浏览器API | Polypane](https://polypane.app/blog/the-intl-api-the-best-browser-api-youre-not-using/?ref=tailwindweekly.com)

**原文标题**: [The Intl API: The best browser API you're not using | Polypane](https://polypane.app/blog/the-intl-api-the-best-browser-api-youre-not-using/?ref=tailwindweekly.com)

### 概述摘要
Intl API 是浏览器内置的国际化格式化工具，无需额外库即可处理日期、数字、货币、列表等本地化格式，支持零依赖且性能优异。

- 📅 **日期与时间**：`Intl.DateTimeFormat` 可自动适配用户区域设置，支持 `dateStyle`/`timeStyle` 快速格式化，并提供 `formatToParts()` 方法拆分输出组件。
- ⏳ **相对时间**：`Intl.RelativeTimeFormat` 生成“昨天”“3天后”等人类可读表述，需手动计算时间差后传入。
- ⏱️ **持续时间**：`Intl.DurationFormat` 将时长对象转为“2小时5分钟30秒”或 `2:05:30` 格式，支持 `digital` 样式。
- 💰 **数字与货币**：`Intl.NumberFormat` 处理千分位、百分比、科学记数法，货币格式化自动调整符号位置与分组规则，支持 `unit` 单位（如 km/h）。
- 📋 **列表与复数**：`Intl.ListFormat` 生成自然语言列表（含牛津逗号），`Intl.PluralRules` 识别语言复数规则（如“one”/“other”），用于动态词形变化。
- ✂️ **文本分割**：`Intl.Segmenter` 按字素、单词或句子分割文本，正确处理emoji（如👨‍👩‍👧‍👦长度=1）和日语无空格语言。
- 🔤 **排序与比较**：`Intl.Collator` 实现区域感知排序（如西班牙语中 ñ 排在 n 后），支持数字排序（`numeric: true` 避免“10”排在“2”前）。
- ⚡ **性能优势**：零KB依赖，原生实现比第三方库快，建议复用格式化器实例以优化性能。

---

### [SVG滤镜指南：基础入门 – 前端大师博客](https://frontendmasters.com/blog/svg-filters-guide-getting-started-with-the-basics/?ref=tailwindweekly.com)

**原文标题**: [SVG Filters Guide: Getting Started with the Basics – Frontend Masters Blog](https://frontendmasters.com/blog/svg-filters-guide-getting-started-with-the-basics/?ref=tailwindweekly.com)

本指南介绍了SVG滤镜的基础知识，包括如何设置、使用和注意事项，适合初学者入门。

- 🎨 **SVG滤镜需放在`<svg>`元素内**：若仅用于定义滤镜，应将其尺寸设为0、隐藏屏幕阅读器并脱离文档流（如`position: fixed`），避免影响布局。
- 🆔 **滤镜元素必须设置`id`属性**：通过CSS的`filter: url(#id)`引用，可与其他CSS滤镜（如`blur()`）链式使用。
- 🌈 **设置`color-interpolation-filters="sRGB"`**：在操作RGB通道的滤镜中显式设置，确保跨浏览器（如Safari、Chrome、Firefox）结果一致。
- 📏 **调整滤镜区域（`x`、`y`、`width`、`height`）**：默认区域为输入元素边界框的120%（从-10%到110%），可扩展（避免裁剪效果如模糊）或缩小（限制效果如噪点）。
- 🔧 **滤镜原语（`fe`前缀元素）按顺序处理**：默认输入为上一原语输出或`SourceGraphic`，输出可命名（`result`属性）供后续引用，无需为每个原语设置属性。
- 📐 **区分`filterUnits`和`primitiveUnits`**：前者控制滤镜区域单位（默认`objectBoundingBox`），后者控制原语长度单位（默认`userSpaceOnUse`，即绝对像素），可改为`objectBoundingBox`实现相对值。
- ⚠️ **常见限制**：长度值仅支持相对边界框或绝对像素，无法相对`font-size`，需通过链式滤镜或变通方法解决。

---

### [获取失败](https://css-tricks.com/4-reasons-that-make-tailwind-great-for-building-layouts/?ref=tailwindweekly.com)

**原文标题**: [Failed to retrieve](https://css-tricks.com/4-reasons-that-make-tailwind-great-for-building-layouts/?ref=tailwindweekly.com)

无法总结：获取内容失败，状态码 415。

---

### [史密森尼美国艺术博物馆与伦威克画廊](https://americanart.si.edu/?ref=tailwindweekly.com)

**原文标题**: [Smithsonian American Art Museum and Renwick Gallery](https://americanart.si.edu/?ref=tailwindweekly.com)

史密森尼美国艺术博物馆与伦威克画廊当前展览与活动概览
- 🦣 尼克·凯夫：《猛犸象》展览至2027年1月3日，邀请观众漫步于这些远古生物的超现实遗骸之间。
- 🖼️ 摩西奶奶：《充实的一天》展览至2026年7月12日，重新诠释这位艺术家备受喜爱的作品。
- 🎪 州博览会：培育美国工艺展至2026年9月7日，首次聚焦艺术家对美国州博览会传统的贡献。
- 🎷 爵士之夜：2026年5月21日与6月18日，分别由克拉拉·坎贝尔和保罗·贝利演出，免费但需注册。
- 🤟 手语艺术导览：2026年6月11日，提供美国手语的艺术对话，免费但需注册。
- 🏛️ 新馆长任命：琳达·罗斯科·哈蒂根于2026年9月8日被任命为博物馆馆长。
- 🌽 贾斯汀·法维拉奇幻展：以金边墙壁和皮纳塔玉米棒装饰伦威克画廊，突出玉米在北美视觉文化中的角色。
- 🎨 新收购作品：包括亚伦·道格拉斯的《灵感》（1967年）、塞西莉亚·维库尼亚的《奎普内脏》（2017/2025年）等。
- 📹 精选视频：艺术家沙赫齐娅·西坎德和贾斯汀·法维拉的创作访谈，以及摩西奶奶的介绍。

---

### [骨场 - 用户界面的骨架屏](https://boneyard.vercel.app/overview?ref=tailwindweekly.com)

**原文标题**: [boneyard - skeleton screens for your UI](https://boneyard.vercel.app/overview?ref=tailwindweekly.com)

### 概述总结
Boneyard 是一个自动生成骨架屏的工具，通过快照真实 UI 生成精确的骨骼数据，无需手动测量或调整占位符。

- 🦴 **自动生成骨骼**：通过快照真实 UI，自动捕获位置和尺寸精确的矩形骨骼，无需手动测量。
- 📦 **简单集成**：使用 `npm install boneyard-js` 安装，通过 `<Skeleton>` 组件包裹即可实现像素级骨架屏。
- ⚡ **CLI 一键构建**：运行 `npx boneyard-js build` 自动检测开发服务器和 Tailwind 断点，生成响应式 JSON 骨骼文件。
- 🔄 **实时同步**：骨骼数据基于真实渲染内容生成，运行一次 CLI 后，所有 `<Skeleton>` 自动解析，无布局偏移。
- 🚀 **生产级优化**：运行时仅 ~7.5KB，骨骼数据以紧凑数组格式存储，支持增量构建，仅重新捕获修改的组件。
- 📊 **项目数据**：下载量 18.2k，星标 4,521，骨骼数 1.2M，版本 v1.7.3。

---

### [WindyBase - 探索免费与高级的Tailwind CSS模板](https://windybase.com/?ref=tailwindweekly.com)

**原文标题**: [WindyBase - Explore free and premium Tailwind CSS templates ](https://windybase.com/?ref=tailwindweekly.com)

WindyBase 是一个每周精选的 Tailwind CSS 模板和工具目录，旨在帮助开发者快速构建现代网站和应用。

- 🌐 提供丰富的 Tailwind CSS 模板和组件库，包括着陆页、SaaS、博客、仪表盘和电商模板。
- 💰 资源涵盖免费和付费选项，价格从免费到 $249 不等，满足不同预算需求。
- 🔍 支持搜索功能，方便开发者快速找到所需模板或组件。
- 📧 提供新闻订阅服务，用户可获取最新模板和组件更新通知。
- 🛠️ 包含组件库如 HyperUI、Mamba UI 和 Preline UI，部分免费，部分需付费。
- 📄 网站设有法律条款，包括隐私政策和服务条款，保护用户权益。
- 🐦 通过 Twitter/X 和 Bluesky 等社交媒体保持社区互动。

---

### [GitHub - faiscadev/fakecloud 在 tailwindweekly.com · GitHub](https://github.com/faiscadev/fakecloud?ref=tailwindweekly.com)

**原文标题**: [GitHub - faiscadev/fakecloud at tailwindweekly.com · GitHub](https://github.com/faiscadev/fakecloud?ref=tailwindweekly.com)

fakecloud 是一个免费、开源的本地 AWS 模拟器，专为集成测试和本地开发设计。它作为 LocalStack 的替代品，无需账户或认证令牌，提供单二进制文件、快速启动和广泛的 AWS 服务支持。

- 🆓 **完全免费开源**：采用 AGPL-3.0 许可，无付费层级，无需账户或令牌。
- ⚡ **轻量高效**：单二进制文件约 19 MB，空闲内存约 10 MiB，启动时间约 500 毫秒。
- ✅ **100% 服务一致性**：每个实现的服务都经过 AWS Smithy 模型验证，每次提交运行超过 59,000 个测试变体。
- 🔗 **真实跨服务集成**：支持 EventBridge、Step Functions、S3、Lambda 等 15 种以上端到端集成。
- 🐳 **真实基础设施**：Lambda 在 Docker 容器中运行（23 种运行时），RDS 运行真实数据库，ElastiCache 运行真实缓存。
- 🛠️ **广泛服务支持**：涵盖 33 个服务、2,422 个操作，包括 S3、SQS、SNS、Lambda、DynamoDB、Bedrock 等。
- 🔒 **可选安全功能**：支持 SigV4 验证和 IAM 强制策略，包括条件块和跨账户语义。
- 📚 **第一方测试 SDK**：提供 TypeScript、Python、Go、PHP、Java 和 Rust 的 SDK，便于断言测试结果。
- 🤖 **AI 工具集成**：提供针对 Claude Code、Cursor 和 GitHub Copilot 的配置片段。
- 📖 **丰富文档**：网站、入门指南、参考文档和博客，帮助用户快速上手。

---

### [PanicLock - Mac 紧急锁定按钮](https://paniclock.github.io/?ref=tailwindweekly.com)

**原文标题**: [PanicLock - Panic Button for Your Mac](https://paniclock.github.io/?ref=tailwindweekly.com)

## 概述总结
PanicLock 是一款为Mac用户设计的紧急安全工具，在保留Touch ID日常便利性的同时，提供一键禁用生物识别并锁定屏幕的功能。该工具针对法律风险（如执法机构强制生物识别解锁）和边境检查等场景，通过密码保护恢复设备访问的主动权。

- 🚨 **核心功能**：一键禁用Touch ID并锁定屏幕，支持自定义快捷键和合盖锁定，操作快速（1秒内完成）
- ⚖️ **法律背景**：美国第九巡回法院（2024年）认为强制指纹解锁不违反第五修正案，而华盛顿特区巡回法院（2025年）持相反观点，形成法律分歧
- 🛂 **边境风险**：在美国入境口岸，CBP可无需 warrant 搜索设备，启用生物识别可能使设备在无密码情况下被解锁
- 🌍 **国际差异**：部分国家法律强制要求披露密码，但生物识别可能完全剥夺用户的选择权
- 🎯 **目标用户**：旅行者、记者、律师、活动人士等需要保护敏感数据或客户机密的人群
- 🔓 **开源优势**：PanicLock 是开源软件，提供透明度和可审计性，可免费下载使用

---

### [端口菜单 — localhost，已整理](https://www.portmenu.dev/?ref=tailwindweekly.com)

**原文标题**: [Port Menu — localhost, organized](https://www.portmenu.dev/?ref=tailwindweekly.com)

macOS菜单栏应用Port Menu，用于集中管理开发服务器，支持跨项目追踪和快速访问。

- 🖥️ 应用概述：Port Menu是一款macOS菜单栏应用，帮助开发者集中管理本地开发服务器。
- 📂 跨项目追踪：该应用能够追踪不同项目中的开发服务器，方便开发者快速切换。
- ⏱️ 实时状态：显示每个服务器的运行状态、端口号和运行时长（如“2m”、“14m”）。
- ⬇️ 下载与支持：提供macOS下载链接，并托管在GitHub上供用户星标和获取支持。
- ©️ 版权信息：应用由Eduard Wieandt开发，版权至2026年。

---

