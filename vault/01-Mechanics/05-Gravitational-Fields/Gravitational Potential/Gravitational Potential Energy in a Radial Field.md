# Gravitational Potential Energy in a Radial Field / 径向场中的引力势能

---

## 1. Overview / 概述

**English:**
Gravitational Potential Energy (GPE) in a radial field extends the simple $mgh$ formula from uniform fields to the more general case of a point mass or spherical body. This sub-topic explores how GPE is defined, calculated, and applied in radial gravitational fields, where the force follows an inverse-square law. Understanding this concept is crucial for analyzing satellite motion, escape velocity, and energy changes in orbital mechanics. It builds directly on [[Gravitational Force and Field]] and [[Kinetic Energy and Potential Energy]], and is closely linked to [[Gravitational Potential (V)]] and [[Escape Velocity]].

**中文:**
径向场中的引力势能（GPE）将均匀场中的简单公式 $mgh$ 扩展到点质量或球体的更一般情况。本子知识点探讨了在径向引力场中如何定义、计算和应用引力势能，其中力遵循平方反比定律。理解这一概念对于分析卫星运动、逃逸速度和轨道力学中的能量变化至关重要。它直接建立在[[Gravitational Force and Field]]和[[Kinetic Energy and Potential Energy]]的基础上，并与[[Gravitational Potential (V)]]和[[Escape Velocity]]密切相关。

---

## 2. Core Definition / 核心定义

| Term (EN/CN) | Definition (EN) | Definition (CN) |
| ------------ | --------------- | --------------- |
| **Gravitational Potential Energy** / 引力势能 | The work done by an external agent to bring a mass from infinity to a point in a gravitational field, without acceleration. | 在无加速的情况下，将质量从无穷远处移动到引力场中某一点时外力所做的功。 |
| **Radial Field** / 径向场 | A gravitational field where field lines radiate outward from a point mass or spherical body, with strength following an inverse-square law. | 场线从点质量或球体向外辐射的引力场，场强遵循平方反比定律。 |
| **Infinity** / 无穷远 | A reference point where gravitational potential energy is defined as zero, representing a location beyond the influence of the gravitational field. | 引力势能被定义为零的参考点，代表超出引力场影响范围的位置。 |
| **Work Done** / 做功 | The product of force and displacement in the direction of the force, representing energy transfer. | 力与力方向上的位移的乘积，代表能量转移。 |
| **Negative Potential Energy** / 负势能 | A consequence of defining zero at infinity; GPE is always negative in a bound system, indicating that work must be done to separate the masses. | 将零点定义在无穷远处的结果；在束缚系统中引力势能始终为负，表示必须做功才能分离质量。 |

---

## 3. Key Concepts / 关键概念

**English:**

### The Definition of GPE in a Radial Field

