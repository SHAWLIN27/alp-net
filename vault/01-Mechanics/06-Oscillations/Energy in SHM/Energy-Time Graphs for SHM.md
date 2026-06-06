# Energy-Time Graphs for SHM

---

# 1. Overview / 概述

**English:**
Energy-Time Graphs for SHM show how the kinetic energy (KE), potential energy (PE), and total mechanical energy of an oscillating system vary with time. Unlike [[Energy-Displacement Graphs for SHM]] which show energy variation with position, energy-time graphs reveal the *temporal* behaviour — how energy flows between KE and PE as the oscillator moves through its cycle. This is crucial for understanding the conservation of mechanical energy in ideal SHM and for analysing real-world oscillatory systems.

These graphs are sinusoidal in shape, with KE and PE oscillating at *twice* the frequency of the displacement. The total energy remains constant (a horizontal line) for undamped SHM. Mastering these graphs allows students to predict energy values at any instant, relate them to [[Simple Harmonic Motion]] parameters, and understand the effects of [[Damped and Forced Oscillations / Resonance]].

**中文:**
简谐运动的能量-时间图展示了振荡系统中动能 (KE)、势能 (PE) 和总机械能随时间的变化。与[[Energy-Displacement Graphs for SHM]]（显示能量随位置变化）不同，能量-时间图揭示了*时间*行为——能量如何在振荡器完成一个周期时在动能和势能之间流动。这对于理解理想简谐运动中的机械能守恒以及分析现实世界的振荡系统至关重要。

这些图形呈正弦形状，动能和势能以位移*两倍*的频率振荡。对于无阻尼简谐运动，总能量保持不变（一条水平线）。掌握这些图形使学生能够预测任意时刻的能量值，将其与[[Simple Harmonic Motion]]参数联系起来，并理解[[Damped and Forced Oscillations / Resonance]]的影响。

---

# 2. Core Definition / 核心定义

| Term (EN/CN) | Definition (EN) | Definition (CN) |
| ------------ | --------------- | --------------- |
| **Energy-Time Graph** / 能量-时间图 | A graph showing how kinetic energy, potential energy, and total mechanical energy of an SHM system vary with time over one or more complete cycles. | 显示简谐运动系统中动能、势能和总机械能在一个或多个完整周期内随时间变化的图形。 |
| **Total Mechanical Energy** / 总机械能 | The constant sum of kinetic and potential energy in ideal undamped SHM, equal to the maximum KE or maximum PE. | 在理想无阻尼简谐运动中，动能和势能的恒定总和，等于最大动能或最大势能。 |
| **Energy Oscillation Frequency** / 能量振荡频率 | The frequency at which KE and PE oscillate, which is twice the frequency of displacement oscillation ($f_{energy} = 2f_{displacement}$). | 动能和势能振荡的频率，是位移振荡频率的两倍 ($f_{能量} = 2f_{位移}$)。 |
| **Phase Relationship** / 相位关系 | The relationship where KE and PE are exactly $\pi/2$ radians (90°) out of phase with each other — when one is maximum, the other is zero. | 动能和势能彼此恰好相差 $\pi/2$ 弧度（90°）的关系——当一个最大时，另一个为零。 |
| **Amplitude of Energy** / 能量振幅 | The maximum value of KE or PE, equal to the total mechanical energy $E_{total} = \frac{1}{2}m\omega^2 A^2$. | 动能或势能的最大值，等于总机械能 $E_{总} = \frac{1}{2}m\omega^2 A^2$。 |

---

# 3. Key Concepts / 关键概念

**English:**

### The Shape of Energy-Time Graphs

For an object undergoing SHM with displacement $x = A\sin(\omega t)$, the energy-time graphs have specific shapes:

1. **Kinetic Energy ($E_K$):** $E_K = \frac{1}{2}m\omega^2 A^2 \cos^2(\omega t)$ — a $\cos^2$ function, which is a sine wave oscillating between 0 and $E_{total}$ at frequency $2f$.

2. **Potential Energy ($E_P$):** $E_P = \frac{1}{2}m\omega^2 A^2 \sin^2(\omega t)$ — a $\sin^2$ function, also oscillating between 0 and $E_{total}$ at frequency $2f$.

3. **Total Energy ($E_{total}$):** $E_{total} = E_K + E_P = \frac{1}{2}m\omega^2 A^2$ — a constant horizontal line.

