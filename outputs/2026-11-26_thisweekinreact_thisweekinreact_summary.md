# [This Week In React #307: Security, React Router, Next.js, TanStack Query, RTL, RTK, Styled Components, Talata, Pierre | Reanimated, Worklets, Expo, Skia, WebGPU, Unistyles, Legend List | TC39, Node.js, Parcel, Firefox, webpack, Nudeps | This Week In React](https://thisweekinreact.com/newsletter/307)

### [CodeRabbit | 智能体开发的治理与控制](https://www.coderabbit.ai/?utm_source=newsletter&utm_medium=email&utm_campaign=creator_program&utm_term=twir&utm_content=ad-twir-002&ref=twir&dub_id=xM0UdDgkeVsYTu3k)

CodeRabbit 以 Agentic change management 为定位，面向编码智能体大量提交 PR 后团队难以验证、排优先级、理解、保障安全和测试的瓶颈，将 Review、Triage、Explain、Security、Verify 与 Slack 智能体整合为从想法到完成的变更管理闭环。页面强调共享代码上下文、与编码智能体回环修复、合并前后自动化以及客户成效数据，同时注明部分安全扫描和 Verify 内容为示例或演示数据。

- 🚀 **产品定位**：CodeRabbit 提出 Agentic change management，目标是在不牺牲质量、安全和控制的前提下缩短从想法到完成的路径；核心痛点是编码智能体以更快速度灌入大量 PR，超过团队验证、排序、理解、保护和测试的能力。
- 🧩 **自动审查**：CodeRabbit Review 自动审查每个 PR，提供可提交建议，例如在创建会话前检查刷新令牌是否过期并返回 `null`；页面展示与编码智能体 codex 的回环，codex 在 `9f2c4a1` 中修复缓存失效问题后，CodeRabbit 验证提交后清除缓存且回归测试覆盖失败路径。
- 🔄 **合并前后**：Pre-Merge Checks 在合并前执行描述、标题、docstring 覆盖率等检查；Post-Merge Actions 在合并后更新 changelog、通知发布频道、同步文档，并在失败时报告或创建后续 PR。Review 还支持从团队用法持续学习，以及 Quiet、Chill、Assertive 审查风格配置。
- 📊 **优先级**：CodeRabbit Triage 对 PR 打分、排序和路由，按业务价值优先、按风险分级，并自动分配合适审查者；示例用 `P0`、`P1`、`P2` 和每人每日容量组织队列，提供 Kanban 板帮助理解积压。
- 🧭 **变更解释**：CodeRabbit Explain 面向智能体代码的 PR 界面，用语义 diff、爆炸半径上下文和架构图解释大规模改动，目标是让团队在数分钟内理解上千行 diff，并基于上下文而非猜测批准变更。
- 🛡️ **安全扫描**：CodeRabbit Security 提供持续监控、AI Deep Scan 和依赖漏洞扫描，支持定时深度扫描与每个 PR 扫描，并通过 Verify & Repair 验证发现以减少误报后在 PR 中修复；示例显示 `axios` 的 `GHSA-4w2v-q235-vp99` 在 PR `#482` 被检出且有修复就绪，页面同时注明部分扫描分布为示例数据。
- 🧪 **功能验证**：CodeRabbit Verify 从代码库和 PR diff 生成用户旅程并对应用运行测试，失败时提供录屏、截图和日志，可把证据发给编码智能体修复；演示中结账场景 `SAVE20` 预期 `$80` 但示例扣款 `$100`，生成场景为 2 失败 1 通过，页面标注该测试运行为示意。
- 💬 **Slack 智能体**：CodeRabbit for Slack 复用代码库智能，支持规划、事件响应和分诊；它监控错误、部署告警和事件流，调查并建议修复，也能分诊支持案例并起草回复，还可在生成代码前帮助界定范围、假设和成功标准。
- 🧠 **共享上下文**：共享智能层包括 Codegraph 构建变更影响节点的确定性地图，自适应系统收集历史、文档和团队工作上下文，业务上下文引入 PRD、issue 和内部文档，审查生成结合智能体代码生成与探索、静态验证和分析，并用多模型与工具集成处理难题。
- 📈 **客户成效**：页面称已有 20K 客户、8.5M 仓库，是 GitHub 和 GitLab 上安装量最高的 AI App，并引用 NVIDIA CEO Jensen Huang 的使用评价；案例数据包括 70% 建议采纳率和每天 50 个 PR 节省 30% 时间（Writer）、30 天节省 100+ 审查小时且关键发现采纳率 65%+（Abnormal）、合并提速 70% 且审查循环减少 30%（Swiggy）、合并流程提速 40% 且潜在 bug 采纳率 70%（Clerk）。

### [GitHub - Pagepro/nexity：Nexity 是一个开源系统，用于在 Next.js + Sanity 上创建和发展 AI 原生网站。· GitHub](https://github.com/Pagepro/nexity)

Nexity 是 Pagepro 以 MIT 许可开源的一套基于 Next.js 与 Sanity 的 AI 原生网站启动与增长系统，面向每次网站改动都需要开发者参与的团队：它把设计系统、区块和 Sanity schema 交给 Claude Code、Codex、Cursor 等编码代理，让营销人员可用 AI 搭建新区块，再由开发者审核上线；仓库包含 base 起始模板、Meridian 演示站和 .agents 代理层。

- 🚀 **快速开始**：提供 base 与 theme-meridian 两个模板，可用 `npm create sanity@latest -- --template Pagepro/nexity/base` 创建无品牌起始项目，Meridian 模板用 `Pagepro/nexity/theme-meridian` 并运行 `pnpm seed`；要求 Node.js 22.12+ 与 pnpm 12.15（可 `corepack enable`），站点运行在 http://localhost:3000，Studio 在 /admin；在线演示为 https://meridian.nexity.build。
- 🧩 **代理层**：每个项目内置 .agents 代理层：`AGENTS.md` 规定架构、命令和分步清单，`DESIGN.md` 规定 token、区块解剖与规范，`BRAND.md` 规定受众、语气和文案；.agents/skills 以开放 Agent Skills 格式提供 project-setup、create-section、link-fix、generate-alts、sanity-optimizations 等技能，.agents/agents 提供只读审查器，create-section 会调用 styling-fidelity-reviewer、sanity-schema-reviewer、groq-parity-reviewer 和 link-reviewer，另有 Sanity 查询、图片、交付审计器与 alt-text-writer。
- 🎨 **页面构建**：两个模板约有二十多个现成区块，覆盖 hero、feature grids、bento grid、split sections、stats、pricing、comparison table、testimonials、FAQ、contact form、CTA 和 listings；区块共享可见性、明暗主题、分隔线和锚点 ID 选项；内容类型包括页面、博客、案例研究、播客、可复用库、共享/全局区块、页头页脚和站点设置。
- ⚡ **编辑发布**：Studio 嵌入同域 /admin，支持点击编辑可视化预览、实时草稿预览、发布时基于标签的重新验证而无需重建，以及为每个区块提供示例内容的 Sections Gallery；CMS 管理的重定向和重写约在发布两分钟后生效，支持模式、查询字符串透传和循环保护。
- 📈 **SEO 与 AI 可读**：每页支持 title、description、分享图、noindex/nofollow、canonical、hreflang，自动生成分享图、XML sitemap、由单个 `IS_INDEXABLE` 开关控制的 robots.txt 和 schema.org JSON-LD，并提供发布前 GROQ 检查；站点提供 `llms.txt`，任意 URL 追加 `.md` 可获 Markdown 页面。
- 🛠️ **技术栈**：base 是 pnpm monorepo：web/ 为 Next.js 16.4 应用（App Router、Turbopack、Tailwind CSS 4.3、TypeScript 7.0，内嵌 Sanity Studio 于 /admin），studio/ 为独立 Sanity Studio，schema 由 web/ 导入；版本下限包括 React 19.3、Sanity Studio 6.20、next-sanity 13.3、@sanity/client 8.11、Zod 4.6、Oxlint/Oxfmt 1.89/0.74、c15t 3.1、Resend 6.34；站点基础含 GDPR cookie consent、环境变量启用的 GTM、Resend 联系表单、Sanity CDN 图片优化和 PWA manifest，`sanity.blueprint.ts` 从环境变量配置 CORS 与重新验证 webhook。
- 🔄 **模板差异**：base 是无品牌基础，使用默认 Tailwind 调色板和 Inter，初始数据集为空并显示 Next steps 引导；theme-meridian 是虚构 B2B 品牌 Meridian 的演示站，含完整设计、产品 mock 和种子内容，通过 `pnpm seed` 导入；种子会用相同 ID 替换文档，需使用新数据集。
- ⚙️ **安装更新**：`pnpm agent:doctor` 检查 Node、pnpm、env、代理文件和客户端链接；`pnpm agent:install` 可修复 .claude 链接，并支持 `--clients claude,codex,cursor` 以链接 .cursor/skills；`pnpm agent:update --source <checkout> --dry-run` 可预览更新，`.agents/install-lock.json` 记录安装内容并在遇到用户改动时停止覆盖，安装器只读取该 checkout 中的文件，不下载也不执行其中代码。
- 💬 **营销技能**：仓库额外提供面向营销人员的只读技能 brand-kit、site-contradictions、blog-post-quality-review、internal-links 和 blog-post-update，适用于任意站点和 CMS，不在起始模板中；可安装为 Claude Code 插件 nexity-marketing-skills（`/plugin marketplace add Pagepro/nexity`，再 `/plugin install nexity-marketing-skills@nexity`），或使用 `npx skills add Pagepro/nexity`，并通过 marketing-setup 引导配置。
- ⚠️ **限制**：起始模板生成的是用户自有副本，不会自动跟随上游更新，需让编码代理挑选并应用提交，代理层可用 `pnpm agent:update --source <checkout>` 更新；模板仅支持单语言；newsletter 表单仅为 UI，未接邮件服务前不存储或发送地址；部分技能额外依赖 Chrome、Python Pillow 或 ImageMagick、具备写权限的 Sanity token；product-mock 仅在 theme-meridian 可用；生产环境只在 /admin 提供 Studio，3333 端口仅供本地。

### [概览 · remix-run/react-router · GitHub](https://github.com/remix-run/react-router/security)

React Router（remix-run/react-router）安全页面说明 8.x 与 7.x 仍获得安全更新，6.x 及以下不再支持；同时列出漏洞上报入口、修复与公告披露流程，以及 2026 年 7 月和 11 月发布的多项安全公告，涵盖 DoS、原型污染、XSS、CSRF 绕过和开放重定向等问题。

- 🛡️ **支持范围**：当前 8.x 和 7.x 获得安全更新，6.x 及以下不再受支持。
- 🔍 **漏洞上报**：通过 GitHub Security Advisory 的 Report a vulnerability 提交；团队会回复后续步骤，第三方模块问题应报给维护者或经 npm 联系表选择 I'm reporting a security vulnerability。
- 🗓️ **披露流程**：有效公告先进入 Draft 调查，提前通知常见托管平台，发布带修复的 React Router 版本并更新官方站点，通常最多约一个月后再公开公告；托管商可发邮件至 hello@remix.run 申请提前通知。
- ⚠️ **2026-11-18 公告**：发布 7 项：服务端路由发现 DoS（GHSA-2rq8-3rm6-2w8f，High）、数据反序列化原型污染（GHSA-qhgm-jj2j-75wj，High）、RSC 重定向 XSS（GHSA-mjj8-rxh9-q8f5，Moderate）、Node.js 请求处理 DoS（GHSA-mp5r-736v-j8x9，High）、路由匹配 DoS（GHSA-x8j4-g9rr-8j87，High）、服务端 actions CSRF 绕过（GHSA-8wpx-2pj4-ggvx，Moderate）、loader 与 action 响应开放重定向（GHSA-7m2v-44vx-v55w，Moderate）。
- ⚠️ **2026-07-22 公告**：发布 3 项：RSC 模式 CSRF 绕过可在 400 响应前执行 action（GHSA-qwww-vcr4-c8h2，Moderate）、开放重定向导致 XSS（GHSA-jjmj-jmhj-qwj2，Moderate）、`__manifest` 端点未认证 DoS（GHSA-chx6-hx7r-mcp5，High）。
- 📚 **公告列表**：页面显示公告分页为 Previous 1 2 3 Next，当前可见内容只是相关安全公告的一部分，完整信息可查 GitHub Advisory Database。

### [React2STEAL 利用 GitHub Actions 攻击 React2Shell | OpenSourceMalware](https://opensourcemalware.com/blog/react2steal-github-actions)

2026年11月18日披露的 React2STEAL 活动滥用被劫持的 GitHub 账号和 GitHub Actions，把公开仓库同时当作扫描器、React2Shell（CVE-2025-55182）与 Next.js 中间件绕过（CVE-2025-29927）的利用平台以及窃密数据外泄点；已发现45个 `ci-wk-<number>` 仓库、至少1,281个受害主机名，活动在11月17日仍约每11分钟提交新结果，且与 wfx-loot 活动共用大量账号，显示一次令牌失窃可能被持续复用。

- 🚀 **活动披露**：React2STEAL 被确认为端到端自动化攻击框架，不是供人安装的恶意 Action；45个仓库分布在44个所有者账号，按10月22日、11月11日、11月14日三波创建，可读取的34个有结果仓库合计1,281个唯一受害主机名、约1,100个域名；作者称在11月17日仍每11分钟提交新结果，`dascxzcw` 是最佳线索且账号已返回404。
- 🧩 **攻击流水线**：`scan.yml` 通过 `workflow_dispatch` 接收 `chunk` 主机列表，在 `ubuntu-latest` 上以 `contents: write` 和 `timeout-minutes: 350` 运行；它把列表分半，`prefilter_nextjs.py` 以400并发筛出 Next.js 目标，随后两个 `batch_output.py` 各以250并发利用，成功后在受害 Node.js 进程执行 `fast_recon.js`，最后由工作流执行 `git add/commit/push` 把结果写回公开仓库。
- 🎯 **漏洞基础**：两个目标漏洞均有修复版本：CVE-2025-55182 影响 React Server Components 19.0.0、19.1.0、19.1.1 和 19.2.0，因 Server Function 端点不安全反序列化导致预认证 RCE；基于这些版本的 Next.js 同样暴露。CVE-2025-29927 利用 Next.js 中间件信任 `x-middleware-subrequest` 内部头，可跳过包括认证在内的中间件检查。
- 🛠️ **利用细节**：`batch_output.py` 依次尝试7种 React2Shell 变体，包括 chunked 编码、8KB 填充前缀、随机 multipart boundary、Content-Type 前加空字节等，并用 `x-middleware-subrequest` 尝试中间件绕过；还通过 `/_next/image?url=http://169.254.169.254/...` 发起 SSRF，先取 IAM 角色名再取该角色的临时 AWS 凭证。
- 🔑 **窃密载荷**：`fast_recon.js` 有两个变体，收集进程环境、云凭证文件、Kubernetes token 和 `.env`；新变体额外回传完整 `.env` 和配置文件内容，单受害机上限300KB，某仓库143条受害记录中142条含此类文件。它按28个环境变量名在10家 AI 提供商中查找密钥，并用真实推理请求测试 OpenAI、Anthropic、Gemini 等服务，优先小模型且 `max_tokens` 为20，DeepSeek 与 OpenRouter 还会查余额；不驻留、不下载第二阶段载荷。
- 📦 **公开外泄**：窃密结果以明文、JSON 和 ZIP 三种格式提交到同一公开仓库，提交作者为 `w <w@w>`；在11个仍可访问仓库的快照中约有9,100个 ZIP、3,800个 JSON、3,000个明文记录，合计约7.4GB。Telegram 机器人配置硬编码在 `batch_output.py`，但 `SEND_TELEGRAM` 默认0且只发送小于50MB的 ZIP，因此公开仓库才是实际外泄通道，任何人都能读取赃物。
- 🗓️ **三波与时间线**：第一波10月22日02:05至02:13至少26个仓库，其中7个在10月28日停止扫描，22个后来出现 wfx-loot 探针；第二波11月11日04:15至04:16创建8个仓库，间隔约26秒，每个约90至100个受害主机，3个出现探针；第三波11月14日14:43至14:44创建5个仓库，仅预置相同1,845主机列表，无结果、无探针。代码注释日期从2026年9月10日到10月9日，均早于首批仓库，记录 Perplexity 密钥误判修复、45个已知漏洞主机评估、并发从250降至150再降至90等，但注释日期未经独立验证。
- 🔗 **关联活动**：wfx-loot 自11月10日起用数千被劫持账号窃取 CI secret；在39个可检查的 React2STEAL 仓库中，25个有 `wfx-docs` 分支和 `docs/wfx-audit.md`，其中24个与探针文件哈希 `ee6e5addfe591923fc385553cb66cf0d25634a6b` 一致；25/38 个所有者的仓库存在 wfx-loot 探针 PR，4人还有其他仓库的载荷阶段提交。两者共用账号且令牌未被及时吊销，但无共享代码、服务器 IP 或 Telegram 基础设施，运营手法也不同，无法判定同一或两个运营者。
- 🧪 **AI与ARTEX**：代码呈现 AI 编码助手参与痕迹：注释称人类为 `operator`、按日期记录修复和并发调整、写入 `marker_lift.py` 的测试表、在自身代码中给机器人名打码、输出含 emoji 以及使用大写强调和破折号。未发现 SentinelOne 列出的 ARTEX 痕迹，如 `artex-probe` 文件、`artex`/`artx` 字符串或 ARTEX 用户代理；脚本使用普通 Chrome UA，因此只能判断可能由 AI 辅助编写，不能归因到 ARTEX 或特定模型。
- 🛡️ **处置建议**：若运行 React 或 Next.js，应在请求和 WAF 日志中查找重复5次的 `x-middleware-subrequest` 头，以及指向云元数据地址的 `/_next/image?url=` 请求；命中后轮换该服务器进程可触达的所有密钥和配置，并将配置视为已泄露，审查 AI 密钥用量。边缘代理应剥离或拒绝该头，启用 IMDSv2 阻止 SSRF 读取实例凭证；使用 `NEXT_PUBLIC_OPENAI_API_KEY` 的应用应立即轮换，因为该变量会被构建进浏览器代码。
- 🔍 **GitHub狩猎**：排查 GitHub 时不要依赖 `ci-wk-<number>` 仓库名，应组合搜索 `batch_output.py`、`prefilter_nextjs.py`、`fast_recon.js`，以及 `wfx-docs` 分支、标题为「docs: dependency audit notes」的 PR 和哈希 `ee6e5...` 的 `docs/wfx-audit.md`；可用 `Capture FULL env vars for exploitation`、`VULNERABLE_TARGETS_FILE` 配合 `send_telegram_document`、`filename:scan.yml` 配合 `SCAN_REGISTRY_DB` 等代码搜索。匹配账号应按已失陷处理，吊销令牌和应用授权；CI runner 应限制出站流量；删除仓库不构成修复，克隆、fork、缓存和 Git 历史仍保留数据，所有暴露密钥都必须轮换。
- ⚠️ **证据边界**：作者未能确认运营者身份、账号令牌如何被获取，也未测试泄露凭证是否仍有效；1,281是未读取历史版本的下限，GitHub 提交搜索只覆盖默认分支且部分搜索报错。第三方 GitHub App OAuth 令牌泄露只是解释性假设，无证据；有一个账号还分别感染 PolinRider 和 GhostAction，说明凭证可能被多组攻击者重复利用。

### [为 next start 添加实验性 Go 前端服务器，由 jamiboym · 拉取请求 #101695 · vercel/next.js · GitHub](https://github.com/vercel/next.js/pull/101695)

Next.js 在 canary 中合入了为 `next start` 增加实验性 Go 前置服务器的 PR #101695，默认关闭；启用后，该 Go 程序接管公共端口，并把请求原样转发到私有回环端口上的 Node 服务器。该改动为后续逐步把路由等工作迁出 Node 建立 HTTP 前置层，并在 #102035 中更名为 Switchyard。

- 🚀 **实验合入**：#101695 合入 canary，为 `next start` 增加 Stage 1 Go 前置服务器；只有设置 `__NEXT_EXPERIMENTAL_FRONT_SERVER=1` 才启用，未设置时行为完全不变，后续 #102035 将环境变量改为 `__NEXT_EXPERIMENTAL_SWITCHYARD` 并统一更名为 Switchyard。
- 🧩 **核心机制**：Go 程序 `next-front` 监听 `next start` 的公共端口，把每个请求原样反向代理到 Node 在 `127.0.0.1` 上随机分配的私有端口，自身不做路由决策；Node 是父进程，启动前置服务器并等待 `NEXT_FRONT_READY <port>` 后打印 `Local:` 和 `Ready`，关闭时先停前置服务器再关 Node，前置进程退出则 Node 以 1 退出。
- ⚙️ **超时与转发**：Node 从私有 `http.Server` 读取 `keepAliveTimeout`、`headersTimeout`、`requestTimeout`，通过 `--listen`、`--upstream`、`--idle-timeout-ms`、`--header-timeout-ms`、`--request-timeout-ms`、`--upstream-idle-ms` 传入且 Go 端无默认值；代理保留 Host 和原始请求目标，补齐 `X-Forwarded-For`、`X-Forwarded-Port`，每次写入即 flush、不压缩；上传超时返回 408，完整上传前已作答的响应会带 `Connection: close`。
- 📦 **构建分发**：实验阶段 `next` 不随 npm 包发布前置二进制，需用 `__NEXT_EXPERIMENTAL_FRONT_SERVER_BINARY` 指定，或本地以 `NEXT_BUILD_FRONT_SERVER=1` 构建当前平台二进制（约 6 MB）；仅支持 linux 和 darwin 的 amd64/arm64，构建要求 Go 1.24+，其他构建不需要 Go；Windows、未知架构或缺二进制会报错退出。
- 🧪 **测试覆盖**：新增 CI 作业 `test-front-server-prod`，安装 Go 构建 `next-front`，在启用变量下重跑 start 模式路由门禁及 front-server 行为/进程两组测试；canary 每次推送运行，PR 仅在 front server 相关文件变更时触发，且当时未加入 `tests-pass`，不阻塞合并；需要真实前置的用例通过 `// @force-gate frontServerBinary` 跳过普通 prod 作业。
- ⚠️ **行为差异**：响应原因短语改用 Go 内置文案，自定义 `res.statusMessage` 不保留，例如 `400 Invalid JSON` 变成 `400 Bad Request`，Node 的 `413 Payload Too Large` 变成 `413 Request Entity Too Large`，状态码与响应体不变；`/%zz` 等畸形目标由 Go 先返回 400；绝对形式目标只把路径转给 Node 并用目标主机作 Host；无 Host 的 HTTP/1.0 请求回填公共地址；WebSocket 关闭不等待；响应头名规范化会改变 `rawHeaders` 大小写。
- 📈 **性能数据**：Apple M5 Pro、Node 24.22.2 基准显示，简单 route handler 并发 1 从 10,319 降至 6,582 RPS，p50 增加约 50 µs；并发 64 从 13,338 降至 11,655 RPS（−12.6%）；动态页面 2,708→2,709 RPS、流式页面 240→240 RPS 基本不变；`next-front` RSS 为 18–25 MB，Node RSS 约 385–510 MB 不变。
- 🛡️ **安全限制**：Node 的私有端口在同一台机器上可绕过前置直接访问；当前前置不做路由决策所以无害，但首个把决策移入前置的 PR 必须加 token；启用变量时 Windows 不支持，`next dev`、standalone `server.js` 和自定义服务器都不使用前置。
- 🔄 **更名与头限制**：#102035 将包路径、二进制名、环境变量、ready 行、测试和 CI 作业统一改为 Switchyard；同时向 Node 传递认证 TCP 对端元数据以恢复客户端 socket 身份，按客户端地址隔离上游连接池，并执行 Node 的 `--max-http-header-size` 等有效头部大小限制，配置预算为 4 KiB 或更小时会拒绝启动。
- 🧭 **route.go 直连栈**：#102101 已合入 route.go 直连栈的骨架：Node 向 Switchyard 发送精确路径路由表和 worker 上线/退出消息，但所有请求仍走 Node；后续 #102102、#102103、#102113 等逐步把查询串、动态段、catch-all、basePath、请求体、压缩等条件下可原样转发的请求直接发往 Go worker，部分 PR 仍为 Open/Draft。
- ⚡ **运行优化**：#101901 将 Go 代码默认线程上限设为 4，除非 `GOMAXPROCS` 显式设置为正数或 Go 默认已不超过 4；#101902 为代理响应复制加入 `sync.Pool` 复用 32 KB 缓冲区，归还时清零，降低 CPU 和 GC，内存约增加 1–3 MB。

