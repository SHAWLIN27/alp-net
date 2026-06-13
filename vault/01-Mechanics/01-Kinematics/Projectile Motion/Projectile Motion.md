# 1. Overview / 概述

**English:**
Projectile motion is the study of objects moving under the influence of gravity after being launched with an initial velocity. This topic is a cornerstone of classical mechanics, bridging [[Scalars and Vectors]] with [[Equations of Motion (SUVAT)]]. In projectile motion, we treat the horizontal and vertical components of motion independently: the horizontal component has constant velocity (ignoring air resistance), while the vertical component experiences constant acceleration due to gravity ($g \approx 9.81 \, \text{m s}^{-2}$ downward). This independence principle allows us to predict the trajectory, time of flight, range, and maximum height of any projectile.

In real-world applications, projectile motion is essential for understanding sports (e.g., basketball shots, golf drives), ballistics (e.g., artillery fire, missile guidance), and engineering (e.g., water fountains, fireworks design). In both Cambridge 9702 and Edexcel IAL examinations, projectile motion is a high-frequency topic, typically appearing in multiple-choice questions, structured calculations, and practical design tasks. Mastery of this topic requires strong vector resolution skills, confident use of SUVAT equations, and the ability to interpret [[Projectile Motion Graphs]].

**中文：**
抛体运动是研究物体在初始速度发射后，在重力作用下运动的学科。该主题是经典力学的基石，连接了[[标量与矢量]]和[[运动方程（SUVAT）]]。在抛体运动中，我们将运动的水平分量和垂直分量独立处理：水平分量具有恒定速度（忽略空气阻力），而垂直分量则经历由于重力引起的恒定加速度（$g \approx 9.81 \, \text{m s}^{-2}$ 向下）。这一独立性原理使我们能够预测任何抛体的轨迹、飞行时间、射程和最大高度。

在实际应用中，抛体运动对于理解体育（如篮球投篮、高尔夫击球）、弹道学（如火炮射击、导弹制导）和工程（如喷泉设计、烟花设计）至关重要。在剑桥 9702 和爱德思 IAL 考试中，抛体运动是一个高频主题，通常出现在选择题、结构化计算题和实验设计题中。掌握该主题需要扎实的矢量分解技能、自信地使用 SUVAT 方程，以及解释[[抛体运动图表]]的能力。

---

# 2. Syllabus Learning Objectives / 考纲学习目标

| CAIE 9702 | Edexcel IAL |
|-----------|-------------|
| 3.1(l) Recognise that the horizontal and vertical components of motion of a projectile are independent. | 1.13 Understand that the horizontal and vertical components of projectile motion are independent. |
| 3.1(m) Describe and explain the motion of a projectile, including the independence of horizontal and vertical components. | 1.14 Use the equations of motion for constant acceleration to solve problems involving projectiles. |
| 3.1(n) Solve problems using the equations of motion for constant acceleration, including projectile motion. | 1.15 Derive and use the equations for the time of flight, range, and maximum height of a projectile launched horizontally or at an angle. |
| (Implicit) Derive and use equations for time of flight, range, and maximum height. | 1.16 Analyse projectile motion using vector diagrams and graphical methods. |

**Examiner Expectations / 考官期望:**

**English:**
- Candidates must be able to resolve initial velocity into horizontal ($u_x = u \cos \theta$) and vertical ($u_y = u \sin \theta$) components.
- Candidates must apply SUVAT equations separately to horizontal (constant velocity) and vertical (constant acceleration) motion.
- Candidates must recognise that time of flight is determined solely by vertical motion, while range depends on both components.
- Candidates should be able to sketch and interpret [[Projectile Motion Graphs]] (e.g., displacement-time, velocity-time, trajectory).
- For Edexcel, candidates may be asked to derive equations for range and maximum height from first principles.
- For CAIE, practical contexts (e.g., measuring range using a projectile launcher) are common in Paper 5.

**中文：**
- 考生必须能够将初始速度分解为水平分量（$u_x = u \cos \theta$）和垂直分量（$u_y = u \sin \theta$）。
- 考生必须分别对水平运动（匀速）和垂直运动（匀加速）应用 SUVAT 方程。
- 考生必须认识到飞行时间仅由垂直运动决定，而射程取决于两个分量。
- 考生应能够绘制和解释[[抛体运动图表]]（例如位移-时间图、速度-时间图、轨迹图）。
- 对于爱德思，考生可能需要从基本原理推导射程和最大高度的方程。
- 对于剑桥，实验背景（例如使用抛体发射器测量射程）在试卷 5 中很常见。

> 📋 **CIE Only:** CAIE Paper 5 may require candidates to design an experiment to investigate the relationship between launch angle and range, including error analysis and graph plotting.
>
> 📋 **Edexcel Only:** Edexcel Unit 1 may include questions requiring derivation of $R = \frac{u^2 \sin 2\theta}{g}$ and $H = \frac{u^2 \sin^2 \theta}{2g}$.

---

# 3. Core Definitions / 核心定义

| Term (EN/CN) | Definition (EN) | Definition (CN) | Common Mistakes / 常见错误 |
|--------------|-----------------|-----------------|---------------------------|
| **Projectile** / 抛体 | An object moving under the influence of gravity only, after being given an initial velocity. Air resistance is assumed negligible. | 仅受重力影响的物体，在获得初始速度后运动。假设空气阻力可忽略。 | Confusing projectile with free fall; a projectile has both horizontal and vertical motion. |
| **Trajectory** / 轨迹 | The curved path followed by a projectile. | 抛体所遵循的弯曲路径。 | Thinking the trajectory is always a parabola (true only with constant $g$ and no air resistance). |
| **Time of Flight ($T$)** / 飞行时间 | The total time a projectile remains in the air from launch to landing. | 抛体从发射到着陆在空中停留的总时间。 | Using horizontal motion to find $T$; $T$ is determined by vertical motion only. |
| **Range ($R$)** / 射程 | The horizontal distance travelled by a projectile from launch to landing. | 抛体从发射到着陆所经过的水平距离。 | Forgetting that range depends on $\sin 2\theta$, not $\sin \theta$ or $\cos \theta$ alone. |
| **Maximum Height ($H$)** / 最大高度 | The greatest vertical displacement reached by a projectile above its launch point. | 抛体在其发射点上方达到的最大垂直位移。 | Using $v=0$ at the top but forgetting that horizontal velocity is still non-zero. |
| **Angle of Projection ($\theta$)** / 投射角 | The angle between the initial velocity vector and the horizontal. | 初始速度矢量与水平方向之间的夹角。 | Measuring from the vertical instead of the horizontal. |
| **Horizontal Component ($u_x$)** / 水平分量 | The component of initial velocity in the horizontal direction: $u_x = u \cos \theta$. | 初始速度在水平方向上的分量：$u_x = u \cos \theta$。 | Using $\sin$ instead of $\cos$ for horizontal component. |
| **Vertical Component ($u_y$)** / 垂直分量 | The component of initial velocity in the vertical direction: $u_y = u \sin \theta$. | 初始速度在垂直方向上的分量：$u_y = u \sin \theta$。 | Using $\cos$ instead of $\sin$ for vertical component. |

---

# 4. Key Concepts Explained / 关键概念详解

## 4.1 Independence of Horizontal and Vertical Motion / 水平与垂直运动的独立性

### Explanation / 解释
**English:**
The most fundamental concept in projectile motion is that the horizontal and vertical components of motion are completely independent. This means that the horizontal motion does not affect the vertical motion, and vice versa. The horizontal component has zero acceleration (assuming no air resistance), so horizontal velocity remains constant. The vertical component has constant acceleration $g = 9.81 \, \text{m s}^{-2}$ downward, following the [[Equations of Motion (SUVAT)]] exactly as in free fall. This independence allows us to solve projectile problems by treating the two components separately and then combining results using the common time variable $t$.

**中文：**
抛体运动中最基本的概念是水平运动和垂直运动分量完全独立。这意味着水平运动不影响垂直运动，反之亦然。水平分量的加速度为零（假设无空气阻力），因此水平速度保持恒定。垂直分量具有向下的恒定加速度 $g = 9.81 \, \text{m s}^{-2}$，完全遵循[[运动方程（SUVAT）]]，如同自由落体。这种独立性使我们能够通过分别处理两个分量，然后使用共同的时间变量 $t$ 组合结果来解决抛体问题。

### Physical Meaning / 物理意义
**English:**
Imagine throwing a ball horizontally off a cliff. The ball's horizontal speed remains constant (ignoring air resistance), while it accelerates downward due to gravity. If you drop another ball from the same height at the same instant, both balls hit the ground at the same time, even though one has horizontal motion. This demonstrates that vertical motion is unaffected by horizontal motion.

**中文：**
想象一下从悬崖上水平抛出一个球。球的水平速度保持不变（忽略空气阻力），而它由于重力向下加速。如果你在同一时刻从同一高度放下另一个球，两个球会同时落地，即使其中一个有水平运动。这表明垂直运动不受水平运动影响。

### Common Misconceptions / 常见误区
- **Misconception:** The projectile's speed is constant throughout its flight.
  **Correction:** Only the horizontal component of velocity is constant; the vertical component changes, so the resultant speed changes.
- **Misconception:** At the highest point, the projectile has zero velocity.
  **Correction:** At the highest point, vertical velocity is zero, but horizontal velocity is still $u \cos \theta$.
- **Misconception:** A projectile launched at a larger angle always has a longer range.
  **Correction:** Range is maximum at $\theta = 45^\circ$; angles complementary (e.g., $30^\circ$ and $60^\circ$) give the same range.

### Exam Tips / 考试提示
**English:**
- Always resolve the initial velocity into components first.
- Write separate SUVAT lists for horizontal and vertical motion.
- Remember that time $t$ is the same for both components.
- For CAIE, be prepared to sketch and interpret [[Projectile Motion Graphs]].
- For Edexcel, derivation of range and maximum height equations is frequently tested.

**中文：**
- 始终先将初始速度分解为分量。
- 为水平和垂直运动分别列出 SUVAT 列表。
- 记住时间 $t$ 对两个分量是相同的。
- 对于剑桥，准备好绘制和解释[[抛体运动图表]]。
- 对于爱德思，射程和最大高度方程的推导经常被测试。

