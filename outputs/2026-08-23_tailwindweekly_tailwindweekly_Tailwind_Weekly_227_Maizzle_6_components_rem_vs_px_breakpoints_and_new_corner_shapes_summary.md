### [](https://github.com/francoismassart/eslint-plugin-tailwindcss/releases?ref=tailwindweekly.com)

**原文标题**: [Releases · francoismassart/eslint-plugin-tailwindcss · GitHub](https://github.com/francoismassart/eslint-plugin-tailwindcss/releases?ref=tailwindweekly.com)

eslint-plugin-tailwindcss 是一个用于 Tailwind CSS 的 ESLint 插件，页面展示了其从 v4.0.0-alpha 到 v4.4.0 的发布记录，重点包括性能提升、新规则、Svelte 支持增强以及对 Tailwind CSS v4 的全面适配。

- 🚀 v4.4.0：大幅提升 lint 速度，新增 `enforces-canonical-classname` 规则（需 Tailwind v4.3.0+），并修复 `import.meta.url` 路径与 TypeScript `satisfies` 支持。
- 🌈 v4.3.0：增强 Svelte 项目支持，可处理 `class` 字符串、`class:lg:block` 指令、对象及数组绑定语法。
- ⚠️ v4.2.0：新增 `important-modifier-suffix` 规则，要求 `!` 修饰符置于类名末尾，兼容旧写法弃用。
- 🔍 v4.1.0：扩展 `no-unnecessary-arbitrary-value` 规则，可解析单位换算与间距配置，自动替换冗余任意值。
- 🐞 v4.0.6：修复 `no-contradicting-classname` 对 `border` 和 `divide` 的误报问题。
- 🐛 v4.0.5：补齐缺失的 `eslint` 作为 peer dependency，并修复 `enforces-shorthand` 在带前缀时失效的问题。
- 🔧 v4.0.4：默认设置中加入 shadcn/ui 的 `cn` 函数，并将 `peer` 及 `peer/...` 视为有效类名。
- 🎉 v4.0.3（Tailwind CSS v4）：完全用 TypeScript 重写，基于 Tailwind 内部资源（`prettier-plugin-tailwindcss` 和 `tailwind-api-utils`），仅兼容 Tailwind v4、ESLint flat config 与 Node >=20.19.0。
- ⚡ v4.0.0-alpha.5：实现缓存和多项性能增强，涵盖多个核心规则。
- 🔰 v4.0.0-alpha.3：预发布版本，加入 `no-contradicting-classname`、`enforces-shorthand` 等规则及亮点改进。

---

### [](https://todowing.com/?ref=tailwindweekly.com)

**原文标题**: [Todowing — Nested Sub-tasks & More for Todoist](https://todowing.com/?ref=tailwindweekly.com)

Todowing 是一款 Chrome 扩展，用于增强 Todoist 网页版体验。它恢复了 Todoist 在日期和筛选视图中被压平的子任务层级，并额外提供专注计时器、字体替换、文本大小调节等功能。该扩展采取免费基础层加一次性付费解锁的模式，强调无订阅、隐私友好，并持续加入新功能。

- 🧩 在“今天”、“即将到来”、筛选器、标签和看板视图中，将子任务以内联方式嵌套显示于父任务下，最多支持四级层级
- ✅ 可直接在列表中勾选或重新打开子任务，无需进入任务详情；折叠父任务的状态还能跨刷新保持
- 🔁 合并已完成子任务以显示进度，并在重复任务重新开始时自动重置子任务清单，让每次循环从全新清单开始
- ⏱️ 专注计时器：从“今天”列表挑选任务并启动倒计时，卡片显示在侧边，并跨所有打开的标签页保持运行
- 🔤 支持浏览并选用 50 种 Google 字体，让整个 Todoist 界面（包括新增的子任务行）重新换肤
- 📏 文本大小可在 85% 到 200% 之间以 5% 步进自由缩放，标题、任务、描述和子任务行同步调整
- 🆓 免费版包含所有嵌套功能并限每项主任务 5 行子任务，另有文本大小滑块，且无需注册账号
- 💎 一次性支付 $9.99 即可终身解锁：无限子任务行、隐藏已完成开关、专注会话、字体选择器，以及所有未来付费功能
- 🚫 无订阅、无续费邮件；支持 14 天无理由退款，价格从 $14.99 限时折扣，目前已售 13/25 份
- 🔐 隐私设计：Todoist API token 只保存在浏览器中，数据仅发送至官方 Todoist API，任务不经过其服务器，也无任何分析或追踪
- 👤 由 Todoist 日常重度用户 Vivian Guillen 开发，最初是自用的 userscript，后重建成正式扩展
- ✅ 适用于任何 Todoist 套餐（无需 Pro），在 Chrome 中的 Todoist 网页应用即可运行；若验证服务器宕机，已解锁状态不受影响（仅明确“撤销”才会锁定）

---

### [](https://windybase.com/?ref=tailwindweekly.com)

**原文标题**: [WindyBase - Explore free and premium Tailwind CSS templates ](https://windybase.com/?ref=tailwindweekly.com)

overview summary  
WindyBase 是一个每周精心整理的 Tailwind CSS 模板与工具目录，面向现代开发者，提供免费及付费的模板、组件库和资源，涵盖落地页、SaaS、博客、仪表盘、电商等多种类别，并支持订阅更新。

- 🧭 网站定位：WindyBase 是专为开发者打造的 Tailwind CSS 模板与工具导航站，每周更新。
- 🎯 核心功能：提供免费与付费的 Tailwind 模板、组件库及开发资源，帮助用户快速构建现代网站和应用。
- 📄 模板分类：包括落地页、SaaS、博客、仪表盘、电商等主要类别，每类均展示多款精选产品。
- 💰 价格差异：模板价格从免费到 $249 不等，例如 Horizon、Landing Pad、K-WD Dashboard 等为免费，Voyager、Nova、Preline Pro 等为付费。
- 🧩 组件库：收录 Mamba UI、HyperUI、Preline UI 等免费/付费组件库，满足不同开发需求。
- 🔍 探索体验：支持搜索、实时预览和直接购买，方便开发者快速筛选并试用。
- 📬 邮件订阅：提供新闻通讯订阅，用户可第一时间获取新模板和组件更新通知。
- 🔗 站内导航：包含分类浏览、提交项目、联系及法律条款等常规入口，整体结构清晰。

---

### [Baselair - 微缩模型画家的最佳社区](https://thebaselair.com/?ref=tailwindweekly.com)

**原文标题**: [Baselair - The best community for miniature painters](https://thebaselair.com/?ref=tailwindweekly.com)

该内容是一个微缩模型涂装分享平台的动态列表，展示了大量由不同创作者提交的涂装作品，涵盖奇幻、科幻、恐怖等多样题材，每项附有点赞与评论数；目前所有创作者个人页均显示“暂无项目”。

- 🎨 收录众多微缩模型涂装作品，如 Hobgrot Hangover、Chaos Warrior、Gold Dragon 等
- ⚔️ 包含战锤/科幻题材：Warhammer 40k Company Heroes、Leman Russ、Dark Angels Terminator Captain 等
- 🐉 奇幻与传说生物丰富：Cave Troll、Hill Giant、Dragon King、Tomb Kings Bone Dragon 等
- 🧝‍♀️ 原创角色与英雄众多：Arianna Fairy Princess、Elven Warrior Princess、Dwarf Witcher 等
- 💀 恐怖/暗黑风格作品：Nyarlathotep、Lost in the Dark、Trench Prophet、The Wolfman 等
- 👥 每件作品均由不同创作者发布，并附点赞与评论数，部分作品互动量较高
- 📭 所有创作者个人页均显示“No projects just yet”，暂无更多项目详情

---

### [让您的小企业拥有强大的线上形象。• FLX Websites](https://flxwebsites.com/?ref=tailwindweekly.com)

**原文标题**: [Give your small business a big online presence. • FLX Websites](https://flxwebsites.com/?ref=tailwindweekly.com)

FLX Websites 是一家专为本地小企业打造定制网站与数字营销的团队，强调快速建站、个性化设计、搜索优化及持续支持，已获得多家小企业客户好评。

- 🌐 为小企业打造强大的线上形象，由专业网页与营销团队全程负责。
- 🎨 不套用模板，提供量身定制的网站设计，让企业形象独一无二。
- ✅ 已获得超过74家本地小企业的信赖。
- 📖 案例研究展示成果：沉浸式视觉、定制图形与预约系统集成。
- 🍷 优化用户体验，提升酒类、美食等主题的浏览与选择体验。
- 🔄 重新设计页面并简化导航，帮助用户快速找到所需服务。
- ⭐ 客户称赞执行力强，网站上线迅速，且服务响应及时。
- 🗣️ 客户表示经常向同事推荐，合作体验远超预期。
- 🔍 同时针对传统搜索引擎和AI优化，让顾客更快、更早找到你。
- 📊 提供策略性营销支持，实时监控流量、转化等关键数据。
- 🛠️ 提供24/7支持，包括维护、升级、安全防护，且改动不额外收费。
- 📍 联系或到访：位于 Canandaigua，156 Mill Street, NY 14424。

---

### [](https://spatie.be/blog/can-we-make-default-tailwind-a-more-accessible-choice?ref=tailwindweekly.com)

**原文标题**: [Can we make default tailwind a more accessible choice? | Spatie](https://spatie.be/blog/can-we-make-default-tailwind-a-more-accessible-choice?ref=tailwindweekly.com)

本文探讨了 Tailwind CSS 默认使用 rem 作为断点单位所带来的可访问性影响：断点会随浏览器默认字体大小变化，但不受作者 CSS 设置影响。文章通过实际案例解释了这一机制、利弊权衡，以及如何切换为 px 断点，并强调关键是清楚自己在为哪类用户做取舍。

- 🐛 问题起因：用户调大浏览器默认字体后，作者无法复现布局错乱，最终发现是 Tailwind 的 rem 断点随默认字体缩放，导致断点触发位置偏离预期。
- 📏 默认断点：Tailwind v3.2 起默认断点使用 rem，如 `md` 实际是 `min-width: 48rem`，注释像素值按 16px 换算。
- 🔍 关键机制：媒体查询中的 rem/em 基于“初始值”，作者在 `html { font-size: 10px }` 中设置无效，但浏览器默认字体大小设置会改变这个初始值。
- 📊 行为对比：浏览器默认字体大小会同时缩放 rem 文本和 rem/em 断点，px 断点不变；页面缩放影响所有单位；作者设置 html 字体大小只影响文本，不影响断点。
- ✅ 支持 rem 的理由：用户调大默认字体时，断点跟随移动，给更大文字提供更宽松的布局，这是重要的可访问性优势。
- ⚠️ 潜在风险：若只在 16px 下测试，用户使用更大默认字体时，断点可能在更窄视口触发，导致卡片溢出、组件库内部布局翻转，且问题难以复现。
- ⚖️ 争论点：px 断点提供完全可预测的布局，依赖页面缩放置入可访问性；rem 断点额外尊重默认字体设置，是超出 WCAG 1.4.4 要求的主动选择，而非合规必需。
- 🔧 修改方案：Tailwind v4 中通过 `@theme` 覆盖 `--breakpoint-*` 为 px；v3 在 `theme.screens` 中配置 px 值。
- 💡 核心结论：没有绝对正确的答案，关键在于是否意识到默认断点单位的取舍，并有意识地选择能匹配目标用户需求的方案。

---

### [获取失败](https://www.youtube.com/watch?v=x6YBZ4w7Ueg&ref=tailwindweekly.com)

**原文标题**: [Failed to retrieve](https://www.youtube.com/watch?v=x6YBZ4w7Ueg&ref=tailwindweekly.com)

无法总结：获取内容失败，状态码 429。

---

### [获取失败](https://www.youtube.com/watch?v=oKcrTBjmOio&ref=tailwindweekly.com)

**原文标题**: [Failed to retrieve](https://www.youtube.com/watch?v=oKcrTBjmOio&ref=tailwindweekly.com)

无法总结：获取内容失败，状态码 429。

---

### [标准代码 | 永远在线。无限使用。统一价格。](https://standardcode.ai/?ref=tailwindweekly.com)

**原文标题**: [Standard Code | Always online. Unlimited usage. One flat price.](https://standardcode.ai/?ref=tailwindweekly.com)

Standard Code 是一款云端编码代理，以“线路”为计费单位提供无限使用，并通过多代理协作架构实现自动化编码。以下是其核心要点：

- 💻 云端编码代理：Standard Code 是一个运行在云端的编码代理，支持无限使用，按“线路”计费，每条线路同一时间可运行一个活跃会话。
- 💰 定价模式：首周仅需 $5，之后每月 $49/线路，可按需添加额外线路以支持并行会话，无 token 配额限制。
- ♾️ 无限使用原理：通过“线路计费”模型和精心设计的“代理架构”实现，使用量受时间（线性）而非 token 数量约束。
- 🧠 子代理团队：内置预配置的领域专用子代理（如代码探索、研究、压缩、资产生成等），自动按需调用，且不占用活跃线路。
- 🚀 两种代理选择：Unlimited One（默认，基于开放权重模型）和 Sama One（基于 OpenAI 模型，需 ChatGPT Pro 订阅，使用 Codex 配额，不占线路但需至少一条活跃线路）。
- 📱 全平台客户端：提供 CLI、API、Web、macOS 和 iOS 客户端，所有客户端连接到同一云会话，线程历史、草稿和消息实时同步。
- 🔄 始终在线：会话状态保存在云端，即使客户端断开，代理仍可在服务器上继续运行，支持随时恢复。
- 📡 完整 API：提供 REST 和 WebSocket 接口，支持从代码、CI/CD、仪表盘或自有产品灵活驱动和监控会话。
- 🎯 自动化任务：代理可将大型目标拆解为多个步骤，逐项执行并验证；子代理上下文隔离，压缩过程不阻塞任务进行。
- 🛡️ 扩展与安全：支持 Agent Skills 和 MCP 集成，模型故障自动切换，权限门控和远程审批功能保护环境安全。
- 🏢 企业方案：提供组织统一计费（按人头 $49/月）或全栈自托管许可证，可部署在自有基础设施上。

---

### [](https://github.com/anburocky3/tailwind-suggest-plugins?ref=tailwindweekly.com)

**原文标题**: [GitHub - anburocky3/tailwind-suggest-plugins at tailwindweekly.com · GitHub](https://github.com/anburocky3/tailwind-suggest-plugins?ref=tailwindweekly.com)

该仓库是一个基于 Bun workspaces 的 monorepo，提供 ESLint 和 Prettier 插件，利用 Tailwind 内部语言服务自动将非规范类转换为规范等价物（例如 `w-[100px]` → `w-25`），并解决了与 `prettier-plugin-tailwindcss` 的冲突问题。

- 📦 包含三个包：`eslint-plugin-tailwind-suggestions`（实时编辑器警告与自动修复）、`prettier-plugin-tailwind-suggestions`（保存时格式化并转换）、`tailwind-suggest-core`（共享核心引擎）
- 🔍 与基于正则的工具不同，它使用 Tailwind 内部语言服务准确解析任意值、自定义主题令牌和规范类等价物
- ⚠️ Prettier 存在架构限制（Issue #12807），无法合并多个插件，且 `prettier-plugin-tailwindcss` 会覆盖自定义解析器
- 🛠️ 解决方案：采用两步格式化——先配置 `.prettierrc` 仅包含官方排序插件用于编辑器保存，再通过 npm 脚本顺序运行两次 Prettier（先运行 suggestions 插件转换任意值，再运行官方插件排序）
- ⏳ 权衡：编辑器保存时仅执行 `.prettierrc` 中的格式化，重复运行会增加毫秒级时间；推荐提交前运行 `npm run format` 完成完整转换
- 🧩 支持框架：React / Next.js (JSX/TSX)、Vue、Angular、标准 HTML
- 📌 发布命令：`bun run release patch|minor|major`
- 👤 由 Anbuselvan Annamalai 创建，采用 MIT 许可证

---

### [](https://botdirectory.ai/?ref=tailwindweekly.com)

**原文标题**: [Grok Bot Prompts & AI Bot Directory | botdirectory.ai](https://botdirectory.ai/?ref=tailwindweekly.com)

overview summary  
这是一个 AI 代理（Bot）提示词目录，汇集了 200+ 个可直接复制的机器人设定，涵盖销售、营销、运营、成功、个人与生产力等类别，并列出所需集成工具与贡献者。用户可浏览、筛选、复制提示词，或通过 PR 与 @botdirectoryai 方式贡献新机器人，同时页面也包含多个赞助商推广。

- 🤖 收录 200+ 个现成 Bot 提示词，覆盖销售、营销、运营、客户成功、个人生活与生产力等场景  
- 🔌 每个 Bot 均标注所需集成（如 Gmail、Slack、Salesforce、Notion、YouTube 等），方便直接连接  
- 📁 提供分类与筛选功能，支持按类别、集成、添加时间及字母顺序浏览，并可切换表格/卡片视图  
- 🧩 代表示例包括客户成功、广告创意、社媒发布、房产分析、邮件清理、旅行规划、支持工单等自动化方案  
- ✍️ 贡献机制简单：通过 GitHub PR 提交一个 markdown 文件，或在 X 上标记 @botdirectoryai 自动添加  
- 🔍 提供公开 JSON API，便于开发者搜索、过滤与分页获取全部目录数据  
- 💡 页面附带多项赞助商服务，如 AI 合规、社媒排程、销售线索挖掘、截图 API 等，推广位有限  
- ⚙️ 每个提示词通常包含配置引导、运行方式、审批边界与保存流程，强调人工确认与安全操作  
- 📈 整体定位为“复制提示词、连接工具、立即使用”的 AI 代理应用商店式平台

---

### [](https://pi.dev/?ref=tailwindweekly.com)

**原文标题**: [Pi Coding Agent](https://pi.dev/?ref=tailwindweekly.com)

overview summary  
- 🐛 此内容涉及使用GitHub Issues来报告软件缺陷（bug）  
- ✨ 同时支持通过GitHub Issues提交新功能（features）请求  
- 🔗 鼓励用户前往GitHub平台进行问题反馈与功能建议

---

### [](https://flipper.net/?ref=tailwindweekly.com)

**原文标题**: [
  Flipper Zero — Portable Multi-tool Device for Geeks
](https://flipper.net/?ref=tailwindweekly.com)

overview summary
- 🐬 Flipper Zero 是一款面向渗透测试者和极客的便携式多工具设备，外形似玩具，支持无线电、门禁系统及硬件破解，完全开源可定制。
- 📻 内置 Sub-1 GHz 收发器（CC1101），可读取和模拟遥控器、车库门、IoT 传感器等，最远距离达 50 米。
- 💳 支持 125 kHz RFID 低频卡读取、克隆与模拟，并可远程分享卡片 ID。
- 📱 支持 NFC 高频卡（13.56 MHz），可读写和模拟 MIFARE、FeliCa 等标准卡。
- 🔴 配备红外收发器，可控制电视、空调等设备，并支持学习现有遥控器信号并存入库中。
- 🎮 通过 5 键方向键和 LCD 屏幕实现完全自主操作，无需连接电脑或手机。
- 🧰 提供 GPIO 引脚，可用于 UART、SPI、I2C 调试、固件烧录及硬件探测，甚至作为 USB 转换器。
- 🔑 内置 iButton 1-Wire 读取器，可读取、写入和模拟 Dallas 等接触式钥匙。
- 🛠️ 配备 microSD 卡槽，支持 FAT12/exFAT 等格式，用于存储数据和应用。
- 📶 支持蓝牙低功耗（BLE 5.4），可通过 iOS/Android 应用远程控制与更新设备。
- 🔋 搭载 2100 mAh 锂电池，续航最长 28 天，并配备震动马达和蜂鸣器。

---

