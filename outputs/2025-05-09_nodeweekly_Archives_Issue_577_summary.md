### [Node 周刊第 577 期：2025 年 5 月 6 日](https://nodeweekly.com/issues/577)

**原文标题**: [Node Weekly Issue 577: May 6, 2025](https://nodeweekly.com/issues/577)

Node.js 最新动态与技术资讯速览  

- 🚀 **Node 24 发布**：v24 成为最新当前版本，包含 npm 11、V8 13.6 等新特性，如 `RegExp.escape` 和 `Float16Array`。  
- 🤖 **AI 代理开发课程**：Frontend Masters 提供视频教程，教你构建 AI 代理，涵盖 LLM、聊天历史管理等。  
- 📊 **Node.js 未来十年调查**：Node.js 核心团队邀请开发者参与“Next 10”战略方向调查。  
- 🐇 **Bun v1.2.12 更新**：增强 Node.js 兼容性，支持浏览器控制台日志流式传输。  
- 🦕 **Deno 2.3 发布**：改进单二进制编译功能，支持 FFI 和本地 npm 包。  
- 🏛️ **OpenJS 基金会新董事会**：包括 Jordan Harband 和 Matteo Collina 等知名人士。  
- 📚 **Llama Stack 与 Node 结合**：Meta 的 Llama Stack 提供现代 LLM 堆栈 API，支持 RAG。  
- 🔍 **JavaScript 字符串转换**：Dr. Axel 探讨 JavaScript 中值到字符串转换的复杂性。  
- 🔌 **企业 SSO 快速集成**：Scalekit 的 Node SDK 支持 SAML 和 OIDC SSO，无需重写代码。  
- 🛠️ **新 Kafka 客户端**：Platformatic 发布基于现代 Node 最佳实践的 Kafka 客户端。  
- 📦 **WASM 版 Postgres**：PGlite 0.3 支持在浏览器或 Node 中运行 Postgres。  
- 📄 **Electron 辩护**：文章反驳对 Electron 的常见批评。  
- ⚠️ **npm 恶意软件活动**：Socket 发现模仿知名库的恶意软件活动。  
- 🔄 **ECMAScript 新提案**：显式资源管理提案已在 Chrome 134+ 和 Node 24 中实现。  
- 🎨 **GSAP 免费商用**：GSAP 动画库现在完全免费，包括商业用途。  
- 🔍 **Redis 重新开源**：Redis 8.0 恢复开源许可。

---

### [Node.js — Node v24.0.0（当前版本）](https://nodejs.org/en/blog/release/v24.0.0)

**原文标题**: [Node.js — Node v24.0.0 (Current)](https://nodejs.org/en/blog/release/v24.0.0)

Node.js v24.0.0 是一个重要的当前版本发布，带来了多项显著更新和改进，包括 V8 引擎升级、npm 更新、权限模型改进等。该版本将在 10 月进入长期支持（LTS）阶段。

- 🚀 **V8 引擎升级至 13.6**：新增`Float16Array`、显式资源管理、`RegExp.escape`等 JavaScript 特性。
- 📦 **npm 11**：提升性能、安全性和现代 JavaScript 包的兼容性。
- 🔄 **AsyncLocalStorage 默认使用 AsyncContextFrame**：提供更高效的异步上下文跟踪实现。
- 🌐 **URLPattern 全局可用**：无需显式导入即可使用强大的 URL 模式匹配 API。
- 🔒 **权限模型改进**：实验性标志`--experimental-permission`改为`--permission`，表明其稳定性增强。
- 🧪 **测试运行器增强**：自动等待子测试完成，减少未处理 Promise 的常见错误。
- ⚡ **Undici 7**：HTTP 客户端能力提升，支持更多新 HTTP 特性。
- 🗑️ **废弃和移除的 API**：包括`url.parse()`、`tls.createSecurePair`等。
- 🛠️ **Windows 编译要求变更**：不再支持 MSVC，需使用 ClangCL 编译 Node.js。
- 📅 **长期支持计划**：Node.js 24 将在 2023 年 10 月进入 LTS 阶段。

---

### [Node.js — Node.js 版本发布](https://nodejs.org/en/about/previous-releases)

**原文标题**: [Node.js — Node.js Releases](https://nodejs.org/en/about/previous-releases)

Node.js 的版本发布分为 Current、Active LTS 和 Maintenance LTS 三个阶段，奇数版本在 6 个月后停止支持，偶数版本进入长期支持阶段。生产环境应使用 Active LTS 或 Maintenance LTS 版本。官方和社区提供了多种安装方法，需满足特定标准。

- 🚀 Node.js 主要版本发布后，奇数版本（如 9、11）6 个月后停止支持，偶数版本（如 10、12）进入 Active LTS 阶段，适合生产环境使用。
- 🛡️ LTS（长期支持）版本提供 30 个月的关键 bug 修复，确保稳定性。
- 📅 详细发布计划可在 GitHub 上查看，各版本状态（如 Current、LTS、End-of-life）及时间线明确列出。
- 💼 商业支持可通过 OpenJS 合作伙伴 HeroDevs 获取，适用于 Maintenance 阶段之后的版本。
- 📥 官方安装方法需满足严格标准，如下载官方二进制文件、与 Node.js 项目保持紧密联系等。
- 🌍 社区安装方法需支持所有非 EOL 版本，兼容至少一个官方操作系统，且必须免费开源。
- 🔄 安装方法分类为“官方”和“社区”，提供更多选择和灵活性。

---

### [URLPattern - Web API 接口 | MDN](https://developer.mozilla.org/en-US/docs/Web/API/URLPattern)

**原文标题**: [URLPattern - Web APIs | MDN](https://developer.mozilla.org/en-US/docs/Web/API/URLPattern)

URLPattern 是 URL Pattern API 提供的接口，用于匹配 URL 或其部分内容，支持通过捕获组提取匹配部分。该技术目前处于实验阶段，兼容性有限，需谨慎在生产环境中使用。

- 🌐 **URLPattern 接口**：用于匹配 URL 或部分 URL，支持捕获组提取内容。  
- ⚠️ **实验性技术**：尚未广泛支持，使用前需检查浏览器兼容性。  
- 🔧 **构造函数**：`URLPattern()` 根据给定模式和基础 URL 创建新对象。  
- 📌 **实例属性**：包括 `hash`、`hostname`、`password`、`pathname`、`port`、`protocol`、`search` 和 `username`，分别匹配 URL 的各个部分。  
- 🔍 **实例方法**：  
  - `exec()`：返回匹配的 URL 部分对象，不匹配则返回 `null`。  
  - `test()`：返回布尔值，表示 URL 是否匹配给定模式。  
- 📚 **相关资源**：  
  - 语法参考：[URL Pattern API](https://developer.mozilla.org/en-US/docs/Web/API/URL_Pattern_API)。  
  - GitHub 上有 [polyfill](https://github.com/kenchris/urlpattern-polyfill) 可用。  
- 📅 **最后更新**：2024 年 3 月 6 日，由 MDN 贡献者维护。

---

### [Node.js 未来十年调查 - 2025](https://linuxfoundation.research.net/r/2025nodenext10)

**原文标题**: [Node.js Next 10 Survey - 2025](https://linuxfoundation.research.net/r/2025nodenext10)

Node.js Next 10 调查问卷（2025 年）内容概览  

- 🌍 **居住地**：问卷包含全球所有国家/地区的选项，供参与者选择当前居住地。  
- 🗣️ **主要语言**：提供多种常见语言选项，包括英语、中文、西班牙语等，并支持填写其他语言。  
- ⏳ **Node.js 使用时长**：选项涵盖从 0 到 10 年以上的使用经验，通过滑动条调整输入。  
- 🏢 **组织类型**：包括学术界、企业、政府、自由职业者、非营利组织等类别。  
- 🏭 **公司所属行业**（如适用）：涵盖农业科技、金融、信息技术等多个领域。  
- 👥 **组织规模**：通过滑动条选择员工/成员数量（0 至 1000+ 人）。  
- 📄 **问卷进度**：当前为第 1 页（共 4 页），完成度 25%。  

（注：隐私与 Cookie 声明附在问卷末尾。）

---

### [GitHub - nodejs/next-10: Node.js 未来十年战略方向讨论仓库](https://github.com/nodejs/next-10)

**原文标题**: [GitHub - nodejs/next-10: Repository for discussion on strategic directions for next 10 years of Node.js](https://github.com/nodejs/next-10)

Node.js 社区正在讨论未来 10 年的战略发展方向，旨在延续其首个 10 年的成功。以下是关键信息：

- 🚀 **目标**：制定 Node.js 未来 10 年的战略方向  
- 📅 **会议安排**：每两周举行一次，议程会提前在仓库中发布  
- 📍 **会议日历**：可在 Node.js 日历中查看，标记为“Node.js Next 10 years”  
- 👥 **团队成员**：包括@BethGriggs、@bmeck、@bnb 等核心贡献者  
- 🏛 **组织结构**：包含活跃成员和荣誉成员（Emeritus）  
- 📂 **仓库内容**：涵盖会议记录、调查、行为准则、许可证等文件  
- 🔍 **更多背景**：详见nodejs/TSC#797议题  
- ⭐ **社区关注**：获得 517 颗星和 28 次分叉，显示高度关注  
- 📜 **许可证与行为准则**：明确规定了贡献规范和社区准则  

该仓库是开放协作的平台，旨在推动 Node.js 生态的长期发展。

---

### [Bun v1.2.12 | Bun 博客](https://bun.sh/blog/bun-v1.2.12)

**原文标题**: [Bun v1.2.12 | Bun Blog](https://bun.sh/blog/bun-v1.2.12)

Bun 1.2.12 版本发布，新增了--console 标志用于将浏览器控制台日志流式传输到终端，优化了前端开发服务器的内存使用，并改进了 Node.js 兼容性，包括定时器、vm、net、http 模块的改进，以及 TextDecoder 和热重载的可靠性修复。

- 🚀 新增 `--console` 标志，支持将浏览器控制台日志流式传输到终端，便于调试。
- 💾 开发服务器内存使用显著减少，从 272MB 降至 150MB。
- 🔧 修复了全局包 postinstall 脚本的运行问题，影响如 Claude Code 等流行包。
- ⚡ 启动速度微优化，提升了 30μs。
- 📅 Node.js 兼容性改进，98.4% 的`timers`测试通过，新增`vm.Script`的`cachedData`支持。
- 🛡️ 新增`net.BlockList`支持，允许阻止特定 IP 地址、范围或子网。
- 🔄 `node:http`模块多项边缘案例修复，包括`Agent`中止处理和 URL 参数传递。
- 🐛 修复了导入无效文件 URL 时可能导致的崩溃问题。
- 📖 `TextDecoder`编码标签处理改进，符合 WHATWG 规范，修复了`fatal`选项的强制转换问题。
- 🔥 热重载可靠性修复，解决了长时间运行后可能崩溃的问题。
- 🙏 感谢 10 位贡献者的贡献。

---

### [Deno 2.3：增强的 deno compile、本地 npm 包支持等](https://deno.com/blog/v2.3)

**原文标题**: [Deno 2.3: Improved deno compile, local npm packages, and more](https://deno.com/blog/v2.3)

Deno 2.3 版本带来了多项改进和新功能，包括增强的 deno compile、本地 npm 包支持、性能优化等。

- 🚀 **deno compile 改进**：支持 FFI 和 Node 原生插件，可生成包含本地库的独立二进制文件，并新增文件排除功能。
- 📦 **本地 npm 包支持**：通过 `deno.json` 配置本地 `node_modules`，方便开发和测试本地 npm 包。
- ✨ **deno fmt 增强**：支持格式化嵌入的 CSS、HTML 和 SQL，新增 14 种格式化选项。
- 📌 **deno add 注册表标志**：新增 `--npm` 和 `--jsr` 标志，方便从不同注册表安装包。
- 🔍 **OpenTelemetry 增强**：支持事件记录、跨服务追踪、`node:http` 自动插桩和 V8 引擎指标。
- 🔒 **Windows 代码签名**：Deno 可执行文件现已签名，提升 Microsoft Defender 信任度。
- 🧩 **deno check 更直观**：无需显式参数，默认检查当前目录下的文件。
- 📊 **测试覆盖率改进**：自动生成覆盖率报告，支持忽略注释和自定义输出目录。
- 📝 **Jupyter 笔记本类型检查**：改进变量和类型定义的共享，提升开发体验。
- ⚡ **依赖安装提速**：内存缓存 npm 包信息，避免重复缓存，安装速度提升约 2 倍。
- 🛠️ **显式资源管理**：支持 JavaScript 的 `using` 关键字，简化资源管理。
- 🚄 **性能优化**：`Deno.serve` 和 HTTP 服务器性能提升，LSP 内存占用减少。
- 🔄 **TypeScript 5.8 和 V8 13.5**：升级至最新版本，带来新特性和性能改进。
- 🌟 **其他生活质量改进**：包括强制彩色输出、支持 Linux vsock、WebGPU 方法等。

---

### [认识我们的 2025 年 OpenJS 基金会董事会 | OpenJS 基金会](https://openjsf.org/blog/openjs-board-directors-2025)

**原文标题**: [Meet Our 2025 OpenJS Foundation Board of Directors | OpenJS Foundation](https://openjsf.org/blog/openjs-board-directors-2025)

OpenJS 基金会 2025 年董事会成员更新，包括新成员加入与连任董事名单，涵盖黄金、白银及社区级别代表，共同推动基金会技术政策与发展方向。

- 🎉 欢迎新成员 Stephen Husak（Capital One）加入董事会，担任白银级别董事，拥有 30 年行业经验，擅长企业级 Node.js 架构。  
- 🔄 六名董事连任：Jordan Harband（黄金）、Abby Cabunoc Mayes（白银）、Adrian Estrada（终端用户）、Matteo Collina 等（CPC 社区代表）。  
- 🏛️ 董事会组成规则：白金成员直接任命董事，黄金/白银成员投票选举代表，社区董事由跨项目委员会（CPC）推选。  
- 🌟 现有白金董事包括 IBM、Microsoft 和 Joyent 的代表，共同制定基金会技术愿景与政策方向。  
- 💡 Stephen Husak 曾主导 Capital One 呼叫中心平台向云端 Node.js 架构迁移，并积极推动开源技术在企业中的应用。  
- 🙌 基金会感谢所有董事的服务，期待其为 JavaScript 生态发展贡献力量。

---

### [使用 Llama Stack 和 Node.js 实现检索增强生成 | Red Hat 开发者](https://developers.redhat.com/articles/2025/04/30/retrieval-augmented-generation-llama-stack-and-nodejs)

**原文标题**: [Retrieval-augmented generation with Llama Stack and Node.js | Red Hat Developer](https://developers.redhat.com/articles/2025/04/30/retrieval-augmented-generation-llama-stack-and-nodejs)

本文介绍了如何使用 Node.js 和 Llama Stack 实现检索增强生成（RAG）技术，以提升大型语言模型的应用效果。

- 🚀 **检索增强生成（RAG）概述**：RAG 通过将外部数据转换为向量并存储在数据库中，为模型提供上下文信息，从而生成更准确的回答。
- 📂 **数据处理**：将 Node.js 参考架构的 Markdown 文件转换为适合模型处理的格式，并分块存储。
- 🔍 **向量数据库**：使用 Chroma 等向量数据库存储数据，通过查询匹配向量检索相关文档块。
- 💡 **模型优化**：仅传递最相关的文档块，避免上下文过大导致的成本增加和性能下降。
- 🛠️ **Llama Stack 设置**：通过容器运行 Llama Stack 实例，并指向现有的 Ollama 服务器。
- 📦 **模型支持**：Llama Stack 现在支持更多模型，包括量化模型，提高了灵活性和运行效率。
- 📝 **文档处理**：读取并转换 Markdown 文件为文本，使用 Llama Stack API 将文档块插入向量数据库。
- ❓ **查询与回答**：通过查询向量数据库获取相关文档块，构建提示并发送给模型生成回答。
- 🤖 **代理使用**：Llama Stack 的代理功能简化了 RAG 的使用，自动调用工具获取相关信息。
- ⚖️ **代理与 API 比较**：代理使用更简便，但底层 API 提供更多控制，适合不同需求和资源场景。
- 📚 **学习资源**：提供了更多关于 Node.js 和 AI 开发的教程和资源链接。

---

### [Llama Stack — llama-stack 文档](https://llama-stack.readthedocs.io/en/latest/)

**原文标题**: [Llama Stack — llama-stack  documentation](https://llama-stack.readthedocs.io/en/latest/)

Llama Stack 是一个开源框架，用于构建生成式 AI 应用，提供统一的 API 层、插件架构和多种开发者接口，支持从开发到生产的无缝过渡。

- 🚀 **快速开始**  
  - 安装与设置  
  - 运行 Llama Stack 服务器  
  - 运行演示  

- 📚 **详细教程**  
  - 安装与配置  
  - 运行 Llama Stack  
  - 客户端 CLI 使用  
  - 运行演示  

- ❓ **为什么选择 Llama Stack？**  
  - 提供通用技术栈和核心概念  
  - 支持开放基准评测  

- 🔧 **核心功能**  
  - API 提供者（如推理、向量存储、安全等）  
  - 资源管理（数据集、评估、推理等）  
  - 代理工具与安全防护  

- 🏗️ **部署与扩展**  
  - 库模式使用  
  - Kubernetes 部署指南  
  - 自定义分发构建  

- 🤖 **AI 应用示例**  
  - 检索增强生成（RAG）  
  - 代理配置与工具调用  

- 📊 **评估与监控**  
  - 应用评估与代理响应评测  
  - 遥测数据跟踪（Jaeger、SQLite）  

- 🎮 **Llama Stack Playground**  
  - 聊天机器人、评估与调试功能  

- 👥 **贡献指南**  
  - 问题讨论、开发环境设置、代码风格  

- 📜 **参考文档**  
  - API 参考、Python SDK、CLI 命令  

- 🔗 **支持的技术与提供商**  
  - 推理 API（Meta、Ollama、Fireworks 等）  
  - 向量存储（FAISS、Chroma、Milvus 等）  
  - 安全 API（Llama Guard、AWS Bedrock 等）  

- 🌟 **最新动态**  
  - Llama Stack 0.2.5 版本发布  
  - 支持多语言客户端 SDK（Python、Swift、Node、Kotlin）

---

### [Node.js 开发者实用指南：Llama Stack | Red Hat 开发者](https://developers.redhat.com/articles/2025/04/02/practical-guide-llama-stack-nodejs-developers)

**原文标题**: [A practical guide to Llama Stack for Node.js developers | Red Hat Developer](https://developers.redhat.com/articles/2025/04/02/practical-guide-llama-stack-nodejs-developers)

概述：本文介绍了 Node.js 开发者如何利用 Llama Stack 框架与大型语言模型（LLM）进行交互，包括工具调用、代理 API 使用以及 MCP 协议的集成方法。

- 🚀 Node.js 团队探索了如何通过 JavaScript/TypeScript 和 Llama Stack 框架调用大型语言模型（LLM），并比较了不同框架的易用性和效果。  
- 🔧 Llama Stack 的核心特点是标准化 API 和插件化设计，支持多种发行版，开发者可选择适合的发行版进行实验（如基于 Ollama 的参考发行版）。  
- 🐳 通过 Podman 容器快速部署 Llama Stack 实例，并配置与现有 Ollama 服务器的连接，使用`meta-llama/Llama-3.1-8B-Instruct`模型进行测试。  
- 📚 利用 Llama Stack 的`/docs`端点交互式探索 API 文档，辅助理解自动生成的 TypeScript 客户端的使用方法。  
- 💡 示例应用演示了工具调用流程：定义本地工具（如查询喜好颜色/冰球队），通过补全 API 处理用户问题，并优化工具响应格式以提升交互效果。  
- 🔄 发现 Llama 3.1 模型对工具的强依赖性问题——即使问题与工具无关，模型仍尝试调用工具，导致部分回答受限。  
- 🤖 集成 MCP 协议：将工具封装为 MCP 服务后，通过 Llama Stack 代理 API 调用远程工具，简化了工具管理但牺牲了调用可见性。  
- 💻 支持本地 MCP 工具调用：通过适配器将本地 MCP 工具转换为 Llama Stack 格式，兼顾环境隔离与灵活性。  
- 📌 总结：Llama Stack 为 Node.js 开发者提供了多样化的 LLM 集成方案，涵盖本地/远程工具调用和代理 API，适合进一步探索 AI 应用开发。  

相关资源包括 Node.js 参考架构电子书、Red Hat 的 AI 教程和 GitHub 上的示例代码库。

---

### [在 JavaScript 中将值转换为字符串存在陷阱](https://2ality.com/2025/04/stringification-javascript.html)

**原文标题**: [Converting values to strings in JavaScript has pitfalls](https://2ality.com/2025/04/stringification-javascript.html)

JavaScript 中将值转换为字符串的方法及其潜在问题  

- 🔍 JavaScript 中将值转换为字符串比看起来更复杂，不同方法对某些值可能无效。  
- 🚨 示例代码 `new UnexpectedValueError(Symbol())` 会抛出异常，无法处理 `Symbol` 和原型为 `null` 的对象。  
- 📊 五种转换方法对比：`String(v)`、`'' + v`、`` `${v}` ``、`v.toString()` 和 `{}.toString.call(v)`，其中只有 `{}.toString.call(v)` 能处理所有特殊值（如 `undefined`、`null`、`Symbol()` 等）。  
- 🔧 `{}.toString.call(v)` 的原理是直接调用 `Object.prototype.toString`，避免因接收器无方法而导致的错误。  
- ⚠️ 原型为 `null` 的对象需自定义 `toString`、`valueOf` 或 `Symbol.toPrimitive` 方法才能被转换。  
- 🛠️ 修复方案：在错误类中使用 `{}.toString.call(value)` 确保兼容性。  
- 📦 对象默认字符串转换（如 `[object Object]`）信息有限，数组和函数有特定格式，但可能隐藏细节。  
- 🎨 可通过覆盖对象的 `toString()` 方法自定义字符串输出。  
- 📝 `JSON.stringify()` 适合对象和数组的转换，但不支持 `Symbol`、`BigInt` 和函数等值，且会忽略 `undefined` 属性。  
- ✨ 使用 `JSON.stringify()` 的第三个参数可实现多行和缩进输出，便于阅读。  
- 📌 控制台方法（如 `console.log`）能较好显示复杂对象，但默认深度有限，可通过配置（如 Node.js 的 `depth: null`）调整。  
- 🔄 不同场景需权衡安全性与简洁性，`String(v)` 和 `{}.toString.call(v)` 是常用选择。

---

### [Scalekit SSO 解决方案：为您的 B2B 应用提供无缝安全访问](https://www.scalekit.com/sso?utm_source=node-weekly&utm_medium=referral&utm_campaign=paid-inclusion)

**原文标题**: [Scalekit SSO Solutions: Seamlessly Secure Access for Your B2B app](https://www.scalekit.com/sso?utm_source=node-weekly&utm_medium=referral&utm_campaign=paid-inclusion)

该内容介绍了一个面向 SaaS 应用的 SSO（单点登录）和用户配置管理解决方案，主要功能包括快速集成、自动化用户管理及多身份提供商支持。

- 🔐 **单点登录（SSO）**：支持 SAML 和 OIDC 协议，可快速集成到 SaaS 应用，提供 IdP（身份提供商）发起的登录和证书自动更新。
- ⚡ **快速集成**：声称能在几小时内完成 SSO 集成，提供沙箱环境测试，无需真实 IdP 账户。
- 🔄 **自动化用户管理**：通过 SCIM 实现用户和组的实时自动配置/取消配置，支持角色分配和目录组管理。
- 🌐 **社交登录**：简化注册和登录流程，支持多种社交平台连接。
- 🖥️ **管理门户**：提供配置 SSO 和 SCIM 的集中管理界面，客户可自助设置。
- 📚 **开发者支持**：包含文档、API 参考和 SDK，支持 REST API 和多种开发环境。
- 💡 **增强认证堆栈**：可与 Auth0、Firebase 等现有认证服务集成。
- 🆓 **免费层**：提供 3 个免费 SSO/SCIM 连接，无用户数量限制，含多租户支持。
- 📈 **企业功能**：支持自定义认证方法、多身份提供商统一集成，旨在帮助 SaaS 企业获取客户。

---

### [Scalekit SSO 解决方案：为您的 B2B 应用提供无缝安全访问](https://www.scalekit.com/sso?utm_source=node-weekly&utm_medium=referral&utm_campaign=paid-inclusion)

**原文标题**: [Scalekit SSO Solutions: Seamlessly Secure Access for Your B2B app](https://www.scalekit.com/sso?utm_source=node-weekly&utm_medium=referral&utm_campaign=paid-inclusion)

该内容介绍了一个面向 SaaS 应用的 SSO（单点登录）和用户配置管理解决方案，主要功能包括快速集成、自动化管理及多协议支持。

- 🔐 **单点登录（SSO）**：支持 SAML 和 OIDC 协议，可快速集成到 SaaS 应用，提供 IdP（身份提供商）发起的登录和证书自动更新。  
- ⚡ **快速集成**：通过 API、SDK 和开发环境，几小时内即可完成 SSO 部署，支持企业级身份提供商。  
- 🔄 **SCIM 配置**：自动化用户和群组的实时激活/停用，支持角色分配和统一目录集成。  
- 🌐 **社交登录**：简化注册和登录流程，一次集成支持多平台登录。  
- 🛠️ **管理门户**：提供 SSO 和 SCIM 的配置界面，客户可自助设置。  
- 📚 **开发者资源**：包含文档、API 参考和 SDK，支持无缝集成。  
- 💡 **免费方案**：提供 3 个免费 SSO/SCIM 连接，无用户数量限制，支持多租户。  
- 🔗 **扩展集成**：与 Auth0、Firebase 等身份平台兼容，支持主流目录和社交连接器。  
- 📢 **透明定价**：无隐藏费用，企业功能全开放，可免费开始或预约演示。

---

### [非 HTML 内容](https://blog.vaxry.net/articles/2025-electronAintBad)

**原文标题**: [Non-HTML content](https://blog.vaxry.net/articles/2025-electronAintBad)

无法总结：非 HTML 内容。

---

### [NPM 遭遇恶意软件活动仿冒常见库攻击...](https://socket.dev/blog/npm-targeted-by-malware-campaign-mimicking-familiar-library-names)

**原文标题**: [ NPM targeted by malware campaign mimicking familiar library...](https://socket.dev/blog/npm-targeted-by-malware-campaign-mimicking-familiar-library-names)

研究发现恶意 npm 包通过 Telegram 窃取 BullX 凭证  

- 🕵️ Socket 发现 npm 木马通过混淆代码和 Telegram 外泄数据  
- 💰 恶意软件主要针对加密货币钱包和 BullX 平台的登录凭证  
- 📦 攻击者利用 npm 包分发恶意代码，隐蔽性较强  
- 📡 数据通过 Telegram 渠道外传，规避传统安全检测  
- ⚠️ 开发者需警惕不明依赖包，加强代码审计与安全防护

---

### [npm 应从新包中移除默认许可证（ISC） | extremq.com](https://extremq.com/npm-should-remove-the-default-license-from-new-packages-isc/)

**原文标题**: [npm should remove the default license from new packages (ISC) | extremq.com](https://extremq.com/npm-should-remove-the-default-license-from-new-packages-isc/)

npm 默认在新包中使用 ISC 许可证，这一做法可能带来法律风险，且未提供足够信息让开发者了解其影响。

- 📦 npm 是 JavaScript 的默认包管理器，用于 Node.js 项目，允许开发者使用他人发布的代码包。  
- ⚖️ 许可证决定代码的使用权限（如商业化、开源要求等），工程师需谨慎选择以避免法律问题。  
- ❗ 使用`npm init`创建新包时，默认自动填充 ISC 许可证，但未解释其内容或提供无许可证选项。  
- ⚠️ 默认许可证可能导致开发者无意发布受限制代码，或引发后续许可证冲突（如 ISC 与 GPL 不兼容）。  
- 🤔 用户案例：开发者因默认 ISC 许可证导致项目被他人修改后重新许可，而自己原本拒绝授权。  
- 🐌 相关问题讨论已持续 2 年，但 npm 官方仍未回应或修改此设定。  
- 🔍 对比其他生态（如 Rust 的 cargo、Python 的 PyPi）均不默认添加许可证，强调用户自主选择。  
- 📜 无许可证≠公有领域：未声明许可证的代码默认受版权保护，禁止他人自由使用或分发。  
- 💡 建议：npm 应移除默认许可证，强制开发者主动选择或明确声明无许可证。  

（注：总结保留原文核心争议与案例，省略部分命令行示例和重复性法律解释）

---

### [Node.js 流与 TypeScript —— SitePoint](https://www.sitepoint.com/node-js-streams-with-typescript/)

**原文标题**: [Node.js Streams with TypeScript â SitePoint](https://www.sitepoint.com/node-js-streams-with-typescript/)

Node.js 流与 TypeScript 的结合使用指南，介绍了流的基本概念、四种类型、环境配置及实际应用案例，并提供了高级技巧如处理背压问题。

- 🌊 **流的重要性**：Node.js 流允许分块处理数据，避免内存耗尽，适用于大文件或实时数据处理。
- 🔄 **四种流类型**：可读流（Readable）、可写流（Writable）、双工流（Duplex）和转换流（Transform）。
- ⚙️ **环境配置**：需安装 Node.js 和 TypeScript，配置 `tsconfig.json` 并创建项目结构。
- 📂 **实际案例**：包括文件读取、写入、转换（如大写转换）、压缩及 HTTP 响应流处理。
- ⚠️ **高级技巧**：处理背压问题，确保应用在高负载下仍保持响应。
- 🛠️ **最佳实践**：使用 TypeScript 类型定义数据块、错误处理和管道（piping）以提高代码可读性和安全性。
- 🚀 **实际应用**：构建 API 流式传输大数据集，展示流的模块化和高效性。
- 📚 **总结**：Node.js 流与 TypeScript 结合提供了强大的 I/O 处理能力，适合各种高效数据处理场景。

---

### [为什么我们要为 Node.js 再创建一个 Kafka 客户端](https://blog.platformatic.dev/why-we-created-another-kafka-client-for-nodejs)

**原文标题**: [Why we created another Kafka client for Node.js](https://blog.platformatic.dev/why-we-created-another-kafka-client-for-nodejs)

Apache Kafka 在实时数据管道和流应用开发中至关重要，尤其在金融科技和媒体行业。Node.js 开发者过去主要使用 KafkaJS 或 node-rdkafka，但两者各有不足。为此，Platformatic 推出了新的 Kafka 客户端 @platformatic/kafka，旨在提供更好的性能、开发体验和 TypeScript 支持。

- 🚀 **KafkaJS 的不足**：已两年未更新，基于复杂的回调 API，影响性能和开发体验。
- 🔧 **node-rdkafka 的问题**：依赖过时的 NAN，不支持 Worker 线程，API 复杂。
- 🎯 **@platformatic/kafka 的优势**：结合性能与易用性，支持序列化/反序列化和 TypeScript。
- ⚡ **生产者 API 改进**：简化流程，支持 Promise 和回调，内置序列化。
- 📥 **消费者 API 改进**：仅支持流式处理，内置反序列化，简化开发。
- 📊 **性能对比**：@platformatic/kafka 在生产者和消费者基准测试中均表现最佳。
- 💡 **开发者体验**：提供更直观的 API 和完整的类型支持，提升开发效率。
- 🌟 **总结**：@platformatic/kafka 是 Node.js 中 Kafka 开发的现代、高性能解决方案。

---

### [Apache Kafka](https://kafka.apache.org/)

**原文标题**: [Apache Kafka](https://kafka.apache.org/)

Apache Kafka 是一个开源的分布式事件流处理平台，被数千家公司用于高性能数据管道、流分析、数据集成和关键任务应用，尤其受到财富 100 强企业的广泛信赖和使用。

- 🏦 **财富 100 强信任** - 超过 80% 的财富 100 强公司信赖并使用 Kafka。  
- 🏭 **行业覆盖广泛** - 在制造业、银行、保险、电信等行业中，顶级公司的使用比例极高（如 10/10 的制造业和保险公司）。  
- ⚡ **高吞吐与低延迟** - 支持网络极限吞吐量，延迟低至 2 毫秒。  
- 📈 **高度可扩展** - 可扩展至上千个代理，每日处理数万亿消息和 PB 级数据。  
- 💾 **持久化存储** - 数据安全存储在分布式、容错的集群中。  
- 🌐 **高可用性** - 支持跨可用区或地理区域的集群部署。  
- 🔄 **内置流处理** - 提供事件流处理功能，如聚合、过滤和转换。  
- 🔗 **广泛连接性** - 通过 Connect 接口与数百种数据源和接收器集成。  
- 📚 **多语言支持** - 提供多种编程语言的客户端库。  
- 🛠️ **丰富生态工具** - 拥有庞大的开源工具生态系统。  
- 🚀 **关键任务支持** - 保证消息顺序、零丢失和精确一次处理。  
- 🌍 **庞大用户社区** - 全球数千家组织使用，包括互联网巨头和汽车制造商。  
- 📖 **丰富资源** - 提供详尽的文档、培训、教程和社区支持（如 Stack Overflow）。

---

### [GitHub - ije/mono-jsx: 将`<html>`作为`Response`返回](https://github.com/ije/mono-jsx)

**原文标题**: [GitHub - ije/mono-jsx: `<html>` as a `Response`.](https://github.com/ije/mono-jsx)

mono-jsx 是一个轻量级的 JSX 运行时，用于在 JavaScript 运行时（如 Node.js、Deno、Bun、Cloudflare Workers 等）中将 `<html>` 元素渲染为 `Response` 对象。

- 🚀 无需构建步骤
- 🦋 轻量级（8KB gzipped），零依赖
- 🔫 响应式，具有最小的状态运行时
- 🛟 完整的 Web API TypeScript 定义
- ⏳ 支持流式渲染
- 🥷 集成 htmx
- 🌎 通用，适用于 Node.js、Deno、Bun、Cloudflare Workers 等

- 📦 安装方式：
  - Node.js/Cloudflare Workers: `npm i mono-jsx`
  - Deno: `deno add npm:mono-jsx`
  - Bun: `bun add mono-jsx`

- ⚙️ 配置 JSX 运行时：
  - 在 `tsconfig.json` 或 `deno.json` 中添加 `"jsxImportSource": "mono-jsx"`
  - 或使用指令 `/** @jsxImportSource mono-jsx */`

- 🎯 使用示例：
  - 返回 `<html>` 元素作为 `Response` 对象
  - 支持标准 HTML 属性名（如 `class` 代替 `className`）
  - 支持伪类、媒体查询和 CSS 嵌套
  - 使用 `<slot>` 元素进行内容分发

- ⚡ 响应式特性：
  - 使用 `this` 管理组件状态
  - 支持应用状态（appState）和计算属性（computed）
  - 提供 `<toggle>` 和 `<switch>` 条件渲染元素

- 🌊 流式渲染：
  - 支持异步组件和生成器
  - 可设置 `placeholder` 加载状态
  - 支持错误处理（`catch` 属性）

- 🔌 htmx 集成：
  - 通过 `htmx` 属性启用
  - 支持扩展（如 `htmx-ext-ws`）
  - 可自定义 htmx 版本或手动安装

- ⚠️ 注意事项：
  - 仅支持根 `<html>` 元素作为响应
  - 事件处理程序仅在客户端执行
  - 状态管理有特定限制（如不能使用箭头函数组件）

---

### [PGlite](https://pglite.dev/)

**原文标题**: [PGlite](https://pglite.dev/)

轻量级 Postgres 的完整 WASM 构建，压缩后不到 3MB。

- 🚀 完整的 Postgres WASM 构建  
- 📦 压缩后体积小于 3MB  
- 🌐 适用于 WebAssembly 环境  
- 🔧 功能完备的 Postgres 实现

---

### [PGlite](https://pglite.dev/repl/)

**原文标题**: [PGlite](https://pglite.dev/repl/)

ElectricSQL 是一个开源项目，提供文档和交互式编程环境（REPL），可在 GitHub 上获取。

- 🏠 **主页** - 提供项目的基本信息和入口。  
- ℹ️ **关于** - 包含项目的背景和详细介绍。  
- 📚 **文档** - 提供详细的使用指南和技术文档。  
- 💻 **REPL** - 提供交互式编程环境，方便用户测试和体验。  
- ⚡ **ElectricSQL** - 项目名称，强调其高效和电速的特性。  
- ⭐ **GitHub 星标** - 鼓励用户在 GitHub 上点赞和支持项目。

---

### [发布 6.7.0 版 · prisma/prisma · GitHub](https://github.com/prisma/prisma/releases/tag/6.7.0)

**原文标题**: [Release 6.7.0 · prisma/prisma · GitHub](https://github.com/prisma/prisma/releases/tag/6.7.0)

Prisma 发布了 6.7.0 稳定版本，引入了多项新功能和改进，包括早期访问的 TypeScript 查询编译器、对 better-sqlite3 驱动器的支持、多文件 Prisma 模式的生产就绪以及生成的 Prisma 客户端输出的拆分。

- 🎉 Prisma ORM 现在提供早期访问的 TypeScript 查询编译器，替代了之前的 Rust 引擎，支持 PostgreSQL 和 SQLite 数据库。
- 📚 使用新的查询编译器需要添加`queryCompiler`和`driverAdapters`特性标志，并安装相应的驱动器适配器。
- 🚀 引入了对`better-sqlite3` JavaScript 驱动器的支持，允许以 JS 原生方式与 SQLite 数据库交互。
- 📂 多文件 Prisma 模式现已生产就绪，允许将模式拆分为多个文件以提高组织性。
- ✂️ 新的`prisma-client`生成器将生成的 Prisma 客户端库拆分为多个文件，避免了单一大文件的问题。
- 🛠️ 生成的 Prisma 客户端文件现在不会引发 ESLint 和 TypeScript 错误。
- 📰 公司新闻部分提到了 Prisma 团队的其他动态，包括与 Vercel Marketplace 的集成和 Prisma Postgres 的早期访问功能。

---

### [GitHub - piscinajs/piscina: 快速高效的 Node.js 工作线程池实现](https://github.com/piscinajs/piscina)

**原文标题**: [GitHub - piscinajs/piscina: A fast, efficient Node.js Worker Thread Pool implementation](https://github.com/piscinajs/piscina)

Piscina 是一个高效的 Node.js 工作线程池实现，专注于快速线程间通信和任务处理。

- 🚀 **快速高效**：Piscina 提供了快速的工作线程间通信，适用于固定和可变任务场景。
- 🔧 **灵活配置**：支持自定义线程池大小、任务队列和资源限制。
- 📊 **统计跟踪**：提供任务运行和等待时间的详细统计信息。
- ⏹️ **任务取消**：支持通过 `AbortController` 或 `EventEmitter` 取消任务。
- 📜 **多格式支持**：兼容 CommonJS、ESM 和 TypeScript。
- 🔄 **自定义任务队列**：允许使用自定义任务队列实现，如内置的 `FixedQueue`。
- 🐧 **Linux 优先级**：支持通过 `niceIncrement` 设置工作线程的 CPU 调度优先级。
- 📡 **广播通信**：支持通过 `BroadcastChannel` 在所有工作线程间广播消息。
- 📉 **性能优化**：内置 `FixedQueue` 显著提升大任务队列的性能。
- ⚠️ **注意事项**：异步代码需谨慎处理，避免不可预测的行为。

Piscina 适用于计算密集型任务，但在异步 I/O 操作中性能提升有限。开发团队建议根据具体应用场景调整配置参数以达到最佳性能。

---

### [GitHub - dolanmiu/docx：使用JS/TS轻松生成和修改.docx文件，提供优雅的声明式API。支持Node和浏览器环境。](https://github.com/dolanmiu/docx)

**原文标题**: [GitHub - dolanmiu/docx: Easily generate and modify .docx files with JS/TS with a nice declarative API. Works for Node and on the Browser.](https://github.com/dolanmiu/docx)

一个用于生成和修改.docx 文件的 JavaScript/TypeScript 库，支持 Node 和浏览器环境，提供声明式 API 和丰富的示例。

- 📄 **项目描述**：使用 JS/TS 轻松生成和修改.docx 文件，适用于 Node 和浏览器环境。  
- 🌐 **在线演示**：提供多个框架（HTML/JS、Angular、React、Vue.js）的在线示例链接。  
- ⚙️ **功能示例**：包括段落、表格、图片、页眉页脚等文档功能的代码示例。  
- 📚 **文档与使用**：详细文档和示例请访问 [docx.js.org](https://docx.js.org/)。  
- 🎨 **交互式体验**：可通过 Docx.js Editor 实时预览代码效果。  
- 🤝 **贡献指南**：提供贡献代码的指南和规范。  
- 💖 **开源信息**：MIT 许可证，4.9k 星，526 forks，118 位贡献者。  
- 🛠️ **技术支持**：支持 React、Node.js、Vue.js、Angular 等多种技术栈。

---

### [发布 v8.0.0 · ldapts/ldapts · GitHub](https://github.com/ldapts/ldapts/releases/tag/v8.0.0)

**原文标题**: [Release v8.0.0 · ldapts/ldapts · GitHub](https://github.com/ldapts/ldapts/releases/tag/v8.0.0)

这是一个关于 ldapts 项目发布 v8.0.0 版本的 GitHub 页面内容摘要。

- 🚀 发布了 ldapts 的 v8.0.0 版本，日期为 2025 年 5 月 5 日。
- ⚠️ 主要变更：移除了对 Node.js v18 的支持，现在最低要求版本为 Node.js v20。
- 🔧 更新了 package.json 中的 engines 字段以反映新的 Node.js 版本要求。
- 🔄 更新了 CI 配置，现在仅测试支持的 Node.js 版本。
- 🛠️ 修复了语义发布中的可选作用域问题（#189）。
- 🔍 针对主分支的 PR 现在会运行 CI 作业。
- 📅 该版本由 github-actions 于 5 月 5 日 17:44 发布，包含 2 个提交。

---

### [GitHub - NodeBB/NodeBB: 专为现代网络构建的基于 Node.js 的论坛软件](https://github.com/NodeBB/NodeBB)

**原文标题**: [GitHub - NodeBB/NodeBB: Node.js based forum software built for the modern web](https://github.com/NodeBB/NodeBB)

NodeBB 是一个基于 Node.js 的现代论坛软件，支持实时互动和多种数据库，具有高度可定制性和丰富的插件生态。

- 🚀 **技术栈**：基于 Node.js，支持 Redis、MongoDB 或 PostgreSQL 数据库，使用 WebSocket 实现实时交互。  
- 🎨 **主题与设计**：提供灵活的主题引擎（如默认的 Harmony 主题），支持 SCSS/CSS 和 Bootstrap 5，鼓励设计师贡献主题。  
- 🌍 **国际化**：通过 Transifex 支持多语言翻译，欢迎社区参与本地化。  
- 🔧 **开发与贡献**：开源项目（GPL-3.0 协议），开发者可提交 PR 或开发插件，新手可从插件代码入手学习。  
- ⚙️ **安装要求**：需 Node.js 20+ 和 MongoDB 3.6+/Redis 2.8.9+，支持 Docker 和云部署，提供详细安装文档。  
- 🔒 **安全建议**：强调 Redis 配置安全（如绑定本地 IP 和密码保护），推荐使用 iptables/ufw 限制端口访问。  
- 🔄 **升级与维护**：提供专用升级指南，支持集群化部署需依赖 Redis。  
- 💼 **商业支持**：非开源场景可联系获取子许可协议，另有付费托管服务。  
- 📚 **资源链接**：含演示站点、开发者社区、文档、博客及社交媒体渠道（Twitter/Facebook/IRC）。

---

### [GitHub - weyoss/redis-smq: 一个简单高效的 Node.js Redis 消息队列](https://github.com/weyoss/redis-smq)

**原文标题**: [GitHub - weyoss/redis-smq: A simple high-performance Redis message queue for Node.js.](https://github.com/weyoss/redis-smq)

一个基于 Redis 的高性能 Node.js 消息队列系统，支持多种队列类型和消息传递模型，适用于后台任务、微服务通信等场景。

- 🚀 高性能 Redis 消息队列，专为 Node.js 设计  
- 🔄 支持多队列生产者和消费者模型  
- 🔀 多种交换类型（Direct、Topic、FanOut）  
- 📬 两种消息传递模型（点对点和发布/订阅）  
- 📊 三种队列策略（FIFO、LIFO、优先级队列）  
- 🧵 使用工作线程处理消息，提升性能和隔离性  
- ⏱️ 支持消息过期和消费超时设置  
- 🚦 队列速率限制功能  
- 🕰️ 内置调度器，支持延迟消息和重复消息  
- 🌐 提供 RESTful API 和 Web 界面  
- 📦 支持 ESM 和 CJS 模块  
- 📧 适用于后台任务（如邮件发送、数据处理）  
- 🔄 微服务架构中的服务间通信  
- 🎮 实时事件处理（游戏、IoT、分析系统）  
- 📚 详细文档和 MIT 许可证

---

### [发布 v4.97.0 · openai/openai-node · GitHub](https://github.com/openai/openai-node/releases/tag/v4.97.0)

**原文标题**: [Release v4.97.0 · openai/openai-node · GitHub](https://github.com/openai/openai-node/releases/tag/v4.97.0)

OpenAI 的 Node.js 客户端库发布了 v4.97.0 版本，包含新功能、文档修复和优化。

- 🚀 **新功能**：API 新增图像尺寸和推理加密支持（提交 9c2113a）  
- 📝 **文档更新**：修复实时示例中的拼写错误（#1406，提交 8717b9f）  
- 🔧 **维护**：添加缺失的弃用警告说明（提交 253392c）  
- ✏️ **拼写修正**：README 中的拼写错误修复（提交 cab3478）  
- 🏷️ **版本发布**：发布于 2025 年 5 月 2 日，完整更新日志见 v4.96.2...v4.97.0  
- ❤️ **社区互动**：用户 rupam-kundu 对发布表示喜爱（心形表情反应）

---

### [发布 v4.0.0-rc.4 · svg/svgo · GitHub](https://github.com/svg/svgo/releases/tag/v4.0.0-rc.4)

**原文标题**: [Release v4.0.0-rc.4 · svg/svgo · GitHub](https://github.com/svg/svgo/releases/tag/v4.0.0-rc.4)

SVGO 发布了 v4.0.0-rc.4 版本，这是一个预发布候选版本，主要修复了类型声明问题，并改进了测试流程。  

- 🛠️ 修复了`#loadConfig`的类型声明问题，现在与 v3 版本行为一致，并增加了更严格的测试。  
- 📝 正在编写从 v3 迁移到 v4 的指南，将在正式发布后提供。  
- ❌ 跳过了 v4.0.0-rc.3 版本，因为该版本被错误地发布为稳定版，现已撤销。  
- 🔧 无功能变化影响 SVG 优化或浏览器捆绑包。  
- 🙏 感谢贡献者@ntnyq 报告并修复了类型问题。  
- 🤖 考虑迁移到 GitHub Actions 以减少发布错误的风险。

---

### [发布 v5.1.0 · MrRefactoring/jira.js · GitHub](https://github.com/MrRefactoring/jira.js/releases/tag/v5.1.0)

**原文标题**: [Release v5.1.0 · MrRefactoring/jira.js · GitHub](https://github.com/MrRefactoring/jira.js/releases/tag/v5.1.0)

这是一个关于 jira.js 库 v5.1.0 版本的发布说明，主要包含了新增的 API 组和一些方法的更新与弃用信息。

- 🚀 **版本发布**：v5.1.0 版本于 5 月 3 日发布，包含 1 个提交到主分支。  
- 🔑 **签名验证**：提交使用了 GitHub 的已验证签名，GPG 密钥 ID 为 B5690EEEBB952194。  
- 📌 **新增 API 组**：  
  - **Version 2 Client** 和 **Version 3 Client** 均新增了 `UserNavProperties`、`ProjectTemplates` 和 `IssueCustomFieldAssociations` API 组。  
- ⚠️ **弃用方法**：  
  - `IssueSearch.searchForIssuesUsingJql` 和 `IssueSearch.searchForIssuesUsingJqlPost` 被弃用，推荐使用 `IssueSearch.searchForIssuesUsingJqlEnhancedSearch` 和 `IssueSearch.searchForIssuesUsingJqlEnhancedSearchPost`。  
  - `IssueSearch.searchForIssuesIds` 也被标记为弃用。  
- ➕ **新增属性**：在 `IssueFields.getFieldsPaginated` 方法中新增了 `projectIds` 属性。  
- 🔄 **新增方法**：在 `IssueBulkOperations` API 组中新增了 `submitBulkUnwatch` 和 `submitBulkWatch` 方法。

---

### [GitHub - noblox/noblox.js: 适用于 Roblox 的 Node.js API 封装库](https://github.com/noblox/noblox.js)

**原文标题**: [GitHub - noblox/noblox.js: A Node.js API wrapper for Roblox.](https://github.com/noblox/noblox.js)

noblox.js 是一个基于 Node.js 的 Roblox API 封装库，用于通过 NodeJS 执行 Roblox 网站上的操作。它是 roblox-js 模块的一个分支，支持 JavaScript 和 TypeScript。该库常用于游戏内脚本或 Discord 工具的开发，用于管理社区或执行网站操作。

- 🚀 **项目信息**：noblox.js 是一个开源项目，拥有 272 颗星和 141 个分支，采用 MIT 许可证。
- 📚 **文档与资源**：提供详细的文档、常见问题解答、YouTube 系列教程以及相关资源（如 noblox.js-server）。
- ⚙️ **安装要求**：需要 Node.js v18.18 或更高版本，可通过 npm 或 yarn 安装。
- 🔐 **认证与安全**：使用 `.ROBLOSECURITY` cookie 进行认证，建议使用环境变量（如 dotenv）存储敏感信息，并使用次要账户进行机器人操作。
- 🛠️ **快速开始**：安装库后，通过 `setCookie()` 设置认证，然后可以调用各种功能（如获取用户信息、群组信息等）。
- ❗ **常见问题**：包括未登录错误、角色集无效错误和授权失败错误，提供了相应的解决方案。
- 👏 **贡献者**：感谢 suufi、sentanos 等贡献者的维护和文档支持。
- 🌐 **更多信息**：项目官网为 noblox.js.org，涵盖更多详细内容和更新。

---

### [GitHub - avajs/ava: 让你自信开发的 Node.js 测试运行器 🚀](https://github.com/avajs/ava)

**原文标题**: [GitHub - avajs/ava: Node.js test runner that lets you develop with confidence 🚀](https://github.com/avajs/ava)

AVA 是一个 Node.js 测试运行器，具有简洁的 API、详细的错误输出、支持新语言特性以及线程隔离，让你可以自信地进行开发 🚀  

- 🚀 **特点**：简洁的测试语法、并发运行测试、强制编写原子测试、无隐式全局变量、支持 TypeScript  
- 🎯 **优势**：魔法断言（Magic assert）、独立的测试环境、支持 Promise 和异步函数、增强的断言消息  
- ⚡ **性能**：在 CI 中自动并行运行测试、TAP 报告器  
- 📦 **安装**：通过 `npm init ava` 或 `yarn add ava --dev` 安装，支持本地运行  
- 📝 **使用**：创建测试文件（如 `test.js`），使用 ES 模块语法编写测试  
- 🔧 **运行**：通过 `npm test` 或 `npx ava` 运行测试，支持 `--watch` 模式  
- 🌍 **支持**：支持最新的 Node.js 主要版本，提供详细的错误堆栈和代码片段  
- 📚 **文档**：包含测试编写、断言、快照测试、命令行配置等详细指南  
- ❓ **常见问题**：如名称发音（/ˈeɪvə/）、背景图（仙女座星系）等  
- 💡 **扩展**：提供多种插件和工具（如 `eslint-plugin-ava`、`@ava/typescript`）  
- 👥 **团队**：由 Mark Wubben 和 Sindre Sorhus 等开发者维护  
- 📜 **许可证**：MIT 许可证，代码托管在 GitHub，拥有活跃的社区支持

---

### [为什么我们要为 Node.js 再创建一个 Kafka 客户端](https://blog.platformatic.dev/why-we-created-another-kafka-client-for-nodejs?showSharer=true)

**原文标题**: [Why we created another Kafka client for Node.js](https://blog.platformatic.dev/why-we-created-another-kafka-client-for-nodejs?showSharer=true)

Apache Kafka 在实时数据管道和流应用开发中至关重要，尤其在金融科技和媒体行业。Node.js 开发者以往主要使用 KafkaJS 或 node-rdkafka，但两者各有不足。因此，Platformatic 推出了 @platformatic/kafka，旨在提供更好的性能、开发体验和 TypeScript 支持。

- 🚀 **Kafka 在 Node.js 中的重要性** - Apache Kafka 是实时数据处理的核心工具，尤其在金融科技和媒体行业。
- 🔄 **现有库的问题** - KafkaJS 已不再维护，node-rdkafka 存在兼容性和性能问题。
- 🛠 **@platformatic/kafka 的诞生** - 为了解决现有库的不足，Platformatic 推出了新的 Kafka 客户端，注重性能和开发体验。
- 📊 **性能对比** - @platformatic/kafka 在生产者和消费者基准测试中均优于 KafkaJS 和 node-rdkafka。
- ✨ **开发者体验优化** - 提供更简洁的 API、内置序列化/反序列化支持，以及 TypeScript 集成。
- 🤝 **社区参与** - Platformatic 鼓励开发者提供反馈，以进一步改进库的功能和体验。

---

### [Mastra.ai 快速入门 - 5 分钟内构建 TypeScript 代理指南 — WorkOS](https://workos.com/blog/mastra-ai-quick-start)

**原文标题**: [Mastra.ai Quickstart - How to build a TypeScript agent  in 5 minutes or less â WorkOS](https://workos.com/blog/mastra-ai-quick-start)

Mastra.ai 是一个功能全面的 TypeScript 框架，专为构建代理应用而设计。本文介绍了如何在 5 分钟内使用 Mastra 创建一个能够从 GitHub 获取数据的代理应用。

- 🚀 **Mastra 框架介绍** - Mastra 是一个内置功能的 TypeScript 框架，用于构建代理应用，无需整合多个第三方库。
- ⚡ **快速启动项目** - 使用 `npm create mastra@latest` 命令快速创建项目，并配置代理和工具组件。
- 🔑 **添加 API 密钥** - 通过 CLI 提示或 `.env` 文件添加 LLM 密钥。
- 🛠️ **创建 GitHub 工具** - 在 `src/mastra/tools/github-repo-tool.ts` 中定义工具，使用 Zod 进行运行时验证。
- 🤖 **创建代理** - 在 `src/mastra/agents/github.ts` 中定义代理，明确代理的指令和工具访问权限。
- 🔗 **注册并运行应用** - 在 `src/mastra/index.ts` 中注册代理，运行 `npm run dev` 启动服务。
- 🎮 **本地测试** - Mastra 提供集成的本地 Playground，方便测试代理功能。
- 🌐 **API 调用** - 通过 API 或代码调用代理，获取 GitHub 仓库的统计数据。
- 📈 **后续步骤** - 可以尝试工作流链分析、RAG 文档嵌入、可观测性集成和部署到生产环境。

---

### [GitHub - tc39/proposal-explicit-resource-management: ECMAScript 显式资源管理提案](https://github.com/tc39/proposal-explicit-resource-management)

**原文标题**: [GitHub - tc39/proposal-explicit-resource-management: ECMAScript Explicit Resource Management](https://github.com/tc39/proposal-explicit-resource-management)

ECMAScript 显式资源管理提案旨在简化资源（如内存、I/O 等）的生命周期管理，通过引入新的语法和 API 来确保资源的显式释放。

- 🚀 **提案状态**：Stage 3，由 Ron Buckton 担任 Champion。
- 📜 **许可证**：BSD-3-Clause license。
- ⭐ **GitHub 数据**：833 颗星，32 个 fork。
- 🔄 **语法特性**：
  - `using` 声明用于同步资源管理。
  - `await using` 声明用于异步资源管理。
- 🔧 **API 新增**：
  - `Symbol.dispose` 和 `Symbol.asyncDispose` 用于定义资源的释放方法。
  - `DisposableStack` 和 `AsyncDisposableStack` 用于管理多个资源。
- 🛠️ **使用场景**：
  - 简化文件句柄、流、锁等资源的管理。
  - 避免常见的资源管理错误，如忘记释放资源。
- 🔄 **与其他语言的对比**：
  - 类似 C# 的 `using` 语句、Java 的 `try-with-resources` 和 Python 的 `with` 语句。
- 📚 **文档与示例**：
  - 提供了丰富的代码示例，展示如何在各种场景中使用新语法和 API。
- 🔍 **未来工作**：
  - 完善规范文本。
  - 增加测试用例和实现兼容性。

---

### [通过 Apps Script 将 Google Analytics 数据导出到 Sheets](https://technicalwriting.dev/analytics/sheets.html)

**原文标题**: [Export Google Analytics data to Sheets via Apps Script](https://technicalwriting.dev/analytics/sheets.html)

本教程介绍了如何使用 Google Apps Script 将 Google Analytics 数据导出到 Google Sheets，并实现自动更新和公开访问功能。

- 📊 使用 Google Apps Script 将 Google Analytics 数据导出到 Google Sheets，并支持自动每晚更新和手动更新。
- 🔧 前提条件：熟悉 Google Sheets 和 JavaScript。
- 🛠️ 设置步骤：创建 Google Sheets 表格，关联 Apps Script 项目，配置依赖项和权限。
- 📜 配置文件：修改 appsscript.json 以包含 Google Analytics 库和必要的 OAuth 权限。
- 📝 脚本编写：在 Code.gs 中编写脚本，替换所有 TODO 项，包括 Google Analytics 属性 ID、Google Sheets ID 等。
- 🔄 数据处理：脚本会获取页面路径、浏览量、会话时长和跳出率等数据，并进行格式化。
- 📉 数据可视化：在表格中计算并显示月环比变化，并使用条件格式突出显示变化。
- 🚀 手动更新：通过自定义菜单项手动更新数据。
- ⏰ 自动更新：设置时间触发器，每晚自动更新数据。
- 🌐 公开访问：部署为 Web 应用，公开数据为 JSON 格式（需谨慎使用）。

---

### [3.13 版本发布 | GSAP | 文档与学习](https://gsap.com/blog/3-13/)

**原文标题**: [3.13 release | GSAP | Docs & Learning](https://gsap.com/blog/3-13/)

GSAP 3.13 版本发布，宣布 GSAP 及其所有插件（包括 SplitText 和 MorphSVG 等）现在完全免费，甚至可用于商业用途。团队将继续维护和创新，同时与 Webflow 合作开发下一代交互功能。SplitText 插件进行了全面重写，新增多项功能并优化性能。此外，GSAP 3.13 还支持动画到 CSS 变量，并简化了 Webflow 的安装流程。

- 🎉 GSAP 及其所有插件现在完全免费，包括商业用途  
- 🛠️ 原始团队将继续维护和创新 GSAP  
- 🤝 与 Webflow 合作开发下一代交互功能  
- 📥 所有插件已添加到 GSAP Github 仓库和 NPM 包  
- 💖 感谢 Club GSAP 成员，取消私人仓库访问步骤  
- 🔧 SplitText 插件重写，新增 14 项功能并优化性能  
- ♿ 改进屏幕阅读器可访问性  
- 🔄 新增响应式重新分割功能  
- ✂️ 支持嵌套元素分割  
- 🎭 新增遮罩功能  
- 🆕 支持动画到 CSS 变量  
- 🚀 简化 Webflow 安装流程  
- 📚 提供完整的文档和学习资源

---

### [资源 | GSAP 演示示例](https://gsap.com/demos/)

**原文标题**: [Resources | GSAP Demos](https://gsap.com/demos/)

GSAP 是一个专业的 JavaScript 动画库，适用于现代网页开发，提供丰富的工具和插件支持多种动画效果。

- 🌐 **核心功能** - 提供 Core、Scroll、SVG、UI 和 Text 等核心动画工具。
- 📚 **学习资源** - 包含文档、演示示例和视频教程，帮助用户快速上手。
- 🛠️ **开发支持** - 提供 Starter Templates，支持 Vanilla JS、React、Next 等框架。
- 🔌 **插件扩展** - 包括 ScrollTrigger、MotionPath、Draggable 等多种插件，增强动画效果。
- 💬 **社区互动** - 拥有活跃的论坛和社区，用户可以交流学习经验。
- 📧 **订阅服务** - 提供新闻订阅，及时获取 GSAP 的最新动态。
- 🔗 **外部链接** - 支持 CodePen、GitHub 等平台，方便用户分享和查看更多示例。

---

### [运算符查询 - 搜索 JavaScript 运算符](https://www.joshwcomeau.com/operator-lookup/)

**原文标题**: [Operator Lookup - Search JavaScript Operators](https://www.joshwcomeau.com/operator-lookup/)

这是一个关于 Josh W. Comeau 的个人网站的页面内容，包含了他的课程、分类、工具和联系信息等。

- 🏠 **主页导航**：包含课程、分类、好物和关于等主要板块。  
- 🔍 **操作符查询工具**：提供 JavaScript 操作符的搜索和学习功能。  
- 📧 **订阅功能**：用户可以输入邮箱订阅新内容发布的免费新闻稿。  
- 📂 **分类浏览**：包括 CSS、React、动画、JavaScript、职业发展等类别。  
- 🎓 **互动课程**：提供《CSS for JavaScript Devs》和《The Joy of React》等课程链接。  
- ℹ️ **通用信息**：包含关于 Josh、博客介绍、联系方式等。  
- ⚙️ **用户设置**：支持关闭声音、激活暗黑模式和 RSS 订阅。  
- 📱 **社交媒体**：提供 BlueSky、Github 和 LinkedIn 的个人资料链接。  
- ©️ **版权信息**：包含版权声明和使用条款、隐私政策等链接。

---

### [运算符查询 - 搜索 JavaScript 运算符](https://www.joshwcomeau.com/operator-lookup/?match=unsigned-right-shift-assignment)

**原文标题**: [Operator Lookup - Search JavaScript Operators](https://www.joshwcomeau.com/operator-lookup/?match=unsigned-right-shift-assignment)

这是一个个人博客网站的页面内容，展示了 Josh W Comeau 的个人信息和资源链接。

- 🏠 主页导航：包含分类、课程、资源等栏目  
- 🔍 特色工具：提供 JavaScript 运算符查询功能  
- 📧 订阅服务：用户可通过邮箱订阅新内容通知  
- 📚 内容分类：涵盖 CSS、React、动画、JavaScript 等技术主题  
- 🎓 互动课程：提供《CSS for JavaScript》和《The Joy of React》等课程  
- ℹ️ 个人信息：包含作者介绍、博客说明和联系方式  
- ⚙️ 网站功能：支持关闭音效、切换暗黑模式、RSS 订阅  
- 🔗 社交链接：整合 BlueSky、Github、LinkedIn 等平台入口  
- ©️ 版权声明：包含使用条款、隐私政策等法律文件

---

### [Redis 再次开源 - <antirez>](https://antirez.com/news/151)

**原文标题**: [
Redis is open source again - <antirez>
](https://antirez.com/news/151)

Redis 重新恢复开源模式

- 🔓 Redis 再次采用开源许可证  
- 🚀 保持高性能、内存数据库的核心优势  
- 🌍 社区可自由使用、修改和分发代码  
- 💡 开发者生态得到进一步巩固  
- ⚖️ 平衡商业化与开源协作需求

---

