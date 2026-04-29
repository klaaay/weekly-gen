### [React 摘要：电子邮件通讯](https://reactdigest.net/)

**原文标题**: [React Digest: Email Newsletter](https://reactdigest.net/)

概述摘要  
React Digest 是一份专为 React 开发者精心策划的每周新闻通讯，内容精选文章并附简短摘要，帮助读者节省时间、每周学习新知识，深受超过 22,723 名前端工程师的认可。

- 📬 每周一封邮件，精选 React 相关文章与简短摘要  
- ⏱ 节省寻找优质内容的时间，提升学习效率  
- 🧠 每周学习新知识，紧跟 React 技术演进  
- 🌟 读者高度评价，称其“文章实用、内容优质”  
- 👥 读者包括超过 22,723 名前端工程师，来自知名公司  
- 📅 新闻通讯自 2013 年持续运营至 2026 年

---

### [React 编译器十八个月：历程、争议与未来展望 | Sascha Becker](https://saschb2b.com/blog/react-compiler-year-in-review)

**原文标题**: [The React Compiler at Eighteen Months: The Arc, the Debates, and What's Next | Sascha Becker](https://saschb2b.com/blog/react-compiler-year-in-review)

React 编译器发布18个月后，生态系统经历了从发布集成到社区辩论的完整阶段，其最大贡献是消除了"忘记useCallback依赖"这类bug，但绿色项目已解决，存量项目仍需努力。

- 📅 **十八个月发展弧线**：从2024年底稳定发布，经历框架集成（Next.js/Expo等）、静默采用期（减少重渲染bug）、生态系统清算（暴露违反React规则的旧库），目前绿色项目已解决，存量项目仍是挑战。
- ⚙️ **编译器核心能力**：构建时自动插入记忆化，消除手动useMemo/useCallback/React.memo，可细粒度记忆化子表达式，但会增加构建时间（数十%）和包体积（低个位数百分比）。
- 🚫 **四大失败场景**：渲染时修改props/闭包、渲染时读取ref、遗留类组件、以及"use no memo"逃生口（应视为临时方案而非永久标记）。
- 🛠️ **推荐迁移路径**：先升级React→安装ESLint插件修复违规→注解模式启用编译器→推理模式→批量删除手动记忆化→考虑严格模式，避免一次性大PR。
- 🤔 **三大争议焦点**：React规则成为可执行契约（强制更严格编程模型）、"use no memo"成为永久技术债（类似@ts-ignore）、编译器与运行时优化器（如Million.js）的互补关系。
- 🔮 **未来五大方向**：更细粒度编译控制、编译器感知的服务器组件、useEvent收敛、React Native原生支持、开发者工具可视化编译器行为。
- 💡 **个人观点**：编译器最大遗产是消除特定bug类别，但更关键的是React规则成为构建时契约，旧库仍在适应中。新项目应直接启用，存量项目需在修复旧代码和标记逃生口间权衡。

---

### [网络研讨会：移动应用安全事件的经验教训](https://www.guardsquare.com/webinar-lessons-learned-from-security-incidents-in-mobile-apps?utm_campaign=31454753-2026%20Real%20Attacks.%20Real%20Defenses.&utm_source=ReactDigest&utm_medium=newsletter)

**原文标题**: [Webinar: Lessons Learned from Security Incidents in Mobile Apps](https://www.guardsquare.com/webinar-lessons-learned-from-security-incidents-in-mobile-apps?utm_campaign=31454753-2026%20Real%20Attacks.%20Real%20Defenses.&utm_source=ReactDigest&utm_medium=newsletter)

概述总结
本次网络研讨会聚焦移动应用安全事件，由安全研究员Jan Seredynski主持，深入分析银行、外卖和电商领域的真实案例，探讨开发中的漏洞、安全原则的实效性及防护措施。

- 📱 移动应用已成为全球商业主要入口，处理76%的活跃银行用户和63%的电商收入，但面临人脸验证绕过、位置欺骗等高级攻击
- 🔍 研讨会将剖析银行、外卖和电商领域的真实安全事件，详细说明攻击发生过程及如何避免
- 🛡️ 重点讲解开发过程中引入的漏洞，以及现代移动应用中哪些安全原则有效、哪些在实践中失效
- 💡 提供从真实案例中汲取的见解，帮助创建安全的移动电商体验
- 📅 研讨会将于5月12日下午4点CEST/上午10点EDT举行，由Guardsquare的安全研究员和渗透测试员Jan Seredynski主持

---

### [将铁路前端从Next.js迁移](https://blog.railway.com/p/moving-railways-frontend-off-nextjs)

**原文标题**: [Moving Railway's Frontend Off Next.js](https://blog.railway.com/p/moving-railways-frontend-off-nextjs)

Railway 的前端已从 Next.js 迁移至 Vite + TanStack Stack，实现了零停机、两 PR 完成，构建时间从 10 分钟缩短至 2 分钟以下。

- 📦 **迁移原因**：Next.js 构建时间过长（10 分钟+），且其服务器优先模式不匹配 Railway 客户端主导的实时仪表盘和画布应用。
- 🔧 **新框架选择**：采用 TanStack Start + Vite，提供类型安全路由、一流布局、快速 HMR 和按需 SSR，更符合实际开发需求。
- 🚀 **迁移过程**：通过两个 PR 完成，PR1 移除所有 Next.js 依赖，PR2 替换框架并迁移 200+ 路由，合并后立即上线，无停机。
- 🎯 **放弃内容**：放弃内置图片优化（改用 Fastly 边缘优化）、部分生态工具（自建替代）和框架成熟度，但方向正确。
- ⚡ **性能提升**：构建时间从 10 分钟降至 2 分钟以下，开发服务器即时启动，路由变更类型检查，布局无需变通。
- 🌐 **部署优化**：前端运行在 Railway 上，使用 Fastly 边缘缓存、Vite 内容哈希模块，实现增量更新和零停机部署。
- 💡 **核心理念**：前端框架应优化迭代速度，基础设施应使部署无缝，Railway 正为此构建体验。

---

### [Next.js中的'use client'：作用、代价与使用时机](https://punits.dev/blog/use-client-in-nextjs/)

**原文标题**: ['use client' in Next.js: What It Does, What It Costs, and When to Use It](https://punits.dev/blog/use-client-in-nextjs/)

`use client` 指令在 Next.js 中用于将组件标记为客户端组件，使其支持浏览器端交互，但会带来性能成本。

- 📝 `use client` 不会禁用服务端渲染，组件仍会在服务端生成 HTML，但会额外将 JavaScript 发送到浏览器并进行水合（hydration），以支持 React 钩子和事件处理。
- 📦 **增加包体积**：客户端组件会将 JavaScript 发送到浏览器，导致包体积增大（示例中从 157 kB 增至 215 kB），即使无交互也需要基础运行时。
- ⏳ **水合成本**：浏览器需在主线程上水合客户端组件，这会延迟交互性并影响性能指标（如 INP）。
- 🌊 **数据获取瀑布**：客户端组件中数据获取需用 `useEffect`，导致内容在 HTML 渲染、JS 下载和水合后才开始获取，延迟内容显示并影响 SEO。
- 🔍 **SEO 影响**：`use client` 本身不损害 SEO，但若在客户端获取数据，初始 HTML 可能缺少内容，搜索引擎需依赖 JS 执行，降低可靠性。
- 🧩 **最佳实践**：应将 `use client` 用于需要交互的叶组件，避免在顶层使用，并通过服务端组件传递子组件或属性来保持大部分组件树为服务端组件。
- ✅ **使用场景**：当组件需要 React 钩子、事件处理或浏览器 API 时使用；当数据可在服务端获取或仅渲染静态内容时避免使用。

---

### [我基准测试了五种包体积膨胀模式并扫描了500个仓库，实际上只有两种真正重要。](https://stackinsight.dev/blog/bundle-bloat-empirical-study/)

**原文标题**: [I Benchmarked Five Bundle Bloat Patterns and Scanned 500 Repos. Only Two Actually Matter.](https://stackinsight.dev/blog/bundle-bloat-empirical-study/)

## 概述总结
通过对五种常见打包膨胀模式进行基准测试，并扫描500个前端仓库，发现只有两种模式（lodash和moment.js的默认导入）会显著增加打包体积，而最常被警告的桶导入（barrel imports）在现代打包工具中实际上没有影响。

- 📊 **研究结论**：在五种常见打包膨胀反模式中，只有两种（lodash默认导入和moment.js默认导入）真正影响打包体积，其他三种（MUI桶导入、antd桶导入、react-icons命名空间导入）在现代打包工具中产生完全相同的结果。

- 🔍 **关键数据**：`import _ from 'lodash'`比tree-shakeable替代方案多发送17.6倍代码（25.3 KB gzip），`import moment from 'moment'`比dayjs多发送5.9倍代码（16.8 KB gzip）。

- 🚫 **桶导入误区**：`import { Button } from '@mui/material'`与直接路径导入产生完全相同打包体积，现代打包工具（esbuild、Vite、webpack 5）能正确处理桶导入。

- 📈 **实际影响**：扫描500个仓库发现17,594个发现，其中74.7%是桶导入（无实际影响），只有20.7%（3,637个）是高严重度的lodash和moment导入。

- 💡 **行动建议**：优先检查并替换lodash→lodash-es和moment→dayjs，停止将桶导入转换为路径导入的无用重构，更新ESLint规则关注真正有影响的模式。

---

### [预计算模式：在Next.js中将动态数据编码到URL中 | Aurora Scharff](https://aurorascharff.no/posts/the-precompute-pattern-encoding-dynamic-data-into-urls-in-nextjs/)

**原文标题**: [The Precompute Pattern: Encoding Dynamic Data into URLs in Next.js | Aurora Scharff](https://aurorascharff.no/posts/the-precompute-pattern-encoding-dynamic-data-into-urls-in-nextjs/)

### 概述总结

Next.js 16 中引入的 `cacheComponents` 功能使得 Precompute 模式在多数场景下不再必要，但该模式仍被大型电商团队用于处理动态数据（如认证状态、区域、货币等）的静态生成。其核心思想是将请求特定数据编码到 URL 中，从而将动态渲染转化为已知变体的静态生成。

- 🔄 **核心机制**：在代理层（middleware）读取动态 API（如 `cookies()`），将数据编码为 URL 路径段，并通过内部重写使页面从 `params` 读取，避免直接调用动态 API，实现静态渲染。
- 🧩 **实现步骤**：定义上下文类型与编解码函数 → 在代理中编码并重写 URL → 组件从 `params` 解码获取数据 → 使用 `generateStaticParams` 预生成已知变体（如登录/未登录）。
- ⚠️ **高基数挑战**：电商场景中，每个编码维度（如认证状态、区域、货币）会倍增路由变体，导致构建时间过长和 ISR 缓存命中率下降。团队需选择性编码低基数数据（如认证状态、区域），并依赖 ISR 处理罕见组合。
- 🛠️ **Vercel Flags SDK**：该模式已由 Vercel Flags SDK 正式化，提供 `precompute` 和 `generatePermutations` 等工具，支持加密和构建时生成，简化了实现。
- 🚀 **cacheComponents 替代方案**：Next.js 16 的 `'use cache'` 允许组件独立缓存，动态数据通过 Promise 传递并仅在消费组件中挂起，避免了全局动态渲染。但 Precompute 模式仍适用于需要根据区域、货币等变化缓存内容的场景。
- 🔮 **未来改进**：`rootParams` 功能将允许组件直接导入顶层动态参数（如 `[locale]`），消除 prop drilling，使 Precompute 模式更易用。

---

### [JavaScript 中真正的新特性（以及接下来会发生什么）—— Neciu Dan](https://neciudan.dev/whats-new-in-javascript)

**原文标题**: [What's actually new in JavaScript (and what's coming next) — Neciu Dan](https://neciudan.dev/whats-new-in-javascript)

以下是您提供的文章内容的摘要，使用指定模板：

ECMAScript 2025 已正式发布，ES2026 候选版也已获批，JavaScript 语言迎来多项实用更新。迭代器助手、Set 新方法、Map.getOrInsert、Array.fromAsync 等特性将显著改善日常编码体验。Temporal、using 关键字和 import defer 虽未进入 ES2026，但浏览器和 polyfill 已成熟，可提前使用。AI 编码助手因训练数据滞后，可能仍会输出旧模式，建议通过配置文件或插件引导其使用新 API。

- 📜 **迭代器助手 (Iterator helpers)**：为迭代器原生添加 .map、.filter、.take 等懒加载方法，无需先转换为数组，适合处理无限序列或大数据流。
- 🧩 **Set 新方法**：提供 union、intersection、difference 等非破坏性集合操作，参数支持“类 Set”对象，无需手动循环或依赖 lodash。
- 📦 **JSON 模块**：原生支持通过 `import config from './config.json' with { type: 'json' }` 导入 JSON，无需打包器或 fetch。
- 🔄 **Promise.try**：统一处理同步/异步/抛出异常的函数，所有结果都通过 .then/.catch 链传递，避免双重错误处理。
- 🔒 **RegExp.escape**：安全转义用户输入中的正则特殊字符，内置防注入处理，替代手写转义函数。
- 💾 **Float16Array**：新增 16 位浮点类型数组，内存减半，适用于 WebGPU 和 TensorFlow.js 等场景。
- 🧮 **Math.sumPrecise**：使用 Shewchuk 算法精确求和浮点数，避免累加误差，解决 0.1+0.2 问题。
- 🔢 **Uint8Array base64/hex**：原生支持字节数组与 base64/hex 字符串互转，告别手写 btoa/atob 或工具函数。
- ❌ **Error.isError**：跨 realm 可靠的错误类型检测，替代不稳定的 instanceof Error。
- 🔗 **Iterator.concat**：将多个迭代器串联为一个，无需手动编写生成器包装。
- 🗂️ **Map.getOrInsert**：提供 getOrInsert 和 getOrInsertComputed 方法，简化计数、缓存等常见模式。
- 📥 **Array.fromAsync**：异步版本的 Array.from，将异步可迭代对象收集为数组，替代手动 for-await-of 循环。
- 📝 **JSON.parse 带源文本**：reviver 函数新增 context.source 参数，可获取原始文本，用于安全处理大整数等场景。
- ⏰ **Temporal (ES2027)**：全面替代 Date 对象，提供 PlainDate、ZonedDateTime 等类型，原生支持时区、ISO 8601 和精确日期计算。
- 🧹 **using 关键字 (Stage 3)**：自动资源管理，在作用域结束时自动释放文件句柄、数据库连接等，无需 try/finally。
- ⏳ **import defer (Stage 3)**：延迟模块求值，仅在首次访问命名空间属性时执行，优化应用启动性能。
- 🤖 **AI 编码助手适配**：由于训练数据滞后，AI 可能输出旧模式。建议通过 .cursorrules 或插件配置现代 API 偏好，引导其使用新特性。

---

### [我为什么不再在JavaScript中链式调用所有东西 - Matt Smith](https://allthingssmitty.com/2026/04/20/why-i-dont-chain-everything-in-javascript-anymore/)

**原文标题**: [
    Why I don't chain everything in JavaScript anymore - Matt Smith
  ](https://allthingssmitty.com/2026/04/20/why-i-dont-chain-everything-in-javascript-anymore/)

概述总结
- 🧩 链式调用虽简洁，但超过2-3步时，可读性和可调试性会下降
- 🔍 分步编写代码（命名中间变量）更易理解和调试，避免逻辑混合
- ⚡ 链式调用可能处理多余数据，如用filter+map取第一个值，不如用find或for循环高效
- 🛠️ 调试链式调用时，常需插入console.log或拆分代码，增加麻烦
- 📊 建议：1步链式完全OK，2步通常OK，3-4步考虑拆分，5步以上必须拆分
- 🔄 异步链式（如Promise链）混合数据获取与转换，不如分步清晰
- 💡 命名中间变量、分离逻辑、仅保留清晰链式，是避免头痛的有效方法

---

### [font-family 的回退机制并非你想的那样——CSS Wizardry](https://csswizardry.com/2026/04/font-family-doesnt-fall-back-the-way-you-think/)

**原文标题**: [font-family Doesn’t Fall Back the Way You Think – CSS Wizardry](https://csswizardry.com/2026/04/font-family-doesnt-fall-back-the-way-you-think/)

### 概述总结
本文揭示了`font-family`属性在回退机制中的一个常见误解：当子元素单独声明字体时，浏览器不会继承父元素的字体堆栈，而是仅基于该声明进行回退，导致加载期间出现不期望的字体闪烁（如Times New Roman）。解决方案是始终为每个`font-family`声明提供完整的字体堆栈（包括通用字体族），以避免布局偏移和视觉问题。

- 📝 **`font-family`回退是独立的**：子元素声明字体后，不会继承父元素的回退堆栈，仅基于自身声明处理。
- ⏳ **导致Times字体闪烁的原因**：若声明仅包含单一未加载字体，浏览器会回退到默认字体（如Times），而非父级字体。
- 🔧 **修复方法简单**：始终为每个`font-family`指定完整堆栈（如`"Open Sans", sans-serif`），确保回退行为可控。
- 🎯 **影响核心网页指标**：不正确的回退可能因字体尺寸差异导致布局偏移（CLS），影响用户体验和性能评分。
- 💡 **关键教训**：任何覆盖字体族的地方，都必须完整定义堆栈，避免依赖继承或默认值。

---

### [构建无断点的UI – 前端大师博客](https://frontendmasters.com/blog/building-a-ui-without-breakpoints/)

**原文标题**: [Building a UI Without Breakpoints – Frontend Masters Blog](https://frontendmasters.com/blog/building-a-ui-without-breakpoints/)

本文探讨了现代响应式设计如何从依赖断点转向基于组件内在布局、流体值和容器查询的自适应系统，以实现更简洁、可维护的CSS。

- 📉 **断点模式正在过时**：传统基于视口宽度的断点设计在组件化、嵌套复用的现代界面中，容易导致CSS膨胀、覆盖复杂和组件行为不可预测。
- 🧩 **方法一：内在布局优先**：使用 `auto-fit` 和 `minmax()` 创建自适应网格，或用 `flex-wrap` 实现灵活双栏布局，无需硬编码断点。
- 📏 **方法二：使用流体值**：通过 `clamp()` 函数实现字体、间距等属性的连续缩放，替代离散的断点跳变，减少CSS代码量。
- 📦 **方法三：容器单位实现局部响应**：利用 `cqi` 等容器单位，让组件尺寸基于自身容器宽度而非视口，提升跨上下文复用性。
- 🔄 **方法四：容器查询处理结构变化**：当组件需要真正的结构改变（如从竖排变横排）时，使用 `@container` 查询，而非全局视口断点。
- 🎯 **媒体查询的新定位**：媒体查询应聚焦于设备能力和用户偏好（如悬停、指针、配色方案、减少动效），而非作为主要布局引擎。
- ✅ **迁移清单**：审计现有查询、替换标量分支为 `clamp()`、采用内在布局、添加容器类型、仅在结构变化时用容器查询、保留环境意图的媒体查询。
- 💡 **核心理念转变**：响应式设计从“断点编排”转向“意图驱动系统”，组件默认自适应，断点成为有意的例外工具。

---

### [MDN新前端的幕后揭秘](https://developer.mozilla.org/en-US/blog/mdn-front-end-deep-dive/)

**原文标题**: [Under the hood of MDN's new frontend](https://developer.mozilla.org/en-US/blog/mdn-front-end-deep-dive/)

MDN 前端架构全面升级，采用 Web 组件和服务器组件技术，显著提升性能和开发体验。

- 🏗️ **架构革新**：从臃肿的 React SPA 转型为轻量级 Web 组件 + 服务器组件架构，解决了技术债务和 CSS 混乱问题
- ⚡ **性能飞跃**：开发环境启动时间从 2 分钟缩短至 2 秒，采用 Rspack 构建工具实现极速编译
- 🧩 **Web 组件化**：使用 Lit 构建自定义元素，实现按需加载，仅加载页面实际使用的 JavaScript/CSS
- 📦 **智能加载**：通过自动检测 DOM 中的自定义元素，实现组件级代码分割和异步加载
- 🎨 **CSS 优化**：服务器组件自动收集所需 CSS，仅加载当前页面必要的样式文件
- 🔄 **渐进增强**：利用 Declarative Shadow DOM 实现交互组件的渐进式增强，未加载 JS 时保持基础功能可用
- 🌐 **标准化开发**：基于 Baseline 标准选择 Web API，确保跨浏览器兼容性
- 🛠️ **简化开发**：统一的开发命令和热重载机制，大幅降低贡献门槛

---

### [编程文摘：邮件通讯](https://programmingdigest.net/?utm_source=web-archive&utm_campaign=react)

**原文标题**: [Programming Digest: Email Newsletter](https://programmingdigest.net/?utm_source=web-archive&utm_campaign=react)

概述摘要  
- 📬 《编程文摘》是一份为软件工程师精心策划的每周通讯。  
- 👥 已有超过22,978名软件工程师订阅，每周仅发送一封邮件。  
- 📚 精选文章并附简短摘要，帮您节省寻找优质内容的时间。  
- 🧠 每周都能学到新知识。  
- 💬 读者反馈积极，称赞内容切合实际、推荐优质资源。  
- 🏢 读者来自众多知名科技公司。  
- 📅 涵盖2013至2026年，提供通讯订阅、隐私政策及广告服务。

---

### [科技领导力：电子邮件通讯](https://leadershipintech.com/?utm_source=web-archive&utm_campaign=react)

**原文标题**: [Leadership in Tech: Email Newsletter](https://leadershipintech.com/?utm_source=web-archive&utm_campaign=react)

本通讯专为CTO、工程经理及资深工程师设计，旨在提升领导力，每周一和周四发送一封邮件，精选文章并附简短摘要，帮助节省时间并每周学习新知识。读者反馈强调其在领导力建设、架构讨论、沟通和授权方面的价值，受到众多科技领袖的阅读。

- 📧 每周两封邮件，覆盖CTO、工程经理及资深工程师的领导力提升
- ⏱️ 精选文章附简短摘要，节省寻找优质内容的时间
- 📚 每周学习新知识，持续成长
- 💬 读者称赞领导力文章、架构讨论、会议规划和沟通技巧
- 🤝 强调授权的重要性，指出这是常被忽视的关键技能
- 🌍 读者来自全球科技领袖群体
- 📅 通讯由Bonobo Press于2013-2026年运营，提供隐私保护和广告选项

---

### [C# 摘要：电子邮件通讯](https://csharpdigest.net/?utm_source=web-archive&utm_campaign=react)

**原文标题**: [C# Digest: Email Newsletter](https://csharpdigest.net/?utm_source=web-archive&utm_campaign=react)

概述摘要  
- 📬 每周一封精心策划的邮件，专为.NET开发者设计  
- 👥 已有超过20,234名C#工程师订阅  
- 📝 精选文章并附简短摘要，节省寻找优质内容的时间  
- 🧠 每周都能学到新知识  
- ⭐ 读者反馈：在工作中实际应用了部分内容，并对LINQ、标准功能标志等文章感到惊喜  
- 🌍 读者来自全球各地的.NET工程师社区  
- 🏢 由Bonobo Press于2013-2026年运营，提供新闻通讯、隐私保护和广告服务

---

### [让开发者保持最新动态 – Bonobo Press](https://bonobopress.com/)

**原文标题**: [Keeping developers up to date â Bonobo Press](https://bonobopress.com/)

Bonobo Press 自2013年起，通过简洁的软件通讯，为超过8万名开发者、IT专家和技术人员提供最新资讯。

- 📰 提供面向软件开发者、技术主管和CTO的精选通讯，内容简洁省时
- 🎯 提供广告服务，帮助触达活跃的软件工程师、团队领导及IT决策者
- 📞 欢迎通过官网联系，咨询、建议或洽谈广告合作

---

### [过往通讯：第1页](https://reactdigest.net/newsletters)

**原文标题**: [Past Newsletters: Page 1](https://reactdigest.net/newsletters)

以下是您提供的 React Digest 内容摘要：

React Digest 涵盖了从 React 编译器优化、框架迁移到性能调优、架构设计及 AI 辅助开发等多个方面的最新动态与深度文章。

- ⚛️ **React 编译器18个月进展**：Railway 从 Next.js 迁移至 Vite，构建时间从10分钟降至2分钟以下；研究发现仅 lodash 和 moment.js 导致实际包体积膨胀。
- 🌐 **MDN 前端重构**：MDN 放弃 React SPA，改用服务端 HTML 和 Lit Web 组件，开发构建时间从2分钟缩短至2秒；GitHub 通过减少 DOM 和虚拟化加速大 PR 差异对比。
- 🧵 **React Fiber 渲染机制**：Fiber 将渲染拆分为约5ms的块，优先处理点击等紧急更新；实用技巧包括 useReducer 优于 useState 的场景、startTransition 与防抖的区别，以及避免无意义的 memoization。
- 🧑‍💻 **成为 Web 开发者指南**：为初级开发者提供非语法层面的全局视野；同时揭示信号（signals）并未真正解决 React 的怪癖，并展示如何在 Next.js App Router 中优雅处理错误。
- 🪝 **打破规则的 use() 钩子**：use() 钩子可在渲染时读取 Promise、与 Suspense 配合，消除经典的 useEffect 数据获取反模式；此外，讨论测试 ID 对可访问性的影响，以及为 useEffect 函数命名的理由。
- 🗑️ **18个月代码重构教训**：团队从重建未测试代码库中认识到对真实用户的伤害；Bippy 工具允许在运行时访问 React Fiber 树，无需修改代码；单例模式可与 React 钩子良好配合。
- 🏗️ **基于特性的 React 架构**：React 状态更新是异步的，setState 只是排队重渲染；AsyncLocalStorage 允许任何函数获取 React Router 上下文，无需逐层传递。
- 🧠 **前端内存泄漏研究**：86%的前端项目存在内存泄漏，500个 React、Vue 和 Angular 仓库中发现55,864个泄漏模式，主要源于定时器和事件未清理；每个周期仅8KB，但长期会话中累积显著。
- ⚡ **一周内重建 Next.js**：探索 Steve Faulkner 的 AI 驱动框架 vinext 和 Aiden Bai 的 React Doctor 代码诊断工具；涵盖查询抽象和多目录路由以提升项目水平。
- 📜 **数十亿行的虚拟滚动**：探讨 React 中的虚拟滚动技术、React Router 加载器集成、微前端见解、为 AI 增强 Next.js，以及构建健壮的 React 组件。
- 💔 **心形表情符号的调试故事**：一个心形表情符号导致 Web 应用变慢的趣事；React Native 最新改进、退出动画技巧，以及解决交互卡顿的方法。
- 🤖 **AI 调试 React**：探索 AI 的调试能力、React 新的 ViewTransition 元素、有效单元测试的见解，以及 Copilot CLI ASCII 横幅的工程原理；同时了解何时避免过度使用 useCallback。
- 🚫 **useOptimistic 并非万能**：深入 useOptimistic 钩子的复杂性、React 编译器在库更新中的问题，以及 Turbopack 的高效代码编译；还介绍了一个新的开源 React 桥接和创新的组合模式。
- ✅ **React 最佳实践**：来自 Vercel 的最佳实践、2025年 React 生态系统的演变、使用客户端组件和 React 过渡提升性能，以及避免 TanStack 表单中的陷阱。
- 🔍 **如何“窃取”任何 React 组件**：无需源码即可重建组件、优化性能、使用新的 useEffectEvent 管理状态；还有 React Conf 2025 的精彩演讲。
- 🧠 **AI 编写 React 代码的真实水平**：AI 在 React 编码中的混合表现、30年 Web 开发演变、编写有效前端测试的技巧；以及 React 过渡和类型安全组件的见解。
- 🏆 **2025年最佳 React 文章**：新年快乐！精选2025年最受欢迎的5篇文章，涵盖 React 设计模式、状态管理、重渲染和函数式编程。
- 📉 **React 漏洞教训**：深入探讨 React 近期漏洞、React 服务器组件和性能优化；感谢支持，祝节日快乐，一月再见。
- 🚀 **React 19.2 进一步优化 INP**：React 19.2 的 INP 优化、TanStack Router 见解、TanStack Start 与 Next.js 对比；以及 useEffectEvent 的重要技巧。
- ⚠️ **React 和 Next.js 的严重漏洞**：探索 React 和 Next.js 的严重漏洞、构建设计系统的最佳实践、改进 React 钩子；以及如何为 MDX 文档添加“复制为 markdown”功能。

---

### [隐私](https://reactdigest.net/privacy)

**原文标题**: [Privacy](https://reactdigest.net/privacy)

本隐私政策概述了React Digest如何收集、使用和保护您的个人信息。

- 📧 我们仅收集您的电子邮件地址，用于发送新闻通讯，不会用于其他目的。
- 🔒 我们承诺在收集信息前明确用途，并仅用于指定目的或法律要求。
- ⏳ 我们只在必要期限内保留个人信息，并确保其准确、完整和最新。
- 🛡️ 我们采取合理的安全措施保护个人信息，防止丢失、盗窃或未经授权访问。
- 👶 我们不会故意收集13岁以下儿童的信息，如发现请立即联系我们。
- 📋 根据英国《数据保护法》，您可以请求访问我们存储的您的所有信息。
- 🗑️ 您可以通过邮件请求删除您的数据，我们会在处理中提供必要指导。
- 🚫 我们坚决反对垃圾邮件，您可随时通过邮件中的取消订阅链接退订。
- 📅 本政策适用于2013-2026年，由Bonobo Press发布。

---

### [媒体资料包 – 倭黑猩猩出版社](https://bonobopress.com/media-kit/)

**原文标题**: [Media Kit â Bonobo Press](https://bonobopress.com/media-kit/)

本媒體套件介紹了 Bonobo Press 旗下四份技術通訊的訂閱數據、廣告價格與合作方式，旨在幫助廣告主精準觸及軟體開發與技術領導者。

- 📊 **高互動讀者群**：通訊互動率為業界基準的兩倍以上，並透過嚴格清單清理維持高品質訂閱者。
- 👥 **Leadership in Tech**：專為技術管理者設計，訂閱數 22,325，開信率 57.95%，每次贊助 $2,235，預估點擊 365-585 次。
- 💻 **Programming Digest**：面向軟體工程師，訂閱數 20,032，開信率 50.41%，每次贊助 $985，CPC 約 $2.0-$3.61。
- 🖥️ **C# Digest**：鎖定 .NET 開發者，訂閱數 17,098，開信率 54.92%，每次贊助 $1,220，CTR 高達 21.63%。
- ⚛️ **React Digest**：專注前端 React 開發者，訂閱數 20,075，開信率 54.06%，每次贊助 $1,375，預估點擊 303-523 次。
- 📝 **純文字廣告格式**：僅限文字內容以提升互動，需提供連結、標題與描述，並於發佈前 4 天提交。
- 📅 **預訂流程**：需提前數週聯繫，確認檔期後開立發票，付款鎖定排程，並可協作優化廣告文案。
- 🤝 **合作夥伴案例**：曾與 Okta、GitLab、Datadog、MongoDB、Pluralsight 等知名品牌合作，且多為重複贊助。

---

