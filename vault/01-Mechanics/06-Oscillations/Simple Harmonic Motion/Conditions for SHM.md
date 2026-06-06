# 1. Overview / 概述

**English:**
This sub-topic establishes the fundamental criteria that define Simple Harmonic Motion (SHM). Understanding these conditions is essential because they allow us to identify whether any oscillating system — from a pendulum to a vibrating molecule — truly exhibits SHM. The conditions form the foundation for deriving all subsequent equations and analyzing real-world oscillators. Without meeting these criteria, an oscillation is not simple harmonic, and different mathematical tools must be used.

In the broader context of [[Simple Harmonic Motion]], this leaf node serves as the gateway concept. Before exploring [[Displacement, Velocity and Acceleration in SHM]] or specific systems like [[The Simple Pendulum]] and [[Mass-Spring System]], students must first understand what makes an oscillation "simple harmonic." The conditions also connect directly to [[Energy in SHM]], as the restoring force condition leads to energy conservation principles.

**中文:**
本子知识点建立了定义简谐运动（SHM）的基本标准。理解这些条件至关重要，因为它们使我们能够判断任何振荡系统——从摆锤到振动分子——是否真正表现出简谐运动。这些条件构成了推导所有后续方程和分析现实振荡器的基础。如果不满足这些标准，振荡就不是简谐的，必须使用不同的数学工具。

在[[Simple Harmonic Motion]]的更广泛背景下，本叶节点作为入门概念。在探索[[Displacement, Velocity and Acceleration in SHM]]或[[The Simple Pendulum]]和[[Mass-Spring System]]等特定系统之前，学生必须首先理解什么使振荡成为"简谐的"。这些条件也直接连接到[[Energy in SHM]]，因为恢复力条件导致了能量守恒原理。

---

# 2. Core Definition / 核心定义

| Term (EN/CN) | Definition (EN) | Definition (CN) |
| ------------ | --------------- | --------------- |
| **Simple Harmonic Motion (SHM)** / 简谐运动 | Oscillatory motion where the acceleration is directly proportional to the displacement from equilibrium and always directed towards the equilibrium position. | 加速度与偏离平衡位置的位移成正比，且始终指向平衡位置的振荡运动。 |
| **Restoring Force** / 恢复力 | The net force that acts to return the system to its equilibrium position, always opposing the displacement. | 使系统返回平衡位置的合力，始终与位移方向相反。 |
| **Equilibrium Position** / 平衡位置 | The point where the net force on the oscillating object is zero; the center of oscillation. | 振荡物体所受合力为零的点；振荡中心。 |
| **Displacement** / 位移 | The distance and direction of the oscillating object from its equilibrium position at any instant. | 振荡物体在任意时刻偏离平衡位置的距离和方向。 |
| **Amplitude** / 振幅 | The maximum displacement from the equilibrium position. | 偏离平衡位置的最大位移。 |
| **Proportionality Constant** / 比例常数 | The constant $k$ (or $\omega^2$) relating acceleration to displacement: $a = -\omega^2 x$ | 将加速度与位移联系起来的常数：$a = -\omega^2 x$ |

---

# 3. Key Concepts / 关键概念

**English:**
The conditions for SHM can be stated in two equivalent ways — one in terms of force, and one in terms of acceleration.

### Condition 1: Restoring Force Proportional to Displacement
For a system to exhibit SHM, the net force acting on the oscillating object must satisfy:
$$F = -kx$$
where $k$ is a positive constant (the force constant), and $x$ is the displacement from equilibrium. The negative sign indicates that the force always acts **towards** the equilibrium position — it is a **restoring force**.

