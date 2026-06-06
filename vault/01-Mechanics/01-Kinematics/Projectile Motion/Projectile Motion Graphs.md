# 1. Overview / 概述

**English:**
Projectile motion graphs provide a powerful visual tool for understanding and analyzing the two-dimensional motion of objects under gravity. While numerical calculations using [[Equations of Motion (SUVAT)]] give precise values, graphs reveal the *relationship* between variables over time — showing how horizontal and vertical components of displacement, velocity, and acceleration evolve independently. This sub-topic focuses on interpreting and sketching the three key graph types: displacement-time, velocity-time, and acceleration-time graphs, for both the horizontal and vertical directions. Mastering these graphs is essential for linking the mathematical model to physical intuition, and it directly supports understanding of [[Time of Flight and Range]] and [[Maximum Height]].

**中文:**
抛体运动图像是理解和分析物体在重力作用下二维运动的强大视觉工具。虽然使用[[Equations of Motion (SUVAT)]]进行数值计算能给出精确值，但图像揭示了变量随时间变化的*关系*——展示了位移、速度和加速度的水平与垂直分量如何独立演变。本子知识点专注于解释和绘制三种关键图像类型：位移-时间图、速度-时间图和加速度-时间图，分别针对水平和垂直方向。掌握这些图像对于将数学模型与物理直觉联系起来至关重要，并直接支持对[[Time of Flight and Range]]和[[Maximum Height]]的理解。

---

# 2. Core Definition / 核心定义

| Term (EN/CN) | Definition (EN) | Definition (CN) |
| ------------ | --------------- | --------------- |
| **Projectile Motion Graph** / 抛体运动图像 | A graphical representation showing how one kinematic quantity (displacement, velocity, or acceleration) of a projectile changes with time, typically drawn separately for horizontal and vertical components. | 展示抛体运动的一个运动学量（位移、速度或加速度）随时间变化的图像表示，通常分别绘制水平和垂直分量。 |
| **Horizontal Component Graph** / 水平分量图像 | A graph representing the motion in the x-direction, where acceleration is zero (constant velocity) and displacement increases linearly with time. | 表示x方向运动的图像，其中加速度为零（匀速运动），位移随时间线性增加。 |
| **Vertical Component Graph** / 垂直分量图像 | A graph representing the motion in the y-direction, where acceleration is constant (g = 9.81 m/s² downward), velocity changes linearly, and displacement follows a parabolic relationship. | 表示y方向运动的图像，其中加速度恒定（g = 9.81 m/s²向下），速度线性变化，位移呈抛物线关系。 |
| **Gradient** / 斜率 | The slope of a graph at a point; on a displacement-time graph, gradient = velocity; on a velocity-time graph, gradient = acceleration. | 图像在某点的斜率；在位移-时间图上，斜率 = 速度；在速度-时间图上，斜率 = 加速度。 |
| **Area Under Graph** / 图像下方面积 | The area between the graph line and the time axis; on a velocity-time graph, area = displacement; on an acceleration-time graph, area = change in velocity. | 图像线与时间轴之间的面积；在速度-时间图上，面积 = 位移；在加速度-时间图上，面积 = 速度变化量。 |

---

# 3. Key Concepts / 关键概念

**English:**

The fundamental principle behind projectile motion graphs is **independence of perpendicular components**. The horizontal and vertical motions are completely separate, so we draw two sets of graphs for each quantity.

### Horizontal Motion (x-direction)
- **Acceleration-time graph:** A horizontal line at $a_x = 0$ (no horizontal force after launch, ignoring air resistance).
- **Velocity-time graph:** A horizontal line at $u_x = u \cos \theta$ (constant horizontal velocity).
- **Displacement-time graph:** A straight line through the origin with gradient $u_x$ (linear increase).

### Vertical Motion (y-direction)
- **Acceleration-time graph:** A horizontal line at $a_y = -g$ (constant downward acceleration).
- **Velocity-time graph:** A straight line with gradient $-g$, starting at $u_y = u \sin \theta$, crossing zero at the peak ([[Maximum Height]]), and becoming negative.
- **Displacement-time graph:** A parabola opening downward, starting at zero, rising to maximum height, then falling back to zero (if landing at same level).

