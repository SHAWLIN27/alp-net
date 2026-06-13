---
# Gravitational Potential Energy in a Radial Field / 径向场中的引力势能

---

# 1. Overview / 概述

**English:**
This sub-topic extends the concept of gravitational potential energy ($E_p$) from the uniform field approximation (where $E_p = mgh$) to the more general and accurate **radial field** model. In a radial field, the gravitational force varies with distance ($F \propto 1/r^2$), so the potential energy is no longer linear with height. Instead, we define $E_p$ relative to infinity, leading to the key equation $E_p = -\frac{GMm}{r}$. This is a foundational concept for understanding [[Gravitational Potential (V)]], [[Escape Velocity]], and [[Circular Orbits]]. It is crucial for A2 students as it unifies mechanics and field theory, and is frequently tested in both CAIE and Edexcel exams.

**中文:**
本子知识点将引力势能 ($E_p$) 的概念从均匀场近似（其中 $E_p = mgh$）扩展到更通用、更精确的**径向场**模型。在径向场中，引力随距离变化（$F \propto 1/r^2$），因此势能不再与高度成线性关系。相反，我们定义相对于无穷远处的势能，从而得出关键方程 $E_p = -\frac{GMm}{r}$。这是理解[[Gravitational Potential (V)]]、[[Escape Velocity]]和[[Circular Orbits]]的基础概念。对于A2学生来说至关重要，因为它统一了力学和场论，并且在CAIE和Edexcel考试中经常出现。

---

# 2. Syllabus Learning Objectives / 考纲学习目标

| CAIE 9702 (15.2) | Edexcel IAL (WPH14 U4: 6.6-6.10) |
|-----------|-------------|
| (a) Define gravitational potential energy in a radial field. | 6.6 Know that gravitational potential energy is defined as the work done in moving a mass from infinity to a point. |
| (b) Derive and use $E_p = -\frac{GMm}{r}$. | 6.7 Derive and use $E_p = -\frac{GMm}{r}$. |
| (c) Understand that $E_p$ is negative and approaches zero at infinity. | 6.8 Understand the significance of the negative sign. |
| (d) Calculate the work done in moving a mass between two points in a radial field. | 6.9 Calculate the change in potential energy ($\Delta E_p$) between two points. |
| (e) Relate $E_p$ to gravitational potential $V$ ($E_p = mV$). | 6.10 Use the relationship $E_p = mV$ to solve problems. |
| (f) Apply conservation of energy in radial fields (e.g., rocket launch). | (Implicit in 6.6-6.10 and escape velocity). |

**Examiner Expectations / 考官期望:**
- **EN:** Students must be able to derive the formula using integration of $F = GMm/r^2$. They must explain why $E_p$ is negative and why infinity is the zero point. They must be able to calculate $\Delta E_p$ for a mass moving between two radial distances.
- **CN:** 学生必须能够通过对 $F = GMm/r^2$ 进行积分来推导公式。他们必须解释为什么 $E_p$ 是负的，以及为什么无穷远处是零点。他们必须能够计算质量在两个径向距离之间移动时的 $\Delta E_p$。

---

# 3. Core Definitions / 核心定义

| Term (EN/CN) | Definition (EN) | Definition (CN) | Common Mistakes / 常见错误 |
|--------------|-----------------|-----------------|---------------------------|
| **Gravitational Potential Energy ($E_p$)** / 引力势能 | The work done in moving a mass from infinity to a point in a gravitational field. | 将质量从无穷远处移动到引力场中某一点所做的功。 | Confusing with gravitational potential ($V$). $E_p$ is energy (J), $V$ is potential (J/kg). |
| **Radial Field** / 径向场 | A field where the gravitational force acts along lines radiating from a central mass, with strength varying as $1/r^2$. | 引力沿从中心质量辐射的线作用，强度随 $1/r^2$ 变化的场。 | Thinking the field is uniform. |
| **Zero Point at Infinity** / 无穷远处零点 | The reference point where $E_p = 0$; the point where the gravitational force is effectively zero. | 参考点，其中 $E_p = 0$；引力实际上为零的点。 | Forgetting that $E_p$ is defined relative to infinity, not the surface of the planet. |
| **Work Done ($W$)** / 做功 | The energy transferred when a force moves an object; in this context, $W = \Delta E_p$. | 力移动物体时传递的能量；在此上下文中，$W = \Delta E_p$. | Using $W = Fd$ directly, forgetting that $F$ is not constant. |
| **Change in Potential Energy ($\Delta E_p$)** / 势能变化 | The difference in $E_p$ between two points in the field: $\Delta E_p = E_{p2} - E_{p1} = GMm(1/r_1 - 1/r_2)$. | 场中两点之间 $E_p$ 的差值：$\Delta E_p = E_{p2} - E_{p1} = GMm(1/r_1 - 1/r_2)$. | Getting the sign wrong; work done by the field is negative $\Delta E_p$. |