### [Next.js 现已支持运行 Go：route.go 处理器、基准测试与限制](https://levelupgo.dev/blog/nextjs-go-route-handlers)

Next.js 16.5 canary 引入实验性的 Go Route Handler：在 App Router 中放置 `route.go`，用标准 `net/http` 签名导出 `GET`、`POST` 等函数，Next.js 将每个路由编译为独立原生二进制并由自身 Go 进程提供服务。该特性面向 CPU 密集型端点，让 React 前端继续使用 TypeScript，同时把慢接口迁到 Go，但仍处于 canary 阶段，构建、运行和部署限制较多。

- 🚀 **实验上线**：Next.js 16.5 canary 加入 `route.go`，PR #100130 于 2026-11-03 合并并随 `16.5.0-canary.40` 发布；`proxy.go` 在 `16.5.0-canary.53` 由同一开关启用。需在 `next.config.ts` 开启 `experimental.goRoutes`，API、文件布局和生成代码仍可能变化。
- 🧩 **标准处理器**：在 `app` 下放置 `route.go`，导出 `GET(w http.ResponseWriter, r *http.Request)`、`POST` 等函数；包名为 `main` 但无需写 `main()`，Next.js 构建时生成入口。函数名决定 HTTP 方法，签名就是 `http.HandlerFunc`，同目录其他 `.go` 文件属于同一 `package main`。
- ⚙️ **构建运行**：`next build` 将每个 Go 路由编译为约 9 MB 的原生可执行文件，位于 `.next/server/app/.../route-<hash>`；`next start` 不需要服务器安装 Go，但 dev/build 机器需要 Go 1.24+ 和 Turbopack，Webpack 构建不可用；Node 仍在前置接收请求并转发。
- 🧭 **路由取值**：动态段沿用方括号目录，用 `r.PathValue` 读取；catch-all 可用 Next.js 生成的 `ParamValues` 取得分段切片，能保留编码斜杠，例如 `ci%2Fcd` 在 `ParamValues` 中是 `ci/cd`，而 `PathValue` 返回整个 `ci/cd/deploy-go`。查询参数用 `r.URL.Query()`。
- 📦 **请求体**：用 `http.MaxBytesReader` 限制 JSON body，例如 1 MB；`errors.As` 检测 `*http.MaxBytesError` 返回 413，JSON 解析失败返回 400；表单用 `r.ParseMultipartForm` 与 `r.FormValue`。TypeScript 路由没有内置 body 大小限制，需要自行按块计数。
- ✅ **方法处理**：只导出 `GET` 和 `POST` 时，Next.js 自动补齐 HEAD（执行 GET 并丢弃 body）、OPTIONS（204 并返回 Allow）和未导出方法的 405；无需手写这些处理器。
- ⚡ **流式响应**：使用 `http.Flusher` 分块输出；对 `text/plain` 流必须加 `Cache-Control: no-transform`，否则浏览器带 gzip 时 Next.js 会压缩并缓冲，Chrome 中十个 200 ms 分块会最后一起到达；`curl -N` 因不请求 gzip 不受影响。也可全局 `compress: false` 或改用不被压缩的类型如 `application/x-ndjson`。
- 🧠 **进程内状态**：每个 Go 路由独立进程，首次请求时启动，包级变量仅在该进程存活；不同路由、不同 `next start` 实例之间不共享，编辑路由或进程重启会丢失，持久化仍需数据库或缓存。Go 以 goroutine 并行处理请求，计数器需 `sync.Mutex`；TypeScript 单线程无需锁。五个各睡 1 秒的请求总耗时 1.09 秒，说明并行。
- 🔍 **代理与头部**：Node 处理入站请求后通过本地连接转发，Go 中 `r.RemoteAddr` 是 `127.0.0.1:<port>`；客户端头、`proxy.ts` 设置的头和 `next.config` rewrite 均生效，但客户端伪造的保留头 `x-next-internal-go-token` 会被剥离。
- 🐛 **崩溃行为**：`panic` 被 `net/http` 恢复，只中断当前连接并由 Next.js 返回 500，进程和 PID 不变；`os.Exit` 会杀死 worker，下一次请求启动新进程和新 PID。处理器中应避免 `log.Fatal` 和 `os.Exit`，否则会清空内存状态。
- 🛠️ **构建限制**：构建不会下载 Go 模块或修改 `go.mod`/`go.sum`，需预先 `go mod download`，且不支持 workspace、`replace` 和 vendoring；`CGO_ENABLED=0` 使 cgo 包不可用；不支持交叉编译，需在目标 OS/CPU 上构建；不支持 `output: 'standalone'` 和静态导出，自托管要复制整个 `.next` 并保留可执行权限。
- 🛡️ **运行时限制**：构建不会追踪 Go 运行时打开的文件，读取文件需用 `go:embed`；不支持 WebSocket 升级和 HTTP trailer；Go 通过 `os.Getenv` 读取真实环境变量，`next.config` 的 env 内联不会传入。
- 📊 **基准结果**：在 Next.js `16.5.0-canary.40`、Go 1.27.1、Node 24.20 的 10 核 M2 Pro 上，50 并发时素数计数从 `route.ts` 的 8.5 req/s 提升到 89.9 req/s，p99 从 9.66 s 降至 1.18 s；销售报告从 10.8 提升到 70.9 req/s，p99 从 5.05 s 降至 2.11 s；Hello 从 5,448 提升到 8,985 req/s。canary.45 复测结果相同；50 并发报告路由中 Go 进程占用 595 MB，对比 Node 的 227 MB，TypeScript 单进程顺序处理时占用 326 MB。
- 🧪 **扩展性**：Go 单请求约 2 倍于素数、1.5 倍于报告；50 并发扩大到 10.6 倍和 6.6 倍，主要因为单 Node 进程只用一核而 Go 用满 10 核。`GOMAXPROCS=1` 时素数 17.6 req/s、报告 14.5 req/s；10 个 `next start` 的 TypeScript 进程可达 44 和 48.7 req/s，但内存约 1,170 MB 和 2,382 MB，仍落后于单 Go 进程。
- 🎯 **采用建议**：尚不适合生产，canary API 与构建输出可能变化且限制较多。现有 Next.js 应用若有少量慢且 CPU 密集的端点可尝试，基准显示约 7 到 10 倍吞吐；新应用仍建议独立 Go API；原型或小应用可用 Go 路由作为 React 与 Go 标准库同项目的折中。主要等待 I/O 的端点不会因 Go 明显加速。

### [🗺️ Query v6 路线图 · TanStack/query · 讨论 #12669 · GitHub](https://github.com/TanStack/query/discussions/12669)

TanStack Query 维护者 TkDodo 宣布启动 v6，主线不是大规模重写公开 API，而是借大版本清理内部实现、更新工具链与支持范围，并分项收集反馈；ESM-only、React 19 最低版本、微任务调度、必填 queryFn、哈希与相等性、streamedQuery 稳定化等已实现，gcTime 语义、queryOptions 下沉 core 仍在计划中，enabled 移除和服务端 gcTime 等仍在讨论，官方不承诺时间表。

- 🚀 **版本定位**：v6 已开工，但官方强调大版本用于破坏而非加功能，目前不计划大规模改写使用方式；开发分支为 `query-v6`，不做时间承诺，并会关闭未经沟通的全自动 PR。
- 📦 **仅发布 ESM**：放弃 CJS 和面向旧 webpack4 的 legacy 构建，简化构建并推动生态转向 ESM；状态为已实现。
- ⚡ **React 最低 19**：React 适配器最低要求提高到 v19，内部在 `useSuspenseQuery` 的 Suspense 集成中使用 `use()`，替代已弃用的 throw promise；状态为已实现。
- 🔄 **默认调度改微任务**：默认调度器从 `setTimeout(0)` 切换为 microtask，以获得更好的批处理效果，并缓解 await 失效后 setState 渲染旧 query 数据的问题；状态为已实现。
- 🛠️ **移除 v5 弃用 API**：删除 v5 标记弃用的接口，包括 query-core 的 `context.direction`、`isInitialLoading`、`queryClient.fetch/prefetch/ensure(Infinite)Query(Data)`、`queryObserver.getOptimisticResult`，solid-query 的 suspense option，sync-storage-persister，vue-query 的 Vue 2 via vue-demi，以及 devtools 的 styleNonce；状态为已实现。
- 🎯 **queryFn 必填**：`useQuery` 及框架适配器中的 `queryFn` 改为必填；需要全局默认函数时应显式传入导出的 `defaultQueryFn`，避免隐式依赖前一个组件渲染时提供的 queryFn；状态为已实现。
- 🧩 **全局 hashFn 与 equalityFn**：用 QueryClient/QueryCache 级别的全局 `hashFn` 取代 queryOptions 里的 `queryKeyHashFn`，解决同一 QueryKey 多哈希函数导致精确查找不一致；新增 `equalityFn` 可传入 `replaceEqualDeep`，为 Date 等非 JSON 类型自定义结构共享；状态为已实现。
- 🧪 **streamedQuery 稳定化**：`experimental_streamedQuery` 提升为稳定 API，结束实验状态；状态为已实现。
- 🌐 **提高浏览器基线**：最低支持 Chrome/Edge 119、Firefox 121、Safari/iOS 17.4、Opera 105，以便使用 `promise.withResolvers` 等现代浏览器 API；状态为已实现。
- ⚙️ **重试加入 jitter**：默认指数退避重试延迟加入 jitter，避免 thundering herd；因属于行为破坏性变更，只在 v6 发布；状态为已实现。
- 🧭 **gcTime 改为 last wins**：计划把同一 query 多次设置 `gcTime` 的规则从当前最高值胜出改为最后一次设置胜出，使选项覆盖更确定；状态为计划中。
- ⚠️ **enabled 拟由 skipToken 取代**：讨论移除 `enabled`、改用 `skipToken`；难点是无法复刻永久禁用后按需 `refetch()` 的模式，维护者希望先确认实际使用情况，尚未决定。
- 🎨 **queryOptions 下沉 core**：计划把 `queryOptions` 移入 `query-core`，各框架适配器只再导出或覆盖自身实现；此前受类型问题阻碍，现由协作者推进，并归入 v6 以控风险；状态为计划中。
- 🔍 **服务端 gcTime 待改进**：讨论服务端 `gcTime` 行为：默认是 `Infinity`，但直接传给 `useQuery` 的值仍会在服务端生效，已有文档提示但投诉增加；同时需保留服务端 GC 以支持长生命周期 QueryClient，尚未定案。
- 🛡️ **HydrationBoundary 清理**：移除 HydrationBoundary 中受类型保护的防御检查；但 pages router 使用 `pageProps.dehydratedState` 时用户可能需要额外守卫，维护者表示必要时可回退；状态为已实现。

### [React Testing Library 作为 DOM 的一部分时速度更快 • sigh.dev](https://sigh.dev/posts/vibecoding-faster-react-tests/)

Scott Cooper 在把 jsdom 与 DOMSelector 的若干热路径修复推入 jsdom 30.1.0 后，发布面向 React 组件测试的 @ctrl/dom：它用更轻的 DOM 实现并内置重写的 Testing Library，绕过 jsdom 公共 API 的通用开销，在多个真实测试套件中带来 32%–54% 加速，合成基准中配合自带 Testing Library 可较 jsdom 快 5.2×（Vitest）、3.2×（Jest）和 6.2×（Bun）。

- 🚀 **发布 @ctrl/dom**：项目以 0.x 发布，核心是为 React 组件测试定制的 DOM 和配套 Testing Library；此前对 jsdom 与 DOMSelector 热路径的修复多数已随 jsdom 30.1.0 发布。
- 📈 **真实套件加速**：各项目原有测试套件不改动即可受益：Sentry 从 138.2 s 降到 94.2 s（32%），Base UI 从 59.7 s 降到 34.5 s（42%），React Router 从 17.1 s 降到 8.9 s（48%），React Hook Form 从 5.9 s 降到 2.7 s（54%）。
- 🧩 **单对象节点模型**：jsdom 每个节点是公开包装对象加隐藏实现对象，`@ctrl/dom` 所有节点统一为同一个 `NodeImpl` 普通对象形状且类可跨 window 共享，便于 V8 优化属性访问；首个测试后堆内存为 16 MB，对比 jsdom 的 41 MB，Vitest worker 完成文件时为 111 MB 对 171 MB。
- ⚙️ **环境启动更快**：Vitest 默认 pool 下跑 100 个 React 测试文件，平均每文件环境启动 jsdom 为 259 ms、happy-dom 为 147 ms、`@ctrl/dom` 为 5.13 ms。
- 🎯 **角色查询重写**：`getByRole` 不再像 stock Testing Library 那样用 `querySelectorAll` 抓取 role/button/input 候选并跑 aria-query 的 113 个元素选择器；元素创建时分配数字 tag id，角色表按该 id 建数组，直接遍历 `NodeImpl`。在约 4,000 个元素页面找一个 input，stock 约 12,000 次 `matches()` 和 2,007 次 `getComputedStyle()`，`@ctrl/dom` 为 0 次。
- 🔄 **查询缓存与索引**：每次 DOM 变更递增 document version，版本不变时复用查询结果、可访问名称、计算样式和 live collection；`getAllByLabelText` 的 `[id=x]` 选择器接入 id 索引后，10,000 个 `aria-labelledby` 元素上的查询从 720 ms 降到 14 ms；可见性判断在最近带样式的祖先处停止，无样式页面跳过祖先攀爬，1,000 层嵌套的 `getByRole` 从 6.1 ms 降到 0.09 ms。
- ⚡ **虚拟计时器**：jsdom 计时器按真实时间等待，`findBy*`、`waitFor`、`user-event` 都会消耗毫秒；Sentry 套件 13% 测试时间在等待。`@ctrl/dom` 用虚拟时钟，在只剩计时器时立即触发并推进 `Date.now()` 与 `performance.now()`，顺序不变，可用 `timeSkip: false` 按项目或文件关闭；20 ms 计时器后的 `findByRole` 从 23.3 ms 降到 108 µs（216×）。
- 🧪 **合成基准**：100 个 React 测试文件在 Vitest、Jest、Bun 下：`@ctrl/dom` 配合自带 Testing Library 对比 jsdom 分别为 2.42 s 对 12.59 s（5.2×）、741 ms 对 2.34 s（3.2×）、271 ms 对 1.69 s（6.2×）；只用 `@ctrl/dom` 搭配 stock Testing Library 为 1.3–3.6×，大部分提升来自 Testing Library 重写。
- 🔍 **性能分布**：Base UI 套件在 `@ctrl/dom` 上分析：Node 模块加载 23.1%、Vitest 14.1%、Base UI 自身代码 14.1%、react-dom 11.9%、`@ctrl/dom` DOM 7.3%、`@ctrl/dom` testing 约 3%，`@ctrl/dom` 总计约 10% 运行时间；Sentry 只提升 32% 而非合成基准的 5.2×，因为其测试导入大型应用并渲染大组件树，大部分时间本来不在 DOM。
- ⚠️ **未实现范围**：专为 React 组件测试构建，跳过 scripts、导航、`fetch`、图片加载、iframe `src` 和真实布局；仅支持 Node 26+ 与 React 19。需要这些能力时应继续使用 jsdom。
- 🛠️ **接入方式**：安装 `pnpm add -D @ctrl/dom`；Vitest 配置中加入 `ctrlDom()` 插件，会把 `@testing-library/*` 导入指向 `@ctrl/dom` 版本；传 `ctrlDom({ testingLibrary: false })` 可保留 stock 包只替换 DOM，速度较慢但迁移更稳。Jest 配置见 README。项目仍为 0.x，几乎肯定会在套件中暴露问题，作者邀请提交 issue。

### [你的工具正在向你隐瞒 npm 审计结果—zachleat.com](https://www.zachleat.com/web/npm-audit-report/)

文章通过同一天生成的两个全新默认脚手架项目说明，`npm audit` 显示 0 漏洞并不等于更安全：`create-next-app` 生成的 Next.js 项目把自身依赖打包进 `node_modules/next/dist/compiled`，导致标准审计漏报 139 个依赖中的多级漏洞；而 `create-gatsby` 项目显示 78 个漏洞。文章还梳理了 create CLI 和包管理器隐藏或省略 audit 输出的做法，并介绍按生态归一化比较漏洞的 Prototype Pollution Report。

- 🎯 **对比结果**：全新 `create-gatsby` 项目的 `npm audit` 报告 78 个漏洞（7 low、23 moderate、46 high、2 critical），全新 `create-next-app` 项目报告 0 个漏洞；但作者认为这不能直接说明 Next.js 更安全。
- 🧩 **Next.js 隐藏依赖**：`next` v16.4.6 对自身依赖绕过 `node_modules`，依赖位于 `node_modules/next/dist/compiled`；单独审计这些依赖会发现 139 个唯一依赖中有 11 low、2 moderate、19 high、3 critical 漏洞，且不会被标准审计报告机制报告。Gatsby 已不再维护，但 Next.js 隐藏的 critical 漏洞仍多于 Gatsby 可见的 critical 漏洞。
- 🔍 **Vite 类似做法**：Vite 也在 `node_modules/vite/dist` 中打包依赖，但属于打包器生成产物；作者认为它作为本地开发工具比生产运行时更容易被理解，不过将依赖完全排除在审计之外可能属于过度矫正，并指出 Vite 在保持打包依赖更新和无审计漏洞方面记录很好。
- ⚠️ **CLI 隐藏安装审计**：`create-gatsby` 使用 `npm install --no-audit`；`create-astro`、TanStack CLI 和 `create-preact` 不显示控制台输出；`create-nuxt` 和 `ng new`（Angular）只在安装失败时打印输出；`sv create`（Svelte）短暂显示后清空日志。这类做法不如隐藏依赖严重，因为项目内独立运行 `npm audit` 仍能看到在用依赖，但透明度不足。
- 📦 **包管理器差异**：`npm` 在 `npm install` 后会显示审计报告，而 `pnpm` 和 `yarn` 不会显示。
- 📊 **归一化报告**：作者发布名为 Prototype Pollution Report 的报告，将上述差异归一化后比较不同框架生态，约每天更新一次；Ecosystem Scoreboard 统计各项目发布的全部非废弃包，并主张维护者应废弃不再维护的包；Core-only Scoreboard 只统计核心包；文末列出完整包列表及审计计数。

### [React 表单：不止于 onSubmit](https://www.gmoniava.com/blog/react-forms-beyond-onsubmit)

React 19 允许向表单的 `action` prop 传入函数，文章以模拟订阅接口为例，对比普通 `onSubmit`、`action` 以及 `onSubmit` 配合 `useTransition` 三种表单提交方式，重点说明自动导航拦截、`FormData` 获取、自动重置、Transition 行为、加载状态和渐进增强等差异。

- 🚀 **React 19 的 action**：React 19 支持把函数传给表单的 `action` prop；React 负责阻止浏览器默认导航，函数直接接收 `FormData`，无需 `event.preventDefault()` 或从 `event.currentTarget` 手动构造 `FormData`。
- 🧩 **action 自动重置**：`action` 在不抛错地完成时会自动重置非受控字段；示例中订阅失败通过状态处理而不抛错，因此邮箱字段也会被清空，而 `onSubmit` 示例仅在成功后才调用 `form.reset()`。若需保留字段值，可把值存入 state 并通过 `defaultValue` 传回，或使用 `requestFormReset(form)` 等方式。
- ⚙️ **Transition 语义**：传给 `action` 的函数在 Transition 中运行，因此支持 `useOptimistic` 和错误边界；Transition 内的同步状态更新可能被延后，手动 loading 标志可能不显示，应使用 `useFormStatus().pending` 在子组件中读取提交状态。
- 🧩 **useFormStatus 限制**：`useFormStatus` 读取父级 `<form>` 的状态，所以 `SubmitButton` 和 `FormMessages` 必须渲染在表单内部；在 `NewsletterForm` 自身调用不会跟踪该组件返回的表单。`SubmitButton` 用 `pending` 禁用按钮并显示 Subscribing...，`FormMessages` 在 pending 时隐藏旧消息。
- 🔄 **onSubmit + useTransition**：该方案仍需手动调用 `event.preventDefault()` 和构造 `FormData`，然后把异步订阅包进 `startTransition`，用 `isPending` 控制按钮；在调用 `startTransition` 前清空 error/success，可让旧消息立即消失，不需要 `useFormStatus`。
- 🛡️ **渐进增强差异**：`onSubmit` 以及 `onSubmit` 配合 `useTransition` 的处理器都在客户端运行，必须先加载 JavaScript 并完成 hydration；只有把 Server Function 传给 `action` 时，兼容框架才可能在 JavaScript 加载前支持表单提交，`useTransition` 无法提供这一点。
- 📝 **受控输入注意**：文章示例使用非受控输入，但三种方式也支持受控输入；受控时用 `value` 和 `onChange` 管理 email，可从 state 读取而非 `FormData`，并用 `setEmail` 传入空字符串清空，自动重置仅适用于非受控字段，pending 与 Transition 行为不变。
- 🧪 **示例 API**：示例共用的 `subscribe(email)` 会等待 1 秒，`test@example.com` 返回失败和 This email is already subscribed.，其他邮箱返回成功；所有示例都围绕该函数演示状态处理。
- 🔮 **useActionState**：文章还提到 `useActionState` 可作为 `action` 的另一种用法：返回 action 结果作为 state 并提供 `isPending`，从而减少单独的 `useState` 和 `useFormStatus` 子组件，但未展开。

### [关于绘制图标 :: Pierre Computer Company](https://pierre.computer/writing/on-drawing-icons)

Pierre 完成图标库全面重绘，发布 1,200 多个新图标，覆盖 12、16、24 三种尺寸，并提供 outline、fill、duo 最多三种变体，均可在 Figma、SVG 和 React 中使用。此次重绘统一了绘制规范，并把 Figma 组件、规范 SVG 与 manifest、React 生成和静态预览串成一条可验证的管线；期间验证并放弃了 Figma 直出 React 与运行时徽章组合方案。