> 📷 **IMAGE PROMPT — PM-01: Independence of Motion Demonstration**
>
> A split-screen diagram showing two balls released from the same height: one dropped vertically (free fall) and one launched horizontally. Both balls are at the same vertical position at each time interval, showing they hit the ground simultaneously. Labels: "Ball A (dropped)", "Ball B (projected horizontally)", "Same vertical displacement at time t". Clean white background, educational style, with dashed horizontal lines showing equal time intervals.

---

## 4.2 Resolving Initial Velocity / 初始速度的分解

### Explanation / 解释
**English:**
For a projectile launched with initial speed $u$ at an angle $\theta$ above the horizontal, the initial velocity vector must be resolved into horizontal and vertical components using trigonometry:
- Horizontal component: $u_x = u \cos \theta$
- Vertical component: $u_y = u \sin \theta$

This resolution is essential because the two components obey different laws of motion. The horizontal component remains constant throughout the flight (no horizontal force), while the vertical component changes due to gravity. This concept directly builds on [[Scalars and Vectors]].

**中文：**
对于以初始速度 $u$ 和与水平方向夹角 $\theta$ 发射的抛体，必须使用三角函数将初始速度矢量分解为水平和垂直分量：
- 水平分量：$u_x = u \cos \theta$
- 垂直分量：$u_y = u \sin \theta$

这种分解至关重要，因为两个分量遵循不同的运动定律。水平分量在整个飞行过程中保持不变（无水平力），而垂直分量由于重力而变化。这个概念直接建立在[[标量与矢量]]的基础上。

### Physical Meaning / 物理意义
**English:**
If you throw a ball at a shallow angle (small $\theta$), most of the initial speed goes into horizontal motion, giving a long range but low height. If you throw at a steep angle (large $\theta$), most of the speed goes into vertical motion, giving high height but short range. The angle $\theta = 45^\circ$ gives the best balance for maximum range.

**中文：**
如果你以较小的角度（小 $\theta$）投掷球，大部分初始速度用于水平运动，从而获得较长的射程但较低的高度。如果你以较大的角度（大 $\theta$）投掷，大部分速度用于垂直运动，从而获得较高的高度但较短的射程。角度 $\theta = 45^\circ$ 为最大射程提供了最佳平衡。

### Common Misconceptions / 常见误区
- **Misconception:** $u_x = u \sin \theta$ and $u_y = u \cos \theta$.
  **Correction:** $u_x = u \cos \theta$ (adjacent/hypotenuse) and $u_y = u \sin \theta$ (opposite/hypotenuse).
- **Misconception:** The angle $\theta$ is measured from the vertical.
  **Correction:** $\theta$ is always measured from the horizontal.

### Exam Tips / 考试提示
**English:**
- Draw a clear vector diagram showing $u$, $u_x$, $u_y$, and $\theta$.
- Check your calculator is in degree mode.
- For horizontal launch ($\theta = 0^\circ$), $u_x = u$ and $u_y = 0$.
- For vertical launch ($\theta = 90^\circ$), $u_x = 0$ and $u_y = u$ (this is just free fall).

**中文：**
- 绘制清晰的矢量图，显示 $u$、$u_x$、$u_y$ 和 $\theta$。
- 检查计算器处于角度模式。
- 对于水平发射（$\theta = 0^\circ$），$u_x = u$ 且 $u_y = 0$。
- 对于垂直发射（$\theta = 90^\circ$），$u_x = 0$ 且 $u_y = u$（这只是自由落体）。

---

## 4.3 Time of Flight / 飞行时间

### Explanation / 解释
**English:**
The time of flight $T$ is the total time the projectile spends in the air. It is determined entirely by the vertical motion. For a projectile launched from ground level and landing at the same height, the vertical displacement $s_y = 0$. Using the SUVAT equation $s = ut + \frac{1}{2}at^2$ for vertical motion:
$$0 = u_y T - \frac{1}{2}g T^2$$
Solving for $T$ (excluding $T=0$):
$$T = \frac{2u_y}{g} = \frac{2u \sin \theta}{g}$$

For a projectile launched from height $h$ above landing point, the equation becomes $s_y = -h$ (taking upward as positive), and the quadratic must be solved.

**中文：**
飞行时间 $T$ 是抛体在空中停留的总时间。它完全由垂直运动决定。对于从地面发射并在同一高度着陆的抛体，垂直位移 $s_y = 0$。使用垂直运动的 SUVAT 方程 $s = ut + \frac{1}{2}at^2$：
$$0 = u_y T - \frac{1}{2}g T^2$$
求解 $T$（排除 $T=0$）：
$$T = \frac{2u_y}{g} = \frac{2u \sin \theta}{g}$$

对于从高于着陆点 $h$ 处发射的抛体，方程变为 $s_y = -h$（取向上为正），必须求解二次方程。

### Physical Meaning / 物理意义
**English:**
Time of flight depends only on the vertical component of initial velocity and gravity. A projectile launched straight up ($\theta = 90^\circ$) has the longest time of flight for a given speed. A projectile launched horizontally ($\theta = 0^\circ$) has a time of flight determined only by the launch height (like free fall).

**中文：**
飞行时间仅取决于初始速度的垂直分量和重力。对于给定的速度，垂直向上发射（$\theta = 90^\circ$）的抛体具有最长的飞行时间。水平发射（$\theta = 0^\circ$）的抛体的飞行时间仅由发射高度决定（如同自由落体）。

### Common Misconceptions / 常见误区
- **Misconception:** Time of flight depends on horizontal velocity.
  **Correction:** Time of flight is determined solely by vertical motion.
- **Misconception:** For a projectile launched from height, $T = \sqrt{2h/g}$ always.
  **Correction:** That formula applies only for horizontal launch ($u_y = 0$). For angled launches, the quadratic must be solved.

### Exam Tips / 考试提示
**English:**
- For symmetrical flight (launch and landing at same height), use $T = 2u \sin \theta / g$.
- For asymmetrical flight (different launch and landing heights), set up the SUVAT equation and solve the quadratic.
- Remember that time $t$ is the same for both horizontal and vertical calculations.

**中文：**
- 对于对称飞行（发射和着陆在同一高度），使用 $T = 2u \sin \theta / g$。
- 对于非对称飞行（不同的发射和着陆高度），建立 SUVAT 方程并求解二次方程。
- 记住时间 $t$ 对于水平和垂直计算是相同的。

---

## 4.4 Range / 射程

### Explanation / 解释
**English:**
The range $R$ is the horizontal distance travelled by the projectile. Since horizontal velocity is constant ($u_x = u \cos \theta$), the range is simply:
$$R = u_x \times T = (u \cos \theta) \times \frac{2u \sin \theta}{g} = \frac{2u^2 \sin \theta \cos \theta}{g}$$
Using the trigonometric identity $\sin 2\theta = 2 \sin \theta \cos \theta$:
$$R = \frac{u^2 \sin 2\theta}{g}$$

This equation shows that the range depends on the square of the initial speed and the sine of twice the launch angle. The maximum range occurs when $\sin 2\theta = 1$, i.e., $2\theta = 90^\circ$, so $\theta = 45^\circ$.

**中文：**
射程 $R$ 是抛体经过的水平距离。由于水平速度恒定（$u_x = u \cos \theta$），射程简单地为：
$$R = u_x \times T = (u \cos \theta) \times \frac{2u \sin \theta}{g} = \frac{2u^2 \sin \theta \cos \theta}{g}$$
使用三角恒等式 $\sin 2\theta = 2 \sin \theta \cos \theta$：
$$R = \frac{u^2 \sin 2\theta}{g}$$

该方程表明射程取决于初始速度的平方和两倍发射角的正弦。最大射程出现在 $\sin 2\theta = 1$ 时，即 $2\theta = 90^\circ$，所以 $\theta = 45^\circ$。

### Physical Meaning / 物理意义
**English:**
For a given initial speed, the range is maximum at $45^\circ$. Complementary angles (e.g., $30^\circ$ and $60^\circ$) give the same range because $\sin 60^\circ = \sin 120^\circ$. This is why in sports like shot put or javelin, athletes launch at angles close to $45^\circ$ to maximise distance.

**中文：**
对于给定的初始速度，射程在 $45^\circ$ 时最大。互补角（例如 $30^\circ$ 和 $60^\circ$）给出相同的射程，因为 $\sin 60^\circ = \sin 120^\circ$。这就是为什么在铅球或标枪等运动中，运动员以接近 $45^\circ$ 的角度发射以最大化距离。

### Common Misconceptions / 常见误区
- **Misconception:** Range increases continuously with angle.
  **Correction:** Range increases up to $45^\circ$, then decreases.
- **Misconception:** Range is proportional to $u$, not $u^2$.
  **Correction:** $R \propto u^2$, so doubling speed quadruples range.
- **Misconception:** The range equation applies to all projectile problems.
  **Correction:** It applies only when launch and landing are at the same height.

### Exam Tips / 考试提示
**English:**
- For Edexcel, be prepared to derive $R = u^2 \sin 2\theta / g$ from first principles.
- For CAIE, you may be given the equation and asked to use it.
- Remember that the range equation assumes no air resistance and same launch/landing height.
- For projectiles landing at a different height, use $R = u_x \times T$ where $T$ is found from vertical motion.

**中文：**
- 对于爱德思，准备好从基本原理推导 $R = u^2 \sin 2\theta / g$。
- 对于剑桥，可能会给出方程并要求使用它。
- 记住射程方程假设无空气阻力和相同的发射/着陆高度。
- 对于在不同高度着陆的抛体，使用 $R = u_x \times T$，其中 $T$ 从垂直运动求得。

---

## 4.5 Maximum Height / 最大高度

### Explanation / 解释
**English:**
The maximum height $H$ is the highest vertical displacement reached by the projectile. At the highest point, the vertical velocity becomes zero ($v_y = 0$). Using the SUVAT equation $v^2 = u^2 + 2as$ for vertical motion:
$$0 = u_y^2 - 2gH$$
Solving for $H$:
$$H = \frac{u_y^2}{2g} = \frac{u^2 \sin^2 \theta}{2g}$$

The time to reach maximum height is half the total time of flight (for symmetrical flight):
$$t_{\text{peak}} = \frac{u_y}{g} = \frac{u \sin \theta}{g}$$

