---
# Acceleration / 加速度

---

# 1. Overview / 概述

**English:**
Acceleration is a fundamental vector quantity in kinematics that describes the rate of change of velocity with respect to time. Unlike speed, which only tells you how fast something is moving, acceleration tells you how quickly the velocity is changing — whether that means speeding up, slowing down (deceleration), or changing direction. This sub-topic is essential for understanding [[Equations of Motion (SUVAT)]], [[Motion Graphs]], and real-world phenomena like [[Terminal Velocity]]. It builds directly on the concepts of [[Displacement and Distance]] and [[Speed and Velocity]], and relies on a solid understanding of [[Scalars and Vectors]].

**中文:**
加速度是运动学中一个基本的矢量量，它描述了速度随时间的变化率。与速度不同，速度只告诉你物体运动有多快，而加速度则告诉你速度变化的快慢——无论是加速、减速（负加速度）还是改变方向。本子知识点是理解[[Equations of Motion (SUVAT)]]、[[Motion Graphs]]以及[[Terminal Velocity]]等现实世界现象的基础。它直接建立在[[Displacement and Distance]]和[[Speed and Velocity]]的概念之上，并需要扎实理解[[Scalars and Vectors]]。

---

# 2. Syllabus Learning Objectives / 考纲学习目标

| CAIE 9702 (3.1 d-f) | Edexcel IAL (WPH11 U1: 1.4-1.8) |
|-----------|-------------|
| Define and use acceleration as $a = \frac{\Delta v}{\Delta t}$ | Define and use acceleration as $a = \frac{\Delta v}{\Delta t}$ |
| Interpret velocity-time graphs to determine acceleration | Use velocity-time graphs to determine acceleration |
| Apply the equations of motion for constant acceleration | Derive and apply the equations of motion for constant acceleration |

**Examiner Expectations / 考官期望:**
- **EN:** You must be able to distinguish between acceleration as a vector and speed as a scalar. You must be able to calculate acceleration from a change in velocity and time, and interpret acceleration from velocity-time graphs. For constant acceleration, you must be able to apply the SUVAT equations.
- **CN:** 你必须能够区分作为矢量的加速度和作为标量的速率。你必须能够根据速度变化和时间计算加速度，并从速度-时间图中解读加速度。对于匀加速运动，你必须能够应用SUVAT方程。

---

# 3. Core Definitions / 核心定义

| Term (EN/CN) | Definition (EN) | Definition (CN) | Common Mistakes / 常见错误 |
|--------------|-----------------|-----------------|---------------------------|
| **Acceleration** / 加速度 | The rate of change of velocity with respect to time. A vector quantity. | 速度随时间的变化率。一个矢量量。 | Confusing acceleration with speed; thinking negative acceleration always means slowing down. |
| **Deceleration** / 减速 | A negative acceleration that causes a decrease in speed. | 导致速度减小的负加速度。 | Thinking deceleration is a separate quantity; it is just acceleration in the opposite direction to velocity. |
| **Uniform Acceleration** / 匀加速 | Acceleration that is constant in both magnitude and direction. | 大小和方向都恒定的加速度。 | Assuming all motion problems involve uniform acceleration. |
| **Instantaneous Acceleration** / 瞬时加速度 | The acceleration of an object at a specific instant in time. | 物体在某一特定时刻的加速度。 | Confusing it with average acceleration. |
| **Average Acceleration** / 平均加速度 | The total change in velocity divided by the total time taken. | 总速度变化量除以总时间。 | Using it when acceleration is not constant. |

---

# 4. Key Concepts Explained / 关键概念详解

## 4.1 Acceleration as a Vector / 加速度作为矢量

### Explanation / 解释
**English:** Acceleration is a vector quantity, meaning it has both magnitude and direction. The direction of the acceleration is the same as the direction of the change in velocity ($\Delta \vec{v}$). If an object is speeding up, the acceleration is in the same direction as the velocity. If it is slowing down (decelerating), the acceleration is in the opposite direction to the velocity. This is a critical distinction from [[Speed and Velocity]].