---

# 4. Key Concepts Explained / 关键概念详解

## 4.1 Derivation of $E_p = -\frac{GMm}{r}$ / $E_p = -\frac{GMm}{r}$ 的推导

### Explanation / 解释
**English:**
Gravitational potential energy is defined as the **work done** against the gravitational field to bring a mass $m$ from infinity to a point at distance $r$ from a mass $M$. Since the gravitational force is attractive and varies with distance, we must integrate.

The force on $m$ due to $M$ is:
$$ F = \frac{GMm}{r^2} $$
To move $m$ *against* this force (i.e., away from $M$), we must apply an equal and opposite force. The work done $dW$ to move $m$ a small distance $dr$ away from $M$ is:
$$ dW = F \, dr = \frac{GMm}{r^2} \, dr $$
To find the total work done from infinity ($r = \infty$) to a point $r = r$, we integrate:
$$ W = \int_{\infty}^{r} \frac{GMm}{r^2} \, dr = GMm \int_{\infty}^{r} r^{-2} \, dr $$
$$ W = GMm \left[ -\frac{1}{r} \right]_{\infty}^{r} = GMm \left( -\frac{1}{r} + \frac{1}{\infty} \right) = -\frac{GMm}{r} $$
Since work done on the mass is stored as potential energy, $E_p = W = -\frac{GMm}{r}$.

**中文:**
引力势能定义为克服引力场将质量 $m$ 从无穷远处移动到距离质量 $M$ 为 $r$ 的点所做的**功**。由于引力是吸引力且随距离变化，我们必须进行积分。

$m$ 受到 $M$ 的力为：
$$ F = \frac{GMm}{r^2} $$
为了*克服*这个力移动 $m$（即远离 $M$），我们必须施加一个大小相等、方向相反的力。将 $m$ 移动一小段距离 $dr$ 远离 $M$ 所做的功 $dW$ 为：
$$ dW = F \, dr = \frac{GMm}{r^2} \, dr $$
为了找到从无穷远处 ($r = \infty$) 到点 $r = r$ 所做的总功，我们进行积分：
$$ W = \int_{\infty}^{r} \frac{GMm}{r^2} \, dr = GMm \int_{\infty}^{r} r^{-2} \, dr $$
$$ W = GMm \left[ -\frac{1}{r} \right]_{\infty}^{r} = GMm \left( -\frac{1}{r} + \frac{1}{\infty} \right) = -\frac{GMm}{r} $$
由于对质量所做的功以势能的形式储存，因此 $E_p = W = -\frac{GMm}{r}$。

### Physical Meaning / 物理意义
**English:**
The negative sign indicates that the gravitational potential energy is **negative** because work is done *by* the field (not against it) when the mass moves from infinity towards $M$. The field does positive work, converting potential energy into kinetic energy. At infinity, $E_p = 0$. As $r$ decreases, $E_p$ becomes more negative, meaning the mass is more tightly bound to $M$.

**中文:**
负号表示引力势能为**负**，因为当质量从无穷远处向 $M$ 移动时，是场*做*功（而不是克服场做功）。场做正功，将势能转化为动能。在无穷远处，$E_p = 0$。随着 $r$ 减小，$E_p$ 变得更负，意味着质量与 $M$ 的结合更紧密。

