# 1. Overview / 概述

**English:**
This sub-topic explores the mathematical relationships between displacement, velocity, and acceleration in Simple Harmonic Motion (SHM). Unlike linear motion where these quantities follow polynomial relationships, SHM exhibits sinusoidal variations governed by the phase angle $(\omega t + \phi)$. Understanding these relationships is fundamental to analysing oscillatory systems, from pendulums to mass-spring systems. The key insight is that acceleration is always proportional to negative displacement, which is the defining characteristic of SHM and links directly to [[Conditions for SHM]].

**中文:**
本子知识点探讨简谐运动中位移、速度和加速度之间的数学关系。与线性运动中这些量遵循多项式关系不同，SHM 表现出由相位角 $(\omega t + \phi)$ 控制的正弦变化。理解这些关系是分析从摆到弹簧质量系统等振荡系统的基础。关键在于加速度始终与位移成正比且方向相反，这是 SHM 的定义特征，并直接与 [[Conditions for SHM]] 相关联。

---

# 2. Core Definition / 核心定义

| Term (EN/CN) | Definition (EN) | Definition (CN) |
| ------------ | --------------- | --------------- |
| **Displacement** / 位移 | The distance of the oscillating object from its equilibrium position at any instant, measured in metres (m). | 振荡物体在任意时刻相对于平衡位置的距离，单位为米 (m)。 |
| **Amplitude** / 振幅 | The maximum displacement from equilibrium, denoted by $A$ or $x_0$. | 从平衡位置出发的最大位移，用 $A$ 或 $x_0$ 表示。 |
| **Angular Frequency** / 角频率 | The rate of change of phase angle, $\omega = 2\pi f$, measured in rad s⁻¹. | 相位角的变化率，$\omega = 2\pi f$，单位为 rad s⁻¹。 |
| **Phase Angle** / 相位角 | The argument $(\omega t + \phi)$ that determines the instantaneous state of oscillation. | 决定振荡瞬时状态的参数 $(\omega t + \phi)$。 |
| **Phase Constant** / 初相位 | The initial phase angle $\phi$ at $t = 0$, determining the starting position. | 在 $t = 0$ 时的初始相位角 $\phi$，决定起始位置。 |
| **Velocity** / 速度 | The rate of change of displacement, $v = \frac{dx}{dt}$, measured in m s⁻¹. | 位移的变化率，$v = \frac{dx}{dt}$，单位为 m s⁻¹。 |
| **Acceleration** / 加速度 | The rate of change of velocity, $a = \frac{dv}{dt}$, measured in m s⁻². | 速度的变化率，$a = \frac{dv}{dt}$，单位为 m s⁻²。 |

---

# 3. Key Concepts / 关键概念

**English:**
The core of SHM kinematics lies in the sinusoidal nature of displacement. Starting from the general solution:

$$ x(t) = A \sin(\omega t + \phi) \quad \text{or} \quad x(t) = A \cos(\omega t + \phi) $$

The choice between sine and cosine depends on the initial conditions. For example, if the oscillator starts at equilibrium moving in the positive direction, use $x = A \sin(\omega t)$; if it starts at maximum displacement, use $x = A \cos(\omega t)$.

**Velocity** is obtained by differentiating displacement with respect to time:

$$ v(t) = \frac{dx}{dt} = A\omega \cos(\omega t + \phi) \quad \text{or} \quad v(t) = -A\omega \sin(\omega t + \phi) $$

Key observations:
- Velocity leads displacement by $\frac{\pi}{2}$ radians (90°).
- Maximum velocity $v_{\text{max}} = A\omega$ occurs at equilibrium ($x = 0$).
- Velocity is zero at the turning points ($x = \pm A$).

**Acceleration** is obtained by differentiating velocity:

$$ a(t) = \frac{dv}{dt} = -A\omega^2 \sin(\omega t + \phi) = -\omega^2 x(t) $$

This is the **defining equation** of SHM: $a = -\omega^2 x$. It shows:
- Acceleration is always directed towards equilibrium (restoring force).
- Acceleration leads displacement by $\pi$ radians (180°), i.e., they are in anti-phase.
- Maximum acceleration $a_{\text{max}} = A\omega^2$ occurs at the turning points.