- 🚀 **图标库上线**：发布 1,200 多个新图标，覆盖 12、16、24 三种尺寸，每个图标最多提供 outline、fill、duo 三种变体，均可在 Figma、SVG 和 React 中使用；旧库约 400 个图标，存在描边宽度、viewBox 和构图不一致，以及重复和未使用图标等问题。
- 🧩 **三尺寸三描边**：三种尺寸分别绘制而非缩放，默认描边 token 为 1px、1.25px、2px，填充变体提升到 1.25px、1.5px、2.5px，细部线条可再降一档；这些值存为 Figma 变量，便于整体调整。24px 版本可增加细节，例如信封多几条线、建筑多窗户和门间横条、锁加钥匙孔。
- 🛠️ **Figma 组件组合**：用 base shapes、icon layers 和 masks 组合图标家族，并利用 Figma 非破坏布尔运算，修改 IconFile 等共享形状可自动更新数十个相关图标；squircle、circle、comment、file、folder 等基础形状组合出 65 个组件、每个 9 种变体、3 种尺寸，覆盖近 600 个图标。
- 🔧 **自建设计插件**：为本次重绘编写 Layer Swap，按变体属性替换嵌套图层，并在所有变体中围绕图层中心旋转或翻转；Taper Stroke 插件把矢量网络拆成可编辑描边，识别 stem 和 crown 后收窄交汇处并保持外轮廓，解决箭头等图标交点视觉过重的问题，但 beta 暂不启用，计划后续版本加入；另有 Shape Language Overlay 和 Icon Preview Grid。
- ⚠️ **直出 React 受挫**：React Icon Exporter 能把 Figma 的 Size、Type 属性转成 React props 并生成近 100 行组件，但运行时组合徽章图标会因布尔扁平化产生一像素偏移、viewBox 被撑大，且体积从 1.40KB 增至 2.81KB gzip，文件夹从 1.36KB 增至 2.88KB，最终放弃该方案，改为保留独立扁平图标。
- 📦 **SVG 作为契约**：确定 Figma 负责视觉源、仓库负责代码生成的边界：SVGO Exporter 把每个绘制变体导出为规范 SVG 树，并生成 manifest.json 记录组件名、属性轴、默认值、变体属性和文件路径，同时输出 REPORT.md；npm run icons 再生成 React 组件、SVG sprite、包导出索引和本地 HTML 预览，本地不再二次运行 SVGO。
- 💻 **新 React API**：风格变体改为独立导出，如 IconFileBadgeGear、IconFileBadgeGearFill、IconFileBadgeGearDuo；size prop 选择实际的 12、16 或 24 绘制，不缩放单一 SVG，类型可精确为 12 | 16。组件支持 aria-*、data-*、事件和 role，默认 currentColor，保留源文件中的 overflow="visible"，并用 .bg 和 .fg 类支持双色调及安全的多色定制。
- 🔍 **预览即 QA**：本地静态预览从简单图标墙扩展为画廊加目录应用，可切换已发布集合与重绘集、按名称搜索、按 outline/fill/duo 过滤、单尺寸或三尺寸并排、切换到带真实标签和间距的列表视图，点击图标可查看实时渲染、Multi 双色开关、React 用法和带语法高亮的源码；它捕获了 viewBox 变化、裁剪、缺失尺寸、双色调透明度、命名不匹配和列表视觉问题。
- ✅ **新流程闭环**：流程为在 Figma 绘制三种尺寸变体、用 Layer Swap 等插件保持家族一致、导出规范 SVG 和 manifest、审阅 REPORT.md、替换 @pierre/icons 的 SVG 树并运行 npm run icons、检查 React/sprite/预览、在隔离和产品化列表中测试，最后在绘制、导出、生成器或预览的正确层修复，而不是在 React 里用 CSS 微调。

### [错误](http://joyofreact.com/?couponCode=TWIR)

无法总结：获取内容时出错 - HTTPConnectionPool(host='host.docker.internal', port=7897): Read timed out.

### [来自Pierre的话语](https://diffs.com/words)

Pierre 发布 Beta 版 @pierre/words，这是一款用 WebAssembly Text（解析器为 inline.wat）编写的流式 Markdown 渲染器；它直接输出 HTML，支持 GitHub Flavored Markdown，并可搭配 @pierre/highlights 在流式过程中做语法高亮。它提供增量更新、以字符串钩子自定义生成的 HTML、可选的逐词淡入，以及在代码围栏按 id 保持状态的 reactive islands（响应式岛）。官方基准显示，其 HTML 吞吐、流式更新耗时、渲染后内存与下载体积均明显优于 Streamdown，基础 React 渲染器 gzip 体积小 65%。

- 🚀 **Beta 发布**：@pierre/words 以 Beta 形式发布，用 WebAssembly Text 实现，直接渲染为 HTML，支持 GitHub Flavored Markdown，并可与 @pierre/highlights 组合实现代码高亮。
- ⚡ **吞吐基准**：在 5 篇文档（含 5.4 KiB 的 AI code review）的 HTML 吞吐测试中，Words 达 449.2 MiB/s，高于 md4x 的 NAPI 版 234.9 MiB/s、Wasm 版 185.0 MiB/s 和 markdown-it 的 185.0 MiB/s。
- 🧩 **流式渲染**：浏览器端以 256 个 UTF-16 码元分块、每块间隔 40 ms 推送，Words 的流式更新总耗时为 11.6 ms，Streamdown 为 70.2 ms；流式渲染完成后 V8 堆内存增长 0.5 MB，Streamdown 为 11 MB。
- 📦 **体积优势**：gzip 基准下基础 React 渲染器比 Streamdown 小 65%；计入 148 种语言与 GitHub 明暗主题后为 253.6 KB，Streamdown 为 1,057.8 KB（按需加载语言时会更少），CSS 分别为 1.2 KB 和 0.4 KB。
- 🎨 **淡入动画**：通过 animated 选项让新到达的文本逐词淡入，已有文本位置不变，遵循 reduced-motion 偏好，可调整持续时间（示例 180 ms）并重放流；Words 连代码一起淡入，Streamdown 只淡入正文单词。
- 🛠️ **HTML 钩子**：可用字符串钩子自定义生成的 HTML，例如为标题加图标、为链接和行内代码套用自己的 class 与设计令牌，Markdown 源保持不变，流式更新仍由 Words 处理。
- 🧪 **数学与图表**：开启 math 即可将 TeX 渲染为 SVG，无需额外依赖；将 Pele 传给 createMermaidPlugin 可把 mermaid 代码块绘制成图表。
- 🔄 **响应式岛**：以 ~~~island-* 围栏加 JSON 配置声明交互组件，围栏闭合时组件出现；只要 id 不变，编辑周边正文仍保留投票等状态，按钮就绪前显示 shimmer，重放则重置为新流。
- 💻 **接入方式**：通过 `pnpm add @pierre/words` 安装，React 侧从 `@pierre/words/react` 引入 `Markdown` 组件，用 `isAnimating` 传入流式状态；内置 152 种语言，未知语言回退为纯文本。

### [发布 talata@0.4.0 · lxsmnsyc/talata · GitHub](https://github.com/lxsmnsyc/talata/releases/tag/talata%400.4.0)

talata 发布 0.4.0，新增 `talata/mdx` 子路径和可选的 acorn 集成，使 MDX 解析覆盖 ESM、表达式边界与 `data.estree`，并可与 `@mdx-js/mdx` 3.1.1 配合；同时调整 `talata/directive` 的容器指令解析语义，并大幅提升深层嵌套容器指令的解析速度。

- 🚀 **版本发布**：`talata@0.4.0` 发布，包含 `talata/mdx` 新子路径、acorn 相关选项，以及 `talata/directive` 的语义修正和性能优化。
- 🧩 **acorn 集成**：`talata/mdx` 新增 `acorn` 和 `acornOptions` 选项；`mdx({ acorn: Parser.extend(acornJsx()) })` 返回与 `micromark-extension-mdxjs` 配合 `mdast-util-mdx` 相同的树（含位置）。acorn 决定表达式边界，因此 `{"}"}` 是一个表达式，`import` 和 `export` 行成为 `mdxjsEsm` 节点。
- 🔍 **ESTree 与报错**：表达式、属性表达式和 ESM 将 acorn 的 program 放入 `data.estree`，并带文档位置；acorn 拒绝的代码抛出 `MdxError`，携带参考实现的 reason 和 place。acorn 由调用方提供，talata 不新增依赖。
- 🔗 **Unified 兼容**：配合 acorn，`@mdx-js/mdx` 3.1.1 可用 talata 作为 parser 并编译相同 JS：从 `talata/unified` 传入 `remarkPlugins: [[talata, { extensions: [mdx({ acorn })] }]]`。无 acorn 时没有 ESM 和 `data.estree`，`@mdx-js/mdx` 会编译出破损 JS。
- 📦 **新增子路径**：新增 `talata/mdx` 子路径；`mdx()` 解析 flow 和 text 中的 JSX 元素、花括号表达式、属性与展开表达式，返回与 `micromark-extension-mdx` 配合 `mdast-util-mdx` 相同的树（含位置）。其代码不在主入口中。
- 🧩 **无 acorn 行为**：无 acorn 时，花括号按参考实现计数，不解析 ESM；与参考实现一样关闭缩进代码、自动链接和 HTML，坏语法抛出带 reason 和 place 的 `MdxError`。可通过 `extensions` 与核心或 Unified 插件使用。
- 🔄 **directive 语义**：`talata/directive` 将容器指令内容在周边文本之后作为独立文档解析，与 `micromark-extension-directive` 一致；嵌套文本指令标签中的引用或脚注引用不再解析到更晚定义，`frontmatter({ anywhere: true })` 下容器指令内容第 1 列的 matter 会成为 `yaml` 节点。
- ⚡ **性能优化**：深层嵌套容器指令解析加速：此前每条 line 会重复读取各开放指令周围，800 层嵌套耗时超过 4 秒，现在约 12 ms，解析树不变。

### [发布 v2.15.0 · reduxjs/redux-toolkit · GitHub](https://github.com/reduxjs/redux-toolkit/releases/tag/v2.15.0)

Redux Toolkit 发布 v2.15.0，这是 2.x 功能版本，延续 Redux Toolkit 3.0 路线图，重点重构 RTK Query 的每 Store 运行时、修复 initiate() Promise 结果错配，并新增 startReason、函数 pollingInterval、getRunningQuery、retainFor、getMiddlewareState、isSubscribed 等能力；同时改进 listener middleware 嵌套 fork、类型可读性和多项 RTKQ 边界行为与 bug。

- 🚀 **正式发布**：Redux Toolkit v2.15.0 已发布，包含 12 个提交，主要影响 RTK Query、listener middleware、类型定义和若干修复；部分 RTK Query 变更属于边界行为修复，升级时需留意行为变化。
- 🧩 **每 Store 运行时**：RTK Query middleware 将订阅者计数、运行请求、轮询与缓存计时器、缓存生命周期 Promise 等状态从共享闭包迁移为每个 store 独立 runtime；resetApiState 调用 runtime.reset() 只清理该 store，并中止运行请求、清理 pending tag invalidations；缺少 middleware 检查改为每 store 一次且更严格。
- ⚠️ **initiate 结果**：initiate() Promise 现在在请求 fulfilled 或 rejected action 到达 store 时捕获，并解析为该请求自己的结果，避免缓存条目被删除、重置、失效或替换时返回 undefined 或其他请求数据；unwrap() 在请求运行中被移除时会因 AbortError 拒绝，plain promise 仍不会 reject。
- ⚠️ **缓存移除行为**：请求运行中移除缓存条目会中止该请求，覆盖 removeQueryResult、lazy query 的 reset()、cache collection 和 resetApiState；initiate() Promise 解析为 isError: true 与 AbortError，message 为 removed 或 reset，unwrap() 会拒绝，onQueryStarted 中 await queryFulfilled 需要 try/catch。
- 🎯 **startReason**：BaseQueryApi、fetchBaseQuery 的 prepareHeaders、onQueryStarted 和 onCacheEntryAdded 新增 startReason；QueryStartReason 类型包括 initial、refetch、invalidation、poll、focus、reconnect、upsert、hydrate、nextPage、previousPage；mutation 为 undefined，hydrate 预留给后续 hydration 工作且尚未设置。
- ⚡ **函数式轮询**：pollingInterval 可为接收当前 cache entry 并返回毫秒数的函数，适用于所有 query hooks、initiate() 和 updateSubscriptionOptions；请求 settle 后每个 cache key 调度一次，多个订阅者取最低结果，返回 0、负数或非数字表示不轮询，负数数值不再立即循环轮询；类型变为 number | ((entry) => number) 并新增 PollingInterval 类型。
- 🔍 **运行查询与保留**：api.endpoints.x.getRunningQuery(arg) 是 query 和 infinite query endpoint 的类型化 thunk，返回该 cache entry 正在运行请求的 Promise 或 undefined，等待它不会新增订阅；initiate() 新增 retainFor 秒数选项，最后订阅者离开后按 Math.max(keepUnusedDataFor, retainFor) 保留条目，适合 prefetch 或 subscribe: false 后很快读取。
- 🔑 **订阅状态 API**：api.util.getMiddlewareState() thunk 返回该 store 中 middleware 跟踪的只读状态，目前提供 getSubscriptionCount(queryCacheKey)，middleware 未添加时返回 undefined；query initiate() 结果新增 isSubscribed()；hooks 改用 isSubscribed() 且不再 dispatch internal_getRTKQSubscriptions，该 action 在 2.x 仍可用但已废弃，3.0 移除。
- 🛠️ **嵌套 Fork**：ForkedTaskAPI 新增 getState、dispatch 和 fork，使 forked task 可读取 state、派发 action 并创建子任务；嵌套 fork 会随父任务结束或取消而取消，autoJoin: true 会让父任务等待子任务完成；ForkedTaskAPI 和任务执行器类型新增可选 State、DispatchType 泛型，并流向 startListening、addListener 及其 withTypes() 版本。
- 🧠 **类型可读性**：新增 FetchBaseQueryFn、ApiUtil、ListenerMiddlewareDispatch、AsyncThunkPromise、ReactApiModules 等命名类型，并重写 query、mutation、infinite query selector result 类型以保留名称；编辑器 hover 长度显著下降，例如 useMutation tuple 从 2508 降到 386，api.util 从 16102 降到 471；这些是 type-only 变更，需关注泛型 endpoint 定义兼容性。
- 🔄 **共享查询选项**：多个订阅者共享查询时，各订阅者选项先解析再合并；refetchOnMountOrArgChange: 0 和 forceRefetch: 0 现在总是触发 refetch，refetchOnFocus 和 refetchOnReconnect 在任一订阅者自身或继承设置为 true 时触发，skipPollingIfUnfocused 仅在所有 polling 订阅者都设置时才跳过未聚焦轮询。
- 🐛 **其他修复**：endpoint 的 maxRetries 在 api 级 retry() 带 retryCondition 时仍能限制重试；retry.fail() 在 backoff 函数内不再把错误嵌套进 { error, meta }；fetchBaseQuery 的 timeout 在请求自带 signal 时生效；查询参数改为加在 URL #fragment 前；FetchArgs.headers 接受 number 和 boolean 并转字符串；entity adapter 更新实体 id 时保持 ids 顺序；泛型包装 createSlice 保留 prepare 参数类型。

### [发布 v9.6.0 · mui/material-ui · GitHub](https://github.com/mui/material-ui/releases/tag/v9.6.0)

MUI 发布 v9.6.0，`@mui/material`、`@mui/system`、`@mui/utils`、`@mui/styled-engine`、`@mui/private-theming` 和 `@mui/codemod` 等包同步更新，37 位贡献者参与。此版本以实验性密度增强、焦点可见性定制和乌兹别克语 locale 为亮点，同时集中修复 Autocomplete、Slider、InputBase、Popper、FocusTrap 等组件的交互与类型问题，并改进系统样式、CSP nonce 和 codemod 工具链。

- 🚀 **正式发布**：发布 `@mui/material@9.6.0` 及 `@mui/system`、`@mui/utils`、`@mui/styled-engine`、`@mui/private-theming`、`@mui/codemod` 等同版本包，37 位贡献者参与；亮点包括实验性密度增强、焦点可见性定制与乌兹别克语。
- 🎨 **焦点环定制**：新增 `focusVisible.insetOverrides` 和 `theme.applyFocusVisible`，可进一步定制 focus visible 样式；输入框会渲染 `theme.focusVisible` 环，并修复表格分页行数选择与翻页按钮的焦点环。
- ⚙️ **密度增强**：引入实验性主题增强器 `unstable_enhanceDensity`，用于在组件间应用一致且可调的尺寸密度，当前标记为 experimental。
- 🌐 **新增语言**：增加乌兹别克语 `uz-UZ` locale，并通过主题对 locale 进行测试。
- 🧩 **自动完成**：Autocomplete 支持自动高亮选项的内联补全，Escape 清空时遵守 `readOnly`，使用 CSS transform 时可将高亮选项滚动进视图；同时修复 `onInputChange` 事件与 reason 类型、`React.ComponentProps<typeof Autocomplete>` 展开类型错误和 `slotProps` 下的 TypeScript 性能。
- 🔄 **组件交互**：ButtonBase 允许处理器设置 `defaultMuiPrevented` 跳过内建键盘处理；ButtonGroup 修复增删或重排兄弟节点时子节点重挂载；Grid 响应式属性接受只读数组；SwipeableDrawer 修复 Shadow DOM 内滑动手势；Tabs 修复祖先缩放时指示器位置与尺寸；Tooltip 在 `slotProps.transition` 设置 `onEnter` 或 `onExited` 时保留 popper 生命周期处理器。
- 🐛 **稳定性修复**：修复 InputBase 带起始装饰时出现“Maximum update depth exceeded”、Popper 在 React 19 下同类错误、Menu 的 `MenuItem autoFocus` 与 React 17 问题、MenuList 无聚焦项时 ArrowUp 无限循环，以及 FocusTrap 重新执行 effect 后焦点丢失等交互问题。
- ⚡ **滑块修复**：Slider 键盘步进不再产生浮点值，`onChangeCommitted` 不再报告过期值，拖动时 thumb 不再滞后于指针，非整数 `min` 吸附到 step 时保留小数。
- 📦 **系统样式**：`@mui/system` 修复命名容器查询、`resolveBreakpointValues` 标量返回类型、`color()` 颜色 alpha 保留、容器查询尺寸单位保留，并在运行时创建的 style 标签上设置 CSP nonce；`@mui/styled-engine-sc` 保留 styled-components 的独立 `sx`。
- 🛠️ **工具链**：Codemod 修复 yargs 18 下 CLI 崩溃及包外执行 `v5.0.0/top-level-imports`、`v5.0.0/path-imports` 的问题；Grid codemod 删除 `item` 和 `zeroMinWidth` 时保留 JSX 展开。

### [styled-components 发布 6.7.0 版本 · styled-components/styled-components · GitHub](https://github.com/styled-components/styled-components/releases/tag/styled-components%406.7.0)

`styled-components@6.7.0` 发布，新增 `configureServerStyles({ stylisPlugins })` 以在整个服务器进程中统一配置服务器组件的 Stylis 插件，并修复服务器样式在并发请求、Next.js 13.5/14、动态 `createGlobalStyle`、跨组件选择器、TypeScript 与无单位 CSS 属性等方面的多项问题。

- 🧩 **全局配置**：`configureServerStyles({ stylisPlugins })` 设置整个服务器进程内所有服务器组件的 Stylis 插件；应在每个服务器渲染最先加载的模块顶层调用一次，Next.js 中为根布局文件；它可覆盖构建时预渲染页面和客户端导航到达的页面，这是共享布局中的 `StyleSheetManager` 覆盖不到的；服务器组件内的 `StyleSheetManager` 从这些插件开始，自身的 `stylisPlugins` 会替换它们，`stylisPlugins={[]}` 则丢弃它们；仅作用于服务器组件，客户端组件仍从客户端渲染的 `StyleSheetManager` 获取插件；每应用调用一次，后调用替换前调用并只影响之后开始的渲染。
- 🔄 **动态全局样式**：当两个 `createGlobalStyle` 仅在函数返回值上不同时，每个都会应用自己的 CSS，包括主体仅为一个函数的情况（如返回 `html { --a: 1; }` 的函数）；同一属性冲突时最近挂载的胜出，prop 或 theme 更新不改变胜出者；服务器端多次挂载同一个动态全局样式时，收集的样式包含每一次而非仅最后一次。
- 🐛 **跨组件选择器**：在样式中引用其他组件（如 `${Box}:hover { ... }`）时，任意 `styled` 组件在 `preact/compat` 下，以及 `React.memo` 或函数包装器把 styled 组件静态属性 hoist 到自身时，能生成该组件的选择器。
- 🛡️ **并发与复用**：多个请求同时在同一个服务器渲染时，服务器组件会保留 `StyleSheetManager` 设置；修复等待数据后 `stylisPlugins` 中途丢失、导致 `stylisPluginRSC` 的 `:first-child` 等选择器在高负载下随机未重写的问题；复用同一 `stylisPlugins` 数组的服务器 `StyleSheetManager` 不再误取先前渲染 manager 的 `namespace` 或 `enableVendorPrefixes`。
- ⚙️ **空插件数组**：服务器组件中的 `StyleSheetManager` 在 `stylisPlugins={[]}` 与 `namespace`、`enableVendorPrefixes` 同时传入时仍会让后两者生效，与客户端组件行为一致。
- 🌐 **Next.js 兼容**：服务器组件样式在 Next.js 13.5 和 14 中保留按原样写出的子组合器 `>`、引号和 `&`；这些版本内置 React 18.3 canary 会在内联 `<style>` 标签中 HTML 转义它们（如 `.a &gt; .b`），导致浏览器首次加载丢弃规则；样式值仍不能关闭 `<style>` 标签；Next.js 15 及之后不受影响且输出与之前相同。
- 🐛 **TypeScript 修复**：`styled-components/native` 组件在 Reanimated 的 `useAnimatedRef` ref 上不再触发 TS2590（表达式生成的联合类型过于复杂）错误，该问题从 6.5.3 起出现；但若代码更早检查 DOM 元素或 web styled 组件，错误仍可能出现，类似没有 styled-components 的普通 `<div>`。
- 📦 **无单位属性**：对象样式中 `fontSizeAdjust`、`hyphenateLimitChars`、`initialLetter`、`mathDepth`、`shapeImageThreshold`、`maskBorderOutset`、`maskBorderSlice`、`maskBorderWidth` 的数字值现在无单位渲染，例如输出 `font-size-adjust: 0.5`、`hyphenate-limit-chars: 6`；升级后设置这些属性为数字的组件会因生成的 CSS 变化而获得新类名。
- 🛠️ **插件名称校验**：`stylisPluginRSC` 经生产 bundle 后仍保留名称，使开发和生产类名一致并通过插件名检查；传给 `<StyleSheetManager stylisPlugins={[...]}>` 的匿名 Stylis 插件再次抛出文档中的「not named」错误（#15），不再静默接受并让类名与未传插件时相同。

### [unhead v3.5.0 版本发布 · unjs/unhead · GitHub](https://github.com/unjs/unhead/releases/tag/v3.5.0)

Unhead 发布 v3.5.0，重点提升性能与正确性，尤其是服务端渲染页面在浏览器接管时的 hydration 过程。该版本通过跳过无用查找、减少 DOM 写入和优化流式处理降低开销，同时引入实验性 lazy head，并为未来的 compiled mode 铺路。

- 🚀 **版本发布**：Unhead v3.5.0 正式发布，官方定位为性能与正确性版本，尤其关注浏览器从服务端渲染结果继续接管时的行为，包含 16 个提交和新功能、修复与性能优化。
- ⚡ **Hydration 提速**：当页面带有大型 inline stylesheet 且 Unhead 无需更新时，不再为该 CSS 构建 lookup key，除非客户端 tag 需要它；在 Nuxt-style benchmark 中，首次 hydration 快 23%。
- 🧪 **实验性 lazy head**：如果服务端已经渲染页面所需的全部 head tags，可尝试实验性 lazy head：变更会排队，直到调用 `head.load()`；该能力支持 Vue、React、Svelte、Solid 和 vanilla JavaScript，属于 opt-in。
- 🔮 **compiled mode 探索**：lazy head 的工作也为未来 compiled mode 打开入口；这是一种仍在探索中的 opt-in 方案，计划在构建阶段提前准备 head tags，尚未在 v3.5.0 中发布。
- 🛠️ **SSR 工具链增强**：bundler 新增 `serverOnlyCrawlerTags` 选项；`unhead` 允许预计算静态 server init entries；validate 会为大型 inline tags 建议 keys；Vite 支持将 Vite descriptors 转换为 SSR 用途。
- 🐛 **Schema.org 修复**：修复多项 schema-org 身份与 URL 边界问题：接受 Vue getter inputs，保留专用 organization 的 logo，保持站点身份作为 WebSite publisher，避免无关人员成为 article authors，并修正 Event location、WebPage slug、相对 location URL 和 protocol-relative URL 处理。
- 🐛 **SSR 与 hydration 修复**：修复 Angular SSR root attributes 解析，hydrate server trigger scripts 时从服务器元素读取，保留显式 `undefined` crossorigin，SSR 模板扫描不再依赖 parse5，并处理 JSON 模板参数控制字符转义、script/style 提取结束位置及 server-only `og:image` 下的 `twitter:card` 保留等问题。
- 📦 **体积与流式优化**：版本还缩小了 Unhead client core 和最小 client bundle，减少 hydration 工作量并释放 stale DOM cache，跳过未变化属性写入，降低 stream 每次读取的分配，并在构建时 minify streaming bootstrap。

