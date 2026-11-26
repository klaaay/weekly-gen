# [Issue #812: Bundler-free npm imports in the browser — JavaScript Weekly](https://javascriptweekly.com/issues/812)

### [Nudeps：类似打包器的导入，没有那些累赘 • Lea Verou](https://lea.verou.me/blog/2026/nudeps/)

作者发布了一款新的轻量构建工具 Nudeps（可读作 nude deps 或 nu deps）。它让开发者继续用 `npm install` 管理依赖，把依赖本地化后，再用裸标识符（如 `"vue"`、`@floating-ui/dom`）在浏览器中直接导入，无需打包器介入。它的目标是「light-build」而非「no-build」：打包器仍有存在价值，但应更轻、更可组合、更非必需。Nudeps 只处理依赖文件，从不改动用户自己的代码，因此不需要 watcher，也能与任意工具链或静态站点生成器、岛屿架构搭配。背景是打包器要为使用依赖而处理每个文件并引入易泄漏的抽象层，在 State of JS 2025 中「Managing Dependencies」是第 3 大痛点，「Build tools」排第 6。

- 🚀 **正式发布**：作者与学徒 Dmitry 于 2 月完成 MVP，经多项目测试后发布 Nudeps：保留 `npm install` 的依赖管理方式，把依赖 vendor 到本地，再通过裸标识符在浏览器导入，不再需要打包器。
- 🧩 **核心机制**：以已进入 Baseline Widely Available 的 import maps 为基础，底层复用 JSPM 的依赖图追踪引擎并做了大量改动，生成 import map 注入脚本；由于 import map 目前必须内联，改用一个小脚本模拟外部 import map。
- ⚙️ **使用方式**：运行 `npx nudeps install` 完成一次性配置：加入 `devDependencies`，并在 `package.json` 添加 `dependencies` 与 `prepare` 脚本，使每次 `npm install`/`npm uninstall` 或新克隆后自动重跑；页面只需在所有导入依赖的脚本之前加入 `<script src="/importmap.js"></script>`，无需 watcher。
- 📦 **产物组织**：把 `node_modules/` 中必要文件复制到 `client_modules/`（部署但不提交，自带 `.gitignore`，每次安装重新生成），目录名带版本号如 `vue@3.5.45`，提升去重与缓存粒度；生产环境可用 `prune` 只保留实际用到的 specifier，开发环境收录全部则 import map 只在依赖变化时更新。
- 🌐 **兼容范围**：支持动态 `import()`、`import.meta.resolve()`、本地包、npm 别名、git 依赖与实验性 npm workspaces；CJS-only 包如 `lodash` 通过内置的微型 `require()` shim 运行，jQuery 演示还能借 npm 别名并存两个版本；Vue、React、D3、gsap、Lit、Three.js、Floating UI、interact.js、Underscore 均可用。
- 🎨 **非 JS 依赖**：Open Props、Bootstrap Icons 等可通过真实 URL 使用，因为浏览器尚不支持用 specifier 引入 CSS 样式表；这类包因此不能使用其他依赖（除非自己打包）。Nudeps 会创建符号链接或在不可用时重定向，提供 `client_modules/open-props/` 这类无版本 URL。
- 🧠 **Agent 友好**：早期测试中 Claude 基本能正确理解，只做了多余但无害的操作，例如重复写 `.gitignore`、手动运行 `npx nudeps` 或误加 `npm run build` 脚本、添加不必要的配置覆盖；现在包内附带 `SKILL.md`，指示 agent 使用后这些问题消失。
- ⚠️ **当前限制**：不转换用户代码，JSX、TypeScript、Svelte 仍需各自的编译工具；目前仅支持 npm；CJS 支持高度实验性，依赖 `process.env` 等 Node API 的包需要 stub 或对该包单独打包；小模块众多的包首次加载可能更慢；Workers 不支持 specifier（whatwg/html#8173）；尚无基准测试数据。
- 🗓️ **后续计划**：路线图首位是支持 pnpm、yarn 等其他包管理器和测试更多包以确认兼容性、发现边缘情况，此外还有 bug 修复；作者希望 Nudeps 是迈向更轻、更可组合构建工具的第一步。

### [Nudeps 演示](https://nudeps.dev/demos/)

总结失败：模型未返回符合格式的摘要。

### [Meticulous AI - 无需编写测试的自动化前端测试](https://www.meticulous.ai/?utm_source=javascript+weekly&utm_medium=newsletter&utm_campaign=26q4_2&utm_content=primary)

Meticulous 提供面向复杂代码库的自动化端到端视觉回归测试方案，通过可选录制开发、预发和预览环境中的用户及智能体会话，由 AI 生成持续演进的测试套件，并在 PR 中汇总代码变更对既有用户流程和新功能行为的影响，供开发者与智能体在合并前迭代；其基于 Chromium 的确定性调度和并行计算集群旨在消除 flaky 测试并缩短反馈时间。

- 🎯 **产品定位**：宣称以零开发者投入实现自动、穷尽、确定性的验证，让交付速度匹配智能体编写代码的速度，并面向全球最复杂代码库；页面称已有 100+ 组织使用。
- 🧩 **会话录制**：可选择在本地开发、staging 和 preview 环境添加脚本标签记录用户及智能体会话以增强覆盖，也可仅依赖智能体生成的会话；提供 NextJS、React、Vue、Angular、Nuxt、SvelteKit 接入示例。
- 🧠 **AI 生成测试**：AI 引擎跟踪实际执行的代码分支，持续演化视觉端到端测试套件，目标是覆盖代码库每一行、每个用户流程和每个边缘情况。
- 🔄 **PR 影响预览**：在每次 pull request 上发布评论，按边缘情况拆分预览对现有工作流的影响和新功能行为；智能体可看到类似视图，并在代码提交评审前继续迭代。
- ⚙️ **测试自动演进**：新功能或边缘情况出现时自动增加测试，过时测试自动移除，开发者无需编写、修复或维护测试，测试套件随应用演进保持最新和完整。
- ⚡ **确定性与速度**：基于 Chromium 构建确定性调度引擎以从底层消除 flaky，并在计算集群上高度并行执行，声称可在 120 秒内测试数千个屏幕并返回结果。
- 🔗 **兼容与替换**：可与现有测试套件配合使用，也可完全替换；接入方式包括脚本标签和 `@alwaysmeticulous/recorder-loader`，用于在非生产环境启动录制。

### [jQuery 4.1.0 与 3.8.0 发布：薪火相传 | jQuery 官方博客](https://blog.jquery.com/2026/11/17/jquery-4-1-0-and-3-8-0-released-passing-the-torch/)

2026 年 11 月 17 日，jQuery 发布 4.1.0 与 3.8.0:4.1.0 延续 4.x 活跃开发，带来 AJAX transport 回调、jqXHR responseURL、选择器安全与性能、XML/CSS、表单关联自定义元素序列化等改进；3.8.0 作为 3.x 最后一个计划内功能版本，集中交付待处理修复和弃用提醒。此后 3.x 仅接收关键安全与缺陷修复，官方建议借助升级指南和 jQuery Migrate 迁移到 4.x。

- 🚀 **正式发布**：两个版本均通过 jQuery CDN 和 npm 提供完整版与 slim 构建；3.8.0 是 3.x 最后计划内的功能版本，不是 3.x 回归，后续只处理关键安全与 bug 修复。
- 🧩 **AJAX 回调**：自定义 AJAX transport 的 completeCallback 除原有位置参数外，现可接收单个对象 { status, statusText, responses, headers }，便于未来新增字段和按需提供参数；4.1.0 已利用该机制暴露 responseURL。
- 🛡️ **选择器安全**：修复标识符匹配正则的 ReDoS：长链十六进制转义后接非法字符可触发灾难性回溯并卡住页面；生产实现按规范排除数字和十六进制字符，并将选择器中的非法转义解码为 U+FFFD。
- 🔗 **responseURL**：jqXHR 新增 responseURL，表示浏览器跟随重定向后的最终请求 URL；仅当 transport 可报告时设置，现代浏览器 XHR 支持，IE 11 与 script、JSONP transport 不支持。
- 📦 **表单序列化**：.serialize() 和 .serializeArray() 现在正确序列化 formAssociated = true 的表单关联自定义元素，改为信任 form.elements 中的可提交元素，而非按标签名过滤。
- 🎨 **XML CSS**：在非 XHTML XML 文档中，内部改用 createElementNS 与 XHTML 命名空间，修复 document.createElement 生成元素无 style 属性而导致 .css() 等 CSS 方法失效的问题。
- ⚡ **选择器内部**：全面改用 querySelectorAll，弃用 getElementsByTagName 和 getElementsByClassName，获得静态列表并修复 MathML 小写标签、文档片段前导组合符、含点等少见符号标签名等问题；快速路径更严格，qSA 抛错时回退到常规选择。
- 📈 **uniqueSort**：jQuery.uniqueSort 去重改为单遍双指针压缩，从 O(N²) 时间与 O(N) 额外空间降至 O(N) 时间和常数空间，行为与顺序不变。
- 🗓️ **3.x 收尾**：3.8.0 支持 hidden 属性的 until-found 值，.attr 会按原值设置；这修复了 3.x 布尔属性归一化覆盖该值的问题，4.x 因已调整布尔属性处理无需改动。
- ⚠️ **弃用提醒**：3.8.0 正式弃用 jQuery 原型上的 push、sort、splice 以及 jQuery.expr 的伪类入口和 jQuery.expr.filters，分别建议改用 [].push.call($elems, elem) 与 jQuery.expr.pseudos；jQuery Migrate 可在升级前给出警告。
- 🔧 **回移修复**：3.8.0 纳入多项 4.0.0 已发布修复：.html() 支持自移除脚本、jQuery.cleanData 清理时不再跳过元素、表格 <col> 元素尺寸、leverageNative 原生事件处理更健壮，以及 CSS zoom 和初始隐藏 iframe 下的支持测试修复。

### [State of JavaScript 2025：其他工具](https://2025.stateofjs.com/en-US/other-tools/)

本期汇总 JavaScript 生态调查中开发者常用工具与技术的排名和变化：Zod 在库类别居首，Chart.js、Bun、Vercel、Cursor、pnpm 等表现突出，AI 编程工具使用普遍；调查还覆盖运行时、托管与边缘函数、移动桌面框架、非 JavaScript 语言及希望 JS/TS 引入的语言特性，反映生态在类型校验、AI 辅助编码、边缘计算和 Monorepo 工具上的采用趋势。

- 🚀 **库与日期处理**：Zod 以 5,241 名使用者居首且排名上升 2 位，文中称其同比增长明显；Lodash 4,265、date-fns 4,182、Moment 2,664、Day.js 2,629、RxJS 2,194 紧随，文中提到 Temporal 浏览器支持改善后日期库格局可能变化。
- 🎨 **图形与动画**：Chart.js 作为官方选项进入图形与动画类后成为排名最高的具体库（3,045，+0.20）；选择 None 的受访者为 3,115，Three.js 2,472、D3 1,947 次之。
- ⚙️ **常用工具**：ESLint 9,697 与 Prettier 9,295 居前，nvm 6,218、Babel 3,535 随后；Biome 1,762（+0.28）和 oxlint 123（+0.26）显示新兴工具关注度。
- 🏢 **JavaScript 运行时**：Node.js 10,062（+0.30）和 Browser 9,682（-0.19）居前，Bun 2,321（+0.67）第三；Service Workers 1,660（+0.29）、Cloudflare Workers 1,294（+0.53）、Deno 1,244（+0.32）也进入前列。
- 🌐 **托管与边缘**：托管服务中 AWS 5,099 居首，Vercel 4,703 第二，GitHub Pages 4,541、Netlify 3,180、Cloudflare 3,041（+0.64）；边缘/无服务器运行时中 AWS Lambda 2,532（+0.57）领先，Cloudflare Workers 1,702（+0.64）和 Vercel Functions 1,608（+0.49）次之，None 为 4,292。
- 💻 **编辑器**：VS Code 9,186 居首但变化为 -0.17，Cursor 2,797 第二，WebStorm 2,238、Vim 2,195、Zed 1,387、Windsurf 477；Cursor 的排名得益于 AI 辅助编码定位。
- 🧠 **AI 编程工具**：ChatGPT 6,519 居首，GitHub Copilot 5,584、Claude 4,845、Google Gemini 3,074、Cursor 2,829 紧随；None 991，DeepSeek 916、v0 896、Perplexity 802、JetBrains AI 788。
- 📱 **移动与桌面**：None 5,127（-0.50）仍是最大选项，具体框架中 React Native 2,212（+0.47）领先，Electron 1,746（+0.42）、Expo 1,513（+0.43）、Tauri 978（+0.34）值得关注。
- 📦 **Monorepo**：pnpm 3,940（+0.28）明显领先，None 3,050（+0.27）第二，npm Workspaces 2,129（-0.19）、Turborepo 1,718（+0.42）、Nx 1,682（+0.31）、bun install 1,123（+0.61）。
- 🔄 **非 JavaScript 语言**：Python 4,319（+0.16）居首，PHP 2,808（-0.23）、Bash 2,316（+0.22）、Java 2,223（+0.21）、Go 2,143（+0.19）、C# 2,009（+0.26）、Rust 1,682（+0.34），None 1,461（-0.16）。
- 💡 **语言特性诉求**：Pattern matching 620（+0.58）是最希望 JS/TS 引入的特性，Static typing 387（+0.22）、Error handling 123（+0.17）、Standard Library 102、Enums 96（+0.21）、Structs 53（+0.31）。

### [2026 年 11 月网站 jQuery 使用统计与市场份额](https://w3techs.com/technologies/details/js-jquery)

W3Techs 于 2026 年 11 月 24 日发布的统计显示，jQuery 仍是使用最广泛的 JavaScript 库之一：在已知 JavaScript 库的网站中占 84.7%，相当于全部网站的 62.7%；版本主要集中在 `3`，同时保留历史趋势、市场位置和典型站点示例，反映大量存量网站和大型站点仍在使用 jQuery。

- 🚀 **覆盖规模**：jQuery 被 84.7% 的已知 JavaScript 库网站使用，占全部网站的 62.7%，统计日期为 W3Techs 2026 年 11 月 24 日。
- 🧩 **版本分布**：在使用 jQuery 的网站中，版本 `3` 占 79.0%，版本 `1` 占 16.8%，版本 `2` 占 4.2%，旧版本仍有一定存量。
- 📊 **趋势与市场**：页面提供 jQuery 使用比例的历史趋势，并与其他主流 JavaScript 库按流行度和流量对比市场位置，另有专门趋势与市场报告。
- 🌐 **典型站点**：Microsoft.com、Pinterest.com、Yahoo.com、Adobe.com、Wordpress.org、Samsung.com、Digicert.com、Archive.org 等站点使用 jQuery，部分用于子域名或内页；LinkedIn、Pinterest、Dropbox、Canva、Amazon.co.uk 被列为近期使用示例。
- ⚙️ **统计口径**：84.7% 是按 W3Techs 已知 JavaScript 库的网站计算，不是全部网站比例；全部网站中的比例为 62.7%，相关报告每日更新。

### [DevTools 新功能 - 2026 年 12 月 | 博客 | Chrome for Developers](https://developer.chrome.com/blog/new-in-devtools-december-2026#sources_original_scopes_view_stack_traces_and_expression_evaluation_with_ecma-426_source_map_scopes)

Chrome DevTools 2026 年 12 月版汇总了 Chrome 157 与 Chrome 158 在 11 月稳定版中落地的更新，重点覆盖面向编码代理的 DevTools MCP 服务器、AI 辅助 Lighthouse 审计、Elements 与 Sources 调试能力、Application 和性能内存分析，以及无障碍与日常使用体验改进。

- 🚀 **MCP 调试与认证**：Chrome DevTools MCP server 从 v1.11.0 升级到 v1.13.0，新增 `set_logpoints` 在已提供脚本 URL 或经 source map 映射的文件路径注入 logpoint，并以原始变量名把表达式输出到 `list_console_messages` 而无需暂停执行；`configure_webauthn` 可配置虚拟 `ctap2` 或 `u2f` 认证器，用于测试 passkey 和安全密钥流程；`--watchConfig` 支持热重载 `blockedUrlPattern` 与 `allowedUrlPattern` 等配置，也可自动发现工作区标准位置的配置文件。
- 🧪 **MCP 分析与并行**：同一 MCP 服务器还支持离线分析 `.heapsnapshot`、用 `analyze_heapsnapshot_contexts` 检查 V8 执行上下文保留的内存，并默认分页堆快照查询及 `compare_heapsnapshots` 差异且按 self size 排序类对象；独立工具调用和不同页面的页面级工具可并行执行，默认以设备像素分辨率录制浏览器驱动的 screencast，`lighthouse_audit` 可内联返回失败审计和受影响 DOM 节点，`performance_start_trace` 支持 `ignoreCache`，还可从本地文件执行脚本、让 `wait_for` 只匹配可见文本并调试第三方开发者工具中暴露的 WebMCP 工具。
- 🧠 **AI 辅助审计**：AI assistance 可按请求运行覆盖性能、无障碍、最佳实践和 SEO 的完整多类别（`all`）Lighthouse 报告，以及 `agentic-browsing` 审计；报告上下文会向 AI 提供失败审计标题和分数的结构化摘要，单类别报告内联显示分数仪表。
- 🎨 **Elements 增强**：Elements 面板可强制 `<video>` 和 `<audio>` 的 `:buffering`、`:stalled` 伪类，以便不限制网络条件测试加载与播放回退样式；`position-try-fallbacks` 声明新增交互式色块以强制单个回退选项，`position-area` 可视化编辑器可配置 `justify-self` 和 `align-self`，悬停定位属性或 DOM 节点会在视口覆盖层高亮 IMCB；Styles 还识别 `::highlight(*)`，并在 `!important` 优先级中遵循 `@layer` 与来源顺序。
- 🔍 **Sources 作用域**：Sources 支持 ECMA-426 source map scopes 提案，调试暂停时 Scope 面板重建原始词法作用域树并显示未压缩变量名和值；整个 DevTools 的堆栈跟踪解析原始函数名、合并 outlined helper 帧并过滤编译器生成帧，Step、Step over 和 Step out 可逻辑跳过内联和外联函数，Console、Watch Expressions、条件断点或 logpoint 可用原始变量名求值并获得补全。
- 📦 **Application 检查**：Application 新增 Sub apps 节点，以结构化数据网格显示 Sub apps 和 Sibling sub apps，Manifest > Identity 展示 Isolated Web Apps 的 Bundle ID 和 Parent app name；选择 Frames 中的框架可查看已注册的拼写检查自定义词典；Clear site data 现在同时清除 File System 存储，Local Storage 和 Session Storage 在框架加载完成后可靠重取存储键，Issues 标记无用户手势的 geolocation 权限请求，Ads 面板区分主展示广告与广告相关 DOM 高亮。
- 📈 **性能与内存**：Performance 与 Memory 面板通过 trace 引擎优化让大型 trace 解析速度约提升 26% 并降低峰值内存，同时优化火焰图画布重绘、在 Treemap 去重脚本大小；Lantern 模拟会重置连续请求间的 HTTP/2 overflow 字节、将 HTTP/3 连接视为多路复用并计入 ES module 编译与求值事件；堆快照上下文分析识别挂起的 generator 和 async function 为存活闭包、忽略已完成 ES module 的顶层函数，并将 ScopeInfos 归属父脚本和限制实时堆时间线统计到活动录制视图。
- 💬 **网络、控制台与截图**：Network 的 WebSocket Messages 标签为非 ASCII 文本帧计算准确 UTF-8 字节长度，网络搜索先查缓存响应体，请求负载参数的 Copy value 与显示值一致且仅在文本截断时显示 Show more；Console 选中复制只包含可见文本并保留可展开对象预览，长错误字符串不再显示为 `[object Object]`；设备截图会复制到剪贴板并通知，Fit to window 选择最大适配比例，显式设备缩放跨页面刷新保持。
- ♿ **无障碍改进**：无障碍改进包括在 Accessibility 实时公告表中点击 `ariaNotify` 公告可跳转到 Sources 中的 JavaScript 调用点，右键可定位 Elements 或 Accessibility 树中的关联节点，并可用拖动分隔条调整面板大小；Quick Open、数据网格表头和工具栏下拉菜单的键盘焦点轮廓对比度提升；Settings 增加 combobox 自动补全语义和无障碍名称，Service Workers 更新时间行暴露可展开按钮语义，Recorder 改进步骤选择焦点与代码视图地标。
- 📚 **Modern Web Guidance**：Modern Web Guidance 已稳定，可帮助编码代理通过指南使用平台最新特性；11 月新增 content-first-noise-reduction 指南，并更新 accessible-generated-content、faster-spa-view-transitions 和 cpp-on-the-web。

### [获取失败](https://github.com/tc39/ecma426/blob/main/proposals/scopes.md)

无法总结：获取内容失败，状态码 429。

### [agendas/2026/11.md 位于 main 分支 · tc39/agendas · GitHub](https://github.com/tc39/agendas/blob/main/2026/11.md)

Ecma TC39 第 117 次会议定于 2026 年 11 月 30 日至 12 月 3 日远程举行，每日 10:00—15:00 EASST（Pacific/Easter），预计会议容量 16:00h；议程覆盖 ECMA262/402/404/Test262 与任务组报告、多项 Web 兼容性与共识 PR，以及从 Stage 0 到 Stage 4 的提案推进和调度约束。

