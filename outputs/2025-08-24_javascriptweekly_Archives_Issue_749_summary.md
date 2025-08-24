### [JavaScript 周刊第 749 期：2025 年 8 月 22 日](https://javascriptweekly.com/issues/749)

**原文标题**: [JavaScript Weekly Issue 749: August 22, 2025](https://javascriptweekly.com/issues/749)

JavaScript 周刊第 749 期回归，涵盖编译器进展、工具更新和社区动态，聚焦前端开发与性能优化。

- 🚀 Porffor 编译器实现亚毫秒级启动，提升 AWS Lambda 性能
- 🔍 Rspack 推出 Rslint，Go 语言编写的高性能 JS/TS 代码检查工具
- 📚 前端系统设计课程新增浏览器渲染和 UI 优化实践内容
- ⚡ jQuery 4.0 发布候选版本，兼容现代 Web 标准
- 💬 React 社区讨论服务器组件与开源商业化平衡
- 🌐 Intl API 成为浏览器原生国际化方案替代第三方库
- 📦 Uppy 5.0 文件上传器支持多云服务与框架集成
- 🎯 Chrome 团队揭秘内置 AI Web API 设计理念
- 🛠️ Bun 运行时降低 CPU 占用，Next.js 强化 Turbopack 构建
- 🔥 多款工具更新：ESLintv9.3、Astro5.1、Biome2.2 等

---

### [消除 AWS Lambda 中的 JavaScript 冷启动](https://goose.icu/lambda/)

**原文标题**: [Eliminating JavaScript cold starts on AWS Lambda](https://goose.icu/lambda/)

Porffor 是一种可将 JavaScript 提前编译为 WebAssembly 和原生二进制文件的引擎，现已在 AWS Lambda 上运行，显著降低冷启动时间和成本。

- 🚀 Porffor 将 JS 编译为原生二进制文件（<1MB），执行速度比 Node 快约 12 倍，比 LLRT 快近 4 倍
- 💰 在 Lambda 上成本比 Node 低 2 倍以上，比 LLRT 低近 4 倍，且 P99 延迟低于对手的 P50
- ⚠️ 目前仍处于早期阶段，仅支持约 60% JS 特性，缺乏完整 I/O 和 Node 兼容性
- 📊 测试使用 128MB 内存配置，冷启动性能远超 Node.js 22.x 和亚马逊实验性运行时 LLRT
- 🔜 作者邀请拥有简单 Lambda 场景的企业联系试用，但强调尚未达到生产就绪状态

---

### [紫红](https://porffor.dev/)

**原文标题**: [Porffor](https://porffor.dev/)

Porffor 是一个提前编译 JavaScript 的工具，能够将 JS 编译为 WebAssembly 和本地二进制文件，显著提升性能和安全性，同时大幅减小输出体积。

- 🚀 编译性能卓越：WebAssembly 输出体积和速度比现有方案提升 10-30 倍，本地二进制体积缩小 1000 倍（从 90MB 降至<100KB）
- 🔒 增强安全与隔离：支持 Wasm 沙箱执行，实现安全的服务端 JS 托管和抗逆向工程保护
- 🎯 多场景适用：支持嵌入式设备、游戏主机和 CLI 工具开发，编译后可直接生成轻量级可执行文件
- ⚙️ 技术优势：完全采用 JS 编写避免内存安全漏洞，原生支持 TypeScript 无需转译，专为 AOT 优化设计
- ⏱️ 运行模式革新：通过静态分析和提前编译优化执行效率，摆脱传统解释器或 JIT 的多层性能平衡限制
- 📊 开发进展：目前处于预发布阶段，2025 年可用，每提交均通过 Test262 合规测试，提供在线体验和本地安装方式

---

### [Rspack 推出 Rslint：一款采用 TypeScript 优先策略的代码检查工具...](https://socket.dev/blog/rspack-introduces-rslint-a-typescript-first-linter-written-in-go)

**原文标题**: [Rspack Introduces Rslint, a TypeScript-First Linter Written ...](https://socket.dev/blog/rspack-introduces-rslint-a-typescript-first-linter-written-in-go)

关于近期恶意 Ruby 软件包活动的后续说明与澄清，主要涉及对 60 个恶意 gem 的分析调查。

- 🚨 发现 60 个恶意 Ruby 软件包（gem），存在安全风险
- 🔍 研究团队进行了深入调查与验证工作
- 📝 原作者 Sarah Gooding 发布澄清说明
- ⚠️ 提醒开发者注意依赖包安全性
- 📅 事件最新进展发布于 2025 年 8 月 22 日

---

### [Rspack](https://rspack.rs/)

**原文标题**: [Rspack](https://rspack.rs/)

Rspack 是一个基于 Rust 开发的高性能 Web 打包工具，旨在无缝替代 webpack 并提供卓越的开发体验。

- 🚀 采用并行化 Rust 架构，实现极速启动和热更新
- 🔧 完全兼容 webpack 插件和加载器生态系统
- ⚡ 集成 SWC 和 Lightning CSS，提供超快的 JavaScript/TypeScript 转译和 CSS 处理
- 📦 支持代码分割、Tree Shaking、模块联邦等完整功能
- 🛠️ 提供 Rstack 工具链生态，包括 Rsbuild、Rspress 等配套工具
- 🌐 框架无关，适用于任何前端 UI 框架
- ⏱️ 在构建速度上显著优于 webpack 和 Vite 等工具

---

### [Oxlint 类型感知预览 | JavaScript 氧化编译器](https://oxc.rs/blog/2025-08-17-oxlint-type-aware.html)

**原文标题**: [Oxlint Type-Aware Preview | The JavaScript Oxidation Compiler](https://oxc.rs/blog/2025-08-17-oxlint-type-aware.html)

oxc 团队宣布在 oxlint 中推出类型感知的 linting 预览版，通过与 Go 语言编写的 tsgolint 集成，实现了比 typescript-eslint 快 10 倍的性能表现，同时支持包括 no-floating-promises 在内的 40 余种类型相关规则。

- 🚀 性能提升：采用基于 Go 的 typescript-go 编译器，使大型代码库的 linting 时间从 1 分钟缩短至 10 秒内
- 🔧 快速上手：安装 oxlint-tsgolint 后使用--type-aware 标志即可启用类型感知功能
- 📋 规则丰富：提供 42 种类型相关规则，包括异步处理、类型安全等检测功能
- 🏗️ 架构创新：oxlint(Rust) 作为前端处理 CLI，tsgolint(Go) 作为后端进行类型分析
- ⚠️ 当前限制：大型单体仓库可能存在性能问题，需要匹配 TypeScript 版本
- 🤝 社区协作：感谢 TypeScript 团队、typescript-eslint 团队及贡献者@auvred 和@camc314
- 📅 发展路线：v1.0 版本将解决性能问题、完善规则配置和 IDE 支持

---

### [生物群落，Web 工具链](https://biomejs.dev/)

**原文标题**: [Biome, toolchain of the web](https://biomejs.dev/)

Biome v2—Biotype 现已发布，这是一个专为 Web 项目设计的全功能工具链，集成了代码格式化、lint 检查等功能，旨在提升开发效率和代码质量。

- 🚀 **快速格式化**：支持 JavaScript、TypeScript、JSX 等多种语言，兼容 Prettier 97%，格式化速度比 Prettier 快约 35 倍。
- 🔍 **智能 lint 检查**：提供 349 条规则，包括 ESLint 和 TypeScript ESLint 等来源，能检测并修复代码问题，如优化`.map().flat()`为`.flatMap()`。
- ⚡ **高效性能**：基于 Rust 构建，架构先进，处理大型代码库时表现优异，节省 CI 和开发时间。
- 🛠️ **一体化工具链**：通过单一命令`check`同时执行格式化和 lint，无缝集成，简化工作流程。
- 📋 **开箱即用**：零配置启动，支持 TypeScript 和 JSX，提供详细错误诊断和商用企业支持。
- 🌐 **社区支持**：拥有活跃的开源社区，提供 Discord、GitHub 等多渠道交流和赞助机会。

---

### [jQuery 4.0.0 候选版本 1 | 官方 jQuery 博客](https://blog.jquery.com/2025/08/11/jquery-4-0-0-release-candidate-1/)

**原文标题**: [jQuery 4.0.0 Release Candidate 1 | Official jQuery Blog](https://blog.jquery.com/2025/08/11/jquery-4-0-0-release-candidate-1/)

jQuery 4.0.0 首个候选版本已发布，标志着即将迎来重大版本更新。该版本移除了对旧版 IE 的支持及已弃用的 API，并提供了精简构建版本。团队鼓励开发者测试并反馈问题，若未发现重大问题将发布正式版。

- 🚀 jQuery 4.0.0-rc.1 发布，接近最终版本
- 🔧 移除旧版 IE 支持及已弃用 API，精简代码
- 📦 提供标准版和精简版（体积减少约 8KB）
- 🌐 可通过 jQuery CDN 和 npm 安装
- ⚠️ 附升级指南和迁移工具（可能调整）
- 🐛 呼吁开发者测试并反馈问题
- 🙏 感谢贡献者提交补丁和测试

---

### [React 社区反思 | 李·罗宾逊](https://leerob.com/reflections)

**原文标题**: [Reflections on the React community | Lee Robinson](https://leerob.com/reflections)

作者回顾了十年 React 社区的发展历程，从个人成长到社区管理的挑战，再到商业与开源项目的复杂关系，最后探讨了 React Server Components 的演进与社区反馈的辩证关系。

- 🎯 React 已成为稳定且广泛采用的"无聊技术"，其组合架构和向后兼容性持续推动生态繁荣
- 😓 社区管理消耗巨大精力，React 团队面临反馈过载与负面情绪的压力
- 💡 Meta 作为非商业开源方，缺乏持续投入社区互动的经济动力
- 🏢 商业开源项目（如 Next.js/Remix）因商业模式差异与社区形成不同互动方式
- 🔄 React Server Components 通过 Vercel 与 Next.js 实现跨公司协作开发，但初期沟通不足引发争议
- 🌱 RSC 生态建设缓慢，近年才通过 Vite 等工具实现框架无关方案
- 🤝 呼吁社区保持善意：开源是礼物而非义务，开发者应以乐观态度参与建设

---

### [GitHub - privatenumber/minification-benchmarks: 🏃‍♂️🏃‍♀️🏃 JS 压缩性能基准测试：babel-minify、esbuild、terser、uglify-js、swc、Google Closure Compiler、tdewolff/minify、oxc-minify](https://github.com/privatenumber/minification-benchmarks)

**原文标题**: [GitHub - privatenumber/minification-benchmarks: 🏃‍♂️🏃‍♀️🏃 JS minification benchmarks: babel-minify, esbuild, terser, uglify-js, swc, google closure compiler, tdewolff/minify, oxc-minify](https://github.com/privatenumber/minification-benchmarks)

该项目对多个 JavaScript 压缩工具进行了全面的性能基准测试，旨在帮助开发者根据压缩率和速度选择最适合的工具。

- 🏆 综合表现最佳：@swc/core 在压缩率和速度之间取得了最佳平衡，特别在处理大型文件时表现突出
- ⚡ 极致速度：@tdewolff/minify 在几乎所有测试中都展现出最快的压缩速度
- 📦 优秀压缩率：uglify-js 在多个中型库测试中获得了最小的 gzip 压缩大小
- 🚀 新兴竞争者：oxc-minify 表现稳定，在大型文件处理上接近最佳压缩率且速度较快
- ❌ 淘汰工具：babel-minify、tedivm/jshrink 和 bun 因压缩失败或验证错误被淘汰
- ⚖️ 权衡选择：@cminify/cminify-linux-x64 速度极快但压缩率较低，适合对速度要求极高的场景
- 📊 测试方法：采用 10 秒超时、前后验证、最小配置的公平测试环境
- 🔢 评分机制：结合压缩大小 (85%) 和速度 (15%) 的加权评分系统，极端情况下调整为 50/50 权重

---

### [Jumping-Beaver/cminify：用C语言编写的CSS、JavaScript、XML、HTML、JSON命令行压缩工具。提供小于50 kB 的二进制版本。- Codeberg.org](https://codeberg.org/Jumping-Beaver/cminify)

**原文标题**: [Jumping-Beaver/cminify: Command-line minifier written in C for CSS, JavaScript, XML, HTML, JSON. Binary releases with less than 50 kB size are available. - Codeberg.org](https://codeberg.org/Jumping-Beaver/cminify)

文章概述了人工智能在医疗领域的应用现状与未来潜力，重点分析了其对诊疗效率、精准医疗和可及性的提升作用，同时指出数据隐私与伦理规范等挑战需协同解决。

- 🤖 人工智能辅助医学影像分析，显著提升疾病检测准确率
- 🧬 基于大数据的个性化治疗方案推荐，推动精准医疗发展
- 🌐 远程诊疗系统结合 AI 技术，改善医疗资源分布不均问题
- ⚠️ 患者数据隐私保护与算法透明度成为行业关注焦点
- 🔮 预测性健康管理通过 AI 实现早期疾病风险干预

---

### [比赛已经开始！| 博客 | js13kGames 2025](https://js13kgames.com/2025/blog/competition-has-started)

**原文标题**: [The competition has started! | Blog | js13kGames 2025](https://js13kgames.com/2025/blog/competition-has-started)

无法总结：未找到主要内容。

---

### [Vue 的未来在于你（与您）——Stack Overflow](https://stackoverflow.blog/2025/08/15/the-future-of-vue-is-you-and-you/)

**原文标题**: [The future of Vue is you (and You) - Stack Overflow](https://stackoverflow.blog/2025/08/15/the-future-of-vue-is-you-and-you/)

Vue.js 创始人 Evan You 回顾框架十年发展历程，探讨开源可持续性与 AI 集成未来方向
- 🎉 Vue.js 诞生十周年，创始人 Evan You 分享开发历程与挑战
- 🚀 探讨 AI 技术与 Vue.js 的未来集成可能性
- 🌱 关注开源项目的可持续发展模式
- 🏆 2025 年开发者调查中 Vue.js 位列第八大流行框架
- 💡 开发者 Hari 因「追踪鼠标位置」问题获得 Stellar Question 徽章
- ⚙️ Void Zero 团队正开发新一代 Vue.js 工具链

---

### [新系列博客文章：学习网页开发](https://2ality.com/2025/08/learning-web-dev-toc.html)

**原文标题**: [New series of blog posts: learning web development](https://2ality.com/2025/08/learning-web-dev-toc.html)

该博客文章介绍了一个名为“学习 Web 开发”的新系列博文，概述了 Web 开发所需的技术基础、系列内容结构以及学习资源。
- 🌐 Web 开发需要掌握 HTML（内容）、CSS（样式）、JavaScript（交互性）和服务器技术
- 📚 本系列要求具备 HTML 和 CSS 基础认知，通过实际构建小型应用进行实践教学
- 🚀 内容涵盖 JavaScript 基础语法、部署网站和创建服务器等核心技能
- 📖 提供 GitHub 代码库和《Exploring JavaScript》免费电子书作为延伸学习资源
- 💡 强调编程术语学习的重要性，并说明编程与学校数学的实际差异

---

### [学习网页开发：JavaScript 中的数字、变量与函数](https://2ality.com/2025/08/javascript-numbers-variables-functions.html)

**原文标题**: [Learning web development: Numbers, variables, functions in JavaScript](https://2ality.com/2025/08/javascript-numbers-variables-functions.html)

本文介绍了 JavaScript 编程入门知识，重点讲解了数字、变量和函数的基本概念和使用方法，适合编程新手学习。

- 🖥️ 浏览器控制台是运行 JavaScript 代码的工具，可通过不同方式打开
- 🔢 JavaScript 可以像计算器一样处理数字运算，支持加减乘除等操作
- 📝 变量使用 let 声明，可存储和修改值；常量使用 const 声明，值不可变
- ⚠️ 变量命名有特定规则，需遵循驼峰命名法
- 🔧 函数是可重复使用的代码块，可以接收参数并返回结果
- 🌡️ 示例展示了将摄氏温度转换为华氏温度的函数实现
- 📚 文章提供了练习任务，包括数值计算和函数编写

---

### [学习网页开发：JavaScript 中的字符串与方法](https://2ality.com/2025/08/javascript-strings-methods.html)

**原文标题**: [Learning web development: Strings and methods in JavaScript](https://2ality.com/2025/08/javascript-strings-methods.html)

本文介绍了 JavaScript 中字符串的基础知识及其方法，包括字符串长度、拼接、函数返回字符串、对象与属性、方法的概念，并通过多个项目示例展示了如何在实际网页应用中操作字符串、处理用户交互（如点击事件和温度转换），以及数字与字符串之间的转换。  
- 📝 字符串是 JavaScript 中用于表示文本的数据类型，可使用单引号或双引号定义，包括空字符串。  
- 📏 字符串具有长度属性（.length），可用于获取字符数量。  
- 🔗 字符串可通过加号运算符（+）进行拼接，支持变量和文本的组合。  
- 🔄 函数可以返回字符串，例如通过拼接生成问候语。  
- 🧩 JavaScript 支持嵌套变量（对象和属性），如 Math.PI，属性可包含函数（方法）。  
- 🖱️ 项目示例包括控制台日志（log-hello.html）、点击计数器（log-clicks.html 和 display-clicks.html），后者将点击次数显示在网页而非控制台。  
- 🌡️ 温度转换项目（temperature-converter.html）演示了从输入框读取字符串、转换为数字、计算后再转换回字符串并显示的过程。  
- 🔢 强调了数字（123）与字符串（'123'）的区别，以及使用 String() 和 Number() 进行类型转换的方法。  
- 💡 最后提供了一个练习：修改温度转换项目以实现货币转换（如 USD 与 EUR）。

---

### [学习网页开发：JavaScript 中的数组](https://2ality.com/2025/08/javascript-arrays.html)

**原文标题**: [Learning web development: Arrays in JavaScript](https://2ality.com/2025/08/javascript-arrays.html)

本文介绍了 JavaScript 数组的基础知识，包括创建、访问和修改数组元素，以及数组的可变性。通过一个魔法 8 球项目示例，展示了如何利用数组和随机数生成函数实现交互功能。

- 📚 数组是一种数据结构，用于在变量中存储多个值，使用方括号语法创建
- 🔄 即使使用 const 声明，数组本身也是可变的，因为 const 只防止变量重新赋值，不阻止修改可变值
- 💡 介绍了单行注释 (//) 和多行注释 (/* */) 的用法和格式
- 🎱 通过魔法 8 球项目演示了数组的实际应用：使用数组存储答案，随机选择并显示
- 🎲 getRandomInteger() 函数利用 Math.random() 和 Math.floor() 生成指定范围内的随机整数
- 💻 项目代码展示了事件监听、DOM 操作和数组读取等 Web 开发基础技能

---

### [React Native 0.81 - 支持 Android 16、iOS 构建加速等新特性 · React Native](https://reactnative.dev/blog/2025/08/12/react-native-0.81)

**原文标题**: [React Native 0.81 - Android 16 support, faster iOS builds, and more · React Native](https://reactnative.dev/blog/2025/08/12/react-native-0.81)

React Native 0.81 版本发布，主要包含 Android 16 支持、iOS 构建速度提升及其他多项改进和破坏性变更。

- 📱 默认支持 Android 16（API 级别 36），要求应用全屏显示并弃用 SafeAreaView 组件
- ⚡ 实验性预编译 iOS 构建功能，可将编译时间缩短高达 10 倍
- 🔄 JavaScriptCore 引擎支持转为社区维护包，内置版本已移除
- ⚠️ 多项破坏性变更：Node.js 最低版本要求 20.19.4，Xcode 最低要求 16.1
- 🐛 改进了未捕获 JavaScript 错误的报告机制，包含原始消息和堆栈跟踪
- 📦 引入 RN_SERIALIZABLE_STATE 宏支持新架构组件的可序列化状态
- 👥 包含来自 110 位贡献者的 1110 多次提交，特别感谢社区成员的重大贡献

---

### [Next.js 15.5 | Next.js](https://nextjs.org/blog/next-15-5)

**原文标题**: [Next.js 15.5 | Next.js](https://nextjs.org/blog/next-15-5)

Next.js 15.5 版本发布，包含 Turbopack 构建功能（测试版）、稳定的 Node.js 中间件支持、TypeScript 改进、next lint 弃用以及 Next.js 16 的弃用警告。  
- 🚀 Turbopack 构建进入测试版，生产环境构建速度提升显著，支持多核优化  
- ⚙️ Node.js 中间件运行时正式稳定，支持完整 Node.js API 和复杂用例  
- 📘 TypeScript 路由类型改进，提供编译时类型安全和自动生成类型  
- 🗑️ next lint 命令被弃用，推荐使用显式 ESLint 或 Biome 配置  
- ⚠️ 引入 Next.js 16 弃用警告，包括 legacyBehavior、AMP 支持及 next/image 配置变更  
- 🔧 提供自动化升级工具和迁移指南，帮助开发者平滑过渡

---

### [Bun v1.2.20 | Bun 博客](https://bun.com/blog/bun-v1.2.20)

**原文标题**: [Bun v1.2.20 | Bun Blog](https://bun.com/blog/bun-v1.2.20)

本次更新修复了 141 个问题，包含运行环境、打包工具和开发服务器的多项可靠性改进，重点优化了 CPU 占用、测试工具和 Windows 兼容性。

- 🚀 修复 141 个问题并优化运行时性能
- ⚡ 空闲 CPU 占用降低，垃圾回收调度优化
- 🔄 自动迁移 yarn.lock 至 bun.lock 文件
- 🧪 新增 bun:test 三个 mock 返回值匹配器（toHaveReturnedWith 系列）
- 📝 引入 expectTypeOf 类型测试工具（运行时无操作）
- 🧹 新增 mock.clearAllMocks() 全局 mock 清理功能
- 📦 bun outdated/update支持--recursive递归处理工作区
- 🌐 Bun.serve 静态路由新增 ETag/304 缓存支持
- 🪟 Windows 长路径支持（超过 260 字符）
- ⚡ WebAssembly 新增 compileStreaming/instantiateStreaming
- 🔧 多项 Node.js 兼容性修复（require.main、zlib 线程安全等）
- 🐛 修复 bun shell、打包器、安装器及开发服务器多项崩溃问题
- 📎 包含 19 位贡献者的代码提交

---

### [Astro 5.13 | Astro](https://astro.build/blog/astro-5130/)

**原文标题**: [Astro 5.13 | Astro](https://astro.build/blog/astro-5130/)

Astro 5.13 版本引入了多项实验性改进和新功能，包括环境变量处理优化、Chrome DevTools 工作区支持、多站点地图功能等，同时提供了升级指南和错误修复。

- 🧪 实验性静态 `import.meta.env`：改进环境变量处理，使其与 Vite 保持一致，并取消类型强制转换，未来将在 Astro 6.0 成为默认行为。
- 🛠️ 实验性 Chrome DevTools 工作区支持：自动配置项目文件夹为工作区源，允许在浏览器中直接编辑并保存代码更改。
- 🗺️ 多站点地图支持：通过 `@astrojs/sitemap` 集成新增 `customSitemaps` 配置选项，可包含外部生成的站点地图。
- ⚠️ 实验性托管错误页面：Node.js 适配器支持从指定主机加载预渲染的自定义错误页面，适用于反向代理或容器环境。
- 🗃️ Astro DB 表枚举支持：为文本列添加枚举功能，生成类型定义但不进行运行时验证。
- ☁️ Cloudflare KV 本地支持：Cloudflare 适配器在本地开发中支持 Cloudflare Workers KV，并可选择连接远程命名空间。
- 🔧 升级指南：推荐使用 `@astrojs/upgrade` CLI 工具或手动运行包管理器命令升级到最新版本。
- 🐛 错误修复：包含自 5.12 版本以来的多项问题修复，详情参见更新日志。
- 👥 社区贡献：感谢核心团队及众多社区贡献者的代码和文档改进。

---

### [ESLint v9.33.0 发布 - ESLint - 可插拔 JavaScript 代码检查工具](https://eslint.org/blog/2025/08/eslint-v9.33.0-released/)

**原文标题**: [ESLint v9.33.0 released - ESLint - Pluggable JavaScript Linter](https://eslint.org/blog/2025/08/eslint-v9.33.0-released/)

ESLint v9.33.0 作为次要版本发布，新增功能并修复了之前版本中的多个错误。

- 🆕 `one-var` 规则新增对显式资源管理语法的支持，包括 `using` 和 `await using` 声明
- 🔍 `no-restricted-globals` 规则增强全局对象访问检测功能，新增三个配置选项
- 🐛 修复自定义规则中 `meta.docs.recommended` 类型限制问题
- 📚 更新多个文档内容，包括 playground 按钮和规则文档完善
- 🔧 构建系统和测试相关优化，提升稳定性和类型检查

---

### [发布 v5.5.0 · fastify/fastify · GitHub](https://github.com/fastify/fastify/releases/tag/v5.5.0)

**原文标题**: [Release v5.5.0 · fastify/fastify · GitHub](https://github.com/fastify/fastify/releases/tag/v5.5.0)

Fastify 框架发布了 v5.5.0 版本，包含多项功能优化、错误修复和文档改进，移除了 simple-get 依赖并引入了新的贡献者。

- 🚀 版本 v5.5.0 发布，包含 3 个主要提交
- 🔧 移除所有测试中的 simple-get 依赖项
- 📝 修复文档中的 Markdown 格式和错误描述
- 🐛 修复管道测试关闭问题和 JSON 正文错误处理
- ✨ 新增 Schema 相关类型导出和状态码类型强化
- ⚡ 使用 AsyncResource.bind() 优化内容类型解析器
- 👋 新增 14 位首次贡献者参与开发
- 📦 更新开发依赖（TypeScript、ESLint 等）
- 🌐 生态文档新增 fastify-route-preset 等插件记录

---

### [pnpm 10.15 | pnpm](https://pnpm.io/blog/releases/10.15)

**原文标题**: [pnpm 10.15 | pnpm](https://pnpm.io/blog/releases/10.15)

pnpm 10.15 版本带来配置管理优化、依赖处理改进和多项问题修复  
- 🔧 新增 cleanupUnusedCatalogs 配置，自动清理未使用的目录条目  
- ⚙️ 自动加载符合@*/pnpm-plugin-*命名规范的配置依赖中的 pnpmfiles  
- 📝 config get 命令支持属性路径查询和 INI/JSON 格式输出  
- 🔄 config set 命令支持点语法和下标键名设置  
- 🤝 安装缺失对等依赖时优先选择根工作区现有版本  
- ✅ pnpm create 命令增加节点版本强制验证  
- 🌐 修复 AWS CodeArtifact 的 406 错误请求头问题  
- 🐛 修复独立执行版 glibc 兼容性和 dlx 命令参数传递问题

---

### [发布 Biome CLI v2.2.0
 · biomejs/biome · GitHub](https://github.com/biomejs/biome/releases/tag/%40biomejs/biome%402.2.0)

**原文标题**: [Release Biome CLI v2.2.0
 · biomejs/biome · GitHub](https://github.com/biomejs/biome/releases/tag/%40biomejs/biome%402.2.0)

Biome CLI v2.2.0 版本发布，包含多项新功能、规则增强、性能优化和错误修复。

- 🚀 新增 `noRestrictedImports` 规则的 `patterns` 选项，支持使用 gitignore 样式模式限制导入
- ⚙️ 允许自定义排序操作的顺序，如 `assist/source/useSortedKeys` 等
- 📁 新增 `useBiomeIgnoreFolder` 规则，检测并推广正确的忽略文件夹模式
- 🔧 修复 `files.includes` 处理中的不一致性，改进文件夹忽略逻辑
- 📄 新增对 `.graphqls` 文件的支持，可格式化和检查 GraphQL 文件
- 🔄 新增 `javascript.formatter.operatorLinebreak` 选项，配置长行在二元运算符前或后换行
- 📈 将多个规则从 nursery 升级到稳定组，并重命名部分规则以提高一致性
- ⚠️ 新增 `noBiomeFirstException` 规则，防止 `files.includes` 中错误使用模式
- 🌐 新增 Qwik 域支持，为 Qwik 开发者提供格式化和检查功能
- 🔍 改进项目规则扫描器，提升性能并更好地处理依赖和忽略文件
- 📊 增强 `--reporter=summary`，显示包含违规的文件列表并可点击打开
- 🛠️ 在 `@biomejs/wasm-*` 包中新增多个函数，如 `fileExists` 和 `isPathIgnored`
- ⚛️ 在 `useExhaustiveDependencies` 中支持跟踪 React 钩子返回对象的稳定结果
- 🔧 修复 `useConst` 规则，避免误报未初始化变量在写入前被读取的情况
- 🎨 新增 `useMaxParams` 规则，强制函数参数的最大数量以提高代码可读性
- ⚡ 新增 `noNextAsyncClientComponent` 规则，防止在 Next.js 客户端组件中使用异步函数
- 📦 在 `noUndeclaredDependencies` 规则中将仅类型导入视为开发依赖

---

### [使用自定义高亮 API – Frontend Masters 博客](https://frontendmasters.com/blog/using-the-custom-highlight-api/)

**原文标题**: [Using the Custom Highlight API – Frontend Masters Blog](https://frontendmasters.com/blog/using-the-custom-highlight-api/)

Custom Highlight API 允许通过 JavaScript 的 Range() 对象对文本进行高亮样式处理，无需操作 DOM 结构，适用于搜索高亮和语法高亮等场景。

- 🚀 Firefox 140 于 2025 年 6 月支持该 API，实现所有主流浏览器兼容
- 🔍 通过 Range() 设置文本起止位置，CSS.highlights.set() 注册高亮名称，CSS 中 ::highlight() 应用样式
- ⚡ 优势：避免 DOM 操作性能损耗，减少页面重绘，适合高频文本处理场景
- 🔎 支持多范围高亮，可构建自定义搜索功能（如实时关键词匹配）
- 💻 语法高亮应用：Web Component 替代传统 <span> 方案，但存在客户端渲染延迟
- ⚠️ 局限性：仅限客户端处理，服务端渲染语法高亮仍更具优势

---

### [CSS 自定义高亮 API](https://developer.mozilla.org/en-US/docs/Web/API/CSS_Custom_Highlight_API)

**原文标题**: [CSS Custom Highlight API](https://developer.mozilla.org/en-US/docs/Web/API/CSS_Custom_Highlight_API)

CSS Custom Highlight API 允许通过 JavaScript 创建文本范围并用 CSS 样式化，无需影响 DOM 结构，适用于文本编辑器高亮语法错误或协作编辑场景。

- 🛠️ 通过创建 Range 对象定义需要样式化的文本范围
- 🎨 使用 Highlight 对象管理多个文本范围，支持不同样式配置
- 📋 通过 HighlightRegistry（CSS.highlights）注册高亮对象并自定义标识符
- ✨ 使用::highlight() 伪元素为注册的高亮对象应用 CSS 样式
- 🔍 提供搜索高亮实战示例：监听输入事件、匹配文本、动态创建范围并样式化
- 📱 包含浏览器兼容性说明和相关技术参考链接

---

### [Intl API 的力量：浏览器原生国际化权威指南 — Smashing Magazine](https://www.smashingmagazine.com/2025/08/power-intl-api-guide-browser-native-internationalization/)

**原文标题**: [The Power Of The Intl API: A Definitive Guide To Browser-Native Internationalization — Smashing Magazine](https://www.smashingmagazine.com/2025/08/power-intl-api-guide-browser-native-internationalization/)

Intl API 是浏览器原生国际化解决方案，提供标准化的本地化数据处理能力，可替代第三方库高效处理日期、数字、列表等内容的本地化格式化。

- 🌍 Intl API 是 JavaScript 原生国际化接口，支持根据地区设置格式化日期、数字、列表等内容
- 📅 Intl.DateTimeFormat 可本地化日期时间格式，自动适配不同地区的日期表示习惯
- 💰 Intl.NumberFormat 支持货币、单位等数字格式化，自动处理千位分隔符和小数点符号
- 📝 Intl.ListFormat 智能格式化列表连接词，支持"和"/"或"等不同语言的自然连接方式
- ⏰ Intl.RelativeTimeFormat 生成本地化的相对时间描述（如"昨天"、"3 个月前"）
- 🔢 Intl.PluralRules 处理复数规则，支持阿拉伯语等多复数形式的语言
- 🌐 Intl.DisplayNames 提供语言、地区、文字系统名称的本地化显示
- 🚀 所有现代浏览器均支持 Intl API，无需额外加载库即可使用
- 📦 使用原生 API 可减少依赖、降低打包体积并提升性能

---

### [Embrace 用户旅程平台功能详解](https://embrace.io/blog/user-journeys-walkthrough/?utm_source=newsletter&utm_medium=paid&utm_campaign=javascript-weekly-8-22-2025&utm_content=user-journeys)

**原文标题**: [A walk-through of Embrace's User Journeys platform capability](https://embrace.io/blog/user-journeys-walkthrough/?utm_source=newsletter&utm_medium=paid&utm_campaign=javascript-weekly-8-22-2025&utm_content=user-journeys)

概述：Embrace 推出用户旅程功能，将产品分析与可观测性结合，帮助工程师通过自定义流程分析技术性能对用户参与度的影响。

- 🗺️ 用户旅程平台功能连接产品分析与可观测性
- 🔧 工程师可构建自定义流程分析技术性能影响
- 📊 利用 Embrace 精细化工具分析用户参与度
- ⏱️ 技术性能数据与用户行为数据实现关联

---

### [设计内置 AI Web API | Domenic Denicola](https://domenic.me/builtin-ai-api-design/)

**原文标题**: [Designing the Built-in AI Web APIs | Domenic Denicola](https://domenic.me/builtin-ai-api-design/)

概述了 Chrome 内置 AI 团队设计 Web API 的过程，重点探讨了提示 API 的设计挑战、客户端与服务器 API 的差异，以及互操作性和未来兼容性考量。

- 🧠 基于角色消息格式设计提示 API，处理多模态输入/输出约束和语义规范化
- 🌐 采用状态化的 LanguageModelSession 设计优化客户端资源管理，支持预加载和分支对话
- 🔄 通过独立入口点和选项预设机制实现跨浏览器/模型的互操作性
- 📦 为翻译器等任务 API 设计语言包动态加载架构，隐藏底层实现细节
- ⚡ 面临实时性差距挑战，当前 API 功能落后前沿模型约一年
- 🛡️ 需平衡设备约束选择（本地/云端模型）与隐私保护需求
- ⚠️ 存在提示注入攻击等实施质量问题和超参数标准化争议

---

### [内置 AI API  |  Chrome AI 功能  |  Chrome 开发者指南](https://developer.chrome.com/docs/ai/built-in-apis)

**原文标题**: [Built-in AI APIs  |  AI on Chrome  |  Chrome for Developers](https://developer.chrome.com/docs/ai/built-in-apis)

Chrome 浏览器内置 AI API 的开发状态与功能概述，涵盖翻译、语言检测、文本摘要等多项人工智能服务，部分功能已稳定上线，部分处于试验阶段。

- 🌐 翻译 API（Chrome 138 稳定版）：支持动态内容实时翻译，适用于多语言社交平台和客服场景
- 🔤 语言检测 API（Chrome 138 稳定版）：自动识别文本语言，为翻译流程提供关键支持
- 📝 摘要生成 API（早期预览计划）：用本地 AI 压缩长文本，适用于会议记录、产品评论总结等场景
- ✍️ 写作与重写 API（原始试验阶段）：辅助内容创作与文本风格调整，支持邮件改写等应用
- 💬 提示词 API（扩展程序专用）：允许通过自然语言与 Gemini Nano 模型交互
- ✅ 校对 API（Chrome 139 测试版）：提供交互式文本校对功能，适用于文档编辑和聊天场景
- 🚧 开发阶段差异：部分 API 已稳定，部分仅限早期预览计划或原始试验阶段使用
- 📋 参与方式：开发者可通过加入早期预览计划体验实验性 API 并提供反馈

---

### [React 模拟面试：Kent C. Dodds、Jack Herrington 与 Roadside Coder 解决 React 编程题 - YouTube](https://www.youtube.com/watch?v=5KkaaYl5rwA)

**原文标题**: [React Mock Interview: Kent C. Dodds, Jack Herrington & Roadside Coder Solve React Coding Question - YouTube](https://www.youtube.com/watch?v=5KkaaYl5rwA)

这是 YouTube 网站页脚常见链接列表的概述，涵盖了从公司信息到用户政策等多个方面。

- ℹ️ 关于平台和公司信息
- 📰 新闻与媒体相关资源
- ©️ 版权声明与保护
- 📞 联系与支持渠道
- 🎬 内容创作者相关信息
- 📢 广告与商业合作
- 💻 开发者资源与 API
- 📑 服务条款与协议
- 🔒 隐私政策与数据保护
- ⚖️ 平台政策与安全指南
- 🔧 平台功能运作说明
- 🧪 新功能测试与体验
- ®️ 版权归属与法律声明

---

### [Shopify Webhook 解析错误导致数据库完全删除](https://www.ingressr.com/blog/webhook-security-incident-analysis/)

**原文标题**: [How Incorrect Shopify Webhook Parsing Led to Complete Database Deletion](https://www.ingressr.com/blog/webhook-security-incident-analysis/)

一起 Shopify webhook 解析错误导致数据库被清空的安全事件，揭示了输入验证和 ORM 行为理解的重要性。

- 🛑 漏洞源于 SHOP_REDACT webhook 处理程序中的错误解构：`const {shopId} = payload.shop_id`（实际应为直接取值）
- 🔍 JavaScript 静默失败：对原始值解构不会报错，而是返回 undefined
- 💥 ORM 危险操作：undefined 值触发 Prisma 的 deleteMany()，清空 events 和 visitors 全部数据
- 🚨 异常发现：仅因 shops 表删除操作需要唯一约束而抛出错误，暴露了前两个表的静默删除
- ✅ 数据恢复：得益于完善的备份系统，所有数据在几小时内成功恢复
- 🔧 修复措施：包含正确解析、输入验证、身份验证和 HMAC 加密验证
- 📝 行业启示：需关注 ORM 安全模式、webhook 身份验证和 JavaScript 的隐式陷阱
- 🛡️ 预防策略：加强代码审查、畸形负载测试和操作监控警报

---

### [模态框的问题及其解决方案 | 诺埃尔·德·马丁](https://noeldemartin.com/blog/the-problems-with-modals-and-how-to-solve-them)

**原文标题**: [The Problems With Modals, and How to Solve Them | Noel De Martin](https://noeldemartin.com/blog/the-problems-with-modals-and-how-to-solve-them)

本文讨论了传统模态框实现方式的问题，并提出了一种基于函数调用的改进方案，支持异步响应和 TypeScript 类型安全。

- 🚫 传统模态框需在模板中声明并依赖布尔值控制，限制了从 JS 文件调用的灵活性
- 💡 提出类似原生 alert() 的函数调用方式：const answer = await showModal(MyModal)
- 🎯 通过 ModalsPortal 组件集中渲染模态框，只需在应用中放置一次
- 🔧 支持传递参数和异步获取响应，使用 Promise 封装关闭事件
- 📦 可实现模态框的懒加载：const {default: MyModal} = await import('./MyModal.vue')
- 🧩 提供完整的 TypeScript 支持，可推断组件 props 和 emit 类型
- 🌐 方案不仅适用于模态框，也可扩展至提示框、Toast 等其他覆盖层组件
- ⚠️ 需注意可访问性（焦点控制、键盘交互等）建议使用现有组件库处理

---

### [500 倍速的 postMessage(字符串) | Bun 博客](https://bun.com/blog/how-we-made-postMessage-string-500x-faster)

**原文标题**: [500x faster postMessage(string) | Bun Blog](https://bun.com/blog/how-we-made-postMessage-string-500x-faster)

Bun v1.2.21 通过优化字符串在线程间的传输机制，实现了 postMessage 性能的显著提升，特别适用于多线程服务器和数据处理场景。

- 🚀 Bun v1.2.21 的 postMessage(string) 性能与字符串大小几乎无关，比旧版本快达 500 倍
- 💾 峰值内存使用量减少约 22 倍，通过避免安全字符串的序列化实现优化
- 📊 基准测试显示：传输 3MB 字符串仅需 593 纳秒，而旧版本需要 32 万纳秒
- 🧠 技术核心：利用 JavaScriptCore 字符串本身具备线程安全的引用计数特性
- ⚡ 优化自动触发条件：纯字符串传输、非子串/原子字符串、长度≥256 字符
- 🔧 底层实现：跳过结构化克隆序列化，直接共享字符串指针并预计算哈希值
- 🌟 特别适合：API 服务器、实时应用和大规模 JSON 数据传输场景
- 📈 未来可能扩展至对象和数组中的字符串值优化

---

### [JavaScript 的未来：我们期待什么](https://jsdev.space/future-of-javascript/)

**原文标题**: [The Future of JavaScript: What Awaits Us](https://jsdev.space/future-of-javascript/)

JavaScript 语言持续快速发展，TC39 委员会和 Deno 团队等贡献者推动着新特性的演进。最新进展包括多个提案进入不同阶段，从即将可用的 Stage 4 到早期提案 Stage 1，涵盖了资源管理、异步处理、错误检测和数据处理等方面。

- 🗑️ 显式资源管理（using 关键字）提供确定性资源清理，支持自动调用[Symbol.dispose]方法
- 🔄 Array.fromAsync 支持异步可迭代对象转换为数组，已获主流环境全面支持
- 🚨 Error.isError 提供跨 realm 的错误检测标准方法，解决继承检测难题
- 🔒 不可变 ArrayBuffer 提案引入 transferToImmutable 方法，确保二进制数据安全共享
- 🎲 Random.Seeded 提供确定性随机数生成，适用于模拟和测试场景
- 🔢 Number.prototype.clamp 方法简化数值范围限制，替代 Math.min/Math.max 组合
- 🧮 Intl.NumberFormat 新增 trailingZeroDisplay 选项，优化数字格式化显示
- 📊 Comparisons 提案标准化差异输出生成，助力测试框架开发
- 🎯 Random 命名空间提供便捷随机数生成工具，包括采样和洗牌功能

---

### [Uppy](https://uppy.io/)

**原文标题**: [Uppy](https://uppy.io/)

Uppy 是一个功能强大、响应式且可扩展的文件上传仪表板，支持从远程源添加文件、编辑图像、生成缩略图等多种操作。

- 🌐 支持从 Google Drive 等远程源获取文件，通过 Companion 服务处理认证和下载
- 🖼️ 内置图像编辑器和摄像头拍摄功能，可直接在仪表板中处理媒体文件
- ⚡ 采用 Tus 协议实现可恢复的大文件上传，避免网络中断导致上传失败
- 🔌 提供 React、Vue、Svelte 和 Angular 等主流框架的集成支持
- 🌍 具备多语言支持和无障碍访问设计，注重国际化用户体验
- 🛡️ 通过 Golden Retriever 插件实现浏览器崩溃后的文件恢复功能
- 🔓 完全开源且社区驱动，可根据用户反馈持续改进项目
- 🚀 可与 Transloadit 文件编码处理后端完美配合工作

---

### [GitHub - transloadit/uppy：下一代开源网页浏览器文件上传工具](https://github.com/transloadit/uppy)

**原文标题**: [GitHub - transloadit/uppy: The next open source file uploader for web browsers](https://github.com/transloadit/uppy)

Uppy 是一款开源的浏览器端文件上传工具，由 Transloadit 开发，具有模块化架构和丰富的功能集成。

- 🐶 开源且免费，采用 MIT 许可证，支持高度自定义和扩展
- ⚡ 轻量模块化设计，支持从本地、URL、Google Drive、Dropbox 等多种来源获取文件
- 📁 提供可恢复的文件上传（基于 tus 标准），支持大文件及不稳定网络环境
- 🖥️ 包含 Dashboard 等 UI 组件，支持 React、Vue、Svelte 等框架集成
- 🌍 支持多语言国际化，具备可访问性设计
- 🔧 可与 Transloadit 等后端服务配合使用，也支持自建服务器
- 📸 集成图片编辑、元数据预览、摄像头录制等实用功能
- 🛠️ 提供配套服务 Companion，支持 Instagram、Box 等云服务直接导入

---

### [Faceclick：带关键词搜索的轻量级表情选择器 - ratfactor](https://ratfactor.com/faceclick/index)

**原文标题**: [Faceclick: A lightweight Emoji picker with keyword search - ratfactor](https://ratfactor.com/faceclick/index)

Faceclick 是一款轻量级表情符号选择器，支持分组和关键词搜索，总文件大小仅 70KB（未压缩未精简），通过自定义数据压缩和优化技术实现高效存储。

- 🎯 核心目标：提供分组/关键词搜索表情符号功能，支持悬停显示标签，并追求极致文件体积最小化
- 📊 技术实现：采用空间分隔字符串存储数据，通过词频去重和索引替换（如$0代表"face"）压缩数据量，从原始 735KB 降至 63KB
- 🔧 自定义工具：提供 Ruby 脚本（customizer.rb）允许用户自定义表情数据集和压缩参数
- 🌐 使用方式：通过简单 JS 调用（FC.attach()）集成，支持完全自定义样式和交互逻辑
- ❌ 特性取舍：移除了模糊搜索功能，采用直接字符串匹配提升搜索效率
- 🚴 设计哲学：专为轻量级应用（如 40KB 的 Famsite 网站）设计，避免引入重型第三方库

---

### [注册 - Auth0](https://auth0.com/signup?utm_source=jsweekly&utm_campaign=global_mult_mult_all_ciam-dev_dg-plg_auth0_native_jsweekly_newsletter_aud_JavascriptWeekly-Q3-Newsletter_utm2&utm_medium=cpc&utm_id=aNKKZ00000003Bv4AI)

**原文标题**: [Sign Up - Auth0](https://auth0.com/signup?utm_source=jsweekly&utm_campaign=global_mult_mult_all_ciam-dev_dg-plg_auth0_native_jsweekly_newsletter_aud_JavascriptWeekly-Q3-Newsletter_utm2&utm_medium=cpc&utm_id=aNKKZ00000003Bv4AI)

这是一个用户注册页面，提供多种注册方式和全球国家选择选项。

- 🌐 支持全球多国用户注册，包含完整国家/地区下拉列表
- 📧 提供邮箱注册和第三方登录（GitHub/Google/Microsoft）选项
- 🔐 由 Auth0 提供认证服务，具备暴力破解保护和可疑 IP 限制功能
- 🆓 提供免费套餐，包含 2.5 万月活用户和无限制登录次数
- ⚙️ 支持无代码自定义注册登录流程和社交登录功能
- 📝 包含渐进式用户信息收集功能，提供 5 种操作和表单

---

### [Sidequest.js](https://sidequestjs.com/posts/intro-to-sidequest/)

**原文标题**: [Sidequest.js](https://sidequestjs.com/posts/intro-to-sidequest/)

Sidequest.js 是一个专为 Node.js 设计的分布式后台作业系统，通过数据库协调多节点任务，解决传统调度工具在分布式环境中的局限性。

- 🚀 解决传统调度器痛点：避免多实例重复执行任务，无需开发者手动实现分布式锁机制  
- 🛡️ 线程隔离保障稳定性：使用 Worker 线程执行重型任务，确保主应用线程不被阻塞  
- 🗄️ 无缝集成现有数据库：支持 PostgreSQL/MySQL/MongoDB，无需额外消息队列基础设施  
- ⚡ 开发者友好 API：通过继承 Job 类快速定义任务，自动处理分布式执行和指数退避重试  
- 🌐 规避云服务依赖：无供应商锁定风险，本地开发测试更简便，比 Airflow/RabbitMQ/SQS 更轻量

---

### [仪表板 | Sidequest.js](https://docs.sidequestjs.com/dashboard)

**原文标题**: [Dashboard | Sidequest.js](https://docs.sidequestjs.com/dashboard)

Sidequest Dashboard 是一个用于监控、管理和调试作业处理系统的综合网页界面，提供实时作业执行、队列性能和系统健康状态的洞察。

- 🖥️ 默认启用，运行在端口 8678 上，无需外部依赖
- ⚙️ 支持自定义配置，包括端口设置和基本身份验证
- 🔒 生产环境建议启用身份验证以确保安全
- 📊 提供实时监控、作业管理、队列控制和性能分析功能
- 📱 响应式设计，兼容桌面和移动设备
- 📋 包含作业统计概览、作业列表筛选、详细视图和队列管理
- 🛠️ 支持独立安装和运行仪表板，无需启动完整引擎
- 🔧 提供故障排除指南，解决访问、认证和性能问题

---

### [GitHub - sidequestjs/sidequest: Sidequest 是一个面向 Node.js 应用的现代化、可扩展的后台作业处理器。](https://github.com/sidequestjs/sidequest)

**原文标题**: [GitHub - sidequestjs/sidequest: Sidequest is a modern, scalable background job processor for Node.js applications.](https://github.com/sidequestjs/sidequest)

Sidequest 是一个专为 Node.js 应用设计的现代化、可扩展的后台任务处理器，采用 TypeScript 构建，支持多种数据库后端和实时监控功能。

- 🚀 高性能处理：通过工作线程实现非阻塞任务处理
- 🗄️ 多后端支持：原生支持 SQLite、PostgreSQL 和 MySQL 数据库
- 📝 全面 TypeScript 支持：默认支持 TypeScript 任务，要求 Node.js >= 24 版本
- 📊 可视化仪表板：提供美观的响应式 Web 界面用于监控任务和队列
- ⏰ 灵活调度：支持定时任务和可配置的重试机制（含指数退避）
- 🔒 任务去重：通过唯一性约束防止重复任务执行
- 🛠️ 完整工具链：包含 CLI 工具用于数据库迁移和管理
- 📦 模块化架构：采用 monorepo 结构，支持 ESM 和 CJS 模块规范
- 📄 开源许可：基于 LGPL-3.0 许可证，由 Lucas Merencia 和 Giovani Guizzo 开发维护

---

### [GitHub - yuniko-software/minecraft-mcp-server：基于Mineflayer API 的 Minecraft MCP 服务器。可实时控制游戏角色，使 AI 助手能通过自然语言指令建造结构、探索世界并与游戏环境交互。](https://github.com/yuniko-software/minecraft-mcp-server)

**原文标题**: [GitHub - yuniko-software/minecraft-mcp-server: A Minecraft MCP Server powered by Mineflayer API. It allows to control a Minecraft character in real-time, allowing AI assistants to build structures, explore the world, and interact with the game environment through natural language instruction](https://github.com/yuniko-software/minecraft-mcp-server)

这是一个基于 Mineflayer API 开发的 Minecraft MCP 服务器项目，允许通过自然语言指令实时控制游戏角色，支持 AI 助手进行建筑建造、世界探索和游戏交互。

- 🤖 使用 Mineflayer API 和模型上下文协议 (MCP) 实现 AI 控制 Minecraft 角色
- 🎮 当前仅兼容 Minecraft 1.21.6 及以下版本
- 💬 支持通过 Claude 等 MCP 客户端用自然语言下达指令
- 🏃 包含移动、飞行、物品管理、方块交互等丰富控制命令
- 🛠️ 采用 TypeScript 开发 (95.3%)，开源 Apache-2.0 协议
- 📊 项目获得 224 星标和 22 个分支，处于活跃开发状态
- 🔧 欢迎贡献代码、文档改进和功能建议

---

### [GitHub - PrismarineJS/mineflayer：使用强大、稳定且高级的JavaScript API 创建 Minecraft 机器人](https://github.com/PrismarineJS/mineflayer)

**原文标题**: [GitHub - PrismarineJS/mineflayer: Create Minecraft bots with a powerful, stable, and high level JavaScript API.](https://github.com/PrismarineJS/mineflayer)

Mineflayer 是一个用于创建 Minecraft 机器人的强大 JavaScript 库，提供稳定高级的 API 接口，支持多种版本和丰富功能。

- 🤖 支持 Minecraft 1.8 至 1.21 全版本，提供实体追踪、方块查询、物理运动等核心功能
- 📦 包含完整的物品管理、合成系统、容器交互和战斗机制
- 🌐 可通过 Python 调用，支持浏览器实时查看机器人视角 (prismarine-viewer)
- 🔌 采用模块化设计，拥有活跃的第三方插件生态（路径寻找、PVP、自动采集等）
- 📚 提供详细文档、视频教程和多语言支持（含中文）
- ⚙️ 支持微软/离线认证，可连接领域服务器 (Realms)
- 🧪 包含完整的测试体系，采用 MIT 开源协议
- 🚀 被 2.9 万 + 项目使用，在 GitHub 获得 6k 星标和 1.1k 分叉

---

### [介绍“切片组件”——Waku](https://waku.gg/blog/rethinking-fine-grained-components)

**原文标题**: [Introducing “slice components” — Waku](https://waku.gg/blog/rethinking-fine-grained-components)

Waku v0.25 版本引入了全新的切片组件 API，重新设计了细粒度组件渲染方案，取代了已弃用的页面部件组件，提供了更灵活的渲染模式和跨页面组件复用能力。

- 🧩 切片组件定义在 src/pages/_slices 目录下，可通过<Slice id="组件名">在页面中复用
- 📁 切片 ID 对应文件名，嵌套路径使用 one/two 格式表示
- ⚡ 新增 lazy 切片组件，支持动态渲染静态页面中的特定组件
- 🔄 渲染模式默认值标准化：页面、布局和切片默认为静态，API 路由默认为动态
- ⚠️ 重大变更：页面默认渲染模式改为静态，需通过 getConfig 显式声明 dynamic
- 🎯 切片需在页面配置中明确声明，便于 Waku 进行打包处理
- 🌟 提供了类似 Astro 服务器岛屿功能的组件懒加载方案

---

### [GitHub - RetireJS/retire.js：用于检测使用已知漏洞JavaScript库的扫描器，并可生成所发现库的软件物料清单（SBOM）。](https://github.com/RetireJS/retire.js)

**原文标题**: [GitHub - RetireJS/retire.js: scanner detecting the use of JavaScript libraries with known vulnerabilities. Can also generate an SBOM of the libraries it finds.](https://github.com/RetireJS/retire.js)

Retire.js 是一个用于检测 JavaScript 库中已知漏洞的安全扫描工具，支持多种集成方式和 SBOM 生成功能。

- 🛡️ 核心功能是检测 JavaScript 和 Node.js 库中的已知安全漏洞，防范 OWASP Top 10 中的"使用含已知漏洞组件"风险
- ⚙️ 支持多平台：命令行扫描器、Grunt/Gulp 构建工具插件、浏览器扩展（Chrome/Firefox）及渗透测试工具（Burp/ZAP）集成
- 📋 具备软件物料清单（SBOM）生成能力，支持 CycloneDX 格式输出
- 🌐 开源项目采用 Apache-2.0 许可证，获得 3.9k 星标和 424 个分支，由社区共同维护
- 🔧 提供完整的开发集成方案，包括实时文件监控、构建流程自动检测和可视化告警功能
- 💝 接受捐赠以支持漏洞库维护和工具持续开发

---

### [GitHub - sindresorhus/ky：🌳 基于 Fetch API 的轻量优雅 JavaScript HTTP 客户端](https://github.com/sindresorhus/ky)

**原文标题**: [GitHub - sindresorhus/ky: 🌳 Tiny & elegant JavaScript HTTP client based on the Fetch API](https://github.com/sindresorhus/ky)

Ky 是一个基于 Fetch API 的轻量级 JavaScript HTTP 客户端，提供简洁 API 和增强功能，适用于现代浏览器和 Node.js 等环境。

- 🌳 基于 Fetch API 的轻量级 HTTP 客户端，无依赖且设计优雅
- ⚡ 提供比原生 fetch 更简化的 API，包含快捷方法和自动错误处理
- 🔄 支持请求重试、超时控制和 URL 前缀配置
- 🎯 内置 JSON 处理、TypeScript 支持和自定义钩子函数
- 🌐 兼容浏览器、Node.js、Deno 和 Bun 等多平台运行环境
- 📦 可通过 npm 或 CDN 安装，支持自定义实例和扩展配置

---

### [发布 v1.3.0 · yamadashy/repomix · GitHub](https://github.com/yamadashy/repomix/releases/tag/v1.3.0)

**原文标题**: [Release v1.3.0 · yamadashy/repomix · GitHub](https://github.com/yamadashy/repomix/releases/tag/v1.3.0)

Repomix v1.3.0 版本发布，引入了令牌计数分析工具和 MCP 服务器增强功能，便于代码库处理的分析与优化。

- 🚀 新增令牌计数树形视图功能，可分级显示文件及目录的令牌使用情况
- 📊 支持设置最小阈值筛选高令牌消耗文件，便于优化输出
- 🔧 MCP 服务器新增附加打包输出工具，支持直接分析历史生成的 XML 文件
- 📋 无需重新处理代码库即可获得结构化分析能力
- 🔄 可通过 npm update 命令全局更新 repomix 工具
- 👥 本次更新由 petrarca 和 gudber 两位贡献者主要开发

---

### [GitHub - Hacker0x01/react-datepicker: 一个简单可复用的 React 日期选择器组件](https://github.com/Hacker0x01/react-datepicker)

**原文标题**: [GitHub - Hacker0x01/react-datepicker: A simple and reusable datepicker component for React](https://github.com/Hacker0x01/react-datepicker)

这是一个用于 React 的简单可复用日期选择器组件，具有丰富的功能和良好的社区支持。

- 📅 一个简单可复用的 React 日期选择器组件，支持时间选择和本地化
- ⭐ 在 GitHub 上获得 8.3k 星标和 2.3k 分支，显示其受欢迎程度
- 🌍 支持国际化，使用 date-fns 进行本地化处理，可设置不同语言环境
- ⏰ 提供时间选择功能，可配置时间间隔（默认 30 分钟）
- ⌨️ 具备完整的键盘导航支持，包括方向键、翻页键等快捷键操作
- 📦 通过 npm 或 yarn 安装，需要单独安装 React 和 PropTypes 依赖
- 🔧 提供详细的配置选项和事件处理程序（onChange、onSelect 等）
- 🎯 兼容 React 16 及以上版本，从 v2.0.0 开始使用 date-fns 替代 Moment.js
- 📚 包含完整的文档和示例，支持本地开发和测试
- 📝 采用 MIT 开源许可证，由 HackerOne Inc.和社区贡献者维护

---

### [HackerOne 精心打造的 React 日期选择器](https://reactdatepicker.com/)

**原文标题**: [React Datepicker crafted by HackerOne](https://reactdatepicker.com/)

文章概述了人工智能在医疗领域的应用现状与未来潜力，重点分析了其对诊断效率和精准治疗的提升作用。

- 🤖 通过深度学习技术分析医学影像，辅助医生进行早期疾病筛查
- 🧬 基于基因组数据开发个性化治疗方案，提高癌症等重症治愈率
- ⚡ 大幅缩短药物研发周期，通过模拟实验加速新药上市进程
- 📊 智能健康监测设备实时收集生理数据，实现慢性病动态管理
- 🌐 远程医疗平台突破地域限制，使优质医疗资源惠及偏远地区
- 🔒 采用区块链技术加强患者隐私保护，确保医疗数据安全共享

---

### [GitHub - mourner/flatbush: 一个用于 JavaScript 中 2D 点和矩形的极速静态空间索引 🌱](https://github.com/mourner/flatbush)

**原文标题**: [GitHub - mourner/flatbush: A very fast static spatial index for 2D points and rectangles in JavaScript 🌱](https://github.com/mourner/flatbush)

Flatbush 是一个用于 JavaScript 的极速静态空间索引库，适用于二维点和矩形，支持高效空间查询和低内存占用。

- 🌱 基于打包希尔伯特 R 树算法，支持百万级对象快速查询
- 📦 索引存储为单一数组缓冲区，可跨线程传输或保存为二进制文件
- 🚀 静态索引结构，初始化后无法增删项目，但索引和搜索速度远超 RBush
- 🗺️ 通过 geoflatbush 扩展支持地理坐标查询，兼容 K 最近邻和范围搜索
- 📊 提供多种配置选项（节点大小、数组类型等），支持浏览器和 Node.js 环境
- ⚡ 性能表现卓越：百万矩形索引仅需 273ms，比 RBush 快 4 倍以上
- 🌐 拥有多语言移植版本（C++/Rust/Python/C# 等），采用 ISC 开源协议

---

### [GitHub - plotly/plotly.js：Plotly和Dash背后的开源JavaScript图表库](https://github.com/plotly/plotly.js)

**原文标题**: [GitHub - plotly/plotly.js: Open-source JavaScript charting library behind Plotly and Dash](https://github.com/plotly/plotly.js)

Plotly.js 是一个开源的 JavaScript 数据可视化库，支持多种图表类型，并作为 Plotly 生态系统（如 Plotly.py 和 Plotly.R）的核心组件。  
- 📊 提供数十种图表类型，包括统计图表、3D 图形和地图等  
- 📦 可通过 npm 安装或 CDN 脚本加载使用  
- 🔧 支持自定义捆绑以优化文件大小  
- 📚 官方文档托管在 plotly.com/javascript  
- 👥 拥有活跃的社区和众多贡献者  
- ⭐ GitHub 上获得 17.8k 星标和 1.9k 分叉  
- 📝 采用 MIT 许可证开源

---

### [GitHub - chaijs/chai：适用于 Node.js 和浏览器的 BDD / TDD 断言框架，可与任何测试框架配对使用。](https://github.com/chaijs/chai)

**原文标题**: [GitHub - chaijs/chai: BDD / TDD assertion framework for node.js and the browser that can be paired with any testing framework.](https://github.com/chaijs/chai)

Chai 是一个用于 Node.js 和浏览器的 BDD/TDD 断言库，可与任何 JavaScript 测试框架搭配使用。

- 🚀 支持多种断言风格（assert、expect、should）
- 📦 可通过 npm 安装，支持 Node 和浏览器环境
- 🔌 提供强大的插件架构用于扩展功能
- 🌐 拥有 8.2k 星标和 707 个 fork 的开源项目
- 📚 提供详细文档和官方插件列表
- 🤝 采用 MIT 许可证，拥有 168 位贡献者
- 🧪 与 Mocha 等测试框架完美集成
- 💻 完全使用 JavaScript 编写

---

### [一丝不苟](https://www.meticulous.ai/?utm_source=javascript_weekly&utm_campaign=august22nd2025)

**原文标题**: [Meticulous](https://www.meticulous.ai/?utm_source=javascript_weekly&utm_campaign=august22nd2025)

Meticulous AI 是一款革命性的自动化测试工具，通过记录用户与应用交互过程自动生成并维护测试套件，无需编写代码即可全面覆盖应用功能和边缘情况，帮助开发团队提升代码质量和发布速度。

- 🚀 无需编写或维护测试用例，自动生成覆盖所有代码分支和用户流程的视觉端到端测试
- 📹 通过添加脚本标签记录开发、预发布和生产环境中的用户会话，构建持续演化的测试套件
- ⚡ 在 120 秒内并行完成数千次测试，提供无 flakes 的确定性测试结果
- 🔒 通过模拟后端响应实现无副作用测试，避免因数据变化导致的误报
- 🌐 支持主流前端框架包括 NextJS、React、Vue、Angular、Nuxt 和 SvelteKit
- 💼 已被 Dropbox、Notion、Lattice 等 100 多家组织采用，有效防止回归问题
- 🎯 可与现有测试套件结合使用或完全替代，显著提升开发效率和代码可靠性

---

### [开始使用 Redis](https://redis.io/lp/get-started2/?utm_source=cooper-press&utm_medium=cpa&utm_campaign=2025-08-app_performance-javascript-weekly-1&utm_content=cloud_-_redis_cloud_users)

**原文标题**: [Get started with Redis](https://redis.io/lp/get-started2/?utm_source=cooper-press&utm_medium=cpa&utm_campaign=2025-08-app_performance-javascript-weekly-1&utm_content=cloud_-_redis_cloud_users)

Redis 是一个高速数据平台，提供云端和本地部署解决方案，帮助团队快速构建应用程序。

- 🚀 作为专为速度设计的数据技术，支持向量数据库、缓存和 NoSQL 数据库的快速部署
- 🤖 向量数据库功能可构建最可靠的生成式 AI 应用程序
- ⚡ 内存缓存技术助力团队实现应用极速响应
- 🗄️ 支持多种数据结构的键值存储 NoSQL 数据库，适用于实时应用场景
- 🌩️ 通过 Redis Cloud 可轻松创建首个数据库，支持从实验到生产级 AI 应用的无缝扩展
- 🛠️ 为开发者、架构师和运维团队分别提供专属资源中心和演示服务
- 🆓 提供免费构建体验，支持多种开发语言环境

---

### [开始使用 Redis](https://redis.io/lp/get-started2/?utm_source=cooper-press&utm_medium=cpa&utm_campaign=2025-08-app_performance-javascript-weekly-1&utm_content=cloud_-_redis_cloud_users)

**原文标题**: [Get started with Redis](https://redis.io/lp/get-started2/?utm_source=cooper-press&utm_medium=cpa&utm_campaign=2025-08-app_performance-javascript-weekly-1&utm_content=cloud_-_redis_cloud_users)

Redis 是一个高速数据平台，提供云端和本地部署解决方案，帮助团队快速构建应用程序。

- 🚀 作为矢量数据库、缓存和 NoSQL 数据库，支持开箱即用的快速部署
- 🤖 先进的矢量数据库助力构建高效可靠的生成式 AI 应用
- ⚡ 全球最快内存数据库显著提升应用开发速度
- 🗃️ 支持多种数据结构的键值存储，适用于实时应用场景
- 🌟 提供从实验到生产环境的无缝扩展能力
- 💻 支持多语言开发，提供开发者中心和技术讲座资源
- 🆓 提供免费试用选项，可快速创建首个数据库

---

### [SmallJS - 主页](https://small-js.org/Home/Home.html)

**原文标题**: [SmallJS - Home](https://small-js.org/Home/Home.html)

SmallJS 是一个免费开源的 Smalltalk-80 语言实现，可将代码编译为 JavaScript，适用于现代浏览器和 Node.js 环境。它采用基于文件的开发方式，支持主流 IDE 开发，完全面向对象设计，并封装了多种常用 JS 库。

- 🎉 SmallJS v1.7 版本已于 2025 年 8 月 18 日发布
- 🔗 开源代码托管在 github.com/small-js/smalljs
- 🐧 基于优雅强大的 Smalltalk-80 语言实现
- 📁 采用文件式开发（非镜像式），支持 VS Code 集成开发环境
- 🐞 提供语法高亮和步进调试功能
- 🔄 自动导入使用到的基库组件
- 🧩 完全面向对象设计，保持与 JS 相似的类方法命名
- 🌐 已封装浏览器 DOM、事件、CSS 和 Node.js 服务器、数据库等核心库
- 📚 提供多个示例项目帮助快速入门
- ✉️ 可通过 info@small-js.org 参与贡献或咨询

---

### [NW.js](https://nwjs.io/)

**原文标题**: [NW.js](https://nwjs.io/)

NW.js 是一个基于 Web 技术构建原生应用程序的开源框架，融合了 Node.js 和浏览器环境的功能。

- 🌐 支持使用 HTML5、CSS3 和 WebGL 等 Web 技术开发原生应用
- 🚀 完全兼容浏览器特性与 Node.js API 及第三方模块
- 🔗 支持直接从 DOM 和 Web Workers 调用 Node.js 模块
- 🔒 提供 JavaScript 源代码保护功能
- 💻 支持跨平台运行（Linux/Mac OS X/Windows）
- 🤝 拥有活跃社区支持（邮件列表/Gitter/Discord 讨论组）
- 📚 提供完整文档、Wiki 和 GitHub 开源资源

---

### [我如何构建出比 Next.js 快 4 倍、吞吐量高 4 倍的全栈 React 框架 - Ryan Skinner](https://ryanskinner.com/posts/how-i-built-a-full-stack-react-framework-4x-faster-than-nextjs-with-4x-more-throughput)

**原文标题**: [How I Built a Full-Stack React Framework 4x Faster Than Next.js With 4x More Throughput - Ryan Skinner](https://ryanskinner.com/posts/how-i-built-a-full-stack-react-framework-4x-faster-than-nextjs-with-4x-more-throughput)

经过 25 年 web 开发经验，作者推出全新全栈 React 框架 Rari，通过 Rust 运行时架构实现突破性性能提升，在响应速度、吞吐量和构建效率方面显著优于现有方案，同时保持完整的 React Server Components 兼容性和开发者友好体验。

- 🚀 性能表现卓越：组件渲染速度快 4.04 倍，吞吐量高 3.74 倍，构建时间缩短 5.8 倍
- 🦀 创新架构设计：基于 Rust 运行时核心，直接集成 V8 引擎，实现零成本抽象和真正并发处理
- 🔄 完整 RSC 支持：100% 兼容 React Server Components 并提供真正的流式渲染支持
- ⚡ 智能开发体验：集成 Vite 构建工具，支持服务端/客户端组件自动检测和热模块替换
- 📦 开箱即用：TypeScript 原生支持，文件路由自动发现，无需复杂配置即可启动开发
- 🌐 开源生态：MIT 许可证开放源码，提供完整基准测试代码和社区交流平台

---

### [环法自行车赛中最快的网站——CSS 魔法](https://csswizardry.com/2025/07/the-fastest-site-in-the-tour-de-france/)

**原文标题**: [The Fastest Site in the Tour de France – CSS Wizardry](https://csswizardry.com/2025/07/the-fastest-site-in-the-tour-de-france/)

哈里·罗伯茨是一位专注于提升网站性能的独立顾问工程师，为各类企业提供专业的速度优化解决方案。
- 🛠️ 独立顾问身份
- 💼 服务各类规模企业
- ⚡ 专精网站速度问题诊断与修复

---

### [AWS 2025：那些你以为正确实则错误的认知 - 《上周 AWS 动态》博客](https://www.lastweekinaws.com/blog/aws-in-2025-the-stuff-you-think-you-know-thats-now-wrong/)

**原文标题**: [AWS in 2025: The Stuff You Think You Know That's Now Wrong - Last Week in AWS Blog](https://www.lastweekinaws.com/blog/aws-in-2025-the-stuff-you-think-you-know-thats-now-wrong/)

AWS 作为已有近 20 年历史的云平台，其基础服务持续演进，许多旧有操作方式和认知已过时。本文梳理了多项关键服务的现代化改进。

- 🖥️ EC2 实例支持运行时修改安全组、IAM 角色、EBS 卷调整，并可强制终止实例
- 🔄 实例可靠性大幅提升，实时迁移功能减少服务中断，Spot 实例定价机制更稳定
- 🛡️ 新账户默认启用 AMI 和 S3 存储桶的公共访问阻断功能，S3 实现读写强一致性
- ❄️ Glacier 存储类恢复费用降低且速度提升，不再需要密钥随机化避免热点
- 🌐 VPC 对等连接优化，新增 Transit Gateway 和 Cloud WAN 等高级网络方案
- ⚡ Lambda 支持 15 分钟超时、容器镜像、10GB 内存/存储，冷启动问题显著改善
- 💾 EFS 支持独立调整 IO 性能，EBS 空卷即享全性能（需预读快照卷数据）
- 🗄️ DynamoDB 允许空字段，性能监控更透明，按需计费成为主流选择
- 💰 节省计划逐步替代预留实例，支持秒级计费，成本异常检测功能免费且精准
- 🔐 IAM 角色成为权限管理核心，IAM Identity Center 替代传统 SSO 方案
- 🚨 us-east-1 区域稳定性提升，CloudWatch 数据一致性改善
- ⚠️ 需警惕小众服务的弃用风险，但文中提及的核心服务均属安全选择

（注：最后部分关于 Malphas 晋升等内容属于作者讽刺性创作，未纳入实质性摘要）

---

### [正则表达式等价性检查器](https://gruhn.github.io/regex-utils/equiv-checker.html)

**原文标题**: [RegExp Equivalence Checker](https://gruhn.github.io/regex-utils/equiv-checker.html)

该工具用于检查两个 JavaScript 正则表达式是否等价，即是否匹配完全相同的字符串，并提供差异示例和语法支持说明。

- 🔍 输入两个正则表达式（不带斜杠）即可检测等价性
- ⚠️ 注意未使用^和$锚点时可能产生意外匹配结果
- 📋 支持量词、字符类、分组、前瞻等基本语法
- 🚫 不支持全局标志、Unicode 属性、反向引用等高级功能
- 💡 由@gruhn/regex-utils TypeScript 库提供技术支持
- 📊 不等价时会显示仅被一个表达式匹配的示例字符串

---