### Key Observations

- **KE and PE are complementary:** When KE is maximum, PE is zero (at equilibrium), and vice versa (at amplitude).
- **Energy oscillates at $2f$:** In one complete SHM cycle, KE and PE each complete *two* full cycles.
- **The sum is constant:** This demonstrates conservation of mechanical energy in ideal SHM.
- **Phase shift:** KE leads PE by $\pi/2$ radians (90°).

### Relationship to [[KE and PE in SHM]]

The energy-time graph is the *temporal* representation of the same physics described in [[KE and PE in SHM]]. While that sub-topic focuses on the formulas and instantaneous values, the energy-time graph shows the *evolution* of these values over time.

### Common Pitfalls

- **Confusing frequency:** Students often think KE and PE oscillate at the same frequency as displacement. Remember: $f_{energy} = 2f_{displacement}$.
- **Forgetting the constant total energy line:** Always include the horizontal $E_{total}$ line on the graph.
- **Misinterpreting phase:** KE is maximum at $t=0$ if $x = A\sin(\omega t)$, but if $x = A\cos(\omega t)$, the phase shifts.

**中文:**

### 能量-时间图的形状

对于位移为 $x = A\sin(\omega t)$ 的简谐运动物体，能量-时间图具有特定形状：

1. **动能 ($E_K$):** $E_K = \frac{1}{2}m\omega^2 A^2 \cos^2(\omega t)$ — 一个 $\cos^2$ 函数，是在0和 $E_{总}$ 之间以 $2f$ 频率振荡的正弦波。

2. **势能 ($E_P$):** $E_P = \frac{1}{2}m\omega^2 A^2 \sin^2(\omega t)$ — 一个 $\sin^2$ 函数，也是在0和 $E_{总}$ 之间以 $2f$ 频率振荡。

3. **总能量 ($E_{总}$):** $E_{总} = E_K + E_P = \frac{1}{2}m\omega^2 A^2$ — 一条恒定的水平线。

### 关键观察

- **动能和势能互补：** 当动能最大时，势能为零（在平衡位置），反之亦然（在振幅处）。
- **能量以 $2f$ 振荡：** 在一个完整的简谐运动周期中，动能和势能各完成*两个*完整周期。
- **总和恒定：** 这证明了理想简谐运动中机械能守恒。
- **相位差：** 动能领先势能 $\pi/2$ 弧度（90°）。

### 与[[KE and PE in SHM]]的关系

能量-时间图是[[KE and PE in SHM]]中描述的相同物理量的*时间*表示。该子知识点侧重于公式和瞬时值，而能量-时间图显示了这些值随时间的*演变*。

### 常见陷阱

- **混淆频率：** 学生常认为动能和势能以与位移相同的频率振荡。记住：$f_{能量} = 2f_{位移}$。
- **忘记恒定的总能量线：** 始终在图形上包含水平的 $E_{总}$ 线。
- **误解相位：** 如果 $x = A\sin(\omega t)$，动能在 $t=0$ 时最大；但如果 $x = A\cos(\omega t)$，相位会偏移。

---

# 4. Formulas / 公式

## Key Formula 1: Kinetic Energy as a Function of Time

$$E_K(t) = \frac{1}{2}m\omega^2 A^2 \cos^2(\omega t)$$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
| ------------- | ------------ | ------------ | ----------- |
| $E_K(t)$ | Kinetic energy at time $t$ | 时间 $t$ 时的动能 | J |
| $m$ | Mass of oscillating object | 振荡物体的质量 | kg |
| $\omega$ | Angular frequency | 角频率 | rad s$^{-1}$ |
| $A$ | Amplitude of oscillation | 振荡振幅 | m |
| $t$ | Time | 时间 | s |

## Key Formula 2: Potential Energy as a Function of Time

$$E_P(t) = \frac{1}{2}m\omega^2 A^2 \sin^2(\omega t)$$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
| ------------- | ------------ | ------------ | ----------- |
| $E_P(t)$ | Potential energy at time $t$ | 时间 $t$ 时的势能 | J |

## Key Formula 3: Total Mechanical Energy (Constant)

$$E_{total} = \frac{1}{2}m\omega^2 A^2$$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
| ------------- | ------------ | ------------ | ----------- |
| $E_{total}$ | Total mechanical energy | 总机械能 | J |

