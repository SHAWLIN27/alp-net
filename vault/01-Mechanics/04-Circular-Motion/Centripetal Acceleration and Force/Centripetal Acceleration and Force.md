# 1. Overview / 概述

**English:**
This topic explores the physics of objects moving in circular paths. When an object travels along a circular path at constant speed, its velocity is constantly changing direction. This change in velocity means the object is accelerating, even though its speed remains constant. This acceleration is called **centripetal acceleration**, and it is always directed towards the centre of the circle. The force causing this acceleration is the **centripetal force**, which is not a new type of force but rather the net force acting towards the centre. This topic is fundamental to understanding [[Newton's Laws of Motion]] in two dimensions and forms the basis for analysing [[Circular Orbits]], [[Gravitational Force and Field]], and the motion of charged particles in magnetic fields.

In real-world applications, centripetal force explains why cars can turn corners, how satellites stay in orbit, how a centrifuge separates mixtures, and why rollercoasters can loop-the-loop. It is also crucial in engineering design for roads, railways, and amusement park rides.

For Cambridge 9702 (Topic 14.2 a-d) and Edexcel IAL (WPH14 U4: 5.5-5.9), this is a core A2 topic. Students must be able to derive the formula for centripetal acceleration, apply Newton's Second Law to circular motion, and solve problems involving banked tracks, conical pendulums, and vertical circles. The topic is heavily examined in both multiple-choice and structured questions, often combined with [[Gravitational Force and Field]] for orbital mechanics.

**中文：**
本主题探讨物体沿圆周路径运动的物理学原理。当物体以恒定速度沿圆周路径运动时，其速度方向不断变化。这种速度变化意味着物体在加速，即使其速率保持不变。这种加速度称为**向心加速度**，它始终指向圆心。引起这种加速度的力是**向心力**，它不是一种新型的力，而是指向圆心的合力。本主题是理解二维空间中[[牛顿运动定律]]的基础，也是分析[[圆周轨道]]、[[引力场与引力]]以及带电粒子在磁场中运动的基础。

在实际应用中，向心力解释了汽车如何转弯、卫星如何保持轨道、离心机如何分离混合物以及过山车如何完成回环。它在道路、铁路和游乐园设施的工程设计中至关重要。

对于剑桥 9702（主题 14.2 a-d）和爱德思 IAL（WPH14 U4: 5.5-5.9），这是一个核心的 A2 主题。学生必须能够推导向心加速度公式，将牛顿第二定律应用于圆周运动，并解决涉及倾斜轨道、圆锥摆和竖直圆的问题。该主题在选择题和结构化问题中均有大量考查，通常与[[引力场与引力]]结合用于轨道力学问题。

---

# 2. Syllabus Learning Objectives / 考纲学习目标

**English:**
The following table maps the specific learning objectives from both exam boards. Students should be able to perform all listed tasks.

**中文：**
下表列出了两个考试局的具体学习目标。学生应能完成所有列出的任务。

| CAIE 9702 (Topic 14.2 a-d) | Edexcel IAL (WPH14 U4: 5.5-5.9) |
|----------------------------|----------------------------------|
| (a) Define the radian and express angular displacement in radians. | 5.5 Understand the concept of centripetal acceleration. |
| (b) Understand and use the concept of angular speed. | 5.6 Use the equations for centripetal acceleration: $a = \frac{v^2}{r}$ and $a = \omega^2 r$. |
| (c) Recall and use centripetal acceleration equations $a = \frac{v^2}{r}$ and $a = \omega^2 r$. | 5.7 Understand that a centripetal force is required to maintain circular motion and that it is directed towards the centre of the circle. |
| (d) Recall and use centripetal force equations $F = \frac{mv^2}{r}$ and $F = m\omega^2 r$. | 5.8 Use the equations for centripetal force: $F = \frac{mv^2}{r}$ and $F = m\omega^2 r$. |
| (e) Solve problems involving centripetal force, including banked tracks and conical pendulums. | 5.9 Solve problems involving circular motion, including banked tracks and conical pendulums. |

> 📋 **CIE Only:** CIE explicitly requires defining the radian and angular displacement as part of this topic. Edexcel assumes this knowledge from prior learning.
>
> 📋 **Edexcel Only:** Edexcel explicitly lists "understand the concept of centripetal acceleration" as a separate objective, placing more emphasis on conceptual understanding before formula application.

**Examiner Expectations / 考官期望:**
- **English:** You must be able to derive $a = v^2/r$ from first principles using vector diagrams. You must be able to identify the source of centripetal force in any given scenario (e.g., friction for a car turning, tension for a conical pendulum, gravity for an orbit). You must be able to resolve forces in banked track problems.
- **中文：** 你必须能够使用矢量图从基本原理推导出 $a = v^2/r$。你必须能够在任何给定场景中识别向心力的来源（例如，汽车转弯时的摩擦力、圆锥摆中的张力、轨道中的重力）。你必须能够在倾斜轨道问题中分解力。

---

# 3. Core Definitions / 核心定义

**English:**
The following table provides the official definitions required for both exam boards, along with common student mistakes.

**中文：**
下表提供了两个考试局要求的官方定义，以及学生常见的错误。

| Term (EN/CN) | Definition (EN) | Definition (CN) | Common Mistakes / 常见错误 |
|--------------|-----------------|-----------------|---------------------------|
| **Centripetal Acceleration / 向心加速度** | The acceleration of an object moving in a circle at constant speed. It is always directed towards the centre of the circle. | 物体以恒定速度沿圆周运动时的加速度。它始终指向圆心。 | Confusing it with tangential acceleration. Centripetal acceleration changes only the *direction* of velocity, not its magnitude. |
| **Centripetal Force / 向心力** | The net force acting on an object moving in a circle, directed towards the centre of the circle. It is not a separate force but the resultant of other forces. | 作用在圆周运动物体上的合力，指向圆心。它不是一种独立的力，而是其他力的合力。 | Thinking it is a "new" force like gravity or friction. It is always provided by an existing force (tension, friction, gravity, normal reaction, etc.). |
| **Angular Speed ($\omega$) / 角速度** | The rate of change of angular displacement. $\omega = \frac{\Delta \theta}{\Delta t}$. | 角位移的变化率。$\omega = \frac{\Delta \theta}{\Delta t}$。 | Confusing angular speed with linear speed. They are related by $v = \omega r$. |
| **Radian (rad) / 弧度** | The angle subtended at the centre of a circle by an arc equal in length to the radius. | 在圆心处由长度等于半径的弧所对的角。 | Forgetting that $2\pi$ radians = $360^\circ$. Using degrees in angular speed calculations without converting. |
| **Period ($T$) / 周期** | The time taken for one complete revolution. | 完成一次完整旋转所需的时间。 | Confusing period with frequency ($f = 1/T$). |
| **Frequency ($f$) / 频率** | The number of complete revolutions per unit time. | 单位时间内完成的完整旋转次数。 | Confusing frequency with angular speed ($\omega = 2\pi f$). |

---

# 4. Key Concepts Explained / 关键概念详解

## 4.1 Centripetal Acceleration / 向心加速度

### Explanation / 解释
**English:**
Consider an object moving in a circle of radius $r$ with constant speed $v$. At any instant, its velocity vector is tangential to the circle. After a small time interval $\Delta t$, the object has moved through a small angle $\Delta \theta$, and its velocity vector has rotated by the same angle. The change in velocity $\Delta \vec{v}$ is found by vector subtraction: $\Delta \vec{v} = \vec{v}_2 - \vec{v}_1$. For small angles, the magnitude of $\Delta \vec{v}$ is approximately $v \Delta \theta$. The acceleration is $a = \frac{\Delta v}{\Delta t} = \frac{v \Delta \theta}{\Delta t} = v \omega$. Since $\omega = v/r$, we get $a = v^2/r$. The direction of $\Delta \vec{v}$ (and hence the acceleration) is towards the centre of the circle. This is [[Centripetal Acceleration Formula]].

**中文：**
考虑一个以恒定速率 $v$ 在半径为 $r$ 的圆周上运动的物体。在任何瞬间，其速度矢量与圆相切。经过一小段时间 $\Delta t$ 后，物体移动了一个小角度 $\Delta \theta$，其速度矢量也旋转了相同的角度。速度的变化 $\Delta \vec{v}$ 通过矢量减法求得：$\Delta \vec{v} = \vec{v}_2 - \vec{v}_1$。对于小角度，$\Delta \vec{v}$ 的大小近似为 $v \Delta \theta$。加速度为 $a = \frac{\Delta v}{\Delta t} = \frac{v \Delta \theta}{\Delta t} = v \omega$。由于 $\omega = v/r$，我们得到 $a = v^2/r$。$\Delta \vec{v}$ 的方向（因此也是加速度的方向）指向圆心。这就是[[向心加速度公式]]。

### Physical Meaning / 物理意义
**English:**
Centripetal acceleration is the rate at which the velocity vector changes direction. It does not change the object's speed. A larger centripetal acceleration means the direction is changing more rapidly (tighter turn). For a given speed, a smaller radius requires a larger centripetal acceleration.

**中文：**
向心加速度是速度矢量方向变化的速率。它不改变物体的速率。向心加速度越大，意味着方向变化越快（转弯越急）。对于给定的速率，半径越小，所需的向心加速度越大。

### Common Misconceptions / 常见误区
- **English:** "The object is accelerating, so its speed must be increasing." → No, acceleration can change direction without changing speed.
- **English:** "Centripetal acceleration is a force." → No, it is an acceleration. The force causing it is centripetal force.
- **中文：** "物体在加速，所以它的速率一定在增加。" → 不对，加速度可以改变方向而不改变速率。
- **中文：** "向心加速度是一种力。" → 不对，它是一种加速度。引起它的力是向心力。

### Exam Tips / 考试提示
**English:**
- Always draw a vector diagram to derive $a = v^2/r$ if asked.
- Remember that centripetal acceleration is always perpendicular to the velocity.
- For vertical circles, the centripetal acceleration is not constant because the speed changes due to gravity.

**中文：**
- 如果被要求，务必画矢量图来推导 $a = v^2/r$。
- 记住向心加速度始终垂直于速度。
- 对于竖直圆，向心加速度不是恒定的，因为重力会改变速率。

> 📷 **IMAGE PROMPT — CP01: Vector Diagram for Centripetal Acceleration Derivation**
>
> A diagram showing a circle of radius r. Two velocity vectors v1 and v2 are drawn tangential to the circle at two nearby points separated by angle Δθ. The vector difference Δv = v2 - v1 is shown pointing towards the centre of the circle. Labels: r, v1, v2, Δθ, Δv. Clean white background, educational style, 2D vector diagram.

---

## 4.2 Centripetal Force / 向心力

### Explanation / 解释
**English:**
From [[Newton's Laws of Motion|Newton's Second Law]], if an object has centripetal acceleration $a$, there must be a net force $F = ma$ acting in the same direction. This net force is the centripetal force $F = \frac{mv^2}{r} = m\omega^2 r$. The centripetal force is always directed towards the centre of the circle. It is not a new force; it is the resultant of real forces such as tension, friction, gravity, or the normal reaction. For example:
- A car turning on a flat road: friction provides the centripetal force.
- A satellite in orbit: gravity provides the centripetal force.
- A ball on a string: tension provides the centripetal force.
- A car on a banked track: the horizontal component of the normal reaction provides the centripetal force.

This is the core of [[Centripetal Force]].

**中文：**
根据[[牛顿运动定律|牛顿第二定律]]，如果物体具有向心加速度 $a$，则必须有一个合力 $F = ma$ 作用在同一方向上。这个合力就是向心力 $F = \frac{mv^2}{r} = m\omega^2 r$。向心力始终指向圆心。它不是一种新的力；它是真实力（如张力、摩擦力、重力或法向反作用力）的合力。例如：
- 在平直道路上转弯的汽车：摩擦力提供向心力。
- 轨道上的卫星：重力提供向心力。
- 绳子上的球：张力提供向心力。
- 倾斜轨道上的汽车：法向反作用力的水平分量提供向心力。

这是[[向心力]]的核心。

### Physical Meaning / 物理意义
**English:**
Centripetal force is what "pulls" an object into a circular path. Without it, the object would continue in a straight line ([[Newton's Laws of Motion|Newton's First Law]]). The larger the centripetal force, the tighter the turn (smaller radius) for a given speed.

**中文：**
向心力是将物体"拉"入圆周路径的力。没有它，物体会沿直线运动（[[牛顿运动定律|牛顿第一定律]]）。对于给定的速率，向心力越大，转弯越急（半径越小）。

### Common Misconceptions / 常见误区
- **English:** "Centrifugal force pulls the object outward." → No, centrifugal force is a fictitious force experienced in a rotating reference frame. In an inertial frame, only centripetal force exists.
- **English:** "The centripetal force is an extra force added to the system." → No, it is the net force from existing forces.
- **中文：** "离心力将物体向外拉。" → 不对，离心力是在旋转参考系中感受到的假想力。在惯性系中，只存在向心力。
- **中文：** "向心力是系统额外增加的一种力。" → 不对，它是现有力的合力。

### Exam Tips / 考试提示
**English:**
- Always identify the source of centripetal force before writing equations.
- For banked tracks, resolve the normal reaction into horizontal and vertical components. The horizontal component provides the centripetal force.
- For conical pendulums, resolve tension into horizontal and vertical components. The horizontal component provides the centripetal force.

**中文：**
- 在写方程之前，务必先确定向心力的来源。
- 对于倾斜轨道，将法向反作用力分解为水平和竖直分量。水平分量提供向心力。
- 对于圆锥摆，将张力分解为水平和竖直分量。水平分量提供向心力。

> 📷 **IMAGE PROMPT — CP02: Sources of Centripetal Force**
>
> A split diagram showing four scenarios: (1) Car turning on flat road with friction arrow pointing to centre, (2) Satellite orbiting Earth with gravity arrow pointing to centre, (3) Ball on string with tension arrow pointing to centre, (4) Car on banked track with normal reaction arrow resolved into horizontal component pointing to centre. Each scenario labelled. Clean educational style, 2D.

---

## 4.3 Banked Tracks / 倾斜轨道

### Explanation / 解释
**English:**
A banked track is a curved road or railway track that is tilted at an angle $\theta$ to the horizontal. The banking allows vehicles to turn at higher speeds without relying solely on friction. The centripetal force is provided by the horizontal component of the normal reaction force $N$. For a vehicle moving at the "design speed" $v_0$, no friction is needed. The vertical component of $N$ balances the weight $mg$, and the horizontal component provides the centripetal force:
$$N \cos \theta = mg$$
$$N \sin \theta = \frac{mv_0^2}{r}$$
Dividing gives: $\tan \theta = \frac{v_0^2}{rg}$.
This is a key application in [[Banked Tracks and Conical Pendulum]].

**中文：**
倾斜轨道是弯曲的道路或铁路轨道，与水平面倾斜一个角度 $\theta$。倾斜允许车辆以更高的速度转弯，而不必完全依赖摩擦力。向心力由法向反作用力 $N$ 的水平分量提供。对于以"设计速度" $v_0$ 行驶的车辆，不需要摩擦力。$N$ 的竖直分量平衡重力 $mg$，水平分量提供向心力：
$$N \cos \theta = mg$$
$$N \sin \theta = \frac{mv_0^2}{r}$$
相除得：$\tan \theta = \frac{v_0^2}{rg}$。
这是[[倾斜轨道与圆锥摆]]中的一个关键应用。

### Physical Meaning / 物理意义
**English:**
Banking allows a component of the normal reaction to contribute to the centripetal force, reducing the reliance on friction. This is why race tracks and high-speed railway curves are banked.

**中文：**
倾斜使得法向反作用力的一个分量能够贡献给向心力，从而减少对摩擦力的依赖。这就是为什么赛道和高速铁路弯道是倾斜的。

### Common Misconceptions / 常见误区
- **English:** "The centripetal force is provided by the normal reaction alone." → Only at the design speed. At other speeds, friction also contributes.
- **English:** "The banking angle depends on the mass of the vehicle." → No, $\tan \theta = v^2/(rg)$ is independent of mass.
- **中文：** "向心力仅由法向反作用力提供。" → 仅在设计速度下如此。在其他速度下，摩擦力也会贡献。
- **中文：** "倾斜角度取决于车辆的质量。" → 不对，$\tan \theta = v^2/(rg)$ 与质量无关。

### Exam Tips / 考试提示
**English:**
- Always draw a free-body diagram showing the normal reaction, weight, and (if applicable) friction.
- Resolve forces horizontally and vertically. The horizontal resultant is the centripetal force.
- If friction is involved, remember that friction can act up or down the slope depending on whether the speed is above or below the design speed.

**中文：**
- 务必画出受力图，显示法向反作用力、重力以及（如果适用）摩擦力。
- 水平和竖直分解力。水平合力就是向心力。
- 如果涉及摩擦力，记住摩擦力可以沿斜面向上或向下作用，具体取决于速度是高于还是低于设计速度。

> 📷 **IMAGE PROMPT — CP03: Banked Track Free-Body Diagram**
>
> A car on a banked track inclined at angle θ. Three forces shown: weight mg vertically downward, normal reaction N perpendicular to the track surface, friction f parallel to the track surface (optional). N is resolved into Ncosθ (vertical) and Nsinθ (horizontal towards centre). Labels: θ, mg, N, Ncosθ, Nsinθ, r (radius of curvature). Clean 2D educational diagram.

---

## 4.4 Conical Pendulum / 圆锥摆

### Explanation / 解释
**English:**
A conical pendulum consists of a mass $m$ attached to a string of length $L$, moving in a horizontal circle of radius $r$ such that the string traces out a cone. The string makes an angle $\theta$ with the vertical. The tension $T$ in the string has two components:
- Vertical: $T \cos \theta = mg$ (balances weight)
- Horizontal: $T \sin \theta = \frac{mv^2}{r} = m\omega^2 r$ (provides centripetal force)
Dividing gives: $\tan \theta = \frac{v^2}{rg} = \frac{\omega^2 r}{g}$.
The period $T$ of the conical pendulum is $T = 2\pi \sqrt{\frac{L \cos \theta}{g}}$.
This is another key application in [[Banked Tracks and Conical Pendulum]].

**中文：**
圆锥摆由一个质量为 $m$ 的物体组成，该物体连接在一根长度为 $L$ 的绳子上，在半径为 $r$ 的水平圆周上运动，使得绳子描绘出一个圆锥。绳子与竖直方向成 $\theta$ 角。绳子中的张力 $T$ 有两个分量：
- 竖直方向：$T \cos \theta = mg$（平衡重力）
- 水平方向：$T \sin \theta = \frac{mv^2}{r} = m\omega^2 r$（提供向心力）
相除得：$\tan \theta = \frac{v^2}{rg} = \frac{\omega^2 r}{g}$。
圆锥摆的周期 $T$ 为 $T = 2\pi \sqrt{\frac{L \cos \theta}{g}}$。
这是[[倾斜轨道与圆锥摆]]中的另一个关键应用。

### Physical Meaning / 物理意义
**English:**
The conical pendulum demonstrates how a single force (tension) can be resolved to provide both a balancing force (against weight) and a centripetal force. It is a classic demonstration of circular motion in the laboratory.

**中文：**
圆锥摆展示了单个力（张力）如何被分解，以同时提供平衡力（对抗重力）和向心力。这是实验室中圆周运动的经典演示。

### Common Misconceptions / 常见误区
- **English:** "The centripetal force is the tension in the string." → No, only the horizontal component of tension provides the centripetal force.
- **English:** "The radius of the circle is the length of the string." → No, $r = L \sin \theta$.
- **中文：** "向心力是绳子中的张力。" → 不对，只有张力的水平分量提供向心力。
- **中文：** "圆的半径是绳子的长度。" → 不对，$r = L \sin \theta$。

### Exam Tips / 考试提示
**English:**
- Draw a clear diagram showing the string, the mass, the angle $\theta$, and the radius $r$.
- Resolve tension into components.
- Remember that the vertical acceleration is zero, so $T \cos \theta = mg$.
- The period is independent of the mass.

**中文：**
- 画一个清晰的图，显示绳子、物体、角度 $\theta$ 和半径 $r$。
- 将张力分解为分量。
- 记住竖直加速度为零，所以 $T \cos \theta = mg$。
- 周期与质量无关。

> 📷 **IMAGE PROMPT — CP04: Conical Pendulum Diagram**
>
> A mass m attached to a string of length L, moving in a horizontal circle of radius r. The string makes angle θ with the vertical. Tension T is shown along the string, resolved into Tcosθ (vertical upward) and Tsinθ (horizontal towards centre). Labels: L, r, θ, m, T, Tcosθ, Tsinθ, mg (downward). Clean 2D educational diagram.

---

# 5. Essential Equations / 核心公式

## 5.1 Centripetal Acceleration / 向心加速度

**Equation / 公式:**
$$a = \frac{v^2}{r} = \omega^2 r$$

**Variables / 变量:**
| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $a$ | Centripetal acceleration | 向心加速度 | m s$^{-2}$ |
| $v$ | Linear speed | 线速度 | m s$^{-1}$ |
| $r$ | Radius of circular path | 圆周路径半径 | m |
| $\omega$ | Angular speed | 角速度 | rad s$^{-1}$ |

**Derivation / 推导:**
**English:**
Consider an object moving in a circle of radius $r$ with constant speed $v$. In a small time $\Delta t$, it moves through an angle $\Delta \theta = \omega \Delta t$. The arc length travelled is $s = r \Delta \theta = r \omega \Delta t = v \Delta t$. The velocity vectors $\vec{v}_1$ and $\vec{v}_2$ at the start and end of $\Delta t$ have the same magnitude $v$ but different directions. The change in velocity $\Delta \vec{v} = \vec{v}_2 - \vec{v}_1$ has magnitude $\Delta v \approx v \Delta \theta$ for small $\Delta \theta$. Therefore:
$$a = \frac{\Delta v}{\Delta t} = \frac{v \Delta \theta}{\Delta t} = v \omega = \frac{v^2}{r}$$
The direction of $\Delta \vec{v}$ is towards the centre of the circle.

**中文：**
考虑一个以恒定速率 $v$ 在半径为 $r$ 的圆周上运动的物体。在短时间内 $\Delta t$，它移动了一个角度 $\Delta \theta = \omega \Delta t$。经过的弧长为 $s = r \Delta \theta = r \omega \Delta t = v \Delta t$。在 $\Delta t$ 开始和结束时的速度矢量 $\vec{v}_1$ 和 $\vec{v}_2$ 大小相同 $v$ 但方向不同。速度的变化 $\Delta \vec{v} = \vec{v}_2 - \vec{v}_1$ 的大小，对于小 $\Delta \theta$，近似为 $\Delta v \approx v \Delta \theta$。因此：
$$a = \frac{\Delta v}{\Delta t} = \frac{v \Delta \theta}{\Delta t} = v \omega = \frac{v^2}{r}$$
$\Delta \vec{v}$ 的方向指向圆心。

**Conditions / 适用条件:**
**English:** Object must be moving in a circular path with constant speed. The acceleration is always perpendicular to the velocity.
**中文：** 物体必须以恒定速率沿圆周路径运动。加速度始终垂直于速度。

**Limitations / 局限性:**
**English:** Does not apply to non-uniform circular motion where speed changes (e.g., vertical circles). In such cases, there is also a tangential acceleration component.
**中文：** 不适用于速率变化的非匀速圆周运动（例如，竖直圆）。在这种情况下，还存在切向加速度分量。

**Rearrangements / 变形:**
$$v = \sqrt{ar}$$
$$\omega = \sqrt{\frac{a}{r}}$$
$$r = \frac{v^2}{a}$$

---

## 5.2 Centripetal Force / 向心力

**Equation / 公式:**
$$F = \frac{mv^2}{r} = m\omega^2 r$$

**Variables / 变量:**
| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $F$ | Centripetal force | 向心力 | N |
| $m$ | Mass of object | 物体质量 | kg |
| $v$ | Linear speed | 线速度 | m s$^{-1}$ |
| $r$ | Radius of circular path | 圆周路径半径 | m |
| $\omega$ | Angular speed | 角速度 | rad s$^{-1}$ |

**Derivation / 推导:**
**English:** Directly from [[Newton's Laws of Motion|Newton's Second Law]]: $F = ma$. Substituting $a = v^2/r$ gives $F = mv^2/r$.
**中文：** 直接来自[[牛顿运动定律|牛顿第二定律]]：$F = ma$。代入 $a = v^2/r$ 得 $F = mv^2/r$。

**Conditions / 适用条件:**
**English:** The net force must be directed towards the centre of the circle. The object must be moving in uniform circular motion.
**中文：** 合力必须指向圆心。物体必须做匀速圆周运动。

**Limitations / 局限性:**
**English:** The equation gives the magnitude of the net force required for circular motion. It does not identify the source of that force (e.g., friction, tension, gravity).
**中文：** 该公式给出了圆周运动所需的合力大小。它不指明该力的来源（例如，摩擦力、张力、重力）。

**Rearrangements / 变形:**
$$m = \frac{Fr}{v^2}$$
$$v = \sqrt{\frac{Fr}{m}}$$
$$r = \frac{mv^2}{F}$$

---

## 5.3 Banked Track (Design Speed) / 倾斜轨道（设计速度）

**Equation / 公式:**
$$\tan \theta = \frac{v^2}{rg}$$

**Variables / 变量:**
| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $\theta$ | Banking angle | 倾斜角度 | degrees or rad |
| $v$ | Design speed | 设计速度 | m s$^{-1}$ |
| $r$ | Radius of curvature | 曲率半径 | m |
| $g$ | Acceleration due to gravity | 重力加速度 | m s$^{-2}$ |

**Derivation / 推导:**
**English:**
For a vehicle on a banked track at the design speed, no friction is needed. Resolving forces:
Vertical: $N \cos \theta = mg$
Horizontal: $N \sin \theta = \frac{mv^2}{r}$
Dividing the horizontal equation by the vertical equation gives $\tan \theta = \frac{v^2}{rg}$.

**中文：**
对于以设计速度在倾斜轨道上行驶的车辆，不需要摩擦力。分解力：
竖直方向：$N \cos \theta = mg$
水平方向：$N \sin \theta = \frac{mv^2}{r}$
将水平方程除以竖直方程得 $\tan \theta = \frac{v^2}{rg}$。

**Conditions / 适用条件:**
**English:** Only applies at the design speed where no friction is required. The track is frictionless (or friction is not needed).
**中文：** 仅适用于不需要摩擦力的设计速度。轨道是无摩擦的（或不需要摩擦力）。

**Limitations / 局限性:**
**English:** At speeds other than the design speed, friction is required to maintain circular motion. The equation does not account for friction.
**中文：** 在非设计速度下，需要摩擦力来维持圆周运动。该公式不考虑摩擦力。

**Rearrangements / 变形:**
$$v = \sqrt{rg \tan \theta}$$
$$r = \frac{v^2}{g \tan \theta}$$

---

## 5.4 Conical Pendulum Period / 圆锥摆周期

**Equation / 公式:**
$$T = 2\pi \sqrt{\frac{L \cos \theta}{g}}$$

**Variables / 变量:**
| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $T$ | Period of rotation | 旋转周期 | s |
| $L$ | Length of string | 绳子长度 | m |
| $\theta$ | Angle with vertical | 与竖直方向的夹角 | degrees or rad |
| $g$ | Acceleration due to gravity | 重力加速度 | m s$^{-2}$ |

**Derivation / 推导:**
**English:**
From the conical pendulum analysis:
$T \sin \theta = m\omega^2 r$ and $T \cos \theta = mg$.
Dividing: $\tan \theta = \frac{\omega^2 r}{g}$.
But $r = L \sin \theta$, so $\tan \theta = \frac{\omega^2 L \sin \theta}{g}$.
Simplifying: $\frac{1}{\cos \theta} = \frac{\omega^2 L}{g}$, so $\omega^2 = \frac{g}{L \cos \theta}$.
Since $\omega = \frac{2\pi}{T}$, we get $T = 2\pi \sqrt{\frac{L \cos \theta}{g}}$.

**中文：**
从圆锥摆分析：
$T \sin \theta = m\omega^2 r$ 且 $T \cos \theta = mg$。
相除：$\tan \theta = \frac{\omega^2 r}{g}$。
但 $r = L \sin \theta$，所以 $\tan \theta = \frac{\omega^2 L \sin \theta}{g}$。
简化：$\frac{1}{\cos \theta} = \frac{\omega^2 L}{g}$，所以 $\omega^2 = \frac{g}{L \cos \theta}$。
由于 $\omega = \frac{2\pi}{T}$，我们得到 $T = 2\pi \sqrt{\frac{L \cos \theta}{g}}$。

**Conditions / 适用条件:**
**English:** The string is light and inextensible. Air resistance is negligible. The motion is uniform circular motion in a horizontal plane.
**中文：** 绳子是轻质且不可伸长的。空气阻力可忽略。运动是水平面内的匀速圆周运动。

**Limitations / 局限性:**
**English:** Does not account for air resistance or the mass of the string. Assumes the bob is a point mass.
**中文：** 不考虑空气阻力或绳子的质量。假设摆锤是质点。

**Rearrangements / 变形:**
$$L = \frac{gT^2}{4\pi^2 \cos \theta}$$
$$\cos \theta = \frac{gT^2}{4\pi^2 L}$$

---

# 6. Graphs and Relationships / 图表与关系

## 6.1 Centripetal Acceleration vs. Speed / 向心加速度与速度的关系

### Axes / 坐标轴
**English:** x-axis: Speed $v$ (m s$^{-1}$); y-axis: Centripetal acceleration $a$ (m s$^{-2}$)
**中文：** x轴：速度 $v$ (m s$^{-1}$)；y轴：向心加速度 $a$ (m s$^{-2}$)

### Shape / 形状
**English:** Parabolic curve ($a \propto v^2$) for a fixed radius $r$.
**中文：** 对于固定半径 $r$，为抛物线曲线 ($a \propto v^2$)。

### Gradient Meaning / 斜率含义
**English:** The gradient is not constant. The gradient at any point is $\frac{da}{dv} = \frac{2v}{r}$.
**中文：** 斜率不是常数。任意点的斜率为 $\frac{da}{dv} = \frac{2v}{r}$。

### Area Meaning / 面积含义
**English:** The area under the graph has no direct physical meaning.
**中文：** 图线下的面积没有直接的物理意义。

### Exam Interpretation / 考试解读
**English:** A straight line through the origin when plotting $a$ against $v^2$ confirms the relationship $a = v^2/r$. The gradient is $1/r$.
**中文：** 绘制 $a$ 对 $v^2$ 的图线时，通过原点的直线确认了关系 $a = v^2/r$。斜率为 $1/r$。

### Common Questions / 常见问题
**English:** "Plot a graph of $a$ against $v^2$ and determine the radius of the circle." → Gradient = $1/r$, so $r = 1/\text{gradient}$.
**中文：** "绘制 $a$ 对 $v^2$ 的图线并确定圆的半径。" → 斜率 = $1/r$，所以 $r = 1/\text{斜率}$。

---

## 6.2 Centripetal Force vs. Radius / 向心力与半径的关系

### Axes / 坐标轴
**English:** x-axis: Radius $r$ (m); y-axis: Centripetal force $F$ (N)
**中文：** x轴：半径 $r$ (m)；y轴：向心力 $F$ (N)

### Shape / 形状
**English:** Inverse curve ($F \propto 1/r$) for a fixed speed $v$ and mass $m$.
**中文：** 对于固定速度 $v$ 和质量 $m$，为反比曲线 ($F \propto 1/r$)。

### Gradient Meaning / 斜率含义
**English:** The gradient is negative and not constant. The gradient at any point is $\frac{dF}{dr} = -\frac{mv^2}{r^2}$.
**中文：** 斜率为负且不是常数。任意点的斜率为 $\frac{dF}{dr} = -\frac{mv^2}{r^2}$。

### Area Meaning / 面积含义
**English:** The area under the graph has no direct physical meaning.
**中文：** 图线下的面积没有直接的物理意义。

### Exam Interpretation / 考试解读
**English:** A straight line through the origin when plotting $F$ against $1/r$ confirms the relationship $F = mv^2/r$. The gradient is $mv^2$.
**中文：** 绘制 $F$ 对 $1/r$ 的图线时，通过原点的直线确认了关系 $F = mv^2/r$。斜率为 $mv^2$。

### Common Questions / 常见问题
**English:** "Explain why the graph of $F$ against $r$ is a curve." → Because $F \propto 1/r$, so as $r$ decreases, $F$ increases rapidly.
**中文：** "解释为什么 $F$ 对 $r$ 的图线是曲线。" → 因为 $F \propto 1/r$，所以随着 $r$ 减小，$F$ 迅速增加。

---

## 6.3 Angular Speed vs. Period / 角速度与周期的关系

### Axes / 坐标轴
**English:** x-axis: Period $T$ (s); y-axis: Angular speed $\omega$ (rad s$^{-1}$)
**中文：** x轴：周期 $T$ (s)；y轴：角速度 $\omega$ (rad s$^{-1}$)

### Shape / 形状
**English:** Inverse curve ($\omega \propto 1/T$).
**中文：** 反比曲线 ($\omega \propto 1/T$)。

### Gradient Meaning / 斜率含义
**English:** The gradient is negative and not constant. The gradient at any point is $\frac{d\omega}{dT} = -\frac{2\pi}{T^2}$.
**中文：** 斜率为负且不是常数。任意点的斜率为 $\frac{d\omega}{dT} = -\frac{2\pi}{T^2}$。

### Area Meaning / 面积含义
**English:** The area under the graph has no direct physical meaning.
**中文：** 图线下的面积没有直接的物理意义。

### Exam Interpretation / 考试解读
**English:** A straight line through the origin when plotting $\omega$ against $1/T$ confirms $\omega = 2\pi/T$. The gradient is $2\pi$.
**中文：** 绘制 $\omega$ 对 $1/T$ 的图线时，通过原点的直线确认了 $\omega = 2\pi/T$。斜率为 $2\pi$。

### Common Questions / 常见问题
**English:** "Determine the period when $\omega = 5$ rad s$^{-1}$." → $T = 2\pi/\omega = 2\pi/5 = 1.26$ s.
**中文：** "当 $\omega = 5$ rad s$^{-1}$ 时，确定周期。" → $T = 2\pi/\omega = 2\pi/5 = 1.26$ s。

---

# 7. Required Diagrams / 必备图表

## 7.1 Vector Diagram for Centripetal Acceleration Derivation / 向心加速度推导的矢量图

### Description / 描述
**English:** A diagram showing a circle of radius $r$. Two velocity vectors $\vec{v}_1$ and $\vec{v}_2$ are drawn tangential to the circle at two nearby points separated by a small angle $\Delta \theta$. The vector difference $\Delta \vec{v} = \vec{v}_2 - \vec{v}_1$ is shown pointing towards the centre of the circle. Labels include $r$, $\vec{v}_1$, $\vec{v}_2$, $\Delta \theta$, and $\Delta \vec{v}$.

**中文：** 一个显示半径为 $r$ 的圆的图。两个速度矢量 $\vec{v}_1$ 和 $\vec{v}_2$ 在由小角度 $\Delta \theta$ 分隔的两个邻近点处与圆相切。矢量差 $\Delta \vec{v} = \vec{v}_2 - \vec{v}_1$ 显示指向圆心。标签包括 $r$、$\vec{v}_1$、$\vec{v}_2$、$\Delta \theta$ 和 $\Delta \vec{v}$。

### Image Prompt / 图片生成提示
> 📷 **IMAGE PROMPT — CP05: Vector Diagram for Centripetal Acceleration**
>
> A 2D vector diagram on a clean white background. A circle of radius r is drawn. Two velocity vectors v1 and v2 are shown as arrows tangential to the circle at two points separated by angle Δθ. The vector difference Δv = v2 - v1 is shown as an arrow pointing towards the centre of the circle. All vectors are labelled. The angle Δθ is marked at the centre. Educational style, clear labels, no shadows.

### Labels Required / 需要标注
- $r$ (radius)
- $\vec{v}_1$ (initial velocity)
- $\vec{v}_2$ (final velocity)
- $\Delta \theta$ (angular displacement)
- $\Delta \vec{v}$ (change in velocity)
- Centre of circle

### Exam Importance / 考试重要性
**English:** This diagram is essential for deriving the formula $a = v^2/r$ from first principles. Both CIE and Edexcel may ask students to draw or interpret this diagram.
**中文：** 该图对于从基本原理推导公式 $a = v^2/r$ 至关重要。CIE 和 Edexcel 都可能要求学生绘制或解释此图。

---

## 7.2 Free-Body Diagram for a Banked Track / 倾斜轨道的受力图

### Description / 描述
**English:** A diagram showing a car (or block) on a banked track inclined at angle $\theta$ to the horizontal. Forces shown include: weight $mg$ acting vertically downward, normal reaction $N$ acting perpendicular to the track surface, and optionally friction $f$ acting parallel to the track surface. The normal reaction is resolved into vertical component $N \cos \theta$ and horizontal component $N \sin \theta$ (pointing towards the centre of the circle).

**中文：** 一个显示汽车（或物块）在与水平面成 $\theta$ 角倾斜的轨道上的图。显示的力包括：重力 $mg$ 竖直向下，法向反作用力 $N$ 垂直于轨道表面，以及可选的摩擦力 $f$ 平行于轨道表面。法向反作用力被分解为竖直分量 $N \cos \theta$ 和水平分量 $N \sin \theta$（指向圆心）。

### Image Prompt / 图片生成提示
> 📷 **IMAGE PROMPT — CP06: Banked Track Free-Body Diagram**
>
> A 2D educational diagram. A car is shown on a banked track inclined at angle θ. Three force arrows: mg (downward), N (perpendicular to track surface), f (parallel to track surface, optional). N is resolved into Ncosθ (vertical) and Nsinθ (horizontal towards centre). All forces and components are labelled. Clean white background, clear arrows, educational style.

### Labels Required / 需要标注
- $\theta$ (banking angle)
- $mg$ (weight)
- $N$ (normal reaction)
- $N \cos \theta$ (vertical component)
- $N \sin \theta$ (horizontal component)
- $f$ (friction, optional)
- Centre of circle direction

### Exam Importance / 考试重要性
**English:** This diagram is essential for solving banked track problems. Students must be able to draw and resolve forces correctly.
**中文：** 该图对于解决倾斜轨道问题至关重要。学生必须能够正确绘制和分解力。

---

## 7.3 Conical Pendulum Diagram / 圆锥摆图

### Description / 描述
**English:** A diagram showing a mass $m$ attached to a string of length $L$, moving in a horizontal circle of radius $r$. The string makes an angle $\theta$ with the vertical. The tension $T$ in the string is shown, resolved into vertical component $T \cos \theta$ and horizontal component $T \sin \theta$ (pointing towards the centre of the circle). The weight $mg$ is shown acting downward.

**中文：** 一个显示质量为 $m$ 的物体连接在长度为 $L$ 的绳子上，在半径为 $r$ 的水平圆周上运动的图。绳子与竖直方向成 $\theta$ 角。显示绳子中的张力 $T$，分解为竖直分量 $T \cos \theta$ 和水平分量 $T \sin \theta$（指向圆心）。重力 $mg$ 显示向下作用。

### Image Prompt / 图片生成提示
> 📷 **IMAGE PROMPT — CP07: Conical Pendulum Diagram**
>
> A 2D educational diagram. A mass m is attached to a string of length L, moving in a horizontal circle of radius r. The string makes angle θ with the vertical. Tension T is shown along the string, resolved into Tcosθ (vertical upward) and Tsinθ (horizontal towards centre). Weight mg is shown downward. Labels: L, r, θ, m, T, Tcosθ, Tsinθ, mg. Clean white background, clear arrows, educational style.

### Labels Required / 需要标注
- $L$ (string length)
- $r$ (radius of circle)
- $\theta$ (angle with vertical)
- $m$ (mass)
- $T$ (tension)
- $T \cos \theta$ (vertical component)
- $T \sin \theta$ (horizontal component)
- $mg$ (weight)

### Exam Importance / 考试重要性
**English:** This diagram is essential for solving conical pendulum problems. Students must be able to resolve tension and apply Newton's Second Law.
**中文：** 该图对于解决圆锥摆问题至关重要。学生必须能够分解张力并应用牛顿第二定律。

---

# 8. Worked Examples / 典型例题

## Example 1: Car on a Banked Track / 汽车在倾斜轨道上

### Question / 题目
**English:**
A car of mass 1200 kg travels around a banked track of radius 50 m. The track is banked at an angle of 15° to the horizontal. Calculate:
(a) The design speed at which no friction is required.
(b) The centripetal force acting on the car at this speed.
(c) The normal reaction force on the car.

**中文：**
一辆质量为 1200 kg 的汽车在半径为 50 m 的倾斜轨道上行驶。轨道与水平面成 15° 角倾斜。计算：
(a) 不需要摩擦力时的设计速度。
(b) 在此速度下作用在汽车上的向心力。
(c) 作用在汽车上的法向反作用力。

### Image Prompt / 图片提示
> 📷 **IMAGE PROMPT — CP08: Car on Banked Track Question Diagram**
>
> A car on a banked track inclined at 15°. Radius r = 50 m is shown. Forces: mg, N. Clean 2D educational diagram.

### Solution / 解答

**Part (a): Design speed / 设计速度**

**English:**
Using the banked track formula:
$$\tan \theta = \frac{v^2}{rg}$$
$$v = \sqrt{rg \tan \theta}$$
$$v = \sqrt{50 \times 9.81 \times \tan 15^\circ}$$
$$v = \sqrt{50 \times 9.81 \times 0.2679}$$
$$v = \sqrt{131.4}$$
$$v = 11.5 \text{ m s}^{-1}$$

**中文：**
使用倾斜轨道公式：
$$\tan \theta = \frac{v^2}{rg}$$
$$v = \sqrt{rg \tan \theta}$$
$$v = \sqrt{50 \times 9.81 \times \tan 15^\circ}$$
$$v = \sqrt{50 \times 9.81 \times 0.2679}$$
$$v = \sqrt{131.4}$$
$$v = 11.5 \text{ m s}^{-1}$$

**Part (b): Centripetal force / 向心力**

**English:**
$$F = \frac{mv^2}{r}$$
$$F = \frac{1200 \times (11.5)^2}{50}$$
$$F = \frac{1200 \times 132.25}{50}$$
$$F = \frac{158700}{50}$$
$$F = 3174 \text{ N}$$

**中文：**
$$F = \frac{mv^2}{r}$$
$$F = \frac{1200 \times (11.5)^2}{50}$$
$$F = \frac{1200 \times 132.25}{50}$$
$$F = \frac{158700}{50}$$
$$F = 3174 \text{ N}$$

**Part (c): Normal reaction / 法向反作用力**

**English:**
From vertical equilibrium:
$$N \cos \theta = mg$$
$$N = \frac{mg}{\cos \theta}$$
$$N = \frac{1200 \times 9.81}{\cos 15^\circ}$$
$$N = \frac{11772}{0.9659}$$
$$N = 12187 \text{ N}$$

**中文：**
从竖直方向平衡：
$$N \cos \theta = mg$$
$$N = \frac{mg}{\cos \theta}$$
$$N = \frac{1200 \times 9.81}{\cos 15^\circ}$$
$$N = \frac{11772}{0.9659}$$
$$N = 12187 \text{ N}$$

### Final Answer / 最终答案
**Answer:** (a) $v = 11.5$ m s$^{-1}$ | **答案：** (a) $v = 11.5$ m s$^{-1}$
**Answer:** (b) $F = 3174$ N | **答案：** (b) $F = 3174$ N
**Answer:** (c) $N = 12187$ N | **答案：** (c) $N = 12187$ N

### Examiner Notes / 考官点评
**English:**
- Common mistake: Forgetting to convert degrees to radians when using trigonometric functions in calculators. Ensure calculator is in degree mode.
- Common mistake: Using $N = mg$ instead of $N = mg/\cos \theta$. The normal reaction is larger than the weight because it has to provide both the vertical support and the horizontal centripetal force.
- Always check that the centripetal force equals the horizontal component of $N$: $N \sin \theta = 12187 \times \sin 15^\circ = 12187 \times 0.2588 = 3154$ N (close to 3174 N, small rounding difference).

**中文：**
- 常见错误：在使用计算器进行三角函数计算时，忘记将度数转换为弧度。确保计算器处于度数模式。
- 常见错误：使用 $N = mg$ 而不是 $N = mg/\cos \theta$。法向反作用力大于重力，因为它必须同时提供竖直支撑和水平向心力。
- 始终检查向心力是否等于 $N$ 的水平分量：$N \sin \theta = 12187 \times \sin 15^\circ = 12187 \times 0.2588 = 3154$ N（接近 3174 N，存在小的舍入差异）。

### Alternative Method / 替代方法
**English:**
For part (b), the centripetal force can also be found from the horizontal component of the normal reaction:
$$F = N \sin \theta = 12187 \times \sin 15^\circ = 3154 \text{ N}$$
This provides a useful check.

**中文：**
对于部分 (b)，向心力也可以从法向反作用力的水平分量求得：
$$F = N \sin \theta = 12187 \times \sin 15^\circ = 3154 \text{ N}$$
这提供了一个有用的检查。

---

## Example 2: Conical Pendulum / 圆锥摆

### Question / 题目
**English:**
A conical pendulum consists of a mass of 0.50 kg attached to a string of length 1.2 m. The mass rotates in a horizontal circle such that the string makes an angle of 30° with the vertical. Calculate:
(a) The tension in the string.
(b) The speed of the mass.
(c) The period of rotation.

**中文：**
一个圆锥摆由一个质量为 0.50 kg 的物体组成，连接在一根长度为 1.2 m 的绳子上。物体在水平圆周内旋转，使得绳子与竖直方向成 30° 角。计算：
(a) 绳子中的张力。
(b) 物体的速度。
(c) 旋转周期。

### Solution / 解答

**Part (a): Tension / 张力**

**English:**
From vertical equilibrium:
$$T \cos \theta = mg$$
$$T = \frac{mg}{\cos \theta}$$
$$T = \frac{0.50 \times 9.81}{\cos 30^\circ}$$
$$T = \frac{4.905}{0.8660}$$
$$T = 5.66 \text{ N}$$

**中文：**
从竖直方向平衡：
$$T \cos \theta = mg$$
$$T = \frac{mg}{\cos \theta}$$
$$T = \frac{0.50 \times 9.81}{\cos 30^\circ}$$
$$T = \frac{4.905}{0.8660}$$
$$T = 5.66 \text{ N}$$

**Part (b): Speed / 速度**

**English:**
First, find the radius of the circle:
$$r = L \sin \theta = 1.2 \times \sin 30^\circ = 1.2 \times 0.5 = 0.60 \text{ m}$$

The horizontal component of tension provides the centripetal force:
$$T \sin \theta = \frac{mv^2}{r}$$
$$v^2 = \frac{T \sin \theta \times r}{m}$$
$$v^2 = \frac{5.66 \times \sin 30^\circ \times 0.60}{0.50}$$
$$v^2 = \frac{5.66 \times 0.5 \times 0.60}{0.50}$$
$$v^2 = \frac{1.698}{0.50}$$
$$v^2 = 3.396$$
$$v = 1.84 \text{ m s}^{-1}$$

**中文：**
首先，求圆的半径：
$$r = L \sin \theta = 1.2 \times \sin 30^\circ = 1.2 \times 0.5 = 0.60 \text{ m}$$

张力的水平分量提供向心力：
$$T \sin \theta = \frac{mv^2}{r}$$
$$v^2 = \frac{T \sin \theta \times r}{m}$$
$$v^2 = \frac{5.66 \times \sin 30^\circ \times 0.60}{0.50}$$
$$v^2 = \frac{5.66 \times 0.5 \times 0.60}{0.50}$$
$$v^2 = \frac{1.698}{0.50}$$
$$v^2 = 3.396$$
$$v = 1.84 \text{ m s}^{-1}$$

**Part (c): Period / 周期**

**English:**
Using the period formula:
$$T = 2\pi \sqrt{\frac{L \cos \theta}{g}}$$
$$T = 2\pi \sqrt{\frac{1.2 \times \cos 30^\circ}{9.81}}$$
$$T = 2\pi \sqrt{\frac{1.2 \times 0.8660}{9.81}}$$
$$T = 2\pi \sqrt{\frac{1.039}{9.81}}$$
$$T = 2\pi \sqrt{0.1059}$$
$$T = 2\pi \times 0.3255$$
$$T = 2.04 \text{ s}$$

Alternatively, using $v = 2\pi r / T$:
$$T = \frac{2\pi r}{v} = \frac{2\pi \times 0.60}{1.84} = \frac{3.77}{1.84} = 2.05 \text{ s}$$

**中文：**
使用周期公式：
$$T = 2\pi \sqrt{\frac{L \cos \theta}{g}}$$
$$T = 2\pi \sqrt{\frac{1.2 \times \cos 30^\circ}{9.81}}$$
$$T = 2\pi \sqrt{\frac{1.2 \times 0.8660}{9.81}}$$
$$T = 2\pi \sqrt{\frac{1.039}{9.81}}$$
$$T = 2\pi \sqrt{0.1059}$$
$$T = 2\pi \times 0.3255$$
$$T = 2.04 \text{ s}$$

或者，使用 $v = 2\pi r / T$：
$$T = \frac{2\pi r}{v} = \frac{2\pi \times 0.60}{1.84} = \frac{3.77}{1.84} = 2.05 \text{ s}$$

### Final Answer / 最终答案
**Answer:** (a) $T = 5.66$ N | **答案：** (a) $T = 5.66$ N
**Answer:** (b) $v = 1.84$ m s$^{-1}$ | **答案：** (b) $v = 1.84$ m s$^{-1}$
**Answer:** (c) $T = 2.04$ s | **答案：** (c) $T = 2.04$ s

### Examiner Notes / 考官点评
**English:**
- Common mistake: Using the string length $L$ as the radius $r$. Remember $r = L \sin \theta$.
- Common mistake: Forgetting that the centripetal force is only the horizontal component of tension, not the full tension.
- The period is independent of the mass of the bob. This is a common exam question.
- Always check consistency: The two methods for period should give the same answer (within rounding).

**中文：**
- 常见错误：将绳子长度 $L$ 用作半径 $r$。记住 $r = L \sin \theta$。
- 常见错误：忘记向心力只是张力的水平分量，而不是整个张力。
- 周期与摆锤的质量无关。这是一个常见的考试问题。
- 始终检查一致性：两种求周期的方法应给出相同的答案（在舍入范围内）。

### Alternative Method / 替代方法
**English:**
For part (b), we can also use the relationship derived from dividing the force equations:
$$\tan \theta = \frac{v^2}{rg}$$
$$v = \sqrt{rg \tan \theta} = \sqrt{0.60 \times 9.81 \times \tan 30^\circ} = \sqrt{0.60 \times 9.81 \times 0.5774} = \sqrt{3.398} = 1.84 \text{ m s}^{-1}$$

**中文：**
对于部分 (b)，我们也可以使用从力方程相除推导出的关系：
$$\tan \theta = \frac{v^2}{rg}$$
$$v = \sqrt{rg \tan \theta} = \sqrt{0.60 \times 9.81 \times \tan 30^\circ} = \sqrt{0.60 \times 9.81 \times 0.5774} = \sqrt{3.398} = 1.84 \text{ m s}^{-1}$$

---

# 9. Past Paper Question Types / 历年真题题型

**English:**
The following table summarises the types of questions that appear in both CIE and Edexcel examinations for this topic. Specific past paper references will be added as the question bank is compiled.

**中文：**
下表总结了 CIE 和 Edexcel 考试中本主题出现的题型。具体试卷编号将在题库整理后填入。

| Question Type / 题型 | Frequency / 频率 | Difficulty / 难度 | Past Paper References / 真题索引 |
|----------------------|------------------|------------------|-------------------------------|
| Calculation of centripetal acceleration/force / 计算向心加速度/力 | High | Medium | 📝 *待填入* |
| Derivation of $a = v^2/r$ / 推导 $a = v^2/r$ | Medium | High | 📝 *待填入* |
| Banked track problems / 倾斜轨道问题 | High | High | 📝 *待填入* |
| Conical pendulum problems / 圆锥摆问题 | Medium | High | 📝 *待填入* |
| Vertical circle problems / 竖直圆问题 | Medium | High | 📝 *待填入* |
| Graph interpretation / 图表解读 | Low | Medium | 📝 *待填入* |
| Practical design / 实验设计 | Low | High | 📝 *待填入* |

> 📝 **题库整理中 / Question Bank Under Construction:** 具体试卷编号（如 9702/23/M/J/24 Q3）将在后续整理真题后填入上表。

**Common Command Words / 常见指令词:**

| English | 中文 | Meaning / 含义 |
|---------|------|----------------|
| State | 陈述 | Give a brief answer without explanation. |
| Define | 定义 | Give the precise meaning of a term. |
| Explain | 解释 | Give reasons or causes for a phenomenon. |
| Describe | 描述 | Give a detailed account of a process or diagram. |
| Calculate | 计算 | Use mathematical operations to find a numerical answer. |
| Determine | 确定 | Find a value using given data or a graph. |
| Suggest | 建议 | Propose a possible explanation or method. |
| Derive | 推导 | Show the steps to obtain a formula from first principles. |
| Sketch | 草图 | Draw a graph or diagram showing the main features. |

---

# 10. Practical Skills Connections / 实验技能链接

**English:**
This topic connects to practical work in both CIE and Edexcel specifications.

**CIE Practical Connections:**
- **Paper 3 (AS):** While centripetal force is an A2 topic, the practical skills of measuring time periods, using stopwatches, and analysing circular motion are developed at AS level through experiments like the "whirling bung" or "conical pendulum."
- **Paper 5 (A2):** Students may be asked to design an experiment to investigate the relationship between centripetal force and radius, speed, or mass. This could involve:
  - Using a variable speed motor to rotate a mass on a string.
  - Measuring the radius of the circular path using a ruler or marker.
  - Measuring the period using a light gate or stopwatch.
  - Varying the mass, radius, or speed systematically.
  - Plotting graphs (e.g., $F$ against $v^2$, $F$ against $1/r$) to verify the relationship.
  - Calculating uncertainties in measurements of $r$, $T$, and $m$.
  - Evaluating the effectiveness of the experimental setup (e.g., air resistance, friction, string elasticity).

**Edexcel Practical Connections:**
- **Unit 3 (AS):** Practical skills for measuring time periods and using data loggers.
- **Unit 6 (A2):** Students may be required to:
  - Investigate the factors affecting centripetal force using a rotating platform or "whirling bung."
  - Use a force sensor to measure tension in the string.
  - Use a motion sensor or video analysis to determine speed.
  - Analyse the conical pendulum to determine $g$.
  - Evaluate the uncertainties in the experiment.

**Key Measurements / 关键测量:**
- **Radius ($r$):** Measure using a ruler. Uncertainty: ±1 mm.
- **Period ($T$):** Measure time for 10 or 20 revolutions using a stopwatch. Uncertainty: ±0.1 s for total time, ±0.01 s per revolution.
- **Mass ($m$):** Measure using a balance. Uncertainty: ±0.1 g.
- **Speed ($v$):** Calculate from $v = 2\pi r / T$. Uncertainty propagated from $r$ and $T$.
- **Force ($F$):** Measure using a force sensor or spring balance. Uncertainty: ±0.01 N.

**Common Experimental Errors / 常见实验误差:**
- **English:** Air resistance causes the speed to decrease over time. Use a motor to maintain constant speed.
- **English:** Friction in the pulley or bearing affects the tension. Use a smooth bearing.
- **English:** The string may stretch, changing the radius. Use an inextensible string.
- **English:** Parallax error when measuring the radius. Use a marker on the string.
- **中文：** 空气阻力导致速度随时间减小。使用电机保持恒定速度。
- **中文：** 滑轮或轴承中的摩擦力影响张力。使用光滑轴承。
- **中文：** 绳子可能拉伸，改变半径。使用不可伸长的绳子。
- **中文：** 测量半径时的视差误差。在绳子上使用标记。

> 📋 **CIE Only:** CIE Paper 5 often asks students to design an experiment to investigate the relationship between centripetal force and one variable (e.g., radius). Students must include a labelled diagram, a list of equipment, a step-by-step procedure, a table for data, and an analysis method (graph plotting).
>
> 📋 **Edexcel Only:** Edexcel Unit 6 may include a practical question on the conical pendulum, asking students to determine the acceleration due to gravity $g$ from measurements of $L$, $\theta$, and $T$.

**中文：**
本主题与 CIE 和 Edexcel 考试局中的实验工作相关联。

**CIE 实验联系：**
- **试卷 3（AS）：** 虽然向心力是 A2 主题，但测量周期、使用秒表和分析圆周运动的实验技能在 AS 阶段通过"旋转塞子"或"圆锥摆"等实验得到培养。
- **试卷 5（A2）：** 学生可能被要求设计一个实验来研究向心力与半径、速度或质量之间的关系。这可能涉及：
  - 使用变速电机旋转绳子上的质量。
  - 使用尺子或标记测量圆周路径的半径。
  - 使用光门或秒表测量周期。
  - 系统地改变质量、半径或速度。
  - 绘制图表（例如，$F$ 对 $v^2$，$F$ 对 $1/r$）以验证关系。
  - 计算 $r$、$T$ 和 $m$ 测量的不确定度。
  - 评估实验装置的有效性（例如，空气阻力、摩擦力、绳子弹性）。

**Edexcel 实验联系：**
- **单元 3（AS）：** 测量周期和使用数据记录器的实验技能。
- **单元 6（A2）：** 学生可能需要：
  - 使用旋转平台或"旋转塞子"研究影响向心力的因素。
  - 使用力传感器测量绳子中的张力。
  - 使用运动传感器或视频分析确定速度。
  - 分析圆锥摆以确定 $g$。
  - 评估实验中的不确定度。

**关键测量：**
- **半径 ($r$)：** 使用尺子测量。不确定度：±1 mm。
- **周期 ($T$)：** 使用秒表测量 10 或 20 次旋转的时间。不确定度：总时间 ±0.1 s，每次旋转 ±0.01 s。
- **质量 ($m$)：** 使用天平测量。不确定度：±0.1 g。
- **速度 ($v$)：** 从 $v = 2\pi r / T$ 计算。不确定度从 $r$ 和 $T$ 传播。
- **力 ($F$)：** 使用力传感器或弹簧秤测量。不确定度：±0.01 N。

**常见实验误差：**
- **English:** 空气阻力导致速度随时间减小。使用电机保持恒定速度。
- **English:** 滑轮或轴承中的摩擦力影响张力。使用光滑轴承。
- **English:** 绳子可能拉伸，改变半径。使用不可伸长的绳子。
- **English:** 测量半径时的视差误差。在绳子上使用标记。

> 📋 **CIE 专属：** CIE 试卷 5 经常要求学生设计一个实验来研究向心力与一个变量（例如半径）之间的关系。学生必须包括标注的图表、设备清单、分步程序、数据表格和分析方法（图表绘制）。
>
> 📋 **Edexcel 专属：** Edexcel 单元 6 可能包括一个关于圆锥摆的实验问题，要求学生从 $L$、$\theta$ 和 $T$ 的测量中确定重力加速度 $g$。

---

# 11. Concept Map / 概念图谱

**English:**
The following concept map shows the relationships between this topic (Centripetal Acceleration and Force), its prerequisites, related topics, and sub-topics.

**中文：**
以下概念图显示了本主题（向心加速度与向心力）、其先决条件、相关主题和子主题之间的关系。

```mermaid
graph TD
    %% Central Topic
    CAF[Centripetal Acceleration and Force] --> CA[Centripetal Acceleration Formula]
    CAF --> CF[Centripetal Force]
    CAF --> BTCP[Banked Tracks and Conical Pendulum]

    %% Prerequisites
    AM[Angular Measures] --> CAF
    NLM[Newton's Laws of Motion] --> CAF

    %% Related Topics
    GFF[Gravitational Force and Field] --> CO[Circular Orbits]
    CAF --> CO
    CAF --> GFF

    %% Sub-topics details
    CA --> a_eq[a = v²/r = ω²r]
    CF --> F_eq[F = mv²/r = mω²r]
    BTCP --> BT[Banked Tracks]
    BTCP --> CP[Conical Pendulum]
    BT --> tan_eq[tanθ = v²/rg]
    CP --> T_eq[T = 2π√(Lcosθ/g)]

    %% Connections
    AM --> radian[Radian Definition]
    AM --> omega[Angular Speed ω]
    NLM --> F_ma[F = ma]
    GFF --> gravity[Gravity as Centripetal Force]

    %% Styling
    classDef central fill:#f9f,stroke:#333,stroke-width:4px;
    classDef sub fill:#bbf,stroke:#333,stroke-width:2px;
    classDef pre fill:#bfb,stroke:#333,stroke-width:2px;
    classDef related fill:#fbb,stroke:#333,stroke-width:2px;

    class CAF central;
    class CA,CF,BTCP sub;
    class AM,NLM pre;
    class GFF,CO related;
```

---

# 12. Quick Revision Sheet / 速查表

**English:**
This one-page summary provides all key points for quick revision before exams.

**中文：**
此一页摘要提供了考试前快速复习的所有要点。

| Category / 类别 | Key Points / 要点 |
|----------------|------------------|
| **Definitions / 定义** | **Centripetal Acceleration:** Acceleration towards centre of circle, changes direction only. $a = v^2/r = \omega^2 r$. <br> **Centripetal Force:** Net force towards centre. $F = mv^2/r = m\omega^2 r$. Not a new force. <br> **Angular Speed:** $\omega = \Delta \theta / \Delta t = 2\pi/T = 2\pi f$. <br> **Radian:** Angle when arc length = radius. $2\pi$ rad = $360^\circ$. |
| **Equations / 公式** | $a = \frac{v^2}{r} = \omega^2 r$ <br> $F = \frac{mv^2}{r} = m\omega^2 r$ <br> $v = \omega r$ <br> $\omega = \frac{2\pi}{T} = 2\pi f$ <br> **Banked Track (design speed):** $\tan \theta = \frac{v^2}{rg}$ <br> **Conical Pendulum:** $T = 2\pi \sqrt{\frac{L \cos \theta}{g}}$ |
| **Graphs / 图表** | $a$ vs $v$: Parabola ($a \propto v^2$). <br> $a$ vs $v^2$: Straight line through origin, gradient $= 1/r$. <br> $F$ vs $r$: Inverse curve ($F \propto 1/r$). <br> $F$ vs $1/r$: Straight line through origin, gradient $= mv^2$. <br> $\omega$ vs $T$: Inverse curve ($\omega \propto 1/T$). |
| **Key Facts / 关键事实** | 1. Centripetal force is always perpendicular to velocity. <br> 2. Centripetal force does no work (no change in kinetic energy). <br> 3. For banked tracks, design speed is independent of mass. <br> 4. For conical pendulum, period is independent of mass. <br> 5. In vertical circles, speed is not constant; use energy conservation. |
| **Exam Reminders / 考试提醒** | 1. Always identify the source of centripetal force. <br> 2. Draw free-body diagrams for banked tracks and conical pendulums. <br> 3. Resolve forces into horizontal (centripetal) and vertical (equilibrium) components. <br> 4. Check units: $v$ in m s$^{-1}$, $r$ in m, $\omega$ in rad s$^{-1}$. <br> 5. For derivation of $a = v^2/r$, use vector diagram with $\Delta \vec{v}$. <br> 6. Remember: $F = ma$ applies to circular motion too! |