- 🗓️ **会议安排**：Ecma TC39 第 117 次会议于 2026-11-30 至 2026-12-03 远程举行，每日 10:00—15:00 EASST（Pacific/Easter），预计会议容量 16:00h，参会信息见 Reflector issue 591。
- ✅ **提案截止与排序**：提案推进截止为 2026-11-20 10:00 Pacific/Easter，调度约束截止为2026-11-27 10:00；Stage 4 须链接 spec PR，Stage 2/2.7/3/4 等需提前附支持材料，提案项按 stage 降序、timebox 升序、插入日期排序。
- 📊 **组织与报告**：议程包含主席开场与行为准则、秘书报告（15m，Samina Husain）、ECMA262/402/404/Test262 编辑报告，以及 TG3 安全、TG4 Source Maps、TG5 编程语言标准化实验和 CoC 委员会更新。
- ⚙️ **Web 兼容与共识 PR**：将处理多项 Needs Consensus PR：放宽 HostGetSupportedImportAttributes 返回列表身份要求、移除 yield*返回路径中的双重 await、接受 WSpace 作为 Unicode White_Space 别名、长度为 1 时跳过 Array.prototype.sort 的索引[[Has]]/[[Get]]/[[Set]]、BuiltInRegExpExec 的 Web 现实与规范缺陷、Atomics.notify 中的 RevalidateAtomicAccess。
- 🐛 **兼容性遗留修正**：继续讨论 Un-Annex-B String.prototype.substr（30m，PR）和 async generator 中 yield nonthenable 快速路径（45m，PR/slides），并处理上一会议溢出项。
- 🚀 **Stage 3 提案**：Stage 3 议程包括 Import defer 在循环与 top-level await 下的缺陷（PR tc39/proposal-defer-import-eval#97）、Import Text 争取 Stage 4（需 spec PR）、Thenable Curtailment 基于实现反馈的规范性 PR #22 和#26。
- 🔄 **Stage 2.7 提案**：Stage 2.7 讨论 Export defer 解析破坏性变更（issue tc39/proposal-deferred-reexports#98）、JSON.parse Options 重命名 preferNullPrototype（PR#27）、ESM Phase Imports 从 transfer-gated 改为 import()-gated 安全模型（PR tc39/proposal-esm-phase-imports#65），以及Immutable ArrayBuffers 争取 Stage 3。
- 🧩 **Stage 2 提案**：Stage 2 议程含 Error code property 争取 Stage 2.7、Intl Sequence Units 更新、Math.fusedMultiplyAdd 争取 Stage 2.7、eraDisplay/yearStyle 更新，以及 Composite sorting 讨论（60m）。
- 🧪 **Stage 1/0 提案**：低阶段提案包括 AbortController（Cancellation）争取 Stage 2（slides/spec draft）、Iterator transfer、Trim Specific Characters 争取 Stage 1 或 2、Intl Supported Time Zone Options 争取 Stage 1、Bitwise counting 争取 Stage 1 或 2。
- 💡 **开放讨论**：另设 45m 讨论 Making spec.html executable（James M Snell/Dan Carney），以及 timeboxed 议程溢出按插入顺序处理。
- ⚠️ **调度限制**：Nicolò Ribaudo 周四不可用；Jordan Harband 在 11:30 前和周四大部分时间不可用，并希望参加 Thenable Curtailment、Error code property、Math.fma 和 Iterator transfer；Eemeli Aro 每日 13:00 后不能演讲且周四全天不可用；James Snell 在 12 月 3 日不可用。

### [GitHub - tc39/proposal-import-text：一项用于导入文本的 TC39 提案 · GitHub](https://github.com/tc39/proposal-import-text)

TC39 的 proposal-import-text 已进入 Stage 3，目标是在 JavaScript 中像导入 JSON 或原始字节一样方便地导入文本文件。提案为 import attributes 增加 type: "text"，让文件直接以字符串形式导入；这意在简化常见操作并提升性能，同时与 Import Bytes、HTML、Fetch、CSP 等相关规范改动协同推进。

- 🧭 **提案状态**：proposal-import-text 处于 Stage 3，champion 为 Eemeli Aro，reviewers 为 Jordan Harband 和 Nicolò Ribaudo；2025 年 11 月曾面向 Stage 1/2/2.7 展示，2026 年 3 月面向 Stage 2.7/3 展示。
- 🎯 **动机与用例**：导入文本与导入 JSON 或原始字节一样有用，应同样简单；这能让相对常见的操作更简单、更高效，例如导入 YAML 文件后交给用户库解析。
- 🧩 **核心机制**：提案新增 `'text'` 作为 `type` import attribute 的取值，可用 `import text from "path/to/file.txt" with { type: "text" }` 将文件导入为字符串，且不提供在 JavaScript 中指定编码的能力。
- ⚠️ **编码限制**：若需要指定编码，必须改用 Import Bytes 提案的 `type: "bytes"` 导入为 `Uint8Array`，再用 `new TextDecoder("utf-16le").decode(uint8array)` 等方式显式解码；Import Bytes 已到 Stage 2.7，可能继续推进。
- 🔄 **替代与现状**：Fetch API 也能加载文本，但操作总是异步、相对路径以文档 base URL 而非模块路径为基准、且只在 JavaScript 执行时才开始 fetch；现有 import attributes 已支持 JSON，Deno 和 Bun 等服务器端实现也支持 `type: "text"`。
- 🔗 **规范联动**：提案涉及 HTML Standard、Fetch Standard、Content Security Policy、WinterTC Minimum common web API 的配套改动，并在 test262 与 web-platform-tests 中补充测试。

### [GitHub - tc39/proposal-immutable-arraybuffer：一项关于不可变 ArrayBuffer 的 TC39 提案 · GitHub](https://github.com/tc39/proposal-immutable-arraybuffer)

TC39 的 proposal-immutable-arraybuffer 目前处于 Stage 2.7，拟为 JavaScript 的 ArrayBuffer 增加不可变缓冲区能力：新增 immutable 只读访问器和 transferToImmutable、sliceToImmutable 方法，使缓冲区内容不可修改、不可分离、不可调整大小，从而支持将冻结的 ArrayBuffer、DataView、TypedArray 放入 ROM，并服务嵌入式系统、零拷贝 API 与 OCapN 字节数组等场景。

- 🧭 **提案状态**：该提案为 TC39 Stage 2.7，README 记录从 stage 1 到 stage 3 take 1 的全会演示历史，规范地址为 tc39.es/proposal-immutable-arraybuffer。
- 📚 **背景基础**：可调整大小 ArrayBuffer 和 transfer 系列已到 Stage 4，ArrayBuffer.prototype 现有 transfer、transferToFixedLength、resize、slice 及 detached、resizable、byteLength、maxByteLength，但都无法创建不可变缓冲区。
- 🛠️ **新增 API**：增加 immutable: boolean 只读访问器；transferToImmutable(newByteLength?: number): ArrayBuffer 将原缓冲区内容移入新不可变缓冲区并分离原缓冲区；sliceToImmutable(start?: number, end?: number): ArrayBuffer 从原范围创建不可变缓冲区并便于实现减少甚至消除复制。
- 🛡️ **不可变约束**：不可变缓冲区不能被分离、调整大小或再次 transfer，maxByteLength 等于 byteLength；以其为 backing store 的 DataView 或 TypedArray 可被冻结并保持不可变。
- 🎯 **动机与用例**：面向 Moddable XS 等嵌入式系统将大量固定数据放入 ROM；接受 ArrayBuffer 的 API 可避免防御性复制；OCapN 需要不可变批量二进制容器；示例用 transferToImmutable 构造冻结的 netstring Uint8Array。
- 🔄 **与现有操作**：ArrayBuffer.prototype.slice 及 TypedArray 的 filter、map、slice、toReversed 等不保证保留不可变性，类似不保证保留可调整大小；HTML structuredClone 不可转移但克隆会保留不可变性和底层数据块。
- 🧪 **实现进展**：提供 endo immutable-arraybuffer polyfill/transpiler；原生实现 tracking issues 计划加入 JavaScriptCore、SpiderMonkey、XS、V8。
- 💬 **设计问答**：不可分离因会对 backing TypedArray/DataView 产生可观察变化；TypedArray 索引属性不应改为 configurable/writable；未规定 sliceToImmutable 必须零拷贝但使其可行；getter 命名 immutable 以默认 false 便于特性检测；在无其他决定因素时倾向抛错而非静默。

### [GitHub - tc39/proposal-cancellation：ECMAScript 取消 API 提案 · GitHub](https://github.com/tc39/proposal-cancellation)

TC39 的 ECMAScript Cancellation 提案处于 Stage 1，目标从另立取消机制转为把 WHATWG `AbortController` 与 `AbortSignal` 的待定子集引入 JavaScript，并完成规范工作，使 JavaScript 规范及其他规范可直接使用 `AbortController` 而无需 `EventTarget` 等配套机制；已提供 `AbortController` 的平台预计仅需少量扩展，提案同时整理了取消请求而非结果、异质取消、智能取消、竞态与尽力而为、关注点分离和瞬时清理等架构原则。

- 🧭 **Stage 1**：ECMAScript Cancellation 提案当前为 Stage 1，champions 为 Ron Buckton（@rbuckton）、James M. Snell（@jasnell）、Kevin Gibbons（@bakkot），作者为 Ron Buckton 与 Kevin Gibbons。
- 🎯 **目标调整**：提案不再标准化不同的取消机制，转为引入 WHATWG `AbortController` 和 `AbortSignal` 的待定子集，并完成必要规范工作，让包括 JavaScript 规范自身在内的规范能使用 `AbortController`，而无需 `EventTarget` 等其余机制。
- ⚠️ **平台影响**：已提供 `AbortController` 的平台上的开发者预计不受影响，但可能需要少量扩展，且这些扩展会包含在相应平台中。
- 💡 **动机与场景**：目标是提供清晰一致的异步操作取消方式，并作为通用协调机制，支持同步观察（如游戏循环）、异步观察（如网络请求）、在 async 函数中易用，以及跨 Browser、NodeJS、IoT/embedded 等宿主环境复用。
- 🧩 **取消请求而非结果**：Promise 类似异步对象引用，可能被返回或传递给多个客户端；对 Promise 调用取消类似删除对象引用，容易被其他使用方误用且不可靠，因此应取消请求而不是结果。
- 🔗 **异质取消**：一次取消往往需要影响多个不同层次、彼此无关的活动。例如用户在大增量查询看到少量结果后点停止，应终止后续 fetch 并关闭连接、停止后台结果处理和未渲染内容渲染、停止“加载更多”动画并显示“user cancelled”；各活动可接收同一个 `cancellationToken` 来一致响应。
- 🧠 **智能取消**：库可智能决定取消方式：异步查询结果已从服务器返回时，可能更适合完成解析和缓存而非直接丢弃；券商系统获取最新数据的往返昂贵，已启动并返回的结果可放入本地缓存；已派生 worker 时，让其完成以复用可能比强行终止更高效。
- ⚡ **竞态与尽力而为**：异步系统中取消信号要追赶已启动的计算，部分任务可能选择完成或继续派生工作，因此取消并不及时且“has cancellation finished?”不是良定义状态；取消最多是 best efforts，语义是“不再关心是否完成”，而非“阻止完成”。
- 🛡️ **关注点分离**：取消源通常不是被取消对象之一；库不应因关心同一取消事件而取消无关的服务器查询。取消 token 与取消源的分离类似 Promise 与其 resolver 的分离。
- 🔄 **瞬时清理**：任务推进时清理动作可能变化；例如数据表滚动请求更多结果时，有未完成查询时的取消行为可能与当前页所需内容已全部展示时不同，因此 `register` 方法返回可注销动作的能力。

### [Ladybird](https://ladybird.org/)

Ladybird 是由 501(c)(3) 非营利组织支持、从零构建的独立浏览器引擎，2026-11-23 面向 macOS 和 Linux 发布首个 alpha，强调不受现有引擎和商业利益控制；项目以 C++ 为主并逐步迁移到 Rust，当前仍不适合作为日常浏览器，Windows 和移动端支持尚未完成。

- 🚀 **首个 Alpha**：2026-11-23 发布 macOS 和 Linux 的 alpha 构建，面向愿意报告 bug 的早期采用者；官方明确它还不能替代日常浏览器。
- 🧩 **独立引擎**：Ladybird 是从零编写的新浏览器引擎，不是 Chromium、Gecko 或 WebKit 的分支，也不使用 Blink、WebKit、Gecko 等引擎代码；常见功能使用第三方库，包括其他浏览器也会用的图像、音视频、加密和图形库。
- 🏢 **非营利与无变现**：项目由 501(c)(3) 非营利组织支持，资金来自无限制捐赠和赞助，赞助商不能购买董事会席位或影响技术路线；官方承诺不做默认搜索交易、加密代币或其他用户变现。
- ⚙️ **C++ 与 Rust**：代码库起源于 SerenityOS 的 C++ 项目，现采用 Rust 作为 C++ 的后续语言，并逐步将子系统移植到 Rust。
- 🌐 **平台范围**：当前全职工程重点在 macOS 和 Linux；Windows 的 CI 已能构建和测试 JavaScript 引擎，完整浏览器引擎支持稍后推进，移动端 Android 和 iOS 也要等桌面版成熟后再投入。
- 🧪 **近期引擎能力**：2026 年 10 月月报提到 JavaScript 繁忙时仍可运行的 CSS 动画和悬停、JavaScript JIT、新 WebAssembly 引擎和重新设计的 UI；此前还出现 Twitch/YouTube 视频、CSS scroll snap、JavaScript 调试、会话恢复、隐私浏览、浏览器配置、地理定位、WebAudio 和硬件视频解码等进展。
- 🛡️ **安全与性能**：9 月与 Trail of Bits 进行安全加固，并处理高成本的空闲页面；6 月涉及下载管理、沙箱、浏览历史、DevTools 存储检查、媒体播放速度和 GPU 隔离，9 月还加入硬件视频解码和更平滑动画。
- 🛠️ **开源协作**：Ladybird 免费且开源，由小型全职团队公开开发，社区可通过提交 bug、创建最小复现、测试网站、报告安全问题和技术反馈参与；代码可从 GitHub 克隆，并用 `./Meta/ladybird.py run` 在本地运行。

### [Ladybird 现已进入 Alpha 阶段 - Ladybird](https://ladybird.org/posts/alpha/)

Ladybird 于 2026 年 11 月 23 日发布 alpha 版，面向 macOS 和 Linux 提供下载；其核心是团队从零自研、并非分叉的浏览器引擎，浏览器外壳相对简洁但可用。此次 alpha 以滚动更新方式推进，并开放站点兼容性、崩溃与安全问题的反馈渠道，意味着更多用户无需从源码构建即可体验和参与测试。

- 🚀 **Alpha 发布**：Ladybird 进入 alpha，macOS 与 Linux 用户可下载体验；浏览器外壳相对简洁但功能可用。
- 🧩 **自研引擎**：引擎由团队从零构建，不是对其他浏览器引擎的分叉。
- ⚠️ **Alpha 限制**：部分网站无法正常工作，且浏览器有时会崩溃；用户可在浏览器内报告损坏站点，崩溃后可查看报告并决定是否发送，细节见隐私政策。
- 🛡️ **安全测试**：当前不对安全性作承诺，官方邀请安全研究者攻击并反馈利用方式，以便后续加固。
- 🔄 **滚动更新**：alpha 是滚动通道，将定期推送自动更新；此前用户需从源码构建才能看到改进。
- 🛠️ **开发者测试**：网站开发者可测试兼容性并反馈问题；支持 `WebDriver` 自动测试及 Firefox DevTools 协议。

### [Ladybird 首个 alpha 版本发布](https://simonwillison.net/2026/Nov/23/ladybird/)

2026 年 11 月 23 日，Ladybird 发布首个 alpha 版，首次提供 macOS 和 Linux 可安装包，用户无需自行编译；这个独立浏览器项目自研 HTML 解析、CSS 引擎、布局、JavaScript 和 WebAssembly 等关键组件，并在今年大量借助 AI 编码代理推进 Rust 移植、Web 平台测试兼容性和引擎性能优化，但其 alpha 阶段仍存在兼容性、稳定性和安全性限制。

- 🚀 **首个 alpha**：Ladybird 发布首个 alpha 版，提供 macOS 和 Linux 安装包；官方提醒部分网站不可用且可能崩溃，用户可在浏览器内报告故障站点。
- 🧩 **自研浏览器栈**：Ladybird 自研 HTML 解析、CSS 引擎、布局、JavaScript 和 WebAssembly 等关键组件，仍使用 HarfBuzz 文本整形、Skia 2D 图形、ffmpeg 视频和 SQLite，部分代码来自 SerenityOS。
- ⚙️ **多进程隔离**：不同标签页运行在独立进程中；实测打开多个标签页时出现 Hub、Compositor、RequestServer、WebContent、MediaServer 等进程，作者指出多数浏览器采用类似隔离机制，Chrome 实际为 process-per-site。
- 🧪 **兼容性实测**：Simon Willison 测试由 ffmpeg 编译的 WebAssembly 视频压缩、图片缩放和 `Pyodide` REPL 均可运行；`Datasette Lite` 因 service worker 与 web worker 组合报错 `undefined is not a function (evaluated from 'navigator.serviceWorker.startMessages')`，已提交 issue 并在源码发现 FIXME。
- 🛠️ **AI 编码代理**：项目今年大量使用编码代理；2026 年 2 月 23 日 Andreas Kling 称借助 `Claude Code` 和 `Codex`，两周内将 `LibJS` 部分代码从 C++ 移植为 25,000 行 Rust。
- 📈 **WPT 提升**：2026 年 10 月通过让 AI 编码代理针对 `web-platform-tests` 补齐缺失功能，在该约 225 万子测试的套件上新增 75,650 个通过项并超过 Safari；多数增长集中在 10 月 22 日至 27 日，从约 212 万升至 218 万。
- ⚡ **引擎优化**：10 月更新还包括将样式和布局移至独立线程、引入新的 JavaScript JIT，并用新代码替换 C++ `Cranelift` WebAssembly 引擎，在 `JetStream 3` WASM 基准上取得 7 倍提升。
- 🛡️ **安全定位**：官方明确 alpha 阶段不对安全性作承诺，欢迎安全研究者攻击并报告；Simon 不会用其登录 GitHub、Gmail 等敏感账户，仅保留用于匿名浏览和参与测试。

### [Webpack 5.113 | webpack](https://webpack.js.org/blog/2026-11-19-webpack-5-113/)

Webpack 5.113.0 于 2026-11-19 发布，核心是为原生 HTML 页面引入 CSS Modules 作用域类名连接，同时新增 SVG 资源压缩、loader 的 sourceTest 跳过机制、改进 CommonJS tree shaking 与热更新可靠性，并加入 output.allowOutside 等输出控制及多项修复，目标是减少样式冲突、缩小构建产物并提升开发时稳定性。

- 🚀 **版本发布**：发布 webpack 5.113.0，现有项目可通过 npm install --save-dev webpack@5.113.0 升级。
- 🧩 **HTML 内 CSS Modules**：在 HTML 的 <`style module>` 中使用原始类名，webpack 会为 .button 生成作用域名并同步到标记的 class；HTML 可作为 entry，链接的 .module.css 同样生效，未由 CSS Module 声明的类保持不变。
- 🎯 **模块消歧**：多个模块都声明 .button 时，可用 `<style module=card>` 配合 class 中的 card.button 指定模块；作用域 ID 仍会同步到 label、ARIA 引用和页内链接，但 document.querySelector('.button') 等 JavaScript 选择器不会被重写，应改用 data-action 等独立属性。
- 🎨 **SVG 优化**：通过 optimization.minimizeOptions.xml:{} 对输出的 .svg 和 .xml 资源启用优化，缩短数字、颜色和路径数据，移除未使用命名空间并清理不渲染的空白；removeMetadata、precision、cleanupIds 默认关闭，因元数据可能含许可信息、取整会移动点、ID 可能被外部引用，且除 experiments.futureDefaults 外需显式启用，xml:false 可关闭。
- ⚙️ **按需运行 loader**：新增 sourceTest 条件，使匹配 .js 文件的 loader 仅在当前输入满足 /@instrument/ 等条件时执行；检查包含右侧 loader 已做的修改，pitch 函数仍运行，非 UTF-8 输入按正常流程处理。
- 🔄 **CommonJS tree shaking**：exports.answer = 42 这类简单导出不再让未使用模块被视为有副作用，webpack 还能在引用模块无副作用时移除未使用的 require() 调用；执行初始化的模块仍会运行。
- ⚡ **热更新修复**：修复模块在 chunk 间移动或更新需要浏览器尚未加载的 chunk 时热更新中止的问题；新 chunk 加载其样式表、移除的 chunk 移除样式，现有样式表保留属性与 disabled 状态，watch 模式也能发现递归上下文子目录中新加入的文件。
- 📦 **输出路径控制**：output.allowOutside 控制 webpack 在 output.path 之外写入、复制和清理文件：false 限制在输出目录内，绝对目录数组允许指定位置，true 允许任意位置；配合 experiments.futureDefaults 默认 false，否则保持现有行为，即输出目录外的 asset 仍可写入而复制和清理留在目录内。
- 🛠️ **其他改进**：内置 TypeScript 解析改为一次解析且无需额外配置；experiments.cacheUnaffected 可与 optimization.usedExports、optimization.mangleExports 配合；HTML 中 `<style lang=scss> 或 <script lang=ts> 会按对应语言类型供 mimetype 规则匹配，并新增 transport、updateManifest、chunkHashDependencies 等插件钩子；MultiCompiler done 支持异步 tap，同步 .call() 已弃用`。
- 🐛 **问题修复**：修复 WebAssembly 在 runtime chunk 位于子目录或 universal 构建使用完整 hash 时的加载；HTML 对远程资源、编码后的 asset 路径和 <base href> 保持正确 URL，内联资源保留许可横幅；改进 CommonJS 与 ES 模块互操作、CSS 顺序与层/媒体条件、异步收集顺序、@value URL 相对解析和 composes 链。

### [CSS 和 HTML 是内置的 | webpack](https://webpack.js.org/blog/2026-11-16-css-and-html-are-built-in/)

webpack 自 5.109.0 起内置 CSS 与 HTML 处理能力，导入样式表或直接把 HTML 页面作为入口即可完成解析、打包和资源 URL 重写，从而减少对 css-loader、style-loader、mini-css-extract-plugin、html-webpack-plugin 等依赖与配置的需求；生产模式还提供 CSS 压缩和浏览器前缀，现有项目默认保持兼容并可借助 codemod 迁移。