**中文:** 加速度是一个矢量量，意味着它既有大小也有方向。加速度的方向与速度变化量 ($\Delta \vec{v}$) 的方向相同。如果物体在加速，加速度与速度方向相同。如果物体在减速，加速度与速度方向相反。这是与[[Speed and Velocity]]的一个关键区别。

### Physical Meaning / 物理意义
**English:** Acceleration tells you how quickly an object's velocity is changing. A car accelerating from 0 to 60 mph in 5 seconds has a larger acceleration than one that takes 10 seconds. A ball thrown upwards has a constant downward acceleration due to gravity ($g$) even as it rises and slows down.

**中文:** 加速度告诉你物体速度变化的快慢。一辆在5秒内从0加速到60英里/小时的汽车，其加速度比需要10秒的汽车更大。一个向上抛出的球，即使在上升和减速过程中，也受到恒定的向下重力加速度 ($g$)。

### Common Misconceptions / 常见误区
- **EN:** "Negative acceleration always means slowing down." — *False.* If velocity is also negative, a negative acceleration means speeding up in the negative direction.
- **CN:** “负加速度总是意味着减速。” — *错误。* 如果速度也是负的，那么负加速度意味着在负方向上加速。
- **EN:** "Acceleration is just about getting faster." — *False.* Acceleration includes slowing down and changing direction.
- **CN:** “加速度只是关于变快。” — *错误。* 加速度包括减速和改变方向。

### Exam Tips / 考试提示
- **EN:** Always define a positive direction. A negative acceleration means acceleration in the opposite direction.
- **CN:** 始终定义一个正方向。负加速度意味着相反方向上的加速度。

## 4.2 Uniform vs. Non-Uniform Acceleration / 匀加速与非匀加速

### Explanation / 解释
**English:** Uniform acceleration (constant acceleration) is a special case where the velocity changes by the same amount every second. This is the foundation for the [[Equations of Motion (SUVAT)]]. Non-uniform acceleration is more common in real life (e.g., a car accelerating from rest, then cruising, then braking). For non-uniform acceleration, we use average acceleration or calculus.

**中文:** 匀加速（恒定加速度）是一种特殊情况，即速度每秒变化相同的量。这是[[Equations of Motion (SUVAT)]]的基础。非匀加速在现实生活中更常见（例如，汽车从静止加速，然后匀速行驶，最后刹车）。对于非匀加速，我们使用平均加速度或微积分。

### Physical Meaning / 物理意义
**English:** A constant acceleration means a straight line on a velocity-time graph. A changing acceleration means a curved line.

**中文:** 恒定的加速度意味着速度-时间图上是一条直线。变化的加速度意味着一条曲线。

### Common Misconceptions / 常见误区
- **EN:** "All motion problems use uniform acceleration." — *False.* Only problems that state "constant acceleration" or involve free fall under gravity (ignoring air resistance) use SUVAT.
- **CN:** “所有的运动问题都使用匀加速。” — *错误。* 只有那些说明“恒定加速度”或涉及重力下的自由落体（忽略空气阻力）的问题才使用SUVAT。

### Exam Tips / 考试提示
- **EN:** If a question says "constant acceleration," you can use SUVAT. If it doesn't, you may need to use a velocity-time graph or calculus.
- **CN:** 如果问题说“恒定加速度”，你可以使用SUVAT。如果没有，你可能需要使用速度-时间图或微积分。

---

# 5. Essential Equations / 核心公式

## 5.1 Definition of Acceleration / 加速度的定义

$$ a = \frac{\Delta v}{\Delta t} = \frac{v - u}{t} $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $a$ | Acceleration | 加速度 | $\text{m s}^{-2}$ |
| $\Delta v$ | Change in velocity | 速度变化量 | $\text{m s}^{-1}$ |
| $v$ | Final velocity | 末速度 | $\text{m s}^{-1}$ |
| $u$ | Initial velocity | 初速度 | $\text{m s}^{-1}$ |
| $t$ | Time taken | 所用时间 | $\text{s}$ |

**Derivation / 推导:** This is the definition of average acceleration. For uniform acceleration, it equals instantaneous acceleration.

**Conditions / 适用条件:** Always applicable for calculating average acceleration. For instantaneous acceleration, $\Delta t$ must approach zero.

