# Kinetic Energy (KE) / 动能

---

# 1. Overview / 概述

**English:**
Kinetic Energy (KE) is the energy an object possesses due to its motion. This sub-topic covers the definition, formula derivation, and practical applications of KE for objects moving in a straight line. Understanding KE is fundamental to the [[Work-Energy Theorem]] and the broader [[Conservation of Energy]] principle. It connects directly to [[Gravitational Potential Energy (GPE)]] and [[Elastic Potential Energy]] as the three main forms of mechanical energy in A-Level Physics.

**中文:**
动能（KE）是物体由于运动而具有的能量。本子知识点涵盖直线运动物体的动能定义、公式推导和实际应用。理解动能是掌握[[Work-Energy Theorem|功能定理]]和更广泛的[[Conservation of Energy|能量守恒]]原理的基础。它与[[Gravitational Potential Energy (GPE)|重力势能]]和[[Elastic Potential Energy|弹性势能]]直接相关，是A-Level物理中机械能的三种主要形式。

---

# 2. Core Definition / 核心定义

| Term (EN/CN) | Definition (EN) | Definition (CN) |
| ------------ | --------------- | --------------- |
| **Kinetic Energy** / 动能 | The energy an object has due to its motion, equal to half the product of its mass and the square of its velocity. | 物体由于运动而具有的能量，等于其质量与速度平方乘积的一半。 |
| **Translational KE** / 平移动能 | Kinetic energy associated with the linear motion of an object's centre of mass. | 与物体质心直线运动相关的动能。 |
| **Rotational KE** / 转动动能 | Kinetic energy associated with the rotation of an object about an axis (not required at AS level). | 与物体绕轴旋转相关的动能（AS阶段不要求）。 |
| **Non-relativistic KE** / 非相对论动能 | Kinetic energy formula valid when the object's speed is much less than the speed of light ($v \ll c$). | 当物体速度远小于光速时有效的动能公式。 |
| **Work-KE Theorem** / 功能定理 | The net work done on an object equals its change in kinetic energy. | 对物体所做的净功等于其动能的变化量。 |

---

# 3. Key Concepts / 关键概念

**English:**

### The Nature of Kinetic Energy
Kinetic energy is a **scalar quantity** — it has magnitude but no direction. This means:
- KE is always positive (or zero for stationary objects)
- KE depends on the **square** of velocity, so doubling speed quadruples KE
- KE is measured in **joules (J)**

### Derivation from [[Work Done by a Force]]
Consider a constant force $F$ acting on an object of mass $m$, initially at rest, over a displacement $s$:

1. Work done: $W = Fs$
2. From Newton's Second Law: $F = ma$
3. From kinematics: $v^2 = u^2 + 2as$, with $u = 0$: $v^2 = 2as$, so $s = \frac{v^2}{2a}$
4. Substituting: $W = ma \times \frac{v^2}{2a} = \frac{1}{2}mv^2$

This shows that the work done to accelerate an object from rest becomes its kinetic energy.

### Common Pitfalls
- **Confusing KE with momentum**: Momentum ($p = mv$) is a vector; KE ($\frac{1}{2}mv^2$) is a scalar
- **Forgetting the square**: A car at 60 mph has 4× the KE of the same car at 30 mph
- **Mass units**: Always use kg, not g

**中文:**

### 动能的本质
动能是一个**标量**——它有大小但没有方向。这意味着：
- 动能始终为正（静止物体为零）
- 动能取决于速度的**平方**，因此速度加倍会使动能变为四倍
- 动能的单位是**焦耳（J）**

### 从[[Work Done by a Force|力做功]]推导
考虑一个恒力 $F$ 作用在质量为 $m$、初始静止的物体上，位移为 $s$：

1. 做功：$W = Fs$
2. 根据牛顿第二定律：$F = ma$
3. 根据运动学：$v^2 = u^2 + 2as$，其中 $u = 0$：$v^2 = 2as$，所以 $s = \frac{v^2}{2a}$
4. 代入：$W = ma \times \frac{v^2}{2a} = \frac{1}{2}mv^2$

这表明将物体从静止加速所做的功转化为其动能。

### 常见错误
- **混淆动能和动量**：动量（$p = mv$）是矢量；动能（$\frac{1}{2}mv^2$）是标量
- **忘记平方**：以60 mph行驶的汽车的动能是同一辆车以30 mph行驶时的4倍
- **质量单位**：始终使用kg，而不是g

