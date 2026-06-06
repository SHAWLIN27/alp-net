# 1. Overview / 概述

**English:**
The mass-spring system is one of the two classic examples of Simple Harmonic Motion (SHM) studied at A-Level, alongside the [[The Simple Pendulum]]. This sub-topic focuses on a mass attached to a spring that obeys Hooke's Law, oscillating horizontally on a frictionless surface or vertically under gravity. Understanding this system is crucial because it provides a clean, mathematical model for SHM where the restoring force is directly proportional to displacement. The mass-spring system is the foundation for understanding [[Energy in SHM]], as it clearly demonstrates the continuous exchange between kinetic and elastic potential energy. It also introduces the concept of angular frequency ($\omega$) in terms of the system's physical properties — mass ($m$) and spring constant ($k$) — which is a key distinction from the [[The Simple Pendulum]].

**中文:**
质量-弹簧系统是A-Level学习的两个经典简谐运动（SHM）例子之一，与[[The Simple Pendulum]]并列。本子知识点研究一个遵循胡克定律的弹簧上连接的质量块，在无摩擦水平面上或重力作用下垂直振荡。理解这个系统至关重要，因为它提供了一个清晰的SHM数学模型，其中恢复力与位移成正比。质量-弹簧系统是理解[[Energy in SHM]]的基础，因为它清楚地展示了动能和弹性势能之间的持续转换。它还引入了用系统物理属性（质量$m$和弹簧常数$k$）表示的角频率（$\omega$）概念，这是与[[The Simple Pendulum]]的关键区别。

---

# 2. Core Definition / 核心定义

| Term (EN/CN) | Definition (EN) | Definition (CN) |
| ------------ | --------------- | --------------- |
| **Mass-Spring System** / 质量-弹簧系统 | A system consisting of a mass attached to a spring that obeys Hooke's Law, where the restoring force is proportional to the displacement from equilibrium, leading to SHM. | 一个由连接在遵循胡克定律的弹簧上的质量块组成的系统，其中恢复力与距平衡位置的位移成正比，从而产生简谐运动。 |
| **Spring Constant ($k$)** / 弹簧常数 | A measure of the stiffness of a spring, defined as the force required per unit extension or compression. | 弹簧刚度的度量，定义为单位伸长或压缩所需的力。 |
| **Equilibrium Position** / 平衡位置 | The position where the net force on the mass is zero; for a horizontal system, this is the natural length of the spring; for a vertical system, it is where the spring force balances weight. | 质量块所受合力为零的位置；对于水平系统，这是弹簧的自然长度；对于垂直系统，这是弹簧力平衡重力的位置。 |
| **Restoring Force** / 恢复力 | The force that acts to return the mass to its equilibrium position; in a mass-spring system, $F = -kx$. | 使质量块返回平衡位置的力；在质量-弹簧系统中，$F = -kx$。 |
| **Angular Frequency ($\omega$)** / 角频率 | The rate of change of angular displacement in SHM, related to the period by $\omega = 2\pi/T$; for a mass-spring system, $\omega = \sqrt{k/m}$. | 简谐运动中角位移的变化率，与周期的关系为$\omega = 2\pi/T$；对于质量-弹簧系统，$\omega = \sqrt{k/m}$。 |
| **Natural Frequency ($f_0$)** / 固有频率 | The frequency at which a system oscillates when not subjected to a continuous or repeated external force; for a mass-spring system, $f_0 = \frac{1}{2\pi}\sqrt{k/m}$. | 系统在不受连续或重复外力作用时振荡的频率；对于质量-弹簧系统，$f_0 = \frac{1}{2\pi}\sqrt{k/m}$。 |

---

# 3. Key Concepts / 关键概念

**English:**

### The Restoring Force and Hooke's Law
The fundamental principle behind the mass-spring system is **Hooke's Law**, which states that the force exerted by a spring is proportional to its extension or compression from its natural length:
$$ F = -kx $$
where $k$ is the spring constant and $x$ is the displacement from equilibrium. The negative sign indicates that the force is always directed **towards** the equilibrium position — this is the restoring force.

### Why It Exhibits SHM
For SHM, we need two conditions (see [[Conditions for SHM]]):
1. The acceleration is proportional to the displacement ($a \propto -x$)
2. The acceleration is directed towards the equilibrium position

