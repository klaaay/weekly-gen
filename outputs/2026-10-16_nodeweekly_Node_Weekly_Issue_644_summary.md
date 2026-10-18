### [Skia 画布](https://skia-canvas.org/)

**原文标题**: [Skia Canvas](https://skia-canvas.org/)

Skia Canvas 是一个无需浏览器的无头矢量图形渲染器和桌面窗口工具包，让你在 Node.js 中用熟悉的 Canvas API 绘图，背后由 Chrome 使用的 GPU 加速引擎 Skia 驱动，并可在服务端或原生窗口渲染、导出多种格式，性能基准中显著快于同类库。  
- 🎨 用标准 Canvas API 在 Node.js 中运行，无需浏览器，底层基于 Skia。  
- 🖼️ 兼容 canvas 标准且依赖少，并扩展出远超浏览器 `<canvas>` 的 2D 能力。  
- 📤 可生成 PDF、SVG 矢量图和 JPEG、PNG、WEBP、RAW 位图，保存到文件、dataURL、Buffer 或 Sharp 对象。  
- 📚 支持多页画布，可输出多页 PDF 或图像序列，也能加载多页 PDF 并继续编辑绘制。  
- 📐 可加载 PDF/SVG 为分辨率无关图像，支持 Path2D 切片、采样、布尔运算及轮廓/动词/点分解。  
- 🌈 支持 Display P3 宽色域和 CSS Color 4 语法，渐变可选择色彩空间与色相插值。  
- 🧊 支持 3D 透视变换、缩放旋转平移、纹理/图案填充和自定义描边标记。  
- 🖌️ 支持 CSS 滤镜与丰富排版：多行换行、文本度量、OpenType、可变字体、本地字体、字距行距。  
- ⚙️ 使用可配置 worker 池和原生线程异步渲染/文件 I/O，可在 Linux、Serverless 平台运行。  
- 📦 安装简单：`npm install skia-canvas`，详细配置见 Getting Started 和 API 文档。  
- 🧪 示例涵盖生成图片、多页序列、窗口动画、宽色域、Sharp.js 集成等场景。  
- 🚀 基准测试中性能领先：Path2D 异步 6.7×、缩放旋转异步 33.5×、渐变异步 16.3×、SVG 转 PDF 异步 17×、文本异步 5.7×。  
- 🏁 还支持 PDF 转 PNG，原生 Rust/Hayro 异步可达 11×，且输出文件常更小。

---

### [发布 v4.0.0 · samizdatco/skia-canvas · GitHub](https://github.com/samizdatco/skia-canvas/releases/tag/v4.0.0)

**原文标题**: [Release v4.0.0 · samizdatco/skia-canvas · GitHub](https://github.com/samizdatco/skia-canvas/releases/tag/v4.0.0)

skia-canvas 发布 v4.0.0（samizdatco，10 月 12 日 18:10，提交 21b621d），核心亮点是更快离屏渲染、更稳定屏幕刷新、增强 PDF/SVG/排版/矢量/宽色域支持，并简化安装与依赖。

- 🚀 发布信息：仓库有 5 个 issue、2 个 PR，v4.0.0 为最新版本，完整变更见 v3.0.8...v4.0.0。
- ⚡ 渲染性能：专用 GPU 渲染线程减少 CPU↔GPU 往返与缓存重复，canvas/矢量内容缓存加速重复栅格化，原生内存回报 V8 以改善 GC。
- 🧹 显式释放：canvas 与 image 对象支持 using 关键字进行显式释放。
- 🖥️ 屏幕与事件：重绘绑定硬件 vblank 获得稳定帧率；Node/OS 事件循环协调，setTimeout/requestAnimationFrame 在动画与 UI 事件中继续运行；支持浏览器风格 pointer* 事件桥接鼠标和触摸。
- 🖼️ 图像与文档：原生 PDF 渲染为单页图像或多页文档；SVG 内嵌 `<style>` 被解析并生效；ImageData 支持 Float16；Sharp 集成支持全部 Skia 色彩空间与类型；PNG 导出通过 filters 更高效，默认 "none"。
- 🔤 排版：PDF 导出文本可选择/搜索；可变字体自动实例 wght、wdth、opsz，轴值与 OpenType 特性可手动配置；FontLibrary 可检测字体特性；抗锯齿、kerning、伪粗体/斜体合成可配置。
- ✏️ 矢量绘图：批量 drawlist 加速复杂路径并减少 Node→Rust 桥接；路径与轮廓可测量，长度偏移可计算位置/角度或用于切片；布尔运算兼容 canvas 默认 nonzero 绕线规则。
- 🎨 宽色域：颜色字符串支持完整 CSS 4 Color 规范；canvas 可按 Display P3 或 sRGB 创建，导出位图匹配色彩配置文件；渐变插值色彩空间可自定义；macOS 屏幕渲染默认 Display P3。
- 📦 安装简化：不再需要安装脚本或除 npm registry 外网络访问；仅 3 个第三方依赖，降低供应链风险。
- 📝 更多详情：详见 release notes 与完整变更日志。

---

### [](https://github.com/samizdatco/skia-canvas)

**原文标题**: [GitHub - samizdatco/skia-canvas: A uniquely capable, unusually fast <canvas> for Node.js · GitHub](https://github.com/samizdatco/skia-canvas)

Skia Canvas 是面向 Node.js 的无头矢量图形渲染器与屏幕窗口工具包，基于 Chrome 使用的 GPU 加速 Skia 引擎，让开发者无需浏览器即可使用熟悉的 Canvas API 在服务端或桌面渲染图像、动画与原生窗口。项目采用 MIT 许可，当前版本 4.0，GitHub 约 2.6k stars、106 forks。

- 🎨 **核心定位**：在不依赖浏览器的情况下，为 Node.js 提供类似 HTML `<canvas>` 的绘图能力。
- ⚙️ **底层引擎**：由 Skia 驱动，即 Google Chrome 使用的 GPU 加速图形引擎。
- 🖼️ **丰富输出**：支持 PDF、SVG 等矢量格式，以及 JPEG、PNG、WEBP、RAW 等位图格式。
- 💾 **多种保存方式**：可保存到文件、编码为 dataURL、返回 Buffer，或转为 Sharp 对象。
- 📄 **多页与文档处理**：支持多页画布、多页 PDF、图像序列，并可加载 PDF/SVG 作为可编辑画布。
- 🌈 **广色域与色彩**：支持 Display P3 广色域和 CSS Color 4 语法，渐变可选不同插值色彩空间。
- 🧩 **路径与变换**：支持 Path2D 切片、采样、布尔运算、轮廓/点分解，以及 3D 透视变换。
- ✍️ **排版能力**：支持多行换行文本、逐行度量、OpenType 特性、可变字体、本地字体和精细字距控制。
- 🎛️ **样式扩展**：可用矢量纹理、位图图案、自定义描边标记，并应用完整 CSS 滤镜。
- 🧵 **异步与多线程**：通过用户可配置的 worker pool 进行异步渲染和文件 I/O。
- ☁️ **部署场景**：可在标准 Linux 主机及 Vercel、Cloudflare Containers、AWS Lambda 等无服务器平台运行。
- 📦 **安装方式**：在支持平台上通常只需运行 `npm install skia-canvas`。
- 💻 **示例覆盖**：README 展示生成图像、多页序列、原生窗口渲染、广色域绘图及与 Sharp 集成等用法。
- 🏁 **性能表现**：基准测试中，skia-canvas 在 Path2D、缩放旋转、渐变、SVG 转 PDF、PDF 转 PNG、文本渲染等任务上通常显著快于 canvas、canvaskit-wasm、@napi-rs/canvas，异步模式更快。
- 🤝 **项目致谢**：受益于 Rust Skia 绑定、node-canvas 单元测试，以及多位贡献者在 SVG、Raw 图像、Vulkan、TypeScript 类型和滤镜路径修复方面的帮助。

---

### [](https://www.warpbuild.com/start?utm_source=cooperpress&utm_medium=newsletter&utm_campaign=h2-2026&utm_content=nodeweekly-2026-10-15)

**原文标题**: [Get Started with WarpBuild | $50 in Free Credits | WarpBuild](https://www.warpbuild.com/start?utm_source=cooperpress&utm_medium=newsletter&utm_campaign=h2-2026&utm_content=nodeweekly-2026-10-15)

overview summary
WarpBuild 为 AI 时代的 GitHub Actions 提供更快、更便宜的 CI runner：只需改一行 YAML，即可实现 2 倍速度、半价成本，覆盖 Linux/macOS/Windows 与 x86-64/ARM64，并提供 $50 免费额度和企业级/BYOC 支持。

- 🤖 AI 代理大量生成代码和提交，GitHub Actions 成为 CI 瓶颈；WarpBuild 旨在保持反馈循环快、账单低。
- ⚡ 只需一行 YAML：把 `runs-on: ubuntu-latest` 改为 `runs-on: warp-ubuntu-latest-x64-2x`，无需重写工作流。
- 💰 价格是 GitHub 托管 runner 的一半，构建更快，因此同时节省费率和运行时间。
- 🖥️ 支持 Linux、macOS、Windows，x86-64 和 ARM64，包括 M4 Pro Mac。
- 🍏 macOS 提供无限并发，Mac 任务无需在自己的队列中等待。
- 🚀 比 GitHub 托管 runner 快 2 倍、便宜 50%，缓存速度提升 3-10 倍。
- ☁️ 支持 WarpBuild 托管云和 BYOC，可部署在自有 AWS、GCP 或 Azure，含静态 IP 和自定义镜像。
- 🔐 企业就绪：SOC2 Type 2、临时隔离 VM、SSO、24x7 SLA 支持。
- 🎁 新用户可用促销码 `START50`，在 `Settings > Billing` 兑换 $50 免费额度，无需信用卡，2 分钟设置。
- 🧭 三步开始：注册 `app.warpbuild.com`、兑换 `START50`、修改 `runs-on` 一行。
- 🏢 客户包括 Braintrust、Raycast、OpenRouter、Comcast、Jane Street 等；案例显示构建从约 25 分钟降至约 9 分钟，macOS 从 30 分钟降至 8 分钟。
- ❓ 现有 GitHub Actions 工作流兼容，只需改 `runs-on` 标签，标准工具已预装。
- 📣 行动号召：停止等待 CI，Go Warp，预约演示并领取 $50 额度。

---

### [](https://www.youtube.com/playlist?list=PLHJJhUxJCR0c)

**原文标题**: [nodeconfeu 2026 - YouTube](https://www.youtube.com/playlist?list=PLHJJhUxJCR0c)

这段内容主要是 YouTube 页面底部的导航与信息链接，涵盖平台介绍、创作者/广告/开发者入口、政策条款、版权信息，并显示页面标题为“nodeconfeu 2026 - YouTube”。

- 🏢 关于、新闻、版权、联系我们：提供 YouTube 的基础信息与联络渠道。
- 🎬 创作者、广告、开发者：面向内容创作者、广告主和开发者的相关入口。
- 📜 条款、隐私、政策与安全：列出平台法律、隐私和安全政策链接。
- ⚙️ YouTube 运作方式、测试新功能：介绍平台机制并邀请用户体验新功能。
- ©️ 2026 Google LLC：显示版权归属为 Google。
- 📺 nodeconfeu 2026 - YouTube：页面或视频标题，指向 nodeconfeu 2026 的 YouTube 内容。

---

### [NodeConf EU 2026 | 意大利博洛尼亚](https://nodeconf.eu/)

**原文标题**: [NodeConf EU 2026 | Bologna, Italy](https://nodeconf.eu/)

NodeConf EU 将于 9 月 29-30 日在意大利博洛尼亚举行，是一场面向欧洲 Node.js 开发者、兼具技术深度与温暖社交氛围的聚会，包含两天演讲、交流与晚间活动。

- 🗓️ 时间：9 月 29-30 日；地点：意大利博洛尼亚。
- 🎟️ 门票开放预订，可锁定 2026 年席位，也可观看最新演讲发布与回放。
- 🏨 活动场地：Hotel Savoia Regency。
- 🧑‍💻 为期 2 天，包含演讲、hallway track、1 个场地，以及大量边聊与交流机会。
- 🍝 9 月 29 日晚举办社交晚宴，已包含在门票内，无需额外购买或单独通行证。
- ⚙️ 内容聚焦 Node.js 应用、运行时、工具链、可观测性、架构和生产系统。
- 🗣️ 日程为对话留出空间，鼓励会中认识同行、会后继续深入讨论。
- 🌍 社区齐聚：维护者、资深工程师、库作者和构建严肃 JavaScript 产品的团队。
- 🔗 重要链接一键可达：门票、场地详情、地图、YouTube、X、Bluesky、LinkedIn、Keet。
- 🤝 赞助与支持：Diamond Cloudflare；Platinum Platformatic；Gold Socket、nxtedition、Zephyr Cloud、Tether；Silver Igalia、Typesense、vlt；Supporting OpenJS Foundation、Sentry、Datadog、HeroDevs、Nearform；Community CityJS London、ZurichJS、BolognaJS、GrUSP。
- 💬 Keet 上有 NodeConf EU 点对点群组，可加入并连接社区。

---

### [](https://www.youtube.com/watch?v=rxUVWkBjXGI&list=PLHJJhUxJCR0c&index=15)

**原文标题**: [Paolo Insogna | FFI: Crossing the Native Boundary in Node.js - YouTube](https://www.youtube.com/watch?v=rxUVWkBjXGI&list=PLHJJhUxJCR0c&index=15)

这是一组 YouTube 页面底部的导航与法律信息链接，涵盖平台介绍、创作者与开发者资源、广告合作、政策条款、隐私安全及版权声明。

- 📄 关于：YouTube 平台介绍
- 📰 新闻：Press 媒体信息
- ©️ 版权：Copyright 相关说明
- 📬 联系我们：Contact us
- 🎬 创作者：Creators 资源入口
- 📈 广告：Advertise 广告合作
- 💻 开发者：Developers 开发者入口
- 📜 条款：Terms 使用条款
- 🔒 隐私：Privacy 隐私政策
- 🛡️ 政策与安全：Policy & Safety
- ⚙️ YouTube 运作方式：How YouTube works
- 🧪 测试新功能：Test new features
- © 2026 Google LLC：版权归属 Google LLC

---

### [Guy Bedford | 提升 Emscripten、WebAssembly 和 Rust 的能力 - YouTube](https://www.youtube.com/watch?v=nNlqco5xd20&list=PLHJJhUxJCR0c&index=23)

**原文标题**: [Guy Bedford | Improving the capabilities of Emscripten, WebAssembly and Rust - YouTube](https://www.youtube.com/watch?v=nNlqco5xd20&list=PLHJJhUxJCR0c&index=23)

本内容为 YouTube 网站底部导航与法律信息，涵盖平台介绍、创作者与开发者资源、广告合作、政策条款、功能测试入口，以及 Google LLC 的版权声明。

- 🏢 包含“关于”“新闻”“联系我们”等公司信息入口。
- 🎬 提供“创作者”和“开发者”相关资源入口。
- 📢 包含“广告”合作与商业推广入口。
- ⚖️ 列出“条款”“隐私”“政策与安全”等法律与政策链接。
- ⚙️ 提供“YouTube 如何运作”和“测试新功能”等说明与实验入口。
- ©️ 包含“版权”链接以及 © 2026 Google LLC 版权声明。

---

### [Caio Lima | V8 堆管理概述 - YouTube](https://www.youtube.com/watch?v=dYvGvWPcEYk&list=PLHJJhUxJCR0c&index=25)

**原文标题**: [Caio Lima | Overview of V8 heap management - YouTube](https://www.youtube.com/watch?v=dYvGvWPcEYk&list=PLHJJhUxJCR0c&index=25)

这份内容汇总了 YouTube 页脚的导航链接与版权信息，涵盖平台介绍、政策条款、合作入口、开发者资源及 2026 年版权声明。

- 📖 关于：平台介绍入口
- 📰 新闻：媒体与新闻信息
- ©️ 版权：版权相关说明
- 📞 联系我们：联系渠道
- 🎥 创作者：创作者资源入口
- 📈 广告：广告合作与投放
- 💻 开发者：开发者相关资源
- 📜 条款：服务条款
- 🔒 隐私：隐私政策
- 🛡️ 政策与安全：平台政策及安全信息
- ⚙️ YouTube 运作方式：平台机制说明
- 🧪 测试新功能：体验新功能入口
- © 2026 Google LLC：版权归属 Google LLC

---

### [](https://www.youtube.com/watch?v=bn78fDj2tWc&list=PLHJJhUxJCR0c&index=16)

**原文标题**: [Matteo Collina | Next-Gen Flame Graphs: Making Node.js Performance Profiling Actually Work - YouTube](https://www.youtube.com/watch?v=bn78fDj2tWc&list=PLHJJhUxJCR0c&index=16)

这是 YouTube 页面底部常见的信息与导航链接汇总，涵盖平台介绍、版权、联系、创作者/广告/开发者入口、条款与隐私、政策安全、功能说明及版权归属。

- 📘 关于：了解 YouTube 基本信息
- 📰 新闻：查看媒体报道与新闻
- ©️ 版权：版权相关信息
- ✉️ 联系我们：获取联系渠道
- 🎬 创作者：面向内容创作者的信息
- 📈 广告：广告投放与合作
- 💻 开发者：开发者相关资源
- 📜 条款：服务条款
- 🔐 隐私：隐私政策
- 🛡️ 政策与安全：平台政策与安全说明
- ⚙️ YouTube 运作方式：了解平台机制
- 🧪 测试新功能：体验实验性功能
- © 2026 Google LLC：版权归属声明

---

### [Deno 加入 Cloudflare | Deno](https://deno.com/blog/cloudflare)

**原文标题**: [Deno is joining Cloudflare | Deno](https://deno.com/blog/cloudflare)

2026年10月9日，Ryan Dahl 宣布 Deno 团队整体加入 Cloudflare，未来开发将聚焦 Cloudflare Workers 与 Durable Objects 共享平台，并公布 Deno runtime、Deno Deploy、JSR、rusty_v8 的过渡安排。

- 🚀 Deno 团队整体加入 Cloudflare，继续推进简化服务器软件构建的使命。
- 🧩 Deno 长期探索模块分发、运行时安全、完整工具链、独立可执行文件，以及兼容 Node.js 生态。
- 🌐 Ryan Dahl 的更大目标是让计算、存储和通信协同工作，而不是让每个应用自行拼装基础设施。
- ⚙️ Deno Deploy 让运行应用更简单，但也暴露底层复杂性；celld 基于 Cloudflare Workers 编程模型，让分布式应用从一开始就具备可扩展性。
- 🤝 从 Deno 到 Deno Deploy 再到 celld 的演进，促成了此次加入；Cloudflare 将联合 Workers 与 Durable Objects 团队，推动该编程模型成为构建服务器的默认方式。
- 📉 未来开发将投入这一共享平台，不再继续开发独立运行时和托管服务。
- 🛠️ Deno runtime 将继续支持一年，每月发布错误修复与安全更新；一年后停止开发，但仍保持开源，欢迎他人继续维护。
- ⏳ Deno Deploy 将继续运营六个月后关闭；付费客户迁移到 Cloudflare Workers 将获得支持。
- 📦 JSR 将继续运营，其基础设施将迁移到 Cloudflare。
- 🔧 将继续支持 rusty_v8，并推动其集成到 workerd。
- 🤖 AI 与智能体场景更需要更好抽象；Durable Objects 提供低成本无服务器执行、持久状态、WebSocket 和高级 JS 接口，因此 celld 聚焦 Durable Objects。
- ✍️ Kenton Varda 与 Ryan Dahl 在 Cloudflare 博客联合发文；若要在自有基础设施上大规模运行智能体，可联系 ry@cloudflare.com。

---

### [celld：自托管、分布式的 Durable Objects](https://celld.dev/)

**原文标题**: [celld: self-hosted, distributed Durable Objects](https://celld.dev/)

celld 是一个自托管、分布式的 Durable Objects 兼容运行时，让 Cloudflare 应用无需修改即可在自己的基础设施和存储桶上运行，并以远低于 Cloudflare Durable Objects 的成本实现持久化与故障转移。

- 🧩 **核心定位**：celld v0.6.2 beta 提供自托管、分布式的 Durable Objects 能力，你的 Cloudflare 应用（Workers、Durable Objects、KV、Queues、D1、R2、Workflows、Cron、静态资源）可原样运行。
- 🔐 **数据自主**：所有数据存放在你自己拥有的 S3 兼容存储桶中，节点共享该桶进行持久化存储。
- 💰 **成本优势**：规模越大成本越低，1 万个常驻单元时 Durable Objects 约 $41,500/月，而 celld 仅约 $195/月，便宜数百倍。
- ⚡ **性能表现**：无状态请求 p50/p99 为 0.2/0.3 毫秒，单工作线程吞吐约 94k req/s，休眠单元唤醒仅约 4 毫秒。
- 🛡️ **持久性保证**：每个单元一次只允许一个写入者（epoch 隔离），RPO=0，持久写入延迟约 90 毫秒，节点丢失后约 20 秒完成故障转移且零丢失。
- 📦 **轻量高密度**：常驻单元仅占 0.47 MB 内存，8 GB 节点可承载 2,500 个单元，每个常驻单元月成本约 $0.02。
- 🚀 **安装简易**：提供 58 MB 静态可执行文件，一条 curl 命令或 Docker 容器即可运行；可让 AI agent 直接创建分布式应用。
- 🧱 **兼容性广泛**：支持 Workers、Durable Objects/Facets、KV、Queues、D1、R2、Workflows、Cron、静态资源、动态 Workers，Containers 为实验性支持。
- 🗂️ **统一状态模型**：KV、D1、队列、Workflow 均以单元形式存在，拥有与 Durable Object 相同的租约、SQLite、LTX 复制和故障转移机制。
- 🛠️ **部署透明**：`celld deploy` 读取现有 `wrangler.json`，遇到未知键会停止而非忽略；R2 绑定直接读写你的存储桶。
- 🌐 **无需共识协议**：节点通过条件存储桶写入来分配单元所有权，整个集群不需要成员协议、故障检测器或共识服务。
- 🧯 **自托管带来的改变**：单元可在节点故障后从存储桶恢复；故障域由你选择；可通过 SQLite、LTX 文件和日志自行排查问题。
- ⚠️ **可靠性提醒**：Orange Cloud Report 将 Durable Objects 可靠性评为 2/10，称其“技术上令人印象深刻，运营上令人恐惧”；自托管让你掌控节点与运维，但不保证可靠性。
- 💡 **技术本质**：celld = V8 + SQLite + LTX（Litestream 的复制格式，来自 Ben Johnson），是对 Kenton Varda 与 Cloudflare Workers 团队 Durable Objects 理念的致敬。
- 📜 **开源许可**：Apache-2.0 许可证，由 Deno Land Inc. 开发。

---

### [](https://nodejs.org/en/blog/release/v26.12.0)

**原文标题**: [Node.js — Node.js 26.12.0 (Current)](https://nodejs.org/en/blog/release/v26.12.0)

概述摘要
- 📦 Node.js 26.12.0（Current）于 2026-10-14 发布，发布者为 Richard Lau。
- 🚨 两项 SEMVER-MINOR 变更：缺少 WebAssembly 或 RX 支持时抛错；HTTP 新增 `websocketMask()` 与 `websocketUnmask()`。
- 🧪 更新覆盖 benchmark、build、crypto、deps、doc、fs、http、http2、module、permission、process、quic、sqlite、src、stream、test_runner、tools、vfs、watch 等模块。
- 🔐 crypto 改进：移除多种密钥锁、隔离 EC PKCS8 编码、移除部分 Web Crypto 警告、按 Environment 保持根证书存储。
- 🌊 stream/iter 增强：新增 `dump()`/`dumpSync()`、`pipeToSync()` 选项，改进错误处理、背压与预算行为。
- 🗄️ sqlite 更新：验证 `aggregate()` 名称和选项、持久化 `enableDefensive()`、超长字符串改为抛错。
- 🔄 HTTP/QUIC 修复：校验会话关闭错误码、无效 promise 体销毁流、优化 HTTP 原始头分配、加速 HTTP/2 `getHeaders`。
- 🧰 依赖与工具更新：googletest、acorn 8.19.0、sqlite 3.54.0、simdjson 5.0.3，以及 V8 cherry-pick。
- 📚 文档更新：权限模型、测试运行器诊断通道、stream/iter 行为、HTTP Agent、`keepAliveTimeoutBuffer`、Linux musl 工具链等。
- 💻 提供 Windows、macOS、Linux、AIX、ARMv8 等安装包、二进制和源码下载链接。
- 🔑 发布附带 SHASUMS 与 PGP 签名，可用于校验文件完整性。

---

### [](https://nodejs.org/docs/v26.12.0/api/cli.html#--config-filepath---config-file)

**原文标题**: [Command-line API | Node.js v26.12.0 Documentation](https://nodejs.org/docs/v26.12.0/api/cli.html#--config-filepath---config-file)

本文档是 Node.js v26.12.0 命令行 API 参考，介绍 CLI 选项、程序入口解析、权限模型、测试与基准运行、性能诊断、快照与可执行应用、环境变量及常用 V8 选项等核心内容。

- 🧭 基本用法：`node [options] [V8 options] [入口 | -e "script" | -] [--] [参数]`；无参数进入 REPL；`node inspect` 用于调试；`node --v8-options` 查看 V8 选项。
- 📁 程序入口点：入口按当前工作目录解析，通常按 `require()` 加载；若使用 `--import`、`.mjs/.mts/.wasm` 或最近 `package.json` 中 `"type":"module"`，则按 `import()` 加载。
- ⚙️ 选项规则：选项支持 `-` 或 `_`；重复的单值选项以最后一个为准；命令行选项优先于 `NODE_OPTIONS`。
- 🔐 权限模型：`--permission` 可限制文件系统、网络、子进程、Worker、WASI、Addons、FFI、OpenSSL STORE、Inspector 等；需配合 `--allow-fs-read`、`--allow-net`、`--allow-child-process`、`--allow-worker` 等放行。
- 🧪 测试运行器：`--test` 支持并发、隔离、名称过滤、跳过、超时、随机顺序、失败重跑、分片、覆盖率阈值、快照更新等。
- 📊 基准测试：实验性 `--experimental-bench` / `--bench` 支持基准文件、隔离模式、报告器、样本数、预热次数等。
- 🧵 进程监控与调试：`--watch` / `--watch-path` 监视重启；`--inspect*` 启用调试；`--cpu-prof`、`--heap-prof`、`--heapsnapshot-*`、诊断报告等用于性能与故障分析。
- 📦 快照与单文件应用：`--build-snapshot`、`--snapshot-blob`、`--build-sea`、`--experimental-sea-config` 支持生成快照和单可执行应用。
- 🌐 网络与安全：TLS/SSL 选项、`--use-system-ca`、`--use-openssl-ca`、`--use-bundled-ca`、FIPS 模式、`--use-env-proxy` 等影响证书与代理行为。
- 🧩 模块与语言特性：支持 CommonJS/ESM、TypeScript 类型剥离、`--import`、`--require`、`--input-type`、条件导出、包映射、VFS、WASI、Web Worker 等实验特性。
- 🧪 环境变量：`FORCE_COLOR`、`NODE_OPTIONS`、`NODE_PATH`、`NODE_V8_COVERAGE`、`NODE_EXTRA_CA_CERTS`、`NODE_TLS_REJECT_UNAUTHORIZED`、`UV_THREADPOOL_SIZE` 等可影响 Node.js 运行。
- 🧠 常用 V8 选项：如 `--max-old-space-size`、`--max-semi-space-size`、`--stack-trace-limit`、`--expose-gc`、`--jitless`、`--abort-on-uncaught-exception` 等。

---

### [Node.js — Node.js 24.](https://nodejs.org/en/blog/release/v24.22.0)

**原文标题**: [Node.js — Node.js 24.22.0 (LTS)](https://nodejs.org/en/blog/release/v24.22.0)

Node.js 24.22.0 是 2026-10-14 发布的 LTS 版本，代号 'Krypton'，由 @richardlau 发布、@aduh95 准备；本版带来多项 semver-minor 新功能，重点覆盖 crypto、net、perf_hooks、sqlite、util，并包含大量修复、文档、构建、依赖、测试与工具链更新。

- 🔐 crypto 新增 `crypto.parsePKCS12()`、通用 MAC API，并支持从 OpenSSL providers 发现 cipher/hash。
- 🧩 crypto 的 Cipher/Decipher API 启用 SIV 与 GCM-SIV 模式，同时改进 WebCrypto、JWK、EC/RSA、FIPS 等行为。
- 🌐 net 支持将 `net.BoundSocket` 发送到线程和子进程。
- 📊 perf_hooks 新增 `SlidingWindowHistogram`、Histogram `meanCI`、qrde 分析及 CBOR 导入导出。
- 🗄️ sqlite 新增 `StatementSync.prototype.close()` 与 `StatementSync.prototype[Symbol.dispose]()`。
- 🛠️ util 新增 `util.markPromiseAsHandled`、`util.throttle` 和 `util.debounce`。
- 🧪 修复与改进覆盖 assert、buffer、child_process、fs、http/http2、https、stream、tls、quic、sqlite、src、test_runner、url、zlib 等模块。
- 📦 依赖更新包括 V8 backport、googletest、simdjson、zlib、npm 11.19.1 等。
- 📝 文档更新涵盖 API 参考、权限模型、安全流程、贡献者指南、REPL、TLS、socket、sqlite 等。
- 🏗️ 构建系统调整包括 GN/V8 sandbox、riscv64 默认参数、OpenSSL 警告抑制等。
- 🧰 工具链与元数据更新包括 CodeQL、actions、eslint、贡献者自动化、提交信息校验等。
- 🖥️ 提供 Windows、macOS、Linux、AIX、ARMv8 安装包或二进制、源码包、文档与 SHA256/PGP 校验文件。
- ⏭️ 下一版本为 Node.js 26.12.0 (Current)。

---

### [](https://nodejs.org/docs/v24.22.0/api/util.html#utilthrottlefn-limit-interval-options)

**原文标题**: [Util | Node.js v24.22.0 Documentation](https://nodejs.org/docs/v24.22.0/api/util.html#utilthrottlefn-limit-interval-options)

node:util 是 Node.js v24.22.0 的核心工具模块，状态稳定，可通过 `import util from 'node:util'` 或 `require('node:util')` 使用，主要服务 Node.js 内部 API，也适合应用与模块开发者。

- 🧰 提供异步与回调转换：`callbackify` 把 async/Promise 函数转为 error-first 回调；`promisify` 把回调函数 Promise 化，并支持 `util.promisify.custom`。
- 🪵 调试与弃用：`debuglog`/`util.debug` 按 `NODE_DEBUG` 条件输出日志；`deprecate` 包装废弃 API 并发出 `DeprecationWarning`，支持 code 去重及多种命令行标志。
- ⏱️ 流控工具：`debounce` 在静默期后执行；`throttle` 限制每个 interval 的调用次数，支持队列/丢弃、并发限制、`AbortSignal`、`cancel`、`flush`、`ref`、`unref`。
- 🔍 对象检查与格式化：`util.inspect` 支持 depth、colors、showHidden、compact、sorted、getters、maxArrayLength、numericSeparator 等选项，并可用 `inspect.custom` 自定义；`format`/`formatWithOptions` 提供 printf 风格占位符。
- 🧮 比较与差异：`diff` 用 Myers 算法返回最小差异；`isDeepStrictEqual` 进行深度严格相等，可选跳过原型比较；`markPromiseAsHandled` 可忽略未处理拒绝。
- 🧭 解析工具：`parseArgs` 解析命令行参数，支持 options、strict、allowNegative、tokens；`parseEnv` 解析 `.env` 内容。
- 📨 MIME 工具：`MIMEType`/`MIMEParams` 解析和读写 MIME 类型、子类型、essence、参数，并支持 `toString`/JSON 序列化。
- 🔤 编码与文本：`TextEncoder`/`TextDecoder` 实现 WHATWG 编码 API；`toUSVString` 替换代理项；`stripVTControlCharacters` 去除 ANSI 转义；`styleText` 用于终端着色。
- 🧩 类型检查：`util.types` 提供 ArrayBuffer、TypedArray、Map、Set、Promise、Proxy、Date、RegExp、CryptoKey、KeyObject 等内置对象检查。
- 🧯 系统与进程辅助：`convertProcessSignalToExitCode` 转换信号退出码；`getSystemErrorName`/`getSystemErrorMap`/`getSystemErrorMessage` 查询系统错误；`getCallSites` 获取调用栈；`setTraceSigInt` 控制 SIGINT 栈追踪；`transferableAbortController`/`transferableAbortSignal` 与 `aborted` 处理中止。
- 🚫 废弃 API：`util._extend` 改用 `Object.assign`；`util.isArray` 改用 `Array.isArray`；`util.types.isNativeError` 自 v24.2.0 废弃，建议 `Error.isError`（需权衡性能）；`util.inherits` 为旧式继承，不推荐，改用 `class`/`extends`。

---

### [Util | Node.js v24.22.0 文档](https://nodejs.org/docs/v24.22.0/api/util.html#utildebouncefn-wait-options)

**原文标题**: [Util | Node.js v24.22.0 Documentation](https://nodejs.org/docs/v24.22.0/api/util.html#utildebouncefn-wait-options)

这是 Node.js v24.22.0 官方文档中 `node:util` 模块的 API 参考，稳定性为 2，内容覆盖 Node.js 内部、应用与模块开发者常用工具，包括异步转换、调试日志、弃用警告、防抖节流、差异比较、格式化、对象检查、MIME/命令行/环境变量解析、编码器、类型判断及弃用 API。

- 🧰 `node:util` 支持 Node.js 内部 API，也对应用和模块开发有用，可通过 `require('node:util')` 或 ESM 导入。
- 🔁 `util.callbackify()` 将 async/Promise 函数转成 error-first 回调；Promise 以 falsy 值拒绝时会包装为带 `reason` 的 Error。
- 📈 `util.convertProcessSignalToExitCode()` 将信号名转成 POSIX 退出码，按 `128 + 信号编号` 计算。
- 🐞 `util.debuglog()`/`util.debug()` 依据 `NODE_DEBUG` 条件输出到 stderr，支持通配符、多个 section 和 `.enabled`。
- ⚠️ `util.deprecate()` 包装过时函数，首次调用发出 DeprecationWarning；可用 code 去重，并受 `--no-deprecation`、`--trace-deprecation`、`--throw-deprecation` 等影响。
- ⏱️ v24.22.0 新增 `util.debounce()` 与 `util.throttle()`，支持 Promise、AbortSignal、队列/丢弃、限流/并发、cancel/flush/ref/unref。
- 🔍 `util.diff()` 用 Myers 算法比较字符串/数组，返回 `-1/0/1` 差异条目；`util.isDeepStrictEqual()` 支持 `skipPrototype`。
- 🖨️ `util.format()`/`formatWithOptions()` 提供 printf 风格格式化，支持 `%s`、`%d`、`%i`、`%f`、`%j`、`%o`、`%O`、`%c`、`%%`。
- 📚 `util.inspect()` 输出调试字符串，可配置 `depth`、`colors`、`showHidden`、`compact`、`sorted`、`getters`、`maxArrayLength` 等，并支持 `util.inspect.custom` 自定义检查。
- 🌐 `util.MIMEType` 与 `util.MIMEParams` 解析和操作 MIME 类型、子类型、参数，符合浏览器约定，支持 JSON 序列化。
- 🧩 `util.parseArgs()` 解析命令行参数，支持 short、default、multiple、strict、allowPositionals、allowNegative、tokens；`util.parseEnv()` 解析 `.env`。
- 🔄 `util.promisify()` 将 error-first 回调函数转为 Promise，可通过 `util.promisify.custom` 覆盖，注意类方法需处理 `this`。
- 🎨 `util.stripVTControlCharacters()` 去除 ANSI 转义码；`util.styleText()` 应用终端样式，支持颜色名、修饰符、十六进制颜色及 NO_COLOR/FORCE_COLOR。
- 🧵 `util.TextDecoder`/`TextEncoder` 实现 WHATWG 编码 API；TextDecoder 支持多编码和 fatal/ignoreBOM，TextEncoder 仅支持 UTF-8。
- ✅ `util.types` 提供内置对象类型检查（ArrayBuffer、Map、Set、Promise、Proxy、TypedArray、CryptoKey/KeyObject 等）；`getCallSites()`、`getSystemError*()`、`aborted()`、`transferableAbort*()` 等也归入 Util。
- 🗑️ 弃用 API：`util._extend()` 改用 `Object.assign()`；`util.isArray()` 改用 `Array.isArray()`；`util.types.isNativeError()` 建议改用 `Error.isError()`。

---

### [](https://nodejs.org/en/blog/vulnerability/october-2026-security-releases)

**原文标题**: [Node.js — Wednesday, October 21, 2026 Security Releases](https://nodejs.org/en/blog/vulnerability/october-2026-security-releases)

Node.js 项目计划于 2026 年 10 月 21 日（周三）或之后不久，为 26.x、24.x、22.x 发布新版本，以修复安全漏洞；三条版本线中的最高严重级别均为 HIGH。

- 📅 **发布时间**：2026 年 10 月 21 日（周三）或之后不久。
- 🧩 **受影响版本线**：26.x、24.x、22.x。
- ⚠️ **最高严重性**：三条版本线均为 HIGH。
- 🛑 **EOL 提醒**：生命周期结束版本在安全发布发生时始终受影响，请使用受支持的最新版本。
- 🔐 **安全政策**：https://nodejs.org/en/security/
- 🐛 **漏洞报告**：请遵循 https://github.com/nodejs/node/blob/master/SECURITY.md 中的流程。
- 📬 **安全通知**：可订阅 nodejs-sec 邮件列表：https://groups.google.com/forum/#!forum/nodejs-sec
- 🤝 **商业支持**：Maintenance LTS 之后版本的商业支持可通过 OpenJS Ecosystem Sustainability Program 合作伙伴获取。
- ⏭️ **下一次发布**：页面列出下一次安全发布为 2026 年 7 月 29 日（周三）。

---

### [](https://aws.amazon.com/blogs/compute/exploring-aws-lambda-web-functions-for-building-web-applications/)

**原文标题**: [Exploring AWS Lambda Web Functions for building web applications | AWS Compute Blog](https://aws.amazon.com/blogs/compute/exploring-aws-lambda-web-functions-for-building-web-applications/)

AWS Lambda 现在支持 Web Functions，让你可以直接运行标准 Node.js Web 服务器，无需适配层，一条命令即可部署并获得带 HTTPS 的公共端点。

- 🚀 **新功能发布**：Lambda Web Functions 是一种新型 Lambda 函数，支持运行标准 Node.js Web 服务器，无需适配层，也无需管理服务器或负载均衡器。
- 🧩 **三大核心资源**：Web Function（顶层资源）、Revision（不可变的代码与配置快照，支持回滚）、Endpoint（带唯一 HTTPS 域名的网络入口，含认证类型与流量路由规则）。
- ⚙️ **运行环境**：启动时基于 Node.js 24 和 Arm64，每个执行环境配备 2 vCPU 和 2 GB 内存，并支持 Amazon VPC 连接。
- 🖥️ **框架兼容**：Express、Fastify、Hono 等 Node.js 框架无需适配器即可运行，Next.js 独立模式仅需少量配置。
- 📊 **示例应用**：一个通过服务器发送事件（SSE）向浏览器流式传输实时服务器指标的 Node.js HTTP 服务器仪表板。
- 💰 **活动 CPU 计费**：按请求、内存和实际消耗的 CPU 时间计费，等待数据库、下游 API 或 AI 推理时 CPU 消耗低，成本更省。
- 🔄 **并发与扩展**：每个执行环境可同时处理多个请求（默认最多 64，可调至 128），Lambda 根据流量自动增减环境。
- 🛡️ **限流保护**：可通过 maxEnvironments 和 rateLimit 限制环境数量与每秒请求数，保护下游依赖，超限返回 HTTP 429 且不排队。
- 🌍 **多区域部署**：可创建 MultiRegion 端点，Lambda 将代码复制到各区域，并通过 Amazon Route 53 延迟路由将请求发送至最低延迟区域。
- 🔐 **认证方式**：支持 ApplicationManaged（公开端点，自行处理认证）和 IamAuth（使用 SigV4/SigV4a 验证请求）。
- ☁️ **CloudFront 集成**：可将 Amazon CloudFront 置于端点前，实现自定义域名、边缘缓存和 AWS WAF，配合 IamAuth 与源访问控制防止绕过。
- 🤖 **代理构建**：由于部署只需一条命令且代码是普通 HTTP 服务器，可使用 AWS 编码代理工具包从提示词直接构建和部署应用。
- 🧹 **清理与延伸**：提供清理资源指引；更多示例可参考 Serverless Patterns 集合与 Lambda Web Functions 文档。

---

### [](https://aws.amazon.com/blogs/aws/announcing-aws-lambda-web-functions-for-fast-consistent-web-app-performance-anywhere/)

**原文标题**: [Announcing AWS Lambda Web Functions | AWS News Blog](https://aws.amazon.com/blogs/aws/announcing-aws-lambda-web-functions-for-fast-consistent-web-app-performance-anywhere/)

overview summary
- 🚀 AWS 发布 AWS Lambda Web Functions，一种新的 Lambda 形态，可直接运行标准 HTTP Web 应用，无需改写成事件处理器。
- 🧩 支持 Express、Hono、Fastify、Next.js 等 Node.js 框架，单命令部署，Lambda 自动处理扩缩容、多区域分发和活跃 CPU 计费，无适配器、无基础设施管理、无框架锁定。
- 🧱 Lambda 现有三种形态：Event Functions 为事件驱动、单并发、墙钟计费；Web Functions 为 HTTP 原生、多并发、活跃 CPU 计费；MicroVMs 为隔离有状态沙盒，适合运行不可信或用户生成代码。
- 🔗 三者可互补，同一 AWS 账户可共享运维模型，例如 Event Functions 做异步后端、Web Functions 做用户 API 与 SSR、MicroVMs 做交互式代码执行。
- 🌐 Web Functions 每个执行环境最多处理 128 个并发请求，突发流量可共享热环境，适合全球低延迟 Web、API 后端和交互式 HTTP 负载。
- 💰 CPU 按代码实际使用计费，等待数据库或 API 时消耗较少；内存按执行环境存在时间计费，可降低 SSR、API、AI 流式推理等 I/O 密集负载成本。
- 💻 Express.js 示例无需 Lambda 专用适配器，只需读取 AWS_LAMBDA_HTTP_ENDPOINT 提供的 host/port 并监听。
- 📦 部署命令为 `aws lambda-web deploy --name my-web-app --code ./my-app`，可在一分钟内返回实时 HTTPS URL。
- 🔁 Revision 是代码的不可变快照，endpoint 是 HTTPS URL，可将流量路由到某 revision 或在 revision 间分割。
- 🌍 多区域部署可用 `--regions us-east-1,eu-west-1,ap-northeast-1`，自动复制代码并配置延迟路由，通过全球 URL 将请求路由到最低延迟区域。
- 🐤 生产环境可通过 API 设置 revision 权重，例如 90% 当前版本、10% 新版本，实现金丝雀发布。
- ☁️ 可与 Amazon CloudFront 配合：Web Function endpoint 作为源，静态内容走缓存，动态请求转到 Web Function；OAC 可附加到 endpoint，仅允许指定 CloudFront 分发调用。
- 📍 已在 US East (N. Virginia)、US East (Ohio)、US West (Oregon)、Asia Pacific (Tokyo)、Europe (Ireland) 推出；启动时运行 Node.js 24 (nodejs24.x) on Arm64，并支持 VPC 连接。
- 🛠️ 入门命令为 `aws lambda-web deploy --name hello-world --hello-world`；更多信息见 AWS Lambda 定价页和 Lambda Web Functions 文档。

---

### [获取失败](https://lemire.me/blog/2026/10/10/websocket-servers-in-javascript-node-js-bun-and-deno-in-2026/)

**原文标题**: [Failed to retrieve](https://lemire.me/blog/2026/10/10/websocket-servers-in-javascript-node-js-bun-and-deno-in-2026/)

无法总结：获取内容失败，状态码 202。

---

### [](https://clickhouse.com/campaigns/clickhouse-managed-postgres?utm_source=nodeweekly&utm_medium=sponsored-content&utm_campaign=2026-10-15_SponsoredLink_Clickhouse)

**原文标题**: [ClickHouse Managed Postgres | ClickHouse](https://clickhouse.com/campaigns/clickhouse-managed-postgres?utm_source=nodeweekly&utm_medium=sponsored-content&utm_campaign=2026-10-15_SponsoredLink_Clickhouse)

ClickHouse Managed Postgres 是一款快速、可扩展、企业级且原生集成 ClickHouse 的托管 Postgres 服务，面向实时与 AI 驱动应用；它将 Postgres 事务处理与 ClickHouse 分析能力统一为低复杂度的数据栈，已在 AWS 可用、GCP 私密预览，并提供 30 天免费试用与 300 美元额度。

- 🚀 核心定位：快速、可扩展、企业级 Postgres，原生集成 ClickHouse，适合实时和 AI 应用。
- 🧩 统一数据栈：用 Postgres 处理事务、ClickHouse 处理分析，减少额外复杂度。
- ☁️ 可用平台：AWS 已可用，GCP 处于 Private Preview。
- 🎁 免费试用：30 天试用、300 美元额度，可创建免费账户，或使用 Google、Microsoft 登录。
- ⚡ NVMe 性能：企业级 Postgres 运行在本地 NVMe 上，I/O 密集场景最高快 10 倍，避免 EBS 限流和网络抖动。
- 🔗 ClickHouse 集成：支持 Postgres 到 ClickHouse 的原生 CDC、快速复制，以及 pg_clickhouse 统一查询。
- 🛡️ 企业级能力：高可用、自动备份、时间点恢复、端到端加密、私有网络，基础设施由 Ubicloud 驱动。
- 🔓 开源优先：基于 Postgres、ClickHouse、PeerDB、pg_clickhouse 等开源栈，无厂商锁定，数据可控。
- 💾 OLTP 性能：NVMe 支持微秒级延迟与数百万 IOPS，优于传统 SSD，并加速 VACUUM、检查点和逻辑复制。
- ❤️ 高可用设计：最多两个专用 standby 实例用于 HA，读副本单独提供；支持自动备份、PITR 与 WAL 归档。
- ⏱️ 极速复制：Postgres 数据实时复制到 ClickHouse，分析最高快 100 倍，复制延迟可低至数秒，支持初始快照与 CDC 增量更新。
- 🔎 统一查询层：通过 pg_clickhouse 直接从 Postgres 查询 ClickHouse，无需代理；支持下推连接、过滤、聚合和函数，14/22 个 TPC-H 查询完全下推，带来 60 倍以上加速。
- 💬 客户反馈：用户已运行约 8.5 TB 热数据，从 Aurora/RDS 迁移多 TB 工作负载，认可性能、可靠性与性价比。
- 🚀 下一步：更多原生 CDC 能力，包括亚秒级复制延迟、可靠 slot flushing 等，将专属于 ClickHouse Managed Postgres。

---

### [](https://trigger.dev/blog/zod-4-got-rid-of-a-bunch-of-cpus-for-us)

**原文标题**: [Zod 4 got rid of a bunch of CPUs for us | Trigger.dev](https://trigger.dev/blog/zod-4-got-rid-of-a-bunch-of-cpus-for-us)

Trigger.dev 从 Zod 3.x 升级到 Zod 4.5 后，核心 worker CPU 需求下降近三分之一，批处理吞吐提升 14%，任务触发 p99 降低 18%；同时成为 Zod 首个白金赞助商。升级整体顺利，但曾因 core 包中混入裸 `zod` 导入，影响部分仍在用 Zod v3 + npm 的用户，后已修复并加入 oxlint 检查防止复发。

- ⚡ 从 Zod 3.x 升级到 Zod 4.5，主要服务 CPU 需求下降近三分之一。
- 🚀 批处理吞吐量提升 14%，任务触发 p99 降低 18%。
- 🏆 Trigger.dev 成为 Zod 首个白金赞助商，支持 Colin 的工作并回馈开源。
- 🧩 Zod 被大量用于解析任务负载、批处理项、队列消息、重试包装器等 JSON 和 schema。
- 📊 某 worker 服务约每秒 1,100 次解析、每天近 1 亿次；每个作业至少一次 `safeParse`，约一半作业还会解析每条消息。
- 🧵 升级改善了 Event Loop Utilisation（ELU）：热路径解析更少、主循环阻塞更少、增长余量更大。
- 🧪 schema compilation 实验用于简单服务端 schema，额外降低约 5% worker CPU 和 ELU。
- 🛠️ 升级几乎无痛，但 core 包中曾误用裸 `zod` 导入，而不是显式 `zod/v4`。
- ⚠️ 这导致已升级、仍用 Zod v3 且使用 npm 的用户出现任务运行 warm start 延迟。
- ✅ 团队在里斯本 offsite 修复问题，并增加 oxlint 检查防止再次发生。

---

### [](https://www.thenodebook.com/blog/fast-nodejs-doing-less)

**原文标题**: [Fast Node.js is mostly about doing less](https://www.thenodebook.com/blog/fast-nodejs-doing-less)

这篇文章详细记录了作者如何逐步优化一个 Node.js 链接预览（unfurl）功能，从最初简单的几行代码，到最终约 150 行的高效实现。整个过程围绕一个核心问题展开：“这段代码实际在做什么？”通过缓存、Promise 缓存、超时控制、只读取必要数据等策略，解决了重复请求、缓存踩踏、无限等待和资源浪费等真实场景中的性能问题，并强调了 SSRF 安全防护的重要性。

- 🚀 文章通过构建链接预览功能，演示 Node.js 性能优化的迭代过程。
- 🔍 初始版本使用 `fetch` 和 `cheerio` 提取 Open Graph 标签，简单但存在重复工作。
- 👥 在 300 人频道中，同一链接会被重复下载和解析 300 次，造成巨大浪费。
- 💾 引入 LRU 缓存，限制最大条目数和过期时间，并规范化 URL 以避免重复键。
- ⚡ 缓存 Promise 而非值，让并发请求共享同一个进行中的请求，解决缓存踩踏（stampede）。
- ⏱️ 添加 `AbortSignal.timeout` 超时，防止服务器挂起，并设置失败缓存避免反复请求。
- 📖 只读取 HTML 的 `<head>` 部分，检查 `Content-Type`，取消不需要的响应体，限制读取 512KB。
- 🧩 最终代码约 150 行，整合所有优化，事件循环保持畅通，内存可控。
- 🛡️ 必须防范 SSRF 攻击，拒绝私有和内部地址，并注意重定向可能绕过检查。
- 🤔 核心教训：问正确的问题，减少不必要的工作，而不是寻找更快的算法或库。

---

### [](https://brettcodes.com/the-disappointing-death-of-deno/)

**原文标题**: [The Disappointing Death of Deno: What Happened and the Perils of Venture Capital-Funded Open Source – Brett Codes](https://brettcodes.com/the-disappointing-death-of-deno/)

overview summary
文章讲述 Deno 公司被 Cloudflare 收购后，Deno 运行时进入一年维护模式、Deno Deploy 将于六个月后关闭；作者作为长期用户感到失望，并借此分析 JavaScript 运行时竞争、Bun 与 Node.js 的格局、风险投资驱动开源的问题，以及 AI 编程兴起如何改变 Deno 的命运。

- 🧩 2026年10月9日，Cloudflare 收购 Deno 公司；Deno 运行时进入维护模式，仅提供12个月月度安全补丁与漏洞修复，之后核心团队停止开发。
- ☁️ Deno Deploy 将在6个月后关闭，付费客户可迁移至 Cloudflare Workers；JSR 继续运营，但基础设施迁往 Cloudflare。
- 🏁 文章回顾 JavaScript 运行时之战：Node.js 自2009年起主导服务端，Ryan Dahl 创建 Node 后又推出 Deno，强调安全、简洁和开发体验。
- ⚙️ Deno 可直接运行 TypeScript，内置格式化、lint、标准库和工具链；作者曾将其用于个人项目，并在工作中小范围引入。
- 🥊 Bun 后来加入竞争，主打直接替代 Node.js，同时提供 TypeScript、SQLite、哈希等内置能力；Deno、Bun、Node.js 各有优劣。
- 📦 Deno v2 于2024年10月发布，重点转向 Node.js 兼容，支持 package.json 和 drop-in 替换；但作者认为这没有带来预期增长。
- 🏢 部分企业采用过 Deno，如 Slack SDK、Bunny.net、Netlify 等，因为其默认安全和无需构建步骤适合边缘脚本等场景。
- 💸 Deno 公司获得超过2600万美元风投，需要商业回报；Deno Deploy、JSR 等产品未能形成足够收入。
- 📉 2025年5月 Ryan Dahl 发文称 Deno“不是在收尾，而是在加速”，但文章认为2026年下半年缺乏重大进展。
- 🤖 LLM 与代理式编程兴起改变了竞争格局：Deno 的安全默认和内置工具本应适合 AI 编码，但 Bun 因被 Anthropic 收购而获得更强资金保障。
- 🧠 Claude Code 基于 Bun；Anthropic 于2025年12月收购 Bun 团队，使 Bun 的未来更稳定，也让 Deno 面临更大投资回报压力。
- 🚪 2026年3月，Deno 出现核心员工大规模离职，包括 Fresh 维护者等；没有正式说明，只有社交媒体上的告别。
- 🛡️ Deno 随后推出安全相关项目：Deno Sandbox、Claw Patrol，以及开源分布式对象模型 celld，试图抓住 AI 基础设施机会。
- 🤝 Cloudflare 的收购本质是 acquihire：Ryan Dahl 等人将加入 Cloudflare，主导 workerd 自托管和 Workers 编程模型，celld 是重要诱因。
- 🪦 文章批评 Deno 的收尾方式：仅一年维护、感谢信和 MIT 代码，不足以对依赖它的开发者、公司如 Bunny.net 和生态负责。
- 🌱 Fresh 框架被移出 Deno 官方组织，计划开放治理，但数月无后续；作者担心依赖 Fresh 和 Deno 的项目何去何从。
- 😞 作者不会再在新项目中使用 Deno，也不再向 JSR 发布包；他仍喜欢 Deno 的内置工具链，但无法接受这种不确定性。
- ⚠️ 核心教训是：避免风险投资资助的开源软件；VC 要求增长和退出，可能损害长期稳定、开放治理和社区利益。
- 🔮 未来仍不确定：Deno 可能被社区或公司 fork、建立基金会维护，也可能在12个月后真正终结；作者将把重要程序迁移到更稳定的方案。

---

### [TanStack Start 1.0 稳定版发布 | TanStack 博客](https://tanstack.com/blog/tanstack-start-1-0)

**原文标题**: [TanStack Start 1.0 is Stable | TanStack Blog](https://tanstack.com/blog/tanstack-start-1-0)

TanStack Start 1.0 正式发布稳定版，标志着这一全栈框架结束长期 RC 阶段，正式可用于生产环境。文章回顾了从类型安全路由器起步、坚持显式 API 设计、投入 RSC 与 AI 智能体适配，以及依靠社区、维护者与合作伙伴共同铸就这一框架的完整历程。

- 🎉 **正式稳定**：TanStack Start 1.0 发布，官方承诺 API 稳定，开发者可放心学习、使用并持续构建，无需担心应用架构被大幅改动。
- 🧭 **源于路由器**：项目起点是打造类型安全的路由器，让路由、参数、搜索参数、loader 数据与上下文都能被 TypeScript 精确追踪。
- 🛠️ **提供另一种选择**：在 Next.js 押注 RSC、React Router 与 Remix 转型之际，Start 保留 SPA 的开发体验，同时叠加服务端渲染、流式传输与服务器函数。
- ⚙️ **显式控制运行位置**：通过 `createIsomorphicFn` 与 `createServerFn` 等 API，让开发者清楚知道代码在服务端还是客户端运行，并能组合跨端中间件。
- 👥 **团队贡献巨大**：Manuel、Flo、Chris 等维护者推动了类型安全性能、SSR 优化（吞吐量提升约 5.5 倍）、编译器与回归测试等关键工作。
- 🌐 **框架无关与自由部署**：坚持框架无关理念，支持 Solid，采用 Vite 与 Nitro 分离部署，并额外支持 Rsbuild，避免维护大量部署适配器。
- 🧩 **RSC 的取舍**：投入大量时间将 RSC 集成进 Start 而不改变应用模型，但因复杂度与推理负担，最终在 tanstack.com 上停用。
- 🤖 **拥抱 AI 智能体**：2025 年底起 AI 深度改变开发方式，类型安全与显式 API 对智能体同样有益，并推出 TanStack Intent 将最佳实践注入 npm 包。
- 🤝 **伙伴与赞助支持**：Render、Lovable、Cloudflare、Netlify、Vercel、CodeRabbit、Sentry、Prisma、WorkOS、Clerk 等合作伙伴提供集成、示例与资金支持。
- 🚀 **邀请使用**：官方鼓励开发者尝试 1.0，可借助文档、迁移指南，甚至让 AI 智能体协助新项目或迁移工作。

---

### [](https://tanstack.com/start/latest/docs/framework/react/comparison)

**原文标题**: [Comparison | TanStack Start vs Next.js vs React Router | TanStack Start React Docs](https://tanstack.com/start/latest/docs/framework/react/comparison)

overview summary：该页是 TanStack Start 官方对比文档，以矩阵比较 TanStack Start、Next.js App Router 和 React Router Framework Mode 在渲染与数据、服务端 API 与表单、工具与部署、性能和选型上的差异，并强调性能需实测、类型推断不等于运行时验证或授权。
- 🧭 比较基准：2026-09-11 对照 TanStack Start 当前指南、Next.js 16.3 App Router、React Router 8.3 Framework Mode。
- 🖥️ 渲染：Start 默认 SSR + hydration，支持逐路由全 SSR、仅数据或禁用；Next 使用 Server/Client Components，RSC 为核心；React Router 可配置 SSR 并用路由级 client loader。
- 📦 SPA/静态：Start 有专用 SPA 模式；Next 有 ssr:false 和静态导出，但受服务器功能限制；React Router 可预渲染选定 URL。
- ⚛️ RSC：Start 为实验性 opt-in；Next App Router 将其作为核心模型；React Router 的 RSC 集成尚不稳定。
- 💾 数据缓存：Start 用 Router loader 缓存并集成 Query；Next 有导航/服务器缓存 API 与 ISR；React Router 用 loader/action 重验证，可另加客户端数据工具。
- 🔁 缓存提醒：客户端 loader 缓存、服务端结果缓存、HTML 缓存不同；需比较失效、持久化和多实例协调；CDN stale-while-revalidate 不等同跨供应商 ISR。
- 🛠️ 服务端调用：Start 使用类型化 server functions（GET/POST）；Next 使用 Server Actions；React Router 使用 route actions 与 fetchers。
- ✅ 验证与授权：三者都需运行时验证和服务端授权；类型推断不能替代验证或授权。Start 有 Validator API，Next/React Router 通常用应用代码或 schema。
- 🧩 中间件与表单：Start 有请求/函数中间件，可从事件处理器调用 server functions；Next 有 Proxy 拦截、next/form、Server Action 表单；React Router 有路由中间件、Form/actions/fetchers 与 resource routes。
- 🧰 工具链与部署：Start 基于 Vite/Rsbuild，支持路由和 server function 类型推断；Next 用 Turbopack，内置 Metadata、next/image、next/font；React Router 提供生成路由模块类型和部署模板。
- ⚠️ 部署检查：部署支持取决于适配器、运行时与所用功能；要核实流式渲染、图片处理、文件系统、后台任务和共享缓存。
- 📊 性能：页面不判定性能赢家；启动、HMR、内存、JS 体积、响应延迟需独立测量；应用相同代表应用并记录版本、硬件、依赖、路由数、缓存与冷热运行结果。
- 🧭 选型：Start 适合类型化路由上下文/URL 状态、显式 loader/server function、逐路由渲染控制；Next 适合 Server Component 模型和集成设施；React Router Framework Mode 适合 loader/action、fetcher、表单工作流和渐进增强。
- 📚 下一步：采用 Start 实验功能前查看 overview 与 Server Components 指南；试用可从 Getting Started 或 Migrate from Next.js 开始。

---

### [](https://imapkit.com/)

**原文标题**: [In-memory IMAP server for testing IMAP clients | ImapKit](https://imapkit.com/)

ImapKit 是一个嵌入测试套件的真实 IMAP 服务器，按 RFC 严格响应、支持 50+ 扩展，并可脚本化真实故障，帮助验证客户端而不依赖生产服务器。

- 🧪 严格设计：客户端若违反 RFC 会收到 `BAD` 或 `NO`，让客户端 bug 在测试中暴露，而不是等生产服务器发现。
- 🧩 50+ 扩展：支持 IMAP4rev1 和 IMAP4rev2，包括 IDLE、CONDSTORE、QRESYNC、NOTIFY、ACL、METADATA、QUOTA、SORT、THREAD、COMPRESS 等，可按服务器开启。
- 🎛️ 控制 API：用 `server.control` 添加消息、修改标志、重置 UIDVALIDITY、断开会话；已连接客户端能看到变化。
- ⚡ 脚本化故障：通过脚本规则和怪癖预设模拟真实服务器行为，如延迟响应、拆分输出、限流、自动登出和连接掉线。
- 👥 多会话：同一邮箱多个客户端时，按 RFC 2180 在允许的时机收到 EXISTS、EXPUNGE 和标志更新。
- 🌐 任意语言：通过 `imapkit` 命令、REST API 和服务器事件，可从 Python、Go 或任意测试套件驱动。
- 🚀 测试内真实 IMAP 服务器：与测试套件同进程，毫秒启动，不写磁盘；每个测试获得全新服务器和所需邮箱、消息、用户、扩展。
- 🔌 真实通信：客户端通过真实 socket 使用真实 IMAP，测试可改变底层服务器并检查客户端是否同步。
- 💻 示例流程：导入 imapkit，启用 IDLE/CONDSTORE/QRESYNC，启动服务器；用 `control.addMessage`、`resetUidValidity` 和 `script.add` 让 SELECT 返回 `NO [UNAVAILABLE]`，最后停止。
- 📨 生产集成：若需要生产邮件集成，EmailEngine 是 ImapKit/ImapFlow 团队的自托管邮件 API，将 Gmail、Microsoft 365 和 IMAP 账户转为 REST 端点，含托管 OAuth2 和收件 webhook。

---

### [发布 v5.3.0 · expressjs/express · GitHub](https://github.com/expressjs/express/releases/tag/v5.3.0)

**原文标题**: [Release v5.3.0 · expressjs/express · GitHub](https://github.com/expressjs/express/releases/tag/v5.3.0)

Express v5.3.0 已发布，重点修复 `res.send()` 的 HTTP 头冲突、多个依赖安全漏洞，并改进 QUERY 条件请求、内容类型处理、错误日志与性能，同时包含大量文档、测试、CI 和依赖更新。

- 🚀 v5.3.0 为最新版本，由 UlisesGascon 发布，包含自上一版本以来的 2 个提交。
- 🐞 修复 `res.send()` 中 `Content-Length` 与 `Transfer-Encoding` 冲突：仅在没有 `Transfer-Encoding` 时添加 `Content-Length`，ETag 生成不受影响。
- 🔒 将 `qs` 升级至 `^6.16.0`，修复 CVE-2026-2391、CVE-2026-82417、CVE-2026-82562，包括逗号解析中的 `arrayLimit` 绕过与 `isBuffer` 引发的 DoS。
- 🔒 将 `proxy-addr` 升级至 `^2.0.8`，修复 CVE-2026-90711。
- 🧩 允许 QUERY 请求条件重新验证，`req.fresh` 现在可对匹配验证器的 QUERY 请求返回 `304 Not Modified`。
- 🌐 改进 `res.redirect()` 的 HTML 响应结构，加入 `<!DOCTYPE html>`、`<title>` 和 `<body>`，提升浏览器兼容性。
- 🛠️ `app.render` 的 `options` 为 `null` 时能正确处理 `locals`，行为与省略 `options` 或传空对象一致。
- ⚡ 升级 `content-type` 至 `^2.0.0`，解析约快 1.5 倍；`res.send()` 保留已有 `Content-Type` 参数，解析失败不再抛错，`type-is` 同步升至 `^2.1.0`。
- 🧾 默认错误处理器改为记录完整错误对象，保留 `Error.cause` 与库特定属性，如 Sequelize 的 `parent`/`original`。
- 📎 升级 `content-disposition` 至 `^2.0.1`，`res.download()`、`res.attachment()`、`res.sendFile()` 对有效 HTTP token 文件名不再加引号，需注意精确头断言。
- 🛡️ 升级 `body-parser` 至 `^2.3.0`，修复 CVE-2026-12590：无效 `limit` 曾导致请求体大小限制被静默禁用，现在初始化即抛错。
- 🚀 性能优化：`res.send()` 发送字符串且未显式设置 `Content-Type` 时，避免重复处理 `Content-Type`。
- 👥 包含大量文档、测试、CI/依赖更新，并迎来多位新贡献者；完整变更见 `v5.2.1...v5.3.0`。

---

### [](https://www.bram.us/2026/10/08/caniname-cli-tool-to-check-project-name-availability/)

**原文标题**: [caniname: CLI tool to check project name availability across Netlify and NPM (and other sources) – Bram.us](https://www.bram.us/2026/10/08/caniname-cli-tool-to-check-project-name-availability/)

caniname 是一个 CLI 工具，用于在 Netlify 和 NPM（以及其他来源）上检查项目名称是否可用，由 Bramus 于 2026 年 10 月 8 日发布，旨在自动化命名时的可用性检查。

- 🧩 需求：为工具或自定义元素命名时，常需手动检查 NPM 包名和 Netlify 子域名是否被占用，过程重复且麻烦。
- ⚙️ 使用：无需全局安装，可直接运行 `npx caniname my-fancy-new-project`，也支持一次传入多个名称。
- ✅ 检查结果：对每个名称报告 Netlify 子域名和 NPM 包是否可用（✔）或已被占用（✖），占用时附上现有站点或包链接。
- 🤖 脚本/CI：支持 `--json`（或 `-j`）输出结构化 JSON；也可在 Node.js 中直接导入 `checkName` 和 `checkNames`。
- 🧱 扩展性：目前仅检查 Netlify 和 NPM，但每个检查独立放在 `src/checks/` 中并自动加载，欢迎 PR 添加更多服务。
- 😅 趣闻：作者最初叫它 `namecheck`，但发布前自测发现该名称在 Netlify 和 NPM 都已被占用，于是用这个工具找到了 `caniname`。
- 🔗 资源：可在网站/文档、GitHub 和 NPM 上访问 caniname。
- 🏷️ 标签：CLI、工具；作者 Bramus 是来自比利时的前端开发者，也在 Google 担任 Chrome DevRel 工程师。

---

### [GitHub - sindresorhus/fast-cli：使用 fast.com 测试](https://github.com/sindresorhus/fast-cli)

**原文标题**: [GitHub - sindresorhus/fast-cli: Test your download and upload speed using fast.com · GitHub](https://github.com/sindresorhus/fast-cli)

sindresorhus/fast-cli 是一个开源的 Node.js 命令行工具，使用 fast.com 测试网络下载和上传速度，支持简洁、单行、JSON 与详细诊断输出，仓库约 2.9k stars、123 forks、26 watchers，并采用 MIT 许可证。

- 🚀 项目定位：通过 fast.com 测试下载与上传速度的 CLI 工具，适合命令行环境。
- 📦 安装要求：需要 Node.js 22.12+，全局安装命令为 `npm install --global fast-cli`。
- 🌐 首次运行：底层使用 Puppeteer，若未安装 Chrome，首次运行会下载约 200 MB 的 Chrome，多数安装问题与此相关。
- ⚙️ 基本用法：支持 `fast`、`fast > file`，也可用 `fast --help` 查看帮助。
- 📤 上传测试：默认测下载速度，使用 `--upload` 或 `-u` 可同时测量上传速度。
- 🧾 输出选项：`--single-line` 减少间距并单行输出；`--json` 输出 JSON；`--verbose` 包含延迟、客户端位置和服务器位置等诊断信息。
- 📊 示例结果：`fast --upload > file` 可输出类似 `17 Mbps` 下载、`4.4 Mbps` 上传；详细模式可显示延迟、客户端和服务器位置。
- 🧩 JSON 字段：包含 `downloadSpeed`、`uploadSpeed`、单位、`downloaded`、`uploaded`、`latency`、`bufferBloat`、`userLocation`、`serverLocations`、`userIp`。
- 🔗 相关项目：`speed-test`，可使用 speedtest.net 测试网速和 ping。
- 🏷️ 仓库信息：公开仓库，主题包括 cli-app、command-line-tool、download-speed、nodejs、npm-package、speed-test。

---

### [GitHub - sindresorhus/p-queue：具有并发控制的 Promise 队列 · GitHub](https://github.com/sindresorhus/p-queue)

**原文标题**: [GitHub - sindresorhus/p-queue: Promise queue with concurrency control · GitHub](https://github.com/sindresorhus/p-queue)

p-queue 是一个基于 Promise 的队列库，用于控制异步或同步任务的并发，适合限流 REST API 调用、CPU/内存密集任务等场景；它零依赖、功能完整，采用 MIT 许可，当前约 4.3k stars、224 forks，由 Sindre Sorhus 和 Richie Bendall 维护。

- 📦 安装方式：`npm install p-queue`；该包为原生 ESM，不提供 CommonJS 导出。
- 🧠 核心能力：Promise 队列，支持并发限制、优先级、速率限制、超时、`AbortSignal` 取消、事件和零依赖。
- ⚙️ `PQueue(options?)` 返回一个队列实例，该实例也是 `EventTarget`。
- 🚦 `concurrency`：同一时间运行的最大任务数，默认 `Infinity`，最小为 1。
- ⏱ `timeout`：任务可运行的最长毫秒数，超时后任务 `signal` 中止，`.add()` 以 `TimeoutError` 拒绝；可全局设置或单任务覆盖。
- ▶️ `autoStart`：默认 `true`；若为 `false`，需调用 `.start()` 启动任务。
- 🧩 `queueClass`：可自定义队列类，需实现 `enqueue()`、`dequeue()`、`filter()`、`setPriority()`、`remove()` 和 `size`。
- 🚧 `intervalCap` / `interval`：限制每个时间区间内启动的任务数；`interval` 为 0 时禁用速率限制。
- 🔄 `carryoverIntervalCount`：控制上一区间仍在运行的任务是否计入下一区间的 `intervalCap`。
- 🪟 `strict`：启用滑动窗口限流，严格保证任意 `interval` 内启动数不超过 `intervalCap`，但资源开销更高。
- ➕ `.add(fn, options?)`：添加同步或异步任务，返回任务结果的 Promise；支持 `priority`、`id`、`timeout`、`signal`。
- 🧮 `.addAll(fns, options?)`：批量添加任务，按输入顺序返回所有结果。
- ⏸ `.pause()` / ▶️ `.start()`：暂停启动新任务 / 恢复运行排队任务。
- ⏳ `.onEmpty()`：队列为空时 resolve，但任务可能仍在运行。
- 💤 `.onIdle()`：队列为空且所有任务完成时 resolve。
- 🧵 `.onPendingZero()`：没有运行中任务时 resolve，忽略等待中的任务。
- 🚦 `.onRateLimit()` / `.onRateLimitCleared()`：等待进入或解除速率限制。
- ⚠️ `.onError()`：任务失败、超时或运行中中止时 reject；常与 `Promise.race([queue.onError(), queue.onIdle()])` 配合。
- 📉 `.onSizeLessThan(limit)`：等待排队任务数小于指定值，用于背压控制。
- 🧹 `.clear()`：移除所有等待任务；对应 `.add()` Promise 以 `AbortError` 拒绝，运行中的任务继续。
- 📊 状态属性：`.size`、`.sizeBy()`、`.pending`、`.timeout`、`.concurrency`、`.isPaused`、`.isRateLimited`、`.isSaturated`、`.runningTasks`。
- 🔧 `.setPriority(id, priority)`：修改等待任务的优先级；找不到 `id` 时抛出 `ReferenceError`。
- 📡 事件：`active`、`completed`、`error`、`empty`、`idle`、`pendingZero`、`add`、`next`、`rateLimit`、`rateLimitCleared`。
- 🧪 超时处理：`TimeoutError` 是 `DOMException`；任务需自行处理 `signal` 才能真正停止工作。
- 🧰 自定义队列：通过 `queueClass` 可实现 FIFO 等其他调度策略。
- ❓ 常见用例：背压、取消排队任务、按添加顺序获取结果、调试卡住任务、Jest fake timers 兼容技巧。
- 🔗 相关库：`p-limit`、`p-throttle`、`p-debounce`、`p-all`、`p-map`。
- 🧭 项目状态：功能已完整，欢迎 PR，但不计划更多开发，也不通过邮箱提供支持。
- 📄 许可与仓库：MIT 许可；约 4.3k stars、224 forks、18 watchers、231 commits。

---

### [发布 v10.0.0 · sindresorhus/p-queue · GitHub](https://github.com/sindresorhus/p-queue/releases/tag/v10.0.0)

**原文标题**: [Release v10.0.0 · sindresorhus/p-queue · GitHub](https://github.com/sindresorhus/p-queue/releases/tag/v10.0.0)

overview summary
p-queue v10.0.0 是一次重要的大版本升级，包含破坏性变更与大量修复：要求 Node.js 22，事件系统从 EventEmitter 迁移到 EventTarget，新增零依赖、异步上下文继承、超时中止信号等能力，并修复限流、事件、优先级和 TypeScript 类型等问题。

- ⚠️ 破坏性变更：要求 Node.js 22，队列改为 `EventTarget`，需使用 `addEventListener()` / `removeEventListener()` 替代 `on()` / `once()` / `off()`。
- 📨 `completed` 和 `error` 事件的结果或错误现在位于 `event.detail`；若值为 `undefined`，则 `event.detail` 为 `null`。
- 🚨 事件监听器中抛出的错误现在会导致进程退出，Node.js 会将其报告为未捕获异常。
- 🧹 `.clear()` 现在会用 `AbortError` 拒绝被移除任务的 Promise，而不是让它们永久挂起；由 `.addAll()` 或链式 `.then()` 产生的 Promise 也需要处理拒绝。
- ⏱️ `TimeoutError` 现在是名为 `TimeoutError` 的 `DOMException`，类似 `AbortSignal.timeout()` 的错误。
- 🚫 移除弃用的 `carryoverConcurrencyCount`，改用 `carryoverIntervalCount`；选项验证更严格，如 `concurrency`、`intervalCap` 必须是整数或 `Infinity`。
- 🧩 自定义 `queueClass` 现在必须实现 `remove()`；`.add()` 在 `priority` 为 `NaN` 或非数字时以 `TypeError` 拒绝。
- 📉 `.start()`、`.clear()` 和设置 `concurrency` 不再在队列已空时触发 `empty` 和 `idle`，`idle` 不会在从未有任务的队列上触发。
- 🆕 零依赖；任务会在其 `.add()` 调用的异步上下文中运行，可看到调用方的 `AsyncLocalStorage` 值，即使稍后启动也一样。
- 🛑 带 `timeout` 的任务会获得一个超时中止的 `signal`，可传给 `fetch()` 等以停止工作。
- 📣 `.onEmpty()` 和 `empty` 事件现在在最后一个等待任务开始时触发，而不是下一个任务完成时。
- 🧾 `.addAll()` 在任务返回不同类型时，现在解析为类型化元组。
- 🐛 修复大量限流 bug、共享 signal 时 add/run/abort 缓慢、`PriorityQueue` 内存保留、事件与优先级边界情况、`undefined` 选项、无效 `.timeout` setter 以及许多 TypeScript 类型问题。
- 🔄 迁移提示：重复添加同一监听器只会调用一次；事件派发期间移除的监听器不会收到该事件；有 `signal` 或 `timeout` 的任务会比以前晚 2 个微任务结算。

---

### [发布 v7](https://github.com/actions/setup-node/releases/tag/v7.1.0)

**原文标题**: [Release v7.1.0 · actions/setup-node · GitHub](https://github.com/actions/setup-node/releases/tag/v7.1.0)

actions/setup-node 发布 v7.1.0，新增 mise.toml 与绝对路径支持，修复 Node 版本验证和 manifest 获取问题，并集中更新文档、依赖与版本信息。

- 🚀 v7.1.0 由 v-gowridurgad 于 10 月 8 日发布，为 Marketplace 最新版本。
- 🧩 增强：支持 mise.toml 文件配置。
- 📁 增强：node-version-file 现支持绝对路径。
- 🐛 Bug 修复：加入 Node 版本验证，并为 manifest 获取增加重试机制。
- 📝 文档更新：README 升级 actions/checkout 至 v7，补充 V7 ESM 迁移与 NODE_AUTH_TOKEN 行为变更，修复缓存推荐语法。
- ⬆️ 依赖更新：升级 @actions/cache、actions/checkout、prettier、@vercel/ncc、pnpm/action-setup、eslint 等，并将包版本升至 7.1.0。
- 👥 新贡献者：@v-jitenderpalsingh、@philip-gai、@gperdomor、@SubJunk 首次贡献。
- 🔗 完整变更日志：v7.0.0...v7.1.0，发布资产共 3 个。

---

### [](https://github.com/actions/setup-node/pull/1421)

**原文标题**: [feat: add support for mise.toml file by gperdomor · Pull Request #1421 · actions/setup-node · GitHub](https://github.com/actions/setup-node/pull/1421)

overview summary
该 PR 为 actions/setup-node 添加从 mise.toml 读取 Node.js 版本的能力，经历从 2025 年 10 月到 2026 年 8 月的长期审查与修改后，于 2026-08-13 合并进 actions:main，并关闭 issue #1304。

- 🎯 PR #1421 由 gperdomor 提交，目标是为 actions/setup-node 增加对 mise.toml 的支持，关联 issue #1304。
- 🛠️ 核心改动是在 src/util.ts 中解析 mise.toml，从配置中提取 Node.js 版本，兼容字符串与对象格式。
- 📦 依赖调整方面，最初引入 js-toml，后改用 smol-toml，以减少依赖和打包体积。
- 📝 文档与测试同步更新：README、action.yml、docs/advanced-usage.md 加入 mise.toml 说明，并新增测试用例、tests/data/mise.toml fixture 和 versions.yml 矩阵覆盖。
- 🤖 Copilot 代码审查提出 2 条建议，作者处理后通过；社区也给出大量点赞和 +1 支持。
- ⏳ PR 长时间等待维护者反馈，作者多次催审和 force-push，直到 2026-07-30 维护者给出详细审查意见。
- ✅ 维护者要求解决合并冲突，并在 action.yml、docs/advanced-usage.md、.github/workflows/versions.yml 和 tests/data/ 中补齐 mise.toml 相关支持。
- 🔧 作者随后更新文档与测试，修复 Licensed 和版本检查问题，CI 最终通过。
- 👥 获批者包括 v-gowridurgad、v-priya-kinthali、v-HarithaVattikuti 等；kentem-yu-ogihara 曾误点批准后表示忽略。
- 🎉 2026-08-13 由 v-HarithaVattikuti 合并到 actions:main，226 项检查通过，源分支删除，issue #1304 关闭。
- ⚠️ 合并后该格式尚未进入正式 release tag；使用时需显式指定 node-version-file: mise.toml，Action 不会自动查找该文件，可暂时固定 @main。
- 📈 多个项目已引用该功能，用于统一 mise 工具版本管理，例如 nextjs-boilerplate、rainbow、media-library-client 等。

---

### [](https://github.com/capricorn86/happy-dom)

**原文标题**: [GitHub - capricorn86/happy-dom: A JavaScript implementation of a web browser without its graphical user interface · GitHub](https://github.com/capricorn86/happy-dom)

happy-dom 是一个不含图形用户界面的 Web 浏览器 JavaScript 实现，主要面向测试环境，提供 DOM、Web Components、Fetch API 等浏览器能力，并可搭配多种前端框架与测试工具使用。

- 🌐 核心定位：用 JavaScript 实现无 GUI 的 Web 浏览器，便于在 Node.js 等环境中运行浏览器类测试。
- 📈 仓库热度：约 4.7k stars、355 forks、11 watchers，已有 2,350 次提交。
- 🧩 主要功能：支持 Custom Elements（Web Components）、Declarative Shadow DOM、Mutation Observer、Tree Walker、Fetch API 等。
- 🧪 兼容生态：可与 Vitest、Bun、Jest、Testing Library、LitElement、Vue、React、Svelte、Angular 等配合使用。
- 📚 文档入口：提供 Documentation、Getting started、Setup as Test Environment 等指南。
- 🤝 社区与规范：包含 Contributing Guide、Code of Conduct、Security Policy，鼓励社区贡献。
- ⚖️ 许可协议：MIT License，© 2019-Present David Ortner。
- 🏷️ 相关主题：angular、browser、bun、dom、html、javascript、nodejs、typescript、vitest、vue、web-components、whatwg 等。

---

### [发布 v21.0.0 · capricorn86/happy-dom · GitHub](https://github.com/capricorn86/happy-dom/releases/tag/v21.0.0)

**原文标题**: [Release v21.0.0 · capricorn86/happy-dom · GitHub](https://github.com/capricorn86/happy-dom/releases/tag/v21.0.0)

happy-dom 发布 v21.0.0，这是一次包含破坏性变更的安全更新，默认禁用 CSS 与 IFrame 加载以降低 SSRF 风险；旧设置被弃用，并新增更细粒度开关。
- 🚀 happy-dom 发布 v21.0.0，由 github-actions 于 10 月 11 日 23:46 发布，提交为 0a99c75。
- 💣 破坏性变更：默认禁用 CSS 和 IFrame 加载，以防止服务器端请求伪造（SSRF）。
- ⚠️ 攻击者可在不受信任的 HTML 中嵌入 `<iframe>` 或 `<link rel="stylesheet">`，诱使 Happy DOM 从服务器向攻击者指定 URL 发起 HTTP 请求。
- 🔓 这可能访问原本不可达的内部服务端点，或根据应用与网络权限触发非预期操作。
- 🗑️ 设置属性 `disableCSSFileLoading` 已被弃用。
- 🆕 新增设置属性 `enableCSSFileLoading` 和 `enableIframePageLoading`。
- 👤 贡献者：@capricorn86。

---

### [](https://github.com/sindresorhus/p-map)

**原文标题**: [GitHub - sindresorhus/p-map: Map over promises concurrently · GitHub](https://github.com/sindresorhus/p-map)

p-map 是 sindresorhus 开发的 JavaScript/Node.js 库，用于并发映射 Promise，核心是控制并发数、结果顺序、错误处理与中止，适合批量异步任务。

- 📦 安装方式：`npm install p-map`。
- 🚀 核心用途：对多个输入并发执行返回 Promise 或 async 的 mapper，常用于批量请求、文件处理等。
- 🧮 与 `Promise.all()` 的区别：可限制并发，并可决定出错后是否停止迭代。
- 🧩 主要 API：`pMap`、`pMapSettled`、`pMapKeyed`、`pMapSettledKeyed`、`pMapIterable`。
- ✅ `pMap`：全部成功时按输入顺序返回结果；任一 Promise 拒绝则整体拒绝。
- 🛡️ `pMapSettled`：类似 `Promise.allSettled()`，返回每个元素的 fulfilled/rejected 状态，不因单个错误拒绝整体。
- 🗂️ `pMapKeyed` / `pMapSettledKeyed`：用于对象或 `Map`，保持键和顺序；对象结果原型为 `null`。
- 🌊 `pMapIterable`：返回异步可迭代对象，可边映射边流式产出结果。
- ⚙️ `concurrency`：默认 `Infinity`，最小 1；按网络、数据库、文件系统、子进程等情况设置。
- 🧷 `backpressure`：仅 `pMapIterable`，限制尚未被消费者取走的元素数，默认等于 concurrency。
- 🔀 `preserveOrder`：仅 `pMapIterable`，默认 `true`；设为 `false` 时结果就绪即产出。
- 🚦 `stopOnError`：`pMap` / `pMapKeyed` 默认 `true`；为 `false` 时等待全部完成并抛出 `AggregateError`。
- 🛑 `signal`：用 `AbortController` 中止，不适用于 `pMapIterable`。
- ⏭️ `pMapSkip`：跳过该结果，不加入数组或对象键。
- ⏹️ `pMapStop`：像 `break` 一样停止迭代，保留之前结果，已运行 mapper 不会被取消。
- 🧪 配方：可与 `p-throttle` 组合限速，与 `p-limit` 组合动态改变并发。
- 🔗 相关包：`p-all`、`p-filter`、`p-times`、`p-props`、`p-map-series`。
- ⭐ 项目信息：约 1.5k stars、86 forks、106 commits，提供 README、License、行为准则、贡献和安全政策。

---

### [](https://github.com/sindresorhus/p-map/releases/tag/v7.1.0)

**原文标题**: [Release v7.1.0 · sindresorhus/p-map · GitHub](https://github.com/sindresorhus/p-map/releases/tag/v7.1.0)

p-map v7.1.0（10 月 9 日发布）重点新增 pMapSettled、pMapKeyed、pMapSettledKeyed、pMapStop，并为 pMapIterable 增加 preserveOrder 与预读优化；同时改进错误堆栈、线性消费与 promise 开销，并修复多个 pMapIterable 的顺序、背压和中断问题。

- 🆕 新增 pMapSettled：类似 Promise.allSettled()，支持 mapper 与并发限制。
- 🗂️ 新增 pMapKeyed 和 pMapSettledKeyed：映射对象或 Map 的值，类似 Promise.allKeyed() 与 Promise.allSettledKeyed()。
- ⏹️ 新增 pMapStop：可从 mapper 中停止迭代，类似循环中的 break。
- 🔀 pMapIterable 新增 preserveOrder 选项；设为 false 可结果一就绪就返回，而非按输入顺序。
- ⚡ pMapIterable 在 backpressure 大于 concurrency 时会在 mapper 运行时预读，慢输入不再让 mapper 等待下一个元素；默认 backpressure 下行为不变。
- 🧭 改进：mapper 错误堆栈中现在会保留调用方。
- ⏱️ pMapIterable 结果消费改为线性时间，修复默认 backpressure 下许多结果等待时的 O(n²) 问题。
- 🪶 降低每个元素的 promise 开销。
- 🚫 nullish input 现在与其他无效 input 一样抛出 TypeError。
- 🔢 修复 next() 调用乱序完成时的处理：index 与结果位置跟随 next() 调用顺序。
- 📥 当 stopOnError: false 时，AggregateError 中的错误改为按输入顺序排列，而非发生顺序。
- 💥 修复 pMapIterable 在 mapper 抛错且结果仍被读取时丢弃较早结果；错误前的结果会先被 yield，类似循环。
- 🧱 修复 pMapSkip 结果未计入 pMapIterable 的 backpressure；跳过多数元素时不会超出 backpressure 预读。
- 🛑 修复 pMapIterable 在 next() 待处理时，于 return() 或 throw() 后仍拉取并映射输入的问题。

---

### [GitHub - fent/randexp.js：创建与](https://github.com/fent/randexp.js)

**原文标题**: [GitHub - fent/randexp.js: Create random strings that match a given regular expression. · GitHub](https://github.com/fent/randexp.js)

randexp.js 是一个 JavaScript 库，可根据给定的正则表达式生成随机匹配字符串，适合测试、数据模拟等场景，并支持多种正则特性、自定义字符范围和随机数生成器。

- 🧩 核心功能：根据 `RegExp` 对象生成随机字符串，例如 `new RandExp(/hello+(world|toyou)/).gen()`。
- 🛠️ 支持特性：分组、管道、集合、范围、反向引用、通配符、忽略大小写，以及动态正则字符串。
- ⚡ 快捷用法：`randexp(/[1-6]/)` 或 `randexp('great|good( job)?|excellent')`；调用 `sugar()` 可恢复 `/.../.gen()` 旧语法。
- 🎯 设计动机：正则表达式适合描述复杂字符串，因此也适合用来随机生成匹配该正则的字符串。
- 🔤 默认字符范围：默认可打印 ASCII，可通过 `defaultRange.subtract()` 和 `add()` 调整，也可修改 `RandExp.prototype.defaultRange`。
- 🎲 自定义随机数：可覆盖 `RandExp.prototype.randInt` 或实例的 `randInt`，以使用可播种或加密安全的 PRNG。
- ♾️ 无限重复处理：`*`、`+`、`{3,}` 默认最大值为最小值加 100，可通过 `max` 属性修改。
- ⚠️ 无效正则处理：会忽略位置标记、忽略不存在的反向引用，对 `[^\w\W]` 等返回空字符串。
- 📦 相关项目：JSON-Schema Faker 使用生成器填充 JSON Schema 示例。
- 💻 安装与测试：Node.js 使用 `npm install randexp`；浏览器可下载压缩版；测试基于 mocha；包含 TypeScript 定义。
- 🔒 安全：安全漏洞可通过 Tidelift 安全联系方式报告。
- ⭐ 仓库信息：MIT 许可，约 1.9k stars、95 forks、23 watchers、172 commits。

---

### [](https://github.com/oracle/node-oracledb)

**原文标题**: [GitHub - oracle/node-oracledb: Oracle Database driver for Node.js maintained by Oracle Corporation. Connect your JavaScript and TypeScript applications instantly to Oracle Database. · GitHub](https://github.com/oracle/node-oracledb)

node-oracledb 是 Oracle 官方维护的 Node.js Oracle Database 驱动，用于将 JavaScript/TypeScript 应用连接到 Oracle Database；当前版本 26.0.0，开源、稳定、文档完善，并提供全面测试。

- 📦 **项目定位**：Oracle 官方维护的 Node.js Oracle Database 驱动，支持 TypeScript 和 JavaScript。
- 🚀 **版本与兼容**：26.0.0 支持 Node.js 14.17 及更高版本；旧版驱动可兼容旧版 Node.js。
- 🧩 **功能范围**：支持 Oracle Database 和 Oracle Client 的基础与高级功能，被众多框架、SQL 生成器、ORM 和库使用。
- ⚙️ **执行控制**：可控制 SQL/PLSQL 执行、快速数据摄取、NoSQL 风格文档 API、消息队列、数据库通知和数据库启停。
- 🛡️ **高可用与安全**：内置高可用与安全特性，数据库操作可选择流水线化。
- 📥 **安装方式**：运行 `npm install oracledb`，npm 和镜像提供预构建包，也可从源码构建。
- 🔌 **Thin/Thick 模式**：6.0 起 Oracle Client 库为可选；默认 Thin 模式直接连接数据库；Thick 模式需加载 Oracle Instant Client 等库，支持 19+ 客户端。
- 🗄️ **数据库要求**：Thin 模式需 Oracle Database 12.1+；Thick 模式需 11.2+，具体取决于 Oracle Client 版本，并支持标准客户端-服务器互操作。
- 🧪 **质量与测试**：由 Oracle 维护，稳定、文档完善，并有全面测试套件；测试说明见 `test/README`。
- 📚 **文档与示例**：提供官方文档、发布说明和 `examples` 目录，建议从 `examples/example.js` 开始。
- 💬 **帮助与贡献**：可在 GitHub 或 Slack 提问；项目欢迎社区贡献，需先阅读贡献指南。
- ⚖️ **许可证**：双许可 UPL 1.0 或 Apache 2.0，可任选其一。
- ⭐ **仓库热度**：约 2.4k stars、1.1k forks、165 watchers、3,034 commits；当前 20 个 issues、1 个 PR。

---