### Key Relationships from Graphs
- The **gradient** of the vertical velocity-time graph gives $g$ (should be $-9.81$ m/s²).
- The **area** under the vertical velocity-time graph gives vertical displacement.
- The **time when vertical velocity = 0** on the $v_y$-t graph corresponds to the peak of the displacement-time graph and the [[Time of Flight and Range]] midpoint.

### Common Pitfalls
- **Confusing gradient and area:** Remember: gradient = rate of change (velocity or acceleration); area = accumulation (displacement or velocity change).
- **Forgetting sign conventions:** Upward is usually positive, so $g$ is negative in vertical graphs.
- **Assuming horizontal acceleration exists:** In ideal projectile motion, $a_x = 0$ always.
- **Mixing up graph shapes:** Horizontal displacement is linear, not parabolic; vertical displacement is parabolic, not linear.

**中文:**

抛体运动图像背后的基本原理是**垂直分量的独立性**。水平和垂直运动完全分离，因此我们为每个量绘制两组图像。

### 水平运动（x方向）
- **加速度-时间图：** 在 $a_x = 0$ 处的水平线（发射后无水平力，忽略空气阻力）。
- **速度-时间图：** 在 $u_x = u \cos \theta$ 处的水平线（恒定水平速度）。
- **位移-时间图：** 通过原点、斜率为 $u_x$ 的直线（线性增加）。

### 垂直运动（y方向）
- **加速度-时间图：** 在 $a_y = -g$ 处的水平线（恒定向下加速度）。
- **速度-时间图：** 斜率为 $-g$ 的直线，起始于 $u_y = u \sin \theta$，在最高点（[[Maximum Height]]）穿过零，然后变为负值。
- **位移-时间图：** 开口向下的抛物线，从零开始，上升到最大高度，然后回落到零（如果着陆在同一水平面）。

### 图像的关键关系
- 垂直速度-时间图的**斜率**给出 $g$（应为 $-9.81$ m/s²）。
- 垂直速度-时间图下的**面积**给出垂直位移。
- $v_y$-t 图上垂直速度 = 0 的时间对应于位移-时间图的最高点和[[Time of Flight and Range]]的中点。

### 常见误区
- **混淆斜率和面积：** 记住：斜率 = 变化率（速度或加速度）；面积 = 累积量（位移或速度变化）。
- **忘记符号约定：** 向上通常为正，因此垂直图像中 $g$ 为负。
- **假设存在水平加速度：** 在理想抛体运动中，$a_x = 0$ 始终成立。
- **混淆图像形状：** 水平位移是线性的，不是抛物线；垂直位移是抛物线，不是线性的。

---

# 4. Formulas / 公式

For projectile motion graphs, the key formulas are the relationships between graph features and kinematic quantities:

$$ \text{Gradient of } s\text{-}t \text{ graph} = v \quad \text{(instantaneous velocity)} $$

$$ \text{Gradient of } v\text{-}t \text{ graph} = a \quad \text{(acceleration)} $$

$$ \text{Area under } v\text{-}t \text{ graph} = \Delta s \quad \text{(displacement)} $$

$$ \text{Area under } a\text{-}t \text{ graph} = \Delta v \quad \text{(change in velocity)} $$

For the specific case of projectile motion:

$$ v_x = u \cos \theta \quad \text{(constant, so } v_x\text{-}t \text{ graph is horizontal)} $$

$$ v_y = u \sin \theta - gt \quad \text{(linear, so } v_y\text{-}t \text{ graph has gradient } -g) $$

$$ s_x = (u \cos \theta)t \quad \text{(linear, so } s_x\text{-}t \text{ graph is straight line)} $$

$$ s_y = (u \sin \theta)t - \frac{1}{2}gt^2 \quad \text{(quadratic, so } s_y\text{-}t \text{ graph is parabola)} $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
| ------------- | ------------ | ------------ | ----------- |
| $v_x$ | Horizontal component of velocity | 速度的水平分量 | m/s |
| $v_y$ | Vertical component of velocity | 速度的垂直分量 | m/s |
| $s_x$ | Horizontal displacement | 水平位移 | m |
| $s_y$ | Vertical displacement | 垂直位移 | m |
| $u$ | Initial speed | 初速度大小 | m/s |
| $\theta$ | Launch angle above horizontal | 发射角（与水平面的夹角） | ° or rad |
| $g$ | Acceleration due to gravity (9.81 m/s²) | 重力加速度 | m/s² |
| $t$ | Time elapsed | 经过的时间 | s |