### [发布 · nickjvandyke/eslint-plugin-react-you-might-not-need-an-effect · GitHub](https://github.com/nickjvandyke/eslint-plugin-react-you-might-not-need-an-effect/releases)

nickjvandyke 的 eslint-plugin-react-you-might-not-need-an-effect 从 v1.0.0 稳定发布起步，在 v1.1.0 至 v1.3.3 的连续更新中增强对 React Effects 的静态检测：扩展 TypeScript 语法、第三方 effect 包装器、context 值和重命名 Hook 导入的识别，泛化多条规则并修复规则重叠、同步调用判断和 setter 追踪等误报边界，帮助开发者发现可能不需要的 useEffect 并提升 lint 准确性。

- 🚀 **稳定版发布**：v1.0.0 于 2026-05-31 发布，作者表示经过多轮迭代后对插件的稳定性和可靠性有信心，并感谢贡献真实问题的用户。
- 🧩 **TypeScript 与包装器支持**：v1.2.0 能看穿 TypeScript-only syntax、支持流行的第三方 effect wrappers，并将 context values 视为 props；同时可分析 const Component = function() {} 组件、带省略或变量 deps 的 effects、useState 解构默认值，并忽略非函数 effect callbacks。
- 🛠️ **规则检测泛化**：v1.3.0 将 no-adjust-state-on-prop-change 泛化到所有外部值，将 no-derived-state 扩大到任意 effect dependencies，并让 no-pass-data-to-parent 标记来自函数调用和全局变量的数据。
- 🔄 **调用链与同步判断**：v1.3.1 在追踪值时跟随调用参数，并把立即调用函数视为同步；v1.3.0 还忽略调用链中无关参数、把全局变量的本地别名视为外部值、将配置的全局变量按未解析全局变量处理，并修复组件和 hook 名称检测边界及 async 函数调用的同步性判断。
- 🐛 **规则边界修复**：v1.3.2 在 no-event-handler 中标记同步调用 helper 里的条件，在 no-reset-all-state-on-prop-change 中处理 helper 边缘情况，并让 TypeScript 支持 import-equals 别名 `import x = A.b`。
- ✅ **减少重复报告**：v1.3.3 解决重叠规则，保证每个 effect 的每个 setter 只产生一条规则报告。
- 🌐 **导入与配置兼容**：v1.1.0 支持重命名 React hook imports，为 flat configs 命名并停止向 lint set 添加文件；v1.0.3 停止为消费者定义或推荐 browser globals。

### [版本发布 · BetterTyped/react-zoom-pan-pinch · GitHub](https://github.com/BetterTyped/react-zoom-pan-pinch/releases)

BetterTyped/react-zoom-pan-pinch 在 v4.0.3 至 v4.4.0 的连续发布中，集中完善 React 画布的缩放、平移和小地图体验，并补齐控制 API、键盘操作、跨窗口与构建稳定性；最新 v4.4.0 主要解决拖拽中滚轮缩放、平移后点击、CSP/Shadow DOM 样式和命名位置等遗留问题。

- 🚀 **最新版修复**：v4.4.0 于 2026-11-19 发布，集中解决多项遗留 issue，包括拖拽中滚轮缩放、平移后点击、CSP/Shadow DOM 样式和命名位置等，并关闭 #280、#477、#543、#452、#519 等一批问题。
- 🧩 **小地图**：v4.3.0 增加 React Flow 风格小地图，支持抓取拖拽、内容/视口映射和 SVG 遮罩，便于在大画布中定位与导航。
- ⚡ **越界回弹**：v4.3.0 为平移加入越界橡皮筋回弹，拖拽超出边界后产生回弹反馈。
- 🐛 **Hooks 修复**：v4.3.0 修复 `useTransformComponent`/`useTransformEffect` 挂载时看不到已应用变换，以及 stale ref prop 访问。
- 🧭 **核心交互**：v4.2.0 为核心加入键盘导航、fit-to-view、`panBy`、可选文本和跨窗口平移，并恢复与已发布 MiniMap API 一致的示例。
- 📦 **Source Map**：v4.1.1 修复构建产物 source maps，使其可解析并内嵌源码，关闭 #529、#542。
- 🛠️ **控制 API 扩展**：v4.1.0 为 controls 增加完成 Promise、`zoomToPoint`、坐标辅助函数和多目标 `zoomToElement`，导出 `useZoomPanPinch`，并将 `transform-origin` 内联到内容元素以处理样式问题，同时应用对齐窗口内到达的滚轮事件。
- 🛡️ **稳定性修复**：v4.0.7 修复卸载清理与首帧前初始化、小地图每次渲染泄漏 document mousedown 监听、平移误触表单控件/contenteditable/draggable 子树，并让滚轮横向滑动不再触发缩小、触控板平移受实时边界约束，`zoomIn`/`zoomOut`/双击按绝对增量步进。
- 🐛 **NaN 防护**：v4.0.4 防止无效鼠标/触摸位置导致 NaN 传播，关闭 #566。

### [Sentry 应用指标：最佳实践与用例 | Sentry](https://sentry.io/resources/metrics-workshop/?utm_source=thisweekinreact&utm_medium=paid-community&utm_campaign=metrics-fy27q4-metricsworkshop&utm_content=newsletter-secondary-register)

Sentry 将举办 Application Metrics 工作坊，介绍如何把应用指标与 traces、logs、errors 一起埋点，以便用足够的上下文筛选和聚合关键信号，更快从图表上的指标尖峰定位根因，并把指标转化为仪表盘和告警。

- 🧩 **指标类型与属性**：工作坊会讲解何时使用 counter、gauge 和 distribution，并说明如何添加 attributes，以便按用户、区域、release 或 feature flag 过滤和分组。
- 🔍 **联合排障**：演示如何结合 metrics、traces、logs 和 errors 调试，从指标尖峰跳转到其背后的具体 traces、errors 和 logs。
- 📊 **仪表盘与告警**：介绍如何把关键查询固定到仪表盘，并设置 monitors 来捕获阈值突破或异常，以便在用户发现问题前告警。

### [Reanimated 4.8.0 中的共享元素过渡](https://swmansion.com/blog/shared-element-transitions-in-reanimated-4-8-0/)

Reanimated 4.8.0 发布 Shared Element Transitions，通过 `sharedTransitionTag`、`SharedTransitionBoundary` 和 `isActive` 把共享元素动画从导航触发中解耦，并新增 `fadeContent`、真实视图连续性等能力；同时带来 `Animated.Text` 直接渲染共享值、CSS 渐变动画和一批底层性能优化。

- 🚀 **正式发布**：Reanimated 4.8.0 正式带来 Shared Element Transitions，结束此前实验版本在导航场景上的限制，并扩展同屏、Tab 与自定义导航流中的使用范围。
- 🧩 **使用方式**：用 `sharedTransitionTag` 关联两个 View，分别放入 `SharedTransitionBoundary`，切换边界上的 `isActive` 触发过渡；可配合 `useIsFocused` 在 react-navigation 或 expo-router 的屏幕切换时运行，并用 `sharedTransitionStyle` 自定义动画。
- ⚙️ **过渡机制**：过渡时先以 opacity 隐藏目标视图，将源视图从原父节点移除并挂到根节点顶层，动画到目标位置后在同一原子事务中把源视图放回原父节点并取消隐藏目标视图。
- 🧭 **边界控制**：`SharedTransitionBoundary` 将过渡生命周期与栈的 push/pop 解耦，显式用 `isActive` 控制是否运行，因此支持同一屏幕内两个容器、Tab Navigator 标签间过渡以及单屏自定义导航流。
- 🎨 **子内容淡化**：`fadeContent` 修饰 `SharedTransition` 构建器，解决共享元素在两端子组件不同的问题：源视图子内容淡出、目标视图子内容淡入；若子组件也共享，则继续执行各自的共享元素过渡。
- 🔄 **真实视图连续性**：实现不对视图做快照，而是动画真实视图；源和目标共享同一原生状态时，过渡期间可继续正常操作，例如雪花粒子不会冻结，源目标翻转时也不会跳到不同位置。
- 🛠️ **稳定化原因**：早期实现在旧架构下为 Android 和 iOS 各写一套并共享部分 JS/C++ 逻辑，边缘情况多、维护困难；新架构允许在 React Native 与平台之间插入共享 C++ 层，`SharedTransitionBoundary` 的 `isActive` 又让导航状态从当前渲染获取，降低维护成本并便于排查更新顺序相关 bug。
- 📝 **动画文本**：`Animated.Text` 可直接把 shared value 作为子节点渲染，UI 线程更新嵌套文本且不触发 React 重渲染；可与静态文本混用，格式化需求如取整或加单位用 `useDerivedValue` 包装。
- 🎨 **CSS 动画扩展**：CSS 动画和过渡支持对 `backgroundImage` 做动画，渐变可平滑插值颜色、色标位置、角度以及径向尺寸和位置；新增 `borderCurve`、`writingDirection`、`verticalAlign`、`objectFit` 支持，`PlatformColor` 值不再导致动画崩溃。
- ⚡ **性能优化**：4.8 减少 UI 线程和 JS 线程每帧的不必要工作，整体动画负担更轻。

### [发布 Worklets - 0.14.0 · software-mansion/react-native-reanimated · GitHub](https://github.com/software-mansion/react-native-reanimated/releases/tag/worklets-0.14.0)

react-native-reanimated 仓库发布 Worklets 0.14.0，重点加入 Worklet Runtimes 上的 WebSocket、可中止 Worker Runtime、同步调用 RN Runtime 与更可控的跨运行时序列化，并完善 Bundle Mode、运行时身份与性能正确性；该版本支持 React Native 0.87–0.89，配合 Reanimated 4.8.x。

- 🚀 **正式发布**：Worklets 0.14.0 发布，支持 React Native 0.87–0.89，并与 Reanimated 4.8.x 配对；同时停止支持 React Native 0.86。
- 🌐 **WebSocket 支持**：Worklet Runtimes 新增 WebSocket 支持，使运行在 Worklet 环境中的代码可直接使用 WebSocket。
- ⚙️ **运行时生命周期**：新增 abortWorkletRuntime 和 abortable 运行时选项，可停止 Worker Runtime，丢弃待处理工作并拒绝对应 Promise。
- 🔄 **同步调用 RN Runtime**：新增 runOnRNSync，可同步在 RN Runtime 上执行函数；在 Bundle Mode 下也可从 UI 和 Worker Runtimes 调用。
- 🧭 **跨运行时堆栈**：开发构建启用 ENABLE_CROSS_RUNTIME_STACK_TRACES 后，scheduleOnRN 和 runOnRNSync 抛出的错误可附带跨运行时堆栈。
- 🧩 **序列化控制**：新增 typed 的 createSerializable 变体，例如 createSerializableArray 和 createSerializableMap，只接受单一类型值；同时新增 setSerializableMapping、getSerializableMapping、hasSerializableMapping、removeSerializableMapping，用于控制其他运行时收到的替代值，并弃用 serializableMappingCache。
- 📦 **Bundle Mode 增强**：Bundle Mode 支持在 Worklet Runtimes 上 import() 懒加载 Metro chunk，加入 Metro 和 metro-runtime 0.87.0 补丁；iOS 开发包改为读取 React Native 0.88 及更新版本持久化的文件，避免重复下载。
- ⚡ **运行时性能**：UI Runtime 仅在存在待执行回调或 finalizer 时请求动画帧，而非每帧请求；同步调用产生的微任务在最外层调用返回时排空；运行时身份改用 React Native 实例和 runtime id 标识，修复旧运行时地址复用导致的崩溃和 use-after-free。
- 🐛 **关键修复**：修复 worklet 与其调用的 JS 函数互相持有导致的内存泄漏、createWorkletRuntime 初始化器抛错时 release 构建崩溃、RegExp、Error 和 typed array Serializable 被重复序列化，以及 Android 在无 Activity 且无 headless JS 任务时 UI runtime 帧循环仍随每次 vsync 运行等问题。
- 🛡️ **导入转发限制**：importForwarding.moduleNames 现在只匹配精确模块名，my-library 不再转发 my-library/utils，除非子路径也列入；relativePaths 仅含 src 等常见目录名时会警告，可用 silenceDangerousPathsWarning 关闭。
- 🛠️ **兼容与构建修复**：修复 iOS、tvOS、macOS 在 Xcode 27 上因隐私清单 bundle 部署目标导致的构建失败；为 Apple 的 performance.now() 时钟新增隐私清单声明，并修复 iOS Worklet Runtimes 上 performance.now() 与 RN Runtime 使用不同时钟的问题。

### [智能体真的在终结UI吗？](https://posthog.com/blog/agents-killing-ui?utm_source=twir&utm_campaign=nov25)

PostHog 的 Cleo Lant 撰文反驳「agent 正在杀死 UI」的流行说法：agent 确实成了软件的一类新用户，但界面并未消失，只是像当年的 API 和 GUI 一样，在产品之上又增加了一层。未来是混合（hybrid）而非无头（headless）——每个用户都会带着一个 agent 一起使用产品，因此构建者要为 agent 和人类分别设计入口，并把设计精力集中到审批、审查、撤销、可辨认性和编排这些真正需要人来判断的屏幕上。

- 🧩 **混合而非无头**：文章的核心论点是「我在用的一切都是用户界面」，agent 只是没在用你专门设计的那部分。headless 是叠加在产品构建之上的新一层，而非替代；产品构建者的工作因此翻倍：每个人类用户都会带来一个 agentic plus-one。
- 🔑 **首页不再是前门**：面向技术用户的上手流程越来越少从「get started」按钮开始，而是从终端或 AI 聊天窗口开始。用户可能经 Claude 或 ChatGPT 推荐（AEO）后由 agent 直接开通，永远看不到首页。但 agent 不一定会读安装文档，所以配置必须能被 agent 独立走完：容易找到、容易认证、一次调用完成而非十步。同时别忘了 agent 背后的人最终会打开产品，需要知道它做什么、下一步做什么。
- 🛠️ **两套入口的具体清单**：给 agent 的：能端到端完成的注册流程、在 Claude 和 Codex 等 agent 查找连接器的应用目录中有条目、可解析的文档（`llms.txt`、以纯 Markdown 提供的页面）、agent 即兴发挥时也安全的短时效 scoped token。给人的：若由 agent 代为设置，用户是从流程中段进入，要展示已完成与待完成；若自己点击进入，直接指向下一步。
- 💻 **文中实例**：`npx -y @posthog/wizard@latest` 一条命令创建账户、扫描代码库确定埋点位置并逐步在终端打日志，之后有人继续通过 MCP 以 headless 方式使用，也有人回到 Web 应用查看数据。Slack app 把消息提示变成 PR 草稿，但合并前仍要在 GitHub 看 diff（另一个 UI）。AgentMail 的文档教 agent 自助开通收件箱和密钥，但六位验证码仍需人接收并交付。
- 🔗 **AX 与 MCP**：computer-use 类 agent（如 Perplexity 的 Comet）会点击真实 DOM，但那是缓慢且「人形」的交互。agent 真正需要的是 AX（agent experience），当前标准是 Model Context Protocol：运行一个描述产品能力的服务端，agent 连接后直接与产品交互。要求是每个动作都有 agent 能执行的路径，以及人能核查它是否完成的路径。Vercel 的 MCP server 可查看部署、拉取运行时日志并触发部署，结果同步回仪表盘；PostHog 的 MCP server 让 agent 用你的凭证创建功能开关或实验，变更记入项目活动日志并附 `x-posthog-client` 头以区分 agent 与人的操作。
- 📈 **如何观测 agent**：agent 命中的是 API 而非前端，pageviews、autocapture 和 session replay 都捕不到它们的挫折信号；失败方式也不同：编造参数、认证墙、超时、幻觉出并不存在的工具，现有日志分类接不住。PostHog 因此做了 MCP Analytics，把每次工具调用（含 intent）转成事件；agent 去调用你并不存在的工具，等于机器人写的功能请求。上个月记录了近 1000 万次工具调用，来自 31 个 agent 客户端，背后是发短信告警、跑 A/B 测试、排查线上报错等真实工作。
- 🔍 **外部数据与配套设施**：Cloudflare Radar 6 月数据显示 HTML 流量中自动化请求首次超过人类，占 57.5% 对 42.5%，比其 CEO 的预测早约 18 个月。Temporal 把 agent 运行的每一步记录成可重放、可检查的持久事件历史，用来看循环卡在哪里或重复了什么。
- 🎨 **值得认真设计的六类屏幕**：审批（两秒内看懂自己在同意什么）、审查（给 diff 本身而非变更摘要）、撤销（agent 自主执行的动作旁要有回退）、可辨认（一屏内分辨同事与机器人的操作）、编排（五个 agent 是一屏看还是开五个对话）、打断（agent 运行中如何插手）。应降低会被 agent 取代的屏幕的优先级，把 MCP 当产品做；但 MCP 给的是触达而非质量，护城河可能是比对手更好用、更好看的 UI。Intercom 的 Fin Operator 把每项调整变成结构化提案（他们称之为 Operator 版的 pull request），由人审阅、编辑、批准后才生效；Anthropic 除了终端里的 Claude Code，还提供桌面应用、Web 应用、IDE 扩展和 Cowork。

### [Expo Services App 已发布：Workflows、Observe 和 Expo Simulators 现已登陆手机](https://expo.dev/changelog/expo-services-app)

Expo 发布 Expo Services App，将 Expo Workflows、Expo Observe 数据和 Expo Simulators 带到手机端，iOS 版本完全使用 Expo Exact 编写，让开发者不必只依赖 expo.dev 就能随时管理构建、工作流、性能监控和模拟器。应用已在 App Store 和 Google Play 上架，并适配 iPad 与 iPhone Duo；当前 Simulators 仅限 iOS 版，Android 模拟器、原生小组件、Live Activities 和更多 Observe 数据仍在开发中。

- 🚀 **正式发布**：Expo Services App 上架 App Store 和 Google Play，将 Expo Workflows、Expo Observe 数据与 Expo Simulators 集成到手机端；iOS 版完全用 Expo Exact 编写。
- 📊 **Observe 监控**：Overview 展示 TTI 图表、活跃用户和近期活动，可拖动图表读取每个数据点；项目未启用 Observe 时会显示添加指引或指向 Observe 文档。
- ⚙️ **工作流管理**：Workflows、Builds、Updates 和 Submissions 均有列表与详情页，可筛选运行、选择分支并带输入启动新运行，查看作业、日志和产物，安装或取消构建，以及重跑工作流。
- 💬 **完成通知**：在 Settings 中开启通知后，工作流运行完成会收到推送，点击推送可直接打开对应运行。
- 🧪 **模拟器测试**：可从构建启动云端 iOS 或 Android 模拟器并实时操作，设置位置和方向，观察 CPU、内存与网络变化；会话结束后保留截图、录屏、日志和性能摘要。
- ⚠️ **平台限制**：目前 Expo Simulators 仅在 iOS 版应用中提供，Android 版支持仍在开发，官方表示很快就会推出。
- 📱 **iPad 与 iPhone Duo**：应用在 iPad 上原生运行并提供侧边栏；在 iPhone Duo 上侧边栏跟随铰链，可调整大小或折叠。
- 🔮 **后续计划**：后续将加入 Android 模拟器、原生小组件、Live Activities 和更多 Observe 数据。
- 🔑 **登录与反馈**：支持邮箱密码、Google、GitHub、Apple、SSO 或 passkey 登录；可在应用内 Settings 发送反馈。

### [RFC：平台无关的 React Native 核心，作者 Abbondanzo · 拉取请求 #1037 · react-native-community/discussions-and-proposals · GitHub](https://github.com/react-native-community/discussions-and-proposals/pull/1037)

React Native 社区仓库出现一份编号 #1037 的 Draft RFC，提议让 `React Native core` 与具体平台解耦：核心仅保留共享 C++ 代码和声明的宿主平台接口，iOS、Android 及树外平台则从各自包中实现该接口，以降低核心对平台实现的耦合。

- 🎯 **提案目标**：将 `React Native core` 改为平台无关，使核心不再直接承载各平台实现，而是定义统一的宿主平台边界。
- 🧩 **核心机制**：核心只包含共享 C++ 与声明的宿主平台接口，平台相关能力通过该接口交由外部实现。
- 🌐 **平台实现**：iOS、Android 以及 out-of-tree 平台分别在自己的包中实现宿主平台接口，影响各平台维护者和树外平台适配方。
- 📝 **当前状态**：该 RFC 以 Draft 形式提交到 `discussions-and-proposals` 的 PR #1037，尚未合并，暂无评审、标签和里程碑。

### [Release 5.0.0-beta.2 · software-mansion/react-native-screens · GitHub](https://github.com/software-mansion/react-native-screens/releases/tag/5.0.0-beta.2)

react-native-screens 发布 5.0.0-beta.2，这是 5.0.0 的第二个 beta 版本，重点包括 iOS 上 Stack.Host 可导航 Split.Column、新增 PageSheet 与 ContainedModalReplacingContent 模态组件、Stack v5 的头部定制增强，以及 Stack、Tabs、FormSheet、Split 的多项修复和 v5 类型重命名；同时更新 Android SDK 版本并升级相关工程依赖。

- 🚀 **Beta 发布**：react-native-screens 5.0.0-beta.2 是 5.0.0 的第二个 beta，包含 iOS Stack.Host 导航 Split.Column、新模态组件和 Stack v5 头部定制等变更。
- 🧩 **模态组件**：新增 iOS PageSheet，它是基于 FormSheet host 的独立组件；同时新增 ContainedModalReplacingContent，并修复 ContainedModal 包含判断中的亚像素漂移问题。
- 🧩 **Split 与 Stack**：iOS 的 Stack.Host 现在可导航 Split.Column，并支持原生列隐藏；Split 列使用 stack navigation controller，处理 Split 折叠后列尺寸、重新定位，以及 Tabs、Sheet、ContainedModal 中的 Stack 不与 Split 集成等边界。
- 🎨 **Stack v5 头部**：Stack v5 增加按钮及 prominentButton 文本外观、按钮 tintColor、返回按钮外观和 header bar button items 的 axisBehavior；RNSStackHost 使用自有 shadow node，Stack screen 上报 UIKit 给出的 frame，并支持 Stack.Host 的 headless 模式。
- 📝 **Stack v4 排版**：Stack v4 为 header title、large title、back title 和 bar button items 增加 letter spacing。
- ⚙️ **Android SDK**：Android build.gradle 将 minimum SDK 提升到 24，compile SDK 和 target SDK 提升到 36。
- 🔄 **v5 重命名**：v5 类型存在破坏性重命名，包括 actionOrigin 值改为 camelCase、原生 FormSheet host 重命名为 Sheet，以及为 ContainedModalOverContent 和 ContainedModalReplacingContent 拆分独立 props 类型。
- 🐛 **缺陷修复**：修复 iOS FormSheet 回收与陈旧 content wrapper、Android FormSheet 拖拽与 grabber 高度、Android Tabs 移除与 SafeAreaView insets、Android Stack v4 过渡与 appear 事件、Android Stack v5 重复 screenKey，以及 iOS 交互式 fade 跟随手势等问题。
- 🛠️ **工程维护**：将 RN 升级到 0.89-rc.0，Android 独立库 Gradle 升至 9.4.1、AGP 9.2.1、Spotless 8，并迁移大量 v5 文档约定与测试、重构。

