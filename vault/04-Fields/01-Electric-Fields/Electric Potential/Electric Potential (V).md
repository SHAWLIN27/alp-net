---
# 1. Overview / 概述

**English:**
Electric Potential ($V$) is a scalar quantity that describes the electric potential energy per unit positive charge at a specific point in an electric field. Unlike electric field strength ($\vec{E}$), which is a vector, potential is a scalar, making it easier to calculate the total potential from multiple charges via simple addition. This sub-topic defines potential due to a point charge, explains the concept of zero potential at infinity, and explores the relationship between potential and work done. It is a cornerstone for understanding [[Electric Potential Energy]], [[Capacitance and Capacitors]], and the [[Motion of Charged Particles in Electric Fields]].

**中文:**
电势 ($V$) 是一个标量，描述电场中某一点单位正电荷所具有的电势能。与矢量电场强度 ($\vec{E}$) 不同，电势是标量，因此可以通过简单加法计算多个电荷产生的总电势。本子知识点定义了点电荷的电势，解释了无穷远处电势为零的概念，并探讨了电势与做功之间的关系。它是理解[[电势能]]、[[电容和电容器]]以及[[带电粒子在电场中的运动]]的基础。

---

# 2. Syllabus Learning Objectives / 考纲学习目标

| CAIE 9702 (18.2) | Edexcel IAL (WPH14 U4: 2.6-2.10) |
|-----------|-------------|
| Define electric potential at a point as the work done per unit positive charge in bringing a small test charge from infinity to that point. | Understand the concept of electric potential and its relationship with electric field strength. |
| State and use $V = \frac{Q}{4\pi\epsilon_0 r}$ for the potential in the field of a point charge. | Use the equation $V = \frac{Q}{4\pi\epsilon_0 r}$ for a point charge. |
| Calculate the combined potential due to several point charges. | Calculate the total electric potential at a point due to multiple point charges. |
| Recognise the analogy between electric and gravitational potential. | Understand the relationship between electric field strength and potential gradient: $E = -\frac{dV}{dr}$. |
| Understand the concept of equipotential surfaces. | Understand the concept of equipotential surfaces and their relationship to field lines. |

**Examiner Expectations / 考官期望:**
- **EN:** Students must be able to define potential precisely, distinguishing it from potential energy. They must be able to calculate potential for a point charge and for multiple charges, handling sign conventions correctly. Understanding that potential is a scalar is critical.
- **CN:** 学生必须能够精确定义电势，并将其与电势能区分开。必须能够计算点电荷和多个电荷的电势，正确处理符号约定。理解电势是标量至关重要。

---

# 3. Core Definitions / 核心定义

| Term (EN/CN) | Definition (EN) | Definition (CN) | Common Mistakes / 常见错误 |
|--------------|-----------------|-----------------|---------------------------|
| **Electric Potential** / 电势 | The work done per unit positive charge in bringing a small test charge from infinity to that point. | 将单位正电荷从无穷远处移动到该点所做的功。 | Confusing potential with potential energy. Potential is work done *per unit charge* (J C⁻¹). |
| **Potential Difference** / 电势差 | The work done per unit positive charge in moving a charge between two points in an electric field. | 在电场中将单位正电荷从一点移动到另一点所做的功。 | Forgetting that potential difference is the *difference* in potential, not the absolute value. |
| **Zero Potential (Infinity)** / 零电势（无穷远） | The reference point where the electric potential is defined as zero. For an isolated point charge, this is at infinity. | 电势被定义为零的参考点。对于孤立点电荷，该点在无穷远处。 | Assuming zero potential is always at the Earth's surface (this is a different convention used in circuits). |
| **Equipotential Surface** / 等势面 | A surface on which every point has the same electric potential. No work is done moving a charge along an equipotential surface. | 其上每一点都具有相同电势的表面。沿等势面移动电荷不做功。 | Thinking equipotential surfaces can cross (they cannot). |
| **Test Charge** / 试探电荷 | A small positive charge used to probe an electric field without significantly disturbing the field. | 用于探测电场而不显著干扰电场的小正电荷。 | Forgetting that the test charge must be small enough not to affect the field being measured. |

