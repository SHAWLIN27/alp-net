# 1. Overview / 概述

**English:** Projectile Motion is the study of objects moving under the influence of gravity after being launched with an initial velocity. This topic bridges [[Scalars and Vectors]] with [[Equations of Motion (SUVAT)]] by treating motion as two independent components: horizontal (constant velocity) and vertical (constant acceleration due to gravity). In both CAIE 9702 and Edexcel IAL, this is a high-frequency exam topic (typically 1-2 questions per paper) that tests vector resolution, kinematic equations, and graphical analysis. Real-world applications include sports (basketball trajectories, golf drives), military ballistics, fireworks displays, and space probe landings. Mastering projectile motion develops critical problem-solving skills in decomposing 2D motion into 1D components.

**中文:** 抛体运动研究物体在获得初速度后仅在重力作用下运动的规律。该主题通过将运动分解为两个独立分量——水平方向（匀速运动）和竖直方向（匀加速运动，加速度为重力加速度），将[[标量与矢量]]和[[运动学方程（SUVAT）]]联系起来。在CAIE 9702和Edexcel IAL考试中，这是高频考点（通常每份试卷1-2题），考查矢量分解、运动学方程和图像分析能力。实际应用包括体育运动（篮球轨迹、高尔夫击球）、军事弹道学、烟花表演和太空探测器着陆。掌握抛体运动能培养将二维运动分解为一维运动的关键解题能力。

---

# 2. Syllabus Learning Objectives / 考纲学习目标

| CAIE 9702 (3.1 l-m) | Edexcel IAL (WPH11 U1: 1.13-1.16) |
|---|---|
| Describe and explain motion due to uniform velocity in one direction and uniform acceleration in a perpendicular direction | Recognise that projectile motion is the combination of two independent motions: horizontal (constant velocity) and vertical (constant acceleration) |
| Derive and use equations for projectile motion | Use equations of motion to solve problems involving projectiles |
| Solve problems involving projectiles launched horizontally and at an angle | Analyse projectile motion using vector components |
| Interpret displacement-time, velocity-time, and acceleration-time graphs for projectile motion | Calculate time of flight, range, and maximum height |

**Examiner Expectations / 考官期望:**
- **English:** Candidates must clearly state assumptions (no air resistance, constant g = 9.81 m s⁻²). Always resolve initial velocity into horizontal and vertical components using $u_x = u\cos\theta$ and $u_y = u\sin\theta$. Treat horizontal and vertical motions independently. Use sign conventions consistently (usually upward positive). Show all working with clear SUVAT variable identification.
- **中文:** 考生必须明确说明假设条件（无空气阻力，重力加速度g = 9.81 m s⁻²为常数）。始终将初速度分解为水平分量 $u_x = u\cos\theta$ 和竖直分量 $u_y = u\sin\theta$。将水平和竖直运动独立处理。保持符号约定一致（通常取向上为正）。展示完整解题过程，清晰标出SUVAT变量。

> 📋 **CIE Only:** Questions often require deriving the equation of trajectory $y = x\tan\theta - \frac{gx^2}{2u^2\cos^2\theta}$ and interpreting its parabolic shape. Graph sketching is frequently tested.
> 
> 📋 **Edexcel Only:** Questions may involve projectiles launched from a height (e.g., from a cliff) or onto an inclined plane. Vector notation ($\mathbf{v} = v_x\mathbf{i} + v_y\mathbf{j}$) is sometimes used.

---

# 3. Core Definitions / 核心定义

| Term (EN/CN) | Definition (EN) | Definition (CN) | Common Mistakes / 常见错误 |
|---|---|---|---|
| [[Projectile Motion]] / 抛体运动 | The motion of an object moving under the influence of gravity only, after being given an initial velocity | 物体在获得初速度后仅在重力作用下的运动 | Confusing with free fall (projectile has initial velocity, free fall starts from rest) |
| [[Trajectory]] / 轨迹 | The curved path followed by a projectile | 抛体运动的弯曲路径 | Thinking trajectory is always symmetric (only symmetric if launch and landing heights are equal) |
| [[Time of Flight]] / 飞行时间 | The total time a projectile remains in the air from launch to landing | 抛体从发射到落地在空中停留的总时间 | Using horizontal equation to find time (must use vertical motion) |
| [[Range]] / 射程 | The horizontal distance travelled by a projectile from launch to landing | 抛体从发射点到落地点的水平距离 | Forgetting range depends on $\sin 2\theta$, not just angle |
| [[Maximum Height]] / 最大高度 | The highest vertical position reached by a projectile | 抛体达到的最高竖直位置 | Confusing maximum height with vertical displacement at any time |
| [[Angle of Projection]] / 投射角 | The angle at which the projectile is launched relative to the horizontal | 抛体发射方向与水平方向的夹角 | Using degrees in calculator without checking mode |
| [[Component]] / 分量 | The horizontal or vertical part of a vector quantity | 矢量在水平或竖直方向上的部分 | Forgetting that components are independent and perpendicular |

---

# 4. Key Concepts Explained / 关键概念详解

## 4.1 Independence of Horizontal and Vertical Motion / 水平与竖直运动的独立性

### Explanation / 解释
**English:** The fundamental principle of [[Projectile Motion]] is that horizontal and vertical motions are completely independent. The horizontal component of velocity ($v_x$) remains constant because there is no horizontal force (assuming no air resistance). The vertical component ($v_y$) changes uniformly due to [[Gravitational Acceleration]] ($g = 9.81 \text{ m s}^{-2}$ downward). This independence allows us to apply [[Equations of Motion (SUVAT)]] separately to each direction.

**中文:** 抛体运动的基本原理是水平和竖直运动完全独立。水平速度分量（$v_x$）保持不变，因为没有水平方向的作用力（假设无空气阻力）。竖直速度分量（$v_y$）由于[[重力加速度]]（$g = 9.81 \text{ m s}^{-2}$，方向向下）而均匀变化。这种独立性使我们能够对每个方向分别应用[[运动学方程（SUVAT）]]。

### Physical Meaning / 物理意义
**English:** A bullet dropped and a bullet fired horizontally from the same height will hit the ground at the same time. The horizontal motion does not affect the vertical motion. This is demonstrated by the classic "monkey and hunter" experiment.

**中文:** 从同一高度自由落下的子弹和水平射出的子弹将同时落地。水平运动不影响竖直运动。经典的"猴子和猎人"实验证明了这一点。

### Common Misconceptions / 常见误区
- Thinking a projectile stops moving vertically at maximum height (it still has horizontal velocity)
- Believing heavier objects have different trajectories (in vacuum, all objects fall at same rate)
- Confusing the path shape (parabola) with the velocity vector direction (tangent to path)
- Assuming the angle for maximum range is always 45° (only true for level ground with no air resistance)

### Exam Tips / 考试提示
**English:** Always draw a diagram showing the initial velocity vector resolved into $u_x$ and $u_y$ components. Label the positive direction (usually upward). Write separate SUVAT lists for horizontal and vertical motion. Remember: $a_x = 0$, $a_y = -g$ (or $+g$ depending on sign convention).

**中文:** 始终画出初速度矢量分解为$u_x$和$u_y$分量的示意图。标出正方向（通常向上为正）。为水平和竖直运动分别列出SUVAT变量。记住：$a_x = 0$，$a_y = -g$（或根据符号约定取$+g$）。

> 📷 **IMAGE PROMPT — [PM-01]: Independence of Motion Demonstration**
> **English:** A side-by-side comparison diagram showing two balls released from the same height: Ball A dropped vertically (free fall) and Ball B launched horizontally. Both balls are shown at equal time intervals (strobe effect) reaching the ground simultaneously. Labels: "Ball A: Dropped", "Ball B: Horizontally Launched", "Same height h", "Same time t", "Horizontal velocity constant". Style: Clean physics textbook illustration, vector arrows showing velocities at each position. Exam importance: HIGH - fundamental concept tested in multiple-choice and theory questions.
> **中文:** 并排对比图，显示从同一高度释放的两个球：球A竖直下落（自由落体）和球B水平发射。两个球以相等时间间隔显示（频闪效果），同时到达地面。标签："球A：自由下落"，"球B：水平发射"，"相同高度h"，"相同时间t"，"水平速度恒定"。风格：清晰的物理教科书插图，每个位置用矢量箭头表示速度。考试重要性：高——基础概念，在选择题和理论题中均有考查。

---

## 4.2 Resolving Initial Velocity / 初速度的分解

### Explanation / 解释
**English:** For a projectile launched with initial speed $u$ at angle $\theta$ above the horizontal, the initial velocity components are:
- Horizontal: $u_x = u\cos\theta$ (constant throughout motion)
- Vertical: $u_y = u\sin\theta$ (changes due to gravity)

These components are found using [[Vector Resolution]] from [[Scalars and Vectors]].

**中文:** 对于以初速度$u$、与水平方向夹角$\theta$发射的抛体，初速度分量为：
- 水平方向：$u_x = u\cos\theta$（整个运动过程中保持不变）
- 竖直方向：$u_y = u\sin\theta$（因重力而变化）

这些分量通过[[矢量分解]]从[[标量与矢量]]中得到。

### Physical Meaning / 物理意义
**English:** The angle $\theta$ determines how much of the initial velocity goes into horizontal vs vertical motion. A larger angle gives more vertical velocity (higher flight, shorter range). A smaller angle gives more horizontal velocity (lower flight, longer range). At $\theta = 90^\circ$, the projectile goes straight up (vertical projection). At $\theta = 0^\circ$, it's purely horizontal projection.