**Derivation / 推导:**

The graph shapes follow directly from the [[Equations of Motion (SUVAT)]] applied independently to horizontal and vertical components:

1. **Horizontal:** $a_x = 0$, so $v_x = u_x$ (constant) and $s_x = u_x t$ (linear).
2. **Vertical:** $a_y = -g$, so $v_y = u_y - gt$ (linear with slope $-g$) and $s_y = u_y t - \frac{1}{2}gt^2$ (quadratic).

**Conditions / 适用条件:**
- Ideal projectile motion (no air resistance)
- Uniform gravitational field ($g$ constant)
- Launch and landing at same vertical level (for symmetric graphs)
- Upward direction taken as positive

> 📷 **IMAGE PROMPT — GRAPH-01: Complete Set of Projectile Motion Graphs**
>
> **English Prompt:**
> A clean, textbook-style diagram showing six graphs arranged in a 2×3 grid. Top row: horizontal component graphs (s_x-t, v_x-t, a_x-t). Bottom row: vertical component graphs (s_y-t, v_y-t, a_y-t). Each graph has labeled axes with units (s in m, v in m/s, a in m/s², t in s). The horizontal graphs show: s_x-t is a straight line through origin with positive slope; v_x-t is a horizontal line at positive value; a_x-t is a horizontal line at zero. The vertical graphs show: s_y-t is a downward-opening parabola starting at origin, peaking at t=T/2, returning to zero at t=T; v_y-t is a straight line starting at positive value, crossing zero at t=T/2, reaching negative value at t=T; a_y-t is a horizontal line at -9.81. All graphs share the same time axis from t=0 to t=T. Use a white background, black lines, blue for horizontal, red for vertical. Include gridlines and key points marked (e.g., peak, zero crossings).
>
> **中文描述:**
> 一个干净、教科书风格的图表，显示排列成2×3网格的六个图像。顶行：水平分量图像（s_x-t, v_x-t, a_x-t）。底行：垂直分量图像（s_y-t, v_y-t, a_y-t）。每个图像都有带单位的标注轴（s单位为m，v单位为m/s，a单位为m/s²，t单位为s）。水平图像显示：s_x-t是通过原点、斜率为正的直线；v_x-t是在正值处的水平线；a_x-t是在零处的水平线。垂直图像显示：s_y-t是开口向下的抛物线，从原点开始，在t=T/2处达到峰值，在t=T处回到零；v_y-t是直线，从正值开始，在t=T/2处穿过零，在t=T处达到负值；a_y-t是在-9.81处的水平线。所有图像共享从t=0到t=T的时间轴。使用白色背景、黑色线条，水平方向用蓝色，垂直方向用红色。包括网格线和标记的关键点（例如，峰值、零交叉点）。
>
> **Labels Required / 需要标注:**
> * Each graph title: "Horizontal Displacement", "Horizontal Velocity", "Horizontal Acceleration", "Vertical Displacement", "Vertical Velocity", "Vertical Acceleration"
> * Axes with units: s (m), v (m/s), a (m/s²), t (s)
> * Key points: (0,0), peak of s_y, zero crossing of v_y, T (time of flight)
> * Gradient labels on v_y-t: "-g"
>
> **Style / 风格:** Textbook vector diagram, clean and precise
>
> **Exam Relevance / 考试关联:**
> This is the most common exam question type for this sub-topic — students must be able to sketch and interpret all six graphs. Many exam questions ask to identify which graph corresponds to which component.

---

# 5. Image Prompt / 图片提示