**Phase Relationships:**
- Displacement and acceleration: anti-phase (180° apart)
- Displacement and velocity: 90° apart (velocity leads)
- Velocity and acceleration: 90° apart (acceleration leads)

**Common Pitfalls:**
1. Confusing the sign of velocity — remember velocity is positive when moving away from equilibrium in the positive direction.
2. Forgetting that $v_{\text{max}} = A\omega$ only applies when using the correct form of the velocity equation.
3. Mixing up the phase constant $\phi$ — always check initial conditions.

**中文:**
SHM 运动学的核心在于位移的正弦性质。从通解出发：

$$ x(t) = A \sin(\omega t + \phi) \quad \text{或} \quad x(t) = A \cos(\omega t + \phi) $$

正弦和余弦的选择取决于初始条件。例如，如果振荡器从平衡位置开始向正方向运动，使用 $x = A \sin(\omega t)$；如果从最大位移开始，使用 $x = A \cos(\omega t)$。

**速度** 通过对位移求时间导数得到：

$$ v(t) = \frac{dx}{dt} = A\omega \cos(\omega t + \phi) \quad \text{或} \quad v(t) = -A\omega \sin(\omega t + \phi) $$

关键观察：
- 速度领先位移 $\frac{\pi}{2}$ 弧度（90°）。
- 最大速度 $v_{\text{max}} = A\omega$ 出现在平衡位置（$x = 0$）。
- 速度在转折点（$x = \pm A$）为零。

**加速度** 通过对速度求导得到：

$$ a(t) = \frac{dv}{dt} = -A\omega^2 \sin(\omega t + \phi) = -\omega^2 x(t) $$

这是 SHM 的**定义方程**：$a = -\omega^2 x$。它表明：
- 加速度始终指向平衡位置（恢复力）。
- 加速度领先位移 $\pi$ 弧度（180°），即它们反相。
- 最大加速度 $a_{\text{max}} = A\omega^2$ 出现在转折点。

**相位关系：**
- 位移和加速度：反相（相差 180°）
- 位移和速度：相差 90°（速度领先）
- 速度和加速度：相差 90°（加速度领先）

**常见错误：**
1. 混淆速度的符号——记住当物体沿正方向远离平衡位置时速度为正。
2. 忘记 $v_{\text{max}} = A\omega$ 仅在使用正确形式的速度方程时成立。
3. 混淆初相位 $\phi$——始终检查初始条件。

---

# 4. Formulas / 公式

## Displacement Equation / 位移方程

$$ x(t) = A \sin(\omega t + \phi) $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
| ------------- | ------------ | ------------ | ----------- |
| $x(t)$ | Displacement at time $t$ | 时刻 $t$ 的位移 | m |
| $A$ | Amplitude | 振幅 | m |
| $\omega$ | Angular frequency | 角频率 | rad s⁻¹ |
| $t$ | Time | 时间 | s |
| $\phi$ | Phase constant | 初相位 | rad |

## Velocity Equation / 速度方程

$$ v(t) = A\omega \cos(\omega t + \phi) $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
| ------------- | ------------ | ------------ | ----------- |
| $v(t)$ | Velocity at time $t$ | 时刻 $t$ 的速度 | m s⁻¹ |
| $A\omega$ | Maximum velocity $v_{\text{max}}$ | 最大速度 $v_{\text{max}}$ | m s⁻¹ |

## Acceleration Equation / 加速度方程

$$ a(t) = -A\omega^2 \sin(\omega t + \phi) = -\omega^2 x(t) $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
| ------------- | ------------ | ------------ | ----------- |
| $a(t)$ | Acceleration at time $t$ | 时刻 $t$ 的加速度 | m s⁻² |
| $A\omega^2$ | Maximum acceleration $a_{\text{max}}$ | 最大加速度 $a_{\text{max}}$ | m s⁻² |

## Velocity-Displacement Relationship / 速度-位移关系

$$ v^2 = \omega^2 (A^2 - x^2) $$

This is derived from the energy conservation approach or by eliminating $t$ from the displacement and velocity equations. It shows that velocity depends only on displacement, not on time directly.