From Newton's Second Law: $F = ma = -kx$
Therefore: $a = -\frac{k}{m}x$

Since $k$ and $m$ are constants, $a \propto -x$, satisfying both conditions. The constant of proportionality gives us the angular frequency:
$$ \omega^2 = \frac{k}{m} $$

### Horizontal vs. Vertical Mass-Spring Systems
**Horizontal System:** The equilibrium position is at the spring's natural length. Gravity is perpendicular to motion and does not affect the oscillation.

**Vertical System:** The equilibrium position is **not** at the natural length — the spring stretches by $\Delta x = mg/k$ to balance weight. However, if you measure displacement from this new equilibrium, the same SHM equations apply with the same $\omega = \sqrt{k/m}$. Gravity simply shifts the equilibrium point but does not change the frequency.

### Common Pitfalls
- **Confusing extension with displacement:** In a vertical system, the total extension is $x_{eq} + x$, but the restoring force depends only on the displacement $x$ from the equilibrium position.
- **Forgetting the negative sign:** The restoring force always opposes displacement.
- **Assuming frequency depends on amplitude:** For an ideal spring obeying Hooke's Law, the frequency is independent of amplitude (isochronous oscillation).

**中文:**

### 恢复力和胡克定律
质量-弹簧系统的基本原理是**胡克定律**，它指出弹簧施加的力与其从自然长度的伸长或压缩成正比：
$$ F = -kx $$
其中$k$是弹簧常数，$x$是距平衡位置的位移。负号表示力始终指向平衡位置——这就是恢复力。

### 为什么它表现出简谐运动
简谐运动需要两个条件（参见[[Conditions for SHM]]）：
1. 加速度与位移成正比（$a \propto -x$）
2. 加速度指向平衡位置

根据牛顿第二定律：$F = ma = -kx$
因此：$a = -\frac{k}{m}x$

由于$k$和$m$是常数，$a \propto -x$，满足两个条件。比例常数给出了角频率：
$$ \omega^2 = \frac{k}{m} $$

### 水平与垂直质量-弹簧系统
**水平系统：** 平衡位置在弹簧的自然长度处。重力垂直于运动方向，不影响振荡。

**垂直系统：** 平衡位置**不在**自然长度处——弹簧会伸长$\Delta x = mg/k$以平衡重力。但是，如果从这个新平衡位置测量位移，相同的SHM方程适用，且$\omega = \sqrt{k/m}$相同。重力只是移动了平衡点，但不会改变频率。

### 常见错误
- **混淆伸长和位移：** 在垂直系统中，总伸长是$x_{eq} + x$，但恢复力只取决于距平衡位置的位移$x$。
- **忘记负号：** 恢复力始终与位移方向相反。
- **假设频率取决于振幅：** 对于遵循胡克定律的理想弹簧，频率与振幅无关（等时振荡）。

---

# 4. Formulas / 公式

## Formula 1: Restoring Force / 恢复力公式

$$ F = -kx $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
| ------------- | ------------ | ------------ | ----------- |
| $F$ | Restoring force | 恢复力 | N |
| $k$ | Spring constant | 弹簧常数 | N/m |
| $x$ | Displacement from equilibrium | 距平衡位置的位移 | m |

## Formula 2: Angular Frequency / 角频率公式

$$ \omega = \sqrt{\frac{k}{m}} $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
| ------------- | ------------ | ------------ | ----------- |
| $\omega$ | Angular frequency | 角频率 | rad/s |
| $k$ | Spring constant | 弹簧常数 | N/m |
| $m$ | Mass | 质量 | kg |

## Formula 3: Period of Oscillation / 振荡周期公式

$$ T = 2\pi\sqrt{\frac{m}{k}} $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
| ------------- | ------------ | ------------ | ----------- |
| $T$ | Period | 周期 | s |
| $m$ | Mass | 质量 | kg |
| $k$ | Spring constant | 弹簧常数 | N/m |

## Formula 4: Frequency / 频率公式

$$ f = \frac{1}{T} = \frac{1}{2\pi}\sqrt{\frac{k}{m}} $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
| ------------- | ------------ | ------------ | ----------- |
| $f$ | Frequency | 频率 | Hz |

