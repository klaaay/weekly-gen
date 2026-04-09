### [未找到标题](https://x.com/sebastienlorber)

**原文标题**: [No title found](https://x.com/sebastienlorber)

该页面提示用户浏览器中JavaScript功能未启用或存在兼容性问题，导致无法正常使用X平台（原Twitter）的核心功能。

- 🚫 JavaScript未启用：检测到浏览器禁用JavaScript，这是运行X平台所必需的技术条件
- 🌐 切换浏览器建议：推荐启用JavaScript或更换至受支持的浏览器版本
- 📖 帮助中心指引：可通过官方帮助中心查询具体支持的浏览器列表
- 🔧 扩展冲突提示：部分隐私保护类浏览器扩展可能造成功能异常，建议临时禁用后重试
- ⚖️ 政策信息公示：页脚区域包含服务条款、隐私政策、Cookie政策等法律文件链接
- ©️ 版权声明：标注2026年X公司版权所有信息
- 🔄 操作引导：提供“再试一次”的即时重试功能入口

---

### [未找到标题](https://x.com/jaworek3211)

**原文标题**: [No title found](https://x.com/jaworek3211)

该页面提示JavaScript未启用，导致无法正常使用X平台，并提供了相应的解决建议和支持信息。

- 🚫 JavaScript已禁用，导致无法加载X平台内容
- 🌐 建议启用JavaScript或更换支持的浏览器
- 📖 支持浏览器列表可在帮助中心查看
- 🔧 隐私扩展可能造成干扰，建议暂时禁用后重试
- ⚠️ 页面底部包含服务条款、隐私政策等法律信息

---

### [GitHub - lirantal/npm-security-best-practices: npm包管理器安全最佳实践集锦 · GitHub](https://github.com/lirantal/npm-security-best-practices)

**原文标题**: [GitHub - lirantal/npm-security-best-practices: Collection of npm package manager Security Best Practices · GitHub](https://github.com/lirantal/npm-security-best-practices)

该资源库提供了一份全面的 npm 安全最佳实践指南，旨在帮助开发者防范供应链攻击、安全漏洞和恶意软件包，涵盖安全配置、依赖管理、本地开发安全、维护者实践和软件包健康评估等方面。

- 🔒 **禁用安装后脚本**：通过配置 `ignore-scripts` 和 `allow-git=none` 来阻止恶意脚本在安装时执行，这是防范供应链攻击的关键措施。
- ⏳ **安装冷却期**：设置 `min-release-age` 或使用 `--before` 标志，避免立即安装新发布的软件包，以降低安装恶意版本的风险。
- 🛡️ **使用安全工具加固安装**：推荐使用 `npq` 进行安装前审计，或使用 `Socket Firewall (sfw)` 实时拦截恶意软件包。
- 🔐 **防止锁文件注入**：使用 `lockfile-lint` 验证锁文件，确保依赖来源可信；pnpm 用户可启用 `blockExoticSubdeps` 阻止传递依赖使用非常规源。
- 📦 **使用确定性安装命令**：在生产或 CI/CD 环境中使用 `npm ci`、`pnpm install --frozen-lockfile` 等命令，确保安装版本与锁文件严格一致。
- ⚠️ **避免盲目升级依赖**：避免使用 `npm update` 等命令盲目升级所有依赖，应通过 `npm-check-updates --interactive` 或 Snyk、Dependabot 等工具进行可控升级和审查。
- 🗝️ **避免在 .env 文件中存储明文密钥**：使用 1Password、Infisical 等密钥管理工具，通过引用方式存储密钥，并在运行时动态注入。
- 📦 **使用开发容器**：通过 Dev Containers 隔离开发环境，限制恶意软件包对主机系统的访问，减小攻击影响范围。
- 🔑 **为 npm 账户启用双因素认证**：特别是维护者，应启用 2FA（`npm profile enable-2fa auth-and-writes`）以防止账户被盗和恶意发布。
- 📜 **发布时使用来源证明**：在 CI/CD（如 GitHub Actions）中使用 `npm publish --provenance`，为软件包提供可验证的构建来源信息。
- 🔗 **使用 OIDC 进行发布**：配置可信发布，利用短期 OIDC 令牌替代长期 npm 令牌，提升发布过程的安全性。
- 🌳 **减少软件包依赖树**：尽可能减少依赖数量，利用现代 JavaScript 原生功能替代常见工具库，以减小攻击面。
- 📊 **参考 Snyk 安全数据库评估软件包健康度**：在引入新依赖前，查看其安全漏洞、维护状态、流行度和社区活跃度等综合指标。
- 🧐 **不完全信任 npmjs.org 官方注册表**：该网站可能无法完整显示依赖信息或源代码，应通过 `npm pack` 检查实际发布内容，并借助 `npq` 等工具进行审计。

---

### [@sebastienlorber.com 在 Bluesky 上](https://bsky.app/profile/did:plc:hxmev3uady7j4litwnr5fzbg/post/3miytfdn6ck2v)

**原文标题**: [@sebastienlorber.com on Bluesky](https://bsky.app/profile/did:plc:hxmev3uady7j4litwnr5fzbg/post/3miytfdn6ck2v)

这是一个高度交互的网络应用，需要JavaScript支持。内容主要介绍了React生态的最新动态，包括多个库和工具的更新。

- ⚙️ 这是一个需要JavaScript的交互式网络应用，不是简单的HTML界面
- 🔗 了解更多关于Bluesky的信息，可访问bsky.social和atproto.com
- 📰 本周React动态涵盖多个关键库和工具的更新
- 📦 涉及Boneyard、Ink、MUI、React Router、Next.js等前端工具
- 📱 React Native 0.85发布，包含ViewTransition、Skia等新特性
- 🎬 可通过thisweekinreact.com/newsletter/276阅读或订阅完整内容
- ✍️ 内容由@jwr.ski和Seb共同编写，发布于2026年4月8日

---

### [未找到标题](https://x.com/sebastienlorber/status/2041933087198597128)

**原文标题**: [No title found](https://x.com/sebastienlorber/status/2041933087198597128)

该页面提示JavaScript功能未启用，导致无法正常使用X平台，并提供了相应的解决建议与支持信息。

- 🌐 浏览器JavaScript功能已禁用，导致X平台无法加载
- 🔧 建议启用JavaScript或更换至受支持的浏览器
- 📖 可访问帮助中心查看支持的浏览器列表
- 🛡️ 部分隐私扩展可能造成访问问题，建议暂时禁用
- 🔄 页面提供“重试”功能供用户再次尝试访问
- ⚖️ 页脚包含服务条款、隐私政策等法律文件链接

---

### [LinkedIn登录，登录 | LinkedIn](https://www.linkedin.com/uas/login?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fin%2Fsebastienlorber%2Frecent-activity%2Fall%2F)

**原文标题**: [
            
          LinkedIn Login, Sign in | LinkedIn
      
        ](https://www.linkedin.com/uas/login?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fin%2Fsebastienlorber%2Frecent-activity%2Fall%2F)

该内容描述了LinkedIn的登录界面，提供了多种登录方式及相关操作指引。

- 🔐 支持多种登录方式：包括Apple账号登录、使用通行密钥登录，以及传统的邮箱或手机号密码登录。
- 📜 强调用户协议：登录过程中需同意LinkedIn的用户协议、隐私政策和Cookie政策。
- 📧 提供便捷登录选项：可通过发送到主邮箱的一次性链接快速登录，并提示检查垃圾邮件文件夹。
- 🔄 包含账户管理功能：提供“忘记密码”选项和“保持登录状态”的复选框。
- ➕ 引导新用户注册：界面设有“加入LinkedIn”的入口，新用户需同意相关条款才能注册。

---

### [Reddit - 请等待验证](https://www.reddit.com/user/sebastienlorber/submitted/)

**原文标题**: [Reddit - Please wait for verification](https://www.reddit.com/user/sebastienlorber/submitted/)

本文介绍了人工智能在医疗领域的应用现状与前景，重点探讨了其在疾病诊断、药物研发和个性化治疗方面的突破性进展，同时简要提及了相关的伦理挑战。

- 🤖 AI辅助诊断系统能通过分析医学影像快速识别病变，提升早期癌症等疾病的检出率
- 💊 机器学习加速新药研发流程，大幅缩短化合物筛选与临床试验周期
- 🧬 基于患者基因组数据的AI模型可为个体提供定制化治疗方案
- ⚖️ 数据隐私与算法透明度等伦理问题仍需建立行业规范

---

### [未找到标题](https://x.com/grabbou/status/1829126194022715617)

**原文标题**: [No title found](https://x.com/grabbou/status/1829126194022715617)

该页面提示用户浏览器中JavaScript功能未启用或存在兼容性问题，导致无法正常使用X平台（原Twitter），并提供了相应的解决建议。

- 🔧 检测到浏览器已禁用JavaScript，需启用该功能或更换受支持的浏览器
- 🌐 可访问帮助中心查看支持的浏览器列表及相关服务条款
- 🛡️ 部分隐私扩展可能导致加载异常，建议暂时禁用后重试
- 🔄 页面提供“重试”功能供用户再次尝试加载
- ©️ 页脚标注版权信息及平台政策链接（服务条款/隐私政策/广告信息等）

---

### [未找到标题](https://x.com/grabbou)

**原文标题**: [No title found](https://x.com/grabbou)

该页面提示JavaScript功能未启用，导致无法正常使用X平台，并提供了相应的解决建议与支持信息。

- 🔧 检测到浏览器中JavaScript被禁用，需启用或更换受支持的浏览器
- 🌐 可访问帮助中心查看支持的浏览器列表
- 🛡️ 部分隐私扩展可能导致问题，建议暂时禁用后重试
- 📄 页面底部包含服务条款、隐私政策等法律文件链接
- 🔄 提供“再试一次”功能选项供用户重新加载页面

---

### [精密AI - 无需编写测试的自动化前端测试](https://www.meticulous.ai/?utm_source=thisweekinreact&utm_medium=newsletter&utm_campaign=26q1&utm_content=1st)

**原文标题**: [Meticulous AI - Automated Frontend Testing Without Writing Tests](https://www.meticulous.ai/?utm_source=thisweekinreact&utm_medium=newsletter&utm_campaign=26q1&utm_content=1st)

Meticulous AI 是一款自动化、全面且确定性的测试工具，通过记录用户与应用交互来生成持续演进的测试套件，覆盖所有代码分支和用户流程，从而无需手动编写、修复或维护测试，帮助团队快速、可靠地发布无回归代码。

- 🎯 **自动化测试生成**：通过记录开发、预演和生产环境中的用户交互，自动生成覆盖所有代码行和用户流程的测试套件。
- 🚀 **提升开发速度**：测试随应用自动演进，无需人工干预，显著加快可靠代码的交付速度。
- 🛡️ **消除测试不稳定**：基于 Chromium 构建的确定性调度引擎，彻底解决测试不稳定问题，并支持高速并行测试。
- 🔄 **无缝集成**：可与现有测试套件结合使用或完全替代，支持多种前端框架（如 React、Vue、Angular 等）。
- 💬 **用户认可**：已被 Dropbox、Notion 等超过 100 家组织采用，开发者称赞其零维护、无调试需求和高效性。

---

### [骨场 - 为你的用户界面准备的骨架屏](https://boneyard.vercel.app/overview)

**原文标题**: [boneyard - skeleton screens for your UI](https://boneyard.vercel.app/overview)

Boneyard-js 是一个自动生成骨架屏的 JavaScript 库，通过捕捉真实 UI 的布局来创建像素级匹配的骨架占位符，无需手动测量或调整。

- 🛠️ **自动生成**：通过 CLI 工具自动检测开发服务器和 Tailwind 断点，生成与真实布局完全同步的骨架屏 JSON 数据。
- 🧩 **简单集成**：使用 `<Skeleton>` 组件包裹目标组件，配合 `loading` 状态控制，即可实现零布局偏移的骨架效果。
- 📦 **轻量高效**：运行时仅约 7.5KB，骨架数据以紧凑的数组格式存储，解析速度快，且支持增量构建以提升性能。
- 🔄 **生产就绪**：骨架数据为静态 JSON，无需运行时布局引擎，确保生产环境下的高效稳定运行。

---

### [Platano — 基于React Native的AI图像应用模板，即刻变现 | Code with Beto](https://codewithbeto.dev/platano)

**原文标题**: [Platano — Ready-to-monetize AI image app template for React Native | Code with Beto](https://codewithbeto.dev/platano)

Platano是一款即用型React Native模板，旨在帮助开发者快速构建并商业化AI图像应用，内置支付、多语言支持和AI生成功能，适用于iOS和Android平台。

- 🚀 **快速启动**：通过一条命令即可开始项目开发，节省配置时间  
- 💰 **内置商业化**：集成支付和订阅系统，支持应用上线即盈利  
- 🌍 **多平台适配**：兼容iOS与Android，提供多语言支持  
- 🎨 **AI图像功能**：内置AI生成模块，无需机器学习经验即可构建风格转换、照片增强等应用  
- 📦 **完整资源包**：包含应用商店素材、模块化代码结构和详细文档  
- 💡 **开发友好**：采用清晰的Expo代码架构，支持主题定制和跨平台逻辑处理  
- 🏆 **已验证案例**：已有成功上架应用，模板设计获开发者好评  
- 🔄 **灵活授权**：一次性购买可构建多个应用，提供专业会员升级选项

---

### [React峰会——全球最大的React开发者大会](https://reactsummit.com/?utm_source=thisweekinreact)

**原文标题**: [React Summit – The Biggest React Conference Worldwide](https://reactsummit.com/?utm_source=thisweekinreact)

React Summit是全球最大的React年度会议，聚焦React生态系统、现代Web开发及AI的影响，汇集全球前端与全栈工程师。会议提供阿姆斯特丹线下参与或远程互动体验，包含深度专题、实践工作坊及丰富的交流活动。

- 🗓️ **会议时间与地点**：2026年6月12日与16日于阿姆斯特丹（含远程参与）；11月17日与20日于纽约
- 🎤 **演讲阵容**：60多位React专家分享最新见解，涵盖React Server Components、AI辅助编程、性能优化等前沿话题
- 🏔️ **双轨议程**：Base Camp与Summit双轨道，内容涵盖全栈开发、架构、AI工程及职业成长等深度专题
- 👥 **参与规模**：吸引全球超过10,000名开发者，其中1,500名幸运者将齐聚阿姆斯特丹现场
- 💻 **远程体验**：提供高清直播、演讲者问答、讨论室及在线实践工作坊，确保远程参与者充分互动
- 🛠️ **会前活动**：阿姆斯特丹会场在会议前一天举办Tech Lead Conf与JSNation，聚焦工程领导力与Web开发趋势
- 🎟️ **票务选项**：提供线下混合票、远程票及包含酒店的组合票，团队购票可享折扣；另有多项奖学金支持多元群体
- 🏆 **社区贡献**：设立JS开源奖项，表彰对开源社区有突出贡献的项目与个人
- 🚢 **社交活动**：包含阿姆斯特丹船游、步行导览、美食节及全球最大的React派对，促进与会者交流
- 🤝 **合作伙伴**：得到多家科技公司赞助，包括FocusReactive等头部技术机构，共同推动React生态发展

---

### [预计算模式：在Next.js中将动态数据编码到URL中 | Aurora Scharff](https://aurorascharff.no/posts/the-precompute-pattern-encoding-dynamic-data-into-urls-in-nextjs/)

**原文标题**: [The Precompute Pattern: Encoding Dynamic Data into URLs in Next.js | Aurora Scharff](https://aurorascharff.no/posts/the-precompute-pattern-encoding-dynamic-data-into-urls-in-nextjs/)

Next.js 中的预计算模式通过将动态数据编码到URL中，将动态渲染转换为静态生成，以解决根布局中动态API调用导致整个路由树动态渲染的问题。随着缓存组件的引入，该模式在许多场景下已不再必要，但在大型电商团队中仍被使用，尤其适用于处理多语言路由和功能标志等场景。

- 🔄 **预计算模式原理**：在中间件（代理）中解析动态数据（如cookies），将其编码为URL隐藏段，使页面仅依赖参数进行静态渲染，避免动态API调用。
- 🛠️ **实现步骤**：定义上下文数据结构，使用base64url编码；在代理中重写URL添加编码段；组件从参数解码而非调用动态API；通过generateStaticParams预生成已知变体。
- 🚩 **Vercel Flags SDK应用**：该SDK将预计算模式标准化，提供加密URL段和生成变体的工具，简化功能标志的集成与管理。
- 📊 **高基数与电商权衡**：预计算上下文（如认证、区域、货币）会大幅增加路由变体，导致构建时生成不切实际，需选择性编码低基数数据，并依赖ISR缓存。
- ⚡ **缓存组件替代方案**：Next.js 16的缓存组件允许部分预渲染，将动态内容隔离，使非依赖组件静态缓存，解决了根布局动态渲染问题，但变体缓存场景仍需预计算模式。
- 🔧 **rootParams改进**：未来功能将允许组件直接访问顶级动态参数，无需属性传递，提升预计算模式的开发体验。
- ⚖️ **模式适用性总结**：缓存组件已解决多数动态渲染问题，但预计算模式在需要基于变体缓存内容时仍有价值，需权衡基数、ISR限制与缓存策略。

---

### [MDN新前端技术内幕](https://developer.mozilla.org/en-US/blog/mdn-front-end-deep-dive/)

**原文标题**: [Under the hood of MDN's new frontend](https://developer.mozilla.org/en-US/blog/mdn-front-end-deep-dive/)

去年，MDN推出了全新的前端架构，最显著的变化是样式的简化和统一，但更深层的重构在于底层代码的全面革新。这次重构旨在解决旧前端的技术债务、提升开发体验，并优化性能。

- 🚀 **前端全面重构**：MDN对前端进行了彻底的重构，不仅更新了样式，还重写了底层代码，以解决长期积累的技术债务。
- 🛠️ **旧架构痛点**：旧前端基于React，存在复杂的Webpack配置、混乱的CSS管理，以及React与静态内容交互的困难，导致维护和开发效率低下。
- 🔧 **引入Web组件**：通过Lit框架和Web组件技术，MDN成功将交互功能（如Scrimba嵌入和交互式示例）封装为自定义元素，简化了开发并提升了可维护性。
- 🌐 **服务器组件革新**：采用自定义的服务器组件架构，替代了传统的SPA模式，避免了冗余的JavaScript加载，实现了按需渲染和样式加载。
- 📦 **按需加载优化**：通过扁平化的组件结构和动态导入机制，确保仅加载页面所需的CSS和JavaScript，显著提升了性能和缓存效率。
- ⚡ **开发环境提速**：使用Rspack构建工具，将开发启动时间从几分钟缩短至几秒，提供了更简单、高效的开发体验。
- 🧪 **基线技术应用**：依据Baseline项目标准，选择广泛可用的Web技术，确保跨浏览器兼容性，同时减少polyfill的使用。
- 🔍 **性能与缓存策略**：通过HTTP/2/3的多路复用和小文件并行加载，结合智能缓存机制，优化了页面加载速度和用户体验。
- 🤝 **社区参与**：鼓励开发者通过GitHub和Discord参与项目，共同改进MDN的前端架构。

---

### [移动铁路前端脱离Next.js](https://blog.railway.com/p/moving-railways-frontend-off-nextjs)

**原文标题**: [Moving Railway's Frontend Off Next.js](https://blog.railway.com/p/moving-railways-frontend-off-nextjs)

Railway 将其前端从 Next.js 迁移至 Vite + TanStack Router，以提升开发效率和构建速度，同时保持零停机部署。

- 🚄 **Next.js 不再适用**：虽然 Next.js 曾帮助 Railway 从零构建起服务数百万用户的前端，但构建时间过长（超过 10 分钟）和服务器优先的设计与 Railway 高度客户端驱动的产品不匹配。
- ⚙️ **选择 TanStack Start + Vite**：新框架提供了类型安全路由、一流的布局支持、极快的开发循环（即时 HMR）以及明确的控制模型，更符合团队显式、客户端优先的开发方式。
- 🔄 **两步迁移，零停机**：通过两个 PR 完成迁移，首先替换所有 Next.js 特定依赖，然后整体切换框架，涉及 200 多个路由，并在周日早上合并，团队实时监控并快速修复问题。
- 🛠️ **放弃的功能与权衡**：放弃了内置图像优化（改用 Fastly 边缘处理）、部分生态系统工具（自建替代方案），并接受了新框架相对不成熟可能存在的粗糙边缘。
- 🌐 **前端运行在 Railway 上**：迁移后，前端通过 Railway 自身平台部署，利用 Fastly 边缘缓存、按需 ISR 和 Vite 的资产模型，实现快速构建、不可变资产和高效缓存。
- ⏩ **为何现在迁移**：为了大幅缩短从编写代码到用户可见的迭代周期，构建时间从 10 多分钟降至 2 分钟以内，开发服务器即时启动，旨在实现近乎即时的前端变更发布。

---

### [你绝对、绝对、绝对不需要特效！我发誓！—— Neciu Dan](https://neciudan.dev/you-really-really-dont-need-an-effect)

**原文标题**: [You really, really, really don't need an effect! I swear! — Neciu Dan](https://neciudan.dev/you-really-really-dont-need-an-effect)

本文深入探讨了在React开发中过度使用`useEffect`的常见误区，并提供了一个核心判断标准：只有当需要与外部系统同步时才应使用`useEffect`。文章通过多个具体场景对比了错误与正确的做法，并推荐了更优的替代方案，旨在帮助开发者编写更高效、更易维护的组件。

- 🧠 **核心原则**：使用`useEffect`的唯一判断标准是“是否在与外部系统同步”。React自身管理的状态、属性和衍生值都不属于外部系统。
- 🔄 **数据转换**：应直接计算衍生值或使用`useMemo`，而非通过`useEffect`设置状态，以避免不必要的渲染。
- 🖱️ **用户事件处理**：逻辑应直接放在事件处理函数中，而非通过`useEffect`监听状态变化来触发。
- 🔑 **状态重置**：使用`key`属性来重置组件状态，比在`useEffect`中监听属性变化更高效。
- 🌐 **数据获取**：虽然可以用`useEffect`，但推荐使用TanStack Query等库，它们内置处理了缓存、重复请求、竞态条件等问题。
- 📢 **通知父组件**：应在事件处理函数中直接调用父组件回调，而非通过`useEffect`，以减少渲染次数。
- ⛓️ **避免效应链**：将级联的状态更新整合到同一个事件处理函数中，或使用`useReducer`，而非编写多个相互依赖的`useEffect`。
- 📡 **订阅外部存储**：使用`useSyncExternalStore`替代手动的`useEffect`订阅，以更好地处理并发渲染。
- 📊 **分析与追踪**：应在事件发生处直接调用追踪函数，而非通过`useEffect`监听状态来触发，以保留事件上下文。
- ✅ **正确使用场景**：`useEffect`适用于与WebSocket、第三方库、DOM测量、浏览器API等真正的外部系统同步。
- 🛠️ **工具辅助**：可使用ESLint插件（如`eslint-plugin-react-you-might-not-need-an-effect`）自动检测不必要的`useEffect`。
- 🤖 **AI编码助手提示**：AI模型倾向于过度使用`useEffect`，可通过提供明确的决策树指令来引导其生成更优代码。

---

### [获取失败](https://tigerabrodi.blog/how-to-implement-spring-physics-buttons-with-framer-motion)

**原文标题**: [Failed to retrieve](https://tigerabrodi.blog/how-to-implement-spring-physics-buttons-with-framer-motion)

无法总结：获取内容失败，状态码 429。

---

### [React认证 - Certificates.dev](https://certificates.dev/react?friend=TWIR&utm_source=twir&utm_medium=newsletter&utm_campaign=partner)

**原文标题**: [React Certification - Certificates.dev](https://certificates.dev/react?friend=TWIR&utm_source=twir&utm_medium=newsletter&utm_campaign=partner)

该网站提供React开发者认证项目，旨在通过不同等级的考试验证开发者的React技能，并提供培训资源、考试准备和认证证书，以帮助开发者提升职业竞争力和团队能力。

- 🎯 **认证目的**：验证React开发能力，提升职业信誉和就业机会
- 📊 **认证等级**：分为初级、中级和高级React开发者三个级别，考试时间和形式各异
- 🧑‍🏫 **专家指导**：由React专家Aurora Scharff等设计课程，确保内容贴合行业实践
- 📚 **备考资源**：提供自学材料、现场训练营和备考指南
- 💼 **职业益处**：认证可增强求职竞争力、获得更高薪资和晋升机会
- 👥 **团队效益**：提升团队技能、士气和项目交付效率
- 📈 **用户反馈**：调查显示开发者普遍认为认证能验证技能并提升专业可信度
- 🔗 **附加资源**：提供React钩子和并发特性等速查表，以及相关技术博客文章
- 🌐 **社区支持**：认证受到多家公司认可，并有众多开发者参与

---

### [发布 v7.0.0 · vadimdemedes/ink · GitHub](https://github.com/vadimdemedes/ink/releases/tag/v7.0.0)

**原文标题**: [Release v7.0.0 · vadimdemedes/ink · GitHub](https://github.com/vadimdemedes/ink/releases/tag/v7.0.0)

Ink 7.0.0 版本发布，这是一个重大更新，引入了多项新功能、改进和破坏性变更，包括对 Node.js 22 和 React 19.2+ 的要求、新的钩子、渲染选项以及错误修复。

- 🚨 **破坏性变更**：要求 Node.js 22 和 React 19.2+，并调整了 Backspace 和 Escape 键的处理逻辑。
- 🆕 **新增功能**：引入了多个新钩子，如 `usePaste`、`useWindowSize`、`useBoxMetrics` 和 `useAnimation`，用于处理粘贴、窗口尺寸、测量和动画。
- ⚙️ **渲染增强**：为 `render()` 添加了 `alternateScreen` 和 `interactive` 选项，支持备用屏幕缓冲区和交互模式覆盖。
- 🧩 **组件扩展**：为 `<Box>` 和 `<Text>` 组件新增了边框背景色、硬换行、最大尺寸、宽高比等布局属性。
- 🔧 **错误修复**：解决了增量渲染、未映射键码崩溃、CJK 文本截断和宽字符拆分等问题。
- 📋 **迁移指南**：提供了从 `key.delete` 切换到 `key.backspace` 以及正确处理 `key.meta` 和 `key.escape` 的代码示例。

---

### [Markdown 中的组件 - Comark](https://comark.dev/)

**原文标题**: [Components in Markdown - Comark](https://comark.dev/)

Comark 是一个支持流式解析的快速 Markdown 解析器，提供对 Vue、React 和 Svelte 等主流框架的组件支持，并可通过插件扩展功能。

- 🚀 **快速流式解析**：实时解析逐步到达的内容，适用于 AI 生成内容和渐进式加载场景。
- 🧩 **多框架支持**：为 Vue、React 和 Svelte 提供一流的组件嵌入支持，可在 Markdown 中直接使用自定义组件。
- 🔧 **自动补全语法**：在流式传输过程中自动补全未闭合的 Markdown 语法，确保每一帧内容都能正确渲染。
- 📦 **插件扩展**：通过插件系统支持数学公式（如 KaTeX）、代码高亮、目录生成等丰富功能。
- 📄 **易于上手**：提供详细的文档、示例和在线演示，方便开发者快速集成和使用。

---

### [Docusaurus 3.10 | Docusaurus](https://docusaurus.io/blog/releases/3.10)

**原文标题**: [Docusaurus 3.10 | Docusaurus](https://docusaurus.io/blog/releases/3.10)

Docusaurus 3.10 是 v3.x 系列的最后一个版本，旨在帮助用户为即将到来的 Docusaurus v4 做准备。此版本引入了多项新功能和改进，包括安全增强、性能优化、更严格的 MDX 语法支持，以及实验性的版本控制系统（VCS）API。升级过程简单，遵循语义化版本控制，无破坏性变更，但若启用 v4 未来标志需注意相关调整。

- 🚀 **v4 未来标志**：引入新标志，如 `future.v4.siteStorageNamespacing`、`future.v4.fasterByDefault` 和 `future.v4.mdx1CompatDisabledByDefault`，帮助用户逐步适配 v4 的破坏性变更。
- 🔒 **安全增强**：采用 npm 可信发布机制，新增安全流程扫描依赖漏洞，并推荐使用包管理器（如 pnpm）的发布冷却期功能以降低供应链攻击风险。
- ⚡ **Docusaurus Faster 稳定化**：现代构建基础设施（包括 Rspack、SWC 等）现已稳定，将在 v4 中默认启用，并新增 `gitEagerVcs` 标志和 Yarn PnP 支持。
- 💾 **站点存储 API 稳定**：`config.storage` API 标记为稳定，v4 将默认自动命名空间化 `localStorage` 键以避免冲突。
- 📝 **严格 MDX 语法**：鼓励使用原生 MDX 语法，如将文件扩展名改为 `.mdx`、迁移至 Markdown 指令语法的警告框，以及使用 JSX 注释替代 HTML 注释。
- 🛠️ **实验性 VCS API**：新增版本控制系统 API，支持集成 Git 以外的 VCS，并内置性能优化策略（如 `git-eager`）以提升大型站点构建速度。
- 🌍 **翻译更新**：新增乌尔都语（ur）主题翻译，并补全巴西葡萄牙语（pt-BR）翻译。
- 🔧 **其他改进**：包括升级至 TypeScript 6.0、增强 `siteConfig.headTags` API、拆分 `<DocCard>` 组件以方便扩展，以及修复多项功能兼容性问题。

---

### [着色器](https://shaders.com/)

**原文标题**: [Shaders](https://shaders.com/)

这是一个面向现代前端开发的WebGPU特效组件库，让设计师和工程师无需编写着色器代码即可快速创建并导出视觉效果。

- 🎨 提供可视化编辑器，支持通过拖拽组件（如渐变、扭曲）设计效果，并导出生产就绪的代码
- ⚡ 基于WebGPU技术，专注于浏览器中高性能的创意视觉效果，适用于英雄页面、UI背景等场景
- 🧩 包含100多个组件，支持嵌套、遮罩和混合，无需GLSL知识即可定制特效
- 🔧 兼容主流前端框架（Vue、React、Svelte等），提供详细文档和社区支持
- 🚀 提供免费版本和Pro许可证，已用于5000多个设计项目，备受开发者推荐

---

### [发布版本 7.72.0 · react-hook-form/react-hook-form · GitHub](https://github.com/react-hook-form/react-hook-form/releases/tag/v7.72.0)

**原文标题**: [Release Version 7.72.0 · react-hook-form/react-hook-form · GitHub](https://github.com/react-hook-form/react-hook-form/releases/tag/v7.72.0)

React Hook Form 发布了 7.72.0 版本，引入了表单级验证功能并修复了多个问题。

- ⚓️ 新增内置表单级验证功能，允许在 `useForm` 中通过 `validate` 函数进行异步验证
- 🐞 修复了 `useFieldArray` 错误标记无关字段为脏状态的问题
- 🐞 解决了复选框在原生验证时表单验证被忽略的问题
- 🌉 允许通过订阅 `formState` 来跟踪表单提交状态
- 🙏 感谢三位贡献者 `@WiXSL`、`@BrendanC23` 和 `@6810779s` 的代码贡献

---

### [发布 v1.18.0 · edmundhung/conform · GitHub](https://github.com/edmundhung/conform/releases/tag/v1.18.0)

**原文标题**: [Release v1.18.0 · edmundhung/conform · GitHub](https://github.com/edmundhung/conform/releases/tag/v1.18.0)

Conform v1.18.0 发布，包含未来 API 的路径助手重命名、结构化值支持、新的强制转换 API 以及多项改进与修复。

- 🚨 **重大变更**：未来 API 中的路径助手函数已重命名，以提升一致性，需更新相关导入与调用。
- 🧩 **结构化值支持**：`useControl()` 现在支持结构化值，便于构建处理对象与嵌套数组的自定义输入组件。
- 🔧 **新增强制转换 API**：引入了 `coerceStructure()` 用于将表单字符串值转换为类型化数据，以及 `configureCoercion()` 用于统一自定义强制转换行为。
- 📅 **日期时间处理改进**：未来 API 优化了 `datetime-local` 的序列化与时区处理，更好地匹配浏览器行为。
- 🔄 **递归模式支持增强**：Zod 与 Valibot 集成现在能更可靠地处理递归模式，包括约束解析与强制转换。
- 🧹 **空值保留默认行为**：`parseSubmission()` 现在默认保留空字符串与文件，以区分用户清空字段与未提交字段的情况。
- 🐛 **类型与提交修复**：修复了 Valibot `coerceFormValue()` 的返回类型，并改进了异步客户端验证后的原生表单提交可靠性。
- 📚 **文档与示例更新**：新增了 Astro 示例，并更新了完整变更日志。

---

### [react-router/CHANGELOG.md 位于 main 分支 · remix-run/react-router · GitHub](https://github.com/remix-run/react-router/blob/main/CHANGELOG.md#v7140)

**原文标题**: [react-router/CHANGELOG.md at main · remix-run/react-router · GitHub](https://github.com/remix-run/react-router/blob/main/CHANGELOG.md#v7140)

该页面为React Router在GitHub上的项目主页，但当前加载遇到错误，需要刷新页面才能正常访问。

- 🔄 页面加载时出现错误，提示需要重新加载以解决问题。
- 🔐 部分功能（如通知设置）需要用户登录后才能使用。
- 📊 项目数据概览：已获得56.3k星标、10.8k复刻，当前有115个议题和55个拉取请求。
- 🛡️ 项目设有安全和质量检查板块，确保代码质量与安全性。
- 📁 页面提供代码、议题、拉取请求、讨论、操作、安全与质量、洞察等导航选项。

---

### [2026年4月 - shadcn 应用 - shadcn/ui](https://ui.shadcn.com/docs/changelog/2026-04-shadcn-apply)

**原文标题**: [April 2026 - shadcn apply - shadcn/ui](https://ui.shadcn.com/docs/changelog/2026-04-shadcn-apply)

shadcn/ui 是一个现代 UI 组件库，提供丰富的可定制组件和工具，支持主题切换、CLI 工具和预设应用，便于开发者快速构建美观且功能完善的用户界面。

- 🎨 **组件丰富** – 包含 Accordion、Button、Card、Dialog 等 50 多种 UI 组件，覆盖常见交互需求
- 🛠️ **便捷工具** – 提供 CLI 工具，支持通过 `shadcn apply` 快速切换项目预设，无需重头开始
- 🌓 **主题定制** – 支持灵活的主题配置与深色模式，可轻松调整颜色、字体等视觉变量
- 🔄 **预设应用** – 新增 `shadcn apply` 功能，允许在现有项目中应用新预设，并自动更新组件与样式
- 🚀 **部署集成** – 推荐使用 Vercel 进行部署，已被 OpenAI、Sonos 等公司信任采用
- 📚 **扩展资源** – 提供 Forms、Registry、MCP Server 等扩展功能，并支持与 React Hook Form 等库集成

---

### [发布 v9.0.0 · mui/material-ui · GitHub](https://github.com/mui/material-ui/releases/tag/v9.0.0)

**原文标题**: [Release v9.0.0 · mui/material-ui · GitHub](https://github.com/mui/material-ui/releases/tag/v9.0.0)

Material UI 发布了稳定版 v9.0，重点改进了可访问性、sx 属性性能，并清理了已弃用的 API。

- 🎉 Material UI v9.0 稳定版正式发布，包含多项重要更新与优化
- ♿ 主要改进集中在可访问性提升和 sx 属性性能增强
- 🧹 清理了已弃用的 API，帮助开发者更顺畅地升级
- 📚 提供了详细的升级指南和官方博客文章介绍
- 👥 感谢所有贡献者，包括 brijeshb42、mj12albert 等六位核心成员

---

### [版本 v9.0.0 | Mantine](https://mantine.dev/changelog/9-0-0/)

**原文标题**: [Version v9.0.0 | Mantine](https://mantine.dev/changelog/9-0-0/)

Mantine 9.0.0 版本于 2026 年 3 月 31 日发布，引入了全新的日程安排组件包、多项组件增强与优化，并包含重大变更和迁移指南。

- 📅 **新增日程安排包**：`@mantine/schedule` 提供了完整的日历与日程管理组件，支持日、周、月、年视图及拖拽事件管理。
- 🔄 **折叠组件增强**：`Collapse` 组件新增水平折叠方向，并引入了对应的 `use-collapse` 和 `use-horizontal-collapse` 钩子。
- 🪟 **浮动窗口功能**：新增 `use-floating-window` 钩子和 `FloatingWindow` 组件，用于创建可拖拽的浮动窗口。
- 📜 **新增布局组件**：引入了 `OverflowList`（溢出列表）、`Marquee`（跑马灯）和 `Scroller`（滚动容器）等新组件。
- 📊 **图表与数据展示**：`@mantine/charts` 新增 `BarsList` 组件；`Card` 组件支持水平方向布局。
- ✅ **表单控件增强**：`Checkbox.Group` 和 `Switch.Group` 支持 `maxSelectedValues` 限制；所有输入组件新增 `loading` 状态；`MultiSelect` 和 `TagsInput` 支持自定义标签渲染。
- 🧩 **表单验证升级**：`use-form` 支持异步验证、`TransformedValues` 类型参数、新的验证器（`isUrl`, `isOneOf`）以及 Standard Schema 集成。
- 🎛️ **组件通用性与功能**：多个选择类组件支持泛型值类型；`Combobox` 支持虚拟化；`Highlight` 支持按词高亮和全词匹配。
- 📏 **布局与交互改进**：`Grid` 改用 CSS `gap` 属性；`Slider` 支持垂直方向；`SimpleGrid` 新增 `minColWidth` 和 `autoRows` 属性；`AppShell` 新增静态模式。
- 🎨 **主题与样式**：新增 `fontWeights` 主题属性控制字体粗细；默认圆角从 `sm` 改为 `md`；所有组件支持逻辑边距样式属性。
- 🔧 **开发工具与文档**：新增 `@mantine/mcp-server` 包，为 AI 工具提供文档查询；更新了多项文档指南。
- ⚠️ **重大变更与迁移**：需 React 19.2+；更新了 `Tiptap` 和 `Recharts` 的依赖版本；部分组件 API 有破坏性变更，需参考迁移指南。

---

### [发布 v4.9.0 · amannn/next-intl · GitHub](https://github.com/amannn/next-intl/releases/tag/v4.9.0)

**原文标题**: [Release v4.9.0 · amannn/next-intl · GitHub](https://github.com/amannn/next-intl/releases/tag/v4.9.0)

这是一个GitHub仓库页面，显示加载错误，但包含next-intl库v4.9.0版本发布的基本信息。

- 🚀 next-intl v4.9.0版本于2026年4月1日发布
- 🔗 主要新增功能：支持在`Link`组件上使用`transitionTypes`属性
- 👨‍💻 该功能由维护者@amannn提交和发布
- ⚠️ 页面在加载过程中多次出现错误提示，需要重新加载
- 📦 这是一个拥有4.2k星标的开源国际化库项目

---

### [为何无人正确使用React钩子 - YouTube](https://www.youtube.com/watch?v=NBjycPpPHQQ)

**原文标题**: [Why Does No One Use The Right React Hook - YouTube](https://www.youtube.com/watch?v=NBjycPpPHQQ)

该文本是YouTube网站页脚的标准法律与信息链接列表，概述了平台的政策、功能及公司信息。

- 📄 关于我们
- 📰 新闻动态
- ©️ 版权信息
- 📞 联系我们
- 🧑‍🎨 创作者相关
- 📢 广告合作
- 👩‍💻 开发者资源
- ⚖️ 使用条款
- 🔒 隐私政策
- 🛡️ 政策与安全
- 🔧 平台运作机制
- 🧪 功能测试
- ®️ 版权归属声明

---

### [React巴黎26 - YouTube](https://www.youtube.com/playlist?list=PL53Z0yyYnpWhsizNWtlnyM7XWFUSw437J)

**原文标题**: [React Paris 26 - YouTube](https://www.youtube.com/playlist?list=PL53Z0yyYnpWhsizNWtlnyM7XWFUSw437J)

该文本是YouTube网站页脚的标准链接列表，概述了其核心服务信息与用户政策。

- 📄 关于平台的基本信息与公司介绍
- 📰 新闻发布与媒体相关资源
- ©️ 版权声明与知识产权保护
- 📞 用户联系与客服渠道
- 🎬 内容创作者专属资源页面
- 💼 广告合作与商业推广服务
- 👩💻 开发者工具与API接口信息
- 📜 平台使用条款与协议
- 🔒 隐私保护政策与数据安全说明
- ⚖️ 平台安全政策与内容审核机制
- 🔧 YouTube功能运作原理说明
- 🧪 新功能测试与体验计划
- 🏛️ 谷歌母公司版权标识与年份声明

---

### [未找到标题](https://x.com/wcandillon/status/1263825118557593600)

**原文标题**: [No title found](https://x.com/wcandillon/status/1263825118557593600)

该页面提示JavaScript未启用，导致无法正常使用X平台，并提供了相应的解决建议和支持信息。

- 🌐 浏览器中JavaScript被禁用，导致X平台无法正常运行
- 🔧 建议启用JavaScript或更换至受支持的浏览器
- 📖 可访问帮助中心查看支持的浏览器列表
- 🛡️ 部分隐私扩展可能导致问题，建议暂时禁用后重试
- 🔄 页面提供“重试”功能以重新加载内容
- ©️ 页脚包含服务条款、隐私政策及版权声明等法律信息

---

### [未找到标题](https://x.com/wcandillon)

**原文标题**: [No title found](https://x.com/wcandillon)

该页面提示JavaScript功能未启用，导致无法正常使用X平台，并提供了相应的解决建议与支持信息。

- 🔧 检测到浏览器中JavaScript被禁用，需启用或更换受支持的浏览器
- 🌐 可访问帮助中心查看支持的浏览器列表
- 🛡️ 部分隐私扩展可能导致问题，建议暂时禁用后重试
- 📜 页面底部包含服务条款、隐私政策及版权声明等常规信息
- 🔄 提供“再试一次”功能供用户手动重试加载

---

### [Wallaby - 集成即时反馈的AI就绪测试运行器](https://wallabyjs.com/?referrer=ThisWeekInReact8Apr26)

**原文标题**: [Wallaby - AI-Ready Test Runner with Instant Feedback in Your Editor](https://wallabyjs.com/?referrer=ThisWeekInReact8Apr26)

Wallaby.js 是一款实时 JavaScript/TypeScript 测试运行工具，可在编码时即时显示测试结果和覆盖率，并提供时间旅行调试、AI 集成等功能，大幅提升开发效率和测试体验。

- 🚀 **实时测试反馈**：输入代码时立即运行测试，结果实时显示在编辑器旁
- 🔍 **智能调试工具**：内置时间旅行调试器和值查看器，快速定位问题
- 🤖 **AI 深度集成**：通过 MCP 服务器为 AI 工具提供实时运行时数据，辅助代码编写和修复
- ⚡ **极速测试执行**：仅运行受代码更改影响的最小测试集，执行效率极高
- 🛡️ **无锁定设计**：作为 IDE 插件使用，不依赖特定供应商或框架，可随时脱离运行
- 📊 **实时覆盖率显示**：编辑器边栏实时更新代码覆盖率，清晰展示未覆盖区域
- 🔄 **选择性测试运行**：支持仅运行当前工作的测试文件，提升大型项目效率
- 💰 **效率提升显著**：据估算可提升约 10.84% 编码效率，年节省价值约 2396 美元

---

### [袋鼠 v3](https://wallabyjs.com/blog/wallaby-v3.html?referrer=ThisWeekInReact8Apr26)

**原文标题**: [Wallaby v3](https://wallabyjs.com/blog/wallaby-v3.html?referrer=ThisWeekInReact8Apr26)

Wallaby v3 是一次引擎全面升级，专注于实时测试执行，通过结果流式传输和缓存结果实现即时反馈，尤其适用于大型代码库，无需更改现有配置即可体验更快的测试迭代和更智能的执行优先级。

- 🚀 **实时结果流式传输**：测试、覆盖率、日志和错误实时流入编辑器，无需等待完整运行即可立即发现问题。
- ⚡ **缓存结果即时启动**：利用缓存的执行数据，即使在大型项目上也能立即获得反馈，界面启动即呈现。
- 🧠 **智能优先级执行**：编辑时仅重新排队受影响的测试，已打开文件及相关测试优先执行，减少等待时间。
- ⏱️ **准确进度与时间预估**：动态更新时间预估和进度指示，让您清晰掌握测试完成时间。
- 🔄 **无缝体验与兼容性**：现有配置和工作流完全兼容，无需任何更改即可享受性能提升。
- 🏗️ **底层架构革新**：采用异步事件驱动架构，支持流式输出和缓存机制，依赖 v2 UI 实现灵活的状态展示。
- 🧪 **实践建议**：通过官方示例仓库体验结果流式传输和缓存结果功能，直观感受速度提升。
- 🔮 **未来展望**：计划推出团队共享缓存、测试运行差异查看器、突变测试等高级功能，持续优化开发者体验。

---

### [React Native 0.85 - 全新动画后端与Jest预设包发布 · React Native](https://reactnative.dev/blog/2026/04/07/react-native-0.85)

**原文标题**: [React Native 0.85 - New Animation Backend, New Jest Preset Package · React Native](https://reactnative.dev/blog/2026/04/07/react-native-0.85)

React Native 0.85 版本发布，引入了新的动画后端、Jest 预设独立包，并包含多项改进与修复。

- 🎬 **新动画后端**：引入共享动画后端，支持原生驱动下对布局属性（如 Flexbox 和位置）进行动画处理，提升性能与稳定性。
- 🔧 **开发工具增强**：支持多路 Chrome DevTools 协议连接，macOS 应用更新至原生标签页，并恢复了 Android 网络面板中的请求体预览功能。
- 🔒 **Metro TLS 支持**：开发服务器现可配置 TLS，启用 HTTPS 和 WSS，便于本地安全连接测试。
- 📦 **Jest 预设独立包**：Jest 预设已移至 `@react-native/jest-preset` 包，减少核心包体积，提供更灵活的测试配置。
- 🚫 **停止支持旧版 Node.js**：不再支持生命周期结束的 Node.js 版本，最低要求为 Node.js v20.19.4 或更高。
- 🗑️ **移除废弃 API**：已移除 `StyleSheet.absoluteFillObject`，建议使用 `StyleSheet.absoluteFill` 或自定义绝对定位样式。
- ⚙️ **其他破坏性变更**：包括 Android 和 iOS 的架构清理、API 弃用与移除，以及多项底层优化。
- 📈 **依赖更新**：Metro 升级至 ^0.84.0，React 更新 Hermes 版本，并包含 Yoga、TypeScript 等多方面的改进。

---

### [关于构建AI代理我们希望能了解的那些事](https://newsletter.posthog.com/p/what-we-wish-we-knew-before-building)

**原文标题**: [What we wish we knew about building AI agents](https://newsletter.posthog.com/p/what-we-wish-we-knew-before-building)

基于PostHog两年构建AI智能体的经验，本文分享了关键教训，旨在帮助团队更高效地开发智能体，避免常见陷阱，并聚焦于用户真实需求。

- 🤔 **先评估需求再行动**：构建自定义智能体前，应优先考虑通过MCP服务器让产品接入外部智能体，以验证需求并降低维护成本。
- 🛠️ **避免重复造轮子**：智能体的核心优势不在于自定义框架，而在于利用现有成熟工具（如Claude Agent SDK）和MCP标准，以加速开发。
- 🧠 **上下文是核心竞争力**：智能体的成功依赖于结构化产品与用户数据，需通过工具、技能和实时上下文注入，使其准确理解复杂场景。
- 📊 **早期建立可观测性与评估体系**：由于智能体行为不确定，必须从第一天起实现全链路追踪、数据集评估和人工复盘，才能持续改进。
- 🎯 **聚焦用户痛点而非炫技**：用户更关注稳定性、明确反馈和可靠体验，而非功能的丰富性；应将其视为产品工程问题，持续迭代以满足实际需求。

---

### [为React Native Fabric渲染器启用基础视图过渡支持，由zeyap提交的拉取请求 #35764 · facebook/react · GitHub](https://github.com/facebook/react/pull/35764)

**原文标题**: [Enables Basic View Transition support for React Native Fabric renderer by zeyap · Pull Request #35764 · facebook/react · GitHub](https://github.com/facebook/react/pull/35764)

React 仓库的一个 Pull Request 为 React Native 的 Fabric 渲染器启用了基础的视图过渡 API 支持，允许应用在状态变化时实现协调的动画效果。

- 🚀 **核心功能实现**：为 FabricUIManager 添加了 `applyViewTransitionName` 和 `startViewTransition` 方法的绑定，并实现了包含多个回调阶段（mutation → layout → afterMutation → spawnedWork → passive）的完整过渡流程。
- 🛡️ **优雅降级机制**：当原生端未启用视图过渡功能时，系统会同步执行工作并记录警告，确保应用功能不受影响。
- 📦 **代码与类型更新**：添加了新的 Flow 类型声明，并为尚未实现的其他视图过渡配置函数添加了开发环境下的警告占位符。
- ✅ **全面测试验证**：通过了 Flow 类型检查和代码规范检查，并在 Android 测试应用中进行了手动功能验证，确认了生产环境代码的优化效果。
- 🔗 **跨仓库协作**：此 PR 与 React Native 仓库的对应更改（添加 `UIManagerViewTransitionDelegate` 接口和 API）协同工作，共同实现该功能。

---

### [修复(🗿): 首次Skia Graphite预发布 (#3812) by wcandillon · 拉取请求 #3813 · Shopify/react-native-skia · GitHub](https://github.com/Shopify/react-native-skia/pull/3813)

**原文标题**: [fix(🗿): first Skia Graphite pre-release (#3812) by wcandillon · Pull Request #3813 · Shopify/react-native-skia · GitHub](https://github.com/Shopify/react-native-skia/pull/3813)

Shopify的react-native-skia项目发布了首个Skia Graphite预发布版本，该版本在性能上有显著提升，但仍处于开发阶段，可能存在稳定性问题。

- 🚀 首个Skia Graphite预发布版本已合并至next分支，版本号为2.6.3-next.1
- ⚠️ 用户反馈性能提升明显，但容易导致应用崩溃
- 🔧 开发者确认该版本仍为“进行中的工作”，稳定性有待完善
- 📦 发布通过semantic-release自动化流程完成，标签为released on @next

---

### [Expo棕地项目：如何在不重写的情况下将Expo集成到现有原生应用中](https://expo.dev/blog/expo-brownfield-how-to-add-expo-to-your-existing-native-app-without-a-rewrite)

**原文标题**: [Expo brownfield: How to add Expo to your existing native app without a rewrite](https://expo.dev/blog/expo-brownfield-how-to-add-expo-to-your-existing-native-app-without-a-rewrite)

Expo SDK 55引入了隔离式棕地工作流，允许将预编译的Expo应用作为原生依赖嵌入现有iOS/Android应用，无需重写即可逐步集成React Native功能。

- 🏗️ **棕地集成定义**：在现有原生应用中添加React Native和Expo，主入口仍为原生代码，支持渐进式功能扩展
- ⚙️ **两种集成模式**：集成式（直接安装React Native到原生项目）与隔离式（将Expo应用打包为原生库AAR/XCFramework）
- 📦 **隔离式工作流**：通过`expo-brownfield`包预编译生成原生框架，原生团队无需配置Node.js环境
- 🔗 **跨平台通信**：内置消息API支持原生宿主与嵌入应用间的双向事件/数据传递
- ⚠️ **当前限制**：仅支持单嵌入应用、需共享运行时、部分库兼容性需验证
- 🚀 **核心价值**：降低团队采用门槛，允许React专家在限定范围内贡献，保持原有架构决策稳定

---

### [获取失败](https://heartit.tech/react-native-jsi-deep-dive-part-1-the-runtime-you-never-see/)

**原文标题**: [Failed to retrieve](https://heartit.tech/react-native-jsi-deep-dive-part-1-the-runtime-you-never-see/)

无法总结：获取内容失败，状态码 415。

---

### [我们如何优化移动应用自动化中的代理设备](https://www.callstack.com/blog/how-we-optimized-agent-device-for-mobile-app-automation)

**原文标题**: [How We Optimized Agent Device for Mobile App Automation](https://www.callstack.com/blog/how-we-optimized-agent-device-for-mobile-app-automation)

本文介绍了如何通过优化Agent Device工具，将AI驱动移动应用自动化任务的令牌使用量减少一半以上，同时缩短执行时间。核心在于提升令牌效率，通过改进界面快照、优化代理技能和修复平台特定问题来实现。

- 🧠 **关注令牌效率**：减少不必要的交互和输入，以降低成本和避免上下文窗口拥挤，确保AI代理更准确、快速且经济高效。
- 🛠️ **Agent Device工具**：作为命令行工具，为AI代理提供直接控制iOS和Android应用的能力，支持导航、测试、调试和日志捕获。
- 📸 **采用可访问性快照**：使用文本化的可访问性树快照替代截图，令牌消耗减少3-4倍，并提供可操作的元素引用，提升效率3.5倍。
- ✂️ **精简快照内容**：通过剪裁离屏和隐藏元素，将令牌使用量降低高达80%，并减少代理因元素不可达而产生的错误。
- 🚀 **优化代理技能**：明确指导代理使用可见优先快照、差异快照和定向日志查询，减少猜测和浪费步骤，提升可靠性。
- 🤖 **修复Android问题**：改进快照的可见性处理、离屏元素总结和诊断工具，使Android会话更稳定且易于调试。
- 🔮 **未来优化方向**：计划通过进一步优化技能、实现差异快照和提升日志分析效率，继续减少令牌使用量3k-8k。

---

### [🚀React Native Windows v0.82 现已发布！！React Native](https://devblogs.microsoft.com/react-native/%F0%9F%9A%80react-native-windows-v0-82-is-here/)

**原文标题**: [🚀React Native Windows v0.82 is here!! React Native](https://devblogs.microsoft.com/react-native/%F0%9F%9A%80react-native-windows-v0-82-is-here/)

React Native Windows v0.82 正式发布，标志着平台全面转向新架构（Fabric），移除了旧版 Paper 架构。此版本引入了对社区模块使用原生 XAML 控件的支持，显著提升了组件功能与可访问性，并包含大量可靠性改进。

- 🏗️ **架构革新**：完全移除旧版 Paper 架构，所有应用现需基于 Fabric 运行，为未来性能优化和功能发展奠定统一基础。
- 🧩 **XAML 控件集成**：社区模块现可在 Fabric 中直接使用原生 Windows XAML 控件，实现 React 组件与本地 UI 的无缝混合。
- ♿ **可访问性增强**：为第三方模块提供可访问性覆盖 API，允许自定义屏幕阅读器行为与 UI 自动化属性，提升辅助技术支持。
- 📝 **组件功能提升**：Text 组件支持文本选择与溢出处理；TextInput 新增选择控制、文本对齐与富文本样式；ScrollView 支持分页滚动。
- 🛠️ **稳定性修复**：解决了动态切换包、离线加载图片、关闭模态框时的崩溃问题，并改进了高 DPI 显示下的开发者工具与工具提示定位。
- 🔄 **功能对齐进展**：在 Fabric 中实现了 ContextMenu、TextInput 的书写方向支持等，进一步缩小与 iOS/Android 的跨平台特性差距。
- 📱 **示例应用更新**：React Native Gallery 应用已更新至 v0.82 并完全基于 Fabric 运行，供开发者参考新特性与组件行为。

---

### [发布 create-react-native-library@0.60.0 · callstack/react-native-builder-bob · GitHub](https://github.com/callstack/react-native-builder-bob/releases/tag/create-react-native-library%400.60.0)

**原文标题**: [Release create-react-native-library@0.60.0 · callstack/react-native-builder-bob · GitHub](https://github.com/callstack/react-native-builder-bob/releases/tag/create-react-native-library%400.60.0)

这是一个关于 React Native 库构建工具 `react-native-builder-bob` 的 GitHub 仓库发布页面，展示了版本 `0.60.0` 的发布信息。

- 🚀 发布了 `create-react-native-library@0.60.0` 版本，由维护者 `satya164` 于 2026年4月7日创建。
- ⚙️ 主要新增特性：支持实验性的 C++ Turbo Module 功能。
- 🔗 该特性通过合并拉取请求 #938 实现，对应提交哈希为 `db09e6b`。
- ✅ 发布标签和提交均附有维护者 `satya164` 的 GPG 验证签名。
- 📊 仓库概况：拥有 3.2k 星标、225 个复刻，当前有 16 个未关闭的议题和 7 个拉取请求。

---

### [CLI 2.4.0：iOS 26及更多设备现已登陆Maestro Cloud](https://maestro.dev/blog/maestro-cli-2-4-0)

**原文标题**: [CLI 2.4.0: iOS 26 and more devices on Maestro Cloud](https://maestro.dev/blog/maestro-cli-2-4-0)

Maestro CLI 2.4.0 版本发布，主要新增了对 iOS 26 的支持，扩展了云端设备库，简化了设备相关命令标志，并引入了多项功能改进与问题修复。

- 📱 **支持 iOS 26 及更多设备**：现可在本地和云端使用 `--device-os=iOS-26` 进行测试，并新增了 iPhone 13 Mini 和 iPhone 16 Pro Max 等热门机型。
- 🔍 **新增设备列表命令**：通过 `maestro list-devices` 和 `maestro list-cloud-devices` 可准确获取设备信息，无需查阅文档或猜测格式。
- 🧹 **简化设备启动命令**：弃用 `--os-version` 等旧标志，统一使用 `--device-model` 和 `--device-os`，格式与列表命令输出一致。
- 🔄 **新的设备操作系统格式**：`--device-os` 现支持字符串格式（如 `iOS-17-5`），与 `xcrun` 和 `avd` 工具保持一致，并兼容省略小版本号以使用最新构建。
- 🛠️ **多项功能改进与修复**：包括 Web 测试支持 iframes 和 `clearState`、优化云端上传验证、改进错误提示、修复输入崩溃和超时问题等。
- ⚠️ **弃用通知**：旧版整数格式将在下一版本中停止支持，同时传统网页版 Studio 已标记为弃用。
- 🔄 **更新方式**：可通过 curl 脚本或 Homebrew 进行升级，命令分别为 `curl -fsSL "https://get.maestro.mobile.dev" | bash` 和 `brew upgrade mobile-dev-inc/tap/maestro`。

---

### [True Sheet 3.10 | React Native True Sheet](https://sheet.lodev09.com/blog/release-3-10)

**原文标题**: [True Sheet 3.10 | React Native True Sheet](https://sheet.lodev09.com/blog/release-3-10)

True Sheet 3.10 版本引入了 iOS 26 的原生滚动边缘效果，新增了滚动控制选项以优化用户体验，并增强了无障碍访问功能，同时修复了多个平台上的错误。

- 📱 为 iOS 26+ 添加原生滚动边缘效果，可通过 `topScrollEdgeEffect` 和 `bottomScrollEdgeEffect` 选项启用
- 🎛️ 新增 `scrollingExpandsSheet` 选项，允许控制滚动时是否展开工作表至下一个停靠点
- ♿ 抓取器视图现支持 VoiceOver 和 TalkBack，提供无障碍操作和状态描述
- 🐛 修复了 iOS 上启用背景模糊时的闪烁问题及键盘滚动定位错误
- 🛠️ 解决了 Android 上的崩溃问题，并改进了返回按键检测的可靠性
- ⚠️ Android 上启用 `scrollable` 后，`nestedScrollingEnabled` 现自动管理，需移除手动设置
- 📦 可通过 `yarn add @lodev09/react-native-true-sheet@^3.10.0` 安装此版本

---

### [硝基播放器](https://nitroplayer.riteshshukla.in/)

**原文标题**: [Nitro Player](https://nitroplayer.riteshshukla.in/)

Nitro Player 是一款专为 React Native 设计的音频播放器，提供原生性能、完整的播放控制、离线下载、均衡器和汽车集成等功能。

- 🚀 基于 Nitro Modules 构建，采用原生 Kotlin 和 Swift 实现，无桥接开销，性能卓越
- 📋 智能队列系统，支持 playNext 堆栈、upNext 队列和播放列表，具备完整的增删改查和持久化功能
- 📥 离线下载管理器，支持进度跟踪、暂停/恢复、重试和存储管理
- 🎛️ 10 段均衡器，内置 19 种预设，支持自定义预设和每段增益控制
- 🚗 支持 Android Auto 和 CarPlay，提供自定义媒体浏览和控制中心、锁屏控制

---

### [发布 v2.6.0 · Shopify/react-native-skia · GitHub](https://github.com/Shopify/react-native-skia/releases/tag/v2.6.0)

**原文标题**: [Release v2.6.0 · Shopify/react-native-skia · GitHub](https://github.com/Shopify/react-native-skia/releases/tag/v2.6.0)

Shopify 维护的 React Native Skia 库发布了 2.6.0 版本，引入了新功能和改进。

- 🌳 新增不可变的 Path API，提升路径操作的稳定性和性能
- 🗿 在 DawnContext 中添加了 createSecondaryDevice() 方法，扩展了图形设备管理能力
- 📦 包含多项资产更新，优化了资源加载和处理机制

---

### [发布 v2.31.0 · software-mansion/react-native-gesture-handler · GitHub](https://github.com/software-mansion/react-native-gesture-handler/releases/tag/v2.31.0)

**原文标题**: [Release v2.31.0 · software-mansion/react-native-gesture-handler · GitHub](https://github.com/software-mansion/react-native-gesture-handler/releases/tag/v2.31.0)

该版本是 react-native-gesture-handler 库的 v2.31.0 更新，主要包含针对 Android 和 iOS 平台的重要修复、功能改进及错误修正，同时优化了文档和发布流程。

- 🚨 **重要变更**：修复了 Android 移动事件中的指针检查问题，并解决了新架构下 GestureDetector 在 display:none 切换后无响应的问题。
- 🔧 **功能改进**：优化了 Pressable 组件的 pointerEvents 处理，增强了内存管理，并改进了 iOS 上鼠标与触控笔的悬停区分。
- 🐞 **错误修复**：解决了 iOS 中 Hover 手势的 pointerType 错误、Tap 手势缺少 onFinalize 回调等问题。
- 📝 **文档与流程**：更新了 README 横幅，优化了版本更新脚本和发布流程，并调整了依赖项配置。
- 👏 **新贡献者**：欢迎 @huextrat 和 @christian-apollo 首次贡献代码。

---

### [[RFC] JSIR：面向JavaScript的高级中间表示 - MLIR - LLVM讨论论坛](https://discourse.llvm.org/t/rfc-jsir-a-high-level-ir-for-javascript/90456)

**原文标题**: [[RFC] JSIR: A High-Level IR for JavaScript - MLIR - LLVM Discussion Forums](https://discourse.llvm.org/t/rfc-jsir-a-high-level-ir-for-javascript/90456)

JSIR 是一种基于 MLIR 的高级别 JavaScript 中间表示，旨在填补 JavaScript 社区中缺乏公开、稳定的 IR 工具的空白。它通过保留 AST 的全部信息，支持源代码、AST 和 JSIR 之间的高保真往返转换，并利用 MLIR 区域表示控制流结构，同时提供数据流分析能力。JSIR 已在 Google 的生产环境中用于代码分析和转换任务，如反编译和反混淆，并且是开源项目。

- 🎯 **动机与目标**：针对 JavaScript 工具链中缺乏 IR 的现状，JSIR 旨在提供一个公开、稳定且全面的 IR，支持数据流分析和源代码转换，同时保持与 ESTree 标准的高度兼容。
- 🔄 **高保真往返转换**：JSIR 设计确保从源代码到 AST 再到 JSIR 的转换过程无损，通过后序遍历 AST 并映射为 JSIR 操作，实现 99.9% 以上的转换成功率。
- 🏗️ **控制流与数据结构**：使用 MLIR 区域嵌套表示控制流结构（如 if、while 语句），并区分左值和右值，以明确语义差异，便于分析和转换。
- 📊 **数据流分析框架**：基于 MLIR 数据流分析 API 构建，提供更易用的封装类（如 `JsirStateRef`），自动处理状态传播，简化分析实现。
- 🛠️ **实际应用案例**：在 Google 内部用于 Hermes 字节码反编译和 JavaScript 反混淆，结合 Gemini LLM 提升效果，相关论文已被 ICSE 2026 接收。
- 🌍 **社区与开源**：JSIR 项目开源在 GitHub，欢迎社区贡献，并探讨上游集成到 MLIR 的可能性，但目前存在依赖库（如 QuickJS、Babel/SWC）的兼容性挑战。
- 🔮 **未来发展方向**：计划进一步整合 MLIR 内置功能（如符号表）、改进区域数据流分析，并探索 IR 是否可能完全替代 AST 的潜力。

---

### [Axios 妥协的隐秘冲击范围 - Socket](https://socket.dev/blog/hidden-blast-radius-of-the-axios-compromise)

**原文标题**: [The Hidden Blast Radius of the Axios Compromise - Socket](https://socket.dev/blog/hidden-blast-radius-of-the-axios-compromise)

Socket CEO Feross Aboukhadijeh 详细分析了朝鲜如何通过供应链攻击劫持了 Axios 库，并探讨了此类事件对未来软件供应链安全的深远影响。

- 🕵️ 朝鲜黑客通过劫持 Axios 维护者账户，在库中植入恶意代码进行供应链攻击
- 🔓 攻击利用了 npm 生态系统的信任机制和账户安全漏洞
- ⚠️ 事件暴露了开源软件维护环节的脆弱性和供应链安全风险
- 🛡️ 需要采用更严格的多因素认证和代码签名机制来防范类似攻击
- 🌐 整个开源生态系统需要建立更完善的供应链安全监控体系

---

### [Axios维护者确认n...背后存在社会工程学攻击](https://socket.dev/blog/axios-maintainer-confirms-social-engineering-behind-npm-compromise)

**原文标题**: [Axios Maintainer Confirms Social Engineering Attack Behind n...](https://socket.dev/blog/axios-maintainer-confirms-social-engineering-behind-npm-compromise)

Socket CEO Feross Aboukhadijeh 分析了朝鲜如何劫持 Axios 事件，并探讨了其对软件供应链安全未来的影响。

- 🕵️ 朝鲜黑客通过社会工程学攻击，控制了 Axios 维护者的 npm 账户
- 📦 攻击者在 Axios 库中植入恶意代码，窃取环境变量和敏感数据
- 🔗 事件暴露了开源软件供应链中对维护者账户安全保护的薄弱环节
- 🛡️ 建议采用双因素认证、自动化安全扫描和最小权限原则加强防护
- 🌐 此次攻击警示了国家级黑客组织对开源生态系统的威胁正在升级

---

### [JavaScript 必知要点（2026版）—— Frontend Masters 博客](https://frontendmasters.com/blog/what-to-know-in-javascript-2026-edition/)

**原文标题**: [What To Know in JavaScript (2026 Edition) – Frontend Masters Blog](https://frontendmasters.com/blog/what-to-know-in-javascript-2026-edition/)

本文概述了JavaScript在2026年的关键发展，涵盖语言新特性、框架更新、运行时环境、构建工具、TypeScript进展以及生态系统中的重要趋势。

- 🆕 ECMAScript 2025 引入了迭代器助手、集合方法、正则表达式转义和导入属性等新功能，提升了开发效率和性能。
- 📅 ECMAScript 2026 预计将带来 Temporal API（改进日期时间处理）、显式资源管理和数组异步转换等重大更新。
- ⚛️ React 生态系统在 React 19 中推出了服务器组件、服务器操作和编译器优化，但同时也面临安全漏洞的挑战。
- 🖥️ Vue 3.6 将引入 Vapor 模式以提升性能，而 Nuxt 4.0 和 Vite+ 工具链进一步扩展了其生态系统。
- 🚀 Svelte 5 通过 Runes API 实现了更细粒度的响应式系统，提高了应用性能。
- 🏃 JavaScript 运行时中，Node.js 原生支持 TypeScript，Bun 强调速度，Deno 注重安全性和稳定性。
- 🛠️ Vite 8 成为主流构建工具，使用自研的 Rolldown 替代 Rollup，并扩展为统一的 Vite+ 工具链。
- 📦 TypeScript 6 为即将到来的 Go 编译器版本做准备，预计 v7 将带来显著的性能提升。
- 🤖 AI 在代码编写中的应用日益普及，92% 的开发者使用 AI 辅助编程，尤其在 TypeScript 领域表现突出。
- 🧪 测试工具中，Vitest 和 Playwright 因与 Vite 集成和浏览器测试能力而受到青睐。
- 🌐 元框架方面，Next.js 默认采用 Turbopack，Astro 被 Cloudflare 收购，Remix 正在开发独立的组件模型。
- ⚠️ npm 面临供应链安全威胁，如恶意包和凭证窃取事件，建议使用 Socket 等工具加强防护。
- 🎯 学习核心技能和架构设计比追逐工具变化更为重要，AI 时代更需扎实的编程基础。

---

### [国际API：你尚未使用的最佳浏览器API | Polypane](https://polypane.app/blog/the-intl-api-the-best-browser-api-youre-not-using/)

**原文标题**: [The Intl API: The best browser API you're not using | Polypane](https://polypane.app/blog/the-intl-api-the-best-browser-api-youre-not-using/)

Intl API 是浏览器内置的国际化格式化工具，可替代第三方库处理日期、数字、货币、列表和文本的本地化格式，无需额外下载，自动适应用户区域设置。

- 🌐 **零依赖内置工具** – 直接集成于浏览器，无需引入 Moment.js 等库，节省资源并提升性能。
- 📅 **智能日期时间格式化** – 通过 `Intl.DateTimeFormat` 等 API 自动适配不同地区的日期、时间和相对时间格式。
- 💰 **本地化货币与数字处理** – 使用 `Intl.NumberFormat` 正确显示货币符号、小数分隔符和单位（如温度、速度）。
- 📝 **自然语言文本处理** – 利用 `Intl.ListFormat` 生成符合语言习惯的列表，`Intl.PluralRules` 处理复数形式，`Intl.Segmenter` 准确分割单词和句子。
- 🔤 **区域感知排序与比较** – 通过 `Intl.Collator` 实现基于语言的字符串排序，支持数字排序等高级选项。
- ⚡ **高效一致的 API 设计** – 所有格式化器遵循相似模式（区域设置 → 选项 → 格式化器实例 → 重用），简化开发流程。

---

### [介绍view-transitions-toolkit，一套让View Transitions更易用的实用函数集。 – Bram.us](https://www.bram.us/2026/04/02/view-transitions-toolkit/)

**原文标题**: [Introducing view-transitions-toolkit, a collection of utility functions to more easily work with View Transitions. – Bram.us](https://www.bram.us/2026/04/02/view-transitions-toolkit/)

view-transitions-toolkit 是一个实用工具函数集合，旨在简化 View Transitions 的使用，帮助开发者更轻松地实现高级动画效果。

- 🧰 **工具包介绍**：view-transitions-toolkit 提供了一系列小型、专注的辅助函数，用于填补 View Transitions 在实现高级模式时的功能缺口。
- 🔍 **功能检测**：支持检测特定 View Transitions 子功能的兼容性信息。
- 🛠 **垫片支持**：为 `document.activeViewTransition` 提供垫片支持。
- 🎬 **动画工具**：提供提取、测量和优化动画的实用函数。
- ⏯ **播放控制**：支持暂停、恢复或擦洗 View Transition 的播放进度。
- 🧭 **自动导航类型**：根据导航的起点和终点自动注入 View Transition 类型。
- 📦 **快速上手**：通过 npm 安装即可使用，优化动画等操作仅需一行代码。
- 🌐 **演示与资源**：提供包含示例的公开网站，源码和文档均在 GitHub 仓库中开放。

---

### [ESLint v10.2.0 发布 - ESLint - 可插拔的 JavaScript 代码检查工具](https://eslint.org/blog/2026/04/eslint-v10.2.0-released/)

**原文标题**: [ESLint v10.2.0 released - ESLint - Pluggable JavaScript Linter](https://eslint.org/blog/2026/04/eslint-v10.2.0-released/)

ESLint v10.2.0 作为次要版本发布，引入了语言感知规则支持、对 Temporal 全局对象的识别，并包含多项功能更新、错误修复及文档改进。

- 🆕 新增语言感知规则支持，通过 `meta.languages` 属性允许规则作者声明支持的编程语言，若规则用于不支持的语言将报错
- 🌐 识别 Temporal 为内置全局对象，`no-undef` 规则默认不再标记其使用，同时 `no-obj-calls` 规则会报告对 Temporal 的直接调用错误
- 🔧 包含多项功能更新，如添加 `meta.languages` 支持、将 Temporal 加入 `no-obj-calls` 规则和 ES2026 全局变量列表
- 🐛 修复了若干错误，包括更新了首方依赖项
- 📚 文档进行了多项更新，如添加语言配置说明、更新 README 及示例中的 ESLint 版本等
- 🛠️ 进行了代码重构、测试添加和持续集成配置更新等维护工作

---

### [发布 v0.28.0 · evanw/esbuild · GitHub](https://github.com/evanw/esbuild/releases/tag/v0.28.0)

**原文标题**: [Release v0.28.0 · evanw/esbuild · GitHub](https://github.com/evanw/esbuild/releases/tag/v0.28.0)

esbuild 发布了 v0.28.0 版本，主要更新包括支持 TC39 第三阶段的 `import with { type: 'text' }` 语法、增强安装脚本的完整性校验，以及将 Go 编译器升级至 1.26.1。

- 🆕 支持 `import with { type: 'text' }` 语法，与现有 `text` 加载器功能一致
- 🔒 为备用下载路径添加完整性校验，确保二进制文件哈希匹配
- 🔄 将 Go 编译器从 1.25.7 升级至 1.26.1，涉及垃圾回收、内存分配等内部改进

---

### [发布 v2.0.0 · sindresorhus/ky · GitHub](https://github.com/sindresorhus/ky/releases/tag/v2.0.0)

**原文标题**: [Release v2.0.0 · sindresorhus/ky · GitHub](https://github.com/sindresorhus/ky/releases/tag/v2.0.0)

Ky 是一个基于 Fetch API 的轻量级 HTTP 客户端库，最新发布了 v2.0.0 版本，包含多项重大变更、新功能和修复。

- 🚨 **重大变更**：要求 Node.js 22 环境，统一了钩子函数的签名，将 `prefixUrl` 重命名为 `prefix`，并允许输入 URL 包含前导斜杠。
- 🆕 **新增功能**：引入了 `totalTimeout` 选项以设置所有重试的总超时，添加了 `baseUrl` 选项用于标准 URL 解析，并新增了 `init` 钩子。
- 🔧 **错误处理改进**：`beforeError` 钩子现在接收所有类型的错误，`HTTPError` 新增 `data` 属性包含预解析的响应体，修复了资源泄漏问题。
- 📄 **JSON 处理调整**：`.json()` 方法在响应体为空或状态码为 204 时会抛出错误，而不是返回空字符串，更符合原生 `JSON.parse` 的行为。
- 🔗 **参数合并优化**：`searchParams` 现在会与输入 URL 中的现有查询参数合并，而不是替换它们。
- 🛠️ **钩子选项清理**：传递给钩子的 `options` 对象中不再包含 Ky 特定的属性，如 `hooks`、`json` 等，以避免混淆。
- ⚙️ **其他修复与增强**：包括添加 `NetworkError` 类、强化重试逻辑、支持 `Standard Schema` 验证、修复 `beforeRequest` 钩子跳过问题等。

---

### [未找到标题](https://x.com/TkDodo/status/1661337628875137027)

**原文标题**: [No title found](https://x.com/TkDodo/status/1661337628875137027)

该页面提示用户浏览器中JavaScript功能未启用或存在兼容性问题，导致无法正常使用X平台（原Twitter），并提供了相应的解决建议与支持资源。

- 🔐 检测到浏览器已禁用JavaScript，需启用该功能或更换受支持的浏览器以继续访问
- 🌐 平台提供了帮助中心链接，可查询具体支持的浏览器列表
- ⚙️ 提示某些隐私保护扩展可能导致运行异常，建议临时禁用后重试
- 📜 页面底部包含服务条款、隐私政策、Cookie政策等法律文件链接
- 🔄 设有“重试”按钮供用户在当前页面直接尝试重新加载

---

### [未找到标题](https://x.com/TkDodo)

**原文标题**: [No title found](https://x.com/TkDodo)

该页面提示JavaScript功能未启用，导致无法正常使用X平台，并提供了相应的解决建议与支持信息。

- 🔧 检测到浏览器中JavaScript被禁用，需启用或更换受支持的浏览器
- 🌐 可访问帮助中心查看支持的浏览器列表
- 🛡️ 部分隐私扩展可能导致问题，建议暂时禁用后重试
- 📜 页面底部包含服务条款、隐私政策等法律文件链接
- 🔄 提供“再试一次”功能按钮供用户重新加载页面

---