- 🚀 **正式内置**：从 webpack 5.109.0 开始，CSS 和 HTML 无需额外插件即可开箱使用，导入样式表或用 HTML 页面作为入口，webpack 会处理其余工作。
- 🧩 **CSS 处理机制**：导入 .css 文件后，webpack 会解析 @import 和 url()，把 *.module.css 作为 CSS Modules 处理，并为每个 chunk 提取一个 .css 文件，无需 module.rules 或插件。
- ⚡ **生产优化**：在 mode 为 production 时（webpack 5.110.0 或更高版本），webpack 会压缩 CSS；配置 browserslist target 后，还会补充目标浏览器所需的厂商前缀。
- 🌐 **HTML 入口**：可把 src/index.html 作为 entry，webpack 会打包页面引用的脚本、样式和图片，并把 URL 重写为产出的文件；JavaScript 入口项目可用 output.html: true 生成页面并自动关联脚本和样式表。
- 📦 **可移除依赖**：css-loader、style-loader、mini-css-extract-plugin、css-minimizer-webpack-plugin、html-loader、html-webpack-plugin 和 html-minimizer-webpack-plugin 已因内置支持而被标记为弃用，分别由内置 CSS 解析、样式导出、按 chunk 提取 CSS、CSS 压缩与前缀、HTML 导入、HTML 入口或 output.html、HTML 压缩替代。
- 🛠️ **预处理器兼容**：sass-loader、less-loader、postcss-loader 和 Pug 等预处理器或模板引擎仍可配合内置支持使用；保留预处理器 loader，移除其后的 CSS loader，并将规则 type 设为 css/auto，一条规则可同时覆盖全局 SCSS 和 CSS Module SCSS。
- 🔄 **兼容与迁移**：现有 css-loader 和 html-loader 配置继续可用，webpack 默认检测这些规则并关闭对应内置支持，便于按需迁移；CSS 可用 @webpack/css-plugins-to-native-css codemod，HTML 可用 @webpack/html-plugins-to-native-html codemod（webpack 5.112.0 或更高版本），新项目通过 npx create-webpack-app 创建时已使用内置支持。

### [Bun v1.4.5 | Bun 博客](https://bun.com/blog/bun-v1.4.5)

Bun v1.4.5 于 2026 年 11 月 19 日发布，是一次安全版本，修复 HTTP/3、TLS 和 DNS 相关安全问题，并更新 lsquic、c-ares、SQLite、llhttp 与 BoringSSL 等底层依赖；使用相关协议、API 或运行时能力的用户应升级，以获取安全修复和证书/加密行为修正。

- 🛡️ **安全修复**：修复 HTTP/3、TLS、DNS 安全问题，影响 HTTP/3、HTTP/1.1、TLS、DNS、Zstandard 以及 `Bun.serve`、`Bun.connect`、`Bun.dns`、`Bun.zstdDecompress`、`node:tls`、`node:https`、`node:http`、`node:quic`、`node:dns`、`node:zlib`、`fetch`、`DecompressionStream`。
- 📦 **依赖升级**：lsquic 从 4.9.4 升至 4.11.2，c-ares 从 1.34.8 升至 1.34.9，SQLite 从 3.53.4 升至 3.54.1，llhttp 从 9.4.2 升至 9.4.4，BoringSSL 从 2026 年 8 月更新至 2026 年 11 月。
- 🧩 **SQLite 变更**：SQLite 3.54 不再允许 `ALTER TABLE` 添加、重命名或删除名为 `rowid`、`oid` 或 `_rowid_` 的列，并会对 `DEFAULT` 表达式中的函数运行 `setAuthorizer()` 回调；在 macOS 上 Bun 使用系统自带的 SQLite。
- 🛠️ **HTTP/3 稳定性**：修复 HTTP/3 和 `node:quic` 中的多项稳定性问题。
- 🐛 **RSA 签名修复**：修复 `node:crypto` 中使用 SHA-3、SHA-512/224、SHA-512/256 和 RIPEMD-160 的 RSA 签名抛出 `ERR_OSSL_RSA_UNKNOWN_ALGORITHM_TYPE` 的问题。
- ✅ **过期证书**：来自未知签发者的过期证书现在会像 Node.js 一样报告 `CERT_HAS_EXPIRED`。
- ⚠️ **信任链校验**：`allowPartialTrustChain` 配合 `crl` 时，现在与 Node.js 一样要求证书链以自签发证书结束。
- 🔍 **根证书校验**：自定义根证书校验更严格，部分旧根证书会被拒绝；Bun 内置根证书不受影响。

### [发布 v2.0.0 · jimp-dev/jimp · GitHub](https://github.com/jimp-dev/jimp/releases/tag/v2.0.0)

Jimp v2.0.0 发布，这是包含破坏性变更的大版本：最低运行时提升到 Node.js 22，并集中修正像素运算、边界处理、合成、排版、缩放和旋转等行为；同时新增绘制、形态学、动画 GIF/多页 TIFF、SVG/JPEG XL/JPEG 2000/ICO 格式、TrueType/OpenType/WOFF 字体打印、ICC/EXIF、抖动与多种缩放模式等能力，还改善 WASM 在 Node、Cloudflare Workers、Deno 和浏览器中的部署兼容性。

- 🚀 **正式发布 v2.0.0**：Jimp v2.0.0 发布，包含多项 breaking change、增强、修复和文档更新；升级方需要按破坏性变更调整代码和运行环境。
- ⚠️ **Node 22+ 与破坏性调整**：要求 Node.js 22 或更高；移除无效果选项；`setPixelColor` 越界不再绘制边缘像素；`plugin-print` 保留空行；`write()` 选项按扩展名类型化，支持跨 Jimp 类合成并读取 Uint8Array/Blob。
- 🧩 **核心像素与边界修正**：修正 color/threshold/quantize 像素数学、灰度舍入与 luminance；越界区域裁剪；合成结果取整而非截断；修复 blur 半径、resize alpha、autocrop、displace、circle、shadow、compareHashes 及 nearest-neighbour 旋转中心偏移。
- 🎨 **绘制与字体排版**：新增 @jimp/plugin-draw 支持线、形状、路径、渐变和 flood fill；新增 @jimp/plugin-border 的 roundCorners、border、boxShadow；plugin-print 可打印 TrueType、OpenType、WOFF，按码点打印并测量换行、清理 loadFont HTTP 错误。
- 📦 **格式支持扩展**：支持读写动画 GIF 和多页 TIFF；wasm-svg 读取 SVG；wasm-jxl 新增 JPEG XL，wasm-jpeg2000 新增 JPEG 2000；js-ico 读写 ICO；js-bmp 可写 1/4/8-bit BMP；js-png 默认选择最小无损颜色类型并忽略 IEND 后数据。
- 🧪 **算法与滤镜增强**：新增 plugin-morphology 的 erode()、dilate()、open()、close()；支持 skew() 和 affine()；新增 Floyd–Steinberg、Atkinson、Bayer 抖动与 Otsu 自动阈值；color 增加 multiply、sepia(amount)、exposure()、vibrance()；新增 sharpen() 及卷积 divisor/bias。
- ⚡ **缩放性能与正确性**：新增 LANCZOS、LANCZOS2、MITCHELL 缩放模式；加速 BILINEAR、BICUBIC、HERMITE、BEZIER；修复缩放偏移和最后一行/列丢失；新增 premultiplyAlpha 保留透明像素颜色；crop 按整行复制提升性能。
- 🎯 **色彩与元数据**：支持 Display P3 和 ICC 色彩配置；写 JPEG 时可选择保留 EXIF；新增 exifRotate 选项跳过 EXIF 自动旋转。
- 🌐 **WASM 与运行时兼容**：wasm-* 接受预编译 wasm 模块以适配 Cloudflare Workers；Node 下从磁盘加载 codec wasm；wasm-png 使用单线程 oxipng 便于 webpack 5 打包；修复 Deno、Workers 和浏览器无 polyfill 时的 Buffer 问题。
- 🛠️ **输入输出与类型改进**：核心可接受 ImageData、Uint8ClampedArray、Uint8Array 作为位图数据；Jimp#write 接受普通字符串路径；读取文件和 Buffer 时也传递解码器选项；修正 WASM 格式选项的 TypeScript 类型，导出 Edge 和 ColorActionName 运行时值，并说明浏览器文件系统写入失败。
- 🐛 **解码与安全修复**：解码前校验 GIF/TIFF 头；bmp-ts 1.1.0/1.1.2 限制 BMP 解码尺寸并修复 RLE、奇数宽度和 alpha mask；Node 下解码 CMYK TIFF；跳过 JPEG 头间杂散字节并解码缺失 EOI 的 JPEG；拒绝字体目录外的字体页；新增安全策略。
- 📚 **文档与构建更新**：文档站点重设计和 Jimp 2.0 文档、迁移指南、动画 GIF/多页 TIFF 与 plugin-draw 文档更新；升级 Astro 7 和 Starlight 0.43；CI 在 Node 22 运行并缓存 turbo 任务，修复 Windows 构建测试和浏览器 bundle 问题；升级全部依赖。

### [Nuxt 4.7 · Nuxt 博客](https://nuxt.com/blog/v4-7)

Nuxt 4.7 发布，包含自 v4.6.4 以来约 350 次提交，重点提供可试用的 Nitro v3、实验性 WebMCP、统一开发问题面板、模板诊断、服务端错误边界和运行时配置校验，并带来 SSR、水合、构建与依赖体积优化；同时发布 Nuxt CLI 4.1、新增 Rsbuild 构建器并修复三个安全问题。

- 🚀 **版本发布**：Nuxt 4.7 发布，推荐运行 `npx nuxt upgrade --dedupe` 升级，以刷新锁文件并同步 Nuxt CLI 4.1、my-bad v1 和 vite-plugin-checker v1。
- 🧪 **Nitro v3 试用**：将 `nitro` 加入依赖即启用 Nitro v3，无需改配置；它仍是 release candidate 且高度实验性，不应上生产。基准中首页 RPS 从 926 提升到 1,236（+33%），1,000 链接页面从 219 到 316（+44%）。
- 🧩 **兼容层**：Nuxt 4 上 Nitro v3 通过 `nitroLegacy` 兼容 h3 v1、`nitropack`/`#imports` 导入、自动导入、`useRuntimeConfig(event)`、`event.node` 和 v2 hooks；可设 `nitroLegacy: false` 排查依赖。路由规则语法变化，`/blog/*` 也匹配 `/blog/2026/hello`，多通配符需改成命名参数；它也不再回退到 Nuxt 自身依赖，服务端代码导入的包必须列在 package.json。
- 🛠️ **CLI 4.1**：Nuxt CLI 4.1 自行渲染生产构建输出，兼容 Vite、webpack、Rspack、Rsbuild 及 Nitro v2/v3、`@nuxt/vite-server`；`nuxt generate` 展示预渲染路由和部署建议，另有 `nuxt dev --https` HTTP/2、`nuxt module build/prepare` 等。
- 🧠 **WebMCP**：实验性 WebMCP 通过 `experimental.webmcp: true` 开启，用 `@tool` 将模板中的函数暴露给浏览器 AI agent；参数来自模板，受渲染和禁用状态约束，表单工具会真实执行校验和提交处理。还提供 `defineAgentTool()`、`useAgentTool()`、`useAgentActivity()` 和 `navigate` 工具；Chrome 需 flag，不支持时无行为变化。
- 🔍 **问题面板**：my-bad v1 和 vite-plugin-checker v1 将类型错误、ESLint 等检查器结果、Vue 编译器警告及 Nuxt 扫描警告汇总为 problem set，显示在页面角标和抽屉中，可跳转编辑器，Nuxt DevTools v4 也提供 Problems 面板；`typescript.typeCheck` 新增 `'dev'` 选项，避免开发类型检查拖累生产构建。
- 🧭 **模板诊断**：默认检查 `<NuxtLink>` 静态 `to` 无对应页面（`NUXT_B4025`）、在服务端组件上使用 `v-on`/`v-model`（`NUXT_B3014`）以及向服务端组件传函数或类实例（`NUXT_B3015`），可用 `experimental.templateDiagnostics: false` 关闭。
- ⚙️ **错误边界**：`experimental.ssrErrorBoundary` 让 `<NuxtErrorBoundary>` 捕获 SSR 错误，返回 200 并保留页面其余部分，客户端水合到相同状态；生产环境非 HTTP 错误以普通 500 进入插槽。新增 `retry-on-client` 替代已弃用的 `<NuxtClientFallback>`，插槽暴露 `clearBoundaryError`。
- ✅ **配置校验**：`runtimeConfig` 值可使用 Standard Schema（如 Zod、ArkType、Valibot），schema 决定类型和默认值；环境变量在服务启动时转换，缺失或转换失败则启动失败并集中报错。schema 不进入服务端 bundle，而是编译成轻量描述；模块可用 `updateRuntimeConfig()` 声明 schema。
- ⚡ **性能提升**：官方基准显示 starter 安装包 523→473、node_modules 226.9→208.4 MB、服务端输出 2.17→1.23 MB、首屏 80.4 kB/14 请求→66.3 kB/3 请求、SSR 245→292 req/s；1,000 链接页面 SSR 88→218 req/s，约 170 页应用启用 staticRoutes 后 890→1,976 req/s。
- 🎯 **staticRoutes**：`experimental.staticRoutes` 假设路由在构建时固定，服务端只建一次 vue-router matcher，并启用 `early404`；约 170 页基准中 SSR 吞吐从 890 到 1,976 req/s。代价是 `router.addRoute()`、`removeRoute()`、`clearRoutes()` 会抛错，应改用 `pages:extend`。
- 💻 **客户端与水合**：未使用 `$fetch` 时 ofetch 不进入客户端包，未使用 head 时 unhead 也可排除；Nuxt UI 基准首屏请求从 18 个 JS 文件降到 6 个。V8 compile hints 使重 landing page 水合 477→311 ms、TBT 137→40 ms；浏览器可先绘制再水合。
- 📦 **DevTools 按需**：`nuxt` 不再直接依赖 `@nuxt/devtools`，改为内置 `@nuxt/devtools-onboard`；已安装 v3/v4 则加载，否则 `nuxt dev` 显示安装按钮，减小全新安装体积并允许选择版本。
- 🔧 **Rsbuild 构建器**：新增 `@nuxt/rsbuild-builder`，通过 `builder: 'rsbuild'` 使用 Rsbuild 构建客户端和服务端，Vue 走 `@rsbuild/plugin-vue`，CSS 走 Lightning CSS/PostCSS；替代已弃用的 `@nuxt/rspack-builder`，模块可用 `extendRsbuildConfig()` 和 `addRsbuildPlugin()`。
- 🔗 **模块作者**：新增 `addRendererPlugin`，让模块挂到 renderer 而非特定 server，兼容任意 server builder；旧版 Nuxt 上会注册为 Nitro 插件。另有 `render:document` 钩子在非流式响应 HTML 完成、所有 `render:html` 监听器后调用。
- 🛡️ **安全修复**：修复三个安全问题：`_payload.json` 通配路由规则可能导致用户页面数据被缓存给他人（中危）；catch-all 路由编码斜杠可绕过路由规则（中危）；开发服务器可从旧 Nitro 构建输出读取私有 runtime config（低危，仅开发）。建议升级并清理可能受影响的 CDN/边缘缓存。
- ⚠️ **升级注意**：升级需注意 DevTools 不再随 Nuxt 安装、模板诊断默认开启可能产生新的 `NUXT_B4025` 警告、`experimental.viteEnvironmentApi` 并行构建可能影响读取客户端构建输出的 Vite 插件、`globalThis.$fetch` 仅在检测到使用时安装；Nuxt 4.7 要求 vue `^3.5.46`，`@nuxt/rspack-builder` 和 `<NuxtClientFallback>` 已弃用。

### [GitHub - cure53/DOMPurify：DOMPurify - 一个仅基于 DOM、超快速、极其宽容的 HTML、MathML 和 SVG XSS 净化器。DOMPurify 默认配置安全，但提供大量可配置项和钩子。演示：· GitHub](https://github.com/cure53/DOMPurify)

DOMPurify 是 cure53 维护的纯 DOM XSS 净化库，支持 HTML、MathML 与 SVG，README 已更新到 v3.5.0。本次更新重点是加固 DOM 节点输入路径，允许在 hook 内嵌套调用 sanitize()，统一 hook 与自定义元素处理；文档还补充 Trusted Types、服务端运行环境、旧浏览器策略和浏览器测试矩阵说明。

- 🚀 **版本与支持范围**：DOMPurify 始于 2014 年 2 月，当前版本为 v3.5.0，用 JavaScript 编写，支持 Safari 10+、Opera 15+、Edge、Firefox、Chrome 以及其他使用 Blink、Gecko、WebKit 的浏览器；在 MSIE 等旧浏览器上它不执行任何净化，会原样返回输入，可用 `DOMPurify.isSupported` 判断当前环境是否支持。
- 🛡️ **DOM 节点输入加固**：从 3.4.14 起，对于不是由 HTML 解析器生成的节点（例如用 DOM API 构建的节点，或 XML/XHTML 经 `DOMParser` 与 `importNode()` 解析得到的节点），会做额外处理：它们可能带有保留大小写的 `ONERROR` 等属性名，或出现 `<style>` 内含子元素、结束标签的情况。DOMPurify 改为按精确的 `Attr` 节点移除属性，并把这类字面文本树视为不安全。3.5.0 又覆盖 `<textarea>`/`<title>` 带子元素，以及 `<img>`/`<col>` 等空元素带子节点的情况，均直接移除。
- ⚠️ **闭合 Shadow Root 不可净化**：开放 shadow root 会被遍历，闭合 shadow root 无法被任何脚本看到；用 `setHTMLUnsafe()`/`parseHTMLUnsafe()` 解析包含 `<template shadowrootmode="closed">` 的不可信标记后，其中闭合根不会被清理，这会影响 `IN_PLACE`、`RETURN_DOM`、`RETURN_DOM_FRAGMENT`；字符串输出永远不含 shadow root，字符串输入不受影响。
- 🧩 **allow-list 与 profile**：`USE_PROFILES` 会覆盖 `ALLOWED_TAGS`/`ALLOWED_ATTR`，同时使用会在控制台告警；`<tbody>` 始终被允许且无法禁止，因为浏览器会自行插入，禁止它曾导致 `sanitize()` 死循环（#365），要整体去掉表格需改为禁止 `table`；`ALLOWED_TAGS`/`ALLOWED_ATTR`、`FORBID_TAGS`/`FORBID_ATTR`、`ADD_TAGS`/`ADD_ATTR` 均支持数组或谓词函数。
- 🎨 **自定义元素规则**：`CUSTOM_ELEMENT_HANDLING` 通过 `tagNameCheck`、`attributeNameCheck`、`allowCustomizedBuiltInElements` 控制；`attributeNameCheck` 可接收 tagName 作为第二参数，按元素区分属性；过宽的规则（如 `/./` 或 `() => true`）会放行 `onclick` 等事件处理器；3.5.0 起自定义元素只存在于 HTML，SVG 或 MathML 中的同名元素会被移除。
- 🔗 **URI 与协议白名单**：默认只允许相对 URL 以及 http、https、ftp、ftps、tel、mailto、callto、sms、cid、xmpp、matrix；可用 `ALLOW_UNKNOWN_PROTOCOLS`、`ALLOWED_URI_REGEXP` 扩展，官方提醒该正则要对攻击者可控值执行，必须保持线性时间。
- 🔄 **hook 内嵌套调用**：3.5.0 起可在 hook 或 `CUSTOM_ELEMENT_HANDLING.tagNameCheck` 等配置回调中调用 `DOMPurify.sanitize()`；内层返回后，外层会恢复自己的配置、allow-list 与 `DOMPurify.removed`。使用时需防止递归，且 `removed` 只显示外层移除项；在更早版本中，嵌套调用会覆盖外层配置。
- 🛠️ **Hook 行为调整**：提供 `beforeSanitizeElements`、`uponSanitizeElement`、`afterSanitizeElements`、`beforeSanitizeAttributes`、`uponSanitizeAttribute`、`afterSanitizeAttributes` 及三个 Shadow DOM hook；hook 中 detach 节点受支持，且不计入 `removed`；3.4.13 起 `IN_PLACE` 下被 detach 的子树仍会被处理；3.4.12 起经 `tagNameCheck` 放行的自定义元素也会走 `afterSanitizeElements`（GHSA-c2j3-45gr-mqc4）；建议用 `hookEvent.keepAttr`/`forceKeepAttr`，而不是改写 `allowedAttributes`/`allowedTags`（GHSA-cmwh-pvxp-8882）；`afterSanitize*` 中写入的内容不会被重新校验。
- ⚙️ **IN_PLACE 的 fail-closed**：传入的根节点本身必须是允许标签且未被 DOM clobbering，否则 DOMPurify 会清空根、剥离非白名单属性后抛 `TypeError`；如果遍历中途抛错，同样会对根及已 detach 的子树做中和。它不会跟进 hook 对 `<template>` 内容的节点移动，也不会处理在被清空树中自我重插的自定义元素；无法撤销 `sanitize()` 之前引擎已触发的变更。
- 🔑 **Trusted Types**：自 1.0.9 支持 Trusted Types，2.0.0 起加配置开关；`RETURN_TRUSTED_TYPE: true` 时返回 `TrustedHTML`；在自有策略的 `createHTML` 中调用需设 `RETURN_TRUSTED_TYPE: false`；DOMPurify 会自建名为 `dompurify` 的内部策略，若 CSP 的 `trusted-types` 不允许，会告警并记录违规，可传 `TRUSTED_TYPES_POLICY: null` 关闭；把自己的包装策略回传给 DOMPurify 会形成递归并抛 `TypeError`；页面级默认策略由独立项目 DOMFortify 负责。
- 🌐 **服务端与旧浏览器**：服务端需要自备 DOM，强烈建议使用最新 `jsdom`；旧版如 v19 存在即使 DOMPurify 完全正确也会导致 XSS 的已知向量（v20 修复）；`happy-dom` 目前被认为不安全；Cloudflare Workers、Vercel Edge 可用第三方 `purify-edge`（基于 parse5），官方不维护，通过测试也不构成安全保证；`isomorphic-dompurify` 可简化集成；MSIE 最后支持版本为 v2.5.9，安全更新走 2.x 分支。
- 🧪 **测试矩阵**：每次推送到发布分支，都在 9 组浏览器和操作系统组合上测试 Chromium、Firefox、WebKit（Ubuntu、macOS、Windows）；PR 在 Linux 上运行三个引擎；另有矩阵在约三年前的引擎快照上重跑全套测试（Chromium 110、Firefox 108、WebKit 16.4）；Node.js v20、v22、v24、v26 搭配 jsdom 测试，更旧 Node 版本可用但无保证。
- 📚 **对标准的影响**：DOMPurify 促成了 HTML Sanitizer API 的诞生，该能力已在许多浏览器中发布，并正在 WHATWG HTML 规范中直接标准化。