**Derivation / 推导:**
Starting from $x = A\sin(\omega t + \phi)$ and $v = A\omega\cos(\omega t + \phi)$:
Using $\sin^2\theta + \cos^2\theta = 1$:
$$\frac{x^2}{A^2} + \frac{v^2}{A^2\omega^2} = 1$$
Rearranging: $v^2 = \omega^2(A^2 - x^2)$

**Conditions / 适用条件:**
- Valid for all SHM systems where $a = -\omega^2 x$
- Assumes no damping (energy conserved)
- Works for both sine and cosine forms

> 📷 **IMAGE PROMPT — SHM01: Displacement, Velocity, Acceleration Graphs**
>
> **English Prompt:**
> A clean textbook-style diagram showing three stacked graphs of displacement (x), velocity (v), and acceleration (a) versus time (t) for simple harmonic motion. The top graph shows a sine wave labeled x = A sin(ωt) with amplitude A marked. The middle graph shows a cosine wave labeled v = Aω cos(ωt) with maximum velocity Aω marked. The bottom graph shows a negative sine wave labeled a = -Aω² sin(ωt) with maximum acceleration Aω² marked. Vertical dashed lines align the three graphs at key points: t=0, t=T/4, t=T/2, t=3T/4, t=T. Phase differences of π/2 and π are indicated with arrows. Use blue for displacement, red for velocity, green for acceleration. White background, black axes with gridlines. Labels in English.
>
> **中文描述:**
> 一个清晰的教科书风格图表，显示三个堆叠的简谐运动位移(x)、速度(v)和加速度(a)随时间(t)变化的曲线图。顶部图显示标记为 x = A sin(ωt) 的正弦波，振幅 A 已标注。中间图显示标记为 v = Aω cos(ωt) 的余弦波，最大速度 Aω 已标注。底部图显示标记为 a = -Aω² sin(ωt) 的负正弦波，最大加速度 Aω² 已标注。垂直虚线在关键点对齐三个图：t=0、t=T/4、t=T/2、t=3T/4、t=T。用箭头指示 π/2 和 π 的相位差。位移用蓝色，速度用红色，加速度用绿色。白色背景，黑色坐标轴带网格线。英文标注。
>
> **Labels Required / 需要标注:**
> * x = A sin(ωt) — displacement equation
> * v = Aω cos(ωt) — velocity equation
> * a = -Aω² sin(ωt) — acceleration equation
> * Phase difference: π/2 (velocity leads displacement)
> * Phase difference: π (acceleration anti-phase with displacement)
> * A, Aω, Aω² — maximum values
>
> **Style / 风格:** Textbook vector / 教科书矢量图
>
> **Exam Relevance / 考试关联:**
> Essential for interpreting SHM graphs in exams. Students must be able to read phase differences and maximum values from such graphs.

---

# 5. Image Prompt / 图片提示

> 📷 **IMAGE PROMPT — SHM02: Velocity-Displacement Graph (Phase Portrait)**
>
> **English Prompt:**
> A phase portrait diagram showing velocity (v) versus displacement (x) for simple harmonic motion. The graph is an ellipse centered at the origin, with equation v² = ω²(A² - x²). The x-axis is labeled "Displacement x (m)" ranging from -A to +A. The v-axis is labeled "Velocity v (m/s)" ranging from -Aω to +Aω. Key points marked: (A, 0) — turning point where v=0; (0, Aω) — equilibrium with maximum positive velocity; (0, -Aω) — equilibrium with maximum negative velocity; (-A, 0) — opposite turning point. Arrows on the ellipse show clockwise direction of motion. A small pendulum or mass-spring system icon in the corner indicates the physical system. White background, clean vector style, English labels.
>
> **中文描述:**
> 一个显示简谐运动速度(v)与位移(x)关系的相图。图形是一个以原点为中心的椭圆，方程为 v² = ω²(A² - x²)。x 轴标记为"位移 x (m)"，范围从 -A 到 +A。v 轴标记为"速度 v (m/s)"，范围从 -Aω 到 +Aω。关键点已标注：(A, 0) — 转折点，v=0；(0, Aω) — 平衡位置，最大正速度；(0, -Aω) — 平衡位置，最大负速度；(-A, 0) — 另一转折点。椭圆上的箭头显示顺时针运动方向。角落有一个小摆或弹簧质量系统图标表示物理系统。白色背景，干净矢量风格，英文标注。
>
> **Labels Required / 需要标注:**
> * v² = ω²(A² - x²) — equation
> * (A, 0) — turning point
> * (0, Aω) — max velocity
> * Clockwise direction arrow
>
> **Style / 风格:** Textbook vector / 教科书矢量图
>
> **Exam Relevance / 考试关联:**
> This graph is frequently used in exam questions to test understanding of the relationship between velocity and displacement. Students must be able to interpret the ellipse and identify key points.

