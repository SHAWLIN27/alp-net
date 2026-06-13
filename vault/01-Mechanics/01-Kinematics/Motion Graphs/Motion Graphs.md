# 1. Overview / 概述

**English:**
Motion graphs are a fundamental tool in kinematics that allow physicists to visualize and analyze the motion of objects without using complex equations. This topic covers three primary types of graphs: displacement-time (s-t) graphs, velocity-time (v-t) graphs, and acceleration-time (a-t) graphs. The key skills involve interpreting the gradient and area under these graphs to extract information about an object's motion.

In the context of Cambridge 9702 and Edexcel IAL A-Level Physics, motion graphs are essential because they form the foundation for understanding [[Equations of Motion (SUVAT)]] and more advanced topics like projectile motion and simple harmonic motion. These graphs appear in both multiple-choice and structured questions, often requiring students to calculate instantaneous values, describe motion in words, or sketch graphs from given data.

Real-world applications include analyzing vehicle crash test data (velocity-time graphs), designing roller coasters (acceleration profiles), and monitoring athlete performance in sports science. In engineering, motion graphs are used to optimize machinery performance and in traffic flow analysis.

**中文：**
运动图像是运动学中的基础工具，使物理学家能够直观地观察和分析物体的运动，而无需使用复杂的方程。本主题涵盖三种主要图像类型：位移-时间图（s-t图）、速度-时间图（v-t图）和加速度-时间图（a-t图）。关键技能包括解释这些图像的斜率和面积，以提取有关物体运动的信息。

在剑桥9702和爱德思IAL A-Level物理的背景下，运动图像至关重要，因为它们构成了理解[[运动学方程（SUVAT）]]以及更高级主题（如抛体运动和简谐运动）的基础。这些图像出现在选择题和结构化问题中，通常要求学生计算瞬时值、用语言描述运动或根据给定数据绘制图像。

实际应用包括分析车辆碰撞测试数据（速度-时间图）、设计过山车（加速度曲线）以及监测运动科学中的运动员表现。在工程学中，运动图像用于优化机械性能和交通流量分析。

---

# 2. Syllabus Learning Objectives / 考纲学习目标

| CAIE 9702 | Edexcel IAL |
|-----------|-------------|
| 3.1(j): interpret displacement-time and velocity-time graphs for motion in a straight line | 1.5: Use the equations of motion for constant acceleration in a straight line, including the motion of bodies falling in a uniform gravitational field without air resistance |
| 3.1(j): determine displacement, velocity, and acceleration from graphs | 1.6: Draw and interpret displacement-time, velocity-time, and acceleration-time graphs |
| 3.1(j): understand the significance of gradient and area under graphs | 1.7: Use the gradient of a displacement-time graph to find velocity, and the gradient of a velocity-time graph to find acceleration |
| 3.1(j): sketch graphs for given motion scenarios | 1.8: Use the area under a velocity-time graph to find displacement |

**Examiner Expectations / 考官期望:**

**English:**
- Students must be able to distinguish between displacement-time and distance-time graphs
- For velocity-time graphs, both gradient (acceleration) and area (displacement) are examinable
- Students should be able to sketch graphs from verbal descriptions of motion
- Understanding the difference between instantaneous and average values from graphs is critical
- Edexcel specifically requires using graphs to solve problems involving falling bodies under gravity

**中文：**
- 学生必须能够区分位移-时间图和距离-时间图
- 对于速度-时间图，斜率（加速度）和面积（位移）都是可考的
- 学生应能够根据口头描述的运动绘制图像草图
- 理解从图像中获取瞬时值和平均值的区别至关重要
- 爱德思特别要求使用图像解决涉及重力下落物体的问题

> 📋 **CIE Only:** CAIE 9702 specifically tests the ability to interpret non-linear graphs (curved lines) and calculate instantaneous values using tangents.
>
> 📋 **Edexcel Only:** Edexcel IAL requires students to use motion graphs in conjunction with the [[Equations of Motion (SUVAT)]] for problem-solving, particularly for free-fall scenarios.

---

# 3. Core Definitions / 核心定义

| Term (EN/CN) | Definition (EN) | Definition (CN) | Common Mistakes / 常见错误 |
|--------------|-----------------|-----------------|---------------------------|
| [[Displacement-Time Graphs]] / 位移-时间图 | A graph showing how the position of an object changes with time, with displacement on the y-axis and time on the x-axis | 显示物体位置随时间变化的图像，纵轴为位移，横轴为时间 | Confusing displacement with distance; forgetting that displacement can be negative |
| [[Velocity-Time Graphs]] / 速度-时间图 | A graph showing how the velocity of an object changes with time, with velocity on the y-axis and time on the x-axis | 显示物体速度随时间变化的图像，纵轴为速度，横轴为时间 | Thinking the area gives distance instead of displacement; forgetting sign conventions |
| [[Acceleration-Time Graphs]] / 加速度-时间图 | A graph showing how the acceleration of an object changes with time, with acceleration on the y-axis and time on the x-axis | 显示物体加速度随时间变化的图像，纵轴为加速度，横轴为时间 | Confusing constant acceleration with zero acceleration |
| [[Interpreting Gradient and Area]] / 解释斜率和面积 | The gradient of a displacement-time graph gives velocity; the gradient of a velocity-time graph gives acceleration; the area under a velocity-time graph gives displacement | 位移-时间图的斜率给出速度；速度-时间图的斜率给出加速度；速度-时间图下的面积给出位移 | Using gradient when area is needed, or vice versa; incorrect units |
| Instantaneous Velocity / 瞬时速度 | The velocity at a specific instant in time, found from the gradient of a tangent to a displacement-time graph | 在特定时刻的速度，通过位移-时间图上切线的斜率求得 | Using average gradient instead of tangent gradient |
| Average Velocity / 平均速度 | Total displacement divided by total time, found from the straight line between two points on a displacement-time graph | 总位移除以总时间，通过位移-时间图上两点之间的直线求得 | Confusing with average speed (total distance/total time) |

---

# 4. Key Concepts Explained / 关键概念详解

## 4.1 Displacement-Time Graphs / 位移-时间图

### Explanation / 解释
**English:**
A [[Displacement-Time Graphs|displacement-time graph]] plots the position of an object along a straight line against time. The y-axis represents displacement (s) measured in metres (m), and the x-axis represents time (t) measured in seconds (s). The shape of the graph reveals the nature of the motion:

- **Straight line with positive gradient:** Constant velocity in the positive direction
- **Straight line with negative gradient:** Constant velocity in the negative direction
- **Horizontal line:** Object is stationary (zero velocity)
- **Curved line (parabolic):** Changing velocity (acceleration or deceleration)
- **Curve getting steeper:** Increasing velocity (acceleration)
- **Curve getting shallower:** Decreasing velocity (deceleration)

The gradient at any point gives the instantaneous velocity. For a curved graph, draw a tangent at the point of interest and calculate its gradient.

**中文：**
[[Displacement-Time Graphs|位移-时间图]]绘制物体沿直线运动的位置随时间的变化。纵轴表示位移（s），单位为米（m）；横轴表示时间（t），单位为秒（s）。图像的形状揭示了运动的性质：

- **正斜率的直线：** 正方向的匀速运动
- **负斜率的直线：** 负方向的匀速运动
- **水平线：** 物体静止（速度为零）
- **曲线（抛物线形）：** 速度变化（加速或减速）
- **曲线变陡：** 速度增加（加速）
- **曲线变缓：** 速度减小（减速）

任意点的斜率给出瞬时速度。对于曲线，在感兴趣的点处画切线并计算其斜率。

### Physical Meaning / 物理意义
**English:**
A displacement-time graph tells you where an object is at any given time. If you see a steep slope, the object is moving fast. If the slope is zero, the object is stopped. If the graph goes below the x-axis, the object has moved past its starting point in the opposite direction.

**中文：**
位移-时间图告诉你物体在任何给定时间的位置。如果看到陡峭的斜率，物体运动得快。如果斜率为零，物体静止。如果图像低于x轴，物体已经向相反方向移动超过了起点。

### Common Misconceptions / 常见误区
1. **Confusing displacement with distance:** A displacement-time graph can show negative values; a distance-time graph cannot.
2. **Thinking a curved graph means changing direction:** A curve means changing velocity (acceleration), not necessarily changing direction.
3. **Using the chord gradient instead of tangent:** For instantaneous velocity, always use the tangent, not the chord between two points.