### [发布 v2.15.0 · reduxjs/redux-toolkit · GitHub](https://github.com/reduxjs/redux-toolkit/releases/tag/v2.15.0)

Redux Toolkit 发布 v2.15.0 功能版本，重点改进 RTK Query 在多 store、SSR 和测试场景下的运行时隔离，修正 initiate() Promise 结果归属，并新增 startReason、函数式 pollingInterval、getRunningQuery、retainFor、getMiddlewareState、isSubscribed 等能力；同时增强 listener middleware 嵌套 fork、优化 RTK 类型提示，并修复多项 RTKQ 行为与边界问题。

- 🚀 **正式发布**：Redux Toolkit v2.15.0 发布，属于功能版本，继续推进 Redux Toolkit 3.0 路线图，包含 RTK Query、listener middleware、类型定义和多项缺陷修复。
- 🧩 **每 store 运行时**：RTK Query middleware 将订阅计数、运行请求、轮询与缓存定时器、缓存生命周期 Promise 等状态改为每个 store 独立 runtime；resetApiState 调用 runtime.reset() 只清理当前 store，缺失 middleware 检查改为每 store 一次且更严格。
- 🔄 **initiate 结果归属**：initiate() 的 Promise 现在捕获自身请求的 fulfilled 或 rejected 结果，避免返回 undefined 或其它请求数据；请求运行中删除或 reset 缓存会中止请求，Promise 以 isError true 和 AbortError 结束，unwrap() 会 reject，queryFulfilled 也会 reject，普通 Promise 仍不会 reject。
- ⚡ **失效与重取**：失效带运行中请求的缓存项会等待请求完成，再按订阅情况重取或移除；运行中 refetch 加入现有请求；initiate() 会加入运行中的 upsertQueryData；从持久化状态恢复但没有实际请求的 pending 项会重新请求。
- 🧭 **startReason**：BaseQueryApi、fetchBaseQuery 的 prepareHeaders、onQueryStarted、onCacheEntryAdded 等新增 startReason，QueryStartReason 包含 initial、refetch、invalidation、poll、focus、reconnect、upsert、hydrate、nextPage、previousPage；mutation 为 undefined，hydrate 暂未设置。
- ⚙️ **函数式轮询**：pollingInterval 现在可为函数，接收缓存项并返回毫秒数，适用于 query hooks、initiate() 和 updateSubscriptionOptions；多个订阅者轮询同一 key 时取最低结果，返回 0、负数或非数字表示不轮询，负数数值现在也表示不轮询。
- 🔍 **查询与订阅 API**：新增 endpoint.getRunningQuery(arg) 返回运行中请求的 Promise 或 undefined；initiate() 新增 retainFor 秒数选项，最后订阅者离开后保留 Math.max(keepUnusedDataFor, retainFor) 秒；api.util.getMiddlewareState() 和 initiate() 结果上的 isSubscribed() 提供正式订阅状态 API，internal_getRTKQSubscriptions 被弃用并将在 3.0 移除。
- 🔑 **缓存移除原因**：onCacheEntryAdded 新增 getCacheEntryRemovedReason()，返回 reset 表示由 resetApiState 移除，removed 表示其它移除，undefined 表示条目仍在缓存；cacheEntryRemoved 仍保持 Promise`<void>` 类型。
- 🛠️ **嵌套 fork**：Listener Middleware 的 ForkedTaskAPI 新增 getState、dispatch 和 fork，支持嵌套 fork；嵌套 fork 随父任务结束或取消而取消，autoJoin true 会让父任务等待；State 和 DispatchType 泛型贯穿 startListening、addListener 及 withTypes()。
- 💻 **类型提示可读性**：新增 FetchBaseQueryFn、ApiUtil、ListenerMiddlewareDispatch、AsyncThunkPromise、ReactApiModules 等命名类型，并重写 query、mutation、infinite query selector 结果类型以保留名称；例如 useMutation 悬停从 2508 字符降至 386，api.util 从 16102 降至 471，属于纯类型变更。
- 🎯 **选项合并修复**：多订阅者共享查询时先解析各自选项再合并；refetchOnMountOrArgChange: 0 和 forceRefetch: 0 现在总会重取；任一订阅者自身或继承的 refetchOnFocus、refetchOnReconnect 为 true 即会重取；只有所有轮询订阅者都设置 skipPollingIfUnfocused 才在失焦时跳过轮询。
- 🐛 **其它修复**：endpoint 的 maxRetries 在 api 级 retry() 有 retryCondition 时仍生效；backoff 中 retry.fail() 不再嵌套错误；fetchBaseQuery 的 timeout 在请求自带 signal 时可用；查询参数放到 URL #fragment 之前；FetchArgs.headers 接受 number 和 boolean 并转字符串；entity adapter 更新 ID 时保持 ids 顺序；createSlice 泛型包装保留 prepare 参数类型。
- 📚 **文档更新**：文档补充 getCacheEntryRemovedReason、startReason、getRunningQuery、retainFor、getMiddlewareState、isSubscribed、函数式 pollingInterval 和嵌套 forks，并修复若干文档与 JSDoc 错误。

### [发布 v12.6.0 · nestjs/nest · GitHub](https://github.com/nestjs/nest/releases/tag/v12.6.0)

NestJS 发布 v12.6.0，重点包括 `NestFactory.create()` 根据适配器推断应用类型、WebSocket 与 gRPC 优雅关闭的 `gracePeriod` 机制、微服务在关闭和断连时更快失败待处理请求，以及 Fastify/Node 平台行为和测试模块日志选项的多项修正与性能优化。

- 🚀 **版本发布**：NestJS v12.6.0 于 2026-11-20 发布，包含 30 个提交、20 位提交者，重点更新适配器类型推断、优雅关闭、微服务关闭语义及多项修复和性能优化。
- 🧩 **适配器类型推断**：`NestFactory.create(AppModule, new FastifyAdapter())` 无需显式类型参数即可返回 `NestFastifyApplication`，`ExpressAdapter` 与 `NodeAdapter` 同理；显式类型参数仍可用，自定义适配器需在 `AbstractHttpAdapter` 的第四个类型参数声明应用类型（#18623）。
- 🛡️ **WebSocket 优雅关闭**：`WsAdapter` 新增可选的 `gracefulShutdown`（默认 `false`）与 `gracePeriod`（默认 10,000 ms）：关闭时停止接受连接，共享 HTTP 适配器的升级请求返回 503，忽略新消息，最多等待 `gracePeriod` 处理消息处理器和待回复，并以代码 1001 关闭各 socket（#18589）。
- ⚙️ **gRPC 关闭期限**：gRPC 服务端 `gracefulShutdown` 增加 `gracePeriod`（默认 10,000 ms），关闭不再无限等待进行中的调用；超过期限的调用会被取消，长流场景需调大 `gracePeriod`（#18566）。
- 🔄 **响应装饰器行为**：自定义参数装饰器把响应对象原样传给处理器且不经过管道，行为与 `@Res()` 一致并适用于各适配器；Fastify 下此类处理器此前不会运行。覆盖 `@Res({ passthrough: true })` 的普通 `@Res()` 方法不再继承 `passthrough`（#18600、#18617）。
- 🔍 **路由与发现**：路由冲突检测将字符串 host 视为模式，因此 `:tenant.example.com` 与 `admin.example.com` 的重叠可能被报告；`DiscoveryService` 可发现继承了 `DiscoveryService.createDecorator()` 装饰类的子类并归入该装饰器（#18609、#18582）。
- 🧪 **测试模块日志选项**：测试模块的 `createNestApplication()` 与 `createNestMicroservice()` 按 `NestFactory` 的方式应用 `logger` 和 `forceConsole`：`logger: true` 保留日志器而不再关闭日志，`forceConsole: true` 通过 `console` 输出（#18618）。
- 🌐 **平台行为**：`platform-node` 在 `res.send()` 发送字符串时为 `res.setHeader()` 设置的 `Content-Type` 补 `charset=utf-8`；`platform-fastify` 的上传失败异常以解析器错误为 `cause`，不以 `/` 开头的目标（`*` 和 absolute-form URL 除外）返回 400 `FST_ERR_BAD_URL`，`inject()` 对 HEAD、204、304 响应不返回 body（#18527、#18555、#18569、#18570）。
- ⚠️ **微服务关闭失败**：NATS 和 MQTT 服务端在客户端连接前关闭时，`listen()` 以 `Connection closed` 失败而不是启动；Kafka 的回复消费者停止/崩溃或 rebalance 移走回复分区、MQTT/Redis 在回复订阅确认前关闭、RabbitMQ broker 取消 direct reply-to 消费者时，待处理请求会以 `Connection closed` 失败（#18602、#18603、#18583、#18584、#18585）。
- 🛠️ **Kafka 与网关关闭**：Kafka 服务端关闭时在消费者断开后最多等待 `gracePeriod`（默认 10 秒）处理进行中的回复；网关在应用开始关闭后立即拒绝新客户端（#18535、#18588）。
- 📦 **依赖更新**：`platform-fastify` 升级 `@fastify/middie` 9.3.7、`@fastify/cors` 11.4.3、`@fastify/formbody` 9.0.2、`find-my-way` 9.10.2、`light-my-request` 6.8.1；`platform-node` 升级 `@fastify/proxy-addr` 5.1.3、`encodeurl` 2.0.3、`find-my-way` 9.10.2、`light-my-request` 6.8.1；`platform-ws` 升级 `ws` 8.23.0。
- ⚡ **性能优化**：核心性能优化包括降低 HTTP Observable 响应开销、构建拦截器链时减少多余 RxJS 层、将 Fastify 内置请求钩子合并为一个、无 Promise 地解析 RPC/WS/外部参数，并以 `export type` 重导出仅类型模块（#18607、#18593、#18561、#18559、#18560）。
- 🐛 **其他修复**：common 修复嵌套二进制检查的循环引用、日志脱敏 map 键并跳过数组空洞、`ConfigurableModuleBuilder` 不再变更 options、无 options 但带 extras 的调用、默认值自有 `__proto__` 键复制、`DefaultValuePipe` 稀疏数组长度；core 修复延迟路由处理器名保留、多路径路由非 URI 版本过滤、REPL 执行 `.clear` 后 nest 函数保留（#18612、#18598、#18597、#18571、#18574、#18551、#18568、#18567、#18547）。

### [获取失败](https://www.vlt.io/blog/vlt-1-8-1)

无法总结：获取内容失败，状态码 429。

### [是什么在运行你的 JavaScript？引擎、运行时，以及为什么有这么多](https://blog.stdlib.io/what-runs-your-javascript/)

JavaScript 由 ECMA-262 规范定义而非某个引擎或运行时，TC39 编写规范、Ecma International 每年发布新版，当前为 ECMAScript 2026，test262 用超过 5 万个测试校验实现；浏览器、Node.js、Deno、Bun 等宿主提供 I/O，V8、SpiderMonkey、JavaScriptCore、QuickJS、Hermes、XS 等引擎在内存、语言覆盖、实现语言和编译时机上分化，形成上百种实现，且合规实现仍可能行为不同。

- 🧩 **规范定义**：JavaScript 的正式名是 ECMAScript，由 TC39 编写 ECMA-262、Ecma International 每年发布带日期的版本，当前为第 17 版 ECMAScript 2026；官方测试套件 test262 有超过 5 万个测试，用于校验实现，而不是规定某个参考引擎。
- 📚 **历史脉络**：1995 年 Brendan Eich 在 Netscape 写出 Mocha，后改名 LiveScript，同年 12 月定名 JavaScript 并随 Netscape Navigator 2.0 于次年 3 月发布；微软 JScript 很快带来互操作问题，1996 年开始标准化，1997 年发布首版 ECMAScript。
- ⚙️ **引擎与宿主**：ECMA-262 只定义语言核心，不定义文件、网络、终端输出或按名加载模块，也不包含 `console.log`、`fetch`、`setTimeout`、`require`；这些由宿主提供，浏览器中 Chrome 用 V8、Firefox 用 SpiderMonkey、Safari 用 JavaScriptCore，运行时则把引擎与文件、网络、模块、定时器和事件循环打包。
- 🛠️ **运行时选择**：Node.js 是跨平台开源运行时并基于 V8；Deno 强调安全默认值，也基于 V8；Bun 定位为一体化工具包和 Node.js 的直接替代品，底层使用 JavaScriptCore；Moddable SDK 面向微控制器，围绕 XS 引擎提供网络、传感器和触摸显示支持。
- 🔄 **执行管线**：典型引擎先由 parser 生成 AST，再编译为字节码并由解释器执行，只有热点代码交给 JIT 编译为机器码；QuickJS 跳过 AST 直接生成字节码，Elk 直接解释源码，scriptc 则提前编译为不含引擎的原生程序。
- 🔍 **引擎动物园**：JavaScript 引擎动物园收录上百种实现，差异集中在内存预算、语言覆盖范围、实现语言与宿主、编译时机四个维度；MicroQuickJS 面向嵌入式系统，可在低至 10 kB RAM 运行，Hermes 为 React Native 优化快速启动和低内存。
- 🧪 **子集实现**：Elk 只实现 ES6 的小型可用子集，把字符串当二进制块，`'Київ'.length` 返回 8 而符合规范的引擎返回 4，且没有标准库，需由宿主固件导入；engine262 用 JavaScript 实现 ECMA-262，把 100% 规范合规列为目标；ECMA-327 曾允许资源受限实现省略 `with`、`eval` 和 `Function` 构造器，2015 年撤回。
- 🌐 **嵌入方式**：Boa 用 Rust 编写、便于嵌入 Rust 项目；goja 用 Go 编写；GraalJS 可在 Java 应用中嵌入 JavaScript；engine262 本身用 JavaScript 编写。Embeddable 指可嵌入其他程序，embedded 指面向嵌入式硬件；v8go 只是绑定 V8，不是新引擎。
- 📦 **编译时机**：V8 在运行时先解释字节码，再把热点代码 JIT 编译为机器码；scriptc 在发布前把 JavaScript 编译成原生程序，运行时不再读取 JavaScript 源码；Hermes 以提前编译为核心，应用发布紧凑字节码，由解释器在运行时执行。
- ⚠️ **合规差异**：符合规范不等于所有行为一致：Hermes 维护与规范的刻意差异清单，多数是少见的非严格模式边角，`localeCompare` 忽略传入 locale 被 ECMA-262 允许；XS 因不实现 ECMA-402 跳过国际化测试，也跳过仅浏览器需要的 Annex B 测试；scriptc 发布限制页并按 es2025 标准库检查；test262.fyi 每日跑 test262，另有引擎基准，规范允许实现近似使两个合规引擎仍可能给出不同答案。

### [JavaScript 引擎动物园](https://zoo.js.org/)

总结失败：模型未返回符合格式的摘要。

### [面向开发者的最佳电子签名 API：2026 年 10 款对比](https://developer-api.foxit.com/developer-blogs/api-guides-tutorials/best-esignature-api-developers/?utm_source=draftdev&utm_medium=newsletter&utm_campaign=javascriptweekly_20261124)

Docmosis Cloud 采用按页计费方式，文档越长成本越高，这促使依赖模板生成文档的团队寻找替代方案。这份指南围绕模板语法、定价、托管方式和迁移工作量四个维度横向对比 7 款 Docmosis 替代服务，并建议先筛选出 1 至 2 个候选，用自有模板实测后再决定是否切换。

- 🧩 **按页计费机制**：Docmosis Cloud 按生成页数收费，文档页数增加会直接推高成本，因此长文档与批量生成场景对价格尤其敏感，这也是寻找替代方案的主要动因。
- 🔍 **四个对比维度**：指南从模板语法、定价、托管方式、迁移工作量四方面评估 7 款替代品，便于按现有技术栈、部署合规要求和预算进行筛选。
- ✅ **先试用再切换**：建议把候选范围缩小到 1 至 2 个服务，用自己现有的真实模板做验证测试，确认渲染效果和迁移成本后，再正式迁移。
- ⚠️ **正文信息缺失**：所给正文仅有标题与导语，未列出这 7 款替代方案的具体名称、版本号或价格数字，需要补充完整内容后才能给出逐项结论。

### [为什么我改用 Vite+ — bencodezen](https://www.bencodezen.io/blog/why-i-switched-to-vite-plus)

2026 年 11 月，Ben Hong 分享从传统多工具链切换到 Vite+ 1.0 的体验：Vite+ 将 Vite、Rust/Go 重写的性能工具和最佳实践封装为统一 CLI，通过单一 `vite.config.ts` 与 `vp` 命令管理开发、构建、环境、检查、提交钩子和测试；基准显示检查速度明显提升，同时保持开源、可配置和可退出，但多语言项目仍需额外工具。

- 🚀 **正式发布**：Vite+ 1.0 已发布，作者在 VueConf US 听到 Evan 的主题演讲后开始关注，并在实际项目评估后将其作为主要工具链候选。
- 🧩 **统一工具链**：Vite+ 在单个 CLI 中打包 Oxlint（ESLint 兼容选项）、Oxfmt（Prettier 兼容选项）、Vitest、tsdown、带缓存的 Vite Task，以及管理 Node 和包管理器版本的 `vp env`；底层 Vite 提供近即时 HMR，Vite 8 可通过 Rolldown 打包优化静态资源。
- ⚙️ **配置中心**：把 lint、format、test、commit 等分散配置集中到单个 `vite.config.ts`，减少多个 dot 文件与工具间脆弱接线；`vp hooks` 安装 git hook，让约定在提交时执行。
- 💡 **提交约束**：作者示例中，`staged` 对 `*.{ts,vue,md,json}` 运行检查：`exercises`/`lessons` 等内容目录仍格式化和 lint，但不自动修复，因为 autofix 可能改变代码示例含义。
- ⚡ **性能基准**：在约 1400 个 `.ts`/`.vue` 文件、约 9.7 万行的 Vue 3 项目中，Apple M1 Max 上三次运行取中位数：全仓 format+lint+type-check 从 26.4 秒降至 `vp check` 的 4.5 秒（5.9 倍）；加上 `vue-tsc` 从 31.9 秒降至 10.2 秒（3.1 倍）；type-aware lint 从 13.6 秒降至 `vp lint` 的 1.8 秒（7.7 倍）；format check 从 9.7 秒降至 `vp fmt --check` 的 2.6 秒（3.7 倍）。
- 🧪 **测试与类型**：同一基准中，77 个文件、709 个测试从 `vitest run` 的 7.9 秒到 `vp test` 的 7.8 秒，基本持平；`vue-tsc` 类型检查从 5.7 秒到 5.8 秒，也没有明显加速。
- 🔄 **开源可退出**：Vite+、Vite、Rolldown、Oxc、Vitest 均为 MIT 许可，相关工具可脱离 `vp` CLI 单独使用；`oxlint`/`oxfmt` 与 ESLint/Prettier 大体兼容，工具可配置且可选，团队可按需退出。
- ⚠️ **适用边界**：Vite+ 并非适合所有代码库；若项目包含 Python、Ruby 或 Go 等其他语言，通常仍需额外工具链配合。

### [Vite+ | 面向 Web 的统一工具链](https://viteplus.dev/)

VoidZero 发布 Vite+ 1.0，这是一个以 `vp` CLI 为入口的统一 Web 工具链，把 Vite、Rolldown、Vitest、tsdown、Oxlint、Oxfmt 与 Vite Task 整合到一起，并同时负责 Node.js 运行时和包管理器（pnpm、npm、yarn、bun）的管理。它采用 MIT 开源许可，目标是用一套配置和一致的命令流覆盖开发、检查、测试、任务编排、构建与库打包，同时借助 Rust 底层组件显著提升构建、lint 与格式化的性能。

- 🚀 **1.0 正式发布**：Vite+ 1.0 以免费开源（MIT）形式发布，核心是统一的 `vp` CLI；可全局安装后运行 `vp help`，CI 环境推荐使用 `setup-vp`，macOS/Linux 与 Windows 分别提供安装脚本。
- 🧩 **统一命令与配置**：日常流程收敛为 `vp env`、`vp install`、`vp dev`、`vp check`、`vp build`、`vp run`、`vp pack` 等命令，全栈共用一份配置文件和一致的命令流，减少跨项目工具维护成本。
- ⚡ **性能提升**：底层关键组件用 Rust 编写，官方称生产构建比 webpack 快至 40 倍，lint 比 ESLint 快约 50 到 100 倍，格式化比 Prettier 快至 30 倍；开发侧保留 HMR，并为大型应用提供可选的 full-bundle 开发模式。
- 🛠️ **一体化检查**：`vp check` 由 Oxlint、Oxfmt 和 tsgo 驱动，一次完成格式化、lint 与类型检查，支持 Prettier 兼容格式化和 750 多条 ESLint 兼容规则，`vp check --fix` 可自动修复可修复问题。
- 🧪 **测试能力**：测试基于 Vitest，复用应用的 resolve 与 transform 配置，提供 Jest 兼容 API、默认测试隔离、浏览器模式，以及覆盖率、快照、类型测试和视觉回归等能力。
- 📦 **库打包**：`vp pack` 基于 Rolldown/tsdown，支持 DTS 生成与打包、自动生成 package exports、独立应用二进制以及仅转换不打包的 unbundled 模式。
- 🔄 **任务编排**：`vp run` 由 Vite Task 提供，可执行内置命令和 `package.json` 脚本，具备自动输入追踪的缓存能力和跨 workspace 包的依赖感知执行，面向 monorepo 场景。
- 🌐 **运行时与生态兼容**：Vite+ 自动使用 `node` 并按项目选择包管理器；支持所有构建在 Vite 之上的框架及元框架，可部署到 Vercel、Netlify、Cloudflare，或配合 Nitro 部署到任意平台。
- 🛡️ **供应链安全**：官方强调 Vite+ 的开发遵循严格安全实践，并对统一工具链所依赖的第三方包进行审查。

