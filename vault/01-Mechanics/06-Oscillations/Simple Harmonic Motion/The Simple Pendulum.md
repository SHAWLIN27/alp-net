# 1. Overview / 概述

**English:**
The simple pendulum is one of the most classic examples of [[Simple Harmonic Motion]] in A-Level Physics. This sub-topic explores how a small, heavy bob swinging on a light, inextensible string approximates SHM for small angular displacements. You will derive the formula for its time period, understand the factors that affect it, and learn how to use the pendulum to determine the acceleration due to gravity ($g$). This is a cornerstone experiment in mechanics, linking [[Conditions for SHM]] with practical measurement.

**中文:**
单摆是A-Level物理中[[简谐运动]]最经典的例子之一。本子知识点探讨了一个在轻质、不可伸长的绳子上摆动的小而重的摆锤，在小角度位移下如何近似为简谐运动。你将推导其周期公式，理解影响周期的因素，并学习如何利用单摆测定重力加速度 ($g$)。这是力学中的基石实验，将[[简谐运动的条件]]与实际测量联系起来。

---

# 2. Core Definition / 核心定义

| Term (EN/CN) | Definition (EN) | Definition (CN) |
| ------------ | --------------- | --------------- |
| **Simple Pendulum** / 单摆 | A point mass suspended from a fixed point by a light, inextensible string, which oscillates under gravity. | 一个由轻质、不可伸长的绳子悬挂在固定点上的质点，在重力作用下摆动。 |
| **Restoring Force** / 回复力 | The component of the weight of the bob acting perpendicular to the string, directed towards the equilibrium position. | 摆锤重力的垂直于绳子的分量，方向指向平衡位置。 |
| **Small Angle Approximation** / 小角度近似 | For small angular displacements ($\theta \ll 1$ rad), $\sin\theta \approx \theta$, allowing the motion to be treated as SHM. | 对于小角度位移 ($\theta \ll 1$ rad)，$\sin\theta \approx \theta$，使运动可被视为简谐运动。 |
| **Time Period ($T$)** / 周期 | The time taken for one complete oscillation (to-and-fro motion). | 完成一次全振动（来回运动）所需的时间。 |
| **Amplitude ($\theta_0$)** / 振幅 | The maximum angular displacement from the equilibrium position. | 从平衡位置出发的最大角位移。 |
| **Length ($L$)** / 摆长 | The distance from the pivot point to the centre of mass of the bob. | 从悬挂点到摆锤质心的距离。 |

---

# 3. Key Concepts / 关键概念

**English:**
The simple pendulum is a physical system that demonstrates [[Conditions for SHM]] under specific conditions. Consider a bob of mass $m$ suspended by a string of length $L$. When displaced by a small angle $\theta$ from the vertical, the restoring force is the component of the bob's weight acting tangentially to the arc: $F = -mg\sin\theta$.

For small angles ($\theta < 10^\circ$ or $\theta < 0.175$ rad), we use the **small angle approximation**: $\sin\theta \approx \theta$ (where $\theta$ is in radians). This gives $F \approx -mg\theta$. Since the arc length $s = L\theta$, we can write $F \approx -\frac{mg}{L}s$. This is of the form $F = -kx$, where $k = \frac{mg}{L}$, confirming that the motion is SHM.

The angular frequency $\omega$ is then $\omega = \sqrt{\frac{k}{m}} = \sqrt{\frac{g}{L}}$, leading to the famous period formula $T = 2\pi\sqrt{\frac{L}{g}}$.

**Key points to remember:**
* The period is **independent of mass** — a heavier bob does not swing faster.
* The period is **independent of amplitude** (for small angles) — this is the property of isochronism.
* The period depends only on **length** and **gravitational field strength**.
* The motion is **not** SHM for large amplitudes — the small angle approximation breaks down.

**Common pitfalls:**
* Forgetting to convert degrees to radians when using the small angle approximation.
* Confusing the length $L$ with the amplitude.
* Assuming the period formula applies for any amplitude.

**中文:**
单摆是一个在特定条件下展示[[简谐运动的条件]]的物理系统。考虑一个质量为 $m$ 的摆锤，由长度为 $L$ 的绳子悬挂。当从竖直方向偏离一个小角度 $\theta$ 时，回复力是摆锤重力沿圆弧切线方向的分量：$F = -mg\sin\theta$。

对于小角度 ($\theta < 10^\circ$ 或 $\theta < 0.175$ rad)，我们使用**小角度近似**：$\sin\theta \approx \theta$（其中 $\theta$ 以弧度为单位）。这给出 $F \approx -mg\theta$。由于弧长 $s = L\theta$，我们可以写成 $F \approx -\frac{mg}{L}s$。这是 $F = -kx$ 的形式，其中 $k = \frac{mg}{L}$，证实了运动是简谐运动。