**中文：**
最大高度 $H$ 是抛体达到的最高垂直位移。在最高点，垂直速度变为零（$v_y = 0$）。使用垂直运动的 SUVAT 方程 $v^2 = u^2 + 2as$：
$$0 = u_y^2 - 2gH$$
求解 $H$：
$$H = \frac{u_y^2}{2g} = \frac{u^2 \sin^2 \theta}{2g}$$

达到最大高度的时间是总飞行时间的一半（对于对称飞行）：
$$t_{\text{peak}} = \frac{u_y}{g} = \frac{u \sin \theta}{g}$$

### Physical Meaning / 物理意义
**English:**
Maximum height depends only on the vertical component of initial velocity. A projectile launched at $90^\circ$ (straight up) reaches the greatest height for a given speed. The height is proportional to $u^2$, so doubling the speed quadruples the maximum height.

**中文：**
最大高度仅取决于初始速度的垂直分量。以 $90^\circ$（垂直向上）发射的抛体对于给定的速度达到最大高度。高度与 $u^2$ 成正比，因此速度加倍会使最大高度变为四倍。

### Common Misconceptions / 常见误区
- **Misconception:** At maximum height, the projectile's speed is zero.
  **Correction:** Only vertical velocity is zero; horizontal velocity is still $u \cos \theta$.
- **Misconception:** Maximum height is $u^2/2g$ for all angles.
  **Correction:** It is $u^2 \sin^2 \theta / 2g$, which depends on angle.

### Exam Tips / 考试提示
**English:**
- Use $v_y = 0$ at the highest point as a key condition.
- For symmetrical flight, the time to reach maximum height is $T/2$.
- For asymmetrical flight, the maximum height still occurs when $v_y = 0$, but the time to reach it is not half the total time.

**中文：**
- 使用最高点 $v_y = 0$ 作为关键条件。
- 对于对称飞行，达到最大高度的时间是 $T/2$。
- 对于非对称飞行，最大高度仍然出现在 $v_y = 0$ 时，但达到它的时间不是总时间的一半。

---

## 4.6 Trajectory Equation / 轨迹方程

### Explanation / 解释
**English:**
The trajectory equation describes the path of the projectile, relating horizontal displacement $x$ to vertical displacement $y$. From horizontal motion: $x = u_x t = (u \cos \theta) t$, so $t = \frac{x}{u \cos \theta}$. From vertical motion: $y = u_y t - \frac{1}{2} g t^2 = (u \sin \theta) t - \frac{1}{2} g t^2$. Substituting $t$:
$$y = (u \sin \theta) \left(\frac{x}{u \cos \theta}\right) - \frac{1}{2} g \left(\frac{x}{u \cos \theta}\right)^2$$
$$y = x \tan \theta - \frac{g x^2}{2u^2 \cos^2 \theta}$$

This is a quadratic equation in $x$, confirming that the trajectory is a parabola (assuming constant $g$ and no air resistance).

**中文：**
轨迹方程描述了抛体的路径，将水平位移 $x$ 与垂直位移 $y$ 联系起来。从水平运动：$x = u_x t = (u \cos \theta) t$，所以 $t = \frac{x}{u \cos \theta}$。从垂直运动：$y = u_y t - \frac{1}{2} g t^2 = (u \sin \theta) t - \frac{1}{2} g t^2$。代入 $t$：
$$y = (u \sin \theta) \left(\frac{x}{u \cos \theta}\right) - \frac{1}{2} g \left(\frac{x}{u \cos \theta}\right)^2$$
$$y = x \tan \theta - \frac{g x^2}{2u^2 \cos^2 \theta}$$

这是关于 $x$ 的二次方程，确认了轨迹是抛物线（假设恒定 $g$ 且无空气阻力）。

### Physical Meaning / 物理意义
**English:**
The trajectory equation allows us to find the height $y$ at any horizontal distance $x$, or to find the horizontal distance at which the projectile reaches a certain height. This is useful for determining whether a projectile will clear an obstacle or hit a target at a specific location.

**中文：**
轨迹方程使我们能够找到在任何水平距离 $x$ 处的高度 $y$，或者找到抛体达到特定高度时的水平距离。这对于确定抛体是否能越过障碍物或击中特定位置的目标非常有用。

### Common Misconceptions / 常见误区
- **Misconception:** The trajectory is always a parabola.
  **Correction:** It is a parabola only under constant gravity and negligible air resistance.
- **Misconception:** The trajectory equation can be used without considering the launch angle.
  **Correction:** The equation explicitly contains $\theta$ and $u$.

### Exam Tips / 考试提示
**English:**
- The trajectory equation is not always given in exams; you may need to derive it.
- Use it to find the height at a given horizontal distance.
- For CAIE, you may be asked to sketch the trajectory and label key points.

**中文：**
- 轨迹方程并不总是在考试中给出；你可能需要推导它。
- 使用它来找到给定水平距离处的高度。
- 对于剑桥，可能会要求你绘制轨迹并标注关键点。

---

# 5. Essential Equations / 核心公式

## 5.1 Horizontal Component of Velocity / 水平速度分量

**Equation / 公式:**
$$v_x = u_x = u \cos \theta$$

**Variables / 变量:**
| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $v_x$ | Horizontal velocity at any time | 任意时刻的水平速度 | m s$^{-1}$ |
| $u_x$ | Initial horizontal velocity | 初始水平速度 | m s$^{-1}$ |
| $u$ | Initial speed | 初始速率 | m s$^{-1}$ |
| $\theta$ | Angle of projection above horizontal | 水平方向上的投射角 | degrees or rad |

**Derivation / 推导:**
**English:** From vector resolution: $u_x = u \cos \theta$. Since no horizontal force acts, horizontal acceleration is zero, so $v_x = u_x$ throughout the flight.
**中文：** 从矢量分解：$u_x = u \cos \theta$。由于没有水平力作用，水平加速度为零，因此在整个飞行过程中 $v_x = u_x$。

**Conditions / 适用条件:**
**English:** Assumes no air resistance and no horizontal forces.
**中文：** 假设无空气阻力且无水平力。

**Limitations / 局限性:**
**English:** Does not apply if air resistance is significant or if there is a horizontal force (e.g., wind).
**中文：** 如果空气阻力显著或存在水平力（例如风），则不适用。

**Rearrangements / 变形:**
**English:** $u = \frac{u_x}{\cos \theta}$, $\cos \theta = \frac{u_x}{u}$
**中文：** $u = \frac{u_x}{\cos \theta}$, $\cos \theta = \frac{u_x}{u}$

---

## 5.2 Vertical Component of Velocity / 垂直速度分量

**Equation / 公式:**
$$v_y = u_y - gt = u \sin \theta - gt$$

**Variables / 变量:**
| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $v_y$ | Vertical velocity at time $t$ | 时刻 $t$ 的垂直速度 | m s$^{-1}$ |
| $u_y$ | Initial vertical velocity ($u \sin \theta$) | 初始垂直速度 ($u \sin \theta$) | m s$^{-1}$ |
| $g$ | Acceleration due to gravity (9.81 m s$^{-2}$) | 重力加速度 (9.81 m s$^{-2}$) | m s$^{-2}$ |
| $t$ | Time elapsed | 经过的时间 | s |

**Derivation / 推导:**
**English:** From SUVAT equation $v = u + at$, with $a = -g$ (taking upward as positive).
**中文：** 从 SUVAT 方程 $v = u + at$，其中 $a = -g$（取向上为正）。

**Conditions / 适用条件:**
**English:** Constant gravitational acceleration, no air resistance.
**中文：** 恒定重力加速度，无空气阻力。

**Limitations / 局限性:**
**English:** $g$ varies with altitude and location; air resistance changes the velocity profile.
**中文：** $g$ 随海拔和位置变化；空气阻力改变速度分布。

**Rearrangements / 变形:**
**English:** $t = \frac{u_y - v_y}{g}$, $u_y = v_y + gt$
**中文：** $t = \frac{u_y - v_y}{g}$, $u_y = v_y + gt$

---

## 5.3 Vertical Displacement / 垂直位移

**Equation / 公式:**
$$s_y = u_y t - \frac{1}{2} g t^2 = (u \sin \theta) t - \frac{1}{2} g t^2$$

**Variables / 变量:**
| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $s_y$ | Vertical displacement at time $t$ | 时刻 $t$ 的垂直位移 | m |
| $u_y$ | Initial vertical velocity | 初始垂直速度 | m s$^{-1}$ |
| $g$ | Acceleration due to gravity | 重力加速度 | m s$^{-2}$ |
| $t$ | Time elapsed | 经过的时间 | s |

**Derivation / 推导:**
**English:** From SUVAT equation $s = ut + \frac{1}{2}at^2$, with $a = -g$.
**中文：** 从 SUVAT 方程 $s = ut + \frac{1}{2}at^2$，其中 $a = -g$。

**Conditions / 适用条件:**
**English:** Constant $g$, no air resistance, upward direction taken as positive.
**中文：** 恒定 $g$，无空气阻力，取向上为正方向。

**Limitations / 局限性:**
**English:** Does not account for air resistance or varying $g$.
**中文：** 不考虑空气阻力或变化的 $g$。

**Rearrangements / 变形:**
**English:** $t = \frac{u_y \pm \sqrt{u_y^2 - 2g s_y}}{g}$ (solving quadratic)
**中文：** $t = \frac{u_y \pm \sqrt{u_y^2 - 2g s_y}}{g}$（求解二次方程）

---

## 5.4 Time of Flight (Symmetrical) / 飞行时间（对称）

**Equation / 公式:**
$$T = \frac{2u \sin \theta}{g}$$

**Variables / 变量:**
| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $T$ | Total time of flight | 总飞行时间 | s |
| $u$ | Initial speed | 初始速率 | m s$^{-1}$ |
| $\theta$ | Angle of projection | 投射角 | degrees or rad |
| $g$ | Acceleration due to gravity | 重力加速度 | m s$^{-2}$ |

