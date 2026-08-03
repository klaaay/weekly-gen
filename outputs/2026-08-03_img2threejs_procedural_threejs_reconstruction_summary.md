### [img2threejs：把参考图重建为可动画的程序化 Three.js 模型](https://github.com/img2threejs/img2threejs)

**原文标题**: [img2threejs — Rebuild the object in a reference image as a code-only, procedural, quality-gated, animation-ready Three.js model](https://github.com/img2threejs/img2threejs)

img2threejs 是一个面向编码 Agent 的技能与工作流：输入一张对象参考图，输出由 TypeScript 编写的 `THREE.Group` 工厂函数。它用基础几何体、程序化材质与生成几何来重建对象，并把可运动部件的 pivot、socket、collider 等运行时层级一并建好；目标是得到可继续编辑、可检查、可用于动画的代码资产，而不是下载来的网格或一次性的图像转 3D 结果。

- 🧱 **代码优先，而非网格提取**：整个模型由 Three.js 代码生成并在浏览器实时运行；它明确不采用摄影测量、mesh extraction 或外部美术资源包，因此输出可版本控制、参数化修改并嵌入现有 Web 项目。
- 🔄 **分阶段重建流水线**：依次经历 `blockout → structural → form → material → surface → lighting → interaction → optimization`。每一阶段生成可检查的构建结果，结合渲染图与参考图的对照评审，再决定是否进入下一阶段。
- 🔍 **细节先行的质量门槛**：生成代码前先建立 `detailInventory`，枚举影响辨识度的细节——倒角、圆角、接缝、螺丝/铆钉、刻线、涂装、光泽分区、污渍与磨损等。每项都必须落到真实的组件或材质条目，避免用一张“看起来像”的贴图掩盖缺失的结构。
- ⚙️ **让模型 Token 用在判断而非机械校验**：确定性的 Python 脚本负责图片探测、规格校验与质量门禁；Agent Token 集中用于视觉分析、代码生成和渲染评审。这是一种把 LLM 放在高不确定性环节、将重复规则工程化的设计。
- 🕹️ **面向运行时与动画**：输出不是静态的一团几何，而是带有可操作层级的 `THREE.Group`；需要运动的部件暴露 pivot 和 socket，并可加入 `userData.tick` 等循环动画入口，便于继续接入交互或游戏逻辑。
- 🧑‍🎨 **按对象类型路由**：主体会被分类为 `object`、`character` 或 `hybrid`。硬表面物体走物件流水线；角色走面向解剖的流程，处理头身比例、面部特征点和姿势。武器等特定类别还拥有组件覆盖率与结构完整性检查。
- 🎨 **材质应从图像证据推导**：工作流强调从参考像素判断表面类型、渐变与光泽，而非凭记忆给“金属”“糖果漆”等贴标签；同时提示会在 tone mapping 后失真的颜色，并要求报告无法从图像判断区域的置信度。
- 🧪 **严格模式拒绝“凑合通过”**：`--strict-quality` 会阻止不完整规格继续生成；每一轮通过 side-by-side 对照复核。核心观念是可度量地逼近参考，而非一次提示词后直接接受结果。
- 🤝 **宿主无关**：README 声明可运行于 Claude Code、Codex 或 OpenCode；其中“图像读取”“浏览器工具”等能力由宿主的原生视觉、Browser MCP、项目预览或用户截图提供。

#### 最小使用方式

将仓库放入当前 Agent 宿主可发现的 skills 目录，向 Agent 附上或指出参考图后调用技能。项目给出的最小指令为：

```text
/img2threejs Rebuild this object as a Three.js model, keep the proportions, angles, and colours.
```

若需要更高保真度，应明确约束轮廓与比例、先列出辨识性细节、指定材质判断应基于图像像素、要求可动部件暴露运行时层级，并开启严格质量门禁。其底层脚本只要求 Python 3.10+，可分别执行图片探测、预规格生成、严格校验和 Three.js 工厂代码生成。

#### 学习要点与实践启发

- “图像转 3D”不应只定义为产出一个视觉相似的物体；如果目标是产品、游戏或交互场景，运行时层级、可编辑性与动画接口同样属于交付质量。
- 单张图天然无法揭示背面、遮挡面和精确深度。可靠的系统应把这些区域标为推断并给出置信度，必要时索取更多角度，而不是伪造精确性。
- 复杂视觉生成适合拆成“规格 → 构建 → 对照评审 → 修正”的闭环；这比将所有要求压进一次大提示词更可控，也更容易定位质量退化的阶段。
- 质量门禁的价值在于把主观的“像不像”部分转成可复核的证据：关键部件是否存在、细节是否覆盖、材质与结构是否各自成立。该思路同样可用于 UI 还原和视觉回归测试。
- 对本仓库而言，该项目适合作为“Agent 工作流如何将模型判断与确定性验证组合”的案例；它并不直接依赖本项目的周报生成流程，无需将其安装为运行依赖。

#### 使用边界

- 单图重建不保证隐藏面的真实几何，也不能保证人物或角色达到照片级相似度；项目会以可见面镜像等方式推断，并将低置信区域显式报告。
- 对硬表面对象表现更强；角色结果定位为风格化重建。若需求是精确资产生产，应准备多视图参考与人工复核。

**来源**：[GitHub README](https://github.com/img2threejs/img2threejs) · [在线 Demo Gallery](https://img2threejs.github.io/img2threejs-showcase/)

---