### Exam Tips / 考试提示
**English:**
- Cambridge often asks you to calculate instantaneous velocity from a curved displacement-time graph by drawing a tangent
- Edexcel frequently combines displacement-time graphs with [[Equations of Motion (SUVAT)]] for multi-stage motion problems
- Always check the units on both axes before calculating gradients
- Remember that the gradient of a displacement-time graph is velocity, not speed

**中文：**
- 剑桥经常要求你通过画切线从弯曲的位移-时间图中计算瞬时速度
- 爱德思经常将位移-时间图与[[运动学方程（SUVAT）]]结合用于多阶段运动问题
- 在计算斜率之前始终检查两个轴的单位
- 记住位移-时间图的斜率是速度，不是速率

> 📷 **IMAGE PROMPT — DG01: Displacement-Time Graph Shapes**
>
> A clean, educational diagram showing four different displacement-time graphs side by side: (1) straight line through origin with positive gradient labeled "constant velocity", (2) horizontal line labeled "stationary", (3) upward curving parabola labeled "accelerating", (4) downward curving parabola labeled "decelerating". Each graph has labeled axes (displacement s/m vs time t/s). Use a white background with blue grid lines and red graph lines. Include tangent lines on the curved graphs with gradient calculations shown. Style: textbook-quality, vector-style illustration.

---

## 4.2 Velocity-Time Graphs / 速度-时间图

### Explanation / 解释
**English:**
A [[Velocity-Time Graphs|velocity-time graph]] plots velocity (v) on the y-axis against time (t) on the x-axis. This is arguably the most important motion graph because it contains information about both acceleration (from gradient) and displacement (from area under the graph).

Key interpretations:
- **Positive velocity:** Object moving in the positive direction
- **Negative velocity:** Object moving in the negative direction
- **Horizontal line:** Constant velocity (zero acceleration)
- **Straight line with positive gradient:** Constant positive acceleration
- **Straight line with negative gradient:** Constant negative acceleration (deceleration)
- **Curved line:** Changing acceleration (non-uniform acceleration)
- **Line crossing the x-axis:** Object changes direction (velocity passes through zero)

The gradient at any point gives instantaneous acceleration. The area between the graph and the time axis gives displacement (positive area = displacement in positive direction, negative area = displacement in negative direction).

**中文：**
[[Velocity-Time Graphs|速度-时间图]]将速度（v）绘制在纵轴上，时间（t）绘制在横轴上。这可以说是最重要的运动图像，因为它包含关于加速度（来自斜率）和位移（来自图像下的面积）的信息。

关键解读：
- **正速度：** 物体向正方向运动
- **负速度：** 物体向负方向运动
- **水平线：** 匀速运动（加速度为零）
- **正斜率的直线：** 匀加速运动
- **负斜率的直线：** 匀减速运动
- **曲线：** 加速度变化（非匀变速运动）
- **线穿过x轴：** 物体改变方向（速度经过零点）

任意点的斜率给出瞬时加速度。图像与时间轴之间的面积给出位移（正面积 = 正方向位移，负面积 = 负方向位移）。

### Physical Meaning / 物理意义
**English:**
A velocity-time graph tells you how fast an object is moving and in which direction at any moment. The steeper the line, the faster the velocity is changing (greater acceleration). The area under the graph tells you how far the object has traveled from its starting point.

**中文：**
速度-时间图告诉你物体在任何时刻运动的速度和方向。线越陡，速度变化越快（加速度越大）。图像下的面积告诉你物体从起点移动了多远。

### Common Misconceptions / 常见误区
1. **Thinking area gives distance:** The area under a velocity-time graph gives displacement, not distance. For distance, you must add the absolute values of areas.
2. **Confusing negative velocity with deceleration:** Negative velocity means moving backward; deceleration means slowing down (which could be in either direction).
3. **Forgetting units:** Gradient of v-t graph has units m/s² (acceleration), area has units m (displacement).

### Exam Tips / 考试提示
**English:**
- Cambridge and Edexcel both heavily test the area under velocity-time graphs for displacement calculations
- For multi-stage motion (e.g., acceleration, constant velocity, deceleration), break the graph into geometric shapes (triangles, rectangles, trapeziums)
- Edexcel specifically tests the use of velocity-time graphs for free-fall problems with and without air resistance
- When calculating total distance traveled, use the absolute values of areas

**中文：**
- 剑桥和爱德思都大量测试速度-时间图下的面积用于位移计算
- 对于多阶段运动（例如加速、匀速、减速），将图像分解为几何形状（三角形、矩形、梯形）
- 爱德思特别测试使用速度-时间图解决有/无空气阻力的自由落体问题
- 计算总路程时，使用面积的绝对值

> 📷 **IMAGE PROMPT — DG02: Velocity-Time Graph with Areas**
>
> A velocity-time graph showing a trapezoidal shape: initial positive slope from (0,0) to (4,10) representing acceleration, horizontal line from (4,10) to (8,10) representing constant velocity, negative slope from (8,10) to (12,0) representing deceleration. The area under each section is shaded in different colors: triangle (blue), rectangle (green), triangle (red). Labels show "Area = displacement" with calculations. Axes labeled "v / m s⁻¹" and "t / s". Include a second smaller graph below showing the corresponding displacement-time graph. Style: clean textbook diagram with pastel shading.

---

## 4.3 Acceleration-Time Graphs / 加速度-时间图

### Explanation / 解释
**English:**
An [[Acceleration-Time Graphs|acceleration-time graph]] plots acceleration (a) on the y-axis against time (t) on the x-axis. This graph is less commonly used directly in exams but is important for understanding the relationship between the three motion graphs.

Key interpretations:
- **Horizontal line above x-axis:** Constant positive acceleration
- **Horizontal line below x-axis:** Constant negative acceleration (deceleration)
- **Horizontal line on x-axis:** Zero acceleration (constant velocity)
- **Area under the graph:** Gives the change in velocity (Δv)
- **Gradient of the graph:** Gives the rate of change of acceleration (jerk), which is rarely examined at A-Level

**中文：**
[[Acceleration-Time Graphs|加速度-时间图]]将加速度（a）绘制在纵轴上，时间（t）绘制在横轴上。这个图像在考试中直接使用较少，但对于理解三个运动图像之间的关系很重要。

关键解读：
- **x轴上方的水平线：** 匀加速运动
- **x轴下方的水平线：** 匀减速运动
- **x轴上的水平线：** 加速度为零（匀速运动）
- **图像下的面积：** 给出速度的变化量（Δv）
- **图像的斜率：** 给出加速度的变化率（加加速度），在A-Level中很少考到

### Physical Meaning / 物理意义
**English:**
An acceleration-time graph tells you how the acceleration of an object is changing. If the graph is a horizontal line, the acceleration is constant. The area under the graph tells you how much the velocity has changed over a time interval.

**中文：**
加速度-时间图告诉你物体的加速度如何变化。如果图像是水平线，则加速度恒定。图像下的面积告诉你在一段时间间隔内速度变化了多少。

### Common Misconceptions / 常见误区
1. **Thinking the graph shows velocity:** The y-axis is acceleration, not velocity
2. **Confusing area with gradient:** Area under a-t graph gives change in velocity, not acceleration
3. **Assuming constant acceleration from a horizontal line at zero:** Zero acceleration means constant velocity, not constant acceleration

### Exam Tips / 考试提示
**English:**
- Cambridge rarely asks direct questions about acceleration-time graphs but may ask you to sketch one from a velocity-time graph
- Edexcel may use acceleration-time graphs in multiple-choice questions
- The most common question type is: "Sketch the acceleration-time graph for an object falling under gravity" (answer: horizontal line at a = g = 9.81 m/s²)
- Remember that the area under an acceleration-time graph equals the change in velocity

**中文：**
- 剑桥很少直接问关于加速度-时间图的问题，但可能要求你根据速度-时间图绘制一个
- 爱德思可能在选择题中使用加速度-时间图
- 最常见的问题类型是："绘制自由落体物体的加速度-时间图"（答案：在a = g = 9.81 m/s²处的水平线）
- 记住加速度-时间图下的面积等于速度的变化量

---

## 4.4 Interpreting Gradient and Area / 解释斜率和面积

### Explanation / 解释
**English:**
[[Interpreting Gradient and Area]] is the core skill for motion graphs. The gradient (slope) of a graph at any point tells you the rate of change of the y-axis quantity with respect to the x-axis quantity. The area under a graph between two points tells you the product of the y-axis and x-axis quantities.