## Key Formula 4: Energy Oscillation Period

$$T_{energy} = \frac{T_{displacement}}{2} = \frac{\pi}{\omega}$$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
| ------------- | ------------ | ------------ | ----------- |
| $T_{energy}$ | Period of energy oscillation | 能量振荡周期 | s |
| $T_{displacement}$ | Period of displacement oscillation | 位移振荡周期 | s |

**Derivation / 推导:**

Starting from displacement $x = A\sin(\omega t)$ and velocity $v = \omega A\cos(\omega t)$:

$$E_K = \frac{1}{2}mv^2 = \frac{1}{2}m\omega^2 A^2 \cos^2(\omega t)$$

$$E_P = \frac{1}{2}kx^2 = \frac{1}{2}m\omega^2 x^2 = \frac{1}{2}m\omega^2 A^2 \sin^2(\omega t)$$

Using $\sin^2(\omega t) + \cos^2(\omega t) = 1$:

$$E_{total} = E_K + E_P = \frac{1}{2}m\omega^2 A^2[\sin^2(\omega t) + \cos^2(\omega t)] = \frac{1}{2}m\omega^2 A^2$$

**Conditions / 适用条件:**
- Ideal undamped SHM only (no energy loss)
- System with spring constant $k = m\omega^2$
- Valid for any SHM system (mass-spring, pendulum, etc.)

> 📷 **IMAGE PROMPT — ETG01: Energy-Time Graph for SHM**
>
> **English Prompt:**
> A clean, textbook-style graph with three curves on the same axes. X-axis: "Time / s" from 0 to 2T (where T is the period). Y-axis: "Energy / J" from 0 to E_total. Three curves: (1) A horizontal dashed line at E_total labelled "Total Energy", (2) A cosine-squared curve (starting at maximum) labelled "Kinetic Energy" in blue, (3) A sine-squared curve (starting at zero) labelled "Potential Energy" in red. The curves cross at E_total/2 at t = T/4, 3T/4, etc. Grid lines shown. Labels in English. Clean white background, vector style.
>
> **中文描述:**
> 一个干净的教科书风格图形，在同一坐标轴上显示三条曲线。X轴："时间 / s"，从0到2T（T为周期）。Y轴："能量 / J"，从0到E_total。三条曲线：(1) 在E_total处的水平虚线，标注"总能量"；(2) 余弦平方曲线（从最大值开始），蓝色，标注"动能"；(3) 正弦平方曲线（从零开始），红色，标注"势能"。曲线在t = T/4、3T/4等处交叉于E_total/2。显示网格线。英文标注。干净白色背景，矢量风格。
>
> **Labels Required / 需要标注:**
> * Total Energy (horizontal dashed line)
> * Kinetic Energy (blue cosine-squared curve)
> * Potential Energy (red sine-squared curve)
> * E_total (label on y-axis)
> * T (period marker on x-axis)
> * T/2, T/4 markers
> * Crossing points at E_total/2
>
> **Style / 风格:** Textbook vector / 教科书矢量图
>
> **Exam Relevance / 考试关联:**
> This is the most commonly tested graph for energy in SHM. Students must be able to sketch it, label it, and interpret it.

---

# 5. Image Prompt / 图片提示

> 📷 **IMAGE PROMPT — ETG02: Energy-Time Graph with Displacement Comparison**
>
> **English Prompt:**
> A dual-panel graph for comparison. Top panel: Standard displacement-time graph for SHM (sine wave, amplitude A, period T). Bottom panel: Energy-time graph (same time axis). Three curves in bottom panel: Total Energy (horizontal dashed), KE (blue cosine-squared), PE (red sine-squared). Vertical dashed lines connect key points between panels: at t=0 (displacement=0, KE=max, PE=0), at t=T/4 (displacement=A, KE=0, PE=max), at t=T/2 (displacement=0, KE=max, PE=0). Labels show "Equilibrium" and "Amplitude" at appropriate positions. Clean vector style, white background, English labels.
>
> **中文描述:**
> 用于比较的双面板图形。上面板：简谐运动的标准位移-时间图（正弦波，振幅A，周期T）。下面板：能量-时间图（相同时间轴）。下面板中的三条曲线：总能量（水平虚线），动能（蓝色余弦平方），势能（红色正弦平方）。垂直虚线连接面板之间的关键点：在t=0（位移=0，动能=最大，势能=0），在t=T/4（位移=A，动能=0，势能=最大），在t=T/2（位移=0，动能=最大，势能=0）。在适当位置标注"平衡位置"和"振幅"。干净矢量风格，白色背景，英文标注。
>
> **Labels Required / 需要标注:**
> * Displacement (top panel y-axis)
> * Energy (bottom panel y-axis)
> * Time (both x-axes)
> * A (amplitude on top panel)
> * E_total (on bottom panel)
> * Equilibrium positions
> * Amplitude positions
> * Connecting dashed lines
>
> **Style / 风格:** Textbook vector / 教科书矢量图
>
> **Exam Relevance / 考试关联:**
> This comparison helps students understand the relationship between displacement and energy, which is frequently tested in exam questions.

