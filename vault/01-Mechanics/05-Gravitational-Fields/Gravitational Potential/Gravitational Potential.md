# 1. Overview / 概述

**English:** Gravitational potential is a scalar quantity that describes the gravitational field at a point in terms of the work done per unit mass to bring a test mass from infinity. This topic extends the concept of gravitational potential energy from uniform fields (near Earth's surface) to radial fields (around planets and stars). It is fundamental to understanding satellite motion, escape velocity, orbital mechanics, and the energy considerations in astrophysics. For both CAIE 9702 and Edexcel IAL, this is a high-difficulty A2 topic that frequently appears in multiple-choice, structured questions, and data analysis. Mastery of gravitational potential is essential for linking [[Gravitational Force and Field]] with [[Kinetic Energy and Potential Energy]] and for understanding [[Circular Orbits]].

**中文:** 引力势是一个标量，描述了在引力场中某一点将单位质量的测试质量从无穷远处移动到此点所做的功。本主题将引力势能的概念从均匀场（地球表面附近）扩展到径向场（行星和恒星周围）。它是理解卫星运动、逃逸速度、轨道力学以及天体物理学中能量考虑的基础。对于CAIE 9702和Edexcel IAL，这是一个高难度的A2主题，经常出现在选择题、结构化问题和数据分析中。掌握引力势对于连接[[Gravitational Force and Field]]与[[Kinetic Energy and Potential Energy]]以及理解[[Circular Orbits]]至关重要。

> 📷 **IMAGE PROMPT — GP-OVERVIEW: Gravitational Potential Overview Diagram**
> A conceptual diagram showing a planet at center with concentric circles representing equipotential surfaces. Labels: "V = -GM/r" at each surface, arrows showing direction of decreasing potential (toward planet), and a test mass moving from infinity. Style: clean vector, blue/black on white. Exam importance: HIGH — helps visualize scalar field.

# 2. Syllabus Learning Objectives / 考纲学习目标

| CAIE 9702 (15.2 a-f) | Edexcel IAL (WPH14 U4: 6.6-6.10) |
|---|---|
| Define gravitational potential at a point as the work done per unit mass in bringing a test mass from infinity to that point | Understand gravitational potential as work done per unit mass from infinity |
| Use the equation $V = -\frac{GM}{r}$ for gravitational potential in a radial field | Use $V = -\frac{GM}{r}$ for radial fields |
| Understand that gravitational potential is a scalar quantity | Understand scalar nature of potential |
| Calculate gravitational potential energy: $E_p = mV = -\frac{GMm}{r}$ | Calculate gravitational potential energy in radial fields |
| Derive and use escape velocity: $v_{esc} = \sqrt{\frac{2GM}{r}}$ | Derive and use escape velocity |
| Understand potential gradient: $g = -\frac{dV}{dr}$ | Understand relationship between field strength and potential gradient |

**Examiner Expectations / 考官期望:**
- **English:** Candidates must use correct sign conventions (negative potential). The concept of "zero potential at infinity" is critical. Derivation of escape velocity using energy conservation is frequently tested. Potential gradient questions often appear in data analysis.
- **中文:** 考生必须使用正确的符号约定（负势）。"无穷远处势为零"的概念至关重要。使用能量守恒推导逃逸速度经常被测试。势梯度问题常出现在数据分析中。

> 📋 **CIE Only:** CAIE 9702 specifically requires understanding of gravitational potential in the context of uniform fields (near Earth) vs radial fields. Paper 4 structured questions often ask for derivation of escape velocity.
> 
> 📋 **Edexcel Only:** Edexcel IAL Unit 4 often includes gravitational potential in multi-step calculations involving orbital energy changes. The relationship $g = -\frac{dV}{dr}$ is explicitly tested in data analysis questions.

# 3. Core Definitions / 核心定义

| Term (EN/CN) | Definition (EN) | Definition (CN) | Common Mistakes / 常见错误 |
|---|---|---|---|
| [[Gravitational Potential (V)]] / 引力势 | The work done per unit mass in bringing a small test mass from infinity to that point in the field | 将单位质量的测试质量从无穷远处移动到场中该点所做的功 | Forgetting negative sign; confusing with potential energy |
| [[Gravitational Potential Energy in a Radial Field]] / 径向场中的引力势能 | The energy stored in a system of two masses separated by distance r in a gravitational field: $E_p = -\frac{GMm}{r}$ | 在引力场中相距r的两个质量系统储存的能量 | Using $mgh$ instead of $-\frac{GMm}{r}$ for radial fields |
| [[Escape Velocity]] / 逃逸速度 | The minimum speed required for an object to escape a gravitational field from a given starting point, with no further propulsion | 物体从给定起点逃离引力场所需的最小速度，无需进一步推进 | Thinking escape velocity depends on mass of escaping object |
| [[Potential Gradients]] / 势梯度 | The rate of change of gravitational potential with distance: $g = -\frac{dV}{dr}$ | 引力势随距离的变化率 | Missing negative sign; confusing with field strength direction |
| Equipotential Surface / 等势面 | A surface where gravitational potential is constant; no work is done moving along it | 引力势恒定的表面；沿其移动不做功 | Thinking field lines are perpendicular to equipotentials (they ARE) |
| Infinity / 无穷远 | A point so far from all masses that gravitational potential is defined as zero | 距离所有质量足够远，引力势定义为零的点 | Not understanding this is a reference point, not a physical location |

# 4. Key Concepts Explained / 关键概念详解

## 4.1 Gravitational Potential (V) / 引力势 (V)

### Explanation / 解释
**English:** Gravitational potential $V$ at a point in a [[Gravitational Force and Field|gravitational field]] is defined as the work done per unit mass in bringing a small test mass from infinity to that point. For a radial field around a point mass $M$, $V = -\frac{GM}{r}$. The negative sign indicates that work is done BY the field (the field does positive work) as the mass moves from infinity inward. Potential is a scalar quantity, so potentials from multiple masses add algebraically.

**中文:** 引力场中某点的引力势$V$定义为将单位质量的测试质量从无穷远处移动到该点所做的功。对于点质量$M$周围的径向场，$V = -\frac{GM}{r}$。负号表示当质量从无穷远处向内移动时，场做功（场做正功）。势是标量，因此多个质量的势可以代数相加。

### Physical Meaning / 物理意义
**English:** Gravitational potential represents the "gravitational energy per unit mass" at a point. More negative potential means stronger gravitational binding. The potential well around a planet is deeper (more negative) closer to the surface. This concept directly links to [[Gravitational Potential Energy in a Radial Field]] via $E_p = mV$.

**中文:** 引力势表示某点的"单位质量的引力能"。更负的势意味着更强的引力束缚。行星周围的势阱在靠近表面时更深（更负）。这个概念通过$E_p = mV$直接连接到[[Gravitational Potential Energy in a Radial Field]]。

### Common Misconceptions / 常见误区
- Thinking potential is zero at the surface of a planet (it's zero at infinity)
- Confusing potential $V$ (J kg⁻¹) with potential energy $E_p$ (J)
- Forgetting the negative sign in calculations
- Thinking potential is a vector (it's scalar)

### Exam Tips / 考试提示
**English:** Always write $V = -\frac{GM}{r}$ with the negative sign. When calculating potential difference, remember $\Delta V = V_2 - V_1$. For multiple masses, add potentials algebraically (including signs). Use $V$ to find work done: $W = m\Delta V$.

**中文:** 始终在$V = -\frac{GM}{r}$中写上负号。计算势差时，记住$\Delta V = V_2 - V_1$。对于多个质量，代数相加势（包括符号）。使用$V$求做功：$W = m\Delta V$。

> 📷 **IMAGE PROMPT — GP-POTENTIAL: Gravitational Potential Well Diagram**
> A 2D cross-section showing a planet at center with a "potential well" curve (V vs r). The curve approaches zero as r→∞ and becomes increasingly negative as r→0. Labels: "V = -GM/r", "r", "V", "Surface", "Infinity (V=0)". Style: graph with shaded region under curve. Exam importance: HIGH — essential for understanding energy changes.

## 4.2 Gravitational Potential Energy in a Radial Field / 径向场中的引力势能

### Explanation / 解释
**English:** For two point masses $M$ and $m$ separated by distance $r$, the [[Gravitational Potential Energy in a Radial Field]] is $E_p = -\frac{GMm}{r}$. This is the energy stored in the system. The negative sign means the system has less energy than if the masses were at infinity (where $E_p = 0$). To separate the masses, work must be done against the field, increasing $E_p$ toward zero.

**中文:** 对于相距$r$的两个点质量$M$和$m$，[[Gravitational Potential Energy in a Radial Field]]为$E_p = -\frac{GMm}{r}$。这是系统储存的能量。负号意味着系统比质量在无穷远处（$E_p = 0$）时具有更少的能量。要分离质量，必须克服场做功，使$E_p$向零增加。

### Physical Meaning / 物理意义
**English:** This is the gravitational equivalent of elastic potential energy in a spring. It represents the capacity to do work as masses move closer together. The more negative $E_p$, the more tightly bound the system. This concept is crucial for understanding [[Escape Velocity]] and orbital energy changes in [[Circular Orbits]].

**中文:** 这是弹簧中弹性势能的引力等效。它表示质量相互靠近时做功的能力。$E_p$越负，系统结合得越紧密。这个概念对于理解[[Escape Velocity]]和[[Circular Orbits]]中的轨道能量变化至关重要。

### Common Misconceptions / 常见误区
- Using $mgh$ for radial fields (only valid near Earth's surface where $g$ is constant)
- Thinking $E_p$ is the energy of one mass (it's the energy of the system of two masses)
- Forgetting that $E_p$ becomes less negative (increases) as $r$ increases

### Exam Tips / 考试提示
**English:** For orbital problems, total energy $E_{total} = E_k + E_p = \frac{1}{2}mv^2 - \frac{GMm}{r}$. For circular orbits, $E_k = -\frac{1}{2}E_p$, so $E_{total} = \frac{1}{2}E_p = -\frac{GMm}{2r}$. This relationship is frequently tested.

**中文:** 对于轨道问题，总能量$E_{total} = E_k + E_p = \frac{1}{2}mv^2 - \frac{GMm}{r}$。对于圆形轨道，$E_k = -\frac{1}{2}E_p$，所以$E_{total} = \frac{1}{2}E_p = -\frac{GMm}{2r}$。这个关系经常被测试。

## 4.3 Escape Velocity / 逃逸速度

### Explanation / 解释
**English:** [[Escape Velocity]] is the minimum speed an object must have at a given distance from a massive body to escape its gravitational field completely, with no further propulsion. It is derived from energy conservation: kinetic energy at launch equals the work needed to reach infinity (where potential energy is zero). The result is $v_{esc} = \sqrt{\frac{2GM}{r}}$, independent of the mass of the escaping object.

**中文:** [[Escape Velocity]]是物体在距离大质量天体给定距离处，无需进一步推进即可完全逃离其引力场所需的最小速度。它由能量守恒推导得出：发射时的动能等于到达无穷远处（势能为零）所需的功。结果为$v_{esc} = \sqrt{\frac{2GM}{r}}$，与逃离物体的质量无关。

### Physical Meaning / 物理意义
**English:** Escape velocity represents the "depth" of the gravitational potential well. A deeper well (more negative potential) requires higher escape velocity. For Earth, $v_{esc} \approx 11.2 \text{ km s}^{-1}$. For a black hole, $v_{esc} > c$ (speed of light), defining the event horizon at the Schwarzschild radius $r_s = \frac{2GM}{c^2}$.

**中文:** 逃逸速度代表引力势阱的"深度"。更深的阱（更负的势）需要更高的逃逸速度。对于地球，$v_{esc} \approx 11.2 \text{ km s}^{-1}$。对于黑洞，$v_{esc} > c$（光速），定义了史瓦西半径$r_s = \frac{2GM}{c^2}$处的事件视界。

### Common Misconceptions / 常见误区
- Thinking escape velocity depends on the mass of the escaping object (it doesn't)
- Confusing escape velocity with orbital velocity ($v_{orb} = \sqrt{\frac{GM}{r}}$)
- Thinking escape velocity means you must maintain that speed (it's the initial speed needed)

### Exam Tips / 考试提示
**English:** Derivation using $\frac{1}{2}mv^2 = \frac{GMm}{r}$ is a common exam question. Remember that $v_{esc} = \sqrt{2} \times v_{orb}$ for circular orbits. For a planet, escape velocity from the surface is $v_{esc} = \sqrt{\frac{2GM}{R}}$.

**中文:** 使用$\frac{1}{2}mv^2 = \frac{GMm}{r}$进行推导是常见的考试题目。记住对于圆形轨道，$v_{esc} = \sqrt{2} \times v_{orb}$。对于行星，从表面逃逸的速度为$v_{esc} = \sqrt{\frac{2GM}{R}}$。

## 4.4 Potential Gradients / 势梯度

### Explanation / 解释
**English:** The [[Potential Gradients|potential gradient]] is the rate of change of gravitational potential with distance: $g = -\frac{dV}{dr}$. The negative sign indicates that gravitational field strength $g$ points in the direction of decreasing potential (toward the mass). For a radial field, $g = -\frac{d}{dr}\left(-\frac{GM}{r}\right) = -\frac{GM}{r^2}$, which matches Newton's law of gravitation.

**中文:** [[Potential Gradients|势梯度]]是引力势随距离的变化率：$g = -\frac{dV}{dr}$。负号表示引力场强度$g$指向势减小的方向（朝向质量）。对于径向场，$g = -\frac{d}{dr}\left(-\frac{GM}{r}\right) = -\frac{GM}{r^2}$，这与牛顿万有引力定律一致。

### Physical Meaning / 物理意义
**English:** The potential gradient gives the gravitational field strength at a point. A steeper gradient means stronger gravitational field. On a graph of $V$ vs $r$, the gradient at any point equals $-g$. This relationship allows field strength to be determined from potential measurements, which is useful in geophysics and astrophysics.

**中文:** 势梯度给出某点的引力场强度。梯度越陡，引力场越强。在$V$对$r$的图上，任意点的梯度等于$-g$。这种关系允许从势测量中确定场强度，在地球物理学和天体物理学中很有用。

### Common Misconceptions / 常见误区
- Forgetting the negative sign in $g = -\frac{dV}{dr}$
- Thinking gradient of $V$ vs $r$ graph gives $g$ directly (it gives $-g$)
- Confusing potential gradient with field strength (they are related but different concepts)

### Exam Tips / 考试提示
**English:** In data analysis questions, you may be asked to plot $V$ vs $r$ and find the gradient. Remember gradient $= -g$. For uniform fields (near Earth), $g = -\frac{\Delta V}{\Delta r}$ where $\Delta V = gh$ (potential difference between two heights).

**中文:** 在数据分析题中，你可能需要绘制$V$对$r$的图并求梯度。记住梯度$= -g$。对于均匀场（地球附近），$g = -\frac{\Delta V}{\Delta r}$，其中$\Delta V = gh$（两个高度之间的势差）。

> 📷 **IMAGE PROMPT — GP-GRADIENT: Potential Gradient Graph**
> A graph of V vs r for a radial field. The curve is negative and approaches zero as r→∞. Tangent lines at two points show different gradients (steeper near r=0). Labels: "V", "r", "gradient = -g", "g₁ > g₂". Style: clean graph with labeled tangents. Exam importance: HIGH — common in data analysis questions.

# 5. Essential Equations / 核心公式

## 5.1 Gravitational Potential in a Radial Field / 径向场中的引力势

$$ V = -\frac{GM}{r} $$

| Symbol (符号) | Meaning (EN/CN) | Unit (单位) |
|---|---|---|
| $V$ | Gravitational potential / 引力势 | J kg⁻¹ |
| $G$ | Gravitational constant / 引力常数 | N m² kg⁻² |
| $M$ | Mass of central body / 中心天体质量 | kg |
| $r$ | Distance from center of mass / 距质心距离 | m |

**Derivation / 推导:** Not required for exam, but understanding that $V = \frac{W}{m}$ where $W = \int_{\infty}^{r} F \, dr = \int_{\infty}^{r} \frac{GMm}{r^2} \, dr = -\frac{GMm}{r}$ is helpful.

**Conditions / 适用条件:** Point mass or spherically symmetric mass distribution; outside the mass.

**Limitations / 局限性:** Does not apply inside a uniform sphere (potential varies differently).

**Rearrangements / 变形:**
- $M = -\frac{Vr}{G}$
- $r = -\frac{GM}{V}$

## 5.2 Gravitational Potential Energy / 引力势能

$$ E_p = mV = -\frac{GMm}{r} $$

| Symbol (符号) | Meaning (EN/CN) | Unit (单位) |
|---|---|---|
| $E_p$ | Gravitational potential energy / 引力势能 | J |
| $m$ | Mass of test object / 测试物体质量 | kg |
| $V$ | Gravitational potential / 引力势 | J kg⁻¹ |

**Derivation / 推导:** $E_p = mV$ follows directly from definition of potential.

**Conditions / 适用条件:** Two point masses; radial field.

**Limitations / 局限性:** For extended objects, use center of mass separation.

**Rearrangements / 变形:**
- $m = \frac{E_p}{V}$
- $r = -\frac{GMm}{E_p}$

## 5.3 Escape Velocity / 逃逸速度

$$ v_{esc} = \sqrt{\frac{2GM}{r}} $$

| Symbol (符号) | Meaning (EN/CN) | Unit (单位) |
|---|---|---|
| $v_{esc}$ | Escape velocity / 逃逸速度 | m s⁻¹ |
| $G$ | Gravitational constant / 引力常数 | N m² kg⁻² |
| $M$ | Mass of central body / 中心天体质量 | kg |
| $r$ | Distance from center / 距中心距离 | m |

**Derivation / 推导:** Energy conservation: $\frac{1}{2}mv_{esc}^2 + \left(-\frac{GMm}{r}\right) = 0 + 0$ (at infinity, KE=0, PE=0). Therefore $\frac{1}{2}mv_{esc}^2 = \frac{GMm}{r}$, giving $v_{esc} = \sqrt{\frac{2GM}{r}}$.

**Conditions / 适用条件:** No other forces; no propulsion after initial speed.

**Limitations / 局限性:** Does not account for atmospheric drag or other celestial bodies.

**Rearrangements / 变形:**
- $M = \frac{v_{esc}^2 r}{2G}$
- $r = \frac{2GM}{v_{esc}^2}$

## 5.4 Potential Gradient / 势梯度

$$ g = -\frac{dV}{dr} $$

| Symbol (符号) | Meaning (EN/CN) | Unit (单位) |
|---|---|---|
| $g$ | Gravitational field strength / 引力场强度 | N kg⁻¹ or m s⁻² |
| $V$ | Gravitational potential / 引力势 | J kg⁻¹ |
| $r$ | Distance / 距离 | m |

**Derivation / 推导:** From definition of work: $dW = F \, dr = mg \, dr$. Also $dW = m \, dV$. Therefore $mg \, dr = m \, dV$, so $g = \frac{dV}{dr}$. The negative sign indicates direction toward decreasing potential.

**Conditions / 适用条件:** Valid for any gravitational field.

**Limitations / 局限性:** Requires continuous function $V(r)$.

**Rearrangements / 变形:**
- $dV = -g \, dr$
- $\Delta V = -\int g \, dr$

## 5.5 Total Energy in Circular Orbit / 圆形轨道总能量

$$ E_{total} = E_k + E_p = -\frac{GMm}{2r} $$

| Symbol (符号) | Meaning (EN/CN) | Unit (单位) |
|---|---|---|
| $E_{total}$ | Total mechanical energy / 总机械能 | J |
| $E_k$ | Kinetic energy ($= \frac{GMm}{2r}$) / 动能 | J |
| $E_p$ | Potential energy ($= -\frac{GMm}{r}$) / 势能 | J |

**Derivation / 推导:** For circular orbit, centripetal force = gravitational force: $\frac{mv^2}{r} = \frac{GMm}{r^2}$, so $v^2 = \frac{GM}{r}$. Then $E_k = \frac{1}{2}mv^2 = \frac{GMm}{2r}$. $E_p = -\frac{GMm}{r}$. Therefore $E_{total} = \frac{GMm}{2r} - \frac{GMm}{r} = -\frac{GMm}{2r}$.

**Conditions / 适用条件:** Circular orbits only.

**Limitations / 局限性:** Does not apply to elliptical orbits.

**Rearrangements / 变形:**
- $r = -\frac{GMm}{2E_{total}}$
- $E_k = -E_{total}$ (for circular orbits)

# 6. Graphs and Relationships / 图表与关系

## 6.1 Gravitational Potential vs Distance (V vs r) / 引力势与距离关系图

**Axes / 坐标轴:** x-axis: $r$ (distance from center), y-axis: $V$ (gravitational potential)

**Shape / 形状:** Hyperbolic curve: $V = -\frac{GM}{r}$. Starts very negative near $r=0$, increases (becomes less negative) as $r$ increases, approaches $V=0$ asymptotically as $r \to \infty$.

**Gradient Meaning / 梯度含义:** Gradient $= \frac{dV}{dr} = -g$. The gradient is positive (curve slopes upward) but becomes less steep as $r$ increases. Steeper gradient = stronger gravitational field.

**Area Meaning / 面积含义:** Area under $V$ vs $r$ graph has no direct physical meaning. However, area under $g$ vs $r$ graph gives potential difference: $\Delta V = -\int g \, dr$.

**Exam Interpretation / 考试解读:**
- At any point, gradient $= -g$
- The curve never crosses $V=0$ (asymptotic approach)
- More massive objects have deeper potential wells (more negative at same $r$)

**Common Questions / 常见问题:**
- "Determine the gravitational field strength at point X from the graph"
- "Explain why the potential is negative"
- "Compare the potential wells of two planets with different masses"

> 📷 **IMAGE PROMPT — GP-VRGRAPH: V vs r Graph for Gravitational Potential**
> A graph showing V = -GM/r for two different masses (M₁ > M₂). The curve for M₁ is more negative at all r. Both curves approach V=0 as r→∞. Labels: "V", "r", "V = -GM₁/r", "V = -GM₂/r", "M₁ > M₂". Style: two curves on same axes, different colors. Exam importance: HIGH — fundamental graph for this topic.

## 6.2 Gravitational Field Strength vs Distance (g vs r) / 引力场强度与距离关系图

**Axes / 坐标轴:** x-axis: $r$ (distance from center), y-axis: $g$ (gravitational field strength)

**Shape / 形状:** Inverse square: $g = \frac{GM}{r^2}$. Starts very large near $r=0$, decreases rapidly, approaches $g=0$ as $r \to \infty$.

**Gradient Meaning / 梯度含义:** Gradient $= \frac{dg}{dr} = -\frac{2GM}{r^3}$. The gradient is negative and its magnitude decreases with $r$.

**Area Meaning / 面积含义:** Area under $g$ vs $r$ graph gives potential difference: $\Delta V = -\int_{r_1}^{r_2} g \, dr$. The negative sign means area is positive but potential difference is negative (potential decreases as you move inward).

**Exam Interpretation / 考试解读:**
- Inverse square relationship
- $g \propto \frac{1}{r^2}$
- Area between two $r$ values gives $|\Delta V|$

**Common Questions / 常见问题:**
- "Calculate the potential difference between two points using the area under the graph"
- "Compare field strengths at different distances"
- "Determine the mass of the central body from the graph"

## 6.3 Potential Energy vs Distance (Ep vs r) / 势能与距离关系图

**Axes / 坐标轴:** x-axis: $r$ (distance), y-axis: $E_p$ (gravitational potential energy)

**Shape / 形状:** Same shape as $V$ vs $r$ but scaled by $m$: $E_p = -\frac{GMm}{r}$. Hyperbolic, negative, approaches zero asymptotically.

**Gradient Meaning / 梯度含义:** Gradient $= \frac{dE_p}{dr} = \frac{GMm}{r^2} = mg$. The gradient equals the gravitational force (magnitude). Positive gradient means force is attractive (toward decreasing $r$).

**Area Meaning / 面积含义:** No direct physical meaning for area under $E_p$ vs $r$.

**Exam Interpretation / 考试解读:**
- Gradient gives force magnitude
- More negative $E_p$ = more tightly bound system
- Energy required to separate masses = change in $E_p$ toward zero

**Common Questions / 常见问题:**
- "Calculate the work done to move a satellite from one orbit to another"
- "Determine the force between two masses from the gradient"

# 7. Required Diagrams / 必备图表

## 7.1 Gravitational Potential Well / 引力势阱

> 📷 **IMAGE PROMPT — GP-WELL: Gravitational Potential Well of a Planet**
> A 3D-like diagram showing a planet at the center of a funnel-shaped potential well. The well is deepest near the planet and rises to zero at infinity. Equipotential surfaces are shown as concentric circles at different depths. Labels: "Planet", "Surface", "V = -GM/R", "V = -GM/2R", "V = -GM/3R", "V → 0 as r → ∞". A small ball (test mass) is shown at different positions. Style: 3D perspective, blue gradient for depth. Exam importance: HIGH — helps visualize why potential is negative and how it varies with distance.

## 7.2 Equipotential Surfaces and Field Lines / 等势面与场线

> 📷 **IMAGE PROMPT — GP-EQUIPOTENTIAL: Equipotential Surfaces Around a Planet**
> A 2D cross-section showing a planet (circle) at center. Concentric circles around it represent equipotential surfaces (labeled V₁, V₂, V₃, with V₁ < V₂ < V₃). Radial lines from center represent gravitational field lines, perpendicular to equipotential surfaces. Labels: "Equipotential surfaces", "Field lines", "V₁ (most negative)", "V₃ (least negative)", "Field lines perpendicular to equipotentials". Style: clean vector, dashed circles for equipotentials, solid arrows for field lines. Exam importance: HIGH — understanding perpendicular relationship is frequently tested.

## 7.3 Escape Velocity Diagram / 逃逸速度示意图

> 📷 **IMAGE PROMPT — GP-ESCAPE: Escape Velocity from a Planet**
> A diagram showing a planet with three trajectories from the same launch point: (1) Sub-orbital — falls back to surface (v < v_esc), (2) Orbital — enters circular orbit (v = v_orb), (3) Escape — continues to infinity (v ≥ v_esc). Labels: "Planet", "Launch point", "v < v_esc (falls back)", "v = v_orb (orbits)", "v ≥ v_esc (escapes)", "v_esc = √(2GM/R)". Style: curved trajectories, different colors for each case. Exam importance: MEDIUM — helps distinguish escape from orbital velocity.

## 7.4 Potential Gradient Graph / 势梯度图

> 📷 **IMAGE PROMPT — GP-GRADIENT2: Determining g from V vs r Graph**
> A graph of V vs r with two points A and B marked. A tangent line is drawn at point A, and the gradient is calculated. Labels: "V (J kg⁻¹)", "r (m)", "A", "B", "Tangent at A", "gradient = ΔV/Δr = -g_A". Below the graph, a small calculation box shows: "g_A = -gradient = -(-2.5 × 10⁷ / 2 × 10⁶) = 12.5 N kg⁻¹". Style: clean graph with construction lines. Exam importance: HIGH — common in data analysis questions.

# 8. Worked Examples / 典型例题

## Example 1: Gravitational Potential Calculation / 例1：引力势计算

### Question / 题目
**English:** The mass of Mars is $6.39 \times 10^{23}$ kg and its radius is $3.39 \times 10^6$ m. Calculate:
(a) The gravitational potential at the surface of Mars.
(b) The gravitational potential energy of a 500 kg satellite at the surface.
(c) The work done to move the satellite from the surface to a point where the potential is $-1.0 \times 10^7$ J kg⁻¹.
(G = $6.67 \times 10^{-11}$ N m² kg⁻²)

**中文:** 火星的质量为$6.39 \times 10^{23}$ kg，半径为$3.39 \times 10^6$ m。计算：
(a) 火星表面的引力势。
(b) 500 kg卫星在表面的引力势能。
(c) 将卫星从表面移动到势为$-1.0 \times 10^7$ J kg⁻¹的点所做的功。
(G = $6.67 \times 10^{-11}$ N m² kg⁻²)

### Image Prompt / 图片提示
> 📷 **IMAGE PROMPT — GP-EX1: Mars Potential Diagram**
> Simple diagram of Mars with radius R = 3.39 × 10⁶ m, showing surface point and a point at larger distance. Labels: "Mars M = 6.39×10²³ kg", "R = 3.39×10⁶ m", "Surface V = ?", "Point where V = -1.0×10⁷ J kg⁻¹". Style: simple schematic. Exam importance: LOW (just for visualization).

### Solution / 解答

**(a) Gravitational potential at surface / 表面引力势:**

$$ V = -\frac{GM}{r} = -\frac{(6.67 \times 10^{-11})(6.39 \times 10^{23})}{3.39 \times 10^6} $$

$$ V = -\frac{4.262 \times 10^{13}}{3.39 \times 10^6} = -1.257 \times 10^7 \text{ J kg}^{-1} $$

$$ V \approx -1.26 \times 10^7 \text{ J kg}^{-1} $$

**(b) Gravitational potential energy at surface / 表面引力势能:**

$$ E_p = mV = (500)(-1.257 \times 10^7) = -6.285 \times 10^9 \text{ J} $$

$$ E_p \approx -6.29 \times 10^9 \text{ J} $$

**(c) Work done to move satellite / 移动卫星所做的功:**

Work done = change in potential energy = $m\Delta V = m(V_2 - V_1)$

$$ W = 500[(-1.0 \times 10^7) - (-1.257 \times 10^7)] $$

$$ W = 500(2.57 \times 10^6) = 1.285 \times 10^9 \text{ J} $$

$$ W \approx 1.29 \times 10^9 \text{ J} $$

### Final Answer / 最终答案
(a) $V = -1.26 \times 10^7$ J kg⁻¹
(b) $E_p = -6.29 \times 10^9$ J
(c) $W = 1.29 \times 10^9$ J

### Examiner Notes / 考官点评
**English:** Common mistakes include: forgetting the negative sign in (a) and (b); using $mgh$ instead of $-\frac{GMm}{r}$; calculating work as $m(V_1 - V_2)$ instead of $m(V_2 - V_1)$. The positive work in (c) indicates work is done against the field (moving away from Mars).

**中文:** 常见错误包括：在(a)和(b)中忘记负号；使用$mgh$而不是$-\frac{GMm}{r}$；将功计算为$m(V_1 - V_2)$而不是$m(V_2 - V_1)$。(c)中的正功表示克服场做功（远离火星移动）。

## Example 2: Escape Velocity Derivation and Calculation / 例2：逃逸速度推导与计算

### Question / 题目
**English:** (a) Derive an expression for the escape velocity from the surface of a planet of mass $M$ and radius $R$.
(b) The escape velocity from Earth is $11.2$ km s⁻¹. Calculate the escape velocity from a planet with twice the mass of Earth and half the radius.
(c) Explain why the escape velocity does not depend on the mass of the escaping object.

**中文:** (a) 推导从质量为$M$、半径为$R$的行星表面逃逸的速度表达式。
(b) 地球的逃逸速度为$11.2$ km s⁻¹。计算从质量为地球两倍、半径为地球一半的行星逃逸的速度。
(c) 解释为什么逃逸速度不依赖于逃离物体的质量。

### Image Prompt / 图片提示
> 📷 **IMAGE PROMPT — GP-EX2: Escape Velocity Comparison**
> Two planets side by side: Earth (M, R) and Planet X (2M, R/2). Arrows show escape trajectories. Labels: "Earth: M, R, v_esc = 11.2 km/s", "Planet X: 2M, R/2, v_esc = ?". Style: simple comparison diagram. Exam importance: LOW (just for visualization).

### Solution / 解答

**(a) Derivation / 推导:**

Energy conservation: Total energy at surface = Total energy at infinity

$$ \frac{1}{2}mv_{esc}^2 + \left(-\frac{GMm}{R}\right) = 0 + 0 $$

At infinity, kinetic energy = 0 (object just reaches infinity with zero speed) and potential energy = 0 (by definition).

$$ \frac{1}{2}mv_{esc}^2 = \frac{GMm}{R} $$

$$ v_{esc}^2 = \frac{2GM}{R} $$

$$ v_{esc} = \sqrt{\frac{2GM}{R}} $$

**(b) Calculation for new planet / 新行星的计算:**

Let Earth parameters be $M_E$, $R_E$, $v_{esc,E} = 11.2$ km s⁻¹.

New planet: $M = 2M_E$, $R = \frac{1}{2}R_E$

$$ v_{esc} = \sqrt{\frac{2G(2M_E)}{\frac{1}{2}R_E}} = \sqrt{\frac{4GM_E}{\frac{1}{2}R_E}} = \sqrt{\frac{8GM_E}{R_E}} $$

$$ v_{esc} = \sqrt{8} \times \sqrt{\frac{2GM_E}{R_E}} = \sqrt{8} \times v_{esc,E} $$

$$ v_{esc} = \sqrt{8} \times 11.2 = 2.828 \times 11.2 = 31.7 \text{ km s}^{-1} $$

**(c) Explanation / 解释:**

**English:** The escape velocity is independent of the mass of the escaping object because both kinetic energy ($\frac{1}{2}mv^2$) and gravitational potential energy ($-\frac{GMm}{R}$) are proportional to $m$. When applying energy conservation, $m$ cancels out, leaving an expression that depends only on the planet's mass and radius.

**中文:** 逃逸速度与逃离物体的质量无关，因为动能（$\frac{1}{2}mv^2$）和引力势能（$-\frac{GMm}{R}$）都与$m$成正比。应用能量守恒时，$m$被消去，留下仅依赖于行星质量和半径的表达式。

### Final Answer / 最终答案
(a) $v_{esc} = \sqrt{\frac{2GM}{R}}$
(b) $v_{esc} = 31.7$ km s⁻¹
(c) $m$ cancels in energy conservation equation

### Examiner Notes / 考官点评
**English:** For part (a), full marks require showing the energy conservation equation explicitly. For part (b), the ratio method ($v_{esc} \propto \sqrt{M/R}$) is efficient. Common error: forgetting to square root. For part (c), explicitly stating that $m$ cancels is essential.

**中文:** 对于(a)部分，满分需要明确写出能量守恒方程。对于(b)部分，比例法（$v_{esc} \propto \sqrt{M/R}$）很高效。常见错误：忘记开平方根。对于(c)部分，明确说明$m$被消去至关重要。

# 9. Past Paper Question Types / 历年真题题型

| Question Type / 题型 | Frequency / 频率 | Difficulty / 难度 | Past Paper References / 真题索引 |
|---|---|---|---|
| Define gravitational potential / 定义引力势 | HIGH | EASY | 📝 *待填入* |
| Calculate V or Ep using $V = -GM/r$ / 计算V或Ep | HIGH | MEDIUM | 📝 *待填入* |
| Derive escape velocity / 推导逃逸速度 | HIGH | MEDIUM | 📝 *待填入* |
| Calculate escape velocity / 计算逃逸速度 | HIGH | MEDIUM | 📝 *待填入* |
| Potential gradient from graph / 从图表求势梯度 | MEDIUM | HARD | 📝 *待填入* |
| Work done in moving mass / 移动质量做功 | MEDIUM | MEDIUM | 📝 *待填入* |
| Total energy in orbit / 轨道总能量 | MEDIUM | HARD | 📝 *待填入* |
| Compare potentials of different planets / 比较不同行星的势 | LOW | MEDIUM | 📝 *待填入* |
| Equipotential surfaces / 等势面 | LOW | EASY | 📝 *待填入* |
| Data analysis: V vs r graph / 数据分析：V对r图 | MEDIUM | HARD | 📝 *待填入* |

> 📝 **题库整理中 / Question Bank Under Construction:** 本表格中的真题索引正在整理中。建议学生参考以下资源：CAIE 9702 Paper 4 (2016-2023) 和 Edexcel IAL Unit 4 (2018-2023) 的相关题目。典型题目包括：CAIE 9702/41/M/J/22 Q6 (gravitational potential and escape velocity), Edexcel WPH14/01 (potential gradient analysis)。

**Common Command Words / 常见指令词:**
- **Define / 定义:** State the precise meaning (e.g., "Define gravitational potential")
- **Derive / 推导:** Show step-by-step mathematical derivation
- **Calculate / 计算:** Use given data to find numerical answer
- **Explain / 解释:** Give reasons with physics principles
- **Determine / 确定:** Find value from graph or data
- **Sketch / 草图:** Draw approximate shape of graph
- **Compare / 比较:** State similarities and differences

# 10. Practical Skills Connections / 实验技能链接

**English:** Gravitational potential is primarily a theoretical topic, but practical skills are tested through:
- **Data Analysis (CAIE Paper 5, Edexcel Unit 6):** Plotting $V$ vs $r$ graphs, calculating gradients to find $g$, determining $M$ from graph intercepts
- **Uncertainties:** Propagating errors in $V = -\frac{GM}{r}$ calculations
- **Experimental Design:** Using Cavendish-type experiments to determine $G$, then calculating $V$ for known masses
- **Graph Skills:** Drawing tangents to $V$-$r$ curves, calculating areas under $g$-$r$ graphs
- **Log-Log Plots:** Verifying $V \propto 1/r$ relationship using logarithmic graphs

**中文:** 引力势主要是一个理论主题，但实验技能通过以下方式测试：
- **数据分析（CAIE Paper 5, Edexcel Unit 6）：** 绘制$V$对$r$图，计算梯度以找到$g$，从图截距确定$M$
- **不确定度：** 在$V = -\frac{GM}{r}$计算中传播误差
- **实验设计：** 使用卡文迪许型实验确定$G$，然后计算已知质量的$V$
- **图表技能：** 在$V$-$r$曲线上画切线，计算$g$-$r$图下的面积
- **对数-对数图：** 使用对数图验证$V \propto 1/r$关系

> 📋 **CIE Only:** CAIE Paper 5 may include questions on determining $G$ from experimental data, then using it to calculate gravitational potential. The "graphical method" for finding $g$ from $V$-$r$ gradient is specifically tested.
> 
> 📋 **Edexcel Only:** Edexcel Unit 6 often includes analysis of gravitational potential data from planetary missions. Core Practical 14 (determination of $g$) links to potential gradient concepts.

# 11. Concept Map / 概念图谱

```mermaid
graph TD
    A[Gravitational Potential] --> B[Definition: V = W/m]
    A --> C[Equation: V = -GM/r]
    A --> D[Gravitational Potential Energy: Ep = mV = -GMm/r]
    A --> E[Potential Gradient: g = -dV/dr]
    A --> F[Escape Velocity: v_esc = √(2GM/r)]
    A --> G[Equipotential Surfaces]
    
    B --> H[Work done from infinity]
    B --> I[Scalar quantity]
    B --> J[Negative sign convention]
    
    C --> K[Radial field]
    C --> L[Point mass assumption]
    C --> M[V → 0 as r → ∞]
    
    D --> N[Energy of system]
    D --> O[Links to orbital mechanics]
    
    E --> P[g = GM/r² from gradient]
    E --> Q[Graphical determination of g]
    
    F --> R[Energy conservation derivation]
    F --> S[Independent of escaping mass]
    F --> T[Schwarzschild radius]
    
    G --> U[Perpendicular to field lines]
    G --> V[No work done along surface]
    
    O --> W[Circular Orbits]
    O --> X[Total energy: Etotal = -GMm/2r]
    
    T --> Y[Black holes]
    T --> Z[Event horizon]
    
    style A fill:#f9f,stroke:#333,stroke-width:4px
    style B fill:#bbf,stroke:#333
    style C fill:#bbf,stroke:#333
    style D fill:#bbf,stroke:#333
    style E fill:#bbf,stroke:#333
    style F fill:#bbf,stroke:#333
    style G fill:#bbf,stroke:#333
```

**Prerequisites / 前置知识:** [[Gravitational Force and Field]], [[Kinetic Energy and Potential Energy]]
**Related Topics / 相关主题:** [[Circular Orbits]]
**Sub-topics / 子主题:** [[Gravitational Potential Energy in a Radial Field]], [[Gravitational Potential (V)]], [[Escape Velocity]], [[Potential Gradients]]

# 12. Examiner Insights / 考官洞察

**English:**

**Most Tested Ideas (CAIE 9702):**
1. Definition of gravitational potential (frequently appears as a 2-mark definition question)
2. Calculation of $V$ and $E_p$ using $V = -GM/r$ (standard calculation question)
3. Derivation of escape velocity using energy conservation (common 4-mark derivation)
4. Relationship between $g$ and $V$: $g = -dV/dr$ (often in data analysis)
5. Total energy in circular orbits: $E_{total} = -GMm/2r$ (linking to orbital mechanics)

**Most Tested Ideas (Edexcel IAL):**
1. Gravitational potential as scalar quantity (multiple choice)
2. Escape velocity calculations with ratio method
3. Potential gradient from $V$-$r$ graphs (data analysis in Unit 4)
4. Work done in moving between equipotential surfaces
5. Energy changes in satellite orbit transfers

**Mark Scheme Wording / 评分方案措辞:**
- "Work done per unit mass" (not "energy per unit mass" — though both accepted)
- "From infinity" must be mentioned in definition
- Negative sign must be present in equation
- "Gravitational field does work" for inward movement

**Common Lost Marks / 常见失分点:**
- Omitting negative sign in $V = -GM/r$
- Using $mgh$ instead of $-GMm/r$ for radial fields
- Not stating "from infinity" in definition
- Confusing potential $V$ with potential energy $E_p$
- Incorrect sign when calculating work done: $W = m(V_2 - V_1)$, not $m(V_1 - V_2)$

**High-Scoring Structures / 高分结构:**
- Always define symbols used in derivations
- Show energy conservation equation explicitly for escape velocity
- Use ratio method for comparative calculations
- Draw clear diagrams showing equipotential surfaces and field lines
- State assumptions (point mass, no other forces)

**中文:**

**最常考的概念（CAIE 9702）：**
1. 引力势的定义（常作为2分定义题出现）
2. 使用$V = -GM/r$计算$V$和$E_p$（标准计算题）
3. 使用能量守恒推导逃逸速度（常见的4分推导题）
4. $g$和$V$的关系：$g = -dV/dr$（常在数据分析中）
5. 圆形轨道的总能量：$E_{total} = -GMm/2r$（链接到轨道力学）

**最常考的概念（Edexcel IAL）：**
1. 引力势作为标量（选择题）
2. 使用比例法计算逃逸速度
3. 从$V$-$r$图求势梯度（Unit 4数据分析）
4. 在等势面之间移动做功
5. 卫星轨道转移中的能量变化

**评分方案措辞：**
- "单位质量所做的功"（不是"单位质量的能量"——虽然两者都接受）
- 定义中必须提到"从无穷远处"
- 方程中必须有负号
- 向内移动时"引力场做功"

**常见失分点：**
- 在$V = -GM/r$中省略负号
- 对径向场使用$mgh$而不是$-GMm/r$
- 定义中未说明"从无穷远处"
- 混淆势$V$和势能$E_p$
- 计算功时符号错误：$W = m(V_2 - V_1)$，不是$m(V_1 - V_2)$

**高分结构：**
- 在推导中始终定义所用符号
- 对逃逸速度明确写出能量守恒方程
- 对比较计算使用比例法
- 绘制清晰的等势面和场线图
- 说明假设条件（点质量，无其他力）

# 13. Quick Revision Sheet / 速查表

| Category / 类别 | Key Points / 要点 |
|---|---|
| **Definition / 定义** | $V = \frac{W}{m}$ = work done per unit mass from infinity / 单位质量从无穷远处移动所做的功 |
| **Equation / 方程** | $V = -\frac{GM}{r}$ (radial field) / 径向场 |
| **Sign / 符号** | Negative: field does work as mass moves inward / 负号：质量向内移动时场做功 |
| **Zero point / 零点** | $V = 0$ at $r = \infty$ / 无穷远处为零 |
| **Potential Energy / 势能** | $E_p = mV = -\frac{GMm}{r}$ (system energy) / 系统能量 |
| **Escape Velocity / 逃逸速度** | $v_{esc} = \sqrt{\frac{2GM}{r}}$ (independent of $m$) / 与$m$无关 |
| **Potential Gradient / 势梯度** | $g = -\frac{dV}{dr}$ (gradient of $V$-$r$ graph = $-g$) / $V$-$r$图梯度 = $-g$ |
| **Orbital Energy / 轨道能量** | $E_{total} = -\frac{GMm}{2r}$ (circular orbit) / 圆形轨道 |
| **Equipotentials / 等势面** | Surfaces of constant $V$; field lines perpendicular / 恒定$V$的面；场线垂直 |
| **Scalar / 标量** | $V$ adds algebraically for multiple masses / 多个质量的$V$代数相加 |
| **Key Ratio / 关键比例** | $v_{esc} = \sqrt{2} \times v_{orb}$ / 逃逸速度 = √2 × 轨道速度 |
| **Common Mistake / 常见错误** | Don't use $mgh$ for radial fields! / 径向场不要用$mgh$！ |

# 14. Metadata / 元数据

```yaml
title:
  en: Gravitational Potential
  cn: 引力势
subject: Physics
syllabus: [CAIE 9702, Edexcel IAL]
cie_ref: 15.2 (a-f)
edexcel_ref: WPH14 U4: 6.6-6.10
level: A2
node_type: topic_hub
difficulty: advanced
prerequisites:
  - Gravitational Force and Field
  - Kinetic Energy and Potential Energy
related_topics:
  - Circular Orbits
sub_topics:
  - Gravitational Potential Energy in a Radial Field
  - Gravitational Potential (V)
  - Escape Velocity
  - Potential Gradients
formula_count: 5
diagram_count: 6
exam_frequency: HIGH (appears in 80%+ of A2 papers)
language: bilingual_en_cn
last_updated: 2024-01
```

> 📝 **Note / 备注:** This is the HUB file for Gravitational Potential. Leaf nodes ([[Gravitational Potential Energy in a Radial Field]], [[Gravitational Potential (V)]], [[Escape Velocity]], [[Potential Gradients]]) contain detailed sub-topic content. This hub provides the overview and connections between all sub-topics.