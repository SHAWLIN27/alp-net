# KE and PE in SHM / 简谐运动中的动能与势能

---

# 1. Overview / 概述

**English:**
This sub-topic explores how kinetic energy (KE) and potential energy (PE) vary during simple harmonic motion. In SHM, energy continuously transforms between KE and PE while the total mechanical energy remains constant (in the absence of damping). Understanding these energy changes is fundamental to analyzing oscillatory systems, from mass-spring systems to pendulums. This leaf node focuses specifically on the mathematical expressions for KE and PE in SHM, their instantaneous values, and how they relate to displacement and velocity. It connects directly to [[Energy-Time Graphs for SHM]] and [[Energy-Displacement Graphs for SHM]], and builds on [[Simple Harmonic Motion]] and [[Kinetic Energy and Potential Energy]].

**中文:**
本子知识点探讨简谐运动中动能（KE）和势能（PE）如何变化。在简谐运动中，能量在动能和势能之间不断转换，而总机械能保持不变（无阻尼情况下）。理解这些能量变化对于分析振荡系统（从弹簧-质量系统到单摆）至关重要。本叶节点专注于简谐运动中动能和势能的数学表达式、瞬时值以及它们与位移和速度的关系。它与[[Energy-Time Graphs for SHM]]和[[Energy-Displacement Graphs for SHM]]直接相连，并建立在[[Simple Harmonic Motion]]和[[Kinetic Energy and Potential Energy]]的基础上。

---

# 2. Syllabus Learning Objectives / 考纲学习目标

| CAIE 9702 | Edexcel IAL |
|-----------|-------------|
| 17.2(a): Show an understanding of and use the expressions for kinetic energy and potential energy in SHM | 7.6: Derive and use expressions for kinetic energy and potential energy in SHM |
| 17.2(b): Recall and use the expression for total energy of an oscillator | 7.7: Understand that total energy is constant in undamped SHM |
| 17.2(c): Sketch and interpret energy-time and energy-displacement graphs | 7.8: Sketch and interpret energy variation graphs |

**Examiner Expectations / 考官期望:**
- **English:** Students must be able to derive KE and PE expressions from SHM equations, calculate instantaneous values, and interpret energy graphs. Common exam tasks include finding maximum KE/PE, determining total energy, and analyzing energy conservation.
- **中文:** 学生必须能够从简谐运动方程推导动能和势能表达式，计算瞬时值，并解释能量图。常见考试任务包括求最大动能/势能、确定总能量以及分析能量守恒。

---

# 3. Core Definitions / 核心定义