### [自定义渲染器 • Svelte 文档](https://svelte.dev/docs/svelte/custom-renderers)

Svelte 推出实验性的自定义渲染器（custom renderer），让组件在保留 runes、props、控制流等写法的同时渲染到 WebGL 场景、原生移动 UI、终端或 PDF 等非 DOM 目标；该功能需通过 `experimental.customRenderer` 显式启用，API 在实验标记移除前可能变化。

- 🧪 **实验启用**：自定义渲染器目前为实验特性，需在 Svelte 配置（通常是 `svelte.config.js` 或 `vite.config.js`）中开启 `experimental.customRenderer`，官方提示 API 在实验标记移除前可能变化。
- 🎯 **渲染器选择**：组件可用 `<svelte:options customRenderer=... />` 指定渲染器模块，路径支持包名、别名或相对组件的路径；配置可设默认渲染器，组件可用 `customRenderer={null}` 退回 DOM。
- ⚙️ **按文件配置**：`experimental.customRenderer` 也可设为函数，接收 `{ filename }` 并返回该组件使用的渲染器路径或 `null`；函数可返回相对该文件的路径，组件内 `<svelte:options customRenderer={...}>` 优先于函数。
- ⚠️ **默认路径限制**：全局配置的默认渲染器路径不能是相对路径，因为每个组件都会导入它；应使用包名、子路径导入或绝对路径。
- 🌐 **浏览器外运行**：在终端、PDF、原生运行时或测试器等非浏览器环境，需加入 `svelte-custom-renderer` resolve condition（Node 用 `--conditions=svelte-custom-renderer`），使 `svelte` 解析到运行组件的实现而非 SSR HTML；缺失时 Svelte 会报错说明。
- 💻 **挂载与混用**：可用 `mount(Component, { target, renderer })` 将应用挂到渲染器创建的 target；在浏览器中，自定义渲染器组件也可嵌入普通 Svelte 应用，前提是渲染器支持与 DOM 混用。
- ✅ **支持范围**：自定义渲染器组件支持 runes、props、snippets、组件、context、`{#if}`/`{#each}`/`{#key}`/`{#await}`、`<svelte:boundary>`、`<svelte:element>`、attachments、await 表达式及组件上的 `bind:`；`class`、`style`、`class:`、`style:` 会作为属性传给渲染器，`onclick` 等事件交给 `addEventListener`。
- ⚠️ **不支持项**：元素上的 `bind:`、`transition:`/`in:`/`out:` 与 `animate:`、旧式 `on:` 指令、`{@html ...}`、`<svelte:head>`/`<svelte:window>`/`<svelte:document>`/`<svelte:body>`、`<svelte:options css="injected" />` 在自定义渲染器组件中会编译报错。
- 🎨 **样式与 SSR**：`<style>` 仍会被作用域化并添加类似 `svelte-xyz123` 的类，但不会注入页面，是否利用 CSS 取决于渲染器；`css: 'injected'` 对自定义渲染器组件被忽略，组件内设置 `css='injected'` 会报错；SSR 时自定义渲染器组件不渲染内容，浏览器端在页面加载后创建，周边 DOM 仍正常 SSR 和水合。
- 🧩 **渲染器实现**：渲染器模块默认导出由 `svelte/renderer` 的 `createRenderer` 创建的对象，需实现 `createFragment`、`createElement`、`createText`、`createComment`、`getNodeType`、`getText`/`setText`、`insert`/`remove`、属性读写与事件监听等方法；`createRenderer` 返回参数本身，主要提供类型安全，`Renderer` 类型也从 `svelte/renderer` 导出。
- 🔗 **混用 crossing**：不同渲染器可嵌套，跨渲染器边界称为 crossing；guest 实现可选 `embed`，host 实现可选 `host`，Svelte 先试 guest 的 `embed` 再试 host 的 `host`，都没有则报错；DOM 两者都没有，因此混用应用通常由自定义渲染器提供。
- ⚙️ **crossing 规则**：`embed` 接收 host 渲染器（DOM 为 `null`）、`parent` 和 `anchor`，`host` 接收 guest 渲染器（DOM 为 `null`），二者返回 `node`、`container` 和 `destroy`；调用在组件或 snippet 创建时同步发生，`parent` 可能尚未挂载，Svelte 负责插入/移除节点和内容，`destroy` 仅释放自有资源。
- 📚 **snippet 限制**：snippet 可在渲染器之间传递，但必须由启用 `experimental.customRenderer` 编译的组件创建；`createRawSnippet` 创建的 snippet 不能由自定义渲染器渲染。

### [发布 svelte@5.59.0 · sveltejs/svelte · GitHub](https://github.com/sveltejs/svelte/releases/tag/svelte@5.59.0)

Svelte 发布 `svelte@5.59.0`，这是一次包含 `custom renderer API` 的 minor 版本更新（#18042）。核心变化是为自定义渲染器提供 API，使需要将 Svelte 组件渲染到非默认目标的用户获得新的扩展入口；原文未披露具体实现细节和限制。

- 🚀 **正式发布**：`svelte@5.59.0` 于 20 Nov 发布，属于 minor 版本更新，包含 `custom renderer API` 变更（#18042）。
- 🧩 **核心机制**：新增 `custom renderer API`（#18042），作为 minor change 提供自定义渲染器接口，面向需要自定义渲染目标的用例；原文未说明 API 细节、实验状态或限制。

### [绕过 iOS Safari 的 60 FPS 限制，构建宛如原生的 Web 应用 · Rida F'kih](https://rida.dev/blog/bypassing-ios-safari-60-fps-limit)

Rida F'kih 在 2026 年 11 月 20 日的文章中介绍了如何在不打开 Safari 开发者设置里「Prefer Page Rendering Updates near 60fps」开关的前提下，让 iOS Safari 的 Web 交互突破 60 FPS：把原生滚动区域当作「控制器」，以接近 120 Hz 的频率同步读取 `scrollTop`/`scrollLeft` 获取输入；再通过 `transferControlToOffscreen` 得到 `OffscreenCanvas`，让 WebKit 在推帧时跳过等待下一次渲染流程，从而以 120 FPS 绘制输出。两者结合让 PWA 和微交互获得接近原生的手感，但整套方法依赖尚未标准化的实现细节，苹果随时可能改变其行为。

- 🧩 **限制所在**：iOS WebKit 默认把 `requestAnimationFrame` 限制在 60 Hz，即便屏幕是 120 Hz ProMotion；普通页面上的 touch 与 pointer 事件也被压到同一频率，除非用户在 Safari 开发者设置中打开「Prefer Page Rendering Updates near 60fps」。低电量模式下还会进一步降到 30。
- 🔄 **滚动即输入**：文章沿用 React Aria 的思路：滚动由合成器线程负责，不经过 JavaScript 往返，因此天然流畅。把方块放进可滚动区域，其运动直接由合成器驱动；只要能足够频繁地读出滚动位置，就能把原生动量、回弹、吸附点当作输入源，做出 1:1 触控板、无限滚动轨迹球、带刻度的旋钮等交互。
- 🛠️ **早期失败尝试**：直接监听 scroll 事件在惯性滚动时每秒仅更新 5 到 26 次，慢速刻意滚动的最好情况也接近不了 60 次。递归 `MessageChannel` 每秒可读 5 万次，但只有 80 个不同值，且占满一个 CPU 核心；用 `Atomics` 按刷新率唤醒同样只有每秒 80 个不同位置，还需要 `SharedArrayBuffer`，从而强制启用 COOP/COEP 响应头，破坏站点上的跨域资源。
- ⚙️ **最终读取方案**：最终方案是用 `MessageChannel` 触发读取，按设备刷新间隔用 `setTimeout` 把下一次测量推到下一个 tick，再用 `requestAnimationFrame` 时间戳与 vsync 相位锁定。由于 iOS 把 `performance.now()` 取整到毫秒，作者从刷新间隔推导最小绘制间隔。该方案达到每秒 80 次位置读取。
- ⚡ **绕过 IPC 覆盖**：Safari 的 UI 进程一次只向 Web 进程发送一个滚动位置，并等待确认后才发下一个，期间到达的值会被覆盖，造成丢点。作者发现只要页面有排队中的渲染更新，Safari 就会立即冲刷位置而不等待，于是一个空的 `requestAnimationFrame` 循环即可，读取量提升约 12.5%，达到每秒 90 个不同位置。
- 🎯 **升到 120 Hz**：剩下的 30 Hz 受 ProMotion 判断影响：只有当有内容在滚动且存在 GPU 加速的 CSS 动画时，屏幕才升到 120 Hz。于是让一个不可见的微型滚动容器在后台平滑滚动，仅在预期发生动画时（触摸事件、滚动驱动动画等）启用；若交互不需要动量、回弹或吸附，也可直接用 passive `touchmove` 监听器拿到完整的 120 Hz。
- 🔍 **精度与替代方案**：`scrollTop`/`scrollLeft` 会被取整，解决方法是将可滚动面按设备像素比放大、容器再按倒数缩小。也可以把视口本身当控制器并设置 `initial-scale`，但需按 DPR 缩放单位、禁用文字自动调整、手动缩放安全区，还会出现细小的文字选择柄。页面作为控制器时，滚动方向改变引发的地址栏伸缩会把位置节流到 10 Hz；给页面加一个驱动非 GPU 加速属性的滚动驱动动画（例如两个透明色之间过渡）可跳过该限制。
- 💻 **突破渲染上限**：输入解决后 DOM 仍只有每秒 60 次更新。作者在第七次尝试后找到办法：创建 canvas 并调用 `transferControlToOffscreen` 得到 `OffscreenCanvas`，原 canvas 成为占位符，WebKit 按 HTML 规范建议在 `OffscreenCanvas` 推帧时跳过等待下一次渲染流程，从而实现 120 FPS 画布渲染；该方式耗电低，内存只需支持更高频的后备存储。文章指出此前公开说法均认为不开启特性开关就无法在 iOS Safari 用 canvas 达到 120 Hz。
- 🎨 **演示实现**：作者用这套方法做了 Ando 移动应用的 UI 克隆，含 Liquid Glass 标签栏、按钮与流畅导航，装成 PWA 后几乎与原生无异。页面加载时先截图存入 WebGL 纹理，滚动时采样组件下方区域合成玻璃效果；用 `requestAnimationFrame` 的组件在主线程更新纹理，用 `OffscreenCanvas` 的组件则从各自 worker 直接向管理纹理的 worker 投帧，从而避开主线程并以 120 Hz 刷新着色器。
- 🧩 **标签栏状态机**：标签栏为每个按钮分配一个控制器，控制器只上报带时间戳的事件（哪个控制器被使用、被拖动了多少），并保留一小段采样历史，用于判断按压是否已构成拖动以及手指速度。每帧由状态机产出镜头位置、抬升与拉伸幅度、胶囊可见度：触摸时放大并抬升镜头，按相对起点的偏移移动，拖出标签栏边界时把标签栏朝手指方向拉伸，松手后吸附到最近的标签。
- 📊 **实测性能**：作者搭建基准环境，用 240 FPS 录制 iPhone 18 Pro 并放慢到八分之一做对比：3 秒拖拽中控制器版本平均 118 FPS，pointer 事件版本稳定在 60 FPS；即使在通常限制到 30 FPS 的低电量模式下，该方法也能达到 60 FPS。
- ⚠️ **风险提示**：作者明确表示不会把整个应用重建在这套技巧上：苹果完全有权在不违反 HTML 规范的前提下让 `OffscreenCanvas` 占位符重新等待主线程渲染流程，且此前对 web-haptics 等库有过类似「扫兴」记录。他更希望苹果直接关闭该特性开关、原生为网站支持 ProMotion，让这些发现变得多余。

### [为了移除 Moment.js，我们先让所有东西都依赖它](https://medhat.dev/blog/removing-moment-js/)

这篇 TypeScript 文章讲的是一个反直觉的依赖治理思路：在移除 Moment.js 之前，先让所有日期处理代码都依赖它，也就是先建立一个统一的入口或适配层，把散落在各处的直接调用集中起来，这样后续替换底层实现时，只需改动这一处，避免在全代码库中零散地迁移。

- 🧩 **核心机制**：先引入统一的日期封装或适配入口，让业务代码只通过这一层使用 Moment.js，把分散的直接引用收敛到单一位置。
- 🔄 **迁移策略**：依赖收敛完成后再替换底层实现，改动集中在适配层，避免在调用点逐处重写日期逻辑。
- 💻 **TypeScript 支撑**：文章以 TypeScript 呈现，可用类型约束固定统一入口的 API 边界，使后续替换实现时上层调用不受影响。
- ⚠️ **前提与限制**：该方法成立的前提是能找出并改造所有直接引用 Moment.js 的位置；标题表明这是移除工作的第一步，而非替换本身。

### [Chrome 预渲染很奇怪 · Tom Bennet](https://tombennet.dev/blog/chrome-prerendering-is-weird)

Chrome 地址栏预渲染会在用户输入时后台完整加载高置信度建议页面并执行 JavaScript，甚至把 localStorage 写入保留下来。Synthesia 因此出现间歇性注册引导错乱：预渲染页先写入错误查询参数快照，真实页面因已有快照不再覆盖；修复是在 document.prerendering 为 true 时等待 prerenderingchange 后再保存，并可用 Sec-Purpose 请求头在服务端识别预渲染请求。

- 🧩 **地址栏预渲染**：Chrome 可在用户输入地址栏时预加载顶部建议；页面会被完整预渲染，JavaScript 执行，写入 localStorage 的数据也会保留，即使用户最终没有访问。该行为有文档说明，目标是让导航显得即时。
- ⚠️ **污染快照**：Synthesia 的注册引导依赖首次加载 URL 的查询参数，并在首次加载时把查询串快照写入 localStorage；已有快照就不再覆盖，引导完成后清除。预渲染页面先写入另一组参数后，真实注册页看到已有快照便不再更新，整个 Incognito 会话可能进入错误引导流程。
- 🔍 **隐身模式**：Incognito 不能规避：它从空 localStorage 开始，但同一 Incognito 会话的所有标签页共享该存储，包括 Chrome 不可见的预渲染页；地址栏建议又基于正常浏览历史。
- 🐛 **复现门槛**：该问题难以抓现场：DevTools 打开时 Chrome omnibox 不会预渲染建议（2019 年加入的检查），Speculative loads 面板也不显示；全新浏览器配置没有历史可建议；直接粘贴 URL 会跳过问题；Chrome 仅在高置信度时预渲染，可在 chrome://predictors 查看分数，重度使用者更易触发。
- 🛠️ **修复方式**：修复是在保存查询参数快照前检查 document.prerendering；若为 true，则等待 prerenderingchange 事件（once: true）后再执行，否则立即执行。文章示例封装为 whenActivated(saveSearchParamsSnapshot)，用户从未真正访问页面时回调不运行，也就不会写入快照。
- 📊 **通用建议**：页面加载不等于有人访问。页面加载时只应执行一次的保存状态、记录事件或计数浏览等逻辑，应先检查 document.prerendering；Google Analytics 等分析工具已处理该情况，站点也可通过 Speculation Rules API 主动请求预渲染链接。
- 🌐 **服务端识别**：服务端可通过请求头 Sec-Purpose: prefetch;prerender 识别预渲染请求，并按需处理。

### [Angular 22.3 有哪些新特性？- Ninja Squad](https://blog.ninja-squad.com/2026/11/18/what-is-new-angular-22.3)

Angular 22.3.0 于 2026 年 11 月 18 日发布，是 v22 周期的第三个次版本，重点提升构建性能，引入部分用 Rust 编写的 ngp 编译器和新的库构建器，同时带来路由错误边界、更严格的模板检查、HTTP QUERY 方法支持、视图过渡稳定化等更新；其中部分能力仍为开发者预览、实验性或需显式开启。

- ⚡ **Rust 编译器**：新的 ngp 编译器部分用 Rust 编写，目标是加速构建和增量重建；由于它不依赖 TypeScript 类型检查器分析模板，部分模板警告不会在 ngp 中提供，模板里未被调用的函数或 signal 可能无法被捕获，这是当前版本为性能做出的取舍。
- 🛠️ **移除未完成原型**：团队从代码库中移除了 signal components 的 signals: true 和 selectorless components 两个未完成原型；两者都不是受支持的正式功能，因此影响有限。
- 🛡️ **strictUnknownElements**：新增可选编译器标志 strictUnknownElements，用于捕获此前被属性指令匹配后静默接受未知元素的情况；例如导入 ReactiveFormsModule 后，缺少 CustomColorPicker 导入的 custom-color-picker 仍可编译，开启后会报 NG8001 未知元素错误。该选项在 v22.3 默认 false，计划在 v23 默认启用。
- 🛡️ **strictNgTemplateTypes**：新增可选编译器标志 strictNgTemplateTypes，检测此前被静默忽略的 ng-template 未知属性绑定；例如把 ngTemplateOutlet 拼错为 ngTemplateOutet，开启后会报 NG8002。该选项在 v22.3 默认 false，计划在下一个主版本默认启用。
- ⚠️ **CSS 数值单位诊断**：在 v22.3 中，启用 strictTemplates 时默认启用扩展诊断 numericCssPropertyRequiresUnit，检测绑定到受支持 CSS 长度属性时缺少单位的非零数字字面量和数字字符串字面量；例如把 height 绑定为 200 不会生效，会报 NG8119。该检查允许无单位零和 opacity 等接受无单位数字的属性，目前不检查从组件属性或其他非字面量表达式读取的值。
- 🧩 **事件处理器自增自减**：模板语法新增在事件处理器中使用自增和自减运算符，支持前缀和后缀形式，即 ++count、count++、--count 和 count--，行为与 JavaScript 一致。
- 🔗 **路由资源父级依赖**：v22.3 中路由 resources 的 context 新增 resources signal，暴露祖先路由的资源；子路由可依赖父路由资源，例如父路由 users/:id 获取 user，子路由 users/:id/posts 使用其 authorId 拉取 posts，父资源变化时子资源会响应。父资源必须在资源的 params 函数或传给 httpResource 的请求回调中读取，否则可能不可用并抛出 NG04020；配合 withComponentInputBinding()，父资源也可绑定到组件输入。
- 🛡️ **路由错误边界**：withErrorBoundaries() 以开发者预览形式为路由启用错误边界，当路由组件在创建或渲染期间抛错，包括读取失败资源的值时，可显示回退组件；它不处理守卫、解析器或阻塞型路由资源等导航错误。可通过 defaultErrorComponent 和 onError 全局配置，也可用路由的 errorComponent 覆盖；回退组件可通过输入访问 error 和路由参数，目前没有显式 reset API，未启用 withErrorBoundaries() 却使用 errorComponent 会在控制台警告。
- ✅ **视图过渡稳定**：v17 以实验形式引入的 withViewTransitions() 现已稳定，因为主流浏览器均支持该能力；默认在路由导航间提供淡入淡出过渡，可用 CSS 自定义动画、动画整个视图或跳过部分视图，并标记新旧视图中相同的 DOM 元素以让浏览器在状态间动画。
- 🔄 **RouterLink 滚动控制**：启用滚动恢复后，路由器通常在前向导航后滚动到顶部，即使只改变查询参数；v22.3 可通过 RouterLink 的 scroll 输入设为 manual 来让该次导航不改变滚动位置，适用于页面下方标签或过滤器触发 URL 变化。默认值 after-transition 遵循路由器滚动配置，该输入也适用于通过 withExperimentalPlatformNavigation 使用浏览器 Navigation API 的情况。
- ♿ **焦点重置控制**：针对仍为实验性的浏览器 Navigation API 支持，NavigationBehaviorOptions 新增 focusReset 选项；after-transition 为默认值，浏览器会把焦点移到带 autofocus 的元素或 body，manual 则不让浏览器重置焦点。该选项仅在 withExperimentalPlatformNavigation 下生效，且本身也是实验性功能。
- 🧪 **测试导航辅助**：RouterTestingHarness 新增 navigate() 方法，与现有 navigateByUrl() 并存，允许指定 NavigationExtras，包括 state、skipLocationChange、replaceUrl 等不在 URL 中的选项；此前需要注入路由器并调用其 navigate 方法。
- 📦 **defer 滚动边距**：@defer 的 viewport 触发器新增 scrollMargin，可与 rootMargin 和 threshold 一起使用；scrollMargin 是 IntersectionObserver API 的选项，不同于 rootMargin，它会扩展嵌套滚动容器的裁剪边界，使延迟内容在进入嵌套滚动区域可见范围前加载或预取。
- 🧠 **WebMCP 调试标注**：v22 以实验形式引入的 WebMCP API 在 v22.2 已支持在工具声明中定义标注；v22.3 新增 debugging 标注，用于指示工具面向调试和开发用途，而非最终用户代理交互。通过 experimentalWebMcpTool 暴露的 signal forms 会自动配置 debugging: false。
- 🌐 **HTTP QUERY 方法**：HTTP 规范通过 RFC 10008 引入 QUERY 方法，允许带请求体的安全、幂等查询；HttpClient 在 v22.3 通过 http.query(url, body, options) 支持该 HTTP 方法，但服务器必须支持。QUERY 请求默认与 GET、HEAD 一样有资格进入 Angular 的 SSR 传输缓存。
- 📦 **新库构建器**：新的 @angular/build:library 构建器替代 ng-packagr，与 CLI 其他构建器共享大量代码，目标是提升性能，尤其是更新库中 TS 或 SCSS 文件时的增量重建以及多入口点库；快速基准显示增量重建约快 2 到 4 倍。新生成的库默认使用该构建器，旧 @angular/build:ng-packagr 已弃用并会提示迁移，可选迁移命令为 ng update @angular/cli --migrate-only --name=use-library-builder。
- 🧩 **库入口点生成**：CLI 提供新的 ng generate entry-point testing --project=my-lib 原理图，用于生成次级入口点，使使用方可从 my-lib/testing 导入 API；该原理图仅适用于使用新库构建器的库。
- 🧪 **单元测试配置**：unit-test 构建器现在允许设置 polyfills 选项，此前 polyfills 总是从 buildTarget 继承，现在可覆盖；生成应用和库时 --test-runner 选项已弃用，目前仍可选择 Karma，但未来版本中新生成项目将只配置 Vitest。
- 🌐 **SSR 预渲染文件格式**：现在可将路由预渲染为 name.html 而不是 name/index.html，通过 prerender.format 设为 file 启用，当前默认是 directory；这适合对 /foo 提供 /foo.html 的静态托管以避免重定向，但如果生成服务器则会被忽略，因为 @angular/ssr 期望目录布局。
- 🎨 **oxfmt 格式化**：CLI 现在可使用 oxfmt 配置格式化 ng generate 生成的文件，此前仅支持 Prettier；CLI 会检查两者并选择找到的格式化器，两者都安装时优先 Prettier。目前还不能直接通过 ng new 创建使用 oxfmt 的项目，但 oxfmt 已可配置 Angular 模板格式化而不受文件名限制。

