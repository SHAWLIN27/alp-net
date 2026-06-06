# Force-Displacement Graphs / 力-位移图

---

# 1. Overview / 概述

**English:**
Force-displacement (F-x) graphs provide a powerful visual method for determining the work done by a force. When a force varies with displacement — as in stretching a spring or compressing a gas — the simple formula $W = Fs$ no longer applies directly. Instead, the area under the force-displacement graph represents the work done. This graphical approach bridges the gap between [[Definition of Work]] and real-world applications where forces are not constant. Understanding F-x graphs is essential for analyzing elastic potential energy in springs and forms the foundation for [[Kinetic Energy and Potential Energy]] concepts.

**中文:**
力-位移图（F-x图）提供了一种确定力做功的直观方法。当力随位移变化时——例如拉伸弹簧或压缩气体——简单的公式 $W = Fs$ 不再直接适用。此时，力-位移图下的面积代表所做的功。这种图形方法弥合了[[Definition of Work]]与力不恒定的实际应用之间的差距。理解F-x图对于分析弹簧中的弹性势能至关重要，并为[[Kinetic Energy and Potential Energy]]概念奠定基础。

---

# 2. Core Definition / 核心定义

| Term (EN/CN) | Definition (EN) | Definition (CN) |
| ------------ | --------------- | --------------- |
| **Force-Displacement Graph** / 力-位移图 | A graph plotting force (F) on the y-axis against displacement (s) on the x-axis, where the area under the curve equals the work done by the force. | 以力（F）为纵轴、位移（s）为横轴的图形，曲线下的面积等于力所做的功。 |
| **Area Under Graph** / 图下面积 | The region bounded by the curve, the x-axis, and vertical lines at the start and end displacements; its value represents work done. | 由曲线、x轴以及起始和终止位移处的垂直线所围成的区域；其数值代表所做的功。 |
| **Constant Force** / 恒力 | A force that does not change in magnitude over the displacement; produces a horizontal line on an F-x graph. | 在位移过程中大小不变的力；在F-x图上产生一条水平线。 |
| **Variable Force** / 变力 | A force whose magnitude changes with displacement; produces a non-horizontal curve on an F-x graph. | 大小随位移变化的力；在F-x图上产生非水平曲线。 |
| **Work Done** / 做功 | The energy transferred when a force moves an object through a displacement; equals the area under the F-x graph. | 力使物体发生位移时传递的能量；等于F-x图下的面积。 |
| **Elastic Limit** / 弹性极限 | The maximum displacement beyond which a material does not return to its original shape; relevant for spring F-x graphs. | 材料超过此位移后不再恢复原状的最大位移；与弹簧的F-x图相关。 |

---

# 3. Key Concepts / 关键概念

**English:**

### Interpreting the Area

The fundamental principle is that **work done = area under the F-x graph**. This applies to both constant and variable forces. For a constant force, the graph is a horizontal line, and the area is simply a rectangle: $W = F \times s$. For a variable force, the area must be calculated by:
- Dividing the area into geometric shapes (rectangles, triangles, trapezoids)
- Using integration (at A-Level, typically for linear relationships like springs)

### The Spring Example (Hooke's Law)