### Common Misconceptions / 常见误区
- **EN:** Thinking $E_p$ can be positive. It is always negative or zero.
- **CN:** 认为 $E_p$ 可以是正的。它总是负的或零。
- **EN:** Confusing $E_p$ with gravitational potential $V$. $E_p$ is for a specific mass $m$; $V$ is per unit mass.
- **CN:** 混淆 $E_p$ 和引力势 $V$。$E_p$ 是针对特定质量 $m$ 的；$V$ 是每单位质量的。
- **EN:** Forgetting that the formula applies to point masses or spherical masses (outside the sphere).
- **CN:** 忘记该公式适用于点质量或球形质量（在球体外部）。

### Exam Tips / 考试提示
- **EN:** Always state the reference point (infinity) when defining $E_p$. Use the formula $E_p = -\frac{GMm}{r}$ for radial fields, not $mgh$.
- **CN:** 在定义 $E_p$ 时，始终说明参考点（无穷远处）。对于径向场，使用公式 $E_p = -\frac{GMm}{r}$，而不是 $mgh$。

> 📷 **IMAGE PROMPT — GRAPH: Gravitational Potential Energy vs Distance**
> A graph showing $E_p$ on the y-axis and $r$ on the x-axis. The curve is a negative reciprocal function ($-1/r$), starting from a large negative value near $r=0$, rising steeply, and asymptotically approaching $E_p=0$ as $r \to \infty$. Label the axes: "Gravitational Potential Energy, $E_p$ / J" and "Distance from centre, $r$ / m". Mark the point at $r = R$ (planet surface) with a label "$E_p = -GMm/R$".

---

# 5. Essential Equations / 核心公式

## Equation 1: Gravitational Potential Energy in a Radial Field

$$ E_p = -\frac{GMm}{r} $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $E_p$ | Gravitational potential energy | 引力势能 | J (Joules) |
| $G$ | Gravitational constant ($6.67 \times 10^{-11} \, \text{N m}^2 \text{kg}^{-2}$) | 引力常数 | N m² kg⁻² |
| $M$ | Mass of the central body | 中心天体的质量 | kg |
| $m$ | Mass of the object in the field | 在场中的物体质量 | kg |
| $r$ | Distance from the centre of $M$ to the object | 从 $M$ 中心到物体的距离 | m |

**Derivation / 推导:** See Section 4.1.
**Conditions / 适用条件:**
- **EN:** For point masses or spherical masses (outside the sphere). $r$ must be measured from the centre of $M$.
- **CN:** 适用于点质量或球形质量（在球体外部）。$r$ 必须从 $M$ 的中心测量。
**Limitations / 局限性:**
- **EN:** Does not apply inside a massive body (e.g., inside a planet) where the field is not simply $1/r^2$.
- **CN:** 不适用于大质量天体内部（例如行星内部），因为那里的场不是简单的 $1/r^2$。

## Equation 2: Change in Gravitational Potential Energy

$$ \Delta E_p = E_{p2} - E_{p1} = GMm \left( \frac{1}{r_1} - \frac{1}{r_2} \right) $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $\Delta E_p$ | Change in gravitational potential energy | 引力势能的变化 | J |
| $r_1$ | Initial distance from centre | 初始距离（从中心） | m |
| $r_2$ | Final distance from centre | 最终距离（从中心） | m |

**Derivation / 推导:** $\Delta E_p = -\frac{GMm}{r_2} - \left( -\frac{GMm}{r_1} \right) = GMm \left( \frac{1}{r_1} - \frac{1}{r_2} \right)$.
**Conditions / 适用条件:** Same as Equation 1.
**Limitations / 局限性:** Same as Equation 1.

## Equation 3: Relationship with Gravitational Potential

$$ E_p = mV $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $E_p$ | Gravitational potential energy | 引力势能 | J |
| $m$ | Mass of the object | 物体的质量 | kg |
| $V$ | Gravitational potential at that point ($V = -GM/r$) | 该点的引力势 | J/kg |

