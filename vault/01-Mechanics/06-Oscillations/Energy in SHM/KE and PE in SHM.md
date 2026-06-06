# 1. Overview / 概述

**English:**
This sub-topic explores how kinetic energy (KE) and potential energy (PE) vary during simple harmonic motion (SHM). In any oscillating system — such as a mass on a spring or a simple pendulum — energy continuously transforms between KE and PE while the total mechanical energy remains constant (in the absence of damping). Understanding this energy exchange is fundamental to analysing oscillatory systems, interpreting [[Energy-Time Graphs for SHM]] and [[Energy-Displacement Graphs for SHM]], and later extending to [[Damped and Forced Oscillations / Resonance]]. This builds directly on the concepts of [[Simple Harmonic Motion]] and the definitions of [[Kinetic Energy and Potential Energy]].

**中文:**
本子知识点探讨在简谐运动（SHM）中动能（KE）和势能（PE）如何变化。在任何振荡系统中——例如弹簧上的质量块或单摆——能量在动能和势能之间持续转换，而总机械能保持不变（无阻尼情况下）。理解这种能量交换是分析振荡系统、解读[[Energy-Time Graphs for SHM]]和[[Energy-Displacement Graphs for SHM]]的基础，也为后续学习[[Damped and Forced Oscillations / Resonance]]奠定基础。这直接建立在[[Simple Harmonic Motion]]以及[[Kinetic Energy and Potential Energy]]的概念之上。

---

# 2. Core Definition / 核心定义

| Term (EN/CN) | Definition (EN) | Definition (CN) |
| ------------ | --------------- | --------------- |
| **Kinetic Energy in SHM** / 简谐运动中的动能 | The energy of the oscillating mass due to its motion, given by $E_k = \frac{1}{2} m v^2$, where $v$ varies sinusoidally with time. | 振荡质量因运动而具有的能量，由 $E_k = \frac{1}{2} m v^2$ 给出，其中 $v$ 随时间正弦变化。 |
| **Potential Energy in SHM** / 简谐运动中的势能 | The energy stored in the system due to displacement from equilibrium, e.g., elastic potential energy in a spring: $E_p = \frac{1}{2} k x^2$. | 系统因偏离平衡位置而储存的能量，例如弹簧中的弹性势能：$E_p = \frac{1}{2} k x^2$。 |
| **Total Mechanical Energy** / 总机械能 | The sum of KE and PE at any instant, which remains constant for undamped SHM: $E_{total} = E_k + E_p = \frac{1}{2} k A^2$. | 任意时刻动能与势能之和，在无阻尼简谐运动中保持不变：$E_{total} = E_k + E_p = \frac{1}{2} k A^2$。 |
| **Equilibrium Position** / 平衡位置 | The point where displacement $x = 0$; KE is maximum and PE is minimum (zero for ideal spring). | 位移 $x = 0$ 的位置；动能最大，势能最小（理想弹簧中为零）。 |
| **Amplitude** / 振幅 | The maximum displacement $A$ from equilibrium; at this point KE = 0 and PE is maximum. | 偏离平衡位置的最大位移 $A$；此时动能为零，势能最大。 |
| **Energy Conservation** / 能量守恒 | The principle that total energy in an isolated SHM system is constant, with energy continuously transferring between KE and PE. | 孤立简谐运动系统中总能量保持恒定的原理，能量在动能和势能之间持续转移。 |

---

# 3. Key Concepts / 关键概念

**English:**
In SHM, the displacement $x$ and velocity $v$ are related by the SHM equations:
$$ x = A \sin(\omega t + \phi) $$
$$ v = \omega A \cos(\omega t + \phi) $$

The kinetic energy is:
$$ E_k = \frac{1}{2} m v^2 = \frac{1}{2} m \omega^2 A^2 \cos^2(\omega t + \phi) $$

For a mass-spring system, the potential energy (elastic) is:
$$ E_p = \frac{1}{2} k x^2 = \frac{1}{2} k A^2 \sin^2(\omega t + \phi) $$

Since $\omega^2 = k/m$ for a spring, we have $\frac{1}{2} m \omega^2 A^2 = \frac{1}{2} k A^2$, so the total energy is:
$$ E_{total} = \frac{1}{2} k A^2 $$

**Key insight:** At any instant, $E_k + E_p = \frac{1}{2} k A^2$, confirming energy conservation.