### [使用 Expo 模拟器的智能体工作流](https://expo.dev/blog/agentic-workflows-with-expo-simulators)

总结失败：模型未返回符合格式的摘要。

### [如何确定性地衡量 React Native 性能？| Argent 博客](https://argent.swmansion.com/blog/how-to-measure-react-native-performance-deterministically/)

文章给出了一套可重复的 React Native 性能测量方法：固定手势、数据、设备和度量工具，用 Argent E2E 回放手势、gfxinfo 统计帧、Flashlight 观察线程，并在冷却且同起始状态下对比构建；随后以 FlatList、FlashList、LegendList 的 10,000 行列表为示例展示流程、结果和局限。

- 🎯 **固定四个变量**：可比较的移动端性能数据必须保持手势、数据、设备和测量工具一致；手工滑动速度、随机 mock 数据、手机降频以及模拟器或 debug build 的误差，都会让两次运行无法直接比较。
- 🧩 **多线程瓶颈**：React Native 每帧涉及 JS 线程、UI 线程和 Android render thread，任一落后都可能掉帧；单一 FPS 会把未绘制时间算作流畅，因此最容易漏掉完全卡死的场景。
- 🧭 **工具分工**：Perfetto 和 Android Studio profiler 适合记录单次 trace 解释某帧为什么慢，但不能判断改动是否让屏幕更快；应先用多轮同条件测量回答是否变化，再用 trace 查原因。
- 🛠️ **手势回放**：Argent 通过 coding agent 把一次手势录成 `.argent/e2e/` 下的 YAML：`swipe` 的 `by` 使用屏幕高度比例，`duration` 固定，`momentum: false` 可精确停在手指位置；测试可用 `argent e2e run fling-down --device <adb serial>` 独立运行。
- 🔄 **一致起始状态**：每次测量前彻底停止应用，用 deep link 打开目标屏，等待首屏行可见日志，再执行 `adb shell dumpsys gfxinfo <package> reset`；同时使用保存的 API 响应或 mock server 固定数据。旧新构建应在同一次会话中连续测，因为 Android 可能在夜间后台 AOT 编译同一 APK，改变其速度。
- ⚙️ **冷却检查**：运行前要求 thermal status <=1、所有 cooling device 的 cur_state 为 0、每个 CPU 核的 `scaling_max_freq` 等于 `cpuinfo_max_freq`、电池已降温，并用 `adb shell top -n 1` 检查无其他 CPU 占用；单看一项不够，因为有些手机会不报告降频。
- 📊 **帧统计**：`adb shell dumpsys gfxinfo <package>` 给出总渲染帧数、janky 帧比例及 50/90/95/99 分位帧耗时；不能只读百分比，100% janky 既可能是持续卡顿，也可能是几乎没绘制，需结合总帧数判断。
- 🔍 **线程定位**：Flashlight 显示各线程繁忙度，JS 线程忙指向 React 渲染，UI 线程忙指向原生布局和绘制；但应忽略 Flashlight 的 FPS 数字，因为它把空闲时间计为流畅。
- 🧪 **对比构建**：流程是用 `flashlight test` 对当前构建跑 5 次并保存 `before.json`，只改一个变量后安装 release 构建保存 `after.json`，再执行 `flashlight report before.json after.json`；`--beforeEachCommand ./prepare.sh` 负责冷却和重置，`--testCommand` 串联 Argent E2E 与 `read-gfxinfo.sh`，`--skipRestart` 避免重复重启，结果波动大时增加迭代。
- 📦 **列表机制**：FlatList 默认在可视区周围约 21 屏高度内保持行挂载；FlashList v2 用 JavaScript 重写并依赖 New Architecture，通过 `getItemType` 分池回收行并逐行测量；LegendList 为纯 TypeScript，默认每个固定容器挂载新行组件，开启 `recycleItems` 后复用组件并传入新 item。
- 🧪 **基准配置**：在 Samsung Galaxy A21s 上，同一 release APK 使用 Expo SDK 58、React Native 0.88 New Architecture 与 Hermes、React 19.3，比较 FlatList、FlashList、LegendList 含/不含 `recycleItems` 四种实现；它们渲染同一份 10,000 行种子数据，每测试跑 3 次，覆盖冷启动、一次长 fling 和五次 `scrollToIndex` 远跳（5,000、9,999、2,500、顶部、7,500，每次限 5 秒）。
- 📈 **基准结果**：冷启动四者均约 1.7–2 秒，FlatList/FlashList 比 LegendList 快约 0.3 秒；长 fling 约 180 帧中仅 3–10 帧 janky，样本不足以排序；远跳 FlashList 和 LegendList 均低于 0.6 秒，无 `getItemLayout` 的 FlatList 五次中错过四次；FlatList 内存最高，FlashList 最低，LegendList CPU 占用最低。作者强调这些数字不能直接外推到其他屏幕和机型。
- 🧠 **Agent 技能**：仓库 `.claude/skills/` 提供 `rn-perf-gesture` 录制手势为 Argent E2E 测试、`rn-perf-measure` 在冷却手机和一致起始状态下测量、`rn-perf-compare` 比较两次测量并判断变更是否带来差异。

### [更多使用 React Native SDK 调试 Expo 应用的方法 | Sentry Blog](https://blog.sentry.io/expo-router-react-native-sdk/)

Sentry React Native SDK 发布一轮面向 Expo 的可观测性更新，核心是把 Expo Router 集成从手动接入改为自动注册的一等集成，并补上深链与导航关联、路由错误边界捕获、TTFD 与 OTA 更新耗时、Expo SDK 56+ 原生 fetch 网络追踪以及 Expo 构建的 source map 上传。更新后，开发者在完成少量配置的情况下即可获得更完整的导航、错误、性能与网络数据，减少自写插桩代码。

- 🧩 **自动注册集成**：`expoRouterIntegration()` 会读取 Expo Router 的内部 navigation ref，复用已有的 `reactNavigationIntegration`，在不使用 Expo Router 的项目中不执行操作；若 `Sentry.init()` 早于 Root Layout 挂载，它会重试等待导航 ref，而不是静默放弃。
- 🧭 **导航追踪**：屏幕聚焦事务开箱即用；用 `Sentry.wrapExpoRouter(useRouter())` 包裹后，`push`、`replace`、`navigate`、`back`、`dismiss`、`prefetch` 都会产生 breadcrumb 和短 span，后续 idle navigation transaction 带上 `navigation.method`，且 wrapper 幂等。
- 🔑 **路由隐私控制**：`route.href`、`route.params` 和由字符串 href 解析出的具体路径（如 `/users/42`）受 `sendDefaultPii` 控制；模板对象 href 的结构性 `route.name` 总会记录，关闭 PII 时具体字符串 href 会记为 `route.name: 'unknown'`。
- 🔗 **深链关联**：深链到达后紧接着开始的导航会被标记 `navigation.trigger: 'deeplink'`、`deeplink.url`（清洗并遵守 `sendDefaultPii`）和 `deeplink.dispatch_delay_ms`；覆盖冷启动 `Linking.getInitialURL()`、热启动 `url` 事件以及 Expo Router 抢先自动处理链接的场景。
- 🛡️ **路由错误捕获**：用 `Sentry.wrapExpoRouterErrorBoundary(ExpoErrorBoundary)` 包裹 Expo Router 的 `ErrorBoundary` 后，错误会带路由上下文上报，进行中的导航事务被标记为 errored，并添加 `expo-router.error_boundary` breadcrumb 和 `expo_router_error_boundary` 机制；按错误实例去重，支持 `{ error, retry }` 自定义 fallback。
- 🛠️ **构建时自动包裹**：在 Metro 配置中通过 `getSentryExpoConfig(__dirname, { autoWrapExpoRouterErrorBoundary: true })` 启用后，Sentry Babel 插件会把 `export { ErrorBoundary } from 'expo-router'` 自动改写为包裹版本，无需逐个修改路由文件，新屏幕也会自动覆盖。
- 📈 **性能信号**：`Sentry.reportFullyDisplayed()` 可在数据加载完成、屏幕可用时记录 Time to Full Display，与 TTID 形成差值；Expo Updates listener 为 `app.update.check` 和 `app.update.download` 记录耗时 span，用于定位 OTA 更新慢在检查还是下载阶段。
- 🌐 **原生 fetch 追踪**：Expo SDK 56+ 用原生 `fetch` 替代基于 `XMLHttpRequest` 的 `globalThis.fetch`，导致旧捕获方式漏掉请求；SDK 现在检测并直接追踪原生 fetch，每个请求只记录一次，无需改代码，未使用该实现的应用行为不变。
- 📦 **Source map 支持**：新增 `@sentry/expo-upload-sourcemaps` 用于上传 source map；Metro 启动时若预构建原生项目缺少 Sentry 配置会告警，避免生产环境堆栈指向压缩后的行列。
- 🚀 **升级方式**：上述能力随最新 `@sentry/react-native` 提供，可通过 `npx expo install @sentry/react-native` 安装，并添加 `expoRouterIntegration()`、开启 `autoWrapExpoRouterErrorBoundary` 来启用导航追踪、深链关联和路由错误捕获。

### [Codemagic Patch | 适用于 React Native 的自托管 OTA 更新](https://patch.codemagic.io/?utm_source=newsletter&utm_medium=referral&utm_campaign=twir)

Codemagic 的 Patch 面向 React Native 和 Capacitor 提供自托管 OTA 更新方案，目标是用一条命令和 Docker Compose 快速搭建可扩展的更新服务，并覆盖指纹校验、二进制差分包、发布监控与回滚、CDN 分发和团队权限等能力。其意义在于把现代托管 OTA 服务的控制与管理能力下沉到自托管栈，降低安装和运维门槛，同时让团队掌控发布流程并支撑大规模用户。

- 🚀 **自托管 OTA**：Patch 为 React Native 和 Capacitor 应用提供自托管 OTA 更新，覆盖现代托管 OTA 服务的更新控制与管理能力，且不采用五位数价格标签；官方强调即便数百万用户也有高效安装与架构。
- ⚡ **快速安装**：运行 `cmpatch selfhost install` 启动安装向导，自动配置 OAuth、CDN 缓存规则和 TLS，再用 Docker Compose 启动整套服务；官方称二十分钟可完成安装。
- 🛡️ **指纹校验**：Fingerprinting 会检查目标原生二进制，阻止与目标二进制不兼容的发布，降低错误下发风险。
- 📦 **差分包更新**：Binary diff 只发送变更内容，设备下载小体积 diff 而非完整 bundle，减少对良好移动信号的依赖。
- 📈 **发布管控**：Dashboard 提供每次发布的完整指标，并支持 rollout、安装监控、版本晋升和回滚控制；CLI 也可访问发布指标。
- 🌐 **CDN 扩展**：设备把检查和下载请求发给 CDN，服务器不会被打满；对比中 Patch 的吞吐随 CDN 扩展，停机仅在 CDN 故障时发生，而其他方案常需自行做 autoscaling 与缓存，API 故障会阻断检查。
- 🔄 **安装时机**：支持 immediate、restart、resume、suspend 等安装模式；对比中其他自托管 OTA 的安装时机主要围绕 `sync()` 安装模式。
- 🏢 **团队与支持**：提供带团队访问的 Web dashboard、dashboard 内 RBAC 和可购买的支持许可证；对比中其他工具的用户角色、dashboard 能力因工具而异，支持通常只有 GitHub issues。
- 🧭 **厂商背景**：Patch 由 Codemagic 构建；Codemagic 深耕移动 CI/CD 超过 10 年，团队已向生产应用交付数十亿次 OTA 更新，Patch 将该经验带入自托管栈。

### [发布 · wcandillon/react-native-skia · GitHub](https://github.com/wcandillon/react-native-skia/releases)

react-native-skia 在 2026 年 11 月连续发布 v3.10.1 至 v3.13.1，并推送 Binaries 158.1.0 与 Skia wasm m158 预发布包；更新集中在 Surface 录制与 GPU 资源管理、原生二进制分发、WebGL/WebGPU 兼容、Skottie/SkFont 原生 API 暴露以及多平台渲染稳定性修复，旨在改善跨平台图形应用的性能、构建便利性和运行可靠性。

- 🧩 **Surface 录制**：v3.13.0 新增 `Surface.flushAsync()`（#4532），改为每个离屏 surface 一个 recorder，并新增 `Skia.purgeGpuResources()`（#4520）；同时修复 surface 录制丢失，以及 `outputImage` 无快照时仍保留的问题（#4531）。
- 🛡️ **iOS 构建修复**：v3.13.1 不再把 build stamp 命名为 `.signature`，避免触发 ITMS-91063（#4540，关闭 #4539）。
- 📦 **原生二进制分发**：v3.12.0 支持通过 GitHub Releases 下载 Apple 二进制供 CocoaPods/SPM 使用（#4521）；v3.11.0 支持从 GitHub Releases 下载 Android 二进制（#4484）。
- 🌐 **WebGL 兼容**：v3.11.1 在共享 WebGL 上下文上保留更多视图尺寸的 surface（#4523），并确保 tree-shaken 包中仍保留 Web 端 `SkiaViewApi` 初始化（#4490）。
- 🧩 **原生 API 暴露**：v3.11.1 在原生端暴露 Skottie 的 `setOpacity` 与 `setTransform`（#4506），以及 `SkFont` 的 `isEmbolden` 与 `setEmbeddedBitmaps`（#4507）。
- ⚙️ **Android 稳定性**：v3.11.1 通过单一连接加载远程资源后关闭（#4513），并在所有 Android 设备跳过 Dawn 的 AHardwareBuffer 尺寸检查（#4510）；v3.10.1 还修复 Android 显示密度变化跟随（#4448）及 Android 10 上旋转圆角裁剪下的不透明 TextureView 画布问题（#4228）。
- ⚡ **渲染性能**：v3.11.0 修复 macOS 14+ ProMotion 设备未满帧呈现（#4481），支持在透视矩阵下用 `drawAtlas` 绘制 atlas（#4500）；v3.10.2 用单一调度器控制画布帧节奏，并在 Android 上为 GPU 保留 present（#4478）。
- 🐛 **渲染稳定性**：v3.10.1 修复 WebGL 无法创建 surface 时 draw 抛错（#4440）、已销毁但仍显示在屏上的画布帧保留（#4438）、节点先画自身 paint 再画子节点（#4450）、渲染线程竞态（#4453）及忙时 trim 后空闲再 trim（#4347）。
- 🐛 **交互与文本修复**：v3.10.2 丢弃请求超时后到达的 `e2e` 回复（#4466，关闭 #4458），并使用缓存 text blob 进行绘制（#4473）。
- 🧪 **预发布二进制**：Binaries 158.1.0 为预发布，提供预构建 Skia Graphite（m158a）与 Dawn 二进制；Android 库按 ABI 分组，Apple 静态库按 SDK 分组，并附带兼容 npm 包和记录全部资产 sha256 的 `checksums.json`。
- 🌐 **Skia wasm**：Skia wasm m158 为预发布，面向浏览器 WebGPU 的 Skia Graphite 使用 Emscripten 4.0.7 构建，包含静态 wasm 归档、Skia 头文件、`emdawnwebgpu` 包和 `metadata.json`，由 `skia-wasm` 消费。

### [在 GitHub Sponsors 上赞助 @wcandillon · GitHub](https://github.com/sponsors/wcandillon)

该页面是 William Candillon（wcandillon）为 React Native WebGPU 与 React Native Skia 发起的 GitHub Sponsors 介绍，核心是构建面向 React Native 的统一 GPU 运行时，并以 Dawn 和 Skia 为基础实现 2D、3D 与机器学习共享画布，同时保持对各平台原生表面、帧节奏和媒体管线的深度集成；相关模块在 NPM 的下载量已超过 7000 万次，赞助用于支持这些开源工作及其面向头部应用的持续维护。

- 🧭 **项目定位**：William Candillon 是 React Native WebGPU 和 React Native Skia 的作者，目标包括为 React Native 提供统一 GPU 运行时，以及在不牺牲平台能力的前提下实现完整的原生控制。
- 🧩 **统一渲染机制**：2D 绘图、3D 场景和机器学习模型可在同一画布上以零成本共享，该模型基于 Dawn 和 Skia 构建，并受 Google Chrome 图形栈启发。
- ⚙️ **原生平台集成**：项目强调与各平台原生原语深度集成，包括每个画布背后的原生 surface、由显示设备驱动的 frame pacing，以及平台媒体管线；对 Web 的对称性不以牺牲平台为代价。
- 📈 **采用规模**：相关模块在 NPM 的下载量已超过 7000 万次，并支撑 App Store 和 Google Play 上部分头部应用的用户体验，其中包含获得 Apple、Google 和 Expo 奖项的应用。
- 🎯 **赞助层级**：赞助档位为每月 10、50、200、500、1000、2500 美元：200 美元档含一次 1 对 1 通话和 issue 优先级，500 美元档加每月 2 小时咨询，1000 美元档改为每月 4 小时并可在下一次 YouTube 公告中展示工作，2500 美元档改为每月 6 小时并可在 React Native Skia 和 React Native WebGPU 的 README（GitHub 与 npm）赞助区获得 platinum 名称和 logo 位置及可选视频片段。
- 📦 **相关仓库**：Featured work 包括 `wcandillon/react-native-webgpu`（由 Dawn 驱动的 React Native WebGPU，1,291 星）、`wcandillon/react-native-skia`（基于 Skia 的高性能图形，8,792 星）、`wcandillon/skia-wasm`（Skia Graphite 的 WebAssembly 版本，36 星）和 `wcandillon/can-it-be-done-in-react-native`（YouTube 系列项目，4,193 星）。

### [发布 · wcandillon/react-native-webgpu · GitHub](https://github.com/wcandillon/react-native-webgpu/releases)

react-native-webgpu 在 2026-11-03 至 2026-11-25 连续发布 v0.21.0 到 v0.26.0，重点完善 Apple 与 Android 平台支持、GPU 资源管理、原生缓冲区展示和运行时性能。核心变化包括新增 `purgeGpuResources()` 与 `NativeBufferView`，让 `createNativeBufferFromPointer` 支持 `colorSpace`，改进 Dawn 二进制分发与跨启动管线缓存，并修复多项 Apple 平台和 Android 渲染问题。

- 🚀 **v0.26.0**：v0.26.0 于 2026-11-25 发布，`createNativeBufferFromPointer` 增加 `colorSpace` 参数；修复 Apple 构建标记被命名为 `.signature` 导致的 ITMS-91063 问题。
- ⚙️ **GPU 资源清理**：v0.25.0 新增 `purgeGpuResources()`，并在系统内存不足时主动清理 GPU 资源。
- 📦 **Apple 二进制**：v0.24.0 支持通过 GitHub Releases 下载 Apple 二进制，供 CocoaPods/SPM 使用。
- 🎨 **NativeBufferView**：v0.23.0 新增 `NativeBufferView`，这是一个仅用于显示原生缓冲区的视图。
- 🔄 **帧调度**：v0.23.0 让 `requestAnimationFrame` 由显示刷新节奏驱动，并在每个 runtime 上生效。
- 🛠️ **平台修复**：v0.22.0 修复 macOS 上 WebGPU 的编译与关闭，并在主线程按仅挂载时的 Canvas props 标记 `CAMetalLayer` 色彩空间；Android 改为从二进制 release 下载 Dawn。
- 🐛 **v0.21.4 修复**：v0.21.4 在 iOS 模拟器关闭 `metal_disable_sampler_compare`，修复 Android 10 旋转圆角裁剪下 `TextureView` 画布可见性，并丢弃 e2e 调用超时后到达的回复。
- 🔧 **Dawn 升级**：v0.21.3 将 Dawn 升级至 158.0.0。
- ⚡ **性能优化**：v0.21.2 用一步创建带原型的原生对象包装器，使 `device.queue` 每次读取返回同一个 `GPUQueue`，并修复 null slot 后续索引；CocoaPods 使用 `use_frameworks!` 构建。
- ✅ **tvOS**：v0.21.1 在 podspec 中声明 tvOS，使 autolinking 在 Apple TV 上链接该 pod。
- 🧩 **管线缓存**：v0.21.0 恢复 tvOS 和 visionOS 构建，并在 CI 检查每个 Apple SDK，同时跨启动保留 Dawn 编译管线。

### [版本 1.24 — Swift Package Manager 与按需 Android 视图管理器 📦 | Keyboard Controller](https://kirillzyusko.github.io/react-native-keyboard-controller/blog/release-1-24)

React Native 键盘控制库发布 1.24.0，这是 React Native 0.89 之前的一个刻意小型版本，仅包含两项改动：iOS 端加入 Swift Package Manager 支持，Android 端支持按需注册 view manager。CocoaPods 与既有 React Native 版本仍受支持，同时作者也公布了 iOS 交互式返回滑动修复、示例应用迁移和 Android 17 端到端测试等后续计划。

- 📦 **版本定位**：1.24.0 是 React Native 0.89 之前的一个刻意小型版本，只加入 iOS SwiftPM 支持与 Android on-demand view managers 两项变化。
- 🧩 **iOS SwiftPM**：npm 包中新增 `Package.swift` manifest，使用 SwiftPM 的 React Native 应用可以自动链接该库；CocoaPods 仍受支持，1.24.0 继续兼容此前支持的 React Native 版本，并可与 React Native 0.88 的 opt-in SwiftPM 配置配合使用。
- ⚙️ **Android 按需 ViewManager**：`KeyboardControllerPackage` 实现了 `ViewManagerOnDemandReactPackage`，当原生视图只在后续屏幕出现时，React Native 可以延迟到需要时再完成该库视图的配置。
- 📊 **性能数据**：`UIManager.getConstants` 的 JS 线程 CPU 中位耗时从 29.9 ms 降至 27.0 ms，节省约 3 ms；对单个包而言收益不大，但多个原生模块都采用这种延迟方式时，节省会逐步累积并加快启动速度。
- 🎯 **下一步：iOS 返回滑动**：作者正在处理 iOS 交互式返回滑动：撰写回复时侧滑返回，composer 需要全程与键盘保持同步。修复前 composer 会落到键盘后面，修复后保持在键盘上方，计划在新年前随 1.25.0 发布。
- 🧪 **测试与示例**：所有示例应用已迁移到 React Navigation 的 native stack，可在原生屏幕转场过程中测试键盘行为；同时正在推进 Android 17 上的端到端测试，以提前发现特定版本的问题。
- 💬 **问题优先级**：作者的首要任务是解决开放 issue：👍 反应较多的问题优先处理，标记为 sponsor 💖 的问题作为赞助者专属支持获得最高优先级。

### [版本发布 · callstackincubator/voltra · GitHub](https://github.com/callstackincubator/voltra/releases)

Voltra 发布页面汇总了从 v2.1.0 到 v2.7.0 的迭代，近期版本集中完善 Dynamic Widgets 与 Dynamic Live Activities 的跨端渲染、失败诊断、服务端驱动和配置持久化，并补齐 Android 小组件边框、间距与通知呈现能力；这些变化让小组件在应用未运行、发布构建和异常状态下更可诊断，也更接近 iOS 与 Android 的一致体验。

