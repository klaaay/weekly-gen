### [React 文摘：电子邮件简报](https://reactdigest.net/)

**原文标题**: [React Digest: Email Newsletter](https://reactdigest.net/)

React Digest 是面向 React 开发者的精选周刊，每周发送一封邮件，提供人工挑选并附有简短摘要的文章，帮助读者节省筛选内容的时间并持续学习。

- ⚛️ 面向 React 开发者的精心策划周刊，每周更新一次。
- 📧 已有超过 22,166 名前端软件工程师加入订阅。
- 📝 每期精选文章并附简短摘要，方便快速阅读。
- ⏳ 帮助读者节省寻找优质内容的时间。
- 📚 每周都能学习新知识，紧跟 React 生态发展。
- 💬 读者评价积极，认可文章质量及内容的实用性。
- 👩‍💻 受众为前端工程师，内容聚焦 React 相关主题。
- ©️ 网站信息显示版权归 Bonobo Press 所有（2013-2026）。

---

### [JPEG XL 与 AVIF 在 Web 使用场景中的对比 - JakeArchibald.com](https://jakearchibald.com/2026/jpeg-xl-vs-avif/)

**原文标题**: [JPEG XL vs AVIF for web use-cases - JakeArchibald.com](https://jakearchibald.com/2026/jpeg-xl-vs-avif/)

JPEG XL 已进入主流浏览器，文章通过多张图片、多个编码器和浏览器基准测试，比较 JPEG XL（libjxl 与 jixel）和 AVIF 在网页常见场景中的文件大小、画质、编码/解码速度与内存占用。总体结论是：对大多数有损照片和网页场景，AVIF 4:4:4 更稳妥；JPEG XL 在无损、JPEG 转码和部分异常图片上有优势，jixel 的出现让竞争更激烈，但最终仍应用自己的图片实测。

- 📷 有损照片通常 AVIF 文件更小：默认设置下最佳 JPEG XL 约大 15–25%，最高设置下约大 6–20%，但存在 JPEG XL 反超的离群样本。
- ⚙️ JPEG XL 编码器差异很大：jixel 通常比 libjxl 更小，但在细节透明图上表现较差。
- 🖥️ 截图和插画场景 AVIF 明显更优：默认设置下 JPEG XL 约大 30–90%，最高设置下约大 20–70%，有损 AVIF 已能很好处理这类图。
- 🪟 透明图像 AVIF 优势很大：libjxl 约大 31–44%/61–70%，jixel 因透明通道无损编码，文件可达 AVIF 的 2–3 倍。
- ⏱️ 综合文件大小看，AVIF 编码更快、内存更省；jixel 本身更快更省内存，但文件通常明显更大。
- 🔍 AVIF 解码通常更快：JPEG XL 中等质量下约慢 2–3 倍，极高质量下差距缩小，Chrome 有时可反超。
- 📈 AVIF 和 jixel 提高 effort 通常值得，libjxl 高 effort 往往收益很小甚至文件更大。
- 🎨 不建议把 AVIF 4:2:0 作为默认：它很少减小文件，还会限制高质量上限；无暇逐图测试时优先 4:4:4。
- ✅ 各编码器的质量设置在测试中表现可靠：同一质量值下画质会随图片变化，但趋势一致且合理。
- 🌀 渐进式 JPEG XL 在高 effort 下几乎免费，但默认设置可能增大 12%；AVIF 也支持渐进渲染，控制更强、通常更小且解码更快。
- 🌈 HDR 方面 JPEG XL 缺少浏览器可用的 gain map，是相对 AVIF 的重要限制；非 gain map 的 HDR 比较中指标分歧较大。
- 🔄 JPEG XL 可将现有 JPEG 无损转码缩小 9–20%，大图解码有时更快，小图略慢。
- 🏆 无损压缩 JPEG XL 明显胜出：WebP 约大 9–17%，无损 AVIF 约大 30–120%，但网页上真正需要无损的场景很少。
- 🎞️ 动画图像格式仍不推荐；动画 AVIF 基于 AV1 视频表现更好，但播放实现仍差，视频应使用视频格式。
- 🧭 当前网页默认建议：AVIF 4:4:4，并选择可接受的最高 effort；若某图 AVIF 异常大，再试 jixel 编码的 JPEG XL。
- 🔬 测试使用最新编码器、约 1598px 宽图片、SSIMULACRA2/ColorVideoVDP 指标及多浏览器解码测试；作者强调不要轻信传言或 AI 二手结论，应拿自己的图片实测。

---

### [支持上下文内编辑的 React i18n 库 | Tolgee](https://tolgee.io/lp/react-i18n)

**原文标题**: [React i18n library with in-context editing | Tolgee](https://tolgee.io/lp/react-i18n)

Tolgee 是面向 React 的开源 i18n 库与本地化平台，主打“边写代码边同步文案键”，结合 AI/人工翻译与上下文编辑，让文本不再成为开发工单。它提供 T 组件、useTranslate Hook、ICU 复数、TypeScript、SSR，并支持 CLI/CI、REST API、标准格式与自托管；免费计划含 30,000 托管词和 3 个席位。

- 🚀 开发体验：安装 SDK 后用 T 组件或 useTranslate Hook 包裹字符串，新 key 会自动同步到 Tolgee 项目，三行即可运行。
- 🌍 本地化能力：支持 ICU 复数、占位符、性别、数字和日期，安全处理翻译中的 HTML，并提供 TypeScript 类型。
- 🖥️ 框架适配：SSR 就绪，Next.js 有专门页面；已使用 react-i18next 也可渐进接入。
- ✏️ 上下文编辑：开发模式下 Alt+点击运行中应用的文本即可编辑；产品经理、客户或译者可在应用内改文案，无需表格或代码。
- 🤖 AI 翻译：React SDK 会捕获文本在 UI 中的上下文，AI 可区分按钮“保存”和银行应用“保存”，新语言几分钟内就绪。
- 🔌 工程集成：提供 CLI/CI、REST API，支持 JSON、.po、XLIFF、.strings、.arb 等格式，数据不锁定。
- 🏠 开源与部署：Apache-2.0 许可，GitHub 4,000+ stars，可运行在 Tolgee 云或自有服务器。
- 💳 免费计划：无需信用卡，含 30,000 hosted words、3 个席位和 MT credits。
- 🧠 机器翻译：支持 Tolgee AI、DeepL、Google Translate、Amazon Translate、Microsoft Cognitive。
- 🛡️ 生产安全：生产环境应使用静态资源或 CDN，而非 REST API，避免泄露 API key；开发模式才从 Tolgee 拉取数据并支持编辑。
- 🔁 多端复用：启用 Tolgee ICU placeholders 后，Web、iOS、Android 等平台可复用同一套文案。
- ⚙️ 自动化：可用 GitHub Actions、GitLab CI/CD 配合 CLI pull 命令或 REST API export 自动导出数据。
- ⭐ 用户反馈：Curipod 称浏览器翻译导致的数百次 React 崩溃一夜降到零；客户认可 in-context editing 的易用性。

---

### [](https://jovidecroock.com/blog/graphql-malleable-ui/)

**原文标题**: [GraphQL as a foundation for malleable UI](https://jovidecroock.com/blog/graphql-malleable-ui/)

GraphQL 不只是帮助智能体理解 API 上下文的工具，更是构建“可变 UI”的基础：让智能体在应用运行时按用户需求重塑界面及其数据请求，而不必每次都改动服务端 API。这里的智能体指运行时替用户调整界面的智能体，而非在代码库中工作的编码智能体。

- 🧩 文章指出，GraphQL 与智能体的讨论常聚焦语义内省：让智能体搜索 schema 的相关部分，而不是加载全部定义。
- 🔄 更大的图景是“可变 UI”：智能体可在运行中重塑界面，并同步改变界面所需的数据。
- 🛒 产品卡片转库存对比表的例子说明，UI 形态变化会带来数据需求变化：需要新增库存字段，并去掉图片和价格。
- ⚠️ 固定端点容易导致数据不足或过度获取；增加端点、扩展响应或组合请求又受 API 预判能力和改动成本限制。
- 🎯 GraphQL 允许客户端在字段级别指定响应形状；网格和表格可共用同一 products 能力，服务端无需新增端点。
- 📱 “生成的界面”本质上也是客户端：不同应用、不同用户视图可共享 schema 契约，但拥有不同数据需求。
- 🧱 智能体通常只能改客户端，难以改后端；足够强的 GraphQL schema 让 UI 与查询操作在客户端一起演进，服务端契约保持不变。
- 🧩 Fragment 与组件同置可把数据需求声明局部化，并组合成操作；但渲染和数据选择仍需一起更新。
- 🔍 语义内省解决“发现能力”，客户端自定义选择解决“按新 UI 取数”，二者互补。
- 🚧 Schema 必须暴露相应能力，否则智能体无法凭空查询库存；仍需授权、查询成本控制和批处理等运维纪律。
- 🔐 持久化操作存在张力：生成视图会产生未见过的操作；可通过预注册操作、审批后注册、严格限额下的临时操作并晋升为持久化操作等方式处理。
- 💡 LLM 降低了写样板和处理器的成本，但没有降低每次新视图都改服务端的成本；这正是 GraphQL 适合持续变化界面的核心论据。

---

### [React 父树与所有者树的可视化表示法 | JulesBlom.com](https://julesblom.com/writing/react-visual-notation)

**原文标题**: [A visual notation for React's parent and owner trees | JulesBlom.com](https://julesblom.com/writing/react-visual-notation)

本文介绍一种用于展示 React 组件父级树与所有者树的视觉表示法，旨在通过图表提供仅靠代码难以呈现的结构性概览。

- 👤 作者：Jules Blom
- 🧩 主题：为 React 的父级树与所有者树设计可视化记法
- 📊 目的：将 React 组件以图表形式展示，帮助更清晰地理解整体结构
- 💡 价值：弥补仅靠代码难以表达结构关系的不足
- 🗓️ 发布时间：2026 年 10 月 8 日

---

### [错误](https://jimmyhmiller.com/what-does-the-react-compiler-even-do)

**原文标题**: [Error](https://jimmyhmiller.com/what-does-the-react-compiler-even-do)

无法总结：获取内容时出错 - ('Connection broken: IncompleteRead(8268 bytes read, 14697 more expected)', IncompleteRead(8268 bytes read, 14697 more expected))

---

### [托管式 Node.js 主机：无冷启动，无账单惊吓](https://www.cloudways.com/en/velocity.php?id=1258368&data1=reactdigest)

**原文标题**: [Managed Node.js Hosting Without Cold Starts or Bill Shock](https://www.cloudways.com/en/velocity.php?id=1258368&data1=reactdigest)

Cloudways Velocity 是公共预览阶段的托管 Node.js 托管平台，主打“始终热启动”、分钟级部署生产应用、全托管基础设施、企业级安全和固定可预测月费，面向个人开发者、代理机构、SaaS 初创、AI 构建者及非技术创始人。

- 🚀 **产品定位**：托管 Node.js 托管服务，生产就绪应用分钟内部署，无需招聘系统管理员。
- ♨️ **始终热启动**：持久服务器避免冷启动，固定月费避免按用量计费突增和账单意外。
- 🧩 **多场景支持**：适用于全栈 React、SSR/SSG、后端 API/微服务、内容与性能站点、企业前端、自动化/AI 工作流；其他框架若可按 Node 命令启动也可运行。
- ⚙️ **开发运维简化**：支持 Git 推送部署、内置 CI/CD、自动 OS 补丁/SSL/域名映射/备份、NGINX+PM2 缓存、PostgreSQL、环境变量及构建/错误日志。
- 🔐 **企业安全标配**：所有套餐包含 WAF、恶意软件防护、DDoS 缓解和 Cloudflare Enterprise CDN，无额外费用。
- 💰 **固定定价**：Starter $20/月至 Business $400/月，提供 2–64GB RAM、2–16 vCPU、5–150 个应用；可随时升降级且无锁定；Starter 和 Professional 含 3 天免费试用。
- 💳 **附加费用**：异地备份 $0.033/GB；超出套餐的 CDN 带宽 $0.02/GB。
- 🆚 **对比优势**：相比 VPS 免配置；相比 Railway 更少 DevOps；相比 Vercel 采用持久服务器和固定费用、无冷启动；相比 Heroku 成本更可预测。
- 👥 **适用团队**：代理机构、SaaS/初创、AI 构建者、非技术创始人。
- 🛠️ **框架与运行时**：开箱支持 12 个框架，包括 Next.js、Remix、React、Astro、Express、Fastify、Angular、n8n；Node.js LTS 22.x/24.x 可按应用选择。
- 🗄️ **数据库与支持**：PostgreSQL 可从仪表盘开通，也可使用外部数据库；所有套餐提供 24/7 专家支持。
- ⭐ **口碑**：G2 评分 4.7/5，并被列为 G2 报告“#1 Most Referenced Company”，在 Trustpilot 和 G2 获性能、可靠性与支持好评。

---

### [](https://mattrothenberg.com/notes/classname-considered-harmful/)

**原文标题**: [className Considered Harmful | Matt Rothenberg](https://mattrothenberg.com/notes/classname-considered-harmful/)

组件库普遍允许通过 `className` 覆盖样式，看似灵活，实际上会把组件内部实现变成公开 API；随着各团队复制和叠加覆盖，同一设计系统组件会演化出多种外观，增加维护、变更和协作成本。作者主张限制 `className`、建立覆盖清单，并用 lint 和 CI 审计来管理，同时考虑在 Kumo 中把 `className` 改名为 `DANGEROUS_className`，以便搜索和代码审查。

- 🧩 `className` 让调用方无需等待新变体就能改样式，但每个覆盖都会成为系统组件的“特例”。
- 📈 示例中 6 个组件在 24 个月内产生 64 个覆盖、涉及 7 个团队，每个组件最多出现 8 种外观。
- ⚠️ 覆盖会依赖组件内部 DOM 和类名，体现 Hyrum 定律：可观察行为终会被依赖，组件标记一变就可能破坏调用方。
- 🎨 设计 token 只能限制颜色和尺寸，不能阻止团队用合法 token 组合出语义不一致的多个 Badge。
- 🛡️ 各库策略从严格到宽松：Polaris/Braid 靠 props；Atlassian 用 xcss 且 lint 禁止 `className`；Spectrum 用 styles/`UNSAFE_className`；shadcn/React Aria 接受 `className`。
- 🔍 应先盘点所有传给设计系统组件的 `className`、`style` 和 CSS 选择器，按组件与类名分组，识别高频覆盖和潜在缺失变体。
- 🧪 重复覆盖是信号：五个团队给 Button 加 `rounded-full` 可能需要新 variant；给 Checkbox 加 `-mt-px` 可能是未报告 bug。
- 🚦 用 lint 阻止新覆盖，并在 PR 中对比 main 的覆盖清单、通知设计系统团队；可先非阻塞，避免卡住大量团队。
- ✍️ 作者所在的 Kumo 多数组件接受 `className`，Text 仅接受 `DANGEROUS_className`/`DANGEROUS_style`；他希望通过统一改名，用一次 grep 找到所有覆盖并推动新增 `bold` 等正式 prop。
- 📦 文中展示了一个改动 1,284 个文件、3,917 行增删的草稿 PR，但作者尚未正式提交，并想了解其他库类似迁移的经验。

---

### [用 React Compiler 降低 React Context 的开销 :: jjenzz](https://jjenzz.com/making-react-context-cheap/)

**原文标题**: [Making React Context Cheap with React Compiler :: jjenzz](https://jjenzz.com/making-react-context-cheap/)

文章讨论 React Context 缺少类似 `useContextSelector` 的选择器能力，并通过 5,000 个单选框的基准测试，比较 `useSyncExternalStore`、Context + `React.memo` 和 React Compiler。结果显示，文档推荐的“外层读 Context、内层 memo 视图”模式能跳过绝大多数视图工作，而 React Compiler 能在消费者组件内部复用 JSX 和记忆化中间值，性能可与 store 方案持平。核心结论是：与其执着减少 render 次数，不如让每次 render 变便宜。

- 🧩 React 至今没有 `useContextSelector`，任意 context 值更新都会让所有消费者重渲染，5,000 个 radio 会因一次点击全部更新。
- 🗂️ React 曾通过 `calculateChangedBits` / `unstable_observedBits` 控制消费者更新，但该机制已在 PR #20953 中移除；后续 RFC 和工作区方案也未落地。
- 🧪 官方建议把组件拆成“外层读取 context + 内层 memo 视图”，让内层只在真正使用的 props 变化时渲染。
- 📊 在 5,000 个 radio 的基准中，`useSyncExternalStore` store 与 Context + memoized view 的点击 p95 接近：19.2/64.9 ms vs 18.9/72.6 ms（1×/4× CPU 减速）。
- ⚠️ 自建外部 store 可能偏离 React 原语，并失去并发渲染等能力；`useSyncExternalStore` 更适合桥接已有外部状态。
- ⚡ React Compiler 可在消费者组件内部复用未变化的 JSX 和中间值，无需额外视图组件或选择器。
- 🏁 Compiler 版本点击 p95 为 18.4/63.6 ms（1×/4×），在该基准中与 store 和 memo 方案持平甚至略优。
- 🛠️ 未使用 Compiler 时，`React.memo` 拆分模式仍可用；文章还演示了 `withContextSelector` 抽象，但组件工厂形式与 lint 规则不完全契合。
- 🎯 更重要的不是统计 render 次数，而是降低每次 render 的实际工作量，让渲染变便宜。

---

### [编程文摘：电子邮件通讯](https://programmingdigest.net/?utm_source=web-archive&utm_campaign=react)

**原文标题**: [Programming Digest: Email Newsletter](https://programmingdigest.net/?utm_source=web-archive&utm_campaign=react)

Programming Digest 是一份面向软件工程师的精选周刊，每周通过一封邮件提供优质文章与简短摘要，帮助读者节省筛选内容的时间并持续学习。

- 📬 每周发送一封邮件，精选软件工程相关文章并附简短摘要。
- 👩‍💻 面向软件工程师，已有超过 20,580 名订阅者。
- ⏱️ 帮助读者节省寻找值得阅读内容的时间。
- 📚 强调每周都能学到新知识。
- 💬 读者反馈积极，提到 API 设计、Moving Faster 等优质内容。
- 🏢 受到软件工程师群体阅读。
- ©️ 由 Bonobo Press 运营，版权范围为 2013-2026，并提供 Newsletters、Privacy、Advertise 链接。

---

### [科技领导力：电子邮件通讯](https://leadershipintech.com/?utm_source=web-archive&utm_campaign=react)

**原文标题**: [Leadership in Tech: Email Newsletter](https://leadershipintech.com/?utm_source=web-archive&utm_campaign=react)

这是一份面向 CTO、工程经理和资深工程师的精选通讯，旨在帮助技术领导者提升领导力，并通过精选文章与摘要节省筛选内容的时间。

- 🎯 目标读者是 CTO、工程经理和高级工程师，帮助他们成为更好的领导者。
- 📬 每周一和周四发送邮件，已有超过 28,747 名工程领导者订阅。
- 📝 精选文章并附简短摘要，帮助读者节省寻找有价值内容的时间。
- 📚 每周都能学习新内容，持续提升技术领导力。
- 💬 读者认可其在软件领域领导力文章汇编方面的质量，尤其涉及架构讨论、会议、规划和沟通。
- 🧑‍💼 读者特别称赞关于“委派”的文章，强调委派是一项重要技能。
- 🏢 该通讯受到技术领导者阅读，内容由 Bonobo Press 提供，版权年份为 2013-2026。

---

### [](https://csharpdigest.net/?utm_source=web-archive&utm_campaign=react)

**原文标题**: [C# Digest: Email Newsletter](https://csharpdigest.net/?utm_source=web-archive&utm_campaign=react)

C# Digest 是面向 .NET 开发者的每周精选通讯，提供人工挑选并附简短摘要的文章，帮助读者节省筛选优质内容的时间、每周持续学习；目前已有超过 22,159 名 C# 工程师订阅，读者反馈内容实用，涉及功能标志、LINQ、DiagnosticListener、Operation Result Pattern 等主题。

- 📬 每周一封邮件，面向 .NET 开发者提供精选内容
- ✂️ 文章由人工挑选，并配有简短摘要，便于快速阅读
- ⏱️ 帮助读者节省寻找有价值内容的时间
- 📚 强调每周都能学到新知识
- 👨‍💻 已有超过 22,159 名 C# 工程师订阅
- 💼 读者表示部分内容已用于实际工作，并推荐给同事朋友
- 🧩 提及的主题包括标准功能标志、LINQ、DiagnosticListener、Operation Result Pattern
- ☁️ 有读者因 Operation Result Pattern 文章迁移了 Azure Function
- 🏢 内容面向 .NET 工程师，由 Bonobo Press 运营（© 2013-2026）
- 🔗 页面包含通讯、隐私和广告相关链接

---

### [让开发者紧跟最新动态——Bonobo Press](https://bonobopress.com/)

**原文标题**: [Keeping developers up to date â Bonobo Press](https://bonobopress.com/)

Bonobo Press 自2013年起发布软件行业通讯，面向超过94,000名软件开发人员、IT专业人士和技术人员，提供最新资讯，并通过订阅通讯与广告服务连接技术受众。

- 📰 专注软件通讯，帮助开发者及时了解行业最新动态。
- 👥 覆盖超过94,000名软件开发者、IT专业人士和技术人员。
- 🧑‍💻 通讯面向开发者、工程经理、技术负责人和CTO，强调简洁、精炼、省时。
- 📬 可查看各出版物并订阅。
- 🎯 广告服务可触达技术细分受众，对接软件工程师、团队负责人、工程经理、CTO及IT决策者。
- 📎 提供媒体资料包，可开始投放广告。
- ✉️ 如有问题、建议或广告需求，可联系。
- ©️ 网站版权为2013-2026 Bonobo Press，并附条款。

---

### [往期通讯：第1页](https://reactdigest.net/newsletters)

**原文标题**: [Past Newsletters: Page 1](https://reactdigest.net/newsletters)

这份 React Digest 汇总了 2026 年 6 月至 10 月的 React 与 Web 前端通讯，核心围绕性能优化、React Compiler、状态与表单管理、设计系统协作、Next.js 故障排查、浏览器渲染策略以及框架选型展开，既有具体案例和性能数据，也有对抽象成本与工程取舍的反思。

- 🖼️ AVIF 在大多数 Web 图片场景胜过 JPEG XL：文件更小、编码更快、内存占用更低。
- ⚛️ React Compiler 通过内联和更智能的 memoization 带来实际加速，自动复用未变化的 JSX，让 Context 更便宜，并减少对 useMemo/useCallback 的依赖。
- 🧩 设计系统组件接受 `className` 会埋下难追踪的不一致；Claude Design 的同步命令可把真实组件编译成可用镜像；GitHub 用 CSS Modules 替代 CSS-in-JS，服务端渲染时间降低 55%。
- 💸 过度抽象成本高昂：AI agent 费用高出 30%，部分任务高 5 倍；1,175 项下拉框 INP 达 1,256ms，仅渲染可见行后降至 96ms。
- 📱 Shopify 放弃 React Native，转向原生 Swift/Kotlin；浏览器翻译可能通过分离文本节点悄悄破坏 React；Vidact 直接把 React 编译为 DOM 操作，无需虚拟 DOM。
- 🧵 React 19.3 新增 ViewTransition 和 Fragment Refs；浏览器主线程每帧约有 10ms 预算，批处理更新和把工作卸载到 Web Worker 很关键。
- 🧠 React 内部原理教程覆盖 fiber 树、协调、Hooks、并发等；TanStack Form v2 alpha 引入验证器流水线和更清晰的服务器端验证。
- 🧪 三项修复让 React Testing Library 测试快 43%，关键是避免 jsdom 每次查询都扫描表单标签；TypeScript 可在编译期约束稳定 prop 引用。
- 🐞 Next.js 15.3–16.2 存在三类内存泄漏：缓慢漂移、随流量增长、超时阶跃，16.3 已修复；client hints 用一次 cookie 重载解决服务端时区渲染。
- ✅ Google modern-web-guidance 在真实 React 应用中查出缺失暗色模式、过期验证、表单未原生提交等问题，并用 Baseline 日期判断模式是否可安全发布；TanStack 因依赖缩小、普通 SSR 足够快而放弃 RSC。
- 📝 `useActionState` 减少表单状态样板，但要防本地 pending 标志导致重复提交；Next.js 状态管理可从 URL 状态到乐观更新分层处理。
- ⚡ 乐观 UI 在快速点击下会因请求乱序而失准，按条目 pending 锁可修复；很多 useMemo 实际无效，也并非所有项目都需要状态库。
- 🧾 表单是复杂状态机，不只是 UI；需按场景选择 React 19、客户端库、server actions、多步向导和可编辑表格；“状态管理”很多时候只是缓存，CRDT 可能更合适。
- 🚀 ChatGPT 前端是标准 React 栈，完全服务端渲染并在 100ms 内流式输出，围绕快速输入优化；hydration 不匹配会悄悄拖累 LCP。
- 🧭 React 19 移除 Test Renderer 后可用 reconciler 自建；Next.js 16.3 预览即时导航；组件通信按场景选 props、context、Zustand，React Router v8 要求 React 19 和 Node 22。
- 🏎️ React 19 自动 memoization 后，性能重点转向状态放置和 useTransition；多数 useEffect bug 源于不稳定对象引用，最好的修复常是删除该 effect。
- 🔄 TanStack Query 几乎零配置处理竞态、缓存和后台刷新；Linear 通过在浏览器存数据并后台同步实现无 spinner 的即时 UI；Formisch 用一套表单核心适配六个框架。

---

### [隐私](https://reactdigest.net/privacy)

**原文标题**: [Privacy](https://reactdigest.net/privacy)

该隐私政策说明 React Digest 如何收集、使用、披露和保护个人信息，核心承诺是仅将邮箱地址用于发送邮件新闻通讯，并为用户提供访问、删除数据和退订渠道。

- 🔍 在收集个人信息前或收集时，明确说明信息收集目的。
- 📧 仅收集邮箱地址，用于发送邮件新闻通讯，不用于其他目的。
- 🎯 个人信息仅用于指定目的或兼容目的，除非获得用户同意或法律要求。
- ⏳ 仅在实现收集目的所需期间保留个人信息。
- ⚖️ 通过合法、公平的方式收集信息，并在适当情况下告知用户或征得同意。
- ✅ 个人数据应与使用目的相关，并在必要范围内保持准确、完整和最新。
- 🔒 采取合理安全措施，防止信息丢失、被盗、未经授权访问、披露、复制、使用或修改。
- 📢 向客户提供隐私政策及个人信息管理实践信息，并承诺保护信息机密性。
- 👶 遵守美国 COPPA，不有意收集或存储13岁以下儿童的信息。
- 🗂️ 根据英国《1998年数据保护法》，用户可申请获取所持有的个人数据，但受法律限制。
- 🗑️ 用户可通过邮件请求删除其数据。
- 🚫 反对垃圾邮件，用户可随时通过邮件中的退订链接取消订阅。
- ©️ 网站版权归 Bonobo Press 所有（2013-2026），页面包含新闻通讯、隐私和广告链接。

---

### [媒体资料包 – Bonobo Press](https://bonobopress.com/media-kit/)

**原文标题**: [Media Kit â Bonobo Press](https://bonobopress.com/media-kit/)

Bonobo Press 的媒体资料包介绍其面向程序员和技术人员的新闻简报广告服务，强调内容精选、高互动受众和严格名单清理，帮助广告主精准触达软件开发者、工程管理者、CTO 等，并提升参与、线索与转化。

- 📬 提供四份垂直新闻简报：Leadership in Tech、Programming Digest、C# Digest、React Digest，分别面向技术管理者、软件工程师、.NET/C# 开发者与 React 前端开发者。
- 📈 Leadership in Tech：29,158 订阅，51.47% 独立打开率，11.38% 自然点击率，赞助价 $2,235/期，预计点击 365–585，CPC $3.82–$6.12；次级位置 $1,565。
- 💻 Programming Digest：21,149 订阅，45.57% 打开率，14.83% CTR，$985/期，预计点击 273–493，CPC $2.0–$3.61。
- ⚙️ C# Digest：21,077 订阅，53.41% 打开率，21.63% CTR，$1,220/期，预计点击 411–631，CPC $1.93–$2.97。
- ⚛️ React Digest：22,463 订阅，49.86% 打开率，12.17% CTR，$1,375/期，预计点击 180–400，CPC $3.44–$7.64；次级位置 $962。
- 🌍 读者主要来自欧洲（约 35%–48%）和美国（约 30%–35%），所在公司包括 Google、Amazon、Netflix、Dropbox、Shopify 及不同规模企业。
- 📝 广告为纯文本形式并嵌入正文；素材包括 URL、标题（建议少于 100 字符）和描述（建议少于 400 字符），文案截止为发布前 4 天。
- 🤝 近期合作伙伴覆盖 Okta、GitLab、Datadog、OWASP、MongoDB、Twilio、Pluralsight 等，广告品类包括工具、招聘、会议、网络研讨会、书籍与课程。
- 🗓️ 下单流程：说明产品与目标 → 确认受众/排期 → 付款锁定档期 → 提交素材 → 上线 → 效果报告；广告位紧张，建议提前数周联系。
- 📩 可通过 Bonobo Press 联系广告合作并参考预订条款，其目标是连接合适受众并提升参与、线索和转化。

---
