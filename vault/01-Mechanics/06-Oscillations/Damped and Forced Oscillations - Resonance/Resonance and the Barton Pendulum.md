# 1. Overview / 概述

**English:**
Resonance is one of the most dramatic and practically important phenomena in physics. This sub-topic explores the precise condition for resonance — when the driving frequency equals the natural frequency of a system — and the characteristic "resonance peak" in amplitude-frequency graphs. The **Barton pendulum** is the classic demonstration apparatus used to visualise resonance, showing how a driven pendulum responds most strongly when its natural frequency matches the driver. Understanding resonance is essential for explaining everything from bridge collapses and opera singers shattering glass to tuning a radio and designing earthquake-resistant buildings. This sub-topic builds directly on [[Forced Oscillations]] and [[Light, Critical and Heavy Damping]], and requires a solid grasp of [[Energy in SHM]].

**中文:**
共振是物理学中最引人注目且具有重要实际意义的现象之一。本子知识点探讨共振的精确条件——当驱动力频率等于系统的固有频率时——以及幅频图中特征性的"共振峰"。**巴顿摆**是用于可视化共振的经典演示装置，展示了受迫摆在其固有频率与驱动频率匹配时如何产生最强响应。理解共振对于解释从桥梁倒塌、歌剧歌手震碎玻璃到调谐收音机和设计抗震建筑等一切现象都至关重要。本子知识点直接建立在[[Forced Oscillations]]和[[Light, Critical and Heavy Damping]]的基础上，并需要扎实掌握[[Energy in SHM]]。

---

# 2. Core Definition / 核心定义

| Term (EN/CN) | Definition (EN) | Definition (CN) |
| ------------ | --------------- | --------------- |
| **Resonance** / 共振 | The phenomenon where a driven oscillating system experiences maximum amplitude when the driving frequency equals the natural frequency of the system. | 当驱动力频率等于系统固有频率时，受迫振动系统经历最大振幅的现象。 |
| **Natural Frequency** / 固有频率 | The frequency at which a system oscillates freely when displaced from equilibrium and released, with no external driving force. | 系统在不受外力驱动、从平衡位置释放后自由振动的频率。 |
| **Driving Frequency** / 驱动频率 | The frequency of the external periodic force applied to a system. | 施加在系统上的外部周期性力的频率。 |
| **Resonance Peak** / 共振峰 | The sharp maximum in the amplitude-frequency graph that occurs at the natural frequency of the system. | 幅频图中在系统固有频率处出现的尖锐最大值。 |
| **Barton Pendulum** / 巴顿摆 | A demonstration apparatus consisting of a heavy driver pendulum and several lighter pendulums of different lengths, used to illustrate resonance. | 由重驱动摆和几个不同长度的轻摆组成的演示装置，用于说明共振现象。 |
| **Sharpness of Resonance** / 共振锐度 | A measure of how narrow the resonance peak is; related to the degree of damping in the system. | 衡量共振峰宽窄程度的指标；与系统的阻尼程度有关。 |

---

# 3. Key Concepts / 关键概念

**English:**

### The Resonance Condition
Resonance occurs when the driving frequency $f_d$ equals the natural frequency $f_0$ of the system. At this precise condition, the driving force is always in phase with the velocity of the oscillator, meaning energy is transferred most efficiently into the system. This leads to a maximum amplitude of oscillation.

### The Amplitude-Frequency Graph
The characteristic resonance curve shows:
- **At low driving frequencies** ($f_d \ll f_0$): The oscillator follows the driver almost in phase, with small amplitude.
- **At resonance** ($f_d = f_0$): Amplitude reaches a maximum. The phase difference between displacement and driving force is $90^\circ$ (the oscillator is in quadrature).
- **At high driving frequencies** ($f_d \gg f_0$): The oscillator cannot keep up; amplitude drops to near zero, and the phase difference approaches $180^\circ$.

### The Barton Pendulum
The Barton pendulum is a classic demonstration consisting of:
1. **A heavy driver pendulum** (large mass, driven by hand or motor) — this provides the forced oscillation.
2. **Several light pendulums** of different lengths suspended from the same string — these are the driven oscillators.