- ⚠️ **渲染失败可诊断**：v2.7.0 让 iOS Dynamic Widgets 在 Debug 构建的 Home Screen 显示错误视图，包含 widget id、失败阶段、错误信息和堆栈（含 `voltra/<id>.bundle:line:column`）；iOS 17+ 点击会从 Metro 重新加载 bundle 并重试，Release 构建保留每个 widget、配置、尺寸和外观的最后成功渲染，失败记录在 `widget` 类别。该策略与 Android 在 v2.6.0 引入的 Dynamic Widgets 渲染失败处理一致。
- 🎨 **iOS 渐变支持**：v2.7.0 在 iOS 支持 `style.backgroundImage` 的 `linear-gradient`、`radial-gradient` 和 `conic-gradient`，绘制在 `backgroundColor` 之上，使同一 style 在 iOS 与 Android 呈现相同渐变；`backgroundColor` 中的渐变字符串继续可用。同时修复自 1.3.0 起色标无显式位置的渐变不渲染的问题，例如 `linear-gradient(to right, red, blue)`。
- 🔧 **兼容与抓取修复**：v2.7.0 修复 iOS 应用内 `VoltraView` 在 React Native 0.88（Expo SDK 58）首渲染中止 Debug 构建的问题，此前会从错误对象读取首批 props，在 Release 中也属未定义行为；Android 服务端驱动的 Dynamic Widgets 放置时只抓取一次，不再抓取两次。
- 📦 **发布构建打包修复**：v2.6.1 修复同时使用 Dynamic Widgets 和 Dynamic Live Activities 的 iOS Release 构建：自 2.3.0 起，在同时配置 Dynamic Live Activities 的应用中，widget extension 的打包步骤被覆盖为只打包 Live Activities，导致 Widgets 在 Release 中无法加载 bundle 并持续显示预渲染初始状态。全新 `expo prebuild` 后会重写该步骤，覆盖 EAS 和其他 CNG 构建，升级即可。
- 🧩 **类型与依赖工程**：v2.6.1 让类型声明中的 `react/jsx-runtime` 导入在 `bundler`、`node16` 等支持 `exports` 的模块解析下正确解析，此前这些类型会退化为 `any`；示例应用升级到 Expo SDK 58，仓库 lockfile 不再引入存在已知严重漏洞的包。
- 🎨 **Android 布局补齐**：v2.6.0 让 Android 小组件支持 `borderWidth` 和 `borderColor`，遵循 `borderRadius` 并可与 `backgroundColor` 或 `backgroundImage` 渐变组合，边框绘制在组件边界内不改变布局；仅对 `width` 和 `height` 均为固定数值的组件生效，`flex` 子组件无边框并记录原因。`Column`、`Row`、`LazyColumn` 和 `LazyVerticalGrid` 的 `gap` 开始生效，自适应列的 `LazyVerticalGrid` 外边缘获得一半 gap；`LazyColumn` 和 `LazyVerticalGrid` 也能在 `VoltraWidgetPreview` 中渲染，Android 12（API 31）及更早版本以非滚动近似形式显示。
- ⚠️ **Breaking 清理**：v2.6.0 中 `@use-voltra/android` 不再导出 `renderAndroidLiveUpdateToJson()`、`renderAndroidLiveUpdateToString()` 或 `AndroidLiveUpdate*` 类型，`@use-voltra/android-client` 也不再重新导出；这些是废弃渲染器遗留，设备端无法显示其输出。通过 `requestPromotedOngoing` 的 Android 16 Live Updates 不受影响。
- 🔄 **Live Activity 状态与交互**：v2.5.0 在 iOS 新增 `getLiveActivityPushTokens()`、`getLiveActivityPushToStartToken()`、`areLiveActivitiesEnabled()` 和 `activityEnablementChanged` 事件。按钮和开关的 `interaction` 事件只投递一次，应用已处理的点击不会在下次启动或重载时重放；应用被杀或后台时的点击会在挂载 `interaction` 监听器后到达，最多保留 15 分钟和最近 100 条，每个事件带唯一 `id`，挂载的 `VoltraView` 不再接收本应给 Live Activities 的点击。跨启动保留点击和在应用进程外接收点击需要插件配置 `groupIdentifier`；升级会丢弃旧版本排队的点击，直接订阅 `getNativeVoltra().onInteraction` 的代码需改用 `addVoltraListener('interaction')`。
- 🐛 **Android 稳定性**：v2.5.0 为 WorkManager 通过反射创建的类提供 keep 规则，修复 R8 压缩的 Android Release 构建启动崩溃 `Failed to create an instance of class androidx.work.impl.WorkDatabase…`，该问题在默认压缩 Release 的 Expo SDK 58 模板中被报告。`useAndroidOngoingNotification()` 在通知被划走、超时或被其他代码停止时报告 `isActive: false`，`startAndroidOngoingNotification()` 和 hook 的 `start()` 可在关闭或超时后再次发布，包括同一 `notificationId`，而更新和 upsert 不会恢复已关闭通知；固定宽高的 `Image` 的 `borderRadius` 在 Android 11 及更早版本也生效，并修复 Samsung One UI 8 上 promoted ongoing notifications 大图标贴边裁切。
- 🚀 **Android Live Updates 增强**：v2.4.0 针对 ongoing notifications 打磨 Android 16 Live Updates，并加入 Android 17 `MetricStyle` 的 Metric 布局；新增 SwiftUI 与 Jetpack Glance 原生修饰符、Dynamic Widgets 和 Dynamic Live Activities 本地化、BigPicture 与 Inbox ongoing notification payload、ongoing notification 展示选项，同时修复 `compileSdk 36` 应用与 Metric 布局的兼容及 Android 16.0 上 promoted notification 权限要求。
- 🧩 **服务端驱动与实例配置**：v2.3.0 引入服务端驱动的 Dynamic Widgets，小组件可按 placement 按计划从服务器获取自身 props，不再只依赖应用推送更新；Android 每个已放置小组件可通过 `setWidgetInstanceConfiguration` 保存自己的设置（如一个显示 London、另一个显示 New York），并能在启动器备份/恢复后保留。该版本还让 Android 支持 Android 7.0-11（API 24-30）、小组件 resize 边界、始终输出 `minWidth` 和 `minHeight`，iOS 增加 `kind` 选项以便迁移后保留已放置小组件。
- 🧪 **实验性动态 Live Activity**：v2.3.0 在 iOS 以实验性方式引入 Dynamic Live Activities，可用小型 JSON prop 更新驱动 Live Activities，而不必每次传完整重渲染 payload，并支持构建时热重载；Android 新增 `ArcProgressIndicator` 确定性弧形仪表组件，支持可配置描边宽度、角度、圆角/平端和渐变填充。
- 🛠️ **运行时 props 与构建加固**：v2.2.0 支持 Dynamic Widgets 的运行时 props，并加固 iOS Podfile widget target 生成、Xcode 项目与既有 app extensions 共存、Android 构建打包管线；修复 Android 上 RN 0.81.5 及以下 Hermes prefab target，确保 16 KB ELF 对齐，统一 iOS widget Xcode 管线并支持按构建配置签名和版本传递，还在布局子项超限时发出警告。
- 🚀 **Dynamic Widgets 起点**：v2.1.0 引入实验性 Dynamic Widgets，基于 Voltra 新的原生侧渲染引擎，将 Voltra 组件单独打包并在专用 JS VM 实例中渲染，使其在应用未运行时也能响应环境变化，例如根据 iOS 渲染模式 full color 或 accented 调整布局；该功能需要显式 opt-in，并提供 iOS 与 Android 文档。

### [TypeGPU Kit | TypeGPU Kit](https://docs.swmansion.com/typegpu-kit/)

TypeGPU Kit 将 GPU 模块集中到 `@typegpu/kit` 包中，基于 TypeGPU 在 WebGPU 浏览器和 React Native 中提供可互换的构建块；模块借用调用方传入的 root 并向指定 pass 录制内容，而 loop、frame 与 canvas 仍由开发者掌握，从而降低组装实时 GPU 场景与后处理管线的成本。

- 🚀 **包入口**：TypeGPU Kit 提供统一的 `@typegpu/kit` 包，可通过 `pnpm create @typegpu/kit` 开始使用，并用自有代码补齐模块未覆盖的部分。
- 🧩 **模块机制**：每个 module 是一项 GPU 工作，由工厂借用 root 创建，返回资源、shader 函数和可向 frame 录制的方法；模块按需替换和组合。
- 🔄 **帧所有权**：Kit 不接管主循环，开发者拥有 loop、frame 和 canvas；frame 对象持有 encoder、时间以及距上一帧的时间，模块向调用方提供的 pass 中记录。
- 🔍 **邻近查询**：示例用 `kit.table` 为每只鸟存储位置、朝向和力的 9 个 word，用 `kit.grid` 按单元格统计鸟数并在自身及附近单元格查找邻居，为 steering 提供候选。
- 🎨 **渲染与后处理**：示例串联 `kit.lighting` 的阴影贴图与太阳/灯光、`kit.passes` 的颜色/法线/深度场景 pass、`kit.bloom` 的 5 级模糊辉光，以及 `kit.finish` 的色调映射、暗角和抖动输出。
- ⚙️ **自定义规则**：`createSteering` 接收带 `'use gpu'` 的 TypeScript 函数，从鸟与邻居状态计算力；示例包含 `flock`、`orbit`、`huddle` 三种规则。
- 📚 **模块目录**：模块覆盖 Core、Rendering、Post-processing、Particles、Text、Assets 等类别；依赖关系图用虚线表示被依赖模块还会填充调用方 shader 的 accessors。
- 💻 **示例与调试**：Jelly world、Classroom、Falling sand、Ocean、Censer 等示例可全屏打开，并包含 GPU debug panel；Ocean 使用 FFT 波、泡沫和低太阳，Classroom 使用烘焙 lightmap 与尘埃光束。

### [版本 1.3.0：传送后的视图始终知道自己的位置 🧭 | Teleport](https://kirillzyusko.github.io/react-native-teleport/blog/1-3-0-measurements-rewrite)

`react-native-teleport` 发布 `1.3.0`，重写了 Fabric 对传送内容的测量方式：不再维护预计算的 native offset，而是把传送的 `Portal` 标记为 shadow tree 中的根节点，测量时直接读取 host 在同一 shadow tree revision 中的位置。这修复了滚动后 `measure()` 和 `Pressable` 使用旧位置的问题，并消除一类 stale position bug；API 不变，但因最低 React Native 版本和 iOS 链接方式变化而作为 minor 版本发布。

- 🚀 **正式发布**：`react-native-teleport` `1.3.0` 发布，核心是重写 Fabric 对 teleported 内容的测量，解决 `measure()` 和 `Pressable` 在滚动后仍指向旧位置的问题，并消除一类 stale position bug。
- 🧩 **核心机制**：传送的 `Portal` 在 shadow tree 中被标记为根节点（`RootNodeKind` trait）；Fabric 测量到它时停止向上遍历，改为从同一 shadow tree revision 读取 host 位置继续计算，公式由 `Portal + offset` 变为 `host`。
- ✅ **旧方案问题**：自 `1.1.10`（#150）起使用 native 侧缓存的 `host − source` offset 修正位置；当 `Portal` 位于 `ScrollView` 中并滚动时，offset 不会重算，测量偏差正好等于滚动距离，导致 `Pressable` 取消按压（#220）。
- ⚡ **性能与实现**：不再有缓存 offset，无需每帧同步或重算；位置只在被询问时计算；native 侧只需报告子节点挂载到哪个 host 及其尺寸，iOS 和 Android 上的屏幕偏移计算及布局、挂载 hook 被移除。
- 🐛 **Android 闪烁修复**：`1.3.0` 同时修复 Android 上 `Portal` 切换 host 时的一帧闪烁（#228）：在更改 `hostName` 的同一次 commit 中采用新 host 尺寸，避免先用旧 host 布局绘制一帧。
- ⚠️ **版本与兼容性**：无 API 变化，但库通过 Fabric `UIManager`（`ShadowTreeRevisionProvider`）和 `RuntimeScheduler` 读取 shadow tree，最低支持 React Native `0.78`；iOS 依赖更多 pod，使用 `use_frameworks!` 且从源码构建 RN 时，podspec 声明 `React-runtimescheduler`、`React-performancetimeline` 以及到 RN `0.81` 为止的 `React-jsinspectortracing`，因此发 minor 而非 patch。
- 🛠️ **升级方式**：执行 `yarn add react-native-teleport@1.3.0` 并在 `ios` 目录运行 `pod install`；React Native `< 0.78` 应继续使用 `1.2.x`，升级后遇到位置错误、按压取消或构建问题需附 RN 版本和复现开 issue。

### [React Native Bottom Sheet 1.1.0](https://swmansion.com/changelog/react-native-bottom-sheet-1-1-0/)

React Native Bottom Sheet 于 2026 年 11 月 16 日发布 1.1.0 小版本，为 iOS、Android 和 Web 的 `BottomSheet` 与 `ModalBottomSheet` 新增 `maxWidth` 和 `placement` 布局属性，同时减少 iOS 动画卡顿并修复三端动画最终帧跳动，使 sheet 的宽度控制、对齐方式和停靠动画更稳定可配。

- 🚀 **版本发布**：1.1.0 是 Minor Release，面向 iOS、Android 和 Web 上使用 `BottomSheet` 与 `ModalBottomSheet` 的用户。
- 🧩 **宽度上限**：新增 `maxWidth`，以 points 为单位限制 sheet 宽度且包含 detent 的 side insets；容器更窄时仍使用可用宽度；省略或传入 `Infinity` 表示不设上限。
- 🎯 **对齐控制**：新增 `placement`，在宽度上限留下额外空间时控制对齐，默认 `'center'`，可设为 `'start'` 或 `'end'` 以按当前布局方向对应边缘对齐；`maxWidth` 和 `placement` 均可在 sheet 打开时动态变更。
- ⚡ **动画优化**：减少 iOS 上 sheet 动画到 detent 时的卡顿。
- 🐛 **最终帧修复**：修复 iOS、Android 和 Web 上的最终帧跳动，sheet 会在目标 detent 减速停止，从关闭到全高打开时最明显；本次发布处理 #87、#95、#131，感谢 @Gnative 贡献。

### [发布 v6.3.0 · gre/react-native-view-shot · GitHub](https://github.com/gre/react-native-view-shot/releases/tag/v6.3.0)

react-native-view-shot 发布 v6.3.0，新增 iOS `tmpfile` 捕获的 `fileName` 支持和跨平台 `sizeUnit` 选项，并集中修复 Android 截图、Gradle/ProGuard、TypeScript 类型以及 iOS/Windows 捕获行为。此次更新让 Android 与 iOS 的文件名行为对齐、统一各平台尺寸语义，并通过 PixelCopy 改善地图/视频等 TextureView 的截图层级，同时清理弃用 API 并提升类型兼容性。

- 🎯 **iOS fileName**：iOS 的 `tmpfile` 捕获现在支持 `fileName`，行为与 Android 一致：该值是文件名前缀，后接唯一后缀和扩展名；iOS 过去忽略 `fileName`，现在与 Android 一样，在名称少于 3 个字符或包含 `/` 时拒绝捕获。
- ⚙️ **sizeUnit**：新增 `sizeUnit` 选项（`dp` 或 `px`），让 `width`/`height` 在各平台含义一致；不设置时，iOS 和 Windows 仍按 points/dp，Android 和 web 仍按像素。
- 🧩 **Android captureScreen**：Android 的 `captureScreen` 在 API 26+ 使用 PixelCopy 截取窗口，使地图或视频等 TextureView 与绘制在其上的视图保持 z-order；启用 `handleGLSurfaceViewOnAndroid` 或 PixelCopy 失败时回退到旧绘制路径。
- 🛠️ **弃用 API 清理**：Android 停止使用 React Native 0.88 和 Android 中弃用的 `TurboReactPackage`、`getCurrentActivity()`、`GuardedAsyncTask`、`CompressFormat.WEBP` 等 API，以消除构建警告。
- 🏢 **Gradle/AGP 调整**：Android 移除 Gradle 10 和 AGP 8 弃用的 Gradle 语法与属性，包括空格赋值属性、方法式 `compileSdkVersion`/`minSdkVersion`、manifest 的 `package` 属性以及库的 `versionCode`/`versionName`；`namespace` 现在始终设置，因此不再支持 AGP 7 或更旧版本（React Native 0.80+ 已要求 AGP 8）。
- 📦 **Android 默认 SDK**：当应用未定义时，库默认 `compileSdkVersion` 为 35（原 34）、`minSdkVersion` 为 24（原 21），且不再设置 `targetSdkVersion`；React Native 0.80+ 模板已定义这些值，因此多数应用不受影响。
- 🛡️ **ProGuard/R8**：Android 为原生模块提供显式 consumer ProGuard/R8 规则，不再只依赖 React Native 自身的 keep 规则。
- ✅ **fileName 安全化**：`fileName` 选项会把字母、数字、`.`、`_` 和 `-` 之外的字符替换为 `_`（并给出开发警告），确保生成的 `tmpfile` 路径始终可安全转换为 `file://` URL。
- 🔄 **TypeScript 兼容**：改用 type-only imports，使启用 `verbatimModuleSyntax` 的 React Native 使用方在类型检查库源码时不再触发 TS1484 错误。
- 🔍 **iOS captureScreen**：iOS 的 `captureScreen` 使用前台场景的 key window 而非弃用的 `keyWindow`，在应用处于后台时仍可工作，并在无可用窗口时以清晰消息拒绝。
- 🧪 **TS 严格选项修复**：修复启用 `exactOptionalPropertyTypes` 或 `noPropertyAccessFromIndexSignature` 的应用中的 TypeScript 错误；React Native 会通过 `react-native` 导出条件用应用自身编译选项检查该包 `src/`，此时 `skipLibCheck` 不生效。
- 💻 **Windows 尺寸**：Windows 将 `width`/`height` 按小数读取而非截断，并按远离零的方式对半像素取整（类似 JS `Math.round`），使 `sizeUnit` 产生精确请求的像素尺寸。
- 📝 **Windows path 类型**：在 TypeScript 类型和 README 中声明 Windows 专用的 `path` 捕获选项；Windows 模块此前已支持该选项。

### [发布 · LegendApp/legend-list · GitHub](https://github.com/LegendApp/legend-list/releases)

LegendApp/legend-list 从 v3.3.11 到 v3.9.0 的发布集中在滚动定位与末尾跟随的可靠性：新增可选的首次提交前按估算视口渲染、基于 key 的取消/锚定/跳转与更精确的 scroll ref Promise 语义，并持续修复键盘、粘性头部、Web/Fabric 布局以及聊天列表在数据变更时的跳动。

- 🚀 **首帧渲染**：v3.9.0 新增 opt-in 的 `showImmediately`，在布局前按估算视口于首次提交时渲染行；尺寸估算错误或存在初始滚动目标时，首帧位置可能偏移。
- 🧩 **Web 修复**：v3.9.0 修复 Web 上列表在大幅内容收缩后仍保持末尾跟随，并修复 Strict Mode 下布局前重新渲染时 `numColumns` 变更不生效的问题。
- 🔄 **末尾自动回顶**：v3.8.0 新增 `maintainVisibleContentPosition.autoscrollToTopThreshold`，前置插入后若原偏移在阈值内则动画回到列表开头；同时修复 `KeyboardAwareLegendList` 折叠/删除行和 capped chat 裁剪旧行时的锚定与末尾跟随。
- 🔑 **滚动 Promise**：v3.7.0 让 `scrollToIndex`、`scrollToOffset`、`scrollToItem`、`scrollToKey`、`scrollToEnd`、`scrollIndexIntoView`、`scrollItemIntoView` 在滚动落位、被用户输入中断、取消/替换或无法到达目标时才 resolve；隐藏状态下的请求直接 resolve 且不重放。
- 🛠️ **类型与 key API**：v3.7.0 新增 `cancelScroll`、`scrollToKey`、`anchorVisibleContent`；`LegendListRef` 需实现这些成员，`LegendListState` 需包含 `distanceFromEnd`、`isFollowingEnd`，`dataKey` 为可选；`SectionListRef` 的 key 使用 `${sectionKey}:item:${itemKey}` 等扁平格式。
- 🎯 **可视区域参数**：v3.7.0 为 `scrollIndexIntoView` 增加 `viewportMargin: { start, end }`，并为 `scrollIndexIntoView`/`scrollItemIntoView` 增加 `itemOffset` 和 `itemLength`，用于在垂直和水平列表中露出条目内部区域。
- 🧪 **用户滚动**：v3.7.0 的 `onUserScroll` 仍为 `@experimental`，每次被接受的真实用户手势触发一次，库或 ref 发起的滚动不触发；wheel 分组为启发式，原生 pointer/wheel-only 与 Web overlay scrollbar 检测仍有缺口。
- ⚙️ **布局修复**：v3.7.0 修复末尾阈值将尾部内容和键盘 inset 重复计算、行/头尾尺寸变化后无需滚动即可触发 `onStartReached`/`onEndReached`、`scrollMessageToEnd({ closeKeyboard: true })` 一次动画到位，以及 `maintainScrollAtEnd.on.dataAppend` 仅跟随保留既有 key 顺序的追加。
- 📈 **补丁稳定性**：v3.7.1 至 v3.7.3 修复滚动位置在行、inset、视口变化时保持，iOS `contentInset.top` 起始测量，键盘收起/中断滚动跳动，Web 行顺序与焦点，prepend 锚点，`scrollToOffset`/`scrollToIndex` 落点，Fabric NaN 测量，CSS transform 祖先尺寸，`minimumViewTime` 与 Home 置顶等问题，并优化方向缓冲和尺寸估算复用。
- 🧩 **超尺寸项**：v3.6.0 新增 `viewPositionFallback`，在初始或程序化滚动时将超出视口的条目对齐到视口开头或结尾，适合视口的条目仍按 `viewPosition` 对齐。
- 🌐 **Web 共享滚动**：v3.5.0 新增 `scrollElement`，Web 列表可共享祖先元素的滚动条；停止滚动后保留最后滚动方向的行准备状态，单列列表在尺寸和数据不变时减少初始渲染与滚动布局工作。
- ✅ **就绪回调**：v3.4.0 新增 `onReady`，在每次初始放置和滚动周期完成后调用，包括 `dataKey` 变更导致的重启；数值 `initialScrollIndex` 指向最后一行时，末尾打开会包含 footer。
- 🐛 **末尾与数据切换**：v3.3.11 修复 `scrollToEnd`/`maintainScrollAtEnd` 在内容变化时继续到达末尾，切换数据集会取消旧滚动请求，`anchoredEndSpace` 随行测量收缩多余空白，Web 调整不再留额外尾部 padding，并改善 Web 行重排时的焦点、动画和内嵌内容状态保持。

### [发布 v0.4.0 · blazejkustra/react-native-effects · GitHub](https://github.com/blazejkustra/react-native-effects/releases/tag/v0.4.0)

react-native-effects 发布 v0.4.0，集中加入材质、粒子与社交应用动效示例，并扩展 ShaderView 的 texture 属性和 onFirstFrame 回调；同时升级到 react-native 0.88 与 Expo 58，推进 Effects 应用目录、示例 App Store 上架准备和 README 演示更新。

- 🚀 **v0.4.0 发布**：blazejkustra 于 11 月 22 日发布 v0.4.0，包含多项新效果、示例应用与文档更新。
- 🧩 **ShaderView 增强**：`ShaderView` 新增 `texture` 属性，可配合实拍啤酒泡沫等素材；并新增 `onFirstFrame` 回调，由 @kagantemizkan 首次贡献。
- 🎨 **材质与粒子示例**：新增 materials 屏幕、生日蜡烛、粒子扩散、雪球与魔法 8 球、香烟、蒲公英、沙漏番茄钟等示例，后续移除雪球。
- 💬 **社交应用动效复刻**：加入 Telegram 溶解与剧透、Instagram 语音消息删除、iMessage 发送效果等示例，并重写 Telegram 剧透聊天的文案。
- 🎯 **新增 11 个 X 效果**：为 X 增加 11 个新效果，扩充示例效果库。
- 📦 **依赖升级**：将示例升级到 `react-native` 0.88 与 `Expo` 58。
- 📱 **App Store 准备**：发布 Effects 应用目录与 App Store 配置，准备示例应用上架，并围绕新演示录像重写 README。