角频率 $\omega$ 为 $\omega = \sqrt{\frac{k}{m}} = \sqrt{\frac{g}{L}}$，从而得出著名的周期公式 $T = 2\pi\sqrt{\frac{L}{g}}$。

**需要记住的关键点：**
* 周期**与质量无关**——更重的摆锤不会摆动得更快。
* 周期**与振幅无关**（对于小角度）——这是等时性。
* 周期仅取决于**摆长**和**重力场强度**。
* 对于大振幅，运动**不是**简谐运动——小角度近似失效。

**常见错误：**
* 使用小角度近似时忘记将度数转换为弧度。
* 混淆摆长 $L$ 和振幅。
* 假设周期公式适用于任何振幅。

---

# 4. Formulas / 公式

## Restoring Force / 回复力

$$ F = -mg\sin\theta $$

For small angles: $F \approx -mg\theta$

## Time Period / 周期

$$ T = 2\pi\sqrt{\frac{L}{g}} $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
| ------------- | ------------ | ------------ | ----------- |
| $T$ | Time period | 周期 | s |
| $L$ | Length of pendulum | 摆长 | m |
| $g$ | Acceleration due to gravity | 重力加速度 | m s$^{-2}$ |

## Angular Frequency / 角频率

$$ \omega = \sqrt{\frac{g}{L}} $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
| ------------- | ------------ | ------------ | ----------- |
| $\omega$ | Angular frequency | 角频率 | rad s$^{-1}$ |

## Displacement as a Function of Time / 位移随时间变化

$$ \theta(t) = \theta_0 \cos(\omega t + \phi) $$

Where $\theta_0$ is the angular amplitude and $\phi$ is the phase constant.

**Derivation / 推导:**
1. Restoring force: $F = -mg\sin\theta \approx -mg\theta$ (for small $\theta$)
2. Using $F = ma$ and $a = L\alpha$ (tangential acceleration = $L \times$ angular acceleration): $mL\frac{d^2\theta}{dt^2} = -mg\theta$
3. Simplify: $\frac{d^2\theta}{dt^2} = -\frac{g}{L}\theta$
4. This is the SHM equation with $\omega^2 = \frac{g}{L}$, so $\omega = \sqrt{\frac{g}{L}}$
5. Therefore: $T = \frac{2\pi}{\omega} = 2\pi\sqrt{\frac{L}{g}}$

**Conditions / 适用条件:**
* Small angular amplitude ($\theta < 10^\circ$ or $\theta < 0.175$ rad)
* Light, inextensible string (mass of string negligible)
* Point mass bob (size of bob negligible compared to $L$)
* No air resistance or friction at the pivot

> 📷 **IMAGE PROMPT — SP01: Simple Pendulum Force Diagram**
>
> **English Prompt:**
> A clean, textbook-style vector diagram of a simple pendulum at a small angular displacement $\theta$. Show a bob of mass $m$ hanging from a fixed pivot by a string of length $L$. Draw and label the forces: weight $mg$ acting vertically downward, tension $T$ along the string, and the restoring force component $mg\sin\theta$ perpendicular to the string. Show the equilibrium position as a dashed vertical line. Use a light blue background with clear black labels. Include a small angle indicator arc showing $\theta$.
>
> **中文描述:**
> 一个干净、教科书风格的矢量图，展示一个小角度位移 $\theta$ 下的单摆。显示一个质量为 $m$ 的摆锤，通过长度为 $L$ 的绳子从固定悬挂点垂下。绘制并标注力：竖直向下的重力 $mg$，沿绳子的张力 $T$，以及垂直于绳子的回复力分量 $mg\sin\theta$。用虚线垂直线显示平衡位置。使用浅蓝色背景和清晰的黑色标签。包含一个显示 $\theta$ 的小角度指示弧。
>
> **Labels Required / 需要标注:**
> * Pivot point / 悬挂点
> * String length $L$ / 摆长 $L$
> * Bob mass $m$ / 摆锤质量 $m$
> * Weight $mg$ / 重力 $mg$
> * Tension $T$ / 张力 $T$
> * Restoring force $mg\sin\theta$ / 回复力 $mg\sin\theta$
> * Angular displacement $\theta$ / 角位移 $\theta$
> * Equilibrium position (dashed) / 平衡位置（虚线）
>
> **Style / 风格:** Textbook vector diagram
>
> **Exam Relevance / 考试关联:**
> Essential for understanding the derivation of the period formula and identifying the restoring force in exam questions.

---

# 5. Image Prompt / 图片提示

