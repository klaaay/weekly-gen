### [una.im | 使用 light-dark()、contrast-color() 和样式查询实现现代 CSS 主题化](https://una.im/modern-css-theming/)

**原文标题**: [una.im | Modern CSS theming with light-dark(), contrast-color(), and style queries](https://una.im/modern-css-theming/)

## 概述总结
现代 CSS 通过组合`light-dark()`、`contrast-color()`和`@container style()`等新特性，实现了声明式、可组合的动态主题系统，支持宏观主题（页面级明暗切换）和微观主题（组件级自适应配色），所有主流浏览器已于 2026 年 5 月全面支持。

- 🎨 **核心函数**：`light-dark()`根据`color-scheme`自动切换颜色值，比媒体查询更灵活，支持继承和覆盖
- 🌓 **阴影切换**：通过`light-dark()`让阴影层在亮色模式可见、暗色模式透明，同时暗色模式自动显示霓虹边框发光效果
- 📐 **自动对比度**：`contrast-color()`根据背景色自动返回黑或白文本，确保 WCAG 可访问性，一行代码解决可读性问题
- 🎭 **风格分支**：`@container style()`结合`contrast-color()`检测结果，实现基于背景明暗的定制调色板（如暖色调或深色调）
- ⚙️ **自定义函数**：`@function`可封装重复逻辑（如阴影生成），但浏览器支持有限（Chrome 139+）
- 🧩 **完整流程**：每个卡片只需传入`--brand-color`，系统自动推导背景、阴影机制、文本颜色和色调分支
- 🌐 **浏览器支持**：2026 年 5 月起所有主流引擎稳定支持，无需 polyfill
- 💡 **扩展建议**：可结合现代 CSS 颜色函数构建完整品牌系统，实现更丰富的动态主题

---

### [适用于任意规模时间序列工作负载的 Postgres。| Tiger Data](https://www.tigerdata.com/go/trial?utm_source=content-syndication&utm_medium=referral&utm_campaign=frontend-focus-newsletter)

**原文标题**: [Postgres for time-series workloads at any scale. | Tiger Data](https://www.tigerdata.com/go/trial?utm_source=content-syndication&utm_medium=referral&utm_campaign=frontend-focus-newsletter)

Tiger Cloud 提供专为时间序列工作负载优化的 Postgres 服务，支持极大规模数据处理，并提供免费试用额度。

- 🚀 支持单服务每日处理 3 万亿指标、3PB 数据及 1 千万亿数据点
- 💰 新用户可获$1000 额度（30 天有效），无需信用卡
- 📈 通过读写分离（最多 10 节点）和分层 SSD/S3 存储实现无缝扩展
- 🔄 计算与存储分离，避免为闲置容量付费，独立优化成本性能
- 🛡️ 企业级安全：多 AZ 集群、自动故障转移、SOC 2/HIPAA/GDPR 合规
- 🔍 深度可观测性：查询下钻与仪表盘，集成 CloudWatch/Datadog/Prometheus
- ⚡ 快速部署：数分钟内通过 SQL/CLI/Terraform 等工具完成数据库配置
- 🔌 支持主流云提供商及 Postgres 生态集成
- 🏢 企业功能：SLA 保障、区域数据隔离、24/7 专家支持

---

### [获取失败](https://hacks.mozilla.org/2026/06/pact-anonymous-credentials-for-the-web/)

**原文标题**: [Failed to retrieve](https://hacks.mozilla.org/2026/06/pact-anonymous-credentials-for-the-web/)

无法总结：获取内容失败，状态码 403。

---

### [Astro 7.0 | Astro](https://astro.build/blog/astro-7/)

**原文标题**: [Astro 7.0 | Astro](https://astro.build/blog/astro-7/)

Astro 7 正式发布，专注于性能提升，带来了多项重大更新，包括 Rust 重写的编译器、更快的 Markdown 处理、新的渲染引擎、高级路由、缓存功能和对 AI 开发的支持。

- 🚀 **性能大幅提升**：构建速度提升 15-61%，部分站点甚至快两倍以上。这得益于 Rust 重写的 `.astro` 编译器、新的 Rust Markdown/MDX 处理管道、更快的队列式渲染引擎，以及升级到 Vite 8 和其新的 Rolldown 打包工具。
- 🦀 **Rust 编译器**：全新的 `.astro` 编译器完全用 Rust 编写，不再进行 HTML 修正，对未闭合标签等错误更严格，并采用 JSX 风格的空白处理方式。
- 📝 **Rust 驱动的 Markdown 与 MDX**：默认使用新的 Rust 处理器 Sätteri，它原生支持 GFM、数学公式、标题 ID 等多种 Markdown 特性，无需额外插件，显著加快 Markdown 密集型站点的构建。
- ⚙️ **队列式渲染**：新的队列式渲染引擎取代了递归方法，速度提升约 2.4 倍，并且内存占用更少。
- 🗺️ **高级路由**：新增 `src/fetch.ts` 入口点，允许开发者通过标准 `fetch` 处理器模式完全控制 Astro 的请求管道，并兼容 Hono 框架，可灵活组合中间件。
- 💾 **路由缓存与 CDN 缓存**：稳定了路由缓存功能，提供平台无关的 `Astro.cache` API。新增对 Netlify、Vercel 和 Cloudflare 的实验性 CDN 缓存提供商支持，可将缓存指令推送至边缘网络。
- 🤖 **AI 增强**：为 AI 编码代理优化开发体验，包括可后台运行的开发服务器（`astro dev --background`）、自动检测代理环境、以及可配置的 JSON 日志输出，便于机器解析。
- 🎉 **社区与升级**：感谢所有贡献者。现有项目可通过 `@astrojs/upgrade` CLI 工具升级，新项目使用 `npm create astro@latest` 创建。

---

### [Vite 8.1 发布！| Vite](https://vite.dev/blog/announcing-vite8-1)

**原文标题**: [Vite 8.1 is out! | Vite](https://vite.dev/blog/announcing-vite8-1)

Vite 8.1 正式发布，带来了多项实验性功能和性能改进，旨在提升大型应用的开发体验。

- 🚀 **实验性打包开发模式**：通过 `--experimental-bundle` 启用，可将开发服务器性能提升高达 15 倍启动速度和 10 倍页面重载速度，特别适合大型应用。
- 🧩 **实验性块导入映射**：利用 import maps 解决块哈希级联问题，提高缓存效率，减少不必要的重新哈希。
- 🌐 **Wasm ESM 集成支持**：可直接导入 `.wasm` 文件并调用其导出函数，简化 WebAssembly 的使用。
- ⚡ **Lightning CSS 默认化进展**：新增对 PostCSS 中缺失功能的支持（如外部 CSS 导入和插件文件依赖注册），为未来默认切换做准备。
- 🔍 **import.meta.glob 大小写不敏感匹配**：新增 `caseSensitive: false` 选项，支持不区分大小写的文件匹配。
- 🖼️ **自定义 HTML 元素和属性资产发现**：通过 `html.additionalAssetSources` 配置，可发现自定义元素和属性中的资源（如 `<html-import>` 或 `data-src-dark`）。
- 📈 **下载量接近 Vite 7 总和**：周下载量达 4160 万次，社区贡献者超 1200 人。

---

### [波浪形/波形输入范围滑块](https://css-tip.com/wiggly-range-slider/)

**原文标题**: [Wiggly/Wavy Input Range Slider](https://css-tip.com/wiggly-range-slider/)

本教程介绍了如何用纯 CSS 创建波浪形/弯曲的输入范围滑块，无需 JavaScript，仅通过原生 HTML `<input>` 元素和 CSS 变量实现动态效果。

- 🎨 **纯 CSS 实现**：利用 `border-shape`、Scroll-Driven Animations 和 `@property` 等现代 CSS 特性，无需额外 HTML 元素或 JavaScript。
- 🛠️ **高度可定制**：通过 `--s`（滑块高度）、`--t`（拇指大小）、`--l`（线条厚度）、`--c`（主色）和 `--p`（线条形状）等 CSS 变量轻松控制外观。
- 📐 **形状生成工具**：使用作者提供的波浪分割生成器，选择“仅边框”配置、“顶部”方向，设置尺寸 100% 并调整粒度，即可获取线条形状代码。
- ⚠️ **Chrome 专属体验**：该演示目前仅支持 Chrome 浏览器。
- 🔗 **延伸阅读**：文中还推荐了其他相关 CSS 技巧，如用现代 CSS 弯曲直线和连接圆圈的曲线线条。

---

### [我把一个网站存进了图标里](https://www.timwehrle.de/blog/i-stored-a-website-in-a-favicon/)

**原文标题**: [I Stored a Website in a Favicon](https://www.timwehrle.de/blog/i-stored-a-website-in-a-favicon/)

概述总结  
作者探索了将网站内容存储在 favicon（浏览器标签页图标）中的技术实验，通过将 HTML 数据编码为像素颜色值，实现了在 9x9 像素的小图标中嵌入完整网页，并展示了如何用 JavaScript 解码还原。虽然实用性有限，但体现了数据存储的边界测试。

- 🧠 受之前鼠标 DPI 寄存器存储数据启发，作者开始将各种设备视为潜在存储空间  
- 🖼️ Favicon 本质是图像，图像由像素组成，像素可存储字节数据  
- 🔍 采用隐写术思想，将 UTF-8 编码的 HTML 直接写入像素的 RGB 通道  
- 📦 示例 HTML 有效载荷仅 208 字节，加上 4 字节长度头，共 212 字节  
- 📐 最小可容纳的方形图像为 9x9 像素（81 像素），容量 239 字节，使用率 87%  
- 🔄 解码过程：浏览器加载 favicon→绘制到画布→读取像素 RGB→重构字节数组→提取有效载荷→解码为 HTML  
- ⚠️ 关键限制：需要额外的 JavaScript 引导程序来解码图像，favicon 本身不包含完整网站逻辑  
- 🤷 实用性为零：存储量小、依赖 JavaScript、有更优替代方案，但旨在测试技术边界  
- 💡 其他方法：SVG favicon 直接存储标记、利用 PNG 注释块（tEXt 等）、ICO 文件格式多图标特性  
- 🔗 提供演示链接和 GitHub 源码供参考

---

### [Wes Bos 在 X 上：“如果我们直接通过视频流式提示用户界面会怎样？https://t.co/kfksHnsYfY” / X](https://x.com/wesbos/status/2067635204055789877)

**原文标题**: [Wes Bos on X: "What if we just prompt user interfaces and streamed them in via video? https://t.co/kfksHnsYfY" / X](https://x.com/wesbos/status/2067635204055789877)

概述总结  
- 🎥 提出通过视频流式传输用户界面的概念，以替代传统交互方式  
- 💬 强调直接通过提示（prompt）生成界面，而非手动编码  
- ⏱️ 示例中显示时间戳为 2026 年 6 月 18 日下午 3:47，体现未来技术设想  
- 📊 获得 45.3K 浏览量、35 条回复、23 次转发、501 次点赞和 216 次收藏，引发广泛讨论  
- 🔄 可能涉及动态 UI 生成与实时流式传输的结合应用

---

### [你的网格布局很可能不符合 WCAG 2.4.3 标准 - Manuel Matuzovic](https://matuzo.at/blog/2026/grid-lanes-accessibility)

**原文标题**: [Your Grid Lanes will likely fail WCAG 2.4.3 - Manuel Matuzovic](https://matuzo.at/blog/2026/grid-lanes-accessibility)

## 概述总结
CSS Grid Lanes（瀑布流布局）默认会导致视觉顺序与 DOM 顺序不匹配，从而违反 WCAG 2.4.3 无障碍标准，但可通过调整 flow-tolerance 或未来使用 reading-flow 属性来改善。

- 🚨 **默认无障碍问题**：Grid Lanes 自动填充项目的特性会导致键盘导航和屏幕阅读器的焦点顺序与视觉顺序不一致，违反 WCAG 2.4.3 要求。
- ⚖️ **flow-tolerance 属性**：通过设置容差阈值（默认 1em），可减少顺序错乱，但高容差值可能导致列高度失衡，且无法完全解决问题。
- 🧪 **reading-flow 前景**：该属性可强制阅读/焦点顺序匹配视觉顺序，但目前仅支持常规 Grid 和 Flex，尚未在 Grid Lanes 中实现。
- 🖼️ **实际案例风险**：WebKit 的 Grid Lanes 演示（如图片库）默认存在严重顺序错乱，即使调整 flow-tolerance 至 10rem 仍不达标，需 640px 容差才能消除错位。
- ⚠️ **浏览器支持现状**：Safari 已原生支持 Grid Lanes 但无 reading-flow，Chrome/Edge 需开启实验标志且 reading-flow 不适用于 Grid Lanes。
- 💡 **临时解决方案**：使用`:has(:focus-visible)`在获得焦点时切换为常规 Grid，但可能引起布局突变和屏幕阅读器问题。
- 📝 **开发者建议**：始终测试键盘和屏幕阅读器兼容性；优先调整 flow-tolerance；未来采用 reading-flow；若无效则改用常规 Grid 布局。

---

### [使用视图过渡动画化对话框元素 - Pqina](https://pqina.nl/blog/animating-the-dialog-element-using-view-transitions/)

**原文标题**: [Animating The Dialog Element Using View Transitions - Pqina](https://pqina.nl/blog/animating-the-dialog-element-using-view-transitions/)

- 本文介绍了如何使用 View Transition API 为 `<dialog>` 元素添加动画，并遵循渐进增强原则，仅在浏览器支持且用户允许动画时启用。
- 🎬 通过 Invoker Commands API 实现无 JavaScript 的对话框开关，使用 `command` 和 `commandfor` 属性链接按钮与对话框。
- 🔄 View Transition API 创建对话框从按钮“起源”的动画效果，增强视觉关联性，例如在 FilePond v5 中用于输入按钮与模态框的过渡。
- ⚙️ 代码示例展示了如何通过 `startViewTransition` 切换 `viewTransitionName`，在打开和关闭对话框时在按钮与对话框之间移动动画名称。
- 🚫 使用 `prefers-reduced-motion` 检测用户偏好，避免在禁用动画时运行过渡，确保无障碍性。
- 🛠️ 分别动画化按钮和按钮标签，防止文本缩放失真；CSS 设置 `overscroll-behavior: contain` 防止对话框打开时页面滚动。
- 📝 通过 `::view-transition` 伪元素自定义过渡动画效果，并提醒使用 `request-close` 而非 `close` 命令以触发 `cancel` 事件。

---

### [Expo — 使用 React 构建原生应用](https://expo.dev/?utm_source=frontendfocus&utm_medium=email&utm_campaign=33087804-React%2520to%2520Native&utm_content=https://expo.dev/)

**原文标题**: [Expo — Build Native Apps with React](https://expo.dev/?utm_source=frontendfocus&utm_medium=email&utm_campaign=33087804-React%2520to%2520Native&utm_content=https://expo.dev/)

### 概述总结
Expo 是一个全栈式 React Native 框架，提供强大的云服务，帮助开发者高效完成应用开发、部署和迭代的全生命周期。

- 📱 **一站式开发工具**：Expo 提供 100+ 生产级库、模块 API 和配置插件，支持 React、Kotlin、Swift 原生代码编写，是 Meta 官方推荐的唯一原生框架。
- 🚀 **高效部署与更新**：通过 EAS 服务实现构建、提交、更新和自动化工作流，支持 Android、iOS 和 Web 多平台分发，并可通过 OTA 更新即时推送修复。
- 📊 **内置监控与洞察**：提供用户平台分布、API 请求统计、错误率等实时数据，帮助开发者追踪应用性能。
- 🏢 **企业级支持**：服务符合 SOC 2 Type 2 和 GDPR 标准，可扩展至数亿用户，被大量顶级应用采用并获 App Store 排名第一。
- 🌍 **强大社区与生态**：拥有 7 万 + Discord 成员、5 万 + GitHub 星标，80% 的 React Native 开发者选择 Expo，全球已创建 50 万 + 项目。
- 🛠️ **极致开发体验**：支持在设备上直接开发（Expo Go）、一键启动模拟器（Expo Orbit）、可视化优化包（Expo Atlas），降低开发门槛。
- 🎯 **适合所有开发者**：从独立开发者到企业团队，Expo 提供从开发到上线的完整解决方案，并获社区广泛好评。

---

### [你的 AI 能通过无障碍测试吗？:: 亚伦·古斯塔夫森](https://www.aaron-gustafson.com/notebook/can-your-ai-pass-the-accessibility-test/)

**原文标题**: [Can Your AI Pass the Accessibility Test?  ::  Aaron Gustafson](https://www.aaron-gustafson.com/notebook/can-your-ai-pass-the-accessibility-test/)

AI 无法自动修复无障碍问题，它只会加速现有流程——若流程中已包含无障碍设计，AI 能扩大包容性；否则，它将放大已有的障碍。

- 📋 无障碍问题越早修复成本越低：规划阶段修复几乎免费，设计阶段成本增加 10 倍，开发阶段增加 100 倍，发布后则高达 1000 倍。
- 🤖 AI 训练数据来自普遍存在无障碍缺陷的网页，因此它生成的代码中自动可检测的无障碍检查通过率仅为 8–25%。
- 🛠️ 通过指令文件、技能注入和确定性测试，AI 代码的无障碍通过率可提升至 86%，但仍仅覆盖约 50% 的真正无障碍需求。
- 🎨 Figma 的 Accessibility Assistant 插件帮助设计师在早期明确界面意图、标注无障碍规范，并可导出给开发或智能体工作流。
- 🔍 GitHub 开源的无障碍扫描器集成到 PR 和 CI/CD 流程中，形成“发现 - 提交 - 修复”闭环，并支持 Copilot 辅助修复。
- 🗣️ 微软 AI 团队发现 Copilot 中 37% 的语音任务被放弃，而 76% 的阅读障碍用户表示使用 Copilot 后工作效率提升，因此开发了“Speak to Done”语音功能。
- ♿ 无障碍设计遵循“路缘坡效应”：最初为残障人士设计的解决方案，最终惠及所有人（如推婴儿车者、快递员等）。
- 🔁 无障碍应嵌入软件开发生命周期的每个阶段（规划、设计、编码、审查、发布），而非事后补救。

---

### [使用锚点定位优化卡片模式](https://thatemil.com/blog/clickable-surface-expansion-using-anchor-position/)

**原文标题**: [Improving card patterns with anchor positioning](https://thatemil.com/blog/clickable-surface-expansion-using-anchor-position/)

本篇文章探讨了如何使用 CSS 锚点定位来优化卡片组件的可点击区域，解决了传统方法中链接包裹、交互冲突和死区设置等问题。

- 📌 **核心问题**：传统卡片链接方式存在可访问性差（屏幕阅读器冗余）和交互冲突（嵌套交互元素）两大缺陷。
- 🛠️ **锚点定位方案**：通过 `anchor-name` 和 `anchor-scope` 将卡片设为锚点，利用伪元素 `::after` 覆盖整个卡片表面作为主点击区域。
- 🎯 **精准定位**：使用 `position-area: center` 和 `place-self: stretch` 使伪元素完全贴合卡片，并配合 `position: fixed` 避免父元素定位干扰。
- 🚫 **处理次操作**：为次操作按钮（如收藏）设置独立锚点 `--card-actions`，通过 `bottom: anchor(--card-actions top, 0)` 动态调整伪元素底部边界，自动留出死区空间。
- ✨ **优势总结**：无需魔法数字或复杂计算，支持多锚点引用，且不依赖特定父元素定位，代码更简洁健壮。
- 🌐 **扩展应用**：该模式可推广至表格行、列表项等需要整体可点击但需保留局部交互的 UI 场景。

---

### [哪种 Copyleft 许可证适合 SVG？——特伦斯·伊甸的博客](https://shkspr.mobi/blog/2026/06/which-copyleft-licence-is-suitable-for-an-svg/)

**原文标题**: [Which Copyleft Licence is Suitable for an SVG? – Terence Eden’s Blog](https://shkspr.mobi/blog/2026/06/which-copyleft-licence-is-suitable-for-an-svg/)

本文探讨了 SVG（可缩放矢量图形）适合使用哪种 Copyleft 许可证，分析了 Creative Commons 和 GPL 的适用性，并讨论了 SVG 作为代码或图像的本质争议。

- 📜 **SVG 本质争议**：SVG 既是图像（XML 描述图形）也是代码（包含变量、指令和脚本），这决定了许可证的选择。
- ❌ **Creative Commons 不推荐**：CC 许可证不适合软件，因为它缺乏源代码分发条款，且与主流软件许可证不兼容，尽管 SVG 是图像，但 CC 官方建议避免用于软件。
- ✅ **GPL 可能适用**：GPL 明确适用于“软件及其他作品”，只要定义“源代码”（即 SVG 的 XML 文本），但 FSF 对艺术类作品推荐 Free Art License。
- ⚖️ **SVG 作为库的考量**：LGPL 和 MPL 允许库集成到非自由软件中，但 SVG 作为“库”的界定模糊，需视使用场景而定。
- 🖼️ **嵌入光栅图像的影响**：SVG 可包含 PNG 等图像，这些图像可用 CC BY-SA，且与 GPLv3 兼容，但纯嵌入图像可能不算软件。
- 🗳️ **公众调查结果**：作者进行的非正式调查显示，多数人认为 SVG 是软件，应使用代码类许可证。
- 💡 **作者观点**：SVG 本质是软件，因其内容被计算机“执行”，即使简化后仍保留源代码特性，建议使用 GPL 等 Copyleft 许可证。
- 🔍 **社区讨论**：评论者提出 SVG 类似 PostScript 或 PDF，是“声明式数据”而非代码；也有观点认为许可证选择应基于实际行为而非语义。

---

### [导航标签中无需包含“导航”二字——tempertemper](https://www.tempertemper.net/blog/theres-no-need-to-include-navigation-in-your-navigation-labels)

**原文标题**: [There’s no need to include ‘navigation’ in your navigation labels – tempertemper](https://www.tempertemper.net/blog/theres-no-need-to-include-navigation-in-your-navigation-labels)

### 概述总结
文章强调在 HTML 导航标记中无需重复使用“导航”一词，因为屏幕阅读器已能通过`<nav>`元素和`aria-label`属性识别角色与名称，避免冗余信息。

- 🚫 避免冗余：在`<nav>`标签的`aria-label`中不要包含“导航”一词，否则屏幕阅读器会重复播报（如“导航，主要导航”）。
- 🔍 角色与名称分离：`<nav>`元素隐式提供“导航”角色，`aria-label`提供唯一名称（如“主要”），两者组合清晰标识导航区域。
- 📢 屏幕阅读器播报逻辑：会依次宣布元素角色、名称和状态（如展开/折叠），无需额外说明。
- 🎯 命名建议：用简洁描述性词汇（如“主要”“社交”）区分多个导航组，避免冗长标签。
- 📧 附加信息：文章末尾提供无障碍新闻订阅选项，强调不收集用户数据。

---

### [网站是否需要在每个平台上功能完全相同？– Bram.us](https://www.bram.us/2026/06/21/do-websites-need-to-function-exactly-the-same-on-every-platform/)

**原文标题**: [Do Websites Need to Function Exactly the Same on Every Platform? – Bram.us](https://www.bram.us/2026/06/21/do-websites-need-to-function-exactly-the-same-on-every-platform/)

概述：文章认为网站无需在所有平台上功能完全一致，应拥抱渐进增强，根据不同输入方式提供差异化体验。

- 📱 **早期像素完美误区**：2000 年代初，开发者执着于网站在所有浏览器中外观完全一致，导致跨浏览器兼容性成为巨大痛点。
- 🔄 **功能一致性的新误区**：如今社区已接受外观不必相同，但陷入“功能必须一致”的新误区，例如键盘快捷键、触摸手势等平台特有功能不应强制统一。
- 🖥️ **输入方式决定功能差异**：不同设备（鼠标、触屏、键盘、眼动追踪）有独特交互范式，网站应为触摸设备提供滑动/捏合、为键盘提供快捷键、为指针设备提供悬停效果。
- ⚙️ **平台特性阻碍 Web 标准发展**：如“兴趣调用器”在触屏上长按与系统菜单冲突，“文档画中画”因 iOS 限制被 WebKit 反对，根源都是要求功能跨平台一致。
- 💡 **解决方案：接受渐进增强**：若长按不可行，可让触屏用户跳过该功能（如 GitHub 信息卡），通过其他方式获取信息，而非强行统一交互。

---

### [获取失败](https://cloudfour.com/thinks/ending-responsive-images/)

**原文标题**: [Failed to retrieve](https://cloudfour.com/thinks/ending-responsive-images/)

无法总结：获取内容失败，状态码 403。

---

### [billboard.js 4.0 发布：Canvas 渲染模式，基准测试整体性能提升 94.3%！ | 作者：Jae Sung Park | 2026 年 6 月 | Medium](https://netil.medium.com/billboard-js-4-0-release-canvas-rendering-mode-94-3-faster-overall-in-benchmark-894b18798ffe)

**原文标题**: [billboard.js 4.0 release: Canvas rendering mode, 94.3% faster overall in benchmark! | by Jae Sung Park | Jun, 2026 | Medium](https://netil.medium.com/billboard-js-4-0-release-canvas-rendering-mode-94-3-faster-overall-in-benchmark-894b18798ffe)

billboard.js 4.0 版本发布：Canvas 渲染模式，基准测试整体性能提升 94.3%！

- 🎉 新版本主要聚焦于高密度图表性能提升和现代打包工具的轻量 ESM 体验
- 🖌️ 新增 Canvas 渲染模式，支持 line、bar、scatter 等十多种图表类型，通过 `render.mode: canvas()` 启用
- 🎨 提供 `canvas.theme.selectors` 映射 SVG 选择器到 Canvas 绘制样式，简化样式迁移
- ⚡ 基准测试显示，4.0 Canvas 模式比 3.18.0 整体快 94.3%，4.0 SVG 也比 3.18.0 快 47.4%
- 📦 ESM 包体积更小，分离 `exportApi`、`flow`、`grid` 等可选模块，最小化 bar 图表可减小约 19KB
- 🔄 ESM 用户需显式导入并使用 `grid()`、`regions()` 等解析器，否则会触发清晰的运行时错误
- 📚 提供详细的迁移指南和模块导入文档，支持单次配置或应用启动时一次性注册解析器
- 💡 SVG 仍为默认渲染模式，Canvas 为可选性能优化路径，适用于高密度数据场景

---

### [billboard.js - 示例](https://naver.github.io/billboard.js/demo/)

**原文标题**: [billboard.js - examples](https://naver.github.io/billboard.js/demo/)

以下是對 billboard.js 範例頁面的摘要：

billboard.js 是一個圖表庫，提供多種圖表類型和互動功能，支援主題切換與渲染方式，並附有即時編輯器供使用者測試。

- 📊 **支援多種圖表類型**：包括 Area、Bar、Bubble、Candlestick、Donut、Gauge、Line、Pie、Polar、Radar、Scatter、Spline、Stacked Bar、Step、Treemap 等。
- 🎨 **多種主題選擇**：提供 default、datalab、dark、insight、graph、modern 等主題。
- 🖼️ **渲染方式可選**：支援 SVG 和 Canvas 兩種渲染模式。
- 💻 **即時編輯器**：可透過左側選單瀏覽範例，並在右側編輯器直接修改程式碼測試效果。
- 📋 **程式碼複製功能**：支援一鍵複製 JS 或 TS 程式碼到剪貼簿。
- 🔗 **ESM 匯入參考**：提供外部連結說明 ESM 匯入方式。

---

### [billboard.js - 示例](https://naver.github.io/billboard.js/demo/#Chart.DonutChart)

**原文标题**: [billboard.js - examples](https://naver.github.io/billboard.js/demo/#Chart.DonutChart)

概述摘要
- 📊 billboard.js 提供多种图表类型，包括面积图、条形图、气泡图、烛台图、组合图、甜甜圈图、漏斗图、仪表图、折线图、饼图、极地图、雷达图、散点图、样条图、堆叠条形图、阶梯图和树状图。
- 🎨 支持多种主题（default、datalab、dark、insight、graph、modern）和渲染方式（SVG 或 Canvas）。
- 🚀 提供代码编辑器，可直接编辑 JS 或 TS 代码并运行示例。
- 📋 左侧菜单列出所有示例，右侧按钮可快速切换或复制代码到剪贴板。
- 🔗 提供 ESM 导入用法示例的链接，方便模块化开发。

---

### [billboard.js - 示例](https://naver.github.io/billboard.js/demo/#Chart.FunnelChart)

**原文标题**: [billboard.js - examples](https://naver.github.io/billboard.js/demo/#Chart.FunnelChart)

以下是對 billboard.js 範例頁面的內容摘要：

billboard.js 是一個圖表庫，提供多種圖表類型和即時編輯功能。

- 📊 **支援多種圖表類型**：包括 Area、Bar、Bubble、Candlestick、Combination、Donut、Funnel、Gauge、Line、Pie、Polar、Radar、Scatter、Spline、Stacked Bar、Step、Treemap 等。
- 🎨 **多樣主題與渲染選項**：提供 default、datalab、dark、insight、graph、modern 主題，並支援 SVG 或 Canvas 渲染。
- 🖥️ **即時編輯與程式碼範例**：使用者可直接在頁面上編輯 JS 或 TS 程式碼，並點擊按鈕試用效果。
- 📋 **複製與匯出功能**：支援將程式碼複製到剪貼簿，並提供 ESM 匯入的使用範例連結。
- 🔗 **資源連結**：包含 API 文件與 GitHub 儲存庫的快速連結。

---

### [billboard.js - 示例](https://naver.github.io/billboard.js/demo/#BarChartOptions.BarOverlap)

**原文标题**: [billboard.js - examples](https://naver.github.io/billboard.js/demo/#BarChartOptions.BarOverlap)

以下是基于您提供的 billboard.js 页面内容的概述和要点总结：

📊 billboard.js 是一个功能丰富的图表库，支持多种图表类型和主题，提供 API 文档和 GitHub 资源，并允许用户通过代码编辑器实时编辑和测试。

- 📚 **提供 API 文档和 GitHub 链接**：方便开发者查阅详细文档和获取源代码。
- 🎨 **支持多种主题**：包括 default、datalab、dark、insight、graph、modern，满足不同视觉风格需求。
- 🖼️ **渲染方式可选**：支持 SVG 和 Canvas 两种渲染模式。
- 🚀 **内置代码编辑器**：允许用户直接编辑 JS 或 TS 代码，并实时查看效果。
- 📈 **涵盖多种图表类型**：如 Area、Bar、Bubble、Candlestick、Combination、Donut、Funnel、Gauge、Line、Pie、Polar、Radar、Scatter、Spline、Stacked Bar、Step、Treemap 等。
- 📝 **提供示例代码**：用户可通过左侧菜单浏览示例，并点击右侧按钮尝试编辑。
- 🔗 **支持 ESM 导入**：提供 ESM 用法示例链接，方便现代前端项目集成。

---

### [billboard.js - 示例](https://naver.github.io/billboard.js/demo/#RadarChartOptions.RadarAxis)

**原文标题**: [billboard.js - examples](https://naver.github.io/billboard.js/demo/#RadarChartOptions.RadarAxis)

以下是对 billboard.js 示例页面的内容总结：

📊 概述：该页面展示了 billboard.js 图表库的多种图表类型和交互功能，用户可通过左侧菜单浏览示例，并直接在编辑器中修改代码进行测试。

- 📚 提供丰富的图表类型：包括面积图、面积范围图、条形图、气泡图、蜡烛图、组合图、甜甜圈图、漏斗图、仪表图、折线图、饼图、极地图、雷达图、散点图、样条图、堆叠条形图、阶梯图、树状图等。
- 🎨 支持多种主题和渲染方式：用户可选择默认、数据实验室、暗色、洞察、图形、现代主题，以及 SVG 或 Canvas 渲染。
- 🛠️ 提供交互式代码编辑器：用户可直接在页面右侧编辑 JS 或 TS 代码，并实时查看效果，便于学习和测试。
- 📋 包含示例代码和复制功能：支持复制代码到剪贴板，并提供了 ESM 导入用法的参考链接。

---

### [影](https://kage.tamnd.com/)

**原文标题**: [kage](https://kage.tamnd.com/)

概览摘要：  
kage（影）是一款通过真实浏览器渲染页面、移除所有脚本并保存完整离线镜像的工具，生成可直接从磁盘打开的静态 HTML 文件夹。

- 📸 使用无头 Chrome 完整渲染页面，包括 JavaScript 动态生成的内容，而非空白外壳  
- 🔒 移除所有脚本标签、事件处理器和 JavaScript 链接，保存的页面不执行任何代码  
- 🎨 下载并重写 CSS、图片和字体为本地相对路径，保持原始布局样式  
- 🔗 重写站内链接指向已保存页面，实现离线浏览的完整导航体验  
- 📦 支持将镜像打包为单个 ZIM 文件或自包含二进制文件，便于分发和离线使用  
- 🖥️ 通过 webview 标签构建后，打包的二进制文件可独立窗口运行，模拟原生应用体验  
- ⚡ 提供完整文档：快速入门、安装指南、任务导向教程及 CLI 参考手册

---

### [页面安装组件的齐平高度选项](https://clerk.com/changelog/2026-05-22-flush-appearance-option?utm_source=cooper_press&utm_medium=newsletter&utm_campaign=flush-option&utm_content=06-24-26&dub_id=OTuyRMH6H0rgG1YS)

**原文标题**: [Flush elevation option for page-mounted components](https://clerk.com/changelog/2026-05-22-flush-appearance-option?utm_source=cooper_press&utm_medium=newsletter&utm_campaign=flush-option&utm_content=06-24-26&dub_id=OTuyRMH6H0rgG1YS)

### 概述总结
- 🆕 新增 `elevation` 外观选项，控制页面挂载组件的显示样式。
- 📦 默认值为 `raised`，组件以卡片形式渲染（含背景、边框、阴影）。
- 🚫 设置为 `flush` 时，组件去除卡片样式，直接嵌入页面布局。
- 🔒 模态框和弹出窗口始终使用 `raised` 模式，不受此设置影响。
- 📝 适用于 `SignIn` 等组件，简化自定义布局的集成过程。

---

### [Wely — 轻量级 Web 组件框架](https://litepacks.github.io/welyjs/)

**原文标题**: [Wely — Lightweight Web Component Framework](https://litepacks.github.io/welyjs/)

## 概述总结
Wely 是一个轻量级 Web 组件框架，通过单一 `defineComponent()` 函数即可创建原生自定义元素，无需类语法，无框架锁定，输出可在任何前端框架中运行。

- 🚀 **极简入门** — 只需 `wely init` + `npm install`，一个 CLI 搞定脚手架、开发、构建、测试、导出全流程
- 📦 **轻量体积** — 运行时仅 13KB（gzip），每增加一个组件仅增加 0.4-0.5KB，按需打包
- 🧩 **组件定义** — 使用 `defineComponent()` 传入普通对象，包含 `tag`、`props`、`state`、`actions`、`render` 等字段
- 🔄 **自动响应式** — 状态通过 Proxy 实现自动追踪，修改即触发重渲染
- 🎨 **Tailwind 集成** — 模板中使用 Tailwind 类，自动编译注入 Shadow DOM
- 🌐 **HTTP 客户端** — 内置 `createClient()`，支持拦截器、超时、查询参数
- 🧪 **测试支持** — `wely test` 基于 Vitest + jsdom，无需额外配置
- 🛠️ **开发者工具** — 组件暴露 `$wely` 属性，可通过 DevTools 直接访问状态和操作
- 🔌 **完全可移植** — 输出为标准 Web Components，可在 React、Vue、Angular、Svelte 等任何框架中直接使用
- 📚 **自动文档** — `wely docs` 生成 `COMPONENTS.md`，保持文档与代码同步

---

### [Wirewiki](https://www.wirewiki.com/)

**原文标题**: [Wirewiki](https://www.wirewiki.com/)

本工具集提供了一系列网络诊断与域名查询功能，帮助用户快速获取 DNS、IP 及域名相关信息。

- 🌐 DNS 传播检查器：验证域名 DNS 记录是否已全球生效
- 🔍 网站 IP 查询：获取指定网站的 IP 地址
- 📧 SPF 记录检查：验证域名的 SPF 邮件验证记录是否正确
- 📬 MX 记录查询：查找域名的邮件服务器地址
- 📝 TXT 记录查询：获取域名的文本记录信息
- 🔄 DNS 追踪：从根服务器到权威服务器，追踪 DNS 解析路径
- 🛡️ 区域传输检查：检测 DNS 区域传输是否开启并查看记录
- 📅 DNS 历史记录：查看域名 DNS 记录的变更历史
- 🔗 反向 DNS 查询：根据 IP 地址查找对应的域名

---

### [字体缩放工具 – 精准排版，快速获取 CSS](https://precise-type.com/)

**原文标题**: [Type Scale Tool â Craft Precise Typography, Get CSS Fast](https://precise-type.com/)

该工具是一个用于构建和谐排版体系的类型比例生成器，支持从基础值到输出代码的完整流程。

- 🎯 **核心功能**：通过基础值（字号、行高、字间距）生成完整的类型比例，支持模块化与度量两种模型
- 🎵 **比例选择**：提供基于音乐音程（如大三度、纯五度）的预设比例，确保字体大小间和谐关系
- 📐 **网格约束**：可设置像素网格（如 4px）强制行高对齐，设为 1px 则取消约束
- 🔧 **自定义调整**：支持添加/删除比例阶梯，并可通过“紧/中/宽”预设调整整体间距
- 📊 **可视化分析**：提供图表展示字号、行高、字间距的变化趋势，支持多单位（px/rem/ratio 等）对比
- 💻 **输出格式**：一键生成 CSS 或 CSV 格式的排版值，方便开发者直接使用
- 📜 **历史背景**：基于 Tim Brown 的模块化比例理论，并参考 Material Design 等设计系统
- 🛠️ **适用场景**：从商业应用到消费产品网站，覆盖设计稿到开发实现的全流程

---

### [Able Player v5.0.0 发布！ - Joe Dolson 网页无障碍](https://www.joedolson.com/2026/06/able-player-v5-0-0-released/)

**原文标题**: [Able Player v5.0.0 released! - Joe Dolson Web Accessibility](https://www.joedolson.com/2026/06/able-player-v5-0-0-released/)

Able Player v5.0.0 版本发布，主要更新包括新增斯洛伐克语翻译、修复数据语言属性处理错误，以及更新了 WordPress 插件至 2.4.0 版本，新增 YouTube 嵌入块转换、视频 URL 支持等功能。

- 🎉 发布 Able Player 5.0.0 版本，修复多个错误
- 🌐 新增斯洛伐克语翻译，修复 `data-lang` 属性处理问题
- 🧪 增加使用 Jest 运行测试的文档
- 🔧 更新 WordPress 插件至 2.4.0 版本
- 📦 重构文件结构，从 NPM 注册表获取文件
- 🔄 自动将 YouTube 嵌入块转换为使用 Able Player
- 🔗 支持在短代码中通过 URL 引用视频
- 🛡️ 新增 `ableplayer_capability` 过滤器，控制插件设置访问权限

---

### [Able Player | 完全无障碍的跨浏览器 HTML5 媒体播放器](https://ableplayer.github.io/ableplayer/)

**原文标题**: [Able Player | Fully accessible cross-browser HTML5 media player.](https://ableplayer.github.io/ableplayer/)

Able Player 是一款完全可访问的跨浏览器 HTML5 媒体播放器，支持音频和视频，具备丰富的无障碍功能和自定义选项。

- 🎯 **核心功能**：支持音频和视频播放，提供键盘可访问、屏幕阅读器友好的控制按钮，以及高对比度、可缩放的界面。
- 🌐 **多语言支持**：已翻译成包括中文（繁体）、英语、法语、日语等在内的 20 多种语言。
- 🔧 **兼容性**：在 Windows、Mac OS、iOS 和 Android 系统的最新版 Chrome、Firefox、Safari、Edge 等浏览器上测试通过。
- 🔒 **内容安全策略**：默认仅引用本地资源，支持配置 YouTube 和 Vimeo 的外部资源策略。
- 📦 **依赖项**：依赖 jQuery（推荐 3.5.0+）、可选 js-cookie 存储偏好，以及 DOMPurify 库进行安全处理。
- 📝 **安装与设置**：支持通过 `<script>` 标签、NPM 或 RequireJS 安装，需使用 HTML5 文档类型并添加相应 CSS 和 JS。
- 🎬 **功能特性**：支持隐藏式字幕、章节、音频描述、可调播放速度、交互式文字记录、YouTube/Vimeo 视频，以及用户可自定义的显示偏好。
- 🎛️ **自定义属性**：提供大量 `data-*` 属性用于配置播放器，如语言、字幕位置、文字记录类型、搜索等。
- ⌨️ **键盘快捷键**：支持播放/暂停、快进/快退、音量控制等快捷键，并可通过偏好设置修改修饰键。
- 🎨 **用户偏好**：用户可通过偏好按钮自定义修饰键、字幕显示、描述行为、文字记录高亮等设置，并保存在浏览器中。

---

### [调色板灵感——大师们的永恒色彩](https://paletteinspiration.com/)

**原文标题**: [Palette Inspiration - Timeless Colors of the Great Masters](https://paletteinspiration.com/)

该网站是一个艺术色彩探索平台，从数万幅大师画作中提取配色方案，提供艺术家、风格和流派浏览，以及多种色彩工具。

- 🎨 拥有超过 3,000 位艺术家和 23,252 幅画作的庞大数据库
- 🖌️ 涵盖 94 种艺术风格和 44 种流派，从文艺复兴到印象派
- 🎯 提供交互式 HSV/RYB 色轮，支持 464+ 种历史命名颜色搜索
- 🎞️ 特色功能包括“调色板生成器”和“快速调色板构建器”，基于真实画作数据
- 🖼️ 每日精选画作展示，每幅附带 10 色提取调色板
- 🔍 支持按艺术家字母索引浏览，及“颜色搭配”探索功能
- 🛠️ 可导出 CSS、Tailwind、ASE、Figma JSON 等格式
- 📱 提供“颜色探索器”和“快速浏览”工具，方便用户即时生成配色

---

### [毕加索调色板 - 调色灵感](https://paletteinspiration.com/pablo-picasso-palettes/)

**原文标题**: [Picasso Color Palettes - Palette Inspiration](https://paletteinspiration.com/pablo-picasso-palettes/)

巴勃罗·毕加索是一位 20 世纪西班牙艺术家，作品涵盖立体主义、后印象派和超现实主义，其标志性调色板以柔和茶色为主，包含 24 种独特配色方案，并受多位大师影响。

- 🎨 毕加索是 20 世纪西班牙艺术家，风格涵盖立体主义、后印象派和超现实主义
- 🖌️ 其主调色板包含#D7C7AB、#231D1D 等颜色，共有 24 种独特配色方案
- 🌟 受马克·夏加尔、亨利·卢梭、埃尔·格雷科和弗朗西斯科·戈雅影响
- 🎭 影响了马克·夏加尔、阿梅代奥·莫迪利亚尼等艺术家，属于巴黎画派
- 📚 毕加索是 20 世纪最具影响力的艺术家之一，成年后大部分时间在法国度过
- 🎨 调色板变体包括亮白、亮金黄、柔和茶色等 24 种不同名称
- 🖼️ 展示了 17 件毕加索作品，如《蓝色房间》（1901）和《亚威农少女》等
- 🔍 可发现类似调色板艺术家，如 T. C. Steele 和 Pedro Américo
- 🌍 支持按世纪或国籍浏览艺术家，20 世纪有 669 位艺术家

---

### [使用 Foxit 的 Python 和 cURL 实现 DOCX 转 PDF API](https://developer-api.foxit.com/developer-blogs/api-guides-tutorials/docx-to-pdf-api/?utm_source=draftdev&utm_medium=newsletter&utm_campaign=frontendfocus_20260624)

**原文标题**: [DOCX to PDF API in Python and cURL with Foxit](https://developer-api.foxit.com/developer-blogs/api-guides-tutorials/docx-to-pdf-api/?utm_source=draftdev&utm_medium=newsletter&utm_campaign=frontendfocus_20260624)

本指南详细介绍了通过 Foxit PDF Services API 将 DOCX 转换为 PDF 的完整流程，并提供了可运行的 Python 和 cURL 代码示例。

- 📄 **概述**：通过 API 调用实现 DOCX 到 PDF 的转换，支持 Python 和 cURL 两种方式。
- 🐍 **Python 示例**：提供完整的 Python 代码，包括发送请求、处理响应和保存 PDF 文件。
- 🔗 **cURL 示例**：展示使用 cURL 命令行工具执行相同转换的步骤，适合快速测试。
- ⚙️ **API 流程**：涵盖认证、上传 DOCX 文件、触发转换任务以及下载生成的 PDF 文件。
- 🎯 **关键要点**：需要 API 密钥和文件路径，转换完成后会返回 PDF 下载链接。

---

### [cssQuake - 由 PolyCSS 驱动](https://cssquake.com/)

**原文标题**: [cssQuake - Powered by PolyCSS](https://cssquake.com/)

该内容为游戏设置与操作界面的文本描述，包含多人游戏、操作控制、调试选项和特殊对象等模块。

- 🎮 **多人游戏设置**：包含房间名称、颜色、地图、击杀上限和最大玩家数，可创建房间或返回。
- ⌨️ **操作控制**：WASD 移动、鼠标瞄准、点击射击、空格跳跃、Shift 奔跑、Ctrl 蹲下；菜单用方向键导航，回车选择。
- 🔧 **调试选项**：可开关轮廓显示、统计面板、FPS 面板、动态光照、静音、粒子效果、敌人显示、伤害/移动/攻击禁用、鼠标反转。
- 🎯 **游戏玩法设置**：准星样式（+）、动态光照、静音、粒子、敌人显示、伤害/移动/攻击禁用、鼠标反转。
- 📹 **录制功能**：提供录制、捕获、可见性、DOM、敌人、拾取物、世界等调试选项。
- 🧩 **特殊对象**：包含物品/道具和敌人。

---

### [PolyCSS - 面向 DOM 的 CSS 3D 引擎](https://polycss.com/)

**原文标题**: [PolyCSS - CSS 3D Engine for the DOM](https://polycss.com/)

通过 CSS 在 DOM 中渲染带纹理的 3D 网格，无需 WebGL 或 Canvas，每个多边形都是真实 DOM 元素。

- 📦 支持 OBJ、glTF、GLB 和 MagicaVoxel VOX 格式，包含 UV 纹理和材质颜色
- 🧩 兼容原生 JS、React 和 Vue，提供 npm 包和 CDN 引入方式
- ⚙️ 工作原理：加载网格文件后，每个多边形转为 DOM 元素，用 transform: matrix3d(...) 定位，UV 纹理打包到精灵图
- 🖱️ 每个多边形可单独添加点击事件、CSS 类和动画，浏览器合成器处理 3D 分层
- 🎨 提供自定义元素（<poly-camera>、<poly-scene>、<poly-mesh>）和命令式 API，支持 React/Vue 绑定
- 🌟 示例：通过简单标签或组件即可创建带轨道控制的 3D 二十面体

---

### [GitHub - LayoutitStudio/cssQuake：基于PolyCSS 3D 引擎的《雷神之锤》（1996）移植版](https://github.com/LayoutitStudio/cssQuake)

**原文标题**: [GitHub - LayoutitStudio/cssQuake: A port of Quake (1996), powered by the PolyCSS 3D engine. · GitHub](https://github.com/LayoutitStudio/cssQuake)

cssQuake 是一个将经典游戏《雷神之锤》移植到浏览器中的项目，它使用 PolyCSS 3D DOM 渲染引擎，将游戏几何体转换为真实的 HTML/CSS 3D 元素，无需 WebGL 或 Canvas 渲染器。

- 👹 项目概述：将 id Software 的《雷神之锤》移植到浏览器，通过 PolyCSS 引擎将 BSP 世界渲染为 HTML/CSS 3D 几何体
- 🎮 玩法说明：需安装依赖并生成 Quake 资源，支持分享版或本地 PAK 文件，运行 `pnpm dev` 启动开发服务器
- ⚙️ 工作原理：使用 PolyCSS 引擎，将游戏几何体转换为带 CSS `matrix3d` 变换的 HTML 元素，纹理使用像素化 CSS 背景
- 🛠️ 构建与运行时：预处理步骤解析原始 BSP、WAD、MDL 等数据，生成浏览器就绪的 JSON 和图片资源；运行时由 TypeScript 控制游戏循环、玩家移动、碰撞等逻辑
- 🔗 URL API：支持通过 URL 参数直接打开地图和设置玩家视角，如 `?map=e1m1&view=480,-192,72,0,90,0`
- 📦 嵌入功能：可在 iframe 中运行，通过 `relayKeys=1` 参数实现按键事件中继
- 📜 许可证：源代码采用 GPL-2.0 许可，原始游戏数据不包含在仓库中

---

### [《自你到来》第四卷——已取走](https://sinceyouarrived.world/taken)

**原文标题**: [taken. — Since You Arrived Vol. IV](https://sinceyouarrived.world/taken)

### 概述总结
该页面揭示了浏览器在用户不知情的情况下收集的大量数据，并以此作为艺术项目的一部分，旨在引发对隐私问题的反思。

- 📜 **页面依赖 JavaScript**：关闭 JS 后，页面无法告知你浏览器泄露了哪些数据，但数据收集依然发生。
- 🌐 **已收集的信息**：包括 IP 地址（用于定位城市和 ISP）、屏幕参数、浏览器语言、GPU、电池状态、已安装字体等。
- 🎨 **字体指纹识别**：通过测量文本宽度检测已安装字体，该技术自 2010 年起被用于追踪用户，即使无 Cookie 也能识别。
- 🖼️ **Canvas 指纹识别**：页面未执行此技术（绘制隐藏图像并读取像素），但浏览器支持，其他网站可能已使用。
- 📋 **剪贴板 API**：页面未请求读取剪贴板，但现代浏览器默认支持此功能，任何页面在用户点击时都可获取复制的密码或地址。
- 🔋 **电池状态泄露**：2015 年研究表明电池百分比和放电时间组合可唯一标识用户，Firefox 已移除该 API，Chrome 和 Edge 仍保留。
- 🔍 **未运行的登录检测**：页面未通过加载网站图标检测用户登录状态，但该技术合法且常见，可判断用户是否登录 Facebook、Google 等。
- 📊 **唯一条形码**：基于设备信息（GPU、字体、屏幕等）生成 16 条竖线，不同用户条形码不同，但计算在本地完成，未上传。
- ✍️ **内容创作**：所有文字由人类编写，基于浏览器返回的数据选择模板，未使用 AI 生成。
- 📡 **发送的数据**：仅发送两个匿名事件（到达和离开），无 Cookie、无标识符、不保留 IP，服务器丢弃请求体。
- 🗑️ **本地存储**：页面未在设备上存储任何数据（无 Cookie、无 localStorage 等），关闭标签页后即遗忘用户。
- 📚 **系列作品**：该页面是“Since You Arrived”系列第四卷，前几卷分别关注全球事件、天空和脚下，本卷聚焦用户自身。

---