### [发布 v3.9.0 · jpudysz/react-native-unistyles · GitHub](https://github.com/jpudysz/react-native-unistyles/releases/tag/v3.9.0)

React Native Unistyles 发布 v3.9.0 小版本，无破坏性变更，重点是将 Babel 插件标记为弃用并计划在 4.0 移除，同时为 Re.Pack、Rspack、Rsbuild 引入实验性 UnistylesPlugin，并修复主题冻结与并发渲染、Reanimated 透明度、React Compiler 缓存样式、Android insets、Web CSS 规则及 React Native nightlies 兼容等问题。

- 🚀 **正式发布**：v3.9.0 是无破坏性变更的小版本；Babel 插件 `react-native-unistyles/plugin` 在 3.x 中行为不变，但已弃用并将在 Unistyles 4.0 移除，升级到 3.9.0 无需改代码。
- ⚠️ **弃用计划**：`RepackUnistylePlugin` 和 `BASE_REPACK_EXCLUDE_PATHS` 也已弃用，前者仍可用但会打印警告；建议改用新的 `UnistylesPlugin`，或在 `babel.config.js` 中加入 `react-native-unistyles/plugin`。
- 📦 **构建集成**：Metro 可用 `withUnistylesConfig` 替代 Babel 插件；Re.Pack、Rspack、Rsbuild 新增实验性 `UnistylesPlugin`，在 Rspack 内运行 Metro 集成的 resolver，替换相同 imports，并让 StyleSheets 在运行时记录依赖，无需 Babel 插件。
- ⚙️ **集成约束**：`UnistylesPlugin` 不接受 `root`、`autoProcessImports`、`autoProcessPaths` 等选项，要求 `@rspack/core` 1.7.5 或更新；已在 Re.Pack 的 Rspack 配置中测试，未测试其 webpack 配置，切换后需用 `--reset-cache` 重启。Module Federation 中替换发生在决定共享模块之前，各 container 应共享 `react-native`、`react-native-unistyles` 及其子路径；`node_modules` 内库也会被替换，出现第二份 Unistyles 会警告且样式不更新。
- 🔄 **变体 API**：`styles.useVariants()` 不再修改 `styles`，应使用它返回的 styles；可用 codemod 转换组件：`npx jscodeshift --parser=tsx --extensions=tsx,ts,jsx,js -t node_modules/react-native-unistyles/codemods/use-variants.js src`，Jest 无需改动。
- 🎨 **主题修复**：冻结子树恢复后会显示新主题，即使未重新渲染；`<ScopedTheme>` 在 `startTransition` 或 Suspense 并发渲染让出时不再把主题泄漏到作用域外，改为按视图作用域读取主题。
- ⚡ **Reanimated 修复**：主题切换并发生无关 React commit 后，用 Reanimated 淡出的视图不再停在动画中间透明度，例如 `0.5`；Unistyles commit 后 React 节点保留自身 props 加上 Unistyles 值。
- 🧠 **缓存样式修复**：由 React Compiler 或 `useMemo` 保留的元素在主题切换后首次挂载的视图会显示新主题；每个 style 记录创建时的 revision，旧 revision 挂载时提交当前值。主题设为 `undefined` 的 props 切换后重置为 `null`，但新样式完全省略的 props 尚未重置。
- 📱 **Android insets**：Android 11 以下通过 `WindowInsetsControllerCompat` 隐藏状态栏时，`rt.insets.top` 现在为 `0`，覆盖 React Native 的 `StatusBar` edge-to-edge、`SystemBars` 和 react-native-keyboard-controller 等场景；Android 15 桌面窗口化下，顶部 inset 会包含系统标题栏，并取状态栏与标题栏的较大值。
- 🌐 **Web CSS**：当尚未挂载到 document 的元素仍在使用 CSS 规则时，不再删除这些规则，例如 portal 容器稍后才被地图应用追加到 pane；此前规则只会在后续样式渲染时恢复。
- 🛠️ **Nightlies 兼容**：Unistyles 重新支持针对 React Native nightlies 的 iOS 和 Android 构建；React Native 将 `ShadowNodeFamily::nativeProps_DEPRECATED` 改为 struct，Unistyles 在编译期检测类型，从而同时兼容正式版本和 nightlies。
- 🧪 **内部测试**：新增 e2e 场景覆盖 `status-bar`、`safe-area`、`undefined-reset`、主题切换后的 Reanimated 淡出和跨主题保留元素；e2e host 也运行于 Android API 29 模拟器，并支持 `--window desktop` 桌面窗口和 `--skip` 跳过场景。

### [版本发布 · JoaoPauloCMarra/react-native-nitro-markdown · GitHub](https://github.com/JoaoPauloCMarra/react-native-nitro-markdown/releases)

react-native-nitro-markdown 连续发布 v0.13.0 至 v0.17.0，核心方向是改进流式 Markdown 解析与渲染性能，同时处理错误上报、无障碍、内存上限和依赖兼容性；v0.17.0 新增 streaming 选项以隐藏未完成块和半输入内联语法，并让长文档刷新更快。

- 🚀 **v0.17 流式显示**：`MarkdownStream` 和 `useMarkdownStreamState` 新增 `streaming` prop，可暂不显示最后一个未完成块；开启后，最后一层未闭合的 `**`、反引号、`~~`、链接和公式按完成后的样式显示，该版本无破坏性变更。
- 🧩 **流式渲染选项**：新增 `streamingOptions`，可选择表格、代码块和媒体行是否在到达时立即显示；新增 `openCodeFence` 流状态和 `MarkdownSession.parseStreamView` 原生调用。
- ⚡ **长文档刷新**：顶层块按 32 个一组渲染以缩短长文档 flush 时间；已完成的 `**bold**` 后纯文本不再触发原生解析，原生 JSON writer 更快且输出不变。
- 🐛 **AST 拷贝移除**：v0.16.3 中 `MarkdownStream` 每次 flush 不再验证和深拷贝自身 AST，示例流在 iPhone 17 模拟器上的 Markdown 渲染时间从 534 ms 降至 42 ms；代码高亮器复用正则。
- 🔄 **增量流式恢复**：v0.16.4 恢复顶层代码块和数学块的增量流式解析：此前流中出现一个缩进围栏（如列表项中的代码）会让后续多行块每次全量解析，修复后渲染输出不变。
- 🛡️ **错误与无障碍**：v0.16.0 让抛错的 `astTransform` 或 `highlightCode` 调用 `onError`，`MarkdownErrorPhase` 新增 `transform`；修复内联数学、HTML 和图片标题的纯文本提取，以及表格和图片的无障碍读取。
- ⚠️ **v0.15 破坏性变更**：`session.getTextRange(from, to)` 对非法范围抛出 `MarkdownError` 的 `invalid_range`，不再返回空串；AST 拒绝 `metadata` 节点属性并报 `invalid_ast`；表格单元格改用 12pt 粗体表头和 14pt 正文样式。
- ⚠️ **图片白名单语义**：v0.14.0 将 `imageOptions.allowedHosts: []` 改为拒绝所有图片主机，而不是禁用白名单；要保留默认策略需省略 `allowedHosts`，或显式提供允许的主机名，协议限制仍然生效。
- 📦 **RaTeX 子路径**：v0.13.0 将 RaTeX 数学渲染移到 `react-native-nitro-markdown/math` 子路径，`ratex-react-native` 变为可选 peer 依赖；主入口不再加载它，未使用子路径时 `math_inline` 和 `math_block` 以等宽文本显示。
- 🧠 **内存与 BOM**：v0.13.1 跳过首个 UTF-8 BOM；`sourceOffsets: true` 的偏移映射约占输入 6%，10 MB 非 ASCII 文档解析峰值约 11 MB，而此前为 52–94 MB；OOM 时返回带原因的 `parse_failed`。
- 🎨 **默认主题调色板**：v0.13.0 将默认代码 token 调色板改为浅色，旧深色调色板移至 `darkMarkdownTheme`；自定义深色主题若只设 `codeBackground`，需补 `codeTokenColors: darkMarkdownTheme.colors.codeTokenColors` 以保持可读性。
- 🧩 **AST 预算错误**：v0.13.0 新增 `input_too_complex`：超过原生 AST 预算（100,000 节点、500,000 单位 AST 工作、64 MiB AST JSON 或扁平文本）的文档返回该错误；session buffer 上限改为 10,485,760 UTF-8 字节，v0.13.1 将 64 MiB AST JSON 限制改为写入时执行。
- 🧪 **兼容基线**：v0.13.0 将 React Native peer 下限设为 `>=0.77`，支持 RN 0.77 / Expo SDK 53 及以上；v0.16.2 起开发和示例基线更新到 Expo SDK 58、React Native 0.88.1 和 `react-native-nitro-modules` 0.37.2。

### [发布 · callstack/agent-device · GitHub](https://github.com/callstack/agent-device/releases)

总结失败：模型未返回符合格式的摘要。

### [software-mansion/argent 发布 v0.34.0 · GitHub](https://github.com/software-mansion/argent/releases/tag/v0.34.0)

software-mansion 发布 `argent` v0.34.0，自 v0.33.0 起合入 114 个提交，重点扩展 E2E 脚本类型、合并 MCP 原生工具并优化元素树传输，同时为 macOS 应用加入原生与 React 性能分析；此外集中修复 Android/iOS 设备控制、安装器、归档压缩和 Node 22.18+ 运行要求等问题。

- 🚀 **发布 v0.34.0**：发布 `argent` v0.34.0，包含自 v0.33.0 以来的 114 个提交；该 release 未附 `swmansion-argent-0.34.0.tgz`，可用 `npm pack @swmansion/argent@0.34.0` 或从 npm registry 获取同内容 tarball。
- ⚙️ **Node 要求**：项目要求 Node 22.18+，CI 单元测试仅在 Node 22 上运行，安装器和测试流程需使用该版本。
- 🧪 **E2E 脚本**：E2E 的 script steps 可运行 `.js`、`.ts` 和 `.mts` 文件；`e2e list` 新增 `--json` 输出，便于脚本化处理。
- 🧩 **MCP 工具**：MCP 将两个 native view-at-point 工具合并；当元素树未变化时发送一条说明代替重复元素树，减少传输与处理开销。
- 🎨 **macOS 分析**：新增面向 Mac 应用的原生 profiler，以及面向 react-native-macos 应用的 React profiler；修复默认原生 profile 下展示 Web 内容时冻结应用的问题。
- ⚡ **设备列表性能**：`list-devices` 不再因单个冻结的 Android 模拟器拖慢每次调用，避免一个异常设备阻塞整体设备枚举。
- 🛠️ **Android 稳定性**：超时的 Android helper 会被停止，使 `describe` 的回退路径可读取；重连和 dispose 时也会停止静默 helper；启动器 activity 使用 `MAIN` action 和 launcher category 启动。
- 🔧 **Android profiler**：Android profiler 用自研 RPC 客户端替换 Lynx Perfetto 解码器，改变性能数据采集链路。
- 📱 **iOS 修复**：iOS 设备 runner 不再把屏幕录制文件留在手机上；`describe` 在 iOS 26 上显示 Web 登录表单；Xcode 使用自定义构建位置时仍能找到 runner 构建产物。
- 🔄 **设备选择**：当已知 `logicalDeviceId` 离开 Metro 时，不再回退到另一台设备，避免误连错误目标。
- 📦 **归档压缩**：归档传输将 bundles 改为 zstd，并通过协商选择，保留 gzip 作为回退。
- 🏢 **安装器修复**：安装器在解析后的项目根目录安装 project-scope skills；skills CLI 克隆固定源时跳过私有子模块；本地 pnpm install 可在 workspace 根目录运行；暴露 pnpm 全局安装错误；在 `fs.rmSync` 会保留链接的 Node 版本上移除链接。
- 🐛 **技能测试**：`test-ui-flow` 的点击改从元素树获取，并移除 project-memory push。

### [2027年React Native对比Swift：两者都上线后我会选哪个 - YouTube](https://www.youtube.com/watch?v=0rEfoLc9MQY)

提供的正文没有技术文章内容，只有 YouTube 页脚导航与版权声明，包含 About、Press、Copyright、Contact us、Creators、Advertise、Developers、Terms、Privacy、Policy & Safety、How YouTube works、Test new features、NFL Sunday Ticket 等链接，以及 © 2026 Google LLC；因此无法整理出产品发布、核心机制或版本变更等技术周刊信息。

- 📝 **页脚导航**：正文仅为 YouTube 页脚链接列表，涵盖 About、Press、Copyright、Contact us、Creators、Advertise、Developers、Terms、Privacy、Policy & Safety、How YouTube works、Test new features 和 NFL Sunday Ticket。
- 🗓️ **版权信息**：页面底部标注 © 2026 Google LLC，未包含产品版本、功能机制、发布计划或技术细节。

### [请提供需要翻译的文章标题或文件内容。](https://raw.githubusercontent.com/tc39/agendas/main/2026/11.md)

Ecma TC39 第117次会议将于2026年11月30日至12月3日远程举行，每天10:00至15:00 EASST，预计会议容量16小时；议程涵盖ECMA262、ECMA402、ECMA404、Test262及任务组报告，并集中审议多项规范修复与从Stage 0到Stage 4的提案晋升，重点包括Import Text推进至Stage 4、Import defer与Thenable Curtailment等Stage 3事项，以及AbortController、Math.fusedMultiplyAdd、Immutable ArrayBuffers等提案。

- 🗓️ **会议安排**：第117次TC39会议远程举行，2026-11-30至2026-12-03每天10:00至15:00 EASST，预计会议容量16小时；日程约束需至少会前3天提交，原文提供Temporal时区转换代码示例。
- ⚠️ **晋升截止**：提案晋升资格截止为2026-11-20 10:00 Pacific/Easter，恰为会前10天；Stage 0和Stage 1提案需截止前登记，Stage 2、2.7、3、4及规范变更须附支持材料，Stage 4须链接ecma262 PR，否则可能被反对或保留共识。
- 📊 **报告安排**：会议包含秘书报告15m，ECMA262、ECMA402、Test262各5m，ECMA404 1m；TG3安全1m、TG4 Source Maps 5m、TG5 5m，以及CoC委员会1m更新。
- 🐛 **规范修复**：ECMA262的needs-consensus与Web兼容议题包括放宽HostGetSupportedImportAttributes返回列表身份要求、移除yield* return路径对值的双重await、接受WSpace作为White_Space别名、BuiltInRegExpExec的web reality与规范缺陷、Atomics.notify中的RevalidateAtomicAccess，以及Un-Annex-B String.prototype.substr。
- ⚡ **性能路径**：讨论length为1时跳过Array.prototype.sort的索引[[Has]]、[[Get]]、[[Set]]访问，以及async generators中yield nonthenable的快速路径，后者安排45m。
- 🚀 **Stage 3与4**：Import defer讨论循环与top-level await相关bug及PR #97；Import Text申请Stage 4并链接spec PR；Thenable Curtailment基于实现反馈提出规范PR #22和#26。
- 🧩 **Stage 2.7与3**：Export defer解析破坏性变更、JSON.parse Options将preferNullPrototype重命名、ESM Phase Imports从transfer-gated改为import()-gated安全模型，以及Immutable ArrayBuffers申请Stage 3。
- 🧪 **Stage 2**：Error code property申请Stage 2.7；Intl Sequence Units和eraDisplay/yearStyle进行Stage 2更新；Math.fusedMultiplyAdd申请Stage 2.7；Composite用60m讨论排序问题。
- 🎯 **Stage 0至2**：AbortController/Cancellation申请Stage 2；Iterator transfer为Stage 0；Trim Specific Characters申请Stage 1或2；Intl Supported Time Zone Options申请Stage 1；Bitwise counting申请Stage 1或2。
- 💡 **长讨论**：安排45m讨论Making spec.html executable，由James M Snell和Dan Carney参与。
- 🔄 **日程约束**：Nicolò Ribaudo周四不可用；Jordan Harband在11:30前和周四大部分时间不可用，希望参加Thenable Curtailment、Error code property、Math.fma和Iterator transfer；Eemeli Aro每天13:00后不能演讲且周四全天不可用；James Snell在12月3日不可用。

### [src：当堆即将超出指针压缩限制时发出警告 by jasnell · Pull Request #67468 · nodejs/node · GitHub](https://github.com/nodejs/node/pull/67468)

Node.js 主分支合并 PR #67468，在未启用指针压缩的构建中新增 `HEAP_EXCEEDS_POINTER_COMPRESSION_LIMIT` 进程警告，以 6.5 GiB 和 8 GiB 两档阈值提示全量 GC 后存活堆可能或将会超过启用指针压缩时每个 isolate 的 4 GiB cage 限制。该改动旨在为未来默认启用指针压缩铺路，同时被标记为不进入 v22/v24/v26 LTS。

- 🚀 **合并落地**：James M Snell 的 PR #67468 已合并到 Node.js main，落地提交为 428dd86，新增针对未启用指针压缩构建的堆上限预警。
- ⚠️ **双阈值预警**：全量 GC 后存活堆从 6.5 GiB 起警告可能超过限制，从 8 GiB 起警告将会超过限制；依据是指针压缩最多将堆缩小一半，实践中约缩小 40%。
- ⚙️ **触发与关闭**：检查只在 mark-compact GC 的 epilogue 回调中运行，每个 Environment 至多执行一次，安排警告后即注销；可用 `--disable-warning=HEAP_EXCEEDS_POINTER_COMPRESSION_LIMIT` 静默。
- 🧩 **限制背景**：当前指针压缩需在构建时开启且默认关闭，目标是未来默认启用；启用后每个 isolate 的堆受 4 GiB cage 限制。V8 多 cage 模式下主线程和每个 worker 各有 Isolate Group 和 4 GiB 堆上限，不再是进程级统一 4 GiB，大堆应用可能内存不足或崩溃。
- 🛡️ **LTS 排除**：该 PR 被加上 dont-land-on-v22.x、v24.x、v26.x 标签，避免进入 LTS；原因是未启用指针压缩的构建原本无警告，新增警告属于可观察的行为变化。

### [2026 年 HTML 现状](https://2026.stateofhtml.com/en-US)

State of HTML 调查于2026年10月1日至11月1日收集2,091份回复，主题转向重新审视现代浏览器的原生能力。文章指出，Web API 曾长期落后，JavaScript 框架因此填补空白并快速扩张；如今框架格局收敛、浏览器厂商协作加速新特性跨浏览器落地，而 AI 辅助代码生成在合适场景可直接调用浏览器 API、绕过框架，开发者因此更需要回到基础。

- 🗓️ **调查窗口**：该调查于2026年10月1日开始、11月1日结束，共收到2,091份回复。
- 🔄 **趋势反转**：Web API 曾长期弱于原生等价能力，复杂布局依赖 hack；JavaScript 因此填补空白并催生大量框架和库。
- ⚙️ **框架收敛**：JavaScript 框架已向少数稳定选项集中，变化速度放缓，生态从爆炸式扩张转向整合。
- 🌐 **浏览器协作**：浏览器厂商加强协作，以更快速度发布新特性，并确保跨浏览器可用，弥补平台能力短板。
- 🧠 **AI 生成代码**：AI 辅助代码生成不排斥跳过 JavaScript 框架，在合适场景直接利用浏览器 API，提升原生 Web 能力的重要性。
- 🎯 **回到基础**：调查旨在帮助开发者重新熟悉现代浏览器实际能力，查漏补缺并评估原生 API 的适用边界。

### [Chrome 预渲染很怪 · Tom Bennet](https://tombennet.dev/blog/chrome-prerendering-is-weird)

Chrome 地址栏可能在用户按 Enter 前对高置信度建议页做完整预渲染，执行 JavaScript 并把写入 `localStorage` 的数据持久化；Synthesia 的 onboarding 因此偶发读到错误查询参数快照，最终通过 `document.prerendering` 与 `prerenderingchange` 修复，说明页面加载不等于用户访问。

- 🧩 **后台预渲染**：Chrome 会在地址栏输入时后台加载排名靠前的建议页，不只是 DNS 或 HTML 请求，而是完整预渲染：JavaScript 会运行，写入 `localStorage` 的内容即使页面从未被访问也会保留；这是文档化行为，用于让导航显得即时。
- 🏢 **触发场景**：Synthesia 的注册流程依赖首个 URL 上的查询参数来决定 onboarding 路径；应用首次加载时把查询字符串快照写入 `localStorage`，之后只在没有快照时保留，完成 onboarding 后清除，后端据此选择流程。
- 🐛 **参数污染**：用户输入 `synt…` 时，Chrome 可能预渲染此前访问过的应用页面，该页面先把错误参数写入 `localStorage`；用户随后打开带正确参数的真实 URL，但快照已存在且不会被覆盖，导致该 Incognito 会话后续页面都使用错误快照。Incognito 的 `localStorage` 在同一会话所有标签页间共享，包括不可见的预渲染页，且建议仍基于正常浏览历史。
- 🔍 **复现困难**：打开 DevTools 的标签页不会触发 omnibox 预渲染，这是 2019 年加入的检查，Speculative loads 面板也不显示；全新浏览器 profile 没有历史可建议，粘贴正确 URL 也会绕过问题；Chrome 只在根据历史判断用户很可能选择建议时才预渲染，`chrome://predictors` 可查看相关分数。
- 🛠️ **修复方式**：应用在保存快照前检查 `document.prerendering`；若页面正在预渲染，就等待 `prerenderingchange` 事件且只监听一次，用户真正导航到页面后再执行保存，否则立即执行；如果用户从未访问该页面，回调不会运行，也就不会保存任何内容。
- 🧭 **通用判断**：加载页面不等于有人访问页面；如果代码在页面加载时执行只应发生一次的操作，例如保存状态、记录事件或统计浏览量，应先检查 `document.prerendering`；Google Analytics 等分析工具已经这样做。
- 🌐 **其他入口**：站点可通过 `Speculation Rules API` 请求预渲染链接；服务端收到的预渲染请求会带有 `Sec-Purpose: prefetch;prerender` 请求头，也可以在服务端处理这类请求。

### [Firefox 161 面向开发者的发行说明（稳定版）- Mozilla | MDN](https://developer.mozilla.org/en-US/docs/Mozilla/Firefox/Releases/161)

Firefox 161 稳定版于 2026 年 11 月 24 日发布，面向开发者的变化覆盖 SVG、CSS、HTTP 压缩字典传输、Web API、WebRTC 和 WebDriver BiDi；HTML 与 JavaScript 无显著变化，另有多项默认关闭、可在 Nightly 或通过 about:config 试验的实验特性。