**中文:** 角度$\theta$决定了初速度中有多少分配给水平运动和竖直运动。较大的角度提供更大的竖直速度（飞行更高，射程更短）。较小的角度提供更大的水平速度（飞行更低，射程更远）。当$\theta = 90^\circ$时，抛体竖直向上运动（竖直上抛）。当$\theta = 0^\circ$时，为纯水平抛射。

### Common Misconceptions / 常见误区
- Using $u\cos\theta$ for vertical component (common sign error)
- Forgetting to check calculator is in degree mode
- Assuming components are equal when $\theta = 45^\circ$ (they are: $u\cos45^\circ = u\sin45^\circ = u/\sqrt{2}$)
- Not resolving when projectile is launched horizontally ($\theta = 0^\circ$, so $u_x = u$, $u_y = 0$)

### Exam Tips / 考试提示
**English:** Write $u_x = u\cos\theta$ and $u_y = u\sin\theta$ as the first step in any projectile problem. For horizontal projection, state $u_x = u$ and $u_y = 0$ explicitly. Always include the angle in the diagram.

**中文:** 在任何抛体问题的第一步都写出$u_x = u\cos\theta$和$u_y = u\sin\theta$。对于水平抛射，明确写出$u_x = u$和$u_y = 0$。始终在图中标出角度。

---

## 4.3 Time of Flight / 飞行时间

### Explanation / 解释
**English:** [[Time of Flight]] ($T$) is found using vertical motion only. For a projectile launched from and landing at the same height:
$$T = \frac{2u\sin\theta}{g}$$

Derivation: Use $s = u_yt + \frac{1}{2}a_yt^2$ with $s = 0$ (net vertical displacement is zero), $u_y = u\sin\theta$, $a_y = -g$:
$$0 = (u\sin\theta)T - \frac{1}{2}gT^2$$
$$T(u\sin\theta - \frac{1}{2}gT) = 0$$
$$T = 0 \text{ (launch)} \quad \text{or} \quad T = \frac{2u\sin\theta}{g}$$

**中文:** [[飞行时间]]（$T$）仅通过竖直运动求得。对于从同一高度发射和落地的抛体：
$$T = \frac{2u\sin\theta}{g}$$

推导：使用$s = u_yt + \frac{1}{2}a_yt^2$，其中$s = 0$（净竖直位移为零），$u_y = u\sin\theta$，$a_y = -g$：
$$0 = (u\sin\theta)T - \frac{1}{2}gT^2$$
$$T(u\sin\theta - \frac{1}{2}gT) = 0$$
$$T = 0 \text{（发射时刻）} \quad \text{或} \quad T = \frac{2u\sin\theta}{g}$$

### Physical Meaning / 物理意义
**English:** Time of flight depends only on the vertical component of initial velocity and gravity. A projectile launched at a steeper angle stays in the air longer. For a given launch speed, maximum time of flight occurs at $\theta = 90^\circ$ (straight up).

**中文:** 飞行时间仅取决于初速度的竖直分量和重力加速度。以更陡角度发射的抛体在空中停留时间更长。对于给定的发射速度，最大飞行时间出现在$\theta = 90^\circ$（竖直上抛）。

### Common Misconceptions / 常见误区
- Using horizontal motion to find time of flight
- Forgetting that $s = 0$ only when launch and landing heights are equal
- Not considering the case where projectile lands at a different height (e.g., launched from cliff)

### Exam Tips / 考试提示
**English:** For projectiles landing at a different height, use $s = u_yt + \frac{1}{2}a_yt^2$ with the correct displacement value (positive if landing below launch point, negative if above). Solve the quadratic equation for $t$.

**中文:** 对于在不同高度落地的抛体，使用$s = u_yt + \frac{1}{2}a_yt^2$，代入正确的位移值（如果落点低于发射点则为正，高于发射点则为负）。解二次方程求$t$。

---

## 4.4 Range / 射程

### Explanation / 解释
**English:** [[Range]] ($R$) is the horizontal distance travelled. Since horizontal velocity is constant:
$$R = u_x \times T = (u\cos\theta) \times \frac{2u\sin\theta}{g} = \frac{2u^2\sin\theta\cos\theta}{g} = \frac{u^2\sin 2\theta}{g}$$

The maximum range for a given launch speed occurs when $\sin 2\theta = 1$, i.e., $2\theta = 90^\circ$, so $\theta = 45^\circ$.

**中文:** [[射程]]（$R$）是水平方向运动的距离。由于水平速度恒定：
$$R = u_x \times T = (u\cos\theta) \times \frac{2u\sin\theta}{g} = \frac{2u^2\sin\theta\cos\theta}{g} = \frac{u^2\sin 2\theta}{g}$$

对于给定的发射速度，最大射程出现在$\sin 2\theta = 1$时，即$2\theta = 90^\circ$，所以$\theta = 45^\circ$。

### Physical Meaning / 物理意义
**English:** Range depends on both horizontal and vertical components. Complementary angles ($\theta$ and $90^\circ - \theta$) give the same range because $\sin 2\theta = \sin(180^\circ - 2\theta) = \sin 2(90^\circ - \theta)$. For example, $30^\circ$ and $60^\circ$ give the same range (but different times of flight and maximum heights).

**中文:** 射程取决于水平和竖直两个分量。互补角（$\theta$和$90^\circ - \theta$）给出相同的射程，因为$\sin 2\theta = \sin(180^\circ - 2\theta) = \sin 2(90^\circ - \theta)$。例如，$30^\circ$和$60^\circ$给出相同的射程（但飞行时间和最大高度不同）。

### Common Misconceptions / 常见误区
- Thinking $45^\circ$ always gives maximum range (only true for level ground, no air resistance)
- Forgetting the $\sin 2\theta$ relationship and using $\sin\theta$ alone
- Not recognizing that range is proportional to $u^2$ (doubling speed quadruples range)

### Exam Tips / 考试提示
**English:** When asked for maximum range, immediately state $\theta = 45^\circ$ and use $R_{\text{max}} = u^2/g$. For range at any angle, use $R = u^2\sin 2\theta/g$. Remember to check if launch and landing heights are equal before using these formulas.

**中文:** 当问到最大射程时，立即写出$\theta = 45^\circ$并使用$R_{\text{max}} = u^2/g$。对于任意角度的射程，使用$R = u^2\sin 2\theta/g$。在使用这些公式前，检查发射和落地高度是否相等。

> 📷 **IMAGE PROMPT — [PM-02]: Range vs Angle of Projection**
> **English:** A graph showing Range (R) on y-axis vs Angle of projection (θ) on x-axis from 0° to 90°. The curve is a parabola-like shape peaking at θ = 45°. Dashed vertical line at 45° labeled "Maximum Range". Two points at 30° and 60° marked with same range value, connected by a horizontal dashed line labeled "Same Range". Labels: "R = u²sin2θ/g", "Rmax = u²/g at θ = 45°". Style: Scientific graph with gridlines, clear axis labels with units. Exam importance: HIGH - frequently tested in data analysis and theory questions.
> **中文:** 图表显示射程（R）随投射角（θ）从0°到90°的变化曲线。曲线呈抛物线状，在θ = 45°处达到峰值。在45°处画垂直虚线，标注"最大射程"。在30°和60°处标记相同射程值，用水平虚线连接，标注"相同射程"。标签："R = u²sin2θ/g"，"Rmax = u²/g，θ = 45°"。风格：带网格线的科学图表，清晰的轴标签和单位。考试重要性：高——在数据分析和理论题中频繁考查。

---

## 4.5 Maximum Height / 最大高度

### Explanation / 解释
**English:** [[Maximum Height]] ($H$) is reached when the vertical velocity becomes zero ($v_y = 0$). Using $v_y^2 = u_y^2 + 2a_ys$:
$$0 = (u\sin\theta)^2 - 2gH$$
$$H = \frac{u^2\sin^2\theta}{2g}$$

The time to reach maximum height is half the time of flight: $t_{\text{peak}} = \frac{T}{2} = \frac{u\sin\theta}{g}$

**中文:** [[最大高度]]（$H$）在竖直速度为零（$v_y = 0$）时达到。使用$v_y^2 = u_y^2 + 2a_ys$：
$$0 = (u\sin\theta)^2 - 2gH$$
$$H = \frac{u^2\sin^2\theta}{2g}$$

到达最大高度的时间是飞行时间的一半：$t_{\text{peak}} = \frac{T}{2} = \frac{u\sin\theta}{g}$

### Physical Meaning / 物理意义
**English:** Maximum height depends only on the vertical component of initial velocity. A projectile launched at 90° (straight up) achieves maximum height $H_{\text{max}} = u^2/2g$. The path is symmetric about the maximum height point when launch and landing heights are equal.

**中文:** 最大高度仅取决于初速度的竖直分量。以90°（竖直向上）发射的抛体达到最大高度$H_{\text{max}} = u^2/2g$。当发射和落地高度相等时，轨迹关于最大高度点对称。

### Common Misconceptions / 常见误区
- Thinking velocity is zero at maximum height (only vertical component is zero; horizontal component remains)
- Using $v = u + at$ instead of $v^2 = u^2 + 2as$ to find maximum height
- Forgetting that $v_y = 0$ at the peak is the key condition