**Common pitfalls:**
- Students often forget that PE is zero at equilibrium only for ideal springs; for a pendulum, gravitational PE is minimum (not zero) at the lowest point.
- Confusing the instantaneous values with maximum values — KE and PE are not constant; only the total is constant.
- Forgetting that the formulas assume no damping — real systems lose energy over time (see [[Damped and Forced Oscillations / Resonance]]).

**Physical interpretation:** The energy exchange is analogous to a pendulum: at the extremes (maximum displacement), all energy is potential; at the centre (equilibrium), all energy is kinetic. The system continuously "borrows" energy between these two forms.

**中文:**
在简谐运动中，位移 $x$ 和速度 $v$ 由简谐运动方程关联：
$$ x = A \sin(\omega t + \phi) $$
$$ v = \omega A \cos(\omega t + \phi) $$

动能为：
$$ E_k = \frac{1}{2} m v^2 = \frac{1}{2} m \omega^2 A^2 \cos^2(\omega t + \phi) $$

对于弹簧-质量系统，势能（弹性）为：
$$ E_p = \frac{1}{2} k x^2 = \frac{1}{2} k A^2 \sin^2(\omega t + \phi) $$

由于弹簧的 $\omega^2 = k/m$，我们有 $\frac{1}{2} m \omega^2 A^2 = \frac{1}{2} k A^2$，因此总能量为：
$$ E_{total} = \frac{1}{2} k A^2 $$

**关键洞察：** 任意时刻，$E_k + E_p = \frac{1}{2} k A^2$，证实能量守恒。

**常见错误：**
- 学生常忘记只有在理想弹簧中，平衡位置势能为零；对于单摆，最低点重力势能最小（不为零）。
- 混淆瞬时值与最大值——动能和势能不恒定；只有总和恒定。
- 忘记公式假设无阻尼——实际系统能量随时间衰减（见[[Damped and Forced Oscillations / Resonance]]）。

**物理解释：** 能量交换类似于单摆：在极端位置（最大位移），所有能量为势能；在中心（平衡位置），所有能量为动能。系统在这两种形式之间持续"借用"能量。

---

# 4. Formulas / 公式

## Key Formula 1: Total Energy in SHM

$$ E_{total} = \frac{1}{2} k A^2 $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
| ------------- | ------------ | ------------ | ----------- |
| $E_{total}$ | Total mechanical energy | 总机械能 | J (Joules) |
| $k$ | Spring constant (or force constant) | 弹簧常数（或力常数） | N/m |
| $A$ | Amplitude of oscillation | 振荡振幅 | m |

## Key Formula 2: Kinetic Energy at Displacement x

$$ E_k = \frac{1}{2} k (A^2 - x^2) $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
| ------------- | ------------ | ------------ | ----------- |
| $E_k$ | Kinetic energy | 动能 | J |
| $x$ | Displacement from equilibrium | 偏离平衡位置的位移 | m |

## Key Formula 3: Potential Energy at Displacement x

$$ E_p = \frac{1}{2} k x^2 $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
| ------------- | ------------ | ------------ | ----------- |
| $E_p$ | Potential energy | 势能 | J |

**Derivation / 推导:**
From SHM, $v^2 = \omega^2 (A^2 - x^2)$. Since $\omega^2 = k/m$:
$$ E_k = \frac{1}{2} m v^2 = \frac{1}{2} m \omega^2 (A^2 - x^2) = \frac{1}{2} k (A^2 - x^2) $$
$$ E_p = \frac{1}{2} k x^2 $$
Adding: $E_k + E_p = \frac{1}{2} k A^2 = E_{total}$