> 📷 **IMAGE PROMPT — GRAPH-02: Interpreting Gradient and Area on v_y-t Graph**
>
> **English Prompt:**
> A single, large velocity-time graph for the vertical component of a projectile. The graph is a straight line from (0, u_y) to (T, -u_y), crossing the time axis at (T/2, 0). Two visual annotations: (1) A right triangle drawn between two points on the line, with the vertical side labeled "Δv_y" and horizontal side labeled "Δt", and the slope labeled "gradient = -g = -9.81 m/s²". (2) The area under the line from t=0 to t=T/2 is shaded in light blue, labeled "Area = Δs_y = maximum height". The area above the line from t=T/2 to t=T is shaded in light red, labeled "Area = Δs_y = -maximum height". Include a small note: "Net area = 0 (returns to launch height)". Use a clean white background, black axes, red line, blue and red shading.
>
> **中文描述:**
> 一个单一的、大的垂直分量速度-时间图。图像是一条从(0, u_y)到(T, -u_y)的直线，在(T/2, 0)处穿过时间轴。两个视觉注释：(1) 在线上两点之间画一个直角三角形，垂直边标注"Δv_y"，水平边标注"Δt"，斜率标注"gradient = -g = -9.81 m/s²"。(2) 从t=0到t=T/2的线下区域用浅蓝色阴影，标注"Area = Δs_y = maximum height"。从t=T/2到t=T的线上区域用浅红色阴影，标注"Area = Δs_y = -maximum height"。包含一个小注释："Net area = 0 (returns to launch height)"。使用干净的白色背景、黑色坐标轴、红色线条、蓝色和红色阴影。
>
> **Labels Required / 需要标注:**
> * Axes: v_y (m/s), t (s)
> * Points: (0, u_y), (T/2, 0), (T, -u_y)
> * Gradient annotation: "gradient = -g = -9.81 m/s²"
> * Area annotations: "Area = maximum height" and "Area = -maximum height"
> * Note: "Net area = 0"
>
> **Style / 风格:** Textbook vector diagram with clear annotations
>
> **Exam Relevance / 考试关联:**
> This directly tests the two key skills: calculating g from gradient and finding displacement from area. Common exam questions ask: "Use the graph to determine g" or "Use the graph to find the maximum height."

---

# 6. Worked Example / 典型例题

### Example 1: Interpreting a Vertical Velocity-Time Graph

### Question / 题目
**English:**
A projectile is launched from ground level. The graph below shows the vertical component of its velocity against time.

[Imagine a v_y-t graph: straight line from (0, 15.0) to (3.06, -15.0), crossing t-axis at (1.53, 0)]

(a) Determine the acceleration due to gravity from the graph.
(b) Calculate the maximum height reached by the projectile.
(c) Find the total time of flight.

**中文:**
一个抛体从地面发射。下图显示了其速度的垂直分量随时间的变化。

[想象一个 v_y-t 图：从 (0, 15.0) 到 (3.06, -15.0) 的直线，在 (1.53, 0) 处穿过 t 轴]

(a) 从图像中确定重力加速度。
(b) 计算抛体达到的最大高度。
(c) 求总飞行时间。

### Solution / 解答

**(a) Acceleration from gradient**

The gradient of a v-t graph gives acceleration.

$$ \text{gradient} = \frac{\Delta v_y}{\Delta t} = \frac{-15.0 - 15.0}{3.06 - 0} = \frac{-30.0}{3.06} = -9.80 \text{ m/s}^2 $$

**Answer:** $g = 9.80 \text{ m/s}^2$ (magnitude) **答案:** $g = 9.80 \text{ m/s}^2$（大小）

**(b) Maximum height from area**

The area under the v_y-t graph from t=0 to t=1.53 s gives the vertical displacement (maximum height).

$$ \text{Area} = \frac{1}{2} \times \text{base} \times \text{height} = \frac{1}{2} \times 1.53 \times 15.0 = 11.475 \text{ m} $$

**Answer:** Maximum height = 11.5 m (3 s.f.) **答案:** 最大高度 = 11.5 m (3位有效数字)

**(c) Total time of flight**

The graph shows the projectile returns to launch height at t = 3.06 s (where v_y = -15.0 m/s, equal and opposite to initial v_y).

**Answer:** Time of flight = 3.06 s **答案:** 飞行时间 = 3.06 s

### Quick Tip / 提示
**English:** On a v_y-t graph, the time when the line crosses the t-axis (v_y = 0) is exactly half the total time of flight for symmetric motion. The area above the axis equals the area below the axis (net displacement = 0).

**中文:** 在 v_y-t 图上，线与 t 轴相交（v_y = 0）的时间恰好是对称运动总飞行时间的一半。轴上方面积等于轴下方面积（净位移 = 0）。

---

### Example 2: Sketching Graphs from Given Data

### Question / 题目
**English:**
A ball is kicked from ground level with an initial speed of 20.0 m/s at an angle of 30° above the horizontal. Sketch the following graphs for the motion from launch until it returns to ground level:
(a) Horizontal displacement against time
(b) Vertical velocity against time

