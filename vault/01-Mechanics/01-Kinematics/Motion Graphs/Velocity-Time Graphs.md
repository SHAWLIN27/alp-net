# Velocity-Time Graphs / 速度-时间图

---

# 1. Overview / 概述

**English:**
Velocity-time graphs are one of the most powerful tools in kinematics, allowing us to visualize how an object's velocity changes over time. Unlike [[Displacement-Time Graphs]] which show position, velocity-time graphs directly reveal the object's **acceleration** (as the gradient) and **displacement** (as the area under the graph). This sub-topic is foundational for understanding [[Motion Graphs]] as a whole and directly connects to [[Equations of Motion (SUVAT)]] for solving kinematic problems. Mastering velocity-time graphs is essential for interpreting real-world motion, from cars accelerating on a highway to objects in free fall.

**中文:**
速度-时间图是运动学中最强大的工具之一，它使我们能够直观地看到物体速度随时间的变化。与显示位置的[[位移-时间图]]不同，速度-时间图直接揭示物体的**加速度**（作为梯度）和**位移**（作为图线下的面积）。本子知识点是理解整个[[运动图像]]的基础，并直接与[[运动学方程（SUVAT）]]相连，用于解决运动学问题。掌握速度-时间图对于解释现实世界中的运动至关重要，从汽车在高速公路上加速到自由落体物体。

---

# 2. Core Definition / 核心定义

| Term (EN/CN) | Definition (EN) | Definition (CN) |
| ------------ | --------------- | --------------- |
| **Velocity-Time Graph** / 速度-时间图 | A graph plotting velocity (v) on the y-axis against time (t) on the x-axis, showing how velocity changes over time. | 以速度（v）为纵轴、时间（t）为横轴的图像，显示速度随时间的变化。 |
| **Gradient** / 梯度 | The slope of the velocity-time graph, equal to the acceleration of the object. | 速度-时间图的斜率，等于物体的加速度。 |
| **Area Under Graph** / 图线下面积 | The area between the velocity-time curve and the time axis, equal to the displacement of the object. | 速度-时间曲线与时间轴之间的面积，等于物体的位移。 |
| **Constant Velocity** / 恒定速度 | A horizontal line on a velocity-time graph, indicating zero acceleration. | 速度-时间图上的水平线，表示加速度为零。 |
| **Uniform Acceleration** / 匀加速 | A straight line with constant gradient on a velocity-time graph. | 速度-时间图上具有恒定梯度的直线。 |
| **Deceleration** / 减速 | A negative gradient on a velocity-time graph, indicating velocity decreasing with time. | 速度-时间图上的负梯度，表示速度随时间减小。 |

---

# 3. Key Concepts / 关键概念

**English:**
The velocity-time graph is fundamentally different from the [[Displacement-Time Graphs]] because its gradient gives **acceleration**, not velocity. This is a critical distinction that students often confuse.

### Reading the Graph
- **Horizontal line**: Constant velocity (zero acceleration). The object moves at steady speed.
- **Straight line with positive gradient**: Uniform acceleration. The velocity increases at a constant rate.
- **Straight line with negative gradient**: Uniform deceleration. The velocity decreases at a constant rate.
- **Curved line**: Non-uniform acceleration. The gradient changes, meaning acceleration is not constant.

### Gradient = Acceleration
The gradient at any point on a velocity-time graph is:
$$ a = \frac{\Delta v}{\Delta t} = \text{gradient} $$

For a straight line, this is constant. For a curve, you must draw a tangent to find instantaneous acceleration.

### Area Under Graph = Displacement
The area between the velocity-time curve and the time axis represents **displacement**, not distance. This is because:
$$ s = \int v \, dt $$

- Area **above** the time axis = positive displacement (moving forward)
- Area **below** the time axis = negative displacement (moving backward)
- Total displacement = net area (above minus below)
- Total distance = sum of absolute areas

### Common Pitfall
A common mistake is thinking the area under a velocity-time graph gives **distance**. It gives **displacement**. For distance, you must take the absolute value of each area segment.

> 📷 **IMAGE PROMPT — VTG-01: Velocity-Time Graph Shapes**
> A clean diagram showing four different velocity-time graph shapes side by side: (1) horizontal line for constant velocity, (2) straight upward sloping line for uniform acceleration, (3) straight downward sloping line for uniform deceleration, (4) curved line for non-uniform acceleration. Each graph should have labeled axes (v on y-axis, t on x-axis) and a brief annotation explaining the motion type. Use a textbook-style vector graphic with clear gridlines.