**Derivation / 推导:**
**English:** Set $s_y = 0$ in $s_y = u_y t - \frac{1}{2} g t^2$: $0 = (u \sin \theta) T - \frac{1}{2} g T^2$. Factor $T$: $T(u \sin \theta - \frac{1}{2} g T) = 0$. Non-zero solution: $T = \frac{2u \sin \theta}{g}$.
**中文：** 在 $s_y = u_y t - \frac{1}{2} g t^2$ 中设 $s_y = 0$：$0 = (u \sin \theta) T - \frac{1}{2} g T^2$。提取 $T$：$T(u \sin \theta - \frac{1}{2} g T) = 0$。非零解：$T = \frac{2u \sin \theta}{g}$。

**Conditions / 适用条件:**
**English:** Launch and landing at the same vertical height. No air resistance.
**中文：** 发射和着陆在同一垂直高度。无空气阻力。

**Limitations / 局限性:**
**English:** Does not apply if launch and landing heights differ, or if air resistance is significant.
**中文：** 如果发射和着陆高度不同，或空气阻力显著，则不适用。

**Rearrangements / 变形:**
**English:** $u = \frac{gT}{2 \sin \theta}$, $\sin \theta = \frac{gT}{2u}$
**中文：** $u = \frac{gT}{2 \sin \theta}$, $\sin \theta = \frac{gT}{2u}$

---

## 5.5 Range (Symmetrical) / 射程（对称）

**Equation / 公式:**
$$R = \frac{u^2 \sin 2\theta}{g}$$

**Variables / 变量:**
| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $R$ | Horizontal range | 水平射程 | m |
| $u$ | Initial speed | 初始速率 | m s$^{-1}$ |
| $\theta$ | Angle of projection | 投射角 | degrees or rad |
| $g$ | Acceleration due to gravity | 重力加速度 | m s$^{-2}$ |

**Derivation / 推导:**
**English:** $R = u_x \times T = (u \cos \theta) \times \frac{2u \sin \theta}{g} = \frac{2u^2 \sin \theta \cos \theta}{g} = \frac{u^2 \sin 2\theta}{g}$ (using $\sin 2\theta = 2 \sin \theta \cos \theta$).
**中文：** $R = u_x \times T = (u \cos \theta) \times \frac{2u \sin \theta}{g} = \frac{2u^2 \sin \theta \cos \theta}{g} = \frac{u^2 \sin 2\theta}{g}$（使用 $\sin 2\theta = 2 \sin \theta \cos \theta$）。

**Conditions / 适用条件:**
**English:** Launch and landing at the same vertical height. No air resistance.
**中文：** 发射和着陆在同一垂直高度。无空气阻力。

**Limitations / 局限性:**
**English:** Does not apply if launch and landing heights differ, or if air resistance is significant.
**中文：** 如果发射和着陆高度不同，或空气阻力显著，则不适用。

**Rearrangements / 变形:**
**English:** $u = \sqrt{\frac{Rg}{\sin 2\theta}}$, $\theta = \frac{1}{2} \sin^{-1}\left(\frac{Rg}{u^2}\right)$
**中文：** $u = \sqrt{\frac{Rg}{\sin 2\theta}}$, $\theta = \frac{1}{2} \sin^{-1}\left(\frac{Rg}{u^2}\right)$

---

## 5.6 Maximum Height / 最大高度

**Equation / 公式:**
$$H = \frac{u^2 \sin^2 \theta}{2g}$$

**Variables / 变量:**
| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $H$ | Maximum height above launch point | 发射点以上的最大高度 | m |
| $u$ | Initial speed | 初始速率 | m s$^{-1}$ |
| $\theta$ | Angle of projection | 投射角 | degrees or rad |
| $g$ | Acceleration due to gravity | 重力加速度 | m s$^{-2}$ |

**Derivation / 推导:**
**English:** At maximum height, $v_y = 0$. Using $v_y^2 = u_y^2 - 2g s_y$: $0 = (u \sin \theta)^2 - 2gH$. Solving: $H = \frac{u^2 \sin^2 \theta}{2g}$.
**中文：** 在最大高度处，$v_y = 0$。使用 $v_y^2 = u_y^2 - 2g s_y$：$0 = (u \sin \theta)^2 - 2gH$。求解：$H = \frac{u^2 \sin^2 \theta}{2g}$。

**Conditions / 适用条件:**
**English:** Constant $g$, no air resistance. Height measured from launch point.
**中文：** 恒定 $g$，无空气阻力。高度从发射点测量。

**Limitations / 局限性:**
**English:** Does not account for air resistance or varying $g$.
**中文：** 不考虑空气阻力或变化的 $g$。

**Rearrangements / 变形:**
**English:** $u = \sqrt{\frac{2gH}{\sin^2 \theta}}$, $\sin \theta = \sqrt{\frac{2gH}{u^2}}$
**中文：** $u = \sqrt{\frac{2gH}{\sin^2 \theta}}$, $\sin \theta = \sqrt{\frac{2gH}{u^2}}$

---

## 5.7 Trajectory Equation / 轨迹方程

**Equation / 公式:**
$$y = x \tan \theta - \frac{g x^2}{2u^2 \cos^2 \theta}$$

**Variables / 变量:**
| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $y$ | Vertical displacement at horizontal distance $x$ | 水平距离 $x$ 处的垂直位移 | m |
| $x$ | Horizontal displacement | 水平位移 | m |
| $u$ | Initial speed | 初始速率 | m s$^{-1}$ |
| $\theta$ | Angle of projection | 投射角 | degrees or rad |
| $g$ | Acceleration due to gravity | 重力加速度 | m s$^{-2}$ |

**Derivation / 推导:**
**English:** From $x = (u \cos \theta) t$, $t = \frac{x}{u \cos \theta}$. Substitute into $y = (u \sin \theta) t - \frac{1}{2} g t^2$: $y = (u \sin \theta) \frac{x}{u \cos \theta} - \frac{1}{2} g \frac{x^2}{u^2 \cos^2 \theta} = x \tan \theta - \frac{g x^2}{2u^2 \cos^2 \theta}$.
**中文：** 从 $x = (u \cos \theta) t$，$t = \frac{x}{u \cos \theta}$。代入 $y = (u \sin \theta) t - \frac{1}{2} g t^2$：$y = (u \sin \theta) \frac{x}{u \cos \theta} - \frac{1}{2} g \frac{x^2}{u^2 \cos^2 \theta} = x \tan \theta - \frac{g x^2}{2u^2 \cos^2 \theta}$。

**Conditions / 适用条件:**
**English:** Constant $g$, no air resistance. Origin at launch point.
**中文：** 恒定 $g$，无空气阻力。原点在发射点。

**Limitations / 局限性:**
**English:** Does not account for air resistance or varying $g$.
**中文：** 不考虑空气阻力或变化的 $g$。

**Rearrangements / 变形:**
**English:** Can be rearranged to solve for $x$ given $y$, but typically results in a quadratic.
**中文：** 可以重新排列以在给定 $y$ 时求解 $x$，但通常得到二次方程。

---

# 6. Graphs and Relationships / 图表与关系

## 6.1 Horizontal Displacement vs Time / 水平位移-时间图

### Axes / 坐标轴
**English:** x-axis: Time ($t$), y-axis: Horizontal displacement ($x$)
**中文：** x 轴：时间 ($t$)，y 轴：水平位移 ($x$)

### Shape / 形状
**English:** A straight line through the origin with positive slope.
**中文：** 一条通过原点的直线，斜率为正。

### Gradient Meaning / 斜率含义
**English:** The gradient equals the horizontal velocity $v_x = u \cos \theta$, which is constant.
**中文：** 斜率等于水平速度 $v_x = u \cos \theta$，是常数。

### Area Meaning / 面积含义
**English:** Not physically meaningful in this context.
**中文：** 在此上下文中没有物理意义。

### Exam Interpretation / 考试解读
**English:** A steeper line indicates a larger horizontal velocity. The graph confirms that horizontal motion has constant velocity.
**中文：** 更陡的线表示更大的水平速度。该图确认水平运动具有恒定速度。

### Common Questions / 常见问题
**English:** "Calculate the horizontal velocity from the gradient of the graph." "Explain why the graph is a straight line."
**中文：** "从图的斜率计算水平速度。" "解释为什么该图是一条直线。"

---

## 6.2 Vertical Displacement vs Time / 垂直位移-时间图

### Axes / 坐标轴
**English:** x-axis: Time ($t$), y-axis: Vertical displacement ($y$)
**中文：** x 轴：时间 ($t$)，y 轴：垂直位移 ($y$)

### Shape / 形状
**English:** A parabola opening downward (for symmetrical flight). It starts at $y=0$, rises to a maximum at $t = T/2$, then returns to $y=0$ at $t = T$.
**中文：** 一条开口向下的抛物线（对于对称飞行）。从 $y=0$ 开始，在 $t = T/2$ 时上升到最大值，然后在 $t = T$ 时回到 $y=0$。

### Gradient Meaning / 斜率含义
**English:** The gradient at any point equals the vertical velocity $v_y$ at that time. The gradient is positive initially, zero at the peak, and negative on the descent.
**中文：** 任意点的斜率等于该时刻的垂直速度 $v_y$。初始斜率为正，在峰值处为零，在下降过程中为负。

### Area Meaning / 面积含义
**English:** Not directly meaningful; the area under a $v_y$-$t$ graph gives vertical displacement.
**中文：** 没有直接意义；$v_y$-$t$ 图下的面积给出垂直位移。

### Exam Interpretation / 考试解读
**English:** The symmetry of the parabola confirms that time up equals time down. The maximum point gives the maximum height and the time to reach it.
**中文：** 抛物线的对称性确认上升时间等于下降时间。最大值点给出最大高度和达到它的时间。

### Common Questions / 常见问题
**English:** "Determine the maximum height from the graph." "Find the time of flight." "Explain the shape of the graph."
**中文：** "从图中确定最大高度。" "找出飞行时间。" "解释图的形状。"

---

## 6.3 Vertical Velocity vs Time / 垂直速度-时间图

### Axes / 坐标轴
**English:** x-axis: Time ($t$), y-axis: Vertical velocity ($v_y$)
**中文：** x 轴：时间 ($t$)，y 轴：垂直速度 ($v_y$)

