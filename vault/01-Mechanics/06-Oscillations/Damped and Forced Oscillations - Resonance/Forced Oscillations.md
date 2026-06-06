# 1. Overview / 概述

**English:**
Forced oscillations occur when an external, periodic driving force is applied to an oscillating system, causing it to vibrate at the **driving frequency** rather than its natural frequency. This sub-topic is central to understanding how energy is transferred into oscillatory systems and sets the foundation for [[Resonance and the Barton Pendulum]]. Unlike [[Free Oscillations]] (which are covered in [[Simple Harmonic Motion]]), forced oscillations involve continuous energy input from an external source, which can sustain or amplify motion even in the presence of damping. Understanding forced oscillations is crucial for A-Level Physics as it explains real-world phenomena such as machinery vibrations, musical instrument sustain, and structural responses to periodic forces.

**中文:**
受迫振动发生在外部周期性驱动力施加于振动系统时，迫使系统以**驱动频率**而非其固有频率振动。本子知识点是理解能量如何传递到振动系统的核心，并为[[共振与巴顿摆]]奠定基础。与[[自由振动]]（在[[简谐运动]]中涵盖）不同，受迫振动涉及来自外部源的持续能量输入，即使在阻尼存在的情况下也能维持或放大运动。理解受迫振动对A-Level物理至关重要，因为它解释了机械振动、乐器延音以及结构对周期性力的响应等现实世界现象。

---

# 2. Core Definition / 核心定义

| Term (EN/CN) | Definition (EN) | Definition (CN) |
| ------------ | --------------- | --------------- |
| **Forced Oscillation** / 受迫振动 | An oscillation in which an external periodic driving force is applied to a system, causing it to oscillate at the driving frequency. | 外部周期性驱动力施加于系统，迫使系统以驱动频率振动的振动。 |
| **Driving Frequency** / 驱动频率 | The frequency of the external periodic force applied to the system. | 施加于系统的外部周期性力的频率。 |
| **Natural Frequency** / 固有频率 | The frequency at which a system oscillates freely when displaced from equilibrium and released, without any external driving force. | 系统在不受外部驱动力的情况下，从平衡位置被释放后自由振动的频率。 |
| **Steady State** / 稳态 | The condition reached after initial transients have died away, where the system oscillates at a constant amplitude at the driving frequency. | 初始瞬态消失后，系统以恒定振幅和驱动频率振动的状态。 |
| **Transient** / 瞬态 | The initial, temporary response of a system before it settles into steady-state oscillation. | 系统在进入稳态振动之前的初始、临时响应。 |
| **Amplitude of Forced Oscillation** / 受迫振动振幅 | The maximum displacement of the system from equilibrium during steady-state forced oscillation. | 稳态受迫振动期间系统从平衡位置的最大位移。 |

---

# 3. Key Concepts / 关键概念

**English:**

### How Forced Oscillations Work
When a periodic driving force is applied to an oscillating system, the system initially exhibits a **transient** response — a combination of its natural frequency and the driving frequency. Over time, damping causes the natural frequency component to decay, and the system settles into **steady-state** oscillation at the **driving frequency** only. The amplitude of this steady-state oscillation depends on:
1. The **driving frequency** relative to the system's **natural frequency**
2. The **magnitude** of the driving force
3. The **damping** present in the system (see [[Light, Critical and Heavy Damping]])

### Energy Transfer in Forced Oscillations
The driving force does **positive work** on the system, transferring energy into it. In steady state, the energy input per cycle equals the energy dissipated per cycle due to damping. This is analogous to pushing a child on a swing — you push at the right moment to transfer energy efficiently. The system's [[Energy in SHM]] concepts apply here, but with continuous energy input.

### Key Differences from Free Oscillations
- **Frequency**: Free oscillations occur at the natural frequency; forced oscillations occur at the driving frequency.
- **Amplitude**: Free oscillations have constant amplitude (undamped) or decaying amplitude (damped); forced oscillations can have constant amplitude in steady state.
- **Energy**: Free oscillations have no external energy input; forced oscillations have continuous external energy input.