---

# 4. Formulas / 公式

## Primary Formula / 主要公式

$$E_k = \frac{1}{2}mv^2$$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
| ------------- | ------------ | ------------ | ----------- |
| $E_k$ | Kinetic energy | 动能 | J (joules) |
| $m$ | Mass of the object | 物体的质量 | kg |
| $v$ | Speed of the object | 物体的速度 | m s⁻¹ |

## Alternative Form / 另一种形式

$$E_k = \frac{p^2}{2m}$$

Where $p = mv$ is the momentum. This form is useful when momentum is known.

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
| ------------- | ------------ | ------------ | ----------- |
| $p$ | Momentum | 动量 | kg m s⁻¹ |

**Derivation / 推导:**
$$E_k = \frac{1}{2}mv^2 = \frac{1}{2}m\left(\frac{p}{m}\right)^2 = \frac{p^2}{2m}$$

**Conditions / 适用条件:**
- Object speed $v \ll c$ (much less than speed of light)
- Non-relativistic regime
- Translational motion only (no rotation)

> 📷 **IMAGE PROMPT — KE01: Kinetic Energy vs Speed Graph**
>
> **English Prompt:**
> A clean, textbook-style graph showing kinetic energy (y-axis, in joules) plotted against speed (x-axis, in m/s) for three different masses (m, 2m, 3m). Each curve is a parabola (quadratic relationship). The graph should have clear axis labels with units, a legend distinguishing the three masses, and gridlines. Use a white background with black lines and colored curves (blue for m, red for 2m, green for 3m). Include a callout box highlighting that doubling speed quadruples KE.
>
> **中文描述:**
> 一个清晰的教科书式图表，显示三种不同质量（m、2m、3m）的动能（y轴，单位焦耳）与速度（x轴，单位m/s）的关系。每条曲线都是抛物线（二次关系）。图表应有清晰的轴标签和单位、区分三种质量的图例以及网格线。使用白色背景、黑色线条和彩色曲线（m为蓝色，2m为红色，3m为绿色）。包含一个标注框，强调速度加倍使动能变为四倍。
>
> **Labels Required / 需要标注:**
> * x-axis: Speed / v (m s⁻¹)
> * y-axis: Kinetic Energy / E_k (J)
> * Legend: m, 2m, 3m
> * Callout: "Doubling v → 4× KE"
>
> **Style / 风格:** Textbook vector graph
>
> **Exam Relevance / 考试关联:**
> This graph is essential for understanding the quadratic relationship between KE and speed, a common exam question topic.

---

# 5. Image Prompt / 图片提示

> 📷 **IMAGE PROMPT — KE02: Work-Energy Demonstration**
>
> **English Prompt:**
> A 3D-rendered physics illustration showing a block of mass m being pushed by a constant force F across a frictionless horizontal surface. The block starts from rest at position A and reaches position B after displacement s. Show velocity vectors increasing in length from A to B. Include a side panel showing the energy transformation: Work Done (W = Fs) converting to Kinetic Energy (E_k = ½mv²). Use a clean, modern style with labeled arrows, a light blue background, and the block in dark grey. Include a speedometer-like indicator showing v increasing.
>
> **中文描述:**
> 一个3D渲染的物理插图，显示质量为m的物块在无摩擦水平面上受到恒力F推动。物块从A位置静止开始，经过位移s后到达B位置。显示从A到B速度矢量长度逐渐增加。包含一个侧面板，显示能量转换：做功（W = Fs）转化为动能（E_k = ½mv²）。使用干净现代的风格，带有标注箭头、浅蓝色背景和深灰色物块。包含一个类似速度表的指示器显示v增加。
>
> **Labels Required / 需要标注:**
> * Force arrow: F
> * Displacement: s
> * Initial velocity: u = 0
> * Final velocity: v
> * Energy panel: W → E_k
>
> **Style / 风格:** 3D render, modern textbook illustration
>
> **Exam Relevance / 考试关联:**
> This visual helps students connect the [[Work-Energy Theorem]] to the derivation of KE, a common exam topic.

---

# 6. Worked Example / 典型例题

### Example 1: Basic KE Calculation

### Question / 题目
**English:** A car of mass 1200 kg is travelling at 25 m s⁻¹. Calculate its kinetic energy.