**Derivation / 推导:** By definition, $V = E_p / m$.
**Conditions / 适用条件:** Always true for a given point in a gravitational field.
**Limitations / 局限性:** None.

---

# 6. Graphs and Relationships / 图表与关系

## 6.1 $E_p$ vs $r$ Graph / $E_p$ 与 $r$ 关系图

### Axes / 坐标轴
- **X-axis:** Distance from centre, $r$ / m (距离中心，$r$ / 米)
- **Y-axis:** Gravitational potential energy, $E_p$ / J (引力势能，$E_p$ / 焦耳)

### Shape / 形状
- **EN:** A negative reciprocal curve ($-1/r$). It is steep near the centre and flattens out as $r$ increases, asymptotically approaching $E_p = 0$ from below.
- **CN:** 负倒数曲线 ($-1/r$)。在中心附近很陡，随着 $r$ 增加而变平，从下方渐近接近 $E_p = 0$。

### Gradient Meaning / 斜率含义
- **EN:** The gradient of the $E_p$ vs $r$ graph is equal to the **negative of the gravitational force** ($-F$). This is because $F = -dE_p/dr$.
- **CN:** $E_p$ 与 $r$ 关系图的斜率等于**引力的负值** ($-F$)。这是因为 $F = -dE_p/dr$。

### Area Meaning / 面积含义
- **EN:** The area under the $F$ vs $r$ graph (force-distance graph) gives the work done, which equals $\Delta E_p$.
- **CN:** $F$ 与 $r$ 关系图（力-距离图）下的面积给出所做的功，等于 $\Delta E_p$。

### Exam Interpretation / 考试解读
- **EN:** Be able to sketch this graph. Understand that moving from $r_1$ to $r_2$ (where $r_2 > r_1$) results in a less negative $E_p$, so $\Delta E_p$ is positive (work must be done against the field).
- **CN:** 能够画出此图。理解从 $r_1$ 移动到 $r_2$（其中 $r_2 > r_1$）会导致 $E_p$ 负值减小，因此 $\Delta E_p$ 为正（必须克服场做功）。

---

# 7. Required Diagrams / 必备图表

## 7.1 $E_p$ vs $r$ Graph / $E_p$ 与 $r$ 关系图

### Description / 描述
- **EN:** A graph showing the variation of gravitational potential energy with distance from the centre of a planet.
- **CN:** 显示引力势能随距行星中心距离变化的图表。

### Image Prompt / 图片生成提示
> 📷 **IMAGE PROMPT — DIAGRAM: Ep vs r Graph**
> A clear, labeled graph. X-axis: "Distance from centre, r / m". Y-axis: "Gravitational potential energy, Ep / J". The curve is a smooth, decreasing function that is steep near the origin and asymptotically approaches the x-axis (Ep=0) as r increases. Mark a point on the curve at r = R (planet surface) and label it "Ep = -GMm/R". Draw a horizontal dashed line at Ep=0 labeled "Ep = 0 at infinity". Use a grid for clarity.

### Labels Required / 需要标注
- **EN:** Axes, curve, asymptote at $E_p=0$, point at $r=R$ (planet surface).
- **CN:** 坐标轴、曲线、$E_p=0$ 处的渐近线、$r=R$（行星表面）处的点。

### Exam Importance / 考试重要性
- **EN:** High. Students are often asked to sketch or interpret this graph.
- **CN:** 高。学生经常被要求画出或解释此图。

---

# 8. Worked Examples / 典型例题

## Example 1: Calculating $\Delta E_p$ for a Satellite / 计算卫星的 $\Delta E_p$

### Question / 题目
**English:**
A satellite of mass $m = 500 \text{ kg}$ is moved from a circular orbit of radius $r_1 = 7.0 \times 10^6 \text{ m}$ to a higher orbit of radius $r_2 = 1.0 \times 10^7 \text{ m}$ around Earth. Earth's mass $M = 5.97 \times 10^{24} \text{ kg}$ and $G = 6.67 \times 10^{-11} \text{ N m}^2 \text{kg}^{-2}$.
(a) Calculate the change in gravitational potential energy of the satellite.
(b) Explain whether this change is positive or negative.