**Derivation / 推导:**
From $F = ma = -kx$, we get $a = -\frac{k}{m}x$. Comparing with the SHM condition $a = -\omega^2 x$, we identify $\omega^2 = \frac{k}{m}$, so $\omega = \sqrt{k/m}$. Since $T = 2\pi/\omega$, we get $T = 2\pi\sqrt{m/k}$.

**Conditions / 适用条件:**
- Spring obeys Hooke's Law (elastic limit not exceeded)
- No damping (frictionless surface or negligible air resistance)
- Small oscillations (for ideal spring, amplitude-independent)

> 📷 **IMAGE PROMPT — MSS-01: Mass-Spring System Diagram**
>
> **English Prompt:**
> A clean, textbook-style vector diagram showing a horizontal mass-spring system. A block of mass m sits on a frictionless surface, attached to a spring on the left wall. The equilibrium position is marked with a dashed vertical line labeled "x=0". The block is shown displaced to the right by distance x, with an arrow labeled "F = -kx" pointing left towards equilibrium. Labels: "Spring constant k", "Mass m", "Displacement x". Clean white background, professional physics textbook style, blue and black lines, sans-serif font.
>
> **中文描述:**
> 一个清晰、教科书风格的矢量图，显示水平质量-弹簧系统。一个质量为m的块体位于无摩擦表面上，连接到左侧墙壁的弹簧上。平衡位置用虚线垂直线标记，标注"x=0"。块体显示向右位移距离x，有一个箭头标注"F = -kx"指向左侧朝向平衡位置。标签："弹簧常数k"、"质量m"、"位移x"。干净的白色背景，专业物理教科书风格，蓝色和黑色线条，无衬线字体。
>
> **Labels Required / 需要标注:**
> * Spring constant $k$
> * Mass $m$
> * Displacement $x$
> * Restoring force $F = -kx$
> * Equilibrium position $x = 0$
>
> **Style / 风格:** Textbook vector diagram
>
> **Exam Relevance / 考试关联:**
> This diagram is essential for understanding the restoring force concept and is frequently used in exam questions to set up the problem.

---

# 5. Image Prompt / 图片提示

> 📷 **IMAGE PROMPT — MSS-02: Vertical Mass-Spring System**
>
> **English Prompt:**
> A detailed 3D-rendered diagram of a vertical mass-spring system. A spring hangs from a fixed support at the top. A mass m is attached to the bottom. Three positions are shown: (1) The natural length of the spring (no mass) shown as a faint ghost spring, (2) The equilibrium position with the mass hanging stationary, marked with a dashed line labeled "Equilibrium", showing extension Δx = mg/k, (3) The mass pulled down further by amplitude A, with arrows showing the restoring force upward. Labels: "Natural length", "Equilibrium (x=0)", "Amplitude A", "Extension Δx = mg/k". Soft blue gradient background, realistic spring coils, professional 3D render style.
>
> **中文描述:**
> 一个详细的3D渲染图，显示垂直质量-弹簧系统。一个弹簧从顶部的固定支架悬挂下来。一个质量为m的块体连接在底部。显示三个位置：(1)弹簧的自然长度（无质量）显示为淡色幽灵弹簧，(2)质量块静止悬挂时的平衡位置，用虚线标记标注"平衡"，显示伸长Δx = mg/k，(3)质量块被进一步向下拉振幅A，箭头显示向上的恢复力。标签："自然长度"、"平衡位置(x=0)"、"振幅A"、"伸长Δx = mg/k"。柔和的蓝色渐变背景，逼真的弹簧线圈，专业3D渲染风格。
>
> **Labels Required / 需要标注:**
> * Natural length
> * Equilibrium position
> * Extension at equilibrium $\Delta x = mg/k$
> * Amplitude $A$
> * Restoring force direction
>
> **Style / 风格:** 3D render
>
> **Exam Relevance / 考试关联:**
> Vertical mass-spring systems are common in exam questions. Understanding that gravity shifts the equilibrium but doesn't change the frequency is a key exam concept.

---

# 6. Worked Example / 典型例题

### Example 1: Finding Period and Frequency / 例题1：求周期和频率