### [Solid 1 到 Solid 2 - Component Party](https://component-party.dev/compare/solid1-vs-solid2/)

Solid 2 迁移指南用 22 个 Solid 1/2 对照示例说明升级影响，其中 8 个示例需要改动。核心变化集中在用 `onSettled` 统一处理挂载、清理、DOM ref 和状态更新等副作用，Context 去掉 `.Provider`，异步数据获取改用 `Loading`/`Errored` 组件配合 `createMemo`；大量模板、样式、循环、事件、条件渲染和表单用法保持不变。

- 📊 **迁移范围**：指南给出 22 个对照示例，其中 8 个在 Solid 2 中需要修改，可据此判断升级影响面。
- 🔄 **状态更新调度**：Solid 1 在组件体直接调用 `setName("Jane")`；Solid 2 改为在 `onSettled(() => { setName("Jane") })` 中执行，把状态更新副作用放到 settles 后。
- 🧩 **生命周期统一**：`onMount`/`onCleanup` 示例迁移为 `onSettled`：挂载后聚焦输入框或读取 `document.title` 用 `onSettled`，卸载清理则让 `onSettled` 返回清理函数，例如清除 `setInterval`。
- 🔗 **Context 简化**：Context 提供方式从 `<UserContext.Provider value={...}>` 改为 `<UserContext value={...}>`，移除 `.Provider`。
- ⚡ **异步数据**：数据获取从 `createResource` 配合 `Switch`/`Match` 判断 `data.loading`、`data.error`，改为 `createMemo(() => fetchUsers())` 获取结果，并用 `Loading`、`Errored` 的 `fallback` 处理加载和错误；`fetchUsers` 直接返回 `results`。
- ✅ **兼容范围**：`createSignal` 声明状态与计算状态、最小模板、CSS/内联样式、`For` 循环、点击事件、`Switch`/`Match`、事件向父组件传递、插槽及文本/复选框/单选框/下拉框表单示例在 Solid 1 与 Solid 2 中代码相同。

### [Component Party – 并排对比 JavaScript 框架](https://component-party.dev/?f=react-vue3-svelte5-angularRenaissance-lit)

这篇技术周刊对比 React 与 Svelte 5 在响应式状态、模板、样式、事件、生命周期、组件组合、表单绑定及数据获取等常见前端场景中的写法差异，核心是 Svelte 5 通过 `$state`、`$derived`、`$effect` 等 runes 与 `bind:` 指令把状态声明、派生计算和双向绑定内建到语言或编译层，从而减少 React 中常见的 hook、setter 和受控输入样板；原文为代码对照，未给出性能基准或迁移结论。

- 🧩 **响应式核心**：Svelte 5 用 `let name = $state("John")` 声明状态、`$derived(count * 2)` 表达派生值、`$effect(...)` 处理副作用；React 对应使用 `useState`、普通计算表达式和 `useEffect`，更新通常经 setter 完成。
- ⚡ **更新更直接**：React 更新状态需调用 `setName` 或 `setCount`，示例中通过 `useEffect` 挂载后执行；Svelte 直接执行 `name = "Jane"` 或 `count++` 即可，减少显式更新函数和部分样板。
- 🎨 **模板与样式**：React 组件以函数返回 JSX，样式通过导入 CSS、`className` 和对象形式内联样式；Svelte 单文件组件直接写类 HTML 模板，使用 `class`、字符串形式 `style`，并在 `<style>` 中定义样式。
- 🔄 **列表与条件**：React 用 `colors.map(...)` 配合 `key` 渲染列表，用三元表达式或 `&&` 做条件；Svelte 使用带 key 的 `{#each colors as color (color)}` 以及 `{#if}`、`{:else if}`、`{/if}` 模板语法。
- ⚙️ **事件与 DOM 引用**：React 使用 `onClick`、`useRef` 和 `useEffect` 绑定事件及聚焦输入框；Svelte 使用小写 `onclick`、`bind:this={inputElement}` 和 `$effect`，事件处理中可直接修改状态。
- 🧭 **生命周期与清理**：React 在 `useEffect` 中以空依赖数组模拟挂载，并在返回函数中清理 `setInterval`；Svelte 的 `$effect` 可直接读写状态并返回清理函数，示例同样用于挂载设值和定时器卸载清理。
- 🔗 **组件组合与上下文**：两者都通过 props 向子组件传值并用回调向父组件通信；React 还示例 `children` 和 `Context.Provider` 提供用户状态，Svelte 示例 `setContext("user", user)` 与 `createUserState.svelte.js` 共享状态。
- 📝 **表单绑定**：React 文本、复选框、单选框和下拉框均用受控值加 `onChange` 处理函数更新状态；Svelte 用 `bind:value`、`bind:checked`、`bind:group` 和 `bind:value` 实现双向绑定，减少显式事件处理。
- 🌐 **应用入口与数据获取**：React 入口从 `index.html` 加载 `main.jsx`，数据请求通过自定义 hook 返回 `isLoading`、`error`、`data`；Svelte 入口加载 `app.js`，`.svelte.js` 中的请求逻辑返回响应对象，并在模板中以 `{#if}` 和 `{#each}` 渲染加载、错误和用户列表。
- ⚠️ **限定说明**：原文只是 React 与 Svelte 5 的并排代码示例，覆盖常见 UI 模式，未提供性能测试、包体积数据或正式迁移结论；Svelte 示例依赖 Svelte 5 的 runes 写法。

### [Solid 2.0 - 漫长的等待 | Solid](https://www.solidjs.com/blog/solid-2-0-the-long-hold/)

Solid 2.0 于 2026 年 11 月 16 日稳定发布，核心变化包括把异步引入响应式图、将 Server Functions 下沉到核心、面向 AI/Agent 提供可定位的运行时诊断，同时大幅收缩 API 面并退役 SolidStart 元框架，改由核心原语和框架无关的 Vite 插件支撑上层方案。

- 🚀 **正式发布**：Solid 2.0 在 2026 年 11 月 16 日达到稳定，距 1.0 已五年；官方强调 async graph、server functions、agent diagnostics 和更小 API 面，用户可通过 `npm create solid@latest` 开始使用。
- 🧩 **异步响应式图**：计算函数现在可返回 `Promise` 或 async iterator，下游的 `createMemo`、`Loading` 和 `isPending` 等能直接理解异步状态；框架自动处理竞态并回滚推测状态，保持服务器为真相源，减少手写异步流程。
- 🌐 **服务端函数回核心**：2022 年由 SolidStart 引入的 Server Functions 进入 Solid 核心，支持基于 Request/Response 的 RPC 和基于 Server Sent Events 的持久连接；示例用 `live(async function*(){ ... })` 暴露价格流，后续还将公布 reactive Server Components。
- 🧠 **Agent 诊断**：开发构建会针对响应式错误给出稳定错误码、源码位置和修复建议，例如 `STRICT_READ_UNTRACKED`；细粒度图可检测异步瀑布、effect 循环以及宽扇入/扇出等图形态，并提供 `SKILL.md` 修复指南。
- 🔍 **可观测工具**：诊断能力延伸到工具链，已集成 Chrome Performance Tracks 和更新版 Sentry 插件，使生产构建也能获得同类信息；结合 lint 规则，可在编译期和运行期为 agent 提供方向。
- 🧪 **实验语法**：Solid 2.0 增加对 `ReactiveScript` 和 `TSRX` 的实验性支持，目标是通过编译进一步改善 agent 编写体验；官方表示该领域仍在随着 agent 构建方式的学习而演进。
- 🧭 **退役元框架**：构建 Solid 元框架所需的原语已由核心或框架无关的 Vite 插件提供，因此官方退役 SolidStart；Server Functions 支持任意 router，Single-Flight Mutation 支持任意缓存方案，生态只需一个 Clerk 或 Sentry 插件即可覆盖。
- 📦 **API 收缩**：移除 `createResource`、`batch`、`startTransition`、`on`、`produce`、`createComputed`、`createMutable`，减少必须学习的原语和异步仪式，也减少对 `createEffect` 等逃生舱的依赖，鼓励从状态派生而非放入 reducer。
- ⚡ **示例简化**：异步级联下拉框示例仅用 `createMemo` 和 `createSignal` 组织州与城市数据，加载状态、竞态和取消逻辑由框架承担，最终剩余代码主要是 UI，体现安全由构造约束而非人工穷举。
- 📈 **发布过程**：2.0 路线在 2025 年 2 月公布，随后经历一年以上实验并重写响应式核心；beta 在 3 月、API 冻结的 RC 在 8 月发布，14 周内发布 23 个 RC，合并 971 个 PR、关闭 753 个 issue，稳定门槛是普通应用代码连续一周无回归且无崩溃或挂起。
- 📝 **名称含义**：The Long Hold 指 Solid 2.0 的一项诊断警告：当 `isPending` 已展示 hold 但距上次输入已过足够时间时触发；官方借这个名称承认异步工作耗时较长才最终落地。

### [SolidStart：细粒度响应式走向全栈](https://start.solidjs.com/)

Solid v2 已上线，最大变化是 SolidStart 的全栈能力被内置进 Solid 2，原先由 SolidStart 提供的能力现在随 Solid 2 一起发布；Solid 1 用户仍可继续使用 SolidStart。SolidStart 以可组合元框架方式整合序列化、打包、部署与路由等模块，并增强单航班变更、请求与资源去重、服务端动作/函数、并行数据预加载和 Vite 插件多平台部署体验。

- 🚀 **正式发布**：Solid v2 已正式上线，SolidStart 现在内置到 Solid 2；仍在使用 Solid 1 的用户可以继续使用 SolidStart。
- 🧩 **可组合架构**：SolidStart 将多个独立包集成为完整功能，包括 Seroval 高性能序列化器、Vite 打包器、Nitro V3 部署、Netlify Vite 插件和 Cloudflare Vite 插件，各部分可用自有实现替换。
- 🔗 **路由无关**：SolidStart 支持官方 Solid Router，也支持第三方 TanStack Router，路由层可替换。
- 🔄 **单航班变更**：Single-Flight Mutations 避免服务端更新数据时的请求瀑布；即使 mutation 触发导航，新数据也会随 mutation 响应在同一航班返回。
- ⚡ **请求去重**：一次往返中，两个相同请求不会重复发出，两个相同资源也不会重复序列化。
- 🛠️ **服务端能力**：Server Actions 支持在服务端运行表单动作并实现代码同置；Server Functions 即 Lambda Functions，可像普通路由一样自动创建 API 端点。
- 📈 **数据预加载**：提供强并行化的数据加载，可定义预加载策略，减少等待并提升交互流畅度。
- 🌐 **部署生态**：借助 Vite 插件可部署到 Cloudflare、Netlify、Vercel、Bun、Deno、AWS、Azure 等 20 多个平台；示例配置使用 `solidStart()` 与 `netlify({ build: { enabled: true } })`。

### [Trigger.dev | 持久 AI 智能体的开源平台](https://trigger.dev/?utm_source=fnf&utm_medium=newsletter&utm_campaign=october&utm_term=js-weekly&utm_content=homepage)

Trigger.dev 发布面向 AI agents 的 webhooks，并以其开源 TypeScript 平台承载持久化 AI agents 与工作流：长任务支持重试、队列、人类审批、实时流式输出与可观测性，按实际执行付费并可弹性伸缩。平台同时提供多种 agent 编排模式和可定制运行时，近期更新还包括统一日志搜索、GitHub Actions 可信发布、API key 权限预设与 OIDC 工作负载身份。

- 🚀 **正式发布**：Trigger.dev 上线面向 AI agents 的 webhooks，面向用 TypeScript 构建和部署持久化 AI agents 与工作流的开发者；功能列表同时列出 durable webhooks 与 wait for HTTP callback。
- 🧩 **核心机制**：通过 `chat.agent` 声明 `id` 和 tools，在 `run()` 中调用 `streamText`；`chat.toStreamTextOptions` 负责 system prompt、tool approval、compaction、mid-turn steering 与 telemetry，示例模型为 `claude-sonnet-4-5`，并用 `stopWhen: stepCountIs(15)` 限制步数。
- ✅ **人工审批**：`refundOrder` 工具设置 `needsApproval: true` 后，调用会暂停等待人工批准，且运行保持存活；tool calling 与 `run()` 类型贯通，适合需审批的支付或退款等操作。
- 🧭 **编排模式**：提供 autonomous agent、prompt chaining、routing、parallelization、orchestrator、evaluator-optimizer 六种模式，对应开放式任务、多阶段处理、按内容路由、并行执行、多 agent 协调与迭代优化。
- ⚡ **实时流**：Realtime API 可转发任意 provider 的 LLM 流到前端，无需 API routes；应用可展示 run 的进行中、完成、失败状态和 metadata，并实时更新 UI。
- 🛠️ **运行时自由**：可自定义构建过程、产物和最终容器镜像；支持通过 requirements.txt 自动安装 Python 包、生成或迁移 Prisma、控制 Puppeteer、接入 esbuild 插件、加入 FFmpeg 二进制、用 apt-get 安装系统包，以及 additionalPackages、audioWaveform 和自定义构建扩展。
- 🔄 **重试机制**：task 可配置 `maxAttempts`、`minTimeoutInMs`、`maxTimeoutInMs`、`factor`、`randomize`；提供 `catchError()` 条件重试、`retry.onThrow()` 细粒度重试、`retry.fetch()` 按响应重试和 `trigger.config` 默认配置，示例为 3 次尝试、1000 到 5000ms、factor 2。
- 📈 **伸缩与计费**：运行无超时，按代码实际执行付费，无需管理服务器；每次部署为原子版本，已启动任务不受代码变更影响；生产能力包括并发与队列、多区域 workers、静态 IP、AWS PrivateLink、弹性基础设施和自动重试。
- 🛡️ **安全更新**：新增 GitHub Actions trusted publishing，仅选定仓库、分支或环境可部署到项目；API key 支持自定义权限和团队预设；OIDC workload identity 让任务向 Anthropic 等服务证明身份，无需存储 API key。
- 📊 **可观测性**：提供 LLM observability、日志与追踪、tags、advanced run filters、run metadata、bulk actions、实时告警、查询、dashboard 和 errors；新增在同一处搜索环境中所有 run 的日志，或用 Ask Trigger 检查。
- 🌐 **开源合规**：Trigger.dev 以 Apache 2.0 开源，可查看源码、贡献和自托管；GitHub 16.8k+ stars、Discord 5.1k+ members；提供 SOC 2 Type II、HIPAA BAA 和 GDPR 合规。

### [获取失败](https://vlt.io/blog/free-public-npm-mirror)

无法总结：获取内容失败，状态码 429。

### [获取失败](https://www.vlt.io/blog/registry-metadata-70-percent-smaller)

无法总结：获取内容失败，状态码 429。

### [GitHub - ocavue/astrobook：极简的 Storybook 替代方案 · GitHub](https://github.com/ocavue/astrobook)

Astrobook 是面向多框架的极简 UI 组件 playground，作为 Storybook 的轻量替代，支持 React、Vue、Preact、Svelte、Solid、Lit 和 Astro，在统一环境中开发、测试和展示组件。它通过 Astro 集成扫描 `.stories.*` 文件，兼容 Storybook Component Story Format v3 的有限子集，支持 `args` 与 `decorators`，并提供目录、子路径、样式、head、首页和标题等配置，可独立运行或嵌入现有 Astro 项目。

- 🧩 **多框架统一环境**：支持 React、Vue、Preact、Svelte、Solid、Lit 和 Astro，可在同一 playground 中开发、测试与展示组件，示例覆盖多框架混用及 TailwindCSS、UnoCSS、PandaCSS 等集成。
- 🚀 **快速接入**：安装 `astro`、对应框架集成和 `astrobook`，在 `astro.config.mjs` 的 `integrations` 中加入 `astrobook()`，运行 `npm run dev` 后默认访问 `http://localhost:4321`。
- 🧪 **Story 约定**：扫描所有 `.stories.{ts,tsx,js,jsx,mts,mjs}` 文件；每个 story 文件包含必需默认导出和若干具名导出，兼容 Storybook CSF v3 的有限子集，支持 `args` 和 `decorators`。
- 🎨 **Decorators 限制**：decorators 由带 children slot 的组件和 props 构成，可用于包裹组件并添加样式；当前只支持样式变化，不能改变组件 context 或客户端行为，且由 Astro 渲染为 HTML 后发送到客户端。
- 🧭 **单 Story 提升**：当模块只导出一个 story 且其名称与模块同名时，该 story 会自动提升以替换父组件显示，避免侧边栏出现 `Button/Button` 这类冗余嵌套。
- ⚙️ **配置项**：支持 `directory` 指定扫描目录（默认当前工作目录），`subpath` 指定 Astrobook 子路径，`css` 导入自定义样式，`head` 指定自定义 head Astro 组件，`home` 替换首页，`homeContent` 调整内置首页内容，`title` 设置站点标题。
- 🔗 **子路径规则**：`subpath` 相对于 Astro 项目的 `base` 路径；例如 `base` 为 `/docs`、`subpath` 为 `/playground` 时，Astrobook 位于 `http://localhost:4321/docs/playground`。
- 🏢 **首页定制**：`homeContent` 可设置 `title`、`subtitle`、`version` 和 `repo`；字段可自定义、设为 `false` 隐藏或省略用默认值。`version.label` 默认显示当前 Astrobook 版本（示例 `v0.12.7`）并可链接 changelog；提供自定义 `home` 或 `home: false` 时 `homeContent` 被忽略。
- 🛠️ **按需启用**：可通过 `process.env.NODE_ENV === 'development'` 条件加入 `astrobook` 集成，仅在开发环境启用，生产构建不包含 Astrobook。
- 💬 **iframe 主题控制**：在 iframe 中运行时，可向 iframe 的 contentWindow 发送 `{ type: 'astrobook:set-theme', theme }` 消息切换主题，`theme` 取值为 `light` 或 `dark`。

### [Astrobook](https://astrobook.pages.dev/)

Astrobook 以极简 UI 组件 playground 为定位，当前页面标注版本 v0.13.3，并提供 GitHub Star 入口；原文未展开具体功能、更新内容或技术机制。

- 🧩 **核心定位**：Astrobook 被描述为 minimal UI component playground，即一个极简的 UI 组件实验环境。
- 🔗 **GitHub 入口**：页面提供 Star on GitHub，引导用户在 GitHub 上为项目标星。

### [melonJS 发布 v20.17.0 · melonjs/melonJS · GitHub](https://github.com/melonjs/melonJS/releases/tag/20.17.0)

melonJS 20.17.0 于 11 月 21 日发布，核心变化是让等距、交错和六边形 Tiled 地图像正交地图一样在 WebGL/WebGPU 上由 GPU 绘制，单瓦片层主线程耗时最多降低 98%；同时新增按图像或 Sprite 形状收拢到玩家的遮罩过渡，以及渐变映射和抖动两种效果，并集中修复 Tiled 偏移、大图块、旋转图集帧和多个渲染/物理问题。

- 🚀 **正式发布**：melonJS 20.17.0 为最新版本，包含 5 个提交，重点覆盖 Tiled GPU 渲染、遮罩过渡、新效果和一批渲染修复。
- ⚡ **GPU 地图渲染**：等距、交错和六边形 Tiled 地图现可在 WebGL 和 WebGPU 上由 GPU 绘制，无需手动开启；由单一 tileset 绘制的瓦片层会自动使用该路径（#1897）。
- 📈 **性能提升**：1200 个可见瓦片时等距瓦片层主线程耗时从 0.68 ms/帧降至 0.07 ms/帧（约 90%），4000 个时从 2.0 ms/帧降至 0.04 ms/帧（约 98%）；正交瓦片层自 19.4 起在 1000/3600 个可见瓦片下分别约降 85%/97%。
- 🧩 **遮罩过渡**：`state.transition`、`MaskEffect` 和 `Trigger` 支持以图像或 `Sprite` 作为遮罩形状，可通过 `center` 向玩家收拢，并通过 `invert` 填充形状（#1399）。
- 🎨 **渐变映射**：`GradientMapEffect` 依据亮度用 2 到 8 种颜色重着色精灵或场景，可用于队伍配色、双色调、夜景或设置 `smooth: false` 的硬调色板替换。
- 🎨 **抖动效果**：`DitherEffect` 用少量颜色和有序抖动模拟早期主机画面，可按通道设置 `levels`，或使用 2 到 16 色调色板，并按 `size` 设置像素宽度。
- 🛠️ **Tiled 修复**：Tiled 图层偏移现在会作用于瓦片层绘制与 `getTile()` 查找、对象层对象和组内瓦片层；此前偏移被忽略。大图块在视口边缘不再被裁掉，交错/六边形地图按 Tiled 的位置绘制，`tileoffset`、整像素和 GPU 正交层的软边、叠放顺序及 `margin` 读取也更一致。
- 🐛 **渲染与过渡修复**：等距/交错/六边形图层 `opacity` 低于 1 时在 WebGL/WebGPU 上整体淡出而非逐瓦片透视；移除并重新加入瓦片层、tileset 缺失瓦片不再抛错；遮罩 Sprite 随关卡消失或未给形状时只提示一次并回退到普通 iris。
- 🐛 **其他关键修复**：`NineSliceSprite` 现在响应 `flicker()`；macOS 上 `textBaseline` 为 `hanging` 的描边多行文本保留顶部轮廓；旋转图集帧绘制位置及由此生成的 `NineSliceSprite` 轴向修正；glTF Draco/meshopt 无法解码时控制台指出扩展名；物理适配器方法在无 body 对象上报错提示，raycast 跳过非适配器 body；WebGL `antiAlias` 下抓帧后再绘制不再偶发黑屏；Path2D 半圆 `A` 弧不再被舍入成直线。
- 📦 **工程与包**：依赖更新清除了安全审计报告的 46 个漏洞；lint 按包缓存，CI 修复测试页随机丢失并使测试套件耗时约减半；npm 包补回 `CHANGELOG.md` 和许可证，`sideEffects` 指向发布包；引擎下载体积约 323 kB（minified+gzip），较 350 kB 减少约 8%。

