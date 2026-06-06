# 1. Overview / 概述

**English:**
Acceleration-Time (a-t) graphs are a fundamental tool in kinematics, showing how an object's acceleration changes over time. This sub-topic focuses on interpreting a-t graphs, understanding their shape, and extracting key information such as changes in velocity. While [[Displacement-Time Graphs]] and [[Velocity-Time Graphs]] are more commonly tested, a-t graphs provide a deeper insight into the forces acting on an object. The area under an a-t graph represents the change in velocity, making it a crucial link to [[Equations of Motion (SUVAT)]]. Mastering a-t graphs is essential for understanding the relationship between [[Displacement, Velocity and Acceleration]] and for solving complex motion problems.

**中文:**
加速度-时间（a-t）图是运动学中的基本工具，展示了物体的加速度如何随时间变化。本子知识点侧重于解读a-t图，理解其形状，并提取关键信息，例如速度的变化。虽然[[位移-时间图]]和[[速度-时间图]]更常被考察，但a-t图能更深入地洞察作用在物体上的力。a-t图下的面积代表速度的变化，这使其成为连接[[运动学方程 (SUVAT)]]的关键。掌握a-t图对于理解[[位移、速度和加速度]]之间的关系以及解决复杂的运动问题至关重要。

---

# 2. Core Definition / 核心定义

| Term (EN/CN) | Definition (EN) | Definition (CN) |
| ------------ | --------------- | --------------- |
| **Acceleration-Time Graph** / 加速度-时间图 | A graph plotting acceleration (a) on the y-axis against time (t) on the x-axis, showing how acceleration varies during motion. | 以加速度 (a) 为纵轴、时间 (t) 为横轴的图表，显示运动过程中加速度如何变化。 |
| **Constant Acceleration** / 恒定加速度 | A horizontal line on an a-t graph, indicating the acceleration does not change over time. | a-t图上的一条水平线，表示加速度不随时间变化。 |
| **Changing Acceleration** / 变化的加速度 | A non-horizontal line (sloped or curved) on an a-t graph, indicating the acceleration is increasing or decreasing. | a-t图上的一条非水平线（倾斜或弯曲），表示加速度在增加或减少。 |
| **Area Under a-t Graph** / a-t图下的面积 | The area between the graph line and the time axis, representing the change in velocity ($\Delta v$) of the object. | 图线与时间轴之间的面积，代表物体速度的变化 ($\Delta v$)。 |
| **Zero Acceleration** / 零加速度 | A line along the time axis (a=0), indicating the object is moving at constant velocity. | 沿着时间轴的线 (a=0)，表示物体以恒定速度运动。 |

---

# 3. Key Concepts / 关键概念