**中文:**
一个球以 20.0 m/s 的初速度、与水平面成 30° 角从地面踢出。绘制从发射到返回地面整个运动过程的以下图像：
(a) 水平位移随时间变化
(b) 垂直速度随时间变化

### Solution / 解答

First, calculate the components:

$$ u_x = 20.0 \cos 30° = 20.0 \times 0.866 = 17.32 \text{ m/s} $$
$$ u_y = 20.0 \sin 30° = 20.0 \times 0.500 = 10.0 \text{ m/s} $$

Time of flight: $T = \frac{2u_y}{g} = \frac{2 \times 10.0}{9.81} = 2.04 \text{ s}$

**(a) Horizontal displacement-time graph:**
- Straight line through origin
- Gradient = $u_x = 17.32$ m/s
- At $t = T = 2.04$ s, $s_x = 17.32 \times 2.04 = 35.3$ m

**(b) Vertical velocity-time graph:**
- Straight line from (0, 10.0) to (2.04, -10.0)
- Gradient = $-g = -9.81$ m/s²
- Crosses t-axis at $t = \frac{u_y}{g} = 1.02$ s

### Final Answer / 最终答案
**Answer:** See sketches above. **答案:** 见上方草图。

### Quick Tip / 提示
**English:** Always calculate the time of flight first — it gives you the endpoint for all graphs. For horizontal displacement, the graph is always linear; for vertical velocity, it's always linear with slope -g.

**中文:** 始终先计算飞行时间——它给出了所有图像的终点。对于水平位移，图像始终是线性的；对于垂直速度，图像始终是斜率为 -g 的线性。

---

# 7. Flashcards / 闪卡

**Flashcard 1**
Q (EN): What is the shape of the horizontal displacement-time graph for a projectile?
Q (CN): 抛体运动的水平位移-时间图是什么形状？
A (EN): A straight line through the origin with positive gradient (constant horizontal velocity).
A (CN): 一条通过原点、斜率为正的直线（恒定水平速度）。

**Flashcard 2**
Q (EN): What does the gradient of a vertical velocity-time graph represent?
Q (CN): 垂直速度-时间图的斜率代表什么？
A (EN): The acceleration due to gravity (g = 9.81 m/s² downward, so gradient = -g).
A (CN): 重力加速度（g = 9.81 m/s² 向下，因此斜率 = -g）。

**Flashcard 3**
Q (EN): How can you find the maximum height from a vertical velocity-time graph?
Q (CN): 如何从垂直速度-时间图中找到最大高度？
A (EN): Calculate the area under the graph from t=0 to the time when v_y = 0 (the peak).
A (CN): 计算从 t=0 到 v_y = 0（最高点）时刻的图像下方面积。

**Flashcard 4**
Q (EN): What is the shape of the vertical acceleration-time graph for a projectile?
Q (CN): 抛体运动的垂直加速度-时间图是什么形状？
A (EN): A horizontal line at a_y = -g (constant downward acceleration of 9.81 m/s²).
A (CN): 在 a_y = -g 处的水平线（恒定向下加速度 9.81 m/s²）。

**Flashcard 5**
Q (EN): On a vertical velocity-time graph, what is the significance of the time when the line crosses the t-axis?
Q (CN): 在垂直速度-时间图上，线与 t 轴相交的时间有什么意义？
A (EN): It is the time to reach maximum height, which is exactly half the total time of flight for symmetric motion.
A (CN): 这是达到最大高度的时间，对于对称运动来说恰好是总飞行时间的一半。

---

# 8. Metadata / 元数据

```yaml
title:
  en: Projectile Motion Graphs
  cn: 抛体运动图像
parent_topic: Projectile Motion
parent_hub: "[[Projectile Motion]]"
subject: Physics
syllabus:
  - CAIE 9702
  - Edexcel IAL
level: AS
node_type: leaf_concept
difficulty: advanced
related_leaf_nodes:
  - "[[Horizontal and Vertical Components]]"
  - "[[Time of Flight and Range]]"
  - "[[Maximum Height]]"
prerequisites:
  - "[[Scalars and Vectors]]"
  - "[[Equations of Motion (SUVAT)]]"
related_topics:
  - "[[Newton's Laws of Motion]]"
language: bilingual_en_cn