### Exam Tips / 考试提示
**English:** At maximum height, write $v_y = 0$ as your starting condition. Use $v_y^2 = u_y^2 + 2a_ys$ for height. Use $v_y = u_y + a_yt$ for time to peak. Remember: at the peak, the projectile still has horizontal velocity $v_x = u\cos\theta$.

**中文:** 在最大高度处，以$v_y = 0$作为起始条件。使用$v_y^2 = u_y^2 + 2a_ys$求高度。使用$v_y = u_y + a_yt$求到达最高点的时间。记住：在最高点，抛体仍然具有水平速度$v_x = u\cos\theta$。

---

## 4.6 Equation of Trajectory / 轨迹方程

### Explanation / 解释
**English:** The [[Trajectory]] equation relates horizontal position $x$ to vertical position $y$, eliminating time $t$:
$$y = x\tan\theta - \frac{gx^2}{2u^2\cos^2\theta}$$

Derivation: From $x = (u\cos\theta)t$, we get $t = \frac{x}{u\cos\theta}$. Substitute into $y = (u\sin\theta)t - \frac{1}{2}gt^2$:
$$y = (u\sin\theta)\frac{x}{u\cos\theta} - \frac{1}{2}g\left(\frac{x}{u\cos\theta}\right)^2$$
$$y = x\tan\theta - \frac{gx^2}{2u^2\cos^2\theta}$$

This is a quadratic equation in $x$, confirming the parabolic shape.

**中文:** [[轨迹]]方程将水平位置$x$与竖直位置$y$联系起来，消去时间$t$：
$$y = x\tan\theta - \frac{gx^2}{2u^2\cos^2\theta}$$

推导：由$x = (u\cos\theta)t$得$t = \frac{x}{u\cos\theta}$。代入$y = (u\sin\theta)t - \frac{1}{2}gt^2$：
$$y = (u\sin\theta)\frac{x}{u\cos\theta} - \frac{1}{2}g\left(\frac{x}{u\cos\theta}\right)^2$$
$$y = x\tan\theta - \frac{gx^2}{2u^2\cos^2\theta}$$

这是关于$x$的二次方程，证实了抛物线形状。

### Physical Meaning / 物理意义
**English:** The trajectory equation shows that projectile motion follows a parabolic path. The coefficient of $x^2$ is negative, confirming the parabola opens downward. This equation is useful for finding the height at any horizontal position or determining if a projectile can clear an obstacle.

**中文:** 轨迹方程表明抛体运动遵循抛物线路径。$x^2$的系数为负，确认抛物线开口向下。该方程可用于求任意水平位置的高度，或判断抛体是否能越过障碍物。

### Common Misconceptions / 常见误区
- Thinking the trajectory is always symmetric (only when launch and landing heights are equal)
- Forgetting that this equation assumes no air resistance
- Using this equation when time is given (use parametric equations instead)

### Exam Tips / 考试提示
**English:** Use the trajectory equation when you need to find $y$ at a given $x$, or vice versa. For CAIE, you may be asked to derive this equation. For Edexcel, you may need to use it to solve problems involving obstacles. Remember: $y = 0$ at launch and landing points (same height).

**中文:** 当需要求给定$x$处的$y$值，或反之，使用轨迹方程。对于CAIE考试，可能会要求推导该方程。对于Edexcel考试，可能需要用它解决涉及障碍物的问题。记住：在发射点和落地点（相同高度）$y = 0$。

> 📷 **IMAGE PROMPT — [PM-03]: Projectile Trajectory with Key Points**
> **English:** A parabolic trajectory curve showing a projectile launched from point O at angle θ. Key points labeled: Launch point O (0,0), Maximum height point P (R/2, H) with tangent line showing only horizontal velocity, Landing point Q (R, 0). Velocity vectors shown at O (u at angle θ), P (horizontal only, ucosθ), and Q (u at angle -θ). Dashed lines showing horizontal and vertical components at launch. Labels: "u", "θ", "ux = ucosθ", "uy = usinθ", "Range R", "Maximum Height H", "Time of Flight T". Style: Clean physics diagram with vector arrows, dashed construction lines, clear labels. Exam importance: HIGH - standard diagram for all projectile problems.
> **中文:** 抛物线轨迹曲线，显示从O点以角度θ发射的抛体。关键点标注：发射点O (0,0)，最高点P (R/2, H)（切线显示只有水平速度），落地点Q (R, 0)。在O点（速度u，角度θ）、P点（只有水平速度ucosθ）和Q点（速度u，角度-θ）显示速度矢量。虚线显示发射时的水平和竖直分量。标签："u"，"θ"，"ux = ucosθ"，"uy = usinθ"，"射程R"，"最大高度H"，"飞行时间T"。风格：带矢量箭头的清晰物理图，虚线辅助线，清晰标签。考试重要性：高——所有抛体问题的标准图示。

---

# 5. Essential Equations / 核心公式

## 5.1 Initial Velocity Components / 初速度分量

$$u_x = u\cos\theta \quad \text{and} \quad u_y = u\sin\theta$$

| Symbol (符号) | Meaning (EN/CN) | Unit (单位) |
|---|---|---|
| $u$ | Initial speed / 初速度 | m s⁻¹ |
| $\theta$ | Angle of projection above horizontal / 投射角（与水平方向夹角） | degrees (°) or rad |
| $u_x$ | Horizontal component of initial velocity / 初速度水平分量 | m s⁻¹ |
| $u_y$ | Vertical component of initial velocity / 初速度竖直分量 | m s⁻¹ |

**Conditions:** Always true for any projectile launched at angle $\theta$ above horizontal. For horizontal projection, $\theta = 0^\circ$, so $u_x = u$, $u_y = 0$.

---

## 5.2 Time of Flight / 飞行时间

$$T = \frac{2u\sin\theta}{g}$$

| Symbol (符号) | Meaning (EN/CN) | Unit (单位) |
|---|---|---|
| $T$ | Time of flight / 飞行时间 | s |
| $u$ | Initial speed / 初速度 | m s⁻¹ |
| $\theta$ | Angle of projection / 投射角 | ° |
| $g$ | Acceleration due to gravity (9.81 m s⁻²) / 重力加速度 | m s⁻² |

**Derivation:** From $s = u_yt + \frac{1}{2}a_yt^2$ with $s = 0$, $u_y = u\sin\theta$, $a_y = -g$.

**Conditions:** Only valid when launch and landing heights are equal. For different heights, solve $s = u_yt + \frac{1}{2}a_yt^2$ with the correct $s$ value.

**Rearrangements:** $u = \frac{gT}{2\sin\theta}$, $\sin\theta = \frac{gT}{2u}$

---

## 5.3 Range / 射程

$$R = \frac{u^2\sin 2\theta}{g}$$

| Symbol (符号) | Meaning (EN/CN) | Unit (单位) |
|---|---|---|
| $R$ | Range (horizontal distance) / 射程（水平距离） | m |
| $u$ | Initial speed / 初速度 | m s⁻¹ |
| $\theta$ | Angle of projection / 投射角 | ° |
| $g$ | Acceleration due to gravity / 重力加速度 | m s⁻² |

**Derivation:** $R = u_x \times T = (u\cos\theta) \times \frac{2u\sin\theta}{g} = \frac{2u^2\sin\theta\cos\theta}{g} = \frac{u^2\sin 2\theta}{g}$

**Conditions:** Same as time of flight (equal launch and landing heights). Maximum range when $\theta = 45^\circ$: $R_{\text{max}} = u^2/g$.

**Rearrangements:** $u = \sqrt{\frac{Rg}{\sin 2\theta}}$, $\sin 2\theta = \frac{Rg}{u^2}$

---

## 5.4 Maximum Height / 最大高度

$$H = \frac{u^2\sin^2\theta}{2g}$$

| Symbol (符号) | Meaning (EN/CN) | Unit (单位) |
|---|---|---|
| $H$ | Maximum height reached / 达到的最大高度 | m |
| $u$ | Initial speed / 初速度 | m s⁻¹ |
| $\theta$ | Angle of projection / 投射角 | ° |
| $g$ | Acceleration due to gravity / 重力加速度 | m s⁻² |

**Derivation:** From $v_y^2 = u_y^2 + 2a_ys$ with $v_y = 0$, $u_y = u\sin\theta$, $a_y = -g$, $s = H$.

**Conditions:** Valid for any projectile motion. Time to reach maximum height: $t_{\text{peak}} = \frac{u\sin\theta}{g} = \frac{T}{2}$.

**Rearrangements:** $u = \sqrt{\frac{2gH}{\sin^2\theta}}$, $\sin\theta = \sqrt{\frac{2gH}{u^2}}$

---

## 5.5 Equation of Trajectory / 轨迹方程

$$y = x\tan\theta - \frac{gx^2}{2u^2\cos^2\theta}$$

| Symbol (符号) | Meaning (EN/CN) | Unit (单位) |
|---|---|---|
| $x$ | Horizontal displacement from launch point / 距发射点的水平位移 | m |
| $y$ | Vertical displacement from launch point / 距发射点的竖直位移 | m |
| $u$ | Initial speed / 初速度 | m s⁻¹ |
| $\theta$ | Angle of projection / 投射角 | ° |
| $g$ | Acceleration due to gravity / 重力加速度 | m s⁻² |