| Term (EN/CN) | Definition (EN) | Definition (CN) | Common Mistakes / 常见错误 |
|--------------|-----------------|-----------------|---------------------------|
| **Kinetic Energy (KE)** / 动能 | The energy of an oscillator due to its motion, given by $E_k = \frac{1}{2} m v^2$ | 振荡体由于运动而具有的能量，由 $E_k = \frac{1}{2} m v^2$ 给出 | Confusing KE with total energy; forgetting that KE is maximum at equilibrium |
| **Potential Energy (PE)** / 势能 | The energy stored in the oscillator due to its displacement from equilibrium, given by $E_p = \frac{1}{2} k x^2$ | 振荡体由于偏离平衡位置而储存的能量，由 $E_p = \frac{1}{2} k x^2$ 给出 | Thinking PE is zero only at equilibrium; confusing with gravitational PE |
| **Total Mechanical Energy** / 总机械能 | The sum of KE and PE, which remains constant in undamped SHM: $E_{total} = \frac{1}{2} k A^2 = \frac{1}{2} m v_{max}^2$ | 动能和势能之和，在无阻尼简谐运动中保持不变：$E_{total} = \frac{1}{2} k A^2 = \frac{1}{2} m v_{max}^2$ | Forgetting that total energy depends on amplitude squared |
| **Amplitude (A)** / 振幅 | The maximum displacement from equilibrium, which determines the total energy of the oscillator | 从平衡位置的最大位移，决定振荡体的总能量 | Confusing amplitude with displacement at any instant |
| **Equilibrium Position** / 平衡位置 | The position where net force is zero and PE is minimum (zero for ideal SHM) | 净力为零且势能最小（理想简谐运动中为零）的位置 | Thinking KE is zero at equilibrium (it's actually maximum) |

---

# 4. Key Concepts Explained / 关键概念详解

## 4.1 Energy Conservation in SHM / 简谐运动中的能量守恒

### Explanation / 解释
**English:**
In undamped [[Simple Harmonic Motion]], the total mechanical energy $E_{total}$ is constant. Energy continuously transforms between [[Kinetic Energy and Potential Energy]]:
- At maximum displacement ($x = \pm A$): velocity $v = 0$, so KE = 0, PE = maximum = $E_{total}$
- At equilibrium ($x = 0$): velocity $v = v_{max}$, so KE = maximum = $E_{total}$, PE = 0
- At any intermediate position: $E_{total} = KE + PE = \frac{1}{2} m v^2 + \frac{1}{2} k x^2$

This conservation principle is analogous to energy conservation in [[Damped and Forced Oscillations - Resonance]], but without energy loss.

**中文:**
在无阻尼[[Simple Harmonic Motion]]中，总机械能 $E_{total}$ 保持不变。能量在[[Kinetic Energy and Potential Energy]]之间不断转换：
- 在最大位移处（$x = \pm A$）：速度 $v = 0$，所以 KE = 0，PE = 最大值 = $E_{total}$
- 在平衡位置（$x = 0$）：速度 $v = v_{max}$，所以 KE = 最大值 = $E_{total}$，PE = 0
- 在任何中间位置：$E_{total} = KE + PE = \frac{1}{2} m v^2 + \frac{1}{2} k x^2$

这一守恒原理类似于[[Damped and Forced Oscillations - Resonance]]中的能量守恒，但没有能量损失。

### Physical Meaning / 物理意义
**English:**
The constant total energy means that as the oscillator moves, the "currency" of energy changes form but the total amount never changes. This is why an ideal pendulum or mass-spring system oscillates forever — energy is merely recycled between kinetic and potential forms.

**中文:**
总能量恒定意味着当振荡体运动时，能量的"货币"形式发生变化，但总量从未改变。这就是为什么理想单摆或弹簧-质量系统会永远振荡——能量只是在动能和势能形式之间循环利用。

### Common Misconceptions / 常见误区
- ❌ **Misconception:** KE and PE are always equal. → **Truth:** They are equal only at specific positions ($x = \pm A/\sqrt{2}$).
- ❌ **Misconception:** Total energy depends on mass only. → **Truth:** Total energy depends on $k$ and $A^2$ (or $m$ and $v_{max}^2$).
- ❌ **Misconception:** PE is always positive. → **Truth:** In SHM, PE is defined as zero at equilibrium and positive elsewhere.

### Exam Tips / 考试提示
- ✅ Always check if damping is mentioned — if not, assume total energy is constant.
- ✅ Use $E_{total} = \frac{1}{2} k A^2$ when given spring constant and amplitude.
- ✅ Use $E_{total} = \frac{1}{2} m v_{max}^2$ when given mass and maximum velocity.

> 📷 **IMAGE PROMPT — KE-PE-01: Energy Transformation in SHM**
> A clear diagram showing a mass on a spring at three positions: (1) at maximum extension (x=+A) with PE maximum and KE=0, (2) at equilibrium (x=0) with KE maximum and PE=0, (3) at maximum compression (x=-A) with PE maximum and KE=0. Arrows show energy flow between KE and PE. Labels indicate the energy values at each position.

---

## 4.2 Mathematical Expressions for KE and PE / 动能和势能的数学表达式

### Explanation / 解释
**English:**
Using the SHM equations $x = A \sin(\omega t)$ and $v = A\omega \cos(\omega t)$, we derive:

**Kinetic Energy:**
$$E_k = \frac{1}{2} m v^2 = \frac{1}{2} m (A\omega \cos(\omega t))^2 = \frac{1}{2} m A^2 \omega^2 \cos^2(\omega t)$$

Since $\omega^2 = k/m$ for a mass-spring system:
$$E_k = \frac{1}{2} k A^2 \cos^2(\omega t)$$

**Potential Energy:**
$$E_p = \frac{1}{2} k x^2 = \frac{1}{2} k (A \sin(\omega t))^2 = \frac{1}{2} k A^2 \sin^2(\omega t)$$

**Total Energy:**
$$E_{total} = E_k + E_p = \frac{1}{2} k A^2 (\cos^2(\omega t) + \sin^2(\omega t)) = \frac{1}{2} k A^2$$

**中文:**
利用简谐运动方程 $x = A \sin(\omega t)$ 和 $v = A\omega \cos(\omega t)$，我们推导出：

**动能：**
$$E_k = \frac{1}{2} m v^2 = \frac{1}{2} m (A\omega \cos(\omega t))^2 = \frac{1}{2} m A^2 \omega^2 \cos^2(\omega t)$$

由于弹簧-质量系统中 $\omega^2 = k/m$：
$$E_k = \frac{1}{2} k A^2 \cos^2(\omega t)$$

**势能：**
$$E_p = \frac{1}{2} k x^2 = \frac{1}{2} k (A \sin(\omega t))^2 = \frac{1}{2} k A^2 \sin^2(\omega t)$$

**总能量：**
$$E_{total} = E_k + E_p = \frac{1}{2} k A^2 (\cos^2(\omega t) + \sin^2(\omega t)) = \frac{1}{2} k A^2$$

### Physical Meaning / 物理意义
**English:**
The $\cos^2$ and $\sin^2$ terms show that KE and PE oscillate at twice the frequency of the displacement. This means energy changes occur twice as fast as the motion itself — a key insight for [[Energy-Time Graphs for SHM]].

**中文:**
$\cos^2$ 和 $\sin^2$ 项表明动能和势能以位移频率的两倍振荡。这意味着能量变化的速度是运动本身的两倍——这是理解[[Energy-Time Graphs for SHM]]的关键。

### Common Misconceptions / 常见误区
- ❌ **Misconception:** KE and PE vary at the same frequency as displacement. → **Truth:** They vary at $2f$ (twice the frequency).
- ❌ **Misconception:** The expressions for PE always involve $\frac{1}{2}kx^2$. → **Truth:** This is specific to elastic SHM; for pendulums, PE is gravitational.

### Exam Tips / 考试提示
- ✅ Remember $\omega^2 = k/m$ — this substitution is frequently tested.
- ✅ The identity $\sin^2\theta + \cos^2\theta = 1$ is the mathematical proof of energy conservation.
- ✅ For pendulums, use $E_p = mgh$ where $h$ relates to angular displacement.

> 📋 **CIE Only:** CAIE 9702 expects students to recall and use $E_p = \frac{1}{2}kx^2$ for mass-spring systems and $E_p = mgh$ for pendulums.
> 📋 **Edexcel Only:** Edexcel IAL requires derivation of KE and PE expressions from SHM equations, including the use of $\omega = 2\pi f$.

---

## 4.3 Energy at Specific Positions / 特定位置的能量

### Explanation / 解释
**English:**
The energy distribution depends on displacement:

| Position | Displacement $x$ | Velocity $v$ | KE | PE |
|----------|------------------|--------------|----|----|
| Equilibrium | 0 | $\pm A\omega$ | $\frac{1}{2}kA^2$ | 0 |
| Maximum displacement | $\pm A$ | 0 | 0 | $\frac{1}{2}kA^2$ |
| Half amplitude | $\pm A/2$ | $\pm \frac{\sqrt{3}}{2}A\omega$ | $\frac{3}{8}kA^2$ | $\frac{1}{8}kA^2$ |
| Equal KE and PE | $\pm A/\sqrt{2}$ | $\pm A\omega/\sqrt{2}$ | $\frac{1}{4}kA^2$ | $\frac{1}{4}kA^2$ |

**中文:**
能量分布取决于位移：

| 位置 | 位移 $x$ | 速度 $v$ | 动能 | 势能 |
|------|----------|----------|------|------|
| 平衡位置 | 0 | $\pm A\omega$ | $\frac{1}{2}kA^2$ | 0 |
| 最大位移 | $\pm A$ | 0 | 0 | $\frac{1}{2}kA^2$ |
| 半振幅 | $\pm A/2$ | $\pm \frac{\sqrt{3}}{2}A\omega$ | $\frac{3}{8}kA^2$ | $\frac{1}{8}kA^2$ |
| 动能等于势能 | $\pm A/\sqrt{2}$ | $\pm A\omega/\sqrt{2}$ | $\frac{1}{4}kA^2$ | $\frac{1}{4}kA^2$ |

### Physical Meaning / 物理意义
**English:**
The position where KE = PE ($x = \pm A/\sqrt{2}$) is a commonly tested concept. At this point, each form of energy is exactly half of the total energy. This occurs at about 70.7% of the amplitude.

**中文:**
动能等于势能的位置（$x = \pm A/\sqrt{2}$）是一个常考概念。此时，每种能量形式恰好是总能量的一半。这发生在约振幅的70.7%处。

### Exam Tips / 考试提示
- ✅ Memorize $x = A/\sqrt{2}$ as the position where KE = PE — this is a frequent exam question.
- ✅ To find velocity at any position, use energy conservation: $\frac{1}{2}mv^2 = \frac{1}{2}kA^2 - \frac{1}{2}kx^2$.

---

# 5. Essential Equations / 核心公式

## Equation 1: Kinetic Energy in SHM / 简谐运动中的动能

$$E_k = \frac{1}{2} m v^2 = \frac{1}{2} m A^2 \omega^2 \cos^2(\omega t) = \frac{1}{2} k (A^2 - x^2)$$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $E_k$ | Kinetic energy | 动能 | J |
| $m$ | Mass of oscillator | 振荡体质量 | kg |
| $A$ | Amplitude | 振幅 | m |
| $\omega$ | Angular frequency | 角频率 | rad s$^{-1}$ |
| $k$ | Spring constant | 弹簧常数 | N m$^{-1}$ |
| $x$ | Displacement from equilibrium | 偏离平衡位置的位移 | m |

**Derivation / 推导:**
$$E_k = \frac{1}{2} m v^2 = \frac{1}{2} m (A\omega \cos(\omega t))^2 = \frac{1}{2} m A^2 \omega^2 \cos^2(\omega t)$$
Using $\omega^2 = k/m$: $E_k = \frac{1}{2} k A^2 \cos^2(\omega t)$
Using $x = A\sin(\omega t)$ and $\cos^2(\omega t) = 1 - \sin^2(\omega t)$: $E_k = \frac{1}{2} k (A^2 - x^2)$

**Conditions / 适用条件:**
- **English:** Valid for any undamped SHM system. For pendulums, use $E_k = \frac{1}{2} m v^2$ directly.
- **中文:** 适用于任何无阻尼简谐运动系统。对于单摆，直接使用 $E_k = \frac{1}{2} m v^2$。

**Limitations / 局限性:**
- **English:** Does not account for damping or energy loss. The expression $\frac{1}{2} k (A^2 - x^2)$ assumes elastic potential energy.
- **中文:** 不考虑阻尼或能量损失。表达式 $\frac{1}{2} k (A^2 - x^2)$ 假设为弹性势能。

---

## Equation 2: Potential Energy in SHM / 简谐运动中的势能

$$E_p = \frac{1}{2} k x^2 = \frac{1}{2} k A^2 \sin^2(\omega t) = \frac{1}{2} m \omega^2 x^2$$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $E_p$ | Potential energy | 势能 | J |
| $k$ | Spring constant | 弹簧常数 | N m$^{-1}$ |
| $x$ | Displacement | 位移 | m |
| $A$ | Amplitude | 振幅 | m |
| $\omega$ | Angular frequency | 角频率 | rad s$^{-1}$ |
| $m$ | Mass | 质量 | kg |

**Derivation / 推导:**
$$E_p = \frac{1}{2} k x^2 = \frac{1}{2} k (A \sin(\omega t))^2 = \frac{1}{2} k A^2 \sin^2(\omega t)$$
Using $\omega^2 = k/m$: $E_p = \frac{1}{2} m \omega^2 x^2$

**Conditions / 适用条件:**
- **English:** Valid for elastic SHM (mass-spring systems). For pendulums, use $E_p = mgh = mgL(1-\cos\theta)$.
- **中文:** 适用于弹性简谐运动（弹簧-质量系统）。对于单摆，使用 $E_p = mgh = mgL(1-\cos\theta)$。

**Limitations / 局限性:**
- **English:** Assumes Hooke's law is obeyed (linear restoring force). Not valid for large amplitudes where anharmonic effects occur.
- **中文:** 假设遵循胡克定律（线性恢复力）。不适用于出现非谐效应的大振幅情况。

---

## Equation 3: Total Energy in SHM / 简谐运动中的总能量

$$E_{total} = \frac{1}{2} k A^2 = \frac{1}{2} m \omega^2 A^2 = \frac{1}{2} m v_{max}^2$$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $E_{total}$ | Total mechanical energy | 总机械能 | J |
| $k$ | Spring constant | 弹簧常数 | N m$^{-1}$ |
| $A$ | Amplitude | 振幅 | m |
| $m$ | Mass | 质量 | kg |
| $\omega$ | Angular frequency | 角频率 | rad s$^{-1}$ |
| $v_{max}$ | Maximum velocity ($= A\omega$) | 最大速度 | m s$^{-1}$ |

**Derivation / 推导:**
$$E_{total} = E_k + E_p = \frac{1}{2} k A^2 (\cos^2(\omega t) + \sin^2(\omega t)) = \frac{1}{2} k A^2$$

**Conditions / 适用条件:**
- **English:** Only constant for undamped SHM. In damped systems, total energy decreases exponentially.
- **中文:** 仅对无阻尼简谐运动恒定。在阻尼系统中，总能量呈指数衰减。

**Limitations / 局限性:**
- **English:** Does not account for thermal energy loss in real systems. Real oscillators lose energy over time.
- **中文:** 不考虑实际系统中的热能损失。实际振荡体随时间推移会损失能量。

> 📷 **IMAGE PROMPT — KE-PE-02: Energy Equations Summary**
> A visual summary showing the three key equations for KE, PE, and total energy in SHM. Each equation is displayed in a colored box with its derivation path shown by arrows. The central box shows $E_{total} = \frac{1}{2}kA^2$ with branches to KE and PE expressions.

---

# 6. Graphs and Relationships / 图表与关系

## 6.1 Energy vs. Time Graph / 能量-时间图

### Axes / 坐标轴
- **X-axis:** Time $t$ (s) / 时间 $t$（秒）
- **Y-axis:** Energy $E$ (J) / 能量 $E$（焦耳）

### Shape / 形状
**English:**
- KE (blue curve): $\frac{1}{2}kA^2 \cos^2(\omega t)$ — oscillates between 0 and $E_{total}$ at frequency $2f$
- PE (red curve): $\frac{1}{2}kA^2 \sin^2(\omega t)$ — oscillates between 0 and $E_{total}$ at frequency $2f$
- Total energy (green line): Constant horizontal line at $E_{total} = \frac{1}{2}kA^2$
- KE and PE curves are phase-shifted by $\pi/2$ (quarter cycle) relative to each other

**中文:**
- 动能（蓝色曲线）：$\frac{1}{2}kA^2 \cos^2(\omega t)$ — 在0和$E_{total}$之间以频率$2f$振荡
- 势能（红色曲线）：$\frac{1}{2}kA^2 \sin^2(\omega t)$ — 在0和$E_{total}$之间以频率$2f$振荡
- 总能量（绿色线）：在$E_{total} = \frac{1}{2}kA^2$处的恒定水平线
- 动能和势能曲线彼此相位差$\pi/2$（四分之一周期）

### Gradient Meaning / 斜率含义
**English:** The gradient of the KE curve represents the rate of change of kinetic energy ($dE_k/dt$), which equals the power transferred between KE and PE. The gradient is zero at maxima and minima of KE.

**中文:** 动能曲线的斜率表示动能的变化率（$dE_k/dt$），等于动能和势能之间传递的功率。在动能的最大值和最小值处斜率为零。

### Area Meaning / 面积含义
**English:** The area under the KE or PE curve over one complete cycle represents the average energy of that form over the cycle. For both KE and PE, the average is $E_{total}/2$.

**中文:** 动能或势能曲线在一个完整周期下的面积表示该能量形式在一个周期内的平均值。对于动能和势能，平均值均为$E_{total}/2$。

### Exam Interpretation / 考试解读
- **English:** Common questions ask students to identify which curve represents KE vs. PE, determine the period of energy oscillation, or calculate total energy from the graph.
- **中文:** 常见问题要求学生识别哪条曲线代表动能或势能，确定能量振荡的周期，或从图中计算总能量。

> 📷 **IMAGE PROMPT — KE-PE-03: Energy vs Time Graph for SHM**
> A clear graph with time on the x-axis and energy on the y-axis. Three curves: (1) KE as a blue cosine-squared wave oscillating between 0 and $E_{total}$, (2) PE as a red sine-squared wave oscillating between 0 and $E_{total}$, (3) Total energy as a green horizontal line at $E_{total}$. The period of energy oscillation is half the period of displacement. Labels indicate key points where KE=0, PE=0, and KE=PE.

---

## 6.2 Energy vs. Displacement Graph / 能量-位移图

### Axes / 坐标轴
- **X-axis:** Displacement $x$ (m) / 位移 $x$（米）
- **Y-axis:** Energy $E$ (J) / 能量 $E$（焦耳）

### Shape / 形状
**English:**
- KE (blue parabola opening downward): $E_k = \frac{1}{2}k(A^2 - x^2)$ — maximum at $x=0$, zero at $x=\pm A$
- PE (red parabola opening upward): $E_p = \frac{1}{2}kx^2$ — zero at $x=0$, maximum at $x=\pm A$
- Total energy (green line): Constant horizontal line at $E_{total} = \frac{1}{2}kA^2$
- The two parabolas intersect at $x = \pm A/\sqrt{2}$ where KE = PE

**中文:**
- 动能（蓝色开口向下抛物线）：$E_k = \frac{1}{2}k(A^2 - x^2)$ — 在$x=0$处最大，在$x=\pm A$处为零
- 势能（红色开口向上抛物线）：$E_p = \frac{1}{2}kx^2$ — 在$x=0$处为零，在$x=\pm A$处最大
- 总能量（绿色线）：在$E_{total} = \frac{1}{2}kA^2$处的恒定水平线
- 两条抛物线在$x = \pm A/\sqrt{2}$处相交，此时KE = PE

### Gradient Meaning / 斜率含义
**English:** The gradient of the PE curve ($dE_p/dx = kx$) equals the restoring force (with sign). The gradient of the KE curve ($dE_k/dx = -kx$) equals the negative of the restoring force.

**中文:** 势能曲线的斜率（$dE_p/dx = kx$）等于恢复力（带符号）。动能曲线的斜率（$dE_k/dx = -kx$）等于恢复力的负值。

### Area Meaning / 面积含义
**English:** The area between the KE curve and the x-axis from $-A$ to $+A$ represents the total energy integrated over displacement, which relates to the work done by the restoring force.

**中文:** 动能曲线与x轴之间从$-A$到$+A$的面积表示对位移积分后的总能量，与恢复力所做的功有关。

### Exam Interpretation / 考试解读
- **English:** Students must be able to read energy values at any displacement, identify the amplitude from the graph, and find where KE = PE.
- **中文:** 学生必须能够读取任意位移处的能量值，从图中识别振幅，并找到动能等于势能的位置。

> 📷 **IMAGE PROMPT — KE-PE-04: Energy vs Displacement Graph for SHM**
> A graph with displacement x on the x-axis (from -A to +A) and energy on the y-axis. Three curves: (1) KE as a blue downward-opening parabola, maximum at x=0, zero at x=±A, (2) PE as a red upward-opening parabola, zero at x=0, maximum at x=±A, (3) Total energy as a green horizontal line. The intersection points at x=±A/√2 are clearly marked with dashed lines and labeled "KE = PE".

---

# 7. Required Diagrams / 必备图表

## 7.1 Energy Distribution at Key Positions / 关键位置的能量分布

### Description / 描述
**English:** A diagram showing a mass-spring system at four key positions: (a) at maximum extension, (b) moving through equilibrium, (c) at maximum compression, and (d) at the position where KE = PE. Each position shows bar charts of KE and PE.

**中文:** 一个显示弹簧-质量系统在四个关键位置的图：(a) 最大伸长处，(b) 经过平衡位置时，(c) 最大压缩处，(d) 动能等于势能的位置。每个位置显示动能和势能的条形图。

### Image Prompt / 图片生成提示
> 📷 **IMAGE PROMPT — KE-PE-05: Energy Distribution at Key Positions**
> A detailed diagram showing a horizontal mass-spring system at four positions. Position 1: mass at rightmost (x=+A), spring stretched, bar chart shows PE=100%, KE=0%. Position 2: mass at center (x=0), spring at natural length, bar chart shows KE=100%, PE=0%. Position 3: mass at leftmost (x=-A), spring compressed, bar chart shows PE=100%, KE=0%. Position 4: mass at x=+A/√2, bar chart shows KE=50%, PE=50%. Arrows indicate direction of motion. Labels clearly show energy values.

### Labels Required / 需要标注
- **English:** Equilibrium position, amplitude A, displacement x, KE bar, PE bar, total energy level, position where KE = PE
- **中文:** 平衡位置、振幅A、位移x、动能条、势能条、总能量水平、动能等于势能的位置

### Exam Importance / 考试重要性
- **English:** High — students are often asked to sketch or interpret such diagrams in exam questions about energy distribution in SHM.
- **中文:** 高——学生经常被要求在关于简谐运动能量分布的考试题目中绘制或解释此类图。

---

## 7.2 Energy Flow Diagram / 能量流动图

### Description / 描述
**English:** A circular flow diagram showing the continuous transformation between KE and PE during one complete oscillation cycle. Arrows indicate the direction of energy flow at each quarter-cycle.

**中文:** 一个圆形流动图，显示在一个完整振荡周期内动能和势能之间的连续转换。箭头指示每个四分之一周期内的能量流动方向。

### Image Prompt / 图片生成提示
> 📷 **IMAGE PROMPT — KE-PE-06: Energy Flow in SHM Cycle**
> A circular diagram divided into four quadrants. Top: "PE Maximum (x=±A)" with arrow pointing right to "KE Increasing". Right: "KE Maximum (x=0)" with arrow pointing down to "PE Increasing". Bottom: "PE Maximum (x=±A)" with arrow pointing left to "KE Increasing". Left: "KE Maximum (x=0)" with arrow pointing up to "PE Increasing". Center shows "Total Energy = ½kA² (Constant)". Color coding: red for PE, blue for KE.

### Labels Required / 需要标注
- **English:** PE maximum, KE maximum, energy transformation direction, total energy constant, quarter-cycle markers
- **中文:** 势能最大、动能最大、能量转换方向、总能量恒定、四分之一周期标记

### Exam Importance / 考试重要性
- **English:** Medium — helps visualize the conservation principle but is less frequently tested directly than energy graphs.
- **中文:** 中——有助于可视化守恒原理，但直接测试的频率低于能量图。

---

# 8. Worked Examples / 典型例题

## Example 1: Finding Energy at a Given Displacement / 求给定位移处的能量

### Question / 题目
**English:**
A 0.50 kg mass oscillates on a spring with spring constant $k = 200 \text{ N m}^{-1}$. The amplitude of oscillation is 0.080 m. Calculate:
(a) The total energy of the oscillator.
(b) The kinetic energy when the displacement is 0.050 m.
(c) The speed of the mass at this displacement.

**中文:**
一个0.50 kg的质量在弹簧常数为 $k = 200 \text{ N m}^{-1}$ 的弹簧上振荡。振荡振幅为0.080 m。计算：
(a) 振荡体的总能量。
(b) 位移为0.050 m时的动能。
(c) 质量在该位移处的速度。

### Solution / 解答

**Step 1: Total Energy / 步骤1：总能量**
$$E_{total} = \frac{1}{2} k A^2 = \frac{1}{2} \times 200 \times (0.080)^2$$
$$E_{total} = \frac{1}{2} \times 200 \times 0.0064 = 0.64 \text{ J}$$

**Step 2: Potential Energy at x = 0.050 m / 步骤2：x = 0.050 m处的势能**
$$E_p = \frac{1}{2} k x^2 = \frac{1}{2} \times 200 \times (0.050)^2$$
$$E_p = \frac{1}{2} \times 200 \times 0.0025 = 0.25 \text{ J}$$

**Step 3: Kinetic Energy / 步骤3：动能**
$$E_k = E_{total} - E_p = 0.64 - 0.25 = 0.39 \text{ J}$$

**Step 4: Speed / 步骤4：速度**
$$E_k = \frac{1}{2} m v^2 \implies v = \sqrt{\frac{2E_k}{m}}$$
$$v = \sqrt{\frac{2 \times 0.39}{0.50}} = \sqrt{1.56} = 1.25 \text{ m s}^{-1}$$

### Final Answer / 最终答案
**Answer:** (a) $E_{total} = 0.64 \text{ J}$, (b) $E_k = 0.39 \text{ J}$, (c) $v = 1.25 \text{ m s}^{-1}$ | **答案：** (a) $E_{total} = 0.64 \text{ J}$, (b) $E_k = 0.39 \text{ J}$, (c) $v = 1.25 \text{ m s}^{-1}$

### Quick Tip / 提示
- **English:** Always use energy conservation ($E_k = E_{total} - E_p$) rather than trying to find velocity from SHM equations directly — it's faster and less error-prone.
- **中文:** 始终使用能量守恒（$E_k = E_{total} - E_p$），而不是直接尝试从简谐运动方程求速度——这样更快且不易出错。

---

## Example 2: Position Where KE = PE / 动能等于势能的位置

### Question / 题目
**English:**
A particle performs SHM with amplitude 0.12 m. At what displacement from equilibrium are the kinetic energy and potential energy equal?

**中文:**
一个质点以振幅0.12 m进行简谐运动。在偏离平衡位置多大的位移处，动能和势能相等？

### Solution / 解答

**Step 1: Set KE = PE / 步骤1：令KE = PE**
$$E_k = E_p$$
$$\frac{1}{2} k (A^2 - x^2) = \frac{1}{2} k x^2$$

**Step 2: Solve for x / 步骤2：解出x**
$$A^2 - x^2 = x^2$$
$$A^2 = 2x^2$$
$$x^2 = \frac{A^2}{2}$$
$$x = \pm \frac{A}{\sqrt{2}}$$

**Step 3: Substitute values / 步骤3：代入数值**
$$x = \pm \frac{0.12}{\sqrt{2}} = \pm \frac{0.12}{1.414} = \pm 0.0849 \text{ m}$$

### Final Answer / 最终答案
**Answer:** $x = \pm 0.085 \text{ m}$ (to 2 significant figures) | **答案：** $x = \pm 0.085 \text{ m}$（保留两位有效数字）

### Quick Tip / 提示
- **English:** The position where KE = PE is always $x = \pm A/\sqrt{2}$, regardless of mass or spring constant. Memorize this!
- **中文:** 动能等于势能的位置始终是 $x = \pm A/\sqrt{2}$，与质量或弹簧常数无关。记住这个！

---

# 9. Past Paper Question Types / 历年真题题型

| Question Type / 题型 | Frequency / 频率 | Difficulty / 难度 | Past Paper References / 真题索引 |
|----------------------|------------------|------------------|-------------------------------|
| Calculate total energy from amplitude and spring constant | High | Easy | 📝 *待填入* |
| Find KE or PE at given displacement | High | Medium | 📝 *待填入* |
| Determine position where KE = PE | Medium | Easy | 📝 *待填入* |
| Sketch and interpret energy-time graphs | High | Medium | 📝 *待填入* |
| Sketch and interpret energy-displacement graphs | High | Medium | 📝 *待填入* |
| Derive KE/PE expressions from SHM equations | Medium | Hard | 📝 *待填入* |
| Energy calculations with pendulum systems | Low | Hard | 📝 *待填入* |
| Compare energy in different oscillators | Low | Medium | 📝 *待填入* |

**Common Command Words / 常见指令词:**
- **English:** Calculate, determine, sketch, derive, state, explain, compare
- **中文:** 计算、确定、绘制、推导、陈述、解释、比较

---

# 10. Practical Skills Connections / 实验技能链接

**English:**
This sub-topic connects to practical work in several ways:

1. **Energy Conservation Verification:** Use a motion sensor and force sensor with a mass-spring system to measure displacement and velocity simultaneously. Calculate KE and PE at each point and verify that $E_{total}$ is constant.

2. **Graph Plotting:** Plot experimental $E_k$ vs. $t$ and $E_p$ vs. $t$ graphs. Compare with theoretical $\cos^2$ and $\sin^2$ curves. Calculate the period of energy oscillation and verify it is half the period of motion.

3. **Uncertainty Analysis:** When measuring amplitude $A$ and spring constant $k$, propagate uncertainties to find the uncertainty in $E_{total} = \frac{1}{2}kA^2$:
   $$\frac{\Delta E_{total}}{E_{total}} = \frac{\Delta k}{k} + 2\frac{\Delta A}{A}$$

4. **Experimental Design:** Design an experiment to find the spring constant $k$ by measuring the total energy at different amplitudes. Use the relationship $E_{total} \propto A^2$ to determine $k$ from the gradient of an $E_{total}$ vs. $A^2$ graph.

**中文:**
本子知识点通过以下方式与实验工作联系：

1. **能量守恒验证：** 使用运动传感器和力传感器与弹簧-质量系统同时测量位移和速度。计算每个点的动能和势能，验证 $E_{total}$ 是否恒定。

2. **图表绘制：** 绘制实验的 $E_k$ 与 $t$ 以及 $E_p$ 与 $t$ 的图。与理论的 $\cos^2$ 和 $\sin^2$ 曲线进行比较。计算能量振荡的周期并验证它是运动周期的一半。

3. **不确定度分析：** 测量振幅 $A$ 和弹簧常数 $k$ 时，传播不确定度以求出 $E_{total} = \frac{1}{2}kA^2$ 的不确定度：
   $$\frac{\Delta E_{total}}{E_{total}} = \frac{\Delta k}{k} + 2\frac{\Delta A}{A}$$

4. **实验设计：** 设计一个实验，通过测量不同振幅下的总能量来求弹簧常数 $k$。利用 $E_{total} \propto A^2$ 的关系，从 $E_{total}$ 与 $A^2$ 图的斜率确定 $k$。

---

# 11. Concept Map / 概念图谱

```mermaid
graph TD
    %% Core concept
    SHM["Simple Harmonic Motion"] --> KE_PE["KE and PE in SHM"]
    
    %% Prerequisites
    KE["Kinetic Energy"] --> KE_PE
    PE["Potential Energy"] --> KE_PE
    SHM_Eq["SHM Equations<br/>(x = A sin ωt, v = Aω cos ωt)"] --> KE_PE
    
    %% Key equations
    KE_PE --> KE_eq["E_k = ½mv² = ½k(A²-x²)"]
    KE_PE --> PE_eq["E_p = ½kx²"]
    KE_PE --> Total_eq["E_total = ½kA² = ½mv_max²"]
    
    %% Key concepts
    KE_PE --> Conservation["Energy Conservation<br/>E_total = constant"]
    KE_PE --> MaxMin["Maximum/Minimum Values<br/>KE_max at x=0, PE_max at x=±A"]
    KE_PE --> Equal["KE = PE at x = ±A/√2"]
    
    %% Graphs
    KE_PE --> ET_Graph["Energy-Time Graphs<br/>for SHM"]
    KE_PE --> ED_Graph["Energy-Displacement<br/>Graphs for SHM"]
    
    %% Related topics
    Conservation --> Damping["Damped and Forced<br/>Oscillations - Resonance"]
    
    %% Styling
    classDef core fill:#e1f5fe,stroke:#01579b,stroke-width:2px
    classDef equation fill:#f3e5f5,stroke:#7b1fa2,stroke-width:1px
    classDef concept fill:#fff3e0,stroke:#e65100,stroke-width:1px
    classDef graph fill:#e8f5e9,stroke:#1b5e20,stroke-width:1px
    
    class KE_PE core
    class KE_eq,PE_eq,Total_eq equation
    class Conservation,MaxMin,Equal concept
    class ET_Graph,ED_Graph graph
```

---

# 12. Quick Revision Sheet / 速查表

| Category / 类别 | Key Points / 要点 |
|----------------|------------------|
| **Definition / 定义** | KE = energy due to motion ($\frac{1}{2}mv^2$); PE = energy due to displacement ($\frac{1}{2}kx^2$); Total energy = KE + PE = constant |
| **Key Formula / 核心公式** | $E_k = \frac{1}{2}k(A^2 - x^2)$, $E_p = \frac{1}{2}kx^2$, $E_{total} = \frac{1}{2}kA^2 = \frac{1}{2}mv_{max}^2$ |
| **Key Graph / 核心图表** | Energy-time: KE and PE oscillate at $2f$ between 0 and $E_{total}$; Energy-displacement: KE is downward parabola, PE is upward parabola, intersect at $x = \pm A/\sqrt{2}$ |
| **Exam Tip / 考试提示** | ✅ Memorize $x = A/\sqrt{2}$ for KE = PE ✅ Use $E_k = E_{total} - E_p$ for speed calculations ✅ Energy graphs have double the frequency of displacement graphs ✅ Total energy depends on $A^2$ — doubling amplitude quadruples energy |
| **Common Mistake / 常见错误** | ❌ Thinking KE and PE vary at same frequency as displacement ❌ Forgetting total energy is constant in undamped SHM ❌ Using $\frac{1}{2}kx^2$ for pendulum PE (use $mgh$ instead) |
| **Practical Link / 实验联系** | Use motion sensor + force sensor to verify $E_{total}$ constant; plot $E_{total}$ vs $A^2$ to find $k$ from gradient |
| **Prerequisites / 前置知识** | [[Simple Harmonic Motion]], [[Kinetic Energy and Potential Energy]] |
| **Next Topics / 后续主题** | [[Energy-Time Graphs for SHM]], [[Energy-Displacement Graphs for SHM]], [[Damped and Forced Oscillations - Resonance]] |