When the driver is set oscillating:
- The pendulum **with the same length** (and therefore the same natural frequency) as the driver resonates — it swings with the largest amplitude.
- Pendulums with **different lengths** (different natural frequencies) oscillate with much smaller amplitudes.
- This beautifully demonstrates that resonance is frequency-specific.

### Energy Transfer at Resonance
At resonance, the driving force does maximum positive work on the oscillator each cycle. The energy input per cycle equals the energy dissipated per cycle (due to damping), establishing a steady-state maximum amplitude. Without damping, the amplitude would theoretically increase without limit — this is why [[Light, Critical and Heavy Damping]] is crucial: damping controls the height and width of the resonance peak.

### Common Pitfalls
- **Confusing natural frequency with driving frequency**: The natural frequency is a property of the system; the driving frequency is external.
- **Thinking resonance only occurs at one exact frequency**: In lightly damped systems, the resonance peak is very sharp; in heavily damped systems, it is broad and may not even be noticeable.
- **Forgetting phase relationships**: At resonance, displacement lags the driving force by $90^\circ$, not $0^\circ$ or $180^\circ$.

**中文:**

### 共振条件
当驱动频率 $f_d$ 等于系统的固有频率 $f_0$ 时，发生共振。在这个精确条件下，驱动力始终与振荡器的速度同相，这意味着能量最有效地传递到系统中。这导致振荡幅度达到最大值。

### 幅频图
特征性的共振曲线显示：
- **在低驱动频率时** ($f_d \ll f_0$)：振荡器几乎与驱动器同相跟随，振幅较小。
- **在共振时** ($f_d = f_0$)：振幅达到最大值。位移与驱动力之间的相位差为 $90^\circ$（振荡器处于正交状态）。
- **在高驱动频率时** ($f_d \gg f_0$)：振荡器无法跟上；振幅降至接近零，相位差接近 $180^\circ$。

### 巴顿摆
巴顿摆是一个经典演示装置，包括：
1. **一个重驱动摆**（大质量，用手或马达驱动）——提供受迫振动。
2. **几个不同长度的轻摆**悬挂在同一根绳子上——这些是被驱动的振荡器。

当驱动摆开始振荡时：
- **与驱动器长度相同**（因此固有频率相同）的摆发生共振——它以最大振幅摆动。
- **不同长度**（不同固有频率）的摆以小得多的振幅振荡。
- 这很好地证明了共振是频率特异性的。

### 共振时的能量传递
在共振时，驱动力每个周期对振荡器做最大的正功。每个周期的能量输入等于每个周期耗散的能量（由于阻尼），从而建立稳态最大振幅。如果没有阻尼，振幅理论上会无限增加——这就是[[Light, Critical and Heavy Damping]]至关重要的原因：阻尼控制共振峰的高度和宽度。

### 常见误区
- **混淆固有频率和驱动频率**：固有频率是系统的属性；驱动频率是外部的。
- **认为共振只发生在一个精确频率**：在轻阻尼系统中，共振峰非常尖锐；在重阻尼系统中，共振峰很宽，甚至可能不明显。
- **忘记相位关系**：在共振时，位移滞后驱动力 $90^\circ$，而不是 $0^\circ$ 或 $180^\circ$。

---

# 4. Formulas / 公式

The key formula for resonance is the condition itself:

$$ f_d = f_0 $$

Where:
- $f_d$ = driving frequency (Hz)
- $f_0$ = natural frequency of the system (Hz)

For a simple pendulum, the natural frequency is:

$$ f_0 = \frac{1}{2\pi} \sqrt{\frac{g}{L}} $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
| ------------- | ------------ | ------------ | ----------- |
| $f_0$ | Natural frequency | 固有频率 | Hz |
| $g$ | Acceleration due to gravity | 重力加速度 | m s⁻² |
| $L$ | Length of pendulum | 摆长 | m |

**Derivation / 推导:**
The natural frequency of a simple pendulum comes from the restoring force $F = -mg\sin\theta \approx -mg\theta$ for small angles. Using $F = ma = mL\ddot{\theta}$, we get $\ddot{\theta} + \frac{g}{L}\theta = 0$, which is SHM with angular frequency $\omega_0 = \sqrt{g/L}$, so $f_0 = \omega_0/2\pi = \frac{1}{2\pi}\sqrt{g/L}$.