**中文:**
速度-时间图与[[位移-时间图]]有根本区别，因为它的梯度给出的是**加速度**，而不是速度。这是学生经常混淆的关键区别。

### 读图
- **水平线**：恒定速度（加速度为零）。物体以稳定速度运动。
- **正梯度直线**：匀加速。速度以恒定速率增加。
- **负梯度直线**：匀减速。速度以恒定速率减小。
- **曲线**：非匀加速。梯度变化，意味着加速度不恒定。

### 梯度 = 加速度
速度-时间图上任意一点的梯度为：
$$ a = \frac{\Delta v}{\Delta t} = \text{梯度} $$

对于直线，这是恒定的。对于曲线，必须画切线来求瞬时加速度。

### 图线下面积 = 位移
速度-时间曲线与时间轴之间的面积代表**位移**，而不是路程。这是因为：
$$ s = \int v \, dt $$

- 时间轴**上方**的面积 = 正位移（向前运动）
- 时间轴**下方**的面积 = 负位移（向后运动）
- 总位移 = 净面积（上方减下方）
- 总路程 = 绝对面积之和

### 常见误区
一个常见错误是认为速度-时间图下的面积给出的是**路程**。它给出的是**位移**。对于路程，必须取每个面积段的绝对值。

---

# 4. Formulas / 公式

## Primary Formula: Gradient = Acceleration

$$ a = \frac{\Delta v}{\Delta t} = \frac{v_f - v_i}{t_f - t_i} $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
| ------------- | ------------ | ------------ | ----------- |
| $a$ | Acceleration | 加速度 | m s⁻² |
| $\Delta v$ | Change in velocity | 速度变化量 | m s⁻¹ |
| $\Delta t$ | Change in time | 时间变化量 | s |
| $v_f$ | Final velocity | 末速度 | m s⁻¹ |
| $v_i$ | Initial velocity | 初速度 | m s⁻¹ |

## Secondary Formula: Area = Displacement

For a rectangular area:
$$ s = v \times t $$

For a triangular area:
$$ s = \frac{1}{2} \times \text{base} \times \text{height} = \frac{1}{2} \times t \times v $$

For a trapezoidal area:
$$ s = \frac{1}{2}(v_i + v_f) \times t $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
| ------------- | ------------ | ------------ | ----------- |
| $s$ | Displacement | 位移 | m |
| $v$ | Velocity | 速度 | m s⁻¹ |
| $t$ | Time | 时间 | s |

**Derivation / 推导:**
The area under a velocity-time graph is derived from the definition of velocity:
$$ v = \frac{ds}{dt} \implies ds = v \, dt $$
Integrating both sides:
$$ s = \int v \, dt $$
This integral represents the area under the v-t curve.

**Conditions / 适用条件:**
- The gradient formula applies for **straight-line segments** (constant acceleration).
- For curved graphs, use tangents for instantaneous acceleration.
- The area formula gives **displacement**, not distance. For distance, consider absolute values.

> 📷 **IMAGE PROMPT — VTG-02: Area Under Velocity-Time Graph**
> A detailed diagram showing a velocity-time graph with a trapezoidal shape. The area should be shaded and labeled as "Displacement = Area". Include dimensions: base = Δt, heights = v_i and v_f. Show the formula s = ½(v_i + v_f)Δt written next to the shaded region. Use a clean textbook vector style with gridlines and axis labels.

---

# 5. Image Prompt / 图片提示

