# 1. Overview / 概述

**English:** This topic explores the physics of objects moving in circular paths. When an object moves in a circle at constant speed, its velocity is constantly changing direction, meaning it is accelerating. This acceleration, called [[Centripetal Acceleration Formula|centripetal acceleration]], is always directed towards the centre of the circle. The force causing this acceleration, [[Centripetal Force|centripetal force]], is not a new type of force but the net force required to maintain circular motion. This topic is fundamental to understanding [[Circular Orbits|orbits]], [[Banked Tracks and Conical Pendulum|banked tracks]], and many real-world applications from car cornering to particle accelerators. In both CAIE 9702 and Edexcel IAL, this is a high-weightage A2 topic, frequently tested in multiple-choice, structured questions, and practical contexts.

**中文:** 本主题探讨物体沿圆周路径运动的物理原理。当物体以恒定速度做圆周运动时，其速度方向不断变化，这意味着它在加速。这种加速度称为[[Centripetal Acceleration Formula|向心加速度]]，始终指向圆心。引起这种加速度的力称为[[Centripetal Force|向心力]]，它不是一种新的力，而是维持圆周运动所需的合力。本主题是理解[[Circular Orbits|轨道]]、[[Banked Tracks and Conical Pendulum|倾斜轨道和圆锥摆]]以及从汽车转弯到粒子加速器等许多实际应用的基础。在CAIE 9702和Edexcel IAL中，这是一个高权重的A2主题，经常在选择题、结构化问题和实验背景中出现。

# 2. Syllabus Learning Objectives / 考纲学习目标

| CAIE 9702 (14.2 a-d) | Edexcel IAL (WPH14 U4: 5.5-5.9) |
|---|---|
| (a) Define radian and express angular displacement in radians | 5.5 Understand the concept of angular speed for circular motion |
| (b) Understand and use the concept of angular speed | 5.6 Understand that a resultant force (centripetal force) is required to maintain circular motion |
| (c) Recall and use equations $a = v^2/r$ and $a = \omega^2 r$ | 5.7 Derive and use equations for centripetal acceleration: $a = v^2/r$ and $a = \omega^2 r$ |
| (d) Recall and use equations $F = mv^2/r$ and $F = m\omega^2 r$ | 5.8 Derive and use equations for centripetal force: $F = mv^2/r$ and $F = m\omega^2 r$ |
| | 5.9 Solve problems involving centripetal force in various contexts (e.g., banked tracks, conical pendulum) |

**Examiner Expectations / 考官期望:**
- **English:** Candidates must be able to derive $a = v^2/r$ from velocity vector diagrams. They must identify the source of centripetal force in different scenarios (e.g., tension, friction, gravity, normal reaction). For [[Banked Tracks and Conical Pendulum|banked tracks]], candidates should resolve forces horizontally and vertically.
- **中文:** 考生必须能够从速度矢量图推导出 $a = v^2/r$。他们必须能够识别不同场景中向心力的来源（例如张力、摩擦力、重力、法向反作用力）。对于[[Banked Tracks and Conical Pendulum|倾斜轨道和圆锥摆]]，考生应在水平和垂直方向上分解力。

> 📋 **CIE Only:** CAIE requires explicit definition of the radian and conversion between degrees and radians.
> 📋 **Edexcel Only:** Edexcel places greater emphasis on deriving centripetal acceleration using calculus (differentiation of position vectors) and solving problems involving variable speed circular motion.

# 3. Core Definitions / 核心定义

| Term (EN/CN) | Definition (EN) | Definition (CN) | Common Mistakes / 常见错误 |
|---|---|---|---|
| [[Angular Measures|Angular Displacement]] / 角位移 | The angle swept out by the radius vector as an object moves along a circular path, measured in radians. | 物体沿圆周路径运动时，半径矢量扫过的角度，以弧度为单位。 | Confusing with linear displacement; forgetting to use radians in equations |
| [[Angular Measures|Angular Speed]] ($\omega$) / 角速度 | The rate of change of angular displacement: $\omega = \Delta\theta / \Delta t$, measured in rad s⁻¹. | 角位移的变化率：$\omega = \Delta\theta / \Delta t$，单位为 rad s⁻¹。 | Confusing with linear speed; forgetting that $\omega$ is constant for uniform circular motion |
| [[Centripetal Acceleration Formula|Centripetal Acceleration]] ($a$) / 向心加速度 | The acceleration of an object moving in a circle at constant speed, always directed towards the centre of the circle. | 物体以恒定速度做圆周运动时的加速度，始终指向圆心。 | Thinking acceleration is zero because speed is constant; confusing direction |
| [[Centripetal Force|Centripetal Force]] ($F$) / 向心力 | The net force required to keep an object moving in a circular path, directed towards the centre of the circle. | 使物体保持圆周运动所需的合力，方向指向圆心。 | Calling it a "new" force; forgetting it is the resultant of real forces |
| Period ($T$) / 周期 | The time taken for one complete revolution: $T = 2\pi/\omega$. | 完成一次完整旋转所需的时间：$T = 2\pi/\omega$。 | Confusing with frequency; using wrong units |
| Frequency ($f$) / 频率 | The number of complete revolutions per second: $f = 1/T = \omega/2\pi$, measured in Hz. | 每秒完成的完整旋转次数：$f = 1/T = \omega/2\pi$，单位为 Hz。 | Confusing with angular speed; forgetting $f = 1/T$ |

# 4. Key Concepts Explained / 关键概念详解

## 4.1 Centripetal Acceleration / 向心加速度

### Explanation / 解释
**English:** [[Centripetal Acceleration Formula|Centripetal acceleration]] arises because velocity is a vector quantity. Even when an object moves at constant speed $v$ around a circle of radius $r$, its direction changes continuously. Over a small time interval $\Delta t$, the velocity vector rotates by an angle $\Delta\theta$. Using vector subtraction, the change in velocity $\Delta v$ points towards the centre of the circle. The magnitude of centripetal acceleration is given by $a = v^2/r = \omega^2 r$. This is derived from the geometry of velocity vectors: for small angles, $\Delta v \approx v\Delta\theta$, and since $\Delta\theta = \omega\Delta t$, we get $a = \Delta v/\Delta t = v\omega = v^2/r$.

**中文:** [[Centripetal Acceleration Formula|向心加速度]]的产生是因为速度是矢量。即使物体以恒定速度 $v$ 绕半径为 $r$ 的圆运动，其方向也在不断变化。在微小时间间隔 $\Delta t$ 内，速度矢量旋转了角度 $\Delta\theta$。通过矢量减法，速度变化量 $\Delta v$ 指向圆心。向心加速度的大小由 $a = v^2/r = \omega^2 r$ 给出。这是从速度矢量的几何推导得出的：对于小角度，$\Delta v \approx v\Delta\theta$，且由于 $\Delta\theta = \omega\Delta t$，我们得到 $a = \Delta v/\Delta t = v\omega = v^2/r$。

### Physical Meaning / 物理意义
**English:** The centripetal acceleration is the rate of change of the velocity vector's direction, not its magnitude. It quantifies how "tightly" the object is turning: for a given speed, a smaller radius means larger acceleration (sharper turn). For a given radius, higher speed means larger acceleration. The direction is always perpendicular to the instantaneous velocity, towards the centre.

**中文:** 向心加速度是速度矢量方向的变化率，而不是其大小的变化率。它量化了物体转弯的"紧密程度"：对于给定速度，半径越小，加速度越大（转弯越急）。对于给定半径，速度越高，加速度越大。方向始终垂直于瞬时速度，指向圆心。