**Conditions / 适用条件:**
- Small angle approximation ($\theta < 10^\circ$)
- No damping (ideal case)
- For the Barton pendulum specifically: the driver must be significantly heavier than the driven pendulums

> 📷 **IMAGE PROMPT — RES-01: Resonance Amplitude-Frequency Graph**
>
> **English Prompt:**
> A clean, textbook-style vector graph showing amplitude (y-axis) against driving frequency (x-axis). Three curves on the same axes: one sharp, tall peak for light damping (blue), one medium peak for moderate damping (green), and one broad, low curve for heavy damping (red). All peaks occur at the same natural frequency f₀ on the x-axis. The y-axis is labelled "Amplitude" and x-axis "Driving Frequency". A vertical dashed line marks f₀. Clear gridlines and axis labels in a professional sans-serif font. White background, no shadows.
>
> **中文描述:**
> 一个干净的教科书式矢量图，显示振幅（y轴）与驱动频率（x轴）的关系。同一坐标轴上有三条曲线：轻阻尼（蓝色）的尖锐高峰，中等阻尼（绿色）的中等峰，重阻尼（红色）的宽而低的曲线。所有峰值都出现在x轴上的同一固有频率f₀处。y轴标记为"振幅"，x轴标记为"驱动频率"。一条垂直虚线标记f₀。清晰的网格线和专业无衬线字体的轴标签。白色背景，无阴影。
>
> **Labels Required / 需要标注:**
> * f₀ (natural frequency)
> * Light damping / 轻阻尼
> * Moderate damping / 中等阻尼
> * Heavy damping / 重阻尼
>
> **Style / 风格:** Textbook vector
>
> **Exam Relevance / 考试关联:**
> This graph is the single most important diagram for resonance questions in A-Level exams. Students must be able to sketch it, interpret it, and explain how damping affects the peak.

---

# 5. Image Prompt / 图片提示

> 📷 **IMAGE PROMPT — RES-02: Barton Pendulum Setup**
>
> **English Prompt:**
> A clear 3D isometric diagram of a Barton pendulum apparatus. A horizontal string is stretched between two supports. From this string hangs: one heavy pendulum (large metal bob, thick string) on the left side, and five lighter pendulums (small plastic bobs, thin strings) of different lengths spaced evenly along the string. The driver pendulum is shown being pulled to one side with a small arrow indicating its motion. The pendulum with the same length as the driver is shown swinging with a large amplitude (indicated by a double-headed arrow showing its maximum displacement), while the others have much smaller amplitudes. Labels point to: "Driver pendulum (heavy)", "Driven pendulums (light)", "Support string", "Resonating pendulum". Clean white background, professional physics textbook style.
>
> **中文描述:**
> 巴顿摆装置的清晰3D等轴测图。一根水平绳子拉紧在两个支架之间。从这根绳子上悬挂着：左侧一个重摆（大金属球，粗绳），以及沿绳子均匀分布的五个不同长度的轻摆（小塑料球，细绳）。驱动摆被拉到一侧，一个小箭头指示其运动。与驱动器长度相同的摆以大幅度摆动（双箭头指示其最大位移），而其他摆的振幅小得多。标签指向："驱动摆（重）"、"被驱动摆（轻）"、"支撑绳"、"共振摆"。干净的白色背景，专业物理教科书风格。
>
> **Labels Required / 需要标注:**
> * Driver pendulum (heavy) / 驱动摆（重）
> * Driven pendulums (light) / 被驱动摆（轻）
> * Support string / 支撑绳
> * Resonating pendulum / 共振摆
>
> **Style / 风格:** 3D isometric, textbook vector
>
> **Exam Relevance / 考试关联:**
> The Barton pendulum is a common exam context for explaining resonance. Students should be able to describe the setup, predict which pendulum resonates, and explain why.

---

# 6. Worked Example / 典型例题

### Example 1: Barton Pendulum Analysis

### Question / 题目
**English:**
A Barton pendulum has a driver pendulum of length 25 cm. Five driven pendulums have lengths: 15 cm, 20 cm, 25 cm, 30 cm, and 35 cm. The driver is set oscillating with a small amplitude at its natural frequency.