**Limitations / 局限性:** This equation gives average acceleration. It does not describe how acceleration changes within the time interval.

> 📷 **IMAGE PROMPT — ACC-01: Acceleration Definition Diagram**
> A simple diagram showing a car moving from left to right. At time t=0, it has velocity u. At time t, it has velocity v. An arrow labeled "a = (v-u)/t" points between the two states. The car is shown with a speedometer showing increasing speed.

## 5.2 Acceleration from Velocity-Time Graph / 从速度-时间图求加速度

$$ a = \text{gradient of } v-t \text{ graph} $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $a$ | Acceleration | 加速度 | $\text{m s}^{-2}$ |
| gradient | Slope of the line | 线的斜率 | $\text{m s}^{-2}$ |

**Derivation / 推导:** From the definition $a = \frac{\Delta v}{\Delta t}$, the gradient of a $v-t$ graph is $\frac{\Delta v}{\Delta t}$.

**Conditions / 适用条件:** For a straight line (uniform acceleration). For a curve, the gradient of the tangent gives instantaneous acceleration.

**Limitations / 局限性:** Only directly applicable to uniform acceleration. For non-uniform acceleration, you must draw tangents.

---

# 6. Graphs and Relationships / 图表与关系

## 6.1 Velocity-Time Graph / 速度-时间图

### Axes / 坐标轴
- **X-axis:** Time / 时间 (s)
- **Y-axis:** Velocity / 速度 ($\text{m s}^{-1}$)

### Shape / 形状
- **Uniform Acceleration:** A straight line with a positive slope (speeding up) or negative slope (slowing down).
- **Non-Uniform Acceleration:** A curved line.

### Gradient Meaning / 斜率含义
- **Gradient = Acceleration / 斜率 = 加速度**
- A steeper slope means a larger acceleration.
- A horizontal line means zero acceleration (constant velocity).

### Area Meaning / 面积含义
- **Area under the graph = Displacement / 图线下面积 = 位移**

### Exam Interpretation / 考试解读
- **EN:** You must be able to read acceleration directly from the gradient. For a curve, draw a tangent at the point of interest and calculate its gradient.
- **CN:** 你必须能够直接从斜率读取加速度。对于曲线，在感兴趣的点画一条切线并计算其斜率。

```mermaid
graph LR
    subgraph Velocity-Time Graph
        A[Time (s)] --> B[Velocity (m/s)]
        B --> C{Gradient = Acceleration}
        C --> D[Positive: Speeding up]
        C --> E[Negative: Slowing down]
        C --> F[Zero: Constant velocity]
    end
```

> 📷 **IMAGE PROMPT — ACC-02: Velocity-Time Graph Examples**
> A set of three velocity-time graphs on the same axes. Graph A: a straight line with positive slope (uniform acceleration). Graph B: a straight line with negative slope (uniform deceleration). Graph C: a horizontal line (constant velocity). Each graph is labeled with its gradient value.

---

# 7. Required Diagrams / 必备图表

## 7.1 Acceleration Vector Diagram / 加速度矢量图

### Description / 描述
**English:** A diagram showing a car moving to the right. Two scenarios: (1) Car speeding up: velocity vector to the right, acceleration vector also to the right. (2) Car slowing down: velocity vector to the right, acceleration vector to the left.

**中文:** 一个显示汽车向右行驶的图。两种情景：(1) 汽车加速：速度矢量向右，加速度矢量也向右。(2) 汽车减速：速度矢量向右，加速度矢量向左。

### Image Prompt / 图片生成提示
> 📷 **IMAGE PROMPT — ACC-03: Acceleration Vector Diagram**
> A clean, educational diagram. Top half: a car moving right with a long velocity arrow (v) pointing right and a shorter acceleration arrow (a) also pointing right. Label: "Speeding Up: a in same direction as v". Bottom half: same car moving right with a long velocity arrow (v) pointing right and a shorter acceleration arrow (a) pointing left. Label: "Slowing Down: a opposite to v".

### Labels Required / 需要标注
- Velocity vector ($\vec{v}$)
- Acceleration vector ($\vec{a}$)
- Direction of motion