---

# 6. Worked Example / 典型例题

### Example 1: Finding Velocity and Acceleration at a Given Displacement

### Question / 题目
**English:**
A particle oscillates with SHM of amplitude 0.05 m and frequency 2.0 Hz. At a certain instant, the displacement is 0.03 m from equilibrium. Calculate:
(a) The angular frequency
(b) The speed of the particle at this displacement
(c) The acceleration of the particle at this displacement

**中文:**
一个质点以振幅 0.05 m 和频率 2.0 Hz 做简谐运动。在某一时刻，位移为距平衡位置 0.03 m。计算：
(a) 角频率
(b) 质点在该位移处的速度
(c) 质点在该位移处的加速度

### Solution / 解答

**Step 1: Calculate angular frequency**
$$\omega = 2\pi f = 2\pi \times 2.0 = 4\pi \text{ rad s}^{-1} \approx 12.57 \text{ rad s}^{-1}$$

**Step 2: Use velocity-displacement relationship**
$$v^2 = \omega^2(A^2 - x^2)$$
$$v^2 = (4\pi)^2 \times (0.05^2 - 0.03^2)$$
$$v^2 = 16\pi^2 \times (0.0025 - 0.0009)$$
$$v^2 = 16\pi^2 \times 0.0016$$
$$v^2 = 0.0256\pi^2$$
$$v = \pm 0.16\pi \text{ m s}^{-1} \approx \pm 0.503 \text{ m s}^{-1}$$

The sign depends on direction of motion.

**Step 3: Calculate acceleration**
$$a = -\omega^2 x = -(4\pi)^2 \times 0.03$$
$$a = -16\pi^2 \times 0.03$$
$$a = -0.48\pi^2 \text{ m s}^{-2} \approx -4.74 \text{ m s}^{-2}$$

The negative sign indicates acceleration is towards equilibrium.

### Final Answer / 最终答案
**Answer:** (a) $\omega = 4\pi \text{ rad s}^{-1}$ (b) $v = \pm 0.503 \text{ m s}^{-1}$ (c) $a = -4.74 \text{ m s}^{-2}$
**答案:** (a) $\omega = 4\pi \text{ rad s}^{-1}$ (b) $v = \pm 0.503 \text{ m s}^{-1}$ (c) $a = -4.74 \text{ m s}^{-2}$

### Quick Tip / 提示
**English:** Always use the velocity-displacement relationship $v^2 = \omega^2(A^2 - x^2)$ when you know displacement but not time. It's faster than using the sinusoidal equations.
**中文:** 当你知道位移但不知道时间时，始终使用速度-位移关系 $v^2 = \omega^2(A^2 - x^2)$。这比使用正弦方程更快。

---

### Example 2: Phase Difference Problem

### Question / 题目
**English:**
An object oscillates with SHM described by $x = 0.08 \cos(3\pi t)$ where $x$ is in metres and $t$ in seconds. Determine:
(a) The amplitude and angular frequency
(b) The velocity as a function of time
(c) The time when the object first reaches maximum velocity

**中文:**
一个物体做简谐运动，方程为 $x = 0.08 \cos(3\pi t)$，其中 $x$ 单位为米，$t$ 单位为秒。求：
(a) 振幅和角频率
(b) 速度作为时间的函数
(c) 物体首次达到最大速度的时间

### Solution / 解答

**Step 1: Read from equation**
Amplitude $A = 0.08$ m
Angular frequency $\omega = 3\pi$ rad s⁻¹

