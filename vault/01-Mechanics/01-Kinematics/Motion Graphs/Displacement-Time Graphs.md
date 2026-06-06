# 1. Overview / 概述

**English:**
A displacement-time graph (s-t graph) is one of the most fundamental tools in kinematics. It shows how an object's displacement from a fixed point changes over time. The shape of the graph tells you everything about the object's motion — whether it's stationary, moving at constant velocity, or accelerating. This sub-topic is the foundation for understanding [[Velocity-Time Graphs]] and [[Acceleration-Time Graphs]], as the gradient of an s-t graph gives velocity. Mastering s-t graphs is essential for interpreting real-world motion and solving problems in [[Equations of Motion (SUVAT)]].

**中文:**
位移-时间图（s-t图）是运动学中最基本的工具之一。它展示了物体相对于固定点的位移随时间的变化。图的形状告诉你关于物体运动的一切——它是静止的、匀速运动还是加速运动。这个子知识点是理解[[Velocity-Time Graphs]]和[[Acceleration-Time Graphs]]的基础，因为s-t图的斜率给出了速度。掌握s-t图对于解释现实世界中的运动和解决[[Equations of Motion (SUVAT)]]中的问题至关重要。

---

# 2. Core Definition / 核心定义

| Term (EN/CN) | Definition (EN) | Definition (CN) |
| ------------ | --------------- | --------------- |
| **Displacement-Time Graph** / 位移-时间图 | A graph plotting displacement (s) on the y-axis against time (t) on the x-axis, showing how position changes over time. | 以位移(s)为纵轴、时间(t)为横轴的图，显示位置随时间的变化。 |
| **Gradient** / 斜率 | The slope of the tangent to the curve at any point, equal to the instantaneous velocity. | 曲线上任意一点的切线斜率，等于瞬时速度。 |
| **Stationary** / 静止 | When the displacement does not change with time, shown as a horizontal line on the s-t graph. | 当位移不随时间变化时，在s-t图上显示为水平线。 |
| **Constant Velocity** / 匀速 | When displacement changes linearly with time, shown as a straight line with constant gradient. | 当位移随时间线性变化时，显示为具有恒定斜率的直线。 |
| **Accelerating** / 加速 | When the gradient of the s-t graph changes over time, shown as a curved line. | 当s-t图的斜率随时间变化时，显示为曲线。 |
| **Instantaneous Velocity** / 瞬时速度 | The velocity at a specific instant, found by drawing a tangent to the curve at that point and calculating its gradient. | 在特定时刻的速度，通过在该点画切线并计算其斜率得到。 |

---

# 3. Key Concepts / 关键概念

**English:**
The displacement-time graph is your first window into [[Displacement, Velocity and Acceleration]]. Here's how to interpret it:

1. **Stationary Object**: A horizontal line means the object is not moving. The displacement remains constant over time. For example, a car stopped at a traffic light.

2. **Constant Velocity**: A straight line with a constant gradient means the object is moving at constant velocity. The steeper the line, the faster the speed. A positive gradient means motion in the positive direction; a negative gradient means motion in the negative direction.

3. **Accelerating Object**: A curved line means the velocity is changing. If the curve is getting steeper (concave up), the object is speeding up. If the curve is flattening (concave down), the object is slowing down.

4. **Finding Velocity**: The gradient of the s-t graph at any point gives the instantaneous velocity. For a straight line, this is simply $\frac{\Delta s}{\Delta t}$. For a curve, you must draw a tangent line and calculate its gradient.

5. **Common Pitfall**: Students often confuse displacement with distance. An s-t graph can show negative displacement (if the object moves backwards relative to the starting point), but distance is always positive. Also, a curved s-t graph does NOT mean the path is curved — it means the velocity is changing.

**中文:**
位移-时间图是你理解[[Displacement, Velocity and Acceleration]]的第一个窗口。以下是解读方法：

1. **静止物体**：水平线意味着物体没有移动。位移随时间保持不变。例如，在红绿灯前停下的汽车。

2. **匀速运动**：具有恒定斜率的直线意味着物体以恒定速度运动。线越陡，速度越快。正斜率表示沿正方向运动；负斜率表示沿负方向运动。

3. **加速物体**：曲线意味着速度在变化。如果曲线变得越来越陡（凹向上），物体在加速。如果曲线变平（凹向下），物体在减速。

4. **求速度**：s-t图上任意一点的斜率给出瞬时速度。对于直线，这简单地是$\frac{\Delta s}{\Delta t}$。对于曲线，你必须画一条切线并计算其斜率。

5. **常见错误**：学生经常混淆位移和距离。s-t图可以显示负位移（如果物体相对于起点向后移动），但距离总是正的。另外，弯曲的s-t图并不意味着路径是弯曲的——它意味着速度在变化。

---

# 4. Formulas / 公式

The key formula for displacement-time graphs is the gradient calculation:

$$ \text{velocity} = \frac{\Delta s}{\Delta t} = \frac{s_2 - s_1}{t_2 - t_1} $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
| ------------- | ------------ | ------------ | ----------- |
| $v$ | velocity | 速度 | m/s |
| $\Delta s$ | change in displacement | 位移变化量 | m |
| $\Delta t$ | change in time | 时间变化量 | s |
| $s_1, s_2$ | initial and final displacement | 初始和最终位移 | m |
| $t_1, t_2$ | initial and final time | 初始和最终时间 | s |

**Derivation / 推导:**
The gradient of a straight line is defined as the ratio of vertical change to horizontal change. For an s-t graph, the vertical axis is displacement (s) and the horizontal axis is time (t), so:

$$ \text{gradient} = \frac{\text{rise}}{\text{run}} = \frac{\Delta s}{\Delta t} = v $$

This is the definition of average velocity for a straight line, or instantaneous velocity when using a tangent.

**Conditions / 适用条件:**
- For average velocity: the formula works for any straight line segment between two points.
- For instantaneous velocity: the tangent must be drawn accurately at the exact point of interest.
- The graph must have displacement on the y-axis and time on the x-axis.

> 📷 **IMAGE PROMPT — S-T-GRADIENT: Gradient of Displacement-Time Graph**
>
> **English Prompt:**
> A clean, textbook-style vector diagram showing a displacement-time graph with three distinct sections. Left section: a horizontal line labeled "Stationary" with gradient = 0. Middle section: a straight diagonal line labeled "Constant Velocity" with a right triangle showing Δs and Δt, and the formula v = Δs/Δt. Right section: a curved line (concave up) labeled "Accelerating" with a tangent line drawn at one point, showing how to find instantaneous velocity. The axes are labeled "Displacement (s) / m" and "Time (t) / s". Use a clean white background with blue lines and black labels. Include gridlines for clarity.
>
> **中文描述:**
> 一个干净的教科书风格矢量图，显示具有三个不同部分的位移-时间图。左侧部分：标有"静止"的水平线，斜率为0。中间部分：标有"匀速"的直线对角线，带有一个显示Δs和Δt的直角三角形，以及公式v = Δs/Δt。右侧部分：标有"加速"的曲线（凹向上），在一点处画有切线，显示如何求瞬时速度。坐标轴标有"位移(s)/m"和"时间(t)/s"。使用干净的白色背景，蓝色线条和黑色标签。包含网格线以便清晰。
>
> **Labels Required / 需要标注:**
> * Stationary (静止) — gradient = 0
> * Constant Velocity (匀速) — v = Δs/Δt
> * Accelerating (加速) — tangent for instantaneous velocity
> * Δs, Δt on the triangle
>
> **Style / 风格:** Textbook vector diagram
>
> **Exam Relevance / 考试关联:**
> This diagram is essential for understanding how to read s-t graphs in exams. Students must be able to identify stationary, constant velocity, and accelerating sections, and calculate gradients.

---

# 5. Image Prompt / 图片提示

> 📷 **IMAGE PROMPT — S-T-EXAMPLE: Real-World Displacement-Time Graph**
>
> **English Prompt:**
> A detailed displacement-time graph showing the motion of a person walking from home to a shop and back. The graph has three clear sections: (1) A straight diagonal line from (0,0) to (100, 500) representing walking to the shop at constant velocity. (2) A horizontal line from (100, 500) to (200, 500) representing 100 seconds stationary at the shop. (3) A straight diagonal line from (200, 500) to (350, 0) representing walking back home at constant velocity (negative gradient). The axes are labeled "Displacement from home (s) / m" and "Time (t) / s". Key points are marked with dots and labeled with coordinates. Include a small icon of a person and a house at the origin. Use a clean, modern textbook style with a light blue background and dark blue lines. Add gridlines and a title: "Displacement-Time Graph: Walking to the Shop and Back".
>
> **中文描述:**
> 一个详细的位移-时间图，显示一个人从家走到商店再返回的运动。图有三个清晰的部分：(1) 从(0,0)到(100,500)的直线对角线，表示以匀速走到商店。(2) 从(100,500)到(200,500)的水平线，表示在商店静止100秒。(3) 从(200,500)到(350,0)的直线对角线，表示以匀速走回家（负斜率）。坐标轴标有"离家位移(s)/m"和"时间(t)/s"。关键点用点标记并标有坐标。包括一个人和原点处房子的图标。使用干净的现代教科书风格，浅蓝色背景和深蓝色线条。添加网格线和标题："位移-时间图：走到商店再返回"。
>
> **Labels Required / 需要标注:**
> * Walking to shop (走向商店) — positive gradient
> * At shop (在商店) — gradient = 0
> * Walking back (走回家) — negative gradient
> * Coordinates of key points: (0,0), (100,500), (200,500), (350,0)
>
> **Style / 风格:** Modern textbook vector illustration
>
> **Exam Relevance / 考试关联:**
> This real-world example is commonly used in exam questions. Students must be able to calculate velocities from each section and understand the meaning of the horizontal section.