> 📷 **IMAGE PROMPT — VTG-03: Complete Velocity-Time Graph Analysis**
>
> **English Prompt:**
> A comprehensive educational diagram showing a multi-segment velocity-time graph for a car journey. The graph has 5 distinct segments: (1) positive gradient straight line from (0,0) to (5,20) labeled "Acceleration", (2) horizontal line from (5,20) to (15,20) labeled "Constant Velocity", (3) negative gradient straight line from (15,20) to (20,0) labeled "Deceleration", (4) negative velocity horizontal line from (20,0) to (25,-10) labeled "Reverse", (5) positive gradient from (25,-10) to (30,0) labeled "Return to Start". Each segment should have its gradient and area calculation shown in a side panel. The total displacement and total distance should be calculated at the bottom. Use a clean textbook vector style with gridlines, axis labels (v/m s⁻¹, t/s), and color-coded segments. Include a small car icon at the start point.
>
> **中文描述:**
> 一个全面的教育示意图，显示汽车旅程的多段速度-时间图。图表有5个不同的段：(1) 从(0,0)到(5,20)的正梯度直线，标注为"加速"，(2) 从(5,20)到(15,20)的水平线，标注为"匀速"，(3) 从(15,20)到(20,0)的负梯度直线，标注为"减速"，(4) 从(20,0)到(25,-10)的负速度水平线，标注为"倒车"，(5) 从(25,-10)到(30,0)的正梯度直线，标注为"返回起点"。每个段应在侧面板显示其梯度和面积计算。底部应计算总位移和总路程。使用干净的教科书矢量风格，带网格线、轴标签（v/m s⁻¹, t/s）和颜色编码的段。在起点处包含一个小汽车图标。
>
> **Labels Required / 需要标注:**
> * Segment 1: Acceleration (a = 4 m s⁻²)
> * Segment 2: Constant Velocity (a = 0 m s⁻²)
> * Segment 3: Deceleration (a = -4 m s⁻²)
> * Segment 4: Reverse (v = -10 m s⁻¹)
> * Segment 5: Return to Start (a = 2 m s⁻²)
> * Total Displacement = 175 m
> * Total Distance = 275 m
>
> **Style / 风格:** Textbook vector graphic with gridlines
>
> **Exam Relevance / 考试关联:**
> This multi-segment graph is a common exam question type where students must calculate acceleration from gradients and displacement from areas. Understanding how to handle segments above and below the axis is crucial for exam success.

---

# 6. Worked Example / 典型例题

## Example 1: Basic Gradient and Area Calculation

### Question / 题目
**English:**
A car accelerates uniformly from rest to 20 m s⁻¹ in 10 seconds, then travels at constant velocity for 15 seconds, then decelerates uniformly to rest in 5 seconds.

(a) Sketch the velocity-time graph for this journey.
(b) Calculate the acceleration during the first 10 seconds.
(c) Calculate the total displacement of the car.

**中文:**
一辆汽车从静止匀加速到20 m s⁻¹，用时10秒，然后以恒定速度行驶15秒，最后匀减速到静止，用时5秒。

(a) 画出这段旅程的速度-时间图。
(b) 计算前10秒内的加速度。
(c) 计算汽车的总位移。

### Solution / 解答

**(a) Graph / 图像:**
The graph has three segments:
- Segment 1: Straight line from (0,0) to (10,20)
- Segment 2: Horizontal line from (10,20) to (25,20)
- Segment 3: Straight line from (25,20) to (30,0)

**(b) Acceleration in first 10 seconds / 前10秒的加速度:**

$$ a = \frac{\Delta v}{\Delta t} = \frac{20 - 0}{10 - 0} = \frac{20}{10} = 2 \text{ m s}^{-2} $$

**(c) Total displacement / 总位移:**

The total displacement is the total area under the graph.

**Segment 1 (Triangle):**
$$ s_1 = \frac{1}{2} \times \text{base} \times \text{height} = \frac{1}{2} \times 10 \times 20 = 100 \text{ m} $$

**Segment 2 (Rectangle):**
$$ s_2 = \text{length} \times \text{width} = 15 \times 20 = 300 \text{ m} $$

**Segment 3 (Triangle):**
$$ s_3 = \frac{1}{2} \times 5 \times 20 = 50 \text{ m} $$

**Total displacement:**
$$ s_{\text{total}} = 100 + 300 + 50 = 450 \text{ m} $$

### Final Answer / 最终答案
**Answer:** (a) See sketch; (b) $a = 2 \text{ m s}^{-2}$; (c) $s = 450 \text{ m}$
**答案:** (a) 见草图；(b) $a = 2 \text{ m s}^{-2}$；(c) $s = 450 \text{ m}$

### Quick Tip / 提示
Always break the graph into simple shapes (triangles, rectangles, trapezoids) for area calculation. Remember that the area under a velocity-time graph gives **displacement**, not distance. If the graph goes below the time axis, subtract that area for displacement but add it for distance.

---

## Example 2: Graph with Negative Velocity

### Question / 题目
**English:**
A ball is thrown vertically upward. Its velocity-time graph shows it moving upward at 15 m s⁻¹ at t=0, reaching its highest point at t=1.5 s, then falling back down. At t=3.0 s, it returns to the starting point.