### Common Misconceptions / 常见误区
- Thinking that constant speed means zero acceleration
- Believing centripetal acceleration is a force itself
- Confusing centripetal acceleration with tangential acceleration (which changes speed magnitude)
- Forgetting that $a = \omega^2 r$ applies only when $\omega$ is constant

### Exam Tips / 考试提示
**English:** Always draw a velocity vector diagram when deriving $a = v^2/r$. Remember that centripetal acceleration is always perpendicular to velocity. In exam questions, identify whether you are given $v$ or $\omega$ and use the appropriate formula.
**中文:** 在推导 $a = v^2/r$ 时，务必画出速度矢量图。记住向心加速度始终垂直于速度。在考试题目中，确定题目给出的是 $v$ 还是 $\omega$，并使用相应的公式。

> 📷 **IMAGE PROMPT — [CA-01]: Velocity Vector Diagram for Centripetal Acceleration Derivation**
> **English:** A diagram showing an object moving in a circle of radius r. Two velocity vectors v1 and v2 at two nearby points, separated by angle Δθ. Show Δv = v2 - v1 pointing towards the centre. Labels: r, v1, v2, Δθ, Δv. Style: clear vector arrows, geometric, exam-style. Importance: HIGH - essential for derivation.
> **中文:** 显示物体在半径为r的圆上运动的示意图。两个相邻点处的速度矢量v1和v2，夹角为Δθ。显示Δv = v2 - v1指向圆心。标签：r, v1, v2, Δθ, Δv。风格：清晰的矢量箭头，几何风格，考试风格。重要性：高 - 推导必备。

## 4.2 Centripetal Force / 向心力

### Explanation / 解释
**English:** [[Centripetal Force|Centripetal force]] is not a new fundamental force. It is the net force (resultant force) that must act on an object to keep it moving in a circle. According to [[Newton's Laws of Motion|Newton's Second Law]], $F = ma$, so $F = mv^2/r = m\omega^2 r$. The centripetal force is always directed towards the centre of the circle. In different scenarios, different real forces provide the centripetal force:
- **Car on a flat road:** Friction between tyres and road
- **Satellite in orbit:** Gravitational force
- **Object on a string:** Tension in the string
- **Car on a banked track:** Component of normal reaction (and possibly friction)
- **Conical pendulum:** Horizontal component of tension