**Summary Table:**

| Graph Type | Gradient gives | Area gives |
|------------|----------------|------------|
| Displacement-Time | Velocity (v = ds/dt) | Not applicable |
| Velocity-Time | Acceleration (a = dv/dt) | Displacement (s = ∫v dt) |
| Acceleration-Time | Rate of change of acceleration (jerk) | Change in velocity (Δv = ∫a dt) |

**Mathematical relationships:**
- For a straight line: gradient = Δy/Δx
- For a curve: instantaneous gradient = dy/dx (using tangent)
- Area for simple shapes: triangle = ½ × base × height, rectangle = base × height, trapezium = ½ × (sum of parallel sides) × height

**中文：**
[[Interpreting Gradient and Area]]是运动图像的核心技能。图像上任意点的斜率（坡度）告诉你y轴量相对于x轴量的变化率。两点之间图像下的面积告诉你y轴量和x轴量的乘积。

**总结表：**

| 图像类型 | 斜率给出 | 面积给出 |
|---------|---------|---------|
| 位移-时间 | 速度（v = ds/dt） | 不适用 |
| 速度-时间 | 加速度（a = dv/dt） | 位移（s = ∫v dt） |
| 加速度-时间 | 加速度变化率（加加速度） | 速度变化量（Δv = ∫a dt） |

**数学关系：**
- 对于直线：斜率 = Δy/Δx
- 对于曲线：瞬时斜率 = dy/dx（使用切线）
- 简单形状的面积：三角形 = ½ × 底 × 高，矩形 = 底 × 高，梯形 = ½ ×（平行边之和）× 高

### Physical Meaning / 物理意义
**English:**
Understanding gradient and area allows you to extract all kinematic information from a single graph. For example, from a velocity-time graph alone, you can determine acceleration (gradient), displacement (area), and even the shape of the displacement-time graph (by integrating).

**中文：**
理解斜率和面积使你能够从单个图像中提取所有运动学信息。例如，仅从速度-时间图，你可以确定加速度（斜率）、位移（面积），甚至位移-时间图的形状（通过积分）。

### Common Misconceptions / 常见误区
1. **Using gradient when area is needed:** Always check what the question asks for
2. **Forgetting sign conventions:** Negative gradient means decreasing quantity; area below x-axis is negative
3. **Incorrect units:** Gradient units = y-axis units / x-axis units; area units = y-axis units × x-axis units

### Exam Tips / 考试提示
**English:**
- This is the most tested concept in motion graphs
- Cambridge often asks: "Use the gradient of the graph to find..." or "Use the area under the graph to find..."
- Edexcel frequently combines gradient and area calculations in multi-part questions
- Always show your working: draw the tangent, show the triangle used for gradient, show the shape used for area

**中文：**
- 这是运动图像中考得最多的概念
- 剑桥经常问："使用图像的斜率来求..."或"使用图像下的面积来求..."
- 爱德思经常在多部分问题中结合斜率和面积计算
- 始终展示你的计算过程：画切线，显示用于斜率的三角形，显示用于面积的形状

---

# 5. Essential Equations / 核心公式

## 5.1 Gradient of a Straight Line / 直线的斜率

**Equation / 公式:**
$$ \text{gradient} = \frac{\Delta y}{\Delta x} = \frac{y_2 - y_1}{x_2 - x_1} $$

**Variables / 变量:**
| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| Δy | Change in y-axis quantity | y轴量的变化 | Depends on graph |
| Δx | Change in x-axis quantity | x轴量的变化 | s (time) |
| y₁, y₂ | y-coordinates of two points | 两点的y坐标 | Depends on graph |
| x₁, x₂ | x-coordinates of two points | 两点的x坐标 | s (time) |

**Derivation / 推导:**
**English:**
The gradient formula comes from the definition of slope: rise over run. For any two points (x₁, y₁) and (x₂, y₂) on a straight line, the gradient is constant and given by the change in y divided by the change in x.

**中文：**
斜率公式来自坡度的定义：垂直变化除以水平变化。对于直线上的任意两点（x₁, y₁）和（x₂, y₂），斜率是恒定的，由y的变化量除以x的变化量给出。

**Conditions / 适用条件:**
**English:** Only for straight-line graphs (constant gradient). For curved graphs, this gives the average gradient between two points, not the instantaneous gradient.

**中文：** 仅适用于直线图（恒定斜率）。对于曲线图，这给出两点之间的平均斜率，而不是瞬时斜率。

**Limitations / 局限性:**
**English:** Cannot be used for curved graphs to find instantaneous values. For curves, use the tangent method.

**中文：** 不能用于曲线图求瞬时值。对于曲线，使用切线法。

**Rearrangements / 变形:**
**English:** The formula can be rearranged to find any missing variable: y₂ = y₁ + m(x₂ - x₁) where m is the gradient.

**中文：** 公式可以变形以求出任何缺失的变量：y₂ = y₁ + m(x₂ - x₁)，其中m是斜率。

---

## 5.2 Gradient of a Tangent / 切线的斜率

**Equation / 公式:**
$$ \text{instantaneous gradient} = \frac{dy}{dx} = \lim_{\Delta x \to 0} \frac{\Delta y}{\Delta x} $$

**Variables / 变量:**
| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| dy/dx | Derivative of y with respect to x | y对x的导数 | Depends on graph |
| Δy | Small change in y | y的微小变化 | Depends on graph |
| Δx | Small change in x | x的微小变化 | s (time) |

**Derivation / 推导:**
**English:**
The instantaneous gradient is the limit of the average gradient as the two points get infinitely close together. In practice, for A-Level, you draw a tangent line to the curve at the point of interest and calculate its gradient using two points on the tangent line.

**中文：**
瞬时斜率是当两点无限接近时平均斜率的极限。在实践中，对于A-Level，你在感兴趣的点处画一条曲线的切线，并使用切线上两点的坐标计算其斜率。

**Conditions / 适用条件:**
**English:** Used for curved graphs where the gradient changes continuously.

**中文：** 用于梯度连续变化的曲线图。

**Limitations / 局限性:**
**English:** The accuracy depends on how precisely you draw the tangent. This introduces uncertainty in the calculated value.

**中文：** 精度取决于你画切线的精确程度。这会在计算值中引入不确定度。

**Rearrangements / 变形:**
**English:** Not applicable; this is a conceptual formula.

**中文：** 不适用；这是一个概念性公式。

---

## 5.3 Area Under a Graph / 图像下的面积

**Equation / 公式:**
$$ \text{Area} = \int_{x_1}^{x_2} y \, dx $$

For simple shapes:
- Triangle: $A = \frac{1}{2} \times \text{base} \times \text{height}$
- Rectangle: $A = \text{base} \times \text{height}$
- Trapezium: $A = \frac{1}{2} \times (a + b) \times h$

**Variables / 变量:**
| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| A | Area under graph | 图像下的面积 | y-unit × x-unit |
| base | Length along x-axis | 沿x轴的长度 | s (time) |
| height | Length along y-axis | 沿y轴的长度 | Depends on graph |
| a, b | Lengths of parallel sides of trapezium | 梯形平行边的长度 | Depends on graph |
| h | Height of trapezium (perpendicular distance) | 梯形的高（垂直距离） | s (time) |

**Derivation / 推导:**
**English:**
The area under a graph represents the integral of the y-axis quantity with respect to the x-axis quantity. For velocity-time graphs, area = ∫v dt = displacement. For acceleration-time graphs, area = ∫a dt = change in velocity.

**中文：**
图像下的面积表示y轴量对x轴量的积分。对于速度-时间图，面积 = ∫v dt = 位移。对于加速度-时间图，面积 = ∫a dt = 速度变化量。

**Conditions / 适用条件:**
**English:** The area is calculated between two specific x-values (time values). For areas below the x-axis, the area is negative.

**中文：** 面积是在两个特定的x值（时间值）之间计算的。对于x轴下方的面积，面积为负值。

**Limitations / 局限性:**
**English:** For curved graphs, you may need to count squares or use integration. Counting squares introduces uncertainty.

**中文：** 对于曲线图，你可能需要数方格或使用积分。数方格会引入不确定度。

**Rearrangements / 变形:**
**English:** For compound shapes, break into simple shapes and sum the areas.

**中文：** 对于复合形状，分解为简单形状并求和。

