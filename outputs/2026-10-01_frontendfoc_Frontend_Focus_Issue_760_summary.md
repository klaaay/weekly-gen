### [](https://github.blog/engineering/architecture-optimization/improving-site-performance-by-shipping-more-css/)

**原文标题**: [Improving site performance by shipping more CSS - The GitHub Blog](https://github.blog/engineering/architecture-optimization/improving-site-performance-by-shipping-more-css/)

GitHub 通过将 github.com 从 CSS-in-JS 全面迁移到 CSS Modules，解决了组件增长带来的性能瓶颈；团队借助功能标志、视觉回归测试和渐进发布，安全完成 Primer 与产品代码迁移，最终在 2026 年 6 月实现 100% CSS Modules，并移除 sx、styled-components 和 styled-system，同时提升性能与用户体验。

- 🧩 Primer Design System 支撑 GitHub 大量界面；2023 年组件数量激增，暴露出 CSS-in-JS 的客户端样式初始化、SSR 性能下降和样式更新失控问题。
- 🎯 团队选择 CSS Modules：使用原生 CSS、与组件同文件、类名默认局部作用域，无客户端或服务器运行时，样式随 HTML 以 CSS 文件发送。
- 🚩 迁移采用渐进策略：为每个组件新增 CSS Modules 文件，用功能标志切换新旧样式，借助视觉回归测试验证，再逐步向团队、员工和所有用户发布。
- 📉 到 2024 年 12 月，Primer 组件全部迁移；服务端渲染时间减少 55%，页面组件初始化时间减少 25%。
- ⚛️ 更大挑战是 GitHub 产品中的 sx prop：TypeScript 与 Design Tokens 支持好、与组件共置，但动态内联对象运行时成本高、难以扩展。
- 🧱 为兼容迁移，创建 @primer/styled-react 包装组件，让使用 sx 的代码继续消费新组件，同时逐步将导入替换为 @primer/react。
- 🤖 2025 年 4 月启动 sx 迁移，峰值约 7,760 个；内部 VS Code 插件和 codemod 辅助，8 名工程师 6 个月迁移 6,419 个，部分页面 SSR 提升 1%–22%。
- 🦾 2026 年 4 月借助 Copilot coding agents，两名工程师三周内将剩余 895 个 sx props 降至 0。
- 🎨 主题是最后障碍：GitHub 支持 7 种主题及高对比度模式，依赖 styled-components；团队将主题逻辑与 JS 工具解耦，经过两个月迁移、功能标志和逐步发布后移除依赖。
- ✅ 2026 年 6 月起 GitHub 运行在 100% CSS Modules 上；这次迁移不仅移除 sx、styled-components、styled-system，也实现了安全的渐进式重平台化，提升性能与用户体验。

---

### [](https://www.tigerdata.com/go/trial?utm_source=content-syndication&utm_medium=referral&utm_campaign=frontend-focus-newsletter)

**原文标题**: [Postgres for time-series workloads at any scale. | Tiger Data](https://www.tigerdata.com/go/trial?utm_source=content-syndication&utm_medium=referral&utm_campaign=frontend-focus-newsletter)

Tiger Data（Timescale）提供面向时间序列工作负载的 Postgres 云服务，主打任意规模扩展、企业级安全与高可用，并以超大规模真实案例吸引 IoT 等场景客户。

- 📬 页面提供联系与开始使用入口。
- 🚀 单实例 Tiger Cloud 服务可达每天 3 万亿指标、3 PB 数据、1 千万亿数据点。
- 🎁 新用户注册可得 $1000 信用额度，30 天有效，无需信用卡，仅限新账户。
- 🏭 受数千家 IoT 公司信赖。
- 📈 核心能力包括弹性扩展：读写分离，副本集最多 10 节点，SSD/S3 分层存储，实现低成本、海量存储。
- 💰 计算与存储分离，可独立扩缩容，避免为空闲容量付费，并优化性能与成本。
- 🛡️ 高可用：多可用区集群、自动故障转移、时间点恢复、跨区域备份。
- 🔐 企业级合规与安全：SOC 2、HIPAA、GDPR，始终加密，支持 SSO、RBAC、审计日志。
- 🔍 深度可观测性：查询下钻与仪表板，指标可发送至 CloudWatch、Datadog、Prometheus。
- ⚡ 快速开通：几分钟内创建数据库，可通过 SQL、CLI、Terraform、Cursor、Claude Code 管理。
- 🔌 集成能力：可搭配首选云厂商及更广泛的 Postgres 生态。
- 🏢 企业默认就绪：提供正常运行时间 SLA、区域数据隔离、合规认证，以及 24/7 全球 Postgres 专家支持和保证响应时间。
- ©️ 页面包含隐私偏好、法律、隐私、站点地图；2026 年版权归 Timescale, Inc. d/b/a Tiger Data 所有。

---

### [](https://emdashcms.com/blog/emdash-1-0)

**原文标题**: [EmDash 1.0: an open source CMS for Astro â EmDash CMS](https://emdashcms.com/blog/emdash-1-0)

EmDash 1.0 正式发布，这是一个基于 Astro 构建的稳定、免费且开源的 CMS，历经六个月开发与生产环境验证，现已准备好服务于从个人博客到大型生产站点的各类需求。

- 🚀 EmDash 1.0 正式发布，稳定、免费、开源，基于 Astro 构建，已通过生产环境验证，适合个人博客到大型站点
- 💡 构建灵感源于“如果今天重新打造 WordPress 会是什么样”，优先考虑易用性、插件生态和主题系统
- ☁️ 支持免费部署到 Cloudflare，无需新服务器即可应对大规模流量，无锁定，可在任何 Node.js 环境运行
- 🤖 从底层为人类和 AI 代理设计，内置 MCP 服务器、API 和 CLI，人类能做的代理也能做
- 🛠️ 内置 OAuth 与细粒度访问控制，默认模板附带代理技能，可轻松搭建新插件或从 WordPress 迁移
- 📅 项目于 4 月 1 日首次公布，六个月间合并数千个 PR，1.0 目标聚焦稳定、安全和大规模测试
- 🌐 Cloudflare 博客在 7 月 Agents Week 前率先切换至 EmDash，成功应对数百万页面浏览和 DDoS 攻击
- 🔓 采用 MIT 许可证，给予用户更多自由和灵活性，可分发私有主题或插件
- 👥 社区蓬勃发展，Discord 数百名成员，近 200 名外部贡献者，多数提交来自外部
- 🔒 插件采用沙箱模型，每个插件在隔离环境中运行，无直接访问站点权限，解决 WordPress 96% 安全问题
- 🌐 插件注册表基于 AT Protocol 构建，去中心化，无中央权威控制，任何人可创建兼容商店
- 🎯 注册表本周启动，计划举办插件黑客松，所有现有插件均可参与
- 🔮 团队表示这只是开始，未来有更大计划，邀请用户加入 Discord 参与塑造 EmDash 的未来
- 🧪 提供在线游乐场试用，可通过 npm create emdash@latest 或让代理参考文档快速开始

---

### [](https://emdashcms.com/blog/emdash-plugin-registry)

**原文标题**: [Ship your plugin to the EmDash plugin registry â EmDash CMS](https://emdashcms.com/blog/emdash-plugin-registry)

EmDash 1.0 正式发布，官方插件注册表同步上线，本文详细介绍了如何从零开始创建、测试并发布一个沙盒化插件到注册表。

- 🚀 EmDash 1.0 发布，官方插件注册表 plugins.emdashcms.com 正式上线，开发者可发布插件供其他站点安装
- 🔒 注册表插件始终在沙盒中运行，仅获得声明的权限；原生插件无法发布到注册表，需通过 npm 分发
- 👤 发布者以个人 Atmosphere 账号签名发布，需提前创建账号，脚手架会将账号写入清单文件
- 🛠️ 使用 `pnpm dlx @emdash-cms/plugin-cli init my-plugin` 生成项目，包含清单、入口、测试和 AGENTS.md
- ⚙️ 清单文件声明 capabilities 和 allowedHosts，管理员安装前审核，运行时严格限制插件行为
- ⚠️ 若钩子所需权限未声明，钩子会被跳过并记录警告；运行 `pnpm run validate` 可捕获大部分清单错误
- 📌 publisher 必须固定为 DID 而非 handle；新增权限或主机需作为主版本发布，已发布版本不可替换
- 🧪 开发时先运行 `pnpm dev`，站点通过 `sandboxed` 和 `sandboxRunner` 配置加载插件，缺少 runner 会导致插件被跳过
- ☁️ Node.js 使用 workerd 运行器，Cloudflare Workers 需 Worker Loader 绑定且要求付费计划；建议在 Cloudflare 上测试后再发布
- 📦 打包有硬性限制：解压后总大小 256 KB，单文件 128 KB，最多 20 个文件，后端代码不可使用 Node 内置模块
- 📤 使用 `pnpm exec emdash-plugin login` 和 `publish` 发布，插件命名为 `@your-handle/slug`，发布记录写入个人 PDS
- 🔍 新插件上线前需通过自动检查和人工审核，CLI 提供 `--watch` 命令跟踪检查进度
- 🤖 可通过 `pnpm exec emdash-plugin release setup` 配置 GitHub Actions 自动发布，标签格式为 `slug@version`
- 🌐 发布记录存储在个人账号中，注册表只是索引之一，任何人都可基于相同记录运行自己的目录
- ✅ 站点安装前会验证发布记录的签名来源、校验和及权限，目录无法替换代码
- 💰 目前所有注册表插件免费，未来计划支持付费插件并保持账号所有权模型
- 📚 官方提供沙盒插件入门、打包发布和清单参考等文档，开发者可在 EmDash Discord 分享插件

---

### [EmDash 插件](https://plugins.emdashcms.com/)

**原文标题**: [EmDash Plugins](https://plugins.emdashcms.com/)

EmDash 插件注册中心汇聚沙盒化、可移植插件，用于为 EmDash 添加工作流、集成和内容工具；支持搜索、浏览注册表，并展示最近更新插件及其作者、版本、MIT 许可与标签。

- 🧩 平台定位：EmDash 插件注册中心让用户“打造自己的 EmDash”，发现沙盒化、可移植插件。
- 🔎 发现方式：提供搜索和“探索注册表”，按最近更新展示插件。
- 📦 插件信息：每个条目包含作者、路径/名称、版本、许可（大多为 MIT）和标签。
- 📊 分析工具：Umami Analytics、Analytics、Dynamic QR 等提供流量、热门页面、来源、国家、单篇浏览和扫码分析。
- 🚦 发布与 SEO 检查：Preflight、seo-guard、Publish Check、SEO Suite、Link Guardian、Crosslink 等阻止或警告 SEO、链接、标题、描述、图片 alt 等问题。
- 📝 表单与提交：Contact Forms、Forms、Freeform、contact-form 等支持字段构建器、条件逻辑、提交收件箱、CSV 导出和通知。
- ✉️ 邮件与通知：SMTP、Resend、Forward Email、Cloudflare Email Sending、Comment Notify、Bulletin 等处理事务邮件、订阅和评论通知。
- 🗂️ 内容历史与审计：Simple History、audit-log 跟踪内容/媒体创建、更新、删除，用于合规和调试。
- 📅 事件管理：Eventual 管理事件、场馆和公共 feed，含 MCP 工具与 Astro 七种访客视图示例。
- 🤖 AI 与多语言：AI Alt Text 生成图片替代文本；LinguaDash 翻译内容与 SEO 字段；ai-search 提供 AI 搜索与聊天。
- 🔔 自动化与分发：Discord Notifier、Webhook Notifier、EmDash to Buffer、AT Protocol Syndication 等发送提醒、webhook、排队社交发布和跨站同步。
- 🧪 测试与扩展：marketplace-test 用于注册、授权、运行时和管理测试；插件可添加管理页面、内容钩子、存储、API 路由和自定义 Portable Text 块。
- 🛠️ 行动号召：有想法可为 EmDash 构建插件，或阅读文档。

---

### [](https://claude.dev/blog/how-we-made-claude-ai-faster/)

**原文标题**: [How we made claude.ai 3x faster in two weeks / claude.dev Blog](https://claude.dev/blog/how-we-made-claude-ai-faster/)

overview summary
Anthropic 团队在两周冲刺中，让 claude.ai 和 Claude 桌面应用的核心用户体验约快 3 倍。他们把性能工作放进一个 Slack 频道，让 Claude 在几乎每个线程中找瓶颈、建基准、提交 PR、监控部署；人类负责设定目标、做取舍并批准改动。最终 13 项核心指标平均提升 3.1 倍，合并 3000+ 改动，且没有客户可见事故或回滚。
- 🎯 聚焦占 95% 用户活动的四大旅程：启动应用、开始对话、加载已有对话、发送消息。
- 📊 p75 指标显著改善：claude.ai 新加载可输入页面 3.1s→0.55s，Claude Code 新会话 0.8s→0.3s，Cowork 云会话 2.6s→0.73s。
- ⚡ 跨 web、桌面与产品共 13 项测量，几何平均提速 3.1 倍，估计每天节省数万用户小时等待。
- 🤖 使用 Claude Tag（beta，接近 Opus 5.5 的内部研究模型）分析 Datadog 使用数据，识别高影响旅程并建立可比基线。
- 🧱 冲刺开始时列出约 20 个项目，Claude 以毫秒估算影响，团队据此设目标；第 3 天完成 13 个目标中的 12 个。
- 🚀 早期落地包括静态 composer 写入 HTML、V8 代码缓存、跨会话保持 composer 挂载、hover 预取、侧边栏重渲染减少 90%。
- 🧪 核心经验：让 Claude 测量某物，它就能优化；确定性基准包括 Valgrind + node --predictable 指令数、React commits、V8 调用数、样式重算、DOM 变更。
- 📉 基准必须证明与墙钟延迟相关，并通过 CI ratchet 只能下降；消息树组装指令 -48%/墙钟 -78%，状态行扫描器 -31%/-44%。
- 🔁 工作循环：开线程→追踪并建基准→提交带 flag 的 PR→部署→读真实用户数据→成功则 ratchet、失败则关 flag 迭代→寻找下一慢点。
- 🧵 同时运行 150+ 线程，单线程可提交 50–100 个优化 PR；最忙一天 200+ 改动，约三分之一 PR 增加遥测或护栏。
- 🔍 Claude 发现的问题包括：composer 打字路径 6900 个 hooks、:root:has() 增加 24ms、遗留 location.reload() 每天 50 万隐藏刷新、em dash 触发 UTF-16 慢路径导致代码高亮卡顿。
- 🛡️ 安全机制：自动审查 + 人类批准、测试先于优化、短期 feature flag；近 200 个 flag，超过一半已清理。
- 🧩 静态 composer 有多重护栏：jsdom 生成真实组件、14 种视口 1px 对齐测试、按键穿透测试、现场 handoff 十分之一像素监测。
- 🎛️ 人类通过三件事引导：Ambition 鼓励更大胆、Taste 裁决用户体验取舍、Direction 保持线程聚焦并排序优先级。
- 🎞️ 8.33ms 帧预算：Claude 用 headless Chrome DevTools 固定 120Hz 逐帧测试，长回复流式渲染近 60 个 PR，主线程总阻塞 750ms→200ms，CPU 约降至三分之一，120Hz 全程 120fps。
- 🔭 下一步：继续优化 p95、其他旅程与超长对话；还将分享对 Electron、Chromium、Node.js 等上游贡献，Slack 频道仍在运行。

---

### [](https://blog.cloudflare.com/turnstile-spin/)

**原文标题**: [Agents can now set up your websiteâs security with Turnstile Spin | Cloudflare Blog](https://blog.cloudflare.com/turnstile-spin/)

Cloudflare 推出 Turnstile Spin，让 AI 编码代理自动完成 Turnstile 机器人验证的安装、修复与迁移，把原本前端小部件加后端 Siteverify 的两步流程，变成由代理引导、用户批准、端到端完成的简化工作流。

- 🛡️ Turnstile 是 Cloudflare 于 2023 年推出的隐私优先、无需 CAPTCHA 的客户端挑战，免费且可用于任意网站。
- 🤖 新推出的 Turnstile Spin 面向 AI 编码代理，帮助自动完成 Turnstile 的端到端部署与后端验证。
- 🧩 传统 Turnstile 需要两步：前端渲染 widget 获取 token，后端调用 Siteverify 验证 token。
- 📈 Turnstile 每个典型工作日处理约 30 亿次验证，近期一周有超过 23,000 个账户创建新 widget。
- ⚙️ Spin 将设置变成引导流程：用户选择保护位置，代理定位前后端代码、提出计划、等待批准后完成集成。
- 🔐 Spin 不把应用代码发送给 Cloudflare，也不远程修改；由用户已有的编码代理在代码库中做已批准更改，Cloudflare 账户只新增 widget。
- 🛠️ 支持三种场景：全新安装、修复缺少后端验证的现有 widget，以及从其他 CAPTCHA 迁移。
- 🚀 可从 Cloudflare 仪表盘、Wrangler 或粘贴 public skill URL 给代理来启动 Spin。
- 📊 7 月发布以来，仪表盘记录超过 65,000 次成功 Spin widget 创建，生成提示被复制超过 30,000 次。
- 🆓 Turnstile 对所有人免费，可创建 Cloudflare 账户试用，并查看文档与反馈。

---

### [](https://blog.cloudflare.com/cloudflare-cf-cli-launch/)

**原文标题**: [Introducing cf: the agentic CLI for the entire Cloudflare API | Cloudflare Blog](https://blog.cloudflare.com/cloudflare-cf-cli-launch/)

Cloudflare 发布面向智能体（agent）的 CLI 工具 cf，目标是让智能体通过单一工具使用整个 Cloudflare API：从创建和部署 Worker、监控、Access 保护、购买域名到 WAF 防护。cf 基于 OpenAPI/Forge 自动生成，覆盖 3000+ 操作，默认 JSON 输出，内置自然语言命令搜索，采用 TypeScript 配置 cloudflare.config.ts，并以 Vite 作为默认开发体验，同时支持从 Wrangler 迁移。

- 🤖 智能体使用 Wrangler 激增：2026 年 3 月占比 25%，上周达到 48%；智能体每天使用不同命令数几乎是人类两倍，使用 6 个以上命令的可能性高近四倍。
- 🚀 cf 是新一代智能体 CLI：智能体可通过定制搜索和引导找到完成任何任务所需的命令。
- 📦 借助 Forge 从 OpenAPI schema 生成 CLI，把 Wrangler 约 280 个操作扩展到 Cloudflare API 的 3000+ 操作。
- 🧾 默认 JSON 接口：对人类美化打印，对智能体压缩输出，减少上下文消耗；不再依赖 --json 和 jq 过滤。
- 🔎 新增 cf cli search：智能体可用自然语言描述需求，获得合适命令列表；首次运行 --help 时会自动提示该功能。
- ⚙️ cloudflare.config.ts 成为新配置格式：从 Workers 开始，提供 TypeScript 类型检查、程序化配置，并让 LSP/智能体更准确编辑配置。
- 🧩 提供 bindings 和 triggers 辅助函数：集中管理环境变量、密钥、KV、D1、R2、队列、AI、Vectorize、Worker 绑定，以及 fetch、定时、队列、邮件等触发器。
- ⚡ Vite 成为默认：带来最佳本地开发服务器、HMR、插件生态和基于 Rolldown 的构建；Cloudflare Vite Plugin 是推荐 Workers 构建方式。
- 🔁 迁移简单：cf migrate 可从 Wrangler 迁移；已用 Vite 的 Worker 会转为 cloudflare.config.ts；依赖 esbuild、Rust 或 Python 的 Worker 仍委托 Wrangler。
- 🧪 新项目可用 cf init/deploy 自动配置；静态站点仍无需配置文件，运行 cf deploy 即可部署。
- 📅 公测结束后将发布 Wrangler 最终大版本并引导使用 cf，同时继续维护 Wrangler 18 个月。
- 🌐 cf 已开源，问题可提交到 GitHub；安装方式为 npm i -g cf，目前全球开放测试。

---

### [](https://webkit.org/blog/18357/release-notes-for-safari-technology-preview-253/)

**原文标题**: [  Release Notes for Safari Technology Preview 253 | WebKit](https://webkit.org/blog/18357/release-notes-for-safari-technology-preview-253/)

Safari Technology Preview 253 于 2026 年 9 月 23 日发布，适用于 macOS Golden Gate 和 macOS Tahoe；已安装用户可在“系统设置 → 通用 → 软件更新”中更新。本版本包含 320113@main…321067@main 之间的 WebKit 变更，覆盖无障碍、动画、CSS、JavaScript、媒体、网络、性能、渲染、SVG、安全、Web API、扩展、Web Inspector、WebAssembly、WebDriver、WebGL、WebGPU 和 WebRTC 等大量新功能与修复。

- 📅 发布信息：Safari Technology Preview 253 由 Saron Yitbarek 发布，支持 macOS Golden Gate 与 macOS Tahoe。
- ⬇️ 更新方式：已安装用户可在“系统设置 → 通用 → 软件更新”中获取更新。
- ♿ 无障碍：修复 VoiceOver 对 aria-keyshortcuts 中 Meta/Alt 的朗读，以及重复播报实时区域内容。
- 🎞️ 动画：新增样式来源滚动时间线全局匹配支持，并修复 ViewTimeline、timeline-scope、暂停/恢复等多项问题。
- 🎨 CSS 新特性：支持东亚计数样式扩展数字范围、CSSContainerRule.conditions、safe/unsafe 与 normal 对齐组合、容器查询中的 sibling-index()/sibling-count()。
- 🧱 CSS 修复：改进网格/弹性轨道、背景平铺、高亮颜色、列表标记、box-shadow、corner-shape、行高 quirk、attr()、text-indent、tab-size、渐变 content 等。
- 🖌️ Canvas：修复 OffscreenCanvas 占位画布、噪声注入像素、drawImage 自身绘制性能、2D 上下文分配失败后不可用等问题。
- ✏️ 编辑与表单：修复禁用复制 PDF 的右键/编辑菜单，以及基础外观 select 大选择器跑出视口。
- 🌐 HTML/API：修复窗口 load 事件可能不触发；新增 QuotaExceededError 为 DOMException 子类。
- ⚙️ JavaScript：Intl.PluralRules 支持 BigInt，大 BigInt 采用更快的 Toom-3 乘法；修复 JIT、RegExp、Temporal、TypedArray、Object.freeze 等多项问题。
- 🎬 媒体：修复无线播放会话创建、MediaRecorder 关键帧、AV1 序列头边界、视频黑位像素等问题。
- 🔗 网络：修复 file: URL 子资源 CORS、大于 2GB Blob 读取溢出、HTTP 头尾字符验证。
- 🚀 性能：修复长 URL 重复解析卡顿、IntersectionObserver 高 CPU、scroll-timeline 样式解析阻塞、滚动节点排序和全层重绘。
- 🖼️ 渲染：修复负 z-index 合成、MathML、组合标记绘制、图片底部间距、blur 重绘、clip-path/mask 不透明判断、sticky 反射等。
- 🧩 SVG：新增 <textPath> 的 SVG 2 path 属性；修复条件处理、SVGLength ex 单位、SMIL 释放、加色动画精度等。
- 🔒 安全：修复后台窗口点击可触发操作，以及未清除默认端口 HTTPS 凭据。
- 🧪 Web API/扩展：修复 URLPattern、Cache、WebXR、点击修饰键等；扩展新增 offscreen API，并改进 i18n/webRequest/declarativeNetRequest。
- 🛠️ 工具与底层：Web Inspector 新增网络节流；WebAssembly、WebDriver、WebGL、WebGPU、WebRTC 均有多项修复。
- 📚 参考：上一版为 WebKit Features for Safari 27.0。

---

### [获取失败](https://blog.mozilla.org/en/firefox/new-firefox-design-is-here/)

**原文标题**: [Failed to retrieve](https://blog.mozilla.org/en/firefox/new-firefox-design-is-here/)

无法总结：获取内容失败，状态码 403。

---

### [](https://www.youtube.com/watch?v=l7tQ1v4TCeY)

**原文标题**: [That’s Firefox? See the browser’s surprising new changes - YouTube](https://www.youtube.com/watch?v=l7tQ1v4TCeY)

本内容为 YouTube/Google 页面底部的导航与法律信息，涵盖平台介绍、联系与合作入口、创作者/广告/开发者资源、政策条款，以及版权声明。

- ℹ️ About：平台或公司介绍
- 📰 Press：新闻与媒体信息
- ©️ Copyright：版权相关说明
- 📞 Contact us：联系方式
- 🎬 Creators：创作者资源与入口
- 📣 Advertise：广告与商业合作
- 💻 Developers：开发者资源与接口
- 📜 Terms：服务条款
- 🔒 Privacy：隐私政策
- 🛡️ Policy & Safety：政策与安全
- ⚙️ How YouTube works：YouTube 运作方式
- 🧪 Test new features：测试新功能
- © 2026 Google LLC：版权归 Google LLC 所有

---

### [Web 开发](https://molily.de/web-dev-education/)

**原文标题**: [The death of web development education – Rescuing a field from disappearing](https://molily.de/web-dev-education/)

生成式AI正在重创Web开发教育生态：许多教育者、技术作者、课程创作者和DevRel从业者收入骤降甚至归零，内容被AI爬虫和LLM无偿抓取、吞并并再生成，导致优质免费内容、独立教学和社区协作难以为继。文章通过多位从业者经历，呼吁承认并补偿人类知识劳动，反对“适应AI”的冷漠叙事，重建以人为本、开放、民主、可持续的Web开发学习共同体。

- 📉 Baldur Bjarnason：跨界经历长期难以经济维生，社区还排斥跨学科者；GenAI让培训、课程和电子书需求崩溃，开发者转向易错、非确定性的聊天机器人当作“Web开发教育”。
- 💸 Axel Rauschmayer：JavaScript/TypeScript多产作者，书收入从2024年足以维生到2026年归零；博客和免费书流量多来自AI爬虫，没有广告收入，只能下线以应对AI公司窃取作品。
- 🔥 Salma Alam-Naylor：DevRel压力导致倦怠焦虑；AI正在杀死开发者教育，开发者不再真实协作，而沉迷短视频和聊天机器人；精心课程被预测算法窃取再生成，个人经验与教学价值被抹除。
- 📚 Josh W. Comeau：课程创作者普遍收入下降50%以上，参与减少，用户转向LLM；LLM未经同意和补偿吞食内容并再吐出，免费优质内容失去制作激励。
- 🎥 Kyle Cook/Web Dev Simplified：编程教程观看量和收入约减半，难以持续；做AI模型视频更易、更赚钱、更高流量，编程内容几乎无经济理由，只能靠热爱和其他收入支撑。
- ✍️ Rachel Andrew：GenAI破坏作者与编辑关系，AI可能引入细微错误且自信地出错，增加编辑核查负担；LLM用途有限，输出必须由真正关心结果的人审查。
- ⚙️ 生产率质疑：AI自动化本可不用AI完成；所谓个人效率提升常是把工作转嫁给编辑或读者，降低质量。应教更多人用现有工具自动化，只在真正增值处用AI。
- 🧭 对“适应AI”叙事的批评：简单劝人适应、转型、清理AI垃圾，等于在伤口撒盐；应感谢并承认教育者、作者、研究者、开源开发者，要求AI寡头为其造成的危机付费。
- 🌐 价值重申：Web是激进民主媒介，独立学习社区、开放技术、伦理原则和共享数字基础设施是自我赋权；GenAI的“民主化”说辞实则集中权力、商品化知识。
- 🧱 结论：Bjarnason认为Web开发已不是原领域，怀旧源于领域一夜消失；要重建需互助网络、掌握技术、挖掘并建立最佳实践、分享洞见，并确保人类知识教育工作获得报酬。

---

### [](https://bell.bz/in-response-to-the-death-of-web-development-education/)

**原文标题**: [
  In response to “The death of web development education” - Andy Bell
](https://bell.bz/in-response-to-the-death-of-web-development-education/)

这篇发表于 2026 年 9 月 30 日的短文回应了 Matthias Schäfer 的《The death of web development education》。作者认为最有效的贡献是展示 Piccalilli 的 Stripe 历史销售图表：自 2025 年以来总销售额下降 67.5%，形势严峻，必须改变，否则人们会怀念消失的出版商。文末他介绍了自己的身份与项目。

- 📝 文章回应 Matthias Schäfer 的《The death of web development education》。
- 🤔 作者想参与讨论，却很难清楚表达问题所在。
- 📉 他选择用粗略草图展示 Piccalilli 的 Stripe 历史销售数据。
- ⚠️ 数据显示自 2025 年以来总销售额下降 67.5%，前景黯淡。
- 🔄 他强调必须改变，否则当出版商消失后大家会想念他们。
- 👋 作者 Andy 介绍了自己的个人网站。
- 🏢 他是 Set Studio 创始人，该创意机构专注打造适合所有人且出众的网站。
- 📚 他也是 Piccalilli 创始人，这一出版物帮助前端开发者提升水平。
- 🎓 他还推出 Complete CSS 课程，帮助开发者达到意想不到的开发水平。

---

### [](https://polypane.app/blog/polypane-31-canvas-layout-elements-panel-improvements-and-chromium-155/)

**原文标题**: [Polypane 31: Canvas layout, elements panel improvements and Chromium 155 | Polypane](https://polypane.app/blog/polypane-31-canvas-layout-elements-panel-improvements-and-chromium-155/)

Polypane 31 是一次重大版本更新，核心亮点包括全新无限画布布局、Elements 面板增强、更多设备预设、性能监控、截图与录屏改进，并升级至 Chromium 155。

- 🧭 新增 Canvas layout：在无限画布上自由排列和缩放窗格，支持吸附、对齐、矩形创建窗格与缩略图导航。
- 📱 新增设备预设：iPhone 18 Pro、iPhone 18 Pro Max、iPhone Duo（折叠/展开）以及 5K 屏幕。
- 📊 新增每窗格 CPU 与内存性能监控，达到阈值时警告，帮助定位页面性能瓶颈。
- 🧩 Elements 面板支持跳转到自定义属性定义并一键返回，避免丢失样式编辑位置。
- 📐 新增 Flex item 可视化：展示基础尺寸、伸缩性、约束和最终尺寸，匹配约束时显示锁图标。
- 🖱️ 滚动调试增强：滚动元素时对应滚动徽章高亮，快速识别当前活动滚动容器。
- 🔍 Elements 面板支持在 DOM 树中搜索，并可在 Style 标签中过滤样式。
- 📸 截图改进：新增“可见工作区”截图，支持更广字符集，并提升高 DPI 截图可靠性。
- ♿ 支持每窗格独立页面缩放，便于并排测试 200% 和 400% 缩放等可访问性场景。
- 📦 下载体积约缩小 25%，启动加载更快。
- 🎥 视频录制改进：使用原生光标录制，并以 Mediabunny 替代 ffmpeg，视频处理更快。
- 🏷️ Meta 面板更新：不再警告缺少 `initial-scale=1`，显示 `llms.txt`，并遵循缓存设置请求 well-known 文件。
- 🧾 Console 面板优化：大型日志性能更好，控制台脚本错误记录更准确。
- 🔗 Outline 面板改进：用零数据 GET 复核 HEAD 误报，图片属性变更即时更新，并可控制隐藏元素显示。
- ⌨️ 多项体验优化：地址栏 Esc 行为更接近其他浏览器、清理 404 建议、崩溃覆盖层可禁用实验特性、Browse 面板支持缩放/认证/扩展安装、项目设置可复制、受限窗格显示锁图标。
- ⚙️ 基于 Chromium 155，并启用最新实验性 Web 平台特性。
- 💻 支持 Windows、macOS、Linux 的 64 位与 ARM 版本，自动更新，并提供 14 天免费试用。

---

### [](https://bsky.app/profile/matuzo.at/post/3mw65xm2co22o)

**原文标题**: [@matuzo.at on Bluesky](https://bsky.app/profile/matuzo.at/post/3mw65xm2co22o)

Manuel Matuzović 发帖称，征稿（CFP）还剩 10 天，目前只有 11 份投稿，但至少需要 24 份，因此呼吁大家分享投稿想法，并特别欢迎首次投稿的作者。
- ⏳ CFP 还剩 10 天开放。
- 📭 目前仅收到 11 份投稿。
- 🎯 目标是至少收到 24 份投稿。
- 📢 呼吁大家分享投稿想法。
- 🌱 特别欢迎首次作者投稿。
- 🕒 帖子发布于 2026-09-23T06:56:22.457Z。
- 🧩 原帖包含引用或其他嵌入内容。
- 💻 Bluesky 页面需要启用 JavaScript 才能使用。

---

### [使用 CSS 检测元素何时重叠](https://ishadeed.com/article/css-detect-overlap/)

**原文标题**: [Detect when elements overlap with CSS](https://ishadeed.com/article/css-detect-overlap/)

本节内容极为简短，仅包含一个章节标题和一段占位式文字，没有提供实质信息或关键结论。

- 📌 标题为“Section title”。
- 📝 正文只是模仿内容、仅供娱乐的占位文字。
- ⚠️ 文章未包含可提取的核心信息或有效观点。

---

### [](https://developer.chrome.com/blog/connection-allowlist-announcement)

**原文标题**: [Connection allowlists: Secure your web application's network access  |  Blog  |  Chrome for Developers](https://developer.chrome.com/blog/connection-allowlist-announcement)

Chrome 152 推出 Connection allowlists，让浏览器成为网络连接守门人，通过 `Connection-Allowlist` 响应头为文档和 Worker 设置默认拒绝的端点白名单，防止第三方脚本或 AI 生成代码将敏感数据外泄到未授权服务器；可与 CSP 搭配，支持报告模式、重定向/WebRTC 显式放行，并已在 Chrome 152 正式可用。

- 🛡️ Chrome 152 引入连接允许列表，为文档和 worker 建立严格网络沙箱，控制页面可通信的端点。
- 🌐 现代 Web 应用常集成第三方脚本和生成式 AI 动态代码，增加数据外泄风险，需要显式网络边界。
- 🚫 CSP 擅长控制加载/执行，但不适合限制通信目的地，且覆盖不全，如 DNS 预取、导航、WebRTC。
- ⚙️ 通过 `Connection-Allowlist` HTTP 响应头，使用 URLPattern 语法指定允许的 URL 模式，浏览器默认拒绝未匹配连接。
- 🧩 策略按每个 window 或 worker 上下文独立生效；`response-origin` 可动态加入响应来源。
- ⚠️ 建议将不可信代码隔离在跨源或沙箱 iframe，并仅对该 iframe 应用头，避免绕过和误伤可信请求。
- 🔁 默认阻止重定向和 WebRTC；可用 `redirects=allow; webrtc=allow` 显式放行。
- 📊 支持 `Connection-Allowlist-Report-Only` 报告模式，配合 `Reporting-Endpoints` 监控违规而不阻断服务。
- 🎯 典型场景：保护生成式 AI 执行环境、监督第三方脚本/游戏、为敏感架构设置严格网络边界，并可作为 CSP 的渐进增强。
- 🧪 Chrome 152 起正式可用；开发时配置本地服务器发送头，并在 DevTools 的 Network/Issues 面板测试和排查。
- 📚 可参考 Connection Allowlists 规范、WICG GitHub 仓库和 ChromeStatus 页面。

---

### [](https://master.dev/courses/codex/?utm_source=email&utm_medium=frontendfocus&utm_content=codexcooper)

**原文标题**: [Build Ambitious Interfaces with OpenAI Codex | Master.dev](https://master.dev/courses/codex/?utm_source=email&utm_medium=frontendfocus&utm_content=codexcooper)

这是一门免费的 OpenAI Codex 前端开发课程，帮助学习者用智能体编码更快构建现代前端界面，涵盖从配置 Codex、规划与构建 UI、视觉反馈与验证，到部署到 ChatGPT Sites 的完整工作流；含 22 节课、约 3.4 小时、4.5 评分和完成证书。

- 🎓 免费 Codex 课程：用 OpenAI Codex 更快构建宏大、现代的前端界面。
- 🤖 前端开发已因智能体编码而改变，需为 Codex 配置合适模型、推理强度、项目上下文、插件、技能和浏览器工具。
- 🛠️ 通过结构良好的 Agents.md 文件，让 Codex 获得高效工作所需上下文。
- 🎯 通过目标设定、明确 UI 测试和迭代反馈，指导并控制 Codex 构建与验证 UI。
- ⚡ 用技能、插件和自动化，把团队前端工作流变成可重复流程，稳定产出组件和功能。
- 🚀 可直接从 Codex 部署到 ChatGPT Sites，轻松分享 UI 项目。
- 📚 课程包含 22 节课、约 3.4 小时、4.5 评分、完成证书，并可自定进度学习。
- 🧠 学习内容涵盖从想法到应用、视觉反馈、App Shots、标注、技能引用、测试策略和 Living Frontends。
- 👩🏫 讲师 Katia Gil Guzman 是 OpenAI 开发者体验工程师，曾任职 Microsoft Azure Cognitive Services、Stripe 等。
- ✅ 先修要求：了解提示词，并具备基础软件开发经验。
- 🗂️ 课程模块包括介绍、Codex 概览、Sites 构建、3D/动画/交互、现有代码库、Living Frontends 和总结。
- 🎥 平台支持笔记、测验与闪卡、进度保存、完成证书、免费终身访问，且无需信用卡。

---

### [Interop 2027 及未来](https://olliewilliams.xyz/blog/interop-and-beyond/)

**原文标题**: [Interop 2027 and beyond](https://olliewilliams.xyz/blog/interop-and-beyond/)

本文作者列出了自己为 Interop 2027 投票的 Web 功能排名，并补充了一份因过于早期、尚不适合进入 Interop 2027 的“Pre-op”愿望清单，涵盖表单控件、暗色模式、动画图像、DOM 模板、锚点定位、Open UI、JavaScript Signals、Temporal 等方向。最后调侃：这些做完后，互联网就算完成，浏览器工程师可以专心修 bug。

- 🧼 Interop 2027 投票首选包括 Sanitizer API、新 HTML setter/streaming 方法，以及 `moveBefore()`。
- 🎞️ 视频与图像互操作重点：VP9 透明度、动画 AVIF、AVIF 互操作性改进，以及 JPEG XL 和 AVIF 的渐进式渲染支持。
- 🎨 CSS 相关诉求包括：SVG 链接参数、`focusgroup`、取消 `box-decoration-break` 前缀、块布局支持 `justify-self`、`AccentColor` 反映 `accent-color`、gap decorations、`flex-wrap: balance`、响应式 iframe、按钮/输入框的 `align-content` 居中、`grid-lanes`（Masonry 布局）和 Speculation Rules API。
- 📝 Pre-op 愿望清单第一项是 `appearance: base` 与整个 CSS Forms 规范，让原生 HTML 表单控件可被样式化；Chromium 已开始早期实现。
- 🌙 暗色模式标准仍不完善：Web Preferences API 可能不会实现；`<meta name="color-scheme">` 应影响 `prefers-color-scheme`，但尚无浏览器实现，可给相关 Chromium issue 点赞。
- 🖼️ CSS `image-animation` 希望提供对动画图像（“gif”）的更多控制；Chrome Canary 已在 flag 后实现。
- 🧾 表单与模板方面：希望 HTML 表单支持 PUT、PATCH 和 DELETE；DOM Templating API 仍需大量工作。
- ⚓ 锚点定位需要更好控制：为使用锚点定位的元素添加动画时，希望能根据锚点位置改变 `transform-origin` 和 `translate`。
- 🧩 其他早期提案包括：Persistent Widgets、Open UI 正在推进的新菜单元素、JavaScript Signals（仍卡在 stage 1），以及 `<input type="date">` 对 Temporal 的支持。
- 😄 作者结尾表示：做完这些，互联网就完成了，浏览器工程师可以花余生专心消灭 bug。

---

### [](https://github.com/web-platform-tests/interop/issues/1336)

**原文标题**: [Web Sanitizer API · Issue #1336 · web-platform-tests/interop · GitHub](https://github.com/web-platform-tests/interop/issues/1336)

Web-platform-tests/interop 的公开议题 #1336 提议将 Web Sanitizer API 纳入 Interop 2027，核心是 setHTML() 与 Document.parseHTML()，用于安全插入和解析 HTML 以防 XSS；该提案获 WebKit 积极标准立场，Chrome/Edge 146 与 Firefox 148 已支持，并具较高社区热度，目前在 Interop 2027 项目中状态为 Todo。

- 📌 议题位于 web-platform-tests/interop 仓库，编号 #1336，由 o-t-w 于 2026年9月3日创建，当前开放。
- 🛡️ 提案聚焦 setHTML() 和 Document.parseHTML()，分别用于防 XSS 地插入 HTML 与解析/净化 HTML 字符串。
- 🗳️ 另有 HTML setter methods 和 streaming methods 的独立 Interop 提案，发起者呼吁一并投票支持。
- 📚 规范见 WHATWG HTML Sanitization；功能说明见 web-features Sanitizer；测试见 wpt.fyi/results/sanitizer-api。
- 🌐 WebKit 标准立场为 positive；Chrome/Edge 146 与 Firefox 148 起已支持该功能。
- 📈 社区信号包括推文 445 赞、Bluesky 203 赞、开发者信号库 79 票，在 358 个功能中排第 11。
- 🏷️ 标签为 focus-area-proposal / Focus Area Proposal，已纳入 Interop 2027 项目，状态 Todo。
- 📊 仓库公开指标：525 stars、36 forks、170 issues、5 pull requests，另有 Actions、Projects、Security 等栏目。
- 🧾 元数据：无 assignee、无 milestone、无关联关系、无开发分支或 PR；更改通知需登录。

---

### [](https://github.com/web-platform-tests/interop/issues/1348)

**原文标题**: [HTML `focusgroup` · Issue #1348 · web-platform-tests/interop · GitHub](https://github.com/web-platform-tests/interop/issues/1348)

该 issue 提出为 HTML 增加原生 `focusgroup` 属性，以替代各 UI 库重复实现的 roving tabindex，为工具栏、标签页、菜单、列表框、单选组等提供方向键导航、单一 Tab 停靠点和焦点记忆；Chrome 150 已支持，规范提案见 WHATWG HTML，并已纳入 Interop 2027 待办。

- 📦 仓库/Issue：web-platform-tests/interop 的 #1348，标题为 HTML focusgroup，状态 Open。
- 🏷️ 标签：focus-area-proposal（焦点领域提案）。
- 💡 核心提案：`focusgroup` 是拟议 HTML 属性，用于替代手写“roving tabindex”逻辑。
- 🧭 使用方式：在容器上设置如 `focusgroup="toolbar wrap"`，即可让子项支持方向键/箭头键导航。
- 🎯 主要能力：提供单一保证的 Tab 停靠点、记住上次焦点项，无需 JavaScript；选择状态仍由作者负责。
- ✅ 浏览器支持：Chrome 150 已支持。
- 📜 规范链接：WHATWG HTML 提案 whatwg/html#11723；web-feature 为 focusgroup。
- 🧪 测试位置：WPT 的 `html/interaction/focus/focusgroup`。
- 🌐 其他信号：Mozilla、WebKit 标准立场仓库及 Web Platform DX 开发者信号。
- 🗂️ 项目状态：Interop 2027，状态 Todo；无 assignee、milestone，暂无关联分支或 PR。

---

### [](https://github.com/web-platform-tests/interop/issues/1445)

**原文标题**: [CSS Grid Lanes · Issue #1445 · web-platform-tests/interop · GitHub](https://github.com/web-platform-tests/interop/issues/1445)

该议题来自 web-platform-tests/interop 公开仓库，提议将 CSS Grid Lanes 作为互操作重点领域；它是一种 CSS Grid 容器的一维网格布局模式，并附有规范、Web 特性、测试与浏览器实现链接。

- 📌 议题 #1445「CSS Grid Lanes」开放中，由 colelao 创建，标签为 focus-area-proposal。
- 🧩 CSS Grid Lanes 是 CSS Grid 容器的一维网格布局模式。
- 📄 规范：https://drafts.csswg.org/css-grid-3/
- 🌐 Web 特性：https://web-platform-dx.github.io/web-features-explorer/features/grid-lanes/
- 🧪 测试：wpt.fyi 的 css/css-grid/grid-lanes，含 experimental、master、aligned 标签。
- 📣 附加信号：开发者兴趣 web-platform-dx/developer-signals#308；规范议题 w3c/csswg-drafts#945、#9041。
- 🧭 浏览器实现：Chromium issues 343257585、40128480；Mozilla bug 1981604；WebKit 博客介绍 CSS Grid Lanes。
- 🗂️ 元数据：无负责人、无类型、无里程碑；项目 Interop 2027 状态 Todo；无关联、分支或 PR。
- 📊 仓库概况：web-platform-tests/interop 公开，525 Star、36 Fork、170 Issues、5 PR。
- 💬 需登录才能更改通知或评论，当前 reactions 不可用。

---

### [使用 CSS 提取网格信息 – Master.dev 博客](https://blog.master.dev/extracting-grid-information-using-css/)

**原文标题**: [Extracting Grid Information Using CSS – Master.dev Blog](https://blog.master.dev/extracting-grid-information-using-css/)

本文介绍如何仅用 CSS 从 Grid 布局中提取列数、行数以及每个网格项的列/行起止位置；即使项目随机放置并可跨多行多列，也能通过自定义属性、容器查询和滚动驱动动画实现，目前完整支持主要限于 Chrome 和 Edge。

- 🎯 核心目标：不依赖 JavaScript，提取 Grid 的列数、行数，以及每个项目的列开始/结束、行开始/结束位置。
- 📊 基础网格：当每个项目只占一行一列时，可用 `round()`、`sibling-count()`、`sibling-index()` 等函数计算列数、行数和坐标。
- 🧱 复杂网格：项目可随机放置并跨多列/多行，坐标不再均匀，需要追踪项目四条边对应的网格线位置。
- ⚙️ 网格配置：要求列等宽、行等高，用 `--c`、`--r`、`--g` 控制列宽、行高和间距；列数可由 `100cqw` 计算，行数需要容器高度 `--h`。
- 🌀 关键技术：使用 Scroll-Driven Animations 的 `view-timeline` 跟踪项目在 x/y 轴上的起始边和结束边，并借助 `entry-crossing` / `exit-crossing` 调整 `animation-range`。
- 🧮 位置计算：关键帧让变量从 `1` 动画到 `0`，再用 `round(var(--x) * (n - 1) + 1)` 等公式换算成列起止；行位置同理，使用 `--r` 和 `--m`。
- 🔒 注意事项：网格容器需设置 `overflow: hidden` 作为滚动容器，`timeline-scope` 用于限制时间线作用域，避免命名冲突。
- 📏 容器高度难点：在 `height: auto` 下无法直接用 `100cqh`，文章用伪元素、`1px` 高度和 `view-timeline` 的 hack 方式获取容器高度 `--h`。
- 🧠 结论：现代 CSS 已能完成复杂的布局计算，但需要更新思维模型；该纯 CSS 方案可动态适应项目增删、位置变化和尺寸调整。

---

### [接口 › 速查表](https://interfaces.dev/cheat-sheet)

**原文标题**: [Interfaces › Cheat Sheet](https://interfaces.dev/cheat-sheet)

界面设计速查表，涵盖用户界面、动画、排版、颜色、无障碍、布局与文案写作等核心原则，旨在帮助设计师与开发者打造精致、易用的产品界面。

- 🎯 **同心圆角**：嵌套元素时，外圆角 = 内圆角 + 间距，保持圆角同心。
- 👁️ **视觉对齐优先**：视觉对齐比几何对齐更重要，人眼感受比精确计算更关键。
- 🔘 **图标按钮内边距**：带图标和文字的按钮，图标一侧的内边距应略小。
- 🌑 **层叠阴影代替边框**：用分层 box-shadow 营造深度感，而非使用边框。
- 🖼️ **图片描边**：给图片加 1px 描边并偏移 -1px，浅色模式黑色 8% 透明度，深色模式白色 8%。
- ✏️ **图标描边匹配文字**：图标的描边粗细应与旁边文字一致。
- 🎬 **动画从触发点开始**：根据触发位置设置 transform-origin，而非从中心开始。
- ⚡ **常用菜单跳过开启动画**：频繁打开的菜单只做关闭动画，开启时直接显示。
- 🌫️ **退出动画更含蓄**：退出时移动距离更短，配合透明度与 4px 模糊渐隐。
- 🎛️ **指定具体过渡属性**：明确写下要动画的属性，永远不要用 transition: all。
- 🔽 **按钮按下缩放**：按下时缩放至 0.95–0.98，用 transition: scale 200ms ease-out。
- 🔄 **图标切换淡入淡出**：新图标从 scale 0.25 → 1、opacity 0 → 1、blur 4px → 0，旧图标反向。
- 🧩 **交互用 CSS 过渡**：需要中途改变方向的交互用 transition，仅运行一次的序列用 keyframes。
- 🌗 **切换深浅色时禁用过渡**：避免主题切换时出现动画闪烁。
- 🌀 **防止元素抖动**：动画中元素随机偏移 1–2px 时，添加 will-change: transform（iOS Safari 尤其有用）。
- 📦 **分组进入动画**：元素入场时分小组依次出现，而非整块一起动画。
- 🚫 **避免页面加载动画**：除非有意为之，否则阻止元素在页面加载时播放动画。
- ⚡ **常用交互保持即时**：悬停变色等高频交互应瞬间或极快响应。
- 📄 **使用 .woff2 字体**：网页字体只用 .woff2，避免 .ttf 与 .otf。
- 🔢 **等宽数字**：计时器、计数器、价格和表格使用 font-variant-numeric: tabular-nums，防止数值变化时布局跳动。
- 📏 **控制行宽**：文章等长文本每行保持 60–75 个字符，过宽难以阅读。
- ⚖️ **文本换行优化**：标题用 text-wrap: balance，描述用 text-wrap: pretty 防止孤字。
- 🔗 **长内容不溢出**：用 overflow-wrap: break-word 处理长词与链接，用 white-space: nowrap 防止标签换行。
- 🔍 **字体平滑**：在根布局设置 -webkit-font-smoothing: antialiased 和 -moz-osx-font-smoothing: grayscale，让文字更锐利。
- 🔤 **正常大小写书写**：文字用正常大小写书写，需要大写或小写时使用 text-transform。
- ✒️ **智能标点**：使用弯引号、短破折号（–）表示范围、长破折号（—）表示插入语、省略号（…）。
- 🖊️ **下划线避让**：使用 text-underline-position: from-font 与 text-decoration-skip-ink: auto，避免下划线穿过 g、y 等字母尾部。
- 💬 **省略号补充完整内容**：文字被省略号截断时，通过 tooltip 或展开视图让用户看到全文。
- 🎨 **色阶各有用途**：调色板每一步都应有明确用途（页面背景、悬停、边框、实色填充、正文），不要添加无用的色阶。
- 🏷️ **语义化颜色令牌**：组件使用语义令牌（如 --color-text-secondary），而非原始色值（如 --blue-500）。
- 📛 **按用途命名颜色令牌**：用 --color-accent-solid 而非 --color-blue-button 或 --color-sidebar-gray。
- 🌟 **强调色专属品牌色**：accent 保留给品牌色，避免 primary 同时表示品牌色和正文主色。
- 🔲 **对比度以实际背景为准**：测量元素直接所在背景的对比度，而非页面背景。
- 🌙 **深色模式独立调色板**：为深色模式创建独立调色板，而非反转浅色模式。
- 🔀 **统一主题切换方式**：选择 prefers-color-scheme 或 .dark 类其中之一，不要混用。
- 🌈 **渐变混合模式**：用 in oklab 获得均匀亮度，in oklch 让中间色更鲜艳，in srgb 让中间色更柔和。
- 🧱 **使用原生 HTML 元素**：按钮用 <button>，链接用 <a>，原生元素自带无障碍与预期行为。
- 🎯 **使用 :focus-visible**：替代 :focus，不要在没有替代方案的情况下移除轮廓。
- ⌨️ **tabindex 仅用 0 和 -1**：正值会改变元素的预期顺序。
- 🖱️ **图标按钮加 aria-label**：仅有图标的按钮需有描述性 aria-label，可聚焦元素上不要加 aria-hidden="true"。
- 🖼️ **图片替代文本**：替代文本说明图片用途与内容，装饰性图片用 alt=""。
- 🏷️ **输入框使用可见标签**：用 <label> 标注每个输入框，并设置匹配的 type 与 inputmode。
- 📋 **不阻止粘贴**：用户需要粘贴密码和一次性验证码。
- ✅ **提交时校验**：提交按钮保持可用直到请求开始，用 aria-invalid="true" 标记无效字段，aria-describedby 关联错误信息，并将焦点移到第一个无效字段。
- 👆 **点击区域足够大**：至少 24×24px，触屏目标 44×44px，桌面 40×40px，且不可重叠。
- ✨ **装饰元素禁用指针事件**：光晕、渐变等装饰元素使用 pointer-events: none，避免吞掉事件。
- 🖐️ **悬停样式加媒体查询**：将悬停样式放入 @media (hover: hover)，避免触屏点击后 :hover 保持激活。
- 🎞️ **尊重减少动态效果**：将动画放入 @media (prefers-reduced-motion: no-preference) 中。
- 📢 **状态播报角色**：常规更新用 role="status"，紧急错误用 role="alert"。
- 🚦 **不只依赖颜色**：状态变化需配合图标、标签或下划线。
- ⏭️ **跳转内容链接置顶**：让“跳到内容”链接成为 Tab 键的第一站。
- 📌 **滚动边距**：用 scroll-margin-top 在标题上方留出空间，方便锚点跳转。
- 📐 **组间距是项间距两倍**：组与组之间至少留出组内项目间距的两倍。
- 🗣️ **按钮标签以动词开头**：如“保存草稿”“删除项目”，不要用“OK!”或“是”。
- 🧾 **确认按钮说明操作**：“删除项目”搭配“取消”，而非“是/否”。
- 🔁 **流程中步骤标签一致**：全流程统一使用“继续”或“下一步”。
- 🔗 **描述链接去向**：用“阅读文档”代替“点击这里”。
- 🔠 **大小写风格统一**：按钮、标题、标签在全站统一使用句式大小写（如“Save changes”）。
- 🔘 **开关标签说明开启行为**：写“发送已读回执”，而非“禁用已读回执”。
- 📭 **空状态给出指引**：说明此处应有什么，并提供一个起步操作。
- 🙋 **称呼读者为“你”**：用“你将收到邮件”，而非“用户将收到邮件”。
- 💳 **订阅方案**：月度 $7.99/月，年度 $79.99/年（节省 18%），终身 $299 一次性，均含新刊、资源库、交互演示、源码、Agent 技能与私密 Discord 社区。

---

### [Expo — 使用 React 构建原生应用](https://expo.dev/?utm_source=frontendfocus&utm_medium=email&utm_campaign=agentic-development)

**原文标题**: [Expo — Build native apps with React](https://expo.dev/?utm_source=frontendfocus&utm_medium=email&utm_campaign=agentic-development)

Expo 是面向移动端 AI 基础设施与 React Native 应用开发的一体化平台，覆盖开发、测试、构建、部署、更新和监控全流程，支持 Android、iOS 与 Web 单代码库，服务数百万开发者与大量生产应用。

- 🚀 Expo 提供完整工具链：Expo CLI、Expo SDK、MCP、Expo Go、Simulators、Launch、Build、Update、Hosting、Observe 等。
- 📱 开发者可用 Expo CLI、Skills 和 MCP 构建应用，用 Expo Go 真机测试，或用云端模拟器验证，无需 Mac。
- 🧪 测试能力面向团队与 AI Agent：云模拟器可自动运行应用、验证结果，并附带截图、录屏和日志作为证明。
- 📦 部署支持 TestFlight 与应用商店原生发布；Update 提供 OTA 更新、渠道控制和灰度发布。
- 📊 Observe 监控崩溃、性能指标和 Update 采用率，帮助在生产环境快速发现问题并发布修复。
- 🧩 Expo SDK 积累 10+ 年，提供 100+ 生产级 API，一次安装即可使用，并兼容 React Native、Swift、Jetpack Compose、Kotlin 等原生代码。
- 🌍 单代码库即可构建并发布 Android、iOS 和 Web；Update 能即时向所有用户推送修复与改进。
- 🤖 云模拟器可由编码 Agent 按需驱动，让 Agent 运行应用、验证自身工作并提交证据。
- ⚙️ Workflows 自动化构建、测试和发布；Launch 引导上架 App Store；平台内置监控与可观测性。
- 📈 关键规模数据：3M+ 开发者、50K+ GitHub stars、7M+ 周下载、100K+ 活跃开发者、500K+ 项目、100K+ 日构建。
- 💬 社区影响力：80% React Native 开发者选择 Expo，Discord 70K+ 成员，并获得大量开发者好评。
- 🔐 信任与合规：获 Meta 推荐、React Foundation 成员，符合 SOC 2 Type II、GDPR、CCPA，并支持 SSO。

---

### [自定义属性 polyfill](https://www.keithcirkel.co.uk/custom-attributes-polyfill/)

**原文标题**: [Custom Attributes polyfill](https://www.keithcirkel.co.uk/custom-attributes-polyfill/)

无法总结：未找到主要内容。

---

### [流体排版](https://blog.damato.design/posts/fluid-typography/)

**原文标题**: [Fluid Typography](https://blog.damato.design/posts/fluid-typography/)

视口单位让字体可随设备尺寸变化，但单独使用可能损害可访问性；作者建议用 `clamp()` 混合固定单位，并反对用容器查询控制字体大小，因为容器宽度任意且会破坏信息层级，流体排版仍应优先使用视口单位。

- 📏 视口单位的初衷：让字体大小能随设备尺寸自动调整。
- 🧮 在 `min()`、`max()`、`clamp()` 出现前，通常要用断点停止使用视口单位，改为固定字号，避免字体过大或过小。
- ✅ `clamp()` 简化了做法：可在一次赋值中同时定义最小值、首选值和最大值。
- ♿ 可访问性陷阱：只使用视口单位时，缩放级别和视口单位可能相互抵消，导致字体不尊重用户设置。
- 🔧 解决方法：将视口单位与固定单位混合，例如 `clamp(16px, 15px + 0.2vw, 18px)`；作者认为 `rem` 可能更合适，因为它关联用户的根字体大小。
- 🎥 Kevin Powell 发布了关于流体字体的视频，介绍用容器查询影响字号，并提到一些 CSS 冷门特性，值得一看。
- 🧭 作者曾考虑用容器查询做排版，但后来避免这样做，因为它会让信息层级难以理解。
- ⚠️ 示例中两张卡片的标题原本应同等重要，但容器查询会让较窄卡片中的标题变小，看起来像优先级更低。
- 🏷️ 若所有 `h2` 都受容器查询字号影响，它们可能显得不一致，甚至像不存在的更小标题级别。
- 🧩 与 `Mise en Mode` 的区别：那里可按密度有意缩放，同一密度区域仍保持一致；但容器查询中容器宽度可以是任意值，内容还可能反过来影响标题大小。
- 🎯 核心问题：不应由容器决定标题大小，而应由作者有意识地选择并应用字号。
- 📐 建议：流体排版继续使用视口单位，使相似版式中的变化保持一致，也兼容 `Mise en Mode`。
- 🧪 作者已有基于视口单位的标题方案，并期待 CSS 支持按单位数相除，同时催促 Firefox 支持相关能力。

---

### [阻止按钮在双击时触发缩放 - Piccalilli](https://piccalil.li/blog/stop-buttons-triggering-zoom-when-theyre-double-tapped/)

**原文标题**: [
  Stop buttons triggering zoom when they’re double tapped - Piccalilli
](https://piccalil.li/blog/stop-buttons-triggering-zoom-when-theyre-double-tapped/)

移动端快速双击按钮会误触发浏览器缩放；给按钮添加 CSS 的 `touch-action: manipulation` 可禁用双击缩放，同时保留正常的平移与捏合缩放。

- 📻 作者在 Barry Prendergast 的网页电台播放器上发现：手机上快速切台时，浏览器会放大缩小。
- 🔍 起初怀疑是 viewport meta 设置问题，但该页面已正确使用 `width=device-width, initial-scale=1.0`。
- 🚫 不要通过添加 `maximum-scale=1.0, user-scalable=no` 来阻止缩放，因为这会完全禁止缩放，违反 WCAG。
- 📱 真正原因是浏览器响应双击手势；在 iOS Safari 中，双击会放大被点击的按钮元素。
- 🧩 解决方案是一行 CSS：`.button { touch-action: manipulation; }`。
- 📖 根据 MDN，`touch-action: manipulation` 允许平移和捏合缩放，但禁用双击缩放等非标准手势。
- ⚡ 禁用双击缩放还能避免浏览器为生成 `click` 事件而延迟。
- 🔁 它等同于 `pan-x pan-y pinch-zoom`，后者出于兼容性仍然有效。
- 🧪 文中提供 CodePen 示例，对比未加和加上 `touch-action` 的按钮，可在触摸设备上测试。
- ✍️ 文章作者为 Andy Bell，发布于 2026 年 9 月 23 日，主题是 CSS。

---

### [别再像对待传统媒体查询那样对待 CSS 容器查询 — Smashing Magazine](https://www.smashingmagazine.com/2026/09/stop-treating-css-container-queries-traditional-media-queries/)

**原文标题**: [Stop Treating CSS Container Queries Like Traditional Media Queries — Smashing Magazine](https://www.smashingmagazine.com/2026/09/stop-treating-css-container-queries-traditional-media-queries/)

概述摘要
- 📊 CSS 容器查询浏览器支持率约 94%，但采用率低：86% 开发者知道，仅 41.4% 实际使用，常被误认为媒体查询。
- 🔍 媒体查询“向外看”：询问视口宽度，适合页面级宏观布局，如页头、页脚、主网格、系统偏好和设备能力。
- 📦 容器查询“向内看”：询问组件所在容器可用空间，适合卡片、表单、导航、小组件等微观/组件布局。
- 🧩 示例：同一卡片放在 1920px 视口的 300px 网格中，媒体查询会按视口触发导致变形；容器查询按父容器宽度判断，让组件适配实际上下文。
- ✍️ 流体排版：用 `cqi`、`cqw` 等容器单位配合 `clamp()`，让字号随组件容器缩放，而不是随视口变化。
- 🔄 Flex 换行检测：嵌套容器查询可借助 `flex-grow` 检测 flex 项是否换行，无需 JavaScript `ResizeObserver`，但并非万能。
- ⚠️ 注意事项：容器不能查询自身，通常需要额外包裹层；查询 `size` 可能因忽略子元素而高度塌陷，优先用 `inline-size`。
- 🚫 限制：容器查询不能直接用自定义属性作为查询条件，因为变量级联可能与查询逻辑互相影响。
- 🧭 选择原则：页面级、只受视口影响时用 `@media`；可复用组件、会出现在多种上下文中时用 `@container`，二者互补而非替代。
- ✅ 结论：容器查询不是“新式媒体查询”，而是让组件根据自身容器和内容自适应；理解宏观/微观布局分工，才能真正用好。

---

### [组件测试：前端开发人员实用指南](https://storybook.js.org/blog/component-testing-a-practical-guide-for-frontend-developers/)

**原文标题**: [Component testing: a practical guide for frontend developers](https://storybook.js.org/blog/component-testing-a-practical-guide-for-frontend-developers/)

组件测试是在真实浏览器中隔离渲染单个 UI 组件，模拟用户交互并断言其渲染与行为是否正确的前端测试方法；它兼具单元测试的快速隔离和端到端测试的浏览器级保真度，适合覆盖组件的大量状态，并与单元、视觉、可访问性、E2E 测试共同组成完整策略。

- 🧩 定义：组件测试渲染单个组件，不启动整个应用；测试可像用户一样点击、输入、选择并验证组件响应。
- 🎯 定位：组件是前端开发的核心单元；组件测试在开发早期和日常流程中频繁进行，从原子组件到页面级组件都适用。
- 🧱 核心特征：隔离、范围灵活、真实浏览器环境、通常由构建组件的前端开发者编写和维护，而不是交给独立 QA 团队。
- 💡 为什么重要：它填补单元测试“保真度低”和 E2E 测试“慢、脆、贵”之间的空白，能快速可靠覆盖加载、错误、空状态、表单校验失败等难触发状态。
- 🧪 常用技术：渲染测试作为冒烟测试；交互测试模拟点击、输入、提交等行为；Mocking/Spying 模拟数据、网络请求和依赖并验证函数调用。
- 🛠️ 主要工具：Storybook 用 stories 同时做开发、渲染测试和交互测试；Vitest/Jest 提供测试运行与 mock；Testing Library 提供用户式查询；Cypress/Playwright 也有组件测试模式；Chromatic 提供视觉回归测试。
- 🧭 示例：EventForm 先做默认渲染测试，再用 play 函数测试空标题报错，最后 mock getUsers 并用 spy 验证 onSubmit 收到标题和邀请人。
- ⚖️ 与单元测试对比：单元测试验证纯逻辑、最快、Node 环境；组件测试渲染真实组件在真实浏览器中验证外观与交互，二者互补。
- 🔗 与集成测试对比：现代前端中，集成测试常被吸收到组件测试和 E2E 测试里；组件树一起测试可视为组件测试，前后端全栈流程则交给 E2E。
- 🌐 与 E2E 对比：E2E 覆盖完整用户旅程但慢、易波动、维护成本高；组件测试快、稳定、隔离，适合覆盖大量 UI 状态，E2E 只保留关键流程。
- 🤖 AI 时代：组件测试是 AI 代理的护栏，测试失败能给出具体错误供代理迭代修复；stories 还是结构化上下文，帮助代理复用现有组件和模式。
- ✅ 结论：组件测试不替代单元测试或 E2E 测试，而是补充它们；它有时被称为模块测试，是大多数 UI 测试的理想选择。

---

### [Transitions.dev：面向 AI 智能体的 UI 过渡效果](https://transitions.dev/)

**原文标题**: [Transitions.dev: UI transitions for AI agents](https://transitions.dev/)

Transitions.dev 是一个 UI 动效平台，将 AI 代理、43+ 精心制作的过渡动效库与工作流技能融为一体，帮助设计与工程团队提升界面动效质量。

- 🎯 核心定位：一个 UI 动效代理，背后由动效库支撑，专为改善界面动效而生
- 📚 动效库：内置 43+ 精心制作的过渡效果，开箱即用，可直接投入项目
- 🤖 AI 代理：Transitions Agent 可扫描代码库、评估动效质量并自动修复为 PR
- 📊 动效评分：一条命令即可对代码库动效打分（0–100），每个问题映射到对应修复配方
- 🧠 本地确定性运行：无需 AI、无需账户，运行结果可复现
- 🔧 修复方式：以 diff 形式呈现修复，支持"润色"（小改动）与"重构"（按真实配方重写），最终生成 PR
- 🚦 PR 门禁：Action 会为每个 PR 评分，动效质量下降时可阻止合并（如设定最低分 75）
- ✨ 动效示例丰富：涵盖卡片缩放、数字弹入、通知徽章、菜单下拉、模态框、面板展开、拖放物理、3D 倾斜、点赞粒子、骨架加载等
- 👨💻 作者：由 Jakub Antalik 创建
- 🎓 推荐学习：Emil Kowalski 的 UI 动画课程被高度推荐

---

### [](https://github.com/Jakubantalik/transitions.dev)

**原文标题**: [GitHub - Jakubantalik/transitions.dev: UI montion AI agent, a library of 43+ crafted transitions, a skill that fits your workflow. · GitHub](https://github.com/Jakubantalik/transitions.dev)

Transitions.dev 是一个交互式可复用 CSS 过渡集合，展示多种 UI 交互动效，并为每张卡片提供可直接复制到任意项目的便携 CSS 片段；仓库还包含 npm CLI、AI agent skill 与 Refine 实时调优工具。

- 🎞️ 每个卡片演示不同交互模式，如卡片缩放、数字弹入、通知徽章、文本切换、菜单下拉、模态框、面板揭示、页面并排、图标交换、成功勾选、头像组悬停、错误抖动等。
- 🧩 项目定位为 UI motion AI agent，包含 43+ 手工过渡的库与适配工作流的技能。
- 📋 复制按钮输出自包含 CSS：`:root` 自定义属性、`t-*` 命名空间类，以及 `prefers-reduced-motion` 降级保护，无需演示专属标记或尺寸。
- 📦 可通过 npm CLI 使用：`npx transitions-dev add card-resize`、`--free`、`list`、`login`、`add confetti-burst`；Pro 过渡需通过无密码浏览器设备流登录后拉取。
- 🔐 `cli/` 发布为公共 `transitions-dev` 包；旧名 `transitions-pro` 仅转发且无高级源码，Pro 配方从认证 API 获取。
- 🤖 同一批过渡被封装为 agent skill：`npx skills add Jakubantalik/transitions.dev`；技能源在 `skills/transitions-dev/`，含 `SKILL.md`、18 个逐过渡参考文件与 `_root.css`。
- 🔄 skill 由 `index.html` 生成，`npm run build` 通过 `build/extract.mjs` 解析模板并重建，确保与展示站同步。
- 🛠️ Refine 工具用 `npx transitions-refine live` 注入时间线与 Refine 面板及本地 relay，`--llm` 接入 Cursor CLI/LLM，`stop` 移除；也可在编辑器运行 `/refine live`。
- 📁 主要文件包括 `index.html` 展示页、`prototypes.html` 调参游乐场、`skill.html` 技能落地页、`example.html` 对比示例、`skills/`、`refine/`、`build/`、`assets/` 及 PWA/SEO 元数据。
- 🌐 本地运行：`python3 -m http.server 8765`，然后访问 `http://127.0.0.1:8765/`。
- ⚖️ 许可允许个人与商业项目无限使用、修改并发布；唯一限制是不得把库本身重新分发为竞争性过渡库/套件；CLI、agent、Refine 工具为 MIT。
- ⭐ 仓库公开：约 4.5k stars、188 forks、448 commits、4 issues、3 pull requests。

---

### [](https://markuplint.dev/)

**原文标题**: [Markuplint - An HTML linter for all markup developers. | Markuplint](https://markuplint.dev/)

Markuplint 是一款标记代码检查工具，支持规范一致性验证、自定义团队规则、设计系统结构校验、按选择器精细应用规则、多种模板与框架语法，以及 VS Code 实时反馈。  
- 🚨 一致性检查：依据 HTML 标准、WAI-ARIA 等规范校验标记，捕获浏览器静默忽略但辅助技术和搜索引擎可能发现的问题。  
- 🛡️ 自定义团队规则：可强制执行无障碍、安全、性能、命名规范等标准，让团队约定变成机器可检查的规则。  
- 📐 设计系统结构校验：验证组件属性、特性及父子关系，确保设计系统中的组件契约不被破坏。  
- 🆔 按选择器应用规则：通过 CSS 选择器、扩展伪类或正则表达式，对不同元素精细启用或调整规则。  
- 📝 超越 HTML：借助官方解析插件支持 JSX、Vue、Svelte、Astro、Alpine.js、HTMX、Pug、PHP、Smarty、eRuby、EJS、Mustache/Handlebars、Nunjucks、Liquid、Markdown、MDX 和 lit-html 等。  
- 🧩 VS Code 扩展：安装后无需项目配置，打开 HTML 文件即可获得实时输入反馈并开始检查。

---

### [发布 v5.0.0 · markuplint/markuplint · GitHub](https://github.com/markuplint/markuplint/releases/tag/v5.0.0)

**原文标题**: [Release v5.0.0 · markuplint/markuplint · GitHub](https://github.com/markuplint/markuplint/releases/tag/v5.0.0)

markuplint v5.0.0 是一次重大版本发布，核心在于规则系统重构、AST 大改、默认 ARIA 1.3、新增 Markdown/MDX 解析器，并移除旧 API、引入多项破坏性变更；全部 40 个已发布包同步升至 5.0.0。

- 🚀 v5.0.0 发布，包含 36 个提交，重点为 v5 规则系统重新设计与整体架构升级。
- 🧩 规则系统重构：`wai-aria` 拆分为细粒度 ARIA 规则，引入 `specConformance`、命名规则组与 `nodeRules`，并新增大量规则。
- 🌳 AST 大改：节点引用改用 UUID 的 `parentNodeUuid`/`pairNodeUuid`，移除对象引用；各框架解析器 token 属性简化。
- 📝 新解析器：新增 Markdown、MDX、tagged-template-literal 解析器；移除 `htmx-parser`，简化 `alpine-parser` 并提供迁移指南。
- ♿ 默认 ARIA 从 1.2 升至 1.3：加入 DPub ARIA 角色、上下文角色校验、generic-role 透明性，部分 ARIA 规则结果会变化。
- ⚠️ 破坏性 API：旧 v1 API 移除；`MLCore.verify()` 返回 `VerifyResult`；`RuleSeed.fix()` 改为 `report()` 内联修复回调；`autoLoad`、`getIndent()`、`getLine()`/`getCol()` 等移除。
- ⚙️ 配置变更：`--config` 不再隐式加载默认配置；`deepmerge` 改浅合并，数组规则值覆盖而非拼接；`ignoreOmittedElements` 默认 `true`；`invalid-attr` 移除废弃选项。
- 🛠️ 工具链与打包：ESLint/Prettier 替换为 oxlint/oxfmt；`@markuplint/spec-generator` 合并进 `@markuplint/html-spec`；VS Code 扩展改由 `markuplint` 发布者发布。
- 🆕 CLI/API/VS Code：实验性批量抑制、`--severity-deprecation`、`--show-config=details`、非致命解析错误分级；VS Code 支持 `workingDirectories` 等。
- 🐛 修复与规范数据：透明元素解析性能、heading-levels、表格对齐、ARIA 规则收紧；HTML Living Standard、MathML、SVG2 修正；URL、Srcset、MediaQueryList、MIME、BCP 47 校验增强。
- 📦 全部 40 个已发布包升至 5.0.0，覆盖核心包、配置预设、类型、选择器、文件解析器及所有框架解析器/规范包。
- 🔗 完整变更日志：`v4.18.3...v5.0.0`。

---

### [Markuplint 试炼场](https://playground.markuplint.dev/)

**原文标题**: [Markuplint Playground](https://playground.markuplint.dev/)

未提供可总结的文本内容，因此无法生成摘要。请补充文章正文后，我会按您的要求整理成中文要点。

- 📄 当前消息中缺少需要总结的内容。
- ✍️ 请将文本粘贴在“Use the following content:”之后。
- ✅ 收到内容后，我会输出概览摘要和带 emoji 的“-”项目符号要点。

---

### [让你的标志比白色更亮](https://www.soverybright.com/)

**原文标题**: [Make your logo brighter than white](https://www.soverybright.com/)

overview summary
- 🌐 这是一款免费在线工具，可将 logo 或文本的选定颜色转为 HDR JPEG，使其在 HDR 屏幕上比 #FFFFFF 更亮（最高约 7.5 倍），普通屏幕上仍是正常 JPEG，且不存储图像。
- 🖼️ 上传 PNG/JPEG/WebP，选择要发光的颜色，即可下载 HDR JPEG；无需付费，图像仅在内存处理。
- 🔆 HDR 屏幕上选定部分可亮至 #FFFFFF 的 7.5 倍；其他屏幕看起来是完美正常的 JPEG。
- 🧪 网络版使用 ISO 21496-1 gain-map JPEG；LinkedIn 版使用 BT.2100 PQ 与匹配 ICC；基础像素保持不变。
- ⚪ 亮度基准：SDR 白是屏幕常规最亮；HDR 白约 +2.9 档、~1,500 尼特，最高 7.5 倍。
- 🎨 示例：白色文字自动选白；白环 + 品牌蓝 #2f6bff 同时发光；深青底上的奶油色 #f5e9c8 也可被选中。
- 🌑 深色背景上的浅色/近白元素发光效果最好；暗色难以真正发光，增强后易呈泛白霓虹感。
- ⚠️ 仅在 HDR 显示器且支持 gain map/PQ 的软件中可见（Chrome 137+、Safari 26/iOS 26、Apple Photos、LinkedIn 应用）；其他平台会剥离或归一化，但文件仍正常。
- ✍️ 也适用于文字：CSS 尚不能直接写出比 #FFFFFF 更亮的颜色，但可用 background-clip:text 透过 HDR gain-map JPEG 绘制文字。
- 🛡️ 用 @media (dynamic-range: high) 和 @supports 限定 HDR；SDR、Firefox、打印保留普通颜色；注意 background-clip 裁剪和 ::selection 可读性。
- 🚫 filter: brightness() 无法突破 SDR 白色，因为页面在 SDR 中合成；只有 HDR 内容获得额外亮度。
- 📦 附 white-7.5x.jpg 色块（64×64、1.3 KB、7.5×、+2.9 档、~1,500 尼特）可下载或自制其他强度，并提供 CSS/HTML 示例。
- 👤 作者 Chris Bennett，可在 LinkedIn 关注；图像处理不存储。

---

### [soundcn - 面向现代 Web 应用的免费音效](https://www.soundcn.xyz/)

**原文标题**: [soundcn - Free Sound Effects for Modern Web Apps](https://www.soundcn.xyz/)

概述摘要
- ⚠️ 你尚未提供需要总结的正文内容，目前只看到“...”，因此无法生成摘要。
- 📄 请粘贴文章或文本内容，我会按要求提炼中文要点。
- ✅ 收到内容后，将用“- + 合适 emoji”列出核心信息、关键结论与重要细节。

---

### [](https://github.com/kapishdima/soundcn)

**原文标题**: [GitHub - kapishdima/soundcn: 700+ curated UI sound effects for modern web apps. Browse, preview, and install sounds with a single command. Free and open source · GitHub](https://github.com/kapishdima/soundcn)

soundcn 是由 kapishdima 维护的开源项目，提供 700+ 精选 UI 音效，可通过 shadcn CLI 一键安装；每个音效都是内联 base64 的独立 TypeScript 模块，并附带基于 Web Audio API 的零依赖 `useSound` 钩子，用于快速为 React/Web 应用添加点击、通知、转场和游戏音效。

- 🎧 仓库为公共开源项目，MIT 许可证，约 797 stars、34 forks、1 issue、158 commits。
- 🧩 目标是解决网页添加音效繁琐的问题：找素材、处理授权、加载音频或引入重型库都很麻烦。
- 📦 提供 700+ 短音效注册库，涵盖点击、通知、转场、游戏音效等。
- ⚡ 安装命令示例：`npx shadcn add @soundcn/click-soft`。
- 🛠️ 每个音效是自包含 TypeScript 模块，使用内联 base64 data URI，无外部文件、运行时请求或 CORS 问题。
- 📁 音效会复制到代码库中，而不是作为依赖安装。
- 🪝 内置 `useSound` 钩子，基于 Web Audio API，零依赖。
- 🚀 使用流程：在 soundcn.xyz 浏览音效，安装后导入音效与钩子并调用 `play()` 播放。
- 🌐 官网/预览：soundcn.xyz；项目简介为“700+ curated UI sound effects for modern web apps”。
- 📜 多数音效来自 CC0 授权合集，主要来自 Kenney。
- ⚠️ 《魔兽世界》合集 110 个音效为版权例外，归 Blizzard 所有，非 CC0/自由授权，仅限非商业、教育和参考用途；项目与 Blizzard 无关联。
- 💰 赞助商之一为 Shadcnblocks.com，提供 2000+ Shadcn UI Blocks。

---

### [](https://jobs.fidelity.com/en/technology-careers/?utm_source=javascript&utm_medium=paidsocial&utm_campaign=jobssocial&utm_content=awn-tech-sl4-txt)

**原文标题**: [Technology careers at Fidelity | Fidelity Careers](https://jobs.fidelity.com/en/technology-careers/?utm_source=javascript&utm_medium=paidsocial&utm_campaign=jobssocial&utm_content=awn-tech-sl4-txt)

Fidelity 科技职业页面介绍其技术团队如何以创业心态和财富500强基础推动金融创新，并邀请人才加入，通过招聘职位、技能方向、学习支持和更多技术/加密职业信息展示发展机会。

- 🚀 使命：推动有影响力的创新，打造未来金融科技，重新定义金融未来。
- 🏢 文化：兼具初创公司心态与财富500强平台，持续投资创新并兑现数字化未来。
- 👩‍💻 团队：拥有大量技术专家；页面展示技术人员数量、2023年员工新/扩展角色比例及美国专利等数据。
- 🎥 员工体验：视频中全栈工程师 Monica 表示，Fidelity 最棒之处是人与人之间的互动。
- 💼 热招职位：包括 Defined Benefit Configuration Analyst（肯塔基州卡温顿，现场）、Director, Product Management（新罕布什尔州梅里马克，现场）、Delivery & Systems Coordinator（得州西湖/肯塔基州卡温顿/罗德岛史密斯菲尔德，现场），均发布于9月30日，属技术类。
- 🔎 招聘提示：职位频繁更新；若暂无合适岗位，可加入人才网络并订阅职位提醒。
- 🛠️ 技能需求：软件工程、全栈工程、云工程、数据可视化、人工智能与机器学习、架构、系统工程、系统分析。
- 📚 学习发展：技术人员每周有专门学习时间，可用于在线课程、职业辅导、导师跟岗等。
- 🌐 更多信息：可了解技术职业类型、福利和播客，也可探索 Fidelity 的加密货币职业历史与招聘领域。
- 📍 求职入口：可按技能与地点搜索职位，查看所有技术岗位。

---

### [JavaScript 周刊](https://javascriptweekly.com/)

**原文标题**: [JavaScript Weekly](https://javascriptweekly.com/)

这是一份名为 JavaScript Weekly 的 JavaScript 主题通讯，专注汇总文章、新闻和有趣项目；自 2010 年 11 月起已累计 804 期并持续更新，提供订阅、最新一期、全部期数与 RSS 等入口，同时重视隐私、反垃圾邮件和 GDPR 政策，并声明与 Oracle 无隶属或背书关系。

- 📰 JavaScript Weekly 是一份汇总 JavaScript 文章、新闻和酷项目的通讯
- 🗓️ 自 2010 年 11 月起已发布 804 期，且仍在继续更新
- 🔗 提供订阅、最新一期、全部期数和 RSS 等访问方式
- 🔒 明确重视隐私、反垃圾邮件和 GDPR 政策
- ™️ 指出 JavaScript 是 Oracle 在美国的商标，但该通讯与 Oracle 无背书或关联

---

### [](https://bastardica.mitpit.com/)

**原文标题**: [Bastardica](https://bastardica.mitpit.com/)

Bastardica 是一个在浏览器中运行的“杂种网页字体”铸造工具，可混合、拉伸或挤压不同字体，并导出为普通 OpenType 字体。

- 🛠️ 选择基础字体与混入字体，支持上传字体及多种随机化操作。
- 🎲 点击按钮可将所有 Google Fonts 加入下拉菜单；另有 UNCUT、Velvetyne、Font Squirrel、FontSpace、DaFont 等免费字体来源。
- ⚙️ 提供简单/高级模式、白/黑/浅/深主题、Y 偏移与缩放等效果，可添加多个混入字体。
- 👀 支持实时更新、预设加载、随机化全部字体和创建字体。
- 📦 输出格式包括下载 TTF、构建 OTF 和 WOFF2。
- 🌐 下载文件是普通 OpenType 字体；替换通过为所有脚本注册的 liga 上下文替换实现，浏览器默认启用。
- 💻 可用于浏览器、设计工具和打印；若字体未变化，请检查应用是否关闭了连字。
- 🔒 所有操作均在浏览器本地完成，使用 Pyodide 和 fontTools，字体不会上传。
- 🧩 技巧：用 Y 偏移和缩放让字形对齐；混合 3 种以上字体时按步长相交，首个字体优先且步长不中断。
- 🔢 建议用质数作步长，以减少混入字体碰撞。
- ⚖️ 混合字体会产生衍生作品，商业使用前需检查源字体许可；Bastardica 不附加条件，致谢可选。
- 💡 灵感来自 Times New Bastard 和 Easy Pete，可发邮件至 [email protected] 咨询。

---