(a) Which driven pendulum will resonate? Explain your answer.
(b) Describe the motion of the other four pendulums.
(c) If the driver is now moved faster (higher frequency), what happens to the amplitude of the 25 cm pendulum?

**中文:**
一个巴顿摆的驱动摆长度为25厘米。五个被驱动摆的长度分别为：15厘米、20厘米、25厘米、30厘米和35厘米。驱动摆以其固有频率以小振幅开始振荡。

(a) 哪个被驱动摆会发生共振？解释你的答案。
(b) 描述其他四个摆的运动。
(c) 如果驱动摆现在移动得更快（更高频率），25厘米摆的振幅会发生什么变化？

### Solution / 解答

**(a)** The 25 cm pendulum will resonate because it has the same length (and therefore the same natural frequency) as the driver. When the driving frequency equals the natural frequency, resonance occurs, giving maximum amplitude.

**(b)** The other four pendulums will oscillate with much smaller amplitudes because their natural frequencies differ from the driving frequency. The 20 cm and 30 cm pendulums (closer in length) will have slightly larger amplitudes than the 15 cm and 35 cm pendulums (further from resonance).

**(c)** If the driver moves faster, the driving frequency increases above the natural frequency of the 25 cm pendulum. The amplitude of the 25 cm pendulum will decrease significantly because the system is no longer at resonance. The pendulum that now has the closest natural frequency to the new driving frequency will show the largest amplitude.

### Final Answer / 最终答案
**Answer:** (a) 25 cm pendulum; (b) Small amplitude oscillations, with 20 cm and 30 cm pendulums having slightly larger amplitudes than 15 cm and 35 cm; (c) Amplitude decreases. **答案:** (a) 25厘米摆；(b) 小振幅振荡，20厘米和30厘米摆的振幅略大于15厘米和35厘米摆；(c) 振幅减小。

### Quick Tip / 提示
In Barton pendulum questions, always identify which pendulum has the same length as the driver — that's the one that resonates. Remember that the natural frequency of a pendulum depends only on its length (for small angles), not on its mass.

---

# 7. Flashcards / 闪卡

**Flashcard 1:**
Q (EN): What is the condition for resonance?
Q (CN): 共振的条件是什么？
A (EN): The driving frequency equals the natural frequency of the system ($f_d = f_0$).
A (CN): 驱动频率等于系统的固有频率（$f_d = f_0$）。

**Flashcard 2:**
Q (EN): In a Barton pendulum, which pendulum resonates?
Q (CN): 在巴顿摆中，哪个摆会发生共振？
A (EN): The pendulum with the same length (and therefore same natural frequency) as the driver pendulum.
A (CN): 与驱动摆长度相同（因此固有频率相同）的摆。

**Flashcard 3:**
Q (EN): What is the phase relationship between displacement and driving force at resonance?
Q (CN): 在共振时，位移与驱动力之间的相位关系是什么？
A (EN): Displacement lags the driving force by 90° (quadrature).
A (CN): 位移滞后驱动力90°（正交）。

**Flashcard 4:**
Q (EN): How does damping affect the resonance peak?
Q (CN): 阻尼如何影响共振峰？
A (EN): Increased damping reduces the peak height and broadens the peak width. Light damping gives a tall, sharp peak; heavy damping gives a low, broad peak.
A (CN): 增加阻尼会降低峰高并加宽峰宽。轻阻尼产生高而尖锐的峰；重阻尼产生低而宽的峰。

**Flashcard 5:**
Q (EN): What happens to the amplitude of a driven oscillator when the driving frequency is much higher than the natural frequency?
Q (CN): 当驱动频率远高于固有频率时，受迫振荡器的振幅会发生什么变化？
A (EN): The amplitude becomes very small (approaches zero) because the oscillator cannot keep up with the rapid driving force.
A (CN): 振幅变得非常小（趋近于零），因为振荡器无法跟上快速的驱动力。

---

# 8. Metadata / 元数据

```yaml
title:
  en: Resonance and the Barton Pendulum
  cn: 共振与巴顿摆
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
  - "[[Forced Oscillations]]"
  - "[[Energy in SHM]]"
language: bilingual_en_cn