> 📷 **IMAGE PROMPT — SP02: Period vs Length Graph**
>
> **English Prompt:**
> A graph showing the relationship between the time period $T$ and the length $L$ of a simple pendulum. Plot $T$ on the y-axis and $L$ on the x-axis. Show a curve following $T = 2\pi\sqrt{L/g}$ for $g = 9.81$ m s$^{-2}$. Include data points with error bars to suggest experimental results. Add a second graph inset showing $T^2$ vs $L$ as a straight line through the origin, with gradient $4\pi^2/g$. Use a clean white background with gridlines. Labels in black serif font.
>
> **中文描述:**
> 一张展示单摆周期 $T$ 与摆长 $L$ 关系的图表。在 y 轴上绘制 $T$，在 x 轴上绘制 $L$。显示 $g = 9.81$ m s$^{-2}$ 时 $T = 2\pi\sqrt{L/g}$ 的曲线。包含带有误差棒的数据点以暗示实验结果。添加一个内嵌图，显示 $T^2$ 与 $L$ 的关系为一条通过原点的直线，斜率为 $4\pi^2/g$。使用干净的白色背景和网格线。标签使用黑色衬线字体。
>
> **Labels Required / 需要标注:**
> * $T$ / s (y-axis) / $T$ / 秒（y轴）
> * $L$ / m (x-axis) / $L$ / 米（x轴）
> * $T = 2\pi\sqrt{L/g}$ / $T = 2\pi\sqrt{L/g}$
> * Experimental data points / 实验数据点
> * Error bars / 误差棒
> * Inset: $T^2$ vs $L$ / 内嵌图：$T^2$ 与 $L$
> * Gradient = $4\pi^2/g$ / 斜率 = $4\pi^2/g$
>
> **Style / 风格:** Scientific graph with experimental data
>
> **Exam Relevance / 考试关联:**
> This graph is commonly used in practical exam questions to determine $g$ from experimental pendulum data.

---

# 6. Worked Example / 典型例题

### Example 1: Finding the Period / 例题1：求周期

**English:**
A simple pendulum of length 1.20 m is set oscillating with a small amplitude on Earth ($g = 9.81$ m s$^{-2}$). Calculate:
a) The time period of the pendulum.
b) The length of a pendulum on the Moon ($g = 1.62$ m s$^{-2}$) that would have the same period.

**中文:**
一个摆长为1.20 m的单摆在地球上以小振幅摆动（$g = 9.81$ m s$^{-2}$）。计算：
a) 单摆的周期。
b) 在月球上（$g = 1.62$ m s$^{-2}$）具有相同周期的单摆的摆长。

### Solution / 解答

**a) Time period on Earth / 地球上的周期:**

$$ T = 2\pi\sqrt{\frac{L}{g}} = 2\pi\sqrt{\frac{1.20}{9.81}} $$

$$ T = 2\pi \times 0.3498 = 2.20 \text{ s} $$

**b) Length on Moon / 月球上的摆长:**

Since $T$ is the same, $T = 2\pi\sqrt{\frac{L_{\text{Earth}}}{g_{\text{Earth}}}} = 2\pi\sqrt{\frac{L_{\text{Moon}}}{g_{\text{Moon}}}}$

Therefore: $\frac{L_{\text{Earth}}}{g_{\text{Earth}}} = \frac{L_{\text{Moon}}}{g_{\text{Moon}}}$

$$ L_{\text{Moon}} = L_{\text{Earth}} \times \frac{g_{\text{Moon}}}{g_{\text{Earth}}} = 1.20 \times \frac{1.62}{9.81} = 0.198 \text{ m} $$

### Final Answer / 最终答案

**Answer:** a) $T = 2.20$ s, b) $L = 0.198$ m
**答案:** a) $T = 2.20$ 秒, b) $L = 0.198$ 米

### Quick Tip / 提示

**English:** When comparing pendulums in different gravitational fields, remember that $T \propto \sqrt{L/g}$. If $T$ is constant, then $L \propto g$.

**中文:** 比较不同重力场中的单摆时，记住 $T \propto \sqrt{L/g}$。如果 $T$ 恒定，则 $L \propto g$。

---

### Example 2: Determining $g$ from Experimental Data / 例题2：从实验数据求 $g$

**English:**
In an experiment, a student measures the period of a simple pendulum for different lengths. The results are:

| $L$ (m) | $T$ (s) |
| ------- | ------- |
| 0.40    | 1.27    |
| 0.60    | 1.55    |
| 0.80    | 1.79    |
| 1.00    | 2.01    |

Plot a suitable graph to determine the value of $g$.

**中文:**
在一个实验中，学生测量了不同摆长下单摆的周期。结果如下：

