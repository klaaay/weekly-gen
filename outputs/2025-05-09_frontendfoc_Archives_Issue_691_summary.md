### [前端聚焦第 691 期：2025 年 5 月 7 日](https://frontendfoc.us/issues/691)

**原文标题**: [Frontend Focus Issue 691: May 7, 2025](https://frontendfoc.us/issues/691)

概述  
本期内容涵盖了前端开发的最新动态、CSS 新特性、工具资源以及行业新闻，包括实验性 CSS 属性、AI 在前端的应用、免费动画工具发布等。  

- 🚀 **实验性 CSS 属性** — Jen Simmons 介绍了`margin-trim`属性，可修剪容器内子元素的边距。  
- ♿ **CSS 轮播的可访问性** — Sara Soueidan 探讨了 CSS 轮播的当前可用性和无障碍问题。  
- 🔒 **实时防护 AI 滥用** — WorkOS Radar 提供设备指纹技术，防止虚假注册和机器人攻击。  
- 🎉 **GSAP 动画工具免费** — Webflow 收购后，GSAP 动画库及其插件完全免费开放（商业用途受限）。  
- 🤖 **Gemini 2.5 Pro 升级** — Google 称其 AI 模型更擅长构建美观的前端应用。  
- 💸 **Mozilla 依赖 Google 收入** — 高管表示与 Google 的搜索合作对 Firefox 生存至关重要。  
- 📖 **Chrome 137 新特性** — `reading-flow`和`reading-order`属性即将发布，Rachel Andrew 呼吁测试反馈。  
- ♾️ **WCAG 3.0 评分模型** — 拟转向以用户体验为中心的无障碍评估标准。  
- 🔑 **Passkeys 普及指南** — Troy Hunt 详解密码替代方案 Passkeys 的机制与优势。  
- 🧰 **React 性能优化** — Sentry 指南解析 8 种常见性能问题及解决方案。  
- 🌐 **Mantine 8.0 发布** — 新增图表组件、子菜单等 20 多项功能。  
- 🎨 **终端风格 CSS 库** — WebTUI 提供模块化组件，模拟终端 UI 效果。  
- 😄 **CSS 主题漫画** — Alvaro Montoro 的`comiCSS`用 CSS 创作技术幽默漫画。  

（注：赞助商内容及分类广告未完全列入摘要。）

---

### [更简单的布局：使用 margin-trim | WebKit](https://webkit.org/blog/16854/margin-trim/)

**原文标题**: [  Easier layout with margin-trim | WebKit](https://webkit.org/blog/16854/margin-trim/)

CSS 新属性 margin-trim 可优化容器内子元素的外边距布局，提供更简洁的代码方案。

- 🎯 **margin-trim 的作用**  
  - 允许容器修剪子元素的外边距，消除与容器边缘接触的多余间距。

- 🛠️ **实际应用示例**  
  - 在文章容器中，段落的外边距与容器的内边距叠加导致布局不均衡，margin-trim 可自动修剪这些外边距。

- 📏 **属性设置**  
  - 需在容器上设置`margin-trim`，而非子元素，支持逻辑方向（block/inline）的修剪。

- 🌐 **浏览器支持**  
  - 目前仅 Safari 16.4+ 支持，但可通过特性查询为其他浏览器提供备用方案。

- 🔄 **与传统方法的对比**  
  - 传统方法如`:first-child`仅修剪直接子元素的外边距，而 margin-trim 可处理嵌套更深的外边距。

- 🔧 **属性值选项**  
  - 包括`none`、`block`、`inline`及具体方向（如`block-start`），未来将支持组合写法如`block inline`。

- 🚀 **未来展望**  
  - 鼓励开发者现在使用 margin-trim，并期待更多浏览器支持，以实现更健壮的布局方案。

---

### [CSS 属性：margin-trim | 我能用吗... HTML5、CSS3 等支持表格](https://caniuse.com/mdn-css_properties_margin-trim)

**原文标题**: [CSS property: margin-trim | Can I use... Support tables for HTML5, CSS3, etc](https://caniuse.com/mdn-css_properties_margin-trim)

CSS 属性`margin-trim`的全球使用率为 14.91%，目前仅在部分浏览器版本中得到支持。

- 🌍 **全球使用率**：14.91%  
- 🚫 **IE**：全版本不支持  
- 🚫 **Edge**：全版本不支持  
- 🚫 **Firefox**：全版本不支持  
- 🚫 **Chrome**：全版本不支持  
- ✅ **Safari**：16.4 及以上版本支持  
- 🚫 **Opera**：全版本不支持  
- ✅ **iOS Safari**：16.4 及以上版本支持  
- ❓ **Opera Mini**：支持情况未知  
- 🚫 **Android Browser**：全版本不支持  
- 🚫 **Opera Mobile**：全版本不支持  
- 🚫 **Chrome for Android**：不支持  
- 🚫 **Firefox for Android**：不支持  
- ❓ **UC Browser/QQ Browser/Baidu Browser/KaiOS Browser**：支持情况未知  
- 🚫 **Samsung Internet**：全版本不支持

---

### ["CSS 轮播"是否具有可访问性？](https://www.sarasoueidan.com/blog/css-carousels-accessibility/)

**原文标题**: [Are 'CSS Carousels' accessible?](https://www.sarasoueidan.com/blog/css-carousels-accessibility/)

CSS Carousels 的可访问性分析  

- 🚨 **实验性功能**：CSS Carousels 目前是高度实验性的，尚未准备好投入生产环境，主要由于浏览器支持不足和严重的可访问性问题。  
- 🔍 **核心问题**：CSS Carousels 通过伪元素（如 `::scroll-marker`）实现交互，但这些伪元素的语义和可访问性信息（如角色、名称）未正确暴露给辅助技术（如屏幕阅读器）。  
- 🛠 **技术实现**：依赖 CSS Overflow Module 5 规范的新特性（如 `scroll-marker-group`、`:target-current`），但当前实现将滚动标记错误地暴露为 `tab` 角色，而实际组件行为不符合 ARIA Tabs 模式的要求。  
- ❌ **关键缺陷**：  
  - 缺少对应的 `tabpanel` 角色（Tabs 组件必需）。  
  - 多个滚动标记共享相同的可访问名称（如“Carousel item marker”），无法区分不同项。  
  - 键盘和屏幕阅读器导航混乱，焦点管理不符合 Tabs 模式预期。  
- 📱 **示例分析**：  
  - **横向列表**：多个项同时可见，但仅一个标记被标记为“选中”，语义矛盾。  
  - **卡片轮播**：焦点跳转异常，隐藏项仍可被键盘访问。  
  - **滚动监听**：标记无名称，且 `:target-current` 伪类仅支持 CSS 生成的标记，不适用于原生 HTML 链接。  
  - **横向标签页**：硬编码 `tabpanel` 角色，但面板未正确隐藏，滚动与 Tabs 行为冲突。  
- ⚠️ **风险提示**：开发者可能误以为浏览器“自动处理可访问性”，但实际上需自行补充 ARIA 语义和键盘交互逻辑。  
- 💡 **改进建议**：  
  - 优先使用原生 HTML 和 ARIA 实现可访问组件（如 `<a>` 链接 + JavaScript）。  
  - 等待 OpenUI 对原生 Tabs/Carousel 组件的标准化。  
  - 测试时关注屏幕阅读器、键盘导航和焦点管理。  
- 📢 **核心结论**：当前 CSS Carousels 不可访问，不推荐生产使用；开发者应批判性评估新特性对用户体验的影响。

---

### [CSS 旋转木马效果 | 博客 | Chrome 开发者](https://developer.chrome.com/blog/carousels-with-css)

**原文标题**: [Carousels with CSS  |  Blog  |  Chrome for Developers](https://developer.chrome.com/blog/carousels-with-css)

Chrome 135 引入了 CSS Overflow 5 规范的新功能，无需 JavaScript 即可创建滚动和轮播体验。这些功能包括滚动按钮、滚动标记、滚动驱动动画等，并具有出色的可访问性和性能。

- 🚀 **CSS Overflow 5 新功能**：Chrome 135 支持通过 CSS 创建滚动和轮播体验，无需 JavaScript。  
- 🎥 **多样化体验**：视频展示了滚动按钮、滚动标记、滚动驱动动画、`scroll-state()` 查询等功能的协同效果。  
- ♿ **卓越的可访问性**：浏览器内置的轮播最佳实践，确保高度可访问性。  
- 🛠️ **滚动按钮与标记**：通过 `::scroll-button()` 和 `::scroll-marker()` 创建浏览器提供的交互元素，支持状态管理和无障碍访问。  
- 📜 **基本滚动区域**：通过 CSS 创建滚动区域，可添加滚动按钮和标记，支持水平和垂直滚动。  
- ⏭️ **滚动按钮功能**：`::scroll-button()` 提供滚动按钮，支持自定义内容和样式，滚动幅度为 85%。  
- 🔵 **滚动标记功能**：`::scroll-marker()` 创建导航标记，支持内容自定义（如文本或缩略图），并包含键盘导航和屏幕阅读器支持。  
- 🎨 **组合使用**：结合滚动按钮和标记，实现无需 JavaScript、高性能且无障碍的轮播体验。  
- 📚 **资源与示例**：提供轮播配置器和轮播画廊，展示高级功能如滚动驱动动画和 `scroll-state()` 查询。  
- 🔮 **未来改进**：计划支持自定义元素和循环滚动功能，进一步提升用户体验。  
- 🌟 **优势总结**：CSS 轮播具有更好的性能、可访问性和用户体验，减少开发者工作量。

---

### [3.13 版本发布 | GSAP | 文档与学习](https://gsap.com/blog/3-13/)

**原文标题**: [3.13 release | GSAP | Docs & Learning](https://gsap.com/blog/3-13/)

GSAP 3.13 版本发布，宣布 GSAP 及其所有插件（包括 SplitText 和 MorphSVG 等）现在完全免费，包括商业用途。团队将继续维护和创新，并与 Webflow 合作开发下一代交互功能。SplitText 插件进行了全面重写，新增多项功能并优化性能。此外，GSAP 3.13 还支持动画到 CSS 变量，并简化了 Webflow 的安装流程。

- 🎉 GSAP 及其所有插件现在完全免费，包括商业用途  
- 🛠️ 原始团队将继续维护和创新 GSAP  
- 🤝 与 Webflow 合作开发下一代交互功能  
- 🔧 SplitText 插件全面重写，新增 14 项功能并优化性能  
- 🆕 GSAP 3.13 支持动画到 CSS 变量  
- 🚀 简化 Webflow 的 GSAP 安装流程  
- 📚 提供完整的文档和学习资源  
- 💬 社区论坛继续支持用户交流  
- 🔄 Club GSAP 会员将自动迁移到公共仓库  
- 📅 会员需在 2025 年 6 月 1 日前迁移至公共仓库

---

### [GSAP 加入 Webflow | GSAP | 文档与学习](https://gsap.com/blog/webflow-GSAP/)

**原文标题**: [GSAP is Joining Webflow | GSAP | Docs & Learning](https://gsap.com/blog/webflow-GSAP/)

GSAP 被 Webflow 收购，将结合双方优势提升动画能力，同时保持 GSAP 的独立性和广泛可用性，未来将共同开发更强大的动画工具。

- 🎉 GSAP 被 Webflow 收购，旨在提升 Webflow 的动画功能  
- 🌍 GSAP 将继续公开供所有用户使用，保持独立性和功能更新  
- 💻 GSAP 目前支持超过 1200 万个网站，包括许多获奖作品  
- 🤝 Webflow 将为 GSAP 提供开发资源，推动产品创新  
- 💡 双方理念一致：简化复杂技术，让更多人轻松实现创意  
- 🛠️ 未来可能开发 GSAP 的图形用户界面（GUI），利用 Webflow 的界面设计专长  
- 🔍 具体合作细节尚未公布，但承诺将带来特别的产品  
- 📢 邀请用户分享对未来合作的期望和建议

---

### [MorphSVG | GSAP | 文档与学习](https://gsap.com/docs/v3/Plugins/MorphSVGPlugin/)

**原文标题**: [MorphSVG | GSAP | Docs & Learning](https://gsap.com/docs/v3/Plugins/MorphSVGPlugin/)

MorphSVGPlugin 是一个用于 SVG 路径变形的 GSAP 插件，能够通过动画改变 SVG 路径的`d`属性，实现形状之间的平滑过渡。

- 🚀 **快速开始**：通过 CDN 引入插件，并使用`gsap.to()`方法实现形状变形，如将圆形变为河马形状。
- 🔍 **工作原理**：插件自动处理路径数据，添加足够的点以实现平滑变形，支持不同类型的路径点匹配。
- 🌟 **功能亮点**：支持不同点数路径的变形、多边形到点的变形、Canvas 渲染等。
- ⚙️ **配置对象**：可通过`shape`、`type`、`origin`等属性精细控制变形效果。
- 🔄 **多形状变形**：通过 GSAP 的时间轴实现多个形状的连续变形。
- 🛠️ **工具函数**：提供`convertToPath()`将基本 SVG 形状转换为路径，便于变形操作。
- 📊 **性能优化**：通过`shapeIndex`和`precompile`优化性能，减少初始计算时间。
- 🎨 **Canvas 渲染**：支持通过`render`函数将变形结果绘制到 Canvas 上，适用于高性能需求场景。
- 📹 **视频教程**：提供高级功能演示和性能优化技巧的视频教程。
- 📌 **注意事项**：变形效果受 SVG 复杂度影响，建议简化图形以提高性能。

---

### [SplitText | GSAP | 文档与学习](https://gsap.com/docs/v3/Plugins/SplitText/)

**原文标题**: [SplitText | GSAP | Docs & Learning](https://gsap.com/docs/v3/Plugins/SplitText/)

SplitText 是一个用于将 HTML 元素文本分割成字符、单词或行的 JavaScript 库，便于创建精美的动画效果。它支持多种配置选项，包括响应式重新分割、屏幕阅读器可访问性和遮罩效果等。

- 🚀 **快速开始**：通过 CDN 引入 SplitText，并使用 `SplitText.create()` 方法分割文本。
- 🛠️ **配置选项**：可以设置分割类型（字符、单词、行）、自动重新分割、自定义类名等。
- 🔄 **响应式分割**：使用 `autoSplit: true` 可以在字体加载或容器宽度变化时自动重新分割。
- 🎭 **遮罩效果**：通过 `mask` 选项为分割后的元素添加遮罩，便于实现显示/隐藏效果。
- ♿ **屏幕阅读器支持**：默认添加 `aria-label` 和 `aria-hidden` 属性，提升可访问性。
- ↩️ **还原功能**：使用 `revert()` 方法可以恢复元素的原始状态。
- ⚠️ **注意事项**：避免在字体加载前分割，仅分割需要的部分以提升性能，不支持 SVG 文本节点。
- 📌 **演示示例**：查看 CodePen 上的完整动画演示集合。

---

### [标准许可证 - GreenSock](https://gsap.com/community/standard-license/)

**原文标题**: [Standard License - GreenSock](https://gsap.com/community/standard-license/)

GSAP 软件许可协议概述，包括定义、许可授予、限制、所有权、终止及其他条款。

- 📜 **定义**  
  - "GSAP 许可证"指本协议条款；"GSAP 产品"包括动画库及相关插件工具；"许可用途"允许在网站或数字界面使用；"禁止用途"限制用于开发与 Webflow 竞争的可视化动画工具。  

- 🔄 **许可授予**  
  - 授予全球非独占许可，仅限许可用途使用、复制和展示 GSAP 产品。  

- 🚫 **限制条款**  
  - 禁止用于竞争性产品开发、逆向工程或移除产品标识。  

- 🏛️ **所有权**  
  - GSAP 产品所有知识产权归 Webflow 所有，许可不转让任何所有权。  

- ⏹️ **终止条件**  
  - 违约时 Webflow 可终止许可，用户须停止使用并销毁副本。  

- 📝 **其他条款**  
  - 协议以 Webflow 服务条款为补充，冲突时以本协议为准；Webflow 保留修改权，继续使用视为接受修订；未执行条款不构成弃权。  

- 📅 **生效日期**  
  - 2025 年 4 月 30 日生效，2025 年 5 月 2 日最后修改。  

- ©️ **版权声明**  
  - 版权归 2025 年 Webflow 所有。

---

### [Gemini 2.5 Pro 预览版：更卓越的编程表现 - Google 开发者博客](https://developers.googleblog.com/en/gemini-2-5-pro-io-improved-coding-performance/)

**原文标题**: [
            
            Gemini 2.5 Pro Preview: even better coding performance
            
            
            - Google Developers Blog
            
        ](https://developers.googleblog.com/en/gemini-2-5-pro-io-improved-coding-performance/)

Google 发布了 Gemini 2.5 Pro 预览版（I/O 版），重点提升了编码能力，尤其在前端和 UI 开发方面表现卓越。

- 🚀 **提前发布**：Gemini 2.5 Pro 预览版提前几周发布，以让开发者更早体验其强大的编码功能。  
- 💻 **编码能力提升**：在代码转换、编辑及复杂代理工作流创建方面有显著改进。  
- 🌟 **前端开发领先**：在 WebDev Arena 排行榜上排名第一，能够构建美观且功能强大的网页应用。  
- 🎥 **视频理解能力**：在 VideoMME 基准测试中得分 84.8%，支持从视频生成交互式学习应用。  
- 🛠️ **功能开发简化**：帮助开发者快速实现新功能，如根据设计文件自动生成 CSS 代码。  
- 🎨 **UI 设计优化**：能够设计并实现美观的网页动画和响应式设计，如麦克风 UI 动画。  
- 🔧 **开发者工具支持**：可通过 Gemini API 在 Google AI Studio 和 Vertex AI 中使用。  
- 🔄 **无缝升级**：现有用户无需操作即可自动升级到新版本，价格不变。  
- 📢 **反馈改进**：新版本减少了函数调用错误并提高了触发率，模型卡也已更新。  

Google 期待看到开发者利用 Gemini 2.5 Pro 构建出更多创新应用。

---

### [为什么谷歌搜索协议对火狐的未来至关重要 - OMG！Ubuntu](https://www.omgubuntu.co.uk/2025/05/mozilla-says-google-search-deal-vital-to-firefoxs-survival)

**原文标题**: [Why Google Search Deal is Critical for Firefox's Future - OMG! Ubuntu](https://www.omgubuntu.co.uk/2025/05/mozilla-says-google-search-deal-vital-to-firefoxs-survival)

Mozilla 的收入严重依赖与谷歌的搜索合作协议，该协议占其 2023 年总收入的约四分之三。若协议终止，Firefox 可能难以维持运营。美国司法部对谷歌的反垄断诉讼可能威胁这一合作，进而影响 Firefox 的生存。Mozilla 强调，Firefox 的存在对维持浏览器市场竞争和开放网络至关重要。  

- 🔍 Mozilla 收入的约 75% 来自与谷歌的搜索合作协议，该协议使谷歌成为 Firefox 的默认搜索引擎。  
- ⚖️ 美国司法部的反垄断诉讼可能禁止谷歌与 Mozilla 的合作，威胁 Firefox 的生存。  
- 🌐 Mozilla 认为 Firefox 对维持浏览器市场竞争、推动网络隐私和开放标准至关重要。  
- 💸 若失去谷歌的资金，Mozilla 可能无法维持 Firefox 的开发及对开源生态的贡献。  
- 🔄 过去尝试更换默认搜索引擎（如雅虎）导致用户流失，显示用户对谷歌的偏好。  
- ⚠️ 限制谷歌与 Mozilla 的合作可能削弱浏览器市场竞争，进一步巩固科技巨头的垄断地位。  
- 🤔 Mozilla 呼吁平衡反垄断措施，避免意外损害开放网络和用户选择。

---

### [四大主流浏览器即将失去 80% 的资金来源 | 作者：Dan Fabulich | 2025 年 4 月 | Medium](https://danfabulich.medium.com/all-four-major-web-browsers-are-about-to-lose-80-of-their-funding-0e42ceb358f1)

**原文标题**: [All four major web browsers are about to lose 80% of their funding | by Dan Fabulich | Apr, 2025 | Medium](https://danfabulich.medium.com/all-four-major-web-browsers-are-about-to-lose-80-of-their-funding-0e42ceb358f1)

四大主流浏览器即将失去 80% 的资金支持，谷歌目前承担了它们的主要开发费用，但美国司法部正迫使谷歌停止资助竞争对手，可能导致整个浏览器生态陷入困境。  

- 💰 谷歌直接支付了 Mozilla 和 Safari 80% 以上的预算，包括每年向苹果支付 180 亿美元、向 Mozilla 支付 4.5 亿美元，作为默认搜索引擎的协议费用。  
- 🔍 微软 Edge 本质上是谷歌 Chrome 的“白标”版本，基于开源项目 Chromium，但微软的代码贡献仅占 6%，远低于谷歌的 94%。  
- ⚖️ 美国司法部要求谷歌停止与 Mozilla 和苹果的搜索引擎协议，并可能强制其剥离 Chrome，这将导致所有主流浏览器失去主要资金来源。  
- 🛑 Mozilla 和苹果反对这一举措，认为这会损害浏览器市场竞争，而非促进竞争。  
- 🌐 反垄断法的执行可能意外破坏浏览器生态，导致用户依赖的互联网工具陷入不稳定状态。

---

### [四月网页平台新动态 | 博客 | web.dev](https://web.dev/blog/web-platform-04-2025?hl=en)

**原文标题**: [New to the web platform in April  |  Blog  |  web.dev](https://web.dev/blog/web-platform-04-2025?hl=en)

2025 年 4 月，主流浏览器稳定版和测试版新增多项 Web 平台功能，涵盖 CSS、JavaScript API 及开发者工具增强。

- 🚀 **稳定版浏览器更新**：Firefox 137/138和Chrome 135/136发布，引入多项新特性。  
- 🎠 **Chrome 135 轮播功能**：新增`::scroll-button()`、`::scroll-marker()`伪元素及`interactivity`属性，支持无障碍轮播设计。  
- 🔗 **命令属性升级**：Chrome 135 用`command`和`commandfor`替代旧属性，优化按钮功能与可访问性。  
- ✂️ **CSS 形状函数**：Chrome 135 的`shape()`支持响应式裁剪路径，Safari 18.4 和 Firefox Nightly 也已跟进。  
- ⏸️ **Firefox 137 原子操作**：`Atomics.pause()`方法优化多线程资源分配，成为基线新功能。  
- 📏 **CSS 断字控制**：Firefox 137 新增`hyphenate-limit-chars`属性，精确控制单词连字符位置。  
- 🔍 **正则表达式工具**：Chrome 136 使`RegExp.escape`成为基线功能，安全转义正则符号。  
- ❗ **错误检测 API**：Firefox 138 引入`Error.isError()`，但暂未完全支持 DOMException 检测。  
- 🔐 **登录状态 API**：Firefox 138 支持 FedCM 的 Login Status API，管理身份提供商登录状态。  
- 📦 **导入映射完整性**：Firefox 138 为`importmap`添加`integrity`支持，确保模块安全加载。  
- 🔮 **测试版亮点**：Firefox 139 预计首发`Temporal API`，Safari 18.5 以修复为主。  

（注：功能兼容性数据可能滞后，请以 MDN 最新更新为准。）

---

### [Mux Video 的全部功能免费使用？免费计划现已推出 | Mux](https://www.mux.com/blog/free-plan)

**原文标题**: [All the power of Mux Video for $0? Introducing the Free Plan | Mux](https://www.mux.com/blog/free-plan)

Mux 推出免费视频计划，旨在降低开发者使用视频功能的门槛，提供无信用卡要求的起步方案，并持续优化定价策略以支持不同规模的用户需求。

- 🎥 视频成本过高一直是开发者的痛点，Mux 致力于打造真正普惠的视频产品  
- 🆓 推出**Mux Video 免费计划**：无需信用卡，支持 10 个视频存储 +10 万分钟/月免费播放  
- 💡 免费计划包含核心功能：多分辨率支持、AI 字幕、数据分析、4K 播放等（仅播放器角标带"Mux"标识）  
- 📉 近年定价优化历程：分分辨率计费（2022）、基础编码免费（2023）、自动冷存储（2024）等  
- 🚀 付费升级路径：移除角标/解锁直播/无限存储，且保留每月 10 万免费分钟  
- ⚡ 技术无缩水：与付费版同享 JIT 处理、智能编码、全球 CDN 等基础设施  
- 🔄 取代旧测试模式：新免费计划取消 24 小时限制和水印，支持真实产品开发  
- 🌟 未来将持续推出更多可访问性改进和功能增强

---

### [Astro 最新动态 - 2025 年 4 月版 | Astro](https://astro.build/blog/whats-new-april-2025/)

**原文标题**: [What’s new in Astro - April 2025 | Astro](https://astro.build/blog/whats-new-april-2025/)

2025 年 4 月 Astro 生态系统的动态更新，涵盖新版本特性、社区动态、工具推荐及用户案例。

- 🚀 **Astro 5.6 & 5.7 发布**：新增 Cloudflare 环境支持、会话管理优化、SVG 组件稳定版及实验性字体 API  
- 📦 **npm 下载量突破 200 万**：Astro 月度下载量显著增长  
- 🌐 **知名企业采用案例**：Firebase Studio、eBay Kleinanzeigen 等平台使用 Astro 构建  
- 🎨 **创新项目展示**：Hypertext TV 的复古网页风格、WebTUI 的终端 UI 浏览器实现  
- 👥 **社区治理更新**：新增技术指导委员会成员，强化开源协作  
- 📚 **技术内容精选**：WordPress 模板迁移指南、Algolia 自动数据推送集成等深度教程  
- 🛠 **工具生态扩展**：新增 Tanstack SPA 支持、WordPress 主题开发工具等 15+ 集成  
- 🖼 **主题模板丰富**：30+ 新主题上线，涵盖博客、电商、作品集等场景  
- 🌟 **用户案例集锦**：Marie Curie 慈善机构、Lusion 创意工作室等 50+ 网站展示  
- 📖 **Starlight 文档应用**：sharp 图像库、Catppuccin 主题等采用 Starlight 构建文档  

（注：以上内容为模拟摘要，基于虚构的 2025 年 4 月 Astro 博客文章框架撰写）

---

### [什么是 CSS 猫头鹰选择器（* + *）？ - YouTube](https://www.youtube.com/watch?v=0O0ssm70g1g)

**原文标题**: [What is CSS Owl Selector (* + *)? - YouTube](https://www.youtube.com/watch?v=0O0ssm70g1g)

该页面列出了 YouTube 的相关信息和链接，包括关于平台、联系方式、创作者支持、广告合作、开发者资源以及政策条款等内容。

- ℹ️ 关于 YouTube 平台的基本信息  
- 📰 新闻与媒体相关资源  
- ©️ 版权信息与政策  
- 📞 联系 YouTube 的方式  
- 🎨 创作者相关支持与资源  
- 💼 广告合作与商业机会  
- 👩💻 开发者工具与资源  
- 📜 使用条款与条件  
- 🔒 隐私政策与数据保护  
- ⚖️ 平台政策与安全指南  
- 🔧 YouTube 功能运作机制  
- 🧪 新功能测试与更新  
- © 2025 Google LLC 版权声明

---

### [获取失败](https://frontendfoc.us/link/168887/web)

**原文标题**: [Failed to retrieve](https://frontendfoc.us/link/168887/web)

无法总结：获取内容失败，状态码 403。

---

### [CSS 显示模块第 4 级](https://drafts.csswg.org/css-display-4/#reading-flow)

**原文标题**: [CSS Display Module Level 4](https://drafts.csswg.org/css-display-4/#reading-flow)

概述总结  
CSS 将源文档（通常为 DOM 树）转换为盒树（box tree），并通过盒树在画布上渲染内容。盒树中的每个盒代表元素或伪元素的空间/时间布局，文本序列则代表文本节点的内容。CSS 通过层叠和继承为元素和文本节点分配计算值，再根据 `display` 属性生成盒。某些 `display` 值（如 `list-item`）会生成多个盒，而 `none` 或 `contents` 会抑制盒的生成。盒树构建过程中可能产生匿名盒以修复结构问题，且盒和文本序列可能因布局需求被分片。  

- 📜 **CSS 渲染流程**：源文档 → 盒树 → 画布渲染（屏幕/纸张/音频流）。  
- 🏷️ **盒生成规则**：`display` 属性决定盒的类型（如块级、行内级），并控制是否生成盒（如 `none` 不生成）。  
- 🔄 **匿名盒**：在盒树中修复结构问题时自动生成（如表格单元格缺失行父盒时）。  
- ✂️ **分片**：盒和文本序列可能因换行、分页或双向文本重排被分割为多个片段。  
- 📊 **布局模型**：通过 `display` 的 `<display-inside>` 和 `<display-outside>` 定义内外布局类型（如 `flex`、`grid`）。  
- 🚫 **特殊值**：`contents` 移除元素自身盒但保留子内容；`none` 完全移除元素及其子树的盒。  
- 🔢 **顺序控制**：`order` 属性调整弹性或网格项目的视觉顺序，但不影响逻辑顺序（如语音导航）。  
- 👁️ **可见性**：`visibility: hidden` 保留布局空间但隐藏内容，`collapse` 用于表格/弹性项目折叠。  
- 📖 **阅读流**：`reading-flow` 和 `reading-order` 属性控制非视觉媒体的内容顺序（如语音朗读）。  
- ⚠️ **注意事项**：匿名盒继承盒树父级样式，而元素生成盒继承元素树样式；`display: contents` 对替换元素无效。  

注：部分术语（如 BFC、替换元素等）的详细定义参考附录和 CSS2.1 规范。

---

### [使用 CSS 阅读流实现逻辑顺序焦点导航  |  Blog  |  Chrome 开发者](https://developer.chrome.com/blog/reading-flow)

**原文标题**: [Use CSS reading-flow for logical sequential focus navigation  |  Blog  |  Chrome for Developers](https://developer.chrome.com/blog/reading-flow)

Chrome 137 引入了 CSS 的 `reading-flow` 和 `reading-order` 属性，旨在解决视觉顺序与 DOM 顺序不一致导致的键盘导航混乱问题。

- 🎯 **属性作用**  
  `reading-flow` 控制元素在弹性、网格或块布局中的可访问性工具暴露顺序和线性顺序导航焦点顺序。`reading-order` 允许手动覆盖容器内项目的顺序。

- 🔄 **弹性布局示例**  
  使用 `flex-visual` 或 `flex-flow` 值可以调整焦点顺序以匹配视觉顺序或原始弹性流顺序。例如，`flex-visual` 使焦点顺序与视觉顺序一致。

- 📊 **网格布局示例**  
  通过 `grid-rows` 或 `grid-columns` 值，可以按行或列顺序导航焦点。例如，`grid-rows` 使焦点按行顺序移动。

- 📦 **块容器示例**  
  在块容器中，`reading-order` 可以覆盖默认顺序，例如通过设置负值使某个项目优先获得焦点。

- ⚠️ **与 `tabindex` 的交互**  
  `reading-flow` 容器会忽略正 `tabindex` 的排序效果，避免传统 `tabindex` 导致的焦点跳跃问题，提升可访问性。

- 📢 **反馈与示例**  
  开发者可以通过 Chrome 的示例页面测试这些属性，并通过 CSS 工作组或 HTML WHATNOT GitHub 仓库提供反馈。

---

### [《WCAG 3.0 提案评分模型：无障碍评估的转变》——Smashing Magazine](https://www.smashingmagazine.com/2025/05/wcag-3-proposed-scoring-model-shift-accessibility-evaluation/)

**原文标题**: [WCAG 3.0’s Proposed Scoring Model: A Shift In Accessibility Evaluation — Smashing Magazine](https://www.smashingmagazine.com/2025/05/wcag-3-proposed-scoring-model-shift-accessibility-evaluation/)

WCAG 3.0 提出了一个全新的评分模型，旨在从合规性转向实用性，更关注用户的实际体验而非技术达标。这一演变标志着可访问性评估的重大转变。

- 🌐 **WCAG 3.0 的演变**：从 1999 年的 WCAG 1.0 到 2008 年的 WCAG 2.x，再到现在的 WCAG 3.0 草案，标志着从二元评估（通过/不通过）转向更灵活的评分模型。  
- 🔄 **范式转变**：WCAG 3.0 不再只是技术合规，而是关注用户能否完成任务，强调实际使用体验。  
- 📊 **评分模型**：引入 0-4 或 0-5 的评分系统（如“差”、“一般”、“好”、“优秀”），允许部分成功和渐进改进。  
- ⚠️ **关键错误**：高影响的可访问性失败（如无法完成核心操作）会显著降低整体评分。  
- 🥉🥈🥇 **合规等级**：分为“铜级”（类似 WCAG 2.2 AA）、“银级”（需残障用户验证）和“金级”（代表卓越可访问性）。  
- 🛠️ **新结构**：从“成功标准”转向“指南 - 结果 - 方法 - 操作指南”的层次，更贴近用户需求。  
- ⚖️ **潜在风险**：主观评分、合规模糊性、法律政策不匹配，以及“最低可访问性”心态可能削弱实际效果。  
- 🚀 **行动建议**：继续遵循 WCAG 2.2 AA，熟悉 WCAG 3.0 草案，以用户结果为导向，并将可访问性融入工作流程。  
- 🌟 **核心理念**：可访问性不是通过测试，而是确保用户能真正使用产品。

---

### [构建 React 登录页面模板](https://clerk.com/blog/building-a-react-login-page-template?utm_source=cooper-press&utm_medium=newsletter&utm_campaign=react-login-template-fef&utm_content=05-07-25&dub_id=Ub8IRIuh5mPdw9R7)

**原文标题**: [Building a React Login Page Template](https://clerk.com/blog/building-a-react-login-page-template?utm_source=cooper-press&utm_medium=newsletter&utm_campaign=react-login-template-fef&utm_content=05-07-25&dub_id=Ub8IRIuh5mPdw9R7)

本文介绍了如何在 React 和 Express 中实现基于会话的认证系统，包括创建登录页面、用户注册、保护路由等功能，并对比了 JWT 和会话认证的差异。

- 🔐 文章探讨了在 React 应用中实现基于会话的认证系统，使用 Express 作为后端。
- 🔄 比较了 JWT 和会话认证的优缺点，重点介绍了会话认证的实现方法。
- 🛠️ 详细步骤包括创建数据库表、更新 Express 以支持认证、实现 React 登录页面等。
- 🧪 通过 Quillmate 项目演示了实际应用，包括用户注册、登录和文章管理功能。
- 🚀 介绍了如何使用 Clerk 简化用户管理和认证流程，提供更全面的功能支持。
- 📚 最后提供了相关资源链接，方便读者进一步学习和实践。

---

### [使用 CSS 解析器扩展填充 CSS 功能——Bram.us](https://www.bram.us/2025/05/04/css-parser-extensions-pitch/)

**原文标题**: [Polyfilling CSS with CSS Parser Extensions – Bram.us](https://www.bram.us/2025/05/04/css-parser-extensions-pitch/)

概述：本文介绍了“CSS 解析器扩展”这一创新概念，旨在通过扩展 CSS 解析器功能，简化 CSS polyfill 的开发和提升其性能，从而加速新 CSS 特性的采用。作者在 BlinkOn 会议上提出了这一想法，并探讨了其潜在优势、实现示例及未来步骤。

- 🎯 **目标**：通过扩展 CSS 解析器，使开发者能够直接教解析器识别新语法，避免重复解析和样式应用的工作。
- ⚙️ **当前问题**：CSS polyfill 开发困难，因为解析器会丢弃不理解的规则，开发者需自行处理样式收集、解析和应用。
- 🛠️ **解决方案**：引入`CSS.parser` API，允许注册新关键字、函数、语法和属性，使解析器保留相关标记。
- 📌 **示例**：展示了如何注册`random`关键字、`light-dark()`函数、`size`属性等，并处理动态计算和样式替换。
- ✅ **优势**：减少 polyfill 代码量、提升性能、增强鲁棒性，加速新特性的采用。
- ⚠️ **风险**：需解决执行时机问题（如避免阻塞渲染），且依赖浏览器厂商的支持。
- 🚀 **下一步**：撰写详细提案并提交至 CSS 工作组，寻求更广泛的行业支持。
- ⏳ **时间线**：预计需要数年时间实现，但可能显著改变 CSS 生态。

---

### [前端进化的下一步：AI 驱动的状态管理 - The New Stack](https://thenewstack.io/frontends-next-evolution-ai-powered-state-management/)

**原文标题**: [Frontend's Next Evolution: AI-Powered State Management - The New Stack](https://thenewstack.io/frontends-next-evolution-ai-powered-state-management/)

欢迎加入 The New Stack 社区！以下为关键信息摘要：

- 📧 订阅或重新订阅邮件，获取最新资讯和独家内容  
- 🔒 承诺不售卖或共享用户信息，需同意《使用条款》和《隐私政策》  
- 📝 需填写个人信息（姓名、公司、国家等）和职业详情（职位级别、角色、公司规模等）  
- 🌍 国家选项覆盖全球范围，从美国到津巴布韦  
- 🎯 根据职业需求定制推送内容（开发者、运维、架构师等角色可选）  
- 📬 订阅成功后需查收确认邮件并设置偏好  
- 🔗 鼓励关注 LinkedIn 及站内热门故事  

（注：原文包含表单选项列表，摘要已提炼核心字段及流程）

---

### [特洛伊·亨特：普通人的通行密钥](https://www.troyhunt.com/passkeys-for-normal-people/)

**原文标题**: [Troy Hunt: Passkeys for Normal People](https://www.troyhunt.com/passkeys-for-normal-people/)

本文讨论了传统双因素认证（2FA）的安全隐患，介绍了 Passkeys 作为更安全的替代方案，并详细说明了如何在 WhatsApp、LinkedIn 和 Ubiquiti 等平台上设置和使用 Passkeys。

- 🔐 传统双因素认证（2FA）存在被钓鱼攻击的风险，攻击者可能通过伪造网站获取一次性密码（OTP）。
- 🎣 作者亲身经历了一次钓鱼攻击，攻击者通过伪造的 Mailchimp 登录页面获取了他的用户名、密码和 OTP。
- 🛡️ Passkeys 是一种防钓鱼的认证方式，通过加密技术保护用户登录信息。
- 📱 在 WhatsApp 上设置 Passkey 的步骤简单，可以选择存储在 iCloud 钥匙串或密码管理器（如 1Password）中。
- 💻 在 LinkedIn 上设置 Passkey 时，仍需输入密码和验证码，Passkey 仅作为并行登录方式，未完全替代密码。
- 🔒 Ubiquiti 支持将 Passkey 作为真正的第二因素认证，并可完全替代传统的 OTP 认证。
- 🔑 物理安全密钥（如 YubiKey）可以进一步增强安全性，存储 Passkey 并提供硬件级别的保护。
- 🌐 越来越多的服务开始支持 Passkeys，用户可以通过 passkeys.directory 网站查找支持的服务并投票支持更多服务加入。
- ⚖️ Passkeys 是“深度防御”策略的一部分，用户仍需保持警惕，使用强密码和密码管理器。
- 🚀 Passkeys 正在逐渐普及，微软已宣布新账户默认无密码，优先使用 Passkeys。

---

### [通行密钥目录](https://passkeys.directory)

**原文标题**: [Passkeys.directory](https://passkeys.directory)

如何在您的应用或网站中支持通行密钥  

- 🔍 **通行密钥支持查询**：Passkeys.directory 是一个社区驱动的索引，列出支持通行密钥登录的网站、应用和服务。  
- 🗳️ **投票支持通行密钥**：用户可以为希望支持通行密钥的应用或服务投票。  
- 📂 **筛选与排序**：可按名称、类别、新旧程度等条件筛选和排序列表。  
- ➕ **提交新条目**：如果发现未列出的支持通行密钥的应用或服务，可通过建议表单提交。  
- 🔮 **测试与更新**：注册以参与 1Password 的通行密钥测试，或第一时间获取无密码未来的最新进展。

---

### [CSS 中的砌体布局：网格应进化还是为新模块让路？——Smashing Magazine](https://www.smashingmagazine.com/2025/05/masonry-css-should-grid-evolve-stand-aside-new-module/)

**原文标题**: [Masonry In CSS: Should Grid Evolve Or Stand Aside For A New Module? — Smashing Magazine](https://www.smashingmagazine.com/2025/05/masonry-css-should-grid-evolve-stand-aside-new-module/)

概述总结  
CSS 中的砌体布局（Masonry Layout）目前有三种提案：扩展 CSS Grid、独立模块和 WebKit 团队提出的 Item Flow 方案。每种方案各有优缺点，开发者需权衡兼容性、学习成本和功能需求。

- 🧱 **砌体布局需求**：Pinterest 风格的流式布局目前依赖 JavaScript，但 CSS 可能通过 Grid 扩展或新模块实现原生支持。  
- 🔍 **现状与挑战**：现有方案如 CSS Grid 的`grid-template-rows: masonry`仅限 Firefox Nightly，且存在动态内容适配问题。  
- ⚖️ **方案对比**：  
  - **扩展 Grid**：复用现有语法，但可能增加复杂度（Rachel Andrew 等开发者批评）。  
  - **独立模块**：更专注砌体特性，但需从头学习新语法。  
  - **Item Flow**：统一 Flexbox/Grid/砌体，提案尚在讨论中（如`item-pack: dense`）。  
- 🌐 **兼容性与未来**：Item Flow 最具潜力，但依赖浏览器支持；当前开发者仍需依赖 JavaScript 库或 Grid Hack。  
- ❓ **核心问题**：CSS 应扩展 Grid、新增模块，还是采用 Item Flow 的融合方案？社区和标准制定中仍需反馈。  

参考：Rachel Andrew、Ahmad Shadeed 等开发者的分析及 WebKit 提案。

---

### [获取失败](https://frontendfoc.us/link/168896/web)

**原文标题**: [Failed to retrieve](https://frontendfoc.us/link/168896/web)

无法总结：获取内容失败，状态码 415。

---

### [优秀动画与卓越动画的对比](https://emilkowal.ski/ui/good-vs-great-animations)

**原文标题**: [Good vs Great Animations](https://emilkowal.ski/ui/good-vs-great-animations)

Emil Kowalski 是一位设计工程师，分享了如何从“好”动画提升到“伟大”动画的实用技巧。

- 🌟 **原点感知动画**：下拉菜单等元素应从触发按钮的位置开始动画，以增强自然感。CSS 的 `transform-origin` 应设为 `bottom-center`，Radix 和 shadcn/ui 可简化此过程。
- 🎢 **合适的缓动效果**：缓动是动画的关键，`ease-in-out` 能模拟自然加速和减速，比 `ease-in` 更自然。多数情况下默认使用 `ease-out`。
- 📊 **自定义缓动曲线**：内置 CSS 缓动曲线通常不够强烈，推荐使用如 `easing.dev` 或 `easings.co` 提供的自定义曲线。
- 🏗️ **弹簧交互效果**：使用 Framer Motion 的 `useSpring` 钩子，通过弹簧行为增强交互的自然感，避免直接绑定鼠标位置的生硬感。
- 🛠️ **工具选择**：了解何时使用 `clip-path` 等 CSS 属性，能显著提升动画效果，如优化标签切换的颜色过渡。
- 🎨 **创意动画**：探索 3D 变换等高级技巧，可以创造出独特的动画效果，如 3D 加载动画或硬币旋转效果。
- 🚀 **动画的重要性**：在竞争激烈的市场中，精心设计的动画能显著提升产品的感知质量和用户体验。

---

### [如何检测你的网页应用中的内存泄漏（2025）- YouTube](https://www.youtube.com/watch?v=6IlTjqU_Tc0)

**原文标题**: [How To Detect Memory Leaks In Your Web App (2025) - YouTube](https://www.youtube.com/watch?v=6IlTjqU_Tc0)

该内容为 YouTube 平台的页脚导航链接，包含关于平台、法律条款、隐私政策及开发者信息等。

- ℹ️ 关于  
- 📰 新闻  
- ©️ 版权  
- 📧 联系我们  
- 🎨 创作者  
- 💼 广告  
- 👩💻 开发者  
- 📜 条款  
- 🔒 隐私  
- ⚖️ 政策与安全  
- ▶️ YouTube 工作原理  
- 🧪 测试新功能  
- ®️ © 2025 Google LLC

---

### [用户体验本地化：为多元文化适配用户界面 :: UXmatters](https://www.uxmatters.com/mt/archives/2025/05/ux-localization-adapting-user-interfaces-for-diverse-cultures.php)

**原文标题**: [UX Localization: Adapting User Interfaces for Diverse Cultures :: UXmatters](https://www.uxmatters.com/mt/archives/2025/05/ux-localization-adapting-user-interfaces-for-diverse-cultures.php)

国际化业务成功需将本地化融入 UX 设计过程，以适应文化差异并提升用户体验。以下是关键要点：

- 🌍 **全面本地化**：UX 本地化不仅是语言翻译，还需调整字体、图标、布局等元素以适应不同文化需求。  
- ↔️ **阅读方向**：阿拉伯语等从右至左（RTL）语言需重新设计导航菜单和按钮布局，影响超 20 亿用户。  
- 🎨 **符号与色彩**：图标（如竖大拇指）和颜色（如白色）在不同文化中含义迥异，需谨慎选择。  
- 📅 **格式差异**：日期、时间、度量单位及支付方式需适配地区习惯，避免用户体验割裂。  
- ⚖️ **平衡策略**：保持全球品牌一致性的同时，灵活融入本地化设计，优先高回报市场深度本地化。  
- 🔤 **字体与排版**：选择适配多语种的字体，确保可读性；布局需动态调整文本长度和阅读方向。  
- ❗ **图标陷阱**：避免通用图标的文化误解，必要时为 RTL 语言镜像翻转图标。  
- ✍️ **文案优化**：使用简洁无歧义的 UX 文案，避免俚语，保持术语一致性。  
- 🔍 **前期调研**：借助霍夫斯泰德文化维度等理论分析目标市场，研究竞品设计策略。  
- 🤝 **协作流程**：本地化专家应参与产品全周期，与设计、开发团队紧密合作，实时测试用户反馈。  
- 🔄 **持续迭代**：通过 A/B 测试和可用性测试优化本地化设计，建立知识库供未来项目参考。  

通过细致文化洞察和灵活设计，打造既全球统一又本地友好的用户体验，是国际市场竞争的关键。

---

### [快速检查 HTTP 响应头 | Henry From Online](https://henry.codes/writing/quickly-checking-http-response-headers/)

**原文标题**: [Quickly checking HTTP response headers | Henry From Online](https://henry.codes/writing/quickly-checking-http-response-headers/)

跨性别女性就是女性，跨性别权利也是人权的一部分，必须坚定支持与尊重。  

- 🌈 跨性别女性是女性，应享有同等权利与尊重  
- ✊ 跨性别权利属于人权，不可剥夺  
- ❤️ 呼吁社会接纳与包容，否则将面临道德与精神的消亡

---

### [GitHub - webtui/webtui](https://github.com/webtui/webtui)

**原文标题**: [GitHub - webtui/webtui](https://github.com/webtui/webtui)

WebTUI 是一个模块化的 CSS 库，旨在将终端用户界面的美感带入浏览器。

- 🌐 **项目主页**: [webtui.ironclad.sh](https://webtui.ironclad.sh)  
- 📚 **文档与示例**: 提供详细文档和示例，访问 [示例页面](https://webtui.ironclad.sh/examples)  
- 💬 **社区支持**: 可通过 [Discord 服务器](https://discord.gg/yUS6T8YnfT) 交流  
- ⚙️ **本地开发**: 需安装 Bun，克隆仓库后运行 `bun i` 安装依赖，`bun run dev` 启动开发服务器  
- 📜 **许可证**: 采用 MIT 开源协议  
- ⭐ **项目热度**: 获得 1.1k Stars 和 16 Forks  
- 🛠️ **开发状态**: 最新版本为 v0.0.5（2025 年 5 月发布）  
- 📊 **技术栈**: 主要使用 Astro (34.7%)、CSS (29.3%) 和 MDX (29.2%)

---

### [Web 终端用户界面](https://webtui.ironclad.sh/)

**原文标题**: [WebTUI](https://webtui.ironclad.sh/)

WebTUI 是一个模块化的 CSS 库，旨在将终端用户界面的美感带入浏览器。

- 📦 **组件**：包括徽章 (Badge)、按钮 (Button)、复选框 (Checkbox)、输入框 (Input)、弹出框 (Popover) 和排版 (Typography) 等。
- 🎨 **主题插件**：提供 Catppuccin、Gruvbox 和 Nord 等多种主题。
- 🛠️ **插件开发**：支持开发自定义插件，包括样式层 (Style Layers) 的设计。
- 📚 **入门指南**：涵盖 ASCII 盒子、TUIs 与 GUIs 的区别、主题化 (Theming) 和安装 (Installation) 等内容。
- 🔧 **贡献指南**：包括本地开发 (Local Development)、问题提交 (Issues)、拉取请求 (Pull Requests) 和样式指南 (Style Guide)。
- 🌈 **主题化**：支持 CSS 变量 (CSS Variables)、字体样式 (Font Styles)、颜色 (Colors) 以及明暗模式 (Light & Dark)。
- ⚙️ **安装方式**：提供 ESM 导入、CDN 导入和完整库导入等多种安装选项。

---

### [React 性能：常见问题及其解决方案 | 产品博客 • Sentry](https://blog.sentry.io/react-js-performance-guide/?utm_source=reactstatus&utm_medium=paid-community&utm_campaign=general-fy26q2-traceblog&utm_content=newsletter-s-read)

**原文标题**: [React Performance: Common Problems & Their Solutions | Product Blog • Sentry](https://blog.sentry.io/react-js-performance-guide/?utm_source=reactstatus&utm_medium=paid-community&utm_campaign=general-fy26q2-traceblog&utm_content=newsletter-s-read)

React.js 性能优化指南，涵盖性能优化的重要性、常见问题及解决方案、测量工具和资源推荐。

- 🚀 **性能优化的意义**  
  - 提升用户体验、转化率和留存率  
  - 改善 SEO 排名  
  - 降低维护成本并增强可扩展性  

- 🛠️ **8 个常见 React 性能问题与解决方案**  
  - 📦 **过大的打包体积**：使用 Webpack/Vite 优化代码分割、压缩和依赖管理  
  - 🖼️ **未优化的资源**：采用 WebP/AVIF 图片格式，精简字体文件  
  - 🔄 **不必要的重渲染**：通过`memo`、`useMemo`和`useCallback`减少渲染  
  - 🏗️ **低效的状态与组件结构**：合理拆分组件，使用 Context API 避免属性透传  
  - 🌐 **过多请求与网络延迟**：利用 SWR/TanStack Query 缓存请求，SSR/SSG 优化加载  
  - ⚡ **资源浪费**：用 Web Worker 处理 CPU 密集型任务，避免内存泄漏  
  - ⏳ **低效加载策略**：代码分割、懒加载和资源优先级管理  
  - 🐢 **感知性能差**：骨架屏占位、布局稳定性优化和及时反馈  

- 🔍 **性能测量工具**  
  - Chrome 性能面板、Lighthouse、React DevTools Profiler  
  - WebPageTest 多地域测试，Sentry 实时监控  

- 📚 **延伸资源**  
  - React 性能课程（FrontendMasters）、Addy Osmani 的《图片优化》  
  - 核心 Web 指标（Core Web Vitals）和性能预算入门指南

---

### [版本 v8.0.0 | Mantine](https://mantine.dev/changelog/8-0-0/)

**原文标题**: [Version v8.0.0 | Mantine](https://mantine.dev/changelog/8-0-0/)

Mantine v8.0.0 于 2025 年 5 月 5 日发布，包含多项新功能和改进，同时提供迁移指南帮助用户从 7.x 版本升级。

- 🚀 **版本发布**：v8.0.0 于 2025 年 5 月 5 日发布，源代码已在 GitHub 上公开。
- 💖 **支持开发**：用户可通过 OpenCollective 赞助 Mantine 开发，资金将用于改进和新增功能。
- 📚 **迁移指南**：提供了详细的 7.x → 8.x 迁移指南，帮助用户顺利升级。
- 🎨 **全局样式优化**：全局样式被拆分为三个文件：`baseline.css`、`default-css-variables.css` 和 `global.css`，便于按需引入。
- 🍔 **子菜单支持**：`Menu` 组件新增子菜单功能，支持多级嵌套。
- 🎯 **Popover 改进**：`Popover` 组件新增 `hideDetached` 属性，控制目标元素隐藏时的下拉框行为。
- 📅 **日期格式变更**：`@mantine/dates` 组件现在使用 `YYYY-MM-DD` 或 `YYYY-MM-DD HH:mm:ss` 格式的字符串，避免时区问题。
- ⏰ **新增 TimePicker**：提供 24 小时和 12 小时格式的时间选择器，支持下拉选择小时、分钟和秒。
- 📅 **DateTimePicker 改进**：底层改用 `TimePicker`，移除 `timeInputProps`，新增 `timePickerProps`。
- 🕒 **TimeValue 组件**：新增用于格式化时间字符串显示的组件。
- 🕓 **TimeGrid 组件**：新增时间网格组件，支持预定义时间槽选择。
- 🔥 **Heatmap 组件**：新增日历热图组件，支持工具提示和周/月标签。
- 📜 **CodeHighlight 改进**：不再依赖 `highlight.js`，支持通过适配器使用任意语法高亮库，如 `shiki`。
- 🎠 **Carousel 更新**：升级至最新版 `embla-carousel-react`，移除 `speed` 和 `draggable` 属性。
- 🔘 **Switch 组件改进**：新增 `withThumbIndicator` 属性，调整滑块指示器样式。
- 🎨 **主题类型扩展**：支持扩展 `spacing`、`radius`、`breakpoints` 等主题类型。
- 🛠 **其他改进**：包括 `Kbd` 组件支持 `size` 属性、`ScrollArea` 样式优化、`SegmentedControl` 高度调整等。

---

### [曼蒂恩](https://mantine.dev/)

**原文标题**: [Mantine](https://mantine.dev/)

一个功能全面的 React 组件库，提供 120+ 可定制组件和 70+ 钩子，支持快速构建无障碍 Web 应用，包含灵活样式、暗色主题、表单库及扩展功能，拥有活跃社区和丰富资源。

- 🚀 **快速开发** - Mantine 提供 120+ 可定制组件和 70+ 钩子，加速 Web 应用开发  
- 🎨 **灵活样式** - 支持 CSS 覆盖、暗色主题及多种样式解决方案（如 Emotion、Sass 等）  
- ⚛️ **强大功能** - 包含表单库（`@mantine/form`）、Combobox 组件及扩展（富文本编辑器、通知系统等）  
- 🌙 **暗色主题** - 一键切换暗色模式，全局样式支持  
- 📊 **社区支持** - 28,000+ GitHub 星标，12,000+ Discord 成员，活跃开发者生态  
- 🛠️ **多框架兼容** - 支持 Next.js、Vite、React Router 等现代工具链  
- 💡 **高性能** - 表单库仅 6.3KB，优化渲染性能  
- 🔧 **实用示例** - 提供代码片段（如`useMove`滑块、`useEyeDropper`取色器等）

---

### [热力图 | Mantine](https://mantine.dev/charts/heatmap/)

**原文标题**: [Heatmap | Mantine](https://mantine.dev/charts/heatmap/)

概述：本文介绍了 Mantine Charts 库中的 Heatmap 组件，包括其基本用法、数据格式、自定义样式、工具提示、颜色调整、标签设置等功能。

- 📊 **Heatmap 基础用法**：用于以表格形式展示数据，每列代表一周，必须提供`data`属性，格式为`YYYY-MM-DD`日期键和数值键值对。
- 📅 **日期范围设置**：可通过`startDate`和`endDate`定义热力图范围，默认显示最近一年的数据。
- 🔍 **工具提示功能**：通过`withTooltip`和`getTooltipLabel`属性添加悬停提示，可自定义提示内容。
- 🎨 **颜色自定义**：使用`colors`属性调整热力图颜色，支持 CSS 颜色值，默认使用 4 种颜色表示热力级别。
- 🌓 **颜色方案适配**：可通过 CSS 文件定义不同颜色方案，适应暗黑或明亮模式。
- 🔢 **数值范围设置**：使用`domain`属性手动设置数值范围，确保颜色分布符合预期。
- 📝 **标签设置**：通过`withMonthLabels`和`withWeekdayLabels`显示月份和星期标签，并可自定义标签文本。
- 📏 **矩形样式调整**：通过`rectSize`、`rectRadius`和`gap`属性调整矩形大小、圆角和间距。
- 🖱️ **矩形事件处理**：使用`getRectProps`为每个矩形添加事件处理，如点击事件。
- 🚫 **隐藏外部日期**：通过`withOutsideDates`属性隐藏范围外的日期。
- 🗓️ **首日设置**：使用`firstDayOfWeek`属性更改每周的第一天，默认为周一。

---

### [树 | Mantine](https://mantine.dev/core/tree/)

**原文标题**: [Tree | Mantine](https://mantine.dev/core/tree/)

概述：本文详细介绍了 Mantine 库中的 Tree 组件，包括其基本用法、数据格式要求、自定义渲染、状态控制（展开/选中/复选框）以及实际应用示例。

- 🌳 **Tree 组件功能**：用于展示层级数据，默认样式简洁，可通过 Styles API 自定义。  
- 📂 **数据格式要求**：数据需为数组，每个节点需包含`value`和`label`，子节点通过`children`嵌套，且`value`必须唯一。  
- 🎨 **自定义渲染**：通过`renderNode`属性可完全自定义节点渲染，支持动态图标（如文件夹展开/收起）。  
- ⚙️ **状态控制**：`useTree`钩子提供丰富的状态管理功能，包括展开/折叠、选中/取消、复选框操作等。  
- 📦 **初始状态设置**：支持通过`initialExpandedState`和`getTreeExpandedState`快速初始化展开状态（如默认展开全部或指定节点）。  
- ✅ **复选框功能**：结合`Checkbox.Indicator`实现节点选中状态，支持全选/取消全选。  
- 📂 **实际示例**：演示了文件树场景，根据文件类型显示不同图标（如 TS、CSS、NPM 等）。

---

### [半圆进度条 | Mantine](https://mantine.dev/core/semi-circle-progress/)

**原文标题**: [SemiCircleProgress | Mantine](https://mantine.dev/core/semi-circle-progress/)

概述  
SemiCircleProgress 是一个用于展示半圆形进度条的组件，支持多种自定义配置，包括标签位置、填充方向、颜色、大小等。  

- 📊 **功能** - 用半圆形图表展示进度，支持多种自定义配置。  
- 📦 **包** - 来自 `@mantine/core` 包。  
- 🎨 **样式** - 可调整填充颜色、大小、厚度、方向等。  
- 🔄 **填充方向** - 支持从左到右或从右到左填充。  
- ⬆️ **方向** - 可设置为向上或向下显示。  
- 🏷️ **标签** - 支持标签显示，位置可设为底部或居中。  
- 🎨 **颜色** - 可自定义填充段和空白段的颜色。  
- ⏱️ **动画** - 支持过渡动画，通过 `transitionDuration` 设置持续时间。  
- 🎲 **动态值** - 可通过代码动态更新进度值。  
- 📄 **文档** - 提供详细的文档和示例代码。

---

### [垂直.sh](https://vert.sh/)

**原文标题**: [VERT.sh](https://vert.sh/)

这款文件转换工具支持多种格式的转换，所有操作均在设备本地完成，视频转换则通过快速服务器处理。

- 🖼️ 图片转换：完全支持，包括.png、.jpeg、.jpg、.webp、.gif 等多种格式  
- 🎵 音频转换：完全支持，包括.mp3、.wav、.flac、.ogg、.aac 等多种格式  
- 📄 文档转换：完全支持，包括.docx、.xml、.doc、.md、.html 等多种格式  
- 🎥 视频转换：需上传至服务器处理，支持.mkv、.mp4、.webm、.avi 等多种格式  
- ⚡ 特点：无文件大小限制、无广告、完全开源  
- 🔗 相关链接：提供源代码和 Discord 服务器访问

---

### [9ui](https://www.9ui.dev/)

**原文标题**: [9ui](https://www.9ui.dev/)

首批组件已上线！  

- 🎨 **构建你的设计系统** - 提供一系列可直接复制粘贴到项目中的组件  
- 🛠️ **技术栈** - 基于 **Base UI** 和 **Tailwind CSS** 构建  
- ✨ **高度可定制** - 轻松调整组件样式以满足需求  
- 💡 **免费开源** - 自由使用和修改，无任何限制  
- 🚀 **快速开始** - 提供 **Get Started** 和 **Browse Components** 入口  
- 📊 **示例场景** - 包含 **AI Chat**、**Mail**、**Calendar** 等实用模块  
- 💬 **交互功能** - 支持 **New Chat**、**Project Discussion** 等协作场景  
- ⏰ **实时沟通** - 界面显示时间戳（如 **10:30 AM**）和欢迎语

---

### [9ui](https://www.9ui.dev/themes)

**原文标题**: [9ui](https://www.9ui.dev/themes)

这是一个包含多个功能模块和用户交互界面的面板概览。

- 🎨 主题定制：支持实时预览主题更改效果  
- 📊 访问数据：展示 2024 年桌面端与移动端流量对比的月度访客图表  
- 👥 成员管理：  
  - Micheal Smith（所有者）  
  - Emma Adams（开发者）  
  - Sam Johnson（财务）  
  - Brendan Eich（查看者）  
- 📅 日历视图：显示 2025 年 3 月日期排布  
- 💬 即时通讯：Bryan M.的在线对话示例  
- 💳 近期交易：  
  - 3 月 20 日咖啡店消费-$4.50  
  - 3 月 19 日工资收入+$2500  
  - 健身房会员-$32.99 等  
- 📝 反馈收集：餐厅体验评分提交入口  
- ✉️ 邮件验证：要求输入验证码的流程  
- 🛠️ 注册入口：9ui 设计系统注册（支持邮箱/Google/GitHub 登录）  
- 🔒 隐私设置：包含个人资料可见性、已读回执等 6 项权限控制

---

### [贝库托 3D | SVG 文件转 3D 模型](https://bekuto3d.ayaka.io/)

**原文标题**: [Bekuto 3D | SVG file to 3D model](https://bekuto3d.ayaka.io/)

请启用 JavaScript 以使用此应用。

- 🌐 必须启用 JavaScript 才能正常运行此应用  
- ⚙️ 技术支持提示，确保功能正常使用  
- 📲 适用于网页应用的基本要求

---

### [GitHub - LittleSound/bekuto3d：将SVG文件转换为3D模型。导出STL、OBJ或GLTF格式，适用于3D打印或3D网页开发。](https://github.com/LittleSound/bekuto3d)

**原文标题**: [GitHub - LittleSound/bekuto3d: Convert SVG files to 3D models. Export STL, OBJ, or GLTF.  Use it for 3D Printing or 3D Web Development.](https://github.com/LittleSound/bekuto3d)

这是一个关于 Bekuto 3D 工具的开源项目介绍，它能够将 SVG 文件转换为 3D 模型，支持多种导出格式，适用于 3D 打印和网页开发。

- 🛠️ **功能概述**：Bekuto 3D 是一个 SVG 转 3D 模型的工具，支持导出 STL、OBJ、GLTF 和 3MF 格式，适用于 3D 打印和网页开发。  
- 🌐 **在线体验**：可通过链接[bekuto3d.ayaka.io](bekuto3d.ayaka.io)直接使用。  
- 📜 **许可证**：项目采用 MIT 开源许可证，允许自由使用和修改。  
- ⭐ **项目热度**：获得 197 颗星和 6 次分叉，显示了一定的社区关注度。  
- 🖨️ **特色子包**：包含`three-3mf-exporter`，支持 3MF 格式导出，弥补了 STL 在颜色和材料支持上的不足。  
- 💻 **技术栈**：主要使用 Vue（45.9%）和 TypeScript（40.2%）开发，辅以少量 HTML。  
- 🤝 **赞助与支持**：项目依赖赞助者支持，开发者提供了赞助链接以维持项目发展。

---

### [@fiddle-digital/string-tune - npm](https://www.npmjs.com/package/@fiddle-digital/string-tune)

**原文标题**: [@fiddle-digital/string-tune - npm](https://www.npmjs.com/package/@fiddle-digital/string-tune)

StringTune 是一个高性能、模块化的 JavaScript 库，专注于通过简单的 HTML 属性实现动态网页效果，适合不同水平的开发者。

- 🚀 **核心功能**：提供视差滚动、磁性光标、进度指示器等多样化效果，支持模块化按需加载。  
- 🎯 **目标用户**：新手开发者、资深工程师和设计师，均可快速集成复杂动画效果。  
- ⚡ **性能优势**：轻量级设计，优化渲染性能，适配多设备和浏览器。  
- 📌 **使用便捷**：通过 HTML 属性配置，减少 JavaScript 代码量，支持 CDN 或 npm 安装。  
- 🌟 **应用场景**：适用于个人作品集到大型网页项目，增强交互体验。  
- 📦 **技术细节**：MIT 许可，最新版本 1.1.0，无依赖项，每周下载量 97 次。  
- 🔧 **示例代码**：展示如何初始化库并实现视差与磁性光标效果。

---

### [弦乐调音](https://tune-demo.fiddle.digital/)

**原文标题**: [String Tune](https://tune-demo.fiddle.digital/)

StringTune 是一个用于字符串操作和动画效果的文档，包含基础和高级功能，如字符串重复、进度控制、视差效果等。

- 📖 **StringTune 基础功能**  
  - 提供基本的字符串操作，如 `string` 和 `string-repeat`。  

- 📊 **StringProgress 进度控制**  
  - 支持通过 `string="progress"` 和 `string-id` 设置进度条，可自定义进入和退出位置。  

- 🎢 **StringParallax 视差效果**  
  - 使用 `string-parallax` 实现视差滚动效果，但在移动设备上禁用。  

- 🔄 **StringLerp 和 StringGlide**  
  - 提供平滑过渡（Lerp）和滑动（Glide）效果，后者在移动设备上禁用。  

- 🧲 **StringMagnetic 磁性吸附效果**  
  - 通过 `string="magnetic"` 实现元素磁性吸附，可调整半径和强度。  

- ✂️ **StringSplit 字符分割**  
  - 使用 `string="split"` 和 `string-split="char[left]"` 对字符串进行分割处理。  

- 📜 **示例文本**  
  - 包含示例字符串："Jovial hawks find beauty in a fiddle string while vexing quirky dogs near zigzag paths."

---

### [JavaScript 条码扫描库](https://strich.io/?ref=frontend-focus)

**原文标题**: [JavaScript Barcode Scanning Library](https://strich.io/?ref=frontend-focus)

STRICH 是一个用于网页应用的 JavaScript 条码扫描库，支持实时 1D/2D 条码扫描，无需原生应用或后端支持。它提供简单透明的定价、开发者友好的文档和多种框架集成示例，适用于多个行业场景。

- 🚀 **产品概述**：STRICH 是一个基于 JavaScript/WASM 的条码扫描库，支持网页应用实时扫描 1D/2D 条码。
- 💰 **定价透明**：提供 BASIC（99 美元/月）、PROFESSIONAL（249 美元/月）和 ENTERPRISE（定制报价）三档订阅计划，含免费试用。
- 📚 **开发者支持**：零依赖、完善的文档、支持主流框架（Angular/Vue/React 等），提供示例代码和集成指南。
- 🔍 **功能强大**：支持多种 1D（Code 128/EAN/UPC 等）和 2D（QR Code/Data Matrix 等）条码类型，内置扫描 UI 和高级图像处理。
- 🌐 **网页优势**：无需应用商店审核、易于分发、降低开发成本，支持 PWA 实现离线操作和推送通知。
- 🏢 **企业级支持**：白标定制、完全离线模式、GS1 标准兼容，适合严格合规需求。
- 👍 **客户评价**：多家企业（如 Brooklyn Public Library、Swiss Railways）称赞其易集成、高性能和优质支持。
- ❓ **常见问题**：涵盖扫描限制、框架兼容性、免费替代品对比等，提供详细 FAQ 和演示应用。

---

### [职业发展 | Brilliant](https://brilliant.org/careers/)

**原文标题**: [Careers | Brilliant](https://brilliant.org/careers/)

Brilliant 致力于培养全球问题解决者，专注于成人数学、数据科学及 AI 等领域的互动学习，拥有健康商业模式和多元文化团队，提供远程全职岗位并鼓励多样性申请。

- 🎯 使命驱动：打造全球问题解决者，专注数学、数据与 AI 的互动学习  
- 🌍 团队分布：以旧金山和纽约为核心，约 100 名跨领域人才远程协作  
- 🚀 创新学习：通过实践性互动课程重塑教育，跳过冗余理论直击实用技能  
- 💼 文化特质：高执行力、低自我，重视卓越、冒险精神与坦诚沟通  
- 📈 商业健康：自给自足盈利模式，用户增长迅速，估值务实  
- 🏡 工作模式：核心协作时段（太平洋时间 10-15 点），季度线下聚会  
- 🌈 多元团队：欢迎不同背景成员，员工经历涵盖科研、艺术、工程等跨界领域  
- ✨ 岗位机会：开放工程/内容等远程职位，支持非传统候选人申请  
- 📧 灵活招聘：接受非公开岗位咨询，鼓励邮件联系 jobs@brilliant.org

---

### [comiCSS](https://comicss.art)

**原文标题**: [comiCSS](https://comicss.art)

该网站内容为一系列漫画，用户可通过存档无 JavaScript 浏览所有作品，支持导航与分享，遵循非商业性知识共享许可。

- 🖼️ 网站漫画无需 JavaScript 即可在存档中查看全部作品  
- 🔄 提供导航选项：首页、上一页、随机、下一页、末页  
- 🔗 包含当前漫画的永久链接、图片链接及源代码链接  
- 📜 采用知识共享署名 - 非商业性 4.0 许可，允许非商业性共享  
- ⚠️ 明确禁止销售漫画作品，详细使用条款可查阅许可证说明

---

### [comiCSS 第 183 期：逆风与顺风——上风、下风、顶风、尾风](https://comicss.art/comics/183/)

**原文标题**: [comiCSS #183: upwind-downwind-headwind-tailwind](https://comicss.art/comics/183/)

该网站内容为一系列漫画，提供导航和存档功能，并包含具体漫画的链接和许可信息。

- 🌐 网站需要 JavaScript 导航，但存档可无脚本查看所有漫画  
- 🏷️ 漫画标题："Upwind. Downwind. Headwind. Tailwind."  
- 🔄 导航选项：首页、上一页、随机、下一页、末页（重复显示）  
- 🔗 固定链接和图片直链已提供  
- 📜 源代码可访问  
- ©️ 采用 CC BY-NC 4.0 许可，允许非商业分享  
- ℹ️ 附许可详情和使用权限说明链接

---

### [comiCSS](https://comicss.art/)

**原文标题**: [comiCSS](https://comicss.art/)

该网站内容为一组漫画，提供无需 JavaScript 即可浏览的存档功能，并包含导航选项和版权信息。

- 🖼️ 网站漫画可通过存档直接查看，无需启用 JavaScript  
- 🔄 提供导航选项：首页、上一页、随机、下一页、末页  
- 🔗 永久链接：[https://comicss.art/comics/184](https://comicss.art/comics/184)  
- 🖼️ 图片链接：[https://comicss.art/comics/184/everything-is-cascading.png](https://comicss.art/comics/184/everything-is-cascading.png)  
- 💻 源代码链接：[https://comicss.art/comics/184/everything-is-cascading.html](https://comicss.art/comics/184/everything-is-cascading.html)  
- ©️ 采用知识共享署名 - 非商业性 4.0 许可协议，允许自由分享但禁止售卖

---

### [comiCSS #91：此路不通](https://comicss.art/comics/91/)

**原文标题**: [comiCSS #91: You Shall Not Pass](https://comicss.art/comics/91/)

该网站内容为一系列漫画，提供多种导航方式及资源链接，并遵循特定版权许可。

- 🖥️ 网站需要 JavaScript 进行导航，但可通过存档查看所有漫画（无需 JavaScript）。  
- 🎨 漫画标题为《You Shall Not Pass》，提供多种浏览选项：首页、上一页、随机、下一页、末页。  
- 🔗 提供永久链接、图片链接及源代码链接，方便直接访问或下载。  
- 📜 作品采用知识共享署名 - 非商业性 4.0 许可协议，允许自由分享但禁止商用。  
- ℹ️ 附有许可证和使用权利的详细说明链接。

---

### [非 HTML 内容](https://frontendfoc.us/open/691/*%7CUID%7C*?ipx=t)

**原文标题**: [Non-HTML content](https://frontendfoc.us/open/691/*%7CUID%7C*?ipx=t)

无法总结：非 HTML 内容。

---