This is analogous to [[Hooke's Law]] for springs, but applies more broadly to any system where the restoring force is linear with displacement.

### Condition 2: Acceleration Proportional to Negative Displacement
Using Newton's Second Law ($F = ma$), we can rewrite the force condition as:
$$a = -\frac{k}{m}x = -\omega^2 x$$
where $\omega = \sqrt{k/m}$ is the angular frequency. This is the **defining equation** of SHM.

### Physical Interpretation
- The acceleration is **always opposite** to the displacement.
- The magnitude of acceleration is **maximum** at the amplitude extremes ($x = \pm A$) and **zero** at equilibrium ($x = 0$).
- The motion is **isochronous** — the period is independent of amplitude (for small oscillations).

### Common Pitfalls
1. **Confusing displacement with distance**: Displacement is a vector (has direction); distance is scalar.
2. **Forgetting the negative sign**: Without it, the motion would be unstable (acceleration away from equilibrium).
3. **Assuming all oscillations are SHM**: Only when $F \propto -x$ exactly. Many real oscillations (e.g., large-angle pendulum) are only approximately SHM.

> 📷 **IMAGE PROMPT — SHM-COND-01: Restoring Force Diagram**
> A clear vector diagram showing a mass on a spring at three positions: equilibrium (center), displaced right (positive x), and displaced left (negative x). At each displaced position, show the restoring force vector (F) pointing back toward equilibrium, with length proportional to displacement. Label: equilibrium position (x=0), displacement (x), restoring force (F = -kx). Use a clean textbook style with arrows and labels.

**中文:**
简谐运动的条件可以用两种等价的方式表述——一种用力的形式，一种用加速度的形式。

### 条件1：恢复力与位移成正比
对于系统表现出简谐运动，作用在振荡物体上的合力必须满足：
$$F = -kx$$
其中$k$是正常数（力常数），$x$是偏离平衡位置的位移。负号表示力始终指向平衡位置——它是**恢复力**。

这类似于弹簧的[[胡克定律]]，但更广泛地适用于任何恢复力与位移成线性关系的系统。

### 条件2：加速度与负位移成正比
利用牛顿第二定律（$F = ma$），我们可以将力的条件改写为：
$$a = -\frac{k}{m}x = -\omega^2 x$$
其中$\omega = \sqrt{k/m}$是角频率。这是简谐运动的**定义方程**。

### 物理解释
- 加速度**始终与位移方向相反**。
- 加速度的大小在振幅极值处（$x = \pm A$）**最大**，在平衡位置（$x = 0$）**为零**。
- 运动是**等时的**——周期与振幅无关（对于小振幅振荡）。

### 常见误区
1. **混淆位移和距离**：位移是矢量（有方向）；距离是标量。
2. **忘记负号**：如果没有负号，运动将是不稳定的（加速度远离平衡位置）。
3. **假设所有振荡都是简谐运动**：只有当$F \propto -x$精确成立时才成立。许多实际振荡（例如大角度摆）只是近似简谐运动。

---

# 4. Formulas / 公式

## Defining Equation of SHM

$$a = -\omega^2 x$$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
| ------------- | ------------ | ------------ | ----------- |
| $a$ | Acceleration of the oscillating object | 振荡物体的加速度 | m s⁻² |
| $\omega$ | Angular frequency | 角频率 | rad s⁻¹ |
| $x$ | Displacement from equilibrium | 偏离平衡位置的位移 | m |

## Force-Displacement Relation

$$F = -kx$$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
| ------------- | ------------ | ------------ | ----------- |
| $F$ | Restoring force | 恢复力 | N |
| $k$ | Force constant (spring constant) | 力常数（弹簧常数） | N m⁻¹ |
| $x$ | Displacement from equilibrium | 偏离平衡位置的位移 | m |

## Relationship Between Constants

$$\omega = \sqrt{\frac{k}{m}}$$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
| ------------- | ------------ | ------------ | ----------- |
| $\omega$ | Angular frequency | 角频率 | rad s⁻¹ |
| $k$ | Force constant | 力常数 | N m⁻¹ |
| $m$ | Mass of oscillating object | 振荡物体的质量 | kg |

**Derivation / 推导:**
Starting from Newton's Second Law: $F = ma$
Substitute the restoring force: $-kx = ma$
Rearrange: $a = -\frac{k}{m}x$
Define $\omega^2 = \frac{k}{m}$, giving: $a = -\omega^2 x$

**Conditions / 适用条件:**
- The restoring force must be **linearly proportional** to displacement (Hooke's law regime).
- For pendulums, this holds only for **small angular displacements** ($\theta < 10^\circ$ approximately).
- No damping (friction) is present — this is ideal SHM.
- The system must have a **stable equilibrium position**.

> 📷 **IMAGE PROMPT — SHM-COND-02: Acceleration vs Displacement Graph**
> A graph with displacement (x) on the horizontal axis and acceleration (a) on the vertical axis. Show a straight line passing through the origin with negative slope. Label the slope as $-\omega^2$. Mark points: at x = +A, a = $-\omega^2 A$; at x = -A, a = $+\omega^2 A$; at x = 0, a = 0. Use a clean graph paper style with gridlines and clear axis labels.

---

# 5. Image Prompt / 图片提示

> 📷 **IMAGE PROMPT — SHM-COND-03: Three Systems Showing SHM Conditions**
>
> **English Prompt:**
> A split-panel diagram showing three different oscillating systems that satisfy SHM conditions. Left panel: a mass on a horizontal spring on a frictionless surface, with force vectors. Middle panel: a simple pendulum at small angle, showing the tangential restoring force component. Right panel: a floating object in liquid (buoyancy oscillation), showing displaced volume and restoring force. Each panel should have: equilibrium position marked with dashed line, displacement labeled (x or θ), restoring force vector (F) pointing toward equilibrium. Use a clean educational illustration style with consistent color coding: blue for equilibrium, red for force vectors, green for displacement.
>
> **中文描述:**
> 一个分屏图，显示三种满足简谐运动条件的振荡系统。左面板：水平弹簧上的质量块在无摩擦表面上，带有力矢量。中面板：小角度简单摆，显示切向恢复力分量。右面板：液体中的浮动物体（浮力振荡），显示排开体积和恢复力。每个面板应有：用虚线标记的平衡位置，标注的位移（x或θ），指向平衡位置的恢复力矢量（F）。使用清晰的教育插图风格，颜色编码一致：蓝色表示平衡位置，红色表示力矢量，绿色表示位移。
>
> **Labels Required / 需要标注:**
> * Equilibrium position (平衡位置)
> * Displacement x (位移 x)
> * Restoring force F (恢复力 F)
> * For pendulum: angle θ (角度 θ)
> * For spring: spring constant k (弹簧常数 k)
>
> **Style / 风格:** Textbook vector illustration with clean lines and labels
>
> **Exam Relevance / 考试关联:**
> This diagram helps students recognize that SHM conditions apply to multiple physical systems, a common exam question type where they must identify whether a given system exhibits SHM.

---

# 6. Worked Example / 典型例题

### Example 1: Identifying SHM from a Force-Displacement Graph

### Question / 题目
**English:**
A mass oscillates on a spring. The graph of restoring force $F$ against displacement $x$ is a straight line through the origin with gradient $-50\ \text{N m}^{-1}$. The mass is $0.20\ \text{kg}$.

(a) Show that the motion is simple harmonic.
(b) Calculate the angular frequency $\omega$ of the oscillation.

**中文:**
一个质量块在弹簧上振荡。恢复力$F$与位移$x$的关系图是通过原点、斜率为$-50\ \text{N m}^{-1}$的直线。质量块为$0.20\ \text{kg}$。

(a) 证明该运动是简谐运动。
(b) 计算振荡的角频率$\omega$。

### Solution / 解答

**(a) Proof / 证明:**
The graph shows $F \propto -x$ (linear through origin with negative slope).
This satisfies the condition $F = -kx$ where $k = 50\ \text{N m}^{-1}$.
Since the restoring force is proportional to displacement and opposite in direction, the motion is simple harmonic.

**(b) Calculation / 计算:**
$$\omega = \sqrt{\frac{k}{m}} = \sqrt{\frac{50}{0.20}} = \sqrt{250} = 15.8\ \text{rad s}^{-1}$$

### Final Answer / 最终答案
**Answer:** (a) The force-displacement relationship is linear with negative gradient, satisfying $F = -kx$. (b) $\omega = 15.8\ \text{rad s}^{-1}$
**答案:** (a) 力-位移关系为线性且斜率为负，满足$F = -kx$。 (b) $\omega = 15.8\ \text{rad s}^{-1}$

### Quick Tip / 提示
**English:** In exam questions, always check TWO things: (1) Is the force/acceleration proportional to displacement? (2) Is it directed toward equilibrium (negative sign)? Both are required for SHM.

**中文:** 在考试题目中，始终检查两件事：(1) 力/加速度是否与位移成正比？(2) 是否指向平衡位置（负号）？两者都是简谐运动所必需的。

---

### Example 2: Checking SHM Conditions for a Pendulum

### Question / 题目
**English:**
A simple pendulum of length $L$ has a bob of mass $m$. When displaced by a small angle $\theta$, the restoring force is $F = -mg\sin\theta$.

(a) Explain why this motion is **not** exactly simple harmonic for large angles.
(b) State the condition under which it approximates SHM, and derive the expression for angular frequency.

**中文:**
一个长度为$L$的简单摆，摆锤质量为$m$。当偏离小角度$\theta$时，恢复力为$F = -mg\sin\theta$。

(a) 解释为什么对于大角度，该运动**不是**精确的简谐运动。
(b) 说明在什么条件下它近似为简谐运动，并推导角频率的表达式。

### Solution / 解答

**(a) Explanation / 解释:**
For SHM, we require $F \propto -x$ (linear). Here $F = -mg\sin\theta$, and $\sin\theta \neq \theta$ for large angles. Since $\sin\theta$ is not proportional to $\theta$ (and hence not proportional to displacement $x = L\theta$), the restoring force is not linear — the motion is not exactly SHM.

**(b) Condition and Derivation / 条件和推导:**
For small angles ($\theta < 10^\circ$ or $< 0.17\ \text{rad}$), $\sin\theta \approx \theta$ (in radians).
Then: $F \approx -mg\theta = -mg\frac{x}{L} = -\frac{mg}{L}x$
This is of the form $F = -kx$ with $k = \frac{mg}{L}$.
Therefore: $\omega = \sqrt{\frac{k}{m}} = \sqrt{\frac{g}{L}}$

### Final Answer / 最终答案
**Answer:** (a) For large angles, $\sin\theta \neq \theta$, so $F \not\propto -x$. (b) For small angles ($\theta < 10^\circ$), $\sin\theta \approx \theta$, giving $\omega = \sqrt{g/L}$.
**答案:** (a) 对于大角度，$\sin\theta \neq \theta$，所以$F \not\propto -x$。 (b) 对于小角度（$\theta < 10^\circ$），$\sin\theta \approx \theta$，得到$\omega = \sqrt{g/L}$。

### Quick Tip / 提示
**English:** The "small angle approximation" ($\sin\theta \approx \theta$) is a common exam topic. Remember that $\theta$ must be in **radians** for this approximation to work.

**中文:** "小角度近似"（$\sin\theta \approx \theta$）是常见的考试主题。记住$\theta$必须用**弧度**表示才能使该近似成立。

---

# 7. Flashcards / 闪卡

**Flashcard 1:**
Q (EN): What are the two conditions for a system to exhibit Simple Harmonic Motion?
Q (CN): 系统表现出简谐运动的两个条件是什么？
A (EN): (1) The restoring force (or acceleration) must be directly proportional to the displacement from equilibrium. (2) The restoring force (or acceleration) must always be directed toward the equilibrium position.
A (CN): (1) 恢复力（或加速度）必须与偏离平衡位置的位移成正比。(2) 恢复力（或加速度）必须始终指向平衡位置。

**Flashcard 2:**
Q (EN): Write the defining equation of SHM and explain each symbol.
Q (CN): 写出简谐运动的定义方程并解释每个符号。
A (EN): $a = -\omega^2 x$, where $a$ = acceleration (m s⁻²), $\omega$ = angular frequency (rad s⁻¹), $x$ = displacement from equilibrium (m). The negative sign indicates acceleration is opposite to displacement.
A (CN): $a = -\omega^2 x$，其中$a$ = 加速度（m s⁻²），$\omega$ = 角频率（rad s⁻¹），$x$ = 偏离平衡位置的位移（m）。负号表示加速度与位移方向相反。

**Flashcard 3:**
Q (EN): How is angular frequency $\omega$ related to the force constant $k$ and mass $m$?
Q (CN): 角频率$\omega$与力常数$k$和质量$m$有什么关系？
A (EN): $\omega = \sqrt{k/m}$. This comes from combining $F = -kx$ with Newton's Second Law $F = ma$.
A (CN): $\omega = \sqrt{k/m}$。这来自将$F = -kx$与牛顿第二定律$F = ma$结合。

**Flashcard 4:**
Q (EN): Why is a simple pendulum only approximately SHM?
Q (CN): 为什么简单摆只是近似简谐运动？
A (EN): The restoring force is $F = -mg\sin\theta$. For SHM we need $F \propto -x$ (linear). $\sin\theta \approx \theta$ only for small angles ($<10^\circ$). For large angles, $\sin\theta \neq \theta$, so the motion is not exactly SHM.
A (CN): 恢复力为$F = -mg\sin\theta$。对于简谐运动，我们需要$F \propto -x$（线性）。$\sin\theta \approx \theta$仅对小角度（$<10^\circ$）成立。对于大角度，$\sin\theta \neq \theta$，所以运动不是精确的简谐运动。

**Flashcard 5:**
Q (EN): What is the acceleration of an SHM oscillator at (a) equilibrium and (b) maximum displacement?
Q (CN): 简谐运动振荡器在(a)平衡位置和(b)最大位移处的加速度是多少？
A (EN): (a) At equilibrium ($x = 0$), $a = 0$ (zero acceleration). (b) At maximum displacement ($x = \pm A$), $a = \mp \omega^2 A$ (maximum acceleration, opposite direction to displacement).
A (CN): (a) 在平衡位置（$x = 0$），$a = 0$（加速度为零）。(b) 在最大位移处（$x = \pm A$），$a = \mp \omega^2 A$（加速度最大，方向与位移相反）。

---

# 8. Metadata / 元数据

```yaml
title:
  en: Conditions for Simple Harmonic Motion
  cn: 简谐运动的条件
parent_topic: Simple Harmonic Motion
parent_hub: "[[Simple Harmonic Motion]]"
subject: Physics
syllabus:
  - CAIE 9702
  - Edexcel IAL
level: A2
node_type: leaf_concept
difficulty: intermediate
related_leaf_nodes:
  - "[[Displacement, Velocity and Acceleration in SHM]]"
  - "[[The Simple Pendulum]]"
  - "[[Mass-Spring System]]"
  - "[[Energy in SHM]]"
prerequisites:
  - "[[Equations of Motion (SUVAT)]]"
  - "[[Angular Measures]]"
language: bilingual_en_cn