(a) What is the acceleration of the ball?
(b) Calculate the displacement at t=3.0 s.
(c) Calculate the total distance traveled by t=3.0 s.

**中文:**
一个球被竖直向上抛出。其速度-时间图显示在t=0时向上运动速度为15 m s⁻¹，在t=1.5 s时到达最高点，然后下落。在t=3.0 s时，它回到起点。

(a) 球的加速度是多少？
(b) 计算t=3.0 s时的位移。
(c) 计算到t=3.0 s时球运动的总路程。

### Solution / 解答

**(a) Acceleration / 加速度:**

The graph is a straight line from (0,15) to (1.5,0) to (3.0,-15).

$$ a = \frac{\Delta v}{\Delta t} = \frac{-15 - 15}{3.0 - 0} = \frac{-30}{3.0} = -10 \text{ m s}^{-2} $$

The negative sign indicates acceleration is downward (deceleration upward, acceleration downward).

**(b) Displacement at t=3.0 s / t=3.0 s时的位移:**

The displacement is the net area (area above axis minus area below axis).

**Area above axis (t=0 to t=1.5):**
$$ A_{\text{above}} = \frac{1}{2} \times 1.5 \times 15 = 11.25 \text{ m} $$

**Area below axis (t=1.5 to t=3.0):**
$$ A_{\text{below}} = \frac{1}{2} \times 1.5 \times (-15) = -11.25 \text{ m} $$

**Net displacement:**
$$ s = 11.25 + (-11.25) = 0 \text{ m} $$

The ball returns to the starting point, so displacement is zero.

**(c) Total distance by t=3.0 s / 到t=3.0 s时的总路程:**

Distance is the sum of absolute areas:
$$ \text{Distance} = |11.25| + |-11.25| = 11.25 + 11.25 = 22.5 \text{ m} $$

### Final Answer / 最终答案
**Answer:** (a) $a = -10 \text{ m s}^{-2}$; (b) $s = 0 \text{ m}$; (c) Distance = 22.5 m
**答案:** (a) $a = -10 \text{ m s}^{-2}$；(b) $s = 0 \text{ m}$；(c) 路程 = 22.5 m

### Quick Tip / 提示
When a velocity-time graph crosses the time axis, the object has changed direction. The area above the axis represents forward motion, and the area below represents backward motion. For displacement, subtract the negative area; for distance, add the absolute values.

---

# 7. Flashcards / 闪卡

**Flashcard 1:**
- **Q (EN):** What does the gradient of a velocity-time graph represent?
- **Q (CN):** 速度-时间图的梯度代表什么？
- **A (EN):** The gradient of a velocity-time graph represents acceleration.
- **A (CN):** 速度-时间图的梯度代表加速度。

**Flashcard 2:**
- **Q (EN):** What does the area under a velocity-time graph represent?
- **Q (CN):** 速度-时间图下的面积代表什么？
- **A (EN):** The area under a velocity-time graph represents displacement.
- **A (CN):** 速度-时间图下的面积代表位移。

**Flashcard 3:**
- **Q (EN):** What does a horizontal line on a velocity-time graph indicate?
- **Q (CN):** 速度-时间图上的水平线表示什么？
- **A (EN):** A horizontal line indicates constant velocity (zero acceleration).
- **A (CN):** 水平线表示恒定速度（加速度为零）。

**Flashcard 4:**
- **Q (EN):** How do you find instantaneous acceleration from a curved velocity-time graph?
- **Q (CN):** 如何从弯曲的速度-时间图中求瞬时加速度？
- **A (EN):** Draw a tangent to the curve at the point of interest and calculate its gradient.
- **A (CN):** 在感兴趣的点画曲线的切线，并计算其梯度。

**Flashcard 5:**
- **Q (EN):** What is the difference between displacement and distance when calculating area under a velocity-time graph?
- **Q (CN):** 在计算速度-时间图下的面积时，位移和路程有什么区别？
- **A (EN):** Displacement is the net area (above minus below the axis). Distance is the sum of absolute areas.
- **A (CN):** 位移是净面积（轴上方减下方）。路程是绝对面积之和。

---

# 8. Metadata / 元数据

```yaml
title:
  en: Velocity-Time Graphs
  cn: 速度-时间图
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
  - "[[Acceleration-Time Graphs]]"
  - "[[Interpreting Gradient and Area]]"
  - "[[Displacement, Velocity and Acceleration]]"
  - "[[Equations of Motion (SUVAT)]]"
language: bilingual_en_cn