The most common A-Level application is a spring obeying [[Hooke's Law]]: $F = kx$, where $k$ is the spring constant and $x$ is extension. The F-x graph is a straight line through the origin. The area under this line is a triangle:

$$W = \frac{1}{2} \times \text{base} \times \text{height} = \frac{1}{2} \times x \times F = \frac{1}{2} k x^2$$

This work done equals the elastic potential energy stored in the spring.

### Sign Convention

Work done **by** the force is positive when the force and displacement are in the same direction. If the force opposes the displacement (e.g., friction), the area represents negative work. On an F-x graph, areas above the x-axis represent positive work; areas below represent negative work.

### Common Pitfalls

- **Confusing area with gradient**: The gradient of an F-x graph gives the spring constant $k$ (for a linear spring), not the work done.
- **Forgetting units**: Work is in joules (J), so ensure force is in newtons (N) and displacement in metres (m).
- **Ignoring direction**: Work is a scalar, but the sign matters for energy transfer.

**中文:**

### 解释面积

基本原则是：**做功 = F-x图下的面积**。这适用于恒力和变力。对于恒力，图形是一条水平线，面积就是矩形：$W = F \times s$。对于变力，面积必须通过以下方式计算：
- 将面积分割成几何形状（矩形、三角形、梯形）
- 使用积分（在A-Level中，通常用于线性关系，如弹簧）

### 弹簧示例（胡克定律）

最常见的A-Level应用是遵循[[Hooke's Law]]的弹簧：$F = kx$，其中$k$是弹簧常数，$x$是伸长量。F-x图是一条通过原点的直线。该直线下的面积是一个三角形：

$$W = \frac{1}{2} \times \text{底} \times \text{高} = \frac{1}{2} \times x \times F = \frac{1}{2} k x^2$$

所做的功等于储存在弹簧中的弹性势能。

### 符号约定

当力和位移方向相同时，力所做的功为正。如果力与位移方向相反（例如摩擦力），则面积为负功。在F-x图上，x轴上方的面积代表正功；x轴下方的面积代表负功。

### 常见误区

- **混淆面积和斜率**：F-x图的斜率给出弹簧常数$k$（对于线性弹簧），而不是所做的功。
- **忘记单位**：功的单位是焦耳（J），因此确保力的单位是牛顿（N），位移的单位是米（m）。
- **忽略方向**：功是标量，但符号对能量传递很重要。

---

# 4. Formulas / 公式

## Primary Formula

$$W = \int_{s_1}^{s_2} F \, ds \quad \text{or} \quad W = \text{Area under F-x graph}$$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
| ------------- | ------------ | ------------ | ----------- |
| $W$ | Work done | 所做的功 | J (joules) |
| $F$ | Force | 力 | N (newtons) |
| $s$ | Displacement | 位移 | m (metres) |
| $s_1, s_2$ | Initial and final displacement | 初始和最终位移 | m (metres) |

## Special Case: Constant Force

$$W = F \times \Delta s$$

Where $\Delta s = s_2 - s_1$ is the total displacement.

## Special Case: Linear Spring (Hooke's Law)

$$W = \frac{1}{2} k x^2$$

Where $x$ is extension from natural length, and $k$ is the spring constant.

**Derivation / 推导:**
For a spring obeying Hooke's Law, $F = kx$. The F-x graph is a straight line from $(0,0)$ to $(x, F)$. The area under this line is a triangle:
$$\text{Area} = \frac{1}{2} \times \text{base} \times \text{height} = \frac{1}{2} \times x \times (kx) = \frac{1}{2} k x^2$$

**Conditions / 适用条件:**
- The force must be the **net force** doing work on the object
- For springs: must be within the elastic limit
- Displacement must be in the direction of the force (or use component)

> 📷 **IMAGE PROMPT — FxG-01: Force-Displacement Graph for a Spring**
>
> **English Prompt:**
> A clean, textbook-style vector diagram showing a force-displacement (F-x) graph for a spring obeying Hooke's Law. The graph is a straight line from the origin (0,0) to point (x, F). The triangular area under the line is shaded in light blue and labeled "Work Done = ½kx²". Axes are labeled: y-axis "Force F (N)" and x-axis "Displacement x (m)". Include a small inset diagram of a spring being stretched with force F and extension x. Use a white background, black lines, and professional labeling in Arial font. Suitable for an A-Level physics textbook.
>
> **中文描述:**
> 一个清晰、教科书风格的矢量图，展示遵循胡克定律的弹簧的力-位移（F-x）图。图形是一条从原点（0,0）到点（x, F）的直线。直线下的三角形区域用浅蓝色阴影填充，并标注"做功 = ½kx²"。坐标轴标注：y轴"力 F (N)"，x轴"位移 x (m)"。包含一个小插图，显示弹簧被拉伸，标有力F和伸长量x。使用白色背景、黑色线条和Arial字体的专业标注。适合A-Level物理教科书。
>
> **Labels Required / 需要标注:**
> * "Work Done = ½kx²" inside the shaded triangle
> * "F = kx" along the line
> * Axes: "Force F (N)" and "Displacement x (m)"
> * Point coordinates: (0,0) and (x, F)
>
> **Style / 风格:** Textbook vector diagram
>
> **Exam Relevance / 考试关联:**
> This is the most common F-x graph question in A-Level exams. Students must recognize the triangular area and relate it to elastic potential energy.

---

# 5. Image Prompt / 图片提示

> 📷 **IMAGE PROMPT — FxG-02: Comparing Constant vs Variable Force Graphs**
>
> **English Prompt:**
> A side-by-side comparison diagram with two force-displacement graphs. Left graph: a horizontal line at F = 10 N from s = 0 to s = 5 m, with the rectangular area shaded in green and labeled "W = F × s = 50 J". Right graph: a diagonal line from (0,0) to (5, 10) representing a spring, with the triangular area shaded in orange and labeled "W = ½ × base × height = 25 J". Both graphs share the same axes: y-axis "Force (N)" from 0 to 12, x-axis "Displacement (m)" from 0 to 6. Below each graph, a small icon: a box being pushed by a constant force (left) and a spring being stretched (right). Clean, educational style with white background, suitable for a physics textbook.
>
> **中文描述:**
> 一个并排比较图，包含两个力-位移图。左图：从s=0到s=5 m处F=10 N的水平线，矩形区域用绿色阴影填充，标注"W = F × s = 50 J"。右图：从(0,0)到(5,10)的对角线，代表弹簧，三角形区域用橙色阴影填充，标注"W = ½ × 底 × 高 = 25 J"。两个图共享相同的坐标轴：y轴"力 (N)"从0到12，x轴"位移 (m)"从0到6。每个图下方有一个小图标：一个被恒力推动的盒子（左）和一个被拉伸的弹簧（右）。干净的教育风格，白色背景，适合物理教科书。
>
> **Labels Required / 需要标注:**
> * Left graph: "Constant Force" and "W = Fs = 50 J"
> * Right graph: "Variable Force (Spring)" and "W = ½kx² = 25 J"
> * Axes labels on both graphs
>
> **Style / 风格:** Textbook vector diagram with color coding
>
> **Exam Relevance / 考试关联:**
> Helps students distinguish between constant and variable force scenarios, a common source of confusion in exams.

---

# 6. Worked Example / 典型例题

### Example 1: Constant Force

**Question / 题目:**
**English:**
A constant force of 12 N acts on a box, moving it 4.0 m across a frictionless floor. Draw the force-displacement graph and calculate the work done.

**中文:**
一个12 N的恒力作用在一个盒子上，使其在无摩擦的地面上移动4.0 m。画出力-位移图并计算所做的功。

**Solution / 解答:**

**Step 1: Draw the graph**
The force is constant at 12 N, so the F-x graph is a horizontal line at F = 12 N from s = 0 to s = 4.0 m.

**Step 2: Calculate the area**
The area under the graph is a rectangle:
$$\text{Area} = \text{height} \times \text{width} = 12 \text{ N} \times 4.0 \text{ m} = 48 \text{ J}$$

**Step 3: State the answer**
$$W = 48 \text{ J}$$

**Final Answer / 最终答案:**
**Answer:** 48 J **答案:** 48 J

**Quick Tip / 提示:**
For constant forces, always check that the graph is a horizontal line. The area is simply $F \times \Delta s$.

---

### Example 2: Variable Force (Spring)

**Question / 题目:**
**English:**
A spring with spring constant $k = 200 \text{ N m}^{-1}$ is stretched from its natural length by 0.15 m. Calculate the work done in stretching the spring.

**中文:**
一个弹簧常数为 $k = 200 \text{ N m}^{-1}$ 的弹簧从其自然长度被拉伸0.15 m。计算拉伸弹簧所做的功。

**Solution / 解答:**

**Step 1: Identify the relationship**
The spring obeys Hooke's Law: $F = kx = 200x$

**Step 2: Draw the F-x graph**
The graph is a straight line from (0,0) to (0.15, 200 × 0.15 = 30 N).

**Step 3: Calculate the area (triangle)**
$$W = \frac{1}{2} \times \text{base} \times \text{height} = \frac{1}{2} \times 0.15 \text{ m} \times 30 \text{ N}$$
$$W = \frac{1}{2} \times 0.15 \times 30 = 2.25 \text{ J}$$

**Alternative using formula:**
$$W = \frac{1}{2} k x^2 = \frac{1}{2} \times 200 \times (0.15)^2 = \frac{1}{2} \times 200 \times 0.0225 = 2.25 \text{ J}$$

**Final Answer / 最终答案:**
**Answer:** 2.25 J **答案:** 2.25 J

**Quick Tip / 提示:**
Always use the formula $W = \frac{1}{2} k x^2$ for springs — it's faster and less error-prone than calculating the triangle area manually. But understand the graphical interpretation for exam questions that ask you to "use the graph."

---

# 7. Flashcards / 闪卡

**Flashcard 1:**
Q (EN): How do you find work done from a force-displacement graph?
Q (CN): 如何从力-位移图中找到所做的功？
A (EN): The work done equals the area under the force-displacement graph.
A (CN): 所做的功等于力-位移图下的面积。

**Flashcard 2:**
Q (EN): What shape is the area under a constant force F-x graph?
Q (CN): 恒力F-x图下的面积是什么形状？
A (EN): A rectangle: Area = F × Δs.
A (CN): 矩形：面积 = F × Δs。

**Flashcard 3:**
Q (EN): What shape is the area under a spring's F-x graph (Hooke's Law)?
Q (CN): 弹簧的F-x图（胡克定律）下的面积是什么形状？
A (EN): A triangle: Area = ½ × base × height = ½ kx².
A (CN): 三角形：面积 = ½ × 底 × 高 = ½ kx²。

**Flashcard 4:**
Q (EN): What does the gradient of a force-displacement graph represent for a spring?
Q (CN): 对于弹簧，力-位移图的斜率代表什么？
A (EN): The spring constant k (from F = kx).
A (CN): 弹簧常数k（来自F = kx）。

**Flashcard 5:**
Q (EN): What does a negative area under an F-x graph represent?
Q (CN): F-x图下的负面积代表什么？
A (EN): Work done against the force (e.g., friction), meaning energy is dissipated.
A (CN): 克服力所做的功（例如摩擦力），意味着能量被耗散。

---

# 8. Metadata / 元数据

```yaml
title:
  en: Force-Displacement Graphs
  cn: 力-位移图
parent_topic: Work Done by a Force
parent_hub: "[[Work Done by a Force]]"
subject: Physics
syllabus:
  - CAIE 9702
  - Edexcel IAL
level: AS
node_type: leaf_concept
difficulty: foundation
related_leaf_nodes:
  - "[[Definition of Work]]"
  - "[[Work Done by a Force at an Angle]]"
prerequisites:
  - "[[Scalars and Vectors]]"
  - "[[Newton's Laws of Motion]]"
related_topics:
  - "[[Kinetic Energy and Potential Energy]]"
language: bilingual_en_cn