### Shape / 形状
**English:** A straight line with negative slope. It starts at $v_y = u \sin \theta$, crosses zero at $t = T/2$, and reaches $v_y = -u \sin \theta$ at $t = T$.
**中文：** 一条斜率为负的直线。从 $v_y = u \sin \theta$ 开始，在 $t = T/2$ 时穿过零，在 $t = T$ 时达到 $v_y = -u \sin \theta$。

### Gradient Meaning / 斜率含义
**English:** The gradient equals the acceleration due to gravity, $-g = -9.81 \, \text{m s}^{-2}$.
**中文：** 斜率等于重力加速度，$-g = -9.81 \, \text{m s}^{-2}$。

### Area Meaning / 面积含义
**English:** The area under the graph (between the line and the time axis) gives the vertical displacement. The area above the axis (positive) equals the area below (negative) for symmetrical flight, giving net zero displacement.
**中文：** 图下的面积（线和时间轴之间）给出垂直位移。对于对称飞行，轴上方的面积（正）等于轴下方的面积（负），净位移为零。

### Exam Interpretation / 考试解读
**English:** The constant gradient confirms constant acceleration. The zero crossing gives the time to reach maximum height. The area under the graph can be used to find displacement.
**中文：** 恒定斜率确认恒定加速度。零交叉点给出达到最大高度的时间。图下的面积可用于求位移。

### Common Questions / 常见问题
**English:** "Determine the acceleration due to gravity from the gradient." "Calculate the maximum height using the area under the graph." "Find the time to reach maximum height."
**中文：** "从斜率确定重力加速度。" "使用图下的面积计算最大高度。" "找出达到最大高度的时间。"

---

## 6.4 Horizontal Velocity vs Time / 水平速度-时间图

### Axes / 坐标轴
**English:** x-axis: Time ($t$), y-axis: Horizontal velocity ($v_x$)
**中文：** x 轴：时间 ($t$)，y 轴：水平速度 ($v_x$)

### Shape / 形状
**English:** A horizontal straight line at $v_x = u \cos \theta$.
**中文：** 一条在 $v_x = u \cos \theta$ 处的水平直线。

### Gradient Meaning / 斜率含义
**English:** The gradient is zero, confirming zero horizontal acceleration.
**中文：** 斜率为零，确认水平加速度为零。

### Area Meaning / 面积含义
**English:** The area under the graph gives the horizontal displacement (range).
**中文：** 图下的面积给出水平位移（射程）。

### Exam Interpretation / 考试解读
**English:** The constant velocity confirms no horizontal forces. The area under the graph equals $R = v_x \times T$.
**中文：** 恒定速度确认无水平力。图下的面积等于 $R = v_x \times T$。

### Common Questions / 常见问题
**English:** "Calculate the range from the graph." "Explain why the graph is a horizontal line."
**中文：** "从图中计算射程。" "解释为什么该图是一条水平线。"

---

## 6.5 Trajectory (y vs x) / 轨迹图（y 对 x）

### Axes / 坐标轴
**English:** x-axis: Horizontal displacement ($x$), y-axis: Vertical displacement ($y$)
**中文：** x 轴：水平位移 ($x$)，y 轴：垂直位移 ($y$)

### Shape / 形状
**English:** A parabola opening downward. Starts at $(0,0)$, rises to maximum height at $x = R/2$, and returns to $y=0$ at $x = R$.
**中文：** 一条开口向下的抛物线。从 $(0,0)$ 开始，在 $x = R/2$ 处上升到最大高度，在 $x = R$ 处回到 $y=0$。

### Gradient Meaning / 斜率含义
**English:** The gradient at any point equals $\frac{dy}{dx} = \tan \theta - \frac{gx}{u^2 \cos^2 \theta}$, which is the slope of the trajectory. It is positive initially, zero at the peak, and negative on the descent.
**中文：** 任意点的梯度等于 $\frac{dy}{dx} = \tan \theta - \frac{gx}{u^2 \cos^2 \theta}$，即轨迹的斜率。初始为正，在峰值处为零，在下降过程中为负。

### Area Meaning / 面积含义
**English:** Not applicable; this is a path graph, not a time-dependent graph.
**中文：** 不适用；这是一个路径图，不是时间相关图。

### Exam Interpretation / 考试解读
**English:** The graph shows the actual path of the projectile. The maximum point gives the maximum height and the horizontal distance to it. The x-intercept gives the range.
**中文：** 该图显示了抛体的实际路径。最大值点给出最大高度和到达它的水平距离。x 轴截距给出射程。

### Common Questions / 常见问题
**English:** "Determine the range and maximum height from the graph." "Sketch the trajectory for a different launch angle." "Explain the effect of increasing initial speed on the trajectory."
**中文：** "从图中确定射程和最大高度。" "为不同的发射角绘制轨迹。" "解释增加初始速度对轨迹的影响。"

---

# 7. Required Diagrams / 必备图表

## 7.1 Vector Resolution Diagram / 矢量分解图

### Description / 描述
**English:** A diagram showing the initial velocity vector $u$ at an angle $\theta$ above the horizontal, resolved into horizontal component $u_x = u \cos \theta$ and vertical component $u_y = u \sin \theta$. The diagram should include a right-angled triangle to illustrate the trigonometric relationships.

**中文：** 一个显示初始速度矢量 $u$ 与水平方向成 $\theta$ 角的图，分解为水平分量 $u_x = u \cos \theta$ 和垂直分量 $u_y = u \sin \theta$。该图应包括一个直角三角形以说明三角关系。

### Image Prompt / 图片生成提示
> 📷 **IMAGE PROMPT — PM-02: Vector Resolution for Projectile Motion**
>
> A clean educational diagram showing a vector $u$ (thick arrow) at angle $\theta$ above the horizontal. A dashed horizontal line and a dashed vertical line form a right triangle. The horizontal component is labeled "$u_x = u \cos \theta$" with a horizontal arrow. The vertical component is labeled "$u_y = u \sin \theta$" with a vertical arrow. The angle $\theta$ is marked between $u$ and the horizontal. Use a white background, blue arrows for vectors, black text. Style: textbook-quality, 2D, flat design.

### Labels Required / 需要标注
- $u$ (initial velocity / 初始速度)
- $u_x = u \cos \theta$ (horizontal component / 水平分量)
- $u_y = u \sin \theta$ (vertical component / 垂直分量)
- $\theta$ (angle of projection / 投射角)
- Horizontal reference line / 水平参考线

### Exam Importance / 考试重要性
**English:** This diagram is essential for understanding how to resolve the initial velocity into components, which is the first step in solving any projectile motion problem. Examiners expect candidates to be able to draw and label this diagram.

**中文：** 该图对于理解如何将初始速度分解为分量至关重要，这是解决任何抛体运动问题的第一步。考官期望考生能够绘制并标注此图。

---

## 7.2 Projectile Trajectory with Key Points / 带关键点的抛体轨迹

### Description / 描述
**English:** A parabolic trajectory showing the projectile's path from launch to landing. Key points should be labeled: launch point, highest point (maximum height $H$), and landing point. The range $R$ should be indicated as the horizontal distance between launch and landing. Velocity vectors should be shown at several points along the trajectory to illustrate how the direction and magnitude of velocity change.

**中文：** 一条抛物线轨迹，显示抛体从发射到着陆的路径。应标注关键点：发射点、最高点（最大高度 $H$）和着陆点。射程 $R$ 应表示为发射和着陆之间的水平距离。应在轨迹上的几个点显示速度矢量，以说明速度方向和大小如何变化。

### Image Prompt / 图片生成提示
> 📷 **IMAGE PROMPT — PM-03: Projectile Trajectory with Velocity Vectors**
>
> A parabolic curve on a grid background, starting from the left (launch point) and ending on the right (landing point) at the same height. Label the launch point "Launch", the highest point "Maximum Height ($H$)", and the landing point "Landing". Draw a horizontal double-headed arrow labeled "Range ($R$)" between launch and landing. At three points (launch, peak, and a point on descent), draw velocity vectors as arrows: at launch, the arrow is at angle $\theta$; at peak, the arrow is horizontal; on descent, the arrow points downward at an angle. Use different colors for horizontal and vertical components. Style: educational, clean, 2D, white background.

### Labels Required / 需要标注
- Launch point / 发射点
- Maximum height ($H$) / 最大高度 ($H$)
- Landing point / 着陆点
- Range ($R$) / 射程 ($R$)
- Velocity vectors at multiple points / 多个点的速度矢量
- Horizontal and vertical components / 水平和垂直分量

### Exam Importance / 考试重要性
**English:** This diagram is frequently used in exam questions to test understanding of the trajectory, the independence of components, and how velocity changes throughout the flight. Candidates should be able to sketch this diagram and explain the velocity at different points.

**中文：** 该图在考试题中经常用于测试对轨迹、分量独立性以及速度在整个飞行过程中如何变化的理解。考生应能够绘制此图并解释不同点的速度。

---

## 7.3 Effect of Launch Angle on Range / 发射角对射程的影响

### Description / 描述
**English:** A diagram showing multiple trajectories for the same initial speed but different launch angles (e.g., $30^\circ$, $45^\circ$, $60^\circ$). The trajectories should be plotted on the same axes to show that $45^\circ$ gives the maximum range, and that complementary angles ($30^\circ$ and $60^\circ$) give the same range.

**中文：** 一个显示相同初始速度但不同发射角（例如 $30^\circ$、$45^\circ$、$60^\circ$）的多条轨迹图。这些轨迹应绘制在同一坐标轴上，以显示 $45^\circ$ 给出最大射程，并且互补角（$30^\circ$ 和 $60^\circ$）给出相同的射程。

### Image Prompt / 图片生成提示
> 📷 **IMAGE PROMPT — PM-04: Effect of Launch Angle on Projectile Range**
>
> Three parabolic trajectories on the same set of axes, all starting from the same launch point at the origin. Trajectory 1: angle $30^\circ$, medium height, medium range. Trajectory 2: angle $45^\circ$, medium-high height, longest range. Trajectory 3: angle $60^\circ$, high height, medium range (same as $30^\circ$). Use different colors for each trajectory (e.g., blue for $30^\circ$, red for $45^\circ$, green for $60^\circ$). Label each trajectory with its angle. Draw a horizontal line at the landing height. Style: educational, clear, 2D, white background, with grid lines.