### Common Pitfalls
- **Confusing driving frequency with natural frequency**: The system oscillates at the driving frequency, not its natural frequency, in steady state.
- **Assuming amplitude is constant regardless of driving frequency**: Amplitude varies significantly with driving frequency, especially near resonance.
- **Forgetting that transients exist**: Students often jump straight to steady-state analysis without considering initial behavior.

**中文:**

### 受迫振动的工作原理
当周期性驱动力施加于振动系统时，系统最初表现出**瞬态**响应——固有频率和驱动频率的组合。随着时间的推移，阻尼导致固有频率分量衰减，系统最终进入以**驱动频率**振动的**稳态**。稳态振幅取决于：
1. **驱动频率**相对于系统**固有频率**的关系
2. 驱动力的**大小**
3. 系统中存在的**阻尼**（参见[[轻阻尼、临界阻尼与重阻尼]]）

### 受迫振动中的能量传递
驱动力对系统做**正功**，将能量传递到系统中。在稳态下，每个周期的能量输入等于因阻尼而耗散的能量。这类似于推秋千上的孩子——在正确的时机推动以高效传递能量。系统的[[简谐运动中的能量]]概念在此适用，但具有持续的能量输入。

### 与自由振动的关键区别
- **频率**：自由振动以固有频率发生；受迫振动以驱动频率发生。
- **振幅**：自由振动具有恒定振幅（无阻尼）或衰减振幅（有阻尼）；受迫振动在稳态下可具有恒定振幅。
- **能量**：自由振动无外部能量输入；受迫振动有持续的外部能量输入。

### 常见误区
- **混淆驱动频率与固有频率**：系统在稳态下以驱动频率振动，而非固有频率。
- **假设振幅与驱动频率无关**：振幅随驱动频率显著变化，尤其在共振附近。
- **忽略瞬态的存在**：学生常直接跳到稳态分析，而不考虑初始行为。

---

# 4. Formulas / 公式

The key formula for forced oscillations relates the amplitude of the forced oscillation to the driving frequency and damping:

$$ A = \frac{F_0 / m}{\sqrt{(\omega_0^2 - \omega^2)^2 + (b\omega / m)^2}} $$

Where:
- $A$ = amplitude of forced oscillation (m)
- $F_0$ = amplitude of driving force (N)
- $m$ = mass of oscillating object (kg)
- $\omega_0$ = natural angular frequency (rad/s)
- $\omega$ = driving angular frequency (rad/s)
- $b$ = damping coefficient (kg/s)

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
| ------------- | ------------ | ------------ | ----------- |
| $A$ | Amplitude of forced oscillation | 受迫振动振幅 | m |
| $F_0$ | Driving force amplitude | 驱动力振幅 | N |
| $m$ | Mass | 质量 | kg |
| $\omega_0$ | Natural angular frequency | 固有角频率 | rad/s |
| $\omega$ | Driving angular frequency | 驱动角频率 | rad/s |
| $b$ | Damping coefficient | 阻尼系数 | kg/s |

**Derivation / 推导:**
Starting from the equation of motion for a damped, driven oscillator:
$$ m\frac{d^2x}{dt^2} + b\frac{dx}{dt} + kx = F_0 \cos(\omega t) $$

Assume a steady-state solution of the form $x = A\cos(\omega t - \phi)$. Substituting and solving for $A$ yields the amplitude formula above. The phase difference $\phi$ is given by:
$$ \tan\phi = \frac{b\omega}{m(\omega_0^2 - \omega^2)} $$