| $L$ (m) | $T$ (s) |
| ------- | ------- |
| 0.40    | 1.27    |
| 0.60    | 1.55    |
| 0.80    | 1.79    |
| 1.00    | 2.01    |

绘制合适的图表以确定 $g$ 的值。

### Solution / 解答

**Step 1: Linearise the equation / 步骤1：线性化方程**

$$ T = 2\pi\sqrt{\frac{L}{g}} \implies T^2 = \frac{4\pi^2}{g}L $$

This is of the form $y = mx$, where $y = T^2$, $x = L$, and gradient $m = 4\pi^2/g$.

**Step 2: Calculate $T^2$ values / 步骤2：计算 $T^2$ 值**

| $L$ (m) | $T$ (s) | $T^2$ (s$^2$) |
| ------- | ------- | -------------- |
| 0.40    | 1.27    | 1.61           |
| 0.60    | 1.55    | 2.40           |
| 0.80    | 1.79    | 3.20           |
| 1.00    | 2.01    | 4.04           |

**Step 3: Plot $T^2$ vs $L$ and find gradient / 步骤3：绘制 $T^2$ 与 $L$ 的图并求斜率**

Gradient $m = \frac{\Delta T^2}{\Delta L} = \frac{4.04 - 1.61}{1.00 - 0.40} = \frac{2.43}{0.60} = 4.05$ s$^2$ m$^{-1}$

**Step 4: Calculate $g$ / 步骤4：计算 $g$**

$$ m = \frac{4\pi^2}{g} \implies g = \frac{4\pi^2}{m} = \frac{4\pi^2}{4.05} = 9.75 \text{ m s}^{-2} $$

### Final Answer / 最终答案

**Answer:** $g = 9.75$ m s$^{-2}$
**答案:** $g = 9.75$ 米/秒$^2$

### Quick Tip / 提示

**English:** Always plot $T^2$ against $L$ (not $T$ against $L$) to get a straight line. The gradient gives $4\pi^2/g$, from which you can calculate $g$.

**中文:** 始终绘制 $T^2$ 与 $L$ 的关系图（而不是 $T$ 与 $L$）以获得直线。斜率给出 $4\pi^2/g$，由此可以计算 $g$。

---

# 7. Flashcards / 闪卡

**Flashcard 1:**
Q (EN): What is the condition for a simple pendulum to exhibit SHM?
Q (CN): 单摆表现出简谐运动的条件是什么？
A (EN): The angular displacement must be small ($\theta < 10^\circ$ or $\theta < 0.175$ rad) so that $\sin\theta \approx \theta$.
A (CN): 角位移必须很小（$\theta < 10^\circ$ 或 $\theta < 0.175$ rad），使得 $\sin\theta \approx \theta$。

**Flashcard 2:**
Q (EN): State the formula for the time period of a simple pendulum.
Q (CN): 写出单摆周期的公式。
A (EN): $T = 2\pi\sqrt{\frac{L}{g}}$
A (CN): $T = 2\pi\sqrt{\frac{L}{g}}$

**Flashcard 3:**
Q (EN): What factors does the period of a simple pendulum depend on?
Q (CN): 单摆的周期取决于哪些因素？
A (EN): The period depends only on the length $L$ and the gravitational field strength $g$. It is independent of the mass and amplitude (for small angles).
A (CN): 周期仅取决于摆长 $L$ 和重力场强度 $g$。它与质量和振幅无关（对于小角度）。

**Flashcard 4:**
Q (EN): How can you determine $g$ using a simple pendulum experiment?
Q (CN): 如何利用单摆实验测定 $g$？
A (EN): Measure $T$ for different $L$, plot $T^2$ against $L$, find the gradient $m$, then $g = 4\pi^2/m$.
A (CN): 测量不同 $L$ 下的 $T$，绘制 $T^2$ 与 $L$ 的关系图，求斜率 $m$，则 $g = 4\pi^2/m$。

**Flashcard 5:**
Q (EN): What is the restoring force in a simple pendulum?
Q (CN): 单摆中的回复力是什么？
A (EN): The component of the bob's weight acting perpendicular to the string: $mg\sin\theta$.
A (CN): 摆锤重力垂直于绳子的分量：$mg\sin\theta$。

---

# 8. Metadata / 元数据

```yaml
title:
  en: The Simple Pendulum
  cn: 单摆
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
  - "[[Conditions for SHM]]"
  - "[[Displacement, Velocity and Acceleration in SHM]]"
  - "[[Mass-Spring System]]"
  - "[[Energy in SHM]]"
prerequisites:
  - "[[Equations of Motion (SUVAT)]]"
  - "[[Angular Measures]]"
language: bilingual_en_cn