**Derivation:** Eliminate $t$ from $x = (u\cos\theta)t$ and $y = (u\sin\theta)t - \frac{1}{2}gt^2$.

**Conditions:** Valid for any projectile motion. Assumes launch point at origin (0,0). For different launch heights, add constant $y_0$: $y = y_0 + x\tan\theta - \frac{gx^2}{2u^2\cos^2\theta}$.

**Alternative form:** $y = x\tan\theta - \frac{gx^2}{2u^2}(1 + \tan^2\theta)$ (using $\frac{1}{\cos^2\theta} = 1 + \tan^2\theta$)

---

## 5.6 Velocity at Any Time / 任意时刻的速度

$$v_x = u\cos\theta \quad \text{(constant)}$$
$$v_y = u\sin\theta - gt$$
$$v = \sqrt{v_x^2 + v_y^2}$$
$$\phi = \tan^{-1}\left(\frac{v_y}{v_x}\right)$$

| Symbol (符号) | Meaning (EN/CN) | Unit (单位) |
|---|---|---|
| $v$ | Speed at time $t$ / t时刻的速率 | m s⁻¹ |
| $\phi$ | Direction of velocity below horizontal at time $t$ / t时刻速度方向与水平方向的夹角 | ° |
| $t$ | Time after launch / 发射后的时间 | s |

**Conditions:** Valid for any time $t$ during flight. At maximum height, $v_y = 0$, so $v = v_x = u\cos\theta$ and $\phi = 0^\circ$.

---

# 6. Graphs and Relationships / 图表与关系

## 6.1 Horizontal Displacement-Time Graph / 水平位移-时间图

**Axes:** x-axis: Time ($t$ / s), y-axis: Horizontal displacement ($x$ / m)

**Shape:** Straight line through origin with positive slope.

**Gradient Meaning:** 
- **English:** Gradient = horizontal velocity ($v_x = u\cos\theta$), which is constant.
- **中文:** 斜率 = 水平速度（$v_x = u\cos\theta$），为常数。

**Area Meaning:** Not applicable (area under $x$-$t$ graph has no physical meaning).

**Exam Interpretation:** 
- **English:** A steeper line means greater horizontal velocity. The line is always straight (no acceleration horizontally).
- **中文:** 更陡的线表示更大的水平速度。线始终是直的（水平方向无加速度）。

**Common Questions:** Finding horizontal velocity from gradient, comparing projectiles with different launch angles.

> 📷 **IMAGE PROMPT — [PM-04]: Horizontal Displacement-Time Graph**
> **English:** A graph with time (s) on x-axis and horizontal displacement (m) on y-axis. A straight line through origin with positive slope. Label: "x = (ucosθ)t", "Gradient = ucosθ = constant". Style: Clean scientific graph with gridlines. Exam importance: MEDIUM - basic understanding required.
> **中文:** 时间（s）为x轴，水平位移（m）为y轴的图表。一条通过原点的直线，斜率为正。标签："x = (ucosθ)t"，"斜率 = ucosθ = 常数"。风格：带网格线的清晰科学图表。考试重要性：中——需要基本理解。

---

## 6.2 Vertical Displacement-Time Graph / 竖直位移-时间图

**Axes:** x-axis: Time ($t$ / s), y-axis: Vertical displacement ($y$ / m)

**Shape:** Parabola opening downward, symmetric about the peak.

**Gradient Meaning:** 
- **English:** Gradient = vertical velocity ($v_y$). At $t = 0$, gradient = $u\sin\theta$ (positive). At peak, gradient = 0. At landing, gradient = $-u\sin\theta$ (negative).
- **中文:** 斜率 = 竖直速度（$v_y$）。在$t = 0$时，斜率 = $u\sin\theta$（正）。在最高点，斜率 = 0。在落地点，斜率 = $-u\sin\theta$（负）。

**Area Meaning:** Not directly applicable.

**Exam Interpretation:** 
- **English:** The peak of the parabola corresponds to maximum height. The time at the peak is $t = u\sin\theta/g$. The graph is symmetric about the peak when launch and landing heights are equal.
- **中文:** 抛物线的顶点对应最大高度。到达顶点的时间为$t = u\sin\theta/g$。当发射和落地高度相等时，图形关于顶点对称。

**Common Questions:** Finding maximum height from graph, determining time of flight, comparing vertical motion of different projectiles.

> 📷 **IMAGE PROMPT — [PM-05]: Vertical Displacement-Time Graph**
> **English:** A parabolic curve opening downward on a graph with time (s) on x-axis and vertical displacement (m) on y-axis. Peak labeled: "Maximum Height H". Points at t=0 and t=T where y=0. Tangent lines at three points showing gradient (velocity) decreasing from positive to zero to negative. Labels: "y = (usinθ)t - ½gt²", "At peak: vy = 0". Style: Scientific graph with tangent lines showing gradient interpretation. Exam importance: HIGH - frequently tested in data analysis.
> **中文:** 时间（s）为x轴，竖直位移（m）为y轴的开口向下抛物线。顶点标注："最大高度H"。在t=0和t=T处y=0的点。三个点的切线显示梯度（速度）从正到零再到负。标签："y = (usinθ)t - ½gt²"，"在顶点：vy = 0"。风格：带切线显示梯度解释的科学图表。考试重要性：高——在数据分析中频繁考查。

---

## 6.3 Horizontal Velocity-Time Graph / 水平速度-时间图

**Axes:** x-axis: Time ($t$ / s), y-axis: Horizontal velocity ($v_x$ / m s⁻¹)

**Shape:** Horizontal straight line (constant velocity).

**Gradient Meaning:** 
- **English:** Gradient = horizontal acceleration = 0 (no horizontal force).
- **中文:** 斜率 = 水平加速度 = 0（无水平方向作用力）。

**Area Meaning:** 
- **English:** Area under graph = horizontal displacement ($x$). For time $T$, area = $v_x \times T = R$ (range).
- **中文:** 图线下方面积 = 水平位移（$x$）。对于时间$T$，面积 = $v_x \times T = R$（射程）。

**Exam Interpretation:** 
- **English:** The line is always horizontal at $v_x = u\cos\theta$. Any deviation would indicate horizontal acceleration (air resistance).
- **中文:** 线始终在$v_x = u\cos\theta$处水平。任何偏离都表示水平加速度（空气阻力）。

**Common Questions:** Finding range from area, confirming constant horizontal velocity.

---

## 6.4 Vertical Velocity-Time Graph / 竖直速度-时间图

**Axes:** x-axis: Time ($t$ / s), y-axis: Vertical velocity ($v_y$ / m s⁻¹)

**Shape:** Straight line with negative slope (constant downward acceleration).

**Gradient Meaning:** 
- **English:** Gradient = vertical acceleration = $-g$ (or $g$ downward). Constant at $-9.81$ m s⁻².
- **中文:** 斜率 = 竖直加速度 = $-g$（或向下$g$）。恒为$-9.81$ m s⁻²。

**Area Meaning:** 
- **English:** Area under graph = vertical displacement ($y$). Positive area above x-axis = upward displacement. Negative area below x-axis = downward displacement. Net area = 0 when launch and landing heights are equal.
- **中文:** 图线下方面积 = 竖直位移（$y$）。x轴上方正面积 = 向上位移。x轴下方负面积 = 向下位移。当发射和落地高度相等时，净面积 = 0。

**Exam Interpretation:** 
- **English:** The line crosses the x-axis at $t = u\sin\theta/g$ (time to maximum height). The intercept on the y-axis is $u\sin\theta$ (initial vertical velocity). The intercept on the x-axis gives time to peak.
- **中文:** 线与x轴的交点在$t = u\sin\theta/g$（到达最大高度的时间）。y轴截距为$u\sin\theta$（初速度竖直分量）。x轴截距给出到达最高点的时间。

**Common Questions:** Finding acceleration from gradient, finding displacement from area, determining time of flight and maximum height.

> 📷 **IMAGE PROMPT — [PM-06]: Vertical Velocity-Time Graph**
> **English:** A straight line with negative slope on a graph with time (s) on x-axis and vertical velocity (m/s) on y-axis. Line starts at positive value (usinθ) on y-axis, crosses x-axis at t = usinθ/g, continues to negative value (-usinθ) at t = T. Areas above and below x-axis shaded differently. Labels: "vy = usinθ - gt", "Gradient = -g = -9.81 ms⁻²", "Area above = upward displacement", "Area below = downward displacement", "Net area = 0". Style: Scientific graph with shaded areas, clear intercepts labeled. Exam importance: HIGH - most important graph for projectile motion.
> **中文:** 时间（s）为x轴，竖直速度（m/s）为y轴的负斜率直线。线从y轴正起始值（usinθ）开始，在t = usinθ/g处穿过x轴，在t = T处达到负值（-usinθ）。x轴上方和下方的区域用不同颜色填充。标签："vy = usinθ - gt"，"斜率 = -g = -9.81 ms⁻²"，"上方面积 = 向上位移"，"下方面积 = 向下位移"，"净面积 = 0"。风格：带填充区域、清晰标注截距的科学图表。考试重要性：高——抛体运动最重要的图表。

---

## 6.5 Speed-Time Graph / 速率-时间图

**Axes:** x-axis: Time ($t$ / s), y-axis: Speed ($v$ / m s⁻¹)

**Shape:** Curve that decreases to a minimum at the peak (where $v = u\cos\theta$), then increases symmetrically.