**Step 2: Differentiate to find velocity**
$$v = \frac{dx}{dt} = -0.08 \times 3\pi \times \sin(3\pi t)$$
$$v = -0.24\pi \sin(3\pi t) \text{ m s}^{-1}$$

Maximum velocity $v_{\text{max}} = 0.24\pi \approx 0.754 \text{ m s}^{-1}$

**Step 3: Find time for maximum velocity**
Maximum velocity occurs when $|\sin(3\pi t)| = 1$, i.e., $\sin(3\pi t) = \pm 1$
First maximum (positive) occurs when $3\pi t = \frac{\pi}{2}$
$$t = \frac{\pi/2}{3\pi} = \frac{1}{6} \text{ s}$$

### Final Answer / 最终答案
**Answer:** (a) $A = 0.08$ m, $\omega = 3\pi$ rad s⁻¹ (b) $v = -0.24\pi \sin(3\pi t)$ m s⁻¹ (c) $t = \frac{1}{6}$ s
**答案:** (a) $A = 0.08$ m, $\omega = 3\pi$ rad s⁻¹ (b) $v = -0.24\pi \sin(3\pi t)$ m s⁻¹ (c) $t = \frac{1}{6}$ s

### Quick Tip / 提示
**English:** When using cosine for displacement, velocity becomes negative sine. The negative sign is important for determining direction.
**中文:** 当位移使用余弦函数时，速度变为负正弦函数。负号对于确定方向很重要。

---

# 7. Flashcards / 闪卡

**Flashcard 1:**
Q (EN): What is the relationship between acceleration and displacement in SHM?
Q (CN): 简谐运动中加速度和位移之间的关系是什么？
A (EN): $a = -\omega^2 x$ — acceleration is proportional to negative displacement.
A (CN): $a = -\omega^2 x$ — 加速度与位移的负值成正比。

**Flashcard 2:**
Q (EN): At what point in SHM is velocity maximum, and what is its value?
Q (CN): 在简谐运动中，速度在何处最大，其值是多少？
A (EN): At equilibrium ($x = 0$), $v_{\text{max}} = A\omega$.
A (CN): 在平衡位置 ($x = 0$)，$v_{\text{max}} = A\omega$。

**Flashcard 3:**
Q (EN): What is the phase difference between displacement and acceleration in SHM?
Q (CN): 简谐运动中位移和加速度之间的相位差是多少？
A (EN): $\pi$ radians (180°) — they are in anti-phase.
A (CN): $\pi$ 弧度（180°）— 它们反相。

**Flashcard 4:**
Q (EN): Write the velocity-displacement relationship for SHM.
Q (CN): 写出简谐运动的速度-位移关系。
A (EN): $v^2 = \omega^2(A^2 - x^2)$
A (CN): $v^2 = \omega^2(A^2 - x^2)$

**Flashcard 5:**
Q (EN): If displacement is given by $x = A\sin(\omega t)$, what is the velocity equation?
Q (CN): 如果位移由 $x = A\sin(\omega t)$ 给出，速度方程是什么？
A (EN): $v = A\omega\cos(\omega t)$ — velocity leads displacement by $\frac{\pi}{2}$.
A (CN): $v = A\omega\cos(\omega t)$ — 速度领先位移 $\frac{\pi}{2}$。

---

# 8. Metadata / 元数据

```yaml
title:
  en: "Displacement, Velocity and Acceleration in SHM"
  cn: "简谐运动中的位移、速度和加速度"
parent_topic: "Simple Harmonic Motion"
parent_hub: "[[Simple Harmonic Motion]]"
subject: Physics
syllabus:
  - CAIE 9702: 17.1 (a-d)
  - Edexcel IAL: WPH14 U4: 7.1-7.5
level: A2
node_type: leaf_concept
difficulty: intermediate
related_leaf_nodes:
  - "[[Conditions for SHM]]"
  - "[[The Simple Pendulum]]"
  - "[[Mass-Spring System]]"
  - "[[Energy in SHM]]"
prerequisites:
  - "[[Equations of Motion (SUVAT)]]"
  - "[[Angular Measures]]"
language: bilingual_en_cn