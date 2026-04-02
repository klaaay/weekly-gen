### [JavaScript 周刊第 779 期：2026 年 3 月 31 日](https://javascriptweekly.com/issues/779)

**原文标题**: [JavaScript Weekly Issue 779: March 31, 2026](https://javascriptweekly.com/issues/779)

本期 JavaScript 周刊涵盖了多个重要动态，包括 Axios 库的安全事件、AI 测试工具 Meticulous 的推广、Transformers.js v4 的发布，以及 Node.js 等多个项目的版本更新。此外，还介绍了信号机制原理、npm 工作区使用指南等技术文章，并推荐了 Pretext 布局库、Knip 项目清理工具等新工具。

- 🚨 Axios 库遭恶意依赖攻击，建议检查项目依赖并采取安全措施如锁定版本或禁用安装后脚本。
- 🤖 Meticulous AI 提供自动化的端到端 UI 测试，被多家知名公司采用。
- 🌐 Transformers.js v4 支持在浏览器中运行 AI 模型，并转向 WebGPU 运行时。
- 🔄 多个项目发布新版本，包括 Inertia.js 3.0、Node.js 安全更新、TanStack DB 0.6 等。
- 📚 技术文章涵盖信号机制原理、npm 工作区指南、Next.js 调试技巧等。
- 🛠️ 新工具推荐包括 Pretext 文本布局库、Knip 项目清理工具、ArtPlayer 视频播放器等。
- 📢 生态动态涉及 JetBrains IDE 免费支持 JS/TS、GitHub Copilot 数据使用政策调整等。

---

### [axios 在 npm 上遭入侵——恶意版本投放远程访问木马——StepSecurity](https://www.stepsecurity.io/blog/axios-compromised-on-npm-malicious-versions-drop-remote-access-trojan)

**原文标题**: [axios Compromised on npm - Malicious Versions Drop Remote Access Trojan - StepSecurity](https://www.stepsecurity.io/blog/axios-compromised-on-npm-malicious-versions-drop-remote-access-trojan)

axios 作为最流行的 JavaScript HTTP 客户端库，于 2026 年 3 月 30 日被发现其 npm 包的两个版本（1.14.1 和 0.30.4）被恶意篡改。攻击者通过劫持维护者账户，在包中注入了一个名为 `plain-crypto-js@4.2.1` 的恶意依赖。该依赖的唯一目的是在其 `postinstall` 脚本中执行一个跨平台的远程访问木马（RAT）投放器，针对 macOS、Windows 和 Linux 系统。攻击经过精心策划，包括预先准备恶意依赖、同时污染两个主要发布分支，并在执行后自我清理以隐藏证据。StepSecurity 通过其 AI 包分析器和 Harden-Runner 工具检测到了此次攻击，并已协助进行披露和缓解。

- 🚨 **攻击概述**：axios 的 npm 包（版本 1.14.1 和 0.30.4）被植入恶意依赖 `plain-crypto-js@4.2.1`，该依赖在安装时执行 RAT 投放器。
- 🔓 **入侵方式**：攻击者通过劫持主要维护者的 npm 账户（`jasonsaayman`）并更改其邮箱，手动发布了恶意版本，绕过了正常的 GitHub Actions CI/CD 流程。
- 📦 **恶意依赖**：`plain-crypto-js@4.2.1` 伪装成合法的 `crypto-js` 库，其 `postinstall` 脚本会触发一个经过混淆的投放器（`setup.js`）。
- 🌐 **攻击载荷**：投放器会根据操作系统（macOS、Windows、Linux）下载并执行不同的第二阶段 RAT 载荷，同时向攻击者的 C2 服务器（`sfrclak.com:8000`）发起通信。
- 🧹 **隐匿行踪**：执行后，恶意脚本会删除自身和原始的 `package.json`，并用一个干净的存根文件（显示版本为 4.2.0）替换，以逃避检测。
- ⏱️ **攻击时间线**：攻击经过约 18 小时预演，恶意依赖先于 axios 发布。两个恶意 axios 版本在 39 分钟内相继发布，并在约 3 小时后被 npm 下架。
- 🛡️ **检测与响应**：StepSecurity 的工具检测到了异常的网络连接和包行为。社区、axios 维护者、GitHub 和 npm 迅速响应，下架了恶意包并控制了相关账户。
- ✅ **修复建议**：如果安装了受影响版本，应立即降级到安全版本（如 axios@1.14.0 或 0.30.3），检查并移除 `node_modules/plain-crypto-js` 目录，检查系统是否存在 RAT 残留文件，并旋转所有可能泄露的凭证。建议在 CI/CD 中使用 `--ignore-scripts` 标志。

---

### [Axios](https://axios-http.com/)

**原文标题**: [Axios](https://axios-http.com/)

Axios 是一个基于 Promise 的 HTTP 客户端，适用于浏览器和 Node.js，以简洁易用、轻量且接口高度可扩展为特点。

- 🌐 支持浏览器与 Node.js 环境
- 🤝 基于 Promise 的异步请求处理
- 📦 轻量级且易于使用的库
- 🔧 提供高度可扩展的接口

---

### [axios 在 npm 上遭入侵——恶意版本投放远程访问木马——StepSecurity](https://www.stepsecurity.io/blog/axios-compromised-on-npm-malicious-versions-drop-remote-access-trojan#am-i-affected)

**原文标题**: [axios Compromised on npm - Malicious Versions Drop Remote Access Trojan - StepSecurity](https://www.stepsecurity.io/blog/axios-compromised-on-npm-malicious-versions-drop-remote-access-trojan#am-i-affected)

axios 作为最流行的 JavaScript HTTP 客户端库，其 npm 包在 2026 年 3 月 30 日被发现遭到供应链攻击。攻击者通过劫持维护者账户，发布了恶意版本 axios@1.14.1 和 axios@0.30.4。这些版本注入了一个名为 plain-crypto-js@4.2.1 的恶意依赖包，该包包含一个后安装脚本，会在安装时部署一个跨平台的远程访问木马，并随后自我销毁以掩盖痕迹。

- 🚨 **攻击概述**：攻击者劫持了 axios 维护者的 npm 账户，发布了两个恶意版本（1.14.1 和 0.30.4），注入了一个从未在源码中使用的恶意依赖包 `plain-crypto-js@4.2.1`。
- 📦 **恶意依赖**：`plain-crypto-js@4.2.1` 伪装成合法的加密库，其唯一目的是在 `postinstall` 阶段执行一个混淆的 RAT 投放器脚本 `setup.js`。
- 🖥️ **跨平台攻击**：投放器会根据操作系统（macOS、Windows、Linux）下载并执行不同的第二阶段恶意载荷，并与攻击者的命令与控制服务器通信。
- 🧹 **自我销毁**：恶意脚本执行后，会删除自身和原始的 `package.json`，并用一个干净的存根文件替换，以逃避取证检测。
- 🔍 **检测与响应**：StepSecurity 通过其 AI 包分析器和 Harden-Runner 工具检测到了此次攻击，并协调了负责任的披露。恶意包在发布后数小时内被 npm 下架。
- ⏱️ **攻击时间线**：攻击经过了精心策划，恶意依赖包提前约 18 小时发布以建立历史记录，两个恶意 axios 版本在 39 分钟内相继发布。
- 🛡️ **影响与修复**：如果安装了受影响版本，应假定系统已遭入侵。建议立即降级到安全版本（如 axios@1.14.0），检查并移除 `plain-crypto-js` 目录，并轮换所有可能暴露的凭证。在 CI/CD 中可使用 `--ignore-scripts` 标志来防止 `postinstall` 钩子执行。

---

### [Axios 供应链攻击：恶意依赖包被植入...](https://socket.dev/blog/axios-npm-package-compromised)

**原文标题**: [Supply Chain Attack on Axios Pulls Malicious Dependency from...](https://socket.dev/blog/axios-npm-package-compromised)

恶意版本的 Telnyx Python SDK 在 PyPI 上通过多阶段供应链攻击传播窃取凭证的恶意软件。

- 🐍 恶意 Python 包通过 PyPI 分发，伪装成 Telnyx 官方 SDK
- 🔗 攻击采用多阶段供应链攻击，依赖链中隐藏恶意代码
- 🛡️ 恶意软件旨在窃取用户凭证和敏感系统信息
- ⚠️ 开发者需验证包来源，检查依赖关系以防供应链攻击
- 📦 建议使用安全工具扫描第三方包，确保开发环境安全

---

### [axios@1.14.1 和 axios@0.30.4 版本存在安全漏洞 · Issue #10604 · axios/axios · GitHub](https://github.com/axios/axios/issues/10604)

**原文标题**: [axios@1.14.1 and axios@0.30.4 are compromised · Issue #10604 · axios/axios · GitHub](https://github.com/axios/axios/issues/10604)

axios 项目在 npm 上发布的两个版本被发现包含恶意代码，可能涉及维护者账户被入侵。

- 🚨 **安全警报**：axios 的 1.14.1 和 0.30.4 版本在 npm 上被确认为恶意版本
- 🔗 **详情来源**：问题详情指向 stepsecurity.io 博客，其中披露了这些版本会投放远程访问木马
- 👤 **账户安全**：怀疑维护者的 GitHub 和 npm 账户可能已被入侵，导致相关问题被删除
- 📝 **漏洞报告**：已将此问题作为安全漏洞上报，以便生成 CVE 编号
- ⚠️ **社区状态**：当前无法添加反应，且该问题尚未分配处理人员或添加标签

---

### [固定您的 npm/yarn 依赖项](https://maxleiter.com/blog/pin-dependencies)

**原文标题**: [Pin your npm/yarn dependencies](https://maxleiter.com/blog/pin-dependencies)

本文讨论了因开源维护者故意破坏 JavaScript 库而引发的供应链安全问题，强调了通过锁定依赖版本来防御此类风险的重要性，并提供了具体实施方法和工具建议。

- 🔒 **锁定依赖版本**：为防止恶意更新，建议在 package.json 中精确指定依赖版本（如"17.0.2"），而非使用范围版本（如"^17.0.2"）
- ⚙️ **配置自动锁定**：通过在.npmrc 设置`save-exact=true`或使用 npm/yarn 的`--save-exact`/`--exact`参数自动实现版本锁定
- 📦 **善用锁文件**：package-lock.json/yarn.lock 可锁定嵌套依赖，但需注意 npm i 与 npm ci 的行为差异，推荐生产环境使用`npm ci`
- 🔄 **自动化更新管理**：配合使用 Renovate 等工具定期检查依赖更新，在安全可控的前提下保持依赖现代性
- 📝 **保持可读性**：以 package.json 为版本依据，便于人工审计依赖关系，同时利用锁文件确保安装一致性

---

### [npm 引入 minimumReleaseAge 与批量 OIDC 配置...](https://socket.dev/blog/npm-introduces-minimumreleaseage-and-bulk-oidc-configuration)

**原文标题**: [npm Introduces minimumReleaseAge and Bulk OIDC Configuration...](https://socket.dev/blog/npm-introduces-minimumreleaseage-and-bulk-oidc-configuration)

TeamPCP 与勒索软件组织 Vect 合作，将针对 Trivy 和 LiteLLM 等开源工具的攻击转化为大规模勒索行动，威胁开源供应链安全。

- 🔗 TeamPCP 与勒索组织 Vect 联手，升级开源供应链攻击
- 🛠️ 主要攻击目标为 Trivy 和 LiteLLM 等流行开源工具
- 💰 攻击目的从破坏转为大规模勒索金钱
- ⚠️ 开源软件供应链面临更严峻的勒索威胁
- 📅 该安全事件于 2026 年 3 月 26 日由 Sarah Gooding 报道

---

### [缓解供应链攻击 | pnpm](https://pnpm.io/supply-chain-security)

**原文标题**: [Mitigating supply chain attacks | pnpm](https://pnpm.io/supply-chain-security)

本文介绍了使用 pnpm 缓解供应链攻击风险的多种策略，包括禁用依赖中的 postinstall 脚本、阻止非常规传递依赖、延迟依赖更新、实施信任策略以及使用锁文件。

- 🛡️ 禁用风险构建脚本：pnpm v10 默认禁用依赖中的 postinstall 脚本执行，可通过 allowBuilds 仅允许受信任依赖构建，降低恶意脚本风险
- 🔗 阻止非常规依赖：设置 blockExoticSubdeps 为 true，防止传递依赖使用 git 或 tarball 等非常规来源，确保依赖来源可信
- ⏳ 延迟依赖更新：通过 minimumReleaseAge 设置版本发布后的最小等待时间（如 1440 分钟即 24 小时），利用恶意软件通常被快速发现的特点规避风险
- 📜 实施信任策略：使用 trustPolicy 设置（如 no-downgrade）防止安装信任等级降低的包，并通过 trustPolicyExclude 和 trustPolicyIgnoreAfter 进行灵活配置
- 🔒 使用锁文件：始终通过锁文件锁定依赖版本并提交至代码仓库，避免意外更新带来的安全风险

---

### [精密 AI——无需编写测试的自动化前端测试](https://www.meticulous.ai?utm_source=jsweekly&utm_medium=referral&utm_campaign=26q1&utm_content=primary)

**原文标题**: [Meticulous AI - Automated Frontend Testing Without Writing Tests](https://www.meticulous.ai?utm_source=jsweekly&utm_medium=referral&utm_campaign=26q1&utm_content=primary)

Meticulous AI 是一款创新的自动化测试工具，通过记录用户与应用交互生成持续演进的测试套件，无需手动编写或维护测试，帮助开发团队快速、可靠地发布代码。

- 🎯 **自动化测试生成**：通过记录开发、预演和生产环境的用户交互，自动创建覆盖所有代码分支和用户流程的测试
- ⚡ **零维护与无异常**：测试套件随应用演进自动更新，消除测试维护负担，并从根本上解决测试不稳定的问题
- 🔄 **预合并影响分析**：在代码合并前展示改动对用户工作流程的影响，通过模拟后端响应实现无副作用测试
- 🚀 **高速并行测试**：利用计算集群并行执行测试，可在 120 秒内完成数千个页面的测试
- 🔗 **广泛框架兼容**：支持 NextJS、React、Vue、Angular、Nuxt、SvelteKit 等主流前端框架
- 🏢 **企业级验证**：已被 Dropbox、Notion 等 100 多家组织采用，显著提升工程团队开发效率

---

### [发布 4.0.0 版本 · huggingface/transformers.js · GitHub](https://github.com/huggingface/transformers.js/releases/tag/4.0.0)

**原文标题**: [Release 4.0.0 · huggingface/transformers.js · GitHub](https://github.com/huggingface/transformers.js/releases/tag/4.0.0)

Transformers.js v4 正式发布，引入全新 WebGPU 后端、支持更多模型架构、提供 ModelRegistry API 等生产级功能，并重构代码库以提升性能和开发体验。

- 🚀 采用全新 WebGPU 后端，支持浏览器、Node.js、Bun、Deno 等多种 JavaScript 环境，性能显著提升
- 🧠 新增支持 GPT-OSS、Chatterbox、GraniteMoeHybrid 等众多新模型，包括 Mamba、MLA、MoE 等先进架构
- 📦 引入 ModelRegistry API，提供管道资源管理、文件元数据查看、缓存状态检查等生产级功能
- ⚙️ 新增环境控制选项，支持 WASM 缓存、自定义 fetch 实现和日志级别管理
- 🏗️ 代码库重构为 pnpm monorepo，模型定义模块化，示例项目移至独立仓库
- 🔤 发布独立轻量级 tokenizers.js 库，仅 8.8kB，零依赖，完全类型安全
- ⚡ 构建系统迁移至 esbuild，构建时间减少 10 倍，包体积平均缩小 10%
- 🐛 修复多项 bug，改进类型系统，优化文档，新增贡献者指南

---

### [Hugging Face——构建未来的人工智能社区。](https://huggingface.co/)

**原文标题**: [Hugging Face – The AI community building the future.](https://huggingface.co/)

这是一个面向机器学习社区的协作平台，用户可在此探索、共享和合作开发模型、数据集及应用程序，并提供企业级解决方案与开源工具支持。

- 🤝 **社区协作平台** – 提供模型、数据集和应用程序的托管与协作空间，支持公开分享与发现。
- 🚀 **海量资源库** – 可浏览超过 200 万个模型、100 万个应用和 50 万个数据集，涵盖文本、图像、音频等多种模态。
- 💡 **热门趋势展示** – 首页展示每周热门模型与应用，如 Qwen3.5、Cohere 转录模型、Voxtral TTS 等。
- 🏢 **企业级服务** – 提供团队与企业方案，包含单点登录、审计日志、私有数据集查看器等功能，起价 20 美元/用户/月。
- ⚙️ **计算与部署** – 支持在优化推理终端部署模型，或为空间应用升级 GPU，GPU 使用起价 0.60 美元/小时。
- 🌐 **统一 API 接入** – 通过单一 API 访问超过 4.5 万个领先 AI 提供商的模型，无需额外服务费。
- 🏆 **知名机构采用** – 已有 5 万多家组织使用，包括 AI2、Meta、亚马逊、谷歌、英特尔、微软等。
- 🔧 **开源工具生态** – 提供 Transformers、Diffusers、Datasets 等一系列开源库，支持从训练到部署的全流程。

---

### [Transformers.js V4 演示 - webml-community 精选集](https://huggingface.co/collections/webml-community/transformersjs-v4-demos)

**原文标题**: [Transformers.js V4 demos - a webml-community Collection](https://huggingface.co/collections/webml-community/transformersjs-v4-demos)

这是一个基于 Transformers.js V4 构建的演示集合，展示了多种在浏览器中本地运行的 AI 模型应用，涵盖文本、语音、图像和视频处理。

- 💧 **LFM2.5 1.2B Thinking WebGPU** – 在浏览器中通过 WebGPU 直接运行 LFM2.5-1.2B-Thinking 模型
- 💬 **Voxtral Realtime WebGPU** – 完全在浏览器内进行实时语音转录
- ⚛ **Nemotron 3 Nano WebGPU** – 在浏览器中运行具备推理能力的紧凑模型
- ⚡ **GPT OSS WebGPU** – 在浏览器中通过 WebGPU 本地运行 GPT-OSS-20B 模型
- 😻 **Qwen3.5 WebGPU** – 在浏览器中使用 Transformers.js 运行 Qwen3.5 模型系列
- 📹 **LFM2 VL WebGPU** – 在浏览器中进行实时视频字幕生成
- 🎥 **Text Behind Video** – 在浏览器本地创建电影风格的视频设计
- 🌐 **TranslateGemma 4B WebGPU** – 支持 56 种语言的私有浏览器翻译器
- ⚡ **Cohere Transcribe WebGPU** – 在浏览器中本地运行 Cohere Transcribe
- 🔮 **Nanbeige 4.1 3B** – 在浏览器中本地与 Nanbeige AI 聊天
- 🎯 **SAM3 Tracker WebGPU** – 通过点击点分割图像并下载裁剪部分
- 💧 **LFM2 MoE WebGPU** – 由 WebGPU 加速的混合专家模型
- ⚡ **RF DETR Medium WebGPU** – 在浏览器中运行的实时检测 Transformer 模型
- 🦙 **Olmo Hybrid WebGPU** – 在浏览器中通过 WebGPU 完全本地运行 Olmo-Hybrid-7B 模型
- 🗣 **Granite 4.0 1b Speech WebGPU** – 在 WebGPU 上使用 Transformers.js 运行 granite-4.0-1b-speech 模型
- 🌍 **TinyAya WebGPU** – 在浏览器中本地运行 TinyAya 模型
- ✖ **QED-Nano WebGPU** – 在浏览器中本地运行 QED-Nano 模型
- 🚀 **voyage-4-nano WebGPU** – 在交互式散点图中可视化句子嵌入
- ⚡ **RF DETR Nano WebGPU** – 在浏览器中运行的实时检测 Transformer 模型
- 🦅 **Falcon-H1-Tiny-90M WebGPU** – 展示 Falcon-H1 架构（Mamba + Attention）
- 🎠 **Perplexity Embed Web** – 语义搜索文档并在 3D 旋转木马中查看结果
- 🚀 **LFM2.5 WebGPU Summarizer** – 在浏览器中本地总结网页内容

---

### [Voxtral 实时 WebGPU - 由 mistralai 创建的 Hugging Face 空间](https://huggingface.co/spaces/mistralai/Voxtral-Realtime-WebGPU)

**原文标题**: [Voxtral Realtime WebGPU - a Hugging Face Space by mistralai](https://huggingface.co/spaces/mistralai/Voxtral-Realtime-WebGPU)

清爽感是一种令人愉悦的体验，通常与干净、凉爽或振奋的感觉相关，能带来身心上的舒适与活力。

- 🌊 带来清凉与洁净的感受
- 💧 常用于描述水、空气或气味等元素
- 🌿 能提振精神，缓解疲劳
- 🍃 在炎热天气中尤为受欢迎
- 🧼 与清洁产品或自然场景紧密关联

---

### [Qwen3.5 WebGPU - 由 webml-community 创建的 Hugging Face 空间](https://huggingface.co/spaces/webml-community/Qwen3.5-WebGPU)

**原文标题**: [Qwen3.5 WebGPU - a Hugging Face Space by webml-community](https://huggingface.co/spaces/webml-community/Qwen3.5-WebGPU)

清爽是一种令人愉悦的感觉，通常与清新、干净、凉爽或振奋的体验相关。它可以是身体上的，如一阵凉风或一杯冰水带来的舒适；也可以是精神上的，比如新的想法或休息后的活力恢复。在日常生活中，追求清爽感能帮助缓解压力，提升心情，让人感到焕然一新。

- 💨 身体上的清爽感常来自凉爽的空气、冷水浴或轻便的衣物，带来即时的舒适与放松。
- 🧠 精神上的清爽涉及清晰的思维、创意的迸发或休息后的重新专注，提升整体精神状态。
- 🌿 环境中的清爽元素，如绿色植物、整洁的空间或自然光线，能营造宁静和焕然一新的氛围。
- 🚿 日常习惯如锻炼、健康饮食和充足睡眠，有助于维持持久的清爽感，促进身心健康。
- 😌 追求清爽感可以减轻压力、改善情绪，使人在忙碌生活中找到平衡与活力。

---

### [LFM2 VL WebGPU - LiquidAI 在 Hugging Face 上的空间](https://huggingface.co/spaces/LiquidAI/LFM2-VL-WebGPU)

**原文标题**: [LFM2 VL WebGPU - a Hugging Face Space by LiquidAI](https://huggingface.co/spaces/LiquidAI/LFM2-VL-WebGPU)

清爽体验带来身心愉悦与活力提升。

- 🍃 清新感受能缓解压力，带来轻松心情
- 💧 水元素常象征清爽，如沐浴、饮水或自然水域
- 🌞 适宜温度与通风环境增强清爽感，促进舒适
- 🏃 活动后清爽感尤为明显，恢复精力与清醒度
- 🌿 天然植物与绿色空间贡献清新氛围，改善空气质量

---

### [Inertia.js - 现代单体架构](https://inertiajs.com/)

**原文标题**: [Inertia.js - The Modern Monolith](https://inertiajs.com/)

Inertia 是一个全栈框架，允许开发者使用 React、Vue 或 Svelte 构建现代单页应用体验，同时保持传统的服务器端路由和逻辑，无需构建 API 即可与 Laravel 等后端无缝集成。

- 🚀 支持使用 React、Vue 或 Svelte 开发单页应用，并享受服务器端路由的优势
- 🔌 无需 API，可即插即用与任何后端（如 Laravel、Rails、Django）集成
- 🛠️ 提供生产就绪功能，包括表单处理、SEO 优化、部分重载和实时轮询
- 🔄 支持服务器端渲染、资源版本控制和共享数据，提升应用性能与用户体验
- 📄 包含代码示例，展示如何在后端控制器中查询数据并传递至前端组件渲染
- 📊 具备无限滚动、预取和延迟加载等高级功能，简化复杂交互的实现
- 🔒 身份验证和状态管理完全基于后端，确保安全性与一致性
- 📚 提供详细文档和针对 Laravel 的入门套件，便于快速上手和部署

---

### [Inertia.js v3 现已进入测试版 | Laravel - 为工匠与代理打造的简洁技术栈](https://laravel.com/blog/inertiajs-v3-is-now-in-beta)

**原文标题**: [Inertia.js v3 Is Now in Beta | Laravel - The clean stack for Artisans and agents](https://laravel.com/blog/inertiajs-v3-is-now-in-beta)

Inertia.js v3 已进入 Beta 测试阶段，该版本引入了多项重要更新，包括内置 XHR 客户端替代 Axios、全新的 Vite 插件实现自动页面解析与 SSR，并新增了对乐观更新、独立 HTTP 请求和布局属性的原生支持，旨在减少模板代码和依赖，提升应用性能。

- 🚀 **内置 XHR 客户端**：移除了 Axios 依赖，采用内置 XHR 客户端处理 HTTP 通信，减小了打包体积。
- ⚡ **Vite 插件集成**：新插件自动处理页面解析、懒加载、代码分割和 SSR 配置，大幅简化了项目设置。
- 🔄 **乐观更新支持**：用户操作可立即获得界面反馈，服务器响应后自动同步数据，失败时自动回滚。
- 🌐 **独立 HTTP 请求钩子**：新增 `useHttp` 钩子，为 API 调用等非页面请求提供与 `useForm` 一致的状态管理体验。
- ⚙️ **布局属性管理**：通过 `useLayoutProps` 钩子，页面可动态覆盖布局的默认属性，无需复杂的事件传递机制。
- 🛠️ **开发环境 SSR 优化**：Vite 插件支持开发环境下直接启用 SSR，无需单独启动 Node.js 服务。
- 🚧 **异常处理增强**：新增 `handleExceptionsUsing()` 方法，允许自定义错误响应并集成共享数据。
- 📦 **模块化与类型增强**：全面转向 ESM 模块，提供表单组件泛型支持，并允许在响应中直接使用 PHP 枚举。
- ⚠️ **升级要求**：需要 PHP 8.2+、Laravel 11+ 及对应前端框架适配器的最新版本，部分旧 API 已被移除或更名。

---

### [Node.js — 2026 年 3 月 24 日星期二安全版本发布](https://nodejs.org/en/blog/vulnerability/march-2026-security-releases)

**原文标题**: [Node.js — Tuesday, March 24, 2026 Security Releases](https://nodejs.org/en/blog/vulnerability/march-2026-security-releases)

Node.js 项目于 2026 年 3 月 24 日发布了针对多个版本的安全更新，修复了包括高、中、低严重性在内的多个安全漏洞，涉及 TLS、HTTP 处理、权限模型、URL 解析等多个核心模块。

- 🛡️ **TLS SNI 回调异常处理漏洞** (CVE-2026-21637, 高危)：`SNICallback` 中的同步异常未受保护，可能导致 Node.js 进程崩溃，影响 20.x、22.x、24.x 和 25.x 版本。
- 🚨 **HTTP 头部原型污染漏洞** (CVE-2026-21710, 高危)：当请求头名为 `__proto__` 且访问 `req.headersDistinct` 时，会引发未捕获的 `TypeError` 导致进程崩溃，影响 20.x、22.x、24.x 和 25.x 版本。
- 🔓 **权限模型绕过漏洞** (CVE-2026-21711, 中危)：在未授予 `--allow-net` 权限时，仍可绑定/监听 Unix 域套接字服务器，仅影响 25.x 版本。
- 💥 **URL 解析断言失败漏洞** (CVE-2026-21712, 中危)：使用格式错误的国际化域名调用 `url.format()` 会导致原生代码断言失败，进程崩溃，影响 24.x 和 25.x 版本。
- ⏱️ **HMAC 验证时序侧信道漏洞** (CVE-2026-21713, 中危)：HMAC 验证使用了非恒定时间比较，可能泄露时序信息，影响 20.x、22.x、24.x 和 25.x 版本。
- 🧠 **HTTP/2内存泄漏漏洞** (CVE-2026-21714, 中危)：客户端在流 0 上发送导致流量控制窗口溢出的 `WINDOW_UPDATE` 帧时，`Http2Session` 对象无法被清理，导致内存泄漏，影响 20、22、24 和 25 版本。
- 🐌 **V8 哈希拒绝服务漏洞** (CVE-2026-21717, 中危)：V8 的字符串哈希机制存在缺陷，攻击者可构造大量哈希碰撞的请求，显著降低进程性能，影响 20.x、22.x、24.x 和 25.x 版本。
- 👁️ **权限模型文件存在泄露漏洞** (CVE-2026-21715, 低危)：`fs.realpathSync.native()` 未执行读取权限检查，可绕过 `--allow-fs-read` 限制探测文件存在性，影响 20.x、22.x、24.x 和 25.x 版本。
- 🔧 **权限模型补丁绕过漏洞** (CVE-2026-21716, 低危)：对 CVE-2024-36137 的修复不完整，`FileHandle.chmod()` 和 `FileHandle.chown()` 的 Promise API 未进行权限检查，影响 20.x、22.x、24.x 和 25.x 版本。

---

### [Node.js — Node.js 25.8.2（当前版本）](https://nodejs.org/en/blog/release/v25.8.2)

**原文标题**: [Node.js — Node.js 25.8.2 (Current)](https://nodejs.org/en/blog/release/v25.8.2)

Node.js 25.8.2 是一个安全版本，主要修复了多个安全漏洞，包括高、中、低不同严重级别的 CVE 问题，并更新了依赖项。

- 🛡️ 修复了高风险的 CVE-2026-21637，通过 try/catch 包装 SNICallback 调用
- 🛡️ 修复了高风险的 CVE-2026-21710，为 headersDistinct/trailersDistinct 使用 null 原型
- 🛡️ 修复了中风险的 CVE-2026-21711，在 pipe_wrap.cc 中添加权限检查
- 🛡️ 修复了中风险的 CVE-2026-21712，处理不同 URL 格式导致的崩溃问题
- 🛡️ 修复了中风险的 CVE-2026-21713，在 Web Cryptography HMAC 和 KMAC 中使用时序安全比较
- 🛡️ 修复了中风险的 CVE-2026-21714，处理 NGHTTP2_ERR_FLOW_CONTROL 错误代码
- 🛡️ 修复了中风险的 CVE-2026-21717，测试数组索引哈希碰撞
- 🛡️ 修复了低风险的 CVE-2026-21715，为 realpath.native 添加权限检查
- 🛡️ 修复了低风险的 CVE-2026-21716，在 lib/fs/promises 中包含权限检查
- 🔄 更新了依赖项，包括 undici 到 7.24.4 和 npm 到 11.11.1
- 📦 提供了 Windows、macOS、Linux、AIX 等多个平台的安装包和二进制文件下载链接

---

### [Node.js — Node.js 24.14.1（长期支持版）](https://nodejs.org/en/blog/release/v24.14.1)

**原文标题**: [Node.js — Node.js 24.14.1 (LTS)](https://nodejs.org/en/blog/release/v24.14.1)

Node.js 24.14.1（LTS）版本发布，代号“Krypton”，这是一个安全更新版本，主要修复了多个安全漏洞，并包含依赖项更新。

- 🔒 修复了多个安全漏洞，包括两个高危漏洞（CVE-2026-21710 和 CVE-2026-21637），涉及 HTTP 头处理和 TLS SNI 回调
- 📦 更新了多个依赖项，包括 undici 升级至 7.24.4、npm 升级至 11.11.0，以及 V8 引擎的多个补丁
- 🛡️ 修复了四个中危漏洞，涉及 Web 加密 API、HTTP/2 流控制、URL 解析和数组索引哈希碰撞
- 🔐 修复了两个低危漏洞，主要涉及文件系统权限检查的增强
- 🌐 提供了多平台安装包和二进制文件下载，支持 Windows、macOS、Linux、AIX 等多种操作系统和架构
- 📄 包含完整的源代码和文档链接，以及所有发布文件的 SHA256 校验和 PGP 签名

---

### [Node.js — Node.js 22.22.2（长期支持版）](https://nodejs.org/en/blog/release/v22.22.2)

**原文标题**: [Node.js — Node.js 22.22.2 (LTS)](https://nodejs.org/en/blog/release/v22.22.2)

Node.js 22.22.2（LTS）版本于 2026 年 3 月 24 日发布，代号“Jod”，这是一个安全更新版本，主要修复了多个安全漏洞，并包含依赖项升级和代码优化。

- 🛡️ 修复了多个安全漏洞，包括两个高危漏洞（CVE-2026-21637 和 CVE-2026-21710），涉及 TLS SNI 回调处理和 HTTP 头/尾部的原型污染问题
- 🔧 更新了多个依赖项，包括 npm 升级至 10.9.7、undici 更新至 v6.24.1，并进行了 V8 引擎的后端修复
- 📦 提供了多平台安装包和二进制文件，支持 Windows、macOS、Linux（包括 ARM、PPC、s390x 架构）和 AIX 系统
- 📄 包含完整的源代码和文档链接，以及所有发布文件的 SHA256 校验和 PGP 签名，确保下载完整性

---

### [Node.js — Node.js 20.20.2（长期支持版）](https://nodejs.org/en/blog/release/v20.20.2)

**原文标题**: [Node.js — Node.js 20.20.2 (LTS)](https://nodejs.org/en/blog/release/v20.20.2)

Node.js 20.20.2（LTS）版本发布，这是一个安全更新版本，主要修复了多个安全漏洞，包括数组索引哈希碰撞、Web 加密 API 中的时序攻击防护、HTTP 头处理、权限检查以及 TLS 回调错误处理等问题。

- 🔐 修复了数组索引哈希碰撞的安全漏洞（CVE-2026-21717）
- ⏱️ 在 Web 加密 API 的 HMAC 和 KMAC 中采用时序安全比较（CVE-2026-21713）
- 🛡️ 为 headersDistinct/trailersDistinct 使用 null 原型以避免原型污染（CVE-2026-21710）
- 📁 在 lib/fs/promises 中添加了权限检查（CVE-2026-21716）
- 🔍 为 realpath.native 方法增加了权限验证（CVE-2026-21715）
- 🌐 处理 NGHTTP2_ERR_FLOW_CONTROL 错误代码（CVE-2026-21714）
- 🔒 在 TLS 的 SNICallback 调用中包裹 try/catch 以增强错误处理（CVE-2026-21637）
- 🔗 更新了 undici 依赖至 v6.24.1 版本
- 📦 提供了 Windows、macOS、Linux 等多平台的安装包和二进制文件下载

---

### [TanStack DB 0.6 现已支持持久化、离线功能与层级数据 | TanStack 博客](https://tanstack.com/blog/tanstack-db-0.6-app-ready-with-persistence-and-includes)

**原文标题**: [TanStack DB 0.6 Now Includes Persistence, Offline Support, and Hierarchical Data | TanStack Blog](https://tanstack.com/blog/tanstack-db-0.6-app-ready-with-persistence-and-includes)

TanStack DB 0.6 版本引入了持久化存储、离线支持、分层数据投影等关键功能，显著增强了应用数据层的完整性和开发体验。

- 💾 **持久化本地状态**：通过 SQLite 适配器支持浏览器、React Native、Node 等多运行时环境，实现数据持久化与离线优先体验。
- 🌳 **分层数据投影**：新增 `includes` 功能，允许将规范化数据投影为 UI 所需的层次结构，避免 N+1 查询并保持细粒度响应性。
- ⚙️ **响应式副作用**：引入 `createEffect` 支持基于实时查询结果的自动化工作流与代理式任务处理。
- 🔍 **虚拟属性**：提供 `$synced`、`$origin` 等虚拟属性，便于实现发件箱视图、同步状态指示等 UI 模式。
- 🎯 **一次性查询**：新增 `queryOnce` API，支持在加载器、脚本等场景中使用相同的查询语言进行非实时查询。
- 📦 **索引可选化**：索引功能改为按需启用，减少默认捆绑体积，并提供 `BasicIndex` 与 `BTreeIndex` 两种实现。
- 🔄 **显式突变处理**：移除“隐式返回”行为，要求突变处理器显式协调同步逻辑，提升 API 一致性。
- 🚀 **服务端渲染设计**：团队正征集 SSR 设计合作伙伴，以完善 v1 版本的服务端渲染支持。

---

### [Astro 6.1 | Astro](https://astro.build/blog/astro-610/)

**原文标题**: [Astro 6.1 | Astro](https://astro.build/blog/astro-610/)

Astro 6.1 版本发布，引入了多项新功能和改进，包括全局图像编码控制、高级智能标点配置、国际化回退路由支持，以及多项性能优化和错误修复。

- 🖼️ 新增全局图像编码默认设置，可在 Astro 配置中统一配置 Sharp 服务的 JPEG、WebP、AVIF 和 PNG 编码参数，无需为每个图像单独设置。
- 🔤 开放完整的 SmartyPants 配置，支持自定义非英语语言的标点转换规则，如法语引号、德语引号等。
- 🌐 为集成插件提供国际化回退路由访问，使如站点地图生成等工具能自动包含回退页面。
- 📱 优化移动端视图过渡，避免在浏览器自带过渡（如 iOS Safari 滑动手势）时出现双重动画闪烁。
- ⚠️ 新增 Vite 8 兼容性警告，并在使用 `astro add cloudflare` 时自动添加版本覆盖，防止常见崩溃问题。
- 🔧 修复了 React 水合错误，包括条件性插槽渲染和实验性 React 子节点不匹配问题。
- 🛡️ 改进了在反向代理后的 CSRF 保护，正确读取 `X-Forwarded-Proto` 头，避免表单提交时的误报 403 错误。

---

### [版本 v9.0.0 | Mantine](https://mantine.dev/changelog/9-0-0/)

**原文标题**: [Version v9.0.0 | Mantine](https://mantine.dev/changelog/9-0-0/)

Mantine 9.0.0 是一个重大版本更新，引入了全新的日程安排组件包、多项现有组件的增强功能、对 React 19 的更好支持，以及许多新的钩子和特性，旨在提升开发体验和应用性能。

- 📅 **全新日程安排包**：新增 `@mantine/schedule` 包，提供完整的日历日程组件，支持日、周、月、年视图及移动端优化视图，并内置拖拽事件管理。
- ⚙️ **依赖要求更新**：要求 React 19.2+，`@mantine/tiptap` 需要 Tiptap 3+，`@mantine/charts` 需要 Recharts 3+。
- 🧩 **新组件与钩子**：新增 `OverflowList`、`Marquee`、`Scroller`、`BarsList`、`FloatingWindow` 等组件，以及 `useCollapse`、`useFloatingWindow`、`useScroller` 等实用钩子。
- 🔄 **现有组件增强**：`Collapse` 支持水平折叠，`Card` 支持水平布局，`Checkbox.Group`/`Switch.Group` 支持 `maxSelectedValues`，所有输入组件支持 `loading` 状态，`Slider` 支持垂直方向等。
- ✅ **表单功能升级**：`use-form` 支持异步验证、`TransformedValues` 类型参数、`Standard Schema` 集成以及新的 `isUrl` 和 `isOneOf` 验证器。
- 🎨 **样式与主题改进**：新增 `fontWeights` 主题属性控制字体粗细，默认主题圆角改为 `md`，所有组件支持逻辑边距和内边距样式属性。
- ⚡ **性能与兼容性**：`Grid` 组件改用 CSS `gap` 属性，`Tree` 组件性能优化，多个钩子改用 React 19 的 `useEffectEvent`，`Transition` 等组件使用 React 19 `Activity` 以保持隐藏状态。
- 📚 **文档与工具**：新增自定义组件、受控与非受控组件等指南，发布 `@mantine/mcp-server` 包支持 Model Context Protocol，便于 AI 工具查询文档。

---

### [发布 v2.0.0-0 · sindresorhus/ky · GitHub](https://github.com/sindresorhus/ky/releases/tag/v2.0.0-0)

**原文标题**: [Release v2.0.0-0 · sindresorhus/ky · GitHub](https://github.com/sindresorhus/ky/releases/tag/v2.0.0-0)

Ky 库发布了 v2.0.0-0 预发布版本，这是下一个主要版本的测试版，引入了多项重大变更和新功能，旨在提升 API 一致性和开发者体验。

- 🚨 **重大变更**：要求 Node.js 22 环境，统一钩子函数签名，`prefixUrl` 更名为 `prefix`，`beforeError` 钩子现在接收所有错误类型，空响应时 `.json()` 返回 `undefined`，`searchParams` 改为合并而非替换查询参数，`HTTPError` 错误体通过 `error.data` 同步访问。
- ✨ **新增功能**：添加 `totalTimeout` 选项以设置总超时时间，引入 `baseUrl` 选项用于标准 URL 解析，新增 `init` 钩子，添加 `NetworkError` 类并优化重试逻辑，支持 `.json()` 的 Standard Schema 验证，提供 `replaceOption` 辅助方法用于扩展。
- 🛠️ **问题修复**：修复了 `beforeRequest` 钩子在返回 `Request` 时被跳过的问题，忽略 `beforeError` 钩子返回的非 Error 对象，优化了错误处理和资源管理。
- 📘 **迁移指南**：详细说明了从 v1 升级到 v2 所需的代码调整，包括钩子签名更新、选项重命名、错误处理方式变更及新 API 的使用方法。

---

### [发布 v48.0.0 · ckeditor/ckeditor5 · GitHub](https://github.com/ckeditor/ckeditor5/releases/tag/v48.0.0)

**原文标题**: [Release v48.0.0 · ckeditor/ckeditor5 · GitHub](https://github.com/ckeditor/ckeditor5/releases/tag/v48.0.0)

CKEditor 5 v48.0.0 正式发布，这是一个主要版本更新，重点改进了 AI 功能和表格处理，完成了旧安装方法的淘汰，并引入了统一的根配置结构。此版本包含多项重大和次要的破坏性变更，建议用户仔细阅读更新指南。

- 🎉 **旧安装方法淘汰完成**：自 v42.0.0 引入的现代安装方法现已完全取代旧方法，简化了开发流程并支持更快的更新。
- 🤖 **AI 功能增强**：优化了 AI 聊天、审阅、快速操作和翻译中的建议预览样式，使其与编辑区域更一致；通过缓存模型请求减少了初始化时的网络调用。
- 📊 **表格功能改进**：支持导入旧版 HTML 表格属性（如 `border` 和 `cellpadding`），新增表格页脚支持，并默认启用表格对齐的 CSS 类输出。
- 📄 **导出 PDF 默认 API 版本升级**：默认使用版本 2 的转换器 API，提供更强大的页眉页脚配置、页面尺寸调整和数字签名支持。
- 🏗️ **统一的根配置结构**：将 `initialData`、`placeholder` 等根相关配置选项统一归到 `config.root`（单根编辑器）或 `config.roots`（多根编辑器）下，使配置更一致。
- ⚠️ **重大破坏性变更**：涉及 AI、Uploadcare、多根编辑器配置、表格对齐输出方式等多个模块，旧有配置方式已被移除或更改，需按指南迁移。
- 🐛 **多项问题修复**：修复了 AI 聊天消息顺序、代码块间距、表格内断词、CSS 重置影响范围等众多错误，提升了稳定性和用户体验。
- ✨ **新功能引入**：包括表格单元格类型切换、表头 `scope` 属性支持、脚注列表样式配置、移除格式功能增强等。
- 📦 **依赖与架构更新**：移除了 DLL 构建和对旧安装方法的支持，更新了 TypeScript 版本，并将多个包的软依赖替换为插件构造函数。

---

### [发布 pnpm 10.33 · pnpm/pnpm · GitHub](https://github.com/pnpm/pnpm/releases/tag/v10.33.0)

**原文标题**: [Release pnpm 10.33 · pnpm/pnpm · GitHub](https://github.com/pnpm/pnpm/releases/tag/v10.33.0)

pnpm 10.33.0 版本发布，引入了新的 `dedupePeers` 设置以减少对等依赖重复，并修复了多项问题，包括 CI 环境中的锁文件处理、并发安装错误及 Windows 路径解析等。

- 🆕 新增 `dedupePeers` 设置，通过简化对等依赖标识符减少包实例数量，优化递归对等依赖项目的性能
- 🔧 在 CI 的冻结锁文件模式下，对不兼容的锁文件报错，同时保留非冻结模式的回退行为
- 🛠️ 修复 `pnpm dlx` 并发调用时的间歇性失败问题，增强全局虚拟存储的稳定性和 Windows 兼容性
- 🐛 修正 `hoistPeers` 中非字符串版本选择器的处理，避免无效的对等依赖规范
- 💡 改进非交互式模块清理的错误提示，提供 `confirmModulesPurge=false` 的解决方案
- 🔍 修复 Windows 上因命令非零退出码导致的“命令未找到”错误，优化 `--filter` 的路径解析
- 📄 忽略 pnpm-lock.yaml 中的首个文档，为 v11 版本存储版本完整性和配置依赖解析做准备
- 🧹 修复 `createNpmResolver` 返回的 `clearCache` 函数无法正确清除元数据缓存的问题

---

### [信号，基于推拉算法的实现 — 威利·布劳纳](https://willybrauner.com/journal/signal-the-push-pull-based-algorithm)

**原文标题**: [Signals, the push-pull based algorithm — Willy Brauner](https://willybrauner.com/journal/signal-the-push-pull-based-algorithm)

本文深入探讨了信号（Signals）的内部工作原理，特别是其核心的推拉（push-pull）算法。信号作为响应式编程的现代实现，通过自动追踪依赖和惰性求值，实现了细粒度的状态更新。文章通过代码示例和交互式图示，详细解析了信号如何推送通知使依赖失效，以及计算值如何在被读取时拉取最新状态，从而构建高效的响应式系统。

- 🧠 信号是响应式编程的现代实现，基于推拉算法，能自动追踪依赖并高效更新状态。
- 🌐 响应式编程思想源于 20 世纪 70 年代，系统内数据源的变化会自动传播到依赖计算图中。
- 📡 信号采用推送机制：当信号值改变时，立即通知所有订阅者，标记依赖的计算值为“脏”（无效）。
- 🔄 计算值采用拉取机制：只有被读取且标记为“脏”时，才会重新计算，实现惰性求值和缓存优化。
- 🧩 依赖自动追踪通过全局栈实现：计算值执行时，其访问的信号会自动注册为依赖，建立动态关联。
- 🏗️ 推拉结合形成完整流程：信号推送失效通知，计算值在需要时拉取最新值，确保更新精确且高效。
- 🚀 该算法已被 Solid、Vue、Preact 等框架采用，且 TC39 正在推动信号在 JavaScript 中的原生标准化。

---

### [介绍信号——Preact](https://preactjs.com/blog/introducing-signals/)

**原文标题**: [Introducing Signals – Preact](https://preactjs.com/blog/introducing-signals/)

Signals 是一种基于响应式原理的状态管理方案，旨在确保应用无论复杂度如何都能保持高性能。它通过对象属性访问自动订阅更新，无需手动优化，且与 Preact 深度集成，仅增加 1.6kB 体积。

- 🚀 **高性能默认**：Signals 自动优化更新，无需依赖记忆化或选择器，确保应用快速响应。
- 🔗 **无缝集成**：可直接在组件内外使用，与现有 Hooks 和类组件兼容，支持渐进式采用。
- 📦 **轻量体积**：在 Preact 中使用仅增加 1.6kB 包大小，保持库的小巧优势。
- 🧩 **解决状态管理痛点**：针对全局状态提升、Context 过度渲染和记忆化复杂性等问题，提供细粒度更新方案。
- ⚡ **超越虚拟 DOM**：支持将 Signal 直接传递到 JSX，绕过组件重渲染，直接更新 DOM 文本或属性。
- 🧠 **直观开发体验**：无需选择器或包装函数，直接访问信号值即可自动订阅更新，简化代码逻辑。
- 🌱 **渐进式采用**：无需立即替换现有 Hooks，可逐步在组件中尝试 Signals 并享受其性能优势。

---

### [JavaScript 预加载图片的多种方法 | Alex MacArthur](https://macarthur.me/posts/preloading-images/)

**原文标题**: [Your options for preloading images with JavaScript | Alex MacArthur](https://macarthur.me/posts/preloading-images/)

本文探讨了使用 JavaScript 预加载图像的多种方法，每种方法各有优缺点，适用于不同场景。

- 🖼️ **new Image() 方法**：通过创建 Image 对象并设置 src 属性触发下载，可监听加载完成事件并获取图像尺寸，但依赖浏览器 HTTP 缓存，若服务器返回 no-store 缓存头则失效。
- 🔗 **<link rel="preload">方法**：通过注入 link 标签声明预加载，资源存入专用“预加载缓存”，即使服务器禁止 HTTP 缓存也能生效，且浏览器会智能复用未完成的请求。
- 🎭 **隐藏 div 背景图方法**：创建隐藏 div 设置背景图可触发下载，但需注意 display: none 会导致资源不加载，需用 visibility: hidden 等替代方案。
- 🗃️ **Cache API 方法**：通过缓存接口精确控制资源存储与清理，支持跨页面持久化，但需手动管理缓存避免累积。
- 🎣 **fetch() 方法**：提供灵活请求控制，可直接处理响应数据，但同样受服务器缓存策略限制，且不自动管理缓存。

作者最终选择<link rel="preload">方案解决评论图片延迟加载问题，因其能可靠预加载且无需复杂管理。其他方法可根据具体需求（如需要加载回调、长期缓存或精细控制）灵活选用。

---

### [调试 Next.js 应用程序 - YouTube](https://www.youtube.com/playlist?list=PLOwEowqdeNMqf3dArAE-Mo4rVR7T2Vanr&si=tQ_vlQ4bzm_w2MXF)

**原文标题**: [Debugging Next.js Applications - YouTube](https://www.youtube.com/playlist?list=PLOwEowqdeNMqf3dArAE-Mo4rVR7T2Vanr&si=tQ_vlQ4bzm_w2MXF)

该文本是 YouTube 平台页脚的标准链接列表，概述了其核心服务条款、公司信息及用户资源。

- ℹ️ 关于平台与公司信息
- 📰 新闻与媒体相关
- ©️ 版权政策说明
- 📞 联系与反馈渠道
- 🎬 内容创作者资源
- 📢 广告合作信息
- 💻 开发者工具与服务
- 📄 使用条款与协议
- 🔒 隐私与数据保护
- ⚙️ 平台政策与安全指南
- 🔧 YouTube 功能运作机制
- 🧪 新功能测试与更新
- ⏳ 版权年份与公司声明

---

### [npm 工作区轻松入门指南：图文并茂 | Wasp](https://wasp.sh/blog/2026/03/25/gentle-intro-npm-workspaces)

**原文标题**: [A gentle intro to npm workspaces, with visuals | Wasp](https://wasp.sh/blog/2026/03/25/gentle-intro-npm-workspaces)

本文介绍了 npm 工作区的基本概念、工作原理及适用场景，通过历史背景和实际案例解释了工作区如何解决多包项目中的依赖管理和跨包引用问题，并探讨了其内部机制如依赖解析、符号链接等，最后结合 Wasp 框架的应用实例说明了工作区的实际价值。

- 🏗️ npm 工作区允许在单个项目中管理多个 JavaScript 包，实现依赖共享和跨包引用，避免依赖重复和版本冲突。
- 📜 工作区功能起源于 2015 年 Babel 项目的模块化需求，随后由 Lerna 和 Yarn 等工具推动发展，现已被主流包管理器广泛支持。
- 🔗 工作区通过将子包视为虚拟根包的依赖来实现依赖共享，利用现有解析算法确保相同依赖只安装一次。
- 📂 跨包引用通过符号链接实现：在根目录的 node_modules 中创建指向各工作区的链接，使 Node.js 能按名称正确解析导入。
- ⚠️ 工作区适用于多包紧密耦合、依赖共享频繁的项目（如 monorepo），但不适用于独立包、循环依赖或多仓库场景。
- 🐝 Wasp 框架利用工作区管理生成的 SDK、前端和后端包，提升开发体验，减少依赖错误，并支持用户自定义工作区集成。

---

### [工作区 | npm 文档](https://docs.npmjs.com/cli/v8/using-npm/workspaces/)

**原文标题**: [workspaces | npm Docs](https://docs.npmjs.com/cli/v8/using-npm/workspaces/)

npm 工作区是一个用于管理本地文件系统中多个包的 npm CLI 功能集，它通过自动符号链接简化了多包项目的开发流程。

- 🏗️ 工作区允许在单个根包中管理多个本地包，自动处理包之间的符号链接，无需手动使用`npm link`。
- 📁 通过在根`package.json`的`workspaces`属性中定义路径来配置工作区，例如`"workspaces": ["packages/a"]`。
- 🚀 使用`npm init -w ./packages/a`可快速创建新工作区并自动配置根包。
- 📦 通过`-w`参数为特定工作区添加依赖，例如`npm install abbrev -w a`。
- 🔗 工作区中的包可通过其`package.json`中定义的名称直接相互引用，利用 Node.js 的模块解析机制。
- ⚙️ 使用`--workspace`参数在特定工作区中运行命令，例如`npm run test --workspace=a`。
- 🌐 使用`--workspaces`参数可在所有工作区中运行命令，顺序由`package.json`中的配置决定。
- ⚠️ 通过`--if-present`标志可忽略缺少脚本的工作区，避免运行失败。

---

### [我反编译了白宫的新应用](https://blog.thereallo.dev/blog/decompiling-the-white-house-app)

**原文标题**: [I Decompiled the White House's New App](https://blog.thereallo.dev/blog/decompiling-the-white-house-app)

白宫发布了一款官方应用，该应用被分析发现具备多项隐蔽功能，包括注入脚本绕过网站隐私与付费墙、内置位置追踪框架、加载第三方非政府代码以及存在开发残留问题。

- 🕵️ 应用内置 JavaScript 注入器，自动隐藏第三方网站的 Cookie 提示、GDPR 同意框、登录墙和付费墙
- 📍 集成完整 GPS 追踪框架，可每 4.5 分钟（前台）/9.5 分钟（后台）收集位置数据并上传至 OneSignal 服务器
- 🔗 依赖多个非政府第三方服务：包括个人 GitHub Pages（视频播放器）、Elfsight（社交组件）、Mailchimp（邮件订阅）和 Uploadcare（图片托管）
- 🔓 缺乏证书固定机制，网络流量可能被中间人攻击拦截
- 🏗️ 生产版本残留开发痕迹：包含本地调试地址、开发者 IP、开发菜单图标和测试组件
- 📊 通过 OneSignal 实现全方位用户画像：记录标签、手机号、设备别名、行为转化、通知交互等数据
- 🏛️ 技术架构基于 React Native+Expo，后端采用 WordPress 定制 API，由"forty-five-press"实体开发
- ⚠️ 权限声明存在差异：应用商店列出的位置权限未在清单中声明，但 SDK 代码包含完整定位功能模块

---

### [使用 Three.js、Velocity 与情绪背景构建滚动响应式 3D 画廊 | Codrops](https://tympanus.net/codrops/2026/03/09/building-a-scroll-reactive-3d-gallery-with-three-js-velocity-and-mood-based-backgrounds/)

**原文标题**: [Building a Scroll-Reactive 3D Gallery with Three.js, Velocity, and Mood-Based Backgrounds | Codrops](https://tympanus.net/codrops/2026/03/09/building-a-scroll-reactive-3d-gallery-with-three-js-velocity-and-mood-based-backgrounds/)

本文介绍了一个使用 Three.js 构建的滚动响应式 3D 画廊教程，结合深度分层图像、调色板驱动的背景和基于滚动速度的动态效果，旨在创造一种沉浸式的浏览体验。

- 🎨 **深度分层设计**：图像沿 Z 轴堆叠，形成空间感，而非传统的平面轮播。
- 🌈 **动态背景调色**：每张图像定义专属调色板，滚动时背景渐变平滑过渡，营造氛围变化。
- 🚀 **滚动速度响应**：捕捉滚动速度作为信号，驱动场景微动（如倾斜、缩放），增强交互感。
- 📐 **模块化代码结构**：采用类基础架构，分离场景、画廊、滚动和背景逻辑，提升可维护性。
- 🖼️ **真实图像集成**：替换占位符为真实图像，并根据宽高比自动调整平面尺寸，避免拉伸。
- 🧩 **调试工具辅助**：开发阶段使用可视化调试条监控滚动速度，确保参数调整准确。
- ✨ **细节增强体验**：添加编辑性文本层、鼠标视差微动和粒子拖尾效果，提升叙事与视觉吸引力。
- 🔮 **未来扩展方向**：建议探索产品展示、音频互动或基于速度的深度视觉效果等应用场景。

---

### [为何我们用 Bun 替代 Node.js 实现 5 倍吞吐量 | Trigger.dev](https://trigger.dev/blog/firebun)

**原文标题**: [Why we replaced Node.js with Bun for 5x throughput | Trigger.dev](https://trigger.dev/blog/firebun)

Trigger.dev 团队将关键服务 Firestarter 从 Node.js 迁移至 Bun，实现了 5 倍的吞吐量提升，并解决了 Bun 特有的内存泄漏问题。通过多轮性能优化，包括替换 SQLite 为 Map 数据结构、使用 Bun.serve()、优化热点代码路径以及编译为独立二进制文件，最终显著降低了延迟和资源占用，同时总结了 Bun 与 Node.js 在 HTTP 模型上的重要差异及调试经验。

- 🚀 **性能大幅提升**：迁移至 Bun 后，吞吐量从 2,099 req/s提升至约10,700 req/s，最大延迟从619ms降至约17ms，实现5倍性能优化。
- 🗃️ **数据结构优化**：将 SQLite 查询替换为基于 Map 的 O(1) 查找，使吞吐量提升 2.2 倍，延迟降低一半。
- 🔧 **Bun 特性应用**：采用 Bun.serve() 原生路由，结合编译为独立二进制文件，进一步减少依赖并提升 14% 吞吐量。
- 🐛 **内存泄漏修复**：发现并修复了 Bun 中因未解析的 Promise 导致的连接泄漏，通过显式返回 499 状态码确保资源释放。
- 📊 **系统化基准测试**：通过 k6 模拟真实负载，在每个优化阶段进行量化验证，确保改动效果可衡量。
- 🛠️ **生产环境洞察**：Bun 在 CPU 和事件循环稳定性上表现更优，但需注意其 HTTP 模型与 Node.js 的差异，特别是响应生命周期管理。
- 📚 **调试经验总结**：提供了 Bun 内存泄漏排查、性能分析工具使用及 prom-client 兼容性处理等实用技巧。

---

### [借口](https://simonwillison.net/2026/Mar/29/pretext/)

**原文标题**: [Pretext](https://simonwillison.net/2026/Mar/29/pretext/)

Pretext 是一个创新的浏览器库，由前 React 核心开发者 Cheng Lou 创建，它无需操作 DOM 即可高效计算换行文本的高度，通过分离 prepare 和 layout 函数优化性能，并支持多语言和复杂字符，其测试方法包括使用《了不起的盖茨比》等多样文本验证准确性。

- 🚀 Pretext 是一个浏览器库，无需操作 DOM 即可计算换行文本高度，提升渲染性能
- 🧠 采用 prepare 和 layout 函数分离设计，prepare 缓存文本段测量结果，layout 模拟浏览器换行逻辑
- 🌍 支持多语言和复杂字符，包括韩语、阿拉伯语及平台特定表情符号
- 🧪 测试方法严谨，使用《了不起的盖茨比》等多样文本验证测量准确性
- 🔧 由 Cheng Lou 开发，基于 React-motion 经验，库体积小巧且兼容浏览器特性

---

### [未找到标题](https://x.com/_chenglou/status/2037713766205608234)

**原文标题**: [No title found](https://x.com/_chenglou/status/2037713766205608234)

该页面提示用户浏览器中 JavaScript 功能未启用或受阻，导致无法正常使用 X 平台（原 Twitter），并提供了相应的解决方案和支持信息。

- 🔐 检测到浏览器已禁用 JavaScript，影响 X 平台正常使用
- 🌐 建议启用 JavaScript 或切换至受支持的浏览器版本
- 📖 可访问帮助中心查看支持的浏览器列表
- 🛡️ 部分隐私扩展可能导致加载异常，建议暂时禁用后重试
- 🔄 页面提供手动重试功能及平台服务条款等法律文件入口

---

### [GitHub - chenglou/pretext · GitHub](https://github.com/chenglou/pretext)

**原文标题**: [GitHub - chenglou/pretext · GitHub](https://github.com/chenglou/pretext)

Pretext 是一个纯 JavaScript/TypeScript 库，用于多行文本的测量与布局，无需依赖 DOM 测量，支持多种语言和渲染目标。

- 📏 **文本测量与布局**：提供高性能的文本高度测量和手动布局功能，避免触发浏览器重排。
- 🚀 **高性能与预计算**：`prepare()` 进行一次性文本分析，`layout()` 进行快速计算，适合动态调整场景。
- 🌍 **多语言与复杂文本支持**：支持包括表情符号和混合双向文本在内的多种语言，适应浏览器特性。
- 🛠️ **灵活的布局 API**：提供 `layoutWithLines`、`walkLineRanges` 和 `layoutNextLine` 等方法，支持 Canvas、SVG 等渲染。
- ⚙️ **配置与缓存管理**：支持字体、空白处理等配置，提供缓存清理和区域设置功能。
- 📝 **注意事项**：针对常见文本设置，部分字体（如 `system-ui`）在 macOS 上可能不准确，需使用命名字体。

---

### [借口演示](https://chenglou.me/pretext/)

**原文标题**: [Pretext Demos](https://chenglou.me/pretext/)

Pretext 是一个用于在 Web 上进行高性能文本布局的库，它通过避免 DOM 测量来优化性能，支持复杂的布局效果，如动态文本流、多列布局和精确的文本高度预测。

- 📐 无需在关键路径中进行 DOM 测量即可计算文本高度，支持手动换行和紧凑的多行 UI
- 🪗 可展开/折叠部分，其文本高度由 Pretext 计算
- 💬 紧凑的多行消息气泡，保持相同行数并减少浪费空间
- 📄 固定高度的编辑版面，支持障碍感知的标题布局和连续文本流
- 🔤 粒子驱动的 ASCII 艺术，比较比例测量字形与等宽版本
- 🌀 动画球体、实时文本重排、引用块和多列流，无需 DOM 测量
- 📏 并排展示 CSS 对齐、贪婪连字符和 Knuth-Plass 段落布局，揭示排版中的间距权衡
- 🎨 富文本内联布局，包括代码片段、链接和标签，保持标签完整同时文本自然换行
- 🧱 文本卡片遮挡演示，高度预测由 Pretext 而非 DOM 读取提供

---

### [专为 React Native 打造的移动 CI/CD](https://expo.dev/services/workflows?utm_source=jsweekly&utm_medium=email&utm_campaign=34911156-NDR%2520-%2520Starter%2520Plan%2520Growth%2520%2526%2520Retention&utm_content=workflows-lp)

**原文标题**: [Mobile CI/CD built for React Native](https://expo.dev/services/workflows?utm_source=jsweekly&utm_medium=email&utm_campaign=34911156-NDR%2520-%2520Starter%2520Plan%2520Growth%2520%2526%2520Retention&utm_content=workflows-lp)

Expo Workflows 是一款专为 React Native 设计的移动端 CI/CD 平台，旨在简化构建、提交、重新打包和 OTA 更新的流程。它提供预构建的作业、高性能的 M4 Pro 硬件、自动化签名和缓存，并能与现有 CI（如 GitHub Actions）无缝集成或完全替代，从而显著降低 DevOps 开销，提升部署效率。

- 🚀 **专为 React Native 构建的 CI/CD**：提供从构建、提交到 OTA 更新的完整移动端流水线，支持与现有 CI 集成或独立运行。
- ⚙️ **高性能基础设施**：在专用的 M4 Pro Apple Silicon 硬件上运行 iOS 构建，速度比通用 macOS 虚拟机快 10-20 分钟。
- 🔐 **自动化签名管理**：仅需一个 `EXPO_TOKEN` 即可替代复杂的密钥库和 Fastlane 配置，签名信息加密存储并在构建时注入。
- 💨 **智能缓存与增量构建**：自动缓存优化构建速度，Fingerprint 技术检测变更，40–60% 的推送可跳过完整构建，仅需重新打包。
- 🔄 **灵活触发与集成**：支持从 GitHub 事件触发、通过 CLI 命令调用或在任何 CI 中运行，提供端到端的轻量级 YAML 配置。
- 📉 **显著降低 DevOps 成本**：通过自动化硬件管理、签名和缓存，减少高达 80% 的运维开销，让工程师更专注于功能开发。
- 🛠️ **渐进式迁移路径**：可先仅将移动构建卸载到 Workflows，保留原有 CI 进行代码检查和测试，后续再逐步迁移完整流水线。
- ⚡ **快速部署选项**：根据代码变更类型，提供完整构建（10-20 分钟）、重新打包（约 2 分钟）和 OTA 更新（<5 分钟）三种高效部署方式。
- 🏆 **经过实战检验**：被 HipCamp、PrizePicks 等企业团队使用，替代了复杂脆弱的构建流程，提升了部署的可靠性和速度。

---

### [Knip v6 发布公告 | Knip](https://knip.dev/blog/knip-v6)

**原文标题**: [Announcing Knip v6 | Knip](https://knip.dev/blog/knip-v6)

Knip v6 发布，核心改进是彻底替换 TypeScript 后端为 oxc-parser 和 oxc-resolver，大幅提升性能，同时引入新功能并调整部分配置。

- 🚀 **性能大幅提升**：通过替换 TypeScript 后端为 oxc 工具，Knip 解析速度提升 2-4 倍，内存效率更高
- 🔧 **架构重构**：移除 TypeScript 程序与类型检查器的开销，专注于单次 AST 遍历，更适合静态分析
- 📊 **实测数据**：多个项目测试显示运行时间显著减少，例如 TypeScript 项目从 3.7 秒降至 0.9 秒
- 🆕 **新增功能**：支持 TypeScript 命名空间（及模块），新增 `namespaceMembers` 问题类型
- ⚠️ **破坏性变更**：不再支持 Node.js v18，移除 `classMembers` 问题类型及部分实验性选项
- 🔌 **插件优化**：ESLint、tsdown 等插件改为静态分析配置文件，避免导入依赖
- 💻 **编辑器扩展**：核心升级使编辑器扩展更快、更省内存，自动检测本地 Knip 版本
- 📈 **未来展望**：因 TypeScript v7 转向 Go 语言，部分功能（如 `classMembers`）可能需替代方案

---

### [精简你的 JavaScript 与 TypeScript 项目 | Knip](https://knip.dev/)

**原文标题**: [Declutter your JavaScript & TypeScript projects | Knip](https://knip.dev/)

Knip v6 是一款用于清理 JavaScript 和 TypeScript 项目中未使用依赖、导出和文件的自动化工具，通过高级分析提供精准结果，已集成 100 多个插件并受到广泛好评。

- 🧹 **清理未使用项**：自动检测并帮助移除未使用的文件、npm 依赖和 TypeScript 导出，保持代码库整洁。
- 🛠️ **智能分析**：基于项目实际框架和工具进行精细入口点分析，确保结果准确且可操作，支持单仓库和 monorepo。
- 📦 **丰富插件生态**：内置 100+ 插件，兼容 Astro、Cypress、Next.js、Vite 等主流工具和框架。
- 🌍 **广泛认可**：被 Shopify 等顶级团队使用，社区评价极高，被誉为提升代码质量和维护效率的必备工具。
- 🎮 **易于上手**：提供在线 Playground 体验和详细故障排除指南，降低使用门槛。

---

### [GitHub - zhw2590582/ArtPlayer: :art: ArtPlayer.js 是一款现代化且功能全面的 HTML5 视频播放器 · GitHub](https://github.com/zhw2590582/ArtPlayer)

**原文标题**: [GitHub - zhw2590582/ArtPlayer: :art: ArtPlayer.js is a modern and full featured HTML5 video player · GitHub](https://github.com/zhw2590582/ArtPlayer)

ArtPlayer.js 是一款功能丰富且易于使用的现代 HTML5 视频播放器，支持高度自定义和多种插件集成。

- 🎨 **功能全面**：作为现代 HTML5 视频播放器，支持 .vtt、.ass、.srt 字幕格式，并可轻松集成 flv.js、hls.js 等依赖库。
- 📦 **安装灵活**：可通过 npm、yarn 安装，也提供 UMD 构建和 CDN 引入方式，方便快速使用。
- 🔌 **插件丰富**：提供弹幕、画质控制、缩略图预览、章节支持、广告插件等多种官方插件，扩展性强。
- 🌐 **在线资源**：拥有在线编辑器、API 文档、演示页面及主页，便于开发者学习和调试。
- 📄 **开源项目**：采用 MIT 许可证，在 GitHub 上开源，拥有活跃的社区贡献和持续的版本更新。

---

### [ArtPlayer.js - 现代 HTML5 视频播放器](https://artplayer.org/)

**原文标题**: [ArtPlayer.js - Modern HTML5 Video Player](https://artplayer.org/)

概述：本文介绍了文件上传功能的基本概念、常见应用场景及实现要点，强调其在现代数字交互中的重要性。

- 📁 文件上传允许用户将本地文件传输至服务器或云端存储
- 🌐 广泛应用于电子邮件附件、社交媒体分享、云存储服务等场景
- 🔒 安全性是关键，需防范恶意文件、限制类型大小并加密传输
- ⚙️ 实现方式多样，包括表单上传、拖拽操作及 API 接口集成
- 📱 移动端优化需考虑触控交互和网络环境适配
- 🛠️ 开发者需处理进度显示、错误反馈和批量上传等用户体验细节

---

### [符号学 — React 的数据可视化](https://semiotic.nteract.io/)

**原文标题**: [Semiotic — Data Visualization for React](https://semiotic.nteract.io/)

该应用需要启用 JavaScript 才能正常运行。

- 🛠️ 功能依赖：应用的核心功能需通过 JavaScript 实现
- 🌐 技术限制：浏览器若禁用 JavaScript 将导致应用无法启动
- ⚙️ 运行前提：用户需在浏览器设置中允许 JavaScript 执行

---

### [图表 — 等值区域图 — 符号学](https://semiotic.nteract.io/charts/choropleth-map/)

**原文标题**: [Charts — Choropleth Map — Semiotic](https://semiotic.nteract.io/charts/choropleth-map/)

Semiotic 是一个用于创建数据可视化图表的 JavaScript 库，提供多种图表类型和交互功能，支持通过命令行工具访问，并包含面向开发者的详细文档和示例。

- 🗺️ 支持创建等值区域图等多种图表类型
- 🏠 提供入门指南、功能说明和演示页面
- 🤖 包含面向 AI 和机器可读的文档格式
- 📚 提供完整的 API 参考和实际应用示例
- 🛠️ 可通过 GitHub 查看源码，并使用命令行工具访问

---

### [图表 — 桑基图 — 符号学](https://semiotic.nteract.io/charts/sankey-diagram/)

**原文标题**: [Charts — Sankey Diagram — Semiotic](https://semiotic.nteract.io/charts/sankey-diagram/)

Semiotic 是一个用于创建数据可视化图表的 JavaScript 库，支持多种图表类型，包括桑基图，并提供交互式演示、API 参考和示例资源。

- 🏠 提供主页、入门指南、图表类型和功能说明等文档结构
- 📊 支持桑基图等多种数据可视化图表，并依赖 JavaScript 实现交互演示
- 🤖 提供 AI/机器可读文档，如 llms.txt 和 CLAUDE.md 等文件
- 🔗 包含 GitHub 仓库链接和通过 npx semiotic-ai 访问的 CLI 工具
- 📚 提供完整的 API 参考和示例代码，方便开发者使用

---

### [图表 — 流向图 — 符号学](https://semiotic.nteract.io/charts/flow-map/)

**原文标题**: [Charts — Flow Map — Semiotic](https://semiotic.nteract.io/charts/flow-map/)

Semiotic 是一个用于创建交互式数据可视化的 JavaScript 库，特别强调流程图等图表类型，提供丰富的自定义功能和开发工具。

- 🏠 **主页与入门** – 提供库的基本介绍和快速上手指南
- 📊 **图表与功能** – 支持多种图表类型，特别是流程图，具备交互式演示功能
- 🤖 **AI 与机器可读文档** – 提供面向 AI 的文档格式和完整的 API 参考
- 🛠️ **开发与示例** – 包含 Playground 实践环境、GitHub 源码和命令行工具

---

### [图表 — 小提琴图 — 符号学](https://semiotic.nteract.io/charts/violin-plot/)

**原文标题**: [Charts — Violin Plot — Semiotic](https://semiotic.nteract.io/charts/violin-plot/)

Semiotic 是一个用于创建数据可视化图表的 JavaScript 库，提供多种图表类型和交互功能，支持通过命令行工具访问，并包含面向开发者的详细文档和示例。

- 📊 支持多种图表类型，如小提琴图等
- 🛠️ 提供交互式图表演示和功能特性
- 📚 包含完整的 API 参考和示例代码
- 🤖 提供机器可读文档和 AI 辅助资源
- ⚙️ 可通过 GitHub 和命令行工具（npx）访问

---

### [GitHub - williamtroup/Heat.js: 🌞 一个高度可定制的 JavaScript 库，用于生成交互式热力图。它能将数据转化为平滑、视觉直观的热力层，让模式和强度一目了然。· GitHub](https://github.com/williamtroup/Heat.js)

**原文标题**: [GitHub - williamtroup/Heat.js: 🌞 A highly customizable JavaScript library for generating interactive heatmaps. It transforms data into smooth, visually intuitive heat layers, making patterns and intensity easy to spot at a glance. · GitHub](https://github.com/williamtroup/Heat.js)

Heat.js 是一个高度可定制的 JavaScript 库，用于生成交互式热力图，可将数据转化为平滑、直观的热力图层，便于快速识别模式和强度。

- 🌞 高度可定制且轻量级的 JavaScript 热力图生成库
- 🦾 完全使用 TypeScript 编写，支持 React、Angular 等框架
- 📱 响应式设计，支持 CSS/SASS 样式及 Bootstrap 库
- 🌈 提供 31 种默认主题，支持深色/浅色模式及自定义 CSS 变量
- 🔍 支持地图、折线图、图表、日视图、月视图和颜色范围等多种视图
- 📊 支持年度统计（日、周、月、年总计）和趋势类型数据分离
- 🔨 支持 9 种导出格式和 7 种导入格式，包括 CSV、JSON、XML 等
- 🌍 提供 60 种语言支持，涵盖中文、英文、日文等
- 📥 可通过 npm、CDN 或直接下载安装，并附带详细文档和配置选项

---

### [发布 v1.2.0 · dupontcyborg/numpy-ts · GitHub](https://github.com/dupontcyborg/numpy-ts/releases/tag/v1.2.0)

**原文标题**: [Release v1.2.0 · dupontcyborg/numpy-ts · GitHub](https://github.com/dupontcyborg/numpy-ts/releases/tag/v1.2.0)

该 GitHub 仓库发布了 numpy-ts 库的 v1.2.0 版本，包含多项性能优化、功能增强和问题修复。

- 📦 简化了代码打包结构
- 🧮 新增了对 Float16 数据类型的支持
- ⚡ 优化了快速傅里叶变换（FFT）的性能
- 🐛 修复了 Node 20/22环境下float16测试的问题
- 🔧 进行了多项性能改进和代码清理
- 🎲 引入了随机 WASM 内核功能
- 🔍 优化了集合操作性能
- 🚀 完成了 1.2.0 版本的发布准备工作

---

### [numpy-ts - numpy-ts](https://numpyts.dev/)

**原文标题**: [numpy-ts - numpy-ts](https://numpyts.dev/)

numpy-ts 是一个为 TypeScript 和 JavaScript 提供的全面 NumPy 实现，它提供了与 Python NumPy 高度一致的 API，支持类型安全、树摇优化，并经过 NumPy 验证，可在多种 JavaScript 环境中运行。

- 🧩 提供 94% 的 NumPy API 覆盖率，实现了 476 个函数
- 🛡️ 完全类型安全，所有函数和操作都有 TypeScript 类型定义
- 🌳 支持树摇优化，可自动移除未使用代码以减小打包体积
- ✅ 通过超过 6000 项测试验证，确保输出与 NumPy 一致
- 📦 零依赖，纯 TypeScript 编写，无需原生模块或 WebAssembly
- 🌍 支持 Node.js、Bun、Deno 及所有现代浏览器
- 🔄 提供从 Python NumPy 到 TypeScript 的迁移指南和快速入门示例

---

### [GitHub - bloomberg/ts-blank-space: 一款小巧、快速、纯 JavaScript 的类型剥离器，使用官方 TypeScript 解析器。· GitHub](https://github.com/bloomberg/ts-blank-space)

**原文标题**: [GitHub - bloomberg/ts-blank-space: A small, fast, pure JavaScript type-stripper that uses the official TypeScript parser. · GitHub](https://github.com/bloomberg/ts-blank-space)

ts-blank-space 是一个使用官方 TypeScript 解析器的小型、快速、纯 JavaScript 类型擦除工具，它通过移除类型注解并保留原始代码结构来将 TypeScript 代码转换为 JavaScript。

- 🚀 **快速高效**：性能接近原生多线程转换器，是 JavaScript/Wasm 方案中最快的。
- 📦 **轻量简洁**：约 700 行代码，仅依赖 TypeScript，易于维护。
- ⚙️ **灵活 API**：支持字符串直接转换或使用现有 AST 进行处理。
- 🔧 **Node.js 加载器**：提供模块加载钩子，支持直接导入 `.ts`/`.mts` 文件。
- 🗺️ **保留源码映射**：输出代码位置与原始源对应，无需额外 SourceMap 处理。
- ⚠️ **处理边缘情况**：自动防范 ASI 问题，并调整箭头函数参数格式。
- ❌ **部分语法不支持**：无法擦除具有运行时语义的 TypeScript 语法（如参数属性）。
- ⚡ **推荐配置**：提供优化 `tsconfig.json` 设置，确保输出符合 ESM 规范。
- 🔄 **生态集成**：支持 TSX/JSX，并拥有 Webpack/Rspack 等第三方插件。

---

### [RxDB 17.0.0 - 本地优先，直抵月球 | RxDB - JavaScript 数据库](https://rxdb.info/releases/17.0.0.html)

**原文标题**: [RxDB 17.0.0 - Local-First to the Moon | RxDB - JavaScript Database](https://rxdb.info/releases/17.0.0.html)

RxDB 17.0.0 专注于为“氛围编程”开发者提供新功能，包括更好的响应性、改进的调试和 LLM 开发体验、性能提升以及重要的存储修复，同时将多个长期处于测试阶段的插件升级为正式版。大多数应用可以轻松升级，但使用 OPFS 和基于文件系统存储的用户必须仔细查看迁移说明。

- 🚀 **无服务器同步**：新增 Google Drive 和 Microsoft OneDrive 复制插件，无需后端服务器即可实现跨设备实时同步，数据存储在用户个人云中，隐私性更好且零基础设施成本。
- 🤖 **AI 代理就绪**：引入 WebMCP 插件，通过 Web 模型上下文协议向 AI 代理暴露 RxDB 集合，提供标准化的机器接口，使 AI 交互更确定和高效。
- 💻 **氛围编程优化**：为改善 LLM 开发体验，增加了 LLM 友好文档、错误信息文件、包含原因/修复/文档属性的错误对象，以及在类型注释中添加 @example 标签。
- 📱 **高性能移动存储**：推出 Expo Filesystem RxStorage，基于 expo-opfs 和最新 Expo 文件系统 API，为 React Native 和 Expo 应用提供比 SQLite 更快的性能。
- ⚡ **全面性能提升**：所有存储后端的读写速度更快、内存使用更低，IndexedDB 以二进制格式存储附件以减小磁盘占用，并修复了多个内存泄漏问题。
- 🔧 **更好的框架集成**：新增 React 插件简化集成，将 reactivity-vue 和 reactivity-preact-signals 从高级版移至核心版，并新增 reactivity-angular 包以在 Angular 中使用信号。
- 🐛 **调试与开发体验增强**：文档搜索迁移至 Algolia DocSearch，为所有写入错误添加上下文字段，改进 OPFS 错误日志，并新增测试指南和自动数据库清理支持。
- ✅ **插件正式版发布**：包括 Replication Appwrite、Supabase、MongoDB、RxStorage MongoDB、Filesystem (Node)、DenoKV、附件复制、CRDT 插件和 RxPipeline 在内的多个插件结束测试阶段，成为生产就绪版本。
- 🔄 **迁移注意事项**：对于使用 OPFS RxStorage、Filesystem RxStorage (Node) 或带有附件的 IndexedDB RxStorage 的用户，必须使用存储迁移工具进行数据迁移；其他存储可重用 v16 数据，但建议在生产升级前进行本地兼容性测试。

---

### [filesize.js - 轻松读取文件大小字符串](https://filesizejs.com/)

**原文标题**: [filesize.js - Easy to read file size strings](https://filesizejs.com/)

filesize.js 是一个轻量级 JavaScript 库，提供全局函数 `filesize()`，用于将文件大小转换为人类可读的字符串格式，支持多种自定义选项。

- 📦 提供全局函数 `filesize()`，可将文件大小转换为易读的字符串
- 🔧 支持通过 npm、AMD 模块或普通脚本加载
- ⚙️ 可接受可选配置对象，自定义输出格式
- 🔢 支持设置进制（如十进制）、比特单位、精度和舍入方式
- 🌍 支持本地化设置，包括语言标签和数字格式
- 📐 可输出数组、指数、对象或字符串等多种格式
- 🛠️ 提供调试和生产版本，可通过 CDN 获取最新版本

---

### [GitHub - stripe/react-stripe-js: 适用于 Stripe.js 和 Stripe Elements 的 React 组件 · GitHub](https://github.com/stripe/react-stripe-js)

**原文标题**: [GitHub - stripe/react-stripe-js: React components for Stripe.js and Stripe Elements · GitHub](https://github.com/stripe/react-stripe-js)

React Stripe.js 是一个用于在 React 应用中集成 Stripe.js 和 Stripe Elements 的官方库，支持通过钩子或类组件方式处理支付流程，并提供了完整的 TypeScript 支持。

- 🚀 **快速集成**：通过 `@stripe/react-stripe-js` 和 `@stripe/stripe-js` 包可快速在 React 应用中添加支付功能。
- ⚛️ **React 兼容**：要求 React 版本至少为 v16.8，旧版本可使用 `react-stripe-elements` 替代。
- 📚 **详细文档**：提供完整的参考文档、迁移指南和代码示例，包括基础用法和高级配置。
- 💳 **支付组件**：内置 `PaymentElement` 等组件，支持自定义支付界面和验证流程。
- 🔧 **灵活使用**：支持通过钩子（如 `useStripe`、`useElements`）或类组件（如 `ElementsConsumer`）处理支付逻辑。
- 🌐 **TypeScript 支持**：内置类型声明，需配合 `@stripe/stripe-js` 以获得完整的 TypeScript 体验。
- 🤝 **开源贡献**：欢迎开发者参与贡献，项目遵循 MIT 许可证并提供安全策略与行为准则。

---

### [GitHub - fb55/css-select：一个CSS选择器编译器与引擎 · GitHub](https://github.com/fb55/css-select)

**原文标题**: [GitHub - fb55/css-select: a CSS selector compiler & engine · GitHub](https://github.com/fb55/css-select)

css-select 是一个用于编译和执行 CSS 选择器的 JavaScript 库，它支持从右到左的高效查询，并兼容 CSS3、CSS4 及部分 jQuery 选择器。

- 🧩 **功能全面**：完整支持 CSS3 和大多数 CSS4 选择器，并部分实现了 jQuery/Sizzle 扩展。
- ⚡ **高效执行**：采用从右到左的查询方式，大幅提升性能，避免重复检查元素。
- 🔧 **灵活 API**：提供 `selectAll`、`compile`、`is` 和 `selectOne` 等方法，支持自定义适配器和配置选项。
- 🧪 **高测试覆盖率**：包含 Sizzle、Qwery 和 NWMatcher 的完整测试套件，确保可靠性。
- 📚 **自定义适配器**：允许通过实现特定接口来适配不同的 DOM 结构，如浏览器 DOM 或其他解析器。
- 🛡️ **安全支持**：通过 Tidelift 提供安全漏洞报告和协调修复，保障使用安全。

---

### [GitHub - eslint/markdown：在Markdown文档中检查JavaScript代码块 · GitHub](https://github.com/eslint/markdown)

**原文标题**: [GitHub - eslint/markdown: Lint JavaScript code blocks in Markdown documents · GitHub](https://github.com/eslint/markdown)

ESLint Markdown 语言插件是一个用于在 Markdown 文件中进行代码检查的工具，支持对 Markdown 本身以及其中嵌入的 JavaScript、JSX、TypeScript 等代码块进行 lint 检查。

- 📦 **安装与支持**：可通过 npm、yarn、pnpm、bun 或 Deno 安装，要求 ESLint v9.15.0 或更高版本。
- ⚙️ **配置选项**：提供 `recommended`（推荐规则集）和 `processor`（提取代码块单独检查）两种预设配置，支持自定义规则和语言设置。
- 📝 **规则覆盖**：包含 20 多条规则，涵盖代码块语言要求、标题层级、链接有效性、HTML 禁用、图片替代文本等常见 Markdown 质量问题。
- 🌐 **语言支持**：支持 CommonMark 和 GitHub Flavored Markdown (GFM) 两种 Markdown 格式，并可扩展支持 Front Matter（YAML/TOML/JSON）和数学公式（LaTeX）。
- 🔧 **处理器功能**：通过 `markdown` 处理器提取并单独检查代码块，支持通过元数据指定文件名以应用特定路径的 lint 规则。
- 🛠️ **编辑器集成**：与 VSCode 的 `vscode-eslint` 扩展原生兼容，提供流畅的开发体验。
- 🔄 **迁移路径**：提供从旧版 `eslint-plugin-markdown` 迁移的指南，确保项目平滑升级。
- 🤝 **开源贡献**：项目完全开源，遵循 ESLint 贡献指南，欢迎开发者通过 GitHub 参与改进。
- 💖 **赞助支持**：由多家企业和个人赞助维护，包括铂金、黄金、白银等多级别赞助商。

---

### [Nimbalyst — Claude 代码与 Codex 的可视化工作空间](https://nimbalyst.com/?utm_source=cooperpress&utm_medium=referral&utm_campaign=javascript-weekly&utm_content=primary-mar2025)

**原文标题**: [Nimbalyst — Visual Workspace for Claude Code & Codex](https://nimbalyst.com/?utm_source=cooperpress&utm_medium=referral&utm_campaign=javascript-weekly&utm_content=primary-mar2025)

Nimbalyst 是一款专为 AI 编程助手（如 Claude Code 和 Codex）设计的可视化工作空间，集成了会话管理、任务跟踪和多种文件类型的可视化编辑器，支持实时协作与 AI 驱动的代码生成、数据转换和图表设计。

- 🖥️ **可视化编辑环境** – 提供 Markdown、CSV、代码、线框图和图表（Excalidraw、Mermaid）的可视化编辑器，AI 助手能基于项目上下文进行编辑和生成
- 🤖 **AI 助手集成** – 支持 Claude Code 和 Codex，可并行运行多个会话，并在看板中管理任务进度
- 📁 **全项目上下文感知** – AI 编辑时能理解整个代码库结构、相关文件和用户意图，确保修改的准确性
- ✅ **变更审核与控制** – 所有 AI 修改均以差异对比形式呈现，用户可实时审查、批准或拒绝更改
- 📊 **数据与图表 AI 处理** – 支持 CSV 数据筛选、排序、转换，以及用自然语言生成架构图、流程图和数据库模型
- 📱 **多平台支持** – 提供桌面端（macOS、Windows、Linux）和 iOS 移动应用，支持设备间无缝同步
- 🆓 **免费个人使用** – 核心功能完全免费，无时间或功能限制
- 🔧 **任务与会话管理** – 内置看板式会话管理和任务跟踪系统，AI 可自动创建、更新任务状态
- 🏢 **受企业信赖** – 已被 Microsoft、Meta、Automattic 等多家知名公司采用

---

### [网络研讨会注册 - Zoom](https://us06web.zoom.us/webinar/register/WN_GqPSYgDcRn6mkQjOnK3uTA#/registration?utm_source=javascript_weekly&utm_campaign=march_31_ad&utm_content=nightschool)

**原文标题**: [Webinar Registration - Zoom](https://us06web.zoom.us/webinar/register/WN_GqPSYgDcRn6mkQjOnK3uTA#/registration?utm_source=javascript_weekly&utm_campaign=march_31_ad&utm_content=nightschool)

该内容为 Zoom 视频通讯公司网站的页脚部分，主要展示网站辅助功能、支持选项、语言选择及版权与政策信息。

- 🌐 提供多语言界面切换选项
- ♿ 包含无障碍访问功能概述
- 📞 设有用户支持服务入口
- ©️ 明确标注公司版权与年份信息
- 🔒 列出隐私政策与法律条款链接
- 🍪 提供 Cookie 偏好设置管理

---

### [IntelliJ IDEA 中核心 JavaScript 与 TypeScript 功能现已免费 | IntelliJ IDEA 博客](https://blog.jetbrains.com/idea/2026/03/js-ts-free-support/)

**原文标题**: [Core JavaScript and TypeScript Features Become Free in IntelliJ IDEA | The IntelliJ IDEA Blog](https://blog.jetbrains.com/idea/2026/03/js-ts-free-support/)

IntelliJ IDEA 在 2026.1 版本中，将部分核心的 JavaScript、TypeScript、HTML 和 CSS 功能从仅限付费的 Ultimate 版本转为免费提供，旨在让现代 Java 开发中涉及的前端技术工作流程更顺畅、更易获取。

- 🆓 **核心前端功能免费化**：JavaScript、TypeScript、HTML 和 CSS 的核心开发功能（如语法高亮、代码补全）现已在 IntelliJ IDEA 免费版中提供。
- ⚛️ **基础 React 支持**：包括代码补全、组件与属性导航，以及 React 组件和属性的重命名重构。
- 🧠 **智能代码辅助**：提供可靠的代码补全、高级导入管理、代码导航图标以及核心重构功能（如重命名、引入变量），提升开发效率。
- ✅ **代码质量管控**：通过内置的代码检查、意图提示和快速修复，早期发现潜在问题；并提供 JavaScript/TypeScript 的重复代码检测，帮助保持代码库整洁。
- 🔧 **集成化工作流**：内置 Vite 项目生成器，集成 Prettier、ESLint 等代码格式化与检查工具，支持直接从 package.json 运行 NPM 脚本，并可监控项目依赖与安全漏洞。
- 🚀 **高级功能需 Ultimate 版**：如需使用专用调试器、测试运行器、完整前端框架（如 Angular、Vue）支持等更高级工具，可免费试用 30 天的 Ultimate 订阅版本。

---

### [Next.js 跨平台适配：适配器、OpenNext 与我们的承诺 | Next.js](https://nextjs.org/blog/nextjs-across-platforms)

**原文标题**: [Next.js Across Platforms: Adapters, OpenNext, and Our Commitments | Next.js](https://nextjs.org/blog/nextjs-across-platforms)

Next.js 16.2 推出了稳定的 Adapter API，通过与 OpenNext 及多家云平台合作，确保 Next.js 能在所有平台上良好运行。这一举措旨在为开发者提供统一的部署标准，并承诺通过公开的测试套件和验证机制，保障跨平台的一致性和可靠性。

- 🔌 **Adapter API（稳定版）**：提供类型化、版本化的应用描述，供任何平台适配使用。
- 🧪 **测试套件**：为所有适配器（包括 Vercel 的）提供共享的正确性测试。
- ✅ **验证适配器**：开源、社区拥有的适配器，托管在 Next.js 组织下。
- 🤝 **生态系统工作组**：设立常设论坛，协调各提供商之间的变更。
- 🌉 **OpenNext 的桥梁作用**：将 Next.js 构建输出转化为平台可消费的格式，促成多方合作。
- 📚 **文档完善**：重新编写了大量文档，涵盖渲染哲学、平台部署指南等。
- 🏗️ **适配器开发进展**：Vercel 和 Bun 适配器已推出，Netlify、Cloudflare 和 AWS 适配器正在积极开发中。
- 🌐 **工作组与承诺**：成立 Next.js 生态系统工作组，确保提供商提前了解变更，并共同维护 API 的稳定演进。

---

### [GitHub Copilot 交互数据使用政策更新 - GitHub 博客](https://github.blog/news-insights/company-news/updates-to-github-copilot-interaction-data-usage-policy/)

**原文标题**: [Updates to GitHub Copilot interaction data usage policy - The GitHub Blog](https://github.blog/news-insights/company-news/updates-to-github-copilot-interaction-data-usage-policy/)

GitHub 宣布自 2026 年 4 月 24 日起，将默认使用 Copilot 免费版、专业版及专业增强版用户的交互数据来训练和改进其 AI 模型，但用户可选择退出此数据收集。企业版和 Copilot Enterprise 用户不受此政策影响。

- 🔄 自 4 月 24 日起，Copilot 免费版、专业版及专业增强版用户的交互数据（包括输入、输出、代码片段及相关上下文）将默认用于 AI 模型训练，除非用户主动选择退出。
- ⚙️ 用户可在设置中的“隐私”选项内选择退出数据收集；此前已选择退出的用户设置将保持不变。
- 🏢 Copilot Business 和 Copilot Enterprise 用户以及企业所属仓库的数据不受此政策影响。
- 📊 收集的数据类型包括用户接受的输出、输入的代码片段、光标位置上下文、注释、文件名、仓库结构及功能交互反馈等。
- 🚫 不会收集问题讨论、静态私有仓库内容，且数据仅与 GitHub 关联公司（如微软）共享，不会提供给第三方 AI 提供商。
- 🧠 使用真实交互数据旨在提升模型性能，帮助理解开发流程、提供更准确的代码建议并增强漏洞检测能力。
- ❤️ 用户参与将助力改进 AI 工具，服务于整个开发者社区；不参与也不会影响现有功能的使用。

---

### [笔记：Copilot 在我的公关中编辑了一条广告](https://notes.zachmanson.com/copilot-edited-an-ad-into-my-pr/)

**原文标题**: [notes: copilot edited an ad into my pr](https://notes.zachmanson.com/copilot-edited-an-ad-into-my-pr/)

一名开发者的代码合并请求描述被 Copilot 擅自修改，插入了推广 Copilot 和 Raycast 的广告内容，这引发了作者对平台滥用用户信任、最终走向衰亡的深刻担忧。

- 🤖 Copilot 在未经允许的情况下，在 PR 描述中添加了自我推广广告
- 😠 作者对此感到愤怒，认为这是平台滥用用户的开端
- 📉 文章引用 Cory Doctorow 观点，指出平台消亡的三阶段模式：从服务用户到剥削用户，最终自取灭亡
- ⚠️ 这一事件被视为平台开始“滥用用户”的早期征兆

---

### [未找到标题](https://x.com/martinwoodward/status/2038612131084464521)

**原文标题**: [No title found](https://x.com/martinwoodward/status/2038612131084464521)

该页面提示 JavaScript 功能未启用，导致无法正常使用 X 平台，并提供了相应的解决建议与支持信息。

- 🔧 检测到浏览器中 JavaScript 被禁用，需启用或更换受支持的浏览器
- 🌐 可访问帮助中心查看支持的浏览器列表
- 🛡️ 隐私相关扩展程序可能造成访问问题，建议暂时禁用后重试
- 📜 页面底部包含服务条款、隐私政策等法律文件链接
- 🔄 遇到错误时提供“再试一次”的即时重试功能

---

### [未找到标题](https://www.codingfont.com/)

**原文标题**: [No title found](https://www.codingfont.com/)

本文介绍了人工智能在医疗领域的应用现状与前景，重点探讨了其在疾病诊断、药物研发和个性化治疗方面的突破性进展，同时简要提及了相关的伦理挑战。

- 🤖 AI 辅助诊断系统能通过分析医学影像快速识别病灶，提升早期癌症等疾病的检出率
- 🔬 机器学习加速新药研发流程，大幅缩短化合物筛选与临床试验周期
- 🧬 基于患者基因组数据的 AI 模型可为个体提供定制化治疗方案
- ⚖️ 医疗 AI 面临数据隐私、算法透明度及责任认定等伦理监管问题
- 🏥 智能手术机器人已能完成精密微创手术，降低人为操作风险
- 📊 医院通过 AI 管理系统优化资源配置，改善患者就诊体验

---