---

## 5.4 Relationship Between Velocity and Displacement / 速度与位移的关系

**Equation / 公式:**
$$ v = \frac{ds}{dt} \quad \text{and} \quad s = \int v \, dt $$

**Variables / 变量:**
| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| v | Velocity | 速度 | m s⁻¹ |
| s | Displacement | 位移 | m |
| t | Time | 时间 | s |

**Derivation / 推导:**
**English:**
Velocity is defined as the rate of change of displacement. Therefore, v = ds/dt. Conversely, displacement is the integral of velocity with respect to time: s = ∫v dt. This is why the gradient of a displacement-time graph gives velocity and the area under a velocity-time graph gives displacement.

**中文：**
速度定义为位移的变化率。因此，v = ds/dt。反之，位移是速度对时间的积分：s = ∫v dt。这就是为什么位移-时间图的斜率给出速度，速度-时间图下的面积给出位移。

**Conditions / 适用条件:**
**English:** Always true for one-dimensional motion.

**中文：** 对于一维运动始终成立。

**Limitations / 局限性:**
**English:** This is a definition, so it has no limitations in one-dimensional motion.

**中文：** 这是一个定义，因此在一维运动中没有局限性。

**Rearrangements / 变形:**
**English:** ds = v dt (infinitesimal form)

**中文：** ds = v dt（无穷小形式）

---

## 5.5 Relationship Between Acceleration and Velocity / 加速度与速度的关系

**Equation / 公式:**
$$ a = \frac{dv}{dt} \quad \text{and} \quad \Delta v = \int a \, dt $$

**Variables / 变量:**
| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| a | Acceleration | 加速度 | m s⁻² |
| v | Velocity | 速度 | m s⁻¹ |
| t | Time | 时间 | s |
| Δv | Change in velocity | 速度变化量 | m s⁻¹ |

**Derivation / 推导:**
**English:**
Acceleration is defined as the rate of change of velocity. Therefore, a = dv/dt. The change in velocity is the integral of acceleration with respect to time: Δv = ∫a dt. This is why the gradient of a velocity-time graph gives acceleration and the area under an acceleration-time graph gives change in velocity.

**中文：**
加速度定义为速度的变化率。因此，a = dv/dt。速度变化量是加速度对时间的积分：Δv = ∫a dt。这就是为什么速度-时间图的斜率给出加速度，加速度-时间图下的面积给出速度变化量。

**Conditions / 适用条件:**
**English:** Always true for one-dimensional motion.

**中文：** 对于一维运动始终成立。

**Limitations / 局限性:**
**English:** This is a definition, so it has no limitations in one-dimensional motion.

**中文：** 这是一个定义，因此在一维运动中没有局限性。

**Rearrangements / 变形:**
**English:** dv = a dt (infinitesimal form)

**中文：** dv = a dt（无穷小形式）

---

# 6. Graphs and Relationships / 图表与关系

## 6.1 Displacement-Time Graph Shapes / 位移-时间图形状

### Axes / 坐标轴
**English:** x-axis: Time (t / s); y-axis: Displacement (s / m)
**中文：** x轴：时间（t / s）；y轴：位移（s / m）

### Shape / 形状
**English:**
- **Stationary:** Horizontal line (gradient = 0)
- **Constant velocity (positive):** Straight line with positive gradient
- **Constant velocity (negative):** Straight line with negative gradient
- **Accelerating:** Upward curving parabola (gradient increasing)
- **Decelerating:** Downward curving parabola (gradient decreasing)

**中文：**
- **静止：** 水平线（斜率 = 0）
- **匀速（正方向）：** 正斜率的直线
- **匀速（负方向）：** 负斜率的直线
- **加速：** 向上弯曲的抛物线（斜率增加）
- **减速：** 向下弯曲的抛物线（斜率减小）

### Gradient Meaning / 斜率含义
**English:** Gradient = velocity (v = ds/dt). Positive gradient = positive velocity; negative gradient = negative velocity.
**中文：** 斜率 = 速度（v = ds/dt）。正斜率 = 正速度；负斜率 = 负速度。

### Area Meaning / 面积含义
**English:** Not applicable for displacement-time graphs.
**中文：** 不适用于位移-时间图。

### Exam Interpretation / 考试解读
**English:**
- A curved s-t graph means velocity is changing (acceleration is non-zero)
- The steeper the curve, the faster the object is moving
- Where the graph crosses the time axis, displacement = 0 (object passes through the origin)
- The graph never goes vertical (that would mean infinite velocity)

**中文：**
- 弯曲的s-t图意味着速度在变化（加速度非零）
- 曲线越陡，物体运动越快
- 图像穿过时间轴处，位移 = 0（物体经过原点）
- 图像永远不会垂直（那意味着无限速度）

### Common Questions / 常见问题
**English:**
- "Calculate the instantaneous velocity at t = X s" (draw tangent)
- "Describe the motion of the object" (interpret shape)
- "Sketch the velocity-time graph for this motion" (differentiate)

**中文：**
- "计算在t = X秒时的瞬时速度"（画切线）
- "描述物体的运动"（解释形状）
- "绘制该运动的速度-时间图"（求导）

---

## 6.2 Velocity-Time Graph Shapes / 速度-时间图形状

### Axes / 坐标轴
**English:** x-axis: Time (t / s); y-axis: Velocity (v / m s⁻¹)
**中文：** x轴：时间（t / s）；y轴：速度（v / m s⁻¹）

### Shape / 形状
**English:**
- **Stationary/constant velocity:** Horizontal line (gradient = 0)
- **Constant acceleration (positive):** Straight line with positive gradient
- **Constant deceleration (negative):** Straight line with negative gradient
- **Increasing acceleration:** Upward curving line
- **Decreasing acceleration:** Downward curving line
- **Changing direction:** Line crosses the time axis (v = 0)

**中文：**
- **静止/匀速：** 水平线（斜率 = 0）
- **匀加速：** 正斜率的直线
- **匀减速：** 负斜率的直线
- **加速度增加：** 向上弯曲的线
- **加速度减小：** 向下弯曲的线
- **改变方向：** 线穿过时间轴（v = 0）

### Gradient Meaning / 斜率含义
**English:** Gradient = acceleration (a = dv/dt). Positive gradient = positive acceleration; negative gradient = negative acceleration (deceleration).
**中文：** 斜率 = 加速度（a = dv/dt）。正斜率 = 正加速度；负斜率 = 负加速度（减速）。

### Area Meaning / 面积含义
**English:** Area between graph and time axis = displacement (s = ∫v dt). Area above axis = positive displacement; area below axis = negative displacement.
**中文：** 图像与时间轴之间的面积 = 位移（s = ∫v dt）。轴上方面积 = 正位移；轴下方面积 = 负位移。

### Exam Interpretation / 考试解读
**English:**
- A horizontal line means constant velocity (zero acceleration)
- A straight line with gradient means constant acceleration
- The area under the graph gives displacement (not distance)
- For total distance, add absolute values of all areas
- Where the graph crosses the time axis, the object changes direction

**中文：**
- 水平线意味着匀速运动（加速度为零）
- 有斜率的直线意味着匀变速运动
- 图像下的面积给出位移（不是路程）
- 对于总路程，将所有面积的绝对值相加
- 图像穿过时间轴处，物体改变方向

### Common Questions / 常见问题
**English:**
- "Calculate the acceleration during the first X seconds" (find gradient)
- "Calculate the total displacement" (find area)
- "Calculate the total distance traveled" (find sum of absolute areas)
- "Sketch the acceleration-time graph" (differentiate)
- "Sketch the displacement-time graph" (integrate)

**中文：**
- "计算前X秒内的加速度"（求斜率）
- "计算总位移"（求面积）
- "计算总路程"（求绝对面积之和）
- "绘制加速度-时间图"（求导）
- "绘制位移-时间图"（积分）

---

## 6.3 Acceleration-Time Graph Shapes / 加速度-时间图形状

### Axes / 坐标轴
**English:** x-axis: Time (t / s); y-axis: Acceleration (a / m s⁻²)
**中文：** x轴：时间（t / s）；y轴：加速度（a / m s⁻²）

### Shape / 形状
**English:**
- **Zero acceleration (constant velocity):** Horizontal line on the x-axis (a = 0)
- **Constant positive acceleration:** Horizontal line above x-axis
- **Constant negative acceleration:** Horizontal line below x-axis
- **Increasing acceleration:** Line with positive gradient
- **Decreasing acceleration:** Line with negative gradient

