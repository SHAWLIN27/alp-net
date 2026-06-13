# 1. Overview / 概述

**English:**
This sub-topic focuses on the fundamental technique of resolving projectile motion into independent horizontal and vertical components. This is the cornerstone of analyzing any projectile problem. By treating the motion in two perpendicular directions separately, we can apply the [[Equations of Motion (SUVAT)]] to each component, dramatically simplifying complex curved trajectories. Understanding this decomposition is essential for solving all projectile motion problems, including calculating [[Time of Flight and Range]], [[Maximum Height]], and interpreting [[Projectile Motion Graphs]]. This concept directly builds on [[Scalars and Vectors]] and is a prerequisite for applying [[Newton's Laws of Motion]] to two-dimensional motion.

**中文:**
本子知识点专注于将抛体运动分解为独立的水平分量和垂直分量这一基本技巧。这是分析任何抛体问题的基石。通过将运动分别处理为两个垂直方向，我们可以对每个分量应用[[Equations of Motion (SUVAT)]]，从而极大地简化复杂的曲线轨迹。理解这种分解对于解决所有抛体运动问题至关重要，包括计算[[Time of Flight and Range]]、[[Maximum Height]]以及解读[[Projectile Motion Graphs]]。此概念直接建立在[[Scalars and Vectors]]之上，也是将[[Newton's Laws of Motion]]应用于二维运动的先决条件。

---

# 2. Syllabus Learning Objectives / 考纲学习目标

| CAIE 9702 | Edexcel IAL |
|-----------|-------------|
| 3.1(l) Describe and explain the motion of a projectile as a special case of two-dimensional motion under constant acceleration due to gravity, where air resistance is negligible. | 1.13 Understand that the horizontal and vertical components of a projectile's motion are independent. |
| 3.1(m) Derive and use equations for the horizontal and vertical components of velocity and displacement of a projectile. | 1.14 Use the independence of horizontal and vertical motion to solve problems involving projectiles launched horizontally. |
| | 1.15 Use the independence of horizontal and vertical motion to solve problems involving projectiles launched at an angle to the horizontal. |
| | 1.16 Understand that the horizontal component of velocity remains constant (assuming negligible air resistance), while the vertical component is subject to constant acceleration due to gravity. |

**Examiner Expectations / 考官期望:**
- **English:** You must be able to state that the horizontal and vertical components are independent. You must be able to resolve initial velocity into components using trigonometry. You must apply SUVAT equations separately to each component, recognizing that acceleration only acts vertically ($g$ downwards) and is zero horizontally.
- **中文:** 你必须能够说明水平分量和垂直分量是独立的。你必须能够使用三角函数将初速度分解为分量。你必须分别对每个分量应用SUVAT方程，并认识到加速度仅作用于垂直方向（$g$向下），水平方向为零。

---

# 3. Core Definitions / 核心定义

| Term (EN/CN) | Definition (EN) | Definition (CN) | Common Mistakes / 常见错误 |
|--------------|-----------------|-----------------|---------------------------|
| **Projectile** / 抛体 | An object upon which the only force acting is gravity (air resistance is negligible). | 一个只受重力作用的物体（空气阻力可忽略不计）。 | Confusing a projectile with an object under powered flight (e.g., a rocket with engines on). |
| **Horizontal Component** / 水平分量 | The part of the projectile's velocity or displacement that acts parallel to the ground. It remains constant (zero acceleration) in ideal projectile motion. | 抛体速度或位移中平行于地面的部分。在理想抛体运动中保持不变（加速度为零）。 | Forgetting that horizontal velocity is constant; thinking it changes like vertical velocity. |
| **Vertical Component** / 垂直分量 | The part of the projectile's velocity or displacement that acts perpendicular to the ground. It changes uniformly due to constant acceleration $g$ downwards. | 抛体速度或位移中垂直于地面的部分。由于恒定的向下加速度$g$而均匀变化。 | Using the wrong sign for $g$ (e.g., $+9.81$ when upward is positive). |
| **Independence of Motion** / 运动独立性 | The principle that the horizontal and vertical motions of a projectile do not affect each other; they can be analyzed separately. | 抛体的水平运动和垂直运动互不影响的原则；它们可以分开分析。 | Thinking that the horizontal motion "carries" the vertical motion or vice versa. |
| **Resolution of Velocity** / 速度分解 | The process of splitting an initial velocity vector $u$ at an angle $\theta$ into its horizontal ($u\cos\theta$) and vertical ($u\sin\theta$) components. | 将角度为$\theta$的初速度矢量$u$分解为水平分量（$u\cos\theta$）和垂直分量（$u\sin\theta$）的过程。 | Mixing up $\sin$ and $\cos$; using the wrong angle in the triangle. |

---

# 4. Key Concepts Explained / 关键概念详解

## 4.1 Independence of Horizontal and Vertical Motion / 水平与垂直运动的独立性

### Explanation / 解释
**English:** The most critical concept in projectile motion is that the horizontal and vertical components are **completely independent**. This means:
- The horizontal motion is **not affected** by the vertical motion.
- The vertical motion is **not affected** by the horizontal motion.
- They share only **time** ($t$) as a common variable.

For example, if you drop a ball and throw another ball horizontally from the same height at the same time, they will hit the ground at the **same time** (ignoring air resistance). The horizontal motion of the thrown ball does not "keep it in the air" longer. This is a classic demonstration of independence.

**中文:** 抛体运动中最关键的概念是水平分量和垂直分量**完全独立**。这意味着：
- 水平运动**不受**垂直运动的影响。
- 垂直运动**不受**水平运动的影响。
- 它们仅共享**时间**（$t$）作为共同变量。

例如，如果你从同一高度同时释放一个球和水平抛出另一个球，它们将**同时**落地（忽略空气阻力）。被抛出球的水平运动并不会让它“在空中停留”更长时间。这是独立性的经典演示。

### Physical Meaning / 物理意义
**English:** Physically, this independence arises because the forces acting on the projectile are only in the vertical direction (gravity). There is no horizontal force (assuming no air resistance). According to [[Newton's Laws of Motion]], without a net force, there is no acceleration, so horizontal velocity is constant. The vertical motion is governed solely by gravity.

**中文:** 从物理上讲，这种独立性源于作用在抛体上的力仅在垂直方向（重力）。没有水平方向的力（假设无空气阻力）。根据[[Newton's Laws of Motion]]，没有净力就没有加速度，因此水平速度是恒定的。垂直运动仅由重力支配。

### Common Misconceptions / 常见误区
- **English:**
  - Thinking a projectile travels fastest at the start or end.
  - Believing the horizontal velocity changes.
  - Confusing the path (parabola) with the forces (only gravity).
- **中文:**
  - 认为抛体在开始或结束时运动最快。
  - 相信水平速度会变化。
  - 混淆路径（抛物线）与力（只有重力）。

### Exam Tips / 考试提示
- **English:** Always draw a diagram showing the initial velocity vector resolved into $u_x$ and $u_y$. Label the acceleration $a_x = 0$ and $a_y = -g$ (or $+g$ depending on sign convention). State clearly: "Horizontal: constant velocity. Vertical: constant acceleration."
- **中文:** 始终画一个图，显示初速度矢量分解为$u_x$和$u_y$。标注加速度$a_x = 0$和$a_y = -g$（或$+g$，取决于符号约定）。明确说明：“水平方向：匀速运动。垂直方向：匀加速运动。”

> 📷 **IMAGE PROMPT — DIAG-01: Independence of Motion Demonstration**
> A side-by-side comparison diagram. Left side: A ball dropped vertically from a height H. Right side: A ball thrown horizontally from the same height H with initial horizontal velocity v_x. Both balls are shown at the same vertical positions at times t1, t2, t3, t4, demonstrating they hit the ground at the same time. The horizontally thrown ball also shows its horizontal displacement increasing. Labels: "Same height H", "Same time t", "g = 9.81 m/s²". Clean, educational style.

---

## 4.2 Resolving Initial Velocity / 分解初速度

### Explanation / 解释
**English:** When a projectile is launched with an initial speed $u$ at an angle $\theta$ to the horizontal, we use trigonometry to find its components:
- **Horizontal component:** $u_x = u \cos \theta$
- **Vertical component:** $u_y = u \sin \theta$

These components are then used as the initial conditions ($u$) in the SUVAT equations for each direction. The angle $\theta$ is always measured from the horizontal.

**中文:** 当抛体以初速度$u$和与水平方向夹角$\theta$发射时，我们使用三角函数来求其分量：
- **水平分量：** $u_x = u \cos \theta$
- **垂直分量：** $u_y = u \sin \theta$

这些分量随后被用作每个方向SUVAT方程中的初始条件（$u$）。角度$\theta$始终从水平方向测量。

### Physical Meaning / 物理意义
**English:** The components represent how much of the initial velocity is directed horizontally (moving forward) and how much is directed vertically (moving upward initially). A larger angle means more velocity is directed upward, leading to higher [[Maximum Height]] but shorter [[Time of Flight and Range]] (for a given speed).

**中文:** 这些分量代表了初速度中有多少是水平方向（向前运动）和多少是垂直方向（初始向上运动）。角度越大，意味着更多的速度被导向向上，导致更高的[[Maximum Height]]，但[[Time of Flight and Range]]更短（对于给定的速度）。

### Common Misconceptions / 常见误区
- **English:**
  - Using $\sin$ for horizontal and $\cos$ for vertical.
  - Measuring the angle from the vertical instead of the horizontal.
  - Forgetting to resolve when the projectile is launched horizontally ($\theta = 0^\circ$, so $u_x = u$, $u_y = 0$).
- **中文:**
  - 对水平分量使用$\sin$，对垂直分量使用$\cos$。
  - 从垂直方向而不是水平方向测量角度。
  - 当抛体水平发射时忘记分解（$\theta = 0^\circ$，所以$u_x = u$，$u_y = 0$）。

### Exam Tips / 考试提示
- **English:** Always write down $u_x = u\cos\theta$ and $u_y = u\sin\theta$ explicitly before substituting numbers. For horizontal launches, state $u_x = u$ and $u_y = 0$. Check your calculator is in degree mode.
- **中文:** 在代入数字之前，始终明确写出$u_x = u\cos\theta$和$u_y = u\sin\theta$。对于水平发射，说明$u_x = u$和$u_y = 0$。检查计算器是否处于角度模式。

---

# 5. Essential Equations / 核心公式

## 5.1 Component Resolution Equations / 分量分解方程

$$ u_x = u \cos \theta $$
$$ u_y = u \sin \theta $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $u$ | Initial speed | 初速度 | m s⁻¹ |
| $\theta$ | Launch angle from horizontal | 发射角（与水平方向夹角） | ° (degrees) |
| $u_x$ | Horizontal component of initial velocity | 初速度的水平分量 | m s⁻¹ |
| $u_y$ | Vertical component of initial velocity | 初速度的垂直分量 | m s⁻¹ |

**Conditions / 适用条件:** Any projectile launched at an angle $\theta$ to the horizontal. For horizontal launch, $\theta = 0^\circ$, so $u_x = u$, $u_y = 0$.
**Limitations / 局限性:** Assumes the angle is measured from the horizontal. If given from the vertical, adjust accordingly.

## 5.2 Horizontal Motion Equations (Constant Velocity) / 水平运动方程（匀速）

$$ s_x = u_x t = (u \cos \theta) t $$
$$ v_x = u_x = u \cos \theta $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $s_x$ | Horizontal displacement | 水平位移 | m |
| $v_x$ | Horizontal velocity (constant) | 水平速度（恒定） | m s⁻¹ |
| $t$ | Time | 时间 | s |

**Conditions / 适用条件:** Only valid when air resistance is negligible. $a_x = 0$.
**Limitations / 局限性:** Does not apply if horizontal forces are present (e.g., wind, air resistance).

## 5.3 Vertical Motion Equations (Constant Acceleration) / 垂直运动方程（匀加速）

$$ v_y = u_y + a_y t = u \sin \theta - gt $$
$$ s_y = u_y t + \frac{1}{2} a_y t^2 = (u \sin \theta) t - \frac{1}{2} g t^2 $$
$$ v_y^2 = u_y^2 + 2 a_y s_y = (u \sin \theta)^2 - 2g s_y $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $v_y$ | Vertical velocity at time $t$ | 时刻$t$的垂直速度 | m s⁻¹ |
| $s_y$ | Vertical displacement (from launch point) | 垂直位移（从发射点起） | m |
| $a_y$ | Vertical acceleration ($-g$) | 垂直加速度（$-g$） | m s⁻² |
| $g$ | Acceleration due to gravity ($9.81$ m s⁻²) | 重力加速度（$9.81$ m s⁻²） | m s⁻² |

**Conditions / 适用条件:** Constant acceleration $g$ downwards. Sign convention: upward positive, so $a_y = -g$.
**Limitations / 局限性:** Assumes $g$ is constant and air resistance is negligible. Near Earth's surface only.

> 📷 **IMAGE PROMPT — DIAG-02: Velocity Components at Different Points**
> A diagram showing a projectile's parabolic trajectory. At three points (launch, apex, and a point on the descent), the velocity vector is shown as an arrow. At each point, the arrow is resolved into horizontal (v_x, constant length) and vertical (v_y, changing length) components. At the apex, v_y = 0. Labels: "v_x constant", "v_y decreasing", "v_y = 0 at apex". Clean, educational style with arrows.

---

# 6. Graphs and Relationships / 图表与关系

## 6.1 Horizontal Velocity vs. Time / 水平速度-时间图

### Axes / 坐标轴
- **x-axis:** Time / 时间 $t$ (s)
- **y-axis:** Horizontal velocity / 水平速度 $v_x$ (m s⁻¹)

### Shape / 形状
A horizontal straight line (constant value).

### Gradient Meaning / 斜率含义
Gradient = 0, representing zero horizontal acceleration ($a_x = 0$).

### Area Meaning / 面积含义
Area under the line = horizontal displacement $s_x = v_x \times t$.

### Exam Interpretation / 考试解读
**English:** This graph confirms that horizontal velocity is constant. Any deviation from a horizontal line would indicate horizontal acceleration (e.g., air resistance).
**中文:** 该图证实了水平速度是恒定的。任何偏离水平线的现象都表明存在水平加速度（例如空气阻力）。

## 6.2 Vertical Velocity vs. Time / 垂直速度-时间图

### Axes / 坐标轴
- **x-axis:** Time / 时间 $t$ (s)
- **y-axis:** Vertical velocity / 垂直速度 $v_y$ (m s⁻¹)

### Shape / 形状
A straight line with negative gradient (downward slope).

### Gradient Meaning / 斜率含义
Gradient = $a_y = -g = -9.81$ m s⁻². The slope is constant, confirming constant acceleration.

### Area Meaning / 面积含义
Area under the line = vertical displacement $s_y$. Area above the x-axis represents upward displacement; area below represents downward displacement.

### Exam Interpretation / 考试解读
**English:** The line crosses the x-axis ($v_y = 0$) at the time of maximum height. The time from launch to this crossing is half the total [[Time of Flight and Range]]. The symmetry of the graph (equal positive and negative areas) indicates the projectile returns to its launch height.
**中文:** 该线与x轴相交（$v_y = 0$）的时刻对应最大高度。从发射到该交点的时间是总[[Time of Flight and Range]]的一半。图的对称性（正负面积相等）表明抛体返回其发射高度。

> 📷 **IMAGE PROMPT — GRAPH-01: Vertical Velocity vs Time for a Projectile**
> A graph with time on the x-axis (0 to T, where T is total time of flight) and vertical velocity v_y on the y-axis. A straight line starts at +u_y (positive), crosses zero at t = T/2 (apex), and reaches -u_y at t = T. The gradient is labeled as "-g". The area under the line is shaded to show displacement. Clean, educational graph style.

---

# 7. Required Diagrams / 必备图表

## 7.1 Initial Velocity Resolution Diagram / 初速度分解图

### Description / 描述
**English:** A right-angled triangle diagram showing the initial velocity vector $u$ at an angle $\theta$ to the horizontal. The horizontal side is labeled $u_x = u\cos\theta$, and the vertical side is labeled $u_y = u\sin\theta$.
**中文:** 一个直角三角形图，显示与水平方向夹角为$\theta$的初速度矢量$u$。水平边标注为$u_x = u\cos\theta$，垂直边标注为$u_y = u\sin\theta$。

### Image Prompt / 图片生成提示
> 📷 **IMAGE PROMPT — DIAG-03: Initial Velocity Resolution**
> A right-angled triangle. The hypotenuse is a vector arrow labeled "u (initial velocity)" at an angle θ from the horizontal base. The horizontal adjacent side is a vector arrow labeled "u_x = u cos θ". The vertical opposite side is a vector arrow labeled "u_y = u sin θ". The right angle is marked. The angle θ is shown between the hypotenuse and the horizontal side. Clean, educational diagram with clear labels and arrows.

### Labels Required / 需要标注
- Hypotenuse: $u$ (initial velocity / 初速度)
- Horizontal side: $u_x = u \cos \theta$ (horizontal component / 水平分量)
- Vertical side: $u_y = u \sin \theta$ (vertical component / 垂直分量)
- Angle: $\theta$ (launch angle / 发射角)

### Exam Importance / 考试重要性
**English:** This diagram is essential for setting up any projectile problem. Drawing it correctly ensures you use the correct trigonometric functions and avoid sign errors.
**中文:** 此图对于建立任何抛体问题至关重要。正确绘制它可确保你使用正确的三角函数并避免符号错误。

## 7.2 Complete Projectile Motion Diagram / 完整抛体运动图

### Description / 描述
**English:** A parabolic trajectory showing the projectile at multiple points (launch, apex, landing). At each point, the velocity vector is shown and resolved into components. The constant horizontal velocity and changing vertical velocity are highlighted.
**中文:** 一条抛物线轨迹，显示抛体在多个点（发射点、最高点、落地点）的状态。在每个点，速度矢量被显示并分解为分量。恒定的水平速度和变化的垂直速度被突出显示。

### Image Prompt / 图片生成提示
> 📷 **IMAGE PROMPT — DIAG-04: Complete Projectile Motion with Components**
> A parabolic arc from left to right. At the launch point (left), a velocity vector is resolved into u_x (horizontal, rightward) and u_y (vertical, upward). At the apex (top of arc), only a horizontal velocity vector v_x is shown (v_y = 0). At a point on the descent (right), the velocity vector is resolved into v_x (horizontal, same length as at launch) and v_y (vertical, downward, longer than at launch). Labels: "u_x constant", "v_y = 0 at apex", "g = 9.81 m/s² downward". Clean, educational style.

### Labels Required / 需要标注
- Launch point: $u_x$, $u_y$, $\theta$
- Apex: $v_x$, $v_y = 0$
- Landing point: $v_x$, $v_y$ (downward)
- Acceleration: $g$ (downward arrow)

### Exam Importance / 考试重要性
**English:** This diagram helps visualize the independence of components and is crucial for understanding [[Projectile Motion Graphs]] and solving problems involving [[Time of Flight and Range]] and [[Maximum Height]].
**中文:** 此图有助于可视化分量的独立性，对于理解[[Projectile Motion Graphs]]以及解决涉及[[Time of Flight and Range]]和[[Maximum Height]]的问题至关重要。

---

# 8. Worked Examples / 典型例题

## Example 1: Horizontal Launch / 水平发射

### Question / 题目
**English:** A ball is thrown horizontally from a cliff of height 45 m with an initial speed of 20 m s⁻¹. Calculate:
(a) The time taken for the ball to reach the ground.
(b) The horizontal distance from the base of the cliff where the ball lands.
(Take $g = 9.81$ m s⁻², ignore air resistance.)

**中文:** 一个球从45米高的悬崖上以20 m s⁻¹的初速度水平抛出。计算：
(a) 球到达地面所需的时间。
(b) 球落地时距悬崖底部的水平距离。
（取$g = 9.81$ m s⁻²，忽略空气阻力。）

### Solution / 解答

**Step 1: Resolve components / 分解分量**
Since the launch is horizontal ($\theta = 0^\circ$):
$$ u_x = u \cos 0^\circ = 20 \times 1 = 20 \text{ m s}^{-1} $$
$$ u_y = u \sin 0^\circ = 20 \times 0 = 0 \text{ m s}^{-1} $$

**Step 2: Vertical motion (find time) / 垂直运动（求时间）**
Use $s_y = u_y t + \frac{1}{2} a_y t^2$
Take downward as positive: $s_y = +45$ m, $u_y = 0$, $a_y = +g = +9.81$ m s⁻²
$$ 45 = 0 \times t + \frac{1}{2} \times 9.81 \times t^2 $$
$$ 45 = 4.905 t^2 $$
$$ t^2 = \frac{45}{4.905} = 9.174 $$
$$ t = \sqrt{9.174} = 3.03 \text{ s} $$

**Step 3: Horizontal motion (find range) / 水平运动（求射程）**
Use $s_x = u_x t$ (constant velocity)
$$ s_x = 20 \times 3.03 = 60.6 \text{ m} $$

### Final Answer / 最终答案
**Answer:** (a) $t = 3.03$ s | **答案：** (a) $t = 3.03$ 秒
**Answer:** (b) $s_x = 60.6$ m | **答案：** (b) $s_x = 60.6$ 米

### Quick Tip / 提示
**English:** For horizontal launches, the vertical motion is identical to free fall from rest. The time to hit the ground depends only on height, not on horizontal speed.
**中文:** 对于水平发射，垂直运动等同于从静止开始的自由落体。落地时间仅取决于高度，与水平速度无关。

---

## Example 2: Angled Launch / 倾斜发射

### Question / 题目
**English:** A projectile is launched with an initial velocity of 30 m s⁻¹ at an angle of 40° to the horizontal. Calculate:
(a) The horizontal and vertical components of the initial velocity.
(b) The vertical velocity after 2.0 seconds.
(Take $g = 9.81$ m s⁻², ignore air resistance.)

**中文:** 一个抛体以30 m s⁻¹的初速度、与水平方向成40°角发射。计算：
(a) 初速度的水平分量和垂直分量。
(b) 2.0秒后的垂直速度。
（取$g = 9.81$ m s⁻²，忽略空气阻力。）

### Solution / 解答

**Step 1: Resolve components / 分解分量**
$$ u_x = u \cos \theta = 30 \times \cos 40^\circ = 30 \times 0.7660 = 22.98 \text{ m s}^{-1} $$
$$ u_y = u \sin \theta = 30 \times \sin 40^\circ = 30 \times 0.6428 = 19.28 \text{ m s}^{-1} $$

**Step 2: Vertical velocity after 2.0 s / 2.0秒后的垂直速度**
Use $v_y = u_y + a_y t$
Take upward as positive: $u_y = +19.28$ m s⁻¹, $a_y = -g = -9.81$ m s⁻², $t = 2.0$ s
$$ v_y = 19.28 + (-9.81) \times 2.0 $$
$$ v_y = 19.28 - 19.62 = -0.34 \text{ m s}^{-1} $$

The negative sign indicates the projectile is moving downward after 2.0 seconds.

### Final Answer / 最终答案
**Answer:** (a) $u_x = 23.0$ m s⁻¹, $u_y = 19.3$ m s⁻¹ | **答案：** (a) $u_x = 23.0$ m s⁻¹, $u_y = 19.3$ m s⁻¹
**Answer:** (b) $v_y = -0.34$ m s⁻¹ (downward) | **答案：** (b) $v_y = -0.34$ m s⁻¹（向下）

### Quick Tip / 提示
**English:** The negative vertical velocity means the projectile has passed its maximum height and is descending. At the apex, $v_y = 0$.
**中文:** 负的垂直速度意味着抛体已经过了其最大高度并正在下降。在最高点，$v_y = 0$。

---

# 9. Past Paper Question Types / 历年真题题型

| Question Type / 题型 | Frequency / 频率 | Difficulty / 难度 | Past Paper References / 真题索引 |
|----------------------|------------------|------------------|-------------------------------|
| Resolve initial velocity into components | Very High / 非常高 | Easy / 简单 | 📝 *待填入* |
| Calculate time of flight from vertical motion | High / 高 | Medium / 中等 | 📝 *待填入* |
| Calculate range from horizontal motion | High / 高 | Medium / 中等 | 📝 *待填入* |
| Find velocity at a given time (magnitude and direction) | Medium / 中等 | Medium-Hard / 中高 | 📝 *待填入* |
| Multi-step problem combining both components | High / 高 | Hard / 困难 | 📝 *待填入* |

**Common Command Words / 常见指令词:**
- **English:** "Calculate", "Determine", "Find", "Show that", "State", "Explain why"
- **中文:** "计算"、"确定"、"求"、"证明"、"说明"、"解释为什么"

---

# 10. Practical Skills Connections / 实验技能链接

**English:**
This sub-topic connects to practical work in several ways:
1. **Measurements:** Measuring initial speed (e.g., using a light gate) and launch angle (using a protractor or inclinometer).
2. **Data Collection:** Recording horizontal and vertical positions of a projectile (e.g., using video analysis software like Tracker or Logger Pro).
3. **Graph Plotting:** Plotting $s_y$ vs. $t$ or $v_y$ vs. $t$ to determine $g$ from the gradient.
4. **Uncertainties:** Estimating uncertainties in angle measurement ($\pm 1^\circ$) and time measurement, and propagating them to find uncertainty in calculated range or time of flight.
5. **Experimental Design:** Designing an experiment to verify the independence of horizontal and vertical motion (e.g., the "monkey and hunter" demonstration or the simultaneous drop and horizontal throw).

**中文:**
本子知识点通过多种方式与实验工作相关联：
1. **测量：** 测量初速度（例如使用光门）和发射角（使用量角器或倾角仪）。
2. **数据收集：** 记录抛体的水平和垂直位置（例如使用视频分析软件，如Tracker或Logger Pro）。
3. **绘图：** 绘制$s_y$与$t$或$v_y$与$t$的关系图，以从斜率确定$g$。
4. **不确定度：** 估计角度测量（$\pm 1^\circ$）和时间测量的不确定度，并传递它们以找到计算出的射程或飞行时间的不确定度。
5. **实验设计：** 设计实验以验证水平和垂直运动的独立性（例如“猴子和猎人”演示或同时下落和水平抛出的实验）。

---

# 11. Concept Map / 概念图谱

```mermaid
graph TD
    %% Core Node
    A[Horizontal and Vertical Components] --> B[Independence of Motion]
    A --> C[Resolution of Initial Velocity]
    A --> D[Applying SUVAT Separately]

    %% Connections to Prerequisites
    A --> E[[Scalars and Vectors]]
    A --> F[[Equations of Motion (SUVAT)]]

    %% Connections to Sibling Topics
    A --> G[[Time of Flight and Range]]
    A --> H[[Maximum Height]]
    A --> I[[Projectile Motion Graphs]]

    %% Connections to Related Topics
    A --> J[[Newton's Laws of Motion]]

    %% Sub-components of Independence
    B --> K[Horizontal: Constant Velocity]
    B --> L[Vertical: Constant Acceleration g]

    %% Sub-components of Resolution
    C --> M[u_x = u cos θ]
    C --> N[u_y = u sin θ]

    %% Sub-components of SUVAT application
    D --> O[s_x = u_x t]
    D --> P[v_y = u_y - gt]
    D --> Q[s_y = u_y t - ½gt²]

    %% Styling
    style A fill:#4a90d9,stroke:#2c3e50,color:#ffffff
    style B fill:#e74c3c,stroke:#2c3e50,color:#ffffff
    style C fill:#27ae60,stroke:#2c3e50,color:#ffffff
    style D fill:#f39c12,stroke:#2c3e50,color:#ffffff
    style E fill:#95a5a6,stroke:#2c3e50,color:#ffffff
    style F fill:#95a5a6,stroke:#2c3e50,color:#ffffff
    style G fill:#8e44ad,stroke:#2c3e50,color:#ffffff
    style H fill:#8e44ad,stroke:#2c3e50,color:#ffffff
    style I fill:#8e44ad,stroke:#2c3e50,color:#ffffff
    style J fill:#d35400,stroke:#2c3e50,color:#ffffff
```

---

# 12. Quick Revision Sheet / 速查表

| Category / 类别 | Key Points / 要点 |
|----------------|------------------|
| **Definition / 定义** | Horizontal and vertical motions are **independent**. They share only time $t$. / 水平和垂直运动是**独立的**。它们仅共享时间$t$。 |
| **Key Formula / 核心公式** | $u_x = u \cos \theta$, $u_y = u \sin \theta$ <br> Horizontal: $s_x = u_x t$, $v_x = \text{constant}$ <br> Vertical: $v_y = u_y - gt$, $s_y = u_y t - \frac{1}{2}gt^2$ |
| **Key Graph / 核心图表** | $v_y$ vs $t$: Straight line with gradient $-g$. Crosses x-axis at apex. / $v_y$与$t$：斜率为$-g$的直线。在最高点与x轴相交。 |
| **Exam Tip / 考试提示** | Always resolve first! Draw the triangle. Check sign convention for $g$. For horizontal launches, $u_y = 0$. / 始终先分解！画三角形。检查$g$的符号约定。对于水平发射，$u_y = 0$。 |
| **Common Mistake / 常见错误** | Thinking horizontal velocity changes. Forgetting $g$ only acts vertically. Using wrong trig function ($\sin$ vs $\cos$). / 认为水平速度会变化。忘记$g$只作用于垂直方向。使用错误的三角函数（$\sin$与$\cos$）。 |
| **Practical Link / 实验联系** | Use video analysis to plot $s_y$ vs $t$ and find $g$ from gradient. / 使用视频分析绘制$s_y$与$t$的关系图，并从斜率求$g$。 |