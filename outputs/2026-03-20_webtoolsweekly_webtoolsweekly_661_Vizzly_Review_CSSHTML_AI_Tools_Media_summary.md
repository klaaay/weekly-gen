### [可视化证明：您的用户界面行之有效 | Vizzly](https://vizzly.dev/?utm_source=webtoolsweekly&utm_medium=newsletter&utm_campaign=2026q1&utm_content=march19)

**原文标题**: [Visual Proof That Your UI Works | Vizzly](https://vizzly.dev/?utm_source=webtoolsweekly&utm_medium=newsletter&utm_campaign=2026q1&utm_content=march19)

Vizzly 是一个视觉测试平台，帮助开发者通过截图对比验证UI变更，确保代码变更不会引入视觉错误，尤其适用于AI生成代码的验证。

- 🖼️ **视觉验证UI变更**：提供可视化差异对比，确保代码变更（无论是AI生成还是手动修改）在发布前符合预期。
- 🤖 **专注AI生成代码验证**：快速检测AI编写代码可能引入的视觉错误，弥补代码审查的不足。
- 💰 **高性价比测试方案**：价格优势明显，每美元可处理远超竞争对手的截图数量，支持全面测试而无预算压力。
- 🔧 **无缝集成现有工具**：兼容Playwright、Cypress等常用测试工具，无需改变现有工作流程。
- 🧠 **智能差异检测引擎**：采用Honeydiff技术，能自动忽略时间戳、广告等动态内容噪声，准确识别真实UI变化。
- ⚡ **本地即时测试反馈**：支持离线本地测试，提供实时视觉反馈，无需等待CI构建，提升开发效率。
- 🌐 **预览环境集成**：提供应用构建的托管预览，支持在真实上下文中审查视觉差异，而不仅仅是静态截图。
- 📦 **灵活的定价模式**：提供按用户月度订阅，无按截图收费，团队使用成本可控。

---

### [功能特性 | 每个PR的可视化验证 | Vizzly](https://vizzly.dev/features/?utm_source=webtoolsweekly&utm_medium=newsletter&utm_campaign=2026q1&utm_content=march19)

**原文标题**: [Features | Visual Proof for Every PR | Vizzly](https://vizzly.dev/features/?utm_source=webtoolsweekly&utm_medium=newsletter&utm_campaign=2026q1&utm_content=march19)

Vizzly是一款可视化测试平台，帮助开发者在编码阶段即时发现界面错误，支持本地测试、智能差异检测和团队协作，并提供灵活的定价方案。

- 🐛 即时捕获编码中的界面错误，无需等待CI流程
- 🧠 智能差异检测引擎Honeydiff，自动过滤时间戳、广告等干扰因素
- 🔌 兼容多种测试工具（Playwright、Cypress等）的截图源
- 👥 支持基于位置的评论、审批流程和团队协作功能
- 🚀 提供本地TDD工作流，比传统工具快12倍
- 🤖 专门针对AI生成代码提供可视化验证保障
- 💰 按团队人数定价，无按截图数量收费的担忧
- 🆓 提供永久免费层，无需信用卡即可开始使用

---

### [Vizzly - 高级视觉评审与协作平台](https://app.vizzly.dev/register?utm_source=webtoolsweekly&utm_medium=newsletter&utm_campaign=2026q1&utm_content=march19)

**原文标题**: [Vizzly - Advanced Visual Review & Collaboration Platform](https://app.vizzly.dev/register?utm_source=webtoolsweekly&utm_medium=newsletter&utm_campaign=2026q1&utm_content=march19)

本文介绍了人工智能在医疗领域的应用现状与前景，重点探讨了其在疾病诊断、治疗方案优化及医疗管理效率提升方面的作用，并指出相关技术发展面临的挑战与伦理考量。

- 🏥 AI辅助诊断系统能通过分析医学影像提升早期疾病检出率
- 💊 机器学习可基于患者数据生成个性化治疗方案，提高疗效
- ⚙️ 智能流程管理工具帮助医院优化资源分配，减少行政负担
- 🔬 基因组学与AI结合加速新药研发和精准医疗发展
- ⚖️ 数据隐私保护与算法透明度是当前面临的主要伦理挑战

---

### [快速入门指南 | Vizzly 文档](https://docs.vizzly.dev/getting-started/quick-start/?utm_source=webtoolsweekly&utm_medium=newsletter&utm_campaign=2026q1&utm_content=march19)

**原文标题**: [Quick Start Guide | Vizzly Docs](https://docs.vizzly.dev/getting-started/quick-start/?utm_source=webtoolsweekly&utm_medium=newsletter&utm_campaign=2026q1&utm_content=march19)

Vizzly 是一款通过截图对比检测视觉错误的工具，提供两种使用方式：直接上传现有截图或集成到测试框架中自动捕获。

- 🚀 **快速开始**：需要 Node.js 22 及以上版本和 Vizzly 账户，支持本地 OAuth 登录或 CI/CD 环境使用 API 令牌认证。
- 📤 **上传截图**：安装 CLI 工具后，可通过命令上传单个截图或整个目录，并指定构建名称以在仪表板查看结果。
- 🔧 **集成测试框架**：在测试代码中调用 SDK 捕获截图，可添加浏览器、视口等元数据，使用 `vizzly run` 命令运行测试并即时获取对比反馈。
- 📊 **首次构建处理**：首次构建的截图均标记为“新增”，系统默认使用 Git 模式基于分支历史自动选择基线，后续构建将分类显示未更改、已变更、新增或缺失的截图。
- 🔄 **基线策略配置**：支持 Git 模式、手动模式或分支持不同基线，可在项目设置中按需调整。
- ⚙️ **CI/CD 集成**：提供 GitHub Actions 等示例，可将视觉测试加入持续集成流程，确保令牌正确设置以启用自动化。
- 🛠️ **问题排查**：检查令牌连接、截图生成路径及构建处理状态，使用 `vizzly doctor` 诊断 API 连通性。
- 📚 **进阶学习**：可深入了解构建与基线概念、CLI 与 SDK 完整文档、基线管理配置及团队协作流程。

---

### [CLI 概览 | Vizzly 文档](https://docs.vizzly.dev/integration/cli/overview/?utm_source=webtoolsweekly&utm_medium=newsletter&utm_campaign=2026q1&utm_content=march19)

**原文标题**: [CLI Overview | Vizzly Docs](https://docs.vizzly.dev/integration/cli/overview/?utm_source=webtoolsweekly&utm_medium=newsletter&utm_campaign=2026q1&utm_content=march19)

Vizzly CLI 是一个用于视觉测试的工具，它通过本地服务器处理测试截图，支持本地开发（TDD模式）和CI/CD（云模式）两种测试方式，并提供多种集成选项和AI辅助功能。

- 🖥️ **本地开发（TDD模式）**：运行 `vizzly tdd` 启动本地服务器和仪表板，在 `npm test --watch` 模式下实时比较截图与本地基线，无需上传。
- ☁️ **CI/CD（云模式）**：使用 `vizzly run "npm test"` 运行测试，截图会上传至Vizzly云端，生成可供团队审查的构建URL。
- 📦 **安装要求**：通过 `npm install -D @vizzly-testing/cli` 安装，需要Node.js 22或更高版本。
- 🔑 **身份验证**：本地开发使用 `vizzly login` 进行OAuth认证；CI/CD中通过设置 `VIZZLY_TOKEN` 环境变量使用项目令牌。
- 🛠️ **主要命令**：包括 `vizzly run`（云测试）、`vizzly tdd`（本地测试）、`vizzly upload`（上传截图）、`vizzly init`（创建配置）等。
- 📄 **测试集成**：在测试文件中导入 `vizzlyScreenshot` 函数，支持传递截图缓冲区或文件路径，兼容Playwright、Cypress等工具。
- 📦 **包导出**：提供 `@vizzly-testing/cli/client`（轻量客户端）、`@vizzly-testing/cli/sdk`（自定义集成）、`@vizzly-testing/cli/config`（配置助手）等多个入口点。
- 🤖 **AI集成**：内置AI支持，如Claude Code集成，可辅助视觉测试工作流、调试和测试覆盖建议。

---

### [TDD 模式 | Vizzly 文档](https://docs.vizzly.dev/integration/cli/tdd-mode/?utm_source=webtoolsweekly&utm_medium=newsletter&utm_campaign=2026q1&utm_content=march19)

**原文标题**: [TDD Mode | Vizzly Docs](https://docs.vizzly.dev/integration/cli/tdd-mode/?utm_source=webtoolsweekly&utm_medium=newsletter&utm_campaign=2026q1&utm_content=march19)

Vizzly的TDD模式提供本地视觉测试工具，包含实时更新的仪表板、静态报告生成和多种对比模式，支持在开发过程中快速迭代和审查UI变更。

- 🖥️ **TDD模式**：本地运行视觉测试，无需上传云端，实时仪表板显示差异并允许接受基线，适合UI迭代开发。
- 📊 **仪表板模式**：启动后台服务器提供实时仪表板，支持在开发过程中自动更新测试截图并审查变更。
- 📄 **报告模式**：运行一次测试生成静态HTML报告，适用于提交前检查、预提交钩子或与团队分享视觉变更。
- 🎛️ **仪表板视图**：包含比较、统计、设置、项目和构建五个视图，支持筛选、搜索和批量操作如接受所有变更或重置基线。
- 🔍 **差异对比模式**：提供叠加、切换、滑动和并排四种方式，便于详细审查视觉差异。
- 📁 **本地文件存储**：所有测试数据存储在`.vizzly/`目录中，包括基线、当前截图、差异和报告，建议添加到`.gitignore`。
- ⚙️ **命令操作**：支持`vizzly tdd start`启动服务器、`vizzly tdd run`生成报告和`vizzly tdd stop`停止服务器等命令。
- 🌐 **基线管理**：可从云端下载基线，通过仪表板或CLI接受变更，支持全局或按命令调整比较敏感度阈值。

---

### [SDK 概览 | Vizzly 文档](https://docs.vizzly.dev/integration/sdk/overview/?utm_source=webtoolsweekly&utm_medium=newsletter&utm_campaign=2026q1&utm_content=march19)

**原文标题**: [SDK Overview | Vizzly Docs](https://docs.vizzly.dev/integration/sdk/overview/?utm_source=webtoolsweekly&utm_medium=newsletter&utm_campaign=2026q1&utm_content=march19)

Vizzly SDK 提供了一套简洁的视觉测试解决方案，允许开发者在测试中直接捕获屏幕截图，并通过本地服务器或云端平台进行管理和对比。

- 🛠️ **SDK 设计简洁**：仅负责将截图通过 HTTP 发送到本地服务器（端口 47392），由 CLI 处理 API 通信、重试、认证和上传等复杂任务。
- 🌐 **多语言/框架支持**：提供 JavaScript/Node.js（支持 Playwright、Cypress、Jest、Puppeteer）、Ruby（RSpec、Minitest、Cucumber）、Storybook（自动捕获故事）、静态站点（Gatsby、Astro、Jekyll、Next.js 等）、Vitest（替代原生视觉测试）、Ember（Testem 集成）和 Swift（XCTest 集成）的 SDK。
- 🔐 **认证灵活**：TDD 模式无需认证，所有操作在本地进行；云模式（CI/CD）需设置环境变量 `VIZZLY_TOKEN` 使用 API 令牌。
- 🖥️ **TDD 模式（本地开发）**：运行 `vizzly tdd start` 启动服务器后执行测试，截图在本地对比，可通过 `http://localhost:47392` 查看差异并接受/拒绝更改。
- ☁️ **云模式（CI/CD）**：使用 `vizzly run "测试命令"` 将截图上传至云端供团队审核，支持 `--wait` 参数阻塞 CI 流程直至处理完成。
- 🚀 **快速开始**：根据项目技术栈选择对应 SDK 安装并集成，无需额外配置即可开始视觉测试。

---

### [CI/CD集成 | Vizzly 文档](https://docs.vizzly.dev/integration/ci-cd/?utm_source=webtoolsweekly&utm_medium=newsletter&utm_campaign=2026q1&utm_content=march19)

**原文标题**: [CI/CD Integration | Vizzly Docs](https://docs.vizzly.dev/integration/ci-cd/?utm_source=webtoolsweekly&utm_medium=newsletter&utm_campaign=2026q1&utm_content=march19)

Vizzly 是一个用于在 CI/CD 流程中集成视觉回归测试的工具，帮助开发者在代码部署到生产环境前发现界面变化。

- 🚀 **快速集成**：通过设置 `VIZZLY_TOKEN` 环境变量并运行 `vizzly run` 命令，即可将视觉测试加入 CI 管道。
- 🔐 **认证方式**：在 CI 环境中使用 API 令牌进行认证，本地开发则可通过 `vizzly login` 进行 OAuth 认证。
- ⚙️ **核心命令**：
  - `vizzly run`：运行测试并捕获截图，可使用 `--wait` 参数在检测到视觉差异时使构建失败。
  - `vizzly upload`：直接上传已有截图。
  - `vizzly preview`：上传应用构建（如 Storybook、Next.js 导出文件），供审阅者在实际 UI 环境中查看视觉差异。
- 📊 **退出代码**：使用 `--wait` 时，0 表示成功或无视觉变化，1 表示检测到差异需审阅，2 表示构建失败或配置错误。
- 🔧 **CI 提供者示例**：支持 GitHub Actions、GitLab CI、CircleCI、Jenkins、Azure DevOps、Bitbucket Pipelines 和 Travis CI 等主流 CI 工具。
- 🔀 **并行测试**：通过 `--parallel-id` 在多个 CI 任务中分割大型测试套件，并使用 `vizzly finalize` 在所有任务完成后汇总结果。
- 🌐 **环境变量**：提供 `VIZZLY_BUILD_NAME`、`VIZZLY_PARALLEL_ID` 等用于自定义构建信息，并支持覆盖自动检测的 Git 信息。
- 🤖 **自动检测**：工具能自动识别常见的 CI 提供者环境，无需额外配置即可获取正确的 Git 提交信息。

---

### [AI助手集成 | Vizzly文档](https://docs.vizzly.dev/integration/ai-integrations/?utm_source=webtoolsweekly&utm_medium=newsletter&utm_campaign=2026q1&utm_content=march19)

**原文标题**: [AI Assistant Integration | Vizzly Docs](https://docs.vizzly.dev/integration/ai-integrations/?utm_source=webtoolsweekly&utm_medium=newsletter&utm_campaign=2026q1&utm_content=march19)

Vizzly 为 AI 助手提供无缝集成，通过其 CLI 的 JSON 输出接口，使 AI 助手（如 Claude）能够直接查询和操作可视化测试数据，无需特殊配置或服务器。

- 🤖 **AI 助手直接使用 CLI**：AI 助手通过运行 `vizzly` 命令并解析 `--json` 输出与 Vizzly 交互，与人类使用方式一致。
- 🔍 **查询构建状态与故障分析**：AI 可以查询最新构建状态、分析失败原因（如识别具体页面的视觉差异百分比和位置），并帮助调试回归问题。
- 💻 **支持本地 TDD 状态检查**：AI 能检查本地测试驱动开发服务器的运行状态、基线数量和测试结果。
- 📜 **完整的 CLI 命令访问**：AI 代理可使用所有 CLI 命令，包括查看用户、组织、项目、构建详情、比较结果、审批/拒绝比较、添加评论等。
- ⚙️ **简易设置**：只需通过 npm 全局安装 Vizzly CLI 并进行认证，AI 助手（如 Claude Code）即可使用；还可安装插件增强本地 TDD 集成。
- 🔄 **实际工作流示例**：展示了 AI 如何协助审查 PR 中的 UI 变更，自动检查构建结果、识别视觉变化并建议操作。
- 🛠️ **选择 CLI 而非协议的原因**：CLI 方式更简单（无需服务器配置）、通用（兼容任何能运行 shell 的 AI）、易于调试、一致（人机接口统一）且支持离线操作。
- 📚 **LLM 友好文档**：提供针对 AI 优化的文档格式（如 `docs.vizzly.dev/llms.txt`），方便 AI 获取上下文信息。

---

### [评论 | Vizzly 文档](https://docs.vizzly.dev/features/comments/?utm_source=webtoolsweekly&utm_medium=newsletter&utm_campaign=2026q1&utm_content=march19)

**原文标题**: [Comments | Vizzly Docs](https://docs.vizzly.dev/features/comments/?utm_source=webtoolsweekly&utm_medium=newsletter&utm_campaign=2026q1&utm_content=march19)

Vizzly 提供评论功能，支持在构建和截图上进行讨论，包括定位评论、@提及、线程回复和分类管理，以促进团队协作和反馈跟踪。

- 💬 支持在构建和截图上添加评论，包括定位评论和一般评论
- 🧵 评论支持线程回复，保持讨论有序并发送通知
- 🏷️ 评论可分类为一般、批准、拒绝或问题类型
- @ 通过 @提及通知团队成员，提及对象需有项目访问权限
- ✏️ 评论作者或项目管理员可编辑、删除评论，并可标记为已解决
- 🔔 收到提及或回复时发送通知，含直接链接
- 🔒 项目访问者均可评论，编辑删除需权限；公开项目仅限认证用户评论

---

### [组织 | Vizzly 文档](https://docs.vizzly.dev/team-management/organizations/?utm_source=webtoolsweekly&utm_medium=newsletter&utm_campaign=2026q1&utm_content=march19)

**原文标题**: [Organizations | Vizzly Docs](https://docs.vizzly.dev/team-management/organizations/?utm_source=webtoolsweekly&utm_medium=newsletter&utm_campaign=2026q1&utm_content=march19)

Vizzly中的组织用于管理项目、团队成员和账单，是使用平台的基础单元。创建组织时需提供名称等详细信息，系统会生成唯一URL标识并默认分配免费计划，创建者自动成为所有者。组织设置包括更新资料、调整隐私（默认为私有）以及集成GitHub（不同计划权限不同）。成员分为所有者、管理员和普通成员三种角色，拥有不同权限，所有者拥有最高控制权。邀请和管理成员可通过邮件进行，角色可调整但所有者权限不可变更。隐私设置控制组织和项目的公开性，公开项目允许外部访问只读内容。组织按计划计费，免费计划包含基础功能，订阅数量随团队规模自动调整。仪表板提供项目统计、团队动态和活动概览。

- 🏢 组织是Vizzly的核心单元，负责项目管理、成员与账单，使用平台前必须创建
- 🆕 创建组织需填写名称等资料，系统自动生成URL标识并分配免费计划，创建者成为所有者
- ⚙️ 组织设置允许更新资料、调整隐私（默认私有）及集成GitHub（开源计划仅支持公开仓库）
- 👥 成员角色分所有者（全权控制）、管理员（除管理管理员外等同所有者）和普通成员（仅项目参与）
- 📧 所有者和管理员可邀请成员，通过邮件发送限时令牌，角色在邀请时设定且可后期调整
- 🔒 组织默认为私有，公开后方可创建公开项目，私有化将自动隐藏所有项目内容
- 💳 组织按计划计费，免费计划含30天周期，订阅数量随成员增减自动更新
- 📊 仪表板汇总项目统计、团队状态与近期活动，帮助管理者整体把控组织动态

---

### [欢迎来到 Vizzly | Vizzly 文档](https://docs.vizzly.dev/?utm_source=webtoolsweekly&utm_medium=newsletter&utm_campaign=2026q1&utm_content=march19)

**原文标题**: [Welcome to Vizzly | Vizzly Docs](https://docs.vizzly.dev/?utm_source=webtoolsweekly&utm_medium=newsletter&utm_campaign=2026q1&utm_content=march19)

Vizzly是一款视觉测试工具，通过自动比对UI截图来检测视觉变化，支持从测试、设计工具或手动捕获中获取截图，并与基线对比以高亮显示差异，便于团队协作审查和集成到CI/CD流程中。

- 🖼️ 截图捕获：通过测试中的SDK调用或CLI上传截图
- 🔍 自动比对：将截图与基线进行对比分析
- 👁️ 差异审查：并排显示对比结果并高亮差异
- ✅ 团队协作：支持评论和批准构建，促进团队决策
- 🔗 CI/CD集成：在拉取请求中提供状态检查
- 📂 基线管理：Git模式自动跟踪或手动选择基线
- 💬 团队评审：在合并前评论比较结果并批准构建
- 💻 本地开发：开发期间测试视觉变化，无需推送至CI
- 🛠️ 灵活集成：CLI和SDK兼容Playwright、Cypress等测试框架
- 🤖 AI助手支持：Claude、ChatGPT等可通过CLI查询构建和调试回归
- 🚀 快速开始：通过CLI上传截图或集成到现有测试套件
- 📚 详细文档：涵盖CLI、SDK、团队管理和配置指南
- 🎯 适用场景：检测CSS变化导致的布局偏移、跨浏览器渲染差异、组件设计不一致及依赖更新引发的意外变更，特别适用于组件库、电商网站和设计密集型应用

---

### [定价 - 可扩展的可视化开发工作流程 | Vizzly](https://vizzly.dev/pricing/?utm_source=webtoolsweekly&utm_medium=newsletter&utm_campaign=2026q1&utm_content=march19)

**原文标题**: [Pricing - Visual Development Workflow That Scales | Vizzly](https://vizzly.dev/pricing/?utm_source=webtoolsweekly&utm_medium=newsletter&utm_campaign=2026q1&utm_content=march19)

Vizzly是一个可视化测试平台，提供按团队规模定价的灵活方案，支持与现有测试工具无缝集成，并强调无按截图收费的透明成本结构。

- 🧑‍💻 **免费计划**：适用于个人开发者与开源项目，提供基础功能与有限存储
- 🏢 **团队计划**：按用户数阶梯定价（12-29美元/人/月），包含私有项目、存储扩展与高级协作功能
- 🚀 **核心优势**：支持Playwright/Cypress等主流测试框架，内置评审协作系统，成本可预测无隐藏费用
- 🌐 **特色功能**：预览托管服务支持实时UI对比，自动开源验证机制，本地TDD工作流兼容
- 📊 **差异化**：与Percy等按用量计费平台形成对比，提供企业级自部署方案与定制化支持

---

### [GitHub - cheeriojs/cheerio：快速、灵活且优雅的HTML与XML解析及操作库。· GitHub](https://github.com/cheeriojs/cheerio/)

**原文标题**: [GitHub - cheeriojs/cheerio: The fast, flexible, and elegant library for parsing and manipulating HTML and XML. · GitHub](https://github.com/cheeriojs/cheerio/)

Cheerio 是一个快速、灵活且优雅的 HTML 和 XML 解析与操作库，它实现了 jQuery 核心功能的子集，适用于浏览器和服务器环境。

- 🚀 **快速高效**：采用简洁一致的 DOM 模型，解析、操作和渲染性能极高。
- 💡 **类 jQuery 语法**：提供与 jQuery 相似的 API，去除浏览器兼容性差异，易于上手。
- 🌐 **高度灵活**：支持 parse5 和 htmlparser2 作为解析器，可处理几乎所有 HTML/XML 文档。
- 📦 **易于安装**：可通过 npm、yarn 或 bun 等包管理器直接安装。
- 🔧 **丰富功能**：支持加载文档、选择器查询、内容渲染及 DOM 节点操作。
- 🌍 **广泛应用**：被众多生产项目使用，拥有活跃的社区和赞助支持。
- 📜 **开源许可**：基于 MIT 许可证发布，鼓励贡献和协作。

---

### [GitHub - danielroe/beasties: 一个用于内联应用关键CSS并懒加载其余部分的库。· GitHub](https://github.com/danielroe/beasties)

**原文标题**: [GitHub - danielroe/beasties: A library to inline your app's critical CSS and lazy-load the rest. · GitHub](https://github.com/danielroe/beasties)

Beasties 是一个用于内联关键 CSS 并懒加载其余 CSS 的插件，它是 GoogleChromeLabs/critters 的一个维护分支。它通过不依赖无头浏览器来实现快速和轻量级，特别适合预渲染/SSR 的单页应用，并能与 Webpack、Vite 等工具集成。

- 🚀 **快速轻量**：不依赖无头浏览器，处理速度快，资源占用少。
- 🧩 **多工具集成**：提供 Webpack 插件 (`beasties-webpack-plugin`) 和 Vite 插件 (`vite-plugin-beasties`) 方便集成。
- ✂️ **CSS 优化**：自动内联关键 CSS，移除未使用的 CSS 规则（如关键帧和媒体查询），并可压缩输出。
- 🔧 **灵活配置**：支持多种预加载策略、字体处理、日志控制，并可通过注释或配置包含/排除特定 CSS 规则。
- 📦 **容器支持**：通过 `data-beasties-container` 属性限制 CSS 评估范围，提升大文档处理性能。
- 📄 **丰富文档**：提供详细参数说明、使用示例和类似库对比，便于开发者上手和调优。

---

### [获取失败](https://recommendations.page/web-tools-weekly?ref_code=1fb93bdda8&email=<<subscriber@example.com>>)

**原文标题**: [Failed to retrieve](https://recommendations.page/web-tools-weekly?ref_code=1fb93bdda8&email=<<subscriber@example.com>>)

无法总结：获取内容失败，状态码 403。

---

### [GitHub - Toheeb/base：首个多用途无类样式表，拥有最语义化的规则，用于网页的完全定制与个性化。· GitHub](https://github.com/Toheeb/base)

**原文标题**: [GitHub - Toheeb/base: The web's first multipurpose classless stylesheet, with the most semantic rules, for complete customization and personalization of a webpage. · GitHub](https://github.com/Toheeb/base)

Base.css 是一个多用途、无类别的样式表，旨在通过语义化规则实现网页的完全自定义和个性化。

- 🌐 **首个多用途无类别样式表**：Base.css 是网络上首个此类样式表，专注于语义化规则，无需依赖类名即可实现样式定制。
- 🔗 **快速安装**：只需在网页头部添加指定链接即可使用，方便快捷。
- 📖 **详细文档**：提供完整的使用指南和说明，帮助用户深入了解和个性化定制。
- 📄 **开源项目**：项目托管在 GitHub 上，包含 README、许可证和核心文件，支持社区参与和贡献。
- 🛠️ **语义化设计**：通过语义化规则实现高度可定制性，适用于各种网页需求。

---

### [颜色API](https://www.thecolorapi.com/)

**原文标题**: [The Color API](https://www.thecolorapi.com/)

Color API 是一个多功能颜色工具，提供颜色转换、命名、配色方案生成及占位图服务，仅需两个端点即可操作。

- 🎨 通过 `/id` 端点可转换和识别颜色，支持 HEX、RGB、CMYK、HSL、HSV 等多种格式输入
- 📚 返回的颜色对象包含名称（基于2000多种颜色库）、示例图片、多种格式转换值及最佳对比色
- 🌈 使用 `/scheme` 端点生成配色方案，支持单色、类比、互补、三色等多种模式
- 🔗 API 提供 JSON、HTML、SVG 格式输出，SVG 格式可直接嵌入图片使用
- 💡 所有功能开源，开发者可通过文档快速上手并支持项目发展

---

### [GitHub - cloudfour/image-compare：一个用于通过滑块比较图像的网页组件。· GitHub](https://github.com/cloudfour/image-compare)

**原文标题**: [GitHub - cloudfour/image-compare: A web component for comparing images with a slider. · GitHub](https://github.com/cloudfour/image-compare)

这是一个名为 image-compare 的零依赖 Web 组件，用于通过滑块比较两张图片，注重可访问性、性能和渐进增强。

- 🖼️ 一个用于通过滑块比较图片的 Web 组件
- 📦 零依赖，体积小巧
- ♿ 专注于可访问性和性能
- 📄 提供完整文档和 npm 包
- ⭐ 在 GitHub 上获得 132 个星标和 7 个复刻

---

### [字体生成器 – 在线创建精美与时尚文本](https://fontgenerator.design/)

**原文标题**: [Font Generator – Create Fancy & Stylish Text Online](https://fontgenerator.design/)

该在线工具可将普通文本转换为基于Unicode的各类艺术字体样式，用户可直接复制并粘贴到社交媒体、游戏等平台使用，无需安装字体文件。

- 🎨 **功能说明**：通过Unicode字符映射将常规文字转换为视觉风格各异的字体样式，生成内容为可编辑文本而非图像
- 📋 **使用方式**：输入文本后选择字体样式，支持即时预览与一键复制，需启用JavaScript以获得完整交互功能
- 🌐 **兼容特性**：生成的文字可在Instagram、Discord、游戏等多平台正常显示编辑，支持与表情符号混合使用
- 🎭 **字体示例**：提供数学粗体、手写体、哥特体、气泡文字、全角字符等十余种流行Unicode字体样式
- ⚠️ **注意事项**：不同字体对字母/数字支持程度存在差异，各平台渲染效果可能受系统字体设置影响
- 📱 **应用场景**：适用于社交媒体个人简介、游戏昵称、标题设计及短文本创意排版等场景
- 🔍 **扩展探索**：网站提供花式字体、符号库及针对不同平台的专用字体分类导航功能

---

### [安迪·克拉克的卡通文字](https://stuffandnonsense.co.uk/toon-text/tool.html)

**原文标题**: [Andy Clarke’s Toon Text](https://stuffandnonsense.co.uk/toon-text/tool.html)

这是一个名为“Scooter Looter”的在线CSS文本样式生成器，允许用户自定义文字颜色、描边、阴影和字体等属性，并实时预览和导出CSS代码。

- 🎨 提供颜色、描边、阴影和字体等多种文本样式自定义选项
- 👁️ 支持实时预览效果，方便用户调整样式
- 📋 可一键导出生成的CSS代码，便于直接使用
- 🏠 由Stuff & Nonsense公司开发，主要用于CSS和SVG教学目的
- ⚠️ 声明项目仅用于教育，与所用字体和字符的版权方无关联

---

### [Keychains.dev — AI代理的安全凭证委托平台](https://keychains.dev/)

**原文标题**: [Keychains.dev — Secure credential delegation for AI agents](https://keychains.dev/)

Keychains.dev 是一个为AI代理设计的凭证安全委托平台，它允许代理访问API而无需接触原始敏感凭证，通过服务器端注入、用户授权和即时撤销机制，确保权限可控、透明且安全。

- 🔐 使用 `keychains curl` 替换 `curl`，将硬编码凭证替换为模板变量（如 `{{GITHUB_TOKEN}}`），代理无需直接处理原始密钥
- 👁️ 用户需明确批准每个API访问权限，全程可见代理操作范围，并拥有完整的审计追踪
- 🛡️ 凭证在服务器端安全注入，避免提示注入攻击导致凭证泄露，代理无法获取原始秘密
- 🔑 基于SSH密钥对进行机器身份验证，无需密码或API密钥存储在代理环境中
- 📜 支持超过6,800个API提供商，包括OAuth 2.0（带PKCE）、API密钥和基础认证等多种验证方式
- ⚡ 权限可即时撤销，用户可通过仪表板一键取消任何代理的访问，无需等待或密钥轮换
- 🌐 提供范围委托令牌和空白令牌功能，允许安全创建子代理，并限制或要求其获取新权限的用户批准
- 🏗️ 与传统密钥管理器（如Vault）和API网关（如Kong）互补，专注于代理使用时的凭证保护，并针对自主代理设计身份和委托机制

---

### [获取失败](https://openai.com/codex/)

**原文标题**: [Failed to retrieve](https://openai.com/codex/)

无法总结：获取内容失败，状态码 403。

---

### [多视镜](https://getpolyscope.com/)

**原文标题**: [Polyscope](https://getpolyscope.com/)

本文介绍了人工智能在医疗领域的应用现状与前景，重点探讨了其在疾病诊断、药物研发和个性化治疗方面的突破性进展，同时提及了相关的伦理挑战和未来发展趋势。

- 🤖 AI辅助诊断系统能通过分析医学影像快速识别病灶，提升早期疾病检出率
- 💊 机器学习加速新药研发流程，大幅缩短化合物筛选与临床试验周期
- 🧬 基于患者基因组数据的个性化治疗方案正成为精准医疗的核心方向
- ⚖️ 医疗AI面临数据隐私、算法透明度及责任界定等伦理监管挑战
- 🌐 跨机构医疗数据共享与联邦学习技术有望突破数据孤岛困境
- 🏥 智能手术机器人已实现亚毫米级操作精度，推动微创外科发展
- 📱 可穿戴设备结合AI实现全天候健康监测与慢性病管理

---

### [获取失败](https://recs.page/web-tools-weekly?ref_code=a082baf699&email=<<subscriber@example.com>>)

**原文标题**: [Failed to retrieve](https://recs.page/web-tools-weekly?ref_code=a082baf699&email=<<subscriber@example.com>>)

无法总结：获取内容失败，状态码 403。

---

### [GitHub - cloudflare/vibesdk：一个开源的情绪编码平台，助您构建专属的情绪编码环境，完全基于Cloudflare技术栈打造 · GitHub](https://github.com/cloudflare/vibesdk)

**原文标题**: [GitHub - cloudflare/vibesdk: An open-source vibe coding platform that helps you build your own vibe-coding platform, built entirely on Cloudflare stack · GitHub](https://github.com/cloudflare/vibesdk)

Cloudflare VibeSDK 是一个开源的、基于 Cloudflare 开发者平台构建的全栈式 AI 网页应用生成器。它允许用户通过自然语言描述来创建和部署应用程序，并提供了完整的平台供用户自行部署和定制。

- 🧡 **开源平台**：一个可自行部署和定制的 AI 驱动“氛围编程”平台，用于构建应用程序。
- 🚀 **一键部署**：提供在线演示，并可通过“部署到 Cloudflare”按钮快速部署自己的实例。
- 🤖 **AI 代码生成**：通过分阶段开发和智能纠错，根据自然语言描述生成 React + TypeScript + Tailwind 应用。
- ⚡ **实时预览**：生成的应用程序在沙盒化容器中运行，提供即时预览。
- 💬 **交互式聊天**：通过自然语言对话引导和迭代开发过程。
- 📦 **GitHub 集成**：支持将生成的代码直接导出到 GitHub 仓库。
- 🏗️ **基于 Cloudflare 生态**：全面利用 Workers、Durable Objects、D1 数据库、R2 存储、AI Gateway 和容器等 Cloudflare 服务。
- 🔧 **SDK 支持**：提供官方 TypeScript SDK，支持以编程方式构建应用。
- 🔑 **部署要求**：需要 Cloudflare Workers 付费计划、Workers for Platforms 订阅、高级证书管理器以及 Google Gemini API 密钥等。
- 🌐 **域名与 DNS 配置**：需配置自定义域名，并为预览应用设置通配符 CNAME 记录。
- 🏗️ **沙盒实例配置**：可配置容器性能层级（如 standard-3, standard-4），以平衡应用预览性能、构建速度和资源。
- 🔗 **OAuth 设置（可选）**：部署后可配置 Google 或 GitHub OAuth 以实现用户登录功能。
- 🎨 **工作原理**：遵循“用户描述 → AI 分析 → 蓝图规划 → 分阶段代码生成 → 实时预览 → 用户反馈迭代 → 一键部署”的流程。
- 🏠 **本地开发**：支持克隆仓库并运行本地开发服务器进行测试和开发。
- 🔒 **安全与隐私**：提供企业级安全措施，包括加密存储、沙盒执行、输入验证、速率限制和审计日志。
- ❓ **故障排除**：文档提供了常见部署问题（如权限不足、AI 网关认证失败、数据库迁移问题等）的解决方案。
- 🤝 **贡献与资源**：欢迎通过 Fork 和 PR 贡献代码，并提供丰富的社区支持（Discord、论坛）和学习资源。

---

### [GitHub - benjitaylor/agentation：面向智能体的视觉反馈工具。· GitHub](https://github.com/benjitaylor/agentation)

**原文标题**: [GitHub - benjitaylor/agentation: The visual feedback tool for agents. · GitHub](https://github.com/benjitaylor/agentation)

Agentation 是一个与 AI 代理无关的视觉反馈工具，允许用户通过点击页面元素、添加注释并复制结构化输出来帮助 AI 编码代理准确定位相关代码。

- 🛠️ **工具功能** – 点击页面元素自动识别选择器，支持文本选择、多选、区域选择，并能暂停动画以捕捉特定状态
- 📋 **结构化输出** – 可复制包含选择器、位置和上下文信息的 Markdown 格式内容，便于 AI 代理直接定位代码
- 🎨 **界面适配** – 支持深色/浅色模式，匹配用户偏好或手动设置，采用纯 CSS 动画，无运行时依赖
- ⚙️ **技术要求** – 需 React 18+ 和桌面浏览器环境（不支持移动端）
- 📚 **文档与许可** – 完整文档位于 agentation.dev，采用 PolyForm Shield 1.0.0 许可证

---

### [GitHub - steipete/claude-code-mcp: 将Claude Code作为一次性MCP服务器，实现“智能体中的智能体”。· GitHub](https://github.com/steipete/claude-code-mcp)

**原文标题**: [GitHub - steipete/claude-code-mcp: Claude Code as one-shot MCP server to have an agent in your agent. · GitHub](https://github.com/steipete/claude-code-mcp)

这是一个名为 Claude Code MCP Server 的开源项目，它作为一个 MCP（模型上下文协议）服务器，允许 AI 模型通过一个统一的工具直接调用 Claude Code CLI，并自动绕过权限检查，从而执行复杂的代码编辑、文件操作、Git 管理等任务。

- 🚀 **核心功能**：提供一个名为 `claude_code` 的 MCP 工具，让 AI 能直接、无干扰地使用 Claude Code CLI 的强大功能。
- ⚙️ **配置灵活**：支持通过环境变量自定义 Claude CLI 二进制路径，并需完成一次性的权限接受设置。
- 🔌 **集成简便**：可通过 `npx` 快速安装，并配置到 Cursor、Windsurf 等支持 MCP 的客户端中。
- 🛠️ **应用广泛**：适用于代码生成重构、文件系统操作、版本控制、运行终端命令、执行复杂多步骤工作流等场景。
- 🐛 **问题排查**：文档提供了常见的安装、权限及运行错误的解决方案。
- 🧪 **开发者友好**：项目包含完整的测试套件，支持本地开发和贡献，并采用 MIT 开源协议。

---

### [代理技能目录](https://skills.sh/)

**原文标题**: [The Agent Skills Directory](https://skills.sh/)

本文展示了一个技能排行榜，列出了当前最受欢迎的AI技能及其安装次数，涵盖了开发、设计、营销等多个领域。

- 🔍 **技能搜索与排行**：排行榜提供“全部时间”和“24小时趋势”等筛选，收录了超过89,000项技能，便于用户发现热门工具。
- 🥇 **热门技能领先**：榜首“find-skills”安装量高达62.2万次，凸显了技能发现与工具检索的广泛需求。
- 🛠️ **开发与云服务主导**：Vercel、Microsoft（Azure、GitHub Copilot）和Anthropic等厂商的技能包占据前列，涉及前端、AI、云计算等实践。
- 📈 **营销与内容技能丰富**：大量技能专注于SEO、内容策略、文案写作和转化率优化，反映了AI在营销自动化中的应用趋势。
- 🧩 **多样化技能生态**：榜单涵盖从UI设计、音频生成到代码审查、工作流自动化等广泛领域，展示了AI技能生态的多元化和专业化。

---

### [#1 视觉网站反馈工具用于Bug追踪 | BugHerd](https://bugherd.com/ref/home?pscd=partners.bugherd.com&ps_partner_key=NTQ2YWI1Y2MzNGY4&ps_xid=vbScSKDeffqhT1&gsxid=vbScSKDeffqhT1&gspk=NTQ2YWI1Y2MzNGY4)

**原文标题**: [#1 Visual Website Feedback Tool For Bug Tracking | BugHerd](https://bugherd.com/ref/home?pscd=partners.bugherd.com&ps_partner_key=NTQ2YWI1Y2MzNGY4&ps_xid=vbScSKDeffqhT1&gsxid=vbScSKDeffqhT1&gspk=NTQ2YWI1Y2MzNGY4)

BugHerd 是一款专为网站开发和设计团队打造的视觉反馈与错误追踪工具，旨在简化客户反馈流程，提升协作效率。它允许客户直接在网站上点击并评论，自动捕获截图和技术细节，并将反馈转化为可管理的任务。该工具支持与多种项目管理、通讯和开发工具集成，适用于营销机构、网络开发团队及内部团队，尤其适用于用户验收测试、错误追踪和网站反馈等场景。

- 🎯 **直观的网站标注**：客户可直接在网页上点击添加评论，反馈精准定位到具体元素。
- 🤝 **高效的客户协作**：无需客户登录，通过链接即可收集反馈，所有任务和对话集中展示，实时更新进度。
- 🐞 **可操作的错误报告**：自动捕获浏览器版本、屏幕分辨率等技术细节，附带截图，简化错误复现和修复。
- 📋 **集成看板任务管理**：反馈自动转为看板上的可追踪任务，支持优先级排序，并可一键同步至其他项目管理工具。
- 🎥 **视频反馈功能**：支持录制和分享交互式反馈会话，提升沟通清晰度。
- 🌐 **公开反馈收集**：通过小工具收集来自网站访问者的广泛反馈，适用于持续优化。
- 🔗 **丰富的工具集成**：无缝连接 Asana、Jira、Slack、WordPress 等 20 多种常用工具，适配现有工作流。
- 🏢 **多类型团队适用**：特别受营销机构、网络开发机构和内部团队青睐，显著提升客户满意度和交付效率。
- ⚡ **快速设置与免费试用**：通过浏览器扩展或代码片段快速部署，提供 7 天免费试用，无需信用卡。

---

### [GitHub - p2r3/beheader：媒体文件的多语言生成器 · GitHub](https://github.com/p2r3/beheader)

**原文标题**: [GitHub - p2r3/beheader: Polyglot generator for media files · GitHub](https://github.com/p2r3/beheader)

Beheader 是一个用于生成媒体文件多态（polyglot）的工具，可将图像、视频、音频、HTML、PDF 和 ZIP 等多种文件格式合并为单一文件，并根据文件扩展名在不同系统中呈现不同内容。

- 🛠️ **功能用途**：将图像、视频/音频、HTML、PDF 和 ZIP 等文件合并成一个多态文件，根据扩展名（如 .ico、.mp4、.html 等）在不同程序中显示相应内容。
- 📦 **依赖环境**：需要 Bun JavaScript 运行时、Linux 系统，以及 ffmpeg、ImageMagick、zip 等工具；支持通过 Nix 自动安装依赖。
- 🚀 **使用方式**：通过命令行运行，指定输出文件、输入图像和视频/音频路径，可选附加 HTML、PDF、ZIP 等文件，并支持添加额外数据。
- ⚠️ **技术注意**：合并过程可能非无损（如视频重新编码为 MP4，图像转换为 PNG），ZIP 类文件（如 JAR、APK）支持合并，但部分程序可能因元数据问题报错。
- 📄 **项目信息**：开源项目，采用 GPL-3.0 许可证，GitHub 上获 1.4k 星标，主要用 JavaScript 和 Nix 编写。

---

### [GitHub - ChartGPU/ChartGPU：美观、开源、基于WebGPU的图表库 · GitHub](https://github.com/ChartGPU/ChartGPU)

**原文标题**: [GitHub - ChartGPU/ChartGPU: Beautiful, open source, WebGPU-based charting library · GitHub](https://github.com/ChartGPU/ChartGPU)

ChartGPU 是一个基于 WebGPU 构建的 TypeScript 图表库，旨在处理海量数据时提供流畅、交互式的渲染体验，其核心优势在于高性能，能够以 60 FPS 渲染数千万数据点。

- 🚀 **高性能渲染**：基于 WebGPU 加速，可流畅渲染高达 5000 万个数据点，支持实时流式更新。
- 📊 **丰富的图表类型**：支持折线图、面积图、柱状图、散点图、饼图和 K 线图等多种系列。
- 🎨 **交互式标注系统**：提供参考线、点标记和文本标签等标注功能，支持交互式创建、编辑和拖拽。
- 🔄 **实时数据流**：通过 `appendData` 方法支持流式数据更新，并兼容多种数据格式。
- 🧩 **数据间隙处理**：支持通过 `null` 值处理数据中的间隙，并可选择是否连接断点。
- 🌡️ **散点密度图**：提供 GPU 加速的密度/热图模式，可清晰展示超大量散点的分布结构。
- 📱 **多图表仪表盘**：支持共享 GPU 设备和渲染管道缓存，高效构建多图表实时仪表盘。
- ⚙️ **易于集成**：提供 npm 包安装，并配有专门的 React 绑定库 `chartgpu-react`。
- 📖 **完善的文档**：包含详细的 API 参考、示例代码和架构说明，便于开发者使用和贡献。
- 🔓 **开源与跨平台**：采用 MIT 许可证，支持现代主流浏览器（需 WebGPU 功能）。

---

### [它的悬停](https://www.itshover.com/)

**原文标题**: [Its Hover](https://www.itshover.com/)

Its Hover 是一个开源的动态图标库，提供可编辑的 React 组件，内置流畅动画，专为现代界面设计打造，支持 Next.js 和 shadcn 等框架。

- 🎨 **开源可编辑**：图标完全开源，社区共同维护，支持自由定制和修改。
- ⚡ **动态优先设计**：每个图标都以动画为核心功能，注重交互意图而非装饰。
- 🤝 **强大支持**：项目由 Vercel 等工具提供基础设施，确保快速可靠。
- 💼 **品牌合作**：欢迎赞助商加入，助力互动图标的未来发展。
- 🌍 **社区喜爱**：受到众多开发者和设计师的喜爱，拥有丰富的展示案例。
- 🔗 **便捷使用**：提供图标浏览、GitHub 星标、多种赞助方式（包括加密货币）等快速链接。

---

### [获取失败](https://recommendations.page/web-tools-weekly?ref_code=2fdf2b1ce7&email=<<subscriber@example.com>>)

**原文标题**: [Failed to retrieve](https://recommendations.page/web-tools-weekly?ref_code=2fdf2b1ce7&email=<<subscriber@example.com>>)

无法总结：获取内容失败，状态码 403。

---

### [SVG工作室](https://www.svg.studio/)

**原文标题**: [SVG Studio](https://www.svg.studio/)

本文介绍了人工智能在医疗领域的应用现状与前景，重点探讨了其在疾病诊断、治疗方案优化及医疗管理效率提升方面的作用，同时简要提及了相关的技术挑战和伦理考量。

- 🤖 AI辅助诊断系统通过分析医学影像提升疾病识别准确率
- 💊 基于算法的个性化治疗方案推荐助力精准医疗发展
- ⚡ 智能流程管理工具优化医院资源分配与患者就诊体验
- 🧠 自然语言处理技术加速医疗文献分析与临床决策支持
- ⚖️ 数据隐私保护与算法透明度成为行业关注焦点

---

### [GitHub - xdadda/mini-photo-editor：在线WebGL照片编辑器，支持特效、滤镜和裁剪功能 · GitHub](https://github.com/xdadda/mini-photo-editor)

**原文标题**: [GitHub - xdadda/mini-photo-editor: Online webgl photo editor with effects, filters and cropping · GitHub](https://github.com/xdadda/mini-photo-editor)

这是一个基于WebGL2的在线照片编辑器，所有图像处理均在浏览器本地完成，无需上传至服务器，确保100%的隐私安全。它提供了丰富的编辑功能，包括裁剪、透视校正、色彩调整、滤镜效果等，并支持多种现代图像格式。

- 🌐 **在线隐私编辑** – 图像完全在浏览器本地处理，无需上传到后端服务器，保障用户隐私。
- 🛠️ **多功能编辑工具** – 支持裁剪、透视校正、图像大小调整、光影色彩调整、晕影、清晰度/锐化、降噪等功能。
- 🎨 **高级效果与滤镜** – 提供颜色曲线调整、类似Instagram的滤镜、图像混合、模糊效果（散景/高斯模糊）以及修复画笔。
- 📊 **专业辅助功能** – 包含分割视图对比、颜色直方图、Exif/Tiff/GPS信息显示，并支持Display-P3色彩空间和sRGB正确工作流程。
- ⚙️ **技术特性与限制** – 支持多种现代图像格式（如HEIC、JPEG-XL、AVIF），但受WebGL限制，16位图像处理目前仅限于8位输出。
- 📄 **开源项目** – 基于MIT许可证开源，使用mini-js、mini-gl和mini-exif技术构建，欢迎在GitHub上提交功能请求。

---

### [放置猫咪](https://placecats.com/)

**原文标题**: [Place Cats](https://placecats.com/)

PlaceCats 是一个在线服务，通过简单的URL参数即可生成指定尺寸的猫咪占位图片，支持选择特定猫咪、随机图片、灰度效果，并能调整图片的适配方式和裁剪位置。

- 🐱 在URL后添加宽高尺寸即可生成对应大小的猫咪图片，例如：`https://placecats.com/300/200`
- 📝 可通过在尺寸前添加猫咪名字（如`/neo/`）来指定特定猫咪，留空则随机选择
- ⚫️ 添加`/g/`参数可生成黑白灰度效果的图片
- 🔧 使用`fit`参数控制图片适配方式：`cover`（裁剪填充，默认）、`contain`（完整包含）、`fill`（拉伸填充）、`inside`（限制内嵌）、`outside`（最小边适配）
- 🎯 使用`position`参数设置裁剪焦点位置：`center`（居中，默认）、`top`/`bottom`/`left`/`right`（对应边缘）
- 🌐 网站提供交互式URL构建工具，可实时预览并生成图片链接
- ❤️ 支持通过“给模特买零食”的方式赞助该项目

---

### [Tooooools.app](https://www.tooooools.app/)

**原文标题**: [Tooooools.app](https://www.tooooools.app/)

Tooooools是一个在线图像处理工具，用户可上传图片并应用各种效果后导出使用。

- 🖼️ 上传图片并选择调整效果后导出
- 🛠️ 由Daniil Sukhovskoy创建，支持个人和商业用途
- 📄 无需署名但欢迎注明来源，工具可免费使用

---

### [联系网络工具周刊](https://webtoolsweekly.com/contact?opt=classifieds)

**原文标题**: [Contact Web Tools Weekly](https://webtoolsweekly.com/contact?opt=classifieds)

如需在《Web Tools Weekly》投放广告，请查看广告计划页面了解选项，并通过下方表单咨询当前可预订时段或直接预订。请注意，此表单仅用于广告咨询；若有关乎简报的常规问询或工具提交，请通过X私信、Bluesky聊天或订阅后回复邮件联系。

- 📄 查看广告计划页面了解投放选项
- 📩 通过表单咨询可预订时段或直接预订广告位
- ⚠️ 该表单仅限广告业务使用
- 📬 常规问询或工具提交需通过社交平台或邮件联系

---

### [超强记忆](https://supermemory.ai/)

**原文标题**: [Supermemory](https://supermemory.ai/)

Supermemory是一个专注于为AI智能体构建先进上下文与记忆基础设施的研究与产品实验室，提供完整的上下文堆栈解决方案，包括用户画像、记忆图谱、检索、提取器和连接器五大层次，旨在让AI不仅记住信息，更能深入理解用户意图与上下文。

- 🏆 在MemoryBench等基准测试中表现领先，延迟低于300毫秒，每月处理超过1000亿令牌
- 🧠 提供完整的上下文堆栈，涵盖用户画像、记忆图谱、检索、提取器和连接器五大层次
- 🔧 为开发者提供Supermemory API，支持RAG、记忆和提取功能，提供TypeScript和Python SDK
- 🌐 为普通用户提供个人Supermemory，实现跨AI工具的统一记忆和上下文共享
- ⚡ 采用自定义向量图谱引擎，实现知识更新、合并和推理，而非简单追加
- 🔗 支持从Notion、Slack、Google Drive等多种来源自动同步数据
- 💬 已获得超过10,000名活跃用户和众多开发者好评，显著提升AI代理性能
- 💰 提供从免费到企业级的透明定价方案，包含无限存储和用户

---

### [Refind – 每日精神食粮，准时送达。](https://refind.com/?utm_source=xn6y&utm_medium=ran-x-rfnd)

**原文标题**: [Refind – Brain food, delivered daily](https://refind.com/?utm_source=xn6y&utm_medium=ran-x-rfnd)

每日精选，为您提供高质量文章摘要，从数千篇文章中筛选出最佳内容，直接发送至您的邮箱。目前已有超过50万求知者信赖并喜爱我们的服务，用户评价高达4.9分（满分5星）。

- 📧 每日分析数千篇文章，仅推送精华内容至邮箱
- ✅ 需验证邮箱地址以确保顺利接收
- ❤️ 深受50万+求知者喜爱与信赖
- ⭐ 用户评价优异，评分达4.9/5星

---

### [Vecti - 光速设计](https://vecti.com/)

**原文标题**: [Vecti - Design at the speed of light](https://vecti.com/)

Vecti是一款专为现代UX工作流打造的协作式设计工具，旨在帮助设计师更快地构建卓越用户体验。它提供实时协作、高性能渲染引擎和直观界面，支持从免费到专业的灵活付费方案。

- 🚀 **实时协作设计** – 支持多成员同时编辑与审阅，所有资源和成果在团队间无缝共享。
- ⚡ **高性能渲染引擎** – 提供高保真、像素级完美的设计渲染，支持无限规模项目。
- 🎨 **直观界面与组件库** – 界面简单易用，可快速创意；支持创建可复用组件与共享资源库。
- 🔒 **灵活的分享与权限** – 可按团队或项目设置查看与编辑权限，并提供全屏演示模式。
- 💰 **按需付费的定价模式** – 提供免费版（最多5个项目、2名编辑）和专业版（按编辑计费，支持无限项目、高级权限与优先支持）。
- ❓ **全面的支持与折扣** – 提供工作日邮件支持、教育及开源项目折扣，免费版无需信用卡即可开始使用。
- 🌍 **以用户为中心的使命** – 工具基于欧盟隐私标准构建，注重性能、隐私与创意自由，致力于服务设计师与开发者。

---

### [AgentMail | AI代理专用邮箱](https://www.agentmail.to/)

**原文标题**: [AgentMail | Email for AI agents](https://www.agentmail.to/)

AgentMail是一个专为AI智能体设计的电子邮件收件箱API平台，使AI代理能够像人类一样通过电子邮件进行双向沟通。

- 📧 提供API优先的电子邮件收件箱服务，专为AI智能体构建
- 💰 已获得600万美元种子轮融资，由Y Combinator等机构支持
- ⚡ 可即时创建收件箱，支持自定义域名和附件处理
- 🔗 具备实时事件、语义搜索和数据提取功能
- 🌍 已实现全球范围1亿+邮件递送，采用企业级冗余架构
- 🤖 支持多种应用场景：浏览器代理、日程管理、文档处理、客户服务
- 🛠️ 提供Python/TypeScript等SDK，开发者可快速集成
- 📈 获多家企业认可，证明其可靠性和扩展性
- 🔒 专注邮件送达率，确保邮件进入收件箱而非垃圾文件夹

---

### [科技生产力 | 为渴望高效完成工作的科技专业人士打造的每周通讯](https://techproductivity.co/)

**原文标题**: [Tech Productivity | A Weekly Newsletter for Tech Pros Who Want to Get Stuff Done](https://techproductivity.co/)

这是一份面向技术专业人士的每周通讯，提供精选工具与资源，广受订阅者好评。

- 📧 每周一封精选邮件，无垃圾内容，保障隐私
- 👍 已拥有超过3400名订阅者，读者反馈积极
- 💬 用户评价称其内容简洁、价值高，是每周期待的信息来源
- 🔧 帮助读者发现实用技术工具，提升工作效率
- ✨ 被多位用户评为最喜爱且从不错过的行业简报

---

### [SejHey - 强大且性价比高的翻译服务](https://sejhey.com/)

**原文标题**: [SejHey - Powerful and cost effective translations](https://sejhey.com/)

该平台是一个AI驱动的本地化解决方案，帮助用户轻松翻译和分发网站、应用、游戏等内容，提供高效、低成本的多语言管理工具。

- 🚀 **快速添加语言**：10秒内即可发布新语言版本，无需手动处理繁琐的翻译文件
- 🤖 **AI智能翻译**：利用人工智能提供上下文感知的翻译建议，支持术语库统一管理
- 💰 **高性价比定价**：提供免费及低价套餐（0/15/39欧元），比同类平台成本更低
- 🔌 **无缝集成**：支持Next.js、React、GitHub等开发工具，通过CDN实时更新翻译内容
- 👥 **协作功能**：包含任务分配、截图上下文、术语库、质量检查等团队协作工具
- 🌍 **区域化翻译**：支持同一语言的不同区域变体，无需创建独立语言项目
- 📊 **版本管理**：具备变更日志、多环境发布（测试/预发/生产）、Webhook通知等专业功能

---

### [VideoEditAI.app | 一站式AI视频编辑与生成工具](https://videoeditai.app/)

**原文标题**: [VideoEditAI.app | All-in-one AI video editor & generator](https://videoeditai.app/)

VideoEditAI.app是一个集成了Runway Aleph、Kling O1、Veo/Sora、Nano Banana等多种领先AI模型的多合一视频编辑与生成平台。它通过简单的文本提示，让用户能够快速完成专业级的视频编辑、生成、风格转换、对象处理等复杂任务，显著提升创作效率并降低成本。

- 🎁 **新用户福利**：注册即可获得免费积分，用于体验平台各项AI视频编辑功能。
- 🚀 **核心功能**：支持视频编辑、生成、图像创建，并能进行风格迁移、环境变换、对象增删、镜头生成等12项高级AI操作。
- 🛠️ **操作简便**：只需三步——上传素材、选择模型并输入提示、导出结果，无需专业技术背景。
- 💰 **成本优势**：平台积分比单独使用各AI模型便宜10%，提供高性价比的多模型工作流。
- ⏱️ **高效省时**：复杂视频编辑可在几分钟内完成，大幅减少传统VFX和重拍的成本与时间。
- 🎬 **专业适用**：受到电影制片人、内容创作者、营销人员等专业人士好评，可用于电影、社交媒体、纪录片等多种项目。
- 🔒 **安全可靠**：采用行业标准加密，用户内容不会被用于AI训练，并提供企业级安全选项。
- ❓ **常见问题**：平台提供详细的FAQ，涵盖格式支持、处理时长、安全措施及专业功能等常见疑问。

---

### [@smmarotta.bsky.social 在 Bluesky 上](https://bsky.app/profile/smmarotta.bsky.social/post/3mhdp2puchs2x)

**原文标题**: [@smmarotta.bsky.social on Bluesky](https://bsky.app/profile/smmarotta.bsky.social/post/3mhdp2puchs2x)

这篇文章讨论了AI在专业领域应用的一个常见误解，强调写作本身就是思考和深度分析的过程，而非仅仅是记录结果的机械性工作。

- 📝 写作与思考密不可分，是分析和理清思路的关键过程
- 🤖 AI倡导者常误以为思考快速、写作只是繁琐的收尾工作
- 💡 实际工作中，写作是深化和完成分析的核心环节
- ⚖️ 尤其在法律等专业领域，这一误解可能影响对AI工具的正确使用

---

### [未找到标题](https://x.com/LouisLazaris)

**原文标题**: [No title found](https://x.com/LouisLazaris)

该页面提示JavaScript功能未启用，导致无法正常使用X平台，并提供了相应的解决建议与支持信息。

- 🌐 浏览器JavaScript功能已禁用，导致X平台无法正常运行
- 🔧 建议启用JavaScript或更换至受支持的浏览器
- 📖 可访问帮助中心查看支持的浏览器列表
- 🛡️ 部分隐私扩展可能造成访问问题，建议暂时禁用后重试
- 🔄 页面提供“重试”功能供用户再次尝试加载
- ⚖️ 页脚包含服务条款、隐私政策等法律文件链接

---

### [路易斯拉扎里斯在蓝天的博客](https://bsky.app/profile/louislazaris.com)

**原文标题**: [@louislazaris.com on Bluesky](https://bsky.app/profile/louislazaris.com)

这是一个高度交互的网络应用，需要JavaScript支持。它并非简单的HTML界面，而是基于Bluesky社交平台和AT协议构建的互动体验。

- 🌐 这是一个依赖JavaScript的高度交互式网络应用，非简单HTML界面
- 🔗 关联Bluesky社交平台（bsky.social）及其底层AT协议（atproto.com）
- 👤 用户Louis Lazaris：前端开发工程师兼新闻简报策划人
- 📧 运营多个专业平台：Web工具周刊、科技生产力、VS Code资讯
- 🎸 同时经营吉他教学YouTube频道@tunejotter

---

### [提交工具至Web工具周刊](https://webtoolsweekly.com/submit)

**原文标题**: [Submit a Tool to Web Tools Weekly](https://webtoolsweekly.com/submit)

本文邀请前端开发者提交各类实用工具，以丰富开发资源库。

- 📦 可提交工具类型包括库、框架、插件、脚本及各类应用程序
- 🚫 不接受文章或教程类内容，生产力工具需转投其他通讯
- 📮 可通过X或Bluesky平台联系指定账号进行提交
- 🔧 征集范围涵盖网页开发、编程及设计相关工具

---

### [AgeMDB - 电影演员年龄查询 | 演员当时多大年纪？](https://agemdb.com/)

**原文标题**: [AgeMDB - Check Actor Ages in Movies | How Old Was the Actor?](https://agemdb.com/)

AgeMDB是一个专注于查询演员在拍摄电影时具体年龄的数据库网站，提供演员的当前年龄及在影片上映时的年龄信息，并包含电影作品列表和年龄对比工具。

- 🎬 网站核心功能是查询演员在特定电影上映时的年龄及其当前年龄，例如可查看罗伯特·唐尼在《复仇者联盟4》上映时为54岁
- 🔍 用户可通过搜索电影名称或演员姓名来获取详细的演员年龄数据和完整的演员表信息
- 📊 网站提供年龄对比工具，可发现与用户当前年龄相同的演员曾出演的电影作品
- 🎂 所有数据来源于电影数据库（TMDB），基于已验证的出生日期和电影上映日期进行计算
- 🚫 网站明确声明不用于外貌对比、长相相似度判断或人格特征分析，仅提供年龄相关数据
- 💡 该工具旨在帮助影迷从年龄角度分析演员职业生涯、发现电影趣闻并研究影视历史
- 🆓 网站所有功能完全免费使用，无需注册，且数据库会持续更新最新电影和演员信息

---

### [Web Tools Weekly | 前端开发者周刊](https://webtoolsweekly.com/)

**原文标题**: [Web Tools Weekly | A Weekly Newsletter for Front-end Developers](https://webtoolsweekly.com/)

《Web Tools Weekly》是一份面向网页开发者的每周通讯，提供前沿工具与实用技巧，深受订阅者信赖与好评。

- 📧 每周一封无垃圾邮件，已拥有超过1.3万订阅者，注重隐私保护
- ⭐ 读者评价极高，被誉为“最实用的技术简报之一”和“前端开发者必备资源”
- 🔧 持续分享创新的JavaScript技巧与工具，帮助开发者提升工作效率
- ❤️ 长期订阅者众多，许多人表示多年来每期必读并从中获得巨大价值

---