**Conditions / 适用条件:**
- The system must be linear (Hooke's law applies)
- The driving force must be sinusoidal
- Valid only for steady-state (after transients have decayed)
- Damping must be present for steady-state amplitude to be finite at resonance

> 📷 **IMAGE PROMPT — FOSC-01: Forced Oscillation Amplitude vs Driving Frequency**
>
> **English Prompt:**
> A clean, textbook-style vector graph showing amplitude of forced oscillation (y-axis) against driving frequency (x-axis). Three curves are plotted for different damping levels: low damping (tall, narrow peak), medium damping (shorter, wider peak), and high damping (flat, low curve). The natural frequency is marked with a vertical dashed line at f₀. The x-axis is labeled "Driving Frequency / Hz" and y-axis "Amplitude / m". Use a white background with black axes and colored curves (blue for low damping, red for medium, green for high). Include a legend in the top right corner.
>
> **中文描述:**
> 一个干净、教科书风格的矢量图，显示受迫振动振幅（y轴）与驱动频率（x轴）的关系。绘制三条不同阻尼水平的曲线：低阻尼（高而窄的峰值）、中阻尼（较短、较宽的峰值）和高阻尼（平坦、低曲线）。固有频率用垂直虚线标记在f₀处。x轴标记为"驱动频率/Hz"，y轴标记为"振幅/m"。使用白色背景、黑色坐标轴和彩色曲线（蓝色为低阻尼，红色为中阻尼，绿色为高阻尼）。右上角包含图例。
>
> **Labels Required / 需要标注:**
> * f₀ (natural frequency)
> * Low damping curve
> * Medium damping curve
> * High damping curve
> * Axes labels
>
> **Style / 风格:** Textbook vector
>
> **Exam Relevance / 考试关联:**
> This graph is essential for understanding how amplitude varies with driving frequency and damping — a common exam question topic.

---

# 5. Image Prompt / 图片提示

> 📷 **IMAGE PROMPT — FOSC-02: Forced Oscillation Phase Difference Diagram**
>
> **English Prompt:**
> A 3D-rendered diagram showing a mass-spring system being driven by an external periodic force. The mass (a blue block) is attached to a spring (coiled, silver) on the left, and a hand or mechanical arm (shown in orange) is pushing the mass from the right with a sinusoidal motion. Arrows indicate the direction of the driving force (F_drive) and the displacement (x). Below the system, two sine waves are shown: one for the driving force (orange) and one for the displacement (blue), with a phase difference φ marked between them. The phase difference should be less than 90° (driving force leading displacement). Use a clean, educational style with a white background and clear labels.
>
> **中文描述:**
> 一个3D渲染图，显示一个由外部周期性力驱动的质量-弹簧系统。质量块（蓝色方块）连接到左侧的弹簧（银色螺旋），一只手或机械臂（橙色）从右侧以正弦运动推动质量块。箭头指示驱动力（F_drive）和位移（x）的方向。系统下方显示两个正弦波：一个用于驱动力（橙色），一个用于位移（蓝色），它们之间的相位差φ被标记。相位差应小于90°（驱动力领先位移）。使用干净的教育风格，白色背景和清晰的标签。
>
> **Labels Required / 需要标注:**
> * Mass (m)
> * Spring (k)
> * Driving force (F_drive)
> * Displacement (x)
> * Phase difference (φ)
> * Driving force sine wave
> * Displacement sine wave
>
> **Style / 风格:** 3D render
>
> **Exam Relevance / 考试关联:**
> Understanding phase difference in forced oscillations is key to explaining energy transfer and resonance behavior.

---

# 6. Worked Example / 典型例题

### Question / 题目
**English:**
A mass-spring system has a natural frequency of 2.0 Hz. It is driven by an external periodic force of amplitude 5.0 N. The mass is 0.50 kg and the damping coefficient is 0.20 kg/s.

(a) Calculate the amplitude of the forced oscillation when the driving frequency is 1.5 Hz.
(b) Explain why the amplitude would be larger if the driving frequency were 2.0 Hz.

**中文:**
一个质量-弹簧系统的固有频率为2.0 Hz。它受到振幅为5.0 N的外部周期性力的驱动。质量为0.50 kg，阻尼系数为0.20 kg/s。

(a) 计算驱动频率为1.5 Hz时受迫振动的振幅。
(b) 解释为什么如果驱动频率为2.0 Hz，振幅会更大。

### Solution / 解答

**Part (a):**

First, convert frequencies to angular frequencies:
$$ \omega_0 = 2\pi f_0 = 2\pi \times 2.0 = 4\pi \text{ rad/s} $$
$$ \omega = 2\pi f = 2\pi \times 1.5 = 3\pi \text{ rad/s} $$

Use the amplitude formula:
$$ A = \frac{F_0 / m}{\sqrt{(\omega_0^2 - \omega^2)^2 + (b\omega / m)^2}} $$

Substitute values:
$$ A = \frac{5.0 / 0.50}{\sqrt{((4\pi)^2 - (3\pi)^2)^2 + (0.20 \times 3\pi / 0.50)^2}} $$

$$ A = \frac{10}{\sqrt{((16\pi^2 - 9\pi^2)^2 + (0.60\pi)^2}} $$

$$ A = \frac{10}{\sqrt{(7\pi^2)^2 + (0.60\pi)^2}} $$

$$ A = \frac{10}{\sqrt{(7 \times 9.87)^2 + (1.88)^2}} $$

$$ A = \frac{10}{\sqrt{(69.1)^2 + 3.54}} $$

$$ A = \frac{10}{\sqrt{4775 + 3.54}} = \frac{10}{\sqrt{4779}} $$

$$ A = \frac{10}{69.1} = 0.145 \text{ m} $$

**Part (b):**
At the natural frequency (2.0 Hz), $\omega = \omega_0$, so the term $(\omega_0^2 - \omega^2)^2$ becomes zero. The denominator is then minimized, consisting only of the damping term $(b\omega/m)^2$. This results in the maximum possible amplitude for the given damping — this is the condition for **resonance** (see [[Resonance and the Barton Pendulum]]). Therefore, the amplitude at 2.0 Hz would be larger than at 1.5 Hz.

### Final Answer / 最终答案
**Answer:** (a) 0.145 m (b) At resonance, the denominator is minimized, giving maximum amplitude. **答案:** (a) 0.145 米 (b) 在共振时，分母最小化，得到最大振幅。

### Quick Tip / 提示
**English:** Always convert frequency to angular frequency ($\omega = 2\pi f$) before using the amplitude formula. Remember that at resonance ($\omega = \omega_0$), the amplitude is limited only by damping.

**中文:** 在使用振幅公式前，务必先将频率转换为角频率（$\omega = 2\pi f$）。记住在共振时（$\omega = \omega_0$），振幅仅受阻尼限制。

---

# 7. Flashcards / 闪卡

**Flashcard 1:**
Q (EN): What is a forced oscillation?
Q (CN): 什么是受迫振动？
A (EN): An oscillation where an external periodic driving force causes the system to oscillate at the driving frequency.
A (CN): 外部周期性驱动力迫使系统以驱动频率振动的振动。

**Flashcard 2:**
Q (EN): What frequency does a forced oscillator oscillate at in steady state?
Q (CN): 受迫振子在稳态下以什么频率振动？
A (EN): The driving frequency, not the natural frequency.
A (CN): 驱动频率，而非固有频率。

**Flashcard 3:**
Q (EN): What happens to the transient response in a forced oscillation?
Q (CN): 受迫振动中的瞬态响应会发生什么？
A (EN): It decays due to damping, leaving only the steady-state oscillation at the driving frequency.
A (CN): 它因阻尼而衰减，只留下以驱动频率振动的稳态。

**Flashcard 4:**
Q (EN): How does the amplitude of forced oscillation depend on driving frequency?
Q (CN): 受迫振动的振幅如何依赖于驱动频率？
A (EN): Amplitude is maximum when driving frequency equals natural frequency (resonance), and decreases as driving frequency moves away from natural frequency.
A (CN): 当驱动频率等于固有频率（共振）时振幅最大，随着驱动频率远离固有频率而减小。

**Flashcard 5:**
Q (EN): What is the condition for steady-state in forced oscillations?
Q (CN): 受迫振动中稳态的条件是什么？
A (EN): Energy input per cycle from the driving force equals energy dissipated per cycle due to damping.
A (CN): 每个周期驱动力输入的能量等于每个周期因阻尼而耗散的能量。

---

# 8. Metadata / 元数据

```yaml
title:
  en: Forced Oscillations
  cn: 受迫振动
parent_topic: Damped and Forced Oscillations / Resonance
parent_hub: "[[Damped and Forced Oscillations / Resonance]]"
subject: Physics
syllabus:
  - CAIE 9702
  - Edexcel IAL
level: A2
node_type: leaf_concept
difficulty: advanced
related_leaf_nodes:
  - "[[Light, Critical and Heavy Damping]]"
  - "[[Resonance and the Barton Pendulum]]"
  - "[[Energy in SHM]]"
language: bilingual_en_cn