---

# 4. Key Concepts Explained / 关键概念详解

## 4.1 Definition of Electric Potential / 电势的定义

### Explanation / 解释
**English:**
Electric potential at a point is defined as the work done per unit positive charge in bringing a small test charge from infinity to that point. Mathematically, $V = \frac{W}{q}$, where $W$ is the work done and $q$ is the test charge. The unit is the volt (V), which is equivalent to joules per coulomb (J C⁻¹). This definition is directly linked to [[Electric Potential Energy]]: $V = \frac{E_p}{q}$.

**中文:**
某点的电势定义为将单位正电荷从无穷远处移动到该点所做的功。数学表达式为 $V = \frac{W}{q}$，其中 $W$ 是所做的功，$q$ 是试探电荷。单位是伏特 (V)，相当于焦耳每库仑 (J C⁻¹)。该定义直接与[[电势能]]相关：$V = \frac{E_p}{q}$。

### Physical Meaning / 物理意义
**English:**
Potential represents the "electrical pressure" or "potential to do work" at a point. A positive charge placed at a point of high positive potential has high potential energy and will naturally move towards a point of lower potential. It is a measure of the energy per unit charge stored in the field at that location.

**中文:**
电势表示某点的“电压力”或“做功的潜力”。放置在正高电势点的正电荷具有高电势能，会自然地向较低电势点移动。它是该位置电场中每单位电荷储存能量的量度。

### Common Misconceptions / 常见误区
- **EN:** Thinking potential is a vector. It is a scalar, so you add potentials algebraically, not vectorially.
- **CN:** 认为电势是矢量。它是标量，因此代数相加，而不是矢量相加。
- **EN:** Confusing potential with potential energy. Potential is energy per unit charge.
- **CN:** 混淆电势和电势能。电势是单位电荷的能量。
- **EN:** Believing potential is always positive. It can be negative for a negative charge.
- **CN:** 认为电势总是正的。对于负电荷，电势可以是负的。

### Exam Tips / 考试提示
- **EN:** Always state the reference point (infinity) in your definition. This is a mark-scoring detail.
- **CN:** 在定义中始终说明参考点（无穷远处）。这是得分点。
- **EN:** When calculating total potential from multiple charges, remember to include the sign of each charge.
- **CN:** 计算多个电荷的总电势时，记得包含每个电荷的符号。

> 📷 **IMAGE PROMPT — V01: Definition of Electric Potential**
> A diagram showing a positive test charge being moved from infinity (far left) to a point P near a positive point charge Q. An arrow shows the path. Labels: "Infinity (V=0)", "Work done = W", "Point P (V = W/q)". The field lines radiate outward from Q.

---

## 4.2 Potential Due to a Point Charge / 点电荷的电势

### Explanation / 解释
**English:**
For a point charge $Q$, the electric potential at a distance $r$ is given by:
$$ V = \frac{Q}{4\pi\epsilon_0 r} $$
This equation shows that potential is inversely proportional to distance. For a positive charge, $V$ is positive and decreases as $r$ increases. For a negative charge, $V$ is negative and increases (becomes less negative) as $r$ increases. This is derived from integrating the work done against the electric field from infinity to $r$.

**中文:**
对于点电荷 $Q$，距离 $r$ 处的电势由下式给出：
$$ V = \frac{Q}{4\pi\epsilon_0 r} $$
该方程表明电势与距离成反比。对于正电荷，$V$ 为正，并随 $r$ 增大而减小。对于负电荷，$V$ 为负，并随 $r$ 增大而增大（变得更负）。这是通过对从无穷远处到 $r$ 克服电场力所做的功进行积分推导得出的。

### Physical Meaning / 物理意义
**English:**
The potential is highest near the charge and falls off to zero at infinity. The sign of the potential tells you the direction a positive test charge would naturally move: from high potential to low potential.