**中文:** [[Centripetal Force|向心力]]不是一种新的基本力。它是使物体保持圆周运动所需的合力（净力）。根据[[Newton's Laws of Motion|牛顿第二定律]]，$F = ma$，所以 $F = mv^2/r = m\omega^2 r$。向心力始终指向圆心。在不同场景中，不同的真实力提供向心力：
- **平路上的汽车：** 轮胎与路面之间的摩擦力
- **轨道上的卫星：** 引力
- **绳子上的物体：** 绳子中的张力
- **倾斜轨道上的汽车：** 法向反作用力的分量（可能还有摩擦力）
- **圆锥摆：** 张力的水平分量

### Physical Meaning / 物理意义
**English:** Centripetal force is the "centre-seeking" force. It does no work on the object because it is always perpendicular to the displacement (velocity). Therefore, the kinetic energy and speed of the object remain constant in uniform circular motion. The magnitude of centripetal force required increases with mass, with the square of speed, and decreases with radius.

**中文:** 向心力是"向心"力。它不对物体做功，因为它始终垂直于位移（速度）。因此，在匀速圆周运动中，物体的动能和速度保持不变。所需的向心力大小随质量增加、随速度的平方增加、随半径减小而减小。

### Common Misconceptions / 常见误区
- Thinking centripetal force is an outward force (that's centrifugal, which is a fictitious force in the rotating frame)
- Believing that centripetal force is an additional force rather than the resultant of existing forces
- Forgetting to identify the real physical force providing the centripetal force in a given scenario
- Using $F = mv^2/r$ when the motion is not uniform circular motion

### Exam Tips / 考试提示
**English:** Always start by drawing a free-body diagram. Identify ALL forces acting on the object. The vector sum of these forces (resultant) must equal $mv^2/r$ towards the centre. For vertical circles, remember that speed may not be constant, so use energy conservation to find speed at different points.
**中文:** 始终从画受力分析图开始。识别作用在物体上的所有力。这些力的矢量和（合力）必须等于指向圆心的 $mv^2/r$。对于竖直圆，记住速度可能不是恒定的，因此使用能量守恒来找到不同点的速度。

## 4.3 Banked Tracks / 倾斜轨道

### Explanation / 解释
**English:** A [[Banked Tracks and Conical Pendulum|banked track]] is curved road or track that is tilted at an angle $\theta$ to the horizontal. The banking allows vehicles to travel at higher speeds around the curve without relying solely on friction. The normal reaction force $N$ has a horizontal component $N\sin\theta$ that provides the centripetal force. For the ideal banking angle (no friction needed), the horizontal component of the normal reaction provides exactly the required centripetal force: $N\sin\theta = mv^2/r$. The vertical forces balance: $N\cos\theta = mg$. Combining these gives $\tan\theta = v^2/(rg)$.

**中文:** [[Banked Tracks and Conical Pendulum|倾斜轨道]]是与水平面成角度 $\theta$ 倾斜的弯曲道路或轨道。倾斜使车辆能够在不完全依赖摩擦力的情况下以更高的速度通过弯道。法向反作用力 $N$ 的水平分量 $N\sin\theta$ 提供向心力。对于理想倾斜角（无需摩擦力），法向反作用力的水平分量恰好提供所需的向心力：$N\sin\theta = mv^2/r$。竖直方向力平衡：$N\cos\theta = mg$。结合这两个方程得到 $\tan\theta = v^2/(rg)$。

### Physical Meaning / 物理意义
**English:** The banking angle is designed for a specific "design speed". At this speed, no friction is needed. If the vehicle travels faster than the design speed, friction (acting down the slope) provides additional centripetal force. If slower, friction acts up the slope to prevent sliding down.

**中文:** 倾斜角是针对特定的"设计速度"设计的。在此速度下，不需要摩擦力。如果车辆行驶速度超过设计速度，摩擦力（沿斜坡向下作用）提供额外的向心力。如果速度较慢，摩擦力沿斜坡向上作用，以防止向下滑动。

### Common Misconceptions / 常见误区
- Thinking the normal reaction is vertical (it is perpendicular to the surface)
- Forgetting to resolve forces into horizontal and vertical components
- Confusing the direction of friction when speed is above or below design speed
- Using $N = mg$ directly without considering the banking angle

### Exam Tips / 考试提示
**English:** Draw a clear free-body diagram showing the banked surface at angle $\theta$. Resolve forces horizontally (for centripetal force) and vertically (for equilibrium). Remember that for the ideal case (no friction), $\tan\theta = v^2/(rg)$. For problems with friction, consider both cases: friction acting down or up the slope.
**中文:** 画出清晰的受力分析图，显示与水平面成角度 $\theta$ 的倾斜表面。在水平方向（向心力）和竖直方向（平衡）分解力。记住对于理想情况（无摩擦），$\tan\theta = v^2/(rg)$。对于有摩擦的问题，考虑两种情况：摩擦力沿斜坡向下或向上作用。

> 📷 **IMAGE PROMPT — [CA-02]: Banked Track Force Diagram**
> **English:** A car on a banked track at angle θ. Show forces: weight mg (down), normal reaction N (perpendicular to surface). Resolve N into Ncosθ (vertical) and Nsinθ (horizontal). Show centripetal force direction towards centre of circular path. Labels: θ, mg, N, Ncosθ, Nsinθ, r. Style: clear vector diagram, exam-style. Importance: HIGH - frequently tested.
> **中文:** 倾斜角度为θ的轨道上的汽车。显示力：重力mg（向下），法向反作用力N（垂直于表面）。将N分解为Ncosθ（竖直）和Nsinθ（水平）。显示向心力方向指向圆周路径中心。标签：θ, mg, N, Ncosθ, Nsinθ, r。风格：清晰的矢量图，考试风格。重要性：高 - 经常考查。

## 4.4 Conical Pendulum / 圆锥摆

### Explanation / 解释
**English:** A [[Banked Tracks and Conical Pendulum|conical pendulum]] consists of a mass attached to a string that moves in a horizontal circle while the string traces out a cone. The string makes an angle $\theta$ with the vertical. The tension $T$ in the string has two components: $T\cos\theta$ balances the weight $mg$, and $T\sin\theta$ provides the centripetal force $mv^2/r$. The radius of the circular path is $r = L\sin\theta$, where $L$ is the string length. Combining these gives $\tan\theta = v^2/(rg)$ or $\omega^2 = g/(L\cos\theta)$.

**中文:** [[Banked Tracks and Conical Pendulum|圆锥摆]]由一个系在绳子上的质量组成，该质量在水平面内做圆周运动，同时绳子描绘出一个圆锥。绳子与竖直方向成角度 $\theta$。绳子中的张力 $T$ 有两个分量：$T\cos\theta$ 平衡重力 $mg$，$T\sin\theta$ 提供向心力 $mv^2/r$。圆周路径的半径为 $r = L\sin\theta$，其中 $L$ 是绳长。结合这些方程得到 $\tan\theta = v^2/(rg)$ 或 $\omega^2 = g/(L\cos\theta)$。

### Physical Meaning / 物理意义
**English:** The conical pendulum demonstrates that the period of rotation depends on the vertical height $h = L\cos\theta$: $T = 2\pi\sqrt{h/g}$. This is independent of the mass and the string length, depending only on the vertical distance from the point of suspension to the plane of rotation.

**中文:** 圆锥摆表明旋转周期取决于竖直高度 $h = L\cos\theta$：$T = 2\pi\sqrt{h/g}$。这与质量和绳长无关，仅取决于悬挂点到旋转平面的竖直距离。

### Common Misconceptions / 常见误区
- Thinking the tension equals $mg$ (it is greater than $mg$ because it has a horizontal component)
- Confusing the radius $r$ with the string length $L$
- Forgetting that the centripetal force is horizontal, not along the string
- Using $v$ when $\omega$ is more convenient

### Exam Tips / 考试提示
**English:** Draw the force diagram showing tension components. Remember $r = L\sin\theta$. The centripetal force is horizontal, so resolve forces horizontally. The vertical equilibrium gives $T\cos\theta = mg$. Combine with $T\sin\theta = mv^2/r$ to eliminate $T$.
**中文:** 画出显示张力分量的力图。记住 $r = L\sin\theta$。向心力是水平的，因此在水平方向分解力。竖直平衡给出 $T\cos\theta = mg$。与 $T\sin\theta = mv^2/r$ 结合以消去 $T$。

> 📷 **IMAGE PROMPT — [CA-03]: Conical Pendulum Force Diagram**
> **English:** A mass m on a string of length L moving in a horizontal circle of radius r. String makes angle θ with vertical. Show forces: weight mg (down), tension T (along string). Resolve T into Tcosθ (vertical, balancing mg) and Tsinθ (horizontal, providing centripetal force). Show radius r = Lsinθ. Labels: L, θ, r, m, mg, T, Tcosθ, Tsinθ. Style: clear diagram, exam-style. Importance: HIGH - frequently tested.
> **中文:** 质量为m的物体在长度为L的绳子上，在半径为r的水平圆内运动。绳子与竖直方向成角度θ。显示力：重力mg（向下），张力T（沿绳子方向）。将T分解为Tcosθ（竖直，平衡mg）和Tsinθ（水平，提供向心力）。显示半径r = Lsinθ。标签：L, θ, r, m, mg, T, Tcosθ, Tsinθ。风格：清晰的图，考试风格。重要性：高 - 经常考查。

# 5. Essential Equations / 核心公式

## 5.1 Angular Speed / 角速度

$$ \omega = \frac{\Delta\theta}{\Delta t} = \frac{2\pi}{T} = 2\pi f $$

| Symbol (符号) | Meaning (EN/CN) | Unit (单位) |
|---|---|---|
| $\omega$ | Angular speed / 角速度 | rad s⁻¹ |
| $\Delta\theta$ | Angular displacement / 角位移 | rad |
| $\Delta t$ | Time interval / 时间间隔 | s |
| $T$ | Period / 周期 | s |
| $f$ | Frequency / 频率 | Hz |

## 5.2 Relationship between Linear and Angular Speed / 线速度与角速度的关系

$$ v = \omega r $$

| Symbol (符号) | Meaning (EN/CN) | Unit (单位) |
|---|---|---|
| $v$ | Linear (tangential) speed / 线（切向）速度 | m s⁻¹ |
| $\omega$ | Angular speed / 角速度 | rad s⁻¹ |
| $r$ | Radius of circular path / 圆周路径半径 | m |

## 5.3 Centripetal Acceleration / 向心加速度

$$ a = \frac{v^2}{r} = \omega^2 r = v\omega $$

| Symbol (符号) | Meaning (EN/CN) | Unit (单位) |
|---|---|---|
| $a$ | Centripetal acceleration / 向心加速度 | m s⁻² |
| $v$ | Linear speed / 线速度 | m s⁻¹ |
| $\omega$ | Angular speed / 角速度 | rad s⁻¹ |
| $r$ | Radius / 半径 | m |

**Derivation / 推导:**
From velocity vector diagram: $\Delta v \approx v\Delta\theta$ for small $\Delta\theta$. Since $\Delta\theta = \omega\Delta t$, $\Delta v = v\omega\Delta t$. Therefore $a = \Delta v/\Delta t = v\omega = v^2/r = \omega^2 r$.

**Conditions / 适用条件:**
- Uniform circular motion (constant speed)
- Object moving in a perfect circle

**Limitations / 局限性:**
- Does not apply to non-circular curved paths (use radius of curvature instead)
- Does not account for tangential acceleration (changing speed)

## 5.4 Centripetal Force / 向心力

$$ F = \frac{mv^2}{r} = m\omega^2 r = mv\omega $$

| Symbol (符号) | Meaning (EN/CN) | Unit (单位) |
|---|---|---|
| $F$ | Centripetal force / 向心力 | N |
| $m$ | Mass of object / 物体质量 | kg |
| $v$ | Linear speed / 线速度 | m s⁻¹ |
| $\omega$ | Angular speed / 角速度 | rad s⁻¹ |
| $r$ | Radius / 半径 | m |

**Derivation / 推导:**
From [[Newton's Laws of Motion|Newton's Second Law]]: $F = ma$. Substituting $a = v^2/r$ gives $F = mv^2/r$.

**Conditions / 适用条件:**
- Uniform circular motion
- Net force (resultant) towards centre

**Limitations / 局限性:**
- $F$ is the resultant force, not a separate force
- For non-uniform circular motion, there is also a tangential component

## 5.5 Banked Track (Ideal, No Friction) / 倾斜轨道（理想，无摩擦）

$$ \tan\theta = \frac{v^2}{rg} $$

| Symbol (符号) | Meaning (EN/CN) | Unit (单位) |
|---|---|---|
| $\theta$ | Banking angle / 倾斜角 | ° or rad |
| $v$ | Design speed / 设计速度 | m s⁻¹ |
| $r$ | Radius of curve / 弯道半径 | m |
| $g$ | Acceleration due to gravity / 重力加速度 | m s⁻² |

**Derivation / 推导:**
Horizontal: $N\sin\theta = mv^2/r$
Vertical: $N\cos\theta = mg$
Dividing: $\tan\theta = v^2/(rg)$

## 5.6 Conical Pendulum / 圆锥摆

$$ \tan\theta = \frac{v^2}{rg} \quad \text{or} \quad \omega^2 = \frac{g}{L\cos\theta} $$

$$ T = 2\pi\sqrt{\frac{L\cos\theta}{g}} = 2\pi\sqrt{\frac{h}{g}} $$

| Symbol (符号) | Meaning (EN/CN) | Unit (单位) |
|---|---|---|
| $\theta$ | Angle with vertical / 与竖直方向夹角 | ° or rad |
| $v$ | Linear speed / 线速度 | m s⁻¹ |
| $r$ | Radius of horizontal circle / 水平圆半径 | m |
| $L$ | String length / 绳长 | m |
| $h$ | Vertical height ($L\cos\theta$) / 竖直高度 | m |
| $T$ | Period / 周期 | s |

**Derivation / 推导:**
Horizontal: $T\sin\theta = mv^2/r$
Vertical: $T\cos\theta = mg$
Dividing: $\tan\theta = v^2/(rg)$
Since $r = L\sin\theta$: $\tan\theta = v^2/(L\sin\theta \cdot g)$ → $v^2 = gL\sin\theta\tan\theta$
Using $v = \omega r = \omega L\sin\theta$: $\omega^2 L^2\sin^2\theta = gL\sin\theta\tan\theta$ → $\omega^2 = g/(L\cos\theta)$
Period: $T = 2\pi/\omega = 2\pi\sqrt{L\cos\theta/g} = 2\pi\sqrt{h/g}$

# 6. Graphs and Relationships / 图表与关系

## 6.1 Centripetal Acceleration vs Radius (Constant Speed) / 向心加速度与半径的关系（恒定速度）

$$ a = \frac{v^2}{r} $$

**Axes / 坐标轴:**
- x-axis: Radius $r$ / 半径 $r$ (m)
- y-axis: Centripetal acceleration $a$ / 向心加速度 $a$ (m s⁻²)

**Shape / 形状:**
- Inverse relationship: $a \propto 1/r$ (hyperbola)
- As $r$ increases, $a$ decreases

**Gradient Meaning / 斜率意义:**
- Gradient = $da/dr = -v^2/r^2$
- Not constant; steeper at small $r$

**Area Meaning / 面积意义:**
- Area under $a$ vs $1/r$ graph = $v^2$ (constant)
- Area under $a$ vs $r$ graph has no direct physical meaning

**Exam Interpretation / 考试解读:**
- For constant $v$, smaller radius means much larger acceleration
- Used to explain why tight turns require more centripetal force

## 6.2 Centripetal Acceleration vs Angular Speed (Constant Radius) / 向心加速度与角速度的关系（恒定半径）

$$ a = \omega^2 r $$

**Axes / 坐标轴:**
- x-axis: Angular speed $\omega$ / 角速度 $\omega$ (rad s⁻¹)
- y-axis: Centripetal acceleration $a$ / 向心加速度 $a$ (m s⁻²)

**Shape / 形状:**
- Quadratic relationship: $a \propto \omega^2$ (parabola)
- If plotting $a$ vs $\omega^2$, it is a straight line through origin

**Gradient Meaning / 斜率意义:**
- Gradient of $a$ vs $\omega^2$ graph = $r$ (radius)
- Gradient of $a$ vs $\omega$ graph = $2\omega r$ (not constant)

**Area Meaning / 面积意义:**
- Area under $a$ vs $\omega$ graph has no direct physical meaning

**Exam Interpretation / 考试解读:**
- Doubling $\omega$ quadruples $a$
- Straight line through origin for $a$ vs $\omega^2$ confirms relationship

## 6.3 Centripetal Force vs Speed (Constant Radius) / 向心力与速度的关系（恒定半径）

$$ F = \frac{mv^2}{r} $$

**Axes / 坐标轴:**
- x-axis: Speed $v$ / 速度 $v$ (m s⁻¹)
- y-axis: Centripetal force $F$ / 向心力 $F$ (N)

**Shape / 形状:**
- Quadratic relationship: $F \propto v^2$ (parabola)
- If plotting $F$ vs $v^2$, it is a straight line through origin

**Gradient Meaning / 斜率意义:**
- Gradient of $F$ vs $v^2$ graph = $m/r$
- Can be used to determine mass or radius experimentally

**Area Meaning / 面积意义:**
- Area under $F$ vs $v$ graph has no direct physical meaning

**Exam Interpretation / 考试解读:**
- Doubling speed quadruples required centripetal force
- Explains why high-speed cornering is dangerous

> 📷 **IMAGE PROMPT — [CA-04]: Graphs of Centripetal Relationships**
> **English:** Three graphs side by side: (1) a vs r showing hyperbola, (2) a vs ω² showing straight line through origin, (3) F vs v² showing straight line through origin. All with labelled axes and units. Style: clear, exam-style graphs. Importance: MEDIUM - helps visual understanding.
> **中文:** 并排的三个图：(1) a vs r 显示双曲线，(2) a vs ω² 显示通过原点的直线，(3) F vs v² 显示通过原点的直线。所有图都有标注的坐标轴和单位。风格：清晰，考试风格。重要性：中 - 有助于视觉理解。

# 7. Required Diagrams / 必备图表

## 7.1 Velocity Vector Diagram for Centripetal Acceleration Derivation / 向心加速度推导的速度矢量图

> 📷 **IMAGE PROMPT — [CA-05]: Velocity Vector Derivation Diagram**
> **English:** A circle of radius r with an object at two nearby positions P and Q separated by angle Δθ. At P, velocity vector v₁ (tangent to circle). At Q, velocity vector v₂ (tangent to circle). Show Δv = v₂ - v₁ by placing vectors tail-to-tail: v₂ and -v₁, with Δv pointing towards centre. Labels: r, v₁, v₂, Δθ, Δv, centre O. Style: geometric, clear vector arrows, exam-style. Importance: HIGH - essential for derivation in both boards.
> **中文:** 半径为r的圆，物体在两个相邻位置P和Q，夹角为Δθ。在P处，速度矢量v₁（与圆相切）。在Q处，速度矢量v₂（与圆相切）。通过将矢量尾对尾放置来显示Δv = v₂ - v₁：v₂和-v₁，Δv指向圆心。标签：r, v₁, v₂, Δθ, Δv, 圆心O。风格：几何风格，清晰的矢量箭头，考试风格。重要性：高 - 两个考试局推导必备。

## 7.2 Free-Body Diagram for Car on Banked Track / 倾斜轨道上汽车的受力分析图

> 📷 **IMAGE PROMPT — [CA-06]: Banked Track Free-Body Diagram**
> **English:** A car (simplified as a block) on a banked track inclined at angle θ to horizontal. Show three forces: weight mg (vertically downward), normal reaction N (perpendicular to track surface), friction f (parallel to track surface, direction depends on speed relative to design speed). Show the horizontal component Nsinθ providing centripetal force towards centre of circular path (radius r). Labels: θ, mg, N, Nsinθ, Ncosθ, f, r, centre. Style: clear vector diagram, exam-style. Importance: HIGH - frequently tested.
> **中文:** 倾斜角度为θ的轨道上的汽车（简化为方块）。显示三个力：重力mg（竖直向下），法向反作用力N（垂直于轨道表面），摩擦力f（平行于轨道表面，方向取决于速度相对于设计速度）。显示水平分量Nsinθ提供指向圆周路径中心（半径r）的向心力。标签：θ, mg, N, Nsinθ, Ncosθ, f, r, 中心。风格：清晰的矢量图，考试风格。重要性：高 - 经常考查。

## 7.3 Conical Pendulum Force Diagram / 圆锥摆受力分析图

> 📷 **IMAGE PROMPT — [CA-07]: Conical Pendulum Diagram**
> **English:** A mass m attached to a string of length L, moving in a horizontal circle of radius r. The string makes angle θ with vertical. Show: weight mg (down), tension T (along string towards suspension point). Resolve T into Tcosθ (vertical, balancing mg) and Tsinθ (horizontal, providing centripetal force). Show radius r = Lsinθ and vertical height h = Lcosθ. Labels: L, θ, r, h, m, mg, T, Tcosθ, Tsinθ, centre of circle. Style: clear diagram, exam-style. Importance: HIGH - frequently tested.
> **中文:** 质量为m的物体系在长度为L的绳子上，在半径为r的水平圆内运动。绳子与竖直方向成角度θ。显示：重力mg（向下），张力T（沿绳子指向悬挂点）。将T分解为Tcosθ（竖直，平衡mg）和Tsinθ（水平，提供向心力）。显示半径r = Lsinθ和竖直高度h = Lcosθ。标签：L, θ, r, h, m, mg, T, Tcosθ, Tsinθ, 圆心。风格：清晰的图，考试风格。重要性：高 - 经常考查。

## 7.4 Forces on a Mass in Vertical Circular Motion / 竖直圆周运动中物体上的力

> 📷 **IMAGE PROMPT — [CA-08]: Vertical Circular Motion Force Diagram**
> **English:** A mass m on a string moving in a vertical circle of radius r. Show the mass at four positions: top, bottom, left, right. At each position, show forces: weight mg (down) and tension T (along string towards centre). At top: T + mg = mv²/r (both down). At bottom: T - mg = mv²/r (T up, mg down). At sides: T = mv²/r (horizontal), mg vertical. Labels: r, m, mg, T, v at each position. Style: clear diagram, exam-style. Importance: MEDIUM - tested in both boards.
> **中文:** 质量为m的物体在绳子上做竖直圆周运动，半径为r。显示物体在四个位置：顶部、底部、左侧、右侧。在每个位置显示力：重力mg（向下）和张力T（沿绳子指向圆心）。在顶部：T + mg = mv²/r（都向下）。在底部：T - mg = mv²/r（T向上，mg向下）。在侧面：T = mv²/r（水平），mg竖直。标签：r, m, mg, T, 每个位置的v。风格：清晰的图，考试风格。重要性：中 - 两个考试局都考查。

# 8. Worked Examples / 典型例题

## Example 1: Car on a Banked Track / 倾斜轨道上的汽车

### Question / 题目
**English:** A car of mass 1200 kg travels around a circular track of radius 80 m. The track is banked at an angle of 15° to the horizontal. Calculate:
(a) The design speed at which no friction is required.
(b) The normal reaction force on the car at this speed.
(c) The maximum speed at which the car can travel without slipping if the coefficient of friction between the tyres and the track is 0.30.

**中文:** 一辆质量为1200 kg的汽车在半径为80 m的圆形轨道上行驶。轨道与水平面成15°角倾斜。计算：
(a) 不需要摩擦力的设计速度。
(b) 在此速度下汽车受到的法向反作用力。
(c) 如果轮胎与轨道之间的摩擦系数为0.30，汽车在不打滑的情况下可以行驶的最大速度。

### Image Prompt / 图片提示
> 📷 **IMAGE PROMPT — [CA-09]: Banked Track Example Diagram**
> **English:** A car on a banked track at 15° with radius 80 m. Show forces: weight mg, normal N, friction f (acting down the slope for part c). Labels: 15°, 80 m, 1200 kg. Style: clear diagram for exam question. Importance: HIGH - typical exam question.
> **中文:** 倾斜角度为15°、半径为80 m的轨道上的汽车。显示力：重力mg，法向反作用力N，摩擦力f（在部分c中沿斜坡向下作用）。标签：15°, 80 m, 1200 kg。风格：考试题目用的清晰图。重要性：高 - 典型考试题。

### Solution / 解答

**Part (a): Design speed / 设计速度**

For ideal banking (no friction):
$$\tan\theta = \frac{v^2}{rg}$$

$$v^2 = rg\tan\theta = 80 \times 9.81 \times \tan(15^\circ)$$

$$v^2 = 80 \times 9.81 \times 0.2679 = 210.3$$

$$v = \sqrt{210.3} = 14.5 \text{ m s}^{-1}$$

**Part (b): Normal reaction / 法向反作用力**

From vertical equilibrium:
$$N\cos\theta = mg$$

$$N = \frac{mg}{\cos\theta} = \frac{1200 \times 9.81}{\cos(15^\circ)}$$

$$N = \frac{11772}{0.9659} = 12187 \text{ N} \approx 1.22 \times 10^4 \text{ N}$$

**Part (c): Maximum speed with friction / 有摩擦时的最大速度**

At maximum speed, friction acts down the slope (to provide additional centripetal force). The maximum friction force is $f = \mu N$.

Horizontal components provide centripetal force:
$$N\sin\theta + f\cos\theta = \frac{mv^2}{r}$$

Vertical equilibrium:
$$N\cos\theta = mg + f\sin\theta$$

Substituting $f = \mu N$:
$$N\cos\theta = mg + \mu N\sin\theta$$
$$N(\cos\theta - \mu\sin\theta) = mg$$
$$N = \frac{mg}{\cos\theta - \mu\sin\theta}$$

$$N = \frac{1200 \times 9.81}{\cos(15^\circ) - 0.30 \times \sin(15^\circ)}$$
$$N = \frac{11772}{0.9659 - 0.30 \times 0.2588}$$
$$N = \frac{11772}{0.9659 - 0.0776} = \frac{11772}{0.8883} = 13252 \text{ N}$$

Now using the horizontal equation:
$$N\sin\theta + \mu N\cos\theta = \frac{mv^2}{r}$$
$$N(\sin\theta + \mu\cos\theta) = \frac{mv^2}{r}$$
$$v^2 = \frac{rN(\sin\theta + \mu\cos\theta)}{m}$$

$$v^2 = \frac{80 \times 13252 \times (\sin(15^\circ) + 0.30 \times \cos(15^\circ))}{1200}$$
$$v^2 = \frac{80 \times 13252 \times (0.2588 + 0.30 \times 0.9659)}{1200}$$
$$v^2 = \frac{80 \times 13252 \times (0.2588 + 0.2898)}{1200}$$
$$v^2 = \frac{80 \times 13252 \times 0.5486}{1200}$$
$$v^2 = \frac{581,600}{1200} = 484.7$$
$$v = \sqrt{484.7} = 22.0 \text{ m s}^{-1}$$

### Final Answer / 最终答案
(a) Design speed = 14.5 m s⁻¹
(b) Normal reaction = 1.22 × 10⁴ N
(c) Maximum speed with friction = 22.0 m s⁻¹

### Examiner Notes / 考官点评
**English:** 
- Part (a) is straightforward using $\tan\theta = v^2/(rg)$. Many candidates forget to use radians or degrees correctly.
- Part (b) requires recognising that $N\cos\theta = mg$, not $N = mg$.
- Part (c) is challenging. Candidates must correctly identify that friction acts down the slope at maximum speed. The two equations (horizontal and vertical) must be solved simultaneously. Common mistakes include using $N = mg$ directly or getting the direction of friction wrong.

**中文:**
- 部分(a)直接使用 $\tan\theta = v^2/(rg)$。许多考生忘记正确使用弧度或角度。
- 部分(b)需要认识到 $N\cos\theta = mg$，而不是 $N = mg$。
- 部分(c)具有挑战性。考生必须正确识别出在最大速度时摩擦力沿斜坡向下作用。必须同时求解两个方程（水平和竖直）。常见错误包括直接使用 $N = mg$ 或弄错摩擦力的方向。

## Example 2: Conical Pendulum / 圆锥摆

### Question / 题目
**English:** A conical pendulum consists of a mass of 0.50 kg attached to a light string of length 1.2 m. The mass rotates in a horizontal circle with the string making an angle of 30° with the vertical. Calculate:
(a) The tension in the string.
(b) The linear speed of the mass.
(c) The period of rotation.

**中文:** 一个圆锥摆由一个质量为0.50 kg的物体和一根长度为1.2 m的轻绳组成。物体在水平面内旋转，绳子与竖直方向成30°角。计算：
(a) 绳子中的张力。
(b) 物体的线速度。
(c) 旋转周期。

### Image Prompt / 图片提示
> 📷 **IMAGE PROMPT — [CA-10]: Conical Pendulum Example Diagram**
> **English:** A conical pendulum with string length 1.2 m, angle 30° with vertical, mass 0.50 kg. Show forces: weight mg, tension T. Show radius r = Lsin30° = 0.6 m, height h = Lcos30° = 1.04 m. Labels: 1.2 m, 30°, 0.50 kg, r, h. Style: clear diagram for exam question. Importance: HIGH - typical exam question.
> **中文:** 圆锥摆，绳长1.2 m，与竖直方向夹角30°，质量0.50 kg。显示力：重力mg，张力T。显示半径r = Lsin30° = 0.6 m，高度h = Lcos30° = 1.04 m。标签：1.2 m, 30°, 0.50 kg, r, h。风格：考试题目用的清晰图。重要性：高 - 典型考试题。

### Solution / 解答

**Part (a): Tension in the string / 绳子中的张力**

Vertical equilibrium:
$$T\cos\theta = mg$$

$$T = \frac{mg}{\cos\theta} = \frac{0.50 \times 9.81}{\cos(30^\circ)}$$

$$T = \frac{4.905}{0.8660} = 5.66 \text{ N}$$

**Part (b): Linear speed / 线速度**

The radius of the horizontal circle:
$$r = L\sin\theta = 1.2 \times \sin(30^\circ) = 1.2 \times 0.50 = 0.60 \text{ m}$$

Horizontal component of tension provides centripetal force:
$$T\sin\theta = \frac{mv^2}{r}$$

$$v^2 = \frac{rT\sin\theta}{m} = \frac{0.60 \times 5.66 \times \sin(30^\circ)}{0.50}$$

$$v^2 = \frac{0.60 \times 5.66 \times 0.50}{0.50} = 0.60 \times 5.66 = 3.40$$

$$v = \sqrt{3.40} = 1.84 \text{ m s}^{-1}$$

**Alternative method using $\tan\theta$:**
$$\tan\theta = \frac{v^2}{rg}$$

$$v^2 = rg\tan\theta = 0.60 \times 9.81 \times \tan(30^\circ)$$

$$v^2 = 0.60 \times 9.81 \times 0.5774 = 3.40$$

$$v = 1.84 \text{ m s}^{-1}$$

**Part (c): Period of rotation / 旋转周期**

$$T = \frac{2\pi r}{v} = \frac{2\pi \times 0.60}{1.84} = \frac{3.77}{1.84} = 2.05 \text{ s}$$

**Alternative method:**
$$T = 2\pi\sqrt{\frac{L\cos\theta}{g}} = 2\pi\sqrt{\frac{1.2 \times \cos(30^\circ)}{9.81}}$$

$$T = 2\pi\sqrt{\frac{1.2 \times 0.8660}{9.81}} = 2\pi\sqrt{\frac{1.039}{9.81}}$$

$$T = 2\pi\sqrt{0.1059} = 2\pi \times 0.3255 = 2.05 \text{ s}$$

### Final Answer / 最终答案
(a) Tension = 5.66 N
(b) Linear speed = 1.84 m s⁻¹
(c) Period = 2.05 s

### Examiner Notes / 考官点评
**English:**
- Part (a) is straightforward using vertical equilibrium. Common mistake: thinking $T = mg$.
- Part (b) can be solved using either $T\sin\theta = mv^2/r$ or $\tan\theta = v^2/(rg)$. Both methods are acceptable.
- Part (c) can be solved using $T = 2\pi r/v$ or the derived formula $T = 2\pi\sqrt{h/g}$. The derived formula is quicker and shows understanding.
- The period is independent of mass - a key insight for conical pendulums.

**中文:**
- 部分(a)直接使用竖直平衡。常见错误：认为 $T = mg$。
- 部分(b)可以使用 $T\sin\theta = mv^2/r$ 或 $\tan\theta = v^2/(rg)$ 求解。两种方法都可以接受。
- 部分(c)可以使用 $T = 2\pi r/v$ 或推导公式 $T = 2\pi\sqrt{h/g}$ 求解。推导公式更快，并能显示理解程度。
- 周期与质量无关——这是圆锥摆的一个关键见解。

# 9. Past Paper Question Types / 历年真题题型

| Question Type / 题型 | Frequency / 频率 | Difficulty / 难度 | Past Paper References / 真题索引 |
|---|---|---|---|
| Derivation of $a = v^2/r$ using velocity vectors | High / 高 | Medium / 中 | 📝 *待填入* |
| Calculation of centripetal acceleration/force (direct substitution) | Very High / 非常高 | Easy / 易 | 📝 *待填入* |
| Identifying source of centripetal force in different scenarios | High / 高 | Medium / 中 | 📝 *待填入* |
| Banked track problems (ideal and with friction) | High / 高 | Hard / 难 | 📝 *待填入* |
| Conical pendulum calculations | Medium / 中 | Medium-Hard / 中难 | 📝 *待填入* |
| Vertical circular motion (tension at top/bottom) | Medium / 中 | Hard / 难 | 📝 *待填入* |
| Multiple choice on angular/linear relationships | Very High / 非常高 | Easy-Medium / 易中 | 📝 *待填入* |
| Graph interpretation ($a$ vs $r$, $F$ vs $v^2$) | Medium / 中 | Medium / 中 | 📝 *待填入* |
| Practical: measuring centripetal force with whirling bung | Low-Medium / 低中 | Medium / 中 | 📝 *待填入* |

> 📝 **题库整理中 / Question Bank Under Construction:** 本表格中的真题索引（Past Paper References）正在整理中。我们将逐步添加CAIE 9702和Edexcel IAL的具体年份和题号。请定期查看更新。如需特定年份的真题，请参考官方试卷或联系您的老师。

**Common Command Words / 常见指令词:**
- **Define / 定义:** Give the precise meaning (e.g., "Define angular speed")
- **Derive / 推导:** Show the steps to obtain an equation (e.g., "Derive $a = v^2/r$")
- **Calculate / 计算:** Use given data to find a numerical answer
- **Explain / 解释:** Give reasons or causes (e.g., "Explain why centripetal force does no work")
- **State / 陈述:** Give a brief answer without explanation
- **Sketch / 画草图:** Draw a graph or diagram showing key features
- **Determine / 确定:** Find a value using given information

# 10. Practical Skills Connections / 实验技能链接

**English:** The topic of centripetal acceleration and force connects to practical work in several ways:

1. **Whirling Bung Experiment (CAIE Paper 3/5, Edexcel Unit 3/6):**
   - A rubber bung is whirled in a horizontal circle on a string
   - The tension is provided by hanging masses
   - Measure: radius $r$, time for $N$ revolutions, mass of bung $m$, hanging mass $M$
   - Verify $F = mv^2/r$ by comparing calculated centripetal force with weight of hanging masses
   - **Uncertainties:** Timing errors (±0.1 s for 20 revolutions → ±0.005 s per revolution), radius measurement (±0.5 cm), mass measurement (±0.1 g)
   - **Graph:** Plot $F$ vs $v^2$ (should be straight line through origin with gradient $m/r$)

2. **Centripetal Force Apparatus:**
   - Rotating platform with spring balance
   - Measure force required for different speeds and radii
   - Verify $F \propto v^2$ and $F \propto 1/r$

3. **Banked Track Simulation:**
   - Use a marble on a curved track
   - Measure speed and radius to verify $\tan\theta = v^2/(rg)$

4. **Key Measurements and Uncertainties / 关键测量与不确定度:**
   - **Time period:** Use a stopwatch to measure time for multiple revolutions to reduce percentage uncertainty
   - **Radius:** Measure from centre of circle to centre of mass of bung
   - **Speed:** Calculate from $v = 2\pi r/T$ (indirect measurement)
   - **Force:** For whirling bung, $F = Mg$ (weight of hanging masses)

**中文:** 向心加速度和力的主题在多个方面与实验工作相关：

1. **旋转塞子实验（CAIE Paper 3/5, Edexcel Unit 3/6）：**
   - 橡胶塞子在绳子上做水平圆周运动
   - 张力由悬挂的质量提供
   - 测量：半径 $r$，N次旋转的时间，塞子质量 $m$，悬挂质量 $M$
   - 通过比较计算出的向心力与悬挂质量的重量来验证 $F = mv^2/r$
   - **不确定度：** 计时误差（20次旋转±0.1秒 → 每次旋转±0.005秒），半径测量（±0.5 cm），质量测量（±0.1 g）
   - **图表：** 绘制 $F$ vs $v^2$（应为通过原点的直线，斜率为 $m/r$）

2. **向心力装置：**
   - 带弹簧秤的旋转平台
   - 测量不同速度和半径所需的力
   - 验证 $F \propto v^2$ 和 $F \propto 1/r$

3. **倾斜轨道模拟：**
   - 在弯曲轨道上使用弹珠
   - 测量速度和半径以验证 $\tan\theta = v^2/(rg)$

4. **关键测量与不确定度：**
   - **周期：** 使用秒表测量多次旋转的时间，以减少百分比不确定度
   - **半径：** 从圆心测量到塞子质心
   - **速度：** 从 $v = 2\pi r/T$ 计算（间接测量）
   - **力：** 对于旋转塞子，$F = Mg$（悬挂质量的重量）

> 📋 **CIE Only:** CAIE Paper 3 (Practical) may require plotting $T^2$ vs $m$ or $v^2$ vs $F$ and calculating gradient. Paper 5 (Planning) may ask for experimental design to verify centripetal force equations.
> 📋 **Edexcel Only:** Edexcel Unit 3/6 may include questions on the whirling bung experiment with error analysis and improvements. Core Practical 13 (Edexcel) involves investigating circular motion.

# 11. Concept Map / 概念图谱

```mermaid
graph TD
    A[Circular Motion / 圆周运动] --> B[Angular Measures / 角度测量]
    A --> C[Centripetal Acceleration / 向心加速度]
    A --> D[Centripetal Force / 向心力]
    
    B --> B1[Angular Displacement θ / 角位移]
    B --> B2[Angular Speed ω / 角速度]
    B --> B3[Period T & Frequency f / 周期与频率]
    
    C --> C1[a = v²/r = ω²r]
    C --> C2[Derivation from velocity vectors / 从速度矢量推导]
    C --> C3[Direction: towards centre / 方向：指向圆心]
    
    D --> D1[F = mv²/r = mω²r]
    D --> D2[Source identification / 来源识别]
    D --> D3[Applications / 应用]
    
    D2 --> D2a[Tension / 张力]
    D2 --> D2b[Friction / 摩擦力]
    D2 --> D2c[Gravity / 重力]
    D2 --> D2d[Normal Reaction / 法向反作用力]
    
    D3 --> D3a[Banked Tracks / 倾斜轨道]
    D3 --> D3b[Conical Pendulum / 圆锥摆]
    D3 --> D3c[Vertical Circles / 竖直圆]
    D3 --> D3d[Orbits / 轨道]
    
    D3a --> D3a1[Ideal: tanθ = v²/rg]
    D3a --> D3a2[With friction]
    
    D3b --> D3b1[T = 2π√(h/g)]
    D3b --> D3b2[Independent of mass]
    
    %% Prerequisites
    E[Newton's Laws of Motion / 牛顿运动定律] --> D
    F[Kinematics / 运动学] --> C
    
    %% Related Topics
    D3d --> G[Gravitational Force and Field / 引力与场]
    G --> H[Circular Orbits / 圆形轨道]
    
    %% Styling
    classDef core fill:#f9f,stroke:#333,stroke-width:2px
    classDef formula fill:#bbf,stroke:#333,stroke-width:1px
    classDef app fill:#bfb,stroke:#333,stroke-width:1px
    class A,B,C,D core
    class C1,D1 formula
    class D3a,D3b,D3c,D3d app
```

# 12. Examiner Insights / 考官洞察

**English:**

**Most Tested Ideas (CAIE 9702):**
1. **Derivation of $a = v^2/r$** — Appears in almost every exam cycle. Candidates must draw velocity vectors and show $\Delta v$ pointing towards centre.
2. **Identifying centripetal force source** — Common in multiple choice. E.g., "What provides the centripetal force for a car on a banked track?"
3. **Banked track calculations** — Both ideal (no friction) and with friction. The friction direction is a common trap.
4. **Conical pendulum** — Period formula $T = 2\pi\sqrt{h/g}$ is frequently tested.
5. **Vertical circular motion** — Finding tension at top and bottom of a vertical circle.

**Most Tested Ideas (Edexcel IAL):**
1. **Derivation using calculus** — Edexcel may require differentiation of position vectors $r = (r\cos\omega t, r\sin\omega t)$.
2. **Banked tracks with friction** — More emphasis on maximum/minimum speeds.
3. **Conical pendulum** — Often combined with energy considerations.
4. **Practical: whirling bung** — Error analysis and improvements.

**Mark Scheme Wording / 评分方案措辞:**
- "The centripetal force is the **resultant** force towards the centre" — NOT "a force towards the centre"
- "The acceleration is **directed towards** the centre" — NOT "the acceleration is towards the centre"
- For derivations: "Correct vector diagram" + "$\Delta v = v\Delta\theta$" + "$a = \Delta v/\Delta t = v\omega = v^2/r$"

**Common Lost Marks / 常见失分点:**
1. Forgetting to state direction of centripetal acceleration/force
2. Using $v = \omega r$ incorrectly (mixing $v$ and $\omega$)
3. Not resolving forces correctly on banked tracks
4. Confusing centripetal force with centrifugal force
5. Using $F = mv^2/r$ when the motion is not uniform circular motion
6. Not converting degrees to radians when required

**High-Scoring Structures / 高分答题结构:**
- **Derivation questions:** Draw diagram → Label vectors → Show $\Delta v$ → Write $\Delta v = v\Delta\theta$ → Substitute $\Delta\theta = \omega\Delta t$ → Get $a = v\omega = v^2/r$
- **Calculation questions:** State formula → Substitute values → Calculate → State answer with units
- **Explanation questions:** Identify force → State direction → Write equation → Explain physical meaning

**中文:**

**最常考的概念（CAIE 9702）：**
1. **推导 $a = v^2/r$** — 几乎每个考试周期都会出现。考生必须画出速度矢量并显示 $\Delta v$ 指向圆心。
2. **识别向心力来源** — 常见于选择题。例如："什么为倾斜轨道上的汽车提供向心力？"
3. **倾斜轨道计算** — 包括理想情况（无摩擦）和有摩擦的情况。摩擦力方向是常见的陷阱。
4. **圆锥摆** — 周期公式 $T = 2\pi\sqrt{h/g}$ 经常被考查。
5. **竖直圆周运动** — 求竖直圆顶部和底部的张力。

**最常考的概念（Edexcel IAL）：**
1. **使用微积分推导** — Edexcel 可能要求对位置矢量 $r = (r\cos\omega t, r\sin\omega t)$ 进行微分。
2. **有摩擦的倾斜轨道** — 更强调最大/最小速度。
3. **圆锥摆** — 常与能量考虑结合。
4. **实验：旋转塞子** — 误差分析和改进。

**评分方案措辞：**
- "向心力是**指向圆心的合力**" — 不是"指向圆心的力"
- "加速度**方向指向**圆心" — 不是"加速度指向圆心"
- 对于推导："正确的矢量图" + "$\Delta v = v\Delta\theta$" + "$a = \Delta v/\Delta t = v\omega = v^2/r$"

**常见失分点：**
1. 忘记说明向心加速度/力的方向
2. 错误使用 $v = \omega r$（混淆 $v$ 和 $\omega$）
3. 在倾斜轨道上未正确分解力
4. 混淆向心力与离心力
5. 在非匀速圆周运动中使用 $F = mv^2/r$
6. 需要时未将角度转换为弧度

**高分答题结构：**
- **推导题：** 画图 → 标注矢量 → 显示 $\Delta v$ → 写出 $\Delta v = v\Delta\theta$ → 代入 $\Delta\theta = \omega\Delta t$ → 得到 $a = v\omega = v^2/r$
- **计算题：** 写出公式 → 代入数值 → 计算 → 写出带单位的答案
- **解释题：** 识别力 → 说明方向 → 写出方程 → 解释物理意义

# 13. Quick Revision Sheet / 速查表

| Category / 类别 | Key Points / 要点 |
|---|---|
| **Key Definitions / 关键定义** | **Angular speed:** $\omega = \Delta\theta/\Delta t$ (rad s⁻¹) / 角速度 |
| | **Centripetal acceleration:** Acceleration towards centre, magnitude $a = v^2/r$ / 向心加速度 |
| | **Centripetal force:** Resultant force towards centre, $F = mv^2/r$ / 向心力 |
| **Essential Equations / 核心公式** | $v = \omega r$ |
| | $a = v^2/r = \omega^2 r$ |
| | $F = mv^2/r = m\omega^2 r$ |
| | $\tan\theta = v^2/(rg)$ (banked track, ideal) / 倾斜轨道（理想） |
| | $T = 2\pi\sqrt{h/g}$ (conical pendulum) / 圆锥摆周期 |
| **Key Relationships / 关键关系** | $a \propto v^2$ (constant $r$) / 加速度与速度平方成正比 |
| | $a \propto 1/r$ (constant $v$) / 加速度与半径成反比 |
| | $F \propto v^2$ (constant $r$) / 向心力与速度平方成正比 |
| **Common Force Sources / 常见力来源** | **Car on flat road:** Friction / 平路汽车：摩擦力 |
| | **Satellite:** Gravity / 卫星：重力 |
| | **Object on string:** Tension / 绳子上的物体：张力 |
| | **Car on banked track:** Normal reaction component / 倾斜轨道汽车：法向反作用力分量 |
| | **Conical pendulum:** Tension horizontal component / 圆锥摆：张力水平分量 |
| **Key Directions / 关键方向** | Velocity: Tangent to circle / 速度：与圆相切 |
| | Acceleration: Towards centre / 加速度：指向圆心 |
| | Force: Towards centre / 力：指向圆心 |
| **Common Mistakes / 常见错误** | Thinking constant speed = zero acceleration / 认为恒定速度 = 零加速度 |
| | Calling centripetal force a "new" force / 称向心力为"新"力 |
| | Using $N = mg$ on banked tracks / 在倾斜轨道上使用 $N = mg$ |
| | Confusing $v$ and $\omega$ / 混淆 $v$ 和 $\omega$ |
| **Exam Tips / 考试提示** | Always draw free-body diagram / 始终画受力分析图 |
| | Identify ALL forces, then find resultant towards centre / 识别所有力，然后求指向圆心的合力 |
| | For banked tracks, resolve horizontally and vertically / 对于倾斜轨道，水平和竖直分解 |
| | For vertical circles, use energy conservation for speed / 对于竖直圆，使用能量守恒求速度 |
| **Practical / 实验** | Whirling bung: $F = Mg$ vs $mv^2/r$ / 旋转塞子 |
| | Measure $T$ for multiple revolutions / 测量多次旋转的周期 |
| | Plot $F$ vs $v^2$: straight line through origin / 绘制 $F$ vs $v^2$：通过原点的直线 |

# 14. Metadata / 元数据

```yaml
title:
  en: "Centripetal Acceleration and Force"
  cn: "向心加速度与向心力"
subject: Physics
syllabus: [CAIE 9702, Edexcel IAL]
cie_ref: "14.2 (a-d)"
edexcel_ref: "WPH14 U4: 5.5-5.9"
level: A2
node_type: topic_hub
difficulty: advanced
prerequisites:
  - "[[Angular Measures]]"
  - "[[Newton's Laws of Motion]]"
related_topics:
  - "[[Gravitational Force and Field]]"
  - "[[Circular Orbits]]"
sub_topics:
  - "[[Centripetal Acceleration Formula]]"
  - "[[Centripetal Force]]"
  - "[[Banked Tracks and Conical Pendulum]]"
formula_count: 6
diagram_count: 10
exam_frequency: very_high
language: bilingual_en_cn
last_updated: 2024-01
```

---
*This note is part of the Obsidian Physics Knowledge Graph. Link to parent: [[04-Circular-Motion]]*