**English:**
The acceleration-time graph is the third type of motion graph, following [[Displacement-Time Graphs]] and [[Velocity-Time Graphs]]. Its primary purpose is to show how acceleration changes, which is directly related to the net force acting on an object (Newton's Second Law).

**Interpreting the Graph:**
*   **Horizontal Line:** A horizontal line at a constant value (e.g., a = 2 m/s²) means the object has **constant acceleration**. This is the most common scenario in A-Level physics, often seen with objects in free fall or under constant forces.
*   **Line at a=0:** This means the acceleration is zero, so the object is moving at a **constant velocity**.
*   **Sloped Line:** A sloped line means the acceleration is changing. This is called "jerk" or "rate of change of acceleration." This is less common in basic problems but appears in more complex scenarios.
*   **Negative Values:** Acceleration can be negative (deceleration). A negative value on the a-t graph means the object is slowing down (if velocity is positive) or speeding up in the negative direction.

**Key Relationship:**
The most important concept is that the **area under the a-t graph** equals the **change in velocity** ($\Delta v$). This is the integral of acceleration with respect to time:
$$ \Delta v = \int a \, dt $$
This is analogous to how the area under a v-t graph gives displacement.

**Common Pitfalls:**
*   **Confusing a-t graphs with v-t graphs:** Students often try to read velocity directly from an a-t graph. You cannot. You must calculate the area to find the change in velocity.
*   **Forgetting initial velocity:** The area gives $\Delta v$, not the final velocity. To find final velocity ($v$), you need to know the initial velocity ($u$): $v = u + \Delta v$.
*   **Ignoring sign conventions:** When calculating area, treat areas above the time axis as positive and areas below as negative. This determines whether velocity increases or decreases.

**中文:**
加速度-时间图是继[[位移-时间图]]和[[速度-时间图]]之后的第三种运动图。其主要目的是展示加速度如何变化，这与作用在物体上的合力直接相关（牛顿第二定律）。

**解读图表：**
*   **水平线：** 在恒定值处的水平线（例如 a = 2 m/s²）意味着物体具有**恒定加速度**。这是A-Level物理中最常见的情况，常见于自由落体或恒定力作用下的物体。
*   **a=0 处的线：** 这意味着加速度为零，因此物体以**恒定速度**运动。
*   **斜线：** 斜线意味着加速度在变化。这被称为“加加速度”或“加速度的变化率”。在基础问题中不太常见，但会出现在更复杂的场景中。
*   **负值：** 加速度可以是负的（减速）。a-t图上的负值意味着物体正在减速（如果速度为正）或在负方向上加速。

**关键关系：**
最重要的概念是**a-t图下的面积**等于**速度的变化** ($\Delta v$)。这是加速度对时间的积分：
$$ \Delta v = \int a \, dt $$
这类似于v-t图下的面积给出位移。

**常见误区：**
*   **混淆 a-t 图和 v-t 图：** 学生经常试图直接从a-t图中读取速度。这是不可能的。你必须计算面积才能找到速度的变化。
*   **忘记初速度：** 面积给出的是 $\Delta v$，而不是最终速度。要找到最终速度 ($v$)，你需要知道初速度 ($u$)：$v = u + \Delta v$。
*   **忽略符号约定：** 计算面积时，将时间轴上方的面积视为正，下方的面积视为负。这决定了速度是增加还是减少。

---

# 4. Formulas / 公式

The key formula for a-t graphs is the relationship between area and change in velocity:

$$ \Delta v = \text{Area under a-t graph} $$

For a rectangular area (constant acceleration):
$$ \Delta v = a \times t $$

For a triangular area (linearly changing acceleration):
$$ \Delta v = \frac{1}{2} \times \text{base} \times \text{height} $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
| ------------- | ------------ | ------------ | ----------- |
| $\Delta v$ | Change in velocity | 速度的变化 | m/s |
| $a$ | Acceleration | 加速度 | m/s² |
| $t$ | Time interval | 时间间隔 | s |

**Derivation / 推导:**
From the definition of acceleration:
$$ a = \frac{dv}{dt} $$
Rearranging:
$$ dv = a \, dt $$
Integrating both sides:
$$ \int_{u}^{v} dv = \int_{0}^{t} a \, dt $$
$$ v - u = \text{Area under a-t graph} $$
$$ \Delta v = \text{Area} $$

**Conditions / 适用条件:**
*   The formula applies for any shape of a-t graph.
*   The area must be calculated with sign (positive above axis, negative below).
*   The initial velocity ($u$) must be known to find the final velocity ($v$).

> 📷 **IMAGE PROMPT — A01: Area Under a-t Graph**
>
> **English Prompt:**
> A clean, textbook-style vector diagram showing an acceleration-time (a-t) graph. The graph has a horizontal line at a = 3 m/s² from t = 0 to t = 5 s. The area under the line is shaded in light blue, forming a rectangle. An arrow points from the shaded area to a label: "Area = Δv = 15 m/s". The axes are labeled: y-axis "a / m s⁻²" and x-axis "t / s". The graph is on a white background with a simple grid.
>
> **中文描述:**
> 一个干净、教科书风格的矢量图，显示一个加速度-时间 (a-t) 图。该图有一条从 t=0 到 t=5 秒、位于 a=3 m/s² 处的水平线。线下方的区域用浅蓝色阴影表示，形成一个矩形。一个箭头从阴影区域指向标签：“面积 = Δv = 15 m/s”。坐标轴已标注：y轴为“a / m s⁻²”，x轴为“t / s”。图表位于白色背景上，带有简单的网格。
>
> **Labels Required / 需要标注:**
> *   a = 3 m/s²
> *   t = 5 s
> *   Area = Δv = 15 m/s
>
> **Style / 风格:** Textbook vector
>
> **Exam Relevance / 考试关联:**
> This diagram is essential for understanding the core concept of a-t graphs. Exams often ask students to calculate the area to find the change in velocity.

---

# 5. Image Prompt / 图片提示

> 📷 **IMAGE PROMPT — A02: Comparing Motion Graphs**
>
> **English Prompt:**
> A side-by-side comparison of three motion graphs for the same object: a displacement-time (s-t) graph, a velocity-time (v-t) graph, and an acceleration-time (a-t) graph. The object starts from rest and accelerates uniformly (constant acceleration). The s-t graph is a parabola curving upwards. The v-t graph is a straight line with a positive slope. The a-t graph is a horizontal line at a constant positive value. Each graph is on a white background with a grid. Arrows connect corresponding points on the graphs to show the relationship. The graphs are labeled clearly.
>
> **中文描述:**
> 同一物体的三种运动图的并排比较：位移-时间 (s-t) 图、速度-时间 (v-t) 图和加速度-时间 (a-t) 图。物体从静止开始并匀加速（恒定加速度）。s-t 图是一条向上弯曲的抛物线。v-t 图是一条具有正斜率的直线。a-t 图是一条位于恒定正值处的水平线。每个图表都在白色背景上，带有网格。箭头连接图表上的对应点以显示关系。图表已清晰标注。
>
> **Labels Required / 需要标注:**
> *   s-t graph: Parabola (curved)
> *   v-t graph: Straight line (slope = a)
> *   a-t graph: Horizontal line (a = constant)
> *   "Constant Acceleration" label on a-t graph
>
> **Style / 风格:** Textbook vector
>
> **Exam Relevance / 考试关联:**
> This comparison is a common exam question. Students must be able to relate the shape of an a-t graph to the shapes of s-t and v-t graphs for the same motion.

---

# 6. Worked Example / 典型例题

### Question / 题目
**English:**
An object starts from rest and experiences an acceleration described by the a-t graph below. The graph shows a constant acceleration of 4 m/s² for the first 3 seconds, followed by a constant deceleration of -2 m/s² for the next 2 seconds.
(a) Calculate the velocity of the object at t = 3 s.
(b) Calculate the velocity of the object at t = 5 s.

**中文:**
一个物体从静止开始，经历如下a-t图所示的加速度。该图显示前3秒内恒定加速度为4 m/s²，随后2秒内恒定减速度为-2 m/s²。
(a) 计算物体在 t = 3 秒时的速度。
(b) 计算物体在 t = 5 秒时的速度。

### Solution / 解答

**(a) Velocity at t = 3 s:**
The area under the a-t graph from t=0 to t=3 s is a rectangle:
$$ \text{Area}_1 = a \times t = 4 \times 3 = 12 \text{ m/s} $$
Since the object starts from rest ($u = 0$):
$$ v_{3} = u + \Delta v = 0 + 12 = 12 \text{ m/s} $$

**(b) Velocity at t = 5 s:**
The area under the a-t graph from t=3 to t=5 s is another rectangle (but negative):
$$ \text{Area}_2 = a \times t = (-2) \times 2 = -4 \text{ m/s} $$
Total change in velocity from t=0 to t=5 s:
$$ \Delta v_{\text{total}} = \text{Area}_1 + \text{Area}_2 = 12 + (-4) = 8 \text{ m/s} $$
Therefore:
$$ v_{5} = u + \Delta v_{\text{total}} = 0 + 8 = 8 \text{ m/s} $$

### Final Answer / 最终答案
**Answer:** (a) 12 m/s, (b) 8 m/s
**答案:** (a) 12 米/秒, (b) 8 米/秒

### Quick Tip / 提示
Always remember that the area gives the **change** in velocity, not the velocity itself. You must add the initial velocity. Also, treat areas above and below the axis with opposite signs.

---

# 7. Flashcards / 闪卡

**Card 1:**
Q (EN): What does the area under an acceleration-time graph represent?
Q (CN): 加速度-时间图下的面积代表什么？
A (EN): The change in velocity ($\Delta v$).
A (CN): 速度的变化 ($\Delta v$)。

**Card 2:**
Q (EN): What does a horizontal line at a = 0 on an a-t graph indicate?
Q (CN): a-t图上 a=0 处的水平线表示什么？
A (EN): The object is moving at constant velocity (zero acceleration).
A (CN): 物体以恒定速度运动（加速度为零）。

**Card 3:**
Q (EN): If an a-t graph shows a horizontal line at a = 5 m/s² for 4 seconds, what is the change in velocity?
Q (CN): 如果一个a-t图显示在4秒内有一条位于 a=5 m/s² 的水平线，速度的变化是多少？
A (EN): $\Delta v = 5 \times 4 = 20$ m/s.
A (CN): $\Delta v = 5 \times 4 = 20$ 米/秒。

**Card 4:**
Q (EN): Can you read the instantaneous velocity directly from an a-t graph?
Q (CN): 你能直接从a-t图中读取瞬时速度吗？
A (EN): No. You must calculate the area to find the change in velocity, then add the initial velocity.
A (CN): 不能。你必须计算面积来找到速度的变化，然后加上初速度。

**Card 5:**
Q (EN): What does a negative area under an a-t graph represent?
Q (CN): a-t图下的负面积代表什么？
A (EN): A decrease in velocity (deceleration).
A (CN): 速度的减小（减速）。

---

# 8. Metadata / 元数据

```yaml
title:
  en: Acceleration-Time Graphs
  cn: 加速度-时间图
parent_topic: Motion Graphs
parent_hub: "[[Motion Graphs]]"
subject: Physics
syllabus:
  - CAIE 9702
  - Edexcel IAL
level: AS
node_type: leaf_concept
difficulty: foundation
related_leaf_nodes:
  - "[[Displacement-Time Graphs]]"
  - "[[Velocity-Time Graphs]]"
  - "[[Interpreting Gradient and Area]]"
language: bilingual_en_cn