### Labels Required / 需要标注
- $\theta = 30^\circ$ trajectory / $\theta = 30^\circ$ 轨迹
- $\theta = 45^\circ$ trajectory / $\theta = 45^\circ$ 轨迹
- $\theta = 60^\circ$ trajectory / $\theta = 60^\circ$ 轨迹
- Maximum range at $45^\circ$ / $45^\circ$ 时的最大射程
- Same range for $30^\circ$ and $60^\circ$ / $30^\circ$ 和 $60^\circ$ 的相同射程

### Exam Importance / 考试重要性
**English:** This diagram illustrates the key relationship between launch angle and range. It is commonly used in multiple-choice questions and in explanations. Candidates should understand why $45^\circ$ gives maximum range and why complementary angles give the same range.

**中文：** 该图说明了发射角和射程之间的关键关系。它常用于选择题和解释题中。考生应理解为什么 $45^\circ$ 给出最大射程，以及为什么互补角给出相同的射程。

---

# 8. Worked Examples / 典型例题

## Example 1: Horizontal Projectile from a Cliff / 从悬崖水平抛出的抛体

### Question / 题目
**English:**
A ball is thrown horizontally with a speed of $15 \, \text{m s}^{-1}$ from the top of a cliff that is $45 \, \text{m}$ high. Calculate:
(a) The time taken for the ball to reach the ground.
(b) The horizontal distance from the base of the cliff where the ball lands.
(c) The velocity (magnitude and direction) of the ball just before it hits the ground.

Take $g = 9.81 \, \text{m s}^{-2}$ and ignore air resistance.

**中文：**
一个球以 $15 \, \text{m s}^{-1}$ 的速度从 $45 \, \text{m}$ 高的悬崖顶水平抛出。计算：
(a) 球到达地面所需的时间。
(b) 球着陆点距离悬崖底部的水平距离。
(c) 球即将撞击地面时的速度（大小和方向）。

取 $g = 9.81 \, \text{m s}^{-2}$，忽略空气阻力。

### Image Prompt / 图片提示
> 📷 **IMAGE PROMPT — PM-05: Horizontal Projectile from Cliff**
>
> A diagram showing a cliff of height 45 m on the left. A ball is shown at the top of the cliff with a horizontal arrow labeled "$u = 15 \, \text{m/s}$". A parabolic trajectory shows the ball's path to the ground. The horizontal distance from the cliff base to the landing point is labeled "$R$". The height of the cliff is labeled "$45 \, \text{m}$". A velocity vector at the landing point shows the final velocity with components $v_x$ and $v_y$. Style: educational, 2D, clean, white background.

### Solution / 解答

**Step 1: Identify known quantities / 步骤 1：确定已知量**

**English:**
- Initial horizontal velocity: $u_x = 15 \, \text{m s}^{-1}$
- Initial vertical velocity: $u_y = 0 \, \text{m s}^{-1}$ (thrown horizontally)
- Vertical displacement: $s_y = -45 \, \text{m}$ (downward, so negative if upward is positive)
- Acceleration: $a_y = -g = -9.81 \, \text{m s}^{-2}$
- Horizontal acceleration: $a_x = 0 \, \text{m s}^{-2}$

**中文：**
- 初始水平速度：$u_x = 15 \, \text{m s}^{-1}$
- 初始垂直速度：$u_y = 0 \, \text{m s}^{-1}$（水平抛出）
- 垂直位移：$s_y = -45 \, \text{m}$（向下，所以如果向上为正则为负）
- 加速度：$a_y = -g = -9.81 \, \text{m s}^{-2}$
- 水平加速度：$a_x = 0 \, \text{m s}^{-2}$

**Step 2: Solve for time of flight (part a) / 步骤 2：求解飞行时间（a 部分）**

**English:**
Use the vertical SUVAT equation: $s_y = u_y t + \frac{1}{2} a_y t^2$

$$-45 = 0 \times t + \frac{1}{2} (-9.81) t^2$$
$$-45 = -4.905 t^2$$
$$t^2 = \frac{45}{4.905} = 9.174$$
$$t = \sqrt{9.174} = 3.03 \, \text{s}$$

**中文：**
使用垂直 SUVAT 方程：$s_y = u_y t + \frac{1}{2} a_y t^2$

$$-45 = 0 \times t + \frac{1}{2} (-9.81) t^2$$
$$-45 = -4.905 t^2$$
$$t^2 = \frac{45}{4.905} = 9.174$$
$$t = \sqrt{9.174} = 3.03 \, \text{s}$$

**Step 3: Solve for horizontal range (part b) / 步骤 3：求解水平射程（b 部分）**

**English:**
Use horizontal motion: $R = u_x \times t$ (since $a_x = 0$)

$$R = 15 \times 3.03 = 45.5 \, \text{m}$$

**中文：**
使用水平运动：$R = u_x \times t$（因为 $a_x = 0$）

$$R = 15 \times 3.03 = 45.5 \, \text{m}$$

**Step 4: Solve for final velocity (part c) / 步骤 4：求解最终速度（c 部分）**

**English:**
Horizontal component remains constant: $v_x = u_x = 15 \, \text{m s}^{-1}$

Vertical component just before impact: $v_y = u_y + a_y t = 0 + (-9.81)(3.03) = -29.7 \, \text{m s}^{-1}$

Magnitude of velocity: $v = \sqrt{v_x^2 + v_y^2} = \sqrt{15^2 + (-29.7)^2} = \sqrt{225 + 882.1} = \sqrt{1107.1} = 33.3 \, \text{m s}^{-1}$

Direction (angle below horizontal): $\phi = \tan^{-1}\left(\frac{|v_y|}{v_x}\right) = \tan^{-1}\left(\frac{29.7}{15}\right) = \tan^{-1}(1.98) = 63.2^\circ$ below the horizontal.

**中文：**
水平分量保持不变：$v_x = u_x = 15 \, \text{m s}^{-1}$

撞击前的垂直分量：$v_y = u_y + a_y t = 0 + (-9.81)(3.03) = -29.7 \, \text{m s}^{-1}$

速度大小：$v = \sqrt{v_x^2 + v_y^2} = \sqrt{15^2 + (-29.7)^2} = \sqrt{225 + 882.1} = \sqrt{1107.1} = 33.3 \, \text{m s}^{-1}$

方向（水平向下角度）：$\phi = \tan^{-1}\left(\frac{|v_y|}{v_x}\right) = \tan^{-1}\left(\frac{29.7}{15}\right) = \tan^{-1}(1.98) = 63.2^\circ$ 低于水平方向。

### Final Answer / 最终答案
**Answer:**
(a) $t = 3.03 \, \text{s}$
(b) $R = 45.5 \, \text{m}$
(c) $v = 33.3 \, \text{m s}^{-1}$ at $63.2^\circ$ below the horizontal

**答案：**
(a) $t = 3.03 \, \text{s}$
(b) $R = 45.5 \, \text{m}$
(c) $v = 33.3 \, \text{m s}^{-1}$，方向为水平向下 $63.2^\circ$

### Examiner Notes / 考官点评
**English:**
- Common mistake: Using $s_y = 45 \, \text{m}$ instead of $-45 \, \text{m}$ (sign convention).
- Common mistake: Forgetting that $u_y = 0$ for horizontal launch.
- Common mistake: Using $v = u + at$ for horizontal motion (horizontal acceleration is zero).
- Marks are typically awarded for: correct sign convention, correct SUVAT selection, correct substitution, and final answer with units.

**中文：**
- 常见错误：使用 $s_y = 45 \, \text{m}$ 而不是 $-45 \, \text{m}$（符号约定）。
- 常见错误：忘记水平发射时 $u_y = 0$。
- 常见错误：对水平运动使用 $v = u + at$（水平加速度为零）。
- 分数通常授予：正确的符号约定、正确的 SUVAT 选择、正确的代入以及带单位的最终答案。

### Alternative Method / 替代方法
**English:**
For part (a), the time can also be found using $s = \frac{1}{2}gt^2$ directly (since $u_y = 0$): $t = \sqrt{\frac{2h}{g}} = \sqrt{\frac{2 \times 45}{9.81}} = 3.03 \, \text{s}$.

**中文：**
对于 (a) 部分，也可以直接使用 $s = \frac{1}{2}gt^2$ 求时间（因为 $u_y = 0$）：$t = \sqrt{\frac{2h}{g}} = \sqrt{\frac{2 \times 45}{9.81}} = 3.03 \, \text{s}$。

---

## Example 2: Angled Projectile (Symmetrical) / 有角度抛体（对称）

### Question / 题目
**English:**
A projectile is launched from ground level with an initial speed of $20 \, \text{m s}^{-1}$ at an angle of $35^\circ$ above the horizontal. Calculate:
(a) The time of flight.
(b) The maximum height reached.
(c) The horizontal range.
(d) The velocity (magnitude and direction) at $t = 1.5 \, \text{s}$.

Take $g = 9.81 \, \text{m s}^{-2}$ and ignore air resistance.

**中文：**
一个抛体从地面以 $20 \, \text{m s}^{-1}$ 的初始速度和 $35^\circ$ 的仰角发射。计算：
(a) 飞行时间。
(b) 达到的最大高度。
(c) 水平射程。
(d) 在 $t = 1.5 \, \text{s}$ 时的速度（大小和方向）。

取 $g = 9.81 \, \text{m s}^{-2}$，忽略空气阻力。

### Solution / 解答

**Step 1: Resolve initial velocity / 步骤 1：分解初始速度**

**English:**
$$u_x = u \cos \theta = 20 \cos 35^\circ = 20 \times 0.8192 = 16.38 \, \text{m s}^{-1}$$
$$u_y = u \sin \theta = 20 \sin 35^\circ = 20 \times 0.5736 = 11.47 \, \text{m s}^{-1}$$

**中文：**
$$u_x = u \cos \theta = 20 \cos 35^\circ = 20 \times 0.8192 = 16.38 \, \text{m s}^{-1}$$
$$u_y = u \sin \theta = 20 \sin 35^\circ = 20 \times 0.5736 = 11.47 \, \text{m s}^{-1}$$

**Step 2: Time of flight (part a) / 步骤 2：飞行时间（a 部分）**

**English:**
Using $T = \frac{2u_y}{g}$ (symmetrical flight, launch and landing at same height):