### Exam Importance / 考试重要性
- **EN:** Essential for understanding the vector nature of acceleration. Frequently tested in multiple-choice questions.
- **CN:** 对于理解加速度的矢量性质至关重要。常在选择题中考查。

## 7.2 Velocity-Time Graph for Free Fall / 自由落体的速度-时间图

### Description / 描述
**English:** A graph showing velocity against time for an object dropped from rest. The line is straight with a constant positive gradient equal to $g$ (9.81 $\text{m s}^{-2}$).

**中文:** 一个显示从静止释放的物体的速度随时间变化的图。线是直的，具有恒定的正斜率，等于 $g$ (9.81 $\text{m s}^{-2}$)。

### Image Prompt / 图片生成提示
> 📷 **IMAGE PROMPT — ACC-04: Free Fall v-t Graph**
> A velocity-time graph. X-axis: Time (s). Y-axis: Velocity (m/s). A straight line starting from the origin (0,0) with a positive slope. The slope is labeled "g = 9.81 m/s²". The line is labeled "Free Fall (no air resistance)".

### Labels Required / 需要标注
- Gradient = $g$ (acceleration due to gravity)
- Initial velocity = 0
- Time axis
- Velocity axis

### Exam Importance / 考试重要性
- **EN:** A classic example of uniform acceleration. Often used as a starting point for more complex problems involving [[Terminal Velocity]].
- **CN:** 匀加速的经典例子。常作为涉及[[Terminal Velocity]]的更复杂问题的起点。

---

# 8. Worked Examples / 典型例题

## Example 1: Calculating Acceleration / 计算加速度

### Question / 题目
**English:** A car accelerates from rest to a velocity of 20 $\text{m s}^{-1}$ in 5 seconds. Calculate its acceleration.

**中文:** 一辆汽车从静止加速，在5秒内达到20 $\text{m s}^{-1}$ 的速度。计算其加速度。

### Solution / 解答
1. **Identify knowns / 确定已知量:**
   - Initial velocity, $u = 0 \text{ m s}^{-1}$
   - Final velocity, $v = 20 \text{ m s}^{-1}$
   - Time, $t = 5 \text{ s}$

2. **Choose equation / 选择公式:**
   $$ a = \frac{v - u}{t} $$

3. **Substitute / 代入:**
   $$ a = \frac{20 - 0}{5} = \frac{20}{5} = 4 \text{ m s}^{-2} $$

### Final Answer / 最终答案
**Answer:** $4 \text{ m s}^{-2}$ | **答案：** $4 \text{ m s}^{-2}$

### Quick Tip / 提示
- **EN:** Always check units. Acceleration is always in $\text{m s}^{-2}$.
- **CN:** 始终检查单位。加速度的单位总是 $\text{m s}^{-2}$。

## Example 2: Deceleration / 减速

### Question / 题目
**English:** A train is moving at 30 $\text{m s}^{-1}$. It brakes and comes to a stop in 10 seconds. Calculate its deceleration.

**中文:** 一列火车以30 $\text{m s}^{-1}$ 的速度行驶。它刹车并在10秒内停下来。计算其减速度。

### Solution / 解答
1. **Identify knowns / 确定已知量:**
   - Initial velocity, $u = 30 \text{ m s}^{-1}$
   - Final velocity, $v = 0 \text{ m s}^{-1}$
   - Time, $t = 10 \text{ s}$

2. **Choose equation / 选择公式:**
   $$ a = \frac{v - u}{t} $$

3. **Substitute / 代入:**
   $$ a = \frac{0 - 30}{10} = \frac{-30}{10} = -3 \text{ m s}^{-2} $$

### Final Answer / 最终答案
**Answer:** $-3 \text{ m s}^{-2}$ (deceleration of $3 \text{ m s}^{-2}$) | **答案：** $-3 \text{ m s}^{-2}$ (减速度为 $3 \text{ m s}^{-2}$)

### Quick Tip / 提示
- **EN:** A negative acceleration does not mean "bad" — it just means the acceleration is in the opposite direction to the velocity.
- **CN:** 负加速度并不意味着“不好”——它只是意味着加速度与速度方向相反。