---

# 6. Worked Example / 典型例题

### Example 1: Reading Values from an Energy-Time Graph

### Question / 题目
**English:**
A mass-spring system oscillates with SHM. The energy-time graph shows that the total energy is 8.0 J, and the period of displacement oscillation is 2.0 s.

(a) What is the period of oscillation of the kinetic energy?
(b) At what time(s) in the first cycle is the kinetic energy equal to the potential energy?
(c) If the amplitude is 0.10 m and the mass is 0.50 kg, calculate the angular frequency $\omega$.

**中文:**
一个质量-弹簧系统以简谐运动振荡。能量-时间图显示总能量为8.0 J，位移振荡周期为2.0 s。

(a) 动能振荡的周期是多少？
(b) 在第一个周期中，动能等于势能的时间是什么？
(c) 如果振幅为0.10 m，质量为0.50 kg，计算角频率 $\omega$。

### Solution / 解答

**(a)** The energy oscillation period is half the displacement period:
$$T_{energy} = \frac{T_{displacement}}{2} = \frac{2.0}{2} = 1.0 \text{ s}$$

**(b)** KE = PE when both equal half the total energy:
$$E_K = E_P = \frac{E_{total}}{2} = 4.0 \text{ J}$$

From the graph, this occurs at $t = \frac{T_{displacement}}{8} = \frac{2.0}{8} = 0.25 \text{ s}$ and $t = \frac{3T_{displacement}}{8} = 0.75 \text{ s}$.

**(c)** Using $E_{total} = \frac{1}{2}m\omega^2 A^2$:
$$8.0 = \frac{1}{2}(0.50)\omega^2(0.10)^2$$
$$8.0 = 0.0025\omega^2$$
$$\omega^2 = \frac{8.0}{0.0025} = 3200$$
$$\omega = \sqrt{3200} = 56.6 \text{ rad s}^{-1}$$

### Final Answer / 最终答案
**Answer:** (a) 1.0 s (b) 0.25 s and 0.75 s (c) 56.6 rad s$^{-1}$
**答案:** (a) 1.0 秒 (b) 0.25 秒和 0.75 秒 (c) 56.6 弧度/秒

### Quick Tip / 提示
Remember that KE and PE are equal at $t = T/8$, $3T/8$, $5T/8$, $7T/8$ — these are the times when the oscillator is at $x = \pm A/\sqrt{2}$.

---

### Example 2: Sketching an Energy-Time Graph

### Question / 题目
**English:**
A particle of mass 0.20 kg oscillates with SHM of amplitude 0.050 m and angular frequency 40 rad s$^{-1}$.

(a) Calculate the total mechanical energy.
(b) Sketch the energy-time graph for one complete cycle of displacement, labelling all key values.
(c) On the same axes, sketch the graph if the amplitude is doubled.

**中文:**
一个质量为0.20 kg的粒子以振幅0.050 m和角频率40 rad s$^{-1}$进行简谐运动。

(a) 计算总机械能。
(b) 绘制一个完整位移周期的能量-时间图，标注所有关键值。
(c) 在同一坐标轴上，绘制振幅加倍时的图形。

### Solution / 解答

**(a)** 
$$E_{total} = \frac{1}{2}m\omega^2 A^2 = \frac{1}{2}(0.20)(40)^2(0.050)^2$$
$$E_{total} = \frac{1}{2}(0.20)(1600)(0.0025)$$
$$E_{total} = \frac{1}{2}(0.20)(4.0) = 0.40 \text{ J}$$