$$T = \frac{2 \times 11.47}{9.81} = \frac{22.94}{9.81} = 2.34 \, \text{s}$$

**中文：**
使用 $T = \frac{2u_y}{g}$（对称飞行，发射和着陆在同一高度）：

$$T = \frac{2 \times 11.47}{9.81} = \frac{22.94}{9.81} = 2.34 \, \text{s}$$

**Step 3: Maximum height (part b) / 步骤 3：最大高度（b 部分）**

**English:**
Using $H = \frac{u_y^2}{2g}$:

$$H = \frac{(11.47)^2}{2 \times 9.81} = \frac{131.6}{19.62} = 6.71 \, \text{m}$$

**中文：**
使用 $H = \frac{u_y^2}{2g}$：

$$H = \frac{(11.47)^2}{2 \times 9.81} = \frac{131.6}{19.62} = 6.71 \, \text{m}$$

**Step 4: Horizontal range (part c) / 步骤 4：水平射程（c 部分）**

**English:**
Using $R = u_x \times T$ or $R = \frac{u^2 \sin 2\theta}{g}$:

Method 1: $R = u_x \times T = 16.38 \times 2.34 = 38.3 \, \text{m}$

Method 2: $R = \frac{u^2 \sin 2\theta}{g} = \frac{20^2 \sin 70^\circ}{9.81} = \frac{400 \times 0.9397}{9.81} = \frac{375.9}{9.81} = 38.3 \, \text{m}$

**中文：**
使用 $R = u_x \times T$ 或 $R = \frac{u^2 \sin 2\theta}{g}$：

方法 1：$R = u_x \times T = 16.38 \times 2.34 = 38.3 \, \text{m}$

方法 2：$R = \frac{u^2 \sin 2\theta}{g} = \frac{20^2 \sin 70^\circ}{9.81} = \frac{400 \times 0.9397}{9.81} = \frac{375.9}{9.81} = 38.3 \, \text{m}$

**Step 5: Velocity at $t = 1.5 \, \text{s}$ (part d) / 步骤 5：$t = 1.5 \, \text{s}$ 时的速度（d 部分）**

**English:**
Horizontal component: $v_x = u_x = 16.38 \, \text{m s}^{-1}$ (constant)

Vertical component: $v_y = u_y - gt = 11.47 - (9.81 \times 1.5) = 11.47 - 14.72 = -3.25 \, \text{m s}^{-1}$

Magnitude: $v = \sqrt{v_x^2 + v_y^2} = \sqrt{16.38^2 + (-3.25)^2} = \sqrt{268.3 + 10.56} = \sqrt{278.9} = 16.7 \, \text{m s}^{-1}$

Direction: $\phi = \tan^{-1}\left(\frac{|v_y|}{v_x}\right) = \tan^{-1}\left(\frac{3.25}{16.38}\right) = \tan^{-1}(0.1984) = 11.2^\circ$ below the horizontal.

**中文：**
水平分量：$v_x = u_x = 16.38 \, \text{m s}^{-1}$（恒定）

垂直分量：$v_y = u_y - gt = 11.47 - (9.81 \times 1.5) = 11.47 - 14.72 = -3.25 \, \text{m s}^{-1}$

大小：$v = \sqrt{v_x^2 + v_y^2} = \sqrt{16.38^2 + (-3.25)^2} = \sqrt{268.3 + 10.56} = \sqrt{278.9} = 16.7 \, \text{m s}^{-1}$

方向：$\phi = \tan^{-1}\left(\frac{|v_y|}{v_x}\right) = \tan^{-1}\left(\frac{3.25}{16.38}\right) = \tan^{-1}(0.1984) = 11.2^\circ$ 低于水平方向。

### Final Answer / 最终答案
**Answer:**
(a) $T = 2.34 \, \text{s}$
(b) $H = 6.71 \, \text{m}$
(c) $R = 38.3 \, \text{m}$
(d) $v = 16.7 \, \text{m s}^{-1}$ at $11.2^\circ$ below the horizontal

**答案：**
(a) $T = 2.34 \, \text{s}$
(b) $H = 6.71 \, \text{m}$
(c) $R = 38.3 \, \text{m}$
(d) $v = 16.7 \, \text{m s}^{-1}$，方向为水平向下 $11.2^\circ$

### Examiner Notes / 考官点评
**English:**
- Common mistake: Using $u$ instead of $u_y$ in $T = 2u/g$.
- Common mistake: Forgetting to use $\sin 2\theta$ in the range equation.
- Common mistake: Not checking whether the projectile is ascending or descending at the given time.
- For part (d), the negative $v_y$ indicates the projectile is on its way down.
- Marks are typically awarded for: correct resolution, correct equation selection, correct substitution, and final answer with units and direction.

**中文：**
- 常见错误：在 $T = 2u/g$ 中使用 $u$ 而不是 $u_y$。
- 常见错误：忘记在射程方程中使用 $\sin 2\theta$。
- 常见错误：未检查抛体在给定时间是上升还是下降。
- 对于 (d) 部分，负的 $v_y$ 表示抛体正在下降。
- 分数通常授予：正确的分解、正确的方程选择、正确的代入以及带单位和方向的最终答案。

### Alternative Method / 替代方法
**English:**
For part (d), the time $t = 1.5 \, \text{s}$ is less than $T/2 = 1.17 \, \text{s}$? Actually $1.5 > 1.17$, so the projectile is on its way down. The time after the peak is $t - T/2 = 1.5 - 1.17 = 0.33 \, \text{s}$. The vertical velocity on descent is $v_y = -g \times 0.33 = -3.24 \, \text{m s}^{-1}$, confirming our result.

**中文：**
对于 (d) 部分，时间 $t = 1.5 \, \text{s}$ 小于 $T/2 = 1.17 \, \text{s}$？实际上 $1.5 > 1.17$，所以抛体正在下降。峰值后的时间为 $t - T/2 = 1.5 - 1.17 = 0.33 \, \text{s}$。下降时的垂直速度为 $v_y = -g \times 0.33 = -3.24 \, \text{m s}^{-1}$，确认了我们的结果。

---

# 9. Past Paper Question Types / 历年真题题型

| Question Type / 题型 | Frequency / 频率 | Difficulty / 难度 | Past Paper References / 真题索引 |
|----------------------|------------------|------------------|-------------------------------|
| Calculation of time of flight, range, or maximum height / 计算飞行时间、射程或最大高度 | High | Medium | 📝 *待填入* |
| Explanation of independence of horizontal and vertical motion / 解释水平与垂直运动的独立性 | Medium | Low | 📝 *待填入* |
| Graph analysis (displacement-time, velocity-time, trajectory) / 图表分析（位移-时间、速度-时间、轨迹） | Medium | Medium | 📝 *待填入* |
| Derivation of range or maximum height equations / 推导射程或最大高度方程 | Low (CAIE) / Medium (Edexcel) | High | 📝 *待填入* |
| Practical design (e.g., measuring range vs angle) / 实验设计（例如测量射程与角度的关系） | Low (CAIE Paper 5) | High | 📝 *待填入* |
| Multi-stage problems (e.g., projectile then collision) / 多阶段问题（例如抛体后碰撞） | Low | High | 📝 *待填入* |
| Vector resolution and component analysis / 矢量分解与分量分析 | High | Low | 📝 *待填入* |

> 📝 **题库整理中 / Question Bank Under Construction:** 具体试卷编号（如 9702/23/M/J/24 Q3）将在后续整理真题后填入上表。

**Common Command Words / 常见指令词:**

| Command Word (EN) | Command Word (CN) | What to Do / 做什么 |
|-------------------|-------------------|---------------------|
| State | 陈述 | Give a brief answer without explanation. |
| Define | 定义 | Give the precise meaning of a term. |
| Explain | 解释 | Give reasons or causes for a phenomenon. |
| Describe | 描述 | Give a detailed account of a process or observation. |
| Calculate | 计算 | Use mathematical methods to find a numerical answer. |
| Determine | 确定 | Find a value using given data or a graph. |
| Suggest | 建议 | Propose a possible explanation or method. |
| Derive | 推导 | Obtain an equation from fundamental principles. |
| Sketch | 绘制 | Draw a graph or diagram showing key features. |
| Show that | 证明 | Demonstrate that a given result is correct. |

---

# 10. Practical Skills Connections / 实验技能链接

**English:**
Projectile motion provides excellent opportunities for practical work in both CAIE and Edexcel specifications.

**CAIE Paper 3 (AS) / Paper 5 (A2):**
- **Paper 3 (AS):** Candidates may be asked to investigate the relationship between the range of a projectile and the launch angle using a projectile launcher or a ramp. Measurements include: launch angle (using a protractor), range (using a measuring tape), and time of flight (using a stopwatch or light gate). Uncertainties in angle measurement ($\pm 0.5^\circ$) and range measurement ($\pm 1 \, \text{mm}$) should be considered.
- **Paper 5 (A2):** Candidates may be required to design an experiment to determine the initial speed of a projectile or to verify the relationship $R \propto u^2$. This involves: selecting appropriate equipment (e.g., projectile launcher, light gates, meter ruler), controlling variables (e.g., launch angle, air resistance), and analysing data using graphs (e.g., plotting $R$ against $u^2$ to obtain a straight line through the origin).

**Edexcel Unit 3 (AS) / Unit 6 (A2):**
- **Unit 3 (AS):** Practical investigations may involve measuring the range of a projectile launched at different angles. Candidates should be able to: set up equipment safely, take repeat readings, calculate mean values, estimate uncertainties, and plot graphs of range against angle.
- **Unit 6 (A2):** More complex experiments may involve using video analysis software to track the trajectory of a projectile and determine its initial velocity and launch angle. Candidates should be able to: use software to capture data, plot displacement-time and velocity-time graphs, and determine $g$ from the gradient of a $v_y$-$t$ graph.

**Key Practical Skills / 关键实验技能:**
1. **Measurement / 测量:** Using protractors, meter rulers, stopwatches, and light gates accurately.
2. **Uncertainty / 不确定度:** Estimating and combining uncertainties in angle, distance, and time measurements.
3. **Graph Plotting / 图表绘制:** Plotting $R$ vs $\theta$, $R$ vs $u^2$, and $y$ vs $x$ (trajectory).
4. **Experimental Design / 实验设计:** Controlling variables (e.g., launch speed, air resistance) and suggesting improvements.