---

# 9. Past Paper Question Types / 历年真题题型

| Question Type / 题型 | Frequency / 频率 | Difficulty / 难度 | Past Paper References / 真题索引 |
|----------------------|------------------|------------------|-------------------------------|
| Calculate acceleration from $v$, $u$, $t$ | High | Easy | 📝 *待填入* |
| Interpret acceleration from $v-t$ graph gradient | High | Medium | 📝 *待填入* |
| Distinguish between acceleration and deceleration | Medium | Easy | 📝 *待填入* |
| Apply acceleration in SUVAT problems | High | Medium-Hard | 📝 *待填入* |

**Common Command Words / 常见指令词:**
- **Calculate / 计算:** Use the formula $a = \frac{\Delta v}{\Delta t}$.
- **Determine / 确定:** Often requires reading from a graph.
- **Explain / 解释:** Must discuss the vector nature of acceleration.
- **State / 陈述:** A one-word or one-phrase answer (e.g., "acceleration").

---

# 10. Practical Skills Connections / 实验技能链接

**English:**
Acceleration is a key quantity in practical work. You may be asked to:
- **Measure acceleration** using light gates and a data logger. A card of known length passes through two light gates, and the time is recorded to calculate velocity and then acceleration.
- **Plot a velocity-time graph** from experimental data and determine acceleration from the gradient.
- **Estimate uncertainties** in time and distance measurements, and propagate them to find the uncertainty in acceleration.
- **Design an experiment** to investigate the acceleration of a trolley down a ramp, varying the angle or mass.

**中文:**
加速度是实验工作中的关键量。你可能会被要求：
- **使用光门和数据记录器测量加速度**。一个已知长度的卡片通过两个光门，记录时间以计算速度，然后计算加速度。
- **根据实验数据绘制速度-时间图**，并从斜率确定加速度。
- **估计时间和距离测量的不确定度**，并传播它们以找到加速度的不确定度。
- **设计实验**研究小车沿斜坡下滑的加速度，改变角度或质量。

---

# 11. Concept Map / 概念图谱

```mermaid
graph TD
    subgraph "Acceleration Leaf Node"
        A[Acceleration] --> B[Definition: a = Δv/Δt]
        A --> C[Vector Quantity]
        A --> D[Uniform vs Non-Uniform]
        A --> E[Graphical Interpretation]
        
        B --> F[Average Acceleration]
        B --> G[Instantaneous Acceleration]
        
        C --> H[Direction matters]
        C --> I[Deceleration = opposite direction]
        
        D --> J[SUVAT Equations]
        D --> K[Calculus for non-uniform]
        
        E --> L[v-t graph gradient]
        E --> M[Tangent for instantaneous]
        
        A --> N[Related Topics]
        N --> O[[Displacement, Velocity and Acceleration]]
        N --> P[[Motion Graphs]]
        N --> Q[[Equations of Motion (SUVAT)]]
        N --> R[[Terminal Velocity]]
        N --> S[[Scalars and Vectors]]
    end
```

---

# 12. Quick Revision Sheet / 速查表

| Category / 类别 | Key Points / 要点 |
|----------------|------------------|
| Definition / 定义 | $a = \frac{\Delta v}{\Delta t}$; rate of change of velocity / 速度变化率 |
| Key Formula / 核心公式 | $a = \frac{v - u}{t}$ |
| Key Graph / 核心图表 | $v-t$ graph: gradient = acceleration / 速度-时间图：斜率 = 加速度 |
| Vector Nature / 矢量性质 | Direction of $a$ = direction of $\Delta v$; deceleration = $a$ opposite to $v$ / $a$的方向 = $\Delta v$的方向；减速 = $a$与$v$相反 |
| Common Mistake / 常见错误 | Negative $a$ ≠ always slowing down; check direction of $v$ / 负$a$ ≠ 总是减速；检查$v$的方向 |
| Exam Tip / 考试提示 | Always define a positive direction before solving / 解题前始终定义正方向 |
| Practical Link / 实验联系 | Use light gates to measure $\Delta v$ and $\Delta t$ / 使用光门测量$\Delta v$和$\Delta t$ |