**Gradient Meaning:** 
- **English:** Gradient = rate of change of speed (not acceleration, since direction changes).
- **中文:** 斜率 = 速率变化率（不是加速度，因为方向在变化）。

**Area Meaning:** Not directly applicable (area under speed-time graph is distance travelled along path, not displacement).

**Exam Interpretation:** 
- **English:** The minimum speed occurs at maximum height and equals $u\cos\theta$. Speed is symmetric about the peak (same speed at same height going up and down).
- **中文:** 最小速率出现在最大高度处，等于$u\cos\theta$。速率关于最高点对称（上升和下降过程中在同一高度速率相同）。

**Common Questions:** Finding minimum speed, comparing speeds at different points.

---

# 7. Required Diagrams / 必备图表

## 7.1 Complete Projectile Motion Diagram / 完整抛体运动示意图

> 📷 **IMAGE PROMPT — [PM-07]: Complete Projectile Motion with All Parameters**
> **English:** A comprehensive diagram showing a projectile launched from point O at ground level, following a parabolic trajectory to landing point Q. Include: Initial velocity vector u at angle θ from horizontal, resolved into ux = ucosθ (horizontal arrow) and uy = usinθ (vertical arrow). At the peak point P, show velocity vector v = ucosθ (horizontal only). At landing point Q, show velocity vector u at angle -θ below horizontal. Label: Range R (horizontal distance O to Q), Maximum Height H (vertical distance from ground to P), Time of Flight T. Add dashed vertical line through P showing symmetry. Include coordinate axes (x horizontal, y vertical) with origin at O. Add small time markers (t = 0, t = T/2, t = T) along the path. Style: Professional physics textbook diagram, clean lines, vector arrows with arrowheads, all labels in clear font. Use blue for horizontal components, red for vertical components, black for resultant vectors. Exam importance: ESSENTIAL - must be able to draw and label this from memory.
> **中文:** 综合示意图，显示从地面O点发射的抛体，沿抛物线轨迹运动到落地点Q。包括：初速度矢量u与水平方向成角度θ，分解为ux = ucosθ（水平箭头）和uy = usinθ（竖直箭头）。在最高点P，显示速度矢量v = ucosθ（仅水平方向）。在落地点Q，显示速度矢量u与水平方向成角度-θ（向下）。标注：射程R（O到Q的水平距离），最大高度H（地面到P的竖直距离），飞行时间T。通过P点画垂直虚线显示对称性。包括坐标轴（x水平，y竖直），原点在O。沿路径添加时间标记（t = 0，t = T/2，t = T）。风格：专业物理教科书插图，线条清晰，矢量箭头带箭头，所有标签字体清晰。水平分量用蓝色，竖直分量用红色，合矢量用黑色。考试重要性：必备——必须能凭记忆画出并标注。

---

## 7.2 Velocity Vector Diagram at Multiple Points / 多点速度矢量图

> 📷 **IMAGE PROMPT — [PM-08]: Velocity Vectors Along Projectile Path**
> **English:** A parabolic trajectory with 5 equally spaced points along the path (including launch, two points on ascent, peak, two points on descent, landing). At each point, draw the velocity vector as an arrow tangent to the path. Show the horizontal component (constant length) and vertical component (decreasing to zero at peak, then increasing downward) as dashed arrows. At launch: long arrow at angle θ. At peak: horizontal arrow only (shortest). At landing: long arrow at angle -θ (same length as launch). Include a separate vector addition diagram showing v = vx + vy at one point. Labels: "Velocity tangent to path", "vx constant", "vy changes", "v = √(vx² + vy²)". Style: Vector diagram with clear component resolution, different colors for components. Exam importance: HIGH - helps understand velocity changes.
> **中文:** 抛物线轨迹上5个等距点（包括发射点、上升段两点、最高点、下降段两点、落地点）。在每个点，画出与路径相切的速度矢量箭头。用虚线箭头显示水平分量（长度恒定）和竖直分量（在最高点减小到零，然后向下增加）。在发射点：与水平方向成角度θ的长箭头。在最高点：仅水平箭头（最短）。在落地点：与水平方向成角度-θ的长箭头（与发射点长度相同）。在一点处包含单独的矢量加法图，显示v = vx + vy。标签："速度与路径相切"，"vx恒定"，"vy变化"，"v = √(vx² + vy²)"。风格：带清晰分量分解的矢量图，不同分量用不同颜色。考试重要性：高——有助于理解速度变化。

---

## 7.3 Graph Set for Projectile Motion / 抛体运动图组

> 📷 **IMAGE PROMPT — [PM-09]: Four-Graph Set for Projectile Motion**
> **English:** A 2×2 grid of four graphs for the same projectile motion (θ = 60°, u = 20 m/s). Top-left: Horizontal displacement vs time (straight line). Top-right: Vertical displacement vs time (parabola opening downward). Bottom-left: Horizontal velocity vs time (horizontal line at ucosθ). Bottom-right: Vertical velocity vs time (straight line with negative slope, crossing zero at t = usinθ/g). All graphs share the same time axis scale from t=0 to t=T. Key values labeled on axes. Style: Clean scientific graphs with gridlines, consistent scaling, professional layout. Exam importance: HIGH - understanding the relationship between these graphs is crucial.
> **中文:** 同一抛体运动（θ = 60°，u = 20 m/s）的2×2四图网格。左上：水平位移-时间图（直线）。右上：竖直位移-时间图（开口向下抛物线）。左下：水平速度-时间图（在ucosθ处的水平线）。右下：竖直速度-时间图（负斜率直线，在t = usinθ/g处过零）。所有图共享从t=0到t=T的时间轴刻度。轴上标注关键值。风格：带网格线的清晰科学图表，比例一致，专业布局。考试重要性：高——理解这些图之间的关系至关重要。

---

# 8. Worked Examples / 典型例题

## Example 1: Horizontal Projection from a Height / 从高处水平抛射

### Question / 题目
**English:** A ball is thrown horizontally from the top of a cliff 45 m high with a speed of 12 m s⁻¹. Calculate:
(a) The time taken for the ball to reach the sea.
(b) The horizontal distance from the base of the cliff where the ball lands.
(c) The speed of the ball just before it hits the sea.
(Take $g = 9.81 \text{ m s}^{-2}$)

**中文:** 一个球从45米高的悬崖顶部以12 m s⁻¹的速度水平抛出。计算：
(a) 球到达海面所需的时间。
(b) 球落地点距悬崖底部的水平距离。
(c) 球即将撞击海面时的速率。
（取$g = 9.81 \text{ m s}^{-2}$）

### Image Prompt / 图片提示
> 📷 **IMAGE PROMPT — [PM-10]: Horizontal Projection from Cliff**
> **English:** A diagram showing a cliff of height 45 m. A ball is shown at the top edge being thrown horizontally to the right with velocity 12 m/s. The parabolic path is shown from the cliff top to the sea surface. Labels: "h = 45 m", "u = 12 m/s", "θ = 0°", "ux = 12 m/s", "uy = 0". The landing point is marked on the sea surface with horizontal distance R from the cliff base. Style: Simple clear diagram, side view. Exam importance: HIGH - standard horizontal projection problem.
> **中文:** 显示高度45米的悬崖示意图。球在顶部边缘以12 m/s的速度水平向右抛出。显示从悬崖顶部到海面的抛物线路径。标签："h = 45 m"，"u = 12 m/s"，"θ = 0°"，"ux = 12 m/s"，"uy = 0"。落地点在海面上标记，距悬崖底部的水平距离为R。风格：简单清晰的侧视图。考试重要性：高——标准水平抛射问题。

### Solution / 解答

**Step 1: Identify known quantities and choose sign convention**
- **English:** Take downward as positive for vertical motion.
  $u_y = 0$ (horizontal projection), $s_y = +45$ m (downward displacement), $a_y = +g = 9.81$ m s⁻²
  $u_x = 12$ m s⁻¹ (constant)
- **中文:** 取向下为竖直运动的正方向。
  $u_y = 0$（水平抛射），$s_y = +45$ m（向下位移），$a_y = +g = 9.81$ m s⁻²
  $u_x = 12$ m s⁻¹（恒定）

**Step 2: (a) Find time of flight using vertical motion**
- **English:** Use $s = u_yt + \frac{1}{2}a_yt^2$
  $45 = 0 \times t + \frac{1}{2} \times 9.81 \times t^2$
  $45 = 4.905t^2$
  $t^2 = \frac{45}{4.905} = 9.174$
  $t = \sqrt{9.174} = 3.03$ s
- **中文:** 使用$s = u_yt + \frac{1}{2}a_yt^2$
  $45 = 0 \times t + \frac{1}{2} \times 9.81 \times t^2$
  $45 = 4.905t^2$
  $t^2 = \frac{45}{4.905} = 9.174$
  $t = \sqrt{9.174} = 3.03$ s

**Step 3: (b) Find horizontal range**
- **English:** Use $x = u_x \times t$ (constant horizontal velocity)
  $x = 12 \times 3.03 = 36.4$ m
- **中文:** 使用$x = u_x \times t$（水平速度恒定）
  $x = 12 \times 3.03 = 36.4$ m