**中文：**
抛体运动为剑桥和爱德思大纲中的实验工作提供了绝佳机会。

**剑桥试卷 3（AS）/ 试卷 5（A2）：**
- **试卷 3（AS）：** 考生可能需要使用抛体发射器或斜面研究抛体射程与发射角之间的关系。测量包括：发射角（使用量角器）、射程（使用卷尺）和飞行时间（使用秒表或光门）。应考虑角度测量（$\pm 0.5^\circ$）和射程测量（$\pm 1 \, \text{mm}$）的不确定度。
- **试卷 5（A2）：** 考生可能需要设计实验以确定抛体的初始速度或验证 $R \propto u^2$ 的关系。这包括：选择合适的设备（例如抛体发射器、光门、米尺）、控制变量（例如发射角、空气阻力）以及使用图表分析数据（例如绘制 $R$ 对 $u^2$ 的图以获得通过原点的直线）。

**爱德思单元 3（AS）/ 单元 6（A2）：**
- **单元 3（AS）：** 实验研究可能涉及测量以不同角度发射的抛体的射程。考生应能够：安全设置设备、进行重复读数、计算平均值、估计不确定度以及绘制射程对角度图。
- **单元 6（A2）：** 更复杂的实验可能涉及使用视频分析软件跟踪抛体的轨迹并确定其初始速度和发射角。考生应能够：使用软件捕获数据、绘制位移-时间和速度-时间图，以及从 $v_y$-$t$ 图的斜率确定 $g$。

**关键实验技能：**
1. **测量：** 准确使用量角器、米尺、秒表和光门。
2. **不确定度：** 估计和组合角度、距离和时间测量中的不确定度。
3. **图表绘制：** 绘制 $R$ 对 $\theta$、$R$ 对 $u^2$ 以及 $y$ 对 $x$（轨迹）的图。
4. **实验设计：** 控制变量（例如发射速度、空气阻力）并提出改进建议。

> 📋 **CIE Only:** CAIE Paper 5 may require candidates to evaluate the method, identify sources of error, and suggest improvements. Common errors include: air resistance, parallax error in angle measurement, and difficulty in measuring the exact landing point.
>
> 📋 **Edexcel Only:** Edexcel Unit 6 may require candidates to use ICT (e.g., video analysis, data loggers) to collect and analyse data. Candidates should be familiar with using software to plot graphs and calculate gradients.

---

# 11. Concept Map / 概念图谱

```mermaid
graph TD
    %% Core Topic
    PM[Projectile Motion / 抛体运动]
    
    %% Prerequisites
    SV[Scalars and Vectors / 标量与矢量]
    SUVAT[Equations of Motion (SUVAT) / 运动方程]
    
    %% Sub-topics (Leaf Nodes)
    HVC[Horizontal and Vertical Components / 水平和垂直分量]
    TFR[Time of Flight and Range / 飞行时间和射程]
    MH[Maximum Height / 最大高度]
    PMG[Projectile Motion Graphs / 抛体运动图表]
    
    %% Related Topics
    NLM[Newton's Laws of Motion / 牛顿运动定律]
    
    %% Connections from Prerequisites
    SV -->|"Vector resolution / 矢量分解"| HVC
    SUVAT -->|"Apply separately to x and y / 分别应用于 x 和 y"| HVC
    SUVAT -->|"Derive equations / 推导方程"| TFR
    SUVAT -->|"Derive equation / 推导方程"| MH
    
    %% Connections to Sub-topics
    PM --> HVC
    PM --> TFR
    PM --> MH
    PM --> PMG
    
    %% Connections between Sub-topics
    HVC -->|"Determines / 决定"| TFR
    HVC -->|"Determines / 决定"| MH
    TFR -->|"Used to find / 用于求"| PMG
    MH -->|"Shown on / 显示在"| PMG
    
    %% Connections to Related Topics
    PM -->|"Explains why / 解释为什么"| NLM
    
    %% Styling
    classDef core fill:#f9f,stroke:#333,stroke-width:4px;
    classDef prereq fill:#bbf,stroke:#333,stroke-width:2px;
    classDef sub fill:#bfb,stroke:#333,stroke-width:2px;
    classDef related fill:#fbb,stroke:#333,stroke-width:2px;
    
    class PM core;
    class SV,SUVAT prereq;
    class HVC,TFR,MH,PMG sub;
    class NLM related;
```

**English:**
The concept map shows that [[Projectile Motion]] builds on [[Scalars and Vectors]] (for resolving initial velocity) and [[Equations of Motion (SUVAT)]] (for describing motion in each component). The four sub-topics — [[Horizontal and Vertical Components]], [[Time of Flight and Range]], [[Maximum Height]], and [[Projectile Motion Graphs]] — are interconnected. The topic also relates to [[Newton's Laws of Motion]], particularly the first law (constant horizontal velocity due to no net force) and the second law (vertical acceleration due to gravity).

**中文：**
概念图显示[[抛体运动]]建立在[[标量与矢量]]（用于分解初始速度）和[[运动方程（SUVAT）]]（用于描述每个分量中的运动）之上。四个子主题——[[水平和垂直分量]]、[[飞行时间和射程]]、[[最大高度]]和[[抛体运动图表]]——相互关联。该主题还与[[牛顿运动定律]]相关，特别是第一定律（由于无净力导致水平速度恒定）和第二定律（由于重力导致垂直加速度）。

---

# 12. Quick Revision Sheet / 速查表

| Category / 类别 | Key Points / 要点 |
|----------------|------------------|
| **Definitions / 定义** | **Projectile:** Object moving under gravity only, after initial launch. / 抛体：初始发射后仅受重力作用的物体。<br>**Trajectory:** Parabolic path of projectile. / 轨迹：抛体的抛物线路径。<br>**Time of Flight ($T$):** Total time in air. / 飞行时间 ($T$)：在空中总时间。<br>**Range ($R$):** Horizontal distance travelled. / 射程 ($R$)：水平行进距离。<br>**Maximum Height ($H$):** Greatest vertical displacement. / 最大高度 ($H$)：最大垂直位移。 |
| **Equations / 公式** | **Resolution:** $u_x = u \cos \theta$, $u_y = u \sin \theta$ / 分解<br>**Time of Flight:** $T = \frac{2u \sin \theta}{g}$ (symmetrical) / 飞行时间（对称）<br>**Range:** $R = \frac{u^2 \sin 2\theta}{g}$ (symmetrical) / 射程（对称）<br>**Max Height:** $H = \frac{u^2 \sin^2 \theta}{2g}$ / 最大高度<br>**Trajectory:** $y = x \tan \theta - \frac{g x^2}{2u^2 \cos^2 \theta}$ / 轨迹<br>**Vertical velocity:** $v_y = u \sin \theta - gt$ / 垂直速度<br>**Vertical displacement:** $s_y = (u \sin \theta)t - \frac{1}{2}gt^2$ / 垂直位移 |
| **Graphs / 图表** | **$x$-$t$:** Straight line (constant $v_x$) / 直线（恒定 $v_x$）<br>**$y$-$t$:** Parabola (maximum at $T/2$) / 抛物线（在 $T/2$ 处最大）<br>**$v_y$-$t$:** Straight line with slope $-g$ / 斜率为 $-g$ 的直线<br>**$v_x$-$t$:** Horizontal line / 水平线<br>**$y$-$x$:** Parabola (trajectory) / 抛物线（轨迹） |
| **Key Facts / 关键事实** | 1. Horizontal and vertical motions are independent. / 水平和垂直运动独立。<br>2. Horizontal velocity is constant (no air resistance). / 水平速度恒定（无空气阻力）。<br>3. Vertical acceleration is $g = 9.81 \, \text{m s}^{-2}$ downward. / 垂直加速度为向下的 $g = 9.81 \, \text{m s}^{-2}$。<br>4. Time of flight depends only on vertical motion. / 飞行时间仅取决于垂直运动。<br>5. Maximum range at $\theta = 45^\circ$. / 最大射程在 $\theta = 45^\circ$ 时。<br>6. Complementary angles ($\theta$ and $90^\circ - \theta$) give same range. / 互补角（$\theta$ 和 $90^\circ - \theta$）给出相同射程。<br>7. At maximum height, $v_y = 0$ but $v_x \neq 0$. / 在最大高度处，$v_y = 0$ 但 $v_x \neq 0$。<br>8. For symmetrical flight, time up = time down. / 对于对称飞行，上升时间 = 下降时间。 |
| **Exam Reminders / 考试提醒** | ✅ Always resolve $u$ into $u_x$ and $u_y$ first. / 始终先将 $u$ 分解为 $u_x$ 和 $u_y$。<br>✅ Use separate SUVAT lists for $x$ and $y$. / 为 $x$ 和 $y$ 分别使用 SUVAT 列表。<br>✅ Time $t$ is the same for both components. / 时间 $t$ 对两个分量相同。<br>✅ Watch sign convention (upward positive). / 注意符号约定（向上为正）。<br>✅ Check calculator is in degree mode. / 检查计算器处于角度模式。<br>✅ For asymmetrical flight, solve quadratic for $t$. / 对于非对称飞行，求解 $t$ 的二次方程。<br>✅ Include units in final answers. / 在最终答案中包含单位。<br>✅ For Edexcel: be ready to derive equations. / 对于爱德思：准备好推导方程。<br>✅ For CAIE: be ready for practical design questions. / 对于剑桥：准备好实验设计题。 |

---

> 📝 **Document Version / 文档版本:** v1.0
> **Last Updated / 最后更新:** 2025-01-01
> **Author / 作者:** AI Physics Knowledge Graph Architect
> **Parent Folder / 父文件夹:** vault/01-Mechanics/01-Kinematics/Projectile Motion/
> **Sub-topics / 子主题:** [[Horizontal and Vertical Components]], [[Time of Flight and Range]], [[Maximum Height]], [[Projectile Motion Graphs]]
> **Prerequisites / 先决条件:** [[Scalars and Vectors]], [[Equations of Motion (SUVAT)]]
> **Related Topics / 相关主题:** [[Newton's Laws of Motion]]