### [Replay Node 26 — Replay Blog](https://replay.io/blog/replay-node-26)

Replay Node 已正式发布并基于 Node 26 重建录制运行时，提供可完整捕获运行时行为的时间旅行录制，并可通过 Replay MCP 代理或 Replay DevTools UI 进行事后调试；它取代此前基于 Node 16 的早期 alpha，未来将跟随当前 Node 版本，但现阶段仅支持 Linux x86-64。

- 🚀 **正式发布**：Replay Node 从早期 alpha 进入 GA，基于 Node 26，面向需要调试 Node 服务端运行过程并保留完整运行时录制的用户。
- 🧩 **时间旅行录制**：录制会完整捕获运行时行为，支持通过 Replay MCP 让代理调试，或用 Replay DevTools UI 人工查看源码、执行次数、变量值和调用栈。
- ⚙️ **Node 26 能力**：录制运行时重建在 Node 26 上，支持现代 Node 能力，包括通过内置 type stripping 直接运行 TypeScript 文件；后续只跟踪当前 Node 版本，不再单独维护 Node 22 或 24 构建。
- 📦 **安装与更新**：全局安装 `@replayio/node` 后获得 `replay-node` 命令，首次运行会把运行时下载到 `~/.replay/node/node`；旧版用户需执行 `replay-node --update`，因为命令不会自动检查新版本。
- 💻 **平台限制**：Replay Node 26 目前仅支持 Linux x86-64，没有 Windows 构建，macOS 下载仍提供旧的 Node 16 运行时，Mac 构建支持计划在不久后评估。
- 🛠️ **录制服务端**：`replay-node --exec ./node_modules/.bin/next start -p 3457` 会把 Replay Node 放到 `PATH` 前面并运行命令，启动的 Node 进程会被录制；`next start` 只有一个进程，因此生成一条服务器录制，按 Ctrl+C 退出后完成写入。
- ⚠️ **Next.js 注意点**：构建时预渲染的页面不会在录制的服务器中运行，其代码不会出现；`next dev` 会启动多个 Node 进程并各自生成录制，目标通常是处理请求的 `start-server.js`，停止开发服务器时需把 `NEXT_EXIT_TIMEOUT_MS` 提高到如 `30000`，否则 Next 在请求退出约 100ms 后杀进程，录制来不及写完。
- 📝 **上传与源码映射**：使用 Replay CLI 的 `replayio upload` 上传录制，`replayio list` 查看本地录制；上传会带上 Next 生成的 source map，使开发和生产服务器录制都能显示原始 TypeScript 文件而非编译后的服务器 bundle。
- 🔍 **MCP 调试示例**：代理可通过 Replay MCP 的 `RecordingOverview` 识别框架并汇总请求；示例中识别为 Node.js v26.13.1、Next.js 16.1.6 生产模式，`Logpoint` 在 `src/actions/analytics.ts:4` 命中 5 次，返回 `name` 为 `root-layout`、`users-layout`、`root-layout`、`users-layout`、`user-profile`，`GetStack` 显示调用来自 Next 的 Server Action handler。
- 🧠 **事后检查未记录值**：时间旅行调试可在事后检查应用没有打印的值，例如在 `src/app/users/page.tsx` 的 `redirect()` 行设置 logpoint，用 `JSON.stringify(user)` 取得完整 user 对象，无需重启服务器、添加日志或复现请求。
- 🔮 **后续方向**：下一篇将回到 Nadia 的 Next.js 示例应用，展示代理同时使用浏览器录制和服务器录制调查同一批 bug，因为浏览器中出现的许多问题实际源于服务器或客户端与服务器的不一致。

### [发布 v2.3.0 · frappe/charts · GitHub](https://github.com/frappe/charts/releases/tag/v2.3.0)

Frappe Charts 发布 v2.3.0（2026-11-21，Latest），重点提升坐标轴可配置性、布局自适应能力和饼图/环形图图例展示，并修复柱列点击回调、折线值重叠及窄容器热力图溢出等问题。

- 🚀 **正式发布**：Frappe Charts 发布 v2.3.0（2026-11-21，Latest），包含 3 个提交。
- 🧩 **坐标轴配置**：新增 `xAxisTitle`、`yAxisTitle`、`hideXAxis`、`hideYAxis` 和 `xAxisLabelRotation`，可设置 X/Y 轴标题、隐藏对应坐标轴并旋转 X 轴标签。
- 🎨 **高度自适应**：`height` 设为 `100%` 时可跟随父元素高度，便于嵌入自适应布局。
- 🎨 **图例位置**：通过 `legendPosition` 将饼图和环形图的图例显示在图表旁边。
- 🐛 **柱列点击回调**：修复点击坐标轴图表的柱列时未调用 `onClick` 的问题。
- 🐛 **折线值重叠**：修复靠得很近的折线数值与数据点重叠的问题。
- 🐛 **热力图滚动**：热力图在窄容器内改为内部滚动，不再溢出容器。

### [版本 3.0.0 发布 · opensheetmusicdisplay/opensheetmusicdisplay · GitHub](https://github.com/opensheetmusicdisplay/opensheetmusicdisplay/releases/tag/3.0.0)

OpenSheetMusicDisplay 发布 3.0.0，版本号主要标志破坏性变更与 API 清理，同时带来性能、生命周期、错误处理和乐谱排版改进；多数应用无需修改代码即可升级，但需留意移除无效或弃用 API、停止修改页面全局状态，以及 load() 错误报告方式的变化。

- 🚀 **版本发布**：OpenSheetMusicDisplay 发布 3.0.0，包含 31 个 bug 修复、2 个功能和 2 项性能改进。版本号主要表示破坏性变更和 API 清理，多数应用无需修改代码即可升级，升级前应查看 changelog 末尾的 BREAKING CHANGES。
- 🧩 **单页应用生命周期**：新增 osmd.destroy()，可移除实例及其页面、光标和监听器；autoResize 通过 ResizeObserver 跟随容器宽度而非仅窗口宽度；render() 只移除自己的页面并保留容器内应用自有元素，容器隐藏时跳过渲染；最后一次 load() 生效，即使更早的请求更晚完成；被后续 load()、clear() 或 dispose() 取代的请求以 AbortError 拒绝并中止请求；新增 onRender 选项。
- ⚙️ **实例隔离**：移调、音符缩放、符干和谱线宽度、符号工厂、力度音量表改为每个 OSMD 实例独立；TransposeCalculator 也不再是静态共享，避免同一页面多个实例相互影响。相关静态 API 被移除，EngravingRules.unit 和 PageFormatStandards 变为只读。
- 🛡️ **全局副作用清理**：OSMD 不再向 Array.prototype 添加 last()、contains()、clear()，应改用 array[array.length - 1]、array.includes()、array.length = 0；setLogLevel() 只设置 OSMD 自己的 logger，不再修改 loglevel 根 logger 或写入 localStorage。
- 🛡️ **加载错误处理**：load() 失败时总是以原因 reject，格式错误的 XML 会带解析器行列号；无法读取的单个元素只跳过自身并以警告标明小节、声部和元素，不再丢弃该声部该小节剩余内容；XML 字符串错误改为 rejected promise 而非同步抛出；非 MusicXML 内容报 The file is not MusicXML，只有传给 load() 的字符串才可能被当作 URL。
- 🛡️ **资源限制**：恶意或异常小文件不能再用巨大数值耗尽内存：每声部超过 100 个谱表会加载失败，超过 100 条谱线被忽略，超过 8 个颤音记号被截为 8，均带警告；对应限制为 EngravingRules.MaxStavesPerPart、MaxStaffLines、MaxTremoloStrokes。Fraction 中 309 位以上数字导致的 Infinity 或相距很远的非整数也不再冻结页面，相关音符或 forward/backup 会跳过并警告。
- 🎨 **排版改进**：新增按 MusicXML `<dashes>` 在 cresc.、rit. 等文字后绘制虚线并跨系统换行；修复多声部休止符按声部放置、琶音与移位音符头的重叠、延音线进入第二结尾、装饰音连线、复拍子自动连桁 6/8 按 3+3、隐藏谱表时的力度位置等排版问题。
- 📦 **安装体积与依赖**：vexflow 和 loglevel 被打入 OSMD 构建并改为 devDependencies，node_modules 体积从 21 MB 降至 7.3 MB；直接 import vexflow 或 loglevel 的应用需自行在 package.json 中添加依赖。npm 包同时补发 bundle 的 LICENSE 文件。
- ⚡ **性能提升**：load() 通过省略 MusicXML 元素间空白解析，加载速度提升 12%；已显示的光标图像在重新渲染时复用，不再每次重绘。
- 🔄 **选项与缩放行为**：load() 和 clear() 保留 osmd.Zoom，不再重置为 1.0；setOptions() 可以把所有选项重新打开，例如 drawFingerings: true、disableCursor: false。依赖缩放重置的应用需要自行设置 osmd.Zoom = 1。
- 🔑 **API 清理与导出**：3.0.0 移除无效或弃用的成员，包括 MusicSheetCalculator.TextMeasurer、stafflineNoteCalculator、WebGL skyline 相关选项、VexFlowBackends、64 条无效果规则和 PagePlacementEnum；新增导出 57 个公共类型，如 PlacementEnum、TabNote、LyricsEntry、Slur、Pedal，便于 bundle 访问。

### [发布 v8.0.0 · testing-library/jest-dom · GitHub](https://github.com/testing-library/jest-dom/releases/tag/v8.0.0)

testing-library/jest-dom 发布 v8.0.0（2026-11-19），新增对 vitest 5 的支持，同时移除了对 vitest 5 以下版本的兼容支持，属于破坏性变更，使用旧版 vitest 的消费者需要先升级到受支持版本。

- 🚀 **正式发布**：testing-library/jest-dom 发布 v8.0.0（2026-11-19），并标记为 Latest 版本。
- 🧩 **Vitest 5 支持**：新增对 vitest 5 的支持（#742），使 jest-dom 可在 vitest 5 环境中使用。
- ⚠️ **破坏性变更**：移除对 vitest 5 以下版本的兼容支持，消费者必须升级到受支持的 vitest 版本。

### [Svelte Flow 2 - xyflow](https://xyflow.com/blog/svelte-flow-2-major-release)

Svelte Flow 2 在 v1 发布约一年半后推出，重点是把节点和边的更新控制权交给开发者，同时调整 hooks 的响应式写法、简化子流父子关系、改进主题与样式覆盖，并提供迁移指南和 Svelte Flow Pro 支持；同期 xyflow 宣布 Vue Flow 正式加入其生态并发布 Vue Flow 2。

- 🚀 **正式发布**：Svelte Flow 2 发布，距 v1 约一年半，包含新功能和破坏性变更，官方提供迁移指南说明升级细节。
- 🧩 **更新拦截**：新增 `onnodeschange` 和 `onedgeschange` 处理器，可在变更应用到节点和边之前检查、修改或丢弃变更，也可清空 changeset 并自行应用更新；更新节点和边的方式也更规范，需参考 Handling Updates 指南。
- 🔄 **Hook 写法**：hooks 不再需要 `$derived` 包装，改为传入返回参数的函数，例如 `useNodesData(() => ({ nodeIds }))`；Svelte 会保持函数传递值的响应性，参数变化时 hook 自动更新，但仍沿用 `use` 前缀。
- 🧭 **子流改进**：使用子流时，父节点和子节点的顺序不再重要；新增 `changeParent` 辅助函数，可将节点移动到不同父级并自动处理位置计算。
- 🎨 **主题样式**：Svelte Flow 自动跟随站点的明暗模式，也仍可强制指定模式；样式放入 CSS layer 便于覆盖，官网示例主题以 `xy-theme.css` 单独提供。
- 📦 **生态整合**：Vue Flow 加入 xyflow 并发布 Vue Flow 2，xyflow 表示已与 Vue Flow 创建者密切合作一段时间，此次将合作正式化。
- 📚 **迁移与支持**：Svelte Flow 2 迁移指南覆盖破坏性变更和更新步骤；Svelte Flow Pro 提供高级、可直接使用的 Pro 示例，订阅可支持 Svelte Flow 持续开发。

### [用于 Web 应用的 JavaScript 条形码和二维码扫描器 SDK](https://strich.io/?ref=js-weekly)

Pixelverse 的 STRICH 是面向 Web 应用的 JavaScript 条码扫描 SDK，让用户在浏览器中直接调用摄像头实时读取 1D/2D 码，主打完全客户端处理、无需后端、零依赖和低端设备性能，并通过预制扫描 UI 把集成简化为少量代码；其订阅定价按扫描量或按应用年费计算，强调离线隐私、真实设备测试和商业支持。

- 🚀 **浏览器端 SDK**：STRICH 使用手机摄像头在浏览器中实时扫描条码，完全客户端处理、无需后端，npm 包为 `@pixelverse/strichjs-sdk`，目标是让 Web 应用无需安装原生应用即可获得扫码能力。
- 🧩 **解码架构**：采用 GPU 加速的 1D/2D 解码管线并完全在设备端运行；以单个 JS 文件分发、内嵌 WASM，bundle 小于 1 MB，零依赖，兼容 vanilla JS、React、Angular、Vue 和 Svelte，可从 NPM 或 CDN 安装。
- 📦 **条码类型**：支持 Code 128、EAN/UPC、Code 39、Code 93、ITF、GS1 DataBar、Codabar、MSI Plessey、QR Code、Micro QR、Data Matrix、Aztec Code 和 PDF417；其中 PDF417 常见于登机牌和美国驾照。
- 💻 **集成与 UI**：提供预制 Popup Scanner，可用 `await PopupScanner.scan({symbologies:['code128','qr']})` 弹出扫描对话框；嵌入自有布局时带瞄准覆盖层、摄像头选择、闪光灯和点按对焦，并自动处理摄像头差异。
- 🔍 **复杂场景**：解码管线可读取褪色或破损印刷、反光和低光、瓶罐等曲面包装以及浅色码在深色背景上的反色码，文章称开源库在这些条件下常失败，并与 ZXing-JS、QuaggaJS 作对比。
- 🧪 **真机测试**：每次 SDK 发布都在实验室覆盖当前 iPhone、iPad 到低价 Android 手机和平板做 QA；文章强调模拟器无法复现摄像头差异、自动对焦和慢硬件，SDK 针对低端硬件调优，并跟踪 Safari、Chrome、Firefox 及 OS beta。
- 📊 **订阅定价**：Basic 为 €99/月，限最多 10k 次扫描/月且设备与 URL 不限；Professional 为 €249/月，限最多 100k 次扫描/月，可选扫描 UI 定制品牌；年度 Business 起价 €4,000/年，含 1 个应用，每增加 1 个应用加 €1,500/年，不限扫描和设备，可选离线许可证检查；Enterprise 起价 €7,500/年，支持采购订单、供应商注册、经销商、OEM 许可和定制条款。价格不含 VAT 和销售税，由 Paddle 作为 Merchant of Record 代收。
- ⚠️ **限额与试用**：扫描限额为软限制，绝不阻断扫描；若连续两个月超限，STRICH 会要求在 7 天内升级。订阅始终包含最新版本，提供 14 天免费试用，可随时取消。
- 🛡️ **隐私与采购**：解码完全本地进行，条码数据不离开设备；可选 Offline Operation 实现零网络流量；零依赖降低供应链风险，NPM 使用 Trusted 和 Staged 发布；支持采购订单、发票和银行转账，并可通过 SoftwareOne、SHI、worldsoft 等经销商购买；Pixelverse 是瑞士 GS1 Solution Partner 和 swiss made software 成员。
- 🧠 **商业支持**：FAQ 指出 ZXing-JS、html5-qrcode 和 QuaggaJS 处于无人维护状态或不提供商业支持，STRICH 定位为持续维护且有商业支持的替代方案；文章还引用 SBB、Brooklyn Public Library、Zeercle 等使用案例。

### [SpreadJS 产品经理办公时间 | MESCIUS](https://developer.mescius.com/spreadjs/pm-office-hours?utm_source=CooperPress&utm_medium=JavaScript-Weekly&utm_campaign=SPJS-JSWeekly-Classified-11-26)

MESCIUS 的 SpreadJS 产品经理 Chris Bannon 将举办 PM Office Hours，直接面向客户介绍产品路线图、分享产品进展和客户案例，并实时答疑；同时，SpreadJS v19.2 已发布，为其 JavaScript 电子表格组件和可选附加组件新增 What If 场景管理、增强数据绑定、Ribbon KeyTips、进度迷你图、圆角单元格边框等能力，并改进 UI/UX 与 Angular 22 兼容性，以提升分析、无障碍和布局体验。

- 🗓️ **PM Office Hours**：SpreadJS 产品经理 Chris Bannon 将主持 PM Office Hours，介绍产品路线图、分享进展和客户成功案例，并覆盖客户请求的主题；直播全程提供实时问答。
- 💬 **议题与案例征集**：客户可在 PM Office Hours 论坛提交产品问题或功能演示请求，也可提交基于 SpreadJS 的客户故事，有机会在直播中展示；直播互动渠道包括 YouTube、Twitch、X 和 Facebook。
- 🚀 **v19.2 发布**：SpreadJS v19.2 已发布，面向其 JavaScript 电子表格组件及可选附加组件带来多项增强和新功能。
- 🧩 **What If 场景管理器**：新增 What If Scenario Manager，可保存、比较并切换工作簿场景，简化假设分析。
- 🔗 **数据绑定增强**：增强数据绑定，支持将工作表、单元格和表格绑定到 `DataManager`。
- ♿ **Ribbon KeyTips**：新增 Ribbon KeyTips，改善 `Designer` 的无障碍体验和键盘导航。
- 📊 **进度迷你图**：新增 Progress Sparklines，通过基于公式的单元格内条形展示进度、KPI 和完成状态。
- 🎨 **圆角单元格边框**：支持圆角单元格边框，用于创建更精致的电子表格布局。
- 🛠️ **可选插件增强**：`Designer Ribbon`、`PivotTable`、`Collaboration Server`、`AI-Assistant`、`DataCharts`、`ReportSheet` 和 `GanttSheet` 等可选附加组件均有增强。
- ⚙️ **UI/UX 改进**：改进电子表格筛选和输入等 UI/UX，提升可用性。
- 🌐 **框架兼容**：新增对 `Angular 22` 的兼容支持。
- 🗓️ **近期直播**：近期直播日期包括 2026-11-05、2026-10-01 和 2026-09-01。

### [TWD - 开发时测试 | 浏览器内前端测试 | TWD](https://twd.dev/?utm_source=jsweekly&utm_medium=newsletter&utm_campaign=cooperpress-q4-2026#review-heading)

TWD 将前端测试放回开发者正在使用的浏览器和 dev server：在侧边栏对真实应用运行组件与流程测试，AI agent 可通过 `twd-cli` 无头执行、读取结构化失败并修复重跑，合并前还会用真实 API 校验 mock；同时提供 CI 录屏、多框架支持和 MIT 开源许可，定位为开发期快速反馈工具，而非替代端到端测试。

- 🚀 **浏览器内运行**：通过 `npm install twd-js` 和 Vite 插件，在开发服务器侧边栏直接对真实应用运行组件与流程测试，不需要另开第二个浏览器维护测试页面。
- 🧩 **真实应用测试**：测试运行在真实 dev server 和真实路由、provider 环境中；文中称合并前每个 mock 都会用真实 API 校验，以减少 mock 与真实契约的偏差。
- 🧠 **AI 闭环**：AI agent 编写测试后用 `twd-cli` 对 dev server 无头运行，读取结构化失败信息并修复重跑直至通过；结果以文本而非截图或 DOM 快照返回，降低 token 消耗，`twd-relay` 可在自有标签页中观看。
- 🛠️ **快速接入**：支持用 Claude Code 插件或 Agent Skills 让 agent 自动识别技术栈、安装 `twd-js` 与 `twd-cli` 并接入 Vite 插件；也提供手动安装路径，整体为一个包加一个插件。
- 🌐 **框架覆盖**：支持 React、Vue、Angular、Solid、Astro、Nuxt、HTMX 和 vanilla JS，适配 Vite、Webpack 或 CDN；不覆盖由服务器拥有渲染的 Next.js App Router RSC 场景。
- 🎯 **工具定位**：TWD 底层使用 Testing Library，`screenDom` 是带作用域的查询封装；它补充而非替代 Playwright/Cypress 的端到端测试，也不要求放弃 Vitest 中适合 jsdom 的纯函数测试。
- 🧪 **与 Vitest 差异**：Vitest Browser Mode 在专用 harness 页面挂载组件，TWD 则运行于实际 dev server，既可驱动整个应用的真实路由，也可用 Testing Library `render()` 挂载单组件，周边 provider、router 和 network 均为真实，并在同一会话和覆盖率报告中运行。
- 📦 **CI 录屏**：`twd-cli` 自带 GitHub Action；给 PR 加 `record` 标签后，单独任务录制该分支新增或修改的测试，每个测试一个视频并作为 artifact 上传，再由评论链接；录制作业与门禁作业分离，不会影响关键检查。
- 🛡️ **生产与许可**：所有 TWD 导入由 `import.meta.env.DEV` 保护，不会进入生产包；`twd-js`、`twd-relay`、`twd-cli` 和 `twd-ai` 均为 MIT 许可，个人和企业免费且无付费功能或用量限制。

### [React Anatomy — 3D React 组件检查器](https://react-anatomy.com/)

React Anatomy 是一款浏览器扩展，在开发者工具里新增 Anatomy 面板，把当前页面和 React 实际渲染出的组件对应起来：既能把页面拆成 3D 图层，也能跟随真实组件树，还能查看渲染结果背后的 props。它已在 Chrome Web Store 和 Firefox Add-ons 上架，Brave、Edge 可使用 Chrome 商店版本；安装和使用都不需要改动项目代码，但它依赖 React 的私有内部实现，兼容性和视觉保真度可能随版本变化。

