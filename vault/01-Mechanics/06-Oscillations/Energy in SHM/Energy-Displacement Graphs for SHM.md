# 1. Overview / 概述

**English:**
Energy-Displacement Graphs for SHM provide a powerful visual tool for understanding how kinetic energy (KE) and potential energy (PE) vary as an oscillating object moves through its cycle. Unlike [[Energy-Time Graphs for SHM]] which show energy changes over time, these graphs plot energy against displacement from equilibrium, revealing the fundamental relationship between position and energy storage. This sub-topic is crucial for understanding the conservation of mechanical energy in [[Simple Harmonic Motion]] and forms the foundation for analyzing [[Damped and Forced Oscillations / Resonance]] where energy is gradually lost. The parabolic shape of these graphs is a direct consequence of the restoring force being proportional to displacement (Hooke's law).

**中文:**
简谐运动的能量-位移图提供了一个强大的可视化工具，用于理解当振荡物体在其周期中运动时，动能和势能如何变化。与[[Energy-Time Graphs for SHM]]不同，这些图将能量相对于平衡位置的位移绘制出来，揭示了位置与能量储存之间的基本关系。这个子知识点对于理解[[Simple Harmonic Motion]]中的机械能守恒至关重要，并为分析[[Damped and Forced Oscillations / Resonance]]（能量逐渐损失）奠定了基础。这些图的抛物线形状是恢复力与位移成正比（胡克定律）的直接结果。

---

# 2. Core Definition / 核心定义

| Term (EN/CN) | Definition (EN) | Definition (CN) |
| ------------ | --------------- | --------------- |
| **Energy-Displacement Graph** / 能量-位移图 | A graph showing how kinetic energy (KE) and potential energy (PE) of an SHM oscillator vary with displacement from equilibrium. | 显示简谐运动振荡器的动能和势能如何随距平衡位置的位移变化的图表。 |
| **Total Energy (E)** / 总能量 | The constant sum of KE and PE in undamped SHM, equal to the maximum PE at amplitude. | 无阻尼简谐运动中动能和势能的恒定总和，等于振幅处的最大势能。 |
| **Amplitude (A)** / 振幅 | The maximum displacement from equilibrium, where KE = 0 and PE = E. | 距平衡位置的最大位移，此处动能=0，势能=总能量。 |
| **Equilibrium Position** / 平衡位置 | The point where displacement x = 0, where PE = 0 and KE = E. | 位移x=0的点，此处势能=0，动能=总能量。 |
| **Parabolic Relationship** / 抛物线关系 | The quadratic dependence of PE on displacement: PE ∝ x². | 势能对位移的二次依赖关系：PE ∝ x²。 |

---

# 3. Key Concepts / 关键概念

**English:**
The energy-displacement graph for SHM is fundamentally different from the [[Energy-Time Graphs for SHM]]. While time graphs show sinusoidal variations, displacement graphs reveal the **parabolic** nature of potential energy.

**Key features of the graph:**
1. **Potential Energy (PE):** Follows a parabolic curve: $PE = \frac{1}{2}kx^2$. At $x = \pm A$, PE reaches its maximum value $E = \frac{1}{2}kA^2$. At $x = 0$, PE = 0.
2. **Kinetic Energy (KE):** Follows an inverted parabola: $KE = E - PE = \frac{1}{2}k(A^2 - x^2)$. At $x = 0$, KE is maximum ($E$). At $x = \pm A$, KE = 0.
3. **Total Energy (E):** A horizontal straight line at $y = E$, representing conservation of mechanical energy.

**Physical interpretation:**
- When the oscillator is at maximum displacement (turning points), all energy is stored as potential energy.
- When passing through equilibrium, all energy is kinetic.
- At any intermediate displacement, energy is shared between KE and PE.

**Common pitfalls:**
- ❌ Thinking KE and PE are sinusoidal functions of displacement (they are parabolic).
- ❌ Confusing displacement graphs with time graphs.
- ❌ Forgetting that total energy remains constant only in undamped SHM.

**中文:**
简谐运动的能量-位移图与[[Energy-Time Graphs for SHM]]有根本不同。时间图显示正弦变化，而位移图揭示了势能的**抛物线**性质。

**图的关键特征：**
1. **势能 (PE):** 遵循抛物线曲线：$PE = \frac{1}{2}kx^2$。在 $x = \pm A$ 处，PE达到最大值 $E = \frac{1}{2}kA^2$。在 $x = 0$ 处，PE = 0。
2. **动能 (KE):** 遵循倒置抛物线：$KE = E - PE = \frac{1}{2}k(A^2 - x^2)$。在 $x = 0$ 处，KE最大（$E$）。在 $x = \pm A$ 处，KE = 0。
3. **总能量 (E):** 在 $y = E$ 处的水平直线，代表机械能守恒。

**物理解释：**
- 当振荡器处于最大位移（转折点）时，所有能量都储存为势能。
- 当经过平衡位置时，所有能量都是动能。
- 在任何中间位移处，能量在动能和势能之间分配。

**常见陷阱：**
- ❌ 认为动能和势能是位移的正弦函数（它们是抛物线函数）。
- ❌ 将位移图与时间图混淆。
- ❌ 忘记总能量仅在无阻尼简谐运动中保持恒定。

---

# 4. Formulas / 公式

## Primary Formula

$$PE = \frac{1}{2}kx^2$$

$$KE = \frac{1}{2}k(A^2 - x^2)$$

$$E = \frac{1}{2}kA^2$$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
| ------------- | ------------ | ------------ | ----------- |
| $PE$ | Potential energy | 势能 | J |
| $KE$ | Kinetic energy | 动能 | J |
| $E$ | Total mechanical energy | 总机械能 | J |
| $k$ | Spring constant / force constant | 弹簧常数/力常数 | N/m |
| $A$ | Amplitude | 振幅 | m |
| $x$ | Displacement from equilibrium | 距平衡位置的位移 | m |

**Derivation / 推导:**
1. For SHM, restoring force $F = -kx$, so potential energy is the work done against this force:
   $$PE = \int_0^x kx \, dx = \frac{1}{2}kx^2$$
2. At maximum displacement $x = A$, $PE = E = \frac{1}{2}kA^2$
3. By conservation of energy: $KE = E - PE = \frac{1}{2}kA^2 - \frac{1}{2}kx^2 = \frac{1}{2}k(A^2 - x^2)$

**Conditions / 适用条件:**
- Valid only for **undamped** SHM (no energy loss)
- Assumes ideal spring or pendulum with small amplitude
- $x$ is measured from equilibrium position

> 📷 **IMAGE PROMPT — EDS-01: Energy-Displacement Graph for SHM**
>
> **English Prompt:**
> A clean, textbook-style 2D vector graph with three curves on the same axes. X-axis labeled "Displacement x (m)" ranging from -A to +A. Y-axis labeled "Energy (J)" ranging from 0 to E. A horizontal dashed line at y = E labeled "Total Energy E". A blue upward-opening parabola labeled "PE = ½kx²" starting at (0,0) and reaching (A,E) and (-A,E). A red downward-opening parabola labeled "KE = ½k(A²-x²)" starting at (0,E) and reaching (A,0) and (-A,0). Vertical dashed lines at x = ±A. Clear grid lines. White background. Professional physics textbook style.
>
> **中文描述:**
> 一个干净、教科书风格的2D矢量图，在同一坐标轴上有三条曲线。X轴标记为"位移 x (m)"，范围从-A到+A。Y轴标记为"能量 (J)"，范围从0到E。在y=E处有一条水平虚线标记为"总能量 E"。一条蓝色向上开口的抛物线标记为"PE = ½kx²"，从(0,0)开始到达(A,E)和(-A,E)。一条红色向下开口的抛物线标记为"KE = ½k(A²-x²)"，从(0,E)开始到达(A,0)和(-A,0)。在x=±A处有垂直虚线。清晰的网格线。白色背景。专业物理教科书风格。
>
> **Labels Required / 需要标注:**
> * PE curve (blue parabola)
> * KE curve (red inverted parabola)
> * Total Energy (horizontal dashed line)
> * Amplitude points (±A)
> * Equilibrium point (x=0)
>
> **Style / 风格:** Textbook vector / 2D graph
>
> **Exam Relevance / 考试关联:**
> This graph is frequently tested in A-Level exams. Students must be able to sketch it, label key points, and explain why PE is parabolic and KE is its complement.

---

# 5. Image Prompt / 图片提示

> 📷 **IMAGE PROMPT — EDS-02: Mass-Spring System with Energy States**
>
> **English Prompt:**
> A 3D rendered split-screen diagram. Left side: A mass-spring system on a frictionless horizontal surface showing three positions: (1) mass at x=+A with spring fully stretched, (2) mass at x=0 with spring at natural length, (3) mass at x=-A with spring fully compressed. Each position has a color-coded energy bar: blue for PE, red for KE. Right side: The corresponding energy-displacement graph with the three positions marked as points on the curves. The mass is a metallic cube, the spring is silver. Clean lighting, educational style, white background.
>
> **中文描述:**
> 一个3D渲染的分屏图。左侧：一个在无摩擦水平面上的质量-弹簧系统，显示三个位置：(1) 质量在x=+A处，弹簧完全拉伸，(2) 质量在x=0处，弹簧处于自然长度，(3) 质量在x=-A处，弹簧完全压缩。每个位置都有一个颜色编码的能量条：蓝色代表势能，红色代表动能。右侧：相应的能量-位移图，三个位置标记为曲线上的点。质量是一个金属立方体，弹簧是银色的。清晰的光照，教育风格，白色背景。
>
> **Labels Required / 需要标注:**
> * Three positions: +A, 0, -A
> * Energy bars showing PE (blue) and KE (red) proportions
> * Corresponding points on the graph
>
> **Style / 风格:** 3D render / educational illustration
>
> **Exam Relevance / 考试关联:**
> Helps students visualize the physical meaning of the graph — connecting the oscillator's position to the energy distribution.

---

# 6. Worked Example / 典型例题

### Example 1: Reading the Graph

### Question / 题目
**English:**
A 0.50 kg mass oscillates on a spring with spring constant $k = 200 \text{ N/m}$ and amplitude $A = 0.10 \text{ m}$.
(a) Calculate the total energy of the system.
(b) Calculate the kinetic energy when the displacement is $x = 0.060 \text{ m}$.
(c) At what displacement is the kinetic energy equal to the potential energy?

**中文:**
一个0.50 kg的质量在弹簧常数为 $k = 200 \text{ N/m}$、振幅 $A = 0.10 \text{ m}$ 的弹簧上振荡。
(a) 计算系统的总能量。
(b) 计算位移为 $x = 0.060 \text{ m}$ 时的动能。
(c) 在什么位移处动能等于势能？

### Solution / 解答

**(a) Total Energy:**
$$E = \frac{1}{2}kA^2 = \frac{1}{2}(200)(0.10)^2 = 1.0 \text{ J}$$

**(b) Kinetic Energy at x = 0.060 m:**
$$PE = \frac{1}{2}kx^2 = \frac{1}{2}(200)(0.060)^2 = 0.36 \text{ J}$$
$$KE = E - PE = 1.0 - 0.36 = 0.64 \text{ J}$$

**(c) When KE = PE:**
$$KE = PE \implies \frac{1}{2}k(A^2 - x^2) = \frac{1}{2}kx^2$$
$$A^2 - x^2 = x^2 \implies A^2 = 2x^2$$
$$x = \pm \frac{A}{\sqrt{2}} = \pm \frac{0.10}{\sqrt{2}} = \pm 0.071 \text{ m}$$

### Final Answer / 最终答案
**Answer:** (a) $E = 1.0 \text{ J}$ (b) $KE = 0.64 \text{ J}$ (c) $x = \pm 0.071 \text{ m}$
**答案:** (a) $E = 1.0 \text{ J}$ (b) $KE = 0.64 \text{ J}$ (c) $x = \pm 0.071 \text{ m}$

### Quick Tip / 提示
**English:** When KE = PE, the displacement is always $x = \pm A/\sqrt{2}$ regardless of the values of $k$ and $A$. This is a common exam shortcut!
**中文:** 当动能等于势能时，位移总是 $x = \pm A/\sqrt{2}$，与 $k$ 和 $A$ 的值无关。这是一个常见的考试技巧！

---

### Example 2: Graph Interpretation

### Question / 题目
**English:**
The graph shows the energy-displacement relationship for an SHM oscillator. The total energy is 8.0 J and the amplitude is 0.20 m.
(a) Determine the spring constant $k$.
(b) Sketch the KE curve on the same axes.
(c) Find the displacement where KE = 3.0 J.

**中文:**
该图显示了一个简谐运动振荡器的能量-位移关系。总能量为8.0 J，振幅为0.20 m。
(a) 确定弹簧常数 $k$。
(b) 在同一坐标轴上画出动能曲线。
(c) 找到动能=3.0 J时的位移。

### Solution / 解答

**(a) Spring constant:**
$$E = \frac{1}{2}kA^2 \implies k = \frac{2E}{A^2} = \frac{2(8.0)}{(0.20)^2} = 400 \text{ N/m}$$

**(b) KE curve:**
The KE curve is an inverted parabola: $KE = \frac{1}{2}k(A^2 - x^2) = 8.0 - 400x^2$
It starts at (0, 8.0) and reaches zero at $x = \pm 0.20 \text{ m}$.

**(c) Displacement when KE = 3.0 J:**
$$KE = E - \frac{1}{2}kx^2 \implies 3.0 = 8.0 - \frac{1}{2}(400)x^2$$
$$\frac{1}{2}(400)x^2 = 5.0 \implies 200x^2 = 5.0$$
$$x^2 = 0.025 \implies x = \pm 0.158 \text{ m}$$

### Final Answer / 最终答案
**Answer:** (a) $k = 400 \text{ N/m}$ (b) Inverted parabola (c) $x = \pm 0.158 \text{ m}$
**答案:** (a) $k = 400 \text{ N/m}$ (b) 倒置抛物线 (c) $x = \pm 0.158 \text{ m}$

### Quick Tip / 提示
**English:** Always check your answer makes physical sense: KE = 3.0 J is less than E = 8.0 J, so the displacement should be less than A = 0.20 m. ✓
**中文:** 始终检查答案是否合理：KE = 3.0 J 小于 E = 8.0 J，所以位移应小于 A = 0.20 m。✓

---

# 7. Flashcards / 闪卡

**Flashcard 1:**
Q (EN): What shape is the PE-displacement graph for SHM?
Q (CN): 简谐运动的势能-位移图是什么形状？
A (EN): A parabola (upward opening), because PE = ½kx².
A (CN): 抛物线（向上开口），因为 PE = ½kx²。

**Flashcard 2:**
Q (EN): At what displacement(s) is KE = PE in SHM?
Q (CN): 在简谐运动中，什么位移处动能等于势能？
A (EN): At x = ±A/√2 (approximately ±0.707A).
A (CN): 在 x = ±A/√2（约 ±0.707A）处。

**Flashcard 3:**
Q (EN): What is the total energy of an SHM oscillator in terms of k and A?
Q (CN): 简谐运动振荡器的总能量用k和A如何表示？
A (EN): E = ½kA²
A (CN): E = ½kA²

**Flashcard 4:**
Q (EN): What is the kinetic energy at displacement x in SHM?
Q (CN): 简谐运动中位移x处的动能是多少？
A (EN): KE = ½k(A² - x²)
A (CN): KE = ½k(A² - x²)

**Flashcard 5:**
Q (EN): How does the energy-displacement graph differ from the energy-time graph?
Q (CN): 能量-位移图与能量-时间图有何不同？
A (EN): Energy-displacement graphs show parabolic relationships, while energy-time graphs show sinusoidal variations.
A (CN): 能量-位移图显示抛物线关系，而能量-时间图显示正弦变化。

---

# 8. Metadata / 元数据

```yaml
title:
  en: "Energy-Displacement Graphs for SHM"
  cn: "简谐运动的能量-位移图"
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
  - "[[KE and PE in SHM]]"
  - "[[Energy-Time Graphs for SHM]]"
prerequisites:
  - "[[Simple Harmonic Motion]]"
  - "[[Kinetic Energy and Potential Energy]]"
related_topics:
  - "[[Damped and Forced Oscillations / Resonance]]"
language: bilingual_en_cn