**中文：**
- **加速度为零（匀速）：** x轴上的水平线（a = 0）
- **匀加速：** x轴上方的水平线
- **匀减速：** x轴下方的水平线
- **加速度增加：** 正斜率的线
- **加速度减小：** 负斜率的线

### Gradient Meaning / 斜率含义
**English:** Gradient = rate of change of acceleration (jerk). Rarely examined at A-Level.
**中文：** 斜率 = 加速度的变化率（加加速度）。在A-Level中很少考到。

### Area Meaning / 面积含义
**English:** Area between graph and time axis = change in velocity (Δv = ∫a dt).
**中文：** 图像与时间轴之间的面积 = 速度变化量（Δv = ∫a dt）。

### Exam Interpretation / 考试解读
**English:**
- A horizontal line at a = g = 9.81 m s⁻² represents free fall under gravity
- The area under the graph gives the change in velocity, not the final velocity
- To find final velocity, add the area to the initial velocity: v = u + Δv

**中文：**
- a = g = 9.81 m s⁻²处的水平线表示重力作用下的自由落体
- 图像下的面积给出速度变化量，不是最终速度
- 要求最终速度，将面积加到初速度上：v = u + Δv

### Common Questions / 常见问题
**English:**
- "Calculate the change in velocity between t = X and t = Y" (find area)
- "Sketch the acceleration-time graph for an object thrown upwards" (a = -g constant)
- "Determine the final velocity given initial velocity" (v = u + area)

**中文：**
- "计算在t = X和t = Y之间的速度变化量"（求面积）
- "绘制向上抛出的物体的加速度-时间图"（a = -g 常数）
- "给定初速度求最终速度"（v = u + 面积）

---

## 6.4 Converting Between Graph Types / 图像类型之间的转换

### Axes / 坐标轴
**English:** The three graph types are related through differentiation and integration.
**中文：** 三种图像类型通过微分和积分相关联。

### Shape / 形状
**English:**
```
s-t graph → differentiate → v-t graph → differentiate → a-t graph
s-t graph ← integrate ← v-t graph ← integrate ← a-t graph
```

**中文：**
```
s-t图 → 求导 → v-t图 → 求导 → a-t图
s-t图 ← 积分 ← v-t图 ← 积分 ← a-t图
```

### Gradient Meaning / 斜率含义
**English:** Differentiation (finding gradient) moves "down" the chain: s → v → a.
**中文：** 微分（求斜率）沿链"向下"移动：s → v → a。

### Area Meaning / 面积含义
**English:** Integration (finding area) moves "up" the chain: a → v → s.
**中文：** 积分（求面积）沿链"向上"移动：a → v → s。

### Exam Interpretation / 考试解读
**English:**
- To convert s-t to v-t: find gradient at each point
- To convert v-t to a-t: find gradient at each point
- To convert a-t to v-t: find area up to each point
- To convert v-t to s-t: find area up to each point

**中文：**
- 将s-t图转换为v-t图：求每点的斜率
- 将v-t图转换为a-t图：求每点的斜率
- 将a-t图转换为v-t图：求到每点的面积
- 将v-t图转换为s-t图：求到每点的面积

### Common Questions / 常见问题
**English:**
- "Sketch the velocity-time graph for the motion shown in the displacement-time graph"
- "Using the acceleration-time graph, determine the velocity at t = X s"

**中文：**
- "绘制位移-时间图所示运动的速度-时间图"
- "使用加速度-时间图，确定在t = X秒时的速度"

---

# 7. Required Diagrams / 必备图表

## 7.1 Displacement-Time Graph with Tangent / 带切线的位移-时间图

### Description / 描述
**English:**
A displacement-time graph showing a curved line (parabolic shape) representing an accelerating object. A tangent line is drawn at a specific point (e.g., t = 3 s). The tangent line extends to form a right-angled triangle, with the rise (Δs) and run (Δt) labeled. The gradient calculation is shown: v = Δs/Δt.

**中文：**
一个位移-时间图，显示代表加速物体的曲线（抛物线形）。在特定点（例如t = 3秒）画了一条切线。切线延伸形成一个直角三角形，标有垂直变化（Δs）和水平变化（Δt）。显示了斜率计算：v = Δs/Δt。

### Image Prompt / 图片生成提示
> 📷 **IMAGE PROMPT — DG03: Displacement-Time Graph with Tangent**
>
> A displacement-time graph with a curved line (parabolic shape) on a white background with light blue grid lines. The curve starts at (0,0) and curves upward. At t = 3 s, a red dashed tangent line is drawn touching the curve. A right-angled triangle is formed using the tangent line, with horizontal side labeled "Δt = 2 s" and vertical side labeled "Δs = 8 m". The gradient calculation is shown in a box: "v = Δs/Δt = 8/2 = 4 m s⁻¹". Axes labeled "Displacement s / m" and "Time t / s". Style: clean textbook diagram, vector illustration, professional appearance.

### Labels Required / 需要标注
**English:** Curve (motion), Tangent line, Δs (rise), Δt (run), Point of tangency, Axes labels, Gradient calculation
**中文：** 曲线（运动）、切线、Δs（垂直变化）、Δt（水平变化）、切点、坐标轴标签、斜率计算

### Exam Importance / 考试重要性
**English:**
This diagram is essential for understanding how to calculate instantaneous velocity from a curved displacement-time graph. Cambridge frequently asks students to draw tangents and calculate gradients in Paper 2 and Paper 4.

**中文：**
这个图对于理解如何从弯曲的位移-时间图计算瞬时速度至关重要。剑桥经常在试卷2和试卷4中要求学生画切线并计算斜率。

---

## 7.2 Velocity-Time Graph with Area Shading / 带面积阴影的速度-时间图

### Description / 描述
**English:**
A velocity-time graph showing a multi-stage motion: acceleration (positive slope), constant velocity (horizontal), and deceleration (negative slope). The area under each section is shaded in different colors. The shapes are labeled as triangle, rectangle, and triangle. Area calculations are shown for each shape and summed to find total displacement.

**中文：**
一个速度-时间图，显示多阶段运动：加速（正斜率）、匀速（水平）和减速（负斜率）。每个部分下的面积用不同颜色阴影标记。形状被标记为三角形、矩形和三角形。显示每个形状的面积计算，并求和得到总位移。

### Image Prompt / 图片生成提示
> 📷 **IMAGE PROMPT — DG04: Velocity-Time Graph with Area Shading**
>
> A velocity-time graph showing a trapezoidal shape on a white background. The graph starts at (0,0), rises with positive slope to (4,12), continues horizontally to (8,12), then falls with negative slope to (12,0). Three shaded regions: triangle from t=0 to t=4 (blue, labeled "Area₁ = ½ × 4 × 12 = 24 m"), rectangle from t=4 to t=8 (green, labeled "Area₂ = 4 × 12 = 48 m"), triangle from t=8 to t=12 (red, labeled "Area₃ = ½ × 4 × 12 = 24 m"). Total displacement shown: "s = 24 + 48 + 24 = 96 m". Axes labeled "Velocity v / m s⁻¹" and "Time t / s". Style: clean textbook diagram with pastel shading, vector illustration.

### Labels Required / 需要标注
**English:** Acceleration phase, Constant velocity phase, Deceleration phase, Area₁, Area₂, Area₃, Total displacement, Axes labels
**中文：** 加速阶段、匀速阶段、减速阶段、面积₁、面积₂、面积₃、总位移、坐标轴标签

### Exam Importance / 考试重要性
**English:**
This is the most common type of velocity-time graph question in both Cambridge and Edexcel exams. Students must be able to break the graph into geometric shapes and calculate areas correctly.

**中文：**
这是剑桥和爱德思考试中最常见的速度-时间图问题类型。学生必须能够将图像分解为几何形状并正确计算面积。

---

## 7.3 Free Fall Velocity-Time Graph / 自由落体速度-时间图

### Description / 描述
**English:**
A velocity-time graph showing an object thrown vertically upward and falling back down. The graph starts at positive initial velocity (u), decreases linearly to zero at the highest point, then continues linearly to negative velocity. The gradient is constant at -g = -9.81 m s⁻². The area above the axis equals the area below the axis (net displacement = 0).