**Step 4: (c) Find speed just before impact**
- **English:** First find vertical velocity at impact: $v_y = u_y + a_yt = 0 + 9.81 \times 3.03 = 29.7$ m s⁻¹ (downward)
  Horizontal velocity remains: $v_x = u_x = 12$ m s⁻¹
  Speed: $v = \sqrt{v_x^2 + v_y^2} = \sqrt{12^2 + 29.7^2} = \sqrt{144 + 882.1} = \sqrt{1026.1} = 32.0$ m s⁻¹
- **中文:** 先求撞击时的竖直速度：$v_y = u_y + a_yt = 0 + 9.81 \times 3.03 = 29.7$ m s⁻¹（向下）
  水平速度保持不变：$v_x = u_x = 12$ m s⁻¹
  速率：$v = \sqrt{v_x^2 + v_y^2} = \sqrt{12^2 + 29.7^2} = \sqrt{144 + 882.1} = \sqrt{1026.1} = 32.0$ m s⁻¹

### Final Answer / 最终答案
**English:**
(a) Time of flight = 3.03 s
(b) Horizontal range = 36.4 m
(c) Speed at impact = 32.0 m s⁻¹

**中文:**
(a) 飞行时间 = 3.03 s
(b) 水平射程 = 36.4 m
(c) 撞击速率 = 32.0 m s⁻¹

### Examiner Notes / 考官点评
**English:** 
- Common mistake: Using $s = -45$ m with upward positive convention without being consistent.
- Always state your sign convention clearly.
- For horizontal projection, $u_y = 0$ simplifies calculations significantly.
- Part (c) requires combining components using Pythagoras, not simply adding velocities.
- Marks are awarded for: correct equation selection (1), correct substitution (1), correct calculation (1), correct units (1).

**中文:**
- 常见错误：使用向上为正的约定时，$s = -45$ m但符号不一致。
- 始终明确说明你的符号约定。
- 对于水平抛射，$u_y = 0$大大简化了计算。
- 第(c)部分需要使用勾股定理合成分量，而不是简单相加。
- 得分点：正确选择方程（1分），正确代入（1分），正确计算（1分），正确单位（1分）。

---

## Example 2: Projectile Launched at an Angle / 以一定角度发射的抛体

### Question / 题目
**English:** A projectile is launched from ground level with an initial velocity of 25 m s⁻¹ at an angle of 40° above the horizontal. Calculate:
(a) The maximum height reached.
(b) The time of flight.
(c) The horizontal range.
(d) The velocity (magnitude and direction) after 2.0 seconds.
(Take $g = 9.81 \text{ m s}^{-2}$)

**中文:** 一个抛体从地面以25 m s⁻¹的初速度、与水平方向成40°角发射。计算：
(a) 达到的最大高度。
(b) 飞行时间。
(c) 水平射程。
(d) 2.0秒后的速度（大小和方向）。
（取$g = 9.81 \text{ m s}^{-2}$）

### Image Prompt / 图片提示
> 📷 **IMAGE PROMPT — [PM-11]: Angled Projection with All Parameters**
> **English:** A parabolic trajectory from ground to ground. Initial velocity vector u = 25 m/s at θ = 40° shown at launch point. Components ux = 25cos40° and uy = 25sin40° shown as dashed arrows. Peak point P labeled with H. Landing point Q labeled with R. A point at t = 2.0 s marked on the ascending part of the path with velocity vector v. Labels: "u = 25 m/s", "θ = 40°", "H = ?", "R = ?", "T = ?", "t = 2.0 s". Style: Clean physics diagram with vector resolution. Exam importance: HIGH - standard angled projection problem.
> **中文:** 从地面到地面的抛物线轨迹。在发射点显示初速度矢量u = 25 m/s，与水平方向成θ = 40°。用虚线箭头显示分量ux = 25cos40°和uy = 25sin40°。最高点P标注H。落地点Q标注R。在路径上升段t = 2.0 s处标记一点，显示速度矢量v。标签："u = 25 m/s"，"θ = 40°"，"H = ?"，"R = ?"，"T = ?"，"t = 2.0 s"。风格：带矢量分解的清晰物理图。考试重要性：高——标准角度抛射问题。

### Solution / 解答

**Step 1: Resolve initial velocity**
- **English:** Take upward as positive.
  $u_x = u\cos\theta = 25\cos40^\circ = 25 \times 0.7660 = 19.2$ m s⁻¹
  $u_y = u\sin\theta = 25\sin40^\circ = 25 \times 0.6428 = 16.1$ m s⁻¹
  $a_x = 0$, $a_y = -g = -9.81$ m s⁻²
- **中文:** 取向上为正。
  $u_x = u\cos\theta = 25\cos40^\circ = 25 \times 0.7660 = 19.2$ m s⁻¹
  $u_y = u\sin\theta = 25\sin40^\circ = 25 \times 0.6428 = 16.1$ m s⁻¹
  $a_x = 0$, $a_y = -g = -9.81$ m s⁻²

**Step 2: (a) Maximum height**
- **English:** At maximum height, $v_y = 0$. Use $v_y^2 = u_y^2 + 2a_ys$:
  $0 = (16.1)^2 + 2(-9.81)H$
  $0 = 259.2 - 19.62H$
  $H = \frac{259.2}{19.62} = 13.2$ m
- **中文:** 在最大高度处，$v_y = 0$。使用$v_y^2 = u_y^2 + 2a_ys$：
  $0 = (16.1)^2 + 2(-9.81)H$
  $0 = 259.2 - 19.62H$
  $H = \frac{259.2}{19.62} = 13.2$ m

**Step 3: (b) Time of flight**
- **English:** Use $s = u_yt + \frac{1}{2}a_yt^2$ with $s = 0$ (returns to ground):
  $0 = 16.1T + \frac{1}{2}(-9.81)T^2$
  $0 = 16.1T - 4.905T^2$
  $T(16.1 - 4.905T) = 0$
  $T = 0$ (launch) or $T = \frac{16.1}{4.905} = 3.28$ s
- **中文:** 使用$s = u_yt + \frac{1}{2}a_yt^2$，其中$s = 0$（回到地面）：
  $0 = 16.1T + \frac{1}{2}(-9.81)T^2$
  $0 = 16.1T - 4.905T^2$
  $T(16.1 - 4.905T) = 0$
  $T = 0$（发射时刻）或$T = \frac{16.1}{4.905} = 3.28$ s

**Step 4: (c) Horizontal range**
- **English:** $R = u_x \times T = 19.2 \times 3.28 = 63.0$ m
  Alternatively: $R = \frac{u^2\sin 2\theta}{g} = \frac{25^2 \times \sin 80^\circ}{9.81} = \frac{625 \times 0.9848}{9.81} = 62.8$ m (slight difference due to rounding)
- **中文:** $R = u_x \times T = 19.2 \times 3.28 = 63.0$ m
  或者：$R = \frac{u^2\sin 2\theta}{g} = \frac{25^2 \times \sin 80^\circ}{9.81} = \frac{625 \times 0.9848}{9.81} = 62.8$ m（因四舍五入略有差异）

**Step 5: (d) Velocity after 2.0 seconds**
- **English:** 
  $v_x = u_x = 19.2$ m s⁻¹ (constant)
  $v_y = u_y + a_yt = 16.1 + (-9.81)(2.0) = 16.1 - 19.62 = -3.52$ m s⁻¹ (negative means downward)
  
  Magnitude: $v = \sqrt{v_x^2 + v_y^2} = \sqrt{19.2^2 + (-3.52)^2} = \sqrt{368.6 + 12.4} = \sqrt{381.0} = 19.5$ m s⁻¹
  
  Direction: $\phi = \tan^{-1}\left(\frac{|v_y|}{v_x}\right) = \tan^{-1}\left(\frac{3.52}{19.2}\right) = \tan^{-1}(0.1833) = 10.4^\circ$ below the horizontal
- **中文:**
  $v_x = u_x = 19.2$ m s⁻¹（恒定）
  $v_y = u_y + a_yt = 16.1 + (-9.81)(2.0) = 16.1 - 19.62 = -3.52$ m s⁻¹（负值表示向下）
  
  大小：$v = \sqrt{v_x^2 + v_y^2} = \sqrt{19.2^2 + (-3.52)^2} = \sqrt{368.6 + 12.4} = \sqrt{381.0} = 19.5$ m s⁻¹
  
  方向：$\phi = \tan^{-1}\left(\frac{|v_y|}{v_x}\right) = \tan^{-1}\left(\frac{3.52}{19.2}\right) = \tan^{-1}(0.1833) = 10.4^\circ$ 水平向下

### Final Answer / 最终答案
**English:**
(a) Maximum height = 13.2 m
(b) Time of flight = 3.28 s
(c) Horizontal range = 63.0 m (or 62.8 m using formula)
(d) Velocity at t = 2.0 s: 19.5 m s⁻¹ at 10.4° below the horizontal

**中文:**
(a) 最大高度 = 13.2 m
(b) 飞行时间 = 3.28 s
(c) 水平射程 = 63.0 m（或使用公式得62.8 m）
(d) t = 2.0 s时的速度：19.5 m s⁻¹，方向水平向下10.4°

### Examiner Notes / 考官点评
**English:**
- Always resolve components first — this is the most common place to lose marks.
- For maximum height, use $v_y^2 = u_y^2 + 2a_ys$ (not $s = u_yt + \frac{1}{2}at^2$ which requires knowing time).
- The negative sign in $v_y$ after 2.0 s indicates the projectile is on its way down.
- Direction must be stated relative to the horizontal (e.g., "below the horizontal").
- Using the formula $R = u^2\sin 2\theta/g$ is faster but only works for equal launch and landing heights.
- Mark scheme: Each part typically worth 2-3 marks. Show all working for partial credit.