---

# 6. Worked Example / 典型例题

### Question / 题目
**English:**
A cyclist travels along a straight road. The displacement-time graph for the journey is shown below. The graph consists of three straight line segments:
- From t = 0 to t = 20 s, the displacement increases from 0 m to 100 m.
- From t = 20 s to t = 40 s, the displacement remains constant at 100 m.
- From t = 40 s to t = 60 s, the displacement decreases from 100 m to 0 m.

(a) Calculate the velocity during the first 20 seconds.
(b) Describe the motion between t = 20 s and t = 40 s.
(c) Calculate the velocity during the last 20 seconds.

**中文:**
一名骑自行车的人沿直线道路行驶。行程的位移-时间图如下所示。图由三段直线段组成：
- 从t = 0到t = 20秒，位移从0米增加到100米。
- 从t = 20秒到t = 40秒，位移保持在100米不变。
- 从t = 40秒到t = 60秒，位移从100米减少到0米。

(a) 计算前20秒内的速度。
(b) 描述t = 20秒到t = 40秒之间的运动。
(c) 计算最后20秒内的速度。

### Solution / 解答

**(a)** Velocity = gradient of first section:
$$ v = \frac{\Delta s}{\Delta t} = \frac{100 - 0}{20 - 0} = \frac{100}{20} = 5 \text{ m/s} $$

**(b)** Between t = 20 s and t = 40 s, the displacement is constant at 100 m. The cyclist is stationary (not moving). The gradient is zero, so velocity = 0 m/s.

**(c)** Velocity = gradient of third section:
$$ v = \frac{\Delta s}{\Delta t} = \frac{0 - 100}{60 - 40} = \frac{-100}{20} = -5 \text{ m/s} $$

The negative sign indicates the cyclist is moving in the opposite direction (back towards the starting point).

### Final Answer / 最终答案
**Answer:**
(a) 5 m/s
(b) Stationary (velocity = 0 m/s)
(c) -5 m/s (moving in opposite direction)

**答案:**
(a) 5米/秒
(b) 静止（速度 = 0米/秒）
(c) -5米/秒（向相反方向运动）

### Quick Tip / 提示
**English:** Always include the sign when giving velocity from an s-t graph. A negative gradient means motion in the negative direction. Also, remember that a horizontal line means zero velocity, not "no displacement" — the object could be far from the starting point but stationary.

**中文:** 从s-t图给出速度时，始终包含符号。负斜率表示沿负方向运动。另外，记住水平线意味着速度为零，而不是"没有位移"——物体可能离起点很远但静止。

---

# 7. Flashcards / 闪卡

**Q (EN):** What does the gradient of a displacement-time graph represent?
**Q (CN):** 位移-时间图的斜率代表什么？
**A (EN):** The gradient represents the velocity of the object.
**A (CN):** 斜率代表物体的速度。

---

**Q (EN):** What does a horizontal line on a displacement-time graph indicate?
**Q (CN):** 位移-时间图上的水平线表示什么？
**A (EN):** A horizontal line indicates the object is stationary (velocity = 0).
**A (CN):** 水平线表示物体静止（速度 = 0）。

---

**Q (EN):** How do you find instantaneous velocity from a curved displacement-time graph?
**Q (CN):** 如何从弯曲的位移-时间图中找到瞬时速度？
**A (EN):** Draw a tangent to the curve at the point of interest and calculate its gradient.
**A (CN):** 在感兴趣的点画一条曲线的切线，并计算其斜率。

---

**Q (EN):** What does a negative gradient on a displacement-time graph mean?
**Q (CN):** 位移-时间图上的负斜率意味着什么？
**A (EN):** A negative gradient means the object is moving in the negative direction (backwards relative to the starting point).
**A (CN):** 负斜率意味着物体沿负方向运动（相对于起点向后）。

---

**Q (EN):** If a displacement-time graph is curved and getting steeper, what is happening to the object?
**Q (CN):** 如果位移-时间图是弯曲的且越来越陡，物体正在发生什么？
**A (EN):** The object is accelerating (speeding up), as the gradient (velocity) is increasing.
**A (CN):** 物体正在加速（加速），因为斜率（速度）在增加。

---

# 8. Metadata / 元数据

```yaml
title:
  en: Displacement-Time Graphs
  cn: 位移-时间图
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
  - "[[Velocity-Time Graphs]]"
  - "[[Acceleration-Time Graphs]]"
  - "[[Interpreting Gradient and Area]]"
  - "[[Displacement, Velocity and Acceleration]]"
  - "[[Equations of Motion (SUVAT)]]"
language: bilingual_en_cn