**Conditions / 适用条件:**
- Applies to **undamped** SHM only (no energy loss).
- For a mass-spring system, $k$ is the spring constant.
- For a simple pendulum, use $E_p = mgh$ and $E_k = \frac{1}{2}mv^2$, with $h \approx \frac{x^2}{2L}$ for small angles.
- Valid for any SHM system where restoring force is proportional to displacement (Hooke's law).

> 📷 **IMAGE PROMPT — KE-PE-ENERGY: Energy Exchange in SHM**
>
> **English Prompt:**
> A clean, textbook-style vector diagram showing a mass-spring system at three positions: (1) at maximum displacement (left), with label "PE max, KE = 0"; (2) at equilibrium (centre), with label "KE max, PE = 0"; (3) at maximum displacement (right), with label "PE max, KE = 0". Below, a bar chart showing total energy constant (green bar) split into KE (blue) and PE (red) at each position. Use a white background, clear labels in Arial font, and arrows indicating direction of motion. Style: educational vector illustration.
>
> **中文描述:**
> 一个干净、教科书风格的矢量图，展示弹簧-质量系统在三个位置：(1) 最大位移处（左侧），标注"势能最大，动能为零"；(2) 平衡位置（中心），标注"动能最大，势能为零"；(3) 最大位移处（右侧），标注"势能最大，动能为零"。下方为条形图，显示每个位置总能量恒定（绿色），分为动能（蓝色）和势能（红色）。白色背景，Arial字体的清晰标签，箭头指示运动方向。风格：教育矢量插图。
>
> **Labels Required / 需要标注:**
> * "PE max, KE = 0" at extreme positions
> * "KE max, PE = 0" at equilibrium
> * "Total Energy = ½kA²" constant bar
>
> **Style / 风格:** Textbook vector illustration
>
> **Exam Relevance / 考试关联:**
> This diagram is frequently used in exam questions to test understanding of energy transformation at key positions in SHM.

---

# 5. Image Prompt / 图片提示

> 📷 **IMAGE PROMPT — KE-PE-GRAPH: Energy vs Displacement in SHM**
>
> **English Prompt:**
> A graph with displacement x on the horizontal axis (from -A to +A) and energy E on the vertical axis. Three curves: (1) PE = ½kx² — a red upward-opening parabola; (2) KE = ½k(A²-x²) — a blue downward-opening parabola; (3) Total Energy = ½kA² — a green horizontal line. Label the intersection points where KE = PE at x = ±A/√2. Use a clean white background, grid lines in light grey, and a legend box. Style: precise mathematical graph, suitable for A-Level Physics textbook.
>
> **中文描述:**
> 一张以位移 x 为横轴（从 -A 到 +A）、能量 E 为纵轴的图表。三条曲线：(1) PE = ½kx² —— 红色开口向上的抛物线；(2) KE = ½k(A²-x²) —— 蓝色开口向下的抛物线；(3) 总能量 = ½kA² —— 绿色水平线。标注交点处 KE = PE，即 x = ±A/√2。使用干净的白色背景、浅灰色网格线和图例框。风格：精确的数学图表，适合 A-Level 物理教科书。
>
> **Labels Required / 需要标注:**
> * "PE = ½kx²" on red curve
> * "KE = ½k(A²-x²)" on blue curve
> * "Total Energy = ½kA²" on green line
> * "x = ±A/√2" at intersection points
>
> **Style / 风格:** Precise mathematical graph
>
> **Exam Relevance / 考试关联:**
> This graph is essential for interpreting [[Energy-Displacement Graphs for SHM]] and is a common exam question type where students must identify curves and calculate energy values.

---

# 6. Worked Example / 典型例题

### Example 1: Energy Calculation at a Given Displacement

**English:**
A 0.50 kg mass oscillates on a spring with spring constant $k = 200 \text{ N/m}$ and amplitude $A = 0.10 \text{ m}$. Calculate:
(a) The total mechanical energy of the system.
(b) The kinetic energy when the displacement is $x = 0.060 \text{ m}$.
(c) The speed of the mass at this displacement.

**中文:**
一个 0.50 kg 的质量块在弹簧上振荡，弹簧常数 $k = 200 \text{ N/m}$，振幅 $A = 0.10 \text{ m}$。计算：
(a) 系统的总机械能。
(b) 位移为 $x = 0.060 \text{ m}$ 时的动能。
(c) 该位移下质量块的速度。

### Solution / 解答

**(a) Total energy:**
$$ E_{total} = \frac{1}{2} k A^2 = \frac{1}{2} \times 200 \times (0.10)^2 = 1.0 \text{ J} $$

**(b) Kinetic energy at $x = 0.060 \text{ m}$:**
$$ E_k = \frac{1}{2} k (A^2 - x^2) = \frac{1}{2} \times 200 \times (0.10^2 - 0.060^2) $$
$$ E_k = 100 \times (0.01 - 0.0036) = 100 \times 0.0064 = 0.64 \text{ J} $$

**(c) Speed at this displacement:**
$$ E_k = \frac{1}{2} m v^2 \implies v = \sqrt{\frac{2E_k}{m}} = \sqrt{\frac{2 \times 0.64}{0.50}} = \sqrt{2.56} = 1.6 \text{ m/s} $$

### Final Answer / 最终答案
**Answer:** (a) 1.0 J, (b) 0.64 J, (c) 1.6 m/s
**答案：** (a) 1.0 焦耳，(b) 0.64 焦耳，(c) 1.6 米/秒

### Quick Tip / 提示
Always check that $E_k + E_p = E_{total}$ as a verification step. Here $E_p = \frac{1}{2} k x^2 = 0.36 \text{ J}$, and $0.64 + 0.36 = 1.0 \text{ J}$ ✓

---

### Example 2: Finding Displacement Where KE = PE

**English:**
For the same system in Example 1, find the displacement at which the kinetic energy equals the potential energy.

**中文:**
对于例1中的同一系统，求动能等于势能时的位移。

### Solution / 解答

Set $E_k = E_p$:
$$ \frac{1}{2} k (A^2 - x^2) = \frac{1}{2} k x^2 $$
$$ A^2 - x^2 = x^2 $$
$$ A^2 = 2x^2 $$
$$ x = \pm \frac{A}{\sqrt{2}} = \pm \frac{0.10}{\sqrt{2}} = \pm 0.0707 \text{ m} $$

### Final Answer / 最终答案
**Answer:** $x = \pm 0.071 \text{ m}$ (to 2 s.f.)
**答案：** $x = \pm 0.071$ 米（保留两位有效数字）

### Quick Tip / 提示
The condition $x = \pm A/\sqrt{2}$ is a standard result — memorise it! At these points, KE = PE = half of total energy.

---

# 7. Flashcards / 闪卡

**Flashcard 1:**
Q (EN): What is the total mechanical energy of an undamped SHM system in terms of spring constant k and amplitude A?
Q (CN): 无阻尼简谐运动系统的总机械能用弹簧常数 k 和振幅 A 如何表示？
A (EN): $E_{total} = \frac{1}{2} k A^2$
A (CN): $E_{total} = \frac{1}{2} k A^2$

**Flashcard 2:**
Q (EN): At which displacement(s) does kinetic energy equal potential energy in SHM?
Q (CN): 在简谐运动中，动能等于势能时的位移是多少？
A (EN): $x = \pm \frac{A}{\sqrt{2}}$
A (CN): $x = \pm \frac{A}{\sqrt{2}}$

**Flashcard 3:**
Q (EN): What is the kinetic energy of a mass in SHM at displacement x, in terms of k, A, and x?
Q (CN): 简谐运动中质量块在位移 x 处的动能，用 k、A 和 x 如何表示？
A (EN): $E_k = \frac{1}{2} k (A^2 - x^2)$
A (CN): $E_k = \frac{1}{2} k (A^2 - x^2)$

**Flashcard 4:**
Q (EN): Where is KE maximum and PE minimum in SHM?
Q (CN): 简谐运动中动能最大、势能最小的位置在哪里？
A (EN): At the equilibrium position (x = 0)
A (CN): 在平衡位置（x = 0）

**Flashcard 5:**
Q (EN): What happens to the total energy of an SHM system if damping is introduced?
Q (CN): 如果引入阻尼，简谐运动系统的总能量会发生什么变化？
A (EN): It decreases over time as energy is dissipated (e.g., as heat or sound).
A (CN): 随时间减少，因为能量被耗散（例如以热或声音的形式）。

---

# 8. Metadata / 元数据

```yaml
title:
  en: "Kinetic Energy and Potential Energy in SHM"
  cn: "简谐运动中的动能与势能"
parent_topic: "Energy in SHM"
parent_hub: "[[Energy in SHM]]"
subject: Physics
syllabus:
  - CAIE 9702: 17.2 (a-c)
  - Edexcel IAL: WPH14 U4: 7.6-7.8
level: A2
node_type: leaf_concept
difficulty: intermediate
related_leaf_nodes:
  - "[[Energy-Time Graphs for SHM]]"
  - "[[Energy-Displacement Graphs for SHM]]"
  - "[[Simple Harmonic Motion]]"
  - "[[Kinetic Energy and Potential Energy]]"
  - "[[Damped and Forced Oscillations / Resonance]]"
language: bilingual_en_cn