**中文:**
一颗质量为 $m = 500 \text{ kg}$ 的卫星从半径 $r_1 = 7.0 \times 10^6 \text{ m}$ 的圆形轨道移动到半径 $r_2 = 1.0 \times 10^7 \text{ m}$ 的更高轨道。地球质量 $M = 5.97 \times 10^{24} \text{ kg}$，$G = 6.67 \times 10^{-11} \text{ N m}^2 \text{kg}^{-2}$。
(a) 计算卫星引力势能的变化。
(b) 解释这个变化是正的还是负的。

### Solution / 解答

**Step 1: Write down the formula for $\Delta E_p$.**
$$ \Delta E_p = GMm \left( \frac{1}{r_1} - \frac{1}{r_2} \right) $$

**Step 2: Substitute the values.**
$$ \Delta E_p = (6.67 \times 10^{-11})(5.97 \times 10^{24})(500) \left( \frac{1}{7.0 \times 10^6} - \frac{1}{1.0 \times 10^7} \right) $$

**Step 3: Calculate the bracket.**
$$ \frac{1}{7.0 \times 10^6} = 1.4286 \times 10^{-7} $$
$$ \frac{1}{1.0 \times 10^7} = 1.0 \times 10^{-7} $$
$$ \text{Bracket} = (1.4286 - 1.0) \times 10^{-7} = 0.4286 \times 10^{-7} = 4.286 \times 10^{-8} $$

**Step 4: Calculate the product.**
$$ \Delta E_p = (6.67 \times 10^{-11})(5.97 \times 10^{24})(500)(4.286 \times 10^{-8}) $$
$$ \Delta E_p = (6.67 \times 5.97 \times 500 \times 4.286) \times 10^{-11+24-8} $$
$$ \Delta E_p = (6.67 \times 5.97 \times 500 \times 4.286) \times 10^{5} $$
$$ \Delta E_p \approx (6.67 \times 5.97 \times 500 \times 4.286) \times 10^{5} $$
$$ \Delta E_p \approx (6.67 \times 5.97 \approx 39.82) \times 500 \approx 19910 \times 4.286 \approx 85300 $$
$$ \Delta E_p \approx 8.53 \times 10^4 \times 10^{5} = 8.53 \times 10^9 \text{ J} $$

**Step 5: Determine the sign.**
Since $r_2 > r_1$, the satellite is moving to a higher orbit (further from Earth). $E_p$ becomes less negative, so $\Delta E_p$ is **positive**.

### Final Answer / 最终答案
**Answer:** (a) $\Delta E_p = +8.53 \times 10^9 \text{ J}$ (b) Positive, because the satellite moves to a higher orbit where $E_p$ is less negative. | **答案：** (a) $\Delta E_p = +8.53 \times 10^9 \text{ J}$ (b) 正的，因为卫星移动到更高轨道，那里 $E_p$ 的负值更小。

### Quick Tip / 提示
- **EN:** Always check the sign of $\Delta E_p$. Moving away from the planet requires work input, so $\Delta E_p$ is positive.
- **CN:** 始终检查 $\Delta E_p$ 的符号。远离行星需要输入功，因此 $\Delta E_p$ 为正。

---

# 9. Past Paper Question Types / 历年真题题型

| Question Type / 题型 | Frequency / 频率 | Difficulty / 难度 | Past Paper References / 真题索引 |
|----------------------|------------------|------------------|-------------------------------|
| Derivation of $E_p = -GMm/r$ | Medium | Medium | 📝 *待填入* |
| Calculation of $\Delta E_p$ for a satellite or rocket | High | Medium | 📝 *待填入* |
| Sketching $E_p$ vs $r$ graph | Medium | Easy | 📝 *待填入* |
| Explaining the negative sign | High | Easy | 📝 *待填入* |
| Combining $E_p$ with kinetic energy for total energy in orbits | High | Hard | 📝 *待填入* |

