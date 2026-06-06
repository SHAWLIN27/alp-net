# Drawing Free-body Diagrams / 绘制受力分析图

---

## 1. Overview / 概述

**English:**
Drawing free-body diagrams is the foundational skill for applying [[Newton's Laws of Motion]] to real-world problems. A free-body diagram (FBD) is a simplified sketch showing all forces acting on a single object, represented as arrows from the object's centre. This sub-topic teaches the systematic method for isolating an object, identifying all forces from [[Types of Force]], and representing them correctly. Mastering FBDs is essential before tackling [[Resolving Forces on Inclined Planes]] and [[Equilibrium Conditions]], as it transforms complex physical situations into clear vector problems.

**中文:**
绘制受力分析图是应用[[牛顿运动定律]]解决实际问题的基础技能。受力分析图（FBD）是一种简化示意图，用从物体中心出发的箭头表示作用在单个物体上的所有力。本子知识点教授系统化的方法：隔离物体、识别来自[[力的类型]]的所有力、并正确表示它们。掌握受力分析图是学习[[斜面受力分解]]和[[平衡条件]]的前提，它能将复杂的物理情境转化为清晰的矢量问题。

---

## 2. Core Definition / 核心定义

| Term (EN/CN) | Definition (EN) | Definition (CN) |
| ------------ | --------------- | --------------- |
| **Free-body Diagram (FBD)** / 受力分析图 | A diagram showing all external forces acting on a single isolated object, with forces represented as vectors from the object's centre of mass. | 显示作用在单个隔离物体上所有外力的示意图，力用从物体质心出发的矢量表示。 |
| **Isolated Object** / 隔离物体 | The single object being analysed, drawn alone without its surroundings. | 被分析的单个物体，单独画出，不包含周围环境。 |
| **Force Vector** / 力矢量 | An arrow representing a force, with length proportional to magnitude and direction showing the line of action. | 表示力的箭头，长度与大小成正比，方向表示作用线。 |
| **Contact Force** / 接触力 | A force that requires physical contact between objects (e.g., [[Normal Reaction Force]], [[Friction]]). | 需要物体间物理接触的力（如[[支持力]]、[[摩擦力]]）。 |
| **Non-contact Force** / 非接触力 | A force that acts at a distance without physical contact (e.g., [[Weight]], [[Electrostatic Force]]). | 无需物理接触、在距离上作用的力（如[[重力]]、[[静电力]]）。 |
| **System Boundary** / 系统边界 | The imaginary boundary separating the object of interest from its environment. | 将目标物体与周围环境分开的假想边界。 |

---

## 3. Key Concepts / 关键概念

**English:**

### The Systematic Method for Drawing FBDs

**Step 1: Isolate the Object**
Draw the object as a simple shape (box, dot, or circle). Remove all surroundings — no ropes, surfaces, or other objects. This is the "free body".

**Step 2: Identify All Forces**
Work through the [[Types of Force]] systematically:
- **Weight ($W$ or $mg$):** Always present, acts vertically downward from centre of mass.
- **Normal Reaction ($N$ or $R$):** Perpendicular to any contact surface, pushing away from the surface.
- **Tension ($T$):** Along a string/rope, pulling away from the object.
- **Friction ($F_f$):** Parallel to contact surface, opposing relative motion or attempted motion.
- **Thrust/Applied Force ($F$):** Any other push or pull.

**Step 3: Draw Force Vectors**
- Draw arrows starting from the object's centre.
- Arrow length should roughly represent relative magnitude.
- Label each force with its symbol (e.g., $W$, $N$, $T$).

**Step 4: Choose a Coordinate System**
- Typically $x$ horizontal, $y$ vertical.
- For inclined planes, rotate axes to be parallel/perpendicular to the slope (see [[Resolving Forces on Inclined Planes]]).

### Common Pitfalls

- **Missing forces:** Forgetting weight or normal reaction.
- **Extra forces:** Including forces the object exerts on others (e.g., "reaction to weight" is not on the object).
- **Wrong direction:** Normal reaction is always perpendicular to the surface, not necessarily vertical.
- **Incorrect starting point:** Forces should start from the centre, not the edges.

**中文:**

### 绘制受力分析图的系统方法

**第1步：隔离物体**
将物体画成简单形状（方块、点或圆圈）。移除所有周围环境——没有绳子、表面或其他物体。这就是"自由体"。

**第2步：识别所有力**
系统地检查[[力的类型]]：
- **重力（$W$或$mg$）：** 始终存在，从质心竖直向下作用。
- **支持力（$N$或$R$）：** 垂直于任何接触面，从表面向外推。
- **张力（$T$）：** 沿绳子/绳索方向，从物体向外拉。
- **摩擦力（$F_f$）：** 平行于接触面，阻碍相对运动或运动趋势。
- **推力/施加力（$F$）：** 任何其他推或拉。

**第3步：绘制力矢量**
- 从物体中心开始画箭头。
- 箭头长度应大致表示相对大小。
- 用符号标注每个力（如$W$、$N$、$T$）。

**第4步：选择坐标系**
- 通常$x$水平，$y$竖直。
- 对于斜面，旋转坐标轴使其平行/垂直于斜面（参见[[斜面受力分解]]）。

### 常见错误

- **遗漏力：** 忘记重力或支持力。
- **多余力：** 包括物体对其他物体施加的力（如"重力的反作用力"不在物体上）。
- **方向错误：** 支持力始终垂直于表面，不一定是竖直方向。
- **起点错误：** 力应从中心开始，而不是从边缘。

> 📷 **IMAGE PROMPT — FBD-01: Comparison of Correct vs Incorrect FBDs**
>
> **English Prompt:**
> A textbook-style comparison diagram showing three versions of a block on a rough horizontal surface being pulled by a rope at 30° above horizontal. Left panel: Correct FBD with weight (W) down, normal reaction (N) up, tension (T) at 30°, friction (F) left. Centre panel: Missing weight force. Right panel: Extra upward force labelled "reaction to weight". Each panel has a tick or cross. Clean white background, black arrows with labels, simple block shape. Educational vector style.
>
> **中文描述:**
> 教科书风格的对比图，显示粗糙水平面上被绳子以30°角拉动的木块的三个版本。左图：正确的受力分析图，重力（W）向下，支持力（N）向上，张力（T）30°，摩擦力（F）向左。中图：缺少重力。右图：多了一个标有"重力的反作用力"的向上力。每个图有对勾或叉号。白色背景，黑色箭头带标签，简单方块形状。教育矢量风格。
>
> **Labels Required / 需要标注:**
> * Correct ✓ / 正确 ✓
> * Missing weight ✗ / 缺少重力 ✗
> * Extra force ✗ / 多余力 ✗
>
> **Style / 风格:** Textbook vector / 教科书矢量图
>
> **Exam Relevance / 考试关联:**
> Common exam mistakes are shown explicitly — students lose marks for missing or extra forces.

---

## 4. Formulas / 公式

There is no single formula for drawing FBDs, but the key relationship used is:

$$ \vec{F}_{\text{net}} = \sum \vec{F} = m\vec{a} $$

This is [[Newton's Second Law]] — the FBD is the tool to find $\sum \vec{F}$.

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
| ------------- | ------------ | ------------ | ----------- |
| $\vec{F}_{\text{net}}$ | Net (resultant) force | 合力 | N |
| $\sum \vec{F}$ | Vector sum of all forces | 所有力的矢量和 | N |
| $m$ | Mass of object | 物体质量 | kg |
| $\vec{a}$ | Acceleration of object | 物体加速度 | m/s² |

**Derivation / 推导:**
Not applicable — this is a graphical method, not a derived formula.

**Conditions / 适用条件:**
- The object must be treated as a point mass at its centre.
- Only external forces on the object are included.
- Forces are vectors and must be added using vector addition (see [[Resolving Forces on Inclined Planes]]).

> 📷 **IMAGE PROMPT — FBD-02: Step-by-Step FBD Construction**
>
> **English Prompt:**
> A four-panel step-by-step diagram showing construction of an FBD for a book on a table. Panel 1: Book alone as a rectangle. Panel 2: Weight arrow (W) added downward from centre. Panel 3: Normal reaction arrow (N) added upward from centre, equal length to W. Panel 4: Completed FBD with both forces labelled, coordinate axes (x horizontal, y vertical) shown. Clean educational vector style, blue arrows for weight, red for normal reaction, white background.
>
> **中文描述:**
> 四格分步图，展示桌子上书本的受力分析图构建过程。图1：单独的书本为矩形。图2：从中心向下添加重力箭头（W）。图3：从中心向上添加支持力箭头（N），长度与W相等。图4：完成的受力分析图，两个力都标注，显示坐标轴（x水平，y竖直）。干净的教育矢量风格，蓝色箭头表示重力，红色表示支持力，白色背景。
>
> **Labels Required / 需要标注:**
> * Step 1: Isolate / 第1步：隔离
> * Step 2: Add Weight / 第2步：添加重力
> * Step 3: Add Normal Reaction / 第3步：添加支持力
> * Step 4: Complete FBD / 第4步：完成受力分析图
>
> **Style / 风格:** Textbook vector / 教科书矢量图
>
> **Exam Relevance / 考试关联:**
> Shows the exact step-by-step process examiners expect in free-response questions.

---

## 5. Image Prompt / 图片提示

> 📷 **IMAGE PROMPT — FBD-03: Common FBD Scenarios for A-Level Physics**
>
> **English Prompt:**
> A grid of 6 small free-body diagrams showing common A-Level scenarios, each with a small sketch of the real situation above the FBD. Scenarios: (1) Block on horizontal surface with applied force at angle, (2) Object hanging from two strings, (3) Block on inclined plane, (4) Object in free fall (air resistance), (5) Car towing a trailer (simplified), (6) Book on a table. Each FBD shows correct force vectors from centre, labelled with standard symbols (W, N, T, F, Ff). Clean white background, black arrows, professional textbook layout. Educational vector illustration style.
>
> **中文描述:**
> 6个小受力分析图的网格，展示A-Level常见场景，每个受力分析图上方有真实情境的小草图。场景：(1) 水平面上受角度拉力的木块，(2) 两根绳子悬挂的物体，(3) 斜面上的木块，(4) 自由落体（有空气阻力），(5) 汽车拖挂车（简化），(6) 桌子上的书。每个受力分析图显示从中心出发的正确力矢量，用标准符号标注（W、N、T、F、Ff）。干净的白色背景，黑色箭头，专业教科书布局。教育矢量插图风格。
>
> **Labels Required / 需要标注:**
> * Each scenario labelled / 每个场景标注名称
> * All force vectors labelled with standard symbols / 所有力矢量用标准符号标注
>
> **Style / 风格:** Textbook vector grid / 教科书矢量网格图
>
> **Exam Relevance / 考试关联:**
> Covers the most common exam scenarios — students should recognise and be able to draw each one.

---

## 6. Worked Example / 典型例题

### Example 1: Block on a Rough Horizontal Surface

### Question / 题目
**English:**
A block of mass 5.0 kg is being pulled across a rough horizontal surface by a rope at 30° above the horizontal. The tension in the rope is 20 N. Draw a free-body diagram for the block, labelling all forces.

**中文:**
一个质量为5.0 kg的木块在粗糙水平面上被一根与水平方向成30°角的绳子拉动。绳子中的张力为20 N。画出木块的受力分析图，标注所有力。

### Solution / 解答

**Step 1: Isolate the block**
Draw the block as a simple rectangle or dot.

**Step 2: Identify all forces**
- **Weight ($W$):** $W = mg = 5.0 \times 9.81 = 49.05 \text{ N}$ downward
- **Tension ($T$):** 20 N at 30° above horizontal, pulling to the right
- **Normal reaction ($N$):** Upward, perpendicular to the surface
- **Friction ($F_f$):** To the left, opposing motion

**Step 3: Draw the FBD**

```
        T = 20 N
          ↑ 30°
           \
            \
    N ↑      \→
    ┌─────────┐
    │   ●     │
    └─────────┘
    ↓ W = 49.05 N
    ← Ff
```

**Step 4: Choose coordinate system**
$x$: horizontal (right positive), $y$: vertical (up positive)

### Final Answer / 最终答案
**Answer:** The FBD shows four forces: $W$ (49.05 N down), $N$ (up), $T$ (20 N at 30° above horizontal right), $F_f$ (left, opposing motion). **答案：** 受力分析图显示四个力：$W$（49.05 N向下）、$N$（向上）、$T$（20 N，与水平方向成30°向右上方）、$F_f$（向左，阻碍运动）。

### Quick Tip / 提示
Always check that the number of forces equals the number of contact points plus non-contact forces. For this block: 1 contact surface → normal + friction, plus weight and tension = 4 forces total.

---

### Example 2: Object Hanging from Two Strings

### Question / 题目
**English:**
A sign of weight 30 N is suspended from two strings at angles of 40° and 50° to the horizontal. Draw the free-body diagram for the sign.

**中文:**
一个重30 N的标志牌由两根绳子悬挂，绳子与水平方向分别成40°和50°角。画出标志牌的受力分析图。

### Solution / 解答

**Step 1: Isolate the sign**
Draw the sign as a dot (point mass).

**Step 2: Identify all forces**
- **Weight ($W$):** 30 N downward
- **Tension in left string ($T_1$):** Along the string, at 40° above horizontal to the left
- **Tension in right string ($T_2$):** Along the string, at 50° above horizontal to the right

**Step 3: Draw the FBD**

```
          T₁    T₂
           \   /
            \ /
             ●
             ↓
             W = 30 N
```

### Final Answer / 最终答案
**Answer:** The FBD shows three forces: $W$ (30 N down), $T_1$ (at 40° above horizontal left), $T_2$ (at 50° above horizontal right). **答案：** 受力分析图显示三个力：$W$（30 N向下）、$T_1$（与水平方向成40°向左上方）、$T_2$（与水平方向成50°向右上方）。

### Quick Tip / 提示
For hanging objects, tensions always pull away from the object along the strings. The object is in equilibrium, so the vector sum of all forces is zero — this will be used in [[Equilibrium Conditions]].

---

## 7. Flashcards / 闪卡

**Flashcard 1**
Q (EN): What are the four steps for drawing a free-body diagram?
Q (CN): 绘制受力分析图的四个步骤是什么？
A (EN): (1) Isolate the object, (2) Identify all forces, (3) Draw force vectors from centre, (4) Choose coordinate system.
A (CN): (1) 隔离物体，(2) 识别所有力，(3) 从中心绘制力矢量，(4) 选择坐标系。

**Flashcard 2**
Q (EN): What is the most common mistake when drawing a free-body diagram?
Q (CN): 绘制受力分析图时最常见的错误是什么？
A (EN): Including forces that the object exerts on other objects (e.g., "reaction to weight"), or forgetting weight.
A (CN): 包括物体对其他物体施加的力（如"重力的反作用力"），或忘记重力。

**Flashcard 3**
Q (EN): In which direction does the normal reaction force always act?
Q (CN): 支持力始终朝哪个方向作用？
A (EN): Perpendicular to the contact surface, pushing away from the surface.
A (CN): 垂直于接触面，从表面向外推。

**Flashcard 4**
Q (EN): What does the length of a force arrow in an FBD represent?
Q (CN): 受力分析图中力箭头的长度表示什么？
A (EN): The relative magnitude of the force (longer arrow = larger force).
A (CN): 力的相对大小（箭头越长 = 力越大）。

**Flashcard 5**
Q (EN): How many forces act on a book resting on a horizontal table?
Q (CN): 静止在水平桌面上的书受到几个力？
A (EN): Two: weight (down) and normal reaction (up).
A (CN): 两个：重力（向下）和支持力（向上）。

---

## 8. Metadata / 元数据

```yaml
title:
  en: Drawing Free-body Diagrams
  cn: 绘制受力分析图
parent_topic: Free-body Diagrams
parent_hub: "[[Free-body Diagrams]]"
subject: Physics
syllabus:
  - CAIE 9702
  - Edexcel IAL
level: AS
node_type: leaf_concept
difficulty: foundation
related_leaf_nodes:
  - "[[Resolving Forces on Inclined Planes]]"
  - "[[Equilibrium Conditions]]"
prerequisites:
  - "[[Types of Force]]"
related_topics:
  - "[[Newton's Laws of Motion]]"
language: bilingual_en_cn