**中文：**
一个速度-时间图，显示物体垂直向上抛出并落回。图像从正的初速度（u）开始，线性减小到最高点为零，然后继续线性变化到负速度。斜率为常数 -g = -9.81 m s⁻²。轴上方面积等于轴下方面积（净位移 = 0）。

### Image Prompt / 图片生成提示
> 📷 **IMAGE PROMPT — DG05: Free Fall Velocity-Time Graph**
>
> A velocity-time graph on a white background showing an object thrown upward. The graph is a straight line starting at (0, 20) on the positive y-axis, crossing the x-axis at (2.04, 0) (the highest point), and continuing to (4.08, -20). The gradient is labeled "a = -g = -9.81 m s⁻²". The area above the axis is shaded blue and labeled "Upward displacement", the area below the axis is shaded red and labeled "Downward displacement". A note says "Net displacement = 0". Axes labeled "Velocity v / m s⁻¹" and "Time t / s". Style: clean textbook diagram, vector illustration.

### Labels Required / 需要标注
**English:** Initial velocity (u), Highest point (v = 0), Final velocity (v = -u), Gradient = -g, Upward displacement, Downward displacement, Axes labels
**中文：** 初速度（u）、最高点（v = 0）、最终速度（v = -u）、斜率 = -g、向上位移、向下位移、坐标轴标签

### Exam Importance / 考试重要性
**English:**
This diagram is essential for understanding projectile motion and free fall under gravity. Both Cambridge and Edexcel test this concept, with Edexcel placing particular emphasis on using graphs to solve free-fall problems.

**中文：**
这个图对于理解抛体运动和重力作用下的自由落体至关重要。剑桥和爱德思都测试这个概念，爱德思特别强调使用图像解决自由落体问题。

---

## 7.4 Converting Between Graph Types / 图像类型之间的转换

### Description / 描述
**English:**
A three-panel diagram showing the same motion represented as displacement-time, velocity-time, and acceleration-time graphs. The graphs are aligned vertically so that corresponding time points line up. Arrows show the relationships: gradient of s-t = v-t, gradient of v-t = a-t, area of v-t = s-t, area of a-t = v-t.

**中文：**
一个三面板图，显示同一运动分别表示为位移-时间、速度-时间和加速度-时间图。图像垂直对齐，使对应的时间点对齐。箭头显示关系：s-t的斜率 = v-t，v-t的斜率 = a-t，v-t的面积 = s-t，a-t的面积 = v-t。

### Image Prompt / 图片生成提示
> 📷 **IMAGE PROMPT — DG06: Converting Between Graph Types**
>
> Three graphs stacked vertically on a white background, all sharing the same time axis. Top graph: displacement-time (parabolic curve). Middle graph: velocity-time (straight line with positive slope). Bottom graph: acceleration-time (horizontal line above x-axis). Vertical dashed lines connect key time points across all three graphs. Arrows on the left side show: "Gradient ↓" pointing from s-t to v-t, "Gradient ↓" from v-t to a-t, "Area ↑" from a-t to v-t, "Area ↑" from v-t to s-t. Each graph has labeled axes. Style: clean textbook diagram, vector illustration, professional appearance.

### Labels Required / 需要标注
**English:** s-t graph, v-t graph, a-t graph, Gradient (differentiation), Area (integration), Corresponding time points, Axes labels
**中文：** s-t图、v-t图、a-t图、斜率（微分）、面积（积分）、对应时间点、坐标轴标签

### Exam Importance / 考试重要性
**English:**
Understanding the relationships between the three graph types is fundamental to kinematics. Cambridge and Edexcel both test this through questions asking students to sketch one graph from another.

**中文：**
理解三种图像类型之间的关系是运动学的基础。剑桥和爱德思都通过要求学生根据一种图像绘制另一种图像的问题来测试这一点。

---

# 8. Worked Examples / 典型例题

## Example 1: Calculating Acceleration and Displacement from a Velocity-Time Graph / 从速度-时间图计算加速度和位移

### Question / 题目
**English:**
A car travels along a straight road. The velocity-time graph for its motion is shown below.

The graph shows:
- From t = 0 to t = 5 s: velocity increases uniformly from 0 to 15 m s⁻¹
- From t = 5 to t = 15 s: velocity remains constant at 15 m s⁻¹
- From t = 15 to t = 20 s: velocity decreases uniformly to 0 m s⁻¹

(a) Calculate the acceleration of the car during the first 5 seconds.
(b) Calculate the total displacement of the car.
(c) Calculate the total distance traveled by the car.

**中文：**
一辆汽车沿直路行驶。其运动的速度-时间图如下所示。

图像显示：
- 从t = 0到t = 5秒：速度从0均匀增加到15 m s⁻¹
- 从t = 5到t = 15秒：速度保持在15 m s⁻¹不变
- 从t = 15到t = 20秒：速度均匀减小到0 m s⁻¹

(a) 计算汽车在前5秒内的加速度。
(b) 计算汽车的总位移。
(c) 计算汽车的总路程。

### Image Prompt / 图片提示
> 📷 **IMAGE PROMPT — EX01: Car Velocity-Time Graph**
>
> A velocity-time graph on a white background with light blue grid lines. The graph is a trapezoid: from (0,0) to (5,15) with positive slope, horizontal from (5,15) to (15,15), negative slope from (15,15) to (20,0). Axes labeled "Velocity v / m s⁻¹" and "Time t / s". Grid lines at intervals of 5 on both axes. Style: clean exam-style diagram.

### Solution / 解答

**Part (a): Acceleration during first 5 seconds**

**English:**
Acceleration = gradient of velocity-time graph

$$ a = \frac{\Delta v}{\Delta t} = \frac{15 - 0}{5 - 0} = \frac{15}{5} = 3.0 \text{ m s}^{-2} $$

**中文：**
加速度 = 速度-时间图的斜率

$$ a = \frac{\Delta v}{\Delta t} = \frac{15 - 0}{5 - 0} = \frac{15}{5} = 3.0 \text{ m s}^{-2} $$

**Part (b): Total displacement**

**English:**
Total displacement = area under velocity-time graph

Break into three shapes:
1. Triangle (0-5 s): $A_1 = \frac{1}{2} \times 5 \times 15 = 37.5 \text{ m}$
2. Rectangle (5-15 s): $A_2 = 10 \times 15 = 150 \text{ m}$
3. Triangle (15-20 s): $A_3 = \frac{1}{2} \times 5 \times 15 = 37.5 \text{ m}$

Total displacement = $37.5 + 150 + 37.5 = 225 \text{ m}$

**中文：**
总位移 = 速度-时间图下的面积

分解为三个形状：
1. 三角形（0-5秒）：$A_1 = \frac{1}{2} \times 5 \times 15 = 37.5 \text{ m}$
2. 矩形（5-15秒）：$A_2 = 10 \times 15 = 150 \text{ m}$
3. 三角形（15-20秒）：$A_3 = \frac{1}{2} \times 5 \times 15 = 37.5 \text{ m}$

总位移 = $37.5 + 150 + 37.5 = 225 \text{ m}$

**Part (c): Total distance**

**English:**
Since the velocity is always positive (graph is always above the time axis), the displacement equals the distance.

Total distance = 225 m

**中文：**
由于速度始终为正（图像始终在时间轴上方），位移等于路程。

总路程 = 225 m

### Final Answer / 最终答案
**Answer:**
(a) a = 3.0 m s⁻²
(b) s = 225 m
(c) Distance = 225 m

**答案：**
(a) a = 3.0 m s⁻²
(b) s = 225 m
(c) 路程 = 225 m

### Examiner Notes / 考官点评
**English:**
- Part (a): Common mistake is using the wrong time interval. Always use Δv/Δt.
- Part (b): Students often forget to include all three sections. Always break the graph into simple shapes.
- Part (c): This is a trick question — when velocity is always positive, displacement = distance. If the graph went below the axis, you would need to add absolute areas.

**中文：**
- 第(a)部分：常见错误是使用错误的时间间隔。始终使用Δv/Δt。
- 第(b)部分：学生经常忘记包括所有三个部分。始终将图像分解为简单形状。
- 第(c)部分：这是一个陷阱题——当速度始终为正时，位移 = 路程。如果图像低于轴，你需要将绝对面积相加。

### Alternative Method / 替代方法
**English:**
For part (b), you could also use the formula for the area of a trapezium:
$$ A = \frac{1}{2}(a + b)h = \frac{1}{2}(10 + 20) \times 15 = 225 \text{ m} $$
where a = 10 s (top base), b = 20 s (bottom base), h = 15 m s⁻¹ (height).