In a uniform gravitational field (near Earth's surface), GPE is simply $mgh$, with zero at the surface. However, in a radial field, the gravitational force varies with distance according to Newton's law of gravitation:

$$F = -\frac{GMm}{r^2}$$

The negative sign indicates the force is attractive (toward the center). To define GPE consistently, we choose a reference point at infinity ($r \to \infty$), where the gravitational force is effectively zero. This means:

- **GPE at infinity = 0**
- **GPE at any finite distance is negative** (because work must be done *against* the field to move a mass to infinity)

### Physical Interpretation

The gravitational potential energy $U$ of a mass $m$ at distance $r$ from mass $M$ is:

$$U = -\frac{GMm}{r}$$

This represents the energy stored in the gravitational interaction between the two masses. The negative value indicates that the system is **bound** — energy must be supplied to separate the masses.

### Relationship to Gravitational Potential

The gravitational potential $V$ is the GPE per unit mass:

$$V = \frac{U}{m} = -\frac{GM}{r}$$

This links directly to [[Gravitational Potential (V)]].

### Common Pitfalls

1. **Confusing GPE with gravitational potential**: GPE ($U$) depends on both masses; potential ($V$) is per unit mass.
2. **Forgetting the negative sign**: Many students mistakenly write $U = +\frac{GMm}{r}$.
3. **Using $mgh$ in radial fields**: The $mgh$ formula only applies near Earth's surface where $g$ is approximately constant.
4. **Misinterpreting "work done by field" vs "work done against field"**: Work done *by* the gravitational field is positive when masses move closer; work done *against* the field (by an external agent) is positive when masses separate.

**中文:**

### 径向场中引力势能的定义

在均匀引力场（地球表面附近）中，引力势能简单表示为 $mgh$，零点在地表。然而，在径向场中，引力随距离变化，遵循牛顿万有引力定律：

$$F = -\frac{GMm}{r^2}$$

负号表示力是吸引的（指向中心）。为了一致地定义引力势能，我们选择无穷远处（$r \to \infty$）作为参考点，此处引力实际上为零。这意味着：

- **无穷远处的引力势能 = 0**
- **任何有限距离处的引力势能为负**（因为必须克服场做功才能将质量移动到无穷远）

### 物理意义

质量 $m$ 在距离质量 $M$ 为 $r$ 处的引力势能 $U$ 为：

$$U = -\frac{GMm}{r}$$

这代表两个质量之间引力相互作用中储存的能量。负值表示系统是**束缚的**——必须提供能量才能分离质量。

### 与引力势的关系

引力势 $V$ 是单位质量的引力势能：

$$V = \frac{U}{m} = -\frac{GM}{r}$$

这与[[Gravitational Potential (V)]]直接相关。

### 常见误区

1. **混淆引力势能与引力势**：引力势能（$U$）取决于两个质量；引力势（$V$）是单位质量的量。
2. **忘记负号**：许多学生错误地写成 $U = +\frac{GMm}{r}$。
3. **在径向场中使用 $mgh$**：$mgh$ 公式仅适用于地球表面附近 $g$ 近似恒定的情况。
4. **误解"场做功"与"克服场做功"**：质量靠近时，引力场*做正功*；质量分离时，外力*克服场做正功*。

> 📷 **IMAGE PROMPT — GPE-01: Gravitational Potential Energy Diagram**
>
> **English Prompt:**
> A clean vector diagram showing two masses M and m separated by distance r. The larger mass M is at the center, with radial field lines radiating outward. Mass m is shown at two positions: one closer (r₁) and one farther (r₂). Arrows indicate the direction of gravitational force (toward M). A graph below shows U vs r, with U = -GMm/r curve, highlighting that U approaches 0 as r → ∞ and becomes more negative as r decreases. Labels: "M (central mass)", "m (test mass)", "r₁", "r₂", "U₁ = -GMm/r₁", "U₂ = -GMm/r₂", "U = 0 at r = ∞". Color scheme: blue for field lines, red for force arrows, green for energy curve.
>
> **中文描述:**
> 一个清晰的矢量图，显示两个质量M和m相距距离r。较大的质量M在中心，径向场线向外辐射。质量m显示在两个位置：较近（r₁）和较远（r₂）。箭头表示引力方向（指向M）。下方的图表显示U与r的关系，曲线为U = -GMm/r，突出显示当r → ∞时U趋近于0，当r减小时U变得更负。标签："M（中心质量）"，"m（测试质量）"，"r₁"，"r₂"，"U₁ = -GMm/r₁"，"U₂ = -GMm/r₂"，"U = 0 at r = ∞"。配色方案：蓝色为场线，红色为力箭头，绿色为能量曲线。
>
> **Labels Required / 需要标注:**
> * M (central mass / 中心质量)
> * m (test mass / 测试质量)
> * r₁, r₂ (distances / 距离)
> * U₁, U₂ (potential energies / 势能)
> * U = 0 at r = ∞
>
> **Style / 风格:** Textbook vector diagram with graph
>
> **Exam Relevance / 考试关联:**
> Essential for understanding the inverse relationship between GPE and distance, and the concept of negative potential energy.

---

## 4. Formulas / 公式

### Primary Formula

$$U = -\frac{GMm}{r}$$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
| ------------- | ------------ | ------------ | ----------- |
| $U$ | Gravitational potential energy | 引力势能 | J (Joules) |
| $G$ | Gravitational constant ($6.67 \times 10^{-11} \text{ N·m}^2\text{/kg}^2$) | 万有引力常数 | N·m²/kg² |
| $M$ | Mass of central body | 中心天体质量 | kg |
| $m$ | Mass of test object | 测试物体质量 | kg |
| $r$ | Distance between centers of mass | 质心间距离 | m |

### Change in GPE

$$\Delta U = U_f - U_i = -\frac{GMm}{r_f} - \left(-\frac{GMm}{r_i}\right) = GMm\left(\frac{1}{r_i} - \frac{1}{r_f}\right)$$

### Work Done by Gravitational Field

$$W_{\text{field}} = -\Delta U = GMm\left(\frac{1}{r_f} - \frac{1}{r_i}\right)$$

### Derivation / 推导

Starting from the definition of work:

$$W = \int_{r_i}^{r_f} F \, dr = \int_{r_i}^{r_f} \left(-\frac{GMm}{r^2}\right) dr$$

$$W = -GMm \int_{r_i}^{r_f} r^{-2} \, dr = -GMm \left[-\frac{1}{r}\right]_{r_i}^{r_f}$$

$$W = GMm\left(\frac{1}{r_f} - \frac{1}{r_i}\right)$$

Since work done by the field equals the negative change in potential energy:

$$\Delta U = -W = -GMm\left(\frac{1}{r_f} - \frac{1}{r_i}\right) = GMm\left(\frac{1}{r_i} - \frac{1}{r_f}\right)$$

Setting $U = 0$ at $r = \infty$ and $r_i = \infty$, $r_f = r$:

$$U = GMm\left(\frac{1}{\infty} - \frac{1}{r}\right) = -\frac{GMm}{r}$$

### Conditions / 适用条件

- **Point masses or spherically symmetric bodies** (e.g., planets, stars)
- **Outside the surface** of the central body (inside, the formula changes due to mass distribution)
- **Non-relativistic** (Newtonian gravity)
- **Zero at infinity** reference point

---

## 5. Image Prompt / 图片提示

> 📷 **IMAGE PROMPT — GPE-02: Energy Changes in Orbital Motion**
>
> **English Prompt:**
> A 3D rendered diagram showing a satellite in elliptical orbit around Earth. The orbit is drawn as an ellipse with Earth at one focus. Two key points are marked: perigee (closest approach) and apogee (farthest point). At each point, bar charts show the relative magnitudes of kinetic energy (KE), gravitational potential energy (GPE), and total mechanical energy (TME). At perigee: KE is high (tall bar), GPE is low (short negative bar), TME is constant. At apogee: KE is low (short bar), GPE is high (taller negative bar), TME is same as at perigee. Labels: "Perigee (r_min)", "Apogee (r_max)", "KE + GPE = TME (constant)". Color scheme: blue for KE, red for GPE, green for TME. Background: dark space with stars.
>
> **中文描述:**
> 一个3D渲染图，显示卫星绕地球的椭圆轨道。轨道画为椭圆，地球在一个焦点上。标记两个关键点：近地点（最近点）和远地点（最远点）。在每个点处，条形图显示动能（KE）、引力势能（GPE）和总机械能（TME）的相对大小。在近地点：KE高（长条），GPE低（短负条），TME恒定。在远地点：KE低（短条），GPE高（较长的负条），TME与近地点相同。标签："Perigee (r_min)"，"Apogee (r_max)"，"KE + GPE = TME (constant)"。配色方案：蓝色为KE，红色为GPE，绿色为TME。背景：深色星空。
>
> **Labels Required / 需要标注:**
> * Perigee / 近地点
> * Apogee / 远地点
> * KE (kinetic energy / 动能)
> * GPE (gravitational potential energy / 引力势能)
> * TME (total mechanical energy / 总机械能)
> * r_min, r_max
>
> **Style / 风格:** 3D render with bar charts
>
> **Exam Relevance / 考试关联:**
> Crucial for understanding energy conservation in orbits and the relationship between orbital position and energy distribution.

---

## 6. Worked Example / 典型例题

### Example 1: Calculating GPE Change

### Question / 题目

**English:**
A satellite of mass $m = 500 \text{ kg}$ is moved from an orbit of radius $r_1 = 7.0 \times 10^6 \text{ m}$ to an orbit of radius $r_2 = 1.0 \times 10^7 \text{ m}$ around Earth. Given $M_{\text{Earth}} = 5.97 \times 10^{24} \text{ kg}$ and $G = 6.67 \times 10^{-11} \text{ N·m}^2\text{/kg}^2$, calculate:

(a) The gravitational potential energy at each orbit.
(b) The change in gravitational potential energy.
(c) The work done by the gravitational field during this move.

**中文:**
一颗质量 $m = 500 \text{ kg}$ 的卫星从半径 $r_1 = 7.0 \times 10^6 \text{ m}$ 的轨道移动到半径 $r_2 = 1.0 \times 10^7 \text{ m}$ 的轨道绕地球运行。已知 $M_{\text{地球}} = 5.97 \times 10^{24} \text{ kg}$，$G = 6.67 \times 10^{-11} \text{ N·m}^2\text{/kg}^2$，计算：

(a) 每个轨道的引力势能。
(b) 引力势能的变化。
(c) 在此移动过程中引力场做的功。

### Solution / 解答

**Part (a):**

$$U_1 = -\frac{GMm}{r_1} = -\frac{(6.67 \times 10^{-11})(5.97 \times 10^{24})(500)}{7.0 \times 10^6}$$

$$U_1 = -\frac{1.99 \times 10^{17}}{7.0 \times 10^6} = -2.84 \times 10^{10} \text{ J}$$

$$U_2 = -\frac{GMm}{r_2} = -\frac{(6.67 \times 10^{-11})(5.97 \times 10^{24})(500)}{1.0 \times 10^7}$$

$$U_2 = -\frac{1.99 \times 10^{17}}{1.0 \times 10^7} = -1.99 \times 10^{10} \text{ J}$$

**Part (b):**

$$\Delta U = U_2 - U_1 = (-1.99 \times 10^{10}) - (-2.84 \times 10^{10}) = +8.5 \times 10^9 \text{ J}$$

The positive change means GPE increases (becomes less negative) as the satellite moves to a higher orbit.

**Part (c):**

$$W_{\text{field}} = -\Delta U = -8.5 \times 10^9 \text{ J}$$

The negative work done by the field indicates that the field does negative work (i.e., an external agent must do positive work to raise the satellite).

### Final Answer / 最终答案

**Answer:**
(a) $U_1 = -2.84 \times 10^{10} \text{ J}$, $U_2 = -1.99 \times 10^{10} \text{ J}$
(b) $\Delta U = +8.5 \times 10^9 \text{ J}$
(c) $W_{\text{field}} = -8.5 \times 10^9 \text{ J}$

**答案:**
(a) $U_1 = -2.84 \times 10^{10} \text{ J}$，$U_2 = -1.99 \times 10^{10} \text{ J}$
(b) $\Delta U = +8.5 \times 10^9 \text{ J}$
(c) $W_{\text{field}} = -8.5 \times 10^9 \text{ J}$

### Quick Tip / 提示

**English:**
Remember that GPE is always negative in a bound system. When an object moves to a higher orbit (larger $r$), GPE increases (becomes less negative). The work done *by* the field is negative when the object moves away from the central mass.

**中文:**
记住在束缚系统中引力势能始终为负。当物体移动到更高轨道（更大的 $r$）时，引力势能增加（变得更不负面）。当物体远离中心质量时，场*做的功*为负。

---

## 7. Flashcards / 闪卡

**Flashcard 1:**
Q (EN): What is the formula for gravitational potential energy in a radial field?
Q (CN): 径向场中引力势能的公式是什么？
A (EN): $U = -\frac{GMm}{r}$, where $G$ is the gravitational constant, $M$ is the central mass, $m$ is the test mass, and $r$ is the distance between their centers.
A (CN): $U = -\frac{GMm}{r}$，其中 $G$ 是万有引力常数，$M$ 是中心质量，$m$ 是测试质量，$r$ 是它们质心之间的距离。

**Flashcard 2:**
Q (EN): Why is gravitational potential energy always negative in a bound system?
Q (CN): 为什么在束缚系统中引力势能始终为负？
A (EN): Because zero is defined at infinity. Work must be done against the gravitational field to separate the masses, so the system has negative energy when bound.
A (CN): 因为零点定义在无穷远处。必须克服引力场做功才能分离质量，所以束缚时系统具有负能量。

**Flashcard 3:**
Q (EN): How does gravitational potential energy change when a satellite moves to a higher orbit?
Q (CN): 当卫星移动到更高轨道时，引力势能如何变化？
A (EN): GPE increases (becomes less negative) because $r$ increases, making $-\frac{GMm}{r}$ closer to zero.
A (CN): 引力势能增加（变得更不负面），因为 $r$ 增加，使 $-\frac{GMm}{r}$ 更接近零。

**Flashcard 4:**
Q (EN): What is the relationship between gravitational potential energy $U$ and gravitational potential $V$?
Q (CN): 引力势能 $U$ 和引力势 $V$ 之间有什么关系？
A (EN): $V = \frac{U}{m} = -\frac{GM}{r}$. Gravitational potential is GPE per unit mass.
A (CN): $V = \frac{U}{m} = -\frac{GM}{r}$。引力势是单位质量的引力势能。

**Flashcard 5:**
Q (EN): What is the work done by the gravitational field when a mass moves from $r_i$ to $r_f$?
Q (CN): 当质量从 $r_i$ 移动到 $r_f$ 时，引力场做的功是多少？
A (EN): $W_{\text{field}} = GMm\left(\frac{1}{r_f} - \frac{1}{r_i}\right)$. This equals $-\Delta U$.
A (CN): $W_{\text{field}} = GMm\left(\frac{1}{r_f} - \frac{1}{r_i}\right)$。这等于 $-\Delta U$。

---

## 8. Metadata / 元数据

```yaml
title:
  en: Gravitational Potential Energy in a Radial Field
  cn: 径向场中的引力势能
parent_topic: Gravitational Potential
parent_hub: "[[Gravitational Potential]]"
subject: Physics
syllabus:
  - CAIE 9702: 15.2 (a-f)
  - Edexcel IAL: WPH14 U4: 6.6-6.10
level: A2
node_type: leaf_concept
difficulty: advanced
related_leaf_nodes:
  - "[[Gravitational Potential (V)]]"
  - "[[Escape Velocity]]"
  - "[[Potential Gradients]]"
prerequisites:
  - "[[Gravitational Force and Field]]"
  - "[[Kinetic Energy and Potential Energy]]"
related_topics:
  - "[[Circular Orbits]]"
language: bilingual_en_cn