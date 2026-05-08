### [React 项目实战 — 坦纳·林斯利](https://tannerlinsley.com/posts/projecting-react)

**原文标题**: [Projecting React â Tanner Linsley](https://tannerlinsley.com/posts/projecting-react)

### 概述总结
作者通过AI辅助构建了一个精简版React运行时（@tanstack/redact），将React核心API投影为仅7-9KB的定制化版本，在保持兼容性的同时实现了80-85%的体积缩减和2倍性能提升，并指出在AI辅助下，按需定制依赖已成为可行且负责任的选择。

- 🚀 **核心创新**：将React公共API视为“基表”，通过AI代理生成仅包含TanStack Start所需功能的精简投影，而非传统fork
- 📦 **惊人压缩**：完整投影仅9.39KB（gzip），最小核心7.08KB，相比React 19的60KB减少80-85%
- ⚡ **性能飞跃**：客户端导航速度提升2.24倍（34.9Hz→78.1Hz），SSR请求处理提升3倍（48Hz→168Hz）
- 🔧 **模块化设计**：8个可开关功能（portal/context/suspense等），通过Vite插件在构建时彻底移除未用代码
- 🧪 **实战验证**：已在tannerlinsley.com和tanstack.com上线，LCP降低12-18%，JS传输量减少33%
- 🤖 **AI开发效率**：核心功能1天完成开发，后续仅需描述生产环境bug即可获得即时修复
- ⚠️ **已知局限**：RSC密集型页面LCP增加8-43%，但仍在Core Web Vitals“良好”阈值内
- 🎯 **明确立场**：不进行市场推广，不纳入TanStack Start主线，仅作为个人实验项目
- 💡 **行业启示**：类比Linux发行版和歌曲混音，AI使“按需投影依赖”成为新常态，默认使用上游不再是最优解

---

### [细致AI - 无需编写测试的自动化前端测试](https://www.meticulous.ai/?utm_source=reactstatus&utm_medium=newsletter&utm_campaign=26q2&utm_content=primary)

**原文标题**: [Meticulous AI - Automated Frontend Testing Without Writing Tests](https://www.meticulous.ai/?utm_source=reactstatus&utm_medium=newsletter&utm_campaign=26q2&utm_content=primary)

Meticulous AI 是一款革命性的自动化测试工具，通过AI引擎自动生成并维护测试套件，无需手动编写或维护测试代码，支持复杂代码库，已获超过100家组织信赖。

- 🚀 **零维护自动化测试**：AI自动生成端到端测试，覆盖所有用户流程和边缘情况，测试随应用演化而自动更新
- 🔍 **无flake确定性引擎**：基于Chromium构建的确定性调度引擎，彻底消除测试不稳定问题，执行速度极快
- ⏱️ **超快并行测试**：通过计算集群并行测试数千个屏幕，结果在120秒内返回
- 🛡️ **安全无副作用**：自动模拟后端响应，无需特殊测试账号或模拟数据，避免假阳性
- 🔌 **简单集成**：只需添加脚本标签即可记录开发、预览环境交互，支持NextJS/React/Vue/Angular等主流框架
- 📈 **提升迭代速度**：持续添加新测试并移除过时测试，确保测试套件始终完整且最新
- 🤝 **灵活使用**：可补充或完全替代现有测试套件，已获Dropbox、Notion等企业验证
- 🎯 **PR预检**：在合并前即可查看代码变更对用户工作流的影响，避免回归问题

---

### [Next.js 2026年5月安全更新 - Vercel](https://vercel.com/changelog/next-js-may-2026-security-release)

**原文标题**: [Next.js May 2026 security release - Vercel](https://vercel.com/changelog/next-js-may-2026-security-release)

Next.js 发布安全更新，修复13个漏洞，涵盖拒绝服务、中间件与代理绕过、服务端请求伪造、缓存投毒和跨站脚本攻击。其中一个漏洞涉及上游React Server Components（CVE-2026-23870）。所有受影响用户应立即升级。

- 🔒 中间件和代理绕过：影响使用middleware.js或proxy.js进行授权的应用，包括App Router段预取URL绕过、Pages Router i18n默认语言路径绕过等4个高危漏洞
- 🛑 拒绝服务：影响使用Server Functions、Partial Prerendering或Image Optimization API的应用，包括React Server Components DoS（CVE-2026-23870）和连接耗尽攻击
- 🌐 服务端请求伪造：影响处理WebSocket升级请求的应用，存在SSRF高危漏洞
- 🧹 缓存投毒：影响在React Server Component响应前有缓存层的应用，包括RSC响应缓存投毒和缓存破坏碰撞
- ⚠️ 跨站脚本攻击：影响使用CSP nonces或beforeInteractive脚本处理不可信输入的应用
- 📦 受影响版本：Next.js 13.x/14.x/15.x/16.x，需升级至15.5.18或16.2.6；react-server-dom-* 19.0.x/19.1.x/19.2.x，需升级至对应补丁版本
- 🚀 修复版本：Next.js 15.5.18和16.2.6；React 19.0.6、19.1.7和19.2.6（针对react-server-dom-*包）
- ⚡ 升级建议：立即升级，补丁是唯一完整缓解措施，WAF无法可靠拦截这些漏洞

---

### [WAF与框架适配器针对React和Next.js漏洞的缓解措施 · 更新日志](https://developers.cloudflare.com/changelog/post/2026-05-06-react-nextjs-vulnerabilities/)

**原文标题**: [WAF and framework adapter mitigations for React and Next.js vulnerabilities Â· Changelog](https://developers.cloudflare.com/changelog/post/2026-05-06-react-nextjs-vulnerabilities/)

Cloudflare 发布了针对 React 和 Next.js 安全漏洞的 WAF 规则及框架适配器更新，强烈建议用户立即更新应用和依赖。

- 🛡️ **WAF 规则已部署**：针对拒绝服务漏洞（CVE-2025-55184 和 CVE-2026-23864）的规则已默认启用，并覆盖新漏洞 CVE-2026-23870，所有使用 Cloudflare 托管规则集的用户（包括免费计划）均受保护。
- 🔍 **正在调查其他漏洞**：Cloudflare 正在评估是否能为三个高危漏洞（CVE-2026-23870、GHSA-267c-6grr-h53f、GHSA-mg66-mrh9-m8jx）安全部署额外 WAF 规则，但部分漏洞无法通过 WAF 完全阻止。
- ⚠️ **无法完全依赖 WAF**：多个漏洞（如中间件绕过、SSRF、XSS 等）无法通过 WAF 规则安全缓解，强烈建议用户更新应用版本。
- 📦 **React 和 Next.js 补丁版本**：已发布修复版本，包括 React（19.0.6、19.1.7、19.2.6）和 Next.js（15.5.16、16.2.5）。
- 🔧 **框架适配器更新**：Vinext 插件不受影响，但要求 React 19.2.6 或更高版本；OpenNext 适配器已更新以增强防护，用户需更新 Next.js 版本。
- 📋 **漏洞摘要**：涵盖 12 个漏洞，严重程度从低到高，包括拒绝服务、中间件绕过、SSRF、XSS 和缓存投毒等，WAF 覆盖状态各异。

---

### [React 服务端组件中的拒绝服务漏洞 · 公告 · facebook/react · GitHub](https://github.com/facebook/react/security/advisories/GHSA-rv78-f8rc-xrxh)

**原文标题**: [Denial of Service Vulnerability in React Server Components · Advisory · facebook/react · GitHub](https://github.com/facebook/react/security/advisories/GHSA-rv78-f8rc-xrxh)

React Server Components 存在拒绝服务漏洞，影响多个版本，需立即更新。

- 🔴 漏洞影响 `react-server-dom-webpack`、`react-server-dom-parcel` 和 `react-server-dom-turbopack` 的 19.0.0 至 19.2.5 版本
- 🚨 攻击者可通过发送特制 HTTP 请求到服务器函数端点，触发内存溢出或 CPU 过度使用，导致服务不可用
- 🛠️ 修复版本为 19.0.6、19.1.7 和 19.2.6，建议立即升级
- ✅ 未使用服务器的 React 应用不受影响，未使用支持 React Server Components 的框架或打包器的应用也不受影响
- 📊 漏洞严重性为高（CVSS 评分 7.5），攻击向量为网络，复杂度低，无需权限或用户交互
- 🆔 CVE 编号为 CVE-2026-23870，弱点为 CWE-400（资源消耗失控）和 CWE-770（无限制资源分配）

---

### [Expo SDK 56 测试版现已发布 - Expo 更新日志](https://expo.dev/changelog/sdk-56-beta)

**原文标题**: [Expo SDK 56 Beta is now available - Expo Changelog](https://expo.dev/changelog/sdk-56-beta)

SDK 56 测试版现已推出，为期约两周，供开发者测试并确保无回归问题。该版本包含多项重大更新，如 Expo UI 稳定、性能优化和新 API。

- 🚀 SDK 56 测试版开始，持续约两周，期间会持续发布修复和改进。
- 🎨 Expo UI 现已稳定，包含通用组件、稳定原生 API 和社区组件替代品，默认集成到新项目中。
- ⚡ 性能提升：iOS 预编译 XCFrameworks 加速构建，Android 使用 Kotlin 编译器插件实现 40% 更快的冷启动，iOS 原生模块采用新 JSI 层减少调用开销。
- 📱 新 API 稳定：日历、通讯录和媒体库 API 重新设计为面向对象，iOS 小组件功能正式推出。
- 🛠️ 开发者工具增强：内联模块支持直接在项目中定义原生模块，`create-expo-module` 重写，Expo CLI 性能改进，TypeScript 6 支持。
- 🧭 Expo Router 不再依赖 React Navigation，新增工具栏、堆栈 v5 实验性支持和 Web 流式 SSR。
- 🔧 其他更新：`expo-file-system` 功能增强，状态栏和导航栏 API 统一，`expo/fetch` 成为默认实现，多项工具版本升级和弃用通知。

---

### [介绍deepsec：用于发现代码库漏洞的安全工具 - Vercel](https://vercel.com/blog/introducing-deepsec-find-and-fix-vulnerabilities-in-your-code-base)

**原文标题**: [Introducing deepsec: The security harness for finding vulnerabilities in your codebase - Vercel](https://vercel.com/blog/introducing-deepsec-find-and-fix-vulnerabilities-in-your-code-base)

概述总结  
- 🔓 开源发布 deepsec：一款基于编码代理的安全检测工具，可在本地基础设施运行，发现大型代码库中的隐蔽问题。  
- 💻 本地运行：无需云服务，支持使用现有 Claude 或 Codex 订阅进行推理。  
- ⚡ 并行扫描：支持可选扩展至 Vercel Sandboxes，实现 1000+ 并发沙盒，加速大型仓库扫描。  
- 🧠 核心架构：使用 Opus 4.7 和 GPT 5.5 进行静态分析、代理调查、重新验证和丰富输出，生成可操作的安全发现。  
- ✅ 真实案例：在 Dub.co 和 Vercel 代码库中有效识别认证漏洞等关键问题，误报率约 10-20%。  
- 🔧 插件系统：支持自定义扫描器，可适配不同代码库的认证模型或数据层。  
- 🚀 快速上手：运行 `npx deepsec init` 即可配置，无需特殊“网络模型”，标准模型即可工作。  
- 📢 反馈开放：项目仍在早期开发，欢迎在 GitHub 上贡献和反馈。

---

### [CHANGELOG.md | React Router](https://reactrouter.com/changelog#v7150)

**原文标题**: [CHANGELOG.md  | React Router](https://reactrouter.com/changelog#v7150)

React Router 是一个功能强大的路由库，它提供了多种模式（框架模式、数据模式、声明式模式）和丰富的 API，用于构建单页应用（SPA）和全栈应用。其核心功能包括路由定义、数据加载、表单处理、导航、错误边界、代码分割等。该文档详细记录了从 v6.0.0 到 v7.15.0 的版本更新日志，涵盖了新功能、稳定性改进、错误修复和安全补丁，并提供了从 Remix 和 React Router v6 升级的指南。

- 🚀 **核心功能**：提供路由定义、数据加载（loader）、表单操作（action）、导航（Link, NavLink）和错误处理（ErrorBoundary）等核心 API。
- 🧩 **多种模式**：支持框架模式（全栈）、数据模式（SPA）和声明式模式，适应不同应用场景。
- 🗺️ **路由配置**：通过 `routes.ts` 文件或文件系统约定（`@react-router/fs-routes`）定义路由，支持嵌套路由、动态参数和可选路径段。
- 🔒 **安全更新**：多个版本修复了 CSRF、XSS 和开放重定向等安全漏洞，增强了应用的安全性。
- ⚡ **性能优化**：引入了懒加载路由（`route.lazy`）、路由匹配优化和代码分割（`future.v8_splitRouteModules`）来提升性能。
- 🛠️ **开发者体验**：提供类型安全的 `href` 工具、自动类型生成、未来标志（Future Flags）和 Vite 集成，简化开发流程。
- 🌟 **新特性**：支持视图过渡（View Transitions）、URL 掩码（URL Masking）、中间件（Middleware）和 React Server Components（RSC，不稳定）。
- 📚 **版本迭代**：从 v6.0.0 到 v7.15.0，持续引入新功能、稳定性改进和错误修复，并提供了详细的升级指南。

---

### [从React到原生Web的nanotags迁移：节省了100KB——火星编年史，邪恶火星人团队博客](https://evilmartians.com/chronicles/from-react-to-native-web-with-nanotags-a-migration-that-saved-100kb)

**原文标题**: [From React to native web with nanotags: a migration that saved 100 KB—Martian Chronicles, Evil Martians’ team blog](https://evilmartians.com/chronicles/from-react-to-native-web-with-nanotags-a-migration-that-saved-100kb)

### 概述总结
- 📉 将营销站点从React迁移到原生Web组件，节省了100KB的JavaScript体积，且未丢失任何功能。
- 🧩 使用nanotags库简化了自定义元素的编写，提供了类型安全、响应式属性和自动清理功能。
- 🌐 强调Web平台原生组件（Custom Elements）的优势，无需额外框架运行时，适合静态内容为主的站点。
- ♿ 通过W3C ARIA指南和附件模式实现无障碍功能，未出现退化，部分交互甚至更优。
- 🚀 结合Astro和nanostores，总运行时仅约3KB，远低于React或Lit等框架。
- 📦 模块化设计，核心库小于2.5KB，按需导入额外功能，避免不必要的体积开销。
- 🔧 迁移过程快速，因为大部分内容已是静态HTML，仅需对交互部分进行轻量级绑定。

---

### [免费试用Tiger Cloud：$1,000信用额度 | Tiger Data](https://www.tigerdata.com/go/trial?utm_source=content-syndication&utm_medium=referral&utm_campaign=react-status-newsletter)

**原文标题**: [Try Tiger Cloud Free: $1,000 Credit | Tiger Data](https://www.tigerdata.com/go/trial?utm_source=content-syndication&utm_medium=referral&utm_campaign=react-status-newsletter)

概述总结  
- 🚀 注册即获$1,000云服务额度，30天有效，无需信用卡  
- ⚡️ 读写分离支持最多10个节点，SSD/S3分层存储实现无限容量与低成本  
- 💰 计算与存储分离，独立扩展，避免为闲置资源付费  
- 🔒 多可用区集群自动故障切换，支持时间点恢复与跨区域备份  
- 🛡️ 符合SOC 2、HIPAA、GDPR标准，提供加密、SSO、RBAC和审计日志  
- 📊 查询钻取与仪表盘深度监控，集成CloudWatch、Datadog、Prometheus  
- ⏱️ 分钟级数据库部署，支持SQL、CLI、Terraform、Cursor、Claude Code管理  
- 🤝 企业级SLA保障、区域数据隔离、24/7专家支持与合规认证

---

### [React 迈阿密 2026](https://brookslybrand.com/posts/react-miami-2026.html)

**原文标题**: [React Miami 2026](https://brookslybrand.com/posts/react-miami-2026.html)

### 概述总结
作者参加了2026年React Miami大会，观察到React社区兴趣下降、AI影响深远、React Router和Remix项目面临挑战与机遇，同时表达了对行业未来的乐观态度。

- 🎉 **大会组织**：React Miami由Michelle、Rebecca和Gabe成功举办五年，Michelle今年卸任，组织者备受尊敬，大会兼具专业性与社交性。
- 📉 **React兴趣低迷**：新功能（如RSC、React Compiler）关注度创新低，原因包括AI编码工具普及和React分裂为“旧版稳定”与“新版复杂”两种形态。
- 🤖 **AI情绪复杂**：开发者对AI既恐惧又兴奋，但作者认为AI不会取代工程师，反而会创造更多机会；建议忽略极端观点，专注学习工程思维。
- 🔧 **React Router现状**：项目已澄清与Remix的混淆，v8即将发布，支持RSC和SPA，周下载量超5000万，采用开放治理模式。
- 🚀 **Remix前景**：新版本即将推出，优势包括更小JS体积、AI友好、真正全栈、单一依赖；但需重新定位以激发开发者兴趣。
- 💡 **行业反思**：技术迭代加速，但“思考能力”比以往更重要；开发者应保持学习，避免被社交媒体误导。

---

### [谁拥有这棵树？RSC作为协议而非架构 | TanStack博客](https://tanstack.com/blog/who-owns-the-tree)

**原文标题**: [Who Owns the Tree? RSC as a Protocol, Not an Architecture | TanStack Blog](https://tanstack.com/blog/who-owns-the-tree)

TanStack Start 将 RSC 视为一种协议而非固定架构，支持服务器和客户端两种组件组合模型，让开发者根据需求灵活选择。

- 🧩 **RSC 是协议，不是架构**：RSC 本质是序列化 React 输出的协议，服务器拥有树（传统模型）和客户端拥有树（通过 Composite Components）都是其有效用法。
- 🔄 **双向组合模型**：服务器拥有树用 `'use client'` 插入交互；客户端拥有树用 Composite Components 插入服务器渲染的 UI，两者由同一协议驱动。
- 🎯 **实际案例：仪表盘**：客户端控制大部分 UI（标签、过滤器），只需一处服务器渲染图表时，Composite Components 可避免将整个路由转为服务器优先架构。
- ⚖️ **两种模型可相互转换**：服务器模型推高 `'use client'` 边界可变为 SPA；客户端模型在高层渲染服务器组件可模拟服务器渲染页面。
- 🛠️ **大多数框架只支持一半**：标准 RSC 模型假设服务器拥有树，但客户端拥有树场景下（如从 `useQuery` 获取服务器组件）缺乏原生支持，Composite Components 填补了这一空白。
- 🚫 **不提供缓存指令**：因 TanStack Start 支持多种平台（Cloudflare、Node、Bun 等），无法假设统一持久层，故采用透明方式：服务器函数返回 Flight 流字节，由开发者控制各层缓存（React.cache、Redis、HTTP 缓存等）。
- 💡 **核心哲学**：RSC 是强大原语而非银弹，路由、数据获取、缓存等已有更佳工具，开发者应选择最适合的组合方式。

---

### [在React Router中理清对话框——编程不易——](https://programmingarehard.com/2026/05/06/react-router-dialogs.html/)

**原文标题**: [Untangling dialogs in React Router — ProgrammingAreHard — ](https://programmingarehard.com/2026/05/06/react-router-dialogs.html/)

以下是對這篇文章的摘要，重點說明如何使用 React Router 7 實現無 useEffect 的模態對話框，涵蓋路由設計、資料載入、錯誤處理、動畫及使用者回饋。

總覽摘要
本文介紹如何利用 React Router 7 的巢狀路由、View Transitions 及 Flash Session 等功能，在不使用 useEffect 的情況下實現功能完整的模態對話框，並解決動畫、錯誤處理與使用者回饋等常見問題。

- 🚀 **使用巢狀路由取代單一元件內的對話框**：將安裝與卸載模型的功能獨立為子路由（如 `models.install.tsx` 和 `models.uninstall.$name.tsx`），使程式碼結構更清晰，職責單一。
- 🔗 **利用 Link 取代 fetcher 進行導航**：透過 `Link` 元件搭配 `unstable_defaultShouldRevalidate` 和 `preventScrollReset` 屬性，避免不必要的重新驗證與頁面滾動，提升效能與使用者體驗。
- 🗑️ **透過路由 action 處理提交與重導向**：在對話框路由的 action 中直接處理表單提交，成功後使用 `throw redirect` 返回列表頁，無需額外的 useState 或 useEffect 來控制對話框開關。
- 🎨 **使用 View Transitions 實現退出動畫**：為對話框的 overlay 和 content 設定 `viewTransitionName`，並撰寫 CSS 關鍵影格，讓對話框關閉時有平滑的淡出縮放效果，解決元件立即移除的動畫問題。
- 📬 **透過 Flash Session 傳遞成功訊息**：在 action 中將成功訊息寫入 cookie session，並在父路由的 clientLoader 中讀取並觸發 toast，避免在元件中使用 useEffect 處理副作用。
- ⚠️ **錯誤處理的權衡**：若需避免動畫因錯誤而抖動，可選擇在 action 中回傳資料而非 redirect，並在元件中使用 useEffect 監聽成功狀態後再觸發導航動畫，這是少數需要妥協的情境。
- 🧩 **專案設定與工具**：使用 React Router 框架模式、Tailwind CSS 和 shadcn 元件，搭配 Ollama 作為示範應用，管理本地 LLM 模型的安裝與卸載。

---

### [MapLibre React Native](https://maplibre.org/maplibre-react-native/)

**原文标题**: [MapLibre React Native](https://maplibre.org/maplibre-react-native/)

概述摘要：这是一个使用MapLibre React Native库在Android和iOS平台上显示地图的代码示例。

- 📱 使用MapLibre React Native库的Map组件
- 🗺️ 通过mapStyle属性指定地图样式为"https://demotiles.maplibre.org/style.json"
- 🔄 代码同时适用于Android和iOS平台

---

### [2026年5月 - 包导入与目标别名 - shadcn/ui](https://ui.shadcn.com/docs/changelog/2026-05-package-imports-target-aliases)

**原文标题**: [May 2026 - Package Imports and Target Aliases - shadcn/ui](https://ui.shadcn.com/docs/changelog/2026-05-package-imports-target-aliases)

以下是您提供的文本内容的摘要：

shadcn/ui 新增了包导入和目标别名功能，以提升组件安装和导入的灵活性。

- 📦 **包导入支持**：CLI 现在支持 `package.json` 中的 `#imports` 来安装组件和重写导入，替代了仅依赖 `tsconfig.json` 的路径配置。
- 🎯 **目标别名功能**：注册表项可在 `files[].target` 中使用别名（如 `@ui/ai`），将文件安装到用户配置的 shadcn 目录下。
- 🔧 **配置示例**：提供了 `package.json` 和 `components.json` 的配置示例，展示如何设置别名和根路径。
- 🏢 **Monorepo 兼容**：包导入在 monorepo 中也能工作，支持本地文件使用包导入，共享 UI 文件从工作区包导出导入。
- 🚀 **版本更新**：这些功能在 `shadcn@4.7.0` 中引入，增强了 CLI 和注册表的能力。

---

### [React日期选择器组件 | React DayPicker](https://daypicker.dev/)

**原文标题**: [Date Picker Component for React | React DayPicker](https://daypicker.dev/)

React DayPicker 是一个用于创建日期选择器、日历和日期输入框的 React 组件，功能丰富且易于定制。

- 🛠️ 提供大量自定义属性，可灵活配置日历外观和行为
- 🎨 极简设计，易于通过 CSS 或任何框架进行样式化
- 📅 支持单日、多日、日期范围或自定义选择模式
- 🌍 可本地化为任何语言并支持时区
- 🌐 兼容 ISO 8601、波斯历、伊斯兰历、佛历、埃塞俄比亚历、希伯来历和广播日历
- 🦮 符合 WCAG 2.1 AA 无障碍标准
- ⚙️ 组件可定制，能扩展渲染元素
- 🔤 与输入字段轻松集成
- 📝 使用 TypeScript 编写，编译为 CommonJS 和 ESM，依赖 date-fns 处理日期
- 🚀 兼容 React 16.8 及以上版本
- 💬 提供讨论论坛和问题报告渠道，支持社区反馈
- 🎗️ 通过 GitHub Sponsors 接受赞助以维持项目发展
- 📄 基于 MIT 许可证发布

---

### [GitHub - remarkablemark/html-react-parser: 📝 HTML 转 React 解析器。](https://github.com/remarkablemark/html-react-parser)

**原文标题**: [GitHub - remarkablemark/html-react-parser: 📝 HTML to React parser. · GitHub](https://github.com/remarkablemark/html-react-parser)

html-react-parser 是一个用于将 HTML 字符串转换为 React 元素的解析器，支持服务端（Node.js）和客户端（浏览器）使用。

- 📦 **安装方式多样**：支持 npm、yarn 和 CDN 安装，灵活适配不同项目需求。
- 🔄 **核心功能强大**：通过 `parse()` 函数将 HTML 转换为 React 元素，支持单个、多个及嵌套元素的解析。
- 🛠️ **丰富的自定义选项**：提供 `replace` 选项替换元素、`transform` 选项转换元素、`library` 选项指定 UI 库（如 Preact）。
- 🔧 **高级用法灵活**：支持 `replace` 元素及其子元素、转换 DOM 属性为 React props、移除元素，以及通过 `trim` 控制空白字符。
- 🌐 **跨平台兼容**：支持服务端渲染（SSR），并可通过 `htmlparser2` 选项覆盖默认解析行为。
- 🔒 **安全与性能**：支持 Trusted Types 策略增强 XSS 防护，同时提供性能基准测试数据。
- 📜 **版本迁移清晰**：提供从 v1 到 v6 的详细迁移指南，帮助用户平滑升级。
- ❓ **常见问题解答**：涵盖 XSS 安全、HTML 清理、脚本标签处理、属性调用、嵌套错误等常见疑问。

---

### [STRICH | 网页应用条码扫描](https://strich.io/?ref=react-status)

**原文标题**: [STRICH | Barcode Scanning for Web Apps](https://strich.io/?ref=react-status)

STRICH 是一个基于 JavaScript 的网页端条码扫描库，支持实时扫描 1D/2D 条码，无需原生应用或后端。

- 📦 轻松集成：通过 NPM 安装 `@pixelverse/strichjs-sdk`，零依赖，兼容所有主流框架。
- 🆓 免费试用：提供 30 天免费试用，定价透明，可按月或年订阅，无设备数量限制。
- 🌐 纯网页方案：无需 App Store，通过链接或二维码分发，一次开发即可覆盖所有平台。
- 📱 条码支持：涵盖 Code 128、EAN、QR Code、Data Matrix、PDF417 等多种 1D/2D 条码。
- 🎯 强大扫描能力：内置扫描 UI，支持闪光灯、点击对焦，可读取褪色、破损、反光或反色条码。
- 🏢 企业级功能：提供白标定制、离线扫描、SOC2 合规选项，支持银行转账和采购订单。
- 🗣️ 客户好评：众多用户称赞其性能稳定、集成简单、文档清晰，且性价比优于 Scandit 等竞品。
- 🔄 持续更新：跟踪最新 Web 技术，定期更新以适配浏览器变化，并提供技术支持。
- ❓ 常见问题：支持 Angular/Vue/React 等框架，超出扫描限额不会立即拒绝扫描，会友好提醒升级。

---

### [Node.js — Node.js 26.0.0（当前版本）](https://nodejs.org/en/blog/release/v26.0.0)

**原文标题**: [Node.js — Node.js 26.0.0 (Current)](https://nodejs.org/en/blog/release/v26.0.0)

Node.js 26.0.0 正式发布，带来多项重要更新，包括默认启用 Temporal API、V8 引擎升级至 14.6、Undici 更新至 8.0，以及多项弃用和移除。

- 🚀 **Temporal API 默认启用**：现代日期/时间 API，替代传统 Date 对象，提供更强大、更丰富的功能。
- ⚙️ **V8 引擎升级至 14.6**：新增 `Map.prototype.getOrInsert()` 和 `Iterator.concat()` 等特性。
- 🌐 **Undici 更新至 8.0.2**：HTTP 客户端实现迎来新功能和改进。
- 🗑️ **多项弃用和移除**：包括 `crypto`、`http`、`stream`、`module` 等模块的旧 API 被移除或弃用。
- 🛠️ **构建要求提升**：GCC 要求升至 13.2，Python 3.9 支持被移除，Power 9 成为 AIX/IBM i 目标。
- 🔒 **安全修复**：修复了数组索引哈希碰撞漏洞（CVE-2026-21717）。
- 📦 **其他更新**：libuv 更新至 1.52.1，ICU 更新至 78.3，并新增 Ed25519 上下文参数支持。

---

### [Node.js — Node.js 26.1.0（当前版本）](https://nodejs.org/en/blog/release/v26.1.0)

**原文标题**: [Node.js — Node.js 26.1.0 (Current)](https://nodejs.org/en/blog/release/v26.1.0)

Node.js 26.1.0 版本发布，引入了实验性的 `node:ffi` 模块，并包含多项功能增强和错误修复。

- 🧪 **实验性 FFI 模块**：新增 `node:ffi` 模块，允许从 JavaScript 加载动态库并调用原生符号，需通过 `--experimental-ffi` 标志启用，且存在安全风险。
- 📦 **Buffer 增强**：为 `indexOf` 和 `lastIndexOf` 方法添加了 `end` 参数。
- 🔐 **加密功能更新**：`crypto.diffieHellman()` 现在接受密钥数据，并实现了 `randomUUIDv7()` 方法。
- 🐛 **调试器改进**：`node inspect` 新增了无需编辑的运行时表达式探测功能。
- 📁 **文件系统更新**：`fs.stat()` 添加了 `signal` 选项，`statfs` 暴露了 `frsize` 字段。
- 🌐 **HTTP 改进**：`ClientRequest` 选项合并更健壮，`IncomingMessage` 新增 `req.signal` 属性。
- 🔄 **流（Stream）优化**：`duplexPair` 支持销毁传播，并修复了多个流相关问题。
- 🧪 **测试运行器增强**：支持 mock 超时 API、`AbortSignal.timeout` 模拟、测试顺序随机化等功能。
- 🛠️ **进程与工具**：`process` 在 `execve(2)` 失败时抛出错误而非中止，允许空的 `--experimental-config-file`。
- 🎨 **工具函数更新**：`util` 模块支持使用十六进制颜色进行文本着色。
- 📦 **依赖升级**：更新了 undici、npm、openssl、sqlite 等多个依赖库至最新版本。

---

### [宣布 Rolldown 1.0 | VoidZero](https://voidzero.dev/posts/announcing-rolldown-1-0)

**原文标题**: [Announcing Rolldown 1.0 | VoidZero](https://voidzero.dev/posts/announcing-rolldown-1-0)

Rolldown 1.0 正式发布，这是一款基于 Rust 的高性能 JavaScript 打包工具，现已达到生产就绪状态。

- 🚀 **性能卓越**：Rolldown 比 Rollup 快 10-30 倍，速度与 esbuild 相当，采用 Rust 和 Oxc 实现，多家公司已实现显著构建时间缩短。
- 🔄 **Rollup 插件兼容**：完全兼容 Rollup 插件 API，支持钩子过滤和内置插件，无需大规模代码迁移即可从 Vite 8 无缝升级。
- 🛠️ **独特打包功能**：提供更小的默认包体积、激进的死代码消除、细粒度代码分割（如 Framer 减少 67% 分块），以及 webpack 风格的分块规则。
- 📅 **开发历程**：从 2024 年 4 月首次公开到 2026 年 5 月 1.0 稳定版，历经两年打磨，Vite 8 已默认使用 Rolldown。
- 🎯 **未来规划**：计划推出 Vite 全包模式（开发启动快 3 倍）、稳定延迟桶优化（减少构建时间和输出体积），以及原生 MagicString 支持。
- 🤝 **社区贡献**：感谢约 200 位贡献者，欢迎参与文档改进、插件兼容性测试和首次贡献。

---

### [[提案] 无引擎Vitest（引擎无关API）· vitest-dev/vitest · 讨论 #10271 · GitHub](https://github.com/vitest-dev/vitest/discussions/10271)

**原文标题**: [[Proposal] Viteless Vitest (Engine-Agnostic API) · vitest-dev/vitest · Discussion #10271 · GitHub](https://github.com/vitest-dev/vitest/discussions/10271)

### 概述总结
Vitest 团队提出“Viteless Vitest”提案，旨在通过引擎无关的API解耦测试运行器与Vite的强绑定，允许用户选择不同的构建工具或运行时环境，同时保持现有功能不变。

- 🚀 **核心提案**：新增 `--engine` 标志，允许用户指定适配器包（如 `@vitest/engine-node`），以支持非Vite环境（如原生Node、Deno、Bun等），Vite作为默认引擎。
- 🔗 **解耦动机**：Vitest的测试运行器、断言、快照等功能已不依赖Vite，仅转换、模块解析、热重载等边缘功能耦合Vite，解耦后可避免强制使用完整Vite管道。
- 📦 **引擎契约**：引擎包导出一组指令（如配置解析、模块转换、文件监听等），Vitest核心通过稳定接口驱动，引擎负责配置加载，Vite成为可选集成之一。
- 🛠️ **迁移兼容**：现有用户无破坏性变更，省略 `--engine` 默认使用 `@vitest/engine-vite`，保持 `vite.config.ts` 等行为不变。
- ❓ **开放问题**：引擎契约的具体形状、非CLI下引擎指定方式、引擎特有选项的类型隔离、报告器/覆盖率等组件的兼容性声明。
- 🎯 **非目标**：不替代Vite作为默认推荐、不定义通用插件格式、不要求首日支持所有构建工具，仅需一个替代引擎验证契约。

---