**(b)** The displacement period: $T = \frac{2\pi}{\omega} = \frac{2\pi}{40} = 0.157 \text{ s}$
The energy period: $T_{energy} = \frac{T}{2} = 0.0785 \text{ s}$

Key values on the graph:
- Total energy: horizontal line at 0.40 J
- KE: starts at 0.40 J (maximum), reaches 0 J at $t = T/4 = 0.0393$ s
- PE: starts at 0 J, reaches 0.40 J at $t = T/4 = 0.0393$ s
- KE = PE = 0.20 J at $t = T/8 = 0.0196$ s

**(c)** If $A$ is doubled, $E_{total}$ increases by a factor of 4:
$$E_{total(new)} = 4 \times 0.40 = 1.60 \text{ J}$$

The new graph has the same period but all energy values are multiplied by 4.

### Final Answer / 最终答案
**Answer:** (a) 0.40 J (b) Graph with E_total = 0.40 J, T_energy = 0.0785 s (c) New E_total = 1.60 J
**答案:** (a) 0.40 焦耳 (b) 图形：E_total = 0.40 J，T_能量 = 0.0785 秒 (c) 新 E_total = 1.60 J

### Quick Tip / 提示
When amplitude changes, the shape of the energy-time graph remains the same (same period), but the amplitude of the energy oscillation changes. Since $E \propto A^2$, doubling $A$ quadruples $E$.

---

# 7. Flashcards / 闪卡

**Flashcard 1**
Q (EN): What is the relationship between the period of energy oscillation and the period of displacement oscillation in SHM?
Q (CN): 在简谐运动中，能量振荡周期与位移振荡周期之间有什么关系？
A (EN): The energy oscillation period is half the displacement oscillation period: $T_{energy} = T_{displacement}/2$.
A (CN): 能量振荡周期是位移振荡周期的一半：$T_{能量} = T_{位移}/2$。

**Flashcard 2**
Q (EN): At what times in one complete SHM cycle are kinetic energy and potential energy equal?
Q (CN): 在一个完整的简谐运动周期中，动能和势能在哪些时间相等？
A (EN): At $t = T/8$, $3T/8$, $5T/8$, and $7T/8$ (where T is the displacement period).
A (CN): 在 $t = T/8$、$3T/8$、$5T/8$ 和 $7T/8$ 时（其中 T 是位移周期）。

**Flashcard 3**
Q (EN): What is the phase difference between kinetic energy and potential energy in SHM?
Q (CN): 在简谐运动中，动能和势能之间的相位差是多少？
A (EN): They are $\pi/2$ radians (90°) out of phase — when one is maximum, the other is zero.
A (CN): 它们相差 $\pi/2$ 弧度（90°）——当一个最大时，另一个为零。

**Flashcard 4**
Q (EN): If the amplitude of SHM is doubled, what happens to the total mechanical energy?
Q (CN): 如果简谐运动的振幅加倍，总机械能会发生什么变化？
A (EN): The total energy increases by a factor of 4 (since $E \propto A^2$).
A (CN): 总能量增加4倍（因为 $E \propto A^2$）。

**Flashcard 5**
Q (EN): Sketch the energy-time graph for undamped SHM, showing KE, PE, and total energy.
Q (CN): 绘制无阻尼简谐运动的能量-时间图，显示动能、势能和总能量。
A (EN): A horizontal line for total energy; a cosine-squared curve for KE (starting at maximum); a sine-squared curve for PE (starting at zero); both oscillating at twice the displacement frequency.
A (CN): 总能量为水平线；动能为余弦平方曲线（从最大值开始）；势能为正弦平方曲线（从零开始）；两者都以位移频率的两倍振荡。

---

# 8. Metadata / 元数据

```yaml
title:
  en: Energy-Time Graphs for SHM
  cn: 简谐运动的能量-时间图
parent_topic: Energy in SHM
parent_hub: "[[Energy in SHM]]"
subject: Physics
syllabus:
  - CAIE 9702
  - Edexcel IAL
level: A2
node_type: leaf_concept
difficulty: intermediate
related_leaf_nodes:
  - "[[KE and PE in SHM]]"
  - "[[Energy-Displacement Graphs for SHM]]"
prerequisites:
  - "[[Simple Harmonic Motion]]"
  - "[[Kinetic Energy and Potential Energy]]"
related_topics:
  - "[[Damped and Forced Oscillations / Resonance]]"
language: bilingual_en_cn