**中文:**
电势在电荷附近最高，在无穷远处降至零。电势的符号告诉你正试探电荷的自然移动方向：从高电势到低电势。

### Common Misconceptions / 常见误区
- **EN:** Forgetting the $4\pi\epsilon_0$ constant in the denominator.
- **CN:** 忘记分母中的 $4\pi\epsilon_0$ 常数。
- **EN:** Thinking $V$ is proportional to $1/r^2$ (that's field strength, $E$).
- **CN:** 认为 $V$ 与 $1/r^2$ 成正比（那是电场强度 $E$）。

### Exam Tips / 考试提示
- **EN:** Remember that $V$ is a scalar, so the sign of $Q$ matters. A negative $Q$ gives a negative $V$.
- **CN:** 记住 $V$ 是标量，所以 $Q$ 的符号很重要。负 $Q$ 给出负 $V$。
- **EN:** For a system of charges, the total potential at a point is the algebraic sum of the potentials due to each charge.
- **CN:** 对于多个电荷系统，某点的总电势是每个电荷在该点产生的电势的代数和。

> 📷 **IMAGE PROMPT — V02: Potential vs Distance for Point Charge**
> A graph with two curves. One curve (for positive Q) shows V decreasing from +∞ near r=0 to 0 as r→∞. The other curve (for negative Q) shows V increasing from -∞ near r=0 to 0 as r→∞. Axes labelled: "V (V)" and "r (m)". The curves are hyperbolic (1/r shape).

---

# 5. Essential Equations / 核心公式

## Equation 1: Definition of Electric Potential

$$ V = \frac{W}{q} $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $V$ | Electric potential | 电势 | V (J C⁻¹) |
| $W$ | Work done to bring charge from infinity | 将电荷从无穷远处移动所做的功 | J |
| $q$ | Test charge | 试探电荷 | C |

**Derivation / 推导:** Definitional equation.
**Conditions / 适用条件:** Any electric field, with reference point at infinity.
**Limitations / 局限性:** Requires a clear definition of the reference point.

## Equation 2: Potential Due to a Point Charge

$$ V = \frac{Q}{4\pi\epsilon_0 r} $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $V$ | Electric potential at distance $r$ | 距离 $r$ 处的电势 | V |
| $Q$ | Source charge | 源电荷 | C |
| $\epsilon_0$ | Permittivity of free space | 真空介电常数 | F m⁻¹ |
| $r$ | Distance from charge | 距电荷的距离 | m |

**Derivation / 推导:** Derived from $V = -\int_{\infty}^{r} \vec{E} \cdot d\vec{r}$ where $E = \frac{Q}{4\pi\epsilon_0 r^2}$.
**Conditions / 适用条件:** Point charge or spherically symmetric charge distribution.
**Limitations / 局限性:** Assumes charge is in a vacuum. Does not apply inside a conductor.

## Equation 3: Total Potential from Multiple Charges

$$ V_{\text{total}} = \sum_{i} V_i = \sum_{i} \frac{Q_i}{4\pi\epsilon_0 r_i} $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $V_{\text{total}}$ | Total electric potential | 总电势 | V |
| $Q_i$ | $i$-th point charge | 第 $i$ 个点电荷 | C |
| $r_i$ | Distance from $i$-th charge to point | 第 $i$ 个电荷到该点的距离 | m |

**Derivation / 推导:** Superposition principle for scalar fields.
**Conditions / 适用条件:** Any configuration of point charges.
**Limitations / 局限性:** Does not account for induced charges on conductors.

> 📷 **IMAGE PROMPT — V03: Superposition of Potentials**
> A diagram showing two point charges (+Q and -Q) and a point P. Distances r1 and r2 are shown. The equation V_total = V1 + V2 is displayed. Arrows indicate the algebraic addition.

---

# 6. Graphs and Relationships / 图表与关系

## 6.1 V-r Graph for a Point Charge / 点电荷的 V-r 图

### Axes / 坐标轴
- **x-axis:** Distance from charge, $r$ (m) / 距电荷的距离 $r$ (m)
- **y-axis:** Electric potential, $V$ (V) / 电势 $V$ (V)

### Shape / 形状
- **Positive charge:** Hyperbolic curve decreasing from $+\infty$ at $r=0$ to $0$ as $r \to \infty$.
- **Negative charge:** Hyperbolic curve increasing from $-\infty$ at $r=0$ to $0$ as $r \to \infty$.
- **正电荷:** 双曲线，从 $r=0$ 处的 $+\infty$ 下降到 $r \to \infty$ 时的 $0$。
- **负电荷:** 双曲线，从 $r=0$ 处的 $-\infty$ 上升到 $r \to \infty$ 时的 $0$。

### Gradient Meaning / 斜率含义
- The gradient of the V-r graph is $\frac{dV}{dr}$, which is related to the electric field strength: $E = -\frac{dV}{dr}$.
- The negative sign indicates that the field points in the direction of decreasing potential.
- V-r 图的梯度是 $\frac{dV}{dr}$，与电场强度相关：$E = -\frac{dV}{dr}$。
- 负号表示电场指向电势降低的方向。

### Area Meaning / 面积含义
- The area under a V-r graph has no direct physical meaning in this context.
- V-r 图下的面积在此上下文中没有直接的物理意义。

### Exam Interpretation / 考试解读
- **EN:** You may be asked to sketch the V-r graph for a point charge or to use the gradient to find the electric field strength at a point.
- **CN:** 可能会要求你画出点电荷的 V-r 图，或利用梯度求某点的电场强度。

> 📷 **IMAGE PROMPT — V04: V-r Graph for Positive and Negative Charges**
> A single graph with two curves. One curve (solid line, labelled "+Q") shows V decreasing from +∞ to 0. The other curve (dashed line, labelled "-Q") shows V increasing from -∞ to 0. Both curves approach the r-axis asymptotically. Axes labelled "V" and "r".

---

# 7. Required Diagrams / 必备图表

## 7.1 Equipotential Surfaces for a Point Charge / 点电荷的等势面

### Description / 描述
**English:** Concentric spheres centred on the point charge. Each sphere represents a constant potential. The potential decreases as the radius increases. Field lines are radial and perpendicular to the equipotential surfaces.
**中文:** 以点电荷为中心的同心球面。每个球面代表一个恒定电势。电势随半径增大而减小。电场线是径向的，并与等势面垂直。

### Image Prompt / 图片生成提示
> 📷 **IMAGE PROMPT — V05: Equipotential Surfaces for a Point Charge**
> A 2D cross-section showing a positive point charge at the centre. Concentric circles (representing equipotential surfaces) are drawn around it. Radial arrows (field lines) point outward from the charge, perpendicular to the circles. Labels: "V1 > V2 > V3", "Field Lines", "Equipotential Surfaces".

### Labels Required / 需要标注
- Point charge (+Q) / 点电荷 (+Q)
- Equipotential surfaces (V1, V2, V3...) / 等势面 (V1, V2, V3...)
- Field lines (arrows) / 电场线（箭头）
- Perpendicular relationship / 垂直关系

### Exam Importance / 考试重要性
- **EN:** High. Understanding the relationship between field lines and equipotential surfaces is a common exam topic.
- **CN:** 高。理解电场线和等势面之间的关系是常见的考试主题。

---

# 8. Worked Examples / 典型例题

## Example 1: Potential Due to a Single Point Charge / 单个点电荷的电势

### Question / 题目
**English:**
A point charge of $+4.0 \times 10^{-9} \text{ C}$ is placed in a vacuum. Calculate the electric potential at a point $0.20 \text{ m}$ from the charge. ($\epsilon_0 = 8.85 \times 10^{-12} \text{ F m}^{-1}$)

**中文:**
将一个 $+4.0 \times 10^{-9} \text{ C}$ 的点电荷置于真空中。计算距该电荷 $0.20 \text{ m}$ 处的电势。（$\epsilon_0 = 8.85 \times 10^{-12} \text{ F m}^{-1}$）

### Solution / 解答
**Step 1:** Write down the formula.
$$ V = \frac{Q}{4\pi\epsilon_0 r} $$

**Step 2:** Substitute the values.
$$ V = \frac{4.0 \times 10^{-9}}{4\pi (8.85 \times 10^{-12})(0.20)} $$

**Step 3:** Calculate.
$$ V = \frac{4.0 \times 10^{-9}}{2.22 \times 10^{-11}} $$
$$ V = 180 \text{ V} $$

### Final Answer / 最终答案
**Answer:** $180 \text{ V}$ | **答案：** $180 \text{ V}$

### Quick Tip / 提示
- **EN:** Remember to use the correct value of $\frac{1}{4\pi\epsilon_0} = 8.99 \times 10^9 \text{ N m}^2 \text{ C}^{-2}$ if you prefer.
- **CN:** 如果方便，记得使用 $\frac{1}{4\pi\epsilon_0} = 8.99 \times 10^9 \text{ N m}^2 \text{ C}^{-2}$ 的正确值。

---

## Example 2: Total Potential from Two Charges / 两个电荷的总电势

### Question / 题目
**English:**
Two point charges, $Q_1 = +6.0 \times 10^{-9} \text{ C}$ and $Q_2 = -3.0 \times 10^{-9} \text{ C}$, are placed $0.30 \text{ m}$ apart. Calculate the electric potential at the midpoint between them.

**中文:**
两个点电荷 $Q_1 = +6.0 \times 10^{-9} \text{ C}$ 和 $Q_2 = -3.0 \times 10^{-9} \text{ C}$ 相距 $0.30 \text{ m}$。计算它们中点处的电势。

### Solution / 解答
**Step 1:** Determine the distance from each charge to the midpoint.
$$ r = \frac{0.30}{2} = 0.15 \text{ m} $$

**Step 2:** Calculate the potential due to $Q_1$.
$$ V_1 = \frac{Q_1}{4\pi\epsilon_0 r} = \frac{6.0 \times 10^{-9}}{4\pi (8.85 \times 10^{-12})(0.15)} $$
$$ V_1 = \frac{6.0 \times 10^{-9}}{1.67 \times 10^{-11}} = 359 \text{ V} $$

**Step 3:** Calculate the potential due to $Q_2$.
$$ V_2 = \frac{Q_2}{4\pi\epsilon_0 r} = \frac{-3.0 \times 10^{-9}}{4\pi (8.85 \times 10^{-12})(0.15)} $$
$$ V_2 = \frac{-3.0 \times 10^{-9}}{1.67 \times 10^{-11}} = -180 \text{ V} $$

**Step 4:** Add the potentials (scalar addition).
$$ V_{\text{total}} = V_1 + V_2 = 359 + (-180) = 179 \text{ V} $$

### Final Answer / 最终答案
**Answer:** $179 \text{ V}$ | **答案：** $179 \text{ V}$

### Quick Tip / 提示
- **EN:** Always include the sign of the charge when calculating potential. The total potential is the algebraic sum.
- **CN:** 计算电势时始终包含电荷的符号。总电势是代数和。

---

# 9. Past Paper Question Types / 历年真题题型

| Question Type / 题型 | Frequency / 频率 | Difficulty / 难度 | Past Paper References / 真题索引 |
|----------------------|------------------|------------------|-------------------------------|
| Definition of electric potential | High | Easy | 📝 *待填入* |
| Calculation of potential for a point charge | High | Medium | 📝 *待填入* |
| Calculation of total potential from multiple charges | Medium | Medium-Hard | 📝 *待填入* |
| V-r graph interpretation | Medium | Medium | 📝 *待填入* |
| Relationship between V and E (gradient) | Medium | Hard | 📝 *待填入* |
| Equipotential surfaces and field lines | High | Medium | 📝 *待填入* |

**Common Command Words / 常见指令词:**
- **EN:** Define, Calculate, Sketch, Explain, Determine, State
- **CN:** 定义，计算，画出，解释，确定，陈述

---

# 10. Practical Skills Connections / 实验技能链接

**English:**
While electric potential is often calculated theoretically, practical connections include:
- **Measurements:** Using a voltmeter to measure potential difference between two points in a circuit or field.
- **Uncertainties:** When measuring distances ($r$) and charges ($Q$), uncertainties propagate into the calculated potential.
- **Graph Plotting:** Plotting $V$ against $1/r$ for a point charge should yield a straight line through the origin, confirming the relationship $V \propto 1/r$.
- **Experimental Design:** Using a search coil or probe to map equipotential surfaces in an electrolytic tank or on conducting paper.

**中文:**
虽然电势通常是理论计算的，但实验联系包括：
- **测量:** 使用电压表测量电路或电场中两点之间的电势差。
- **不确定度:** 测量距离 ($r$) 和电荷 ($Q$) 时，不确定度会传递到计算出的电势中。
- **绘图:** 绘制点电荷的 $V$ 与 $1/r$ 关系图应得到一条通过原点的直线，证实 $V \propto 1/r$ 的关系。
- **实验设计:** 使用搜索线圈或探针在电解槽或导电纸上绘制等势面。

---

# 11. Concept Map / 概念图谱

```mermaid
graph TD
    %% Electric Potential Leaf Node
    V[Electric Potential V] --> DEF[Definition: Work per unit charge from infinity]
    V --> EQ[Equation: V = Q/(4πε₀r)]
    V --> SCALAR[Scalar Quantity: Algebraic addition]
    V --> GRAPH[V-r Graph: Hyperbolic shape]
    V --> EQUIP[Equipotential Surfaces: Perpendicular to field lines]

    %% Connections to other concepts
    V --> PE[Electric Potential Energy: Ep = qV]
    V --> E[Electric Field Strength: E = -dV/dr]
    V --> CAP[Capacitance: V = Q/C]

    %% Prerequisites
    E --> COULOMB[Coulomb's Law: F = Q₁Q₂/(4πε₀r²)]

    %% Sibling topics
    PE --> POT_GRAD[Potential Gradients]
    EQUIP --> MOTION[Motion of Charged Particles]

    %% Styling
    classDef leaf fill:#f9f,stroke:#333,stroke-width:2px;
    class V leaf;
```

---

# 12. Quick Revision Sheet / 速查表

| Category / 类别 | Key Points / 要点 |
|----------------|------------------|
| **Definition / 定义** | Work done per unit positive charge from infinity. $V = W/q$. Unit: V (J C⁻¹). / 将单位正电荷从无穷远处移动所做的功。$V = W/q$。单位：V (J C⁻¹)。 |
| **Key Formula / 核心公式** | $V = \frac{Q}{4\pi\epsilon_0 r}$ (point charge). Total potential: $V_{\text{total}} = \sum V_i$. / $V = \frac{Q}{4\pi\epsilon_0 r}$（点电荷）。总电势：$V_{\text{total}} = \sum V_i$。 |
| **Key Graph / 核心图表** | V-r graph: Hyperbolic curve. Gradient gives $E = -dV/dr$. / V-r 图：双曲线。梯度给出 $E = -dV/dr$。 |
| **Scalar Nature / 标量性质** | Potential is a scalar. Add potentials algebraically, including signs. / 电势是标量。代数相加，包括符号。 |
| **Equipotential Surfaces / 等势面** | Surfaces of constant V. No work done moving along them. Perpendicular to field lines. / 恒定 V 的表面。沿其移动不做功。垂直于电场线。 |
| **Exam Tip / 考试提示** | Always state "from infinity" in definitions. Include sign of charge in calculations. / 在定义中始终说明“从无穷远处”。计算中包含电荷的符号。 |