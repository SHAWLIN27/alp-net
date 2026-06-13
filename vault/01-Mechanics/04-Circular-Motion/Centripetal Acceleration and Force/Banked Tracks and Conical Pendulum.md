---
# Banked Tracks and Conical Pendulum / 倾斜轨道与圆锥摆

---

# 1. Overview / 概述

**English:**
This sub-topic extends the concept of [[Centripetal Force]] to two classic real-world scenarios where the centripetal force is provided by a combination of forces rather than a single force. For a **banked track**, the horizontal component of the normal reaction from the road (or track) provides the necessary centripetal force, allowing vehicles to turn safely at high speeds without relying on friction. For a **conical pendulum**, the horizontal component of the tension in the string provides the centripetal force, causing the bob to move in a horizontal circle while the string sweeps out a cone. Understanding these systems requires resolving forces into horizontal and vertical components and applying [[Newton's Laws of Motion]] in two dimensions. This is a key application of [[Centripetal Acceleration Formula]] and is essential for understanding [[Circular Orbits]] and [[Gravitational Force and Field]].

**中文:**
本子知识点将[[向心力]]的概念扩展到两个经典的现实场景，其中向心力由多个力的组合而非单一力提供。对于**倾斜轨道**，来自道路（或轨道）的法向反作用力的水平分量提供必要的向心力，使车辆能够在高速下安全转弯而无需依赖摩擦力。对于**圆锥摆**，绳子张力的水平分量提供向心力，使摆锤在水平圆内运动，同时绳子扫过一个圆锥体。理解这些系统需要将力分解为水平和竖直分量，并在二维空间中应用[[牛顿运动定律]]。这是[[向心加速度公式]]的关键应用，对于理解[[圆周轨道]]和[[引力场与重力场]]至关重要。

---

# 2. Syllabus Learning Objectives / 考纲学习目标

| CAIE 9702 | Edexcel IAL |
|-----------|-------------|
| 14.2(a): Understand the concept of centripetal force and its application to banked curves. | 5.5: Understand the concept of centripetal force and its application to banked curves. |
| 14.2(b): Solve problems involving centripetal force, including the conical pendulum. | 5.6: Solve problems involving centripetal force, including the conical pendulum. |
| 14.2(c): Derive and apply the relationship for the angle of banking. | 5.7: Derive and apply the relationship for the angle of banking. |
| 14.2(d): Understand the conditions for a vehicle to negotiate a banked curve safely. | 5.8: Understand the conditions for a vehicle to negotiate a banked curve safely. |
| | 5.9: Solve problems involving the conical pendulum, including deriving the relationship between the angle and the speed. |

**Examiner Expectations / 考官期望:**
- **English:** You must be able to draw free-body diagrams for both systems, resolve forces correctly, and derive the key equations. For banked tracks, you must understand the "design speed" concept and the role of friction (or its absence). For the conical pendulum, you must be able to relate the angle of the string to the speed and radius of the circular path.
- **中文:** 你必须能够为这两个系统绘制受力分析图，正确分解力，并推导出关键方程。对于倾斜轨道，你必须理解“设计速度”的概念以及摩擦力的作用（或缺失）。对于圆锥摆，你必须能够将绳子的角度与速度和圆周路径的半径联系起来。

---

# 3. Core Definitions / 核心定义

| Term (EN/CN) | Definition (EN) | Definition (CN) | Common Mistakes / 常见错误 |
|--------------|-----------------|-----------------|---------------------------|
| **Banked Track** / 倾斜轨道 | A curved road or track that is tilted sideways, with the outer edge higher than the inner edge, to help vehicles turn safely. | 一种侧向倾斜的弯曲道路或轨道，外缘高于内缘，以帮助车辆安全转弯。 | Confusing the angle of banking with the angle of the resultant force. |
| **Angle of Banking (θ)** / 倾斜角(θ) | The angle between the surface of the track and the horizontal. | 轨道表面与水平面之间的夹角。 | Forgetting that the normal reaction is perpendicular to the surface, not vertical. |
| **Design Speed (v₀)** / 设计速度(v₀) | The speed at which a vehicle can negotiate a banked curve without relying on friction; the centripetal force is provided entirely by the horizontal component of the normal reaction. | 车辆无需依赖摩擦力即可通过倾斜弯道的速度；向心力完全由法向反作用力的水平分量提供。 | Thinking the design speed is the maximum safe speed (it is the *ideal* speed). |
| **Conical Pendulum** / 圆锥摆 | A pendulum consisting of a bob attached to a fixed point by a string, moving in a horizontal circle such that the string sweeps out a cone. | 一种摆锤，通过绳子连接到固定点，在水平圆内运动，使得绳子扫过一个圆锥体。 | Forgetting that the vertical component of tension balances the weight, not the horizontal component. |
| **Tension (T)** / 张力(T) | The force exerted by the string on the bob, directed along the string towards the point of suspension. | 绳子对摆锤施加的力，方向沿绳子指向悬挂点。 | Resolving tension incorrectly; the horizontal component is $T \sin \theta$, not $T \cos \theta$. |

---

# 4. Key Concepts Explained / 关键概念详解

## 4.1 Banked Track (No Friction) / 倾斜轨道（无摩擦）

### Explanation / 解释
**English:** Consider a car of mass $m$ moving at speed $v$ on a banked track of radius $r$ with banking angle $\theta$. Assume no friction. The only forces acting on the car are its weight $mg$ (downwards) and the normal reaction $N$ (perpendicular to the track surface). The resultant of these two forces must provide the [[Centripetal Force]] $F_c = \frac{mv^2}{r}$ directed horizontally towards the center of the circle.

Resolving forces:
- **Vertically:** $N \cos \theta = mg$ (no vertical acceleration).
- **Horizontally:** $N \sin \theta = \frac{mv^2}{r}$ (provides centripetal force).

Dividing the horizontal equation by the vertical equation gives:
$$ \tan \theta = \frac{v^2}{rg} $$

This is the condition for the **design speed** $v_0 = \sqrt{rg \tan \theta}$. At this speed, no friction is needed.

**中文:** 考虑一辆质量为 $m$ 的汽车以速度 $v$ 在半径为 $r$、倾斜角为 $\theta$ 的倾斜轨道上行驶。假设无摩擦。作用在汽车上的力只有重力 $mg$（向下）和法向反作用力 $N$（垂直于轨道表面）。这两个力的合力必须提供水平指向圆心的[[向心力]] $F_c = \frac{mv^2}{r}$。

分解力：
- **竖直方向：** $N \cos \theta = mg$（无竖直加速度）。
- **水平方向：** $N \sin \theta = \frac{mv^2}{r}$（提供向心力）。

将水平方程除以竖直方程得到：
$$ \tan \theta = \frac{v^2}{rg} $$

这就是**设计速度** $v_0 = \sqrt{rg \tan \theta}$ 的条件。在此速度下，不需要摩擦力。

### Physical Meaning / 物理意义
**English:** The banking angle is designed for a specific speed. If a car travels at this speed, the normal reaction alone provides the exact centripetal force needed. If the car travels faster or slower, friction (if present) must act to prevent sliding up or down the track.
**中文:** 倾斜角是为特定速度设计的。如果汽车以该速度行驶，仅法向反作用力就能提供所需的精确向心力。如果汽车行驶得更快或更慢，摩擦力（如果存在）必须起作用以防止车辆向上或向下滑动。

### Common Misconceptions / 常见误区
- **English:**
  - Thinking the normal reaction is vertical. It is perpendicular to the surface.
  - Confusing the angle of banking with the angle of the resultant force.
  - Assuming the design speed is the maximum safe speed (it is the *ideal* speed).
- **中文:**
  - 认为法向反作用力是竖直的。它垂直于表面。
  - 混淆倾斜角与合力角。
  - 假设设计速度是最大安全速度（它是*理想*速度）。

### Exam Tips / 考试提示
- **English:** Always draw a clear free-body diagram. Resolve the normal reaction, not the weight. Remember that the centripetal force is horizontal, not parallel to the track.
- **中文:** 始终绘制清晰的受力分析图。分解法向反作用力，而不是重力。记住向心力是水平的，而不是平行于轨道。

> 📷 **IMAGE PROMPT — BCT-01: Banked Track Free-Body Diagram**
> A car on a banked track. Show the forces: weight (mg) vertically down, normal reaction (N) perpendicular to the track surface. Show the horizontal component of N (N sin θ) pointing towards the center of the circle, and the vertical component (N cos θ) balancing mg. Label the banking angle θ.

## 4.2 Conical Pendulum / 圆锥摆

### Explanation / 解释
**English:** Consider a bob of mass $m$ attached to a fixed point by a string of length $L$. The bob moves in a horizontal circle of radius $r$ with constant speed $v$. The string makes an angle $\theta$ with the vertical. The forces acting on the bob are its weight $mg$ (downwards) and the tension $T$ (along the string).

Resolving forces:
- **Vertically:** $T \cos \theta = mg$ (no vertical acceleration).
- **Horizontally:** $T \sin \theta = \frac{mv^2}{r}$ (provides centripetal force).

Dividing the horizontal equation by the vertical equation gives:
$$ \tan \theta = \frac{v^2}{rg} $$

Also, the radius $r = L \sin \theta$. Substituting this into the equation gives:
$$ \tan \theta = \frac{v^2}{(L \sin \theta)g} \implies v^2 = Lg \tan \theta \sin \theta $$

Alternatively, using $\omega = \frac{v}{r}$, we can derive:
$$ \cos \theta = \frac{g}{\omega^2 L} $$

**中文:** 考虑一个质量为 $m$ 的摆锤，通过长度为 $L$ 的绳子连接到固定点。摆锤以恒定速度 $v$ 在半径为 $r$ 的水平圆内运动。绳子与竖直方向成 $\theta$ 角。作用在摆锤上的力是重力 $mg$（向下）和张力 $T$（沿绳子方向）。

分解力：
- **竖直方向：** $T \cos \theta = mg$（无竖直加速度）。
- **水平方向：** $T \sin \theta = \frac{mv^2}{r}$（提供向心力）。

将水平方程除以竖直方程得到：
$$ \tan \theta = \frac{v^2}{rg} $$

另外，半径 $r = L \sin \theta$。将其代入方程得到：
$$ \tan \theta = \frac{v^2}{(L \sin \theta)g} \implies v^2 = Lg \tan \theta \sin \theta $$

或者，使用 $\omega = \frac{v}{r}$，我们可以推导出：
$$ \cos \theta = \frac{g}{\omega^2 L} $$

### Physical Meaning / 物理意义
**English:** The angle $\theta$ is determined by the speed of the bob and the length of the string. A faster speed or a shorter string results in a larger angle. The period of the conical pendulum is independent of the mass of the bob.
**中文:** 角度 $\theta$ 由摆锤的速度和绳子的长度决定。速度越快或绳子越短，角度越大。圆锥摆的周期与摆锤的质量无关。

### Common Misconceptions / 常见误区
- **English:**
  - Thinking the tension is equal to the weight. The vertical component of tension balances the weight.
  - Confusing the length of the string $L$ with the radius $r$ of the circle.
  - Forgetting that the centripetal force is horizontal.
- **中文:**
  - 认为张力等于重力。张力的竖直分量平衡重力。
  - 混淆绳子的长度 $L$ 与圆的半径 $r$。
  - 忘记向心力是水平的。

### Exam Tips / 考试提示
- **English:** Draw a clear diagram showing the string, the angle, and the radius. Resolve tension correctly. Remember that $r = L \sin \theta$.
- **中文:** 绘制清晰的图表，显示绳子、角度和半径。正确分解张力。记住 $r = L \sin \theta$。

> 📷 **IMAGE PROMPT — CP-01: Conical Pendulum Diagram**
> A conical pendulum showing a bob moving in a horizontal circle. Label the string length L, the angle θ from the vertical, the radius r of the circle, and the speed v. Show the forces: weight (mg) vertically down, tension (T) along the string. Show the horizontal component of T (T sin θ) pointing towards the center of the circle, and the vertical component (T cos θ) balancing mg.

---

# 5. Essential Equations / 核心公式

## 5.1 Banked Track (No Friction) / 倾斜轨道（无摩擦）

$$ \tan \theta = \frac{v^2}{rg} $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $\theta$ | Angle of banking | 倾斜角 | rad or ° |
| $v$ | Speed of vehicle | 车辆速度 | m s⁻¹ |
| $r$ | Radius of curvature | 曲率半径 | m |
| $g$ | Acceleration due to gravity | 重力加速度 | m s⁻² |

**Derivation / 推导:** From resolving forces: $N \cos \theta = mg$ and $N \sin \theta = \frac{mv^2}{r}$. Dividing gives $\tan \theta = \frac{v^2}{rg}$.

**Conditions / 适用条件:**
- **English:** No friction. The track is banked at angle $\theta$. The vehicle is moving at the design speed $v_0 = \sqrt{rg \tan \theta}$.
- **中文:** 无摩擦。轨道倾斜角为 $\theta$。车辆以设计速度 $v_0 = \sqrt{rg \tan \theta}$ 行驶。

**Limitations / 局限性:**
- **English:** This equation only applies when friction is negligible. In reality, friction often plays a role, especially when the vehicle's speed deviates from the design speed.
- **中文:** 该方程仅在摩擦力可忽略时适用。实际上，摩擦力通常起作用，尤其是当车辆速度偏离设计速度时。

## 5.2 Conical Pendulum / 圆锥摆

$$ \tan \theta = \frac{v^2}{rg} $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $\theta$ | Angle of string from vertical | 绳子与竖直方向的夹角 | rad or ° |
| $v$ | Speed of bob | 摆锤速度 | m s⁻¹ |
| $r$ | Radius of horizontal circle | 水平圆半径 | m |
| $g$ | Acceleration due to gravity | 重力加速度 | m s⁻² |

**Derivation / 推导:** From resolving forces: $T \cos \theta = mg$ and $T \sin \theta = \frac{mv^2}{r}$. Dividing gives $\tan \theta = \frac{v^2}{rg}$.

**Conditions / 适用条件:**
- **English:** The string is massless and inextensible. Air resistance is negligible. The bob moves in a perfect horizontal circle.
- **中文:** 绳子无质量且不可伸长。空气阻力可忽略。摆锤在完美的水平圆内运动。

**Limitations / 局限性:**
- **English:** The equation assumes a point mass bob and a perfectly rigid string. In reality, the string may have some mass and the bob may not be a point mass.
- **中文:** 该方程假设摆锤为质点，绳子完全刚性。实际上，绳子可能有质量，摆锤可能不是质点。

---

# 6. Graphs and Relationships / 图表与关系

## 6.1 Banked Track: $\tan \theta$ vs $v^2$ / 倾斜轨道：$\tan \theta$ 与 $v^2$ 的关系

### Axes / 坐标轴
- **x-axis:** $v^2$ (speed squared) / 速度平方
- **y-axis:** $\tan \theta$ (tangent of banking angle) / 倾斜角的正切值

### Shape / 形状
- **English:** A straight line passing through the origin with gradient $\frac{1}{rg}$.
- **中文:** 一条通过原点的直线，斜率为 $\frac{1}{rg}$。

### Gradient Meaning / 斜率含义
- **English:** The gradient is $\frac{1}{rg}$. For a given radius $r$, a steeper gradient means a smaller radius.
- **中文:** 斜率为 $\frac{1}{rg}$。对于给定的半径 $r$，斜率越陡意味着半径越小。

### Area Meaning / 面积含义
- **English:** Not applicable.
- **中文:** 不适用。

### Exam Interpretation / 考试解读
- **English:** You may be asked to determine the radius of the track from the gradient of a $\tan \theta$ vs $v^2$ graph.
- **中文:** 可能会要求你从 $\tan \theta$ 与 $v^2$ 关系图的斜率确定轨道的半径。

## 6.2 Conical Pendulum: $\cos \theta$ vs $\frac{1}{\omega^2}$ / 圆锥摆：$\cos \theta$ 与 $\frac{1}{\omega^2}$ 的关系

### Axes / 坐标轴
- **x-axis:** $\frac{1}{\omega^2}$ (inverse square of angular speed) / 角速度平方的倒数
- **y-axis:** $\cos \theta$ (cosine of angle) / 角度的余弦值

### Shape / 形状
- **English:** A straight line passing through the origin with gradient $\frac{g}{L}$.
- **中文:** 一条通过原点的直线，斜率为 $\frac{g}{L}$。

### Gradient Meaning / 斜率含义
- **English:** The gradient is $\frac{g}{L}$. For a given string length $L$, a steeper gradient means a shorter string.
- **中文:** 斜率为 $\frac{g}{L}$。对于给定的绳子长度 $L$，斜率越陡意味着绳子越短。

### Area Meaning / 面积含义
- **English:** Not applicable.
- **中文:** 不适用。

### Exam Interpretation / 考试解读
- **English:** You may be asked to determine the length of the string from the gradient of a $\cos \theta$ vs $\frac{1}{\omega^2}$ graph.
- **中文:** 可能会要求你从 $\cos \theta$ 与 $\frac{1}{\omega^2}$ 关系图的斜率确定绳子的长度。

---

# 7. Required Diagrams / 必备图表

## 7.1 Banked Track Free-Body Diagram / 倾斜轨道受力分析图

### Description / 描述
- **English:** A diagram showing a car on a banked track. The forces acting on the car are weight (mg) acting vertically downwards and the normal reaction (N) acting perpendicular to the track surface. The horizontal component of N (N sin θ) provides the centripetal force towards the center of the circle.
- **中文:** 显示汽车在倾斜轨道上的图表。作用在汽车上的力是竖直向下的重力 (mg) 和垂直于轨道表面的法向反作用力 (N)。N 的水平分量 (N sin θ) 提供指向圆心的向心力。

### Image Prompt / 图片生成提示
> 📷 **IMAGE PROMPT — BCT-02: Banked Track Free-Body Diagram (Detailed)**
> A detailed free-body diagram of a car on a banked track. The car is represented as a box. The track is inclined at an angle θ to the horizontal. The weight (mg) is a downward arrow from the center of the box. The normal reaction (N) is an arrow perpendicular to the track surface, pointing away from it. From the tip of N, draw a dashed line to show its horizontal component (N sin θ) pointing towards the center of the circle, and its vertical component (N cos θ) pointing upwards. Label all forces and components. The angle θ is clearly marked between the track and the horizontal.

### Labels Required / 需要标注
- **English:** Weight (mg), Normal Reaction (N), Banking Angle (θ), Horizontal Component (N sin θ), Vertical Component (N cos θ), Center of Circle.
- **中文:** 重力 (mg), 法向反作用力 (N), 倾斜角 (θ), 水平分量 (N sin θ), 竖直分量 (N cos θ), 圆心。

### Exam Importance / 考试重要性
- **English:** This diagram is essential for deriving the banking equation and understanding the forces involved. You must be able to draw and label it correctly.
- **中文:** 此图对于推导倾斜方程和理解所涉及的力至关重要。你必须能够正确绘制和标注它。

## 7.2 Conical Pendulum Diagram / 圆锥摆图

### Description / 描述
- **English:** A diagram showing a conical pendulum. The bob is moving in a horizontal circle of radius r. The string of length L makes an angle θ with the vertical. The forces acting on the bob are weight (mg) and tension (T). The horizontal component of T (T sin θ) provides the centripetal force.
- **中文:** 显示圆锥摆的图表。摆锤在半径为 r 的水平圆内运动。长度为 L 的绳子与竖直方向成 θ 角。作用在摆锤上的力是重力 (mg) 和张力 (T)。T 的水平分量 (T sin θ) 提供向心力。

### Image Prompt / 图片生成提示
> 📷 **IMAGE PROMPT — CP-02: Conical Pendulum Diagram (Detailed)**
> A detailed diagram of a conical pendulum. Show a fixed point at the top. A string of length L extends downwards at an angle θ from the vertical. At the end of the string is a bob (a small circle). The bob is moving in a horizontal circle of radius r. Draw the circular path as a dashed line. From the bob, draw two force arrows: weight (mg) vertically down, and tension (T) along the string towards the fixed point. From the tip of T, draw dashed lines to show its horizontal component (T sin θ) pointing towards the center of the circle, and its vertical component (T cos θ) pointing upwards. Label all forces, components, L, r, and θ.

### Labels Required / 需要标注
- **English:** String Length (L), Radius (r), Angle (θ), Weight (mg), Tension (T), Horizontal Component (T sin θ), Vertical Component (T cos θ), Center of Circle.
- **中文:** 绳子长度 (L), 半径 (r), 角度 (θ), 重力 (mg), 张力 (T), 水平分量 (T sin θ), 竖直分量 (T cos θ), 圆心。

### Exam Importance / 考试重要性
- **English:** This diagram is essential for deriving the conical pendulum equations. You must be able to draw and label it correctly.
- **中文:** 此图对于推导圆锥摆方程至关重要。你必须能够正确绘制和标注它。

---

# 8. Worked Examples / 典型例题

## Example 1: Banked Track Design Speed / 示例 1：倾斜轨道设计速度

### Question / 题目
**English:**
A racing track has a banked curve of radius 200 m. The track is banked at an angle of 15° to the horizontal. Calculate the design speed of the curve. Assume no friction is required. (Take $g = 9.81 \text{ m s}^{-2}$)

**中文:**
一条赛车道有一个半径为 200 m 的倾斜弯道。轨道与水平面成 15° 角倾斜。计算该弯道的设计速度。假设不需要摩擦力。（取 $g = 9.81 \text{ m s}^{-2}$）

### Solution / 解答
**English:**
1. **Identify the relevant equation:** For a banked track with no friction, $\tan \theta = \frac{v^2}{rg}$.
2. **Rearrange for $v$:** $v = \sqrt{rg \tan \theta}$.
3. **Substitute values:** $r = 200 \text{ m}$, $g = 9.81 \text{ m s}^{-2}$, $\theta = 15^\circ$.
   $$ v = \sqrt{200 \times 9.81 \times \tan 15^\circ} $$
   $$ v = \sqrt{200 \times 9.81 \times 0.2679} $$
   $$ v = \sqrt{525.6} $$
   $$ v = 22.9 \text{ m s}^{-1} $$

**中文:**
1. **确定相关方程：** 对于无摩擦的倾斜轨道，$\tan \theta = \frac{v^2}{rg}$。
2. **解出 $v$：** $v = \sqrt{rg \tan \theta}$。
3. **代入数值：** $r = 200 \text{ m}$, $g = 9.81 \text{ m s}^{-2}$, $\theta = 15^\circ$。
   $$ v = \sqrt{200 \times 9.81 \times \tan 15^\circ} $$
   $$ v = \sqrt{200 \times 9.81 \times 0.2679} $$
   $$ v = \sqrt{525.6} $$
   $$ v = 22.9 \text{ m s}^{-1} $$

### Final Answer / 最终答案
**Answer:** $22.9 \text{ m s}^{-1}$ | **答案：** $22.9 \text{ m s}^{-1}$

### Quick Tip / 提示
- **English:** Ensure your calculator is in degree mode when using angles in degrees.
- **中文:** 使用角度度数时，确保计算器处于度数模式。

## Example 2: Conical Pendulum Angle / 示例 2：圆锥摆角度

### Question / 题目
**English:**
A conical pendulum consists of a bob of mass 0.50 kg attached to a string of length 1.2 m. The bob moves in a horizontal circle with a constant speed of 3.0 m s⁻¹. Calculate the angle the string makes with the vertical. (Take $g = 9.81 \text{ m s}^{-2}$)

**中文:**
一个圆锥摆由一个质量为 0.50 kg 的摆锤和一根长度为 1.2 m 的绳子组成。摆锤以 3.0 m s⁻¹ 的恒定速度在水平圆内运动。计算绳子与竖直方向所成的角度。（取 $g = 9.81 \text{ m s}^{-2}$）

### Solution / 解答
**English:**
1. **Identify the relevant equation:** For a conical pendulum, $\tan \theta = \frac{v^2}{rg}$.
2. **Relate $r$ to $L$ and $\theta$:** $r = L \sin \theta$.
3. **Substitute $r$ into the equation:**
   $$ \tan \theta = \frac{v^2}{(L \sin \theta)g} $$
   $$ \tan \theta \sin \theta = \frac{v^2}{Lg} $$
   $$ \frac{\sin^2 \theta}{\cos \theta} = \frac{v^2}{Lg} $$
   $$ \frac{1 - \cos^2 \theta}{\cos \theta} = \frac{v^2}{Lg} $$
   This is a quadratic in $\cos \theta$. Alternatively, use the derived form $v^2 = Lg \tan \theta \sin \theta$.
4. **Solve numerically:**
   $$ \tan \theta \sin \theta = \frac{3.0^2}{1.2 \times 9.81} = \frac{9}{11.772} = 0.7645 $$
   Using trial and error or a solver:
   - Try $\theta = 40^\circ$: $\tan 40^\circ \sin 40^\circ = 0.8391 \times 0.6428 = 0.5394$ (too low)
   - Try $\theta = 50^\circ$: $\tan 50^\circ \sin 50^\circ = 1.1918 \times 0.7660 = 0.9129$ (too high)
   - Try $\theta = 45^\circ$: $\tan 45^\circ \sin 45^\circ = 1 \times 0.7071 = 0.7071$ (close)
   - Try $\theta = 47^\circ$: $\tan 47^\circ \sin 47^\circ = 1.0724 \times 0.7314 = 0.7843$ (slightly high)
   - Try $\theta = 46^\circ$: $\tan 46^\circ \sin 46^\circ = 1.0355 \times 0.7193 = 0.7448$ (slightly low)
   - Interpolating: $\theta \approx 46.5^\circ$.
   Therefore, $\theta \approx 46.5^\circ$.

**中文:**
1. **确定相关方程：** 对于圆锥摆，$\tan \theta = \frac{v^2}{rg}$。
2. **将 $r$ 与 $L$ 和 $\theta$ 关联：** $r = L \sin \theta$。
3. **将 $r$ 代入方程：**
   $$ \tan \theta = \frac{v^2}{(L \sin \theta)g} $$
   $$ \tan \theta \sin \theta = \frac{v^2}{Lg} $$
   $$ \frac{\sin^2 \theta}{\cos \theta} = \frac{v^2}{Lg} $$
   $$ \frac{1 - \cos^2 \theta}{\cos \theta} = \frac{v^2}{Lg} $$
   这是关于 $\cos \theta$ 的二次方程。或者，使用推导形式 $v^2 = Lg \tan \theta \sin \theta$。
4. **数值求解：**
   $$ \tan \theta \sin \theta = \frac{3.0^2}{1.2 \times 9.81} = \frac{9}{11.772} = 0.7645 $$
   使用试错法或求解器：
   - 尝试 $\theta = 40^\circ$: $\tan 40^\circ \sin 40^\circ = 0.8391 \times 0.6428 = 0.5394$ (太低)
   - 尝试 $\theta = 50^\circ$: $\tan 50^\circ \sin 50^\circ = 1.1918 \times 0.7660 = 0.9129$ (太高)
   - 尝试 $\theta = 45^\circ$: $\tan 45^\circ \sin 45^\circ = 1 \times 0.7071 = 0.7071$ (接近)
   - 尝试 $\theta = 47^\circ$: $\tan 47^\circ \sin 47^\circ = 1.0724 \times 0.7314 = 0.7843$ (略高)
   - 尝试 $\theta = 46^\circ$: $\tan 46^\circ \sin 46^\circ = 1.0355 \times 0.7193 = 0.7448$ (略低)
   - 插值：$\theta \approx 46.5^\circ$。
   因此，$\theta \approx 46.5^\circ$。

### Final Answer / 最终答案
**Answer:** $\theta \approx 46.5^\circ$ | **答案：** $\theta \approx 46.5^\circ$

### Quick Tip / 提示
- **English:** When solving $\tan \theta \sin \theta = \text{constant}$, you can use the identity $\tan \theta \sin \theta = \frac{\sin^2 \theta}{\cos \theta}$ and solve numerically.
- **中文:** 求解 $\tan \theta \sin \theta = \text{常数}$ 时，可以使用恒等式 $\tan \theta \sin \theta = \frac{\sin^2 \theta}{\cos \theta}$ 并进行数值求解。

---

# 9. Past Paper Question Types / 历年真题题型

| Question Type / 题型 | Frequency / 频率 | Difficulty / 难度 | Past Paper References / 真题索引 |
|----------------------|------------------|------------------|-------------------------------|
| Banked track: calculate design speed | High | Medium | 📝 *待填入* |
| Banked track: derive $\tan \theta = v^2/rg$ | Medium | Medium | 📝 *待填入* |
| Conical pendulum: calculate angle or speed | High | Medium | 📝 *待填入* |
| Conical pendulum: derive relationship | Medium | Hard | 📝 *待填入* |
| Banked track with friction | Low | Hard | 📝 *待填入* |

**Common Command Words / 常见指令词:**
- **English:** Derive, Calculate, Determine, Show that, Explain, Sketch.
- **中文:** 推导，计算，确定，证明，解释，画出草图。

---

# 10. Practical Skills Connections / 实验技能链接

**English:**
This sub-topic connects to practical skills in the following ways:
- **Measurements:** Measuring the radius of a circular path, the angle of a string, and the period of rotation.
- **Uncertainties:** Estimating uncertainties in measurements of length, angle, and time.
- **Graph Plotting:** Plotting graphs of $\tan \theta$ vs $v^2$ or $\cos \theta$ vs $1/\omega^2$ to determine unknown quantities like radius or string length.
- **Experimental Design:** Designing an experiment to verify the relationship for a conical pendulum, including controlling variables like string length and speed.

**中文:**
本子知识点通过以下方式与实验技能联系：
- **测量：** 测量圆周路径的半径、绳子的角度和旋转周期。
- **不确定度：** 估计长度、角度和时间测量的不确定度。
- **图表绘制：** 绘制 $\tan \theta$ 与 $v^2$ 或 $\cos \theta$ 与 $1/\omega^2$ 的关系图，以确定半径或绳子长度等未知量。
- **实验设计：** 设计实验以验证圆锥摆的关系，包括控制绳子长度和速度等变量。

---

# 11. Concept Map / 概念图谱

```mermaid
graph TD
    %% Core Concepts
    A[Banked Tracks & Conical Pendulum] --> B[Banked Track]
    A --> C[Conical Pendulum]
    
    %% Banked Track Details
    B --> D[Forces: Weight & Normal Reaction]
    B --> E[Key Equation: tan θ = v²/rg]
    B --> F[Design Speed: v₀ = √(rg tan θ)]
    B --> G[Role of Friction]
    
    %% Conical Pendulum Details
    C --> H[Forces: Weight & Tension]
    C --> I[Key Equation: tan θ = v²/rg]
    C --> J[Radius: r = L sin θ]
    C --> K[Alternative: cos θ = g/(ω²L)]
    
    %% Connections to Prerequisites
    D --> L[[Newton's Laws of Motion]]
    H --> L
    E --> M[[Centripetal Acceleration Formula]]
    I --> M
    E --> N[[Angular Measures]]
    I --> N
    
    %% Connections to Related Topics
    F --> O[[Circular Orbits]]
    G --> P[[Gravitational Force and Field]]
    
    %% Styling
    classDef core fill:#f9f,stroke:#333,stroke-width:2px;
    class A core;
```

---

# 12. Quick Revision Sheet / 速查表

| Category / 类别 | Key Points / 要点 |
|----------------|------------------|
| Definition / 定义 | **Banked Track:** A curved track tilted sideways to help vehicles turn. **Conical Pendulum:** A pendulum moving in a horizontal circle. |
| Key Formula / 核心公式 | **Both:** $\tan \theta = \frac{v^2}{rg}$ <br> **Banked Track:** $v_0 = \sqrt{rg \tan \theta}$ <br> **Conical Pendulum:** $r = L \sin \theta$, $\cos \theta = \frac{g}{\omega^2 L}$ |
| Key Graph / 核心图表 | **Banked Track:** $\tan \theta$ vs $v^2$ (straight line through origin, gradient $1/rg$) <br> **Conical Pendulum:** $\cos \theta$ vs $1/\omega^2$ (straight line through origin, gradient $g/L$) |
| Exam Tip / 考试提示 | **Always draw a free-body diagram.** Resolve the normal reaction (banked track) or tension (conical pendulum) correctly. Remember the centripetal force is horizontal. For banked tracks, the design speed is the *ideal* speed, not the maximum. |