**中文：**
对于第(b)部分，你也可以使用梯形面积公式：
$$ A = \frac{1}{2}(a + b)h = \frac{1}{2}(10 + 20) \times 15 = 225 \text{ m} $$
其中a = 10秒（上底），b = 20秒（下底），h = 15 m s⁻¹（高）。

---

## Example 2: Instantaneous Velocity from a Curved Displacement-Time Graph / 从弯曲的位移-时间图求瞬时速度

### Question / 题目
**English:**
The displacement-time graph for a moving object is shown below. The graph follows the equation $s = 2t^2$ where s is in metres and t is in seconds.

(a) Calculate the instantaneous velocity at t = 3.0 s.
(b) Calculate the average velocity between t = 0 s and t = 3.0 s.

**中文：**
一个运动物体的位移-时间图如下所示。图像遵循方程 $s = 2t^2$，其中s以米为单位，t以秒为单位。

(a) 计算在t = 3.0秒时的瞬时速度。
(b) 计算在t = 0秒和t = 3.0秒之间的平均速度。

### Image Prompt / 图片提示
> 📷 **IMAGE PROMPT — EX02: Curved Displacement-Time Graph**
>
> A displacement-time graph on a white background with light blue grid lines. The graph is a parabola starting at (0,0) and curving upward. At t = 3 s, a red dashed tangent line is drawn. The tangent extends to form a right triangle with Δt = 1.5 s and Δs = 18 m. The gradient calculation is shown. Axes labeled "Displacement s / m" and "Time t / s". Grid lines at intervals of 1 on x-axis and 5 on y-axis. Style: clean exam-style diagram.

### Solution / 解答

**Part (a): Instantaneous velocity at t = 3.0 s**

**Method 1: Using calculus (differentiation)**

**English:**
$$ s = 2t^2 $$
$$ v = \frac{ds}{dt} = 4t $$
At t = 3.0 s:
$$ v = 4 \times 3.0 = 12 \text{ m s}^{-1} $$

**中文：**
$$ s = 2t^2 $$
$$ v = \frac{ds}{dt} = 4t $$
在t = 3.0秒时：
$$ v = 4 \times 3.0 = 12 \text{ m s}^{-1} $$

**Method 2: Using tangent on graph**

**English:**
Draw a tangent at t = 3.0 s. The tangent passes through points (2.0, 4) and (4.0, 28).
$$ v = \frac{\Delta s}{\Delta t} = \frac{28 - 4}{4.0 - 2.0} = \frac{24}{2.0} = 12 \text{ m s}^{-1} $$

**中文：**
在t = 3.0秒处画切线。切线经过点(2.0, 4)和(4.0, 28)。
$$ v = \frac{\Delta s}{\Delta t} = \frac{28 - 4}{4.0 - 2.0} = \frac{24}{2.0} = 12 \text{ m s}^{-1} $$

**Part (b): Average velocity between t = 0 and t = 3.0 s**

**English:**
$$ \text{Average velocity} = \frac{\text{Total displacement}}{\text{Total time}} $$
At t = 0: s = 2(0)² = 0 m
At t = 3.0: s = 2(3.0)² = 18 m
$$ v_{avg} = \frac{18 - 0}{3.0 - 0} = \frac{18}{3.0} = 6.0 \text{ m s}^{-1} $$

**中文：**
$$ \text{平均速度} = \frac{\text{总位移}}{\text{总时间}} $$
在t = 0时：s = 2(0)² = 0 m
在t = 3.0时：s = 2(3.0)² = 18 m
$$ v_{avg} = \frac{18 - 0}{3.0 - 0} = \frac{18}{3.0} = 6.0 \text{ m s}^{-1} $$

### Final Answer / 最终答案
**Answer:**
(a) v = 12 m s⁻¹
(b) v_avg = 6.0 m s⁻¹

**答案：**
(a) v = 12 m s⁻¹
(b) v_avg = 6.0 m s⁻¹

### Examiner Notes / 考官点评
**English:**
- Part (a): The calculus method is faster and more accurate. However, if the equation is not given, you must use the tangent method.
- Part (b): Average velocity is NOT the same as instantaneous velocity at the midpoint. Here, average velocity (6.0 m s⁻¹) is less than instantaneous velocity at t = 3.0 s (12 m s⁻¹) because the object is accelerating.
- Common mistake: Using the chord gradient (average velocity) when instantaneous velocity is required.

**中文：**
- 第(a)部分：微积分方法更快更准确。但是，如果没有给出方程，你必须使用切线法。
- 第(b)部分：平均速度与中点的瞬时速度不同。这里，平均速度（6.0 m s⁻¹）小于t = 3.0秒时的瞬时速度（12 m s⁻¹），因为物体在加速。
- 常见错误：当需要瞬时速度时使用了弦的斜率（平均速度）。

### Alternative Method / 替代方法
**English:**
For part (a), you could also use the [[Equations of Motion (SUVAT)]] if you recognize that s = 2t² corresponds to u = 0 and a = 4 m s⁻² (from s = ut + ½at²). Then v = u + at = 0 + 4 × 3 = 12 m s⁻¹.

**中文：**
对于第(a)部分，如果你认识到s = 2t²对应于u = 0和a = 4 m s⁻²（来自s = ut + ½at²），你也可以使用[[运动学方程（SUVAT）]]。然后v = u + at = 0 + 4 × 3 = 12 m s⁻¹。

---

# 9. Past Paper Question Types / 历年真题题型

| Question Type / 题型 | Frequency / 频率 | Difficulty / 难度 | Past Paper References / 真题索引 |
|----------------------|------------------|------------------|-------------------------------|
| Calculation of gradient (acceleration/velocity) / 斜率计算（加速度/速度） | High | Low-Medium | 📝 *待填入* |
| Calculation of area under graph (displacement) / 图像下面积计算（位移） | High | Medium | 📝 *待填入* |
| Describing motion from a graph / 从图像描述运动 | Medium | Low-Medium | 📝 *待填入* |
| Sketching graphs from description / 根据描述绘制图像 | Medium | Medium | 📝 *待填入* |
| Converting between graph types / 图像类型转换 | Low-Medium | Medium-High | 📝 *待填入* |
| Drawing tangents for instantaneous values / 画切线求瞬时值 | Medium | Medium | 📝 *待填入* |
| Multi-stage motion problems / 多阶段运动问题 | High | Medium-High | 📝 *待填入* |
| Free fall graph interpretation / 自由落体图像解读 | Medium | Medium | 📝 *待填入* |

> 📝 **题库整理中 / Question Bank Under Construction:** 具体试卷编号（如 9702/23/M/J/24 Q3）将在后续整理真题后填入上表。

**Common Command Words / 常见指令词:**

| Command Word (EN) | Command Word (CN) | What to Do |
|-------------------|-------------------|------------|
| State / 陈述 | 陈述 | Give a brief answer without explanation |
| Define / 定义 | 定义 | Give the precise meaning |
| Explain / 解释 | 解释 | Give reasons or causes |
| Describe / 描述 | 描述 | Give a detailed account |
| Calculate / 计算 | 计算 | Use mathematics to find a numerical answer |
| Determine / 确定 | 确定 | Find a value using given data |
| Suggest / 建议 | 建议 | Give a possible answer based on reasoning |
| Sketch / 绘制 | 绘制 | Draw a graph showing general shape and key features |
| Interpret / 解读 | 解读 | Explain the meaning of data or a graph |

---

# 10. Practical Skills Connections / 实验技能链接

**English:**
Motion graphs are closely linked to practical work in both CAIE and Edexcel specifications.

**CAIE Paper 3 (AS) / Paper 5 (A2):**
- **Measurement techniques:** Using ticker timers, light gates, and motion sensors to collect displacement and time data
- **Data analysis:** Plotting displacement-time and velocity-time graphs from experimental data
- **Graphical analysis:** Drawing lines of best fit, calculating gradients, and determining areas
- **Uncertainties:** Estimating uncertainty in gradient calculations from tangent drawing; using error bars on graphs
- **Experimental design:** Setting up experiments to investigate motion (e.g., trolley on a ramp, free fall apparatus)

