### [React 状态周报第 436 期：2025 年 7 月 16 日](https://react.statuscode.com/issues/436)

**原文标题**: [React Status Issue 436: July 16, 2025](https://react.statuscode.com/issues/436)

概述  
本期内容涵盖 React 生态的最新动态、框架更新、教程资源及工具推荐，包括 React 历史回顾、Next.js 新特性、React Native 支持 Node-API 等亮点，同时提供开发者学习资源和实用工具介绍。  

- ⚛️ **React 发展史**：通过代码回顾 React 从 Facebook 起源到现今的演变，解析其核心哲学与重大 API 决策。  
- 🚀 **Next.js 进阶**：React 19 与 Next.js 15 全栈开发训练营，涵盖认证、文件上传等实战技能。  
- 📱 **React Native 突破**：支持 Node-API，实现跨平台代码共享及原生模块预构建。  
- 🐝 **Wasp 框架**：类 Rails 的 React/Node/Prisma 框架公布开发路线图。  
- 🔄 **Next.js 15.4 更新**：性能优化与 Turbopack 兼容性改进，并预告 Next.js 16 新特性。  
- ⏳ **React Hooks 迁移**：大型应用从类组件/MobX 转向函数式组件与 Hooks 的三年实践。  
- 🤖 **AI 编程工具**：利用 Lovable 快速构建安全的全栈应用。  
- 🛠️ **实用工具推荐**：  
  - `react-easy-crop`（交互式图像裁剪）  
  - `Hyper Fetch`（强化版 Fetch 库）  
  - 动画天气效果（WebGL 实现雨雪雾）。  
- 📢 **JavaScript 生态动态**：Node.js 多版本更新、Vercel 收购 NuxtLabs、Nuxt 4.0 发布等。

---

### [React 代码演变史 | 趣味编程](https://playfulprogramming.com/posts/react-history-through-code)

**原文标题**: [
	The History of React Through Code | Playful Programming
](https://playfulprogramming.com/posts/react-history-through-code)

React 的发展历程及其核心设计理念的演变，展示了其从诞生至今的持续一致性与创新。

- 🚀 **React 的起源**：由 Jordan Walke 创建，旨在解决 Facebook 内部框架 BoltJS 的问题，最终演变为 React 并在 2013 年开源。
- 🎨 **JSX 的引入**：通过将 HTML 嵌入 JavaScript，提供更灵活的模板处理，同时优化了 XSS 保护和调试体验。
- 🔄 **虚拟 DOM (VDOM)**：通过 VDOM 实现高效的 DOM 更新，显著提升了大型应用的性能。
- ⚛️ **组件化开发**：从类组件到函数组件的演进，最终通过 Hooks 实现逻辑复用和更简洁的代码结构。
- 🛠️ **Fiber 架构**：2017 年引入的 Fiber 架构，支持并发渲染、错误处理和性能优化，为未来功能奠定基础。
- 📡 **数据获取的演进**：从手动状态管理到 `use` API 和 Suspense，实现了更高效的数据加载和错误处理。
- 🌐 **服务器组件 (RSC)**：React 19 引入的服务器组件，优化了 SSR 并支持双向数据流，提升了用户体验。
- 🔮 **未来展望**：包括 `<Activity>` API 和 React 编译器，进一步优化状态管理和性能。

React 的设计始终围绕一致性、可组合性和性能优化，展现了其长期的技术愿景和开发者友好理念。

---

### [宣布 React Native 支持 Node-API](https://www.callstack.com/blog/announcing-node-api-support-for-react-native)

**原文标题**: [Announcing Node-API Support for React Native](https://www.callstack.com/blog/announcing-node-api-support-for-react-native)

React Native 宣布支持 Node-API，这是一个跨平台的本地模块系统，旨在简化开发流程并提升性能。以下是关键点总结：

- 🚀 **Node-API 引入 React Native**：社区合作将 Node.js 的本地模块系统 Node-API 引入 React Native，提供运行时无关的稳定接口。  
- 🔧 **跨平台与多语言支持**：Node-API 支持多种编程语言（如 C++、Rust、Swift 等），并兼容 Node.js、Deno 和 Bun 等运行时。  
- ⏱️ **预构建模块加速构建**：通过预构建本地模块，显著减少应用构建时间（如 Android 可缩短至 7 秒）。  
- 🌍 **生态系统共享**：利用现有 Node-API 生态（如 WebRTC、Web Audio），促进 Web 与 React Native 的代码复用。  
- 🛠️ **适用场景**：适合跨平台共享代码、高性能计算（如 AI、加密）或调用平台 API 的模块开发。  
- 📦 **当前进展**：支持 iOS 和 Android，需使用特定 Hermes 版本（PR 合并后将解除限制）。  
- 🤝 **社区协作**：感谢 Microsoft、NativeScript 和 Callstack 等团队的关键贡献。  
- 📚 **示例与文档**：提供示例仓库（[node-api-example-lib](https://github.com/callstackincubator/node-api-example-lib)）和详细文档供开发者参考。  
- 💡 **未来展望**：鼓励开发者尝试并贡献，推动 React Native 原生模块的预构建和生态扩展。

---

### [React Native 迎来苹果设备端 LLM 支持](https://www.callstack.com/blog/on-device-apple-llm-support-comes-to-react-native)

**原文标题**: [On-Device Apple LLM Support Comes to React Native](https://www.callstack.com/blog/on-device-apple-llm-support-comes-to-react-native)

React Native 现已支持苹果设备端大型语言模型（LLM），通过新发布的 @react-native-ai/apple 包，开发者可以在 React Native 生态中使用苹果的本地基础模型，实现私密、快速且离线的 AI 体验。

- 🚀 **预览版发布**：@react-native-ai/apple 现已开放预览，需 React Native 0.80+ 或 Expo Canary，并启用新架构。  
- 🍏 **苹果智能技术**：基于约 30 亿参数的 Transformer 模型，专为移动设备优化，支持动态适配器（LoRA）和高级压缩技术。  
- 🔒 **隐私与性能**：本地计算确保数据隐私、零延迟响应和离线功能，适用于智能文本编辑、隐私保护助手等场景。  
- 📝 **功能支持**：包括文本生成与流式传输、Vercel AI SDK 兼容性，以及结构化 JSON 输出（支持 Zod 模式）。  
- 🛠️ **未来计划**：稳定版将与 iOS 26 同步发布，新增工具调用和按需适配器支持，并扩展至 Android 设备。  
- 📦 **快速开始**：通过 `npm install @react-native-ai/apple` 安装，文档和示例即将推出。  
- 🌟 **社区参与**：欢迎开发者试用并提供反馈，GitHub 仓库已开放。

---

### [黄蜂](https://wasp.sh/)

**原文标题**: [Wasp](https://wasp.sh/)

概述：Wasp 是一个类似 Rails 的全栈框架，支持 React、Node.js 和 Prisma，旨在快速开发并简化部署流程。通过简单的配置文件，开发者可以高效构建应用，并享受内置的全栈功能如身份验证、类型安全和 RPC 等。

- 🚀 **快速开发全栈应用**：Wasp 提供类似 Rails 的开发体验，支持 React、Node.js 和 Prisma，一天内即可完成应用开发并通过 CLI 一键部署。  
- ⚙️ **简洁的配置文件**：通过 `.wasp` 文件声明应用的高层逻辑（如路由、身份验证），减少样板代码。  
- 🔐 **全栈身份验证**：内置多种登录方式（Google、GitHub、邮箱），无需依赖第三方服务。  
- 🔄 **类型安全的 RPC**：自动生成客户端与服务器间的类型安全通信层。  
- ☁️ **简易部署**：支持主流平台，提供 CLI 工具简化部署流程。  
- 📧 **开箱即用功能**：包括邮件发送、后台任务调度、WebSockets 等。  
- 🛠️ **开源与扩展性**：完全开源，支持自定义 API 路由、数据库填充等高级功能。  
- 📚 **示例丰富**：提供 Todo 应用、实时投票等示例项目，方便快速上手。  
- 💬 **社区好评**：开发者称赞其学习曲线低、开发效率高，适合个人和小团队。  
- 🏗️ **持续更新**：公开路线图展示未来功能规划，如更多技术栈支持。  

（注：根据内容长度，部分功能点已合并，确保核心信息完整且简洁。）

---

### [Wasp 现已公开开发路线图！ | Wasp](https://wasp.sh/blog/2025/07/08/public-wasp-dev-roadmap)

**原文标题**: [Wasp now has a public development roadmap! | Wasp](https://wasp.sh/blog/2025/07/08/public-wasp-dev-roadmap)

Wasp 公开了开发路线图，旨在提高透明度并集中规划，重点关注 1.0 版本发布、AI 集成及创新功能开发。

- 🚀 Wasp 公开了开发路线图，增强项目透明度，方便用户了解未来计划。  
- 🏗️ 路线图通过 GitHub 项目管理，仅包含 Epic 级别任务，保持简洁高效。  
- 🎯 主要目标是为 1.0 版本做准备，涵盖核心功能优化、实验性功能及 AI 集成。  
- 🔍 核心优化包括改进开发体验（DX）、修复现有功能的粗糙边缘。  
- 🌟 主功能升级涉及 Operations、Auth 等，提升灵活性和用户体验。  
- 🧪 实验性功能如全栈模块（FSMs）和 Wasp Studio，探索模块化开发新方向。  
- 🤖 AI 相关计划包括优化 AI 辅助编程体验，如集成 Cursor/Claude 等工具。  
- 📢 邀请社区参与反馈，用户可通过 GitHub 或 Discord 提出建议或订阅感兴趣的任务。  
- 🔄 路线图将定期更新，反映季度调整和任务进展。  
- ℹ️ Open SaaS 模板有独立开发计划，未包含在此路线图中。

---

### [在 Vercel 五年间学到的五件事 | Lee Robinson](https://leerob.com/vercel)

**原文标题**: [5 things I learned from 5 years at Vercel | Lee Robinson](https://leerob.com/vercel)

在 Vercel 工作五年后，作者总结了五点关键经验，涵盖了工作与生活的平衡、领导力、团队管理、决策方式以及适应变化的重要性。

- 🏖️ **工作与生活的平衡**：作者起初将全部热情投入工作，甚至在蜜月期间处理工作事务，但后来意识到建立界限和支持系统的重要性，以实现工作与生活的和谐。
  
- ⚡ **提高工作效率**：作为领导者，推动团队快速交付是关键。设定激进的截止日期可以加速项目进展，同时允许偶尔的延期，以保持团队的动力和创造力。
  
- 📈 **团队扩展与管理**：为了应对快速增长，必须持续招聘优秀人才，并对表现不佳的成员及时反馈。拥有一个能够自主运作的团队是实现规模化的关键。
  
- 🚫 **避免“俯冲轰炸”式管理**：作者反思了自己在晋升为 VP 后，未经充分了解就干预团队决策的错误，强调了建立信任和团队共识的重要性。
  
- 🔄 **灵活调整决策**：作者最初坚持审核所有社交媒体内容，但后来意识到应区分决策的重要性，并赋予团队更多自主权，从而提高效率和团队参与感。

---

### [Reddit——互联网的核心](https://www.reddit.com/r/reactjs/comments/1lwwpnm/2025_remix_or_nextjs_which_one_should_i_choose/)

**原文标题**: [Reddit - The heart of the internet](https://www.reddit.com/r/reactjs/comments/1lwwpnm/2025_remix_or_nextjs_which_one_should_i_choose/)

2025 年关于 Remix 与 Next.js 框架选择的讨论，聚焦于长期可靠性、适用场景及特定动态数据库应用的适配性。

- 🏗️ 社区探讨 2025 年 Remix 与 Next.js 的优劣对比，寻求明确选择依据  
- ⚖️ 关注两大框架在生产环境中的长期稳定性与可靠性差异  
- 🎯 讨论特定使用场景下（包括开发者体验）何者表现更优  
- 💡 针对动态数据库交互的 WYSIWYG 类网页应用，寻求框架适配建议  
- 🌐 推荐加入 Reactiflux Discord 社区获取更多 React 生态讨论支持

---

### [Next.js 15.4 | Next.js](https://nextjs.org/blog/next-15-4)

**原文标题**: [Next.js 15.4 | Next.js](https://nextjs.org/blog/next-15-4)

Next.js 15.4 版本发布，重点优化性能、稳定性和 Turbopack 兼容性，并预告了 Next.js 16 的新功能。

- 🚀 **Turbopack 构建**：`next build --turbopack` 已通过全部 8298 项集成测试，并应用于 vercel.com。  
- 🔧 **稳定性改进**：Next.js 和 Turbopack 进行了多项性能和稳定性优化。  
- 🔜 **Next.js 16 预览**：包括缓存组件、优化客户端路由、DevTools 调试等功能。  
- ⚙️ **升级指南**：提供自动升级 CLI 或手动安装命令，支持新项目创建。  
- 🐞 **问题反馈**：鼓励用户尝试 Turbopack 并报告问题，为生产环境做准备。  
- 📅 **未来计划**：Next.js 16 将引入更多实验性功能，如缓存组件和 Turbopack 构建的公开测试版。  
- 🙏 **贡献者致谢**：感谢超过 3000 名开发者的贡献，包括 Next.js、Turbopack 和文档团队的成员。

---

### [世界上最长的一次 React Hooks 迁移 | 作者：Chris Krogh | 2025 年 6 月 | The Craft](https://craft.faire.com/the-worlds-longest-react-hooks-migration-8f357cdcdbe9?gi=c3855bbf9332)

**原文标题**: [The world’s longest React hooks migration | by Chris Krogh | Jun, 2025 | The Craft](https://craft.faire.com/the-worlds-longest-react-hooks-migration-8f357cdcdbe9?gi=c3855bbf9332)

Faire 公司完成了其前端代码库历史上最长的迁移，从类组件和 MobX 类转向功能组件和 hooks，提升了代码库的可维护性和性能。迁移过程历时多年，克服了诸多挑战，最终显著改善了开发效率和用户体验。

- 🚀 **迁移背景**：Faire 将最大的 React 应用从类组件和 MobX 迁移到功能组件和 hooks，提升了代码可维护性和性能。  
- ⏳ **延迟原因**：2019 年 hooks 发布时，公司刚完成 MobX 迁移，因快速发展和产品需求未立即转向 hooks。  
- 📈 **问题积累**：代码库增长导致类组件数量激增，维护和性能问题日益突出。  
- 🛠️ **迁移策略**：2022 年启动迁移，使用 ESLint 规则跟踪进度，升级 mobx-react 以支持 hooks。  
- 🤖 **自动化工具**：与 Grit 合作，部分自动化类组件到功能组件的转换，但测试和审查仍是瓶颈。  
- 🏆 **团队激励**：通过 useQuery 等 hooks 的显著优势激励团队，最终在 2025 年强制完成迁移。  
- 📊 **迁移效果**：数据预取提升页面加载速度，订单量增加 5%；移除 MobX 后，React 编译器实验显示性能提升 25%。  
- 🔮 **未来计划**：继续在其他 React 应用中移除 MobX，利用 AI 加速迁移。  
- 💡 **经验总结**：迁移需周密计划、定制工具和耐心，最终带来更模块化、高效的代码库。

---

### [如何使用 Clerk、Lovable 和 Supabase 构建 AI 编码规则应用](https://clerk.com/blog/build-app-with-lovable-supabase-clerk?utm_source=cooper_press&utm_medium=newsletter&utm_campaign=ai-coding-rules&utm_content=07-16-25-rs&dub_id=zszlGYh8JGSq18oU)

**原文标题**: [How to build an AI coding rules app with Clerk, Lovable, and Supabase](https://clerk.com/blog/build-app-with-lovable-supabase-clerk?utm_source=cooper_press&utm_medium=newsletter&utm_campaign=ai-coding-rules&utm_content=07-16-25-rs&dub_id=zszlGYh8JGSq18oU)

本文介绍了如何利用 Clerk、Lovable 和 Supabase 构建一个安全的 AI 编码规则应用的全过程。

- 🛠️ **工具组合**：使用 Lovable 的 AI 生成平台、Clerk 的认证服务和 Supabase 的数据库存储，快速构建全栈应用。
- 🤖 **Lovable 简介**：Lovable 是一个通过聊天提示生成全栈应用的 AI 平台，支持 React 和 Supabase 等流行框架。
- 🔑 **Clerk 集成**：Clerk 提供简化的用户认证管理，只需一行代码即可添加登录表单，如`<SignIn />`。
- 🏗️ **应用构建**：通过 Lovable 提示生成一个存储 AI 编码规则的应用，包括规则名称、项目名称和规则内容等字段。
- 🛡️ **认证配置**：在 Clerk 仪表板中创建应用并配置登录方法，确保与 Lovable 生成的 React 应用兼容。
- 🗄️ **Supabase 存储**：使用 Supabase 作为后端服务，配置行级安全（RLS）策略，确保用户只能访问自己的数据。
- 🔄 **数据安全**：通过 Clerk 的 JWT 令牌和 Supabase 的 RLS 策略，确保用户数据的安全性和隔离性。
- 🐛 **问题修正**：提供常见问题的解决方案，如类型不匹配和认证失败，确保应用顺利运行。
- 🚀 **部署与测试**：完成应用构建后，进行测试并确保所有功能按预期工作，包括添加和存储编码规则。
- 💡 **结论**：AI 工具如 Lovable 结合 Clerk 和 Supabase，可以快速构建安全应用，但仍需人工监督以确保质量和安全性。

---

### [松散同步多个 Tauri 进程中的（Zustand）存储](https://www.gethopp.app/blog/tauri-window-state-sync)

**原文标题**: [Loosely synchronize your (Zustand) stores in multiple Tauri processes](https://www.gethopp.app/blog/tauri-window-state-sync)

概述：本文介绍了在 Tauri 多进程（窗口）中实现 Zustand 存储的松散同步方法，解决了多窗口应用中状态管理的问题，并提供了实现代码和改进方向。

- 🚀 **问题背景**：在 Hopp 开发中，使用 Zustand 进行状态管理时，多窗口应用的状态同步成为挑战。  
- 🔄 **解决方案**：采用松散同步策略，避免复杂性和异步调用污染代码。  
- 📡 **实现机制**：通过 Tauri 事件系统广播和监听状态变更，使用标志位防止无限循环更新。  
- 💡 **代码示例**：提供了完整的实现代码，包括状态定义、同步逻辑和初始状态水合。  
- ⚠️ **改进方向**：可能丢失事件或出现竞态条件，理想方案是将状态保存在后端（Rust）并加锁更新。  
- 🔗 **示例代码**：可参考提供的代码库链接，了解具体实现细节。  
- 🎯 **结论**：该方法为多窗口状态管理提供了简单有效的解决方案，适合大多数应用场景。

---

### [Tauri 2.0 | Tauri](https://v2.tauri.app/)

**原文标题**: [Tauri 2.0 | Tauri](https://v2.tauri.app/)

Tauri 2.0 是一个用于创建小型、快速、安全且跨平台应用程序的工具，支持多种前端框架和操作系统，并提供强大的安全性和性能。

- 🚀 **快速开始**：提供多种安装方式（Bash、PowerShell、npm、Yarn 等）来创建 Tauri 项目。  
- 🔄 **前端独立**：支持任何前端框架，无需更改现有技术栈。  
- 🌍 **跨平台**：可构建适用于 Linux、macOS、Windows、Android 和 iOS 的应用程序。  
- 📡 **进程间通信**：前端使用 JavaScript，应用逻辑使用 Rust，并支持 Swift 和 Kotlin 深度集成。  
- 🔒 **高安全性**：安全性是 Tauri 团队的首要任务和核心创新点。  
- 📦 **极小体积**：利用操作系统原生 Web 渲染器，应用体积可小至 600KB。  
- 🦀 **基于 Rust**：以性能和安全性为核心，Rust 是下一代应用程序的理想语言。  
- © **版权声明**：2025 年 Tauri 贡献者，采用 CC-BY / MIT 许可。

---

### [React Native 图片列表：用 React Native 重现苹果和谷歌相册——第 1 部分 | Software Mansion](https://blog.swmansion.com/react-native-image-list-recreating-apple-google-photos-in-react-native-part-1-7f73fb74fc63?gi=7b76650ba196)

**原文标题**: [React Native Image List: Recreating Apple & Google Photos in React Native — Part 1 | Software Mansion](https://blog.swmansion.com/react-native-image-list-recreating-apple-google-photos-in-react-native-part-1-7f73fb74fc63?gi=7b76650ba196)

概述：本文是系列文章的第一部分，介绍了如何使用 React Native 构建一个类似 Apple Photos 和 Google Photos 的高性能照片列表应用。文章重点讨论了从设备加载照片、优化列表组件以及提升用户体验的关键技术。

- 📱 目标：使用 React Native 构建高性能照片列表，模仿 Apple 和 Google Photos 的功能和体验。
- 🎥 资源：提供视频教程和公开的 GitHub 仓库，方便读者实践。
- 🖼️ 第一步：从设备加载照片，采用分批处理和缓存策略，优化加载时间。
  - Android 加载时间较长，iOS 则更快。
  - 使用`expo-media-library`分批加载照片，每批 50 张。
  - 使用`react-native-mmkv`缓存照片数据，提升后续加载速度。
- 🖌️ 第二步：比较 React Native 的`<Image>`组件和`Expo Image`组件。
  - iOS 上`<Image>`加载速度更快，但`Expo Image`在 Android 上表现更优。
  - `Expo Image`提供更多功能，如缓存策略和 Android 特定的 RGB 解码格式。
- 🛠️ 第三步：使用 mipmaps 技术优化图像加载。
  - 生成适合列表视图的缩小版本图像，减少内存使用和提高渲染速度。
  - 在 iOS 上自定义 mipmap 生成，以解决`Expo Image`的兼容性问题。
- 📜 第四步：选择合适的列表组件：`FlatList`、`FlashList`和`LegendList`。
  - `FlashList`在大数据集和低端设备上表现最佳，滚动更流畅。
  - `FlatList`内存使用最少，适合高性能设备和小数据集。
  - `LegendList`纯 JavaScript 实现，但滚动时容易出现空白区域。
- 🌍 跨平台：优化技术适用于所有平台，未来将扩展到更多设备。
- 🙏 致谢：感谢贡献者和团队的支持，并邀请读者参与社区讨论和代码实践。

---

### [如何测试 React 服务器组件 | Nico 的博客](https://www.nico.fyi/blog/how-to-test-react-server-component)

**原文标题**: [How to test React Server Component | Nico's Blog](https://www.nico.fyi/blog/how-to-test-react-server-component)

React Server Components（RSC）的测试方法目前尚无官方支持，但开发者通过开源社区找到了一种临时解决方案。

- 🛠️ **作者背景**：Nico Prananta 分享了他在 Next.js 项目中使用 RSC 的经验，并指出目前缺乏官方测试工具。  
- 🤖 **挑战**：即使 LLM 也无法提供 RSC 测试方案，因为其逻辑需依赖实际代码实现。  
- 💡 **解决方案**：基于 Steven Robert 的 Gist 代码，通过`renderServerComponent`函数模拟 RSC 渲染测试，利用 React 内部 API 绕过客户端限制。  
- ⚠️ **注意事项**：代码涉及 React 内部未公开 API（`__CLIENT_INTERNALS...`），未来 React 版本更新可能导致失效。  
- 🔍 **实现逻辑**：  
  - 递归解析异步组件（`evaluateServerComponent`）。  
  - 代理 React 调度器以区分服务端/客户端组件。  
- 📂 **使用步骤**：将代码复制到项目中，调用`renderServerComponent`即可测试 RSC。  
- 🔗 **示例项目**：作者提供了[GitHub 示例](https://github.com/testing-library/react-testing-library/issues/1209)供参考。  
- 🌟 **期待**：未来官方能推出更稳定的测试方案。  

（注：Bluesky/GitHub 等外链及标签列表未纳入核心摘要）

---

### [react 简易裁剪](https://valentinh.github.io/react-easy-crop/)

**原文标题**: [react-easy-crop](https://valentinh.github.io/react-easy-crop/)

一个 React 组件，用于轻松实现图像裁剪交互  

- 🌐 **演示功能**：支持缩放、旋转和显示裁剪结果  
- 🛠️ **核心特性**：拖拽和缩放交互操作  
- 📏 **尺寸输出**：提供像素和百分比两种裁剪尺寸数据  
- 🖼️ **图像兼容**：支持多种格式（JPEG/PNG/GIF），可传入 URL 或 Base64 字符串  
- 📱 **移动适配**：对移动端设备友好  
- 💻 **代码示例**：提供基础 Hook 用法示例及 Codesandbox 实例

---

### [GitHub - ValentinH/react-easy-crop: 一个 React 组件，用于简单交互式裁剪图片/视频](https://github.com/ValentinH/react-easy-crop)

**原文标题**: [GitHub - ValentinH/react-easy-crop: A React component to crop images/videos with easy interactions](https://github.com/ValentinH/react-easy-crop)

概述：react-easy-crop 是一个 React 组件，用于轻松裁剪图像和视频，支持多种交互方式和功能。

- 🌟 项目拥有 2.5k 星标和 172 个 fork，采用 MIT 许可证。
- 🎥 支持图像和视频裁剪，包括 JPEG、PNG、GIF 和 HTML5 视频格式。
- 🖱️ 提供拖拽、缩放和旋转等交互功能。
- 📏 支持以像素或百分比形式返回裁剪尺寸。
- 📱 移动设备友好，适配各种屏幕。
- 🛠️ 提供多种示例，包括基本用法、TypeScript 示例、实时输出、服务器端裁剪等。
- 📦 安装简单，可通过 yarn 或 npm 安装。
- 🎨 支持自定义样式和类名，可手动注入 CSS 样式。
- ⚠️ 已知问题包括在模态框中显示时尺寸不正确，建议避免使用缩放动画。
- 🔧 提供丰富的属性配置，如裁剪形状、网格显示、初始裁剪区域等。
- 📄 详细文档和社区视频教程，帮助快速上手。
- 👥 由 Valentin Hervieu 维护，有众多贡献者参与开发。

---

### [GitHub - cookpete/react-player: 一个 React 组件，用于播放多种 URL，包括文件路径、YouTube、Facebook、Twitch、SoundCloud、Streamable、Vimeo、Wistia 和 DailyMotion](https://github.com/cookpete/react-player)

**原文标题**: [GitHub - cookpete/react-player: A React component for playing a variety of URLs, including file paths, YouTube, Facebook, Twitch, SoundCloud, Streamable, Vimeo, Wistia and DailyMotion](https://github.com/cookpete/react-player)

ReactPlayer 是一个 React 组件，支持播放多种来源的媒体文件，包括文件路径、YouTube、Facebook、Twitch、SoundCloud、Streamable、Vimeo、Wistia 和 DailyMotion 等。

- 🎥 **功能概述**：ReactPlayer 是一个多功能的媒体播放组件，支持多种媒体来源和格式。
- 🔧 **安装使用**：通过 npm 或 yarn 安装，支持懒加载和代码分割。
- 🚀 **高级功能**：支持自定义控件、响应式设计、多源和轨道、移动端适配等。
- 📜 **配置选项**：提供丰富的配置选项和回调函数，支持自定义播放器行为。
- 🔄 **版本迁移**：v3 版本不向后兼容，需参考迁移指南进行升级。
- 📱 **移动端限制**：某些移动浏览器需要用户交互才能播放媒体。
- 🌟 **社区支持**：由 Mux 团队维护，保持开源并持续改进。
- 📂 **项目结构**：包含示例、脚本、源代码和测试文件，结构清晰。
- 📄 **文档资源**：提供详细的 README、许可证和贡献指南。
- 🤝 **贡献感谢**：欢迎社区贡献，特别感谢 Patreon 支持者。

---

### [机器人验证](https://cookpete.com/react-player/)

**原文标题**: [Bot Verification](https://cookpete.com/react-player/)

验证中，请稍候...  

- 🔍 系统正在确认您是否为真人用户  
- ⏳ 此过程可能需要短暂等待  
- 🤖 旨在防止自动化程序滥用或攻击  
- ✅ 完成后即可正常访问或继续操作

---

### [无缝请求与实时连接 | HyperFetch](https://hyperfetch.bettertyped.com/)

**原文标题**: [Seamless Requests and Real-Time Connectivity | HyperFetch](https://hyperfetch.bettertyped.com/)

Hyper Fetch 是一个现代化的数据交换框架，旨在简化与任何远程 API 的连接，提供类型安全和高效的开发体验。

- 🚀 **统一数据层**：Hyper Fetch 提供类型安全、卓越的开发体验和灵活的架构，适用于现代开发需求。  
- 🤖 **AI/LLM 支持**：标准化架构支持 AI 适配器和 SDK 生成，内置 LLM 支持，适用于流式响应和实时更新。  
- 📊 **标准化请求**：通过 Swagger/OpenAPI 代码生成，提升开发效率，减少错误。  
- 🔍 **专用开发者工具**：HyperFlow 提供实时请求跟踪、错误分析和性能监控，全面掌控数据和缓存。  
- ⚙️ **核心功能**：框架无关的核心模块，支持构建强大的 API 客户端和实时 WebSocket 通信。  
- ⚛️ **React 集成**：通过自定义钩子简化数据获取和状态管理。  
- 🔄 **SDK 生成**：从 OpenAPI/Swagger 生成类型安全的 SDK，支持 tRPC-like 语法和自动补全。  
- 🌐 **框架无关**：兼容 React、Next.js、Node.js 等，适用于 SPA、SSR 和静态站点。  
- 🔒 **类型安全**：充分利用 TypeScript，自动生成类型，增强开发信心。  
- 💡 **开源灵活**：几乎零依赖，可无缝集成到任何项目，支持社区贡献。  
- 💖 **赞助支持**：通过 GitHub Sponsors 或合作支持项目发展。  
- 🛠️ **提升效率**：减少样板代码，专注于构建用户喜爱的功能。

---

### [GitHub - BetterTyped/hyper-fetch: ⚡ 数据获取与实时交换框架](https://github.com/BetterTyped/hyper-fetch)

**原文标题**: [GitHub - BetterTyped/hyper-fetch: ⚡ Fetching and realtime data exchange framework.](https://github.com/BetterTyped/hyper-fetch)

Hyper Fetch 是一个专注于简单性和高效性的数据获取和实时数据交换框架，具有类型安全和用户友好的设计，支持浏览器和服务器端集成。

- ⚡ **框架特点** - 提供类型安全、用户友好的接口，支持实时数据交换和高效架构创建。  
- 🔮 **核心功能** - 包括简单设置、请求取消、请求去重、队列管理、响应缓存、离线优先等。  
- 📦 **安装方式** - 支持通过 npm 或 yarn 安装核心包、Socket 包和 React 包。  
- 🛠 **使用示例** - 提供简单的客户端设置、请求发送、动态数据绑定及 React 集成示例。  
- 🔄 **实时交互** - 支持生命周期钩子、手动触发请求和动态数据提交。  
- 💖 **社区支持** - 鼓励通过 GitHub Sponsors 赞助项目发展。  
- 📜 **开源协议** - 采用 Apache-2.0 许可证，代码托管在 GitHub 上。

---

### [GitHub - rauschermate/react-weather-effects: 在任何背景图片上添加动态天气效果（雨、雪、雾）](https://github.com/rauschermate/react-weather-effects)

**原文标题**: [GitHub - rauschermate/react-weather-effects: Animated weather effects (rain, snow, fog) on any background image](https://github.com/rauschermate/react-weather-effects)

一个基于 React 和 Next.js 的天气效果动画项目，提供雨、雪、雾三种动态效果，支持交互式切换和响应式设计。

- 🌦️ 项目名称：react-weather-effects，提供动态天气效果（雨、雪、雾）的背景动画  
- 🚀 演示地址：react-weather-effects.vercel.app  
- ✨ 核心功能：  
  - 🌧️ 逼真的 WebGL 降雨效果（含闪电）  
  - ❄️ Three.js 实现的雪景粒子系统（轻柔/暴风雪模式）  
  - 🌫️ 可调节浓度的雾效叠加  
- 🛠️ 技术栈：  
  - React + Next.js（App Router）  
  - WebGL 自定义着色器 + Three.js  
  - GSAP 动画 + Tailwind CSS UI  
- 🌈 效果分类：  
  - 雨（暴雨/细雨/辐射雨）  
  - 雪（轻柔/暴风雪）  
  - 雾（薄雾/浓雾）  
- 📂 开发指南：  
  - `npm install`安装依赖  
  - 通过`npm run dev`启动本地服务  
- 📄 开源协议：MIT License  
- ⭐ 项目数据：1 星标 / 0 分支 / 96% JavaScript 代码

---

### [3D 演示](https://react-weather-effects.vercel.app/snow)

**原文标题**: [3D demo](https://react-weather-effects.vercel.app/snow)

天气现象概述  
- 🌧️ 雨：降水形式，水滴从云层落下。  
- ❄️ 雪：固态降水，由冰晶组成，通常在低温下形成。  
- 🌫️ 雾：近地面水汽凝结导致能见度降低的天气现象。  
- 🌬️ 微风：轻柔的风，通常带来舒适的感觉。  
- ⚡ 暴风雨：强风伴随降雨或雷电的剧烈天气现象。

---

### [GitHub - rpearce/react-medium-image-zoom: 🔎 🏞 源自 medium.com 的 React 图片缩放库（2016 年发布）](https://github.com/rpearce/react-medium-image-zoom)

**原文标题**: [GitHub - rpearce/react-medium-image-zoom: 🔎 🏞 The original medium.com-inspired image zooming library for React (since 2016)](https://github.com/rpearce/react-medium-image-zoom)

react-medium-image-zoom 是一个受 Medium.com 启发的 React 图片缩放库，自 2016 年发布以来广受欢迎。

- 🔎 支持多种图片元素：`<img>`、`<div>`、`<picture>`、`<figure>` 和 `<svg>`  
- 🎨 提供自定义缩放模态内容的功能  
- ♿ 支持多种屏幕阅读器，如 JAWS、NVDA、VoiceOver 和 TalkBack  
- 🛠 兼容主流工具：Gatsby、Next.js 等  
- 📦 零依赖，轻量级  
- ⚡ 支持懒加载 (`loading="lazy"`)  
- 🎭 提供受控和非受控组件两种使用方式  
- 🖌 可自定义样式和过渡效果  
- 🔄 支持手势滑动关闭缩放  
- 📜 详细的 API 文档和迁移指南（v4 到 v5）  
- 🌟 开源项目，拥有活跃的社区贡献者  

该库适用于需要优雅实现图片缩放功能的 React 项目，特别适合内容展示类应用。

---

### [故事书 - Storybook](https://rpearce.github.io/react-medium-image-zoom/?path=/story/galleries--image-gallery)

**原文标题**: [storybook - Storybook](https://rpearce.github.io/react-medium-image-zoom/?path=/story/galleries--image-gallery)

好的，请提供您需要总结的文本内容，我会按照您要求的模板进行整理，包括概述总结和带表情符号的要点列表。  

示例模板：  

概述总结  
- 📌 要点 1  
- 🌟 要点 2  
- 🔍 要点 3  

请提供具体文本，我会为您生成符合要求的总结。

---

### [发布 v0.17.0 · wasp-lang/wasp · GitHub](https://github.com/wasp-lang/wasp/releases/tag/v0.17.0)

**原文标题**: [Release v0.17.0 · wasp-lang/wasp · GitHub](https://github.com/wasp-lang/wasp/releases/tag/v0.17.0)

Wasp 语言项目 v0.17.0 版本发布，包含重大变更、新功能、错误修复和小改进。

- ⚠️ **重大变更**：`usernameAndPassword`认证方法的`login()`函数现在接受包含`username`和`password`的对象，而非两个单独参数；TypeScript 配置需更新；不再自动生成`favicon.ico`；Express 升级至 v5。  
- 🎉 **新功能**：支持 Railway 一键部署；新增`onAfterEmailVerified`认证钩子；支持 Slack 作为认证提供商；支持 Prisma `Decimal`类型返回；新增客户端环境变量验证和`prismaSetupFn`数据库钩子。  
- 🐞 **错误修复**：修复 OAuth 逻辑竞争条件、未登录时`useAuth()`请求失败、Prisma 文件无模型导致应用无法渲染、Wasp Studio 在 Firefox 中无法使用等问题。  
- 🔧 **小改进**：优化无路由定义时的错误提示；TypeScript 支持现代化；支持 Wasp 符号跳转定义；改进类型传播和错误处理等。  
- 🙏 **社区贡献者**：感谢@0xTaneja、@Scorpil、@Reikon95 的贡献。

---

### [黄蜂](https://wasp.sh/)

**原文标题**: [Wasp](https://wasp.sh/)

概述总结  
Wasp 是一个类似 Rails 的全栈 Web 应用开发框架，支持 React、Node.js 和 Prisma，旨在快速构建和部署应用。  

- 🚀 **快速开发**：通过简单的配置文件和高阶逻辑，Wasp 能快速生成全栈应用源码。  
- 🔧 **简单配置**：使用`.wasp`文件声明应用的高阶细节，减少样板代码。  
- 🔐 **全栈认证**：支持多种登录方式（Google、GitHub、邮箱等），无需第三方依赖。  
- 🔄 **类型安全**：全面支持 TypeScript，自动生成跨栈类型。  
- ⚡ **RPC 通信**：提供类型安全的 RPC 层，方便客户端与服务器交互。  
- 🛠️ **简单部署**：通过 CLI 命令一键部署到主流平台。  
- 📧 **邮件发送**：集成邮件服务，轻松发送邮件。  
- 📅 **任务调度**：支持定义、调度和运行持久化任务。  
- 🌟 **开源社区**：完全开源，欢迎贡献，拥有活跃的 Discord 社区。  
- 📚 **丰富示例**：提供多个示例项目（如 Todo 应用、实时投票应用等）供参考。  
- 🏆 **用户案例**：已有用户成功构建 SaaS、内部工具等，验证了 Wasp 的高效性。  
- 📅 **持续更新**：公开路线图，未来功能持续迭代中。  
- ❓ **常见问题**：解答了与 Next.js、Rails 等框架的差异及学习难度等问题。

---

### [GitHub - Clariity/react-chessboard: 适用于 React 应用的现代化响应式棋盘组件](https://github.com/Clariity/react-chessboard)

**原文标题**: [GitHub - Clariity/react-chessboard: A modern, responsive chessboard component for React applications.](https://github.com/Clariity/react-chessboard)

一个现代的、响应式的 React 国际象棋棋盘组件。

- ♟️ 项目名称：react-chessboard，由 Clariity 开发，MIT 许可证。
- 🌟 项目特点：423 个星标，132 个分支，支持 TypeScript。
- 🎨 功能亮点：拖放操作、自定义棋子、动画效果、移动端支持、可访问性等。
- 📦 安装方式：支持 pnpm、yarn 和 npm 安装。
- 🚀 快速开始：通过简单的导入和配置即可使用 Chessboard 组件。
- 📚 文档资源：提供详细的文档和 API 参考，支持框架集成如 Next.js、Vite 等。
- 🤝 社区与贡献：鼓励社区贡献，提供 Discord 社区交流，支持新功能开发和文档改进。
- 🔧 技术栈：主要使用 TypeScript 开发，占比 96.7%。
- 📄 许可证：MIT 许可证，由 Ryan Gregory 维护。

---

### [@storybook/core - Storybook](https://react-chessboard.vercel.app/?path=/docs/how-to-use-basic-examples--docs)

**原文标题**: [@storybook/core - Storybook](https://react-chessboard.vercel.app/?path=/docs/how-to-use-basic-examples--docs)

好的，请提供您需要总结的文本内容，我会按照以下模板为您生成简洁的要点列表：  

overview summary  

- 🌟 Emoji 要点  

（示例：若原文关于“健康饮食”，可能生成如下总结）  

均衡饮食对健康至关重要  
- 🥦 多吃蔬菜水果，补充维生素和纤维  
- 🍗 适量摄入蛋白质，如鱼肉、豆类  
- 🚫 减少高糖高盐食品，避免慢性病风险  
- 💧 每日保持充足水分，促进新陈代谢  

请提供您的文本内容，我会立即为您处理！

---

### [发布 v6.4.0 · tinyplex/tinybase · GitHub](https://github.com/tinyplex/tinybase/releases/tag/v6.4.0)

**原文标题**: [Release v6.4.0 · tinyplex/tinybase · GitHub](https://github.com/tinyplex/tinybase/releases/tag/v6.4.0)

tinybase 发布 v6.4.0 版本，新增 React Native SQLite 数据持久化模块。

- 🚀 发布新版本 **v6.4.0**，包含 `persister-react-native-sqlite` 模块。  
- 📱 支持通过 `react-native-sqlite-storage` 库在 React Native 中持久化数据到 SQLite 数据库。  
- 💡 使用示例：引入库、创建数据库连接、初始化存储并调用 `persister.save()` 保存数据。  
- 🔄 提供简单的 API，开发者可快速集成（代码示例已展示基本用法）。  
- ❓ 鼓励用户反馈使用体验和建议。  
- 🔍 其他导航选项包括代码、议题、安全等（页面部分内容加载异常需刷新）。

---

### [发布 v8.8.0 · mui/mui-x · GitHub](https://github.com/mui/mui-x/releases/tag/v8.8.0)

**原文标题**: [Release v8.8.0 · mui/mui-x · GitHub](https://github.com/mui/mui-x/releases/tag/v8.8.0)

MUI-X v8.8.0 版本发布，包含数据网格、图表、树视图等多个组件的功能改进和错误修复，特别感谢 13 位贡献者的努力。

- 🚀 **版本发布**：MUI-X v8.8.0 发布，包含多项功能更新和错误修复。  
- 🌍 **本地化支持**：数据网格新增印尼语（id-ID）本地化支持。  
- 📊 **图表功能增强**：新增图表缩放预览功能，优化轴高亮控制和默认域限制。  
- 🛠 **数据网格改进**：修复了 `useGridSelector` 在严格模式下的订阅问题，优化滚动条填充和分页数据源缓存。  
- 🌳 **树视图修复**：解决了懒加载和复选框选择启用时的滚动问题。  
- 📝 **文档更新**：新增独立金字塔图表页面，优化移动端条形图示例。  
- 🤝 **其他改进**：包括代码基础设施的修复和 Prettier 配置的优化。  
- 🙏 **致谢**：特别感谢 13 位贡献者，包括社区成员和团队成员的辛勤工作。

---

### [Node.js — 2025 年 7 月 15 日星期二安全版本发布](https://nodejs.org/en/blog/vulnerability/july-2025-security-releases)

**原文标题**: [Node.js — Tuesday, July 15, 2025 Security Releases](https://nodejs.org/en/blog/vulnerability/july-2025-security-releases)

Node.js 项目于 2025 年 7 月 15 日发布了安全更新，涉及 24.x、22.x 和 20.x 版本，修复了两个高危漏洞。

- 🚨 **Windows 设备名称路径遍历漏洞 (CVE-2025-27210)**  
  - 影响所有活跃版本（20.x、22.x、24.x），特别是 Windows 用户使用 `path.join` API 时。  
  - 漏洞涉及 CON、PRN 等设备名称绕过 `path.normalize()` 的保护机制。  

- ⚠️ **V8 引擎 HashDoS 漏洞 (CVE-2025-27209)**  
  - 仅影响 24.x 版本，攻击者可通过控制字符串生成哈希碰撞，导致服务拒绝。  
  - Node.js 团队将其列为高危漏洞，尽管 V8 团队未认定其安全性问题。  

- 📥 **更新版本**  
  - 修复版本：v20.19.4、v22.17.1、v24.4.1，建议用户立即升级以确保安全。  

- 📅 **发布时间**  
  - 补丁于 2025 年 7 月 15 日或之后发布，结束支持版本同样受影响。  

- 🔗 **后续联系**  
  - 安全政策及漏洞报告流程详见 Node.js 官网和 GitHub 安全文档。  
  - 建议订阅 nodejs-sec 邮件列表获取安全公告。

---

### [JavaScript 日期测验](https://jsdate.wtf/)

**原文标题**: [The JavaScript Date Quiz](https://jsdate.wtf/)

JavaScript 的 Date 类测试挑战  
- 🧐 测试你对 JavaScript Date 类的了解程度  
- 🖥️ 使用 NodeJS 24.4.0 在 MacBook Pro 上验证（时区设为 BST，UTC+1）  
- ❤️ 由 samwho 制作  
- 📝 包含 20 个问题的小测验  
- 🔄 可逐个回答问题或直接查看结果（0/0 正确率）  
- 📤 支持分享和复制测验链接

---

### [NuxtLabs 加入 Vercel - Vercel](https://vercel.com/blog/nuxtlabs-joins-vercel)

**原文标题**: [NuxtLabs joins Vercel - Vercel](https://vercel.com/blog/nuxtlabs-joins-vercel)

NuxtLabs（Nitro 和 Nuxt 的创建者及管理者）将加入 Vercel。Nuxt 作为全栈 Web 框架深受开发者信任，每周下载量超百万次；Nitro 是跨框架、平台和负载的服务器运行时。团队核心成员包括 Nuxt 创始人 Sebastien Chopin 等，他们将继续保持项目 MIT 许可、公开路线图及社区优先。Vercel 承诺推动开放网络，支持 Nuxt 和 Nitro 保持独立开源，未来将免费开放多项工具。

- 🚀 NuxtLabs（Nitro 和 Nuxt 团队）宣布加入 Vercel，继续推进开源生态  
- 🌐 Nuxt 框架每周下载超百万次，被全球大企业广泛使用  
- ⚙️ Nitro 是跨平台服务器运行时，为 AI 代理、API 等提供统一标准  
- 👥 核心团队包括 Nuxt 创始人 Sebastien Chopin 等，保持项目独立性与开源性  
- 🔓 所有项目维持 MIT 许可、公开路线图，社区仍是核心  
- 🤝 Vercel 承诺支持开放网络，不设技术锁定，中立服务所有框架  
- 🎉 未来将免费开源 Nuxt Studio MDC、Nuxt UI Pro 等工具  
- 🌟 强调对开发者及开源人才的长期投入与共同愿景

---

### [发布 Nuxt 4.0 · Nuxt 博客](https://nuxt.com/blog/v4)

**原文标题**: [Announcing Nuxt 4.0 · Nuxt Blog](https://nuxt.com/blog/v4)

Nuxt 4.0 正式发布，专注于提升开发者体验，带来更清晰的项目结构、更智能的数据获取和更完善的类型安全支持。

- 🎉 **Nuxt 4.0 发布**：经过一年的实际测试，Nuxt 4.0 正式推出，注重稳定性并引入了一些改进性的破坏性变更。  
- 🏗️ **更清晰的项目结构**：默认使用 `app/` 目录组织代码，提升文件监视速度和 IDE 上下文感知。  
- 🔄 **智能数据获取优化**：改进 `useAsyncData` 和 `useFetch`，支持自动数据共享、清理和响应式键。  
- 🔧 **更好的 TypeScript 支持**：为不同代码上下文（应用、服务器、共享文件夹等）创建独立的 TypeScript 项目，提升类型推断和自动补全。  
- ⚡ **更快的 CLI 和开发体验**：优化冷启动速度、引入 Node.js 编译缓存、原生文件监视和基于 Socket 的通信。  
- 🚀 **平滑升级路径**：大多数项目可无缝升级，提供兼容性标志和迁移工具（如 Codemod）辅助过渡。  
- 📂 **可选迁移**：现有项目结构仍受支持，无需强制更改。  
- 🛠️ **TypeScript 配置简化**：仅需一个根目录下的 `tsconfig.json` 文件。  
- ❤️ **致谢与未来计划**：感谢社区贡献，Nuxt 3 将持续维护至 2026 年 1 月，Nuxt 5 将带来 Nitro v3 和更多性能优化。  
- 📑 **详细升级指南**：建议阅读完整升级文档以了解潜在影响。  

Happy coding with Nuxt 4! 🚀

---

### [fx – 终端 JSON 查看与处理工具](https://fx.wtf/)

**原文标题**: [fx – a terminal JSON viewer & processor](https://fx.wtf/)

终端交互式 JSON 查看器，支持在命令行界面直观浏览和探索 JSON 数据。

- 🖥️ 在终端中交互式查看 JSON 数据  
- 🔍 支持直观浏览和探索 JSON 结构  
- 🛠️ 提供便捷的交互操作功能  
- 📂 适用于命令行环境下的 JSON 数据处理

---

### [发布 37.0.0 · antonmedv/fx · GitHub](https://github.com/antonmedv/fx/releases/tag/37.0.0)

**原文标题**: [Release 37.0.0 · antonmedv/fx · GitHub](https://github.com/antonmedv/fx/releases/tag/37.0.0)

Fx 终端 JSON 查看器及处理器发布 37.0.0 版本，包含多项新功能和改进。

- 🆕 **新功能**  
  - 🔢 支持 Vim 风格的跳转行号功能（如 `:42`）  
  - 🧮 增强 JSON 解析能力，支持特殊值（`Infinity`、`-Infinity`、`NaN`）  
  - 🚫 新增 `--strict` 标志以强制严格标准 JSON 解析  

- 🛠 **修复与改进**  
  - 修正对象节点预览问题  
  - 提供更精确的错误提示信息  

- 🔄 **数据工具**  
  - 新增递归数据转换函数 `walk`  
  - `map` 函数现支持对象映射  

- 📢 **社区反馈**  
  - 获得 11 位用户的积极反应（👍🎉❤️🚀）  

- 🔖 **版本信息**  
  - 由开发者 antonmedv 于 6 月 23 日发布，包含 17 次提交

---

