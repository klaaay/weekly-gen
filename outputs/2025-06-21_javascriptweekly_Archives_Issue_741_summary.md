### [JavaScript 周刊第 741 期：2025 年 6 月 20 日](https://javascriptweekly.com/issues/741)

**原文标题**: [JavaScript Weekly Issue 741: June 20, 2025](https://javascriptweekly.com/issues/741)

概述总结  
本期内容涵盖 JavaScript 技术动态、工具更新、文章推荐及行业新闻，包括现代 JavaScript 书籍推荐、性能优化工具、框架发布、开发者资源等。  

- 📚 Dr. Axel 发布《Exploring JavaScript (ES2025 Edition)》，免费在线阅读并提供学习闪卡。  
- ⚡ Notion 通过优化减少 15% 输入延迟，Palette 工具帮助诊断 Web 应用性能问题。  
- 🔍 Biome v2 推出首个无需 TypeScript 编译器的类型感知 Linter。  
- 🌐 Chrome 团队更新 HTML 规范，Figma 收购开源框架 Payload。  
- 🚀 多个框架发布新版本：Bun、Astro、ESLint、Hono 等。  
- 📹 视频与文章推荐：JavaScript 预编译、顶层 await 使用、TypeScript 解决全局命名冲突等。  
- 🛠️ 新工具推荐：语法高亮自定义元素、React Native 0.80、数据网格 Handsontable 等。  
- 📢 行业动态：CKEditor 包体积优化 40%、JPEG 统治 Web 的故事、Git 2.50.0 发布等。

---

### [探索 JavaScript（ES2025 版）](https://exploringjs.com/js/)

**原文标题**: [Exploring JavaScript (ES2025 Edition)](https://exploringjs.com/js/)

Axel 的《探索 JavaScript》ES2025 版是一本面向新手的现代 JavaScript 指南，提供免费在线阅读及付费离线资源包，涵盖 ES2025 核心特性并附带练习和闪卡辅助学习。

- 📚 书名《探索 JavaScript》（原《JavaScript for impatient programmers》），作者 Dr. Axel Rauschmayer，专为新手设计现代学习路径  
- 🎯 特点：从现代特性切入、可选进阶章节、无 DRM 数字资源、含测试驱动练习和 API 闪卡  
- 💻 免费在线阅读全书，付费包提供 HTML/EPUB/PDF 格式及额外学习工具（练习题/Anki 闪卡）  
- 💰 数字套餐：39 美元（电子书）或 59 美元（电子书 + 附加资源），旧版升级可享 5-7.5 折优惠  
- 📖 印刷版《JavaScript for impatient programmers》（ES2019 版）在全球多国亚马逊有售  
- ✉️ 支持批量购买（10 本以上）及经济困难折扣申请，印刷版持有者可优惠获取数字附加包  
- 👨🏫 作者为 JavaScript 专家，自 2009 年起持续输出博客、书籍及培训课程

---

### [目录 • 探索 JavaScript（ES2025 版）](https://exploringjs.com/js/book/index.html)

**原文标题**: [Table of contents • Exploring JavaScript (ES2025 Edition)](https://exploringjs.com/js/book/index.html)

这是一本关于 JavaScript（ES2025 版）的书籍，涵盖了从基础到高级的广泛主题，包括变量、控制流、模块、异步编程、集合、正则表达式等。

- 📚 书籍支持购买和捐赠，并提供预览和购买选项  
- 🔍 搜索功能需要启用 JavaScript  
- 📖 包含背景知识、常见问题解答和 JavaScript 的历史与演变  
- 🆕 详细列出 ES2025 到 ES2016 的新特性  
- 📝 提供变量、值、运算符、原始值等基础概念的深入讲解  
- 🔄 涵盖控制流、异常处理、函数调用和动态代码评估  
- 🧩 讨论模块化、对象、类和集合（如 Map、Set 等）  
- ⏳ 深入探讨异步编程，包括 Promise、async 函数和异步迭代  
- 📊 包含正则表达式、日期处理和 JSON 操作等标准库内容  
- 🌐 提供 Web 开发的下一步学习建议和工具概览  
- 🔗 附录包含索引，方便快速查找内容

---

### [主题闪卡（预览）](https://exploringjs.com/js/downloads/exploring-js-cards-topics-preview.html)

**原文标题**: [Topic flashcards (preview)](https://exploringjs.com/js/downloads/exploring-js-cards-topics-preview.html)

JavaScript 是一种多范式的编程语言，支持事件驱动、函数式和面向对象编程风格。以下是关于 JavaScript 的一些关键点总结：

- 🚀 **历史与影响**：JavaScript 于 1995 年由 Brendan Eich 在 10 天内创建，受到 Java、Self、Scheme、AWK、Perl 和 HyperTalk 的影响。
- 🔄 **标准与命名**：JavaScript 的标准由 ECMA-262 和 ISO/IEC 16262 定义，正式名称为 ECMAScript，因商标问题未使用 JavaScript。
- 🔧 **TC39 流程**：TC39 是推动 JavaScript 发展的委员会，提案分为 0 到 4 阶段，包括设计、测试和集成。
- ⚙️ **变量与作用域**：`const` 和 `let` 是块级作用域变量，`const` 绑定不可变，但值可能可变。变量声明前访问会进入暂时性死区（TDZ）。
- 🔄 **函数与闭包**：所有 JavaScript 函数都是闭包，保持其出生地的变量连接。函数可以是普通函数、箭头函数或方法。
- 🔢 **数据类型**：JavaScript 有原始类型（如 `undefined`、`null`、布尔、数字、字符串等）和对象类型。原始类型不可变，按值传递和比较。
- 🔍 **类型检查**：`typeof` 操作符返回类型字符串，如 `'undefined'`、`'object'`（`null`）、`'boolean'`、`'number'` 等。
- 🔄 **类型转换**：JavaScript 自动进行类型强制转换（coercion），如 `'7' * '3'` 返回 `21`。`==` 操作符在类型不同时进行强制转换。
- 🔢 **数字与 BigInt**：JavaScript 有 64 位浮点数（数字）和任意精度整数（BigInt）。数字有安全整数范围（±2^53-1）。
- 📜 **字符串与 Unicode**：字符串由 UTF-16 代码单元组成，支持 Unicode 码点和字形簇。模板字符串支持多行文本和插值。
- 🔑 **符号（Symbols）**：符号是唯一且不可变的原始值，常用作对象属性的键，避免命名冲突。
- 🔄 **对象与原型**：对象可以是固定布局或字典形式。原型链用于继承，`Object.create(null)` 创建无原型对象。
- 🛡️ **对象保护**：`Object.preventExtensions`、`Object.seal` 和 `Object.freeze` 提供不同级别的不可变性保护。
- 🔄 **类与继承**：类语法是构造函数的语法糖，支持静态方法、实例方法和字段。`instanceof` 检查原型链。
- 🔗 **模块系统**：ES 模块支持静态导入/导出，动态导入使用 `import()`。模块可以是脚本、CommonJS、AMD 或 ES 模块。
- 📦 **包管理**：npm 是常用的包管理器，包通过 `package.json` 定义依赖，`node_modules` 存储依赖。
- 🔄 **错误处理**：`try/catch/finally` 用于异常处理，`Error` 及其子类表示错误，支持自定义错误和链式错误。
- 🔄 **控制流**：JavaScript 支持 `if`、`switch`、循环（`for`、`while` 等）和提前退出（`break`、`continue`）。
- 🔄 **异步编程**：`Promise`、`async/await` 用于处理异步操作，`for-await-of` 遍历异步可迭代对象。
- 🔄 **元编程**：`eval` 和 `new Function()` 动态执行代码，`Proxy` 和 `Reflect` 提供对象操作的钩子。

JavaScript 的设计注重向后兼容，新特性通过完全兼容的版本引入，避免破坏现有代码。

---

### [主题闪卡（预览）](https://exploringjs.com/js/downloads/exploring-js-cards-topics-preview.html)

**原文标题**: [Topic flashcards (preview)](https://exploringjs.com/js/downloads/exploring-js-cards-topics-preview.html)

以下是按照您提供的模板对文本内容的概述总结和关键点列表：

### 概述总结
本文深入探讨了 JavaScript 的多个核心概念，包括其历史背景、语言特性、数据类型、函数、模块、对象、类以及错误处理等。JavaScript 作为一种多范式的编程语言，支持事件驱动、函数式和面向对象编程风格。文章详细解释了 JavaScript 的语法、变量作用域、控制流、异常处理、动态代码评估、模块系统、对象和类的使用，以及如何有效地处理错误和异常。此外，还涵盖了 JavaScript 的类型系统，包括原始值和对象的区别，以及如何使用符号（Symbols）作为唯一的属性键。文章还讨论了 JavaScript 的模块化开发，包括 CommonJS 和 ECMAScript 模块的区别，以及如何使用包管理器（如 npm）来管理依赖。最后，文章提供了关于 JavaScript 的未来发展趋势和最佳实践的见解。

### 关键点列表
- 📜 **JavaScript 的历史和影响**：JavaScript 在 1995 年由 Brendan Eich 创建，受到 Java、Self、Scheme、AWK、Perl 和 HyperTalk 的影响。
- 🔄 **JavaScript 的静默失败**：由于历史原因，JavaScript 在 ECMAScript 3 之前没有异常处理机制，导致静默失败。
- 📅 **JavaScript 的创建时间**：JavaScript 在 1995 年 5 月用 10 天时间创建。
- 🌐 **JavaScript 的标准组织**：ECMA-262 由 Ecma International 主持，ISO/IEC 16262 由 ISO 和 IEC 主持。
- 🔍 **JavaScript 与 ECMAScript 的区别**：JavaScript 指语言及其实现，ECMAScript 指语言标准及版本。
- 📊 **TC39 委员会**：负责 JavaScript 的演进，成员包括 Adobe、Apple、Facebook、Google 等公司。
- 🔄 **TC39 提案阶段**：包括从 Stage 0（构思）到 Stage 4（集成到标准）的多个阶段。
- ⏮️ **JavaScript 的向后兼容性**：新版本完全向后兼容，旧特性不会被移除或修复，而是引入更好的版本。
- 🔢 **TC39 过程中的 Stage 2.7**：在 2023 年底添加，位于 Stage 2 和 Stage 3 之间，更接近 Stage 3。
- 🔒 **const 变量的不可变性**：const 仅保证绑定不可变，值本身可能可变。
- 🌍 **变量作用域**：变量的作用域是程序中可访问的区域，const 和 let 是块级作用域。
- 👥 **变量遮蔽**：在嵌套块中使用相同变量名会遮蔽外部变量。
- 🔄 **静态与动态现象**：静态现象与源代码相关，动态现象在运行时发生。
- 🌐 **JavaScript 变量作用域结构**：全局作用域是树的根，模块作用域是其直接子节点。
- 🔗 **globalThis 访问全局对象**：globalThis 是访问全局对象的标准方式。
- 🚫 **全局对象的用例**：通常被认为是错误，现代 JavaScript 特性使其使用减少。
- ⚠️ **访问未声明变量的异常**：JavaScript 在访问未声明变量时抛出异常。
- ⏳ **时间死区（TDZ）**：变量在声明前不可访问的时间段。
- 🚀 **早期激活的 JavaScript 构造**：包括 const、let、function、class、import 和 var。
- 🔗 **变量闭包**：函数与其出生地变量的连接，所有 JavaScript 函数都是闭包。
- 🔢 **原始值与对象的区别**：原始值不可变，按值传递和比较；对象可变，按身份传递和比较。
- 🔍 **typeof 的结果**：返回值的类型，如'undefined'、'object'、'boolean'、'number'等。
- 🏗️ **包装类的目的**：如 Number 和 String，用于转换值、提供工具函数和创建对象。
- 🔄 **强制类型转换**：JavaScript 自动将操作数转换为适合的类型。
- 🤔 **运算符的意外结果**：由于强制类型转换和仅处理原始值，运算符可能产生意外结果。
- ➕ **加号运算符的工作方式**：根据操作数类型切换到字符串模式或数字模式。
- ❓ **==运算符的怪异行为**：由于类型强制转换，==可能产生非直观结果。
- === **与 Object.is() 的区别**：Object.is() 更严格，如认为 NaN 等于自身，区分 +0 和 -0。
- , **逗号运算符**：评估两个操作数并返回第二个。
- void **运算符**：评估操作数并返回 undefined。
- ❓ **undefined 与 null 的区别**：undefined 表示未初始化或不存在的值，null 表示有意缺少对象值。
- 📝 **undefined 的出现场景**：未初始化变量、未提供参数、缺少属性、无返回值的函数等。
- 📌 **null 的出现场景**：对象原型链末端、正则表达式匹配失败、JSON 不支持 undefined 等。
- ?? **空值合并运算符**：如果值为 undefined 或 null，则返回默认值。
- ??= **空值合并赋值运算符**：如果值为 undefined 或 null，则赋值默认值。
- ❌ **读取属性时的错误**：仅在 undefined 和 null 时尝试读取属性会抛出异常。
- 🤷 **JavaScript 有两个非值的原因**：null 表示“非对象”，undefined 表示“非对象也非原始值”。
- ✔️ **真值与假值**：除 undefined、null、false、0、NaN、0n、''外，所有值都是真值。
- ❓ **if 语句的表达式版本**：条件运算符（三元运算符）。
- && **和||运算符**：逻辑与和逻辑或，具有值保留和短路特性。
- ! **逻辑非运算符**：将值强制转换为布尔值后取反。
- 🔢 **JavaScript 的数字类型**：包括双精度浮点数（Number）和任意精度整数（BigInt）。
- 📖 **整数字面量**：支持二进制、八进制、十进制和十六进制。
- e **指数表示法**：如 3e2 表示 3×10²。
- 🔍 **访问十进制整数属性的方法**：如 (7).toString(2)。
- 🔄 **转换为数字的方法**：Number(value)、+value、parseFloat(value)。
- ❌ **数字错误值**：NaN 和 Infinity，分别表示非数字和无限大。
- 🔢 **浮点数无法精确表示的十进制分数**：如 0.1 和 0.2。
- 🔢 **整数与浮点数的区别**：整数是无小数部分的浮点数，但在某些场景下行为不同。
- 🔒 **安全整数范围**：-2⁵³+1 到 2⁵³-1，超出此范围整数可能无法精确表示。
- 🔢 **位运算符的位数限制**：使用 32 位整数。
- 🔢 **BigInt 的引入原因**：处理超出安全整数范围的整数，如 Twitter 的 64 位 ID。
- 🔢 **BigInt 的工作方式**：原始数据类型，表示任意精度整数，字面量以 n 结尾。
- 🌐 **Unicode 码点与码元**：码点表示字符，码元编码码点，UTF-8 使用 8 位码元。
- 📊 **Unicode 码点结构**：分为 17 个平面，包括基本多文种平面（BMP）和补充平面。
- 🌐 **Web 开发中的 Unicode 编码**：UTF-16 用于内部表示，UTF-8 用于文件。
- ✍️ **Unicode 中的字素簇和字形**：字素簇是用户感知的字符，字形是绘制的图像。
- 📜 **字符串字面量**：包括普通字符串字面量和模板字面量。
- 🔄 **转换为字符串的常见方法**：String(v)、'' + v、v.toString()。
- 🔤 **字符串的组成单位**：码点、JavaScript 字符（UTF-16 码元）、字素簇。
- 🔠 **字符串字面量中的转义**：码单元转义、码点转义、ASCII 转义。
- 🔗 **字符串连接方法**：使用 + 运算符、+=运算符或数组的 join 方法。
- 🏷️ **标签函数的工作方式**：处理模板字符串，接收模板字符串和替换值。
- 📝 **多行模板字面量的两种使用方式**：使用标签函数或.trim() 方法。
- 🛠️ **String.raw 的作用**：创建原始字符串字面量，反斜杠不转义。
- 🔣 **符号的性质**：原始值，具有唯一身份，可用作对象属性键。
- 🏷️ **符号的用例**：用于常量和唯一属性键。
- 🔑 **符号作为属性键的优点**：避免与基级和元级属性键冲突。
- 🔄 **控制流语句**：包括 if、switch、while、do-while、for、for-of、for-await-of、for-in。
- 🚪 **提前退出循环的语句**：break 和带标签的 break。
- ⏭️ **跳过循环迭代的语句**：continue。
- ✔️ **控制流语句的条件**：可以是任何值，转换为布尔值后判断。
- 🔄 **选择循环方法的建议**：根据异步性、迭代性和数组类型选择。
- 🛑 **try-catch-finally 的作用**：try 执行常规代码，catch 处理异常，finally 始终执行。
- 📋 **Error 及其子类的属性**：包括 name、message、cause、stack。
- 🔧 **函数的种类**：普通函数（函数、方法、构造函数）和专用函数（箭头函数、方法、类）。
- 🔄 **参数默认值**：指定未提供参数时的默认值。
- 🔄 **剩余参数**：收集剩余参数为数组。
- 📝 **模拟命名参数**：使用对象字面量。
- 🔄 **展开函数调用**：使用...将可迭代对象展开为多个参数。
- 📞 **函数方法.call()**：显式指定 this 值。
- 📞 **函数方法.apply()**：显式指定 this 值，参数为数组。
- 📞 **函数方法.bind()**：返回新函数，固定 this 值和部分参数。
- 🔍 **eval 的直接与间接调用区别**：直接调用在当前作用域评估，间接调用在全局作用域评估。
- 🛠️ **new Function() 的工作方式**：创建函数对象，参数为字符串。
- 📦 **常见的 JavaScript 源代码单元**：脚本、CommonJS 模块、AMD 模块、ECMAScript 模块。
- 📦 **命名导出与默认导出的区别**：命名导出多个，默认导出一个。
- 📦 **命名空间导入**：将模块导入为对象，属性为命名导出。
- 🔄 **重新导出**：将其他模块的导出转为当前模块的导出。
- 📦 **包的定义**：包含标准化布局的目录，可包含各种文件。
- 📦 **包注册表与包管理器**：注册表存储包，管理器下载和安装包。
- 📦 **npm 包的两种名称**：全局名称和带范围的名称。
- 📦 **npm 包的两个重要文件系统条目**：package.json 和 node_modules 目录。
- 📦 **模块说明符的种类**：绝对说明符、相对说明符、裸说明符。
- 🌐 **import.meta.url**：包含当前模块文件的 URL。
- 🔄 **动态导入模块**：使用 import() 运算符，返回 Promise。
- ⏳ **顶层 await**：在模块顶层使用 await，模块变为异步。
- 📦 **导入属性**：如 type: 'json'，用于指定导入类型。
- 🛠️ **polyfill 的定义**：在不支持某特性的平台上实现该特性的代码。
- 📊 **对象的两种使用方式**：固定布局对象和字典对象。
- 🔑 **对象字面量中的访问器**：getter 和 setter 方法。
- 🔄 **展开到对象字面量**：使用...添加其他对象的属性。
- 🔄 **structuredClone() 的复制能力**：可复制除符号、函数、DOM 节点外的所有值。
- 🔄 **对象保护的三个级别**：防止扩展、密封、冻结。
- 🔒 **私有槽的存储位置**：使用类似符号的唯一键存储。
- 🔗 **超类、子类和实例的关系**：实例的原型链包括子类和超类的原型。
- 📊 **类成员的存储位置**：静态方法在类上，方法在原型上，字段在实例上。
- 🔍 **instanceof 的检查方式**：检查类的原型是否在实例的原型链上。
- 📊 **列出属性键的影响**：受符号和可枚举性影响。
- 🔢 **自有属性的列出顺序**：整数索引属性、字符串键属性、符号键属性。
- ⚠️ **使用对象作为字典的陷阱**：继承属性、存在检查、__proto__键。
- 🔍 **属性属性**：包括 configurable、enumerable、value、writable、get、set。
- 🛡️ **对象的三个保护级别**：防止扩展、密封、冻结。

---

### [API 抽认卡](https://exploringjs.com/js/api.html)

**原文标题**: [API flashcards](https://exploringjs.com/js/api.html)

以下是文本的概述总结和关键点：

概述总结：
本文详细介绍了 JavaScript 中各种 API 的使用方法，包括数字、数学、字符串、对象、类、同步迭代、数组、类型化数组、映射、集合、Promise 和正则表达式等。每个 API 都有详细的说明和示例代码，帮助开发者理解和应用这些功能。

- 🔢 **Number.EPSILON**: ES6 引入，表示 1 与下一个可表示的浮点数之间的差值。
- 🔢 **Number.MAX_VALUE**: ES1 引入，表示 JavaScript 中最大的正有限数。
- 🔢 **Number.MIN_VALUE**: ES1 引入，表示 JavaScript 中最小的正数。
- 🔢 **Number.NaN**: ES1 引入，与全局变量 NaN 相同。
- 🔢 **Number.NEGATIVE_INFINITY**: ES1 引入，与-Number.POSITIVE_INFINITY 相同。
- 🔢 **Number.POSITIVE_INFINITY**: ES1 引入，与全局变量 Infinity 相同。
- 🔢 **Number.isFinite()**: ES6 引入，检查一个数是否为实际数字（非 Infinity、-Infinity 或 NaN）。
- 🔢 **Number.isNaN()**: ES6 引入，检查一个数是否为 NaN。
- 🔢 **Number.parseFloat()**: ES6 引入，将字符串解析为浮点数。
- 🔢 **Number.prototype.toExponential()**: ES3 引入，返回数字的指数表示字符串。
- 🔢 **Number.prototype.toFixed()**: ES3 引入，返回指定位数的小数字符串。
- 🔢 **Number.prototype.toPrecision()**: ES3 引入，返回指定精度的数字字符串。
- 🔢 **Number.prototype.toString()**: ES1 引入，返回数字的字符串表示。
- 🔢 **Number.MIN_SAFE_INTEGER**: ES6 引入，表示 JavaScript 能明确表示的最小整数。
- 🔢 **Number.MAX_SAFE_INTEGER**: ES6 引入，表示 JavaScript 能明确表示的最大整数。
- 🔢 **Number.isInteger()**: ES6 引入，检查一个数是否为整数。
- 🔢 **Number.isSafeInteger()**: ES6 引入，检查一个数是否能明确表示一个整数。
- 🔢 **Number.parseInt()**: ES6 引入，将字符串解析为整数。
- 🔢 **Math.E**: ES1 引入，欧拉数，自然对数的底数。
- 🔢 **Math.LN10**: ES1 引入，10 的自然对数。
- 🔢 **Math.LN2**: ES1 引入，2 的自然对数。
- 🔢 **Math.LOG10E**: ES1 引入，以 10 为底 e 的对数。
- 🔢 **Math.LOG2E**: ES1 引入，以 2 为底 e 的对数。
- 🔢 **Math.PI**: ES1 引入，圆周率π。
- 🔢 **Math.SQRT1_2**: ES1 引入，1/2 的平方根。
- 🔢 **Math.SQRT2**: ES1 引入，2 的平方根。
- 🔢 **Math.cbrt()**: ES6 引入，返回一个数的立方根。
- 🔢 **Math.exp()**: ES1 引入，返回 e 的 x 次方。
- 🔢 **Math.expm1()**: ES6 引入，返回 e 的 x 次方减 1。
- 🔢 **Math.log()**: ES1 引入，返回一个数的自然对数。
- 🔢 **Math.log1p()**: ES6 引入，返回 1 加 x 的自然对数。
- 🔢 **Math.log10()**: ES6 引入，返回以 10 为底的对数。
- 🔢 **Math.log2()**: ES6 引入，返回以 2 为底的对数。
- 🔢 **Math.pow()**: ES1 引入，返回 x 的 y 次方。
- 🔢 **Math.sqrt()**: ES1 引入，返回一个数的平方根。
- 🔢 **Math.ceil()**: ES1 引入，向上取整。
- 🔢 **Math.floor()**: ES1 引入，向下取整。
- 🔢 **Math.round()**: ES1 引入，四舍五入。
- 🔢 **Math.trunc()**: ES6 引入，去除小数部分。
- 🔢 **Math.fround()**: ES6 引入，将数舍入到 32 位单精度浮点数。
- 🔢 **Math.f16round()**: ES2025 引入，将数舍入到 16 位半精度浮点数。
- 🔢 **Math.acos()**: ES1 引入，返回反余弦值。
- 🔢 **Math.acosh()**: ES6 引入，返回反双曲余弦值。
- 🔢 **Math.asin()**: ES1 引入，返回反正弦值。
- 🔢 **Math.asinh()**: ES6 引入，返回反双曲正弦值。
- 🔢 **Math.atan()**: ES1 引入，返回反正切值。
- 🔢 **Math.atanh()**: ES6 引入，返回反双曲正切值。
- 🔢 **Math.atan2()**: ES1 引入，返回 y/x 的反正切值。
- 🔢 **Math.cos()**: ES1 引入，返回余弦值。
- 🔢 **Math.cosh()**: ES6 引入，返回双曲余弦值。
- 🔢 **Math.hypot()**: ES6 引入，返回参数的平方和的平方根。
- 🔢 **Math.sin()**: ES1 引入，返回正弦值。
- 🔢 **Math.sinh()**: ES6 引入，返回双曲正弦值。
- 🔢 **Math.tan()**: ES1 引入，返回正切值。
- 🔢 **Math.tanh()**: ES6 引入，返回双曲正切值。
- 🔢 **Math.abs()**: ES1 引入，返回绝对值。
- 🔢 **Math.clz32()**: ES6 引入，返回 32 位整数前导零的数量。
- 🔢 **Math.max()**: ES1 引入，返回参数中的最大值。
- 🔢 **Math.min()**: ES1 引入，返回参数中的最小值。
- 🔢 **Math.random()**: ES1 引入，返回 0 到 1 之间的伪随机数。
- 🔢 **Math.sign()**: ES6 引入，返回数的符号。
- 🔢 **String.prototype.startsWith()**: ES6 引入，检查字符串是否以指定字符串开头。
- 🔢 **String.prototype.endsWith()**: ES6 引入，检查字符串是否以指定字符串结尾。
- 🔢 **String.prototype.includes()**: ES6 引入，检查字符串是否包含指定字符串。
- 🔢 **String.prototype.indexOf()**: ES1 引入，返回字符串中指定字符串首次出现的索引。
- 🔢 **String.prototype.lastIndexOf()**: ES1 引入，返回字符串中指定字符串最后出现的索引。
- 🔢 **String.prototype.slice()**: ES3 引入，返回字符串的指定部分。
- 🔢 **String.prototype.at()**: ES2022 引入，返回指定索引处的字符。
- 🔢 **String.prototype.substring()**: ES1 引入，返回字符串的子串（不推荐使用）。
- 🔢 **String.prototype.concat()**: ES3 引入，连接字符串。
- 🔢 **String.prototype.padEnd()**: ES2017 引入，用指定字符串填充到指定长度。
- 🔢 **String.prototype.padStart()**: ES2017 引入，用指定字符串填充到指定长度。
- 🔢 **String.prototype.repeat()**: ES6 引入，重复字符串指定次数。
- 🔢 **String.prototype.toUpperCase()**: ES1 引入，将字符串转换为大写。
- 🔢 **String.prototype.toLowerCase()**: ES1 引入，将字符串转换为小写。
- 🔢 **String.prototype.trim()**: ES5 引入，去除字符串两端的空白字符。
- 🔢 **String.prototype.trimStart()**: ES2019 引入，去除字符串开头的空白字符。
- 🔢 **String.prototype.trimEnd()**: ES2019 引入，去除字符串结尾的空白字符。
- 🔢 **String.prototype.normalize()**: ES6 引入，返回字符串的 Unicode 规范化形式。
- 🔢 **String.prototype.isWellFormed()**: ES2024 引入，检查字符串是否格式良好。
- 🔢 **String.prototype.toWellFormed()**: ES2024 引入，将字符串转换为格式良好的字符串。
- 🔢 **Object.create()**: ES5 引入，创建一个新对象，使用现有对象作为新对象的原型。
- 🔢 **Object.getPrototypeOf()**: ES5 引入，返回指定对象的原型。
- 🔢 **Object.setPrototypeOf()**: ES6 引入，设置对象的原型。
- 🔢 **Object.defineProperty()**: ES5 引入，定义或修改对象的属性。
- 🔢 **Object.defineProperties()**: ES5 引入，定义或修改对象的多个属性。
- 🔢 **Object.getOwnPropertyDescriptor()**: ES5 引入，返回对象属性的描述符。
- 🔢 **Object.getOwnPropertyDescriptors()**: ES2017 引入，返回对象所有属性的描述符。
- 🔢 **Object.keys()**: ES5 引入，返回对象的所有可枚举属性名。
- 🔢 **Object.getOwnPropertyNames()**: ES5 引入，返回对象的所有属性名（包括不可枚举）。
- 🔢 **Object.getOwnPropertySymbols()**: ES6 引入，返回对象的所有 Symbol 属性。
- 🔢 **Object.values()**: ES2017 引入，返回对象的所有可枚举属性值。
- 🔢 **Object.entries()**: ES2017 引入，返回对象的所有可枚举键值对。
- 🔢 **Object.fromEntries()**: ES2019 引入，将键值对列表转换为对象。
- 🔢 **Object.hasOwn()**: ES2022 引入，检查对象是否有指定属性。
- 🔢 **Object.preventExtensions()**: ES5 引入，防止对象扩展。
- 🔢 **Object.isExtensible()**: ES5 引入，检查对象是否可扩展。
- 🔢 **Object.seal()**: ES5 引入，密封对象。
- 🔢 **Object.isSealed()**: ES5 引入，检查对象是否密封。
- 🔢 **Object.freeze()**: ES5 引入，冻结对象。
- 🔢 **Object.isFrozen()**: ES5 引入，检查对象是否冻结。
- 🔢 **Object.assign()**: ES6 引入，复制一个或多个对象的属性到目标对象。
- 🔢 **Object.groupBy()**: ES2024 引入，根据回调函数分组对象。
- 🔢 **Object.is()**: ES6 引入，比较两个值是否相同。
- 🔢 **Reflect.apply()**: ES6 引入，调用目标函数。
- 🔢 **Reflect.construct()**: ES6 引入，作为函数调用 new 操作符。
- 🔢 **Reflect.defineProperty()**: ES6 引入，定义或修改对象属性。
- 🔢 **Reflect.deleteProperty()**: ES6 引入，删除对象属性。
- 🔢 **Reflect.get()**: ES6 引入，获取对象属性值。
- 🔢 **Reflect.getOwnPropertyDescriptor()**: ES6 引入，获取对象属性描述符。
- 🔢 **Reflect.getPrototypeOf()**: ES6 引入，获取对象原型。
- 🔢 **Reflect.has()**: ES6 引入，检查对象是否有指定属性。
- 🔢 **Reflect.isExtensible()**: ES6 引入，检查对象是否可扩展。
- 🔢 **Reflect.ownKeys()**: ES6 引入，返回对象的所有属性键。
- 🔢 **Reflect.preventExtensions()**: ES6 引入，防止对象扩展。
- 🔢 **Reflect.set()**: ES6 引入，设置对象属性值。
- 🔢 **Reflect.setPrototypeOf()**: ES6 引入，设置对象原型。
- 🔢 **Object.prototype.toString()**: ES1 引入，返回对象的字符串表示。
- 🔢 **Object.prototype.toLocaleString()**: ES3 引入，返回对象的本地化字符串表示。
- 🔢 **Object.prototype.valueOf()**: ES1 引入，返回对象的原始值。
- 🔢 **Object.prototype.isPrototypeOf()**: ES3 引入，检查对象是否在另一个对象的原型链上。
- 🔢 **Object.prototype.propertyIsEnumerable()**: ES3 引入，检查属性是否可枚举。
- 🔢 **Object.prototype.__proto__**: ES6 引入，获取或设置对象的原型（不推荐使用）。
- 🔢 **Object.prototype.hasOwnProperty()**: ES3 引入，检查对象是否有指定属性（不推荐使用）。
- 🔢 **Iterator.prototype.drop()**: ES2025 引入，返回跳过前 n 个元素的迭代器。
- 🔢 **Iterator.prototype.filter()**: ES2025 引入，返回过滤后的迭代器。
- 🔢 **Iterator.prototype.flatMap()**: ES2025 引入，返回扁平映射后的迭代器。
- 🔢 **Iterator.prototype.map()**: ES2025 引入，返回映射后的迭代器。
- 🔢 **Iterator.prototype.take()**: ES2025 引入，返回前 n 个元素的迭代器。
- 🔢 **Iterator.prototype.every()**: ES2025 引入，检查所有元素是否满足条件。
- 🔢 **Iterator.prototype.some()**: ES2025 引入，检查是否有元素满足条件。
- 🔢 **Iterator.prototype.find()**: ES2025 引入，返回第一个满足条件的元素。
- 🔢 **Iterator.prototype.reduce()**: ES2025 引入，将迭代器元素归约为单个值。
- 🔢 **Iterator.prototype.toArray()**: ES2025 引入，将迭代器转换为数组。
- 🔢 **Iterator.prototype.forEach()**: ES2025 引入，对每个元素执行回调。
- 🔢 **new Array()**: ES1 引入，创建数组。
- 🔢 **Array.from()**: ES6 引入，将类数组或可迭代对象转换为数组。
- 🔢 **Array.of()**: ES6 引入，创建包含参数的新数组。
- 🔢 **Array.prototype.at()**: ES2022 引入，返回指定索引处的元素。
- 🔢 **Array.prototype.with()**: ES2023 引入，返回修改指定索引后的新数组。
- 🔢 **Array.prototype.forEach()**: ES5 引入，对数组每个元素执行回调。
- 🔢 **Array.prototype.keys()**: ES6 引入，返回数组键的迭代器。
- 🔢 **Array.prototype.values()**: ES6 引入，返回数组值的迭代器。
- 🔢 **Array.prototype.entries()**: ES6 引入，返回数组键值对的迭代器。
- 🔢 **Array.prototype.pop()**: ES3 引入，移除并返回数组最后一个元素。
- 🔢 **Array.prototype.push()**: ES3 引入，向数组末尾添加元素。
- 🔢 **Array.prototype.shift()**: ES3 引入，移除并返回数组第一个元素。
- 🔢 **Array.prototype.unshift()**: ES3 引入，向数组开头添加元素。
- 🔢 **Array.prototype.concat()**: ES3 引入，合并数组。
- 🔢 **Array.prototype.slice()**: ES3 引入，返回数组的浅拷贝部分。
- 🔢 **Array.prototype.splice()**: ES3 引入，修改数组内容。
- 🔢 **Array.prototype.toSpliced()**: ES2023 引入，返回修改后的新数组。
- 🔢 **Array.prototype.fill()**: ES6 引入，填充数组元素。
- 🔢 **Array.prototype.copyWithin()**: ES6 引入，复制数组元素到指定位置。
- 🔢 **Array.prototype.includes()**: ES2016 引入，检查数组是否包含指定元素。
- 🔢 **Array.prototype.indexOf()**: ES5 引入，返回元素首次出现的索引。
- 🔢 **Array.prototype.lastIndexOf()**: ES5 引入，返回元素最后出现的索引。
- 🔢 **Array.prototype.find()**: ES6 引入，返回第一个满足条件的元素。
- 🔢 **Array.prototype.findLast()**: ES2023 引入，返回最后一个满足条件的元素。
- 🔢 **Array.prototype.findIndex()**: ES6 引入，返回第一个满足条件的元素的索引。
- 🔢 **Array.prototype.findLastIndex()**: ES2023 引入，返回最后一个满足条件的元素的索引。
- 🔢 **Array.prototype.filter()**: ES5 引入，返回满足条件的元素数组。
- 🔢 **Array.prototype.map()**: ES5 引入，返回映射后的数组。
- 🔢 **Array.prototype.flatMap()**: ES2019 引入，返回扁平映射后的数组。
- 🔢 **Array.prototype.flat()**: ES2019 引入，返回扁平化后的数组。
- 🔢 **Array.prototype.every()**: ES5 引入，检查所有元素是否满足条件。
- 🔢 **Array.prototype.some()**: ES5 引入，检查是否有元素满足条件。
- 🔢 **Array.prototype.reduce()**: ES5 引入，将数组归约为单个值。
- 🔢 **Array.prototype.reduceRight()**: ES5 引入，从右到左归约数组。
- 🔢 **Array.prototype.join()**: ES1 引入，将数组元素连接为字符串。
- 🔢 **Array.prototype.toString()**: ES1 引入，返回数组的字符串表示。
- 🔢 **Array.prototype.toLocaleString()**: ES3 引入，返回数组的本地化字符串表示。
- 🔢 **Array.prototype.sort()**: ES1 引入，排序数组。
- 🔢 **Array.prototype.toSorted()**: ES2023 引入，返回排序后的新数组。
- 🔢 **Array.prototype.reverse()**: ES1 引入，反转数组。
- 🔢 **Array.prototype.toReversed()**: ES2023 引入，返回反转后的新数组。
- 🔢 **new ArrayBuffer()**: ES6 引入，创建 ArrayBuffer。
- 🔢 **ArrayBuffer.isView()**: ES6 引入，检查参数是否为 ArrayBuffer 视图。
- 🔢 **ArrayBuffer.prototype.byteLength**: ES6 引入，返回 ArrayBuffer 的字节长度。
- 🔢 **ArrayBuffer.prototype.slice()**: ES6 引入，返回 ArrayBuffer 的部分字节。
- 🔢 **ArrayBuffer.prototype.resize()**: ES2024 引入，调整 ArrayBuffer 大小。
- 🔢 **ArrayBuffer.prototype.resizable**: ES2024 引入，检查 ArrayBuffer 是否可调整大小。
- 🔢 **ArrayBuffer.prototype.maxByteLength**: ES2024 引入，返回 ArrayBuffer 的最大字节长度。
- 🔢 **TypedArray.from()**: ES6 引入，将类数组或可迭代对象转换为类型化数组。
- 🔢 **TypedArray.of()**: ES6 引入，创建包含参数的类型化数组。
- 🔢 **TypedArray.prototype.buffer**: ES6 引入，返回类型化数组的 ArrayBuffer。
- 🔢 **TypedArray.prototype.length**: ES6 引入，返回类型化数组的元素数量。
- 🔢 **TypedArray.prototype.byteLength**: ES6 引入，返回类型化数组的字节长度。
- 🔢 **TypedArray.prototype.byteOffset**: ES6 引入，返回类型化数组的字节偏移量。
- 🔢 **TypedArray.prototype.set()**: ES6 引入，复制元素到类型化数组。
- 🔢 **TypedArray.prototype.subarray()**: ES6 引入，返回类型化数组的子数组。
- 🔢 **new DataView()**: ES6 引入，创建 DataView。
- 🔢 **DataView.prototype.buffer**: ES6 引入，返回 DataView 的 ArrayBuffer。
- 🔢 **DataView.prototype.byteLength**: ES6 引入，返回 DataView 的字节长度。
- 🔢 **DataView.prototype.byteOffset**: ES6 引入，返回 DataView 的字节偏移量。
- 🔢 **DataView.prototype.get()**: ES6 引入，从 DataView 读取值。
- 🔢 **DataView.prototype.set()**: ES6 引入，向 DataView 写入值。
- 🔢 **new Map()**: ES6 引入，创建 Map。
- 🔢 **Map.groupBy()**: ES2024 引入，根据回调函数分组 Map。
- 🔢 **Map.prototype.get()**: ES6 引入，获取 Map 中的值。
- 🔢 **Map.prototype.set()**: ES6 引入，设置 Map 中的键值对。
- 🔢 **Map.prototype.has()**: ES6 引入，检查 Map 中是否有键。
- 🔢 **Map.prototype.delete()**: ES6 引入，删除 Map 中的键值对。
- 🔢 **Map.prototype.size**: ES6 引入，返回 Map 中的键值对数量。
- 🔢 **Map.prototype.clear()**: ES6 引入，清空 Map。
- 🔢 **Map.prototype.entries()**: ES6 引入，返回 Map 的键值对迭代器。
- 🔢 **Map.prototype.forEach()**: ES6 引入，对 Map 每个键值对执行回调。
- 🔢 **Map.prototype.keys()**: ES6 引入，返回 Map 的键迭代器。
- 🔢 **Map.prototype.values()**: ES6 引入，返回 Map 的值迭代器。
- 🔢 **Map.prototype[Symbol.iterator]()**: ES6 引入，返回 Map 的键值对迭代器。
- 🔢 **new Set()**: ES6 引入，创建 Set。
- 🔢 **Set.prototype.add()**: ES6 引入，向 Set 添加元素。
- 🔢 **Set.prototype.delete()**: ES6 引入，从 Set 删除元素。
- 🔢 **Set.prototype.has()**: ES6 引入，检查 Set 中是否有元素。
- 🔢 **Set.prototype.size**: ES6 引入，返回 Set 中的元素数量。
- 🔢 **Set.prototype.clear()**: ES6 引入，清空 Set。
- 🔢 **Set.prototype.values()**: ES6 引入，返回 Set 的值迭代器。
- 🔢 **Set.prototype[Symbol.iterator]()**: ES6 引入，返回 Set 的值迭代器。
- 🔢 **Set.prototype.forEach()**: ES6 引入，对 Set 每个元素执行回调。
- 🔢 **Set.prototype.entries()**: ES6 引入，返回 Set 的键值对迭代器。
- 🔢 **Set.prototype.keys()**: ES6 引入，返回 Set 的值迭代器。
- 🔢 **Set.prototype.union()**: ES2025 引入，返回两个 Set 的并集。
- 🔢 **Set.prototype.intersection()**: ES2025 引入，返回两个 Set 的交集。
- 🔢 **Set.prototype.difference()**: ES2025 引入，返回两个 Set 的差集。
- 🔢 **Set.prototype.symmetricDifference()**: ES2025 引入，返回两个 Set 的对称差集。
- 🔢 **Set.prototype.isSubsetOf()**: ES2025 引入，检查 Set 是否为另一个 Set 的子集。
- 🔢 **Set.prototype.isSupersetOf()**: ES2025 引入，检查 Set 是否为另一个 Set 的超集。
- 🔢 **Set.prototype.isDisjointFrom()**: ES2025 引入，检查两个 Set 是否不相交。
- 🔢 **new Promise()**: ES6 引入，创建 Promise。
- 🔢 **Promise.withResolvers()**: ES2024 引入，创建 Promise 及其解析函数。
- 🔢 **Promise.resolve()**: ES6 引入，返回已解析的 Promise。
- 🔢 **Promise.reject()**: ES6 引入，返回已拒绝的 Promise。
- 🔢 **Promise.try()**: ES2025 引入，创建 Promise 并执行回调。
- 🔢 **Promise.all()**: ES6 引入，等待所有 Promise 解析。
- 🔢 **Promise.race()**: ES6 引入，返回第一个解析或拒绝的 Promise。
- 🔢 **Promise.any()**: ES2021 引入，返回第一个解析的 Promise。
- 🔢 **Promise.allSettled()**: ES2020 引入，等待所有 Promise 完成。
- 🔢 **Promise.prototype.then()**: ES6 引入，处理 Promise 解析。
- 🔢 **Promise.prototype.catch()**: ES6 引入，处理 Promise 拒绝。
- 🔢 **Promise.prototype.finally()**: ES2018 引入，无论 Promise 结果如何都执行回调。
- 🔢 **String.prototype.match()**: ES3 引入，匹配正则表达式。
- 🔢 **String.prototype.matchAll()**: ES2020 引入，匹配所有正则表达式。
- 🔢 **String.prototype.search()**: ES3 引入，搜索正则表达式。
- 🔢 **String.prototype.split()**: ES3 引入，根据分隔符分割字符串。
- 🔢 **String.prototype.replace()**: ES3 引入，替换字符串中的匹配项。
- 🔢 **String.prototype.replaceAll()**: ES2021 引入，替换字符串中的所有匹配项。
- 🔢 **RegExp.prototype.test()**: ES3 引入，测试正则表达式匹配。
- 🔢 **RegExp.prototype.exec()**: ES3 引入，执行正则表达式匹配。

---

### [生物群落 v2—代号：生物型 | 生物群落](https://biomejs.dev/blog/biome-v2/)

**原文标题**: [Biome v2—codename: Biotype | Biome](https://biomejs.dev/blog/biome-v2/)

Biome v2（代号：Biotype）正式发布，这是首个不依赖 TypeScript 编译器即可实现类型感知的 JavaScript 和 TypeScript 代码检查工具。

- 🎉 **Biome v2 发布**：首个不依赖 TypeScript 编译器的类型感知代码检查工具，无需安装`typescript`包即可使用。
- 🚀 **里程碑**：在短短两年内实现这一成就，特别感谢 Vercel 对类型推断工作的赞助。
- ⚡ **性能优势**：`noFloatingPromises`规则在性能影响极小的情况下，能检测约 75% 的浮动 Promise 问题。
- 📦 **安装与迁移**：通过`npm install`安装或更新，使用`migrate`命令处理配置变更，详情参见迁移指南。
- 🔍 **多文件分析与类型推断**：新增文件扫描器，支持跨文件类型查询，默认情况下为可选功能以保持性能。
- 🏗️ **Monorepo 支持**：改进对 monorepo 的支持，支持嵌套配置文件，通过`root`字段或`extends`字段进行配置。
- 🔌 **插件系统**：首次引入 Linter 插件，目前功能有限，但未来会扩展。
- 🔄 **导入组织器改进**：解决了 v1 中的多个限制，支持合并同模块导入、自定义排序等。
- 🛠️ **辅助功能**：新增 Biome Assist，支持如对象字面量键排序等操作。
- 🚫 **改进的抑制功能**：新增`// biome-ignore-all`和范围抑制标记。
- 📜 **HTML 格式化器**：实验性支持 HTML 文件格式化，未来将扩展至 Vue 和 Svelte 等框架。
- 👏 **致谢**：特别感谢 Vercel、Depot 等赞助商，以及所有核心贡献者和社区成员。
- 🔮 **未来计划**：包括稳定 HTML 支持、扩展框架支持、Markdown 解析器开发等。
- 🤝 **如何贡献**：可通过翻译、社区交流、代码贡献或财务支持等方式参与项目。

---

### [HTML 规范变更：属性中转义<和> | 博客 | Chrome 开发者](https://developer.chrome.com/blog/escape-attributes)

**原文标题**: [HTML spec change: escaping < and > in attributes  |  Blog  |  Chrome for Developers](https://developer.chrome.com/blog/escape-attributes)

HTML 规范更新：在属性中转义<和>字符，以增强安全性并防止 mXSS 漏洞。此变更主要影响序列化操作（如 innerHTML/outerHTML），不影响 DOM API 或 HTML 解析。Chrome 138（2025 年 6 月 24 日稳定版）将率先实施。

- 🛡️ **安全更新**：HTML 规范要求转义属性中的<和>，防止 mXSS 漏洞。  
- 🔄 **序列化变更**：通过 innerHTML/outerHTML 获取属性值时，字符将转义为&lt;和&gt;。  
- ⚠️ **潜在问题**：依赖正则提取属性值的代码可能失效，建议改用 DOM API（如 getAttribute）。  
- ✅ **兼容性**：DOM API（dataset/attributes 等）返回值不变，仅序列化结果受影响。  
- 🧪 **测试调整**：需更新含<或>的静态 HTML 测试预期值，匹配新转义规则。  
- 🌐 **浏览器支持**：Chrome 138（2025.6.24）、Firefox 140 及 Safari 26 Beta（约 2025.9）陆续生效。  
- 📝 **反馈渠道**：若遇兼容问题，可通过 Chromium 问题库提交反馈。  
- 📚 **延伸阅读**：规范 PR、安全博客及许可声明等资源链接已提供。

---

### [Payload 即将加入 Figma！](https://payloadcms.com/posts/blog/payload-is-joining-figma)

**原文标题**: [Payload is joining Figma!](https://payloadcms.com/posts/blog/payload-is-joining-figma)

Payload 宣布加入 Figma，双方将共同解决设计与代码之间的鸿沟问题，同时保持 Payload 的开源性和现有用户体验不变。

- 🎉 **重大消息**：Payload 正式加入 Figma，双方将携手推动设计与开发的无缝协作。  
- 🎨 **共同愿景**：Figma 认可 Payload 的开源理念，双方在简化工作流程和提升开发者体验上目标一致。  
- 🔄 **解决痛点**：旨在消除设计师（Figma）与开发者（代码）之间的效率瓶颈，避免内容团队重复劳动。  
- 🔒 **用户承诺**：短期内 Payload 的功能、开源协议、自托管能力和社区支持均保持不变。  
- 🚀 **未来变化**：更多资源投入、更大规模问题解决能力，以及与设计系统的深度集成。  
- 💬 **社区沟通**：团队将通过 Discord 和 GitHub 解答疑问，持续更新进展。  
- 🌟 **核心优势**：Payload 继续专注企业级应用、无头 CMS、电子商务等场景，保持开发者友好特性。

---

### [GitHub - payloadcms/payload: Payload 是一款开源的 Next.js 全栈框架，助您即刻拥有后端超能力。立即获取完整的 TypeScript 后端及管理面板，可将 Payload 用作无头 CMS 或构建强大应用。](https://github.com/payloadcms/payload)

**原文标题**: [GitHub - payloadcms/payload: Payload is the open-source, fullstack Next.js framework, giving you instant backend superpowers. Get a full TypeScript backend and admin panel instantly. Use Payload as a headless CMS or for building powerful applications.](https://github.com/payloadcms/payload)

Payload 是一个开源的、基于 Next.js 的全栈框架，提供即时后端功能和 TypeScript 支持，可作为无头 CMS 或用于构建强大应用。

- 🚀 **开源全栈框架**：Payload 是开源的，基于 Next.js，提供即时后端功能和 TypeScript 支持。  
- 🛠️ **多功能用途**：可作为无头 CMS 或用于构建强大的应用程序。  
- 📂 **Next.js 原生支持**：可直接在 `/app` 文件夹中运行，支持服务器组件。  
- 🔄 **模板支持**：提供多种生产就绪模板，如网站模板，支持 Tailwind 和 RSCs。  
- ✨ **丰富功能**：包括身份验证、版本控制、本地化、区块布局构建器等。  
- 📚 **详细文档**：提供全面的文档和迁移指南。  
- 🤝 **社区支持**：有活跃的 GitHub 讨论区和 Discord 社区。  
- 🔌 **插件扩展**：支持官方和社区插件，可扩展功能。  
- 🌟 **受欢迎**：拥有 35.6k GitHub stars 和 2.6k forks。

---

### [ViteConf 2025](https://viteconf.amsterdam/)

**原文标题**: [ViteConf 2025](https://viteconf.amsterdam/)

ViteConf 2025 是 Vite 的首次线下官方会议，将于 10 月 9 日至 10 日在阿姆斯特丹举行，汇聚前端生态系统的核心开发者和社区成员。

- 🎤 **官方 Vite 会议**：首次线下举办，聚焦 Vite 生态系统的最新动态。  
- 📅 **活动日程**：  
  - 🎉 **社区之夜**（10 月 8 日）：与开发者和嘉宾交流。  
  - 🚀 **主题会议**（10 月 9-10 日）：为期两天的技术分享与发布。  
  - 🎊 **派对之夜**（10 月 10 日）：庆祝活动与社交。  
- ☕ **参会福利**：免费餐饮、充电工作站、签到证书。  
- 🌟 **特邀嘉宾**：  
  - 👨💻 **Evan You**（Vue 和 Vite 创始人）  
  - 🛠️ **Matias Capeletto**（Vite 核心团队）  
  - 🔧 **Anthony Fu**（Vite/Vue/Nuxt 核心成员）  
  - 🚀 **Rich Harris**（Svelte 创始人）  
  - ⚡ **Ryan Carniato**（SolidJS 创始人）  
  - 及其他 Angular、Astro、Storybook 等生态的贡献者。  
- 🏟️ **场地亮点**：阿姆斯特丹剧院，配备巨幕、3D 音效及一流餐饮。  
- 🚇 **交通便利**：提供公共交通和停车指南。  
- 🤝 **合作机会**：欢迎赞助与社区合作。

---

### [JSON 模块脚本现已成为基线新功能  |  Blog  |  web.dev](https://web.dev/blog/json-imports-baseline-newly-available)

**原文标题**: [JSON module scripts are now Baseline Newly available  |  Blog  |  web.dev](https://web.dev/blog/json-imports-baseline-newly-available)

现代浏览器现已全面支持 JSON 模块脚本和导入属性，简化了 JSON 文件的导入流程。  

- 📜 以往在 JavaScript 模块中导入 JSON 文件需通过复杂方法（如嵌入 JSON 或使用 fetch()），现在所有现代浏览器已解决此问题。  
- 🛠️ 使用`import attributes`（如`with { type: "json" }`）可直接导入 JSON 文件，无需手动解析`JSON.parse()`。  
- 🌐 示例代码展示了如何导入 JSON 数据并直接使用其字段（如标题、描述、URL）更新 DOM 内容。  
- ⚠️ 必须声明 MIME 类型（如`Content-Type: text/json`），否则浏览器会默认请求 JavaScript 模块导致失败。  
- 📚 更多细节可参考 HTML 规范，代码示例遵循 Apache 2.0 许可证，内容遵循 Creative Commons 4.0 许可证。

---

### [Bun v1.2.16 | Bun 博客](https://bun.sh/blog/bun-v1.2.16)

**原文标题**: [Bun v1.2.16 | Bun Blog](https://bun.sh/blog/bun-v1.2.16)

Bun v1.2.16 版本修复了 73 个问题，增加了 119 个通过的 Node.js 测试，并引入了多项新功能和改进。

- 🛠️ 修复 73 个问题（处理 124 个👍）并增加 119 个 Node.js 测试通过。
- 🌐 新增 `Bun.serve` 通过 `routes` 直接返回文件功能。
- 🔗 在 `bunfig.toml` 中新增 `install.linkWorkspacePackages` 选项，控制工作区包链接行为。
- 🔍 `bun outdated` 支持目录依赖，便于检查 monorepo 中的更新。
- 🚀 新增 `Bun.hash.rapidhash` 支持，适用于非加密哈希需求。
- 🔌 大幅改进 `node:net` 模块，提升 Node.js 兼容性。
- 📦 新增 `vm.SyntheticModule` 支持，可在 VM 上下文中创建和评估合成模块。
- 🌍 新增 `HTTPParser` 绑定，使用 `llhttp` 库精确匹配 Node.js 行为。
- 🧹 修复多个内存泄漏问题，包括 N-API 句柄作用域和 `Bun.spawn` stdio。
- 🐛 修复运行时、JavaScript 解析器、CSS 解析器、FFI、TLS、HTTP/2 和 Windows 的多个问题。
- 📝 CLI 改进，包括帮助文本格式化和文档链接优化。
- 🏷️ 修复 TypeScript 类型，如 `RedisClient.prototype.del` 的参数问题。
- 🙏 感谢 25 位贡献者的贡献！

---

### [Astro 5.10 | Astro](https://astro.build/blog/astro-5100/)

**原文标题**: [Astro 5.10 | Astro](https://astro.build/blog/astro-5100/)

Astro 5.10 引入了多项新功能和改进，包括实验性的实时内容集合、稳定的响应式图片、CSP 改进以及自定义 Cloudflare Workers 入口点。

- 🚀 **实验性实时内容集合**：支持在运行时获取内容，适用于频繁变化或需要个性化的数据。  
- 🖼️ **响应式图片稳定版**：自动生成优化的 `srcset` 和 `sizes` 属性，提升页面加载性能。  
- 🔒 **CSP 改进**：支持生成 CSP 头部，提升安全性和性能，适配更多指令。  
- ☁️ **自定义 Cloudflare Workers 入口点**：支持自定义入口文件，便于使用 Durable Objects 等高级功能。  
- 🔄 **升级指南**：提供自动和手动升级方法，推荐使用 `@astrojs/upgrade` CLI 工具。  
- 🛠️ **错误处理和类型安全**：实时内容集合提供明确的错误处理和类型安全 API。  
- 📸 **图片布局和优先级控制**：新增 `layout` 和 `priority` 属性，优化关键图片加载。  
- 📜 **社区贡献**：感谢众多贡献者的代码和文档改进。

---

### [ESLint v9.29.0 发布 - ESLint - 可插拔的 JavaScript 代码检查工具](https://eslint.org/blog/2025/06/eslint-v9.29.0-released/)

**原文标题**: [ESLint v9.29.0 released - ESLint - Pluggable JavaScript Linter](https://eslint.org/blog/2025/06/eslint-v9.29.0-released/)

ESLint v9.29.0 是一个小版本升级，引入了新功能并修复了之前版本中的多个错误。

- 🆕 **ECMAScript 2026 显式资源管理支持**：默认解析器 `espree` 新增对 `using` 和 `await using` 声明的支持，需设置 `ecmaVersion: 2026` 或 `"latest"`。
- 🛠 **`no-restricted-properties` 新增 `allowProperties` 选项**：允许限制对象属性时排除特定属性（如 `settings` 和 `version`）。
- 💻 **核心规则支持 TypeScript 语法**：`no-restricted-globals` 忽略类型注解引用，`no-var` 允许全局类型声明中的 `var`。
- 🔍 **新增 `SourceCode#isGlobalReference(node)` 方法**：检查标识符是否为全局变量引用。
- 🌐 **新增 ECMAScript 2025 全局变量**：`Float16Array` 和 `Iterator` 在 `ecmaVersion: 2025` 或更高时自动启用。
- ✂ **`--prune-suppressions` CLI 选项优化**：移除不存在的文件的抑制条目。
- 🛠 **`includeIgnoreFile()` 支持自定义配置名称**：新增可选 `name` 参数。
- 🏗 **`class-methods-use-this` 支持类自动访问器**：兼容装饰器提案的语法（如 TypeScript）。
- 🐞 **多项错误修复**：包括显式匹配行为、类型修正和文档更新等。
- 📚 **文档与维护更新**：增强文档链接、修复拼写错误，升级依赖项并重构部分代码。

---

### [发布 v4.8.0 · honojs/hono · GitHub](https://github.com/honojs/hono/releases/tag/v4.8.0)

**原文标题**: [Release v4.8.0 · honojs/hono · GitHub](https://github.com/honojs/hono/releases/tag/v4.8.0)

Hono v4.8.0 版本发布，带来多项功能增强和新特性，包括路由助手、JWT 自定义头支持、JSX 流式非 ce 值支持等，同时代码体积进一步减小。

- 🚀 **代码体积减小** - `hono/tiny` 包体积减少约 800 字节，现仅约 11 KB（gzip 后 4.5 KB）。
- 🛣️ **路由助手** - 新增 `matchedRoutes`、`routePath` 等助手函数，简化路由信息获取。
- 🔐 **JWT 自定义头支持** - 支持从非标准头（如 `X-Auth-Token`）获取 JWT 令牌。
- 🛡️ **JSX 流式非 ce 支持** - 为 CSP 合规性，JSX 流式渲染支持添加 `scriptNonce`。
- 🌐 **CORS 动态方法控制** - 允许根据请求来源动态返回不同的 `allowedMethods`。
- 🔓 **JWK 匿名访问支持** - 新增 `allow_anon` 选项，允许未认证请求继续处理。
- 💾 **缓存状态码选项** - 可指定哪些状态码（如 200、404）应被缓存。
- 🔥 **Service Worker `fire()` 函数** - 新增独立 `fire()` 函数替代 `app.fire()`。
- 🧩 **SSG 插件系统** - 静态站点生成支持插件系统，可扩展生成过程（如生成 sitemap）。
- 📦 **第三方中间件更新** - 新增 MCP 中间件、UA 拦截中间件，并支持 Zod v4 验证器。
- 👏 **社区贡献** - 感谢多位新贡献者的代码提交和问题修复。

---

### [发布 v20.0.0 · facebook/relay · GitHub](https://github.com/facebook/relay/releases/tag/v20.0.0)

**原文标题**: [Release v20.0.0 · facebook/relay · GitHub](https://github.com/facebook/relay/releases/tag/v20.0.0)

Relay v20.0.0 版本发布，包含 ESLint 插件更新、文档改进、破坏性变更修复及多项功能优化。  

- 🚀 **ESLint 插件 v2.0.0 发布**：兼容性更新并移除部分过时规则。  
- 📚 **新增自动生成文档**：新增 Relay 编译器配置文档及 API 源码自动生成工具。  
- ⚠️ **破坏性变更**：弃用非模型弱类型返回，需迁移至强类型或弱对象。  
- � **Bug 修复**：修复嵌套`@defer`、清理操作、变量名等多项问题。  
- ✨ **功能改进**：增加时间日志、VSCode 任务支持、预取过期时间配置等。  
- 📝 **文档优化**：更新 GraphQL 文档、修复拼写错误、新增分页片段参数说明等。  
- 🧪 **实验性更新**：优化查询状态标记、支持标准化响应等。  
- 👏 **贡献者致谢**：多位开发者提交代码修复与改进。

---

### [发布 v5.4.0 · fastify/fastify · GitHub](https://github.com/fastify/fastify/releases/tag/v5.4.0)

**原文标题**: [Release v5.4.0 · fastify/fastify · GitHub](https://github.com/fastify/fastify/releases/tag/v5.4.0)

Fastify 项目发布了 v5.4.0 版本，包含多项更新和改进，涉及测试迁移、文档修正、性能优化和依赖项清理等。

- 🚀 发布了 Fastify v5.4.0 版本，包含 36 个提交更新  
- 🔧 多项测试从 tap 迁移，提升测试效率  
- 📝 文档更新，包括移除 fastify-sentry 插件和添加社区插件免责声明  
- 🛠️ 修复了类型定义和异步钩子问题  
- ⚡ 性能优化，特别是 reply.js 的改进  
- 🔄 清理和移除了多个依赖项，如 simple-get  
- 🌟 新增了对 Node.js v24 的支持  
- 🏗️ 改进了错误处理配置和路由选项冻结问题  
- 👏 感谢多位贡献者的努力和社区的反应

---

### [框架 | Neutralinojs](https://neutralino.js.org/docs/release-notes/framework/#v610)

**原文标题**: [Framework | Neutralinojs](https://neutralino.js.org/docs/release-notes/framework/#v610)

以下是按照您提供的模板总结的内容：

Neutralinojs 框架的多个版本更新，涵盖了 API 增强、核心功能改进、安全增强和错误修复。

- 🚀 **v6.1.0**: 新增 `window.setMainMenu` 函数，支持在 GNU/Linux、Windows 和 macOS 上动态更新原生菜单。macOS 支持快捷键注册，其他平台显示快捷键但不注册。
- 🌍 **v6.0.0**: 新增全局变量 `NL_LOCALE` 和 `NL_COMPDATA`，支持剪贴板 HTML 读写，改进 `os.execCommand` 和 `os.spawnProcess` 以支持环境变量设置，文件系统 API 新增权限管理和时间戳功能。
- 🔧 **v5.6.0**: 引入 `server` 命名空间，支持本地文件目录映射，替代 `file://` 协议。新增资源统计和窗口截图功能。
- 📦 **v5.5.0**: 支持通过 `window.injectGlobals` 和 `window.injectClientLibrary` 注入全局变量和客户端库，新增预加载脚本支持，配置选项支持设置数据和存储目录位置。
- 🖼️ **v5.4.0**: 新增资源模块 API，支持从资源包中读取文件。窗口 API 新增最小化和恢复功能，修复剪贴板图像写入问题。
- 🛠️ **v5.3.0**: Windows 支持窗口透明模式，新增文件和路径操作 API，修复 Unicode 字符处理问题。
- ⚙️ **v5.2.0**: 支持无配置文件启动，新增 SPA 路由支持，改进窗口显示行为。
- ✂️ **v5.1.0**: 支持窗口透明模式（除 Windows 外），新增剪贴板图像读写和清除功能。
- 🔒 **v5.0.0**: 增强安全性，要求有效的连接令牌，新增标准流读写 API，文件系统 API 支持递归操作，弃用部分函数。
- 📱 **v4.15.0**: 支持自定义用户代理字符串和配置文件，改进 DevOps 流程。
- 🐞 **v4.14.1**: 修复 DevOps 相关问题，更新编译环境。
- 👀 **v4.14.0**: 新增文件系统观察器 API，支持设置子进程工作目录，修复 Unicode 字符问题。
- 💾 **v4.13.0**: 支持持久化窗口状态，修复 Windows 窗口问题。
- 🖥️ **v4.12.0**: 新增窗口居中功能，支持设置初始窗口位置，静态链接 WebView2 加载器。
- 📂 **v4.11.0**: 引入文件观察器 API，修复 Windows 窗口闪烁问题，支持系统主题。
- 🏗️ **v4.10.0**: 支持 macOS arm64 和通用二进制，新增 JSON 模式定义，修复编译问题。
- 🛠️ **v4.9.0**: 支持自定义方法 API 和文件流 API，改进异步文件操作。
- 🌐 **v4.8.0**: 新增 `os.getEnvs` 和 `storage.getKeys` API，支持文件读取位置和大小设置，新增鼠标位置获取功能。
- 💻 **v4.7.0**: 新增系统信息 API，支持设置对话框默认路径，改进测试流程。
- 🔄 **v4.6.0**: 引入进程生成 API，支持长时间运行进程，新增文件系统时间戳功能。
- 👁️ **v4.5.0**: 新增窗口焦点和失去焦点事件，支持夜间构建，修复托盘图标问题。
- 📝 **v4.4.0**: 新增窗口位置获取和文件追加功能，更新依赖项。
- 🔐 **v4.3.0**: 增强令牌安全性，新增窗口置顶和大小获取功能，修复文件对话框顺序问题。
- 📋 **v4.2.0**: 新增剪贴板 API，支持 Chrome 相关 CLI 参数，修复路径问题。
- 🌐 **v4.1.0**: 支持 Chrome 模式，新增窗口标题获取功能，改进环境变量处理。
- 🔌 **v4.0.0**: 引入扩展 API，支持静态服务器文档根设置，新增更新检查功能，修复端口和日志文件问题。

---

### [发布版本 v1.10.0 · axios/axios · GitHub](https://github.com/axios/axios/releases/tag/v1.10.0)

**原文标题**: [Release Release v1.10.0 · axios/axios · GitHub](https://github.com/axios/axios/releases/tag/v1.10.0)

axios GitHub 仓库的 v1.10.0 版本发布信息  

- 🐛 **Bug 修复**  
  - 修复了`adapter`中未传递`fetchOptions`到 fetch 函数的问题 (#6883)  
  - 在`form-data`中将布尔值转换为字符串 (#6917)  
  - 为 React Native 添加模块入口点 (#6933)  

- ✨ **新特性**  
  - 改进了`fetchOptions`的类型定义接口 (#6867)  

- 👥 **贡献者**  
  - 包括 Dmitriy Mozgovoy、Noritaka Kobayashi 等 8 位开发者  

- 🎯 **发布详情**  
  - 版本号：v1.10.0  
  - 发布日期：2024 年 6 月 14 日  
  - 提交哈希：73a836d（GitHub 签名验证）  

- ❗ **加载问题提示**  
  - 页面部分内容加载失败需手动刷新  

- 🚀 **社区反响**  
  - 获 20 次👍、4 次🎉、3 次🚀等表情互动

---

### [奥利弗·梅德赫斯特 - JavaScript 的预编译技术 - YouTube](https://www.youtube.com/watch?v=RU5N5O-O5Zw)

**原文标题**: [Oliver Medhurst - Compiling JavaScript ahead-of-time - YouTube](https://www.youtube.com/watch?v=RU5N5O-O5Zw)

该内容为 YouTube 网站的页脚导航链接，包含关于平台、法律条款、开发者信息及公司版权的各类条目。

- 📢 关于 - 提供 YouTube 平台的基本信息  
- 📰 新闻 - 链接至媒体与新闻相关内容  
- ©️ 版权 - 版权声明及法律信息  
- 📩 联系我们 - 用户与平台沟通渠道  
- 🎨 创作者 - 面向内容创作者的相关资源  
- 💼 广告 - 广告合作与商业推广信息  
- 🔧 开发者 - 开发者工具和技术支持  
- 📜 条款 - 平台使用条款与条件  
- 🔒 隐私 - 隐私政策与数据保护措施  
- ⚖️ 政策与安全 - 社区准则与安全政策  
- 🔍 YouTube 运作机制 - 平台功能原理解释  
- 🧪 测试新功能 - 实验性功能试用信息  
- 🏢 谷歌公司 - 版权归属及公司信息（2025 年）

---

### [紫红](https://porffor.dev/)

**原文标题**: [Porffor](https://porffor.dev/)

Porffor 是一款将 JavaScript 提前编译为 WebAssembly 和原生二进制文件的工具，目前处于预发布阶段，预计 2025 年可用。它通过直接编译而非打包解释器，显著提升了性能和体积效率，同时支持安全沙箱执行和原生应用开发。

- 🚀 **高效编译**：Porffor 将 JS 编译为 Wasm 或原生代码，体积缩小 10-30 倍（Wasm）甚至 1000 倍（原生）。
- 🔒 **安全执行**：支持沙箱化运行，适合服务器端和边缘计算场景，兼顾安全与性能。
- 🛡️ **反逆向增强**：编译后的代码比混淆更难逆向，保护敏感逻辑。
- 📦 **原生应用支持**：JS 可编译为微小原生二进制（<100KB），适用于嵌入式设备、CLI 工具等。
- ⚙️ **底层优化**：从零设计的 AOT 编译器，实现传统 JIT/解释器无法做到的静态优化。
- 🌐 **TypeScript 原生支持**：直接编译 TS 文件，无需额外转译步骤。
- ⚠️ **局限性**：不支持运行时动态代码（如 eval），且早期版本可能存在稳定性问题。
- ✅ **标准兼容**：通过 Test262 测试套件验证 ECMAScript 合规性。
- 🎮 **体验方式**：提供在线 Playground 或通过 npm 安装本地试用（`npm i -g porffor@latest && porf`）。

---

### [在 ES 模块的顶层使用 await - Matt Smith](https://allthingssmitty.com/2025/06/16/using-await-at-the-top-level-in-es-modules/)

**原文标题**: [
    Using await at the top level in ES modules - Matt Smith
  ](https://allthingssmitty.com/2025/06/16/using-await-at-the-top-level-in-es-modules/)

ES2022 引入了顶层 await，允许在 ES 模块的顶层直接使用 await 关键字，简化异步代码编写，但需注意模块执行顺序和循环依赖问题。

- 🚀 **顶层 await 的引入**：ES2022 允许在 ES 模块顶层使用 await，无需包裹在 async 函数中，简化异步代码结构。  
- 🚫 **传统限制**：此前 await 只能在 async 函数内使用，否则会报语法错误。  
- 📦 **模块限制**：仅适用于 ES 模块（.mjs 或 type="module"的.js 文件），不支持 CommonJS 或传统<script>标签。  
- 🔄 **循环依赖风险**：顶层 await 可能导致模块间循环依赖时运行时错误。  
- ⏳ **执行暂停**：导入含顶层 await 的模块会等待其执行完成，可能引发隐藏的加载顺序依赖。  
- 🌐 **浏览器与 Node 支持**：现代浏览器和 Node.js v16+ 均支持，需注意配置（如 MIME 类型、HTTPS 环境）。  
- ⚠️ **使用场景建议**：适合远程配置获取、动态导入等，但避免在公共库或计算密集型逻辑中使用。  
- 🔧 **备选方案**：WebAssembly 等需 await 初始化的场景可直接使用，但需确保正确 MIME 类型。  
- 💡 **最佳实践**：在独立应用中使用可提升代码清晰度，但共享模块中慎用以防阻塞下游。

---

### [OAuth 提供商改进](https://clerk.com/changelog/2025-06-13-oauth-improvements?utm_source=cooper-press&utm_medium=newsletter&utm_campaign=oauth&utm_content=06-20-25&dub_id=OWgUjDEayJYCI0fr)

**原文标题**: [OAuth Provider Improvements](https://clerk.com/changelog/2025-06-13-oauth-improvements?utm_source=cooper-press&utm_medium=newsletter&utm_campaign=oauth&utm_content=06-20-25&dub_id=OWgUjDEayJYCI0fr)

Clerk 宣布对其 OAuth 功能进行了重大扩展，新增多项特性以支持更广泛的应用场景，包括 MCP 服务的实现。

- 🔒 OAuth 令牌现在可以通过 Clerk 的 SDK 进行验证和即时撤销。
- 📜 支持开箱即用的授权服务器元数据。
- 🖥️ OAuth 授权流程新增了同意屏幕，确保用户在完成流程前了解并同意所授予的访问权限。
- 🌐 改进了 CORS 处理，使得在浏览器中完成令牌交换的公共客户端实现成为可能。
- 🔄 支持 OAuth 客户端的动态客户端注册。
- 🤖 Clerk 的 OAuth 实现满足使用 Clerk 作为授权服务实现 MCP 服务的所有要求。
- 📚 提供了详细的指南和文档，帮助开发者快速上手新功能。
- 🛠️ 目前大多数 SDK 已支持 OAuth 令牌验证，部分 SDK 支持即将推出。
- 🔍 新增的 OAuth 同意屏幕显示请求应用的名称、徽标、请求的具体范围以及明确的接受/拒绝选项。
- ⚙️ 动态客户端注册允许通过 API 编程方式创建 OAuth 客户端。
- 🚀 Clerk 的 OAuth 功能现已成为功能完备的 OAuth 服务器实现，支持 OAuth 范围访问。
- 🔜 自定义范围的支持即将推出，开发者可以通过路线图提供反馈。

---

### [OAuth 提供商改进](https://clerk.com/changelog/2025-06-13-oauth-improvements?utm_source=cooper-press&utm_medium=newsletter&utm_campaign=oauth&utm_content=06-20-25&dub_id=OWgUjDEayJYCI0fr)

**原文标题**: [OAuth Provider Improvements](https://clerk.com/changelog/2025-06-13-oauth-improvements?utm_source=cooper-press&utm_medium=newsletter&utm_campaign=oauth&utm_content=06-20-25&dub_id=OWgUjDEayJYCI0fr)

Clerk 宣布对其 OAuth 功能进行了重大扩展，新增多项特性以支持更广泛的应用场景，包括 MCP 服务的实现。

- 🔄 OAuth 令牌现在可以通过 Clerk 的 SDK 进行验证和即时撤销。
- 📜 支持授权服务器元数据，开箱即用。
- 🖥 OAuth 授权流程新增了同意屏幕，确保用户在完成流程前了解并同意所授予的访问权限。
- 🌐 改进了 CORS 处理，使得在浏览器中完成令牌交换的公共客户端实现成为可能。
- 🔄 支持 OAuth 客户端的动态客户端注册。
- 🛠 Clerk 的 OAuth 实现满足使用 Clerk 作为授权服务实现 MCP 服务的所有要求。
- 📚 提供了详细的 OAuth 指南和实现示例，帮助开发者快速上手。
- 🛡 新增的 OAuth 同意屏幕增强了安全性，防止恶意应用无声获取用户账户访问权限。
- 🚀 动态客户端注册功能允许通过 API 编程方式创建 OAuth 客户端。
- 🔜 自定义 OAuth 范围的支持即将推出，目前正在收集用户反馈以优化功能。
- 📅 对于即将支持的 SDK，开发者可以直接使用 Clerk 的 REST API 进行 OAuth 令牌验证。

---

### [JavaScript 破坏了网络（还称之为进步）——乔诺·奥尔德森](https://www.jonoalderson.com/conjecture/javascript-broke-the-web-and-called-it-progress/)

**原文标题**: [JavaScript broke the web (and called it progress) - Jono Alderson](https://www.jonoalderson.com/conjecture/javascript-broke-the-web-and-called-it-progress/)

现代网页开发过度依赖 JavaScript，导致网站臃肿、性能低下且难以维护。开发者追求技术复杂性，忽视了用户体验和基本网页标准。

- 🐌 现代网站普遍臃肿、加载缓慢且不稳定，用户体验差。
- 🔄 开发者过度使用 JavaScript 框架，将简单问题复杂化。
- 📱 为追求“类应用体验”，牺牲了网页的快速加载和易用性。
- 🏗️ 技术栈日益复杂，需要多个工程师和工具来完成简单任务。
- 🔍 SEO 和可访问性因过度依赖 JavaScript 而受损。
- 💡 大多数网站只需简单 HTML、CSS 和少量 JavaScript 即可满足需求。
- 🛠️ 开发者体验 (DX) 优先于用户体验 (UX)，导致过度抽象。
- 🔄 行业陷入不断迭代工具的循环，而非解决实际问题。
- 💰 复杂性增加了开发和维护成本，降低了业务敏捷性。
- 🌐 呼吁回归网页本质：服务器渲染、语义化标记和适度使用 JavaScript。

---

### [TypeScript 如何解决其全局`Iterator`命名冲突问题](https://2ality.com/2025/06/typescript-iterator-types.html)

**原文标题**: [How TypeScript solved its global `Iterator` name clash](https://2ality.com/2025/06/typescript-iterator-types.html)

TypeScript 通过引入新的类型`IteratorObject`来解决与 ECMAScript 2025 中新增的全局类`Iterator`的命名冲突，同时保持旧代码的兼容性。

- 🔄 TypeScript 通过将内置迭代器的类型从`IterableIterator`改为`IteratorObject`来避免与新的全局类`Iterator`冲突。
- 🛠️ 新的`IteratorObject`类型包含了迭代器辅助方法，如`.map()`和`.filter()`，这些方法支持增量处理且无需创建中间数组。
- 📜 TypeScript 通过内部类`Iterator`和类型合并技术，确保全局类`Iterator`的实例类型为`IteratorObject`，而非冲突的`Iterator`类型。
- 🔗 所有内置迭代器（如数组、Map、Set 的迭代器）现在都继承自`Iterator.prototype`，并具有新的辅助方法。
- 📖 开发者可以继续使用`Iterable`类型表示可迭代对象，而新代码建议使用`IteratorObject`类型以获得辅助方法支持。

---

### [获取失败](https://javascriptweekly.com/link/170754/web)

**原文标题**: [Failed to retrieve](https://javascriptweekly.com/link/170754/web)

无法总结：获取内容失败，状态码 530。

---

### [使用 Three.js、GSAP 和 Web Audio API 编写 3D 音频可视化工具 | Codrops](https://tympanus.net/codrops/2025/06/18/coding-a-3d-audio-visualizer-with-three-js-gsap-web-audio-api/)

**原文标题**: [Coding a 3D Audio Visualizer with Three.js, GSAP & Web Audio API | Codrops](https://tympanus.net/codrops/2025/06/18/coding-a-3d-audio-visualizer-with-three-js-gsap-web-audio-api/)

使用 Three.js、GSAP 和 Web Audio API 创建 3D 音频可视化效果，展示了一个音乐驱动的视觉化场景，其中发光的 3D 球体随着节拍脉动和尖刺，而 GSAP 可拖动的面板在其周围平滑漂移。

- 🎵 项目结合了 Three.js、GSAP 和 Web Audio API，创建了一个音乐驱动的 3D 音频可视化效果。
- 🖥️ 使用 Three.js 设置场景，包括相机、渲染器和轨道控制器，创建了一个动态的球体对象。
- 🔊 通过 Web Audio API 分析音频数据，实时获取频率数据，驱动 3D 球体的动画效果。
- 🌀 使用 GLSL 着色器实现顶点扭曲和菲涅耳发光效果，使球体随音乐脉动和变形。
- 🎨 通过 GSAP 实现平滑的动画和交互，包括可拖动的 UI 面板和惯性效果。
- 🚀 项目还包括一个科幻风格的 UI 界面，带有控制面板和终端输出，增强了沉浸感。
- 🌌 最终效果是一个交互式艺术装置，用户可以上传音频或选择预设曲目，实时体验音乐与视觉的结合。

---

### [将 React 的<ViewTransition>引入原生 JS](https://plainvanillaweb.com/blog/articles/2025-06-12-view-transitions/)

**原文标题**: [Bringing React's <ViewTransition> to vanilla JS](https://plainvanillaweb.com/blog/articles/2025-06-12-view-transitions/)

overview summary  
本文作者表达了对 React 的喜爱，但也指出其过度设计的倾向，提倡探索更简单、更原生的解决方案。文章以视图过渡（View Transitions）为例，详细介绍了其基本原理、浏览器兼容性问题及实际应用中的挑战，并对比了 React 的解决方案与原生实现的优劣。最后，作者通过一个 GitHub 示例展示了如何用原生代码实现类似 React 的视图过渡效果，并提及了 Shadow DOM 的相关问题。

- 🚀 React 是现代 Web 开发的默认选择，但有时过度设计，原生解决方案可能更简单高效。  
- 🌈 视图过渡（View Transitions）允许浏览器在页面状态变化时平滑动画，但兼容性有限（仅 Chrome、Edge、Safari 支持）。  
- 📸 通过`document.startViewTransition()`，浏览器会捕获页面快照并自动生成过渡动画，支持独立元素过渡控制。  
- ⚠️ 实际应用中存在诸多问题：Firefox 不支持、命名冲突、过渡中断、用户输入阻塞等。  
- 🧙 React 通过`<ViewTransition>`组件和`startTransition()`封装了复杂逻辑，但实现晦涩难调试。  
- 🔄 原生解决方案可通过队列和批处理优化过渡调用，避免中断和性能问题。  
- 💡 作者在 GitHub 上提供了原生实现的完整示例，代码简洁且功能强大。  
- 👻 Shadow DOM 中元素过渡需特殊处理（如暴露为 DOM Parts），增加了复杂性。  
- 🛠️ 文章倡导通过原生实现探索更简单的方案，同时揭示了框架与原生平台的权衡。

---

### [<syntax-highlight>元素 - Web 组件](https://andreruffert.github.io/syntax-highlight-element/)

**原文标题**: [<syntax-highlight> element - Web Component](https://andreruffert.github.io/syntax-highlight-element/)

这是一个关于使用 CSS Custom Highlight API 实现语法高亮的自定义元素组件的介绍。  

- 📦 **安装** - 可通过 npm 安装：`npm install syntax-highlight-element`，或通过 CDN 引入。  
- 🛠️ **使用** - 支持 ES 模块导入或直接通过 HTML 标签`<syntax-highlight>`使用，需指定语言属性（如`language="js"`）。  
- 🎨 **主题** - 需加载主题 CSS 文件，例如`prettylights.css`，支持自定义主题或贡献新主题。  
- 🌐 **语言支持** - 默认支持`html`、`css`、`js`，可配置更多语言（基于 Prism 的语法标记器）。  
- ⚙️ **配置** - 通过全局`window.she.config`对象可扩展语言和语法标记类型。  
- 🙏 **致谢** - 灵感来自 Bramus Van Damme 的博客，并使用了 Prism 的语法标记器。

---

### [CSS 自定义高亮 API - Web API | MDN](https://developer.mozilla.org/en-US/docs/Web/API/CSS_Custom_Highlight_API)

**原文标题**: [CSS Custom Highlight API - Web APIs | MDN](https://developer.mozilla.org/en-US/docs/Web/API/CSS_Custom_Highlight_API)

CSS Custom Highlight API 允许通过 JavaScript 创建文本范围并使用 CSS 为其添加样式，适用于文本编辑器和代码编辑器等场景。

- 🌟 **功能概述**：通过 JavaScript 创建 Range 对象，CSS 自定义样式，不影响 DOM 结构。  
- 🛠️ **使用步骤**：  
  - 1️⃣ 创建`Range`对象定义文本范围。  
  - 2️⃣ 实例化`Highlight`对象关联多个范围。  
  - 3️⃣ 通过`HighlightRegistry`注册高亮（如`CSS.highlights.set("name", highlight)`）。  
  - 4️⃣ 用`::highlight()`伪元素设置样式（如背景色）。  
- 📚 **核心接口**：  
  - `Highlight`：管理需高亮的范围集合。  
  - `HighlightRegistry`：通过`CSS.highlights`注册/删除高亮。  
- 🔍 **示例场景**：搜索关键词高亮，监听输入事件动态匹配文本并标记。  
- ⚙️ **兼容性**：需检查浏览器支持（如`CSS.highlights`是否存在）。  
- 🔗 **扩展阅读**：与`::selection`等伪元素对比，支持更灵活的自定义范围。  

代码示例：  
- **JavaScript**：创建 Range、Highlight 并注册。  
- **CSS**：`::highlight(search-results) { background-color: #f06; }`。

---

### [Highlight API：has | Can I use... 对 HTML5、CSS3 等的支持表格](https://caniuse.com/mdn-api_highlight_has)

**原文标题**: [Highlight API: has | Can I use... Support tables for HTML5, CSS3, etc](https://caniuse.com/mdn-api_highlight_has)

Highlight API 的全球使用率为 88.74%，不同浏览器和版本对其支持情况各异。

- 🌍 全球使用率：88.74%  
- 🚫 IE：6-11 版本均不支持  
- ✅ Edge：105-137 版本支持  
- 🚫 Firefox：2-139 版本不支持，140-142 版本支持  
- ✅ Chrome：105-140 版本支持  
- ✅ Safari：17.2-18.5 及 26.0-TP 版本支持  
- ✅ Opera：91-117 版本支持  
- ✅ Safari iOS：17.2-18.5 及 26.0 版本支持  
- ❓ Opera Mini：支持情况未知  
- ✅ Android Browser：137 版本支持  
- ✅ Opera Mobile：80 版本支持  
- ✅ Chrome Android：137 版本支持  
- 🚫 Firefox Android：139 版本不支持  
- ❓ UC/QQ/Baidu/KaiOS浏览器：支持情况未知  
- ✅ Samsung Internet：20-28 版本支持

---

### [GitHub - andreruffert/syntax-highlight-element: 👓 使用 CSS 自定义高亮 API 实现语法高亮](https://github.com/andreruffert/syntax-highlight-element)

**原文标题**: [GitHub - andreruffert/syntax-highlight-element: 👓 Syntax Highlighting using the CSS Custom Highlight API](https://github.com/andreruffert/syntax-highlight-element)

一个基于 CSS Custom Highlight API 实现的语法高亮 Web 组件，支持通过 Prism 分词器实现无 span 包裹的代码高亮效果。

- 👓 项目名称：`syntax-highlight-element`  
- 🌐 功能特点：利用 CSS Custom Highlight API 实现无 DOM 污染的语法高亮  
- 📦 安装方式：支持 npm 安装或 CDN 直接引入  
- 🛠️ 使用示例：通过`<syntax-highlight language="js">`标签快速使用  
- 🎨 主题支持：内置有限主题，支持自定义主题开发  
- ⚙️ 配置选项：可自定义语言支持范围（默认支持 html/css/js）  
- 🌍 浏览器兼容：依赖 CSS Custom Highlight API  
- 📜 开源协议：MIT License  
- ✨ 核心依赖：Prism 分词器 + Bramus Van Damme 的 API 灵感  
- 📊 项目数据：158 Stars / 1 Fork / 2 Contributors  
- 🔧 开发状态：最新版本 v1.1.0（2025 年 4 月发布）

---

### [React Native 0.80 - React 19.1 版本更新、JS API 变更、冻结旧架构及其他重要内容 · React Native](https://reactnative.dev/blog/2025/06/12/react-native-0.80)

**原文标题**: [React Native 0.80 - React 19.1, JS API Changes, Freezing Legacy Arch and much more · React Native](https://reactnative.dev/blog/2025/06/12/react-native-0.80)

React Native 0.80 发布，包含 React 19.1 支持、JavaScript API 改进、旧架构冻结等多项重要更新。

- 🚀 **React 19.1.0 支持**：React Native 0.80 内置最新稳定版 React 19.1.0，包含错误堆栈等新特性。  
- ⚠️ **JavaScript 深层导入弃用**：深层导入将触发警告，未来版本将移除，建议改用根导入。  
- 📌 **旧架构冻结**：不再为旧架构开发新功能或修复，未来将完全弃用，新增警告提示不兼容 API。  
- 🛠️ **严格 TypeScript API（实验性）**：提供更精准的类型定义，未来将成为默认 API。  
- ⚡ **iOS 依赖预构建（实验性）**：预构建第三方依赖，减少首次构建时间约 12%。  
- 📉 **Android APK 体积优化**：启用过程间优化（IPO），APK 体积减少约 1MB。  
- 🎨 **新应用屏幕重设计**：社区模板的新应用界面更简洁，适配大屏幕。  
- ❗ **JSC 社区支持**：0.80 是最后一个官方支持 JSC 的版本，后续由社区维护。  
- 🔧 **其他破坏性变更**：包括 `exports` 字段引入、Kotlin 版本升级、部分类迁移等。  
- 🙏 **致谢**：感谢 127 位贡献者的 1167 次提交，特别提及关键贡献者。  
- 🔄 **升级指南**：建议使用 React Native Upgrade Helper 进行升级，新项目可直接创建。

---

### [React 数据网格 - 文档 | Handsontable](https://handsontable.com/docs/react-data-grid/?utm_source=jsweekly&utm_medium=referral&utm_campaign=jsw20.06.25)

**原文标题**: [React Data Grid - Documentation | Handsontable](https://handsontable.com/docs/react-data-grid/?utm_source=jsweekly&utm_medium=referral&utm_campaign=jsw20.06.25)

Handsontable 是一个流行的 JavaScript 数据网格组件，可将电子表格的外观和功能集成到应用程序中，支持多种数据源和框架。

- 🚀 **快速入门**：支持 JavaScript、TypeScript 及主流框架（React、Angular、Vue 等），提供从安装到创建数据网格的指南。  
- 🌐 **SSR 示例**：兼容 Next.js、Astro、Remix 和 Nuxt 等服务器端渲染框架。  
- 💡 **应用场景**：适用于财务、医疗、游戏开发等行业，支持数据导入、编辑及定制化表格界面。  
- 📊 **软件类型**：适合库存管理、ERP 系统、数据建模等数据密集型应用。  
- 👥 **社区支持**：可通过 GitHub Discussions、开发者论坛等渠道交流与反馈。  
- 🔧 **技术支持**：提供专业支持服务，需有效订阅计划。  
- 🔔 **更新动态**：通过博客、社交媒体等渠道获取最新版本信息和行业动态。

---

### [React 可搜索下拉框](https://react-searchable-dropdown.netlify.app/)

**原文标题**: [ReactSearchable Dropdown](https://react-searchable-dropdown.netlify.app/)

好的，请提供需要总结的文本内容，我会按照您要求的模板生成概述和带表情符号的要点列表。  

示例模板：  

概述总结  
- 🌟 要点一  
- 📌 要点二  
- 🔍 要点三  

请提供具体文本，我会为您生成符合要求的中文总结。

---

### [GitHub - luciodale/react-searchable-dropdown: 支持单选多选、虚拟滚动、新增选项、搜索等功能](https://github.com/luciodale/react-searchable-dropdown)

**原文标题**: [GitHub - luciodale/react-searchable-dropdown: single and multi selection, virtualized, new option creation, search, and more](https://github.com/luciodale/react-searchable-dropdown)

一个现代化的、可访问且可定制的 React 下拉选择组件库，支持单/多选、虚拟滚动、动态创建选项和实时搜索等功能。

- 🌟 **功能丰富** - 提供实时搜索、键盘导航、虚拟滚动、动态创建选项等特性  
- 🎨 **高度可定制** - 支持自定义样式、图标、分组选项及多种搜索过滤模式  
- 🚀 **高性能** - 采用虚拟化列表技术优化大型数据渲染  
- ♿ **无障碍支持** - 遵循可访问性设计规范  
- 📦 **易用集成** - 支持字符串数组和对象数组两种数据类型，开箱即用  
- ⚙️ **灵活配置** - 可控制定位策略（absolute/fixed）、搜索键定义、防抖延迟等  
- 🔧 **多场景适配** - 单选框（SearchableDropdown）和多选框（SearchableDropdownMulti）独立组件  
- 📚 **完善文档** - 提供清晰的 API 说明和类型定义（MIT 协议开源）

---

### [GitHub - gnh1201/welsonjs: WelsonJS - 基于 Windows 内置 JavaScript 引擎构建应用](https://github.com/gnh1201/welsonjs)

**原文标题**: [GitHub - gnh1201/welsonjs: WelsonJS - Build a Windows app on the Windows built-in JavaScript engine](https://github.com/gnh1201/welsonjs)

WelsonJS 是一个基于 Windows 内置 JavaScript 引擎的框架，用于构建 Windows 桌面应用程序，支持多种脚本语言和工具集成。

- 🚀 **项目简介**: WelsonJS 允许开发者使用 JavaScript、TypeScript、CoffeeScript 等语言在 Windows 内置 ECMAScript 引擎上构建桌面应用。
- 📜 **许可证**: 默认使用 GPL 3.0 许可证，若与微软产品不兼容则采用 MS-RL 许可证。
- ⭐ **项目数据**: 324 个星标，18 个复刻，72 个问题。
- 🛠️ **主要特性**: 轻量高效、Windows ECMAScript 兼容、独立运行、安全导向、极简设计。
- 💡 **使用场景**: 旧系统集成、自动化脚本、嵌入式应用、安全敏感环境、办公自动化。
- 📦 **内置工具**: 支持多种转译器（TypeScript、Rescript 等）、代码编辑器（Monaco Editor）、网络工具、AI 集成（如 ChatGPT）。
- 🏗️ **快速开始**: 提供简单的代码示例展示如何创建和运行脚本。
- 📤 **发布方式**: 支持压缩为 Zip 文件、构建安装包或直接复制文件目录。
- 🌟 **社区与支持**: 提供多种社区交流渠道，包括 Discord、Microsoft Teams 等，并支持付费咨询。
- 🤝 **贡献与赞助**: 欢迎协作与赞助，特别鸣谢多位贡献者和赞助商。

---

### [GitHub - httptoolkit/mockrtc：强大友好的WebRTC模拟对等端与代理](https://github.com/httptoolkit/mockrtc)

**原文标题**: [GitHub - httptoolkit/mockrtc: Powerful friendly WebRTC mock peer & proxy](https://github.com/httptoolkit/mockrtc)

MockRTC 是一个强大的 WebRTC 模拟对等体和代理工具，用于拦截、断言和模拟 WebRTC 对等体，适用于自动化测试、错误模拟和流量调试。

- 🚀 **功能概述**  
  - 支持自动化测试 WebRTC 流量  
  - 可模拟 WebRTC 错误，实现可靠复现  
  - 捕获和检查真实 WebRTC 对等体间的流量以进行调试  
  - 创建代理对等体以自动化消息转换、监控或日志记录  

- 📦 **安装与设置**  
  - 通过 `npm install --save-dev mockrtc` 安装  
  - 支持在浏览器和 Node.js 环境中使用  
  - 需要启动一个 MockRTC 管理服务器（Node.js）和客户端（浏览器）  

- 🛠 **使用示例**  
  - 创建模拟对等体并定义行为步骤  
  - 支持生成 WebRTC offer 或 answer 进行连接  
  - 提供 `hookWebRTCConnection` 和 `hookAllWebRTC` 方法自动代理流量  

- 🔄 **代理功能**  
  - 可作为中间人代理记录或修改流量  
  - 使用 `thenPassThrough` 方法实现透明代理  

- 📚 **文档与资源**  
  - 详细参考文档和测试套件提供多种示例  
  - 支持通过 GitHub 提交问题或功能请求  

- 🌍 **项目背景**  
  - 由欧盟 Horizon 2020 研究计划资助  
  - 采用 Apache-2.0 许可证开源

---

### [GitHub - asmyshlyaev177/state-in-url：将任意用户状态存储于查询参数中；想象一下浏览器URL中的JSON，同时保留数据的类型与结构，例如数字会被解码为数字而非字符串。支持TypeScript验证。共享状态与URL状态同步，无需繁琐代码或样板文件。兼容Next.js@14-15、react-router@6-7及Remix@2。](https://github.com/asmyshlyaev177/state-in-url)

**原文标题**: [GitHub - asmyshlyaev177/state-in-url: Store any user state in query parameters; imagine JSON in a browser URL, while keeping types and structure of data, e.g.numbers will be decoded as numbers not strings. With TS validation. Shared state and URL state sync without any hassle or boilerplate. Supports Next.js@14-15, react-router@6-7, and Remix@2.](https://github.com/asmyshlyaev177/state-in-url)

state-in-url 是一个用于在 URL 查询参数中存储用户状态的库，支持复杂数据类型（如对象、数组、日期等），并保持类型安全。它提供了与 React 状态钩子相似的 API，适用于 Next.js、React-Router 和 Remix 等框架。

- 🌐 **核心功能**：将 JSON 数据存储在 URL 中，保留类型和结构（如数字解码为数字而非字符串）。
- 🛠️ **框架支持**：兼容 Next.js 14-15、React-Router 6-7 和 Remix 2。
- ⚡ **高效性能**：编码/解码速度快（约 1ms），库体积小（<2KB），零依赖。
- 🔒 **类型安全**：通过 TypeScript 实现静态验证和自动补全。
- 🔄 **状态同步**：支持深链接（URL 状态同步），组件间状态自动同步。
- 📂 **多种用途**：存储未保存的表单、页面过滤器，或在组件间共享状态。
- 📚 **丰富文档**：提供详细文档、JSDoc 注释和示例代码。
- 🧪 **全面测试**：包含单元测试和 Playwright 测试（支持 Chrome/Firefox/Safari）。
- 📜 **MIT 许可**：宽松的开源许可证。

---

### [LogTape 0.12.0 版本发布说明](https://hackers.pub/@hongminhee/2025/logtape-0-12)

**原文标题**: [LogTape 0.12.0 Release Notes](https://hackers.pub/@hongminhee/2025/logtape-0-12)

LogTape 0.12.0 是一个无依赖的 JavaScript 和 TypeScript 日志库，支持多种 JavaScript 运行时，提供分层类别、结构化日志记录，并适用于应用程序和库的无缝集成。

- 🔍 **Trace 日志级别**：新增 `trace` 级别，位于 `debug` 之下，提供更细粒度的日志控制。
- 🚀 **增强文件接收器性能**：新增 `bufferSize` 和 `flushInterval` 选项，优化高吞吐量场景下的写入性能。
- 📡 **Syslog 支持**：新增 `@logtape/syslog` 包，支持通过 RFC 5424 格式发送日志到 syslog 服务器。
- 🔄 **Logger 方法别名**：新增 `Logger.warning()` 作为 `Logger.warn()` 的别名，确保与 `LogLevel` 类型定义一致。
- 📦 **统一包发布**：所有 LogTape 包（如 `@logtape/otel`、`@logtape/sentry` 和 `@logtape/syslog`）现在共享相同的版本号，简化版本管理。
- 🛠️ **改进构建基础设施**：从 `dnt` 迁移到 `tsdown`，优化了构建过程，提高了兼容性和性能。
- 📝 **迁移指南**：提供了更新到 `trace` 级别和利用缓冲区配置的指南。
- 📥 **安装方式**：支持通过 JSR 和 npm 安装，适用于 Deno、Node.js、Bun 等多种运行时。
- 🙏 **致谢**：感谢所有贡献者，包括报告问题、提交拉取请求和提供反馈的人。

---

### [GitHub - ant-design/ant-design-charts: 📈 基于 @antvis 的 React 图表库，包含统计图表、关系图及地图](https://github.com/ant-design/ant-design-charts)

**原文标题**: [GitHub - ant-design/ant-design-charts: 📈 A React Chart Library based on @antvis, include plot, graph, and map.](https://github.com/ant-design/ant-design-charts)

Ant Design Charts 是一个基于 React 的图表库，集成了多种图表类型，包括统计图表、关系图和地图等，基于 AntV 技术栈开发。

- 📈 **功能特点**：支持多种图表类型（基于 G2/G6/X6/L7），易于使用，轻量且美观，响应式设计，支持 TypeScript。  
- 🛠️ **安装使用**：通过 npm 安装 `@ant-design/charts`，提供简洁的 API 快速集成到 React 项目。  
- 🌟 **开发贡献**：开源项目（MIT 协议），欢迎通过 GitHub Issues 提交贡献，提供钉钉群（44788198）交流支持。  
- 📊 **项目状态**：2.1k Stars，410 Forks，14k+ 项目使用，活跃维护中（最新版本 2.4.0）。  
- 🔍 **技术支持**：官网提供文档、示例和常见问题解答，开发者可本地克隆调试（pnpm 管理依赖）。

---

### [所有图表 | Ant Design Charts 可视化组件库](https://ant-design-charts.antgroup.com/examples)

**原文标题**: [所有图表 | Ant Design Charts 可视化组件库](https://ant-design-charts.antgroup.com/examples)

overview summary  
本文详细介绍了多种数据可视化图表类型及其交互功能，涵盖折线图、面积图、条形图、热力图、饼图、散点图、双轴图、漏斗图等，并提供了丰富的自定义选项和交互配置。

- 📊 **高级交互** - 支持图表联动、默认提示、图例过滤等交互功能  
- 📈 **折线图** - 包括基础折线图、平滑折线图、多色折线图等变体  
- 🔵 **面积图** - 涵盖基础面积图、堆叠面积图、阶梯面积图等  
- 📊 **条形图/柱形图** - 提供堆叠、分组、反射条形图及自定义样式  
- 🔥 **热力图** - 支持形状大小映射、密度热力图等  
- 🍰 **饼图/环图** - 包含基础饼图、甜甜圈图、自定义标签等  
- ✨ **散点图/气泡图** - 支持标签散点图、渐变色散点图、对数气泡图  
- ⚖️ **双轴图** - 柱线混合、多轴图、帕累托图等复合图表  
- 🎯 **漏斗图/直方图** - 对比漏斗图、颜色分类直方图等  
- 🌟 **雷达图/迷你图** - 基础雷达图、带网格迷你图等  
- 📦 **箱线图/子弹图** - 预处理箱线图、多指标子弹图等  
- 🌀 **韦恩图/矩阵树图** - 基础韦恩图、自定义颜色等  
- 🌊 **水波图/玫瑰图** - 水滴形状水波图、堆积玫瑰图等  
- ☀️ **旭日图/词云图** - 带标签旭日图、图片遮罩词云图  
- 🎚️ **仪表盘/小提琴图** - 自定义指针、极坐标小提琴图  
- 🌐 **复合视图/桑基图** - 层叠容器、支付宝流量桑基图  
- 🏷️ **图形标注/交互** - 点标记条形图、刷选事件、图表联动  
- 🌳 **生态树/思维导图** - 水平/垂直生态树、动态展开节点  
- 🕸️ **网络图/流程图** - 流向图、任务调度流程图

---

### [GitHub - chartjs/Chart.js：使用<canvas>标签的简易HTML5图表库](https://github.com/chartjs/Chart.js)

**原文标题**: [GitHub - chartjs/Chart.js: Simple HTML5 Charts using the <canvas> tag](https://github.com/chartjs/Chart.js)

Chart.js 是一个基于 HTML5 Canvas 的简单灵活的 JavaScript 图表库，适用于设计师和开发者。

- 📊 **功能特点**：使用 `<canvas>` 标签创建简单而灵活的 HTML5 图表。
- 🌐 **文档与版本**：提供详细的文档，当前版本为 4.x，旧版文档需通过指定版本号访问。
- 🔧 **开发与贡献**：支持开发者通过 GitHub 提交问题和拉取请求，贡献前需阅读贡献指南。
- 💡 **支持与社区**：技术支持可通过 Stack Overflow 上的 `chart.js` 标签提问。
- 📜 **许可证**：采用 MIT 许可证，允许自由使用和修改。
- ⭐ **项目热度**：拥有 66.1k 星标、12k 分叉和 1.3m+ 使用者，显示出广泛的社区支持和应用。
- 🛠️ **技术栈**：主要使用 JavaScript (88.9%) 和 TypeScript (10.7%) 开发。
- 🔄 **维护与更新**：项目活跃，最新版本为 v4.5.0，发布于 2025 年 6 月 14 日。

---

### [Chart.js 示例 | Chart.js](https://www.chartjs.org/docs/4.5.0/samples/information.html)

**原文标题**: [Chart.js Samples | Chart.js](https://www.chartjs.org/docs/4.5.0/samples/information.html)

概述：本文介绍了 Chart.js 示例的使用方法、注意事项以及相关功能，包括本地运行示例、示例数据的生成方式以及操作按钮的实现。

- 🚀 通过侧边栏或本地运行（克隆仓库、安装依赖、构建文档）访问 Chart.js 示例  
- ⚠️ 示例仅供演示，直接复制粘贴到网站可能无法使用，需参考使用页面  
- 📊 示例数据通过自定义函数自动生成，不包含在库中，详情见工具页面  
- 🔘 操作按钮由文档插件实现，需自行添加按钮和事件监听器以实现功能  
- 📅 最后更新日期：2025 年 6 月 14 日，示例主题：条形图圆角边框

---

### [GitHub - image-js/tiff：完全用JavaScript编写的TIFF图像解码器](https://github.com/image-js/tiff)

**原文标题**: [GitHub - image-js/tiff: TIFF image decoder written entirely in JavaScript](https://github.com/image-js/tiff)

这是一个基于 JavaScript 的 TIFF 图像解码器项目，完全用 JavaScript 编写，支持多种 TIFF 图像格式和解码功能。

- 📜 **项目名称**: image-js/tiff  
- 🌟 **Stars**: 209  
- 🍴 **Forks**: 18  
- 📜 **许可证**: MIT  
- 🏠 **维护者**: Zakodium  

- 📂 **功能概述**:  
  - 🖼️ 支持解码灰度图和 RGB 图像（8、16 或 32 位）  
  - 🔄 支持 LZW 压缩和带 Alpha 通道的图像  
  - 📦 支持 Zlib/deflate 算法压缩的图像  

- 📥 **安装**:  
  - `npm install tiff`  

- 📊 **API 主要功能**:  
  - `tiff.decode(data[, options])` - 解码文件并返回 TIFF IFDs  
  - `tiff.pageCount(data)` - 返回文件中的 IFD（页）数量  
  - `tiff.isMultiPage(data)` - 检查文件是否有多页  

- 📄 **IFD 对象属性**:  
  - `data` - 像素数据的 Typed Array（Uint8Array、Uint16Array 或 Float32Array）  
  - `size`、`width`、`height` - 图像的尺寸信息  
  - `bitsPerSample` - 位深度  
  - `alpha` - 是否包含 Alpha 通道  

- 🌍 **资源**:  
  - 官网：[image-js.github.io/tiff/](https://image-js.github.io/tiff/)  
  - 文档：完整 API 文档  

- 📌 **其他信息**:  
  - 使用语言：TypeScript 99.6%, JavaScript 0.4%  
  - 发布版本：最新 v7.0.0（2025 年 6 月 15 日）

---

### [一丝不苟](https://www.meticulous.ai?utm_source=javascript_weekly&utm_campaign=june20th2025)

**原文标题**: [Meticulous](https://www.meticulous.ai?utm_source=javascript_weekly&utm_campaign=june20th2025)

Meticulous AI 是一个自动化测试平台，通过记录用户与应用的交互来生成和维护测试套件，无需手动编写或维护测试用例，帮助开发团队快速、可靠地发布代码。

- 🚀 **无需编写测试** - Meticulous AI 自动生成覆盖所有边缘用例的测试套件，无需手动编写或维护测试。  
- 🔍 **记录用户交互** - 通过在开发、预发布和生产环境中添加脚本标签，记录用户会话以生成测试用例。  
- 🤖 **AI 驱动测试** - AI 引擎根据代码分支和用户交互动态生成并更新测试，确保全面覆盖。  
- ⚡ **快速集成** - 支持多种前端框架（如 React、Vue、Angular 等），几分钟内即可完成集成。  
- 🛡️ **零误报** - 通过模拟后端响应，避免因数据变化导致的误报，测试结果更可靠。  
- 📊 **高效并行测试** - 测试任务在计算集群上并行执行，可在 120 秒内完成数千次测试。  
- 💬 **用户见证** - 被 Dropbox、Lattice 等 100 多家组织信任，显著提升开发效率和代码质量。  
- 🔄 **无缝兼容** - 可单独使用或与现有测试套件结合，灵活适配不同团队需求。  
- 📈 **持续进化** - 测试套件随应用功能更新自动调整，始终保持最新状态。

---

### [EncolaJS Enforma | VueJS 应用的全套表单解决方案](https://encolajs.com/enforma/)

**原文标题**: [EncolaJS Enforma | Complete form solution for VueJS applications](https://encolajs.com/enforma/)

数据处理能力强大，支持复杂结构  

- 🏗️ 内置支持嵌套表单  
- 🔄 可处理重复字段  
- 🧩 支持复杂数据结构

---

### [JSNation – 美国顶级 JavaScript 大会](https://jsnation.us/?utm_source=Newsletter&utm_medium=JSWeekly%20)

**原文标题**: [JSNation – The main JS conference in the US](https://jsnation.us/?utm_source=Newsletter&utm_medium=JSWeekly%20)

美国主要的 JS 会议将于 2025 年 11 月 17 日（纽约线下 + 线上）和 11 月 20 日（纯线上）举行，汇聚 50+ 顶尖思想家和 700+ 开发者，全球连接 10K 开发者，共同探索 JS 未来趋势。  

- 🌟 活动形式：纽约线下 + 线上混合模式，全球开发者共同参与  
- 🗓️ 主要日期：11 月 17 日（线下 + 线上）、11 月 18 日（线下派对）、11 月 20 日（纯线上）  
- 🎤 核心团队参与：Vite、Deno、Svelte、Chrome、Webpack 等团队  
- 🚀 特色活动：  
  - 🌌 西方最大天文馆演讲（React 技术前沿）  
  - 🚢 曼哈顿景观渡轮接送  
  - 🎉 全美最大 JS 派对（行业交流 + 街机游戏）  
  - 🗽 自由女神像附近打卡  
  - 💻 高清远程会议体验（互动问答 + 讨论室）  
- 🎤 部分演讲嘉宾：  
  - Addy Osmani（Google Chrome 工程负责人）  
  - Rich Harris（Svelte 创始人）  
  - Wes Bos（Syntax.fm 联合主持人）  
- 🛠️ 免费与付费工作坊：  
  - 现代 React 架构（远程）  
  - Node.js 构建 MCP（线下）  
- 🎟️ 票务选项：  
  - 线下 + 线上联票（$640 起）  
  - 纯线上票（$190 起）  
  - Multipass 通票（$19/月，畅享 10+ 会议）  
- 🎁 福利：早鸟优惠、演讲录像、社交证书、周边礼包  
- 📍 线下地点：纽约自由科学中心（Liberty Science Center）  
- 📢 特别机会：分享活动徽章可赢免费线上票！  

（注：内容已精简，保留核心信息与关键亮点。）

---

### [我们如何将 CKEditor 的包大小减少 40% | CKEditor](https://ckeditor.com/blog/how-we-reduced-ckeditor-bundle-size/)

**原文标题**: [How We Reduced CKEditorâs Bundle Size by 40% | CKEditor](https://ckeditor.com/blog/how-we-reduced-ckeditor-bundle-size/)

CKEditor 5 团队通过一系列优化技术成功将编辑器包体积减小 40%，包括树摇优化、代码纯净化、依赖管理升级等。以下是关键优化步骤和成果：

- 🌳 **树摇优化基础**：通过重构代码消除副作用，使用`/* #__PURE__ */`注释标记无副作用代码，使打包工具能安全移除未使用代码。  
- 🎯 **编译目标升级**：将代码编译目标从 ES2019 提升至 ES2022，避免旧版语法转换导致的不可树摇代码。  
- 📦 **依赖管理**：替换重量级依赖（如`lodash-es`为轻量`es-toolkit`），并确保所有依赖使用统一版本以减少重复打包。  
- 🚫 **副作用声明**：在`package.json`中精确配置`sideEffects`字段，明确非树摇安全文件（如 CSS 和 UMD 翻译文件）。  
- 📊 **监控机制**：引入自动化回归测试工具 Sonda，实时监测包体积变化并定位问题代码，防止优化回退。  
- 📉 **实际效果**：优化后常见编辑器配置的打包体积下降 38%-43%（Vite 最小达 251 KiB），非树摇代码减少 90%。  

团队强调优化需持续迭代，并提供了开源库优化清单（如优先代码拆分、避免 Polyfill 等）。此次优化显著提升了 CKEditor 5 在各类前端环境中的加载性能。

---

### [JPEG 如何成为互联网的图像标准 - IEEE 频谱](https://spectrum.ieee.org/jpeg-image-format-history)

**原文标题**: [How JPEG Became the Internet’s Image Standard - IEEE Spectrum](https://spectrum.ieee.org/jpeg-image-format-history)

JPEG 格式在三十年前成为互联网上分享数字照片的主导方式，至今仍在网络中占据重要地位。

- 📅 **历史背景**：三十年前，JPEG 格式成为互联网上分享数字照片的标准。  
- 🖼️ **技术优势**：JPEG 以其高效的压缩算法，在保持较好图像质量的同时大幅减小文件大小。  
- 🌐 **网络普及**：JPEG 的普及推动了数字照片在互联网上的广泛传播和共享。  
- 🔄 **持久影响**：尽管有新技术出现，JPEG 因其兼容性和广泛支持，至今仍是网络图像的主流格式。  
- 📰 **专家观点**：Ernie Smith 通过其长期运营的新闻通讯 Tedium，探讨了这一技术的长期影响。

---

### [三行代码将任何 React 应用连接到 MCP 服务器](https://blog.cloudflare.com/connect-any-react-application-to-an-mcp-server-in-three-lines-of-code/)

**原文标题**: [Connect any React application to an MCP server in three lines of code](https://blog.cloudflare.com/connect-any-react-application-to-an-mcp-server-in-three-lines-of-code/)

概述：本文介绍了如何通过三行代码将任何 React 应用连接到 MCP 服务器，并开源了两个工具：use-mcp React 库和 AI Playground，以简化 MCP 客户端的构建和部署。

- 🚀 **一键部署 MCP 服务器**：可在 Cloudflare 上一键部署支持最新 MCP 标准的远程服务器，已被多家知名公司采用。  
- ⚛️ **开源 React 库 use-mcp**：仅需三行代码即可连接远程 MCP 服务器，自动处理传输、认证和会话管理。  
- 🔍 **动态工具发现**：自动获取服务器提供的工具，支持类型安全元数据，无需代码变更即可适配新功能。  
- 🔄 **连接管理**：内置重连机制和状态提示（如“连接中”“就绪”“失败”），提升用户体验。  
- 🔐 **认证支持**：集成 OAuth 2.1 流程，自动处理登录、令牌存储和权限撤销。  
- 🛠️ **调试与监控**：提供结构化日志和实时调试界面，便于开发和生产环境问题排查。  
- 🌐 **未来兼容性**：支持 SSE 和 Streamable HTTP 传输协议，并持续跟进 MCP 标准更新。  
- 🤖 **AI Playground 开源**：内置 MCP 客户端的聊天界面平台，支持多模型交互和实时调试功能。  
- 📂 **社区贡献**：将 use-mcp 贡献至 MCP 生态系统，鼓励开发者参与共建，提供示例代码和 GitHub 资源。  
- 📧 **反馈与合作**：欢迎通过邮件联系团队，分享建议或协作想法。

---

### [GitHub - modelcontextprotocol/use-mcp](https://github.com/modelcontextprotocol/use-mcp)

**原文标题**: [GitHub - modelcontextprotocol/use-mcp](https://github.com/modelcontextprotocol/use-mcp)

一个轻量级的 React 钩子，用于连接 Model Context Protocol (MCP) 服务器，简化 AI 系统的认证和工具调用。

- 🦑 **use-mcp** 是一个 React 钩子，用于连接 MCP 服务器，支持自动重连和 OAuth 认证流程。
- 🔧 **功能**：自动连接管理、OAuth 认证处理、简单的 React 钩子接口、TypeScript 类型支持、全面的调试日志、支持 HTTP 和 SSE 传输。
- 📥 **安装**：通过 npm、pnpm 或 yarn 安装，命令分别为 `npm install use-mcp`、`pnpm add use-mcp` 或 `yarn add use-mcp`。
- 🚀 **快速开始**：使用 `useMcp` 钩子连接 MCP 服务器，支持多种状态管理（如连接中、认证中、失败等）和工具调用。
- 🔄 **OAuth 回调设置**：支持 React Router 和 Next.js Pages Router 设置 OAuth 回调端点。
- 📚 **API 参考**：提供详细的 `useMcp` 钩子选项和返回值说明，包括连接状态、工具列表、错误信息等。
- 📜 **许可证**：MIT 许可证，开源免费使用。
- 🌐 **资源**：包含 README、许可证、行为准则和安全政策等文档。

---

### [微软社区中心宣布：VS Code 中推出全新的 PostgreSQL IDE](https://techcommunity.microsoft.com/blog/adforpostgresql/announcing-a-new-ide-for-postgresql-in-vs-code-from-microsoft/4414648)

**原文标题**: [Announcing a new IDE for PostgreSQL in VS Code from Microsoft | Microsoft Community Hub](https://techcommunity.microsoft.com/blog/adforpostgresql/announcing-a-new-ide-for-postgresql-in-vs-code-from-microsoft/4414648)

微软宣布在 VS Code 中推出全新的 PostgreSQL 扩展公开预览版，旨在简化 PostgreSQL 数据库管理和开发流程。

- 🎉 **新扩展发布**：PostgreSQL 扩展为 VS Code 提供数据库管理和智能查询编写功能，集成 GitHub Copilot 代理“@pgsql”。
- ⏱️ **解决开发痛点**：减少任务切换和调试时间，提供统一的应用开发和数据库管理体验。
- 🖼️ **模式可视化**：通过右键菜单轻松可视化数据库模式。
- 🤖 **AI 辅助开发**：GitHub Copilot 提供实时指导，优化查询、调试和性能调优。
- 🔗 **简化连接管理**：支持本地和云托管 PostgreSQL 实例，集成 Entra ID 进行身份验证。
- 🔒 **无密码认证**：利用 Entra ID 实现无缝登录和自动令牌刷新，增强安全性。
- 📊 **数据库资源管理器**：结构化查看和管理数据库对象，如模式、表和函数。
- 📜 **查询历史**：快速查看和重用之前运行的查询。
- ✍️ **智能查询编辑**：上下文感知的 IntelliSense 提供 SQL 关键字、表名和函数的自动完成。
- 🚀 **独特优势**：增强生产力、智能 Copilot 代理、简化入门、改进安全性和全面的工具集。
- 📥 **安装简单**：通过 VS Code 扩展市场搜索并安装 PostgreSQL 扩展。
- 💬 **反馈与支持**：欢迎用户通过 VS Code 内置反馈工具分享意见和建议。

---

### [介绍微软为 PostgreSQL 推出的 VS Code 扩展 | POSETTE：2025 年 Postgres 大会活动 - YouTube](https://www.youtube.com/watch?v=wzyY7GNV7Xo)

**原文标题**: [Introducing Microsoft's VS Code Extension for PostgreSQL | POSETTE: An Event for Postgres 2025 - YouTube](https://www.youtube.com/watch?v=wzyY7GNV7Xo)

YouTube 平台相关信息概览  

- 📢 关于我们 - 提供 YouTube 的背景和基本信息  
- 🗞️ 新闻动态 - 获取 YouTube 的最新新闻和公告  
- ©️ 版权信息 - 了解 YouTube 的版权政策和相关内容  
- 📩 联系我们 - 提供与 YouTube 团队联系的途径  
- 🎨 创作者信息 - 面向内容创作者的相关资源和支持  
- 💼 广告合作 - 广告主和合作伙伴的相关信息  
- 💻 开发者资源 - 为开发者提供的工具和 API 信息  
- 📜 服务条款 - 使用 YouTube 平台的法律条款  
- 🔒 隐私政策 - 用户数据保护和隐私政策说明  
- ⚖️ 政策与安全 - 平台规则、安全措施及合规信息  
- 🔧 工作原理 - YouTube 平台的运作机制和功能解释  
- 🧪 测试新功能 - 参与新功能的试用和反馈  
- © 2025 Google LLC - 版权归属及公司信息

---

### [Git 2.50.0 有哪些新变化？](https://about.gitlab.com/blog/what-s-new-in-git-2-50-0/)

**原文标题**: [Whatâs new in Git 2.50.0?](https://about.gitlab.com/blog/what-s-new-in-git-2-50-0/)

平台概述  
最全面的 AI 驱动 DevSecOps 平台  

- 🔍 探索我们的一体化 AI 驱动 DevSecOps 平台  
- 🛡️ 提供全面的安全防护与开发运维整合  
- 🤖 利用人工智能优化开发与安全流程  
- 🚀 旨在提升效率与保障系统安全性

---

### [Git 2.50 亮点集锦 - GitHub 博客](https://github.blog/open-source/git/highlights-from-git-2-50/)

**原文标题**: [Highlights from Git 2.50 - The GitHub Blog](https://github.blog/open-source/git/highlights-from-git-2-50/)

开源项目 Git 发布了 2.50 版本，包含来自 98 位贡献者的功能更新和错误修复，其中 35 位是新贡献者。以下是主要亮点：

- 🚀 **多 cruft 包改进**：Git 2.50 引入了`--combine-cruft-below-size`选项，优化了多 cruft 包的管理，修复了对象更新时间刷新的问题。  
- 🔍 **增量多包可达性位图**：支持增量多包索引（MIDX）链中的多包位图，提升大型仓库的性能，尽管该功能仍处于实验阶段。  
- 🔄 **ORT 合并引擎取代 recursive**：ORT 成为默认合并引擎，完全移除了旧的 recursive 引擎，新增`--quiet`模式以检测可合并性而不写入新对象。  
- 🛠️ **git cat-file 增强**：新增对象类型过滤功能（如`--filter='object:type=tree'`），并弃用`--allow-unknown-type`选项。  
- 🧹 **git maintenance 新任务**：支持`worktree-prune`、`rerere-gc`和`reflog-expire`任务，优化松散对象打包配置（`maintenance.loose-objects.batchSize`）。  
- 📜 **reflog 管理简化**：新增`git reflog delete`命令，替代复杂的`expire`操作。  
- ⚡ **引用处理优化**：提升`git update-ref`性能，减少冗余检查，支持引用前缀缓存和迭代器复用。  
- 🌐 **HTTP 连接调优**：新增 TCP Keepalive 配置选项（`http.keepAliveIdle`、`http.keepAliveInterval`、`http.keepAliveCount`）。  
- 🐧 **减少 Perl 依赖**：测试套件和文档工具链不再依赖 Perl，部分功能改用 Shell 或 C 实现。  
- ✏️ **交互式 rebase 界面改进**：提交信息前添加`#`注释符，避免误修改。  
- 📦 **bundle-uri 性能提升**：克隆时广告所有已知引用，加速填充式拉取。  
- 🌱 **稀疏检出兼容性**：`git add -p`和`git add -i`无需扩展稀疏索引即可操作。  

其他更新包括 Git 20 周年庆祝活动及更多细节，可查阅[2.50 版本说明](https://github.com/git/git/blob/master/Documentation/RelNotes/2.50.0.txt)。

---

### [Makefile 示例教程](https://makefiletutorial.com/)

**原文标题**: [Makefile Tutorial By Example](https://makefiletutorial.com/)

这篇指南旨在帮助读者理解和掌握 Makefile 的使用，通过详细的示例和解释，使复杂的 Makefile 规则变得清晰易懂。

- 🛠️ 作者因对 Makefile 的复杂性感到困惑，决定深入研究并整理出这份指南，包含关键知识点和可运行的示例。
- 📖 指南适合初学者，也提供了《Makefile Cookbook》供有经验的用户参考，用于中等规模项目的模板。
- ⚙️ Makefile 主要用于决定大型程序中哪些部分需要重新编译，尤其在 C/C++ 项目中常见。
- 🔄 Makefile 通过文件时间戳判断依赖关系，决定是否需要重新编译。
- 📝 Makefile 基本语法包括目标（targets）、依赖（prerequisites）和命令（commands），命令必须以 Tab 开头。
- 🏗️ 示例展示了从简单的“Hello World”到编译 C 文件的多目标 Makefile，逐步增加复杂性。
- 🧩 介绍了 Makefile 中的变量使用、通配符、自动变量和模式规则等高级特性。
- 🔧 提供了错误处理、递归调用 make、环境变量传递等实用技巧。
- 📌 强调了.PHONY 和.DELETE_ON_ERROR 等特殊目标的重要性，避免常见错误。
- 🍲 最后的 Makefile Cookbook 展示了一个自动化处理依赖的中型项目 Makefile 模板，支持 C/C++ 文件编译。

这份指南通过循序渐进的方式，帮助读者从基础到高级全面掌握 Makefile 的编写和使用。

---