**中文:**
- 始终先分解分量——这是最常见的失分点。
- 求最大高度使用$v_y^2 = u_y^2 + 2a_ys$（而不是$s = u_yt + \frac{1}{2}at^2$，后者需要知道时间）。
- 2.0秒后$v_y$为负表示抛体正在下降。
- 方向必须相对于水平方向说明（例如"水平向下"）。
- 使用公式$R = u^2\sin 2\theta/g$更快，但仅适用于发射和落地高度相等的情况。
- 评分标准：每部分通常2-3分。展示所有解题过程以获得步骤分。

---

# 9. Past Paper Question Types / 历年真题题型

| Question Type / 题型 | Frequency / 频率 | Difficulty / 难度 | Past Paper References / 真题索引 |
|---|---|---|---|
| Horizontal projection from height (find time, range, impact speed) | Very High / 非常高 | Medium / 中等 | 📝 *待填入* |
| Angled projection (find H, T, R) | Very High / 非常高 | Medium-Hard / 中高 | 📝 *待填入* |
| Derivation of trajectory equation | Medium / 中等 | Hard / 高 | 📝 *待填入* |
| Graph interpretation (v-t, s-t graphs) | High / 高 | Medium / 中等 | 📝 *待填入* |
| Velocity vector at a point (magnitude and direction) | High / 高 | Medium / 中等 | 📝 *待填入* |
| Projectile clearing an obstacle (trajectory equation) | Medium / 中等 | Hard / 高 | 📝 *待填入* |
| Comparison of two projectiles (different angles/speeds) | Medium / 中等 | Medium-Hard / 中高 | 📝 *待填入* |
| Experimental determination of initial velocity | Low-Medium / 低中 | Medium / 中等 | 📝 *待填入* |
| Projectile launched from and landing at different heights | Medium / 中等 | Hard / 高 | 📝 *待填入* |
| Multiple choice: basic concepts and definitions | High / 高 | Easy / 低 | 📝 *待填入* |

> 📝 **题库整理中 / Question Bank Under Construction:** 具体真题索引正在整理中。建议参考CAIE 9702/22, 9702/23, 9702/12及Edexcel WPH11/01近年试卷中的运动学题目。所有抛体运动题目均适用本节内容。

**Common Command Words / 常见指令词:**
- **Calculate / 计算:** Use equations to find numerical value
- **Derive / 推导:** Show step-by-step mathematical derivation
- **Sketch / 画草图:** Draw approximate shape with key features labeled
- **Determine / 确定:** Find value using given data or graph
- **Explain / 解释:** Give reasons with physics principles
- **Compare / 比较:** State similarities and differences
- **State / 写出:** Give answer without explanation
- **Show that / 证明:** Demonstrate that a given result follows from data

---

# 10. Practical Skills Connections / 实验技能链接

**English:** Projectile motion practical work connects to several experimental skills tested in CAIE Paper 3/5 and Edexcel Unit 3/6:

1. **Measurement Techniques:**
   - Using a stopwatch to measure time of flight (typical uncertainty ±0.1 s)
   - Using a meter ruler or measuring tape for range (typical uncertainty ±0.01 m)
   - Using a protractor to measure launch angle (typical uncertainty ±1°)
   - Using a video camera with frame-by-frame analysis for more accurate measurements

2. **Experimental Design:**
   - Horizontal projection: Release ball from measured height, measure range
   - Angled projection: Use a projectile launcher or ramp at measured angle
   - Determining initial velocity from range and time measurements
   - Investigating factors affecting range (angle, initial speed, height)

3. **Data Analysis:**
   - Plotting range vs angle graph to find optimum angle (should be 45°)
   - Plotting range vs $u^2$ graph to verify $R \propto u^2$
   - Using $y$-$x^2$ graph to verify parabolic trajectory
   - Calculating $g$ from experimental data

4. **Uncertainties and Errors:**
   - Air resistance causes systematic error (actual range < theoretical range)
   - Timing errors (reaction time) for manual measurements
   - Parallax error in reading range measurements
   - Uncertainty in angle measurement

5. **Typical Experiments:**
   - **CAIE Paper 3:** Measuring range of horizontal projection from different heights
   - **CAIE Paper 5:** Designing experiment to investigate relationship between range and launch angle
   - **Edexcel Unit 3:** Using light gates to measure time of flight more accurately
   - **Edexcel Unit 6:** Investigating projectile motion using video analysis software

**中文:** 抛体运动实验与CAIE Paper 3/5和Edexcel Unit 3/6中考查的实验技能相关：

1. **测量技术：**
   - 使用秒表测量飞行时间（典型不确定度±0.1 s）
   - 使用米尺或卷尺测量射程（典型不确定度±0.01 m）
   - 使用量角器测量发射角度（典型不确定度±1°）
   - 使用摄像机逐帧分析以获得更精确的测量

2. **实验设计：**
   - 水平抛射：从测量高度释放球，测量射程
   - 角度抛射：使用抛体发射器或斜面以测量角度发射
   - 从射程和时间测量确定初速度
   - 研究影响射程的因素（角度、初速度、高度）

3. **数据分析：**
   - 绘制射程-角度图以找到最佳角度（应为45°）
   - 绘制射程-$u^2$图以验证$R \propto u^2$
   - 使用$y$-$x^2$图验证抛物线轨迹
   - 从实验数据计算$g$

4. **不确定度和误差：**
   - 空气阻力导致系统误差（实际射程 < 理论射程）
   - 手动测量的计时误差（反应时间）
   - 读取射程测量值的视差误差
   - 角度测量的不确定度

5. **典型实验：**
   - **CAIE Paper 3:** 测量不同高度水平抛射的射程
   - **CAIE Paper 5:** 设计实验研究射程与发射角度的关系
   - **Edexcel Unit 3:** 使用光门更精确地测量飞行时间
   - **Edexcel Unit 6:** 使用视频分析软件研究抛体运动

> 📋 **CIE Only:** Paper 3 often includes an experiment measuring range for horizontal projection from different heights. Plot $R$ against $\sqrt{h}$ to get a straight line through origin (gradient = $u\sqrt{2/g}$).
> 
> 📋 **Edexcel Only:** Unit 3 may involve using a projectile launcher with light gates to measure initial velocity. Unit 6 may require designing an experiment to investigate the effect of launch angle on range.

---

# 11. Concept Map / 概念图谱

```mermaid
graph TD
    %% Main Topic
    PM[Projectile Motion / 抛体运动]
    
    %% Prerequisites
    SV[Scalars and Vectors / 标量与矢量]
    SUVAT[Equations of Motion (SUVAT) / 运动学方程]
    G[Gravitational Acceleration g / 重力加速度]
    
    %% Core Concepts
    IND[Independence of Motions / 运动独立性]
    RES[Vector Resolution / 矢量分解]
    TRAJ[Trajectory / 轨迹]
    
    %% Key Parameters
    TOF[Time of Flight / 飞行时间]
    RNG[Range / 射程]
    MH[Maximum Height / 最大高度]
    VEL[Velocity at Any Point / 任意点速度]
    
    %% Sub-topics (Leaf Nodes)
    HVC[Horizontal and Vertical Components / 水平和竖直分量]
    TFR[Time of Flight and Range / 飞行时间和射程]
    MAXH[Maximum Height / 最大高度]
    PMG[Projectile Motion Graphs / 抛体运动图像]
    
    %% Equations
    EQ1[u_x = ucosθ, u_y = usinθ]
    EQ2[T = 2usinθ/g]
    EQ3[R = u²sin2θ/g]
    EQ4[H = u²sin²θ/2g]
    EQ5[y = xtanθ - gx²/2u²cos²θ]
    
    %% Related Topics
    NL[Newton's Laws of Motion / 牛顿运动定律]
    EM[Energy Methods / 能量方法]
    
    %% Connections
    SV --> RES
    SUVAT --> IND
    G --> IND
    
    RES --> HVC
    IND --> HVC
    
    HVC --> TOF
    HVC --> RNG
    HVC --> MH
    HVC --> VEL
    
    TOF --> TFR
    RNG --> TFR
    MH --> MAXH
    
    TOF --> EQ2
    RNG --> EQ3
    MH --> EQ4
    HVC --> EQ1
    TRAJ --> EQ5
    
    PM --> IND
    PM --> RES
    PM --> TRAJ
    PM --> TFR
    PM --> MAXH
    PM --> PMG
    
    PM --> NL
    PM --> EM
    
    %% Styling
    classDef main fill:#e74c3c,color:#fff,stroke:#c0392b
    classDef prereq fill:#3498db,color:#fff,stroke:#2980b9
    classDef concept fill:#2ecc71,color:#fff,stroke:#27ae60
    classDef param fill:#f39c12,color:#fff,stroke:#e67e22
    classDef leaf fill:#9b59b6,color:#fff,stroke:#8e44ad
    classDef eq fill:#1abc9c,color:#fff,stroke:#16a085
    classDef related fill:#95a5a6,color:#fff,stroke:#7f8c8d
    
    class PM main
    class SV,SUVAT,G prereq
    class IND,RES,TRAJ concept
    class TOF,RNG,MH,VEL param
    class HVC,TFR,MAXH,PMG leaf
    class EQ1,EQ2,EQ3,EQ4,EQ5 eq
    class NL,EM related
```