### Question / 题目
**English:**
A mass of 0.50 kg is attached to a spring with spring constant $k = 80 \text{ N/m}$. The mass is displaced 0.10 m from equilibrium and released on a frictionless horizontal surface. Calculate:
(a) The angular frequency of oscillation
(b) The period of oscillation
(c) The frequency of oscillation

**中文:**
一个0.50 kg的质量块连接到弹簧常数为$k = 80 \text{ N/m}$的弹簧上。质量块从平衡位置位移0.10 m后，在无摩擦水平面上释放。计算：
(a) 振荡的角频率
(b) 振荡的周期
(c) 振荡的频率

### Solution / 解答

**(a) Angular frequency / 角频率:**
$$ \omega = \sqrt{\frac{k}{m}} = \sqrt{\frac{80}{0.50}} = \sqrt{160} = 12.65 \text{ rad/s} $$

**(b) Period / 周期:**
$$ T = \frac{2\pi}{\omega} = \frac{2\pi}{12.65} = 0.497 \text{ s} $$
Alternatively: $T = 2\pi\sqrt{\frac{m}{k}} = 2\pi\sqrt{\frac{0.50}{80}} = 2\pi\sqrt{0.00625} = 2\pi(0.0791) = 0.497 \text{ s}$

**(c) Frequency / 频率:**
$$ f = \frac{1}{T} = \frac{1}{0.497} = 2.01 \text{ Hz} $$
Alternatively: $f = \frac{1}{2\pi}\sqrt{\frac{k}{m}} = \frac{1}{2\pi}\sqrt{160} = \frac{12.65}{6.283} = 2.01 \text{ Hz}$

### Final Answer / 最终答案
**Answer:** (a) $\omega = 12.7 \text{ rad/s}$, (b) $T = 0.497 \text{ s}$, (c) $f = 2.01 \text{ Hz}$
**答案:** (a) $\omega = 12.7 \text{ rad/s}$，(b) $T = 0.497 \text{ s}$，(c) $f = 2.01 \text{ Hz}$

### Quick Tip / 提示
Notice that the amplitude (0.10 m) was **not needed** to calculate the period or frequency. For an ideal mass-spring system, the period is independent of amplitude. This is a common exam trick — don't be fooled into using amplitude in period calculations!

注意振幅（0.10 m）**不需要**用来计算周期或频率。对于理想的质量-弹簧系统，周期与振幅无关。这是一个常见的考试陷阱——不要被误导在周期计算中使用振幅！

---

### Example 2: Vertical Mass-Spring System / 例题2：垂直质量-弹簧系统

### Question / 题目
**English:**
A 0.20 kg mass is hung from a vertical spring of spring constant $k = 50 \text{ N/m}$. The mass is pulled down an additional 0.050 m from its equilibrium position and released.
(a) Calculate the period of oscillation.
(b) Calculate the maximum acceleration of the mass.
(c) State how the period would change if the experiment were performed on the Moon (where $g = 1.62 \text{ m/s}^2$).

**中文:**
一个0.20 kg的质量块挂在弹簧常数为$k = 50 \text{ N/m}$的垂直弹簧上。质量块从其平衡位置再向下拉0.050 m后释放。
(a) 计算振荡周期。
(b) 计算质量块的最大加速度。
(c) 说明如果在月球上进行实验（$g = 1.62 \text{ m/s}^2$），周期会如何变化。

### Solution / 解答

**(a) Period / 周期:**
$$ T = 2\pi\sqrt{\frac{m}{k}} = 2\pi\sqrt{\frac{0.20}{50}} = 2\pi\sqrt{0.004} = 2\pi(0.0632) = 0.397 \text{ s} $$

**(b) Maximum acceleration / 最大加速度:**
In SHM, $a_{\text{max}} = \omega^2 A$
$$ \omega = \sqrt{\frac{k}{m}} = \sqrt{\frac{50}{0.20}} = \sqrt{250} = 15.81 \text{ rad/s} $$
$$ a_{\text{max}} = \omega^2 A = (15.81)^2 \times 0.050 = 250 \times 0.050 = 12.5 \text{ m/s}^2 $$