**Edexcel Unit 3 (AS) / Unit 6 (A2):**
- **Core practical 1:** Determine the acceleration of a freely falling object using a light gate and data logger
- **Core practical 2:** Investigate the relationship between force, mass, and acceleration using motion graphs
- **Data logging:** Using software to generate real-time velocity-time graphs
- **Analysis:** Using gradients and areas from experimental graphs to determine physical quantities

**Key practical skills:**
1. **Using a ticker timer:** Attach ticker tape to a moving object; the dots on the tape represent position at regular time intervals. The spacing between dots indicates velocity (wider spacing = faster).
2. **Using light gates:** Measure the time for an object to pass through a gate; calculate instantaneous velocity using v = length of object / time.
3. **Using motion sensors:** Ultrasonic or infrared sensors can generate real-time displacement-time graphs on a computer.
4. **Graph plotting:** Plot displacement against time; draw a smooth curve or line of best fit; calculate gradient at specific points using tangents.

**中文：**
运动图像与CAIE和Edexcel大纲中的实验工作密切相关。

**CAIE 试卷3（AS）/ 试卷5（A2）：**
- **测量技术：** 使用打点计时器、光门和运动传感器收集位移和时间数据
- **数据分析：** 从实验数据绘制位移-时间图和速度-时间图
- **图形分析：** 画最佳拟合线、计算斜率和确定面积
- **不确定度：** 估计从切线绘制中斜率计算的不确定度；在图上使用误差棒
- **实验设计：** 设置实验以研究运动（例如，斜坡上的小车、自由落体装置）

**Edexcel 单元3（AS）/ 单元6（A2）：**
- **核心实验1：** 使用光门和数据记录器确定自由落体物体的加速度
- **核心实验2：** 使用运动图像研究力、质量和加速度之间的关系
- **数据记录：** 使用软件生成实时的速度-时间图
- **分析：** 使用实验图像中的斜率和面积来确定物理量

**关键实验技能：**
1. **使用打点计时器：** 将打点纸带连接到运动物体上；纸带上的点表示在规则时间间隔的位置。点之间的间距表示速度（间距越宽 = 速度越快）。
2. **使用光门：** 测量物体通过光门的时间；使用v = 物体长度 / 时间计算瞬时速度。
3. **使用运动传感器：** 超声波或红外传感器可以在计算机上生成实时的位移-时间图。
4. **图表绘制：** 绘制位移对时间的图；画平滑曲线或最佳拟合线；使用切线计算特定点的斜率。

> 📋 **CIE Only:** CAIE Paper 3 often requires students to draw tangents on displacement-time graphs to find instantaneous velocity. Practice this skill with curved graphs.
>
> 📋 **Edexcel Only:** Edexcel Unit 3 core practicals specifically require using light gates and data loggers to generate velocity-time graphs for free-fall experiments.

---

# 11. Concept Map / 概念图谱

```mermaid
graph TD
    %% Main Topic
    MG[Motion Graphs] --> DTG[Displacement-Time Graphs]
    MG --> VTG[Velocity-Time Graphs]
    MG --> ATG[Acceleration-Time Graphs]
    MG --> IGA[Interpreting Gradient and Area]
    
    %% Prerequisites
    DVA[Displacement, Velocity and Acceleration] --> MG
    
    %% Related Topics
    MG --> SUVAT[Equations of Motion (SUVAT)]
    
    %% Sub-topics connections
    DTG --> |Gradient gives| VEL[Velocity]
    VTG --> |Gradient gives| ACC[Acceleration]
    VTG --> |Area gives| DISP[Displacement]
    ATG --> |Area gives| DVEL[Change in Velocity]
    
    %% Graph relationships
    DTG --> |Differentiate| VTG
    VTG --> |Differentiate| ATG
    ATG --> |Integrate| VTG
    VTG --> |Integrate| DTG
    
    %% Practical connections
    MG --> PRAC[Practical Skills]
    PRAC --> TG[Ticker Timer Graphs]
    PRAC --> LG[Light Gate Data]
    PRAC --> MS[Motion Sensors]
    
    %% Exam connections
    MG --> EXAM[Exam Questions]
    EXAM --> CALC[Calculations]
    EXAM --> SKETCH[Sketching]
    EXAM --> INTERP[Interpretation]
    
    %% Styling
    classDef main fill:#4a90d9,stroke:#2c5f8a,color:white
    classDef sub fill:#6abf69,stroke:#3d8b3d,color:white
    classDef related fill:#e6a817,stroke:#b8860b,color:white
    classDef practical fill:#d94a4a,stroke:#8b2c2c,color:white
    
    class MG main
    class DTG,VTG,ATG,IGA sub
    class DVA,SUVAT related
    class PRAC,TG,LG,MS practical
```

**English:**
The concept map shows that [[Motion Graphs]] is the central topic that connects [[Displacement, Velocity and Acceleration]] (prerequisite) to [[Equations of Motion (SUVAT)]] (related topic). The three graph types (displacement-time, velocity-time, acceleration-time) are connected through differentiation and integration. The key skills of [[Interpreting Gradient and Area]] link to practical work and exam questions.

**中文：**
概念图显示[[运动图像]]是中心主题，将[[位移、速度和加速度]]（先决条件）连接到[[运动学方程（SUVAT）]]（相关主题）。三种图像类型（位移-时间、速度-时间、加速度-时间）通过微分和积分相互连接。[[解释斜率和面积]]的关键技能连接到实验工作和考试问题。

---

# 12. Quick Revision Sheet / 速查表

| Category / 类别 | Key Points / 要点 |
|----------------|------------------|
| **Definitions / 定义** | • **Displacement-time graph:** Shows position vs time; gradient = velocity<br>• **Velocity-time graph:** Shows velocity vs time; gradient = acceleration; area = displacement<br>• **Acceleration-time graph:** Shows acceleration vs time; area = change in velocity<br>• **位移-时间图：** 显示位置随时间变化；斜率 = 速度<br>• **速度-时间图：** 显示速度随时间变化；斜率 = 加速度；面积 = 位移<br>• **加速度-时间图：** 显示加速度随时间变化；面积 = 速度变化量 |
| **Equations / 公式** | • Gradient: $m = \frac{\Delta y}{\Delta x} = \frac{y_2 - y_1}{x_2 - x_1}$<br>• Area (triangle): $A = \frac{1}{2} \times \text{base} \times \text{height}$<br>• Area (rectangle): $A = \text{base} \times \text{height}$<br>• Area (trapezium): $A = \frac{1}{2}(a + b)h$<br>• Instantaneous gradient: $\frac{dy}{dx} = \lim_{\Delta x \to 0} \frac{\Delta y}{\Delta x}$ |
| **Graphs / 图表** | • **s-t graph:** Straight line = constant velocity; Curve = acceleration; Horizontal = stationary<br>• **v-t graph:** Horizontal = constant velocity; Straight slope = constant acceleration; Area = displacement<br>• **a-t graph:** Horizontal = constant acceleration; Area = change in velocity<br>• **s-t图：** 直线 = 匀速；曲线 = 加速；水平 = 静止<br>• **v-t图：** 水平 = 匀速；直线斜率 = 匀变速；面积 = 位移<br>• **a-t图：** 水平 = 匀变速；面积 = 速度变化量 |
| **Key Facts / 关键事实** | • Gradient of s-t = velocity; Gradient of v-t = acceleration<br>• Area under v-t = displacement; Area under a-t = change in velocity<br>• For curved graphs, use tangent for instantaneous values<br>• For total distance, add absolute values of areas (ignore sign)<br>• s-t的斜率 = 速度；v-t的斜率 = 加速度<br>• v-t下的面积 = 位移；a-t下的面积 = 速度变化量<br>• 对于曲线图，使用切线求瞬时值<br>• 对于总路程，将面积的绝对值相加（忽略符号） |
| **Exam Reminders / 考试提醒** | • Always check units before calculating gradients/areas<br>• Show working: draw tangents, show triangles for gradient, show shapes for area<br>• Distinguish between instantaneous and average values<br>• Remember sign conventions: positive/negative for direction<br>• For free fall: a = g = 9.81 m s⁻² (constant)<br>• 在计算斜率/面积前始终检查单位<br>• 展示计算过程：画切线、显示用于斜率的三角形、显示用于面积的形状<br>• 区分瞬时值和平均值<br>• 记住符号约定：正/负表示方向<br>• 对于自由落体：a = g = 9.81 m s⁻²（常数） |

---

**End of Motion Graphs Knowledge Graph Node / 运动图像知识图谱节点结束**