---

# 12. Examiner Insights / 考官洞察

**English:**

### Most Tested Ideas (CAIE 9702 + Edexcel IAL)

1. **Horizontal projection from height** — appears in nearly every exam session. Candidates must find time using vertical motion ($s = \frac{1}{2}gt^2$) then range using horizontal motion ($x = ut$).

2. **Resolving initial velocity** — the single most important skill. Marks are often lost because candidates fail to correctly calculate $u\cos\theta$ and $u\sin\theta$.

3. **Maximum height calculation** — using $v_y^2 = u_y^2 + 2a_ys$ with $v_y = 0$ at the peak. Common error: using $v_y = u_y + a_yt$ without knowing time.

4. **Graph interpretation** — especially the $v_y$-$t$ graph. Candidates must understand gradient = $-g$ and area = displacement.

5. **Equation of trajectory derivation** — frequently tested in CAIE. Must show clear algebraic steps.

### Mark Scheme Wording / Key Phrases

- "Resolve the initial velocity into horizontal and vertical components" (1 mark)
- "Use appropriate equation of motion for vertical motion" (1 mark)
- "State that horizontal velocity is constant" (1 mark)
- "Calculate time of flight from vertical motion" (1 mark)
- "Calculate range using horizontal velocity × time" (1 mark)
- "Use Pythagoras theorem to find resultant velocity" (1 mark)
- "State direction relative to horizontal" (1 mark)

### Common Reasons for Lost Marks

1. **Sign convention errors** — mixing up positive and negative directions
2. **Using wrong equation** — e.g., using $s = ut + \frac{1}{2}at^2$ when $v^2 = u^2 + 2as$ is needed
3. **Not resolving components** — treating initial velocity as purely horizontal or vertical
4. **Calculator mode errors** — using radians instead of degrees
5. **Incomplete answers** — giving magnitude without direction for velocity
6. **Unit errors** — forgetting to include units or using incorrect units
7. **Premature rounding** — rounding intermediate values leads to inaccurate final answers

### High-Scoring Answer Structure

1. **Diagram** — draw and label all known quantities
2. **Resolution** — write $u_x = u\cos\theta$, $u_y = u\sin\theta$ with values
3. **SUVAT lists** — separate lists for horizontal and vertical motion
4. **Equation selection** — state which equation you're using and why
5. **Substitution** — show substitution with units
6. **Calculation** — show numerical working
7. **Final answer** — with correct units and direction where applicable

**中文:**

### 最常考的知识点（CAIE 9702 + Edexcel IAL）

1. **从高处水平抛射** — 几乎每次考试都出现。考生必须通过竖直运动求时间（$s = \frac{1}{2}gt^2$），然后通过水平运动求射程（$x = ut$）。

2. **分解初速度** — 最重要的单一技能。常因考生未能正确计算$u\cos\theta$和$u\sin\theta$而失分。

3. **最大高度计算** — 使用$v_y^2 = u_y^2 + 2a_ys$，在最高点$v_y = 0$。常见错误：在不知道时间的情况下使用$v_y = u_y + a_yt$。

4. **图像解读** — 特别是$v_y$-$t$图。考生必须理解斜率 = $-g$，面积 = 位移。

5. **轨迹方程推导** — CAIE考试中频繁考查。必须展示清晰的代数步骤。

### 评分方案关键词

- "将初速度分解为水平和竖直分量"（1分）
- "使用适当的竖直运动方程"（1分）
- "说明水平速度恒定"（1分）
- "从竖直运动计算飞行时间"（1分）
- "使用水平速度×时间计算射程"（1分）
- "使用勾股定理求合速度"（1分）
- "说明相对于水平方向的方向"（1分）

### 常见失分原因

1. **符号约定错误** — 混淆正负方向
2. **使用错误方程** — 例如需要$v^2 = u^2 + 2as$时使用了$s = ut + \frac{1}{2}at^2$
3. **未分解分量** — 将初速度视为纯水平或纯竖直方向
4. **计算器模式错误** — 使用弧度而非角度
5. **答案不完整** — 给出速度大小但未给出方向
6. **单位错误** — 忘记写单位或使用错误单位
7. **过早四舍五入** — 四舍五入中间值导致最终答案不准确

### 高分答题结构

1. **图示** — 画出并标注所有已知量
2. **分解** — 写出$u_x = u\cos\theta$，$u_y = u\sin\theta$并代入数值
3. **SUVAT列表** — 为水平和竖直运动分别列出
4. **选择方程** — 说明使用的方程及原因
5. **代入** — 展示带单位的代入过程
6. **计算** — 展示数值计算步骤
7. **最终答案** — 包含正确单位和方向（如适用）

---

# 13. Quick Revision Sheet / 速查表

| Category / 类别 | Key Points / 要点 |
|---|---|
| **Key Principle / 关键原理** | Horizontal and vertical motions are independent / 水平和竖直运动独立 |
| **Assumptions / 假设条件** | No air resistance, constant $g = 9.81$ m s⁻², Earth's curvature negligible / 无空气阻力，$g$恒定，地球曲率可忽略 |
| **Horizontal Motion / 水平运动** | $a_x = 0$, $v_x = u\cos\theta$ (constant), $x = (u\cos\theta)t$ |
| **Vertical Motion / 竖直运动** | $a_y = -g$, $v_y = u\sin\theta - gt$, $y = (u\sin\theta)t - \frac{1}{2}gt^2$ |
| **Initial Components / 初速度分量** | $u_x = u\cos\theta$, $u_y = u\sin\theta$ |
| **Time of Flight / 飞行时间** | $T = \frac{2u\sin\theta}{g}$ (same height) / 解$s = u_yt + \frac{1}{2}a_yt^2$ (different height) |
| **Range / 射程** | $R = \frac{u^2\sin 2\theta}{g}$ (same height) / $R = u_x \times T$ (always) |
| **Maximum Height / 最大高度** | $H = \frac{u^2\sin^2\theta}{2g}$, reached when $v_y = 0$ |
| **Trajectory Equation / 轨迹方程** | $y = x\tan\theta - \frac{gx^2}{2u^2\cos^2\theta}$ (parabola / 抛物线) |
| **Velocity at Any Time / 任意时刻速度** | $v = \sqrt{v_x^2 + v_y^2}$, $\phi = \tan^{-1}(v_y/v_x)$ |
| **Maximum Range / 最大射程** | $\theta = 45^\circ$, $R_{\text{max}} = u^2/g$ |
| **Complementary Angles / 互补角** | $\theta$ and $90^\circ - \theta$ give same range / 给出相同射程 |
| **At Maximum Height / 在最高点** | $v_y = 0$, $v = v_x = u\cos\theta$, $t = u\sin\theta/g$ |
| **Key Graphs / 关键图表** | $x$-$t$: straight line; $y$-$t$: parabola; $v_x$-$t$: horizontal line; $v_y$-$t$: straight line slope $-g$ |
| **Common Mistakes / 常见错误** | Not resolving, sign errors, calculator mode, premature rounding / 未分解、符号错误、计算器模式、过早四舍五入 |
| **Exam Tips / 考试提示** | Draw diagram, resolve first, separate SUVAT lists, check units / 画图、先分解、分别列SUVAT、检查单位 |

---

# 14. Metadata / 元数据

```yaml
title:
  en: "Projectile Motion"
  cn: "抛体运动"
subject: Physics
syllabus: [CAIE 9702, Edexcel IAL]
cie_ref: "9702/3.1(l-m)"
edexcel_ref: "WPH11/U1:1.13-1.16"
level: AS
node_type: topic_hub
difficulty: advanced
prerequisites:
  - "[[Scalars and Vectors]]"
  - "[[Equations of Motion (SUVAT)]]"
related_topics:
  - "[[Newton's Laws of Motion]]"
sub_topics:
  - "[[Horizontal and Vertical Components]]"
  - "[[Time of Flight and Range]]"
  - "[[Maximum Height]]"
  - "[[Projectile Motion Graphs]]"
formula_count: 8
diagram_count: 11
exam_frequency: "Very High (1-2 questions per paper)"
language: bilingual_en_cn
last_updated: "2025-01"
```

---

> 📷 **IMAGE PROMPT — [PM-COVER]: Topic Cover Image for Projectile Motion**
> **English:** A visually striking composite image showing multiple real-world examples of projectile motion: a basketball player shooting a ball (parabolic arc shown), a fireworks display with multiple colored trajectories, a cannon firing a cannonball, and a diver jumping from a diving board. Overlaid with physics annotations showing velocity vectors, angle labels, and trajectory equations. Style: Modern educational infographic, clean design, physics formulas in white text on dark background. Title: "Projectile Motion / 抛体运动" in large font. Exam importance: HIGH - visual summary of topic applications.
> **中文:** 视觉冲击力强的合成图像，显示多个抛体运动的现实世界例子：篮球运动员投篮（显示抛物线弧）、烟花表演（多条彩色轨迹）、大炮发射炮弹、跳水运动员从跳板跃起。叠加物理标注，显示速度矢量、角度标签和轨迹方程。风格：现代教育信息图，设计简洁，深色背景上白色文字的物理公式。标题："Projectile Motion / 抛体运动"大字体。考试重要性：高——主题应用的视觉总结。