- 🚀 **正式发布**：Firefox 161 稳定版发布，影响使用新版浏览器进行 Web 开发和自动化测试的开发者。
- 🧩 **SVG referrerpolicy**：`<image>`、`<script>`、`<feImage>` 元素支持 `referrerpolicy` 属性，以及对应的 `SVGImageElement.referrerPolicy`、`SVGScriptElement.referrerPolicy`、`SVGFEImageElement.referrerPolicy` 属性，用于控制 `href` 资源请求的 Referer 信息，行为类似 HTML `img` 和 `script`。
- 🎨 **CSS random()**：新增 `random()` CSS 函数，可在指定范围内生成随机值，并可按指定步长限制取值；可选 `<random-key>` 参数用于在不同元素或属性间共享同一随机基值。
- 🧩 **CSS 函数嵌套**：`var()`、`attr()`、`env()` 的首个参数现在可接受嵌套函数，例如 `var(attr(data-theme-prop type(<custom-ident>)))` 和 `env(var(--safe-area-block-start))`。
- ⚡ **压缩字典传输**：支持 Compression Dictionary Transport：服务器可用 `Use-As-Dictionary` 标记响应为字典，浏览器在匹配请求中用 `Available-Dictionary` 列出已存字典，服务器可用 `dcb`（Brotli）或 `dcz`（Zstandard）作为 `Content-Encoding` 返回压缩响应，从而显著减小版本间变化较小的资源体积，如 JavaScript bundle。
- 🌐 **WebTransport 流预期**：`WebTransport` 接口新增 `anticipatedConcurrentIncomingUnidirectionalStreams` 和 `anticipatedConcurrentIncomingBidirectionalStreams` 属性，并可在 `WebTransport()` 构造函数的 `options` 中设置，表示应用预期服务器同时打开的单向和双向入站流最大数量。
- 🛡️ **剪贴板自定义格式**：Clipboard API 支持自定义剪贴板格式，Web 应用可通过 `Clipboard.write()` 和 `Clipboard.read()` 读写自有数据格式；自定义格式是以 `web ` 为前缀的 MIME 类型，例如 `web text/x-my-format`，且只能被与写入页面同源的页面读取。
- 🧭 **NavigationTransition.to**：Navigation API 新增 `NavigationTransition.to` 属性，返回进行中导航的 `NavigationDestination`，使 `navigate` 事件处理器之外的代码也能获知导航目标，例如在 `navigateerror` 处理器中报告哪个导航失败。
- 🧩 **CSS Typed OM**：支持 CSS Typed Object Model API，脚本可通过 `Element.computedStyleMap()`、`HTMLElement.attributeStyleMap` 等以带类型的 JavaScript 对象读写 CSS 值；`CSSColorValue`、`CSSRGB` 等颜色值接口在 Firefox 及其他浏览器中尚不支持。
- 💻 **WebRTC 关键帧请求**：`RTCRtpSender.setParameters()` 支持可选参数 `setParameterOptions`，可在修改发送端编码参数（如 `active`、`scaleResolutionDownBy`）的同一次调用中要求编码器生成关键帧，接收端随后无需再请求关键帧。
- 🐛 **WebDriver BiDi 脚本修正**：`script.callFunction` 遇到参数或 `this` 值包含未知 `type` 的本地值（包括嵌套值）时改为返回 invalid argument 错误，不再静默替换为 `undefined`；`script.evaluate` 和 `script.callFunction` 在 `userActivation: false` 时不再清除已有的用户激活标志。
- ✅ **WebDriver BiDi 稳定性修复**：修复 `browsingContext.navigate` 与 `browsingContext.reload` 在上一个文档仍加载时启动导航可能挂起或返回错误错误的问题；修复 `browsingContext.setViewport` 随会话生命周期变慢的性能问题；`network.continueRequest` 替换已有请求体时会同步更新 `Content-Length`，避免服务器收到截断或不完整请求体。
- 🧪 **margin-trim 实验特性**：`margin-trim` 属性作为实验特性支持块容器，通过 `layout.css.margin-trim.enabled` 控制，Nightly 默认启用；可移除容器起始边、结束边或两边的子元素块轴外边距，同时保留兄弟元素之间的外边距。
- 🧪 **跨文档视图过渡**：跨文档视图过渡通过 `dom.viewTransitions.cross-document.enabled` 控制，Nightly 默认启用，可用于多页应用中同源页面之间的动画过渡。
- 🧪 **渲染阻塞**：`link`、`script`、`style` 元素的 `blocking="render"` 属性通过 `dom.element.blocking.enabled` 控制，Nightly 默认启用；可阻止页面渲染直到标记的样式表加载完成或脚本执行，避免页面先以无样式或不完整状态出现。
- 🧪 **quotes match-parent**：`quotes` CSS 属性通过 `layout.css.quotes.match-parent.enabled` 试验支持 `match-parent` 值，使元素使用与其父元素相同组引号对中的引号，Nightly 默认启用。
- 🧪 **text-autospace-size**：新增 `text-autospace-size` 属性，通过 `layout.css.text-autospace-size.enabled` 控制，Nightly 默认启用；用于设置 `text-autospace` 在中文、日文、韩文（CJK）与非 CJK 字符之间添加的间距大小。
- 🧪 **color-scheme 元标签**：`prefers-color-scheme` 媒体特性通过 `layout.css.prefers-color-scheme.meta-tag.enabled` 试验反映 `<meta name="color-scheme">` 声明的单一配色方案，Nightly 默认启用；有助于按配色方案选择图片和视频，并简化主题切换器实现。

### [Parcel 3 alpha 3：静态站点](https://v3.parceljs.org/blog/v3-alpha3/)

Parcel 3 alpha 3 将静态站点生成能力内置到打包器，新增 Markdown 编译、布局与 include、构建期 HTML 宏、RSS/Atom feed 生成和输出命名规则，并带来构建性能与内存优化及原生插件增强；官网已迁移为仅用 Parcel 和 .parcelrc 构建。

- 🚀 **版本发布**：发布 `parcel@next` 对应的 Parcel 3 alpha 3，也可用 `@parcel/parcel3` 与 Parcel 2 并行试用；该版本把静态站点所需能力内置，官网已从 Eleventy 和自定义插件迁移为仅用 Parcel 与 `.parcelrc` 构建。
- 📝 **Markdown 支持**：可直接把 Markdown 编译为 HTML 页面，Markdown 可作为构建入口或被其他页面链接，Markdown 间链接指向编译后页面，图片等引用照常处理；`.parcelrc` 可配置 GFM、目录、标题锚点、从内容生成 `<title>` 和 `<meta name="description">`，并可按 glob 为站点不同部分设置不同选项。
- 🧩 **布局与包含**：布局是带 `<parcel:slot>` 占位符的 HTML 文件，HTML 页面用 `<parcel:layout>` 套用，命名槽由 `parcel:slot` 属性填充，布局可嵌套，`<title>`/`<meta>` 移入布局 `<head>` 且 `<html>`/`<body>` 属性合并；`<parcel:include>` 插入共享文件并可由子元素填充槽，被包含文件独立编译且内部 URL 相对自身解析。
- 🔧 **HTML 宏**：`<parcel:macro>` 可在 HTML 中调用构建期 JavaScript 函数，函数接收元素内容和属性并返回 HTML；返回内容继续参与处理，如示例 `posts.js#postList` 生成帖子列表且链接被重写到 Markdown 编译结果。还可用 `<parcel:define>` 定义自定义元素，或通过 HTML transformer 的 `macros` 为所有页面（含编译后的 Markdown）配置宏，甚至覆盖内置元素，如构建期高亮 `<pre>`。
- 🔗 **Feed 生成**：宏同样可用于 XML，从而生成 RSS/Atom feed；每个条目可用 `<parcel:include>` 嵌入文章全文，博客 feed 与导航复用同一帖子列表生成。
- 🎯 **命名规则**：默认 namer 新增命名规则，用 glob 将源路径映射到输出路径，支持 `$1`/`$2` 等捕获、`[hash]` 和 `[ext]`；例如 `src/**/*.md` 可输出到 `$1/$2/index.html`，`shared` 选项配置共享 bundle 名称。HTML transformer 的 `directoryIndex` 使链接指向目录，如 `getting-started.md` 写成 `/docs/getting-started/`。
- ⚡ **性能优化**：开发环境 JavaScript 以生成代码而非 AST 存储，减少内存并避免重建时重复打印未变代码，PNG 优化并行化；冷构建中 three.js x10 dev 141ms→104ms（−26%）、prod 179ms→153ms（−15%），Storybook dev 408ms→325ms（−20%）、prod 4.87s→1.12s（4.4×）；开发峰值内存 three.js x10 564MB→132MB（−77%），Storybook dev 1.07GB→602MB（−44%），Storybook prod 峰值内存则从 1.21GB 增至 1.25GB（+4%）。
- 🛠️ **原生插件**：原生插件初始化时获得 `.parcelrc` 文件路径和 Parcel 选项，可解析插件配置中的相对路径并读取 Parcel 文件系统跟踪的文件；诊断支持多个 code frame、高亮和提示，code frame 可展示磁盘上不存在的生成代码如修复建议。旧 alpha 插件无需重建，使用新 SDK 重建的插件需 Parcel 3.0.0-alpha.3+ 并在 `package.json#engines.parcel` 声明。

### [Nudeps：类似打包器的导入，没有任何包袱 • Lea Verou](https://lea.verou.me/blog/2026/nudeps/)

Nudeps 是一款新的轻量构建工具，目标是让开发者继续用 npm 安装和管理依赖，把依赖本地 vendor 后通过包名即 bare specifiers 在浏览器中直接导入，从而避免为使用依赖而引入完整 bundler。它只处理依赖、不触碰用户代码，试图填补简单项目无需复杂构建的空白，同时保留 bundler 处理复杂场景的空间。

- 🚀 **正式发布**：Nudeps 发布，定位为轻量构建工具而非无构建方案；开发者可继续用 npm 管理依赖，并在浏览器中通过包名导入，无需 bundler 介入。
- 🧩 **工作原理**：运行 `npx nudeps install` 会将 Nudeps 加入 `devDependencies`，并添加 `dependencies` 和 `prepare` 脚本；每次 npm install 或 uninstall 后自动运行，把 `node_modules/` 中所需文件复制到 `client_modules/`，目录名带版本号如 `vue@3.5.45`，再基于 JSPM 生成 import map 注入脚本。
- 💻 **使用方式**：安装后在 HTML 中于其他导入依赖的脚本之前加入 `<script src="/importmap.js"></script>`，即可直接写 `import { createApp } from "vue"`；之后正常增删 npm 包即可，生产环境可用 `prune` 只保留实际使用的 specifier。
- ⚡ **轻量设计**：Nudeps 不监听源码、不重写用户代码，只处理依赖文件，因此不增加源码与部署之间的抽象层，可与纯 HTML/CSS/JS 项目、现有编译工具、静态站点生成器和岛屿架构组合使用。
- 🧪 **兼容范围**：支持 Vue、React（无 JSX 时体验较差）、D3、gsap、Lit、Three.js、Floating UI、interact.js 和 Underscore；也支持动态 `import()`、`import.meta.resolve()`、本地包、npm 别名、git 依赖和实验性 npm workspaces，`lodash` 等 CJS 包可通过小型 `require()` shim 工作。
- 🎨 **非 JS 依赖**：可使用 Open Props 和 Bootstrap Icons 等 CSS 或图标库，但浏览器目前无法通过 specifier 引入 CSS，需使用实际 URL；Nudeps 会创建符号链接或重定向，支持 `client_modules/open-props/` 这类无版本 URL，但这些包不能依赖其他未打包的依赖。
- ⚠️ **限制与取舍**：Nudeps 不转换用户代码，JSX、TypeScript、Svelte 等仍需编译工具；目前仅支持 npm，pnpm 和 yarn 在路线图前列；Workers 不支持 specifier；CJS 支持仍很实验性；依赖 `process.env` 等 Node API 的包需要 stub 或单独打包；尚无基准测试，大量小模块的包首次加载可能较慢。
- 🧠 **代理支持**：早期测试中 Claude 基本能理解 Nudeps，只会做少量无害的多余操作，例如误加 `.gitignore` 条目、手动运行 `npx nudeps` 或添加不必要配置；项目加入 `SKILL.md` 并让代理使用后可消除这些问题。
- 🔮 **后续计划**：路线图包括修复 bug、补齐缺口、测试更多包以验证兼容性和发现边缘情况，以及支持 npm 之外的包管理器；目标是推动构建工具更轻、可组合且非必需。

### [Webpack 5.113 | webpack](https://webpack.js.org/blog/2026-11-19-webpack-5-113/)

Webpack 5.113 于 2026-11-19 发布，核心是在原生 HTML 中支持 CSS Modules，并带来 SVG 资源压缩、loader 按需运行、CommonJS tree shaking 改进、热更新稳定性提升和输出路径控制。此次更新还包含 TypeScript 解析、缓存、多编译器钩子、实验性 parser API 以及多项 Bug 修复，面向使用 HTML 入口、设计工具导出 SVG、CommonJS 包和复杂 HMR 场景的构建用户。

- 🚀 **正式发布**：Webpack 5.113.0 发布，升级命令为 `npm install --save-dev webpack@5.113.0`；本版重点包括 HTML 中的 CSS Modules、SVG 资源压缩、按需运行 loader、改进 CommonJS tree shaking、HMR 稳定性以及输出路径控制。
- 🧩 **HTML CSS Modules**：原生 HTML 页面可在 `<style module>` 中使用 CSS Modules，webpack 会为 `.button` 生成作用域名称并同步到按钮的 `class`；HTML 可作为 entry，链接的 `.module.css` 也可用。多个模块声明同名类时可用 `module=card` 与 `card.button` 指定；作用域 ID 会保持与标签、ARIA 引用和页面链接的连接，但 `document.querySelector('.button')` 等 JS 选择器不会被重写，应改用 `data-action` 等独立属性。
- 🎨 **SVG 压缩**：通过 `optimization.minimizeOptions.xml` 对输出的 `.svg` 和 `.xml` 资源启用优化，`xml: {}` 会缩短数字、颜色和路径数据，删除未使用命名空间声明，并修剪 SVG 容器中不渲染内容的空白；SVG 内样式遵循 CSS 优化设置和浏览器目标。`removeMetadata`、`precision`、`cleanupIds` 需显式开启，默认关闭；非 `experiments.futureDefaults` 场景下需主动启用，可用 `xml: false` 关闭。
- 🛠️ **按需运行 loader**：新增 `sourceTest` 条件，让 loader 先检查输入再决定是否执行转换，例如 `/@instrument/` 只处理包含该注释的 JS 文件，其余文件跳过正常处理；检查能看到当前输入，包括右侧 loader 所做的改动，pitch 函数仍会运行，非 UTF-8 输入也会正常处理。
- 📦 **CommonJS tree shaking**：`exports.answer = 42` 这类简单导出赋值不再让未使用模块看似有副作用；当被引用模块无副作用时，webpack 也可移除未使用的 `require()` 调用，但执行初始化的模块仍会运行。
- 🔄 **热更新改进**：修复模块在 chunk 间移动或更新需要浏览器尚未加载的 chunk 时热更新中止的问题；新 chunk 加载其样式表，移除的 chunk 丢失样式表，已有样式表保留属性和 disabled 状态；watch 模式也能发现递归上下文子目录中新增的文件，无需重启 watcher。
- 🔑 **输出路径控制**：`output.allowOutside` 控制 webpack 在 `output.path` 之外的写入、复制和清理：`false` 将操作限制在输出目录，绝对目录路径数组允许指定外部位置，`true` 允许任意位置；在 `experiments.futureDefaults` 下默认 `false`，否则保留现有行为。
- ⚡ **其他改进**：内置 TypeScript 支持现在一次解析文件，无需单独的类型剥离步骤；`experiments.cacheUnaffected` 可与 `optimization.usedExports` 和 `optimization.mangleExports` 配合；`<style lang='scss'>` 或 `<script lang='ts'>` 可按语言通过 `mimetype` 规则匹配。新增 lazy compilation 的 `transport` 钩子、`MultiCompiler` 的 `done` 异步 tap、`updateManifest` HMR 钩子和 `compilation.hooks.chunkHashDependencies`；实验性 parser API 支持 `path: true` 和 `webpack.javascript.syntax.scopes`，移除 `JavascriptParser.extend` 和实验性 `TypeScriptPlugin`。
- 🐛 **Bug 修复**：修复 WebAssembly 在运行时 chunk 位于子目录或 universal 构建文件名使用完整 hash 时的加载；HTML 对远程资源、编码资源路径和 `<base href>` 页面保持正确 URL，内联资源保留自定义 license banner；改善 CommonJS 与 ES 模块互操作，包括循环再导出和同时被 `import` 与 `require()` 使用的模块；CSS 保持顺序和上下文，导入保留 layer 与 media 条件，服务端异步收集的 CSS 保持请求顺序，导入的 `@value` URL 相对源解析，更长的 `composes` 链可正常工作。

### [Express 现已天生可观测 · Express.js](https://expressjs.com/en/blog/2026-11-17-express-tracing-channels/)

Express 的路由层现在通过 `express.router.request` 这个 `TracingChannel`，为每个中间件、路由处理器和 `router.param()` 回调发布可观测事件，让 APM、日志工具和用户代码无需 monkey patching 或模块钩子即可订阅。该能力随驱动 Express 5 路由的 `router v2.3.0` 提供，依赖 Node 18.19 及以上版本；其意义在于把可观测性变成框架自身契约，降低补丁式集成对加载顺序、打包和 ESM 的脆弱依赖。

- 🚀 **正式发布**：`router v2.3.0` 新增 `express.router.request` 追踪通道，覆盖中间件、路由处理器和 `router.param()` 回调；Express 5 应用已依赖该包，无需升级 Express，只需确保 lockfile 选中新版本，且需要 Node 18.19 或更高版本，旧版本不会发布事件。
- 🧩 **生命周期事件**：该通道基于 `node:diagnostics_channel` 的 `TracingChannel`，提供 `start`、`end`、`asyncStart`、`asyncEnd`、`error` 五个事件，覆盖同步、回调和 Promise API，并用共享上下文和 `AsyncLocalStorage` 自动关联异步操作的开始与结束。
- 📦 **上下文字段**：事件上下文包含 `req`、`res`、匹配的路由模式 `route`、`handler`、仅用于 `router.param()` 的 `param`、处理器通过 `next(err)` 或抛错报告的 `error`、错误处理器收到的 `incomingError`、标识错误处理中间件的 `errorHandler`，以及处理器返回值或 Promise 解析值 `result`。
- 🛠️ **消除补丁**：传统 APM 需要包装 `app.use`、`app.get/post` 等 API 或使用 `require-in-the-middle`、`import-in-the-middle` 和模块钩子，存在签名兼容、需传入 app、必须在 Express 前加载、打包后 Express 被内联而无法触发钩子等问题；新通道把路由内部与观察者解耦，通道及上下文成为稳定契约。
- ⚡ **低开销设计**：无订阅者时向通道发布事件接近零成本，库还可检查是否存在订阅者并跳过上下文对象分配；相比事件发射器，它避免了每次调用构建事件载荷、必须持有发射器实例、监听器抛错表现为库错误以及手工关联请求上下文等问题。
- 📊 **可构建能力**：可用少量代码按路由模式而非原始 URL 聚合延迟，例如把 `/users/1` 和 `/users/2` 归入同一桶；可精确记录哪个中间件或处理器报错；也可为每个处理器创建 OpenTelemetry span，并把同一请求下的 span 关联到请求父级而非层层嵌套。
- 🌐 **生态影响**：`mysql2`、`node-redis`、`ioredis`、`graphql`、`mongoose` 和 Nitro 生态等已开始发布自己的追踪通道；Express 加入后，APM 可消除模块劫持、加载顺序要求和特殊 ESM 处理，库和中间件维护者也被鼓励发布自有通道以让生态工具理解其行为。

### [版本发布 · trpc/trpc · GitHub](https://github.com/trpc/trpc/releases)

tRPC 在 11 月 23—24 日连续发布 v11.29.12 至 v11.31.3 共 10 个版本，重点集中在客户端流式批处理生命周期、wsLink 与 SSE 的连接和错误处理、Fastify 适配器重连通知、WebSocket 适配器结构化类型，以及 tanstack-react-query 在 react-server 环境的可导入性等修复与增强。

- 🚀 **Fastify 重连通知**：v11.31.0 为 `@trpc/server` 的 Fastify 适配器新增 `broadcastReconnectNotification`，用于向客户端广播重连通知，作者 Emmanuelzyronis 和 KATT，#7608。
- 🧩 **WS 适配器类型**：v11.30.0 让 `@trpc/server` 的 WebSocket 适配器以结构化方式标注 server 与 clients 类型，作者 sakaintp 和 KATT，#8058，sakaintp 为首位贡献。
- 🔄 **wsLink 连接恢复**：v11.31.3 修复 `wsLink` 在无 id 事件上保留 `lastEventId`（#8199）；v11.30.4 在 keepAlive pong 超时后立即重连（#7914）；v11.30.2 将无法解码的 `wsLink` 帧视为连接丢失（#7927）。
- 🐛 **流式批处理释放**：v11.31.2 在调用的 deferred 值落定后释放流式批处理（#8195）；v11.31.1 阻止已完成查询继续占用流式批处理（#8194）。
- ⚠️ **流式错误隔离**：v11.30.3 在流式 JSONL 值无法序列化时只让对应调用失败（#7937）；v11.30.1 让 `onError` 拿到经 `httpBatchStreamLink` 流式传输的错误所属调用（#7938），并在 `errorFormatter` 抛错时保持流式批处理存活（#7936）。
- 🛡️ **SSE 错误上报**：v11.30.2 修复 `@trpc/server`：SSE 响应在发送 headers 后失败时，将错误归属到对应调用（#7935）。
- 📦 **包副作用标记**：v11.30.2 将 `@trpc/client` 标记为 side-effect free（#7701），作者 KATT 和 kuldeeepy。
- 🧪 **react-server 导入**：v11.30.3 让 `@trpc/tanstack-react-query` 的 `createTRPCOptionsProxy` 可从 react-server 环境导入（#7708）。
- ✅ **早期错误 JSON**：v11.29.12 让 `@trpc/server` 将早期错误响应以 JSON 发送（#7768），作者 10kartik。

### [GitHub - jasnell/node-skills · GitHub](https://github.com/jasnell/node-skills)

jasnell/node-skills 在 GitHub 提供一套面向编码代理的 Node.js 技能，用于补齐训练数据之后的新能力，覆盖 Node.js 24 LTS 以来的新内置模块、API 与 flag、默认值变更和移除项，并通过固定文档提交和多版本可运行示例降低代理生成过时代码的风险，同时配套 Claude Code 与 opencode 安装方式和维护工具链。

- 🚀 **技能定位**：仓库提供可被 Claude Code 和 opencode 加载的代理技能，专门补齐编码代理训练数据之后新增的 Node.js 能力，覆盖 Node.js 24 LTS 以来的新内置模块、API 与 flag、默认值变更和移除项。
- 🧪 **文档与示例验证**：每项技能依据 nodejs/node 文档的固定 commit 编写，技能中的结论由可运行示例在 v24 LTS、current 和 main 构建上检查，以确认跨版本行为。
- 🧩 **覆盖范围**：技能覆盖 `node:sqlite`、`node:crypto`、`node:test`、权限模型、网络、`node:vfs`、`node:ffi`、`node:quic`/`node:dtls` 等主题，并为部分能力标出最低版本，如 `node-process-timeout` 26.11、`node-bench` 26.9、`node-zip` 26.8、`node-vfs` 26.4、`node-ffi` 26.1。
- 🛡️ **实验性 API 防护**：覆盖 Stability 1.x 功能的技能会以 Experimental API 横幅开头，要求代理先调用 `node-experimental-check`，在已安装的 Node.js 版本上核验细节后再生成代码，该检查技能的 floor 为 24。
- 📦 **安装方式**：Claude Code 可通过 `/plugin marketplace add jasnell/node-skills` 和 `/plugin install node-skills@node-skills` 安装带命名空间、可更新版本；也可用 `node install/install.mjs --target claude` 或 `--target opencode` 创建符号链接，并支持 `--scope project`、`--mode copy`、`--only`、`--uninstall`、`--dry-run`。
- 🛠️ **维护流程**：仓库内置 `.claude/skills/node-skills-maintainer` 维护技能，但不会随插件发布；流程包括用 `tools/survey.mjs` 调查新增和变更 API、分流归属、并行委派编写、在二进制矩阵上验证、用触发评测打磨描述，以及处理晋级、移除和 floor 线路 EOL。
- ⚙️ **质量工具**：工具仅需 Node.js 24+ 且无依赖，提供 `survey.mjs --since --changes --uncovered`、`skill-budget.mjs`（常驻 ≤200 tokens、激活 ≤1000）、`skill-lint.mjs`、`run-examples.mjs`、`check-drift.mjs`、`trigger-eval.mjs` 和 `discrepancies.mjs`，并用 `node --test tools/` 跑结构、lint 与预算测试。
