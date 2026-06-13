# 1. Overview / 概述

**English:**
Gravitational Potential is a scalar quantity that describes the gravitational field at a point in terms of the work done per unit mass to bring a test mass from infinity to that point. This topic bridges the concepts of [[Gravitational Force and Field]] with [[Kinetic Energy and Potential Energy]], providing a unified framework for understanding gravitational interactions in radial fields.

In A-Level Physics, gravitational potential is fundamental for:
- Understanding how objects move in gravitational fields (e.g., satellites, planets)
- Calculating [[Escape Velocity]] from celestial bodies
- Analyzing [[Circular Orbits]] and orbital mechanics
- Explaining phenomena like black holes and gravitational collapse

Real-world applications include:
- Satellite orbit design and station-keeping
- Space mission planning (escape velocities, transfer orbits)
- Understanding tidal forces and gravitational lensing
- Gravitational wave detection

For Cambridge 9702 (Topic 15.2 a-f) and Edexcel IAL (Unit 4: 6.6-6.10), this topic is examined through:
- Definitions and calculations of gravitational potential (V)
- Gravitational potential energy (Ep) in radial fields
- Potential gradients and field strength relationships
- Escape velocity derivations and applications
- Graphical analysis of potential against distance

**中文：**
引力势是一个标量，描述在引力场中某一点将单位质量的测试质量从无穷远处移动到该点所做的功。这个主题将[[引力力与场]]的概念与[[动能与势能]]联系起来，为理解径向场中的引力相互作用提供了统一框架。

在A-Level物理中，引力势对于以下方面至关重要：
- 理解物体在引力场中的运动（如卫星、行星）
- 计算天体的[[逃逸速度]]
- 分析[[圆形轨道]]和轨道力学
- 解释黑洞和引力坍缩等现象

实际应用包括：
- 卫星轨道设计与保持
- 太空任务规划（逃逸速度、转移轨道）
- 理解潮汐力和引力透镜效应
- 引力波探测

对于剑桥9702（主题15.2 a-f）和爱德思IAL（单元4：6.6-6.10），该主题通过以下方式考查：
- 引力势（V）的定义和计算
- 径向场中的引力势能（Ep）
- 势梯度和场强关系
- 逃逸速度推导与应用
- 势与距离的图形分析

---

# 2. Syllabus Learning Objectives / 考纲学习目标

| CAIE 9702 (15.2 a-f) | Edexcel IAL (WPH14 U4: 6.6-6.10) |
|----------------------|----------------------------------|
| (a) Define gravitational potential at a point as the work done per unit mass in bringing a small test mass from infinity to that point | 6.6 Understand the concept of gravitational potential and gravitational potential energy |
| (b) State and use the equation V = -GM/r for gravitational potential in a radial field | 6.7 Use the equation V = -GM/r for gravitational potential |
| (c) Calculate gravitational potential energy using Ep = mV = -GMm/r | 6.8 Calculate gravitational potential energy using Ep = -GMm/r |
| (d) Understand and use the relationship g = -dV/dr (potential gradient) | 6.9 Understand the relationship between gravitational field strength and potential gradient: g = -ΔV/Δr |
| (e) Derive and use escape velocity: v_esc = √(2GM/r) | 6.10 Derive and use escape velocity: v_esc = √(2GM/R) |
| (f) Understand that gravitational potential is always negative and approaches zero at infinity | (Implicit in 6.6-6.10) |

**Examiner Expectations / 考官期望:**

**English:**
- Candidates must be able to define gravitational potential precisely, including the phrase "work done per unit mass" and "from infinity"
- The negative sign in V = -GM/r must be explained physically (potential well concept)
- Graphical interpretation of V vs r graphs is essential
- Derivation of escape velocity using energy conservation is frequently tested
- The relationship g = -dV/dr must be understood both mathematically and conceptually
- Candidates should be able to calculate gravitational potential energy for systems of multiple masses

**中文：**
- 考生必须能够精确定义引力势，包括"单位质量所做的功"和"从无穷远处"等短语
- 必须从物理上解释V = -GM/r中的负号（势阱概念）
- V vs r图的图形解释至关重要
- 利用能量守恒推导逃逸速度是常见考点
- 必须从数学和概念上理解g = -dV/dr的关系
- 考生应能够计算多质量系统的引力势能

> 📋 **CIE Only:** CIE specifically requires understanding that gravitational potential is always negative and approaches zero at infinity. The derivation of escape velocity using energy conservation is explicitly required.
>
> 📋 **Edexcel Only:** Edexcel emphasizes the practical application of escape velocity to real celestial bodies and may ask for calculations involving planetary data. The relationship g = -ΔV/Δr is treated more numerically.

---

# 3. Core Definitions / 核心定义