**(c) On the Moon / 在月球上:**
The period would **remain the same**. The period depends only on $m$ and $k$, not on $g$. Gravity only shifts the equilibrium position but does not affect the oscillation frequency.

周期**保持不变**。周期只取决于$m$和$k$，与$g$无关。重力只移动平衡位置，但不影响振荡频率。

### Final Answer / 最终答案
**Answer:** (a) $T = 0.397 \text{ s}$, (b) $a_{\text{max}} = 12.5 \text{ m/s}^2$, (c) Period unchanged
**答案:** (a) $T = 0.397 \text{ s}$，(b) $a_{\text{max}} = 12.5 \text{ m/s}^2$，(c) 周期不变

### Quick Tip / 提示
For vertical mass-spring systems, always remember: **$g$ does not appear in the period formula!** The equilibrium extension $\Delta x = mg/k$ tells you where the mass hangs, but the oscillation frequency is the same as if it were horizontal.

对于垂直质量-弹簧系统，始终记住：**$g$不会出现在周期公式中！** 平衡伸长$\Delta x = mg/k$告诉你质量块悬挂的位置，但振荡频率与水平系统相同。

---

# 7. Flashcards / 闪卡

**Flashcard 1:**
Q (EN): What is the condition for a mass-spring system to exhibit SHM?
Q (CN): 质量-弹簧系统表现出简谐运动的条件是什么？
A (EN): The spring must obey Hooke's Law ($F = -kx$), and there must be no damping. The restoring force must be proportional to displacement and directed towards equilibrium.
A (CN): 弹簧必须遵循胡克定律（$F = -kx$），且必须无阻尼。恢复力必须与位移成正比并指向平衡位置。

**Flashcard 2:**
Q (EN): What is the formula for the period of a mass-spring system?
Q (CN): 质量-弹簧系统的周期公式是什么？
A (EN): $T = 2\pi\sqrt{m/k}$, where $m$ is the mass and $k$ is the spring constant.
A (CN): $T = 2\pi\sqrt{m/k}$，其中$m$是质量，$k$是弹簧常数。

**Flashcard 3:**
Q (EN): How does gravity affect the oscillation of a vertical mass-spring system?
Q (CN): 重力如何影响垂直质量-弹簧系统的振荡？
A (EN): Gravity shifts the equilibrium position but does NOT affect the period or frequency. The period depends only on $m$ and $k$.
A (CN): 重力移动平衡位置，但**不**影响周期或频率。周期只取决于$m$和$k$。

**Flashcard 4:**
Q (EN): What happens to the period if the amplitude of a mass-spring system is doubled?
Q (CN): 如果质量-弹簧系统的振幅加倍，周期会发生什么变化？
A (EN): The period remains unchanged. For an ideal spring obeying Hooke's Law, the period is independent of amplitude (isochronous oscillation).
A (CN): 周期保持不变。对于遵循胡克定律的理想弹簧，周期与振幅无关（等时振荡）。

**Flashcard 5:**
Q (EN): A mass-spring system has period $T$. If the mass is quadrupled, what is the new period?
Q (CN): 一个质量-弹簧系统的周期为$T$。如果质量变为四倍，新周期是多少？
A (EN): $T_{\text{new}} = 2T$. Since $T \propto \sqrt{m}$, quadrupling $m$ doubles $T$.
A (CN): $T_{\text{new}} = 2T$。由于$T \propto \sqrt{m}$，质量变为四倍使周期加倍。

---

# 8. Metadata / 元数据

```yaml
title:
  en: Mass-Spring System
  cn: 质量-弹簧系统
parent_topic: Simple Harmonic Motion
parent_hub: "[[Simple Harmonic Motion]]"
subject: Physics
syllabus:
  - CAIE 9702 (17.1 a-d)
  - Edexcel IAL (WPH14 U4: 7.1-7.5)
level: A2
node_type: leaf_concept
difficulty: intermediate
related_leaf_nodes:
  - "[[Conditions for SHM]]"
  - "[[Displacement, Velocity and Acceleration in SHM]]"
  - "[[The Simple Pendulum]]"
  - "[[Energy in SHM]]"
prerequisites:
  - "[[Equations of Motion (SUVAT)]]"
  - "[[Angular Measures]]"
language: bilingual_en_cn