- 🚀 **扩展上架**：在浏览器开发者工具中新增 Anatomy 面板，Chrome Web Store 可直接安装，Brave 和 Edge 可复用该商店条目，Firefox Add-ons 也提供安装；官方在 Chrome 与 Firefox 上测试。
- 🧩 **核心机制**：从运行中的页面读取 React 实际渲染的组件：图层来自屏幕上的内容，名称与嵌套关系来自 React 本身；3D 视图以页面形状为起点，Auto depth 为每个可见区域分层，输出相同的 wrapper 共享同一平面，所有捕获到的组件都保留在树中。
- 🔍 **渲染树而非导入图**：面板展示的是当前这一刻 React 渲染出的组件树，并非 import 依赖图：导入但未出现在屏幕上的组件不会显示，渲染三次的组件会出现三次并各自带有 props，文件、导入和依赖属于另一张图。
- 🎨 **示例走查**：在 orbit.react-anatomy.com 的示例中点击 Anatomy 标签、执行 Explode、选择 Inspect props，即可在组件树与 3D 视图中选中 ProjectCard，并在展开的 `project` prop 里找到卡片名称；该交互示例无需安装扩展。
- 🛠️ **零改动接入**：直接读取运行中的 React 应用，不需要安装包或修改代码，检查过程完全发生在浏览器内。
- 🎯 **典型用途**：在陌生布局中定位某块界面对应的组件及其位置，理解父子与重复组件的结构以及列表传给每个子项的 props，排查位置或取值异常的组件，为 PR 导出带标注和关键 props 的图片，以及在接手 AI 生成的页面时先看它渲染了什么、嵌套多深、带了哪些 props。
- ⚠️ **限制与边界**：依赖 React 的私有内部实现，因此兼容性与视觉保真度可能变化，具体能观察到什么以文档为准；它只是检查器而非代码审查器，只呈现结构、不评价结构好坏。
- 💡 **由来**：作者过去要靠记忆和源码在 Excalidraw 里手画框图（侧边栏、列表卡片、卡片内的徽章），既耗时又只是对代码的解读；现在这张图直接由运行中的页面生成。

### [React Anatomy — 3D React 组件检查器](https://react-anatomy.com/#demo)

React Anatomy 是一款浏览器扩展，在开发者工具中加入 Anatomy 面板，把当前页面与 React 实际渲染的组件对应起来，支持 3D 分层、查看真实组件树和 props，帮助理解页面组成、排查异常和解释改动；它直接读取运行中的 React 应用，无需改包或代码，但依赖 React 私有内部机制，兼容性和视觉保真度可能变化。

- 🚀 **扩展发布**：在浏览器 DevTools 中新增 Anatomy 面板，已上架 Chrome Web Store 和 Firefox Add-ons；Brave、Edge 可使用 Chrome Web Store 版本，官方测试覆盖 Chrome 和 Firefox。
- 🧩 **真实渲染树**：从运行中的 React 应用读取当前渲染的组件树，而不是导入图：被导入但未出现在屏幕上的组件不显示，渲染三次的组件会出现三次并各自带有 props。
- 🛠️ **零改动接入**：无需安装包或修改应用代码，检查在浏览器内完成，适合直接在现有页面上观察组件结构与数据。
- 🎨 **3D 分层**：3D 视图从页面实际布局出发，Auto depth 分离可见区域，输出相同的 wrapper 共享平面，同时所有捕获组件仍保留在树中。
- 🔍 **定位与读值**：选中页面元素可找到渲染它的组件及所处层级，查看父子、重复组件结构和列表传给每项的 props，并读取组件实际收到的值。
- 📝 **协作说明**：可聚焦改动区域并导出带标签和关键 props 的图片，用于在 pull request 中配合 diff 解释结构变化。
- 🧭 **适用场景**：适用于陌生布局导航、理解 React 组合与数据流、排查错位区域或异常值、审阅 AI 生成页面等需要理解页面而非只改页面的时刻。
- ⚠️ **边界与限制**：React Anatomy 是检查器而非代码审查器，不评价结构好坏；它使用 React 私有内部机制，兼容性和视觉保真度可能变化，捕获范围也有限，文档会说明当前可观察内容。

### [React2STEAL 利用 GitHub Actions 攻击 React2Shell | OpenSourceMalware](https://opensourcemalware.com/blog/react2steal-github-actions)

OpenSourceMalware 将一套以公开 GitHub 仓库为载体、利用 GitHub Actions 自动化扫描并攻击 React/Next.js 服务器的活动命名为 React2STEAL：45 个仓库分三波创建，利用 React2Shell（CVE-2025-55182）和 Next.js 中间件授权绕过（CVE-2025-29927），在入侵后窃取环境变量、云凭据、配置文件和 AI key，并把战利品提交回同一公开仓库；至少 1,281 个受害主机名和与 wfx-loot 的账号重叠表明，被盗 GitHub token 正被持续复用，公开仓库外泄和 CI 秘密暴露成为核心风险。

- 🚀 **活动曝光**：OpenSourceMalware 确认 45 个公开 GitHub 仓库以 `ci-wk-<number>` 命名，分三波创建于 10 月 22 日、11 月 11 日和 11 月 14 日；这些仓库本身是攻击基础设施而非供安装的 Action，截至 11 月 17 日仍在约每 11 分钟提交新结果。
- 🧩 **攻击链**：仓库内的 `.github/workflows/scan.yml` 通过 `workflow_dispatch` 接收 `chunk` 主机列表，用 `prefilter_nextjs.py` 以 400 并发筛出 Next.js 目标，再由两个 `batch_output.py` 扫描进程各以 250 并发利用，最后用 `contents: write` 和 `if: always()` 执行 `git add`、`git commit`、`git push` 回传结果。
- ⚠️ **漏洞利用**：利用 React Server Components 19.0.0、19.1.0、19.1.1、19.2.0 中的 React2Shell（CVE-2025-55182）预认证 RCE，并尝试七种请求变体（分块编码、8 KB 填充、随机 multipart 边界、空字节等）；同时探测 Next.js 中间件授权绕过 CVE-2025-29927 的 `x-middleware-subrequest`，再经 `/_next/image` SSRF 访问 `169.254.169.254` 获取 IAM 角色临时 AWS 凭据。
- 🔑 **窃取内容**：`fast_recon.js` 在受害 Node.js 进程内收集环境变量、云凭据、Kubernetes token、`.env` 和配置文件，较新变体回传最多 300 KB 的完整 `.env`/配置内容；按 10 家 AI 提供商的 28 个环境变量名找 key，并用小模型、20 token 的真实推理请求验证 OpenAI、Anthropic、Gemini 等 key，DeepSeek 和 OpenRouter 还会查余额，请求使用桌面 Chrome UA 绕过 Cloudflare。
- 📦 **外泄方式**：窃取结果以明文、JSON 和 ZIP 三种格式提交到同一公开仓库，提交作者为 `w <w@w>`；Telegram bot token 和 chat ID 硬编码但 `SEND_TELEGRAM` 默认 0，公开仓库才是主外泄通道。11 个可访问仓库快照含约 9,100 个 ZIP、3,800 个 JSON、3,000 条明文记录，约 7.4 GB。
- 📊 **影响规模**：34 个有结果的活跃仓库合计至少 1,281 个唯一受害主机名，覆盖约 1,100 个域名，单仓库 38 到 894 个；一个第一波仓库有 1,266 个 `hosts_<date>_<time>.txt`，每个 20,000 主机名，合计约 1,800 万个唯一主机名。结果文件含进程环境 dump，常见凭据为数据库 URL、Stripe key 和 AI key；第三波 5 个仓库仅有相同的 1,845 主机目标列表，尚无结果。
- 🧭 **归属线索**：运营者未知，最佳线索是 GitHub 账号 `dascxzcw`，其现返回 404，但 `w <w@w>` 结果提交仍归因于它；45 个仓库属于 44 个所有者，26 个可读资料显示中位数 4 个公开仓库、6 个仅有该公开仓库、20 个无关注者，代码和时序更像令牌被盗后账号被滥用而非所有者主动攻击。
- 🔗 **wfx-loot 关联**：独立活动 wfx-loot 自 11 月 10 日起用被劫持 GitHub 账号窃取 CI secret，报告规模达 4,837 个账号、66,200 个探针 PR、8,093 个公开仓库含恶意提交、至少 1,835 个仓库执行 payload；39 个可检查 React2STEAL 仓库中 25 个有 `wfx-docs` 探针分支，24 个的 `docs/wfx-audit.md` 与 blob `ee6e5addfe591923fc385553cb66cf0d25634a6b` 完全一致，38 个所有者中 25 个有探针 PR。两者无共享代码和基础设施，无法判定同一或两个运营者，但同一批令牌在两次活动中持续可用；另有 5 个仓库出现无法归属的 `ci-sync-<6字符>` 分支，提交 18 行 workflow 将 secrets 以 base32 打印到日志，Actions 历史无运行记录。
- 🧠 **AI 辅助迹象**：代码注释出现 `operator format`、`operator directive`、带日期的变更日志、45 个已知漏洞主机的命中率表、程序输出 emoji、被隐去的 bot 名和 `DEDUP_BLOCK_v1` 横幅，符合 AI 编码助手参与的特征；但未发现 SentinelOne 列出的 ARTEX 痕迹，如 `artex-probe`、`artex`/`artx` 字符串或特殊 UA，脚本使用普通 Chrome UA，不能据此归因到 ARTEX 或特定模型。
- 🛡️ **处置建议**：排查请求和 WAF 日志中的 `x-middleware-subrequest` 头以及指向云元数据地址的 `/_next/image?url=` 请求；一旦命中，轮换该服务器进程可触达的所有 secret 并视配置文件已泄露，审查 AI key 使用；在代理/WAF 剥离或拒绝该头，启用 IMDSv2，若应用设置 `NEXT_PUBLIC_OPENAI_API_KEY` 应无条件轮换。
- 🔍 **GitHub 狩猎**：不要只搜仓库名，应按内容搜 `batch_output.py`、`prefilter_nextjs.py`、`fast_recon.js` 同时出现的仓库，并用 `Capture FULL env vars for exploitation`、`bissa_cve_boundary` 等字符串交叉验证；检查 `wfx-docs` 分支、标题为“docs: dependency audit notes”的 PR、`docs/wfx-audit.md` blob 哈希，以及对 CI runner 设置出站 allowlist；匹配账号应撤销 token 和应用授权，删除仓库不是修复，克隆、fork、缓存和 Git 历史仍保留数据，暴露过的 secret 必须轮换。
- 🗓️ **时间线**：仓库创建分三波：10 月 22 日 02:05–02:13 至少 26 个，11 月 11 日 04:15–04:16 共 8 个，11 月 14 日 14:43–14:44 共 5 个；脚本注释日期为 2026 年 9 月 10 日至 10 月 9 日，早于首个仓库，作者笔记称 9 月 10 日已在高量运行，但日期未经验证。

### [React2STEAL：它是什么以及需要检查什么](https://www.chainguard.dev/unchained/react2steal-what-it-is-and-what-to-check)

2026 年 11 月 18 日，OpenSourceMalware 披露 React2STEAL 自动化利用活动：攻击者利用被劫持的 GitHub 账号及其 Actions 运行器，扫描互联网上的 React/Next.js 服务器，并利用两个已修补漏洞 CVE-2025-55182 React2Shell 与 CVE-2025-29927 Next.js 中间件绕过，窃取环境变量、配置文件、云凭证和 API 密钥后提交到公开 GitHub 仓库；这不是供应链攻击，暴露规模至少 1,281 个主机名，凸显补丁滞后与令牌治理问题。

- 🚀 **活动定性**：React2STEAL 是自动化利用活动，不是供应链攻击；没有 npm 包、GitHub Action 或维护者账号被篡改，攻击者只是把 GitHub 托管运行器当免费算力，报告时间为 2026 年 11 月 18 日。
- 🧩 **两个已修补漏洞**：CVE-2025-55182 React2Shell 是 React Server Components 预认证 RCE，CVSS 10.0，影响 React 19.0.0/19.1.0/19.1.1/19.2.0 及基于它们的框架；修复版本包括 React 19.0.1、19.1.2、19.2.1 和 Next.js 15.0.5、15.1.9、15.2.6、15.3.6、15.4.8、15.5.7、16.0.7。CVE-2025-29927 是 Next.js 中间件授权绕过，携带 `x-middleware-subrequest` 可跳过中间件，影响 11.1.4 至 15.2.2，修复于 15.2.3、14.2.25、13.5.9、12.3.5；另有 `/_next/image` 云元数据 SSRF 配置风险。
- ⚙️ **攻击流水线**：每个仓库运行 `scan.yml`，经 `workflow_dispatch` 在 `ubuntu-latest` 上执行；`prefilter_nextjs.py` 以最多 400 并发筛出 Next.js 主机，`batch_output.py` 用两组各 250 并发扫描器尝试七种 React2Shell 变体（分块编码、8 KB 填充前缀、随机 multipart boundary），失败后再试中间件绕过和 `/_next/image` SSRF；成功后 `fast_recon.js` 在受害者 Node.js 进程内执行，无需在受害者机器安装或下载第二阶段载荷。
- 📦 **窃取与回传**：载荷收集进程环境、主机名、网络接口、监听端口、云凭证文件、Kubernetes 令牌和 `.env`/配置文件，新变体最多返回 300 KB 完整配置；还会用受害者服务器测试最多十家 AI 提供商密钥（含 OpenAI、Anthropic、Gemini）并发起真实推理请求、查询余额，调用源 IP 为受害者，可能产生费用。
- 📈 **暴露规模**：截至 2026 年 11 月 18 日发现 45 个仓库、44 个账号，其中 34 个仓库有结果；目标主机 20,000+，唯一受害主机名至少 1,281 个、域名约 1,100 个；抽样的 11 个仓库约 7.4 GB，含 9,100 个 ZIP、3,800 个 JSON、3,000 条明文记录；仓库约每 11 分钟提交新结果，三波创建于 10 月 22 日、11 月 11 日和 11 月 14 日，数据写在公开仓库且保留在 git 历史，删除或转私有不能清除克隆、分叉和缓存。
- 🔍 **日志指标**：请求或 WAF 日志中出现重复五次的 `x-middleware-subrequest` 头、指向 `169.254.169.254` 等云元数据地址的 `/_next/image?url=` 请求、带 `Next-Action: x` 和 `bissa_cve_boundary` multipart boundary 的请求；出站日志、AI 提供商用量和账单中出现 Web 服务器向 OpenAI、Anthropic、Gemini 等发起调用或余额异常。前三项命中说明扫描器到达，不等于利用成功，但应假定进程可读数据已公开。
- ✅ **修复与缓解**：补丁是根本修复，应升级到所在版本线的最新补丁，而不只是首个修复版；后续 CVE-2025-55183、CVE-2025-55184、CVE-2025-67779 修复相关信息泄露和 DoS，因此需升级最新补丁。检查 lockfile 和 SBOM，防止传递依赖 `react-server-dom-webpack` 或 `react-server-dom-turbopack` 仍锁定漏洞版本。若日志命中，轮换进程可访问的全部环境变量和配置文件，包括数据库 URL、Stripe、云凭证、Kubernetes 令牌和 AI 密钥，并从首次命中请求起审查用量；边缘层删除或拒绝 `x-middleware-subrequest`，启用 IMDSv2，限制 `images.remotePatterns`，WAF 规则只作纵深防御。
- 🔄 **wfx-loot 关联**：44 个 GitHub 账号所有者被评估为受害者；检查的 39 个 React2STEAL 仓库中 25 个带有 wfx-loot 探测分支 `wfx-docs` 和文件 `docs/wfx-audit.md`（blob `ee6e5addfe591923fc385553cb66cf0d25634a6b`），38 个被搜账号中 25 个有探测 PR，4 个有 `ci: refresh build cache`、`ci: restore` 载荷提交；wfx-loot 自 11 月 10 日起用约 4,800 个被盗账号向数千仓库推送 CI 密钥窃取器，且一分钟内回滚删除，而 React2STEAL 将战利品公开数周。
- 🛡️ **GitHub 账号检查**：搜索未创建的 `ci-wk-<number>` 仓库、`wfx-docs` 分支、标题为 `docs: dependency audit notes` 的 PR，以及工作流运行编号缺口；发现后按账号失陷处理，撤销 PAT 和 OAuth 应用授权、轮换受影响仓库所有密钥、审查窃取器可能植入的云信任关系。CI 运行器出站允许列表可阻断 wfx-loot 外传，但挡不住从攻击者自有仓库运行的 React2STEAL；按仓库名搜索不可靠，可用 `ci-wk` 标签和 `filename:fast_recon.js "llm_checks" "writable_paths"` 等内容搜索。
- 🧪 **Chainguard 状态**：文中称 Chainguard 不受影响，安全团队已对 GitHub 组织和端点核查无匹配，镜像及 chainguard.dev 上的 React/Next.js 均达到或高于修复版本（公开措辞待安全签核）。作者强调 GitHub Actions 加固不会阻止该活动，因为攻击者使用自有 workflow；Chainguard Libraries for JavaScript 通过 SLSA Level 3 构建、签名来源和 SBOM 帮助确认实际运行版本，Chainguard Repository 可对构建可拉取内容设策略。
- 🧠 **关键判断**：该活动不是可信包源或 Actions 能预防的供应链问题，而是大量服务器在修复发布数月后仍运行漏洞版本，并被劫持账号当作算力；被盗令牌不会被只用一次，两个活动之间无人撤销。令牌获取方式尚未确定，研究者提出第三方 GitHub 应用 OAuth 令牌泄漏可能，但无直接证据。
- ⚠️ **限制**：1,281 等数字是下限，早前结果文件未读取；研究者尚未测试暴露凭证是否仍有效，受影响组织披露另行处理。多数受害者是中小型组织，许多是开发、预发布或管理主机，通常运行旧框架并持有更大权限凭证。

### [2026 年 JavaScript 现状](https://survey.devographics.com/en-US/survey/state-of-js/2026)

总结失败：模型未返回符合格式的摘要。

### [2026 年 HTML 现状](https://2026.stateofhtml.com/en-US/)

State of HTML 2025 调查以“回归浏览器基础能力”为主题，回顾 Web API 曾落后于原生端、促使 JavaScript 框架大量涌现的阶段，并指出如今框架格局已收敛、更新放缓，浏览器厂商转而加强协作以更快发布跨浏览器一致的新特性；在 AI 辅助代码生成可能绕过框架直接调用浏览器 API 的背景下，调查旨在帮助开发者重新掌握现代浏览器能力。页面同时列出调查周期 2026-10-01 至 2026-11-01、2,091 名受访者以及数据下载入口。

- 🗓️ **调查概况**：页面标注调查开始日期为 2026-10-01、结束日期为 2026-11-01，共有 2,091 名受访者，并提供 Survey Archive、Review Questions、Get Data 和 Download 入口。
- 🔄 **趋势反转**：Web API 过去相对原生能力有限，复杂布局常依赖取巧手段，促使 JavaScript 框架、库和周边工具爆发式增长；如今 JavaScript 框架已收敛到少数成熟选项，变化速度放缓。
- 🌐 **浏览器协作**：浏览器厂商已开始协同工作，以更快的速度发布新特性，并确保这些特性在各浏览器中一致可用。
- 🧠 **AI 与浏览器 API**：AI 辅助代码生成正在广泛采用，它在合适场景下会跳过 JavaScript 框架，直接利用浏览器 API，因此重新熟悉现代浏览器能力变得更重要。
- 🎯 **调查目标**：调查希望帮助开发者回归基础，补足对现代浏览器实际能力的认知，以应对平台能力提升和开发方式变化。

### [HTML 2026 现状：结语](https://2026.stateofhtml.com/en-US/conclusion/)

文章围绕近期 HTML 开发者调查结果，梳理 Web 基础层的新变化：声明式 HTML 和新表单能力持续补齐，dialog、popover 等特性已显著降低交互实现成本；与此同时，datalist、WebUSB、SpeechRecognition 和 model 等特性仍未获得广泛采用，移动操作系统对 Web 的影响以及无障碍支持成为主要痛点。作者认为平台方向正确，HTML 的演进虽慢但更审慎，基础依然稳固。

- 🚀 **权限声明化**：浏览器正在试验无需 JavaScript 即可让用户授予摄像头等权限的新元素，减少脚本依赖。
- 🎨 **表单能力扩展**：可定制 select 接近在所有浏览器落地，color、switch、showPicker() 以及可能的 rangegroup 等新表单能力正在出现。
- 🧩 **声明式交互**：dialog、details、popover 已可直接使用；`command="show-modal" commandfor="dialog"` 比自写 click 处理器代码更少且处理更多情况。
- ⚡ **基础层不止用户界面**：speculation rules、声明式 WebMCP、loading 和 fetchpriority 可帮助用户代理优化数据加载与交互，用户通常无需感知。
- ⚠️ **部分特性遇冷**：datalist 难以可靠当作带搜索框的 select 使用；WebUSB、SpeechRecognition 用例有限；model 仅用于展示静态 3D 模型文件。
- 🌐 **浏览器差异转向**：浏览器差异仍是长期痛点，但问题从实现行为不一致，转为部分浏览器尚未跟上新能力。
- 📱 **移动 OS 影响突出**：移动操作系统及其 UI 选择对 Web 的冲击成为今年主要痛点，作者认为移动 OS 相对不成熟。
- ♿ **无障碍受重视**：无障碍是调查受访者的首要关注之一，与良好 HTML 相互交织；浏览器应帮助开发者判断是否照顾到所有用户。
- 🔮 **后续愿望清单**：可定制 select 落地后，下一步是全面定制表单相关控件，先从 datalist 开始；HTML includes 也在高优先级清单中。
- 🧪 **OpenUI 探索**：OpenUI 正在推进 tabs 和 focusgroup 等工作，并引发应用型组件是否已足够标准化的讨论。
- ✅ **平台方向**：dialog 和 popover 的广泛支持已消除主要痛点，可定制 select 也将如此；HTML 演进较慢但更审慎，基础层状态良好。