| Term (EN/CN) | Definition (EN) | Definition (CN) | Common Mistakes / 常见错误 |
|--------------|-----------------|-----------------|---------------------------|
| **Gravitational Potential (V)** / 引力势 | The work done per unit mass in bringing a small test mass from infinity to that point in the gravitational field | 将单位质量的测试质量从无穷远处移动到引力场中某一点所做的功 | Confusing with gravitational potential energy; forgetting the negative sign; not specifying "from infinity" |
| **Gravitational Potential Energy (Ep)** / 引力势能 | The energy stored in a system of two masses due to their gravitational attraction, given by Ep = -GMm/r | 由于引力吸引而储存在两个质量系统中的能量，由Ep = -GMm/r给出 | Thinking Ep is positive; confusing with mgh (which is only valid near Earth's surface); not recognizing it's a system property |
| **Escape Velocity (v_esc)** / 逃逸速度 | The minimum velocity required for an object to escape from a gravitational field without further propulsion | 物体无需进一步推进即可逃离引力场所需的最小速度 | Thinking it depends on the mass of the escaping object; confusing with orbital velocity; forgetting it's a scalar speed |
| **Potential Gradient (dV/dr)** / 势梯度 | The rate of change of gravitational potential with respect to distance, related to gravitational field strength by g = -dV/dr | 引力势随距离的变化率，通过g = -dV/dr与引力场强度相关 | Forgetting the negative sign; confusing gradient with field strength direction |
| **Equipotential Surface** / 等势面 | A surface on which the gravitational potential is constant; no work is done moving along an equipotential surface | 引力势恒定的表面；沿等势面移动不做功 | Thinking field lines are perpendicular to equipotentials (they are, but students often get the relationship wrong) |
| **Infinity** / 无穷远处 | A reference point where gravitational potential is defined as zero; a point so far from all masses that gravitational effects are negligible | 引力势定义为零的参考点；距离所有质量足够远，引力效应可忽略不计 | Not understanding why infinity is chosen; thinking it's a physical location |

---

# 4. Key Concepts Explained / 关键概念详解

## 4.1 Gravitational Potential (V) / 引力势

### Explanation / 解释
**English:**
Gravitational potential (V) is a scalar quantity that describes the gravitational field at any point. It is defined as the work done per unit mass in bringing a small test mass from infinity to that point. For a point mass M, the gravitational potential at distance r is:

$$ V = -\frac{GM}{r} $$

The negative sign indicates that gravitational potential is always attractive — work must be done *against* the field to move a mass away from M. At infinity, V = 0, and as we approach the mass, V becomes increasingly negative (deeper potential well).

Gravitational potential is a property of the field, not of any particular mass placed in it. It tells us how much energy per unit mass is "stored" in the field at that location.

**中文：**
引力势（V）是描述引力场中任意一点的标量。它定义为将单位质量的测试质量从无穷远处移动到该点所做的功。对于点质量M，距离r处的引力势为：

$$ V = -\frac{GM}{r} $$

负号表示引力势始终是吸引的——必须克服引力场做功才能将质量移离M。在无穷远处，V = 0，当我们接近质量时，V变得越来越负（更深的势阱）。

引力势是场的属性，而不是放入其中的任何特定质量的属性。它告诉我们该位置每单位质量在场中"储存"了多少能量。

### Physical Meaning / 物理意义
**English:**
Think of gravitational potential as a "gravitational height" map. Just as a ball rolls downhill to lower gravitational potential energy, masses move from regions of higher (less negative) gravitational potential to lower (more negative) gravitational potential. The steeper the potential gradient, the stronger the gravitational field.

**中文：**
将引力势想象成一张"引力高度"地图。就像球滚下坡到较低的引力势能一样，质量从较高（负值较小）的引力势区域移动到较低（负值较大）的引力势区域。势梯度越陡，引力场越强。

### Common Misconceptions / 常见误区
1. **Thinking V is positive:** Gravitational potential is always negative (or zero at infinity). This represents the attractive nature of gravity.
2. **Confusing V with Ep:** V is potential *per unit mass* (J/kg), while Ep is total potential energy (J) for a specific mass.
3. **Forgetting the reference point:** V = 0 at infinity is a convention; without this reference, the definition is meaningless.
4. **Applying V = -GM/r to non-point masses:** This equation is valid only for point masses or spherically symmetric objects (outside their surface).

### Exam Tips / 考试提示
**English:**
- Always include the negative sign when writing V = -GM/r
- When calculating V for a system of masses, use scalar addition (V_total = V1 + V2 + ...)
- Remember that V is a scalar, so direction doesn't matter for addition
- CIE often asks for the definition verbatim — memorize it precisely
- Edexcel may ask you to compare V at different points in a field

**中文：**
- 写V = -GM/r时始终包含负号
- 计算多质量系统的V时，使用标量加法（V_total = V1 + V2 + ...）
- 记住V是标量，加法时不考虑方向
- CIE常要求逐字定义——精确记忆
- Edexcel可能要求比较场中不同点的V

---

## 4.2 Gravitational Potential Energy in a Radial Field / 径向场中的引力势能

### Explanation / 解释
**English:**
Gravitational potential energy (Ep) in a radial field is the energy stored in the system of two masses due to their gravitational interaction. For two point masses M and m separated by distance r:

$$ E_p = -\frac{GMm}{r} $$

This is derived from the work done to bring mass m from infinity to distance r from M. The negative sign means the system has less energy than if the masses were infinitely separated (where Ep = 0). This is why objects are "bound" — you need to add energy to separate them.

Note: The equation Ep = mgh is only valid near Earth's surface (constant g). In radial fields, we must use Ep = -GMm/r.

**中文：**
径向场中的引力势能（Ep）是由于引力相互作用而储存在两个质量系统中的能量。对于相距r的两个点质量M和m：

$$ E_p = -\frac{GMm}{r} $$

这是将质量m从无穷远处移动到距离M为r处所做的功推导而来。负号意味着系统的能量比质量无限分离时（Ep = 0）更少。这就是物体被"束缚"的原因——需要添加能量才能将它们分开。

注意：Ep = mgh仅在接近地球表面（恒定g）时有效。在径向场中，必须使用Ep = -GMm/r。

### Physical Meaning / 物理意义
**English:**
Gravitational potential energy represents the "binding energy" of a system. The more negative Ep is, the more tightly bound the system. For example, a satellite in low Earth orbit has more negative Ep than one in high orbit — it's "deeper" in Earth's potential well.

**中文：**
引力势能代表系统的"结合能"。Ep越负，系统结合得越紧密。例如，低地球轨道上的卫星比高轨道上的卫星具有更负的Ep——它在地球的势阱中"更深"。

### Common Misconceptions / 常见误区
1. **Thinking Ep is the energy of one mass:** Ep is a property of the *system* of masses, not of either mass individually.
2. **Using Ep = mgh in radial fields:** This is only valid for uniform fields (near Earth's surface).
3. **Forgetting Ep is negative:** Students often write Ep = +GMm/r, missing the negative sign.
4. **Confusing Ep with kinetic energy:** In orbits, total energy E = Ep + Ek = -GMm/2r (for circular orbits).

### Exam Tips / 考试提示
**English:**
- When calculating Ep for a system of multiple masses, sum over all pairs: Ep_total = -G Σ (MiMj/rij)
- Remember that Ep is always negative for bound systems
- CIE may ask you to derive Ep from the definition of work done
- Edexcel may combine Ep with kinetic energy in orbital mechanics problems

**中文：**
- 计算多质量系统的Ep时，对所有对求和：Ep_total = -G Σ (MiMj/rij)
- 记住束缚系统的Ep始终为负
- CIE可能要求从做功的定义推导Ep
- Edexcel可能将Ep与轨道力学问题中的动能结合

---

## 4.3 Escape Velocity / 逃逸速度

### Explanation / 解释
**English:**
Escape velocity is the minimum speed an object must have to escape from a gravitational field without further propulsion. It is derived from energy conservation: the object's initial kinetic energy must be at least equal to the gravitational potential energy binding it.

For a mass m escaping from a planet of mass M and radius R:

$$ \frac{1}{2}mv_{esc}^2 = \frac{GMm}{R} $$

$$ v_{esc} = \sqrt{\frac{2GM}{R}} $$

Key points:
- Escape velocity is independent of the mass of the escaping object
- It depends only on the mass and radius of the celestial body
- Escape velocity is a scalar (speed), not a vector (velocity)
- For Earth, v_esc ≈ 11.2 km/s

**中文：**
逃逸速度是物体无需进一步推进即可逃离引力场所需的最小速度。它由能量守恒推导而来：物体的初始动能必须至少等于束缚它的引力势能。

对于从质量为M、半径为R的行星逃离的质量m：

$$ \frac{1}{2}mv_{esc}^2 = \frac{GMm}{R} $$

$$ v_{esc} = \sqrt{\frac{2GM}{R}} $$

关键点：
- 逃逸速度与逃离物体的质量无关
- 仅取决于天体的质量和半径
- 逃逸速度是标量（速率），不是矢量（速度）
- 对于地球，v_esc ≈ 11.2 km/s

### Physical Meaning / 物理意义
**English:**
Escape velocity represents the "speed of no return" — if you launch an object at this speed (or greater), it will never fall back. This concept is crucial for:
- Space missions (launching probes to other planets)
- Understanding black holes (where v_esc > c)
- Atmospheric retention (planets with low escape velocity lose their atmospheres)

**中文：**
逃逸速度代表"不归速度"——如果你以这个速度（或更大）发射物体，它将永远不会落回。这个概念对于以下方面至关重要：
- 太空任务（向其他行星发射探测器）
- 理解黑洞（其中v_esc > c）
- 大气保持（逃逸速度低的行星会失去大气层）

### Common Misconceptions / 常见误区
1. **Thinking escape velocity depends on object mass:** The m cancels out in the derivation — all objects have the same escape speed from a given body.
2. **Confusing escape velocity with orbital velocity:** Orbital velocity (v = √(GM/r)) is smaller than escape velocity (v_esc = √(2GM/r)).
3. **Thinking you must launch vertically:** Direction doesn't matter for the speed required, but launching vertically minimizes atmospheric drag.
4. **Forgetting escape velocity is from the surface:** The escape speed from a given point depends on the distance from the center.

### Exam Tips / 考试提示
**English:**
- Derive escape velocity using energy conservation — this is a common exam question
- Remember that escape velocity from Earth's surface is about 11.2 km/s
- CIE may ask you to calculate escape velocity from other planets given M and R
- Edexcel may ask about the concept of black holes (where v_esc = c)
- Be careful with units: GM/R gives m²/s², so take square root for m/s

**中文：**
- 使用能量守恒推导逃逸速度——这是常见考题
- 记住地球表面的逃逸速度约为11.2 km/s
- CIE可能要求根据M和R计算其他行星的逃逸速度
- Edexcel可能询问黑洞的概念（其中v_esc = c）
- 注意单位：GM/R给出m²/s²，开平方得到m/s

---

## 4.4 Potential Gradients / 势梯度

### Explanation / 解释
**English:**
The potential gradient is the rate of change of gravitational potential with respect to distance. It is directly related to gravitational field strength:

$$ g = -\frac{dV}{dr} $$

For a radial field where V = -GM/r:

$$ g = -\frac{d}{dr}\left(-\frac{GM}{r}\right) = -\frac{GM}{r^2} $$

The negative sign in g = -dV/dr indicates that the gravitational field points in the direction of decreasing potential (from higher to lower potential). This is consistent with the fact that masses move from regions of higher potential to lower potential.

**中文：**
势梯度是引力势随距离的变化率。它与引力场强度直接相关：

$$ g = -\frac{dV}{dr} $$

对于V = -GM/r的径向场：

$$ g = -\frac{d}{dr}\left(-\frac{GM}{r}\right) = -\frac{GM}{r^2} $$

g = -dV/dr中的负号表示引力场指向势减小的方向（从较高势到较低势）。这与质量从较高势区域移动到较低势区域的事实一致。

### Physical Meaning / 物理意义
**English:**
The potential gradient tells us how "steep" the potential well is at any point. A steeper gradient means a stronger gravitational field. On a V vs r graph, the gradient at any point gives the gravitational field strength (with a negative sign).

**中文：**
势梯度告诉我们势阱在任何点有多"陡"。梯度越陡意味着引力场越强。在V vs r图上，任意点的梯度给出引力场强度（带负号）。

### Common Misconceptions / 常见误区
1. **Forgetting the negative sign:** g = -dV/dr, not g = dV/dr
2. **Confusing gradient with field strength direction:** The gradient gives the rate of change; the negative sign gives the direction
3. **Thinking gradient is constant:** In radial fields, gradient varies with r (g ∝ 1/r²)
4. **Applying to uniform fields incorrectly:** In uniform fields, g = -ΔV/Δr (constant gradient)

### Exam Tips / 考试提示
**English:**
- On a V vs r graph, the gradient at any point equals -g
- CIE may ask you to sketch V vs r and then determine g from the gradient
- Edexcel may ask numerical calculations of g from potential differences
- Remember that g is a vector (direction matters), while V is a scalar

**中文：**
- 在V vs r图上，任意点的梯度等于-g
- CIE可能要求绘制V vs r图，然后从梯度确定g
- Edexcel可能要求从势差数值计算g
- 记住g是矢量（方向重要），而V是标量

---

## 4.5 Equipotential Surfaces / 等势面

### Explanation / 解释
**English:**
Equipotential surfaces are surfaces where the gravitational potential is constant. In a radial field around a point mass, equipotential surfaces are concentric spheres centered on the mass. Key properties:

1. No work is done moving a mass along an equipotential surface
2. Gravitational field lines are always perpendicular to equipotential surfaces
3. The spacing between equipotential surfaces indicates field strength (closer spacing = stronger field)
4. Equipotential surfaces never cross

**中文：**
等势面是引力势恒定的表面。在点质量周围的径向场中，等势面是以质量为中心的同心球面。关键特性：

1. 沿等势面移动质量不做功
2. 引力场线始终垂直于等势面
3. 等势面之间的间距表示场强（间距越近 = 场越强）
4. 等势面永不相交

### Physical Meaning / 物理意义
**English:**
Equipotential surfaces are like contour lines on a topographic map. Just as contour lines show constant height, equipotential surfaces show constant gravitational potential. Moving along a contour line requires no work against gravity.

**中文：**
等势面就像地形图上的等高线。就像等高线显示恒定高度一样，等势面显示恒定的引力势。沿等高线移动不需要克服重力做功。

### Common Misconceptions / 常见误区
1. **Thinking equipotentials are always spheres:** Only for point masses or spherically symmetric objects
2. **Confusing equipotentials with field lines:** They are perpendicular to each other
3. **Thinking work is done moving along equipotentials:** By definition, no work is done
4. **Forgetting that V is constant on equipotentials:** This is the defining property

### Exam Tips / 考试提示
**English:**
- CIE may ask you to sketch equipotential surfaces around a mass
- Edexcel may ask about the relationship between equipotentials and field lines
- Remember that closer equipotentials indicate stronger fields
- Equipotential surfaces are useful for understanding gravitational potential energy changes

**中文：**
- CIE可能要求绘制质量周围的等势面
- Edexcel可能询问等势面与场线之间的关系
- 记住等势面越近表示场越强
- 等势面有助于理解引力势能变化

---

# 5. Essential Equations / 核心公式

## 5.1 Gravitational Potential / 引力势

**Equation / 公式:**
$$ V = -\frac{GM}{r} $$

**Variables / 变量:**
| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| V | Gravitational potential | 引力势 | J kg⁻¹ |
| G | Gravitational constant | 引力常数 | N m² kg⁻² |
| M | Mass of the object creating the field | 产生场的物体质量 | kg |
| r | Distance from the center of mass | 距质量中心的距离 | m |

**Derivation / 推导:**
**English:**
The gravitational potential at a point is the work done per unit mass to bring a test mass from infinity to that point. The work done against the gravitational force F = GMm/r² over a small displacement dr is dW = F dr = (GMm/r²) dr. The total work from infinity to r is:

$$ W = \int_{\infty}^{r} \frac{GMm}{r^2} dr = GMm \left[-\frac{1}{r}\right]_{\infty}^{r} = -\frac{GMm}{r} $$

Dividing by the test mass m gives V = -GM/r.

**中文：**
某点的引力势是将测试质量从无穷远处移动到该点每单位质量所做的功。克服引力F = GMm/r²在微小位移dr上所做的功为dW = F dr = (GMm/r²) dr。从无穷远到r的总功为：

$$ W = \int_{\infty}^{r} \frac{GMm}{r^2} dr = GMm \left[-\frac{1}{r}\right]_{\infty}^{r} = -\frac{GMm}{r} $$

除以测试质量m得到V = -GM/r。

**Conditions / 适用条件:**
**English:**
- Valid for point masses or spherically symmetric objects (outside the object's surface)
- r must be measured from the center of mass
- The field must be radial (not uniform)

**中文：**
- 适用于点质量或球对称物体（在物体表面之外）
- r必须从质量中心测量
- 场必须是径向的（非均匀）

**Limitations / 局限性:**
**English:**
- Not valid inside a massive object (r < R, where R is the object's radius)
- Does not account for relativistic effects (use general relativity for strong fields)
- Assumes the mass M is stationary (no motion effects)

**中文：**
- 不适用于大质量物体内部（r < R，其中R是物体半径）
- 不考虑相对论效应（强场使用广义相对论）
- 假设质量M是静止的（无运动效应）

**Rearrangements / 变形:**
**English:**
- M = -Vr/G (to find mass from potential)
- r = -GM/V (to find distance from potential)
- ΔV = V₂ - V₁ = -GM(1/r₂ - 1/r₁) (potential difference)

**中文：**
- M = -Vr/G（从势求质量）
- r = -GM/V（从势求距离）
- ΔV = V₂ - V₁ = -GM(1/r₂ - 1/r₁)（势差）

---

## 5.2 Gravitational Potential Energy / 引力势能

**Equation / 公式:**
$$ E_p = -\frac{GMm}{r} $$

**Variables / 变量:**
| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| Ep | Gravitational potential energy | 引力势能 | J |
| G | Gravitational constant | 引力常数 | N m² kg⁻² |
| M | Mass of the larger object | 较大物体的质量 | kg |
| m | Mass of the smaller object | 较小物体的质量 | kg |
| r | Separation between centers of mass | 质量中心之间的距离 | m |

**Derivation / 推导:**
**English:**
Gravitational potential energy is the work done to bring mass m from infinity to distance r from M. From the derivation of V:

$$ E_p = m \times V = m \times \left(-\frac{GM}{r}\right) = -\frac{GMm}{r} $$

Alternatively, from the definition of work:

$$ E_p = \int_{\infty}^{r} \frac{GMm}{r^2} dr = -\frac{GMm}{r} $$

**中文：**
引力势能是将质量m从无穷远处移动到距离M为r处所做的功。从V的推导：

$$ E_p = m \times V = m \times \left(-\frac{GM}{r}\right) = -\frac{GMm}{r} $$

或者，从功的定义：

$$ E_p = \int_{\infty}^{r} \frac{GMm}{r^2} dr = -\frac{GMm}{r} $$

**Conditions / 适用条件:**
**English:**
- Valid for two point masses or spherically symmetric objects
- r is the separation between centers of mass
- The system is isolated (no external forces)

**中文：**
- 适用于两个点质量或球对称物体
- r是质量中心之间的距离
- 系统是孤立的（无外力）

**Limitations / 局限性:**
**English:**
- Not valid for objects inside a massive body
- Does not include self-gravitational energy of extended objects
- Assumes Newtonian gravity (not valid for very strong fields)

**中文：**
- 不适用于大质量物体内部的物体
- 不包括扩展物体的自引力能
- 假设牛顿引力（不适用于非常强的场）

**Rearrangements / 变形:**
**English:**
- M = -Epr/Gm (to find mass)
- r = -GMm/Ep (to find separation)
- ΔEp = Ep₂ - Ep₁ = -GMm(1/r₂ - 1/r₁) (change in potential energy)

**中文：**
- M = -Epr/Gm（求质量）
- r = -GMm/Ep（求距离）
- ΔEp = Ep₂ - Ep₁ = -GMm(1/r₂ - 1/r₁)（势能变化）

---

## 5.3 Escape Velocity / 逃逸速度

**Equation / 公式:**
$$ v_{esc} = \sqrt{\frac{2GM}{R}} $$

**Variables / 变量:**
| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| v_esc | Escape velocity | 逃逸速度 | m s⁻¹ |
| G | Gravitational constant | 引力常数 | N m² kg⁻² |
| M | Mass of the celestial body | 天体的质量 | kg |
| R | Radius of the celestial body | 天体的半径 | m |

**Derivation / 推导:**
**English:**
Using energy conservation: the total mechanical energy at the surface must be at least zero for the object to escape to infinity.

Initial kinetic energy: Ek = ½mv²
Initial gravitational potential energy: Ep = -GMm/R
At infinity: Ek = 0, Ep = 0 (by definition)

For escape: Ek_initial + Ep_initial ≥ 0
½mv² - GMm/R ≥ 0
½mv² ≥ GMm/R
v² ≥ 2GM/R
v_esc = √(2GM/R)

**中文：**
使用能量守恒：物体要逃逸到无穷远处，表面的总机械能必须至少为零。

初始动能：Ek = ½mv²
初始引力势能：Ep = -GMm/R
在无穷远处：Ek = 0，Ep = 0（按定义）

逃逸条件：Ek_初始 + Ep_初始 ≥ 0
½mv² - GMm/R ≥ 0
½mv² ≥ GMm/R
v² ≥ 2GM/R
v_esc = √(2GM/R)

**Conditions / 适用条件:**
**English:**
- Valid for escaping from the surface of a spherically symmetric body
- Assumes no atmospheric drag or other forces
- Assumes the object is launched from the surface (r = R)

**中文：**
- 适用于从球对称体表面逃逸
- 假设无大气阻力或其他力
- 假设物体从表面发射（r = R）

**Limitations / 局限性:**
**English:**
- Does not account for rotation of the celestial body (which can help with escape)
- Assumes Newtonian gravity (for black holes, use general relativity)
- Ignores the gravitational effect of the escaping object on the larger body

**中文：**
- 不考虑天体的自转（自转有助于逃逸）
- 假设牛顿引力（对于黑洞，使用广义相对论）
- 忽略逃逸物体对大天体的引力效应

**Rearrangements / 变形:**
**English:**
- M = v_esc²R/(2G) (to find mass from escape velocity)
- R = 2GM/v_esc² (to find radius)
- For black holes: v_esc = c, so Schwarzschild radius R_s = 2GM/c²

**中文：**
- M = v_esc²R/(2G)（从逃逸速度求质量）
- R = 2GM/v_esc²（求半径）
- 对于黑洞：v_esc = c，所以史瓦西半径R_s = 2GM/c²

---

## 5.4 Potential Gradient / 势梯度

**Equation / 公式:**
$$ g = -\frac{dV}{dr} $$

**Variables / 变量:**
| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| g | Gravitational field strength | 引力场强度 | N kg⁻¹ or m s⁻² |
| V | Gravitational potential | 引力势 | J kg⁻¹ |
| r | Distance from center of mass | 距质量中心的距离 | m |

**Derivation / 推导:**
**English:**
For a radial field, V = -GM/r. Differentiating with respect to r:

$$ \frac{dV}{dr} = \frac{d}{dr}\left(-\frac{GM}{r}\right) = \frac{GM}{r^2} $$

Since g = GM/r² (magnitude of field strength), and the field points in the direction of decreasing potential:

$$ g = -\frac{dV}{dr} $$

**中文：**
对于径向场，V = -GM/r。对r求导：

$$ \frac{dV}{dr} = \frac{d}{dr}\left(-\frac{GM}{r}\right) = \frac{GM}{r^2} $$

由于g = GM/r²（场强大小），且场指向势减小的方向：

$$ g = -\frac{dV}{dr} $$

**Conditions / 适用条件:**
**English:**
- Valid for any gravitational field (radial or uniform)
- For uniform fields: g = -ΔV/Δr (constant gradient)
- For radial fields: g varies with r

**中文：**
- 适用于任何引力场（径向或均匀）
- 对于均匀场：g = -ΔV/Δr（恒定梯度）
- 对于径向场：g随r变化

**Limitations / 局限性:**
**English:**
- Requires V to be differentiable (smooth function)
- For discrete mass distributions, use superposition
- Not valid at points where V is discontinuous (e.g., at the surface of a mass)

**中文：**
- 要求V可微（光滑函数）
- 对于离散质量分布，使用叠加原理
- 在V不连续的点无效（例如，质量表面）

**Rearrangements / 变形:**
**English:**
- dV = -g dr (infinitesimal potential change)
- ΔV = -∫g dr (potential difference from field)
- For uniform field: ΔV = -gΔr

**中文：**
- dV = -g dr（无穷小势变化）
- ΔV = -∫g dr（从场求势差）
- 对于均匀场：ΔV = -gΔr

---

# 6. Graphs and Relationships / 图表与关系

## 6.1 Gravitational Potential vs Distance (V vs r) / 引力势与距离关系图

### Axes / 坐标轴
**English:** x-axis: r (distance from center of mass), y-axis: V (gravitational potential)
**中文：** x轴：r（距质量中心的距离），y轴：V（引力势）

### Shape / 形状
**English:** The graph is a hyperbola approaching zero as r → ∞ and becoming increasingly negative as r → 0. For r > R (outside the mass), V = -GM/r. For r < R (inside the mass), the shape depends on the mass distribution.

**中文：** 图形是双曲线，当r → ∞时趋近于零，当r → 0时变得越来越负。对于r > R（质量外部），V = -GM/r。对于r < R（质量内部），形状取决于质量分布。

### Gradient Meaning / 斜率含义
**English:** The gradient of the V vs r graph at any point equals -g (negative of gravitational field strength). A steeper gradient means a stronger field.

**中文：** V vs r图上任意点的梯度等于-g（引力场强度的负值）。梯度越陡表示场越强。

### Area Meaning / 面积含义
**English:** The area under a g vs r graph gives the potential difference (ΔV). However, for V vs r, the area is not directly meaningful.

**中文：** g vs r图下的面积给出势差（ΔV）。但对于V vs r，面积没有直接意义。

### Exam Interpretation / 考试解读
**English:**
- The graph shows that V is always negative (attractive field)
- V approaches zero asymptotically as r → ∞
- Near the mass, V becomes very negative (deep potential well)
- The gradient becomes steeper near the mass (stronger field)
- CIE may ask you to sketch this graph and label key features
- Edexcel may ask you to determine g from the gradient at a specific point

**中文：**
- 图形显示V始终为负（吸引场）
- 当r → ∞时，V渐近趋近于零
- 在质量附近，V变得非常负（深势阱）
- 在质量附近梯度变得更陡（场更强）
- CIE可能要求绘制此图并标注关键特征
- Edexcel可能要求从特定点的梯度确定g

### Common Questions / 常见问题
**English:**
1. Sketch V vs r for a point mass M
2. Explain why V is negative
3. Determine g at a point from the gradient
4. Compare V at two different distances
5. Calculate the work done to move a mass between two points

**中文：**
1. 绘制点质量M的V vs r图
2. 解释为什么V为负
3. 从梯度确定某点的g
4. 比较两个不同距离处的V
5. 计算在两个点之间移动质量所做的功

---

## 6.2 Gravitational Potential Energy vs Distance (Ep vs r) / 引力势能与距离关系图

### Axes / 坐标轴
**English:** x-axis: r (separation between masses), y-axis: Ep (gravitational potential energy)
**中文：** x轴：r（质量之间的分离距离），y轴：Ep（引力势能）

### Shape / 形状
**English:** Same shape as V vs r but scaled by the mass m: Ep = -GMm/r. Hyperbolic, approaching zero as r → ∞ and becoming increasingly negative as r → 0.

**中文：** 与V vs r形状相同，但按质量m缩放：Ep = -GMm/r。双曲线，当r → ∞时趋近于零，当r → 0时变得越来越负。

### Gradient Meaning / 斜率含义
**English:** The gradient of Ep vs r gives the gravitational force: F = -dEp/dr. This is consistent with F = GMm/r².

**中文：** Ep vs r的梯度给出引力：F = -dEp/dr。这与F = GMm/r²一致。

### Area Meaning / 面积含义
**English:** Not directly meaningful for Ep vs r.

**中文：** 对于Ep vs r没有直接意义。

### Exam Interpretation / 考试解读
**English:**
- Shows that bound systems have negative total energy
- The more negative Ep, the more tightly bound the system
- Work must be done to increase r (make Ep less negative)
- CIE may ask to compare Ep for different mass systems
- Edexcel may combine with kinetic energy for orbital energy analysis

**中文：**
- 显示束缚系统具有负的总能量
- Ep越负，系统结合得越紧密
- 必须做功才能增加r（使Ep负值减小）
- CIE可能要求比较不同质量系统的Ep
- Edexcel可能结合动能进行轨道能量分析

### Common Questions / 常见问题
**English:**
1. Sketch Ep vs r for two masses M and m
2. Calculate the work done to increase separation from r₁ to r₂
3. Determine the binding energy of a system
4. Compare Ep for different mass combinations

**中文：**
1. 绘制两个质量M和m的Ep vs r图
2. 计算将分离距离从r₁增加到r₂所做的功
3. 确定系统的结合能
4. 比较不同质量组合的Ep

---

## 6.3 Field Strength vs Distance (g vs r) / 场强与距离关系图

### Axes / 坐标轴
**English:** x-axis: r (distance from center of mass), y-axis: g (gravitational field strength)
**中文：** x轴：r（距质量中心的距离），y轴：g（引力场强度）

### Shape / 形状
**English:** For r > R, g = GM/r² (inverse square law). The graph is a decreasing curve that approaches zero as r → ∞. For r < R (inside a uniform sphere), g ∝ r (linear increase).

**中文：** 对于r > R，g = GM/r²（平方反比定律）。图形是递减曲线，当r → ∞时趋近于零。对于r < R（均匀球体内部），g ∝ r（线性增加）。

### Gradient Meaning / 斜率含义
**English:** The gradient of g vs r gives the rate of change of field strength. For r > R, dg/dr = -2GM/r³ (negative, decreasing).

**中文：** g vs r的梯度给出场强的变化率。对于r > R，dg/dr = -2GM/r³（负值，递减）。

### Area Meaning / 面积含义
**English:** The area under the g vs r graph gives the potential difference: ΔV = -∫g dr. This is a key relationship for calculating work done.

**中文：** g vs r图下的面积给出势差：ΔV = -∫g dr。这是计算所做功的关键关系。

### Exam Interpretation / 考试解读
**English:**
- Shows the inverse square law for gravitational fields
- Area under the curve gives potential difference
- CIE may ask to sketch both g vs r and V vs r on the same axes
- Edexcel may ask numerical integration to find ΔV

**中文：**
- 显示引力场的平方反比定律
- 曲线下的面积给出势差
- CIE可能要求在相同坐标轴上绘制g vs r和V vs r
- Edexcel可能要求数值积分求ΔV

### Common Questions / 常见问题
**English:**
1. Sketch g vs r for a planet of radius R
2. Calculate the area under the curve between two points
3. Determine the potential difference from the graph
4. Compare g at different distances

**中文：**
1. 绘制半径为R的行星的g vs r图
2. 计算两点之间曲线下的面积
3. 从图形确定势差
4. 比较不同距离处的g

---

# 7. Required Diagrams / 必备图表

## 7.1 Gravitational Potential Well Diagram / 引力势阱图

### Description / 描述
**English:**
A 2D cross-section showing the gravitational potential well around a massive object. The diagram should show:
- The central mass (e.g., Earth or a star)
- Concentric equipotential surfaces (circles in 2D)
- The potential well shape (like a funnel or bowl)
- Arrows showing the direction of gravitational field lines (perpendicular to equipotentials)
- Labels for V = 0 at infinity, decreasing V near the mass

**中文：**
显示大质量物体周围引力势阱的二维截面图。图示应显示：
- 中心质量（如地球或恒星）
- 同心等势面（二维中为圆形）
- 势阱形状（如漏斗或碗状）
- 箭头显示引力场线方向（垂直于等势面）
- 标注无穷远处V = 0，质量附近V递减

### Image Prompt / 图片生成提示
> 📷 **IMAGE PROMPT — GP-DIAG-01: Gravitational Potential Well Cross-Section**
>
> A 2D cross-sectional diagram of a gravitational potential well. In the center, a large blue sphere representing Earth. Around it, concentric dashed circles (equipotential surfaces) getting closer together near the Earth and farther apart at greater distances. The potential well is shown as a 3D funnel shape in cross-section, with the Earth at the bottom of the funnel. Arrows perpendicular to equipotentials point inward toward Earth. Labels: "V = 0 at infinity" at the top, "V = -GM/r" near the surface, "Equipotential surfaces" on one circle, "Field lines" on arrows. Color scheme: blue for Earth, gray dashed lines for equipotentials, red arrows for field lines. Clean scientific diagram style, white background, suitable for A-Level physics textbook.

### Labels Required / 需要标注
**English:**
- Central mass (M)
- Equipotential surfaces (V₁, V₂, V₃, ...)
- Gravitational field lines (arrows)
- V = 0 at infinity
- Decreasing potential (V₁ > V₂ > V₃)
- Distance r from center

**中文：**
- 中心质量（M）
- 等势面（V₁, V₂, V₃, ...）
- 引力场线（箭头）
- 无穷远处V = 0
- 势递减（V₁ > V₂ > V₃）
- 距中心的距离r

### Exam Importance / 考试重要性
**English:**
- CIE uses this to test understanding of potential as a scalar field
- Edexcel uses it to relate equipotentials to field lines
- Helps visualize why V is negative and how it varies with distance
- Essential for understanding potential gradient concept

**中文：**
- CIE用此测试对势作为标量场的理解
- Edexcel用此关联等势面与场线
- 有助于可视化为什么V为负以及它如何随距离变化
- 对理解势梯度概念至关重要

---

## 7.2 V vs r and g vs r Graphs / V vs r和g vs r图

### Description / 描述
**English:**
Two graphs on the same axes or side-by-side showing:
- V vs r: Hyperbolic curve, negative values, approaching zero at infinity
- g vs r: Inverse square curve, positive values (magnitude), approaching zero at infinity
- Key points labeled: surface (r = R), infinity (r → ∞)
- Gradient of V vs r shown at a point to illustrate g = -dV/dr

**中文：**
在同一坐标轴或并排显示的两个图形：
- V vs r：双曲线，负值，在无穷远处趋近于零
- g vs r：平方反比曲线，正值（大小），在无穷远处趋近于零
- 标注关键点：表面（r = R），无穷远（r → ∞）
- 在一点显示V vs r的梯度以说明g = -dV/dr

### Image Prompt / 图片生成提示
> 📷 **IMAGE PROMPT — GP-DIAG-02: V vs r and g vs r Comparison Graphs**
>
> Two graphs placed side by side on the same page. Left graph: V vs r. x-axis labeled "r / m", y-axis labeled "V / J kg⁻¹". A hyperbolic curve in the negative region, starting very negative near r=0, rising steeply then gradually approaching zero as r increases. Dashed line at V=0. Right graph: g vs r. x-axis labeled "r / m", y-axis labeled "g / N kg⁻¹". A decreasing curve starting high near r=0, following inverse square law. Both graphs have a vertical dashed line at r=R (planet surface). A tangent line drawn on the V vs r graph at a point, with annotation "gradient = -g". Clean scientific style, grid lines, professional labeling, suitable for A-Level physics textbook.

### Labels Required / 需要标注
**English:**
- V vs r: V = -GM/r, V → 0 as r → ∞, V → -∞ as r → 0
- g vs r: g = GM/r², g → 0 as r → ∞, g → ∞ as r → 0
- r = R (surface of planet)
- Tangent line showing gradient
- Annotation: g = -dV/dr

**中文：**
- V vs r：V = -GM/r，r → ∞时V → 0，r → 0时V → -∞
- g vs r：g = GM/r²，r → ∞时g → 0，r → 0时g → ∞
- r = R（行星表面）
- 切线显示梯度
- 标注：g = -dV/dr

### Exam Importance / 考试重要性
**English:**
- CIE frequently asks to sketch these graphs
- Edexcel uses them for numerical analysis
- Tests understanding of the relationship between V and g
- Essential for potential gradient concept

**中文：**
- CIE常要求绘制这些图形
- Edexcel用它们进行数值分析
- 测试对V和g之间关系的理解
- 对势梯度概念至关重要

---

## 7.3 Escape Velocity Diagram / 逃逸速度图

### Description / 描述
**English:**
A diagram showing:
- A planet (e.g., Earth) with radius R
- An object on the surface with velocity v
- Trajectories for different velocities:
  - v < v_esc: object falls back (parabolic/suborbital)
  - v = v_esc: object escapes (parabolic trajectory)
  - v > v_esc: object escapes (hyperbolic trajectory)
- Labels for escape velocity equation
- Energy bar chart showing KE and GPE at surface and at infinity

**中文：**
显示以下内容的图示：
- 半径为R的行星（如地球）
- 表面上的物体，速度为v
- 不同速度的轨迹：
  - v < v_esc：物体落回（抛物线/亚轨道）
  - v = v_esc：物体逃逸（抛物线轨迹）
  - v > v_esc：物体逃逸（双曲线轨迹）
- 逃逸速度方程标注
- 能量柱状图显示表面和无穷远处的KE和GPE

### Image Prompt / 图片生成提示
> 📷 **IMAGE PROMPT — GP-DIAG-03: Escape Velocity Trajectories**
>
> A diagram showing a planet (Earth) in the center with radius R labeled. From the surface, three trajectories emanate: 1) A dashed curve that rises then falls back to the surface, labeled "v < v_esc (falls back)". 2) A solid curve that rises and flattens out, never returning, labeled "v = v_esc (escape)". 3) A dotted curve that rises more steeply and curves away, labeled "v > v_esc (escape)". All trajectories start from the same point on the surface. An inset energy bar chart shows: at surface, a tall KE bar and a deep GPE bar (negative); at infinity, both bars at zero. Equation v_esc = √(2GM/R) displayed prominently. Clean scientific diagram, blue planet, colored trajectories, white background.

### Labels Required / 需要标注
**English:**
- Planet radius R
- Surface point
- Three trajectories with velocity conditions
- v_esc = √(2GM/R)
- Energy bar chart: KE (positive), GPE (negative), Total E = 0 at escape
- "At infinity: KE = 0, GPE = 0"

**中文：**
- 行星半径R
- 表面点
- 三条轨迹及速度条件
- v_esc = √(2GM/R)
- 能量柱状图：KE（正），GPE（负），逃逸时总E = 0
- "在无穷远处：KE = 0，GPE = 0"

### Exam Importance / 考试重要性
**English:**
- CIE requires derivation and application of escape velocity
- Edexcel tests understanding through energy conservation
- Visualizes why escape velocity is independent of object mass
- Connects to black hole concept (v_esc = c)

**中文：**
- CIE要求推导和应用逃逸速度
- Edexcel通过能量守恒测试理解
- 可视化为什么逃逸速度与物体质量无关
- 连接到黑洞概念（v_esc = c）

---

# 8. Worked Examples / 典型例题

## Example 1: Calculating Gravitational Potential and Potential Energy / 计算引力势和势能

### Question / 题目
**English:**
The Earth has mass M = 5.97 × 10²⁴ kg and radius R = 6.37 × 10⁶ m. A satellite of mass m = 500 kg is in orbit at an altitude of 400 km above Earth's surface. G = 6.67 × 10⁻¹¹ N m² kg⁻².

(a) Calculate the gravitational potential at the satellite's position.
(b) Calculate the gravitational potential energy of the satellite-Earth system.
(c) Calculate the work done to move the satellite from the surface to this orbit.

**中文：**
地球质量M = 5.97 × 10²⁴ kg，半径R = 6.37 × 10⁶ m。一颗质量为m = 500 kg的卫星在距地球表面400 km的高度轨道上运行。G = 6.67 × 10⁻¹¹ N m² kg⁻²。

(a) 计算卫星位置处的引力势。
(b) 计算卫星-地球系统的引力势能。
(c) 计算将卫星从表面移动到该轨道所做的功。

### Solution / 解答

**Step 1: Calculate the distance from Earth's center / 计算距地心距离**

**English:**
r = R + h = 6.37 × 10⁶ + 400 × 10³ = 6.77 × 10⁶ m

**中文：**
r = R + h = 6.37 × 10⁶ + 400 × 10³ = 6.77 × 10⁶ m

**Step 2: Calculate gravitational potential / 计算引力势**

**English:**
V = -GM/r

V = -(6.67 × 10⁻¹¹)(5.97 × 10²⁴) / (6.77 × 10⁶)

V = -(3.98 × 10¹⁴) / (6.77 × 10⁶)

V = -5.88 × 10⁷ J kg⁻¹

**中文：**
V = -GM/r

V = -(6.67 × 10⁻¹¹)(5.97 × 10²⁴) / (6.77 × 10⁶)

V = -(3.98 × 10¹⁴) / (6.77 × 10⁶)

V = -5.88 × 10⁷ J kg⁻¹

**Step 3: Calculate gravitational potential energy / 计算引力势能**

**English:**
Ep = mV = m × (-GM/r)

Ep = 500 × (-5.88 × 10⁷)

Ep = -2.94 × 10¹⁰ J

Alternatively: Ep = -GMm/r = -(6.67 × 10⁻¹¹)(5.97 × 10²⁴)(500) / (6.77 × 10⁶) = -2.94 × 10¹⁰ J

**中文：**
Ep = mV = m × (-GM/r)

Ep = 500 × (-5.88 × 10⁷)

Ep = -2.94 × 10¹⁰ J

或者：Ep = -GMm/r = -(6.67 × 10⁻¹¹)(5.97 × 10²⁴)(500) / (6.77 × 10⁶) = -2.94 × 10¹⁰ J

**Step 4: Calculate work done to move from surface to orbit / 计算从表面移动到轨道所做的功**

**English:**
Work done = ΔEp = Ep_orbit - Ep_surface

First, calculate Ep at surface:
Ep_surface = -GMm/R = -(6.67 × 10⁻¹¹)(5.97 × 10²⁴)(500) / (6.37 × 10⁶)
Ep_surface = -3.13 × 10¹⁰ J

Work done = Ep_orbit - Ep_surface = (-2.94 × 10¹⁰) - (-3.13 × 10¹⁰)
Work done = 1.9 × 10⁹ J

**中文：**
所做的功 = ΔEp = Ep_轨道 - Ep_表面

首先，计算表面的Ep：
Ep_表面 = -GMm/R = -(6.67 × 10⁻¹¹)(5.97 × 10²⁴)(500) / (6.37 × 10⁶)
Ep_表面 = -3.13 × 10¹⁰ J

所做的功 = Ep_轨道 - Ep_表面 = (-2.94 × 10¹⁰) - (-3.13 × 10¹⁰)
所做的功 = 1.9 × 10⁹ J

### Final Answer / 最终答案
**Answer:**
(a) V = -5.88 × 10⁷ J kg⁻¹
(b) Ep = -2.94 × 10¹⁰ J
(c) Work done = 1.9 × 10⁹ J

**答案：**
(a) V = -5.88 × 10⁷ J kg⁻¹
(b) Ep = -2.94 × 10¹⁰ J
(c) 所做的功 = 1.9 × 10⁹ J

### Examiner Notes / 考官点评
**English:**
- Common mistake: forgetting to add altitude to Earth's radius (using R instead of r)
- Common mistake: using Ep = mgh (which is only valid near Earth's surface)
- The work done is positive because we must do work against gravity to raise the satellite
- Note that Ep becomes less negative (increases) as the satellite moves to higher orbit
- Always check units: V in J kg⁻¹, Ep in J

**中文：**
- 常见错误：忘记将高度加到地球半径上（使用R而不是r）
- 常见错误：使用Ep = mgh（仅在地球表面附近有效）
- 所做的功为正，因为我们必须克服重力做功才能提升卫星
- 注意当卫星移动到更高轨道时，Ep变得不那么负（增加）
- 始终检查单位：V单位为J kg⁻¹，Ep单位为J

---

## Example 2: Escape Velocity Calculation / 逃逸速度计算

### Question / 题目
**English:**
A planet has mass M = 3.0 × 10²³ kg and radius R = 2.5 × 10⁶ m. G = 6.67 × 10⁻¹¹ N m² kg⁻².

(a) Calculate the escape velocity from the surface of this planet.
(b) A spacecraft of mass 1000 kg is launched from the surface. Calculate the minimum kinetic energy required for it to escape the planet's gravitational field.
(c) Explain why the escape velocity is independent of the mass of the spacecraft.

**中文：**
某行星质量M = 3.0 × 10²³ kg，半径R = 2.5 × 10⁶ m。G = 6.67 × 10⁻¹¹ N m² kg⁻²。

(a) 计算从该行星表面逃逸的逃逸速度。
(b) 一艘质量为1000 kg的航天器从表面发射。计算它逃离行星引力场所需的最小动能。
(c) 解释为什么逃逸速度与航天器的质量无关。

### Solution / 解答

**Step 1: Calculate escape velocity / 计算逃逸速度**

**English:**
v_esc = √(2GM/R)

v_esc = √[2 × (6.67 × 10⁻¹¹) × (3.0 × 10²³) / (2.5 × 10⁶)]

v_esc = √[(4.00 × 10¹³) / (2.5 × 10⁶)]

v_esc = √(1.60 × 10⁷)

v_esc = 4.0 × 10³ m s⁻¹ = 4.0 km s⁻¹

**中文：**
v_esc = √(2GM/R)

v_esc = √[2 × (6.67 × 10⁻¹¹) × (3.0 × 10²³) / (2.5 × 10⁶)]

v_esc = √[(4.00 × 10¹³) / (2.5 × 10⁶)]

v_esc = √(1.60 × 10⁷)

v_esc = 4.0 × 10³ m s⁻¹ = 4.0 km s⁻¹

**Step 2: Calculate minimum kinetic energy / 计算最小动能**

**English:**
For escape: KE_min = -Ep_surface = GMm/R

KE_min = (6.67 × 10⁻¹¹)(3.0 × 10²³)(1000) / (2.5 × 10⁶)

KE_min = (2.00 × 10¹⁶) / (2.5 × 10⁶)

KE_min = 8.0 × 10⁹ J

Alternatively: KE_min = ½mv_esc² = ½ × 1000 × (4.0 × 10³)² = 8.0 × 10⁹ J

**中文：**
逃逸条件：KE_最小 = -Ep_表面 = GMm/R

KE_最小 = (6.67 × 10⁻¹¹)(3.0 × 10²³)(1000) / (2.5 × 10⁶)

KE_最小 = (2.00 × 10¹⁶) / (2.5 × 10⁶)

KE_最小 = 8.0 × 10⁹ J

或者：KE_最小 = ½mv_esc² = ½ × 1000 × (4.0 × 10³)² = 8.0 × 10⁹ J

**Step 3: Explain independence of mass / 解释与质量无关**

**English:**
From the energy conservation derivation:
½mv² = GMm/R

The mass m cancels out from both sides:
½v² = GM/R

Therefore v = √(2GM/R), which does not depend on m. This is because both kinetic energy and gravitational potential energy are proportional to the mass of the object.

**中文：**
从能量守恒推导：
½mv² = GMm/R

质量m从两边消去：
½v² = GM/R

因此v = √(2GM/R)，与m无关。这是因为动能和引力势能都与物体质量成正比。

### Final Answer / 最终答案
**Answer:**
(a) v_esc = 4.0 × 10³ m s⁻¹ (4.0 km s⁻¹)
(b) KE_min = 8.0 × 10⁹ J
(c) The mass cancels out in the energy conservation equation because both KE and GPE are proportional to mass.

**答案：**
(a) v_esc = 4.0 × 10³ m s⁻¹ (4.0 km s⁻¹)
(b) KE_最小 = 8.0 × 10⁹ J
(c) 在能量守恒方程中质量被消去，因为KE和GPE都与质量成正比。

### Examiner Notes / 考官点评
**English:**
- Common mistake: forgetting to take the square root when calculating v_esc
- Common mistake: using diameter instead of radius
- The explanation of mass independence is frequently tested in exams
- Remember that escape velocity is a scalar (speed), not a vector
- For part (c), a clear mathematical derivation is expected

**中文：**
- 常见错误：计算v_esc时忘记开平方
- 常见错误：使用直径而不是半径
- 质量无关性的解释在考试中经常测试
- 记住逃逸速度是标量（速率），不是矢量
- 对于(c)部分，期望清晰的数学推导

---

# 9. Past Paper Question Types / 历年真题题型

| Question Type / 题型 | Frequency / 频率 | Difficulty / 难度 | Past Paper References / 真题索引 |
|----------------------|------------------|------------------|-------------------------------|
| Calculation of V or Ep / 计算V或Ep | High | Medium | 📝 *待填入* |
| Escape velocity derivation / 逃逸速度推导 | High | Medium | 📝 *待填入* |
| V vs r graph analysis / V vs r图分析 | Medium | Medium-High | 📝 *待填入* |
| Potential gradient calculation / 势梯度计算 | Medium | Medium | 📝 *待填入* |
| Energy conservation in gravitational fields / 引力场中的能量守恒 | High | High | 📝 *待填入* |
| Comparison of potentials / 势的比较 | Low-Medium | Medium | 📝 *待填入* |
| Black hole / Schwarzschild radius / 黑洞/史瓦西半径 | Low (Edexcel) | High | 📝 *待填入* |
| Multi-mass systems / 多质量系统 | Low-Medium | High | 📝 *待填入* |

> 📝 **题库整理中 / Question Bank Under Construction:** 具体试卷编号（如 9702/23/M/J/24 Q3）将在后续整理真题后填入上表。

**Common Command Words / 常见指令词:**

| Command Word (EN) | 指令词 (CN) | Typical Usage / 典型用法 |
|-------------------|-------------|-------------------------|
| State | 陈述 | State the definition of gravitational potential |
| Define | 定义 | Define gravitational potential at a point |
| Explain | 解释 | Explain why gravitational potential is negative |
| Describe | 描述 | Describe how gravitational potential varies with distance |
| Calculate | 计算 | Calculate the escape velocity from the planet |
| Determine | 确定 | Determine the gravitational potential at point P |
| Derive | 推导 | Derive an expression for escape velocity |
| Suggest | 建议 | Suggest why the escape velocity from the Moon is less than from Earth |
| Sketch | 绘制 | Sketch a graph of V against r |
| Compare | 比较 | Compare the gravitational potential at two different points |

---

# 10. Practical Skills Connections / 实验技能链接

**English:**
While gravitational potential is primarily a theoretical concept, it connects to practical skills in several ways:

**CAIE Paper 3 (AS) / Paper 5 (A2):**
- **Graph plotting and analysis:** Plotting V vs r or g vs r graphs from given data; determining gradients to find field strength
- **Uncertainty analysis:** Propagating uncertainties in M, r, and G to find uncertainty in V or Ep
- **Experimental design:** Designing experiments to determine G (Cavendish experiment) or to verify inverse square law
- **Data analysis:** Using logarithmic plots to verify relationships (e.g., log V vs log r to confirm V ∝ 1/r)

**Edexcel Unit 3 (AS) / Unit 6 (A2):**
- **Measurements:** Measuring gravitational field strength using pendulum or free-fall methods
- **Graphical analysis:** Using gradients of V vs r graphs to determine g
- **Error analysis:** Identifying systematic errors in gravitational experiments
- **Practical investigations:** Investigating factors affecting orbital motion using simulations

**Common Practical Skills:**
1. **Using logarithmic scales:** Plotting log V against log r to determine the power relationship
2. **Determining gradients:** Drawing tangents to curves to find instantaneous gradient (g = -dV/dr)
3. **Area under curves:** Estimating area under g vs r graphs to find potential differences
4. **Uncertainty propagation:** Calculating percentage uncertainties in derived quantities
5. **Significant figures:** Reporting answers with appropriate precision

**中文：**
虽然引力势主要是理论概念，但它通过多种方式与实践技能相关联：

**CAIE Paper 3 (AS) / Paper 5 (A2)：**
- **图表绘制与分析：** 根据给定数据绘制V vs r或g vs r图；确定梯度以求出场强
- **不确定度分析：** 传播M、r和G的不确定度以求出V或Ep的不确定度
- **实验设计：** 设计实验确定G（卡文迪许实验）或验证平方反比定律
- **数据分析：** 使用对数图验证关系（如log V vs log r确认V ∝ 1/r）

**Edexcel Unit 3 (AS) / Unit 6 (A2)：**
- **测量：** 使用单摆或自由落体方法测量引力场强度
- **图形分析：** 使用V vs r图的梯度确定g
- **误差分析：** 识别引力实验中的系统误差
- **实践调查：** 使用模拟研究影响轨道运动的因素

**常见实践技能：**
1. **使用对数刻度：** 绘制log V vs log r以确定幂关系
2. **确定梯度：** 绘制曲线的切线以找到瞬时梯度（g = -dV/dr）
3. **曲线下面积：** 估算g vs r图下的面积以求出势差
4. **不确定度传播：** 计算导出量的百分比不确定度
5. **有效数字：** 以适当的精度报告答案

> 📋 **CIE Only:** CIE Paper 5 may ask you to design an experiment to determine G or to verify the inverse square law. You should be familiar with the Cavendish experiment setup.
>
> 📋 **Edexcel Only:** Edexcel Unit 6 may include practical investigations using computer simulations of gravitational fields or orbital motion.

---

# 11. Concept Map / 概念图谱

```mermaid
graph TD
    %% Main Topic
    GP[Gravitational Potential]
    
    %% Prerequisites
    GFF[Gravitational Force and Field]
    KEPE[Kinetic Energy and Potential Energy]
    
    %% Sub-topics (Leaf Nodes)
    V[Gravitational Potential V]
    EPR[Gravitational Potential Energy in Radial Field]
    ESC[Escape Velocity]
    PG[Potential Gradients]
    
    %% Related Topics
    CO[Circular Orbits]
    
    %% Key Equations
    EQ1[V = -GM/r]
    EQ2[Ep = -GMm/r]
    EQ3[v_esc = √(2GM/R)]
    EQ4[g = -dV/dr]
    
    %% Concepts
    DEF[Definition: Work per unit mass from infinity]
    NEG[Negative sign: Attractive field]
    INF[V = 0 at infinity]
    WELL[Potential Well Concept]
    BIND[Binding Energy]
    CONS[Energy Conservation]
    GRAD[Gradient = Field Strength]
    EQUI[Equipotential Surfaces]
    
    %% Connections
    GP --> V
    GP --> EPR
    GP --> ESC
    GP --> PG
    
    GFF --> GP
    KEPE --> GP
    
    V --> EQ1
    EPR --> EQ2
    ESC --> EQ3
    PG --> EQ4
    
    V --> DEF
    V --> NEG
    V --> INF
    V --> WELL
    
    EPR --> BIND
    ESC --> CONS
    
    PG --> GRAD
    PG --> EQUI
    
    GP --> CO
    
    %% Styling
    classDef main fill:#f9f,stroke:#333,stroke-width:4px
    classDef subtopic fill:#bbf,stroke:#333,stroke-width:2px
    classDef equation fill:#bfb,stroke:#333,stroke-width:2px
    classDef concept fill:#fbb,stroke:#333,stroke-width:2px
    classDef related fill:#ffb,stroke:#333,stroke-width:2px
    
    class GP main
    class V,EPR,ESC,PG subtopic
    class EQ1,EQ2,EQ3,EQ4 equation
    class DEF,NEG,INF,WELL,BIND,CONS,GRAD,EQUI concept
    class GFF,KEPE,CO related
```

**Concept Map Explanation / 概念图说明:**

**English:**
The concept map shows how Gravitational Potential connects to:
- **Prerequisites:** [[Gravitational Force and Field]] (provides the force law F = GMm/r²) and [[Kinetic Energy and Potential Energy]] (provides energy conservation framework)
- **Sub-topics:** Four leaf nodes that are explored in detail in separate notes
- **Related Topics:** [[Circular Orbits]] (where gravitational potential energy combines with kinetic energy)
- **Key Equations:** The four fundamental equations that govern gravitational potential
- **Core Concepts:** The physical ideas that underpin the mathematics

**中文：**
概念图显示引力势如何连接到：
- **先决条件：** [[引力力与场]]（提供力定律F = GMm/r²）和[[动能与势能]]（提供能量守恒框架）
- **子主题：** 四个叶节点，在单独的笔记中详细探讨
- **相关主题：** [[圆形轨道]]（其中引力势能与动能结合）
- **关键方程：** 控制引力势的四个基本方程
- **核心概念：** 支撑数学的物理思想

---

# 12. Quick Revision Sheet / 速查表

| Category / 类别 | Key Points / 要点 |
|----------------|------------------|
| **Definitions / 定义** | • **Gravitational Potential (V):** Work done per unit mass to bring a test mass from infinity to that point (J kg⁻¹)<br>• **Gravitational Potential Energy (Ep):** Energy stored in a system of two masses due to gravitational attraction (J)<br>• **Escape Velocity (v_esc):** Minimum speed to escape gravitational field without further propulsion (m s⁻¹)<br>• **Potential Gradient:** Rate of change of V with distance; g = -dV/dr |
| **Equations / 公式** | • V = -GM/r (gravitational potential)<br>• Ep = mV = -GMm/r (gravitational potential energy)<br>• v_esc = √(2GM/R) (escape velocity)<br>• g = -dV/dr (potential gradient)<br>• For black holes: R_s = 2GM/c² (Schwarzschild radius) |
| **Graphs / 图表** | • **V vs r:** Hyperbolic curve, negative values, approaches zero at infinity<br>• **g vs r:** Inverse square curve, positive values, approaches zero at infinity<br>• **Ep vs r:** Same shape as V vs r, scaled by mass m<br>• Gradient of V vs r = -g; Area under g vs r = -ΔV |
| **Key Facts / 关键事实** | • V is always negative (attractive field)<br>• V = 0 at infinity (reference point)<br>• Ep is a system property, not of individual masses<br>• Escape velocity is independent of escaping object's mass<br>• Equipotential surfaces are perpendicular to field lines<br>• No work is done moving along an equipotential surface |
| **Exam Reminders / 考试提醒** | • **Always include negative sign** in V = -GM/r and Ep = -GMm/r<br>• **Don't use Ep = mgh** in radial fields (only valid near Earth's surface)<br>• **Check units:** V (J kg⁻¹), Ep (J), g (N kg⁻¹ or m s⁻²)<br>• **Derive escape velocity** using energy conservation (KE + GPE = 0 at escape)<br>• **Scalar addition** for V in multi-mass systems<br>• **Gradient interpretation:** Steeper V vs r = stronger field<br>• **Common calculation errors:** Forgetting to add altitude to radius; using diameter instead of radius; forgetting square root in v_esc |

---

> 📝 **Note / 备注:** This is the HUB (overview) file for Gravitational Potential. For detailed exploration of specific sub-topics, refer to the leaf nodes: [[Gravitational Potential Energy in a Radial Field]], [[Gravitational Potential (V)]], [[Escape Velocity]], and [[Potential Gradients]].