**Common Command Words / 常见指令词:**
- **EN:** Define, Derive, Calculate, Sketch, Explain, State
- **CN:** 定义，推导，计算，画出，解释，陈述

---

# 10. Practical Skills Connections / 实验技能链接

**English:**
While gravitational potential energy in a radial field is not directly measurable in a school lab, the concept is linked to practical skills in several ways:
- **Graphing and Data Analysis:** Students must be able to plot $E_p$ vs $r$ graphs and interpret gradients.
- **Uncertainties:** When calculating $\Delta E_p$, uncertainties in $r$ (distance) propagate. Students should be able to estimate the percentage uncertainty in $\Delta E_p$ given uncertainties in $r_1$ and $r_2$.
- **Experimental Design:** The concept is used in the design of satellite launches and space missions, where energy calculations are critical.

**中文:**
虽然径向场中的引力势能无法在学校实验室中直接测量，但该概念在以下几个方面与实验技能相关：
- **绘图和数据分析：** 学生必须能够绘制 $E_p$ 与 $r$ 的关系图并解释斜率。
- **不确定度：** 在计算 $\Delta E_p$ 时，$r$（距离）的不确定度会传播。学生应该能够根据 $r_1$ 和 $r_2$ 的不确定度估算 $\Delta E_p$ 的百分比不确定度。
- **实验设计：** 该概念用于卫星发射和太空任务的设计，其中能量计算至关重要。

---

# 11. Concept Map / 概念图谱

```mermaid
graph TD
    %% Show connections for this leaf node
    A[Gravitational Potential Energy in a Radial Field] --> B[Definition: Work done from infinity]
    A --> C[Key Formula: Ep = -GMm/r]
    A --> D[Change in Ep: ΔEp = GMm(1/r1 - 1/r2)]
    A --> E[Relationship: Ep = mV]
    
    B --> F[Prerequisite: Gravitational Force F = GMm/r²]
    C --> G[Integration of F dr]
    C --> H[Negative Sign: Field does work]
    D --> I[Work Done by/against Field]
    E --> J[Gravitational Potential V]
    
    A --> K[Applications]
    K --> L[Satellite Orbits]
    K --> M[Escape Velocity]
    K --> N[Rocket Launches]
    
    F --> O[Parent Hub: Gravitational Potential]
    J --> O
    L --> P[Related: Circular Orbits]
    M --> Q[Related: Escape Velocity]
    
    style A fill:#f9f,stroke:#333,stroke-width:2px
    style O fill:#bbf,stroke:#333,stroke-width:2px
    style P fill:#bfb,stroke:#333,stroke-width:2px
    style Q fill:#bfb,stroke:#333,stroke-width:2px
```

---

# 12. Quick Revision Sheet / 速查表

| Category / 类别 | Key Points / 要点 |
|----------------|------------------|
| **Definition / 定义** | Work done to bring mass from infinity to a point. / 将质量从无穷远处移动到某点所做的功。 |
| **Key Formula / 核心公式** | $E_p = -\frac{GMm}{r}$ |
| **Change in Ep / 势能变化** | $\Delta E_p = GMm \left( \frac{1}{r_1} - \frac{1}{r_2} \right)$ |
| **Sign / 符号** | Always negative; zero at infinity. / 总是负的；在无穷远处为零。 |
| **Key Graph / 核心图表** | $E_p$ vs $r$: Negative reciprocal curve, asymptote at $E_p=0$. / $E_p$ 与 $r$ 关系图：负倒数曲线，渐近线在 $E_p=0$。 |
| **Exam Tip / 考试提示** | Always use $E_p = -GMm/r$ for radial fields, not $mgh$. Check sign of $\Delta E_p$. / 对于径向场始终使用 $E_p = -GMm/r$，而不是 $mgh$。检查 $\Delta E_p$ 的符号。 |
| **Common Mistake / 常见错误** | Confusing $E_p$ with $V$; forgetting the negative sign. / 混淆 $E_p$ 和 $V$；忘记负号。 |