**中文:** 一辆质量为1200 kg的汽车以25 m s⁻¹的速度行驶。计算其动能。

### Solution / 解答

**Step 1:** Identify known values
- $m = 1200 \text{ kg}$
- $v = 25 \text{ m s}^{-1}$

**Step 2:** Apply the formula
$$E_k = \frac{1}{2}mv^2 = \frac{1}{2} \times 1200 \times (25)^2$$

**Step 3:** Calculate
$$E_k = 600 \times 625 = 375\,000 \text{ J} = 3.75 \times 10^5 \text{ J}$$

### Final Answer / 最终答案
**Answer:** $3.75 \times 10^5$ J (or 375 kJ) **答案:** $3.75 \times 10^5$ J（或375 kJ）

### Quick Tip / 提示
Always square the velocity **before** multiplying by mass. A common mistake is to do $\frac{1}{2} \times 1200 \times 25$ and then square the result — this gives the wrong answer.

---

### Example 2: Speed from KE

### Question / 题目
**English:** A cyclist and bicycle have a total mass of 85 kg. Their kinetic energy is 1700 J. Calculate their speed.

**中文:** 骑自行车的人和自行车总质量为85 kg，动能为1700 J。计算他们的速度。

### Solution / 解答

**Step 1:** Rearrange the formula
$$E_k = \frac{1}{2}mv^2 \implies v^2 = \frac{2E_k}{m}$$

**Step 2:** Substitute values
$$v^2 = \frac{2 \times 1700}{85} = \frac{3400}{85} = 40$$

**Step 3:** Take square root
$$v = \sqrt{40} = 6.32 \text{ m s}^{-1}$$

### Final Answer / 最终答案
**Answer:** 6.32 m s⁻¹ **答案:** 6.32 m s⁻¹

### Quick Tip / 提示
When rearranging for speed, remember to take the **square root** at the end. Many students forget this step and leave the answer as $v^2$.

---

# 7. Flashcards / 闪卡

**Flashcard 1:**
Q (EN): What is the formula for kinetic energy?
Q (CN): 动能的公式是什么？
A (EN): $E_k = \frac{1}{2}mv^2$, where m is mass in kg and v is speed in m s⁻¹.
A (CN): $E_k = \frac{1}{2}mv^2$，其中m是质量（kg），v是速度（m s⁻¹）。

**Flashcard 2:**
Q (EN): If the speed of an object doubles, what happens to its kinetic energy?
Q (CN): 如果物体的速度加倍，其动能会如何变化？
A (EN): The kinetic energy quadruples (increases by a factor of 4), because KE ∝ v².
A (CN): 动能变为原来的四倍（增加4倍），因为KE ∝ v²。

**Flashcard 3:**
Q (EN): Is kinetic energy a scalar or vector quantity?
Q (CN): 动能是标量还是矢量？
A (EN): Kinetic energy is a scalar quantity — it has magnitude but no direction.
A (CN): 动能是标量——它有大小但没有方向。

**Flashcard 4:**
Q (EN): What is the alternative formula for KE in terms of momentum?
Q (CN): 用动量表示的动能公式是什么？
A (EN): $E_k = \frac{p^2}{2m}$, where p = mv is the momentum.
A (CN): $E_k = \frac{p^2}{2m}$，其中p = mv是动量。

**Flashcard 5:**
Q (EN): What is the relationship between work done and kinetic energy?
Q (CN): 做功和动能之间有什么关系？
A (EN): The net work done on an object equals its change in kinetic energy (Work-KE Theorem).
A (CN): 对物体所做的净功等于其动能的变化量（功能定理）。

---

# 8. Metadata / 元数据

```yaml
title:
  en: Kinetic Energy (KE)
  cn: 动能
parent_topic: Kinetic Energy and Potential Energy
parent_hub: "[[Kinetic Energy and Potential Energy]]"
subject: Physics
syllabus:
  - CAIE 9702
  - Edexcel IAL
level: AS
node_type: leaf_concept
difficulty: intermediate
related_leaf_nodes:
  - "[[Gravitational Potential Energy (GPE)]]"
  - "[[Elastic Potential Energy]]"
  - "[[Work-Energy Theorem]]"
prerequisites:
  - "[[Work Done by a Force]]"
related_topics:
  - "[[Conservation of Energy]]"
language: bilingual_en_cn