### [JavaScript 周刊第 734 期：2025 年 5 月 2 日](https://javascriptweekly.com/issues/734)

**原文标题**: [JavaScript Weekly Issue 734: May 2, 2025](https://javascriptweekly.com/issues/734)

概述总结  
本期内容涵盖了 JavaScript 生态的最新动态，包括开源库更新、技术文章、工具发布以及开发者活动等。  

- 🎉 **GSAP v3.13 发布**：Webflow 收购后，GSAP 动画库及其付费插件（如 MorphSVG 和 SplitText）现已完全免费，适用于商业用途。  
- 📊 **AG Charts**：AG Grid 推出的开源图表库，支持 React、Angular 和 Vue，提供 20 多种图表类型和高级功能。  
- 🔍 **JavaScript 值转字符串的复杂性**：Dr. Axel Rauschmayer 探讨了看似简单但实际复杂的值转字符串问题。  
- ⚡ **V8 显式编译提示优化**：Chrome 136 引入的 V8 优化，通过提前编译特定文件加速启动。  
- 📅 **Node.js 版本动态**：v18 已停止支持，v23 进入维护模式，v24 即将发布。  
- 🎂 **jQuery 20 周年纪念活动**：2026 年 1 月将在德州举办 jQuery 重聚活动。  
- 🛠️ **Deno 2.3 发布**：支持 FFI 和 Node 原生插件，单二进制编译功能增强。  
- 📖 **React 的`use client`指令解析**：Dan Abramov 详解 React Server Components 中客户端/服务端指令的实践意义。  
- 🧩 **PDFSlick 3.0**：基于 PDF.js 的 PDF 查看工具，支持 React、Solid 等框架，新增 ICC 配置和大页面渲染优化。  
- 🔄 **Redis 重新开源**：Redis 8 回归 AGPL 许可证，再次成为真正开源项目。  
- ❤️ **静态 HTML 与 JavaScript 的结合**：Simon Willison 提倡使用 GitHub Pages 发布静态 HTML+JavaScript 项目。  
- 🎨 **CSS 新功能**：`shape()`函数支持复杂路径裁剪，提升 CSS 图形能力。

---

### [3.13 版本发布 | GSAP | 文档与学习](https://gsap.com/blog/3-13/)

**原文标题**: [3.13 release | GSAP | Docs & Learning](https://gsap.com/blog/3-13/)

GSAP 3.13 版本发布，宣布 GSAP 及其所有插件（包括 SplitText 和 MorphSVG 等）现在完全免费，甚至可用于商业用途。团队将继续维护和创新，同时与 Webflow 合作开发下一代交互功能。SplitText 插件进行了全面重写，新增多项功能并优化了性能。此外，GSAP 3.13 还支持动画到 CSS 变量，并简化了在 Webflow 中的安装流程。

- 🎉 GSAP 及其所有插件（包括 SplitText、MorphSVG 等）现在完全免费，可用于商业用途。
- 🛠️ GSAP 团队（Jack、Cassie 和 Rodrigo）将继续维护和创新，并与 Webflow 合作开发新功能。
- 📥 所有插件已添加到 GSAP Github 仓库和 NPM 包，可直接从 gsap.com 下载。
- 💌 Club GSAP 会员无需再使用私有仓库，可直接从公共 NPM 仓库安装，社区徽章将在论坛更新。
- 🔧 SplitText 插件完全重写，新增 14 项功能，包括屏幕阅读器支持、响应式重新分割、嵌套元素处理等。
- ⚠️ SplitText v3.13 有一些不常见的破坏性变更，如移除了`position: "absolute"`和`lineThreshold`。
- 🆕 GSAP 3.13 支持动画到 CSS 变量，如`gsap.to(".target", {color: "var(--my-color)"})`。
- 🌐 Webflow 用户现在可以直接在设置中启用 GSAP 及其插件，安装更加便捷。
- 📚 提供完整的发布说明、文档、学习资源和社区论坛链接。

---

### [GSAP 加入 Webflow | GSAP | 文档与学习](https://gsap.com/blog/webflow-GSAP/)

**原文标题**: [GSAP is Joining Webflow | GSAP | Docs & Learning](https://gsap.com/blog/webflow-GSAP/)

GSAP（GreenSock 动画平台）被 Webflow 收购，以提升其动画能力。这一合作将使 GSAP 在更广泛的网络社区中发挥更大作用，同时保持其独立性和现有定价计划。Webflow 作为网站体验平台，与 GSAP 共享“赋予所有人开发超能力”的使命，双方将结合优势创造更易用的动画工具。

- 🎉 GSAP 被 Webflow 收购，将增强 Webflow 的动画功能  
- 🌍 GSAP 继续公开可用，服务于更广泛的网络社区  
- 💰 现有用户的定价和许可计划保持不变  
- 🚀 Webflow 将投入资源推动 GSAP 的产品创新  
- 💡 双方使命一致：简化复杂技术，赋能所有人  
- 🤝 合作将结合 GSAP 的动画技术与 Webflow 的界面设计专长  
- 🔮 未来计划尚未明确，但承诺将带来特别的产品  
- 📢 邀请用户分享对 GSAP 加入 Webflow 家族的期望和建议

---

### [MorphSVG | GSAP | 文档与学习](https://gsap.com/docs/v3/Plugins/MorphSVGPlugin/)

**原文标题**: [MorphSVG | GSAP | Docs & Learning](https://gsap.com/docs/v3/Plugins/MorphSVGPlugin/)

MorphSVGPlugin 是一个用于 SVG 路径变形的插件，能够通过动画改变 SVG 路径的`d`属性，实现形状之间的平滑过渡。

- 🚀 **快速开始**：通过 CDN 引入插件，使用`gsap.to()`方法即可实现形状变形，如将圆形变为河马形状。
- 🛠️ **功能亮点**：支持不同点数或类型的路径变形，可将多边形、折线等转换为路径，并支持在 Canvas 上绘制结果。
- ⚙️ **配置选项**：可通过配置对象设置变形类型（线性或旋转）、原点、形状索引等，以获得更自然的变形效果。
- 🔍 **形状索引**：使用`shapeIndex`调整起点映射，`findShapeIndex()`工具可帮助可视化并调整起点。
- 📊 **性能优化**：通过预编译（`precompile`）和定义`shapeIndex`提前优化性能，减少初始计算时间。
- 🎨 **Canvas 渲染**：支持通过`render`函数将变形结果绘制到 Canvas，适用于高性能渲染需求。
- 🔄 **多形状变形**：利用 GSAP 的时间轴功能，轻松实现形状的连续变形。
- 📹 **视频教程**：提供高级功能演示和性能优化技巧的视频教程。

该插件功能强大且灵活，适用于各种 SVG 动画需求。

---

### [SplitText | GSAP | 文档与学习](https://gsap.com/docs/v3/Plugins/SplitText/)

**原文标题**: [SplitText | GSAP | Docs & Learning](https://gsap.com/docs/v3/Plugins/SplitText/)

SplitText 是一个用于将 HTML 元素文本分割成字符、单词和/或行的 JavaScript 库，便于创建精美的动画效果。它支持响应式重新分割、屏幕阅读器可访问性、嵌套元素处理等功能，并与 GSAP 无缝集成。

- 🚀 **快速开始**：通过 CDN 引入 SplitText，使用 `SplitText.create()` 方法分割文本，并通过 GSAP 实现动画效果。
- 🔧 **配置选项**：支持多种分割类型（字符、单词、行），可自定义 CSS 类名、响应式重新分割、嵌套元素处理等。
- 🌟 **新特性**：v3.13.0 版本新增了自动屏幕阅读器可访问性、响应式重新分割、嵌套元素处理等功能。
- 🎭 **动画效果**：使用 GSAP 对分割后的字符、单词或行进行动画处理，支持延迟和淡入效果。
- 🔄 **响应式分割**：通过 `autoSplit` 选项在字体加载或容器宽度变化时自动重新分割文本。
- 🎭 **遮罩效果**：通过 `mask` 选项为分割后的文本添加遮罩元素，便于实现显示/隐藏效果。
- ♿ **屏幕阅读器支持**：默认添加 `aria-label` 和 `aria-hidden` 属性，提升可访问性。
- ↩ **恢复功能**：使用 `revert()` 方法将分割后的文本恢复到原始状态。
- ⚠ **注意事项**：避免在字体加载前分割文本，仅分割需要的部分以提升性能，不支持 SVG 文本节点。

---

### [GSAP 展示](https://gsap.com/showcase/)

**原文标题**: [GSAP Showcase](https://gsap.com/showcase/)

GSAP（GreenSock Animation Platform）是一个专业的 JavaScript 动画库，适用于现代网页开发，提供丰富的工具和插件支持。

- 🎬 **核心功能** - 提供高性能的 JavaScript 动画解决方案，适用于各种网页动画需求。  
- 🛠️ **工具与插件** - 包括 ScrollTrigger、MotionPath、Flip 等插件，支持滚动、SVG、UI 交互等动画效果。  
- 🌟 **展示与社区** - 提供作品展示平台（Showcase）和活跃的社区，用户可以分享和学习动画案例。  
- 📚 **学习资源** - 包含文档（Docs）、教程视频和 Starter Templates，帮助开发者快速上手。  
- 🆓 **免费与注册** - 提供免费账户注册，用户可参与论坛讨论、接收更新并管理个人设置。  
- 📧 **订阅服务** - 支持通过邮件订阅 GSAP 的最新动态和功能更新。  
- 🔗 **社交与支持** - 提供 GitHub、CodePen、LinkedIn 等社交平台链接，方便用户交流和获取支持。

---

### [资源 | GSAP 演示示例](https://gsap.com/demos/)

**原文标题**: [Resources | GSAP Demos](https://gsap.com/demos/)

GSAP 是一个专业的 JavaScript 动画库，适用于现代网页开发，提供丰富的工具和插件支持多种动画效果。

- 🌐 **核心功能** - 提供 GSAP 核心动画库，支持高性能的 JavaScript 动画。
- 🎚️ **滚动动画** - 包含 ScrollTrigger、ScrollSmoother 等插件，实现复杂的滚动动画效果。
- 🖍️ **SVG 支持** - 提供 DrawSVG、MorphSVG 等插件，专门用于 SVG 图形的动画处理。
- 🖱️ **UI 交互** - 包含 Flip、Draggable 等插件，增强用户界面交互体验。
- ✍️ **文本动画** - 提供 SplitText、ScrambleText 等插件，实现丰富的文本动画效果。
- 📚 **学习资源** - 提供文档、视频教程和社区论坛，帮助开发者学习和使用 GSAP。
- 🛠️ **模板与示例** - 提供多种框架的启动模板（如 React、Next.js）和演示示例，方便快速上手。
- 📧 **社区与支持** - 拥有活跃的社区论坛和 Codepen 示例库，开发者可以分享和学习。
- 🔄 **持续更新** - 通过订阅 GSAP 新闻通讯，获取最新动态和更新信息。

---

### [缓动效果 | GSAP | 文档与学习](https://gsap.com/resources/getting-started/Easing/)

**原文标题**: [Easing | GSAP | Docs & Learning](https://gsap.com/resources/getting-started/Easing/)

缓动（Easing）是运动设计中最关键的部分，能为动画赋予个性和生命力。通过不同的缓动效果，可以控制动画的变化速率，从而创造出更自然或更具表现力的动态效果。

- 🌀 **缓动的重要性**：选择合适的缓动效果能为动画增添个性，使其更生动。  
- 🎢 **缓动效果对比**：无缓动的动画（如匀速旋转）与带弹跳缓动的动画（如加速后弹跳停止）效果截然不同。  
- 📊 **缓动的数学原理**：缓动是通过数学计算控制补间动画的变化速率，但用户无需手动计算，直接选择即可。  
- 🛠️ **缓动可视化工具**：可通过点击选择缓动类型或调整参数，实时预览效果。  
- 🔧 **缓动类型**：包括线性（none）、弹性（elastic）、弹跳（bounce）、指数（expo）等，每种类型还分 in、out、inOut 三种子类型。  
- 🚀 **UI 动画推荐**：`power1.out`等缓出效果适合 UI 过渡，快速启动增强响应感，缓停则显得自然。  
- ⚠️ **注意事项**：部分高级缓动（如 SlowMo、RoughEase）需单独加载，核心库中未包含。  
- 📹 **学习资源**：推荐通过视频教程（如 CreativeCodingClub.com 的免费 GSAP 课程）深入学习缓动技巧。

---

### [标准许可证 - GreenSock](https://gsap.com/community/standard-license/)

**原文标题**: [Standard License - GreenSock](https://gsap.com/community/standard-license/)

GSAP 软件许可协议概述，包括定义、许可授予、限制、所有权、终止条款及其他杂项规定。

- 📜 **定义**：GSAP 许可证指本协议条款；GSAP 产品包括动画库及相关插件；允许用途涵盖网站或数字接口使用；禁止用途涉及与 Webflow 竞争的可视化动画工具开发。  
- 🎟️ **许可授予**：授予全球非独占许可，仅限允许用途使用、复制和展示 GSAP 产品。  
- 🚫 **限制**：禁止用于竞争性产品、逆向工程或移除产品标识。  
- 🔐 **所有权**：GSAP 产品的所有知识产权归 Webflow 所有，许可不转让任何所有权。  
- ⏹️ **终止条款**：违约时 Webflow 可终止许可，用户须停止使用并销毁副本。  
- 📝 **杂项规定**：协议以 Webflow 服务条款为补充，冲突时以本许可为准；Webflow 保留修改权；无弃权条款。  
- 📅 **生效日期**：2025 年 4 月 30 日生效，2025 年 5 月 2 日最后修改。

---

### [在 JavaScript 中将值转换为字符串](https://2ality.com/2025/04/stringification-javascript.html)

**原文标题**: [Converting values to strings in JavaScript](https://2ality.com/2025/04/stringification-javascript.html)

JavaScript 中将值转换为字符串的方法及其注意事项

- 🔍 在 JavaScript 中，将值转换为字符串比看起来更复杂，有多种方法但各有局限性。
- 🛠️ 五种常见的转换方法：`String(v)`、`'' + v`、``${v}``、`v.toString()`、`{}.toString.call(v)`。
- ⚠️ 只有`{}.toString.call(v)`能处理所有特殊值（如`undefined`、`null`、`Symbol()`、`{__proto__: null}`）。
- 🔧 `String(v)`是较安全且简洁的替代方案，但无法处理所有情况。
- ❓ `{}.toString.call(v)`等同于`Object.prototype.toString.call(v)`，直接调用方法避免接收器问题。
- � 原型为`null`的对象因缺少必要方法而难以转换，需自定义`toString`或`Symbol.toPrimitive`。
- 📝 修复问题示例：使用`{}.toString.call(value)`确保所有值都能被转换。
- 🏷️ 普通对象和数组的默认字符串表示不直观，`JSON.stringify()`能提供更详细的信息。
- 🎨 自定义对象的字符串化：通过实现`toString()`方法覆盖默认行为。
- 📊 `JSON.stringify()`的优缺点：支持多数值但不支持`undefined`、`Symbol`、`BigInt`等，且会忽略某些属性。
- 📜 通过`JSON.stringify()`的第三个参数可实现多行输出和缩进控制。
- 👀 使用`JSON.stringify()`显示字符串时，特殊字符（如换行符和制表符）会变得可见。
- 📋 控制台方法（如`console.log`）通常能生成良好的输出，但默认深度有限，可通过配置调整。

---

### [给 V8 一个提示：利用显式编译提示加速 JavaScript 启动 · V8](https://v8.dev/blog/explicit-compile-hints)

**原文标题**: [Giving V8 a Heads-Up: Faster JavaScript Startup with Explicit Compile Hints · V8](https://v8.dev/blog/explicit-compile-hints)

优化 JavaScript 启动性能：通过显式编译提示加速 V8 引擎解析与编译过程  

- 🚀 **V8 引擎优化需求**：快速启动 JavaScript 对网页响应至关重要，但解析和编译关键脚本仍可能成为性能瓶颈。  
- ⏳ **编译策略选择**：V8 需决定函数是立即编译（"eagerly"）还是延迟编译，后者会在调用时触发，可能拖慢主线程。  
- 🔄 **重复解析问题**：延迟编译会导致轻量解析和完整解析重复工作，而立即编译可利用后台线程并行处理。  
- 📊 **实验效果**：测试显示 17/20 的网页性能提升，平均减少 630 毫秒的前台解析和编译时间。  
- 🛠️ **显式编译提示功能**：Chrome 136 支持开发者通过注释`//# allFunctionsCalledOnLoad`标记需立即编译的文件或函数。  
- ⚠️ **谨慎使用**：过度编译会消耗额外时间和内存，建议仅针对核心文件或关键函数。  
- 🔍 **功能验证方法**：通过命令行日志可观察函数编译事件，对比有无编译提示的效果差异。  
- 🔮 **未来方向**：计划支持单个函数级别的编译选择，进一步精细化性能优化。  

（由 Marja Hölttä发布 | 2025 年 4 月 29 日 | 标签：JavaScript）

---

### [Node.js — Node.js 版本发布](https://nodejs.org/en/about/previous-releases)

**原文标题**: [Node.js — Node.js Releases](https://nodejs.org/en/about/previous-releases)

Node.js 的版本发布和支持周期概述，包括官方与社区安装方法的分类标准。

- 🚀 **主要版本发布**：Node.js 的主要版本在发布后有 6 个月的当前支持期，供库作者适配。  
- ⏳ **版本支持周期**：奇数版本（如 9、11）6 个月后停止支持，偶数版本（如 10、12）进入 Active LTS（长期支持），总支持时长为 30 个月。  
- 🔧 **生产环境建议**：仅推荐使用 Active LTS 或 Maintenance LTS 版本。  
- 📅 **发布计划**：详细发布时间表可在 GitHub 查看。  
- 💼 **商业支持**：超过维护期的版本可通过 OpenJS 合作伙伴 HeroDevs 获得商业支持。  
- 🔄 **版本状态表**：包含多个版本的代号、发布时间、最后更新日期及当前状态（如 v23 维护中、v22 为 LTS 等）。  
- 📥 **安装方法分类**：分为“官方”和“社区”两类，官方方法需满足严格标准（如同步发布、直接沟通渠道、使用官方二进制文件等）。  
- 🌍 **社区方法要求**：需支持所有非 EOL 版本、兼容至少一个官方操作系统，且必须开源免费。  
- 🖥️ **操作系统兼容性**：如声称支持 Windows 或 Linux，需覆盖所有主流版本及发行版。

---

### [jQuery 重聚——20 年后](https://www.jqueryreunion.com/)

**原文标题**: [jQuery Reunion - 20 years later](https://www.jqueryreunion.com/)

jQuery 20 周年重聚活动，回顾这一改变 Web 开发的革命性库的诞生与影响，活动将于 2026 年 1 月 16 日至 18 日在德克萨斯州弗里斯科举行。

- 🎉 **jQuery 20 周年庆典**：庆祝 jQuery 库发布 20 周年，回顾其如何简化 Web 开发，解决浏览器兼容性问题。  
- 📅 **活动日期**：2026 年 1 月 16 日至 18 日，为期三天。  
- 🏨 **活动地点**：德克萨斯州达拉斯弗里斯科的 Hyatt Regency 酒店。  
- 🕒 **首日安排**：  
  - ✈️ 抵达弗里斯科（时间自定）。  
  - 🏨 下午 4 点至 6 点：酒店签到。  
  - 🎮 晚上 6 点至 9 点：在国家电子游戏博物馆享用晚餐并无限畅玩街机游戏。  
- 🏎️ **次日安排**：  
  - 🚌 上午 8:30 至 9:30：乘车前往赛道。  
  - 🏁 上午 10 点至中午 12 点：在达拉斯卡丁车综合体体验德州最快的卡丁车。  
  - 🍖 中午 12 点至下午 1 点：德州烧烤午餐。  
  - 🎤 下午 2:30 至 6 点：非 jQuery 主题的短演讲（5-15 分钟）。  
  - 🍽️ 晚上 6 点至 7 点：晚餐。  
  - 🐞 晚上 7 点至 7:30：戏剧性的 Bug 朗读环节。  
  - 🍻 晚上 7:30 至 10 点：欢乐时光。  
- 😢 **最后一天**：  
  - 上午 11 点至中午 12 点：告别活动“悲伤时刻”。

---

### [Svelte 最新动态：2025 年 5 月](https://svelte.dev/blog/whats-new-in-svelte-may-2025)

**原文标题**: [What’s new in Svelte: May 2025](https://svelte.dev/blog/whats-new-in-svelte-may-2025)

Svelte Summit 2025 即将在巴塞罗那举行，同时介绍了 Svelte 和 SvelteKit 的最新更新和社区动态。

- 🎉 **Svelte Summit 2025**：即将在巴塞罗那举行，提供虚拟门票选项。
- ⚡ **异步 Svelte**：开发团队正在构建异步功能，支持在组件中使用`await`。
- 🚀 **性能优化**：部分表达式现可部分评估以提高运行时性能（Svelte 5.27.0/5.28.0）。
- 📦 **CLI 更新**：Svelte CLI 新增`--install <package-manager>`标志以指定包管理器（cli@0.8.1）。
- ☁️ **适配器改进**：CloudFlare 适配器合并为一个（adapter-cloudflare@7.0.0），Vercel 适配器新增符号链接功能（adapter-vercel@5.7.0）。
- 🛠️ **SvelteKit 修复**：包括`HandleServerError`钩子改进，支持`getRequestEvent`。
- 🌟 **社区展示**：多个基于 Svelte 的应用和工具，如 TableSlayer、Iconia、CMSDocs 等。
- 📚 **学习资源**：包括 SvelteKit 教程、Svelte London 会议视频和 This Week in Svelte 播客。
- 📖 **推荐文章**：涵盖 Graphite、Cloudflare Workers 与 SvelteKit 集成、实时仪表盘构建等主题。
- 🛠️ **工具与库**：如 diaper（Svelte 5 底部栏组件）、Anime.js v4、Vite 静态资源插件等。
- 💬 **反馈渠道**：欢迎通过 Reddit 或 Discord 提供反馈。

---

### [Astro 2025 年 4 月更新动态 | Astro](https://astro.build/blog/whats-new-april-2025/)

**原文标题**: [What’s new in Astro - April 2025 | Astro](https://astro.build/blog/whats-new-april-2025/)

2025 年 4 月 Astro 生态系统的更新概览，包括新功能发布、社区动态、工具推荐及用户案例展示。

- 🚀 Astro 5.6 和 5.7 版本发布，新增 Cloudflare 环境支持、SVG 组件稳定化及实验性字体 API  
- 🌟 Starlight 0.33 和 0.34 带来社交图标自定义、Tailwind 4 支持等改进  
- 🔥 Astro 月下载量突破 200 万次，Firebase Studio 等知名项目采用  
- 🎨 社区展示多个创新网站，如 Hypertext TV 和 WebTUI 终端风格 CSS 库  
- 👥 新晋技术指导委员会成员加入，框架团队领导层调整  
- 📚 丰富的内容资源：Next.js 迁移对比、WordPress 集成指南等教程  
- 🛠️ 实用工具推荐：Astro Tanstack SPA 方案、Starlight 全屏模式插件等  
- 🎭 新增多款主题模板，涵盖博客、企业站、作品集等场景  
- 📱 用户案例亮点：医疗慈善机构 Marie Curie、游戏开发门户 LudumLanding 等  
- 📖 Starlight 文档框架应用实例，如 Sharp 高性能图像处理文档  
- 💡 鼓励社区参与，邀请分享项目至 Discord 展示频道

---

### [使用 pnpm 和 Yarn 添加 JSR 包](https://deno.com/blog/add-jsr-with-pnpm-yarn)

**原文标题**: [Add JSR packages with pnpm and Yarn](https://deno.com/blog/add-jsr-with-pnpm-yarn)

JSR 现在支持通过 pnpm 和 Yarn 直接安装包，并且可以安装带有 JSR 依赖的 npm 包，同时支持发布带有 JSR 依赖的 npm 包。

- 🎉 **支持 pnpm 和 Yarn**：现在可以通过 pnpm 和 Yarn 直接安装 JSR 包。  
- 🔗 **兼容 npm 包**：可以安装带有 JSR 依赖的 npm 包，并发布带有 JSR 依赖的 npm 包。  
- 📜 **安装指南更新**：JSR 包页面已更新，显示如何通过 pnpm 和 Yarn 安装。  
- 📦 **pnpm 支持**：从 pnpm v10.9 开始，支持通过 `pnpm add jsr:<scope>/<pkg_name>` 安装 JSR 包，并自动更新 `package.json`。  
- 🧶 **Yarn 支持**：从 Yarn v4.9.0 开始，支持通过 `yarn add jsr:<scope>/<pkg_name>` 安装 JSR 包，并自动更新 `package.json`。  
- 🔮 **未来计划**：JSR 将提供更多功能，包括模块作者发布带有 JSR 依赖的包。  
- 💬 **社区互动**：可以通过 Discord、Twitter、Bluesky、YouTube 关注 JSR 动态，或参加双周办公时间。  
- 📢 **最新动态**：JSR 近期宣布了开放治理委员会和 OpenAI 在 JSR 上的支持。

---

### [运算符查询 - 搜索 JavaScript 运算符](https://www.joshwcomeau.com/operator-lookup/)

**原文标题**: [Operator Lookup - Search JavaScript Operators](https://www.joshwcomeau.com/operator-lookup/)

这是一个个人博客网站的页面内容，主要展示了 Josh W Comeau 的个人信息和资源链接。

- 🏠 主页包含导航菜单，如分类、课程、资源等  
- 🔍 提供 JavaScript 运算符查询工具  
- 📧 支持订阅新闻邮件的表单  
- 📂 按分类浏览文章（CSS、React、动画等）  
- 🎓 推荐互动课程（CSS for JavaScript、The Joy of React）  
- ℹ️ 通用信息页（关于作者、博客介绍、联系方式）  
- ⚙️ 网站功能选项（禁用音效、暗黑模式、RSS 订阅）  
- 🔗 社交媒体链接（BlueSky、GitHub、LinkedIn）  
- ©️ 版权声明和使用条款

---

### [Deno 2.3：增强的 deno compile、本地 npm 包支持等](https://deno.com/blog/v2.3)

**原文标题**: [Deno 2.3: Improved deno compile, local npm packages, and more](https://deno.com/blog/v2.3)

Deno 2.3 版本带来了多项改进和新功能，包括增强的 deno compile、本地 npm 包支持、性能优化等。

- 🚀 **deno compile 改进**：支持 FFI 和 Node 原生插件，可生成包含本地库的独立二进制文件，并新增文件排除功能。
- 📦 **本地 npm 包支持**：通过 `deno.json` 配置本地 `node_modules`，方便开发和测试本地 npm 包。
- ✨ **deno fmt 增强**：新增对嵌入 CSS、HTML 和 SQL 的格式化支持，并提供 14 种新的格式化选项。
- 🔧 **deno add 注册表标志**：新增 `--npm` 和 `--jsr` 标志，方便从不同注册表安装依赖。
- 📊 **OpenTelemetry 增强**：支持事件记录、跨服务追踪、`node:http` 自动插桩和 V8 引擎指标收集。
- 🔒 **Windows 代码签名**：Deno 可执行文件现已签名，提升 Microsoft Defender 的信任度。
- 🧩 **deno check 更直观**：无需显式参数，默认检查当前目录下的文件。
- 📈 **测试覆盖率改进**：自动生成覆盖率报告，支持忽略注释和自定义输出目录。
- 📚 **Jupyter 笔记本类型检查**：提升 VSCode 中变量和类型的共享体验。
- ⚡ **依赖安装提速**：内存缓存 npm 包信息，避免重复缓存，安装速度提升约 2 倍。
- 🔄 **显式资源管理**：支持 JavaScript 的 `using` 关键字，简化资源管理。
- 🏎️ **性能优化**：`Deno.serve` 和 HTTP 服务器性能提升，LSP 内存占用减少。
- 🔄 **TypeScript 5.8 和 V8 13.5**：升级至最新版本，带来新特性和性能改进。
- 🛠️ **其他生活质量改进**：包括强制彩色输出、支持 Linux vsock、WebGPU 方法等。

---

### [Prisma 6.7.0 版本发布 · prisma/prisma · GitHub](https://github.com/prisma/prisma/releases/tag/6.7.0)

**原文标题**: [Release 6.7.0 · prisma/prisma · GitHub](https://github.com/prisma/prisma/releases/tag/6.7.0)

Prisma 发布了 6.7.0 稳定版本，引入了多项新功能和改进，包括早期访问的 TypeScript 查询编译器、对 better-sqlite3 驱动器的支持、多文件 Prisma 模式的生产就绪以及生成的输出文件的拆分优化。

- 🎉 Prisma 6.7.0 稳定版发布，包含多项新功能和改进。
- 🔄 早期访问：Prisma ORM 现在支持 TypeScript 查询编译器，替代了原有的 Rust 引擎，适用于 PostgreSQL 和 SQLite。
- 📦 新增对 better-sqlite3 JavaScript 驱动器的支持，可通过 driverAdapters 预览功能使用。
- 📂 多文件 Prisma 模式现已生产就绪，允许用户将模式拆分为多个文件进行组织。
- ✂️ 新 prisma-client 生成器将生成的输出拆分为多个文件，优化大型模式的性能。
- 📚 公司新闻：Prisma 团队还发布了与 Vercel Marketplace 的 Postgres 集成、前端安全访问 Prisma Postgres 的早期访问以及 Prisma 的 MCP 服务器。

---

### [Bun v1.2.11 | Bun 博客](https://bun.sh/blog/bun-v1.2.11)

**原文标题**: [Bun v1.2.11 | Bun Blog](https://bun.sh/blog/bun-v1.2.11)

本次 Bun v1.2.11 版本更新修复了 62 个错误，新增多项功能并优化了 Node.js 兼容性。以下是主要内容：

- 🐛 修复了 62 个错误（处理了 77 个👍）  
- ✨ 新增支持`process.ref`和`process.unref`方法  
- 🛠 添加`util.parseArgs`负选项支持及默认参数功能  
- 🚀 引入 Highway SIMD 库，提升性能  
- 🔧 新增`BUN_INSPECT_PRELOAD`环境变量支持  
- 🌐 改进 Node.js 兼容性（`node:http`、`node:https`、`node:crypto`等）  
- 📥 提供多种安装方式（curl、npm、powershell 等）  
- 🔄 升级命令：`bun upgrade`  
- 🚄 优化 JavaScript 解析器，速度提升约 40%  
- 🛡 改进 DevServer 可靠性，修复崩溃问题  
- 🔑 完善`node:crypto`模块，支持`KeyObject`类层次结构和`structuredClone`  
- 🔌 修复`node:https`中`rejectUnauthorized`选项验证问题  
- 📜 改进`node:readline/promises`错误处理  
- 💻 优化 TypeScript 对`Bun.$`的支持  
- 🐘 修复 PostgreSQL 连接`flush()`方法问题  
- 🔢 修正 HTTP/2 客户端选项验证和端口处理  
- � 修复`queueMicrotask`错误处理，匹配 Node.js 行为  
- 📚 修复`ReadableStream.prototype.tee()`中的拼写错误  
- � 修复`Bun.plugin`在特定情况下的崩溃问题  
- 🔌 修正`TLSSocket`中`allowHalfOpen`行为  
- 🙏 感谢 14 位贡献者的努力！

---

### [发布 electron v36.0.0 · electron/electron · GitHub](https://github.com/electron/electron/releases/tag/v36.0.0)

**原文标题**: [Release electron v36.0.0 · electron/electron · GitHub](https://github.com/electron/electron/releases/tag/v36.0.0)

Electron v36.0.0 发布，包含多项功能更新、改进和错误修复。

- 🚀 **核心升级**：Chromium 升级至 136.0.7103.48，Node.js 升级至 22.14.0，V8 引擎升级至 13.6。
- ⚠️ **破坏性变更**：废弃了 `NativeImage.getBitmap()`，移除了 `systemPreferences.isAeroGlassEnabled()` API。
- 🛠️ **新增功能**：
  - 添加了 `BrowserWindow.isSnapped()` 以检测窗口是否被 Snap 排列。
  - 引入了 `ServiceWorkerMain` 类以在主进程中与服务工作者交互。
  - 添加了 `contextBridge.executeInMainWorld` 以安全地跨世界边界执行代码。
  - 支持 Windows 上的 `roundedCorners` 窗口选项。
- � **错误修复**：
  - 修复了 macOS 上 `getNativeWindowHandle()` 的崩溃问题。
  - 修复了 Linux 上 `webContents.print()` 的崩溃问题。
  - 修复了 Windows 上拖放文件时的崩溃问题。
  - 修复了 macOS 上透明窗口的闪烁和重影问题。
- 📚 **文档改进**：更新了多个 API 的文档，标记了 `Window.autoHideMenuBar` 在 Linux 和 Windows 上的支持。
- 🚫 **废弃功能**：废弃了 `systemPreferences.isAeroGlassEnabled()` API，并将在未来版本中移除。
- 🏗️ **其他变更**：优化了 `webFrame.getZoomLevel` 和 `webFrame.getZoomFactor` API，修复了多个内存泄漏问题。

---

### [发布 pnpm 10.10 · pnpm/pnpm · GitHub](https://github.com/pnpm/pnpm/releases/tag/v10.10.0)

**原文标题**: [Release pnpm 10.10 · pnpm/pnpm · GitHub](https://github.com/pnpm/pnpm/releases/tag/v10.10.0)

pnpm 是一个公共的开源项目，最新版本为 v10.10.0，发布于 2023 年 4 月 27 日，包含了一些小改动和修复。

- 🚀 **项目状态** - pnpm 是一个公共开源项目，拥有 31.5k 星标和 1.1k 分叉。
- 🔄 **最新版本** - 最新版本为 v10.10.0，发布于 2023 年 4 月 27 日，包含 5 次提交。
- 🛠 **小改动** - 允许从本地 pnpmfile 加载 `preResolution`、`importPackage` 和 `fetchers` 钩子。
- 🐞 **修复内容** - 修复了 `cd` 命令在 `shellEmulator` 为 `true` 时的问题，排序了 `pnpm-workspace.yaml` 的键值，并传递了 `npm_package_json` 环境变量到执行的脚本。
- 📜 **文档修正** - 修正了 `--reporter=silent` 选项的描述错误。
- 💖 **社区反应** - 发布后获得了多种表情反应，包括 👍、🎉、❤️ 和 🚀，总计 18 人参与。

---

### [通过 Apps Script 将 Google Analytics 数据导出到表格](https://technicalwriting.dev/analytics/sheets.html)

**原文标题**: [Export Google Analytics data to Sheets via Apps Script](https://technicalwriting.dev/analytics/sheets.html)

本教程详细介绍了如何通过 Google Apps Script 将 Google Analytics 数据导出到 Google Sheets，并实现自动更新和公开访问功能。

- 📊 使用 Google Apps Script 将 Google Analytics 数据导出到 Google Sheets，支持每晚自动更新和手动更新。
- 🛠️ 前提条件：熟悉 Google Sheets 和 JavaScript。
- 📝 设置步骤：创建 Google Sheets 表格，关联 Apps Script 项目，配置依赖和权限。
- 🔧 配置依赖：在 appsscript.json 中添加 Google Analytics 库和必要的 OAuth 权限。
- 📜 脚本创建：复制提供的 Code.gs 脚本，并根据提示修改 TODO 部分（如 Google Analytics 属性 ID、Google Sheets ID 等）。
- 🔒 授权权限：手动运行脚本以授权所需的权限。
- ⏰ 自动更新：设置时间触发器，每晚自动更新数据。
- 🌐 公开数据：通过部署 Web 应用将数据以 JSON 格式公开到互联网（需谨慎使用）。
- 📊 数据展示：表格中包含页面路径、不同时间段的浏览量、会话时长、跳出率等数据，并计算月环比变化。
- 🎨 格式设置：自动为月环比数据列设置颜色格式（红色表示下降，绿色表示增长）。

---

### [Apps Script | Google for Developers](https://developers.google.com/apps-script)

**原文标题**: [Apps Script  |  Google for Developers](https://developers.google.com/apps-script)

Google Workspace 的 Apps Script 是一个基于云的 JavaScript 平台，用于自动化和扩展 Google 产品功能。

- 🚀 **平台概述**：Apps Script 是基于 Google Drive 的云端 JavaScript 平台，可与 Google 产品集成并自动化任务。  
- ⏱️ **自动化功能**：通过自定义菜单、按钮、用户操作或时间表，跨 Google 产品自动执行任务。  
- 📊 **自定义函数**：在 Apps Script 中编写 Google Sheets 函数，像内置函数一样在表格中调用。  
- 🔧 **扩展插件**：构建自动化任务或连接第三方服务的应用，并通过 Google Workspace Marketplace 分享。  
- 💬 **聊天应用**：为 Google Chat 提供对话式界面，让用户像与人交互一样与服务互动。  
- 📺 **学习资源**：Google Workspace Developers 频道提供技巧、窍门和新功能视频。  
- 📝 **更新日志**：查看 Apps Script 的最新功能和改进。  
- 🆘 **支持帮助**：可提问、报告错误或请求新功能。  
- 🔌 **REST API**：通过编程方式管理脚本项目。  
- ©️ **许可信息**：内容遵循 Creative Commons 4.0 许可，代码遵循 Apache 2.0 许可。

---

### [构建离线友好的图片上传系统——Smashing Magazine](https://www.smashingmagazine.com/2025/04/building-offline-friendly-image-upload-system/)

**原文标题**: [Building An Offline-Friendly Image Upload System — Smashing Magazine](https://www.smashingmagazine.com/2025/04/building-offline-friendly-image-upload-system/)

概述：本文介绍了如何利用 PWA 技术（如 IndexedDB、Service Workers 和 Background Sync API）构建一个离线友好的图片上传系统，以解决网络不稳定导致的用户体验问题。系统通过本地存储图片并在网络恢复后自动上传，提升了用户操作的可靠性。

- 🌐 网络不稳定可能导致图片上传失败，影响用户体验  
- 🔄 使用 PWA 技术（IndexedDB、Service Workers、Background Sync API）构建离线上传系统  
- 📊 系统流程：用户选择图片 → 检查网络 → 离线时存储至 IndexedDB → 网络恢复后自动上传  
- 🛠️ 实现步骤：注册 Service Worker → 检测网络状态 → 注册同步事件 → 存储/检索图片 → 上传后清理本地数据  
- ⚠️ 局限性：网络检测不可靠、仅支持 Chromium 浏览器、IndexedDB 存储策略限制  
- 💡 优化建议：通过 UI 反馈（通知、进度条等）提升用户体验  
- 🚀 目标：通过技术手段减少网络依赖，增强应用可靠性

---

### [如何将你的 Clerk 应用部署到生产环境](https://clerk.com/blog/how-to-take-your-clerk-app-to-prod?utm_source=cooper-press&utm_medium=newsletter&utm_campaign=clerk-prod-jsw&utm_content=05-02-25&dub_id=o5T5NynfcMn4ou9O)

**原文标题**: [How to take your Clerk app to prod](https://clerk.com/blog/how-to-take-your-clerk-app-to-prod?utm_source=cooper-press&utm_medium=newsletter&utm_campaign=clerk-prod-jsw&utm_content=05-02-25&dub_id=o5T5NynfcMn4ou9O)

概述  
本文详细介绍了如何将 Clerk 应用从开发环境迁移到生产环境，包括创建生产实例、配置 DNS、更新 API 密钥和设置 SSO 连接等关键步骤，并提供了一个实际案例（Quillmate）的迁移过程。

- 🔄 **开发与生产环境的区别**  
  开发实例注重速度和简便性，支持 HTTP 和共享 OAuth 凭证；生产实例则强调安全性和隔离性，要求 HTTPS 和独立的 OAuth 凭证。

- 🛠️ **迁移到生产环境的步骤**  
  1. 创建生产实例；2. 配置 DNS 记录；3. 更新 API 密钥；4. 设置 SSO 连接（如 Google、GitHub 等）。

- 🌐 **配置 DNS 记录**  
  需要在域名注册商处添加多条 DNS 记录，以确保 Clerk 能够管理认证请求并发送邮件。

- 🔑 **更新 API 密钥**  
  生产环境的 API 密钥以`pk_live`和`sk_live`开头，需在应用配置中替换开发环境的密钥。

- 🔗 **设置 SSO 连接**  
  生产环境中需为每个社交登录提供商（如 Google）注册独立应用，获取客户端 ID 和密钥，并在 Clerk 仪表盘中配置。

- 📝 **实际案例：Quillmate 迁移**  
  1. 创建生产实例并克隆设置；2. 配置 Google SSO；3. 更新 DNS 记录；4. 在 Vercel 中更新域名和 API 密钥。

- ⚠️ **注意事项**  
  DNS 记录可能需要较长时间生效，API 密钥需妥善保管，避免泄露。

- ✅ **结论**  
  迁移到生产环境是确保用户认证安全的关键步骤，需完成实例创建、DNS 配置、OAuth 凭证设置和密钥更新等操作。

---

### ["use client" 有什么用？——过度反应](https://overreacted.io/what-does-use-client-do/)

**原文标题**: [What Does "use client" Do? — overreacted](https://overreacted.io/what-does-use-client-do/)

React Server Components 中的 `'use client'` 和 `'use server'` 指令通过模块系统抽象了客户端与服务器的交互，使跨环境编程更直观和类型安全。

- 🚪 `'use server'`：标记服务器端函数，允许客户端通过异步调用直接触发（底层转为 `fetch`），实现类型安全的 RPC 通信。  
- 📦 `'use client'`：标记客户端组件，服务器可将其转为客户端引用（如 `'/src/file.js#Component'`），自动生成 `<script>` 并注入初始数据。  
- 🌐 **双向门模型**：两个指令分别在模块系统中建立双向通道——`'use server'` 为客户端开向服务器的门，`'use server'` 反之。  
- 🔗 **单一程序思维**：将前后端视为跨环境的整体，通过 `import` 直接引用对方代码（实际不执行），工具链可静态分析类型和依赖。  
- ⚡ **优势**：消除字符串式 API 约定，支持类型检查、代码导航和跨网络组合抽象，同时承认序列化与网络边界的存在。  
- 🛠 **非 React 专属**：本质是模块级 RPC 模式，适用于任何需要跨客户端/服务器协作的 JavaScript 应用架构。

---

### [Deno 的衰落（6 个地区及更多）——David Bushell——Web Dev（英国）](https://dbushell.com/2025/04/28/denos-decline/)

**原文标题**: [Denoâs Decline (6 Regions and Falling) â David Bushell â Web Dev (UK)](https://dbushell.com/2025/04/28/denos-decline/)

Deno Land Inc.及其产品 Deno Deploy 的未来前景黯淡，其全球服务区域持续缩减，其他产品更新缓慢，整体呈现衰退趋势。

- 🌍 **Deno Deploy 区域缩减**：从 2023 年的 35 个区域降至 2025 年的 6 个，服务覆盖大幅缩水，性能下降。  
- 🏢 **商业对比劣势**：相比 Cloudflare（335 城市）和 Bunny（119 PoPs），Deno 的“全球规模”宣传显得名不副实。  
- 📉 **文档与承诺调整**：官方文档删除“新增区域”表述，暗示短期内无扩张计划。  
- 🛠 **其他产品停滞**：  
  - Fresh 框架自 2024 年 10 月后无更新。  
  - Deno KV 自 2023 年底未发布正式版本，疑似被弃用。  
  - JSR（包管理工具）被批评为“山寨 NPM”，背离 Deno 初衷。  
- 🔄 **Deno 运行时问题**：更新集中于 Node 兼容性修复，缺乏创新，甚至引入争议功能（如遥测）。  
- 😠 **用户失望情绪**：作者曾全力投入 Deno，现对项目失去信心，转而关注 Bun 等替代品。  
- 📢 **附加说明**：作者合并了博客与笔记的 RSS 订阅源，供读者选择。  

（注：总结保留了关键数据、产品状态及作者观点，省略了部分个人吐槽和次要细节。）

---

### [如何检测你的网页应用中的内存泄漏（2025 年）- YouTube](https://www.youtube.com/watch?v=6IlTjqU_Tc0)

**原文标题**: [How To Detect Memory Leaks In Your Web App (2025) - YouTube](https://www.youtube.com/watch?v=6IlTjqU_Tc0)

该页面列出了 YouTube 的相关信息和链接，包括关于平台、联系方式、创作者资源、广告合作、开发者工具以及政策条款等内容。

- ℹ️ 关于 YouTube 平台的基本信息  
- 📰 媒体与新闻相关资源  
- ©️ 版权信息与政策  
- 📞 联系 YouTube 的方式  
- 🎨 创作者相关资源与支持  
- 💼 广告合作与商业机会  
- 🛠️ 开发者工具与资源  
- 📜 使用条款与条件  
- 🔒 隐私政策与数据保护  
- ⚖️ 平台政策与安全指南  
- 🔧 YouTube 功能运作机制  
- 🆕 测试新功能的入口  
- © 2025 Google LLC 版权声明

---

### [入侵 Ladybird 浏览器 | Jess 的咖啡馆](https://jessie.cafe/posts/pwning-ladybirds-libjs/)

**原文标题**: [Pwning the Ladybird browser | Jess's Cafe
](https://jessie.cafe/posts/pwning-ladybirds-libjs/)

Ladybird 浏览器引擎 LibJS 中发现并利用了一个 UAF 漏洞，通过构造恶意代理对象触发参数缓冲区释放后重用，最终实现任意代码执行。

- 🕵️♂️ Ladybird 浏览器引擎 LibJS 处于预开发阶段，允许公开披露漏洞  
- 🐛 使用 Fuzzilli 模糊测试发现 10 个崩溃，包括 3 个高危漏洞（堆溢出、GC freelist 损坏、堆 UAF）  
- 💥 漏洞核心：代理构造函数时，恶意[[Get]]处理程序可释放参数缓冲区导致 UAF  
- 🧩 利用步骤：泄露对象地址→伪造 JS 对象→构建任意读写原语→ROP 链实现代码执行  
- 🔧 修复方案：调整原型[[Get]]调用时机（已提交补丁）  
- 💻 漏洞影响：完全控制渲染器进程，演示中通过 ROP 链执行系统命令  
- 📽️ 提供完整漏洞利用代码和演示视频（x86_64-linux 环境）  

关键时间节点：2025 年 4 月 23 日披露，测试基于 commit b8fa355a21 版本。漏洞利用涉及 glibc 堆操作、ASLR 绕过和 vtable 伪造等技术。

---

### [PDF 流畅版](https://pdfslick.dev/)

**原文标题**: [PDFSlick](https://pdfslick.dev/)

PDFSlick 是一个支持在 React、SolidJS、Svelte 和 JavaScript 应用中查看和交互 PDF 的库，提供多种功能和示例。

- 📄 **PDFSlick 全功能查看器** - 包含各种 PDF 工具和功能的完整应用  
- 📂 **多 PDF 文档支持** - 在单个应用中同时处理多个 PDF 文件  
- 🖼️ **缩略图布局** - 突出显示页面缩略图  
- ↔️ **水平缩略图栏** - 水平显示缩略图，垂直展示完整页面  
- 👀 **简易 PDF 查看器** - 提供基本导航和缩放功能  
- ❗ **错误处理支持** - 内置错误处理机制  
- ©️ **版权信息** - PDFSlick 版权所有，Logo 由 Vane Kosturanov 设计

---

### [PDFSlick 全功能阅读器应用](https://pdfslick.dev/examples/pdf-viewer-app)

**原文标题**: [PDFSlick Full Viewer App](https://pdfslick.dev/examples/pdf-viewer-app)

加载数据并打开 PDFSlick 菜单的简要说明  

- 🔄 正在加载数据，请稍候...  
- 📂 数据加载完成后，将自动打开 PDFSlick 菜单  
- 🖱️ 用户可通过菜单进行进一步操作或查看内容  
- ⏳ 加载时间可能因数据大小和网络速度而有所不同

---

### [Koa - 新一代 Node.js Web 框架](https://koajs.com/)

**原文标题**: [Koa - next generation web framework for node.js](https://koajs.com/)

Koa 是由 Express 团队设计的新 Web 框架，旨在为 Web 应用和 API 提供更小巧、更富表现力且更健壮的基础。通过利用异步函数，Koa 摒弃了回调并大幅提升了错误处理能力。其核心不捆绑任何中间件，提供了一套优雅的方法，使服务器开发快速而愉快。

- 🌀 Koa 是 Express 团队打造的新 Web 框架，更轻量、灵活且健壮  
- ⚡ 利用异步函数，避免回调，显著改善错误处理  
- 🧩 核心不捆绑中间件，保持简洁和可扩展性  
- 🛠 提供优雅工具方法，让服务器开发高效愉快

---

### [Express@5.1.0：现作为 npm 默认版本并提供 LTS 支持时间线](https://expressjs.com/2025/03/31/v5-1-latest-release.html)

**原文标题**: [Express@5.1.0: Now the Default on npm with LTS Timeline](https://expressjs.com/2025/03/31/v5-1-latest-release.html)

Express v5.0.0 发布后未立即设为 npm 默认版本，现公布 LTS 时间线及未来规划。

- 📅 **发布时间线**  
  - Express v5.0.0 发布于 2024 年 9 月 9 日，但未立即设为 npm 的 `latest` 版本。  
  - 2025 年 3 月 31 日，v5.1.0 成为默认版本，标志着 v5 进入 `ACTIVE` 阶段。  

- 📚 **文档与迁移支持**  
  - 更新了 v5 文档和迁移指南，社区贡献者帮助完善内容。  
  - 推出 codemod 工具包，简化从 v4 到 v5 的迁移，部分变更仍需手动调整。  

- 🔄 **生态系统兼容性**  
  - 确保中间件和文档适配 v5，减少对新手用户的影响。  
  - 合作伙伴（如 NestJS）提前更新以降低升级摩擦。  

- ⏳ **长期支持（LTS）策略**  
  - 三个阶段：`CURRENT`（新功能 + 修复）、`ACTIVE`（稳定版）、`MAINTENANCE`（仅安全修复）。  
  - v4 进入维护阶段，EOL 时间灵活延长；v5 维护期至少至 2027 年 4 月。  

- 🛠 **v5.1.0 主要变更**  
  - 支持 `Uint8Array` 和 ETag 选项，依赖项版本范围调整，性能优化。  
  - 移除旧版 Node.js 兼容代码，清理冗余依赖。  

- 🌟 **未来计划**  
  - 成立性能工作组，优化 Express 核心瓶颈。  
  - 改进 TypeScript 开发体验和官网，v6 讨论已启动。  
  - 呼吁企业通过 OpenCollective 提供资金支持。  

- 🙏 **致谢**  
  - 感谢所有贡献者和合作伙伴，特别提及 HeroDevs 对企业的迁移支持。

---

### [AI 代码助手——Amazon Q 开发者：构建——AWS](https://aws.amazon.com/q/developer/build/?utm_source=f-f&utm_medium=newsletter&utm_campaign=amazon-q-developer-may&utm_term=jsweekly&utm_content=cli)

**原文标题**: [AI Code Assistant – Amazon Q Developer: Build – AWS](https://aws.amazon.com/q/developer/build/?utm_source=f-f&utm_medium=newsletter&utm_campaign=amazon-q-developer-may&utm_term=jsweekly&utm_content=cli)

Amazon Q Developer 是一款专为大型项目设计的 AI 编程助手，能够从构思到生产代码全程协助开发者，支持多种开发环境和工具。

- 🚀 **快速开始**：免费使用，支持从 IDE 到命令行的多种开发环境。  
- ⚡ **智能 CLI 代理**：Q Developer CLI 代理提供闪电般的编码体验，可读写本地文件、调用 AWS API、运行 bash 命令或生成代码，并实时适应反馈。  
- 💡 **IDE 集成**：支持 VS Code 等主流 IDE，智能代理可自动读写文件、运行 shell 命令，并提供实时状态更新。  
- 📂 **代码理解**：通过@workspace 命令理解整个项目上下文，从认证流程到服务依赖，生成答案和架构图。  
- 📝 **文档生成**：使用“/doc”命令生成和更新 README 文件、数据流图，保持项目文档化，加快入职速度。  
- 🔍 **代码审查**：输入“/review”进行拉取请求审查，代理可捕捉代码中的错误、安全漏洞或 IaC 配置问题。  
- 🌍 **多平台支持**：支持 JetBrains、VS Code、Visual Studio、命令行和 Eclipse（预览版）等多种开发环境。  
- 📊 **高接受率**：Amazon Q Developer 在多行代码建议中行业接受率最高，BT Group 报告 37% 接受率，澳大利亚国民银行报告 50% 接受率。  
- 🔒 **安全扫描**：在大多数流行编程语言中，安全扫描能力优于公开可比的领先工具。  
- 📚 **丰富资源**：提供文档、社区资源等，帮助开发者高效调试和维护代码。  
- 🆓 **免费体验**：通过 AWS Free Tier 免费开始使用。

---

### [AI 代码助手——Amazon Q 开发者：构建 - AWS](https://aws.amazon.com/q/developer/build/?utm_source=f-f&utm_medium=newsletter&utm_campaign=amazon-q-developer-may&utm_term=jsweekly&utm_content=cli)

**原文标题**: [AI Code Assistant – Amazon Q Developer: Build – AWS](https://aws.amazon.com/q/developer/build/?utm_source=f-f&utm_medium=newsletter&utm_campaign=amazon-q-developer-may&utm_term=jsweekly&utm_content=cli)

Amazon Q Developer 是一款专为大型项目设计的 AI 编程助手，能够从构思到生产代码全程协助开发者，支持多种开发环境和工具，提供高效的代码生成、审查和文档管理功能。

- 🚀 **快速开发体验**：Q Developer CLI 代理提供闪电般的编码体验，支持本地文件读写、调用 AWS API、运行 bash 命令和生成代码，并实时反馈调整。  
- 💡 **智能 IDE 集成**：在 VS Code 等 IDE 中，通过代理自动操作文件、运行命令，并实时更新状态，提升开发效率。  
- 📂 **项目上下文理解**：输入`@workspace`可快速了解项目全貌，包括授权流程和服务依赖，支持生成架构图。  
- 📝 **自动文档生成**：使用`/doc`命令生成或更新 README 文件、数据流图，简化项目文档管理，加速团队协作。  
- 🔍 **自动化代码审查**：输入`/review`检查拉取请求，提前发现代码错误、安全漏洞或 IaC 配置问题。  
- 🌐 **多平台支持**：兼容 JetBrains、VS Code、Visual Studio、命令行及 Eclipse（预览版）等开发环境。  
- 📊 **高代码接受率**：行业领先的多行代码建议接受率，BT Group 报告 37% 接受率，澳大利亚国民银行达 50%。  
- 🔒 **安全扫描优势**：在多数流行编程语言中，安全检测能力优于公开基准测试工具。  
- 📚 **丰富资源支持**：提供文档、测试、安全扫描及调试维护等学习资源，支持 AWS 免费层快速入门。  
- 🆓 **免费开始**：通过 AWS Free Tier 免费体验，社区资源助力学习与开发。

---

### [赛弗特 | 黑魔法框架](https://www.seyfert.dev/)

**原文标题**: [Seyfert | The Black Magic Framework](https://www.seyfert.dev/)

Seyfert 发布了 v3.1 版本，这是一个强大且易于使用的 Discord 机器人框架，专注于开发者体验和可扩展性，支持 TypeScript 并提供丰富的自定义选项。

- 🚀 **发布 v3.1 版本**：Seyfert 是一个现代 Discord 框架，平衡了强大功能和简单性。  
- 📜 **TypeScript 编写**：提供类型安全，提升开发体验。  
- ⚡ **高性能与可扩展**：无论机器人规模大小，均表现优异。  
- 🛠️ **开发便捷**：简化设置流程，让开发者专注于逻辑实现。  
- 🎨 **全面自定义**：支持按需调整框架的每个细节。  
- 🔄 **持续更新**：紧跟 Discord 最新功能。  
- 😆 **社区好评**：用户称赞其错误处理、文档、类型系统和事件响应速度（带幽默色彩）。  
- 🤖 **知名用户案例**：包括 CactusFire、Listen 等，认可其在大型机器人中的高效表现（如降低内存占用、提升性能）。  
- 🌍 **开源社区**：代码公开于 GitHub，欢迎贡献。  
- 📥 **快速入门**：提供安装指南和 Discord 社区支持。

---

### [创建你的第一个命令](https://www.seyfert.dev/guide/getting-started/first-command)

**原文标题**: [Creating Your First Command](https://www.seyfert.dev/guide/getting-started/first-command)

概述  
本文介绍了如何使用 Seyfert 框架创建和管理 Discord 机器人的命令，包括基本命令的创建、注册以及如何通过选项增强命令功能。  

- 🚀 **Seyfert 简介** - Seyfert 是一个用于创建 Discord 机器人的框架，能够轻松管理和执行命令。  
- 📂 **命令文件夹** - 所有命令需放在 `commands` 文件夹中，Seyfert 会自动加载并执行这些命令。  
- ✏️ **创建命令** - 使用 `@Declare` 装饰器定义命令信息，并通过继承 `Command` 类实现命令逻辑。  
- 🔄 **注册命令** - 启动机器人时，需通过 `client.uploadCommands()` 方法将命令上传至 Discord，并生成缓存文件避免重复上传。  
- ⚙️ **使用选项** - 通过 `@Options` 装饰器为命令添加选项（如隐藏响应），增强命令的灵活性。  
- 📁 **项目结构** - 建议将命令文件组织在 `src/commands` 目录下，保持代码结构清晰。  
- 📚 **更多信息** - 关于命令选项的详细说明可参考官方文档。

---

### [Storybook 9 现已进入测试版](https://storybook.js.org/blog/storybook-9-beta/)

**原文标题**: [Storybook 9 is now in beta](https://storybook.js.org/blog/storybook-9-beta/)

Storybook 9 现已进入测试阶段，这是迄今为止最具雄心的版本，功能完备并准备就绪，期待用户的反馈以进一步完善。

- 🚀 **功能亮点**  
  - 🚥 组件测试工具  
  - ▶️ 交互测试  
  - ♿️ 无障碍测试  
  - 👁️ 视觉测试  
  - 🛡️ 测试覆盖率  
  - 🪶 体积减少 48%  
  - 🏷️ 基于标签的组织方式  
  - ⚛️ React Native 支持设备和网页  

- 🧩 **组件测试**  
  - 结合了单元测试的速度和端到端测试的准确性，适合大规模覆盖 UI 状态。  
  - 与 Vitest 合作，提供更快的测试运行体验。  

- 🔄 **交互测试**  
  - 支持单独、批量或全 Storybook 运行，可启用监视模式实时测试。  

- ♿ **无障碍测试**  
  - 全新 UI，支持全故事无障碍测试和违规检查。  

- 🖼️ **视觉测试**  
  - 一键测试所有故事，精确到像素级变化。  

- 📊 **测试覆盖率**  
  - 一键计算组件测试的代码覆盖率。  

- ⚖️ **性能优化**  
  - 体积比 Storybook 8 小 48%，依赖结构更扁平，安装更快且无冲突。  

- 🏷️ **标签组织**  
  - 新方式组织和过滤侧边栏中的故事。  

- 📱 **React Native 支持**  
  - 官方支持网页版 React Native，兼容文档和测试功能。  

- 🔄 **轻松升级**  
  - 使用命令`npx storybook@next upgrade`一键升级，自动化迁移系统指导过程。  

- 📢 **反馈需求**  
  - 欢迎用户测试并提供反馈，团队随时准备修复问题和解答疑问。  

- ✉️ **社区与招聘**  
  - 加入邮件列表获取最新动态，团队正在招聘远程开发人员。

---

### [PGlite](https://pglite.dev/)

**原文标题**: [PGlite](https://pglite.dev/)

轻量级 Postgres WASM 构建，压缩后不足 3MB。

- 🚀 完整的 Postgres WASM 构建  
- 📦 压缩后体积小于 3MB  
- 🛠️ 适用于 WebAssembly 环境  
- 🔥 高效且轻量级

---

### [PGlite](https://pglite.dev/repl/)

**原文标题**: [PGlite](https://pglite.dev/repl/)

ElectricSQL 是一个开源项目，提供本地优先的实时数据同步解决方案。

- 🏠 **主页** - 提供项目的基本信息和入口。
- 📄 **关于** - 详细介绍项目的背景和目标。
- 📚 **文档** - 提供使用指南和技术文档。
- 💻 **REPL** - 提供交互式编程环境。
- ⚡ **ElectricSQL** - 项目的核心功能，实现实时数据同步。
- ⭐ **GitHub 星标** - 鼓励用户在 GitHub 上支持项目。

---

### [GitHub - sindresorhus/pretty-bytes：将字节转换为易读的字符串：1337 → 1.34 kB](https://github.com/sindresorhus/pretty-bytes)

**原文标题**: [GitHub - sindresorhus/pretty-bytes: Convert bytes to a human readable string: 1337 → 1.34 kB](https://github.com/sindresorhus/pretty-bytes)

这是一个名为 `pretty-bytes` 的开源项目，用于将字节数转换为人类可读的字符串格式。

- 📦 **项目功能**: 将字节数转换为易读的字符串（例如：1337 → 1.34 kB）。
- 🔧 **安装方式**: 通过 `npm install pretty-bytes` 安装。
- 📝 **基本用法**: 导入 `prettyBytes` 函数并传入数字即可转换。
- ⚙️ **选项配置**: 支持多种选项，如显示正负符号、以比特为单位、使用二进制前缀、本地化输出等。
- 🌍 **本地化支持**: 可以指定语言环境来格式化数字和分隔符。
- 📊 **小数位数控制**: 可设置最小和最大小数位数。
- ❓ **常见问题**: 解释了为什么使用 `kB` 而不是 `KB`（遵循国际单位制标准）。
- 🔗 **相关项目**: 提供了类似功能的 CLI 工具和其他相关模块。
- 📜 **许可证**: 采用 MIT 许可证。
- ⭐ **项目活跃度**: 拥有 1.2k 星标和 84 个分支，被超过 1500 万项目使用。

---

### [GitHub - sebastianwessel/quickjs：一个TypeScript包，用于在WebAssembly QuickJS 沙箱中执行 JavaScript 和 TypeScript 代码](https://github.com/sebastianwessel/quickjs)

**原文标题**: [GitHub - sebastianwessel/quickjs: A typescript package to execute JavaScript and TypeScript code in a webassembly quickjs sandbox](https://github.com/sebastianwessel/quickjs)

一个 TypeScript 包，用于在 WebAssembly QuickJS 沙箱中执行 JavaScript 和 TypeScript 代码，提供安全隔离环境。

- 🚀 **功能特点**：支持安全执行 JavaScript 和 TypeScript 代码，提供基础 Node.js 模块、虚拟文件系统、自定义模块、fetch 客户端及测试运行器。
- 🔒 **安全性**：在隔离的 WebAssembly QuickJS 沙箱中运行不受信任的代码，确保安全。
- ⚡ **性能**：基于轻量高效的 QuickJS 引擎，优化执行速度。
- 📦 **易用性**：提供简洁 API，支持 TypeScript 项目集成。
- 📂 **文件系统**：可挂载虚拟文件系统，支持`node:fs`模块。
- 🌐 **网络请求**：允许通过 fetch 客户端进行 HTTP(S) 调用。
- 🧪 **测试支持**：内置测试运行器和 Chai 断言库。
- 📜 **许可证**：采用 MIT 开源协议。
- 🔧 **依赖工具**：使用 Bun、Biome、Hono 等工具开发。
- 📊 **项目状态**：拥有 726 星标、22 分叉，活跃维护中。

---

### [QuickJS JavaScript 引擎](https://bellard.org/quickjs/)

**原文标题**: [QuickJS Javascript Engine](https://bellard.org/quickjs/)

概述  
QuickJS 是一个轻量级、可嵌入的 JavaScript 引擎，支持 ES2023 规范，具有快速启动和低内存占用特点，适用于多种平台。  

- 🚀 **2025-04-26 新版本发布**：移除了 bignum 扩展和 qjscalc 应用，推荐使用 BFCalc 替代。  
- 📅 **2024-01-13 与 2023-12-09 版本更新**：详情见更新日志。  
- 📖 **简介**：QuickJS 小巧且无外部依赖，支持 ES2023（包括模块、异步生成器等），代码仅 367 KiB。  
- ⚡ **高性能**：低启动时间，单核 2 分钟内完成 ECMAScript 测试套件，生命周期<300 微秒。  
- ✅ **高兼容性**：近乎 100% 通过 ES2023 测试套件，支持垃圾回收（引用计数 + 循环移除）。  
- 💻 **工具链**：可将 JS 编译为无依赖的可执行文件，提供命令行解释器（支持语法高亮）。  
- 🌐 **在线演示**：通过 JSLinux 运行 qjs。  
- 📚 **文档**：提供 HTML/PDF 版本。  
- 📦 **下载**：源码、Unicode 扩展、跨平台二进制文件（Linux/Mac/Windows 等），集成 TypeScript/Babel 编译器。  
- 🔧 **子项目**：嵌入 libregexp（正则库）、libunicode（Unicode 库）、dtoa（浮点解析库）。  
- 📧 **社区**：开发邮件列表。  
- ⚖️ **许可**：MIT 许可证，版权归 Fabrice Bellard 和 Charlie Gordon 所有。

---

### [GitHub - piscinajs/piscina：一个快速高效的Node.js工作线程池实现](https://github.com/piscinajs/piscina)

**原文标题**: [GitHub - piscinajs/piscina: A fast, efficient Node.js Worker Thread Pool implementation](https://github.com/piscinajs/piscina)

Piscina 是一个高效的 Node.js Worker 线程池实现，专注于提升多线程任务的执行效率。

- 🚀 **高效线程通信**：支持线程间快速通信，适用于固定和可变任务场景。
- ⚙️ **灵活配置**：可调整线程池大小，支持资源限制和异步跟踪。
- 📊 **性能监控**：提供任务运行和等待时间的统计信息。
- ❌ **任务取消**：支持通过 `AbortController` 或 `EventEmitter` 取消任务。
- 📜 **多格式支持**：兼容 CommonJS、ESM 和 TypeScript。
- 🔄 **自定义任务队列**：允许使用自定义任务队列实现，如 `FixedQueue` 提升性能。
- 🐧 **Linux 优先级调度**：通过 `niceIncrement` 设置线程优先级（需安装 `@napi-rs/nice`）。
- 📡 **广播通信**：支持通过 `BroadcastChannel` 向所有工作线程广播消息。
- 📉 **队列压力管理**：提供 `maxQueue` 配置防止任务堆积，支持动态调整。
- 📚 **丰富文档与示例**：详细文档和多个示例帮助快速上手。

---

### [GitHub - MrRefactoring/jira.js: JIRA Cloud、Service Desk 及 Agile REST API 的 JavaScript/TypeScript 封装库](https://github.com/MrRefactoring/jira.js)

**原文标题**: [GitHub - MrRefactoring/jira.js: A JavaScript/TypeScript wrapper for the JIRA Cloud, Service Desk and Agile REST API](https://github.com/MrRefactoring/jira.js)

一个用于与 JIRA Cloud、Service Desk 和 Agile REST API 交互的 JavaScript/TypeScript 封装库。

- 🚀 **项目概述**: jira.js 是一个强大的 Node.JS/浏览器模块，支持与 JIRA Cloud API、JIRA Agile Cloud API 和 JIRA ServiceDesk Cloud API 的交互。
- 📦 **安装**: 支持 npm 和 yarn 安装，要求 Node.js 20.0.0 或更高版本。
- 📄 **文档**: 提供详细的文档，覆盖了 JIRA API 的几乎所有功能。
- 🔐 **认证方式**: 支持多种认证方式，包括 Email 和 API Token、OAuth 2.0 等。
- 🛠 **错误处理**: 从 4.0.0 版本开始，引入了新的错误处理系统，包括 HttpException 和 AxiosError。
- 📝 **使用示例**: 提供了创建项目、添加问题等操作的示例代码。
- 📊 **API 分组**: 支持 Agile Cloud API、Version 2/3 Cloud REST API 和 Service Desk Cloud API 等多个 API 分组。
- 📉 **优化 Webpack 包大小**: 支持按需引入 API 分组以减少打包体积。
- 🔗 **其他产品**: 还提供了 Confluence.js 和 Trello.js 等其他 Atlassian 产品的封装库。
- 📜 **许可证**: 采用 MIT 许可证开源。

---

### [发布 v4.3.0 · NodeBB/NodeBB · GitHub](https://github.com/NodeBB/NodeBB/releases/tag/v4.3.0)

**原文标题**: [Release v4.3.0 · NodeBB/NodeBB · GitHub](https://github.com/NodeBB/NodeBB/releases/tag/v4.3.0)

NodeBB v4.3.0 版本发布，包含文档更新、新功能、错误修复、代码重构及测试改进。

- 📄 **文档变更**  
  - 更新 OpenAPI 规范，补充缺失属性。

- ✨ **新功能**  
  - 新增 `clamp-fade` 混入效果，支持分类描述展开处理。  
  - 支持 `Announce(Update(Note))` 消息类型。  
  - 新增分类快速搜索功能及主题版本更新。  
  - 远程用户迁移至分类时，本地用户关注自动转为分类关注。  
  - 聊天允许/拒绝列表功能。  
  - 根级帖子以 `as:Article` 形式联合发布（原为 `as:Note`）。

- 🐛 **错误修复**  
  - 修复非公开内容解析失败问题。  
  - 修复远程分类主题误显示在 `/recent` 的问题。  
  - 修复标记远程分类主题为已读的功能。  
  - 修复标签 URL 双重转义问题。  
  - 处理用户删除时的断言失败清理逻辑。

- 🔧 **代码重构**  
  - 移除日期选择器组件。  
  - 将部分规则迁移至 `nodebb-config`。  
  - 使用 `Promise.all` 优化异步操作。  
  - 直接断言主题至远程分类的逻辑简化。

- 🧪 **测试改进**  
  - 新增远程分类主题回复测试。  
  - 添加用户及群组断言失败测试用例。  
  - 修复测试中因类型变更（`Note` → `Article`）导致的失败。  

- ↩️ **回退**  
  - 撤销虚荣域名功能（需重新设计）。  

- 👥 **贡献者**  
  - 主要开发者：`julianlam`。

---

### [一丝不苟](https://www.meticulous.ai?utm_source=javascript_weekly&utm_campaign=may2nd2025)

**原文标题**: [Meticulous](https://www.meticulous.ai?utm_source=javascript_weekly&utm_campaign=may2nd2025)

Meticulous AI 提供了一种无需编写和维护测试的自动化测试解决方案，通过记录用户交互并生成持续演化的测试套件，覆盖所有代码分支和边缘情况，帮助团队快速迭代并确保代码质量。

- 🚀 **无需编写测试** - Meticulous AI 通过记录用户交互自动生成测试，无需手动编写或维护测试用例。  
- 🔍 **全面覆盖** - 监控代码分支和用户流程，确保所有边缘情况都被测试覆盖。  
- ⚡ **快速反馈** - 在合并代码前查看 PR 对用户工作流的影响，避免回归问题。  
- 🛠️ **无缝集成** - 支持与现有测试套件结合使用或完全替代，轻松集成到开发流程中。  
- 📊 **高效并行测试** - 通过集群并行化测试，数千次测试可在 120 秒内完成。  
- 💬 **用户认可** - 被 Dropbox、WithPower 等 100 多家组织信任，显著提升开发效率和代码质量。  
- 🔗 **多框架支持** - 兼容 NextJS、React、Vue、Angular、Nuxt 和 SvelteKit 等主流前端框架。  
- 🔒 **安全可靠** - 从底层消除测试波动，确保测试结果稳定且无错误。

---

### [JavaScript 条码扫描库](https://strich.io/?ref=js-weekly)

**原文标题**: [JavaScript Barcode Scanning Library](https://strich.io/?ref=js-weekly)

STRICH 是一个用于网页应用的 JavaScript 库，支持实时 1D/2D 条形码扫描，无需原生应用或后端支持。它提供简单透明的定价、丰富的文档和广泛的条码类型支持，适用于多种行业场景。

- 📦 **产品功能**  
  STRICH 提供实时条码扫描，支持 1D/2D 条码类型，包括 Code 128、QR Code、Data Matrix 等。

- 💰 **定价透明**  
  提供 BASIC（99 美元/月）、PROFESSIONAL（249 美元/月）和 ENTERPRISE（定制报价）三种订阅方案，支持免费试用。

- 📚 **开发者友好**  
  零依赖，兼容主流框架（Angular/Vue/React 等），提供详细的文档和示例代码。

- 🌍 **行业应用**  
  成功案例覆盖公共图书馆、零售、医疗物流等多个领域，如 Brooklyn Public Library 和 Swiss Federal Railways。

- 🔍 **技术优势**  
  基于 WebAssembly 和 WebGL，支持离线操作、自定义 UI 和白标功能，适应复杂扫描环境（如模糊或倒置条码）。

- ❓ **常见问题**  
  支持 GS1 标准，提供免费试用和演示应用，与免费方案（如 ZXing）相比性能更优且维护及时。

- 🚀 **免费试用**  
  提供 30 天免费试用和在线演示，便于快速集成测试。

---

### [Redis - 实时数据平台](https://redis.io/)

**原文标题**: [Redis - The Real-time Data Platform](https://redis.io/)

overview summary  
Redis 提供高性能内存数据库解决方案，助力开发者快速构建 AI 应用，支持多种部署方式和数据集成，具备低延迟、高可用性和丰富的功能特性，适用于各类技术栈和场景。  

- 🚀 **加速 AI 应用开发** - 提供高速、大内存和高精度的工具，支持构建聊天机器人和 AI 代理。  
- 🔍 **多功能数据支持** - 包括向量数据库、语义搜索、AI 代理内存和语义缓存（LangCache），降低 LLM 成本。  
- 💡 **可视化开发工具** - Redis Insight 提供免费的图形界面，方便开发、调试和可视化。  
- 💰 **高效缓存方案** - Redis Flex 支持 5 倍缓存扩容，且无需额外成本。  
- ⚡ **实时数据处理** - Redis Query Engine 支持实时数据查询和搜索，Data Integration 实现数据库即时同步。  
- ☁️ **灵活部署选项** - 支持云端、本地/混合云部署，以及开源版本（Redis 8）下载。  
- 🔗 **广泛技术栈兼容** - 与 AWS、Azure、Google Cloud、Vercel 等主流平台及多种编程语言（如 Python、Java、NodeJS）集成。  
- 🛠️ **高可用性与扩展性** - 提供 99.999% uptime、自动故障转移、集群化和多数据结构（如 JSON、向量集合）支持。  
- 🌍 **开发者社区支持** - 通过 GitHub、Discord 等渠道加入社区，获取企业级 Redis 专家咨询。  
- 🏗️ **快速入门** - 提供多语言开发库（如 JavaScript、Go、PHP），文档齐全，支持分钟级接入。

---

### [Redis 的许可证变更与分支乱局，谁看了都闹心 - Ars Technica](https://arstechnica.com/information-technology/2024/04/redis-license-change-and-forking-are-a-mess-that-everybody-can-feel-bad-about/)

**原文标题**: [Redis’ license change and forking are a mess that everybody can feel bad about - Ars Technica](https://arstechnica.com/information-technology/2024/04/redis-license-change-and-forking-are-a-mess-that-everybody-can-feel-bad-about/)

Redis 近期将其许可证从开源的 BSD 许可证更改为“源代码可用许可证”和“服务器端公共许可证”（SSPL），此举引发了云服务提供商和开源社区的分歧与争议。

- 🏢 **Redis 许可证变更**：Redis 公司 CEO Rowan Trollope 解释称，此举是为了防止大型云服务提供商免费使用 Redis 源代码进行商业化销售，尤其是像 AWS 这样的巨头。  
- 🔄 **社区反应与分叉**：Linux 基金会及 AWS、Google Cloud 等支持分叉项目 Valkey，采用 BSD-3-Clause 许可证，以保持完全开源。  
- 🤔 **开发者态度**：多数开发者对许可证变更影响不大，但核心贡献者如 AWS 工程师 Madelyn Olson 表示失望。  
- 💡 **开源历史重演**：类似的分叉事件在 OpenSearch 和 OpenTofu 等项目中也曾发生，开源社区与商业利益再次碰撞。  
- ⚖️ **法律与道德争议**：各方在法律框架内行动，但分歧凸显了开源软件商业化与社区贡献之间的紧张关系。

---

### [Redis 再次开源 —— <antirez>](https://antirez.com/news/151)

**原文标题**: [
Redis is open source again - <antirez>
](https://antirez.com/news/151)

Redis 重新恢复开源模式  

- � 核心变化：Redis 宣布恢复开源许可，回归其最初的开放生态策略。  
- 🔓 许可证调整：从之前的限制性许可（RSAL）重新切换至宽松的开源协议（BSD 或类似）。  
- 💡 影响：开发者可自由使用、修改和分发代码，无需担忧商业限制。  
- 🌍 社区反响：开源社区普遍欢迎这一决定，认为有利于生态创新与协作。  
- 🛠️ 未来方向：Redis 或通过增值服务实现商业化，同时保持核心开源。

---

### [Redis 8 正式发布，新增多项功能及 30 余项性能优化](https://redis.io/blog/redis-8-ga/)

**原文标题**: [Redis 8 is now GA, loaded with new features and more than 30 performance improvements](https://redis.io/blog/redis-8-ga/)

Redis 8 正式发布，作为迄今为止性能最强、扩展性最佳的版本，集成了超过 30 项性能改进、8 种新数据结构，并合并了 Redis Stack 和社区版为统一的 Redis 开源发行版，同时新增 AGPLv3 许可证选项。

- 🚀 **性能飞跃**：Redis 8 实现高达 87% 命令延迟降低、2 倍吞吐量提升及 18% 复制加速，查询引擎处理能力提升 16 倍。  
- 🧩 **新数据结构**：新增向量集合（Beta）、JSON、时间序列及 5 种概率结构（如布隆过滤器、t-digest），强化实时应用支持。  
- 🔄 **统一开源版**：整合 Redis Stack 功能至 Redis 开源版，预装所有模块，简化使用流程。  
- 🔒 **安全增强**：细化 ACL 权限控制，适配新数据结构命令，提升数据完整性。  
- ⚡ **多线程优化**：I/O 多线程实现最高 112% 吞吐量提升，复制内存占用减少 35%。  
- 📜 **许可证新增**：除 RSALv2/SSPLv1 外，新增 OSI 批准的 AGPLv3 选项。  
- 🤖 **AI 与向量支持**：向量集合助力语义搜索，RedisVL 库简化 GenAI 应用开发，兼容主流客户端库。  
- 🛠️ **开发者工具**：Redis Insight 与 VS Code 插件提供可视化支持，集成 AI 助手 Copilot。  
- ⬆️ **升级建议**：Redis Stack 用户需迁移至开源版，旧版维护截止 2025 年 9 月。  
- 📥 **安装渠道**：支持 Docker、Snap、Homebrew 等多种方式，详情见官方文档。

---

### [TypeScript 类似 C#](https://typescript-is-like-csharp.chrlschn.dev/)

**原文标题**: [TypeScript is Like C#](https://typescript-is-like-csharp.chrlschn.dev/)

TypeScript和C#均由微软的Anders Hejlsberg 设计，两者在设计和风格上相似，熟悉其中一种语言可以轻松学习另一种。

- 🧠 设计相似 - TypeScript和C#由同一人设计，风格和结构相近。  
- 🔄 学习曲线平缓 - 掌握其中一种语言后，另一种语言的学习会更容易。  
- 💻 微软背景 - 两者均来自微软，共享相似的设计理念。

---

### [免费提供软件](https://simonwillison.net/2025/Apr/28/give-it-away-for-free/)

**原文标题**: [Giving software away for free](https://simonwillison.net/2025/Apr/28/give-it-away-for-free/)

Simon Willison 认为，目前最佳的自由软件交付方式是使用静态 HTML 和 JavaScript，并通过信誉良好的免费网络托管服务提供。WebAssembly 和 Pyodide 等技术使得这种方法更加灵活和强大。

- 🌐 静态 HTML 和 JavaScript 是目前创建完全免费软件的最佳交付方式  
- 🚀 WebAssembly 扩展了可通过这种方式交付的软件范围  
- � Pyodide 支持客户端 Python 应用程序  
- 💡 这种方法确保软件长期可用，无需持续维护  
- 💰 免费托管服务（如 GitHub Pages）避免了持续费用和更新问题  
- ⚠️ Heroku 等曾经可靠的服务因政策变化不再推荐  
- 📜 开源许可证和可直接使用的链接对用户至关重要  
- 🏆 GitHub Pages 是 2025 年的首选托管平台

---

### [微型模拟器](https://floooh.github.io/tiny8bit/)

**原文标题**: [Tiny Emulators](https://floooh.github.io/tiny8bit/)

该内容主要列举了一系列复古计算机平台（如 CPC、C64、KC85 等）上的游戏和演示程序，并标注了部分操作提示。

- 🎮 包含多种复古计算机平台的游戏和演示程序，如 Amstrad CPC、Commodore C64、KC85 等。
- 🕹️ 部分游戏标注了操作提示，例如“按空格键开始”或“选择 Kempston 操纵杆”。
- 🏗️ 列出了多个演示程序，如“Visual 6502 Remix”、“Visual Z80 Remix”等。
- 📟 包含一些经典游戏，如《Boulderdash》、《Bomb Jack》、《Ghosts'n'Goblins》等。
- 🖥️ 部分游戏支持多种平台，如《Boulderdash》在 CPC、ZX48k、KC85 等多个平台上运行。
- 🎨 演示程序来自不同团队，如 Overlanders、Condense、Vanity 等。
- ⚠️ 部分内容带有警告提示，如“频闪警告”或“按 F1 开始”。

---

### [CSS shape() 命令 | CSS-Tricks](https://css-tricks.com/css-shape-commands/)

**原文标题**: [CSS shape() Commands | CSS-Tricks](https://css-tricks.com/css-shape-commands/)

CSS 的`shape()`函数最近在 Chromium 和 WebKit 浏览器中获得支持，它提供了一种更直观的方式来绘制复杂形状，用于`clip-path`属性剪裁元素。相比传统的 SVG 路径命令，`shape()`使用更易理解的英语术语和 CSS 单位，简化了复杂形状的绘制过程。

- 🎨 `shape()`函数支持在 CSS 中直接绘制复杂形状，替代传统的 SVG 路径命令。
- 📏 使用`from`命令设置起点，支持关键词（如`top left`）或 CSS 单位（如`0 0`）。
- 📐 提供多种绘图命令：`line`（直线）、`vline`（垂直线）、`hline`（水平线）、`arc`（椭圆弧）、`curve`（曲线）和`smooth`（平滑贝塞尔曲线）。
- 🔄 支持动态调整，如悬停时改变形状，但目前不支持过渡或动画效果。
- 🤔 学习曲线较陡，但比手动编写 SVG 路径更友好，适合前端开发者使用。

---

